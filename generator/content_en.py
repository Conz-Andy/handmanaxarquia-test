# English content for handymanaxarquia.com
from helpers import make_url_fn, service_body, cta_band, SERVICE_ORDER

SV_SLUGS = {"reforms": "renoveringar", "plastering": "putsarbeten", "extensions": "tillbyggnader",
            "tiling": "kakel", "bathrooms": "badrum", "kitchens": "kok",
            "gallery": "galleri", "contact": "kontakt"}
u = make_url_fn(SV_SLUGS)

UI = {
    "nav_home": "Home", "nav_services": "Services", "nav_gallery": "Gallery", "nav_contact": "Contact",
    "services_names": {
        "reforms": "Reforms & Renovations", "plastering": "Plastering & Rendering",
        "extensions": "Extensions", "tiling": "Tiling",
        "bathrooms": "Bathroom Renovations", "kitchens": "Kitchen Renovations",
    },
    "aside_title": "Get a free quote",
    "aside_blurb": "Tell us about your project and we'll get back to you the same day with a no-obligation estimate.",
    "aside_wa": "Message us on WhatsApp",
    "aside_terms": "Free quotes · 50% deposit to book, balance on completion · 12-month workmanship guarantee.",
    "faq_title": "Frequently asked questions",
    "cta_h": "Ready to start your project? <em>Let's talk.</em>",
    "cta_p": "Free, no-obligation quotes across the Axarquia. Call, WhatsApp or send us a message — we answer the same day.",
    "cta_btn": "Request a free quote",
    "foot_blurb": "Professional building, renovation and property care across the Axarquia and eastern Costa del Sol. Over 35 years of experience, always on time and on budget.",
    "foot_areas": "Areas we cover: Torre del Mar, Vélez-Málaga, Algarrobo, Caleta de Vélez, Almayate, Nerja, Torrox, Frigiliana, Cómpeta, Viñuela and Rincón de la Victoria.",
    "foot_pages": "Pages",
    "foot_rights": "All rights reserved.",
    "spain": "Spain",
}

# ---------------------------------------------------------------- service pages

REFORMS_PROSE = """
<h2>Complete and partial property reforms</h2>
<p>Whether you have just bought a townhouse in Vélez-Málaga that needs bringing up to date, or your holiday apartment in Torre del Mar is ready for a new look, we manage the whole reform from first sketch to final clean. One team, one point of contact, one agreed price — no chasing separate trades across the Axarquia.</p>
<ul class="tick">
<li>Full property reforms — strip-out, layout changes, new installations and finishes</li>
<li>Partial reforms — update a floor, a facade, a terrace or a single room</li>
<li>Structural work — wall removals with proper beams and supports</li>
<li>New plumbing and electrics brought up to current Spanish regulations</li>
<li>Damp treatment, insulation and window replacement</li>
<li>Painting, flooring, carpentry and all finishing trades</li>
</ul>
<h2>How we work</h2>
<p>Every reform starts with a free visit and a free written quotation with no obligation. We ask for a 50% deposit to schedule the work and order materials; the balance is only due when the job is finished and you are happy. Unforeseen issues — and older Spanish properties do like to hide them — are always priced and agreed in writing before we carry on.</p>
<p>We are used to working for owners who are not in Spain full-time. Many of our clients in Nerja, Torrox and the villages of the Axarquia follow their reform through weekly photo updates on WhatsApp, and come back to a finished, cleaned property.</p>
<h2>Reforms across the Axarquia</h2>
<p>Based in Almayate, we carry out reforms in Torre del Mar, Vélez-Málaga, Nerja, Torrox, Caleta de Vélez, Algarrobo, Frigiliana, Cómpeta, Viñuela, Rincón de la Victoria and throughout the Axarquia region. Country properties and cortijos are welcome — we know the access, water and power challenges that come with them.</p>
"""

