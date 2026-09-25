# SmartHire AI

SmartHire AI is a full-stack career intelligence workspace for students and job seekers. It combines explainable resume analysis, job-description matching, improvement guidance, and a career chatbot in one focused interface.

## Architecture

- **Frontend:** React, TypeScript, Vite, React Router, Lucide React, Recharts-ready component surface, custom responsive CSS.
- **Backend:** FastAPI, Pydantic, SQLAlchemy, JWT authentication, secure upload handling.
- **Data:** SQLite by default for local development; PostgreSQL through `DATABASE_URL` for deployment.
- **AI/ML:** PyMuPDF PDF extraction, transparent weighted scoring, skill/entity detection, lexical and skill-overlap matching, configurable OpenAI chatbot with a local fallback.

## Project structure

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

## Prerequisites

- Python 3.11+
- Node.js 20+
- npm 10+
- Docker Desktop (optional, only needed for PostgreSQL)

## Local setup

### Backend

```powershell
cd backend
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn app.main:app --host 127.0.0.1 --reload --port 8000
```

The API and interactive docs are available at `http://localhost:8000/docs`.

### Frontend

```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```

Open `http://127.0.0.1:5173`.

### PostgreSQL option

```powershell
docker compose up -d postgres
```

Set this in `backend/.env` before starting the API:

```env
DATABASE_URL=postgresql+psycopg://smarthire:smarthire_dev@localhost:5432/smarthire
```

Install the PostgreSQL driver when using that URL:

```powershell
pip install psycopg[binary]
```

## AI configuration

OpenAI is optional. Add an API key to `backend/.env` to enable the LLM-backed assistant:

```env
OPENAI_API_KEY=your-key
OPENAI_MODEL=gpt-4o-mini
```

Without a key, the app uses a clearly bounded local fallback for common career questions. No secrets are sent to the browser.

## API surface

- `POST /api/auth/register`, `POST /api/auth/login`, `GET /api/auth/me`, `POST /api/auth/logout`
- `POST /api/auth/forgot-password`, `POST /api/auth/reset-password`
- `POST /api/resumes/upload`, `GET /api/resumes`, `DELETE /api/resumes/{id}`
- `POST /api/resumes/{id}/analyze`, `GET /api/resumes/{id}/analysis`
- `POST /api/jobs/match`, `GET /api/jobs/history`
- `POST /api/chat`, `GET /api/chat/conversations`, `GET /api/chat/conversations/{id}`, `DELETE /api/chat/conversations/{id}`
- `GET /api/users/profile`, `PUT /api/users/profile`

## Algorithm notes

1. **Resume extraction:** PyMuPDF reads each page and joins the text content.
2. **Resume score:** skills, education, projects, experience, and structure receive explicit 0-100 sub-scores. The overall score is their arithmetic mean and is presented as an internal coaching signal, never as an official ATS score.
3. **Skill gaps:** a curated skill vocabulary is matched case-insensitively against resume and job text. Matching and missing sets are persisted with the job match.
4. **Job matching:** the current implementation combines skill coverage (65%) with TF-IDF cosine similarity (35%). The two components remain visible as matching and missing skills plus a single coaching score.
5. **Chat:** the service keeps the last ten messages for context when an OpenAI key is configured; otherwise, deterministic fallback guidance answers common topics.

## Testing and verification

```powershell
# Backend syntax check
python -m compileall backend\app

# Frontend typecheck and production bundle
cd frontend
npm run build
```

For a complete manual smoke test: register, upload a text-based PDF, open the analysis, open the improvement page and print/export it as PDF, paste a job description, run a match, update the profile, request a password reset, then send a message in SmartHire Assistant. The reset endpoint creates expiring one-time tokens; connect it to an email provider before production use.

## Final-year presentation modules

- Problem definition and user journey
- Secure full-stack architecture
- Explainable resume scoring
- NLP extraction and skill gap analysis
- Job matching and recommendation logic
- Authenticated conversational AI
- Database design and ownership isolation
- Responsive UX and deployment strategy

## Future enhancements

- Replace the curated vocabulary with a versioned skills taxonomy and embeddings.
- Add Alembic migrations, background processing, object storage, rate limiting, and observability.
- Add resume improvement generation with human review and PDF export.
- Add role recommendation from a curated job source rather than treating pasted descriptions as live listings.
