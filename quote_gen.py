"""
Bhama Vision - command-driven quotation generator ("quote bot").

Type a plain-English command and it builds a branded A4 PDF quotation in
seconds, using the SAME renderer (`build_quotes.py`) as every hand-written
quote. No external AI / API is used - it runs fully offline. It reads the
command, works out the kind of website (e-commerce store, travel, real
estate, news, blog, business/services, rental, recruitment, restaurant,
portfolio or a plain website), pulls out the details (item count, price,
payment, admin, domain, hosting, support, reference site) and fills the
quotation template, then assigns a BV-Q number.

USAGE

    # one-shot: pass the command as an argument
    python3 quote_gen.py "travel website 50 packages with admin 1 year support 12k"

    # see what it parsed without building
    python3 quote_gen.py --dry-run "real estate website 80 properties admin seo 15k"

    # interactive chat mode: type commands at the prompt, Ctrl-D / 'quit' to exit
    python3 quote_gen.py

EXAMPLES OF COMMANDS

    jewellery ecommerce 40 products payment integration no domain with hosting admin 8k
    travel website 50 packages with admin panel 1 year support 12k
    real estate website 60 properties admin panel seo with hosting 15k
    news portal multi-language admin adsense 10k
    business website services admin enquiry 6k

Output PDFs are written to `output/`.
"""
import os
import re
import sys

import build_quotes

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Fixed brand details (identical to the hand-written quotes).
# ---------------------------------------------------------------------------
COMPANY = {
    "name": "Bhama Vision",
    "tagline": "Websites, apps & AI for growing businesses",
    "email": "info@bhamavision.com",
    "phone": "+91 88606 40250",
    "website": "www.bhamavision.com",
    "location": "India",
}

PAYMENT = {
    "account_name": "Prafull Kumar Sharma",
    "upi": "8860640250@idfcfirst",
    "bank": "IDFC First Bank",
    "qr_image": "payment qr.jpeg",
}

# Make the Noto Sans fonts resolve on whatever machine this runs on.
# The bundled copy in assets/fonts is tried first so the app is fully
# self-contained on free hosting (Streamlit Cloud, Hugging Face Spaces, ...).
for _fd in (
    os.path.join(HERE, "assets", "fonts"),
    build_quotes.FONT_DIR,
    "/inner_container/usr/share/fonts/google-noto",
    "/usr/share/fonts/google-noto",
):
    if os.path.isfile(os.path.join(_fd, "NotoSans-Regular.ttf")):
        build_quotes.FONT_DIR = _fd
        break

# ---------------------------------------------------------------------------
# E-commerce niches - wording for product stores.
# ---------------------------------------------------------------------------
NICHES = [
    {"keys": ["jewellery", "jewelry", "jeweller", "jeweler"], "word": "Jewellery",
     "noun": "online jewellery store",
     "collections": "rings, necklaces, earrings & bangles",
     "variants": "metal / size variants"},
    {"keys": ["apparel", "clothing", "fashion", "t-shirt", "tshirt", "hoodie",
              "streetwear", "garment", "saree", "kurti"], "word": "Apparel",
     "noun": "online clothing store",
     "collections": "t-shirts, hoodies & sweatshirts",
     "variants": "size & colour variants"},
    {"keys": ["perfume", "fragrance", "attar"], "word": "Perfume",
     "noun": "online perfume store",
     "collections": "eau de parfum, attars & gift sets",
     "variants": "size / volume variants"},
    {"keys": ["grocery", "kirana", "supermarket"], "word": "Grocery",
     "noun": "online grocery store",
     "collections": "staples, snacks, beverages & household",
     "variants": "weight / pack-size variants"},
    {"keys": ["optical", "eyewear", "spectacle", "sunglass"], "word": "Optical",
     "noun": "online optical store",
     "collections": "eyeglasses, sunglasses & lenses",
     "variants": "frame / lens variants"},
    {"keys": ["footwear", "shoe", "sneaker"], "word": "Footwear",
     "noun": "online footwear store",
     "collections": "sneakers, formals & sandals",
     "variants": "size & colour variants"},
    {"keys": ["cosmetic", "beauty", "skincare", "makeup"], "word": "Beauty",
     "noun": "online beauty & cosmetics store",
     "collections": "skincare, makeup & haircare",
     "variants": "shade / size variants"},
    {"keys": ["electronic", "gadget", "appliance"], "word": "Electronics",
     "noun": "online electronics store",
     "collections": "phones, accessories & appliances",
     "variants": "model / colour variants"},
    {"keys": ["furniture", "home decor", "decor", "homeware"], "word": "Home Decor",
     "noun": "online home & decor store",
     "collections": "furniture, lighting & decor",
     "variants": "size / finish variants"},
    {"keys": ["food", "bakery", "snack", "sweet"], "word": "Food",
     "noun": "online food store",
     "collections": "snacks, sweets & packaged food",
     "variants": "weight / pack-size variants"},
]

GENERIC_STORE_NICHE = {
    "keys": [], "word": "", "noun": "online store",
    "collections": "featured products & categories", "variants": "variants"}

