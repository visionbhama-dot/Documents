"""
Bhama Vision - Ravis Enterprises multi-domain website quotation content.

A comprehensive proposal for three dynamic websites (ravis.in, jbpower.in,
jbsolar.in), each with its own dynamic CMS backend, domain + zero-loss email
migration, WhatsApp integration, an AI chatbot / lead assistant, and a
modern Vercel + Supabase hosting stack for a fast, responsive experience.

Pricing is shown as a per-website breakdown, totalling Rs. 47,000 one-time
for all three websites and their CMS backends. AI usage and hosting are
third-party recurring costs.

Reuses the Bhama Vision quotation renderer:

    python3 build_ravis_multidomain_quote.py

Edit price, features, client or terms below, then re-run.
"""

# ---------------------------------------------------------------------------
# Price breakdown (kept in one place so the breakdown section, the price box
# and the terms stay in sync).
# ---------------------------------------------------------------------------
BASE_PRICE = 15000           # base price per website
COMPLEX_UPLIFT = 2000        # uplift for the more complex website (jbsolar.in)

PRICE_RAVIS = BASE_PRICE                      # 15,000
PRICE_JBPOWER = BASE_PRICE                    # 15,000
PRICE_JBSOLAR = BASE_PRICE + COMPLEX_UPLIFT   # 17,000 (more complex)
TOTAL_DEV = PRICE_RAVIS + PRICE_JBPOWER + PRICE_JBSOLAR   # 47,000


def _r(n):
    return "\u20b9{:,}".format(int(n))


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
    "company": "Ravis Enterprises Pvt Ltd",
    "note": "3 dynamic websites + CMS backends, migration, AI & WhatsApp, Vercel + Supabase",
}

