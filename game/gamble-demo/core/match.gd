# VERSION: v0.4.0 — 2026-11-26 — 준비 동작(라이터 놓기·협력자 부르기) · 반사경 엿보기 · 협력자 신호 · 카드 덮개 · 블러핑(시간)
# 이전 VERSION: v0.3.0 — 2026-11-26 — 속임수는 노예(암살자) 측만: 노예 측 판 = 매 턴 속임수 턴, 왕 측 판 = 매 턴 감시 턴
#
# 자리(seat): 0 = 사람(시뮬레이션에선 AI 정책), 1 = AI
# 턴 종류 = 그 판 진영 (속임수는 노예 측만):
#   속임수 턴 (CHEAT)  = 자리 0 이 노예 측: 자리 1(왕)이 먼저 냄 → 자리 0 이 고르는 동안
#       · place_lighter()  — 준비: 라이터(뚜껑 안 반사경)를 테이블에 놓음 (판마다 한 번 · 상대가 손·얼굴을 보면 의심 ↑)
#         → 시선 "shiner" 를 PEEK_SECONDS 두면 상대 카드가 비침 (상대가 카드에 덮개를 올리면 안 비침)
#       · call_accomplice() — 준비: 협력자를 부름 (매치 2번) → ACC_WALK_SECONDS 뒤 상대 뒤에 섬
#         → 시선 "accomplice" 를 SIGNAL_SECONDS 두면 손 신호로 상대 카드 (덮개로 못 막음 · 상대가 뒤를 보면 크게 위험)
#       자리 1 은 지켜보다가 알아채면 바로 고발(적중) — 반사경이면 라이터 몰수, 협력자면 그 매치에서 쫓겨남.
#   감시 턴 (DETECT)  = 자리 0 이 왕 측: 자리 0 이 먼저 냄 → 자리 1(노예)이 고민하는 동안 자기 라이터(반사경)를 몰래 봄
#       · cover_card() — 내 카드에 덮개(칩): 이번 턴 상대 반사경에 안 비침 (매치 2번)
#       · accuse()     — 상대가 지금 반사경을 보거나 GRACE_SECONDS 안이면 적중 (라이터 몰수)
#   bluff() — 여유 부리기 (매치 3번, 법에 걸리지 않음): 내 시간 +, 상대 시간 − (지금 흐르는 시간이면 바로, 아니면 다음 차례)
#             자리 0 의 시간 = 고르는 시간(±5초) · 자리 1 의 시간 = 고민 시간(±2초)
# 흐름: start() → [PLAYER_CHOOSE: tick() · 행동 · commit()] → (감시 턴만) [AI_THINK: tick() · accuse()] → [REVEALED: next()]
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
const P0_ACCUSE_HOLD := 0.25         # 시뮬레이션 자리 0 은 상대가 반사경 보는 걸 이만큼 봐야 고발
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
var turn_limit := CheatRules.TURN_SECONDS   # 이번 턴 자리 0 이 고를 시간 (블러핑으로 바뀜)
var committed: Array = [-1, -1]
var gaze: Array = ["own_card", "own_card"]  # face · hands · shiner · accomplice · own_card · away · behind · table
var gaze_prev: Array = ["own_card", "own_card"]
var gaze_since: Array = [0.0, 0.0]
var seg_left: Array = [0.0, 0.0]
var peek_progress: Array = [0.0, 0.0]       # 반사경 읽기 진행도
var signal_progress := 0.0                   # 협력자 신호 읽기 진행도 (자리 0)
var peek_done: Array = [false, false]
var peek_source := ""                        # "shiner" · "accomplice"
var shiner_last: Array = [-99.0, -99.0]
var think_left := 0.0
var think_total := 0.0
var ai_will_peek := false
var lighter: Array = [false, false]          # 이번 판 라이터(반사경)를 테이블에 놓았나
var covered: Array = [false, false]          # 이번 턴 자기 카드에 덮개를 올렸나
var cover_left: Array = [CheatRules.COVERS_PER_MATCH, CheatRules.COVERS_PER_MATCH]
var bluff_left: Array = [CheatRules.BLUFFS_PER_MATCH, CheatRules.BLUFFS_PER_MATCH]
var pending_time: Array = [0.0, 0.0]         # 다음 자기 시간에 더하거나 뺄 초 (블러핑)
var acc_state := "none"                      # none · walking · present · out(들켜서 쫓겨남)
var acc_walk_left := 0.0
var acc_calls_left := CheatRules.ACC_CALLS_PER_MATCH
var stranger_seen := false
var p0_will_peek := false
var p0_commit_at := 1.0
var p0_seen_glass := 0.0
var round_over := false
var revealed := false
var last_award := {"seat": -1, "points": 0}
var events: Array = []
var stats := {"peek_tries": [0, 0], "peek_done": [0, 0], "signal_done": [0, 0], "caught": [0, 0], "acc_caught": [0, 0],
	"accusations": [0, 0], "hits": [0, 0], "timeouts": [0, 0], "setups": [0, 0], "setups_seen": [0, 0],
	"covers": [0, 0], "bluffs": [0, 0], "acc_calls": [0, 0]}
