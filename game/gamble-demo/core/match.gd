# VERSION: v0.2.0 — 2026-11-26 — 실시간 매치: 속임수 턴·감시 턴 번갈아 · 잔 엿보기(시선 시간) · 들킴(위험률) · 고발(현장)
# 이전 VERSION: v0.1.1 — 2026-11-26 — 전역 enum Side 와 겹치던 enum 이름을 Team 으로
#
# 자리(seat): 0 = 사람(시뮬레이션에선 AI 정책), 1 = AI
# 턴 (전체 턴 번호로 번갈아):
#   홀수 = 속임수 턴 (CHEAT)  : 자리 1 이 먼저 카드를 냄(뒷면) → 자리 0 이 고르는 동안 잔을 보면 엿볼 수 있음.
#                              자리 1 은 자리 0 을 지켜보다가, 자리 0 이 잔을 보는 걸 알아채면 바로 고발(적중).
#   짝수 = 감시 턴 (DETECT)  : 자리 0 이 먼저 냄 → 자리 1 이 고민하는 동안 잔을 몰래 볼 수 있음.
#                              자리 0 은 자리 1 얼굴을 보다가 accuse() — 지금 잔을 보거나 막 뗐으면 적중.
# 흐름: start() → [PLAYER_CHOOSE: tick() · commit()] → (감시 턴만) [AI_THINK: tick() · accuse()] → [REVEALED: next()] → …
# 시간: tick(dt, 사람 시선) 를 매 프레임 부름. 시험·시뮬레이션은 같은 tick 을 고정 dt 로.
# 적중: 경고 +1 · 벌금 · 그 판 몰수(잡은 쪽 진영 점수) · 경고 2개면 즉시 패배. 헛고발: 토큰 −1 · 벌금.
# 연구·교육용 데모 — 실제 돈과 관계없음.
extends RefCounted

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const GameLog = preload("res://core/game_log.gd")

const ROUNDS := 6
const EXTRA_ROUNDS := 2              # 6판 뒤 동점이면 연장 (최대 2판, 진영은 동전)
const SIM_DT := 0.05                 # run_auto 한 걸음 (초)
const SIM_GIVE_UP := 8.0             # 시뮬레이션 자리 0 이 엿보기를 포기하고 내는 시간
const P0_ACCUSE_HOLD := 0.25         # 시뮬레이션 자리 0 은 상대가 잔 보는 걸 이만큼 봐야 고발
const AUTO_GUARD := 400000

enum Phase { IDLE, PLAYER_CHOOSE, AI_THINK, REVEALED, MATCH_OVER }
enum TurnType { CHEAT, DETECT }

var rng := RandomNumberGenerator.new()
var seed_value := 0
var brains: Array = [null, null]
var hands: Array = [[], []]
var sides: Array = [RankCards.Team.KING_SIDE, RankCards.Team.ASSASSIN_SIDE]
var scores: Array = [0, 0]
var strikes: Array = [0, 0]
var tokens: Array = [CheatRules.TOKENS_PER_MATCH, CheatRules.TOKENS_PER_MATCH]
var round_index := -1
var turn_in_round := 0
var global_turn := 0
var turn_type: int = TurnType.CHEAT
var phase: int = Phase.IDLE
var winner := -1                     # -1 진행 중 · 0/1 자리 · 2 무승부
var end_reason := ""
var t := 0.0                         # 이번 턴 경과 시간 (초)
var committed: Array = [-1, -1]      # 이번 턴에 낸 카드 (공개 전엔 뒷면)
var gaze: Array = ["own_card", "own_card"]        # 지금 보는 곳: face · hands · glass · own_card · away · table
var gaze_prev: Array = ["own_card", "own_card"]
var gaze_since: Array = [0.0, 0.0]   # 지금 시선이 시작된 시각 (t)
var seg_left: Array = [0.0, 0.0]     # AI 시선 묶음 남은 시간
var peek_progress: Array = [0.0, 0.0]
var peek_done: Array = [false, false]
var glass_last: Array = [-99.0, -99.0]
var think_left := 0.0
var think_total := 0.0
var ai_will_peek := false
var p0_will_peek := false
var p0_commit_at := 1.0
var p0_seen_glass := 0.0
var round_over := false
var revealed := false                # 이번 턴 카드가 공개됐나 (몰수면 false)
var last_award := {"seat": -1, "points": 0}
var events: Array = []
var stats := {"peek_tries": [0, 0], "peek_done": [0, 0], "caught": [0, 0], "accusations": [0, 0], "hits": [0, 0], "timeouts": [0, 0]}
var turn_glass: Array = [0.0, 0.0]   # 이번 턴 잔을 본 시간
var turn_watched := 0.0              # 잔을 보는 동안 상대가 그 사람 얼굴을 본 시간
var turn_glances := 0                # 이번 턴 자리 1 이 잔으로 눈을 돌린 횟수
var _summary_sent := false
var _cursor := 0


