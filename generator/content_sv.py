# Swedish content for handymanaxarquia.com/sv/
from helpers import make_url_fn, service_body, cta_band, SERVICE_ORDER
from content_en import SV_SLUGS, gallery_body, contact_body

u = make_url_fn(SV_SLUGS)

UI = {
    "nav_home": "Hem", "nav_services": "Tjänster", "nav_gallery": "Galleri", "nav_contact": "Kontakt",
    "services_names": {
        "reforms": "Renoveringar", "plastering": "Puts & fasad",
        "extensions": "Tillbyggnader", "tiling": "Kakel & klinker",
        "bathrooms": "Badrumsrenovering", "kitchens": "Köksrenovering",
    },
    "aside_title": "Få en kostnadsfri offert",
    "aside_blurb": "Berätta om ditt projekt så återkommer vi samma dag med en offert utan förpliktelser.",
    "aside_wa": "Skriv till oss på WhatsApp",
    "aside_terms": "Kostnadsfria offerter · 50 % handpenning vid bokning, resten vid färdigställande · 12 månaders garanti på arbetet.",
    "faq_title": "Vanliga frågor",
    "cta_h": "Redo att sätta igång? <em>Hör av dig.</em>",
    "cta_p": "Kostnadsfria offerter i hela Axarquía. Ring, skriv på WhatsApp eller skicka ett meddelande — vi svarar samma dag, på svenska eller engelska.",
    "cta_btn": "Begär kostnadsfri offert",
    "foot_blurb": "Professionellt bygg-, renoverings- och fastighetsarbete i Axarquía och östra Costa del Sol. Över 25 års erfarenhet — alltid i tid och inom budget.",
    "foot_areas": "Vi arbetar i: Torre del Mar, Vélez-Málaga, Algarrobo, Caleta de Vélez, Almayate, Nerja, Torrox, Frigiliana, Cómpeta, Viñuela och Rincón de la Victoria.",
    "foot_pages": "Sidor",
    "foot_rights": "Alla rättigheter förbehållna.",
    "spain": "Spanien",
}

REFORMS_PROSE = """
<h2>Hel- och delrenoveringar av bostäder</h2>
<p>Har du köpt ett radhus i Vélez-Málaga som behöver moderniseras, eller är semesterlägenheten i Torre del Mar redo för ett lyft? Vi tar hand om hela renoveringen från första skiss till slutstädning. Ett team, en kontaktperson, ett avtalat pris — du slipper jaga olika hantverkare runt om i Axarquía.</p>
<ul class="tick">
<li>Helrenoveringar — rivning, planlösningsändringar, nya installationer och ytskikt</li>
<li>Delrenoveringar — ett golv, en fasad, en terrass eller ett enskilt rum</li>
<li>Konstruktionsarbeten — väggar tas bort med korrekta balkar och stöd</li>
<li>Nya el- och VVS-installationer enligt gällande spanska regler</li>
<li>Fuktbehandling, isolering och fönsterbyte</li>
<li>Målning, golv, snickeri och alla avslutande arbeten</li>
</ul>
<h2>Så arbetar vi</h2>
<p>Varje renovering börjar med ett kostnadsfritt besök och en tydlig skriftlig offert, så att du ser exakt vart budgeten går. Vi tar 50 % handpenning för att boka in arbetet och beställa material; resten betalas först när jobbet är klart och du är nöjd. Oförutsedda problem — och äldre spanska hus gillar att gömma sådana — prissätts och godkänns alltid skriftligt innan vi fortsätter.</p>
<p>Vi är vana att arbeta åt ägare som inte bor i Spanien året runt. Många av våra kunder i Nerja, Torrox och byarna i Axarquía följer sin renovering via veckovisa fotouppdateringar på WhatsApp — och kommer tillbaka till ett färdigt, städat hem.</p>
<h2>Renoveringar i hela Axarquía</h2>
<p>Med bas i Almayate utför vi renoveringar i Torre del Mar, Vélez-Málaga, Nerja, Torrox, Caleta de Vélez, Algarrobo, Frigiliana, Cómpeta, Viñuela, Rincón de la Victoria och i hela Axarquía. Även lanthus och cortijos — vi känner väl till utmaningarna med tillfart, vatten och el på landsbygden.</p>
"""

