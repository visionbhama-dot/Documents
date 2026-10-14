"""
Bhama Vision - Pattron Tech website design quotation content.

A simple, website-only package: a clean responsive website design with
WhatsApp integration, free hosting and 1 year of bug & error support.
No backend / admin panel, no e-commerce, no SEO. The domain is arranged
by the client (not on our side). Reuses the Bhama Vision quotation
renderer:

    python3 build_pattron_tech_quote.py

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
    "name": "Pattron Tech",
    "company": "Pattron Tech",
    "note": "Website design only (no backend)",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive website design (up to 5 pages)",
        "Clean, modern layout designed for your brand",
        "WhatsApp integration (click-to-chat button)",
        "Contact / enquiry form",
        "Click-to-call and Google Maps location",
        "Mobile, tablet & desktop responsive",
        "Hosting - free plan",
        "1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Website content, logo & images (provided by the client)",
        "Backend / admin panel - this is a website-only package",
        "Online store, cart or payment gateway",
        "User login / registration",
        "SEO, ads or social media marketing (separate service)",
        "Extra pages beyond 5",
        "Any paid plugin, theme, tool or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-029",
        "package": "Website Design",
        "title": "Website Design",
        "subtitle": "Responsive website for Pattron Tech - design & development only",
        "price": 2800,
        "price_note": "one-time (design & development)",
        "timeline": "5-8 working days",
        "summary": (
            "A straightforward, website-only package for Pattron Tech. We "
            "design and develop a clean, responsive website of up to 5 pages "
            "that presents your company, services and contact details "
            "professionally. Visitors can reach you in one tap through a "
            "WhatsApp chat button, a click-to-call link or a simple enquiry "
            "form. This is a design-and-development package only - there is "
            "no backend or admin panel, no online store and no marketing "
            "included. It comes with a free hosting plan and 1 year of bug & "
            "error support. The domain is arranged by you (it is not on our "
            "side), and we will help connect it to the website."
        ),
        "sections": [
            {
                "heading": "What we will design & develop",
                "items": [
                    "A responsive website of up to 5 pages (e.g. home, about, "
                    "services, gallery, contact)",
                    "Modern, clean design using your logo, colours and content",
                    "WhatsApp integration - a click-to-chat button so visitors "
                    "message you directly",
                    "Contact / enquiry form that delivers to your email",
                    "Click-to-call button and Google Maps location",
                    "Fully responsive across mobile, tablet & desktop",
                    "Basic on-page setup - page titles, favicon and fast-loading "
                    "images",
                    "Free hosting plan setup and go-live",
                    "Connecting your domain to the website (domain arranged by "
                    "you)",
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
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "This is a website-only package - no backend / admin panel, online store or marketing is included.",
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Website content, logo and images are provided by the client.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "This package covers up to 5 pages; additional pages are charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
