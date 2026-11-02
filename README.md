<div align="center">

<img src="smarthire-pro-hero.jpg" alt="SmartHire AI: a resume and a job description linked by a glowing match ring" width="100%"/>

</div>

<img src="smarthire-pro-titlecard.svg" alt="Your resume, decoded." width="100%"/>

<div align="center">

<img src="https://img.shields.io/badge/React-0b1038?style=flat-square&logo=react&logoColor=61DAFB" alt="React"/>
<img src="https://img.shields.io/badge/TypeScript-0b1038?style=flat-square&logo=typescript&logoColor=3178C6" alt="TypeScript"/>
<img src="https://img.shields.io/badge/Vite-0b1038?style=flat-square&logo=vite&logoColor=A78BFA" alt="Vite"/>
<img src="https://img.shields.io/badge/FastAPI-0b1038?style=flat-square&logo=fastapi&logoColor=22D3EE" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Python-0b1038?style=flat-square&logo=python&logoColor=3776AB" alt="Python"/>
<img src="https://img.shields.io/badge/SQLAlchemy-0b1038?style=flat-square&logo=sqlalchemy&logoColor=EC4899" alt="SQLAlchemy"/>

</div>

<img src="smarthire-pro-h-overview.svg" alt="Overview" width="100%"/>

**SmartHire AI** is a full-stack career intelligence workspace for students and job seekers. It reads a resume, compares it with the job you actually want, and points at the exact skills that are missing, so each application can be a little sharper than the last.

> **You can't fix what you can't see.** Every score in SmartHire AI shows its ingredients, so you can tell *why* a number moved.

<table>
<tr>
<td width="33%"><img src="smarthire-pro-still-read.jpg" alt="Read: extract the text" width="100%"/></td>
<td width="33%"><img src="smarthire-pro-still-match.jpg" alt="Match: resume against job" width="100%"/></td>
<td width="33%"><img src="smarthire-pro-still-improve.jpg" alt="Improve: close the gaps" width="100%"/></td>
</tr>
</table>

<img src="smarthire-pro-divider.svg" alt="" width="100%"/>

<img src="smarthire-pro-h-modules.svg" alt="Modules" width="100%"/>

<img src="smarthire-pro-modules.svg" alt="Resume Radar, Job Fit Scale, Gap Finder, Co-Pilot, Workspace, Glass Box" width="100%"/>

| Module | What you get | Powered by |
| :--- | :--- | :--- |
| **Resume Radar** | Your PDF's text, graded in parts: skills, education, projects, experience and structure | PyMuPDF, component scoring |
| **Job Fit Scale** | A match against any job post, built on skill coverage plus wording overlap | Skill overlap, TF-IDF, cosine similarity |
| **Gap Finder** | Two clear lists: skills you have and skills you are missing | Curated skill vocabulary |
| **Co-Pilot** | Career answers on demand, with or without an API key | Optional OpenAI, local fallback |
| **Workspace** | One private place for resumes, past analyses, matches, chats and profile | SQLAlchemy, JWT authentication |
| **Glass-Box Scoring** | Scores that show their ingredients | Component-level breakdowns |

<img src="smarthire-pro-h-pipeline.svg" alt="Pipeline" width="100%"/>

<img src="smarthire-pro-pipeline.svg" alt="Upload, extract, score, match, advise" width="100%"/>

| Step | Stage | What happens |
| :-: | :--- | :--- |
| 1 | **Read** | PyMuPDF reads each page and joins the text content |
| 2 | **Grade** | Component scores are blended into one overall coaching score |
| 3 | **Spot** | A curated skill vocabulary is matched case-insensitively against resume and job text |
| 4 | **Compare** | TF-IDF vectors and cosine similarity measure how closely the wording lines up |
| 5 | **Blend** | 65% skill coverage plus 35% text similarity gives the job-fit number |
| 6 | **Advise** | Optional LLM guidance, or deterministic fallback guidance when there is no key |

<img src="smarthire-pro-h-scoring.svg" alt="Scoring" width="100%"/>

