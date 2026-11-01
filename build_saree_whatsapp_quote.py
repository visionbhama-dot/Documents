"""
Bhama Vision - build the saree marketplace (WhatsApp ordering) quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `saree_whatsapp_quote.py`, so the branded look stays
100% consistent with the other quotations.

    python3 build_saree_whatsapp_quote.py

Output is written to `output/`.
"""
import build_quotes
import saree_whatsapp_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = saree_whatsapp_quote

if __name__ == "__main__":
    build_quotes.build()