# Clear includes / excludes shown as two columns on the quotation.
REQUIREMENTS = {
    "title": "What's included & what's a third-party cost",
    "left_label": "Included in this package",
    "right_label": "Third-party / not included",
    "covered": [
        "3 fully dynamic websites - ravis.in, jbpower.in, jbsolar.in",
        "3 dynamic CMS backends (edit content without coding)",
        "Domain connection / DNS setup for all 3 (transfer optional)",
        "Zero-loss email migration (Google Workspace / existing emails)",
        "WhatsApp chat widget + automated lead notifications (email/WhatsApp)",
        "AI chatbot / lead assistant - integration & setup",
        "Vercel + Supabase deployment (fast & responsive) with SSL",
        "Basic on-page SEO & mobile-first responsive build",
    ],
    "not_covered": [
        "AI usage / API cost - third-party, billed by the AI provider",
        "Vercel / Supabase paid tiers - billed by the provider as usage grows",
        "WhatsApp Business API provider fees (if official API is used)",
        "Domain renewal & Google Workspace subscription fees",
        "Product photos, content, videos & copywriting (client-provided)",
        "AMC / ongoing IT support retainer (optional - quoted separately)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-047",
        "package": "3 Websites + CMS Backends",
        "title": "Ravis Enterprises - Multi-Domain Website Project",
        "subtitle": "3 dynamic websites + 3 CMS backends, migration, WhatsApp & AI integration on a Vercel + Supabase stack",
        "price": TOTAL_DEV,
        "price_note": "one-time development",
        "timeline": "4-6 weeks (all three sites)",
        "summary": (
            "A complete, long-term build for your three business domains - "
            "ravis.in (B2B wholesale), jbpower.in (power electronics) and "
            "jbsolar.in (solar) - delivered as three fully dynamic websites, "
            "each with its own easy-to-use CMS backend so your team can "
            "update content without touching code. We migrate the domains and "
            "move your business emails with zero data loss and no downtime, "
            "add a WhatsApp chat widget with automated lead notifications and "
            "an AI chatbot / lead assistant that answers basic solar & power "
            "queries 24/7 and captures leads. Everything is built on a modern "
            "Vercel + Supabase stack (database included) for a fast, "
            "responsive, scalable experience with SSL and basic SEO. The "
            "price below is a one-time development fee with a clear "
            "per-website breakdown; AI usage and hosting are third-party "
            "recurring costs billed directly by the providers."
        ),
        "sections": [
            {
                "heading": "ravis.in - Ravis Enterprises (B2B wholesale)",
                "items": [
                    "Clean, corporate B2B layout for dealers & wholesale "
                    "buyers",
                    "Wholesale solar product range with authorized "
                    "distributorships (APS & Velox) highlighted",
                    "Dynamic CMS backend to manage products, pages & enquiries",
                    "Dealer / wholesale enquiry forms with lead capture",
                    "Company profile, certifications & contact pages",
                ],
            },
            {
                "heading": "jbpower.in - JB Power Electronics (service-oriented)",
                "items": [
                    "Service-oriented layout for end-users & commercial "
                    "clients",
                    "Product sections - Online/Offline UPS, inverters, "
                    "batteries, servo stabilizers, transformers & AMCs",
                    "Dynamic CMS backend to manage products, services & "
                    "enquiries",
                    "Service / AMC enquiry forms with lead capture",
                    "About, service area & contact pages",
                ],
            },
            {
                "heading": "jbsolar.in - JB Solar",
                "items": [
                    "Lead-generation-focused layout for residential "
                    "(PM Surya Ghar), commercial & off-grid clients",
                    "Dynamic project portfolio / gallery for installation "
                    "photos",
                    "Video integration and customer testimonials",
                    "Detailed solar product pages (rooftop, off-grid, "
                    "subsidy schemes)",
                    "Dynamic CMS backend + strong enquiry / subsidy lead "
                    "forms",
                ],
            },
            {
                "heading": "Shared across all three sites",
                "items": [
                    "Dynamic CMS backend per site - add / edit pages, "
                    "products & media without coding",
                    "Floating WhatsApp chat widget, automated welcome "
                    "messages & quick inquiry buttons",
                    "Automated lead notifications by email / WhatsApp when a "
                    "form is submitted",
                    "SSL (https), basic on-page SEO and mobile-first "
                    "responsive design",
                    "Fast page loads and a consistent, modern brand feel",
                ],
            },
            {
                "heading": "Migration & go-live (all 3 domains)",
                "items": [
                    "Secure domain connection / DNS setup for all three "
                    "domains (registrar transfer from GoDaddy optional)",
                    "Zero-loss email migration - Google Workspace (jbpower.in) "
                    "and existing emails (ravis.in) preserved via correct "
                    "MX / DNS",
                    "Uninterrupted business continuity - no email downtime "
                    "during cutover",
                    "SSL issued and verified for every domain",
                    "Post-launch verification of mail flow, forms & pages",
                ],
            },
            {
                "heading": "AI chatbot / lead assistant",
                "items": [
                    "Lightweight AI chatbot to answer basic solar & power "
                    "backup queries 24/7",
                    "Collects lead info (name, phone, location) and routes it "
                    "to your sales team",
                    "Cost-effective approach (open-source / custom wrapper) "
                    "integrated into all sites",
                    "Integration & setup is included in the development fee",
                    "Note: the AI usage / API is a THIRD-PARTY cost, billed "
                    "directly by the AI provider based on usage (client-"
                    "borne).",
                ],
            },
            {
                "heading": "Hosting & tech stack (Vercel + Supabase)",
                "items": [
                    "Frontend hosted on Vercel - a global CDN for fast, "
                    "responsive delivery",
                    "Supabase as the managed database (Postgres) powering the "
                    "dynamic content & CMS",
                    "Scales smoothly from a free tier to paid plans as traffic "
                    "grows",
                    "SSL, automatic deployments and strong uptime out of the "
                    "box",
                    "Note: Vercel / Supabase paid tiers are a THIRD-PARTY "
                    "cost, billed by the provider on the client's account.",
                    "(A unified host like Hostinger can be used instead on "
                    "request; Vercel + Supabase is recommended for speed.)",
                ],
            },
            {
                "heading": "Price breakdown",
                "items": [
                    "ravis.in - B2B wholesale website + CMS backend: "
                    "{}".format(_r(PRICE_RAVIS)),
                    "jbpower.in - power electronics website + CMS backend: "
                    "{}".format(_r(PRICE_JBPOWER)),
                    "jbsolar.in - solar website + CMS backend (gallery, "
                    "video, detailed product pages): "
                    "{}".format(_r(PRICE_JBSOLAR)),
                    "Each website price includes its CMS backend, WhatsApp "
                    "widget + lead notifications, AI chatbot integration, "
                    "domain + zero-loss email migration, SSL, basic SEO and "
                    "Vercel + Supabase deployment.",
                    "Total one-time development (3 websites + 3 backends): "
                    "{}".format(_r(TOTAL_DEV)),
                    "Third-party (not in the above): AI usage / API, Vercel & "
                    "Supabase paid tiers, WhatsApp API fees, domain & email "
                    "subscriptions - billed directly by each provider.",
                    "AMC / IT support retainer: optional, quoted separately "
                    "on request.",
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
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
        "Website development is quoted per website as shown in the price breakdown; the total one-time development for all three websites and their CMS backends is {}.".format(
            _r(TOTAL_DEV)),
        "AI chatbot / lead assistant integration is included; the AI usage / API is a third-party cost billed directly by the AI provider based on usage.",
        "Hosting uses Vercel + Supabase for speed and scalability; their paid tiers are third-party costs billed by the providers on the client's account. A unified host (Hostinger or similar) can be used instead on request.",
        "Domain renewal, Google Workspace / email subscriptions and any official WhatsApp Business API provider fees are paid by the client directly.",
        "Email migration is carried out with zero data loss and no downtime; mailboxes remain on Google Workspace / the client's provider and are preserved via correct MX / DNS.",
        "Product photos, content, videos and copywriting are provided by the client and managed via the CMS backends.",
        "An Annual Maintenance Contract (AMC) / ongoing IT support retainer is available and quoted separately on request.",
        "Timelines begin once content, access and the advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
