// VERSION: v0.8.0-web.1 — 2026-11-27 — AI 대 AI 밸런스 (Godot tools/simulate.gd 와 같은 조합·칸)
// 실행: node game/gamble-web/tools/sim.js [매치 수=1000] [시드=42]
"use strict";
const { GameLog, AiBrain, GambleMatch, STAT_KEYS } = require("../core.js");
GameLog.level = GameLog.Level.ERROR;
const n = parseInt(process.argv[2] || "1000", 10), base = parseInt(process.argv[3] || "42", 10);
const PAIRS = [["honest", "honest"], ["cheater", "honest"], ["honest", "cheater"], ["cheater", "watcher"], ["watcher", "cheater"], ["gambler", "watcher"], ["cheater", "cheater"]];
const mk = (k) => { const b = new AiBrain(); b.configure(k); return b; };
console.log(`[SIM] matches=${n} base_seed=${base}`);
for (const [k0, k1] of PAIRS) {
  const t0 = Date.now(), W = [0, 0, 0], O2 = [0, 0], S = {}; for (const k of STAT_KEYS) S[k] = [0, 0];
  for (let i = 0; i < n; i++) {
    const m = new GambleMatch(); m.setup(base + i, mk(k0), mk(k1)); m.run_auto(); W[m.winner]++;
    if (m.end_reason === "CAUGHT_TWICE") O2[1 - m.winner]++;
    for (const k of STAT_KEYS) for (let s = 0; s < 2; s++) S[k][s] += m.stats[k][s];
  }
  const a = (k, s) => (S[k][s] / n).toFixed(2), r = (x, y) => (y ? (x / y).toFixed(2) : "0.00");
  const side = (s) => `s${s}: info=${((S.info_peek[s] + S.info_acc[s]) / n).toFixed(2)} acc=${a("info_acc", s)} fake=${a("info_fake", s)} caught=${a("caught", s)} out2=${(100 * O2[s] / n).toFixed(1)}% marks=${a("marks", s)} baits=${a("baits", s)} calls=${a("acc_calls", s)} conn=${a("acc_connects", s)} insp=${a("inspect", s)}@${r(S.inspect_hit[s], S.inspect[s])} srch=${a("search", s)}@${r(S.search_hit[s], S.search[s])} voids=${a("voids", s)}`;
  console.log(`[SIM] ${k0} vs ${k1} win=${(100 * W[0] / n).toFixed(1)}/${(100 * W[1] / n).toFixed(1)} | ${side(0)} | ${side(1)} (${Date.now() - t0}ms)`);
}
