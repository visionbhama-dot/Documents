"""
Bhama Vision - e-commerce website quotation content.

A single-vendor (one seller / one store) e-commerce website with a full
admin panel. Reuses the Bhama Vision quotation renderer:

    python3 build_ecommerce_quote.py

Edit prices, features, client or terms below, then re-run.
"""

# ---------------------------------------------------------------------------
# Company details (shown on the header + footers). Update with your real info.
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
    "note": "E-commerce website with admin panel",
}

# Requirements box shown on the quotation. Two columns:
#   left  (highlighted) = what Bhama Vision builds & delivers
#   right (muted)       = third-party subscriptions arranged by the client
REQUIREMENTS = {
    "title": "Scope & requirements",
    "left_label": "Delivered by Bhama Vision",
    "right_label": "On client's side (third-party)",
    "covered": [
        "Complete UI/UX design & development of the store + admin panel",
        "Setup of database, products, categories and all data models",
        "Integration of the third-party services listed alongside",
        "Deployment to the client's hosting + handover",
        "Testing and bug fixing before launch",
    ],
    "not_covered": [
        "Domain and web hosting / server",
        "Payment gateway account and its transaction fees",
        "SMS / email / OTP sending service subscription",
        "Product photos & content (provided by the client)",
        "Any other paid API or plugin",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-003",
        "package": "Website + Admin",
        "title": "E-Commerce Website",
        "subtitle": "Online store frontend + full admin panel (single seller)",
        "price": 7000,
        "price_note": "one-time (design & development)",
        "timeline": "12-18 working days",
        "summary": (
            "A complete online store for a single seller, with a customer-"
            "facing website and a full admin panel to run it. Customers can "
            "browse products, add to cart and place orders with online payment "
            "or Cash on Delivery, while you manage products, orders, customers "
            "and offers from one dashboard. Fully responsive across mobile, "
            "tablet and desktop."
        ),
        "sections": [
            {
                "heading": "Customer-facing store",
                "items": [
                    "Home page with banners, featured products & categories",
                    "Product listing with categories, search, filters & sort",
                    "Product detail page with image gallery, variants & price",
                    "Add to cart, wishlist and smooth checkout",
                    "Customer sign up & login with email / mobile + OTP",
                    "Multiple payments: UPI, cards, net-banking & Cash on Delivery",
                    "Order placement, order history & basic tracking status",
                    "Coupons / discount codes at checkout",
                    "Content pages: about, contact, and policy pages",
                    "Fully responsive & SEO-friendly across all devices",
                ],
            },
            {
                "heading": "Admin panel",
                "items": [
                    "Dashboard with sales, orders & top products at a glance",
                    "Add / edit / delete products, categories & variants",
                    "Stock / inventory management with low-stock view",
                    "Order management: view, update status & mark delivered",
                    "Customer management and basic enquiries",
                    "Coupons, offers & homepage banner management",
                    "Basic sales & order reports",
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
        "All third-party subscriptions (hosting, domain, payment gateway, email/OTP/SMS) are arranged and paid for by the client directly.",
        "Timelines begin once content, product details, access and the advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
