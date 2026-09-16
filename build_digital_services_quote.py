"""
Bhama Vision - build the animated digital-services website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `digital_services_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_digital_services_quote.py

Output is written to `output/`.
"""
import build_quotes
import digital_services_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = digital_services_quote

if __name__ == "__main__":
    build_quotes.build()
