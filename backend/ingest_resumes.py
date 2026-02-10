import os
import fitz
from backend.embed import get_embedding
from backend.endee_client import insert_vector

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESUME_DIR = os.path.join(BASE_DIR, "data", "resumes")

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    return " ".join(page.get_text() for page in doc)

def ingest_resumes():
    if not os.path.isdir(RESUME_DIR):
        raise RuntimeError(f"Resume directory not found: {RESUME_DIR}")

    for file in os.listdir(RESUME_DIR):
        if file.endswith(".pdf"):
            path = os.path.join(RESUME_DIR, file)
            text = extract_text(path)
            vector = get_embedding(text)

            insert_vector(vector, {
                "type": "resume",
                "filename": file
            })

if __name__ == "__main__":
    ingest_resumes()