# ---------------------------------------------------------------------------
# Non-store website types. Checked in order; first keyword hit wins.
# ordering: how customers transact -> booking / enquiry / apply / content / leads
# ---------------------------------------------------------------------------
SITE_TYPES = [
    {
        "keys": ["travel", "tour", "tourism", "holiday", "trip", "vacation"],
        "title": "Travel Website", "package": "Travel Website",
        "noun": "travel website", "item": "tour packages",
        "count_word": "Packages", "ordering": "booking", "seo": True,
        "admin_manage": "tour packages, destinations & images",
        "frontend_extra": [
            "Destination / package listing with photos, days & price",
            "Package detail page with itinerary, inclusions & gallery",
        ],
    },
    {
        "keys": ["real estate", "real-estate", "realtor", "property", "properties",
                 "proptech", "builder", "flats", "apartments"],
        "title": "Real Estate Website", "package": "Real Estate Website",
        "noun": "real estate website", "item": "property listings",
        "count_word": "Properties", "ordering": "enquiry", "seo": True,
        "admin_manage": "property listings, categories & images",
        "frontend_extra": [
            "Property listing with filters (type, location, budget, BHK)",
            "Property detail page with gallery, map view & amenities",
        ],
    },
    {
        "keys": ["rental", "rent a", "taxi", "car rental", "bike rental", "vehicle"],
        "title": "Rental Website", "package": "Rental Website",
        "noun": "rental website", "item": "vehicle listings",
        "count_word": "Vehicles", "ordering": "booking", "seo": False,
        "admin_manage": "vehicles, availability & bookings",
        "frontend_extra": [
            "Vehicle listing with photos, rates & availability",
            "Vehicle detail page with specs, pricing & booking enquiry",
        ],
    },
    {
        "keys": ["news", "magazine", "newspaper", "media portal"],
        "title": "News Portal", "package": "News Website",
        "noun": "news portal", "item": "articles",
        "count_word": "Articles", "ordering": "content", "seo": True,
        "admin_manage": "articles, categories, authors & media",
        "frontend_extra": [
            "Category sections with featured & latest stories",
            "Article page with image, share buttons & related posts",
            "Multi-language support (optional) & AdSense-ready layout",
        ],
    },
    {
        "keys": ["blog", "article website", "content website"],
        "title": "Blog Website", "package": "Blog Website",
        "noun": "blog website", "item": "posts",
        "count_word": "Posts", "ordering": "content", "seo": True,
        "admin_manage": "posts, categories & media",
        "frontend_extra": [
            "Blog listing with categories, tags & search",
            "Post page with image gallery & related posts",
            "AdSense & Google Analytics ready",
        ],
    },
    {
        "keys": ["recruitment", "job portal", "jobs", "hiring", "placement",
                 "career"],
        "title": "Recruitment Website", "package": "Recruitment Website",
        "noun": "recruitment website", "item": "job listings",
        "count_word": "Jobs", "ordering": "apply", "seo": True,
        "admin_manage": "job listings & applications",
        "frontend_extra": [
            "Job listing with filters (role, location, experience)",
            "Job detail page with description & apply form",
        ],
    },
    {
        "keys": ["restaurant", "cafe", "café", "fast food", "fast-food",
                 "cloud kitchen", "dining", "menu"],
        "title": "Restaurant Website", "package": "Restaurant Website",
        "noun": "restaurant website", "item": "menu items",
        "count_word": "Menu Items", "ordering": "enquiry", "seo": False,
        "admin_manage": "menu items, categories & offers",
        "frontend_extra": [
            "Menu by category with photos, description & price",
            "Table reservation / order enquiry over WhatsApp",
        ],
    },
    {
        "keys": ["portfolio", "production house", "photography", "film",
                 "animated", "studio", "agency portfolio"],
        "title": "Portfolio Website", "package": "Portfolio Website",
        "noun": "portfolio website", "item": "projects",
        "count_word": "Projects", "ordering": "leads", "seo": False,
        "admin_manage": "projects, gallery & sliders",
        "frontend_extra": [
            "Work / project gallery with categories & lightbox",
            "Project detail page with media, credits & description",
        ],
    },
    {
        "keys": ["business", "corporate", "company", "agency", "consult",
                 "digital services", "service website", "services website",
                 "manufacturer", "b2b", "startup"],
        "title": "Business Website", "package": "Business Website",
        "noun": "business website", "item": "services",
        "count_word": "Services", "ordering": "leads", "seo": True,
        "admin_manage": "services, case studies & enquiries",
        "frontend_extra": [
            "Services section with detail pages",
            "Case studies / portfolio & testimonials",
        ],
    },
    {
        "keys": ["static", "landing page", "single page", "single-page",
                 "basic website", "one page", "one-page", "brochure"],
        "title": "Website", "package": "Website",
        "noun": "website", "item": "pages",
        "count_word": "Pages", "ordering": "leads", "seo": False,
        "static": True, "admin_manage": "content & enquiries",
        "frontend_extra": [
            "Clean multi-section layout with clear calls-to-action",
        ],
    },
]

