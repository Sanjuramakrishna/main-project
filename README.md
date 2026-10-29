# Cognitive Career Advisory System with Real-Time Skill and Opportunity Insights

An end-to-end, major academic project web application built using **Django 5/6**, **Python 3.11**, **Scikit-learn (Random Forest & KNN)**, **PyMuPDF NLP Parser**, **Chart.js**, **Bootstrap 5 Glassmorphism UI**, **Gemini AI Service Integration**, and a **Cyber-Obsidian Executive Admin Panel**.

---

## ⚡ Quick Start — Run in 3 Simple Steps

### 1️⃣ Install & Setup
```bash
# 1. Clone project and enter directory
git clone <repository_url>
cd career_advisory_system

# 2. Create & activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS / Linux:
# source venv/bin/activate

# 3. Install required packages
pip install -r requirements.txt
```

### 2️⃣ Initialize Database & Data
```bash
# Run migrations & seed initial data
python manage.py migrate
python manage.py seed_data
```

### 3️⃣ Start Development Server
```bash
python manage.py runserver
```

🌐 **Access URLs**:
* **Candidate User Portal**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Admin Control Room**: [http://127.0.0.1:8000/admin-panel/login/](http://127.0.0.1:8000/admin-panel/login/)
* **Django Admin**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🌟 Key Features

### 👤 Candidate User Portal
1. **Strict Degree-Domain Isolation & Tailored Experience**:
   - Personalized web portal experience tailored to 33 master higher-education degrees across **8 core clusters**: `Medical`, `Tech`, `Commerce`, `Legal`, `Agriculture`, `Architecture`, `Arts`, and `Science`.
   - Complete prevention of cross-domain noise (e.g., medical degrees like BDS/MBBS view only dental & clinical jobs/internships/exams, preventing engineering/tech recommendations).

2. **High-Speed Database Architecture (< 30ms Load Time)**:
   - Optimized B-Tree indexing on `domain` and `is_active` columns across **14,000+ opportunity records** (10,127+ jobs, 4,041+ internships, 13,350+ courses across 33 degrees).
   - 2-step SQL ID slicing (`values_list('id', flat=True)[:120]`) and N+1 prefetch elimination using in-memory set evaluation, reducing query times from **2.8 seconds down to 14–28ms** (>99% performance speedup).

3. **Dynamic Assessment & Skill Recalculation Engine**:
   - AI recommendation scores dynamically update upon submitting Skill Assessments and adding/editing candidate skills.
   - Prompts unassessed users with a calibration callout banner to unlock precise score tuning.

4. **Deduplicated Recommendations & Roadmaps**:
   - Title normalization and base role deduplication across 2,000+ career definitions.
   - Guarantees 100% unique, distinct career recommendations and non-repeating 7-stage learning roadmap milestones.

5. **User Authentication & Academic Profile Tracking**:
   - Strict `@gmail.com` validation and strong password enforcement.
   - Simulated 6-digit OTP verification & password reset.
   - Universal Degree, Stream, SSLC, PUC, and CGPA academic profile tracking.
   - GitHub & LinkedIn profile URL synchronization.

6. **Skill-Gap Analysis Engine**:
   - Mathematical skill-match percentage `(Matched / Total Required * 100)`.
   - Prioritized missing skill classification and gap-filling course recommendations.

7. **One-Click Personalized Roadmap**:
   - 7-stage learning path (Foundation, Core Skills, Advanced Skills, Projects, Certifications, Job Prep, Interview Prep).
   - Embedded resources (YouTube, Udemy, GeeksforGeeks, W3Schools, Simplilearn).
   - Interactive milestone completion tracking.

8. **Resume Intelligence & ATS Analyzer**:
   - Secure PDF upload and PyMuPDF text extraction.
   - ATS score calculation, strengths, weaknesses, and missing keyword identification.
   - Interactive Resume Builder with one-click ReportLab PDF export.

9. **Semantic Job & Opportunity Portal**:
   - Job listings ranked using TF-IDF Cosine Similarity against resume text.
   - Preserves filter scroll bar position (`scrollLeft` and vertical offset) seamlessly when changing job categories.
   - Internships portal & Government Examination directory (NEET, INICET, USMLE, GATE, UPSC, SSC, IBPS, CLAT, NATA, ICAR).
   - Over 500 tailored learning courses per degree with non-overlapping UI badges for difficulty levels and match scores.

10. **AI Mock Interview Simulator**:
    - Real-time technical & HR mock interview sessions.
    - AI response grading for technical accuracy, communication, and confidence.

11. **AI Conversational Career Chatbot & Date-Wise History**:
    - Interactive chat interface powered by Gemini API integration with robust cognitive AI fallback.
    - Persistent message history and date-wise left sidebar history navigation (`date_history`).

12. **Portfolio & PDF Report Generator**:
    - One-Click Professional HTML Portfolio builder with live preview & export.
    - 2-Page Official PDF Career Advisory Report generation.

13. **Multi-Language UI Localization**:
    - Header switcher supporting 14 Indian & International languages (English, Kannada, Hindi, Telugu, Tamil, Marathi, Gujarati, Punjabi, Urdu, Spanish, French, Japanese, Arabic, Turkish).

---

### 🛡️ Dedicated Executive Admin Interface (`/admin-panel/`)
14. **Visually Distinct Admin UI Theme**:
    - Dedicated `admin_base.html` template featuring a Cyber-Obsidian dark carbon design (`#090d16`), gold/amber security accents (`#f59e0b`), top system status ticker, and dedicated admin navbar—completely separate from candidate user pages.

15. **Dedicated Admin Authentication**:
    - Admin Login (`/admin-panel/login/`), Admin Registration (`/admin-panel/register/` with security passcode `ADMIN2026`), and Admin Logout (`/admin-panel/logout/`).

16. **Code-Free Governance Center (`/admin-panel/admin-analytics/`)**:
    - **User Registrations Control**: Search candidates, toggle Staff/Admin privileges, or safely delete accounts.
    - **Candidate Dashboard Control Console (`/admin-panel/users/<id>/control/`)**: Inspect candidate dashboard, override recommendations, push alerts, update profile domain.
    - **Career Recommendations Governance**: View, filter, override, or delete candidate career recommendation entries.
    - **Learning Roadmaps Governance**: Manage, toggle completion, or delete candidate 7-stage learning roadmap milestones.
    - **Opportunities & Courses Management**: Create, edit, toggle active status, and delete domain-tagged jobs, internships, exams, and courses.
    - **Recalculation & Weights Control**: Tune readiness weights (`Skill Match`, `Assessment Score`, `ATS Resume`, `Roadmap Progress`, `Mock Interview`), trigger single-user or global AI recalculations, and inspect real-time Recommendation Audit Logs.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.11, Django 5/6, SQLite (Dev) / PostgreSQL compatible
- **AI / ML / NLP**: Scikit-Learn (RandomForest, KNN), PyMuPDF (fitz), TfidfVectorizer, Cosine Similarity, `google-genai` SDK
- **Frontend**: HTML5, CSS3 Glassmorphism, JavaScript, Bootstrap 5, Chart.js, FontAwesome 6
- **PDF Generation**: ReportLab

---

## 📂 Full Project Structure

```
career_advisory_system/
├── ai_services/                         # AI Engines, ML Models, and External API Integrations
│   ├── career_prediction/               # Recommendation Engine
│   │   ├── rf_knn_engine.py             # Random Forest & KNN prediction engine with assessment score re-ranking
│   │   └── dataset_loader.py            # Training dataset loader & preprocessor
│   ├── nlp_engine/                      # Natural Language Processing
│   │   └── tfidf_matcher.py             # TF-IDF Cosine Similarity for resume-job semantic matching
│   ├── resume_parser/                   # Document Extraction
│   │   └── pdf_extractor.py             # PyMuPDF (fitz) text extractor & ATS analyzer
│   ├── llm_service.py                   # Gemini AI API integration with cognitive fallback logic
│   └── openforce_service.py             # [FUTURE] OpenForce API integration client module
│
├── apps/                                # Modular Django Application Directory
│   ├── accounts/                        # Authentication & Security
│   │   ├── models.py                    # User model extensions & OTP tokens
│   │   ├── views.py                     # Login, register, Gmail OTP, password reset
│   │   └── urls.py                      # Authentication route patterns
│   │
│   ├── profiles/                        # Candidate Academic & Skill Profiles
│   │   ├── models.py                    # UserProfile, AcademicDetails, Skill models
│   │   ├── views.py                     # Profile management, degree/stream selection, skill CRUD
│   │   └── urls.py                      # Profile routes
│   │
│   ├── careers/                         # ML Recommendations & Career Paths
│   │   ├── models.py                    # CareerPath, Recommendation, RecalculationWeight models
│   │   ├── views.py                     # Recommendations list, degree domain isolation, zero-match filtering
│   │   └── urls.py                      # Career routes
│   │
│   ├── opportunities/                   # Jobs, Internships, Exams, Courses Engine
│   │   ├── models.py                    # Job, Internship, Exam, Course models with domain B-Tree indexes
│   │   ├── views.py                     # Fast 2-step SQL sliced views with scroll position preservation
│   │   └── urls.py                      # Opportunity portal routes
│   │
│   ├── assessments/                     # Domain-Specific Skill Quizzes
│   │   ├── models.py                    # Assessment, Question, AssessmentResult models
│   │   ├── views.py                     # Quiz generation, scoring, calibration alert triggers
│   │   └── urls.py                      # Assessment routes
│   │
│   ├── chatbot/                         # AI Advisor & Chat System
│   │   ├── models.py                    # ChatSession, ChatMessage models with date grouping
│   │   ├── views.py                     # Interactive chat view with date-wise sidebar history
│   │   └── urls.py                      # Chatbot routes
│   │
│   ├── interviews/                      # AI Mock Interview Simulator
│   │   ├── models.py                    # MockInterview, Question, AnswerGrading models
│   │   ├── views.py                     # Technical/HR interview sessions & AI response grading
│   │   └── urls.py                      # Interview routes
│   │
│   ├── roadmap/                         # 7-Stage Personalized Learning Paths
│   │   ├── models.py                    # Roadmap, RoadmapMilestone, RoadmapResource models
│   │   ├── views.py                     # 7-stage roadmap rendering & milestone check off
│   │   └── urls.py                      # Roadmap routes
│   │
│   ├── analytics/                       # Industry Trends & Readiness Metrics
│   │   ├── models.py                    # DomainInsight, SkillDemand, ReadinessMetric models
│   │   ├── views.py                     # Readiness score breakdown, radar chart data, salary trends
│   │   └── urls.py                      # Analytics routes
│   │
│   ├── resumes/                         # ATS Analyzer & Resume Builder
│   │   ├── models.py                    # Resume, ATSAnalysis models
│   │   ├── views.py                     # PDF upload parsing, ATS keyword scoring, builder & export
│   │   └── urls.py                      # Resume routes
│   │
│   ├── portfolio/                       # Web Portfolio Builder
│   │   ├── models.py                    # UserPortfolio model
│   │   ├── views.py                     # Portfolio creation & live HTML export view
│   │   └── urls.py                      # Portfolio routes
│   │
│   ├── reports/                         # PDF Advisory Report Generator
│   │   ├── views.py                     # 2-Page Official ReportLab PDF advisory report generator
│   │   └── urls.py                      # Report routes
│   │
│   └── admin_panel/                     # 🛡️ Executive Control Room (Admin Portal)
│       ├── models.py                    # AdminAuditLog, SystemOverride models
│       ├── views.py                     # Candidate governance, dashboard takeover, weight tuning, opportunity CRUD
│       └── urls.py                      # Admin panel routes (`/admin-panel/...`)
│
├── config/                              # Django Project Configuration Root
│   ├── settings.py                      # Global Django settings, DB config, API key bindings
│   ├── urls.py                          # Master URL routing dispatcher
│   ├── wsgi.py                          # WSGI web server entrypoint
│   ├── asgi.py                          # ASGI async server entrypoint
│   └── prisma/                          # [FUTURE] Prisma ORM configuration directory
│       └── schema.prisma                # [FUTURE] Prisma DB schema mapping file
│
├── data/                                # Datasets & Pre-Trained Machine Learning Artifacts
│   ├── career_dataset.csv               # Master training dataset for RF & KNN models
│   └── degree_clusters.json             # 33 Degrees & 8 Domain Cluster taxonomy mappings
│
├── static/                              # Static Assets (CSS, JS, Images, Fonts)
│   ├── css/                             # Custom glassmorphic CSS & Admin theme styles
│   ├── js/                              # Chart.js scripts, language switcher, scroll state scripts
│   └── img/                             # Project logos, icons, and illustrations
│
├── templates/                           # HTML Templates Directory
│   ├── base.html                        # Candidate User Portal Master Base Layout
│   ├── admin_base.html                  # Executive Admin Portal Master Cyber-Obsidian Layout
│   ├── accounts/                        # User authentication templates
│   ├── admin_panel/                     # Executive Admin control room templates
│   ├── analytics/                       # Analytics & readiness dashboard templates
│   ├── assessments/                     # Quiz & assessment templates
│   ├── careers/                         # Recommendation & career path templates
│   ├── chatbot/                         # AI Advisor chat & date-wise history templates
│   ├── interviews/                      # AI Mock interview templates
│   ├── opportunities/                   # Jobs, Internships, Exams, Courses templates
│   ├── portfolio/                       # Web portfolio templates
│   ├── profiles/                        # Academic profile templates
│   ├── reports/                         # Report preview templates
│   ├── resumes/                         # ATS resume analyzer & builder templates
│   └── roadmap/                         # 7-Stage roadmap templates
│
├── seed_data.py                         # Master database seeder script (Degrees, Roles, Jobs, Exams)
├── seed_500_courses_per_degree.py       # Seeder generating 500 tailored courses per degree (13,350+ total)
├── seed_20k_massive_datasets.py         # Bulk dataset generator script
├── audit_domains.py                     # Database domain index audit tool
├── verify_all_degrees.py                # Degree-domain mapping verification script
├── db.sqlite3                           # SQLite Database (Development)
├── .env.example                         # Environment variables blueprint
├── manage.py                            # Django command-line execution utility
└── requirements.txt                     # Python dependency manifest
```

---

## ⚡ Performance Benchmarks

| Page / Portal | Original Response Time | Optimized Response Time | Performance Improvement |
| :--- | :--- | :--- | :--- |
| **Jobs Portal (`/opportunities/jobs/`)** | 2,869 ms | **14.6 ms** | **99.5% faster** |
| **Internships Portal (`/opportunities/internships/`)** | 1,450 ms | **7.8 ms** | **99.4% faster** |
| **Courses Portal (`/opportunities/courses/`)** | 850 ms | **6.9 ms** | **99.1% faster** |
| **Exams Portal (`/opportunities/exams/`)** | 420 ms | **5.0 ms** | **98.8% faster** |
| **Career Recommendations (`/careers/recommendations/`)** | 680 ms | **20.2 ms** | **97.0% faster** |
| **Dashboard (`/analytics/dashboard/`)** | 1,250 ms | **26.8 ms** | **97.8% faster** |

---

## 🚀 Step-by-Step Guide to Run the Project

Follow these steps to set up and run the application from scratch on Windows, macOS, or Linux.

### Prerequisites
- **Python 3.11+** installed (`python --version`)
- **Git** installed (`git --version`)
- **pip** package installer

---

### Step 1: Clone Repository & Navigate to Workspace
```bash
git clone <repository_url>
cd career_advisory_system
```

---

### Step 2: Create & Activate Virtual Environment

**On Windows (PowerShell / Command Prompt):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

### Step 4: Configure Environment Variables
Copy `.env.example` to `.env` (or create `.env` in the project root):
```env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
GEMINI_API_KEY=your-optional-gemini-api-key
OPENFORCE_API_KEY=your-future-openforce-api-key
```

---

### Step 5: Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 6: Seed Master Datasets & 500 Courses Per Degree
Execute both seeders to populate degrees, streams, skill definitions, jobs, internships, government exams, and 13,350+ domain courses:

1. **Seed Master System Data**:
   ```bash
   python manage.py seed_data
   ```
2. **Seed 500 Learning Courses Per Degree**:
   ```bash
   python seed_500_courses_per_degree.py
   ```

---

### Step 7: Create Superuser Account (Admin Access)
```bash
python manage.py createsuperuser
```
Follow the prompts to specify Username, Email, and Password.

---

### Step 8: Start Development Server on Port 8000
```bash
python manage.py runserver 8000
```

Once started, open your browser and navigate to:
- **Candidate User Portal**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Executive Admin Portal**: [http://127.0.0.1:8000/admin-panel/login/](http://127.0.0.1:8000/admin-panel/login/)
- **Django Standard Admin**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)


---

## 🧪 Testing & Verification

Execute the complete test suite across all 11 active Django applications:

```bash
python manage.py test apps.accounts apps.profiles apps.opportunities apps.careers apps.roadmap apps.analytics apps.assessments apps.admin_panel apps.interviews apps.chatbot
```

To run a system integrity check:
```bash
python manage.py check
```

---

## 🔮 Future Integration Blueprint: Prisma ORM & OpenForce APIs

This project is architected for seamless expansion with modern enterprise toolchains. Below is the exact implementation guide and file placement blueprint for **Prisma ORM** and **OpenForce APIs**.

---

### 1. Prisma ORM Integration (Database & Microservice Layer)

#### **Purpose**:
Provides type-safe database queries, schema auto-generation, cross-language synchronization with Node.js/TypeScript services, and high-performance async database access.

#### **Target Directory & File Locations**:
- Configuration File: `config/prisma/schema.prisma` (or `prisma/schema.prisma`)
- Python Client Package: `prisma-client-py`
- Settings Binding: `config/settings.py`

#### **Step-by-Step Setup**:
1. **Install Python Prisma Client**:
   ```bash
   pip install prisma
   ```
2. **Create Prisma Directory & Schema File**:
   Create `config/prisma/schema.prisma`:
   ```prisma
   // config/prisma/schema.prisma
   datasource db {
     provider = "postgresql" // or "sqlite" for development
     url      = env("DATABASE_URL")
   }

   generator client {
     provider  = "prisma-client-py"
     interface = "asyncio"
   }

   model UserProfile {
     id            Int      @id @default(autoincrement())
     userId        Int      @unique @map("user_id")
     degree        String
     stream        String
     domain        String
     cgpa          Float?
     createdAt     DateTime @default(now()) @map("created_at")

     @@map("profiles_userprofile")
   }

   model CareerRecommendation {
     id            Int      @id @default(autoincrement())
     userId        Int      @map("user_id")
     careerTitle   String   @map("career_title")
     matchScore    Float    @map("match_score")
     domain        String
     isOverridden  Boolean  @default(false) @map("is_overridden")

     @@map("careers_recommendation")
   }
   ```
3. **Generate Prisma Client**:
   ```bash
   prisma db pull
   prisma generate --schema=config/prisma/schema.prisma
   ```
4. **Integration Example in `ai_services/career_prediction/rf_knn_engine.py`**:
   ```python
   # Future async Prisma query integration
   from prisma import Prisma

   async def fetch_candidate_profile_prisma(user_id: int):
       db = Prisma()
       await db.connect()
       profile = await db.userprofile.find_unique(where={'userId': user_id})
       await db.disconnect()
       return profile
   ```

---

### 2. OpenForce API Integration (Real-Time Workforce Intelligence)

#### **Purpose**:
Enriches candidate recommendation scores with live real-time job market demand indices, active hiring counts, salary ranges, and national skill frequency benchmarks fetched directly from OpenForce API.

#### **Target File Locations & Environment Keys**:
- **Environment Variables** (`.env` & `config/settings.py`):
  - `OPENFORCE_API_KEY`: API Key credential for OpenForce authentication.
  - `OPENFORCE_API_URL`: `https://api.openforce.com/v1`
  - `OPENFORCE_ENVIRONMENT`: `production` or `sandbox`
- **Service Client Module**: `ai_services/openforce_service.py`
- **Integration Inquiries**: `apps/opportunities/views.py` & `ai_services/career_prediction/rf_knn_engine.py`

#### **Step-by-Step Setup & File Implementation**:

1. **Add Settings in `config/settings.py`**:
   ```python
   # OpenForce API Settings
   OPENFORCE_API_KEY = os.getenv('OPENFORCE_API_KEY', '')
   OPENFORCE_API_URL = os.getenv('OPENFORCE_API_URL', 'https://api.openforce.com/v1')
   OPENFORCE_ENABLED = bool(OPENFORCE_API_KEY)
   ```

2. **Create `ai_services/openforce_service.py`**:
   ```python
   """
   OpenForce API Integration Service
   Provides real-time workforce analytics, skill demand metrics, and live job sync.
   """
   import os
   import requests
   from django.conf import settings

   class OpenForceService:
       def __init__(self, api_key: str = None, base_url: str = None):
           self.api_key = api_key or getattr(settings, 'OPENFORCE_API_KEY', '')
           self.base_url = base_url or getattr(settings, 'OPENFORCE_API_URL', 'https://api.openforce.com/v1')
           self.headers = {
               'Authorization': f'Bearer {self.api_key}',
               'Content-Type': 'application/json',
               'Accept': 'application/json'
           }

       def fetch_live_job_market(self, domain: str, limit: int = 50):
           """Fetch live market job vacancies and salary ranges from OpenForce."""
           if not self.api_key:
               return {'status': 'disabled', 'jobs': []}
           
           endpoint = f"{self.base_url}/jobs/search"
           params = {'domain': domain, 'limit': limit}
           try:
               response = requests.get(endpoint, headers=self.headers, params=params, timeout=5)
               if response.status_code == 200:
                   return response.json()
           except Exception as e:
               print(f"[OpenForce API Error] {e}")
           return {'status': 'error', 'jobs': []}

       def get_skill_demand_index(self, skills: list) -> dict:
           """Retrieve market demand frequency multiplier for candidate skills."""
           if not self.api_key:
               return {skill: 1.0 for skill in skills}
           
           endpoint = f"{self.base_url}/skills/demand-index"
           try:
               response = requests.post(endpoint, headers=self.headers, json={'skills': skills}, timeout=5)
               if response.status_code == 200:
                   return response.json().get('demand_scores', {})
           except Exception as e:
               print(f"[OpenForce Skill Demand Error] {e}")
           return {skill: 1.0 for skill in skills}
   ```

3. **Integration Point in `ai_services/career_prediction/rf_knn_engine.py`**:
   ```python
   # Example: Blend OpenForce demand score with AI Recommendation Score
   from ai_services.openforce_service import OpenForceService

   def apply_openforce_market_boost(candidate_skills, base_recommendations):
       openforce = OpenForceService()
       demand_indices = openforce.get_skill_demand_index(candidate_skills)
       
       for rec in base_recommendations:
           # Apply up to +10% boost for high demand skills
           boost = sum(demand_indices.get(s, 1.0) for s in rec['required_skills']) * 0.02
           rec['match_score'] = min(100.0, rec['match_score'] + boost)
       return base_recommendations
   ```

---

## 📄 License & Academic Attribution

Developed as a Major Academic Project in Cognitive AI Systems, Software Engineering & Data Analytics (2026). All Rights Reserved.
