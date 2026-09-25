"""
Bhama Vision - Aviraj Enterprises detergent manufacturer website quotation.

A clean, professional showcase website for a detergent manufacturer, with all
the basic pages (home, about us, products, contact us) and a simple admin
panel to add products in future and manage basic company details (WhatsApp
number, address, contact info and more).

Reuses the Bhama Vision quotation renderer:

    python3 build_aviraj_enterprises_quote.py

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
    "company": "Aviraj Enterprises",
    "note": "Detergent manufacturer showcase website with admin panel",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Clean, professional, responsive showcase website",
        "All basic pages - Home, About Us, Products, Contact Us",
        "Product showcase with images, description & details",
        "Admin panel to add / edit products in future",
        "Manage company details - WhatsApp, address, phone, email",
        "Enquiry / contact form + WhatsApp & call buttons",
        "Basic on-page SEO & Google Map on contact page",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Product photos & content (provided by the client)",
        "Online store / cart / payments (this is a showcase site)",
        "Distributor login / ordering portal - separate scope",
        "Mobile app (Android / iOS) - separate scope",
        "Ongoing marketing / SEO and any paid plugin or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-021",
        "package": "Showcase Website + Admin",
        "title": "Aviraj Enterprises Website",
        "subtitle": "Detergent product showcase with basic pages & a simple admin panel",
        "price": 5000,
        "price_note": "one-time (design & development)",
        "timeline": "8-14 working days",
        "summary": (
            "A clean, professional showcase website for Aviraj Enterprises "
            "that presents your detergent range attractively across all the "
            "essential pages - Home, About Us, Products and Contact Us. "
            "Visitors can browse your products with images and details and "
            "reach you instantly via an enquiry form, WhatsApp or call. A "
            "simple admin panel lets you add and edit products in future and "
            "update your basic company details - WhatsApp number, company "
            "address, phone, email and more - without any coding. The site is "
            "responsive and SEO-friendly."
        ),
        "sections": [
            {
                "heading": "Website pages (frontend)",
                "items": [
                    "Home - hero banner, about snapshot, featured products & "
                    "call-to-action",
                    "About Us - company story, vision / mission & why choose "
                    "us",
                    "Products - detergent range shown in a clean grid with "
                    "images & details",
                    "Product detail - image(s), description, key features / "
                    "specifications & enquiry button",
                    "Contact Us - enquiry form, WhatsApp & call buttons, "
                    "address & Google Map",
                    "Responsive design that looks great on mobile & desktop",
                ],
            },
            {
                "heading": "Products showcase",
                "items": [
                    "Detergent products displayed with images, name, "
                    "description & details (e.g. size / pack / type)",
                    "Organised into categories if needed (powder, liquid, "
                    "bar, etc.)",
                    "Initial products set up for you at launch",
                    "Add / edit / remove products yourself in future from the "
                    "admin panel",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with a simple dashboard",
                    "Add / edit / delete products with image upload",
                    "Manage product categories (if used)",
                    "Manage company details - WhatsApp number, address, "
                    "phone, email, social links",
                    "Edit basic page content (About text, banners, etc.)",
                    "View / manage contact enquiries",
                ],
            },
            {
                "heading": "SEO & contact",
                "items": [
                    "Basic on-page SEO - titles, meta descriptions & "
                    "friendly URLs",
                    "Google Map embedded on the contact page",
                    "WhatsApp click-to-chat & call buttons site-wide",
                    "Social share / links and mobile-friendly performance",
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
        "Domain and hosting are arranged and paid for by the client directly.",
        "This is a showcase website - it does not include an online store, cart or payments.",
        "Product photos and content are provided by the client; an initial set of products is added at launch and more can be added via the admin panel.",
        "The admin panel lets the client add products in future and manage basic company details (WhatsApp, address, contact info, etc.).",
        "A mobile app and distributor/ordering portal are separate scope.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
