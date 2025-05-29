from fastapi import FastAPI, Request
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

app = FastAPI()
model = SentenceTransformer('all-MiniLM-L6-v2')
docs = ["TSMC earnings beat expectations", "Samsung misses estimates"]
index = faiss.IndexFlatL2(384)
embeddings = model.encode(docs)
index.add(np.array(embeddings).astype("float32"))

@app.post("/retrieve/docs")
def retrieve(request: Request):
    body = await request.json()
    query = body["query"]
    q_vec = model.encode([query])
    D, I = index.search(np.array(q_vec).astype("float32"), k=2)
    results = [docs[i] for i in I[0]]
    return {"results": results}