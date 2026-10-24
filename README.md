<!-- SMART HIRE AI | CINEMATIC README -->

<div align="center">

<img src="assets/smarthire-cinematic-banner.gif" width="100%" alt="SmartHire AI animated cinematic hero banner" />

<br/>

# SmartHire AI

### CAREER INTELLIGENCE. REENGINEERED.

**Your potential is greater than a resume. Discover what makes you stand out.**

An AI-powered career workspace for resume intelligence, skill-gap discovery, job matching, and smarter career preparation.

<br/>

<a href="https://github.com/SyedRaqi/Resume-analyzer">
  <img src="https://img.shields.io/badge/EXPLORE%20PROJECT-6366F1?style=for-the-badge&logo=github&logoColor=white" alt="Explore project"/>
</a>
&nbsp;
<a href="#features">
  <img src="https://img.shields.io/badge/DISCOVER%20FEATURES-0891B2?style=for-the-badge&logo=rocket&logoColor=white" alt="Discover features"/>
</a>

<br/><br/>

<img src="https://img.shields.io/badge/REACT-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React"/>
<img src="https://img.shields.io/badge/TYPESCRIPT-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/>
<img src="https://img.shields.io/badge/FASTAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
<img src="https://img.shields.io/badge/PYTHON-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/AI%20%2B%20NLP-8B5CF6?style=flat-square" alt="AI and NLP"/>

</div>

---

<a id="vision"></a>

## ◉  THE VISION

The next opportunity shouldn't depend on guesswork.

SmartHire AI transforms career preparation into a structured, data-informed process. It helps users understand their resume, compare their skills with job requirements, identify gaps, and get practical guidance.

**Upload. Understand. Improve. Advance.**

<a id="features"></a>

## ◈  INTELLIGENCE MODULES

<table>
<tr>
<td width="50%" valign="top">

### 01 / Resume Intelligence

Extract and analyze resume content, with component-based assessments covering skills, education, projects, experience, and structure.

</td>
<td width="50%" valign="top">

### 02 / Job Match Engine

Compare resumes with job descriptions using skill coverage and TF-IDF cosine similarity.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 03 / Skill-Gap Discovery

Identify matching and missing skills to help users understand where additional preparation may be valuable.

</td>
<td width="50%" valign="top">

### 04 / AI Career Assistant

Get career guidance through optional OpenAI integration, with a local fallback for supported common questions.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 05 / Personal Workspace

Manage accounts, resumes, analysis history, job matches, conversations, and profile information.

</td>
<td width="50%" valign="top">

### 06 / Explainable Results

Keep resume assessment components and job-matching signals visible instead of presenting every result as an unexplained number.

</td>
</tr>
</table>

---

## ⌬  THE EXPERIENCE

<div align="center">

| PHASE | ACTION | OUTCOME |
|:---:|---|---|
| 01 | Upload your resume | Extracted resume content |
| 02 | Analyze your profile | Component-based feedback |
| 03 | Compare a job description | Matching and missing skills |
| 04 | Explore your next steps | More focused career preparation |

</div>

## ⟁  UNDER THE HOOD

```mermaid
flowchart LR
    U([USER]) --> UI[React + TypeScript]
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

### TECHNOLOGY MATRIX

| SYSTEM | TECHNOLOGY |
|---|---|
| Interface | React, TypeScript, Vite, React Router |
| Visual layer | Responsive CSS, Lucide React |
| API layer | Python, FastAPI, Pydantic |
| Persistence | SQLAlchemy, SQLite, PostgreSQL option |
| Document processing | PyMuPDF |
| Matching algorithms | TF-IDF, cosine similarity, skill overlap |
| Security | JWT-based authentication |
| Conversational AI | Optional OpenAI integration and local fallback |

---

## ⌘  RUN IT LOCALLY

### Requirements

- Python 3.11+
- Node.js 20+
- npm 10+
- Git

### 01 — Clone

```powershell
git clone https://github.com/SyedRaqi/Resume-analyzer.git
cd Resume-analyzer
```

### 02 — Start the backend

```powershell
cd backend
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn app.main:app --reload --port 8000
```

API documentation: http://localhost:8000/docs

### 03 — Start the frontend

Open a second terminal from the project root:

```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```

Open the local URL printed by Vite, usually http://localhost:5173.

Configure any required API base URL using the variable documented in `frontend/.env.example`.

### 04 — Optional AI configuration

Add your own API key to `backend/.env` if you want to enable the OpenAI-backed assistant:

```dotenv
OPENAI_API_KEY=your-api-key
OPENAI_MODEL=gpt-4o-mini
```

Never commit secrets or `.env` files to GitHub.

---

## ◈  MATCHING METHODOLOGY

| COMPONENT | APPROACH |
|---|---|
| Resume extraction | PDF text extraction with PyMuPDF |
| Resume assessment | Component scores combined into an overall coaching score |
| Skill detection | Curated vocabulary and case-insensitive matching |
| Job similarity | TF-IDF vectorization and cosine similarity |
| Job-match calculation | 65% skill coverage + 35% text similarity |
| Career guidance | Optional LLM integration or deterministic fallback |

These scores are coaching signals, not official ATS scores or guarantees of hiring outcomes.

## ⛨  ENGINEERING & SECURITY

- JWT-based authentication and protected API workflows
- User-specific resume and conversation operations
- Environment-based configuration for secrets
- SQLite for local development and a PostgreSQL option
- PDF upload and processing workflow

Before production deployment, verify file validation, access controls, persistent storage, CORS, token handling, rate limiting, and email delivery for password resets.

## ⌁  ROADMAP

- [ ] Semantic skill matching with embeddings
- [ ] Enhanced resume-improvement recommendations
- [ ] Curated job-source integration
- [ ] Background processing and durable file storage
- [ ] Automated tests and continuous integration
- [ ] Production monitoring and deployment hardening

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0891B2,50:312E81,100:0B1020&height=120&section=footer" width="100%" alt="Blue and violet cinematic footer"/>

### ENGINEER YOUR NEXT OPPORTUNITY.

**SmartHire AI** · Built by [Syed Raqi](https://github.com/SyedRaqi)

<a href="https://github.com/SyedRaqi/Resume-analyzer">SOURCE CODE</a>

<sub>Understand your profile. Discover your potential. Keep moving forward.</sub>

</div>
