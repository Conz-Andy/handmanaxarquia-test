# Marketing pack hub (/brand/) — admin-bar selector over every brand asset,
# plus a presupuesto page at standard market rates. Generated into site/ at build time.
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PHONE = "+34 711 027 432"
EMAIL = "info@handymanaxarquia.com"
WEB = "handymanaxarquia.com"
ADDR1 = "Los Toscanos 33, Almayate Bajo"
ADDR2 = "29749 Málaga, Spain"

# ---------------------------------------------------------------- document CSS

DOC_CSS = """
:root { --orange:#FBA917; --black:#0B0B0C; --ink:#1C1C1E; --muted:#6E6E73;
  --line:#E8E6E1; --paper:#FFFFFF; --wash:#F7F6F3; }
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Poppins',sans-serif; color:var(--ink); background:#3a3a3e;
  font-size:9pt; line-height:1.45; -webkit-print-color-adjust:exact; print-color-adjust:exact;
  display:flex; justify-content:center; padding:20px 0; }
.page { width:210mm; min-height:297mm; background:var(--paper); position:relative;
  display:flex; flex-direction:column; box-shadow:0 10px 40px rgba(0,0,0,.4); }
@media print { body{background:#fff;padding:0} .page{box-shadow:none} @page{size:A4;margin:0} }
.head { background:var(--black); color:#fff; padding:7mm 14mm 6mm;
  display:flex; align-items:center; justify-content:space-between; }
.head .brand { display:flex; align-items:center; gap:6mm; }
.head .brand img { width:18mm; height:18mm; }
.head .brand .name { font-size:15pt; font-weight:700; letter-spacing:.5px; line-height:1.15; }
.head .brand .name span { color:var(--orange); }
.head .brand .tag { font-size:7.5pt; color:#B9B9BE; letter-spacing:2.2px; text-transform:uppercase; margin-top:1mm; }
.doc-title { text-align:right; }
.doc-title h1 { font-size:22pt; font-weight:300; letter-spacing:6px; text-transform:uppercase; color:#fff; }
.doc-title .accent { display:inline-block; width:18mm; height:1.2mm; background:var(--orange); margin-top:2mm; }
.rule { height:1.6mm; background:var(--orange); }
.meta { display:flex; justify-content:space-between; gap:8mm; padding:6mm 14mm 0; }
.meta .block { font-size:9pt; }
.meta .block h3 { font-size:7pt; font-weight:600; letter-spacing:2px; text-transform:uppercase; color:var(--muted); margin-bottom:2mm; }
.meta .block .big { font-weight:600; font-size:10.5pt; color:var(--black); }
.kv { display:grid; grid-template-columns:auto auto; gap:.5mm 5mm; font-size:9pt; }
.kv dt { color:var(--muted); } .kv dd { font-weight:500; text-align:right; }
.items { padding:4mm 14mm 0; flex:1; }
table { width:100%; border-collapse:collapse; }
thead th { background:var(--black); color:#fff; font-size:7.5pt; font-weight:600;
  letter-spacing:1.5px; text-transform:uppercase; padding:2.6mm 4mm; text-align:left; }
thead th:first-child { border-radius:2mm 0 0 0; }
thead th:last-child { border-radius:0 2mm 0 0; text-align:right; }
tbody td { padding:2.7mm 4mm; border-bottom:.35mm solid var(--line); vertical-align:top; }
tbody tr:nth-child(even) td { background:var(--wash); }
td.num, th.num { text-align:right; white-space:nowrap; font-variant-numeric:tabular-nums; }
td .desc-sub { color:var(--muted); font-size:8pt; }
.totals-wrap { display:flex; justify-content:flex-end; padding:5mm 14mm 0; }
.totals { width:82mm; font-size:9.5pt; }
.totals .row { display:flex; justify-content:space-between; padding:1.3mm 4mm; }
.totals .row.sub { color:var(--muted); }
.totals .grand { background:var(--black); color:#fff; border-radius:2mm; font-weight:600;
  font-size:11.5pt; padding:3.2mm 4mm; margin-top:2mm; }
.totals .grand .cur { color:var(--orange); }
.totals .deposit { background:#FFF4DE; border:.4mm solid var(--orange); border-radius:2mm;
  margin-top:2.5mm; padding:2.6mm 4mm; font-size:8.5pt; }
.totals .deposit b { color:#A96D00; }
.notes { padding:3.5mm 14mm 0; display:flex; gap:8mm; }
.notes .col { flex:1; }
.notes h4 { font-size:7pt; font-weight:600; letter-spacing:2px; text-transform:uppercase;
  color:var(--black); margin-bottom:2mm; border-bottom:.5mm solid var(--orange);
  display:inline-block; padding-bottom:1mm; }
.notes p, .notes li { font-size:7.2pt; color:var(--muted); line-height:1.45; }
.notes ol { padding-left:4mm; } .notes li { margin-bottom:1mm; }
.foot { margin-top:auto; background:var(--black); color:#C9C9CE; padding:3.5mm 14mm;
  font-size:8pt; display:flex; align-items:center; justify-content:space-between; gap:6mm; }
.foot .contact { display:flex; flex-direction:column; gap:1mm; }
.foot .contact .line { display:flex; align-items:center; gap:2.5mm; }
.foot .dot { color:var(--orange); font-weight:700; }
.foot a { color:#fff; text-decoration:none; }
.foot .qr { background:#fff; border-radius:2mm; padding:1.5mm; }
.foot .qr img { width:13mm; height:13mm; display:block; }
.foot .scan { font-size:6.5pt; letter-spacing:1.5px; text-transform:uppercase; color:#8E8E93; text-align:center; margin-top:1mm; }
"""

