"""
Bhama Vision - starter e-commerce website quotation content (10 products).

A single-seller online store with up to 10 products and a backend admin
panel to manage products, orders and customers. Customers can browse, add
to cart and order with online payment or Cash on Delivery. Includes free
hosting and 1 year of bug & error support. The domain is arranged by the
client (not on our side). Reuses the Bhama Vision quotation renderer:

    python3 build_ecommerce_10products_quote.py

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
    "note": "Starter e-commerce website (10 products) with backend",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive online store (frontend) + backend admin panel",
        "Up to 10 products set up with photos, price & details",
        "Cart, checkout and order placement",
        "Online payment (UPI / cards) + Cash on Delivery",
        "Backend to manage products, orders & customers",
        "WhatsApp integration (click-to-chat button)",
        "Hosting - free plan",
        "1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Payment gateway account & its transaction fees",
        "Product photos & content (provided by the client)",
        "Products beyond 10 (added at a small per-product charge)",
        "SMS / email / OTP sending service subscription",
        "SEO / marketing (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-025",
        "package": "Starter Store + Backend",
        "title": "E-Commerce Website (10 Products)",
        "subtitle": "Single-seller online store with backend admin panel",
        "price": 9000,
        "price_note": "one-time (design & development)",
        "timeline": "12-16 working days",
        "summary": (
            "A complete, ready-to-launch online store for a single seller "
            "with up to 10 products and a backend admin panel to run it. "
            "Customers can browse products, add to cart and place orders with "
            "online payment or Cash on Delivery, while you manage products, "
            "orders and customers from one dashboard. It comes with a WhatsApp "
            "chat button, a free hosting plan and 1 year of bug & error "
            "support. The domain is arranged by you (it is not on our side), "
            "and we will help connect it to the store."
        ),
        "sections": [
            {
                "heading": "Customer-facing store",
                "items": [
                    "Home page with banners, featured products & categories",
                    "Product listing with categories, search & sort",
                    "Product detail page with image gallery, variants & price",
                    "Up to 10 products set up with photos, price and details",
                    "Add to cart and smooth, simple checkout",
                    "Online payment (UPI / cards) + Cash on Delivery",
                    "Order placement with order confirmation",
                    "WhatsApp click-to-chat button for quick enquiries",
                    "Content pages: about, contact and policy pages",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Backend admin panel",
                "items": [
                    "Secure admin login for the store owner",
                    "Add, edit and remove products, categories & variants",
                    "Upload product photos and set price, stock and status",
                    "Order management - view orders and update status "
                    "(new / shipped / delivered)",
                    "Basic customer list and enquiries",
                    "Homepage banner management",
                    "A short walkthrough so you are comfortable running the "
                    "store",
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
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it to the store.",
        "This package covers up to 10 products; additional products are added at a small per-product charge.",
        "The payment gateway account and its transaction fees, and any SMS / email / OTP service, are arranged and paid for by the client.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new products/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
