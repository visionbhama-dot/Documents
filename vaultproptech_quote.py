"""
Bhama Vision - Property legal-services website quotation content.

A modern, service-marketplace style website (inspired by vaultproptech.com)
for a property legal & documentation business. Visitors browse services with
prices, book / enquire online and pay through an integrated payment gateway;
the owner manages everything from a full admin panel. Price includes domain
and hosting for 1 year.

Reuses the Bhama Vision quotation renderer:

    python3 build_vaultproptech_quote.py

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
    "company": "Property Legal Services",
    "note": "Service website with online payments, admin panel, domain & hosting",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Modern, responsive service website (like vaultproptech.com)",
        "Domain registration + hosting for 1 year",
        "Payment gateway integration (Razorpay / UPI / cards)",
        "Admin panel to manage services, prices & bookings",
        "Service listing & detail pages with online booking / enquiry",
        "Booking inbox + order / payment records in the admin panel",
        "Basic on-page SEO + WhatsApp / call contact",
    ],
    "not_covered": [
        "Payment gateway company fees / per-transaction charges",
        "Service content, images & legal copy (provided by client)",
        "Hosting / domain renewal from year 2 onwards",
        "Mobile app (Android / iOS) - separate scope",
        "Ongoing marketing / paid ads & content entry",
        "Advanced SEO campaigns & third-party paid APIs",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-036",
        "package": "Service Website + Admin",
        "title": "Property Legal-Services Website",
        "subtitle": "Service marketplace with online payments, admin panel, domain & hosting (1 year)",
        "price": 12000,
        "price_note": "one-time (incl. domain & hosting for 1 year)",
        "timeline": "12-18 working days",
        "summary": (
            "A modern, service-marketplace style website for your property "
            "legal & documentation business, inspired by vaultproptech.com. "
            "Visitors browse your services - each with a price, short "
            "description and a clear call to action - then book or enquire "
            "online and pay instantly through an integrated payment gateway. "
            "A full admin panel lets you add and manage services, prices, "
            "bookings and payments from one place. The package is all-in for "
            "one price: it includes domain registration and hosting for the "
            "first year, so your site goes live without any extra setup from "
            "your side."
        ),
        "sections": [
            {
                "heading": "Visitor-facing website (frontend)",
                "items": [
                    "Modern, responsive design - home with featured services, "
                    "offers and quick search",
                    "Service categories (e.g. registration, due diligence, "
                    "Khata, mutation, EC, drafting)",
                    "Service detail page - price, timeline, what's covered & "
                    "an online book / enquire button",
                    "Online booking / enquiry form with the selected service "
                    "pre-filled",
                    "Integrated payment gateway - pay or part-pay at the time "
                    "of booking",
                    "WhatsApp & call buttons, about, contact and policy pages",
                    "Reviews / 'completed' counts and 'why choose us' sections",
                ],
            },
            {
                "heading": "Online payments",
                "items": [
                    "Payment gateway integration (Razorpay / UPI / cards / "
                    "net-banking)",
                    "Pay full amount or advance against a booked service",
                    "Automatic payment confirmation to customer & admin",
                    "Every payment linked to its booking & service in admin",
                    "Secure, PCI-compliant checkout handled by the gateway",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard overview",
                    "Add / edit / delete services, prices, discounts & "
                    "timelines",
                    "Manage categories and featured / hidden services",
                    "Bookings inbox - every lead & order with customer "
                    "details",
                    "Payment & order records with status tracking",
                    "Homepage & banner management + SEO meta per service",
                ],
            },
            {
                "heading": "Domain, hosting & go-live",
                "items": [
                    "Domain registration for 1 year (.com / .in as available)",
                    "Website hosting for 1 year with SSL (https) included",
                    "Business email setup guidance & DNS configuration",
                    "Deployment, go-live and basic performance setup",
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
        "Price includes domain registration and hosting for the first year; renewals from year 2 are billed separately at actuals.",
        "Payment gateway integration is included; the gateway's own company fees / per-transaction charges are borne by the client.",
        "Service content, images and legal copy are provided by the client.",
        "Basic on-page SEO is included; ongoing SEO / marketing and any paid third-party API are separate.",
        "A mobile app (Android / iOS) is a separate scope.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
