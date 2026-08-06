"""
Bhama Vision - A4 PDF invoice builder.

Renders each invoice defined in `invoices.py` to a branded, print-ready A4
PDF in the `output/` folder. Shares the Bhama Vision look (logo, fonts,
colours) with the quotation builder.

    python3 build_invoices.py
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
import invoices as data

ON_YELLOW = HexColor("#6E6600")   # readable text on the yellow accent


class Invoice:
    """Draws one invoice across as many A4 pages as needed."""

    def __init__(self, c, inv):
        self.c = c
        self.inv = inv
        self.logo = ImageReader(os.path.join(ASSETS, "logo.png"))
        iw, ih = self.logo.getSize()
        self.logo_ratio = iw / ih
        self.page = 0
        self.right = PAGE_W - MARGIN
        self.max_w = PAGE_W - 2 * MARGIN
        self.subtotal = 0

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
                          "INVOICE  \u00b7  " + self.inv["id"])
        c.setFillColor(INK)
        c.setFont("Noto-Sb", 9.5)
        c.drawRightString(self.right, PAGE_H - 48, self.inv["client"]["name"])
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
        c.drawString(MARGIN, self.y, "Invoice")
        self.y -= 30

    def _bill_block(self):
        c = self.c
        inv = self.inv
        top = self.y
        # Left - billed to
        c.setFillColor(MUTED)
        c.setFont("Noto-Md", 8.5)
        c.drawString(MARGIN, top, "BILLED TO")
        c.setFillColor(INK)
        c.setFont("Noto-Sb", 13)
        c.drawString(MARGIN, top - 19, inv["client"]["name"])
        yy = top - 35
        c.setFillColor(MUTED)
        c.setFont("Noto", 9.5)
        for ln in inv["client"].get("lines", []):
            c.drawString(MARGIN, yy, ln)
            yy -= 13
        # Right - meta
        today = date.today()
        meta = [
            ("Invoice No.", inv["id"]),
            ("Issue date", today.strftime("%d %b %Y")),
        ]
        my = top
        lbl_x = self.right - 200
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
        self.y -= 16

    def _items_table(self):
        c = self.c
        x_num, x_desc = 54, 78
        qty_c, rate_r, amount_r = 400, 480, self.right
        desc_w = 360 - x_desc
        # header row
        self._ensure(46)
        hbar_h = 20
        c.setFillColor(CARD)
        c.rect(MARGIN, self.y - hbar_h + 6, self.max_w, hbar_h,
               fill=1, stroke=0)
        c.setFillColor(MUTED)
        c.setFont("Noto-Sb", 8.5)
        ty = self.y - hbar_h + 11
        c.drawString(x_num, ty, "#")
        c.drawString(x_desc, ty, "DESCRIPTION")
        c.drawCentredString(qty_c, ty, "QTY")
        c.drawRightString(rate_r, ty, "RATE")
        c.drawRightString(amount_r, ty, "AMOUNT")
        self.y -= hbar_h + 10
        # rows
        subtotal = 0
        for i, it in enumerate(self.inv["items"], 1):
            desc_lines = self._wrap(it["desc"], "Noto-Sb", 10.5, desc_w)
            detail = it.get("detail", "")
            detail_lines = self._wrap(detail, "Noto", 8.5, desc_w) if detail \
                else []
            row_h = len(desc_lines) * 13.5 + len(detail_lines) * 11 + 12
            self._ensure(row_h)
            top = self.y
            amount = it["qty"] * it["rate"]
            subtotal += amount
            c.setFillColor(MUTED)
            c.setFont("Noto", 10)
            c.drawString(x_num, top, str(i))
            yy = top
            c.setFillColor(INK)
            c.setFont("Noto-Sb", 10.5)
            for ln in desc_lines:
                c.drawString(x_desc, yy, ln)
                yy -= 13.5
            if detail_lines:
                c.setFillColor(MUTED)
                c.setFont("Noto", 8.5)
                for ln in detail_lines:
                    c.drawString(x_desc, yy, ln)
                    yy -= 11
            c.setFillColor(INK)
            c.setFont("Noto", 10.5)
            c.drawCentredString(qty_c, top, str(it["qty"]))
            c.drawRightString(rate_r, top, rupee(it["rate"]))
            c.setFont("Noto-Sb", 10.5)
            c.drawRightString(amount_r, top, rupee(amount))
            self.y = yy - 6
            c.setStrokeColor(LINE)
            c.setLineWidth(0.8)
            c.line(MARGIN, self.y + 2, self.right, self.y + 2)
            self.y -= 10
        self.subtotal = subtotal

    def _totals(self):
        c = self.c
        tax_p = data.TERMS.get("tax_percent", 0)
        tax = round(self.subtotal * tax_p / 100)
        total = self.subtotal + tax
        self._ensure(80)
        lbl_x = self.right - 230
        c.setFillColor(MUTED)
        c.setFont("Noto-Md", 9.5)
        c.drawString(lbl_x, self.y, "Subtotal")
        c.setFillColor(INK)
        c.setFont("Noto-Sb", 10.5)
        c.drawRightString(self.right, self.y, rupee(self.subtotal))
        self.y -= 18
        if tax_p:
            c.setFillColor(MUTED)
            c.setFont("Noto-Md", 9.5)
            c.drawString(lbl_x, self.y, "Tax ({}%)".format(tax_p))
            c.setFillColor(INK)
            c.setFont("Noto-Sb", 10.5)
            c.drawRightString(self.right, self.y, rupee(tax))
            self.y -= 18
        # Total due box
        box_h = 34
        box_x = lbl_x - 14
        box_w = self.right - box_x
        box_top = self.y + 6
        c.setFillColor(YELLOW)
        c.roundRect(box_x, box_top - box_h, box_w, box_h, 6, fill=1, stroke=0)
        cy = box_top - box_h / 2
        c.setFillColor(ON_YELLOW)
        c.setFont("Noto-Sb", 9.5)
        c.drawString(box_x + 14, cy - 3, "TOTAL DUE")
        c.setFillColor(INK)
        c.setFont("Noto-Blk", 15)
        c.drawRightString(self.right - 14, cy - 5, rupee(total))
        self.y = box_top - box_h - 18

    def _payment_and_notes(self):
        c = self.c
        p = data.PAYMENT
        self._mini_title("Payment details")
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
        self._mini_title("Notes")
        for n in data.TERMS["notes"]:
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

    def render(self):
        self._new_page(first=True)
        self._title()
        self.y -= 6
        self._bill_block()
        self._items_table()
        self._totals()
        self._payment_and_notes()


def build():
    _register_fonts()
    os.makedirs(OUTPUT, exist_ok=True)
    outputs = []
    for inv in data.INVOICES:
        fname = "{}_{}.pdf".format(
            inv["id"], inv["client"]["name"].replace(" ", "-"))
        path = os.path.join(OUTPUT, fname)
        c = canvas.Canvas(path, pagesize=A4)
        c.setTitle("{} - Invoice {}".format(data.COMPANY["name"], inv["id"]))
        c.setAuthor(data.COMPANY["name"])
        Invoice(c, inv).render()
        c.showPage()
        c.save()
        outputs.append(path)
        print("Wrote", path)
    return outputs


if __name__ == "__main__":
    build()