func setup(p_seed: int, brain0, brain1) -> void:
	assert(brain1 != null, "자리 1 은 AI 여야 함")
	seed_value = p_seed
	rng.seed = p_seed
	brains = [brain0, brain1]
	GameLog.info("MATCH", {"event": "setup", "seed": p_seed, "seat0": _brain_name(0), "seat1": _brain_name(1),
		"rounds": ROUNDS, "peek_seconds": CheatRules.PEEK_SECONDS, "turn_seconds": CheatRules.TURN_SECONDS,
		"strikes_to_lose": CheatRules.STRIKES_TO_LOSE})


func start() -> void:
	_begin_round()


func is_over() -> bool:
	return phase == Phase.MATCH_OVER


func pop_events() -> Array:
	var out := events.slice(_cursor)
	_cursor = events.size()
	return out


## 한 걸음. seat0_gaze = 사람이 지금 보는 곳 (자리 0 이 AI 면 무시)
func tick(dt: float, seat0_gaze: String = "") -> void:
	if phase != Phase.PLAYER_CHOOSE and phase != Phase.AI_THINK:
		return
	t += dt
	if brains[0] == null:
		_set_gaze(0, seat0_gaze if seat0_gaze != "" else "table")
	else:
		_p0_policy()
		if phase != Phase.PLAYER_CHOOSE and phase != Phase.AI_THINK:
			return
	_advance_ai_gaze(dt)
	if phase == Phase.PLAYER_CHOOSE:
		if turn_type == TurnType.CHEAT:
			_update_peek(0, dt, CheatRules.PEEK_SECONDS)
			if phase != Phase.PLAYER_CHOOSE:
				return
		if t >= CheatRules.TURN_SECONDS:
			_timeout()
	elif phase == Phase.AI_THINK:
		_update_peek(1, dt, float(brains[1].peek_need_seconds()))
		if brains[0] != null:
			_p0_watch(dt)
			if phase != Phase.AI_THINK:
				return
		think_left -= dt
		if think_left <= 0.0:
			_ai_commit_and_reveal()


## 자리 0 이 카드를 냄. 속임수 턴이면 바로 공개, 감시 턴이면 AI 고민 시작.
func commit(card0: int) -> Dictionary:
	if phase != Phase.PLAYER_CHOOSE:
		return _refuse("commit", 0, "phase=%d" % phase)
	if not hands[0].has(card0):
		return _refuse("commit", 0, "card_not_in_hand=%d" % card0)
	committed[0] = card0
	GameLog.info("COMMIT", {"seat": 0, "turn_type": _tt_name(), "t": t, "peek_done": peek_done[0],
		"card": RankCards.CARD_NAMES[card0]})
	if turn_type == TurnType.CHEAT:
		_reveal()
		return {"ok": true}
	phase = Phase.AI_THINK
	think_total = float(brains[1].think_seconds(rng))
	think_left = think_total
	ai_will_peek = bool(brains[1].decide_peek(rng, int(sides[1]), int(strikes[1])))
	seg_left[1] = 0.0
	GameLog.info("AI_THINK", {"seconds": think_total, "will_peek": ai_will_peek,
		"need_seconds": float(brains[1].peek_need_seconds())})
	_emit({"type": "ai_think_start", "seconds": think_total})
	return {"ok": true}


