"""
Quotation content for a dynamic sports results & stats portal (live result
cards, tables, weekly charts) with a full admin panel, in Hindi + English.
"""

# ---------------------------------------------------------------------------
# Company and client details.
# ---------------------------------------------------------------------------
COMPANY = {
    "name": "Bhama Vision",
    "tagline": "Websites, apps & AI for growing businesses",
    "email": "info@bhamavision.com",
    "phone": "+91 88606 40250",
    "website": "www.bhamavision.com",
    "location": "India",
}

CLIENT = {
    "name": "Prospective Client",
    "company": "Confidential",
    "note": "Sports results & stats portal with admin panel",
}

# Payment details + UPI QR (rendered on the quotation).
PAYMENT = {
    "account_name": "Prafull Kumar Sharma",
    "upi": "8860640250@idfcfirst",
    "bank": "IDFC First Bank",
    "qr_image": "payment qr.jpeg",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Dynamic, mobile-responsive sports results portal",
        "Live-result cards, tables & weekly charts",
        "Team / player stats & head-to-head pages",
        "Bilingual content support (Hindi + English)",
        "Full admin panel to manage all data & content",
        "Editable SEO title / description per page",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Written content, logos, images & other media assets",
        "Live data feeds / paid third-party sports data APIs",
        "Any betting, wagering, real-money gaming or odds features",
        "Ongoing maintenance, SEO, advertising or content entry",
        "Features or integrations outside the scope listed here",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-015",
        "package": "Website + Admin",
        "title": "Sports Results & Stats Portal",
        "subtitle": "Live result cards, tables & weekly charts with a full admin panel (Hindi + English)",
        "price": 10000,
        "price_note": "one-time (design & development)",
        "timeline": "15-20 working days",
        "summary": (
            "A fast, dynamic and mobile-responsive sports results & stats "
            "portal, with a clean data-focused homepage and a complete admin "
            "panel so you can run everything yourself. Publish live result "
            "cards, results tables, team/player stats and weekly charts, in "
            "both Hindi and English - no coding needed. This is an "
            "information & statistics portal only; it does not include any "
            "betting, wagering or real-money gaming features."
        ),
        "sections": [
            {
                "heading": "Frontend - homepage & layout",
                "items": [
                    "Structured homepage: header, navigation & logo / branding",
                    "Live-result cards with latest published results",
                    "Results / standings tables by league or category",
                    "Clean, data-focused, mobile-responsive layout",
                    "Footer with links, announcements & social / Telegram links",
                    "Full Hindi + English content support",
                ],
            },
            {
                "heading": "Frontend - results & stats pages",
                "items": [
                    "Team & player stats pages (head-to-head / detail view)",
                    "Weekly charts and standings history",
                    "Secondary league / tournament section",
                    "Search & filter results by league, team or date",
                    "SEO-friendly page structure",
                ],
            },
            {
                "heading": "Admin panel",
                "items": [
                    "Secure admin login",
                    "Add, edit and delete leagues / categories",
                    "Enter today's results and update fixtures",
                    "Set match / event start & end times (schedule)",
                    "Mark a match / event as postponed or cancelled",
                    "Edit team & player stats / detail data",
                    "Manage weekly charts and standings",
                    "Manage editorial preview / analysis content",
                    "Manage announcements and Telegram / social links",
                    "Manage SEO title & description per page",
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
        "This is an information & statistics portal only - no betting, wagering, odds or real-money gaming features are included.",
        "Domain and hosting are arranged and paid for by the client directly; we will help set them up.",
        "Content, results, images and stats are added by the client via the admin panel.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
