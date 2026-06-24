from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "logo_outputs"
OUT.mkdir(exist_ok=True)

SCALE = 3
SIZE = 1024
W = H = SIZE * SCALE

FONT_DIR = Path("C:/Windows/Fonts")
FONT_BOLD = FONT_DIR / "arialbd.ttf"
FONT_REG = FONT_DIR / "arial.ttf"
FONT_NARROW_BOLD = FONT_DIR / "ARIALNB.TTF"
FONT_BAHN = FONT_DIR / "bahnschrift.ttf"


COLORS = {
    "pantone_2945": "#004C97",
    "pantone_300": "#005EB8",
    "pantone_2925": "#009CDE",
    "classic_blue": "#0F4C81",
    "startup_navy": "#172B85",
    "ink": "#10233F",
    "cream": "#FFFDF8",
    "soft_blue": "#D7ECFF",
    "line": "#C7D8EF",
}


def hex_to_rgba(value, alpha=255):
    value = value.strip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def font(path, size):
    return ImageFont.truetype(str(path), size * SCALE)


def new_canvas(bg=None):
    if bg is None:
        return Image.new("RGBA", (W, H), (255, 255, 255, 0))
    return Image.new("RGBA", (W, H), hex_to_rgba(bg))


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def draw_centered_text(draw, xy, text, fnt, fill, anchor="mm", spacing=0):
    draw.text(xy, text, font=fnt, fill=fill, anchor=anchor, spacing=spacing)


def draw_wordmark(draw, center_x, y, main_size, sub_size, color, align="center"):
    title_font = font(FONT_BOLD, main_size)
    sub_font = font(FONT_REG, sub_size)
    main = "Katie Hong"
    sub = "AI EDUCATION · PRACTICAL GROWTH"
    if align == "left":
        draw.text((center_x, y), main, font=title_font, fill=color, anchor="la")
        draw.text((center_x + 4 * SCALE, y + main_size * 1.05 * SCALE), sub, font=sub_font, fill=hex_to_rgba(COLORS["classic_blue"], 215), anchor="la")
    else:
        draw.text((center_x, y), main, font=title_font, fill=color, anchor="ma")
        draw.text((center_x, y + main_size * 1.05 * SCALE), sub, font=sub_font, fill=hex_to_rgba(COLORS["classic_blue"], 215), anchor="ma")


def save(img, name):
    img = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    path = OUT / name
    img.save(path)
    return path


def concept_01_horizontal_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = hex_to_rgba(COLORS["pantone_2945"])
    light = hex_to_rgba(COLORS["soft_blue"], 255)
    icon_x, icon_y = 250 * SCALE, 512 * SCALE
    r = 136 * SCALE
    d.rounded_rectangle((icon_x - r, icon_y - r, icon_x + r, icon_y + r), radius=48 * SCALE, fill=blue)
    d.text((icon_x, icon_y + 2 * SCALE), "KH", font=font(FONT_BOLD, 96), fill=(255, 255, 255, 255), anchor="mm")
    d.ellipse((icon_x + 80 * SCALE, icon_y - 112 * SCALE, icon_x + 110 * SCALE, icon_y - 82 * SCALE), fill=hex_to_rgba(COLORS["pantone_2925"]))
    d.line((icon_x + 63 * SCALE, icon_y - 72 * SCALE, icon_x + 95 * SCALE, icon_y - 97 * SCALE), fill=light, width=8 * SCALE)
    draw_wordmark(d, 432 * SCALE, 444 * SCALE, 73, 22, blue, align="left")
    return save(img, "katiehong_concept01_horizontal_A.png")


def concept_01_horizontal_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = hex_to_rgba(COLORS["pantone_300"])
    d.text((512 * SCALE, 460 * SCALE), "KATIE HONG", font=font(FONT_NARROW_BOLD, 86), fill=blue, anchor="mm")
    d.rounded_rectangle((221 * SCALE, 528 * SCALE, 803 * SCALE, 548 * SCALE), radius=10 * SCALE, fill=hex_to_rgba(COLORS["pantone_2925"]))
    d.text((512 * SCALE, 604 * SCALE), "AI EDUCATION FOR REAL WORK", font=font(FONT_REG, 28), fill=hex_to_rgba(COLORS["classic_blue"], 225), anchor="mm")
    d.ellipse((795 * SCALE, 437 * SCALE, 823 * SCALE, 465 * SCALE), fill=hex_to_rgba(COLORS["pantone_2925"]))
    return save(img, "katiehong_concept01_horizontal_B.png")


