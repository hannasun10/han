from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "logo_outputs_ai융합지도사_katehong"
OUT.mkdir(exist_ok=True)

SCALE = 3
SIZE = 1024
W = H = SIZE * SCALE

FONT_DIR = Path("C:/Windows/Fonts")
FONT_KO_REG = FONT_DIR / "NotoSansCJKkr-Regular.otf"
FONT_KO_BOLD = FONT_DIR / "malgunbd.ttf"
FONT_EN_BOLD = FONT_DIR / "arialbd.ttf"
FONT_EN_REG = FONT_DIR / "arial.ttf"
FONT_EN_NARROW = FONT_DIR / "ARIALNB.TTF"
FONT_EN_STARTUP = FONT_DIR / "bahnschrift.ttf"

COLORS = {
    "pantone_2945": "#004C97",
    "pantone_300": "#005EB8",
    "pantone_2925": "#009CDE",
    "classic_blue": "#0F4C81",
    "deep_blue": "#172B85",
    "ink": "#10233F",
    "cream": "#FFFDF8",
    "soft_blue": "#D7ECFF",
    "line": "#C7D8EF",
}


def rgba(hex_color, alpha=255):
    h = hex_color.strip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def font(path, size):
    return ImageFont.truetype(str(path), size * SCALE)


def new_canvas(bg=None):
    if bg is None:
        return Image.new("RGBA", (W, H), (255, 255, 255, 0))
    return Image.new("RGBA", (W, H), rgba(bg))


def fit_text(draw, text, font_path, max_width, start_size, min_size=18):
    for size in range(start_size, min_size - 1, -1):
        f = font(font_path, size)
        box = draw.textbbox((0, 0), text, font=f)
        if box[2] - box[0] <= max_width * SCALE:
            return f
    return font(font_path, min_size)


def draw_tagline(draw, x, y, text, size=22, color=None, anchor="ma"):
    color = color or rgba(COLORS["classic_blue"], 225)
    draw.text((x, y), text, font=font(FONT_EN_REG, size), fill=color, anchor=anchor)


def draw_kh_chip(draw, cx, cy, size, fill_color, accent=True):
    r = size * SCALE
    draw.rounded_rectangle(
        (cx - r, cy - r, cx + r, cy + r),
        radius=int(size * 0.34 * SCALE),
        fill=fill_color,
    )
    draw.text((cx, cy + 2 * SCALE), "KH", font=font(FONT_EN_BOLD, int(size * 0.72)), fill=(255, 255, 255, 255), anchor="mm")
    if accent:
        draw.line((cx + int(size * 0.48) * SCALE, cy - int(size * 0.56) * SCALE, cx + int(size * 0.75) * SCALE, cy - int(size * 0.78) * SCALE), fill=rgba(COLORS["soft_blue"]), width=max(4, int(size * 0.055 * SCALE)))
        dot = int(size * 0.13 * SCALE)
        dx, dy = cx + int(size * 0.8) * SCALE, cy - int(size * 0.82) * SCALE
        draw.ellipse((dx - dot, dy - dot, dx + dot, dy + dot), fill=rgba(COLORS["pantone_2925"]))


def save(img, name):
    path = OUT / name
    img.resize((SIZE, SIZE), Image.Resampling.LANCZOS).save(path)
    return path


def concept01_horizontal_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = rgba(COLORS["pantone_2945"])
    draw_kh_chip(d, 230 * SCALE, 500 * SCALE, 118, blue)
    ko = fit_text(d, "AI 융합 지도사", FONT_KO_BOLD, 520, 54)
    d.text((385 * SCALE, 430 * SCALE), "AI 융합 지도사", font=ko, fill=blue, anchor="la")
    d.text((388 * SCALE, 505 * SCALE), "Kate Hong", font=font(FONT_EN_BOLD, 62), fill=rgba(COLORS["deep_blue"]), anchor="la")
    d.rounded_rectangle((390 * SCALE, 578 * SCALE, 786 * SCALE, 596 * SCALE), radius=9 * SCALE, fill=rgba(COLORS["pantone_2925"]))
    draw_tagline(d, 392 * SCALE, 638 * SCALE, "AI FUSION EDUCATOR · PRACTICAL BUSINESS GROWTH", 21, anchor="la")
    return save(img, "ai_fusion_katehong_concept01_horizontal_A.png")


