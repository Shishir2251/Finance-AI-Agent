import json
import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_vector_db(index_path="data/faiss.index", chunks_path="data/chunks.json"):
    if not os.path.exists(chunks_path):
        print("⚠️ chunks.json not found")
        return None

    with open(chunks_path, "r", encoding="utf-8") as f:
        docs = json.load(f)

    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Build FAISS from text list
    db = FAISS.from_texts(docs, embedder)

    return db
