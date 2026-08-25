# Rebuilds the two /brand/tshirt-*/ pages: a clean artwork mock-up (no caption text
# burnt into the image) plus a printer-facing brand specification panel underneath —
# exact colours (hex / RGB / CMYK / Pantone), fonts and tracking, print sizes and
# method — in English or Spanish via a language switch. Runs after brand_pack.build().
from pathlib import Path

PHONE = "+34 711 027 432"
WEB = "handymanaxarquia.com"

FONT_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
             '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">')

FRONT_INNER = """<div style="width:100%;height:100%;background:radial-gradient(600px 400px at 50% 50%, #1a1a1e, #0B0B0C);display:flex;align-items:center;justify-content:center">
  <img src="/images/logo_mark.svg" alt="HA" style="width:270px">
</div>"""

BACK_INNER = f"""<div style="width:100%;height:100%;background:radial-gradient(600px 400px at 50% 50%, #1a1a1e, #0B0B0C);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:26px">
  <div style="font-size:52px;font-weight:700;letter-spacing:8px;white-space:nowrap"><span style="color:#fff">HANDYMAN</span> <span style="color:#FBA917">AXARQUIA</span></div>
  <div style="color:#FBA917;font-size:21px;letter-spacing:5px">{PHONE} &nbsp;&middot;&nbsp; <span style="color:#fff">{WEB}</span></div>
</div>"""

SPEC_CSS = """
body { font-family:'Poppins',sans-serif; background:#232326; }
.specwrap { max-width:1180px; margin:0 auto; padding:26px 20px 60px; }
.mock { display:flex; justify-content:center; }
.tophead { display:flex; align-items:flex-end; justify-content:space-between; gap:16px; margin:34px 0 16px; flex-wrap:wrap; }
.spec-h { color:#fff; font-size:1.05rem; font-weight:600; letter-spacing:.4px; }
.spec-h span { color:#FBA917; }
.spec-sub { color:#8E8E93; font-size:.72rem; letter-spacing:2.2px; text-transform:uppercase; margin-top:4px; }
.langsw { display:flex; gap:6px; flex:0 0 auto; }
.langsw button { background:#1a1a1d; color:#9a9aa0; border:1px solid #3a3a3e; border-radius:8px;
  padding:7px 14px; font-size:12.5px; font-family:inherit; cursor:pointer; letter-spacing:.5px; }
.langsw button:hover { border-color:#FBA917; color:#FBA917; }
.langsw button.on { background:#FBA917; border-color:#FBA917; color:#0B0B0C; font-weight:600; }
.spec-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(270px,1fr)); gap:16px; }
.spec-card { background:#1a1a1d; border:1px solid #303034; border-radius:14px; padding:18px 20px; }
.spec-card h4 { color:#FBA917; font-size:.68rem; letter-spacing:2.5px; text-transform:uppercase;
  font-weight:600; margin-bottom:14px; padding-bottom:9px; border-bottom:1px solid #303034; }
.sw { display:flex; align-items:flex-start; gap:14px; margin-bottom:16px; }
.sw:last-child { margin-bottom:0; }
.sw .chip { width:52px; height:52px; border-radius:12px; flex:0 0 auto; border:1px solid #45454a; }
.sw .n { color:#fff; font-size:.88rem; font-weight:600; margin-bottom:2px; }
.sw .v { color:#9a9aa0; font-size:.73rem; line-height:1.7; font-variant-numeric:tabular-nums; }
.sw .v b { color:#d6d6da; font-weight:500; }
.frow { margin-bottom:18px; }
.frow .fname { color:#fff; font-size:.9rem; font-weight:600; }
.frow .fsample { color:#fff; margin:8px 0 8px; }
.frow .fmeta, .fnote { color:#9a9aa0; font-size:.73rem; line-height:1.75; }
.frow .fmeta b, .fnote b { color:#d6d6da; font-weight:500; }
.fnote { margin-top:14px; padding-top:12px; border-top:1px solid #303034; }
.spec-card ul { list-style:none; }
.spec-card li { color:#9a9aa0; font-size:.76rem; line-height:1.85; padding-left:15px; position:relative; }
.spec-card li::before { content:"\\203A"; position:absolute; left:0; color:#FBA917; font-weight:700; }
.spec-card li b { color:#d6d6da; font-weight:500; }
.spec-note { color:#6E6E73; font-size:.72rem; line-height:1.75; margin-top:18px; }
[data-lang] { display:none; }
[data-lang].on { display:block; }
.spec-grid[data-lang].on { display:grid; }
"""

# ---------------------------------------------------------------- copy

