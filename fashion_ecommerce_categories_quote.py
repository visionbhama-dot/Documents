"""
Bhama Vision - fashion e-commerce website (multiple categories) quotation.

A modern fashion online store with a full admin panel, multiple product
categories, cart & checkout and payment gateway integration. Domain and
hosting are arranged by the client (not included).

Reuses the Bhama Vision quotation renderer:

    python3 build_fashion_ecommerce_categories_quote.py

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
    "note": "Fashion e-commerce website with admin panel & multiple categories",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Modern, responsive fashion online store",
        "Full admin panel to manage the whole store",
        "Multiple product categories & collections",
        "Payment gateway integration + Cash on Delivery",
        "Up to {} products set up across your categories".format(MAX_PRODUCTS),
        "Cart, wishlist, customer accounts & checkout",
        "Coupons, offers, banners & WhatsApp click-to-chat",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not included)",
        "Hosting - arranged and paid by the client (not included)",
        "Payment gateway account & its transaction fees",
        "SMS / email / OTP service subscription",
        "Product photos & content (provided by the client)",
        "Multi-vendor / marketplace features, mobile app & paid plugins",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-048",
        "package": "Fashion Store + Admin",
        "title": "Fashion E-Commerce Website",
        "subtitle": "Full online fashion store + admin panel with multiple categories & payment gateway (domain & hosting not included)",
        "price": 12000,
        "price_note": "one-time (design & development)",
        "timeline": "16-22 working days",
        "summary": (
            "A modern, ready-to-sell online store for your fashion brand, "
            "with a complete admin panel to run it. Your products are "
            "organised into multiple categories and collections so customers "
            "can browse quickly - pick size and colour, add to cart or "
            "wishlist, create an account and check out with online payment or "
            "Cash on Delivery. We set up up to {} products across your "
            "categories. From the admin panel you control categories, "
            "products, sizes / variants, orders, customers, coupons and "
            "banners. The store is built responsive with payment gateway "
            "integration and WhatsApp click-to-chat. Domain and hosting are "
            "arranged by you (not included), and we will help set them "
            "up.".format(MAX_PRODUCTS)
        ),
        "sections": [
            {
                "heading": "Customer-facing store (frontend)",
                "items": [
                    "Modern, responsive design - home with banners, featured "
                    "products & category highlights",
                    "Multiple categories & collections (e.g. men, women, "
                    "kids, ethnic, western, footwear, accessories)",
                    "Product listing with search, filters & sort (category, "
                    "size, colour, price)",
                    "Product detail page - image gallery, size & colour "
                    "variants, stock & related products",
                    "Cart, wishlist and a smooth, secure checkout",
                    "Customer accounts with sign up / login + OTP, order "
                    "history & tracking",
                    "Multiple payments: UPI, cards, net-banking, wallets & "
                    "Cash on Delivery",
                    "Coupons / discount codes + content pages (about, "
                    "contact, policies)",
                ],
            },
            {
                "heading": "Categories & product listings",
                "items": [
                    "Products organised into multiple categories & "
                    "sub-collections for quick browsing",
                    "Up to {} products set up for you at launch across your "
                    "categories".format(MAX_PRODUCTS),
                    "Each listing with images, description, price, size & "
                    "colour variants and stock",
                    "Featured / new-arrival products highlighted on the home "
                    "page",
                    "Easily add more categories & products yourself from the "
                    "admin panel",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Dashboard with sales, orders & top products at a glance",
                    "Manage categories, products, sizes & variants (add / "
                    "edit / delete), with bulk upload",
                    "Inventory / stock management with low-stock view",
                    "Order management - view, update status, invoices & "
                    "mark delivered",
                    "Customer management and enquiries",
                    "Coupons, offers & homepage banner management",
                    "Sales & order reports",
                ],
            },
            {
                "heading": "Payment gateway",
                "items": [
                    "Integration of a leading Indian payment gateway "
                    "(Razorpay / PayU / Cashfree or similar)",
                    "Accept UPI, credit / debit cards, net-banking & wallets",
                    "Secure checkout with order confirmation",
                    "Cash on Delivery as an additional option",
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
        "Domain and hosting are NOT included; they are arranged and paid for by the client directly. We will help set them up and connect them.",
        "The payment gateway account (and its transaction fees) and any SMS / OTP subscription are arranged and paid for by the client directly.",
        "This package includes setting up multiple categories and up to {} products; additional categories and products can be added by the client via the admin panel.".format(MAX_PRODUCTS),
        "Product photos and content are provided by the client.",
        "This is a single-seller store; multi-vendor / marketplace features and a mobile app are separate.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
