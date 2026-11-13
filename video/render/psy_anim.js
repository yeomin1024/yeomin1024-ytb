/* VERSION: v1.0 — 2026-11-13 — 심리 편 공통 애니메이션 엔진 (주식 만스피 장면 v3.1 엔진을 바탕으로 — 원화 바꿔 끼우기 · 세계 층 카메라 · 앞 물건)
   사용자 지시 2026-11-13 "만스피 영상처럼 영상 만들거니까 …" → "1시간 마다 오디오 확인하고 생긴것 부터 영상 만들어".
   쓰는 곳: video/episodes/<심리 영상ID>/index.html — kit.js(K) 다음에 불러 PSY.setup(...) 후 shot()·world()·actor()… 로 장면을 짓고 PSY.build().
   · 세계(world) = 배경 → 뒤 소품 → 인물 → 앞 물건 → 떠 있는 것 → 빛 층이 한 카메라(cam)로 같이 움직임.
   · 인물 = 원화 바꿔 끼우기 (K.onSeek — 시각 t 의 순수 함수라 렌더·점검이 같은 그림) · 숨쉬기 · 자세가 바뀔 때 눌림.
   · 글자 칸(말풍선·판 카드·장 제목) = 코드. 말풍선은 머리 상자 옆에 (얼굴을 가리지 않게).
   · 배치 표: 세계 안 물건 = WORLD 칸 · 장 제목 = HEAD 칸 · 목록 카드 = LIST 칸 (layout-check).
   연구·교육용 영상 — 심리 진단·치료가 아님.
   CHANGELOG
   | 버전 | 날짜 | 바뀐 것 |
   |---|---|---|
   | v1.0 | 2026-11-13 | 최초 — world·cam·shake·actor·moves·talk·bubble·boardCard·title·listCard·weather·waves·heart |
*/
(function () {
"use strict";
const P = window.PSY = {};
let MAN, CUT, BGF, tl;
const SHOTS = [];
const ACTORS = [];
P.RD = "#FF5A4A"; P.TL = "#22C7B0"; P.YL = "#FFD400"; P.BL = "#5B8CFF"; P.INK = "#1B2030";

P.setup = (o) => {
  MAN = o.man; CUT = o.cut; BGF = o.bg; tl = K.tl;
  window.LAYOUT = Object.assign({ WORLD: [-620, -400, 3160, 1880], HEAD: [40, 28, 1840, 150], LOW: [40, 560, 1840, 300], LIST: [80, 150, 1760, 720] }, o.layout || {});
  window.LAYOUT_ALLOW = [["WORLD", "HEAD"], ["WORLD", "LIST"], ["HEAD", "LIST"], ["WORLD", "LOW"]].concat(o.allow || []);
  const css = `
.world{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0}
.lay{position:absolute;left:0;top:0;width:1920px;height:1080px}
.lay>img.bgp{position:absolute;left:0;top:0;width:1920px;height:1080px}
.act{position:absolute}.act .inn{position:absolute;left:0;top:0;width:100%;height:100%}.act .inn>img{position:absolute;opacity:0}
.shd{position:absolute;border-radius:50%;background:radial-gradient(closest-side,rgba(0,0,0,.38),rgba(0,0,0,0))}
.spr{position:absolute;left:0;top:0}.fg{position:absolute}
.light{position:absolute;left:0;top:0;width:1920px;height:1080px;pointer-events:none}
.pbub{position:absolute;left:0;top:0;background:#FFFDF6;color:#1B2030;font-weight:800;line-height:1.18;text-align:center;word-break:keep-all;
  border:5px solid #1B2030;border-radius:38px;padding:22px 34px;box-shadow:0 10px 0 rgba(0,0,0,.18)}
.pbub.think{border-radius:60px}
.pbub .tail{position:absolute;width:34px;height:34px;background:#FFFDF6;border:5px solid #1B2030;border-top:none;border-left:none;transform:rotate(45deg)}
.pbub.think .tail{border-radius:50%;transform:none;border:5px solid #1B2030;width:26px;height:26px}
.pbub .tail2{position:absolute;border-radius:50%;background:#FFFDF6;border:5px solid #1B2030;width:16px;height:16px}
.pcard{position:absolute;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#1B2030;font-weight:800;word-break:keep-all;line-height:1.16}
.pcard .big{font-weight:900;line-height:1.02}
.pcard .row{display:flex;align-items:center;gap:18px;justify-content:center}
.pchip{display:inline-block;padding:10px 26px;border-radius:999px;font-weight:900;color:#fff}
.ptitle{position:absolute;display:flex;align-items:center;gap:22px;padding:18px 40px 18px 18px;border-radius:999px;background:rgba(10,14,28,.86);
  border:3px solid rgba(255,255,255,.18);color:#fff;font-weight:900;font-size:52px;line-height:1;white-space:nowrap;box-shadow:0 10px 26px rgba(0,0,0,.35)}
.ptitle .no{width:84px;height:84px;border-radius:50%;display:grid;place-items:center;color:#1B2030;font-size:52px}
.plist{position:absolute;border-radius:30px;background:rgba(10,14,28,.88);border:3px solid rgba(255,255,255,.16);padding:30px 46px;color:#F4F6FA;box-shadow:0 14px 40px rgba(0,0,0,.4)}
.plist .it{display:flex;align-items:center;gap:22px;font-weight:800;font-size:50px;line-height:1.1;margin:14px 0}
.plist .it .no{flex:none;width:68px;height:68px;border-radius:50%;display:grid;place-items:center;color:#1B2030;font-weight:900;font-size:44px}
.pw{position:absolute;border-radius:50%;border:6px solid #FFD27A}
.sun{position:absolute;border-radius:50%;background:radial-gradient(circle at 40% 38%,#FFF2A8,#FFC93C 60%,#F5A623);box-shadow:0 0 50px rgba(255,201,60,.8)}
.cloud{position:absolute}
.cloud i{position:absolute;border-radius:50%;background:#C9D2E3;border:5px solid #59647A}
.heart{position:absolute;color:#FF6B7A;font-weight:900;line-height:1}
`;
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
};

/* ─────────── 장면 = 세계 + 층 ─────────── */
P.shot = (t, fn) => SHOTS.push({ t, fn });
P.build = () => {
  SHOTS.sort((p, q) => p.t - q.t);
  SHOTS.forEach((s, i) => s.fn(s.t, i + 1 < SHOTS.length ? SHOTS[i + 1].t : K.D));
};
P.world = (a, b, bg, opt) => {
  opt = opt || {};
  const sc = K.scene(a, b + 0.4);
  const w = K.el(`<div class="world" data-slot="WORLD" data-bg="${bg}"></div>`, sc);
  const L = {};
  for (const k of ["bg", "back", "act", "front", "fly", "light"]) L[k] = K.el(`<div class="lay" data-l="${k}"></div>`, w);
  const img = K.el(`<img class="bgp" src="${BGF[bg]}" alt="">`, L.bg);
  if (opt.filter) img.style.filter = opt.filter;
  if (opt.memory) {                                   // 어린 시절 기억 — 살짝 바랜 색 + 가장자리 어둡게
    L.bg.style.filter = "sepia(.28) saturate(.9)";
    L.act.style.filter = "sepia(.18)";
    K.el(`<div class="light" style="background:radial-gradient(ellipse at 50% 45%,rgba(0,0,0,0) 55%,rgba(30,18,6,.42) 100%)"></div>`, L.light);
  }
  if (opt.tint) K.el(`<div class="light" style="background:${opt.tint}"></div>`, L.light);
  return { sc, w, L, a, b };
};
P.cam = (W_, a, b, from, to, ease) => {             // [배율, 초점 x, 초점 y] — 초점이 제자리에 남게 확대
  const xy = ([s, fx, fy]) => ({ scale: s, x: Math.min(0, Math.max(1920 - 1920 * s, fx * (1 - s))), y: Math.min(0, Math.max(1080 - 1080 * s, fy * (1 - s))) });
  tl.fromTo(W_.w, xy(from), Object.assign(xy(to), { duration: Math.max(0.1, b - a), ease: ease || "sine.inOut", immediateRender: false }), a);
  if (a <= W_.a + 0.01) gsap.set(W_.w, xy(from));
};
P.shake = (W_, t, amp, dur) => {
  amp = amp || 14; dur = dur || 0.35;
  const k = [];
  for (let i = 0; i < 6; i++) k.push({ x: (i % 2 ? -1 : 1) * amp * (1 - i / 6), y: (i % 3 - 1) * amp * 0.5 * (1 - i / 6), duration: dur / 7 });
  k.push({ x: 0, y: 0, duration: dur / 7 });
  tl.to(W_.sc, { keyframes: k, ease: "none" }, t);
};
P.dark = (W_, t, op, color, dur) => {                // 방이 어두워짐 (마음이 무거워짐)
  const n = K.el(`<div class="light" style="background:${color || "rgba(8,14,40,.5)"}"></div>`, W_.L.light);
  gsap.set(n, { opacity: 0 });
  tl.to(n, { opacity: op == null ? 1 : op, duration: dur || 0.8, ease: "sine.inOut" }, t);
  return n;
};
const show = P.show = (n, t, d) => tl.to(n, { opacity: 1, duration: d == null ? 0.25 : d, ease: "none" }, t);
const hide = P.hide = (n, t, d) => tl.to(n, { opacity: 0, duration: d == null ? 0.25 : d, ease: "none" }, t);
P.pop = (n, t, s0) => tl.fromTo(n, { opacity: 0, scale: s0 == null ? 0.3 : s0 }, { opacity: 1, scale: 1, duration: 0.42, ease: "back.out(2.2)", immediateRender: false }, t);

/* ─────────── 인물 = 원화 바꿔 끼우기 ─────────── */
P.actor = (W_, keys, x, y, s, opt) => {
  opt = opt || {};
  keys = [...new Set(keys)];
  const sp = keys.map(k => { const m = MAN[k]; if (!m) throw new Error(`그림 없음: ${k}`); return { k, m }; });
  const fl = opt.flip ? -1 : 1;
  const L = Math.max(...sp.map(p => (fl > 0 ? p.m.ax : p.m.w - p.m.ax) * s)), R = Math.max(...sp.map(p => (fl > 0 ? p.m.w - p.m.ax : p.m.ax) * s));
  const U = Math.max(...sp.map(p => p.m.ay * s)), D = Math.max(...sp.map(p => (p.m.h - p.m.ay) * s)) + 30;
  const parent = opt.layer ? W_.L[opt.layer] : W_.L.act;
  const box = K.el(`<div class="act" data-id="${opt.id || sp[0].m.who}" style="left:${(x - L).toFixed(1)}px;top:${(y - U).toFixed(1)}px;width:${(L + R).toFixed(1)}px;height:${(U + D).toFixed(1)}px"></div>`, parent);
  if (opt.shadow !== false) {
    const sw = (opt.shw || 330) * s;
    K.el(`<div class="shd" style="left:${(L - sw / 2).toFixed(1)}px;top:${(U - 18 * s).toFixed(1)}px;width:${sw.toFixed(1)}px;height:${(40 * s).toFixed(1)}px"></div>`, box);
  }
  const inn = K.el(`<div class="inn"></div>`, box);
  if (opt.filter) inn.style.filter = opt.filter;
  gsap.set(box, { transformOrigin: `${L.toFixed(1)}px ${U.toFixed(1)}px` });
  gsap.set(inn, { transformOrigin: `${L.toFixed(1)}px ${U.toFixed(1)}px` });
  const imgs = {};
  for (const { k, m } of sp) {
    const left = fl > 0 ? L - m.ax * s : L - (m.w - m.ax) * s;
    imgs[k] = K.el(`<img src="${CUT}${k}.png" alt="" style="left:${left.toFixed(1)}px;top:${(U - m.ay * s).toFixed(1)}px;width:${(m.w * s).toFixed(1)}px;height:${(m.h * s).toFixed(1)}px${fl < 0 ? ";transform:scaleX(-1)" : ""}">`, inn);
  }
  const A = { box, inn, imgs, x, y, s, L, U, fl, track: [], cur: null, keys };
  ACTORS.push(A);
  if (opt.at != null) { gsap.set(box, { opacity: 0 }); show(box, opt.at, opt.fade == null ? 0.3 : opt.fade); }
  return A;
};
// 동작 목록: [[시작, 원화 목록, 초당 장 수, 방식]] — hold · once · loop · pp(1→2→3→2→1)
P.moves = (A, list, end) => {
  list = list.filter(Boolean).sort((p, q) => p[0] - q[0]);
  list.forEach((m, i) => {
    const [a, seq, fps, mode] = m;
    const b = i + 1 < list.length ? list[i + 1][0] : end;
    for (const k of [].concat(seq)) if (!A.imgs[k]) throw new Error(`원화 없음(actor 에 넣지 않음): ${k}`);
    A.track.push({ a, b, seq: [].concat(seq), fps: fps || 8, mode: mode || "hold" });
  });
};
function frameAt(tr, t) {
  const n = tr.seq.length, i = Math.floor((t - tr.a) * tr.fps + 1e-6);
  switch (tr.mode) {
    case "once": return tr.seq[Math.min(n - 1, i)];
    case "loop": return tr.seq[i % n];
    case "pp": { if (n < 2) return tr.seq[0]; const p = 2 * n - 2, j = i % p; return tr.seq[j < n ? j : p - j]; }
    case "talk": {                                    // 말하기: 입 연 장·다문 장을 고르지 않게 (정해진 난수 — 렌더마다 같음)
      const h = Math.sin(i * 12.9898 + tr.a * 78.233) * 43758.5453; return tr.seq[(h - Math.floor(h)) < 0.62 ? 0 : 1];
    }
    default: return tr.seq[0];
  }
}
K.onSeek(t => {
  for (const A of ACTORS) {
    let key = null;
    for (const tr of A.track) if (t >= tr.a && t < tr.b) key = frameAt(tr, t);
    if (key !== A.cur) {
      if (A.cur) A.imgs[A.cur].style.opacity = 0;
      if (key) A.imgs[key].style.opacity = 1;
      A.cur = key;
    }
  }
});
P.squash = (A, t, amt) => {
  amt = amt || 0.045;
  tl.fromTo(A.box, { scaleY: 1 - amt, scaleX: 1 + amt * 0.6 }, { scaleY: 1, scaleX: 1, duration: 0.32, ease: "back.out(3)", immediateRender: false }, t);
};
P.breathe = (A, a, b) => {
  const per = 1.4, n = Math.max(1, Math.floor((b - a) / per) - 1);
  tl.fromTo(A.inn, { scaleY: 1 }, { scaleY: 1.012, duration: per / 2, ease: "sine.inOut", repeat: n, yoyo: true, immediateRender: false }, a);
};
P.slide = (A, t, dx, dur) => {                         // 옆에서 걸어 들어옴 (몸 이동)
  tl.fromTo(A.box, { x: dx }, { x: 0, duration: dur || 0.8, ease: "power2.out", immediateRender: false }, t);
};
P.headOf = (A, f) => {                                // 원화 f 의 머리 상자 (세계 좌표) [x0, y0, x1, y1]
  const m = MAN[f], h = m.pt.head;
  const hx = A.fl > 0 ? h[0] - m.ax : m.ax - h[0];
  const cx = A.x + hx * A.s, cy = A.y + (h[1] - m.ay) * A.s, w = h[2] * A.s, hh = h[3] * A.s;
  return [cx - w / 2, cy - hh / 2, cx + w / 2, cy + hh / 2];
};
// 말하기 설명 (A07 같은 시트: 1 = 가리킴 · 2 = 입 엶 · 3 = 입 다묾) — points = 가리키는 시각들
P.explain = (A, sheet, a, b, points) => {
  const k1 = `${sheet}-1`, k2 = `${sheet}-2`, k3 = `${sheet}-3`;
  const list = [[a, [k2, k3], 7, "talk"]];
  for (const p of (points || [])) { list.push([p, k1, 1, "hold"]); list.push([p + 1.1, [k2, k3], 7, "talk"]); }
  P.moves(A, list, b + 0.4);
};

/* ─────────── 소품 ─────────── */
P.spr = (parent, key, cx, cy, size, extra) => {
  const m = MAN[key]; if (!m) throw new Error(`그림 없음: ${key}`);
  const k = size / Math.max(m.w, m.h);
  const n = K.el(`<img class="spr" src="${CUT}${key}.png" alt="" style="width:${(m.w * k).toFixed(1)}px;height:${(m.h * k).toFixed(1)}px${extra || ""}">`, parent);
  gsap.set(n, { xPercent: -50, yPercent: -50, x: cx, y: cy, opacity: 0 });
  return n;
};
P.fgCut = (parent, key) => {
  const m = MAN[key];
  return K.el(`<img class="fg" src="${CUT}${key}.png" alt="" style="left:${m.x}px;top:${m.y}px;width:${m.sw}px;height:${m.sh}px">`, parent);
};

/* ─────────── 글자 칸 ─────────── */
// 말풍선: 머리 옆 (side -1 = 머리 왼쪽 · 1 = 오른쪽) · kind 'say' | 'think' · 머리를 가리지 않음
P.bubble = (W_, A, f, html, t, out, opt) => {
  opt = opt || {};
  const size = opt.size || 48, w = opt.w || 520;
  const hb = P.headOf(A, f), side = opt.side || -1;
  const n = K.el(`<div class="pbub ${opt.kind === "think" ? "think" : ""}" style="width:${w}px;font-size:${size}px${opt.color ? `;color:${opt.color}` : ""}">${html}</div>`, W_.L.fly);
  const tail = opt.kind === "think"
    ? K.el(`<div class="tail" style="${side < 0 ? "right:-30px" : "left:-30px"};bottom:-26px"></div>`, n)
    : K.el(`<div class="tail" style="${side < 0 ? "right:46px" : "left:46px"};bottom:-21px"></div>`, n);
  if (opt.kind === "think") K.el(`<div class="tail2" style="${side < 0 ? "right:-50px" : "left:-50px"};bottom:-46px"></div>`, n);
  void tail;
  const gap = opt.gap == null ? 34 : opt.gap;
  const x = side < 0 ? hb[0] - gap - w : hb[2] + gap;
  const y = (opt.y != null ? opt.y : hb[1] - 40);
  gsap.set(n, { x, y, opacity: 0, transformOrigin: side < 0 ? "100% 100%" : "0% 100%" });
  tl.fromTo(n, { opacity: 0, scale: 0.35 }, { opacity: 1, scale: 1, duration: 0.38, ease: "back.out(2.2)", immediateRender: false }, t);
  if (out) hide(n, out, 0.25);
  return n;
};
// 화면 밖 사람의 말 (말하는 사람 없이 — 꼬리가 화면 가장자리 쪽)
P.voice = (W_, html, x, y, t, out, opt) => {
  opt = opt || {};
  const n = K.el(`<div class="pbub" style="width:${opt.w || 560}px;font-size:${opt.size || 48}px;background:#EAF3FF">${html}</div>`, W_.L.fly);
  K.el(`<div class="tail" style="background:#EAF3FF;${opt.tail === "right" ? "right:-21px;top:40%;transform:rotate(-45deg)" : "left:-21px;top:40%;transform:rotate(135deg)"}"></div>`, n);
  gsap.set(n, { x, y, opacity: 0 });
  P.pop(n, t, 0.4);
  if (out) hide(n, out, 0.25);
  return n;
};
// 판(화이트보드 등) 위 카드: rect = [x, y, w, h] 세계 좌표 · html = 안의 글 · 차례로 나타남
P.board = (W_, rect, html, t, out, opt) => {
  opt = opt || {};
  const [x, y, w, h] = rect;
  const n = K.el(`<div class="pcard" style="left:${x}px;top:${y}px;width:${w}px;height:${h}px;font-size:${opt.size || 56}px${opt.color ? `;color:${opt.color}` : ""}">${html}</div>`, W_.L.back);
  gsap.set(n, { opacity: 0 });
  tl.fromTo(n, { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.4, ease: "power2.out", immediateRender: false }, t);
  if (out) hide(n, out, 0.25);
  return n;
};
// 장 제목 (화면 위 — 세계 밖, 카메라와 상관없이)
P.title = (W_, no, color, text, t, out) => {
  const n = K.el(`<div class="ptitle" data-slot="HEAD" style="left:60px;top:40px"><span class="no" style="background:${color}">${no}</span><span>${text}</span></div>`, W_.sc);
  gsap.set(n, { opacity: 0, transformOrigin: "0% 50%" });
  tl.fromTo(n, { opacity: 0, x: -50 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out", immediateRender: false }, t);
  if (out) hide(n, out, 0.35);
  return n;
};
// 번호 목록 카드 (세계 밖) — items = [[번호, 색, 글, 나타날 시각]]
P.list = (W_, rect, items, out, opt) => {
  opt = opt || {};
  const [x, y, w] = rect;
  const box = K.el(`<div class="plist" data-slot="LIST" style="left:${x}px;top:${y}px;width:${w}px"></div>`, W_.sc);
  gsap.set(box, { opacity: 0 });
  const rows = items.map(([no, c, text, at]) => {
    const r = K.el(`<div class="it"><span class="no" style="background:${c}">${no}</span><span>${text}</span></div>`, box);
    gsap.set(r, { opacity: 0 });
    tl.fromTo(r, { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.35, ease: "power3.out", immediateRender: false }, at);
    return r;
  });
  show(box, Math.min(...items.map(i => i[3])) - 0.05, 0.2);
  if (out) hide(box, out, 0.3);
  return { box, rows };
};
// 가운데 위 이름표 (세계 밖 — HEAD 칸): 장면의 핵심 한 줄
P.label = (W_, html, t, out, opt) => {
  opt = opt || {};
  const slot = (opt.top || 44) > 300 ? "LOW" : "HEAD";            // 아래쪽 이름표 (판 아래 · 자막 위) = LOW 칸
  const n = K.el(`<div class="ptitle" data-slot="${slot}" style="left:50%;top:${opt.top || 44}px;padding:20px 44px;font-size:${opt.size || 54}px${opt.bg ? `;background:${opt.bg}` : ""}">${html}</div>`, W_.sc);
  gsap.set(n, { xPercent: -50, opacity: 0 });
  tl.fromTo(n, { opacity: 0, y: -30 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out", immediateRender: false }, t);
  if (out) hide(n, out, 0.3);
  return n;
};
P.mark = (row, t, color) => tl.to(row, { color: color || P.YL, scale: 1.04, transformOrigin: "0% 50%", duration: 0.3 }, t);

/* ─────────── 효과 ─────────── */
P.waves = (parent, cx, cy, t, dur, color) => {       // 소리 물결 (문 너머 목소리)
  for (let i = 0; i < 3; i++) {
    const n = K.el(`<div class="pw" style="left:${cx - 40}px;top:${cy - 40}px;width:80px;height:80px;border-color:${color || "#FFD27A"}"></div>`, parent);
    gsap.set(n, { opacity: 0 });
    tl.fromTo(n, { opacity: 0.9, scale: 0.4 }, { opacity: 0, scale: 2.6, duration: 1.2, ease: "power1.out", repeat: Math.max(0, Math.floor(dur / 1.2) - 1), immediateRender: false }, t + i * 0.4);
  }
};
P.sun = (parent, cx, cy, r) => K.el(`<div class="sun" style="left:${cx - r}px;top:${cy - r}px;width:${2 * r}px;height:${2 * r}px"></div>`, parent);
P.cloud = (parent, cx, cy, s, dark) => {
  const c = K.el(`<div class="cloud" style="left:${cx - 120 * s}px;top:${cy - 60 * s}px;width:${240 * s}px;height:${120 * s}px"></div>`, parent);
  const f = dark ? "#8D97AB" : "#DDE4F0";
  for (const [x, y, r] of [[30, 50, 40], [80, 22, 52], [140, 38, 46], [175, 60, 34], [60, 66, 34], [118, 70, 36]])
    K.el(`<i style="left:${(x - r) * s}px;top:${(y - r) * s}px;width:${2 * r * s}px;height:${2 * r * s}px;background:${f}"></i>`, c);
  return c;
};
P.heart = (parent, cx, cy, size, color) => K.el(`<div class="heart" style="left:${cx - size / 2}px;top:${cy - size / 2}px;font-size:${size}px;color:${color || "#FF6B7A"}">♥</div>`, parent);
P.float = (n, t, dur, dy) => tl.to(n, { y: `-=${dy || 16}`, duration: (dur || 2) / 2, yoyo: true, repeat: 1, ease: "sine.inOut" }, t);
})();