var turn_look: Array = [0.0, 0.0]            # 이번 턴 반사경·신호를 본 시간
var turn_watched := 0.0                      # 그동안 상대가 그 사람 얼굴을 본 시간
var turn_glances := 0                        # 이번 턴 자리 1 이 반사경으로 눈을 돌린 횟수
var _summary_sent := false
var _cursor := 0


func setup(p_seed: int, brain0, brain1) -> void:
	assert(brain1 != null, "자리 1 은 AI 여야 함")
	seed_value = p_seed
	rng.seed = p_seed
	brains = [brain0, brain1]
	GameLog.info("MATCH", {"event": "setup", "seed": p_seed, "seat0": _brain_name(0), "seat1": _brain_name(1),
		"rounds": ROUNDS, "peek_seconds": CheatRules.PEEK_SECONDS, "signal_seconds": CheatRules.SIGNAL_SECONDS,
		"turn_seconds": CheatRules.TURN_SECONDS, "strikes_to_lose": CheatRules.STRIKES_TO_LOSE})


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
	_advance_accomplice(dt)
	if brains[0] == null:
		_set_gaze(0, seat0_gaze if seat0_gaze != "" else "table")
	else:
		_p0_policy()
		if phase != Phase.PLAYER_CHOOSE and phase != Phase.AI_THINK:
			return
	_advance_ai_gaze(dt)
	if phase == Phase.PLAYER_CHOOSE:
		if turn_type == TurnType.CHEAT:
			_update_player_reading(dt)
			if phase != Phase.PLAYER_CHOOSE:
				return
		if t >= turn_limit:
			_timeout()
	elif phase == Phase.AI_THINK:
		_update_ai_reading(dt)
		if brains[0] != null:
			_p0_watch(dt)
			if phase != Phase.AI_THINK:
				return
		think_left -= dt
		if think_left <= 0.0:
			_ai_commit_and_reveal()


# ───────────────────────── 자리 0 행동 ─────────────────────────

## 준비: 라이터(반사경)를 테이블에 놓음 — 속임수 턴·고르는 중, 판마다 한 번
func place_lighter() -> Dictionary:
	if phase != Phase.PLAYER_CHOOSE or turn_type != TurnType.CHEAT:
		return _refuse("lighter", 0, "not_cheat_choose")
	if bool(lighter[0]):
		return _refuse("lighter", 0, "already")
	lighter[0] = true
	stats["setups"][0] += 1
	var seen: bool = _setup_seen("lighter", gaze[1] == "hands" or gaze[1] == "face")
	GameLog.info("SETUP", {"seat": 0, "kind": "lighter", "t": t, "ai_gaze": gaze[1], "seen": seen})
	_emit({"type": "setup", "seat": 0, "kind": "lighter", "seen": seen})
	# 라이터를 본 상대는 자기 카드에 덮개를 올릴 수 있음
	if seen and not bool(covered[1]) and bool(brains[1].decide_cover(rng, true, int(cover_left[1]))):
		_cover(1)
	return {"ok": true, "seen": seen}


