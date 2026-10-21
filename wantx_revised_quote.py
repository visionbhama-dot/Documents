"""
Bhama Vision - WantX revised budget quotation content.

Revision of the original WantX Complete Platform quotation
(BV-Q-2026-WX1, Rs 75,000). The build has turned out more technically
demanding and time-consuming than first scoped, so the budget is revised
upward by 30%:

    Original (base) budget      75,000
    Revision (+30%)            +22,500
    Revised total               97,500   (excl. GST)

    Received against base      -52,500   (30,000 + 22,500)
    Final payment due now       45,000 + 18% GST = 53,100
      = base balance            22,500
      + revision                22,500

Reuses the Bhama Vision quotation renderer:

    python3 build_wantx_revised_quote.py

Edit price, features, client or terms below, then re-run.
"""

# ---------------------------------------------------------------------------
# Budget maths - single source of truth for the numbers quoted below.
# ---------------------------------------------------------------------------
ORIGINAL_BUDGET = 75000
UPLIFT_PERCENT = 30
UPLIFT_AMOUNT = ORIGINAL_BUDGET * UPLIFT_PERCENT // 100       # 22,500
REVISED_TOTAL = ORIGINAL_BUDGET + UPLIFT_AMOUNT               # 97,500

# Two part payments already received, both against the base price.
RECEIVED_1 = 30000
RECEIVED_2 = 22500
ALREADY_RECEIVED = RECEIVED_1 + RECEIVED_2                    # 52,500

# What is left: the unpaid part of the base price plus the revision.
BASE_BALANCE = ORIGINAL_BUDGET - ALREADY_RECEIVED             # 22,500
DUE_NOW = BASE_BALANCE + UPLIFT_AMOUNT                        # 45,000

GST_PERCENT = 18
GST_ON_DUE_NOW = DUE_NOW * GST_PERCENT // 100                 # 8,100
PAYABLE_NOW = DUE_NOW + GST_ON_DUE_NOW                        # 53,100

# This is the final payment - nothing remains after it.
BALANCE_AFTER = REVISED_TOTAL - ALREADY_RECEIVED - DUE_NOW    # 0


def _r(n):
    """Format an amount the same way the renderer does, for use in text."""
    return "Rs {:,}".format(int(n))


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
    "name": "WantX (OPC) Private Limited",
    "company": "WantX (OPC) Private Limited",
    "note": "WantX reverse marketplace - revised budget",
}