def concept_01_vertical_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = hex_to_rgba(COLORS["pantone_2945"])
    icon_x, icon_y = 512 * SCALE, 355 * SCALE
    d.rounded_rectangle((332 * SCALE, 175 * SCALE, 692 * SCALE, 535 * SCALE), radius=72 * SCALE, fill=blue)
    d.text((icon_x, icon_y + 5 * SCALE), "KH", font=font(FONT_BOLD, 132), fill=(255, 255, 255, 255), anchor="mm")
    d.line((632 * SCALE, 232 * SCALE, 677 * SCALE, 197 * SCALE), fill=hex_to_rgba(COLORS["soft_blue"]), width=9 * SCALE)
    d.ellipse((674 * SCALE, 182 * SCALE, 718 * SCALE, 226 * SCALE), fill=hex_to_rgba(COLORS["pantone_2925"]))
    draw_wordmark(d, 512 * SCALE, 637 * SCALE, 70, 22, blue)
    return save(img, "katiehong_concept01_vertical_A.png")


def concept_01_vertical_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = hex_to_rgba(COLORS["startup_navy"])
    d.text((512 * SCALE, 310 * SCALE), "KH", font=font(FONT_BOLD, 190), fill=blue, anchor="mm")
    d.rounded_rectangle((352 * SCALE, 430 * SCALE, 672 * SCALE, 448 * SCALE), radius=9 * SCALE, fill=hex_to_rgba(COLORS["pantone_2925"]))
    d.text((512 * SCALE, 550 * SCALE), "Katie", font=font(FONT_BOLD, 96), fill=blue, anchor="mm")
    d.text((512 * SCALE, 648 * SCALE), "Hong", font=font(FONT_BOLD, 96), fill=blue, anchor="mm")
    d.text((512 * SCALE, 750 * SCALE), "PRACTICAL AI LEARNING", font=font(FONT_REG, 24), fill=hex_to_rgba(COLORS["classic_blue"], 220), anchor="mm")
    return save(img, "katiehong_concept01_vertical_B.png")


def concept_02_horizontal_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = hex_to_rgba(COLORS["classic_blue"])
    accent = hex_to_rgba(COLORS["pantone_2925"])
    nodes = [(196, 450), (248, 392), (302, 458), (252, 526), (344, 520)]
    nodes = [(x * SCALE, y * SCALE) for x, y in nodes]
    for a, b in [(0, 1), (1, 2), (0, 3), (2, 4), (3, 4), (2, 3)]:
        d.line((nodes[a], nodes[b]), fill=hex_to_rgba(COLORS["line"]), width=7 * SCALE)
    for i, (x, y) in enumerate(nodes):
        d.ellipse((x - 20 * SCALE, y - 20 * SCALE, x + 20 * SCALE, y + 20 * SCALE), fill=accent if i in (1, 4) else blue)
    draw_wordmark(d, 410 * SCALE, 442 * SCALE, 67, 21, blue, align="left")
    return save(img, "katiehong_concept02_horizontal_A.png")


def concept_02_horizontal_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = hex_to_rgba(COLORS["pantone_2945"])
    d.text((512 * SCALE, 462 * SCALE), "Katie Hong", font=font(FONT_BOLD, 88), fill=blue, anchor="mm")
    dot_positions = [(338, 394), (374, 348), (431, 369), (676, 386), (725, 344), (763, 398)]
    for x, y in dot_positions:
        d.ellipse(((x - 10) * SCALE, (y - 10) * SCALE, (x + 10) * SCALE, (y + 10) * SCALE), fill=hex_to_rgba(COLORS["pantone_2925"]))
    d.text((512 * SCALE, 576 * SCALE), "AI LITERACY · WORKSHOP · CONSULTING", font=font(FONT_REG, 26), fill=hex_to_rgba(COLORS["classic_blue"], 220), anchor="mm")
    return save(img, "katiehong_concept02_horizontal_B.png")


