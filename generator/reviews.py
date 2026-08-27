# Customer reviews section (shown on the home and gallery pages).
# Static copies of real Google / Facebook reviews with links to the live sources.

GOOGLE_REVIEWS_URL = "https://search.google.com/local/reviews?placeid=ChIJ781fzipHcg0R-T6XK73cOTs"
FACEBOOK_URL = "https://www.facebook.com/handymanaxarquia"
FACEBOOK_REVIEWS_URL = "https://www.facebook.com/handymanaxarquia/reviews"

FB_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M24 12.073C24 5.405 18.627 0 12 0S0 5.405 0 12.073C0 18.1 4.388 23.094 10.125 24v-8.437H7.078v-3.49h3.047v-2.66c0-3.026 1.792-4.697 4.533-4.697 1.313 0 2.686.236 2.686.236v2.971H15.83c-1.491 0-1.956.931-1.956 1.886v2.264h3.328l-.532 3.49h-2.796V24C19.612 23.094 24 18.1 24 12.073z"/></svg>'
G_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M23.49 12.27c0-.79-.07-1.54-.19-2.27H12v4.51h6.47c-.29 1.48-1.14 2.73-2.4 3.58v3h3.86c2.26-2.09 3.56-5.17 3.56-8.82z"/><path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.86-3c-1.08.72-2.45 1.16-4.07 1.16-3.13 0-5.78-2.11-6.73-4.96H1.29v3.09C3.26 21.3 7.31 24 12 24z"/><path fill="#FBBC05" d="M5.27 14.29c-.25-.72-.38-1.49-.38-2.29s.14-1.57.38-2.29V6.62H1.29C.47 8.24 0 10.06 0 12s.47 3.76 1.29 5.38l3.98-3.09z"/><path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.31 0 3.26 2.7 1.29 6.62l3.98 3.09C6.22 6.86 8.87 4.75 12 4.75z"/></svg>'

_STARS = '<span class="rv-stars">★★★★★</span>'

REVIEWS = [
    ("Lars Behrendt-Green", "Google & Facebook",
     "Nick and his team recently renovated our patio and we are absolutely thrilled with the results. Nick is reliable, conscientious, hard working, professional, always cheerful and much more. One of the best things was the communication — during the job we received photos and messages on a daily basis. The result of this project is truly stunning, we couldn't be happier."),
    ("Penelope Jones", "Google",
     "Nick has succeeded in fixing some problems with my roof terrace, where others have failed, and has completely transformed the whole area into a lovely place to sit and enjoy the views. His work is top quality, and he has always been punctual and tidy, and done everything with very good humour."),
    ("Arturo", "Google",
     "Handyman Axarquia provided me with excellent support during various renovation projects at my cortijo (painting, carpentry, plumbing, electrical work, insect screens, etc.). All jobs were completed to my complete satisfaction in terms of quality, deadlines, and cost. I can recommend him without reservation."),
    ("SY OntheGo", "Google",
     "Nick and his team worked on a larger project for us. His excellent organization and communication skills made it a pleasure to work with him and his team. He communicated very timely, and always kept us informed throughout all steps of the work. We can highly recommend him!"),
    ("Alan, Torrox Campo", "Google",
     "A tricky job well done by a very polite and conscientious professional. This review is to thank Nick for the professional job he did on our swimming pool. Despite encountering complications mid-way, Nick's experience and knowledge quickly resolved the problem. Very satisfied with the work and will undoubtedly call on him again in the future."),
    ("Sarah Hermitage", "Google",
     "Much more than a handyman. Great builder. Honest and reliable. Listens to what you want and does it to the best of his abilities. Always happy and doesn't rip you off."),
]

STYLE = """<style>
.rv-badges { display: flex; flex-wrap: wrap; gap: 14px; justify-content: center; margin: 4px 0 30px; }
.rv-badge { display: inline-flex; align-items: center; gap: 10px; background: #fff; border: 1px solid var(--line);
  border-radius: 999px; padding: 10px 20px; font-size: .9rem; font-weight: 600; color: inherit; text-decoration: none; }
.rv-badge svg { width: 20px; height: 20px; flex: none; }
.rv-badge .rv-stars { letter-spacing: 2px; }
.rv-badge:hover { border-color: var(--orange); }
.rv-stars { color: var(--orange); }
.rv-card { background: #fff; border: 1px solid var(--line); border-radius: var(--radius); padding: 22px; display: flex; flex-direction: column; gap: 10px; }
.rv-card p { font-size: .9rem; line-height: 1.6; flex: 1; }
.rv-meta { display: flex; align-items: baseline; justify-content: space-between; gap: 10px; font-size: .82rem; }
.rv-meta b { font-weight: 600; }
.rv-meta span { color: #8E8E93; }
</style>"""


def reviews_html(lang, ui):
    en = lang == "en"
    kicker = "Reviews" if en else "Omdömen"
    title = "What our customers say" if en else "Vad våra kunder säger"
    sub = ("Real reviews from Google and Facebook — tap through to read them all."
           if en else
           "Riktiga omdömen från Google och Facebook (på engelska) — klicka vidare för att läsa alla.")
    g_label = "5.0 on Google · 11 reviews" if en else "5,0 på Google · 11 omdömen"
    f_label = "Recommended on Facebook" if en else "Rekommenderad på Facebook"
    cards = "".join(f"""<div class="rv-card">
      {_STARS}
      <p>“{text}”</p>
      <div class="rv-meta"><b>{name}</b><span>{src}</span></div>
    </div>""" for name, src, text in REVIEWS)
    return f"""{STYLE}<section class="alt"><div class="container">
  <div class="sec-head">
    <div class="kicker">{kicker}</div>
    <h2>{title}</h2>
    <p>{sub}</p>
  </div>
  <div class="rv-badges">
    <a class="rv-badge" href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">{G_SVG} <span>{g_label}</span> {_STARS}</a>
    <a class="rv-badge" href="{FACEBOOK_REVIEWS_URL}" target="_blank" rel="noopener" style="color:#1877F2">{FB_SVG} <span style="color:var(--black)">{f_label}</span></a>
  </div>
  <div class="grid c3">{cards}</div>
</div></section>"""
