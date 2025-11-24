import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_financial_report(data):
    prompt = f"""
Create a structured financial report from the following data:

{data}

Include:
- Revenue
- Expenses
- Net Profit
- Observations
- Suggestions
    """

    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)

    return response.text
