"""
ml/predictor.py
===============
Loads the trained RandomForestClassifier (Lab Activity 2, Part 3A)
and converts raw assessment scores into the exact 11-feature vector
the model was trained on.

FEATURE VECTOR (11 features, must match training order exactly):
  Academic scores  (range in training data):
    [0]  Math_Score           – integer, 60–97
    [1]  Science_Score        – integer, 60–97
    [2]  Programming_Skill    – integer, 2–5
    [3]  Communication_Skill  – integer, 2–5
    [4]  Logical_Ability      – integer, 2–5

  RIASEC interest scores  (range in training data):
    [5]  R_score  (Realistic)      – integer, 0–10
    [6]  I_score  (Investigative)  – integer, 0–10
    [7]  A_score  (Artistic)       – integer, 0–10
    [8]  S_score  (Social)         – integer, 0–10
    [9]  E_score  (Enterprising)   – integer, 0–10
    [10] C_score  (Conventional)   – integer, 0–10

  All features are passed through StandardScaler before prediction.
  The scaler was fit on the full training dataset — do NOT re-scale inputs manually.

Target classes (6):
  Accountant | Data Scientist | Doctor | Entrepreneur | Software Engineer | Teacher

Usage:
    from ml.predictor import get_top5_recommendations

    results = get_top5_recommendations(
        academic = {
            "Math_Score": 85,
            "Science_Score": 78,
            "Programming_Skill": 4,
            "Communication_Skill": 3,
            "Logical_Ability": 4,
        },
        riasec = {
            "R_score": 3,
            "I_score": 8,
            "A_score": 2,
            "S_score": 4,
            "E_score": 5,
            "C_score": 7,
        },
    )
    # returns: [{"rank": 1, "course": "Data Scientist", "confidence": 62.0}, ...]
"""

import os
import numpy as np
import pandas as pd
import joblib

# ── Artifact paths ─────────────────────────────────────────────────────────────
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH  = os.path.join(BASE_DIR, "artifacts", "course_model.joblib")
SCALER_PATH = os.path.join(BASE_DIR, "artifacts", "scaler.joblib")
LE_PATH     = os.path.join(BASE_DIR, "artifacts", "label_encoder.joblib")
FN_PATH     = os.path.join(BASE_DIR, "artifacts", "feature_names.joblib")

# ── Lazy-load artifacts (loaded once, reused across requests) ──────────────────
_model    = None
_scaler   = None
_le       = None
_features = None

def _load_artifacts():
    global _model, _scaler, _le, _features
    if _model is None:
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            _model    = joblib.load(MODEL_PATH)
            _scaler   = joblib.load(SCALER_PATH)
            _le       = joblib.load(LE_PATH)
            _features = joblib.load(FN_PATH)


# ── Expected feature groups ────────────────────────────────────────────────────

ACADEMIC_FEATURES = [
    "Math_Score",
    "Science_Score",
    "Programming_Skill",
    "Communication_Skill",
    "Logical_Ability",
]

RIASEC_FEATURES = [
    "R_score",   # Realistic
    "I_score",   # Investigative
    "A_score",   # Artistic
    "S_score",   # Social
    "E_score",   # Enterprising
    "C_score",   # Conventional
]

# Full feature order as saved in feature_names.joblib (matches training column order)
ALL_FEATURES = ACADEMIC_FEATURES + RIASEC_FEATURES  # length = 11


# ── Input validation ───────────────────────────────────────────────────────────

def _validate_inputs(academic: dict, riasec: dict) -> None:
    """Raises ValueError if any required key is missing."""
    missing_academic = [f for f in ACADEMIC_FEATURES if f not in academic]
    missing_riasec   = [f for f in RIASEC_FEATURES   if f not in riasec]
    if missing_academic or missing_riasec:
        raise ValueError(
            f"Missing academic fields: {missing_academic} | "
            f"Missing RIASEC fields: {missing_riasec}"
        )


# ── Feature vector assembly ────────────────────────────────────────────────────

def build_feature_vector(academic: dict, riasec: dict) -> pd.DataFrame:
    """
    Assembles raw scores into the 11-feature DataFrame the model expects.
    No manual normalization is applied here — StandardScaler handles that.

    Parameters
    ----------
    academic : dict
        Keys: Math_Score, Science_Score, Programming_Skill,
              Communication_Skill, Logical_Ability
        Values: integers matching training data ranges.

    riasec : dict
        Keys: R_score, I_score, A_score, S_score, E_score, C_score
        Values: integers 0–10.

    Returns
    -------
    pd.DataFrame with shape (1, 11) and columns in exact training order.
    """
    _validate_inputs(academic, riasec)

    row = {}
    for feat in ACADEMIC_FEATURES:
        row[feat] = academic[feat]
    for feat in RIASEC_FEATURES:
        row[feat] = riasec[feat]

    return pd.DataFrame([row], columns=ALL_FEATURES)


# ── Main prediction function ───────────────────────────────────────────────────

def get_top5_recommendations(
    academic: dict,
    riasec:   dict,
    k:        int = 5,
) -> list[dict]:
    """
    Returns the top-K career/course recommendations with confidence scores.

    Parameters
    ----------
    academic : dict
        Raw academic scores. Keys must include:
        Math_Score, Science_Score, Programming_Skill,
        Communication_Skill, Logical_Ability.

    riasec : dict
        RIASEC interest scores (0–10 each). Keys must include:
        R_score, I_score, A_score, S_score, E_score, C_score.

    k : int
        Number of top recommendations to return (default 5).

    Returns
    -------
    list of dicts:
        [
            {"rank": 1, "course": "Data Scientist",     "confidence": 62.0},
            {"rank": 2, "course": "Software Engineer",  "confidence": 18.5},
            ...
        ]
    """
    _load_artifacts()

    # Build and order the feature vector to match training column order
    X_df      = build_feature_vector(academic, riasec)
    X_ordered = X_df[_features]   # enforces exact training column order

    # Apply the same StandardScaler used during training
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        X_scaled = _scaler.transform(X_ordered)

    # Predict class probabilities and pick top-K
    proba  = _model.predict_proba(X_scaled)[0]
    top_k  = np.argsort(proba)[::-1][:k]

    return [
        {
            "rank":       int(rank + 1),
            "course":     str(_le.classes_[idx]),
            "confidence": round(float(proba[idx]) * 100, 1),
        }
        for rank, idx in enumerate(top_k)
    ]