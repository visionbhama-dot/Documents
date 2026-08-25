"""
Bhama Vision - starter website quotation content.

A budget 4-5 page responsive website with WhatsApp integration and free
hosting, with 1 year of bug & error support. The domain is arranged by
the client (not on our side). Reuses the Bhama Vision quotation renderer:

    python3 build_starter_website_quote.py

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
    "note": "Starter website (4-5 pages)",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive website design (4-5 pages)",
        "WhatsApp integration (click-to-chat button)",
        "Contact / enquiry form",
        "Mobile, tablet & desktop responsive",
        "Hosting - free plan",
        "1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Website content & images (provided by the client)",
        "SEO / marketing (separate service)",
        "Payment gateway / online-store features",
        "Extra pages beyond 5",
        "Any paid plugin, tool or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-006",
        "package": "Starter Website",
        "title": "Website Design",
        "subtitle": "4-5 page responsive website with WhatsApp integration",
        "price": 1999,
        "price_note": "one-time (design & development)",
        "timeline": "5-8 working days",
        "summary": (
            "An affordable, ready-to-launch website for businesses that want a "
            "clean online presence. We design and develop a responsive 4-5 "
            "page website with a WhatsApp chat button so visitors can reach "
            "you in one tap. It comes with a free hosting plan and 1 year of "
            "bug & error support. The domain is arranged by you (it is not on "
            "our side), and we will help connect it to the website."
        ),
        "sections": [
            {
                "heading": "What we will design & develop",
                "items": [
                    "A responsive website of 4-5 pages (e.g. home, about, "
                    "services, gallery, contact)",
                    "WhatsApp integration - a click-to-chat button so visitors "
                    "message you directly",
                    "Contact / enquiry form",
                    "Clean, mobile-friendly design across mobile, tablet & "
                    "desktop",
                    "Free hosting plan setup and go-live",
                    "Connecting your domain to the website (domain arranged by "
                    "you)",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

# Terms shown on the closing page of the quotation.
TERMS = {
    "validity_days": 15,
    "payment": "40% advance to start, 60% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "This package covers up to 5 pages; additional pages are charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
