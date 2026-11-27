(() => {
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
const root = document.documentElement;
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const touch = matchMedia('(pointer: coarse)').matches;
const lenis = () => window.__lenis;
const ease = t => 1 - Math.pow(1 - t, 3);

/* loader, first visit of the session only */
function start() { root.classList.add('ready'); heroLoop() }
if (root.classList.contains('loading')) {
 lenis() && lenis().stop();
 const n = $('#lnum'), bar = $('#lbar'), t0 = performance.now(), dur = reduce ? 200 : 1700;
 const step = now => { const p = Math.min(1, (now - t0) / dur), v = Math.round(ease(p) * 100); n.textContent = v; bar.style.transform = `scaleX(${ease(p)})`; if (p < 1) requestAnimationFrame(step); else done() };
 requestAnimationFrame(step);
 function done() { try { sessionStorage.setItem('acre.loaded', '1') } catch (e) { } setTimeout(() => { root.classList.add('loaded'); lenis() && lenis().start(); setTimeout(start, 250); setTimeout(() => root.classList.remove('loading', 'loaded'), 1100) }, 250) }
} else requestAnimationFrame(start);

/* nav */
const nav = $('#nav'), hero = $('.hero');
const ns = () => nav.classList.toggle('solid', scrollY > (hero ? hero.offsetHeight - 80 : 10));
ns(); addEventListener('scroll', ns, { passive: true });
const burger = $('#burger');
burger.onclick = () => { const o = !root.classList.contains('menu-open'); root.classList.toggle('menu-open', o); o ? lenis() && lenis().stop() : lenis() && lenis().start() };
$$('#menu a').forEach(a => a.addEventListener('click', () => { root.classList.remove('menu-open'); lenis() && lenis().start() }));
addEventListener('keydown', e => { if (e.key === 'Escape' && root.classList.contains('menu-open')) burger.click() });
const here = location.pathname.replace(/\/$/, '');
$$('.links a, #menu a.l').forEach(a => { const h = a.getAttribute('href'); if (h !== '/' && (here === h || here.startsWith(h + '/'))) a.classList.add('cur') });

/* theme */
const modeBtn = $('#mode'), setIcon = () => modeBtn.innerHTML = `<svg><use href="#${root.classList.contains('night') ? 'sun' : 'moon'}"/></svg>`;
setIcon(); modeBtn.onclick = () => { const on = root.classList.toggle('night'); try { localStorage.setItem('acre.night', on ? '1' : '0') } catch (e) { } setIcon() };

/* hero rotator, background and card stay in sync */
const segs = $$('#segs button'), bgs = $$('#bgs .bg');
let fi = 0, fT;
function feature(i) {
 if (!segs.length) return; fi = i; const s = segs[i], t = $('#ftxt');
 bgs.forEach((b, k) => b.classList.toggle('on', k === i));
 t.classList.add('swap');
 setTimeout(() => { $('#fName').textContent = s.dataset.n; $('#fAddr').textContent = s.dataset.a; $('#fPrice').textContent = s.dataset.p; $('#feat').href = '/residences/' + s.dataset.slug; t.classList.remove('swap') }, 300);
 segs.forEach((x, k) => { x.classList.remove('on', 'done'); void x.offsetWidth; if (k < i) x.classList.add('done'); if (k === i) x.classList.add('on') });
 clearTimeout(fT); fT = setTimeout(() => feature((fi + 1) % segs.length), 6000);
}
function heroLoop() { if (segs.length && !segs.some(s => s.classList.contains('on'))) feature(0) }
segs.forEach((s, i) => s.addEventListener('click', e => { e.preventDefault(); e.stopPropagation(); feature(i) }));

/* residences filters, from chips or the home search */
const cards = $$('#cards .pc');
if (cards.length) {
 const q = new URLSearchParams(location.search);
 let type = q.get('type') || '';
 const loc = q.get('loc') || '', price = q.get('price') || '', bed = +(q.get('bed') || 0);
 const apply = () => {
  let shown = 0; const [lo, hi] = (price || '0-999999999').split('-').map(Number);
  cards.forEach(c => { const ok = (!type || c.dataset.type === type) && (!loc || c.dataset.city === loc) && +c.dataset.price >= lo && +c.dataset.price <= hi && +c.dataset.bed >= bed; c.classList.toggle('hide', !ok); if (ok) shown++ });
  $('#none').classList.toggle('show', !shown);
  $$('#chips button').forEach(b => b.classList.toggle('on', b.dataset.f === type));
 };
 $$('#chips button').forEach(b => b.onclick = () => { type = b.dataset.f; apply(); lenis() && lenis().resize() });
 apply();
}

/* reveal */
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); $$('.imr', e.target).forEach(x => x.classList.add('in')); io.unobserve(e.target) } }), { threshold: .1, rootMargin: '0px 0px -30px 0px' });
$$('.reveal, .imr').forEach(el => { const sib = [...el.parentElement.children].filter(c => c.classList.contains('reveal')); el.style.transitionDelay = Math.min(Math.max(sib.indexOf(el), 0), 4) * 80 + 'ms'; io.observe(el) });

