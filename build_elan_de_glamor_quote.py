"""
Bhama Vision - build the Elan De Glamor fragrance website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `elan_de_glamor_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_elan_de_glamor_quote.py

Output is written to `output/`.
"""
import build_quotes
import elan_de_glamor_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = elan_de_glamor_quote

if __name__ == "__main__":
    build_quotes.build()