PLASTERING_PROSE = """
<h2>Putsning, spackling och fasadputs</h2>
<p>Bra putsarbete är skillnaden mellan en målning som ser platt ut och väggar som ser nya ut. Vi putsar invändigt, lagar och putsar fasader och åtgärdar de spruckna, bom- och fuktskadade ytor som är så vanliga i spanska kustfastigheter.</p>
<ul class="tick">
<li>Invändig putsning och finspackling — släta ytor redo för målning</li>
<li>Borttagning av gotelé (strukturtapet/strukturfärg) — moderna släta väggar</li>
<li>Fasadputs — traditionell puts och monocapa, ny eller reparerad</li>
<li>Lagning av sprickor och bomputs på fasader och murar</li>
<li>Fuktskadad puts avlägsnas, väggen behandlas och putsas om korrekt</li>
<li>Dekorativa ytskikt och detaljer kring valv och kanter</li>
</ul>
<h2>Fuktproblem vid kusten</h2>
<p>Fastigheter i Torre del Mar, Almayate och längs kusten utsätts hårt för salt luft och vinterfukt. Att måla över fuktig puts döljer bara problemet en säsong. Vi tar bort den skadade putsen, åtgärdar orsaken — stigande fukt, skadad fasadputs, dåliga fogar — och putsar om med rätt diffusionsöppna material så att lagningen håller.</p>
<h2>Rent och dammkontrollerat</h2>
<p>Putsarbete är smutsigt, men ditt hem behöver inte bli det. Golv och möbler täcks, rummen försluts medan vi arbetar och vi lämnar alla ytor rena. De flesta enskilda rum är spacklade och redo för målning inom två till tre dagar.</p>
"""

EXTENSIONS_PROSE = """
<h2>Tillbyggnader och nybyggnation</h2>
<p>Behöver du mer plats? Ett extra sovrum för gäster, ett större kök eller en täckt terrass för utomhusliv året runt — en tillbyggnad är ofta betydligt bättre värde än att flytta. Vi bygger till i hela Axarquía och hanterar allt från grund till sista strykningen färg.</p>
<ul class="tick">
<li>Tillbyggnader i ett plan och annex</li>
<li>Täckta terrasser, uterum och pergolor</li>
<li>Garage och förråd som görs om till boyta</li>
<li>Utekök och grillplatser</li>
<li>Poolhus och casitas</li>
<li>Takterrasser och solarium</li>
</ul>
<h2>Bygglov och papper</h2>
<p>Byggarbeten i Spanien kräver rätt tillstånd — licencia de obra menor för mindre projekt eller obra mayor med arkitektprojekt för konstruktiva tillbyggnader. Vi samarbetar med lokala arkitekter och kommunerna i Vélez-Málaga, Torrox och Nerja, och redan i offertskedet berättar vi ärligt vilka tillstånd ditt projekt kräver och vad de brukar kosta. Inga överraskningar halvvägs in.</p>
<h2>Byggt för klimatet</h2>
<p>En tillbyggnad på Costa del Sol måste klara stark sommarsol och piskande vinterregn. Vi bygger med ordentlig isolering, fuktspärr och solskydd från början, så att ditt nya utrymme fungerar lika bra i augusti som i januari.</p>
"""

TILING_PROSE = """
<h2>Kakel och klinker — golv och vägg</h2>
<p>Plattsättningen är ytan du ser och rör vid varje dag, och den förlåter inga genvägar — ojämna plattor, sneda fogar och bomplattor gör sig påminda i åratal. Våra plattsättare mäter upp varje jobb ordentligt, kapar rent och lägger i våg — oavsett om det gäller ett stänkskydd i badrummet eller tvåhundra kvadratmeter terrass.</p>
<ul class="tick">
<li>Golvläggning inomhus — klinker, keramik och natursten</li>
<li>Väggkakel i badrum, kök och accentväggar</li>
<li>Terrasser och poolområden med halkfria och frostsäkra plattor</li>
<li>Storformatplattor och golvdusch i nivå med golvet</li>
<li>Reparationer — bomplattor och spruckna plattor, omfogning och försegling</li>
<li>Tätskikt (impermeabilización) under terrasser och våtutrymmen</li>
</ul>
<h2>Terrasser som inte läcker</h2>
<p>En stor del av läckorna vi lagar i Axarquía börjar med en terrass som kaklats direkt på gamla ytor utan membran. Vi lägger tätskikt först, sedan plattor, med korrekta fall och rörelsefogar — så att vattnet rinner till avloppet i stället för in i sovrummet under.</p>
<h2>Med eller utan material</h2>
<p>Välj plattor själv hos valfri lokal leverantör — vi rekommenderar gärna butiker i Torre del Mar och Vélez-Málaga — eller beskriv looken du vill ha så tar vi fram alternativ inom din budget. Oavsett vilket får du en tydlig skriftlig offert per kvadratmeter, godkänd innan vi börjar.</p>
"""

