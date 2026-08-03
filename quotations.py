"""
Bhama Vision - quotation content.

Edit this file to change prices, features, clients or terms, then run:
    python3 build_quotes.py
"""

# ---------------------------------------------------------------------------
# Company details (shown on the cover + footers). Update with your real info.
# ---------------------------------------------------------------------------
COMPANY = {
    "name": "Bhama Vision",
    "tagline": "Websites, apps & AI for growing businesses",
    "email": "info@bhamavision.com",
    "phone": "+91 88606 40250",
    "website": "www.bhamavision.com",
    "location": "India",
}

# Client the quotation is prepared for. Update per customer.
CLIENT = {
    "name": "Prospective Client",
    "company": "Travel Business",
    "note": "Travel & tourism website",
}

# Shared support policy for packages that include support.
SUPPORT_ONE_YEAR = {
    "title": "1 Year Support - included",
    "covered": [
        "Fixing bugs and errors in the delivered features",
        "Repairing anything that stops working - forms, buttons, "
        "links, and admin actions (non-functional issues)",
        "Deployment / hosting issues for the delivered website",
        "Best-effort response within 1-2 business days",
    ],
    "not_covered": [
        "New features, new pages or new modules",
        "Content changes - adding or editing text, images, tour "
        "packages or blogs",
        "Design changes or redesigns",
        "Third-party costs: hosting, domain, paid APIs or plugins",
    ],
}

# ---------------------------------------------------------------------------
# The two quotations.
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-001",
        "package": "Frontend Package",
        "title": "Travel Website",
        "subtitle": "Design-only frontend website (no admin backend)",
        "price": 2999,
        "price_note": "one-time",
        "timeline": "5-7 working days",
        "summary": (
            "A fast, modern, mobile-friendly travel website that showcases "
            "your destinations and tours. Content is fixed at build time - "
            "there is no admin panel, so updates are handled by us or in a "
            "future upgrade to the backend package."
        ),
        "sections": [
            {
                "heading": "What's included",
                "items": [
                    "Responsive multi-page website (mobile, tablet & desktop)",
                    "Pages: Home, Destinations, Tours, About, Contact",
                    "Modern UI designed to match your brand",
                    "Image gallery for destinations and tours",
                    "Enquiry form that sends submissions to your email",
                    "Click-to-call and WhatsApp enquiry buttons",
                    "Basic on-page SEO (titles, meta tags, image alt text)",
                    "Deployment to your domain / hosting",
                ],
            },
            {
                "heading": "Not included in this package",
                "muted": True,
                "items": [
                    "Admin panel / content management",
                    "Dynamic blogs, tour packages or place categories",
                    "Image uploads and self-service editing",
                    "(All of the above are covered by the Full Website "
                    "package below.)",
                ],
            },
        ],
        "support": SUPPORT_ONE_YEAR,
    },
    {
        "id": "BV-Q-2026-002",
        "package": "Full Website + Admin",
        "title": "Travel Website",
        "subtitle": "Frontend + backend with admin panel and 1 year support",
        "price": 4999,
        "price_note": "one-time",
        "timeline": "12-15 working days",
        "summary": (
            "A complete, self-manageable travel website. You get everything "
            "in the frontend package plus a secure admin panel to manage "
            "blogs, tour packages and place categories (such as Manali, "
            "Shimla and more) with images - all without touching code."
        ),
        "sections": [
            {
                "heading": "Everything in the Frontend Package, plus",
                "items": [
                    "Secure admin panel with login",
                    "Blogs: create, edit and delete posts with images",
                    "Tour packages: pricing, itinerary, highlights & images",
                    "Place categories (Manali, Shimla, etc.) - each with "
                    "images and description, with tours & blogs grouped under them",
                    "Image upload and media management",
                    "Dynamic listing pages driven by your database",
                    "Enquiries saved in the admin panel + email notification",
                    "SEO-friendly dynamic pages",
                ],
            },
        ],
        "support": SUPPORT_ONE_YEAR,
    },
]

# Terms shown on the closing page of every quotation.
TERMS = {
    "validity_days": 15,
    "payment": "50% advance to start, 50% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time unless stated.",
        "Hosting, domain and any paid third-party services are billed at actuals.",
        "Timelines begin once content, access and the advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
