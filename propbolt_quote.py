"""
Bhama Vision - PropBolt real estate website quotation content.

A modern, SEO-first real estate website with a full admin panel to list and
manage properties (up to 10 listings set up at launch), rich property detail
pages and WhatsApp / enquiry contact.

Reuses the Bhama Vision quotation renderer:

    python3 build_propbolt_quote.py

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
    "company": "PropBolt",
    "note": "Real estate website with property listings & full SEO",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Modern, responsive real estate website",
        "Admin panel to list & manage properties",
        "Up to 10 property listings set up for you at launch",
        "Rich property pages - gallery, details, map & amenities",
        "Full on-page SEO (meta, sitemap, schema, social cards)",
        "Search & filters (type, location, price, bedrooms)",
        "Enquiry form + WhatsApp / call contact on each property",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Property photos & content (provided by the client)",
        "Online payments / booking & payment gateway",
        "Paid property portals / MLS feeds & any paid API",
        "Mobile app (Android / iOS) - separate scope",
        "Ongoing marketing / paid ads & content entry",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-020",
        "package": "Real Estate Website + Admin",
        "title": "PropBolt Real Estate Website",
        "subtitle": "Property listings with a full admin panel & complete SEO setup",
        "price": 7000,
        "price_note": "one-time (design & development)",
        "timeline": "12-18 working days",
        "summary": (
            "A modern, SEO-first real estate website for PropBolt where "
            "visitors browse properties, search and filter by type, location, "
            "price and bedrooms, and open a rich property page with an image "
            "gallery, full details, amenities and a map. Each listing has an "
            "enquiry form plus WhatsApp / call buttons so buyers reach you "
            "instantly. A full admin panel lets you add and manage properties "
            "- we set up your first 10 listings for you. The whole site is "
            "built with complete on-page SEO so your properties rank and get "
            "found."
        ),
        "sections": [
            {
                "heading": "Visitor-facing website (frontend)",
                "items": [
                    "Modern, responsive design - home with featured & latest "
                    "properties and quick search",
                    "Property listing pages with search & filters (type, "
                    "location, price, bedrooms, status)",
                    "Property detail page - image gallery, price, full "
                    "description, amenities & specifications",
                    "Location map (Google Maps) and nearby highlights",
                    "Enquiry form + WhatsApp & call buttons on every property",
                    "Buy / Rent / Commercial categories and agent / contact "
                    "section",
                    "About, contact and policy pages",
                ],
            },
            {
                "heading": "Property listings",
                "items": [
                    "Up to 10 property listings set up for you at launch",
                    "Each with images, price, location, type, area, bedrooms "
                    "& amenities",
                    "Organised by category (buy / rent / commercial) and "
                    "location",
                    "Featured & 'sold / rented' status flags",
                    "Easily add more listings yourself from the admin panel",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard overview",
                    "Add / edit / delete properties with image upload",
                    "Manage categories, locations, amenities & status",
                    "Mark listings as featured / sold / rented / hidden",
                    "Enquiries inbox - every lead captured with property "
                    "context",
                    "Homepage & banner management + SEO meta per property",
                ],
            },
            {
                "heading": "SEO (complete on-page setup)",
                "items": [
                    "SEO-friendly URLs, titles & meta descriptions per page "
                    "and per property",
                    "Structured data / schema for real-estate listings "
                    "(rich results)",
                    "XML sitemap, robots.txt & clean internal linking",
                    "Open Graph / social share cards for shared links",
                    "Image alt tags, fast mobile-first pages & performance "
                    "basics",
                    "Google Analytics & Search Console setup",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

# Terms shown on the closing page of the quotation.
TERMS = {
    "validity_days": 15,
    "payment": "40% advance to start, 30% at midway, 30% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
        "Domain and hosting are arranged and paid for by the client directly.",
        "This package includes setting up up to 10 property listings; additional listings can be added by the client via the admin panel.",
        "Property photos and content are provided by the client.",
        "Complete on-page SEO is included; ongoing SEO / marketing and any paid portal, MLS feed or API are separate.",
        "Online payments / booking, payment gateway and a mobile app are separate scope.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
