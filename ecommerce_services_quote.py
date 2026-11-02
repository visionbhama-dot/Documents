"""
Bhama Vision - e-commerce + services website quotation content.

A combined website that both sells products online (cart, checkout, payment
gateway) and presents services (with enquiry / booking over WhatsApp),
backed by a full admin panel. Up to 30 listings (products + services).
Hosting for 1 year is free from our side; the domain is arranged by the
client (not included).

Reuses the Bhama Vision quotation renderer:

    python3 build_ecommerce_services_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Scope cap - repeated in the included list, the bullets and the terms so
# the fixed price is unambiguous. Adjust if the client needs more.
MAX_LISTINGS = 30

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
    "note": "E-commerce + services website with backend (free hosting 1 year, domain not included)",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive e-commerce + services website",
        "Free hosting for 1 year (from our side)",
        "Backend admin panel to manage products, services & orders",
        "Up to {} listings (products + services) set up".format(MAX_LISTINGS),
        "Payment gateway integration + Cash on Delivery (products)",
        "Cart & checkout + service enquiry / booking over WhatsApp",
        "Basic on-page SEO & Google Map on the contact page",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not included)",
        "Hosting renewal from year 2 onwards",
        "Payment gateway account & its transaction fees",
        "SMS / email / OTP service subscription",
        "Product / service photos & content (provided by the client)",
        "Multi-vendor features, mobile app & paid plugins / APIs",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-051",
        "package": "E-Commerce + Services + Admin",
        "title": "E-Commerce & Services Website",
        "subtitle": "Sell products online and showcase services, with a backend admin panel, {} listings & free 1 year hosting (domain not included)".format(MAX_LISTINGS),
        "price": 9000,
        "price_note": "one-time (incl. free hosting for 1 year)",
        "timeline": "14-20 working days",
        "summary": (
            "One website that does two jobs - it sells your products online "
            "and showcases your services. On the shop side, customers browse "
            "products, add to cart and check out securely with an integrated "
            "payment gateway or Cash on Delivery. On the services side, each "
            "service has its own page with details and an enquiry / booking "
            "button that reaches you over WhatsApp and email. We set up up to "
            "{} listings in total (products + services). A full backend admin "
            "panel lets you manage products, services, categories, orders and "
            "enquiries from one place. The site is responsive and "
            "SEO-friendly, and hosting for the first year is free from our "
            "side. The domain is arranged by you (not included), and we help "
            "connect it.".format(MAX_LISTINGS)
        ),
        "sections": [
            {
                "heading": "Customer-facing website (frontend)",
                "items": [
                    "Modern, responsive design - home with banners, featured "
                    "products & services",
                    "Shop section - product listing with search, filters & "
                    "sort (category, price)",
                    "Product detail page - image gallery, price, variants, "
                    "stock & add to cart",
                    "Services section - each service with details, pricing "
                    "(if shown) & an enquiry / booking button",
                    "Cart & secure checkout (payment gateway + Cash on "
                    "Delivery)",
                    "WhatsApp click-to-chat & click-to-call on products & "
                    "services",
                    "About, contact (with Google Map) and policy pages",
                ],
            },
            {
                "heading": "Listings (products + services)",
                "items": [
                    "Up to {} listings in total set up for you at launch "
                    "(products + services)".format(MAX_LISTINGS),
                    "Products with images, price, variants & stock",
                    "Services with description, pricing (optional) & "
                    "enquiry / booking",
                    "Both organised into categories for quick browsing",
                    "Featured products & services highlighted on the home "
                    "page",
                    "Easily add more products / services from the admin "
                    "panel",
                ],
            },
            {
                "heading": "Payment, cart & enquiry",
                "items": [
                    "Payment gateway integration (Razorpay / PayU / Cashfree "
                    "or similar) for products",
                    "Accept UPI, cards, net-banking & wallets + Cash on "
                    "Delivery",
                    "Secure checkout with order confirmation to you & the "
                    "customer",
                    "Service enquiry / booking form - submissions reach your "
                    "email & WhatsApp",
                    "Every order & enquiry stored in the admin panel",
                ],
            },
            {
                "heading": "Backend admin panel",
                "items": [
                    "Secure admin login with dashboard overview",
                    "Manage products, categories, variants & stock (add / "
                    "edit / delete)",
                    "Manage services & their details",
                    "Order management - view, update status, invoices & "
                    "mark delivered",
                    "Enquiry / booking inbox for services",
                    "Homepage & banner management + SEO meta per listing",
                ],
            },
            {
                "heading": "Design, SEO, hosting & delivery",
                "items": [
                    "Modern design matched to your brand colours and logo",
                    "Basic on-page SEO - titles, meta descriptions, clean "
                    "URLs and image alt text",
                    "XML sitemap & Google Analytics / Search Console setup",
                    "Fast-loading, mobile-first build tested across browsers "
                    "& devices",
                    "Free hosting for 1 year from our side with SSL + help "
                    "connecting your domain",
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
        "The payment gateway account (and its transaction fees) and any SMS / OTP subscription are arranged and paid for by the client directly.",
        "This package includes setting up up to {} listings in total (products + services); additional listings can be added by the client via the admin panel.".format(MAX_LISTINGS),
        "Product / service photos and content are provided by the client.",
        "Multi-vendor features and a mobile app are a separate scope.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
