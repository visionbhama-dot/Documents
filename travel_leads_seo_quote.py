"""
Bhama Vision - travel website + admin panel (lead capture + SEO) quotation.

A responsive tour & travel website built to capture leads, with an admin
panel to manage tour packages and view enquiry leads, plus on-page SEO and
Google Search Console setup. Priced as a one-time development fee with an
optional monthly website-management plan (adding 2-3 new packages each
month with SEO).

Reuses the Bhama Vision quotation renderer:

    python3 build_travel_leads_seo_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Monthly management plan details (kept in one place so the price note,
# the plan section and the terms all stay in sync).
MONTHLY_FEE = 3000
PACKAGES_PER_MONTH = "2-3"

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
    "note": "Travel website + admin panel to capture leads, with SEO",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive tour & travel website with all standard pages",
        "Admin panel to manage tour packages & view leads",
        "Lead capture - enquiry form reaching email & WhatsApp",
        "WhatsApp click-to-chat & enquire-on-package buttons",
        "On-page SEO + Google Search Console setup & indexing",
        "Tour packages set up at launch with photos & details",
        "Monthly plan: add {} packages / month with SEO (\u20b9{:,}/mo)".format(
            PACKAGES_PER_MONTH, MONTHLY_FEE),
    ],
    "not_covered": [
        "Domain & hosting - arranged and paid by the client (we help set up)",
        "Photos, package details & company content (provided by the client)",
        "Live flight / hotel booking engine & GDS API (separate scope)",
        "Paid ad campaigns & any paid plugin / tool / API",
        "Mobile app (Android / iOS) - separate scope",
        "Monthly plan is optional & billed only while active",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-039",
        "package": "Travel Website + Admin",
        "title": "Travel Website + Admin (Lead Capture + SEO)",
        "subtitle": "Tour & travel website with admin panel, lead capture & SEO - plus an optional monthly management plan",
        "price": 9000,
        "price_note": "one-time development  (+  \u20b93,000 / month website management)",
        "timeline": "12-16 working days",
        "summary": (
            "A complete tour & travel website built to capture leads and to "
            "be found on Google. Visitors browse your tour packages with "
            "photos and details and reach you in one tap - an enquiry form "
            "that lands in your email and WhatsApp, a WhatsApp chat button "
            "and an 'Enquire on WhatsApp' button on each package. A full "
            "admin panel lets you add and manage packages and view every "
            "lead in one place. The whole site is built SEO-friendly and "
            "submitted to Google Search Console so your packages can rank and "
            "pull in organic enquiries. The project is a one-time development "
            "fee, with an optional monthly website-management plan under "
            "which we add {} new tour packages every month with SEO and keep "
            "the site fresh.".format(PACKAGES_PER_MONTH)
        ),
        "sections": [
            {
                "heading": "Website pages (frontend)",
                "items": [
                    "Home - hero banner, featured packages, services "
                    "snapshot & clear call-to-action",
                    "About Us - your agency's story and why travellers "
                    "should choose you",
                    "Tour Packages - clean grid with photos, duration & "
                    "highlights, browsable by destination / type",
                    "Package detail - photo gallery, itinerary highlights, "
                    "inclusions and an enquiry button",
                    "Services, gallery and supporting pages as needed",
                    "Contact Us - enquiry form, WhatsApp & call buttons, "
                    "address and Google Map",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Lead capture",
                "items": [
                    "Enquiry form capturing name, phone, travel dates, "
                    "destination / package and message",
                    "Submissions delivered to your email and WhatsApp, so no "
                    "booking enquiry is missed",
                    "Spam protection on the form to keep junk enquiries out",
                    "Floating WhatsApp click-to-chat button on every page",
                    "'Enquire on WhatsApp' button on each package (subject "
                    "pre-filled) + click-to-call button",
                    "All leads also stored in the admin panel with details",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard overview",
                    "Add / edit / delete tour packages with image upload",
                    "Manage categories, destinations and featured packages",
                    "Leads inbox - every enquiry captured with package "
                    "context",
                    "Homepage & banner management",
                    "SEO meta (title / description) editable per package & "
                    "page",
                ],
            },
            {
                "heading": "SEO setup & delivery",
                "items": [
                    "On-page SEO across the site - titles, meta "
                    "descriptions, headings, clean URLs and image alt text",
                    "Google Search Console set up, ownership verified and "
                    "sitemap submitted for indexing",
                    "XML sitemap generated covering all pages",
                    "Fast-loading, mobile-first build tested across major "
                    "browsers and devices",
                    "Deployment and help connecting your domain & hosting",
                    "Google Analytics setup for traffic & lead tracking",
                ],
            },
            {
                "heading": "Monthly website management  (\u20b93,000 / month, optional)",
                "items": [
                    "Add {} new tour packages every month with photos, "
                    "details and SEO-optimised content".format(
                        PACKAGES_PER_MONTH),
                    "On-page SEO for each new package - titles, meta, "
                    "headings, clean URLs, internal links & alt text",
                    "Sitemap updated and new pages submitted to Search "
                    "Console for indexing",
                    "Content & banner updates and general upkeep of the site",
                    "Monthly summary of packages added, indexing & lead "
                    "activity",
                    "Billed monthly and only while the plan is active - start "
                    "or pause anytime",
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
    "payment": "Development: 40% advance to start, 30% midway, 30% on delivery. "
               "Monthly management: \u20b93,000 / month, payable in advance.",
    "notes": [
        "All prices are in Indian Rupees (INR). \u20b99,000 is a one-time development fee for the website & admin panel.",
        "The monthly website-management plan is \u20b93,000 / month and is optional; it is billed in advance and only while active - you can start or pause it anytime.",
        "The monthly plan covers adding {} new tour packages each month with on-page SEO, plus content upkeep; additional packages or pages beyond this are quoted separately.".format(PACKAGES_PER_MONTH),
        "Domain and hosting are arranged and paid for by the client directly; we will help set them up and connect them.",
        "Package photos, itineraries and company content are provided by the client.",
        "On-page SEO and Search Console setup help your pages become eligible to rank; search rankings depend on Google and competition and cannot be guaranteed.",
        "Live flight / hotel booking engines, GDS APIs, paid ad campaigns and a mobile app are a separate scope.",
        "Timelines begin once the content, logo and advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
