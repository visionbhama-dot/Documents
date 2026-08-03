"""
Generate a placeholder BhamaVision logo (transparent PNG).

This is only a stand-in so the quotations look branded out of the box.
Replace `assets/logo.png` with your real logo (transparent PNG recommended,
roughly a 4:1 width:height ratio) and re-run `build_quotes.py`.

Usage:
    python3 assets/make_logo.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/google-noto"

# Brand palette
WHITE = (255, 255, 255, 255)
YELLOW = (240, 228, 10, 255)          # BhamaVision accent
TRANSPARENT = (0, 0, 0, 0)

SCALE = 4                              # supersample for smooth edges
H = 380 * SCALE


def load_font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def build():
    # Measure the wordmark first so the canvas is wide enough.
    font = load_font("NotoSans-ExtraBold.ttf", int(H * 0.5))
    measure = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    pad = 30 * SCALE
    eye_h = int(H * 0.42)
    eye_w = int(eye_h * 1.9)
    gap = int(35 * SCALE)
    text_x = pad + eye_w + gap
    word_w = measure.textlength("BhamaVision", font=font)
    W = int(text_x + word_w + pad)

    img = Image.new("RGBA", (W, H), TRANSPARENT)
    d = ImageDraw.Draw(img)

    # ---- Eye icon (lens outline + pupil) ----
    cx = pad + eye_w // 2
    cy = H // 2
    stroke = int(14 * SCALE)

    # Outer lens shape drawn as an ellipse outline
    d.ellipse(
        [cx - eye_w // 2, cy - eye_h // 2, cx + eye_w // 2, cy + eye_h // 2],
        outline=WHITE, width=stroke,
    )
    # Pupil (brand yellow)
    pr = int(eye_h * 0.32)
    d.ellipse([cx - pr, cy - pr, cx + pr, cy + pr], fill=YELLOW)

    # ---- Wordmark: "Bhama" (white) + "Vision" (yellow) ----
    # vertical centering using text bbox
    bbox = d.textbbox((0, 0), "BhamaVision", font=font)
    text_h = bbox[3] - bbox[1]
    text_y = (H - text_h) // 2 - bbox[1]

    d.text((text_x, text_y), "Bhama", font=font, fill=WHITE)
    w_bhama = d.textlength("Bhama", font=font)
    d.text((text_x + w_bhama, text_y), "Vision", font=font, fill=YELLOW)

    # Downscale for anti-aliasing, then crop to content
    out = img.resize((W // SCALE, H // SCALE), Image.LANCZOS)
    bbox = out.getbbox()
    if bbox:
        margin = 12
        bbox = (max(0, bbox[0] - margin), max(0, bbox[1] - margin),
                min(out.width, bbox[2] + margin), min(out.height, bbox[3] + margin))
        out = out.crop(bbox)

    dest = os.path.join(HERE, "logo.png")
    out.save(dest)
    print(f"Wrote {dest}  ({out.width}x{out.height})")


if __name__ == "__main__":
    build()
