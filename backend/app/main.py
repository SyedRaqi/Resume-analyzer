from contextlib import asynccontextmanager
from pathlib import Path
from datetime import datetime, timedelta, timezone
from hashlib import sha256
from secrets import token_urlsafe
from uuid import uuid4

from fastapi import Depends, FastAPI, File, HTTPException, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Base, engine, ensure_storage, get_db, settings
from .deps import current_user
from .models import ChatMessage, Conversation, JobMatch, PasswordResetToken, Resume, ResumeAnalysis, User
from .schemas import AnalysisOut, ChatMessageOut, ChatRequest, ChatResponse, ConversationOut, JobMatchOut, JobMatchRequest, PasswordResetConfirm, PasswordResetRequest, ResumeOut, Token, UserCreate, UserLogin, UserOut, UserUpdate
from .security import create_access_token, hash_password, verify_password
from .services.chatbot_service import answer
from .services.resume_service import analyze_resume, extract_resume_text, match_job

@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    ensure_storage()
    yield

app = FastAPI(
    title="SmartHire AI API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://syedraqi.github.io",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root() -> dict[str, str]:
    return {"service": "SmartHire AI API", "docs": "/docs", "health": "/api/health"}


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "SmartHire AI"}


@app.post("/api/auth/register", response_model=Token, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)) -> Token:
    if db.scalar(select(User).where(User.email == payload.email.lower())):
        raise HTTPException(status_code=409, detail="An account with this email already exists")
    user = User(name=payload.name.strip(), email=payload.email.lower(), password_hash=hash_password(payload.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return Token(access_token=create_access_token(user.id), user=user)


@app.post("/api/auth/login", response_model=Token)
def login(payload: UserLogin, db: Session = Depends(get_db)) -> Token:
    user = db.scalar(select(User).where(User.email == payload.email.lower()))
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return Token(access_token=create_access_token(user.id), user=user)


@app.get("/api/auth/me", response_model=UserOut)
def me(user: User = Depends(current_user)) -> User:
    return user


@app.post("/api/auth/logout")
def logout(user: User = Depends(current_user)) -> dict[str, str]:
    return {"message": "Logged out. Remove the access token on the client."}


@app.post("/api/auth/forgot-password")
def forgot_password(payload: PasswordResetRequest, db: Session = Depends(get_db)) -> dict[str, str]:
    user = db.scalar(select(User).where(User.email == payload.email.lower()))
    if user:
        raw_token = token_urlsafe(48)
        db.add(PasswordResetToken(user_id=user.id, token_hash=sha256(raw_token.encode()).hexdigest(), expires_at=datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(minutes=30)))
        db.commit()
        # A mail provider can consume this token without changing the API contract.
    return {"message": "If an account exists, reset instructions will be sent shortly."}


@app.post("/api/auth/reset-password")
def reset_password(payload: PasswordResetConfirm, db: Session = Depends(get_db)) -> dict[str, str]:
    token = db.scalar(select(PasswordResetToken).where(PasswordResetToken.token_hash == sha256(payload.token.encode()).hexdigest(), PasswordResetToken.used_at.is_(None)))
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    if not token or token.expires_at < now:
        raise HTTPException(status_code=400, detail="Reset token is invalid or expired")
    token.user.password_hash = hash_password(payload.password)
    token.used_at = now
    db.commit()
    return {"message": "Password updated successfully"}


@app.get("/api/users/profile", response_model=UserOut)
def profile(user: User = Depends(current_user)) -> User:
    return user


@app.put("/api/users/profile", response_model=UserOut)
def update_profile(payload: UserUpdate, user: User = Depends(current_user), db: Session = Depends(get_db)) -> User:
    existing = db.scalar(select(User).where(User.email == payload.email.lower(), User.id != user.id))
    if existing:
        raise HTTPException(status_code=409, detail="That email is already in use")
    user.name = payload.name.strip()
    user.email = payload.email.lower()
    db.commit()
    db.refresh(user)
    return user


@app.post("/api/resumes/upload", response_model=ResumeOut, status_code=status.HTTP_201_CREATED)
def upload_resume(file: UploadFile = File(...), user: User = Depends(current_user), db: Session = Depends(get_db)) -> Resume:
    lower_name = (file.filename or "").lower()
    allowed_extensions = (".pdf", ".png", ".jpg", ".jpeg", ".webp")
    is_supported_type = (file.content_type in {"application/pdf", "image/png", "image/jpeg", "image/webp"} or lower_name.endswith(allowed_extensions))
    if not is_supported_type:
        raise HTTPException(status_code=400, detail="Only PDF and image resumes are supported")
    content = file.file.read()
    if len(content) > 10 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="Resume must be 10 MB or smaller")
    original_suffix = Path(lower_name).suffix.lower() if lower_name else ".pdf"
    safe_name = f"{uuid4().hex}{original_suffix}"
    path = Path(settings.upload_dir).resolve() / safe_name
    path.write_bytes(content)
    try:
        text = extract_resume_text(str(path), file.filename or safe_name)
    except Exception as exc:
        path.unlink(missing_ok=True)
        raise HTTPException(status_code=400, detail="The resume could not be read") from exc
    resume = Resume(user_id=user.id, filename=file.filename, file_path=str(path), extracted_text=text)
    db.add(resume)
    db.commit()
    db.refresh(resume)
    return resume


@app.get("/api/resumes", response_model=list[ResumeOut])
def list_resumes(user: User = Depends(current_user), db: Session = Depends(get_db)) -> list[Resume]:
    return list(db.scalars(select(Resume).where(Resume.user_id == user.id).order_by(Resume.uploaded_at.desc())))


def owned_resume(resume_id: int, user: User, db: Session) -> Resume:
    resume = db.scalar(select(Resume).where(Resume.id == resume_id, Resume.user_id == user.id))
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return resume


@app.post("/api/resumes/{resume_id}/analyze", response_model=AnalysisOut)
def create_analysis(resume_id: int, user: User = Depends(current_user), db: Session = Depends(get_db)) -> ResumeAnalysis:
    resume = owned_resume(resume_id, user, db)
    data = analyze_resume(resume.extracted_text)
    analysis = ResumeAnalysis(resume_id=resume.id, **data)
    db.add(analysis)
    db.commit()
    db.refresh(analysis)
    return analysis


@app.get("/api/resumes/{resume_id}/analysis", response_model=AnalysisOut)
def latest_analysis(resume_id: int, user: User = Depends(current_user), db: Session = Depends(get_db)) -> ResumeAnalysis:
    resume = owned_resume(resume_id, user, db)
    analysis = db.scalar(select(ResumeAnalysis).where(ResumeAnalysis.resume_id == resume.id).order_by(ResumeAnalysis.created_at.desc()))
    if not analysis:
        raise HTTPException(status_code=404, detail="Analyze this resume first")
    return analysis


@app.delete("/api/resumes/{resume_id}")
def delete_resume(resume_id: int, user: User = Depends(current_user), db: Session = Depends(get_db)) -> dict[str, str]:
    resume = owned_resume(resume_id, user, db)
    Path(resume.file_path).unlink(missing_ok=True)
    db.delete(resume)
    db.commit()
    return {"message": "Resume deleted"}


@app.post("/api/jobs/match", response_model=JobMatchOut)
def create_match(payload: JobMatchRequest, user: User = Depends(current_user), db: Session = Depends(get_db)) -> JobMatch:
    resume = owned_resume(payload.resume_id, user, db)
    job_title = payload.resolved_job_title
    job_description = payload.resolved_job_description
    result = match_job(resume.extracted_text, job_description)
    match = JobMatch(resume_id=resume.id, job_title=job_title, job_description=job_description, **result)
    db.add(match)
    db.commit()
    db.refresh(match)
    return match


@app.get("/api/jobs/history", response_model=list[JobMatchOut])
def job_history(user: User = Depends(current_user), db: Session = Depends(get_db)) -> list[JobMatch]:
    return list(db.scalars(select(JobMatch).join(Resume).where(Resume.user_id == user.id).order_by(JobMatch.created_at.desc())))


@app.post("/api/chat", response_model=ChatResponse)
def chat(payload: ChatRequest, user: User = Depends(current_user), db: Session = Depends(get_db)) -> ChatResponse:
    conversation = db.get(Conversation, payload.conversation_id) if payload.conversation_id else None
    if conversation and conversation.user_id != user.id:
        raise HTTPException(status_code=404, detail="Conversation not found")
    if not conversation:
        conversation = Conversation(user_id=user.id, title=payload.message[:60])
        db.add(conversation)
        db.flush()
    history = [{"role": item.role, "content": item.content} for item in conversation.messages]
    reply = answer(payload.message, history)
    db.add_all([ChatMessage(conversation_id=conversation.id, role="user", content=payload.message), ChatMessage(conversation_id=conversation.id, role="assistant", content=reply)])
    db.commit()
    return ChatResponse(reply=reply, conversation_id=conversation.id)


@app.get("/api/chat/conversations", response_model=list[ConversationOut])
def conversations(user: User = Depends(current_user), db: Session = Depends(get_db)) -> list[Conversation]:
    return list(db.scalars(select(Conversation).where(Conversation.user_id == user.id).order_by(Conversation.updated_at.desc())))


@app.get("/api/chat/conversations/{conversation_id}", response_model=list[ChatMessageOut])
def conversation_messages(conversation_id: int, user: User = Depends(current_user), db: Session = Depends(get_db)) -> list[ChatMessage]:
    conversation = db.scalar(select(Conversation).where(Conversation.id == conversation_id, Conversation.user_id == user.id))
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return list(db.scalars(select(ChatMessage).where(ChatMessage.conversation_id == conversation_id).order_by(ChatMessage.created_at)))


@app.delete("/api/chat/conversations/{conversation_id}")
def delete_conversation(conversation_id: int, user: User = Depends(current_user), db: Session = Depends(get_db)) -> dict[str, str]:
    conversation = db.scalar(select(Conversation).where(Conversation.id == conversation_id, Conversation.user_id == user.id))
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    db.delete(conversation)
    db.commit()
    return {"message": "Conversation deleted"}
