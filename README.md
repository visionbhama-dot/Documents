# Bhama Vision — Quotations

Branded, print-ready **A4 PDF quotations** for Bhama Vision, generated from Python.
Dark cover + clean white content pages, yellow brand accent, and a replaceable logo.

## What's inside

| File | Purpose |
| --- | --- |
| `quotations.py` | Quotation content — company info, client, prices, features, terms. **Edit this.** |
| `build_quotes.py` | Renderer that turns quotation data into A4 PDFs. |
| `invoices.py` | Invoice content — client, line items, payment details, notes. **Edit this.** |
| `build_invoices.py` | Renderer that turns invoice data into A4 PDFs. |
| `resume.py` | Resume content — profile, experience, projects, skills. **Edit this.** |
| `build_resume.py` | Renderer that turns resume data into an A4 PDF. |
| `assets/make_logo.py` | Generates a placeholder BhamaVision logo. |
| `assets/logo.png` | The logo used on every document — **replace with your real logo**. |
| `output/` | Generated PDFs. |

## Quick start

```bash
pip install -r requirements.txt
python3 build_quotes.py     # quotations
python3 build_invoices.py   # invoices
python3 build_resume.py     # resume
```

PDFs are written to `output/`.

## Invoices

Invoices reuse the same Bhama Vision branding. Edit `invoices.py` (client,
line items, payment details, notes) and run `python3 build_invoices.py`.

Current invoice:

| # | Client | Line items | Total |
| --- | --- | --- | --- |
| BV-INV-20260806-1800 | Bharat iON Systems | Website Design (₹7,500) + Catalog/Portfolio/Quotation etc. (₹3,500) | ₹11,000 |

> Give each new invoice a unique `id` in `invoices.py` (e.g. a date-based
> number). Set `tax_percent` there to add a GST line.

## Resume

A clean, two-column A4 resume for Prafull Kumar Sharma. Edit `resume.py`
(profile, experience, projects, skills, education, personal) and run
`python3 build_resume.py`. Output: `output/Prafull-Kumar-Sharma-Resume.pdf`.

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
