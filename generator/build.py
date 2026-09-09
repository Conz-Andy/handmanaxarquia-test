#!/usr/bin/env python3
"""Static site generator for handymanaxarquia.com (EN + SV)."""
import base64, json, shutil, datetime, html as _html
from pathlib import Path

GEN = Path(__file__).parent
SITE = GEN.parent / "site"
BASE_URL = "https://handymanaxarquia.com"
TODAY = datetime.date.today().isoformat()

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
from reviews import reviews_html, FACEBOOK_URL, FB_SVG, GOOGLE_REVIEWS_URL
from helpers import aside_card, faq_section, cta_band
from areas import AREAS, AREA_ORDER
from blog_posts import POSTS, AUTHOR
import social_image

# UI strings for the pages added by this generator (areas + blog), kept here
# so content_en.py / content_sv.py stay untouched.
UI_EN.update({
    "nav_blog": "Blog", "nav_areas": "Areas",
    "areas_title": "Areas we cover", "areas_blurb": "Local pages for the towns and villages we work in most.",
    "blog_title": "Blog — advice for property owners in the Axarquia",
    "blog_home_h2": "Advice for property owners in the Axarquia",
    "blog_lead": "Straight answers on reforms, licences, damp, costs and looking after a home on the eastern Costa del Sol — from a builder who has been here over 35 years.",
    "blog_read": "Read article", "blog_by": "By", "blog_more": "More from the blog", "blog_back": "All articles",
    "areas_nearby": "Other areas we cover",
})
UI_SV.update({
    "nav_blog": "Blogg", "nav_areas": "Områden",
    "areas_title": "Områden vi täcker", "areas_blurb": "Lokala sidor för de orter och byar där vi arbetar mest.",
    "blog_title": "Blogg — råd för bostadsägare i Axarquía",
    "blog_home_h2": "Råd för bostadsägare i Axarquía",
    "blog_lead": "Raka svar om renovering, bygglov, fukt, kostnader och skötsel av en bostad på östra Costa del Sol — från en byggare som varit här i över 35 år.",
    "blog_read": "Läs artikeln", "blog_by": "Av", "blog_more": "Mer från bloggen", "blog_back": "Alla artiklar",
    "areas_nearby": "Andra områden vi täcker",
})
# Shorter home <title> / description (the originals were 75 / 202 characters
# and were being truncated in search results).
EN["home"]["title"] = "Builders & Reforms in the Axarquia, Costa del Sol | Handyman Axarquia"
EN["home"]["desc"] = "Reforms, extensions, plastering, tiling, bathroom & kitchen renovations in Torre del Mar, Vélez-Málaga, Nerja, Torrox and Rincón de la Victoria. 35+ years, free written quotes."
SV["home"]["title"] = "Svensktalande byggfirma i Axarquía, Costa del Sol | Handyman Axarquia"
SV["home"]["desc"] = "Renovering, tillbyggnad, puts, kakel, badrum och kök i Torre del Mar, Nerja, Torrox, Rincón de la Victoria och hela Axarquía. 35+ års erfarenhet, kostnadsfri offert. Vi talar svenska."

try:
    from slider_gallery import gallery_body_slider
    EN["gallery"]["body"] = gallery_body_slider
    SV["gallery"]["body"] = gallery_body_slider
except ImportError:
    pass

WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.52.149-.174.198-.298.297-.497.1-.198.05-.371-.025-.52-.074-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'

SERVICE_ORDER = ["reforms", "plastering", "extensions", "tiling", "bathrooms", "kitchens"]

# A representative "after" photo for each service page (shown next to the
# intro and used as that page's og:image).
SERVICE_IMAGES = {
    "reforms":    ("/wp-content/uploads/2026/08/handyman-axarquia-courtyard-lighting-after.webp", "Courtyard reform with lighting and glass floor — after"),
    "plastering": ("/wp-content/uploads/2024/02/axarquia-handyman-reform-garden-wall-repair-render-repaint-after.webp", "Garden wall repaired, re-rendered and repainted — after"),
    "extensions": ("/wp-content/uploads/2026/08/handyman-axarquia-pergola-vinuela-after.webp", "New pergola and printed-concrete driveway, Viñuela — after"),
    "tiling":     ("/wp-content/uploads/2026/08/handyman-axarquia-terrace-planters-after.webp", "Roof terrace re-tiled with decorative tiles and planters — after"),
    "bathrooms":  ("/wp-content/uploads/2026/08/handyman-axarquia-bathroom-reform-1-after.webp", "Complete bathroom renovation — after"),
    "kitchens":   ("/wp-content/uploads/2026/08/handyman-axarquia-kitchen-reform-open-after.webp", "Open-plan kitchen reform — after"),
}

