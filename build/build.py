import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import HOMES, PEOPLE, POSTS, QUOTES, FAQ, PRIVACY, TERMS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
money = lambda n: '${:,}'.format(n)
A = '<i>→</i>'

def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0A3B25">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
<script>try{{if(localStorage.getItem('acre.night')==='1')document.documentElement.classList.add('night');if(!sessionStorage.getItem('acre.loaded'))document.documentElement.classList.add('loading')}}catch(e){{}}</script>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
 <symbol id="mark" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="square"><rect x="1.5" y="1.5" width="29" height="29" rx="1"/><path d="M7 25 16 7l9 18"/><path d="M10.6 17.8h10.8M12.2 21.4h7.6M13.6 25h4.8"/></symbol>
 <symbol id="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></symbol>
 <symbol id="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></symbol>
 <symbol id="plus" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></symbol>
</svg>
<div class="loader" id="loader" aria-hidden="true"><div class="lw">{''.join(f'<span style="--d:{i}">{c}</span>' for i,c in enumerate('ACRE'))}</div><div class="lbar"><i id="lbar"></i></div><div class="lnum" id="lnum">0</div></div>
'''

def nav(light=False):
    links = [('Residences','/residences'),('Advisors','/advisors'),('About','/about'),('Journal','/journal'),('Contact','/contact')]
    return f'''<header class="nav{' lightnav' if light else ''}" id="nav">
 <div class="wrap">
  <a href="/" class="logo" aria-label="Acre home"><svg><use href="#mark"/></svg>ACRE</a>
  <nav class="links">{''.join(f'<a href="{u}">{t}</a>' for t,u in links)}</nav>
  <div class="r"><button class="mode" id="mode" aria-label="Switch light and dark"><svg><use href="#moon"/></svg></button><a class="btn" href="/contact">Private viewing</a><button class="burger" id="burger" aria-label="Menu"><i></i><i></i></button></div>
 </div>
</header>
<div class="menu" id="menu">
 <nav>{''.join(f'<a class="l" href="{u}" style="--i:{i}"><span>{t}</span><em>0{i+1}</em></a>' for i,(t,u) in enumerate(links))}</nav>
 <a class="btn btn-c mb" href="/contact">Private viewing</a>
</div>
'''

CTA = f'''<section class="cta">
 <img src="/img/cta.jpg" alt="" loading="lazy" class="px">
 <div class="in">
  <span class="eb reveal">Private viewings</span>
  <h2 class="reveal">Ready for your next chapter?</h2>
  <p class="reveal">Tell us what you are looking for and we will pair you with the advisor who knows that place best.</p>
  <div class="reveal"><a class="btn btn-c" href="/contact">Arrange a private viewing {A}</a></div>
 </div>
</section>
'''

FOOT = '''<footer>
 <div class="wrap">
  <div class="fg">
   <div><a href="/" class="logo"><svg><use href="#mark"/></svg>ACRE</a><p>A private brokerage for considered homes. Licensed in nine states.</p></div>
   <div class="col"><h6>EXPLORE</h6><a href="/residences">Residences</a><a href="/advisors">Advisors</a><a href="/about">About</a><a href="/journal">Journal</a></div>
   <div class="col"><h6>CONTACT</h6><a href="mailto:hello@acre.homes">hello@acre.homes</a><a href="tel:+18055550187">+1 (805) 555 0187</a><span>210 East Ojai Avenue, Ojai, CA 93023</span></div>
   <div class="col"><h6>NEVER MISS A RESIDENCE</h6><p>New homes in your inbox before they reach the portals.</p><form class="news" novalidate><label>YOUR EMAIL</label><input type="email" placeholder="you@example.com" aria-label="Your email"><button class="btn">Subscribe <i>→</i></button><div class="fmsg"></div></form></div>
  </div>
  <div class="fb"><div class="l"><span>© 2026 Acre. All rights reserved.</span><a href="/privacy">Privacy</a><a href="/terms">Terms</a></div><span>Designed by <a href="https://elementa-studio.vercel.app" target="_blank" rel="noopener">Elementa Studio</a></span></div>
 </div>
