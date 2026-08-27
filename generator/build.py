#!/usr/bin/env python3
"""Static site generator for handymanaxarquia.com (EN + SV)."""
import base64, json, shutil
from pathlib import Path

GEN = Path(__file__).parent
SITE = GEN.parent / "site"
BASE_URL = "https://handymanaxarquia.com"

# Decode the logo / logo-mark from the base64 sources checked into git. This
# must happen before anything below is imported: slider_gallery.py opens
# site/images/logo.png at *import time*, so on a brand-new clone (where
# site/images/ doesn't exist yet) that import would otherwise crash.
ASSETS_B64 = GEN.parent / "assets_b64"
(SITE / "images").mkdir(parents=True, exist_ok=True)
for _b64name, _outname in [("logo160.png.b64", "logo.png"), ("logo_mark.svg.b64", "logo_mark.svg")]:
    _b64path = ASSETS_B64 / _b64name
    if _b64path.exists():
        (SITE / "images" / _outname).write_bytes(base64.b64decode(_b64path.read_text()))

# Decode the before/after gallery photos into site/wp-content/uploads/... —
# the same paths the old WordPress site served them from, so the URLs in
# GALLERY_PAIRS (and any old links/Google image results) keep working on the
# static deployment. Filenames use "__" for "/": 2024__02__foo.webp.b64 →
# wp-content/uploads/2024/02/foo.webp. Larger photos are split into
# foo.webp.b64.part01/.part02/... (they were pushed through an API with a
# per-file size cap) — concatenate the parts in name order before decoding.
_gallery = {}
for _b64path in sorted((ASSETS_B64 / "gallery").glob("*.b64*")):
    _base = _b64path.name.split(".b64")[0] + ".b64"
    _gallery.setdefault(_base, []).append(_b64path)
for _base, _paths in _gallery.items():
    _text = "".join(p.read_text().strip() for p in sorted(_paths, key=lambda p: p.name))
    _rel = _base[:-len(".b64")].replace("__", "/")
    _out = SITE / "wp-content" / "uploads" / _rel
    _out.parent.mkdir(parents=True, exist_ok=True)
    _out.write_bytes(base64.b64decode(_text))

from content_en import PAGES as EN, UI as UI_EN
from content_sv import PAGES as SV, UI as UI_SV

try:
    from slider_gallery import gallery_body_slider
    EN["gallery"]["body"] = gallery_body_slider
    SV["gallery"]["body"] = gallery_body_slider
except ImportError:
    pass

WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.52.149-.174.198-.298.297-.497.1-.198.05-.371-.025-.52-.074-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'

SERVICE_ORDER = ["reforms", "plastering", "extensions", "tiling", "bathrooms", "kitchens"]

def slug_to_url(lang, slug):
    if lang == "en":
        return "/" if slug == "home" else f"/{slug}/"
    m = {p["key"]: p["slug"] for p in SV.values()}
    return "/sv/" if slug == "home" else f"/sv/{m[slug]}/"

def counterpart(lang, key):
    return slug_to_url("sv" if lang == "en" else "en", key)

