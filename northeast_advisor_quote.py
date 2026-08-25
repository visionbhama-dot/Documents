"""
Bhama Vision - Northeast Advisor website quotation content.

A travel website (frontend + admin backend) with WhatsApp integration and
SEO: manage tour packages, homestays, blogs, a "Partner with us" property
leads form and the hero banner. Reuses the Bhama Vision quotation renderer:

    python3 build_northeast_advisor_quote.py

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
    "name": "Northeast Advisor",
    "company": "Northeast Advisor",
    "note": "Travel website with admin panel & SEO",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive frontend website with hero banner",
        "Tour packages, homestays & blog sections",
        "\"Partner with us\" property lead form",
        "Admin panel to manage all of the above",
        "WhatsApp integration (click-to-chat)",
        "On-page SEO setup & Search Console indexing",
        "Enquiry / lead data captured in the admin panel",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Website content, images & blog articles (provided by client)",
        "Online payment / booking & real-time availability",
        "Ongoing monthly SEO or ad campaigns (separate service)",
        "Mobile app (Android / iOS)",
        "Any paid plugin, tool or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-008",
        "package": "Website + Admin",
        "title": "Northeast Advisor Website",
        "subtitle": "Travel website + admin panel, with WhatsApp integration & SEO",
        "price": 9000,
        "price_note": "one-time (design & development)",
        "timeline": "12-18 working days",
        "summary": (
            "A complete travel website for Northeast Advisor with a powerful "
            "admin panel to run it. Visitors can explore tour packages, "
            "homestays and blog articles, reach you instantly on WhatsApp, and "
            "property owners can submit their details through a \"Partner with "
            "us\" form. From the admin panel you can manage packages, "
            "homestays, blogs, the hero banner and view all incoming leads. "
            "The site is built SEO-friendly so it can rank and get found on "
            "Google."
        ),
        "sections": [
            {
                "heading": "Frontend (website)",
                "items": [
                    "Responsive website with an eye-catching hero banner",
                    "Tour / travel packages listing and detail pages",
                    "Homestays listing and detail pages",
                    "Blog section for travel articles & guides",
                    "\"Partner with us\" page with a property submission / "
                    "leads form",
                    "WhatsApp integration - click-to-chat button to reach you "
                    "in one tap",
                    "Contact & enquiry forms",
                    "Mobile, tablet & desktop responsive design",
                ],
            },
            {
                "heading": "Backend (admin panel)",
                "items": [
                    "Manage tour packages - add, edit, view & remove",
                    "Manage homestays - add, edit, view & remove",
                    "Manage blog posts - write, edit & publish",
                    "View & manage \"Partner with us\" property leads / form "
                    "submissions",
                    "Manage the homepage hero banner",
                    "View contact & enquiry form data",
                    "Simple dashboard to see it all at a glance",
                ],
            },
            {
                "heading": "SEO features",
                "items": [
                    "On-page SEO - titles, meta tags, headings & clean URLs",
                    "XML sitemap & Google Search Console setup and indexing",
                    "Image alt tags and basic page-speed optimization",
                    "SEO-friendly structure so pages can rank on Google",
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
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "Domain and hosting are arranged and paid for by the client directly; we will help set them up.",
        "Content, images and blog articles are provided by the client.",
        "SEO here is a one-time on-page setup + indexing; ongoing monthly SEO is a separate service.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