</footer>
<script src="/lenis.min.js"></script>
<script src="/smooth.js"></script>
<script src="/main.js"></script>
</body>
</html>
'''

def page(title, desc, body, cta=True, light=True):
    return head(title, desc) + nav(light) + '<main>' + body + (CTA if cta else '') + '</main>' + FOOT

def card(h):
    return f'''<a class="pc reveal" href="/residences/{h['slug']}" data-type="{h['t'].lower()}" data-city="{h['c']}" data-price="{h['p']}" data-bed="{h['bd']}"><div class="im imr"><img src="/img/{h['img']}.jpg" alt="{h['n']}" loading="lazy"><span class="badge">{h['b']}</span><span class="price">{money(h['p'])}</span></div><span class="ty">{h['t'].upper()}</span><h3>{h['n']}</h3><div class="ad">{h['a']} · {h['c']}, {h['st']}</div><div class="sp">{h['bd']} beds · {h['ba']} baths · {h['sf']:,} sq ft</div></a>'''

def phead(eb, h1, p):
    return f'<section class="phead"><div class="wrap"><span class="eb line reveal">{eb}</span><h1 class="reveal">{h1}</h1><p class="reveal">{p}</p></div></section>'

def adv_card(p):
    return f'<a class="av reveal" href="/advisors/{p["slug"]}"><div class="im imr"><img src="/img/{p["img"]}.jpg" alt="{p["n"]}" loading="lazy"></div><h4>{p["n"]}</h4><small>{p["r"]} · {p["c"]}</small></a>'

def post_card(p):
    return f'<a class="jp reveal" href="/journal/{p["slug"]}"><div class="im imr"><img src="/img/{p["img"]}.jpg" alt="" loading="lazy"></div><span class="eb">{p["cat"]} · {p["m"]}</span><h4>{p["h"]}</h4><p>{p["x"]}</p></a>'

def write(path, html):
    full = os.path.join(ROOT, path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(html)

# ---------- home
feat = [h for h in HOMES if h['featured']]
home = f'''<section class="hero">
 <div class="bgs" id="bgs">{''.join(f'<div class="bg{" on" if i==0 else ""}"><img decoding="async" src="/img/{h["hero"]}.jpg" alt="{h["n"]}" {"fetchpriority=high" if i==0 else "loading=lazy"}></div>' for i,h in enumerate(feat))}</div>
 <div class="wrap">
  <div class="hrow">
   <div>
    <span class="eb hi">Private residences</span>
    <h1 class="hi">Homes with room <br>to breathe.</h1>
    <p class="hi">A private brokerage for considered homes, each one walked, verified and presented by a senior advisor.</p>
    <div class="ctas hi"><a class="btn btn-c" href="/residences">View residences {A}</a><a class="btn btn-o" href="/contact">Private viewing</a></div>
   </div>
   <a class="feat hi" id="feat" href="/residences/{feat[0]['slug']}">
    <div class="top"><span>NOW PRESENTING</span><span>FEATURED</span></div>
    <div class="ftxt" id="ftxt"><h3 id="fName">{feat[0]['n']}</h3><small id="fAddr">{feat[0]['a']}, {feat[0]['c']}, {feat[0]['st']}</small><div class="pr"><b id="fPrice">{money(feat[0]['p'])}</b><span class="tl">View {A}</span></div></div>
    <div class="segs" id="segs">{''.join(f'<button aria-label="Residence {i+1}" data-slug="{h["slug"]}" data-n="{h["n"]}" data-a="{h["a"]}, {h["c"]}, {h["st"]}" data-p="{money(h["p"])}"><i></i></button>' for i,h in enumerate(feat))}</div>
   </a>
  </div>
  <form class="search hi" id="search" action="/residences">
   <div class="sf"><label for="sLoc">LOCATION</label><select id="sLoc" name="loc"><option value="">All locations</option>{''.join(f'<option>{c}</option>' for c in sorted({h['c'] for h in HOMES}))}</select></div>
   <div class="sf"><label for="sType">PROPERTY TYPE</label><select id="sType" name="type"><option value="">All types</option><option value="estate">Estate</option><option value="modern">Modern</option><option value="waterfront">Waterfront</option><option value="family">Family</option></select></div>
   <div class="sf"><label for="sPrice">PRICE RANGE</label><select id="sPrice" name="price"><option value="">Any price</option><option value="0-1200000">Under $1.2m</option><option value="1200000-2000000">$1.2m to $2m</option><option value="2000000-99999999">$2m +</option></select></div>
   <div class="sf"><label for="sBed">BEDROOMS</label><select id="sBed" name="bed"><option value="">Any</option><option value="3">3+</option><option value="4">4+</option><option value="5">5+</option></select></div>
   <button class="btn" type="submit">Search {A}</button>
  </form>
 </div>