def concept01_horizontal_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = rgba(COLORS["pantone_300"])
    ko = fit_text(d, "AI 융합 지도사", FONT_KO_BOLD, 620, 62)
    d.text((512 * SCALE, 410 * SCALE), "AI 융합 지도사", font=ko, fill=blue, anchor="mm")
    d.text((512 * SCALE, 505 * SCALE), "KATE HONG", font=font(FONT_EN_NARROW, 82), fill=rgba(COLORS["deep_blue"]), anchor="mm")
    d.rounded_rectangle((245 * SCALE, 568 * SCALE, 779 * SCALE, 586 * SCALE), radius=9 * SCALE, fill=rgba(COLORS["pantone_2925"]))
    draw_tagline(d, 512 * SCALE, 638 * SCALE, "AI · CONTENT MARKETING · STARTUP EDUCATION", 24)
    d.ellipse((775 * SCALE, 386 * SCALE, 804 * SCALE, 415 * SCALE), fill=rgba(COLORS["pantone_2925"]))
    return save(img, "ai_fusion_katehong_concept01_horizontal_B.png")


def concept01_vertical_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = rgba(COLORS["pantone_2945"])
    draw_kh_chip(d, 512 * SCALE, 314 * SCALE, 144, blue)
    ko = fit_text(d, "AI 융합 지도사", FONT_KO_BOLD, 710, 62)
    d.text((512 * SCALE, 568 * SCALE), "AI 융합 지도사", font=ko, fill=blue, anchor="mm")
    d.text((512 * SCALE, 664 * SCALE), "Kate Hong", font=font(FONT_EN_BOLD, 70), fill=rgba(COLORS["deep_blue"]), anchor="mm")
    draw_tagline(d, 512 * SCALE, 744 * SCALE, "PRACTICAL AI LEARNING", 25)
    return save(img, "ai_fusion_katehong_concept01_vertical_A.png")


def concept01_vertical_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = rgba(COLORS["deep_blue"])
    d.text((512 * SCALE, 274 * SCALE), "KH", font=font(FONT_EN_BOLD, 178), fill=blue, anchor="mm")
    d.rounded_rectangle((360 * SCALE, 402 * SCALE, 664 * SCALE, 420 * SCALE), radius=9 * SCALE, fill=rgba(COLORS["pantone_2925"]))
    d.text((512 * SCALE, 517 * SCALE), "AI 융합", font=font(FONT_KO_BOLD, 70), fill=rgba(COLORS["pantone_2945"]), anchor="mm")
    d.text((512 * SCALE, 610 * SCALE), "지도사", font=font(FONT_KO_BOLD, 70), fill=rgba(COLORS["pantone_2945"]), anchor="mm")
    d.text((512 * SCALE, 720 * SCALE), "Kate Hong", font=font(FONT_EN_BOLD, 56), fill=blue, anchor="mm")
    return save(img, "ai_fusion_katehong_concept01_vertical_B.png")


def concept02_horizontal_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = rgba(COLORS["classic_blue"])
    accent = rgba(COLORS["pantone_2925"])
    pts = [(168, 505), (222, 432), (294, 485), (246, 568), (342, 548)]
    pts = [(x * SCALE, y * SCALE) for x, y in pts]
    for a, b in [(0, 1), (1, 2), (0, 3), (2, 4), (3, 4), (2, 3)]:
        d.line((pts[a], pts[b]), fill=rgba(COLORS["line"]), width=7 * SCALE)
    for idx, (x, y) in enumerate(pts):
        r = 20 * SCALE
        d.ellipse((x - r, y - r, x + r, y + r), fill=accent if idx in (1, 4) else blue)
    d.text((390 * SCALE, 430 * SCALE), "AI 융합 지도사", font=fit_text(d, "AI 융합 지도사", FONT_KO_BOLD, 510, 50), fill=blue, anchor="la")
    d.text((392 * SCALE, 505 * SCALE), "Kate Hong", font=font(FONT_EN_BOLD, 62), fill=rgba(COLORS["deep_blue"]), anchor="la")
    draw_tagline(d, 394 * SCALE, 586 * SCALE, "CONNECTED AI · PRACTICAL CONTENT STRATEGY", 22, anchor="la")
    return save(img, "ai_fusion_katehong_concept02_horizontal_A.png")


def concept02_horizontal_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = rgba(COLORS["pantone_2945"])
    for x, y in [(334, 383), (380, 347), (432, 371), (616, 367), (680, 340), (736, 388)]:
        d.ellipse(((x - 10) * SCALE, (y - 10) * SCALE, (x + 10) * SCALE, (y + 10) * SCALE), fill=rgba(COLORS["pantone_2925"]))
    d.text((512 * SCALE, 460 * SCALE), "AI 융합 지도사", font=fit_text(d, "AI 융합 지도사", FONT_KO_BOLD, 680, 64), fill=blue, anchor="mm")
    d.text((512 * SCALE, 548 * SCALE), "Kate Hong", font=font(FONT_EN_BOLD, 66), fill=rgba(COLORS["deep_blue"]), anchor="mm")
    draw_tagline(d, 512 * SCALE, 628 * SCALE, "AI LITERACY · MARKETING · EDUCATION", 24)
    return save(img, "ai_fusion_katehong_concept02_horizontal_B.png")