PLASTERING_PROSE = """
<h2>Plastering, skimming and rendering</h2>
<p>Good plastering is the difference between a paint job that looks flat and walls that look new. We plaster interiors, render exteriors and repair the cracked, blown or damp-damaged surfaces that are so common in coastal Spanish properties.</p>
<ul class="tick">
<li>Internal plastering and skimming — smooth finishes ready for paint</li>
<li>Gotelé removal — say goodbye to textured walls, hello to clean modern surfaces</li>
<li>Exterior render — traditional and monocapa render, applied or repaired</li>
<li>Crack and blown-render repairs on facades and boundary walls</li>
<li>Damp-affected plaster removed, walls treated and re-plastered properly</li>
<li>Decorative finishes and arch/edge detailing</li>
</ul>
<h2>The coastal damp problem</h2>
<p>Properties in Torre del Mar, Almayate and along the coast take a beating from salt air and winter humidity. Painting over damp plaster only hides the problem for a season. We take the affected plaster back to the wall, treat the cause — rising damp, bridged render, failed pointing — and re-plaster with the right breathable materials so the repair lasts.</p>
<h2>Tidy, dust-controlled work</h2>
<p>Plastering is messy work, but your home doesn't have to be. Floors and furniture are sheeted, rooms are sealed while we work, and we leave every space clean. Most single rooms are skimmed and ready for paint within two to three days.</p>
"""

EXTENSIONS_PROSE = """
<h2>House extensions and new build works</h2>
<p>Need more space? An extra bedroom for visiting family, a bigger kitchen, a covered terrace for year-round outdoor living — an extension is often far better value than moving. We build extensions across the Axarquia, handling everything from foundations to the final coat of paint.</p>
<ul class="tick">
<li>Single-storey extensions and annexes</li>
<li>Covered terraces, porches and pergolas</li>
<li>Garage and storeroom conversions into living space</li>
<li>Outdoor kitchens and barbecue areas</li>
<li>Pool houses and casitas</li>
<li>Roof terraces and solariums</li>
</ul>
<h2>Licences and paperwork</h2>
<p>Building work in Spain needs the right licence — a licencia de obra menor for smaller projects or obra mayor with an architect's project for structural extensions. We work alongside local architects and the town halls in Vélez-Málaga, Torrox and Nerja, and we'll tell you honestly at the quote stage what permissions your project needs and what they typically cost. No surprises halfway through.</p>
<h2>Built for the climate</h2>
<p>An extension on the Costa del Sol has to handle fierce summer sun and driving winter rain. We build with proper insulation, damp-proofing and shading from the start, so your new space is usable in August and in January alike.</p>
"""

TILING_PROSE = """
<h2>Floor and wall tiling</h2>
<p>Tiling is the finish you see and touch every day, and it is unforgiving of shortcuts — lippage, uneven grout lines and hollow tiles announce themselves for years. Our tilers set out every job properly, cut cleanly and level precisely, whether it's a bathroom splashback or two hundred square metres of terrace.</p>
<ul class="tick">
<li>Interior floor tiling — porcelain, ceramic and natural stone</li>
<li>Wall tiling for bathrooms, kitchens and feature walls</li>
<li>Terrace and pool-surround tiling with anti-slip and frost-rated tiles</li>
<li>Large-format tiles and level-entry wet rooms</li>
<li>Repairs — re-fixing hollow or cracked tiles, re-grouting and sealing</li>
<li>Waterproofing (impermeabilización) beneath terraces and wet areas</li>
</ul>
<h2>Terraces that don't leak</h2>
<p>A huge share of the leaks we repair in the Axarquia start with a terrace tiled straight onto old surfaces with no membrane. We waterproof first, then tile, with the correct falls and expansion joints, so water goes to the drain instead of into the bedroom below.</p>
<h2>Supply or labour-only</h2>
<p>Choose your own tiles from any local supplier — we're happy to recommend showrooms in Torre del Mar and Vélez-Málaga — or tell us the look you want and we'll source options within your budget. Either way you get a clear written quote for the job.</p>
"""

BATHROOMS_PROSE = """
<h2>Complete bathroom renovations</h2>
<p>A dated bathroom drags a whole property down — and in rental homes it's the first thing guests photograph. We renovate bathrooms across the Axarquia from strip-out to silicone: plumbing, electrics, waterproofing, tiling, fittings and finishing, all by one team on one schedule.</p>
<ul class="tick">
<li>Full bathroom refits, typically completed in one to two weeks</li>
<li>Bath-to-shower conversions and walk-in showers</li>
<li>Level-access wet rooms — ideal for accessibility and small spaces</li>
<li>New sanitaryware, vanity units, mirrors and heated towel rails</li>
<li>Proper tanking/waterproofing before a single tile goes on</li>
<li>Ventilation to keep mould away for good</li>
</ul>
<h2>Designed around real use</h2>
<p>Holiday home, rental property or full-time residence — each needs different choices. Rentals need robust, easy-clean surfaces and fittings that survive guests; retirement homes benefit from level access and grab-rail-ready walls. We'll advise on what actually works, not just what looks good in a showroom.</p>
<h2>A clear, fixed process</h2>
<p>You get a written quote, a start date and a realistic duration. We protect the rest of your home, manage our own waste, and keep water off for the shortest time possible — usually you're never without a working bathroom overnight when the property has a second one.</p>
"""