EN = {
    "sub": "Brand specification &middot; fonts &middot; colours &middot; print sizes",
    "front_h": 'T-shirt front &mdash; <span>HA mark</span>',
    "back_h": 'T-shirt back &mdash; <span>wordmark</span>',
    "colours": "Colours used",
    "fonts": "Fonts used",
    "print": "Print specification",
    "c_orange": "Brand Orange", "c_white": "White", "c_black": "Garment Black",
    "c_black_use": "Shirt colour &mdash; not printed",
    "back_orange_use": "&ldquo;AXARQUIA&rdquo; and the phone number",
    "back_white_use": "&ldquo;HANDYMAN&rdquo; and the web address",
    "front_orange_use": "The mark &mdash; the only printed colour",
    "front_white_use": "Not used on the front print",
    "f_bold": "Poppins Bold &mdash; weight 700",
    "f_reg": "Poppins Regular &mdash; weight 400",
    "f_wordmark": "Wordmark &middot; uppercase &middot; tracking <b>+0.15 em</b> (150)",
    "f_cap": "Cap height at 30 cm print width: <b>&asymp; 38 mm</b>",
    "f_contact": "Contact strip &middot; tracking <b>+0.24 em</b> (240)",
    "f_contact2": "Set at <b>&asymp; 40 %</b> of the wordmark cap height",
    "f_notype": "No live type in this print",
    "f_notype2": ("The chest mark is a <b>vector shape</b>, not text &mdash; the letterforms are "
                  "outlined paths, so the printer needs no font file."),
    "f_ifadded": ("Used if the wordmark is added below the mark &middot; uppercase &middot; "
                  "tracking <b>+0.15 em</b> (150)"),
    "f_note": ("Poppins &mdash; Indian Type Foundry, <b>SIL Open Font License</b>, free for "
               "commercial use.<br>Download: <b>fonts.google.com/specimen/Poppins</b><br>"
               "Supply artwork with text <b>converted to outlines</b>."),
    "back_print": [
        "Placement: <b>back, across the shoulders</b>",
        "Print width: <b>30 cm</b> &middot; top edge <b>&asymp; 8 cm</b> below the collar",
        "Method: <b>DTF transfer</b> (direct-to-film), heat applied",
        "Artwork: <b>HA_Back_Wordmark_30cm_TRANSPARENT_300dpi.png</b>",
        "Resolution: <b>300 DPI</b>, transparent background, no white box",
        "Press: <b>150&ndash;160 &deg;C, 15 s, medium pressure</b> &mdash; confirm with supplier",
        "Two print colours only: <b>white + #FBA917</b>",
    ],
    "front_print": [
        "Placement: <b>left chest</b>, or centred as a large print",
        "Print width: <b>9 cm</b> chest &middot; <b>25 cm</b> large &middot; <b>5 cm</b> cap or sleeve",
        "Method: <b>DTF transfer</b> (direct-to-film), heat applied",
        "Artwork: <b>HA_Logo_Chest_9cm_TRANSPARENT_300dpi.png</b>",
        "Vector master: <b>HA_Logo_VECTOR.svg</b> &mdash; scales to any size",
        "Resolution: <b>300 DPI</b>, transparent background, no white box",
        "Single flat colour (<b>#FBA917</b>) &mdash; one-colour print",
    ],
    "note": ("Hex and RGB values are exact. CMYK and Pantone are the nearest equivalents and should "
             "be confirmed against a physical proof &mdash; screen colour and ink on fabric never "
             "match perfectly. For DTF printing the supplier works directly from the RGB artwork files above."),
}

