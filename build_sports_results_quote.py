"""
Bhama Vision - build the sports results & stats portal quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `sports_results_quote.py`, so the branded look stays
consistent with the other quotations.

    python3 build_sports_results_quote.py

Output is written to `output/`.
"""
import build_quotes
import sports_results_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = sports_results_quote

if __name__ == "__main__":
    build_quotes.build()
