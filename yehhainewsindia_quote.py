"""
Bhama Vision - Yeh Hai News India news website quotation content.

A modern, fast news / media website with a full admin panel (CMS) to
publish and manage articles, and a multi-language reading experience -
Gujarati (default), English and Hindi.

Reuses the Bhama Vision quotation renderer:

    python3 build_yehhainewsindia_quote.py

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
    "company": "Yeh Hai News India",
    "note": "Multi-language news website with admin panel (CMS)",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Modern, fast, responsive news website",
        "Full admin panel (CMS) to publish & manage articles",
        "Categories, breaking news, featured & trending sections",
        "Language switch - Gujarati (default), English & Hindi",
        "Reporter / author accounts with roles",
        "Search, related articles, images & video embeds",
        "Basic on-page SEO, sitemap & social sharing",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Automatic machine translation of article text (see notes)",
        "News content, articles, images & videos (provided by the client)",
        "Paid subscriptions / paywall & payment gateway",
        "Mobile app (Android / iOS) - separate scope",
        "Ongoing content entry, marketing / SEO and any paid API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-019",
        "package": "News Website + Admin",
        "title": "Yeh Hai News India Website",
        "subtitle": "Multi-language news portal (Gujarati default, English & Hindi) with a full admin panel",
        "price": 9000,
        "price_note": "one-time (design & development)",
        "timeline": "18-25 working days",
        "summary": (
            "A modern, fast news portal for Yeh Hai News India where readers "
            "browse the latest stories by category, read breaking, featured "
            "and trending news, and switch the site language between "
            "Gujarati (default), English and Hindi. A full admin panel (CMS) "
            "lets your team publish and manage articles - with images, "
            "videos, categories and tags - and control what appears on the "
            "homepage. Reporters can be given their own logins with roles. "
            "The site is responsive, SEO-friendly and built to handle a "
            "growing library of news."
        ),
        "sections": [
            {
                "heading": "Reader-facing website (frontend)",
                "items": [
                    "Modern, responsive news design - homepage with breaking "
                    "ticker, featured, latest & trending",
                    "Category & sub-category pages (e.g. National, Gujarat, "
                    "Politics, Sports, Business, Entertainment)",
                    "Article page - title, cover image, body, author, date, "
                    "gallery & video embeds",
                    "Language switch on every page: Gujarati (default), "
                    "English, Hindi",
                    "Search, tags, related & most-read articles",
                    "Social sharing (WhatsApp, Facebook, X) & click-to-share",
                    "Photo gallery / video sections and web-story style posts",
                    "About, contact (with form) and policy pages",
                ],
            },
            {
                "heading": "Language & translation",
                "items": [
                    "Site interface (menus, labels, buttons) in Gujarati, "
                    "English & Hindi",
                    "Gujarati set as the default language on first visit",
                    "One-tap language switch that remembers the reader's "
                    "choice",
                    "Each article supports Gujarati / English / Hindi "
                    "versions entered from the admin panel",
                    "Optional: connect a translation API (e.g. Google) to "
                    "auto-draft other languages for the editor to review "
                    "(API billed to the client)",
                ],
            },
            {
                "heading": "Admin panel / CMS (backend)",
                "items": [
                    "Secure login with dashboard (views, latest posts, "
                    "drafts)",
                    "Create / edit / publish / schedule articles with a rich "
                    "text editor",
                    "Enter article content per language (Gujarati / English "
                    "/ Hindi)",
                    "Manage categories, tags, breaking-news & featured flags",
                    "Media library for images & videos",
                    "Author / reporter accounts with roles (admin, editor, "
                    "reporter)",
                    "Homepage & menu management, plus basic SEO meta per "
                    "article",
                    "Comments / enquiry moderation (if enabled)",
                ],
            },
            {
                "heading": "Performance & SEO",
                "items": [
                    "Fast-loading, mobile-first pages built for news traffic",
                    "SEO-friendly URLs, meta tags, sitemap & structured data "
                    "for articles",
                    "Social preview cards for shared links",
                    "Google Analytics / Search Console ready",
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
        "The site supports Gujarati (default), English and Hindi; the interface is fully translated and each article can be published in these languages from the admin panel.",
        "Article-text translation is entered by your team; if fully automatic machine translation is required, a translation API can be integrated and is billed to the client.",
        "News content - articles, images and videos - is provided and entered by the client (an initial demo set is added at launch).",
        "Paywall / paid subscriptions, payment gateway and a mobile app are separate scope.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
