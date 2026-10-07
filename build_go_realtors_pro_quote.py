"""
Bhama Vision - build the Go Realtors Pro (15k) website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `go_realtors_pro_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_go_realtors_pro_quote.py

Output is written to `output/`.
"""
import build_quotes
import go_realtors_pro_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = go_realtors_pro_quote

if __name__ == "__main__":
    build_quotes.build()
