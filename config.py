import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI API KEY")
STRIPE_KEY = os.getenv("STRIPE KEY")