## 준비: 협력자를 부름 — 속임수 턴·고르는 중, 매치 2번 (그 판 동안 상대 뒤에 섬)
func call_accomplice() -> Dictionary:
	if phase != Phase.PLAYER_CHOOSE or turn_type != TurnType.CHEAT:
		return _refuse("accomplice", 0, "not_cheat_choose")
	if acc_state != "none":
		return _refuse("accomplice", 0, "state=" + acc_state)
	if acc_calls_left <= 0:
		return _refuse("accomplice", 0, "no_calls")
	acc_calls_left -= 1
	acc_state = "walking"
	acc_walk_left = CheatRules.ACC_WALK_SECONDS
	stats["acc_calls"][0] += 1
	stats["setups"][0] += 1
	var seen: bool = _setup_seen("accomplice", gaze[1] == "face")
	GameLog.info("SETUP", {"seat": 0, "kind": "accomplice", "t": t, "ai_gaze": gaze[1], "seen": seen, "calls_left": acc_calls_left})
	_emit({"type": "setup", "seat": 0, "kind": "accomplice", "seen": seen})
	return {"ok": true, "seen": seen}


## 내 카드에 덮개(칩) — 감시 턴, 이번 턴 상대 반사경에 안 비침
func cover_card() -> Dictionary:
	if turn_type != TurnType.DETECT or (phase != Phase.PLAYER_CHOOSE and phase != Phase.AI_THINK):
		return _refuse("cover", 0, "not_detect")
	if bool(covered[0]):
		return _refuse("cover", 0, "already")
	if int(cover_left[0]) <= 0:
		return _refuse("cover", 0, "no_uses")
	_cover(0)
	return {"ok": true}


## 블러핑(여유 부리기): 내 시간 +, 상대 시간 −
func bluff() -> Dictionary:
	if phase != Phase.PLAYER_CHOOSE and phase != Phase.AI_THINK:
		return _refuse("bluff", 0, "phase=%d" % phase)
	if int(bluff_left[0]) <= 0:
		return _refuse("bluff", 0, "no_uses")
	_bluff(0)
	return {"ok": true}


## 자리 0 의 고발 (감시 턴에만). 자리 1 이 지금 반사경을 보거나 막 뗐으면 적중.
func accuse() -> Dictionary:
	if phase != Phase.AI_THINK:
		return _refuse("accuse", 0, "phase=%d" % phase)
	if int(tokens[0]) <= 0:
		return _refuse("accuse", 0, "no_token")
	stats["accusations"][0] += 1
	var looking_now: bool = gaze[1] == "shiner"
	var since: float = t - float(shiner_last[1])
	var hit: bool = looking_now or since <= CheatRules.GRACE_SECONDS
	if hit:
		stats["hits"][0] += 1
		stats["caught"][1] += 1
		lighter[1] = false   # 라이터 몰수
		_punish(1, 0, "accuse")
	else:
		tokens[0] -= 1
		scores[0] -= CheatRules.FALSE_ACCUSE_FINE
		scores[1] += CheatRules.FALSE_ACCUSE_FINE
		GameLog.info("ACCUSE", {"accuser": 0, "accused": 1, "hit": false, "t": t, "since_shiner": since,
			"tokens_left": tokens[0], "score0": scores[0], "score1": scores[1]})
		_emit({"type": "accuse", "accuser": 0, "hit": false, "by": "accuse", "strikes": strikes.duplicate(),
			"tokens": tokens.duplicate(), "scores": scores.duplicate()})
	return {"ok": true, "hit": hit, "looking_now": looking_now, "since_shiner": since}


