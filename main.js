(() => {
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const money = n => '$' + n.toLocaleString('en-US');

/* data */
const homes = [
 { n: 'Cielo House', a: '4 Sierra Vista Lane', c: 'Ojai', st: 'CA', p: 4200000, bd: 5, ba: 5, sf: 5120, t: 'estate', b: 'FOR SALE', img: '/img/l1.jpg', d: 'A hillside estate built around an infinity pool that seems to pour into the valley. Stone terraces step down to an olive grove, and every main room opens to the evening light.' },
 { n: 'The Lantern', a: '17 Ridgeline Drive', c: 'Asheville', st: 'NC', p: 1850000, bd: 4, ba: 3, sf: 3640, t: 'modern', b: 'FOR SALE', img: '/img/l2.jpg', d: 'A glass and timber home that glows like a lantern after dark. Tall ceilings, a wraparound terrace and a kitchen designed by the architect who drew the whole house.' },
 { n: 'Willow Shore', a: '88 Willow Bend', c: 'Lake Oswego', st: 'OR', p: 960000, bd: 3, ba: 2, sf: 2180, t: 'waterfront', b: 'NEW', img: '/img/l3.jpg', d: 'A calm waterfront house with its own jetty and a lawn that runs straight to the lake. Light, easy to keep, and quietly restored by its last owners.' }
];
const people = [
 { n: 'Julian Hart', r: 'Managing broker', c: 'Ojai', img: '/img/a1.jpg' },
 { n: 'Naomi Brooks', r: 'Senior advisor', c: 'Asheville', img: '/img/a2.jpg' },
 { n: 'Elias Ward', r: 'Estate specialist', c: 'Bozeman', img: '/img/a3.jpg' },
 { n: 'Sofia Marin', r: "Buyer's advisor", c: 'Lake Oswego', img: '/img/a4.jpg' }
];
const quotes = [
 ['The first brokerage that asked how we wanted to live before asking what we could spend.', 'DANIEL & AMARA O.', 'Bought in Ojai, CA'],
 ['Acre made selling our family home feel calm instead of stressful. Every step was explained before it happened.', 'RUTH & LEON K.', 'Sold in Asheville, NC'],
 ['Naomi told us to walk away from a house we loved, and she was right. Three weeks later she found the one.', 'PRIYA S.', 'Bought in Lake Oswego, OR']
];
const posts = [
 { cat: 'MARKET REPORT', m: '6 MIN READ', h: 'What rising inventory means for buyers this autumn', x: 'Inventory is up nineteen per cent. In two of our markets that means leverage. In the other two it mostly means the wrong homes are sitting.', img: '/img/j1.jpg', b: ['For the first time in three years, buyers in our markets have more than a handful of homes to choose from. Inventory is up nineteen per cent on last autumn, and the headlines are calling it a buyer\'s market.', 'The reality is more uneven. In Ojai and Bozeman, good homes are still moving in under three weeks, and well priced listings are drawing more than one offer. The new supply there is mostly at the edges: homes that need serious work or sit on difficult plots.', 'In Asheville and Lake Oswego the picture is different. Sellers who priced for last year are now sitting, and patient buyers are negotiating real reductions.', 'Our advice is simple. Do not read the national number and assume it applies to your street. Ask your advisor how long comparable homes are taking to sell right now, and let that shape your offer.'] },
 { cat: 'BUYING GUIDE', m: '4 MIN READ', h: 'Seven questions to ask before your first viewing', x: 'The useful questions are duller than the kitchen, and they are about the parts of the house you cannot see.', img: '/img/j2.jpg', b: ['A first viewing is designed to charm you. The light is good, the flowers are fresh and the kitchen has been cleared of everything but a bowl of lemons.', 'The questions that matter are about what you cannot see. How old is the roof, and has it ever leaked? When was the wiring last checked? Where does the water go when it rains hard?', 'Ask about running costs, recent repairs and why the owners are moving. Ask what the neighbours are like at eleven on a Friday night.', 'None of these will make the house more beautiful. All of them will tell you whether it is the right one.'] },
 { cat: 'SELLING', m: '5 MIN READ', h: 'Staging that actually moves the price', x: 'Most staging spend never comes back. Three things reliably do, and one of them costs sixty dollars.', img: '/img/j3.jpg', b: ['Sellers spend thousands on staging every year, and most of it never shows up in the final price.', 'Three things consistently do. First, light: clean windows, warm bulbs and open curtains change how every room photographs. Second, the entrance: a freshly painted front door and one good plant set the tone before anyone steps inside.', 'Third, and cheapest, is scent and quiet. Fix the dripping tap, oil the squeaky hinge and open a window an hour before a viewing. It costs about sixty dollars and buyers remember it.'] }
];
const svcs = [
 ['Mortgage and finance', 'Unusual homes are harder to lend on. We introduce you to lenders who understand architect designed, rural and historic properties, so your finance is agreed before you fall in love with a house.'],
 ['Property management', 'For owners who spend part of the year elsewhere, we look after the house as if it were ours: seasonal checks, trusted trades and a short monthly note so you always know how it is doing.'],
 ['Renovation and design', 'Before you buy, we can bring an architect or builder we trust to walk the house with you. You will know what is possible, and roughly what it costs, before you make an offer.']
];

/* nav */
const nav = $('#nav'), onScroll = () => nav.classList.toggle('solid', scrollY > innerHeight * .75);
onScroll(); addEventListener('scroll', onScroll, { passive: true });
const menu = $('#menu');
$('#burger').onclick = () => menu.classList.add('open'); $('#close').onclick = () => menu.classList.remove('open');
$$('#menu a').forEach(a => a.onclick = () => menu.classList.remove('open'));

/* theme */
const modeBtn = $('#mode'), setIcon = () => modeBtn.innerHTML = `<svg><use href="#${document.documentElement.classList.contains('night') ? 'sun' : 'moon'}"/></svg>`;
setIcon(); modeBtn.onclick = () => { const on = document.documentElement.classList.toggle('night'); try { localStorage.setItem('acre.night', on ? '1' : '0') } catch (e) { } setIcon() };

/* listings */
const cards = $('#cards');
cards.innerHTML = homes.map((h, i) => `<button class="pc reveal" data-home="${i}"><div class="im imr"><img src="${h.img}" alt="${h.n}" loading="lazy"><span class="badge">${h.b}</span><span class="price">${money(h.p)}</span></div><h3>${h.n}</h3><div class="ad">${h.a} · ${h.c}, ${h.st}</div><div class="sp">${h.bd} beds · ${h.ba} baths · ${h.sf.toLocaleString('en-US')} sq ft</div></button>`).join('') + `<div class="none" id="none">No residences match that search right now. Try widening it, or ask an advisor about homes not yet listed.</div>`;
function filter(f) {
 let shown = 0;
 $$('.pc', cards).forEach((c, i) => { const h = homes[i]; const [lo, hi] = (f.price || '0-999999999').split('-').map(Number);
  const ok = (!f.loc || h.c === f.loc) && (!f.type || h.t === f.type) && h.p >= lo && h.p <= hi && h.bd >= (+f.bed || 0);
  c.classList.toggle('hide', !ok); if (ok) shown++ });
 $('#none').classList.toggle('show', !shown);
 $('#count').textContent = shown === homes.length ? '' : `${shown} of ${homes.length} residences`;
}
$('#search').onsubmit = e => { e.preventDefault(); filter({ loc: $('#sLoc').value, type: $('#sType').value, price: $('#sPrice').value, bed: $('#sBed').value }); $('#residences').scrollIntoView({ behavior: 'smooth' }) };
$('#viewAll').onclick = () => { $('#search').reset(); filter({}) };

/* hero feature rotator */
let fi = 0, fT;
const segs = $$('#segs button');
function feature(i) {
 fi = i; const h = homes[i], t = $('#ftxt'); t.style.opacity = 0;
 setTimeout(() => { $('#fName').textContent = h.n; $('#fAddr').textContent = `${h.a}, ${h.c}, ${h.st}`; $('#fPrice').textContent = money(h.p); $('#fBadge').textContent = i === 0 ? 'FEATURED' : h.b; t.style.opacity = 1 }, 250);
 segs.forEach((s, k) => { s.classList.remove('on', 'done'); void s.offsetWidth; if (k < i) s.classList.add('done'); if (k === i) s.classList.add('on') });
 clearTimeout(fT); fT = setTimeout(() => feature((fi + 1) % homes.length), 5500);
}
segs.forEach((s, i) => s.onclick = () => feature(i)); feature(0);
$('#fView').onclick = () => openHome(fi);

/* advisors */
$('#advs').innerHTML = people.map((p, i) => `<button class="av reveal" data-adv="${i}"><div class="im imr"><img src="${p.img}" alt="${p.n}" loading="lazy"><span class="bk">BOOK →</span></div><h4>${p.n}</h4><small>${p.r} · ${p.c}</small></button>`).join('');

/* testimonials */
let qi = 0, qT;
$('#tdots').innerHTML = quotes.map((_, i) => `<button aria-label="Quote ${i + 1}"></button>`).join('');
function quote(i, first) {
 qi = i; const q = $('#tq'), w = $('#tw');
 const set = () => { q.textContent = '“' + quotes[i][0] + '”'; w.innerHTML = `${quotes[i][1]}<small>${quotes[i][2]}</small>`; q.classList.remove('out'); w.style.opacity = 1 };
 if (first) set(); else { q.classList.add('out'); w.style.opacity = 0; setTimeout(set, 450) }
 $$('#tdots button').forEach((d, k) => d.classList.toggle('on', k === i));
 clearTimeout(qT); qT = setTimeout(() => quote((qi + 1) % quotes.length), 7000);
}
$$('#tdots button').forEach((d, i) => d.onclick = () => quote(i)); quote(0, true);

/* journal */
$('#jr').innerHTML = posts.map((p, i) => `<button class="jp reveal" data-post="${i}"><div class="im imr"><img src="${p.img}" alt="" loading="lazy"></div><span class="eb">${p.cat} · ${p.m}</span><h4>${p.h}</h4><p>${p.x}</p></button>`).join('');

/* reveal */
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); $$('.imr', e.target).forEach(x => x.classList.add('in')); io.unobserve(e.target) } }), { threshold: .12, rootMargin: '0px 0px -40px 0px' });
$$('.reveal').forEach(el => { const sib = [...el.parentElement.children].filter(c => c.classList.contains('reveal')); el.style.transitionDelay = Math.min(sib.indexOf(el), 4) * 90 + 'ms'; io.observe(el) });

