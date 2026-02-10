from fastapi import FastAPI
from pydantic import BaseModel
from backend.embed import get_embedding
from backend.endee_client import search_vector

app = FastAPI(title="Resume–Job Matching using Endee")

# ---------- Request Schemas ----------

class JobRequest(BaseModel):
    job_description: str

class ResumeRequest(BaseModel):
    resume_text: str


# ---------- APIs ----------

@app.post("/match_job_to_resumes")
def match_job(request: JobRequest):
    vector = get_embedding(request.job_description)
    return search_vector(vector, top_k=5)

@app.post("/match_resume_to_jobs")
def match_resume(request: ResumeRequest):
    vector = get_embedding(request.resume_text)
    return search_vector(vector, top_k=5)

@app.get("/")
def root():
    return {
        "message": "Resume–Job Matching API is running. Visit /docs for Swagger UI."
    }

