#!/usr/bin/env python3
"""Build entry.png for make.fun news-image-20261121 (vocaine).

Magazine-cover design: warm cream background, giant "21" + "NOVEMBER 2026"
masthead, title band, six numbered story blocks in muted colours.
Pure stdlib + PIL, no network, fully deterministic.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

CREAM = (246, 239, 221)
INK = (30, 42, 50)
INK_SOFT = (61, 74, 84)
GOLD = (138, 109, 59)
BAND = (34, 48, 60)
WHITE = (255, 255, 255)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# (number, headline, one-line deck, row tint, number accent)
STORIES = [
    ("01", "TRUMP, XI AND PUTIN SIGN JOINT DECLARATION",
     "Trilateral summit in Shenzhen ends with a signed declaration.",
     (221, 230, 210), (95, 122, 82)),
    ("02", "RUSSIAN MISSILES HIT KYIV, ENTER POLAND",
     "Missiles cross into Polish airspace as NATO jets scramble.",
     (242, 216, 203), (168, 90, 56)),
    ("03", "COURT: MYANMAR COMMITTED ROHINGYA GENOCIDE",
     "The world court finds Myanmar responsible for the Rohingya.",
     (215, 226, 236), (74, 107, 138)),
    ("04", "COP31 STALLS OVER FOSSIL-FUEL PHASE-OUT",
     "Talks miss the deadline with no deal on ending fossil fuels.",
     (243, 227, 184), (154, 123, 30)),
    ("05", "EU–UK SUMMIT SEALS TRADE, CARBON, YOUTH DEAL",
     "London and Brussels agree on trade, carbon and youth travel.",
     (232, 216, 232), (122, 74, 122)),
    ("06", "US CLEARS NEARLY 900,000 AI CHIPS FOR CHINA",
     "House panel approves export of almost 900,000 chips in six months.",
     (216, 222, 227), (78, 93, 107)),
]

TEXT_X = 172          # left edge of headline/deck inside a row
TEXT_RIGHT = 972      # right edge of text inside a row


def font(path, size):
    return ImageFont.truetype(path, size)


def fit(draw, text, path, size, max_size, min_size, max_width):
    """Largest font size in [min_size, max_size] that fits max_width."""
    size = min(size, max_size)
    while size > min_size:
        f = font(path, size)
        if draw.textlength(text, font=f) <= max_width:
            return f
        size -= 1
    return font(path, min_size)


def draw_header(draw):
    # Eyebrow
    draw.text((36, 28), "SATURDAY  \u2022  THE WORLD IN BRIEF",
              font=font(FONT_BOLD, 22), fill=GOLD)
    # Giant day number
    draw.text((28, 46), "21", font=font(FONT_BOLD, 250), fill=INK)
    # Month / year block on the right
    draw.text((560, 88), "NOVEMBER", font=font(FONT_BOLD, 62), fill=INK)
    draw.text((560, 166), "2026", font=font(FONT_BOLD, 62), fill=GOLD)
    draw.line([(560, 246), (988, 246)], fill=GOLD, width=4)
    draw.text((560, 258), "SIX STORIES  \u2022  ONE DAY  \u2022  THE WORLD TODAY",
              font=font(FONT_BOLD, 16), fill=INK_SOFT)
    # Title band
    draw.rectangle([0, 300, W, 358], fill=BAND)
    title = "6 STORIES THAT DEFINED THE DAY"
    tf = font(FONT_BOLD, 32)
    tw = draw.textlength(title, font=tf)
    draw.text(((W - tw) / 2, 312), title, font=tf, fill=WHITE)


def draw_rows(draw):
    y = 372
    row_h, gap = 98, 7
    for num, headline, deck, tint, accent in STORIES:
        draw.rounded_rectangle([28, y, 996, y + row_h], radius=14, fill=tint)
        nf = font(FONT_BOLD, 56)
        draw.text((52, y + 20), num, font=nf, fill=accent)
        draw.line([(150, y + 16), (150, y + row_h - 16)], fill=accent, width=3)
        max_w = TEXT_RIGHT - TEXT_X
        hf = fit(draw, headline, FONT_BOLD, 27, 27, 20, max_w)
        draw.text((TEXT_X, y + 15), headline, font=hf, fill=INK)
        df = fit(draw, deck, FONT_REG, 21, 21, 16, max_w)
        draw.text((TEXT_X, y + 56), deck, font=df, fill=INK_SOFT)
        y += row_h + gap


def build(path):
    img = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(img)
    draw_header(draw)
    draw_rows(draw)
    img.save(path, format="PNG", optimize=True)
    return path


def main():
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    build(out)
    img = Image.open(out)
    assert img.size == (1024, 1024), img.size
    assert img.format == "PNG"
    size = os.path.getsize(out)
    assert size <= 1048576, size
    print(f"entry.png: {img.size[0]}x{img.size[1]} PNG, {size} bytes")


if __name__ == "__main__":
    main()
