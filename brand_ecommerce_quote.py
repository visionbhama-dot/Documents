"""
Bhama Vision - brand e-commerce website quotation content.

A polished, conversion-focused single-brand online store in the style of
wavex.in - sale pricing with strike-through MRP and savings badges, unit
pricing, customer reviews, a strong brand home page - with up to 30
product listings, a full admin panel, cart, checkout and payment gateway,
and SEO-friendly build. Includes one year of free hosting and the Bhama
Vision 1-year bug & error support. The domain is arranged by the client
(not on our side). Reuses the Bhama Vision quotation renderer:

    python3 build_brand_ecommerce_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Product listings covered by this package. Repeated in the included list,
# the bullets and the terms so the fixed price is unambiguous.
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
    "note": "Brand e-commerce store (wavex.in style) with admin panel",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Polished, responsive single-brand online store",
        "Up to {} product listings set up with photos & details".format(
            MAX_PRODUCTS),
        "Sale pricing - MRP strike-through, sale price & savings % badge",
        "Cart, checkout, order placement & order tracking",
        "Payment gateway integration (UPI / cards / net banking) + COD",
        "Customer reviews & ratings on products",
        "Full admin panel to manage products, orders & customers",
        "SEO-friendly build (titles, meta, clean URLs, sitemap)",
        "1 year free hosting",
        "1 year of Bhama Vision bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Payment gateway account & its transaction fees",
        "Product photos, copy & price list (provided by the client)",
        "Products beyond {} (added at a small per-product charge)".format(
            MAX_PRODUCTS),
        "SMS / email / OTP sending service subscription",
        "Product photography, ad creatives & content writing",
        "SEO campaigns & paid ads management (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-066",
        "package": "Brand Store + Admin Panel",
        "title": "Brand E-Commerce Website",
        "subtitle": "Conversion-focused online store (wavex.in style) with admin panel",
        "price": 9000,
        "price_note": "one-time (design & development)",
        "timeline": "15-20 working days",
        "summary": (
            "A polished, conversion-focused online store for your brand, "
            "built in the style of sites like wavex.in. Your products are "
            "presented the way shoppers expect from a modern D2C brand - a "
            "strong home page with hero banners and best-sellers, clean "
            "product cards showing the MRP struck through, the sale price "
            "and a 'Save X%' badge, unit pricing, and genuine customer "
            "reviews and ratings that build trust. Shoppers add to cart and "
            "check out paying securely by UPI, card or net banking, or with "
            "Cash on Delivery, and can track their order. Up to "
            + str(MAX_PRODUCTS) + " products are set up for you. Running it "
            "all is a full admin panel for products, prices and offers, "
            "orders with their payment status, customers and reviews. The "
            "site is built SEO-friendly so it can be found on Google, and "
            "comes with one year of free hosting plus one year of our bug & "
            "error support. The domain is arranged by you (it is not on our "
            "side), and we will help connect it to the store."
        ),
        "sections": [
            {
                "heading": "Storefront (customer-facing)",
                "items": [
                    "Brand home page with hero banners, best-sellers, "
                    "featured collections & call-to-action",
                    "Product listing by collection / category with search, "
                    "sort and filters",
                    "Product cards showing MRP strike-through, sale price and "
                    "a 'Save X%' discount badge",
                    "Product detail page with image gallery, variants, unit "
                    "price, description and specifications",
                    "Customer reviews & star ratings on each product",
                    "Add to cart, quantity stepper and a smooth checkout",
                    "Coupon / discount code entry at checkout",
                    "Order confirmation and order tracking for the customer",
                    "Content pages: about, contact and policy pages "
                    "(shipping, returns, privacy)",
                    "Fully responsive - built mobile-first for phone shoppers",
                ],
            },
            {
                "heading": "Payments & checkout",
                "items": [
                    "Payment gateway integration (Razorpay / PayU / "
                    "Instamojo - your choice)",
                    "Accept UPI, debit & credit cards, net banking and "
                    "wallets",
                    "Cash on Delivery option you can switch on or off",
                    "Secure, PCI-compliant hosted checkout - card details "
                    "never touch your website",
                    "Automatic payment success / failure handling with the "
                    "order status updated accordingly",
                    "Order confirmation on screen and by email",
                ],
            },
            {
                "heading": "Admin panel",
                "items": [
                    "Secure admin login with a dashboard of orders, sales & "
                    "low-stock items",
                    "Products - add, edit, remove; set MRP, sale price, "
                    "variants, stock, photos and status",
                    "Collections / categories - create, rename and reorder",
                    "Order management - view every order, its items and "
                    "payment status; update status through to delivered",
                    "Customers list with order history",
                    "Reviews & ratings moderation (approve / hide)",
                    "Coupons & offers - percentage or flat discount, minimum "
                    "order, validity and usage limits",
                    "Homepage banner & featured-product management",
                    "Basic sales reports, exportable to Excel",
                    "A guided walkthrough and handover so your team can run "
                    "the store confidently",
                ],
            },
            {
                "heading": "SEO, design & delivery",
                "items": [
                    "SEO-friendly build - page titles, meta descriptions, "
                    "clean URLs, headings, image alt text & auto XML sitemap",
                    "Fast-loading, mobile-first storefront",
                    "Product & organisation structured data so listings can "
                    "show rich results on Google",
                    "Brand-matched design using your colours, logo & fonts",
                    "WhatsApp click-to-chat button for quick enquiries",
                    "Testing across major browsers and devices before launch",
                    "1 year free hosting, with help connecting your domain",
                    "1 year of Bhama Vision support for bugs & errors after "
                    "launch",
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
        "Hosting is free for the first year; renewal from the second year (or an upgrade for higher traffic) is optional and charged separately.",
        "This package covers up to {} product listings; additional products are added at a small per-product charge.".format(
            MAX_PRODUCTS),
        "The payment gateway account is opened in the client's name with the client's KYC; its transaction fees are charged by the gateway and are not part of this quote.",
        "Product photos, copy, price list and any review content are provided by the client.",
        "Any SMS / email / OTP sending service subscription is arranged and paid for by the client.",
        "Timelines begin once the content, product list and advance payment are received.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new features or redesigns.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