FONT_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
             '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">')

def doc_head(title):
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{title}</title>{FONT_LINK}<style>{DOC_CSS}</style></head><body>')

DOC_BRAND = f"""<div class="head">
  <div class="brand">
    <img class="dlogo" src="/images/logo.png" alt="">
    <div>
      <div class="name">HANDYMAN <span>AXARQUIA</span></div>
      <div class="tag">Property Care &amp; Repairs · Costa del Sol</div>
    </div>
  </div>
  <div class="doc-title"><h1>__TITLE__</h1><span class="accent"></span></div>
</div>
<div class="rule"></div>"""

def doc_foot(center):
    return f"""<div class="foot">
  <div class="contact">
    <div class="line"><span class="dot">✆</span> {PHONE}</div>
    <div class="line"><span class="dot">✉</span> {EMAIL}</div>
    <div class="line"><span class="dot">⌂</span> {WEB}</div>
  </div>
  <div style="text-align:center;font-size:7pt;color:#8E8E93;max-width:70mm">{center}<br>Handyman Axarquia · {ADDR1}, 29749 Málaga</div>
  <div><div class="qr"><img src="/images/qr_website.png" alt="QR"></div><div class="scan">Scan · Website</div></div>
</div></div></body></html>"""

FROM_BLOCK = f"""<div class="block"><h3>From</h3>
  <div class="big">Handyman Axarquia</div><div>{ADDR1}</div><div>{ADDR2}</div><div>NIF/CIF: [NIF/CIF]</div></div>"""