/* counters */
const co = new IntersectionObserver(es => es.forEach(e => { if (!e.isIntersecting) return; co.unobserve(e.target); const t = +e.target.dataset.count, s = performance.now();
 const f = n => { const p = Math.min(1, (n - s) / 1800), v = Math.round(t * ease(p)); e.target.textContent = v.toLocaleString('en-US'); if (p < 1) requestAnimationFrame(f) }; reduce ? e.target.textContent = t.toLocaleString('en-US') : requestAnimationFrame(f) }), { threshold: .6 });
$$('[data-count]').forEach(el => co.observe(el));

/* about quote fills word by word, and gentle parallax on wide images */
const qEl = $('#quote'); let qws = [];
if (qEl) { qEl.innerHTML = qEl.textContent.split(' ').map(w => `<span>${w}</span>`).join(' '); qws = $$('span', qEl) }
const pxs = touch || reduce ? [] : $$('.px, .px2');
let q = 0;
function frame() {
 q = 0;
 if (qEl) { const r = qEl.getBoundingClientRect(), p = Math.min(1, Math.max(0, (innerHeight * .85 - r.top) / (r.height + innerHeight * .35))), n = Math.round(p * qws.length); qws.forEach((w, i) => w.classList.toggle('on', i < n)) }
 pxs.forEach(img => { const r = img.parentElement.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return; img.style.transform = `translate3d(0,${((r.top + r.height / 2) / innerHeight - .5) * -50}px,0) scale(1.08)` });
}
addEventListener('scroll', () => { if (!q) q = requestAnimationFrame(frame) }, { passive: true }); frame();

/* testimonials */
const dots = $$('#tdots button');
if (dots.length) {
 let qi = 0, qT; const tq = $('#tq'), tw = $('#tw');
 const show = i => { qi = i; tq.classList.add('out'); tw.style.opacity = 0; setTimeout(() => { const d = dots[i].dataset; tq.textContent = '“' + d.q + '”'; tw.innerHTML = `${d.w}<small>${d.s}</small>`; tq.classList.remove('out'); tw.style.opacity = 1 }, 450); dots.forEach((d, k) => d.classList.toggle('on', k === i)); clearTimeout(qT); qT = setTimeout(() => show((qi + 1) % dots.length), 7000) };
 dots.forEach((d, i) => d.onclick = () => show(i)); dots[0].classList.add('on'); qT = setTimeout(() => show(1), 7000);
}

/* forms */
const okEmail = v => /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v);
$$('.cform').forEach(f => f.addEventListener('submit', e => {
 e.preventDefault(); const d = new FormData(f), err = $('.err', f);
 if (!String(d.get('n') || '').trim()) return err.textContent = 'Please add your name.';
 if (!okEmail(String(d.get('e') || '').trim())) return err.textContent = 'Please use a valid email address.';
 err.textContent = ''; f.parentElement.classList.add('sent');
}));
$$('form.news').forEach(f => f.addEventListener('submit', e => { e.preventDefault(); const i = $('input', f), m = $('.fmsg', f); if (!okEmail(i.value.trim())) { m.textContent = 'Please enter a valid email.'; return } m.textContent = 'Thank you. New residences will reach you first.'; f.reset() }));

/* faq */
$$('.qa button').forEach(b => b.onclick = () => { const it = b.parentElement, was = it.classList.contains('on'); $$('.qa').forEach(x => { x.classList.remove('on'); $('button', x).setAttribute('aria-expanded', 'false') }); if (!was) { it.classList.add('on'); b.setAttribute('aria-expanded', 'true') } setTimeout(() => lenis() && lenis().resize(), 450) });
})();