</section>
<div class="tick" aria-hidden="true"><div class="row">{''.join(f'<span>{t}</span>' for t in ['New this week','Waterfront','Architect led','Move in ready','Off market','Historic homes']*2)}</div></div>
<section class="sec">
 <div class="wrap">
  <div class="shead"><div><span class="eb reveal">Featured residences</span><h2 class="reveal">Chosen by hand, not by feed</h2></div><p class="reveal">A short list our advisors walked through this month. No syndicated listings, no tired photographs.</p></div>
  <div class="cards">{''.join(card(h) for h in feat)}</div>
  <div class="below"><a class="tl reveal" href="/residences">View all residences {A}</a></div>
 </div>
</section>
<section class="about">
 <div class="im"><img src="/img/about.jpg" alt="Soft beige hallway with a curved staircase" loading="lazy"></div>
 <div class="box"><div class="inner reveal">
  <span class="eb">About Acre</span>
  <blockquote id="quote">We work with people who care how they will live, not only what they will spend. Fewer listings, longer conversations, and the honesty to tell you when a house is wrong.</blockquote>
  <div class="trio">
   <div><i>01</i><b>Design led search</b><p>We begin with how you want to live, then find the homes that fit, not the other way round.</p></div>
   <div><i>02</i><b>Structure and survey</b><p>Every home is read by someone who knows what a hairline crack is telling them.</p></div>
   <div><i>03</i><b>Energy and longevity</b><p>Running costs and retrofit potential are on the table before you ever commit.</p></div>
  </div>
 </div></div>
</section>
STATS
<section class="sec">
 <div class="wrap">
  <div class="shead"><div><span class="eb reveal">What else we do</span><h2 class="reveal">Support beyond the sale</h2></div></div>
  <div class="svc">
   <a class="sv reveal" href="/contact"><img src="/img/s1.jpg" alt="" loading="lazy"><h3>Mortgage and finance</h3><div><p>Introductions to lenders who understand architect designed and unusual homes.</p><span class="btn btn-c">Learn more {A}</span></div></a>
   <a class="sv reveal" href="/contact"><img src="/img/s2.jpg" alt="" loading="lazy"><h3>Property management</h3><div><p>Quiet, careful care for owners who spend part of the year somewhere else.</p><span class="btn btn-c">Learn more {A}</span></div></a>
   <a class="sv reveal" href="/contact"><img src="/img/s3.jpg" alt="" loading="lazy"><h3>Renovation and design</h3><div><p>Architects and builders we have trusted for years, briefed before you buy.</p><span class="btn btn-c">Learn more {A}</span></div></a>
  </div>
 </div>
</section>
<div class="wrap"><div class="rule"></div></div>
<section style="padding-bottom:120px">
 <div class="wrap">
  <div class="shead"><div><span class="eb reveal">Our advisors</span><h2 class="reveal">The people behind every introduction</h2></div><p class="reveal">Four senior advisors, four markets, one standard of care.</p></div>
  <div class="advs">{''.join(adv_card(p) for p in PEOPLE)}</div>
  <div class="below"><a class="tl reveal" href="/advisors">Meet all advisors {A}</a></div>
 </div>
</section>
<section class="tst">
 <div class="wrap">
  <div class="stars">★★★★★</div>
  <blockquote id="tq">“{QUOTES[0][0]}”</blockquote>
  <div class="who" id="tw">{QUOTES[0][1]}<small>{QUOTES[0][2]}</small></div>
  <div class="dots" id="tdots">{''.join(f'<button aria-label="Quote {i+1}" data-q="{q[0]}" data-w="{q[1]}" data-s="{q[2]}"></button>' for i,q in enumerate(QUOTES))}</div>
 </div>
</section>
<section class="sec">
 <div class="wrap">
  <div class="shead"><div><span class="eb reveal">The journal</span><h2 class="reveal">Notes for buyers and sellers</h2></div><p class="reveal">Written by the advisors doing the work, not by a content team.</p></div>
  <div class="jr">{''.join(post_card(p) for p in POSTS)}</div>
  <div class="below"><a class="tl reveal" href="/journal">Read the journal {A}</a></div>
 </div>
