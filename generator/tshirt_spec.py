# Rebuilds the two /brand/tshirt-*/ pages with a printer-facing brand specification
# panel underneath the mock-up: exact colours (hex / RGB / CMYK / Pantone), the fonts
# and tracking used, and the print sizes and method. Runs after brand_pack.build().
from pathlib import Path

PHONE = "+34 711 027 432"
WEB = "handymanaxarquia.com"

FONT_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
             '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">')

FRONT_INNER = """<div style="width:100%;height:100%;background:radial-gradient(600px 400px at 50% 40%, #1a1a1e, #0B0B0C);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:34px">
  <img src="/images/logo_mark.svg" alt="HA" style="width:270px">
  <div style="color:#5A5A5F;font-size:13px;letter-spacing:3px;text-transform:uppercase">Front — left chest 9 cm · large print 25 cm</div>
</div>"""

BACK_INNER = f"""<div style="width:100%;height:100%;background:radial-gradient(600px 400px at 50% 40%, #1a1a1e, #0B0B0C);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:26px">
  <div style="font-size:52px;font-weight:700;letter-spacing:8px;white-space:nowrap"><span style="color:#fff">HANDYMAN</span> <span style="color:#FBA917">AXARQUIA</span></div>
  <div style="color:#FBA917;font-size:21px;letter-spacing:5px">{PHONE} &nbsp;·&nbsp; <span style="color:#fff">{WEB}</span></div>
  <div style="color:#5A5A5F;font-size:13px;letter-spacing:3px;text-transform:uppercase;margin-top:12px">Back — 30 cm across the shoulders · DTF transfer</div>
</div>"""

SPEC_CSS = """
body { font-family:'Poppins',sans-serif; background:#232326; }
.specwrap { max-width:1180px; margin:0 auto; padding:26px 20px 60px; }
.mock { display:flex; justify-content:center; }
.spec-h { color:#fff; font-size:1.05rem; font-weight:600; letter-spacing:.4px; margin:34px 0 4px; }
.spec-h span { color:#FBA917; }
.spec-sub { color:#8E8E93; font-size:.72rem; letter-spacing:2.2px; text-transform:uppercase; margin-bottom:16px; }
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
"""


def _swatch(name, hexv, rgb, cmyk, pantone, use):
    return (f'<div class="sw"><div class="chip" style="background:{hexv}"></div>'
            f'<div><div class="n">{name}</div><div class="v"><b>{hexv}</b> &nbsp;RGB {rgb}<br>'
            f'CMYK {cmyk}<br>Pantone {pantone}<br>{use}</div></div></div>')


def colour_card(orange_use, white_use):
    return ('<div class="spec-card"><h4>Colours used</h4>'
            + _swatch("Brand Orange", "#FBA917", "251 · 169 · 23", "0 / 33 / 91 / 2", "≈ 130 C", orange_use)
            + _swatch("White", "#FFFFFF", "255 · 255 · 255", "0 / 0 / 0 / 0", "—", white_use)
            + _swatch("Garment Black", "#0B0B0C", "11 · 11 · 12", "75 / 68 / 67 / 90", "≈ Black 6 C",
                      "Shirt colour — not printed")
            + '</div>')

FONT_NOTE = ('<div class="fnote">Poppins — Indian Type Foundry, <b>SIL Open Font License</b>, '
             'free for commercial use.<br>Download: <b>fonts.google.com/specimen/Poppins</b><br>'
             'Supply artwork with text <b>converted to outlines</b>.</div>')

BACK_TYPE_CARD = """<div class="spec-card"><h4>Fonts used</h4>
<div class="frow">
  <div class="fname">Poppins Bold &mdash; weight 700</div>
  <div class="fsample" style="font-weight:700;letter-spacing:.15em;font-size:1.25rem">HANDYMAN <span style="color:#FBA917">AXARQUIA</span></div>
  <div class="fmeta">Wordmark &middot; uppercase &middot; tracking <b>+0.15 em</b> (150)<br>
  Cap height at 30 cm print width: <b>&asymp; 38 mm</b></div>
</div>
<div class="frow" style="margin-bottom:0">
  <div class="fname">Poppins Regular &mdash; weight 400</div>
  <div class="fsample" style="font-weight:400;letter-spacing:.24em;font-size:1rem;color:#FBA917">+34 711 027 432</div>
  <div class="fmeta">Contact strip &middot; tracking <b>+0.24 em</b> (240)<br>
  Set at <b>&asymp; 40 %</b> of the wordmark cap height</div>
</div>""" + FONT_NOTE + "</div>"

