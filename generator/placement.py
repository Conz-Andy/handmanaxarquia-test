# Print-placement diagrams for the t-shirt spec pages: a flat t-shirt outline drawn
# to scale, with the print area, the centre fold and dimensioned callouts. The back
# prints also carry an enlarged detail strip of the actual artwork. Bilingual labels.

CM = 5.5          # px per cm — the tee body (296 px) is a ~54 cm flat-width adult shirt
COLLAR = 108      # y of the collar seam at the centre
FOLD = 300        # x of the centre fold

TEE = ("M 212,52 C 212,52 192,46 176,54 L 88,98 L 52,180 L 120,214 L 152,162 "
       "L 152,566 L 448,566 L 448,162 L 480,214 L 548,180 L 512,98 L 424,54 "
       "C 408,46 388,52 388,52 C 383,88 352,108 300,108 C 248,108 217,88 212,52 Z")

CSS = """
.plc { display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:16px; }
.plc figure { background:#1a1a1d; border:1px solid #303034; border-radius:14px; padding:16px 16px 14px; }
.plc svg { width:100%; height:auto; display:block; }
.plc figcaption { color:#fff; font-size:.85rem; font-weight:600; margin-top:10px; }
.plc .cap2 { color:#9a9aa0; font-size:.73rem; line-height:1.7; margin-top:4px; overflow-wrap:anywhere; }
.plc .cap2 b { color:#d6d6da; font-weight:500; }
"""

_S = {
    "tee": 'fill="#141417" stroke="#3f3f45" stroke-width="2"',
    "collar": 'fill="none" stroke="#3f3f45" stroke-width="2"',
    "fold": 'stroke="#FBA917" stroke-width="1.5" stroke-dasharray="7 7" opacity=".45"',
    "box": 'fill="rgba(251,169,23,.07)" stroke="#FBA917" stroke-width="1.6" stroke-dasharray="5 4"',
    "dim": 'stroke="#8E8E93" stroke-width="1.2"',
    "lead": 'stroke="#5a5a60" stroke-width="1" stroke-dasharray="4 4"',
    "txt": 'fill="#d6d6da" font-family="Poppins,sans-serif" font-size="15"',
    "txts": 'fill="#8E8E93" font-family="Poppins,sans-serif" font-size="13"',
    "txtxs": 'fill="#6E6E73" font-family="Poppins,sans-serif" font-size="11"',
}


def _defs():
    return ('<defs><marker id="a" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">'
            '<path d="M0,0 L7,3.5 L0,7 z" fill="#8E8E93"/></marker>'
            '<marker id="b" markerWidth="7" markerHeight="7" refX="1" refY="3.5" orient="auto">'
            '<path d="M7,0 L0,3.5 L7,7 z" fill="#8E8E93"/></marker></defs>')


def _tee():
    return (f'<path d="{TEE}" {_S["tee"]}/>'
            f'<path d="M 212,52 C 217,88 248,108 300,108 C 352,108 383,88 388,52" {_S["collar"]}/>'
            f'<line x1="300" y1="112" x2="300" y2="566" {_S["fold"]}/>')


def _wordmark(cx, y, width, size, contact=None, csize=0, cy=0):
    """Wordmark set to an exact width so it always fits its print box."""
    out = (f'<text x="{cx}" y="{y}" text-anchor="middle" textLength="{width}" '
           f'lengthAdjust="spacingAndGlyphs" font-family="Poppins,sans-serif" '
           f'font-size="{size}" font-weight="700">'
           f'<tspan fill="#ffffff">HANDYMAN</tspan> <tspan fill="#FBA917">AXARQUIA</tspan></text>')
    if contact:
        out += (f'<text x="{cx}" y="{cy}" text-anchor="middle" textLength="{width * .94}" '
                f'lengthAdjust="spacingAndGlyphs" font-family="Poppins,sans-serif" '
                f'font-size="{csize}" fill="#FBA917">{contact}</text>')
    return out