## 자리 0 이 카드를 냄. 속임수 턴이면 바로 공개, 감시 턴이면 AI 고민 시작.
func commit(card0: int) -> Dictionary:
	if phase != Phase.PLAYER_CHOOSE:
		return _refuse("commit", 0, "phase=%d" % phase)
	if not hands[0].has(card0):
		return _refuse("commit", 0, "card_not_in_hand=%d" % card0)
	committed[0] = card0
	GameLog.info("COMMIT", {"seat": 0, "turn_type": _tt_name(), "t": t, "limit": turn_limit,
		"peek_done": peek_done[0], "source": peek_source, "card": RankCards.CARD_NAMES[card0]})
	if turn_type == TurnType.CHEAT:
		_reveal()
		return {"ok": true}
	phase = Phase.AI_THINK
	think_total = maxf(float(brains[1].think_seconds(rng)) + float(pending_time[1]), CheatRules.MIN_TIME_LEFT)
	pending_time[1] = 0.0
	think_left = think_total
	ai_will_peek = false
	if bool(lighter[1]) and not bool(covered[0]):
		ai_will_peek = bool(brains[1].decide_peek(rng, int(sides[1]), int(strikes[1])))
	if ai_will_peek and int(bluff_left[1]) > 0 and bool(brains[1].decide_bluff(rng)):
		_bluff(1)
	seg_left[1] = 0.0
	GameLog.info("AI_THINK", {"seconds": think_total, "will_peek": ai_will_peek,
		"need_seconds": float(brains[1].peek_need_seconds()), "covered": covered[0]})
	_emit({"type": "ai_think_start", "seconds": think_total})
	return {"ok": true}


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
	var s0: int = RankCards.Team.KING_SIDE if round_index % 2 == 0 else RankCards.Team.ASSASSIN_SIDE
	if round_index >= ROUNDS:
		s0 = RankCards.Team.KING_SIDE if rng.randf() < 0.5 else RankCards.Team.ASSASSIN_SIDE
	sides = [s0, RankCards.other_side(s0)]
	hands = [RankCards.new_hand(sides[0]), RankCards.new_hand(sides[1])]
	turn_in_round = 0
	round_over = false
	last_award = {"seat": -1, "points": 0}
	lighter = [false, false]   # 라이터는 판이 끝나면 주머니로
	if acc_state == "walking" or acc_state == "present":
		acc_state = "none"     # 협력자는 판이 끝나면 돌아감 (쫓겨났으면 그대로)
	stranger_seen = false
	GameLog.info("DEAL", {"round": round_index + 1, "extra": round_index >= ROUNDS,
		"seat0_side": RankCards.SIDE_NAMES[sides[0]], "seat1_side": RankCards.SIDE_NAMES[sides[1]]})
	_emit({"type": "round_start", "sides": sides.duplicate()})
	# AI 가 노예 측이면 판 시작에 라이터를 놓을 수 있음 (사람에게 보이는 준비 동작)
	if int(sides[1]) == RankCards.Team.ASSASSIN_SIDE and bool(brains[1].decide_lighter(rng, int(strikes[1]))):
		lighter[1] = true
		stats["setups"][1] += 1
		GameLog.info("SETUP", {"seat": 1, "kind": "lighter", "round": round_index + 1})
		_emit({"type": "setup", "seat": 1, "kind": "lighter", "seen": true})
	_begin_turn()


func _begin_turn() -> void:
	if hands[0].is_empty() or hands[1].is_empty():
		GameLog.warn("TURN", {"problem": "empty_hand", "round": round_index + 1})
		round_over = true
		phase = Phase.REVEALED
		return
	global_turn += 1
	turn_in_round += 1
	turn_type = TurnType.CHEAT if int(sides[0]) == RankCards.Team.ASSASSIN_SIDE else TurnType.DETECT
	phase = Phase.PLAYER_CHOOSE
	t = 0.0
	turn_limit = maxf(CheatRules.TURN_SECONDS + float(pending_time[0]), 3.0)
	pending_time[0] = 0.0
	committed = [-1, -1]
	covered = [false, false]
	gaze_since = [0.0, 0.0]
	seg_left = [0.0, 0.0]
	peek_progress = [0.0, 0.0]
	signal_progress = 0.0
	peek_done = [false, false]
	peek_source = ""
	shiner_last = [-99.0, -99.0]
	turn_look = [0.0, 0.0]
	turn_watched = 0.0
	turn_glances = 0
	ai_will_peek = false
	p0_will_peek = false
	p0_seen_glass = 0.0
	_summary_sent = false
	revealed = false
	GameLog.info("TURN", {"round": round_index + 1, "turn": turn_in_round, "global_turn": global_turn,
		"type": _tt_name(), "limit": turn_limit})
	_emit({"type": "turn_start", "turn_type": turn_type, "turn_in_round": turn_in_round, "limit": turn_limit})
	if turn_type == TurnType.CHEAT:
		committed[1] = brains[1].choose_card(rng, hands[1], sides[1], {})   # 왕 측이 정보 없이 먼저 냄
		GameLog.debug("AI_COMMIT", {"seat": 1, "first": true, "card": RankCards.CARD_NAMES[committed[1]]})
		if bool(brains[1].decide_cover(rng, bool(lighter[0]), int(cover_left[1]))):
			_cover(1)
	if brains[0] != null:
		p0_commit_at = float(brains[0].p0_commit_delay(rng))
		if turn_type == TurnType.CHEAT:
			p0_will_peek = bool(brains[0].decide_peek(rng, int(sides[0]), int(strikes[0])))


