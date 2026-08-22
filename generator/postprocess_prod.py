#!/usr/bin/env python3
"""Post-process the built site into the PRODUCTION bundle (prod_build/) for the
real domain: no path prefix, no noindex, indexable robots.txt/sitemap, and real
favicon/apple-touch-icon files generated from the logo so the <link> tags in
<head> actually resolve. Mirrors postprocess_test.py's asset generation
(brand pack, QR codes, mobile fixes) but skips the GitHub-Pages-subpath-only
rewriting that script does."""
import shutil
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = ROOT / "prod_build"

shutil.rmtree(OUT, ignore_errors=True)

# generate the /brand/ marketing pack, QR codes and mobile-fit fixes into site/
import brand_pack
brand_pack.build(SITE)
import qr_fix
qr_fix.ensure(SITE)
import mobile_fix
mobile_fix.apply(SITE)

# real favicon / apple-touch-icon from the logo (postprocess_test.py strips the
# <link> tags referencing these because they don't exist yet at that point)
logo_path = SITE / "images/logo.png"
if logo_path.exists():
    logo = Image.open(logo_path).convert("RGBA")
    logo.resize((32, 32), Image.LANCZOS).save(SITE / "images/favicon.png", "PNG", optimize=True)
    logo.resize((180, 180), Image.LANCZOS).save(SITE / "images/apple-touch-icon.png", "PNG", optimize=True)

# copy the whole built site as-is — build.py already writes root-relative
# absolute paths, correct canonical/hreflang URLs, sitemap.xml and an
# indexable robots.txt, so no rewriting is needed for the real domain.
shutil.copytree(SITE, OUT)
(OUT / ".nojekyll").write_text("")

print("production build ready:", sum(1 for _ in OUT.rglob("*") if _.is_file()), "files")
