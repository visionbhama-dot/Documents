"""
Bhama Vision - Go Realtors website quotation content (Pro / 15k tier).

A premium, responsive real-estate website with a full backend admin panel so
the Go Realtors team can manage unlimited property listings, agents, leads
and enquiries on their own. Builds on the standard package with advanced
search, map view, agent profiles, a blog and a lead-management dashboard.
Includes free hosting and 1 year of bug & error support. The domain is
arranged by the client (not on our side). Reuses the Bhama Vision
quotation renderer:

    python3 build_go_realtors_pro_quote.py

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
    "note": "Premium real-estate website with backend admin & lead management",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Premium responsive real-estate website (extended pages)",
        "Full backend admin panel - unlimited property listings",
        "Advanced search & filters (type, location, budget, BHK, status)",
        "Interactive map view with property pins",
        "Agent profiles & assign listings to agents",
        "Lead-management dashboard (capture & track enquiries)",
        "Blog / news section (managed from the admin panel)",
        "WhatsApp integration + enquiry forms",
        "Hosting - free plan",
        "1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Property content, photos & details (provided by the client)",
        "Online payment / booking or EMI calculator integrations",
        "Agent / customer mobile app",
        "Paid third-party map or CRM subscriptions (if required)",
        "SEO / marketing campaigns (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-024",
        "package": "Real-Estate Website - Pro",
        "title": "Go Realtors Website - Pro",
        "subtitle": "Premium property website with full backend, map view & lead management",
        "price": 15000,
        "price_note": "one-time (design & development)",
        "timeline": "18-25 working days",
        "summary": (
            "A premium, feature-rich website for Go Realtors with a complete "
            "backend admin panel so your team can manage unlimited property "
            "listings, agents, leads and content on your own - no coding "
            "needed. Visitors get advanced search and filters, an interactive "
            "map view, detailed property pages and agent profiles, and can "
            "send enquiries that are captured in a lead-management dashboard "
            "and delivered to your WhatsApp. It comes with a blog / news "
            "section, a free hosting plan and 1 year of bug & error support. "
            "The domain is arranged by you (it is not on our side), and we "
            "will help connect it to the website."
        ),
        "sections": [
            {
                "heading": "What we will design & develop",
                "items": [
                    "A premium responsive website with pages such as home, "
                    "about, property listings, property detail, map view, "
                    "agents, blog, enquiry and contact",
                    "Property listings with photos, price, location, type "
                    "(buy / rent), BHK and key details",
                    "Advanced search & filters by property type, location, "
                    "budget, BHK and status",
                    "Interactive map view with property pins and locations",
                    "Property detail pages with photo gallery, amenities and "
                    "an enquiry button",
                    "Agent profiles - photo, contact and the listings assigned "
                    "to each agent",
                    "Blog / news section to publish updates and attract "
                    "visitors",
                    "WhatsApp integration + enquiry forms delivered to you and "
                    "captured as leads",
                    "Clean, mobile-friendly design across mobile, tablet & "
                    "desktop",
                    "Free hosting plan setup and go-live; connecting your "
                    "domain (arranged by you)",
                ],
            },
            {
                "heading": "Backend admin panel & lead management",
                "items": [
                    "Secure admin login with roles for the Go Realtors team",
                    "Add, edit and remove unlimited property listings - no "
                    "coding needed",
                    "Upload photo galleries and set price, location, type, "
                    "BHK and status (available / sold / rented)",
                    "Mark listings as featured to highlight them on the "
                    "homepage",
                    "Manage agent profiles and assign listings to agents",
                    "Lead-management dashboard - capture, view and track every "
                    "enquiry with status (new / contacted / closed)",
                    "Publish and manage blog / news posts from the panel",
                    "A guided walkthrough and handover so your team is "
                    "comfortable using everything",
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
        "The backend admin panel covers property listings, agents, leads and blog content; online payment / booking and EMI calculators are not included and can be quoted separately.",
        "Map view uses a standard embeddable map; any paid map or CRM subscription, if required for very high volume, is charged separately.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