## 자리 0 의 고발 (감시 턴에만). 자리 1 이 지금 잔을 보거나 막 뗐으면 적중.
func accuse() -> Dictionary:
	if phase != Phase.AI_THINK:
		return _refuse("accuse", 0, "phase=%d" % phase)
	if int(tokens[0]) <= 0:
		return _refuse("accuse", 0, "no_token")
	stats["accusations"][0] += 1
	var looking_now: bool = gaze[1] == "glass"
	var since_glass: float = t - float(glass_last[1])
	var hit: bool = looking_now or since_glass <= CheatRules.GRACE_SECONDS
	if hit:
		stats["hits"][0] += 1
		stats["caught"][1] += 1
		_punish(1, 0, "accuse")
	else:
		tokens[0] -= 1
		scores[0] -= CheatRules.FALSE_ACCUSE_FINE
		scores[1] += CheatRules.FALSE_ACCUSE_FINE
		GameLog.info("ACCUSE", {"accuser": 0, "accused": 1, "hit": false, "t": t, "since_glass": since_glass,
			"tokens_left": tokens[0], "score0": scores[0], "score1": scores[1]})
		_emit({"type": "accuse", "accuser": 0, "hit": false, "by": "accuse", "strikes": strikes.duplicate(),
			"tokens": tokens.duplicate(), "scores": scores.duplicate()})
	return {"ok": true, "hit": hit, "looking_now": looking_now, "since_glass": since_glass}


func next() -> void:
	if phase != Phase.REVEALED:
		_refuse("next", -1, "phase=%d" % phase)
		return
	if round_over:
		_begin_round()
	else:
		_begin_turn()


## 두 자리 모두 AI 일 때 끝까지 (시험·시뮬레이션)
func run_auto() -> void:
	assert(brains[0] != null and brains[1] != null, "run_auto 는 AI 둘")
	start()
	var guard := 0
	while phase != Phase.MATCH_OVER and guard < AUTO_GUARD:
		if phase == Phase.REVEALED:
			next()
		else:
			tick(SIM_DT)
		guard += 1
	if guard >= AUTO_GUARD:
		GameLog.warn("MATCH", {"problem": "auto_guard", "seed": seed_value, "phase": phase})


# ───────────────────────── 내부 ─────────────────────────

func _begin_round() -> void:
	round_index += 1
	if round_index >= ROUNDS:
		var tied: bool = int(scores[0]) == int(scores[1])
		if not tied or round_index >= ROUNDS + EXTRA_ROUNDS:
			round_index -= 1
			_finish_by_score()
			return
	# 판마다 진영을 바꿈 — 자리 0 은 1·3·5판에 왕 측. 연장 판은 동전 던지기
	var s0: int = RankCards.Team.KING_SIDE if round_index % 2 == 0 else RankCards.Team.ASSASSIN_SIDE
	if round_index >= ROUNDS:
		s0 = RankCards.Team.KING_SIDE if rng.randf() < 0.5 else RankCards.Team.ASSASSIN_SIDE
	sides = [s0, RankCards.other_side(s0)]
	hands = [RankCards.new_hand(sides[0]), RankCards.new_hand(sides[1])]
	turn_in_round = 0
	round_over = false
	last_award = {"seat": -1, "points": 0}
	GameLog.info("DEAL", {"round": round_index + 1, "extra": round_index >= ROUNDS,
		"seat0_side": RankCards.SIDE_NAMES[sides[0]], "seat1_side": RankCards.SIDE_NAMES[sides[1]]})
	_emit({"type": "round_start", "sides": sides.duplicate()})
	_begin_turn()


