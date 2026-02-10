import os
from backend.embed import get_embedding
from backend.endee_client import insert_vector

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB_DIR = os.path.join(BASE_DIR, "data", "jobs")

def ingest_jobs():
    if not os.path.isdir(JOB_DIR):
        raise RuntimeError(f"Job directory not found: {JOB_DIR}")

    for file in os.listdir(JOB_DIR):
        if file.endswith(".txt"):
            path = os.path.join(JOB_DIR, file)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            vector = get_embedding(text)
            insert_vector(vector, {
                "type": "job",
                "filename": file
            })

if __name__ == "__main__":
    ingest_jobs()
