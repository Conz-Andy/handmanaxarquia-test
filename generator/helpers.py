"""Shared page-body builders for the Handyman Axarquia site."""

SERVICE_ORDER = ["reforms", "plastering", "extensions", "tiling", "bathrooms", "kitchens"]

def _u(lang, key, sv_slugs):
    if lang == "en":
        return "/" if key == "home" else f"/{key}/"
    return "/sv/" if key == "home" else f"/sv/{sv_slugs[key]}/"

def make_url_fn(sv_slugs):
    def u(lang, key):
        return _u(lang, key, sv_slugs)
    return u

def aside_card(lang, ui, u, current):
    links = "".join(
        f'<li><a href="{u(lang, k)}">{ui["services_names"][k]}</a></li>'
        for k in SERVICE_ORDER if k != current)
    return f"""<div class="aside-card">
  <h3>{ui["aside_title"]}</h3>
  <p>{ui["aside_blurb"]}</p>
  <a class="btn primary" href="https://wa.me/34711027432">{ui["aside_wa"]}</a>
  <a class="btn ghost" href="tel:+34711027432">+34 711 027 432</a>
  <p class="small" style="margin-top:12px">{ui["aside_terms"]}</p>
  <ul class="links">{links}</ul>
</div>"""

def faq_section(ui, faqs):
    if not faqs:
        return ""
    items = "".join(
        f'<details><summary>{q}</summary><div class="a"><p>{a}</p></div></details>'
        for q, a in faqs)
    return f"""<section class="alt"><div class="container">
  <div class="sec-head"><div class="kicker">FAQ</div><h2>{ui["faq_title"]}</h2></div>
  <div class="faq" style="max-width:760px">{items}</div>
</div></section>"""

def cta_band(lang, ui, u):
    return f"""<section class="cta-band"><div class="container">
  <h2>{ui["cta_h"]}</h2>
  <p>{ui["cta_p"]}</p>
  <div class="actions" style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
    <a class="btn primary" href="{u(lang,'contact')}">{ui["cta_btn"]}</a>
    <a class="btn ghost" href="https://wa.me/34711027432">WhatsApp</a>
  </div>
</div></section>"""

def service_body(page, u):
    """Standard service-page layout."""
    def body(lang, ui):
        return f"""<div class="page-hero"><div class="container">
  <div class="crumbs"><a href="{u(lang,'home')}">{ui["nav_home"]}</a> / {ui["nav_services"]} / {ui["services_names"][page["key"]]}</div>
  <h1>{page["h1"]}</h1>
  <p class="lead">{page["lead"]}</p>
</div></div>
<section><div class="container split">
  <div class="prose">{page["prose"]}</div>
  {aside_card(lang, ui, u, page["key"])}
</div></section>
{faq_section(ui, page.get("faqs"))}
{cta_band(lang, ui, u)}"""
    return body
