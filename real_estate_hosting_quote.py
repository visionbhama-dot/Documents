"""
Bhama Vision - real estate website + admin (with hosting) quotation content.

A modern, SEO-first real estate website with a full admin panel to list and
manage properties, rich property detail pages and WhatsApp / enquiry contact.
Hosting for 1 year is included from our side; the domain is arranged by the
client (not included).

Reuses the Bhama Vision quotation renderer:

    python3 build_real_estate_hosting_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Scope cap - repeated in the included list, the bullets and the terms so
# the fixed price is unambiguous. Adjust if the client needs more.
MAX_LISTINGS = 15

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
    "note": "Real estate website with admin panel & hosting (domain not included)",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Modern, responsive real estate website",
        "Admin panel to list & manage properties",
        "Hosting for 1 year (from our side)",
        "Up to {} property listings set up for you at launch".format(
            MAX_LISTINGS),
        "Rich property pages - gallery, details, map & amenities",
        "Search & filters (type, location, price, bedrooms)",
        "Enquiry form + WhatsApp / call on each property + on-page SEO",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not included)",
        "Hosting renewal from year 2 onwards",
        "Property photos & content (provided by the client)",
        "Online payments / booking & payment gateway",
        "Paid property portals / MLS feeds & any paid API",
        "Mobile app (Android / iOS) & ongoing marketing / ads",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-043",
        "package": "Real Estate Website + Admin",
        "title": "Real Estate Website",
        "subtitle": "Property listings with a full admin panel, complete SEO & 1 year hosting (domain not included)",
        "price": 9000,
        "price_note": "one-time (incl. hosting for 1 year)",
        "timeline": "12-18 working days",
        "summary": (
            "A modern, SEO-first real estate website where visitors browse "
            "properties, search and filter by type, location, price and "
            "bedrooms, and open a rich property page with an image gallery, "
            "full details, amenities and a map. Each listing has an enquiry "
            "form plus WhatsApp / call buttons so buyers reach you instantly. "
            "A full admin panel lets you add and manage properties - we set "
            "up your first {} listings for you. The whole site is built with "
            "complete on-page SEO so your properties rank and get found. "
            "Hosting for the first year is included from our side; the domain "
            "is arranged by you (not included), and we will help connect "
            "it.".format(MAX_LISTINGS)
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
                    "Up to {} property listings set up for you at "
                    "launch".format(MAX_LISTINGS),
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
                "heading": "SEO, hosting & delivery",
                "items": [
                    "SEO-friendly URLs, titles & meta descriptions per page "
                    "and per property",
                    "Structured data / schema for real-estate listings "
                    "(rich results)",
                    "XML sitemap, robots.txt & clean internal linking",
                    "Open Graph / social share cards for shared links",
                    "Google Analytics & Search Console setup",
                    "Hosting for 1 year included from our side with SSL + "
                    "help connecting your domain",
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
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
        "Hosting for the first year is included from our side (with SSL). Renewal from year 2 onwards is billed separately at actuals.",
        "The domain is NOT included - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "This package includes setting up up to {} property listings; additional listings can be added by the client via the admin panel.".format(MAX_LISTINGS),
        "Property photos and content are provided by the client.",
        "Complete on-page SEO is included; ongoing SEO / marketing and any paid portal, MLS feed or API are separate.",
        "Online payments / booking, payment gateway and a mobile app are a separate scope.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
