"""
Bhama Vision - A4 PDF quotation builder.

Renders each quotation defined in `quotations.py` to a branded, print-ready
A4 PDF in the `output/` folder.

    python3 build_quotes.py

Replace `assets/logo.png` with your real logo (transparent PNG, ~8:1 ratio)
to rebrand every document.
"""
import os
from datetime import date, timedelta

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

import quotations as data

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUTPUT = os.path.join(HERE, "output")
FONT_DIR = "/usr/share/fonts/google-noto"

# ---- Brand palette ---------------------------------------------------------
BLACK = HexColor("#0E0E0E")
PANEL = HexColor("#171717")
YELLOW = HexColor("#F0E40A")
WHITE = HexColor("#FFFFFF")
INK = HexColor("#1A1A1A")        # body text on white
MUTED = HexColor("#6E6E6E")      # secondary text
FAINT = HexColor("#9AA0A6")      # tertiary text on dark
LINE = HexColor("#E6E6E6")       # hairlines
CARD = HexColor("#F6F6F4")       # light card fill

PAGE_W, PAGE_H = A4              # 595.27 x 841.89 pt
MARGIN = 50


# ---- Fonts -----------------------------------------------------------------
def _register_fonts():
    faces = {
        "Noto": "NotoSans-Regular.ttf",
        "Noto-Md": "NotoSans-Medium.ttf",
        "Noto-Sb": "NotoSans-SemiBold.ttf",
        "Noto-Bd": "NotoSans-Bold.ttf",
        "Noto-Xb": "NotoSans-ExtraBold.ttf",
        "Noto-Blk": "NotoSans-Black.ttf",
        "Noto-Lt": "NotoSans-Light.ttf",
    }
    for name, fn in faces.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fn)))


def rupee(n):
    return "\u20b9{:,}".format(int(n))


