"""
Bhama Vision - saree marketplace website (WhatsApp ordering) quotation content.

A modern saree catalogue / marketplace-style website where every product has
an "Order on WhatsApp" button - customers browse sarees and complete the
order over WhatsApp (no cart / online payment). Comes with a full admin
panel to manage products and categories, with up to 30 products set up.

Reuses the Bhama Vision quotation renderer:

    python3 build_saree_whatsapp_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Scope cap - repeated in the included list, the bullets and the terms so
# the fixed price is unambiguous. Adjust if the client needs more.
MAX_PRODUCTS = 30

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
    "note": "Saree marketplace website with WhatsApp ordering & admin panel",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Modern, responsive saree catalogue website",
        "'Order on WhatsApp' button on every product (details pre-filled)",
        "Admin panel to manage products & categories",
        "Up to {} saree products set up for you".format(MAX_PRODUCTS),
        "Product detail - image gallery, fabric, colour & price",
        "Search, filters & categories (fabric, occasion, colour, price)",
        "Enquiry form + WhatsApp click-to-chat & call buttons",
    ],
    "not_covered": [
        "Domain & hosting - arranged and paid by the client (we help set up)",
        "Online payments / cart checkout & payment gateway (orders via "
        "WhatsApp)",
        "Product photos, descriptions & content (provided by the client)",
        "Logo / brand identity design (separate service)",
        "Multi-vendor seller accounts & logins (single catalogue store)",
        "Mobile app & ongoing marketing / SEO campaigns",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-044",
        "package": "Saree Website + Admin",
        "title": "Saree Marketplace Website",
        "subtitle": "Saree catalogue with WhatsApp ordering & a full admin panel ({} products)".format(MAX_PRODUCTS),
        "price": 9000,
        "price_note": "one-time (design & development)",
        "timeline": "12-16 working days",
        "summary": (
            "A modern, marketplace-style website to showcase your saree "
            "collection and turn visitors into WhatsApp orders. Customers "
            "browse sarees by category, search and filter by fabric, "
            "occasion, colour and price, and open a rich product page with an "
            "image gallery and full details. Instead of a cart and online "
            "payment, every product has an 'Order on WhatsApp' button that "
            "opens a chat with the saree's name, image and price already "
            "filled in - so you close the order personally on WhatsApp. A "
            "full admin panel lets you add and manage products and "
            "categories; we set up your first {} sarees for you. The store is "
            "fully responsive and SEO-friendly.".format(MAX_PRODUCTS)
        ),
        "sections": [
            {
                "heading": "Customer-facing website (frontend)",
                "items": [
                    "Modern, responsive design - home with banners, featured "
                    "sarees & categories",
                    "Saree listing with search, filters & sort (fabric, "
                    "occasion, colour, price)",
                    "Product detail page - image gallery, fabric, colour, "
                    "price and description",
                    "Categories / collections (e.g. silk, cotton, wedding, "
                    "festive, daily wear)",
                    "'Order on WhatsApp' button on every product and a "
                    "floating WhatsApp chat button",
                    "Enquiry form + click-to-call button",
                    "About, contact and policy pages",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Saree product listings",
                "items": [
                    "Up to {} saree products set up for you at "
                    "launch".format(MAX_PRODUCTS),
                    "Each listing with images, fabric, colour, price and "
                    "description",
                    "Organised into categories / collections for quick "
                    "browsing",
                    "Featured / new-arrival sarees highlighted on the home "
                    "page",
                    "Easily add more sarees yourself from the admin panel",
                ],
            },
            {
                "heading": "WhatsApp ordering & enquiry",
                "items": [
                    "'Order on WhatsApp' button on each saree that opens a "
                    "chat with the product name, image link & price "
                    "pre-filled",
                    "Floating WhatsApp click-to-chat button on every page",
                    "Click-to-call button for instant phone enquiries",
                    "Enquiry form capturing name, phone, saree of interest & "
                    "message (reaches email & WhatsApp)",
                    "No cart or online payment - you confirm every order "
                    "personally on WhatsApp",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard",
                    "Add / edit / delete sarees with image upload",
                    "Manage categories, collections & featured items",
                    "Mark items as in stock / sold out / hidden",
                    "View enquiry leads received through the site",
                    "Homepage & banner management + SEO meta per product",
                ],
            },
            {
                "heading": "Design, SEO & delivery",
                "items": [
                    "Modern design matched to your brand colours and logo",
                    "Basic on-page SEO - titles, meta descriptions, clean "
                    "URLs and image alt text",
                    "XML sitemap & Google Analytics / Search Console setup",
                    "Fast-loading, mobile-first build",
                    "Testing across major browsers and devices before launch",
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
    "payment": "40% advance to start, 30% at midway, 30% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
        "Orders are completed over WhatsApp - this package has no cart, online payment or payment gateway. An online-payment store can be added as a separate scope.",
        "Domain and hosting are arranged and paid for by the client directly; we will help set them up and connect them.",
        "This package includes setting up up to {} saree products; additional products can be added by the client via the admin panel.".format(MAX_PRODUCTS),
        "Product photos, descriptions and content are provided by the client.",
        "This is a single-catalogue store; multi-vendor seller accounts and a mobile app are separate.",
        "Timelines begin once the content, logo and advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
