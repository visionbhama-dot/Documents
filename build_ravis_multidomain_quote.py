"""
Bhama Vision - build the Ravis Enterprises multi-domain website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `ravis_multidomain_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_ravis_multidomain_quote.py

Output is written to `output/`.
"""
import build_quotes
import ravis_multidomain_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = ravis_multidomain_quote

if __name__ == "__main__":
    build_quotes.build()
