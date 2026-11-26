"""
Bhama Vision - Evident Globe digital agency website quotation content.

A clean, responsive website for Evident Globe (a digital agency) with an
admin panel to manage blogs, SEO-friendly options, free hosting for 1 year
and 1 year of bug & error support. The domain is arranged by the client
(not included).

Reuses the Bhama Vision quotation renderer:

    python3 build_evident_globe_quote.py

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
    "company": "Evident Globe",
    "note": "Digital agency website + admin panel to manage blogs (free hosting 1 year, domain not included)",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Clean, responsive digital agency website",
        "Free hosting for 1 year (from our side)",
        "Admin panel to manage blogs (write, edit & publish)",
        "SEO-friendly build with per-post SEO options",
        "Services & portfolio sections",
        "Enquiry form + WhatsApp click-to-chat & call buttons",
        "1 year support for any bugs & errors",
    ],
    "not_covered": [
        "Domain - client's (approx \u20b91,000-\u20b91,500 / year)",
        "Hosting renewal from year 2 (approx \u20b91,500 / year)",
        "Content, images & copywriting (provided by the client)",
        "Logo / brand identity design (separate service)",
        "Ongoing SEO / marketing campaigns (separate service)",
        "Mobile app (Android / iOS) - separate scope",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-064",
        "package": "Website + Admin",
        "title": "Evident Globe",
        "subtitle": "Digital agency website with a blog admin panel, SEO-friendly options, free hosting for 1 year & 1 year support (domain not included)",
        "price": 3500,
        "price_note": "one-time (incl. free hosting for 1 year)",
        "timeline": "7-10 working days",
        "summary": (
            "A clean, modern and responsive website for Evident Globe to "
            "present the agency, its services and work, and to publish "
            "content that brings in organic traffic. Visitors explore your "
            "services and portfolio and get in touch through an enquiry form "
            "that reaches your email and WhatsApp, a WhatsApp chat button and "
            "a click-to-call button. An easy-to-use admin panel lets you "
            "write, edit and publish blog posts yourself - each with "
            "SEO-friendly options - so you can keep the site fresh without "
            "touching code. The whole site is built SEO-friendly, comes with "
            "free hosting for the first year and 1 year of support for any "
            "bugs & errors. The domain is arranged by you (not included), and "
            "we help connect it."
        ),
        "sections": [
            {
                "heading": "Website pages (frontend)",
                "items": [
                    "Home - hero banner, agency snapshot, services & clear "
                    "call-to-action",
                    "About - your story, team and why clients choose you",
                    "Services - your digital services presented with "
                    "descriptions",
                    "Portfolio / work - projects & case studies showcase",
                    "Blog - articles listing with categories, search & "
                    "featured posts",
                    "Contact - enquiry form, WhatsApp & call buttons, address "
                    "and Google Map",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Blog admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard",
                    "Write, edit, publish & delete blog posts with images",
                    "Organise posts into categories & tags",
                    "Per-post SEO options - title, meta description, slug / "
                    "clean URL & image alt text",
                    "Manage featured posts and homepage highlights",
                    "View enquiry leads received through the site",
                ],
            },
            {
                "heading": "SEO, hosting, support & delivery",
                "items": [
                    "SEO-friendly build - titles, meta descriptions, "
                    "headings, clean URLs and image alt text",
                    "XML sitemap, robots.txt & Google Analytics / Search "
                    "Console setup",
                    "Fast-loading, mobile-first build tested across browsers "
                    "& devices",
                    "Free hosting for 1 year from our side with SSL + help "
                    "connecting your domain",
                    "1 year of support for any bugs & errors after launch",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

# Payment details (renders a UPI QR on the quotation).
PAYMENT = {
    "account_name": "Prafull Kumar Sharma",
    "upi": "8860640250@idfcfirst",
    "bank": "IDFC First Bank",
    "qr_image": "payment qr.jpeg",
}

# Terms shown on the closing page of the quotation.
TERMS = {
    "validity_days": 15,
    "payment": "50% advance to start, 50% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
        "Hosting for the first year is free from our side (with SSL).",
        "The domain is NOT included - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Next-year renewal (from year 2 onwards), paid by the client at actuals: domain approx \u20b91,000-\u20b91,500 / year and hosting approx \u20b91,500 / year.",
        "The website is built SEO-friendly; on-page SEO and Search Console setup help the pages become eligible to rank. Rankings depend on Google and competition and cannot be guaranteed; ongoing SEO / marketing is a separate service.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages / features or redesigns.",
        "Text, photos, blog content and images are provided by the client and managed via the admin panel.",
        "Timelines begin once the content, logo and advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
