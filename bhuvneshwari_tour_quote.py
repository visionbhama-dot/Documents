"""
Bhama Vision - Bhuvneshwari Tour travel website quotation content.

A travel website for Bhuvneshwari Tour (Mumbai, Maharashtra) with a backend
admin panel, free hosting and Indian + international destination pages.
Domain is arranged by the client (not included). Reuses the Bhama Vision
quotation renderer:

    python3 build_bhuvneshwari_tour_quote.py

Edit price, features, client or terms below, then re-run.
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
    "name": "Bhuvneshwari Tour",
    "company": "Bhuvneshwari Tour",
    "note": "Travel website - Mumbai, Maharashtra",
}

# Destination lists provided by the client (typos normalised).
INDIAN = ("Vaishno Devi, Kashmir, Leh Ladakh, Himachal, Punjab, Uttarakhand, "
          "Chardham, Madhya Pradesh, Uttar Pradesh, Rajasthan, Gujarat, "
          "Maharashtra, Goa, Kerala, Telangana, Karnataka, Andaman & Nicobar, "
          "Lakshadweep, North-East, Sikkim & Odisha")
INTERNATIONAL = ("Dubai, Thailand, Singapore, Malaysia, Sri Lanka, Bali, Nepal, "
                 "Bhutan, Turkey, Greece, Mauritius, South Africa, Europe, "
                 "Australia, Azerbaijan, Seychelles, Iceland, Norway, "
                 "New Zealand, Egypt, Maldives, Japan, Korea, China, Russia & USA")

REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive travel website (frontend) + backend admin panel",
        "Indian & international destination pages (full list set up)",
        "Tour package listings with itinerary, inclusions & gallery",
        "Enquiry / booking-request form + WhatsApp click-to-chat",
        "Backend to manage destinations, packages & enquiries",
        "Free hosting (1 year)",
        "Basic on-page SEO setup",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not included)",
        "Tour content, itineraries & photos (provided by the client)",
        "Online payment gateway (can be added on request)",
        "Hosting renewal after the first year (optional, charged separately)",
        "Paid ads / marketing (separate service)",
    ],
}

QUOTATIONS = [
    {
        "id": "BV-Q-2026-061",
        "package": "Travel Website + Admin",
        "title": "Bhuvneshwari Tour - Travel Website",
        "subtitle": "Travel website with backend admin panel & free hosting (domain not included)",
        "price": 9000,
        "price_note": "one-time (design & development)",
        "timeline": "12-16 working days",
        "summary": (
            "A professional, responsive travel website for Bhuvneshwari Tour "
            "(Mumbai, Maharashtra). Visitors explore your Indian and "
            "international destinations and tour packages and send a booking "
            "enquiry over WhatsApp or the enquiry form, so every lead reaches "
            "you directly. A backend admin panel lets you manage destinations, "
            "tour packages and enquiries from one dashboard. The package "
            "includes free hosting for the first year; the domain is arranged "
            "by you (not included) and we will help connect it."
        ),
        "sections": [
            {
                "heading": "Travel website (frontend)",
                "items": [
                    "Home page with hero banner, featured destinations & "
                    "tour packages",
                    "Top Indian Destinations section with dedicated pages",
                    "Top International Destinations section with dedicated "
                    "pages",
                    "Destination page with highlights, photos & related "
                    "packages",
                    "Tour package / itinerary pages with inclusions, days & "
                    "price",
                    "Enquiry / booking-request form that reaches you directly",
                    "WhatsApp click-to-chat for quick enquiries",
                    "Photo gallery, about & contact pages",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Destinations covered",
                "items": [
                    "Indian destinations: " + INDIAN,
                    "International destinations: " + INTERNATIONAL,
                    "More destinations & packages can be added anytime from "
                    "the admin panel",
                ],
            },
            {
                "heading": "Backend admin panel",
                "items": [
                    "Secure admin login",
                    "Add, edit & remove destinations (Indian & international)",
                    "Create & manage tour packages and itineraries",
                    "Upload destination & package photos",
                    "View and manage enquiries / leads",
                    "Homepage banner & featured-destination management",
                    "A short walkthrough so you are comfortable running it",
                ],
            },
            {
                "heading": "Design, hosting & delivery",
                "items": [
                    "Modern design matched to your brand colours and logo",
                    "Basic on-page SEO - titles, meta descriptions & clean "
                    "URLs",
                    "Fast-loading, mobile-first build",
                    "Testing across major browsers and devices before launch",
                    "Free hosting for the first year; deployment and help "
                    "connecting your domain",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

PAYMENT = {
    "account_name": "Prafull Kumar Sharma",
    "upi": "8860640250@idfcfirst",
    "bank": "IDFC First Bank",
    "qr_image": "payment qr.jpeg",
}

TERMS = {
    "validity_days": 15,
    "payment": "50% advance to start, 50% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
        "The domain is NOT included; it is arranged and paid for by the client directly. We will help connect it.",
        "Free hosting is included for the first year; renewal / upgrading afterwards is optional and charged separately.",
        "Tour content, itineraries, destination details and photos are provided by the client.",
        "An online payment gateway is not included in this package; it can be added on request and quoted separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