KITCHENS_PROSE = """
<h2>Kitchen renovations and refits</h2>
<p>The kitchen is where budgets are won and lost. We renovate kitchens across the Axarquia with one team handling demolition, plumbing, electrics, plastering, tiling and installation — so the units, worktop and appliances all arrive at a room that is actually ready for them.</p>
<ul class="tick">
<li>Complete kitchen strip-out and refit</li>
<li>Layout changes — walls moved, islands added, open-plan conversions</li>
<li>New electrics with enough circuits for modern appliances</li>
<li>Plumbing for sinks, dishwashers, water filters and gas hobs</li>
<li>Tiled or stone splashbacks and hard-wearing floors</li>
<li>Fitting kitchens supplied by any retailer — or sourced by us</li>
</ul>
<h2>Bring your own kitchen, or let us source it</h2>
<p>Many clients buy their units from national suppliers or local kitchen studios in Vélez-Málaga and have us do everything else: preparation, first-fix, installation and finishing. Others hand us a budget and a photo. Both work — the quote will always show exactly what is included.</p>
<h2>Open-plan living</h2>
<p>The most requested job in Spanish townhouses and apartments: removing the wall between a closed kitchen and the living room. Done properly — with structural assessment, a correctly sized beam and a licence where required — it transforms how a property lives and how it values.</p>
"""

def _svc(key, title, desc, h1, lead, prose, faqs):
    return {"key": key, "title": title, "desc": desc, "h1": h1, "lead": lead,
            "prose": prose, "faqs": faqs}

