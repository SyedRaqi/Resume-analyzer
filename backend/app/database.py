from collections.abc import Generator
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Settings(BaseSettings):
    database_url: str = "sqlite:///./smarthire.db"
    jwt_secret: str = "change-me-in-production"
    access_token_expire_minutes: int = 1440
    upload_dir: str = "../uploads"
    frontend_origin: str = "http://localhost:5173"
    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine = create_engine(settings.database_url, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def ensure_storage() -> None:
    Path(settings.upload_dir).resolve().mkdir(parents=True, exist_ok=True)
