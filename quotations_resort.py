"""
Bhama Vision - Resort / Cottage informative website quotation.

Reference style: an eco-resort site (e.g. earthoraresort.in) with cottage &
places listings, rooms & tariffs, dining & gallery, tourism and guest reviews.

Two options:
  - With Admin Panel      -> owner manages listings himself   (Rs 2,499)
  - Catalogue (No Admin)  -> same site, content set by us      (Rs 1,499)

Build:  python3 build_resort.py
"""

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
    "note": "Resort & cottage informative website",
}

# Two-column scope card.
REQUIREMENTS = {
    "title": "Scope & requirements",
    "left_label": "Delivered by Bhama Vision",
    "right_label": "On client's side (third-party)",
    "covered": [
        "Complete, responsive website design & development",
        "All pages/sections listed in this quotation",
        "Enquiry / contact form and click-to-call & WhatsApp",
        "Google Map location embed and basic on-page SEO setup",
        "Deployment to the client's hosting + handover",
        "Testing and bug fixing before launch",
    ],
    "not_covered": [
        "Domain and web hosting / server (and its yearly cost)",
        "All content: cottage & room photos, videos, text, logo, "
        "tariffs and place/tourism details",
        "Business email account, if required",
        "Google Business / Maps listing (we embed; the account is the client's)",
        "Any paid plugin, stock media or third-party API",
        "Online payment gateway (only if online booking/payment is added later)",
    ],
}

QUOTATIONS = [
    {
        "id": "BV-Q-2026-ER1",
        "package": "With Admin Panel",
        "title": "Resort & Cottage Website",
        "subtitle": "Informative website + admin panel to manage all listings",
        "price": 2499,
        "price_note": "one-time (design & development)",
        "timeline": "10-14 working days",
        "summary": (
            "A beautiful, informative website for a resort/cottage stay, plus a "
            "simple admin panel so the owner can add and manage listings himself "
            "- cottages/rooms, places to visit, gallery, dining and guest "
            "reviews - without any coding. Fully responsive on mobile, tablet "
            "and desktop."
        ),
        "sections": [
            {
                "heading": "Website (front-end) pages & sections",
                "items": [
                    "Home: hero, highlights, amenities & call-to-action",
                    "Stay - Rooms & Tariffs: cottage/room listings with photos, "
                    "features and pricing",
                    "Experiences: activities & things to do at the property",
                    "Regional Tourism: nearby places/attractions listings",
                    "Dining & Gallery: restaurant info + photo gallery",
                    "Guest Reviews: testimonials from visitors",
                    "Contact: enquiry form, map, click-to-call & WhatsApp",
                    "'Book Now' button (links to call / WhatsApp / enquiry)",
                ],
            },
            {
                "heading": "Admin panel - owner can manage",
                "items": [
                    "Add / edit / remove cottage & room listings with tariffs",
                    "Add / edit places & tourism listings",
                    "Upload and organise gallery / experience photos",
                    "Manage dining details and guest reviews",
                    "Update home-page highlights and contact details",
                    "Secure admin login",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
    {
        "id": "BV-Q-2026-ER2",
        "package": "Catalogue (No Admin)",
        "title": "Resort & Cottage Website",
        "subtitle": "Same informative website, content set up by us (no admin panel)",
        "price": 1499,
        "price_note": "one-time (design & development)",
        "timeline": "5-8 working days",
        "summary": (
            "The same informative resort/cottage website with all the same "
            "sections - cottages, tourism places, gallery, dining and reviews - "
            "but without a self-service admin panel. We set up all the content "
            "for you at launch; future changes are handled by us as a small "
            "update request."
        ),
        "sections": [
            {
                "heading": "Website (front-end) pages & sections",
                "items": [
                    "Home: hero, highlights, amenities & call-to-action",
                    "Stay - Rooms & Tariffs: cottage/room listings with photos "
                    "and pricing",
                    "Experiences & Regional Tourism: activities and nearby places",
                    "Dining & Gallery: restaurant info + photo gallery",
                    "Guest Reviews: visitor testimonials",
                    "Contact: enquiry form, map, click-to-call & WhatsApp",
                    "'Book Now' button (links to call / WhatsApp / enquiry)",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Not included in this package",
                "muted": True,
                "items": [
                    "Self-service admin panel to manage listings",
                    "Owner-side add/edit of cottages, places, gallery & reviews",
                    "(All of the above are covered by the 'With Admin Panel' option.)",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

TERMS = {
    "validity_days": 15,
    "payment": "50% advance to start and 50% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design "
        "& development work quoted.",
        "Domain, hosting and any paid plugin/API are arranged and paid for by "
        "the client directly.",
        "Content (photos, videos, text, tariffs, logo) is provided by the client.",
        "Timelines begin once content, access and the advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
