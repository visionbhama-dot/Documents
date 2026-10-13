# Quotation writing conventions

Conventions for the quotation content modules (`*_quote.py`) and the
`build_quotes.py` renderer.

## Don't advertise what the client isn't buying

Never write that online payment (or any other omitted feature) is absent.
Phrases like "no online payment", "NO online payment", or a "Not included"
line such as "Online payment / cart / checkout" must not appear.

Describe what the customer actually asked for instead. For an
enquiry-based site, frame it positively: buyers send a quote request or
order over WhatsApp and email, and those leads reach the client directly.

The "Not included" column is for things the client must arrange or may
want to buy later (domain, product photos, extra products, SEO) — not for
features they chose not to have.

## Quotation IDs

IDs run in sequence as `BV-Q-2026-0NN`. Before adding a quotation, check
the highest existing ID and take the next one:

```sh
grep -rho "BV-Q-2026-0[0-9][0-9]" --include=*.py . | sort -u | tail -1
```

## Standard package shape

Unless the client asks otherwise, quotations include a free hosting plan
and 1 year of bug & error support, and state that the domain is arranged
and paid for by the client (not on our side) with help connecting it.

Product-count limits ("up to N products") are repeated in the included
list, the feature bullets and the terms notes so the scope is unambiguous.

## Building

Each quotation has a content module plus a thin `build_*.py` that swaps
`build_quotes.data` and calls `build_quotes.build()`. Rebuild the PDF and
commit it with the content change. `reportlab` and `pillow` are required
(see `requirements.txt`).
