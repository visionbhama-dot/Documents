"""
Bhama Vision - invoice content for Doer Way Nex only.

Reuses the seller details, payment details and terms from `invoices.py`
so there is a single source of truth, and defines just the Doer Way Nex
invoice (ref. quotation BV-Q-2026-013).

Build with:
    python3 build_doerway_nex_invoice.py
"""
from invoices import COMPANY, PAYMENT, TERMS  # noqa: F401  (re-exported)

# ---------------------------------------------------------------------------
# Invoice(s) to render - only Doer Way Nex.
# ---------------------------------------------------------------------------
INVOICES = [
    {
        "id": "BV-INV-20260906-1200",
        "client": {
            "name": "Doer Way Nex",
            "lines": [],
        },
        "items": [
            {
                "desc": "Website + Admin Panel",
                "detail": "Design & development with case studies & services "
                          "management (ref. quotation BV-Q-2026-013)",
                "qty": 1,
                "rate": 5500,
            },
        ],
    },
]
