"""
Bhama Vision - SXR (SmartXReview) Dynamic QR Code Management System quote.

A fully functional, private Dynamic QR Code Management System built
exclusively for the client - secure admin dashboard, dynamic QR codes
with permanent redirect links whose destination can be changed anytime
without reprinting, scan analytics and more. Free-tier hosting is provided
initially (the client buys paid hosting only if usage grows beyond the
free tier); the domain is arranged by the client. Comes with 1 year of
bug & error support. Reuses the Bhama Vision quotation renderer:

    python3 build_sxr_qr_system_quote.py

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
    "name": "SXR - SmartXReview",
    "company": "SXR - SmartXReview",
    "note": "Private Dynamic QR Code Management System",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Private Dynamic QR Code Management System, built exclusively "
        "for you",
        "Secure admin login & private dashboard",
        "500+ dynamic QR codes per month - no fixed generation limit",
        "Permanent redirect links; change destination URLs anytime "
        "without reprinting",
        "High-quality PNG & SVG downloads, preview & one-click copy",
        "Scan analytics - per-QR & total counts, date-wise statistics",
        "Recycle Bin, URL history, database backup & export",
        "Custom SXR branding; mobile-friendly dashboard",
        "Free-tier hosting & database set up initially",
        "1 year bug & error support; full ownership handed to you",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Paid hosting / database - only if usage grows beyond the free "
        "tier (your approval first)",
        "No monthly software subscription & no per-QR generation charges",
        "Bulk-printing of the QR codes on physical materials",
        "SMS / email / OTP sending service subscription",
        "New features or redesigns beyond the scope above",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-068",
        "package": "Dynamic QR Code System",
        "title": "SXR - SmartXReview",
        "subtitle": "Private Dynamic QR Code Management System - one-time build, full ownership",
        "price": 9000,
        "price_note": "one-time (design & development)",
        "timeline": "8-10 working days",
        "summary": (
            "A fully functional, private Dynamic QR Code Management System "
            "developed exclusively for SXR - SmartXReview. You get a secure "
            "admin dashboard from which you can generate 500+ dynamic QR "
            "codes every month with no fixed generation limit. Each QR code "
            "has a unique, permanent redirect link, so you can change its "
            "destination URL anytime without ever reprinting the code. "
            "Download codes in high-quality PNG and SVG, preview them, copy "
            "links in one click, and search, edit, activate, deactivate or "
            "delete codes as you go - with individual and total scan counts "
            "and date-wise statistics to see how they perform. The system is "
            "designed around simplicity, security and ease of use, and is "
            "handed over with full ownership and control. There is no "
            "monthly software subscription and no per-QR charge. We set it "
            "up on free-tier hosting and database to start; if your usage "
            "grows beyond the free tier, paid hosting is optional and only "
            "activated with your approval. The domain is arranged by you, "
            "and it comes with 1 year of bug & error support."
        ),
        "sections": [
            {
                "heading": "Core QR management",
                "items": [
                    "Secure admin login and a private dashboard",
                    "Generate 500+ dynamic QR codes per month with no fixed "
                    "generation limit",
                    "Unique, permanent redirect link for every QR code",
                    "Change the destination URL anytime - the printed QR "
                    "never needs to change or be reprinted",
                    "Download QR codes in high-quality PNG and SVG formats",
                    "QR preview and one-click link copying",
                    "Search, edit, activate, deactivate and delete QR codes",
                    "Mobile-friendly dashboard for Android devices",
                ],
            },
            {
                "heading": "Scan analytics",
                "items": [
                    "Individual scan count for each QR code",
                    "Total scan count across all codes",
                    "Date-wise scan statistics to track performance over time",
                ],
            },
            {
                "heading": "Included at no extra cost",
                "items": [
                    "Recycle Bin - restore accidentally deleted QR codes",
                    "URL history - view and restore previous destination URLs",
                    "Database backup & export",
                    "Custom SXR branding across the dashboard",
                    "Secure database and admin access",
                ],
            },
            {
                "heading": "Hosting, ownership & delivery",
                "items": [
                    "Set up on free-tier hosting and database to start - no "
                    "running software cost",
                    "No monthly software subscription and no per-QR "
                    "generation charges",
                    "If usage grows beyond the free tier, paid hosting is "
                    "optional and activated only with your approval",
                    "The domain is arranged by you; we help connect it",
                    "Full ownership and control of the system handed over to "
                    "you",
                    "Guided walkthrough & handover",
                    "1 year of support for bugs & errors after launch",
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
    "payment": "40% advance to start, 30% at midway, 30% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "There is no monthly software subscription and no per-QR generation charge.",
        "The system is set up on free-tier hosting and database initially; if usage grows beyond the free tier, paid hosting / database is optional, charged separately and activated only with your prior approval.",
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it.",
        "Full ownership and control of the system is handed over to the client on delivery.",
        "No paid third-party service will be activated without the client's approval.",
        "Timelines begin once the content, access and advance payment are received.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover new features, content changes or redesigns.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
