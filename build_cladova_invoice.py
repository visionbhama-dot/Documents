"""
Bhama Vision - build the Cladova invoice PDF only.

Reuses the existing invoice renderer in `build_invoices.py` but drives it
with the content in `cladova_invoice.py`, so only the Cladova invoice is
generated and the other invoices are left untouched.

    python3 build_cladova_invoice.py

Output is written to `output/`.
"""
import os

import build_quotes
import build_invoices
import cladova_invoice

# Swap the content module the renderer reads from, then build as usual.
build_invoices.data = cladova_invoice

# The invoice renderer registers fonts via build_quotes, so point its FONT_DIR
# at whichever Noto Sans directory exists in this environment.
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
    build_invoices.build()