# --------------------------------------------------------------------- URLs

def slug_to_url(lang, slug):
    if lang == "en":
        return "/" if slug == "home" else f"/{slug}/"
    m = {p["key"]: p["slug"] for p in SV.values()}
    return "/sv/" if slug == "home" else f"/sv/{m[slug]}/"

def area_url(lang, key):
    return f"/areas/{key}/" if lang == "en" else f"/sv/omraden/{AREAS[key]['slug_sv']}/"

def areas_index_url(lang):
    return "/areas/" if lang == "en" else "/sv/omraden/"

def post_url(lang, post):
    return f"/blog/{post['slug']}/" if lang == "en" else f"/sv/blogg/{post['slug_sv']}/"

def blog_index_url(lang):
    return "/blog/" if lang == "en" else "/sv/blogg/"

def other(lang):
    return "sv" if lang == "en" else "en"

# ------------------------------------------------------------------- schema

def business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": BASE_URL + "/#business",
        "name": "Handyman Axarquia",
        "alternateName": "Handyman Axarquía",
        "description": "Family-run building, reform and property-care company on the eastern Costa del Sol: reforms, extensions, plastering & rendering, tiling, bathroom and kitchen renovations. English and Swedish spoken.",
        "image": BASE_URL + "/images/og-default.jpg",
        "logo": BASE_URL + "/images/logo.png",
        "url": BASE_URL,
        "telephone": "+34711027432",
        "email": "info@handymanaxarquia.com",
        "priceRange": "€€",
        "currenciesAccepted": "EUR",
        "foundingDate": "1990",
        "knowsLanguage": ["en", "sv", "es"],
        "address": {"@type": "PostalAddress", "streetAddress": "Los Toscanos 33, Almayate Bajo",
                    "addressLocality": "Vélez-Málaga", "addressRegion": "Málaga",
                    "postalCode": "29749", "addressCountry": "ES"},
        "geo": {"@type": "GeoCoordinates", "latitude": 36.7386, "longitude": -4.1200},
        "hasMap": "https://www.google.com/maps/search/?api=1&query=Handyman+Axarquia+Almayate",
        "areaServed": [{"@type": "City", "name": n} for n in
                       ["Torre del Mar", "Vélez-Málaga", "Algarrobo", "Caleta de Vélez", "Almayate",
                        "Nerja", "Torrox", "Frigiliana", "Viñuela",
                        "Rincón de la Victoria", "La Cala del Moral", "Benajarafe"]] +
                      [{"@type": "AdministrativeArea", "name": "Axarquía"}, {"@type": "Place", "name": "Costa del Sol"}],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                       "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                       "opens": "08:00", "closes": "20:00"}],
        "sameAs": [FACEBOOK_URL, GOOGLE_REVIEWS_URL],
        "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": BASE_URL + slug_to_url("en", k)}}
                       for k, n in UI_EN["services_names"].items()],
    }

def breadcrumb_schema(items):
    """items: list of (name, url) from home to current page."""
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BASE_URL + u}
                                for i, (n, u) in enumerate(items)]}

# --------------------------------------------------------------------- head

