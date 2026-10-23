"""
Bhama Vision - build the Chatrabhuj Traders grocery (9k) quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `chatrabhuj_grocery_quote.py`, so the branded look
stays 100% consistent with the other quotations.

    python3 build_chatrabhuj_grocery_quote.py

Output is written to `output/`.
"""
import build_quotes
import chatrabhuj_grocery_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = chatrabhuj_grocery_quote

if __name__ == "__main__":
    build_quotes.build()
