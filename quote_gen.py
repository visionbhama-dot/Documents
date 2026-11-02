"""
Bhama Vision - command-driven quotation generator ("quote bot").

Type a plain-English command and it builds a branded A4 PDF quotation in
seconds, using the SAME renderer (`build_quotes.py`) as every hand-written
quote. No external AI / API is used - it runs fully offline. It reads the
command, pulls out the details (niche, product count, price, payment,
admin, domain, hosting, reference site, support) and fills the quotation
template, then auto-assigns the next BV-Q number.

USAGE

    # one-shot: pass the command as an argument
    python3 quote_gen.py "ecommerce jewellery website 40 products payment integration no domain with hosting admin panel 8k"

    # see what it parsed without building
    python3 quote_gen.py --dry-run "ecommerce 25 products payment admin 8k ref lukaoriginals.com"

    # interactive chat mode: type commands at the prompt, Ctrl-D / 'quit' to exit
    python3 quote_gen.py

EXAMPLES OF COMMANDS

    ecommerce website payment integration 30 products, website + admin, no domain, with hosting, 6k
    jewellery ecommerce 40 products with payment integration no domain with hosting admin panel 8k
    apparel ecommerce 25 products payment admin 8k reference lukaoriginals.com

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
# Niche dictionary - maps keywords in the command to store wording.
# "variants" / "collections" drive the niche-specific frontend bullets.
# ---------------------------------------------------------------------------
NICHES = [
    {
        "keys": ["jewellery", "jewelry", "jeweller", "jeweler"],
        "word": "Jewellery",
        "noun": "online jewellery store",
        "collections": "rings, necklaces, earrings & bangles",
        "variants": "metal / size variants",
    },
    {
        "keys": ["apparel", "clothing", "fashion", "t-shirt", "tshirt",
                 "hoodie", "streetwear", "garment"],
        "word": "Apparel",
        "noun": "online clothing store",
        "collections": "t-shirts, hoodies & sweatshirts",
        "variants": "size & colour variants",
    },
    {
        "keys": ["perfume", "fragrance", "attar"],
        "word": "Perfume",
        "noun": "online perfume store",
        "collections": "eau de parfum, attars & gift sets",
        "variants": "size / volume variants",
    },
    {
        "keys": ["grocery", "kirana", "supermarket"],
        "word": "Grocery",
        "noun": "online grocery store",
        "collections": "staples, snacks, beverages & household",
        "variants": "weight / pack-size variants",
    },
    {
        "keys": ["optical", "eyewear", "spectacle", "sunglass"],
        "word": "Optical",
        "noun": "online optical store",
        "collections": "eyeglasses, sunglasses & lenses",
        "variants": "frame / lens variants",
    },
    {
        "keys": ["footwear", "shoe", "sneaker"],
        "word": "Footwear",
        "noun": "online footwear store",
        "collections": "sneakers, formals & sandals",
        "variants": "size & colour variants",
    },
    {
        "keys": ["cosmetic", "beauty", "skincare", "makeup"],
        "word": "Beauty",
        "noun": "online beauty & cosmetics store",
        "collections": "skincare, makeup & haircare",
        "variants": "shade / size variants",
    },
    {
        "keys": ["electronic", "gadget", "appliance"],
        "word": "Electronics",
        "noun": "online electronics store",
        "collections": "phones, accessories & appliances",
        "variants": "model / colour variants",
    },
    {
        "keys": ["furniture", "home decor", "decor", "homeware"],
        "word": "Home Decor",
        "noun": "online home & decor store",
        "collections": "furniture, lighting & decor",
        "variants": "size / finish variants",
    },
    {
        "keys": ["food", "bakery", "snack", "sweet"],
        "word": "Food",
        "noun": "online food store",
        "collections": "snacks, sweets & packaged food",
        "variants": "weight / pack-size variants",
    },
]

DEFAULT_NICHE = {
    "keys": [],
    "word": "E-Commerce",
    "noun": "online store",
    "collections": "featured products & categories",
    "variants": "variants",
}


# ---------------------------------------------------------------------------
# Command parsing
# ---------------------------------------------------------------------------
def _flag(text, positive, negative):
    """Return True / False / None for an include-or-not feature.

    positive / negative are lists of phrases. None means 'not mentioned'.
    """
    for p in negative:
        if p in text:
            return False
    for p in positive:
        if p in text:
            return True
    return None


def parse_command(command):
    """Turn a plain-English command into a dict of quotation slots."""
    text = " " + command.lower().strip() + " "

    # Product count: "25 products", "40 product listings".
    products = None
    m = re.search(r"(\d+)\s*products?\b", text)
    if m:
        products = int(m.group(1))

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
    payment = _flag(text, ["payment", "razorpay", "payu", "cashfree", "gateway"],
                    ["no payment", "without payment"])
    admin = _flag(text, ["admin", "backend", "dashboard", "cms"],
                  ["no admin", "without admin"])
    domain = _flag(text, ["with domain", "domain included", "including domain"],
                   ["no domain", "without domain", "domain not"])
    hosting = _flag(text, ["with hosting", "hosting included", "including hosting",
                           "free hosting"],
                    ["no hosting", "without hosting", "hosting not"])

    # Support duration: "1 year support".
    support_years = None
    m = re.search(r"(\d+)\s*year", text)
    if m:
        support_years = int(m.group(1))

    # Reference site: first domain-looking token that isn't ours.
    reference = None
    for cand in re.findall(r"\b([a-z0-9][a-z0-9-]*\.(?:com|in|co|net|org|store|shop|io)(?:\.[a-z]{2})?)\b", text):
        if "bhamavision" not in cand:
            reference = cand
            break

    # Niche.
    niche = DEFAULT_NICHE
    for n in NICHES:
        if any(k in text for k in n["keys"]):
            niche = n
            break

    return {
        "products": products,
        "price": price,
        "payment": True if payment is None else payment,
        "admin": True if admin is None else admin,
        "domain": False if domain is None else domain,      # default: client arranges
        "hosting": False if hosting is None else hosting,    # default: client arranges
        "support_years": support_years,
        "reference": reference,
        "niche": niche,
        "raw": command.strip(),
    }


# ---------------------------------------------------------------------------
# ID assignment
# ---------------------------------------------------------------------------
def highest_quote_number():
    """Return the highest BV-Q-2026-NNN number found in the repo (int)."""
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


def build_quote_data(slots, quote_id=None):
    niche = slots["niche"]
    n = slots["products"] or 20
    price = slots["price"] or 0
    word = niche["word"]

    timeline = "8-12 working days" if n <= 10 else (
        "12-16 working days" if n <= 30 else "14-18 working days")

    package = "{} Store + Admin".format(word) if slots["admin"] else \
        "{} Store".format(word)
    if slots["hosting"]:
        package += " + Hosting"

    title = "{} E-Commerce Website ({} Products)".format(word, n)

    subtitle_bits = []
    if slots["payment"]:
        subtitle_bits.append("payment integration")
    if slots["admin"]:
        subtitle_bits.append("backend admin panel")
    if slots["hosting"]:
        subtitle_bits.append("hosting")
    subtitle = "{} with ".format(niche["noun"].capitalize()) + \
        ", ".join(subtitle_bits) if subtitle_bits else niche["noun"].capitalize()
    if not slots["domain"]:
        subtitle += " (domain not included)"
    if slots["reference"]:
        subtitle += " - style reference: {}".format(slots["reference"])

    # ---- includes / excludes ----
    covered = [
        "Responsive {} (frontend)".format(niche["noun"]) +
        (" + backend admin panel" if slots["admin"] else ""),
        "Up to {} product listings set up with photos, price & details".format(n),
    ]
    if slots["payment"]:
        covered.append("Payment gateway integration (UPI / cards / net-banking / wallets)")
        covered.append("Cart, secure checkout & Cash on Delivery")
    else:
        covered.append("Cart & enquiry-based ordering over WhatsApp & email")
    if slots["admin"]:
        covered.append("Backend to manage products, orders & customers")
    covered.append("WhatsApp integration (click-to-chat button)")
    if slots["hosting"]:
        covered.append("Hosting - included")
    if slots["support_years"]:
        covered.append("{} year bug & error support".format(slots["support_years"]))

    not_covered = []
    if not slots["domain"]:
        not_covered.append("Domain - arranged and paid by the client (not included)")
    if not slots["hosting"]:
        not_covered.append("Hosting - arranged and paid by the client (not included)")
    if slots["payment"]:
        not_covered.append("Payment gateway account & its transaction fees")
    not_covered += [
        "Product photos & content (provided by the client)",
        "Products beyond {} (added at a small per-product charge)".format(n),
        "SMS / email / OTP service subscription & SEO / marketing",
    ]

    requirements = {
        "title": "What's included & what's not",
        "left_label": "Included in this package",
        "right_label": "Not included",
        "covered": covered,
        "not_covered": not_covered,
    }

    # ---- summary ----
    if slots["payment"]:
        order_sentence = (
            "Customers browse your products, add them to the cart and check out "
            "securely with an integrated payment gateway (UPI / cards / "
            "net-banking / wallets) or Cash on Delivery.")
    else:
        order_sentence = (
            "Customers browse your products and place an order by sending you an "
            "enquiry over WhatsApp or email, so every lead reaches you directly.")
    admin_phrase = (" A backend admin panel lets you manage products, orders "
                    "and customers from one dashboard." if slots["admin"] else "")
    ref_phrase = (" The design takes cues from {}.".format(slots["reference"])
                  if slots["reference"] else "")
    host_phrase = (" Hosting is included." if slots["hosting"]
                   else " Domain and hosting are arranged by you (not included), "
                        "and we will help set them up.")
    summary = (
        "A clean, ready-to-launch {} for a single seller with up to {} product "
        "listings. {}{}{}{}".format(
            niche["noun"], n, order_sentence, admin_phrase, ref_phrase, host_phrase)
    )

    # ---- sections ----
    frontend = [
        "Home page with banners, featured products & categories",
        "Shop-by-collection layout ({})".format(niche["collections"]),
        "Product listing with search, sort & category filters",
        "Product detail page with image gallery, {} & price".format(niche["variants"]),
        "Up to {} product listings set up with photos, price and details".format(n),
    ]
    if slots["payment"]:
        frontend += [
            "Add to cart and smooth, secure checkout",
            "Order placement with order confirmation to you & the customer",
        ]
    else:
        frontend += [
            "Add to cart / build an enquiry list",
            "Place an order by sending an enquiry over WhatsApp & email",
            "Enquiry / order-request form that reaches you directly",
        ]
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
        sections.append({
            "heading": "Backend admin panel",
            "items": [
                "Secure admin login for the store owner",
                "Add, edit and remove products, collections & variants",
                "Upload product photos and set price, stock and status",
                "Order management - view orders and update status "
                "(new / shipped / delivered)",
                "Basic customer list and enquiries",
                "Homepage banner & featured-collection management",
                "A short walkthrough so you are comfortable running the store",
            ],
        })

    delivery_last = ("Hosting included; deployment and help connecting your domain"
                     if slots["hosting"]
                     else "Deployment and help connecting your domain & hosting")
    sections.append({
        "heading": "Design, SEO & delivery",
        "items": [
            "Modern design matched to your brand colours and logo",
            "Basic on-page SEO - titles, meta descriptions & clean URLs",
            "Fast-loading, mobile-first build",
            "Testing across major browsers and devices before launch",
            delivery_last,
        ],
    })

    quote = {
        "id": quote_id or next_quote_id(),
        "package": package,
        "title": title,
        "subtitle": subtitle,
        "price": price,
        "price_note": "one-time (design & development)",
        "timeline": timeline,
        "summary": summary,
        "sections": sections,
        "support": requirements,
    }

    # ---- terms ----
    notes = [
        "All prices are in Indian Rupees (INR) and are one-time for the design & development work quoted.",
    ]
    if slots["reference"]:
        notes.append("{} is used only as a style / layout reference; this is a "
                      "custom build and not a copy of that site.".format(slots["reference"]))
    if not slots["domain"] and not slots["hosting"]:
        notes.append("Domain and hosting are NOT included; they are arranged and paid "
                     "for by the client directly. We will help set them up and connect them.")
    elif not slots["domain"]:
        notes.append("The domain is NOT included; it is arranged and paid for by the "
                     "client directly. We will help connect it to the store.")
    if slots["hosting"]:
        notes.append("Hosting is included. Renewal / upgrading to higher plans after the "
                     "first term is optional and charged separately.")
    notes.append("This package covers up to {} product listings; additional products are "
                 "added at a small per-product charge.".format(n))
    if slots["payment"]:
        notes.append("The payment gateway account (and its transaction fees) and any SMS / "
                     "email / OTP service are arranged and paid for by the client directly.")
    if slots["support_years"]:
        notes.append("{} year support covers bugs & errors only (things that stop working). "
                     "It does not cover content changes, new features or redesigns.".format(
                         slots["support_years"]))
    notes.append("Product photos and content are provided by the client.")
    notes.append("Prices are exclusive of GST, if applicable.")

    terms = {
        "validity_days": 15,
        "payment": "50% advance to start, 50% on delivery (or as mutually agreed).",
        "notes": notes,
    }

    client = {
        "name": "Prospective Client",
        "company": "Confidential",
        "note": "{} ({} products){}".format(
            title, n,
            " - reference: {}".format(slots["reference"]) if slots["reference"] else ""),
    }

    return _QuoteData(COMPANY, client, PAYMENT, terms, [quote])


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------
def summarize(slots):
    niche = slots["niche"]
    yn = lambda b: "yes" if b else "no"
    return (
        "  Niche      : {}\n"
        "  Products   : {}\n"
        "  Price      : {}\n"
        "  Payment    : {}\n"
        "  Admin panel: {}\n"
        "  Domain     : {}\n"
        "  Hosting    : {}\n"
        "  Support    : {}\n"
        "  Reference  : {}".format(
            niche["word"],
            slots["products"] or "(default 20)",
            ("\u20b9{:,}".format(slots["price"]) if slots["price"] else "(not given!)"),
            yn(slots["payment"]),
            yn(slots["admin"]),
            "included" if slots["domain"] else "client arranges",
            "included" if slots["hosting"] else "client arranges",
            "{} year".format(slots["support_years"]) if slots["support_years"] else "none",
            slots["reference"] or "none",
        ))


def generate(command, dry_run=False):
    """Parse a command and build the PDF. Returns (slots, output_path|None)."""
    slots = parse_command(command)
    if dry_run:
        return slots, None
    data = build_quote_data(slots)
    build_quotes.data = data
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
        print("\n! No price detected. Add something like '8k' or 'rs 8000' to the command.")
    if dry_run:
        return
    data = build_quote_data(slots)
    build_quotes.data = data
    outputs = build_quotes.build()
    if outputs:
        print("\nDone -> {}".format(outputs[0]))


def _chat_loop():
    print("Bhama Vision quote bot. Type a command, or 'quit' to exit.")
    print("e.g. jewellery ecommerce 40 products payment integration no domain with hosting admin 8k\n")
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
