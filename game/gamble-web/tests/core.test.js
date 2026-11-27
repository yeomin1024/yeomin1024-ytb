// VERSION: v0.8.0-web.1 — 2026-11-27 — Godot tests/run_tests.gd v0.8.0 과 같은 시험을 웹판 규칙(core.js)에 (Node 로 실행)
// 실행: node game/gamble-web/tests/core.test.js   (실패가 있으면 종료 코드 1)
"use strict";
const { GameLog, RankCards, CheatRules, AiBrain, GambleMatch, Phase } = require("../core.js");
GameLog.level = GameLog.Level.ERROR; // 시험 중 일부러 내는 거절 경고는 숨김
const DT = 0.05;
let P = 0, F = 0;
const check = (c, m) => { if (c) P++; else { F++; console.error("  FAIL: " + m); } };
const brain = (kind, kw = {}) => { const b = new AiBrain(); b.configure(kind); Object.assign(b, kw); return b; };
const hm = (seed, ai, objs) => { const m = new GambleMatch(); m.setup(seed, null, ai); if (objs) m.set_objects(0, objs); return m; };
const run = (m, sec, g) => { const ph = m.phase; for (let i = 0; i < Math.ceil(sec / DT - 1e-9); i++) { m.tick(DT, g); if (m.phase !== ph) return; } };
const runUntil = (m, cond, g, sec = 40) => { for (let i = 0; i < Math.floor(sec / DT); i++) { if (cond()) return true; m.tick(DT, g); } return cond(); };
const startSlave = (m) => { m.round_index = 0; m.start(); runUntil(m, () => m.phase === Phase.SLAVE_TURN, "table"); };
const first = (m, t) => m.events.find((e) => e.type === t) || null;
const eq = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const { KING, CITIZEN, ASSASSIN } = RankCards.Card;

