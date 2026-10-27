#!/usr/bin/env python3
"""Generate the Ontario Cryptography Day social media card (1200x630).

Reproduces the layout of the hand-made Photoshop images: the event title in
Helvetica Neue Condensed Bold, the date in Helvetica Neue, and the host
university's logo to the right of the date.

    python3 tools/make-social-image.py --date "December 8, 2026" --logo waterloo \
        --out images/socialmedia-20261208.png

The fonts, sizes and baselines below were measured from the June 2025 card
(images/socialmedia-20250606.png), so the type matches the earlier images to
within a pixel. The date and logo are positioned by rule rather than by hand,
which moves them a few pixels from where Photoshop had them.
"""

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parent.parent
LOGO_DIR = REPO / "images" / "logos"

# Helvetica Neue ships with macOS as a font collection; these are the face
# indices for the two styles the original Photoshop file used.
FONT_PATH = Path("/System/Library/Fonts/HelveticaNeue.ttc")
FACE_CONDENSED_BOLD = 4
FACE_REGULAR = 0

WIDTH, HEIGHT = 1200, 630
BACKGROUND = (255, 255, 255)
INK = (0, 0, 0)

TITLE = "Ontario Cryptography Day"
TITLE_SIZE = 100
TITLE_BASELINE = 262  # puts the cap height at y=189
TITLE_CENTER_X = WIDTH // 2

DATE_SIZE = 67
DATE_BASELINE = 457  # puts the cap height at y=409

# The logo is scaled down to fit this box (never scaled up).
LOGO_MAX_SIZE = (420, 200)
LOGO_CENTER_Y = 438

# The date and the logo are laid out as one row centred on the canvas. A long
# date ("December 9, 2026" is 40% wider than "June 6, 2025") first eats into the
# gap, and only then shrinks the type, so short dates keep the original spacing.
SIDE_MARGIN = 90  # matches the title's margin, so the two blocks line up
PREFERRED_GAP = 126
MIN_GAP = 60
MIN_DATE_SIZE = 40


def load_font(face_index: int, size: int) -> ImageFont.FreeTypeFont:
    if not FONT_PATH.exists():
        sys.exit(
            f"error: {FONT_PATH} not found.\n"
            "This script needs the macOS Helvetica Neue collection to match the\n"
            "typography of the previously published images. Substituting another\n"
            "font would silently change the design, so no image was written."
        )
    return ImageFont.truetype(str(FONT_PATH), size, index=face_index)


def resolve_logo(name: str) -> Path:
    """A bare name means images/logos/<name>.png; anything path-like is used as given."""
    path = Path(name) if ("/" in name or name.endswith(".png")) else LOGO_DIR / f"{name}.png"
    if not path.exists():
        available = sorted(p.stem for p in LOGO_DIR.glob("*.png"))
        sys.exit(
            f"error: logo {path} not found.\n"
            f"Available logos: {', '.join(available) or '(none)'}\n"
            "Add a new one by dropping a PNG into images/logos/ (transparent or "
            "white background, at least 420px wide)."
        )
    return path


def ink_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> int:
    """Width of the visible ink, which is what the layout is measured against.

    Pillow's own anchors work off font metrics (side bearings included), so every
    position here is derived from the ink box instead.
    """
    box = draw.textbbox((0, 0), text, font=font, anchor="ls")
    return box[2] - box[0]


def draw_at(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont,
            ink_left: float, baseline: int) -> None:
    """Draw text so its leftmost ink lands on ink_left, sitting on the baseline."""
    box = draw.textbbox((0, baseline), text, font=font, anchor="ls")
    draw.text((round(ink_left - box[0]), baseline), text, font=font, fill=INK, anchor="ls")


def load_logo(logo_path: Path) -> Image.Image:
    logo = Image.open(logo_path)
    logo = logo.convert("RGBA") if "A" in logo.getbands() else logo.convert("RGB")

    scale = min(LOGO_MAX_SIZE[0] / logo.width, LOGO_MAX_SIZE[1] / logo.height, 1.0)
    if scale < 1.0:
        logo = logo.resize((round(logo.width * scale), round(logo.height * scale)),
                           Image.LANCZOS)
    return logo


def fit_row(draw: ImageDraw.ImageDraw, date: str, logo_width: int) -> tuple[ImageFont.FreeTypeFont, int, int]:
    """Choose the date's font size and the gap to the logo so the row fits the margins.

    Returns (font, date ink width, gap). With no logo, the gap is 0.
    """
    max_row = WIDTH - 2 * SIDE_MARGIN
    for size in range(DATE_SIZE, MIN_DATE_SIZE - 1, -1):
        font = load_font(FACE_REGULAR, size)
        width = ink_width(draw, date, font)
        if not logo_width:
            if width <= max_row:
                return font, width, 0
            continue
        gap = min(PREFERRED_GAP, max_row - width - logo_width)
        if gap >= MIN_GAP:
            return font, width, gap
    sys.exit(
        f'error: the date "{date}" does not fit'
        + (f" beside a {logo_width}px-wide logo" if logo_width else "")
        + f", even at {MIN_DATE_SIZE}px.\n"
        'Use a shorter form of the date (e.g. "Dec 9, 2026").'
    )


def build(date: str, logo_path: Path | None) -> Image.Image:
    canvas = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(canvas)

    title_font = load_font(FACE_CONDENSED_BOLD, TITLE_SIZE)
    draw_at(draw, TITLE, title_font,
            TITLE_CENTER_X - ink_width(draw, TITLE, title_font) / 2, TITLE_BASELINE)

    logo = load_logo(logo_path) if logo_path else None
    date_font, date_width, gap = fit_row(draw, date, logo.width if logo else 0)

    row_width = date_width + gap + (logo.width if logo else 0)
    row_left = (WIDTH - row_width) / 2
    draw_at(draw, date, date_font, row_left, DATE_BASELINE)
    if logo:
        canvas.paste(logo,
                     (round(row_left + date_width + gap), round(LOGO_CENTER_Y - logo.height / 2)),
                     logo if logo.mode == "RGBA" else None)
    return canvas


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--date", required=True,
                        help='date line, e.g. "December 9, 2026"')
    parser.add_argument("--logo",
                        help="logo name in images/logos (e.g. waterloo) or a path to a PNG; "
                             "omit for a card with no logo, which centres the date")
    parser.add_argument("--out", required=True, help="output PNG path")
    args = parser.parse_args()

    image = build(args.date, resolve_logo(args.logo) if args.logo else None)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    image.save(out)
    print(f"wrote {out} ({image.width}x{image.height})")


if __name__ == "__main__":
    main()
