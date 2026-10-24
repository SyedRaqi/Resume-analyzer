<!-- SMART HIRE AI | 3D ANIMATED README -->

<div align="center">

<img src="assets/smarthire-banner.svg" width="100%" alt="SmartHire AI animated 3D banner" />

<a href="https://github.com/SyedRaqi/Resume-analyzer">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2800&pause=900&color=A78BFA&center=true&vCenter=true&width=720&lines=Upload+your+resume.;Compare+it+with+any+job+description.;See+your+skill+gaps+instantly.;Engineer+your+next+opportunity." alt="Typing animation" />
</a>

<br/>

<a href="https://github.com/SyedRaqi/Resume-analyzer"><img src="https://img.shields.io/badge/EXPLORE%20PROJECT-6366F1?style=for-the-badge&logo=github&logoColor=white" alt="Explore project"/></a>
&nbsp;
<a href="#-intelligence-modules"><img src="https://img.shields.io/badge/DISCOVER%20FEATURES-0891B2?style=for-the-badge&logo=rocket&logoColor=white" alt="Discover features"/></a>
&nbsp;
<a href="#-run-it-locally"><img src="https://img.shields.io/badge/RUN%20LOCALLY-DB2777?style=for-the-badge&logo=terminal&logoColor=white" alt="Run locally"/></a>

<br/><br/>

<img src="https://img.shields.io/badge/REACT-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React"/>
<img src="https://img.shields.io/badge/TYPESCRIPT-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/>
<img src="https://img.shields.io/badge/VITE-646CFF?style=flat-square&logo=vite&logoColor=white" alt="Vite"/>
<img src="https://img.shields.io/badge/FASTAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
<img src="https://img.shields.io/badge/PYTHON-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/SQLALCHEMY-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"/>
<img src="https://img.shields.io/badge/AI%20%2B%20NLP-8B5CF6?style=flat-square" alt="AI and NLP"/>

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0891B2,50:6366F1,100:DB2777&height=3" width="100%" alt="divider"/>

## 🌌 The Vision

> **The next opportunity shouldn't depend on guesswork.**

SmartHire AI turns career preparation into a structured, data-informed process. Understand your resume, compare your skills with real job requirements, find the gaps, and get practical guidance, all in one workspace.

<div align="center">
<img src="assets/smarthire-pipeline.svg" width="92%" alt="Animated flow: Upload, Analyze, Match, Advance" />
</div>

## 🧊 Intelligence Modules

<table>
<tr>
<td width="33%" valign="top">

### 📄 Resume Intelligence
Extracts and analyzes resume content with component assessments for skills, education, projects, experience, and structure.

</td>
<td width="33%" valign="top">

### 🎯 Job Match Engine
Compares resumes with job descriptions using skill coverage and TF-IDF cosine similarity.

</td>
<td width="33%" valign="top">

### 🧭 Skill-Gap Discovery
Shows matching and missing skills so you know where to prepare next.

</td>
</tr>
<tr>
<td width="33%" valign="top">

### 🤖 AI Career Assistant
Career guidance via optional OpenAI integration, with a local fallback for common questions.

</td>
<td width="33%" valign="top">

### 🗂️ Personal Workspace
Accounts, resumes, analysis history, job matches, conversations, and profile in one place.

</td>
<td width="33%" valign="top">

### 🔍 Explainable Results
Score components and matching signals stay visible instead of hiding behind one unexplained number.

</td>
</tr>
</table>

## 🛰️ Under the Hood

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

<details>
<summary><b>⚙️ Technology matrix (click to expand)</b></summary>

<br/>

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

</details>

## 🧮 Matching Methodology

<div align="center">

| 🧩 COMPONENT | 🔬 APPROACH |
|---|---|
| Resume extraction | PDF text extraction with PyMuPDF |
| Resume assessment | Component scores combined into an overall coaching score |
| Skill detection | Curated vocabulary and case-insensitive matching |
| Job similarity | TF-IDF vectorization and cosine similarity |
| **Job-match score** | **65% skill coverage + 35% text similarity** |
| Career guidance | Optional LLM integration or deterministic fallback |

</div>

> ⚠️ These scores are coaching signals, not official ATS scores or guarantees of hiring outcomes.

## 🚀 Run It Locally

**Requirements:** Python 3.11+ · Node.js 20+ · npm 10+ · Git

<details open>
<summary><b>01 · Clone</b></summary>

```powershell
git clone https://github.com/SyedRaqi/Resume-analyzer.git
cd Resume-analyzer
```
</details>

<details open>
<summary><b>02 · Start the backend</b></summary>

```powershell
cd backend
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn app.main:app --reload --port 8000
```

API docs: http://localhost:8000/docs
</details>

<details open>
<summary><b>03 · Start the frontend</b></summary>

Open a second terminal from the project root:

```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```

Open the URL printed by Vite, usually http://localhost:5173. Set the API base URL using the variable documented in `frontend/.env.example`.
</details>

<details>
<summary><b>04 · Optional AI configuration</b></summary>

Add your own key to `backend/.env` to enable the OpenAI-backed assistant:

```dotenv
OPENAI_API_KEY=your-api-key
OPENAI_MODEL=gpt-4o-mini
```

🔐 Never commit secrets or `.env` files to GitHub.
</details>

## 🛡️ Engineering & Security

- 🔑 JWT-based authentication and protected API workflows
- 👤 User-specific resume and conversation operations
- 🌱 Environment-based configuration for secrets
- 🗄️ SQLite for local development, PostgreSQL option
- 📑 PDF upload and processing workflow

> Before production deployment, verify file validation, access controls, persistent storage, CORS, token handling, rate limiting, and email delivery for password resets.

## 🗺️ Roadmap

- [ ] Semantic skill matching with embeddings
- [ ] Enhanced resume-improvement recommendations
- [ ] Curated job-source integration
- [ ] Background processing and durable file storage
- [ ] Automated tests and continuous integration
- [ ] Production monitoring and deployment hardening

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0891B2,50:6366F1,100:DB2777&height=140&section=footer&text=ENGINEER%20YOUR%20NEXT%20OPPORTUNITY&fontColor=ffffff&fontSize=24&fontAlignY=70" width="100%" alt="Animated footer"/>

**SmartHire AI** · Built by [Syed Raqi](https://github.com/SyedRaqi) · [⭐ Star the repo](https://github.com/SyedRaqi/Resume-analyzer)

<sub>Understand your profile. Discover your potential. Keep moving forward.</sub>

</div>
