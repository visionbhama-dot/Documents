"""
Bhama Vision - build the ROAMO Pencils invoice PDF only.

Reuses the existing invoice renderer in `build_invoices.py` but drives it
with the content in `roamo_invoice.py`, so only the ROAMO Pencils invoice
is generated and the other invoices are left untouched.

    python3 build_roamo_invoice.py

Output is written to `output/`.
"""
import build_invoices
import roamo_invoice

# Swap the content module the renderer reads from, then build as usual.
build_invoices.data = roamo_invoice

if __name__ == "__main__":
    build_invoices.build()
