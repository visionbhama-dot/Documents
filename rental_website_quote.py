"""
Bhama Vision - taxi & bike rental website quotation content.

A responsive rental-service website with vehicle listings, an enquiry-based
booking form and WhatsApp integration, with free hosting and 1 year of bug
& error support. The domain is arranged by the client (not on our side).
Reuses the Bhama Vision quotation renderer:

    python3 build_rental_website_quote.py

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
    "company": "Confidential",
    "note": "Taxi & bike rental service website",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive rental website (multiple pages)",
        "Vehicle listings for taxis & bikes with photos and rates",
        "Booking enquiry form (pickup, drop, date/time, vehicle)",
        "WhatsApp integration (click-to-chat + enquiries to WhatsApp)",
        "Google Maps location & contact details",
        "Hosting - free plan",
        "1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Content, vehicle photos & rate details (provided by the client)",
        "Online payment, live GPS tracking or real-time booking system",
        "Driver / vehicle mobile app",
        "SEO / marketing (separate service)",
        "Any paid plugin, tool or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-007",
        "package": "Rental Website",
        "title": "Taxi & Bike Rental Website",
        "subtitle": "Rental service website with vehicle listings & WhatsApp booking",
        "price": 3500,
        "price_note": "one-time (design & development)",
        "timeline": "7-10 working days",
        "summary": (
            "A clean, ready-to-launch website for a taxi and bike rental "
            "business. Customers can browse your available taxis and bikes "
            "with photos and rates, and send a booking enquiry (pickup, drop, "
            "date/time and vehicle) that reaches you directly on WhatsApp. It "
            "comes with a WhatsApp chat button, a free hosting plan and 1 year "
            "of bug & error support. The domain is arranged by you (it is not "
            "on our side), and we will help connect it to the website."
        ),
        "sections": [
            {
                "heading": "What we will design & develop",
                "items": [
                    "A responsive website with pages such as home, about, our "
                    "fleet, tariff / pricing, booking enquiry and contact",
                    "Vehicle listings for taxis (cars) and bikes / scooters - "
                    "photos, details and rental rates",
                    "Booking enquiry form (pickup, drop, date/time, vehicle) "
                    "delivered to your WhatsApp / email",
                    "WhatsApp integration - click-to-chat button so customers "
                    "reach you in one tap",
                    "Google Maps location and clear contact details",
                    "Clean, mobile-friendly design across mobile, tablet & "
                    "desktop",
                    "Free hosting plan setup and go-live; connecting your "
                    "domain (arranged by you)",
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
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Bookings are enquiry-based (sent to WhatsApp / email); online payment, live GPS tracking and real-time booking are not included and can be quoted separately.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
