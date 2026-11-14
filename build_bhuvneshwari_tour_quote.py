"""
Bhama Vision - build the Bhuvneshwari Tour travel website quotation PDF.

Reuses the existing quotation renderer in `build_quotes.py` but drives it
with the content in `bhuvneshwari_tour_quote.py`.

    python3 build_bhuvneshwari_tour_quote.py

Output is written to `output/`.
"""
import os

import build_quotes
import bhuvneshwari_tour_quote

build_quotes.data = bhuvneshwari_tour_quote

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
