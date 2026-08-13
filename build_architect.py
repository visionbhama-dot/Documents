"""
Build the Architect portfolio website quotation PDFs using the shared renderer.

    python3 build_architect.py
"""
import build_quotes
import quotations_architect

build_quotes.data = quotations_architect

if __name__ == "__main__":
    build_quotes.build()
