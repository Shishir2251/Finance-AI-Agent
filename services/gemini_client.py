# gemini_client.py
import google.generativeai as genai
import os

# Load GEMINI API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY is None:
    raise ValueError("❌ GEMINI_API_KEY is not set in environment variables")

genai.configure(api_key=GEMINI_API_KEY)

# You can change model here if needed
MODEL_NAME = "gemini-1.5-flash"

def generate_gemini_response(prompt: str) -> str:
    """Send a prompt to Gemini and return text response."""
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"