# ---------------------------------------------------------------- front


def chest(L):
    """Left-chest mark — wearer's left, i.e. the right side of the flat garment."""
    w = 9 * CM
    h = w * 1.112
    cx = FOLD + 10 * CM
    x0 = cx - w / 2
    y0 = COLLAR + 7 * CM
    return f"""<svg viewBox="0 0 600 640" role="img">{_defs()}{_tee()}
<rect x="{x0:.1f}" y="{y0:.1f}" width="{w:.1f}" height="{h:.1f}" rx="4" {_S["box"]}/>
<image href="/images/logo_mark.svg" x="{x0 + 4:.1f}" y="{y0 + 3:.1f}" width="{w - 8:.1f}" height="{h - 6:.1f}"
  preserveAspectRatio="xMidYMid meet"/>
<line x1="{cx}" y1="134" x2="{cx}" y2="{y0:.1f}" {_S["dim"]} stroke-dasharray="3 3"/>
<line x1="{FOLD}" y1="134" x2="{cx}" y2="134" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<text x="{cx}" y="120" {_S["txts"]} text-anchor="middle">{L["d_centre"]}</text>
<line x1="{x0 + w + 26:.1f}" y1="{COLLAR}" x2="{x0 + w + 26:.1f}" y2="{y0:.1f}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<line x1="{x0 + w:.1f}" y1="{COLLAR}" x2="{x0 + w + 32:.1f}" y2="{COLLAR}" {_S["dim"]} stroke-dasharray="3 3"/>
<line x1="{x0 + w:.1f}" y1="{y0:.1f}" x2="{x0 + w + 32:.1f}" y2="{y0:.1f}" {_S["dim"]} stroke-dasharray="3 3"/>
<text x="{x0 + w + 34:.1f}" y="135" {_S["txts"]}>{L["d_collar"]}</text>
<line x1="{x0:.1f}" y1="{y0 + h + 18:.1f}" x2="{x0 + w:.1f}" y2="{y0 + h + 18:.1f}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<text x="{cx}" y="{y0 + h + 38:.1f}" {_S["txt"]} text-anchor="middle">9 &times; 10 cm</text>
<text x="300" y="612" {_S["txts"]} text-anchor="middle">{L["d_fold"]}</text>
</svg>"""


def large(L):
    w = 25 * CM
    h = w * 1.112
    x0 = FOLD - w / 2
    y0 = COLLAR + 9 * CM
    return f"""<svg viewBox="0 0 600 640" role="img">{_defs()}{_tee()}
<rect x="{x0:.1f}" y="{y0:.1f}" width="{w:.1f}" height="{h:.1f}" rx="4" {_S["box"]}/>
<image href="/images/logo_mark.svg" x="{x0 + 7:.1f}" y="{y0 + 6:.1f}" width="{w - 14:.1f}" height="{h - 12:.1f}"
  preserveAspectRatio="xMidYMid meet"/>
<line x1="{x0 - 30:.1f}" y1="{COLLAR}" x2="{x0 - 30:.1f}" y2="{y0:.1f}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<line x1="{x0 - 36:.1f}" y1="{COLLAR}" x2="{x0:.1f}" y2="{COLLAR}" {_S["dim"]} stroke-dasharray="3 3"/>
<line x1="{x0 - 36:.1f}" y1="{y0:.1f}" x2="{x0:.1f}" y2="{y0:.1f}" {_S["dim"]} stroke-dasharray="3 3"/>
<text x="{x0 - 38:.1f}" y="{y0 - 8:.1f}" {_S["txts"]} text-anchor="end">{L["d_collar2"]}</text>
<line x1="{x0:.1f}" y1="{y0 + h + 18:.1f}" x2="{x0 + w:.1f}" y2="{y0 + h + 18:.1f}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<text x="300" y="{y0 + h + 38:.1f}" {_S["txt"]} text-anchor="middle">25 &times; 28 cm</text>
<text x="300" y="612" {_S["txts"]} text-anchor="middle">{L["d_centred"]}</text>
</svg>"""


