"""
Bhama Vision - recruitment website quotation content.

A static, single-page website for a recruitment / staffing agency. One
scrolling landing page (hero, services, roles, about, contact) with a
WhatsApp chat button and an enquiry form. Design & development only -
no backend / admin panel, no job-board database, no applicant login.
Comes with a free hosting plan and 1 year of bug & error support. The
domain is arranged by the client (not on our side). Reuses the Bhama
Vision quotation renderer:

    python3 build_recruitment_website_quote.py

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
    "note": "Recruitment website - static single page",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Static single-page (one-page scrolling) website design",
        "Sections: hero, services, open roles, about & contact",
        "WhatsApp integration (click-to-chat button)",
        "Contact / enquiry form that delivers to your email",
        "Click-to-call and Google Maps location",
        "Mobile, tablet & desktop responsive",
        "Hosting - free plan",
        "1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Website content, logo & images (provided by the client)",
        "Backend / admin panel - this is a static website-only package",
        "Searchable job board / live vacancy database",
        "Candidate or employer login, profiles or applications",
        "Resume upload & applicant tracking",
        "Additional pages beyond the single page",
        "SEO, ads or social media marketing (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-030",
        "package": "Static Single-Page Website",
        "title": "Recruitment Website",
        "subtitle": "Static single-page website for a recruitment agency - design & development only",
        "price": 2000,
        "price_note": "one-time (design & development)",
        "timeline": "4-6 working days",
        "summary": (
            "A clean, static single-page website for your recruitment "
            "agency. Everything lives on one smooth scrolling page - an "
            "introduction, the services you offer, the kinds of roles you "
            "hire for, a short about section and your contact details. "
            "Visitors can reach you in one tap through a WhatsApp chat "
            "button, a click-to-call link or a simple enquiry form. This is "
            "a design-and-development package only - there is no backend or "
            "admin panel, no searchable job board and no candidate login. "
            "It comes with a free hosting plan and 1 year of bug & error "
            "support. The domain is arranged by you (it is not on our side), "
            "and we will help connect it to the website."
        ),
        "sections": [
            {
                "heading": "What we will design & develop",
                "items": [
                    "A single-page (one-page scrolling) website with smooth "
                    "section navigation",
                    "Hero section with your headline, tagline and a clear "
                    "call-to-action",
                    "Services section - the recruitment / staffing services "
                    "you offer",
                    "Open roles / sectors section to showcase the kinds of "
                    "positions you hire for (static content)",
                    "About section to build trust with employers & "
                    "candidates",
                    "WhatsApp integration - a click-to-chat button so "
                    "visitors message you directly",
                    "Contact / enquiry form that delivers to your email",
                    "Click-to-call button and Google Maps location",
                    "Fully responsive across mobile, tablet & desktop",
                    "Basic on-page setup - page title, favicon and "
                    "fast-loading images",
                    "Free hosting plan setup and go-live, plus connecting "
                    "your domain (arranged by you)",
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
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "This is a static, single-page website-only package - no backend / admin panel, job board or candidate login is included.",
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Website content, logo and images are provided by the client.",
        "Open roles are shown as static content; updating them later is a small content-change charge (or can be quoted as a dynamic job board separately).",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "This package covers a single page; additional pages are charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
