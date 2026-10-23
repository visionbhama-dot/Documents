"""
Bhama Vision - build the Fatima Tour & Travel (4k) quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `fatima_tour_travel_quote.py`, so the branded look
stays 100% consistent with the other quotations.

    python3 build_fatima_tour_travel_quote.py

Output is written to `output/`.
"""
import build_quotes
import fatima_tour_travel_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = fatima_tour_travel_quote

if __name__ == "__main__":
    build_quotes.build()
