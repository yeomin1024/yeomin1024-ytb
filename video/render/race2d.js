// VERSION: v1.0 — 2026-10-16 — 최초 (같은 날 고침: pin(…, bounds) 칩 가로 범위 · $0 눈금 글자는 zeroLabel 일 때만 — 연도 글자와 겹침). 주식 2·3·4번 공통 '날짜가 흐르며 계좌 여럿을 실시간으로 견주는' 2D 캔버스 그래프 (사용자 지시 2026-10-15
//   "날짜가 지남에 따라 백테스트 수치를 실시간 비교하는 과정을 애니메이션으로 표현하면 좋겠지" · 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상
//   미리보기 영상 만들어봐"). kit.js 의 K.onSeek(t) 에서 그리면 렌더기(render.mjs)가 프레임마다 그대로 찍는다 (시각 t 만으로 그림 — 재현).
//   화면 글자는 숫자·$·연도·기호만 (stock/guides/README.md 4번). 숫자는 장면이 넘겨준 자료(anim.js ← run.py)만 그린다. 연구·교육용 — 투자 권유 아님.
// 사용:
//   const ch = new R2.Chart({x, y, w, h, n: 날 수, years: ["2014-..."], series: [{vals, color, width}], mode: "lin"|"log", min, max, baselines: [{v, color, dash}]})
//   ch.draw(ctx, d)            // d = 날(소수) — 0..n-1. 선은 d 까지만 (미래 값을 그리지 않음)
//   const pace = R2.warp([[t0, d0], [t1, d1], …], "이름")   // 시각 → 날 (기준점 사이 같은 속도) · pace.tOf(d) 날 → 시각 · [PACE] 로그
(function (G) {
  "use strict";
  const FONT = '"Noto Sans KR", sans-serif';
  const fmtMoney = v => {
    const a = Math.abs(v);
    if (a >= 1e6) return "$" + (v / 1e6).toFixed(a >= 1e7 ? 0 : 1).replace(/\.0$/, "") + "M";
    if (a >= 1e3) return "$" + Math.round(v / 1e3).toLocaleString("en-US") + "K";
    return "$" + Math.round(v).toLocaleString("en-US");
  };
  function nice(step) {
    const p = Math.pow(10, Math.floor(Math.log10(step))), m = step / p;
    return (m <= 1 ? 1 : m <= 2 ? 2 : m <= 2.5 ? 2.5 : m <= 5 ? 5 : 10) * p;
  }
  function cummax(a) { const o = new Float64Array(a.length); let m = -Infinity; for (let i = 0; i < a.length; i++) { if (a[i] > m) m = a[i]; o[i] = m; } return o; }

  function Chart(o) {
    Object.assign(this, { mode: "lin", min: 0, max: null, maxMin: 0, pad: 1.12, grid: true, money: fmtMoney, yLabelX: null, xFrom: 0, xTo: null, baselines: [], labelSize: 32 }, o);
    this.xTo = this.xTo == null ? this.n - 1 : this.xTo;
    this.cm = this.series.map(s => cummax(s.vals));
  }
  Chart.prototype.X = function (i) { return this.x + (i - this.xFrom) / Math.max(1, this.xTo - this.xFrom) * this.w; };
  Chart.prototype.range = function (d) {
    if (this.mode === "log") return [this.min, this.max];
    if (this.max != null) return [this.min, this.max];
    const k = Math.max(0, Math.min(this.n - 1, Math.floor(d)));
    let m = this.maxMin;
    for (let j = 0; j < this.series.length; j++) if (!this.series[j].noScale) m = Math.max(m, this.cm[j][k]);
    return [this.min, m * this.pad];
  };
  Chart.prototype.Yf = function (d) {
    const [lo, hi] = this.range(d), y = this.y, h = this.h;
    if (this.mode === "log") { const a = Math.log10(lo), b = Math.log10(hi); return v => y + h - (Math.log10(Math.max(v, lo * 0.5)) - a) / (b - a) * h; }
    return v => y + h - (v - lo) / (hi - lo) * h;
  };
  Chart.prototype.at = function (s, d) {               // 소수 날의 값 (앞뒤 날 사이 직선)
    const v = this.series[s].vals, i = Math.floor(d), u = d - i;
    if (i >= v.length - 1) return v[v.length - 1];
    return v[i] + (v[i + 1] - v[i]) * u;
  };
  Chart.prototype.draw = function (ctx, d, opt) {
    opt = opt || {};
    d = Math.max(this.xFrom, Math.min(this.xTo, d));
    const Y = (this.Y = this.Yf(d)), [lo, hi] = this.range(d), L = this.labelSize;
    ctx.save();
    // 눈금
    if (this.grid) {
      ctx.font = `700 ${L}px ${FONT}`; ctx.textBaseline = "middle"; ctx.textAlign = "right";
      const ticks = [];
      if (this.mode === "log") { for (let p = Math.ceil(Math.log10(lo)); p <= Math.floor(Math.log10(hi)); p++) ticks.push(Math.pow(10, p)); }
      else { const st = nice((hi - lo) / 4.5); for (let v = Math.ceil(lo / st) * st; v <= hi + 1e-9; v += st) ticks.push(v); }
      for (const v of ticks) {
        const yy = Y(v);
        ctx.strokeStyle = "rgba(160,176,204,.13)"; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(this.x, yy); ctx.lineTo(this.x + this.w, yy); ctx.stroke();
        if (v !== 0 || this.zeroLabel) { ctx.fillStyle = "#7F8BA3"; ctx.fillText(this.money(v), (this.yLabelX == null ? this.x - 14 : this.yLabelX), yy); }
      }
      // 연도 (1월 첫 거래일)
      ctx.textAlign = "center"; ctx.textBaseline = "top"; ctx.fillStyle = "#7F8BA3";
      const ys = this.years || [];
      let lastX = -1e9;
      for (const [i, lab] of ys) {
        if (i < this.xFrom || i > this.xTo) continue;
        const xx = this.X(i);
        ctx.strokeStyle = "rgba(160,176,204,.10)"; ctx.beginPath(); ctx.moveTo(xx, this.y); ctx.lineTo(xx, this.y + this.h); ctx.stroke();
        if (xx - lastX > (this.yearGap || 110)) { ctx.fillText(lab, xx, this.y + this.h + 14); lastX = xx; }
      }
    }
    // 기준선 (노란 점선 = 기준)
    for (const b of this.baselines) {
      const bv = typeof b.v === "function" ? null : b.v;
      ctx.setLineDash(b.dash || [18, 12]); ctx.lineWidth = b.width || 4; ctx.strokeStyle = b.color || "#FFD400";
      ctx.beginPath();
      if (bv != null) { const yy = Y(bv); ctx.moveTo(this.x, yy); ctx.lineTo(this.x + this.w, yy); }
      else {                                            // 날마다 다른 기준 (예: 넣은 돈 누적) — d 까지만
        const k = Math.floor(d);
        for (let i = this.xFrom; i <= k; i += Math.max(1, b.step || 1)) { const xx = this.X(i), yy = Y(b.v(i)); i === this.xFrom ? ctx.moveTo(xx, yy) : ctx.lineTo(xx, yy); }
        ctx.lineTo(this.X(d), Y(b.v(Math.min(this.n - 1, Math.ceil(d)))));
      }
      ctx.stroke(); ctx.setLineDash([]);
    }
    // 선 (d 까지만)
    const heads = [];
    this.series.forEach((s, j) => {
      if (s.hidden) return;
      const k = Math.floor(d), v = s.vals;
      ctx.lineJoin = "round"; ctx.lineCap = "round";
      if (s.fill) {
        ctx.beginPath(); ctx.moveTo(this.X(this.xFrom), Y(lo));
        for (let i = this.xFrom; i <= k; i++) ctx.lineTo(this.X(i), Y(v[i]));
        ctx.lineTo(this.X(d), Y(this.at(j, d))); ctx.lineTo(this.X(d), Y(lo)); ctx.closePath();
        ctx.fillStyle = s.fill; ctx.fill();
      }
      ctx.beginPath();
      for (let i = this.xFrom; i <= k; i++) { const xx = this.X(i), yy = Y(v[i]); i === this.xFrom ? ctx.moveTo(xx, yy) : ctx.lineTo(xx, yy); }
      const hv = this.at(j, d);
      ctx.lineTo(this.X(d), Y(hv));
      ctx.strokeStyle = s.color; ctx.lineWidth = s.width || 6; ctx.globalAlpha = s.alpha == null ? 1 : s.alpha;
      if (s.glow) { ctx.shadowColor = s.color; ctx.shadowBlur = 18; }
      ctx.stroke(); ctx.shadowBlur = 0; ctx.globalAlpha = 1;
      heads.push({ j, x: this.X(d), y: Y(hv), v: hv, s });
    });
    if (!opt.noHeads) for (const h of heads) {
      if (h.s.noHead) continue;
      ctx.beginPath(); ctx.arc(h.x, h.y, 11, 0, Math.PI * 2); ctx.fillStyle = "#0B1428"; ctx.fill();
      ctx.lineWidth = 6; ctx.strokeStyle = h.s.color; ctx.stroke();
    }
    ctx.restore();
    this.heads = heads;
    return heads;
  };

  // 말 칩 (값 이름표) — 화살 끝 (x, y) 위쪽(up=true) 또는 아래
  function pin(ctx, x, y, text, color, alpha, up, size, bounds) {
    if (alpha <= 0) return;
    size = size || 36;
    ctx.save(); ctx.globalAlpha = Math.min(1, alpha);
    ctx.font = `900 ${size}px ${FONT}`;
    const w = ctx.measureText(text).width + 28, h = size + 22, dy = up === false ? 26 : -26 - h;
    const [b0, b1] = bounds || [44, 1876];                // 칩 상자가 들어갈 가로 범위 (옆 칸을 덮지 않게)
    let bx = Math.max(b0, Math.min(b1 - w, x - w / 2));
    const by = y + dy;
    ctx.fillStyle = "rgba(5,10,22,.88)"; ctx.strokeStyle = color; ctx.lineWidth = 3;
    rr(ctx, bx, by, w, h, 12); ctx.fill(); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(x, y + (up === false ? 12 : -12)); ctx.lineTo(x, up === false ? by : by + h); ctx.stroke();
    ctx.fillStyle = "#fff"; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText(text, bx + w / 2, by + h / 2 + 2);
    ctx.restore();
  }
  function rr(ctx, x, y, w, h, r) { ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath(); }
  function coin(ctx, x, y, r, alpha, color) {
    ctx.save(); ctx.globalAlpha = alpha;
    const g = ctx.createRadialGradient(x - r * 0.35, y - r * 0.35, r * 0.2, x, y, r);
    g.addColorStop(0, "#FFF3A6"); g.addColorStop(1, color || "#E8B800");
    ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fillStyle = g; ctx.fill();
    ctx.lineWidth = Math.max(2, r * 0.14); ctx.strokeStyle = "rgba(90,60,0,.55)"; ctx.stroke();
    ctx.fillStyle = "rgba(90,60,0,.75)"; ctx.font = `900 ${Math.round(r * 1.1)}px ${FONT}`; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText("$", x, y + 1);
    ctx.restore();
  }

  // 시각 → 날: 기준점 [[t, d]] 사이를 같은 속도로 (기준점 밖은 끝 값). 구간 속도를 [PACE] 로 남김 (너무 빠르면 경고).
  function warp(anchors, name, maxSpeed) {
    const A = anchors.slice().sort((p, q) => p[0] - q[0]);
    for (let i = 1; i < A.length; i++) if (A[i][1] < A[i - 1][1] - 1e-9) throw new Error(`[PACE] ${name}: 날이 거꾸로 감 ${JSON.stringify(A[i - 1])} → ${JSON.stringify(A[i])}`);
    const segs = [];
    for (let i = 1; i < A.length; i++) {
      const v = (A[i][1] - A[i - 1][1]) / Math.max(1e-6, A[i][0] - A[i - 1][0]);
      segs.push({ t0: +A[i - 1][0].toFixed(2), t1: +A[i][0].toFixed(2), d0: A[i - 1][1], d1: A[i][1], v: +v.toFixed(1) });
    }
    const vmax = Math.max(...segs.map(s => s.v)), lim = maxSpeed || 120;
    const line = `[PACE] ${name} anchors=${A.length} days=${(A[A.length - 1][1] - A[0][1]).toFixed(0)} sec=${(A[A.length - 1][0] - A[0][0]).toFixed(1)} v_max=${vmax} v_mean=${((A[A.length - 1][1] - A[0][1]) / Math.max(1e-6, A[A.length - 1][0] - A[0][0])).toFixed(1)}`;
    (G.PACE_LOG = G.PACE_LOG || []).push({ name, line, segs });
    if (vmax > lim) console.warn(`${line} — 구간 속도 ${vmax} 날/초 > ${lim}`);
    const f = t => {
      if (t <= A[0][0]) return A[0][1];
      for (let i = 1; i < A.length; i++) if (t <= A[i][0]) { const u = (t - A[i - 1][0]) / Math.max(1e-6, A[i][0] - A[i - 1][0]); return A[i - 1][1] + (A[i][1] - A[i - 1][1]) * u; }
      return A[A.length - 1][1];
    };
    f.tOf = d => {                                     // 날 → 처음 닿는 시각
      if (d <= A[0][1]) return A[0][0];
      for (let i = 1; i < A.length; i++) if (d <= A[i][1] + 1e-9) { const span = A[i][1] - A[i - 1][1]; return span <= 0 ? A[i][0] : A[i - 1][0] + (A[i][0] - A[i - 1][0]) * (d - A[i - 1][1]) / span; }
      return A[A.length - 1][0];
    };
    f.segs = segs; f.vmax = vmax;
    return f;
  }
  G.R2 = { Chart, pin, coin, rr, warp, fmtMoney, nice, FONT };
})(typeof window !== "undefined" ? window : globalThis);
