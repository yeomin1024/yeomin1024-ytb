// VERSION: v1.0 — 2026-10-26 — 주식 심리 테스트 편 코드 그림 (ChatGPT 그림이 오기 전 같은 자리 · 같은 이름 — puppet.js v1.2 spec.draw).
//   사용자 지시 2026-10-26 "썸네일과 영상 만들어봐" — 그림 요청(stock/source/simri-test-2026-10/images_chatgpt.md) 중 아직 없는 것:
//   주인공 = 표정 있는 흰둥이(시청자 자신) 7가지 모습 · 얼굴 없는 흰둥이 '낯선 사람' · 소품 쥐덫·달걀 바구니·새는 양동이.
//   화풍은 다시 쓰는 옛 그림(W-CROWD 등 — 흰 종이 머리·회색 겉옷·크림 테두리)에 맞춤: 종이 겹(크림 테두리 7px) + 겹 그림자 + 한지 결(같은 씨앗 —
//   렌더 일꾼마다 같은 그림). 1024×1024 캔버스 · 위·아래·양옆 8% 넘게 비움 (puppet.js 가 알파 상자로 자름). 그림 안에 글자·숫자 없음.
//   연구·교육용 영상 — 투자 권유 아님.
(function () {
  "use strict";
  const C = { cream: "#F2E6CF", white: "#F7F3EA", shade: "#E4DED2", gray: "#B9C0CC", gray2: "#9AA3B2", navy: "#1B2440", pants: "#2E3A57",
    shoe: "#2B2B2B", scarf: "#A9C1D9", cheek: "rgba(236,150,140,.55)", teal: "#1FA79A", red: "#D92B2B", yellow: "#F2C230", gold: "#E9B832",
    goldD: "#B8871B", coat: "#2B2B2B", coat2: "#3A3A3F", wood: "#C9A46A", woodL: "#DDBE86", woodD: "#A9824A", metal: "#8A8F98", slate: "#3A4A6B", slateL: "#5B6E92" };
  let seed = 7;
  const rnd = () => { seed = (seed * 16807) % 2147483647; return seed / 2147483647; };

  // ---------- 종이 겹 ----------
  // parts: [{d: g => 경로, fill, line: 굵기(선이면)}] — 1차: 크림 테두리 · 2차: 색 + 겹 그림자
  function paper(g, parts, border) {
    const b = border == null ? 7 : border;
    g.save(); g.lineJoin = "round"; g.lineCap = "round";
    for (const p of parts) {
      g.beginPath(); p.d(g); g.strokeStyle = C.cream; g.fillStyle = C.cream;
      if (p.line) { g.lineWidth = p.line + 2 * b; g.stroke(); } else { g.lineWidth = 2 * b; g.fill(); g.stroke(); }
    }
    for (const p of parts) {
      g.save(); g.shadowColor = "rgba(20,24,40,.22)"; g.shadowBlur = 6; g.shadowOffsetX = 2; g.shadowOffsetY = 4;
      g.beginPath(); p.d(g);
      if (p.line) { g.strokeStyle = p.fill; g.lineWidth = p.line; g.stroke(); } else { g.fillStyle = p.fill; g.fill(); }
      g.restore();
    }
    g.restore();
  }
  function grain(g, w, h) {                                          // 한지 결 (그린 곳에만)
    const n = document.createElement("canvas"); n.width = n.height = 128;
    const ng = n.getContext("2d"), id = ng.createImageData(128, 128);
    seed = 11;
    for (let i = 0; i < id.data.length; i += 4) { const v = rnd() < 0.5 ? 0 : 255; id.data[i] = id.data[i + 1] = id.data[i + 2] = v; id.data[i + 3] = rnd() * 22; }
    ng.putImageData(id, 0, 0);
    g.save(); g.globalCompositeOperation = "source-atop"; g.fillStyle = g.createPattern(n, "repeat"); g.fillRect(0, 0, w, h); g.restore();
  }
  const circ = (x, y, r) => g => g.arc(x, y, r, 0, Math.PI * 2);
  const ell = (x, y, rx, ry, rot) => g => g.ellipse(x, y, rx, ry, rot || 0, 0, Math.PI * 2);
  const poly = pts => g => { g.moveTo(pts[0][0], pts[0][1]); for (let i = 1; i < pts.length; i++) g.lineTo(pts[i][0], pts[i][1]); };
  const rr = (x, y, w, h, r) => g => g.roundRect(x, y, w, h, r);
  const bez = (pts) => g => { g.moveTo(pts[0][0], pts[0][1]); g.bezierCurveTo(pts[1][0], pts[1][1], pts[2][0], pts[2][1], pts[3][0], pts[3][1]); };

  // ---------- 흰둥이 몸 (서 있음) ----------
  // o: {arms: [[어깨, 팔꿈치, 손], …], body: 겉옷 색, legs: true, coat: 긴 코트, behind: 몸 뒤 부품, front: 손 앞 부품, hands: 손 색}
  function standing(o) {
    const parts = [], col = o.body || C.gray;
    if (o.behind) parts.push(...o.behind);
    if (o.legs !== false) {
      parts.push({ d: rr(446, 700, 58, 200, 26), fill: C.pants }, { d: rr(520, 700, 58, 200, 26), fill: C.pants });
      parts.push({ d: ell(468, 904, 54, 26), fill: C.shoe }, { d: ell(556, 904, 54, 26), fill: C.shoe });
    }
    const torso = g => { g.moveTo(400, 455); g.quadraticCurveTo(512, 420, 624, 455); g.quadraticCurveTo(660, 470, 652, 540); g.lineTo(630, o.coat ? 860 : 740);
      g.quadraticCurveTo(512, o.coat ? 880 : 760, 394, o.coat ? 860 : 740); g.lineTo(372, 540); g.quadraticCurveTo(364, 470, 400, 455); g.closePath(); };
    parts.push({ d: torso, fill: col });
    if (!o.coat) parts.push({ d: rr(492, 462, 40, 270, 16), fill: C.white });
    for (const a of o.arms || []) parts.push({ d: g => { g.moveTo(a[0][0], a[0][1]); g.quadraticCurveTo(a[1][0], a[1][1], a[2][0], a[2][1]); }, fill: col, line: 54 });
    return parts;
  }
  const hands = (arms, col) => (arms || []).map(a => ({ d: circ(a[2][0], a[2][1], 31), fill: col || C.white }));
  const scarf = (dx) => [{ d: poly([[452 + dx, 440], [572 + dx, 440], [512 + dx, 512]]), fill: C.scarf }, { d: circ(512 + dx, 446, 20), fill: C.scarf }];
  const head = (cx, cy, r) => ({ d: circ(cx, cy, r || 118), fill: C.white });

  // ---------- 얼굴 (주인공만) ----------
  // e: {eyes: dot|arc|wide|shut|look, look:[dx,dy], brows: up|knit|worried|flat|one, mouth: smile|grin|o|flat|down|small, sweat}
  function face(g, cx, cy, e) {
    const ex = 44, ey = -6;
    g.save(); g.lineCap = "round"; g.lineJoin = "round"; g.strokeStyle = C.navy; g.fillStyle = C.navy;
    g.fillStyle = C.cheek; [-1, 1].forEach(s => { g.beginPath(); g.ellipse(cx + s * 70, cy + 34, 24, 15, 0, 0, Math.PI * 2); g.fill(); });
    g.fillStyle = C.navy; g.strokeStyle = C.navy;
    const lk = e.look || [0, 0];
    [-1, 1].forEach(s => {
      const x = cx + s * ex, y = cy + ey;
      if (e.eyes === "arc") { g.lineWidth = 10; g.beginPath(); g.arc(x, y + 8, 18, Math.PI * 1.1, Math.PI * 1.9); g.stroke(); }
      else if (e.eyes === "shut") { g.lineWidth = 9; g.beginPath(); g.arc(x, y - 10, 18, Math.PI * 0.15, Math.PI * 0.85); g.stroke(); }
      else if (e.eyes === "wide") { g.fillStyle = "#FFFFFF"; g.beginPath(); g.arc(x, y, 26, 0, Math.PI * 2); g.fill(); g.lineWidth = 5; g.stroke(); g.fillStyle = C.navy; g.beginPath(); g.arc(x + lk[0], y + lk[1], 10, 0, Math.PI * 2); g.fill(); }
      else { g.beginPath(); g.ellipse(x + lk[0], y + lk[1], 14, 20, 0, 0, Math.PI * 2); g.fill(); g.fillStyle = "#FFFFFF"; g.beginPath(); g.arc(x + lk[0] + 5, y + lk[1] - 7, 5, 0, Math.PI * 2); g.fill(); g.fillStyle = C.navy; }
    });
    g.lineWidth = 9;
    const bw = (s, inner, outer) => { g.beginPath(); g.moveTo(cx + s * (ex - 22), cy - 42 + inner); g.quadraticCurveTo(cx + s * ex, cy - 52 + Math.min(inner, outer) - 4, cx + s * (ex + 24), cy - 42 + outer); g.stroke(); };
    ({ up: () => [-1, 1].forEach(s => bw(s, -16, -14)), knit: () => [-1, 1].forEach(s => bw(s, 8, -10)), worried: () => [-1, 1].forEach(s => bw(s, -14, 6)),
       flat: () => [-1, 1].forEach(s => bw(s, 0, 0)), one: () => { bw(-1, -14, -10); bw(1, 6, -4); } })[e.brows || "flat"]();
    const my = cy + 52;
    g.lineWidth = 9;
    if (e.mouth === "grin") { g.beginPath(); g.moveTo(cx - 44, my - 8); g.quadraticCurveTo(cx, my + 58, cx + 44, my - 8); g.closePath(); g.fill(); g.fillStyle = "#E7837A"; g.beginPath(); g.ellipse(cx, my + 22, 20, 10, 0, 0, Math.PI * 2); g.fill(); }
    else if (e.mouth === "o") { g.beginPath(); g.ellipse(cx, my + 6, 13, 17, 0, 0, Math.PI * 2); g.fill(); }
    else if (e.mouth === "flat") { g.beginPath(); g.moveTo(cx - 20, my + 4); g.lineTo(cx + 18, my + 2); g.stroke(); }
    else if (e.mouth === "down") { g.beginPath(); g.arc(cx, my + 26, 24, Math.PI * 1.2, Math.PI * 1.8); g.stroke(); }
    else if (e.mouth === "small") { g.beginPath(); g.arc(cx, my - 6, 16, Math.PI * 0.2, Math.PI * 0.8); g.stroke(); }
    else { g.beginPath(); g.arc(cx, my - 14, 30, Math.PI * 0.18, Math.PI * 0.82); g.stroke(); }
    if (e.sweat) { g.fillStyle = "#BFD7EE"; g.beginPath(); g.moveTo(cx + 150, cy - 70); g.quadraticCurveTo(cx + 176, cy - 26, cx + 150, cy - 14); g.quadraticCurveTo(cx + 124, cy - 26, cx + 150, cy - 70); g.fill(); }
    g.restore();
  }
  const phone = (x, y, w, h, rot) => ({ d: g => { g.save(); g.translate(x, y); g.rotate(rot || 0); g.roundRect(-w / 2, -h / 2, w, h, 16); g.restore(); }, fill: "#2B3550" });

  // ---------- 주인공 모습 7 ----------
  const HERO = {
    PHONE: g => {
      const arms = [[[400, 478], [372, 610], [474, 572]], [[624, 478], [652, 610], [552, 572]]];
      paper(g, [...standing({ arms }), phone(512, 548, 104, 166, -0.04), ...hands(arms), ...scarf(-14), head(498, 332)]);
      face(g, 480, 336, { eyes: "dot", look: [0, 8], brows: "up", mouth: "small" });
    },
    THINK: g => {
      const arms = [[[396, 480], [420, 640], [608, 614]], [[628, 478], [700, 590], [560, 448]]];
      paper(g, [...standing({ arms: [arms[0]] }), ...hands([arms[0]]), ...scarf(10), head(522, 330), ...standing({ arms: [arms[1]], legs: false }).slice(-1), ...hands([arms[1]])]);
      face(g, 536, 330, { eyes: "dot", look: [-6, -9], brows: "one", mouth: "flat" });
    },
    SHOCK: g => {
      g.save(); g.translate(512, 910); g.rotate(-0.09); g.translate(-512, -910);
      const arms = [[[400, 480], [340, 600], [470, 546]], [[624, 480], [684, 600], [556, 546]]];
      paper(g, [...standing({ arms }), phone(512, 548, 100, 150, 0), ...hands(arms), ...scarf(0), head(512, 330)]);
      face(g, 512, 330, { eyes: "wide", look: [0, 2], brows: "up", mouth: "o", sweat: true });
      g.restore();
    },
    DESPAIR: g => {
      const parts = [
        { d: ell(386, 884, 56, 26), fill: C.shoe }, { d: ell(640, 884, 56, 26), fill: C.shoe },
        { d: g => { g.moveTo(360, 600); g.quadraticCurveTo(512, 560, 664, 600); g.lineTo(690, 870); g.quadraticCurveTo(512, 900, 334, 870); g.closePath(); }, fill: C.gray },
        { d: rr(372, 742, 282, 140, 66), fill: C.pants },
      ];
      const arms = [[[392, 616], [304, 540], [418, 452]], [[632, 616], [720, 540], [606, 452]]];
      for (const a of arms) parts.push({ d: g => { g.moveTo(a[0][0], a[0][1]); g.quadraticCurveTo(a[1][0], a[1][1], a[2][0], a[2][1]); }, fill: C.gray, line: 52 });
      parts.push(...scarf(0).map(p => ({ d: g => { g.save(); g.translate(0, 132); p.d(g); g.restore(); }, fill: p.fill })), head(512, 470, 112), ...hands(arms));
      paper(g, parts);
      face(g, 512, 486, { eyes: "shut", brows: "worried", mouth: "down" });
    },
    PLAN: g => {
      const armL = [[400, 480], [372, 640], [452, 640]], armR = [[626, 480], [676, 620], [598, 600]];
      const board = [{ d: rr(330, 470, 210, 260, 14), fill: "#8A6A44" }, { d: rr(344, 490, 182, 226, 8), fill: "#FBF6EA" }, { d: rr(400, 458, 70, 30, 8), fill: C.metal }];
      paper(g, [...standing({ arms: [armR] }), ...hands([armR]), { d: g => { g.moveTo(598, 600); g.lineTo(548, 548); }, fill: C.yellow, line: 14 }, ...scarf(-12), head(500, 330),
        ...board, ...standing({ arms: [armL], legs: false }).slice(-1), ...hands([armL])]);
      g.save(); g.lineWidth = 6; g.strokeStyle = C.slate; g.lineCap = "round"; g.lineJoin = "round";
      for (let i = 0; i < 4; i++) { const y = 512 + i * 48; g.strokeRect(366, y, 30, 30); g.beginPath(); g.moveTo(410, y + 16); g.lineTo(500, y + 16); g.globalAlpha = 0.35; g.stroke(); g.globalAlpha = 1;
        if (i < 3) { g.strokeStyle = C.teal; g.lineWidth = 8; g.beginPath(); g.moveTo(370, y + 14); g.lineTo(381, y + 26); g.lineTo(402, y - 2); g.stroke(); g.strokeStyle = C.slate; g.lineWidth = 6; } }
      g.restore();
      face(g, 484, 334, { eyes: "dot", brows: "flat", mouth: "smile" });
    },
    BOW: g => {
      paper(g, [{ d: rr(476, 700, 70, 200, 30), fill: C.pants }, { d: ell(500, 904, 66, 26), fill: C.shoe }]);
      g.save(); g.translate(512, 720); g.rotate(-0.72); g.translate(-512, -720);
      const arms = [[[470, 500], [452, 620], [500, 700]]];
      paper(g, [{ d: g => { g.moveTo(420, 455); g.quadraticCurveTo(512, 430, 600, 455); g.lineTo(612, 740); g.quadraticCurveTo(512, 760, 410, 740); g.closePath(); }, fill: C.gray },
        ...scarf(-20), head(500, 330), { d: arms[0] && (g => { g.moveTo(arms[0][0][0], arms[0][0][1]); g.quadraticCurveTo(arms[0][1][0], arms[0][1][1], arms[0][2][0], arms[0][2][1]); }), fill: C.gray2, line: 50 }, ...hands(arms)]);
      face(g, 452, 336, { eyes: "arc", brows: "flat", mouth: "smile" });
      g.restore();
    },
  };
  HERO.PROUD = g => {                                               // 두 주먹을 들고 가슴을 편 과신
    const arms = [[[398, 482], [318, 400], [346, 252]], [[626, 482], [706, 400], [678, 252]]];
    paper(g, [...standing({ arms }), { d: circ(346, 246, 38), fill: C.white }, { d: circ(678, 246, 38), fill: C.white }, ...scarf(0), head(512, 334)]);
    face(g, 512, 336, { eyes: "arc", brows: "up", mouth: "grin" });
  };

  // ---------- 얼굴 없는 흰둥이: 낯선 사람 (검은 긴 코트·챙 넓은 모자) ----------
  function SCAM(g) {
    g.save(); g.translate(512, 910); g.rotate(0.06); g.translate(-512, -910);
    const armP = [[400, 480], [330, 560], [262, 548]], armB = [[624, 480], [712, 560], [664, 470]];
    paper(g, [{ d: rr(456, 840, 52, 60, 20), fill: C.pants }, { d: rr(520, 840, 52, 60, 20), fill: C.pants },
      { d: ell(474, 904, 52, 24), fill: C.shoe }, { d: ell(552, 904, 52, 24), fill: C.shoe },
      ...standing({ arms: [armB, armP], body: C.coat, coat: true, legs: false }),
      { d: poly([[470, 446], [554, 446], [512, 560]]), fill: C.coat2 },
      phone(240, 540, 74, 120, 0.1), { d: circ(262, 548, 30), fill: C.white }, { d: circ(664, 470, 30), fill: C.white }, { d: circ(650, 438, 13), fill: C.white },
      head(512, 340, 112),
      { d: rr(418, 176, 188, 96, 22), fill: C.coat }, { d: ell(512, 268, 182, 32), fill: C.coat }, { d: rr(418, 236, 188, 20, 4), fill: "#111111" }]);
    g.restore();
  }
  // ---------- 소품 ----------
  function TRAP(g) {
    paper(g, [
      { d: poly([[250, 640], [700, 600], [790, 660], [340, 706]]), fill: C.woodL },
      { d: poly([[340, 706], [790, 660], [790, 720], [340, 770]]), fill: C.wood },
      { d: poly([[250, 640], [340, 706], [340, 770], [250, 700]]), fill: C.woodD },
      { d: g => { g.moveTo(330, 664); g.quadraticCurveTo(300, 470, 460, 430); }, fill: C.metal, line: 16 },
      { d: g => { g.moveTo(460, 430); g.quadraticCurveTo(560, 420, 610, 520); }, fill: C.metal, line: 16 },
      { d: circ(470, 650, 26), fill: C.metal }, { d: rr(560, 612, 110, 16, 6), fill: "#6F747E" },
      { d: circ(612, 548, 64), fill: C.gold },
    ]);
    g.save(); g.strokeStyle = C.goldD; g.lineWidth = 8; g.beginPath(); g.arc(612, 548, 44, 0, Math.PI * 2); g.stroke();
    g.fillStyle = "rgba(255,255,255,.55)"; g.beginPath(); g.ellipse(590, 520, 14, 8, -0.6, 0, Math.PI * 2); g.fill(); g.restore();
  }
  function BASKET(g) {
    const eggs = [[372, 500], [450, 470], [530, 462], [610, 476], [680, 506], [420, 530], [580, 520], [500, 520]].map(([x, y]) => ({ d: ell(x, y, 46, 60, (x - 512) / 900), fill: "#FBF6EA" }));
    paper(g, [{ d: g => { g.moveTo(330, 560); g.bezierCurveTo(330, 230, 694, 230, 694, 560); }, fill: "#A87A47", line: 30 }, ...eggs,
      { d: poly([[296, 540], [728, 540], [682, 800], [342, 800]]), fill: "#B98A55" }, { d: rr(284, 528, 456, 42, 18), fill: "#A87A47" }]);
    g.save(); g.strokeStyle = "rgba(90,60,30,.45)"; g.lineWidth = 6;
    for (let i = 0; i < 5; i++) { g.beginPath(); g.moveTo(310 + i * 6, 600 + i * 42); g.lineTo(714 - i * 6, 600 + i * 42); g.stroke(); }
    for (let i = 0; i < 9; i++) { const x = 350 + i * 41; g.beginPath(); g.moveTo(x, 576); g.lineTo(x + (512 - x) * 0.12, 796); g.stroke(); }
    g.restore();
  }
  function BUCKET(g) {
    const coin = (x, y, r) => ({ d: ell(x, y, r, r * 0.42), fill: C.gold });
    const top = []; for (let i = 0; i < 9; i++) top.push(coin(360 + i * 38, 372 - (i % 3) * 14, 40));
    const holes = [[420, 560], [530, 650], [612, 520]], stream = [];
    holes.forEach(([x, y], k) => { const dx = k === 2 ? 1 : -1; for (let j = 1; j <= 4; j++) stream.push(coin(x + dx * (12 + j * 26), y + j * 52, 22 - j * 2)); });
    paper(g, [...top, { d: poly([[318, 380], [706, 380], [664, 800], [360, 800]]), fill: C.slate }, { d: ell(512, 382, 196, 30), fill: C.slateL },
      ...holes.map(([x, y]) => ({ d: circ(x, y, 20), fill: "#121A2E" })), ...stream]);
    g.save(); g.strokeStyle = C.goldD; g.lineWidth = 4; for (const p of [...top, ...stream]) { g.beginPath(); p.d(g); g.stroke(); } g.restore();
  }

  const wrap = f => (g, w, h) => { f(g); grain(g, w, h); };
  window.FIG = {
    HERO: Object.fromEntries(Object.entries(HERO).map(([k, f]) => [k, wrap(f)])),
    SCAM: wrap(SCAM), TRAP: wrap(TRAP), BASKET: wrap(BASKET), BUCKET: wrap(BUCKET),
  };
})();