def concept02_vertical_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = rgba(COLORS["classic_blue"])
    accent = rgba(COLORS["pantone_2925"])
    d.ellipse((330 * SCALE, 138 * SCALE, 694 * SCALE, 502 * SCALE), outline=rgba(COLORS["line"]), width=12 * SCALE)
    pts = [(512, 214), (404, 314), (515, 390), (624, 306), (590, 455)]
    pts = [(x * SCALE, y * SCALE) for x, y in pts]
    for a, b in [(0, 1), (0, 3), (1, 2), (2, 3), (2, 4), (3, 4)]:
        d.line((pts[a], pts[b]), fill=rgba(COLORS["line"]), width=8 * SCALE)
    for idx, (x, y) in enumerate(pts):
        r = 25 * SCALE
        d.ellipse((x - r, y - r, x + r, y + r), fill=accent if idx in (0, 4) else blue)
    d.text((512 * SCALE, 333 * SCALE), "AI", font=font(FONT_EN_BOLD, 70), fill=blue, anchor="mm")
    d.text((512 * SCALE, 588 * SCALE), "AI 융합 지도사", font=fit_text(d, "AI 융합 지도사", FONT_KO_BOLD, 710, 60), fill=blue, anchor="mm")
    d.text((512 * SCALE, 682 * SCALE), "Kate Hong", font=font(FONT_EN_BOLD, 66), fill=rgba(COLORS["deep_blue"]), anchor="mm")
    draw_tagline(d, 512 * SCALE, 762 * SCALE, "CONNECTED LEARNING SYSTEM", 24)
    return save(img, "ai_fusion_katehong_concept02_vertical_A.png")


def concept02_vertical_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = rgba(COLORS["pantone_300"])
    d.text((512 * SCALE, 248 * SCALE), "AI 융합", font=font(FONT_KO_BOLD, 76), fill=blue, anchor="mm")
    d.text((512 * SCALE, 350 * SCALE), "지도사", font=font(FONT_KO_BOLD, 76), fill=blue, anchor="mm")
    d.text((512 * SCALE, 456 * SCALE), "Kate Hong", font=font(FONT_EN_BOLD, 62), fill=rgba(COLORS["deep_blue"]), anchor="mm")
    line = [(340, 556), (430, 600), (512, 548), (604, 600), (690, 552)]
    for i in range(len(line) - 1):
        d.line((line[i][0] * SCALE, line[i][1] * SCALE, line[i + 1][0] * SCALE, line[i + 1][1] * SCALE), fill=rgba(COLORS["line"]), width=7 * SCALE)
    for x, y in line:
        r = 17 * SCALE
        d.ellipse((x * SCALE - r, y * SCALE - r, x * SCALE + r, y * SCALE + r), fill=rgba(COLORS["pantone_2925"]))
    draw_tagline(d, 512 * SCALE, 716 * SCALE, "AI CONTENT MARKETING", 27)
    return save(img, "ai_fusion_katehong_concept02_vertical_B.png")


def concept03_horizontal_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    navy = rgba(COLORS["deep_blue"])
    accent = rgba(COLORS["pantone_2925"])
    d.text((512 * SCALE, 413 * SCALE), "AI 융합 지도사", font=fit_text(d, "AI 융합 지도사", FONT_KO_BOLD, 690, 60), fill=navy, anchor="mm")
    d.text((512 * SCALE, 505 * SCALE), "Kate Hong", font=font(FONT_EN_STARTUP, 76), fill=rgba(COLORS["pantone_2945"]), anchor="mm")
    d.line((270 * SCALE, 584 * SCALE, 755 * SCALE, 584 * SCALE), fill=accent, width=14 * SCALE)
    d.polygon([(755 * SCALE, 584 * SCALE), (710 * SCALE, 558 * SCALE), (720 * SCALE, 611 * SCALE)], fill=accent)
    draw_tagline(d, 512 * SCALE, 650 * SCALE, "START SMART WITH PRACTICAL AI", 23)
    return save(img, "ai_fusion_katehong_concept03_horizontal_A.png")


def concept03_horizontal_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = rgba(COLORS["pantone_2945"])
    d.rounded_rectangle((158 * SCALE, 375 * SCALE, 866 * SCALE, 642 * SCALE), radius=46 * SCALE, outline=blue, width=9 * SCALE)
    d.text((512 * SCALE, 456 * SCALE), "AI 융합 지도사", font=fit_text(d, "AI 융합 지도사", FONT_KO_BOLD, 610, 56), fill=blue, anchor="mm")
    d.text((512 * SCALE, 542 * SCALE), "KATE HONG", font=font(FONT_EN_NARROW, 68), fill=rgba(COLORS["deep_blue"]), anchor="mm")
    d.rectangle((210 * SCALE, 624 * SCALE, 814 * SCALE, 642 * SCALE), fill=rgba(COLORS["pantone_2925"]))
    return save(img, "ai_fusion_katehong_concept03_horizontal_B.png")


