"""
Bhama Vision - perfume brand e-commerce website quotation content (35 listings).

A polished single-seller perfume online store with a full admin panel and
payment gateway integration, with up to 35 product listings set up at
launch. Hosting for 1 year is included from our side; the domain is
arranged by the client (not included).

Reuses the Bhama Vision quotation renderer:

    python3 build_perfume_ecommerce_35_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Scope cap - repeated in the included list, the bullets and the terms so
# the fixed price is unambiguous. Adjust if the client needs more.
MAX_PRODUCTS = 35

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
    "note": "Perfume e-commerce website with admin panel, payment gateway & hosting",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Premium, responsive perfume online store",
        "Full admin panel to manage the whole store",
        "Payment gateway integration + Cash on Delivery",
        "Up to {} product listings set up for you".format(MAX_PRODUCTS),
        "Hosting for 1 year (from our side)",
        "Customer accounts, cart, wishlist & checkout",
        "Coupons, offers, banners & WhatsApp click-to-chat",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not included)",
        "Hosting renewal from year 2 onwards",
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
        "id": "BV-Q-2026-042",
        "package": "Perfume Store + Admin",
        "title": "Perfume Brand E-Commerce Website",
        "subtitle": "Full online store + admin panel, with payment gateway, {} listings & 1 year hosting (domain not included)".format(MAX_PRODUCTS),
        "price": 12000,
        "price_note": "one-time (incl. hosting for 1 year)",
        "timeline": "15-22 working days",
        "summary": (
            "A premium, ready-to-sell online store for your perfume brand, "
            "with a complete admin panel to run it. Customers browse "
            "fragrances by category, search and filter, add to cart or "
            "wishlist, create an account and check out with online payment or "
            "Cash on Delivery. We set up your first {} product listings for "
            "you. From the admin panel you control products, orders, "
            "customers, coupons and banners. The store is built responsive "
            "with payment gateway integration and WhatsApp click-to-chat so "
            "buyers can reach you instantly. Hosting for the first year is "
            "included from our side; the domain is arranged by you (not "
            "included), and we will help connect it.".format(MAX_PRODUCTS)
        ),
        "sections": [
            {
                "heading": "Customer-facing store (frontend)",
                "items": [
                    "Premium, responsive design - home with banners, featured "
                    "fragrances & categories",
                    "Product listing with search, filters and sort (by scent, "
                    "size, price)",
                    "Product detail page - image gallery, variants "
                    "(size / ml), stock & related products",
                    "Cart, wishlist and a smooth, secure checkout",
                    "Customer accounts with sign up / login + OTP, order "
                    "history & tracking",
                    "Multiple payments: UPI, cards, net-banking, wallets & "
                    "Cash on Delivery",
                    "Coupons / discount codes at checkout",
                    "WhatsApp integration and content pages (about, contact, "
                    "policies)",
                ],
            },
            {
                "heading": "Product listings",
                "items": [
                    "Up to {} perfume products set up for you at "
                    "launch".format(MAX_PRODUCTS),
                    "Each listing with images, description, price, variants "
                    "& stock",
                    "Organised into categories / collections (e.g. men, "
                    "women, unisex, gift sets)",
                    "Easily add more products yourself from the admin panel",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Dashboard with sales, orders & top products at a glance",
                    "Manage products, categories & variants (add / edit / "
                    "delete), with bulk upload",
                    "Inventory / stock management with low-stock view",
                    "Order management - view, update status, invoices & "
                    "mark delivered",
                    "Customer management and enquiries",
                    "Coupons, offers & homepage banner management",
                    "Sales & order reports",
                ],
            },
            {
                "heading": "Payment gateway & hosting",
                "items": [
                    "Integration of a leading Indian payment gateway "
                    "(Razorpay / PayU / Cashfree or similar)",
                    "Accept UPI, credit / debit cards, net-banking & wallets",
                    "Secure checkout with order confirmation",
                    "Cash on Delivery as an additional option",
                    "Hosting for 1 year included from our side, with SSL "
                    "(https)",
                    "Deployment, go-live and help connecting your domain",
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
        "Hosting for the first year is included from our side (with SSL). Renewal from year 2 onwards is billed separately at actuals.",
        "The domain is NOT included - it is arranged and paid for by the client directly; we will help connect it to the store.",
        "The payment gateway account (and its transaction fees) and any SMS / OTP subscription are arranged and paid for by the client directly.",
        "This package includes setting up up to {} product listings; additional listings can be added by the client via the admin panel.".format(MAX_PRODUCTS),
        "Product photos and content are provided by the client.",
        "This is a single-seller store; multi-vendor / marketplace features and a mobile app are separate.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
