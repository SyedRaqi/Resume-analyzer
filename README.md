<!-- SMART HIRE AI | MISSION CONTROL README -->

<div align="center">

<img src="assets/smarthire-banner.svg" width="100%" alt="SmartHire AI animated 3D banner: your resume, decoded" />

<a href="https://github.com/SyedRaqi/Resume-analyzer">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=900&color=A78BFA&center=true&vCenter=true&width=760&lines=Hiring+is+a+black+box.+Let%27s+open+it.;Your+resume+has+a+story.+We+check+if+it+gets+read.;Paste+a+job+post.+See+exactly+where+you+stand.;Stop+guessing.+Start+closing+gaps." alt="Typing animation" />
</a>

<br/>

<a href="https://github.com/SyedRaqi/Resume-analyzer"><img src="https://img.shields.io/badge/SEE%20THE%20CODE-6366F1?style=for-the-badge&logo=github&logoColor=white" alt="See the code"/></a>
&nbsp;
<a href="#-flight-modules"><img src="https://img.shields.io/badge/WHAT%20IT%20DOES-0891B2?style=for-the-badge&logo=rocket&logoColor=white" alt="What it does"/></a>
&nbsp;
<a href="#-launch-sequence"><img src="https://img.shields.io/badge/LAUNCH%20IT-DB2777?style=for-the-badge&logo=terminal&logoColor=white" alt="Launch it"/></a>

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

## 🛰️ Mission Brief

> **You can't fix what you can't see.**

Most people send out resumes and hope. SmartHire AI is a control room for that moment: it reads your resume, lines it up against the job you actually want, and points at the exact skills that are missing, so every application gets a little sharper than the last.

<div align="center">
<img src="assets/smarthire-pipeline.svg" width="92%" alt="Animated flow: Drop it, Decode, Compare, Level up" />
</div>

## 🧊 Flight Modules

<table>
<tr>
<td width="33%" valign="top">

### 📡 Resume Radar
Pulls the text out of your PDF and grades it in parts: skills, education, projects, experience, and structure. No single mystery score.

</td>
<td width="33%" valign="top">

### ⚖️ Job Fit Scale
Weighs your resume against a job post using skill coverage plus TF-IDF cosine similarity, so the match is more than keyword luck.

</td>
<td width="33%" valign="top">

### 🕳️ Gap Finder
Splits skills into "you have it" and "you're missing it," turning a vague worry into a short study list.

</td>
</tr>
<tr>
<td width="33%" valign="top">

### 💬 Co-Pilot
Ask career questions and get answers from OpenAI when you add a key, or from a built-in local fallback that handles common ones offline.

</td>
<td width="33%" valign="top">

### 🧰 Your Hangar
Accounts, uploaded resumes, past analyses, job matches, chats, and your profile, all saved in one private workspace.

</td>
<td width="33%" valign="top">

### 🪟 Glass-Box Scoring
Every score shows its ingredients. You see why a number moved, not just that it did.

</td>
</tr>
</table>

## ⚙️ Engine Room

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
<summary><b>🔩 Open the parts bin: full tech stack</b></summary>

<br/>

| PART | WHAT'S INSIDE |
|---|---|
| Cockpit (UI) | React, TypeScript, Vite, React Router |
| Paint job | Responsive CSS, Lucide React |
| Brain (API) | Python, FastAPI, Pydantic |
| Memory | SQLAlchemy, SQLite, PostgreSQL option |
| PDF reader | PyMuPDF |
| Matchmaking math | TF-IDF, cosine similarity, skill overlap |
| Locks | JWT-based authentication |
| Voice | Optional OpenAI integration and local fallback |

</details>

## 🧪 The Scoring Recipe

<div align="center">

