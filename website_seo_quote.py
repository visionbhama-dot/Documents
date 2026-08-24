"""
Bhama Vision - website design + SEO quotation content.

A website design package with on-page SEO, Google Search Console indexing
and a Google My Business profile, plus domain (1 year) and free hosting,
with 1 year of support. Reuses the Bhama Vision quotation renderer:

    python3 build_website_seo_quote.py

Edit price, features, client or terms below, then re-run.
"""

# ---------------------------------------------------------------------------
# Company details (shown on the header + footers).
# ---------------------------------------------------------------------------
COMPANY = {
    "name": "Bhama Vision",
    "tagline": "Websites, apps & AI for growing businesses",
    "email": "info@bhamavision.com",
    "phone": "+91 88606 40250",
    "website": "www.bhamavision.com",
    "location": "India",
}

# Client the quotation is prepared for.
CLIENT = {
    "name": "Prospective Client",
    "company": "Confidential",
    "note": "Website design with SEO",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Website design & development (responsive)",
        "On-page SEO setup",
        "Google Search Console setup & indexing",
        "Google My Business profile setup",
        "Domain for 1 year",
        "Hosting - free plan",
        "1 year support (bug fixes / things that stop working)",
    ],
    "not_covered": [
        "Domain renewal from the 2nd year onwards",
        "Paid hosting upgrade beyond the free plan",
        "Website content & images (provided by the client)",
        "Payment gateway / online-store features",
        "Ongoing monthly SEO or ad campaigns (separate service)",
        "Any paid plugin, tool or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-005",
        "package": "Website + SEO",
        "title": "Website Design + SEO",
        "subtitle": "Website with SEO, Search Console indexing & Google My Business",
        "price": 6000,
        "price_note": "one-time (incl. domain for 1 year; free hosting)",
        "timeline": "7-12 working days",
        "summary": (
            "A complete, ready-to-launch website with search visibility built "
            "in. We design and develop a clean, responsive website, set up "
            "on-page SEO, get it indexed on Google via Search Console, and "
            "create your Google My Business profile so you show up in local "
            "searches and on Maps. The package also includes a domain for the "
            "first year, a free hosting plan, and 1 year of support."
        ),
        "sections": [
            {
                "heading": "What we will design & develop",
                "items": [
                    "Professional, responsive website (mobile, tablet & desktop)",
                    "On-page SEO setup - titles, meta tags, headings, "
                    "sitemap & basic speed optimization",
                    "Google Search Console setup and indexing so your site "
                    "appears on Google",
                    "Google My Business profile setup for local search & Maps",
                    "Standard pages (home, about, services, contact) with an "
                    "enquiry / contact form",
                ],
            },
            {
                "heading": "Pricing breakdown",
                "items": [
                    "Website design + SEO + Search Console indexing + Google "
                    "My Business  -  \u20b95,000",
                    "Domain (1 year)  -  \u20b91,000",
                    "Hosting  -  Free plan (\u20b90)",
                    "Total  -  \u20b96,000 (one-time)",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

# Terms shown on the closing page of the quotation.
TERMS = {
    "validity_days": 15,
    "payment": "40% advance to start, 30% at midway, 30% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "1 year support covers bug fixes and anything that stops working (non-functional issues). It does not cover content changes, new features or redesigns.",
        "Domain is included for the first year; renewal from the 2nd year onwards is chargeable.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "SEO here is a one-time on-page setup + indexing; ongoing monthly SEO is a separate service.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
