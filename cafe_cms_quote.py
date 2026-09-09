"""
Quotation content for a dynamic cafe / fast-food website with a custom
CMS/admin panel, dynamic content management, interactive database features
and lead management.
"""

# ---------------------------------------------------------------------------
# Company and client details.
# ---------------------------------------------------------------------------
COMPANY = {
    "name": "Bhama Vision",
    "tagline": "Websites, apps & AI for growing businesses",
    "email": "info@bhamavision.com",
    "phone": "+91 88606 40250",
    "website": "www.bhamavision.com",
    "location": "India",
}

CLIENT = {
    "name": "Prospective Client",
    "company": "Confidential",
    "note": "Dynamic cafe / fast-food website with custom CMS",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Dynamic, responsive cafe / fast-food website",
        "Custom CMS / admin panel (no coding needed)",
        "Dynamic menu, offers & content management",
        "Interactive database-driven features",
        "Lead / enquiry management with dashboard",
        "Basic on-page SEO and social-media links",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Written content, logos, food images & other media assets",
        "Online payment gateway / third-party delivery integrations",
        "Paid stock media, plugins, tools or third-party APIs",
        "Ongoing maintenance, SEO, advertising or content entry",
        "Features or integrations outside the scope listed here",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-014",
        "package": "Website + Custom CMS",
        "title": "Cafe & Fast Food Website",
        "subtitle": "Dynamic momos & fast-food site with custom CMS, database features & lead management",
        # list_price is the MRP; price is the final payable after discount.
        "list_price": 15000,
        "discount_percent": 10,
        "price": 13500,
        "price_note": "one-time (after 10% discount)",
        "timeline": "15-20 working days",
        "summary": (
            "A modern, dynamic website for your momos & fast-food cafe, powered "
            "by a custom CMS/admin panel so you can manage everything yourself. "
            "Update your menu, prices, offers and content anytime, capture and "
            "manage customer leads from one dashboard, and use interactive "
            "database-driven features - all without touching any code."
        ),
        "sections": [
            {
                "heading": "Dynamic website (frontend)",
                "items": [
                    "Responsive design for mobile, tablet & desktop",
                    "Home, about, menu, gallery, offers & contact sections",
                    "Dynamic menu with categories (momos, fast food, beverages)",
                    "Item cards with photo, description, price & tags",
                    "Special offers / today's deals section",
                    "Enquiry / order-request & contact forms",
                    "SEO-friendly structure and social-media links",
                ],
            },
            {
                "heading": "Custom CMS / admin panel",
                "items": [
                    "Secure admin login with role-based access",
                    "Add, edit and delete menu items & categories",
                    "Manage prices, availability and daily offers",
                    "Dynamic content management for pages, banners & gallery",
                    "Upload and organise food images",
                    "No coding required to run the site",
                ],
            },
            {
                "heading": "Interactive database features",
                "items": [
                    "Database-driven menu, offers and content",
                    "Search & filter items by category or tags",
                    "Reusable content blocks managed from the CMS",
                    "Structured storage for menu, media & enquiries",
                ],
            },
            {
                "heading": "Lead management",
                "items": [
                    "Capture enquiries and order requests from the website",
                    "Leads dashboard to view, search & update status",
                    "Mark leads as new / contacted / converted",
                    "Export leads (CSV) for follow-up",
                    "Email / WhatsApp link for quick response",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

# Terms shown on the closing page of the quotation.
TERMS = {
    "validity_days": 15,
    "payment": "40% advance to start, 60% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "A 10% discount has been applied: MRP ₹15,000, payable ₹13,500.",
        "Domain and hosting are arranged and paid for by the client directly; we will help set them up.",
        "Menu, prices, content and images are added by the client via the admin panel.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