| 🥄 STEP | 🔬 HOW IT'S DONE |
|---|---|
| Read the PDF | Text extraction with PyMuPDF |
| Grade the resume | Component scores blended into one coaching score |
| Spot the skills | Curated vocabulary, case-insensitive matching |
| Compare the wording | TF-IDF vectors and cosine similarity |
| **Final job-fit number** | **65% skill coverage + 35% text similarity** |
| Offer advice | Optional LLM, or a deterministic fallback |

</div>

> 🧭 Treat these as a compass, not a verdict. They are coaching signals, not official ATS scores, and they can't promise a hiring outcome.

## 🚀 Launch Sequence

<div align="center">
<img src="assets/smarthire-launch.svg" width="92%" alt="Animated launch sequence: clone, backend, frontend, live" />
</div>

### 🧾 Pre-flight checklist

<div align="center">

<img src="https://img.shields.io/badge/PYTHON-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11+"/>
<img src="https://img.shields.io/badge/NODE.JS-20%2B-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js 20+"/>
<img src="https://img.shields.io/badge/NPM-10%2B-CB3837?style=for-the-badge&logo=npm&logoColor=white" alt="npm 10+"/>
<img src="https://img.shields.io/badge/GIT-READY-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>

</div>

### 📍 Where everything lands

| 🛰️ WHAT | 🔗 WHERE |
|---|---|
| Backend API | `http://localhost:8000` |
| Live API docs | `http://localhost:8000/docs` |
| Frontend app | `http://localhost:5173` (or the URL Vite prints) |

> 🧑‍🚀 **Ground control tip:** the backend and frontend each keep a terminal busy, so open two.

### 🔥 Stage 1 · Ignition: get the code

```powershell
git clone https://github.com/SyedRaqi/Resume-analyzer.git
cd Resume-analyzer
```

### ⚙️ Stage 2 · Engine burn: start the backend

```powershell
cd backend
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn app.main:app --reload --port 8000
```

✅ Success looks like: the API docs open at http://localhost:8000/docs.

### 🌠 Stage 3 · Ascent: start the frontend

In a **second terminal**, from the project root:

```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```

If the app needs an API address, set it using the variable named in `frontend/.env.example`.

### 🛸 Stage 4 · Orbit: open it

Visit the URL Vite prints, usually http://localhost:5173. Upload a resume and you're flying.

<details>
<summary><b>🤖 Bonus stage: wake the Co-Pilot (optional)</b></summary>

<br/>

Drop your own key into `backend/.env` to switch on the OpenAI-powered assistant:

```dotenv
OPENAI_API_KEY=your-api-key
OPENAI_MODEL=gpt-4o-mini
```

🔐 Keys stay on your machine. Never commit secrets or `.env` files to GitHub.

</details>

## 🔒 Safety Checks

- 🔑 JWT-based login, with protected API routes
- 👤 Resume and chat actions are tied to the signed-in user
- 🌱 Secrets live in environment variables, not in code
- 🗄️ SQLite for easy local work, PostgreSQL when you need more
- 📑 A complete PDF upload-and-processing pipeline

> ⚠️ Before going public, double-check file validation, access controls, persistent storage, CORS, token handling, rate limiting, and password-reset email delivery.

## 🌠 Next Launches

- [ ] Smarter skill matching with embeddings, so related skills count too
- [ ] Sharper, more specific resume-improvement tips
- [ ] Pull in curated job listings
- [ ] Background processing and durable file storage
- [ ] Automated tests and continuous integration
- [ ] Production monitoring and deployment hardening

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0891B2,50:6366F1,100:DB2777&height=140&section=footer&text=OPEN%20THE%20BLACK%20BOX&fontColor=ffffff&fontSize=26&fontAlignY=70" width="100%" alt="Footer: open the black box"/>

**SmartHire AI** · Built by [Syed Raqi](https://github.com/SyedRaqi) · [⭐ Star it if it helped](https://github.com/SyedRaqi/Resume-analyzer)

<sub>See your profile clearly. Know your gaps. Apply with confidence.</sub>

</div>
