"""Cookie consent + remarketing tags (Google Ads, Meta Pixel) for handymanaxarquia.com.

HOW TO SWITCH IT ON
  Fill in the IDs below and push to main. Leave an ID empty ("") to switch that
  platform off. While BOTH are empty no banner is shown and nothing is loaded.

  GOOGLE_ADS_ID   Google Ads > Tools > Data manager > Google tag. Looks like "AW-123456789".
  GOOGLE_ADS_LEAD Optional. Conversion label for "lead" (call / WhatsApp / form),
                  the part after the slash in "AW-123456789/AbCdEfGh". Leave "" if unsure.
  META_PIXEL_ID   Meta Events Manager > Data sources > your Pixel. A long number.

LEGAL DETAILS shown on the privacy page (Spanish LSSI asks for the owner's name and NIF).
  Leave "" to hide the line.

How it works (GDPR / Spanish AEPD guidance):
  * Google Consent Mode v2 defaults: everything denied.
  * Nothing from Google Ads or Meta is loaded until the visitor clicks Accept
    ("basic" consent mode), so visitors who reject send nothing at all.
  * Accept and Reject are equal buttons on the first screen; the choice is kept
    for 12 months; "Cookie settings" in the footer reopens the banner.
"""
import html as _html
from pathlib import Path

GOOGLE_ADS_ID = "AW-18595997597"
GOOGLE_ADS_LEAD = ""
META_PIXEL_ID = ""

LEGAL_NAME = "Nicholas Britton"
LEGAL_NIF = "Y0163759J"


def enabled():
    return bool(GOOGLE_ADS_ID or META_PIXEL_ID)


# ------------------------------------------------------------------ <head>

def head_snippet():
    if not enabled():
        return ""
    cfg = '{gads:"%s",lead:"%s",pixel:"%s"}' % (GOOGLE_ADS_ID, GOOGLE_ADS_LEAD, META_PIXEL_ID)
    return ("<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
            "gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',"
            "analytics_storage:'denied',wait_for_update:500});"
            f"window.HA_TRACK={cfg};</script>\n"
            '<script src="/js/consent.js" defer></script>\n')


# ------------------------------------------------------------------ banner

TEXT = {
    "en": {
        "title": "Cookies",
        "body": "Help us show you relevant offers. If you accept, Google and Meta advertising cookies let us show you our ads when you're planning your next job, and tell us which ads bring enquiries. Nothing is set unless you accept.",
        "accept": "Accept", "reject": "Reject", "more": "Privacy & cookies",
        "settings": "Cookie settings",
    },
    "sv": {
        "title": "Cookies",
        "body": "Hjälp oss visa dig relevanta erbjudanden. Om du godkänner låter annonscookies från Google och Meta oss visa våra annonser när du planerar ditt nästa jobb, och se vilka annonser som ger förfrågningar. Inget sparas om du inte godkänner.",
        "accept": "Godkänn", "reject": "Avvisa", "more": "Integritet & cookies",
        "settings": "Cookieinställningar",
    },
}


def privacy_url(lang):
    return "/privacy/" if lang == "en" else "/sv/integritet/"


def footer_links(lang):
    """Small links for the footer base line."""
    t = TEXT[lang]
    out = f' · <a href="{privacy_url(lang)}">{t["more"]}</a>'
    if enabled():
        out += f' · <a href="#" data-cookie-settings>{t["settings"]}</a>'
    return out


def banner(lang):
    if not enabled():
        return ""
    t = TEXT[lang]
    return f"""<div class="ha-cc" id="ha-cc" role="dialog" aria-live="polite" aria-label="{t["title"]}" hidden>
  <p><b>{t["title"]}.</b> {_html.escape(t["body"])} <a href="{privacy_url(lang)}">{t["more"]}</a></p>
  <div class="ha-cc-btns"><button type="button" class="ha-cc-btn" data-cc="reject">{t["reject"]}</button><button type="button" class="ha-cc-btn" data-cc="accept">{t["accept"]}</button></div>
</div>
"""


