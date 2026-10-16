// VERSION: v1.0 — 2026-10-16 — pace.js v1.0 점검: 규칙마다 '적당한 속도'(v_base) 로 10년 경주에 몇 초가 필요한지 · 매매 앞뒤에 쓰는 시간 몫 · 시험 3개.
// node pace_check.mjs [vBase=50]   (숫자 = barrier/anim.js 만, 결과는 아래 로그 — 대본이 생기면 문장 기준점(anchors)으로 다시 점검)
import fs from "fs"; import path from "path"; import { fileURLToPath } from "url";
const HERE = path.dirname(fileURLToPath(import.meta.url));
globalThis.window = globalThis;
eval(fs.readFileSync(path.join(HERE, "../../../stock/source/eonje-maesu-2026-10/backtest/barrier/anim.js"), "utf8"));
eval(fs.readFileSync(path.join(HERE, "pace.js"), "utf8"));
const AN = globalThis.AN, P = globalThis.PACE, N = AN.dates.length, V = +(process.argv[2] || 50);
const idx = d => AN.dates.findIndex(x => x >= d);
const KEYS = [[idx("2020-02-19"), idx("2020-04-17")], [idx("2022-01-03"), idx("2022-03-01")]];   // 예: 코로나 폭락 · 2022 하락 시작 (실제는 대본이 말하는 곳)
const log = (st, kv) => console.log(`[${st}] ${new Date().toISOString()} ` + Object.entries(kv).map(([k, v]) => `${k}=${v}`).join(" "));
log("PACE", { vBase: V, A: P.DEF.A, sigma: P.DEF.sigma, vKey: P.DEF.vKey, vMin: P.DEF.vMin, vMax: P.DEF.vMax, keys: KEYS.map(k => AN.dates[k[0]] + "~" + AN.dates[k[1]]).join(",") });
let tot = 0;
for (const k of AN.order) {
  const tr = AN.rules[k].trades, w = P.weights(tr, N);
  const p0 = P.plan(tr, N, 1, KEYS);                          // T 를 모르므로 v_base = V 가 되는 T 를 구함
  let sw = 0; for (let i = 0; i < N - 1; i++) if (!KEYS.some(([a, b]) => i >= a && i < b)) sw += w[i];
  const T = p0.tKey + sw / V, p = P.plan(tr, N, T, KEYS);
  tot += T;
  log("PACE", { rule: k, trades: tr.length, T_s: T.toFixed(1), vBase: p.vBase.toFixed(1), vEvent: p.vEvent.toFixed(1), key_s: p.tKey.toFixed(1),
    event_days_pct: (100 * p.eventDays / (N - 1)).toFixed(0), event_time_pct: (100 * p.tEvent / T).toFixed(0), uniform_dps: ((N - 1) / T).toFixed(1) });
}
log("PACE", { all10_s: tot.toFixed(0), all10_min: (tot / 60).toFixed(1) });
// 시험: ① 전체 시간 = T ② 지도는 늘 앞으로 ③ 중요한 부분 속도 = vKey ④ warp 는 기준점을 지남
const tr = AN.rules.m1.trades, p = P.plan(tr, N, 45, KEYS);
const sum = p.dt.reduce((a, b) => a + b, 0); let mono = true, prev = -1;
for (let t = 0; t <= 45; t += 0.01) { const f = p.map(t); if (f < prev - 1e-9) mono = false; prev = f; }
const [ka, kb] = KEYS[0], tA = p.dt.slice(0, ka).reduce((a, b) => a + b, 0), tB = p.dt.slice(0, kb).reduce((a, b) => a + b, 0);
const wv = P.warp([[0, 0], [10, 500], [30, 1500], [45, N - 1]], P.weights(tr, N));
const okW = [[0, 0], [10, 500], [30, 1500], [45, N - 1]].every(([t, i]) => Math.abs(wv.f(t) - i) < 1e-6);
const res = { total_eq_T: Math.abs(sum - 45) < 1e-6, monotonic: mono, key_speed: ((kb - ka) / (tB - tA)).toFixed(2), warp_hits_anchors: okW };
log("TEST", res);
if (!(res.total_eq_T && res.monotonic && Math.abs((kb - ka) / (tB - tA) - P.DEF.vKey) < 1e-6 && okW)) { console.error("[TEST] FAIL"); process.exit(1); }
