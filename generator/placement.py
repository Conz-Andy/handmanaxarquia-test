# Print-placement diagrams for the t-shirt spec pages: a flat t-shirt outline with
# the print area, the centre fold, and dimensioned callouts. Bilingual labels.

TEE = ("M 212,52 C 212,52 192,46 176,54 L 88,98 L 52,180 L 120,214 L 152,162 "
       "L 152,566 L 448,566 L 448,162 L 480,214 L 548,180 L 512,98 L 424,54 "
       "C 408,46 388,52 388,52 C 383,88 352,108 300,108 C 248,108 217,88 212,52 Z")

CSS = """
.plc { display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:16px; }
.plc.one { grid-template-columns:minmax(0,470px); }
.plc figure { background:#1a1a1d; border:1px solid #303034; border-radius:14px; padding:16px 16px 14px; }
.plc svg { width:100%; height:auto; display:block; }
.plc figcaption { color:#fff; font-size:.85rem; font-weight:600; margin-top:10px; }
.plc .cap2 { color:#9a9aa0; font-size:.73rem; line-height:1.7; margin-top:4px; }
.plc .cap2 b { color:#d6d6da; font-weight:500; }
"""

_S = {  # svg style fragments
    "tee": 'fill="#141417" stroke="#3f3f45" stroke-width="2"',
    "collar": 'fill="none" stroke="#3f3f45" stroke-width="2"',
    "fold": 'stroke="#FBA917" stroke-width="1.5" stroke-dasharray="7 7" opacity=".45"',
    "box": 'fill="rgba(251,169,23,.07)" stroke="#FBA917" stroke-width="1.6" stroke-dasharray="5 4"',
    "dim": 'stroke="#8E8E93" stroke-width="1.2"',
    "txt": 'fill="#d6d6da" font-family="Poppins,sans-serif" font-size="15"',
    "txts": 'fill="#8E8E93" font-family="Poppins,sans-serif" font-size="13"',
}


def _arrow_defs():
    return ('<defs><marker id="a" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">'
            '<path d="M0,0 L7,3.5 L0,7 z" fill="#8E8E93"/></marker>'
            '<marker id="b" markerWidth="7" markerHeight="7" refX="1" refY="3.5" orient="auto">'
            '<path d="M7,0 L0,3.5 L7,7 z" fill="#8E8E93"/></marker></defs>')


def _tee_base():
    return (f'<path d="{TEE}" {_S["tee"]}/>'
            f'<path d="M 212,52 C 217,88 248,108 300,108 C 352,108 383,88 388,52" {_S["collar"]}/>'
            f'<line x1="300" y1="112" x2="300" y2="566" {_S["fold"]}/>')


def chest(L):
    """Left-chest mark. Wearer's left = the right-hand side of the flat garment."""
    x0, y0, w, h = 332, 156, 56, 62
    cx = x0 + w / 2
    return f"""<svg viewBox="0 0 600 620" role="img">{_arrow_defs()}{_tee_base()}
<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="4" {_S["box"]}/>
<image href="/images/logo_mark.svg" x="{x0 + 5}" y="{y0 + 4}" width="{w - 10}" height="{h - 8}"
  preserveAspectRatio="xMidYMid meet"/>
<line x1="{cx}" y1="134" x2="{cx}" y2="{y0}" {_S["dim"]} stroke-dasharray="3 3"/>
<line x1="300" y1="134" x2="{cx}" y2="134" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<text x="{cx}" y="120" {_S["txts"]} text-anchor="middle">{L["d_centre"]}</text>
<line x1="{x0 + w + 26}" y1="108" x2="{x0 + w + 26}" y2="{y0}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<line x1="{x0 + w}" y1="108" x2="{x0 + w + 32}" y2="108" {_S["dim"]} stroke-dasharray="3 3"/>
<line x1="{x0 + w}" y1="{y0}" x2="{x0 + w + 32}" y2="{y0}" {_S["dim"]} stroke-dasharray="3 3"/>
<text x="{x0 + w + 34}" y="137" {_S["txts"]}>{L["d_collar"]}</text>
<line x1="{x0}" y1="{y0 + h + 18}" x2="{x0 + w}" y2="{y0 + h + 18}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<text x="{cx}" y="{y0 + h + 38}" {_S["txt"]} text-anchor="middle">9 cm</text>
<text x="300" y="600" {_S["txts"]} text-anchor="middle">{L["d_fold"]}</text>
</svg>"""


def large(L):
    w, h = 148, 165
    x0, y0 = 300 - w / 2, 162
    return f"""<svg viewBox="0 0 600 620" role="img">{_arrow_defs()}{_tee_base()}
<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="4" {_S["box"]}/>
<image href="/images/logo_mark.svg" x="{x0 + 8}" y="{y0 + 8}" width="{w - 16}" height="{h - 16}"
  preserveAspectRatio="xMidYMid meet"/>
<line x1="{x0 - 30}" y1="108" x2="{x0 - 30}" y2="{y0}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<line x1="{x0 - 36}" y1="108" x2="{x0}" y2="108" {_S["dim"]} stroke-dasharray="3 3"/>
<line x1="{x0 - 36}" y1="{y0}" x2="{x0}" y2="{y0}" {_S["dim"]} stroke-dasharray="3 3"/>
<text x="{x0 - 38}" y="{y0 - 8}" {_S["txts"]} text-anchor="end">{L["d_collar2"]}</text>
<line x1="{x0}" y1="{y0 + h + 18}" x2="{x0 + w}" y2="{y0 + h + 18}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<text x="300" y="{y0 + h + 38}" {_S["txt"]} text-anchor="middle">25 cm</text>
<text x="300" y="600" {_S["txts"]} text-anchor="middle">{L["d_centred"]}</text>
</svg>"""


