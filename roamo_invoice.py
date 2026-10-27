"""
Bhama Vision - invoice content for ROAMO Pencils only.

Marketplace account-management monthly retainer across Amazon, Meesho and
Flipkart. Reuses the seller and payment details from `invoices.py`, but
defines its own TERMS so that GST is not mentioned anywhere on this
invoice.

Build with:
    python3 build_roamo_invoice.py
"""
from invoices import COMPANY, PAYMENT  # noqa: F401  (re-exported)

# Invoice-wide terms. Kept separate from invoices.py so this invoice makes
# no mention of GST at all.
TERMS = {
    "tax_percent": 0,       # no tax line is rendered
    "notes": [
        "Amounts are in Indian Rupees (INR).",
        "This is a monthly retainer for marketplace account management; "
        "the fee recurs each month until cancelled.",
        "Marketplace commissions, ad spend, shipping and other platform "
        "charges are billed by the marketplaces directly and are not part "
        "of this invoice.",
        "Please share the payment reference once the transfer is done.",
    ],
}

# ---------------------------------------------------------------------------
# Invoice(s) to render - only ROAMO Pencils.
# ---------------------------------------------------------------------------
INVOICES = [
    {
        "id": "BV-INV-20261010-1100",
        "client": {
            "name": "ROAMO Pencils",
            "lines": [],
        },
        "items": [
            {
                "desc": "Amazon account management",
                "detail": "Monthly retainer - listings, catalogue, orders & "
                          "performance management",
                "qty": 1,
                "rate": 4000,
            },
            {
                "desc": "Meesho account management",
                "detail": "Monthly retainer - listings, catalogue, orders & "
                          "performance management",
                "qty": 1,
                "rate": 3500,
            },
            {
                "desc": "Flipkart account management",
                "detail": "Monthly retainer - listings, catalogue, orders & "
                          "performance management",
                "qty": 1,
                "rate": 3500,
            },
        ],
    },
]