# Fallback when nothing specific matches: a general business website.
GENERIC_SITE = SITE_TYPES[-2]

# Nouns we accept after a number when reading an item count.
COUNT_NOUNS = [
    (r"products?", "Products"), (r"packages?", "Packages"),
    (r"properties|property", "Properties"), (r"listings?", "Listings"),
    (r"vehicles?", "Vehicles"), (r"cars?", "Cars"), (r"bikes?", "Bikes"),
    (r"articles?", "Articles"), (r"posts?", "Posts"), (r"pages?", "Pages"),
    (r"services?", "Services"), (r"projects?", "Projects"),
    (r"rooms?", "Rooms"), (r"courses?", "Courses"), (r"items?", "Items"),
    (r"jobs?", "Jobs"), (r"designs?", "Designs"), (r"fragrances?", "Fragrances"),
]

STORE_WORDS = ["ecommerce", "e-commerce", "e commerce", "online store",
               "online shop", "web store", "webstore", "online selling",
               "sell online", "shopping website", "shop", "store"]
SHOWCASE_WORDS = ["showcase", "catalogue", "catalog", "enquiry only",
                  "enquiry-based"]


# ---------------------------------------------------------------------------
# Command parsing
# ---------------------------------------------------------------------------
def _flag(text, positive, negative):
    """Return True / False / None for an include-or-not feature."""
    for p in negative:
        if p in text:
            return False
    for p in positive:
        if p in text:
            return True
    return None


# A "don't talk about this" instruction: a negation phrase followed, within the
# same clause (no comma / period in between), by the topic word. This keeps the
# suppression local, so "do not mention hosting, no domain" suppresses only
# hosting - not the separate domain clause.
_SUPPRESS_NEG = (r"(?:do not mention|don't mention|dont mention|without mentioning"
                 r"|no mention of|do not include|don't include|dont include"
                 r"|do not talk about|skip(?:ping)?)")


def _dont_mention(text, topic_pattern):
    return re.search(_SUPPRESS_NEG + r"[^.,;]{0,40}?" + topic_pattern, text) is not None


def _resolve_type(text):
    """Work out the website type. Returns (kind, cfg, niche).

    kind is "store" or "site". For a store, niche is the matched NICHE and
    cfg is None; for a site, cfg is the matched SITE_TYPE and niche is None.
    """
    # 1) Specific non-store website types win first (travel, real estate, ...).
    for cfg in SITE_TYPES:
        if any(k in text for k in cfg["keys"]):
            return "site", cfg, None
    # 2) E-commerce: a product niche, or generic store wording.
    for niche in NICHES:
        if any(k in text for k in niche["keys"]):
            return "store", None, niche
    if any(k in text for k in STORE_WORDS):
        return "store", None, GENERIC_STORE_NICHE
    # 3) Nothing specific -> a general business website.
    return "site", GENERIC_SITE, None


def parse_command(command):
    """Turn a plain-English command into a dict of quotation slots."""
    text = " " + command.lower().strip() + " "

    # Item count + its noun: "25 products", "50 packages", "80 properties".
    count, count_word = None, None
    for pat, label in COUNT_NOUNS:
        m = re.search(r"(\d+)\s*(?:" + pat + r")\b", text)
        if m:
            count, count_word = int(m.group(1)), label
            break

    # Price: "8k" / "rs 8000" / "₹8,000" / "inr 6000".
    price = None
    m = re.search(r"(?:rs\.?|₹|inr|rupees)?\s*(\d+(?:\.\d+)?)\s*k\b", text)
    if m:
        price = int(float(m.group(1)) * 1000)
    else:
        m = re.search(r"(?:rs\.?|₹|inr|rupees)\s*([\d,]+)", text)
        if m:
            price = int(m.group(1).replace(",", ""))

    # Features.
    payment = _flag(text, ["payment", "razorpay", "payu", "cashfree", "gateway",
                           "online pay", "booking payment"],
                    ["no payment", "without payment", "no online payment"])
    admin = _flag(text, ["admin", "backend", "dashboard", "cms", "panel"],
                  ["no admin", "without admin", "no backend"])
    domain = _flag(text, ["with domain", "domain included", "including domain"],
                   ["no domain", "without domain", "domain not"])
    hosting = _flag(text, ["with hosting", "hosting included", "including hosting",
                           "free hosting"],
                    ["no hosting", "without hosting", "hosting not"])
    seo = _flag(text, ["seo", "search engine", "google ranking", "adsense",
                       "analytics"], [])

    # Optional blog / articles section and an image gallery.
    blog = _flag(text, ["blog", "blogs", "article section", "articles section",
                        "news section"], ["no blog"])
    gallery = _flag(text, ["gallery", "image", "images", "photo", "photos"],
                    ["no gallery"])
    delivery = _flag(text, ["delivery", "home delivery", "doorstep",
                            "delivery management"],
                     ["no delivery", "pickup only", "self pickup"])

    # "do not mention X" instructions suppress every line about that topic.
    mention_domain = not _dont_mention(text, r"domain")
    mention_hosting = not _dont_mention(text, r"hosting")
    mention_count = not _dont_mention(
        text, r"(?:product listing|listing|product number|number|products?|quantity)")

    support_years = None
    m = re.search(r"(\d+)\s*[-]?\s*year", text)
    if m:
        support_years = int(m.group(1))
    elif re.search(r"\b(?:a|one|1)\s*[-]?\s*year", text):
        support_years = 1

    reference = None
    for cand in re.findall(
            r"\b([a-z0-9][a-z0-9-]*\.(?:com|in|co|net|org|store|shop|io)(?:\.[a-z]{2})?)\b",
            text):
        if "bhamavision" not in cand:
            reference = cand
            break

    kind, cfg, niche = _resolve_type(text)

    # Resolve payment default by type.
    if kind == "store":
        store_enquiry = any(k in text for k in SHOWCASE_WORDS)
        payment_default = not store_enquiry
    else:
        payment_default = False  # travel/real estate/etc default to enquiry

    # Admin defaults on, except for a plain static website.
    is_static = (kind == "site" and cfg.get("static"))
    admin_default = not is_static

    return {
        "kind": kind,
        "cfg": cfg,
        "niche": niche,
        "count": count,
        "count_word": count_word,
        "products": count,  # backwards-compatible alias
        "price": price,
        "payment": payment_default if payment is None else payment,
        "admin": admin_default if admin is None else admin,
        "domain": False if domain is None else domain,
        "mention_domain": mention_domain,
        "hosting": False if hosting is None else hosting,
        "mention_hosting": mention_hosting,
        "mention_count": mention_count,
        "seo": (cfg["seo"] if (seo is None and kind == "site") else bool(seo)),
        "blog": bool(blog),
        "gallery": bool(gallery),
        "delivery": bool(delivery),
        "support_years": support_years,
        "reference": reference,
        "raw": command.strip(),
    }


