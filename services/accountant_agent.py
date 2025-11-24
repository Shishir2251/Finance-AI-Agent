import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def ask_agent(query: str, vector_db):
    if vector_db is None:
        return "Vector DB is not loaded."

    docs = vector_db.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
You are a financial accountant AI. Use this context to answer:

CONTEXT:
{context}

QUESTION:
{query}
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text