def head(lang, page, ui):
    url = BASE_URL + slug_to_url(lang, page["key"])
    alt = BASE_URL + counterpart(lang, page["key"])
    css = "/css/style.css"
    schema = {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "name": "Handyman Axarquia",
        "image": BASE_URL + "/images/logo.png",
        "url": BASE_URL,
        "telephone": "+34711027432",
        "email": "info@handymanaxarquia.com",
        "priceRange": "€€",
        "address": {"@type": "PostalAddress", "streetAddress": "Los Toscanos 33, Almayate Bajo",
                    "addressLocality": "Vélez-Málaga", "addressRegion": "Málaga",
                    "postalCode": "29749", "addressCountry": "ES"},
        "geo": {"@type": "GeoCoordinates", "latitude": 36.7386, "longitude": -4.1200},
        "areaServed": ["Torre del Mar", "Vélez-Málaga", "Algarrobo", "Caleta de Vélez", "Almayate",
                       "Nerja", "Torrox", "Frigiliana", "Cómpeta", "Viñuela",
                       "Rincón de la Victoria", "Axarquía", "Costa del Sol"],
        "openingHours": "Mo-Fr 08:00-20:00",
        "sameAs": ["https://www.facebook.com/handymanaxarquia"]
    }
    blocks = [f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>']
    if page.get("faqs"):
        faq_schema = {
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in page["faqs"]]
        }
        blocks.append(f'<script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script>')
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page["title"]}</title>
<meta name="description" content="{page["desc"]}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{BASE_URL + slug_to_url('en', page['key'])}">
<link rel="alternate" hreflang="sv" href="{BASE_URL + slug_to_url('sv', page['key'])}">
<link rel="alternate" hreflang="x-default" href="{BASE_URL + slug_to_url('en', page['key'])}">
<meta property="og:type" content="website">
<meta property="og:title" content="{page["title"]}">
<meta property="og:description" content="{page["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE_URL}/images/logo.png">
<link rel="icon" type="image/png" href="/images/favicon.png">
<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
{''.join(blocks)}
</head>"""

def header(lang, page, ui):
    def u(k): return slug_to_url(lang, k)
    active = page["key"]
    links = "".join(
        f'<a href="{u(k)}">{ui["services_names"][k]}</a>' for k in SERVICE_ORDER)
    return f"""<body>
<header class="site-head">
  <div class="bar">
    <a class="brand" href="{u('home')}">
      <img src="/images/logo.png" alt="Handyman Axarquia logo" width="44" height="44">
      <div class="t">HANDYMAN <span>AXARQUIA</span></div>
    </a>
    <button class="burger" aria-label="Menu" onclick="document.querySelector('nav.main').classList.toggle('open')">
      <span></span><span></span><span></span>
    </button>
    <nav class="main">
      <a href="{u('home')}"{' class="active"' if active=='home' else ''}>{ui["nav_home"]}</a>
      <div class="dropdown">
        <a href="{u('reforms')}"{' class="active"' if active in SERVICE_ORDER else ''}>{ui["nav_services"]}</a>
        <div class="menu">{links}</div>
      </div>
      <a href="{u('gallery')}"{' class="active"' if active=='gallery' else ''}>{ui["nav_gallery"]}</a>
      <a href="{u('contact')}"{' class="active"' if active=='contact' else ''}>{ui["nav_contact"]}</a>
      <div class="lang">
        <a href="{slug_to_url('en', page['key'])}" class="{'on' if lang=='en' else ''}">EN</a>
        <a href="{slug_to_url('sv', page['key'])}" class="{'on' if lang=='sv' else ''}">SV</a>
      </div>
      <a class="cta-call" href="tel:+34711027432">✆ +34 711 027 432</a>
    </nav>
  </div>
</header>"""

def footer(lang, ui):
    def u(k): return slug_to_url(lang, k)
    slinks = "".join(f'<a href="{u(k)}">{ui["services_names"][k]}</a>' for k in SERVICE_ORDER)
    return f"""<footer class="site-foot">
  <div class="cols">
    <div>
      <div class="brandline">
        <img src="/images/logo.png" alt="Handyman Axarquia">
        <b style="color:#fff">HANDYMAN <span style="color:var(--orange)">AXARQUIA</span></b>
      </div>
      <p>{ui["foot_blurb"]}</p>
      <p style="font-size:.8rem;color:#8E8E93;margin-top:10px">{ui["foot_areas"]}</p>
    </div>
    <div>
      <h4>{ui["nav_services"]}</h4>
      {slinks}
    </div>
    <div>
      <h4>{ui["foot_pages"]}</h4>
      <a href="{u('home')}">{ui["nav_home"]}</a>
      <a href="{u('gallery')}">{ui["nav_gallery"]}</a>
      <a href="{u('contact')}">{ui["nav_contact"]}</a>
    </div>
    <div>
      <h4>{ui["nav_contact"]}</h4>
      <a href="tel:+34711027432">+34 711 027 432</a>
      <a href="mailto:info@handymanaxarquia.com">info@handymanaxarquia.com</a>
      <p style="margin-top:8px">Los Toscanos 33, Almayate Bajo<br>29749 Málaga, {ui["spain"]}</p>
    </div>
  </div>
  <div class="base">© Handyman Axarquia · {ui["foot_rights"]}</div>
