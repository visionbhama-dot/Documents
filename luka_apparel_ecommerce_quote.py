"""
Bhama Vision - apparel e-commerce website quotation content.

A single-seller online clothing store (oversized t-shirts, hoodies &
sweatshirts) styled on the reference site lukaoriginals.com: shop-by-
collection, size / colour variants and a secure checkout. Includes up to 25
product listings, payment gateway integration and a backend admin panel.
Domain and hosting are arranged by the client (not included). Reuses the
Bhama Vision quotation renderer:

    python3 build_luka_apparel_ecommerce_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Scope cap - repeated in the included list, the bullets and the terms so
# the fixed price is unambiguous. Adjust if the client needs more.
MAX_PRODUCTS = 25

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
    "note": "Apparel e-commerce website (25 products) with payment integration & admin panel - reference: lukaoriginals.com",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive clothing store (frontend) + backend admin panel",
        "Shop-by-collection layout with size & colour variants",
        "Up to {} product listings set up with photos, price & details".format(MAX_PRODUCTS),
        "Payment gateway integration (UPI / cards / net-banking / wallets)",
        "Cart, secure checkout & Cash on Delivery",
        "Backend to manage products, orders & customers",
        "WhatsApp integration (click-to-chat button)",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not included)",
        "Hosting - arranged and paid by the client (not included)",
        "Payment gateway account & its transaction fees",
        "Product photos & content (provided by the client)",
        "Products beyond {} (added at a small per-product charge)".format(MAX_PRODUCTS),
        "SMS / email / OTP service subscription & SEO / marketing",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-054",
        "package": "Apparel Store + Admin",
        "title": "Apparel E-Commerce Website (25 Products)",
        "subtitle": "Clothing store with shop-by-collection, payment integration & backend admin panel (style reference: lukaoriginals.com)",
        "price": 8000,
        "price_note": "one-time (design & development)",
        "timeline": "14-18 working days",
        "summary": (
            "A clean, modern online clothing store for a single seller - "
            "styled on the look and feel of lukaoriginals.com - with up to {} "
            "product listings and a backend admin panel to run it. Customers "
            "shop by collection, pick size and colour variants, add items to "
            "the cart and check out securely with an integrated payment "
            "gateway (UPI / cards / net-banking / wallets) or Cash on "
            "Delivery, while you manage products, orders and customers from "
            "one dashboard. It includes a WhatsApp chat button for quick "
            "enquiries. Domain and hosting are arranged by you (not "
            "included), and we will help set them up and connect "
            "them.".format(MAX_PRODUCTS)
        ),
        "sections": [
            {
                "heading": "Customer-facing store (frontend)",
                "items": [
                    "Modern home page with hero banners, featured products & "
                    "trust badges",
                    "Shop-by-collection layout (e.g. t-shirts, hoodies, "
                    "sweatshirts)",
                    "Product listing with search, sort & collection filters",
                    "Product detail page with image gallery, size & colour "
                    "variants and size guide",
                    "Up to {} product listings set up with photos, price and "
                    "details".format(MAX_PRODUCTS),
                    "Add to cart and smooth, secure checkout",
                    "Order placement with order confirmation to you & the "
                    "customer",
                    "WhatsApp click-to-chat button for quick enquiries",
                    "Content pages: about, contact and policy pages",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Payment gateway integration",
                "items": [
                    "Integration of a leading Indian payment gateway "
                    "(Razorpay / PayU / Cashfree or similar)",
                    "Accept UPI, credit / debit cards, net-banking & wallets",
                    "Secure checkout with order confirmation",
                    "Cash on Delivery as an additional option",
                ],
            },
            {
                "heading": "Backend admin panel",
                "items": [
                    "Secure admin login for the store owner",
                    "Add, edit and remove products, collections & size/colour "
                    "variants",
                    "Upload product photos and set price, stock and status",
                    "Order management - view orders and update status "
                    "(new / shipped / delivered)",
                    "Basic customer list and enquiries",
                    "Homepage banner & featured-collection management",
                    "A short walkthrough so you are comfortable running the "
                    "store",
                ],
            },
            {
                "heading": "Design, SEO & delivery",
                "items": [
                    "Modern design matched to your brand colours and logo",
                    "Basic on-page SEO - titles, meta descriptions & clean "
                    "URLs",
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
    "payment": "50% advance to start, 50% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
        "lukaoriginals.com is used only as a style / layout reference; this is a custom build and not a copy of that site.",
        "Domain and hosting are NOT included; they are arranged and paid for by the client directly. We will help set them up and connect them.",
        "This package covers up to {} product listings; additional products are added at a small per-product charge.".format(MAX_PRODUCTS),
        "The payment gateway account (and its transaction fees) and any SMS / email / OTP service are arranged and paid for by the client directly.",
        "Product photos and content are provided by the client.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