INVOICE_PAGE = doc_head("Sample Invoice — Handyman Axarquia") + '<div class="page">' + \
DOC_BRAND.replace("__TITLE__", "Invoice") + f"""
<div class="meta">{FROM_BLOCK}
  <div class="block"><h3>Billed To</h3><div class="big">Sample Client</div>
    <div>Calle Ejemplo 12</div><div>29740 Torre del Mar, Málaga</div><div>NIF: X0000000X</div></div>
  <div class="block"><h3>Invoice Details</h3><dl class="kv">
    <dt>Invoice №</dt><dd>INV-2026-041</dd><dt>Issue date</dt><dd>1 August 2026</dd>
    <dt>Due date</dt><dd>8 August 2026</dd><dt>Quote ref.</dt><dd>Q-2026-038</dd></dl></div>
</div>
<div class="items"><table><thead><tr><th style="width:52%">Description</th>
<th class="num" style="width:12%">Qty</th><th class="num" style="width:18%">Unit&nbsp;(€)</th>
<th class="num" style="width:18%">Amount&nbsp;(€)</th></tr></thead><tbody>
<tr><td><b>Bathroom renovation — labour</b><div class="desc-sub">Remove old suite, fit new WC, basin and shower enclosure</div></td><td class="num">3</td><td class="num">180.00</td><td class="num">540.00</td></tr>
<tr><td><b>Wall tiling</b><div class="desc-sub">Supply and fit ceramic tiles, 12 m² including adhesive and grout</div></td><td class="num">12</td><td class="num">38.00</td><td class="num">456.00</td></tr>
<tr><td><b>Plumbing materials</b><div class="desc-sub">Pipework, fittings, isolation valves</div></td><td class="num">1</td><td class="num">145.50</td><td class="num">145.50</td></tr>
<tr><td><b>Waste removal</b><div class="desc-sub">Removal and disposal of old bathroom suite and debris</div></td><td class="num">1</td><td class="num">90.00</td><td class="num">90.00</td></tr>
</tbody></table></div>
<div class="totals-wrap"><div class="totals">
  <div class="row sub"><span>Subtotal</span><span>€ 1,231.50</span></div>
  <div class="row sub"><span>IVA (21%)</span><span>€ 258.62</span></div>
  <div class="row grand"><span>Total</span><span><span class="cur">€</span> 1,490.12</span></div>
  <div class="deposit">Deposit received (50%): <b>€ 745.06</b><br><span style="font-weight:600">Balance due: € 745.06</span></div>
</div></div>
<div class="notes">
  <div class="col"><h4>Payment Details</h4><p><b style="color:var(--ink)">Bank transfer:</b> [IBAN]<br>
  <b style="color:var(--ink)">Account holder:</b> [Account holder name]<br>
  <b style="color:var(--ink)">Bizum:</b> {PHONE}<br>Reference: <b style="color:var(--ink)">INV-2026-041</b></p></div>
  <div class="col" style="flex:1.6"><h4>Terms &amp; Conditions</h4><ol>
    <li>A 50% deposit is payable before work commences; the remaining balance is due within 7 days of invoice date unless otherwise agreed in writing.</li>
    <li>Late payments may incur statutory interest and recovery costs under Spanish Law 3/2004 on combating late payment.</li>
    <li>All materials remain the property of Handyman Axarquia until the invoice is paid in full.</li>
    <li>Workmanship is guaranteed for 12 months; materials are covered by the manufacturer's warranty.</li>
    <li>Any queries regarding this invoice must be raised within 7 days of the invoice date.</li></ol></div>
</div>
<div style="height:4mm"></div>""" + doc_foot("Thank you for your business.")

