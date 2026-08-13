"""
Bhama Vision - Architect portfolio website quotation.

Reference style: an architecture-studio site (e.g. architect.nexturex.com) with
a viewable 3D model on the website and a 360-degree virtual tour, plus
portfolio, services and journal/articles.

Two options:
  - Without Admin        -> informative site, 3D + 360 tour       (Rs 2,599)
  - With Admin           -> above + admin to add articles/portfolio (Rs 2,999)

Build:  python3 build_architect.py
"""

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
    "note": "Architect portfolio website with 3D model & 360 tour",
}

REQUIREMENTS = {
    "title": "Scope & requirements",
    "left_label": "Delivered by Bhama Vision",
    "right_label": "On client's side (third-party)",
    "covered": [
        "Complete, responsive website design & development",
        "Integration of a 3D model viewer inside the website",
        "Integration of the 360-degree virtual tour (e.g. Matterport embed)",
        "All pages/sections listed in this quotation",
        "Enquiry / contact form and Google Map embed",
        "Deployment to the client's hosting + handover, testing & bug fixing",
    ],
    "not_covered": [
        "Domain and web hosting / server (and its yearly cost)",
        "The 3D model file(s) to be shown (client-provided, or created "
        "separately on request)",
        "360-degree tour capture and its hosting subscription "
        "(e.g. Matterport) and the tour link/media",
        "All content: project photos, renders, text, logo and articles",
        "Business email account, if required",
        "Any paid plugin, stock media or third-party API",
    ],
}

QUOTATIONS = [
    {
        "id": "BV-Q-2026-PA1",
        "package": "Without Admin",
        "title": "Architect Portfolio Website",
        "subtitle": "3D model on site + 360 virtual tour (content set up by us)",
        "price": 2599,
        "price_note": "one-time (design & development)",
        "timeline": "8-12 working days",
        "summary": (
            "A premium, informative website for an architecture practice - with "
            "an interactive 3D model viewable right on the site and an immersive "
            "360-degree virtual tour so visitors can 'walk through' a project "
            "before it is built. Includes portfolio, services and journal "
            "sections. We set up all content at launch; there is no self-service "
            "admin in this option."
        ),
        "sections": [
            {
                "heading": "Immersive features",
                "items": [
                    "3D model viewer embedded in the website "
                    "(rotate / zoom / explore)",
                    "360-degree virtual tour integration (e.g. Matterport embed)",
                    "Optional interactive hotspots / gallery around the model",
                ],
            },
            {
                "heading": "Website pages & sections",
                "items": [
                    "Home: hero, studio intro & key highlights",
                    "About / Studio: profile, team and stats",
                    "Services: architecture & design offerings",
                    "Portfolio: selected works with project detail pages",
                    "Process: how the studio works, step by step",
                    "Journal: articles / blog (display only in this option)",
                    "Contact: enquiry form, map, call & email",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
    {
        "id": "BV-Q-2026-PA2",
        "package": "With Admin",
        "title": "Architect Portfolio Website",
        "subtitle": "3D + 360 tour + admin to add articles & portfolio projects",
        "price": 2999,
        "price_note": "one-time (design & development)",
        "timeline": "12-16 working days",
        "summary": (
            "Everything in the immersive website (3D model on site + 360-degree "
            "virtual tour, portfolio, services and journal), plus a simple admin "
            "panel so the architect can add and manage journal articles and "
            "portfolio projects themselves - without any coding."
        ),
        "sections": [
            {
                "heading": "Immersive features",
                "items": [
                    "3D model viewer embedded in the website "
                    "(rotate / zoom / explore)",
                    "360-degree virtual tour integration (e.g. Matterport embed)",
                    "Optional interactive hotspots / gallery around the model",
                ],
            },
            {
                "heading": "Website pages & sections",
                "items": [
                    "Home, About / Studio, Services, Process and Contact",
                    "Portfolio: selected works with project detail pages",
                    "Journal: articles / blog listing and detail pages",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Admin panel - architect can manage",
                "items": [
                    "Add / edit / remove journal articles (title, images, content)",
                    "Add / edit / remove portfolio projects (photos, details)",
                    "Update home-page highlights and contact details",
                    "Secure admin login",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

TERMS = {
    "validity_days": 15,
    "payment": "50% advance to start and 50% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design "
        "& development work quoted.",
        "Domain, hosting, 360-tour hosting (e.g. Matterport) and any paid "
        "plugin/API are arranged and paid for by the client directly.",
        "The 3D model file and all content (photos, renders, text, logo, "
        "articles) are provided by the client.",
        "Timelines begin once content, access and the advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
