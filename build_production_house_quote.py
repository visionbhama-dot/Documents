"""
Bhama Vision - build the production-house website + admin quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `production_house_quote.py`, so the branded look stays
consistent with the other quotations.

    python3 build_production_house_quote.py

Output is written to `output/`.
"""
import build_quotes
import production_house_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = production_house_quote

if __name__ == "__main__":
    build_quotes.build()
