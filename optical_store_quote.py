"""
Bhama Vision - optical / eyewear store website quotation content.

A website for an optical store (spectacles, frames, sunglasses, contact
lenses) with up to 20 products and a backend admin panel to manage
products, images and enquiries. Customers browse the catalogue and order
or enquire over WhatsApp. Comes with free hosting and 1 year of bug &
error support. The domain is arranged by the client (not on our side).
Reuses the Bhama Vision quotation renderer:

    python3 build_optical_store_quote.py

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
    "note": "Optical store website (20 products) with backend",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive optical store website + backend admin panel",
        "Up to 20 products set up with photos, price & details",
        "Frames, sunglasses, lenses & contact-lens categories",
        "WhatsApp integration - order & enquire on WhatsApp",
        "Enquiry / appointment form for eye tests & store visits",
        "Backend to manage products, images & enquiries",
        "Hosting - free plan",
        "1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Product photos & content (provided by the client)",
        "Products beyond 20 (added at a small per-product charge)",
        "Virtual try-on / AR frame preview",
        "Prescription-lens configurator (power, coatings, tints)",
        "SMS / email / OTP sending service subscription",
        "SEO / marketing (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-028",
        "package": "Optical Store + Backend",
        "title": "Optical Store Website",
        "subtitle": "Eyewear catalogue with backend admin panel & WhatsApp ordering",
        "price": 6000,
        "price_note": "one-time (design & development)",
        "timeline": "10-14 working days",
        "summary": (
            "A clean, professional website for your optical store that puts "
            "your eyewear range online - spectacle frames, sunglasses, lenses "
            "and contact lenses - with up to 20 products set up for you. "
            "Customers browse the catalogue, view each product in detail and "
            "then order or enquire directly on WhatsApp, so every lead "
            "reaches you instantly. They can also request an eye test or "
            "store visit through a simple appointment form. A backend admin "
            "panel lets you add and update products, prices, photos and "
            "banners yourself, and view all enquiries in one place. It comes "
            "with a free hosting plan and 1 year of bug & error support. The "
            "domain is arranged by you (it is not on our side), and we will "
            "help connect it to the website."
        ),
        "sections": [
            {
                "heading": "Customer-facing website",
                "items": [
                    "Home page with banners, featured eyewear & categories",
                    "Product catalogue - spectacle frames, sunglasses, "
                    "reading glasses, lenses & contact lenses",
                    "Category and brand-wise browsing with search & sort",
                    "Product detail pages with image gallery, frame details "
                    "(shape, material, size, colour) and price",
                    "Up to 20 products set up with photos, price and details",
                    "WhatsApp integration - 'Order on WhatsApp' / "
                    "'Enquire now' buttons that open a chat with the product "
                    "details pre-filled",
                    "Eye test / store visit appointment form (name, phone, "
                    "preferred date & message)",
                    "Click-to-call button and Google Maps store location",
                    "Content pages: about the store, services, offers & "
                    "contact",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Backend admin panel",
                "items": [
                    "Secure admin login for the store owner",
                    "Add, edit and remove products, categories & brands",
                    "Upload product photos and set price, frame details & "
                    "status (in stock / sold out)",
                    "Manage the website gallery and homepage banners",
                    "View and manage enquiries & appointment requests",
                    "Mark products as featured to highlight them on the home "
                    "page",
                    "A short walkthrough so you are comfortable updating the "
                    "website yourself",
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
        "This package covers up to 20 products; additional products are added at a small per-product charge.",
        "Orders and enquiries come to you on WhatsApp, email and the backend enquiry list.",
        "Product photos, brand names and descriptions are provided by the client.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new products/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
