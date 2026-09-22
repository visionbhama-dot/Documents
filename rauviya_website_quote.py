"""
Bhama Vision - RAUVIYA luxury catalog website quotation content.

A premium, luxury brand website with a product catalog organised by
categories, rich product pages that highlight features (not an online
checkout), and a WhatsApp "Enquire / Contact" button in place of add-to-cart.
Comes with a full admin panel to manage categories, products and enquiries.

Reuses the Bhama Vision quotation renderer:

    python3 build_rauviya_website_quote.py

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
    "company": "RAUVIYA",
    "note": "Luxury catalog website with WhatsApp enquiry & admin panel",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Premium, luxury-styled responsive website",
        "Product catalog organised by categories & sub-categories",
        "Rich product pages with images, description & feature highlights",
        "WhatsApp \"Enquire on WhatsApp\" button on every product",
        "Full admin panel to manage categories, products & enquiries",
        "Enquiry / lead capture with WhatsApp + email notification",
        "Basic on-page SEO, contact page & Google Maps",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Online payments / cart / checkout (not part of this scope)",
        "Product photography & content (provided by the client)",
        "WhatsApp Business API subscription (uses free click-to-chat)",
        "Multi-vendor / marketplace features & mobile app",
        "Ongoing marketing / paid ads and any paid plugin or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-018",
        "package": "Luxury Website + Admin",
        "title": "RAUVIYA Luxury Catalog Website",
        "subtitle": "Category & product showcase with WhatsApp enquiry, plus a full admin panel",
        "price": 16000,
        "price_note": "one-time (design & development)",
        "timeline": "15-22 working days",
        "summary": (
            "A premium, luxury-styled website for RAUVIYA that showcases your "
            "products beautifully rather than selling them through a cart. "
            "Visitors browse by category, open a rich product page with an "
            "image gallery, description and clear feature highlights, then tap "
            "an \"Enquire on WhatsApp\" button to reach you directly - no "
            "checkout, no payment gateway. Behind the scenes, a full admin "
            "panel lets you manage categories, products and their features, "
            "update the homepage, and track every enquiry. The design is "
            "responsive and built for a refined, high-end brand feel."
        ),
        "sections": [
            {
                "heading": "Customer-facing website (frontend)",
                "items": [
                    "Premium, luxury-styled responsive design - elegant home "
                    "with hero, featured products & category highlights",
                    "Category & sub-category browsing with search, filter and "
                    "sort",
                    "Product listing pages laid out for a clean, high-end "
                    "showcase",
                    "Product detail page - image gallery, full description "
                    "and a dedicated feature / specification list",
                    "Prominent \"Enquire on WhatsApp\" button on each product "
                    "(pre-fills product name so you know what they want)",
                    "Floating WhatsApp chat button available site-wide",
                    "Enquiry form (name, phone, message) as a fallback to "
                    "WhatsApp",
                    "About, contact (with Google Map) and policy pages",
                ],
            },
            {
                "heading": "Products & features",
                "items": [
                    "Products grouped into categories / collections you "
                    "define",
                    "Each product with images, rich description, price-on-"
                    "request or displayed price (your choice)",
                    "Per-product feature / specification highlights (bullet "
                    "list you control)",
                    "Tags, related products and \"featured\" flag for the "
                    "homepage",
                    "Initial set of products & categories set up for you at "
                    "launch",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard overview",
                    "Manage categories & sub-categories (add / edit / delete, "
                    "reorder)",
                    "Manage products - images, description, price and the "
                    "per-product feature list",
                    "Mark products as featured / hide them from the site",
                    "Enquiries inbox - every WhatsApp/form lead captured with "
                    "product context",
                    "Homepage & banner management, plus content pages",
                    "Basic settings - WhatsApp number, contact details & SEO "
                    "meta",
                ],
            },
            {
                "heading": "WhatsApp enquiry (instead of add-to-cart)",
                "items": [
                    "Click-to-chat (wa.me) integration - opens the customer's "
                    "WhatsApp with your number",
                    "Message pre-filled with the product name / link so you "
                    "instantly know the interest",
                    "Uses the free WhatsApp click-to-chat - no paid API needed",
                    "Every enquiry also logged in the admin panel for "
                    "follow-up",
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
        "This is a catalog / showcase website - it uses WhatsApp enquiry instead of an online cart, checkout or payment gateway.",
        "Product photos and content are provided by the client; an initial set of products/categories is set up at launch and more can be added via the admin panel.",
        "WhatsApp integration uses the free click-to-chat; the WhatsApp Business API (if ever needed) is separate.",
        "Multi-vendor / marketplace features and a mobile app are separate.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