QUOTE_PAGE = doc_head("Sample Quotation — Handyman Axarquia") + \
'<style>.accept{margin:3mm 14mm 0;padding:2.5mm 6mm;background:var(--wash);border:.35mm solid var(--line);border-radius:2mm;display:flex;gap:10mm;align-items:flex-end}.accept .sig{flex:1}.accept .sig .lineblank{border-bottom:.4mm solid var(--ink);height:5mm}.accept .sig label{font-size:7pt;color:var(--muted);letter-spacing:1px;text-transform:uppercase}</style>' + \
'<div class="page">' + DOC_BRAND.replace("__TITLE__", "Quotation") + f"""
<div class="meta">{FROM_BLOCK}
  <div class="block"><h3>Prepared For</h3><div class="big">Sample Client</div>
    <div>Calle Ejemplo 12</div><div>29740 Torre del Mar, Málaga</div></div>
  <div class="block"><h3>Quote Details</h3><dl class="kv">
    <dt>Quote №</dt><dd>Q-2026-042</dd><dt>Date</dt><dd>1 August 2026</dd>
    <dt>Valid until</dt><dd>31 August 2026</dd></dl></div>
</div>
<div class="items" style="padding-top:6mm">
<p style="font-size:9pt;color:var(--muted);margin-bottom:2mm"><b style="color:var(--ink)">Project:</b> Terrace repair, waterproofing and repainting at Calle Ejemplo 12, Torre del Mar.</p>
<table><thead><tr><th style="width:52%">Description</th><th class="num" style="width:12%">Qty</th>
<th class="num" style="width:18%">Unit&nbsp;(€)</th><th class="num" style="width:18%">Amount&nbsp;(€)</th></tr></thead><tbody>
<tr><td><b>Terrace repair — labour</b><div class="desc-sub">Repair cracked terrace surface and re-seal, approx. 20 m²</div></td><td class="num">2</td><td class="num">170.00</td><td class="num">340.00</td></tr>
<tr><td><b>Waterproof coating</b><div class="desc-sub">Supply and apply waterproof membrane coating</div></td><td class="num">20</td><td class="num">14.50</td><td class="num">290.00</td></tr>
<tr><td><b>Painting</b><div class="desc-sub">Two coats exterior masonry paint, walls surrounding terrace</div></td><td class="num">1</td><td class="num">260.00</td><td class="num">260.00</td></tr>
</tbody></table></div>
<div class="totals-wrap"><div class="totals">
  <div class="row sub"><span>Subtotal</span><span>€ 890.00</span></div>
  <div class="row sub"><span>IVA (21%)</span><span>€ 186.90</span></div>
  <div class="row grand"><span>Total</span><span><span class="cur">€</span> 1,076.90</span></div>
  <div class="deposit"><b>50% deposit to commence work: € 538.45</b><br>Balance of € 538.45 due on completion.</div>
</div></div>
<div class="notes">
  <div class="col" style="flex:1.7"><h4>Terms &amp; Conditions</h4><ol>
    <li>This quotation is valid for 30 days from the date shown above.</li>
    <li>A 50% deposit is required to confirm the booking and schedule the work; the balance is due on completion.</li>
    <li>Additional work, or unforeseen conditions discovered once work begins, will be quoted separately and agreed in writing before proceeding.</li>
    <li>Where provisional sums are shown for materials, final costs are confirmed with receipts.</li>
    <li>Workmanship is guaranteed for 12 months; materials carry the manufacturer's warranty.</li>
    <li>Prices shown exclude any fees, permits or community approvals unless expressly included.</li></ol></div>
  <div class="col"><h4>How to Accept</h4><p>Sign below, or reply by email/WhatsApp quoting <b style="color:var(--ink)">Q-2026-042</b>, then pay the 50% deposit (bank transfer or Bizum: <b style="color:var(--ink)">{PHONE}</b>). Work is scheduled on receipt of the deposit.</p></div>
</div>
<div class="accept">
  <div class="sig"><div class="lineblank"></div><label>Client signature</label></div>
  <div class="sig"><div class="lineblank"></div><label>Print name</label></div>
  <div class="sig" style="max-width:35mm"><div class="lineblank"></div><label>Date</label></div>
</div>""" + doc_foot("No obligation · Free estimates")

LETTERHEAD_PAGE = doc_head("Letterhead — Handyman Axarquia") + \
'<style>.letter-body{flex:1;padding:12mm 20mm 10mm;font-size:10pt}.side-accent{position:absolute;left:0;top:60mm;bottom:60mm;width:1.6mm;background:linear-gradient(180deg,var(--orange),rgba(251,169,23,.15))}</style>' + \
'<div class="page"><div class="side-accent"></div>' + \
DOC_BRAND.replace("__TITLE__", "").replace('<div class="doc-title"><h1></h1><span class="accent"></span></div>',
  f'<div class="doc-title" style="text-align:right;font-size:8pt;color:#B9B9BE;line-height:1.7">{ADDR1}<br>{ADDR2}<br>NIF/CIF: [NIF/CIF]</div>') + \
'<div class="letter-body"></div>' + doc_foot("Handyman Axarquia")

# ---------------------------------------------------------------- cards & shirts

