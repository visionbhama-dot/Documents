"""
Bhama Vision - build the e-commerce website (30 products) quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `ecommerce_30products_quote.py`, so the branded look
stays 100% consistent with the other quotations.

    python3 build_ecommerce_30products_quote.py

Output is written to `output/`.
"""
import os

import build_quotes
import ecommerce_30products_quote

# Swap the content module the renderer reads from, then build as usual.
build_quotes.data = ecommerce_30products_quote

# Use whichever Noto Sans font directory exists in this environment, so the
# build is portable across machines that store the static weights elsewhere.
for _font_dir in (
    build_quotes.FONT_DIR,
    "/inner_container/usr/share/fonts/google-noto",
    "/usr/share/fonts/google-noto",
):
    if os.path.isfile(os.path.join(_font_dir, "NotoSans-Regular.ttf")):
        build_quotes.FONT_DIR = _font_dir
        break

if __name__ == "__main__":
    build_quotes.build()