def head(lang, title, desc, url, alt_url, extra_schema=(), og_image=None, og_type="website", noindex=False):
    en_url = url if lang == "en" else alt_url
    sv_url = alt_url if lang == "en" else url
    og_image = og_image or "/images/og-default.jpg"
    if og_image.endswith(".webp") and not og_image.startswith("http"):
        og_image = social_image.og_for(SITE, og_image)  # 1200x630 JPEG variant
    blocks = [f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
              for s in (business_schema(), *extra_schema)]
    robots = '<meta name="robots" content="noindex,nofollow">' if noindex else ''
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{_html.escape(desc, quote=True)}">
{robots}<link rel="canonical" href="{BASE_URL + url}">
<link rel="alternate" hreflang="en" href="{BASE_URL + en_url}">
<link rel="alternate" hreflang="sv" href="{BASE_URL + sv_url}">
<link rel="alternate" hreflang="x-default" href="{BASE_URL + en_url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Handyman Axarquia">
<meta property="og:locale" content="{'en_GB' if lang == 'en' else 'sv_SE'}">
<meta property="og:title" content="{_html.escape(title, quote=True)}">
<meta property="og:description" content="{_html.escape(desc, quote=True)}">
<meta property="og:url" content="{BASE_URL + url}">
<meta property="og:image" content="{BASE_URL + og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/images/favicon.png">
<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
<link rel="stylesheet" href="/css/seo.css">
{''.join(blocks)}
</head>"""

# ------------------------------------------------------------- header/footer

def header(lang, ui, active, url_en, url_sv):
    def u(k): return slug_to_url(lang, k)
    links = "".join(f'<a href="{u(k)}">{ui["services_names"][k]}</a>' for k in SERVICE_ORDER)
    alinks = "".join(f'<a href="{area_url(lang, k)}">{AREAS[k]["name"]}</a>' for k in AREA_ORDER)
    def cls(k): return ' class="active"' if active == k else ''
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
      <a href="{u('home')}"{cls('home')}>{ui["nav_home"]}</a>
      <div class="dropdown">
        <a href="{u('reforms')}"{' class="active"' if active in SERVICE_ORDER else ''}>{ui["nav_services"]}</a>
        <div class="menu">{links}</div>
      </div>
      <div class="dropdown">
        <a href="{areas_index_url(lang)}"{cls('areas')}>{ui["nav_areas"]}</a>
        <div class="menu">{alinks}</div>
      </div>
      <a href="{u('gallery')}"{cls('gallery')}>{ui["nav_gallery"]}</a>
      <a href="{blog_index_url(lang)}"{cls('blog')}>{ui["nav_blog"]}</a>
      <a href="{u('contact')}"{cls('contact')}>{ui["nav_contact"]}</a>
      <div class="lang">
        <a href="{url_en}" class="{'on' if lang=='en' else ''}" hreflang="en">EN</a>
        <a href="{url_sv}" class="{'on' if lang=='sv' else ''}" hreflang="sv">SV</a>
      </div>
      <a class="fb-head" href="{FACEBOOK_URL}" target="_blank" rel="noopener" aria-label="Handyman Axarquia on Facebook"><svg viewBox="0 0 320 512" aria-hidden="true"><path d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"/></svg></a>
      <a class="cta-call" href="tel:+34711027432">✆ +34 711 027 432</a>
    </nav>
  </div>
</header>"""

def footer(lang, ui):
    def u(k): return slug_to_url(lang, k)
    slinks = "".join(f'<a href="{u(k)}">{ui["services_names"][k]}</a>' for k in SERVICE_ORDER)
    alinks = "".join(f'<a href="{area_url(lang, k)}">{AREAS[k]["name"]}</a>' for k in AREA_ORDER)
    return f"""<footer class="site-foot">
  <div class="cols">
    <div>
      <div class="brandline">
        <img src="/images/logo.png" alt="Handyman Axarquia" width="36" height="36">
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
      <h4>{ui["nav_areas"]}</h4>
      {alinks}
    </div>
    <div>
      <h4>{ui["foot_pages"]}</h4>
      <a href="{u('home')}">{ui["nav_home"]}</a>
      <a href="{u('gallery')}">{ui["nav_gallery"]}</a>
      <a href="{blog_index_url(lang)}">{ui["nav_blog"]}</a>
      <a href="{u('contact')}">{ui["nav_contact"]}</a>
      <a href="tel:+34711027432">+34 711 027 432</a>
      <a href="mailto:info@handymanaxarquia.com">info@handymanaxarquia.com</a>
      <a href="{FACEBOOK_URL}" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:8px"><span style="display:inline-flex;width:15px;height:15px;color:#1877F2">{FB_SVG}</span>Facebook</a>
      <p style="margin-top:8px">Los Toscanos 33, Almayate Bajo<br>29749 Málaga, {ui["spain"]}</p>
    </div>
  </div>
  <div class="base">© Handyman Axarquia · {ui["foot_rights"]}</div>
</footer>
<a class="wa-float" href="https://wa.me/34711027432" aria-label="WhatsApp">{WA_SVG}</a>
</body>
</html>"""

