"""
Bhama Vision - build the Aviraj Enterprises website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `aviraj_enterprises_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_aviraj_enterprises_quote.py

Output is written to `output/`.
"""
import build_quotes
import aviraj_enterprises_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = aviraj_enterprises_quote

if __name__ == "__main__":
    build_quotes.build()
