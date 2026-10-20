// VERSION: v1.1 — 2026-10-20 — 4개 묶음 그림에서 물건끼리 닿아 빈 열로 넷이 안 나오면, 가장 넓은 덩어리를 세로로 가장 적게 걸친 열에서 자름
//   (예전: 4등분 — 사람이 잘렸음. ChatGPT 2판 P-PEOPLE·P-ICONS·P-ICONS2 가 닿아 있었음). 나눈 자리는 window.PUPPET[키].segs.
//   · 프레임마다 인형을 처음 자리·크기·기울기·보임으로 되돌린 뒤 움직임을 적용 (Actor.reset) — 렌더 check 가 시각을 앞뒤로 건너뛸 때
//     무대 밖으로 빠져나간(exit) 인형이 그 시각 전으로 돌아가도 밖에 남던 문제 (그림 = 시각 t 만의 함수). exit 는 이제 옆으로 더함.
// (v1.0) — 2026-10-20 — 종이인형극 무대 (Three.js 0.160 + kit.js K.onSeek) — 사용자 지시 2026-10-20 "좋아 저런 방식으로 가자 ... 이제 나머지 부분
//   영상으로 만들자" (test 일본 축제 롱폼·쇼츠). 시험판 video/episodes/ilbon-chukje-2026-10/test_puppet.html v0.2 의 방식을 장면 파일 여러 개가 같이 쓰게 옮김:
//   · 그림 = 배경 1장 + 물건마다 투명 그림 1장 (상태 그림 없음) — 움직임(걸음·들썩·기울기·떨어짐·튀어나옴·뒤집기·흔들림)은 모두 코드.
//   · 4개를 한 줄로 그린 그림(row4)은 투명한 빈 열로 넷을 찾아 자름 (못 찾으면 4등분).
//   · 투명이 아니고 순초록 바탕이면 초록을 뺌 · 그림이 아직 없으면 같은 자리에 임시 그림(회색 + 이름) — 움직임·배치만 미리 점검.
//   · 장면(set) = [a, b] 동안 보이는 배경·인형 묶음, 앞뒤 장면과 0.45초 겹쳐 바뀜(겹친 동안 더 보이는 장면의 카메라).
//   · 3D 는 단순한 것만: 겹 무대 깊이(배경 -24 · 인형 0 · 앞 인형 +) 시차, 불씨·빛 알갱이, 종이 그림자, 상자(계단).
//   모든 움직임은 시각 t 의 함수 — 렌더(SB.seek)가 아무 시각이나 찍어도 같은 그림.
//   연구·교육용 영상 도구.
(function () {
  "use strict";
  const PP = (window.Puppet = {});
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const sm = x => (x <= 0 ? 0 : x >= 1 ? 1 : x * x * (3 - 2 * x));
  const seg = (t, a, b) => sm((t - a) / (b - a));
  const lin = (t, a, b) => clamp((t - a) / (b - a), 0, 1);
  const lerp = (a, b, k) => a + (b - a) * k;
  const rnd = (i, k) => { const x = Math.sin(i * 12.9898 + k * 78.233) * 43758.5453; return x - Math.floor(x); };
  const q12 = t => Math.floor(t * 12) / 12;                         // 인형 흔들림은 초당 12장 (종이인형 느낌)
  const back = x => { const c = 1.9; x = clamp(x, 0, 1); return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };   // 튀어나옴 (살짝 넘침)
  const outC = x => 1 - Math.pow(1 - clamp(x, 0, 1), 3);
  PP.u = { clamp, sm, seg, lin, lerp, rnd, q12, back, outC };

  // ---------- 그림 준비 ----------
  function placeholder(key, kind, label) {
    const w = 1536, h = kind === "sq" ? 1536 : 1024, c = document.createElement("canvas"); c.width = w; c.height = h;
    const g = c.getContext("2d");
    g.font = "bold 64px sans-serif"; g.textAlign = "center"; g.textBaseline = "middle";
    if (kind === "bg") {
      const s = g.createLinearGradient(0, 0, 0, h); s.addColorStop(0, "#26314F"); s.addColorStop(0.62, "#5A4A5C"); s.addColorStop(0.7, "#8C7E6C"); s.addColorStop(1, "#6F6556");
      g.fillStyle = s; g.fillRect(0, 0, w, h); g.fillStyle = "rgba(255,255,255,.35)"; g.fillText(`${label} (임시)`, w / 2, h * 0.35);
      return c;
    }
    const n = kind === "row4" ? 4 : 1;
    for (let i = 0; i < n; i++) {
      const cx = (i + 0.5) / n * w, bw = (n === 1 ? 0.6 : 0.17) * w, bh = 0.55 * h;
      g.fillStyle = "#F2E6CF"; g.beginPath(); g.roundRect(cx - bw / 2 - 6, h * 0.88 - bh - 6, bw + 12, bh + 12, 40); g.fill();
      g.fillStyle = "#7B7F8C"; g.beginPath(); g.roundRect(cx - bw / 2, h * 0.88 - bh, bw, bh, 34); g.fill();
      g.fillStyle = "#fff"; g.fillText(n === 1 ? label : `${label}·${i + 1}`, cx, h * 0.88 - bh / 2);
    }
    return c;
  }
  function rowSegments(A, w, h, n) {                                  // 한 줄 n 개 — 투명한 빈 열로 나눔
    const cnt = new Uint16Array(w);                                   // 열마다 그림이 걸친 줄 수 (3줄 걸러)
    for (let x = 0; x < w; x++) for (let y = 0; y < h; y += 3) if (A(x, y) > 40) cnt[x]++;
    let segs = [], s0 = -1;
    for (let x = 0; x <= w; x++) { const o = x < w && cnt[x] > 0; if (o && s0 < 0) s0 = x; if (!o && s0 >= 0) { segs.push([s0, x]); s0 = -1; } }
    segs = segs.filter(([a, b]) => b - a > w * 0.01);                // 부스러기 버림
    while (segs.length > n) {                                         // 가장 가까운 둘을 합침
      let k = 0, best = 1e9;
      for (let i = 0; i < segs.length - 1; i++) { const gap = segs[i + 1][0] - segs[i][1]; if (gap < best) { best = gap; k = i; } }
      segs.splice(k, 2, [segs[k][0], segs[k + 1][1]]);
    }
    const ok = segs.length === n;
    while (segs.length > 0 && segs.length < n) {                      // v1.1 물건끼리 닿음 → 가장 넓은 덩어리를 가장 적게 걸친 열에서 자름 (가장자리 15% 는 빼고)
      let k = 0;
      for (let i = 1; i < segs.length; i++) if (segs[i][1] - segs[i][0] > segs[k][1] - segs[k][0]) k = i;
      const [a, b] = segs[k], m = Math.floor((b - a) * 0.15);
      let cut = a + m, best = 1e9;
      for (let x = a + m; x < b - m; x++) { const sc = cnt[x] * 10000 + Math.abs(x - (a + b) / 2); if (sc < best) { best = sc; cut = x; } }
      segs.splice(k, 1, [a, cut], [cut, b]);
    }
    if (segs.length !== n) segs = Array.from({ length: n }, (_, i) => [Math.round(i * w / n), Math.round((i + 1) * w / n)]);
    return { ok, segs: segs.map(([a, b]) => {
      let y0 = h, y1 = -1;
      for (let y = 0; y < h; y += 2) for (let x = a; x < b; x += 2) if (A(x, y) > 40) { if (y < y0) y0 = y; if (y > y1) y1 = y; break; }
      return y1 < 0 ? [a / w, 0, b / w, 1] : [a / w, y0 / h, b / w, (y1 + 2) / h];
    }) };
  }
  function prep(img, spec) {                                          // → {c 캔버스, info}
    const ok = img.complete && img.naturalWidth > 0;
    let c;
    if (ok) { c = document.createElement("canvas"); c.width = img.naturalWidth; c.height = img.naturalHeight; c.getContext("2d").drawImage(img, 0, 0); }
    else c = placeholder(spec.key, spec.kind, spec.label || spec.key);
    const w = c.width, h = c.height, info = { key: spec.key, file: spec.f, src: ok ? "file" : "임시", w, h, bbox: [0, 0, 1, 1], keyed: false, opaque: false };
    if (spec.kind === "bg") return { c, info };
    const g = c.getContext("2d", { willReadFrequently: true }), d = g.getImageData(0, 0, w, h), p = d.data;
    const A = (x, y) => p[(y * w + x) * 4 + 3], at = (x, y) => (y * w + x) * 4;
    const corners = [at(2, 2), at(w - 3, 2), at(2, h - 3), at(w - 3, h - 3)];
    if (corners.every(i => p[i + 3] > 250)) {
      if (corners.every(i => p[i + 1] > 150 && p[i] < 110 && p[i + 2] < 110)) {   // 순초록 바탕 → 초록 빼기 + 번짐 줄이기
        for (let i = 0; i < p.length; i += 4) {
          const m = Math.max(p[i], p[i + 2]), gd = p[i + 1] - m, k = clamp((gd - 40) / 50, 0, 1) * clamp((p[i + 1] - 110) / 60, 0, 1);
          if (k > 0) p[i + 3] = Math.round(p[i + 3] * (1 - k));
          if (gd > 12 && p[i + 1] > 110) p[i + 1] = m + 12;
        }
        g.putImageData(d, 0, 0); info.keyed = true;
      } else { info.opaque = true; console.warn(`[PUPPET] ${spec.f} 투명이 아님 — ChatGPT 에 투명 PNG(또는 순초록 바탕)로 다시 요청`); }
    }
    let x0 = w, y0 = h, x1 = -1, y1 = -1;
    for (let y = 0; y < h; y += 2) for (let x = 0; x < w; x += 2) if (A(x, y) > 40) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
    if (x1 > 0) info.bbox = [x0 / w, y0 / h, (x1 + 2) / w, (y1 + 2) / h];
    if (spec.kind === "row4") { const r = rowSegments(A, w, h, 4); info.segs = r.segs; info.splitOk = r.ok; if (!r.ok && ok) console.info(`[PUPPET] ${spec.f} 물건끼리 닿음 — 가장 적게 걸친 열에서 자름`); }
    info.A = A;
    return { c, info };
  }

  // ---------- 무대 ----------
  // opt: {dir, files: {KEY: {f, kind: "bg"|"cut"|"row4"|"sq", label}}, w, h, left, top, fov, clear}
  PP.stage = function (opt) {
    const W = opt.w || 1920, H = opt.h || 1080, stageEl = document.getElementById("stage");
    const box = K.el(`<div style="position:absolute;width:1px;height:1px;overflow:hidden;opacity:0;pointer-events:none"></div>`);
    const IMG = {}, SPEC = {};
    for (const k in opt.files) { SPEC[k] = Object.assign({ key: k, kind: "cut" }, opt.files[k]); IMG[k] = K.el(`<img alt="" src="${opt.dir}${SPEC[k].f}">`, box); }
    const canvas = K.el(`<canvas width="${W}" height="${H}" style="position:absolute;left:${opt.left || 0}px;top:${opt.top || 0}px;width:${W}px;height:${H}px"></canvas>`);
    stageEl.insertBefore(canvas, stageEl.firstChild);
    const ren = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true });
    ren.setPixelRatio(1); ren.setSize(W, H, false); ren.setClearColor(opt.clear == null ? 0x0B0F1E : opt.clear, 1);
    const scene = new THREE.Scene(), cam = new THREE.PerspectiveCamera(opt.fov || 30, W / H, 0.1, 400);
    const S = { W, H, scene, cam, ren, IMG, SPEC, sets: [], tex: {}, info: {}, afters: [] };
    S.ready = () => Object.values(IMG).every(i => i.complete);        // 실패한 그림도 complete (→ 임시 그림)
    S.get = key => {
      if (!S.tex[key]) {
        if (!SPEC[key]) throw new Error(`그림 키 없음: ${key}`);
        const r = prep(IMG[key], SPEC[key]), t = new THREE.CanvasTexture(r.c);
        t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4;
        S.tex[key] = t; S.info[key] = r.info;
      }
      return { tex: S.tex[key], info: S.info[key] };
    };
    S.project = v => { const p = v.clone().project(cam); return [(p.x + 1) / 2 * W, (1 - p.y) / 2 * H, p.z]; };
    S.after = fn => S.afters.push(fn);                               // 렌더 뒤 (DOM 이름표 자리 등)
    window.PUPPET = S.info;                                          // 점검용: 어떤 그림을 썼는지(임시?)·초록 뺌·나눔
    S.set = (a, b, build, o) => {
      const st = new PSet(S, a, b, build, o || {});
      S.sets.push(st);
      return st;
    };
    S.defaultCam = (st, t) => {                                      // 천천히 오른쪽으로 · 살짝 다가감
      const k = lin(t, st.a, st.b);
      return { pos: [lerp(-0.6, 0.6, k), 3.6, lerp(24, 22.8, k)], look: [lerp(-0.6, 0.6, k), 3.34, 0] };
    };
    const tmpC = new THREE.Color();
    K.onSeek(t => {
      if (!S.ready()) return;
      let top = null;
      for (const st of S.sets) {
        const f = st.fadeAt(t);
        if (f <= 0) { if (st.built) st.root.visible = false; continue; }
        if (!st.built) st.doBuild();
        st.root.visible = true; st.fade = f;
        for (const a of st.actors) if (a.reset) a.reset();          // v1.1 매 프레임 처음 상태에서
        if (st.update) st.update(t, st);
        for (const ps of st.parts) ps.step(t);
        for (const a of st.actors) a.apply(f, st.tint, tmpC);
        if (!top || f > top.fade || (f === top.fade && st.a > top.a)) top = st;
      }
      const c = top ? (top.cam ? top.cam(t, top) : S.defaultCam(top, t)) : { pos: [0, 3.6, 24], look: [0, 3.34, 0] };
      const pos = new THREE.Vector3(...c.pos);
      if (top && top.shakes.length) for (const [ti, amp] of top.shakes) if (t > ti) { const d = t - ti, s = amp * Math.exp(-d / 0.22); pos.y += s * Math.sin(d * 38); pos.x += s * 0.6 * Math.sin(d * 27 + 1); }
      cam.position.copy(pos); cam.lookAt(new THREE.Vector3(...c.look)); cam.updateMatrixWorld();
      ren.render(scene, cam);
      for (const fn of S.afters) fn(t);
    });
    return S;
  };

  // ---------- 장면 (배경 + 인형 묶음) ----------
  class PSet {
    constructor(S, a, b, build, o) {
      Object.assign(this, { S, a, b, buildFn: build, fi: o.fadeIn == null ? 0.45 : o.fadeIn, fo: o.fadeOut == null ? 0.45 : o.fadeOut,
        root: new THREE.Group(), actors: [], parts: [], built: false, fade: 0, cam: o.cam || null, update: null,
        tint: new THREE.Color(0xffffff), shakes: [] });
      S.scene.add(this.root); this.root.visible = false;
    }
    fadeAt(t) {                                                      // 앞뒤 장면과 겹쳐 바뀜 (첫 장면은 0초부터 바로)
      if (t < this.a - this.fi || t > this.b + this.fo) return 0;
      const i = this.a <= 0.01 ? 1 : seg(t, this.a - this.fi, this.a + 0.02), o = 1 - seg(t, this.b, this.b + this.fo);
      return Math.min(i, o);
    }
    doBuild() { this.built = true; this.buildFn(this); }
    // 배경: 그림 세로 v 줄(바닥이 시작하는 줄 등)이 월드 높이 y 에 오게, z 깊이, 가로 w
    bg(key, o) {
      o = Object.assign({ z: -24, w: 54, v: 0.62, y: 1.28 }, o);
      const { tex, info } = this.S.get(key), ht = o.w * info.h / info.w;
      const a = new Actor(this, tex, [0, 0, 1, 1], o.w, ht, [0.5, 0.5], { shadow: false });
      a.g.position.set(o.x || 0, o.y + (o.v - 0.5) * ht, o.z); a.ro(0);
      return a;
    }
    // 인형: key(+seg 번째 — row4) · h 월드 높이(알파 상자 기준) · at [x, y, z] 기준점(기본 아래 가운데) 자리
    actor(key, o) {
      o = Object.assign({ h: 4, at: [0, 0, 0], anchor: [0.5, 1], shadow: true }, o);
      const { tex, info } = this.S.get(key);
      const crop = o.crop || (o.seg != null ? info.segs[o.seg] : info.bbox);
      const pw = (crop[2] - crop[0]) * info.w, ph = (crop[3] - crop[1]) * info.h, ht = o.h, wd = o.w || ht * pw / ph;
      const a = new Actor(this, tex, crop, wd, o.w ? o.w * ph / pw : ht, o.anchor, o);
      a.g.position.set(...o.at); a.home = a.g.position.clone();
      if (o.flip) a.m.scale.x = -1;
      a.ro(o.ro == null ? 3 : o.ro);
      return a;
    }
    add(obj, ro) { this.root.add(obj); if (ro != null) obj.renderOrder = ro; return obj; }
    shake(t, amp) { this.shakes.push([t, amp]); }
    part(p) { p.set = this; this.parts.push(p); this.root.add(p.obj); return p; }
  }
  PP.PSet = PSet;

  // 인형 하나 = 기준점에 놓인 묶음(g) 안의 그림(m) + 종이 그림자
  class Actor {
    constructor(st, tex, crop, wd, ht, anchor, o) {
      const [u0, v0, u1, v1] = crop;
      const geo = new THREE.PlaneGeometry(wd, ht), uv = geo.attributes.uv;
      for (let i = 0; i < uv.count; i++) uv.setXY(i, u0 + uv.getX(i) * (u1 - u0), (1 - v1) + uv.getY(i) * (v1 - v0));
      this.mat = new THREE.MeshBasicMaterial({ map: tex, transparent: true, depthWrite: false });
      this.m = new THREE.Mesh(geo, this.mat);
      this.m.position.set((0.5 - anchor[0]) * wd, (anchor[1] - 0.5) * ht, 0);
      this.g = new THREE.Group(); this.g.add(this.m);
      if (o.shadow) {
        this.smat = new THREE.MeshBasicMaterial({ map: tex, color: 0x000000, transparent: true, depthWrite: false });
        const s = new THREE.Mesh(geo, this.smat); s.position.set(0.11 * Math.max(1, ht / 4), -0.09 * Math.max(1, ht / 4), -0.1); s.renderOrder = -1; this.m.add(s);
      }
      this.op = 1; this.tint = new THREE.Color(o.tint == null ? 0xffffff : o.tint); this.wd = wd; this.ht = ht; this.anchor = anchor;
      st.root.add(this.g); st.actors.push(this);
    }
    ro(n) { this.m.renderOrder = n; return this; }
    reset() { if (this.home) this.g.position.copy(this.home); this.g.rotation.set(0, 0, 0); this.g.scale.set(1, 1, 1); this.op = 1; }
    top(dy) {                                                        // 그림 위 가운데의 월드 자리 (+dy) — DOM 이름표를 붙일 때
      this.g.updateMatrixWorld(true);
      const v = this.g.localToWorld(new THREE.Vector3((0.5 - this.anchor[0]) * this.wd, this.anchor[1] * this.ht, 0));
      v.y += dy == null ? 0.3 : dy; return v;
    }
    apply(fade, setTint, tmp) {
      const o = clamp(this.op, 0, 1) * fade;
      this.g.visible = o > 0.002;
      this.mat.opacity = o; tmp.copy(this.tint).multiply(setTint); this.mat.color.copy(tmp);
      if (this.smat) this.smat.opacity = 0.32 * o;
    }
    // 자주 쓰는 움직임 (모두 t 의 함수 — 매 프레임 부름)
    pop(t, at, d) {                                                  // 튀어나옴: 크기 0 → 1 (살짝 넘침) · 그 전엔 안 보임
      const k = (t - at) / (d || 0.45);
      this.op = k <= 0 ? 0 : 1; const s = k <= 0 ? 0.001 : back(k);
      this.g.scale.set(s, s, 1); return this;
    }
    rise(t, at, d, dy) {                                             // 아래에서 솟아오름 (무대 밑에서 올라오는 인형)
      const k = outC((t - at) / (d || 0.5));
      this.op = t < at ? 0 : 1; this.g.position.y = this.home.y - (dy == null ? 3 : dy) * (1 - k); return this;
    }
    slide(t, at, d, dx) {                                            // 옆에서 밀려 들어옴
      const k = outC((t - at) / (d || 0.7));
      this.op = t < at ? 0 : 1; this.g.position.x = this.home.x + dx * (1 - k); return this;
    }
    exit(t, at, d, dx) {                                             // 옆으로 빠져나감 (점점 빠르게)
      const k = clamp((t - at) / (d || 0.8), 0, 1);
      if (t >= at) this.g.position.x += dx * k * k; if (k >= 1) this.op = 0; return this;
    }
    flip(t, at, d) {                                                 // 종이 카드 뒤집듯 가로 폭 0 → 1
      const k = clamp((t - at) / (d || 0.35), 0, 1);
      this.op = t < at ? 0 : 1; this.g.scale.x = Math.max(0.02, Math.sin(k * Math.PI / 2)); return this;
    }
    hide(t, at, d) { if (t >= at) this.op *= 1 - seg(t, at, at + (d || 0.35)); return this; }
    bob(t, amp, hz, ph) {                                            // 걸음·들썩 (12장/초)
      const tq = q12(t); this.g.position.y = this.home.y + (amp || 0.08) * Math.abs(Math.sin(tq * Math.PI * (hz || 2) + (ph || 0))); return this;
    }
    sway(t, amp, hz, ph) { const tq = q12(t); this.g.rotation.z = (amp || 0.02) * Math.sin(tq * Math.PI * 2 * (hz || 0.8) + (ph || 0)); return this; }
    jitter(t, amp) { const tq = q12(t); this.g.rotation.z = (amp || 0.02) * Math.sin(tq * 41) ; this.g.position.x = this.home.x + (amp || 0.02) * 2 * Math.sin(tq * 53); return this; }
  }
  PP.Actor = Actor;

  // ---------- 점 (불씨·빛·먼지) ----------
  function glowTex(inner, outer) {
    const c = document.createElement("canvas"); c.width = c.height = 64; const g = c.getContext("2d"), r = g.createRadialGradient(32, 32, 0, 32, 32, 32);
    r.addColorStop(0, inner); r.addColorStop(1, outer); g.fillStyle = r; g.fillRect(0, 0, 64, 64); return new THREE.CanvasTexture(c);
  }
  // 떠오르는 점: o = {n, x:[a,b], z:[a,b], hgt, speed, size, inner, outer, opacity}
  PP.floaters = function (o) {
    o = Object.assign({ n: 100, x: [-12, 14], z: [-14, 5], hgt: 10, speed: [0.25, 0.85], size: 0.22, inner: "rgba(255,214,150,1)", outer: "rgba(255,120,40,0)", opacity: 0.9 }, o);
    const geo = new THREE.BufferGeometry(), pos = new Float32Array(o.n * 3);
    geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    const mat = new THREE.PointsMaterial({ map: glowTex(o.inner, o.outer), size: o.size, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, opacity: o.opacity });
    const obj = new THREE.Points(geo, mat); obj.renderOrder = 5;
    const p = { obj, mat, op: 1, step(t) {
      for (let i = 0; i < o.n; i++) {
        const sp = lerp(o.speed[0], o.speed[1], rnd(i, 4)), y = (rnd(i, 2) * o.hgt + t * sp) % o.hgt;
        pos[i * 3] = lerp(o.x[0], o.x[1], rnd(i, 1)) + Math.sin(t * 0.7 + rnd(i, 5) * 6.3) * 0.4; pos[i * 3 + 1] = y; pos[i * 3 + 2] = lerp(o.z[0], o.z[1], rnd(i, 3));
      }
      geo.attributes.position.needsUpdate = true; mat.opacity = o.opacity * p.op * (p.set ? p.set.fade : 1);
    } };
    return p;
  };

  // 종이 조각 (흙먼지 덩어리·돌) — 코드로 그림, 크림색 테두리
  function paperBlob(fill, edge, seed, n, cloud) {
    const c = document.createElement("canvas"); c.width = c.height = n; const g = c.getContext("2d");
    const lobes = 5 + (seed % 3), ph = rnd(seed, 3) * 6.28, N = cloud ? 60 : 7;
    const path = r => { g.beginPath(); for (let i = 0; i <= N; i++) { const a = i / N * 6.2832, rr = cloud ? r * (0.88 + 0.12 * Math.abs(Math.cos(lobes * a / 2 + ph))) : r * (0.7 + 0.3 * rnd(seed * 31 + (i % N), 7)); g.lineTo(n / 2 + Math.cos(a) * rr, n / 2 + Math.sin(a) * rr); } g.closePath(); g.fill(); };
    g.fillStyle = "#F2E6CF"; path(n * 0.48); g.fillStyle = fill; path(n * 0.43);
    g.fillStyle = edge; g.save(); g.translate(-n * 0.07, -n * 0.07); g.scale(0.62, 0.62); g.translate(n * 0.33, n * 0.33); path(n * 0.4); g.restore();
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
  }
  let PUFF = null, ROCK = null;
  // 흙먼지: 시각 at 에 world 자리 xyz(함수 가능)에서 터짐 · o = {n, spread, rocks}
  PP.dust = function (at, where, o) {
    o = Object.assign({ n: 26, spread: 4.0, rocks: 16, rise: 1.3 }, o);
    PUFF = PUFF || [0, 1, 2].map(i => paperBlob(["#CDB78E", "#C1AA82", "#D9C59E"][i], ["#E0CDA8", "#D5C19C", "#EBDBB9"][i], i + 1, 128, true));
    ROCK = ROCK || [0, 1].map(i => paperBlob(["#5B5148", "#7A6E62"][i], ["#857A6D", "#9C9182"][i], i + 9, 64, false));
    const obj = new THREE.Group(), puffs = [], rocks = [];
    for (let i = 0; i < o.n; i++) { const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: PUFF[i % 3], transparent: true, depthWrite: false })); s.renderOrder = 4; obj.add(s); puffs.push(s); }
    for (let i = 0; i < o.rocks; i++) { const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: ROCK[i % 2], transparent: true, depthWrite: false })); s.renderOrder = 4; obj.add(s); rocks.push(s); }
    const p = { obj, step(t) {
      const tau = t - at, c = typeof where === "function" ? where(t) : where, f = p.set ? p.set.fade : 1;
      for (let i = 0; i < puffs.length; i++) {
        const s = puffs[i], on = tau > 0 && tau < 3.4; s.visible = on; if (!on) continue;
        const k = 1 - Math.exp(-tau / (0.35 + 0.25 * rnd(i, 1))), dir = rnd(i, 2) * 2 - 1;
        s.position.set(c[0] + dir * (0.6 + o.spread * k * rnd(i, 3)), c[1] + 0.2 + o.rise * k * rnd(i, 4) + 0.2 * tau, c[2] + 0.6 + 1.2 * rnd(i, 5));
        const sz = (0.8 + 1.2 * rnd(i, 6)) * (0.45 + 0.9 * k); s.scale.set(sz, sz * 0.85, 1); s.material.rotation = dir * k * 0.6;
        s.material.opacity = f * 0.92 * sm(clamp(tau / 0.08, 0, 1)) * (1 - seg(tau, 0.9 + 0.7 * rnd(i, 7), 2.8));
        if (p.set) s.material.color.copy(p.set.tint);
      }
      for (let i = 0; i < rocks.length; i++) {
        const s = rocks[i], on = tau > 0 && tau < 1.4; s.visible = on; if (!on) continue;
        const vx = (rnd(i, 11) * 2 - 1) * 5.5, vy = 3 + 3 * rnd(i, 12);
        s.position.set(c[0] + vx * tau, Math.max(c[1] + 0.1, c[1] + 0.4 + vy * tau - 9 * tau * tau), c[2] + 1.2 + rnd(i, 13));
        const sz = 0.22 + 0.25 * rnd(i, 14); s.scale.set(sz, sz, 1); s.material.rotation = tau * 9 * (rnd(i, 15) - 0.5);
        s.material.opacity = f * (1 - seg(tau, 0.9, 1.4));
      }
    } };
    return p;
  };

  // 종이 상자 (계단·단상) — 앞면·윗면·옆면 색을 달리해 빛 없이도 입체로
  PP.box = function (w, h, d, col) {
    const c = new THREE.Color(col || 0xC9A46A), mk = k => new THREE.MeshBasicMaterial({ color: c.clone().multiplyScalar(k), transparent: true });
    const mats = [mk(0.72), mk(0.72), mk(1.12), mk(0.6), mk(1.0), mk(0.8)];   // +x −x +y −y +z −z
    const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mats);
    m.userData.mats = mats; return m;
  };
  // 캔버스로 그린 평면 (지도 등) — draw(g, w, h)
  PP.canvasPlane = function (cw, ch, wd, ht, draw) {
    const c = document.createElement("canvas"); c.width = cw; c.height = ch; draw(c.getContext("2d"), cw, ch);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4;
    const mat = new THREE.MeshBasicMaterial({ map: t, transparent: true, depthWrite: false });
    return new THREE.Mesh(new THREE.PlaneGeometry(wd, ht), mat);
  };
})();