def scaled_page(title, inner_w, inner_h, inner_html, extra_css=""):
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>{FONT_LINK}
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#3a3a3e; font-family:'Poppins',sans-serif; min-height:100vh;
  display:flex; align-items:center; justify-content:center; overflow:auto; }}
.stage {{ width:{inner_w}px; height:{inner_h}px; flex:0 0 auto;
  transform-origin:center center; box-shadow:0 14px 50px rgba(0,0,0,.5); border-radius:18px; overflow:hidden; }}
@media (max-width:{inner_w + 60}px) {{ .stage {{ transform:scale(calc((100vw - 40px) / {inner_w})); }} }}
{extra_css}
</style></head><body><div class="stage">{inner_html}</div></body></html>"""

CARD_FRONT_INNER = """<div style="width:100%;height:100%;background:#0B0B0C;display:flex;align-items:center;justify-content:center">
<div style="text-align:center">
  <img src="/images/logo_mark.svg" alt="" style="width:240px;display:block;margin:0 auto 26px">
  <div style="color:#fff;font-size:30px;font-weight:700;letter-spacing:6px">HANDYMAN <span style="color:#FBA917">AXARQUIA</span></div>
  <div style="color:#7C7C82;font-size:12.5px;letter-spacing:5px;text-transform:uppercase;margin-top:10px">Property Care · Repairs · Renovations</div>
</div></div>"""

CARD_BACK_INNER = f"""<div style="width:100%;height:100%;background:#0B0B0C;color:#fff;position:relative;display:flex">
<div style="position:absolute;left:0;top:0;bottom:0;width:10px;background:#FBA917"></div>
<div style="flex:1;padding:60px 30px 60px 72px;display:flex;flex-direction:column;justify-content:center;gap:26px">
""" + "".join(f"""<div style="display:flex;align-items:center;gap:20px">
  <div style="width:52px;height:52px;border-radius:14px;background:rgba(251,169,23,.12);border:1.5px solid rgba(251,169,23,.55);display:flex;align-items:center;justify-content:center;color:#FBA917;font-size:24px">{ico}</div>
  <div><div style="font-size:11.5px;letter-spacing:3px;text-transform:uppercase;color:#7C7C82">{label}</div>
  <div style="font-size:{sz}px;font-weight:500;margin-top:2px">{val}</div></div></div>"""
  for ico, label, val, sz in [
      ("✆", "Call / WhatsApp", PHONE, 23),
      ("✉", "Email", EMAIL, 23),
      ("⌂", "Web", WEB, 23),
      ("◈", "Based in", f"{ADDR1}<br>29749 Málaga", 19)]) + f"""
</div>
<div style="width:330px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;background:#121214;border-left:1px solid #232326">
  <div style="background:#fff;padding:14px;border-radius:18px"><img src="/images/qr_vcard.png" alt="vCard QR" style="width:200px;height:200px;display:block"></div>
  <div style="color:#FBA917;font-size:12.5px;letter-spacing:3.5px;text-transform:uppercase;font-weight:600;text-align:center">Scan to save contact<br>
  <span style="color:#7C7C82;letter-spacing:1.5px;text-transform:none;font-size:11.5px;font-weight:400">Adds Handyman Axarquia to your phone</span></div>
</div></div>"""

TSHIRT_FRONT_INNER = """<div style="width:100%;height:100%;background:radial-gradient(600px 400px at 50% 30%, #1a1a1e, #0B0B0C);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:34px">
  <img src="/images/logo_mark.svg" alt="HA" style="width:270px">
  <div style="color:#5A5A5F;font-size:13px;letter-spacing:3px;text-transform:uppercase">Front — left chest 9 cm · large print 25 cm</div>