</section>
'''
STATS = '''<section class="stats"><div class="wrap">
  <div class="reveal"><b><span data-count="980">0</span>+</b><em>RESIDENCES PLACED</em></div>
  <div class="reveal"><b data-count="18">0</b><em>YEARS IN PRACTICE</em></div>
  <div class="reveal"><b data-count="9">0</b><em>STATES LICENSED</em></div>
  <div class="reveal"><b><span data-count="32">0</span>+</b><em>SENIOR ADVISORS</em></div>
</div></section>'''
home = home.replace('STATS', STATS)
write('index.html', page('Acre · Homes with room to breathe', 'A private brokerage for considered homes. Every residence walked, verified and presented by a senior advisor.', home, light=False))

# ---------- residences
chips = ['All','Estate','Modern','Waterfront','Family']
res = phead('Residences', 'Every home on our books.', 'Every residence we currently represent, each one walked, photographed and priced by the advisor who knows it best.') + f'''
<section class="sec tight"><div class="wrap">
 <div class="chips" id="chips">{''.join(f'<button class="{"on" if c=="All" else ""}" data-f="{"" if c=="All" else c.lower()}">{c}</button>' for c in chips)}</div>
 <div class="cards" id="cards">{''.join(card(h) for h in HOMES)}<div class="none" id="none">No residences match that search right now. Try widening it, or ask an advisor about homes not yet listed.</div></div>
</div></section>'''
write('residences.html', page('Residences · Acre', 'Every residence Acre currently represents.', res))

# ---------- residence detail
for h in HOMES:
    adv = PEOPLE[h['adv']]
    body = f'''<section class="det"><div class="wrap">
 <a class="back reveal" href="/residences">← All residences</a>
 <div class="dtop"><div><span class="eb reveal">{h['b']}</span><h1 class="reveal">{h['n']}</h1><span class="addr reveal">{h['a']} · {h['c']}, {h['st']}</span></div><div class="dpr reveal"><span class="eb">ASKING PRICE</span><b>{money(h['p'])}</b></div></div>
 <div class="dimg imr reveal"><img src="/img/{h['img']}.jpg" alt="{h['n']}"></div>
 <div class="dgrid">
  <div>
   <span class="eb reveal">The residence</span>
   <p class="dlead reveal">{h['lead']}</p>
   <div class="facts reveal"><div><span>BEDROOMS</span><b>{h['bd']}</b></div><div><span>BATHROOMS</span><b>{h['ba']}</b></div><div><span>INTERIOR</span><b>{h['sf']:,} sq ft</b></div><div><span>LOT</span><b>{h['lot']}</b></div><div><span>YEAR BUILT</span><b>{h['yr']}</b></div></div>
   <span class="eb reveal">About this home</span>
   {''.join(f'<p class="dtxt reveal">{t}</p>' for t in h['d'])}
   <span class="eb reveal">Highlights</span>
   <ul class="hl reveal">{''.join(f'<li>{x}</li>' for x in h['hl'])}</ul>
  </div>
  <aside class="enq reveal">
   <span class="eb">Your advisor</span>
   <a class="who" href="/advisors/{adv['slug']}"><img src="/img/{adv['img']}.jpg" alt="{adv['n']}"><div><b>{adv['n']}</b><small>{adv['r']}</small></div></a>
   <h4>Arrange a private viewing</h4>
   <p>Tell us when suits you. Your advisor replies within one business day.</p>
   <form class="cform" novalidate><label class="fld"><span>FULL NAME</span><input name="n" placeholder="Jane Smith" autocomplete="name"></label><label class="fld"><span>EMAIL</span><input name="e" type="email" placeholder="you@example.com" autocomplete="email"></label><input type="hidden" name="h" value="{h['n']}"><div class="err"></div><button class="btn btn-d">Send enquiry</button></form>
   <div class="okmsg"><b>Thank you.</b><span>{adv['n'].split()[0]} will be in touch within one business day.</span></div>
  </aside>
 </div>
 <div class="gal"><div class="imr reveal"><img src="/img/{h['img']}a.jpg" alt="" loading="lazy"></div><div class="imr reveal"><img src="/img/{h['img']}b.jpg" alt="" loading="lazy"></div></div>