SERVICES = {
"reforms": _svc("reforms",
    "Property Reforms in the Axarquia | Handyman Axarquia",
    "Complete and partial property reforms in Torre del Mar, Vélez-Málaga, Nerja and across the Axarquia. One team, free written quotes, 12-month guarantee. Free quotes.",
    "Property reforms in the Axarquia, done properly",
    "Full and partial reforms for apartments, townhouses and country properties — managed end to end by one experienced team on the eastern Costa del Sol.",
    REFORMS_PROSE,
    [("How much does a property reform cost in the Axarquia?",
      "It depends on scope and finish, but as a guide: a light cosmetic reform (paint, floors, doors) starts from a few thousand euros per room, while full reforms of apartments typically run from €600–€1,000 per square metre. Every quote we give is in writing so you can adjust the scope to your budget."),
     ("How long does a full reform take?",
      "A one-bedroom apartment reform typically takes 4–6 weeks; a full townhouse 2–4 months depending on structural work. You get a schedule with the quote and weekly progress updates."),
     ("Can you manage the reform while I'm not in Spain?",
      "Yes — most of our clients are abroad for some or all of the project. We send weekly photo and video updates by WhatsApp or email and handle keys, deliveries and tradespeople."),
     ("Do I need a licence for a reform?",
      "Cosmetic reforms usually need a simple licencia de obra menor from the town hall; structural changes need more. We advise what applies at the quote stage and can handle the application.")]),

"plastering": _svc("plastering",
    "Plastering & Rendering Axarquia | Handyman Axarquia",
    "Internal plastering, skimming, gotelé removal and exterior rendering in Torre del Mar, Vélez-Málaga, Nerja and the Axarquia. Damp repairs done properly. Free quotes.",
    "Plastering and rendering across the Axarquia",
    "Smooth internal plastering, exterior render and lasting damp repairs for coastal and country properties on the eastern Costa del Sol.",
    PLASTERING_PROSE,
    [("Can you remove gotelé (textured paint) walls?",
      "Yes — gotelé removal and re-skimming is one of our most requested jobs. Depending on the type, we either soak and scrape or skim directly over with plaster, leaving walls smooth and ready for modern paint."),
     ("How do you deal with damp walls?",
      "We never just plaster over damp. We strip back the affected area, identify the cause — rising damp, failed exterior render, condensation — treat it, then re-plaster with breathable materials appropriate for the wall."),
     ("How soon can I paint over new plaster?",
      "In the Axarquia climate, skimmed walls are usually dry enough for a mist coat in 3–7 days depending on season and thickness. We'll tell you the safe date when we finish."),
     ("Do you do small plastering repairs?",
      "Yes. Cracks, blown patches, holes after electrical work — no job is too small, and small repairs are usually done in a single visit.")]),

"extensions": _svc("extensions",
    "House Extensions in the Axarquia | Handyman Axarquia",
    "Home extensions, covered terraces, garage conversions and casitas in Torre del Mar, Vélez-Málaga, Nerja and the Axarquia. Licence guidance included. Free quotes.",
    "House extensions on the eastern Costa del Sol",
    "From covered terraces to full extra rooms — designed for the climate, built to regulation, and priced clearly before we start.",
    EXTENSIONS_PROSE,
    [("Do I need planning permission for an extension in Spain?",
      "Almost always, yes. Smaller works may fall under a licencia de obra menor, but anything structural or that increases built area needs an obra mayor with an architect's project. We guide you through what your town hall requires and work with local architects."),
     ("How much does an extension cost per square metre?",
      "As a guide, straightforward single-storey extensions in the Axarquia typically run from €1,000–€1,600 per square metre including finishes, plus architect and licence fees. Covered terraces and porches cost significantly less."),
     ("Can you convert my garage or storeroom into a bedroom?",
      "Usually yes, and it's one of the most cost-effective ways to gain space. We handle insulation, damp-proofing, ventilation, electrics and finishes, and advise on the legalisation paperwork."),
     ("How long does an extension take?",
      "A covered terrace or porch: 1–3 weeks. A single room extension: 6–10 weeks including drying times. We give you a written schedule with the quote.")]),

"tiling": _svc("tiling",
    "Tiling Services in the Axarquia | Handyman Axarquia",
    "Professional floor, wall, bathroom and terrace tiling in Torre del Mar, Vélez-Málaga, Nerja and the Axarquia. Waterproofing done right. Free quotes.",
    "Professional tiling in the Axarquia",
    "Floors, walls, bathrooms, kitchens and terraces — set out properly, cut cleanly and sealed to last, anywhere on the eastern Costa del Sol.",
    TILING_PROSE,
    [("How much does tiling cost per square metre?",
      "Every tiling job is priced individually — tile prices vary enormously, and the format, the condition of the surface and the amount of preparation and cutting all affect the cost. Tell us the size of the area and the tiles you have in mind and we'll give you a free written quote."),
     ("My terrace leaks into the room below — can tiling fix it?",
      "Tiles alone don't waterproof anything. We strip back, apply a proper waterproof membrane with correct falls, then tile. That combination fixes the leak permanently — it's one of our most common jobs."),
     ("Can you tile over existing tiles?",
      "Sometimes, if the base is sound and heights allow. It saves money and mess, but isn't always the right call — we'll assess and give you both options with prices."),
     ("Do you supply tiles or do I buy my own?",
      "Either. Many clients choose tiles themselves in local showrooms; we're happy to collect, or to source options to a budget and bring samples.")]),

"bathrooms": _svc("bathrooms",
    "Bathroom Renovations Axarquia | Handyman Axarquia",
    "Complete bathroom renovations, walk-in showers and wet rooms in Torre del Mar, Vélez-Málaga, Nerja and the Axarquia. One team, fixed quotes, 12-month guarantee.",
    "Bathroom renovations in the Axarquia",
    "Strip-out to silicone in one to two weeks — plumbing, waterproofing, tiling and fitting by one team, with a written fixed quote.",
    BATHROOMS_PROSE,
    [("How much does a bathroom renovation cost?",
      "A complete standard-size bathroom refit in the Axarquia typically runs €4,500–€9,000 depending on fittings and tiles, with wet rooms and premium finishes above that. You get a free written quote before we start, so you can adjust choices to budget."),
     ("How long will I be without a bathroom?",
      "A typical full refit takes 7–12 working days. Water is only off for short periods, and where the property has a second bathroom you'll never be without one overnight."),
     ("Can you convert my bath to a walk-in shower?",
      "Yes — it's our most requested bathroom job. Including new tray, screen, tiling and plumbing, most conversions take 3–5 days."),
     ("Do you waterproof before tiling?",
      "Always. Wet zones are tanked with a waterproof membrane before any tile goes on. It's invisible when finished, and it's the difference between a bathroom that lasts and one that leaks into the flat below.")]),

"kitchens": _svc("kitchens",
    "Kitchen Renovations Axarquia | Handyman Axarquia",
    "Kitchen renovations and refits in Torre del Mar, Vélez-Málaga, Nerja and the Axarquia — open-plan conversions, electrics, plumbing, tiling and installation.",
    "Kitchen renovations in the Axarquia",
    "One team for the whole job — strip-out, walls, electrics, plumbing, tiling and installation — whether you supply the kitchen or we do.",
    KITCHENS_PROSE,
    [("How much does a kitchen renovation cost?",
      "Preparation and installation work (everything except the units and appliances) typically runs €3,000–€7,000 depending on layout changes and finishes. With mid-range units included, complete kitchens in the Axarquia usually land between €8,000 and €15,000."),
     ("Can you knock through to make an open-plan kitchen?",
      "Usually yes. We assess whether the wall is load-bearing, install a correctly sized beam where needed, and advise on the licence. It's the single most transformative job in most Spanish apartments and townhouses."),
     ("Will you fit a kitchen I buy elsewhere?",
      "Yes — we regularly prepare rooms for and install kitchens supplied by national retailers and local studios. We handle delivery coordination, first-fix services and full installation."),
     ("How long does a kitchen refit take?",
      "Without layout changes: 1–2 weeks. With walls moved or open-plan conversion: 3–5 weeks including plastering and drying. You'll get a schedule with your quote.")]),
}