func _set_gaze(seat: int, target: String) -> void:
	if gaze[seat] == target:
		return
	gaze_prev[seat] = gaze[seat]
	gaze[seat] = target
	gaze_since[seat] = t
	if seat == 1 and target == "shiner":
		turn_glances += 1
	GameLog.debug("GAZE", {"seat": seat, "from": gaze_prev[seat], "to": target, "t": t})


func _turning(seat: int) -> bool:
	return (t - float(gaze_since[seat])) < CheatRules.TURN_TIME


func _setup_seen(kind: String, in_view: bool) -> bool:
	var seen: bool = in_view and not _turning(1)
	if seen:
		stats["setups_seen"][0] += 1
		var delta: float = brains[1].on_setup_seen(kind)
		GameLog.info("SUSPECT", {"seat": 1, "by": "setup_" + kind, "delta": delta, "suspicion": brains[1].suspicion})
	return seen


func _cover(seat: int) -> void:
	covered[seat] = true
	cover_left[seat] -= 1
	stats["covers"][seat] += 1
	GameLog.info("COVER", {"seat": seat, "t": t, "left": cover_left[seat]})
	_emit({"type": "cover", "seat": seat})


func _bluff(seat: int) -> void:
	bluff_left[seat] -= 1
	stats["bluffs"][seat] += 1
	_adjust_time(seat, 1.0)        # 내 시간 늘림
	_adjust_time(1 - seat, -1.0)   # 상대 시간 줄임
	GameLog.info("BLUFF", {"seat": seat, "t": t, "limit": turn_limit, "think_left": think_left,
		"pending0": pending_time[0], "pending1": pending_time[1], "left": bluff_left[seat]})
	_emit({"type": "bluff", "seat": seat})


## direction = +1 늘림 / −1 줄임. 자리 0 의 시간 = 고르는 시간, 자리 1 의 시간 = 고민 시간.
func _adjust_time(seat: int, direction: float) -> void:
	if seat == 0:
		var d0 := direction * CheatRules.CHOOSE_BLUFF_SECONDS
		if phase == Phase.PLAYER_CHOOSE:
			turn_limit = maxf(turn_limit + d0, t + CheatRules.MIN_TIME_LEFT)
		else:
			pending_time[0] += d0
	else:
		var d1 := direction * CheatRules.THINK_BLUFF_SECONDS
		if phase == Phase.AI_THINK:
			think_left = maxf(think_left + d1, CheatRules.MIN_TIME_LEFT)
			think_total = maxf(think_total + d1, think_left)
		else:
			pending_time[1] += d1


func _advance_accomplice(dt: float) -> void:
	if acc_state != "walking":
		return
	acc_walk_left -= dt
	if acc_walk_left <= 0.0:
		acc_state = "present"
		GameLog.info("ACCOMPLICE", {"event": "arrived", "t": t})
		_emit({"type": "acc_arrived"})