def concept03_vertical_a():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    navy = rgba(COLORS["deep_blue"])
    accent = rgba(COLORS["pantone_2925"])
    d.text((512 * SCALE, 244 * SCALE), "K", font=font(FONT_EN_STARTUP, 210), fill=navy, anchor="mm")
    d.line((420 * SCALE, 398 * SCALE, 608 * SCALE, 336 * SCALE), fill=accent, width=15 * SCALE)
    d.polygon([(608 * SCALE, 336 * SCALE), (558 * SCALE, 320 * SCALE), (582 * SCALE, 374 * SCALE)], fill=accent)
    d.text((512 * SCALE, 520 * SCALE), "AI 융합", font=font(FONT_KO_BOLD, 68), fill=rgba(COLORS["pantone_2945"]), anchor="mm")
    d.text((512 * SCALE, 608 * SCALE), "지도사", font=font(FONT_KO_BOLD, 68), fill=rgba(COLORS["pantone_2945"]), anchor="mm")
    d.text((512 * SCALE, 714 * SCALE), "Kate Hong", font=font(FONT_EN_BOLD, 56), fill=navy, anchor="mm")
    return save(img, "ai_fusion_katehong_concept03_vertical_A.png")


def concept03_vertical_b():
    img = new_canvas()
    d = ImageDraw.Draw(img)
    blue = rgba(COLORS["pantone_300"])
    d.rounded_rectangle((276 * SCALE, 128 * SCALE, 748 * SCALE, 580 * SCALE), radius=72 * SCALE, outline=blue, width=12 * SCALE)
    d.text((512 * SCALE, 298 * SCALE), "AI", font=font(FONT_EN_BOLD, 138), fill=blue, anchor="mm")
    d.text((512 * SCALE, 424 * SCALE), "융합", font=font(FONT_KO_BOLD, 64), fill=rgba(COLORS["deep_blue"]), anchor="mm")
    d.rectangle((338 * SCALE, 508 * SCALE, 686 * SCALE, 527 * SCALE), fill=rgba(COLORS["pantone_2925"]))
    d.text((512 * SCALE, 664 * SCALE), "Kate Hong", font=font(FONT_EN_BOLD, 67), fill=blue, anchor="mm")
    d.text((512 * SCALE, 746 * SCALE), "AI 융합 지도사", font=fit_text(d, "AI 융합 지도사", FONT_KO_BOLD, 600, 38), fill=rgba(COLORS["classic_blue"], 230), anchor="mm")
    return save(img, "ai_fusion_katehong_concept03_vertical_B.png")


def contact_sheet(paths):
    thumb = 300
    pad = 36
    label_h = 48
    cols = 4
    rows = 3
    sheet = Image.new("RGB", (cols * thumb + (cols + 1) * pad, rows * (thumb + label_h) + (rows + 1) * pad), rgba(COLORS["cream"])[:3])
    d = ImageDraw.Draw(sheet)
    label_font = ImageFont.truetype(str(FONT_EN_REG), 18)
    for idx, p in enumerate(paths):
        x = pad + (idx % cols) * (thumb + pad)
        y = pad + (idx // cols) * (thumb + label_h + pad)
        tile = Image.new("RGBA", (thumb, thumb), (255, 255, 255, 255))
        logo = Image.open(p).convert("RGBA").resize((thumb, thumb), Image.Resampling.LANCZOS)
        tile.alpha_composite(logo)
        sheet.paste(tile.convert("RGB"), (x, y))
        label = p.stem.replace("ai_fusion_katehong_", "").replace("_", " ")
        d.text((x + thumb // 2, y + thumb + 10), label, font=label_font, fill=rgba(COLORS["ink"])[:3], anchor="ma")
    out = OUT / "ai_fusion_katehong_logo_contact_sheet.png"
    sheet.save(out)
    return out


def main():
    paths = [
        concept01_horizontal_a(),
        concept01_horizontal_b(),
        concept01_vertical_a(),
        concept01_vertical_b(),
        concept02_horizontal_a(),
        concept02_horizontal_b(),
        concept02_vertical_a(),
        concept02_vertical_b(),
        concept03_horizontal_a(),
        concept03_horizontal_b(),
        concept03_vertical_a(),
        concept03_vertical_b(),
    ]
    sheet = contact_sheet(paths)
    print("Generated")
    for p in paths:
        print(p.name)
    print(sheet.name)


if __name__ == "__main__":
    main()
