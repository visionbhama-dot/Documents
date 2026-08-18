"""
Bhama Vision - A4 PDF feature-document builder.

Renders the multi-vendor e-commerce feature list defined in `features.py`
to a branded, print-ready A4 PDF in the `output/` folder. No pricing is
shown - this is a capabilities / features document only.

    python3 build_features.py

Replace `assets/logo.png` with your real logo (transparent PNG) to rebrand.
"""
import os
from datetime import date

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

import features as data

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
FAINT = HexColor("#9AA0A6")      # tertiary text
LINE = HexColor("#E6E6E6")       # hairlines
CARD = HexColor("#F6F6F4")       # light card fill

PAGE_W, PAGE_H = A4              # 595.27 x 841.89 pt
MARGIN = 50


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


# ---------------------------------------------------------------------------
class FeatureDoc:
    """Draws the feature document across as many A4 pages as needed."""

    def __init__(self, c):
        self.c = c
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
        self._logo(MARGIN, PAGE_H - 12, 54, 54)
        c.setFillColor(MUTED)
        c.setFont("Noto-Md", 8.5)
        c.drawRightString(PAGE_W - MARGIN, PAGE_H - 34,
                          data.DOCUMENT["label"] + "  \u00b7  "
                          + data.DOCUMENT["id"])
        c.setFillColor(INK)
        c.setFont("Noto-Sb", 9.5)
        c.drawRightString(PAGE_W - MARGIN, PAGE_H - 48,
                          "Multi-Vendor E-Commerce")
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

    # ---- two-column feature grid (compact) ----
    def _feature_grid(self, sections):
        """Render feature sections as cards flowing in two columns."""
        col_gap = 20
        col_w = (self.max_w - col_gap) / 2
        col_x = [MARGIN, MARGIN + col_w + col_gap]
        # column baseline y-cursors
        col_y = [self.y, self.y]

        for sec in sections:
            h = self._card_height(sec, col_w)
            # choose the column whose cursor is currently higher (more room)
            idx = 0 if col_y[0] >= col_y[1] else 1
            # page break if this card won't fit in the chosen column
            if col_y[idx] - h < 66:
                # if neither column fits, start a new page
                if col_y[1 - idx] - h < 66:
                    self._new_content_page()
                    col_y = [self.y, self.y]
                    idx = 0
                else:
                    idx = 1 - idx
            self._feature_card(col_x[idx], col_y[idx], col_w, sec)
            col_y[idx] -= h + 14
        self.y = min(col_y) - 2

    def _card_height(self, sec, col_w):
        pad, size, leading, gap = 12, 9.3, 12, 5
        head_h = 26
        h = pad + head_h
        for it in sec["items"]:
            lines = self._wrap(it, "Noto", size, col_w - 2 * pad - 12)
            h += len(lines) * leading + gap
        return h + pad - gap

    def _feature_card(self, x, top, w, sec):
        c = self.c
        h = self._card_height(sec, w)
        c.setFillColor(CARD)
        c.roundRect(x, top - h, w, h, 8, fill=1, stroke=0)
        c.setFillColor(YELLOW)
        c.roundRect(x, top - h, 4, h, 2, fill=1, stroke=0)
        pad = 12
        yy = top - pad - 10
        c.setFillColor(INK)
        c.setFont("Noto-Xb", 11)
        c.drawString(x + pad, yy, sec["heading"])
        yy -= 22
        size, leading, gap = 9.3, 12, 5
        for it in sec["items"]:
            c.setFillColor(YELLOW)
            c.setFont("Noto-Bd", 9)
            c.drawString(x + pad, yy, "\u2022")
            lines = self._wrap(it, "Noto", size, w - 2 * pad - 12)
            c.setFillColor(INK)
            c.setFont("Noto", size)
            for ln in lines:
                c.drawString(x + pad + 12, yy, ln)
                yy -= leading
            yy -= gap

    # ---- highlight strip (platform includes) ----
    def _platform_block(self, platform):
        self._section_title(platform["title"], keep=120)
        self._bullets(platform["items"])

    # ---- delivery / requirements two-col cards ----
    def _support_block(self, support):
        self._section_title(support["title"], keep=200)
        col_gap = 24
        col_w = (self.max_w - col_gap) / 2
        self._ensure(160)
        top = self.y
        self._two_col_card(MARGIN, top, col_w, support["left_label"],
                           support["covered"], YELLOW, INK)
        h1 = self._twocol_height(support["covered"], col_w)
        self._two_col_card(MARGIN + col_w + col_gap, top, col_w,
                           support["right_label"], support["not_covered"],
                           HexColor("#C9C9C9"), MUTED)
        h2 = self._twocol_height(support["not_covered"], col_w)
        self.y = top - max(h1, h2) - 14

    def _twocol_height(self, items, col_w):
        pad, head, size, leading, gap = 14, 22, 9.5, 12.5, 6
        h = pad + head
        for it in items:
            lines = self._wrap(it, "Noto", size, col_w - 2 * pad - 14)
            h += len(lines) * leading + gap
        return h + pad - gap

    def _two_col_card(self, x, top, w, label, items, accent, txt):
        c = self.c
        h = self._twocol_height(items, w)
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
            for ln in lines:
                c.drawString(x + pad + 14, yy, ln)
                yy -= leading
            yy -= gap

    # ---- intro block (top of first page) ----
    def _intro(self):
        c = self.c
        d = data.DOCUMENT
        c.setFillColor(MUTED)
        c.setFont("Noto-Xb", 10)
        c.drawString(MARGIN, self.y, d["label"])
        self.y -= 30
        c.setFillColor(INK)
        c.setFont("Noto-Blk", 27)
        for ln in self._wrap(d["title"], "Noto-Blk", 27, self.max_w):
            c.drawString(MARGIN, self.y, ln)
            self.y -= 30
        self.y -= 2
        c.setFillColor(MUTED)
        c.setFont("Noto", 10.5)
        for ln in self._wrap(d["subtitle"], "Noto", 10.5, self.max_w):
            c.drawString(MARGIN, self.y, ln)
            self.y -= 15
        self.y -= 12

        today = date.today()
        meta = [
            ("Document No.", d["id"]),
            ("Date", today.strftime("%d %b %Y")),
            ("Prepared for", data.CLIENT["company"]),
            ("Prepared by", data.COMPANY["name"]),
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

    # ---- closing / next steps (no pricing) ----
    def _closing(self):
        cl = data.CLOSING
        self._section_title(cl["title"], keep=120)
        self._para(cl["note"], "Noto", 10.5, MARGIN, self.max_w, 15.5)
        self.y -= 6
        self._bullets(cl["steps"])
        self.y -= 6
        self._ensure(80)
        c = self.c
        top = self.y
        colw = (self.max_w - 30) / 2
        for i, label in enumerate(["For Bhama Vision", "Client"]):
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
        self._section_title("Overview")
        self._para(data.DOCUMENT["summary"], "Noto", 10.5, MARGIN,
                   self.max_w, 15.5)
        self._platform_block(data.PLATFORM)
        self._section_title("Full feature list", keep=320)
        self._feature_grid(data.FEATURE_SECTIONS)
        if data.REQUIREMENTS:
            self._support_block(data.REQUIREMENTS)
        self._closing()


def build():
    _register_fonts()
    os.makedirs(OUTPUT, exist_ok=True)
    fname = "{}_Multi-Vendor-Ecommerce-Features.pdf".format(
        data.DOCUMENT["id"])
    path = os.path.join(OUTPUT, fname)
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("{} - {}".format(data.COMPANY["name"], data.DOCUMENT["title"]))
    c.setAuthor(data.COMPANY["name"])
    FeatureDoc(c).render()
    c.showPage()
    c.save()
    print("Wrote", path)
    return path


if __name__ == "__main__":
    build()