# Scope card shown on the quotation (two columns) - carried over from the
# original WantX quotation so the delivery boundary stays unchanged.
REQUIREMENTS = {
    "title": "Scope & requirements",
    "left_label": "Delivered by Bhama Vision",
    "right_label": "On client's side (third-party)",
    "covered": [
        "Complete UI/UX design & development of every panel listed",
        "Database design and all data models",
        "Integration of the third-party services listed alongside",
        "Deployment to the client's hosting / server + handover",
        "Testing and bug fixing before launch",
        "Source code, documentation and a handover walkthrough",
        "1 year of support for bugs & non-functional issues",
    ],
    "not_covered": [
        "Domain and web hosting / cloud server (and its monthly cost)",
        "AI / LLM API subscription & usage charges for the chat assistant "
        "(e.g. OpenAI / AWS Bedrock)",
        "Amazon Associates account and affiliate-program approval",
        "Maps / geolocation API keys & usage (e.g. Google Maps)",
        "SMS / OTP verification service subscription",
        "WhatsApp Business API (if WhatsApp entry is required)",
        "Payment gateway account and its transaction fees",
        "App Store / Play Store developer accounts (if mobile apps are added)",
        "Any other paid API, plugin or third-party subscription",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-WX3",
        "package": "Complete Platform - Revised",
        "title": "WantX Reverse Marketplace",
        "subtitle": "Revised budget - supersedes quotation BV-Q-2026-WX1",
        "price": REVISED_TOTAL,
        "price_note": "revised total, excl. GST (75,000 + 30%)",
        "timeline": "As per the revised project plan",
        "summary": (
            "This is a revised quotation for the WantX reverse-marketplace "
            "platform, replacing our earlier quotation BV-Q-2026-WX1 of "
            + _r(ORIGINAL_BUDGET) + ". As the build has progressed, several "
            "parts of the platform have proved significantly more demanding "
            "than they appeared at the time of first scoping - in particular "
            "the natural-language understanding that reads a customer's want, "
            "the live matching and geo-search that puts the right businesses "
            "in front of them, the multi-user business panel with roles, and "
            "the Amazon affiliate integration. These need more engineering "
            "time, more paid infrastructure and a much longer testing cycle "
            "than the original estimate allowed for. We are therefore "
            "revising the budget upward by " + str(UPLIFT_PERCENT) + "%, "
            "taking the total to " + _r(REVISED_TOTAL) + " excluding GST. "
            "Of this, " + _r(ALREADY_RECEIVED) + " has already been received "
            "against the base price (" + _r(RECEIVED_1) + " plus "
            + _r(RECEIVED_2) + "), leaving a final payment of "
            + _r(DUE_NOW) + " - the " + _r(BASE_BALANCE) + " still "
            "outstanding on the base price together with the "
            + _r(UPLIFT_AMOUNT) + " revision. With "
            + str(GST_PERCENT) + "% GST that comes to "
            + _r(PAYABLE_NOW) + ", and it clears the project in full. "
            "The scope, deliverables and support commitment remain exactly as "
            "agreed; only the commercials and schedule change."
        ),
        "sections": [
            {
                "heading": "Revised budget",
                "items": [
                    "Original agreed budget (BV-Q-2026-WX1): "
                    + _r(ORIGINAL_BUDGET),
                    "Revision for added engineering effort (+"
                    + str(UPLIFT_PERCENT) + "%): + " + _r(UPLIFT_AMOUNT),
                    "Revised project total: " + _r(REVISED_TOTAL)
                    + " (excluding GST)",
                    "GST is charged at " + str(GST_PERCENT)
                    + "% on each invoice raised against this quotation",
                ],
            },
            {
                "heading": "Payment position & amount due now",
                "items": [
                    "Received against the base price: "
                    + _r(ALREADY_RECEIVED) + " (" + _r(RECEIVED_1) + " + "
                    + _r(RECEIVED_2) + ", both receipted)",
                    "Still outstanding on the base price: "
                    + _r(BASE_BALANCE),
                    "Plus the " + str(UPLIFT_PERCENT) + "% revision: "
                    + _r(UPLIFT_AMOUNT),
                    "Final payment due now: " + _r(DUE_NOW) + " + "
                    + str(GST_PERCENT) + "% GST " + _r(GST_ON_DUE_NOW)
                    + " = " + _r(PAYABLE_NOW) + " payable",
                    "This is the final payment - nothing further is due after "
                    "it, and it takes the project to " + _r(REVISED_TOTAL)
                    + " paid in full (excluding GST)",
                    "Payment can be made by bank transfer or UPI - details and "
                    "QR are on this quotation",
                ],
            },
            {
                "heading": "Why the budget is being revised",
                "items": [
                    "Natural-language understanding - reading a customer's "
                    "want in plain language and reliably extracting category, "
                    "attributes, budget and location needs far more prompt "
                    "engineering, tuning and fallback handling than a simple "
                    "keyword match, plus paid AI/LLM usage on every request",
                    "Live matching & geo-search - ranking nearby, relevant "
                    "businesses in real time requires a proper search and "
                    "geo-indexing layer, which is heavier to build and more "
                    "expensive to run than a plain database query",
                    "Multi-user business panel - organisation onboarding with "
                    "Owner / Manager / Staff / Viewer roles means permission "
                    "checks on every screen and action, effectively a second "
                    "application alongside the customer app",
                    "Category-driven dynamic fields - each category showing "
                    "only its own relevant fields needs a configurable schema "
                    "engine rather than fixed forms, and it drives the "
                    "listing, matching and admin screens alike",
                    "Amazon affiliate integration - API rate limits force a "
                    "caching layer, and the routing logic between business "
                    "listings and affiliate products added unforeseen work",
                    "Extended testing cycle - verification flows, payments, "
                    "roles and real-time matching across mobile, tablet and "
                    "desktop take a considerably longer QA pass than first "
                    "estimated",
                ],
            },
            {
                "heading": "Scope being delivered (unchanged)",
                "items": [
                    "Customer app - chat-based want posting, intent "
                    "understanding, live matched listings & competing offers, "
                    "comparison filters, nearby-first results, saved wants, "
                    "in-app messaging, ratings and notifications",
                    "Business panel - verified business login, organisation "
                    "onboarding, multi-user roles, KPI dashboard, "
                    "category-driven listings, incoming leads, offer builder "
                    "with templates, listing management and analytics",
                    "Affiliate / Amazon module - auto-fetch of products for "
                    "everyday-goods queries, affiliate tagging, product cards "
                    "in chat, caching and listing-vs-affiliate routing",
                    "Admin panel - categories & dynamic field schema, "
                    "business verification, listing & content moderation, "
                    "affiliate settings, platform analytics, users, plans and "
                    "payouts",
                    "Design & technical - responsive UI/UX across mobile, "
                    "tablet & desktop, secure authentication and roles, "
                    "search & geo-matching, deployment and full handover",
                    "Support - 1 year of bug fixing and non-functional issue "
                    "support after go-live",
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
    "payment": (
        _r(ALREADY_RECEIVED) + " already received against the base price. "
        "Final payment of " + _r(DUE_NOW) + " + " + str(GST_PERCENT)
        + "% GST (" + _r(PAYABLE_NOW) + ") is due now, after which nothing "
        "further is payable."
    ),
    "notes": [
        "This revised quotation supersedes quotation BV-Q-2026-WX1 of "
        + _r(ORIGINAL_BUDGET) + ". The revised project total is "
        + _r(REVISED_TOTAL) + ", excluding GST.",
        "The " + str(UPLIFT_PERCENT) + "% revision covers additional "
        "engineering effort, paid infrastructure and an extended testing "
        "cycle on the work already agreed - it does not add new features to "
        "the scope.",
        _r(ALREADY_RECEIVED) + " has been received against the base price ("
        + _r(RECEIVED_1) + " plus " + _r(RECEIVED_2) + "). The final payment "
        "of " + _r(DUE_NOW) + " is the " + _r(BASE_BALANCE) + " outstanding "
        "on the base price plus the " + _r(UPLIFT_AMOUNT) + " revision.",
        "GST is charged at " + str(GST_PERCENT) + "% on each invoice raised "
        "against this quotation. " + _r(DUE_NOW) + " plus GST of "
        + _r(GST_ON_DUE_NOW) + ", i.e. " + _r(PAYABLE_NOW) + ", is payable "
        "now and completes the project payment.",
        "All amounts are in Indian Rupees (INR) and are one-time for the "
        "design & development work quoted.",
        "All third-party subscriptions (hosting, domain, AI/LLM API, Amazon "
        "Associates, maps/geolocation, SMS/OTP, WhatsApp API, payment "
        "gateway) are arranged and paid for by the client directly.",
        "AI assistant and other API usage are recurring costs billed by the "
        "provider to the client based on usage.",
        "The revised delivery schedule is confirmed alongside this revision "
        "and runs from receipt of the amount now due.",
        "1 year support covers bugs & errors only (things that stop "
        "working). It does not cover new features, content changes or "
        "redesigns, which are quoted separately.",
    ],
}