func _advance_ai_gaze(dt: float) -> void:
	var brain = brains[1]
	# 감시 턴: 반사경을 보다가 사람이 자기 얼굴을 보는 걸 알면 반응 시간 뒤 눈을 돌림
	if phase == Phase.AI_THINK and gaze[1] == "shiner" and gaze[0] == "face":
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
		var want: bool = ai_will_peek and not bool(covered[0])
		seg = brain.cheat_segment(rng, gaze[0] == "face", bool(peek_done[1]), want, str(gaze[1]))
	elif turn_type == TurnType.CHEAT:
		seg = brain.watch_segment(rng, int(strikes[0]), acc_state == "walking" or acc_state == "present")
	else:
		seg = brain.idle_segment(rng)
	_set_gaze(1, str(seg["target"]))
	seg_left[1] = float(seg["dur"])


## 속임수 턴: 자리 0 의 반사경·협력자 읽기와 들킴
func _update_player_reading(dt: float) -> void:
	var on_shiner: bool = gaze[0] == "shiner" and bool(lighter[0])
	var on_acc: bool = gaze[0] == "accomplice" and acc_state == "present"
	if on_shiner or on_acc:
		if float(turn_look[0]) == 0.0:
			stats["peek_tries"][0] += 1
		turn_look[0] += dt
		if gaze[1] == "face" and not _turning(1):
			turn_watched += dt
		var table: Dictionary = CheatRules.HAZARD_SHINER if on_shiner else CheatRules.HAZARD_SIGNAL
		var rate := CheatRules.hazard_rate(table, str(gaze[1]), _turning(1), float(brains[1].perception))
		if rate > 0.0 and rng.randf() < CheatRules.notice_chance(rate, dt):
			var src := "shiner" if on_shiner else "accomplice"
			GameLog.info("NOTICE", {"observer": 1, "source": src, "watch": gaze[1], "rate": rate, "t": t,
				"look_seconds": turn_look[0]})
			stats["accusations"][1] += 1
			stats["hits"][1] += 1
			stats["caught"][0] += 1
			if src == "accomplice":
				stats["acc_caught"][0] += 1
				acc_state = "out"     # 협력자는 그 매치에서 쫓겨남
			else:
				lighter[0] = false    # 라이터 몰수
			_punish(0, 1, src)
			return
	# 협력자가 서 있는데 상대가 뒤를 돌아봄 → 낯선 사람 (경고는 아니고 의심만)
	if acc_state == "present" and not on_acc and gaze[1] == "behind" and not _turning(1) and not stranger_seen:
		stranger_seen = true
		var d: float = brains[1].on_setup_seen("stranger")
		GameLog.info("SUSPECT", {"seat": 1, "by": "stranger", "delta": d, "suspicion": brains[1].suspicion})
		_emit({"type": "stranger_seen"})
	if bool(peek_done[0]):
		return
	peek_progress[0] = CheatRules.peek_step(float(peek_progress[0]), on_shiner and not bool(covered[1]), dt, CheatRules.PEEK_SECONDS)
	signal_progress = CheatRules.peek_step(signal_progress, on_acc, dt, CheatRules.SIGNAL_SECONDS)
	var src2 := ""
	if float(peek_progress[0]) >= 1.0:
		src2 = "shiner"
	elif signal_progress >= 1.0:
		src2 = "accomplice"
	if src2 != "":
		peek_done[0] = true
		peek_source = src2
		stats["peek_done"][0] += 1
		if src2 == "accomplice":
			stats["signal_done"][0] += 1
		GameLog.info("PEEK", {"seat": 0, "event": "done", "source": src2, "t": t, "look_seconds": turn_look[0]})
		_emit({"type": "peek_info", "card": committed[1], "source": src2})


## 감시 턴: 자리 1 의 반사경 읽기 (사람 카드에 덮개가 있으면 안 비침)
func _update_ai_reading(dt: float) -> void:
	var looking: bool = gaze[1] == "shiner" and bool(lighter[1])
	if looking:
		if float(turn_look[1]) == 0.0:
			stats["peek_tries"][1] += 1
		turn_look[1] += dt
		shiner_last[1] = t
		if gaze[0] == "face" and not _turning(0):
			turn_watched += dt
	if bool(peek_done[1]):
		return
	peek_progress[1] = CheatRules.peek_step(float(peek_progress[1]), looking and not bool(covered[0]), dt, float(brains[1].peek_need_seconds()))
	if float(peek_progress[1]) >= 1.0:
		peek_done[1] = true
		stats["peek_done"][1] += 1
		GameLog.info("PEEK", {"seat": 1, "event": "done", "t": t, "look_seconds": turn_look[1]})