</div></section>'''
    write(f'residences/{h["slug"]}.html', page(f'{h["n"]} · {h["c"]}, {h["st"]} | Acre', h['lead'], body, cta=False))

# ---------- advisors
advs = phead('Advisors', 'The people behind<br>every private viewing.', 'Senior advisors, each with a single market they know street by street. Every one has closed at least fifty homes before carrying a residence on their own.') + f'<section class="sec tight"><div class="wrap"><div class="advs">{"".join(adv_card(p) for p in PEOPLE)}</div></div></section>'
write('advisors.html', page('Advisors · Acre', 'Meet the senior advisors at Acre.', advs))
for i, p in enumerate(PEOPLE):
    nx = PEOPLE[(i + 1) % len(PEOPLE)]
    body = f'''<section class="advd"><div class="wrap">
 <div class="ph imr reveal"><img src="/img/{p['img']}.jpg" alt="{p['n']}"></div>
 <div class="ab">
  <a class="back reveal" href="/advisors">← All advisors</a>
  <span class="eb reveal">{p['r'].upper()} · {p['c'].upper()}</span>
  <h1 class="reveal">{p['n']}</h1>
  {''.join(f'<p class="reveal">{t}</p>' for t in p['bio'])}
  <div class="kv reveal"><div><span>LANGUAGES</span>{p['lang']}</div><div><span>WITH ACRE SINCE</span>{p['since']}</div><div><span>EMAIL</span><a href="mailto:{p['email']}">{p['email']}</a></div><div><span>PHONE</span><a href="tel:{p['phone'].replace(' ','').replace('(','').replace(')','')}">{p['phone']}</a></div></div>
  <a class="btn btn-d reveal" href="/contact">Arrange a viewing {A}</a>
  <a class="tl nxt reveal" href="/advisors/{nx['slug']}">{nx['n']} ›</a>
 </div>
</div></section>'''
    write(f'advisors/{p["slug"]}.html', page(f'{p["n"]}, {p["r"]} · Acre', p['bio'][0], body, cta=False))

# ---------- journal
jr = phead('The journal', 'Notes from the<br>market, street by street.', 'Market reports, buying guides and neighbourhood notes, written by the advisors doing the deals.') + f'<section class="sec tight"><div class="wrap"><div class="jr">{"".join(post_card(p) for p in POSTS)}</div></div></section>'
write('journal.html', page('The Journal · Acre', 'Notes for buyers and sellers from the Acre advisors.', jr))
for i, p in enumerate(POSTS):
    nx = POSTS[(i + 1) % len(POSTS)]
    body = f'''<article class="post"><div class="wrap narrow">
 <a class="back reveal" href="/journal">← The journal</a>
 <span class="eb line reveal">{p['cat']} · {p['date'].upper()}</span>
 <h1 class="reveal">{p['h']}</h1>
 <p class="lede reveal">{p['x']}</p>
</div>
<div class="wrap mid"><div class="pimg imr reveal"><img src="/img/{p['img']}.jpg" alt=""></div></div>
<div class="wrap thin">
 {''.join((f'<h2 class="reveal">{t}</h2>' if t else '') + f'<p class="reveal">{b}</p>' for t,b in p['body'])}
 <a class="next reveal" href="/journal/{nx['slug']}"><span class="eb">NEXT STORY</span><b>{nx['h']} ›</b></a>
</div></article>'''
    write(f'journal/{p["slug"]}.html', page(f'{p["h"]} · The Acre Journal', p['x'], body, cta=False))

# ---------- about
about = phead('About', 'A house built the slow way.', 'Acre began with one office, one advisor and a refusal to present a home nobody had stood inside.') + f'''
<section class="sec tight"><div class="wrap">
 <div class="wide imr reveal"><img src="/img/ab1.jpg" alt="A house above the mist in a forest" class="px2"></div>
 <div class="story">
  <div class="imr reveal"><img src="/img/about.jpg" alt="" loading="lazy"></div>
  <div class="items">
   <div class="reveal"><i>01</i><div><b>We started in 2008</b><p>One office above a bakery in Ojai, one advisor, and a rule that has never changed: nobody presents a home they have not walked through themselves. It made us slower than the portals. It also made us right more often.</p></div></div>
   <div class="reveal"><i>02</i><div><b>How we work</b><p>Every residence is checked again each week. Every buyer gets one advisor, not a queue. Every offer is explained in plain language before it is signed, including the parts that are not in your favour.</p></div></div>
   <div class="reveal"><i>03</i><div><b>Where we are going</b><p>Nine states, thirty two advisors, and no ambition to become a portal. We would rather be the brokerage people call back than the one with the most listings.</p></div></div>
  </div>
 </div>