# ---------------------------------------------------------------- writing

def write_page(url, html):
    out = SITE / url.strip("/") / "index.html" if url != "/" else SITE / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    return url

def service_photo(key, lang):
    src, alt = SERVICE_IMAGES[key]
    w, h = social_image.dims(SITE, src)
    return f'<figure class="svc-photo"><img src="{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy"><figcaption>{alt}</figcaption></figure>'

def render_core(lang, page, ui):
    """Home / service / gallery / contact pages (the original site)."""
    key = page["key"]
    url = slug_to_url(lang, key)
    alt = slug_to_url(other(lang), key)
    body = page["body"](lang, ui)
    schemas = []
    og = None
    if key in SERVICE_ORDER:
        # add a real project photo after the intro on service pages
        body = body.replace('<div class="prose">', '<div class="prose">' + service_photo(key, lang), 1)
        schemas.append(breadcrumb_schema([(ui["nav_home"], slug_to_url(lang, "home")),
                                          (ui["nav_services"], slug_to_url(lang, "reforms")),
                                          (ui["services_names"][key], url)]))
        schemas.append({"@context": "https://schema.org", "@type": "Service",
                        "name": ui["services_names"][key], "url": BASE_URL + url,
                        "provider": {"@id": BASE_URL + "/#business"},
                        "areaServed": {"@type": "AdministrativeArea", "name": "Axarquía, Málaga"},
                        "description": page["desc"]})
        og = SERVICE_IMAGES[key][0]
    if page.get("faqs"):
        schemas.append({"@context": "https://schema.org", "@type": "FAQPage",
                        "mainEntity": [{"@type": "Question", "name": q,
                                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in page["faqs"]]})
    if key in ("home", "gallery"):
        body += reviews_html(lang, ui)
    if key == "home":
        # area chips inside the "where we work" section, latest articles after it
        anchor = "    </ul>\n  </div>\n</div></section>\n"
        body = body.replace(anchor, "    </ul>\n    " + areas_strip(lang, ui) + "\n  </div>\n</div></section>\n" + blog_strip(lang, ui), 1)
    html = (head(lang, page["title"], page["desc"], url, alt, schemas, og_image=og)
            + header(lang, ui, key, slug_to_url("en", key), slug_to_url("sv", key)) + body + footer(lang, ui))
    return write_page(url, html)

# ------------------------------------------------------------- area pages

def areas_strip(lang, ui):
    cards = "".join(f'<a class="area-chip" href="{area_url(lang, k)}">{AREAS[k]["name"]}</a>' for k in AREA_ORDER)
    return f'<div class="area-chips">{cards}</div>'

def area_body(lang, ui, key):
    a = AREAS[key]; c = a[lang]
    src, alt = a["img"]
    w, h = social_image.dims(SITE, src)
    others = "".join(f'<li><a href="{area_url(lang, k)}">{AREAS[k]["name"]}</a></li>' for k in AREA_ORDER if k != key)
    def u(l, k): return slug_to_url(l, k)
    return f"""<div class="page-hero"><div class="container">
  <div class="crumbs"><a href="{u(lang,'home')}">{ui["nav_home"]}</a> / <a href="{areas_index_url(lang)}">{ui["nav_areas"]}</a> / {a["name"]}</div>
  <h1>{c["h1"]}</h1>
  <p class="lead">{c["lead"]}</p>
</div></div>
<section><div class="container split">
  <div class="prose">
    <figure class="svc-photo"><img src="{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy"><figcaption>{alt}</figcaption></figure>
    {c["prose"]}
    <h2>{ui["areas_nearby"]}</h2>
    <ul class="tick">{others}</ul>
  </div>
  {aside_card(lang, ui, u, None)}
</div></section>
{faq_section(ui, c["faqs"])}
{cta_band(lang, ui, u)}"""

def render_area(lang, ui, key):
    a = AREAS[key]; c = a[lang]
    url = area_url(lang, key); alt = area_url(other(lang), key)
    schemas = [breadcrumb_schema([(ui["nav_home"], slug_to_url(lang, "home")), (ui["nav_areas"], areas_index_url(lang)), (a["name"], url)]),
               {"@context": "https://schema.org", "@type": "FAQPage",
                "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": t}} for q, t in c["faqs"]]}]
    html = head(lang, c["title"], c["desc"], url, alt, schemas, og_image=a["img"][0]) \
        + header(lang, ui, "areas", area_url("en", key), area_url("sv", key)) + area_body(lang, ui, key) + footer(lang, ui)
    return write_page(url, html)

