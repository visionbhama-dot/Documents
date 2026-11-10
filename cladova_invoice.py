"""
Bhama Vision - invoice content for Cladova only.

Reuses the seller details, payment details and terms from `invoices.py`
so there is a single source of truth, and defines just the Cladova website
redesign invoice.

Build with:
    python3 build_cladova_invoice.py
"""
from invoices import COMPANY, PAYMENT, TERMS  # noqa: F401  (re-exported)

# ---------------------------------------------------------------------------
# Invoice(s) to render - only Cladova.
# ---------------------------------------------------------------------------
INVOICES = [
    {
        "id": "BV-INV-20261110-1200",
        "client": {
            "name": "Cladova",
            "lines": [],
        },
        "items": [
            {
                "desc": "Website redesign",
                "detail": "Redesign of the Cladova website",
                "qty": 1,
                "rate": 2999,
            },
        ],
    },
]
