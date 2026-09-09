"""
Bhama Vision - build the cafe / fast-food dynamic website + custom CMS
quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `cafe_cms_quote.py`, so the branded look stays
consistent with the other quotations.

    python3 build_cafe_cms_quote.py

Output is written to `output/`.
"""
import build_quotes
import cafe_cms_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = cafe_cms_quote

if __name__ == "__main__":
    build_quotes.build()
