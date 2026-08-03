# Bhama Vision — Quotations

Branded, print-ready **A4 PDF quotations** for Bhama Vision, generated from Python.
Dark cover + clean white content pages, yellow brand accent, and a replaceable logo.

## What's inside

| File | Purpose |
| --- | --- |
| `quotations.py` | All content — company info, client, prices, features, terms. **Edit this.** |
| `build_quotes.py` | Renderer that turns the data into A4 PDFs. |
| `assets/make_logo.py` | Generates a placeholder BhamaVision logo. |
| `assets/logo.png` | The logo used on every document — **replace with your real logo**. |
| `output/` | Generated PDFs. |

## Quick start

```bash
pip install -r requirements.txt
python3 build_quotes.py
```

PDFs are written to `output/`.

## Current quotations (travel website)

| # | Package | Price | Support |
| --- | --- | --- | --- |
| BV-Q-2026-001 | Frontend Package (design-only, no backend) | ₹2,999 | — |
| BV-Q-2026-002 | Full Website + Admin (blogs, tour packages, place categories like Manali/Shimla with images) | ₹4,999 | 1 year |

**1 Year Support** covers bug fixes and anything that stops working (non-functional
issues). It does **not** cover content changes, new features or redesigns.

## Customising

- **Prices / features / client name** — edit `quotations.py`, then re-run `build_quotes.py`.
- **Logo** — drop your logo in as `assets/logo.png` (transparent PNG, roughly 8:1
  width:height works best), or run `python3 assets/make_logo.py` to regenerate the
  placeholder.
- **Add a new quotation** — append another entry to the `QUOTATIONS` list in
  `quotations.py`.

Fonts use Noto Sans (system font). If they aren't found, adjust `FONT_DIR` in
`build_quotes.py` / `assets/make_logo.py`.