# ---------------------------------------------------------------------------
# ID assignment
# ---------------------------------------------------------------------------
def highest_quote_number():
    """Return the highest BV-Q-2026-NNN number found in the repo (int).

    Scans both the content modules (*.py) and already-generated PDFs in
    output/, so each newly committed quote gets a fresh, unique number.
    """
    highest = 0
    for fn in os.listdir(HERE):
        if not fn.endswith(".py"):
            continue
        try:
            with open(os.path.join(HERE, fn), "r", encoding="utf-8") as fh:
                body = fh.read()
        except OSError:
            continue
        for num in re.findall(r"BV-Q-2026-(\d{3})", body):
            highest = max(highest, int(num))
    out_dir = os.path.join(HERE, "output")
    if os.path.isdir(out_dir):
        for fn in os.listdir(out_dir):
            for num in re.findall(r"BV-Q-2026-(\d{3})", fn):
                highest = max(highest, int(num))
    return highest


def next_quote_id(offset=1):
    """Return the next BV-Q-2026-NNN id (highest found + offset)."""
    return "BV-Q-2026-{:03d}".format(highest_quote_number() + offset)


# ---------------------------------------------------------------------------
# Build the quotation data structure from parsed slots.
# ---------------------------------------------------------------------------
class _QuoteData:
    """A lightweight stand-in for a content module (attribute access)."""

    def __init__(self, company, client, payment, terms, quotations):
        self.COMPANY = company
        self.CLIENT = client
        self.PAYMENT = payment
        self.TERMS = terms
        self.QUOTATIONS = quotations


def _timeline(n):
    if not n:
        return "10-14 working days"
    return "8-12 working days" if n <= 10 else (
        "12-16 working days" if n <= 30 else "14-18 working days")


def _delivery_section(hosting, seo, mention_domain=True, mention_hosting=True):
    seo_line = ("Full on-page SEO - titles, meta, sitemap & clean URLs"
                if seo else
                "Basic on-page SEO - titles, meta descriptions & clean URLs")
    if mention_hosting and hosting:
        last = ("Hosting included; deployment and help connecting your domain"
                if mention_domain else "Hosting included; deployment and launch")
    else:
        connect = []
        if mention_domain:
            connect.append("domain")
        if mention_hosting:
            connect.append("hosting")
        last = ("Deployment and help connecting your " + " & ".join(connect)
                if connect else "Deployment and launch of the website")
    return {
        "heading": "Design, SEO & delivery",
        "items": [
            "Modern design matched to your brand colours and logo",
            seo_line,
            "Fast-loading, mobile-first build",
            "Testing across major browsers and devices before launch",
            last,
        ],
    }


