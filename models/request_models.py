from pydantic import BaseModel

class QueryModel(BaseModel):
    query: str

class InvoiceModel(BaseModel):
    customer_email: str
    item_desc: str
    amount: float

class ReportModel(BaseModel):
    data: str
