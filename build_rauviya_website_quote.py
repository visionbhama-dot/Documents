"""
Bhama Vision - build the RAUVIYA luxury catalog website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `rauviya_website_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_rauviya_website_quote.py

Output is written to `output/`.
"""
import build_quotes
import rauviya_website_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = rauviya_website_quote

if __name__ == "__main__":
    build_quotes.build()