def _terms(slots, item_word):
    notes = ["All prices are in Indian Rupees (INR) and are one-time for the "
             "design & development work quoted."]
    if slots["reference"]:
        notes.append("{} is used only as a style / layout reference; this is a "
                     "custom build and not a copy of that site.".format(slots["reference"]))
    if slots.get("mention_domain", True):
        if (not slots["domain"] and not slots["hosting"]
                and slots.get("mention_hosting", True)):
            notes.append("Domain and hosting are NOT included; they are arranged and "
                         "paid for by the client directly. We will help set them up and "
                         "connect them.")
        elif not slots["domain"]:
            notes.append("The domain is NOT included; it is arranged and paid for by the "
                         "client directly. We will help connect it.")
    if slots["hosting"] and slots.get("mention_hosting", True):
        notes.append("Hosting is included. Renewal / upgrading to higher plans after "
                     "the first term is optional and charged separately.")
    if slots["count"] and slots.get("mention_count", True):
        notes.append("This package covers up to {} {}; additional {} can be added at a "
                     "small per-item charge.".format(slots["count"], item_word, item_word))
    if slots["payment"]:
        notes.append("The payment gateway account (and its transaction fees) and any "
                     "SMS / email / OTP service are arranged and paid for by the client "
                     "directly.")
    if slots["support_years"]:
        notes.append("{} year support covers bugs & errors only (things that stop "
                     "working). It does not cover content changes, new features or "
                     "redesigns.".format(slots["support_years"]))
    notes.append("Text, photos and content are provided by the client.")
    notes.append("Prices are exclusive of GST, if applicable.")
    return {
        "validity_days": 15,
        "payment": "50% advance to start, 50% on delivery (or as mutually agreed).",
        "notes": notes,
    }


# ---- ordering wording shared by all site types -------------------------------
_ORDER_SUMMARY = {
    "cart": "Customers browse your {items}, add them to the cart and check out "
            "securely with an integrated payment gateway (UPI / cards / net-banking "
            "/ wallets) or Cash on Delivery.",
    "enquiry": "Visitors browse your {items} and send an enquiry over WhatsApp or "
               "email, so every lead reaches you directly.",
    "booking": "Visitors explore your {items} and send a booking enquiry over "
               "WhatsApp or the enquiry form, so every lead reaches you directly.",
    "apply": "Candidates browse the {items} and apply through a simple form that "
             "reaches you directly.",
    "content": "Readers browse content by category, and you publish new {items} "
               "easily from the admin panel.",
    "leads": "Visitors explore what you offer and reach you through the enquiry "
             "form or WhatsApp, so every lead reaches you directly.",
}
_ORDER_FRONTEND = {
    "cart": ["Add to cart and smooth, secure checkout",
             "Order placement with order confirmation to you & the customer"],
    "enquiry": ["Enquiry / order-request form that reaches you directly",
                "Send enquiries over WhatsApp with one tap"],
    "booking": ["Booking / enquiry form that reaches you directly",
                "Send a booking request over WhatsApp with one tap"],
    "apply": ["Application / enquiry form that reaches you directly"],
    "content": ["Newsletter / subscribe block (optional)"],
    "leads": ["Enquiry / contact form that reaches you directly",
              "WhatsApp click-to-chat for quick enquiries"],
}
_ORDER_COVERED = {
    "cart": "Cart, secure checkout & Cash on Delivery",
    "enquiry": "Enquiry-based ordering over WhatsApp & email",
    "booking": "Booking / enquiry capture over WhatsApp & email",
    "apply": "Application / enquiry capture that reaches you directly",
    "content": "Category-based content with easy publishing",
    "leads": "Lead capture via enquiry form & WhatsApp",
}


def _features_subtitle(slots, payment_label):
    bits = []
    if slots["payment"]:
        bits.append(payment_label)
    if slots["admin"]:
        bits.append("backend admin panel")
    if slots.get("delivery"):
        bits.append("delivery management")
    if slots["seo"]:
        bits.append("SEO setup")
    if slots.get("blog"):
        bits.append("blog")
    if slots["hosting"] and slots.get("mention_hosting", True):
        bits.append("hosting")
    return bits


def _blog_gallery_bits(slots):
    """Extra (covered, frontend, admin) bullets for optional add-ons:
    blog / articles, image gallery and delivery management."""
    cov, front, adm = [], [], []
    if slots.get("delivery"):
        cov.append("Delivery options - delivery areas, slots & charges")
        front.append("Delivery area / pincode check with delivery charges at checkout")
        adm.append("Manage delivery areas, slots & charges; track deliveries")
    if slots.get("blog"):
        cov.append("Blog / articles section" +
                   (" (admin-managed)" if slots["admin"] else ""))
        front.append("Blog / articles section with featured posts & images")
        adm.append("Write, edit & publish blog posts with images")
    if slots.get("gallery"):
        cov.append("Image gallery / media section")
        front.append("Image gallery with lightbox")
        adm.append("Manage gallery images")
    return cov, front, adm


def _host_phrase(slots):
    """Closing sentence about hosting/domain, honouring 'don't mention' flags."""
    md = slots.get("mention_domain", True)
    mh = slots.get("mention_hosting", True)
    if mh and slots["hosting"]:
        return " Hosting is included."
    if md and mh:
        return (" Domain and hosting are arranged by you (not included), and we "
                "will help set them up.")
    if md:
        return " The domain is arranged by you (not included); we will help connect it."
    if mh:
        return " Hosting is arranged by you (not included)."
    return ""


