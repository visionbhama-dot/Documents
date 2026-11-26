"""
Bhama Vision - build the Evident Globe Next.js (Pro) website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `evident_globe_nextjs_quote.py`, so the branded look
stays 100% consistent with the other quotations.

    python3 build_evident_globe_nextjs_quote.py

Output is written to `output/`.
"""
import build_quotes
import evident_globe_nextjs_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = evident_globe_nextjs_quote

if __name__ == "__main__":
    build_quotes.build()
