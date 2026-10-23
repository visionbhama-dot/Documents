"""
Bhama Vision - Fling Digital Services website quotation content.

A basic multi-page (4-5 page) website for a digital services company.
Design & development only - no backend / admin panel. Includes a contact
form that delivers to email, WhatsApp click-to-chat, a free hosting plan
and 1 year of bug & error support. The domain is arranged by the client
(not on our side). Reuses the Bhama Vision quotation renderer:

    python3 build_fling_digital_services_quote.py

Edit price, features, client or terms below, then re-run.
"""

# Page count covered by this package - repeated in the included list, the
# bullets and the terms so the fixed price is unambiguous.
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
    "name": "Fling Digital Services",
    "company": "Fling Digital Services",
    "note": "Basic 4-5 page website - design & development only",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Clean, professional {}-page website design".format(MAX_PAGES),
        "Pages: Home, About Us, Services, Portfolio & Contact Us",
        "Modern layout matched to your brand colours & logo",
        "Contact / enquiry form that delivers to your email",
        "WhatsApp click-to-chat & click-to-call buttons",
        "Google Maps location on the contact page",
        "Mobile, tablet & desktop responsive",
        "Basic on-page setup - page titles, favicon & fast-loading images",
        "Hosting - free plan; 1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Website content, logo & images (provided by the client)",
        "Backend / admin panel - this is a website-only package "
        "(available as an add-on)",
        "Pages beyond {} (charged per additional page)".format(MAX_PAGES),
        "Blog / news section managed from a dashboard",
        "Custom illustrations, photography or video production",
        "SEO campaigns, ads or social media marketing "
        "(separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-033",
        "package": "Basic Website Design",
        "title": "Fling Digital Services Website",
        "subtitle": "Basic {}-page website - design & development only".format(
            MAX_PAGES),
        "price": 1999,
        "price_note": "one-time (design & development)",
        "timeline": "4-6 working days",
        "summary": (
            "A clean, professional website for Fling Digital Services that "
            "gets your business online quickly and affordably. You get up to "
            + str(MAX_PAGES) + " pages - a Home page that introduces what you "
            "do, an About Us page that builds trust, a Services page setting "
            "out what you offer, a Portfolio page to show your work, and a "
            "Contact Us page with an enquiry form. Visitors can reach you in "
            "one tap through a WhatsApp chat button, a click-to-call link or "
            "the contact form, which delivers straight to your email. The "
            "design is modern, matched to your brand colours and logo, and "
            "fully responsive on mobile, tablet and desktop. This is a "
            "design-and-development package - the pages are built with your "
            "content, so there is no admin dashboard to maintain. It comes "
            "with a free hosting plan and 1 year of bug & error support. The "
            "domain is arranged by you (it is not on our side), and we will "
            "help connect it to the website."
        ),
        "sections": [
            {
                "heading": "Pages we will design & develop",
                "items": [
                    "Home - hero banner with your headline, what you do, "
                    "service highlights and a clear call-to-action",
                    "About Us - your story, strengths and why clients should "
                    "choose you",
                    "Services - the digital services you offer, presented "
                    "clearly with short descriptions",
                    "Portfolio / Our Work - a simple gallery of your projects "
                    "or client work",
                    "Contact Us - enquiry form, WhatsApp & call buttons, "
                    "address and Google Map",
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
                    "Basic on-page setup - page titles, meta descriptions, "
                    "favicon and clean URLs",
                    "Social media links in the header / footer",
                    "Testing across major browsers and devices before launch",
                ],
            },
            {
                "heading": "Contact & enquiries",
                "items": [
                    "Contact / enquiry form capturing name, phone, email and "
                    "message",
                    "Form submissions delivered straight to your email inbox",
                    "Spam protection on the form to keep junk enquiries out",
                    "WhatsApp click-to-chat button so visitors message you "
                    "directly",
                    "Click-to-call button for instant phone enquiries",
                    "Google Map embedded on the contact page",
                ],
            },
            {
                "heading": "Delivery & support",
                "items": [
                    "Free hosting plan set up and the website taken live",
                    "Help connecting the domain you have arranged",
                    "A walkthrough of the finished website on handover",
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
    "payment": "50% advance to start, 50% on delivery (or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the work quoted.",
        "This is a website-only package of up to {} pages - no backend / admin panel is included; additional pages are charged separately.".format(
            MAX_PAGES),
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Website content, logo and images are provided by the client.",
        "Page content is built in by us; later content changes are a small content-change charge, or an admin panel can be quoted separately.",
        "Timelines begin once the content, logo and advance payment are received.",
        "Two rounds of design revisions are included; further rounds are charged separately.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new pages/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
