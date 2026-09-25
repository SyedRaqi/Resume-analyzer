from fastapi import FastAPI

app = FastAPI(title="Resume Analyzer")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Resume Analyzer API"}