def concept_02_vertical_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = hex_to_rgba(COLORS["classic_blue"])
    accent = hex_to_rgba(COLORS["pantone_2925"])
    center = (512 * SCALE, 330 * SCALE)
    d.ellipse((330 * SCALE, 148 * SCALE, 694 * SCALE, 512 * SCALE), outline=hex_to_rgba(COLORS["line"]), width=12 * SCALE)
    points = [(512, 214), (404, 314), (515, 390), (624, 306), (590, 455)]
    pts = [(x * SCALE, y * SCALE) for x, y in points]
    for a, b in [(0, 1), (0, 3), (1, 2), (2, 3), (2, 4), (3, 4)]:
        d.line((pts[a], pts[b]), fill=hex_to_rgba(COLORS["line"]), width=8 * SCALE)
    for i, (x, y) in enumerate(pts):
        d.ellipse((x - 25 * SCALE, y - 25 * SCALE, x + 25 * SCALE, y + 25 * SCALE), fill=accent if i in (0, 4) else blue)
    d.text(center, "KH", font=font(FONT_BOLD, 78), fill=blue, anchor="mm")
    draw_wordmark(d, 512 * SCALE, 612 * SCALE, 68, 22, blue)
    return save(img, "katiehong_concept02_vertical_A.png")


def concept_02_vertical_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = hex_to_rgba(COLORS["pantone_300"])
    d.text((512 * SCALE, 280 * SCALE), "Katie", font=font(FONT_BOLD, 104), fill=blue, anchor="mm")
    d.text((512 * SCALE, 392 * SCALE), "Hong", font=font(FONT_BOLD, 104), fill=blue, anchor="mm")
    for x, y, r in [(344, 490, 17), (438, 532, 14), (512, 486, 20), (594, 534, 14), (682, 488, 17)]:
        d.ellipse(((x - r) * SCALE, (y - r) * SCALE, (x + r) * SCALE, (y + r) * SCALE), fill=hex_to_rgba(COLORS["pantone_2925"]))
    d.line((344 * SCALE, 490 * SCALE, 438 * SCALE, 532 * SCALE, 512 * SCALE, 486 * SCALE, 594 * SCALE, 534 * SCALE, 682 * SCALE, 488 * SCALE), fill=hex_to_rgba(COLORS["line"]), width=7 * SCALE)
    d.text((512 * SCALE, 670 * SCALE), "AI EDUCATION", font=font(FONT_REG, 30), fill=hex_to_rgba(COLORS["classic_blue"], 230), anchor="mm")
    return save(img, "katiehong_concept02_vertical_B.png")


def concept_03_horizontal_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    navy = hex_to_rgba(COLORS["startup_navy"])
    accent = hex_to_rgba(COLORS["pantone_2925"])
    d.text((512 * SCALE, 462 * SCALE), "Katie Hong", font=font(FONT_BAHN, 92), fill=navy, anchor="mm")
    d.line((252 * SCALE, 540 * SCALE, 772 * SCALE, 540 * SCALE), fill=accent, width=14 * SCALE)
    d.polygon([(772 * SCALE, 540 * SCALE), (722 * SCALE, 513 * SCALE), (732 * SCALE, 568 * SCALE)], fill=accent)
    d.text((512 * SCALE, 608 * SCALE), "START SMART WITH AI", font=font(FONT_REG, 26), fill=hex_to_rgba(COLORS["classic_blue"], 220), anchor="mm")
    return save(img, "katiehong_concept03_horizontal_A.png")


def concept_03_horizontal_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = hex_to_rgba(COLORS["pantone_2945"])
    d.rounded_rectangle((178 * SCALE, 405 * SCALE, 846 * SCALE, 620 * SCALE), radius=44 * SCALE, outline=blue, width=9 * SCALE)
    d.text((512 * SCALE, 488 * SCALE), "KATIE HONG", font=font(FONT_NARROW_BOLD, 76), fill=blue, anchor="mm")
    d.text((512 * SCALE, 560 * SCALE), "AI MARKETING · EDUCATION", font=font(FONT_REG, 25), fill=hex_to_rgba(COLORS["classic_blue"], 230), anchor="mm")
    d.rectangle((208 * SCALE, 604 * SCALE, 815 * SCALE, 620 * SCALE), fill=hex_to_rgba(COLORS["pantone_2925"]))
    return save(img, "katiehong_concept03_horizontal_B.png")


