"""
Bhama Vision - website + admin panel quotation content.

A responsive website with a blog, image gallery and services section, plus
an admin panel to manage it all and connect Google AdSense & Analytics.
Reuses the Bhama Vision quotation renderer:

    python3 build_website_admin_quote.py

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
    "note": "Website with admin panel",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive website (blog, gallery, services & contact)",
        "Admin panel to manage blog, images & services",
        "Blog section with article management",
        "Image gallery management",
        "Services section management",
        "Google AdSense connect option (in admin)",
        "Google Analytics connect option (in admin)",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Content, images & articles (added by the client)",
        "Google AdSense account approval (Google's decision - not guaranteed)",
        "Online store / payment features",
        "Ongoing monthly SEO or ad campaigns (separate service)",
        "Any paid plugin, tool or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-011",
        "package": "Website + Admin",
        "title": "Website with Admin Panel",
        "subtitle": "Blog, image gallery & services section, with AdSense & Analytics connect",
        "price": 5000,
        "price_note": "one-time (design & development)",
        "timeline": "8-12 working days",
        "summary": (
            "A clean, responsive website with an easy-to-use admin panel to "
            "run it yourself. It includes a blog to publish articles, an image "
            "gallery to showcase your work, and a services section to present "
            "what you offer. From the admin panel you can also connect Google "
            "AdSense to monetise the site and Google Analytics to track your "
            "visitors - no coding needed."
        ),
        "sections": [
            {
                "heading": "Frontend (website)",
                "items": [
                    "Responsive website - home, about, services, blog, gallery "
                    "& contact",
                    "Services section to showcase what you offer",
                    "Blog section for articles & updates",
                    "Image gallery to display photos / work",
                    "Contact / enquiry form",
                    "SEO-friendly structure across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Backend (admin panel)",
                "items": [
                    "Write, edit, publish & delete blog articles",
                    "Upload and manage gallery images",
                    "Add & edit the services section content",
                    "Connect Google AdSense (site verification & ad code)",
                    "Connect Google Analytics (add your tracking ID)",
                    "Manage page content and view contact-form submissions",
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
        "Domain and hosting are arranged and paid for by the client directly; we will help set them up.",
        "We provide the option to connect Google AdSense, but AdSense approval is Google's decision and is not guaranteed.",
        "Content, images and blog articles are added by the client via the admin panel.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
