"""
Bhama Vision - real estate project website + monthly social media ads.

A one-time real estate project website (with a backend admin panel) plus an
ongoing monthly service to manage 5 social media ad campaigns. Two fees:
a one-time development fee and a monthly ads management fee. The ad budget
(spend) is set and paid by the client directly to the platform. Reuses the
Bhama Vision quotation renderer:

    python3 build_real_estate_ads_quote.py

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

CLIENT = {
    "name": "Prospective Client",
    "company": "Confidential",
    "note": "Real estate project website + admin panel + monthly social media ad campaigns",
}

REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive real estate project website + backend admin panel",
        "Project & unit listings with photos, floor plans & details",
        "Location / map, amenities & enquiry (lead) capture",
        "WhatsApp integration (click-to-chat button)",
        "Monthly management of 5 social media ad campaigns (Meta - FB & Instagram)",
        "5 custom static ad creatives + research, optimization & monthly report",
        "Conversion / pixel tracking setup & monitoring",
    ],
    "not_covered": [
        "Ad budget / ad spend - set and paid by the client directly to the platform (separate, and will differ by month / goal)",
        "Domain - arranged and paid by the client (not included)",
        "Hosting - arranged and paid by the client (not included)",
        "Video creatives, and any extra campaigns / creatives beyond the 5 included",
        "Project photos & content (provided by the client)",
        "Ad platform / account fees and any paid third-party tools",
    ],
}

# ---------------------------------------------------------------------------
# The quotation.
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-060",
        "package": "Website + Admin + Monthly Ads",
        "title": "Real Estate Project Website + Social Media Ads",
        "subtitle": "Project website with admin panel, plus monthly management of 5 social media ad campaigns",
        "price": 9000,
        "price_note": "one-time development  \u00b7  + \u20b98,000/month ads (budget separate)",
        "timeline": "10-14 working days for the website; ads run monthly (ongoing)",
        "summary": (
            "A complete package for a real estate project: a professional, "
            "responsive project website with a backend admin panel, plus an "
            "ongoing monthly service that plans and runs your social media "
            "advertising. Buyers explore the project, units, floor plans and "
            "amenities and send enquiries that reach you directly, while you "
            "manage listings and leads from one dashboard. Each month we set "
            "up and optimise 5 ad campaigns on Meta (Facebook & Instagram) "
            "with custom creatives and a performance report. There are two "
            "fees: a one-time development fee of \u20b99,000 for the website & "
            "admin, and \u20b98,000 per month for ad campaign management. The "
            "ad budget (the money actually spent on ads) is set and paid by "
            "you directly to the platform - it is separate from our fee and "
            "will differ depending on your monthly goals."
        ),
        "sections": [
            {
                "heading": "Project website (frontend)",
                "items": [
                    "Home / landing page with hero banner, highlights & "
                    "clear calls-to-action",
                    "Project overview with configurations, pricing bands & "
                    "status",
                    "Unit / floor-plan listings with images & key details",
                    "Image & video gallery of the project",
                    "Location section with map, connectivity & nearby "
                    "landmarks",
                    "Amenities & specifications section",
                    "Enquiry / site-visit request form that reaches you "
                    "directly",
                    "WhatsApp click-to-chat for quick enquiries",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Backend admin panel",
                "items": [
                    "Secure admin login",
                    "Add, edit & remove projects, units & floor plans",
                    "Upload project photos, brochures & set status / pricing",
                    "View and manage enquiries / leads",
                    "Homepage banner & highlights management",
                    "A short walkthrough so you are comfortable running it",
                ],
            },
            {
                "heading": "Social media ad campaigns (monthly)",
                "items": [
                    "Audience, competitor & area research before launch",
                    "Setup & management of 5 ad campaigns on Meta "
                    "(Facebook & Instagram)",
                    "5 custom static ad creatives (image / graphic ads)",
                    "Ongoing optimization every other day - audiences, "
                    "placements, bids & budgets",
                    "Lead-form / conversion & pixel tracking setup and "
                    "monitoring",
                    "One detailed performance report each month with "
                    "next-step insights",
                ],
            },
            {
                "heading": "Investment breakdown",
                "items": [
                    "One-time website + admin development: \u20b99,000 "
                    "(one-time)",
                    "Ad campaign management: \u20b98,000 per month "
                    "(5 campaigns)",
                    "Ad budget / ad spend: set & paid by you directly to the "
                    "platform - separate from our fee and will differ by "
                    "month / goal",
                ],
            },
            {
                "heading": "Good to know",
                "muted": True,
                "items": [
                    "The ad budget (spend on the platform) is decided and "
                    "paid by you directly - it is not part of the management "
                    "fee and will vary month to month.",
                    "The ads package covers static creatives only; video ads "
                    "can be added separately on request.",
                    "Ad results depend on budget, project and market - we "
                    "optimize for the best possible outcome; specific numbers "
                    "are not guaranteed.",
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
    "payment": ("Website: 50% advance to start, 50% on delivery. Ads management "
                "fee: \u20b98,000/month payable monthly in advance. The ad budget "
                "is paid by the client directly to the ad platform."),
    "notes": [
        "All prices are in Indian Rupees (INR). The website fee is one-time; the ad campaign management fee is \u20b98,000 per month (ongoing).",
        "The ad budget / ad spend is NOT included - it is set and paid by the client directly to the ad platform, and will differ month to month depending on goals.",
        "The ads package includes 5 campaigns and 5 static creatives per month; video creatives and any extra campaigns / creatives are not included.",
        "Campaign optimization is carried out every other day, or more often when required; reporting is shared once a month.",
        "Ad results depend on budget, project and market; specific numbers / leads are not guaranteed.",
        "Domain and hosting are NOT included; they are arranged and paid for by the client directly. We will help set them up and connect them.",
        "Project photos, brochures and content are provided by the client.",
        "Either side may pause or stop the monthly ads service with notice before the next monthly cycle.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