const tests = {
  rules_table() {
    check(RankCards.resolve(KING, CITIZEN) === 1 && RankCards.resolve(CITIZEN, ASSASSIN) === 1 && RankCards.resolve(ASSASSIN, KING) === 1, "왕 > 시민 > 암살자 > 왕");
    check(RankCards.resolve(CITIZEN, CITIZEN) === 0, "시민 = 시민");
    check(CheatRules.is_mirror("lighter") && !CheatRules.is_mirror("lighter_plain") && CheatRules.TURN_SECONDS === 30, "반사경 여부 · 턴 30초");
  },
  phases() {
    const m = hm(1, brain("inert")); m.start();
    check(m.king === 0 && m.phase === Phase.KING_TURN && m.actor() === 0 && m.limit === 30, "1판: 사람 왕 턴 30초");
    m.commit(m.hands[0][0]); check(m.phase === Phase.SLAVE_TURN && m.actor() === 1, "그다음 AI 노예 턴");
    run(m, 15.0, "table"); check(m.phase === Phase.JUDGE, "AI 노예가 냄 → 판단 시간");
    run(m, 5.1, "table"); check(m.phase === Phase.REVEALED, "판단 끝 → 공개");
    const m2 = hm(2, brain("inert")); m2.round_index = 0; m2.start();
    check(m2.king === 1 && m2.phase === Phase.KING_TURN && m2.actor() === 1, "2판: AI 왕 턴");
    run(m2, 7.0, "table"); check(m2.phase === Phase.SLAVE_TURN && m2.actor() === 0 && m2.committed[1] !== -1, "그다음 사람 노예 턴");
  },
  defense_after_commit() {
    const m = hm(3, brain("inert"), ["lighter"]); m.start();
    check(["cover", "random", "fake", "inspect", "search"].every((a) => m.why_not(0, a) === "after_commit"), "고르는 중엔 방어 못 함");
    m.commit(m.hands[0][0]);
    check(m.cover().ok && m.fake().ok, "낸 뒤 가리기·바꿔치기");
    check(m.play_random().ok && m.hands[0].includes(m.committed[0]) && m.randomized, "낸 뒤 섞기");
  },
  objects() {
    const m = hm(20, brain("inert"), ["lighter", "glass", "phone", "cigcase"]); check(m.objects[0].length === 3, "사전 설정 3개까지");
    const m2 = hm(21, brain("inert"), []); m2.start();
    check(!m2.set_objects(0, ["glass"]).ok, "시작 뒤엔 사전 설정 불가");
    check(m2.place_object("lighter").ok && m2.place_object("lighter_plain").ok, "게임 중 두 번");
    const r = m2.place_object("glass"); check(!r.ok && r.why === "no_uses", "게임 중 놓기 2번 제한");
  },
  peek_gauge() {
    const m = hm(4, brain("inert"), ["lighter", "glass"]); startSlave(m);
    run(m, 1.0, "obj0"); const g = m.dwell_progress(); check(!first(m, "info") && g > 0.5 && g < 0.8, "1초: 카드 X, 게이지 ~0.67");
    run(m, 0.1, "table"); run(m, 1.0, "obj0"); check(!first(m, "info"), "눈을 떼면 처음부터");
    run(m, 0.6, "obj0"); const ev = first(m, "info");
    check(ev && ev.card === m.committed[m.king] && ev.source === "peek" && m.marks[0], "1.5초 → 카드 + '!'");
  },
  marks_regardless() {
    const m = hm(5, brain("inert"), ["lighter", "glass"]); startSlave(m);
    run(m, 1.6, "obj1"); check(m.marks[1] && !m.marks[0] && !first(m, "info") && m.stats.baits[0] === 1, "미끼도 '!'");
  },
  call() {
    const w = brain("inert", { perception: 1.0, force_watch: "face" });
    const m = hm(6, w, []); startSlave(m);
    check(m.start_call().ok && m.calling[0], "부르기 시작");
    run(m, 2.6, "table"); check(m.acc_connected[0] && m.acc_suspect[0] >= 0.8, "연결 · 보고 있었으면 가능성 높음");
    run(m, 3.1, "table"); const ev = first(m, "info"); check(ev && ev.source === "acc" && ev.card === m.committed[m.king], "3초 뒤 이어폰");
    const m2 = hm(7, brain("inert", { perception: 1.0, force_watch: "away" }), []); startSlave(m2); m2.start_call(); run(m2, 2.6, "table");
    check(m2.acc_connected[0] && m2.acc_suspect[0] === 0, "안 볼 때 → 가능성 0");
    const m3 = hm(8, w, []); startSlave(m3); m3.start_call(); run(m3, 1.0, "table"); m3.stop_call();
    check(!m3.acc_connected[0] && m3.acc_calls_left[0] === CheatRules.ACC_CALLS_PER_MATCH - 1 && m3.acc_suspect[0] > 0, "멈추면 실패 · 횟수 씀 · 가능성 남음");
  },
  inspect() {
    const b = brain("inert"); b.objects = ["lighter", "glass"];
    const m = hm(9, b); m.start(); m.commit(m.hands[0][0]);
    const r = m.inspect(0);
    check(r.ok && r.hit && m.strikes[1] === 1 && m.sealed[1].peek && eq(m.objects[1], ["glass"]), "반사경 확인 → 적중·압수·봉인");
    check(m.phase === Phase.KING_TURN && m.turn_in_round === 1 && eq(m.committed, [-1, -1]) && first(m, "turn_void"), "그 턴 무효 → 다시 고름");
    m.commit(m.hands[0][0]); check(m.phase === Phase.SLAVE_TURN && m.limit === 20, "노예 다시 고르는 턴 −10초");
    const b2 = brain("inert"); b2.objects = ["lighter", "glass"];
    const m2 = hm(10, b2); m2.start(); m2.commit(m2.hands[0][0]);
    const r2 = m2.inspect(1);
    check(r2.ok && !r2.hit && m2.checked[1][1] && m2.pending_time[0] === -10 && m2.phase === Phase.SLAVE_TURN, "빈 것 → 헛짚음, 내 다음 −10초");
    check(!m2.inspect(0).ok, "턴마다 한 번");
  },
  search() {
    const m = hm(11, brain("inert")); m.start(); m.commit(m.hands[0][0]); m.acc_connected[1] = true;
    const r = m.search(); check(r.hit && m.strikes[1] === 1 && m.sealed[1].acc && !m.acc_connected[1] && m.phase === Phase.KING_TURN, "이어폰 발견 → 무효");
    const m2 = hm(12, brain("inert")); m2.start(); m2.commit(m2.hands[0][0]);
    const r2 = m2.search(); check(!r2.hit && m2.pending_time[0] === -10, "없으면 헛짚음");
  },
  defenses() {
    const m = hm(13, brain("inert"), ["lighter"]); m.round_index = 0; m.start(); m.acc_connected[0] = true;
    runUntil(m, () => m.phase === Phase.SLAVE_TURN, "table"); m._cover(m.king); run(m, 1.6, "obj0");
    check(!first(m, "info") && (first(m, "info_blocked") || {}).why === "cover", "가리기 → 반사경 막힘");
    run(m, 1.6, "table"); check((first(m, "info") || {}).source === "acc", "가리기는 이어폰 못 막음");
    const m2 = hm(14, brain("inert"), ["lighter"]); m2.round_index = 0; m2.start(); m2.acc_connected[0] = true;
    runUntil(m2, () => m2.phase === Phase.SLAVE_TURN, "table"); m2._randomize(m2.king); run(m2, 1.6, "obj0"); run(m2, 2.0, "table");
    check(!first(m2, "info") && m2.hands[m2.king].includes(m2.committed[m2.king]), "섞기 → 둘 다 막힘");
    const m3 = hm(15, brain("inert"), ["lighter"]); startSlave(m3); m3._fake(m3.king); run(m3, 1.6, "obj0");
    const ev = first(m3, "info"); const real = m3.committed[m3.king];
    check(ev && ev.card === m3._fake_of(real) && ev.card !== real, "바꿔치기 → 가짜");
  },
  attention() {
    const m = hm(16, brain("inert", { perception: 1.0, force_watch: "face" }), ["lighter"]); startSlave(m);
    check(m.attention().ok && m.gaze[1] === "away", "시선 끌기 → 딴 곳");
    run(m, 1.6, "obj0"); check(first(m, "info") && !m.marks[0], "그동안 '!' 안 뜸");
    check(!m.attention().ok, "매치 한 번");
  },
  ai_judge() {
    const m = hm(17, brain("inert", { expose_rate: 10.0 }), ["lighter"]); startSlave(m); run(m, 1.6, "obj0"); m.commit(m.hands[0][0]);
    check(m.strikes[0] === 1 && m.sealed[0].peek && m.phase === Phase.KING_TURN && m.objects[0].length === 0, "AI 판단: '!' 반사경 확인 → 무효");
    const m2 = hm(18, brain("inert"), ["lighter"]); startSlave(m2); run(m2, 1.6, "obj0"); m2.commit(m2.hands[0][0]);
    check(m2.strikes[0] === 0 && m2.phase === Phase.JUDGE && m2.judge_limit === CheatRules.AI_JUDGE_SECONDS, "확인 확률 0 → 안 함, 1.2초");
    run(m2, 1.3, "table"); check(m2.phase === Phase.REVEALED, "AI 판단 끝 → 공개");
  },
  two_strikes() {
    const m = hm(19, brain("inert", { expose_rate: 10.0 }), ["lighter"]); startSlave(m); m.strikes[0] = 1; run(m, 1.6, "obj0"); m.commit(m.hands[0][0]);
    check(m.is_over() && m.winner === 1 && m.end_reason === "CAUGHT_TWICE", "경고 2개 → 패배");
  },
  judge() {
    const m = hm(23, brain("inert")); m.start(); m.commit(m.hands[0][0]); runUntil(m, () => m.phase === Phase.JUDGE, "table");
    check(m.judge_limit === CheatRules.JUDGE_SECONDS && m.why_not(0, "inspect") === "no_target" && m.why_not(0, "search") === "", "사람 판단 5초");
    check(m.judge_done().ok && m.phase === Phase.REVEALED, "판단 끝 → 공개");
  },
  buttons_match_rules() {
    const ids = ["lighter", "lighter_plain", "call", "attention", "cover", "random", "fake", "inspect", "search", "judge_done"];
    const state = (kind) => {
      const b = brain("inert"); b.objects = ["lighter", "glass"];
      const m = hm(40, b, ["lighter"]);
      if (kind.startsWith("slave")) m.round_index = 0;
      m.start();
      if (kind === "king_slave_turn") m.commit(m.hands[0][0]);
      else if (kind === "king_judge") { m.commit(m.hands[0][0]); runUntil(m, () => m.phase === Phase.JUDGE, "table"); }
      else if (kind === "slave_slave_turn") runUntil(m, () => m.phase === Phase.SLAVE_TURN, "table");
      return m;
    };
    const rule = (id) => (id === "lighter" || id === "lighter_plain" ? ["object", id] : id === "inspect" ? ["inspect", "0"] : [id, ""]);
    const act = (m, id) => ({ lighter: () => m.place_object("lighter"), lighter_plain: () => m.place_object("lighter_plain"), call: () => m.start_call(),
      attention: () => m.attention(), cover: () => m.cover(), random: () => m.play_random(), fake: () => m.fake(), inspect: () => m.inspect(0),
      search: () => m.search(), judge_done: () => m.judge_done() })[id]().ok;
    for (const st of ["king_turn", "king_slave_turn", "king_judge", "slave_king_turn", "slave_slave_turn"]) {
      const bad = ids.filter((id) => { const m = state(st); const pred = m.why_not(0, ...rule(id)) === ""; return pred !== !!act(m, id); });
      check(bad.length === 0, `버튼과 규칙이 다름 ${st} ${bad}`);
    }
  },
  ai_ignores_hidden_card() {
    const f = (s, c) => { const m = hm(s, brain("honest")); m.start(); m.commit(c); runUntil(m, () => m.phase === Phase.REVEALED, "table"); const e = first(m, "reveal"); return e ? e.cards[1] : -1; };
    let same = true; for (let s = 100; s < 140; s++) if (f(s, KING) !== f(s, CITIZEN)) same = false;
    check(same, "AI 는 숨긴 카드를 모름");
  },
  timeout() {
    const m = hm(24, brain("inert")); m.start(); run(m, 30.5, "table"); check(first(m, "timeout") && m.phase === Phase.SLAVE_TURN, "30초 초과 → 무작위 카드");
  },
  tiebreak() {
    const m = new GambleMatch(); m.setup(10, brain("honest"), brain("honest"));
    m.round_index = 5; m.scores = [3, 3]; m.round_over = true; m.phase = Phase.REVEALED; m.next();
    check(m.round_index === 6 && !m.is_over(), "동점 → 연장");
    m.scores = [5, 4]; m.round_over = true; m.phase = Phase.REVEALED; m.next();
    check(m.is_over() && m.winner === 0 && m.end_reason === "SCORE", "연장에서 갈리면 끝");
  },
  determinism() {
    const ev = (s) => { const m = new GambleMatch(); m.setup(s, brain("cheater"), brain("watcher")); m.run_auto(); return JSON.stringify(m.events); };
    check(ev(777) === ev(777) && ev(777) !== ev(778), "같은 시드 = 같은 매치");
  },
  auto_match_sane() {
    let ok = true, c2 = 0;
    for (let s = 1; s <= 100; s++) {
      const m = new GambleMatch(); m.setup(s, brain("cheater"), brain("gambler")); m.run_auto();
      ok = ok && m.is_over() && Math.max(...m.strikes) <= 2; if (m.end_reason === "CAUGHT_TWICE") c2++;
    }
    check(ok, "AI 대 AI 100판 정상"); console.log(`[TEST] auto_matches=100 caught_twice=${c2}`);
  },
};
const t0 = Date.now();
for (const [name, fn] of Object.entries(tests)) {
  const before = F;
  try { fn(); } catch (e) { F++; console.error(`  FAIL: ${name} threw ${e.stack}`); }
  console.log(`[TEST] name=${name} result=${F === before ? "PASS" : "FAIL"}`);
}
console.log(`[TEST] checks_passed=${P} checks_failed=${F} ms=${Date.now() - t0}`);
process.exit(F > 0 ? 1 : 0);
