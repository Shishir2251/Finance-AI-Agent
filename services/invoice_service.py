import stripe
from config import STRIPE_KEY

stripe.api_key = STRIPE_KEY

def create_invoice(customer_email: str, item_desc: str, amount: float):
    customer = stripe.Customer.create(email=customer_email)

    stripe.InvoiceItem.create(
        customer=customer.id,
        description=item_desc,
        amount=int(amount * 100),
        currency="usd"
    )

    invoice = stripe.Invoice.create(customer=customer.id)
    return invoice.hosted_invoice_url
