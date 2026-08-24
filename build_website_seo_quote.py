"""
Bhama Vision - build the website design + SEO quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `website_seo_quote.py`, so the branded look stays 100%
consistent with the other quotations.

    python3 build_website_seo_quote.py

Output is written to `output/`.
"""
import build_quotes
import website_seo_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = website_seo_quote

if __name__ == "__main__":
    build_quotes.build()