def render_areas_index(lang, ui):
    url = areas_index_url(lang); alt = areas_index_url(other(lang))
    en = lang == "en"
    title = ("Areas We Cover — Builders across the Axarquia | Handyman Axarquia" if en
             else "Områden vi täcker — byggfirma i hela Axarquía | Handyman Axarquia")
    desc = ("Local building and reform services in Torre del Mar, Vélez-Málaga, Nerja, Torrox, Rincón de la Victoria, Frigiliana and Viñuela. Based in Almayate, no call-out charge." if en
            else "Lokal bygg- och renoveringsservice i Torre del Mar, Vélez-Málaga, Nerja, Torrox, Rincón de la Victoria, Frigiliana och Viñuela. Bas i Almayate, ingen utkörningsavgift.")
    cards = ""
    for k in AREA_ORDER:
        a = AREAS[k]; c = a[lang]; src, ialt = a["img"]; w, h = social_image.dims(SITE, src)
        cards += f"""<a class="card area-card" href="{area_url(lang, k)}">
      <img src="{src}" alt="{ialt}" width="{w}" height="{h}" loading="lazy">
      <h3>{a["name"]}</h3>
      <p>{c["lead"]}</p>
      <span class="more">{"Read more" if en else "Läs mer"}</span>
    </a>"""
    body = f"""<div class="page-hero"><div class="container">
  <h1>{ui["areas_title"]}</h1>
  <p class="lead">{ui["areas_blurb"]}</p>
</div></div>
<section><div class="container"><div class="grid c3">{cards}</div></div></section>
{cta_band(lang, ui, lambda l, k: slug_to_url(l, k))}"""
    html = head(lang, title, desc, url, alt, [breadcrumb_schema([(ui["nav_home"], slug_to_url(lang, "home")), (ui["nav_areas"], url)])]) \
        + header(lang, ui, "areas", areas_index_url("en"), areas_index_url("sv")) + body + footer(lang, ui)
    return write_page(url, html)

# --------------------------------------------------------------- blog

def fmt_date(iso, lang):
    d = datetime.date.fromisoformat(iso)
    if lang == "en":
        return d.strftime("%-d %B %Y")
    months = ["januari", "februari", "mars", "april", "maj", "juni", "juli", "augusti", "september", "oktober", "november", "december"]
    return f"{d.day} {months[d.month - 1]} {d.year}"

def post_card(lang, ui, p):
    c = p[lang]; src, alt_en, alt_sv = p["img"]; w, h = social_image.dims(SITE, src)
    return f"""<a class="card post-card" href="{post_url(lang, p)}">
      <img src="{src}" alt="{alt_en if lang == 'en' else alt_sv}" width="{w}" height="{h}" loading="lazy">
      <div class="post-meta">{fmt_date(p["date"], lang)}</div>
      <h3>{c["title"]}</h3>
      <p>{c["excerpt"]}</p>
      <span class="more">{ui["blog_read"]}</span>
    </a>"""

def blog_strip(lang, ui):
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)[:3]
    cards = "".join(post_card(lang, ui, p) for p in posts)
    return f"""<section class="alt"><div class="container">
  <div class="sec-head"><div class="kicker">{ui["nav_blog"]}</div><h2>{ui["blog_home_h2"]}</h2></div>
  <div class="grid c3">{cards}</div>
  <p style="margin-top:22px"><a class="btn primary" href="{blog_index_url(lang)}">{ui["blog_back"]} →</a></p>
</div></section>"""