/* count */
const co = new IntersectionObserver(es => es.forEach(e => { if (!e.isIntersecting) return; co.unobserve(e.target); const t = +e.target.dataset.count, s = performance.now();
 const f = n => { const p = Math.min(1, (n - s) / 1800), v = Math.round(t * (1 - Math.pow(1 - p, 4))); e.target.textContent = v.toLocaleString('en-US'); if (p < 1) requestAnimationFrame(f) }; reduce ? e.target.textContent = t.toLocaleString('en-US') : requestAnimationFrame(f) }), { threshold: .6 });
$$('[data-count]').forEach(el => co.observe(el));

/* about: words fill on scroll + parallax */
const qEl = $('#quote'); qEl.innerHTML = qEl.textContent.split(' ').map(w => `<span>${w}</span>`).join(' ');
const qws = $$('span', qEl), aImg = $('#aboutImg'), cImg = $('#ctaImg');
function sc() {
 const r = qEl.getBoundingClientRect(), p = Math.min(1, Math.max(0, (innerHeight * .85 - r.top) / (r.height + innerHeight * .35)));
 const n = Math.round(p * qws.length); qws.forEach((w, i) => w.classList.toggle('on', i < n));
 if (!reduce) { const a = aImg.parentElement.getBoundingClientRect(); aImg.style.transform = `translateY(${(a.top / innerHeight) * -60 - 40}px)`; const c = cImg.parentElement.getBoundingClientRect(); cImg.style.transform = `translateY(${(c.top / innerHeight) * -60 - 40}px)` }
}
addEventListener('scroll', sc, { passive: true }); sc();