def _build_store(slots, quote_id):
    niche = slots["niche"]
    show_count = slots.get("mention_count", True)
    n = slots["count"] or 20
    price = slots["price"] or 0
    word = niche["word"]
    mh = slots.get("mention_hosting", True)

    count_label = " ({} Products)".format(n) if show_count else ""
    if word:
        title = "{} E-Commerce Website".format(word) + count_label
        package_base = "{} Store".format(word)
    else:
        title = "E-Commerce Website" + count_label
        package_base = "Online Store"
    package = package_base + (" + Admin" if slots["admin"] else "")
    if slots["hosting"] and mh:
        package += " + Hosting"

    subtitle_bits = _features_subtitle(slots, "payment integration")
    subtitle = (niche["noun"].capitalize() + (" with " + ", ".join(subtitle_bits)
                if subtitle_bits else ""))
    if not slots["domain"] and slots.get("mention_domain", True):
        subtitle += " (domain not included)"
    if slots["reference"]:
        subtitle += " - style reference: {}".format(slots["reference"])

    ordering = "cart" if slots["payment"] else "enquiry"
    cov_extra, front_extra, adm_extra = _blog_gallery_bits(slots)

    catalogue_line = (
        "Up to {} product listings set up with photos, price & details".format(n)
        if show_count else
        "Product catalogue set up with photos, price & details")
    covered = [
        "Responsive {} (frontend)".format(niche["noun"]) +
        (" + backend admin panel" if slots["admin"] else ""),
        catalogue_line,
    ]
    if slots["payment"]:
        covered.append("Payment gateway integration (UPI / cards / net-banking / wallets)")
    covered.append(_ORDER_COVERED[ordering])
    if slots["admin"]:
        covered.append("Backend to manage products, orders & customers")
    covered += cov_extra
    covered.append("WhatsApp integration (click-to-chat button)")
    if slots["hosting"] and mh:
        covered.append("Hosting - included")
    if slots["support_years"]:
        covered.append("{} year bug & error support".format(slots["support_years"]))

    not_covered = []
    if not slots["domain"] and slots.get("mention_domain", True):
        not_covered.append("Domain - arranged and paid by the client (not included)")
    if not slots["hosting"] and mh:
        not_covered.append("Hosting - arranged and paid by the client (not included)")
    if slots["payment"]:
        not_covered.append("Payment gateway account & its transaction fees")
    not_covered.append("Product photos & content (provided by the client)")
    if show_count:
        not_covered.append(
            "Products beyond {} (added at a small per-product charge)".format(n))
    if slots["seo"]:
        not_covered.append("SMS / email / OTP service subscription")
        not_covered.append("Advanced SEO / marketing campaigns (separate service)")
    else:
        not_covered.append("SMS / email / OTP service subscription & SEO / marketing")

    order_sentence = _ORDER_SUMMARY[ordering].format(items="products")
    admin_phrase = (" A backend admin panel lets you manage products, orders and "
                    "customers from one dashboard." if slots["admin"] else "")
    ref_phrase = (" The design takes cues from {}.".format(slots["reference"])
                  if slots["reference"] else "")
    host_phrase = _host_phrase(slots)
    catalogue_phrase = ("with up to {} product listings".format(n) if show_count
                        else "with a full product catalogue")
    summary = ("A clean, ready-to-launch {} for a single seller {}. {}{}{}{}".format(
                   niche["noun"], catalogue_phrase, order_sentence, admin_phrase,
                   ref_phrase, host_phrase))

    front_listing = (
        "Up to {} product listings set up with photos, price and details".format(n)
        if show_count else
        "Product catalogue set up with photos, price and details")
    frontend = [
        "Home page with banners, featured products & categories",
        "Shop-by-collection layout ({})".format(niche["collections"]),
        "Product listing with search, sort & category filters",
        "Product detail page with image gallery, {} & price".format(niche["variants"]),
        front_listing,
    ]
    frontend += _ORDER_FRONTEND[ordering]
    frontend += front_extra
    frontend += [
        "WhatsApp click-to-chat button for quick enquiries",
        "Content pages: about, contact and policy pages",
        "Fully responsive across mobile, tablet & desktop",
    ]
    sections = [{"heading": "Customer-facing store (frontend)", "items": frontend}]

    if slots["payment"]:
        sections.append({
            "heading": "Payment gateway integration",
            "items": [
                "Integration of a leading Indian payment gateway "
                "(Razorpay / PayU / Cashfree or similar)",
                "Accept UPI, credit / debit cards, net-banking & wallets",
                "Secure checkout with order confirmation",
                "Cash on Delivery as an additional option",
            ],
        })
    if slots["admin"]:
        admin_items = [
            "Secure admin login for the store owner",
            "Add, edit and remove products, collections & variants",
            "Upload product photos and set price, stock and status",
            "Order management - view orders and update status "
            "(new / shipped / delivered)",
            "Basic customer list and enquiries",
        ]
        admin_items += adm_extra
        admin_items += [
            "Homepage banner & featured-collection management",
            "A short walkthrough so you are comfortable running the store",
        ]
        sections.append({"heading": "Backend admin panel", "items": admin_items})
    sections.append(_delivery_section(slots["hosting"], slots["seo"], slots.get("mention_domain", True), slots.get("mention_hosting", True)))

    quote = {
        "id": quote_id or next_quote_id(),
        "package": package,
        "title": title,
        "subtitle": subtitle,
        "price": price,
        "price_note": "one-time (design & development)",
        "timeline": _timeline(n),
        "summary": summary,
        "sections": sections,
        "support": {
            "title": "What's included & what's not",
            "left_label": "Included in this package",
            "right_label": "Not included",
            "covered": covered, "not_covered": not_covered,
        },
    }
    client = {"name": "Prospective Client", "company": "Confidential",
              "note": "{}{}".format(title, " - reference: {}".format(slots["reference"])
                                    if slots["reference"] else "")}
    return _QuoteData(COMPANY, client, PAYMENT, _terms(slots, "products"), [quote])


