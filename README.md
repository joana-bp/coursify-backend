## Coursify Backend
## Project Description
Coursify Backend is the shared FastAPI server that powers the Coursify Web. It handles user authentication, psychometric assessment scoring, machine learning course recommendations, AI-generated profile summaries, and role-based admin operations.
It is built with Python and FastAPI, uses MongoDB Atlas as the database, and exposes a REST API consumed by both frontend platforms via JWT-authenticated requests.

## Features

•	**Role-Based Access Control** — Three-tier role system (user, admin, superadmin) enforced via FastAPI middleware dependencies on all protected endpoints

•	**Assessment Engine** — Randomized question delivery across RIASEC, and Aptitude collections

•	**ML Course Recommendations** — scikit-learn model accepts RIASEC raw scores, trait means, aptitude percentages, and strand to return top 5 ranked courses with confidence scores

•	**AI Profile Summaries** — Google Gemini API generates personalized counselor-style summaries from scored assessment data

•	**Assessment History** — Stores all completed assessment results per user; returns full score breakdowns including RIASEC, aptitude, and recommendations

•	**Admin Analytics** — Aggregated user statistics, registration trends, strand/grade breakdowns, and role distribution with date range filtering

•	**User Management** — Superadmin endpoints for listing, searching, filtering, role updating, and status toggling of user accounts

•	**Audit Logging** — Every role change and status change is recorded with actor, timestamp, and new value inside the user document

•	**CSV Export** — Streams all user data as a downloadable CSV file

•	**Account Seeding** — CLI scripts to seed superadmin and admin accounts interactively

## Technology Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI (Python) |
| Database | MongoDB Atlas |
| Async DB Driver | Motor |
| Authentication | JWT via python-jose |
| Password Hashing | Passlib / bcrypt |
| Request Validation | Pydantic |
| Email (local) | Gmail SMTP via smtplib / aiosmtplib |
| ML Model | Random Forest (scikit-learn) |
| AI Summaries | Google Gemini (google-generativeai) |
| Environment | python-dotenv |
| Hosting | Render |

## System Architecture
                    ┌─────────────────────────────────┐
                    │       Coursify Web (React)       │
                    │       Coursify Mobile (Expo)     │
                    └────────────────┬────────────────┘
                                     │
                          REST API — Bearer JWT
                                     │
                    ┌────────────────▼────────────────┐
                    │         FastAPI Backend          │
                    │                                  │
                    │  ┌──────────────────────────┐   │
                    │  │        API Routers        │   │
                    │  │                           │   │
                    │  │  /api/auth/*              │   │
                    │  │    register, verify,      │   │
                    │  │    login, profile,        │   │
                    │  │    forgot-password,       │   │
                    │  │    reset-verify,          │   │
                    │  │    reset-password         │   │
                    │  │                           │   │
                    │  │  /api/assessment/*        │   │
                    │  │    questions, submit,     │   │
                    │  │    results/latest,        │   │
                    │  │    results/history        │   │
                    │  │                           │   │
                    │  │  /api/admin/*             │   │
                    │  │    analytics, users,      │   │
                    │  │    users/{id}/role,       │   │
                    │  │    users/{id}/status,     │   │
                    │  │    audit-log,             │   │
                    │  │    export/users           │   │
                    │  │                           │   │
                    │  │  /api/ai/*                │   │
                    │  │    profile-summary        │   │
                    │  └────────────┬─────────────┘   │
                    │               │                  │
                    │  ┌────────────▼─────────────┐   │
                    │  │     Role Middleware       │   │
                    │  │  require_superadmin()     │   │
                    │  │  get_current_user()       │   │
                    │  │                           │   │
                    │  └──────────────────────────┘   │
                    └───┬──────────────┬───────────┬───┘
                        │              │           │
           ┌────────────▼──┐  ┌────────▼──────┐  ┌▼──────────────────┐
           │ MongoDB Atlas │  │  scikit-learn │  │  Google Gemini AI  │
           │               │  │   ML Model    │  │                    │
           │  collections: │  │               │  │  Input: scored     │
           │  users        │  │  Input:       │  │  RIASEC            │
           │  questions_   │  │  riasec_raw   │  │  + aptitude        │
           │    riasec     │  │               │  │              
           │  questions_   │  │  aptitude_pct │  │                    │
           │               │  │               │  │  Output: 3–4 line  │
           │               │  │               │  │  profile summary   │
           │    aptitude   │  │  Output:      │  └───────────────────┘
           │  assessment_  │  │  top 5 courses│
           │    results    │  │  + confidence │
           └───────────────┘  └───────────────┘
                                      
                          
Assessment scoring flow:
1.	Client submits strand, RIASEC answers, and aptitude answers
2.	Backend fetches question documents from MongoDB to resolve subcategories and correct answers
3.	RIASEC raw scores are summed per code; aptitude correct counts are converted to percentages
4.	Scored data is passed to the scikit-learn ML model which returns top 5 ranked courses
5.	Full result document is stored in assessment_results collection
6.	Recommendations are returned to the client immediately

## Installation & Setup
Prerequisites
•	Python 3.10 or higher
•	MongoDB Atlas account (or local MongoDB instance)
•	Google Gemini API key
•	Gmail account with App Password enabled (for local email testing)

1. Clone the repository
git clone https://github.com/yourusername/coursify-backend.git
cd coursify-backend

2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables
Create a .env file in the project root:
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret_key
GEMINI_API_KEY=your_google_gemini_api_key
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password
FRONTEND_URL=http://localhost:3000

5. Seed the superadmin account
python seed_superadmin.py
You will be prompted to enter a username, email, and password. If the email already exists, the account will be upgraded to superadmin.

6. Seed an admin account (optional)
python seed_admin.py

7. Run the development server
uvicorn main:app --reload
The API will be available at http://localhost:8000
Interactive API docs are accessible at http://localhost:8000/docs

## Deployment Links
http://coursify-backend-paum.onrender.com/


## Known Limitations
•	**Registration OTP** — OTP verification and password reset emails are suspended due to the limitation that requires outbound ports 465 or 587 on render when deployed.

## Lab Activity
**Lab Activity 2** extended the recommendation system by introducing advanced supervised learning techniques capable of improving prediction quality and deployment readiness.
Among all evaluated models, **Random Forest** emerged as the optimal solution because it:


-achieved high accuracy


-handled complex student data effectively


-remained interpretable


-produced stable predictions


-supported efficient real-time deployment


For these reasons, **Random Forest** became the final machine learning model integrated into the course recommendation system.

