</div>"""

TSHIRT_BACK_INNER = f"""<div style="width:100%;height:100%;background:radial-gradient(600px 400px at 50% 30%, #1a1a1e, #0B0B0C);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:26px">
  <div style="font-size:52px;font-weight:700;letter-spacing:8px;white-space:nowrap"><span style="color:#fff">HANDYMAN</span> <span style="color:#FBA917">AXARQUIA</span></div>
  <div style="color:#FBA917;font-size:21px;letter-spacing:5px">{PHONE} &nbsp;·&nbsp; <span style="color:#fff">{WEB}</span></div>
  <div style="color:#5A5A5F;font-size:13px;letter-spacing:3px;text-transform:uppercase;margin-top:12px">Back — 30 cm across the shoulders · DTF transfer</div>
</div>"""

# ---------------------------------------------------------------- presupuesto

PRICE_ITEMS = [
    ("Logo refinement & vectorisation", "Clean print-ready master vector rebuilt from original artwork; scalable to any size", 150),
    ("Business stationery system", "Invoice, quotation and letterhead templates with 21% IVA handling, 50% deposit terms and standard disclaimers", 300),
    ("Business card design", "Front and back design with vCard QR code, print-ready files (85×55 mm)", 150),
    ("Website design & build", "18-page bilingual (English + Swedish) static website: 6 dedicated service pages, gallery, contact; mobile-first, hosting-ready, no CMS licence costs", 1800),
    ("On-page SEO", "Keyword-targeted titles and metas per page, LocalBusiness + FAQ structured data, XML sitemap, hreflang, robots, town targeting", 450),
    ("Content creation", "≈9,000 words of professional copywriting across both languages, including 24 SEO FAQ answers", 750),
    ("Interactive before/after gallery", "Drag-to-compare slider showcasing real projects, branded handle", 150),
    ("Merchandise artwork", "T-shirt front and back print files (DTF-ready, 300 DPI transparent) in three sizes", 150),
    ("Google setup", "Search Console verification, sitemap submission, Google Business Profile creation and optimisation", 200),
]

def presupuesto_page():
    rows = "".join(
        f'<tr><td><b>{t}</b><div class="desc-sub">{d}</div></td><td class="num">{p:,.2f}</td></tr>'
        for t, d, p in PRICE_ITEMS)
    total = sum(p for _, _, p in PRICE_ITEMS)
    return doc_head("Presupuesto — Marketing Bundle") + '<div class="page">' + \
    DOC_BRAND.replace("__TITLE__", "Presupuesto") + f"""
<div class="meta">
  <div class="block"><h3>Prepared For</h3><div class="big">Handyman Axarquia</div>
    <div>{ADDR1}</div><div>{ADDR2}</div></div>
  <div class="block"><h3>Bundle</h3><div class="big">Complete marketing pack</div>
    <div style="color:var(--muted)">Brand · Stationery · Website · SEO · Merch</div></div>
  <div class="block"><h3>Details</h3><dl class="kv">
    <dt>Reference</dt><dd>PACK-2026-001</dd><dt>Date</dt><dd>August 2026</dd>
    <dt>Pricing basis</dt><dd>Standard market rates</dd></dl></div>
</div>
<div class="items" style="padding-top:6mm">
<table><thead><tr><th style="width:82%">Item</th><th class="num" style="width:18%">Market&nbsp;rate&nbsp;(€)</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<div class="totals-wrap"><div class="totals">
  <div class="row grand"><span>Bundle value</span><span><span class="cur">€</span> {total:,.2f}</span></div>
