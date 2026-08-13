"""
Bhama Vision - additional quotations bundle.

  1. College Admission Portal (with backend)          -> Rs 9,999
  1b. College Website (front-end + backend)            -> Rs 7,999
  2. Clothing Brand E-commerce (custom code)           -> Rs 12,999
  3. Connectify - Brand x Influencer matchmaking       -> Rs 3,499

Build:  python3 build_more.py
"""

COMPANY = {
    "name": "Bhama Vision",
    "tagline": "Websites, apps & AI for growing businesses",
    "email": "info@bhamavision.com",
    "phone": "+91 88606 40250",
    "website": "www.bhamavision.com",
    "location": "India",
}

CLIENT = {
    "name": "Prospective Client",
    "company": "Confidential",
    "note": "Multiple projects",
}

# --- Per-project scope cards (left = we deliver, right = client's third-party) ---

REQ_COLLEGE = {
    "title": "Scope & requirements",
    "left_label": "Delivered by Bhama Vision",
    "right_label": "On client's side (third-party)",
    "covered": [
        "Complete UI/UX design & development (website + applicant portal + admin)",
        "Database, data models and secure applicant & admin login",
        "Online application forms with document upload",
        "Integration of the third-party services listed alongside",
        "Deployment to the client's hosting + handover, testing & bug fixing",
    ],
    "not_covered": [
        "Domain and web hosting / server (and its yearly cost)",
        "Payment gateway account and its fees (for the application fee)",
        "SMS / email (OTP & notifications) service subscription",
        "All content: college info, courses, fees, images and logo",
        "Any other paid API or plugin",
    ],
}

REQ_COLLEGE_WEB = {
    "title": "Scope & requirements",
    "left_label": "Delivered by Bhama Vision",
    "right_label": "On client's side (third-party)",
    "covered": [
        "Complete, responsive front-end website design & development",
        "Admin backend to manage the site's content, with secure login",
        "Database and all data models",
        "Enquiry / contact form, Google Map embed & basic on-page SEO",
        "Deployment to the client's hosting + handover, testing & bug fixing",
    ],
    "not_covered": [
        "Domain and web hosting / server (and its yearly cost)",
        "All content: college info, courses, faculty, photos, prospectus & logo",
        "Business email account, if required",
        "Any paid plugin, stock media or third-party API",
    ],
}

REQ_ECOM = {
    "title": "Scope & requirements",
    "left_label": "Delivered by Bhama Vision",
    "right_label": "On client's side (third-party)",
    "covered": [
        "Complete custom-coded store: front-end + backend / admin panel",
        "Database, product catalogue, cart, checkout & order management",
        "Payment gateway integration",
        "Setup of up to 20 products (with size / colour variants)",
        "Deployment to the client's hosting + handover, testing & bug fixing",
    ],
    "not_covered": [
        "Domain, web hosting / server and SSL certificate",
        "Payment gateway account and its transaction fees",
        "Shipping / courier / logistics accounts and charges",
        "SMS / email notification service subscription",
        "All product content: photos, descriptions, prices and logo",
        "Any other paid API, plugin or theme",
    ],
}

REQ_CONNECTIFY = {
    "title": "Scope & requirements",
    "left_label": "Delivered by Bhama Vision",
    "right_label": "On client's side (third-party)",
    "covered": [
        "Complete UI/UX design & development (website + admin panel)",
        "Registration forms for influencers and brands",
        "Database to store all submissions securely",
        "Admin matchmaking tools and email notifications",
        "Deployment to the client's hosting + handover, testing & bug fixing",
    ],
    "not_covered": [
        "Domain and web hosting / server (and its yearly cost)",
        "Email / OTP sending service subscription",
        "All content: text, images and logo",
        "Payment gateway (only if paid plans / commissions are added later)",
        "Any other paid API or plugin",
    ],
}