JS = r"""/* Handyman Axarquia: cookie consent + Google Ads / Meta Pixel (loaded only after Accept) */
(function () {
  var C = window.HA_TRACK || {}, KEY = 'ha_consent', DAYS = 365, loaded = false;
  function get() {
    try { var s = JSON.parse(localStorage.getItem(KEY)); if (s && Date.now() - s.t < DAYS * 864e5) return s.v; } catch (e) {}
    return null;
  }
  function set(v) { try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {} }
  var box = document.getElementById('ha-cc');
  function show() { if (box) box.hidden = false; }
  function hide() { if (box) box.hidden = true; }

  function load() {
    if (loaded) return; loaded = true;
    gtag('consent', 'update', { ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted', analytics_storage: 'granted' });
    if (C.gads) {
      var s = document.createElement('script'); s.async = true;
      s.src = 'https://www.googletagmanager.com/gtag/js?id=' + C.gads; document.head.appendChild(s);
      gtag('js', new Date()); gtag('config', C.gads);
    }
    if (C.pixel) {
      !function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments) };
        if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0;
        t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s) }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', C.pixel); fbq('track', 'PageView');
    }
  }

  function lead(kind) {
    if (!loaded) return;
    if (C.gads) {
      gtag('event', 'generate_lead', { method: kind });
      if (C.lead) gtag('event', 'conversion', { send_to: C.gads + '/' + C.lead });
    }
    if (C.pixel && window.fbq) fbq('track', 'Lead', { content_name: kind });
  }

  function clearCookies() {
    document.cookie.split(';').forEach(function (c) {
      var n = c.split('=')[0].trim();
      if (/^(_gcl|_fbp|_fbc|_ga)/.test(n)) {
        ['', '; domain=.' + location.hostname.replace(/^www\./, '')].forEach(function (d) {
          document.cookie = n + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d;
        });
      }
    });
  }

  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-cc]');
    if (b) {
      var was = get();
      if (b.getAttribute('data-cc') === 'accept') { set('granted'); hide(); load(); }
      else { set('denied'); hide(); if (was === 'granted' || loaded) { clearCookies(); location.reload(); } }
      return;
    }
    if (e.target.closest('[data-cookie-settings]')) { e.preventDefault(); show(); return; }
    var a = e.target.closest('a[href]');
    if (a) {
      var h = a.getAttribute('href');
      if (h.indexOf('tel:') === 0) lead('phone');
      else if (h.indexOf('wa.me') > -1) lead('whatsapp');
      else if (h.indexOf('mailto:') === 0) lead('email');
    }
  });
  document.addEventListener('submit', function (e) { if (e.target.id === 'qform') lead('form'); });

  var v = get();
  if (v === 'granted') load(); else if (v !== 'denied') show();
})();
"""

CSS = """
/* cookie banner */
.ha-cc{position:fixed;left:16px;right:16px;bottom:16px;z-index:9999;max-width:760px;margin:0 auto;background:#0B0B0C;color:#E5E5EA;border:1px solid #FBA917;border-radius:14px;padding:16px 18px;box-shadow:0 10px 30px rgba(0,0,0,.45);display:flex;gap:16px;align-items:center;font-size:.9rem;line-height:1.5}
.ha-cc[hidden]{display:none}
.ha-cc p{margin:0;flex:1}
.ha-cc b{color:#fff}
.ha-cc a{color:#FBA917;text-decoration:underline}
.ha-cc-btns{display:flex;gap:10px;flex-shrink:0}
.ha-cc-btn{font:600 .9rem Poppins,sans-serif;padding:10px 20px;border-radius:999px;border:2px solid #FBA917;background:#FBA917;color:#0B0B0C;cursor:pointer;min-width:110px}
.ha-cc-btn:hover{filter:brightness(1.08)}
.ha-cc-btn:focus-visible{outline:3px solid #fff;outline-offset:2px}
@media (max-width:640px){.ha-cc{flex-direction:column;align-items:stretch;left:10px;right:10px;bottom:10px}.ha-cc-btns .ha-cc-btn{flex:1}}
.site-foot .base a{display:inline;padding:0;color:inherit;text-decoration:underline}
.policy h2{margin-top:1.6em}
.policy table{width:100%;border-collapse:collapse;margin:1em 0;font-size:.92rem}
.policy th,.policy td{border:1px solid #d9d9de;padding:8px 10px;text-align:left;vertical-align:top}
.policy th{background:#f4f4f6}
"""


def write_assets(site: Path):
    (site / "js").mkdir(parents=True, exist_ok=True)
    (site / "js" / "consent.js").write_text(JS)


# ------------------------------------------------------------- policy page

