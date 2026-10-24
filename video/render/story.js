// VERSION: v1.7 — 2026-10-24 — 화면에 투자 영어 허용 (사용자 지시 "국기를 할 필요는 없잖아 그냥 KOSPI, S&P500 이거 달면 되는데 … buy, sell 같은것도
//   그렇고 다 알만한건 넣어도 돼" · "모든 나라 사람들이 보기에 한번에 이해가 되도록 근데 미흡하지 않도록 전력을 다해"): SPEC.allowWords (stock/story/screen_words.txt)
//   → K.init allowWords (render.mjs v1.25 가 목록 밖 영어·한국어를 잡음) · 화면 위 이름표 탭 title= (KOSPI·S&P 500·RULE 1 …) · K5 글자 칩 'TEXT
//   (! 빨간 ✗ · + 청록 ✓) · LIST 화면 (줄마다 ✓/✗ + 짧은 영어, 문장 번호에 나타남) · 그림 chip(반도체)·briefcase·school.
// (v1.6) — 2026-10-24 — 소품 그림 21장이 올라와 still 로 보니 BIG 숫자와 같이 쓰는 소품(차단기·동전 나무)이 작아 보임 → 상자 [6.2, 4.0] → [6.6, 4.7].
// (v1.5) — 2026-10-23 — 배경을 화면 아래 끝까지 (ChatGPT 배경 5장이 올라와 still 로 보니 아래 약 10% — 쇼츠 15% — 가 빈 남색 띠, 바닥 줄도
//   인형 발보다 높았음): bg y 0.35 → −2.8 · w 54 → 56 (쇼츠 y 0.2 → −4.4 · w 40 → 44) — 바닥 줄(그림 높이 80%)이 화면 약 74%(쇼츠 81%).
// (v1.4) — 2026-10-23 — ① 정리 카드(K6) 뺌 (사용자 지시 "그냥 정리 부분은 빼자"). ② 설명 소품 그림 (사용자 지시 "설명에 필요한 이미지 요소들은
//   왜 생성안해?"): SPEC.props = {이름: 'props/<이름>.png'} (ChatGPT 종이 소품 — stock/story/puppet/props_chatgpt.md) · 장면의 props 는 무대 위
//   종이 인형처럼 섬 (롱폼: 오른쪽 바닥 · 쇼츠: 위 가운데에 떠 있음) · 튀어나옴(pop)·솟아오름(rise) · 같은 자리 다음 소품이 나오면 앞 소품은 사라짐 ·
//   BIG 과 같이 쓰면 숫자는 소품 위로 (그림이 없으면 puppet.js 임시 그림).
// (v1.3) — 2026-10-23 — 화면에 영어도 없음 (사용자 지시 "야 영어 문구도 넣지마"): noLatin (render.mjs v1.24 — 라틴 글자 하나도 문제) · 화 배지 '#N' ·
//   BIG icon= (KOSPI·S&P 500·SOXL 같은 이름 대신 국기·×3 그림).
// (v1.2) — 2026-10-23 — 화면에 한국어 없음 (사용자 지시 "외국인 대상으로도 할거니까 그것도 고려해 영상에 한글 문구 사용하지 말고 최대한
//   이해 잘되도록"): K6 정리 카드 = 번호 + 그림 줄 · PIE 원그래프 · 그림 kr·us(국기)·pct(금리 %)·fx(₩⇄$)·people·chart · K5 화살표 칸 · K4·PIE 단위 그림(icon=).
// (v1.1) — 2026-10-23 — SPEC.introOk(제작안 '- 도입 통과:' 줄) → K.init introOk (render.mjs v1.22 도입 마지노선 35초 검사에서 경고로).
// (v1.0) — 2026-10-23 — 새로: '개미 재기 일지' 종이인형극 장면 묶음 — 장면 표(stock/source/<영상ID>/scenes.txt)를 tools/story_kit.py scenes 가
//   SPEC(JSON)으로 바꿔 작은 index.html 에 넣으면, 이 파일이 무대·인형·코드 화면을 만든다. 사용자 지시 2026-10-23 "주제 탐색 -> 요약본 만들기 -> 대본,
//   썸네일 프롬프트 등 영상 소스 -> 영상 만들기 과정을 토큰을 가장 덜 사용하는 구조로 만들어봐" — 영상마다 장면 코드를 손으로 쓰지 않는다
//   (일본 축제 롱폼 index.html 은 손으로 쓴 106KB). 장면 표 한 줄 = 장면 하나.
//   · 무대 = video/render/puppet.js v1.1 (배경 1장 + 표정 있는 인형 투명 PNG, 움직임은 코드) — 그림이 없으면 임시 그림.
//   · 코드 화면: K1 계좌(금액이 굴러감) · K2 연표 · K3 차트(선이 그려짐, 기준 = 노란 점선) · K4 막대 · K5 아이콘 · K7 화 배지 · BIG 큰 숫자 · PIE (v1.4 K6 정리 카드 없음).
//   · 시각은 모두 문장 번호(K.S·K.E·K.W) — 오디오가 바뀌어도 장면 표를 고치지 않는다.
//   · 화면 글자는 숫자·기호만 (주식 noWords) — v1.2 부터 K6 정리 카드도 그림 (한국어 없음).
//   · 롱폼 1920×1080 · 쇼츠 SPEC.vertical (1080×1920 — 화면은 위, 인형은 아래).
//   연구·교육용 영상 도구 — 투자 권유 아님.
(function () {
  "use strict";
  const S_ = (window.Story = {});
  S_.VERSION = "v1.7";
  S_.POSES = { BONSEOK: "P-BONSEOK.png", WALK: "P-BONSEOK-WALK.png", PHONE: "P-BONSEOK-PHONE.png", DESPAIR: "P-BONSEOK-DESPAIR.png",
    RESOLVE: "P-BONSEOK-RESOLVE.png", STUDY: "P-BONSEOK-STUDY.png", BACK: "P-BONSEOK-BACK.png", SMILE: "P-BONSEOK-SMILE.png", CROWD: "P-CROWD.png" };
  S_.BGS = { "HOME-NIGHT": "P-HOME-NIGHT.jpg", OFFICE: "P-OFFICE.jpg", "STREET-DAWN": "P-STREET-DAWN.jpg", BOARD: "P-BOARD.jpg", PAPER: "P-PAPER.jpg" };
  const COOL_POSE = new Set(["PHONE", "DESPAIR"]);
  const COL = { R: "#FF4D3D", G: "#22C7B0", Y: "#FFD400", W: "#F4F6FA" };
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
  const num = s => parseFloat(String(s).replace(/[^\d.\-−]/g, "").replace("−", "-"));
  // v1.7 글자 폭 (글자 크기 1 기준) — 영어 대문자·₩ 는 숫자보다 넓다 (BIG 'USD/KRW ↑' 가 칸 밖으로 나갔음)
  const textW = t => [...String(t)].reduce((w, ch) => w + (/[A-Z₩W&%$]/.test(ch) ? 0.74 : /[0-9]/.test(ch) ? 0.58 : /\s/.test(ch) ? 0.3 : /[a-z]/.test(ch) ? 0.56 : 0.62), 0);

  // 아이콘 (K5) — 글자 없는 그림 · 48×48 칸
  const ICON = {
    basket: `<path d="M8 20h32l-4 20H12z" fill="#D9A441"/><path d="M15 20l9-11 9 11" fill="none" stroke="#F2E6CF" stroke-width="3"/><circle cx="18" cy="29" r="3" fill="#B3202A"/><circle cx="26" cy="31" r="3" fill="#3E8E87"/><circle cx="32" cy="28" r="3" fill="#FFD400"/>`,
    drop: `<path d="M24 6C18 16 12 23 12 30a12 12 0 0024 0c0-7-6-14-12-24z" fill="#5AA9E6"/>`,
    debt: `<rect x="6" y="12" width="36" height="24" rx="4" fill="#B3202A"/><text x="24" y="31" font-size="16" font-weight="900" text-anchor="middle" fill="#fff">₩−</text>`,
    swap: `<path d="M8 17h28l-6-6M40 31H12l6 6" fill="none" stroke="#F2E6CF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>`,
    x3: `<rect x="6" y="10" width="36" height="28" rx="6" fill="#B3202A"/><text x="24" y="31" font-size="17" font-weight="900" text-anchor="middle" fill="#fff">×3</text>`,
    hourglass: `<path d="M14 6h20M14 42h20M16 6c0 10 16 12 16 18S16 32 16 42M32 6c0 10-16 12-16 18s16 8 16 18" fill="none" stroke="#D9A441" stroke-width="3.5" stroke-linecap="round"/>`,
    calendar: `<rect x="7" y="10" width="34" height="30" rx="4" fill="#F2E6CF"/><rect x="7" y="10" width="34" height="9" rx="4" fill="#B3202A"/><circle cx="17" cy="28" r="3" fill="#1E2A4A"/><circle cx="31" cy="28" r="3" fill="#3E8E87"/>`,
    phone: `<rect x="14" y="5" width="20" height="38" rx="4" fill="#2B2B2B" stroke="#F2E6CF" stroke-width="2.5"/><path d="M18 30l5-6 4 3 4-7" fill="none" stroke="#FF4D3D" stroke-width="2.5"/>`,
    book: `<path d="M6 10c7-2 13-1 18 3 5-4 11-5 18-3v28c-7-2-13-1-18 3-5-4-11-5-18-3z" fill="#F2E6CF"/><path d="M24 13v28" stroke="#1E2A4A" stroke-width="2.5"/>`,
    up: `<path d="M6 38l12-12 8 7 15-17" fill="none" stroke="#22C7B0" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M33 15h9v9" fill="none" stroke="#22C7B0" stroke-width="4.5" stroke-linecap="round"/>`,
    down: `<path d="M6 12l12 12 8-7 15 17" fill="none" stroke="#FF4D3D" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M33 35h9v-9" fill="none" stroke="#FF4D3D" stroke-width="4.5" stroke-linecap="round"/>`,
    bell: `<path d="M24 7c-7 0-11 5-11 12v9l-4 6h30l-4-6v-9c0-7-4-12-11-12z" fill="#D9A441"/><circle cx="24" cy="38" r="4" fill="#D9A441"/>`,
    lock: `<rect x="10" y="21" width="28" height="20" rx="4" fill="#D9A441"/><path d="M16 21v-6a8 8 0 0116 0v6" fill="none" stroke="#F2E6CF" stroke-width="4"/>`,
    globe: `<circle cx="24" cy="24" r="17" fill="#3E8E87"/><path d="M7 24h34M24 7c-8 9-8 25 0 34M24 7c8 9 8 25 0 34" fill="none" stroke="#F2E6CF" stroke-width="2.5"/>`,
    coin: `<circle cx="24" cy="24" r="16" fill="#D9A441"/><circle cx="24" cy="24" r="11" fill="none" stroke="#F2E6CF" stroke-width="2.5"/><text x="24" y="30" font-size="15" font-weight="900" text-anchor="middle" fill="#1E2A4A">₩</text>`,
    house: `<path d="M8 24L24 10l16 14v16H8z" fill="#F2E6CF"/><rect x="20" y="29" width="8" height="11" fill="#1E2A4A"/>`,
    // v1.2 언어 없이 뜻이 보이는 그림 (외국인 시청자 — 사용자 지시 2026-10-23 "외국인 대상으로도 할거니까 … 영상에 한글 문구 사용하지 말고")
    kr: `<rect x="3" y="9" width="42" height="30" rx="2" fill="#FFFFFF" stroke="#BFB29A" stroke-width="1"/><path d="M17 24a7 7 0 0 1 14 0z" fill="#CD2E3A"/><path d="M17 24a7 7 0 0 0 14 0z" fill="#0047A0"/><g stroke="#111" stroke-width="1.6"><path d="M7 15l4-3M8 16.5l4-3M9 18l4-3M35 34l4-3M36 35.5l4-3M37 37l4-3M37 12l4 3M36 13.5l4 3M35 15l4 3M7 31l4 3M8 32.5l4 3M9 34l4 3"/></g>`,
    us: `<rect x="3" y="9" width="42" height="30" rx="2" fill="#FFFFFF" stroke="#BFB29A" stroke-width="1"/><g fill="#B22234"><rect x="3" y="9" width="42" height="3"/><rect x="3" y="15" width="42" height="3"/><rect x="3" y="21" width="42" height="3"/><rect x="3" y="27" width="42" height="3"/><rect x="3" y="33" width="42" height="3"/></g><rect x="3" y="9" width="19" height="15" fill="#3C3B6E"/><g fill="#fff"><circle cx="7" cy="13" r="1"/><circle cx="12" cy="13" r="1"/><circle cx="17" cy="13" r="1"/><circle cx="9.5" cy="17" r="1"/><circle cx="14.5" cy="17" r="1"/><circle cx="7" cy="21" r="1"/><circle cx="12" cy="21" r="1"/><circle cx="17" cy="21" r="1"/></g>`,
    pct: `<circle cx="24" cy="24" r="17" fill="#D9A441"/><text x="24" y="31" font-size="20" font-weight="900" text-anchor="middle" fill="#1E2A4A">%</text>`,
    fx: `<rect x="3" y="12" width="42" height="24" rx="5" fill="#3E8E87"/><text x="24" y="29" font-size="12" font-weight="900" text-anchor="middle" fill="#fff">₩⇄$</text>`,
    people: `<g fill="#F2E6CF"><circle cx="14" cy="17" r="5"/><circle cx="34" cy="17" r="5"/><path d="M5 38c0-8 4-13 9-13s9 5 9 13z"/><path d="M25 38c0-8 4-13 9-13s9 5 9 13z"/></g><circle cx="24" cy="14" r="6" fill="#D9A441"/><path d="M13 40c0-10 5-15 11-15s11 5 11 15z" fill="#D9A441"/>`,
    // v1.7 반도체 칩 · 회사(서류 가방) · 학원(책가방)
    chip: `<rect x="12" y="12" width="24" height="24" rx="3" fill="#2F6B4F"/><rect x="18" y="18" width="12" height="12" rx="1.5" fill="#D9A441"/><g stroke="#C9D1E0" stroke-width="2.5" stroke-linecap="round"><path d="M17 6v6M24 6v6M31 6v6M17 36v6M24 36v6M31 36v6M6 17h6M6 24h6M6 31h6M36 17h6M36 24h6M36 31h6"/></g>`,
    briefcase: `<rect x="6" y="16" width="36" height="24" rx="4" fill="#8B5A2B"/><path d="M18 16v-5h12v5" fill="none" stroke="#F2E6CF" stroke-width="3"/><rect x="6" y="25" width="36" height="3" fill="#5C3A1A"/>`,
    school: `<path d="M12 14c0-5 5-8 12-8s12 3 12 8v26H12z" fill="#3E6FB0"/><rect x="16" y="24" width="16" height="10" rx="2" fill="#F2E6CF"/><path d="M18 8c2-3 10-3 12 0" fill="none" stroke="#1E2A4A" stroke-width="2.5"/>`,
    chart: `<rect x="6" y="28" width="7" height="12" fill="#3E8E87"/><rect x="17" y="20" width="7" height="20" fill="#3E8E87"/><rect x="28" y="12" width="7" height="28" fill="#D9A441"/><path d="M5 41h38" stroke="#F2E6CF" stroke-width="2.5"/>`,
  };
  const ARROW = `<path d="M6 24h30M28 14l10 10-10 10" fill="none" stroke="#FFD400" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>`;
  const SMALL = 'data-small="아이콘 안 기호 — viewBox 48 을 크게 늘려 그림 (실제 크기는 큼)"';
  const icon = (x, sz, cls) => `<svg class="${cls || "k5i"}" ${SMALL} width="${sz}" height="${sz}" viewBox="0 0 48 48" aria-hidden="true">${x.arrow ? ARROW : (ICON[x.k] || ICON.coin) + mark(x.m)}</svg>`;
  S_.ICONS = Object.keys(ICON);
  const mark = (k) => k === "!" ? `<path d="M8 8l32 32M40 8L8 40" stroke="#FF4D3D" stroke-width="5" stroke-linecap="round"/>`
    : k === "+" ? `<path d="M10 26l9 9 19-21" fill="none" stroke="#22C7B0" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>` : "";

  S_.build = function (SPEC) {
    const V = !!SPEC.vertical, SW = V ? 1080 : 1920;
    const words = Array.isArray(SPEC.allowWords) ? { allowWords: SPEC.allowWords } : { noWords: true, noLatin: true };   // v1.7 투자 영어 허용 목록
    K.init(window.EP, Object.assign({ subtitles: false, chip: false }, words, { introPart: SPEC.vertical ? undefined : "도입", introOk: !!SPEC.introOk, testFrom: SPEC.testFrom || undefined, w: SW }));
    const { S, E, W, el, pop, out } = K, tl = K.tl;
    const { lin, lerp, seg } = Puppet.u;
    const N = window.EP.sent.length;
    const at = (n, word) => (word ? W(n, word) : S(n));
    const files = {};
    for (const [k, f] of Object.entries(S_.BGS)) files["BG_" + k] = { f, kind: "bg" };
    for (const [k, f] of Object.entries(S_.POSES)) files[k] = { f };
    for (const [k, f] of Object.entries(SPEC.props || {})) files["PROP_" + k] = { f, kind: "sq", label: k };   // v1.4 소품 (정사각 투명 PNG)
    const ST = Puppet.stage({ dir: SPEC.dir, files, w: SW, h: V ? 1920 : 1080 });
    el(`<div class="vig"></div>`);
    // 무대 자리 — 롱폼: 인형 L·C·R, 화면은 오른쪽 칸 / 쇼츠: 인형 아래 가운데, 화면은 위 칸
    const X = V ? { L: -1.7, C: 0, R: 1.7 } : { L: -5.6, C: 0, R: 5.6 };
    const PH = V ? 5.0 : 7.0, CH = V ? 2.4 : 4.8;
    const PANEL = V ? { cx: 540, top: 250, w: 940, h: 560 } : { cx: 1370, top: 170, w: 960, h: 600 };   // v1.7 롱폼 칸 800 → 960 (글자 칩·목록이 작았음)
    const LOOK_Y = V ? 3.6 : 3.34;
    const WARM = new THREE.Color(0xffffff), COOL = new THREE.Color(0xb4b9cc);

    // ---------- 코드 화면 ----------
    let lastP = PANEL;                                             // v1.7 마지막으로 만든 칸 (이름표 탭 자리)
    const fitP = hh => ({ cx: PANEL.cx, w: PANEL.w, h: hh, top: Math.round(PANEL.top + (PANEL.h - hh) / 2) });   // 내용 높이에 맞춘 칸 (가운데 그대로)
    const panel = (sc, cls, inner, P) => (lastP = P || PANEL, el(`<div class="kp ${cls || ""}" style="left:${(P || PANEL).cx - (P || PANEL).w / 2}px;top:${(P || PANEL).top}px;width:${(P || PANEL).w}px;height:${(P || PANEL).h}px">${inner || ""}</div>`, sc));
    const SCREEN = {
      K1(sc, s, t0) {                                              // 계좌: 금액이 from → to 로 굴러감 (빨강 손해 · 청록 회복)
        const from = num(s.from), to = num(s.to), c = to < from ? COL.R : COL.G, pct = from ? (to - from) / from * 100 : 0;
        const p = panel(sc, "k1", `<div class="k1cap">₩</div><div class="k1n w9 nw" style="color:${c}"></div>` +
          `<div class="k1d w9 nw" style="color:${c}">${pct < 0 ? "▼" : "▲"} ${Math.abs(pct).toFixed(1)}%</div>`);
        const n = p.querySelector(".k1n"), d = p.querySelector(".k1d");
        pop(p, t0); K.counter(n, from, to, t0 + 0.3, 1.6, v => Math.round(v).toLocaleString("en-US"));
        pop(d, t0 + 1.9);
        return t0 + 2.2;
      },
      K2(sc, s, t0) {                                              // 연표: 해마다 점, 그 화의 해만 빛남
        const ys = s.years, n = ys.length, w = PANEL.w - 120, step = n > 1 ? w / (n - 1) : 0;
        let h = `<div class="k2l"></div>`;
        ys.forEach((y, i) => {
          const on = s.hl.includes(String(y)), x = 60 + i * step, lab = on || n <= 5 || i === 0 || i === n - 1;   // 해가 많으면 처음·끝·빛나는 해만 글자
          h += `<div class="k2d${on ? " on" : ""}" style="left:${x}px"></div>` + (lab ? `<div class="k2y w9 nw${on ? " Y" : ""}" style="left:${x}px">${esc(y)}</div>` : "");
        });
        const p = panel(sc, "k2", h);
        pop(p, t0);
        p.querySelectorAll(".k2d.on").forEach((d, i) => tl.fromTo(d, { scale: 0.4 }, { scale: 1, duration: 0.5, ease: "back.out(2)" }, t0 + 0.5 + i * 0.3));
        return t0 + 1.2;
      },
      K3(sc, s, t0) {                                              // 차트: 선이 그려짐 · 기준(base) = 노란 점선 · 아래 x 이름(숫자)
        const v = s.values, base = s.base, lo = Math.min(...v, base == null ? Infinity : base), hi = Math.max(...v, base == null ? -Infinity : base);
        const VW = PANEL.w - 80, VH = PANEL.h - 170, py = y => 20 + (hi === lo ? VH / 2 : (hi - y) / (hi - lo) * (VH - 40));
        const pts = v.map((y, i) => [20 + i * (VW - 40) / Math.max(1, v.length - 1), py(y)]);
        let len = 0; for (let i = 1; i < pts.length; i++) len += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]);
        const c = v[v.length - 1] < v[0] ? COL.R : COL.G, last = pts[pts.length - 1];
        const baseLine = base == null ? "" : `<line x1="0" x2="${VW}" y1="${py(base)}" y2="${py(base)}" stroke="${COL.Y}" stroke-width="6" stroke-dasharray="18 14"/>`;
        const labs = (s.labels || []).map((l, i, A) => {
          const x = A.length === v.length ? pts[i][0] : 20 + i * (VW - 40) / Math.max(1, A.length - 1);
          return `<div class="k3x w9 nw" style="left:${40 + x}px">${esc(l)}</div>`;
        }).join("");
        const p = panel(sc, "k3", `<svg class="a" style="left:40px;top:40px" width="${VW}" height="${VH}" viewBox="0 0 ${VW} ${VH}" aria-hidden="true">${baseLine}` +
          `<polyline class="k3p" points="${pts.map(q => q.join(",")).join(" ")}" fill="none" stroke="${c}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="${len}" stroke-dashoffset="${len}"/>` +
          `<circle class="k3e" cx="${last[0]}" cy="${last[1]}" r="16" fill="${c}"/></svg>${labs}` +
          (s.end ? `<div class="k3v w9 nw" style="color:${c};left:${Math.min(PANEL.w - 40, 40 + last[0])}px;top:${Math.max(0, 40 + last[1] - 110)}px">${esc(s.end)}</div>` : ""));
        pop(p, t0);
        const dur = s.dur || 2.4;
        tl.fromTo(p.querySelector(".k3p"), { strokeDashoffset: len }, { strokeDashoffset: 0, duration: dur, ease: "none" }, t0 + 0.4);
        tl.fromTo(p.querySelector(".k3e"), { opacity: 0 }, { opacity: 1, duration: 0.2 }, t0 + 0.4 + dur);
        const ev = p.querySelector(".k3v"); if (ev) pop(ev, t0 + 0.5 + dur);
        return t0 + 0.6 + dur;
      },
      K4(sc, s, t0) {                                              // 막대: 아래 이름(숫자·기호) · 위 값 · 색은 부호 또는 지정
        const it = s.items, n = it.length, mx = Math.max(...it.map(x => Math.abs(num(x.val)) || 0), 1e-9);
        const bw = Math.min(150, (PANEL.w - 80) / (n * 1.55)), gap = (PANEL.w - n * bw) / (n + 1), H = PANEL.h - 230;
        let h = "";
        it.forEach((x, i) => {
          const v = Math.abs(num(x.val)) || 0, hh = Math.max(8, v / mx * H), c = COL[x.c] || (num(x.val) < 0 ? COL.R : COL.G), left = gap + i * (bw + gap);
          h += `<div class="k4b" style="left:${left}px;width:${bw}px;height:${hh}px;background:${c}"></div>` +
            `<div class="k4v w9 nw" style="left:${left + bw / 2}px;bottom:${110 + hh + 14}px;color:${c}">${esc(x.val)}</div>` +
            `<div class="k4l w9 nw" style="left:${left + bw / 2}px">${esc(x.lab)}</div>`;
        });
        if (s.icon) h += `<div style="position:absolute;left:24px;top:18px">${icon({ k: s.icon }, 90, "k4i")}</div>`;   // v1.2 단위를 그림으로 (모래시계 = 기간)
        const p = panel(sc, "k4", h);
        pop(p, t0);
        p.querySelectorAll(".k4b").forEach((b, i) => K.grow(b, t0 + 0.4 + i * 0.35, 0.7, "y"));
        p.querySelectorAll(".k4v").forEach((b, i) => pop(b, t0 + 0.9 + i * 0.35));
        return t0 + 1.1 + n * 0.35;
      },
      K5(sc, s, t0) {                                              // 아이콘 칸: '!' = 빨간 ×(하지 않음) · '+' = 청록 ✓(할 것)
        const it = s.icons, n = it.length, gap = 22;
        // v1.7 칸 너비를 다 쓰는 크기 u: 그림·화살표 = u, 글자 칩 = 0.55u × (글자 폭 + 안쪽 여백 1.0 (+ ✓ 1.0)) + 테두리
        const den = it.reduce((d, x) => d + (x.t != null ? 0.55 * (textW(x.t) + 1.0 + (x.m === "+" ? 1.0 : 0)) : 1), 0);
        const sz = Math.min(170, Math.floor((PANEL.w - 80 - gap * (n - 1) - 14 * it.filter(x => x.t != null).length) / den));
        const chip = x => {                                          // v1.7 글자 칩 (KOSPI·S&P 500·BUY …)
          const fs = Math.max(40, Math.min(94, Math.floor(sz * 0.55)));
          return `<span class="k5i k5t w9 nw${x.m === "!" ? " no" : x.m === "+" ? " yes" : ""}" style="font-size:${fs}px">${x.m === "+" ? "✓ " : ""}${esc(x.t)}</span>`;
        };
        const h = it.map(x => x.t != null ? chip(x) : icon(x, sz)).join("");   // v1.2 '>' = 화살표 칸
        const p = panel(sc, "k5", `<div class="k5r">${h}</div>`, fitP(Math.max(240, sz + 160)));   // v1.7 한 줄 높이에 맞춘 칸
        pop(p, t0);
        p.querySelectorAll(".k5i").forEach((b, i) => pop(b, t0 + 0.3 + i * 0.3, { from: { scale: 0.5, y: 0 } }));
        return t0 + 0.6 + n * 0.3;
      },
      BIG(sc, s, t0, t1, o) {                                      // 큰 숫자·기호 하나 · v1.4 소품이 있으면 소품 위 한 줄 (그림 + 숫자)
        const withProp = !!(o && o.prop), wMax = withProp ? PANEL.w + 120 : PANEL.w;
        const c = COL[s.c] || COL.W, size = Math.min(withProp ? (V ? 140 : 150) : (V ? 170 : 190), Math.floor(wMax * 0.9 / (textW(s.text) + (withProp && s.icon ? 1.2 : 0))));   // v1.2 글자 수에 맞춰 (칸 밖으로 넘지 않게)
        const ic = s.icon ? `<div class="kbigi">${icon({ k: s.icon }, withProp ? Math.round(size * 1.1) : Math.min(V ? 170 : 180, Math.round(size * 1.05)), "k4i")}</div>` : "";   // v1.3 무엇의 숫자인지 그림으로 (국기·×3 …)
        const top = withProp ? (V ? 305 : 250) : PANEL.top + PANEL.h / 2;
        const p = el(`<div class="kbig w9 nw${withProp ? " row" : ""}" style="left:${PANEL.cx}px;top:${top}px;font-size:${size}px;color:${c}">${ic}<span>${esc(s.text)}</span></div>`, sc);
        pop(p, t0, { from: { scale: 0.6, y: 0 } });
        return t0 + 0.6;
      },
      PIE(sc, s, t0) {                                             // v1.2 원그래프: 전체 중 몫 (몫 = 색 · 가운데 글자 = 숫자·기호만)
        const v = Math.max(0, Math.min(100, s.value)), c = COL[s.c] || COL.R, R = (V ? 190 : 200) - (s.cap ? 40 : 0), L = 2 * Math.PI * R;   // v1.7 cap 이 있으면 조금 작게
        const sz = 2 * R + 80, lab = s.label || `${v}%`;
        const svg = `<svg width="${sz}" height="${sz}" viewBox="0 0 ${sz} ${sz}" aria-hidden="true"><circle cx="${sz / 2}" cy="${sz / 2}" r="${R}" fill="none" stroke="rgba(255,255,255,.16)" stroke-width="70"/>` +
          `<circle class="kpie" cx="${sz / 2}" cy="${sz / 2}" r="${R}" fill="none" stroke="${c}" stroke-width="70" stroke-dasharray="${L}" stroke-dashoffset="${L}" transform="rotate(-90 ${sz / 2} ${sz / 2})"/></svg>`;
        const p = panel(sc, "kpiep", `<div style="position:absolute;left:50%;top:${s.cap ? 44 : 50}%;transform:translate(-50%,-50%)">${svg}</div>` +
          `<div class="kpiel w9 nw" style="color:${c}${s.cap ? ";top:44%" : ""}">${esc(lab)}</div>` + (s.cap ? `<div class="kpiec w9 nw">${esc(s.cap)}</div>` : "") + (s.icon ? `<div style="position:absolute;left:24px;top:18px">${icon({ k: s.icon }, 90, "k4i")}</div>` : ""));
        pop(p, t0);
        tl.fromTo(p.querySelector(".kpie"), { strokeDashoffset: L }, { strokeDashoffset: L * (1 - v / 100), duration: 1.2, ease: "power2.out" }, t0 + 0.3);
        pop(p.querySelector(".kpiel"), t0 + 1.3, { from: { scale: 0.7, y: 0 } });
        return t0 + 1.6;
      },
      LIST(sc, s, t0, t1) {                                         // v1.7 줄마다 ✓/✗ + 짧은 영어 (원칙 목록 등) — 줄은 그 문장에 나타남
        const n = s.items.length, longest = Math.max(...s.items.map(x => textW(x.t)));
        const fs = Math.max(40, Math.min(V ? 64 : 62, Math.floor((PANEL.h - 80) / n / 1.9), Math.floor((PANEL.w - 100) / (longest + 1.5))));   // 가장 긴 줄이 칸 안에
        const mk = m => m === "!" ? `<svg ${SMALL} width="${fs}" height="${fs}" viewBox="0 0 48 48" aria-hidden="true">${mark("!")}</svg>`
          : `<svg ${SMALL} width="${fs}" height="${fs}" viewBox="0 0 48 48" aria-hidden="true">${mark("+")}</svg>`;
        const p = panel(sc, "klist", `<div class="klin">${s.items.map(x => `<div class="klr"><span class="klm">${mk(x.m)}</span><span class="w9 nw" style="font-size:${fs}px;color:${x.m === "!" ? COL.R : COL.W}">${esc(x.t)}</span></div>`).join("")}</div>`, fitP(Math.min(PANEL.h, Math.round(n * fs * 1.9 + 110))));
        pop(p, t0);
        const step = Math.max(0.35, Math.min(1.0, (t1 - t0 - 0.6) / Math.max(1, n)));
        let last = t0;
        p.querySelectorAll(".klr").forEach((r, i) => { const ti = s.items[i].at ? at(s.items[i].at[0], s.items[i].at[1]) : t0 + 0.4 + i * step; last = Math.max(last, ti); pop(r, ti, { from: { y: 16 } }); });
        return last + 0.4;
      },
    };

    // ---------- 인형 ----------
    function addActor(st, pz) {
      const crowd = pz.pose === "CROWD", x = X[pz.pos || "C"];
      const a = st.actor(pz.pose, { h: crowd ? CH : PH, at: [x, 0, crowd ? -1.2 : 0], flip: !!pz.flip });
      a.pz = pz; return a;
    }
    // v1.4 소품 — 롱폼: 오른쪽 바닥에 섬 (BIG 이 있으면 낮게 — 숫자는 위) · 쇼츠: 위 가운데에 떠 있음 (인형은 아래)
    const PX1 = { L: -5.6, C: 0.2, R: 5.4 }, PX2 = { L: -5.6, C: 1.3, R: 6.5 };   // 소품 하나 · 둘 (둘이면 인형 책상과 닿지 않게 오른쪽으로)
    function addProp(st, p, n, big) {
      const fit = V ? (big ? [4.4, 2.1] : [5.2, 3.0]) : n > 1 ? (big ? [4.2, 3.6] : [4.6, 4.6]) : (big ? [6.6, 4.7] : [7.0, 5.6]);   // v1.6 BIG 과 같이 쓰는 소품 4.0 → 4.7 (작아 보였음)
      const at = V ? [0, big ? 6.2 : 6.8, 0.3] : [(n > 1 ? PX2 : PX1)[p.pos || "R"], 0, 0.3];   // 쇼츠: 인형 머리·#N 배지와 닿지 않게
      const a = st.actor("PROP_" + p.prop, { fit, at, anchor: V ? [0.5, 0.5] : [0.5, 1] });
      a.pz = p; return a;
    }
    function moveProp(a, t, sa, k) {
      const pz = a.pz, t0 = pz.from != null ? pz.from : sa + 0.2;
      if (!pz.cont) { if (pz.move === "rise") a.rise(t, t0, 0.6, 2.5); else a.pop(t, t0, 0.45); }
      if (pz.until != null) a.hide(t, pz.until, 0.25);
      a.sway(t, 0.012, 0.45, k + 3);
    }
    function moveActor(a, t, sa, sb, k) {                          // k = 이 장면에서 몇 번째 인형 (흔들림 위상)
      const pz = a.pz, t0 = pz.from != null ? pz.from : sa, side = (a.home.x < 0 ? -1 : 1) || -1;
      if (pz.from != null) a.flip(t, t0, 0.35);                     // 장면 안에서 자세가 바뀜 → 종이 카드 뒤집듯
      else if (!pz.cont) {
        if (pz.move === "walk") { a.g.position.x = a.home.x + lerp(side * 6, 0, Puppet.u.outC(lin(t, t0, t0 + Math.min(3, (sb - t0) * 0.6)))); a.bob(t, 0.09, 2.1, k); }
        else if (pz.move === "rise") a.rise(t, t0, 0.6, 3);
        else if (pz.move === "pop") a.pop(t, t0 + 0.05, 0.45);
        else a.slide(t, t0, 0.7, side * 5);
      }
      if (pz.until != null) a.hide(t, pz.until, 0.2);
      const settled = t > t0 + 0.75;
      switch (pz.pose) {
        case "PHONE": if (settled) a.jitter(t, 0.008); break;
        case "DESPAIR": a.sway(t, 0.012, 0.35, k); break;
        case "SMILE": a.bob(t, 0.12, 2.2, k); break;
        case "CROWD": a.bob(t, 0.2, 3.0, k); break;
        case "WALK": if (pz.move !== "walk") a.bob(t, 0.07, 2.0, k); break;
        default: a.sway(t, 0.018, 0.6, k);
      }
    }

    // ---------- 장면 ----------
    const scenes = SPEC.scenes, ep = SPEC.ep;
    let lastEnd = 0;
    scenes.forEach((s, i) => {
      // 장면 시각: 문장 a~b — 다음 장면 시작 0.25초 전까지 (v1.4 정리 카드 없음)
      const a = i === 0 ? 0 : S(s.a) - 0.25;
      const nx = scenes[i + 1];
      const b = !nx ? K.D : S(nx.a) - 0.25;
      const timed = list => (list || []).map(p => Object.assign({}, p, { from: p.at != null ? at(p.at[0], p.at[1]) : null, until: null }));
      // 같은 자리에 다음 것이 나오면 앞 것은 그 시각에 사라짐 (인형은 인형끼리 · 소품은 소품끼리)
      const handoff = L => L.forEach((p, k) => { const nxt = L.slice(k + 1).find(q => q.from != null && (q.pos || "C") === (p.pos || "C")); if (nxt) p.until = nxt.from; });
      const pz = timed(s.puppets), pr = timed(s.props);
      handoff(pz); handoff(pr);
      const big = !!(s.screen && s.screen.type === "BIG");
      const cool = pz.some(p => p.from == null && COOL_POSE.has(p.pose));
      const actors = [], propActs = [];
      const set = ST.set(a, b, st => {
        // v1.5 배경이 화면 아래까지 (예전 y 0.35·w 54 는 아래 약 10% — 쇼츠 15% — 가 빈 띠) · 바닥 줄(그림 높이 80%)이 인형 발 높이 근처
        st.bg("BG_" + (s.bg || "PAPER"), { v: 0.8, y: V ? -4.4 : -2.8, w: V ? 44 : 56 });
        pz.forEach(p => actors.push(addActor(st, p)));
        pr.forEach(p => propActs.push(addProp(st, p, new Set(pr.map(q => q.pos)).size, big)));
        st.part(Puppet.floaters(cool ? { n: 40, inner: "rgba(180,200,255,1)", outer: "rgba(90,110,200,0)", opacity: 0.55, speed: [0.12, 0.35] }
          : { n: 50, opacity: 0.6, speed: [0.15, 0.45] }));
        if (cool) st.tint.copy(COOL); else st.tint.copy(WARM);
      }, {
        cam: (t, st) => { const k = lin(t, st.a, st.b), d = i % 2 ? 1 : -1; return { pos: [d * lerp(-0.35, 0.35, k), 3.6, lerp(24, 23.1, k)], look: [d * lerp(-0.35, 0.35, k), LOOK_Y, 0] }; },
        fadeOut: nx ? 0.45 : 0.01,
      });
      set.update = t => { actors.forEach((ac, k) => moveActor(ac, t, a, b, k)); propActs.forEach((ac, k) => moveProp(ac, t, a, k)); };
      // 코드 화면
      if (s.screen && SCREEN[s.screen.type]) {
        const sc = K.scene(a, b, nx ? null : { keep: true });
        const t0 = s.screen.at ? at(s.screen.at[0], s.screen.at[1]) : (i === 0 ? 0.3 : S(s.a) + 0.35);
        const done = SCREEN[s.screen.type](sc, s.screen, t0, b, { prop: pr.length > 0 });
        if (s.screen.title && s.screen.type !== "BIG") {             // v1.7 화면 위 이름표 탭 (KOSPI · S&P 500 · RULE 1 …)
          const tab = el(`<div class="ktab w9 nw" style="${V ? `left:${lastP.cx}px;transform:translateX(-50%)` : `left:${lastP.cx - lastP.w / 2}px`};top:${lastP.top - 82}px">${esc(s.screen.title)}</div>`, sc);
          pop(tab, t0 + 0.1, { from: { y: 10 } });
        }
        K.cut(Math.min(b - 0.2, Math.max(done + 0.2, (a + b) / 2)), `${i + 1} ${s.screen.type}`);
      } else K.cut(Math.min(b - 0.2, (a + b) / 2 + 0.3), `${i + 1} ${pr.length ? "소품" : "무대"}`);
      lastEnd = b;
    });

    // K7 화 배지 (왼쪽 위) · 끝에 다음 화
    if (ep) {
      const bd = el(`<div class="kep w9 nw" style="${V ? "left:60px;top:170px" : "left:56px;top:44px"}">#${esc(ep)}</div>`);   // v1.3 '#N' (영어 'EP' 없음)
      tl.fromTo(bd, { opacity: 0 }, { opacity: 1, duration: 0.4 }, 0.2);
      if (!V && SPEC.next) {
        const nb = el(`<div class="kep next w9 nw" style="right:56px;bottom:90px">#${esc(SPEC.next)} ▶</div>`);
        pop(nb, Math.max(0, K.D - 4.5));
      }
    }
    if (SPEC.cover && window.EP.thumb !== undefined) K.cover(E(1) + 0.1);
    K.done();
    window.STORY = { version: S_.VERSION, scenes: scenes.length, end: lastEnd };
  };
})();