func _begin_turn() -> void:
	if hands[0].is_empty() or hands[1].is_empty():
		GameLog.warn("TURN", {"problem": "empty_hand", "round": round_index + 1})
		round_over = true
		phase = Phase.REVEALED
		return
	global_turn += 1
	turn_in_round += 1
	turn_type = TurnType.CHEAT if global_turn % 2 == 1 else TurnType.DETECT
	phase = Phase.PLAYER_CHOOSE
	t = 0.0
	committed = [-1, -1]
	gaze_since = [0.0, 0.0]
	seg_left = [0.0, 0.0]
	peek_progress = [0.0, 0.0]
	peek_done = [false, false]
	glass_last = [-99.0, -99.0]
	turn_glass = [0.0, 0.0]
	turn_watched = 0.0
	turn_glances = 0
	ai_will_peek = false
	p0_will_peek = false
	p0_seen_glass = 0.0
	_summary_sent = false
	revealed = false
	if turn_type == TurnType.CHEAT:
		committed[1] = brains[1].choose_card(rng, hands[1], sides[1], {})   # 정보 없이 먼저 냄
		GameLog.debug("AI_COMMIT", {"seat": 1, "first": true, "card": RankCards.CARD_NAMES[committed[1]]})
	if brains[0] != null:
		p0_commit_at = float(brains[0].p0_commit_delay(rng))
		if turn_type == TurnType.CHEAT:
			p0_will_peek = bool(brains[0].decide_peek(rng, int(sides[0]), int(strikes[0])))
	GameLog.info("TURN", {"round": round_index + 1, "turn": turn_in_round, "global_turn": global_turn,
		"type": _tt_name(), "first": "seat1" if turn_type == TurnType.CHEAT else "seat0"})
	_emit({"type": "turn_start", "turn_type": turn_type, "turn_in_round": turn_in_round})


func _set_gaze(seat: int, target: String) -> void:
	if gaze[seat] == target:
		return
	gaze_prev[seat] = gaze[seat]
	gaze[seat] = target
	gaze_since[seat] = t
	if seat == 1 and target == "glass":
		turn_glances += 1
	GameLog.debug("GAZE", {"seat": seat, "from": gaze_prev[seat], "to": target, "t": t})


func _turning(seat: int) -> bool:
	return (t - float(gaze_since[seat])) < CheatRules.TURN_TIME


func _advance_ai_gaze(dt: float) -> void:
	var brain = brains[1]
	# 감시 턴: 잔을 보다가 사람이 자기 얼굴을 보는 걸 알면 반응 시간 뒤 눈을 돌림
	if phase == Phase.AI_THINK and gaze[1] == "glass" and gaze[0] == "face":
		var since: float = maxf(float(gaze_since[0]), float(gaze_since[1]))
		if t - since >= float(brain.reaction_seconds()):
			_set_gaze(1, "own_card")
			seg_left[1] = rng.randf_range(0.5, 1.0)
			return
	seg_left[1] -= dt
	if float(seg_left[1]) > 0.0:
		return
	var seg: Dictionary
	if phase == Phase.AI_THINK:
		seg = brain.cheat_segment(rng, gaze[0] == "face", bool(peek_done[1]), ai_will_peek, str(gaze[1]))
	elif turn_type == TurnType.CHEAT:
		seg = brain.watch_segment(rng, int(strikes[0]))
	else:
		seg = brain.idle_segment(rng)
	_set_gaze(1, str(seg["target"]))
	seg_left[1] = float(seg["dur"])


## 잔을 보는 자리(seat)의 진행도·들킴. 자리 0 이 잔을 보면 자리 1 이 알아챌 수 있음.
func _update_peek(seat: int, dt: float, need: float) -> void:
	var looking: bool = gaze[seat] == "glass"
	if looking:
		if float(turn_glass[seat]) == 0.0:
			stats["peek_tries"][seat] += 1
		turn_glass[seat] += dt
		glass_last[seat] = t
		if gaze[1 - seat] == "face" and not _turning(1 - seat):
			turn_watched += dt
		if seat == 0:
			var rate := CheatRules.hazard_rate(str(gaze[1]), _turning(1), float(brains[1].perception))
			if rate > 0.0 and rng.randf() < CheatRules.notice_chance(rate, dt):
				GameLog.info("NOTICE", {"observer": 1, "watch": gaze[1], "rate": rate, "t": t,
					"glass_seconds": turn_glass[0], "progress": peek_progress[0]})
				stats["accusations"][1] += 1
				stats["hits"][1] += 1
				stats["caught"][0] += 1
				_punish(0, 1, "notice")
				return
	if peek_done[seat]:
		return
	peek_progress[seat] = CheatRules.peek_step(float(peek_progress[seat]), looking, dt, need)
	if float(peek_progress[seat]) >= 1.0:
		peek_done[seat] = true
		stats["peek_done"][seat] += 1
		GameLog.info("PEEK", {"seat": seat, "event": "done", "t": t, "glass_seconds": turn_glass[seat]})
		if seat == 0:
			_emit({"type": "peek_info", "card": committed[1]})


