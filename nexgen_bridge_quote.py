"""
Bhama Vision - NexGen Bridge website quotation content.

A multi-section business platform website with basic pages plus dedicated
modules for Events & Exhibitions (past + a countdown landing for upcoming),
Delegation Trips with packages (price, inclusions & exclusions), an Investors
& Funding section (invest / raise funds forms), a Partnership section
(partner / associate applications) and Case Studies - all managed from a
full admin panel.

Reuses the Bhama Vision quotation renderer:

    python3 build_nexgen_bridge_quote.py

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
    "company": "NexGen Bridge",
    "note": "Events, delegation, investor & partnership platform with admin panel",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Modern, responsive multi-section website",
        "Basic pages - Home, About, Services, Contact",
        "Events & Exhibitions with upcoming (countdown) & past archive",
        "Delegation Trips with packages (price, inclusions & exclusions)",
        "Investors & Funding section with invest / raise-funds forms",
        "Partnership section with partner / associate application forms",
        "Case Studies section & full admin panel to manage everything",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Content, images & documents (provided by the client)",
        "Online payments / ticketing & payment gateway",
        "Investor KYC / legal verification & agreements",
        "Mobile app (Android / iOS) - separate scope",
        "Ongoing marketing / SEO and any paid plugin or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-022",
        "package": "Business Platform + Admin",
        "title": "NexGen Bridge Website",
        "subtitle": "Events, delegation trips, investors, partnerships & case studies with a full admin panel",
        "price": 13000,
        "price_note": "one-time (design & development)",
        "timeline": "22-30 working days",
        "summary": (
            "A modern, multi-section platform website for NexGen Bridge. "
            "Alongside the essential pages, it brings together everything you "
            "run: an Events & Exhibitions module with a striking countdown "
            "landing page for the next event and an archive of past ones; "
            "Delegation Trips presented as packages with clear pricing, "
            "inclusions and exclusions; an Investors & Funding section where "
            "people can apply to invest or to raise funds through dedicated "
            "forms; a Partnership section for partners, associates and others "
            "to apply; and a Case Studies showcase. A full admin panel lets "
            "your team manage every section, form submission and piece of "
            "content without any coding."
        ),
        "sections": [
            {
                "heading": "Basic pages (frontend)",
                "items": [
                    "Home - hero, highlights of events, trips, investment & "
                    "partnership calls-to-action",
                    "About Us - who you are, mission / vision & team",
                    "Services / What we do overview",
                    "Contact Us - enquiry form, WhatsApp & call, address & "
                    "Google Map",
                    "Responsive design across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Events & Exhibitions",
                "items": [
                    "Upcoming event landing page with a live countdown timer "
                    "to the next event",
                    "Event details - date, venue, agenda, speakers / "
                    "exhibitors, gallery & register / enquire",
                    "Past events archive with photos, recap & outcomes",
                    "Listing with filters (upcoming / past, category, year)",
                    "Add / edit events from the admin panel (auto moves to "
                    "'past' after the date)",
                ],
            },
            {
                "heading": "Delegation Trips (packages)",
                "items": [
                    "Trips shown as packages with cover image, overview & "
                    "itinerary",
                    "Each package with price, what's included & what's "
                    "excluded (clearly listed)",
                    "Dates / duration, destination highlights & enquiry / "
                    "apply button",
                    "Manage all packages & their inclusions from the admin "
                    "panel",
                ],
            },
            {
                "heading": "Investors & Funding",
                "items": [
                    "Section explaining investment opportunities & how it "
                    "works",
                    "'Want to invest' form - capture investor interest & "
                    "details",
                    "'Looking for funds' form - for those seeking investment "
                    "/ funding",
                    "Submissions saved and viewable in the admin panel with "
                    "email / WhatsApp notification",
                ],
            },
            {
                "heading": "Partnership",
                "items": [
                    "Content explaining partner / associate / collaboration "
                    "options",
                    "Application form with type selection (partner, "
                    "associate, other)",
                    "Supporting content, benefits & FAQs",
                    "All applications captured in the admin panel for "
                    "follow-up",
                ],
            },
            {
                "heading": "Case Studies",
                "items": [
                    "Showcase of past work / success stories in a clean grid",
                    "Case study detail - challenge, approach, results & "
                    "images",
                    "Filter by category / industry",
                    "Add / edit case studies from the admin panel",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard overview",
                    "Manage events & exhibitions (upcoming / past, countdown "
                    "date, gallery)",
                    "Manage delegation trip packages, pricing & "
                    "inclusions / exclusions",
                    "View & manage all form submissions - investors, funding, "
                    "partnership & contact",
                    "Manage case studies, pages, banners & menus",
                    "Manage basic settings - WhatsApp, address, contact & "
                    "social links",
                    "Export / mark leads and basic email / WhatsApp "
                    "notifications",
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
        "All content - text, images, event details, trip packages, case studies and documents - is provided by the client; a demo set is added at launch.",
        "Forms (invest, funding, partnership, contact) capture leads into the admin panel; online payments / ticketing and payment gateway are not included.",
        "Investor KYC, legal verification and any agreements are handled by the client and are outside this scope.",
        "A mobile app is separate scope.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
