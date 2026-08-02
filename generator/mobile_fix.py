# Mobile polish for the /brand/ hub: scale A4 documents to phone width,
# restack the admin bar on small screens. Injected into generated brand pages.
from pathlib import Path

A4_FIT = """<script>
function fitA4() {
  var p = document.querySelector('.page');
  if (!p) return;
  var z = Math.min(1, (window.innerWidth - 12) / 800);
  p.style.zoom = z;
}
window.addEventListener('resize', fitA4);
window.addEventListener('load', fitA4);
fitA4();
</script>"""

HUB_MOBILE_CSS = """<style>
@media (max-width: 720px) {
  .adminbar { gap: 10px; padding: 10px 12px; }
  .adminbar .tag { display: none; }
  .adminbar b { font-size: .85rem; }
  .adminbar select { min-width: 0; flex: 1 1 100%; order: 3; }
  .adminbar .actions { margin-left: 0; order: 4; width: 100%; }
  .adminbar .actions a, .adminbar .actions button { flex: 1; text-align: center; }
}
</style>"""

DOC_PAGES = ("invoice", "quotation", "letterhead", "presupuesto")
STAGE_PAGES = ("card-front", "card-back", "tshirt-front", "tshirt-back")

STAGE_FIT = """<style>.stage{transform:none !important}</style><script>
var _w0 = null;
function fitStage() {
  var s = document.querySelector('.stage');
  if (!s) return;
  if (_w0 === null) _w0 = s.offsetWidth;
  s.style.zoom = Math.min(1, (window.innerWidth - 16) / _w0);
}
window.addEventListener('resize', fitStage);
window.addEventListener('load', fitStage);
fitStage();
</script>"""

def apply(site: Path):
    brand = site / "brand"
    if not brand.exists():
        return
    for name in DOC_PAGES:
        f = brand / name / "index.html"
        if f.exists():
            h = f.read_text()
            if "fitA4" not in h:
                f.write_text(h.replace("</body>", A4_FIT + "</body>"))
    for name in STAGE_PAGES:
        f = brand / name / "index.html"
        if f.exists():
            h = f.read_text()
            if "fitStage" not in h:
                f.write_text(h.replace("</body>", STAGE_FIT + "</body>"))
    hub = brand / "index.html"
    if hub.exists():
        h = hub.read_text()
        if "max-width: 720px" not in h:
            hub.write_text(h.replace("</head>", HUB_MOBILE_CSS + "</head>"))
    print("mobile fixes applied")
