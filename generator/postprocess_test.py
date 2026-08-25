#!/usr/bin/env python3
"""Post-process built site into a GitHub-Pages test build (path prefix, inline logo CSS, noindex)."""
import base64, io, re, shutil, sys
from pathlib import Path
from PIL import Image

PREFIX = sys.argv[1] if len(sys.argv) > 1 else "/handmanaxarquia-test"
ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = ROOT / "test_build"

shutil.rmtree(OUT, ignore_errors=True)
OUT.mkdir()

# generate the /brand/ marketing pack into site/ before processing
import brand_pack
brand_pack.build(SITE)
import qr_fix
qr_fix.ensure(SITE)
import tshirt_spec
tshirt_spec.apply(SITE)
import mobile_fix
mobile_fix.apply(SITE)

# copy shared images the brand pages reference
(OUT / "images").mkdir()
for f in ("logo.png", "logo_mark.svg", "qr_website.png", "qr_vcard.png"):
    src = SITE / "images" / f
    if src.exists():
        (OUT / "images" / f).write_bytes(src.read_bytes())

img = Image.open(SITE / "images/logo.png")
b = io.BytesIO(); img.resize((160, 160), Image.LANCZOS).save(b, "PNG", optimize=True)
logo = "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()
mark = "data:image/svg+xml;base64," + base64.b64encode((SITE / "images/logo_mark.svg").read_bytes()).decode()

css = (SITE / "css/style.css").read_text()
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
css = re.sub(r"\n\s+", "\n", css).replace("\n\n", "\n")
css += ("\n.logoimg{display:block;width:44px;height:44px;background:url(" + logo + ") center/contain no-repeat;flex:0 0 auto}"
        "\n.brandline .logoimg{width:40px;height:40px}"
        "\n.markbg{background:url(" + mark + ") center/contain no-repeat;height:440px;display:block}")
(OUT / "css").mkdir()
(OUT / "css/style.css").write_text(css)

for f in SITE.rglob("index.html"):
    h = f.read_text()
    h = h.replace('<img src="/images/logo.png" alt="Handyman Axarquia logo" width="44" height="44">', '<span class="logoimg"></span>')
    h = h.replace('<img src="/images/logo.png" alt="Handyman Axarquia">', '<span class="logoimg"></span>')
    h = h.replace('<img class="mark" src="/images/logo_mark.svg" alt="">', '<span class="mark markbg"></span>')
    h = re.sub(r'<link rel="(icon|apple-touch-icon)[^>]*>\n?', "", h)
    h = h.replace('="/wp-content/', '="https://handymanaxarquia.com/wp-content/')
    h = re.sub(r'(href|src|action|value)="/(?!/)', rf'\1="{PREFIX}/', h)
    h = h.replace("<title>", '<meta name="robots" content="noindex, nofollow">\n<title>', 1)
    h = re.sub(r"\n\s+", "\n", h)
    dest = OUT / f.relative_to(SITE)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(h)
(OUT / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
(OUT / ".nojekyll").write_text("")
print("test build ready:", sum(1 for _ in OUT.rglob("*") if _.is_file()), "files")