def render_blog_index(lang, ui):
    url = blog_index_url(lang); alt = blog_index_url(other(lang))
    en = lang == "en"
    title = "Blog — Reform, Building & Property Advice for the Axarquia | Handyman Axarquia" if en \
        else "Blogg — råd om renovering och bostad i Axarquía | Handyman Axarquia"
    desc = ui["blog_lead"]
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)
    cards = "".join(post_card(lang, ui, p) for p in posts)
    body = f"""<div class="page-hero"><div class="container">
  <h1>{ui["blog_title"]}</h1>
  <p class="lead">{ui["blog_lead"]}</p>
</div></div>
<section><div class="container"><div class="grid c3">{cards}</div></div></section>
{cta_band(lang, ui, lambda l, k: slug_to_url(l, k))}"""
    schemas = [breadcrumb_schema([(ui["nav_home"], slug_to_url(lang, "home")), (ui["nav_blog"], url)]),
               {"@context": "https://schema.org", "@type": "Blog", "name": ui["blog_title"], "url": BASE_URL + url,
                "publisher": {"@id": BASE_URL + "/#business"},
                "blogPost": [{"@type": "BlogPosting", "headline": p[lang]["title"], "url": BASE_URL + post_url(lang, p),
                              "datePublished": p["date"]} for p in posts]}]
    html = head(lang, title, desc, url, alt, schemas) + header(lang, ui, "blog", blog_index_url("en"), blog_index_url("sv")) + body + footer(lang, ui)
    return write_page(url, html)

def render_post(lang, ui, p):
    c = p[lang]; url = post_url(lang, p); alt = post_url(other(lang), p)
    src, alt_en, alt_sv = p["img"]; ialt = alt_en if lang == "en" else alt_sv
    w, h = social_image.dims(SITE, src)
    others = [q for q in sorted(POSTS, key=lambda q: q["date"], reverse=True) if q is not p][:3]
    more = "".join(post_card(lang, ui, q) for q in others)
    def u(l, k): return slug_to_url(l, k)
    body = f"""<div class="page-hero"><div class="container">
  <div class="crumbs"><a href="{u(lang,'home')}">{ui["nav_home"]}</a> / <a href="{blog_index_url(lang)}">{ui["nav_blog"]}</a></div>
  <h1>{c["title"]}</h1>
  <p class="post-meta lead">{fmt_date(p["date"], lang)} · {ui["blog_by"]} {AUTHOR}, Handyman Axarquia</p>
</div></div>
<section><div class="container split">
  <article class="prose post">
    <figure class="post-hero"><img src="{src}" alt="{ialt}" width="{w}" height="{h}"><figcaption>{ialt}</figcaption></figure>
    {c["body"]}
  </article>
  {aside_card(lang, ui, u, None)}
</div></section>
<section class="alt"><div class="container">
  <div class="sec-head"><div class="kicker">{ui["nav_blog"]}</div><h2>{ui["blog_more"]}</h2></div>
  <div class="grid c3">{more}</div>
  <p style="margin-top:22px"><a href="{blog_index_url(lang)}">← {ui["blog_back"]}</a></p>
</div></section>
{cta_band(lang, ui, u)}"""
    schemas = [breadcrumb_schema([(ui["nav_home"], u(lang, "home")), (ui["nav_blog"], blog_index_url(lang)), (c["title"], url)]),
               {"@context": "https://schema.org", "@type": "BlogPosting",
                "headline": c["title"], "description": c["desc"], "url": BASE_URL + url,
                "mainEntityOfPage": BASE_URL + url, "inLanguage": lang,
                "image": BASE_URL + social_image.og_for(SITE, src),
                "datePublished": p["date"], "dateModified": p.get("updated", p["date"]),
                "author": {"@type": "Person", "name": AUTHOR, "jobTitle": "Builder", "worksFor": {"@id": BASE_URL + "/#business"}},
                "publisher": {"@id": BASE_URL + "/#business"}}]
    html = head(lang, c["meta_title"], c["desc"], url, alt, schemas, og_image=src, og_type="article") \
        + header(lang, ui, "blog", post_url("en", p), post_url("sv", p)) + body + footer(lang, ui)
    return write_page(url, html)

# ----------------------------------------------------- sitemap / robots etc.