# ---------------------------------------------------------------- back


def back(L, contact=True):
    """30 cm across the shoulders, with or without the contact line under the wordmark."""
    w = 30 * CM
    ratio = 0.143 if contact else 0.077
    h = w * ratio
    x0 = FOLD - w / 2
    y0 = COLLAR + 8 * CM
    cm_h = 4.3 if contact else 2.3

    # print box on the garment
    if contact:
        art = _wordmark(FOLD, y0 + h * .48, w * .95, h * .52,
                        contact=L["contact"], csize=h * .26, cy=y0 + h * .93)
    else:
        art = _wordmark(FOLD, y0 + h * .78, w * .95, h * .95)

    # enlarged detail strip
    sx0, sw = 24, 552
    sy0 = 616
    sh = sw * ratio
    if contact:
        detail = _wordmark(300, sy0 + sh * .48, sw * .95, sh * .52,
                           contact=L["contact"], csize=sh * .26, cy=sy0 + sh * .93)
    else:
        detail = _wordmark(300, sy0 + sh * .78, sw * .95, sh * .95)

    vb_h = sy0 + sh + 34
    leaders = (f'<line x1="{x0:.1f}" y1="{y0 + h:.1f}" x2="{sx0}" y2="{sy0}" {_S["lead"]}/>'
               f'<line x1="{x0 + w:.1f}" y1="{y0 + h:.1f}" x2="{sx0 + sw}" y2="{sy0}" {_S["lead"]}/>')
    return f"""<svg viewBox="0 0 600 {vb_h:.0f}" role="img">{_defs()}{leaders}{_tee()}
<rect x="{x0:.1f}" y="{y0:.1f}" width="{w:.1f}" height="{h:.1f}" rx="3" {_S["box"]}/>
{art}
<line x1="{x0 - 30:.1f}" y1="{COLLAR}" x2="{x0 - 30:.1f}" y2="{y0:.1f}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<line x1="{x0 - 36:.1f}" y1="{COLLAR}" x2="{x0:.1f}" y2="{COLLAR}" {_S["dim"]} stroke-dasharray="3 3"/>
<line x1="{x0 - 36:.1f}" y1="{y0:.1f}" x2="{x0:.1f}" y2="{y0:.1f}" {_S["dim"]} stroke-dasharray="3 3"/>
<text x="{x0 - 38:.1f}" y="{y0 - 8:.1f}" {_S["txts"]} text-anchor="end">{L["d_collar3"]}</text>
<line x1="{x0:.1f}" y1="{y0 + h + 20:.1f}" x2="{x0 + w:.1f}" y2="{y0 + h + 20:.1f}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<text x="300" y="{y0 + h + 40:.1f}" {_S["txt"]} text-anchor="middle">30 &times; {cm_h} cm</text>
<text x="300" y="{y0 + h + 60:.1f}" {_S["txts"]} text-anchor="middle">{L["d_back"]}</text>
<rect x="{sx0}" y="{sy0}" width="{sw}" height="{sh:.1f}" rx="4" fill="#0B0B0C" stroke="#303034" stroke-width="1"/>
{detail}
<text x="300" y="{sy0 + sh + 22:.1f}" {_S["txtxs"]} text-anchor="middle">{L["d_enlarged"]}</text>
</svg>"""


# ---------------------------------------------------------------- copy

