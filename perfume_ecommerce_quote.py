"""
Bhama Vision - perfume brand e-commerce website quotation content.

A polished single-seller perfume online store with a full admin panel,
payment gateway and support for up to 50 product listings. Reuses the
Bhama Vision quotation renderer:

    python3 build_perfume_ecommerce_quote.py

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
    "note": "Perfume brand e-commerce website with admin panel",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Premium, responsive perfume online store",
        "Full admin panel to manage the whole store",
        "Up to 50 product listings set up for you",
        "Payment gateway integration + Cash on Delivery",
        "Customer accounts, cart, wishlist & checkout",
        "Coupons, offers & banner management",
        "WhatsApp integration (click-to-chat)",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Payment gateway account & its transaction fees",
        "SMS / email / OTP service subscription",
        "Product photos & content (provided by the client)",
        "Multi-vendor / marketplace features & mobile app",
        "Ongoing marketing / SEO and any paid plugin or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-016",
        "package": "Perfume Store + Admin",
        "title": "Perfume Brand E-Commerce Website",
        "subtitle": "Full online store + admin panel, with payment gateway & 50 listings",
        "price": 18000,
        "price_note": "one-time (design & development)",
        "timeline": "18-25 working days",
        "summary": (
            "A premium, ready-to-sell online store for your perfume brand, "
            "with a complete admin panel to run it. Customers can browse "
            "fragrances by category, search and filter, add to cart or "
            "wishlist, create an account and check out with online payment or "
            "Cash on Delivery. We set up your first 50 product listings for "
            "you. From the admin panel you control products, orders, "
            "customers, coupons and banners. The store is built responsive "
            "with a payment gateway and WhatsApp integration so buyers can "
            "reach you instantly."
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
                    "Up to 50 perfume products set up for you at launch",
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
                "heading": "Payment gateway",
                "items": [
                    "Integration of a leading Indian payment gateway "
                    "(Razorpay / PayU / Cashfree or similar)",
                    "Accept UPI, credit / debit cards, net-banking & wallets",
                    "Secure checkout with order confirmation",
                    "Cash on Delivery as an additional option",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

# Terms shown on the closing page of the quotation.
TERMS = {
    "validity_days": 15,
    "payment": "40% advance to start, 30% at midway, 30% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
        "Domain, hosting, the payment gateway account (and its fees) and any SMS/OTP subscription are arranged and paid for by the client directly.",
        "This package includes setting up up to 50 product listings; additional listings can be added by the client via the admin panel.",
        "Product photos and content are provided by the client.",
        "This is a single-seller store; multi-vendor / marketplace features and a mobile app are separate.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
