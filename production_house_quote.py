"""
Quotation content for a production-house portfolio website with admin panel.
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
    "note": "Production-house website with admin panel",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive, animated production-house website",
        "Professional custom interface for mobile, tablet & desktop",
        "Movies / projects portfolio with cover and gallery images",
        "Admin panel to manage movies, galleries & slider images",
        "About, services and contact / enquiry sections",
        "Basic on-page SEO and social-media links",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Written content, logos, movie images and other media assets",
        "Video hosting, streaming infrastructure or OTT features",
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
        "id": "BV-Q-2026-012",
        "package": "Website + Admin",
        "title": "Production House Website",
        "subtitle": "Animated portfolio website with movie, gallery and slider management",
        "price": 5800,
        "price_note": "one-time (design & development)",
        "timeline": "8-12 working days",
        "summary": (
            "A modern, animated and professional website created to present the "
            "production house and showcase its completed movies and projects. Each "
            "movie can have a cover image, project information and a gallery of "
            "multiple images. A secure admin panel will make it easy to add, edit "
            "or remove movies and manage homepage slider images without coding."
        ),
        "sections": [
            {
                "heading": "Website design & experience",
                "items": [
                    "Modern, professional visual design tailored for a production house",
                    "Smooth animations and polished transitions across the website",
                    "Responsive layout for mobile, tablet, laptop and desktop",
                    "Home page with a dynamic image slider / hero banner",
                    "About, services and contact / enquiry sections",
                    "SEO-friendly page structure and social-media links",
                ],
            },
            {
                "heading": "Movies & project showcase",
                "items": [
                    "Movies / completed-projects listing with attractive cover images",
                    "Individual movie page with title, description and project details",
                    "One primary cover / poster image for every movie",
                    "Multiple gallery images for each movie or project",
                    "Professional gallery layout for showcasing production work",
                ],
            },
            {
                "heading": "Admin panel",
                "items": [
                    "Secure admin login",
                    "Add, edit and delete movies / completed projects",
                    "Upload a movie cover image and multiple gallery images",
                    "Add or update movie descriptions and project information",
                    "Upload, reorder and remove homepage slider images",
                    "Manage key website content and view contact enquiries",
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
        "The client will provide the logo, text, movie details, images and other media assets.",
        "The website will display supplied or externally hosted media; video hosting and streaming are not included.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
