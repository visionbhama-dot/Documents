"""
Bhama Vision - build the website + admin panel quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `website_admin_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_website_admin_quote.py

Output is written to `output/`.
"""
import build_quotes
import website_admin_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = website_admin_quote

if __name__ == "__main__":
    build_quotes.build()
