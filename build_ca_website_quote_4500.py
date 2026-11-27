"""
Bhama Vision - build the ABHISEKH CHATURVEDI & CO. CA website quotation
PDF at the Rs 4,500 price point (same scope as BV-Q-2026-067).

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `ca_website_quote_4500.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_ca_website_quote_4500.py

Output is written to `output/`.
"""
import build_quotes
import ca_website_quote_4500

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = ca_website_quote_4500

if __name__ == "__main__":
    build_quotes.build()
