"""
Bhama Vision - build the NexGen Bridge website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `nexgen_bridge_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_nexgen_bridge_quote.py

Output is written to `output/`.
"""
import build_quotes
import nexgen_bridge_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = nexgen_bridge_quote

if __name__ == "__main__":
    build_quotes.build()
