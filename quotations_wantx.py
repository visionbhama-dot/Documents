"""
Bhama Vision - WantX quotation content.

Reverse-marketplace platform (buyers post wants; businesses compete).
Edit prices / features / terms here, then run:
    python3 build_wantx.py

NOTE: Prices below are placeholders set for review - adjust `price` in each
QUOTATION entry to your final commercial number before sending.
"""

# ---------------------------------------------------------------------------
# Company details (shown in footers). Same Bhama Vision branding.
# ---------------------------------------------------------------------------
COMPANY = {
    "name": "Bhama Vision",
    "tagline": "Websites, apps & AI for growing businesses",
    "email": "info@bhamavision.com",
    "phone": "+91 88606 40250",
    "website": "www.bhamavision.com",
    "location": "India",
}

# Client the quotation is prepared for (name kept confidential in the doc).
CLIENT = {
    "name": "Prospective Client",
    "company": "Confidential",
    "note": "WantX - reverse marketplace platform",
}

# Two-column scope card shown on each quotation:
#   left  (highlighted) = what Bhama Vision builds & delivers
#   right (muted)       = third-party subscriptions arranged & paid by the client
REQUIREMENTS = {
    "title": "Scope & requirements",
    "left_label": "Delivered by Bhama Vision",
    "right_label": "On client's side (third-party)",
    "covered": [
        "Complete UI/UX design & development of every panel listed",
        "Database design and all data models",
        "Integration of the third-party services listed alongside",
        "Deployment to the client's hosting / server + handover",
        "Testing and bug fixing before launch",
        "Source code, documentation and a handover walkthrough",
    ],
    "not_covered": [
        "Domain and web hosting / cloud server (and its monthly cost)",
        "AI / LLM API subscription & usage charges for the chat assistant "
        "(e.g. OpenAI / AWS Bedrock)",
        "Amazon Associates account and affiliate-program approval",
        "Maps / geolocation API keys & usage (e.g. Google Maps)",
        "SMS / OTP verification service subscription",
        "WhatsApp Business API (if WhatsApp entry is required)",
        "Payment gateway account and its transaction fees",
        "App Store / Play Store developer accounts (if mobile apps are added)",
        "Any other paid API, plugin or third-party subscription",
    ],
}

# ---------------------------------------------------------------------------
# Quotations.
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-WX1",
        "package": "Complete Platform",
        "title": "WantX Reverse Marketplace",
        "subtitle": "Customer app + Business panel + Affiliate module + Admin",
        "price": 75000,
        "price_note": "one-time (design & development)",
        "timeline": "45-60 working days",
        "summary": (
            "A complete demand-first ('reverse') marketplace. Customers describe "
            "what they want in a simple chat; nearby verified businesses compete "
            "with real offers; and for everyday goods, Amazon products appear "
            "instantly with affiliate links. Includes the customer app, a "
            "multi-user business panel, an affiliate engine and a full admin "
            "panel - fully responsive across mobile, tablet and desktop."
        ),
        "sections": [
            {
                "heading": "Customer app - buyer experience",
                "items": [
                    "Chat-based home screen: post any want in plain language",
                    "Intent understanding to detect category, attributes, budget "
                    "& location from the customer's message",
                    "Live matched listings and competing offers shown in chat",
                    "Side-by-side offer comparison with quick filters "
                    "(budget, brand, distance, delivery, rating)",
                    "Location-aware, nearby-first results",
                    "Category browsing (Automotive, Home, Insurance, Travel, "
                    "Electronics, Healthcare, Real Estate & more)",
                    "Saved / active wants, in-app messaging with sellers, "
                    "ratings, profile & real-time notifications",
                    "Sign up & login with email/phone + OTP verification",
                ],
            },
            {
                "heading": "Business panel - seller portal (multi-user)",
                "items": [
                    "Separate, verified business login & organisation onboarding",
                    "Multi-user team with roles (Owner / Manager / Staff / Viewer)",
                    "Dashboard with KPIs: listings, leads, views & deals won",
                    "Category-driven listing creation - each category shows only "
                    "its relevant fields, with photos & location tagging",
                    "Matched buyer requests (leads) delivered to the business",
                    "Offer builder with reusable templates to respond & win",
                    "Listing management: draft, edit, pause, relist",
                    "Performance analytics and subscription plan / billing view",
                ],
            },
            {
                "heading": "Affiliate / Amazon module",
                "items": [
                    "Auto-fetch of Amazon products for everyday-goods queries",
                    "Affiliate (Associate) tag attached to every product link",
                    "Results rendered as cards inside the customer chat",
                    "Caching layer to respect Amazon API rate limits",
                    "Routing logic: business listings vs affiliate products",
                ],
            },
            {
                "heading": "Admin panel",
                "items": [
                    "Manage categories and their dynamic field schema",
                    "Verify, approve or suspend businesses",
                    "Moderate listings, offers and reported content",
                    "Configure the Amazon affiliate settings",
                    "Platform-wide analytics and reports",
                    "Manage users, plans and payouts",
                ],
            },
            {
                "heading": "Design, technical & delivery",
                "items": [
                    "Modern, responsive UI/UX across mobile, tablet & desktop",
                    "Secure authentication, roles & data handling",
                    "Search & geo-matching for fast, relevant results",
                    "Deployment to the client's hosting and full handover",
                    "Testing & bug fixing before go-live",
                ],
            },
            {
                "heading": "Support & maintenance",
                "items": [
                    "1 year of support for bug fixes and non-functional issues "
                    "(anything that stops working)",
                    "Does not include new features, content changes or redesigns "
                    "(available as a separate retainer / change request)",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
    {
        "id": "BV-Q-2026-WX2",
        "package": "Starter MVP",
        "title": "WantX Reverse Marketplace",
        "subtitle": "Customer chat + Business listings + Search (web) + basic admin",
        "price": 40000,
        "price_note": "one-time (design & development)",
        "timeline": "25-35 working days",
        "summary": (
            "A lean first version to launch and validate the idea quickly. "
            "Customers post wants in chat and see matching business listings; "
            "businesses sign in and upload category-based listings; and a basic "
            "admin panel controls users, categories and listings. AI-powered "
            "language understanding and the affiliate engine are added later "
            "via the Complete Platform."
        ),
        "sections": [
            {
                "heading": "What we will design & develop",
                "items": [
                    "Customer chat to post wants and see matching listings",
                    "Keyword / rule-based matching by category & attributes",
                    "Location-aware, nearby-first results with basic filters",
                    "Business login + category-driven listing upload (single user)",
                    "Basic admin panel: users, categories and listings",
                    "Email/phone + OTP sign up & login",
                    "Fully responsive website (mobile, tablet & desktop)",
                ],
            },
            {
                "heading": "Not included in this package",
                "muted": True,
                "items": [
                    "AI / LLM natural-language understanding (rule-based only here)",
                    "Amazon affiliate module",
                    "Multi-user business teams & roles",
                    "Advanced analytics, offer templates & billing",
                    "Native mobile apps",
                    "(All of the above are covered by the Complete Platform.)",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

# Terms shown on the closing page of every quotation.
TERMS = {
    "validity_days": 15,
    "payment": "40% advance to start, 30% at midway, 30% on delivery "
               "(or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design "
        "& development work quoted.",
        "All third-party subscriptions (hosting, domain, AI/LLM API, Amazon "
        "Associates, maps/geolocation, SMS/OTP, WhatsApp API, payment gateway) "
        "are arranged and paid for by the client directly.",
        "AI assistant and other API usage are recurring costs billed by the "
        "provider to the client based on usage.",
        "Timelines begin once content, access and the advance payment are "
        "received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
