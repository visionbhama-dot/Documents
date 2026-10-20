"""
Build the additional quotations (college portal, e-commerce, Connectify).

    python3 build_more.py
"""
import build_quotes
import quotations_more

build_quotes.data = quotations_more

if __name__ == "__main__":
    build_quotes.build()
