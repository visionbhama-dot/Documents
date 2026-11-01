"""
Bhama Vision - Home Decor & Mythological Items website + admin quotation.

A clean, responsive product showcase website for home decor and
mythological items, with an admin panel to manage categories and products.
Customers browse the catalogue and enquire / order over WhatsApp. Hosting
for 1 year is free from our side; the domain is arranged by the client
(not included).

Reuses the Bhama Vision quotation renderer:

    python3 build_home_decor_quote.py

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
    "company": "Home Decor & Mythological Items",
    "note": "Product showcase website with admin panel (free hosting 1 year, domain not included)",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Clean, responsive home decor & mythological items website",
        "Free hosting for 1 year (from our side)",
        "Admin panel to manage categories & products",
        "Multiple categories & up to {} products set up".format(MAX_PRODUCTS),
        "Product detail - image gallery, material, size & price",
        "'Order on WhatsApp' button + enquiry form per product",
        "Basic on-page SEO & Google Map on the contact page",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not included)",
        "Hosting renewal from year 2 onwards",
        "Online payments / cart checkout & payment gateway (add-on)",
        "Product photos, descriptions & content (provided by the client)",
        "Logo / brand identity design (separate service)",
        "Mobile app & ongoing marketing / SEO campaigns",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-050",
        "package": "Website + Admin",
        "title": "Home Decor & Mythological Items Website",
        "subtitle": "Product showcase website with an admin panel & WhatsApp ordering (free hosting 1 year, domain not included)",
        "price": 9000,
        "price_note": "one-time (incl. free hosting for 1 year)",
        "timeline": "10-15 working days",
        "summary": (
            "A clean, attractive website to showcase your home decor and "
            "mythological items and turn visitors into WhatsApp orders. Your "
            "products are organised into categories - like idols & statues, "
            "pooja items, wall art, showpieces and festive decor - so "
            "customers can browse quickly, and each product gets its own page "
            "with an image gallery, material, size and price. Every product "
            "has an 'Order on WhatsApp' button and an enquiry form, so buyers "
            "reach you instantly. A full admin panel lets you add and manage "
            "categories and products yourself - we set up up to {} products "
            "for you. The site is fully responsive and SEO-friendly, and "
            "hosting for the first year is free from our side. The domain is "
            "arranged by you (not included), and we help connect "
            "it.".format(MAX_PRODUCTS)
        ),
        "sections": [
            {
                "heading": "Website (frontend)",
                "items": [
                    "Clean, responsive design - home with banners, featured "
                    "items & category highlights",
                    "Categories (e.g. idols & statues, pooja items, wall "
                    "art, showpieces, festive decor)",
                    "Product listing with search, filters & sort (category, "
                    "material, price)",
                    "Product detail page - image gallery, material, size, "
                    "price & description",
                    "'Order on WhatsApp' button on every product + floating "
                    "WhatsApp chat & click-to-call",
                    "Enquiry / contact form, about and policy pages",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Categories & product listings",
                "items": [
                    "Products organised into multiple categories for quick "
                    "browsing",
                    "Up to {} products set up for you at launch".format(
                        MAX_PRODUCTS),
                    "Each listing with images, material, size, price & "
                    "description",
                    "Featured / new-arrival items highlighted on the home "
                    "page",
                    "Easily add more categories & products from the admin "
                    "panel",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard",
                    "Add / edit / delete categories & products with image "
                    "upload",
                    "Mark items as in stock / sold out / featured / hidden",
                    "View enquiry leads received through the site",
                    "Homepage & banner management",
                    "Edit SEO meta (title / description) per product & page",
                ],
            },
            {
                "heading": "Design, SEO, hosting & delivery",
                "items": [
                    "Modern design matched to your brand colours and logo",
                    "Basic on-page SEO - titles, meta descriptions, clean "
                    "URLs and image alt text",
                    "Google Map embedded on the contact page",
                    "XML sitemap & Google Analytics / Search Console setup",
                    "Free hosting for 1 year from our side with SSL + help "
                    "connecting your domain",
                    "Testing across major browsers and devices before launch",
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
        "Hosting for the first year is free from our side (with SSL). Renewal from year 2 onwards is billed separately at actuals.",
        "The domain is NOT included - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Orders are completed over WhatsApp; an online store with cart and payment gateway can be added as a separate scope.",
        "This package includes setting up multiple categories and up to {} products; additional categories and products can be added by the client via the admin panel.".format(MAX_PRODUCTS),
        "Product photos, descriptions and content are provided by the client.",
        "Timelines begin once the content, logo and advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
