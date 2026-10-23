"""
Bhama Vision - Fatima Tour & Travel website quotation content.

A clean, responsive website for a tour & travel agency with all the
standard pages, an enquiry form and WhatsApp integration so every booking
enquiry reaches the agency directly. Website only - no admin panel in
this package. Comes with free hosting and 1 year of bug & error support.
The domain is arranged by the client (not on our side). Reuses the Bhama
Vision quotation renderer:

    python3 build_fatima_tour_travel_quote.py

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
    "name": "Fatima Tour & Travel",
    "company": "Fatima Tour & Travel",
    "note": "Travel agency website with WhatsApp integration",
}

# Requirements box shown on the quotation (two columns).
REQUIREMENTS = {
    "title": "What's included & what's not",
    "left_label": "Included in this package",
    "right_label": "Not included",
    "covered": [
        "Clean, professional, responsive travel website",
        "All standard pages - Home, About Us, Packages, Services, Contact",
        "Tour & travel packages presented with photos and details",
        "Services section (ticketing, hotels, visa, transport & more)",
        "Enquiry form - submissions reach your email & WhatsApp",
        "WhatsApp integration (click-to-chat + enquire on each package)",
        "Click-to-call button & Google Map on the contact page",
        "Basic on-page SEO so you can be found on Google",
        "Hosting - free plan; 1 year bug & error support",
    ],
    "not_covered": [
        "Domain - arranged and paid by the client (not on our side)",
        "Photos, package details & company content (provided by the client)",
        "Admin panel to self-manage packages (available as an add-on)",
        "Live flight / hotel booking engine & GDS API - separate scope",
        "Multi-language versions of the website",
        "SEO campaigns & paid ads (separate service)",
    ],
}

# ---------------------------------------------------------------------------
# The quotation(s).
# ---------------------------------------------------------------------------
QUOTATIONS = [
    {
        "id": "BV-Q-2026-032",
        "package": "Travel Website",
        "title": "Fatima Tour & Travel Website",
        "subtitle": "Travel agency website with enquiry form & WhatsApp integration",
        "price": 4000,
        "price_note": "one-time (design & development)",
        "timeline": "7-10 working days",
        "summary": (
            "A clean, professional website for Fatima Tour & Travel that "
            "gives your agency a credible online presence and brings "
            "enquiries straight to your phone. Visitors can explore your tour "
            "packages and destinations with photos and details, read about "
            "the services you offer - ticketing, hotel bookings, visa "
            "assistance, transport and more - and learn about your agency on "
            "the About Us page. Getting in touch is effortless: an enquiry "
            "form that reaches your email and WhatsApp, a WhatsApp chat "
            "button on every page, an 'Enquire on WhatsApp' button on each "
            "package that opens a chat with the package name already filled "
            "in, a click-to-call button and a Google Map on the contact page. "
            "The site is fully responsive, built SEO-friendly, and comes with "
            "a free hosting plan and 1 year of bug & error support. The "
            "domain is arranged by you (it is not on our side), and we will "
            "help connect it."
        ),
        "sections": [
            {
                "heading": "Website pages",
                "items": [
                    "Home - attractive hero banner, featured packages, "
                    "services snapshot & call-to-action",
                    "About Us - your agency's story, experience and why "
                    "travellers should choose you",
                    "Tour Packages - packages shown in a clean grid with "
                    "photos, duration and highlights",
                    "Package detail - photo gallery, itinerary highlights, "
                    "inclusions and an enquiry button",
                    "Services - ticketing, hotel booking, visa assistance, "
                    "passport help, taxi / transport and group tours",
                    "Contact Us - enquiry form, WhatsApp & call buttons, "
                    "office address and Google Map",
                    "Gallery page to showcase destination and trip photos",
                    "Fully responsive across mobile, tablet & desktop",
                ],
            },
            {
                "heading": "Packages & destinations",
                "items": [
                    "Your tour packages set up with photos, duration, "
                    "highlights and pricing (if you wish to show it)",
                    "Grouped by type or destination - domestic, "
                    "international, pilgrimage, honeymoon, group tours",
                    "Featured packages highlighted on the home page",
                    "Seasonal or offer packages can be promoted on the banner",
                    "Clean, consistent layout that stays tidy as you add more "
                    "packages",
                ],
            },
            {
                "heading": "Enquiry form & WhatsApp integration",
                "items": [
                    "Enquiry form capturing name, phone, travel dates, "
                    "destination / package and message",
                    "Submissions delivered to your email and WhatsApp, so no "
                    "booking enquiry is missed",
                    "Spam protection on the form to keep junk enquiries out",
                    "Floating WhatsApp click-to-chat button on every page",
                    "'Enquire on WhatsApp' button on each package that opens "
                    "a chat with the package name pre-filled",
                    "Click-to-call button for instant phone enquiries",
                    "Thank-you confirmation shown after the form is submitted",
                ],
            },
            {
                "heading": "Design, SEO & delivery",
                "items": [
                    "Modern, travel-focused design matched to your brand "
                    "colours and logo",
                    "Basic on-page SEO - page titles, meta descriptions, "
                    "clean URLs and image alt text",
                    "Google Map embedded on the contact page",
                    "Fast-loading, mobile-first build",
                    "Testing across major browsers and devices before launch",
                    "Deployment on a free hosting plan and help connecting "
                    "your domain",
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
        "The domain is not on our side - it is arranged and paid for by the client directly; we will help connect it to the website.",
        "Package photos, itineraries and company content are provided by the client.",
        "Enquiries reach you by email and WhatsApp; an admin panel to add and edit packages yourself is available as an add-on and is quoted separately.",
        "Timelines begin once the content, logo and advance payment are received.",
        "1 year support covers bugs & errors only (things that stop working). It does not cover content changes, new packages/features or redesigns.",
        "Hosting is provided on a free plan; upgrading to paid hosting (for higher traffic or needs) is optional and charged separately.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
