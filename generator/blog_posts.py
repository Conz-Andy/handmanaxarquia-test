# Blog posts (EN at /blog/<slug>/, SV at /sv/blogg/<slug_sv>/).
# Add a new post by appending a dict to POSTS. Dates are ISO (YYYY-MM-DD).
# "img" is (src, alt_en, alt_sv). Body HTML uses the same .prose styles as
# service pages (h2, p, ul.tick, etc.).

_G = "/wp-content/uploads/2026/08"
_O = "/wp-content/uploads/2024/02"

AUTHOR = "Nick Britton"

POSTS = [
{
    "slug": "building-licence-spain-obra-menor-obra-mayor",
    "slug_sv": "bygglov-spanien-obra-menor-obra-mayor",
    "date": "2026-09-09",
    "img": (f"{_G}/handyman-axarquia-pergola-vinuela-after.webp",
            "New pergola on a country property near Viñuela — a job that needed a licencia de obra menor",
            "Ny pergola på en landsbygdsfastighet nära Viñuela — ett jobb som krävde licencia de obra menor"),
    "en": {
        "title": "Do I need a licence for building work in Spain? Obra menor vs obra mayor explained",
        "meta_title": "Building Licences in Spain: Obra Menor vs Obra Mayor | Handyman Axarquia",
        "desc": "A plain-English guide to Spanish building licences for the Axarquia: what a licencia de obra menor covers, when you need an obra mayor, what it costs and how long it takes.",
        "excerpt": "Almost every job in Spain needs some form of permission. Here is what the two types of licence cover, what they cost, and what happens if you skip them.",
        "body": """
<p>One of the first questions we get from owners in Torre del Mar, Nerja or the villages is: "Do I actually need a licence for this?" The honest answer, for almost any building work in Spain, is <strong>yes</strong> — but the type of licence, the cost and the paperwork vary enormously. This guide explains the two categories in plain English, based on how the town halls in the Axarquia actually handle them.</p>

<h2>The two types of licence</h2>
<p>Spanish municipalities divide building work into two categories:</p>
<ul class="tick">
<li><strong>Licencia de obra menor</strong> — "minor works". Anything that does not touch the structure, the building's footprint, its volume or its external appearance in a significant way. Think bathroom and kitchen refits, retiling, replacing windows like-for-like, plastering and painting, internal non-structural changes, repairs to terraces and roofs.</li>
<li><strong>Licencia de obra mayor</strong> — "major works". Anything structural or that changes the building: extensions, removing load-bearing walls, new floors or roofs, changes of use, new swimming pools, and most work on protected or rural properties. An obra mayor needs a project signed by an architect and usually an aparejador (technical architect) to supervise it.</li>
</ul>
<p>In practice, many town halls in the Axarquia (Vélez-Málaga included) now run a fast-track system for the simplest minor works called a <em>declaración responsable</em> — a signed declaration that the work complies, which lets you start immediately rather than waiting for a licence to be issued. Your builder or gestor should know which route your town hall uses.</p>

<h2>What does a licence cost?</h2>
<p>Two charges apply: a <strong>tasa</strong> (administrative fee, usually small) and the <strong>ICIO</strong> — a construction tax charged as a percentage of the declared cost of the works, typically around 3–4% in this area. So on a €6,000 bathroom refit, expect roughly €200–€300 in licence costs. For an obra mayor, add the architect's project fees, which for a modest extension start at a few thousand euros and depend on the size and complexity of the job.</p>

<h2>How long does it take?</h2>
<p>A declaración responsable is effectively immediate. A standard licencia de obra menor in Vélez-Málaga, Nerja or Torrox can take anywhere from a couple of weeks to two months depending on how busy the department is. An obra mayor is a different animal: three to six months is normal, sometimes longer if the property is in a protected old-town area or on rural land. Plan around it — nobody wants an architect's project sitting on a desk while the summer rental season passes.</p>

<h2>Apartments: your comunidad has a say too</h2>
<p>If you own a flat, the town hall is only half the story. The comunidad de propietarios must be informed of any works, and anything that affects the façade, terraces, shared pipework or the structure needs the community's approval at a meeting. Working hours are also usually restricted by the community rules — typically no noisy work at siesta time or on Sundays. A good builder will handle the notification for you and keep the neighbours on side.</p>

<h2>What happens if you skip it?</h2>
<p>People do, and it usually goes fine — until it doesn't. The risks are real: a fine, a stop order half-way through the job, problems when you come to sell (the buyer's lawyer will ask), and difficulty legalising the work later. On rural land the consequences of unlicensed building can be far more serious. For the few hundred euros a minor-works licence costs, it is simply not worth it.</p>

<h2>Rural land is different</h2>
<p>Country properties around Viñuela, Frigiliana and the Torrox campo sit on <em>suelo rústico</em>, where new built area is tightly controlled. Repairs, maintenance, pergolas and some conversions of existing space are often possible; new extensions frequently are not. We tell every campo client at the first visit what is realistic — before anyone falls in love with a plan.</p>

<h2>How we handle licences for you</h2>
<p>For every quote we give, we state which licence the job needs. For obra menor work we prepare and submit the paperwork on your behalf, including the budget breakdown the town hall asks for. For obra mayor projects we introduce you to local architects we work with regularly, and we coordinate the project with them so the build and the paperwork move together. No surprises half-way through.</p>
<p>Planning a reform, extension or renovation in the Axarquia? <a href="/contact/">Ask us for a free written quote</a> — we will tell you exactly what permissions it needs.</p>
""",
    },
    "sv": {
        "title": "Behöver jag bygglov i Spanien? Obra menor och obra mayor förklarat",
        "meta_title": "Bygglov i Spanien: Obra menor vs obra mayor | Handyman Axarquia",
        "desc": "Enkel guide till spanska bygglov för Axarquía: vad licencia de obra menor täcker, när du behöver obra mayor, vad det kostar och hur lång tid det tar.",
        "excerpt": "Nästan alla byggarbeten i Spanien kräver någon form av tillstånd. Här är vad de två typerna av bygglov täcker, vad de kostar och vad som händer om du hoppar över dem.",
        "body": """
<p>En av de första frågorna vi får från ägare i Torre del Mar, Nerja eller byarna är: "Behöver jag verkligen bygglov för det här?" Det ärliga svaret, för nästan allt byggarbete i Spanien, är <strong>ja</strong> — men typen av tillstånd, kostnaden och pappersarbetet varierar enormt. Den här guiden förklarar de två kategorierna på enkel svenska, utifrån hur kommunerna i Axarquía faktiskt hanterar dem.</p>

<h2>De två typerna av tillstånd</h2>
<p>Spanska kommuner delar in byggarbeten i två kategorier:</p>
<ul class="tick">
<li><strong>Licencia de obra menor</strong> — "mindre arbeten". Allt som inte rör stommen, byggnadens yta, volym eller yttre utseende på ett väsentligt sätt. Badrums- och köksrenoveringar, ny plattsättning, fönsterbyte till likvärdigt, puts och målning, invändiga icke bärande ändringar, reparation av terrasser och tak.</li>
<li><strong>Licencia de obra mayor</strong> — "större arbeten". Allt som är bärande eller förändrar byggnaden: tillbyggnader, rivning av bärande väggar, nya våningar eller tak, ändrad användning, nya pooler och det mesta på skyddade eller lantliga fastigheter. Obra mayor kräver ett projekt signerat av arkitekt och vanligtvis en aparejador (byggnadsingenjör) som övervakar arbetet.</li>
</ul>
<p>I praktiken har många kommuner i Axarquía (inklusive Vélez-Málaga) numera ett snabbspår för de enklaste mindre arbetena som kallas <em>declaración responsable</em> — en undertecknad försäkran om att arbetet följer reglerna, som låter dig börja direkt i stället för att vänta på beslut. Din byggare eller gestor bör veta vilken väg din kommun använder.</p>

<h2>Vad kostar ett bygglov?</h2>
<p>Två avgifter tillkommer: en <strong>tasa</strong> (administrativ avgift, oftast liten) och <strong>ICIO</strong> — en byggskatt som beräknas som en procentandel av arbetets deklarerade kostnad, vanligtvis omkring 3–4 % i det här området. På en badrumsrenovering för 6 000 euro blir det alltså ungefär 200–300 euro i tillståndskostnader. För obra mayor tillkommer arkitektens projektarvode, som för en mindre tillbyggnad börjar på några tusen euro beroende på storlek och komplexitet.</p>

<h2>Hur lång tid tar det?</h2>
<p>En declaración responsable gäller i praktiken omedelbart. En vanlig licencia de obra menor i Vélez-Málaga, Nerja eller Torrox kan ta från ett par veckor till två månader beroende på kommunens arbetsbelastning. Obra mayor är något helt annat: tre till sex månader är normalt, ibland längre om fastigheten ligger i ett skyddat område i gamla stan eller på landsbygdsmark. Planera efter det — ingen vill ha ett arkitektprojekt liggande på ett skrivbord medan uthyrningssäsongen passerar.</p>

<h2>Lägenheter: samfälligheten har också något att säga</h2>
<p>Om du äger en lägenhet är kommunen bara halva historien. Samfälligheten (comunidad de propietarios) ska informeras om alla arbeten, och allt som påverkar fasad, terrasser, gemensamma rör eller stommen kräver samfällighetens godkännande på ett möte. Arbetstiderna är dessutom oftast begränsade av samfällighetens regler — normalt inget bullrigt arbete under siestan eller på söndagar. En bra byggare sköter anmälan åt dig och håller sig väl med grannarna.</p>

<h2>Vad händer om du hoppar över det?</h2>
<p>Folk gör det, och det går oftast bra — tills det inte gör det. Riskerna är verkliga: böter, byggstopp mitt i jobbet, problem vid försäljning (köparens advokat kommer att fråga) och svårigheter att legalisera arbetet i efterhand. På landsbygdsmark kan konsekvenserna av olovligt byggande vara betydligt allvarligare. För de några hundra euro ett tillstånd för mindre arbeten kostar är det helt enkelt inte värt risken.</p>

<h2>Landsbygdsmark är annorlunda</h2>
<p>Lanthus runt Viñuela, Frigiliana och Torrox ligger på <em>suelo rústico</em>, där ny byggyta är hårt reglerad. Reparationer, underhåll, pergolor och vissa ombyggnader av befintlig yta är ofta möjliga; nya tillbyggnader är det ofta inte. Vi berättar för varje kund på landet redan vid första besöket vad som är realistiskt — innan någon blir förälskad i en plan.</p>

<h2>Så sköter vi bygglovet åt dig</h2>
<p>I varje offert anger vi vilket tillstånd jobbet kräver. För obra menor förbereder och lämnar vi in handlingarna åt dig, inklusive den kostnadsspecifikation kommunen vill ha. För obra mayor presenterar vi dig för lokala arkitekter som vi samarbetar med regelbundet, och vi samordnar projektet med dem så att bygget och pappersarbetet löper parallellt. Inga överraskningar halvvägs.</p>
<p>Planerar du en renovering, tillbyggnad eller ombyggnad i Axarquía? <a href="/sv/kontakt/">Be oss om en kostnadsfri skriftlig offert</a> — vi berättar exakt vilka tillstånd som krävs, på svenska.</p>
""",
    },
},
{
    "slug": "damp-in-spanish-house-causes-and-fixes",
    "slug_sv": "fukt-i-huset-spanien-orsaker-och-losningar",
    "date": "2026-09-09",
    "img": (f"{_O}/axarquia-handyman-reform-garden-wall-repair-render-repaint-after.webp",
            "Repaired and re-rendered garden wall in the Axarquia after damp damage",
            "Reparerad och omputsad trädgårdsmur i Axarquía efter fuktskador"),
    "en": {
        "title": "Damp in your Spanish home: the six causes we see most in the Axarquia (and what actually fixes them)",
        "meta_title": "Damp in a Spanish House: Causes & Real Fixes (Axarquia) | Handyman Axarquia",
        "desc": "Why coastal and village properties in the Axarquia get damp every winter — condensation, failed render, terrace leaks, rising damp — and the repairs that last, from a local builder.",
        "excerpt": "Painting over damp hides it for one season. Here are the six causes we find again and again in Torre del Mar, Nerja and the villages, and the repair that fixes each one for good.",
        "body": """
<p>Every November the same messages arrive: black spots in the corner of a bedroom, bubbling paint under a window, a musty smell in a flat that was closed up since September. Damp is the number one problem in Axarquia properties — and the number one job that gets done badly, because painting over it is quick and cheap and lasts almost exactly one winter. Here are the six causes we find most often, and what actually fixes each one.</p>

<h2>1. Condensation in closed-up holiday homes</h2>
<p><strong>What it looks like:</strong> black mould in cold corners, behind wardrobes and around window frames; a musty smell when you open the door after months away.</p>
<p><strong>Why it happens:</strong> a sealed apartment with no heating and no air movement, on a coast where winter humidity regularly sits above 80%. Moisture condenses on the coldest surfaces — external walls, north-facing corners, single-glazed windows.</p>
<p><strong>The fix:</strong> ventilation, not paint. Trickle vents or a small humidity-controlled extractor, a dehumidifier on a timer if the property is empty for months, and in stubborn rooms an insulating plaster or thermal board on the cold wall so the surface stays above dew point. Anti-mould paint alone is a sticking plaster.</p>

<h2>2. Terrace and roof leaks into the room below</h2>
<p><strong>What it looks like:</strong> a stain on the ceiling that grows after rain, often below a terrace or roof terrace; plaster that comes away in sheets.</p>
<p><strong>Why it happens:</strong> tiles laid straight onto an old surface with no waterproof membrane, failed joints, blocked drains or wrong falls. This is the most common leak on the whole coast, from Torrox Costa to Rincón.</p>
<p><strong>The fix:</strong> strip back the terrace, apply a proper waterproof membrane with correct falls to the drain, then re-tile with expansion joints. Re-grouting or a "liquid membrane" painted over old tiles is a temporary measure at best.</p>

<h2>3. Failed exterior render (salt air and sun)</h2>
<p><strong>What it looks like:</strong> cracked, hollow or blown render on the outside wall; damp patches appearing inside on the same wall.</p>
<p><strong>Why it happens:</strong> years of salt air, summer heat and winter rain open hairline cracks; water gets behind the render and cannot get out.</p>
<p><strong>The fix:</strong> remove the loose render, treat the wall and re-render with a suitable product — monocapa or a traditional lime-based render on older walls — and finish with a breathable paint. Filling cracks and repainting only delays the same repair.</p>

<h2>4. Rising damp in ground-floor and village properties</h2>
<p><strong>What it looks like:</strong> a tide-mark up to about a metre on ground-floor walls, salts crystallising on the surface, plaster that crumbles at the base.</p>
<p><strong>Why it happens:</strong> older properties in Vélez-Málaga's old town, Frigiliana and the villages were built without a damp-proof course. Moisture wicks up from the ground into stone, brick and earth walls. Cement render and plastic paints applied over the years make it worse by trapping the water.</p>
<p><strong>The fix:</strong> remove the affected plaster, treat the wall (injected damp-proof course where the wall allows it), then re-plaster with a breathable lime or renovation plaster so the wall can dry through the surface. It is invisible when done, and it lasts.</p>

<h2>5. Hillside water and blocked drainage</h2>
<p><strong>What it looks like:</strong> damp on the wall that backs onto the hill or the neighbour's higher plot, worse after heavy rain.</p>
<p><strong>Why it happens:</strong> village houses stacked up a slope receive water from above. Without land drains or tanking, the wall becomes the drain.</p>
<p><strong>The fix:</strong> deal with the water outside first — drainage channels, a French drain, repaired gutters and downpipes — then tank or re-render the inside face. Internal treatments alone are fighting the whole hill.</p>

<h2>6. Plumbing leaks that look like damp</h2>
<p><strong>What it looks like:</strong> a persistent wet patch that does not follow the weather, often near a bathroom, kitchen or where pipes run in the wall.</p>
<p><strong>Why it happens:</strong> old galvanised or early plastic pipework, a failed shower tray seal, or a slow leak on a water heater.</p>
<p><strong>The fix:</strong> find the leak before touching the wall — a pressure test or moisture mapping tells us quickly. Then repair the pipe, dry the wall properly and re-plaster. Never re-plaster a wall that is still being fed water.</p>

<h2>The rule we work by</h2>
<p>Treat the cause, then the wall, then the paint — in that order. Every damp job we quote starts with a visit to find out which of the six causes you actually have, because the right repair for one is the wrong repair for another. Most single-room repairs take two to five days, and everything we do carries our 12-month workmanship guarantee.</p>
<p>Got a damp problem in Torre del Mar, Nerja, Torrox, Rincón de la Victoria or the villages? <a href="/plastering/">See our plastering and damp repair service</a> or <a href="/contact/">send us a couple of photos on WhatsApp</a> for a free assessment.</p>
""",
    },
    "sv": {
        "title": "Fukt i huset i Spanien: de sex orsaker vi ser oftast i Axarquía (och vad som faktiskt hjälper)",
        "meta_title": "Fukt i spanska hus: orsaker & hållbara lösningar (Axarquía) | Handyman Axarquia",
        "desc": "Varför kust- och byhus i Axarquía blir fuktiga varje vinter — kondens, sprucken puts, läckande terrasser, stigande fukt — och reparationerna som håller, från en lokal byggfirma.",
        "excerpt": "Att måla över fukt döljer den i en säsong. Här är de sex orsaker vi hittar gång på gång i Torre del Mar, Nerja och byarna, och den åtgärd som löser var och en på riktigt.",
        "body": """
<p>Varje november kommer samma meddelanden: svarta fläckar i hörnet av ett sovrum, bubblande färg under ett fönster, unken lukt i en lägenhet som stått stängd sedan september. Fukt är problem nummer ett i Axarquías bostäder — och det jobb som oftast görs dåligt, eftersom att måla över är snabbt och billigt och håller nästan exakt en vinter. Här är de sex orsaker vi hittar oftast, och vad som faktiskt åtgärdar var och en.</p>

<h2>1. Kondens i stängda semesterbostäder</h2>
<p><strong>Så ser det ut:</strong> svart mögel i kalla hörn, bakom garderober och runt fönsterkarmar; unken lukt när du öppnar dörren efter månader borta.</p>
<p><strong>Varför:</strong> en tillsluten lägenhet utan värme och luftväxling, på en kust där vinterfuktigheten regelbundet ligger över 80 %. Fukten kondenserar på de kallaste ytorna — ytterväggar, hörn mot norr, fönster med enkelglas.</p>
<p><strong>Lösningen:</strong> ventilation, inte färg. Spaltventiler eller en liten fuktstyrd fläkt, en avfuktare på timer om bostaden står tom i månader, och i envisa rum en isolerande puts eller termoskiva på den kalla väggen så att ytan håller sig över daggpunkten. Mögelfärg ensamt är ett plåster.</p>

<h2>2. Terrass- och takläckage ner i rummet under</h2>
<p><strong>Så ser det ut:</strong> en fläck i taket som växer efter regn, ofta under en terrass eller takterrass; puts som lossnar i sjok.</p>
<p><strong>Varför:</strong> plattor lagda direkt på ett gammalt underlag utan tätskikt, spruckna fogar, igensatta brunnar eller fel fall. Det är den vanligaste läckan på hela kusten, från Torrox Costa till Rincón.</p>
<p><strong>Lösningen:</strong> riv upp terrassen, lägg ett riktigt tätskikt med rätt fall mot brunnen och plattsätt på nytt med rörelsefogar. Omfogning eller ett "flytande membran" målat över gamla plattor är i bästa fall tillfälligt.</p>

<h2>3. Sprucken fasadputs (salt luft och sol)</h2>
<p><strong>Så ser det ut:</strong> sprucken, ihålig eller bortsprängd puts på ytterväggen; fuktfläckar inomhus på samma vägg.</p>
<p><strong>Varför:</strong> år av salt luft, sommarhetta och vinterregn öppnar hårfina sprickor; vatten tränger in bakom putsen och kommer inte ut.</p>
<p><strong>Lösningen:</strong> ta bort den lösa putsen, behandla väggen och putsa om med rätt produkt — monocapa eller traditionell kalkputs på äldre väggar — och avsluta med en andande färg. Att spackla sprickor och måla om skjuter bara upp samma reparation.</p>

<h2>4. Stigande fukt i bottenvåningar och byhus</h2>
<p><strong>Så ser det ut:</strong> en fuktrand upp till ungefär en meter på bottenvåningens väggar, salter som kristalliserar på ytan, puts som smulas vid golvet.</p>
<p><strong>Varför:</strong> äldre hus i Vélez-Málagas gamla stan, Frigiliana och byarna byggdes utan fuktspärr. Fukt sugs upp från marken in i sten-, tegel- och jordväggar. Cementputs och plastfärger som lagts på genom åren förvärrar det genom att stänga in vattnet.</p>
<p><strong>Lösningen:</strong> ta bort den skadade putsen, behandla väggen (injicerad fuktspärr där väggen tillåter det) och putsa om med andande kalk- eller saneringsputs så att väggen kan torka genom ytan. Det syns inte när det är klart, och det håller.</p>

<h2>5. Vatten från sluttningen och igensatt avrinning</h2>
<p><strong>Så ser det ut:</strong> fukt på väggen som vetter mot berget eller grannens högre tomt, värre efter kraftigt regn.</p>
<p><strong>Varför:</strong> byhus staplade uppför en sluttning tar emot vatten uppifrån. Utan dränering eller tätning blir väggen avloppet.</p>
<p><strong>Lösningen:</strong> hantera vattnet utomhus först — avrinningsrännor, dräneringsdike, lagade hängrännor och stuprör — och täta eller putsa sedan om insidan. Enbart invändig behandling slåss mot hela berget.</p>

<h2>6. Rörläckage som ser ut som fukt</h2>
<p><strong>Så ser det ut:</strong> en ihållande våt fläck som inte följer vädret, ofta nära badrum, kök eller där rör går i väggen.</p>
<p><strong>Varför:</strong> gamla galvaniserade rör eller tidiga plaströr, en trasig tätning vid duschkaret eller ett långsamt läckage på varmvattenberedaren.</p>
<p><strong>Lösningen:</strong> hitta läckan innan väggen rörs — ett trycktest eller fuktmätning ger snabbt svar. Laga sedan röret, torka väggen ordentligt och putsa om. Putsa aldrig om en vägg som fortfarande matas med vatten.</p>

<h2>Regeln vi arbetar efter</h2>
<p>Åtgärda orsaken, sedan väggen, sedan färgen — i den ordningen. Varje fuktjobb vi offererar börjar med ett besök för att ta reda på vilken av de sex orsakerna du faktiskt har, eftersom rätt reparation för en är fel reparation för en annan. De flesta reparationer av ett enskilt rum tar två till fem dagar, och allt vi gör omfattas av vår 12-månadersgaranti på arbetet.</p>
<p>Har du fuktproblem i Torre del Mar, Nerja, Torrox, Rincón de la Victoria eller byarna? <a href="/sv/putsarbeten/">Läs om vår puts- och fukttjänst</a> eller <a href="/sv/kontakt/">skicka ett par bilder på WhatsApp</a> för en kostnadsfri bedömning.</p>
""",
    },
},
{
    "slug": "bathroom-renovation-cost-axarquia",
    "slug_sv": "vad-kostar-badrumsrenovering-axarquia",
    "date": "2026-09-09",
    "img": (f"{_G}/handyman-axarquia-bathroom-reform-2-after.webp",
            "Renovated bathroom with double vanity in the Axarquia — after",
            "Renoverat badrum med dubbelt handfat i Axarquía — efter"),
    "en": {
        "title": "Bathroom renovation costs in the Axarquia: real price bands for 2026",
        "meta_title": "Bathroom Renovation Cost in the Axarquia (2026 Price Guide) | Handyman Axarquia",
        "desc": "What a bathroom renovation really costs in Torre del Mar, Nerja, Torrox and Rincón de la Victoria: three price bands, what drives the cost up, how long it takes and what to budget for.",
        "excerpt": "Nobody local publishes real numbers, so here are ours: three price bands for a complete bathroom refit in the Axarquia, what pushes the cost up or down, and what is included.",
        "body": """
<p>"How much for a new bathroom?" is the question we answer most often, and it deserves a straight answer rather than "it depends". It does depend — on size, tiles, fittings and what we find behind the old ones — but after hundreds of bathrooms in Torre del Mar, Nerja, Torrox and Rincón de la Victoria we can give you honest price bands. These are for a complete refit of a standard bathroom of roughly 4–6 m², labour and materials included, with IVA on top.</p>

<h2>The three price bands</h2>
<ul class="tick">
<li><strong>Standard — €4,500 to €6,000.</strong> Full strip-out, new plumbing to the fittings, waterproofing (tanking) of the wet zone, mid-range Spanish ceramic tiles on floor and walls, a shower tray with a glass screen, a wall-hung basin unit, toilet, mirror and a simple extractor. Perfect for holiday rentals where robustness matters more than luxury.</li>
<li><strong>Mid-range — €6,000 to €9,000.</strong> Everything above, plus larger-format porcelain tiles, a walk-in or level-access shower with a linear drain, thermostatic shower fittings, a better-quality vanity unit with storage, a heated towel rail, and recessed lighting. This is the band most owner-occupiers choose.</li>
<li><strong>Premium — €9,000 to €15,000+.</strong> Natural stone or large-format porcelain slabs, a full wet room, concealed cisterns and shower valves, bespoke joinery, underfloor heating, designer sanitaryware, and layout changes that involve moving the soil pipe or drainage.</li>
</ul>

<h2>What pushes the price up</h2>
<p>A handful of things move a bathroom from one band to the next, and most of them are decided before we start:</p>
<ul class="tick">
<li><strong>Tiles.</strong> The single biggest variable. Ceramic at €12–€20/m² versus porcelain at €30–€60/m² or stone at €80+ makes a difference of a thousand euros or more on a whole bathroom, before the extra labour for large formats.</li>
<li><strong>Moving things.</strong> Keeping the toilet, basin and shower where they are is the cheapest option. Relocating the toilet means moving the soil pipe, which can add €500–€1,500.</li>
<li><strong>Old pipework.</strong> In 1970s–90s apartments we frequently find galvanised steel pipes that should be replaced while the walls are open. We always tell you before we do it.</li>
<li><strong>Access.</strong> Third-floor apartment with no lift, or a village house with no vehicle access, means more labour hours carrying rubble out and materials in.</li>
<li><strong>Wet rooms.</strong> Level-access showers need the floor screed lowered or built up and more waterproofing — worth it, but it costs more than a tray.</li>
</ul>

<h2>What is included in our quotes</h2>
<p>Every bathroom quote we give is free, in writing and valid for 30 days. It covers strip-out and rubble removal, plumbing and electrical work, tanking, plastering, tiling, fitting of sanitaryware and screen, silicone and finishing, cleaning, and the licencia de obra menor paperwork. Tiles and sanitaryware are your choice — pick your own from the showrooms in Torre del Mar and Vélez-Málaga, or ask us to source options to your budget.</p>

<h2>How long does it take?</h2>
<p>A standard refit takes 7–12 working days. Water is off only for short periods, and where the property has a second bathroom you will never be without one overnight. A wet room or a layout change adds a few days for screeding and drying.</p>

<h2>Two things we always do</h2>
<p>We tank (waterproof) the wet zone before a single tile goes on — it is invisible when finished and it is the difference between a bathroom that lasts and one that leaks into the flat below. And we fit proper ventilation, because a bathroom without an extractor on this coast grows mould within a winter. Both are included in every band.</p>

<h2>Bath to walk-in shower conversions</h2>
<p>If you only want to swap a bath for a walk-in shower and keep the rest, that is a smaller job: typically €1,800–€3,500 including the tray, screen, thermostatic fittings, re-tiling of the shower area and plumbing, done in 3–5 days.</p>
<p>Ready for a number for your bathroom? <a href="/bathrooms/">See our bathroom renovation service</a> or <a href="/contact/">send us a photo and the rough size</a> and we will come back with a free written quote.</p>
""",
    },
    "sv": {
        "title": "Vad kostar en badrumsrenovering i Axarquía? Riktiga prisnivåer för 2026",
        "meta_title": "Badrumsrenovering i Axarquía — prisguide 2026 | Handyman Axarquia",
        "desc": "Vad en badrumsrenovering faktiskt kostar i Torre del Mar, Nerja, Torrox och Rincón de la Victoria: tre prisnivåer, vad som driver upp priset, hur lång tid det tar och vad som ingår.",
        "excerpt": "Ingen lokal firma publicerar riktiga siffror, så här är våra: tre prisnivåer för en komplett badrumsrenovering i Axarquía, vad som gör den dyrare eller billigare, och vad som ingår.",
        "body": """
<p>"Vad kostar ett nytt badrum?" är frågan vi svarar på oftast, och den förtjänar ett rakt svar i stället för "det beror på". Det beror förvisso på — storlek, kakel, inredning och vad vi hittar bakom det gamla — men efter hundratals badrum i Torre del Mar, Nerja, Torrox och Rincón de la Victoria kan vi ge ärliga prisnivåer. De gäller en komplett renovering av ett normalstort badrum på cirka 4–6 m², arbete och material inkluderat, exklusive IVA (moms).</p>

<h2>De tre prisnivåerna</h2>
<ul class="tick">
<li><strong>Standard — 4 500 till 6 000 euro.</strong> Fullständig rivning, nya rör fram till inredningen, tätskikt i våtzonen, spanskt kakel i mellanklass på golv och väggar, duschkar med glasvägg, väggmonterat tvättställsskåp, toalett, spegel och en enkel fläkt. Perfekt för uthyrningslägenheter där tålighet betyder mer än lyx.</li>
<li><strong>Mellanklass — 6 000 till 9 000 euro.</strong> Allt ovan, plus större klinkerplattor, walk-in-dusch i golvnivå med linjeavlopp, termostatblandare, ett bättre tvättställsskåp med förvaring, handdukstork och infällda spotlights. Den nivå de flesta som bor permanent väljer.</li>
<li><strong>Premium — 9 000 till 15 000+ euro.</strong> Natursten eller storformatsplattor, helkaklat våtrum, inbyggda cisterner och duschventiler, platsbyggd snickeri, golvvärme, designporslin och planändringar som innebär att avloppet flyttas.</li>
</ul>

<h2>Vad driver upp priset</h2>
<p>Några saker flyttar ett badrum från en nivå till nästa, och de flesta bestäms innan vi börjar:</p>
<ul class="tick">
<li><strong>Kakel.</strong> Den enskilt största variabeln. Kakel för 12–20 euro/m² jämfört med klinker för 30–60 euro/m² eller sten för 80+ gör en skillnad på tusen euro eller mer på ett helt badrum, innan extraarbetet för stora format.</li>
<li><strong>Att flytta saker.</strong> Att behålla toalett, tvättställ och dusch där de är är det billigaste alternativet. Att flytta toaletten innebär att avloppsröret flyttas, vilket kan lägga på 500–1 500 euro.</li>
<li><strong>Gamla rör.</strong> I lägenheter från 70–90-talet hittar vi ofta galvaniserade stålrör som bör bytas medan väggarna är öppna. Vi berättar alltid innan vi gör det.</li>
<li><strong>Åtkomst.</strong> Tredje våningen utan hiss, eller ett byhus utan bilväg, innebär fler arbetstimmar för att bära ut rivningsmassor och in material.</li>
<li><strong>Våtrum.</strong> Duschar i golvnivå kräver att golvet sänks eller byggs upp och mer tätskikt — värt det, men dyrare än ett duschkar.</li>
</ul>

<h2>Vad som ingår i våra offerter</h2>
<p>Varje badrumsoffert vi lämnar är kostnadsfri, skriftlig och gäller i 30 dagar. Den omfattar rivning och bortforsling, rör- och elarbete, tätskikt, puts, plattsättning, montering av porslin och duschvägg, silikon och finish, städning samt handlingarna för licencia de obra menor. Kakel och porslin väljer du själv i butikerna i Torre del Mar och Vélez-Málaga, eller så tar vi fram alternativ efter din budget.</p>

<h2>Hur lång tid tar det?</h2>
<p>En standardrenovering tar 7–12 arbetsdagar. Vattnet är avstängt bara korta stunder, och om bostaden har ett andra badrum står du aldrig utan över natten. Ett våtrum eller en planändring lägger till några dagar för avjämning och torkning.</p>

<h2>Två saker vi alltid gör</h2>
<p>Vi lägger tätskikt i våtzonen innan en enda platta sätts — det syns inte när det är klart och det är skillnaden mellan ett badrum som håller och ett som läcker ner till lägenheten under. Och vi monterar ordentlig ventilation, eftersom ett badrum utan fläkt på den här kusten får mögel inom en vinter. Båda ingår i alla nivåer.</p>

<h2>Byta badkar mot walk-in-dusch</h2>
<p>Om du bara vill byta badkaret mot en walk-in-dusch och behålla resten är det ett mindre jobb: vanligtvis 1 800–3 500 euro inklusive duschkar, glasvägg, termostatblandare, ny plattsättning i duschzonen och rördragning, klart på 3–5 dagar.</p>
<p>Vill du ha en siffra för ditt badrum? <a href="/sv/badrum/">Läs om vår badrumsrenovering</a> eller <a href="/sv/kontakt/">skicka en bild och ungefärlig storlek</a> så återkommer vi med en kostnadsfri skriftlig offert.</p>
""",
    },
},
{
    "slug": "hire-a-builder-axarquia-spain",
    "slug_sv": "anlita-hantverkare-spanien-axarquia",
    "date": "2026-09-09",
    "img": (f"{_G}/handyman-axarquia-courtyard-lighting-after.webp",
            "Courtyard reform with new lighting and a glass floor — after",
            "Renoverad innergård med ny belysning och glasgolv — efter"),
    "en": {
        "title": "How to hire a builder in the Axarquia without getting burned",
        "meta_title": "Hiring a Builder in Spain: 9 Checks | Handyman Axarquia",
        "desc": "How to hire a builder in Spain without getting burned: nine checks on quotes, deposits, IVA, licences, insurance, references, communication and guarantees.",
        "excerpt": "Most owners need a builder sooner or later. Here are nine checks you can use on any firm — ours included — before you hand over a deposit.",
        "body": """
<p>Sooner or later, most owners on this coast need a builder — for a leaking terrace, a tired bathroom, a full reform of a place they have just bought. The good ones are busy and worth waiting for; the bad ones cost you twice. This is the checklist we would give a friend buying in Nerja, Torre del Mar or the villages. It works on any builder, ourselves included — measure us against it.</p>

<h2>1. Insist on a clear written quote</h2>
<p>A verbal "about eight thousand" is not a quote. Ask for a written price for the whole job, valid for a set period, that states plainly what is and is not included — labour, materials, rubble removal, the licence and IVA. A proper written quote tells you the builder has actually thought the job through, and it protects both sides when a decision has to be made half-way through. If someone will only give you a single round number over the phone, or scribbles it on the back of a receipt, that tells you how the rest of the job will go. Our own quotes are free, in writing and valid for 30 days.</p>

<h2>2. Understand the deposit and payment stages</h2>
<p>In Spain it is completely normal to pay a deposit up front — commonly around 50% — because your builder buys materials, sanitaryware and tiles before the first day on site. What is not normal is being asked for 100% before any work starts. A fair structure is a deposit to book and buy materials, one or two stage payments tied to milestones on a longer job, and the final balance only when the work is finished and you are happy. We work to exactly that: 50% to book, balance on completion.</p>

<h2>3. Ask for a factura with IVA</h2>
<p>You will sometimes be offered a lower price "sin IVA" — cash, no invoice. It is tempting and it is a false economy. Without a factura you have no proof the work was done, no recourse if it fails, and nothing to show a buyer's lawyer when you sell — improvements you cannot document can complicate both the sale and your capital-gains position. Pay the IVA, keep the invoices in the same folder as your escritura, and thank yourself later.</p>

<h2>4. Check the licence is named in the quote</h2>
<p>Almost every job needs some form of permission, and the quote should say which — a licencia de obra menor for most refits, an obra mayor with an architect for anything structural. A builder who shrugs off licences is a builder who will leave you holding a fine, or a problem at sale time. If you are not sure what your job needs, our guide to <a href="/blog/building-licence-spain-obra-menor-obra-mayor/">obra menor versus obra mayor</a> explains it in plain English.</p>

<h2>5. Ask about insurance and liability</h2>
<p>If a burst pipe during your bathroom refit floods the flat below, who pays? A professional builder carries liability insurance and takes responsibility for damage caused by the work. Ask the question directly. In an apartment block it matters even more, because your neighbour's ceiling is your builder's risk, not yours.</p>

<h2>6. See real references and past work</h2>
<p>Photos of finished jobs, a Google profile with reviews, the phone number of a past client who will talk to you — a builder with a track record can show all three without hesitating. Read the reviews for what they say about communication and tidiness, not just the star rating. Anyone can have one good photo; look for a consistent body of work.</p>

<h2>7. Sort out communication before you start</h2>
<p>If you are abroad for most of the year, communication is the whole job. Agree at the outset how you will be kept informed — for us that means photo updates on WhatsApp as the work moves, so you can see the tiling go down and the sanitaryware go in without flying over. A builder who goes quiet for two weeks while you are in Stockholm or Surrey is telling you something.</p>

<h2>8. Get the guarantee in writing</h2>
<p>Workmanship should be guaranteed, and the guarantee should be on paper. Ours is twelve months on the work, with materials keeping their manufacturer's warranty on top. A verbal "don't worry, I'll come back if there's a problem" is worth exactly nothing in February when the builder has stopped answering.</p>

<h2>9. Know what to do if it goes wrong</h2>
<p>Most jobs go fine. If one does not, keep a written record — your quote, your invoices, dated photos and your messages. Raise the problem in writing and give the builder a fair chance to put it right; most disputes are misunderstandings that a calm email solves. If it cannot be resolved, Spain has a consumer-arbitration system, each town hall has an OMIC (municipal consumer office), and the Junta de Andalucía runs a regional consumer service. This is general guidance, not legal advice — but knowing the route exists changes the conversation.</p>

<h2>The quiet point</h2>
<p>Read that list again and you will notice it is simply a description of how a serious builder already works: everything written down, sensible payments, proper paperwork, honest updates, a guarantee. We built the way we work around exactly these expectations, because the clients who ask these questions are the clients we like. If you are lining up quotes for a project anywhere from Rincón de la Victoria to Nerja, ask every builder the nine questions above — and see who answers cleanly.</p>

<p>Planning a reform and want a quote you can actually compare? <a href="/reforms/">See how we handle full reforms</a>, take a look at our work in <a href="/areas/nerja/">Nerja</a>, and <a href="/contact/">ask us for a free written quote</a>.</p>
""",
    },
    "sv": {
        "title": "Anlita en hantverkare i Axarquía utan att bränna dig",
        "meta_title": "Anlita hantverkare i Spanien: 9 råd | Handyman Axarquia",
        "desc": "Så anlitar du en pålitlig byggfirma i Spanien: nio kontroller om offert, handpenning, factura med IVA, bygglov, försäkring, referenser och garanti.",
        "excerpt": "Nästan alla behöver en hantverkare förr eller senare. Här är nio kontroller du kan använda på vilken byggfirma som helst — oss inräknade.",
        "body": """
<p>Förr eller senare behöver de flesta bostadsägare på den här kusten en hantverkare — för en läckande terrass, ett slitet badrum eller en helrenovering av något man just köpt. De skickliga är upptagna och värda att vänta på; de dåliga kostar dig dubbelt. Det här är checklistan vi skulle ge en vän som köper i Nerja, Torre del Mar eller byarna. Den fungerar på vilken byggare som helst, oss själva inkluderat — mät oss mot den.</p>

<h2>1. Kräv en tydlig skriftlig offert</h2>
<p>Ett muntligt "ungefär åttatusen" är ingen offert. Be om ett skriftligt pris för hela jobbet, med en giltighetstid, som tydligt anger vad som ingår och inte ingår — arbete, material, bortforsling, bygglov och IVA (moms). En ordentlig skriftlig offert visar att byggaren faktiskt har tänkt igenom jobbet, och den skyddar båda parter när ett beslut måste fattas halvvägs. Om någon bara ger en enda rund summa i telefon, eller klottrar den på baksidan av ett kvitto, säger det en hel del om hur resten av jobbet kommer att gå. Våra egna offerter är kostnadsfria, skriftliga och gäller i 30 dagar.</p>

<h2>2. Förstå handpenning och delbetalningar</h2>
<p>I Spanien är det helt normalt att betala en handpenning i förskott — ofta omkring 50 % — eftersom byggaren köper material, porslin och kakel innan första dagen på plats. Det som inte är normalt är att bli ombedd att betala 100 % innan något arbete börjat. Ett rimligt upplägg är en handpenning för att boka och köpa material, en eller två delbetalningar kopplade till etapper på ett längre jobb, och slutbetalning först när arbetet är klart och du är nöjd. Vi arbetar precis så: 50 % för att boka, resten vid färdigställande.</p>

<h2>3. Begär en factura med IVA</h2>
<p>Ibland erbjuds du ett lägre pris "sin IVA" — kontant, utan faktura. Det är frestande och det är en falsk besparing. Utan factura har du inget bevis på att arbetet utförts, ingen möjlighet till reklamation om det brister, och inget att visa köparens advokat när du säljer — förbättringar du inte kan styrka kan krångla till både försäljningen och din reavinst. Betala momsen, lägg fakturorna i samma mapp som din escritura och tacka dig själv senare.</p>

<h2>4. Se till att bygglovet står i offerten</h2>
<p>Nästan alla jobb kräver någon form av tillstånd, och offerten bör ange vilket — en licencia de obra menor för de flesta renoveringar, en obra mayor med arkitekt för allt som är bärande. En byggare som viftar bort bygglov är en byggare som lämnar dig med böterna, eller problemet vid försäljning. Är du osäker på vad ditt jobb kräver förklarar vår guide om <a href="/sv/blogg/bygglov-spanien-obra-menor-obra-mayor/">obra menor och obra mayor</a> det på enkel svenska.</p>

<h2>5. Fråga om försäkring och ansvar</h2>
<p>Om ett sprucket rör under din badrumsrenovering översvämmar lägenheten under — vem betalar? En professionell byggare har ansvarsförsäkring och tar ansvar för skador som arbetet orsakar. Ställ frågan rakt ut. I ett lägenhetshus spelar det ännu större roll, eftersom grannens tak är byggarens risk, inte din.</p>

<h2>6. Be att få se referenser och tidigare arbeten</h2>
<p>Bilder på färdiga jobb, en Google-profil med omdömen, telefonnumret till en tidigare kund som vill prata med dig — en byggare med meritlista kan visa alla tre utan att tveka. Läs omdömena för vad de säger om kommunikation och ordning, inte bara betyget. Vem som helst kan ha en bra bild; leta efter en sammanhängande mängd arbeten.</p>

<h2>7. Kom överens om kommunikationen innan ni börjar</h2>
<p>Om du är utomlands större delen av året är kommunikationen hela jobbet. Bestäm från start hur du ska hållas informerad — för oss betyder det bilduppdateringar på WhatsApp medan arbetet fortskrider, så att du kan se kaklet läggas och porslinet monteras utan att flyga hit. En byggare som blir tyst i två veckor medan du är i Stockholm säger dig något.</p>

<h2>8. Få garantin skriftligt</h2>
<p>Hantverket ska vara garanterat, och garantin ska stå på papper. Vår är tolv månader på arbetet, och material behåller dessutom tillverkarens garanti. Ett muntligt "oroa dig inte, jag kommer tillbaka om det blir problem" är värt exakt ingenting i februari när byggaren slutat svara.</p>

<h2>9. Vet vad du gör om det går fel</h2>
<p>De flesta jobb går bra. Om ett inte gör det, för anteckningar skriftligt — din offert, dina fakturor, daterade bilder och dina meddelanden. Ta upp problemet skriftligt och ge byggaren en rimlig chans att rätta till det; de flesta tvister är missförstånd som ett lugnt mejl löser. Går det inte att lösa har Spanien ett system för konsumenttvister, varje kommun har ett OMIC (kommunalt konsumentkontor) och Junta de Andalucía driver en regional konsumenttjänst. Det här är allmän vägledning, inte juridisk rådgivning — men att veta att vägen finns förändrar samtalet.</p>

<h2>Den tysta poängen</h2>
<p>Läs listan igen så ser du att den bara beskriver hur en seriös byggare redan arbetar: allt nedskrivet, förnuftiga betalningar, ordentliga papper, ärliga uppdateringar, en garanti. Vi byggde vårt arbetssätt kring just de förväntningarna, för kunderna som ställer de här frågorna är de kunder vi trivs med. Samlar du in offerter för ett projekt någonstans mellan Rincón de la Victoria och Nerja — ställ de nio frågorna ovan till varje byggare, och se vem som svarar rent.</p>

<p>Planerar du en renovering och vill ha en offert du faktiskt kan jämföra? <a href="/sv/renoveringar/">Läs hur vi sköter helrenoveringar</a>, titta på våra arbeten i <a href="/sv/omraden/nerja/">Nerja</a> och <a href="/sv/kontakt/">be oss om en kostnadsfri skriftlig offert</a>.</p>
""",
    },
},
{
    "slug": "winter-maintenance-spanish-holiday-home",
    "slug_sv": "vinterunderhall-semesterbostad-spanien",
    "date": "2026-09-09",
    "img": (f"{_G}/handyman-axarquia-terrace-planters-after.webp",
            "Roof terrace re-tiled with built-in planters — after",
            "Omlagd takterrass med inbyggda planteringslådor — efter"),
    "en": {
        "title": "Winter maintenance for a Spanish holiday home you only visit twice a year",
        "meta_title": "Winterising a Spanish Holiday Home | Handyman Axarquia",
        "desc": "A room-by-room autumn checklist for a Spanish holiday home left empty over winter: drains, condensation, water off, salt air and pool — from a local builder.",
        "excerpt": "Closing up a Costa del Sol home for the winter? A room-by-room checklist for October and November — and the jobs a key-holder should do while you are away.",
        "body": """
<p>A holiday home you visit twice a year is easiest to look after in the autumn, before the first serious rain. Spend a day in October or November getting it right and you avoid the two classic winter disasters: a terrace that floods into the room below, and a flat you open in spring to find furred with black mould. Here is the room-by-room checklist we run through, and what to hand to whoever holds your keys.</p>

<h2>Outside first: drains, gutters and the terrace</h2>
<p>Most winter damage on this coast comes from water that could not get away. Before the rains, clear every terrace drain, gully and gutter of leaves and grit, and check the falls actually run to the outlet rather than pooling against a wall. Look at the terrace surface itself: cracked grout, lifting tiles or a failed joint at the upstand is where water gets under the waterproofing and into the ceiling below. If your terrace has leaked before, autumn is the time to fix it properly rather than watch it happen again — it is the single most common leak we are called to, and one of the causes in our <a href="/blog/damp-in-spanish-house-causes-and-fixes/">guide to damp</a>.</p>

<h2>Air and damp: the empty-flat problem</h2>
<p>A sealed apartment with no heating, on a coast where winter humidity sits above 80%, will grow mould in cold corners and behind wardrobes. The cheapest defence is air movement: leave internal doors and wardrobe doors open, and fit trickle vents or leave a humidity-controlled extractor running. For a property empty for months, a dehumidifier on a timer or humidistat pays for itself the first winter. Pull furniture a few centimetres off external walls so air can pass behind it.</p>

<h2>Water and the heater</h2>
<p>Turn the water off at the stopcock before you leave — a slow leak or a failed flexible hose does far less damage when the supply is dead. Drain a little from the taps, and switch the water heater off at the breaker rather than leaving it cycling for months in an empty flat. If you are on a well or deposit system in the campo, isolate the pump too.</p>

<h2>Salt air: render and metalwork</h2>
<p>Give the outside a walk-round. Salt air works constantly on this coast: look for hairline cracks and blown patches in the render, rust weeping from railings, gates and window bars, and tired sealant around window frames. None of it is urgent in October, but a photo now means you can plan a repair for spring rather than discover a real problem in July. Failed render lets water behind the wall, so it is worth catching early.</p>

<h2>Pool and garden</h2>
<p>If you have a pool, get the cover on and the pump and timer set for winter, or arrange a maintenance visit — a green pool in March costs more to recover than to keep ticking over. Cut back planting from the walls, because vegetation against render holds damp, and lift or secure anything on the terrace that a levante wind will throw around.</p>

<h2>Shutters, locks and security</h2>
<p>Close the persianas most of the way but not fully — a little airflow beats a sealed box — and check that every lock and window actually fastens. Damp swells timber and warps cheap frames, so a door that shut in September may not in December. A visible, cared-for property is also a less tempting one.</p>

<h2>Give your key-holder a monthly list</h2>
<p>Whoever holds your keys — an agent, a neighbour, a friend — can catch a small problem before it becomes a claim. A sensible monthly walk-round: open up and air the property, look at ceilings under the terrace and around windows for new stains, run the taps briefly, check nothing is leaking under the sinks or the heater, and glance at the pool. Ten minutes a month is cheap insurance against a winter of quiet water damage.</p>

<h2>A pre-winter visit, done for you</h2>
<p>If you would rather not do this from abroad, it is exactly the kind of job we are asked for every October: a fixed pre-winter check where we clear the drains, test the terrace, sort the ventilation, shut down the water and heater and send you photos of anything that needs attention before the rain. We can quote for a one-off visit or a check that repeats each year — tell us the property and how it is left. The same team looks after homes from Torre del Mar through <a href="/areas/torrox/">Torrox</a> and the villages, and any repairs we spot are priced in writing before we touch anything.</p>

<p>Want the terrace, render or ventilation sorted before winter? <a href="/plastering/">See our plastering and damp-repair work</a> and our <a href="/tiling/">terrace tiling and waterproofing</a>, or <a href="/contact/">ask us for a pre-winter check</a>.</p>
""",
    },
    "sv": {
        "title": "Vinterunderhåll för en spansk semesterbostad du bara besöker två gånger om året",
        "meta_title": "Vinterunderhåll semesterbostad Spanien | Handyman Axarquia",
        "desc": "En rum-för-rum-checklista i oktober för en semesterbostad på Costa del Sol som står tom över vintern: avrinning, kondens, avstängt vatten, salt luft och pool.",
        "excerpt": "Ska du stänga bostaden i Spanien för vintern? En rum-för-rum-checklista för oktober och november — och vad en nyckelperson bör kontrollera medan du är borta.",
        "body": """
<p>En semesterbostad du besöker två gånger om året är enklast att sköta på hösten, innan det första riktiga regnet. Lägg en dag i oktober eller november på att göra rätt så slipper du vinterns två klassiker: en terrass som läcker ner i rummet under, och en lägenhet du öppnar på våren och finner täckt av svart mögel. Här är checklistan vi går igenom rum för rum, och vad du lämnar till den som håller dina nycklar.</p>

<h2>Utomhus först: avrinning, hängrännor och terrassen</h2>
<p>Det mesta av vinterns skador på den här kusten kommer från vatten som inte kunde rinna undan. Före regnen, rensa varje terrassbrunn, ränna och hängränna från löv och grus, och kontrollera att fallet faktiskt leder mot brunnen i stället för att samlas mot en vägg. Titta på själva terrassytan: sprucken fog, plattor som lyfter eller en trasig fog vid uppkanten är där vatten tar sig under tätskiktet och in i taket under. Har din terrass läckt tidigare är hösten rätt tid att åtgärda det ordentligt i stället för att se det hända igen — det är den vanligaste läckan vi kallas till, och en av orsakerna i vår <a href="/sv/blogg/fukt-i-huset-spanien-orsaker-och-losningar/">guide om fukt</a>.</p>

<h2>Luft och fukt: problemet med den tomma lägenheten</h2>
<p>En tillsluten lägenhet utan värme, på en kust där vinterfuktigheten ligger över 80 %, får mögel i kalla hörn och bakom garderober. Det billigaste försvaret är luftrörelse: lämna innerdörrar och garderobsdörrar öppna, och sätt in spaltventiler eller låt en fuktstyrd fläkt gå. För en bostad som står tom i månader betalar sig en avfuktare på timer eller fuktstyrning första vintern. Dra ut möbler någon centimeter från ytterväggarna så att luft kan passera bakom dem.</p>

<h2>Vatten och beredaren</h2>
<p>Stäng av vattnet vid huvudkranen innan du åker — ett långsamt läckage eller en trasig slang gör mycket mindre skada när tillförseln är död. Tappa ur lite från kranarna, och stäng av varmvattenberedaren vid proppen i stället för att låta den gå i månader i en tom lägenhet. Har du brunn eller tanksystem på landet, isolera pumpen också.</p>

<h2>Salt luft: puts och metall</h2>
<p>Gå ett varv runt utsidan. Salt luft arbetar oavbrutet på den här kusten: leta efter hårfina sprickor och bortsprängda partier i putsen, rost som rinner från räcken, grindar och fönstergaller, och sliten fogmassa runt fönsterkarmar. Inget av det är akut i oktober, men en bild nu betyder att du kan planera en reparation till våren i stället för att upptäcka ett verkligt problem i juli. Sprucken puts släpper in vatten bakom väggen, så det lönar sig att fånga det tidigt.</p>

<h2>Pool och trädgård</h2>
<p>Har du pool, få på skyddet och ställ in pump och timer för vintern, eller ordna ett servicebesök — en grön pool i mars kostar mer att rädda än att hålla igång. Skär bort växtlighet från väggarna, eftersom grönska mot puts håller kvar fukt, och lyft in eller säkra allt på terrassen som en levantevind kastar omkring.</p>

<h2>Persienner, lås och säkerhet</h2>
<p>Dra ner persiennerna nästan helt men inte helt — lite luftväxling slår en tillsluten låda — och kontrollera att varje lås och fönster verkligen går att stänga. Fukt sväller trä och skevar billiga karmar, så en dörr som stängde i september gör det kanske inte i december. En bebodd och omhändertagen bostad är också en mindre lockande.</p>

<h2>Ge din nyckelperson en månadslista</h2>
<p>Den som håller dina nycklar — en mäklare, en granne, en vän — kan fånga ett litet problem innan det blir ett skadeärende. Ett vettigt månadsvarv: öppna och vädra bostaden, titta på taken under terrassen och runt fönstren efter nya fläckar, spola kranarna en stund, kontrollera att inget läcker under handfaten eller beredaren, och kika på poolen. Tio minuter i månaden är billig försäkring mot en vinter av tyst vattenskada.</p>

<h2>Ett förvintercheck, gjort åt dig</h2>
<p>Vill du hellre slippa göra det här från utlandet är det precis den sortens jobb vi får varje oktober: ett fast förvintercheck där vi rensar brunnarna, testar terrassen, ordnar ventilationen, stänger av vatten och beredare och skickar bilder på allt som behöver åtgärdas före regnet. Vi offererar ett engångsbesök eller ett check som återkommer varje år — berätta om bostaden och hur den lämnas. Samma team sköter hem från Torre del Mar via <a href="/sv/omraden/torrox/">Torrox</a> och byarna, och eventuella reparationer vi hittar prissätts skriftligt innan vi rör något.</p>

<p>Vill du få terrass, puts eller ventilation åtgärdad före vintern? <a href="/sv/putsarbeten/">Läs om våra puts- och fuktarbeten</a> och vår <a href="/sv/kakel/">plattsättning och tätning av terrasser</a>, eller <a href="/sv/kontakt/">be oss om ett förvintercheck</a>.</p>
""",
    },
},
{
    "slug": "holiday-rental-pre-season-checklist-axarquia",
    "slug_sv": "forbereda-uthyrningsbostad-sasong-spanien",
    "date": "2026-09-09",
    "img": (f"{_G}/handyman-axarquia-bathroom-reform-2-after.webp",
            "Renovated bathroom with a double vanity unit — after",
            "Renoverat badrum med dubbelt tvättställsskåp — efter"),
    "en": {
        "title": "Pre-season checklist: getting your Axarquia holiday rental ready for summer",
        "meta_title": "Holiday Rental: Pre-Season Checklist | Handyman Axarquia",
        "desc": "The February–April jobs guests notice and reviews punish in an Axarquia holiday let: silicone and grout, tired bathrooms, terrace tiles, AC, paint and safety.",
        "excerpt": "Guests notice the small things and reviews punish them. Here are the jobs to do between winter and the season so your Axarquia rental shows well and stays booked.",
        "body": """
<p>A holiday rental is judged in photographs and reviews, and both are unforgiving about the small things — mouldy silicone, a cracked tile, a bathroom that was modern fifteen years ago. The quiet months from February to April are when the work gets done, between the winter lull and the first summer bookings. Here is the pre-season list we run for owners across the Axarquia, roughly in the order guests notice it.</p>

<h2>Silicone, grout and sealant</h2>
<p>Nothing says "tired" faster than black silicone around a bath or discoloured grout on a shower wall, and nothing is cheaper to put right. Raking out and renewing the silicone and regrouting the wet areas is a small job that transforms how clean a bathroom photographs and feels. It also stops water tracking behind the tiles, which is how a cosmetic problem becomes a structural one.</p>

<h2>The bathroom guests photograph</h2>
<p>If the bathroom is beyond a refresh, the season is the reason to replace it — it is the room that appears in every listing and the one guests complain about first. A robust mid-range refit aimed at rental use is money back in bookings and reviews. We set out what that costs in our <a href="/blog/bathroom-renovation-cost-axarquia/">guide to bathroom renovation prices</a>, so you can budget before you commit. A bath-to-walk-in-shower swap is a smaller, popular option where space is tight.</p>

<h2>Terrace tiles and lippage</h2>
<p>The terrace is where guests spend the evening, and it is also a trip hazard if tiles have lifted or a proud edge has appeared — "lippage", in the trade. Reseat loose tiles, fix any lifting edge and check the waterproofing while you are at it, because a terrace that leaks into the flat below during a busy August is the worst possible time to find out.</p>

<h2>AC and extractors</h2>
<p>Air conditioning is the first thing a summer guest tests and the fastest way to a bad review if it wheezes or smells. Have the units serviced and the filters cleaned before the season, and check the bathroom and kitchen extractors actually pull — a mould-free, fresh-smelling flat starts with airflow. We do not sell air-conditioning servicing, but we will tell you what needs it while we are on site.</p>

<h2>A paint refresh</h2>
<p>Scuffs, mystery marks and a tide of little repairs accumulate over a season of guests. A fresh coat on the walls, or at least the high-traffic rooms, resets the whole property for a day's labour and a few litres of paint. Neutral, hard-wearing and easy to touch up beats fashionable every time in a rental.</p>

<h2>The safety items</h2>
<p>Guests of every age use a rental, so the boring safety details matter: a grab rail by a step-in shower, secure handrails on terraces and stairs, level access where you can manage it, working smoke detection and no trailing edges to trip on. They rarely appear in reviews when they are right, and always when they are wrong.</p>

<h2>Planning it between bookings</h2>
<p>The trick with a working rental is fitting the work into the gaps. Tell us your calendar — a two-week window in March, or the run before your first June booking — and we quote with a firm start and finish so you can keep the diary open around it. If you are abroad, we collect keys from your agent, send photo updates as we go and leave the place guest-ready and clean, the same way we work for owners in <a href="/areas/nerja/">Nerja</a> and <a href="/areas/torre-del-mar/">Torre del Mar</a>, the two busiest rental markets we serve. Get the big jobs done now and the winter <a href="/blog/winter-maintenance-spanish-holiday-home/">close-up</a> becomes a formality.</p>

<p>Want your rental refreshed before the season? <a href="/bathrooms/">See our bathroom renovations</a> or <a href="/contact/">send us your calendar and a few photos</a> for a free written quote.</p>
""",
    },
    "sv": {
        "title": "Inför säsongen: få din uthyrningsbostad i Axarquía klar till sommaren",
        "meta_title": "Uthyrningsbostad klar inför säsongen | Handyman Axarquia",
        "desc": "Jobben mellan februari och april som gäster märker och omdömen bestraffar i en uthyrningsbostad: silikon och fog, slitna badrum, terrassplattor, AC och färg.",
        "excerpt": "Gäster märker det små och omdömen bestraffar det. Här är jobben att göra mellan vinter och säsong så att din uthyrningsbostad i Axarquía visar sig från sin bästa sida.",
        "body": """
<p>En uthyrningsbostad bedöms i bilder och omdömen, och båda är obarmhärtiga mot det små — möglig silikon, en sprucken platta, ett badrum som var modernt för femton år sedan. De lugna månaderna från februari till april är när arbetet görs, mellan vinterns stiltje och de första sommarbokningarna. Här är listan vi går igenom åt ägare i hela Axarquía, ungefär i den ordning gästerna märker det.</p>

<h2>Silikon, fog och tätning</h2>
<p>Inget säger "slitet" snabbare än svart silikon runt ett badkar eller missfärgad fog på en duschvägg, och inget är billigare att åtgärda. Att skära ur och förnya silikonen och foga om våtzonerna är ett litet jobb som förändrar hur rent ett badrum ser ut och känns. Det stoppar också vatten från att vandra bakom kaklet, som är hur ett kosmetiskt problem blir ett strukturellt.</p>

<h2>Badrummet gästerna fotograferar</h2>
<p>Är badrummet bortom en uppfräschning är säsongen skälet att byta det — det är rummet som syns i varje annons och det gästerna klagar på först. En robust renovering i mellanklass anpassad för uthyrning är pengar tillbaka i bokningar och omdömen. Vi går igenom vad det kostar i vår <a href="/sv/blogg/vad-kostar-badrumsrenovering-axarquia/">prisguide för badrumsrenovering</a>, så att du kan budgetera innan du bestämmer dig. Att byta badkar mot walk-in-dusch är ett mindre, populärt alternativ där ytan är knapp.</p>

<h2>Terrassplattor och nivåskillnader</h2>
<p>Terrassen är där gästerna sitter på kvällen, och den är också en snubbelrisk om plattor lyft eller en kant sticker upp. Lägg om lösa plattor, åtgärda en lyftande kant och kontrollera tätskiktet medan du ändå är där — en terrass som läcker ner till lägenheten under en fullbokad augusti är sämsta tänkbara tillfälle att upptäcka det.</p>

<h2>AC och fläktar</h2>
<p>Luftkonditioneringen är det första en sommargäst provar och den snabbaste vägen till ett dåligt omdöme om den kämpar eller luktar. Låt serva enheterna och rengöra filtren före säsongen, och kontrollera att fläktarna i badrum och kök verkligen drar — en mögelfri, fräsch bostad börjar med luftväxling. Vi säljer inte AC-service, men vi säger vad som behöver det medan vi är på plats.</p>

<h2>En uppfräschning med färg</h2>
<p>Skrapmärken, mystiska fläckar och en flod av små skador samlas under en säsong av gäster. En ny strykning på väggarna, eller åtminstone i de mest trafikerade rummen, nollställer hela bostaden på en dags arbete och några liter färg. Neutralt, tåligt och lätt att bättra slår trendigt varje gång i en uthyrningsbostad.</p>

<h2>Säkerhetsdetaljerna</h2>
<p>Gäster i alla åldrar använder en uthyrningsbostad, så de tråkiga säkerhetsdetaljerna spelar roll: ett stödhandtag vid en dusch med hög kant, säkra räcken på terrasser och trappor, nivåfri åtkomst där du kan ordna det, fungerande brandvarnare och inga lösa kanter att snubbla på. De syns sällan i omdömen när de är rätt, och alltid när de är fel.</p>

<h2>Planera det mellan bokningarna</h2>
<p>Konsten med en uthyrningsbostad i drift är att pussla in arbetet i luckorna. Berätta din kalender — ett fönster på två veckor i mars, eller sträckan före din första junibokning — så offererar vi med fast start och slut så att du kan hålla kalendern öppen runt om. Är du utomlands hämtar vi nyckel hos din mäklare, skickar bilduppdateringar och lämnar bostaden gästklar och städad, precis som vi arbetar åt ägare i <a href="/sv/omraden/nerja/">Nerja</a> och <a href="/sv/omraden/torre-del-mar/">Torre del Mar</a>, de två livligaste uthyrningsmarknaderna vi täcker. Få de stora jobben gjorda nu så blir vinterns <a href="/sv/blogg/vinterunderhall-semesterbostad-spanien/">stängning</a> en formalitet.</p>

<p>Vill du fräscha upp din uthyrningsbostad före säsongen? <a href="/sv/badrum/">Läs om våra badrumsrenoveringar</a> eller <a href="/sv/kontakt/">skicka din kalender och några bilder</a> för en kostnadsfri skriftlig offert.</p>
""",
    },
},
{
    "slug": "rendering-vs-plastering-costa-del-sol",
    "slug_sv": "fasadputs-costa-del-sol-varfor-den-spricker",
    "date": "2026-09-09",
    "img": (f"{_O}/axarquia-handyman-reform-garden-wall-repair-render-repaint-after.webp",
            "Exterior wall re-rendered and repainted after cracking — after",
            "Yttervägg omputsad och ommålad efter sprickbildning — efter"),
    "en": {
        "title": "Rendering vs plastering: why exterior walls fail on the Costa del Sol coast",
        "meta_title": "Rendering vs Plastering: Why Walls Fail | Handyman Axarquia",
        "desc": "What render and plaster are, why cement render traps damp in old walls, monocapa and lime explained, and when a coastal wall needs a repair or a re-render.",
        "excerpt": "Render and plaster are not the same thing, and the wrong one on an old wall causes damp. Here is how exterior walls fail on this coast, and what actually lasts.",
        "body": """
<p>"Rendering" and "plastering" get used interchangeably, but they are different jobs with different materials, and getting them wrong is behind a surprising amount of the damp we are called to. Plaster is the smooth finish on the inside of your walls; render is the tougher coat on the outside that takes the weather. On the Costa del Sol, where salt air and hard sun attack a wall from the day it is finished, the choice of render decides whether it lasts five years or twenty-five.</p>

<h2>Render, plaster and why the difference matters</h2>
<p>Internal plaster — traditionally gypsum, or lime in older houses — is about a flat, paintable surface. External render is structural weather protection: it sheds rain, handles movement and, crucially, has to let the wall behind it breathe. When people ask us to "re-plaster" an outside wall, what they actually need is the right render for the wall they have.</p>

<h2>The cement-render trap on old walls</h2>
<p>The most common mistake on village and country houses is a hard cement render slapped over old stone or earth walls. It looks solid and it causes damp: these walls were built to breathe, drawing moisture up and letting it evaporate through the surface. Seal them in cement and the water has nowhere to go — it rises higher, salts crystallise, and the render eventually blows off in sheets, taking your paint with it. It is one of the six causes in our <a href="/blog/damp-in-spanish-house-causes-and-fixes/">guide to damp in Spanish homes</a>, and it is entirely avoidable.</p>

<h2>Monocapa, lime and breathable paint</h2>
<p>The right material depends on the wall. On modern block and brick, <em>monocapa</em> — a single-coat coloured render — is the standard: durable, self-coloured so it does not need painting, and well suited to new construction. On old stone and earth walls, a traditional lime-based render is the honest choice: it is softer, flexes with the wall and lets it dry through the surface. Finish either with a breathable (vapour-permeable) masonry paint, not a plastic film that traps moisture, and the wall stays dry from the inside out.</p>

<h2>Why coastal walls crack</h2>
<p>Even a good render moves. Sun heats a south-facing wall through the day and it cools sharply at night; that constant expansion and contraction, plus salt working into the surface, opens the hairline cracks you see across the coast. Most are cosmetic — a sign the surface is working, not failing. It is the wider cracks, the hollow-sounding patches and the damp appearing inside on the same wall that mean water is getting behind the render.</p>

<h2>Repair or re-render?</h2>
<p>Not every tired wall needs stripping back. If the render is largely sound with local cracking, a cut-out-and-patch repair, re-point and breathable repaint will see it good for years. If it is hollow over large areas, blown, or letting damp through, patching only chases the problem around the wall — that is when a full re-render earns its cost. We tap the wall, look at what is happening inside, and tell you honestly which one you are looking at. Telling harmless cracks from serious ones is a subject of its own, which we cover in our piece on <a href="/blog/cracks-in-walls-spanish-house/">cracks in Spanish walls</a>.</p>

<h2>How long it takes, and when to do it</h2>
<p>A typical exterior re-render is priced per job after a visit — wall area, access, scaffolding and the state of the substrate vary too much for a square-metre figure to mean anything. On timing, autumn and spring are ideal: renders and lime finishes need moderate temperatures and time to cure, and neither high-summer heat nor a wet winter week is kind to a fresh coat. We work on village and country walls across <a href="/areas/frigiliana/">Frigiliana and the inland villages</a>, where old construction and steep, damp-prone plots make the right render matter most.</p>

<p>Got cracked, blown or damp render? <a href="/plastering/">See our plastering and rendering service</a> or <a href="/contact/">send us a photo of the wall</a> and we will tell you whether it is a repair or a re-render, in writing.</p>
""",
    },
    "sv": {
        "title": "Fasadputs på Costa del Sol: varför ytterväggar spricker och släpper",
        "meta_title": "Fasadputs som spricker på Costa del Sol | Handyman Axarquia",
        "desc": "Vad puts och fasadputs är, varför cementputs stänger in fukt i gamla väggar, monocapa och kalk förklarat, och när en fasad behöver lagas eller putsas om helt.",
        "excerpt": "Puts och fasadputs är inte samma sak, och fel val på en gammal vägg ger fukt. Så här går ytterväggar sönder på den här kusten, och vad som faktiskt håller.",
        "body": """
<p>"Puts" och "fasadputs" används om vartannat, men det är olika jobb med olika material, och att välja fel ligger bakom förvånansvärt mycket av den fukt vi kallas till. Puts är den släta ytan på insidan av dina väggar; fasadputs är det tåligare skiktet på utsidan som tar vädret. På Costa del Sol, där salt luft och hård sol angriper en vägg från dagen den är klar, avgör valet av fasadputs om den håller i fem år eller tjugofem.</p>

<h2>Puts, fasadputs och varför skillnaden spelar roll</h2>
<p>Invändig puts — traditionellt gips, eller kalk i äldre hus — handlar om en slät, målningsbar yta. Utvändig fasadputs är strukturellt väderskydd: den leder bort regn, hanterar rörelse och, framför allt, måste låta väggen bakom andas. När någon ber oss "putsa om" en yttervägg är det rätt fasadputs för väggen de faktiskt har som de behöver.</p>

<h2>Cementputsfällan på gamla väggar</h2>
<p>Det vanligaste misstaget på by- och lanthus är en hård cementputs slängd över gamla sten- eller jordväggar. Den ser stabil ut och den ger fukt: dessa väggar byggdes för att andas, dra upp fukt och låta den avdunsta genom ytan. Stäng in dem i cement och vattnet har ingenstans att ta vägen — det stiger högre, salter kristalliserar och putsen sprängs till slut av i sjok, med din färg på köpet. Det är en av de sex orsakerna i vår <a href="/sv/blogg/fukt-i-huset-spanien-orsaker-och-losningar/">guide om fukt i spanska hus</a>, och den är fullt möjlig att undvika.</p>

<h2>Monocapa, kalk och andande färg</h2>
<p>Rätt material beror på väggen. På modernt block och tegel är <em>monocapa</em> — en enkelskikts färgad fasadputs — standard: tålig, egenfärgad så att den inte behöver målas, och väl lämpad för nybyggnation. På gamla sten- och jordväggar är en traditionell kalkbaserad puts det ärliga valet: den är mjukare, rör sig med väggen och låter den torka genom ytan. Avsluta endera med en andande (ånggenomsläpplig) fasadfärg, inte en plastfilm som stänger in fukt, så håller sig väggen torr inifrån och ut.</p>

<h2>Varför kustväggar spricker</h2>
<p>Även en bra fasadputs rör sig. Solen värmer en söderfasad under dagen och den kyls kraftigt på natten; den ständiga utvidgningen och sammandragningen, plus salt som arbetar in i ytan, öppnar de hårfina sprickor du ser längs kusten. De flesta är kosmetiska — ett tecken på att ytan arbetar, inte havererar. Det är de bredare sprickorna, de ihåliga partierna och fukten som dyker upp inomhus på samma vägg som betyder att vatten tar sig bakom putsen.</p>

<h2>Laga eller putsa om?</h2>
<p>Inte varje sliten vägg behöver rivas ner. Är putsen i stort sett hel med lokala sprickor räcker det ofta att skära ur och laga, foga om och måla om med en andande färg i flera år framåt. Är den ihålig över stora ytor, bortsprängd eller släpper fukt jagar en lagning bara problemet runt väggen — då förtjänar en fullständig omputsning sin kostnad. Vi knackar på väggen, ser vad som händer inuti och säger ärligt vilket av dem du har framför dig. Att skilja ofarliga sprickor från allvarliga är ett ämne i sig, som vi tar upp i vårt inlägg om <a href="/sv/blogg/sprickor-i-vaggen-spanien/">sprickor i spanska väggar</a>.</p>

<h2>Hur lång tid det tar, och när</h2>
<p>En vanlig utvändig omputsning prissätts per jobb efter ett besök — väggyta, åtkomst, ställning och underlagets skick varierar för mycket för att en kvadratmetersiffra ska betyda något. När det gäller tidpunkt är höst och vår idealiska: puts och kalkytor behöver måttliga temperaturer och tid att härda, och varken högsommarhetta eller en blöt vintervecka är snäll mot ett färskt skikt. Vi arbetar på by- och lantväggar i <a href="/sv/omraden/frigiliana/">Frigiliana och byarna inåt landet</a>, där gammal konstruktion och branta, fuktkänsliga tomter gör rätt fasadputs viktigast.</p>

<p>Har du sprucken, bortsprängd eller fuktig fasadputs? <a href="/sv/putsarbeten/">Läs om våra puts- och fasadarbeten</a> eller <a href="/sv/kontakt/">skicka en bild på väggen</a> så säger vi om det är en lagning eller en omputsning, skriftligt.</p>
""",
    },
},
{
    "slug": "house-extension-spain-cost-per-m2",
    "slug_sv": "bygga-ut-hus-spanien-kostnad",
    "date": "2026-09-09",
    "img": (f"{_G}/handyman-axarquia-pergola-vinuela-after.webp",
            "New timber pergola on a country property in Viñuela — after",
            "Ny pergola i trä på en landsbygdsfastighet i Viñuela — efter"),
    "en": {
        "title": "Extending your house in Spain: what's possible, what's not, and what it costs per m²",
        "meta_title": "Extending a House in Spain: Rules & Cost | Handyman Axarquia",
        "desc": "Urban vs rural land, how much you may build, the routes from pergola to extension, obra mayor and architect, and the €1,000–€1,600/m² guide for the Axarquia.",
        "excerpt": "Can you extend your Spanish house, and what does it cost per square metre? A plain guide to urban and rural land, the realistic routes, licences and budgets.",
        "body": """
<p>"Can I add a room?" is one of the best questions an owner can ask, because the answer shapes whether you extend or move. In Spain it depends less on the house than on the land it sits on and what the town hall allows there. Here is how extensions actually work in the Axarquia, the routes people take, and the per-square-metre figure to budget around.</p>

<h2>Urban land or rural land — the first question</h2>
<p>Everything starts with whether your plot is <em>suelo urbano</em> (urban) or <em>suelo rústico</em> (rural). On urban land — most apartments, townhouses and estate homes — extending is normal, within the limits the town hall sets. On rural land, where many campo houses and cortijos sit, new built area is tightly controlled: repairs, pergolas and some conversions of existing space are often fine, but a new extension frequently is not. We tell every campo owner what is realistic at the first visit, before anyone falls for a plan — the same honest conversation we describe on our <a href="/areas/velez-malaga/">Vélez-Málaga and villages</a> page.</p>

<h2>How much you're allowed to build</h2>
<p>Even on urban land you cannot build to the boundary or as high as you like. The town hall sets the <em>edificabilidad</em> — how much floor area you may build on your plot — along with height limits, setbacks and how much of the plot must stay open. Your existing house may already use most of your allowance, or leave room for a good deal more. Checking this at the town hall is the first thing an architect does, and it is what turns "I'd love a second floor" into a real yes or no.</p>

<h2>The routes people take</h2>
<ul class="tick">
<li><strong>Covered terrace or pergola.</strong> The cheapest way to gain usable space — outdoor living, shade and shelter — often achievable as minor works or a light structure rather than a full extension.</li>
<li><strong>Garage or storeroom conversion.</strong> Turning existing space into a bedroom, office or bathroom is usually the best value, because the shell already exists; the work is insulation, damp-proofing, ventilation, electrics and finishes.</li>
<li><strong>Single-storey extension.</strong> Adding footprint to a house — a bigger kitchen, an extra bedroom — where your plot and allowance permit.</li>
<li><strong>Roof terrace or solarium.</strong> Making use of a flat roof, with proper waterproofing and access, for the view and the sun.</li>
</ul>

<h2>Obra mayor and the architect</h2>
<p>Anything that adds built volume or touches the structure is an <em>obra mayor</em>: it needs a project drawn and signed by an architect, usually an aparejador to supervise, and a full licence from the town hall. That sounds heavier than it is — we introduce you to local architects we work with regularly and coordinate the build alongside their paperwork, so the two move together. Our <a href="/blog/building-licence-spain-obra-menor-obra-mayor/">guide to building licences</a> explains where the line between minor and major works falls.</p>

<h2>What it costs, and how long</h2>
<p>As a planning figure, a new extension in the Axarquia runs roughly <strong>€1,000 to €1,600 per square metre</strong> for the build, plus the architect's fees and the licence on top. Where you land in that band depends on foundations, finishes, glazing and how much glass and structural opening you want between old and new. On timing, the build itself is usually six to ten weeks once the licence is granted — but remember the licence for an obra mayor can take months, so start the paperwork early.</p>

<h2>Building for the climate</h2>
<p>An extension here is not a British or Swedish extension with more sun. It wants insulation and shading designed for 40-degree summers as much as for winter, cross-ventilation to move the heat, and proper damp-proofing against driving winter rain and salt air. Get those right at design stage and the new room is the coolest, most comfortable part of the house; get them wrong and it bakes in July and sweats in January. We build with the local climate in mind because we live in it.</p>

<p>Thinking about more space? <a href="/extensions/">See our extensions, conversions and pergolas</a> or <a href="/contact/">tell us about your plot</a> and we will tell you honestly what is possible, and quote it in writing.</p>
""",
    },
    "sv": {
        "title": "Bygga ut hus i Spanien: vad som är möjligt, vad som inte är det och vad det kostar per m²",
        "meta_title": "Bygga ut hus i Spanien: regler & kostnad | Handyman Axarquia",
        "desc": "Stadsmark eller landsbygdsmark, hur mycket du får bygga, vägarna från pergola till tillbyggnad, obra mayor och arkitekt, och riktmärket 1 000–1 600 euro/m².",
        "excerpt": "Kan du bygga ut ditt spanska hus, och vad kostar det per kvadratmeter? En enkel guide till stads- och landsbygdsmark, de realistiska vägarna, bygglov och budget.",
        "body": """
<p>"Kan jag lägga till ett rum?" är en av de bästa frågor en ägare kan ställa, för svaret avgör om du bygger ut eller flyttar. I Spanien beror det mindre på huset än på marken det står på och vad kommunen tillåter där. Här är hur tillbyggnader faktiskt fungerar i Axarquía, vägarna folk tar, och siffran per kvadratmeter att budgetera kring.</p>

<h2>Stadsmark eller landsbygdsmark — första frågan</h2>
<p>Allt börjar med om din tomt är <em>suelo urbano</em> (stadsmark) eller <em>suelo rústico</em> (landsbygdsmark). På stadsmark — de flesta lägenheter, radhus och villor i bostadsområden — är det normalt att bygga ut, inom de gränser kommunen sätter. På landsbygdsmark, där många lanthus och cortijos ligger, är ny byggyta hårt reglerad: reparationer, pergolor och vissa ombyggnader av befintlig yta är ofta möjliga, men en ny tillbyggnad är det ofta inte. Vi berättar för varje ägare på landet vad som är realistiskt redan vid första besöket, innan någon fastnar för en plan — samma ärliga samtal som vi beskriver på vår sida om <a href="/sv/omraden/velez-malaga/">Vélez-Málaga och byarna</a>.</p>

<h2>Hur mycket du får bygga</h2>
<p>Även på stadsmark får du inte bygga ända till tomtgränsen eller hur högt som helst. Kommunen sätter <em>edificabilidad</em> — hur mycket byggyta du får uppföra på din tomt — tillsammans med höjdgränser, avstånd och hur mycket av tomten som måste förbli öppen. Ditt befintliga hus kan redan använda det mesta av din tillåtna yta, eller lämna plats för betydligt mer. Att kontrollera detta hos kommunen är det första en arkitekt gör, och det som gör "jag skulle gärna vilja ha en andra våning" till ett verkligt ja eller nej.</p>

<h2>Vägarna folk tar</h2>
<ul class="tick">
<li><strong>Täckt terrass eller pergola.</strong> Det billigaste sättet att vinna användbar yta — uteliv, skugga och skydd — ofta möjligt som mindre arbeten eller en lätt konstruktion snarare än en full tillbyggnad.</li>
<li><strong>Garage- eller förrådsomvandling.</strong> Att göra befintlig yta till sovrum, kontor eller badrum är oftast bäst värde, eftersom skalet redan finns; arbetet är isolering, fuktspärr, ventilation, el och ytskikt.</li>
<li><strong>Tillbyggnad i ett plan.</strong> Att lägga till byggyta — ett större kök, ett extra sovrum — där tomt och tillåten yta medger det.</li>
<li><strong>Takterrass eller solarium.</strong> Att använda ett platt tak, med ordentligt tätskikt och åtkomst, för utsikten och solen.</li>
</ul>

<h2>Obra mayor och arkitekten</h2>
<p>Allt som lägger till byggvolym eller rör stommen är en <em>obra mayor</em>: det kräver ett projekt ritat och signerat av en arkitekt, oftast en aparejador som övervakar, och ett fullständigt bygglov från kommunen. Det låter tyngre än det är — vi presenterar dig för lokala arkitekter som vi samarbetar med regelbundet och samordnar bygget parallellt med deras papper, så att de två löper tillsammans. Vår <a href="/sv/blogg/bygglov-spanien-obra-menor-obra-mayor/">guide om bygglov</a> förklarar var gränsen mellan mindre och större arbeten går.</p>

<h2>Vad det kostar, och hur länge</h2>
<p>Som planeringssiffra ligger en ny tillbyggnad i Axarquía på ungefär <strong>1 000 till 1 600 euro per kvadratmeter</strong> för bygget, plus arkitektens arvode och bygglovet ovanpå. Var du hamnar i det spannet beror på grund, ytskikt, glas och hur mycket glas och strukturell öppning du vill ha mellan gammalt och nytt. När det gäller tid är själva bygget oftast sex till tio veckor när bygglovet är beviljat — men kom ihåg att bygglovet för en obra mayor kan ta månader, så börja med pappren tidigt.</p>

<h2>Att bygga för klimatet</h2>
<p>En tillbyggnad här är inte en svensk tillbyggnad med mer sol. Den vill ha isolering och solavskärmning tänkta för 40-gradiga somrar lika mycket som för vintern, korsventilation för att flytta värmen och ordentlig fuktspärr mot slagregn och salt luft på vintern. Får du det rätt vid ritbordet blir det nya rummet husets svalaste och skönaste del; får du det fel bakas det i juli och svettas i januari. Vi bygger med det lokala klimatet i åtanke, för vi lever i det.</p>

<p>Funderar du på mer plats? <a href="/sv/tillbyggnader/">Läs om våra tillbyggnader, ombyggnader och pergolor</a> eller <a href="/sv/kontakt/">berätta om din tomt</a> så säger vi ärligt vad som är möjligt, och offererar det skriftligt.</p>
""",
    },
},
{
    "slug": "kitchen-renovation-spain-uk-sweden-differences",
    "slug_sv": "koksrenovering-spanien-skillnader",
    "date": "2026-09-09",
    "img": (f"{_G}/handyman-axarquia-kitchen-reform-open-after.webp",
            "Open-plan kitchen reform — after",
            "Öppen köksrenovering — efter"),
    "en": {
        "title": "Kitchen renovation in Spain: five things that are different from the UK and Sweden",
        "meta_title": "Renovating a Kitchen in Spain: 5 Things | Handyman Axarquia",
        "desc": "Five ways a kitchen renovation in Spain differs from the UK and Sweden: gas vs induction, power supply, plumbing, deliveries, open-plan licences and cost.",
        "excerpt": "Fitting a kitchen in Spain is not quite the job it is back home. Five practical differences — from gas and power supply to open-plan licences — and what to budget.",
        "body": """
<p>A kitchen is where reform budgets are won and lost, and it is also the room where owners from the UK and Sweden get the most surprises, because the way it is done in Spain differs in small, practical ways. After a lot of kitchens across the Axarquia, here are the five differences worth knowing before you start — the kind of thing we would raise at the first visit, exactly as our <a href="/blog/hire-a-builder-axarquia-spain/">guide to hiring a builder</a> suggests you should expect.</p>

<h2>1. Gas, induction and how much power you actually have</h2>
<p>Many older Spanish kitchens run on bottled butane rather than mains gas, and plenty of owners now switch to induction when they reform. The catch is electrical: your home has a contracted power level — the <em>potencia contratada</em> — and induction hobs, ovens and an air-conditioning unit running together can trip a supply that was set decades ago for a gas kitchen. It is worth checking your contracted power with your electricity supplier before you design around induction; sometimes it needs increasing, which is a call to the supplier rather than a building job.</p>

<h2>2. Spanish plumbing and waste layouts</h2>
<p>Waste and water routing in Spanish apartments is often tighter and less forgiving than back home — soil stacks in fixed positions, shallow falls, and pipework buried in solid walls rather than run in stud partitions. Moving a sink or a dishwasher a couple of metres can mean more work than you expect. It is usually very doable, but it is a reason to settle the layout early rather than change your mind once the walls are open.</p>

<h2>3. Delivery lead times and who receives the kitchen</h2>
<p>Kitchen units, worktops and appliances can carry real lead times, and worktops in particular — especially stone and quartz — are often templated only after the units are in, then made to order. If you are abroad, someone has to be there to receive a large delivery and check it, and a missing filler panel can stall the whole install. We coordinate deliveries to the day and receive them on site so the kitchen arrives to a room that is actually ready for it.</p>

<h2>4. Open-plan knock-throughs need a licence</h2>
<p>The most popular kitchen change here is opening the kitchen into the living room. If the wall is not load-bearing it is straightforward; if it is, it means a beam and proper structural support, which is an <em>obra mayor</em> with the paperwork that goes with it. Either way the town hall wants a licence, and in an apartment your comunidad needs informing too. We tell you which side of that line your wall falls before we quote.</p>

<h2>5. IVA, facturas and what it costs</h2>
<p>A proper kitchen job comes with a factura and IVA — worth it for the guarantee and for your records when you sell, as we always advise. On cost, a kitchen refit where we prep and install runs roughly <strong>€3,000 to €7,000</strong>, and a complete high-end kitchen with structural or layout changes runs <strong>€8,000 to €15,000</strong>, units and appliances depending on what you choose. Every quote we give is free, in writing and valid for 30 days — a single price for the whole job, so you can plan the spec around your budget before you commit.</p>

<h2>One team for the whole job</h2>
<p>The reason kitchens go wrong is usually coordination — the plasterer waiting on the electrician waiting on the plumber, and the worktop templated against units that were not level. We run the strip-out, first fix, plastering, tiling and installation as one team on one schedule, whether you supply the kitchen or we do. It is how we work in <a href="/areas/rincon-de-la-victoria/">Rincón de la Victoria</a> and across the coast, and it is why the worktop fits.</p>

<p>Planning a new kitchen? <a href="/kitchens/">See our kitchen renovation service</a> or <a href="/contact/">send us your room size and a photo</a> for a free written quote.</p>
""",
    },
    "sv": {
        "title": "Köksrenovering i Spanien: fem saker som skiljer sig från Sverige och Storbritannien",
        "meta_title": "Köksrenovering i Spanien: 5 skillnader | Handyman Axarquia",
        "desc": "Fem sätt som en köksrenovering i Spanien skiljer sig: gas mot induktion, avloppsdragning, leveranser, öppen planlösning och bygglov, IVA och kostnad.",
        "excerpt": "Att montera ett kök i Spanien är inte riktigt jobbet det är hemma. Fem praktiska skillnader — från gas och elförsörjning till bygglov — och vad du bör budgetera.",
        "body": """
<p>Ett kök är där renoveringsbudgetar vinns och förloras, och det är också rummet där ägare från Sverige och Storbritannien får flest överraskningar, eftersom sättet det görs på i Spanien skiljer sig på små, praktiska vis. Efter många kök i Axarquía är här de fem skillnader värda att känna till innan du börjar — den sorts sak vi tar upp vid första besöket, precis som vår <a href="/sv/blogg/anlita-hantverkare-spanien-axarquia/">guide om att anlita en hantverkare</a> föreslår att du ska förvänta dig.</p>

<h2>1. Gas, induktion och hur mycket effekt du faktiskt har</h2>
<p>Många äldre spanska kök går på gasol snarare än stadsgas, och en hel del ägare byter nu till induktion när de renoverar. Haken är elektrisk: din bostad har en avtalad effektnivå — <em>potencia contratada</em> — och induktionshällar, ugnar och en luftkonditionering som går samtidigt kan slå ut en försörjning som ställdes in för decennier sedan för ett gaskök. Det lönar sig att kontrollera din avtalade effekt med ditt elbolag innan du planerar kring induktion; ibland behöver den höjas, vilket är ett samtal till elbolaget snarare än ett byggjobb.</p>

<h2>2. Spansk rör- och avloppsdragning</h2>
<p>Avlopp och vatten i spanska lägenheter är ofta trängre och mindre förlåtande än hemma — avloppsstammar i fasta lägen, grunda fall och rör ingjutna i massiva väggar i stället för dragna i regelväggar. Att flytta en diskho eller diskmaskin ett par meter kan innebära mer arbete än du tror. Det går oftast utmärkt, men det är ett skäl att bestämma planlösningen tidigt snarare än att ändra dig när väggarna är öppna.</p>

<h2>3. Leveranstider och vem som tar emot köket</h2>
<p>Köksstommar, bänkskivor och vitvaror kan ha verkliga leveranstider, och bänkskivor i synnerhet — särskilt sten och kvarts — mäts ofta upp först när stommarna är på plats och tillverkas sedan på beställning. Är du utomlands måste någon vara där för att ta emot en stor leverans och kontrollera den, och en saknad täckskiva kan stoppa hela monteringen. Vi samordnar leveranser till dagen och tar emot dem på plats så att köket kommer till ett rum som verkligen är redo för det.</p>

<h2>4. Öppen planlösning kräver bygglov</h2>
<p>Den populäraste köksändringen här är att öppna köket mot vardagsrummet. Är väggen inte bärande är det enkelt; är den det innebär det en balk och ordentligt bärande stöd, vilket är en <em>obra mayor</em> med pappersarbetet som hör till. Hur som helst vill kommunen ha ett bygglov, och i en lägenhet ska din comunidad informeras också. Vi säger vilken sida av gränsen din vägg ligger på innan vi offererar.</p>

<h2>5. IVA, facturas och vad det kostar</h2>
<p>Ett ordentligt köksjobb kommer med en factura och IVA — värt det för garantin och för dina papper när du säljer, som vi alltid råder. På kostnaden ligger en köksrenovering där vi förbereder och monterar på ungefär <strong>3 000 till 7 000 euro</strong>, och ett komplett exklusivt kök med struktur- eller planändringar på <strong>8 000 till 15 000 euro</strong>, stommar och vitvaror beroende på vad du väljer. Varje offert vi lämnar är kostnadsfri, skriftlig och gäller i 30 dagar — ett samlat pris för hela jobbet, så att du kan planera nivån efter din budget innan du bestämmer dig.</p>

<h2>Ett team för hela jobbet</h2>
<p>Anledningen till att kök går fel är oftast samordning — plattsättaren väntar på elektrikern som väntar på rörmokaren, och bänkskivan mäts mot stommar som inte var i våg. Vi kör rivning, förberedelser, puts, kakel och montering som ett team på ett schema, oavsett om du köper köket själv eller vi gör det. Så arbetar vi i <a href="/sv/omraden/rincon-de-la-victoria/">Rincón de la Victoria</a> och längs hela kusten, och det är därför bänkskivan passar.</p>

<p>Planerar du ett nytt kök? <a href="/sv/kok/">Läs om vår köksrenovering</a> eller <a href="/sv/kontakt/">skicka rummets mått och en bild</a> för en kostnadsfri skriftlig offert.</p>
""",
    },
},
{
    "slug": "cracks-in-walls-spanish-house",
    "slug_sv": "sprickor-i-vaggen-spanien",
    "date": "2026-09-09",
    "img": (f"{_O}/axarquia-handyman-reform-garden-wall-repair-render-repaint-before.webp",
            "Cracked exterior render on a garden wall before repair — before",
            "Sprucken fasadputs på en trädgårdsmur före reparation — före"),
    "en": {
        "title": "Cracks in the walls of your Spanish house: harmless or serious?",
        "meta_title": "Cracks in Spanish Walls: When to Worry | Handyman Axarquia",
        "desc": "A calm guide to cracks in a Spanish house: hairline render cracks, cracks at windows and lintels, stepped cracks, and when to mark them or call an engineer.",
        "excerpt": "Not every crack is a crisis. A calm guide to reading the cracks in a Spanish house — which are cosmetic, which need watching, and which are worth a professional look.",
        "body": """
<p>A crack appears above a window, or steps down the corner of the house, and the worst-case scenario arrives with it. Most of the time it should not. Walls move, renders shrink, and the Costa del Sol's heat and occasional heavy rain open cracks that are entirely cosmetic. Some, though, are worth attention. Here is how we read them on a first visit — a calm triage, not a diagnosis by article, because a crack has to be seen to be judged.</p>

<h2>Hairline cracks in render and plaster</h2>
<p>Fine, shallow cracks in the surface render or internal plaster — the width of a hair, following no particular pattern — are the most common and the least worrying. They are the surface reacting to heat, cold and time, not the structure moving. They are cosmetic: cut out, fill, and repaint with a breathable finish and they are gone. If they keep coming back in the same place that is worth mentioning, but on their own they are just a wall being a wall on a hot coast.</p>

<h2>Cracks at window and door corners</h2>
<p>Cracks running diagonally from the corners of windows and doors, or along the line of a lintel, are common in Spanish construction. Openings concentrate stress, and a little movement shows up at the weakest point. Usually these are repairable — rake out, reinforce, re-render — and stable once done. We look at whether the lintel itself is sound and whether the crack is old and settled or fresh and moving, which changes the fix.</p>

<h2>Stepped and diagonal cracks in block or stone</h2>
<p>Cracks that step down through the mortar joints of block or stone, especially wider ones, deserve a proper look. They can point to movement in the wall or the ground beneath it rather than just the surface. Often they are historic and long since stable; sometimes they are not. This is the category where we would rather see it in person and, if there is any doubt, bring in an aparejador (technical architect) or structural engineer before deciding anything.</p>

<h2>Cracks that widen over months</h2>
<p>The single most useful thing you can do with a crack that worries you is to date it. Mark each end with a pencil line and the date, and photograph it. A crack that has not moved in six months is telling you it is stable; one that is visibly wider than your mark is telling you the opposite. That simple record is worth more than any amount of speculation, and it is exactly what a professional will ask for.</p>

<h2>Cracks after heavy rain or on hillside plots</h2>
<p>On the steep plots of the villages and the campo, water and ground movement go together. A crack that appears or worsens after heavy rain, on a wall that backs onto a slope, often has drainage behind it — water pressure against or under the wall. Here the fix is frequently outside the house, not in it: drainage, gutters and downpipes first, then the wall. It is a close cousin of the problems in our <a href="/blog/rendering-vs-plastering-costa-del-sol/">guide to render and why coastal walls fail</a>.</p>

<h2>What we do at a free visit</h2>
<p>When you send us a photo or we come out, we are working out which of the above you have: whether it is surface or structural, old or moving, dry or fed by water. For the cosmetic majority we cut out, repair and repaint, and it is done. For the small number that are structural, we are honest that it needs an aparejador or engineer, and we will not paper over something that needs proper attention — filling a moving crack just hides it until next year. Either way you get a straight answer and, if there is work to do, a written quote. We do this on houses from <a href="/areas/torrox/">Torrox</a> to the inland villages every week.</p>

<p>Worried about a crack? <a href="/plastering/">See our plastering and repair work</a>, or explore a <a href="/reforms/">full reform</a> if the house needs more, and <a href="/contact/">send us a dated photo</a> for a free, honest assessment.</p>
""",
    },
    "sv": {
        "title": "Sprickor i väggen på ditt spanska hus: ofarligt eller allvarligt?",
        "meta_title": "Sprickor i väggen: när ska du oroa dig | Handyman Axarquia",
        "desc": "En lugn guide till sprickor i ett spanskt hus: putssprickor, sprickor vid fönster, trappstegssprickor, och när du ska markera dem eller ringa en ingenjör.",
        "excerpt": "Varje spricka är ingen kris. En lugn guide till att läsa sprickorna i ett spanskt hus — vilka som är kosmetiska, vilka som ska bevakas, och vilka som förtjänar en fackman.",
        "body": """
<p>En spricka dyker upp ovanför ett fönster, eller trappar ner i husets hörn, och värsta scenariot kommer med den. Oftast borde det inte göra det. Väggar rör sig, puts krymper, och Costa del Sols hetta och enstaka kraftiga regn öppnar sprickor som är helt kosmetiska. Vissa förtjänar dock uppmärksamhet. Här är hur vi läser dem vid ett första besök — en lugn sortering, inte en diagnos via artikel, för en spricka måste ses för att bedömas.</p>

<h2>Hårfina sprickor i puts</h2>
<p>Fina, ytliga sprickor i fasadputsen eller den invändiga putsen — hårets bredd, utan särskilt mönster — är de vanligaste och minst oroande. De är ytan som reagerar på värme, kyla och tid, inte stommen som rör sig. De är kosmetiska: skär ur, spackla och måla om med en andande färg så är de borta. Kommer de tillbaka på samma ställe är det värt att nämna, men i sig är de bara en vägg som är en vägg på en het kust.</p>

<h2>Sprickor vid fönster- och dörrhörn</h2>
<p>Sprickor som löper diagonalt från fönstrens och dörrarnas hörn, eller längs en överliggare, är vanliga i spansk konstruktion. Öppningar koncentrerar spänningar, och en aning rörelse visar sig vid den svagaste punkten. Oftast är de reparerbara — skär ur, armera, putsa om — och stabila när det är gjort. Vi tittar på om själva överliggaren är hel och om sprickan är gammal och satt eller färsk och rörlig, vilket ändrar åtgärden.</p>

<h2>Trappstegs- och diagonalsprickor i block eller sten</h2>
<p>Sprickor som trappar ner genom murbruksfogarna i block eller sten, särskilt bredare, förtjänar en ordentlig titt. De kan tyda på rörelse i väggen eller marken under den snarare än bara ytan. Ofta är de historiska och sedan länge stabila; ibland inte. Det är i den här kategorin vi hellre ser det på plats och, om det finns någon tvekan, tar in en aparejador (byggnadsingenjör) eller konstruktör innan något bestäms.</p>

<h2>Sprickor som vidgas över månader</h2>
<p>Det enskilt mest användbara du kan göra med en spricka som oroar dig är att datera den. Markera varje ände med ett pennstreck och datumet, och fotografera. En spricka som inte rört sig på sex månader säger att den är stabil; en som är synligt bredare än ditt streck säger motsatsen. Den enkla noteringen är värd mer än hur mycket spekulation som helst, och det är precis vad en fackman kommer att fråga efter.</p>

<h2>Sprickor efter kraftigt regn eller på sluttande tomter</h2>
<p>På byarnas och landsbygdens branta tomter hör vatten och markrörelse ihop. En spricka som dyker upp eller förvärras efter kraftigt regn, på en vägg som vetter mot en sluttning, har ofta dränering bakom sig — vattentryck mot eller under väggen. Här är åtgärden ofta utanför huset, inte i det: dränering, hängrännor och stuprör först, sedan väggen. Det är en nära släkting till problemen i vår <a href="/sv/blogg/fasadputs-costa-del-sol-varfor-den-spricker/">guide om fasadputs och varför kustväggar går sönder</a>.</p>

<h2>Vad vi gör vid ett kostnadsfritt besök</h2>
<p>När du skickar oss en bild eller vi kommer ut arbetar vi ut vilken av ovanstående du har: om det är ytligt eller strukturellt, gammalt eller rörligt, torrt eller matat av vatten. För den kosmetiska majoriteten skär vi ur, lagar och målar om, och det är klart. För de få som är strukturella är vi ärliga med att det behöver en aparejador eller konstruktör, och vi tapetserar inte över något som behöver riktig uppmärksamhet — att spackla en rörlig spricka döljer den bara till nästa år. Hur som helst får du ett rakt svar och, om det finns arbete att göra, en skriftlig offert. Vi gör det på hus från <a href="/sv/omraden/torrox/">Torrox</a> till byarna inåt landet varje vecka.</p>

<p>Orolig för en spricka? <a href="/sv/putsarbeten/">Läs om våra puts- och lagningsarbeten</a>, eller titta på en <a href="/sv/renoveringar/">helrenovering</a> om huset behöver mer, och <a href="/sv/kontakt/">skicka en daterad bild</a> för en kostnadsfri, ärlig bedömning.</p>
""",
    },
},
{
    "slug": "best-tiles-andalusian-climate",
    "slug_sv": "plattor-terrass-pool-andalusien",
    "date": "2026-09-09",
    "img": (f"{_O}/axarquia-handyman-reform-garden-tiling-terrace-after.webp",
            "Terrace tiled with anti-slip porcelain — after",
            "Terrass lagd med halksäker porslinsklinker — efter"),
    "en": {
        "title": "Tiles that survive the Andalusian climate (terraces, bathrooms, pool areas)",
        "meta_title": "Tiles for the Andalusian Climate | Handyman Axarquia",
        "desc": "Porcelain, ceramic or stone outdoors? Frost and slip ratings, large formats and lippage, light colours, joints and the waterproof membrane every terrace needs.",
        "excerpt": "Not every tile survives an Axarquia terrace or pool surround. How to choose porcelain, ceramic or stone for heat, water and slip — and why the membrane underneath matters.",
        "body": """
<p>Tiles do more work on the Costa del Sol than almost anywhere: a terrace tile bakes at midday, cools at night, takes winter rain and the odd frost inland, and has to stay non-slip around a pool with wet feet on it. Choose the wrong one and it crazes, lifts or turns into a skating rink. Here is how we choose tiles for the Andalusian climate, indoors and out.</p>

<h2>Porcelain, ceramic or natural stone?</h2>
<p>Outdoors, <strong>porcelain</strong> is usually the answer. It is dense, absorbs almost no water, holds its colour in strong sun and takes heat and cold without fuss. <strong>Ceramic</strong> is fine for most interior walls and floors but is softer and more porous — better kept indoors and out of the pool area. <strong>Natural stone</strong> is beautiful and characterful, but it is porous and needs sealing and upkeep; on a terrace or by a pool that maintenance is real, so go in with your eyes open.</p>

<h2>Frost and thermal rating</h2>
<p>On the coast, frost is rare; up in the villages and the campo it is not, and a winter freeze will shatter a tile that soaked up water in the wet. For anywhere inland or exposed, use a frost-rated porcelain with very low water absorption. The same density that resists frost also copes with the daily thermal swing of a south-facing terrace, which is what causes cheaper tiles to craze over a few summers.</p>

<h2>Anti-slip around pools and wet areas</h2>
<p>Around a pool or in a wet room, slip resistance is not optional. Tiles carry slip ratings — the barefoot "A/B/C" classes for wet areas and pool surrounds, and the shod "R" ratings — and there are proper standards for the space around a pool. We will not quote a smooth, glossy tile for a pool surround however good it looks in the showroom; the right choice grips wet feet without being so rough it cannot be cleaned. This is one to specify carefully rather than by picture.</p>

<h2>Large formats and lippage</h2>
<p>Big-format tiles are the current look and they suit these bright, open terraces — but they are less forgiving. Any unevenness in the base shows up as "lippage", one tile edge sitting proud of its neighbour, which looks bad and trips people. Large formats need a properly flat, well-prepared bed, the right adhesive and levelling clips, and an installer who takes the base seriously. It is as much about what is under the tile as the tile itself.</p>

<h2>Light colours and heat</h2>
<p>A dark terrace tile in full Andalusian sun becomes too hot to stand on barefoot by lunchtime. Lighter colours reflect heat, stay usable through the day and show less of the dust and salt that blow in off the coast. It is a small choice that makes a big difference to whether the terrace actually gets used in August.</p>

<h2>Grout, expansion joints and the layer that matters most</h2>
<p>Outdoors, tiles move with the heat, so the job needs the right flexible grout and — the part people forget — <strong>expansion joints</strong>, or the whole field tents and lifts on the first hot spell. And underneath all of it, every terrace needs a proper waterproof membrane before a single tile goes down. Tiles and grout are not waterproof; the membrane is what stops water reaching the room below. Skipping it is the number-one cause of terrace leaks on this coast, which is why it is built into our <a href="/tiling/">tiling and terrace work</a> as standard, and why it features in our <a href="/blog/damp-in-spanish-house-causes-and-fixes/">guide to damp</a>.</p>

<h2>Where to see them</h2>
<p>You do not have to choose blind. There are good tile showrooms in Torre del Mar and Vélez-Málaga where you can see large formats and pool-rated ranges in person, and we are happy to tell you which of what you like will actually perform where you want to put it. We tile terraces, bathrooms and pool surrounds across the coast, including plenty in <a href="/areas/torre-del-mar/">Torre del Mar</a>.</p>

<p>Planning a terrace, bathroom or pool surround? <a href="/tiling/">See our tiling and waterproofing service</a> or <a href="/contact/">send us the area and a photo</a> for a free written quote.</p>
""",
    },
    "sv": {
        "title": "Plattor som överlever det andalusiska klimatet (terrasser, badrum, poolområden)",
        "meta_title": "Plattor för det andalusiska klimatet | Handyman Axarquia",
        "desc": "Porslin, keramik eller sten utomhus? Frost- och halkklasser, storformat och nivåskillnader, ljusa färger, fogar och tätskiktet som varje terrass behöver.",
        "excerpt": "Alla plattor överlever inte en terrass eller ett poolområde i Axarquía. Hur du väljer porslin, keramik eller sten för värme, vatten och halka — och varför tätskiktet spelar roll.",
        "body": """
<p>Plattor gör mer arbete på Costa del Sol än nästan någon annanstans: en terrassplatta gassar mitt på dagen, kyls på natten, tar vinterregn och enstaka frost inåt landet, och måste förbli halksäker runt en pool med blöta fötter på sig. Väljer du fel krackelerar den, lyfter eller blir en skridskobana. Så här väljer vi plattor för det andalusiska klimatet, inne och ute.</p>

<h2>Porslin, keramik eller natursten?</h2>
<p>Utomhus är <strong>porslinsklinker</strong> oftast svaret. Den är tät, tar upp nästan inget vatten, håller färgen i stark sol och tål värme och kyla utan problem. <strong>Keramik</strong> fungerar för de flesta invändiga väggar och golv men är mjukare och mer porös — bäst att hålla inomhus och borta från poolområdet. <strong>Natursten</strong> är vacker och karaktärsfull, men den är porös och behöver impregnering och skötsel; på en terrass eller vid en pool är det underhållet verkligt, så gå in med öppna ögon.</p>

<h2>Frost- och värmeklass</h2>
<p>På kusten är frost sällsynt; uppe i byarna och på landet är den det inte, och en vinterfrost spräcker en platta som sög upp vatten i vätan. För allt inåt landet eller utsatt, använd en frostsäker porslinsklinker med mycket låg vattenabsorption. Samma täthet som motstår frost klarar också den dagliga värmeväxlingen på en söderterrass, vilket är det som får billigare plattor att krackelera över några somrar.</p>

<h2>Halksäkert runt pooler och våtytor</h2>
<p>Runt en pool eller i ett våtrum är halksäkerhet inte valfritt. Plattor har halkklasser — de barfota "A/B/C"-klasserna för våtytor och poolkanter, och de skodda "R"-klasserna — och det finns egna standarder för ytan runt en pool. Vi offererar inte en slät, blank platta för en poolkant hur bra den än ser ut i butiken; rätt val greppar blöta fötter utan att vara så grovt att det inte går att rengöra. Det här är ett val att göra noga snarare än efter bild.</p>

<h2>Storformat och nivåskillnader</h2>
<p>Storformatsplattor är den aktuella looken och de passar dessa ljusa, öppna terrasser — men de är mindre förlåtande. Varje ojämnhet i underlaget visar sig som nivåskillnad, där en plattkant sitter högre än grannens, vilket ser illa ut och får folk att snubbla. Storformat behöver en ordentligt plan, väl förberedd bädd, rätt fästmassa och nivåkilar, och en läggare som tar underlaget på allvar. Det handlar lika mycket om vad som är under plattan som om plattan själv.</p>

<h2>Ljusa färger och värme</h2>
<p>En mörk terrassplatta i full andalusisk sol blir för het att stå på barfota vid lunch. Ljusare färger reflekterar värme, förblir användbara genom dagen och visar mindre av det damm och salt som blåser in från kusten. Det är ett litet val som gör stor skillnad för om terrassen faktiskt används i augusti.</p>

<h2>Fog, rörelsefogar och skiktet som betyder mest</h2>
<p>Utomhus rör sig plattor med värmen, så jobbet behöver rätt flexibla fog och — den del folk glömmer — <strong>rörelsefogar</strong>, annars tältar och lyfter hela ytan vid första värmeböljan. Och under alltihop behöver varje terrass ett ordentligt tätskikt innan en enda platta läggs. Plattor och fog är inte vattentäta; tätskiktet är det som hindrar vatten från att nå rummet under. Att hoppa över det är den främsta orsaken till terrassläckage på den här kusten, vilket är varför det ingår i våra <a href="/sv/kakel/">kakel- och terrassarbeten</a> som standard, och varför det tas upp i vår <a href="/sv/blogg/fukt-i-huset-spanien-orsaker-och-losningar/">guide om fukt</a>.</p>

<h2>Var du kan se dem</h2>
<p>Du behöver inte välja blint. Det finns bra kakelbutiker i Torre del Mar och Vélez-Málaga där du kan se storformat och poolklassade serier på plats, och vi berättar gärna vilka av dem du gillar som faktiskt kommer att fungera där du vill sätta dem. Vi lägger plattor på terrasser, badrum och poolkanter längs hela kusten, inklusive många i <a href="/sv/omraden/torre-del-mar/">Torre del Mar</a>.</p>

<p>Planerar du en terrass, ett badrum eller en poolkant? <a href="/sv/kakel/">Läs om våra kakel- och tätskiktsarbeten</a> eller <a href="/sv/kontakt/">skicka ytan och en bild</a> för en kostnadsfri skriftlig offert.</p>
""",
    },
},
{
    "slug": "buying-renovation-project-nerja-torrox",
    "slug_sv": "kopa-renoveringsobjekt-nerja-torrox",
    "date": "2026-09-09",
    "img": (f"{_G}/handyman-axarquia-kitchen-reform-arch-before.webp",
            "Dated kitchen in a property before renovation — before",
            "Omodernt kök i en bostad före renovering — före"),
    "en": {
        "title": "Buying a renovation project in Nerja or Torrox? What to check before you sign",
        "meta_title": "Buying a Renovation Project in Spain | Handyman Axarquia",
        "desc": "Buying a house to renovate in Nerja or Torrox? What to check on a viewing — damp, terrace, electrics, water, licences, rural land, comunidad — before you sign.",
        "excerpt": "A builder's eye on a viewing saves money later. What to check before you buy a renovation project in Nerja, Torrox or the Axarquia — and how to run it from abroad.",
        "body": """
<p>A renovation project can be the best way into the Axarquia — you buy the location and make the house your own — or an expensive lesson in what the survey did not cover. The difference is usually what you knew before you signed. Here is what to look at on a viewing, why a builder's visit before you buy pays for itself, and how the whole thing is run if you are still in Sweden or the UK.</p>

<h2>What to look at on the viewing</h2>
<ul class="tick">
<li><strong>Damp.</strong> Tide-marks low on the walls, black mould in corners, blown plaster, a musty smell in a closed-up house — damp is the most common and most under-estimated problem, and its cause matters more than its look.</li>
<li><strong>The roof terrace.</strong> On this coast the terrace is the number-one source of leaks. Stains on the ceiling below, patched grout and a surface with no obvious falls are all worth noting.</li>
<li><strong>Electrics.</strong> An old consumer unit, cloth or aluminium wiring and too few sockets usually mean a rewire, which is disruptive and worth pricing in.</li>
<li><strong>Water pressure.</strong> Run the taps and the shower. Poor pressure, or a system fed from a roof deposit, changes what the house can do.</li>
<li><strong>Licences on previous work.</strong> Ask whether past extensions, pools or conversions were licensed. Unlicensed work becomes your problem when you come to sell.</li>
<li><strong>Rural land status.</strong> If it is in the campo, whether it sits on <em>suelo urbano</em> or <em>suelo rústico</em> decides what you can ever add — check before you plan an extension.</li>
<li><strong>Comunidad.</strong> In an apartment, ask about any outstanding community debts and any planned major works (a <em>derrama</em>), which transfer with the flat.</li>
</ul>

<h2>Why a builder's visit before you buy pays for itself</h2>
<p>A lawyer checks the paperwork and a valuer confirms the price, but neither tells you what the reform will cost. A builder walking the property with you — or with your agent, if you cannot be there — turns "it needs work" into a realistic figure and a realistic timeline before you commit. It is the cheapest money you will spend on the whole project, and it is the difference between a budget and a hope. It is also the honest-quote habit we describe in our <a href="/blog/hire-a-builder-axarquia-spain/">guide to hiring a builder</a>.</p>

<h2>A realistic budget and timeline</h2>
<p>As a planning guide, a full reform of an apartment runs roughly <strong>€600 to €1,000 per square metre</strong> depending on finishes, and a new extension around <strong>€1,000 to €1,600 per square metre</strong> plus architect and licence. On timing, expect the licence to take weeks for minor works and months for an obra mayor, then the build itself on top — which is why we look at the paperwork route early, as our <a href="/blog/building-licence-spain-obra-menor-obra-mayor/">guide to licences</a> explains. Knowing both before you buy means the price you pay for the house and the price to fix it add up to a number you are happy with.</p>

<h2>Running it from abroad</h2>
<p>Most of our renovation clients buy before they move, and manage the whole project from home. That works when the communication is built in from the start: photo updates as the work moves, keys held securely, and the same payment structure we use on every job — a deposit to book and buy materials, and the balance on completion. You see the house change week by week without living in the dust. We do this constantly for owners buying in <a href="/areas/nerja/">Nerja</a> and <a href="/areas/torrox/">Torrox</a>, the two areas where renovation projects come up most.</p>

<h2>We can come to the viewing</h2>
<p>If you have found a place and want to know what you are taking on, we can visit it with you or your agent and give you an honest read on the work and a ballpark before you sign. There is no substitute for eyes on the actual house. Tell us the property and the timing, and we will make it work around the viewing.</p>

<p>Found a project worth a second opinion? <a href="/reforms/">See how we handle full reforms</a> or <a href="/contact/">tell us about the property</a> and we will come and look before you commit.</p>
""",
    },
    "sv": {
        "title": "Köpa renoveringsobjekt i Nerja eller Torrox? Det här ska du kolla innan du skriver på",
        "meta_title": "Köpa renoveringsobjekt i Spanien | Handyman Axarquia",
        "desc": "Köpa hus att renovera i Nerja eller Torrox? Vad du ska kolla på visningen — fukt, takterrass, el, vatten, bygglov och comunidad — innan du skriver på.",
        "excerpt": "En byggares ögon på visningen sparar pengar sedan. Vad du ska kolla innan du köper ett renoveringsobjekt i Nerja, Torrox eller Axarquía — och hur det sköts från Sverige.",
        "body": """
<p>Ett renoveringsobjekt kan vara den bästa vägen in i Axarquía — du köper läget och gör huset till ditt eget — eller en dyr läxa i vad besiktningen inte täckte. Skillnaden ligger oftast i vad du visste innan du skrev på. Här är vad du ska titta på under visningen, varför ett byggarbesök före köpet lönar sig, och hur allt sköts om du fortfarande är i Sverige.</p>

<h2>Vad du ska titta på under visningen</h2>
<ul class="tick">
<li><strong>Fukt.</strong> Fuktränder lågt på väggarna, svart mögel i hörnen, bortsprängd puts, unken lukt i ett stängt hus — fukt är det vanligaste och mest underskattade problemet, och orsaken betyder mer än utseendet.</li>
<li><strong>Takterrassen.</strong> På den här kusten är terrassen den främsta källan till läckage. Fläckar i taket under, lagade fogar och en yta utan tydligt fall är alla värda att notera.</li>
<li><strong>Elen.</strong> En gammal elcentral, tyg- eller aluminiumledningar och för få uttag betyder oftast en omdragning, som är stökig och värd att räkna in.</li>
<li><strong>Vattentrycket.</strong> Spola i kranarna och duschen. Dåligt tryck, eller ett system som matas från en taktank, förändrar vad huset klarar.</li>
<li><strong>Bygglov på tidigare arbeten.</strong> Fråga om tidigare tillbyggnader, pooler eller ombyggnader var lovgivna. Olovligt arbete blir ditt problem den dag du ska sälja.</li>
<li><strong>Landsbygdsmark.</strong> Ligger huset på landet avgör om det står på <em>suelo urbano</em> eller <em>suelo rústico</em> vad du någonsin kan bygga till — kolla innan du planerar en tillbyggnad.</li>
<li><strong>Comunidad.</strong> I en lägenhet, fråga om utestående samfällighetsskulder och planerade större arbeten (en <em>derrama</em>), som följer med lägenheten.</li>
</ul>

<h2>Varför ett byggarbesök före köpet lönar sig</h2>
<p>En advokat granskar pappren och en värderingsman bekräftar priset, men ingen av dem säger vad renoveringen kommer att kosta. En byggare som går igenom fastigheten med dig — eller med din mäklare, om du inte kan vara på plats — förvandlar "det behöver arbete" till en realistisk siffra och en realistisk tidplan innan du binder dig. Det är de billigaste pengarna du lägger på hela projektet, och skillnaden mellan en budget och en förhoppning. Det är också den ärliga offertvana vi beskriver i vår <a href="/sv/blogg/anlita-hantverkare-spanien-axarquia/">guide om att anlita en hantverkare</a>.</p>

<h2>Realistisk budget och tidplan</h2>
<p>Som riktmärke ligger en helrenovering av en lägenhet på ungefär <strong>600 till 1 000 euro per kvadratmeter</strong> beroende på ytskikt, och en ny tillbyggnad på omkring <strong>1 000 till 1 600 euro per kvadratmeter</strong> plus arkitekt och bygglov. Räkna med att bygglovet tar veckor för mindre arbeten och månader för en obra mayor, och sedan själva bygget ovanpå — därför tittar vi på tillståndsvägen tidigt, som vår <a href="/sv/blogg/bygglov-spanien-obra-menor-obra-mayor/">guide om bygglov</a> förklarar. Att veta bådadera innan du köper gör att priset för huset och priset att rusta upp det blir en summa du är nöjd med.</p>

<h2>Sköta projektet från Sverige</h2>
<p>De flesta av våra renoveringskunder köper innan de flyttar och sköter hela projektet hemifrån. Det fungerar när kommunikationen finns med från början: bilduppdateringar medan arbetet fortskrider, säker nyckelhantering och samma betalningsupplägg som på alla våra jobb — en handpenning för att boka och köpa material, och resten vid färdigställande. Du ser huset förändras vecka för vecka utan att bo i dammet. Det gör vi ständigt åt ägare som köper i <a href="/sv/omraden/nerja/">Nerja</a> och <a href="/sv/omraden/torrox/">Torrox</a>, de två områden där renoveringsobjekt dyker upp oftast.</p>

<h2>Vi kan komma till visningen</h2>
<p>Har du hittat ett ställe och vill veta vad du ger dig in på kan vi besöka det med dig eller din mäklare och ge en ärlig bild av arbetet och en ungefärlig summa innan du skriver på. Det finns ingen ersättning för att se det faktiska huset. Berätta vilken fastighet och när, så ordnar vi det kring visningen.</p>

<p>Hittat ett objekt värt en andra åsikt? <a href="/sv/renoveringar/">Läs hur vi sköter helrenoveringar</a> eller <a href="/sv/kontakt/">berätta om fastigheten</a> så kommer vi och tittar innan du binder dig.</p>
""",
    },
},
]
