"""
Bhama Vision - paid advertisement service quotation content.

A monthly paid-ads management service: 5 campaigns, research, static
creatives, optimization and monthly reporting. Reuses the Bhama Vision
quotation renderer:

    python3 build_paid_ads_quote.py

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
    "note": "Paid advertisement management service",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Setup & management of 5 ad campaigns",
        "5 custom static ad creatives (images / graphics)",
        "Audience, keyword & competitor research",
        "Campaign optimization every other day (or more often when needed)",
        "Monthly performance report with insights",
        "Conversion / pixel tracking setup & monitoring",
    ],
    "not_covered": [
        "Ad budget / ad spend - set and paid by the client directly",
        "Video creatives (this package is static creatives only)",
        "Any extra campaigns or creatives beyond the 5 included",
        "Website / landing page design or changes",
        "Product photography or raw content",
        "Ad platform / account fees and any paid third-party tools",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-004",
        "package": "Paid Ads - Monthly",
        "title": "Paid Advertisement Service",
        "subtitle": "5 campaigns, research, creatives, optimization & monthly reporting",
        "price": 8000,
        "price_note": "per month (management fee - ad budget separate)",
        "timeline": "Monthly (ongoing)",
        "summary": (
            "A complete monthly paid-advertising management service. We plan, "
            "set up and run 5 ad campaigns for you, design the creatives, "
            "optimize the campaigns every other day for better results, and "
            "send you a clear performance report every month. The advertising "
            "budget (the money actually spent on ads) is set and paid by you "
            "directly to the ad platform - our fee covers the management, "
            "creatives and optimization work only."
        ),
        "sections": [
            {
                "heading": "What we will provide",
                "items": [
                    "Research first: audience, keyword & competitor research "
                    "before we launch",
                    "Setup & management of 5 ad campaigns on your chosen "
                    "platforms (e.g. Meta / Google)",
                    "5 custom static ad creatives (image / graphic ads) - "
                    "no videos in this package",
                    "Ongoing optimization every other day, or more often when "
                    "needed - adjusting audiences, placements, bids & budgets",
                    "A/B testing and refinements within the 5 creatives",
                    "Conversion / pixel tracking setup and monitoring",
                    "One detailed performance report each month - reach, "
                    "clicks, spend, results and clear next-step insights",
                ],
            },
            {
                "heading": "Good to know",
                "muted": True,
                "items": [
                    "The ad budget (spend on the platform) is decided and paid "
                    "by you directly - it is not part of this fee.",
                    "This package covers static creatives only; video ads can "
                    "be added separately on request.",
                    "Results depend on budget, product and market - we "
                    "optimize for the best possible outcome.",
                ],
            },
        ],
        "support": REQUIREMENTS,
    },
]

# Terms shown on the closing page of the quotation.
TERMS = {
    "validity_days": 15,
    "payment": "Management fee payable monthly in advance. The ad budget is "
               "paid by the client directly to the ad platform.",
    "notes": [
        "The management fee is in Indian Rupees (INR) and is separate from the ad spend / budget, which the client sets and pays directly to the ad platform.",
        "This package includes 5 static creatives and 5 campaigns; video creatives and additional campaigns/creatives are not included.",
        "Campaign optimization is carried out every other day, or more frequently when required.",
        "Reporting is shared once a month. Ad results depend on budget, product and market; specific numbers are not guaranteed.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
