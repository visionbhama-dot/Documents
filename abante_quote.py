"""
Bhama Vision - Abante Integrated facility-management website quotation.

A corporate website for Abante Integrated Management Services Pvt Ltd, a
comprehensive asset & facility management company, with an admin panel to
manage everything, full on-page SEO, free hosting for 1 year and 1 year of
bug & error support. The domain is arranged by the client (not included).

Reuses the Bhama Vision quotation renderer:

    python3 build_abante_quote.py

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
    "company": "Abante Integrated",
    "note": "Facility & asset management website + admin panel (free hosting 1 year, domain not included)",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive corporate facility-management website",
        "Free hosting for 1 year (from our side)",
        "Admin panel to manage everything - pages, services & content",
        "Service / vertical pages + sectors served",
        "Enquiry / contact form + WhatsApp & call buttons",
        "Full on-page SEO (SEO-friendly build)",
        "1 year support for any bugs & errors",
    ],
    "not_covered": [
        "Domain - client's (approx \u20b91,000-\u20b91,500 / year)",
        "Hosting renewal from year 2 (approx \u20b91,500 / year)",
        "Content, images & copywriting (provided by the client)",
        "Logo / brand identity design (separate service)",
        "Ongoing SEO / marketing campaigns (separate service)",
        "Mobile app (Android / iOS) - separate scope",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-063",
        "package": "Website + Admin",
        "title": "Abante Integrated Management Services",
        "subtitle": "Corporate facility & asset management website with an admin panel, full SEO, free hosting for 1 year & 1 year support (domain not included)",
        "price": 50000,
        "price_note": "one-time (incl. free hosting for 1 year)",
        "timeline": "7-15 working days",
        "summary": (
            "Abante Integrated Management Services Pvt Ltd (incorporated in "
            "2015) is a professionally managed, comprehensive asset & "
            "facility management company, serving state-of-the-art corporate "
            "offices, premium residential complexes, modern business centres "
            "and premium hospitals - with services spanning transition "
            "management, electro-mechanical services, housekeeping, safety & "
            "security, horticulture, statutory compliance and financial "
            "management. This quotation is for a modern, responsive corporate "
            "website that presents these services and sectors credibly, "
            "builds trust with prospective clients and captures enquiries. "
            "Every section is editable from a full admin panel so your team "
            "can manage everything without touching code, and the site is "
            "built SEO-friendly so it is ready to be found on Google. It "
            "comes with free hosting for the first year and 1 year of support "
            "for any bugs & errors. The domain is arranged by you (not "
            "included), and we help connect it."
        ),
        "sections": [
            {
                "heading": "Website pages (frontend)",
                "items": [
                    "Home - hero banner, company snapshot, key services & "
                    "clear call-to-action",
                    "About Us - company story (since 2015), vision, mission & "
                    "global best practices",
                    "Services - transition management, electro-mechanical, "
                    "housekeeping, safety & security, horticulture, statutory "
                    "compliance & financial management, each with a detail "
                    "page",
                    "Sectors served - corporate offices, residential "
                    "complexes, business centres & hospitals",
                    "Clients / testimonials and a 'why choose us' section",
                    "Contact Us - enquiry form, WhatsApp & call buttons, "
                    "office address and Google Map",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Admin panel (backend) - manage everything",
                "items": [
                    "Secure admin login with dashboard overview",
                    "Add / edit / delete services & service detail pages",
                    "Manage sectors served, clients & testimonials",
                    "Change images, banners & content across the website",
                    "Enquiry leads inbox - every enquiry captured with "
                    "details",
                    "Manage menus, pages and homepage sections",
                    "Edit SEO meta (title / description) per page",
                ],
            },
            {
                "heading": "Lead capture & enquiry",
                "items": [
                    "Enquiry / contact form capturing name, company, phone, "
                    "service of interest & message",
                    "Submissions delivered to your email and WhatsApp, so no "
                    "enquiry is missed",
                    "Floating WhatsApp click-to-chat + click-to-call button "
                    "on every page",
                    "Spam protection on the form to keep junk enquiries out",
                    "All enquiries also stored in the admin panel",
                ],
            },
            {
                "heading": "SEO, hosting, support & delivery",
                "items": [
                    "Full on-page SEO - titles, meta descriptions, headings, "
                    "clean URLs and image alt text",
                    "XML sitemap, robots.txt & Google Analytics / Search "
                    "Console setup",
                    "Fast-loading, mobile-first build tested across browsers "
                    "& devices",
                    "Free hosting for 1 year from our side with SSL + help "
                    "connecting your domain",
                    "1 year of support for any bugs & errors after launch",
                    "Delivery in 7-15 working days",
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
        "https://abanteindia.com/ is referenced only to understand the company and services; this is a fresh, custom build.",
        "Hosting for the first year is free from our side (with SSL).",
        "The domain is NOT included - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Next-year renewal (from year 2 onwards), paid by the client at actuals: domain approx \u20b91,000-\u20b91,500 / year and hosting approx \u20b91,500 / year.",
        "The website is built SEO-friendly; on-page SEO and Search Console setup help the pages become eligible to rank. Rankings depend on Google and competition and cannot be guaranteed; ongoing SEO / marketing is a separate service.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages / features or redesigns.",
        "Text, photos and content are provided by the client and can be managed via the admin panel.",
        "Timelines begin once the content, logo and advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
