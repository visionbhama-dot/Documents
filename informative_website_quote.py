"""
Bhama Vision - basic informative website quotation content.

A clean, informative 4-5 page website - design & development only.
Hosting is included; the domain is arranged by the client. Payment is
50% advance and 50% on completion. NOTE: by request, this quotation does
NOT mention any support / 1-year-support line anywhere. Reuses the Bhama
Vision quotation renderer:

    python3 build_informative_website_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Page count covered by this package - repeated in the included list, the
# subtitle, the summary and the terms so the fixed price is unambiguous.
MAX_PAGES = 5

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
    "note": "Basic informative website (4-5 pages) - design & development",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Clean, professional informative website (up to {} pages)".format(
            MAX_PAGES),
        "Pages: Home, About Us, Services, Gallery & Contact",
        "Modern layout matched to your brand colours & logo",
        "Contact / enquiry form that delivers to your email",
        "WhatsApp click-to-chat & click-to-call buttons",
        "Google Map on the contact page",
        "Mobile, tablet & desktop responsive",
        "Basic on-page setup - page titles, favicon & fast-loading images",
        "Hosting - free plan",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Website content, logo & images (provided by the client)",
        "Backend / admin panel (this is a website-only package)",
        "Online store / cart / payments",
        "Pages beyond {} (charged per additional page)".format(MAX_PAGES),
        "SEO campaigns, ads or social media marketing (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-070",
        "package": "Informative Website",
        "title": "Informative Website",
        "subtitle": "Basic {}-page informative website - design & development only".format(
            MAX_PAGES),
        "price": 999,
        "price_note": "one-time (design & development)",
        "timeline": "3 working days",
        "summary": (
            "A clean, professional informative website that gets your "
            "business online quickly and affordably. You get up to "
            + str(MAX_PAGES) + " pages - a Home page that introduces what "
            "you do, an About Us page that builds trust, a Services page "
            "setting out what you offer, a Gallery to showcase your work, "
            "and a Contact page with an enquiry form. Visitors can reach you "
            "in one tap through a WhatsApp chat button, a click-to-call link "
            "or the contact form, which delivers straight to your email. The "
            "design is modern, matched to your brand colours and logo, and "
            "fully responsive on mobile, tablet and desktop. Hosting is "
            "included; the domain is arranged by you and we will help connect "
            "it."
        ),
        "sections": [
            {
                "heading": "Pages we will design & develop",
                "items": [
                    "Home - introduction to your business with key "
                    "highlights and a clear call-to-action",
                    "About Us - your story, strengths and why people should "
                    "choose you",
                    "Services - what you offer, presented clearly with short "
                    "descriptions",
                    "Gallery - a simple image gallery to showcase your work "
                    "or space",
                    "Contact - enquiry form, WhatsApp & call buttons, address "
                    "and Google Map",
                ],
            },
            {
                "heading": "Design & build",
                "items": [
                    "Modern, professional layout matched to your brand "
                    "colours and logo",
                    "Consistent header and footer with navigation across all "
                    "pages",
                    "Fully responsive - looks right on mobile, tablet and "
                    "desktop",
                    "Fast-loading, optimised images",
                    "Basic on-page setup - page titles, favicon and clean "
                    "URLs",
                    "Social media links in the header / footer",
                ],
            },
            {
                "heading": "Contact & delivery",
                "items": [
                    "Contact / enquiry form that delivers to your email",
                    "WhatsApp click-to-chat and click-to-call buttons",
                    "Google Map embedded on the contact page",
                    "Hosting set up on a free plan and the website taken live",
                    "Help connecting the domain you have arranged",
                    "A walkthrough of the finished website on handover",
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
# NOTE: intentionally no support / 1-year-support line in this quotation.
TERMS = {
    "validity_days": 15,
    "payment": "50% advance to start, 50% on completion of the work.",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "This is a website-only package of up to {} pages; additional pages are charged separately.".format(
            MAX_PAGES),
        "The domain is not on our side - it is arranged and paid for by the client directly; hosting is included and we will help connect the domain.",
        "Website content, logo and images are provided by the client.",
        "Timelines begin once the content, logo and advance payment are received.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
