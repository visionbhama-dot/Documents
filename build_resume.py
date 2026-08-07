"""
A4 PDF resume builder for Prafull Kumar Sharma.

Clean two-column layout: main column (profile, experience, projects) and a
light sidebar (skills, tools, education, personal). Yellow brand accent.

    python3 build_resume.py
"""
import os

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas

from build_quotes import (_register_fonts, PAGE_W, PAGE_H, INK, MUTED,
                          YELLOW, LINE, CARD, OUTPUT)
from resume import RESUME as R

M = 44                                   # page margin
PANEL_L = 366                            # sidebar panel left edge
PANEL_R = PAGE_W - M                     # sidebar panel right edge
SIDE_PAD = 16
SIDE_X = PANEL_L + SIDE_PAD
SIDE_W = PANEL_R - SIDE_PAD - SIDE_X
MAIN_X = M
MAIN_W = PANEL_L - 22 - MAIN_X


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


class ResumeDoc:
    def __init__(self, c):
        self.c = c

    def para(self, text, font, size, x, y, w, leading, color=INK):
        c = self.c
        c.setFillColor(color)
        c.setFont(font, size)
        for ln in wrap(text, font, size, w):
            c.drawString(x, y, ln)
            y -= leading
        return y

    def heading(self, text, x, y, w):
        c = self.c
        c.setFillColor(INK)
        c.setFont("Noto-Xb", 10.5)
        c.drawString(x, y, text.upper())
        yl = y - 7
        c.setStrokeColor(LINE)
        c.setLineWidth(1)
        c.line(x, yl, x + w, yl)
        c.setFillColor(YELLOW)
        c.rect(x, yl - 1.5, 30, 3, fill=1, stroke=0)
        return y - 22

    # ---- header ----
    def header(self):
        c = self.c
        c.setFillColor(INK)
        c.setFont("Noto-Blk", 27)
        c.drawString(M, PAGE_H - 62, R["name"])
        c.setFillColor(MUTED)
        c.setFont("Noto-Md", 12)
        c.drawString(M, PAGE_H - 82, R["title"])
        # contact line
        ct = R["contact"]
        contact = "   \u00b7   ".join(
            [ct["phone"], ct["email"], ct["website"], ct["location"]])
        c.setFillColor(INK)
        c.setFont("Noto", 9)
        c.drawString(M, PAGE_H - 100, contact)
        # accent rule
        y = PAGE_H - 114
        c.setStrokeColor(LINE)
        c.setLineWidth(1)
        c.line(M, y, PAGE_W - M, y)
        c.setFillColor(YELLOW)
        c.rect(M, y - 2, 64, 4, fill=1, stroke=0)
        return y - 26

    # ---- main column ----
    def main_column(self, y):
        c = self.c
        # Profile
        y = self.heading("Profile", MAIN_X, y, MAIN_W)
        y = self.para(R["summary"], "Noto", 10, MAIN_X, y, MAIN_W, 14.5,
                      color=INK)
        y -= 14

        # Experience
        y = self.heading("Experience", MAIN_X, y, MAIN_W)
        for job in R["experience"]:
            c.setFillColor(INK)
            c.setFont("Noto-Sb", 11)
            c.drawString(MAIN_X, y, job["role"])
            if job["period"]:
                c.setFillColor(MUTED)
                c.setFont("Noto-Md", 8.5)
                c.drawRightString(MAIN_X + MAIN_W, y, job["period"])
            y -= 13
            c.setFillColor(MUTED)
            c.setFont("Noto-Md", 9.5)
            c.drawString(MAIN_X, y, job["org"])
            y -= 14
            for p in job["points"]:
                c.setFillColor(YELLOW)
                c.setFont("Noto-Bd", 10)
                c.drawString(MAIN_X + 2, y, "\u2022")
                lines = wrap(p, "Noto", 10, MAIN_W - 16)
                c.setFillColor(INK)
                c.setFont("Noto", 10)
                for ln in lines:
                    c.drawString(MAIN_X + 15, y, ln)
                    y -= 14
                y -= 3
            y -= 10

        # Key Projects
        y = self.heading("Key Projects", MAIN_X, y, MAIN_W)
        for name, note in R["projects"]:
            c.setFillColor(YELLOW)
            c.setFont("Noto-Bd", 10)
            c.drawString(MAIN_X + 2, y, "\u2022")
            c.setFillColor(INK)
            c.setFont("Noto-Sb", 10)
            c.drawString(MAIN_X + 15, y, name)
            nx = MAIN_X + 15 + pdfmetrics.stringWidth(name, "Noto-Sb", 10)
            c.setFillColor(MUTED)
            c.setFont("Noto", 10)
            note_txt = " - " + note
            if pdfmetrics.stringWidth(name + note_txt, "Noto-Sb", 10) \
                    < MAIN_W - 15:
                c.drawString(nx, y, note_txt)
                y -= 15
            else:
                y -= 14
                for ln in wrap(note, "Noto", 10, MAIN_W - 16):
                    c.drawString(MAIN_X + 15, y, ln)
                    y -= 14
                y -= 1
        y -= 12

        # Core Services
        y = self.heading("Core Services", MAIN_X, y, MAIN_W)
        for s in R["services"]:
            c.setFillColor(YELLOW)
            c.setFont("Noto-Bd", 10)
            c.drawString(MAIN_X + 2, y, "\u2022")
            c.setFillColor(INK)
            c.setFont("Noto", 10)
            for ln in wrap(s, "Noto", 10, MAIN_W - 16):
                c.drawString(MAIN_X + 15, y, ln)
                y -= 15
        return y

    # ---- sidebar ----
    def sidebar(self, top):
        c = self.c
        # panel background
        c.setFillColor(CARD)
        c.rect(PANEL_L, M, PANEL_R - PANEL_L, top - M, fill=1, stroke=0)
        y = top - SIDE_PAD - 4

        # Skills
        y = self.heading("Skills", SIDE_X, y, SIDE_W)
        for group, detail in R["skills"]:
            c.setFillColor(INK)
            c.setFont("Noto-Sb", 9.5)
            c.drawString(SIDE_X, y, group)
            y -= 12
            c.setFillColor(MUTED)
            c.setFont("Noto", 8.5)
            for ln in wrap(detail, "Noto", 8.5, SIDE_W):
                c.drawString(SIDE_X, y, ln)
                y -= 11
            y -= 6

        y -= 4
        # Strengths
        y = self.heading("Strengths", SIDE_X, y, SIDE_W)
        for s in R["strengths"]:
            c.setFillColor(YELLOW)
            c.setFont("Noto-Bd", 9)
            c.drawString(SIDE_X, y, "\u2022")
            c.setFillColor(INK)
            c.setFont("Noto", 9)
            for ln in wrap(s, "Noto", 9, SIDE_W - 13):
                c.drawString(SIDE_X + 12, y, ln)
                y -= 11.5
            y -= 4
        y -= 4

        # Software
        y = self.heading("Software", SIDE_X, y, SIDE_W)
        c.setFont("Noto", 9.5)
        for s in R["software"]:
            c.setFillColor(YELLOW)
            c.setFont("Noto-Bd", 9.5)
            c.drawString(SIDE_X, y, "\u2022")
            c.setFillColor(INK)
            c.setFont("Noto", 9.5)
            c.drawString(SIDE_X + 13, y, s)
            y -= 14
        y -= 6

        # Education
        y = self.heading("Education", SIDE_X, y, SIDE_W)
        for title, place in R["education"]:
            c.setFillColor(INK)
            c.setFont("Noto-Sb", 9.5)
            for ln in wrap(title, "Noto-Sb", 9.5, SIDE_W):
                c.drawString(SIDE_X, y, ln)
                y -= 12
            c.setFillColor(MUTED)
            c.setFont("Noto", 8.5)
            for ln in wrap(place, "Noto", 8.5, SIDE_W):
                c.drawString(SIDE_X, y, ln)
                y -= 11
            y -= 6
        y -= 4

        # Languages
        y = self.heading("Languages", SIDE_X, y, SIDE_W)
        c.setFillColor(INK)
        c.setFont("Noto", 9.5)
        c.drawString(SIDE_X, y, ", ".join(R["languages"]))
        y -= 18
        y -= 4

        # Personal
        y = self.heading("Personal", SIDE_X, y, SIDE_W)
        for k, v in R["personal"]:
            c.setFillColor(MUTED)
            c.setFont("Noto-Md", 8.5)
            c.drawString(SIDE_X, y, k.upper())
            c.setFillColor(INK)
            c.setFont("Noto-Sb", 9.5)
            c.drawString(SIDE_X, y - 12, v)
            y -= 26
        return y

    def render(self):
        y_cols = self.header()
        self.sidebar(y_cols + 12)
        self.main_column(y_cols)


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
