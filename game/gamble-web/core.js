// VERSION: v0.8.0-web.1 — 2026-11-27 — Godot 데모 v0.8.0 규칙(core/*.gd)을 자바스크립트로 그대로 옮김 (브라우저·Node 공용)
//
// 규칙 원본: game/gamble-demo/core/{rank_cards,cheat_rules,ai_brain,match}.gd — 이름·순서를 그대로 둠 (snake_case 도 그대로)
// 한 턴 = 왕 턴(왕이 고름) → 노예 턴(노예가 고름) → 판단 시간 → 공개   (차례마다 30초)
//   '!' 표시: 노예 시선이 물건에 1.5초 머물면 (진짜·미끼 같음, 시선 끌기 중엔 안 뜸)
//   협력자: 수상한 행동 2.5초로 부르기(보고 있으면 가능성 ↑) → 이어폰으로 3초 뒤 카드
//   밝혀내기: 물건 확인(반사경이면 적중) · 몸 수색(이어폰이면 적중) — 적중하면 그 턴 무효 → 다시 고름
// 난수: 시드 고정 mulberry32 (같은 시드 = 같은 매치). Godot 와 난수 생성기가 달라 같은 시드라도 결과는 다름.
// 연구·교육용 데모 — 실제 돈과 관계없음.
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.GambleCore = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  // ───────────────────────── 로그 ([STAGE] [t=…ms] key=value) ─────────────────────────
  const GameLog = {
    Level: { DEBUG: 0, INFO: 1, WARNING: 2, ERROR: 3 },
    level: 1,
    t0: Date.now(),
    _fmt(v) {
      if (typeof v === "number") return Number.isInteger(v) ? String(v) : v.toFixed(3);
      if (Array.isArray(v) || (v && typeof v === "object")) return JSON.stringify(v);
      return String(v);
    },
    _out(lv, stage, kv) {
      if (lv < GameLog.level) return;
      const parts = [`[${stage}]`, `[t=${Date.now() - GameLog.t0}ms]`];
      for (const k of Object.keys(kv || {})) parts.push(`${k}=${GameLog._fmt(kv[k])}`);
      const line = parts.join(" ");
      if (lv >= 2) console.warn(line); else console.log(line);
    },
    debug(stage, kv) { GameLog._out(0, stage, kv); },
    info(stage, kv) { GameLog._out(1, stage, kv); },
    warn(stage, kv) { GameLog._out(2, stage, kv); },
  };

  // ───────────────────────── 카드 (rank_cards.gd) ─────────────────────────
  const Card = { CITIZEN: 0, KING: 1, ASSASSIN: 2 };
  const Team = { KING_SIDE: 0, ASSASSIN_SIDE: 1 };
  const CARD_NAMES = { 0: "시민", 1: "왕", 2: "암살자" };
  const SIDE_NAMES = { 0: "왕 측", 1: "암살자 측" };
  const WIN_POINTS = { 0: 1, 1: 4 };
  const RankCards = {
    Card, Team, CARD_NAMES, SIDE_NAMES, WIN_POINTS,
    special_of: (side) => (side === Team.KING_SIDE ? Card.KING : Card.ASSASSIN),
    other_side: (side) => (side === Team.KING_SIDE ? Team.ASSASSIN_SIDE : Team.KING_SIDE),
    new_hand: (side) => [Card.CITIZEN, Card.CITIZEN, Card.CITIZEN, Card.CITIZEN, side === Team.KING_SIDE ? Card.KING : Card.ASSASSIN],
    // 1 = a 승, -1 = b 승, 0 = 비김. 왕 > 시민 > 암살자 > 왕
    resolve(a, b) {
      if (a === b) return 0;
      const win = (a === Card.KING && b === Card.CITIZEN) || (a === Card.CITIZEN && b === Card.ASSASSIN) || (a === Card.ASSASSIN && b === Card.KING);
      return win ? 1 : -1;
    },
    p_fair_win_at(side, t) {
      if (t < 1 || t > 5) return 0.0;
      return side === Team.ASSASSIN_SIDE ? 1 / 25 : (2 * (5 - t)) / 25;
    },
    p_perfect_win_at(side, t) {
      if (t < 1 || t > 5) return 0.0;
      if (side === Team.KING_SIDE) return t === 1 ? 1.0 : 0.0;
      return 0.2;
    },
  };

  // ───────────────────────── 값 (cheat_rules.gd) ─────────────────────────
  const CheatRules = {
    PEEK_FIX: 1.5, TURN_SECONDS: 30.0, MIN_TURN_SECONDS: 5.0, EXPOSE_CUT: 10.0, EXPOSE_FAIL_CUT: 10.0,
    ATTENTION_SECONDS: 3.0, ATTENTION_PER_MATCH: 1, COVERS_PER_MATCH: 3, RANDOMS_PER_MATCH: 2, FAKES_PER_MATCH: 2,
    PLACES_PER_MATCH: 2, INSPECTS_PER_MATCH: 3, SEARCHES_PER_MATCH: 2, ACC_CALLS_PER_MATCH: 2,
    ACC_CALL_SECONDS: 2.5, ACC_INFO_DELAY: 3.0, ACC_SUSPECT_RATE: 0.4, OBJECT_SLOTS: 3, TURN_TIME: 0.4,
    STRIKES_TO_LOSE: 2, JUDGE_SECONDS: 5.0, AI_JUDGE_SECONDS: 1.2, AI_DEFEND_DELAY: [0.4, 1.2],
    OBJECTS: {
      lighter: { name: "라이터", mirror: true, look: "lighter" },
      lighter_plain: { name: "라이터", mirror: false, look: "lighter" },
      cigcase: { name: "담뱃갑", mirror: true, look: "cigcase" },
      cigcase_plain: { name: "담뱃갑", mirror: false, look: "cigcase" },
      glass: { name: "술잔", mirror: false, look: "glass" },
      phone: { name: "휴대폰", mirror: false, look: "phone" },
    },
    SUSPICION_ADD: { object: 0.5, call_seen: 0.4, mark: 0.3 },
    is_mirror: (kind) => !!(CheatRules.OBJECTS[kind] && CheatRules.OBJECTS[kind].mirror),
    is_watching: (target) => target === "face" || target === "hands",
  };

  const clampf = (v, lo, hi) => Math.max(lo, Math.min(hi, v));

  // 시드 고정 난수 (mulberry32)
  function makeRng(seed) {
    let a = seed >>> 0;
    return {
      randf() {
        a = (a + 0x6d2b79f5) >>> 0;
        let t = a;
        t = Math.imul(t ^ (t >>> 15), t | 1);
        t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
        return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
      },
      randf_range(lo, hi) { return lo + (hi - lo) * this.randf(); },
      randi_range(lo, hi) { return lo + Math.floor(this.randf() * (hi - lo + 1)); },
    };
  }

  // ───────────────────────── AI (ai_brain.gd) ─────────────────────────
  const PRIOR_LOGODDS = -1.7, SUSPICION_MIN = -4.0, SUSPICION_MAX = 6.0, CHEATER_MIX = 0.5, WATCH_FACE_BASE = 0.35;
  const CAUTION = 0.15; // 경고 1개를 받은 뒤 속임수 확률 배수
  // slave = [cheat, acc, bluff, attention, boldness] · king = [cover, random, fake, expose]
  const PRESETS = {
    honest: [[0, 0, 0, 0, 0], [0.3, 0.1, 0.2, 0.5], 1.0, 1.0, ["glass"]],
    cheater: [[0.7, 0.4, 0.3, 0.5, 0.3], [0.2, 0.05, 0.2, 0.5], 0.8, 0.8, ["lighter", "lighter_plain"]],
    watcher: [[0.25, 0.1, 0.1, 0.3, 0.05], [0.5, 0.2, 0.3, 0.6], 1.4, 1.3, ["cigcase_plain", "cigcase"]],
    gambler: [[0.5, 0.3, 0.6, 0.5, 0.6], [0.3, 0.1, 0.4, 0.4], 1.0, 1.0, ["cigcase_plain", "cigcase", "glass"]],
    inert: [[0, 0, 0, 0, 0], [0, 0, 0, 0], 0.0, 0.0, []],
  };

  class AiBrain {
    constructor() {
      this.display_name = "AI";
      this.suspicion = PRIOR_LOGODDS;
      this.force_watch = "";
      this.configure("honest");
    }
    configure(kind) {
      let p = PRESETS[kind];
      if (!p) { GameLog.warn("AI", { problem: "unknown_preset", kind }); p = PRESETS.honest; }
      this.display_name = kind;
      const [sl, kg, perception, paranoia, objs] = p;
      [this.cheat_rate, this.acc_rate, this.bluff_rate, this.attention_rate, this.boldness] = sl;
      [this.cover_rate, this.random_rate, this.fake_rate, this.expose_rate] = kg;
      this.perception = perception;
      this.paranoia = paranoia;
      this.objects = objs.slice();
    }
    reaction() { return 0.35 / clampf(this.perception, 0.3, 2.0); }
    _extra() { return Math.max(this.suspicion - PRIOR_LOGODDS, 0.0); }
    idle_segment(rng) {
      const r = rng.randf();
      let target = "face";
      if (r >= 0.4) target = r < 0.75 ? "own_card" : "away";
      return { target, dur: rng.randf_range(0.6, 1.8) };
    }
    watch_segment(rng, opp_strikes) {
      if (this.force_watch !== "") return { target: this.force_watch, dur: 99.0 };
      const bonus = opp_strikes >= 1 ? 0.2 : 0.0;
      const p_face = clampf(WATCH_FACE_BASE + 0.12 * this._extra() * this.paranoia + bonus, 0.1, 0.85);
      const r = rng.randf();
      let target = "away";
      if (r < p_face) target = "face";
      else {
        const rest = (r - p_face) / Math.max(1.0 - p_face, 0.001);
        if (rest < 0.4) target = "hands";
        else if (rest < 0.65) target = "own_card";
      }
      let dur = target === "face" ? rng.randf_range(0.6, 1.6) : rng.randf_range(0.7, 2.2);
      dur /= clampf(0.6 + 0.4 * this.perception, 0.5, 1.5);
      return { target, dur };
    }
    king_think(rng) { return rng.randf_range(2.0, 6.0); }
    king_defense(rng, ctx) {
      const threat = ctx.opp_objects > 0 || ctx.opp_acc;
      const ex = 0.1 * this._extra() * this.paranoia;
      const r1 = rng.randf(), r2 = rng.randf(), r3 = rng.randf();
      const use_random = threat && ctx.random_left > 0 && r1 < this.random_rate + ex * 0.5;
      const use_cover = !use_random && ctx.opp_objects > 0 && ctx.cover_left > 0 && r2 < this.cover_rate + ex;
      const use_fake = !use_random && threat && ctx.fake_left > 0 && r3 < this.fake_rate + ex * 0.5;
      return { random: use_random, cover: use_cover, fake: use_fake };
    }
    decide_inspect(rng, marked, unchecked) {
      const r1 = rng.randf(), r2 = rng.randf();
      if (marked.length > 0) {
        const p = clampf(this.expose_rate + 0.08 * this._extra() * this.paranoia, 0.0, 0.95);
        return r1 < p ? marked[Math.min(Math.floor(r2 * marked.length), marked.length - 1)] : -1;
      }
      if (unchecked.length === 0) return -1;
      const p2 = clampf(0.04 * this._extra() * this.paranoia, 0.0, 0.3);
      return r1 < p2 ? unchecked[Math.min(Math.floor(r2 * unchecked.length), unchecked.length - 1)] : -1;
    }
    decide_search(rng, acc_suspect) {
      const r = rng.randf();
      if (acc_suspect <= 0.0) return r < clampf(0.02 * this._extra() * this.paranoia, 0.0, 0.2);
      return r < clampf(acc_suspect * (0.4 + this.expose_rate) + 0.05 * this._extra(), 0.0, 0.9);
    }
    on_seen(kind) {
      const delta = (CheatRules.SUSPICION_ADD[kind] || 0.0) * Math.max(this.paranoia, 0.3);
      this.suspicion = clampf(this.suspicion + delta, SUSPICION_MIN, SUSPICION_MAX);
      return delta;
    }
    on_expose_result(hit) {
      this.suspicion = hit ? PRIOR_LOGODDS : clampf(this.suspicion - 1.0, SUSPICION_MIN, SUSPICION_MAX);
    }
    decide_call(rng, strikes) { return rng.randf() < this.acc_rate * (strikes >= 1 ? CAUTION : 1.0); }
    slave_plan(rng, ctx) {
      const objs = ctx.objects;
      let mirror_idx = -1, decoy_idx = -1;
      objs.forEach((o, i) => {
        const m = CheatRules.is_mirror(o);
        if (m && mirror_idx < 0) mirror_idx = i;
        if (!m && decoy_idx < 0) decoy_idx = i;
      });
      const rate = this.cheat_rate * (ctx.strikes >= 1 ? CAUTION : 1.0);
      const can_peek = mirror_idx >= 0 && !ctx.sealed_peek && !ctx.covered && !ctx.randomized;
      const plan = { peek_obj: -1, bait_obj: -1, attention: false, commit_at: 0.0 };
      const r_peek = rng.randf(), r_bait = rng.randf(), r_att = rng.randf();
      if (can_peek && r_peek < rate) plan.peek_obj = mirror_idx;
      if (decoy_idx >= 0 && r_bait < this.bluff_rate) plan.bait_obj = decoy_idx;
      plan.attention = r_att < this.attention_rate && ctx.attention_left > 0;
      plan.commit_at = rng.randf_range(5.0, 12.0);
      return plan;
    }
    choose_card(rng, hand, side, info) {
      if (info && info.opp_card !== undefined) return AiBrain.best_response(hand, side, info.opp_card);
      const special = RankCards.special_of(side);
      if (!hand.includes(special)) return Card.CITIZEN;
      if (!hand.includes(Card.CITIZEN)) return special;
      return rng.randf() < 1.0 / hand.length ? special : Card.CITIZEN;
    }
    static best_response(hand, side, opp_card) {
      const special = RankCards.special_of(side);
      let want;
      if (side === Team.KING_SIDE) want = opp_card === Card.ASSASSIN ? Card.CITIZEN : special;
      else want = opp_card === Card.KING ? special : Card.CITIZEN;
      if (hand.includes(want)) return want;
      return hand.includes(special) ? special : Card.CITIZEN;
    }
    on_round_result(opp_won, opp_side, decided_turn) {
      let lr = 1.0 - CHEATER_MIX;
      if (opp_won) {
        const pf = RankCards.p_fair_win_at(opp_side, decided_turn), pp = RankCards.p_perfect_win_at(opp_side, decided_turn);
        lr = pf > 0 ? CHEATER_MIX * pp / pf + (1.0 - CHEATER_MIX) : 1.0;
      }
      const delta = this.paranoia * Math.log(lr);
      this.suspicion = clampf(this.suspicion + delta, SUSPICION_MIN, SUSPICION_MAX);
      return delta;
    }
  }

  // ───────────────────────── 매치 (match.gd) ─────────────────────────
  const ROUNDS = 6, EXTRA_ROUNDS = 2, SIM_DT = 0.05, AUTO_GUARD = 600000;
  const Phase = { IDLE: 0, KING_TURN: 1, SLAVE_TURN: 2, JUDGE: 3, REVEALED: 4, MATCH_OVER: 5 };
  const STAT_KEYS = ["info_peek", "info_acc", "info_fake", "marks", "baits", "inspect", "inspect_hit", "search", "search_hit", "caught", "voids",
    "covers", "randoms", "fakes", "attentions", "acc_calls", "acc_connects", "acc_cancels", "objects_placed", "timeouts"];

  class GambleMatch {
    constructor() {
      this.rng = makeRng(0); this.seed_value = 0; this.brains = [null, null];
      this.hands = [[], []]; this.sides = [Team.KING_SIDE, Team.ASSASSIN_SIDE]; this.king = 0; this.slave = 1;
      this.scores = [0, 0]; this.strikes = [0, 0]; this.round_index = -1; this.turn_in_round = 0; this.global_turn = 0;
      this.phase = Phase.IDLE; this.winner = -1; this.end_reason = ""; this.t = 0.0; this.limit = CheatRules.TURN_SECONDS;
      this.committed = [-1, -1]; this.shown_card = -1;
      this.gaze = ["own_card", "own_card"]; this.gaze_prev = ["own_card", "own_card"]; this.gaze_since = [0.0, 0.0]; this.seg_left = [0.0, 0.0];
      this.objects = [[], []]; this.checked = [[], []]; this.marks = [];
      this.covered = false; this.randomized = false; this.faked = false;
      const two = (v) => [v, v];
      this.cover_left = two(CheatRules.COVERS_PER_MATCH); this.random_left = two(CheatRules.RANDOMS_PER_MATCH);
      this.fake_left = two(CheatRules.FAKES_PER_MATCH); this.attention_left = two(CheatRules.ATTENTION_PER_MATCH);
      this.place_left = two(CheatRules.PLACES_PER_MATCH); this.inspect_left = two(CheatRules.INSPECTS_PER_MATCH);
      this.search_left = two(CheatRules.SEARCHES_PER_MATCH); this.acc_calls_left = two(CheatRules.ACC_CALLS_PER_MATCH);
      this.sealed = [{ peek: false, acc: false }, { peek: false, acc: false }];
      this.calling = [false, false]; this.call_progress = [0.0, 0.0]; this.acc_connected = [false, false]; this.acc_suspect = [0.0, 0.0];
      this.acc_wait = -1.0; this.blind_until = -1.0; this.pending_time = [0.0, 0.0];
      this.exposed_turn = { inspect: false, search: false }; this.blocked_sent = false;
      this.info_done = false; this.info_source = ""; this.info_t = 0.0; this.peeked = false;
      this.judge_left = 0.0; this.judge_limit = 0.0; this.plan = [{}, {}];
      this.round_over = false; this.revealed = false; this.last_award = { seat: -1, points: 0 }; this.events = [];
      this.stats = {}; for (const k of STAT_KEYS) this.stats[k] = [0, 0];
      this._summary_sent = false; this._cursor = 0;
    }

    setup(seed, brain0, brain1) {
      if (!brain1) throw new Error("자리 1 은 AI 여야 함");
      this.seed_value = seed; this.rng = makeRng(seed); this.brains = [brain0, brain1];
      for (let s = 0; s < 2; s++) if (this.brains[s]) this._set_objects_raw(s, this.brains[s].objects);
      GameLog.info("MATCH", { event: "setup", seed, seat0: this._brain_name(0), seat1: this._brain_name(1), rounds: ROUNDS,
        turn_seconds: CheatRules.TURN_SECONDS, peek_fix: CheatRules.PEEK_FIX, call_seconds: CheatRules.ACC_CALL_SECONDS });
    }
    set_objects(seat, kinds) {
      if (this.phase !== Phase.IDLE) return this._refuse("set_objects", seat, "started");
      this._set_objects_raw(seat, kinds);
      GameLog.info("SETUP", { seat, objects: this.objects[seat].join(",") });
      return { ok: true };
    }
    start() { this._begin_round(); }
    is_over() { return this.phase === Phase.MATCH_OVER; }
    pop_events() { const out = this.events.slice(this._cursor); this._cursor = this.events.length; return out; }
    actor() { return this.phase === Phase.KING_TURN ? this.king : this.slave; }
    time_left() { return Math.max(this.limit - this.t, 0.0); }
    dwell_progress() {
      if (this.phase !== Phase.SLAVE_TURN) return -1.0;
      if (this._obj_index(this.slave, this.gaze[this.slave]) < 0) return -1.0;
      return clampf((this.t - this.gaze_since[this.slave]) / CheatRules.PEEK_FIX, 0.0, 1.0);
    }
    slave_visible() { return this.t >= this.blind_until; }

    tick(dt, seat0_gaze = "") {
      if (this.phase === Phase.JUDGE) { this._tick_judge(dt, seat0_gaze); return; }
      if (!this._active()) return;
      this.t += dt;
      if (!this.brains[0]) this._set_gaze(0, seat0_gaze !== "" ? seat0_gaze : "table");
      for (let s = 0; s < 2; s++) {
        if (this.brains[s]) {
          this._ai_tick(s, dt);
          if (!this._active()) return;
        }
      }
      this._update_calls(dt);
      if (this.phase === Phase.SLAVE_TURN) {
        this._update_fixation();
        this._update_acc_info(dt);
        if (!this._active()) return;
      }
      if (this.t >= this.limit) this._timeout();
    }

    // ── 사람(자리 0) 행동 ──
    commit(card) {
      if (this.brains[0] || this.actor() !== 0) return this._refuse("commit", 0, "not_your_turn");
      return this.commit_by(0, card);
    }
    place_object(kind) { return this.place_object_by(0, kind); }
    start_call() { return this.start_call_by(0); }
    stop_call() { return this.stop_call_by(0); }
    attention() { return this.attention_by(0); }
    cover() { const w = this.why_not(0, "cover"); if (w) return this._refuse("cover", 0, w); this._cover(0); return { ok: true }; }
    play_random() { const w = this.why_not(0, "random"); if (w) return this._refuse("random", 0, w); this._randomize(0); return { ok: true }; }
    fake() { const w = this.why_not(0, "fake"); if (w) return this._refuse("fake", 0, w); this._fake(0); return { ok: true }; }
    inspect(idx) { return this._inspect(0, idx, "manual"); }
    search() { return this._search(0, "manual"); }
    judge_done() {
      const w = this.why_not(0, "judge_done");
      if (w) return this._refuse("judge_done", 0, w);
      GameLog.info("JUDGE", { event: "done_early", left: this.judge_left });
      this._reveal();
      return { ok: true };
    }
    next() {
      if (this.phase !== Phase.REVEALED) { this._refuse("next", -1, "phase=" + this.phase); return; }
      if (this.round_over) this._begin_round(); else this._begin_turn(false);
    }
    run_auto() {
      if (!this.brains[0] || !this.brains[1]) throw new Error("run_auto 는 AI 둘");
      this.start();
      let guard = 0;
      while (this.phase !== Phase.MATCH_OVER && guard < AUTO_GUARD) {
        if (this.phase === Phase.REVEALED) this.next(); else this.tick(SIM_DT);
        guard++;
      }
      if (guard >= AUTO_GUARD) GameLog.warn("MATCH", { problem: "auto_guard", seed: this.seed_value, phase: this.phase });
    }

    // 행동을 지금 할 수 있는지 — "" 이면 가능. 행동 함수와 화면 버튼이 같은 규칙을 씀
    why_not(seat, action, arg = "") {
      const defending = seat === this.king && (this.phase === Phase.SLAVE_TURN || this.phase === Phase.JUDGE);
      switch (action) {
        case "object":
          if (!this._active()) return "not_active";
          if (!CheatRules.OBJECTS[arg]) return "unknown=" + arg;
          if (this.objects[seat].length >= CheatRules.OBJECT_SLOTS) return "full";
          if (this.place_left[seat] <= 0) return "no_uses";
          break;
        case "call":
          if (seat !== this.slave || !this._active()) return "not_slave";
          if (this.sealed[seat].acc) return "sealed";
          if (this.calling[seat]) return "calling";
          if (this.acc_connected[seat]) return "connected";
          if (this.acc_calls_left[seat] <= 0) return "no_uses";
          break;
        case "stop_call":
          if (!this.calling[seat]) return "not_calling";
          break;
        case "attention":
          if (seat !== this.slave || !this._active()) return "not_slave";
          if (this.attention_left[seat] <= 0) return "no_uses";
          break;
        case "cover": case "random": case "fake": {
          if (seat !== this.king) return "not_king";
          if (this.phase !== Phase.SLAVE_TURN) return "after_commit";
          const left = { cover: this.cover_left, random: this.random_left, fake: this.fake_left }[action][seat];
          if (left <= 0) return "no_uses";
          if ({ cover: this.covered, random: this.randomized, fake: this.faked }[action]) return "done";
          if (action === "fake" && this.info_done) return "already_seen";
          break;
        }
        case "inspect":
          if (!defending) return seat === this.king ? "after_commit" : "not_king";
          if (this.exposed_turn.inspect) return "already_this_turn";
          if (this.inspect_left[seat] <= 0) return "no_uses";
          if (arg === "") {
            if (this._inspectable().length === 0) return "no_target";
          } else {
            const idx = parseInt(arg, 10);
            if (!(idx >= 0 && idx < this.objects[this.slave].length)) return "no_target";
            if (this.checked[this.slave][idx]) return "checked";
          }
          break;
        case "search":
          if (!defending) return seat === this.king ? "after_commit" : "not_king";
          if (this.exposed_turn.search) return "already_this_turn";
          if (this.search_left[seat] <= 0) return "no_uses";
          if (this.sealed[this.slave].acc) return "sealed";
          break;
        case "judge_done":
          if (seat !== this.king || this.phase !== Phase.JUDGE) return "not_judge";
          break;
        default:
          return "unknown_action=" + action;
      }
      return "";
    }

    // ── 자리 공통 행동 ──
    commit_by(seat, card) {
      if (!this._active() || seat !== this.actor() || this.committed[seat] !== -1) return this._refuse("commit", seat, "not_your_turn");
      if (!this.hands[seat].includes(card)) return this._refuse("commit", seat, "card_not_in_hand=" + card);
      this.committed[seat] = card;
      GameLog.info("COMMIT", { seat, role: seat === this.king ? "king" : "slave", t: this.t, limit: this.limit, card: CARD_NAMES[card], info: this.info_source });
      if (this.phase === Phase.KING_TURN) this._start_phase(Phase.SLAVE_TURN); else this._start_judge();
      return { ok: true };
    }
    place_object_by(seat, kind) {
      const w = this.why_not(seat, "object", kind);
      if (w) return this._refuse("object", seat, w);
      this.objects[seat].push(kind); this.checked[seat].push(false);
      if (seat === this.slave && this.phase === Phase.SLAVE_TURN) this.marks.push(false);
      this.place_left[seat] -= 1; this.stats.objects_placed[seat] += 1;
      const seen = this._watched_by_opp(seat), other = 1 - seat;
      if (seen && this.brains[other]) this.brains[other].on_seen("object");
      GameLog.info("OBJECT", { seat, kind, slot: this.objects[seat].length - 1, seen, left: this.place_left[seat] });
      this._emit({ type: "object", seat, kind, slot: this.objects[seat].length - 1, seen });
      return { ok: true, seen };
    }
    start_call_by(seat) {
      const w = this.why_not(seat, "call");
      if (w) return this._refuse("call", seat, w);
      this.acc_calls_left[seat] -= 1; this.calling[seat] = true; this.call_progress[seat] = 0.0; this.stats.acc_calls[seat] += 1;
      GameLog.info("CALL", { seat, event: "start", t: this.t, left: this.acc_calls_left[seat] });
      this._emit({ type: "call_start", seat });
      return { ok: true };
    }
    stop_call_by(seat) {
      const w = this.why_not(seat, "stop_call");
      if (w) return { ok: false, why: w };
      this.calling[seat] = false; this.stats.acc_cancels[seat] += 1;
      GameLog.info("CALL", { seat, event: "cancel", progress: this.call_progress[seat], suspect: this.acc_suspect[seat] });
      this._emit({ type: "call_cancel", seat });
      return { ok: true };
    }
    attention_by(seat) {
      const w = this.why_not(seat, "attention");
      if (w) return this._refuse("attention", seat, w);
      this.attention_left[seat] -= 1; this.blind_until = this.t + CheatRules.ATTENTION_SECONDS; this.stats.attentions[seat] += 1;
      const other = 1 - seat;
      if (this.brains[other]) { this._set_gaze(other, "away"); this.seg_left[other] = CheatRules.ATTENTION_SECONDS; }
      GameLog.info("ATTENTION", { seat, t: this.t, until: this.blind_until });
      this._emit({ type: "attention", seat, until: this.blind_until });
      return { ok: true };
    }

    // ── 진행 ──
    _active() { return this.phase === Phase.KING_TURN || this.phase === Phase.SLAVE_TURN; }
    _begin_round() {
      this.round_index += 1;
      if (this.round_index >= ROUNDS) {
        const tied = this.scores[0] === this.scores[1];
        if (!tied || this.round_index >= ROUNDS + EXTRA_ROUNDS) { this.round_index -= 1; this._finish_by_score(); return; }
      }
      let s0 = this.round_index % 2 === 0 ? Team.KING_SIDE : Team.ASSASSIN_SIDE;
      if (this.round_index >= ROUNDS) s0 = this.rng.randf() < 0.5 ? Team.KING_SIDE : Team.ASSASSIN_SIDE;
      this.sides = [s0, RankCards.other_side(s0)];
      this.king = s0 === Team.KING_SIDE ? 0 : 1; this.slave = 1 - this.king;
      this.hands = [RankCards.new_hand(this.sides[0]), RankCards.new_hand(this.sides[1])];
      this.turn_in_round = 0; this.round_over = false; this.last_award = { seat: -1, points: 0 };
      for (let s = 0; s < 2; s++) { this.acc_connected[s] = false; this.acc_suspect[s] = 0.0; this.calling[s] = false; }
      GameLog.info("DEAL", { round: this.round_index + 1, king: this.king, slave: this.slave });
      this._emit({ type: "round_start", sides: this.sides.slice(), king: this.king });
      this._begin_turn(false);
    }
    _begin_turn(replay) {
      if (this.hands[0].length === 0 || this.hands[1].length === 0) {
        GameLog.warn("TURN", { problem: "empty_hand" }); this.round_over = true; this.phase = Phase.REVEALED; return;
      }
      this.global_turn += 1;
      if (!replay) this.turn_in_round += 1;
      this.committed = [-1, -1]; this.shown_card = -1; this.covered = false; this.randomized = false; this.faked = false; this.revealed = false;
      this.info_done = false; this.info_source = ""; this.peeked = false; this.marks = []; this.acc_wait = -1.0; this._summary_sent = false;
      for (let s = 0; s < 2; s++) if (this.calling[s]) { this.calling[s] = false; this.stats.acc_cancels[s] += 1; }
      GameLog.info("TURN", { round: this.round_index + 1, turn: this.turn_in_round, global_turn: this.global_turn, replay });
      this._emit({ type: "turn_start", turn_in_round: this.turn_in_round, replay });
      this._start_phase(Phase.KING_TURN);
    }
    _start_phase(ph) {
      this.phase = ph; this.t = 0.0;
      const who = this.actor();
      this.limit = Math.max(CheatRules.TURN_SECONDS + this.pending_time[who], CheatRules.MIN_TURN_SECONDS);
      this.pending_time[who] = 0.0;
      this.gaze_since = [0.0, 0.0]; this.seg_left = [0.0, 0.0]; this.blind_until = -1.0;
      if (ph === Phase.SLAVE_TURN) {
        this.marks = this.objects[this.slave].map(() => false);
        this.info_done = false; this.info_source = ""; this.peeked = false; this.blocked_sent = false;
        this.exposed_turn = { inspect: false, search: false };
        this.acc_wait = this.acc_connected[this.slave] && !this.sealed[this.slave].acc ? CheatRules.ACC_INFO_DELAY : -1.0;
      }
      GameLog.info("PHASE", { phase: ph === Phase.KING_TURN ? "king" : "slave", actor: who, limit: this.limit });
      this._emit({ type: "phase_start", phase: ph, actor: who, limit: this.limit });
      for (let s = 0; s < 2; s++) this.plan[s] = this.brains[s] ? this._make_plan(s, ph) : {};
    }
    _make_plan(s, ph) {
      const b = this.brains[s];
      if (ph === Phase.KING_TURN) {
        if (s === this.king) return { commit_at: b.king_think(this.rng) };
        const want = b.decide_call(this.rng, this.strikes[s]);
        const after = this.rng.randf_range(0.5, 4.0);
        const eligible = this.why_not(s, "call") === "";
        return { call: want && eligible, call_after: after, bold_checked: false, watched_at: -1.0 };
      }
      if (s === this.king) {
        const d = b.king_defense(this.rng, { opp_objects: this.objects[this.slave].length,
          opp_acc: this.acc_connected[this.slave] || this.acc_suspect[this.slave] > 0.3,
          random_left: this.random_left[s], cover_left: this.cover_left[s], fake_left: this.fake_left[s] });
        const at = this.rng.randf_range(CheatRules.AI_DEFEND_DELAY[0], CheatRules.AI_DEFEND_DELAY[1]);
        return { defense: d, defend_at: at, defended: false };
      }
      return b.slave_plan(this.rng, { objects: this.objects[s], sealed_peek: this.sealed[s].peek, covered: this.covered,
        randomized: this.randomized, strikes: this.strikes[s], attention_left: this.attention_left[s] });
    }
    _ai_tick(s, dt) {
      const p = this.plan[s];
      if (this.phase === Phase.KING_TURN) {
        if (s === this.king) {
          if (this.t >= this.blind_until) this._seg_gaze(s, dt, false);
          if (this.t >= Math.min(p.commit_at !== undefined ? p.commit_at : 3.0, this.limit - 0.5)) this._ai_king_commit(s);
          return;
        }
        this._seg_gaze(s, dt, false);
        this._ai_call(s, p);
        return;
      }
      if (s === this.king) {
        if (p.defended === false && this.t >= p.defend_at) { p.defended = true; this._ai_king_defend(s, p.defense); }
        if (this.t >= this.blind_until) this._seg_gaze(s, dt, true);
        return;
      }
      this._ai_slave_gaze(s, dt);
      const commit_at = p.commit_at !== undefined ? p.commit_at : 8.0;
      if (this.t >= Math.min(commit_at, this.limit - 0.3) || (this.info_done && this.t >= this.info_t + 0.5)) this._ai_slave_commit(s);
    }
    _seg_gaze(s, dt, watching) {
      this.seg_left[s] -= dt;
      if (this.seg_left[s] > 0.0) return;
      const seg = watching ? this.brains[s].watch_segment(this.rng, this.strikes[this.slave]) : this.brains[s].idle_segment(this.rng);
      this._set_gaze(s, seg.target);
      this.seg_left[s] = seg.dur;
    }
    _ai_call(s, p) {
      if (!this.calling[s]) {
        if (p.call && this.t >= p.call_after && !this._watched_by_opp(s)) { p.call = false; this.start_call_by(s); }
        return;
      }
      if (!this._watched_by_opp(s)) { p.watched_at = -1.0; return; }
      if (!(p.watched_at >= 0.0)) p.watched_at = this.t;
      if (this.t - p.watched_at >= this.brains[s].reaction() && !p.bold_checked) {
        p.bold_checked = true;
        if (this.rng.randf() >= this.brains[s].boldness) this.stop_call_by(s);
      }
    }
    _ai_slave_gaze(s, dt) {
      this.seg_left[s] -= dt;
      if (this.seg_left[s] > 0.0) return;
      const p = this.plan[s], b = this.brains[s];
      let target = "", dur = 0.0;
      const peek_obj = p.peek_obj !== undefined ? p.peek_obj : -1;
      const want_peek = peek_obj >= 0 && peek_obj < this.objects[s].length && !this.info_done && !this.sealed[s].peek && !this.covered && !this.randomized;
      const bait = p.bait_obj !== undefined ? p.bait_obj : -1;
      if (bait >= 0 && bait < this.objects[s].length) {
        target = "obj" + bait; dur = CheatRules.PEEK_FIX + 0.3; p.bait_obj = -1;
      } else if (want_peek) {
        if (p.attention && this.why_not(s, "attention") === "") { p.attention = false; this.attention_by(s); }
        target = "obj" + peek_obj; dur = CheatRules.PEEK_FIX + 0.25;
      } else {
        const seg = b.idle_segment(this.rng); target = seg.target; dur = seg.dur;
      }
      this._set_gaze(s, target);
      this.seg_left[s] = dur;
    }
    _ai_king_commit(s) { this.commit_by(s, this.brains[s].choose_card(this.rng, this.hands[s], this.sides[s], {})); }
    _ai_king_defend(s, d) {
      if (d.random && this.why_not(s, "random") === "") { this._randomize(s); return; }
      if (d.fake && this.why_not(s, "fake") === "") this._fake(s);
      if (d.cover && this.why_not(s, "cover") === "") this._cover(s);
    }
    _ai_slave_commit(s) {
      const info = this.info_done ? { opp_card: this.shown_card } : {};
      this.commit_by(s, this.brains[s].choose_card(this.rng, this.hands[s], this.sides[s], info));
    }
    _timeout() {
      const who = this.actor();
      this.stats.timeouts[who] += 1;
      const card = this.hands[who][this.rng.randi_range(0, this.hands[who].length - 1)];
      GameLog.warn("TIMEOUT", { seat: who, t: this.t, limit: this.limit, auto_card: CARD_NAMES[card] });
      this._emit({ type: "timeout", seat: who, card });
      this.commit_by(who, card);
    }
    _start_judge() {
      this.phase = Phase.JUDGE;
      this.judge_limit = this.brains[this.king] ? CheatRules.AI_JUDGE_SECONDS : CheatRules.JUDGE_SECONDS;
      this.judge_left = this.judge_limit;
      if (this.brains[this.slave]) this._set_gaze(this.slave, "own_card");
      if (this.brains[this.king]) this._set_gaze(this.king, "face");
      GameLog.info("JUDGE", { event: "start", king: this.king, seconds: this.judge_limit, marks: this.marks,
        acc_suspect: this.acc_suspect[this.slave], peeked: this.peeked, acc_connected: this.acc_connected[this.slave] });
      this._emit({ type: "judge_start", king: this.king, limit: this.judge_limit });
      if (this.brains[this.king]) this._ai_judge(this.king);
    }
    _ai_judge(k) {
      const kb = this.brains[k];
      const marked = [];
      for (let i = 0; i < this.marks.length; i++) if (this.marks[i] && !this.checked[this.slave][i]) marked.push(i);
      const idx = kb.decide_inspect(this.rng, marked, this._inspectable());
      if (idx >= 0 && this.why_not(k, "inspect", String(idx)) === "") {
        this._inspect(k, idx, "ai");
        if (this.phase !== Phase.JUDGE) return;
      }
      if (kb.decide_search(this.rng, this.acc_suspect[this.slave]) && this.why_not(k, "search") === "") this._search(k, "ai");
    }
    _tick_judge(dt, seat0_gaze) {
      if (!this.brains[0]) this._set_gaze(0, seat0_gaze !== "" ? seat0_gaze : "table");
      this.judge_left -= dt;
      if (this.judge_left <= 0.0) { GameLog.info("JUDGE", { event: "time_up" }); this._reveal(); }
    }

    // ── 방어 (낸 뒤) ──
    _cover(s) {
      this.covered = true; this.cover_left[s] -= 1; this.stats.covers[s] += 1;
      GameLog.info("COVER", { seat: s, t: this.t, left: this.cover_left[s] });
      this._emit({ type: "cover", seat: s });
    }
    _randomize(s) {
      this.randomized = true; this.random_left[s] -= 1; this.stats.randoms[s] += 1;
      this.committed[s] = this.hands[s][this.rng.randi_range(0, this.hands[s].length - 1)];
      GameLog.info("RANDOM", { seat: s, t: this.t, left: this.random_left[s] });
      this._emit({ type: "random", seat: s });
    }
    _fake(s) {
      this.faked = true; this.fake_left[s] -= 1; this.stats.fakes[s] += 1;
      GameLog.info("FAKE", { seat: s, t: this.t, left: this.fake_left[s] });
      this._emit({ type: "fake", seat: s });
    }
    _fake_of(card) { return card === Card.CITIZEN ? RankCards.special_of(this.sides[this.king]) : Card.CITIZEN; }
    _inspect(by, idx, how) {
      const w = this.why_not(by, "inspect", String(idx));
      if (w) return this._refuse("inspect", by, w);
      this.exposed_turn.inspect = true; this.inspect_left[by] -= 1; this.stats.inspect[by] += 1;
      const s = this.slave, kind = this.objects[s][idx], hit = CheatRules.is_mirror(kind);
      if (hit) {
        this.stats.inspect_hit[by] += 1;
        this.objects[s].splice(idx, 1); this.checked[s].splice(idx, 1);
        if (idx < this.marks.length) this.marks.splice(idx, 1);
        this.sealed[s].peek = true;
      } else this.checked[s][idx] = true;
      return this._expose_result(by, "inspect", hit, how, { obj: idx, obj_kind: kind });
    }
    _search(by, how) {
      const w = this.why_not(by, "search");
      if (w) return this._refuse("search", by, w);
      this.exposed_turn.search = true; this.search_left[by] -= 1; this.stats.search[by] += 1;
      const s = this.slave, hit = this.acc_connected[s] || this.calling[s];
      if (hit) { this.stats.search_hit[by] += 1; this.sealed[s].acc = true; this.acc_connected[s] = false; this.calling[s] = false; }
      return this._expose_result(by, "search", hit, how, { suspect: this.acc_suspect[s] });
    }
    _expose_result(by, kind, hit, how, extra) {
      const s = this.slave;
      if (hit) { this.strikes[s] += 1; this.stats.caught[s] += 1; this.pending_time[s] -= CheatRules.EXPOSE_CUT; }
      else this.pending_time[by] -= CheatRules.EXPOSE_FAIL_CUT;
      if (this.brains[by]) this.brains[by].on_expose_result(hit);
      const ev = Object.assign({ type: "expose", by, kind, hit, how, strikes: this.strikes.slice(), judge: this.phase === Phase.JUDGE }, extra);
      GameLog.info("EXPOSE", { by, kind, how, hit, phase: this.phase, t: this.t, strikes: this.strikes[s],
        slave_pending: this.pending_time[s], king_pending: this.pending_time[by], extra });
      this._emit(ev);
      if (hit && this.strikes[s] >= CheatRules.STRIKES_TO_LOSE) this._end_match(by, "CAUGHT_TWICE");
      else if (hit) this._void_turn(kind);
      return { ok: true, hit };
    }
    _void_turn(kind) {
      this.stats.voids[this.slave] += 1;
      GameLog.info("VOID", { round: this.round_index + 1, turn: this.turn_in_round, by: kind });
      this._emit({ type: "turn_void", kind });
      this._begin_turn(true);
    }

    // ── 시선·협력자 ──
    _obj_index(seat, g) {
      if (typeof g !== "string" || !g.startsWith("obj")) return -1;
      const idx = parseInt(g.slice(3), 10);
      return idx >= 0 && idx < this.objects[seat].length ? idx : -1;
    }
    _inspectable() {
      const out = [];
      for (let i = 0; i < this.objects[this.slave].length; i++) if (!this.checked[this.slave][i]) out.push(i);
      return out;
    }
    _watched_by_opp(seat) {
      const other = 1 - seat;
      return CheatRules.is_watching(this.gaze[other]) && !this._turning(other) && this.t >= this.blind_until;
    }
    _update_fixation() {
      const s = this.slave, k = this.king;
      const idx = this._obj_index(s, this.gaze[s]);
      if (idx < 0) return;
      const dur = this.t - this.gaze_since[s];
      const vis = this.t - Math.max(this.gaze_since[s], this.blind_until);
      const kind = this.objects[s][idx];
      const real = CheatRules.is_mirror(kind) && !this.sealed[s].peek;
      if (real && !this.info_done && dur >= CheatRules.PEEK_FIX) {
        if (this.randomized || this.covered) {
          if (!this.blocked_sent) {
            this.blocked_sent = true;
            this._emit({ type: "info_blocked", seat: s, source: "peek", why: this.randomized ? "random" : "cover" });
          }
        } else { this._give_info("peek"); this.peeked = true; }
      }
      if (vis >= CheatRules.PEEK_FIX && idx < this.marks.length && !this.marks[idx]) {
        this.marks[idx] = true; this.stats.marks[s] += 1;
        if (!CheatRules.is_mirror(kind)) this.stats.baits[s] += 1;
        GameLog.info("MARK", { slave: s, obj: idx, kind, t: this.t });
        this._emit({ type: "mark", seat: s, obj: idx });
        if (this.brains[k]) this.brains[k].on_seen("mark");
      }
    }
    _update_acc_info(dt) {
      if (this.acc_wait < 0.0) return;
      this.acc_wait -= dt;
      if (this.acc_wait > 0.0) return;
      this.acc_wait = -1.0;
      if (!this.acc_connected[this.slave] || this.sealed[this.slave].acc || this.info_done) return;
      if (this.randomized) { this._emit({ type: "info_blocked", seat: this.slave, source: "acc", why: "random" }); return; }
      this._give_info("acc");
    }
    _give_info(source) {
      this.info_done = true; this.info_source = source; this.info_t = this.t;
      this.shown_card = this.faked ? this._fake_of(this.committed[this.king]) : this.committed[this.king];
      this.stats[source === "peek" ? "info_peek" : "info_acc"][this.slave] += 1;
      if (this.faked) this.stats.info_fake[this.slave] += 1;
      GameLog.info("INFO", { seat: this.slave, source, shown: CARD_NAMES[this.shown_card], fake: this.faked, t: this.t });
      this._emit({ type: "info", seat: this.slave, source, card: this.shown_card });
    }
    _update_calls(dt) {
      for (let s = 0; s < 2; s++) {
        if (!this.calling[s]) continue;
        this.call_progress[s] += dt;
        const other = 1 - s;
        if (this._watched_by_opp(s)) {
          const perc = this.brains[other] ? this.brains[other].perception : 1.0;
          const before = this.acc_suspect[s];
          this.acc_suspect[s] = Math.min(before + CheatRules.ACC_SUSPECT_RATE * perc * dt, 1.0);
          if (before < 0.5 && this.acc_suspect[s] >= 0.5) {
            if (this.brains[other]) this.brains[other].on_seen("call_seen");
            this._emit({ type: "call_seen", seat: s, suspect: this.acc_suspect[s] });
          }
        }
        if (this.call_progress[s] >= CheatRules.ACC_CALL_SECONDS) {
          this.calling[s] = false; this.acc_connected[s] = true; this.stats.acc_connects[s] += 1;
          GameLog.info("CALL", { seat: s, event: "connected", t: this.t, suspect: this.acc_suspect[s] });
          this._emit({ type: "acc_connected", seat: s });
          if (this.phase === Phase.SLAVE_TURN && s === this.slave && this.acc_wait < 0.0 && !this.info_done) this.acc_wait = CheatRules.ACC_INFO_DELAY;
        }
      }
    }
    _set_gaze(seat, target) {
      if (this.gaze[seat] === target) return;
      this.gaze_prev[seat] = this.gaze[seat]; this.gaze[seat] = target; this.gaze_since[seat] = this.t;
      GameLog.debug("GAZE", { seat, from: this.gaze_prev[seat], to: target, t: this.t });
    }
    _turning(seat) { return this.t - this.gaze_since[seat] < CheatRules.TURN_TIME; }

    // ── 공개·끝 ──
    _reveal() {
      const c0 = this.committed[0], c1 = this.committed[1];
      if (!this.hands[0].includes(c0) || !this.hands[1].includes(c1)) { GameLog.warn("REVEAL", { problem: "card_not_in_hand", c0, c1 }); return; }
      this.hands[0].splice(this.hands[0].indexOf(c0), 1);
      this.hands[1].splice(this.hands[1].indexOf(c1), 1);
      const res = RankCards.resolve(c0, c1);
      this.phase = Phase.REVEALED; this.revealed = true;
      this._emit_turn_summary();
      GameLog.info("REVEAL", { round: this.round_index + 1, turn: this.turn_in_round, card0: CARD_NAMES[c0], card1: CARD_NAMES[c1], result: res, faked: this.faked, info: this.info_source });
      this._emit({ type: "reveal", cards: [c0, c1], result: res, faked: this.faked, info: this.info_source, shown: this.shown_card, randomized: this.randomized });
      if (res === 0) return;
      const w = res > 0 ? 0 : 1, pts = WIN_POINTS[this.sides[w]];
      this.scores[w] += pts; this.last_award = { seat: w, points: pts }; this.round_over = true;
      GameLog.info("ROUND", { round: this.round_index + 1, winner: w, points: pts, score0: this.scores[0], score1: this.scores[1] });
      this._emit({ type: "round_end", winner: w, points: pts, scores: this.scores.slice() });
      const kb = this.brains[this.king];
      if (kb) {
        const delta = kb.on_round_result(w !== this.king, this.sides[this.slave], this.turn_in_round);
        GameLog.debug("SUSPECT", { seat: this.king, delta, suspicion: kb.suspicion });
      }
    }
    _emit_turn_summary() {
      if (this._summary_sent) return;
      this._summary_sent = true;
      this._emit({ type: "turn_summary", marks: this.marks.slice(), peeked: this.peeked, info: this.info_source, faked: this.faked,
        covered: this.covered, randomized: this.randomized, slave: this.slave, acc_connected: this.acc_connected[this.slave],
        acc_suspect: this.acc_suspect[this.slave], objects: this.objects[this.slave].slice() });
    }
    _end_match(w, reason) {
      this.winner = w; this.end_reason = reason; this.phase = Phase.MATCH_OVER;
      GameLog.info("MATCH", { event: "end", winner: w, reason, score0: this.scores[0], score1: this.scores[1], strikes0: this.strikes[0], strikes1: this.strikes[1] });
      this._emit({ type: "match_end", winner: w, reason, scores: this.scores.slice() });
    }
    _finish_by_score() {
      let w = 2;
      if (this.scores[0] > this.scores[1]) w = 0; else if (this.scores[1] > this.scores[0]) w = 1;
      this._end_match(w, "SCORE");
    }
    _set_objects_raw(seat, kinds) {
      const out = [];
      for (const k of kinds) if (CheatRules.OBJECTS[k] && out.length < CheatRules.OBJECT_SLOTS) out.push(k);
      this.objects[seat] = out; this.checked[seat] = out.map(() => false);
    }
    _emit(ev) { ev.round = this.round_index; ev.turn = this.global_turn; this.events.push(ev); }
    _refuse(action, seat, why) { GameLog.warn("REFUSE", { action, seat, why }); return { ok: false, why }; }
    _brain_name(seat) { return this.brains[seat] ? this.brains[seat].display_name : "human"; }
  }

  return { GameLog, RankCards, CheatRules, AiBrain, GambleMatch, Phase, ROUNDS, SIM_DT, STAT_KEYS, makeRng };
});
