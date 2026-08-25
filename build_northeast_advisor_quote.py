"""
Bhama Vision - build the Northeast Advisor website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `northeast_advisor_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_northeast_advisor_quote.py

Output is written to `output/`.
"""
import build_quotes
import northeast_advisor_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = northeast_advisor_quote

if __name__ == "__main__":
    build_quotes.build()
