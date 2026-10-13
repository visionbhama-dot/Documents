"""
Bhama Vision - build the optical store (6k) quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `optical_store_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_optical_store_quote.py

Output is written to `output/`.
"""
import build_quotes
import optical_store_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = optical_store_quote

if __name__ == "__main__":
    build_quotes.build()