<img src="smarthire-pro-scoring.svg" alt="Five sub-scores averaged into one overall coaching score" width="100%"/>

<img src="smarthire-pro-blend.svg" alt="Job-fit blend: 65 percent skill coverage plus 35 percent text similarity" width="100%"/>

The resume score averages five explicit 0 to 100 sub-scores: skills, education, projects, experience and structure. Matching and missing skills are persisted with each job match.

> **Treat the result as a compass, not a verdict.** These are internal coaching signals, not official ATS scores, and they cannot promise a hiring outcome.

<img src="smarthire-pro-h-architecture.svg" alt="Architecture" width="100%"/>

<img src="smarthire-pro-architecture.svg" alt="Interface, API, engines and data" width="100%"/>

```mermaid
flowchart LR
    U([User]) --> UI[React + TypeScript]
    UI --> API[FastAPI]
    API --> AUTH[Authentication]
    API --> RES[Resume Intelligence]
    API --> JOB[Job Match Engine]
    API --> AI[Career Assistant]
    AUTH --> DB[(SQLite / PostgreSQL)]
    RES --> DB
    JOB --> DB
    AI --> DB

    style U fill:#312e81,color:#fff,stroke:#818cf8
    style UI fill:#172554,color:#fff,stroke:#60a5fa
    style API fill:#134e4a,color:#fff,stroke:#5eead4
    style AUTH fill:#1e1b4b,color:#fff,stroke:#a78bfa
    style RES fill:#1e1b4b,color:#fff,stroke:#a78bfa
    style JOB fill:#1e1b4b,color:#fff,stroke:#a78bfa
    style AI fill:#1e1b4b,color:#fff,stroke:#a78bfa
    style DB fill:#164e63,color:#fff,stroke:#67e8f9
```

<img src="smarthire-pro-h-stack.svg" alt="Tech stack" width="100%"/>

<img src="smarthire-pro-stack.svg" alt="React, TypeScript, Vite, FastAPI, Python, SQLAlchemy" width="100%"/>

| Layer | Technology |
| :--- | :--- |
| Interface | React, TypeScript, Vite, React Router, Lucide React, responsive CSS |
| API | Python, FastAPI, Pydantic |
| Data | SQLAlchemy, SQLite (default), PostgreSQL through `DATABASE_URL` |
| PDF reading | PyMuPDF |
| Matching | TF-IDF, cosine similarity, skill overlap |
| Authentication | JWT |
| Assistant | Optional OpenAI integration with a local fallback |

<img src="smarthire-pro-h-security.svg" alt="Security" width="100%"/>

<img src="smarthire-pro-security.svg" alt="A request with a JWT passes the gate; a request without a token is rejected with 401" width="100%"/>

- JWT-based login with protected API routes.
- Resume and chat actions are tied to the signed-in user.
- Secrets live in environment variables, never in code, and no secrets are sent to the browser.
- SQLite for easy local work, PostgreSQL when you need more.
- A complete PDF upload-and-processing pipeline.

> **Before going public**, review file validation, access controls, persistent storage, CORS, token handling, rate limiting and password-reset email delivery. The reset endpoint creates expiring one-time tokens; connect it to an email provider before production use.

<img src="smarthire-pro-h-quickstart.svg" alt="Quick start" width="100%"/>

<img src="smarthire-pro-terminal.svg" alt="Terminal: git clone, pip install, uvicorn, npm install and npm run dev" width="100%"/>

**Prerequisites:** Python 3.11+, Node.js 20+, npm 10+, Git. Docker Desktop is optional and only needed for PostgreSQL.

| What | Where |
| :--- | :--- |
| Backend API | `http://localhost:8000` |
| Interactive API docs | `http://localhost:8000/docs` |
| Frontend app | `http://127.0.0.1:5173` (or the URL Vite prints) |

**1. Get the code**

```powershell
git clone https://github.com/SyedRaqi/Resume-analyzer.git
cd Resume-analyzer
```

**2. Start the backend**

```powershell
cd backend
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn app.main:app --host 127.0.0.1 --reload --port 8000
```

