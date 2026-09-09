# Town / area landing pages (EN at /areas/<slug>/, SV at /sv/omraden/<slug>/).
# Each page has genuinely different local copy — these are not templated
# doorway pages. Keep facts general (property types, terrain, access) rather
# than claims that go stale.

AREA_ORDER = ["torre-del-mar", "velez-malaga", "nerja", "torrox",
              "rincon-de-la-victoria", "frigiliana"]

_G = "/wp-content/uploads/2026/08"
_O = "/wp-content/uploads/2024/02"

AREAS = {
"torre-del-mar": {
    "slug_sv": "torre-del-mar",
    "name": "Torre del Mar",
    "img": (f"{_G}/handyman-axarquia-terrace-planters-after.webp", "Roof terrace reform with planters and decorative tiling — after"),
    "en": {
        "title": "Builders & Reforms in Torre del Mar | Handyman Axarquia",
        "desc": "Local builders for reforms, bathrooms, kitchens, tiling and plastering in Torre del Mar. Based 5 minutes away in Almayate. Free written quotes, 12-month guarantee.",
        "h1": "Builders and reforms in Torre del Mar",
        "lead": "We are based in Almayate, five minutes from the Torre del Mar seafront — so quotes are quick, visits are easy and we know the apartment blocks, townhouses and communities of the town well.",
        "prose": """
<h2>Working in Torre del Mar apartments and townhouses</h2>
<p>Most of our Torre del Mar work is in apartments — the seafront blocks along the Paseo Marítimo, the 1970s–90s buildings behind the promenade, and the newer developments towards Caleta. Apartment reforms bring their own rules: the comunidad de propietarios needs notifying, lifts and stairwells must be protected, working hours are limited, and rubble has to go down in bags rather than a skip on the pavement. We do this every week, and we handle it without bothering your neighbours.</p>
<ul class="tick">
<li>Bathroom and kitchen refits in apartments, including full re-plumbing where the original pipework is tired</li>
<li>Open-plan conversions — removing the wall between the kitchen and the living room</li>
<li>Terrace waterproofing and re-tiling, the most common leak we are called out to on the coast</li>
<li>Damp and salt-air plaster repairs on seafront properties</li>
<li>Full reforms of townhouses in the old centre and in Almayate, Torre del Mar's western edge</li>
</ul>
<h2>Holiday rentals and absent owners</h2>
<p>A large share of the flats in Torre del Mar are holiday homes or short-term rentals owned by people who live in the UK, Sweden, Germany or Madrid. We are used to working with a key held by an agent or a neighbour, sending photo updates on WhatsApp, and timing work between bookings. If your rental needs a refresh before the season, tell us the booking gaps and we will plan around them.</p>
<h2>Nearby: Almayate, Caleta de Vélez and Algarrobo Costa</h2>
<p>The same team covers Almayate (where we are based), Caleta de Vélez, Algarrobo Costa, Mezquitilla and Lagos. There is no call-out charge anywhere along this stretch of coast.</p>
""",
        "faqs": [
            ("Do I need permission from my comunidad to reform my flat in Torre del Mar?",
             "For internal, non-structural work you normally only need to inform the comunidad (and the town hall for a licencia de obra menor). Anything touching the façade, terraces, structure or shared pipework needs the community's approval. We tell you which applies before we quote."),
            ("How quickly can you come and quote in Torre del Mar?",
             "Usually within a day or two — we are five minutes away in Almayate. Written quotes follow within a few days of the visit."),
            ("Can you work on my apartment while I am abroad?",
             "Yes. Most of our Torre del Mar clients are not in Spain full-time. We collect keys from your agent or neighbour, send daily or weekly photo updates and leave the property clean."),
        ],
    },
    "sv": {
        "title": "Byggfirma & renovering i Torre del Mar | Handyman Axarquia",
        "desc": "Svensktalande byggfirma för renovering, badrum, kök, kakel och puts i Torre del Mar. Vi finns 5 minuter bort i Almayate. Kostnadsfri offert, 12 månaders garanti.",
        "h1": "Byggfirma och renovering i Torre del Mar",
        "lead": "Vi utgår från Almayate, fem minuter från strandpromenaden i Torre del Mar — så offertbesök går snabbt och vi känner stadens lägenhetshus, radhus och samfälligheter väl.",
        "prose": """
<h2>Arbeten i lägenheter och radhus i Torre del Mar</h2>
<p>Det mesta vi gör i Torre del Mar sker i lägenheter — husen längs Paseo Marítimo, 70–90-talsbyggnaderna bakom promenaden och de nyare områdena mot Caleta. Lägenhetsrenoveringar har sina egna regler: samfälligheten (comunidad de propietarios) ska informeras, hissar och trapphus skyddas, arbetstiderna är begränsade och bygg­avfall bärs ner i säckar i stället för att en container ställs på trottoaren. Det gör vi varje vecka, utan att störa grannarna.</p>
<ul class="tick">
<li>Badrums- och köksrenoveringar i lägenheter, inklusive nya rör där de gamla är slitna</li>
<li>Öppen planlösning — väggen mellan kök och vardagsrum tas bort</li>
<li>Tätskikt och ny plattsättning på terrasser — den vanligaste läckan vi kallas ut till på kusten</li>
<li>Fukt- och saltskador i puts på bostäder nära havet</li>
<li>Helrenoveringar av radhus i gamla stan och i Almayate, Torre del Mars västra del</li>
</ul>
<h2>Semesterbostäder och ägare som bor i Sverige</h2>
<p>En stor del av lägenheterna i Torre del Mar ägs av personer som bor i Sverige, Storbritannien eller Madrid och hyr ut eller besöker några veckor om året. Vi är vana vid att hämta nyckel hos en mäklare eller granne, skicka bilduppdateringar på WhatsApp och lägga arbetet mellan bokningarna. Berätta när lägenheten står tom, så planerar vi efter det — på svenska.</p>
<h2>I närheten: Almayate, Caleta de Vélez och Algarrobo Costa</h2>
<p>Samma team täcker Almayate (där vi finns), Caleta de Vélez, Algarrobo Costa, Mezquitilla och Lagos. Ingen utkörningsavgift längs den här delen av kusten.</p>
""",
        "faqs": [
            ("Behöver jag tillstånd från samfälligheten för att renovera min lägenhet i Torre del Mar?",
             "För invändiga, icke bärande arbeten räcker det normalt att informera samfälligheten (och söka licencia de obra menor hos kommunen). Allt som rör fasad, terrasser, stomme eller gemensamma rör kräver samfällighetens godkännande. Vi berättar vad som gäller innan vi lämnar offert."),
            ("Hur snabbt kan ni komma och titta i Torre del Mar?",
             "Oftast inom en eller två dagar — vi finns fem minuter bort i Almayate. Skriftlig offert kommer några dagar efter besöket."),
            ("Kan ni arbeta i lägenheten medan jag är i Sverige?",
             "Ja. De flesta av våra kunder i Torre del Mar bor inte i Spanien på heltid. Vi hämtar nyckel hos mäklare eller granne, skickar bilduppdateringar och lämnar bostaden städad."),
        ],
    },
},
"velez-malaga": {
    "slug_sv": "velez-malaga",
    "name": "Vélez-Málaga",
    "img": (f"{_G}/handyman-axarquia-kitchen-reform-open-after.webp", "Open-plan kitchen reform — after"),
    "en": {
        "title": "Builders & Reforms in Vélez-Málaga | Handyman Axarquia",
        "desc": "Builders for townhouse reforms, extensions, kitchens, bathrooms and plastering in Vélez-Málaga and its villages. Local, English-speaking, free written quotes.",
        "h1": "Builders and property reforms in Vélez-Málaga",
        "lead": "Vélez-Málaga is our home municipality — Almayate is one of its villages — and its old townhouses, cortijos and modern estates are the properties we know best.",
        "prose": """
<h2>Old-town casas and townhouses</h2>
<p>The historic centre of Vélez-Málaga, around the Plaza de las Carmelitas and up towards the castle, is full of tall, narrow townhouses that foreign buyers are steadily restoring. They are wonderful buildings and they hide surprises: solid-earth walls, timber-and-cane ceilings, rooms added over generations and plumbing that was never planned. Reforming one well means respecting the structure, using breathable lime-based plasters where the walls need to dry, and dealing honestly with what we find behind the old surfaces.</p>
<ul class="tick">
<li>Full and phased reforms of old-town houses, floor by floor if you prefer</li>
<li>Replacement of cane-and-plaster ceilings, new floors, rewiring and re-plumbing</li>
<li>Roof terraces (azoteas) — waterproofing, drainage and tiling</li>
<li>Kitchens and bathrooms in modern apartments around the Parque Jurado Lorca and El Ingenio</li>
<li>Extensions, pergolas and pool-area work on country properties in the campo</li>
</ul>
<h2>The Vélez-Málaga town hall and licences</h2>
<p>Because we work in the municipality constantly, we know how the Vélez-Málaga urbanismo department handles licencias de obra menor and what documentation they expect. For larger projects we work with local architects and aparejadores who deal with the town hall every week. You will always be told at the quote stage what licence a job needs.</p>
<h2>Villages of the municipality</h2>
<p>Vélez-Málaga's municipality stretches from the coast at Torre del Mar, Almayate, Caleta and Chilches up to Triana, Trapiche, Benajarafe and the campo around the Viñuela reservoir. We cover all of it, and country access — tracks, water deposits, generators — is not a problem for us.</p>
""",
        "faqs": [
            ("Are old townhouses in Vélez-Málaga expensive to reform?",
             "They can be, but mostly because of what is hidden — poor wiring, no damp-proofing, uneven floors. A proper survey visit before we quote keeps surprises to a minimum, and we price any extras in writing before continuing."),
            ("Do you build extensions on campo properties near Vélez-Málaga?",
             "Yes, subject to the planning rules for rural land, which are stricter than in town. We will tell you honestly at the first visit what is likely to be permitted."),
            ("Can you handle the licence application at Vélez-Málaga town hall?",
             "For licencias de obra menor we can prepare and submit the paperwork for you. Obra mayor projects need an architect's project, which we can arrange."),
        ],
    },
    "sv": {
        "title": "Byggfirma & renovering i Vélez-Málaga | Handyman Axarquia",
        "desc": "Byggfirma för renovering av stadshus, tillbyggnader, kök, badrum och puts i Vélez-Málaga med byar. Lokala, svensktalande, kostnadsfri skriftlig offert.",
        "h1": "Byggfirma och renovering i Vélez-Málaga",
        "lead": "Vélez-Málaga är vår hemkommun — Almayate är en av dess byar — och stadens gamla stadshus, cortijos och moderna bostadsområden är de fastigheter vi känner bäst.",
        "prose": """
<h2>Gamla stan och dess stadshus</h2>
<p>Den historiska stadskärnan i Vélez-Málaga, runt Plaza de las Carmelitas och upp mot borgen, är full av höga, smala stadshus som utländska köpare renoverar ett efter ett. Det är underbara hus och de gömmer överraskningar: massiva jordväggar, tak av trä och rör, rum som lagts till genom generationer och rördragningar som aldrig planerades. Att renovera ett sådant hus väl innebär att respektera stommen, använda andande kalkputs där väggarna behöver torka och vara ärlig om det vi hittar bakom de gamla ytorna.</p>
<ul class="tick">
<li>Hel- eller etappvisa renoveringar av hus i gamla stan — våning för våning om du vill</li>
<li>Byte av rör- och putstak, nya golv, ny el och nya rör</li>
<li>Takterrasser (azoteas) — tätskikt, avrinning och plattsättning</li>
<li>Kök och badrum i moderna lägenheter runt Parque Jurado Lorca och El Ingenio</li>
<li>Tillbyggnader, pergolor och poolområden på landsbygdsfastigheter</li>
</ul>
<h2>Kommunen och bygglov</h2>
<p>Eftersom vi arbetar i kommunen hela tiden vet vi hur Vélez-Málagas stadsbyggnadskontor hanterar licencia de obra menor och vilka handlingar de vill ha. Vid större projekt samarbetar vi med lokala arkitekter som har kontakt med kommunen varje vecka. Du får alltid veta redan vid offerten vilket tillstånd jobbet kräver.</p>
<h2>Kommunens byar</h2>
<p>Vélez-Málaga kommun sträcker sig från kusten vid Torre del Mar, Almayate, Caleta och Chilches upp till Triana, Trapiche, Benajarafe och landsbygden runt Viñuela-sjön. Vi täcker allt, och lantlig åtkomst — grusvägar, vattentankar, generatorer — är inget problem för oss.</p>
""",
        "faqs": [
            ("Är gamla stadshus i Vélez-Málaga dyra att renovera?",
             "De kan vara det, men främst på grund av det dolda — dålig el, ingen fuktspärr, ojämna golv. Ett ordentligt besök innan offerten minimerar överraskningarna, och eventuella tillägg prissätts skriftligt innan vi fortsätter."),
            ("Bygger ni tillbyggnader på landsbygdsfastigheter nära Vélez-Málaga?",
             "Ja, med förbehåll för planreglerna på landsbygdsmark, som är strängare än i stan. Vi säger ärligt vid första besöket vad som sannolikt tillåts."),
            ("Kan ni sköta bygglovsansökan hos kommunen?",
             "För licencia de obra menor kan vi förbereda och lämna in handlingarna åt dig. Obra mayor kräver ett arkitektprojekt, vilket vi kan ordna."),
        ],
    },
},
"nerja": {
    "slug_sv": "nerja",
    "name": "Nerja",
    "img": (f"{_G}/handyman-axarquia-bathroom-reform-1-after.webp", "Complete bathroom renovation — after"),
    "en": {
        "title": "Builders & Bathroom / Kitchen Renovations in Nerja | Handyman Axarquia",
        "desc": "Reliable builders for bathroom and kitchen renovations, reforms, tiling and plastering in Nerja, Maro and Burriana. English & Swedish spoken. Free written quotes.",
        "h1": "Builders and renovations in Nerja",
        "lead": "Nerja has the largest international community on the eastern Costa del Sol — and the busiest holiday-rental market. Most of our Nerja work is bathrooms, kitchens and apartment refreshes for owners who are not here full-time.",
        "prose": """
<h2>Bathrooms, kitchens and rental-ready apartments</h2>
<p>From the apartment blocks around Burriana and Torrecilla to the townhouses off Calle Pintada and the villas in Capistrano, Nerja properties are worked hard by guests. The jobs we are asked for most are complete bathroom refits (often bath-to-walk-in-shower conversions), kitchen replacements, re-tiling of terraces and a general "make it look new again" refresh between seasons.</p>
<ul class="tick">
<li>Bathroom renovations with proper tanking — 7 to 12 working days for a standard bathroom</li>
<li>Kitchen strip-out, first fix and installation, whether you supply the kitchen or we do</li>
<li>Terrace and balcony waterproofing to stop leaks into the apartment below</li>
<li>Plastering, gotelé removal and painting of whole apartments between bookings</li>
<li>Reforms and extensions to villas in Capistrano, Punta Lara and Maro</li>
</ul>
<h2>Planning around bookings</h2>
<p>If your Nerja property is a holiday rental, the calendar decides everything. Tell us the gaps — typically November to February for larger jobs, or a two-week window in spring — and we quote with a start date and a finish date you can book around. We send photo updates as we go and coordinate with your key-holder or management company.</p>
<h2>Frigiliana, Maro and the surrounding hills</h2>
<p>From Nerja we also cover Maro, Frigiliana, Punta Lara, El Capistrano and the campo towards Torrox. Nerja is around 35 minutes from our base in Almayate, and there is no call-out charge.</p>
""",
        "faqs": [
            ("How much does a bathroom renovation cost in Nerja?",
             "A complete standard-size bathroom refit typically comes in between €4,500 and €9,000 depending on tiles and fittings. You get a free written quote before anything starts."),
            ("Can you do the work while my apartment is empty over winter?",
             "Yes — winter is our busiest period for Nerja rentals for exactly that reason. Book early for November to February slots."),
            ("Do you work with rental management companies in Nerja?",
             "Regularly. We collect keys, coordinate with your agent and leave the property guest-ready."),
        ],
    },
    "sv": {
        "title": "Byggfirma & badrums-/köksrenovering i Nerja | Handyman Axarquia",
        "desc": "Svensktalande byggfirma för badrum, kök, renovering, kakel och puts i Nerja, Maro och Burriana. Kostnadsfri skriftlig offert, 12 månaders garanti.",
        "h1": "Byggfirma och renovering i Nerja",
        "lead": "Nerja har den största svenska och internationella kolonin på östra Costa del Sol — och den livligaste uthyrningsmarknaden. Det mesta vi gör i Nerja är badrum, kök och uppfräschning av lägenheter åt ägare som inte bor här på heltid.",
        "prose": """
<h2>Badrum, kök och uthyrningsklara lägenheter</h2>
<p>Från lägenhetshusen runt Burriana och Torrecilla till stadshusen vid Calle Pintada och villorna i Capistrano — bostäder i Nerja används hårt av gäster. Det vi oftast får förfrågningar om är kompletta badrumsrenoveringar (ofta badkar till walk-in-dusch), köksbyten, ny plattsättning på terrasser och en allmän uppfräschning mellan säsongerna.</p>
<ul class="tick">
<li>Badrumsrenovering med korrekt tätskikt — 7 till 12 arbetsdagar för ett normalstort badrum</li>
<li>Rivning av gammalt kök, förberedelser och montering — oavsett om du köper köket själv eller vi ordnar det</li>
<li>Tätskikt på terrasser och balkonger för att stoppa läckage till lägenheten under</li>
<li>Puts, borttagning av gotelé och målning av hela lägenheter mellan bokningar</li>
<li>Renoveringar och tillbyggnader av villor i Capistrano, Punta Lara och Maro</li>
</ul>
<h2>Vi planerar efter bokningarna</h2>
<p>Om din bostad i Nerja hyrs ut styr kalendern allt. Berätta när den står tom — vanligtvis november till februari för större jobb, eller ett fönster på två veckor under våren — så lämnar vi offert med start- och slutdatum som du kan boka runt. Vi skickar bilduppdateringar och samordnar med din nyckelperson eller förvaltare. Allt på svenska om du vill.</p>
<h2>Frigiliana, Maro och omgivningarna</h2>
<p>Från Nerja täcker vi även Maro, Frigiliana, Punta Lara, El Capistrano och landsbygden mot Torrox. Nerja ligger cirka 35 minuter från vår bas i Almayate, och vi tar ingen utkörningsavgift.</p>
""",
        "faqs": [
            ("Vad kostar en badrumsrenovering i Nerja?",
             "En komplett renovering av ett normalstort badrum hamnar vanligtvis mellan 4 500 och 9 000 euro beroende på kakel och inredning. Du får en kostnadsfri skriftlig offert innan något påbörjas."),
            ("Kan ni göra arbetet när lägenheten står tom under vintern?",
             "Ja — vintern är vår mest bokade period i Nerja just av den anledningen. Boka tidigt för november till februari."),
            ("Samarbetar ni med uthyrningsförvaltare i Nerja?",
             "Regelbundet. Vi hämtar nycklar, samordnar med din förvaltare och lämnar bostaden gästklar."),
        ],
    },
},
"torrox": {
    "slug_sv": "torrox",
    "name": "Torrox",
    "img": (f"{_G}/handyman-axarquia-livingroom-logburner-after.webp", "Living room reform with log burner installed — after"),
    "en": {
        "title": "Builders & Reforms in Torrox & Torrox Costa | Handyman Axarquia",
        "desc": "Reforms, extensions, terraces, bathrooms and plastering in Torrox Costa, Torrox Pueblo, El Morche and the Torrox campo. Free written quotes, 12-month guarantee.",
        "h1": "Builders and reforms in Torrox and Torrox Costa",
        "lead": "Torrox Costa's apartment complexes, the white village of Torrox Pueblo and the country houses in between are all regular work for us — roughly 25 minutes from our base.",
        "prose": """
<h2>Torrox Costa apartments and urbanisations</h2>
<p>The coast at Torrox — from El Morche through Torrox Costa to the lighthouse — is largely made up of urbanisations built from the 1980s onwards. Many are now due their first serious refit: original bathrooms, kitchens and terrace tiling that have reached the end of their life. Because these complexes have active comunidades, we handle the notifications, use the approved working hours and protect common areas properly.</p>
<ul class="tick">
<li>Bathroom and kitchen refits in Torrox Costa and El Morche apartments</li>
<li>Terrace and balcony waterproofing — the most common cause of disputes between floors</li>
<li>Interior plastering, gotelé removal and repainting</li>
<li>Village houses in Torrox Pueblo: structural repairs, roof terraces, damp treatment</li>
<li>Country properties in the Torrox campo: extensions, pergolas, pool surrounds and driveways</li>
</ul>
<h2>Village and country houses</h2>
<p>Torrox Pueblo and the campo around it have a large German, British and Scandinavian community living in restored village houses and cortijos. These properties need a builder who understands old construction — lime render rather than cement on breathable walls, proper drainage on steep plots, and realistic advice about what can be legalised on rural land.</p>
<h2>Also covering</h2>
<p>El Morche, Torrox Park, Peñoncillo and Sayalonga are all within our normal working area from Torrox.</p>
""",
        "faqs": [
            ("My Torrox Costa terrace leaks into the apartment below — can you fix it permanently?",
             "Yes. The usual cause is tiles laid on an old surface with no membrane. We strip back, apply a proper waterproof membrane with the right falls, then re-tile. It is one of our most common jobs on this coast."),
            ("Do you work in Torrox Pueblo's narrow streets?",
             "Constantly. Materials are moved in by hand or small vehicle, and we plan deliveries around the village's access restrictions."),
            ("Can you convert a storeroom or garage in my Torrox house into a bedroom?",
             "Usually yes — insulation, ventilation, damp-proofing, electrics and finishes are all part of the job. We will advise on the legalisation paperwork."),
        ],
    },
    "sv": {
        "title": "Byggfirma & renovering i Torrox & Torrox Costa | Handyman Axarquia",
        "desc": "Renovering, tillbyggnader, terrasser, badrum och puts i Torrox Costa, Torrox Pueblo, El Morche och Torrox landsbygd. Svensktalande, kostnadsfri offert.",
        "h1": "Byggfirma och renovering i Torrox och Torrox Costa",
        "lead": "Lägenhetskomplexen i Torrox Costa, den vita byn Torrox Pueblo och lanthusen däremellan är alla vardagsjobb för oss — cirka 25 minuter från vår bas.",
        "prose": """
<h2>Lägenheter och urbanisationer i Torrox Costa</h2>
<p>Kusten vid Torrox — från El Morche via Torrox Costa till fyren — består till stor del av urbanisationer byggda från 1980-talet och framåt. Många är nu mogna för sin första riktiga renovering: originalbadrum, kök och terrassplattor som nått slutet av sin livslängd. Eftersom dessa komplex har aktiva samfälligheter sköter vi anmälningarna, håller de godkända arbetstiderna och skyddar gemensamma utrymmen ordentligt.</p>
<ul class="tick">
<li>Badrums- och köksrenoveringar i lägenheter i Torrox Costa och El Morche</li>
<li>Tätskikt på terrasser och balkonger — den vanligaste orsaken till tvister mellan våningar</li>
<li>Invändig puts, borttagning av gotelé och ommålning</li>
<li>Byhus i Torrox Pueblo: stomreparationer, takterrasser, fuktbehandling</li>
<li>Landsbygdsfastigheter runt Torrox: tillbyggnader, pergolor, poolområden och uppfarter</li>
</ul>
<h2>By- och lanthus</h2>
<p>Torrox Pueblo och landsbygden runt om har en stor tysk, brittisk och skandinavisk befolkning som bor i renoverade byhus och cortijos. Sådana fastigheter behöver en byggare som förstår gammal konstruktion — kalkputs i stället för cement på andande väggar, ordentlig avrinning på branta tomter och realistiska råd om vad som kan legaliseras på landsbygdsmark.</p>
<h2>Vi täcker även</h2>
<p>El Morche, Torrox Park, Peñoncillo och Sayalonga ligger alla inom vårt normala arbetsområde från Torrox.</p>
""",
        "faqs": [
            ("Min terrass i Torrox Costa läcker ner till lägenheten under — kan ni åtgärda det permanent?",
             "Ja. Den vanliga orsaken är plattor lagda på ett gammalt underlag utan tätskikt. Vi river upp, lägger ett riktigt tätskikt med rätt fall och plattsätter på nytt. Det är ett av våra vanligaste jobb på den här kusten."),
            ("Arbetar ni i de smala gränderna i Torrox Pueblo?",
             "Hela tiden. Material bärs in för hand eller med små fordon, och vi planerar leveranser efter byns trafikbegränsningar."),
            ("Kan ni göra om ett förråd eller garage i mitt hus i Torrox till sovrum?",
             "Oftast ja — isolering, ventilation, fuktspärr, el och ytskikt ingår i jobbet. Vi ger råd om legaliseringspappren."),
        ],
    },
},
"rincon-de-la-victoria": {
    "slug_sv": "rincon-de-la-victoria",
    "name": "Rincón de la Victoria",
    "img": (f"{_G}/handyman-axarquia-courtyard-lighting-after.webp", "Courtyard reform with lighting and glass floor — after"),
    "en": {
        "title": "Builders & Reforms in Rincón de la Victoria | Handyman Axarquia",
        "desc": "Reforms, kitchens, bathrooms, extensions and tiling in Rincón de la Victoria, La Cala del Moral, Torre de Benagalbón and Benajarafe. Free written quotes.",
        "h1": "Builders and reforms in Rincón de la Victoria",
        "lead": "Rincón de la Victoria is the western gateway to the Axarquia — 20 minutes from our base along the A-7 — and a fast-growing town of families and Málaga commuters who want homes modernised properly.",
        "prose": """
<h2>Modern homes that need a second life</h2>
<p>Rincón, La Cala del Moral and Torre de Benagalbón grew fast in the 1990s and 2000s. A great many of those homes — apartments near the seafront, townhouses in Añoreta and Los Rubios, and detached houses up in Cotomar and Serramar — are now 20 to 30 years old and ready for their first full reform: new kitchens, bathrooms, floors and, very often, an open-plan kitchen-living space.</p>
<ul class="tick">
<li>Complete apartment and townhouse reforms, managed by one team</li>
<li>Kitchen renovations and open-plan conversions with correct structural support</li>
<li>Bathroom refits and walk-in showers</li>
<li>Extensions, covered terraces and garage conversions on detached houses</li>
<li>Tiling, plastering and repainting inside and out</li>
</ul>
<h2>Working for families and commuters</h2>
<p>Unlike the holiday-home towns further east, most of our Rincón clients live in their property full-time and work in Málaga. That changes how we plan: we sequence work so the kitchen or a bathroom stays usable, protect the rest of the house, and keep to agreed hours. A written schedule comes with every quote.</p>
<h2>Also covering</h2>
<p>La Cala del Moral, Torre de Benagalbón, Benagalbón village, Chilches, Benajarafe and the Añoreta golf area.</p>
""",
        "faqs": [
            ("Do you cover Rincón de la Victoria, or is it too far west for you?",
             "We cover it as standard — it is about 20 minutes from our base in Almayate by the A-7, with no call-out charge."),
            ("Can you reform my home while we live in it?",
             "Yes. We phase the work room by room, seal off dust and keep essential rooms usable. Most Rincón clients stay in the house throughout."),
            ("How much does a full apartment reform cost in Rincón de la Victoria?",
             "As a guide, full reforms of apartments run from roughly €600 to €1,000 per square metre depending on finishes. Every quote is free, in writing and valid for 30 days, so you can plan without pressure."),
        ],
    },
    "sv": {
        "title": "Byggfirma & renovering i Rincón de la Victoria | Handyman Axarquia",
        "desc": "Renovering, kök, badrum, tillbyggnader och kakel i Rincón de la Victoria, La Cala del Moral, Torre de Benagalbón och Benajarafe. Svensktalande, kostnadsfri offert.",
        "h1": "Byggfirma och renovering i Rincón de la Victoria",
        "lead": "Rincón de la Victoria är Axarquías västra port — 20 minuter från vår bas längs A-7 — och en snabbt växande stad av familjer och Málaga-pendlare som vill ha sina hem ordentligt moderniserade.",
        "prose": """
<h2>Moderna hem som behöver ett andra liv</h2>
<p>Rincón, La Cala del Moral och Torre de Benagalbón växte snabbt under 1990- och 2000-talet. Många av de bostäderna — lägenheter nära strandpromenaden, radhus i Añoreta och Los Rubios samt villor uppe i Cotomar och Serramar — är nu 20 till 30 år gamla och redo för sin första helrenovering: nytt kök, nya badrum, nya golv och, mycket ofta, ett öppet kök och vardagsrum.</p>
<ul class="tick">
<li>Kompletta lägenhets- och radhusrenoveringar med ett enda team</li>
<li>Köksrenoveringar och öppna planlösningar med korrekt bärande stöd</li>
<li>Badrumsrenoveringar och walk-in-duschar</li>
<li>Tillbyggnader, täckta terrasser och garageomvandlingar på villor</li>
<li>Plattsättning, puts och ommålning inne och ute</li>
</ul>
<h2>Vi arbetar åt familjer och pendlare</h2>
<p>Till skillnad från semesterorterna längre österut bor de flesta av våra kunder i Rincón permanent och arbetar i Málaga. Det påverkar planeringen: vi lägger upp arbetet så att köket eller ett badrum går att använda, skyddar resten av huset och håller överenskomna tider. Ett skriftligt tidsschema följer med varje offert.</p>
<h2>Vi täcker även</h2>
<p>La Cala del Moral, Torre de Benagalbón, byn Benagalbón, Chilches, Benajarafe och golfområdet Añoreta.</p>
""",
        "faqs": [
            ("Täcker ni Rincón de la Victoria, eller ligger det för långt västerut?",
             "Vi täcker det som standard — cirka 20 minuter från vår bas i Almayate via A-7, utan utkörningsavgift."),
            ("Kan ni renovera medan vi bor kvar i huset?",
             "Ja. Vi delar upp arbetet rum för rum, tätar mot damm och håller viktiga rum användbara. De flesta kunder i Rincón bor kvar under hela renoveringen."),
            ("Vad kostar en helrenovering av en lägenhet i Rincón de la Victoria?",
             "Som riktmärke ligger helrenoveringar av lägenheter på ungefär 600 till 1 000 euro per kvadratmeter beroende på ytskikt. Varje offert är kostnadsfri, skriftlig och gäller i 30 dagar, så du kan planera i lugn och ro."),
        ],
    },
},
"frigiliana": {
    "slug_sv": "frigiliana",
    "name": "Frigiliana & villages",
    "img": (f"{_G}/handyman-axarquia-pergola-vinuela-after.webp", "Pergola and printed-concrete driveway on a country property near Viñuela — after"),
    "en": {
        "title": "Builders for Village & Country Houses — Frigiliana, Viñuela, Sayalonga | Handyman Axarquia",
        "desc": "Reforms, damp repairs, roof terraces, extensions and pool areas for village houses and cortijos in Frigiliana, Viñuela, Sayalonga and the Axarquia hills.",
        "h1": "Village and country house builders — Frigiliana, Viñuela and the Axarquia hills",
        "lead": "The white villages and campo of the inland Axarquia are where old construction, steep plots and rural access rules all come together. We have been building here for over three decades.",
        "prose": """
<h2>Old village houses done properly</h2>
<p>Frigiliana, Sayalonga, Canillas de Albaida and Árchez are full of village houses that have been standing for centuries — stone and earth walls, cane ceilings, rooms stacked up the hillside. They reward careful work and punish shortcuts. We use lime-based renders and plasters that let the walls breathe, sort out drainage on steep streets before it becomes damp inside, and rebuild roof terraces with proper membranes so the room below stays dry.</p>
<ul class="tick">
<li>Full reforms of village houses, phased to suit your visits</li>
<li>Damp diagnosis and repair — rising damp, hillside water, failed render</li>
<li>Roof terraces and azoteas: waterproofing, drainage, tiling</li>
<li>Replacement of cane-and-plaster ceilings and timber beams</li>
<li>Country properties: extensions, pergolas, pool surrounds, printed-concrete driveways</li>
</ul>
<h2>Cortijos and the campo around Viñuela</h2>
<p>Country houses around the Viñuela reservoir, Los Romanes, Puente Don Manuel and Alcaucín need a builder comfortable with tracks, water deposits and solar systems. We are. We also give honest advice on what can be extended or legalised on rural land, which is stricter than in the villages — better to know before you plan.</p>
<h2>Working away from the coast</h2>
<p>Inland jobs are planned with fewer, longer site visits and deliveries batched to suit the access. The villages are 35 to 50 minutes from Almayate, and we do not charge for travel.</p>
""",
        "faqs": [
            ("Why does my village house in Frigiliana get damp every winter?",
             "Usually a combination of hillside water pressure, cement render trapping moisture in earth or stone walls, and closed-up rooms with no ventilation. We diagnose the cause before quoting — treating the symptom alone never lasts."),
            ("Can I extend my cortijo near Viñuela or Frigiliana?",
             "Sometimes. Rural land has strict limits on new built area, though repairs, pergolas and some conversions are often possible. We tell you at the first visit what is realistic."),
            ("Do you handle materials in villages with no vehicle access?",
             "Yes — it is normal for us. Materials are brought in by small vehicle or by hand, and we plan the job to minimise trips."),
        ],
    },
    "sv": {
        "title": "Byggfirma för by- och lanthus — Frigiliana, Viñuela, Sayalonga | Handyman Axarquia",
        "desc": "Renovering, fuktlagning, takterrasser, tillbyggnader och poolområden för byhus och cortijos i Frigiliana, Viñuela, Sayalonga och Axarquías bergsbyar. Svensktalande.",
        "h1": "Byggfirma för by- och lanthus — Frigiliana, Viñuela och Axarquías byar",
        "lead": "De vita byarna och landsbygden i inre Axarquía är där gammal byggteknik, branta tomter och regler för landsbygdsmark möts. Vi har byggt här i över tre decennier.",
        "prose": """
<h2>Gamla byhus gjorda på rätt sätt</h2>
<p>Frigiliana, Sayalonga, Canillas de Albaida och Árchez är fulla av byhus som stått i århundraden — väggar av sten och jord, tak av rör, rum staplade uppför sluttningen. De belönar noggrant arbete och straffar genvägar. Vi använder kalkbaserad puts som låter väggarna andas, löser avrinningen i branta gränder innan den blir fukt inomhus och bygger om takterrasser med riktiga tätskikt så att rummet under förblir torrt.</p>
<ul class="tick">
<li>Helrenoveringar av byhus, i etapper anpassade efter dina besök</li>
<li>Fuktdiagnos och åtgärd — stigande fukt, vatten från sluttningen, sprucken puts</li>
<li>Takterrasser och azoteas: tätskikt, avrinning, plattsättning</li>
<li>Byte av rör- och putstak samt träbjälkar</li>
<li>Landsbygdsfastigheter: tillbyggnader, pergolor, poolområden, mönstergjutna uppfarter</li>
</ul>
<h2>Cortijos och landsbygden runt Viñuela</h2>
<p>Lanthus runt Viñuela-sjön, Los Romanes, Puente Don Manuel och Alcaucín kräver en byggare som är bekväm med grusvägar, vattentankar och solcellssystem. Det är vi. Vi ger också ärliga råd om vad som kan byggas ut eller legaliseras på landsbygdsmark — reglerna är strängare än i byarna, och det är bättre att veta innan du planerar.</p>
<h2>Arbete inne i landet</h2>
<p>Jobb i inlandet planeras med färre men längre platsbesök och leveranser samlade efter åtkomsten. Byarna ligger 35 till 50 minuter från Almayate, och vi tar inget för resan.</p>
""",
        "faqs": [
            ("Varför blir mitt byhus i Frigiliana fuktigt varje vinter?",
             "Oftast en kombination av vattentryck från sluttningen, cementputs som stänger in fukt i jord- eller stenväggar och stängda rum utan ventilation. Vi diagnostiserar orsaken innan vi lämnar offert — att bara behandla symptomet håller aldrig."),
            ("Kan jag bygga ut min cortijo nära Viñuela eller Frigiliana?",
             "Ibland. Landsbygdsmark har strikta gränser för ny byggyta, men reparationer, pergolor och vissa ombyggnader är ofta möjliga. Vi säger vid första besöket vad som är realistiskt."),
            ("Hanterar ni material i byar utan bilväg?",
             "Ja — det är vardag för oss. Material körs in med små fordon eller bärs, och vi planerar jobbet för att minimera antalet turer."),
        ],
    },
},
}
