"""
Bhama Vision - starter e-commerce website (payment integration) quotation.

A clean, affordable starter online store with payment gateway integration,
cart & checkout and a basic admin panel to manage products and orders.
Domain and hosting are arranged by the client (not included).

Reuses the Bhama Vision quotation renderer:

    python3 build_starter_ecommerce_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Scope cap - repeated in the included list, the bullets and the terms so
# the fixed price is unambiguous. Adjust if the client needs more.
MAX_PRODUCTS = 10

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
    "note": "Starter e-commerce website with payment gateway integration",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Clean, responsive starter online store",
        "Payment gateway integration + Cash on Delivery",
        "Cart & secure checkout",
        "Basic admin panel to manage products & orders",
        "Up to {} products set up for you".format(MAX_PRODUCTS),
        "Product detail pages with images, price & description",
        "WhatsApp click-to-chat & enquiry / contact form",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not included)",
        "Hosting - arranged and paid by the client (not included)",
        "Payment gateway account & its transaction fees",
        "SMS / email / OTP service subscription",
        "Product photos & content (provided by the client)",
        "Coupons, customer accounts, multi-vendor & mobile app (add-ons)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-049",
        "package": "Starter Store + Admin",
        "title": "Starter E-Commerce Website",
        "subtitle": "Affordable online store with payment gateway integration & a basic admin panel (domain & hosting not included)",
        "price": 5000,
        "price_note": "one-time (design & development)",
        "timeline": "8-12 working days",
        "summary": (
            "A clean, affordable way to start selling online. Customers "
            "browse your products, add them to the cart and check out "
            "securely with an integrated payment gateway or Cash on Delivery. "
            "We set up up to {} products for you, and a basic admin panel "
            "lets you add or edit products and view orders. The store is "
            "fully responsive with WhatsApp click-to-chat so buyers can reach "
            "you easily. The focus of this package is getting you online with "
            "working payments quickly and affordably. Domain and hosting are "
            "arranged by you (not included), and we will help set them "
            "up.".format(MAX_PRODUCTS)
        ),
        "sections": [
            {
                "heading": "Customer-facing store (frontend)",
                "items": [
                    "Clean, responsive design - home with featured products "
                    "& simple navigation",
                    "Product listing with basic search & categories",
                    "Product detail page - images, price, description & "
                    "'add to cart'",
                    "Cart and a smooth, secure checkout",
                    "Payment gateway (UPI / cards / net-banking / wallets) + "
                    "Cash on Delivery",
                    "WhatsApp click-to-chat and an enquiry / contact form",
                    "About, contact and policy pages",
                ],
            },
            {
                "heading": "Payment gateway integration",
                "items": [
                    "Integration of a leading Indian payment gateway "
                    "(Razorpay / PayU / Cashfree or similar)",
                    "Accept UPI, credit / debit cards, net-banking & wallets",
                    "Secure checkout with order confirmation to you & the "
                    "customer",
                    "Cash on Delivery as an additional option",
                ],
            },
            {
                "heading": "Products & basic admin panel",
                "items": [
                    "Up to {} products set up for you at launch with images, "
                    "price & description".format(MAX_PRODUCTS),
                    "Basic admin login to add / edit / remove products",
                    "View orders with customer & payment details",
                    "Update order status (e.g. confirmed / shipped / "
                    "delivered)",
                    "Easily add more products yourself later",
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
        "Domain and hosting are NOT included; they are arranged and paid for by the client directly. We will help set them up and connect them.",
        "The payment gateway account (and its transaction fees) and any SMS / OTP subscription are arranged and paid for by the client directly.",
        "This starter package includes setting up up to {} products; additional products can be added by the client via the admin panel.".format(MAX_PRODUCTS),
        "Product photos and content are provided by the client.",
        "Coupons, customer accounts / login, wishlist, multi-vendor features and a mobile app are available as add-ons and quoted separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