</footer>
<a class="wa-float" href="https://wa.me/34711027432" aria-label="WhatsApp">{WA_SVG}</a>
</body>
</html>"""

def render(lang, page, ui):
    return head(lang, page, ui) + header(lang, page, ui) + page["body"](lang, ui) + footer(lang, ui)

def write(lang, page, ui):
    url = slug_to_url(lang, page["key"])
    out = SITE / url.strip("/") / "index.html" if url != "/" else SITE / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(lang, page, ui))
    return url

def sitemap(urls):
    entries = "\n".join(
        f"  <url><loc>{BASE_URL}{u}</loc><changefreq>monthly</changefreq></url>" for u in urls)
    (SITE / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n')
    # Allow-all for every crawler, plus explicit named allows for the major AI
    # answer-engine/search bots so intent is unambiguous if rules are ever tightened.
    ai_bots = ["GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-User",
               "Claude-Web", "anthropic-ai", "PerplexityBot", "Perplexity-User",
               "Google-Extended", "Applebot-Extended", "CCBot", "Bytespider", "Amazonbot"]
    bot_blocks = "\n".join(f"User-agent: {b}\nAllow: /\n" for b in ai_bots)
    (SITE / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\n{bot_blocks}\nSitemap: {BASE_URL}/sitemap.xml\n")

def llms_txt():
    """llms.txt (llmstxt.org convention) — a plain-language summary AI agents/answer
    engines can read directly instead of scraping the rendered HTML."""
    (SITE / "llms.txt").write_text(f"""# Handyman Axarquia

> Professional building, reform and property-care company based in Almayate, on the eastern Costa del Sol, Spain. Family-run, 25+ years experience, English and Swedish spoken. Free itemised written quotes, 12-month workmanship guarantee, 50% deposit to book with balance on completion.

## Services
- Reforms & renovations (full and partial): {BASE_URL}/reforms/
- Plastering & rendering: {BASE_URL}/plastering/
- Extensions: {BASE_URL}/extensions/
- Tiling: {BASE_URL}/tiling/
- Bathroom renovations: {BASE_URL}/bathrooms/
- Kitchen renovations: {BASE_URL}/kitchens/

## Areas served
Torre del Mar, Vélez-Málaga, Algarrobo, Caleta de Vélez, Almayate, Nerja, Torrox, Frigiliana, Cómpeta, Viñuela, Rincón de la Victoria, and the wider Axarquía region and villages, Costa del Sol, Málaga, Spain.

## Contact
- Phone / WhatsApp: +34 711 027 432
- Email: info@handymanaxarquia.com
- Address: Los Toscanos 33, Almayate Bajo, 29749 Málaga, Spain
- Hours: Mon–Fri 08:00–20:00

## More
- Homepage: {BASE_URL}/
- Before & after project gallery: {BASE_URL}/gallery/
- Contact / free quote: {BASE_URL}/contact/
- Swedish-language site: {BASE_URL}/sv/
""")

if __name__ == "__main__":
    urls = []
    for key, page in EN.items():
        urls.append(write("en", page, UI_EN))
    for key, page in SV.items():
        urls.append(write("sv", page, UI_SV))
    sitemap(urls)
    llms_txt()
    print(f"Built {len(urls)} pages")
    for u in sorted(urls):
        print(" ", u)
