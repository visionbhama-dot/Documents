"""
Bhama Vision - e-commerce website quotation content (3 products).

A single-seller online store with up to 3 products, a payment gateway,
full social-media integration and a backend admin panel. Includes Google
Analytics 4 and Google Search Console setup, free hosting and 1 year of
bug & error support. The domain is arranged by the client (not on our
side). Reuses the Bhama Vision quotation renderer:

    python3 build_ecommerce_3products_quote.py

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
    "note": "E-commerce website (3 products) with payment gateway & backend",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive online store (frontend) + backend admin panel",
        "Up to 3 products set up with photos, price & details",
        "Cart, checkout and order placement",
        "Payment gateway integration (UPI / cards / net banking)",
        "Social media integration across all your channels",
        "Google Analytics 4 setup with e-commerce tracking",
        "Google Search Console setup with sitemap submission",
        "Hosting - free plan; 1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Payment gateway account & its transaction fees",
        "Product photos & content (provided by the client)",
        "Products beyond 3 (added at a small per-product charge)",
        "SMS / email / OTP sending service subscription",
        "Social media content creation & post scheduling",
        "SEO campaigns & paid ads (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-029",
        "package": "Online Store + Backend",
        "title": "E-Commerce Website",
        "subtitle": "Online store with payment gateway, social media & analytics",
        "price": 7000,
        "price_note": "one-time (design & development)",
        "timeline": "12-16 working days",
        "summary": (
            "A complete, ready-to-launch online store for a single seller "
            "with up to 3 products set up for you. Customers browse your "
            "products, add them to the cart and pay securely through an "
            "integrated payment gateway using UPI, cards or net banking. All "
            "your social media channels are connected to the store, so "
            "visitors can follow and share your products, and your posts "
            "help bring traffic back to the site. A backend admin panel lets "
            "you manage products, prices, photos and orders yourself. We also "
            "set up Google Analytics 4 and Google Search Console so you can "
            "see exactly how many people visit, what they buy and how your "
            "store performs on Google search. It comes with a free hosting "
            "plan and 1 year of bug & error support. The domain is arranged "
            "by you (it is not on our side), and we will help connect it to "
            "the store."
        ),
        "sections": [
            {
                "heading": "Customer-facing store",
                "items": [
                    "Home page with banners, featured products & categories",
                    "Product listing with categories, search & sort",
                    "Product detail page with image gallery, variants & price",
                    "Up to 3 products set up with photos, price and details",
                    "Add to cart and a smooth, simple checkout",
                    "Order placement with on-screen and email confirmation",
                    "Content pages: about, contact and policy pages "
                    "(shipping, returns, privacy)",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Payments & checkout",
                "items": [
                    "Payment gateway integration (Razorpay / PayU / "
                    "Instamojo - your choice)",
                    "Accept UPI, debit & credit cards, net banking and "
                    "wallets",
                    "Secure, PCI-compliant hosted checkout - card details "
                    "never touch your website",
                    "Automatic payment success / failure handling with order "
                    "status update",
                    "Cash on Delivery option that you can switch on or off",
                    "Order confirmation email to the customer and to you",
                ],
            },
            {
                "heading": "Social media integration",
                "items": [
                    "Profile links for all your channels - Instagram, "
                    "Facebook, WhatsApp, YouTube, X, LinkedIn & Pinterest - "
                    "in the header and footer",
                    "WhatsApp click-to-chat button for instant enquiries",
                    "Instagram feed section on the home page that updates "
                    "automatically",
                    "Share buttons on every product (WhatsApp, Instagram, "
                    "Facebook, X & copy link)",
                    "Link previews set up so your products look right when "
                    "shared (Open Graph & Twitter cards)",
                    "Facebook / Instagram page and catalogue linked to the "
                    "store",
                ],
            },
            {
                "heading": "Analytics & Search Console",
                "items": [
                    "Google Analytics 4 property created and installed on "
                    "every page",
                    "E-commerce tracking - product views, add-to-cart, "
                    "checkout and completed purchases",
                    "Traffic source reporting so you can see which social "
                    "channel brings buyers",
                    "Google Search Console set up and site ownership verified",
                    "XML sitemap generated and submitted for indexing",
                    "Page titles, meta descriptions & clean URLs for all "
                    "pages (on-page SEO basics)",
                    "A walkthrough of both dashboards so you can read your "
                    "own numbers",
                ],
            },
            {
                "heading": "Backend admin panel",
                "items": [
                    "Secure admin login for the store owner",
                    "Add, edit and remove products, categories & variants",
                    "Upload product photos and set price, stock and status",
                    "Order management - view orders and update status "
                    "(new / paid / shipped / delivered)",
                    "Payment status visible against each order",
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
        "This package covers up to 3 products; additional products are added at a small per-product charge.",
        "The payment gateway account is opened in the client's name with the client's KYC; its transaction fees are charged by the gateway and are not part of this quote.",
        "Social media integration connects your existing accounts to the store; creating accounts, content or posts is not included.",
        "Google Analytics 4 and Search Console are set up and verified on your Google account; ongoing SEO work and paid ads are a separate service.",
        "Any SMS / email / OTP sending service subscription is arranged and paid for by the client.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new products/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
