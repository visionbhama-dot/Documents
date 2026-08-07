"""
A4 PDF resume builder for Prafull Kumar Sharma.

Premium two-tone layout:
- Full-height dark sidebar (contact, skills, software, education, languages,
  personal) with a yellow monogram and yellow markers.
- White main column (profile, experience, projects, services) with a teal
  accent for a richer, non-monochrome look.

    python3 build_resume.py
"""
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas

from build_quotes import _register_fonts, PAGE_W, PAGE_H, OUTPUT
from resume import RESUME as R

# ---- palette (more than one accent) ----
SLATE = HexColor("#1E2733")        # dark sidebar
SLATE_LINE = HexColor("#39465A")   # sidebar dividers
CLOUD = HexColor("#C4CCD8")        # sidebar body text
CLOUD_DIM = HexColor("#8B94A3")    # sidebar labels
WHITE = HexColor("#FFFFFF")
YELLOW = HexColor("#F0E40A")       # brand accent (sidebar)
TEAL = HexColor("#14B5A5")         # secondary accent (main column)
INK = HexColor("#1F2733")          # main headings / text
MUTED = HexColor("#6B7280")        # main secondary text
HAIR = HexColor("#E5E8EC")         # light hairline

# ---- geometry ----
M = 40
PANEL_W = 196
SIDE_X = 22
SIDE_W = PANEL_W - SIDE_X - 20
MAIN_X = PANEL_W + 28
MAIN_W = (PAGE_W - M) - MAIN_X