# ---------------------------------------------------------------- home

def home_body(lang, ui):
    cards = "".join(f"""<div class="card">
      <div class="ico">◆</div>
      <h3>{ui["services_names"][k]}</h3>
      <p>{HOME_CARDS[k]}</p>
      <a class="more" href="{u(lang, k)}">{"Read more" if lang=="en" else "Läs mer"}</a>
    </div>""" for k in SERVICE_ORDER)
    return f"""<div class="hero"><div class="container">
  <div class="kicker">Torre del Mar · Vélez-Málaga · Nerja · Axarquia</div>
  <h1>Building, reforms &amp; property care on the <em>eastern Costa del Sol</em></h1>
  <p class="lead">One reliable team for reforms, extensions, plastering, tiling, bathrooms and kitchens. Over 35 years of experience — always on time and on budget.</p>
  <div class="actions">
    <a class="btn primary" href="{u(lang,'contact')}">Request a free quote</a>
    <a class="btn ghost" href="https://wa.me/34711027432">WhatsApp us</a>
  </div>
  <img class="mark" src="/images/logo_mark.svg" alt="">
</div></div>
<div class="trustbar"><div class="container">
  <div><b>35+ years</b> experience</div>
  <div><b>Free</b> no-obligation quotes</div>
  <div><b>12-month</b> workmanship guarantee</div>
  <div><b>English</b> &amp; <b>Swedish</b> spoken</div>
</div></div>
<section><div class="container">
  <div class="sec-head">
    <div class="kicker">What we do</div>
    <h2>Services across the Axarquia</h2>
    <p>From a single room to a whole property — every job quoted in writing, built properly and guaranteed for 12 months.</p>
  </div>
  <div class="grid c3">{cards}</div>
</div></section>
<section class="alt"><div class="container">
  <div class="sec-head">
    <div class="kicker">Why Handyman Axarquia</div>
    <h2>One team. One quote. No surprises.</h2>
  </div>
  <div class="grid c2">
    <div class="card"><div class="ico">✎</div><h3>Free written quotes</h3><p>A clear written quote for every job, with no obligation and no surprises. 50% deposit to book, balance only on completion.</p></div>
    <div class="card"><div class="ico">⌂</div><h3>We work for absent owners</h3><p>Abroad most of the year? Most of our clients are. Weekly photo updates on WhatsApp, keys handled securely, property left clean.</p></div>
    <div class="card"><div class="ico">✓</div><h3>Guaranteed workmanship</h3><p>Every job carries a 12-month workmanship guarantee, and materials keep their manufacturer's warranty.</p></div>
    <div class="card"><div class="ico">☏</div><h3>Fast, honest answers</h3><p>Call or WhatsApp between 8:00 and 20:00 weekdays. If a job isn't right for us, we'll say so and point you to someone good.</p></div>
  </div>
</div></section>
<section><div class="container">
  <div class="sec-head">
    <div class="kicker">Where we work</div>
    <h2>Serving the whole Axarquia</h2>
    <p>Based in Almayate, minutes from Torre del Mar — covering Vélez-Málaga, Algarrobo, Caleta de Vélez, Nerja, Torrox, Frigiliana, Cómpeta, Viñuela, Rincón de la Victoria and the surrounding villages and campo.</p>
    <ul class="tick" style="max-width:760px;margin:18px auto 0;display:grid;grid-template-columns:repeat(3,1fr);gap:4px 24px;text-align:left">
      <li>Torre del Mar</li><li>Vélez-Málaga</li><li>Algarrobo</li>
      <li>Caleta de Vélez</li><li>Almayate</li><li>Nerja</li>
      <li>Torrox</li><li>Frigiliana</li><li>Cómpeta</li>
      <li>Viñuela</li><li>Rincón de la Victoria</li><li>Axarquía villages &amp; campo</li>
    </ul>
  </div>
</div></section>
{cta_band(lang, ui, u)}"""

