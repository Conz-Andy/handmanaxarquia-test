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
<p>Every bathroom quote we write itemises: strip-out and rubble removal, plumbing and electrical work, tanking, plastering, tiling, fitting of sanitaryware and screen, silicone and finishing, cleaning, and the licencia de obra menor paperwork. Tiles and sanitaryware are listed separately so you can see exactly what you are paying for, and you are free to choose your own from the showrooms in Torre del Mar and Vélez-Málaga.</p>

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
<p>Varje badrumsoffert vi skriver specificerar: rivning och bortforsling, rör- och elarbete, tätskikt, puts, plattsättning, montering av porslin och duschvägg, silikon och finish, städning samt handlingarna för licencia de obra menor. Kakel och porslin listas separat så att du ser exakt vad du betalar för, och du får gärna välja själv i butikerna i Torre del Mar och Vélez-Málaga.</p>

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
]