func _timeout() -> void:
	stats["timeouts"][0] += 1
	var idx := rng.randi_range(0, hands[0].size() - 1)
	var card: int = hands[0][idx]
	GameLog.warn("TIMEOUT", {"seat": 0, "t": t, "auto_card": RankCards.CARD_NAMES[card]})
	_emit({"type": "timeout", "card": card})
	commit(card)


func _ai_commit_and_reveal() -> void:
	var info := {}
	if peek_done[1]:
		info["opp_card"] = committed[0]
	committed[1] = brains[1].choose_card(rng, hands[1], sides[1], info)
	GameLog.info("AI_COMMIT", {"seat": 1, "peek_done": peek_done[1], "glass_seconds": turn_glass[1],
		"glances": turn_glances, "card": RankCards.CARD_NAMES[committed[1]]})
	_reveal()


func _reveal() -> void:
	var c0: int = committed[0]
	var c1: int = committed[1]
	if not hands[0].has(c0) or not hands[1].has(c1):
		GameLog.warn("REVEAL", {"problem": "card_not_in_hand", "c0": c0, "c1": c1})
		return
	hands[0].erase(c0)
	hands[1].erase(c1)
	var res := RankCards.resolve(c0, c1)
	phase = Phase.REVEALED
	revealed = true
	_emit_turn_summary()
	GameLog.info("REVEAL", {"round": round_index + 1, "turn": turn_in_round, "type": _tt_name(),
		"card0": RankCards.CARD_NAMES[c0], "card1": RankCards.CARD_NAMES[c1], "result": res})
	_emit({"type": "reveal", "cards": [c0, c1], "result": res})
	if res == 0:
		return
	var w := 0 if res > 0 else 1
	var pts: int = RankCards.WIN_POINTS[sides[w]]
	scores[w] += pts
	last_award = {"seat": w, "points": pts}
	round_over = true
	GameLog.info("ROUND", {"round": round_index + 1, "winner": w, "points": pts, "by": "cards",
		"decided_turn": turn_in_round, "score0": scores[0], "score1": scores[1]})
	_emit({"type": "round_end", "winner": w, "points": pts, "by": "cards", "scores": scores.duplicate()})
	for seat in [1, 0]:
		var brain = brains[seat]
		if brain == null:
			continue
		var delta: float = brain.on_round_result(w != seat, sides[1 - seat], turn_in_round)
		GameLog.debug("SUSPECT", {"seat": seat, "delta": delta, "suspicion": brain.suspicion})


func _punish(cheater: int, catcher: int, by: String) -> void:
	strikes[cheater] += 1
	scores[cheater] -= CheatRules.CAUGHT_FINE
	scores[catcher] += CheatRules.CAUGHT_FINE
	peek_done[cheater] = false
	GameLog.info("ACCUSE", {"accuser": catcher, "accused": cheater, "hit": true, "by": by, "t": t,
		"strikes": strikes[cheater], "score0": scores[0], "score1": scores[1]})
	_emit({"type": "accuse", "accuser": catcher, "hit": true, "by": by, "strikes": strikes.duplicate(),
		"tokens": tokens.duplicate(), "scores": scores.duplicate()})
	_emit_turn_summary()
	_forfeit_round(catcher)
	if int(strikes[cheater]) >= CheatRules.STRIKES_TO_LOSE:
		_end_match(catcher, "CAUGHT_TWICE")


