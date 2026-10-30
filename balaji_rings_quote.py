"""
Bhama Vision - Balaji Rings informative product showcase website quotation.

A clean, informative showcase website for Balaji Rings that presents the
ring range with images and details across the standard pages (Home, About,
Products/Collection, Contact), with an enquiry form and WhatsApp so every
lead reaches the client. Hosting is free for 1 year; the domain is arranged
by the client (not included).

Reuses the Bhama Vision quotation renderer:

    python3 build_balaji_rings_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Scope caps - repeated in the included list, the bullets and the terms so
# the fixed price is unambiguous. Adjust if the client needs more.
MAX_CATEGORIES = 4
MAX_PRODUCTS = 20

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
    "company": "Balaji Rings",
    "note": "Informative product showcase website (free hosting 1 year, domain not included)",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Clean, informative, responsive showcase website",
        "Free hosting for 1 year (from our side)",
        "All standard pages - Home, About, Products, Contact",
        "Product range organised into categories",
        "Up to {} categories and {} products set up for you".format(
            MAX_CATEGORIES, MAX_PRODUCTS),
        "Product detail with images, description & specifications",
        "Enquiry form + WhatsApp click-to-chat & call buttons",
        "Basic on-page SEO & Google Map on the contact page",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not included)",
        "Hosting renewal from year 2 onwards",
        "Product photos, descriptions & company content (provided by the "
        "client)",
        "Admin panel to self-manage products (available as an add-on)",
        "Online store / payment gateway & cart checkout",
        "SEO campaigns, paid ads & any paid plugin / API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-038",
        "package": "Product Showcase Website",
        "title": "Balaji Rings",
        "subtitle": "Informative product showcase website with enquiry form & WhatsApp (free hosting 1 year, domain not included)",
        "price": 2500,
        "price_note": "one-time (incl. free hosting for 1 year)",
        "timeline": "7-10 working days",
        "summary": (
            "A clean, informative website for Balaji Rings that puts your "
            "ring range online and gives your business a credible presence. "
            "Products are organised into categories so visitors can browse "
            "quickly, and each product is shown with images, a description "
            "and key details. Alongside the showcase you get all the "
            "standard pages - Home, About, Products and Contact - and it is "
            "easy to get in touch everywhere: an enquiry form that reaches "
            "your email and WhatsApp, a WhatsApp chat button and a "
            "click-to-call button, plus a Google Map on the contact page. "
            "The site is fully responsive and SEO-friendly, and hosting for "
            "the first year is free from our side. The domain is arranged by "
            "you (not included), and we help connect it."
        ),
        "sections": [
            {
                "heading": "Website pages",
                "items": [
                    "Home - hero banner, business snapshot, featured products "
                    "& category highlights",
                    "About - your story, values and why customers choose you",
                    "Products - full range in a clean grid, browsable by "
                    "category",
                    "Product detail - images, description and key details "
                    "(size / variant / specification)",
                    "Contact - enquiry form, WhatsApp & call buttons, address "
                    "and Google Map",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Product showcase & categories",
                "items": [
                    "Products grouped into categories so visitors can narrow "
                    "down quickly",
                    "Up to {} categories and up to {} products in total set "
                    "up with your photos and content".format(
                        MAX_CATEGORIES, MAX_PRODUCTS),
                    "Each product shown with image, name, short description "
                    "and details",
                    "Featured products highlighted on the home page",
                    "Clean, consistent layout that stays tidy as the range "
                    "grows",
                ],
            },
            {
                "heading": "Enquiry & WhatsApp",
                "items": [
                    "Enquiry form capturing name, phone, product of interest "
                    "and message",
                    "Submissions delivered to your email and WhatsApp, so no "
                    "lead is missed",
                    "Floating WhatsApp click-to-chat button on every page",
                    "Click-to-call button for instant phone enquiries",
                    "Thank-you confirmation shown after submitting",
                ],
            },
            {
                "heading": "Design, SEO, hosting & delivery",
                "items": [
                    "Modern, professional design matched to your brand "
                    "colours and logo",
                    "Basic on-page SEO - page titles, meta descriptions, "
                    "clean URLs and image alt text",
                    "Google Map embedded on the contact page",
                    "Fast-loading, mobile-first build",
                    "Testing across major browsers and devices before launch",
                    "Free hosting for 1 year from our side + help connecting "
                    "your domain",
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
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "Hosting for the first year is free from our side (included). Renewal from year 2 onwards is billed separately at actuals.",
        "The domain is NOT included - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Product photos, descriptions and company content are provided by the client.",
        "Enquiries reach you by email and WhatsApp; an admin panel to add and edit products yourself is available as an add-on and is quoted separately.",
        "Timelines begin once the content, logo and advance payment are received.",
        "This is an informative showcase site; online store / payment gateway and cart checkout are a separate scope.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
