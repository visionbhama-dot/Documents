"""
Bhama Vision - build the taxi & bike rental website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `rental_website_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_rental_website_quote.py

Output is written to `output/`.
"""
import build_quotes
import rental_website_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = rental_website_quote

if __name__ == "__main__":
    build_quotes.build()