def _cookie_rows(lang):
    en = lang == "en"
    rows = [("ha_consent", "handymanaxarquia.com",
             "Remembers your cookie choice (stored in your browser, not a cookie)." if en
             else "Kommer ihåg ditt cookieval (sparas i webbläsaren, inte en cookie).",
             "12 months" if en else "12 månader")]
    if GOOGLE_ADS_ID:
        rows.append(("_gcl_au, IDE, test_cookie", "Google (Google Ireland Ltd)",
                     "Google Ads: remembers that you visited so we can show you our ads on other sites and measure enquiries from ads." if en
                     else "Google Ads: kommer ihåg att du besökt oss så att vi kan visa våra annonser på andra webbplatser och mäta förfrågningar från annonser.",
                     "Up to 13 months" if en else "Upp till 13 månader"))
    if META_PIXEL_ID:
        rows.append(("_fbp, fr", "Meta (Meta Platforms Ireland Ltd)",
                     "Meta Pixel: remembers that you visited so we can show you our ads on Facebook and Instagram and measure enquiries from ads." if en
                     else "Meta Pixel: kommer ihåg att du besökt oss så att vi kan visa våra annonser på Facebook och Instagram och mäta förfrågningar från annonser.",
                     "Up to 3 months" if en else "Upp till 3 månader"))
    head = ("Name", "Set by", "Purpose", "Kept for") if en else ("Namn", "Från", "Syfte", "Lagras")
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>"


def _owner_line(lang):
    bits = []
    if LEGAL_NAME:
        bits.append(LEGAL_NAME)
    if LEGAL_NIF:
        bits.append(f"NIE {LEGAL_NIF}")
    if not bits:
        return ""
    return ("Owner: " if lang == "en" else "Ägare: ") + ", ".join(bits) + "<br>"


