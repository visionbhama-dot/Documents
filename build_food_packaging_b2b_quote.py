"""
Bhama Vision - build the food-packaging B2B (9k) quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `food_packaging_b2b_quote.py`, so the branded look
stays 100% consistent with the other quotations.

    python3 build_food_packaging_b2b_quote.py

Output is written to `output/`.
"""
import build_quotes
import food_packaging_b2b_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = food_packaging_b2b_quote

if __name__ == "__main__":
    build_quotes.build()
