"""
Bhama Vision - website + admin panel quotation content.

A modern, SEO-friendly business website with an easy-to-use admin panel to
manage content, images and enquiry leads. Comes with 1 year of support for
bugs & errors. The domain is arranged by the client (not on our side).

Reuses the Bhama Vision quotation renderer:

    python3 build_website_admin_support_quote.py

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
    "note": "SEO-friendly website + admin panel with 1 year bug & error support",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Modern, responsive, SEO-friendly website",
        "Admin panel to manage content, images & pages",
        "Standard pages - Home, About, Services, Gallery, Contact",
        "Enquiry form + WhatsApp click-to-chat & call buttons",
        "Enquiry leads inbox in the admin panel",
        "Basic on-page SEO & Google Map on the contact page",
        "1 year support for any bugs & errors",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Content, images & copywriting (provided by the client)",
        "Logo / brand identity design (separate service)",
        "Online store / payment gateway & cart checkout",
        "Ongoing SEO or ad campaigns & any paid plugin / tool / API",
        "Mobile app (Android / iOS) - separate scope",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-041",
        "package": "Website + Admin",
        "title": "Website with Admin Panel",
        "subtitle": "SEO-friendly website with an admin panel & 1 year bug & error support (domain not on our side)",
        "price": 12000,
        "price_note": "one-time (design & development)",
        "timeline": "12-18 working days",
        "summary": (
            "A modern, professional and fully responsive website for your "
            "business, built SEO-friendly so it is ready to be found on "
            "Google, and backed by an easy-to-use admin panel so you can run "
            "it yourself. From the backend you can change images, update your "
            "pages and content and view every enquiry that comes through the "
            "site - all without touching code. Getting in touch is effortless "
            "for visitors through an enquiry form that reaches your email and "
            "WhatsApp, a WhatsApp chat button and a click-to-call button. The "
            "package includes 1 year of support for any bugs and errors after "
            "launch. The domain is arranged by you (it is not on our side), "
            "and we will help connect it."
        ),
        "sections": [
            {
                "heading": "Website pages (frontend)",
                "items": [
                    "Home - hero banner, business snapshot, services & clear "
                    "call-to-action",
                    "About - your story, values and why customers should "
                    "choose you",
                    "Services - your offerings presented with descriptions",
                    "Gallery / portfolio - showcase your work or photos",
                    "Contact - enquiry form, WhatsApp & call buttons, address "
                    "and Google Map",
                    "Supporting pages as needed (e.g. testimonials, FAQ)",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard",
                    "Change images and content across the website",
                    "Add, edit & remove services / pages & gallery items",
                    "Manage homepage banners & highlights",
                    "View enquiry leads received through the site",
                    "Edit SEO meta (title / description) per page",
                ],
            },
            {
                "heading": "SEO-friendly build",
                "items": [
                    "On-page SEO - page titles, meta descriptions, headings, "
                    "clean URLs and image alt text",
                    "XML sitemap and robots.txt for search engines",
                    "Open Graph / social share cards for shared links",
                    "Fast-loading, mobile-first pages",
                    "Google Analytics & Search Console setup",
                ],
            },
            {
                "heading": "Enquiry, support & delivery",
                "items": [
                    "Enquiry form capturing name, phone, subject and message "
                    "- delivered to email & WhatsApp and stored in admin",
                    "Floating WhatsApp click-to-chat + click-to-call button "
                    "on every page",
                    "Google Map embedded on the contact page",
                    "Testing across major browsers and devices before launch",
                    "Deployment and help connecting your domain",
                    "1 year of support for any bugs & errors after launch",
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
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Content, images and copywriting are provided by the client and can be managed via the admin panel.",
        "The website is built SEO-friendly; on-page SEO and Search Console setup help your pages become eligible to rank. Search rankings depend on Google and competition and cannot be guaranteed. Ongoing monthly SEO and ad campaigns are a separate service.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages / features or redesigns.",
        "Online store / payment gateway and a mobile app are a separate scope.",
        "Timelines begin once the content, logo and advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
