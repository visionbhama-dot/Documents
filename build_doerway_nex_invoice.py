"""
Bhama Vision - build the Doer Way Nex invoice PDF only.

Reuses the existing invoice renderer in `build_invoices.py` but drives it
with the content in `doerway_nex_invoice.py`, so only the Doer Way Nex
invoice is generated and the other invoices are left untouched.

    python3 build_doerway_nex_invoice.py

Output is written to `output/`.
"""
import build_invoices
import doerway_nex_invoice

# Swap the content module the renderer reads from, then build as usual.
build_invoices.data = doerway_nex_invoice

if __name__ == "__main__":
    build_invoices.build()
