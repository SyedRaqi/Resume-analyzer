import re
from pathlib import Path
from typing import Any

import fitz
from rapidocr_onnxruntime import RapidOCR
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ocr = RapidOCR()

SKILL_ALIASES = {
    "Python": ["python", "python 3", "py"],
    "Java": ["java"],
    "JavaScript": ["javascript", "js"],
    "TypeScript": ["typescript", "ts"],
    "React": ["react", "reactjs", "react.js"],
    "Node.js": ["node.js", "nodejs", "node js"],
    "FastAPI": ["fastapi"],
    "SQL": ["sql"],
    "PostgreSQL": ["postgresql", "postgre sql"],
    "Docker": ["docker"],
    "AWS": ["aws", "amazon web services"],
    "Git": ["git"],
    "Machine Learning": ["machine learning", "ml"],
    "Data Analysis": ["data analysis", "analytics"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "TensorFlow": ["tensorflow"],
    "Figma": ["figma"],
    "Communication": ["communication"],
    "Leadership": ["leadership"],
}


def extract_pdf_text(path: str) -> str:
    document = fitz.open(path)
    return "\n".join(page.get_text() for page in document).strip()


def extract_image_text(path: str) -> str:
    result, _ = ocr(path)
    if not result:
        return ""
    lines = [item[1] for item in result if item and len(item) > 1 and item[1]]
    return "\n".join(lines).strip()


def extract_resume_text(path: str, filename: str) -> str:
    lower_name = filename.lower()
    if lower_name.endswith(".pdf"):
        return extract_pdf_text(path)
    if lower_name.endswith((".png", ".jpg", ".jpeg", ".webp")):
        return extract_image_text(path)
    raise ValueError(f"Unsupported resume format: {filename}")


def _extract_skills(text: str) -> list[str]:
    lower = text.lower()
    found: list[str] = []
    for skill, aliases in SKILL_ALIASES.items():
        if any(re.search(rf"(?<![a-z]){re.escape(alias)}(?![a-z])", lower) for alias in aliases):
            found.append(skill)
    return found


def analyze_resume(text: str) -> dict[str, Any]:
    lower = text.lower()
    skills = _extract_skills(text)
    sections = {key: key in lower for key in ("education", "experience", "projects", "certifications")}
    email = re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
    phone = re.search(r"(?:\+?\d[\d\s().-]{8,}\d)", text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    structure = min(100, 45 + len(sections) * 10 + min(15, len(lines) // 8))
    scores = {
        "skills_score": min(100, 45 + len(skills) * 7),
        "education_score": 85 if sections["education"] else 35,
        "projects_score": 85 if sections["projects"] else 30,
        "experience_score": 85 if sections["experience"] else 30,
        "formatting_score": structure,
    }
    overall = round(sum(scores.values()) / len(scores))
    suggestions = []
    if skills:
        suggestions.append(f"Your resume already highlights {', '.join(skills[:3])}. Keep building on them with project outcomes and measurable impact.")
    else:
        suggestions.append("Add a clear skills section with specific technologies and tools used in your projects.")
    if not sections["projects"]: suggestions.append("Add a Projects section with measurable outcomes and the tools you used.")
    if not sections["experience"]: suggestions.append("Describe internships, freelance work, or practical experience with results.")
    if len(skills) < 6: suggestions.append("Add role-relevant technical skills and show them in project bullets.")
    if "summary" not in lower and "objective" not in lower: suggestions.append("Open with a concise professional summary tailored to your target role.")
    suggestions.append("Use action verbs and quantify results wherever possible.")
    return {**scores, "overall_score": overall, "extracted_data": {"email": email.group(0) if email else None, "phone": phone.group(0) if phone else None, "skills": skills, "sections": sections, "name": lines[0] if lines else "Unknown"}, "suggestions": suggestions}


def match_job(resume_text: str, job_description: str) -> dict[str, Any]:
    resume_skills = set(_extract_skills(resume_text))
    job_skills = set(_extract_skills(job_description))
    matching = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)
    matrix = TfidfVectorizer(stop_words="english").fit_transform([resume_text, job_description])
    lexical = round(float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0]) * 100)
    skill_score = round(len(matching) / max(1, len(job_skills)) * 100)
    return {"match_score": round(skill_score * 0.65 + lexical * 0.35), "matching_skills": matching, "missing_skills": missing}
