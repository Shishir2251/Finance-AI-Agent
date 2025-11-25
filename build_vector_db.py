# build_vector_db.py

import os
import json
import numpy as np
import faiss
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ==========================
# Paths
# ==========================
DATA_DIR = "data/raw_docs/"
VECTOR_DB_PATH = "vector_store.faiss"
CHUNKS_PATH = "chunks.json"

# ==========================
# Load Files
# ==========================
def load_documents():
    docs = []
    for file in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                docs.append(f.read())

        elif file.endswith(".pdf"):
            try:
                import pypdf
                reader = pypdf.PdfReader(path)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""
                docs.append(text)
            except Exception as e:
                print(f"❌ PDF read failed for {file}: {e}")

    return docs


# ==========================
# Split Text
# ==========================
def split_into_chunks(texts):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks


# ==========================
# Build FAISS DB
# ==========================
def build_faiss(chunks):
    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectors = embedder.embed_documents(chunks)

    dim = len(vectors[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors).astype("float32"))

    faiss.write_index(index, VECTOR_DB_PATH)
    print("✅ FAISS DB saved:", VECTOR_DB_PATH)

    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)
    print("✅ chunks.json saved:", CHUNKS_PATH)


# ==========================
# Main
# ==========================
if __name__ == "__main__":
    docs = load_documents()
    print(f"📄 Loaded {len(docs)} documents")

    chunks = split_into_chunks(docs)
    print(f"🧩 Generated {len(chunks)} chunks")

    if len(chunks) == 0:
        print("⚠️ No chunks generated — check your data/ folder!")
    else:
        build_faiss(chunks)
