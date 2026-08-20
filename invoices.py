"""
Bhama Vision - invoice content.

Edit this file to change the client, line items, payment details or notes,
then run:
    python3 build_invoices.py

Seller/contact info is reused from quotations.py (COMPANY) so there is a
single source of truth for Bhama Vision's details.
"""
from quotations import COMPANY  # noqa: F401  (re-exported for the renderer)

# Where the money should be paid. Replace the placeholders with real details.
PAYMENT = {
    "account_name": "Prafull Kumar Sharma",
    "bank": "IndusInd Bank",
    "account_no": "158860640250",
    "ifsc": "INDB0000044",
    "upi": "8860640250@ybl",
}

# Invoice-wide terms.
TERMS = {
    "tax_percent": 0,       # set e.g. 18 to add an 18% GST line
    "notes": [
        "Amounts are in Indian Rupees (INR). GST extra, if applicable.",
        "Please share the payment reference once the transfer is done.",
    ],
}

# ---------------------------------------------------------------------------
# Invoices. Add more dicts to this list to generate more invoices.
# ---------------------------------------------------------------------------
INVOICES = [
    {
        "id": "BV-INV-20260806-1800",
        "client": {
            "name": "Bharat iON Systems",
            "lines": [
                "Attn: Accounts",
                "India",
            ],
        },
        "items": [
            {
                "desc": "Website Design",
                "detail": "Design and development of the company website",
                "qty": 1,
                "rate": 7500,
            },
            {
                "desc": "Catalog, Portfolio & Quotation, etc.",
                "detail": "Company catalogue, portfolio and quotation "
                          "documents / pages",
                "qty": 1,
                "rate": 3500,
            },
        ],
    },
    {
        "id": "BV-INV-20260818-1400",
        "client": {
            "name": "Cladova & Phomi",
            "lines": [],
        },
        "items": [
            {
                "desc": "Cladova - website edits",
                "qty": 1,
                "rate": 2500,
            },
            {
                "desc": "Phomi - website edits",
                "qty": 1,
                "rate": 1000,
            },
        ],
    },
]
