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

# Client the quotation is prepared for.
# Customer / agency name is intentionally left out of the document.
CLIENT = {
    "name": "Prospective Client",
    "company": "Confidential",
    "note": "Creator clipping & campaigns platform",
}

# Requirements box shown on each quotation. Two columns:
#   left  (highlighted) = what Bhama Vision builds & delivers
#   right (muted)       = third-party subscriptions arranged by the client
REQUIREMENTS = {
    "title": "Scope & requirements",
    "left_label": "Delivered by Bhama Vision",
    "right_label": "On client's side (third-party)",
    "covered": [
        "Complete UI/UX design & development",
        "Setup of database and all data models",
        "Integration of the third-party services listed alongside",
        "Deployment to the client's hosting + handover",
        "Testing and bug fixing before launch",
    ],
    "not_covered": [
        "Domain and web hosting / server",
        "Payment gateway account and its transaction fees",
        "Email / OTP sending service subscription",
        "Social media API access & keys (for view tracking)",
        "SMS / KYC service, and any other paid API or plugin",
    ],
}

# ---------------------------------------------------------------------------
# The two quotations.
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-001",
        "package": "Complete Platform",
        "title": "Creator Clipping Platform",
        "subtitle": "Website + Creator dashboard + Brand dashboard + Admin panel",
        "price": 30000,
        "price_note": "one-time (design & development)",
        "timeline": "30-40 working days",
        "summary": (
            "A complete clipping & campaigns platform. Brands post campaigns "
            "and pay creators per 1,000 views; creators clip content, post it "
            "on social media, submit the link and earn. Includes the public "
            "website, separate dashboards for creators and brands, and an "
            "admin panel to control everything."
        ),
        "sections": [
            {
                "heading": "What we will design & develop",
                "items": [
                    "Public website: landing page, discover campaigns, FAQ, contact",
                    "Sign up & login with email + password + OTP verification",
                    "Creator dashboard: browse & join campaigns, submit post "
                    "links, wallet, earnings, payout methods, profile",
                    "Brand dashboard: create & manage campaigns, buy points, "
                    "set pay-rate per 1,000 views, review submissions "
                    "(approve / reject / flag), analytics",
                    "Admin panel: manage users, campaigns, flagged "
                    "submissions, points & payouts, and reports",
                    "Payment integration - brands buy points, creators get payouts",
                    "View tracking for submitted clips",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
    {
        "id": "BV-Q-2026-002",
        "package": "Website + Admin",
        "title": "Creator Clipping Platform",
        "subtitle": "Website frontend + one admin panel (no creator/brand dashboards)",
        "price": 20000,
        "price_note": "one-time (design & development)",
        "timeline": "18-25 working days",
        "summary": (
            "The public website plus a single admin panel that controls "
            "everything - campaigns, users, submissions and payments - from "
            "one place. There are no separate dashboards for creators or "
            "brands in this package."
        ),
        "sections": [
            {
                "heading": "What we will design & develop",
                "items": [
                    "Public website: landing page, discover campaigns, FAQ, contact",
                    "Sign up & login with email + password + OTP verification",
                    "One admin panel to control everything: campaigns, users, "
                    "submissions (approve / reject / flag), points & payouts, "
                    "and site content",
                    "Payment and view-tracking integration as required",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Not included in this package",
                "muted": True,
                "items": [
                    "Separate creator dashboard",
                    "Separate brand dashboard",
                    "(Both are covered by the Complete Platform package.)",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

# Terms shown on the closing page of every quotation.
TERMS = {
    "validity_days": 15,
    "payment": "40% advance to start, 30% at midway, 30% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
        "All third-party subscriptions (hosting, domain, payment gateway, email/OTP, social media APIs, SMS/KYC) are arranged and paid for by the client directly.",
        "Timelines begin once content, access and the advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