EN = {
    "contact": "+34 711 027 432  ·  handymanaxarquia.com",
    "d_centre": "≈ 10 cm from fold",
    "d_collar": "≈ 7 cm below collar",
    "d_collar2": "≈ 9 cm below collar",
    "d_collar3": "≈ 8 cm below collar",
    "d_fold": "Wearer's LEFT chest — the right side as the shirt faces you",
    "d_centred": "Centred on the fold line",
    "d_back": "Centred across the shoulders",
    "d_enlarged": "Artwork shown enlarged",
    "h_chest": "Left chest — 9 cm",
    "h_large": "Large front print — 25 cm",
    "h_back1": "Back — wordmark + contact details",
    "h_back2": "Back — wordmark only",
    "c_chest": ("Fold the shirt down the centre to find the line. The centre of the print sits "
                "<b>≈ 10 cm</b> out from the fold, with its top edge <b>≈ 7 cm</b> below the collar seam."),
    "c_large": ("Centred on the fold, top edge <b>≈ 9 cm</b> below the collar seam. Use this "
                "<b>instead of</b> the chest mark, never both."),
    "c_back1": ("The working version — phone number and website read from across a room. "
                "File: <b>HA_Back_Wordmark_Phone_30cm</b>."),
    "c_back2": ("The cleaner version for casual or off-duty shirts. "
                "File: <b>HA_Back_Wordmark_30cm</b>."),
    "note": ("Measurements are for adult M–L. Go up or down about 1 cm per size, and always check the "
             "position on the actual garment before pressing — collar depth varies between brands."),
    "title": "Placement on the garment",
}

ES = {
    "contact": "+34 711 027 432  ·  handymanaxarquia.com",
    "d_centre": "≈ 10 cm del doblez",
    "d_collar": "≈ 7 cm bajo el cuello",
    "d_collar2": "≈ 9 cm bajo el cuello",
    "d_collar3": "≈ 8 cm bajo el cuello",
    "d_fold": "Pecho IZQUIERDO del usuario — el lado derecho visto de frente",
    "d_centred": "Centrado en la línea del doblez",
    "d_back": "Centrado a lo ancho de los hombros",
    "d_enlarged": "Arte ampliado",
    "h_chest": "Pecho izquierdo — 9 cm",
    "h_large": "Estampado grande frontal — 25 cm",
    "h_back1": "Espalda — logotipo + datos de contacto",
    "h_back2": "Espalda — solo logotipo",
    "c_chest": ("Dobla la camiseta por el centro para marcar la línea. El centro del estampado queda "
                "a <b>≈ 10 cm</b> del doblez y su borde superior <b>≈ 7 cm</b> bajo la costura del cuello."),
    "c_large": ("Centrado en el doblez, borde superior <b>≈ 9 cm</b> bajo la costura del cuello. Se usa "
                "<b>en lugar</b> del emblema del pecho, nunca los dos."),
    "c_back1": ("La versión de trabajo: el teléfono y la web se leen a distancia. "
                "Archivo: <b>HA_Back_Wordmark_Phone_30cm</b>."),
    "c_back2": ("La versión más limpia, para camisetas de uso casual. "
                "Archivo: <b>HA_Back_Wordmark_30cm</b>."),
    "note": ("Medidas para tallas M–L de adulto. Ajusta ≈ 1 cm por talla y comprueba siempre la posición "
             "sobre la prenda real antes de planchar — la profundidad del cuello varía entre marcas."),
    "title": "Colocación en la prenda",
}


def _fig(svg, heading, caption):
    return f'<figure>{svg}<figcaption>{heading}</figcaption><div class="cap2">{caption}</div></figure>'


def block(side, code):
    L = EN if code == "en" else ES
    if side == "front":
        figs = (_fig(chest(L), L["h_chest"], L["c_chest"])
                + _fig(large(L), L["h_large"], L["c_large"]))
    else:
        figs = (_fig(back(L, True), L["h_back1"], L["c_back1"])
                + _fig(back(L, False), L["h_back2"], L["c_back2"]))
    on = ' class="on"' if code == "en" else ""
    return (f'<div data-lang="{code}"{on}>'
            f'<div class="spec-h" style="margin:34px 0 14px">{L["title"]}</div>'
            f'<div class="plc">{figs}</div>'
            f'<div class="spec-note">{L["note"]}</div></div>')
