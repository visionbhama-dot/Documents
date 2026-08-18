"""
Bhama Vision - feature document content.

A branded, price-free "features & capabilities" document for a
multi-vendor e-commerce platform (Meesho-style) with two apps:
Buyer app + Supplier app, plus an Admin panel and website.

Edit this file, then run:
    python3 build_features.py

Pricing is intentionally left out of this document. When you are ready
to quote, add the numbers in `quotations.py` and run `build_quotes.py`.
"""

# ---------------------------------------------------------------------------
# Company details (shown on the header + footers). Update with your real info.
# ---------------------------------------------------------------------------
COMPANY = {
    "name": "Bhama Vision",
    "tagline": "Websites, apps & AI for growing businesses",
    "email": "info@bhamavision.com",
    "phone": "+91 88606 40250",
    "website": "www.bhamavision.com",
    "location": "India",
}

# Who the document is prepared for. Customer / agency name intentionally
# left generic - update if you want it personalised.
CLIENT = {
    "company": "Prospective Client",
    "note": "Multi-vendor online selling platform",
}

# ---------------------------------------------------------------------------
# Document header meta
# ---------------------------------------------------------------------------
DOCUMENT = {
    "id": "BV-FEAT-2026-001",
    "label": "FEATURE DOCUMENT",
    "title": "Multi-Vendor E-Commerce Platform",
    "subtitle": (
        "A Meesho-style online marketplace - custom coded, full stack, with a "
        "Buyer app, a Supplier (seller) app, an Admin panel and a website."
    ),
    "summary": (
        "This document lists the complete set of features we can design and "
        "build for a custom, full-stack multi-vendor e-commerce platform - the "
        "kind of marketplace where many suppliers list their products and "
        "buyers shop from all of them in one place, similar to Meesho. It is "
        "delivered as two dedicated apps - a Buyer app and a Supplier app - "
        "backed by a powerful Admin panel and an optional web store. Everything "
        "below is custom coded and owned by you; no per-order commission is "
        "charged by us. Pricing and timeline are shared separately once you "
        "confirm which features you want."
    ),
}

# The building blocks that make up the platform (shown as a highlight strip).
PLATFORM = {
    "title": "What the platform includes",
    "items": [
        "Buyer app - Android & iOS (React Native / Flutter), for shoppers",
        "Supplier app - Android & iOS, for sellers to list & manage orders",
        "Admin panel - web dashboard to control the entire marketplace",
        "Web store - responsive website so buyers can also shop from a browser",
        "Backend, database & APIs powering all of the above",
    ],
}

