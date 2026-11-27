"""
Bhama Vision - Chartered Accountancy firm website quotation content.

A premium, corporate 6-page website for ABHISEKH CHATURVEDI & CO. with a
secure admin panel, lead / enquiry management, a full CA service
catalogue and a client portal. Hosting is included (domain is arranged by
the client). Reuses the Bhama Vision quotation renderer:

    python3 build_ca_website_quote.py

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
    "name": "ABHISEKH CHATURVEDI & CO.",
    "company": "ABHISEKH CHATURVEDI & CO.",
    "note": "Premium CA & business advisory website with admin panel & client portal",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Premium, corporate 6-page website - fully responsive",
        "Design in deep navy, white & muted gold with a modern, minimal feel",
        "Full CA service catalogue across all 10 service areas",
        "Secure admin panel with 3 user roles (Super Admin / Admin / Staff)",
        "Lead & enquiry management with Excel export & follow-ups",
        "Client portal - login, documents, tracking, invoices & messaging",
        "Enquiry forms, appointment booking, WhatsApp & email integration",
        "Blog / insights & FAQ management from the admin panel",
        "SEO-friendly build + Search Console, Analytics & SSL",
        "Online payment gateway integration",
        "Hosting (free plan) + website backup; 1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Payment gateway account & its transaction fees",
        "Website content, team photos & corporate photography (client "
        "provides; stock can be sourced separately)",
        "Third-party CRM subscription (integration-ready; licence on client)",
        "Accounting software licences (Tally / Zoho Books, etc.)",
        "SMS / email / OTP sending service subscription",
        "SEO campaigns & paid ads (separate service)",
        "Mobile app (Android / iOS) - separate scope",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-067",
        "package": "Corporate CA Website + Admin & Portal",
        "title": "ABHISEKH CHATURVEDI & CO. Website",
        "subtitle": "Premium 6-page CA & business advisory website with admin panel, client portal & lead management",
        "price": 5800,
        "price_note": "one-time (design & development)",
        "timeline": "5-7 working days",
        "summary": (
            "A premium, corporate website that positions ABHISEKH CHATURVEDI "
            "& CO. as a complete Chartered Accountancy and business-advisory "
            "firm serving individuals, startups, MSMEs, corporates, "
            "investors and large businesses. The site is built to do three "
            "things: establish credibility and trust through professional "
            "branding; present the firm's full range of CA, taxation, audit, "
            "regulatory and advisory services so clients can find exactly "
            "what they need; and drive business development by generating "
            "enquiries, capturing leads and helping convert them into "
            "assignments. It spans six pages - Home, About Us, Our Services, "
            "Insights & Resources, Contact / Enquiry and a secure Client "
            "Portal - and is backed by an admin panel for leads, content and "
            "users. The look is deep navy and white with muted-gold accents, "
            "a clean Inter / Lato / Poppins typeface, spacious modern layout "
            "and a fixed top navigation, fully responsive on every device. "
            "Hosting is included; the domain is arranged by you and we will "
            "help connect it."
        ),
        "sections": [
            {
                "heading": "Design & brand direction",
                "items": [
                    "Primary deep navy blue with white and muted-gold accents "
                    "on a white / very light grey background",
                    "Clean, professional typography (Inter / Lato / Poppins)",
                    "Minimal, premium, corporate design style",
                    "Spacious, modern, responsive layout with a fixed top "
                    "navigation",
                    "Professional corporate / business imagery placement "
                    "throughout",
                    "Consistent branding to build credibility and trust with "
                    "prospective clients",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Website pages (6)",
                "items": [
                    "Home - firm positioning, service highlights, trust "
                    "signals & clear calls-to-action",
                    "About Us - firm profile, approach, team & credentials",
                    "Our Services - the full catalogue, organised by service "
                    "area (detailed below)",
                    "Insights & Resources - articles, tax updates & "
                    "downloadable resources",
                    "Contact Us / Enquiry - enquiry form, appointment "
                    "booking, map & contact details",
                    "Client Portal - secure client login area (detailed "
                    "below)",
                ],
            },
            {
                "heading": "Services A - Direct Taxation & Income Tax",
                "items": [
                    "Individual, corporate, partnership-firm & LLP income-tax "
                    "return filing",
                    "Tax planning & advisory; advance-tax computation",
                    "Tax audit under Section 44AB; reports in Form 3CA, 3CB & "
                    "3CD",
                    "TDS & TCS compliance; transfer-pricing compliance",
                    "Income-tax assessments, scrutiny, appeals & "
                    "representation",
                    "Rectification & refund matters; tax due diligence",
                    "International taxation & DTAA advisory; non-resident "
                    "taxation",
                    "Tax deduction & exemption advisory",
                ],
            },
            {
                "heading": "Services B - GST & Indirect Taxation",
                "items": [
                    "GST registration & amendment",
                    "Monthly / quarterly returns - GSTR-1, GSTR-3B, GSTR-9 & "
                    "GSTR-9C; annual return & reconciliation",
                    "GST audit & compliance review; GST health check-up",
                    "Input-tax-credit reconciliation; GST refund applications",
                    "GST notices & replies; assessment & appeals",
                    "E-way-bill & e-invoicing compliance; LUT & export "
                    "compliance",
                    "GST advisory & transaction structuring",
                    "Customs duty & import / export tax advisory",
                ],
            },
            {
                "heading": "Services C - Audit & Assurance (prominent section)",
                "items": [
                    "Statutory audit (Companies Act) & tax audit (Income Tax "
                    "Act) shown as distinct services",
                    "Internal audit - process, operational & financial",
                    "GST audit / review & reconciliation assignments",
                    "Concurrent, bank, stock & revenue audits (where "
                    "eligible)",
                    "Management, cost & forensic audits (subject to "
                    "eligibility)",
                    "Special audit, compliance audit & government audit "
                    "assignments",
                    "Due diligence (financial, tax & regulatory) & IFC "
                    "(Internal Financial Controls) audit",
                    "Trust / NGO / Section 8 audit; limited review; branch "
                    "audit",
                    "Audit of financial statements, management representation "
                    "& audit documentation / reporting",
                ],
            },
            {
                "heading": "Services D - Corporate Law, ROC & Incorporation",
                "items": [
                    "Company incorporation - Private Ltd, Public Ltd, OPC & "
                    "Section 8; LLP incorporation",
                    "Partnership-firm registration & proprietorship setup "
                    "assistance",
                    "DIN & DSC assistance; PAN & TAN applications",
                    "MCA / ROC annual filings - AOC-4, MGT-7 / MGT-7A, "
                    "DIR-3 KYC, MSME-1, DPT-3, PAS-3 & event-based filings",
                    "Registered-office change; share-capital alteration",
                    "Director appointment & resignation; charge creation & "
                    "satisfaction",
                    "Company closure & strike-off; corporate restructuring",
                    "Secretarial compliance coordination",
                ],
            },
            {
                "heading": "Services E - Customs, Import & Export Advisory",
                "items": [
                    "Import Export Code (IEC) - new, modification & annual "
                    "update",
                    "Customs documentation & compliance; import-duty & "
                    "customs-valuation advisory",
                    "Export documentation & export-incentive advisory",
                    "RoDTEP scheme, Advance Authorisation & EPCG scheme "
                    "advisory",
                    "Foreign Trade Policy advisory; customs-duty "
                    "reconciliation",
                    "Import / export GST compliance; Letter of Undertaking "
                    "(LUT)",
                    "DGFT-related registration & compliance assistance",
                ],
            },
            {
                "heading": "Services F - Startup, MSME & Govt. Registrations",
                "items": [
                    "Udyam / MSME registration; DPIIT startup recognition & "
                    "Startup India compliance",
                    "MSME subsidy advisory & government-scheme eligibility "
                    "assessment",
                    "Project reports, CMA data, business plans & financial "
                    "projections",
                    "Bank-loan documentation, working-capital assessment & "
                    "fundraising documentation",
                    "Subsidy & incentive advisory",
                    "FSSAI registration coordination; trade-licence "
                    "assistance",
                    "Professional-tax & Shops-&-Establishments registration",
                ],
            },
            {
                "heading": "Services G - Accounting & Bookkeeping",
                "items": [
                    "Day-to-day accounting; monthly & quarterly bookkeeping",
                    "Financial-statement preparation & finalisation of "
                    "accounts",
                    "Bank, vendor & customer reconciliation",
                    "Accounts payable & receivable management; payroll "
                    "accounting",
                    "Fixed-asset register & inventory accounting",
                    "MIS reporting",
                    "Accounting-software implementation & support (Tally, "
                    "Zoho Books & others)",
                ],
            },
            {
                "heading": "Services H - Virtual CFO & Financial Management",
                "items": [
                    "Virtual CFO services with its own dedicated section",
                    "Monthly financial MIS; budgeting & forecasting",
                    "Cash-flow & working-capital management",
                    "Financial planning & analysis; cost control & "
                    "profitability analysis",
                    "Business-performance monitoring & financial-risk "
                    "management",
                    "Fund-management advisory & debt-restructuring assistance",
                    "Financial modelling; board & management reporting",
                    "Business-valuation coordination & strategic financial "
                    "advisory",
                ],
            },
            {
                "heading": "Services I - Business, Transaction & Mgmt. Advisory",
                "items": [
                    "Business setup & structuring; business valuation",
                    "Financial due diligence; M&A advisory & corporate "
                    "restructuring",
                    "Project feasibility studies & detailed project reports "
                    "(DPR)",
                    "Business-expansion, investment & funding advisory",
                    "Financial modelling & risk advisory",
                    "Internal-control-system design, SOP development & "
                    "process improvement",
                    "Business-succession planning",
                    "Insolvency & bankruptcy-related advisory (subject to "
                    "applicable authorisations)",
                ],
            },
            {
                "heading": "Services J - Other Regulatory & Specialised",
                "items": [
                    "Labour-law compliance coordination; EPF & ESIC "
                    "compliance; professional tax",
                    "RERA-related financial compliance; NGO & trust "
                    "compliance",
                    "FCRA compliance assistance (subject to eligibility)",
                    "CSR compliance & reporting; BRSR & sustainability "
                    "reporting",
                    "FEMA & RBI-related compliance advisory",
                    "Foreign-investment, FDI & ODI reporting; transfer-"
                    "pricing documentation",
                    "Trademark & IP registration coordination; DSC "
                    "assistance",
                ],
            },
            {
                "heading": "Client Portal (Page 6)",
                "items": [
                    "Secure client login with username & password",
                    "Document upload - financial statements, invoices & "
                    "supporting documents",
                    "Document download - reports & filed documents",
                    "Assignment tracking - progress of each assignment",
                    "Compliance calendar of important statutory due dates",
                    "Pending-documents list (awaited from the client)",
                    "Secure messaging & notifications",
                    "Invoice section with professional invoices",
                    "Payment status - outstanding & paid invoices",
                ],
            },
            {
                "heading": "Admin panel - dashboard & lead management",
                "items": [
                    "Dashboard - total & new enquiries, pending follow-ups, "
                    "converted leads, service-wise stats, monthly trends, "
                    "latest submissions, appointment requests & recent "
                    "activity",
                    "Lead records - auto Lead ID, name, mobile, email, "
                    "service category, business type, enquiry date, lead "
                    "source, assigned person, status & remarks",
                    "Status pipeline - New, Contacted, Follow-up, Converted, "
                    "Lost - with follow-up dates & reminders",
                    "Search by name / mobile / email; filter by service "
                    "category; export enquiries to Excel",
                    "Assign enquiries to staff; full communication history; "
                    "download individual enquiry details",
                    "Duplicate-lead prevention based on mobile / email",
                ],
            },
            {
                "heading": "Admin panel - content & user roles",
                "items": [
                    "Add / edit services & descriptions; add articles & tax "
                    "updates; upload PDF resources",
                    "Update contact details, office address, team profiles & "
                    "biographies",
                    "Add / modify FAQs; update homepage sections; manage SEO "
                    "titles & descriptions",
                    "Super Admin - complete website & system control",
                    "Admin / Manager - leads, enquiries, content & follow-ups",
                    "Staff - assigned leads & limited enquiry access",
                ],
            },
            {
                "heading": "Platform features",
                "items": [
                    "SEO-friendly build with Google Search Console & Google "
                    "Analytics set up",
                    "SSL certificate & mobile-responsive design",
                    "Website backup; WhatsApp & email integration",
                    "Blog & FAQ management; compliance calendar",
                    "Appointment booking; client portal; CRM-integration "
                    "readiness",
                    "Online payment gateway integration; staff management",
                ],
            },
            {
                "heading": "SEO, hosting & delivery",
                "items": [
                    "On-page SEO - titles, meta descriptions, clean URLs, "
                    "headings, alt text & XML sitemap",
                    "Fast-loading, mobile-first build tested across major "
                    "browsers & devices",
                    "Hosting provided on a free plan with website backup",
                    "Help connecting the domain you have arranged",
                    "Guided walkthrough & handover of the website, admin "
                    "panel & client portal",
                    "1 year of support for bugs & errors after launch",
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
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "The domain is not on our side - it is arranged and paid for by the client directly; hosting is included and we will help connect the domain.",
        "The service catalogue content, team photos and corporate imagery are provided by the client; stock imagery can be sourced separately if required.",
        "The payment gateway account is opened in the client's name with the client's KYC; its transaction fees are charged by the gateway and are not part of this quote.",
        "The website is CRM-integration ready; any third-party CRM subscription and accounting-software licences (Tally / Zoho Books) are arranged and paid for by the client.",
        "Any SMS / email / OTP sending service subscription is arranged and paid for by the client.",
        "Service descriptions are presented for marketing purposes; the firm remains responsible for the professional services and any statutory eligibility.",
        "Timelines begin once the content, logo and advance payment are received.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
