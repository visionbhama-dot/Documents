"""
Build the Resort / Cottage website quotation PDFs using the shared renderer.

    python3 build_resort.py
"""
import build_quotes
import quotations_resort

build_quotes.data = quotations_resort

if __name__ == "__main__":
    build_quotes.build()