ES = {
    "sub": "Especificaci&oacute;n de marca &middot; tipograf&iacute;as &middot; colores &middot; tama&ntilde;os de impresi&oacute;n",
    "front_h": 'Camiseta delantera &mdash; <span>emblema HA</span>',
    "back_h": 'Camiseta espalda &mdash; <span>logotipo</span>',
    "colours": "Colores utilizados",
    "fonts": "Tipograf&iacute;as utilizadas",
    "print": "Especificaci&oacute;n de impresi&oacute;n",
    "c_orange": "Naranja corporativo", "c_white": "Blanco", "c_black": "Negro de la prenda",
    "c_black_use": "Color de la camiseta &mdash; no se imprime",
    "back_orange_use": "&laquo;AXARQUIA&raquo; y el n&uacute;mero de tel&eacute;fono",
    "back_white_use": "&laquo;HANDYMAN&raquo; y la direcci&oacute;n web",
    "front_orange_use": "El emblema &mdash; el &uacute;nico color impreso",
    "front_white_use": "No se usa en el estampado delantero",
    "f_bold": "Poppins Bold &mdash; grosor 700",
    "f_reg": "Poppins Regular &mdash; grosor 400",
    "f_wordmark": "Logotipo &middot; may&uacute;sculas &middot; interletraje <b>+0,15 em</b> (150)",
    "f_cap": "Altura de may&uacute;scula a 30 cm de ancho: <b>&asymp; 38 mm</b>",
    "f_contact": "L&iacute;nea de contacto &middot; interletraje <b>+0,24 em</b> (240)",
    "f_contact2": "Al <b>&asymp; 40 %</b> de la altura de may&uacute;scula del logotipo",
    "f_notype": "Sin texto editable en este estampado",
    "f_notype2": ("El emblema del pecho es una <b>forma vectorial</b>, no texto: las letras est&aacute;n "
                  "convertidas a curvas, por lo que la imprenta no necesita el archivo de fuente."),
    "f_ifadded": ("Se usa si se a&ntilde;ade el logotipo bajo el emblema &middot; may&uacute;sculas "
                  "&middot; interletraje <b>+0,15 em</b> (150)"),
    "f_note": ("Poppins &mdash; Indian Type Foundry, licencia <b>SIL Open Font</b>, uso comercial "
               "gratuito.<br>Descarga: <b>fonts.google.com/specimen/Poppins</b><br>"
               "Enviar el arte con el texto <b>convertido a curvas</b>."),
    "back_print": [
        "Colocaci&oacute;n: <b>espalda, a lo ancho de los hombros</b>",
        "Ancho de impresi&oacute;n: <b>30 cm</b> &middot; borde superior <b>&asymp; 8 cm</b> bajo el cuello",
        "M&eacute;todo: <b>transfer DTF</b> (direct-to-film), aplicado con calor",
        "Arte final: <b>HA_Back_Wordmark_30cm_TRANSPARENT_300dpi.png</b>",
        "Resoluci&oacute;n: <b>300 PPP</b>, fondo transparente, sin recuadro blanco",
        "Plancha: <b>150&ndash;160 &deg;C, 15 s, presi&oacute;n media</b> &mdash; confirmar con el proveedor",
        "Solo dos colores de impresi&oacute;n: <b>blanco + #FBA917</b>",
    ],
    "front_print": [
        "Colocaci&oacute;n: <b>pecho izquierdo</b>, o centrado como estampado grande",
        "Ancho de impresi&oacute;n: <b>9 cm</b> pecho &middot; <b>25 cm</b> grande &middot; <b>5 cm</b> gorra o manga",
        "M&eacute;todo: <b>transfer DTF</b> (direct-to-film), aplicado con calor",
        "Arte final: <b>HA_Logo_Chest_9cm_TRANSPARENT_300dpi.png</b>",
        "Vector maestro: <b>HA_Logo_VECTOR.svg</b> &mdash; escalable a cualquier tama&ntilde;o",
        "Resoluci&oacute;n: <b>300 PPP</b>, fondo transparente, sin recuadro blanco",
        "Un solo color plano (<b>#FBA917</b>) &mdash; impresi&oacute;n a un color",
    ],
    "note": ("Los valores hex y RGB son exactos. CMYK y Pantone son los equivalentes m&aacute;s "
             "pr&oacute;ximos y deben confirmarse con una prueba f&iacute;sica &mdash; el color en "
             "pantalla y la tinta sobre tejido nunca coinciden del todo. Para DTF, el proveedor "
             "trabaja directamente con los archivos RGB indicados arriba."),
}

# ---------------------------------------------------------------- cards


def _swatch(name, hexv, rgb, cmyk, pantone, use):
    return (f'<div class="sw"><div class="chip" style="background:{hexv}"></div>'
            f'<div><div class="n">{name}</div><div class="v"><b>{hexv}</b> &nbsp;RGB {rgb}<br>'
            f'CMYK {cmyk}<br>Pantone {pantone}<br>{use}</div></div></div>')


def _colour_card(L, orange_use, white_use):
    return (f'<div class="spec-card"><h4>{L["colours"]}</h4>'
            + _swatch(L["c_orange"], "#FBA917", "251 &middot; 169 &middot; 23", "0 / 33 / 91 / 2", "&asymp; 130 C", orange_use)
            + _swatch(L["c_white"], "#FFFFFF", "255 &middot; 255 &middot; 255", "0 / 0 / 0 / 0", "&mdash;", white_use)
            + _swatch(L["c_black"], "#0B0B0C", "11 &middot; 11 &middot; 12", "75 / 68 / 67 / 90", "&asymp; Black 6 C", L["c_black_use"])
            + '</div>')

