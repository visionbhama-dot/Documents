"""
Bhama Vision - build the real estate project website + monthly ads quote PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `real_estate_ads_quote.py`.

    python3 build_real_estate_ads_quote.py

Output is written to `output/`.
"""
import os

import build_quotes
import real_estate_ads_quote

build_quotes.data = real_estate_ads_quote

# Use whichever Noto Sans font directory exists in this environment.
for _fd in (
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "fonts"),
    build_quotes.FONT_DIR,
    "/inner_container/usr/share/fonts/google-noto",
    "/usr/share/fonts/google-noto",
):
    if os.path.isfile(os.path.join(_fd, "NotoSans-Regular.ttf")):
        build_quotes.FONT_DIR = _fd
        break

if __name__ == "__main__":
    build_quotes.build()
