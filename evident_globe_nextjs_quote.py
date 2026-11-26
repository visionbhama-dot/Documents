"""
Bhama Vision - Evident Globe digital agency website quotation (Next.js, Pro).

A premium version of the Evident Globe website, built on Next.js (React) for
top performance and SEO, with an admin panel to manage blogs, advanced
SEO-friendly options, free hosting for 1 year and 1 year of bug & error
support. The domain is arranged by the client (not included).

Reuses the Bhama Vision quotation renderer:

    python3 build_evident_globe_nextjs_quote.py

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
    "company": "Evident Globe",
    "note": "Next.js digital agency website + blog admin (free hosting 1 year, domain not included)",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "High-performance Next.js (React) website",
        "Free hosting for 1 year (from our side)",
        "Admin panel to manage blogs with a rich editor & SEO options",
        "Advanced SEO - SSR / SSG, schema, social cards & auto sitemap",
        "Modern UI with smooth animations & light / dark mode",
        "Services & portfolio sections + lead capture",
        "Enquiry form + WhatsApp & automated email lead notifications",
        "1 year support for any bugs & errors",
    ],
    "not_covered": [
        "Domain - client's (approx \u20b91,000-\u20b91,500 / year)",
        "Hosting renewal from year 2 (approx \u20b91,500 / year)",
        "Content, images & copywriting (provided by the client)",
        "Logo / brand identity design (separate service)",
        "Ongoing SEO / marketing campaigns (separate service)",
        "Mobile app (Android / iOS) - separate scope",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-065",
        "package": "Next.js Website + Admin",
        "title": "Evident Globe - Pro (Next.js)",
        "subtitle": "Premium Next.js digital agency website with a blog admin panel, advanced SEO, free hosting for 1 year & 1 year support (domain not included)",
        "price": 5500,
        "price_note": "one-time (incl. free hosting for 1 year)",
        "timeline": "10-14 working days",
        "summary": (
            "A premium, high-performance version of the Evident Globe website "
            "built on Next.js (React) - the modern framework used by top "
            "agencies for speed, SEO and scalability. Pages load almost "
            "instantly thanks to server-side rendering / static generation "
            "and automatic image optimisation, giving you strong Core Web "
            "Vitals and better Google rankings. The design is sleek and "
            "modern with smooth animations and an optional light / dark mode. "
            "You present your services and portfolio, capture leads through "
            "an enquiry form that reaches your email and WhatsApp with "
            "automated notifications, and publish content from an easy admin "
            "panel with a rich editor and per-post SEO options. It is built "
            "with advanced, future-ready SEO, comes with free hosting for the "
            "first year and 1 year of bug & error support. The domain is "
            "arranged by you (not included), and we help connect it."
        ),
        "sections": [
            {
                "heading": "Built on Next.js - why it's better",
                "items": [
                    "Next.js (React) - the modern, production-grade framework "
                    "used by leading agencies",
                    "Server-side rendering / static generation for "
                    "near-instant page loads",
                    "Automatic image optimisation & code-splitting for strong "
                    "Core Web Vitals",
                    "SEO-first architecture - search engines index the pages "
                    "cleanly",
                    "Scalable, maintainable, component-based codebase ready "
                    "to grow",
                    "Deployed on a fast global CDN with SSL",
                ],
            },
            {
                "heading": "Website pages (frontend)",
                "items": [
                    "Home - animated hero, agency snapshot, services & clear "
                    "call-to-action",
                    "About - your story, team and why clients choose you",
                    "Services - your digital services presented with "
                    "descriptions",
                    "Portfolio / work - projects & case studies showcase",
                    "Blog - articles listing with categories, tags, search & "
                    "featured posts",
                    "Contact - enquiry form, WhatsApp & call buttons, address "
                    "and Google Map",
                    "Modern UI with smooth animations and light / dark mode",
                ],
            },
            {
                "heading": "Blog admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard",
                    "Rich text editor to write, edit, publish & delete posts "
                    "with images",
                    "Organise posts into categories & tags",
                    "Per-post SEO options - title, meta, slug / clean URL, "
                    "social card & alt text",
                    "Manage featured posts and homepage highlights",
                    "View enquiry leads received through the site",
                ],
            },
            {
                "heading": "Advanced SEO & performance",
                "items": [
                    "Server-side rendering / static generation for SEO & "
                    "speed",
                    "Structured data / schema and Open Graph / social share "
                    "cards",
                    "Automatic XML sitemap, robots.txt & clean, canonical "
                    "URLs",
                    "Image optimisation, lazy loading & strong Core Web "
                    "Vitals scores",
                    "Google Analytics & Search Console setup",
                    "Accessibility & mobile-first best practices",
                ],
            },
            {
                "heading": "Lead capture, hosting, support & delivery",
                "items": [
                    "Enquiry / contact form capturing name, phone, service & "
                    "message",
                    "Submissions delivered to your email and WhatsApp with "
                    "automated notifications",
                    "Floating WhatsApp click-to-chat + click-to-call on every "
                    "page",
                    "Free hosting for 1 year from our side with SSL + help "
                    "connecting your domain",
                    "1 year of support for any bugs & errors after launch",
                    "Testing across major browsers and devices before launch",
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
    "payment": "50% advance to start, 50% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
        "The website is built on Next.js (React) for performance and SEO.",
        "Hosting for the first year is free from our side (with SSL).",
        "The domain is NOT included - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Next-year renewal (from year 2 onwards), paid by the client at actuals: domain approx \u20b91,000-\u20b91,500 / year and hosting approx \u20b91,500 / year.",
        "The website is built SEO-friendly; on-page SEO and Search Console setup help the pages become eligible to rank. Rankings depend on Google and competition and cannot be guaranteed; ongoing SEO / marketing is a separate service.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages / features or redesigns.",
        "Text, photos, blog content and images are provided by the client and managed via the admin panel.",
        "Timelines begin once the content, logo and advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
