📘 RAG System with Gemini API — README.md
🚀 Overview

This project is a Lightweight RAG (Retrieval-Augmented Generation) system that uses:

Gemini API (instead of OpenAI)

FAISS vector database

HuggingFace sentence-transformers for embeddings

Python CLI interface to ask questions

Chunk-based document retrieval

You can index any PDF/text → chunk → embed → store in FAISS → query using Gemini.

🧠 How the System Works (End-to-End)
1️⃣ Add PDFs or text

Place your PDFs inside:

data/raw_pdfs/

2️⃣ Convert PDFs to text

A script extracts text and saves into:

data/processed_text/

3️⃣ Chunk the text

Long documents are broken into small meaningful chunks (example: 300–500 tokens).

Output saved at:

data/chunks.json

4️⃣ Build Vector DB

Each chunk is embedded using:

sentence-transformers/all-MiniLM-L6-v2


Then inserted into FAISS:

data/faiss.index

5️⃣ Query the system

You ask:

python src/main.py --query "What is the cow referred to in Hinduism?"


System runs:

Embed your query

Retrieve the top relevant chunks

Send retrieved text + user query → Gemini API

Gemini generates a grounded, accurate answer

🧩 Folder Structure
project/
│
├─ src/
│  ├─ main.py                   # CLI entrypoint
│  ├─ rag.py                    # RAG pipeline using Gemini
│  ├─ vectorstore.py            # FAISS loading/building
│  └─ pdf_loader.py             # PDF → text processor
│
├─ data/
│  ├─ raw_pdfs/                 # Add your PDFs here
│  ├─ processed_text/           # Extracted text
│  ├─ faiss.index               # Vector DB
│  └─ chunks.json               # Text chunks
│
├─ requirements.txt
└─ README.md

📦 Installation
1. Create environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

2. Install requirements
pip install -r requirements.txt

3. Add Gemini API Key

Set the environment variable:

export GEMINI_API_KEY="your_key_here"


Windows:

set GEMINI_API_KEY=your_key_here

🔍 How to Use the System
Step 1 — Add your content

Put PDFs inside:

data/raw_pdfs/

Step 2 — Preprocess PDFs

Example command:

python src/pdf_loader.py

Step 3 — Build Vector DB
python src/vectorstore.py


This generates:

faiss.index

chunks.json

Step 4 — Ask any question

Example:

python src/main.py --query "What is the cow referred to in Hinduism?" \
--index-path data/faiss.index \
--chunks-path data/chunks.json

Sample Output
Top relevant chunks found…
Sending to Gemini…

Answer:
In Hinduism, the cow is referred to as "Gau Mata" (Mother Cow)…

🔥 Explanation of load_vector_db() (Your Latest Code)
db = FAISS.from_texts(docs, embedder)


What it does:

Loads all chunks from chunks.json

Creates embeddings using MiniLM

Stores vectors in FAISS index

Makes your RAG system ready for semantic search

🤖 Gemini Integration (RAG v2 Upgraded Pipeline)

Your upgraded RAG v2 uses:

Gemini 1.5 Flash / Pro

Fast response

Long context window

Best for RAG tasks

Flow:
query → embed → vector search → retrieve → Gemini → final answer

📝 Test Questions For Your Document

Given your sample document about Holy Cow, here are testing questions:

Why is the cow considered sacred in Hinduism?

What does the term "Gau Mata" mean?

How is the cow connected with purity or fertility?

What role does the cow play in agrarian life?

What symbolism does the cow represent in ancient texts?

Why is venerating the cow seen as protecting nature?

📚 Example Query You Used
python src/main.py --query "What is the cow referred to in Hinduism?" \
--index-path data/faiss.index \
--chunks-path data/chunks.json
