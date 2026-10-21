"""
Bhama Vision - build the WantX revised-budget quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `wantx_revised_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_wantx_revised_quote.py

Output is written to `output/`.
"""
import build_quotes
import wantx_revised_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = wantx_revised_quote

if __name__ == "__main__":
    build_quotes.build()
