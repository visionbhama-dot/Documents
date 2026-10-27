"""
Bhama Vision - tour & travel website + SEO keyword pages quotation content.

A complete, responsive tour & travel website (all standard pages, tour
packages, enquiry form and WhatsApp integration) together with 20 SEO
keyword landing pages built to rank on Google for high-intent search
terms. Includes on-page SEO and Google Search Console setup, a free
hosting plan and 1 year of bug & error support. The domain is arranged by
the client (not on our side). Reuses the Bhama Vision quotation renderer:

    python3 build_tour_travel_seo_quote.py

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
    "note": "Tour & travel website with 20 SEO keyword pages",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive tour & travel website with all standard pages",
        "Tour packages presented with photos, highlights & details",
        "20 SEO keyword landing pages built to rank on Google",
        "On-page SEO + Google Search Console setup & indexing",
        "Enquiry form - submissions reach your email & WhatsApp",
        "WhatsApp integration (click-to-chat + enquire on each package)",
        "Click-to-call button & Google Map on the contact page",
        "Hosting - free plan; 1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Photos, package details & company content (provided by the client)",
        "Keyword pages beyond 20 (added at a small per-page charge)",
        "Admin panel to self-manage packages (available as an add-on)",
        "Live flight / hotel booking engine & GDS API (separate scope)",
        "Ongoing monthly SEO & paid ad campaigns (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-035",
        "package": "Travel Website + SEO Pages",
        "title": "Tour & Travel Website",
        "subtitle": "Travel website with 20 SEO keyword pages, tour packages & WhatsApp integration",
        "price": 8000,
        "price_note": "one-time (design & development)",
        "timeline": "12-16 working days",
        "summary": (
            "A complete tour & travel website built not just to look good but "
            "to be found on Google. Alongside all the standard pages - home, "
            "about, tour packages, services, gallery and contact - we create "
            "20 SEO keyword landing pages, each targeting a specific "
            "high-intent search term travellers actually type (for example "
            "'Manali tour package from Delhi' or 'Kashmir honeymoon "
            "package'), so your agency has a real chance to rank and pull in "
            "organic enquiries. Visitors explore your packages with photos "
            "and details and reach you in one tap through a WhatsApp chat "
            "button, an 'Enquire on WhatsApp' button on each package, a "
            "click-to-call link or an enquiry form that lands in your email "
            "and WhatsApp. The whole site is built SEO-friendly and submitted "
            "to Google Search Console, and it comes with a free hosting plan "
            "and 1 year of bug & error support. The domain is arranged by you "
            "(it is not on our side), and we will help connect it."
        ),
        "sections": [
            {
                "heading": "Website pages",
                "items": [
                    "Home - hero banner, featured packages, services "
                    "snapshot & clear call-to-action",
                    "About Us - your agency's story, experience and why "
                    "travellers should choose you",
                    "Tour Packages - packages in a clean grid with photos, "
                    "duration and highlights",
                    "Package detail - photo gallery, itinerary highlights, "
                    "inclusions and an enquiry button",
                    "Services - ticketing, hotels, visa assistance, "
                    "transport and group tours",
                    "Gallery - destination and trip photos",
                    "Contact Us - enquiry form, WhatsApp & call buttons, "
                    "office address and Google Map",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "20 SEO keyword pages",
                "items": [
                    "20 dedicated landing pages, each targeting one "
                    "high-intent travel keyword you want to rank for",
                    "Keyword selection done with you - destinations, routes, "
                    "tour types and season-based search terms",
                    "Each page written with SEO-friendly titles, headings, "
                    "meta descriptions and a clean, keyword-based URL",
                    "Content structured to answer the searcher's intent with "
                    "a strong call-to-action and enquiry / WhatsApp button",
                    "Internal links between keyword pages and the matching "
                    "tour packages to strengthen ranking",
                    "Image alt text and fast-loading, mobile-first layout on "
                    "every keyword page",
                ],
            },
            {
                "heading": "Tour packages & destinations",
                "items": [
                    "Your tour packages set up with photos, duration, "
                    "highlights and pricing (if you wish to show it)",
                    "Grouped by type or destination - domestic, "
                    "international, pilgrimage, honeymoon, group tours",
                    "Featured packages highlighted on the home page",
                    "Seasonal or offer packages promoted on the banner",
                    "Clean, consistent layout that stays tidy as you add "
                    "more packages",
                ],
            },
            {
                "heading": "Enquiry form & WhatsApp integration",
                "items": [
                    "Enquiry form capturing name, phone, travel dates, "
                    "destination / package and message",
                    "Submissions delivered to your email and WhatsApp, so no "
                    "booking enquiry is missed",
                    "Spam protection on the form to keep junk enquiries out",
                    "Floating WhatsApp click-to-chat button on every page",
                    "'Enquire on WhatsApp' button on each package and keyword "
                    "page that opens a chat with the subject pre-filled",
                    "Click-to-call button for instant phone enquiries",
                ],
            },
            {
                "heading": "SEO setup & delivery",
                "items": [
                    "On-page SEO across the whole site - titles, meta "
                    "descriptions, headings, clean URLs and image alt text",
                    "Google Search Console set up, ownership verified and "
                    "sitemap submitted for indexing",
                    "XML sitemap generated covering all pages incl. the 20 "
                    "keyword pages",
                    "Fast-loading, mobile-first build tested across major "
                    "browsers and devices",
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
        "This package covers 20 SEO keyword pages; additional keyword pages are added at a small per-page charge.",
        "Keywords are finalised together with the client before the pages are built.",
        "Package photos, itineraries and company content are provided by the client.",
        "On-page SEO and Search Console setup help your pages become eligible to rank; search rankings depend on Google and competition and cannot be guaranteed. Ongoing monthly SEO and ad campaigns are a separate service.",
        "Enquiries reach you by email and WhatsApp; an admin panel to add and edit packages yourself is available as an add-on and is quoted separately.",
        "Timelines begin once the content, logo and advance payment are received.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
