"""
Bhama Vision - B2B food-packaging manufacturer website quotation content.

A B2B website for a food-packaging items manufacturer (cups, plates,
containers, etc.) with a backend to manage products, blogs and images.
Enquiry-based only - NO online payment. Includes WhatsApp integration and
a custom design editor so customers can design their own cups, plates and
packaging (add logo / text / artwork) and send the design with their
enquiry. Comes with free hosting and 1 year of bug & error support. The
domain is arranged by the client (not on our side). Reuses the Bhama
Vision quotation renderer:

    python3 build_food_packaging_b2b_quote.py

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
    "note": "B2B food-packaging website with backend & custom design editor",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive B2B website (frontend) + backend admin panel",
        "Product catalogue (cups, plates, containers, etc.) with specs",
        "Custom design editor - customers design their own products",
        "Enquiry / quote-request form (no online payment)",
        "WhatsApp integration (click-to-chat + enquiries to WhatsApp)",
        "Blog section managed from the backend",
        "Image / gallery management from the backend",
        "Hosting - free plan; 1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Online payment / cart / checkout (enquiry-based only)",
        "Product content, specs, photos & artwork (provided by the client)",
        "Live-order production / printing workflow or ERP integration",
        "Customer / sales mobile app",
        "SEO / marketing campaigns (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-026",
        "package": "B2B Website + Design Editor",
        "title": "Food-Packaging B2B Website",
        "subtitle": "Manufacturer website with backend, enquiry forms & a custom design editor",
        "price": 18000,
        "price_note": "one-time (design & development)",
        "timeline": "25-35 working days",
        "summary": (
            "A professional B2B website for a food-packaging items "
            "manufacturer (cups, plates, containers and more) with a backend "
            "to manage products, blogs and images on your own. The site is "
            "enquiry-based - there is NO online payment; instead, buyers send "
            "a quote / enquiry that reaches you directly on WhatsApp and "
            "email. The highlight is a custom design editor that lets "
            "customers design their own products - pick an item, add their "
            "logo, text and artwork, choose colours, preview it, and send the "
            "finished design along with their enquiry. It comes with a "
            "WhatsApp chat button, a free hosting plan and 1 year of bug & "
            "error support. The domain is arranged by you (it is not on our "
            "side), and we will help connect it to the website."
        ),
        "sections": [
            {
                "heading": "Customer-facing website",
                "items": [
                    "Home page with banners, product highlights & categories",
                    "Product catalogue - cups, plates, containers, bowls, "
                    "boxes, etc. with specifications and sizes",
                    "Product detail pages with image gallery, materials & "
                    "minimum-order details",
                    "Enquiry / request-a-quote form (name, company, product, "
                    "quantity, message) - no online payment",
                    "WhatsApp integration - click-to-chat button and enquiries "
                    "sent to your WhatsApp / email",
                    "Blog / news section to share updates and build trust",
                    "Content pages: about, manufacturing, certifications & "
                    "contact",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Custom design editor (highlight)",
                "items": [
                    "Customers pick a product (cup, plate, container, etc.) to "
                    "customise",
                    "Upload their logo and add custom text with font & colour "
                    "options",
                    "Add artwork / images and position them on the product",
                    "Choose base colours and see a live preview of the design",
                    "Save / download the preview and attach it to an enquiry",
                    "The finished design and specs are sent with the enquiry "
                    "so you can quote accurately",
                ],
            },
            {
                "heading": "Backend admin panel",
                "items": [
                    "Secure admin login for your team",
                    "Add, edit and remove products, categories & specifications",
                    "Manage product images and the website gallery",
                    "Write, edit and publish blog / news posts",
                    "View and manage enquiries (with the attached custom "
                    "designs)",
                    "Homepage banner management",
                    "A guided walkthrough and handover so your team is "
                    "comfortable using everything",
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
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "The website is enquiry-based only; online payment, cart and checkout are not included and can be quoted separately.",
        "The custom design editor lets customers design and preview products and attach the design to an enquiry; it is not a live print-production or ordering system.",
        "The backend covers products, images, blogs and enquiries; ERP / production-workflow integrations are not included and can be quoted separately.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new products/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