# ---------------------------------------------------------------------------
# Feature sections. Each = {heading, items[]}.  No prices anywhere.
# ---------------------------------------------------------------------------
FEATURE_SECTIONS = [
    {
        "heading": "Buyer app",
        "items": [
            "Quick sign up & login with mobile number + OTP (and social login)",
            "Personalised home feed with banners, categories & trending products",
            "Powerful search with filters, sort, and category / sub-category browse",
            "Product pages with image gallery, variants (size/colour), price, "
            "delivery estimate, ratings & reviews",
            "Add to cart, wishlist / save for later, and recently viewed",
            "Smooth checkout with multiple saved addresses",
            "Multiple payments: UPI, cards, net-banking, wallets & Cash on Delivery",
            "Order tracking with live status and delivery updates",
            "Easy returns, replacement & refund requests",
            "In-app wallet, coupons and reward points",
            "Rate & review products, upload review photos",
            "Notifications for offers, order updates & price drops",
            "Help / support chat and order-level query raising",
        ],
    },
    {
        "heading": "Supplier (seller) app",
        "items": [
            "Supplier registration with GST, bank & KYC document upload",
            "Onboarding approval flow controlled by admin",
            "Add / edit products: images, variants, price, stock, description",
            "Bulk product upload via catalogue / spreadsheet",
            "Inventory & stock management with low-stock alerts",
            "Order management: accept, pack, print label & mark ready to ship",
            "Live view of new, pending, shipped, delivered & returned orders",
            "Earnings dashboard with settlements, payouts & deductions",
            "Returns / RTO (return-to-origin) handling",
            "Performance score - ratings, cancellations, on-time dispatch",
            "Promotions: run discounts & join campaigns set by admin",
            "Notifications for new orders, payments & policy updates",
            "In-app support and dispute raising",
        ],
    },
    {
        "heading": "Admin panel (super admin)",
        "items": [
            "Full dashboard: sales, orders, active users, top suppliers & products",
            "Approve / reject / suspend suppliers and manage their KYC",
            "Manage the master catalogue, categories, brands & attributes",
            "Review & moderate products before they go live",
            "Order oversight across every supplier, with manual intervention",
            "Commission / margin setup per category or per supplier",
            "Supplier settlements & payout processing",
            "Coupons, offers, banners & campaign management",
            "Customer & supplier management (block, verify, message)",
            "Returns, refunds & dispute resolution centre",
            "Content management - pages, FAQs, policies, home layout",
            "Roles & permissions for staff / sub-admins",
            "Reports & exports for accounts and operations",
        ],
    },
    {
        "heading": "Catalogue, search & discovery",
        "items": [
            "Unlimited products, categories and sub-categories",
            "Product variants (size, colour, weight) with per-variant stock & price",
            "Smart search with auto-suggest, spelling tolerance & filters",
            "Sort by popularity, price, newest, discount & rating",
            "Personalised & 'similar products' recommendations",
            "Featured, trending and category-wise curated collections",
        ],
    },
    {
        "heading": "Cart, checkout & orders",
        "items": [
            "Single cart across multiple suppliers, split into shipments",
            "Address book with pin-code serviceability check",
            "Coupon & wallet application at checkout",
            "Order confirmation, invoice generation & order history",
            "Cancellation, return, replacement & refund workflows",
            "Guest browsing with login required only at checkout",
        ],
    },
    {
        "heading": "Payments, wallet & settlements",
        "items": [
            "Payment gateway integration (UPI, cards, net-banking, wallets)",
            "Cash on Delivery (COD) with COD limits & verification",
            "Buyer wallet, refunds to wallet or source, and reward points",
            "Automated supplier settlement after delivery / return window",
            "Commission, shipping & tax deductions handled per order",
            "Payout reports and downloadable statements",
        ],
    },
    {
        "heading": "Shipping & logistics",
        "items": [
            "Courier / logistics partner integration (e.g. Shiprocket-style)",
            "Automatic shipping-rate & serviceability by pin-code",
            "Shipping label & manifest generation for suppliers",
            "Real-time tracking synced to buyer & supplier apps",
            "RTO (return to origin) and failed-delivery handling",
        ],
    },
    {
        "heading": "Reselling & share-to-earn (Meesho-style)",
        "items": [
            "Share any product to WhatsApp, Facebook & Instagram in one tap",
            "Resellers add their own margin on top of the supplier price",
            "Track shared orders, margins earned & payouts",
            "Downloadable product images & catalogues for sharing",
            "Reseller earnings wallet and withdrawal to bank",
        ],
    },
    {
        "heading": "Ratings, reviews & trust",
        "items": [
            "Product ratings & written reviews with photos",
            "Verified-purchase badge on reviews",
            "Supplier rating & quality score visible to buyers",
            "Report / flag inappropriate products or reviews",
        ],
    },
    {
        "heading": "Marketing, offers & growth",
        "items": [
            "Coupon codes, flat & percentage discounts, free-shipping offers",
            "Flash sales, deals of the day & festive campaigns",
            "Referral program - invite friends & earn",
            "Push notifications, and optional SMS / email / WhatsApp campaigns",
            "Banners & promotional placements managed from admin",
            "SEO-ready web store for organic traffic",
        ],
    },
    {
        "heading": "Notifications & communication",
        "items": [
            "Push notifications on both apps for orders, offers & updates",
            "Transactional SMS / email / WhatsApp for key events (optional)",
            "In-app support chat and ticketing",
            "Admin broadcast messages to buyers or suppliers",
        ],
    },
    {
        "heading": "Reports & analytics",
        "items": [
            "Sales, revenue & order analytics with date filters",
            "Best-selling products, categories & top suppliers",
            "Buyer behaviour, funnel & retention insights",
            "Supplier performance and settlement reports",
            "Exportable reports (CSV / Excel) for accounting",
        ],
    },
    {
        "heading": "Security, quality & technology",
        "items": [
            "Secure authentication, encrypted data & role-based access",
            "OTP verification and fraud / abuse checks",
            "Scalable cloud architecture that grows with your orders",
            "Fast, responsive apps built with React Native / Flutter",
            "Clean REST APIs and a maintainable, well-documented codebase",
            "Full source-code ownership handed over to you",
        ],
    },
]

# What Bhama Vision delivers vs. third-party subscriptions on the client side.
REQUIREMENTS = {
    "title": "Delivery & requirements",
    "left_label": "Delivered by Bhama Vision",
    "right_label": "On client's side (third-party)",
    "covered": [
        "Complete UI/UX design of both apps, admin panel & website",
        "Full stack development - apps, backend, database & APIs",
        "Integration of the third-party services listed alongside",
        "Testing, bug fixing and app-store / server deployment",
        "Source-code handover, documentation & basic training",
    ],
    "not_covered": [
        "Domain, hosting / cloud server and their running costs",
        "Payment gateway account & its transaction fees",
        "SMS / email / WhatsApp & OTP service subscriptions",
        "Logistics / courier partner account and shipping charges",
        "Google Play & Apple developer accounts, and any paid API / plugin",
    ],
}

# Closing note - no pricing here on purpose.
CLOSING = {
    "title": "How we work & next steps",
    "note": (
        "Everything above is fully customisable - we can start with a focused "
        "first version (MVP) and add features in phases, or build the complete "
        "platform in one go. Once you shortlist the features you want, we will "
        "share a detailed proposal with scope, timeline and pricing, followed "
        "by design mockups for your approval before development begins."
    ),
    "steps": [
        "You review this feature list and mark what you need",
        "We finalise the scope together on a quick call",
        "We share a detailed quotation with timeline & pricing",
        "On confirmation, we begin design, then development in phases",
    ],
}
