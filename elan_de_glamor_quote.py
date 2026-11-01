"""
Bhama Vision - Elan De Glamor fragrance brand website quotation content.

A premium, responsive fragrance brand website for Elan De Glamor showcasing
6 signature fragrances, with a full admin panel to manage the products.
Customers browse the collection and enquire / order over WhatsApp.

Reuses the Bhama Vision quotation renderer:

    python3 build_elan_de_glamor_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Scope cap - repeated in the included list, the bullets and the terms so
# the fixed price is unambiguous. Adjust if the client needs more.
MAX_PRODUCTS = 6

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
    "company": "Elan De Glamor",
    "note": "Fragrance brand website (6 fragrances) with admin panel",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Premium, responsive fragrance brand website",
        "Admin panel to manage the fragrances",
        "{} signature fragrances set up for you".format(MAX_PRODUCTS),
        "Product detail - gallery, scent notes, size & price",
        "'Order on WhatsApp' button + enquiry form per product",
        "Brand story, about & contact pages",
        "Basic on-page SEO & Google Map on the contact page",
    ],
    "not_covered": [
        "Domain & hosting - arranged and paid by the client (we help set up)",
        "Online payments / cart checkout & payment gateway (add-on)",
        "Product photos, scent copy & content (provided by the client)",
        "Logo / brand identity design (separate service)",
        "Additional fragrances beyond {} (added via the admin "
        "panel)".format(MAX_PRODUCTS),
        "Mobile app & ongoing marketing / SEO campaigns",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-045",
        "package": "Fragrance Website + Admin",
        "title": "Elan De Glamor",
        "subtitle": "Premium fragrance brand website showcasing {} fragrances, with an admin panel".format(MAX_PRODUCTS),
        "price": 7000,
        "price_note": "one-time (design & development)",
        "timeline": "8-12 working days",
        "summary": (
            "A premium, elegant website for Elan De Glamor that presents your "
            "fragrance collection beautifully and builds the brand. Visitors "
            "explore your {} signature fragrances, each with its own page - "
            "an image gallery, scent notes (top / heart / base), size and "
            "price - alongside your brand story and contact details. Every "
            "fragrance has an 'Order on WhatsApp' button and an enquiry form, "
            "so customers reach you instantly to place an order. A full admin "
            "panel lets you update the fragrances, images and content "
            "yourself - no code needed. The site is fully responsive and "
            "SEO-friendly.".format(MAX_PRODUCTS)
        ),
        "sections": [
            {
                "heading": "Website (frontend)",
                "items": [
                    "Premium, responsive design - home with hero banner, "
                    "featured fragrances & brand feel",
                    "Collection page showing all {} fragrances in a clean "
                    "grid".format(MAX_PRODUCTS),
                    "Fragrance detail page - image gallery, scent notes "
                    "(top / heart / base), size (ml), price & description",
                    "Brand story / about page and contact page",
                    "'Order on WhatsApp' button on each fragrance + floating "
                    "WhatsApp chat & click-to-call buttons",
                    "Enquiry form capturing name, phone, fragrance of "
                    "interest & message",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Fragrance listings",
                "items": [
                    "{} signature fragrances set up for you at "
                    "launch".format(MAX_PRODUCTS),
                    "Each with images, scent notes, size / variant, price & "
                    "description",
                    "Featured fragrances highlighted on the home page",
                    "Easily add or update fragrances yourself from the admin "
                    "panel",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard",
                    "Add / edit / delete fragrances with image upload",
                    "Update scent notes, size, price & description",
                    "Manage featured items and homepage banners",
                    "View enquiry leads received through the site",
                    "Edit SEO meta (title / description) per fragrance & page",
                ],
            },
            {
                "heading": "Design, SEO & delivery",
                "items": [
                    "Elegant design matched to your brand colours and logo",
                    "Basic on-page SEO - titles, meta descriptions, clean "
                    "URLs and image alt text",
                    "Google Map embedded on the contact page",
                    "XML sitemap & Google Analytics / Search Console setup",
                    "Fast-loading, mobile-first build tested across browsers "
                    "& devices",
                    "Deployment and help connecting your domain & hosting",
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
        "This package showcases {} fragrances with ordering over WhatsApp; a full online store with cart and payment gateway can be added as a separate scope.".format(MAX_PRODUCTS),
        "Domain and hosting are arranged and paid for by the client directly; we will help set them up and connect them.",
        "Product photos, scent copy and content are provided by the client and can be managed via the admin panel.",
        "Additional fragrances beyond {} can be added by the client via the admin panel.".format(MAX_PRODUCTS),
        "Timelines begin once the content, logo and advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