def wrap(text, font, size, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = w if not cur else cur + " " + w
        if pdfmetrics.stringWidth(t, font, size) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def draw_icon(c, kind, x, y, s, col):
    c.saveState()
    c.setStrokeColor(col)
    c.setFillColor(col)
    c.setLineWidth(1)
    if kind == "phone":
        c.roundRect(x + s * 0.22, y, s * 0.56, s, s * 0.14, stroke=1, fill=0)
        c.circle(x + s * 0.5, y + s * 0.13, s * 0.05, stroke=0, fill=1)
    elif kind == "pin":
        r = s * 0.32
        cx = x + s * 0.5
        cy = y + s - r
        c.circle(cx, cy, r, stroke=1, fill=0)
        p = c.beginPath()
        p.moveTo(cx - r * 0.72, cy - r * 0.45)
        p.lineTo(cx, y)
        p.lineTo(cx + r * 0.72, cy - r * 0.45)
        c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


class ResumeDoc:
    def __init__(self, c):
        self.c = c

    def _initials(self):
        parts = [p for p in R["name"].split() if p]
        if len(parts) >= 2:
            return (parts[0][0] + parts[-1][0]).upper()
        return parts[0][:2].upper()

    # ---- section headings ----
    def h_main(self, text, y):
        c = self.c
        c.setFillColor(TEAL)
        c.rect(MAIN_X, y - 0.5, 7, 7, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont("Noto-Xb", 11)
        c.drawString(MAIN_X + 13, y, text.upper())
        yl = y - 8
        c.setStrokeColor(HAIR)
        c.setLineWidth(1)
        c.line(MAIN_X, yl, MAIN_X + MAIN_W, yl)
        c.setStrokeColor(TEAL)
        c.setLineWidth(2)
        c.line(MAIN_X, yl, MAIN_X + 34, yl)
        return y - 22

    def h_side(self, text, y):
        c = self.c
        c.setFillColor(YELLOW)
        c.rect(SIDE_X, y - 0.5, 7, 7, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Noto-Xb", 10.5)
        c.drawString(SIDE_X + 13, y, text.upper())
        yl = y - 8
        c.setStrokeColor(SLATE_LINE)
        c.setLineWidth(1)
        c.line(SIDE_X, yl, SIDE_X + SIDE_W, yl)
        return y - 20

    # ---- main column ----
    def main_header(self):
        c = self.c
        c.setFillColor(INK)
        c.setFont("Noto-Blk", 23)
        c.drawString(MAIN_X, PAGE_H - 56, R["name"])
        c.setFillColor(TEAL)
        c.setFont("Noto-Sb", 11.5)
        c.drawString(MAIN_X, PAGE_H - 75, R["title"])
        y = PAGE_H - 90
        c.setStrokeColor(HAIR)
        c.setLineWidth(1)
        c.line(MAIN_X, y, MAIN_X + MAIN_W, y)
        c.setStrokeColor(TEAL)
        c.setLineWidth(2)
        c.line(MAIN_X, y, MAIN_X + 48, y)
        return y - 24

    def bullet_main(self, text, y, size=10):
        c = self.c
        c.setFillColor(TEAL)
        c.setFont("Noto-Bd", size)
        c.drawString(MAIN_X + 2, y, "\u2022")
        c.setFillColor(INK)
        c.setFont("Noto", size)
        for ln in wrap(text, "Noto", size, MAIN_W - 16):
            c.drawString(MAIN_X + 15, y, ln)
            y -= 14
        return y

    def main_column(self, y):
        c = self.c
        # Profile
        y = self.h_main("Profile", y)
        c.setFillColor(INK)
        c.setFont("Noto", 10)
        for ln in wrap(R["summary"], "Noto", 10, MAIN_W):
            c.drawString(MAIN_X, y, ln)
            y -= 14.5
        y -= 14

        # Experience
        y = self.h_main("Experience", y)
        for job in R["experience"]:
            c.setFillColor(INK)
            c.setFont("Noto-Sb", 11)
            c.drawString(MAIN_X, y, job["role"])
            if job["period"]:
                c.setFillColor(MUTED)
                c.setFont("Noto-Md", 8.5)
                c.drawRightString(MAIN_X + MAIN_W, y, job["period"])
            y -= 13
            c.setFillColor(TEAL)
            c.setFont("Noto-Md", 9.5)
            c.drawString(MAIN_X, y, job["org"])
            y -= 15
            for p in job["points"]:
                y = self.bullet_main(p, y)
                y -= 3
            y -= 9

        # Key Projects
        y = self.h_main("Key Projects", y)
        for name, note in R["projects"]:
            c.setFillColor(TEAL)
            c.setFont("Noto-Bd", 10)
            c.drawString(MAIN_X + 2, y, "\u2022")
            c.setFillColor(INK)
            c.setFont("Noto-Sb", 10)
            c.drawString(MAIN_X + 15, y, name)
            nx = MAIN_X + 15 + pdfmetrics.stringWidth(name, "Noto-Sb", 10)
            note_txt = " - " + note
            if pdfmetrics.stringWidth(name + note_txt, "Noto-Sb", 10) \
                    < MAIN_W - 15:
                c.setFillColor(MUTED)
                c.setFont("Noto", 10)
                c.drawString(nx, y, note_txt)
                y -= 15
            else:
                y -= 14
                c.setFillColor(MUTED)
                c.setFont("Noto", 10)
                for ln in wrap(note, "Noto", 10, MAIN_W - 16):
                    c.drawString(MAIN_X + 15, y, ln)
                    y -= 14
                y -= 1
        y -= 12

        # Core Services
        y = self.h_main("Core Services", y)
        for s in R["services"]:
            y = self.bullet_main(s, y)
            y -= 1
        return y

    # ---- sidebar ----
    def sidebar(self):
        c = self.c
        c.setFillColor(SLATE)
        c.rect(0, 0, PANEL_W, PAGE_H, fill=1, stroke=0)
        # monogram
        cx, cy, r = PANEL_W / 2, PAGE_H - 60, 30
        c.setFillColor(YELLOW)
        c.circle(cx, cy, r, stroke=0, fill=1)
        c.setFillColor(SLATE)
        c.setFont("Noto-Blk", 22)
        c.drawCentredString(cx, cy - 8, self._initials())
        y = PAGE_H - 118

        # Contact
        y = self.h_side("Contact", y)
        for kind, text in [("phone", R["contact"]["phone"]),
                           ("pin", R["contact"]["location"])]:
            draw_icon(c, kind, SIDE_X, y - 1, 10, YELLOW)
            c.setFillColor(CLOUD)
            c.setFont("Noto", 9)
            c.drawString(SIDE_X + 16, y, text)
            y -= 16
        y -= 12

        # Skills
        y = self.h_side("Skills", y)
        for group, detail in R["skills"]:
            c.setFillColor(WHITE)
            c.setFont("Noto-Sb", 9.5)
            c.drawString(SIDE_X, y, group)
            y -= 12
            c.setFillColor(CLOUD)
            c.setFont("Noto", 8.5)
            for ln in wrap(detail, "Noto", 8.5, SIDE_W):
                c.drawString(SIDE_X, y, ln)
                y -= 11
            y -= 7
        y -= 5

        # Software
        y = self.h_side("Software", y)
        for s in R["software"]:
            c.setFillColor(YELLOW)
            c.setFont("Noto-Bd", 9)
            c.drawString(SIDE_X, y, "\u2022")
            c.setFillColor(CLOUD)
            c.setFont("Noto", 9)
            c.drawString(SIDE_X + 13, y, s)
            y -= 14
        y -= 11

        # Education
        y = self.h_side("Education", y)
        for title, place in R["education"]:
            c.setFillColor(WHITE)
            c.setFont("Noto-Sb", 9.5)
            for ln in wrap(title, "Noto-Sb", 9.5, SIDE_W):
                c.drawString(SIDE_X, y, ln)
                y -= 12
            c.setFillColor(CLOUD)
            c.setFont("Noto", 8.5)
            for ln in wrap(place, "Noto", 8.5, SIDE_W):
                c.drawString(SIDE_X, y, ln)
                y -= 11
            y -= 7
        y -= 5

        # Languages
        y = self.h_side("Languages", y)
        c.setFillColor(CLOUD)
        c.setFont("Noto", 9.5)
        c.drawString(SIDE_X, y, ", ".join(R["languages"]))
        y -= 18
        y -= 5

        # Personal
        y = self.h_side("Personal", y)
        for k, v in R["personal"]:
            c.setFillColor(CLOUD_DIM)
            c.setFont("Noto-Md", 8)
            c.drawString(SIDE_X, y, k.upper())
            c.setFillColor(WHITE)
            c.setFont("Noto-Sb", 9.5)
            c.drawString(SIDE_X, y - 12, v)
            y -= 26

    def render(self):
        self.sidebar()
        y = self.main_header()
        self.main_column(y)


def build():
    _register_fonts()
    os.makedirs(OUTPUT, exist_ok=True)
    path = os.path.join(OUTPUT, "Prafull-Kumar-Sharma-Resume.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("Prafull Kumar Sharma - Resume")
    c.setAuthor(R["name"])
    ResumeDoc(c).render()
    c.showPage()
    c.save()
    print("Wrote", path)
    return path


if __name__ == "__main__":
    build()
