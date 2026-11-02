"""
Bhama Vision - e-commerce website (30 products) quotation content.

A single-seller online store with up to 30 product listings, payment gateway
integration, cart & checkout and a backend admin panel to manage products,
orders and customers. Includes hosting. The domain is arranged by the client
(not included). Reuses the Bhama Vision quotation renderer:

    python3 build_ecommerce_30products_quote.py

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
    "note": "E-commerce website (30 products) with payment integration, admin panel & hosting",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive online store (frontend) + backend admin panel",
        "Up to {} product listings set up with photos, price & details".format(MAX_PRODUCTS),
        "Payment gateway integration (UPI / cards / net-banking / wallets)",
        "Cart, secure checkout & Cash on Delivery",
        "Backend to manage products, orders & customers",
        "WhatsApp integration (click-to-chat button)",
        "Hosting - included",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not included)",
        "Payment gateway account & its transaction fees",
        "Product photos & content (provided by the client)",
        "Products beyond {} (added at a small per-product charge)".format(MAX_PRODUCTS),
        "SMS / email / OTP sending service subscription",
        "SEO / marketing (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-052",
        "package": "Online Store + Admin + Hosting",
        "title": "E-Commerce Website (30 Products)",
        "subtitle": "Online store with payment integration, backend admin panel & hosting (domain not included)",
        "price": 6000,
        "price_note": "one-time (design & development)",
        "timeline": "12-16 working days",
        "summary": (
            "A complete, ready-to-launch online store for a single seller "
            "with up to {} product listings and a backend admin panel to run "
            "it. Customers browse products, add them to the cart and check "
            "out securely with an integrated payment gateway (UPI / cards / "
            "net-banking / wallets) or Cash on Delivery, while you manage "
            "products, orders and customers from one dashboard. It comes with "
            "a WhatsApp chat button and hosting is included. The domain is "
            "arranged by you (not included), and we will help connect it to "
            "the store.".format(MAX_PRODUCTS)
        ),
        "sections": [
            {
                "heading": "Customer-facing store (frontend)",
                "items": [
                    "Home page with banners, featured products & categories",
                    "Product listing with categories, search & sort",
                    "Product detail page with image gallery, variants & price",
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
            {
                "heading": "Design, hosting & delivery",
                "items": [
                    "Modern design matched to your brand colours and logo",
                    "Basic on-page SEO - titles, meta descriptions & clean "
                    "URLs",
                    "Fast-loading, mobile-first build",
                    "Testing across major browsers and devices before launch",
                    "Hosting included; deployment and help connecting your "
                    "domain",
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
        "The domain is NOT included; it is arranged and paid for by the client directly. We will help connect it to the store.",
        "Hosting is included. Renewal / upgrading to higher plans (for higher traffic or needs) after the first term is optional and charged separately.",
        "This package covers up to {} product listings; additional products are added at a small per-product charge.".format(MAX_PRODUCTS),
        "The payment gateway account (and its transaction fees) and any SMS / email / OTP service are arranged and paid for by the client directly.",
        "Product photos and content are provided by the client.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