def _build_site(slots, quote_id):
    cfg = slots["cfg"]
    n = slots["count"] if slots.get("mention_count", True) else None
    price = slots["price"] or 0
    item = cfg["item"]
    ordering = cfg["ordering"]
    admin = slots["admin"]  # default already resolved in parse_command
    mh = slots.get("mention_hosting", True)

    count_label = slots["count_word"] or cfg["count_word"]
    title = cfg["title"] + (" ({} {})".format(n, count_label) if n else "")
    package = cfg["package"] + (" + Admin" if admin else "")
    if slots["hosting"] and mh:
        package += " + Hosting"

    payment_label = ("online booking payments" if ordering in ("booking",)
                     else "online payments")
    subtitle_bits = _features_subtitle(slots, payment_label)
    subtitle = (cfg["noun"].capitalize() +
                (" with " + ", ".join(subtitle_bits) if subtitle_bits else ""))
    if n:
        subtitle += " ({} {})".format(n, count_label.lower())
    if not slots["domain"] and slots.get("mention_domain", True):
        subtitle += " (domain not included)"
    if slots["reference"]:
        subtitle += " - style reference: {}".format(slots["reference"])

    cov_extra, front_extra, adm_extra = _blog_gallery_bits(slots)

    # ---- summary ----
    order_sentence = _ORDER_SUMMARY[ordering].format(items=item)
    admin_phrase = (" A backend admin panel lets you manage {} from one "
                    "dashboard.".format(cfg["admin_manage"]) if admin else "")
    pay_phrase = (" Online payment is integrated for advances / bookings."
                  if slots["payment"] else "")
    blog_phrase = (" A blog / articles section keeps your content fresh."
                   if slots.get("blog") else "")
    ref_phrase = (" The design takes cues from {}.".format(slots["reference"])
                  if slots["reference"] else "")
    host_phrase = _host_phrase(slots)
    lead = ("A clean, ready-to-launch {}".format(cfg["noun"]) +
            (" with up to {} {}".format(n, item) if n else "") + ". ")
    summary = (lead + order_sentence + admin_phrase + pay_phrase + blog_phrase +
               ref_phrase + host_phrase)

    # ---- frontend section ----
    frontend = ["Home page with hero banner, highlights & clear calls-to-action"]
    frontend += cfg["frontend_extra"]
    if n:
        frontend.append("Up to {} {} set up with images & details".format(n, item))
    frontend += _ORDER_FRONTEND[ordering]
    frontend += front_extra
    frontend += [
        "Content pages: about, contact and policy pages",
        "Fully responsive across mobile, tablet & desktop",
    ]
    sections = [{"heading": "Customer-facing website (frontend)", "items": frontend}]

    if slots["payment"]:
        sections.append({
            "heading": "Online payment",
            "items": [
                "Integration of a leading Indian payment gateway "
                "(Razorpay / PayU / Cashfree or similar)",
                "Accept UPI, cards, net-banking & wallets",
                "Collect advance / booking payments online with confirmation",
            ],
        })
    if admin:
        admin_items = [
            "Secure admin login",
            "Manage {}".format(cfg["admin_manage"]),
        ]
        if n:
            admin_items.append("Add, edit and remove {}".format(item))
        if ordering == "content":
            admin_items.append("Create, publish & schedule posts")
        else:
            admin_items.append("View and manage enquiries / leads")
        admin_items += adm_extra
        admin_items += [
            "Homepage banner & highlights management",
            "A short walkthrough so you are comfortable running it",
        ]
        sections.append({"heading": "Backend admin panel", "items": admin_items})

    sections.append(_delivery_section(slots["hosting"], slots["seo"], slots.get("mention_domain", True), slots.get("mention_hosting", True)))

    # ---- includes / excludes ----
    covered = ["Responsive {} (frontend)".format(cfg["noun"]) +
               (" + backend admin panel" if admin else "")]
    if n:
        covered.append("Up to {} {} set up with images & details".format(n, item))
    if slots["payment"]:
        covered.append("Online payment (UPI / cards) for advances / bookings")
    covered.append(_ORDER_COVERED[ordering])
    if admin:
        covered.append("Backend to manage {}".format(cfg["admin_manage"]))
    covered += cov_extra
    covered.append("WhatsApp integration (click-to-chat button)")
    if slots["seo"]:
        covered.append("On-page SEO setup (titles, meta, sitemap)")
    if slots["hosting"] and mh:
        covered.append("Hosting - included")
    if slots["support_years"]:
        covered.append("{} year bug & error support".format(slots["support_years"]))

    not_covered = []
    if not slots["domain"] and slots.get("mention_domain", True):
        not_covered.append("Domain - arranged and paid by the client (not included)")
    if not slots["hosting"] and mh:
        not_covered.append("Hosting - arranged and paid by the client (not included)")
    if slots["payment"]:
        not_covered.append("Payment gateway account & its transaction fees")
    not_covered.append("Text, photos & content (provided by the client)")
    if n:
        not_covered.append("Additional {} beyond {} (small per-item charge)".format(item, n))
    not_covered.append("Advanced SEO / marketing campaigns (separate service)")

    quote = {
        "id": quote_id or next_quote_id(),
        "package": package,
        "title": title,
        "subtitle": subtitle,
        "price": price,
        "price_note": "one-time (design & development)",
        "timeline": _timeline(n),
        "summary": summary,
        "sections": sections,
        "support": {
            "title": "What's included & what's not",
            "left_label": "Included in this package",
            "right_label": "Not included",
            "covered": covered, "not_covered": not_covered,
        },
    }
    client = {"name": "Prospective Client", "company": "Confidential",
              "note": "{}{}".format(title, " - reference: {}".format(slots["reference"])
                                    if slots["reference"] else "")}
    return _QuoteData(COMPANY, client, PAYMENT, _terms(slots, item), [quote])


