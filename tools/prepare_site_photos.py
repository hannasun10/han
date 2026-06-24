from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter, ImageOps


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "site-photos"
OUT.mkdir(parents=True, exist_ok=True)

SRC = Path(r"C:\Users\홍주안\Desktop\강사프로필사")

PHOTOS = {
    "hero-professional": SRC / "KakaoTalk_20260624_134028985_04.png",
    "profile-close": SRC / "KakaoTalk_20260624_134028985_07.png",
    "lecture-main": SRC / "KakaoTalk_20260622_190003896_10.jpg",
    "lecture-wide": SRC / "KakaoTalk_20260622_190003896_04.jpg",
    "workshop-laptop": SRC / "KakaoTalk_20260622_190003896.jpg",
    "content-studio": SRC / "KakaoTalk_20260622_190003896_14.jpg",
    "field-class": SRC / "KakaoTalk_20260622_190003896_01.jpg",
    "portrait-formal": SRC / "KakaoTalk_20260624_134028985_06.png",
}


def enhance(img: Image.Image, portrait=False) -> Image.Image:
    img = img.convert("RGB")
    img = ImageEnhance.Brightness(img).enhance(1.12 if portrait else 1.18)
    img = ImageEnhance.Contrast(img).enhance(1.06 if portrait else 1.10)
    img = ImageEnhance.Color(img).enhance(1.04 if portrait else 1.08)
    warm = Image.new("RGB", img.size, (255, 250, 240))
    img = Image.blend(img, warm, 0.025 if portrait else 0.04)
    return img.filter(ImageFilter.UnsharpMask(radius=1.1, percent=70, threshold=3))


def cover_crop(img: Image.Image, size: tuple[int, int], center=(0.5, 0.5)) -> Image.Image:
    target_w, target_h = size
    src_w, src_h = img.size
    src_ratio = src_w / src_h
    target_ratio = target_w / target_h

    if src_ratio > target_ratio:
        crop_h = src_h
        crop_w = int(crop_h * target_ratio)
    else:
        crop_w = src_w
        crop_h = int(crop_w / target_ratio)

    cx = int(src_w * center[0])
    cy = int(src_h * center[1])
    left = max(0, min(src_w - crop_w, cx - crop_w // 2))
    top = max(0, min(src_h - crop_h, cy - crop_h // 2))
    cropped = img.crop((left, top, left + crop_w, top + crop_h))
    return cropped.resize(size, Image.Resampling.LANCZOS)


def contain_resize(img: Image.Image, max_size: tuple[int, int]) -> Image.Image:
    img = ImageOps.contain(img, max_size, Image.Resampling.LANCZOS)
    return img


def save_jpg(img: Image.Image, name: str, quality=88):
    path = OUT / f"{name}.jpg"
    img.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    return path


def main():
    outputs = []

    hero = enhance(Image.open(PHOTOS["hero-professional"]), portrait=True)
    outputs.append(save_jpg(cover_crop(hero, (900, 1080), center=(0.5, 0.38)), "hero-professional"))

    profile = enhance(Image.open(PHOTOS["profile-close"]), portrait=True)
    outputs.append(save_jpg(cover_crop(profile, (760, 760), center=(0.5, 0.45)), "profile-close"))

    portrait = enhance(Image.open(PHOTOS["portrait-formal"]), portrait=True)
    outputs.append(save_jpg(cover_crop(portrait, (780, 980), center=(0.5, 0.42)), "portrait-formal"))

    lecture = enhance(Image.open(PHOTOS["lecture-main"]))
    outputs.append(save_jpg(cover_crop(lecture, (1200, 760), center=(0.52, 0.55)), "lecture-main"))

    lecture_wide = enhance(Image.open(PHOTOS["lecture-wide"]))
    outputs.append(save_jpg(cover_crop(lecture_wide, (760, 560), center=(0.58, 0.55)), "lecture-wide"))

    workshop = enhance(Image.open(PHOTOS["workshop-laptop"]))
    outputs.append(save_jpg(cover_crop(workshop, (760, 560), center=(0.52, 0.56)), "workshop-laptop"))

    studio = enhance(Image.open(PHOTOS["content-studio"]))
    outputs.append(save_jpg(cover_crop(studio, (760, 560), center=(0.52, 0.52)), "content-studio"))

    field = enhance(Image.open(PHOTOS["field-class"]))
    outputs.append(save_jpg(cover_crop(field, (760, 560), center=(0.48, 0.55)), "field-class"))

    print("created")
    for path in outputs:
        print(path)


if __name__ == "__main__":
    main()