HOME_CARDS = {
    "reforms": "Full and partial property reforms managed end to end — strip-out to final clean.",
    "plastering": "Smooth internal plastering, gotelé removal, exterior render and lasting damp repairs.",
    "extensions": "Extra rooms, covered terraces and conversions — built for the climate, licensed properly.",
    "tiling": "Floors, walls and terraces tiled with precision — waterproofed so they never leak.",
    "bathrooms": "Complete bathroom refits and walk-in showers, strip-out to silicone in 1–2 weeks.",
    "kitchens": "Kitchen refits and open-plan conversions — one team for the whole job.",
}

# ---------------------------------------------------------------- gallery

# Real before/after project photos from the existing site.
# Root-relative /wp-content/... paths: keep the wp-content/uploads folder on the
# server when replacing WordPress and these keep working unchanged.
from gallery_data import GALLERY_PAIRS

def gallery_body(lang, ui):
    en = lang == "en"
    title = "Our work — before & after" if en else "Våra arbeten — före & efter"
    sub = ("Real projects across the Axarquia. Drag through — ask us for references, happy customers are our best advert."
           if en else
           "Verkliga projekt i Axarquía. Fråga gärna efter referenser — nöjda kunder är vår bästa reklam.")
    lb, la = ("Before", "After") if en else ("Före", "Efter")
    cards = "".join(f"""<div class="ba-card">
      <div class="ba-imgs">
        <figure><img src="{b}" alt="{lb}: {cap_en if en else cap_sv}" loading="lazy"><span class="tag-b">{lb}</span></figure>
        <figure><img src="{a}" alt="{la}: {cap_en if en else cap_sv}" loading="lazy"><span class="tag-a">{la}</span></figure>
      </div>
      <h3>{cap_en if en else cap_sv}</h3>
    </div>""" for b, a, cap_en, cap_sv in GALLERY_PAIRS)
    return f"""<div class="page-hero"><div class="container">
  <h1>{title}</h1>
  <p class="lead">{sub}</p>
</div></div>
<section><div class="container">
  <div class="ba-grid">{cards}</div>
</div></section>
{cta_band(lang, ui, u)}"""

# ---------------------------------------------------------------- contact

