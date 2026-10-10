"""
Bhama Vision - build the 10-product e-commerce (9k) quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `ecommerce_10products_quote.py`, so the branded look
stays 100% consistent with the other quotations.

    python3 build_ecommerce_10products_quote.py

Output is written to `output/`.
"""
import build_quotes
import ecommerce_10products_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = ecommerce_10products_quote

if __name__ == "__main__":
    build_quotes.build()
