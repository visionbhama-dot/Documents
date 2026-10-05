"""
Bhama Vision - Go Realtors website quotation content.

A responsive real-estate website with a backend admin panel so the Go
Realtors team can add, edit and remove property listings on their own.
Includes property listings with photos & details, enquiry form, WhatsApp
integration, free hosting and 1 year of bug & error support. The domain is
arranged by the client (not on our side). Reuses the Bhama Vision
quotation renderer:

    python3 build_go_realtors_quote.py

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
    "name": "Go Realtors",
    "company": "Go Realtors",
    "note": "Real-estate website with backend admin panel",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive real-estate website (multiple pages)",
        "Backend admin panel to add, edit & remove property listings",
        "Property listings with photos, price, location & details",
        "Search / filter by type, location & budget",
        "Enquiry form (reaches you on WhatsApp / email)",
        "WhatsApp integration (click-to-chat button)",
        "Hosting - free plan",
        "1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Property content, photos & details (provided by the client)",
        "Online payment / booking or EMI calculator integrations",
        "Agent / customer mobile app",
        "SEO / marketing (separate service)",
        "Any paid plugin, tool or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-023",
        "package": "Real-Estate Website",
        "title": "Go Realtors Website",
        "subtitle": "Property website with a backend admin panel",
        "price": 9000,
        "price_note": "one-time (design & development)",
        "timeline": "12-18 working days",
        "summary": (
            "A professional, ready-to-launch website for Go Realtors with a "
            "backend admin panel so your team can manage property listings on "
            "your own - no coding needed. Visitors can browse properties with "
            "photos, price and location, search and filter to find the right "
            "match, and send an enquiry that reaches you directly on WhatsApp. "
            "It comes with a WhatsApp chat button, a free hosting plan and 1 "
            "year of bug & error support. The domain is arranged by you (it is "
            "not on our side), and we will help connect it to the website."
        ),
        "sections": [
            {
                "heading": "What we will design & develop",
                "items": [
                    "A responsive website with pages such as home, about, "
                    "property listings, property detail, enquiry and contact",
                    "Property listings with photos, price, location, type "
                    "(buy / rent) and key details",
                    "Search & filter by property type, location and budget",
                    "Property detail pages with photo gallery and an enquiry "
                    "button",
                    "Enquiry form (name, phone, property of interest) "
                    "delivered to your WhatsApp / email",
                    "WhatsApp integration - click-to-chat button so buyers "
                    "reach you in one tap",
                    "Clean, mobile-friendly design across mobile, tablet & "
                    "desktop",
                    "Free hosting plan setup and go-live; connecting your "
                    "domain (arranged by you)",
                ],
            },
            {
                "heading": "Backend admin panel",
                "items": [
                    "Secure admin login for the Go Realtors team",
                    "Add, edit and remove property listings yourself - no "
                    "coding needed",
                    "Upload property photos and set price, location, type and "
                    "status (available / sold / rented)",
                    "Mark listings as featured to show them on the homepage",
                    "View and manage enquiries received from the website",
                    "A short walkthrough so your team is comfortable using the "
                    "panel",
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
    "payment": "40% advance to start, 60% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "The backend admin panel lets you manage property listings and enquiries; online payment / booking and EMI calculators are not included and can be quoted separately.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
