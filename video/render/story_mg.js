// VERSION: v1.0 — 2026-10-24 — 새로: '개미 재기 일지' 코드 모션 그래픽 화면 (story.js v1.8 이 부름).
//   사용자 지시 2026-10-24 "비유해서 설명하는 것도 아니고 황소,곰, 바구니 이런건 생성할 필요없어 더 직관적으로 의미 전달 되도록 3D, 모션 그래픽으로
//   표현할 수 있잖아 표현 힘든데 꼭 필요한 것만 이미지 요소로 하라고 다시 수정해" — 비유 그림 대신 뜻을 바로 보여 주는 움직이는 화면:
//   RULE 장 카드 · PHONE 매매 앱(account·margin·delete·lock·chat·news) · CANDLE 하루 급락 + TRADING HALT · TREEMAP 시가총액 블록 ·
//   BOXRANGE 박스권 · RACE 두 선 경주 · GRID 점 그리드(500개 회사 · 202번 중 8번) · FLOW 돈의 흐름 · HIT 악재가 떨어져 급락 ·
//   GAUGE 위험 계기판 · DCA 매달 쌓이는 동전 · SELLBOTTOM 바닥 매도 = 손실 확정.
//   규칙: 숫자·이름표는 장면 표가 준 실제 값만 (선의 굴곡·작은 캔들·블록 크기는 모양을 보여 주는 그림 — 숫자를 붙이지 않음).
//   모든 움직임은 GSAP 타임라인(tl) — 렌더가 아무 시각이나 찍어도 같은 그림. 글자는 36px 이상 · 화면 글자는 screen_words.txt 낱말만.
//   연구·교육용 영상 도구 — 투자 권유 아님.
(function () {
  "use strict";
  // ctx: {V, PANEL, el, pop, tl, at, S, esc, COL, icon, textW, fitP, panel, num, K}
  window.StoryMG = function (ctx) {
    const { V, PANEL, el, pop, tl, at, esc, COL, icon, textW, fitP, panel, K } = ctx;
    const rnd = (i, k) => { const x = Math.sin(i * 12.9898 + k * 78.233) * 43758.5453; return x - Math.floor(x); };
    const SM = 'data-small="그림 안 기호 — 큰 그림의 일부(동전의 ₩)"';
    const svg = (w, h, inner, style) => `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" style="position:absolute;overflow:visible;${style || ""}" ${SM} aria-hidden="true">${inner}</svg>`;
    const pathLen = pts => { let L = 0; for (let i = 1; i < pts.length; i++) L += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); return L; };
    const draw = (node, len, t, dur, ease) => tl.fromTo(node, { strokeDashoffset: len }, { strokeDashoffset: 0, duration: dur, ease: ease || "none" }, t);
    const pct = (a, b) => { const v = (b / a - 1) * 100, r = Math.abs(v) < 10 ? Math.round(v * 10) / 10 : Math.round(v * 10) / 10; return (v > 0 ? "+" : v < 0 ? "−" : "") + String(Math.abs(r)).replace(/\.0$/, "") + "%"; };
    const span = (t0, t1, lo, hi) => Math.max(lo, Math.min(hi, (t1 || t0 + 4) - t0));   // 쓸 수 있는 시간
    const COIN = (r) => `<circle r="${r}" fill="#D9A441" stroke="#F2E6CF" stroke-width="${Math.max(2, r / 6)}"/><text y="${r * 0.38}" font-size="${r * 1.05}" font-weight="900" text-anchor="middle" fill="#1E2A4A">₩</text>`;

    // ---------- RULE n — 장 카드: 노란 고리 안 큰 번호가 뒤집혀 들어오고, 아래 점 n/전체 ----------
    function RULE(sc, s, t0) {
      const n = +s.n, of = +s.of || 5, cx = PANEL.cx, cy = PANEL.top + PANEL.h / 2 - 20;
      const card = el(`<div class="krule" style="left:${cx}px;top:${cy}px"><div class="krl w9 nw">RULE</div><div class="krn w9 nw">${n}</div>` +
        `<div class="krd">${Array.from({ length: of }, (_, i) => `<i class="${i < n ? "on" : ""}${i === n - 1 ? " cur" : ""}"></i>`).join("")}</div></div>`, sc);
      tl.set(card, { xPercent: -50, yPercent: -50 }, 0);               // CSS translate 대신 (움직임이 덮어쓰지 않게)
      tl.fromTo(card, { opacity: 0, rotationY: -90, scale: 0.8, transformPerspective: 900 }, { opacity: 1, rotationY: 0, scale: 1, duration: 0.7, ease: "back.out(1.6)" }, t0);
      tl.fromTo(card.querySelector(".krd i.cur"), { scale: 0.3 }, { scale: 1, duration: 0.5, ease: "back.out(3)" }, t0 + 0.6);
      return t0 + 1.0;
    }

    // ---------- PHONE — 매매 앱 화면 (mode: account·margin·delete·lock·chat·news) ----------
    function PHONE(sc, s, t0, t1) {
      const W = V ? 440 : 430, H = V ? 490 : 580, cx = PANEL.cx + (s.mode === "delete" ? -130 : 0), top = PANEL.top + (PANEL.h - H) / 2;
      const ph = el(`<div class="kphone" style="left:${cx - W / 2}px;top:${top}px;width:${W}px;height:${H}px"><div class="kpsc"></div></div>`, sc);
      const scr = ph.querySelector(".kpsc"), SW = W - 36, SH = H - 70;
      pop(ph, t0, { from: { y: 30, scale: 0.94 } });
      const head = (txt, cls) => el(`<div class="kphd w9 nw ${cls || ""}">${esc(txt)}</div>`, scr);
      const chartPts = (n, y0, y1, seed, wig) => Array.from({ length: n }, (_, i) => {
        const k = i / (n - 1); return [20 + k * (SW - 40), y0 + (y1 - y0) * k + (i && i < n - 1 ? (rnd(i, seed) - 0.5) * wig : 0)];
      });
      const line = (pts, c, w) => { const L = pathLen(pts); return { L, html: `<polyline points="${pts.map(p => p.join(",")).join(" ")}" fill="none" stroke="${c}" stroke-width="${w || 8}" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="${L}" stroke-dashoffset="${L}"/>` }; };
      const buttons = (y) => el(`<div class="kpbt" style="top:${y}px"><span class="b w9 nw">BUY</span><span class="s w9 nw">SELL</span></div>`, scr);
      const T = span(t0, t1, 2, 8);
      if (s.mode === "account" || s.mode === "margin") {
        if (s.mode === "account") head(s.title || "MY ACCOUNT");   // margin 은 MARGIN CALL 알림이 머리 자리
        const from = s.from != null ? ctx.num(s.from) : null, to = s.to != null ? ctx.num(s.to) : null;
        if (from != null) {
          const bal = el(`<div class="kpbal w9 nw" style="color:${to < from ? COL.R : COL.G}">₩</div>`, scr);
          const d = el(`<div class="kpdel w9 nw" style="color:${to < from ? COL.R : COL.G}">${to < from ? "▼" : "▲"} ${pct(from, to).replace(/^[+−]/, "")}</div>`, scr);
          K.counter(bal, from, to, t0 + 0.4, Math.min(2.2, T * 0.5), v => "₩" + Math.round(v).toLocaleString("en-US"));
          pop(d, t0 + 0.4 + Math.min(2.2, T * 0.5));
        }
        const pts = chartPts(9, 40, 210, 3, 46), ln = line(pts, COL.R, 8);
        const ch = el(svg(SW, 240, ln.html, `left:18px;top:${from != null ? 190 : 110}px`), scr);
        draw(ch.querySelector("polyline"), ln.L, t0 + 0.4, Math.min(2.2, T * 0.5));
        const bt = buttons(SH - 92);
        pop(bt, t0 + 0.3);
        if (s.mode === "margin") {
          const ban = el(`<div class="kpban w9 nw">MARGIN CALL</div>`, scr);
          tl.fromTo(ban, { y: -80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.45, ease: "back.out(2)" }, t0 + 0.6);
          tl.to(ban, { opacity: 0.45, duration: 0.18, yoyo: true, repeat: 5, ease: "none" }, t0 + 1.1);
          const sell = bt.querySelector(".s"), tp = t0 + Math.min(2.4, T * 0.55);
          tl.to(sell, { scale: 1.18, duration: 0.2, yoyo: true, repeat: 3, ease: "power1.inOut" }, tp - 0.9);
          tl.to(sell, { scale: 0.86, filter: "brightness(1.6)", duration: 0.12 }, tp);
          tl.to(sell, { scale: 1, duration: 0.25 }, tp + 0.15);
          for (let i = 0; i < 9; i++) {                            // 돈이 앱 밖으로 빠져나감
            const c = el(svg(64, 64, `<g transform="translate(32,32)">${COIN(26)}</g>`, `left:${cx - 32}px;top:${top + H - 160}px`), sc);
            const tx = (V ? 160 : 330) + rnd(i, 7) * 160, ty = -260 - rnd(i, 9) * 160;
            tl.fromTo(c, { x: 0, y: 0, opacity: 0, scale: 0.6 }, { x: tx * (i % 2 ? 1 : 0.7), y: ty, opacity: 1, scale: 1, duration: 0.9, ease: "power2.out" }, tp + 0.1 + i * 0.09);
            tl.to(c, { opacity: 0, duration: 0.3 }, tp + 0.9 + i * 0.09);
          }
          return tp + 1.4;
        }
        return t0 + 0.6 + Math.min(2.2, T * 0.5);
      }
      if (s.mode === "delete") {                                     // 홈 화면 → 차트 앱이 떨며 ✕ → 휴지통으로
        const cols = 3, gs = Math.floor((SW - 60) / cols), cells = [];
        const colors = ["#3E6FB0", "#7A5AA8", "#3E8E87", "#B07A3E", "APP", "#5A6B8C", "#8C5A5A", "#4E8C5A", "#6B6B6B"];
        colors.forEach((c, i) => {
          const x = 30 + (i % cols) * gs, y = 80 + Math.floor(i / cols) * gs;
          const inner = c === "APP" ? `<rect width="${gs - 30}" height="${gs - 30}" rx="24" fill="#10192C" stroke="#F2E6CF" stroke-width="3"/>` +
            [0, 1, 2, 3].map(k => `<rect x="${18 + k * 22}" y="${(gs - 30) / 2 - 20 + (k % 2 ? 10 : -14)}" width="12" height="${k % 2 ? 26 : 40}" fill="${k % 2 ? COL.R : COL.G}"/>`).join("")
            : `<rect width="${gs - 30}" height="${gs - 30}" rx="24" fill="${c}" opacity=".75"/>`;
          cells.push(el(svg(gs - 30, gs - 30, inner, `left:${x}px;top:${y}px`), scr));
        });
        const app = cells[4];
        cells.forEach((c, i) => pop(c, t0 + 0.2 + i * 0.05, { from: { y: 10 } }));
        const tw = t0 + Math.min(1.2, T * 0.18), fd = Math.min(0.8, T * 0.18);   // 짧은 문장이면 빨리 (앱이 휴지통까지 가게)
        tl.to(app, { rotation: 7, duration: 0.07, yoyo: true, repeat: 5, ease: "none" }, tw);
        const x = el(`<div class="kpx w9">✕</div>`, scr); x.style.left = `${30 + gs + gs - 64}px`; x.style.top = `${80 + gs - 20}px`;
        pop(x, tw + 0.2, { from: { scale: 0.3, y: 0 } });
        const tx0 = PANEL.cx + 170, ty0 = top + H - 190;
        const trash = el(svg(150, 170, `<path d="M20 40h110l-12 120H32z" fill="#7B7F8C" stroke="#F2E6CF" stroke-width="4"/><rect x="10" y="22" width="130" height="18" rx="6" fill="#9AA7BF"/><rect x="58" y="6" width="34" height="16" rx="5" fill="#9AA7BF"/><path d="M55 62v80M75 62v80M95 62v80" stroke="#4A4E59" stroke-width="6"/>`, `left:${tx0}px;top:${ty0}px`), sc);
        pop(trash, t0 + 0.3);
        const tf = tw + Math.min(1.0, T * 0.2), ax = (cx - W / 2) + 18 + 30 + gs + (gs - 30) / 2, ay = top + 18 + 80 + gs + (gs - 30) / 2;   // 앱 가운데 (장면 좌표)
        tl.to(app, { x: tx0 + 75 - ax, y: ty0 + 40 - ay, scale: 0.45, rotation: 40, duration: fd, ease: "power2.in" }, tf);
        tl.to(x, { opacity: 0, duration: 0.2 }, tf);
        tl.to(app, { opacity: 0, duration: 0.15 }, tf + fd);
        tl.to(trash, { rotation: -6, duration: 0.1, yoyo: true, repeat: 3 }, tf + fd);
        return tf + fd + 0.4;
      }
      if (s.mode === "lock") {                                       // BUY·SELL 잠금 · HOLD ✓
        head(s.title || "MY ACCOUNT");
        const hold = el(`<div class="kphold w9 nw">✓ HOLD</div>`, scr);
        const bt = el(`<div class="kpbt big" style="top:${SH / 2 - 60}px"><span class="b w9 nw">BUY</span><span class="s w9 nw">SELL</span></div>`, scr);
        pop(bt, t0 + 0.2);
        const lock = el(svg(150, 170, `<rect x="15" y="70" width="120" height="90" rx="14" fill="#D9A441" stroke="#F2E6CF" stroke-width="4"/><path d="M40 70V48a35 35 0 0170 0v22" fill="none" stroke="#F2E6CF" stroke-width="14"/><circle cx="75" cy="112" r="12" fill="#1E2A4A"/>`, `left:${(SW - 150) / 2 + 18}px;top:${SH / 2 - 120}px`), scr);
        const tl0 = t0 + Math.min(1.2, T * 0.3);
        tl.fromTo(lock, { y: -320, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "bounce.out" }, tl0);
        tl.to(bt.children, { opacity: 0.28, filter: "grayscale(1)", duration: 0.3 }, tl0 + 0.5);
        pop(hold, tl0 + 0.8, { from: { scale: 0.6, y: 0 } });
        return tl0 + 1.2;
      }
      if (s.mode === "chat" || s.mode === "news") {
        if (s.mode === "news") head("NEWS");
        const items = (s.items && s.items.length ? s.items : s.mode === "chat" ? ["BUY ▲", "▲ ▲ ▲", "BUY", "BUY ▲"] : ["chip ▲", "chip ▲", "chip ▲"]);
        const step = Math.max(0.3, Math.min(0.8, (T - 1.0) / items.length));
        items.forEach((it, i) => {
          let node;
          if (s.mode === "chat") {
            const right = i % 3 === 2;
            node = el(`<div class="kpchat w9 nw${right ? " me" : ""}" style="top:${40 + i * 108}px">${esc(it)}</div>`, scr);
          } else {
            node = el(`<div class="kpnews" style="top:${84 + i * 140}px">${icon({ k: "chip" }, 84, "k4i")}<div class="kpnl"><i></i><i></i><i class="s"></i></div><span class="w9 G kpup">▲</span></div>`, scr);
          }
          pop(node, t0 + 0.4 + i * step, { from: { y: 24, scale: 0.9 } });
        });
        return t0 + 0.6 + items.length * step;
      }
      return t0 + 0.6;
    }

    // ---------- CANDLE — 작은 캔들들 뒤 하루 큰 빨간 캔들(−drop%) · TRADING HALT + 멈춘 시간 카운트다운 ----------
    function CANDLE(sc, s, t0, t1) {
      const p = panel(sc, "kcandle", "");
      const W = PANEL.w - 80, H = PANEL.h - 120, n = 14, cw = W / (n + 3), base = 140;
      let y = base, html = "";
      for (let i = 0; i < n; i++) {                                   // 모양만 (숫자 없음) — 작은 오르내림
        const up = rnd(i, 3) > 0.45, h = 18 + rnd(i, 5) * 34, y2 = up ? y - h : y + h * 0.8;
        const top = Math.min(y, y2), hh = Math.abs(y2 - y);
        html += `<g class="kc"><line x1="${i * cw + cw / 2}" x2="${i * cw + cw / 2}" y1="${top - 12}" y2="${top + hh + 12}" stroke="${up ? COL.G : COL.R}" stroke-width="4"/><rect x="${i * cw + cw * 0.2}" y="${top}" width="${cw * 0.6}" height="${Math.max(6, hh)}" fill="${up ? COL.G : COL.R}"/></g>`;
        y = y2;
      }
      const drop = +s.drop || 9, bigH = Math.min(H - y - 20, drop * 34), bx = n * cw + cw * 0.5;
      html += `<g class="kcb"><line x1="${bx + cw}" x2="${bx + cw}" y1="${y - 10}" y2="${y + bigH + 16}" stroke="${COL.R}" stroke-width="6"/><rect x="${bx + cw * 0.3}" y="${y}" width="${cw * 1.4}" height="${bigH}" fill="${COL.R}"/></g>`;
      const g = el(svg(W, H, html, "left:40px;top:60px"), p);
      const T = span(t0, t1, 2, 8);
      g.querySelectorAll(".kc").forEach((c, i) => tl.fromTo(c, { opacity: 0 }, { opacity: 1, duration: 0.12 }, t0 + 0.2 + i * Math.min(0.08, T * 0.02)));
      const tb = t0 + 0.4 + n * Math.min(0.08, T * 0.02), big = g.querySelector(".kcb rect");
      tl.fromTo(big, { attr: { height: 0 } }, { attr: { height: bigH }, duration: 0.5, ease: "power3.in" }, tb);
      tl.fromTo(g.querySelector(".kcb line"), { opacity: 0 }, { opacity: 1, duration: 0.2 }, tb + 0.4);
      const lab = el(`<div class="kclab w9 nw" style="left:${40 + bx - 200}px;top:${60 + y + bigH - 70}px;color:${COL.R}">−${drop}%</div>`, p);
      pop(lab, tb + 0.5, { from: { scale: 1.4, y: 0 } });
      if (s.halt) {
        const th = tb + Math.max(0.9, Math.min(1.6, T * 0.3));
        tl.to(g, { opacity: 0.35, duration: 0.3 }, th);
        const st = el(`<div class="khalt w9 nw" style="left:${PANEL.w / 2}px;top:${PANEL.h * 0.46}px"><div>TRADING HALT</div><div class="kht">${String(s.halt).padStart(2, "0")}:00</div></div>`, p);
        tl.set(st, { xPercent: -50, yPercent: -50 }, 0);
        tl.fromTo(st, { scale: 1.6, opacity: 0, rotation: -14 }, { scale: 1, opacity: 1, rotation: -8, duration: 0.35, ease: "power3.in" }, th);
        const clock = st.querySelector(".kht"), o = { v: +s.halt * 60 };
        tl.fromTo(o, { v: +s.halt * 60 }, { v: 0, duration: Math.max(1.0, Math.min(2.4, T - (th - t0) - 0.6)), ease: "none", onUpdate: () => {
          const v = Math.ceil(o.v); clock.textContent = `${String(Math.floor(v / 60)).padStart(2, "0")}:${String(v % 60).padStart(2, "0")}`; } }, th + 0.4);
        return th + 0.6;
      }
      return tb + 0.8;
    }

    // ---------- TREEMAP — 시가총액 블록: 큰 블록(몫 share%) + 작은 블록들 · shake 문장에 큰 블록이 흔들리면 전체가 흔들림 ----------
    function TREEMAP(sc, s, t0, t1) {
      const p = panel(sc, "ktree", "");
      const W = PANEL.w - 60, H = PANEL.h - 60, bw = Math.round(W * (s.share || 55) / 100);
      const big = el(`<div class="ktb" style="left:30px;top:30px;width:${bw - 8}px;height:${H}px">${icon({ k: "chip" }, Math.min(150, bw * 0.35), "k4i")}<div class="ktl w9">${esc(s.big || "")}</div><div class="ktv w9 nw">${esc(s.label || "")}</div></div>`, p);
      const cols = 5, rows = 7, cw2 = (W - bw) / cols, ch2 = H / rows, small = [];
      for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++)
        small.push(el(`<div class="kts" style="left:${30 + bw + c * cw2}px;top:${30 + r * ch2}px;width:${cw2 - 6}px;height:${ch2 - 6}px;opacity:${0.55 + rnd(r * 7 + c, 2) * 0.35}"></div>`, p));
      pop(big, t0 + 0.2, { from: { scale: 0.85, y: 0 } });
      small.forEach((b, i) => tl.fromTo(b, { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(2)" }, t0 + 0.4 + i * 0.015));
      if (s.shake) {
        const ts = at(s.shake[0], s.shake[1]);
        tl.to(big, { x: 10, rotation: 1.2, duration: 0.07, yoyo: true, repeat: 9, ease: "none" }, ts);
        tl.to(small, { x: 6, duration: 0.07, yoyo: true, repeat: 7, ease: "none" }, ts + 0.35);
        tl.to(small, { backgroundColor: "rgba(255,77,61,.75)", duration: 0.3 }, ts + 0.35);
        tl.to(p, { y: 8, duration: 0.08, yoyo: true, repeat: 5, ease: "none" }, ts + 0.5);
      }
      return t0 + 1.2;
    }

    // ---------- BOXRANGE — 박스권: 천장(hi)·바닥(lo) 점선 사이에서 선이 튕김 (첫 해 천장 → 급락 → 되찾음 → 오래 박스) ----------
    function BOXRANGE(sc, s, t0, t1) {
      const p = panel(sc, "kbox", "");
      const W = PANEL.w - 160, H = PANEL.h - 170, x0 = 110, y0 = 50, yh = 110, yl = 200;
      const pts = [[0, 300], [W * 0.1, yh], [W * 0.2, H - 10], [W * 0.33, yh]];   // 첫 천장 → 급락(모양만) → 되찾음
      const n = 9; for (let i = 1; i <= n; i++) pts.push([W * 0.33 + (W * 0.67) * i / n, i % 2 ? yl - rnd(i, 4) * 20 : yh + 4 + rnd(i, 6) * 8]);
      const L = pathLen(pts);
      const box = `<rect x="${W * 0.33}" y="${yh}" width="${W * 0.67}" height="${yl - yh}" fill="rgba(255,212,0,.08)"/>`;
      const g = el(svg(W, H, box + `<line x1="0" x2="${W}" y1="${yh}" y2="${yh}" stroke="${COL.Y}" stroke-width="6" stroke-dasharray="18 12"/><line x1="0" x2="${W}" y1="${yl}" y2="${yl}" stroke="#9AA7BF" stroke-width="4" stroke-dasharray="12 12"/>` +
        `<polyline class="kbl" points="${pts.map(q => q.join(",")).join(" ")}" fill="none" stroke="#F4F6FA" stroke-width="8" stroke-linejoin="round" stroke-dasharray="${L}" stroke-dashoffset="${L}"/>`, `left:${x0}px;top:${y0}px`), p);
      const hi = el(`<div class="kbx w9 nw Y" style="left:16px;top:${y0 + yh - 26}px">${esc(s.hi || "")}</div>`, p);
      const lo = el(`<div class="kbx w9 nw N" style="left:16px;top:${y0 + yl - 26}px">${esc(s.lo || "")}</div>`, p);
      const labs = (s.labels || []).map((l, i, A) => el(`<div class="k3x w9 nw" style="left:${x0 + (A.length > 1 ? i * W / (A.length - 1) : 0)}px">${esc(l)}</div>`, p));
      const T = span(t0, t1, 2, 10), dur = Math.max(1.6, T - 1.2);
      pop(hi, t0 + 0.2); pop(lo, t0 + 0.3); labs.forEach((l, i) => pop(l, t0 + 0.3 + i * 0.1));
      draw(g.querySelector(".kbl"), L, t0 + 0.5, dur);
      // 천장에 닿을 때마다 번쩍
      let acc = 0; pts.forEach((q, i) => { if (i) acc += Math.hypot(q[0] - pts[i - 1][0], q[1] - pts[i - 1][1]); if (q[1] <= yh + 14 && i) tl.fromTo(hi, { scale: 1.35 }, { scale: 1, duration: 0.3 }, t0 + 0.5 + dur * acc / L); });
      return t0 + 0.6 + dur;
    }

    // ---------- RACE — 두 선이 같이 그려짐 · 끝에 이름 + 처음 대비 % (값이 없는 칸 '_' 은 건너뜀) ----------
    function RACE(sc, s, t0, t1) {
      const p = panel(sc, "krace", "");
      const W = PANEL.w - 220, H = PANEL.h - 190, all = s.series.flatMap(x => x.v.filter(v => v != null));
      const lo = Math.min(...all, 100), hi = Math.max(...all, 100), n = Math.max(...s.series.map(x => x.v.length));
      const px = i => 20 + i * (W - 40) / Math.max(1, n - 1), py = v => 20 + (hi - v) / (hi - lo || 1) * (H - 40);
      const cols = [COL.N || "#9AA7BF", COL.G, COL.R];
      let html = `<line x1="0" x2="${W}" y1="${py(100)}" y2="${py(100)}" stroke="${COL.Y}" stroke-width="5" stroke-dasharray="16 12"/>`;
      const ends = [];
      s.series.forEach((x, k) => {
        const pts = x.v.map((v, i) => v == null ? null : [px(i), py(v)]).filter(Boolean), L = pathLen(pts);
        const last = x.v.filter(v => v != null).slice(-1)[0], first = x.v.find(v => v != null);
        const c = last < first ? COL.R : last > first ? COL.G : "#C9D1E0";
        html += `<polyline class="krl${k}" points="${pts.map(q => q.join(",")).join(" ")}" fill="none" stroke="${c}" stroke-width="${k ? 10 : 8}" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="${L}" stroke-dashoffset="${L}"/>`;
        const hide = /!$/.test(x.name);                         // 이름 끝 '!' = % 를 붙이지 않음 (끝 값을 모를 때)
        ends.push({ L, c, name: x.name.replace(/!$/, ""), d: hide ? "" : pct(first, last), y: pts[pts.length - 1][1] });
      });
      const g = el(svg(W, H, html, "left:40px;top:50px"), p);
      const labs = (s.labels || []).map((l, i, A) => el(`<div class="k3x w9 nw" style="left:${40 + (A.length === n ? px(i) : 20 + i * (W - 40) / Math.max(1, A.length - 1))}px">${esc(l)}</div>`, p));
      const T = span(t0, t1, 1.6, 8), dur = Math.max(1.0, Math.min(3.2, T - 1.4));
      labs.forEach((l, i) => pop(l, t0 + 0.2 + i * 0.08));
      // 끝 이름표가 겹치지 않게 위아래로 벌림
      const ys = ends.map(e => e.y); if (ys.length === 2 && Math.abs(ys[0] - ys[1]) < 90) { const m = (ys[0] + ys[1]) / 2; ends[ys[0] < ys[1] ? 0 : 1].y = m - 48; ends[ys[0] < ys[1] ? 1 : 0].y = m + 48; }
      ends.forEach((e, k) => {
        draw(g.querySelector(`.krl${k}`), e.L, t0 + 0.4, dur, "power1.inOut");
        const lab = el(`<div class="krend w9 nw" style="right:18px;top:${Math.max(4, 50 + e.y - 84)}px;color:${e.c}"><span>${esc(e.name)}</span> ${esc(e.d)}</div>`, p);
        pop(lab, t0 + 0.5 + dur, { from: { x: -20, y: 0 } });
      });
      return t0 + 0.8 + dur;
    }

    // ---------- GRID — 점 그리드: n칸이 물결처럼 채워짐 · red= 몇 칸 빨강(+ ✓/✕ 셈) · fail=문장 에 가운데 한 칸이 무너져 떨어짐 ----------
    function GRID(sc, s, t0, t1) {
      const p = panel(sc, "kgrid", "");
      const n = +s.n, red = +s.red || 0, W = PANEL.w - 100, H = PANEL.h - (red ? 190 : 110);
      const cols = Math.ceil(Math.sqrt(n * W / H)), rows = Math.ceil(n / cols), cs = Math.min(W / cols, H / rows), gap = Math.max(2, cs * 0.18);
      const ox = 50 + (W - cols * cs) / 2, oy = 50 + (H - rows * cs) / 2;
      let html = "";
      const redIdx = new Set(); for (let i = 0; redIdx.size < red; i++) redIdx.add(Math.floor(rnd(i, 11) * n));
      for (let i = 0; i < n; i++) html += `<rect class="kgd" data-i="${i}" x="${(i % cols) * cs}" y="${Math.floor(i / cols) * cs}" width="${cs - gap}" height="${cs - gap}" rx="${cs * 0.2}" fill="${COL.G}"/>`;
      const g = el(svg(cols * cs, rows * cs, html, `left:${ox}px;top:${oy}px`), p);
      const cells = [...g.querySelectorAll(".kgd")], T = span(t0, t1, 1.6, 8), wave = Math.min(1.4, T * 0.4);
      cells.forEach((c, i) => { const r = Math.floor(i / cols), k = i % cols; tl.fromTo(c, { opacity: 0 }, { opacity: 1, duration: 0.2 }, t0 + 0.3 + wave * (r + k) / (rows + cols)); });
      let end = t0 + 0.5 + wave;
      if (red) {
        const rs = Math.min(1.4, T * 0.3) / red;                    // 빨간 칸을 다 칠하는 데 1.4초 안
        [...redIdx].forEach((i, j) => tl.to(cells[i], { attr: { fill: COL.R }, duration: 0.15 }, end + j * rs));
        end += red * rs + 0.2;
        const ok = el(`<div class="kgc w9 nw" style="left:${PANEL.w / 2 - 260}px;color:${COL.G}">✓ ${n - red}</div>`, p);
        const bad = el(`<div class="kgc w9 nw" style="left:${PANEL.w / 2 + 60}px;color:${COL.R}">✕ ${red}</div>`, p);
        pop(ok, end); pop(bad, end + 0.15); end += 0.5;
      }
      if (s.fail) {
        const tf = at(s.fail[0], s.fail[1]), c = cells[Math.floor(n / 2) + Math.floor(cols / 2) - cols * 2];
        tl.to(c, { attr: { fill: COL.R }, duration: 0.2 }, tf);
        tl.to(c, { y: 6, duration: 0.06, yoyo: true, repeat: 5 }, tf + 0.2);
        tl.to(c, { y: 700, rotation: 50, opacity: 0, duration: 1.0, ease: "power2.in", transformOrigin: "50% 50%" }, tf + 0.6);
        end = Math.max(end, tf + 1.6);
      }
      return end;
    }

    // ---------- FLOW — 돈의 흐름: 왼쪽 → 오른쪽으로 동전이 계속 흘러감 (label = 흐름 위 글) ----------
    function FLOW(sc, s, t0, t1) {
      const p = panel(sc, "kflow", "", fitP(Math.min(PANEL.h, 420)));
      const P = { w: PANEL.w, h: Math.min(PANEL.h, 420) }, box = x => x.t != null ? `<span class="k5t w9 nw" style="font-size:${Math.max(44, Math.min(64, Math.floor(300 / (textW(x.t) + 1))))}px">${esc(x.t)}</span>` : icon(x, 150);
      const L = el(`<div class="kfl" style="top:${P.h / 2 - 50}px">${box(s.from)}</div>`, p), R = el(`<div class="kfr" style="top:${P.h / 2 - 50}px">${box(s.to)}</div>`, p);
      const lab = s.label ? el(`<div class="kflab w9 nw">${esc(s.label)}</div>`, p) : null;
      pop(L, t0 + 0.1); pop(R, t0 + 0.25); if (lab) pop(lab, t0 + 0.4);
      const T = span(t0, t1, 1.6, 9), x0 = 230, x1 = P.w - 230, yb = P.h / 2 + 30;
      for (let i = 0; i < 10; i++) {
        const c = el(svg(70, 70, `<g transform="translate(35,35)">${COIN(28)}</g>`, `left:${x0 - 35}px;top:${yb - 35}px`), p);
        const ts = t0 + 0.5 + i * Math.max(0.15, (T - 1.6) / 10);
        tl.fromTo(c, { x: 0, y: 0, opacity: 0, scale: 0.7 }, { x: x1 - x0, opacity: 1, scale: 1, duration: 0.9, ease: "power1.inOut" }, ts);
        tl.fromTo(c, { y: 0 }, { y: -90, duration: 0.45, ease: "power1.out", yoyo: true, repeat: 1 }, ts);
        tl.to(c, { opacity: 0, duration: 0.15 }, ts + 0.85);
      }
      tl.to(R, { scale: 1.08, duration: 0.25, yoyo: true, repeat: 3 }, t0 + 1.2);
      return t0 + 1.4;
    }

    // ---------- HIT — 오르던 차트 위로 악재 칩이 하나씩 떨어지고, 마지막에 급락 ----------
    function HIT(sc, s, t0, t1) {
      const p = panel(sc, "khit", "");
      const W = PANEL.w - 120, H = PANEL.h - 120, up = [[0, H - 60], [W * 0.2, H - 130], [W * 0.38, H - 150], [W * 0.55, H - 260], [W * 0.68, 120]];
      const dn = [up[up.length - 1], [W * 0.78, H * 0.55], [W * 0.88, H - 90], [W - 10, H - 20]];
      const L1 = pathLen(up), L2 = pathLen(dn);
      const g = el(svg(W, H, `<polyline class="h1" points="${up.map(q => q.join(",")).join(" ")}" fill="none" stroke="${COL.G}" stroke-width="9" stroke-linejoin="round" stroke-dasharray="${L1}" stroke-dashoffset="${L1}"/>` +
        `<polyline class="h2" points="${dn.map(q => q.join(",")).join(" ")}" fill="none" stroke="${COL.R}" stroke-width="10" stroke-linejoin="round" stroke-dasharray="${L2}" stroke-dashoffset="${L2}"/>`, "left:60px;top:70px"), p);
      const T = span(t0, t1, 2, 9);
      draw(g.querySelector(".h1"), L1, t0 + 0.3, Math.min(1.2, T * 0.25));
      const items = s.icons.filter(x => !x.arrow), step = Math.max(0.35, Math.min(0.9, (T - 2.2) / items.length));
      let th = t0 + 0.4 + Math.min(1.2, T * 0.25);
      items.forEach((x, i) => {
        const node = el(`<div class="khi" style="left:${60 + W * (0.12 + i * 0.76 / Math.max(1, items.length))}px;top:24px">${x.t != null ? `<span class="k5t w9 nw" style="font-size:54px;border-color:${COL.R};color:#FF8A7E">${esc(x.t)}</span>` : icon(x, 120)}</div>`, p);
        tl.fromTo(node, { y: -260, opacity: 0 }, { y: 0, opacity: 1, duration: 0.45, ease: "power3.in" }, th + i * step);
        tl.to(p, { y: 10, duration: 0.06, yoyo: true, repeat: 3, ease: "none" }, th + i * step + 0.45);
      });
      const tc = th + items.length * step + 0.1;
      draw(g.querySelector(".h2"), L2, tc, 0.7, "power2.in");
      return tc + 0.9;
    }

    // ---------- GAUGE — 위험 계기판: 바늘이 value(0~100) 로 (70 넘으면 빨갛게 깜빡임) ----------
    function GAUGE(sc, s, t0) {
      const p = panel(sc, "kgauge", "");
      const R = Math.min(PANEL.w / 2 - 80, PANEL.h - 170), cx = PANEL.w / 2, cy = PANEL.h - 90, sw = 70;
      const arc = (a0, a1, c) => { const p0 = [cx + R * Math.cos(Math.PI * (1 - a0)), cy - R * Math.sin(Math.PI * (1 - a0))], p1 = [cx + R * Math.cos(Math.PI * (1 - a1)), cy - R * Math.sin(Math.PI * (1 - a1))];
        return `<path d="M${p0[0]} ${p0[1]} A${R} ${R} 0 0 1 ${p1[0]} ${p1[1]}" fill="none" stroke="${c}" stroke-width="${sw}"/>`; };
      const g = el(svg(PANEL.w, PANEL.h, arc(0, 0.4, COL.G) + arc(0.4, 0.7, COL.Y) + arc(0.7, 1, COL.R) +
        `<g class="kneedle"><line x1="${cx}" y1="${cy}" x2="${cx - R + 40}" y2="${cy}" stroke="#F4F6FA" stroke-width="14" stroke-linecap="round"/></g><circle cx="${cx}" cy="${cy}" r="26" fill="#F4F6FA"/>`, "left:0;top:0"), p);
      const ndl = g.querySelector(".kneedle"), v = Math.max(0, Math.min(100, +s.value));
      tl.set(ndl, { svgOrigin: `${cx} ${cy}`, rotation: 0 }, 0);
      tl.to(ndl, { rotation: 180 * v / 100, duration: 1.2, ease: "back.out(1.4)" }, t0 + 0.4);
      if (v >= 70) tl.to(g.querySelectorAll("path")[2], { opacity: 0.35, duration: 0.2, yoyo: true, repeat: 5 }, t0 + 1.6);
      return t0 + 1.8;
    }

    // ---------- DCA — 매달 정해진 금액: 달력 숫자 1 → months · 동전이 떨어져 쌓임 · amount 가 있으면 '금액 × 달' ----------
    function DCA(sc, s, t0, t1) {
      const p = panel(sc, "kdca", "");
      const months = +s.months || 12, T = span(t0, t1, 2, 9), dur = Math.max(1.2, T - 1.2);
      const cal = el(`<div class="kcal" style="top:${PANEL.h / 2 - 150}px">${icon({ k: "calendar" }, 150, "k4i")}<div class="kcaln w9 nw Y">1</div></div>`, p);
      pop(cal, t0 + 0.1);
      K.counter(cal.querySelector(".kcaln"), 1, months, t0 + 0.4, dur, v => String(Math.round(v)));
      const drops = Math.min(14, months), sx = PANEL.w * 0.62, base = PANEL.h - (s.amount ? 150 : 70);
      for (let i = 0; i < drops; i++) {
        const c = el(svg(110, 40, `<ellipse cx="55" cy="20" rx="50" ry="16" fill="#D9A441" stroke="#F2E6CF" stroke-width="4"/>`, `left:${sx - 55}px;top:${base - 30 - i * 22}px`), p);
        tl.fromTo(c, { y: -320, opacity: 0 }, { y: 0, opacity: 1, duration: 0.35, ease: "power2.in" }, t0 + 0.4 + dur * i / drops);
      }
      if (s.amount) { const a = el(`<div class="kdcaa w9 nw G">${esc(s.amount)} × ${months}</div>`, p); pop(a, t0 + 0.6 + dur * 0.6); }
      return t0 + 0.6 + dur;
    }

    // ---------- SELLBOTTOM — 떨어지는 선의 바닥에서 SELL → 자물쇠(손실 확정) · 그 뒤 회복은 회색 점선 (내 몫이 아님) ----------
    function SELLBOTTOM(sc, s, t0, t1) {
      const p = panel(sc, "ksell", "");
      const W = PANEL.w - 120, H = PANEL.h - 140, dn = [[0, 30], [W * 0.15, 80], [W * 0.28, 60], [W * 0.45, H - 30]];
      const upP = [dn[dn.length - 1], [W * 0.62, H * 0.55], [W * 0.78, H * 0.35], [W - 10, 30]];
      const L1 = pathLen(dn), L2 = pathLen(upP);
      const g = el(svg(W, H, `<line x1="0" x2="${W}" y1="30" y2="30" stroke="${COL.Y}" stroke-width="5" stroke-dasharray="16 12"/>` +
        `<polyline class="s1" points="${dn.map(q => q.join(",")).join(" ")}" fill="none" stroke="${COL.R}" stroke-width="10" stroke-linejoin="round" stroke-dasharray="${L1}" stroke-dashoffset="${L1}"/>` +
        `<polyline class="s2" points="${upP.map(q => q.join(",")).join(" ")}" fill="none" stroke="#9AA7BF" stroke-width="7" stroke-dasharray="4 18" stroke-linecap="round" opacity="0"/>`, "left:60px;top:60px"), p);
      const T = span(t0, t1, 2, 8), d1 = Math.min(1.3, T * 0.3);
      draw(g.querySelector(".s1"), L1, t0 + 0.3, d1, "power1.in");
      const bx = 60 + W * 0.45, by = 60 + H - 30;
      const tag = el(`<div class="kstag w9 nw" style="left:${bx - 100}px;top:${by - 140}px">SELL</div>`, p);
      pop(tag, t0 + 0.4 + d1, { from: { scale: 1.6, y: 0 } });
      const lock = el(`<div class="kslock" style="left:${bx - 210}px;top:${by - 60}px">${icon({ k: "lock" }, 96, "k4i")}<span class="w9 nw R">${esc(s.end || "")}</span></div>`, p);
      pop(lock, t0 + 0.8 + d1, { from: { y: -40 } });
      tl.to(g.querySelector(".s2"), { opacity: 1, duration: 0.3 }, t0 + 1.3 + d1);
      tl.fromTo(g.querySelector(".s2"), { strokeDashoffset: 200 }, { strokeDashoffset: 0, duration: 1.2, ease: "none" }, t0 + 1.3 + d1);
      return t0 + 2.6 + d1;
    }

    return { RULE, PHONE, CANDLE, TREEMAP, BOXRANGE, RACE, GRID, FLOW, HIT, GAUGE, DCA, SELLBOTTOM };
  };
})();
