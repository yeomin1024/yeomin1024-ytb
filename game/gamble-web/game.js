// VERSION: v0.8.0-web.1 — 2026-11-27 — Godot 데모 v0.8.0 화면(scenes/main.gd · scenes/table_view.gd)을 캔버스 + HTML 로 옮김
//
// 화면: 내가 고르는 중 = 내 테이블(mine), 그 밖 = 상대 테이블(theirs) · 상대 시선 = 불빛 · 머묾 게이지 → '!'
// 조작: 마우스(터치) = 내 시선 · 카드 클릭 = 내기 · 상대 테이블에서 물건 클릭 = 물건 확인, 상대 클릭 = 몸 수색
//       협력자 부르기 = 버튼이나 키 2 를 2.5초 누르고 있기 · 버튼·설정 위에선 시선이 마지막 자리 그대로
// 규칙은 core.js(GambleCore) 에만. 시험용으로 window.__gm 에 지금 매치를 보여 줌.
// 연구·교육용 데모 — 실제 돈과 관계없음.
(function () {
  "use strict";
  const { GameLog, RankCards, CheatRules, AiBrain, GambleMatch, Phase, ROUNDS } = window.GambleCore;
  const W = 1280, H = 800;
  const FONT = '"Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", "WenQuanYi Zen Hei", sans-serif';
  const MAX_DT = 0.1; // 프레임이 끊겨도 한 번에 0.1초 넘게 흐르지 않게

  // ───────────────────────── 테이블 좌표 (table_view.gd) ─────────────────────────
  const HAND_Y = 728, HAND_CARD = [92, 128], HAND_GAP = 106, HAND_ZONE_Y = 655;
  const OBJ_ZONE = [46, 62], SLOT_SIZE = [70, 100];
  const HEAD = [640, 196], HEAD_R = 62, EYE_L = [615, 190], EYE_R = [665, 190], FACE_ZONE_R = 92;
  const BODY_ZONE = [410, 290, 460, 190];
  const T_OBJ = [[850, 600], [960, 610], [1070, 600]];
  const T_SLOT = [640, 525], T_MY_CARD = [640, 705];
  const T_LOOK = { own_card: [640, 445], face: [640, 790], hands: [640, 790], away: [1180, 330], table: [640, 570] };
  const M_TOP_Y = 300, M_OBJ = [[430, 440], [640, 420], [850, 440]], M_SLOT = [640, 595], M_OPP_CARD = [640, 220];
  const C_SKIN = [0.86, 0.72, 0.60], C_HAIR = [0.16, 0.12, 0.10], C_SUIT = [0.13, 0.14, 0.20], C_SHIRT = [0.85, 0.84, 0.80];
  const C_FELT = [0.11, 0.33, 0.22], C_WOOD = [0.36, 0.22, 0.12], C_LIGHT = [1.0, 0.86, 0.45], C_MARK = [1.0, 0.78, 0.12];

  // 행동 버튼: [id, 역할, 이름, 단축키, 짧은 설명]
  const ACTIONS = [
    ["lighter", "slave", "반사경 라이터 놓기", "1", "1.5초 보면 상대 카드"],
    ["lighter_plain", "slave", "빈 라이터 놓기", "3", "미끼 — '!' 만 뜸"],
    ["call", "slave", "협력자 부르기 (누르고 있기)", "2", "2.5초 귀 만지기 → 이어폰 연결"],
    ["attention", "slave", "시선 끌기", "F", "3초간 상대가 내 시선·행동을 못 봄"],
    ["cover", "king", "가리기", "C", "낸 카드 위 칩 — 반사경 막기"],
    ["random", "king", "섞기", "R", "낸 카드를 안 보고 섞음 — 둘 다 막기"],
    ["fake", "king", "바꿔치기", "X", "엿보면 가짜가 보임"],
    ["inspect", "king", "물건 확인", "Q", "물건을 클릭 — 반사경이면 적중"],
    ["search", "king", "몸 수색", "W", "이어폰이 있으면 적중"],
    ["judge_done", "king", "판단 끝 · 공개", "Enter", "바로 카드 공개"],
  ];
  const OPP_NAMES = { cheater: "손버릇 나쁜 딜러", watcher: "눈이 매서운 노인", gambler: "대담한 도박꾼" };
  const SETUP_KINDS = ["", "lighter", "lighter_plain", "cigcase", "cigcase_plain", "glass", "phone"];
  const SETUP_NAMES = ["없음", "라이터 (반사경)", "라이터 (빈 것)", "담뱃갑 (반사경)", "담뱃갑 (빈 것)", "술잔", "휴대폰"];
  const SETUP_DEFAULT = [1, 4, 0];
  const RULES_HTML =
    '<h3>한 턴의 흐름</h3>' +
    '<span class="k">왕</span>이 카드를 고름 → <span class="s">노예</span>가 엿보고 고름 → 왕이 판단 → 공개 · 차례마다 <b>30초</b><br>' +
    '내가 고를 땐 <b>내 테이블</b>, 상대가 고를 땐 <b>상대 테이블</b>과 상대 시선(<span class="lamp">불빛</span>)이 보여요.<br><br>' +
    '<span class="s">노예 (공격)</span> 반사경 물건을 <b>1.5초</b> 계속 보면 상대 카드 — 그 물건에 게이지가 차고, 다 차면 상대에게 <span class="lamp">\'!\'</span><br>' +
    '&nbsp;&nbsp;협력자: <b>\'협력자 부르기\'를 2.5초 누르고 있기</b>(귀 만지기) → 이어폰으로 카드를 알려 줌. 상대가 보고 있으면 협력자 가능성 ↑<br>' +
    '<span class="k">왕 (방어)</span> 카드를 <b>낸 뒤에만</b> 방어: 가리기·섞기·바꿔치기 · <b>물건 클릭 = 물건 확인</b> · <b>상대 클릭 = 몸 수색</b><br>' +
    '밝혀내기 성공: 상대 <span class="red">경고</span> +1 · 그 속임수 봉인 · <b>그 턴 무효 → 다시 고름</b> / 실패: 내 다음 차례 −10초<br><br>' +
    '<span class="red">경고 2개 = 즉시 패배</span> · 카드: 왕 &gt; 시민 &gt; 암살자 &gt; 왕 · 점수: 왕 측 승 +1, 노예 측 승 +4 · 6판<br>' +
    '<span class="muted">마우스(터치) = 내 시선 · 버튼 위에선 시선이 그대로 · 연구·교육용 데모, 실제 돈과 무관</span>';
  const TOAST_SECONDS = 2.8, TOAST_MAX = 3;

  // ───────────────────────── 상태 ─────────────────────────
  const $ = (id) => document.getElementById(id);
  const canvas = $("table"), ctx = canvas.getContext("2d");
  let game = null, opponentKind = "cheater";
  let mouse = [640, 400], lastGameMouse = [640, 400], overUi = false, currentGaze = "table";
  let clock = 0, pickMode = false, holdingCall = false;
  let speed = 1; // 시험용 배속 (window.__gm.setSpeed) — 평소엔 1
  const view = { mode: "theirs", hover_index: -1, my_gaze: "table", hover_pick: "", seen_card: -1, seen_source: "", hide_my_card: false, light: [640, 420] };
  let turnNotes = [], lastReveal = {}, lastRoundEnd = {}, lastMatchEnd = {}, resultMode = "";
  const toasts = [];
  const actionEls = {};
  const cache = {};

  // ───────────────────────── 그리기 도우미 ─────────────────────────
  const rgba = (c, a = 1) => `rgba(${Math.round(c[0] * 255)},${Math.round(c[1] * 255)},${Math.round(c[2] * 255)},${a})`;
  const dk = (c, x) => [c[0] * (1 - x), c[1] * (1 - x), c[2] * (1 - x)];
  function circle(x, y, r, style) { ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fillStyle = style; ctx.fill(); }
  function ring(x, y, r, a0, a1, style, w) { ctx.beginPath(); ctx.arc(x, y, r, a0, a1); ctx.strokeStyle = style; ctx.lineWidth = w; ctx.stroke(); }
  function poly(pts, style) { ctx.beginPath(); ctx.moveTo(pts[0][0], pts[0][1]); for (const p of pts.slice(1)) ctx.lineTo(p[0], p[1]); ctx.closePath(); ctx.fillStyle = style; ctx.fill(); }
  function line(x0, y0, x1, y1, style, w) { ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.strokeStyle = style; ctx.lineWidth = w; ctx.lineCap = "round"; ctx.stroke(); }
  function rect(x, y, w, h, style) { ctx.fillStyle = style; ctx.fillRect(x, y, w, h); }
  function srect(x, y, w, h, style, lw) { ctx.strokeStyle = style; ctx.lineWidth = lw; ctx.strokeRect(x, y, w, h); }
  function text(x, y, s, size, style, weight = 700) {
    ctx.font = `${weight} ${size}px ${FONT}`; ctx.textAlign = "center"; ctx.textBaseline = "alphabetic";
    ctx.lineJoin = "round"; ctx.lineWidth = 4; ctx.strokeStyle = "rgba(0,0,0,0.8)"; ctx.strokeText(s, x, y);
    ctx.fillStyle = style; ctx.fillText(s, x, y);
  }
  function ellipse(x, y, rx, ry, style) { ctx.beginPath(); ctx.ellipse(x, y, rx, ry, 0, 0, Math.PI * 2); ctx.fillStyle = style; ctx.fill(); }
  function cap(x, y, r, a0, a1, style) {
    const pts = []; for (let i = 0; i <= 20; i++) { const a = a0 + (a1 - a0) * i / 20; pts.push([x + Math.cos(a) * r, y + Math.sin(a) * r]); }
    poly(pts, style);
  }
  function glow(x, y, r, c, a) { for (let i = 0; i < 6; i++) circle(x, y, r * (1 - i / 6), rgba(c, a * 0.2)); }

  // ───────────────────────── 시선 영역·클릭 대상 ─────────────────────────
  const inObj = (p, c) => Math.abs(p[0] - c[0]) <= OBJ_ZONE[0] && Math.abs(p[1] - (c[1] - 15)) <= OBJ_ZONE[1];
  const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]);
  const inRect = (p, r) => p[0] >= r[0] && p[0] <= r[0] + r[2] && p[1] >= r[1] && p[1] <= r[1] + r[3];
  function gazeTarget(p) {
    if (!game) return "table";
    if (view.mode === "mine") {
      for (let i = 0; i < Math.min(game.objects[0].length, 3); i++) if (inObj(p, M_OBJ[i])) return "obj" + i;
      if (p[1] < M_TOP_Y) return "face";
      if (p[1] >= HAND_ZONE_Y) return "own_card";
      return "table";
    }
    if (dist(p, HEAD) <= FACE_ZONE_R) return "face";
    for (let i = 0; i < Math.min(game.objects[1].length, 3); i++) if (inObj(p, T_OBJ[i])) return "obj" + i;
    if (inRect(p, BODY_ZONE)) return "hands";
    return "table";
  }
  function pickTarget(p) {
    if (!game || view.mode !== "theirs") return "";
    for (let i = 0; i < Math.min(game.objects[1].length, 3); i++) if (inObj(p, T_OBJ[i])) return "obj" + i;
    if (dist(p, HEAD) <= FACE_ZONE_R || inRect(p, BODY_ZONE)) return "body";
    return "";
  }
  function handRect(i, n) {
    const cx = 640 + (i - (n - 1) / 2) * HAND_GAP, lift = i === view.hover_index ? 16 : 0;
    return [cx - HAND_CARD[0] / 2, HAND_Y - HAND_CARD[1] / 2 - lift, HAND_CARD[0], HAND_CARD[1]];
  }
  function cardAt(p) {
    if (!game || view.mode !== "mine") return -1;
    const n = game.hands[0].length;
    for (let i = 0; i < n; i++) if (inRect(p, handRect(i, n))) return i;
    return -1;
  }

  // ───────────────────────── 테이블 그리기 ─────────────────────────
  const slaveVisible = () => game.t >= game.blind_until;
  function dwellIndex(seat) {
    if (game.phase !== Phase.SLAVE_TURN || game.slave !== seat) return -1;
    const g = game.gaze[seat];
    if (!g.startsWith("obj")) return -1;
    const idx = parseInt(g.slice(3), 10);
    return idx >= 0 && idx < game.objects[seat].length ? idx : -1;
  }
  function drawTable() {
    ctx.setTransform(canvas.width / W, 0, 0, canvas.height / H, 0, 0);
    rect(0, 0, W, H, "#0f0d12");
    if (!game) return;
    if (view.mode === "mine") drawMine(); else drawTheirs();
  }
  function drawTheirs() {
    circle(640, 40, 300, rgba([0.15, 0.11, 0.09], 0.55));
    const aiSlave = game.slave === 1;
    const blind = aiSlave && game.phase === Phase.SLAVE_TURN && !slaveVisible();
    drawOpponent(blind);
    poly([[190, 440], [1090, 440], [1280, 800], [0, 800]], rgba(C_FELT));
    line(190, 440, 1090, 440, rgba(C_WOOD), 10);
    drawOpponentHands();
    const dwellIdx = aiSlave && !blind ? dwellIndex(1) : -1;
    for (let i = 0; i < Math.min(game.objects[1].length, 3); i++) {
      const c = T_OBJ[i];
      drawObject(c, game.objects[1][i], false, view.hover_pick === "obj" + i, 1.0);
      if (game.checked[1][i]) text(c[0], c[1] + 58, "빈 것 (확인됨)", 13, "rgb(178,230,178)");
      if (i === dwellIdx) gauge(c[0], c[1] - 8, game.dwell_progress());
      if (aiSlave && i < game.marks.length && game.marks[i]) mark(c);
    }
    if (game.committed[1] !== -1) {
      const r = [T_SLOT[0] - SLOT_SIZE[0] / 2, T_SLOT[1] - SLOT_SIZE[1] / 2, SLOT_SIZE[0], SLOT_SIZE[1]];
      drawCard(r, game.committed[1], game.revealed, false);
      if (game.king === 1 && !game.revealed) kingMarks(r);
    }
    if (game.committed[0] !== -1) drawMyCard(T_MY_CARD, [64, 92]);
    if (!blind && game.phase !== Phase.REVEALED && game.phase !== Phase.MATCH_OVER) drawLightTheirs();
    if (view.hover_pick === "body") {
      ring(HEAD[0], HEAD[1], FACE_ZONE_R, 0, Math.PI * 2, "rgba(255,128,77,0.85)", 3);
      srect(BODY_ZONE[0], BODY_ZONE[1], BODY_ZONE[2], BODY_ZONE[3], "rgba(255,128,77,0.85)", 3);
      text(830, 215, "클릭: 몸 수색 (이어폰 찾기)", 18, "rgb(255,178,128)");
    } else if (view.hover_pick.startsWith("obj")) {
      const idx = parseInt(view.hover_pick.slice(3), 10);
      if (idx >= 0 && idx < 3) text(T_OBJ[idx][0], T_OBJ[idx][1] - 112, "클릭: 물건 확인", 17, "rgb(255,178,128)");
    }
  }
  function lookVec(target) {
    if (!target || target === "face" || target === "hands") return [0, 1.5];
    let to = T_LOOK[target] || [640, 900];
    if (target.startsWith("obj")) { const i = parseInt(target.slice(3), 10); if (i >= 0 && i < 3) to = T_OBJ[i]; }
    const dx = to[0] - HEAD[0], dy = to[1] - HEAD[1], l = Math.hypot(dx, dy) || 1;
    return [dx / l * 7, dy / l * 5.5];
  }
  function pupilOffset() {
    const k = Math.max(0, Math.min(1, (game.t - game.gaze_since[1]) / CheatRules.TURN_TIME));
    const a = lookVec(game.gaze_prev[1]), b = lookVec(game.gaze[1]);
    return [a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k];
  }
  function drawOpponent(blind) {
    const off = pupilOffset(), sh = [off[0] * 1.4, off[1] * 1.4];
    poly([[470, 300], [810, 300], [870, 470], [410, 470]], rgba(C_SUIT));
    poly([[605, 300], [675, 300], [640, 368]], rgba(C_SHIRT));
    rect(618, 240, 44, 66, rgba(dk(C_SKIN, 0.12)));
    const h = [HEAD[0] + sh[0], HEAD[1] + sh[1]];
    circle(h[0], h[1], HEAD_R, rgba(C_SKIN));
    cap(h[0], h[1], HEAD_R + 4, Math.PI * 1.12, Math.PI * 1.88, rgba(C_HAIR));
    for (const e of [EYE_L, EYE_R]) {
      const ec = [e[0] + sh[0], e[1] + sh[1]];
      ellipse(ec[0], ec[1], 13, 9, "rgb(247,247,242)");
      circle(ec[0] + off[0], ec[1] + off[1], 5.5, "rgb(31,23,18)");
    }
    const furrow = Math.max(0, Math.min(1, (game.brains[1].suspicion + 1.7) / 4)) * 6;
    line(EYE_L[0] + sh[0] - 14, EYE_L[1] + sh[1] - 17, EYE_L[0] + sh[0] + 12, EYE_L[1] + sh[1] - 17 + furrow, rgba(C_HAIR), 4);
    line(EYE_R[0] + sh[0] - 12, EYE_R[1] + sh[1] - 17 + furrow, EYE_R[0] + sh[0] + 14, EYE_R[1] + sh[1] - 17, rgba(C_HAIR), 4);
    line(h[0] - 16, h[1] + 36, h[0] + 16, h[1] + 36, "rgb(115,51,51)", 3);
    if (blind) {
      rect(h[0] - 52, h[1] - 26, 104, 30, rgba(C_HAIR));
      text(h[0], h[1] + 92, "술잔을 쏟았다 — 3초간 상대 눈이 안 보임", 16, "rgb(255,178,128)");
    } else if (game.calling[1]) {
      const ear = [h[0] + HEAD_R + 6, h[1]];
      line(790, 330, ear[0] + 10, ear[1] + 18, rgba(C_SUIT), 18);
      circle(ear[0] + 6, ear[1] + 6, 16, rgba(dk(C_SKIN, 0.1)));
      const k = 0.5 + 0.5 * Math.sin(clock * 9);
      text(ear[0] + 40, ear[1] - 30, "?", 34, `rgb(255,${Math.round((0.4 + 0.4 * k) * 255)},77)`);
      text(h[0], h[1] + 92, "귀를 만지작거린다…", 16, "rgb(255,153,102)");
    }
  }
  function drawOpponentHands() {
    for (const hc of [[505, 462], [775, 462]]) { rect(hc[0] - 26, hc[1] - 34, 52, 18, rgba(C_SUIT)); circle(hc[0], hc[1], 22, rgba(C_SKIN)); }
    let n = game.hands[1].length;
    if (game.committed[1] !== -1 && !game.revealed) n -= 1;
    for (let i = 0; i < n; i++) drawCard([452 + i * 14, 400 - i * 2, 34, 50], -1, false, false);
  }
  function drawLightTheirs() {
    const g = game.gaze[1];
    let target = T_LOOK[g] || [640, 570];
    if (g.startsWith("obj")) { const i = parseInt(g.slice(3), 10); if (i >= 0 && i < 3) target = T_OBJ[i]; }
    view.light = [view.light[0] + (target[0] - view.light[0]) * 0.22, view.light[1] + (target[1] - view.light[1]) * 0.22];
    if (g === "face" || g === "hands") {
      glow(640, 800, 260, [1.0, 0.45, 0.35], 0.5);
      text(640, 645, "상대가 당신을 보는 중", 18, "rgb(255,140,115)");
      return;
    }
    if (g === "away") { text(1120, 300, "딴 곳을 봄", 15, "rgba(255,255,255,0.5)"); return; }
    glow(view.light[0], view.light[1], 95, C_LIGHT, 0.55);
  }
  function drawMine() {
    rect(0, 120, W, M_TOP_Y - 120, "rgb(23,18,20)");
    poly([[520, 300], [760, 300], [720, 150], [560, 150]], "rgb(28,28,38)");
    circle(640, 128, 46, "rgb(33,31,36)");
    text(640, 290, "▲ 위쪽 = 상대를 봄", 13, "rgba(255,255,255,0.35)", 500);
    rect(0, M_TOP_Y, W, H - M_TOP_Y, rgba(C_FELT));
    line(0, M_TOP_Y, W, M_TOP_Y, rgba(C_WOOD), 10);
    if (game.committed[1] !== -1) {
      const r = [M_OPP_CARD[0] - 28, M_OPP_CARD[1] - 40, 56, 80];
      drawCard(r, game.committed[1], game.revealed, false);
      if (game.king === 1 && !game.revealed) kingMarks(r);
    }
    if (view.seen_card >= 0 && !game.revealed) {
      const sr = [M_OPP_CARD[0] + 48, M_OPP_CARD[1] - 40, 56, 80];
      rect(sr[0] - 4, sr[1] - 4, sr[2] + 8, sr[3] + 8, "rgba(77,230,255,0.35)");
      drawCard(sr, view.seen_card, true, false);
      text(sr[0] + sr[2] / 2, sr[1] - 8, view.seen_source === "peek" ? "엿본 카드" : "이어폰", 14, "rgb(128,242,255)");
    }
    const meSlave = game.slave === 0;
    const dwellIdx = meSlave ? dwellIndex(0) : -1;
    for (let i = 0; i < Math.min(game.objects[0].length, 3); i++) {
      const c = M_OBJ[i];
      drawObject(c, game.objects[0][i], true, view.my_gaze === "obj" + i, 1.25);
      if (i === dwellIdx) {
        const k = game.dwell_progress();
        gauge(c[0], c[1] - 8, k);
        if (k >= 1 && !slaveVisible()) text(c[0], c[1] - 92, "안 들킴", 16, "rgb(128,255,153)");
      }
      if (meSlave && i < game.marks.length && game.marks[i]) mark(c);
    }
    if (game.committed[0] !== -1) drawMyCard(M_SLOT, SLOT_SIZE);
    drawHand();
    drawHints();
    drawLightMine();
  }
  function drawLightMine() {
    if (game.slave === 0 && game.phase === Phase.SLAVE_TURN && !slaveVisible()) {
      text(860, 225, "시선 끌기 중 — 상대가 당신을 못 봄", 17, "rgb(128,255,153)");
      return;
    }
    const g = game.gaze[1];
    if (g === "face") {
      glow(640, 150, 240, [1.0, 0.4, 0.3], 0.55);
      text(860, 225, "상대가 당신을 보는 중", 19, "rgb(255,153,128)");
    } else if (g === "hands") {
      view.light = [view.light[0] + (640 - view.light[0]) * 0.22, view.light[1] + (715 - view.light[1]) * 0.22];
      glow(view.light[0], view.light[1], 170, [1.0, 0.45, 0.35], 0.45);
      text(860, 225, "상대가 당신 손을 보는 중", 17, "rgb(255,153,128)");
    } else if (g === "own_card") text(860, 225, "상대: 자기 카드를 봄", 15, "rgba(255,255,255,0.55)", 500);
    else text(860, 225, "상대: 딴 곳을 봄", 15, "rgba(255,255,255,0.55)", 500);
    if (view.my_gaze === "face" && game.calling[1]) text(860, 258, "상대가 귀를 만지작거린다!", 18, "rgb(255,178,77)");
  }
  function drawHints() {
    if (game.slave !== 0 || game.phase !== Phase.SLAVE_TURN || game.committed[0] !== -1) return;
    let msg, col = "rgb(255,230,115)";
    const hasMirror = game.objects[0].some((k) => CheatRules.is_mirror(k));
    if (game.sealed[0].peek) { msg = "엿보기 봉인됨 — 반사경이 압수됨"; col = "rgb(255,115,102)"; }
    else if (game.randomized) { msg = "상대가 카드를 섞음 — 엿볼 수 없음"; col = "rgb(255,115,102)"; }
    else if (game.covered) { msg = "상대가 칩으로 가림 — 반사경 안 통함"; col = "rgb(255,115,102)"; }
    else if (hasMirror) msg = "반사경 물건을 1.5초 계속 보면 상대 카드 (게이지가 차면 상대에게 '!')";
    else msg = "반사경 물건이 없음 — 왼쪽 버튼으로 놓기";
    text(640, 530, msg, 15, col);
  }
  function drawHand() {
    const n = game.hands[0].length;
    const myTurn = (game.phase === Phase.KING_TURN || game.phase === Phase.SLAVE_TURN) && game.actor() === 0 && game.committed[0] === -1;
    const skip = game.committed[0] !== -1 ? game.hands[0].indexOf(game.committed[0]) : -1;
    for (let i = 0; i < n; i++) {
      if (i === skip) continue;
      drawCard(handRect(i, n), game.hands[0][i], true, myTurn && i === view.hover_index);
    }
  }
  function drawMyCard(c, sz) {
    const r = [c[0] - sz[0] / 2, c[1] - sz[1] / 2, sz[0], sz[1]];
    const unknown = view.hide_my_card && !game.revealed;
    drawCard(r, unknown ? -1 : game.committed[0], !unknown, false);
    if (unknown) text(r[0] + r[2] / 2, r[1] + r[3] / 2 + 12, "?", 34, "#fff");
    if (game.king === 0 && !game.revealed) {
      kingMarks(r);
      if (game.faked) text(r[0] + r[2] + 70, r[1] + r[3] / 2 + 26, "바꿔치기 준비됨", 13, "rgb(255,204,102)");
    }
    if (!game.revealed) text(r[0] + r[2] + 70, r[1] + r[3] / 2 + 4, "← 내 카드", 13, "rgba(255,255,255,0.6)", 500);
  }
  function kingMarks(r) {
    const cx = r[0] + r[2] / 2, cy = r[1] + r[3] / 2;
    if (game.covered) {
      circle(cx, cy, 20, "rgb(179,26,26)");
      ring(cx, cy, 15, 0, Math.PI * 2, "rgba(255,255,255,0.9)", 3);
      circle(cx, cy, 9, "rgb(217,38,38)");
    }
    if (game.randomized) text(cx, r[1] - 8, "섞음", 13, "rgb(255,230,128)");
  }
  function drawObject(c, kind, mine, looking, sc) {
    const look = CheatRules.OBJECTS[kind].look;
    ctx.save(); ctx.translate(c[0], c[1]); ctx.scale(sc, sc);
    if (look === "lighter") {
      rect(-17, -10, 34, 48, "rgb(184,184,191)"); srect(-17, -10, 34, 48, "rgb(77,77,82)", 2);
      poly([[-17, -10], [17, -10], [13, -40], [-21, -40]], "rgb(204,204,214)");
      rect(-13, -36, 22, 22, "rgba(191,224,255,0.6)");
    } else if (look === "cigcase") {
      rect(-26, -6, 52, 40, "rgb(191,173,102)"); srect(-26, -6, 52, 40, "rgb(89,77,38)", 2);
      rect(-22, -2, 44, 10, "rgba(230,217,153,0.7)");
    } else if (look === "glass") {
      poly([[-22, -30], [22, -30], [17, 34], [-17, 34]], "rgba(191,217,242,0.25)");
      rect(-17, 6, 34, 26, "rgba(153,89,26,0.6)");
    } else {
      rect(-18, -30, 36, 64, "rgb(20,20,26)"); rect(-15, -26, 30, 54, "rgb(38,51,77)");
    }
    ctx.restore();
    if (mine) text(c[0], c[1] + 54 * sc, CheatRules.is_mirror(kind) ? "반사경" : "빈 것", 13, "rgba(255,255,255,0.55)", 500);
    if (looking) ring(c[0], c[1] - 5, 58 * sc, 0, Math.PI * 2, "rgba(255,230,77,0.6)", 3);
  }
  function gauge(x, y, k) {
    if (k < 0) return;
    ring(x, y, 56, 0, Math.PI * 2, "rgba(0,0,0,0.55)", 9);
    const col = k < 1 ? rgba(C_MARK) : "rgb(255,89,64)";
    ring(x, y, 56, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * Math.max(0, Math.min(1, k)), col, 9);
  }
  function mark(c) {
    const x = c[0], y = c[1] - 86 + Math.sin(clock * 6) * 3;
    circle(x, y, 22, rgba(C_MARK));
    ring(x, y, 22, 0, Math.PI * 2, "rgb(89,46,0)", 3);
    text(x, y + 11, "!", 32, "rgb(64,20,0)", 900);
  }
  function drawCard(r, card, faceUp, hl) {
    const [x, y, w, h] = r;
    if (hl) rect(x - 5, y - 5, w + 10, h + 10, "rgba(255,217,77,0.8)");
    rect(x, y, w, h, faceUp ? "rgb(250,245,230)" : "rgb(140,26,31)");
    srect(x, y, w, h, "rgb(20,20,20)", 2);
    if (!faceUp || card < 0) { srect(x + 6, y + 6, w - 12, h - 12, "rgb(204,64,64)", 2); return; }
    const col = card === RankCards.Card.KING ? "rgb(217,166,38)" : card === RankCards.Card.ASSASSIN ? "rgb(115,20,26)" : "rgb(89,115,153)";
    circle(x + w / 2, y + h / 2 - h * 0.1, w * 0.22, col);
    ctx.font = `700 ${Math.round(w * 0.2)}px ${FONT}`; ctx.textAlign = "center"; ctx.fillStyle = "rgb(26,26,26)";
    ctx.fillText(RankCards.CARD_NAMES[card], x + w / 2, y + h - h * 0.12);
  }

  // ───────────────────────── 매치 ─────────────────────────
  function newMatch() {
    const brain = new AiBrain();
    brain.configure(opponentKind);
    game = new GambleMatch();
    const seed = Math.floor(Date.now() % 1000000);
    game.setup(seed, null, brain);
    view.seen_card = -1; view.seen_source = ""; view.hide_my_card = false;
    turnNotes = []; lastReveal = {}; lastRoundEnd = {}; lastMatchEnd = {}; resultMode = ""; pickMode = false;
    $("result").hidden = true; $("help").hidden = true; clearToasts();
    for (const k of Object.keys(cache)) delete cache[k];
    $("setup").hidden = false;
    drain();
  }
  function setupStart() {
    if (!game || game.phase !== Phase.IDLE) return;
    const kinds = [0, 1, 2].map((i) => SETUP_KINDS[$("obj" + i).selectedIndex]).filter((k) => k !== "");
    game.set_objects(0, kinds);
    $("setup").hidden = true;
    game.start();
    drain();
  }
  function toggleHelp() { $("help").hidden = !$("help").hidden; }
  function resultBtn() {
    if (!game) return;
    if (game.phase === Phase.MATCH_OVER) { newMatch(); return; }
    if (game.phase === Phase.REVEALED) { $("result").hidden = true; game.next(); drain(); }
  }
  function currentView() {
    const ph = game.phase;
    if (ph === Phase.KING_TURN && game.king === 0) return "mine";
    if ((ph === Phase.SLAVE_TURN || ph === Phase.JUDGE) && game.slave === 0) return "mine";
    return "theirs";
  }
  const myCardTurn = () => (game.phase === Phase.KING_TURN || game.phase === Phase.SLAVE_TURN) && game.actor() === 0 && game.committed[0] === -1;
  const overlayOpen = () => !$("setup").hidden || !$("help").hidden || !$("result").hidden;
  function pickAt(p) {
    if (view.mode !== "theirs") return "";
    const tgt = pickTarget(p);
    if (tgt.startsWith("obj")) return game.why_not(0, "inspect", tgt.slice(3)) === "" ? tgt : "";
    if (tgt === "body" && !pickMode) return game.why_not(0, "search") === "" ? tgt : "";
    return "";
  }

  // ───────────────────────── 입력 ─────────────────────────
  function stagePoint(e) {
    const r = $("stage").getBoundingClientRect();
    return [(e.clientX - r.left) * W / r.width, (e.clientY - r.top) * H / r.height];
  }
  window.addEventListener("pointermove", (e) => {
    mouse = stagePoint(e);
    overUi = !!(e.target && e.target.closest && e.target.closest(".ui"));
  });
  canvas.addEventListener("pointerdown", (e) => {
    if (!game || e.button !== 0) return;
    const p = stagePoint(e);
    mouse = p; overUi = false; lastGameMouse = p; currentGaze = gazeTarget(p);
    if (myCardTurn() && view.mode === "mine") {
      view.hover_index = -1;
      const idx = cardAt(p);
      if (idx >= 0) { game.commit(game.hands[0][idx]); drain(); }
      return;
    }
    const tgt = pickAt(p);
    if (tgt.startsWith("obj")) { pickMode = false; game.inspect(parseInt(tgt.slice(3), 10)); drain(); }
    else if (tgt === "body") { game.search(); drain(); }
    else if (pickMode) { pickMode = false; toast("물건 확인 취소", "info"); }
  });
  // 키는 e.code 로 (한글 입력 상태여도 같은 자리 키가 먹게)
  window.addEventListener("keydown", (e) => {
    if (!game || e.repeat) return;
    const k = e.code;
    if (k === "Digit2" || k === "Numpad2") { callDown(); e.preventDefault(); return; }
    if (k === "KeyH" || (k === "Escape" && !$("help").hidden)) { toggleHelp(); return; }
    if (k === "Escape" && pickMode) { pickMode = false; return; }
    if (k === "Enter" || k === "NumpadEnter" || k === "KeyN") {
      if (!$("setup").hidden) setupStart();
      else if (!$("result").hidden) resultBtn();
      else if (game.phase === Phase.JUDGE) act("judge_done");
      e.preventDefault();
      return;
    }
    const map = { Digit1: "lighter", Digit3: "lighter_plain", KeyF: "attention", KeyC: "cover", KeyR: "random", KeyX: "fake", KeyQ: "inspect", KeyW: "search" };
    if (map[k]) act(map[k]);
  });
  window.addEventListener("keyup", (e) => { if (e.code === "Digit2" || e.code === "Numpad2") callUp(); });
  function callDown() {
    if (!game || !$("help").hidden || holdingCall) return;
    const r = game.start_call();
    if (!r.ok) toast("지금은 못 해요 — " + shortWhy("call", r.why || ""), "info");
    else holdingCall = true;
    drain();
  }
  function callUp() {
    if (!game) return;
    holdingCall = false;
    game.stop_call();
    drain();
  }
  function act(id) {
    if (!game || !$("help").hidden) return;
    let r = {};
    switch (id) {
      case "lighter": r = game.place_object("lighter"); break;
      case "lighter_plain": r = game.place_object("lighter_plain"); break;
      case "attention": r = game.attention(); break;
      case "cover": r = game.cover(); break;
      case "random": r = game.play_random(); break;
      case "fake": r = game.fake(); break;
      case "inspect": {
        const why = game.why_not(0, "inspect");
        if (why) r = { ok: false, why };
        else if (view.hover_pick.startsWith("obj")) r = game.inspect(parseInt(view.hover_pick.slice(3), 10));
        else { pickMode = true; toast("확인할 물건을 클릭하세요 (Esc 취소)", "info"); return; }
        break;
      }
      case "search": r = game.search(); break;
      case "judge_done": r = game.judge_done(); break;
      default: return;
    }
    if (r && r.ok === false) toast("지금은 못 해요 — " + shortWhy(id, r.why || ""), "info");
    drain();
  }
  const ruleOf = (id) => (id === "lighter" || id === "lighter_plain" ? ["object", id] : [id, ""]);
  function shortWhy(id, code) {
    const m = {
      not_active: "턴 진행 중에만", full: "물건 자리가 꽉 참", no_uses: "남은 횟수 없음", not_slave: "노예일 때만", not_king: "왕일 때만",
      after_commit: "카드를 낸 뒤에만", done: "이번 턴에 이미 함", already_seen: "상대가 이미 봄", already_this_turn: "이번 턴에 이미 함",
      no_target: "확인할 물건이 없음", checked: "이미 확인한 물건", calling: "부르는 중", connected: "이미 연결됨 (이번 판)",
      not_judge: "판단 시간에만", not_calling: "부르는 중이 아님",
    };
    if (code === "sealed") return id === "search" ? "이미 이어폰을 압수함" : "봉인됨";
    return m[code] || code;
  }

  // ───────────────────────── 알림 ─────────────────────────
  function toast(msg, kind = "info") {
    const el = document.createElement("div");
    el.className = "toast " + kind; el.textContent = msg;
    $("toasts").prepend(el);
    toasts.push({ el, age: 0 });
    while (toasts.length > TOAST_MAX) toasts.shift().el.remove();
  }
  function updateToasts(dt) {
    for (let i = toasts.length - 1; i >= 0; i--) {
      const t = toasts[i]; t.age += dt;
      const left = TOAST_SECONDS - t.age;
      if (left <= 0) { t.el.remove(); toasts.splice(i, 1); continue; }
      t.el.style.opacity = String(Math.max(0, Math.min(1, left / 0.5)));
    }
  }
  function clearToasts() { for (const t of toasts) t.el.remove(); toasts.length = 0; }

  // ───────────────────────── 이벤트 → 알림·결과 ─────────────────────────
  function eul(word) {
    if (!word) return "를";
    const code = word.charCodeAt(word.length - 1);
    if (code < 0xac00 || code > 0xd7a3) return "를";
    return (code - 0xac00) % 28 !== 0 ? "을" : "를";
  }
  const roundName = (idx) => (idx >= ROUNDS ? `연장 ${idx - ROUNDS + 1}판` : `${Math.max(idx, 0) + 1}/${ROUNDS}판`);
  function drain() {
    for (const ev of game.pop_events()) render(ev);
    if (game.phase === Phase.MATCH_OVER && resultMode !== "match") showResult("match");
    else if (game.phase === Phase.REVEALED && resultMode === "") showResult("turn");
  }
  function render(ev) {
    const me = ev.seat === 0;
    switch (ev.type) {
      case "round_start": toast(`${roundName(ev.round)} — 당신은 ${ev.king === 0 ? "왕 (방어)" : "노예 (공격)"}`, "info"); break;
      case "turn_start":
        turnNotes = []; lastReveal = {}; lastRoundEnd = {}; resultMode = ""; pickMode = false;
        view.seen_card = -1; view.seen_source = ""; view.hide_my_card = false;
        if (ev.replay) toast("이번 턴 무효 — 둘 다 다시 고르세요", "warn");
        break;
      case "phase_start":
        if (ev.limit < CheatRules.TURN_SECONDS - 0.01) {
          const mine = ev.actor === 0;
          toast(`${mine ? "내" : "상대"} 이번 차례 시간 ${Math.round(ev.limit)}초 (깎임)`, mine ? "bad" : "good");
        }
        break;
      case "object": {
        const n = CheatRules.OBJECTS[ev.kind].name;
        if (!me) toast(`상대가 ${n}${eul(n)} 책상에 놓았다`, "warn");
        else if (ev.seen) toast(`${n}${eul(n)} 놓았다 — 상대가 봤다, 의심 ↑`, "warn");
        else toast(`${n}${eul(n)} 놓았다 (${CheatRules.is_mirror(ev.kind) ? "반사경" : "빈 것"})`, "info");
        break;
      }
      case "call_start": if (me) toast("귀를 만지며 신호 중… (2.5초 누르고 있기)", "info"); break;
      case "call_cancel": if (me) toast("신호를 멈췄다 — 연결 안 됨", "warn"); break;
      case "call_seen": toast(me ? "상대가 수상한 손짓을 봤다 — 협력자 가능성 ↑" : "상대가 귀를 만지작거린다 — 협력자 가능성 ↑", me ? "bad" : "warn"); break;
      case "acc_connected": if (me) toast("이어폰 연결! 이번 판 동안 내 차례마다 카드를 알려 줌", "good"); break;
      case "attention": toast(me ? "시선 끌기 — 3초 동안 상대가 못 봄" : "상대가 술잔을 쏟았다 — 3초간 상대 시선이 안 보임", me ? "good" : "warn"); break;
      case "cover": toast(me ? "칩으로 가렸다 — 반사경 차단" : "상대가 칩으로 가렸다 — 반사경 안 통함", me ? "good" : "warn"); break;
      case "random":
        if (me) { view.hide_my_card = true; toast("카드를 섞었다 — 나도 모름, 엿보기·이어폰 차단", "good"); }
        else toast("상대가 카드를 섞었다 — 엿볼 수 없음", "warn");
        break;
      case "fake": if (me) toast("바꿔치기 준비 — 엿보면 가짜가 보임", "good"); break;
      case "info":
        if (me) {
          const c = RankCards.CARD_NAMES[ev.card], how = ev.source === "peek" ? "반사경" : "이어폰";
          view.seen_card = ev.card; view.seen_source = ev.source;
          toast(`${how}: 상대 카드 = ${c}`, "good");
          turnNotes.push(`${how}로 본 카드: ${c}`);
        }
        break;
      case "info_blocked":
        if (me) { const msg = ev.why === "cover" ? "칩에 가려 안 보인다" : "상대가 섞어서 알 수 없다"; toast(msg, "warn"); turnNotes.push(msg); }
        break;
      case "mark": toast(me ? "상대가 내 시선을 봤다 — 그 물건에 '!'" : "상대 시선이 물건에 머물렀다 — '!'", "warn"); break;
      case "judge_start": if (ev.king === 0) toast(`상대가 냈다 — ${Math.round(ev.limit)}초 안에 판단 (물건·상대 클릭)`, "info"); break;
      case "timeout":
        toast(`${me ? "내" : "상대"} 시간 초과 — 아무 카드나 냈다`, me ? "bad" : "info");
        if (me) turnNotes.push("시간 초과로 아무 카드나 냄");
        break;
      case "expose": renderExpose(ev); break;
      case "turn_summary": noteSummary(ev); break;
      case "reveal": lastReveal = ev; break;
      case "round_end": lastRoundEnd = ev; break;
      case "match_end": lastMatchEnd = ev; break;
    }
  }
  function renderExpose(ev) {
    const search = ev.kind === "search", what = search ? "몸 수색" : "물건 확인";
    let msg, tone;
    if (ev.by === 0 && ev.hit) { msg = `${what} 적중! ${search ? "이어폰 발견" : "반사경 발견"} — 상대 경고 ${ev.strikes[1]}/${CheatRules.STRIKES_TO_LOSE}`; tone = "good"; }
    else if (ev.by === 0) { msg = `${what} 헛짚음 — 내 다음 차례 −${CheatRules.EXPOSE_FAIL_CUT}초`; tone = "bad"; }
    else if (ev.hit) { msg = `들켰다! 상대가 ${what} — ${search ? "이어폰" : "반사경"} 압수 · 내 경고 ${ev.strikes[0]}/${CheatRules.STRIKES_TO_LOSE}`; tone = "bad"; }
    else { msg = `상대 ${what} 헛짚음 — 상대 다음 차례 −${CheatRules.EXPOSE_FAIL_CUT}초`; tone = "good"; }
    toast(msg, tone);
    turnNotes.push(msg);
  }
  function noteSummary(ev) {
    if (ev.slave === 0) return;
    const nMarks = ev.marks.filter(Boolean).length, parts = [];
    if (ev.peeked) parts.push("상대는 반사경으로 진짜 엿봤다");
    else if (nMarks > 0) parts.push("'!' 는 미끼였다");
    if (ev.info === "acc") parts.push("상대는 이어폰으로 들었다");
    if (parts.length === 0) parts.push("상대는 이번 턴 속임수를 안 썼다");
    turnNotes.push(parts.join(" · "));
  }
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
  function showResult(mode) {
    resultMode = mode;
    clearToasts();
    const title = $("result-title"), lines = [];
    if (mode === "match") {
      const w = lastMatchEnd.winner !== undefined ? lastMatchEnd.winner : game.winner;
      const reason = lastMatchEnd.reason || game.end_reason;
      title.textContent = w === 0 ? "매치 승리!" : w === 1 ? "매치 패배" : "무승부";
      title.style.color = w === 0 ? "#7dff8a" : w === 1 ? "#ff6b5e" : "#fff";
      if (reason === "CAUGHT_TWICE") lines.push(`<div class="cards">${w === 0 ? "상대가 두 번 들켰다" : "두 번 들켰다 — 즉시 패배"}</div>`);
      lines.push(`<div class="cards">최종 점수 나 ${game.scores[0]} : ${game.scores[1]} 상대</div>`);
      if (reason === "CAUGHT_TWICE") for (const n of turnNotes) lines.push(`<div class="line">${esc(n)}</div>`);
      $("btn-result").textContent = "새 매치 ▶";
    } else {
      const r = lastReveal.result || 0;
      title.textContent = r > 0 ? "이겼다!" : r < 0 ? "졌다" : "비김";
      title.style.color = r > 0 ? "#7dff8a" : r < 0 ? "#ff6b5e" : "#d9d9d9";
      const cards = lastReveal.cards || [-1, -1];
      const nm = (c) => (c < 0 ? "?" : RankCards.CARD_NAMES[c]);
      lines.push(`<div class="cards">나 <b>${nm(cards[0])}</b> &nbsp;vs&nbsp; 상대 <b>${nm(cards[1])}</b></div>`);
      if (lastRoundEnd.winner !== undefined) {
        lines.push(`<div class="line">${lastRoundEnd.winner === 0 ? "내가" : "상대가"} +${lastRoundEnd.points}점 → 점수 <b>${lastRoundEnd.scores[0]} : ${lastRoundEnd.scores[1]}</b></div>`);
      } else lines.push('<div class="line">같은 판, 남은 카드로 다음 턴</div>');
      for (const n of turnNotes) lines.push(`<div class="line">${esc(n)}</div>`);
      const faked = !!lastReveal.faked, got = !!lastReveal.info;
      if (faked && got && game.slave === 0) lines.push('<div class="line bad">속았다 — 본 카드는 바꿔치기한 가짜</div>');
      else if (faked && got) lines.push('<div class="line good">바꿔치기 성공 — 상대는 가짜를 봤다</div>');
      else if (faked && game.slave === 0) lines.push('<div class="line">상대는 바꿔치기를 준비해 두었었다</div>');
      $("btn-result").textContent = game.round_over ? "다음 판 ▶" : "다음 턴 ▶";
    }
    $("result-lines").innerHTML = lines.join("");
    $("result").hidden = false;
  }

  // ───────────────────────── 매 프레임 표시 ─────────────────────────
  function setText(id, s) { if (cache[id] !== s) { cache[id] = s; $(id).textContent = s; } }
  function setHTML(id, s) { if (cache["h:" + id] !== s) { cache["h:" + id] = s; $(id).innerHTML = s; } }
  function refresh() {
    const ph = game.phase, meKing = game.king === 0;
    // 점수판
    const role = ph === Phase.IDLE ? "-" : meKing ? '<span class="role-king">왕 (방어)</span>' : '<span class="role-slave">노예 (공격)</span>';
    const pend = game.pending_time[0] < 0 ? ` <span class="pend">다음 내 차례 ${Math.round(game.pending_time[0])}초</span>` : "";
    const dots = (n) => '<span class="strike">' + "●".repeat(n) + "</span>" + "○".repeat(Math.max(CheatRules.STRIKES_TO_LOSE - n, 0));
    setHTML("score", `<div class="opp">${roundName(game.round_index)} · 상대: ${OPP_NAMES[opponentKind]}</div>` +
      `<div class="big">나 ${game.scores[0]} : ${game.scores[1]} 상대</div><div>당신: ${role}${pend}</div>` +
      `<div>경고 &nbsp;나 ${dots(game.strikes[0])} &nbsp; 상대 ${dots(game.strikes[1])}</div>`);
    // 지금 할 일
    let title = "", sub = "", myMove = false;
    if (ph === Phase.IDLE) title = "책상 위 물건을 고르고 시작하세요";
    else if (ph === Phase.KING_TURN && meKing) { title = "내 차례 — 카드를 골라 엎으세요"; sub = "고르는 중엔 방어를 못 해요 · 위쪽을 보면 상대를 지켜봄"; myMove = true; }
    else if (ph === Phase.KING_TURN) { title = "상대(왕)가 고르는 중 — 상대 시선을 보세요"; sub = "상대가 안 볼 때 '협력자 부르기'를 2.5초 누르고 있기"; }
    else if (ph === Phase.SLAVE_TURN && meKing) { title = "상대가 엿보는 중 — 불빛과 '!' 를 보세요"; sub = "물건 클릭 = 물건 확인 · 상대 클릭 = 몸 수색 · 가리기·섞기·바꿔치기"; }
    else if (ph === Phase.SLAVE_TURN) { title = "내 차례 — 엿보고 카드를 내세요"; sub = "반사경 물건 1.5초 계속 보기 (상대에게 '!') · 이어폰이 있으면 3초 뒤 알려 줌"; myMove = true; }
    else if (ph === Phase.JUDGE && meKing) { title = "판단하세요 — 상대가 속임수를 썼을까?"; sub = "'!' 물건을 클릭해 확인하거나 상대를 클릭해 몸 수색 · 아니면 '판단 끝'"; myMove = true; }
    else if (ph === Phase.JUDGE) title = "상대가 판단 중…";
    else if (ph === Phase.REVEALED) title = "공개!";
    else if (ph === Phase.MATCH_OVER) title = "매치 끝";
    if (pickMode) { title = "확인할 물건을 클릭하세요"; sub = "Esc 취소"; }
    setText("title", title); setText("sub", sub);
    $("title").classList.toggle("mine", myMove);
    const active = ph === Phase.KING_TURN || ph === Phase.SLAVE_TURN, judging = ph === Phase.JUDGE;
    let left = 0, total = 1;
    if (active) { left = game.time_left(); total = game.limit; } else if (judging) { left = Math.max(game.judge_left, 0); total = game.judge_limit; }
    $("timer-fill").style.width = (active || judging ? Math.max(0, Math.min(1, left / Math.max(total, 0.01))) * 100 : 0) + "%";
    const fill = myMove ? (left < 5 ? "hurry" : "mine") : "theirs";
    if (cache.fill !== fill) { cache.fill = fill; $("timer-fill").className = fill; }
    setText("timer-text", active || judging ? left.toFixed(1) + "초" : "");
    refreshSuspect(ph, meKing);
    refreshActions(ph, meKing);
  }
  function refreshSuspect(ph, meKing) {
    if (ph === Phase.IDLE) {
      setText("sus-title", "의심 표시"); setText("sus-bar-label", ""); setText("sus-lines", "");
      $("sus-fill").style.width = "0%"; $("call-bar").hidden = true; return;
    }
    const marksN = game.marks.filter(Boolean).length;
    const sus = game.acc_suspect[game.slave] * 100;
    $("sus-fill").style.width = sus.toFixed(1) + "%";
    if (meKing) {
      setText("sus-title", "상대 의심 표시"); $("sus-title").style.color = "var(--king)";
      setText("sus-bar-label", `협력자 가능성 ${Math.round(sus)}%`);
      let lines = `엿보기 '!' : 물건 ${marksN}개\n남은 횟수 — 물건 확인 ${game.inspect_left[0]} · 몸 수색 ${game.search_left[0]}`;
      if (game.sealed[1].peek) lines += "\n반사경 압수함 (봉인)";
      if (game.sealed[1].acc) lines += "\n이어폰 압수함 (봉인)";
      setText("sus-lines", lines);
      $("call-bar").hidden = true;
    } else {
      setText("sus-title", "내 속임수 상태"); $("sus-title").style.color = "var(--slave)";
      setText("sus-bar-label", `상대가 느낀 협력자 가능성 ${Math.round(sus)}%`);
      let ear = `이어폰: 연결 안 됨 (부르기 ${game.acc_calls_left[0]}번 남음)`;
      if (game.sealed[0].acc) ear = "이어폰: 압수됨";
      else if (game.calling[0]) ear = "이어폰: 부르는 중… 손 떼지 마세요";
      else if (game.acc_connected[0]) ear = "이어폰: 연결됨 (이번 판)";
      setText("sus-lines", `상대에게 보인 '!' : 물건 ${marksN}개\n${ear}`);
      $("call-bar").hidden = !game.calling[0];
      $("call-fill").style.width = Math.min(100, game.call_progress[0] / CheatRules.ACC_CALL_SECONDS * 100) + "%";
    }
  }
  function subText(id, desc) {
    switch (id) {
      case "lighter": case "lighter_plain": return `${desc} · ${game.place_left[0]}번 남음`;
      case "call":
        if (game.calling[0]) return `신호 중 ${Math.round(Math.min(1, game.call_progress[0] / CheatRules.ACC_CALL_SECONDS) * 100)}% — 손 떼지 마세요`;
        return `${desc} · ${game.acc_calls_left[0]}번 남음`;
      case "attention": return `${desc} · ${game.attention_left[0]}번`;
      case "cover": return `${desc} · ${game.cover_left[0]}번 남음`;
      case "random": return `${desc} · ${game.random_left[0]}번 남음`;
      case "fake": return `${desc} · ${game.fake_left[0]}번 남음`;
      case "inspect": return `${desc} · ${game.inspect_left[0]}번 남음`;
      case "search": return `${desc} · ${game.search_left[0]}번 남음`;
      case "judge_done": return `${desc} · ${Math.max(game.judge_left, 0).toFixed(1)}초 남음`;
    }
    return desc;
  }
  function recommended(id) {
    if (id === "inspect") return game.marks.some(Boolean);
    if (id === "search") return game.acc_suspect[game.slave] >= 0.3;
    return false;
  }
  function refreshActions(ph, meKing) {
    const role = meKing ? "king" : "slave";
    const head = ph === Phase.IDLE ? "내 행동" : meKing ? "내 행동 — 왕 (방어)" : "내 행동 — 노예 (공격)";
    setText("act-head", head);
    $("act-head").style.color = ph === Phase.IDLE ? "" : meKing ? "var(--king)" : "var(--slave)";
    for (const a of ACTIONS) {
      const [id, r, , , desc] = a, e = actionEls[id];
      const show = r === role && ph !== Phase.IDLE && ph !== Phase.MATCH_OVER;
      if (e.btn.hidden === show) e.btn.hidden = !show;
      if (!show) continue;
      const [ra, rb] = ruleOf(id);
      let why = game.why_not(0, ra, rb);
      if (id === "call" && game.calling[0]) why = "";
      e.btn.disabled = why !== "";
      const sub = why === "" ? subText(id, desc) : shortWhy(id, why);
      if (e.sub.textContent !== sub) e.sub.textContent = sub;
      e.btn.classList.toggle("pulse", why === "" && recommended(id));
    }
  }

  // ───────────────────────── 시작 ─────────────────────────
  function build() {
    $("rules-setup").innerHTML = RULES_HTML;
    $("rules-help").innerHTML = RULES_HTML;
    $("setup-note").textContent = `게임 중에도 왼쪽 버튼으로 라이터를 ${CheatRules.PLACES_PER_MATCH}번 더 놓을 수 있어요 · PC 마우스 권장 (터치하면 그 자리를 보는 것으로 칩니다)`;
    for (let i = 0; i < 3; i++) {
      const sel = $("obj" + i);
      SETUP_NAMES.forEach((n, j) => { const o = document.createElement("option"); o.textContent = n; sel.appendChild(o); });
      sel.selectedIndex = SETUP_DEFAULT[i];
    }
    const list = $("act-list");
    for (const [id, role, name, key] of ACTIONS) {
      const b = document.createElement("button");
      b.type = "button"; b.className = "act " + role; b.id = "act-" + id; b.hidden = true;
      b.innerHTML = `<span class="name">${name}</span><span class="sub"></span><span class="key">${key}</span>`;
      if (id === "call") {
        b.addEventListener("pointerdown", (e) => { e.preventDefault(); callDown(); });
        for (const ev of ["pointerup", "pointerleave", "pointercancel"]) b.addEventListener(ev, () => { if (holdingCall) callUp(); });
      } else b.addEventListener("click", () => act(id));
      list.appendChild(b);
      actionEls[id] = { btn: b, sub: b.querySelector(".sub") };
    }
    $("btn-new").addEventListener("click", () => { opponentKind = $("opp").value; newMatch(); });
    $("btn-help").addEventListener("click", toggleHelp);
    $("btn-help-close").addEventListener("click", toggleHelp);
    $("btn-start").addEventListener("click", setupStart);
    $("btn-result").addEventListener("click", resultBtn);
    window.addEventListener("resize", fit);
    fit();
  }
  function fit() {
    const availW = Math.max(200, window.innerWidth - 32), availH = Math.max(150, window.innerHeight - 24);
    const s = Math.min(availW / W, availH / H);
    $("stage").style.transform = `scale(${s})`;
    $("frame").style.width = W * s + "px";
    $("frame").style.height = H * s + "px";
    const dpr = Math.min(window.devicePixelRatio || 1, 2), want = Math.round(W * s * dpr);
    if (canvas.width !== want) { canvas.width = want; canvas.height = Math.round(H * s * dpr); }
  }
  let last = performance.now();
  function frame(now) {
    const dt = Math.min((now - last) / 1000, MAX_DT);
    last = now;
    if (game) {
      clock += dt;
      updateToasts(dt);
      view.mode = currentView();
      const ui = overUi || overlayOpen();
      if (!ui) { lastGameMouse = mouse; currentGaze = gazeTarget(mouse); }
      view.my_gaze = currentGaze;
      view.hover_index = myCardTurn() && !ui ? cardAt(mouse) : -1;
      view.hover_pick = ui ? "" : pickAt(mouse);
      if ($("help").hidden) for (let i = 0; i < speed; i++) game.tick(dt, currentGaze);
      drain();
      const spot = $("spot");
      spot.hidden = !$("chk-spot").checked || !$("setup").hidden;
      if (!spot.hidden) spot.style.background = `radial-gradient(circle at ${lastGameMouse[0]}px ${lastGameMouse[1]}px, rgba(0,0,0,0) 115px, rgba(0,0,0,0.62) 210px)`;
      refresh();
      drawTable();
    }
    requestAnimationFrame(frame);
  }
  // 시험용 손잡이 (Playwright): 지금 매치·화면 상태
  window.__gm = { get game() { return game; }, get view() { return view; }, newMatch, setupStart, act, callDown, callUp,
    setSpeed(n) { speed = Math.max(1, Math.min(16, Math.floor(n))); } };
  build();
  newMatch();
  GameLog.info("WEB", { event: "ready", version: "v0.8.0-web.1" });
  requestAnimationFrame(frame);
})();
