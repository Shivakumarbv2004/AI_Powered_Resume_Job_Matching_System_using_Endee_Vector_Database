import requests

ENDEE_URL = "http://localhost:8080"
INDEX_NAME = "resume_job_index"

def create_index():
    payload = {
        "dimension": 384,
        "metric": "cosine"
    }
    # Safe to call multiple times
    requests.post(f"{ENDEE_URL}/index/{INDEX_NAME}/create", json=payload)

def insert_vector(vector, metadata):
    payload = {
        "data": [
            {
                "id": metadata["filename"],
                "values": vector,
                "metadata": metadata
            }
        ]
    }

    r = requests.post(
        f"{ENDEE_URL}/index/{INDEX_NAME}/add",
        json=payload
    )
    r.raise_for_status()

def search_vector(vector, top_k=5):
    payload = {
        "vector": vector,
        "top_k": top_k
    }

    r = requests.post(
        f"{ENDEE_URL}/index/{INDEX_NAME}/search",
        json=payload
    )
    r.raise_for_status()
    return r.json()