def back(L):
    w, h = 250, 46
    x0, y0 = 300 - w / 2, 158
    return f"""<svg viewBox="0 0 600 620" role="img">{_arrow_defs()}{_tee_base()}
<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="4" {_S["box"]}/>
<text x="300" y="{y0 + 30}" text-anchor="middle" font-family="Poppins,sans-serif"
  font-size="21" font-weight="700" letter-spacing="1.5"><tspan fill="#ffffff">HANDYMAN</tspan> <tspan fill="#FBA917">AXARQUIA</tspan></text>
<line x1="{x0 - 26}" y1="108" x2="{x0 - 26}" y2="{y0}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<text x="{x0 - 34}" y="{y0 - 18}" {_S["txts"]} text-anchor="end">{L["d_collar3"]}</text>
<line x1="{x0}" y1="{y0 + h + 18}" x2="{x0 + w}" y2="{y0 + h + 18}" {_S["dim"]} marker-start="url(#b)" marker-end="url(#a)"/>
<text x="300" y="{y0 + h + 36}" {_S["txt"]} text-anchor="middle">30 cm</text>
<text x="300" y="600" {_S["txts"]} text-anchor="middle">{L["d_back"]}</text>
</svg>"""


EN = {
    "d_centre": "≈ 10 cm from fold",
    "d_collar": "≈ 7 cm below collar",
    "d_collar2": "≈ 9 cm below collar",
    "d_collar3": "≈ 8 cm below collar",
    "d_fold": "Wearer's LEFT chest — the right side as the shirt faces you",
    "d_centred": "Centred on the fold line",
    "d_back": "Centred across the shoulders",
    "h_chest": "Left chest — 9 cm",
    "h_large": "Large front print — 25 cm",
    "h_back": "Back print — 30 cm",
    "c_chest": ("Fold the shirt down the centre to find the line. Measure <b>≈ 10 cm</b> out from the "
                "fold and <b>≈ 7 cm</b> down from the collar seam — that is the top-left corner of the print."),
    "c_large": ("Centred on the fold, top edge <b>≈ 9 cm</b> below the collar seam. Use this "
                "<b>instead of</b> the chest mark, never both."),
    "c_back": ("Centred across the shoulders, top edge <b>≈ 8 cm</b> below the collar seam."),
    "note": ("Measurements are for adult M–L. Go up or down about 1 cm per size, and always check the "
             "position on the actual garment before pressing — collar depth varies between brands."),
    "title": "Placement on the garment",
}

ES = {
    "d_centre": "≈ 10 cm del doblez",
    "d_collar": "≈ 7 cm bajo el cuello",
    "d_collar2": "≈ 9 cm bajo el cuello",
    "d_collar3": "≈ 8 cm bajo el cuello",
    "d_fold": "Pecho IZQUIERDO del usuario — el lado derecho visto de frente",
    "d_centred": "Centrado en la línea del doblez",
    "d_back": "Centrado a lo ancho de los hombros",
    "h_chest": "Pecho izquierdo — 9 cm",
    "h_large": "Estampado grande frontal — 25 cm",
    "h_back": "Estampado trasero — 30 cm",
    "c_chest": ("Dobla la camiseta por el centro para marcar la línea. Mide <b>≈ 10 cm</b> desde el "
                "doblez y <b>≈ 7 cm</b> bajo la costura del cuello: ahí va la esquina superior izquierda."),
    "c_large": ("Centrado en el doblez, borde superior <b>≈ 9 cm</b> bajo la costura del cuello. Se usa "
                "<b>en lugar</b> del emblema del pecho, nunca los dos."),
    "c_back": ("Centrado a lo ancho de los hombros, borde superior <b>≈ 8 cm</b> bajo la costura del cuello."),
    "note": ("Medidas para tallas M–L de adulto. Ajusta ≈ 1 cm por talla y comprueba siempre la posición "
             "sobre la prenda real antes de planchar — la profundidad del cuello varía entre marcas."),
    "title": "Colocación en la prenda",
}


def _fig(svg, heading, caption):
    return f'<figure>{svg}<figcaption>{heading}</figcaption><div class="cap2">{caption}</div></figure>'


def block(side, code):
    L = EN if code == "en" else ES
    one = ""
    if side == "front":
        figs = (_fig(chest(L), L["h_chest"], L["c_chest"])
                + _fig(large(L), L["h_large"], L["c_large"]))
    else:
        figs = _fig(back(L), L["h_back"], L["c_back"])
        one = " one"
    on = ' class="on"' if code == "en" else ""
    return (f'<div data-lang="{code}"{on}>'
            f'<div class="spec-h" style="margin:34px 0 14px">{L["title"]}</div>'
            f'<div class="plc{one}">{figs}</div>'
            f'<div class="spec-note">{L["note"]}</div></div>')
