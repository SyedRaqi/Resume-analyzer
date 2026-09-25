import sys
from uuid import uuid4

sys.path.insert(0, "backend")

from fastapi.testclient import TestClient

from app.main import app


def test_health() -> None:
    response = TestClient(app).get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_register_login_and_profile_update() -> None:
    email = f"{uuid4().hex}@gmail.com"
    with TestClient(app) as client:
        registered = client.post("/api/auth/register", json={"name": "Test Candidate", "email": email, "password": "strong-password"})
        assert registered.status_code == 201
        token = registered.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        profile = client.get("/api/users/profile", headers=headers)
        assert profile.status_code == 200
        updated = client.put("/api/users/profile", headers=headers, json={"name": "Updated Candidate", "email": email})
        assert updated.status_code == 200
        assert updated.json()["name"] == "Updated Candidate"
        login = client.post("/api/auth/login", json={"email": email, "password": "strong-password"})
        assert login.status_code == 200


def test_invalid_email_is_rejected() -> None:
    response = TestClient(app).post("/api/auth/register", json={"name": "Test Candidate", "email": "not-an-email", "password": "strong-password"})
    assert response.status_code == 422

    response = TestClient(app).post("/api/auth/register", json={"name": "Test Candidate", "email": "test@outlook.com", "password": "strong-password"})
    assert response.status_code == 422


def test_resume_skills_are_extracted_from_text() -> None:
    from app.services.resume_service import analyze_resume

    result = analyze_resume("Python developer with React, FastAPI, SQL, and PostgreSQL experience. Built dashboards with JavaScript and Docker.")
    skills = result["extracted_data"]["skills"]
    assert "Python" in skills
    assert "React" in skills
    assert "FastAPI" in skills
    assert "SQL" in skills
    assert "PostgreSQL" in skills
    assert bool(skills)


def test_png_resume_upload_is_accepted() -> None:
    from PIL import Image, ImageDraw

    image = Image.new("RGB", (700, 260), "white")
    draw = ImageDraw.Draw(image)
    draw.text((40, 40), "Python React SQL FastAPI", fill="black")
    image_bytes = __import__("io").BytesIO()
    image.save(image_bytes, format="PNG")

    with TestClient(app) as client:
        registered = client.post("/api/auth/register", json={"name": "PNG User", "email": f"{uuid4().hex}@gmail.com", "password": "strong-password"})
        token = registered.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        response = client.post(
            "/api/resumes/upload",
            files={"file": ("resume.png", image_bytes.getvalue(), "image/png")},
            headers=headers,
        )
        assert response.status_code == 201
        assert response.json()["filename"] == "resume.png"


def test_job_matching_accepts_optional_role_title_and_description() -> None:
    from PIL import Image, ImageDraw

    image = Image.new("RGB", (700, 260), "white")
    draw = ImageDraw.Draw(image)
    draw.text((40, 40), "Python React SQL FastAPI", fill="black")
    image_bytes = __import__("io").BytesIO()
    image.save(image_bytes, format="PNG")

    with TestClient(app) as client:
        registered = client.post("/api/auth/register", json={"name": "Role User", "email": f"{uuid4().hex}@gmail.com", "password": "strong-password"})
        token = registered.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        resume_response = client.post(
            "/api/resumes/upload",
            files={"file": ("resume.png", image_bytes.getvalue(), "image/png")},
            headers=headers,
        )
        assert resume_response.status_code == 201
        resume_id = resume_response.json()["id"]

        response = client.post(
            "/api/jobs/match",
            json={"resume_id": resume_id, "job_title": "Frontend Engineer"},
            headers=headers,
        )
        assert response.status_code == 200
        assert response.json()["job_title"] == "Frontend Engineer"

        response = client.post(
            "/api/jobs/match",
            json={"resume_id": resume_id},
            headers=headers,
        )
        assert response.status_code == 200
        assert response.json()["job_title"] == "Target Role"


def test_authentication_is_required() -> None:
    response = TestClient(app).get("/api/resumes")
    assert response.status_code == 401