BATHROOMS_PROSE = """
<h2>Kompletta badrumsrenoveringar</h2>
<p>Ett omodernt badrum drar ner helhetsintrycket av hela bostäden — och i uthyrningsbostäder är det det första gästerna fotograferar. Vi renoverar badrum i hela Axarquía från rivning till silikon: VVS, el, tätskikt, kakel, inredning och finish — allt av ett och samma team enligt en och samma tidplan.</p>
<ul class="tick">
<li>Totalrenovering av badrum, normalt klart på en till två veckor</li>
<li>Badkar byts till dusch och walk-in-duschar</li>
<li>Golvduschar i nivå med golvet — perfekt för tillgänglighet och små ytor</li>
<li>Nytt porslin, kommoder, speglar och handdukstorkar</li>
<li>Ordentligt tätskikt innan en enda platta sätts</li>
<li>Ventilation som håller mögel borta för gott</li>
</ul>
<h2>Utformat efter verklig användning</h2>
<p>Semesterbostad, uthyrning eller permanentboende — alla kräver olika val. Uthyrningsbostäder behöver tåliga, lättstädade ytor som klarar gäster; ett pensionärsboende vinner på golvdusch och väggar förberedda för stödhandtag. Vi ger råd om det som faktiskt fungerar, inte bara det som ser bra ut i en utställningshall.</p>
<h2>En tydlig, fast process</h2>
<p>Du får en tydlig offert, ett startdatum och en realistisk tidplan. Vi skyddar resten av hemmet, tar hand om vårt eget byggavfall och stänger av vattnet så kort tid som möjligt — har bostäden ett andra badrum står du aldrig utan fungerande badrum över natten.</p>
"""

KITCHENS_PROSE = """
<h2>Köksrenoveringar</h2>
<p>Köket är där budgetar vinns och förloras. Vi renoverar kök i hela Axarquía med ett team som sköter rivning, VVS, el, puts, kakel och montering — så att stommar, bänkskiva och vitvaror levereras till ett rum som faktiskt är redo för dem.</p>
<ul class="tick">
<li>Komplett rivning och nytt kök</li>
<li>Planlösningändringar — väggar flyttas, köksöar byggs, öppen planlösning</li>
<li>Ny el med tillräckligt många kretsar för moderna apparater</li>
<li>VVS för diskhöar, diskmaskiner, vattenfilter och gashällar</li>
<li>Stänkskydd i kakel eller sten och slitstarka golv</li>
<li>Montering av kök från valfri leverantör — eller så tar vi fram ett</li>
</ul>
<h2>Eget kök eller via oss</h2>
<p>Många kunder köper stommarna från större kedjor eller lokala köksstudior i Vélez-Málaga och låter oss göra allt annat: förarbete, installationer, montering och finish. Andra ger oss en budget och en bild. Båda fungerar — offerten visar alltid exakt vad som ingår.</p>
<h2>Öppen planlösning</h2>
<p>Det mest efterfrågade jobbet i spanska radhus och lägenheter: att ta bort väggen mellan ett stängt kök och vardagsrummet. Rätt utfört — med konstruktionsbedömning, korrekt dimensionerad balk och bygglov där det krävs — förvandlar det både hur bostäden fungerar och vad den är värd.</p>
"""

