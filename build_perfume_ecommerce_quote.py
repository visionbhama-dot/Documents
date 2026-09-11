"""
Bhama Vision - build the perfume brand e-commerce website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `perfume_ecommerce_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_perfume_ecommerce_quote.py

Output is written to `output/`.
"""
import build_quotes
import perfume_ecommerce_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = perfume_ecommerce_quote

if __name__ == "__main__":
    build_quotes.build()