def policy_page(lang):
    """Returns (title, desc, h1, body_html)."""
    en = lang == "en"
    ads = enabled()
    platforms = " and ".join(n for n, on in (("Google", GOOGLE_ADS_ID), ("Meta", META_PIXEL_ID)) if on) if en \
        else " och ".join(n for n, on in (("Google", GOOGLE_ADS_ID), ("Meta", META_PIXEL_ID)) if on)
    settings_link = (f'<p><a class="btn primary" href="#" data-cookie-settings>{TEXT[lang]["settings"]}</a></p>' if ads else "")
    owner = _owner_line(lang)
    if en:
        title = "Privacy & Cookie Policy | Handyman Axarquia"
        desc = "How Handyman Axarquia uses your details when you ask for a quote, which cookies the website uses, and how to change your choice."
        h1 = "Privacy & cookie policy"
        if ads:
            cookies_intro = (f"<p>If you click <b>Accept</b> on the cookie banner, we use advertising cookies from {platforms}. "
                             "They let us show our ads to people who have already visited this website (remarketing) and see how many enquiries come from those ads. "
                             "If you click <b>Reject</b>, or don't choose, none of these are set and nothing is sent to them.</p>")
        else:
            cookies_intro = "<p>This website does not currently use advertising or analytics cookies.</p>"
        body = f"""<div class="prose policy">
<p>Last updated: {{UPDATED}}</p>
<h2>Who we are</h2>
<p>Handyman Axarquia, Los Toscanos 33, Almayate Bajo, 29749 Málaga, Spain.<br>{owner}Email: <a href="mailto:info@handymanaxarquia.com">info@handymanaxarquia.com</a> · Phone: <a href="tel:+34711027432">+34 711 027 432</a></p>
<p>We are responsible for the personal details you give us through this website.</p>
<h2>What we collect and why</h2>
<ul>
<li><b>Quote and contact requests.</b> When you use the quote form, email, phone or WhatsApp us, we receive your name, contact details and what you tell us about the job. We use this only to reply, visit, quote and carry out the work. The quote form is delivered to our inbox by FormSubmit (formsubmit.co).</li>
<li><b>Customers.</b> If you hire us, we keep your details and invoices for as long as Spanish tax law requires (normally 6 years).</li>
<li><b>Enquiries that don't go ahead</b> are deleted within 12 months.</li>
</ul>
<p>The legal basis is taking steps at your request before a contract, the contract itself, and our legal obligations. For advertising cookies it is your consent, which you can withdraw at any time.</p>
<h2>Cookies</h2>
{cookies_intro}
{_cookie_rows(lang)}
{settings_link}
<p>The site's font is hosted on our own server, so your browser does not contact Google Fonts.</p>
<h2>Who else sees your data</h2>
<p>We never sell your details. We use FormSubmit for the quote form{", plus " + platforms + " for advertising if you accept cookies" if ads else ""}. Some of these companies may process data outside the EU; where they do, they rely on the EU-US Data Privacy Framework or the European Commission's standard contractual clauses.</p>
<h2>Your rights</h2>
<p>You can ask to see, correct or delete your details, object to or limit how we use them, or take a copy with you. Email <a href="mailto:info@handymanaxarquia.com">info@handymanaxarquia.com</a>. If you're not happy with our answer you can complain to the Spanish data protection authority, the AEPD (<a href="https://www.aepd.es" target="_blank" rel="noopener">www.aepd.es</a>).</p>
</div>"""
    else:
        title = "Integritets- och cookiepolicy | Handyman Axarquia"
        desc = "Hur Handyman Axarquia använder dina uppgifter när du ber om en offert, vilka cookies webbplatsen använder och hur du ändrar ditt val."
        h1 = "Integritets- och cookiepolicy"
        if ads:
            cookies_intro = (f"<p>Om du klickar på <b>Godkänn</b> i cookierutan använder vi annonscookies från {platforms}. "
                             "De gör att vi kan visa våra annonser för personer som redan har besökt webbplatsen (remarketing) och se hur många förfrågningar annonserna ger. "
                             "Om du klickar på <b>Avvisa</b>, eller inte väljer, sparas inga sådana cookies och inget skickas till dem.</p>")
        else:
            cookies_intro = "<p>Webbplatsen använder för närvarande inga annons- eller analyscookies.</p>"
        body = f"""<div class="prose policy">
<p>Senast uppdaterad: {{UPDATED}}</p>
<h2>Vilka vi är</h2>
<p>Handyman Axarquia, Los Toscanos 33, Almayate Bajo, 29749 Málaga, Spanien.<br>{owner}E-post: <a href="mailto:info@handymanaxarquia.com">info@handymanaxarquia.com</a> · Telefon: <a href="tel:+34711027432">+34 711 027 432</a></p>
<p>Vi ansvarar för de personuppgifter du lämnar via webbplatsen.</p>
<h2>Vad vi samlar in och varför</h2>
<ul>
<li><b>Offert- och kontaktförfrågningar.</b> När du använder offertformuläret, mejlar, ringer eller skriver på WhatsApp får vi ditt namn, dina kontaktuppgifter och det du berättar om jobbet. Vi använder det bara för att svara, besöka, lämna offert och utföra arbetet. Offertformuläret levereras till vår inkorg av FormSubmit (formsubmit.co).</li>
<li><b>Kunder.</b> Om du anlitar oss sparar vi dina uppgifter och fakturor så länge spansk skattelag kräver (normalt 6 år).</li>
<li><b>Förfrågningar som inte blir av</b> raderas inom 12 månader.</li>
</ul>
<p>Den rättsliga grunden är åtgärder på din begäran innan ett avtal, själva avtalet och våra rättsliga skyldigheter. För annonscookies är grunden ditt samtycke, som du kan återkalla när som helst.</p>
<h2>Cookies</h2>
{cookies_intro}
{_cookie_rows(lang)}
{settings_link}
<p>Webbplatsens typsnitt ligger på vår egen server, så din webbläsare kontaktar inte Google Fonts.</p>
<h2>Vem mer ser dina uppgifter</h2>
<p>Vi säljer aldrig dina uppgifter. Vi använder FormSubmit för offertformuläret{", samt " + platforms + " för annonsering om du godkänner cookies" if ads else ""}. Vissa av dessa företag kan behandla uppgifter utanför EU; i så fall sker det enligt EU-US Data Privacy Framework eller EU-kommissionens standardavtalsklausuler.</p>
<h2>Dina rättigheter</h2>
<p>Du kan begära att få se, rätta eller radera dina uppgifter, invända mot eller begränsa hur vi använder dem, eller få en kopia. Mejla <a href="mailto:info@handymanaxarquia.com">info@handymanaxarquia.com</a>. Om du inte är nöjd med vårt svar kan du klaga hos den spanska dataskyddsmyndigheten AEPD (<a href="https://www.aepd.es" target="_blank" rel="noopener">www.aepd.es</a>).</p>
</div>"""
    return title, desc, h1, body
