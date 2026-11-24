#!/usr/bin/env python3
"""Build the news poster for make.fun news-image-20261123.

Draws a 1024x1024 newspaper-style poster in PIL:
  masthead with the date -> AI-illustrated hero band -> 6-story grid -> footer.
Text is rendered with PIL (crisp, no AI-garbled text); the hero illustration
(assets/media-generation-hero-20261123-*.webp) was generated with an image
model from a no-text prompt, fresh for this entry.
Output: ../entry.png (PNG, <= 1 MiB, <= 1024x1024).
"""
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
HERO = ROOT / "assets" / "media-generation-hero-20261123-0-f16beeda-af2f-431e-ab05-b0c7a245c0eb.webp"
OUT = ROOT / "entry.png"

W, H = 1024, 1024
NAVY = (16, 28, 78)
AMBER = (232, 160, 32)
PAPER = (247, 243, 232)
INK = (20, 20, 20)
GREY = (90, 90, 90)
DIVIDER = (216, 210, 192)


def font(bold: bool, size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont,
         max_w: int) -> list[str]:
    """Greedy word wrap to max_w pixels."""
    lines: list[str] = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for word in words:
            trial = f"{cur} {word}".strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
    return lines


# Built 2026-11-24 ~19:30 CST with stories that genuinely happened or were
# first reported on Monday 23 Nov 2026 (each corroborated by >=2 sources;
# see NOTES.md). Date traps avoided: the COP31 collapse, the S. Korea
# education minister's resignation, the Democrats' 258th House seat and the
# Dymer/Kyiv strikes all happened on Sunday 22 Nov (reported Monday) and
# were dropped; the Merkury sinking was a Sunday attack, so only its Monday
# confirmation was considered and then dropped in favour of the NATO meeting,
# which is itself a Monday event. Weekday verified: 2026-11-23 is a Monday.
STORIES = [
    ("EUROPE", (140, 32, 32),
     "NATO MEETS AFTER MISSILES HIT POLAND",
     "NATO council meets in Brussels after Russian missiles fell in Poland; AWACS planes to be sent."),
    ("TECH", (176, 92, 8),
     "HUANG BACK AS NVIDIA CEO",
     "Nvidia reinstates Jensen Huang as chief executive, effective immediately; shares soar 31%."),
    ("BUSINESS", (31, 120, 76),
     "CROWDSTRIKE BUYS ZSCALER",
     "$43.9bn all-stock deal, the largest in cybersecurity history; 1.135 shares per Zscaler share."),
    ("IRAN", (110, 52, 130),
     "IRAN FLOGS SINGER AHMADI",
     "Ahmadi lashed 74 times in Qom for a 2024 concert without a hijab; two-year bans on work and travel."),
    ("US", (16, 70, 130),
     "US HITS IRAN'S SHADOW BANKING",
     "Treasury sanctions two dozen exchange houses and front companies; $14.7bn in linked activity found."),
    ("ASIA", (120, 74, 10),
     "INDONESIA FIRE TOLL AT 24",
     "Deaths confirmed on Monday after a factory blaze in Cikande, Banten; about 30 people still missing."),
]


def main() -> None:
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 132], fill=NAVY)
    title_f = font(True, 56)
    d.text((W // 2, 16), "THE WORLD IN ONE DAY", font=title_f, fill="white",
           anchor="ma")
    date_f = font(True, 30)
    d.text((W // 2, 82), "MONDAY, 23 NOVEMBER 2026", font=date_f, fill=AMBER,
           anchor="ma")
    d.rectangle([0, 130, W, 134], fill=AMBER)

    # --- hero band (132..500) ---
    hero = Image.open(HERO).convert("RGB")
    hw, hh = hero.size
    target_w, target_h = W, 368
    scale = max(target_w / hw, target_h / hh)
    hero = hero.resize((round(hw * scale), round(hh * scale)), Image.LANCZOS)
    x0 = (hero.width - target_w) // 2
    y0 = (hero.height - target_h) // 2
    img.paste(hero.crop((x0, y0, x0 + target_w, y0 + target_h)), (0, 134))

    # --- story grid (502..972): 2 cols x 3 rows ---
    grid_top, grid_bottom = 502, 972
    col_w, row_h = W // 2, (grid_bottom - grid_top) // 3
    for i, (tag, colour, headline, summary) in enumerate(STORIES):
        col, row = i % 2, i // 2
        cx, cy = col * col_w, grid_top + row * row_h
        # dividers
        if col == 1:
            d.line([col_w, cy, col_w, cy + row_h], fill=DIVIDER, width=2)
        if row > 0:
            d.line([0, cy, W, cy], fill=DIVIDER, width=2)
        px, py = cx + 18, cy + 14
        # tag chip
        tag_f = font(True, 16)
        tw = d.textlength(tag, font=tag_f)
        d.rounded_rectangle([px, py, px + tw + 18, py + 26], radius=4, fill=colour)
        d.text((px + 9, py + 4), tag, font=tag_f, fill="white")
        # headline (up to 2 lines)
        hl_f = font(True, 23)
        hl_lines = wrap(d, headline, hl_f, col_w - 36)[:2]
        hy = py + 36
        for line in hl_lines:
            d.text((px, hy), line, font=hl_f, fill=INK)
            hy += 28
        # summary (up to 2 lines)
        sm_f = font(False, 18)
        sm_lines = wrap(d, summary, sm_f, col_w - 36)[:2]
        sy = hy + 4
        for line in sm_lines:
            d.text((px, sy), line, font=sm_f, fill=(60, 60, 60))
            sy += 23

    # --- footer ---
    d.rectangle([0, 972, W, H], fill=NAVY)
    ft_f = font(False, 16)
    d.text((W // 2, 990),
           "23 NOVEMBER 2026  \u2022  As reported by Reuters, BBC, CNN, WSJ and others  "
           "\u2022  make.fun news-image-20261123",
           font=ft_f, fill="white", anchor="ma")

    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} {img.size} {OUT.stat().st_size} bytes")


if __name__ == "__main__":
    main()