def _svc(key, title, desc, h1, lead, prose, faqs):
    return {"key": key, "slug": SV_SLUGS[key], "title": title, "desc": desc,
            "h1": h1, "lead": lead, "prose": prose, "faqs": faqs}

SERVICES = {
"reforms": _svc("reforms",
    "Renovering i Axarquía, Spanien | Handyman Axarquia",
    "Hel- och delrenoveringar i Torre del Mar, Vélez-Málaga, Nerja och hela Axarquía. Ett team, tydliga offerter, 12 månaders garanti. Kostnadsfri offert på svenska.",
    "Renoveringar i Axarquía — ordentligt utförda",
    "Hel- och delrenoveringar av lägenheter, radhus och lanthus — hanterade från start till mål av ett erfaret team på östra Costa del Sol. Vi talar svenska.",
    REFORMS_PROSE,
    [("Vad kostar en renovering i Axarquía?",
      "Det beror på omfattning och standard, men som riktmärke: en enklare uppfräschning (målning, golv, dörrar) börjar på några tusen euro per rum, medan helrenoveringar av lägenheter normalt ligger på 600–1 000 € per kvadratmeter. Alla våra offerter är tydliga och detaljerade så att du kan anpassa omfattningen efter budgeten."),
     ("Hur lång tid tar en helrenovering?",
      "En etta/tvåa tar normalt 4–6 veckor; ett helt radhus 2–4 månader beroende på konstruktionsarbeten. Du får en tidplan med offerten och veckovisa uppdateringar."),
     ("Kan ni sköta renoveringen medan jag är i Sverige?",
      "Ja — de flesta av våra kunder är utomlands under hela eller delar av projektet. Vi skickar foto- och videouppdateringar varje vecka via WhatsApp eller e-post och tar hand om nycklar, leveranser och hantverkare."),
     ("Behöver jag bygglov för en renovering?",
      "Ytskiktsrenoveringar kräver oftast bara en enkel licencia de obra menor från kommunen; konstruktiva ändringar kräver mer. Vi berättar vad som gäller redan i offertskedet och kan sköta ansökan.")]),

"plastering": _svc("plastering",
    "Putsarbeten & fasadputs i Axarquía | Handyman Axarquia",
    "Invändig putsning, finspackling, gotelé-borttagning och fasadputs i Torre del Mar, Vélez-Málaga, Nerja och Axarquía. Fuktskador åtgärdas ordentligt.",
    "Putsarbeten och fasadputs i Axarquía",
    "Slät invändig puts, fasadputs och hållbara fuktlagningar för kust- och lanthus på östra Costa del Sol.",
    PLASTERING_PROSE,
    [("Kan ni ta bort gotelé (strukturfärg)?",
      "Ja — borttagning av gotelé med efterföljande finspackling är ett av våra vanligaste jobb. Beroende på typ blöter vi upp och skrapar, eller spacklar direkt över, så att väggarna blir släta och redo för modern färg."),
     ("Hur hanterar ni fuktiga väggar?",
      "Vi putsar aldrig bara över fukt. Vi tar bort den skadade putsen, identifierar orsaken — stigande fukt, skadad fasadputs, kondens — åtgärdar den och putsar sedan om med diffusionsöppna material som passar väggen."),
     ("När kan jag måla på ny puts?",
      "I Axarquías klimat är spacklade väggar normalt torra nog för en grundstrykning inom 3–7 dagar beroende på säsong och tjocklek. Vi säger till när det är säkert att måla."),
     ("Gör ni små putslagningar också?",
      "Ja. Sprickor, bomputs, hål efter elarbeten — inget jobb är för litet, och mindre lagningar klaras oftast på ett enda besök.")]),

"extensions": _svc("extensions",
    "Tillbyggnader i Axarquía, Spanien | Handyman Axarquia",
    "Tillbyggnader, täckta terrasser, garagekonverteringar och casitas i Torre del Mar, Vélez-Málaga, Nerja och Axarquía. Hjälp med bygglov ingår.",
    "Tillbyggnader på östra Costa del Sol",
    "Från täckta terrasser till hela extra rum — anpassade för klimatet, byggda enligt reglerna och tydligt prissatta innan vi börjar.",
    EXTENSIONS_PROSE,
    [("Behöver jag bygglov för en tillbyggnad i Spanien?",
      "Nästan alltid, ja. Mindre arbeten kan rymmas inom en licencia de obra menor, men allt konstruktivt eller ytutökande kräver obra mayor med arkitektprojekt. Vi guidar dig genom kommunens krav och samarbetar med lokala arkitekter."),
     ("Vad kostar en tillbyggnad per kvadratmeter?",
      "Som riktmärke ligger enklare tillbyggnader i ett plan i Axarquía på 1 000–1 600 € per kvadratmeter inklusive ytskikt, plus arkitekt- och bygglovskostnader. Täckta terrasser och uterum kostar betydligt mindre."),
     ("Kan ni göra om mitt garage eller förråd till sovrum?",
      "Oftast ja — och det är ett av de mest kostnadseffektiva sätten att få mer yta. Vi sköter isolering, fuktspärr, ventilation, el och ytskikt, och ger råd om legaliseringen."),
     ("Hur lång tid tar en tillbyggnad?",
      "En täckt terrass eller ett uterum: 1–3 veckor. Ett extra rum: 6–10 veckor inklusive torktider. Du får en skriftlig tidplan med offerten.")]),

"tiling": _svc("tiling",
    "Kakel & klinker i Axarquía | Handyman Axarquia",
    "Professionell plattsättning av golv, väggar, badrum och terrasser i Torre del Mar, Vélez-Málaga, Nerja och Axarquía. Tätskikt gjort på rätt sätt.",
    "Professionell plattsättning i Axarquía",
    "Golv, väggar, badrum, kök och terrasser — uppmätt ordentligt, kapat rent och förseglat för att hålla, var som helst på östra Costa del Sol.",
    TILING_PROSE,
    [("Vad kostar plattsättning per kvadratmeter?",
      "Arbetskostnaden för golvläggning i standardformat ligger normalt på 25–40 € per m² i Axarquía; väggar, storformat, natursten och terrasser kostar mer på grund av förarbete och kapning. Offerten är tydlig och detaljerad innan arbetet börjar."),
     ("Min terrass läcker in i rummet under — löser nya plattor det?",
      "Plattor i sig tätar ingenting. Vi river upp, lägger ett riktigt tätskikt med korrekta fall och kaklar sedan. Den kombinationen löser läckan permanent — det är ett av våra vanligaste jobb."),
     ("Kan ni kakla ovanpå befintligt kakel?",
      "Ibland, om underlaget är stabilt och höjderna tillåter. Det sparar pengar och damm men är inte alltid rätt val — vi bedömer på plats och ger dig båda alternativen med pris."),
     ("Står ni för plattorna eller köper jag själv?",
      "Valfritt. Många kunder väljer plattor själva i lokala butiker — vi hämtar gärna — eller så tar vi fram alternativ inom en budget och kommer med prover.")]),

"bathrooms": _svc("bathrooms",
    "Badrumsrenovering i Axarquía | Handyman Axarquia",
    "Kompletta badrumsrenoveringar, walk-in-duschar och golvduschar i Torre del Mar, Vélez-Málaga, Nerja och Axarquía. Ett team, fast offert, 12 månaders garanti.",
    "Badrumsrenovering i Axarquía",
    "Från rivning till silikon på en till två veckor — VVS, tätskikt, kakel och montering av ett och samma team, med skriftlig fast offert.",
    BATHROOMS_PROSE,
    [("Vad kostar en badrumsrenovering?",
      "En komplett renovering av ett badrum i normalstorlek ligger i Axarquía normalt på 4 500–9 000 € beroende på inredning och plattor; golvduschar och premiumval därutöver. Offerten är tydlig så att du kan anpassa valen efter budget."),
     ("Hur länge är jag utan badrum?",
      "En typisk totalrenovering tar 7–12 arbetsdagar. Vattnet stängs bara av korta stunder, och har bostäden ett andra badrum står du aldrig utan över natten."),
     ("Kan ni byta badkaret mot en walk-in-dusch?",
      "Ja — det är vårt mest efterfrågade badrumsjobb. Inklusive nytt duschkar eller platsbyggd dusch, glasvägg, kakel och VVS tar de flesta konverteringar 3–5 dagar."),
     ("Lägger ni tätskikt innan ni kaklar?",
      "Alltid. Våtzoner förses med tätskikt innan en enda platta sätts. Det syns inte när det är klart — men det är skillnaden mellan ett badrum som håller och ett som läcker ner till grannen.")]),

"kitchens": _svc("kitchens",
    "Köksrenovering i Axarquía | Handyman Axarquia",
    "Köksrenoveringar i Torre del Mar, Vélez-Málaga, Nerja och Axarquía — öppen planlösning, el, VVS, kakel och montering. Kostnadsfri offert på svenska.",
    "Köksrenovering i Axarquía",
    "Ett team för hela jobbet — rivning, väggar, el, VVS, kakel och montering — oavsett om du köper köket själv eller via oss.",
    KITCHENS_PROSE,
    [("Vad kostar en köksrenovering?",
      "Förarbete och installation (allt utom stommar och vitvaror) ligger normalt på 3 000–7 000 € beroende på planlösningändringar och ytskikt. Med stommar i mellanklass ingår hamnar kompletta kök i Axarquía oftast mellan 8 000 och 15 000 €."),
     ("Kan ni öppna upp till öppen planlösning?",
      "Oftast ja. Vi bedömer om väggen är bärande, monterar en korrekt dimensionerad balk där det behövs och ger råd om bygglovet. Det är det enskilt mest förvandlande jobbet i de flesta spanska lägenheter och radhus."),
     ("Monterar ni ett kök jag köper någon annanstans?",
      "Ja — vi förbereder regelbundet rum för och monterar kök från större kedjor och lokala köksstudior. Vi samordnar leverans, drar fram el och VVS och sköter hela monteringen."),
     ("Hur lång tid tar ett köksbyte?",
      "Utan planlösningändringar: 1–2 veckor. Med flyttade väggar eller öppen planlösning: 3–5 veckor inklusive puts och torktider. Tidplan följer med offerten.")]),
}