WORDMARK_SAMPLE = ('<div class="fsample" style="font-weight:700;letter-spacing:.15em;font-size:1.25rem">'
                   'HANDYMAN <span style="color:#FBA917">AXARQUIA</span></div>')


def _back_type_card(L):
    return f"""<div class="spec-card"><h4>{L["fonts"]}</h4>
<div class="frow"><div class="fname">{L["f_bold"]}</div>{WORDMARK_SAMPLE}
  <div class="fmeta">{L["f_wordmark"]}<br>{L["f_cap"]}</div></div>
<div class="frow" style="margin-bottom:0"><div class="fname">{L["f_reg"]}</div>
  <div class="fsample" style="font-weight:400;letter-spacing:.24em;font-size:1rem;color:#FBA917">{PHONE}</div>
  <div class="fmeta">{L["f_contact"]}<br>{L["f_contact2"]}</div></div>
<div class="fnote">{L["f_note"]}</div></div>"""


def _front_type_card(L):
    return f"""<div class="spec-card"><h4>{L["fonts"]}</h4>
<div class="frow"><div class="fname">{L["f_notype"]}</div>
  <div class="fmeta">{L["f_notype2"]}</div></div>
<div class="frow" style="margin-bottom:0"><div class="fname">{L["f_bold"]}</div>{WORDMARK_SAMPLE}
  <div class="fmeta">{L["f_ifadded"]}</div></div>
<div class="fnote">{L["f_note"]}</div></div>"""


def _print_card(L, key):
    return (f'<div class="spec-card"><h4>{L["print"]}</h4><ul>'
            + "".join(f"<li>{l}</li>" for l in L[key]) + "</ul></div>")


def _grid(L, side, on):
    if side == "back":
        cards = (_colour_card(L, L["back_orange_use"], L["back_white_use"])
                 + _back_type_card(L) + _print_card(L, "back_print"))
    else:
        cards = (_colour_card(L, L["front_orange_use"], L["front_white_use"])
                 + _front_type_card(L) + _print_card(L, "front_print"))
    return f'<div class="spec-grid{on}" data-lang="{L["code"]}">{cards}</div>'


SWITCH_JS = """<script>
function setLang(code) {
  document.querySelectorAll('[data-lang]').forEach(function (el) {
    el.classList.toggle('on', el.getAttribute('data-lang') === code);
  });
  document.querySelectorAll('.langsw button').forEach(function (b) {
    b.classList.toggle('on', b.getAttribute('data-set') === code);
  });
  try { localStorage.setItem('ha_spec_lang', code); } catch (e) {}
}
try {
  var saved = localStorage.getItem('ha_spec_lang');
  if (saved === 'es' || saved === 'en') setLang(saved);
} catch (e) {}
</script>"""


def _page(title, w, h, inner, side):
    en, es = dict(EN, code="en"), dict(ES, code="es")
    hk = "back_h" if side == "back" else "front_h"
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>{FONT_LINK}
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
.stage {{ width:{w}px; height:{h}px; flex:0 0 auto; box-shadow:0 14px 50px rgba(0,0,0,.5);
  border-radius:18px; overflow:hidden; }}
{SPEC_CSS}
</style></head><body>
<div class="specwrap">
  <div class="mock"><div class="stage">{inner}</div></div>
  <div class="tophead">
    <div>
      <div class="spec-h on" data-lang="en">{en[hk]}</div>
      <div class="spec-h" data-lang="es">{es[hk]}</div>
      <div class="spec-sub on" data-lang="en">{en["sub"]}</div>
      <div class="spec-sub" data-lang="es">{es["sub"]}</div>
    </div>
    <div class="langsw">
      <button data-set="en" class="on" onclick="setLang('en')">&#127468;&#127463; EN</button>
      <button data-set="es" onclick="setLang('es')">&#127466;&#127480; ES</button>
    </div>
  </div>
  {_grid(en, side, " on")}{_grid(es, side, "")}
  <div class="spec-note on" data-lang="en">{en["note"]}</div>
  <div class="spec-note" data-lang="es">{es["note"]}</div>
</div>{SWITCH_JS}</body></html>"""


def apply(site: Path):
    brand = site / "brand"
    if not brand.exists():
        return
    pages = {
        "tshirt-front": _page("T-shirt — front", 1004, 560, FRONT_INNER, "front"),
        "tshirt-back": _page("T-shirt — back", 1100, 560, BACK_INNER, "back"),
    }
    for name, html in pages.items():
        d = brand / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(html)
    print("t-shirt spec panels applied")


if __name__ == "__main__":
    apply(Path(__file__).resolve().parent.parent / "site")
