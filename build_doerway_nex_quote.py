"""
Bhama Vision - build the Doer Way Nex website + admin quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `doerway_nex_quote.py`, so the branded look stays
consistent with the other quotations.

    python3 build_doerway_nex_quote.py

Output is written to `output/`.
"""
import build_quotes
import doerway_nex_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = doerway_nex_quote

if __name__ == "__main__":
    build_quotes.build()
