# Before/after gallery photo pairs: (before_src, after_src, caption_en, caption_sv).
# Files live in assets_b64/gallery/ as split base64 parts (2026__08__*.b64.partNN)
# and are decoded into site/wp-content/uploads/2026/08/ at build time.
_G = "/wp-content/uploads/2026/08"
GALLERY_PAIRS = [
    (f"{_G}/handyman-axarquia-terrace-planters-before.webp",
     f"{_G}/handyman-axarquia-terrace-planters-after.webp",
     "Roof terrace reform — planters & decorative tiling", "Takterrass — planteringskärl & dekorplattor"),
    (f"{_G}/handyman-axarquia-bathroom-reform-1-before.webp",
     f"{_G}/handyman-axarquia-bathroom-reform-1-after.webp",
     "Full bathroom renovation", "Komplett badrumsrenovering"),
    (f"{_G}/handyman-axarquia-kitchen-reform-open-before.webp",
     f"{_G}/handyman-axarquia-kitchen-reform-open-after.webp",
     "Open-plan kitchen reform", "Kök i öppen planlösning"),
    (f"{_G}/handyman-axarquia-courtyard-lighting-before.webp",
     f"{_G}/handyman-axarquia-courtyard-lighting-after.webp",
     "Courtyard reform with lighting & glass floor", "Innergård med belysning & glasgolv"),
    (f"{_G}/handyman-axarquia-bathroom-reform-2-before.webp",
     f"{_G}/handyman-axarquia-bathroom-reform-2-after.webp",
     "Bathroom renovation with double vanity", "Badrumsrenovering med dubbelt handfat"),
    (f"{_G}/handyman-axarquia-kitchen-reform-arch-before.webp",
     f"{_G}/handyman-axarquia-kitchen-reform-arch-after.webp",
     "Kitchen renovation", "Köksrenovering"),
    (f"{_G}/handyman-axarquia-livingroom-logburner-before.webp",
     f"{_G}/handyman-axarquia-livingroom-logburner-after.webp",
     "Chimney removal & log burner installation", "Rivning av öppen spis & installation av braskamin"),
    (f"{_G}/handyman-axarquia-pergola-vinuela-before.webp",
     f"{_G}/handyman-axarquia-pergola-vinuela-after.webp",
     "Pergola & printed-concrete driveway, Viñuela", "Pergola & mönstergjuten uppfart, Viñuela"),
]
