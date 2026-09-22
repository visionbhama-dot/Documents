"""
Bhama Vision - build the Yeh Hai News India website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `yehhainewsindia_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_yehhainewsindia_quote.py

Output is written to `output/`.
"""
import build_quotes
import yehhainewsindia_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = yehhainewsindia_quote

if __name__ == "__main__":
    build_quotes.build()