FRONT_TYPE_CARD = """<div class="spec-card"><h4>Fonts used</h4>
<div class="frow">
  <div class="fname">No live type in this print</div>
  <div class="fmeta">The chest mark is a <b>vector shape</b>, not text &mdash; the letterforms are
  outlined paths, so no font file is needed by the printer.</div>
</div>
<div class="frow" style="margin-bottom:0">
  <div class="fname">Poppins Bold &mdash; weight 700</div>
  <div class="fsample" style="font-weight:700;letter-spacing:.15em;font-size:1.25rem">HANDYMAN <span style="color:#FBA917">AXARQUIA</span></div>
  <div class="fmeta">Used if the wordmark is added below the mark &middot; uppercase &middot;
  tracking <b>+0.15 em</b> (150)</div>
</div>""" + FONT_NOTE + "</div>"


def _print_card(lines):
    return ('<div class="spec-card"><h4>Print specification</h4><ul>'
            + "".join(f"<li>{l}</li>" for l in lines) + "</ul></div>")

BACK_PRINT_CARD = _print_card([
    "Placement: <b>back, across the shoulders</b>",
    "Print width: <b>30 cm</b> &middot; top edge <b>&asymp; 8 cm</b> below the collar",
    "Method: <b>DTF transfer</b> (direct-to-film), heat applied",
    "Artwork: <b>HA_Back_Wordmark_30cm_TRANSPARENT_300dpi.png</b>",
    "Resolution: <b>300 DPI</b>, transparent background, no white box",
    "Press: <b>150&ndash;160 &deg;C, 15 s, medium pressure</b> &mdash; confirm with supplier",
    "Two print colours only: <b>white + #FBA917</b>",
])

FRONT_PRINT_CARD = _print_card([
    "Placement: <b>left chest</b>, or centred as a large print",
    "Print width: <b>9 cm</b> chest &middot; <b>25 cm</b> large &middot; <b>5 cm</b> cap or sleeve",
    "Method: <b>DTF transfer</b> (direct-to-film), heat applied",
    "Artwork: <b>HA_Logo_Chest_9cm_TRANSPARENT_300dpi.png</b>",
    "Vector master: <b>HA_Logo_VECTOR.svg</b> &mdash; scales to any size",
    "Resolution: <b>300 DPI</b>, transparent background, no white box",
    "Single flat colour (<b>#FBA917</b>) &mdash; one-colour print",
])

FOOTNOTE = ("Hex and RGB values are exact. CMYK and Pantone are the nearest equivalents and should be "
            "confirmed against a physical proof — screen colour and ink on fabric never match perfectly. "
            "For DTF printing the supplier works directly from the RGB artwork files above.")


def _page(title, w, h, inner, heading, colour_html, type_html, print_html):
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
  <div class="spec-h">{heading}</div>
  <div class="spec-sub">Brand specification &middot; fonts &middot; colours &middot; print sizes</div>
  <div class="spec-grid">{colour_html}{type_html}{print_html}</div>
  <div class="spec-note">{FOOTNOTE}</div>
</div></body></html>"""


def apply(site: Path):
    brand = site / "brand"
    if not brand.exists():
        return
    pages = {
        "tshirt-front": _page(
            "T-shirt — front", 1004, 620, FRONT_INNER,
            'T-shirt front &mdash; <span>HA mark</span>',
            colour_card("The mark — the only printed colour", "Not used on the front print"),
            FRONT_TYPE_CARD, FRONT_PRINT_CARD),
        "tshirt-back": _page(
            "T-shirt — back", 1100, 620, BACK_INNER,
            'T-shirt back &mdash; <span>wordmark</span>',
            colour_card("“AXARQUIA” and the phone number",
                        "“HANDYMAN” and the web address"),
            BACK_TYPE_CARD, BACK_PRINT_CARD),
    }
    for name, html in pages.items():
        d = brand / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(html)
    print("t-shirt spec panels applied")


if __name__ == "__main__":
    apply(Path(__file__).resolve().parent.parent / "site")
