// VERSION: v1.0 — 2026-10-16 — 주식 1번 v4 경주 속도 (시안). 사용자 지시 2026-10-16 "buy, sell 이 없는 구간만 빠르게 넘겨 있는 부분도 빠르게 넘기니까
//          중요한 부분이 있으면 느리게 그외는 적당한 속도로 조절해":
//   · 날마다 무게 w(i) = 1 + A·exp(−(d/σ)²) — d = 가장 가까운 매수(b)·판정(h) 날까지 거래일 수 → 매매 앞뒤 며칠은 느리게
//   · 내레이션이 말하는 '중요한 부분'(keys = [[날짜 i0, i1]]) 은 v_key 거래일/초로 고정 (느리게)
//   · 나머지는 같은 무게 비율로 나눠 '적당한 속도' v_base — v_min ~ v_max 를 벗어나면 경고 (내레이션 길이·기준점을 고쳐야 함)
//   · 대본 기준점(anchors = [[초, 거래일]])이 있으면 구간마다 같은 방식으로 나눔 → 문장과 날짜가 맞음
// 숫자(매매 날)는 barrier/anim.js 만 씀. 미래 정보: 속도는 편집(언제 천천히 보여 줄지)일 뿐, 화면 값은 늘 그날까지의 값.
(function (G) {
  "use strict";
  const DEF = { A: 1.5, sigma: 4, vKey: 10, vMin: 25, vMax: 75 };
  // 날마다 무게 (i → i+1 한 걸음)
  function weights(trades, N, opt) {
    const o = Object.assign({}, DEF, opt), ev = [];
    for (const t of trades) { ev.push(t.b); if (t.h != null) ev.push(t.h); }
    ev.sort((a, b) => a - b);
    const w = new Float64Array(N);
    let j = 0;
    for (let i = 0; i < N; i++) {
      while (j + 1 < ev.length && Math.abs(ev[j + 1] - i) <= Math.abs(ev[j] - i)) j++;
      const d = ev.length ? Math.abs(ev[j] - i) : 1e9;
      w[i] = 1 + o.A * Math.exp(-((d / o.sigma) ** 2));
    }
    return w;
  }
  // 경주 길이 T 초 (기준점 없이): 중요한 부분은 vKey, 나머지는 무게 비율 → v_base
  function plan(trades, N, T, keys, opt) {
    const o = Object.assign({}, DEF, opt), w = weights(trades, N, o);
    const inKey = new Uint8Array(N); for (const [a, b] of keys || []) for (let i = a; i < b; i++) inKey[i] = 1;
    let sw = 0, nk = 0, ev = 0;
    for (let i = 0; i < N - 1; i++) { if (inKey[i]) nk++; else sw += w[i]; if (w[i] > 1.5) ev++; }
    const tKey = nk / o.vKey, vBase = sw / Math.max(1e-6, T - tKey);
    const dt = new Float64Array(N - 1);                       // 걸음마다 초
    for (let i = 0; i < N - 1; i++) dt[i] = inKey[i] ? 1 / o.vKey : w[i] / vBase;
    let tEv = 0; for (let i = 0; i < N - 1; i++) if (w[i] > 1.5 && !inKey[i]) tEv += dt[i];
    const need = tKey + sw / o.vMax, needSlow = tKey + sw / o.vMin;   // vMax 를 넘지 않으려면 · vMin 보다 느려지지 않으려면
    return { vBase, tKey, keyDays: nk, eventDays: ev, tEvent: tEv, T, ok: vBase <= o.vMax && vBase >= o.vMin, needMinT: need, maxT: needSlow, dt,
             vEvent: vBase / (1 + o.A), map: mapFrom(dt) };
  }
  function mapFrom(dt) {                                      // 초 → 거래일(소수)
    const c = new Float64Array(dt.length + 1); for (let i = 0; i < dt.length; i++) c[i + 1] = c[i] + dt[i];
    return t => { if (t <= 0) return 0; if (t >= c[c.length - 1]) return dt.length; let lo = 0, hi = c.length - 1;
      while (hi - lo > 1) { const m = (lo + hi) >> 1; if (c[m] <= t) lo = m; else hi = m; } return lo + (t - c[lo]) / Math.max(1e-9, c[lo + 1] - c[lo]); };
  }
  // 대본 기준점이 있을 때: 구간 [t_a, t_b] → [i_a, i_b] 안에서 시간을 무게 비율로 나눔 (구간마다 v 를 돌려줌 — 점검용)
  function warp(anchors, w) {
    const A = anchors.slice().sort((x, y) => x[0] - y[0]), seg = [];
    for (let q = 1; q < A.length; q++) {
      const [ta, ia] = A[q - 1], [tb, ib] = A[q]; let s = 0; for (let i = Math.floor(ia); i < Math.ceil(ib); i++) s += w[i];
      seg.push({ ta, tb, ia, ib, sw: s, vBase: s / Math.max(1e-6, tb - ta) });
    }
    const f = t => {
      if (t <= A[0][0]) return A[0][1];
      for (const g of seg) if (t <= g.tb) {
        let need = (t - g.ta) / Math.max(1e-6, g.tb - g.ta) * g.sw, i = Math.floor(g.ia);
        while (i < g.ib && need > w[i]) { need -= w[i]; i++; }
        return Math.min(g.ib, i + need / w[i]);
      }
      return A[A.length - 1][1];
    };
    return { f, seg };
  }
  G.PACE = { DEF, weights, plan, warp };
})(typeof window !== "undefined" ? window : globalThis);