def build_quote_data(slots, quote_id=None):
    if slots["kind"] == "store":
        return _build_store(slots, quote_id)
    return _build_site(slots, quote_id)


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------
def _type_label(slots):
    if slots["kind"] == "store":
        w = slots["niche"]["word"]
        return "{} store (e-commerce)".format(w) if w else "E-commerce store"
    return slots["cfg"]["title"]


def summarize(slots):
    yn = lambda b: "yes" if b else "no"
    if not slots.get("mention_count", True):
        items = "not mentioned"
    elif slots["count"]:
        items = "{} {}".format(slots["count"], (slots["count_word"] or "").lower())
    else:
        items = "none"
    if not slots.get("mention_domain", True):
        domain = "not mentioned"
    else:
        domain = "included" if slots["domain"] else "client arranges"
    if not slots.get("mention_hosting", True):
        hosting = "not mentioned"
    else:
        hosting = "included" if slots["hosting"] else "client arranges"
    return (
        "  Type       : {}\n"
        "  Items      : {}\n"
        "  Price      : {}\n"
        "  Payment    : {}\n"
        "  Admin panel: {}\n"
        "  SEO        : {}\n"
        "  Blog       : {}\n"
        "  Delivery   : {}\n"
        "  Domain     : {}\n"
        "  Hosting    : {}\n"
        "  Support    : {}\n"
        "  Reference  : {}".format(
            _type_label(slots),
            items,
            ("\u20b9{:,}".format(slots["price"]) if slots["price"] else "(not given!)"),
            yn(slots["payment"]),
            yn(slots["admin"]),
            yn(slots["seo"]),
            yn(slots.get("blog")),
            yn(slots.get("delivery")),
            domain,
            hosting,
            "{} year".format(slots["support_years"]) if slots["support_years"] else "none",
            slots["reference"] or "none",
        ))


def generate(command, dry_run=False):
    """Parse a command and build the PDF. Returns (slots, output_path|None)."""
    slots = parse_command(command)
    if dry_run:
        return slots, None
    build_quotes.data = build_quote_data(slots)
    outputs = build_quotes.build()
    return slots, (outputs[0] if outputs else None)


# ---------------------------------------------------------------------------
# CLI / chat loop
# ---------------------------------------------------------------------------
def _run_once(command, dry_run):
    slots = parse_command(command)
    print("Parsed:")
    print(summarize(slots))
    if slots["price"] is None:
        print("\n! No price detected. Add something like '8k' or 'rs 8000'.")
    if dry_run:
        return
    build_quotes.data = build_quote_data(slots)
    outputs = build_quotes.build()
    if outputs:
        print("\nDone -> {}".format(outputs[0]))


def _chat_loop():
    print("Bhama Vision quote bot. Type a command, or 'quit' to exit.")
    print("e.g. travel website 50 packages with admin 1 year support 12k\n")
    while True:
        try:
            line = input("quote> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        if line.lower() in ("quit", "exit", "q"):
            break
        try:
            _run_once(line, dry_run=False)
        except Exception as exc:  # keep the loop alive on bad input
            print("! Could not build quote:", exc)
        print()


def main(argv):
    dry_run = False
    args = []
    for a in argv:
        if a in ("--dry-run", "-n"):
            dry_run = True
        else:
            args.append(a)
    if args:
        _run_once(" ".join(args), dry_run)
    else:
        _chat_loop()


if __name__ == "__main__":
    main(sys.argv[1:])