/* modal */
const ov = $('#ov'), mod = $('#mod');
function open(html, wide) { mod.className = 'mod' + (wide ? ' wide' : ''); mod.innerHTML = `<button class="x" aria-label="Close">×</button>` + html; ov.classList.add('open'); mod.scrollTop = 0; document.body.style.overflow = 'hidden'; $('.x', mod).onclick = close }
function close() { ov.classList.remove('open'); document.body.style.overflow = '' }
ov.onclick = e => { if (e.target === ov) close() }; addEventListener('keydown', e => e.key === 'Escape' && close());
function openHome(i) { const h = homes[i]; open(`<div class="pm"><img src="${h.img}" alt="${h.n}"><div class="b"><span class="eb">${h.b} · ${h.c.toUpperCase()}, ${h.st}</span><h3>${h.n}</h3><span style="color:var(--mut);font-size:13.5px">${h.a}, ${h.c}, ${h.st}</span><div class="facts"><div><b>${money(h.p)}</b><span>PRICE</span></div><div><b>${h.bd}</b><span>BEDROOMS</span></div><div><b>${h.ba}</b><span>BATHROOMS</span></div><div><b>${h.sf.toLocaleString('en-US')}</b><span>SQ FT</span></div></div><p>${h.d}</p><button class="btn btn-d" data-view="${i}">Arrange a private viewing <i>→</i></button></div></div>`, true) }
function viewing(home, adv) {
 open(`<span class="eb">Private viewing</span><h3>Let us show you around.</h3><p class="lead">Leave your details and the right advisor will be in touch within one working day.</p>
 <form id="vf" novalidate><div class="two"><label class="fld"><span>FULL NAME</span><input name="n" autocomplete="name"></label><label class="fld"><span>EMAIL</span><input name="e" type="email" autocomplete="email"></label></div>
 <label class="fld"><span>RESIDENCE</span><select name="h"><option value="">Not sure yet</option>${homes.map((h, i) => `<option value="${i}" ${String(home) === String(i) ? 'selected' : ''}>${h.n}, ${h.c}</option>`).join('')}</select></label>
 <label class="fld"><span>ADVISOR</span><select name="a"><option value="">Match me with an advisor</option>${people.map((p, i) => `<option value="${i}" ${String(adv) === String(i) ? 'selected' : ''}>${p.n}, ${p.c}</option>`).join('')}</select></label>
 <label class="fld"><span>ANYTHING WE SHOULD KNOW</span><textarea name="m" placeholder="Timing, must haves, questions"></textarea></label><div class="err" id="verr"></div><button class="btn btn-d">Request viewing <i>→</i></button></form>`);
 $('#vf').onsubmit = e => { e.preventDefault(); const f = new FormData(e.target), n = f.get('n').trim(), em = f.get('e').trim();
  if (!n) return $('#verr').textContent = 'Please add your name.'; if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em)) return $('#verr').textContent = 'Please use a valid email address.';
  const a = f.get('a') !== '' ? people[+f.get('a')].n : 'An advisor';
  mod.innerHTML = `<button class="x" aria-label="Close">×</button><div class="ok"><div class="c">✓</div><h3>Thank you, ${n.split(' ')[0]}.</h3><p class="lead">${a} will email ${em} within one working day to arrange a time that suits you.</p><button class="btn btn-d" id="okb">Close</button></div>`; $('.x', mod).onclick = close; $('#okb').onclick = close };
}
document.addEventListener('click', e => {
 const v = e.target.closest('[data-view]'); if (v) { menu.classList.remove('open'); return viewing(v.dataset.view, '') }
 const a = e.target.closest('[data-adv]'); if (a) return viewing('', a.dataset.adv);
 const h = e.target.closest('[data-home]'); if (h) return openHome(+h.dataset.home);
 const p = e.target.closest('[data-post]'); if (p) { const x = posts[+p.dataset.post]; return open(`<div class="art"><span class="eb">${x.cat} · ${x.m}</span><h3 style="margin-top:12px">${x.h}</h3><img src="${x.img}" alt="">${x.b.map(t => `<p>${t}</p>`).join('')}</div>`, true) }
 const s = e.target.closest('[data-svc]'); if (s) { const x = svcs[+s.dataset.svc]; return open(`<span class="eb">What else we do</span><h3>${x[0]}</h3><p class="lead">${x[1]}</p><button class="btn btn-d" data-view>Talk to an advisor <i>→</i></button>`) }
 const l = e.target.closest('[data-legal]'); if (l) { const t = l.dataset.legal === 'terms'; return open(`<h3>${t ? 'Terms' : 'Privacy'}</h3><p class="lead">${t ? 'Acre is a concept brokerage created to show a complete real estate website. The residences, advisors and prices on this page are illustrative.' : 'This concept site does not collect personal data. Forms show a confirmation in your browser and nothing is sent anywhere.'}</p>`) }
});

/* newsletter */
$('#news').onsubmit = e => { e.preventDefault(); const v = $('#nEmail').value.trim(), m = $('#nMsg'); if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v)) { m.textContent = 'Please enter a valid email.'; return } m.textContent = 'Thank you. New residences will reach you first.'; e.target.reset() };
})();
