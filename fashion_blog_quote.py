"""
Bhama Vision - fashion blog website quotation content.

A fashion articles / blogging website with an admin backend, full on-page
SEO options and Google AdSense verification, plus 1 year of error & bug-fix
support. Reuses the Bhama Vision quotation renderer:

    python3 build_fashion_blog_quote.py

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
    "note": "Fashion blog / articles website with admin",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Responsive fashion blog website (7 pages)",
        "Admin backend to manage articles & pages",
        "Full on-page SEO options (editable per article)",
        "Google AdSense verification setup in the backend",
        "Google Search Console setup & indexing",
        "Contact form with submissions in admin",
        "1 year support (errors & bug fixes)",
    ],
    "not_covered": [
        "Domain and hosting (arranged & paid by the client)",
        "Article content, images & written blogs (added by the client)",
        "Google AdSense account approval (Google's decision - not guaranteed)",
        "Ongoing monthly SEO or ad campaigns (separate service)",
        "Online store / payment features",
        "Any paid plugin, tool or API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-010",
        "package": "Blog Website + Admin",
        "title": "Fashion Blog Website",
        "subtitle": "Fashion articles website + admin, full SEO & AdSense verification",
        "price": 3800,
        "price_note": "one-time (design & development)",
        "timeline": "6-10 working days",
        "summary": (
            "A clean, SEO-ready fashion blogging website where you publish "
            "fashion articles and grow an audience. It comes with an admin "
            "backend to write and manage articles and pages, full on-page SEO "
            "options for every article, and Google AdSense verification set up "
            "in the backend so you can start monetising once approved. The "
            "package includes the 7 pages listed and 1 year of error & bug-fix "
            "support."
        ),
        "sections": [
            {
                "heading": "Pages included",
                "items": [
                    "Home page (featured & latest fashion articles)",
                    "Blog page - fashion articles listing with categories",
                    "About page",
                    "Contact us page (with contact form)",
                    "Terms & Conditions",
                    "Privacy Policy",
                    "Disclaimer",
                ],
            },
            {
                "heading": "Backend (admin panel)",
                "items": [
                    "Write, edit, publish & delete fashion articles",
                    "Organise articles into categories",
                    "Per-article SEO fields - meta title, description & URL "
                    "slug",
                    "Google AdSense verification setup (site verification, "
                    "ads.txt & ad code placement)",
                    "Manage page content (about, contact & legal pages)",
                    "View contact-form submissions",
                ],
            },
            {
                "heading": "SEO features",
                "items": [
                    "Full on-page SEO - editable titles, meta tags, headings "
                    "& clean URLs",
                    "XML sitemap and Google Search Console setup & indexing",
                    "Open Graph / social-share tags and article schema",
                    "Image alt tags and basic page-speed optimization",
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
        "We set up Google AdSense verification, but AdSense approval is Google's decision and is not guaranteed.",
        "1 year support covers errors & bug fixes only (things that stop working). It does not cover content changes, new pages/features or redesigns.",
        "Article content, blogs and images are added by the client via the admin panel.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
