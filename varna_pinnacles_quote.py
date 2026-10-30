"""
Bhama Vision - Varna Pinnacles digital-services website quotation content.

A modern, responsive website for Varna Pinnacles (a digital-services company)
with an easy-to-use admin panel to manage content - images, services,
portfolio, blog, testimonials - and to view enquiry leads. Domain and hosting
are arranged by the client (not included in this package).

Reuses the Bhama Vision quotation renderer:

    python3 build_varna_pinnacles_quote.py

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
    "company": "Varna Pinnacles",
    "note": "Digital-services website design with admin panel (domain not included)",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Modern, responsive website for digital services",
        "Admin panel to manage website content",
        "Manage all images across the site",
        "Services & portfolio management (add / edit)",
        "Blog management (write, edit & publish)",
        "Testimonials & client logos management",
        "Enquiry leads inbox (view leads from the site)",
    ],
    "not_covered": [
        "Domain (arranged & paid by the client)",
        "Hosting (arranged & paid by the client)",
        "Content, images & copywriting (provided by the client)",
        "Logo / brand identity design (separate service)",
        "Online store / payment gateway features",
        "Ongoing SEO or ad campaigns & any paid plugin / API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-037",
        "package": "Website + Admin",
        "title": "Varna Pinnacles Digital-Services Website",
        "subtitle": "Website design with an admin panel to manage content & enquiry leads (domain not included)",
        "price": 4800,
        "price_note": "one-time (design & development)",
        "timeline": "10-15 working days",
        "summary": (
            "A clean, modern and responsive website for Varna Pinnacles to "
            "present its digital services, backed by an easy-to-use admin "
            "panel so you can run it yourself. The design works smoothly "
            "across mobile, tablet and desktop, while the backend lets you "
            "change images, update services and portfolio, publish blogs and "
            "manage testimonials - all without touching code. Every enquiry "
            "sent through the site lands in a leads inbox you can view any "
            "time. Domain and hosting are arranged by you; we help set them "
            "up."
        ),
        "sections": [
            {
                "heading": "Frontend (website design)",
                "items": [
                    "Modern, responsive website - home, about, services, "
                    "portfolio, blog, testimonials & contact",
                    "Clean layout with subtle scroll / section animations",
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
                    "Secure admin login with dashboard",
                    "Change all images across the website",
                    "Add, edit & remove services",
                    "Add, edit & remove portfolio / work items",
                    "Write, edit, publish & delete blog articles",
                    "Manage client logos & testimonials",
                    "View enquiry leads received through the site",
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
        "Domain and hosting are NOT included; they are arranged and paid for by the client directly. We will help set them up.",
        "Content, images, blog articles, portfolio items, client logos and testimonials are added by the client via the admin panel.",
        "Enquiry leads are captured and shown in the admin panel; email / SMS delivery of leads can be added on request.",
        "Online store / payment gateway is a separate scope.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