QUOTATIONS = [
    # ---------------------------------------------------------------- 1
    {
        "id": "BV-Q-2026-CA1",
        "package": "With Backend & Admin",
        "title": "College Admission Portal",
        "subtitle": "Public website + online application portal + admin backend",
        "price": 9999,
        "price_note": "one-time (design & development)",
        "timeline": "20-30 working days",
        "summary": (
            "An end-to-end college admission portal. Students apply online, "
            "upload documents and track their status, while the college manages "
            "every application from a secure admin backend - shortlisting, "
            "approving and exporting data. Fully responsive across mobile, "
            "tablet and desktop."
        ),
        "sections": [
            {
                "heading": "Public website & information",
                "items": [
                    "Landing page: about the college & highlights",
                    "Courses / programs with eligibility and fee structure",
                    "Important dates, notices & announcements",
                    "FAQ and contact page with map",
                ],
            },
            {
                "heading": "Applicant portal",
                "items": [
                    "Register / login with email + OTP verification",
                    "Multi-step online admission application form",
                    "Document upload (marksheets, ID proof, photo, signature)",
                    "Pay the application fee online (payment gateway)",
                    "Track application status; download / print the application",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Manage courses, seats, eligibility & fee structure",
                    "View, search & filter all applications",
                    "Shortlist / approve / reject applicants with remarks",
                    "Document verification workflow",
                    "Publish notices & important dates",
                    "Export applicant data (Excel / PDF) and reports",
                    "Send email / SMS notifications to applicants",
                ],
            },
            {
                "heading": "Technical",
                "items": [
                    "Secure authentication with role-based access",
                    "Fully responsive across mobile, tablet & desktop",
                    "Deployment to the client's hosting + handover",
                ],
            },
        ],
        "support": REQ_COLLEGE,
    },
    # ---------------------------------------------------------------- 1b
    {
        "id": "BV-Q-2026-CW1",
        "package": "Website + Backend",
        "title": "College Website",
        "subtitle": "College website with front-end and admin backend",
        "price": 7999,
        "price_note": "one-time (design & development)",
        "timeline": "12-18 working days",
        "summary": (
            "A complete, professional college website with a modern, responsive "
            "front-end and an admin backend, so the college can update its own "
            "content - courses, faculty, news & notices, gallery and placements. "
            "Fully responsive across mobile, tablet and desktop."
        ),
        "sections": [
            {
                "heading": "Website (front-end) pages",
                "items": [
                    "Home: hero, highlights & quick links",
                    "About: history, vision & mission, leadership / management",
                    "Academics: courses / programs / departments with details",
                    "Faculty & departments",
                    "Facilities / infrastructure (labs, library, hostel, sports)",
                    "Admissions info (content only): eligibility, fee structure, "
                    "important dates & how to apply",
                    "Placements & achievements",
                    "Gallery: photos & events",
                    "News / notices / events (display)",
                    "Contact: enquiry form, map & phone",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Add / edit / remove news, notices & events",
                    "Manage gallery photos & albums",
                    "Manage courses / programs & departments",
                    "Manage faculty profiles",
                    "Update placements & achievements",
                    "Update home-page highlights & contact details",
                    "Secure admin login",
                ],
            },
            {
                "heading": "Technical",
                "items": [
                    "Secure authentication with role-based access",
                    "Fully responsive across mobile, tablet & desktop",
                    "Basic on-page SEO setup",
                    "Deployment to the client's hosting + handover",
                ],
            },
        ],
        "support": REQ_COLLEGE_WEB,
    },
    # ---------------------------------------------------------------- 2
    {
        "id": "BV-Q-2026-EC1",
        "package": "Custom-Coded Store",
        "title": "Clothing Brand E-commerce",
        "subtitle": "Custom-coded online store + payment gateway + admin backend",
        "price": 12999,
        "price_note": "one-time (design & development)",
        "timeline": "25-35 working days",
        "summary": (
            "A fully custom-coded online store for a clothing brand - no template "
            "or monthly-fee platform lock-in, and the client owns the source "
            "code. Includes catalogue, cart, secure checkout with a payment "
            "gateway, customer accounts and a complete admin backend to manage "
            "products and orders. Up to 20 products are set up at launch; more "
            "can be added anytime from the admin panel."
        ),
        "sections": [
            {
                "heading": "Custom-coded storefront",
                "items": [
                    "Bespoke design & code - no template / Shopify lock-in; "
                    "client owns the source code",
                    "Home, shop / catalogue, category & product detail pages",
                    "Product search, filters (size, colour, price) & sorting",
                    "Up to 20 products set up, with variants and image galleries",
                ],
            },
            {
                "heading": "Cart, checkout & payments",
                "items": [
                    "Add to cart, wishlist and cart management",
                    "Secure checkout with address & order summary",
                    "Payment gateway integration (e.g. Razorpay / Stripe / PayU)",
                    "Coupons / discount codes",
                    "Order confirmation & email notifications",
                ],
            },
            {
                "heading": "Customer accounts",
                "items": [
                    "Register / login, order history, saved addresses & wishlist",
                ],
            },
            {
                "heading": "Admin panel (backend)",
                "items": [
                    "Manage products, variants, inventory & pricing",
                    "Manage orders (pending / shipped / delivered) & customers",
                    "Coupons, shipping charges / zones setup",
                    "Basic sales dashboard & reports",
                ],
            },
            {
                "heading": "Custom code & technical",
                "items": [
                    "Custom-written code - no monthly platform fees, full ownership",
                    "Basic on-page SEO and fast, responsive design",
                    "Deployment to the client's hosting + handover",
                ],
            },
        ],
        "support": REQ_ECOM,
    },
    # ---------------------------------------------------------------- 3
    {
        "id": "BV-Q-2026-CN1",
        "package": "Matchmaking Platform",
        "title": "Connectify - Brand x Influencer",
        "subtitle": "Website + brand/influencer sign-up + admin matchmaking",
        "price": 3499,
        "price_note": "one-time (design & development)",
        "timeline": "12-18 working days",
        "summary": (
            "Connectify brings brands and influencers together. Influencers and "
            "brands each register through a form; the admin then reviews profiles "
            "and connects the right influencer with the right brand. A focused, "
            "essentials-first build - responsive across all devices."
        ),
        "sections": [
            {
                "heading": "Public website",
                "items": [
                    "Landing page explaining Connectify + a 'How it works' section",
                    "Separate 'For Influencers' and 'For Brands' sections",
                    "FAQ and contact page",
                ],
            },
            {
                "heading": "Influencer onboarding",
                "items": [
                    "Register via a detailed form: niche, social handles, follower "
                    "counts, audience, content samples & collaboration rates",
                ],
            },
            {
                "heading": "Brand onboarding",
                "items": [
                    "Register via a form: brand details, campaign goals, target "
                    "niche and budget",
                ],
            },
            {
                "heading": "Admin matchmaking (backend)",
                "items": [
                    "Review & approve influencer and brand profiles",
                    "Match the right influencer(s) to the right brand",
                    "Send introductions / notifications by email",
                    "Manage all users, profiles and matches",
                ],
            },
            {
                "heading": "Technical",
                "items": [
                    "Secure admin authentication and role-based access",
                    "Fully responsive across mobile, tablet & desktop",
                    "Deployment to the client's hosting + handover",
                ],
            },
        ],
        "support": REQ_CONNECTIFY,
    },
]

TERMS = {
    "validity_days": 15,
    "payment": "40% advance to start, 30% at midway, 30% on delivery "
               "(or as mutually agreed).",
    "notes": [
        "All prices are in Indian Rupees (INR) and are one-time for the design "
        "& development work quoted.",
        "All third-party subscriptions (hosting, domain, payment gateway, "
        "email/OTP, SMS, shipping) are arranged and paid for by the client "
        "directly.",
        "Content (text, images, product details, logo) is provided by the client.",
        "Timelines begin once content, access and the advance payment are received.",
        "Prices are exclusive of GST, if applicable.",
    ],
}
