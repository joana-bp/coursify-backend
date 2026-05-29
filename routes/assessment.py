"""
routes/assessment.py
====================
GET  /api/assessment/questions          — returns a randomized assessment set
POST /api/assessment/submit             — scores answers, runs ML, returns recommendations
GET  /api/assessment/results/latest     — returns the most recent result for the logged-in user
GET  /api/assessment/results/history    — returns all past results (newest first, capped at 20)

ML Feature Schema (matches career_data.csv used for model training):
  Aptitude  : Math_Score, Science_Score, Programming_Skill,
              Communication_Skill, Logical_Ability
  RIASEC    : R_score, I_score, A_score, S_score, E_score, C_score
  Target    : Career  → one of 6 classes:
              Accountant | Data Scientist | Doctor |
              Entrepreneur | Software Engineer | Teacher

Training data ranges (verified from career_data.csv, n=2400):
  Math_Score          : 60–97   (integer)
  Science_Score       : 60–97   (integer)
  Programming_Skill   :  2–5    (integer)
  Communication_Skill :  2–5    (integer)
  Logical_Ability     :  2–5    (integer)
  R_score             :  0–8    (integer)
  I_score             :  0–10   (integer)
  A_score             :  0–8    (integer)
  S_score             :  0–10   (integer)
  E_score             :  0–10   (integer)
  C_score             :  0–10   (integer)
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Any, Optional
from datetime import datetime
import random

from bson import ObjectId
from database import db
from routes.auth import get_current_user
from ml.predictor import get_top5_recommendations

router = APIRouter()

# ── Collections ──────────────────────────────────────────────────────────────
riasec_col      = db["questions_riasec"]
aptitude_col    = db["questions_aptitude"]
results_col     = db["assessment_results"]

# ── Helpers ──────────────────────────────────────────────────────────────────

def serialize(doc: dict) -> dict:
    doc["_id"] = str(doc["_id"])
    return doc

async def random_sample(collection, query: dict, n: int) -> list:
    docs = await collection.find(query).to_list(length=None)
    if len(docs) < n:
        raise HTTPException(
            status_code=500,
            detail=(
                f"Not enough questions in pool. "
                f"Need {n}, found {len(docs)}. Query: {query}"
            ),
        )
    return [serialize(d) for d in random.sample(docs, n)]


# ── GET /api/assessment/questions ────────────────────────────────────────────
# Question pool breakdown:
#   RIASEC    : 6 codes × 6 questions = 36 questions  (Likert 1–5)
#   Aptitude  : 5 subjects × 3 difficulties × 4 questions = 60 questions (MCQ)
#     subjects: math | science | programming | english (→ Communication_Skill)
#               abstract (→ Logical_Ability)
#
# Subject → ML feature mapping:
#   math        → Math_Score
#   science     → Science_Score
#   programming → Programming_Skill
#   english     → Communication_Skill
#   abstract    → Logical_Ability

@router.get("/questions")
async def get_questions(current_user=Depends(get_current_user)):

    # ── RIASEC ───────────────────────────────────────────────────────────────
    riasec_codes = [
        "realistic", "investigative", "artistic",
        "social", "enterprising", "conventional",
    ]
    riasec = []
    for code in riasec_codes:
        samples = await random_sample(
            riasec_col, {"subcategory": code, "active": True}, 6
        )
        riasec.extend(samples)
    random.shuffle(riasec)

    # ── Aptitude ─────────────────────────────────────────────────────────────
    aptitude_subjects = ["math", "science", "programming", "english", "abstract"]
    aptitude: dict[str, list] = {}

    for subject in aptitude_subjects:
        subject_qs: list = []
        for difficulty in ["easy", "medium", "hard"]:
            samples = await random_sample(
                aptitude_col,
                {"subject": subject, "difficulty": difficulty, "active": True},
                4,
            )
            subject_qs.extend(samples)
        random.shuffle(subject_qs)
        aptitude[subject] = subject_qs

    return {"riasec": riasec, "aptitude": aptitude}


# ── POST /api/assessment/submit ──────────────────────────────────────────────

class SubmitRequest(BaseModel):
    riasec_answers:   dict   # { question_id: 1–5 }
    aptitude_answers: dict   # { question_id: "A" | "B" | "C" | "D" }


# ── Rescaling helpers ─────────────────────────────────────────────────────────
#
# The StandardScaler saved at training time was fit on the raw training values,
# so inference inputs must match those exact ranges.  Verified ranges from
# career_data.csv (n=2400):
#
#   Math_Score / Science_Score : 60–97
#   Programming_Skill          :  2–5
#   Communication_Skill        :  2–5
#   Logical_Ability            :  2–5
#   RIASEC *_score             :  0–10  (R and A observed max = 8 in training,
#                                        but 0–10 is the intended scale)
#
# Assessment produces percentage-correct (0–100 %) for all aptitude subjects.
# These must be rescaled before the scaler sees them.

def _pct_to_range(pct: float, lo: float, hi: float) -> float:
    """
    Linear map: 0 % → lo, 100 % → hi.

    Examples
    --------
    _pct_to_range(0,   60, 97) → 60.0
    _pct_to_range(100, 60, 97) → 97.0
    _pct_to_range(50,   2,  5) →  3.5
    """
    return round(lo + (pct / 100.0) * (hi - lo), 4)


@router.post("/submit")
async def submit_assessment(
    data: SubmitRequest,
    current_user=Depends(get_current_user),
):

    # ── 1. RIASEC — average Likert score per code, rescaled to 0–10 ──────────
    #
    #    Training data uses integer RIASEC scores on a 0–10 scale.
    #    We collect 6 Likert-1–5 items per code and multiply the mean by 2:
    #       riasec_score = mean(raw 1–5 scores) × 2   → range [2, 10]
    #
    #    Notes on out-of-distribution edges:
    #      • Low end : min producible = 1×2 = 2 ; training min = 0.
    #        Gap of 2 points — minor OOD, acceptable.
    #      • High end: max producible = 5×2 = 10 ; training max for R and A = 8.
    #        Scores of 9–10 on R/A are OOD by 1–2 units. This is a data
    #        artefact (those codes happened not to reach 10 in the training
    #        set); the impact is small but worth noting if model accuracy on
    #        highly-Realistic or highly-Artistic profiles is reviewed later.

    riasec_oids = [ObjectId(qid) for qid in data.riasec_answers.keys()]
    riasec_docs = await riasec_col.find({"_id": {"$in": riasec_oids}}).to_list(length=None)

    riasec_buckets: dict[str, list[int]] = {
        code: []
        for code in ["realistic", "investigative", "artistic", "social", "enterprising", "conventional"]
    }
    for doc in riasec_docs:
        code  = doc["subcategory"]
        score = data.riasec_answers[str(doc["_id"])]
        riasec_buckets[code].append(score)

    code_key_map = {
        "realistic":     "R_score",
        "investigative": "I_score",
        "artistic":      "A_score",
        "social":        "S_score",
        "enterprising":  "E_score",
        "conventional":  "C_score",
    }
    riasec_scores: dict[str, float] = {}
    for code, scores in riasec_buckets.items():
        if scores:
            avg_likert = sum(scores) / len(scores)   # 1–5
            scaled     = round(avg_likert * 2, 4)    # 2–10
        else:
            scaled = 5.0                             # neutral fallback
        riasec_scores[code_key_map[code]] = scaled

    # ── 2. Aptitude — percentage correct per subject ─────────────────────────

    aptitude_oids = [ObjectId(qid) for qid in data.aptitude_answers.keys()]
    aptitude_docs = await aptitude_col.find({"_id": {"$in": aptitude_oids}}).to_list(length=None)

    subject_tally: dict[str, dict] = {
        s: {"correct": 0, "total": 0}
        for s in ["math", "science", "programming", "english", "abstract"]
    }
    for doc in aptitude_docs:
        subject = doc["subject"]
        if subject not in subject_tally:
            continue
        given  = data.aptitude_answers[str(doc["_id"])]
        subject_tally[subject]["total"]   += 1
        subject_tally[subject]["correct"] += int(given == doc["correct_answer"])

    aptitude_pct: dict[str, float] = {
        subj: round(v["correct"] / v["total"] * 100, 1) if v["total"] else 0.0
        for subj, v in subject_tally.items()
    }

    # ── 3. Rescale aptitude percentages to match training data ranges ─────────
    #
    #    The StandardScaler was fit on the raw training values listed above.
    #    Sending raw 0–100 % scores to the scaler produces heavily
    #    out-of-distribution inputs and degrades prediction quality:
    #
    #    Feature               Assessment (old)   Training range   Fix
    #    --------------------  -----------------  ---------------  ------
    #    Math_Score            0–100 %  ← WRONG   60–97            60 + pct/100 × 37
    #    Science_Score         0–100 %  ← WRONG   60–97            60 + pct/100 × 37
    #    Programming_Skill     0–100 %  ← WRONG    2–5              2 + pct/100 ×  3
    #    Communication_Skill   0–100 %  ← WRONG    2–5              2 + pct/100 ×  3
    #    Logical_Ability       0–100 %  ← WRONG    2–5              2 + pct/100 ×  3
    #
    #    The linear map _pct_to_range(pct, lo, hi) implements this exactly.

    aptitude_features: dict[str, float] = {
        # Academic scores — map 0–100 % onto 60–97
        "Math_Score":          _pct_to_range(aptitude_pct["math"],        lo=60, hi=97),
        "Science_Score":       _pct_to_range(aptitude_pct["science"],     lo=60, hi=97),
        # Skill ratings — map 0–100 % onto 2–5
        "Programming_Skill":   _pct_to_range(aptitude_pct["programming"], lo=2,  hi=5),
        "Communication_Skill": _pct_to_range(aptitude_pct["english"],     lo=2,  hi=5),
        "Logical_Ability":     _pct_to_range(aptitude_pct["abstract"],    lo=2,  hi=5),
    }

    # ── 4. Run ML model ──────────────────────────────────────────────────────
    #    predictor receives the 11 features the model was trained on,
    #    now all within their training-data ranges.
    recommendations = get_top5_recommendations(
        academic=aptitude_features,   # 5 keys — matches predictor.py param name
        riasec=riasec_scores,         # 6 keys — matches predictor.py param name
    )

    # ── 5. Persist everything ────────────────────────────────────────────────
    result_doc = {
        "userId":  current_user["id"],
        "email":   current_user["email"],

        "riasec_answers":   data.riasec_answers,
        "aptitude_answers": data.aptitude_answers,

        "scores": {
            # Raw per-code averages on 2–10 scale
            "riasec_scores":    riasec_scores,
            # Percentage correct per subject (pre-rescaling, for display)
            "aptitude_pct":     aptitude_pct,
            # ML feature vector fed to the model (rescaled to training ranges)
            "aptitude_features": aptitude_features,
        },

        "recommendations": recommendations,
        "status":          "completed",
        "submittedAt":     datetime.utcnow(),
    }

    result = await results_col.insert_one(result_doc)

    return {
        "message":         "Assessment submitted successfully.",
        "result_id":       str(result.inserted_id),
        "status":          "completed",
        "recommendations": recommendations,
    }


# ── GET /api/assessment/results/latest ───────────────────────────────────────

@router.get("/results/latest")
async def get_latest_result(current_user=Depends(get_current_user)):
    doc = await results_col.find_one(
        {"userId": current_user["id"], "status": "completed"},
        sort=[("submittedAt", -1)],
    )
    if not doc:
        raise HTTPException(status_code=404, detail="No results found.")

    return {
        "result_id":   str(doc["_id"]),
        "submittedAt": doc["submittedAt"].isoformat(),
        "scores": {
            "riasec_scores":     doc["scores"]["riasec_scores"],
            "aptitude_pct":      doc["scores"]["aptitude_pct"],
            "aptitude_features": doc["scores"].get("aptitude_features", {}),
        },
        "recommendations": doc["recommendations"],
    }


# ── GET /api/assessment/results/history ──────────────────────────────────────

@router.get("/results/history")
async def get_results_history(current_user=Depends(get_current_user)):
    cursor = results_col.find(
        {"userId": current_user["id"], "status": "completed"},
        sort=[("submittedAt", -1)],
    )
    docs = await cursor.to_list(length=20)

    return [
        {
            "result_id":   str(doc["_id"]),
            "submittedAt": doc["submittedAt"].isoformat(),
            "scores": {
                "riasec_scores":     doc["scores"]["riasec_scores"],
                "aptitude_pct":      doc["scores"]["aptitude_pct"],
                "aptitude_features": doc["scores"].get("aptitude_features", {}),
            },
            "recommendations": doc["recommendations"],
        }
        for doc in docs
    ]