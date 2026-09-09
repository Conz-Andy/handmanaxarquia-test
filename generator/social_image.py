"""Social-share (Open Graph) images and image-dimension helper.

- build_default(site): renders site/images/og-default.jpg (1200x630) — a
  project photo with the brand bar — used by pages that have no photo of their own.
- og_for(site, src): makes a 1200x630 JPEG variant of a gallery .webp (cached
  under site/images/og/) and returns its root-relative URL.
- dims(site, src): (width, height) of an image under site/, for width/height
  attributes (prevents layout shift).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ORANGE = (251, 169, 23)
BLACK = (11, 11, 12)
W, H = 1200, 630
_DIMS = {}

def _font(size, bold=True):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"]:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def _cover(img, w, h):
    r = max(w / img.width, h / img.height)
    img = img.resize((round(img.width * r), round(img.height * r)), Image.LANCZOS)
    x = (img.width - w) // 2; y = (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))

def _compose(site: Path, photo: Path, out: Path, caption=None):
    canvas = Image.new("RGB", (W, H), BLACK)
    img = Image.open(photo).convert("RGB")
    # photo on the right two-thirds, brand panel on the left
    pw = 760
    canvas.paste(_cover(img, pw, H), (W - pw, 0))
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, 0, W - pw, H], fill=BLACK)
    d.rectangle([0, 0, 14, H], fill=ORANGE)
    logo = site / "images/logo.png"
    if logo.exists():
        lg = Image.open(logo).convert("RGBA").resize((120, 120), Image.LANCZOS)
        canvas.paste(lg, (60, 70), lg)
    d.text((60, 225), "HANDYMAN", font=_font(50), fill=(255, 255, 255))
    d.text((60, 283), "AXARQUIA", font=_font(50), fill=ORANGE)
    d.text((60, 370), "Builders & reforms", font=_font(26, False), fill=(214, 214, 218))
    d.text((60, 404), "Eastern Costa del Sol", font=_font(26, False), fill=(214, 214, 218))
    d.text((60, 470), "+34 711 027 432", font=_font(28), fill=ORANGE)
    d.text((60, 512), "handymanaxarquia.com", font=_font(22, False), fill=(142, 142, 147))
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out, "JPEG", quality=82, optimize=True, progressive=True)

def build_default(site: Path):
    photo = site / "wp-content/uploads/2026/08/handyman-axarquia-pergola-vinuela-after.webp"
    if photo.exists():
        _compose(site, photo, site / "images/og-default.jpg")

def og_for(site: Path, src: str) -> str:
    photo = site / src.lstrip("/")
    name = Path(src).stem + ".jpg"
    out = site / "images/og" / name
    if photo.exists() and not out.exists():
        _compose(site, photo, out)
    return f"/images/og/{name}" if out.exists() else "/images/og-default.jpg"

def dims(site: Path, src: str):
    if src not in _DIMS:
        p = site / src.lstrip("/")
        _DIMS[src] = Image.open(p).size if p.exists() else (4, 3)
    return _DIMS[src]
