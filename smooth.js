(() => {
 if (matchMedia('(pointer: coarse)').matches || matchMedia('(prefers-reduced-motion: reduce)').matches || !window.Lenis) return;
 const l = new Lenis({ lerp: .1, wheelMultiplier: 1, anchors: { offset: -74 }, prevent: n => !!(n.closest && n.closest('.ov,.menu')) });
 window.__lenis = l;
 const raf = t => { l.raf(t); requestAnimationFrame(raf) }; requestAnimationFrame(raf);
})();