# ---------------------------------------------------------------------------
class Quote:
    """Draws one quotation across as many A4 pages as needed."""

    def __init__(self, c, q):
        self.c = c
        self.q = q
        self.page = 0
        self.logo = ImageReader(os.path.join(ASSETS, "logo.png"))
        iw, ih = self.logo.getSize()
        self.logo_ratio = iw / ih

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

    def _para(self, text, font, size, x, max_w, leading, color=INK):
        c = self.c
        c.setFillColor(color)
        c.setFont(font, size)
        for ln in self._wrap(text, font, size, max_w):
            self._ensure(leading)
            c.drawString(x, self.y, ln)
            self.y -= leading
        return self.y

    # ---- page scaffolding ----
    def _logo(self, x, top, box_w, box_h):
        # Fit the logo inside a box, preserving aspect ratio; left aligned,
        # vertically centred. Works for wide or square logos.
        w = box_w
        h = w / self.logo_ratio
        if h > box_h:
            h = box_h
            w = h * self.logo_ratio
        yy = top - box_h + (box_h - h) / 2.0
        self.c.drawImage(self.logo, x, yy, width=w, height=h, mask="auto")
        return w, h

    def _content_header(self):
        c = self.c
        band = 78
        # Logo tile, top-left (renders the logo as-is on the white page)
        self._logo(MARGIN, PAGE_H - 12, 54, 54)
        # Right-aligned quotation meta
        c.setFillColor(MUTED)
        c.setFont("Noto-Md", 8.5)
        c.drawRightString(PAGE_W - MARGIN, PAGE_H - 34,
                          "QUOTATION  \u00b7  " + self.q["id"])
        c.setFillColor(INK)
        c.setFont("Noto-Sb", 9.5)
        c.drawRightString(PAGE_W - MARGIN, PAGE_H - 48, self.q["package"])
        # Divider under the header: hairline + short yellow accent
        yline = PAGE_H - band
        c.setStrokeColor(LINE)
        c.setLineWidth(1)
        c.line(MARGIN, yline, PAGE_W - MARGIN, yline)
        c.setFillColor(YELLOW)
        c.rect(MARGIN, yline - 1.5, 54, 3, fill=1, stroke=0)

    def _footer(self):
        c = self.c
        y = 40
        c.setStrokeColor(LINE)
        c.setLineWidth(0.8)
        c.line(MARGIN, y + 12, PAGE_W - MARGIN, y + 12)
        c.setFillColor(MUTED)
        c.setFont("Noto", 8)
        left = "{name}  \u00b7  {email}  \u00b7  {phone}".format(**data.COMPANY)
        c.drawString(MARGIN, y, left)
        c.setFillColor(YELLOW)
        c.rect(MARGIN, y - 0.5, 0, 0, fill=1, stroke=0)
        c.setFillColor(MUTED)
        c.drawRightString(PAGE_W - MARGIN, y, "Page {}".format(self.page))

    def _new_content_page(self, first=False):
        if not first:
            self.c.showPage()
        self.page += 1
        self._content_header()
        self._footer()
        self.y = PAGE_H - 78 - 26
        self.x = MARGIN
        self.max_w = PAGE_W - 2 * MARGIN

    def _ensure(self, needed):
        if self.y - needed < 66:
            self._new_content_page()

    # ---- building blocks ----
    def _section_title(self, text, keep=74):
        # `keep` reserves room for the heading plus the start of its content
        # so a heading never lands alone at the bottom of a page.
        self._ensure(keep)
        self.y -= 12
        c = self.c
        c.setFillColor(YELLOW)
        c.rect(MARGIN, self.y - 2, 26, 5, fill=1, stroke=0)
        self.y -= 20
        c.setFillColor(INK)
        c.setFont("Noto-Xb", 14)
        c.drawString(MARGIN, self.y, text)
        self.y -= 18

    def _bullets(self, items, muted=False):
        c = self.c
        size, leading, gap = 10, 13.5, 7
        text_color = MUTED if muted else INK
        mark = FAINT if muted else YELLOW
        for it in items:
            self._ensure(leading + gap)
            c.setFillColor(mark)
            c.setFont("Noto-Bd", 10)
            c.drawString(MARGIN + 2, self.y, "\u2022")
            lines = self._wrap(it, "Noto", size, self.max_w - 20)
            c.setFillColor(text_color)
            c.setFont("Noto", size)
            for i, ln in enumerate(lines):
                if i:
                    self._ensure(leading)
                c.drawString(MARGIN + 18, self.y, ln)
                self.y -= leading
            self.y -= gap

    def _support_block(self, support):
        self._section_title(support["title"], keep=200)
        c = self.c
        col_gap = 24
        col_w = (self.max_w - col_gap) / 2
        # measure height needed
        self._ensure(150)
        top = self.y
        # Covered card
        self._two_col_card(MARGIN, top, col_w, "Covered",
                           support["covered"], YELLOW, INK)
        h1 = self._card_height(support["covered"], col_w)
        # Not covered card
        self._two_col_card(MARGIN + col_w + col_gap, top, col_w,
                           "Not covered", support["not_covered"],
                           HexColor("#C9C9C9"), MUTED)
        h2 = self._card_height(support["not_covered"], col_w)
        self.y = top - max(h1, h2) - 14

    def _card_height(self, items, col_w):
        pad, head, size, leading, gap = 14, 22, 9.5, 12.5, 6
        h = pad + head
        for it in items:
            lines = self._wrap(it, "Noto", size, col_w - 2 * pad - 14)
            h += len(lines) * leading + gap
        return h + pad - gap

    def _two_col_card(self, x, top, w, label, items, accent, txt):
        c = self.c
        h = self._card_height(items, w)
        c.setFillColor(CARD)
        c.roundRect(x, top - h, w, h, 8, fill=1, stroke=0)
        c.setFillColor(accent)
        c.roundRect(x, top - h, 4, h, 2, fill=1, stroke=0)
        pad = 14
        yy = top - pad - 10
        c.setFillColor(INK)
        c.setFont("Noto-Xb", 10.5)
        c.drawString(x + pad, yy, label)
        yy -= 20
        size, leading, gap = 9.5, 12.5, 6
        for it in items:
            c.setFillColor(accent)
            c.setFont("Noto-Bd", 9.5)
            c.drawString(x + pad, yy, "\u2013")
            lines = self._wrap(it, "Noto", size, w - 2 * pad - 14)
            c.setFillColor(txt)
            c.setFont("Noto", size)
            for i, ln in enumerate(lines):
                c.drawString(x + pad + 14, yy, ln)
                yy -= leading
            yy -= gap

    def _price_box(self):
        q = self.q
        self._ensure(96)
        self.y -= 6
        c = self.c
        h = 84
        x, top = MARGIN, self.y
        on_yellow = HexColor("#6E6600")   # dark, readable text on yellow
        c.setFillColor(YELLOW)
        c.roundRect(x, top - h, self.max_w, h, 10, fill=1, stroke=0)
        c.setFillColor(INK)
        c.roundRect(x, top - h, 5, h, 2, fill=1, stroke=0)
        c.setFillColor(on_yellow)
        c.setFont("Noto-Sb", 9)
        c.drawString(x + 24, top - 26, "TOTAL  \u00b7  " + q["package"])
        c.setFillColor(INK)
        c.setFont("Noto-Sb", 10.5)
        # keep this line clear of the right-aligned price
        avail = self.max_w - 24 - 180
        full = q["title"] + " - " + q["subtitle"]
        label = full
        if pdfmetrics.stringWidth(label, "Noto-Sb", 10.5) > avail:
            words, label = full.split(), ""
            for w in words:
                trial = w if not label else label + " " + w
                if pdfmetrics.stringWidth(trial + "\u2026", "Noto-Sb",
                                          10.5) > avail:
                    break
                label = trial
            label = label + "\u2026"
        c.drawString(x + 24, top - 44, label)
        c.setFillColor(on_yellow)
        c.setFont("Noto", 8.5)
        c.drawString(x + 24, top - 62, "Delivery: " + q["timeline"])
        # price
        c.setFillColor(INK)
        c.setFont("Noto-Blk", 30)
        c.drawRightString(x + self.max_w - 24, top - 46, rupee(q["price"]))
        c.setFillColor(on_yellow)
        c.setFont("Noto", 8.5)
        c.drawRightString(x + self.max_w - 24, top - 62, q["price_note"])
        self.y = top - h - 16

    # ---- intro block (top of first page) ----
    def _intro(self):
        c = self.c
        q = self.q
        # Small label
        c.setFillColor(MUTED)
        c.setFont("Noto-Xb", 10)
        c.drawString(MARGIN, self.y, "QUOTATION")
        self.y -= 30
        # Title
        c.setFillColor(INK)
        c.setFont("Noto-Blk", 30)
        c.drawString(MARGIN, self.y, q["title"])
        self.y -= 23
        # Package + subtitle
        c.setFillColor(INK)
        c.setFont("Noto-Bd", 14)
        c.drawString(MARGIN, self.y, q["package"])
        self.y -= 17
        c.setFillColor(MUTED)
        c.setFont("Noto", 10.5)
        for ln in self._wrap(q["subtitle"], "Noto", 10.5, self.max_w):
            c.drawString(MARGIN, self.y, ln)
            self.y -= 15
        self.y -= 12

        # Meta strip (between two hairlines)
        today = date.today()
        valid = today + timedelta(days=data.TERMS["validity_days"])
        meta = [
            ("Quotation No.", q["id"]),
            ("Date", today.strftime("%d %b %Y")),
            ("Valid until", valid.strftime("%d %b %Y")),
            ("Prepared for", data.CLIENT["company"]),
        ]
        c.setStrokeColor(LINE)
        c.setLineWidth(0.8)
        c.line(MARGIN, self.y, PAGE_W - MARGIN, self.y)
        self.y -= 16
        colw = self.max_w / 4
        for i, (k, v) in enumerate(meta):
            cx = MARGIN + i * colw
            c.setFillColor(MUTED)
            c.setFont("Noto-Md", 8)
            c.drawString(cx, self.y, k.upper())
            c.setFillColor(INK)
            c.setFont("Noto-Sb", 10.5)
            c.drawString(cx, self.y - 15, v)
        self.y -= 15 + 16
        c.setStrokeColor(LINE)
        c.line(MARGIN, self.y, PAGE_W - MARGIN, self.y)
        self.y -= 4

    # ---- terms ----
    def _terms(self):
        self._section_title("Terms & next steps")
        self._para(
            "Payment: " + data.TERMS["payment"], "Noto", 10, MARGIN,
            self.max_w, 14)
        self.y -= 4
        self._bullets(data.TERMS["notes"])
        self.y -= 6
        # signature row
        self._ensure(80)
        c = self.c
        top = self.y
        colw = (self.max_w - 30) / 2
        for i, label in enumerate(["For Bhama Vision", "Client acceptance"]):
            x = MARGIN + i * (colw + 30)
            c.setStrokeColor(HexColor("#BFBFBF"))
            c.setLineWidth(1)
            c.line(x, top - 34, x + colw, top - 34)
            c.setFillColor(MUTED)
            c.setFont("Noto-Md", 9)
            c.drawString(x, top - 48, label)
        self.y = top - 60

    # ---- orchestration ----
    def render(self):
        self._new_content_page(first=True)
        self._intro()
        # Overview
        self._section_title("Overview")
        self._para(self.q["summary"], "Noto", 10.5, MARGIN, self.max_w, 15.5)
        # Sections
        for sec in self.q["sections"]:
            self._section_title(sec["heading"])
            self._bullets(sec["items"], muted=sec.get("muted", False))
        # Support
        if self.q["support"]:
            self._support_block(self.q["support"])
        # Pricing
        self._section_title("Investment", keep=150)
        self._price_box()
        # Terms
        self._terms()


def build():
    _register_fonts()
    os.makedirs(OUTPUT, exist_ok=True)
    outputs = []
    for q in data.QUOTATIONS:
        fname = "{}_{}.pdf".format(
            q["id"], q["package"].replace(" ", "-").replace("+", "and"))
        path = os.path.join(OUTPUT, fname)
        c = canvas.Canvas(path, pagesize=A4)
        c.setTitle("{} - {} Quotation".format(data.COMPANY["name"], q["title"]))
        c.setAuthor(data.COMPANY["name"])
        Quote(c, q).render()
        c.showPage()
        c.save()
        outputs.append(path)
        print("Wrote", path)
    return outputs


if __name__ == "__main__":
    build()
