// VERSION: v1.1 — 2026-10-15 — K.init(ep, {subtitles, chip}) 로 구운 자막·장 이름표를 끌 수 있음 (주식 = 전 세계 대상 — stock/guides/README.md 4번,
//   사용자 지시 2026-10-15 "영상에 자막 달지말고"), 오디오 없는 추정 시각(EP.estimated — render.mjs sync --estimate)은 시계로 미리보기.
// v1.0 — 2026-10-15 — 새 스타일 영상 공통 부품 (guides/video_guide.md v4.0 6번). 근거 시안 video/prototypes/storyboard-2026-10-15/
//   장면 파일(video/episodes/<영상ID>/index.html)이 window.EP(문장 시각·자막 — render.mjs sync 가 넣음)와 이 파일의 K 를 써서
//   GSAP 타임라인 하나를 만든다. 렌더기(render.mjs)는 ?render 로 열어 SB.seek(t) 로 장면을 멈춰 찍는다.
//   연구·교육용 영상 — 투자·세무 권유 아님.
(function () {
  "use strict";
  const K = (window.K = {});
  const RENDER = /[?&]render\b/.test(location.search);
  let EP, OPT, tl, stage, chipEl, ccEl;
  const CHAPTERS = [];        // [{start, tag, title, dots:[n,total]}]
  const CUTS = [];            // 점검용 대표 장면 [{t, name}]

  // ---------- 시각 ----------
  const SYL_DIGIT = { "0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1, "8": 1, "9": 1 };
  function numSyl(s) {                       // 숫자 읽는 음절 수 대강 (1,010 → 천십 = 2, 2026 → 이천이십육 = 5)
    const d = s.replace(/[^0-9]/g, "");
    let n = 0;
    for (let i = 0; i < d.length; i++) {
      const v = d[i], place = d.length - 1 - i;
      if (v === "0") continue;
      n += place === 0 ? 1 : (v === "1" ? 1 : 2);
    }
    return Math.max(1, n);
  }
  function sylLen(text) {                    // 읽는 길이 (음절 대강): 한글 1 · 숫자 묶음은 읽는 음절 · 영어 대문자 1.5 · %·. 등
    let n = 0;
    const re = /([0-9][0-9,]*(?:\.[0-9]+)?)|([가-힣])|([A-Za-z])|(%)|([,.?!])|(\s)/g;
    let m;
    while ((m = re.exec(text))) {
      if (m[1]) n += numSyl(m[1].split(".")[0]) + (m[1].includes(".") ? 1 + m[1].split(".")[1].length : 0);
      else if (m[2]) n += 1;
      else if (m[3]) n += 1.5;
      else if (m[4]) n += 3;
      else if (m[5]) n += 1.2;              // 쉼표·마침표 = 잠깐 쉼
      else if (m[6]) n += 0.15;
    }
    return n;
  }
  K.S = n => sent(n).start;                   // 문장 n 시작 (tts_narration.json — 오디오를 만든 도구의 정확한 시각)
  K.E = n => sent(n).end;
  K.W = (n, word, nth) => {                   // 문장 n 안에서 낱말 word 를 말하기 시작하는 시각 (읽는 음절 비율로 대강)
    const s = sent(n);
    let i = -1;
    for (let k = 0; k <= (nth || 0); k++) i = s.text.indexOf(word, i + 1);
    if (i < 0) throw new Error(`문장 ${n} 에 '${word}' 없음: ${s.text}`);
    const before = sylLen(s.text.slice(0, i)), all = sylLen(s.text);
    return +(s.start + (s.end - s.start) * (before / all)).toFixed(3);
  };
  function sent(n) {
    const s = EP.sent[n - 1];
    if (!s || s.n !== n) throw new Error(`문장 ${n} 없음`);
    return s;
  }

  // ---------- 요소 ----------
  K.el = (html, parent) => {
    const t = document.createElement("template");
    t.innerHTML = html.trim();
    const n = t.content.firstChild;
    (parent || stage).appendChild(n);
    if (n.classList && (n.classList.contains("cx") || n.classList.contains("tick"))) gsap.set(n, { xPercent: -50 });
    return n;
  };
  K.fmt = v => Math.round(v).toLocaleString("ko-KR");
  K.fmt1 = v => (Math.round(v * 10) / 10).toLocaleString("ko-KR", { minimumFractionDigits: 1, maximumFractionDigits: 1 });
  K.scene = (a, b, opts) => {                 // 장면: a 에 0.35초 나타나고 b 에 0.35초 사라짐
    const sc = K.el(`<div class="sc"></div>`);
    tl.fromTo(sc, { opacity: 0 }, { opacity: 1, duration: 0.35, ease: "none" }, Math.max(0, a));
    if (!(opts && opts.keep)) tl.to(sc, { opacity: 0, duration: 0.35, ease: "none" }, b - 0.35);
    return sc;
  };
  K.pop = (n, at, extra) =>
    tl.fromTo(n, Object.assign({ opacity: 0, y: 40, scale: 0.96 }, extra && extra.from),
      Object.assign({ opacity: 1, y: 0, scale: 1, duration: 0.55, ease: "power3.out" }, extra && extra.to), at);
  K.out = (nodes, at, extra) => tl.to(nodes, Object.assign({ opacity: 0, y: -40, duration: 0.4, ease: "power2.in" }, extra), at);
  K.dim = (nodes, at) => tl.to(nodes, { opacity: 0.12, duration: 0.45 }, at);
  K.counter = (node, from, to, at, dur, f) => {
    const o = { v: from };
    f = f || K.fmt;
    node.textContent = f(from);
    tl.fromTo(o, { v: from }, { v: to, duration: dur || 1.4, ease: "power2.out", onUpdate: () => { node.textContent = f(o.v); } }, at);
  };
  K.grow = (n, at, dur, axis) => tl.fromTo(n, axis === "y" ? { scaleY: 0 } : { scaleX: 0 },
    Object.assign(axis === "y" ? { scaleY: 1 } : { scaleX: 1 }, { duration: dur || 1.0, ease: "power2.out" }), at);
  K.color = (n, at, c, prop) => tl.to(n, { [prop || "backgroundColor"]: c, duration: 0.5 }, at);
  K.strike = (parent, left, top, width, at, rot) => {
    const s = K.el(`<div class="strike" style="left:${left}px;top:${top}px;width:${width}px;rotate:${rot == null ? -8 : rot}deg"></div>`, parent);
    tl.fromTo(s, { scaleX: 0 }, { scaleX: 1, duration: 0.35, ease: "power2.out" }, at);
    return s;
  };
  K.text = (parent, cx, top, html, size, cls) =>
    K.el(`<div class="a cx c nw ${cls || "w9"}" style="left:${cx}px;top:${top}px;font-size:${size}px">${html}</div>`, parent);
  K.big = (parent, cx, top, size, color, unit, unitSize) =>   // 큰 숫자 + 단위 → {box, num}
    (box => ({ box, num: box.firstChild }))(K.el(`<div class="a cx c w9 nw" style="left:${cx}px;top:${top}px;font-size:${size}px;line-height:1;letter-spacing:-4px;color:${color || "#F4F6FA"}"><span>0</span><span style="font-size:${unitSize || Math.round(size * 0.5)}px;letter-spacing:0">${unit == null ? "만 원" : unit}</span></div>`, parent));

  // ---------- 그림 부품 (3-6) ----------
  K.person = (fill, h) => `<svg viewBox="0 0 120 200" width="${h * 0.6}" height="${h}" aria-hidden="true"><circle cx="60" cy="42" r="34" fill="${fill}"/><path d="M6 198 C6 124 24 90 60 90 C96 90 114 124 114 198 Z" fill="${fill}"/></svg>`;
  K.couple = (parent, cx, top, kind, h, label) => {
    const g = K.el(`<div class="a cx" style="left:${cx}px;top:${top}px;display:grid;justify-items:center;gap:18px"></div>`, parent);
    K.el(`<div style="display:flex;align-items:flex-end;gap:10px">${K.person("#DCE3EE", h)}${K.person("#AEB9CC", h * 0.88)}</div>`, g);
    if (kind !== null) K.el(`<span class="badge k${kind || "N"}">${label || (kind + " 부부")}</span>`, g);
    return g;
  };
  K.one = (parent, cx, top, fill, h, label, labelCls) => {
    const g = K.el(`<div class="a cx" style="left:${cx}px;top:${top}px;display:grid;justify-items:center;gap:14px">${K.person(fill || "#DCE3EE", h)}</div>`, parent);
    if (label) K.el(`<div class="w7 nw ${labelCls || ""}" style="font-size:40px">${label}</div>`, g);
    return g;
  };
  K.stack = (parent, cx, top, width, rows, at, stagger) => {   // 돈 블록 쌓기: rows=[[글자, 높이px, 색]] (위 → 아래)
    const st = K.el(`<div class="stack" style="left:${cx - width / 2}px;top:${top}px;width:${width}px;grid-template-rows:${rows.map(r => r[1] + "px").join(" ")}">${rows.map(r => `<div style="background:${r[2]}">${r[0]}</div>`).join("")}</div>`, parent);
    if (at != null) tl.fromTo(st.children, { scaleY: 0, transformOrigin: "50% 100%" }, { scaleY: 1, duration: 0.5, ease: "power3.out", stagger: stagger == null ? 0.18 : stagger }, at);
    return st;
  };
  K.umbrella = (parent, cx, w, top) => K.el(`<svg class="a" viewBox="0 0 1000 560" width="${w}" height="${w * 0.56}" style="left:${cx - w / 2}px;top:${top == null ? 240 : top}px" aria-hidden="true">
    <path d="M30 300 C80 90 320 20 500 20 C680 20 920 90 970 300 C900 262 820 262 760 300 C700 262 620 262 560 300 C500 262 420 262 360 300 C300 262 220 262 160 300 C100 262 60 268 30 300 Z" fill="#2A3B5E" stroke="#FFD400" stroke-width="6"/>
    <path d="M500 20 L500 520 C500 552 460 552 452 524" fill="none" stroke="#C9D2E2" stroke-width="12" stroke-linecap="round"/></svg>`, parent);
  K.rain = (parent, left, width, at, n, reps) => {
    const rain = K.el(`<div class="a rain" style="left:${left}px;top:120px;width:${width}px;height:760px;overflow:hidden"></div>`, parent);
    const drops = [];
    for (let i = 0; i < n; i++) drops.push(K.el(`<i style="left:${(i * 53) % (width - 10)}px;top:${-80 - (i * 97) % 400}px"></i>`, rain));
    tl.fromTo(rain, { opacity: 0 }, { opacity: 1, duration: 0.4 }, at);
    tl.fromTo(drops, { y: 0 }, { y: 1000, duration: 1.1, ease: "none", stagger: { each: 0.05, repeat: reps == null ? 2 : reps } }, at);
    return rain;
  };
  K.coins = (parent, x, bottom, n, at, cls, each) => {        // 동전 기둥 (가운데 x, 맨 아래 bottom), n 개
    const cs = [];
    for (let m = 0; m < n; m++) cs.push(K.el(`<div class="coin ${cls || ""}" style="left:${x - 43}px;top:${bottom - m * 20}px"></div>`, parent));
    if (at != null) tl.fromTo(cs, { opacity: 0, y: -260 }, { opacity: 1, y: 0, duration: 0.32, ease: "bounce.out", stagger: each == null ? 0.03 : each }, at);
    return cs;
  };
  K.axis = (parent, x0, w, max, top, ticks, at) => {          // 가로 눈금 → {px(v), wd(v)}
    const px = v => x0 + v * w / max, wd = v => v * w / max;
    const ax = K.el(`<div class="axis" style="left:${x0}px;top:${top}px;width:${w}px"></div>`, parent);
    const tk = (ticks || []).map(([v, lab]) => K.el(`<div class="tick" style="left:${px(v)}px;top:${top + 20}px">${lab}</div>`, parent));
    if (at != null) { K.pop(ax, at); tk.forEach(t => K.pop(t, at + 0.1)); }
    return { px, wd, ax, tk };
  };
  K.thr = (parent, x, top, height, label, at, labelTop, drop) => {   // 세로 기준선 (노란 점선) + 이름표
    const line = K.el(`<div class="thr" style="left:${x - 3}px;top:${top}px;height:${height}px"></div>`, parent);
    const lab = label ? K.el(`<div class="a cx w9 Y nw" style="left:${x}px;top:${labelTop == null ? top - 64 : labelTop}px;font-size:46px">${label}</div>`, parent) : null;
    if (at != null) {
      if (drop) tl.fromTo(line, { opacity: 0, y: -120 }, { opacity: 1, y: 0, duration: 0.6, ease: "bounce.out" }, at);
      else K.pop(line, at);
      if (lab) K.pop(lab, at + 0.1);
    }
    return { line, lab };
  };
  K.hthr = (parent, left, y, width, label, at, labelLeft, labelTop) => {   // 가로 기준선
    const line = K.el(`<div class="hthr" style="left:${left}px;top:${y - 3}px;width:${width}px"></div>`, parent);
    const lab = label ? K.el(`<div class="a w9 Y nw" style="left:${labelLeft == null ? left : labelLeft}px;top:${labelTop == null ? y - 66 : labelTop}px;font-size:46px">${label}</div>`, parent) : null;
    if (at != null) { K.pop(line, at, { from: { y: 0 } }); if (lab) K.pop(lab, at + 0.1); }
    return { line, lab };
  };
  K.seg = (parent, left, top, width, color, html, at, dur, h) => {
    const s = K.el(`<div class="seg" style="left:${left}px;top:${top}px;width:${width}px;background:${color};${h ? `height:${h}px` : ""}">${html || ""}</div>`, parent);
    if (at != null) K.grow(s, at, dur || 0.9);
    return s;
  };
  K.vbar = (parent, left, bottom, width, height, color, at, dur) => {
    const b = K.el(`<div class="vbar" style="left:${left}px;top:${bottom - height}px;width:${width}px;height:${height}px;background:${color}"></div>`, parent);
    if (at != null) K.grow(b, at, dur || 1.0, "y");
    return b;
  };
  K.cards = (parent, items, top, at, gap, width, height) => {  // 번호 카드 [[번호, 글자]] — at 은 숫자 또는 시각 배열
    const w = width || 500, g = gap == null ? 60 : gap, n = items.length, x0 = 960 - (n * w + (n - 1) * g) / 2;
    return items.map((it, i) => {
      const c = K.el(`<div class="card3" style="left:${x0 + i * (w + g)}px;top:${top}px;width:${w}px;height:${height || 470}px"><div class="n">${it[0]}</div><div class="t">${it[1]}</div></div>`, parent);
      if (at != null) K.pop(c, Array.isArray(at) ? at[i] : at + i * 0.3);
      return c;
    });
  };
  K.cal = (parent, left, top, head, body, at) => {
    const c = K.el(`<div class="cal" style="left:${left}px;top:${top}px"><div class="h">${head}</div><div class="b">${body || ""}</div></div>`, parent);
    if (at != null) K.pop(c, at);
    return c;
  };
  K.basket = (parent, cx, top, w, label, color) => {          // 바구니 (사람마다 따로 있는 기준) — 노란 점선 = 기준 높이
    const h = w * 0.62;
    return K.el(`<div class="a cx" style="left:${cx}px;top:${top}px;width:${w}px;display:grid;justify-items:center;gap:12px">
      <svg viewBox="0 0 400 250" width="${w}" height="${h}" aria-hidden="true">
        <path d="M30 40 L370 40 L330 240 L70 240 Z" fill="#2A3B5E" stroke="${color || "#C9D2E2"}" stroke-width="8" stroke-linejoin="round"/>
        <path d="M60 110 L340 110 M70 170 L330 170" stroke="rgba(201,210,226,.35)" stroke-width="6"/>
        <line x1="10" y1="40" x2="390" y2="40" stroke="#FFD400" stroke-width="8" stroke-dasharray="22 14"/></svg>
      ${label ? `<div class="w7 nw" style="font-size:40px">${label}</div>` : ""}</div>`, parent);
  };
  K.check = (parent, cx, top, ok, at) => {
    const n = K.el(`<div class="a cx w9 nw" style="left:${cx}px;top:${top}px;font-size:84px;color:${ok ? "#22C7B0" : "#FF4D3D"}">${ok ? "✓" : "✕"}</div>`, parent);
    if (at != null) K.pop(n, at, { from: { scale: 1.4, y: 0 } });
    return n;
  };
  K.years = (parent, left, top, n, color, at, label) => {    // 햇수 칸 (1 2 3 4 5 …)
    const box = K.el(`<div class="a yrs" style="left:${left}px;top:${top}px;color:${color}"></div>`, parent);
    const cells = [];
    for (let i = 0; i < n; i++) cells.push(K.el(`<i>${i + 1}</i>`, box));
    if (label) K.el(`<div class="w9 nw" style="font-size:56px;margin-left:10px">${label}</div>`, box);
    if (at != null) tl.fromTo(box.children, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.3, stagger: 0.18, ease: "back.out(2)" }, at);
    return box;
  };

  // ---------- 장 이름표 · 장 바뀜 카드 (5번) ----------
  K.chapters = list => {                     // [{part, tag, title?, dots:[n,전체]?, card?}]
    for (const c of list) {
      const first = EP.sent.find(s => s.part === c.part);
      if (!first) throw new Error(`파트 '${c.part}' 없음`);
      CHAPTERS.push(Object.assign({ start: first.start, n: first.n }, c));
      if (c.card) {                          // 장이 바뀌는 쉼(1초) 동안 + 첫 문장 앞부분: 다음 장 이름을 크게 한 번
        const card = K.el(`<div class="chapter"><div class="k">${c.tag}</div><div class="t">${c.title || c.part}</div></div>`);
        const a = first.start - 1.0, b = Math.min(first.start + (c.cardHold == null ? 1.6 : c.cardHold), first.end);
        tl.fromTo(card, { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "none" }, Math.max(0, a));
        tl.fromTo(card.children, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out", stagger: 0.1 }, Math.max(0, a));
        tl.to(card, { opacity: 0, duration: 0.35, ease: "none" }, b);
      }
    }
    CHAPTERS.sort((x, y) => x.start - y.start);
  };
  function chipAt(t) {
    if (!chipEl) return;                     // 장 이름표를 끈 영상 (K.init opts.chip=false)
    let c = null;
    for (const x of CHAPTERS) if (t >= x.start - 1.0) c = x;
    if (!c) c = CHAPTERS[0];
    if (!c || chipEl._k === c) return;
    chipEl._k = c;
    chipEl.children[0].textContent = c.tag;
    chipEl.children[1].textContent = c.chip || c.title || c.part;
    const dots = chipEl.children[2];
    dots.innerHTML = c.dots ? Array.from({ length: c.dots[1] }, (_, i) => `<i class="${i < c.dots[0] ? "on" : ""}"></i>`).join("") : "";
  }
  // ---------- 구운 자막 (3-5) — SRT 그대로 ----------
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  function ccAt(t) {
    if (!ccEl) return;                       // 자막을 굽지 않는 영상 (K.init opts.subtitles=false)
    let txt = "";
    for (const [a, b, s] of EP.subs) { if (t >= a && t < b) { txt = s; break; } }
    if (ccEl._t === txt) return;
    ccEl._t = txt;
    ccEl.innerHTML = txt ? txt.split("\n").map(esc).join("<br>") : "";
  }
  K.cut = (t, name) => CUTS.push({ t: +(+t).toFixed(2), name });   // 점검용 대표 장면

  // ---------- 시작·끝 ----------
  K.init = (ep, opts) => {                   // opts: {subtitles: 구운 자막(기본 true), chip: 장 이름표(기본 true)}
    EP = ep;
    OPT = K.opt = Object.assign({ subtitles: true, chip: true }, opts);
    document.body.classList.toggle("render", RENDER);
    stage = document.getElementById("stage");
    tl = K.tl = gsap.timeline({ paused: true });
    chipEl = OPT.chip ? K.el(`<div id="chip"><span class="Y"></span><span></span><span class="dots"></span></div>`) : null;
    ccEl = OPT.subtitles ? K.el(`<div id="cc"></div>`) : null;
    K.D = EP.duration;
  };
  K.done = () => {
    tl.set({}, {}, EP.duration);
    const seek = t => { tl.seek(t, false); chipAt(t); ccAt(t); };
    window.SB = { D: EP.duration, seek, cuts: CUTS, ep: EP.id, estimated: !!EP.estimated, subtitles: !!ccEl, ready: true };
    seek(0);
    if (!RENDER) player(seek);
  };
  function player(seek) {
    const wrap = document.getElementById("wrap");
    const fit = () => { stage.style.transform = `scale(${wrap.clientWidth / 1920})`; };
    addEventListener("resize", fit); fit();
    const audio = EP.audio ? new Audio(EP.audio) : clock(EP.duration);   // 추정 시각(오디오 전)은 소리 없이 시계로
    const ctrl = document.getElementById("ctrl"), now = document.getElementById("now");
    ctrl.innerHTML = `<button id="pp" type="button">▶ 재생</button><span class="time" id="tm">0:00.0</span><input id="sk" type="range" min="0" max="${EP.duration}" step="0.01" value="0" aria-label="재생 위치">`;
    const pp = ctrl.querySelector("#pp"), tm = ctrl.querySelector("#tm"), sk = ctrl.querySelector("#sk");
    const f = t => `${Math.floor(t / 60)}:${(t % 60).toFixed(1).padStart(4, "0")}`;
    const show = t => {
      seek(t); sk.value = t; tm.textContent = `${f(t)} / ${f(EP.duration)}`;
      const s = EP.sent.find(x => t >= x.start - 0.2 && t < x.end + 0.45);
      now.textContent = (EP.estimated ? "[추정 시각 — 오디오 전] " : "") + (s ? `문장 ${s.n} · ${s.part} — ${s.text}` : "");
    };
    let raf = 0;
    const loop = () => { show(audio.currentTime); if (!audio.paused) raf = requestAnimationFrame(loop); };
    pp.onclick = () => { if (audio.paused) { audio.play(); pp.textContent = "❚❚ 멈춤"; loop(); } else { audio.pause(); pp.textContent = "▶ 재생"; cancelAnimationFrame(raf); } };
    sk.oninput = () => { audio.currentTime = +sk.value; show(+sk.value); };
    const q = new URLSearchParams(location.search).get("t");
    show(q ? +q : 0);
    if (q) audio.currentTime = +q;
  }
  function clock(D) {                          // Audio 와 같은 모양(paused·currentTime·play·pause)의 소리 없는 시계
    let t0 = 0, at = 0, paused = true;
    return {
      get paused() { return paused; },
      get currentTime() { return paused ? at : Math.min(D, at + (performance.now() - t0) / 1000); },
      set currentTime(v) { at = +v; t0 = performance.now(); },
      play() { if (paused) { t0 = performance.now(); paused = false; } return Promise.resolve(); },
      pause() { at = this.currentTime; paused = true; },
    };
  }
})();