# ---------------------------------------------------------------- home (SV)

def home_body(lang, ui):
    cards = "".join(f"""<div class="card">
      <div class="ico">◆</div>
      <h3>{ui["services_names"][k]}</h3>
      <p>{HOME_CARDS[k]}</p>
      <a class="more" href="{u(lang, k)}">Läs mer</a>
    </div>""" for k in SERVICE_ORDER)
    return f"""<div class="hero"><div class="container">
  <div class="kicker">Torre del Mar · Vélez-Málaga · Nerja · Axarquía</div>
  <h1>Bygg, renovering &amp; fastighetsservice på <em>östra Costa del Sol</em></h1>
  <p class="lead">Ett pålitligt team för renoveringar, tillbyggnader, puts, kakel, badrum och kök. Över 25 års erfarenhet — alltid i tid och inom budget. Vi talar svenska.</p>
  <div class="actions">
    <a class="btn primary" href="{u(lang,'contact')}">Begär kostnadsfri offert</a>
    <a class="btn ghost" href="https://wa.me/34711027432">WhatsApp</a>
  </div>
  <img class="mark" src="/images/logo_mark.svg" alt="">
</div></div>
<div class="trustbar"><div class="container">
  <div><b>25+ års</b> erfarenhet</div>
  <div><b>Kostnadsfria</b> offerter</div>
  <div><b>12 månaders</b> garanti på arbetet</div>
  <div>Vi talar <b>svenska</b> &amp; <b>engelska</b></div>
</div></div>
<section><div class="container">
  <div class="sec-head">
    <div class="kicker">Vad vi gör</div>
    <h2>Tjänster i hela Axarquía</h2>
    <p>Från ett enskilt rum till en hel fastighet — varje jobb med skriftlig offert, ordentligt utfört och med 12 månaders garanti.</p>
  </div>
  <div class="grid c3">{cards}</div>
</div></section>
<section class="alt"><div class="container">
  <div class="sec-head">
    <div class="kicker">Varför Handyman Axarquia</div>
    <h2>Ett team. En offert. Inga överraskningar.</h2>
  </div>
  <div class="grid c2">
    <div class="card"><div class="ico">✎</div><h3>Tydliga skriftliga offerter</h3><p>En detaljerad skriftlig offert innan vi börjar, så att du alltid vet vart budgeten går. 50 % handpenning vid bokning, resten först vid färdigställande.</p></div>
    <div class="card"><div class="ico">⌂</div><h3>Vi arbetar åt ägare på distans</h3><p>Utomlands större delen av året? Det är de flesta av våra kunder. Fotouppdateringar varje vecka på WhatsApp, säker nyckelhantering och städat efter oss.</p></div>
    <div class="card"><div class="ico">✓</div><h3>Garanterat hantverk</h3><p>Alla arbeten har 12 månaders garanti, och material behåller tillverkarens garanti.</p></div>
    <div class="card"><div class="ico">☏</div><h3>Snabba, ärliga svar</h3><p>Ring eller skriv på WhatsApp vardagar 8–20. Passar ett jobb oss inte säger vi det — och tipsar om någon bra.</p></div>
  </div>
</div></section>
<section><div class="container">
  <div class="sec-head">
    <div class="kicker">Var vi arbetar</div>
    <h2>Hela Axarquía</h2>
    <p>Med bas i Almayate, några minuter från Torre del Mar — vi täcker Vélez-Málaga, Algarrobo, Caleta de Vélez, Nerja, Torrox, Frigiliana, Cómpeta, Viñuela, Rincón de la Victoria samt byarna och campon runt omkring.</p>
    <ul class="tick" style="max-width:760px;margin:18px auto 0;display:grid;grid-template-columns:repeat(3,1fr);gap:4px 24px;text-align:left">
      <li>Torre del Mar</li><li>Vélez-Málaga</li><li>Algarrobo</li>
      <li>Caleta de Vélez</li><li>Almayate</li><li>Nerja</li>
      <li>Torrox</li><li>Frigiliana</li><li>Cómpeta</li>
      <li>Viñuela</li><li>Rincón de la Victoria</li><li>Byar &amp; campo i Axarquía</li>
    </ul>
  </div>
</div></section>
{cta_band(lang, ui, u)}"""