</div></section>
{STATS}
<section class="sec"><div class="wrap">
 <span class="eb reveal">What we hold to</span><h2 class="h2 reveal">Four promises, kept<br>on every home.</h2>
 <div class="promises">
  <div class="reveal"><b>Say the hard thing</b><p>If a home is priced wrong, you hear it from us first.</p></div>
  <div class="reveal"><b>One advisor, start to finish</b><p>No handoffs between departments halfway through.</p></div>
  <div class="reveal"><b>No hidden fees</b><p>Every cost is on the table before you sign anything.</p></div>
  <div class="reveal"><b>An answer within a day</b><p>Calls, emails and messages, one business day, every time.</p></div>
 </div>
</div></section>'''
write('about.html', page('About · Acre', 'How Acre began and how we work.', about))

# ---------- contact
contact = phead('Private viewing', "Let's talk about<br>your next home.", 'Tell us what you are looking for, or what you are hoping to sell, and an advisor will reply within one business day.') + f'''
<section class="sec tight"><div class="wrap cgrid">
 <div>
  <h3 class="cl reveal">One advisor, one conversation.<br>No call centres, no handoffs.</h3>
  <div class="kv reveal"><div><span>STUDIO</span>210 East Ojai Avenue, Ojai, CA 93023</div><div><span>EMAIL</span><a href="mailto:hello@acre.homes">hello@acre.homes</a></div><div><span>PHONE</span><a href="tel:+18055550187">+1 (805) 555 0187</a></div><div><span>HOURS</span>Mon to Fri, 9:00 to 18:00. Saturdays by appointment.</div></div>
  <div class="cimg imr reveal"><img src="/img/ct.jpg" alt="Sunlit dining room" loading="lazy"></div>
 </div>
 <div>
  <div class="enq big reveal">
   <h4>Arrange a private viewing</h4>
   <p>Share a few details and the right advisor will reply within one business day.</p>
   <form class="cform" novalidate>
    <label class="fld"><span>FULL NAME</span><input name="n" placeholder="Jane Smith" autocomplete="name"></label>
    <label class="fld"><span>EMAIL</span><input name="e" type="email" placeholder="you@example.com" autocomplete="email"></label>
    <label class="fld"><span>INTERESTED IN</span><select name="h"><option value="">Select…</option>{''.join(f'<option>{h["n"]}, {h["c"]}</option>' for h in HOMES)}<option>Selling my home</option><option>Something not listed yet</option></select></label>
    <label class="fld"><span>MESSAGE</span><textarea name="m" placeholder="Timing, must haves, questions"></textarea></label>
    <div class="err"></div><button class="btn btn-d">Send enquiry</button>
   </form>
   <div class="okmsg"><b>Thank you.</b><span>The right advisor will be in touch within one business day.</span></div>
  </div>
  <h3 class="cl small reveal">Common questions</h3>
  <div class="faq reveal">{''.join(f'<div class="qa"><button aria-expanded="false">{q}<svg><use href="#plus"/></svg></button><div class="ans"><div><p>{a}</p></div></div></div>' for q,a in FAQ)}</div>
 </div>
</div></section>'''
write('contact.html', page('Private viewing · Acre', 'Arrange a private viewing with an Acre advisor.', contact, cta=False))

# ---------- legal
def legal(slug, title, sub, items):
    body = phead('Legal', title, sub) + f'''<section class="sec tight"><div class="wrap lgrid">
 <div class="ltext">{''.join(f'<h3 class="reveal">{i+1}. {t}</h3><p class="reveal">{b}</p>' for i,(t,b) in enumerate(items))}</div>
 <aside class="lside reveal"><span class="eb">LAST UPDATED</span><b>28 September 2026</b><span class="eb">SOMETHING UNCLEAR?</span><p>Write to us and a person will answer. We do not use a ticketing system for this.</p><a class="btn btn-d" href="/contact">Contact us {A}</a></aside>
</div></section>'''
    write(f'{slug}.html', page(f'{title} · Acre', sub, body, cta=False))
legal('privacy', 'Privacy notice', 'What we collect when you use this site or enquire about a residence, why we hold it, and how to make us stop.', PRIVACY)
legal('terms', 'Terms of service', 'The terms that apply when you browse this site or send us an enquiry.', TERMS)
print('built')
