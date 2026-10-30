"""
Bhama Vision - build the travel website + admin (lead capture + SEO) quote PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `travel_leads_seo_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_travel_leads_seo_quote.py

Output is written to `output/`.
"""
import build_quotes
import travel_leads_seo_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = travel_leads_seo_quote

if __name__ == "__main__":
    build_quotes.build()
