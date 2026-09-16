"""
Bhama Vision - animated digital-services website + admin panel quotation.

An animated, modern website for a digital-services company, backed by an
admin panel to manage all images, blogs, portfolio, client logos and
testimonials, and to view the enquiry leads received through the site.
Reuses the Bhama Vision quotation renderer:

    python3 build_digital_services_quote.py

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
    "note": "Animated digital-services website with admin panel",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Animated, responsive website for digital services",
        "Admin panel to manage all images",
        "Blog management (write, edit & publish)",
        "Portfolio management (add & edit projects)",
        "Client logos management",
        "Testimonials management",
        "Enquiry leads inbox (view leads received from the site)",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Content, images & copywriting (provided by the client)",
        "Logo / brand identity design (separate service)",
        "Online store / payment gateway features",
        "Ongoing monthly SEO or ad campaigns (separate service)",
        "Any paid plugin, tool, font or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-017",
        "package": "Website + Admin",
        "title": "Animated Website with Admin Panel",
        "subtitle": "Digital-services website with a backend to manage content & enquiry leads",
        "price": 9000,
        "price_note": "one-time (design & development)",
        "timeline": "12-18 working days",
        "summary": (
            "A modern, animated website to showcase your digital services, "
            "backed by an easy-to-use admin panel so you can run it yourself. "
            "Smooth scroll and section animations give the site a premium "
            "feel, while the backend lets you change every image, publish "
            "blogs, update your portfolio, manage client logos and add "
            "testimonials - all without touching code. Every enquiry sent "
            "through the site lands in a leads inbox you can view any time."
        ),
        "sections": [
            {
                "heading": "Frontend (animated website)",
                "items": [
                    "Animated, responsive website - home, about, services, "
                    "portfolio, blog, testimonials & contact",
                    "Smooth scroll effects and section / element animations "
                    "for a premium feel",
                    "Services section to present your digital services",
                    "Portfolio / work showcase with project entries",
                    "Client logos strip and testimonials section",
                    "Blog section for articles & updates",
                    "Enquiry / contact form to capture leads",
                    "Optimised across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Backend (admin panel)",
                "items": [
                    "Change all images across the website",
                    "Write, edit, publish & delete blog articles",
                    "Add, edit & remove portfolio / work items",
                    "Manage client logos (add, replace & remove)",
                    "Add & manage testimonials",
                    "View enquiry leads received through the site",
                    "Secure admin login",
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
        "Domain and hosting are arranged and paid for by the client directly; we will help set them up.",
        "Content, images, blog articles, portfolio items, client logos and testimonials are added by the client via the admin panel.",
        "Enquiry leads are captured and shown in the admin panel; email/SMS delivery of leads can be added on request.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
