"""
Bhama Vision - receipt content.

Edit this file to change the payer, amount, payment mode or notes, then run:
    python3 build_receipts.py

Seller/contact info is reused from quotations.py (COMPANY) and the bank
details from invoices.py (PAYMENT) so there is a single source of truth.
"""
from quotations import COMPANY  # noqa: F401  (re-exported for the renderer)

# NOTE: no PAYMENT block here on purpose - this payment was received into a
# different account, so bank details are intentionally omitted from the
# receipt. Define a PAYMENT dict here (see invoices.py) if a future receipt
# should show "Paid to" bank details.

# Receipt-wide terms / notes.
TERMS = {
    "notes": [
        "Amounts are in Indian Rupees (INR).",
        "This receipt acknowledges the amount received in full as stated above.",
    ],
}

# ---------------------------------------------------------------------------
# Receipts. Add more dicts to this list to generate more receipts.
# ---------------------------------------------------------------------------
RECEIPTS = [
    {
        "id": "BV-RCP-20260916-1200",
        "from": {
            "name": "WantX (OPC) Private Limited",
            "lines": [],
        },
        "amount": 30000,
        # Optional extras (leave as None / remove if not needed):
        "for": "app development",   # purpose of payment
        "mode": "Bank Transfer",    # payment method
    },
]