</div></div>
<div class="notes"><div class="col"><h4>Notes</h4>
<p>Prices shown are indicative standard market rates for equivalent work commissioned separately from Spanish/EU freelance designers and agencies (excl. IVA). Hosting for the static website is available free (GitHub Pages / Cloudflare Pages) or from ~€5/month on conventional hosting; the site has no CMS licence or plugin costs. Domain renewal, photography and paid advertising are not included.</p></div></div>
<div style="height:4mm"></div>""" + doc_foot("Complete marketing bundle")

# ---------------------------------------------------------------- hub

ASSETS = [
    ("presupuesto", "💶 Presupuesto — full bundle", "/brand/presupuesto/"),
    ("website", "🌐 Website (live)", "/"),
    ("invoice", "📄 Invoice", "/brand/invoice/"),
    ("quotation", "📄 Quotation", "/brand/quotation/"),
    ("letterhead", "📄 Letterhead", "/brand/letterhead/"),
    ("card-front", "💳 Business card — front", "/brand/card-front/"),
    ("card-back", "💳 Business card — back", "/brand/card-back/"),
    ("tshirt-front", "👕 T-shirt — front", "/brand/tshirt-front/"),
    ("tshirt-back", "👕 T-shirt — back", "/brand/tshirt-back/"),
]

def hub_page():
    opts = "".join(f'<option value="{u}">{label}</option>' for _, label, u in ASSETS)
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Marketing Pack — Handyman Axarquia</title>{FONT_LINK}
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:'Poppins',sans-serif; height:100vh; display:flex; flex-direction:column; background:#232326; }}
.adminbar {{ background:#0B0B0C; border-bottom:3px solid #FBA917; color:#fff;
  display:flex; align-items:center; gap:16px; padding:10px 18px; flex-wrap:wrap; }}
.adminbar img {{ width:34px; height:34px; }}
.adminbar b {{ font-size:.95rem; letter-spacing:.5px; }}
.adminbar b span {{ color:#FBA917; }}
.adminbar .tag {{ color:#8E8E93; font-size:.72rem; letter-spacing:2px; text-transform:uppercase; }}
.adminbar select {{ background:#1c1c1f; color:#fff; border:1px solid #3a3a3e; border-radius:8px;
  padding:8px 12px; font-size:14px; font-family:inherit; min-width:260px; }}
.adminbar .actions {{ margin-left:auto; display:flex; gap:8px; }}
.adminbar button, .adminbar a.btn {{ background:#1c1c1f; color:#d6d6da; border:1px solid #3a3a3e;
  border-radius:8px; padding:7px 14px; cursor:pointer; font-size:12.5px; font-family:inherit; text-decoration:none; }}
.adminbar button:hover, .adminbar a.btn:hover {{ border-color:#FBA917; color:#FBA917; }}
iframe {{ border:0; flex:1; width:100%; background:#fff; }}
</style></head><body>
<div class="adminbar">
  <img src="/images/logo.png" alt="">
  <div><b>HANDYMAN <span>AXARQUIA</span></b><div class="tag">Marketing pack</div></div>
  <select id="sel" onchange="go(this.value)">{opts}</select>
  <div class="actions">
    <a class="btn" id="open" href="/brand/presupuesto/" target="_blank">Open full ↗</a>
    <button onclick="document.getElementById('fr').contentWindow.print()">Print / Save PDF</button>
  </div>
</div>
<iframe id="fr" src="/brand/presupuesto/"></iframe>
<script>
function go(u) {{
  document.getElementById('fr').src = u;
  document.getElementById('open').href = u;
}}
</script>
</body></html>"""

# ---------------------------------------------------------------- build

def _decode(site, name, out):
    b64 = ROOT / "assets_b64" / name
    if b64.exists():
        try:
            (site / "images" / out).write_bytes(base64.b64decode(b64.read_text()))
        except Exception:
            pass

def build(site: Path):
    (site / "images").mkdir(parents=True, exist_ok=True)
    pages = {
        "brand": hub_page(),
        "brand/presupuesto": presupuesto_page(),
        "brand/invoice": INVOICE_PAGE,
        "brand/quotation": QUOTE_PAGE,
        "brand/letterhead": LETTERHEAD_PAGE,
        "brand/card-front": scaled_page("Business card — front", 1004, 650, CARD_FRONT_INNER),
        "brand/card-back": scaled_page("Business card — back", 1004, 650, CARD_BACK_INNER),
        "brand/tshirt-front": scaled_page("T-shirt — front", 1004, 700, TSHIRT_FRONT_INNER),
        "brand/tshirt-back": scaled_page("T-shirt — back", 1100, 700, TSHIRT_BACK_INNER),
    }
    for rel, html in pages.items():
        d = site / rel
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(html)
    print(f"brand pack: {len(pages)} pages")

if __name__ == "__main__":
    build(ROOT / "site")
