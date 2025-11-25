import json
import os
import faiss
import numpy as np
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTOR_DB_PATH = "vector_store.faiss"
CHUNKS_PATH = "chunks.json"

def load_vector_db():
    # Check files exist
    if not os.path.exists(VECTOR_DB_PATH):
        print(" FAISS index not found:", VECTOR_DB_PATH)
        return None

    if not os.path.exists(CHUNKS_PATH):
        print(" chunks.json not found:", CHUNKS_PATH)
        return None

    # Load chunks
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    # Load FAISS index
    index = faiss.read_index(VECTOR_DB_PATH)

    # Load embedder (same model used in build_vector_db.py)
    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("✅ Vector DB loaded successfully")
    
    return {
        "index": index,
        "chunks": chunks,
        "embedder": embedder
    }