HOME_CARDS = {
    "reforms": "Hel- och delrenoveringar hanterade från start till mål — rivning till slutstädning.",
    "plastering": "Slät invändig puts, gotelé-borttagning, fasadputs och hållbara fuktlagningar.",
    "extensions": "Extra rum, täckta terrasser och konverteringar — byggda för klimatet, med rätt bygglov.",
    "tiling": "Golv, väggar och terrasser plattsatta med precision — med tätskikt som aldrig läcker.",
    "bathrooms": "Kompletta badrumsrenoveringar och walk-in-duschar, klart på 1–2 veckor.",
    "kitchens": "Köksbyten och öppna planlösningar — ett team för hela jobbet.",
}

# ---------------------------------------------------------------- assemble

PAGES = {}
PAGES["home"] = {"key": "home", "slug": "",
    "title": "Handyman Axarquia | Bygg & renovering — Torre del Mar, Vélez-Málaga, Nerja",
    "desc": "Professionell bygg- och renoveringsfirma i Torre del Mar, Nerja, Frigiliana, Cómpeta, Rincón de la Victoria och hela Axarquía, Costa del Sol. Kostnadsfria offerter. Vi talar svenska.",
    "body": home_body}
for k, s in SERVICES.items():
    s["body"] = service_body(s, u)
    PAGES[k] = s
PAGES["gallery"] = {"key": "gallery", "slug": SV_SLUGS["gallery"],
    "title": "Galleri — Våra arbeten | Handyman Axarquia",
    "desc": "Aktuella renoveringar, badrum, kök, plattsättningar och tillbyggnader av Handyman Axarquia i Torre del Mar, Vélez-Málaga, Nerja och Axarquía.",
    "body": gallery_body}
PAGES["contact"] = {"key": "contact", "slug": SV_SLUGS["kontakt"] if "kontakt" in SV_SLUGS else SV_SLUGS["contact"],
    "title": "Kontakt & kostnadsfri offert | Handyman Axarquia",
    "desc": "Få en kostnadsfri offert för renovering och byggarbeten i Axarquía. Ring +34 711 027 432, skriv på WhatsApp eller skicka ett meddelande — svar på svenska.",
    "body": contact_body}
