from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

PROFILE_SRC = Path(r"C:\Users\홍주안\Desktop\강사프로필사\KakaoTalk_20260622_160251210.png")
CLASS_SRC = Path(r"C:\Users\홍주안\Desktop\강사프로필사\KakaoTalk_20260622_190003896_12.jpg")


def brighten_portrait(img: Image.Image) -> Image.Image:
    img = img.convert("RGB")
    img = ImageEnhance.Brightness(img).enhance(1.10)
    img = ImageEnhance.Contrast(img).enhance(1.05)
    img = ImageEnhance.Color(img).enhance(1.05)
    img = ImageEnhance.Sharpness(img).enhance(1.08)
    warm = Image.new("RGB", img.size, (255, 248, 235))
    img = Image.blend(img, warm, 0.035)
    return img


def brighten_classroom(img: Image.Image) -> Image.Image:
    img = img.convert("RGB")
    img = ImageEnhance.Brightness(img).enhance(1.22)
    img = ImageEnhance.Contrast(img).enhance(1.08)
    img = ImageEnhance.Color(img).enhance(1.08)
    warm = Image.new("RGB", img.size, (255, 250, 238))
    img = Image.blend(img, warm, 0.045)
    return img.filter(ImageFilter.UnsharpMask(radius=1.2, percent=65, threshold=3))


def make_hero_crop(img: Image.Image) -> Image.Image:
    width, height = img.size
    target_ratio = 430 / 520
    crop_h = min(height, int(width / target_ratio))
    top = max(0, min(95, height - crop_h))
    crop = img.crop((0, top, width, top + crop_h))
    return crop.resize((860, 1040), Image.Resampling.LANCZOS)


def main():
    portrait = brighten_portrait(Image.open(PROFILE_SRC))
    portrait.save(ASSETS / "katehong-profile-bright.png")

    hero = make_hero_crop(portrait)
    hero.save(ASSETS / "katehong-hero-bright.png")

    classroom = brighten_classroom(Image.open(CLASS_SRC))
    classroom.save(ASSETS / "katehong-classroom-bright.png")

    print("created assets/katehong-profile-bright.png")
    print("created assets/katehong-hero-bright.png")
    print("created assets/katehong-classroom-bright.png")


if __name__ == "__main__":
    main()
