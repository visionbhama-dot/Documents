"""
Quotation content for the Doer Way Nex website with admin panel.
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
    "name": "Doer Way Nex",
    "company": "Doer Way Nex",
    "note": "Website with admin panel (case studies & services)",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive, professional business website",
        "Case studies section with images & details",
        "Services section to present what you offer",
        "Admin panel to manage case studies & services",
        "About, team and contact / enquiry sections",
        "Basic on-page SEO and social-media links",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Written content, logos, images and other media assets",
        "Paid stock media, plugins, tools or third-party APIs",
        "Online store / payment features",
        "Ongoing maintenance, SEO, advertising or content entry",
        "Features or integrations outside the scope listed here",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-013",
        "package": "Website + Admin",
        "title": "Doer Way Nex Website",
        "subtitle": "Business website with case-studies & services management",
        "price": 5500,
        "price_note": "one-time (design & development)",
        "timeline": "8-12 working days",
        "summary": (
            "A clean, professional and responsive website for Doer Way Nex with "
            "an easy-to-use admin panel to run it yourself. It includes a case "
            "studies section to showcase completed work and a services section "
            "to present what you offer. From the admin panel you can add, edit "
            "or remove case studies and services - no coding needed."
        ),
        "sections": [
            {
                "heading": "Frontend (website)",
                "items": [
                    "Responsive website - home, about, services, case studies "
                    "& contact",
                    "Services section to showcase what you offer",
                    "Case studies section with images, details & results",
                    "About / team section to build trust",
                    "Contact / enquiry form",
                    "SEO-friendly structure across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Case studies & services showcase",
                "items": [
                    "Case studies listing with cover images",
                    "Individual case study page with description & images",
                    "Highlight the problem, work done and results",
                    "Services listing with descriptions and icons / images",
                    "Professional layout to present your portfolio of work",
                ],
            },
            {
                "heading": "Backend (admin panel)",
                "items": [
                    "Secure admin login",
                    "Add, edit and delete case studies",
                    "Upload case-study cover and detail images",
                    "Add, edit and delete services",
                    "Manage page content and view contact enquiries",
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
        "Content, images and case-study details are added by the client via the admin panel.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