def contact_body(lang, ui):
    en = lang == "en"
    t = {
        "h1": "Get your free quote" if en else "Få en kostnadsfri offert",
        "lead": ("Tell us about your project — a couple of photos help. We reply the same working day."
                 if en else "Berätta om ditt projekt — ett par bilder hjälper. Vi svarar samma arbetsdag."),
        "call": "Call / WhatsApp" if en else "Ring / WhatsApp",
        "email": "Email" if en else "E-post",
        "hours": "Hours" if en else "Öppettider",
        "hoursv": "Mon–Fri 08:00–20:00" if en else "Mån–fre 08:00–20:00",
        "based": "Based in" if en else "Vi finns i",
        "basedv": "Los Toscanos 33, Almayate Bajo, 29749 Málaga",
        "name": "Your name" if en else "Ditt namn",
        "mail": "Email address" if en else "E-postadress",
        "phone": "Phone (optional)" if en else "Telefon (frivilligt)",
        "town": "Town / area" if en else "Ort / område",
        "msg": "Tell us about the job" if en else "Beskriv arbetet",
        "send": "Send message" if en else "Skicka meddelande",
        "note": ("Prefer WhatsApp? Message us photos of the job on +34 711 027 432 for the fastest reply."
                 if en else "Föredrar du WhatsApp? Skicka bilder på jobbet till +34 711 027 432 för snabbast svar."),
        "areas": ("We cover Torre del Mar, Vélez-Málaga, Algarrobo, Caleta de Vélez, Almayate, Nerja, Torrox, Frigiliana, Cómpeta, Viñuela and Rincón de la Victoria."
                  if en else "Vi täcker Torre del Mar, Vélez-Málaga, Algarrobo, Caleta de Vélez, Almayate, Nerja, Torrox, Frigiliana, Cómpeta, Viñuela och Rincón de la Victoria."),
    }
    return f"""<div class="page-hero"><div class="container">
  <h1>{t["h1"]}</h1>
  <p class="lead">{t["lead"]}</p>
</div></div>
<section><div class="container contact-grid">
  <div class="cinfo">
    <div class="row"><div class="ico">✆</div><div><div class="label">{t["call"]}</div><div class="val"><a href="tel:+34711027432">+34 711 027 432</a></div></div></div>
    <div class="row"><div class="ico">✉</div><div><div class="label">{t["email"]}</div><div class="val"><a href="mailto:info@handymanaxarquia.com">info@handymanaxarquia.com</a></div></div></div>
    <div class="row"><div class="ico">◔</div><div><div class="label">{t["hours"]}</div><div class="val">{t["hoursv"]}</div></div></div>
    <div class="row"><div class="ico">◈</div><div><div class="label">{t["based"]}</div><div class="val">{t["basedv"]}</div></div></div>
    <p style="color:var(--muted);font-size:.9rem;margin-top:8px">{t["note"]}</p>
    <p style="color:var(--muted);font-size:.85rem;margin-top:12px">{t["areas"]}</p>
  </div>
  <form class="contact" action="https://formsubmit.co/info@handymanaxarquia.com" method="POST">
    <input type="hidden" name="_subject" value="Website enquiry — handymanaxarquia.com">
    <input type="hidden" name="_captcha" value="true">
    <label>{t["name"]}</label><input type="text" name="name" required>
    <label>{t["mail"]}</label><input type="email" name="email" required>
    <label>{t["phone"]}</label><input type="tel" name="phone">
    <label>{t["town"]}</label><input type="text" name="town">
    <label>{t["msg"]}</label><textarea name="message" rows="5" required></textarea>
    <button type="submit">{t["send"]}</button>
  </form>
</div></section>"""

# ---------------------------------------------------------------- assemble

PAGES = {}
PAGES["home"] = {"key": "home",
    "title": "Handyman Axarquia | Builders & Reforms — Torre del Mar, Vélez-Málaga, Nerja",
    "desc": "Professional building, reforms, plastering, extensions, tiling, bathroom and kitchen renovations in Torre del Mar, Nerja, Frigiliana, Cómpeta, Rincón de la Victoria and across the Axarquia. Free quotes.",
    "body": home_body}
for k, s in SERVICES.items():
    from helpers import service_body as _sb
    s["body"] = _sb(s, u)
    PAGES[k] = s
PAGES["gallery"] = {"key": "gallery",
    "title": "Gallery — Our Work | Handyman Axarquia",
    "desc": "Recent reforms, bathrooms, kitchens, tiling and extension projects by Handyman Axarquia in Torre del Mar, Vélez-Málaga, Nerja and across the Axarquia.",
    "body": gallery_body}
PAGES["contact"] = {"key": "contact",
    "title": "Contact & Free Quotes | Handyman Axarquia",
    "desc": "Get a free, no-obligation quote for reforms, building and renovation work in the Axarquia. Call +34 711 027 432, WhatsApp, or send a message.",
    "body": contact_body}
