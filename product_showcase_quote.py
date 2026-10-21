"""
Bhama Vision - product showcase website quotation content.

A clean, responsive showcase website that presents a product range across
multiple categories, with the standard pages (Home, About Us, Products,
Contact Us), an enquiry form and WhatsApp integration so every lead
reaches the client directly. Comes with free hosting and 1 year of bug &
error support. The domain is arranged by the client (not on our side).
Reuses the Bhama Vision quotation renderer:

    python3 build_product_showcase_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Scope caps - repeated in the included list, the bullets and the terms so
# the fixed price is unambiguous. Adjust both if the client needs more.
MAX_CATEGORIES = 6
MAX_PRODUCTS = 40

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
    "note": "Product showcase website with categories & enquiry form",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Clean, professional, responsive showcase website",
        "All standard pages - Home, About Us, Products, Contact Us",
        "Product range organised into multiple categories",
        "Up to {} categories and {} products set up for you".format(
            MAX_CATEGORIES, MAX_PRODUCTS),
        "Product detail pages with images, description & specifications",
        "Enquiry form - submissions reach your email & WhatsApp",
        "WhatsApp integration (click-to-chat + per-product enquire button)",
        "Basic on-page SEO & Google Map on the contact page",
        "Hosting - free plan; 1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Product photos, descriptions & company content (provided by the "
        "client)",
        "Admin panel to self-manage products (available as an add-on)",
        "Categories or products beyond the above (added at a small charge)",
        "Multi-language versions of the website",
        "SEO campaigns & paid ads (separate service)",
        "Mobile app (Android / iOS) - separate scope",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-031",
        "package": "Product Showcase Website",
        "title": "Product Showcase Website",
        "subtitle": "Multi-category product catalogue with enquiry form & WhatsApp",
        "price": 6500,
        "price_note": "one-time (design & development)",
        "timeline": "8-12 working days",
        "summary": (
            "A clean, professional website that puts your full product range "
            "online and turns visitors into enquiries. Your products are "
            "organised into categories so customers can find what they need "
            "quickly, and each product gets its own page with images, a "
            "description and specifications. Alongside the catalogue you get "
            "all the standard pages - Home, About Us, Products and Contact "
            "Us - that give your business a credible online presence. Every "
            "page makes it easy to get in touch: an enquiry form that drops "
            "straight into your email and WhatsApp, a WhatsApp chat button, "
            "an 'Enquire on WhatsApp' button on each product that opens a "
            "chat with the product name already filled in, a click-to-call "
            "button and a Google Map on the contact page. The site is fully "
            "responsive, SEO-friendly, and comes with a free hosting plan "
            "and 1 year of bug & error support. The domain is arranged by you "
            "(it is not on our side), and we will help connect it."
        ),
        "sections": [
            {
                "heading": "Website pages",
                "items": [
                    "Home - hero banner, business snapshot, featured products "
                    "& category highlights",
                    "About Us - your story, vision & mission, and why "
                    "customers should choose you",
                    "Products - full range in a clean grid, browsable by "
                    "category",
                    "Category pages - a dedicated page for each product "
                    "category",
                    "Product detail - image gallery, description, key "
                    "features / specifications & enquiry button",
                    "Contact Us - enquiry form, WhatsApp & call buttons, "
                    "address and Google Map",
                    "Supporting pages as needed - services, certifications, "
                    "gallery or FAQ",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Product showcase & categories",
                "items": [
                    "Products grouped into multiple categories so visitors "
                    "can narrow down quickly",
                    "Up to {} categories and up to {} products in total set "
                    "up with your photos and content".format(
                        MAX_CATEGORIES, MAX_PRODUCTS),
                    "Each product shown with image, name, short description "
                    "and details (size / variant / specification)",
                    "Category-wise browsing plus search and sort on the "
                    "products page",
                    "Featured products highlighted on the home page",
                    "Clean, consistent layout that stays tidy as the range "
                    "grows",
                ],
            },
            {
                "heading": "Enquiry form & WhatsApp integration",
                "items": [
                    "Enquiry form capturing name, phone, email, product of "
                    "interest and message",
                    "Submissions delivered to your email inbox and your "
                    "WhatsApp, so no lead is missed",
                    "Spam protection on the form to keep junk enquiries out",
                    "Floating WhatsApp click-to-chat button on every page",
                    "'Enquire on WhatsApp' button on each product that opens "
                    "a chat with the product name pre-filled",
                    "Click-to-call button for instant phone enquiries",
                    "Thank-you confirmation shown to the customer after "
                    "submitting",
                ],
            },
            {
                "heading": "Design, SEO & delivery",
                "items": [
                    "Modern, professional design matched to your brand "
                    "colours and logo",
                    "Basic on-page SEO - page titles, meta descriptions, "
                    "clean URLs and image alt text",
                    "Google Map embedded on the contact page",
                    "Fast-loading, mobile-first build",
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
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "This package covers up to {} categories and up to {} products; anything beyond that is added at a small charge.".format(
            MAX_CATEGORIES, MAX_PRODUCTS),
        "Product photos, descriptions and company content are provided by the client.",
        "Enquiries reach you by email and WhatsApp; an admin panel to add and edit products yourself is available as an add-on and is quoted separately.",
        "Timelines begin once the content, logo and advance payment are received.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new products/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