def concept_03_vertical_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    navy = hex_to_rgba(COLORS["startup_navy"])
    accent = hex_to_rgba(COLORS["pantone_2925"])
    d.text((512 * SCALE, 262 * SCALE), "K", font=font(FONT_BAHN, 210), fill=navy, anchor="mm")
    d.line((420 * SCALE, 414 * SCALE, 608 * SCALE, 352 * SCALE), fill=accent, width=15 * SCALE)
    d.polygon([(608 * SCALE, 352 * SCALE), (558 * SCALE, 336 * SCALE), (582 * SCALE, 390 * SCALE)], fill=accent)
    d.text((512 * SCALE, 548 * SCALE), "Katie", font=font(FONT_BOLD, 88), fill=navy, anchor="mm")
    d.text((512 * SCALE, 642 * SCALE), "Hong", font=font(FONT_BOLD, 88), fill=navy, anchor="mm")
    d.text((512 * SCALE, 752 * SCALE), "AI MARKETING EDUCATOR", font=font(FONT_REG, 25), fill=hex_to_rgba(COLORS["classic_blue"], 225), anchor="mm")
    return save(img, "katiehong_concept03_vertical_A.png")


def concept_03_vertical_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = hex_to_rgba(COLORS["pantone_300"])
    d.rounded_rectangle((278 * SCALE, 140 * SCALE, 746 * SCALE, 608 * SCALE), radius=72 * SCALE, outline=blue, width=12 * SCALE)
    d.text((512 * SCALE, 330 * SCALE), "KH", font=font(FONT_BOLD, 156), fill=blue, anchor="mm")
    d.rectangle((340 * SCALE, 514 * SCALE, 684 * SCALE, 532 * SCALE), fill=hex_to_rgba(COLORS["pantone_2925"]))
    d.text((512 * SCALE, 700 * SCALE), "Katie Hong", font=font(FONT_BOLD, 72), fill=blue, anchor="mm")
    d.text((512 * SCALE, 780 * SCALE), "PRACTICAL STARTUP IDENTITY", font=font(FONT_REG, 22), fill=hex_to_rgba(COLORS["classic_blue"], 220), anchor="mm")
    return save(img, "katiehong_concept03_vertical_B.png")


def create_contact_sheet(paths):
    thumb = 300
    pad = 36
    label_h = 44
    cols = 4
    rows = 3
    sheet = Image.new("RGB", (cols * thumb + (cols + 1) * pad, rows * (thumb + label_h) + (rows + 1) * pad), hex_to_rgba(COLORS["cream"])[:3])
    d = ImageDraw.Draw(sheet)
    label_font = ImageFont.truetype(str(FONT_REG), 18)
    for idx, path in enumerate(paths):
        x = pad + (idx % cols) * (thumb + pad)
        y = pad + (idx // cols) * (thumb + label_h + pad)
        tile = Image.new("RGBA", (thumb, thumb), (255, 255, 255, 255))
        logo = Image.open(path).convert("RGBA").resize((thumb, thumb), Image.Resampling.LANCZOS)
        tile.alpha_composite(logo)
        sheet.paste(tile.convert("RGB"), (x, y))
        label = path.stem.replace("katiehong_", "").replace("_", " ")
        d.text((x + thumb // 2, y + thumb + 10), label, font=label_font, fill=hex_to_rgba(COLORS["ink"])[:3], anchor="ma")
    out = OUT / "katiehong_logo_contact_sheet.png"
    sheet.save(out)
    return out


def main():
    paths = [
        concept_01_horizontal_a(),
        concept_01_horizontal_b(),
        concept_01_vertical_a(),
        concept_01_vertical_b(),
        concept_02_horizontal_a(),
        concept_02_horizontal_b(),
        concept_02_vertical_a(),
        concept_02_vertical_b(),
        concept_03_horizontal_a(),
        concept_03_horizontal_b(),
        concept_03_vertical_a(),
        concept_03_vertical_b(),
    ]
    sheet = create_contact_sheet(paths)
    print("Generated:")
    for p in paths:
        print(p)
    print(sheet)


if __name__ == "__main__":
    main()
