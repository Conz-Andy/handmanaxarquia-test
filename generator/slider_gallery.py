# Before/after comparison-slider gallery (drag the handle to sweep between photos).
from content_en import GALLERY_PAIRS, u
from helpers import cta_band

STYLE = """<style>
.ba-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 26px; }
.ba-card { background: #fff; border: 1px solid var(--line); border-radius: var(--radius); overflow: hidden; }
.ba-card h3 { font-size: .96rem; font-weight: 600; padding: 14px 18px; }
.cmp { position: relative; aspect-ratio: 16/10; overflow: hidden; background: var(--panel); --p: 50%; }
.cmp img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; }
.cmp .cmp-before { clip-path: inset(0 calc(100% - var(--p)) 0 0); }
.cmp-handle {
  position: absolute; top: 0; bottom: 0; left: var(--p); width: 3px;
  background: var(--orange); transform: translateX(-50%); pointer-events: none;
}
.cmp-handle::after {
  content: "\\2194"; position: absolute; top: 50%; left: 50%;
  transform: translate(-50%, -50%); width: 40px; height: 40px; border-radius: 50%;
  background: var(--orange); color: var(--black); font-size: 19px; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 4px 14px rgba(0,0,0,.35);
}
.cmp input[type=range] {
  position: absolute; inset: 0; width: 100%; height: 100%;
  opacity: 0; cursor: ew-resize; margin: 0; -webkit-appearance: none; appearance: none;
}
.cmp-tag {
  position: absolute; top: 12px; font-size: .68rem; font-weight: 700;
  letter-spacing: 1.5px; text-transform: uppercase; padding: 4px 10px;
  border-radius: 999px; pointer-events: none;
}
.cmp-tag-b { left: 12px; background: rgba(11,11,12,.82); color: #fff; }
.cmp-tag-a { right: 12px; background: var(--orange); color: var(--black); }
@media (max-width: 700px) { .ba-grid { grid-template-columns: 1fr; } }
</style>"""

SCRIPT = """<script>
document.querySelectorAll('[data-cmp]').forEach(function (c) {
  var r = c.querySelector('input[type=range]');
  function set() { c.style.setProperty('--p', r.value + '%'); }
  r.addEventListener('input', set);
  set();
});
</script>"""

def gallery_body_slider(lang, ui):
    en = lang == "en"
    title = "Our work — before & after" if en else "Våra arbeten — före & efter"
    sub = ("Real projects across the Axarquia. Drag the orange handle on each photo to sweep between before and after."
           if en else
           "Verkliga projekt i Axarquía. Dra i det orange handtaget på varje bild för att växla mellan före och efter.")
    lb, la = ("Before", "After") if en else ("Före", "Efter")
    cards = "".join(f"""<div class="ba-card">
  <div class="cmp" data-cmp>
    <img src="{a}" alt="{la}: {cap_en if en else cap_sv}" loading="lazy">
    <img class="cmp-before" src="{b}" alt="{lb}: {cap_en if en else cap_sv}" loading="lazy">
    <div class="cmp-handle"></div>
    <span class="cmp-tag cmp-tag-b">{lb}</span>
    <span class="cmp-tag cmp-tag-a">{la}</span>
    <input type="range" min="2" max="98" value="50" aria-label="{'Compare before and after' if en else 'Jämför före och efter'}">
  </div>
  <h3>{cap_en if en else cap_sv}</h3>
</div>""" for b, a, cap_en, cap_sv in GALLERY_PAIRS[:6])
    return f"""{STYLE}<div class="page-hero"><div class="container">
  <h1>{title}</h1>
  <p class="lead">{sub}</p>
</div></div>
<section><div class="container">
  <div class="ba-grid">{cards}</div>
</div></section>
{SCRIPT}
{cta_band(lang, ui, u)}"""
