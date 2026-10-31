"""
Bhama Vision - build the astrologer website + backend quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `astrologer_quote.py`, so the branded look stays 100%
consistent with the other quotations.

    python3 build_astrologer_quote.py

Output is written to `output/`.
"""
import build_quotes
import astrologer_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = astrologer_quote

if __name__ == "__main__":
    build_quotes.build()
