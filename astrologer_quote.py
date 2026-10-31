"""
Bhama Vision - astrologer website + backend quotation content.

A clean, responsive website for an astrologer that presents services,
an about section, a dedicated gallery page and a contact / enquiry form
with WhatsApp - backed by an admin panel to manage services, gallery
images, testimonials and enquiry leads.

Reuses the Bhama Vision quotation renderer:

    python3 build_astrologer_quote.py

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
    "company": "Astrologer",
    "note": "Astrologer website with backend admin panel & gallery page",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Clean, responsive astrologer website",
        "All standard pages - Home, About, Services, Gallery, Contact",
        "Dedicated gallery page (photos / events / certificates)",
        "Admin panel (backend) to manage the site",
        "Manage services, gallery images & testimonials",
        "Enquiry form + WhatsApp click-to-chat & call buttons",
        "Enquiry leads inbox + basic on-page SEO & Google Map",
    ],
    "not_covered": [
        "Domain & hosting - arranged and paid by the client (we help set up)",
        "Content, images & copywriting (provided by the client)",
        "Logo / brand identity design (separate service)",
        "Online payments / consultation booking & payment gateway",
        "Online store / e-commerce features",
        "Ongoing SEO or ad campaigns & any paid plugin / API",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-040",
        "package": "Website + Backend",
        "title": "Astrologer Website",
        "subtitle": "Responsive astrologer website with a gallery page & an admin backend",
        "price": 4800,
        "price_note": "one-time (design & development)",
        "timeline": "7-10 working days",
        "summary": (
            "A clean, professional website for an astrologer that builds "
            "trust and brings in enquiries. Visitors learn about you and "
            "your experience, explore your services - like kundli / "
            "horoscope, matchmaking, vastu, gemstone and puja guidance - and "
            "browse a dedicated gallery of your photos, events and "
            "certificates. Getting in touch is effortless: an enquiry form "
            "that reaches your email and WhatsApp, a WhatsApp chat button and "
            "a click-to-call button, plus a Google Map on the contact page. "
            "Behind the site, an easy-to-use admin panel lets you manage your "
            "services, add or remove gallery images, update testimonials and "
            "view every enquiry - all without touching code. The site is "
            "fully responsive and SEO-friendly."
        ),
        "sections": [
            {
                "heading": "Website pages (frontend)",
                "items": [
                    "Home - hero banner, introduction, services snapshot & "
                    "clear call-to-action",
                    "About - the astrologer's journey, experience and "
                    "specialities",
                    "Services - horoscope / kundli, matchmaking, vastu, "
                    "gemstone, puja and more with descriptions",
                    "Gallery - dedicated page for photos, events, ceremonies "
                    "and certificates in a clean grid / lightbox",
                    "Testimonials - client experiences to build trust",
                    "Contact - enquiry form, WhatsApp & call buttons, address "
                    "and Google Map",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Gallery page",
                "items": [
                    "Dedicated gallery page with a neat, responsive grid",
                    "Click-to-enlarge (lightbox) viewing of images",
                    "Organised into simple albums / categories if needed",
                    "Images added, replaced & removed from the admin panel",
                    "Optimised images for fast loading on mobile",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Secure admin login with dashboard",
                    "Add, edit & remove services",
                    "Manage gallery images (upload, replace & delete)",
                    "Add & manage testimonials",
                    "View enquiry leads received through the site",
                    "Homepage & banner / image management",
                ],
            },
            {
                "heading": "Enquiry, SEO & delivery",
                "items": [
                    "Enquiry form capturing name, phone, service of interest "
                    "and message - delivered to email & WhatsApp",
                    "Floating WhatsApp click-to-chat button + click-to-call "
                    "button on every page",
                    "Basic on-page SEO - page titles, meta descriptions, "
                    "clean URLs and image alt text",
                    "Google Map embedded on the contact page",
                    "Fast-loading, mobile-first build tested across browsers "
                    "& devices",
                    "Deployment and help connecting your domain & hosting",
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
        "Domain and hosting are arranged and paid for by the client directly; we will help set them up and connect them.",
        "Content, images, gallery photos and testimonials are provided by the client and can be managed via the admin panel.",
        "Enquiries reach you by email and WhatsApp and are also stored in the admin panel.",
        "Online payments / consultation booking and a payment gateway are a separate scope.",
        "Timelines begin once the content, logo and advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