def sitemap(urls):
    entries = "\n".join(
        f"  <url><loc>{BASE_URL}{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
    (SITE / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n')
    # Allow-all for every crawler, plus explicit named allows for the major AI
    # answer-engine/search bots so intent is unambiguous if rules are ever tightened.
    ai_bots = ["GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-User",
               "Claude-Web", "anthropic-ai", "PerplexityBot", "Perplexity-User",
               "Google-Extended", "Applebot-Extended", "CCBot", "Bytespider", "Amazonbot"]
    bot_blocks = "\n".join(f"User-agent: {b}\nAllow: /\nDisallow: /brand/\n" for b in ai_bots)
    (SITE / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nDisallow: /brand/\n\n{bot_blocks}\nSitemap: {BASE_URL}/sitemap.xml\n")

def redirects():
    """Old WordPress URLs (still crawled by Google, see Search Console) → new pages.
    Cloudflare Workers static assets honours a _redirects file in the assets dir."""
    rules = [
        ("/handyman-axarquia-gallery/", "/gallery/", 301),
        ("/handyman-axarquia-gallery", "/gallery/", 301),
        ("/services/", "/reforms/", 301),
        ("/services", "/reforms/", 301),
        ("/our-services/", "/reforms/", 301),
        ("/about/", "/", 301),
        ("/about-us/", "/", 301),
        ("/contact-us/", "/contact/", 301),
        ("/feed/", "/", 301),
        ("/feed", "/", 301),
        ("/2021/09/18/hello-world/", "/blog/", 301),
        ("/wp-json/*", "/", 301),
        ("/wp-admin/*", "/", 301),
        ("/wp-includes/*", "/", 301),
        ("/wp-content/plugins/*", "/", 301),
        ("/wp-content/themes/*", "/", 301),
        ("/home/*", "/", 301),
    ]
    (SITE / "_redirects").write_text("".join(f"{a} {b} {c}\n" for a, b, c in rules))
    (SITE / "_headers").write_text("""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
/wp-content/uploads/*
  Cache-Control: public, max-age=31536000, immutable
/images/*
  Cache-Control: public, max-age=2592000
/css/*
  Cache-Control: public, max-age=604800
/brand/*
  X-Robots-Tag: noindex, nofollow
""")

def llms_txt(post_lines):
    """llms.txt (llmstxt.org convention) — a plain-language summary AI agents/answer
    engines can read directly instead of scraping the rendered HTML."""
    areas = "\n".join(f"- {AREAS[k]['name']}: {BASE_URL}{area_url('en', k)}" for k in AREA_ORDER)
    (SITE / "llms.txt").write_text(f"""# Handyman Axarquia

> Professional building, reform and property-care company based in Almayate, on the eastern Costa del Sol, Spain. Family-run, 35+ years experience, English and Swedish spoken. Free written quotes, 12-month workmanship guarantee, 50% deposit to book with balance on completion. 5.0 rating on Google.

## Services
- Reforms & renovations (full and partial): {BASE_URL}/reforms/
- Plastering & rendering (incl. damp repairs, gotelé removal): {BASE_URL}/plastering/
- Extensions, pergolas, garage conversions: {BASE_URL}/extensions/
- Tiling & terrace waterproofing: {BASE_URL}/tiling/
- Bathroom renovations: {BASE_URL}/bathrooms/
- Kitchen renovations: {BASE_URL}/kitchens/

## Areas served (local pages)
{areas}
Also Algarrobo, Caleta de Vélez, Almayate, Viñuela, Sayalonga, Benajarafe, La Cala del Moral and the wider Axarquía region, Costa del Sol, Málaga, Spain.

## Blog (advice for owners)
{post_lines}

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
    shutil.copy(GEN / "seo.css", SITE / "css" / "seo.css")
    social_image.build_default(SITE)
    urls = []
    for lang, PAGES, UI in (("en", EN, UI_EN), ("sv", SV, UI_SV)):
        for key, page in PAGES.items():
            urls.append(render_core(lang, page, UI))
        urls.append(render_areas_index(lang, UI))
        for k in AREA_ORDER:
            urls.append(render_area(lang, UI, k))
        urls.append(render_blog_index(lang, UI))
        for p in POSTS:
            urls.append(render_post(lang, UI, p))
    sitemap(urls)
    redirects()
    llms_txt("\n".join(f"- {p['en']['title']}: {BASE_URL}{post_url('en', p)}" for p in POSTS))
    print(f"Built {len(urls)} pages")
    for u in sorted(urls):
        print(" ", u)
