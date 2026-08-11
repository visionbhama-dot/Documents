"""
Build the WantX quotation PDF(s) using the shared Bhama Vision renderer.

This reuses `build_quotes.py` unchanged - it just points the renderer's
data source at `quotations_wantx` instead of the default `quotations`.

    python3 build_wantx.py

Output PDFs are written to `output/`.
"""
import build_quotes
import quotations_wantx

# Point the shared renderer at the WantX content module.
build_quotes.data = quotations_wantx

if __name__ == "__main__":
    build_quotes.build()