**3. Start the frontend** in a second terminal:

```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```

Open the URL Vite prints, upload a text-based PDF resume, and you are running.

<img src="smarthire-pro-h-config.svg" alt="Configuration" width="100%"/>

OpenAI is optional. Add a key to `backend/.env` to enable the LLM-backed assistant:

```dotenv
OPENAI_API_KEY=your-api-key
OPENAI_MODEL=gpt-4o-mini
```

Without a key, the app uses a clearly bounded local fallback for common career questions. The chat keeps the last ten messages for context when a key is configured. Never commit secrets or `.env` files.

<details>
<summary><b>PostgreSQL option</b></summary>

<br/>

```powershell
docker compose up -d postgres
```

Set this in `backend/.env` before starting the API:

```dotenv
DATABASE_URL=postgresql+psycopg://smarthire:smarthire_dev@localhost:5432/smarthire
```

Install the driver when using that URL:

```powershell
pip install "psycopg[binary]"
```

</details>

<img src="smarthire-pro-h-api.svg" alt="API" width="100%"/>

| Area | Endpoints |
| :--- | :--- |
| Auth | `POST /api/auth/register`, `POST /api/auth/login`, `GET /api/auth/me`, `POST /api/auth/logout` |
| Password reset | `POST /api/auth/forgot-password`, `POST /api/auth/reset-password` |
| Resumes | `POST /api/resumes/upload`, `GET /api/resumes`, `DELETE /api/resumes/{id}` |
| Analysis | `POST /api/resumes/{id}/analyze`, `GET /api/resumes/{id}/analysis` |
| Job matching | `POST /api/jobs/match`, `GET /api/jobs/history` |
| Chat | `POST /api/chat`, `GET /api/chat/conversations`, `GET /api/chat/conversations/{id}`, `DELETE /api/chat/conversations/{id}` |
| Profile | `GET /api/users/profile`, `PUT /api/users/profile` |

<details>
<summary><b>Project structure</b></summary>

```text
backend/
  app/
    main.py              API routes and application startup
    database.py          Settings, engine, sessions
    models.py            SQLAlchemy schema
    schemas.py           API contracts
    security.py          Password hashing and JWT helpers
    deps.py              Authenticated dependency
    services/
      resume_service.py  PDF extraction, scoring, matching
      chatbot_service.py LLM integration and fallback responses
frontend/
  src/
    App.tsx              Routes and product screens
    styles.css           Responsive product UI
    lib/api.ts           Authenticated API client
    components/Logo.tsx  Shared brand component
uploads/
docker-compose.yml
```

</details>

<details>
<summary><b>Testing and verification</b></summary>

<br/>

```powershell
# Backend syntax check
python -m compileall backend\app

# Frontend typecheck and production bundle
cd frontend
npm run build
```

For a manual smoke test: register, upload a text-based PDF, open the analysis, open the improvement page and print or export it as PDF, paste a job description and run a match, update the profile, request a password reset, then send a message in the SmartHire Assistant.

</details>

<img src="smarthire-pro-h-roadmap.svg" alt="Roadmap" width="100%"/>

<img src="smarthire-pro-roadmap.svg" alt="Roadmap: embeddings, sharper tips, job listings, background jobs, tests and CI, monitoring" width="100%"/>

- [ ] Smarter skill matching with embeddings, so related skills count too
- [ ] Sharper, more specific resume-improvement tips
- [ ] Curated job listings, rather than treating pasted descriptions as live listings
- [ ] Background processing, durable file storage and Alembic migrations
- [ ] Automated tests and continuous integration
- [ ] Production monitoring, rate limiting and deployment hardening

<img src="smarthire-pro-footer.svg" alt="SmartHire AI. Your resume, decoded. Built by Syed Raqi." width="100%"/>

<div align="center">

<sub>See your profile clearly. Know your gaps. Apply with confidence. &middot; <a href="https://github.com/SyedRaqi/Resume-analyzer">Star the repo if it helped</a></sub>

</div>
