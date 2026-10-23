"""
Bhama Vision - Chatrabhuj Traders online grocery store quotation content.

A complete online grocery store with a full admin panel and payment
gateway integration. Covers grocery-specific needs: category and
sub-category browsing, weight / pack variants, stock control, delivery
area and slot selection, minimum order value, coupons, customer accounts
with repeat ordering and WhatsApp order updates. Comes with free hosting
and 1 year of bug & error support. The domain is arranged by the client
(not on our side). Reuses the Bhama Vision quotation renderer:

    python3 build_chatrabhuj_grocery_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Initial data-entry allowance. There is no limit on how many products the
# client can add themselves from the admin panel; this is the number we set
# up at launch on their behalf.
INITIAL_PRODUCTS = 100

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
    "name": "Chatrabhuj Traders",
    "company": "Chatrabhuj Traders",
    "note": "Online grocery store with admin panel & payment gateway",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive online grocery store + full admin panel",
        "Unlimited products & categories you can add from the admin panel",
        "{} products set up by us at launch + bulk Excel / CSV import".format(
            INITIAL_PRODUCTS),
        "Weight / pack variants (500g, 1kg, 5kg) with per-variant pricing",
        "Cart, checkout, order placement & order tracking",
        "Payment gateway integration (UPI / cards / net banking) + COD",
        "Delivery area (pincode) check, delivery slots & minimum order value",
        "Coupons & discounts, customer accounts with repeat ordering",
        "WhatsApp integration for enquiries & order updates",
        "Hosting - free plan; 1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Payment gateway account & its transaction fees",
        "Product photos, names & price list (provided by the client)",
        "SMS / email / OTP sending service subscription",
        "Courier / delivery-partner API integration - separate scope",
        "Delivery staff mobile app - separate scope",
        "Tally / accounting or POS-billing software integration",
        "Customer mobile app (Android / iOS) - separate scope",
        "SEO campaigns & paid ads (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-034",
        "package": "Grocery Store + Admin Panel",
        "title": "Chatrabhuj Traders Online Store",
        "subtitle": "Online grocery store with full admin panel & payment gateway",
        "price": 9000,
        "price_note": "one-time (design & development)",
        "timeline": "15-20 working days",
        "summary": (
            "A complete online grocery store for Chatrabhuj Traders, built "
            "for the way grocery actually sells. Customers browse by "
            "category and sub-category - fruits & vegetables, dairy, "
            "staples, snacks, beverages, household and personal care - pick "
            "the pack size they want (500g, 1kg, 5kg and so on, each with "
            "its own price), add items to the cart and check out paying "
            "securely by UPI, card or net banking, or with Cash on Delivery. "
            "The store checks whether you deliver to their pincode, lets "
            "them choose a delivery slot, and applies your minimum order "
            "value and coupon codes. Customers can create an account, see "
            "their order history and reorder their usual basket in one tap, "
            "and they get order updates on WhatsApp. Running it all is a "
            "full admin panel: products, categories, stock, prices and "
            "offers, every order with its payment status, customers, "
            "delivery areas and slots, banners and sales reports. We set up "
            "the first " + str(INITIAL_PRODUCTS) + " products for you and "
            "give you a bulk Excel / CSV import so a large price list is "
            "quick to load. It comes with a free hosting plan and 1 year of "
            "bug & error support. The domain is arranged by you (it is not "
            "on our side), and we will help connect it to the store."
        ),
        "sections": [
            {
                "heading": "Customer-facing store",
                "items": [
                    "Home page with banners, offers, featured items & "
                    "shop-by-category tiles",
                    "Categories and sub-categories - fruits & vegetables, "
                    "dairy, staples & grains, snacks, beverages, household, "
                    "personal care and more",
                    "Product listing with search, sort and filters "
                    "(category, brand, price)",
                    "Product detail page with image gallery, weight / pack "
                    "variants, price, MRP and savings",
                    "Weight & pack variants (500g, 1kg, 5kg, pieces, litres) "
                    "each with its own price and stock",
                    "Out-of-stock items clearly marked so customers aren't "
                    "disappointed at checkout",
                    "Add to cart with quantity stepper and a live cart total",
                    "Delivery pincode check so customers know up front "
                    "whether you deliver to them",
                    "Coupon / promo code entry at checkout",
                    "Customer accounts - signup & login, saved addresses, "
                    "order history and one-tap reorder",
                    "Content pages: about, contact and policy pages "
                    "(delivery, returns, privacy)",
                    "Fully responsive - built mobile-first, since most "
                    "grocery orders come from phones",
                ],
            },
            {
                "heading": "Payments & checkout",
                "items": [
                    "Payment gateway integration (Razorpay / PayU / "
                    "Instamojo - your choice)",
                    "Accept UPI, debit & credit cards, net banking and "
                    "wallets",
                    "Cash on Delivery option that you can switch on or off",
                    "Secure, PCI-compliant hosted checkout - card details "
                    "never touch your website",
                    "Automatic payment success / failure handling with the "
                    "order status updated accordingly",
                    "Minimum order value enforced before checkout",
                    "Delivery charge rules - free above a set order value, "
                    "flat fee below it",
                    "Order confirmation on screen, by email and on WhatsApp",
                ],
            },
            {
                "heading": "Delivery & orders",
                "items": [
                    "Serviceable pincodes that you control from the admin "
                    "panel",
                    "Delivery slot selection (e.g. morning / evening) with "
                    "the slots you define",
                    "Order tracking for the customer - placed, packed, out "
                    "for delivery, delivered",
                    "WhatsApp order updates at each stage so customers stay "
                    "informed",
                    "Stock reduced automatically as orders are placed",
                    "Order notes field for customer instructions "
                    "(e.g. ripe bananas, no plastic bags)",
                ],
            },
            {
                "heading": "Admin panel",
                "items": [
                    "Secure admin login with a dashboard showing today's "
                    "orders, sales and low-stock items",
                    "Products - add, edit, remove; set price, MRP, unit, "
                    "pack variants, photos and status",
                    "Bulk product upload and price update via Excel / CSV - "
                    "essential for a large grocery list",
                    "Categories & sub-categories - create, rename, reorder "
                    "and set their images",
                    "Stock management with low-stock alerts and quick "
                    "in-stock / out-of-stock toggles",
                    "Order management - view every order, its items, payment "
                    "status and customer details; update status through to "
                    "delivered",
                    "Invoices / order slips you can print for packing and "
                    "delivery",
                    "Customers list with their order history",
                    "Coupons & offers - percentage or flat discount, minimum "
                    "order, validity dates and usage limits",
                    "Delivery settings - serviceable pincodes, delivery "
                    "slots, delivery charges and minimum order value",
                    "Homepage banner & featured-product management",
                    "Sales reports - by date, by product and by category, "
                    "exportable to Excel",
                    "A guided walkthrough and handover so your team can run "
                    "the store confidently",
                ],
            },
            {
                "heading": "Design, SEO & delivery",
                "items": [
                    "Clean, trust-building design matched to your brand "
                    "colours and logo",
                    "Mobile-first build optimised for fast loading on phone "
                    "data",
                    "Basic on-page SEO - page titles, meta descriptions, "
                    "clean URLs and image alt text",
                    "WhatsApp click-to-chat button for quick enquiries",
                    "Testing across major browsers and devices before launch",
                    "Deployment on a free hosting plan and help connecting "
                    "your domain",
                    "1 year of support for bugs & errors after launch",
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
        "There is no limit on the products or categories you can add from the admin panel. We set up {} products at launch and provide a bulk Excel / CSV import for the rest.".format(
            INITIAL_PRODUCTS),
        "Product photos, names, units and the price list are provided by the client.",
        "The payment gateway account is opened in the client's name with the client's KYC; its transaction fees are charged by the gateway and are not part of this quote.",
        "WhatsApp order updates are sent through a click-to-send / business messaging setup; if a WhatsApp Business API account is required, its subscription and per-message charges are paid by the client.",
        "Any SMS / email / OTP sending service subscription is arranged and paid for by the client.",
        "Deliveries are managed by the client's own staff; courier / delivery-partner API integration and a delivery staff app are separate scope.",
        "Timelines begin once the content, product list and advance payment are received.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