func _forfeit_round(winner_seat: int) -> void:
	if round_over and int(last_award["seat"]) >= 0:
		scores[int(last_award["seat"])] -= int(last_award["points"])
	var pts: int = RankCards.WIN_POINTS[sides[winner_seat]]
	scores[winner_seat] += pts
	last_award = {"seat": winner_seat, "points": pts}
	round_over = true
	phase = Phase.REVEALED
	GameLog.info("ROUND", {"round": round_index + 1, "winner": winner_seat, "points": pts, "by": "forfeit",
		"score0": scores[0], "score1": scores[1]})
	_emit({"type": "round_end", "winner": winner_seat, "points": pts, "by": "forfeit", "scores": scores.duplicate()})


func _emit_turn_summary() -> void:
	if _summary_sent:
		return
	_summary_sent = true
	_emit({"type": "turn_summary", "turn_type": turn_type, "glass": turn_glass.duplicate(), "watched": turn_watched,
		"glances": turn_glances, "peek_done": peek_done.duplicate(), "ai_will_peek": ai_will_peek})


## 시뮬레이션 자리 0: 속임수 턴엔 상대가 딴 곳을 보면 잔, 얼굴 쪽이면 상대 얼굴 (반응 시간만큼 늦게 봄)
func _p0_policy() -> void:
	var b = brains[0]
	if phase == Phase.AI_THINK:
		return
	if turn_type == TurnType.CHEAT and p0_will_peek and not peek_done[0] and t < SIM_GIVE_UP:
		var react: float = b.p0_reaction(gaze[0] == "face")
		var seen: String = str(gaze[1]) if (t - float(gaze_since[1])) >= react else str(gaze_prev[1])
		var safe: bool = seen == "own_card" or seen == "away"
		_set_gaze(0, "glass" if safe else "face")
		return
	_set_gaze(0, "own_card")
	var ready: bool = t >= p0_commit_at or peek_done[0] or t >= SIM_GIVE_UP
	if ready:
		var info := {}
		if peek_done[0]:
			info["opp_card"] = committed[1]
		var card: int = b.choose_card(rng, hands[0], sides[0], info)
		commit(card)


## 시뮬레이션 자리 0: 감시 턴엔 상대 얼굴을 자주 보고, 잔 보는 걸 P0_ACCUSE_HOLD 만큼 보면 고발
func _p0_watch(dt: float) -> void:
	var b = brains[0]
	seg_left[0] -= dt
	if float(seg_left[0]) <= 0.0:
		var seg: Dictionary = b.p0_watch_segment(rng)
		_set_gaze(0, str(seg["target"]))
		seg_left[0] = float(seg["dur"])
	if gaze[0] == "face" and gaze[1] == "glass" and not _turning(1):
		p0_seen_glass += dt
		if p0_seen_glass >= P0_ACCUSE_HOLD and int(tokens[0]) > 0:
			p0_seen_glass = 0.0
			accuse()
	else:
		p0_seen_glass = 0.0


func _end_match(w: int, reason: String) -> void:
	winner = w
	end_reason = reason
	phase = Phase.MATCH_OVER
	GameLog.info("MATCH", {"event": "end", "winner": w, "reason": reason, "score0": scores[0], "score1": scores[1],
		"strikes0": strikes[0], "strikes1": strikes[1]})
	_emit({"type": "match_end", "winner": w, "reason": reason, "scores": scores.duplicate()})


func _finish_by_score() -> void:
	var w := 2
	if int(scores[0]) > int(scores[1]):
		w = 0
	elif int(scores[1]) > int(scores[0]):
		w = 1
	_end_match(w, "SCORE")


func _emit(ev: Dictionary) -> void:
	ev["round"] = round_index
	ev["turn"] = global_turn
	events.append(ev)


func _refuse(action: String, seat: int, why: String) -> Dictionary:
	GameLog.warn("REFUSE", {"action": action, "seat": seat, "why": why})
	return {"ok": false, "why": why}


func _tt_name() -> String:
	return "cheat" if turn_type == TurnType.CHEAT else "detect"


func _brain_name(seat: int) -> String:
	return "human" if brains[seat] == null else str(brains[seat].display_name)