func _timeout() -> void:
	stats["timeouts"][0] += 1
	var idx := rng.randi_range(0, hands[0].size() - 1)
	var card: int = hands[0][idx]
	GameLog.warn("TIMEOUT", {"seat": 0, "t": t, "limit": turn_limit, "auto_card": RankCards.CARD_NAMES[card]})
	_emit({"type": "timeout", "card": card})
	commit(card)


func _ai_commit_and_reveal() -> void:
	var info := {}
	if bool(peek_done[1]):
		info["opp_card"] = committed[0]
	committed[1] = brains[1].choose_card(rng, hands[1], sides[1], info)
	GameLog.info("AI_COMMIT", {"seat": 1, "peek_done": peek_done[1], "look_seconds": turn_look[1],
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
		if brain == null or int(sides[1 - seat]) != RankCards.Team.ASSASSIN_SIDE:
			continue   # 상대가 속일 수 있는 진영(노예 측)이었을 때만 결과로 의심
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
	_emit({"type": "turn_summary", "turn_type": turn_type, "look": turn_look.duplicate(), "watched": turn_watched,
		"glances": turn_glances, "peek_done": peek_done.duplicate(), "source": peek_source,
		"covered": covered.duplicate(), "ai_will_peek": ai_will_peek})


## 시뮬레이션 자리 0: 속임수 턴엔 준비 동작 → 상대가 딴 곳을 보면 반사경/협력자, 얼굴 쪽이면 상대 얼굴
func _p0_policy() -> void:
	var b = brains[0]
	if phase == Phase.AI_THINK:
		return
	var give_up: float = minf(SIM_GIVE_UP, turn_limit - 0.5)
	if turn_type == TurnType.CHEAT and p0_will_peek and not bool(peek_done[0]) and t < give_up:
		var react: float = b.p0_reaction(gaze[0] == "face")
		var seen: String = str(gaze[1]) if (t - float(gaze_since[1])) >= react else str(gaze_prev[1])
		if not bool(lighter[0]) and not bool(covered[1]) and seen != "hands" and seen != "face":
			place_lighter()
		if bool(covered[1]) and acc_state == "none" and acc_calls_left > 0 and seen != "face":
			call_accomplice()
		var target := "face"
		if acc_state == "present" and (bool(covered[1]) or not bool(lighter[0])):
			if seen == "own_card" or seen == "away" or seen == "hands":
				target = "accomplice"
		elif bool(lighter[0]) and not bool(covered[1]):
			if seen == "own_card" or seen == "away" or seen == "behind":
				target = "shiner"
		_set_gaze(0, target)
		if int(bluff_left[0]) > 0 and turn_limit - t < 4.0:
			bluff()
		return
	_set_gaze(0, "own_card")
	if turn_type == TurnType.DETECT and bool(lighter[1]) and not bool(covered[0]) and int(cover_left[0]) > 0:
		cover_card()
	var ready: bool = t >= p0_commit_at or bool(peek_done[0]) or t >= give_up
	if ready:
		var info := {}
		if bool(peek_done[0]):
			info["opp_card"] = committed[1]
		var card: int = b.choose_card(rng, hands[0], sides[0], info)
		commit(card)


## 시뮬레이션 자리 0: 감시 턴엔 상대 얼굴을 자주 보고, 반사경 보는 걸 P0_ACCUSE_HOLD 만큼 보면 고발
func _p0_watch(dt: float) -> void:
	var b = brains[0]
	if bool(lighter[1]) and not bool(covered[0]) and int(bluff_left[0]) > 0 and think_left > think_total - 0.1:
		bluff()   # 상대 고민 시간을 줄임
	seg_left[0] -= dt
	if float(seg_left[0]) <= 0.0:
		var seg: Dictionary = b.p0_watch_segment(rng)
		_set_gaze(0, str(seg["target"]))
		seg_left[0] = float(seg["dur"])
	if gaze[0] == "face" and gaze[1] == "shiner" and not _turning(1):
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
