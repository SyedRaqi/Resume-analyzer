import re
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


def validate_gmail_email(value: str) -> str:
    normalized = value.strip().lower()
    if not re.fullmatch(r"[a-z0-9._%+-]+@gmail\.com", normalized):
        raise ValueError("Email must be a valid Gmail address like name@gmail.com")
    return normalized


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: EmailStr) -> str:
        return validate_gmail_email(str(value))


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: EmailStr) -> str:
        return validate_gmail_email(str(value))


class UserUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: EmailStr) -> str:
        return validate_gmail_email(str(value))


class PasswordResetRequest(BaseModel):
    email: EmailStr

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: EmailStr) -> str:
        return validate_gmail_email(str(value))


class PasswordResetConfirm(BaseModel):
    token: str = Field(min_length=32, max_length=128)
    password: str = Field(min_length=8, max_length=128)


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    email: EmailStr
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut


class ResumeOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    filename: str
    uploaded_at: datetime


class AnalysisOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    resume_id: int
    overall_score: int
    skills_score: int
    education_score: int
    projects_score: int
    experience_score: int
    formatting_score: int
    extracted_data: dict[str, Any]
    suggestions: list[str]
    created_at: datetime


class JobMatchRequest(BaseModel):
    resume_id: int
    job_title: str | None = Field(default=None, min_length=2, max_length=200)
    job_description: str | None = Field(default=None, min_length=0, max_length=20000)

    @property
    def resolved_job_title(self) -> str:
        return self.job_title.strip() if self.job_title and self.job_title.strip() else "Target Role"

    @property
    def resolved_job_description(self) -> str:
        return self.job_description.strip() if self.job_description and self.job_description.strip() else "Role description not provided. Compare the candidate profile with the selected role title and available skills."


class JobMatchOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    resume_id: int
    job_title: str
    match_score: int
    matching_skills: list[str]
    missing_skills: list[str]
    created_at: datetime


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    conversation_id: int | None = None


class ChatResponse(BaseModel):
    reply: str
    conversation_id: int


class ConversationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    created_at: datetime
    updated_at: datetime


class ChatMessageOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    role: str
    content: str
    created_at: datetime
