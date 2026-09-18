"""
Bhama Vision - A4 PDF receipt builder.

Renders each receipt defined in `receipts.py` to a branded, print-ready A4
PDF in the `output/` folder. Shares the Bhama Vision look (logo, fonts,
colours) with the quotation and invoice builders.

A receipt acknowledges money RECEIVED (unlike an invoice, which requests
payment), so it shows "Received from", the amount received and a
"RECEIVED" confirmation instead of a balance due.

    python3 build_receipts.py
"""
import os

from datetime import date

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas

# Reuse the branding + helpers already defined for the quotations.
from build_quotes import (_register_fonts, rupee, ASSETS, OUTPUT,
                          PAGE_W, PAGE_H, MARGIN, INK, MUTED, YELLOW,
                          LINE, CARD)
import receipts as data

ON_YELLOW = HexColor("#6E6600")   # readable text on the yellow accent


def amount_in_words(n):
    """Return an Indian-English words form of a whole rupee amount."""
    n = int(n)
    if n == 0:
        return "Zero"
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
            "Seventy", "Eighty", "Ninety"]

    def two(x):
        if x < 20:
            return ones[x]
        return tens[x // 10] + (" " + ones[x % 10] if x % 10 else "")

    def three(x):
        h = x // 100
        r = x % 100
        s = ""
        if h:
            s = ones[h] + " Hundred"
            if r:
                s += " "
        if r:
            s += two(r)
        return s

    parts = []
    crore = n // 10000000
    n %= 10000000
    lakh = n // 100000
    n %= 100000
    thousand = n // 1000
    n %= 1000
    hundred = n
    if crore:
        parts.append(three(crore) + " Crore")
    if lakh:
        parts.append(two(lakh) + " Lakh")
    if thousand:
        parts.append(two(thousand) + " Thousand")
    if hundred:
        parts.append(three(hundred))
    return " ".join(parts).strip()


class Receipt:
    """Draws one receipt on a single A4 page (extends if needed)."""

    def __init__(self, c, rc):
        self.c = c
        self.rc = rc
        self.logo = ImageReader(os.path.join(ASSETS, "logo.png"))
        iw, ih = self.logo.getSize()
        self.logo_ratio = iw / ih
        self.page = 0
        self.right = PAGE_W - MARGIN
        self.max_w = PAGE_W - 2 * MARGIN

    # ---- text helpers ----
    def _wrap(self, text, font, size, max_w):
        words, lines, cur = text.split(), [], ""
        for w in words:
            trial = w if not cur else cur + " " + w
            if pdfmetrics.stringWidth(trial, font, size) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines or [""]

    def _logo(self, x, top, box_w, box_h):
        w = box_w
        h = w / self.logo_ratio
        if h > box_h:
            h = box_h
            w = h * self.logo_ratio
        yy = top - box_h + (box_h - h) / 2.0
        self.c.drawImage(self.logo, x, yy, width=w, height=h, mask="auto")

    # ---- page scaffolding ----
    def _header(self):
        c = self.c
        band = 78
        self._logo(MARGIN, PAGE_H - 12, 54, 54)
        c.setFillColor(MUTED)
        c.setFont("Noto-Md", 8.5)
        c.drawRightString(self.right, PAGE_H - 34,
                          "RECEIPT  \u00b7  " + self.rc["id"])
        c.setFillColor(INK)
        c.setFont("Noto-Sb", 9.5)
        c.drawRightString(self.right, PAGE_H - 48, self.rc["from"]["name"])
        yline = PAGE_H - band
        c.setStrokeColor(LINE)
        c.setLineWidth(1)
        c.line(MARGIN, yline, self.right, yline)
        c.setFillColor(YELLOW)
        c.rect(MARGIN, yline - 1.5, 54, 3, fill=1, stroke=0)

    def _footer(self):
        c = self.c
        y = 40
        c.setStrokeColor(LINE)
        c.setLineWidth(0.8)
        c.line(MARGIN, y + 12, self.right, y + 12)
        c.setFillColor(MUTED)
        c.setFont("Noto", 8)
        c.drawString(MARGIN, y,
                     "{name}  \u00b7  {email}  \u00b7  {phone}".format(
                         **data.COMPANY))
        c.drawRightString(self.right, y, "Page {}".format(self.page))

    def _new_page(self, first=False):
        if not first:
            self.c.showPage()
        self.page += 1
        self._header()
        self._footer()
        self.y = PAGE_H - 78 - 26

    def _ensure(self, needed):
        if self.y - needed < 66:
            self._new_page()

    def _mini_title(self, text):
        self._ensure(40)
        c = self.c
        c.setFillColor(YELLOW)
        c.rect(MARGIN, self.y + 1, 22, 4, fill=1, stroke=0)
        self.y -= 16
        c.setFillColor(INK)
        c.setFont("Noto-Xb", 11)
        c.drawString(MARGIN, self.y, text)
        self.y -= 16

    # ---- content blocks ----
    def _title(self):
        c = self.c
        c.setFillColor(INK)
        c.setFont("Noto-Blk", 30)
        c.drawString(MARGIN, self.y, "Receipt")
        self.y -= 30

    def _meta_block(self):
        c = self.c
        rc = self.rc
        top = self.y
        # Left - received from
        c.setFillColor(MUTED)
        c.setFont("Noto-Md", 8.5)
        c.drawString(MARGIN, top, "RECEIVED FROM")
        c.setFillColor(INK)
        c.setFont("Noto-Sb", 13)
        c.drawString(MARGIN, top - 19, rc["from"]["name"])
        yy = top - 35
        c.setFillColor(MUTED)
        c.setFont("Noto", 9.5)
        for ln in rc["from"].get("lines", []):
            c.drawString(MARGIN, yy, ln)
            yy -= 13
        # Right - meta
        today = date.today()
        meta = [
            ("Receipt No.", rc["id"]),
            ("Date", rc.get("date") or today.strftime("%d %b %Y")),
        ]
        if rc.get("mode"):
            meta.append(("Payment mode", rc["mode"]))
        # Only surface a total / balance when this is a part payment.
        total = rc.get("total")
        if total and int(total) > int(rc["amount"]):
            meta.append(("Total amount", rupee(total)))
            meta.append(("Balance due", rupee(int(total) - int(rc["amount"]))))
        my = top
        lbl_x = self.right - 220
        for k, v in meta:
            c.setFillColor(MUTED)
            c.setFont("Noto-Md", 9)
            c.drawString(lbl_x, my, k)
            c.setFillColor(INK)
            c.setFont("Noto-Sb", 10)
            c.drawRightString(self.right, my, v)
            my -= 17
        self.y = min(yy, my) - 8
        c.setStrokeColor(LINE)
        c.setLineWidth(1)
        c.line(MARGIN, self.y, self.right, self.y)
        self.y -= 20

    def _statement(self):
        c = self.c
        rc = self.rc
        words = amount_in_words(rc["amount"])
        text = ("Received with thanks from {name} the sum of {amt} "
                "(Rupees {words} only){forp}.").format(
            name=rc["from"]["name"],
            amt=rupee(rc["amount"]),
            words=words,
            forp=(" towards " + rc["for"]) if rc.get("for") else "")
        c.setFillColor(INK)
        c.setFont("Noto", 10.5)
        for ln in self._wrap(text, "Noto", 10.5, self.max_w):
            self._ensure(16)
            c.drawString(MARGIN, self.y, ln)
            self.y -= 15.5
        self.y -= 8

    def _amount_box(self):
        c = self.c
        self._ensure(70)
        box_h = 56
        top = self.y
        c.setFillColor(YELLOW)
        c.roundRect(MARGIN, top - box_h, self.max_w, box_h, 10,
                    fill=1, stroke=0)
        c.setFillColor(INK)
        c.roundRect(MARGIN, top - box_h, 5, box_h, 2, fill=1, stroke=0)
        c.setFillColor(ON_YELLOW)
        c.setFont("Noto-Sb", 9)
        c.drawString(MARGIN + 24, top - 24, "AMOUNT RECEIVED")
        # Subtitle: mention the balance only when this is a part payment;
        # for a full/standalone payment nothing extra is stated.
        total = self.rc.get("total")
        amount = int(self.rc["amount"])
        subtitle = None
        if total and int(total) > amount:
            subtitle = "Part payment \u00b7 balance due {}".format(
                rupee(int(total) - amount))
        big_y = top - 38 if subtitle else top - 40
        if subtitle:
            c.setFillColor(ON_YELLOW)
            c.setFont("Noto", 8.5)
            c.drawString(MARGIN + 24, top - 40, subtitle)
        c.setFillColor(INK)
        c.setFont("Noto-Blk", 30)
        c.drawRightString(self.right - 24, big_y, rupee(self.rc["amount"]))
        self.y = top - box_h - 20

    def _payment_and_notes(self):
        c = self.c
        p = getattr(data, "PAYMENT", None)
        if p:
            self._mini_title("Paid to")
            lines = [
                "Account name: " + p["account_name"],
                "Bank: " + p["bank"],
                "Account no.: " + p["account_no"],
                "IFSC: " + p["ifsc"],
            ]
            if p.get("upi"):
                lines.append("UPI: " + p["upi"])
            c.setFillColor(MUTED)
            c.setFont("Noto", 9.5)
            for ln in lines:
                self._ensure(13)
                c.drawString(MARGIN, self.y, ln)
                self.y -= 13
            self.y -= 8
        notes = getattr(data, "TERMS", {}).get("notes", [])
        if notes:
            self._mini_title("Notes")
            for n in notes:
                wrapped = self._wrap(n, "Noto", 9.5, self.max_w - 18)
                for j, ln in enumerate(wrapped):
                    self._ensure(13)
                    if j == 0:
                        c.setFillColor(YELLOW)
                        c.setFont("Noto-Bd", 9.5)
                        c.drawString(MARGIN + 2, self.y, "\u2022")
                    c.setFillColor(MUTED)
                    c.setFont("Noto", 9.5)
                    c.drawString(MARGIN + 16, self.y, ln)
                    self.y -= 13
                self.y -= 4

    def _signature(self):
        c = self.c
        self._ensure(70)
        self.y -= 20
        top = self.y
        x = self.right - 200
        c.setStrokeColor(HexColor("#BFBFBF"))
        c.setLineWidth(1)
        c.line(x, top, self.right, top)
        c.setFillColor(MUTED)
        c.setFont("Noto-Md", 9)
        c.drawString(x, top - 14, "Authorised signatory \u00b7 " +
                     data.COMPANY["name"])
        self.y = top - 30

    def render(self):
        self._new_page(first=True)
        self._title()
        self.y -= 6
        self._meta_block()
        self._statement()
        self._amount_box()
        self._payment_and_notes()
        self._signature()


def build():
    _register_fonts()
    os.makedirs(OUTPUT, exist_ok=True)
    outputs = []
    for rc in data.RECEIPTS:
        fname = "{}_{}.pdf".format(
            rc["id"], rc["from"]["name"].replace(" ", "-").replace("/", "-"))
        path = os.path.join(OUTPUT, fname)
        c = canvas.Canvas(path, pagesize=A4)
        c.setTitle("{} - Receipt {}".format(data.COMPANY["name"], rc["id"]))
        c.setAuthor(data.COMPANY["name"])
        Receipt(c, rc).render()
        c.showPage()
        c.save()
        outputs.append(path)
        print("Wrote", path)
    return outputs


if __name__ == "__main__":
    build()
