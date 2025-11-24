from fastapi import FastAPI, UploadFile, File
from services.audio_transcriber import transcribe_audio
from services.vector_db import load_vector_db
from services.accountant_agent import ask_agent
from services.invoice_service import create_invoice
from services.report_generator import generate_financial_report
from models.request_models import QueryModel, InvoiceModel, ReportModel

app = FastAPI(title="AI Finance Accountant Agent API (Gemini Version)")

vector_db = load_vector_db()

@app.get("/")
async def root():
    return {"message": "AI Finance Accountant Agent (Gemini) Running!"}

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    filename = f"temp_{file.filename}"
    with open(filename, "wb") as f:
        f.write(await file.read())
    text = transcribe_audio(filename)
    return {"transcription": text}

@app.post("/ask")
async def ask_finance(query: QueryModel):
    answer = ask_agent(query.query, vector_db)
    return {"answer": answer}

@app.post("/invoice")
async def generate_invoice(data: InvoiceModel):
    url = create_invoice(
        customer_email=data.customer_email,
        item_desc=data.item_desc,
        amount=data.amount
    )
    return {"invoice_url": url}

@app.post("/report")
async def report(data: ReportModel):
    output = generate_financial_report(data.data)
    return {"report": output}
