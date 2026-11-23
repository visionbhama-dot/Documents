"""
Bhama Vision - astrology website + admin panel quotation content.

A clean, responsive astrology website with an admin panel to manage content,
an enquiry form and WhatsApp contact. Includes free hosting for 1 year and
1 year of support for bugs & errors. The domain is arranged by the client
(not included).

Reuses the Bhama Vision quotation renderer:

    python3 build_astrology_website_quote.py

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
    "company": "Astrology Services",
    "note": "Astrology website + admin panel (free hosting 1 year, domain not included)",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Clean, responsive astrology website",
        "Free hosting for 1 year (from our side)",
        "Admin panel to manage services & content",
        "Standard pages - Home, About, Services, Gallery, Contact",
        "Enquiry form + WhatsApp click-to-chat & call buttons",
        "Basic on-page SEO & Google Map on the contact page",
        "1 year support for any bugs & errors",
    ],
    "not_covered": [
        "Domain - client's (approx \u20b91,000-\u20b91,500 / year)",
        "Hosting renewal from year 2 (approx \u20b91,500 / year)",
        "Online payments / consultation booking & payment gateway (add-on)",
        "Content, images & copywriting (provided by the client)",
        "Logo / brand identity design (separate service)",
        "Mobile app & ongoing marketing / SEO campaigns",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-062",
        "package": "Website + Admin",
        "title": "Astrology Website",
        "subtitle": "Responsive astrology website with an admin panel, free hosting for 1 year & 1 year bug & error support (domain not included)",
        "price": 6000,
        "price_note": "one-time (incl. free hosting for 1 year)",
        "timeline": "7-10 working days",
        "summary": (
            "A clean, professional website for your astrology practice that "
            "builds trust and brings in enquiries. Visitors learn about you "
            "and your experience, explore your services - like kundli / "
            "horoscope, matchmaking, vastu, gemstone and puja guidance - and "
            "get in touch easily through an enquiry form that reaches your "
            "email and WhatsApp, a WhatsApp chat button and a click-to-call "
            "button, with a Google Map on the contact page. A full admin "
            "panel lets you manage your services and content without touching "
            "code. The site is fully responsive and SEO-friendly, hosting for "
            "the first year is free from our side, and the package includes "
            "1 year of support for any bugs and errors. The domain is "
            "arranged by you (not included), and we help connect it."
        ),
        "sections": [
            {
                "heading": "Website pages (frontend)",
                "items": [
                    "Home - hero banner, introduction, services snapshot & "
                    "clear call-to-action",
                    "About - your journey, experience and specialities",
                    "Services - kundli / horoscope, matchmaking, vastu, "
                    "gemstone, puja and more with descriptions",
                    "Gallery - photos, events & certificates",
                    "Testimonials - client experiences to build trust",
                    "Contact - enquiry form, WhatsApp & call buttons, address "
                    "and Google Map",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard",
                    "Add, edit & remove services",
                    "Change images and content across the website",
                    "Add & manage testimonials and gallery images",
                    "View enquiry leads received through the site",
                    "Homepage & banner management + SEO meta per page",
                ],
            },
            {
                "heading": "Enquiry, SEO, hosting & support",
                "items": [
                    "Enquiry form capturing name, phone, service of interest "
                    "and message - delivered to email & WhatsApp",
                    "Floating WhatsApp click-to-chat + click-to-call button "
                    "on every page",
                    "Basic on-page SEO - titles, meta descriptions, clean "
                    "URLs and image alt text",
                    "Google Map on the contact page + Google Analytics / "
                    "Search Console setup",
                    "Free hosting for 1 year from our side with SSL + help "
                    "connecting your domain",
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
    "payment": "50% advance to start, 50% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
        "Hosting for the first year is free from our side (with SSL).",
        "The domain is NOT included - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Next-year renewal (from year 2 onwards), paid by the client at actuals: domain approx \u20b91,000-\u20b91,500 / year and hosting approx \u20b91,500 / year.",
        "Content, images and copywriting are provided by the client and can be managed via the admin panel.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages / features or redesigns.",
        "Online payments / consultation booking and a payment gateway are available as an add-on and quoted separately.",
        "Timelines begin once the content, logo and advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
