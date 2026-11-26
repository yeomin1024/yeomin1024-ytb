# VERSION: v0.8.0 — 2026-11-26 — 턴 30초 · 제스처 없앰 · 시선 머묾 '!' 표시 · 협력자 = 수상한 행동 2.5초로 부르고 이어폰으로 정보 · 방어는 낸 뒤에만(가리기·섞기·바꿔치기) · 밝혀내기 = 물건 확인/몸 수색, 성공하면 그 턴 무효 · 횟수 제한
# 이전 VERSION: v0.6.0 — 2026-11-26 — 판단 시간(노예가 낸 뒤 왕이 밝혀내기) · why_not() 하나로 행동 가능 여부 (화면 버튼이 같은 규칙을 씀)
# 이전 VERSION: v0.5.0 — 2026-11-26 — 왕 턴 → 노예 턴 · 물건(사전·게임 중) · 시선 고정 엿보기·협력자 · 가능성 불 · 시선 끌기·제스처 · 가리기·무작위·바꿔치기·밝혀내기
#
# 자리(seat): 0 = 사람(시뮬레이션에선 AI), 1 = AI. 판마다 진영이 바뀜 (1·3·5판 자리 0 = 왕 측).
# 한 턴 = 왕 턴(왕이 고름) → 노예 턴(노예가 고름) → 판단 시간 → 공개   (차례마다 TURN_SECONDS 30초)
#   왕 턴  : 왕은 카드만 고름 (방어 못 함). 노예는 협력자 부르기(수상한 행동 2.5초)·물건 놓기·시선 끌기 가능.
#   노예 턴: 노예가 자기 물건을 계속 봐서(1.5초) 반사경으로 엿봄 · 협력자가 연결돼 있으면 3초 뒤 이어폰으로 카드.
#            왕(이미 냄)은 방어: cover(가리기) · play_random(섞기) · fake(바꿔치기) · inspect(물건 확인) · search(몸 수색).
#   판단 시간: 노예가 낸 뒤 왕이 inspect·search (사람 5초 · AI 1.2초).
# '!' 표시(marks): 노예 시선이 물건에 1.5초 머물면 그 물건에 '!' (진짜든 미끼든, 시선 끌기 중엔 안 뜸) — 왕이 보는 공개 정보.
# 협력자 가능성(acc_suspect): 노예가 부르는 동안 왕이 노예 얼굴·손을 보고 있으면 오름 (0~1) — 왕이 보는 공개 정보.
# 밝혀내기 적중: 경고 +1 · 그 속임수 봉인(반사경 물건은 압수) · 노예 다음 노예 턴 −10초 · 그 턴 무효 → 둘 다 다시 고름.
#            헛짚음: 왕의 다음 차례 −10초. 경고 2개 = 즉시 패배.
# 연구·교육용 데모 — 실제 돈과 관계없음.
extends RefCounted

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const GameLog = preload("res://core/game_log.gd")

const ROUNDS := 6
const EXTRA_ROUNDS := 2
const SIM_DT := 0.05
const AUTO_GUARD := 600000

enum Phase { IDLE, KING_TURN, SLAVE_TURN, JUDGE, REVEALED, MATCH_OVER }

var rng := RandomNumberGenerator.new()
var seed_value := 0
var brains: Array = [null, null]
var hands: Array = [[], []]
var sides: Array = [RankCards.Team.KING_SIDE, RankCards.Team.ASSASSIN_SIDE]
var king := 0
var slave := 1
var scores: Array = [0, 0]
var strikes: Array = [0, 0]
var round_index := -1
var turn_in_round := 0
var global_turn := 0
var phase: int = Phase.IDLE
var winner := -1
var end_reason := ""
var t := 0.0                          # 지금 차례 경과 시간
var limit := CheatRules.TURN_SECONDS  # 지금 차례 제한 시간
var committed: Array = [-1, -1]
var shown_card := -1                  # 노예에게 보인 왕 카드 (바꿔치기면 가짜)
var gaze: Array = ["own_card", "own_card"]
var gaze_prev: Array = ["own_card", "own_card"]
var gaze_since: Array = [0.0, 0.0]
var seg_left: Array = [0.0, 0.0]
var objects: Array = [[], []]         # 자리마다 책상 위 물건 (최대 OBJECT_SLOTS)
var checked: Array = [[], []]         # 확인해서 '빈 것'으로 밝혀진 물건 (objects 와 같은 순서)
var marks: Array = []                 # 이번 노예 턴 '!' 가 뜬 노예 물건 (objects[slave] 와 같은 순서)
var covered := false
var randomized := false
var faked := false
var cover_left: Array = [CheatRules.COVERS_PER_MATCH, CheatRules.COVERS_PER_MATCH]
var random_left: Array = [CheatRules.RANDOMS_PER_MATCH, CheatRules.RANDOMS_PER_MATCH]
var fake_left: Array = [CheatRules.FAKES_PER_MATCH, CheatRules.FAKES_PER_MATCH]
var attention_left: Array = [CheatRules.ATTENTION_PER_MATCH, CheatRules.ATTENTION_PER_MATCH]
var place_left: Array = [CheatRules.PLACES_PER_MATCH, CheatRules.PLACES_PER_MATCH]
var inspect_left: Array = [CheatRules.INSPECTS_PER_MATCH, CheatRules.INSPECTS_PER_MATCH]
var search_left: Array = [CheatRules.SEARCHES_PER_MATCH, CheatRules.SEARCHES_PER_MATCH]
var acc_calls_left: Array = [CheatRules.ACC_CALLS_PER_MATCH, CheatRules.ACC_CALLS_PER_MATCH]
var sealed: Array = [{"peek": false, "acc": false}, {"peek": false, "acc": false}]
var calling: Array = [false, false]   # 협력자 부르는 중 (수상한 행동)
var call_progress: Array = [0.0, 0.0]
var acc_connected: Array = [false, false]   # 이어폰 연결 (그 판 동안)
var acc_suspect: Array = [0.0, 0.0]   # 상대가 느낀 협력자 가능성 0~1 (그 판 동안)
var acc_wait := -1.0                  # 이어폰 정보까지 남은 초 (-1 = 기다리지 않음)
var blind_until := -1.0               # 이 시각까지 상대가 노예 시선·행동을 못 봄 (시선 끌기)
var pending_time: Array = [0.0, 0.0]  # 자리마다 다음 자기 차례에 더하거나 뺄 초
var exposed_turn := {"inspect": false, "search": false}
var blocked_sent := false
var info_done := false
var info_source := ""
var info_t := 0.0
var peeked := false                   # 이번 턴 진짜 반사경으로 봄 (턴 끝 리플레이)
var judge_left := 0.0
var judge_limit := 0.0
var plan: Array = [{}, {}]
var round_over := false
var revealed := false
var last_award := {"seat": -1, "points": 0}
var events: Array = []
var stats := {"info_peek": [0, 0], "info_acc": [0, 0], "info_fake": [0, 0], "marks": [0, 0], "baits": [0, 0],
	"inspect": [0, 0], "inspect_hit": [0, 0], "search": [0, 0], "search_hit": [0, 0], "caught": [0, 0], "voids": [0, 0],
	"covers": [0, 0], "randoms": [0, 0], "fakes": [0, 0], "attentions": [0, 0], "acc_calls": [0, 0],
	"acc_connects": [0, 0], "acc_cancels": [0, 0], "objects_placed": [0, 0], "timeouts": [0, 0]}
var _summary_sent := false
var _cursor := 0


func setup(p_seed: int, brain0, brain1) -> void:
	assert(brain1 != null, "자리 1 은 AI 여야 함")
	seed_value = p_seed
	rng.seed = p_seed
	brains = [brain0, brain1]
	for s in 2:
		if brains[s] != null:
			_set_objects_raw(s, brains[s].objects)
	GameLog.info("MATCH", {"event": "setup", "seed": p_seed, "seat0": _brain_name(0), "seat1": _brain_name(1),
		"rounds": ROUNDS, "turn_seconds": CheatRules.TURN_SECONDS, "peek_fix": CheatRules.PEEK_FIX, "call_seconds": CheatRules.ACC_CALL_SECONDS})


## 사전 설정: 시작 전에 책상 위 물건 (최대 OBJECT_SLOTS)
func set_objects(seat: int, kinds: Array) -> Dictionary:
	if phase != Phase.IDLE:
		return _refuse("set_objects", seat, "started")
	_set_objects_raw(seat, kinds)
	GameLog.info("SETUP", {"seat": seat, "objects": ",".join(PackedStringArray(objects[seat]))})
	return {"ok": true}


func start() -> void:
	_begin_round()


func is_over() -> bool:
	return phase == Phase.MATCH_OVER


func pop_events() -> Array:
	var out := events.slice(_cursor)
	_cursor = events.size()
	return out


func actor() -> int:
	return king if phase == Phase.KING_TURN else slave


func time_left() -> float:
	return maxf(limit - t, 0.0)


## 지금 노예가 보고 있는 물건의 머묾 진행 0~1 (게이지 그림용, 물건이 아니면 -1)
func dwell_progress() -> float:
	if phase != Phase.SLAVE_TURN:
		return -1.0
	if _obj_index(slave, str(gaze[slave])) < 0:
		return -1.0
	return clampf((t - float(gaze_since[slave])) / CheatRules.PEEK_FIX, 0.0, 1.0)


## 왕(상대)이 지금 노예 시선을 볼 수 있나 (시선 끌기 중이면 못 봄)
func slave_visible() -> bool:
	return t >= blind_until


## 한 걸음. seat0_gaze = 사람이 지금 보는 곳 (자리 0 이 AI 면 무시)
func tick(dt: float, seat0_gaze: String = "") -> void:
	if phase == Phase.JUDGE:
		_tick_judge(dt, seat0_gaze)
		return
	if not _active():
		return
	t += dt
	if brains[0] == null:
		_set_gaze(0, seat0_gaze if seat0_gaze != "" else "table")
	for s in 2:
		if brains[s] != null:
			_ai_tick(s, dt)
			if not _active():
				return
	_update_calls(dt)
	if phase == Phase.SLAVE_TURN:
		_update_fixation()
		_update_acc_info(dt)
		if not _active():
			return
	if t >= limit:
		_timeout()


# ───────────────────────── 사람(자리 0) 행동 ─────────────────────────

func commit(card: int) -> Dictionary:
	if brains[0] != null or actor() != 0:
		return _refuse("commit", 0, "not_your_turn")
	return commit_by(0, card)


func place_object(kind: String) -> Dictionary:
	return place_object_by(0, kind)


func start_call() -> Dictionary:
	return start_call_by(0)


func stop_call() -> Dictionary:
	return stop_call_by(0)


func attention() -> Dictionary:
	return attention_by(0)


func cover() -> Dictionary:
	var why := why_not(0, "cover")
	if why != "":
		return _refuse("cover", 0, why)
	_cover(0)
	return {"ok": true}


func play_random() -> Dictionary:
	var why := why_not(0, "random")
	if why != "":
		return _refuse("random", 0, why)
	_randomize(0)
	return {"ok": true}


func fake() -> Dictionary:
	var why := why_not(0, "fake")
	if why != "":
		return _refuse("fake", 0, why)
	_fake(0)
	return {"ok": true}


func inspect(obj_index: int) -> Dictionary:
	return _inspect(0, obj_index, "manual")


func search() -> Dictionary:
	return _search(0, "manual")


## 판단 시간을 일찍 끝내고 공개 (사람 왕)
func judge_done() -> Dictionary:
	var why := why_not(0, "judge_done")
	if why != "":
		return _refuse("judge_done", 0, why)
	GameLog.info("JUDGE", {"event": "done_early", "left": judge_left})
	_reveal()
	return {"ok": true}


func next() -> void:
	if phase != Phase.REVEALED:
		_refuse("next", -1, "phase=%d" % phase)
		return
	if round_over:
		_begin_round()
	else:
		_begin_turn(false)


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


## 행동을 지금 할 수 있는지 — "" 이면 가능, 아니면 까닭 코드. 행동 함수와 화면 버튼이 같은 규칙을 씀 (상태를 바꾸지 않음)
## 방어(cover·random·fake)는 왕이 낸 뒤 노예 턴에만, 밝혀내기(inspect·search)는 노예 턴·판단 시간에만.
func why_not(seat: int, action: String, arg: String = "") -> String:
	var defending: bool = seat == king and (phase == Phase.SLAVE_TURN or phase == Phase.JUDGE)
	match action:
		"object":
			if not _active():
				return "not_active"
			if not CheatRules.OBJECTS.has(arg):
				return "unknown=" + arg
			if objects[seat].size() >= CheatRules.OBJECT_SLOTS:
				return "full"
			if int(place_left[seat]) <= 0:
				return "no_uses"
		"call":
			if seat != slave or not _active():
				return "not_slave"
			if bool(sealed[seat]["acc"]):
				return "sealed"
			if bool(calling[seat]):
				return "calling"
			if bool(acc_connected[seat]):
				return "connected"
			if int(acc_calls_left[seat]) <= 0:
				return "no_uses"
		"stop_call":
			if not bool(calling[seat]):
				return "not_calling"
		"attention":
			if seat != slave or not _active():
				return "not_slave"
			if int(attention_left[seat]) <= 0:
				return "no_uses"
		"cover":
			if seat != king:
				return "not_king"
			if phase != Phase.SLAVE_TURN:
				return "after_commit"
			if int(cover_left[seat]) <= 0:
				return "no_uses"
			if covered:
				return "done"
		"random":
			if seat != king:
				return "not_king"
			if phase != Phase.SLAVE_TURN:
				return "after_commit"
			if int(random_left[seat]) <= 0:
				return "no_uses"
			if randomized:
				return "done"
		"fake":
			if seat != king:
				return "not_king"
			if phase != Phase.SLAVE_TURN:
				return "after_commit"
			if int(fake_left[seat]) <= 0:
				return "no_uses"
			if faked:
				return "done"
			if info_done:
				return "already_seen"
		"inspect":
			if not defending:
				return "after_commit" if seat == king else "not_king"
			if bool(exposed_turn["inspect"]):
				return "already_this_turn"
			if int(inspect_left[seat]) <= 0:
				return "no_uses"
			if arg == "":
				if _inspectable().is_empty():
					return "no_target"
			else:
				var idx := int(arg)
				if idx < 0 or idx >= objects[slave].size():
					return "no_target"
				if bool(checked[slave][idx]):
					return "checked"
		"search":
			if not defending:
				return "after_commit" if seat == king else "not_king"
			if bool(exposed_turn["search"]):
				return "already_this_turn"
			if int(search_left[seat]) <= 0:
				return "no_uses"
			if bool(sealed[slave]["acc"]):
				return "sealed"
		"judge_done":
			if seat != king or phase != Phase.JUDGE:
				return "not_judge"
		_:
			return "unknown_action=" + action
	return ""


# ───────────────────────── 자리 공통 행동 ─────────────────────────

func commit_by(seat: int, card: int) -> Dictionary:
	if not _active() or seat != actor() or int(committed[seat]) != -1:
		return _refuse("commit", seat, "not_your_turn")
	if not hands[seat].has(card):
		return _refuse("commit", seat, "card_not_in_hand=%d" % card)
	committed[seat] = card
	GameLog.info("COMMIT", {"seat": seat, "role": "king" if seat == king else "slave", "t": t, "limit": limit,
		"card": RankCards.CARD_NAMES[card], "info": info_source})
	if phase == Phase.KING_TURN:
		_start_phase(Phase.SLAVE_TURN)
	else:
		_start_judge()
	return {"ok": true}


func place_object_by(seat: int, kind: String) -> Dictionary:
	var why := why_not(seat, "object", kind)
	if why != "":
		return _refuse("object", seat, why)
	objects[seat].append(kind)
	checked[seat].append(false)
	if seat == slave and phase == Phase.SLAVE_TURN:
		marks.append(false)
	place_left[seat] -= 1
	stats["objects_placed"][seat] += 1
	var seen := _watched_by_opp(seat)
	var other := 1 - seat
	if seen and brains[other] != null:
		brains[other].on_seen("object")
	GameLog.info("OBJECT", {"seat": seat, "kind": kind, "slot": objects[seat].size() - 1, "seen": seen, "left": place_left[seat]})
	_emit({"type": "object", "seat": seat, "kind": kind, "slot": objects[seat].size() - 1, "seen": seen})
	return {"ok": true, "seen": seen}


## 협력자 부르기 시작 — 수상한 행동(귀를 만지며 신호)을 ACC_CALL_SECONDS 계속해야 연결. 시작하면 1번 씀
func start_call_by(seat: int) -> Dictionary:
	var why := why_not(seat, "call")
	if why != "":
		return _refuse("call", seat, why)
	acc_calls_left[seat] -= 1
	calling[seat] = true
	call_progress[seat] = 0.0
	stats["acc_calls"][seat] += 1
	GameLog.info("CALL", {"seat": seat, "event": "start", "t": t, "left": acc_calls_left[seat]})
	_emit({"type": "call_start", "seat": seat})
	return {"ok": true}


## 중간에 멈춤 — 연결 안 됨 (횟수는 이미 씀)
func stop_call_by(seat: int) -> Dictionary:
	var why := why_not(seat, "stop_call")
	if why != "":
		return {"ok": false, "why": why}   # 손을 뗄 때마다 불리므로 경고 로그는 남기지 않음
	calling[seat] = false
	stats["acc_cancels"][seat] += 1
	GameLog.info("CALL", {"seat": seat, "event": "cancel", "progress": call_progress[seat], "suspect": acc_suspect[seat]})
	_emit({"type": "call_cancel", "seat": seat})
	return {"ok": true}


## 시선 끌기 — 매치 1번: ATTENTION_SECONDS 동안 상대가 노예 시선·행동을 못 봄 (AI 는 딴 곳을 봄)
func attention_by(seat: int) -> Dictionary:
	var why := why_not(seat, "attention")
	if why != "":
		return _refuse("attention", seat, why)
	attention_left[seat] -= 1
	blind_until = t + CheatRules.ATTENTION_SECONDS
	stats["attentions"][seat] += 1
	var other := 1 - seat
	if brains[other] != null:
		_set_gaze(other, "away")
		seg_left[other] = CheatRules.ATTENTION_SECONDS
	GameLog.info("ATTENTION", {"seat": seat, "t": t, "until": blind_until})
	_emit({"type": "attention", "seat": seat, "until": blind_until})
	return {"ok": true}


# ───────────────────────── 내부: 진행 ─────────────────────────

func _active() -> bool:
	return phase == Phase.KING_TURN or phase == Phase.SLAVE_TURN


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
	king = 0 if s0 == RankCards.Team.KING_SIDE else 1
	slave = 1 - king
	hands = [RankCards.new_hand(sides[0]), RankCards.new_hand(sides[1])]
	turn_in_round = 0
	round_over = false
	last_award = {"seat": -1, "points": 0}
	for s in 2:
		acc_connected[s] = false   # 이어폰 연결은 판이 끝나면 끊김
		acc_suspect[s] = 0.0
		calling[s] = false
	GameLog.info("DEAL", {"round": round_index + 1, "king": king, "slave": slave})
	_emit({"type": "round_start", "sides": sides.duplicate(), "king": king})
	_begin_turn(false)


## replay = 밝혀내기 성공으로 같은 턴을 다시 고름 (turn_in_round 그대로)
func _begin_turn(replay: bool) -> void:
	if hands[0].is_empty() or hands[1].is_empty():
		GameLog.warn("TURN", {"problem": "empty_hand"})
		round_over = true
		phase = Phase.REVEALED
		return
	global_turn += 1
	if not replay:
		turn_in_round += 1
	committed = [-1, -1]
	shown_card = -1
	covered = false
	randomized = false
	faked = false
	revealed = false
	info_done = false
	info_source = ""
	peeked = false
	marks = []
	acc_wait = -1.0
	_summary_sent = false
	for s in 2:
		if bool(calling[s]):
			calling[s] = false
			stats["acc_cancels"][s] += 1
	GameLog.info("TURN", {"round": round_index + 1, "turn": turn_in_round, "global_turn": global_turn, "replay": replay})
	_emit({"type": "turn_start", "turn_in_round": turn_in_round, "replay": replay})
	_start_phase(Phase.KING_TURN)


func _start_phase(ph: int) -> void:
	phase = ph
	t = 0.0
	var who := actor()
	limit = maxf(CheatRules.TURN_SECONDS + float(pending_time[who]), CheatRules.MIN_TURN_SECONDS)
	pending_time[who] = 0.0
	gaze_since = [0.0, 0.0]
	seg_left = [0.0, 0.0]
	blind_until = -1.0
	if ph == Phase.SLAVE_TURN:
		marks = []
		for i in objects[slave].size():
			marks.append(false)
		info_done = false
		info_source = ""
		peeked = false
		blocked_sent = false
		exposed_turn = {"inspect": false, "search": false}
		acc_wait = CheatRules.ACC_INFO_DELAY if bool(acc_connected[slave]) and not bool(sealed[slave]["acc"]) else -1.0
	GameLog.info("PHASE", {"phase": "king" if ph == Phase.KING_TURN else "slave", "actor": who, "limit": limit})
	_emit({"type": "phase_start", "phase": ph, "actor": who, "limit": limit})
	for s in 2:
		plan[s] = _make_plan(s, ph) if brains[s] != null else {}


func _make_plan(s: int, ph: int) -> Dictionary:
	var b = brains[s]
	if ph == Phase.KING_TURN:
		if s == king:
			return {"commit_at": float(b.king_think(rng))}
		var want: bool = bool(b.decide_call(rng, int(strikes[s])))
		var after := rng.randf_range(0.5, 4.0)
		var eligible: bool = why_not(s, "call") == ""
		return {"call": want and eligible, "call_after": after, "bold_checked": false, "watched_at": -1.0}
	if s == king:
		var d: Dictionary = b.king_defense(rng, {"opp_objects": objects[slave].size(),
			"opp_acc": bool(acc_connected[slave]) or float(acc_suspect[slave]) > 0.3,
			"random_left": random_left[s], "cover_left": cover_left[s], "fake_left": fake_left[s]})
		var at := rng.randf_range(float(CheatRules.AI_DEFEND_DELAY[0]), float(CheatRules.AI_DEFEND_DELAY[1]))
		return {"defense": d, "defend_at": at, "defended": false}
	return b.slave_plan(rng, {"objects": objects[s], "sealed_peek": sealed[s]["peek"], "covered": covered,
		"randomized": randomized, "strikes": strikes[s], "attention_left": attention_left[s]})


func _ai_tick(s: int, dt: float) -> void:
	var p: Dictionary = plan[s]
	if phase == Phase.KING_TURN:
		if s == king:
			if t >= blind_until:
				_seg_gaze(s, dt, false)
			if t >= minf(float(p.get("commit_at", 3.0)), limit - 0.5):
				_ai_king_commit(s)
			return
		_seg_gaze(s, dt, false)
		_ai_call(s, p)
		return
	# 노예 턴
	if s == king:
		if not bool(p.get("defended", true)) and t >= float(p.get("defend_at", 0.0)):
			p["defended"] = true
			_ai_king_defend(s, p["defense"])
		if t >= blind_until:
			_seg_gaze(s, dt, true)
		return
	_ai_slave_gaze(s, dt)
	if t >= minf(float(p.get("commit_at", 8.0)), limit - 0.3) or (info_done and t >= info_t + 0.5):
		_ai_slave_commit(s)


func _seg_gaze(s: int, dt: float, watching: bool) -> void:
	seg_left[s] -= dt
	if float(seg_left[s]) > 0.0:
		return
	var seg: Dictionary
	if watching:
		seg = brains[s].watch_segment(rng, int(strikes[slave]))
	else:
		seg = brains[s].idle_segment(rng)
	_set_gaze(s, str(seg["target"]))
	seg_left[s] = float(seg["dur"])


## AI 노예 (왕 턴에): 상대가 안 볼 때 부르기 시작 · 부르는 중 상대가 보면 반응 시간 뒤 대담함만큼만 계속
## (반응 시간 동안 협력자 가능성이 조금 오르므로, 멈춰도 '가능성'은 남음 → 몸 수색이 늘 맞지는 않음)
func _ai_call(s: int, p: Dictionary) -> void:
	if not bool(calling[s]):
		if bool(p.get("call", false)) and t >= float(p.get("call_after", 0.0)) and not _watched_by_opp(s):
			p["call"] = false
			start_call_by(s)
		return
	if not _watched_by_opp(s):
		p["watched_at"] = -1.0
		return
	if float(p.get("watched_at", -1.0)) < 0.0:
		p["watched_at"] = t
	if t - float(p["watched_at"]) >= float(brains[s].reaction()) and not bool(p.get("bold_checked", false)):
		p["bold_checked"] = true
		if rng.randf() >= float(brains[s].boldness):
			stop_call_by(s)


## AI 노예 (노예 턴에): 미끼 물건 먼저(있으면) → 반사경 물건 (시선 끌기를 쓰면 그 직전) → 한가한 시선
func _ai_slave_gaze(s: int, dt: float) -> void:
	seg_left[s] -= dt
	if float(seg_left[s]) > 0.0:
		return
	var p: Dictionary = plan[s]
	var b = brains[s]
	var target := ""
	var dur := 0.0
	var peek_obj: int = int(p.get("peek_obj", -1))
	var want_peek: bool = peek_obj >= 0 and peek_obj < objects[s].size() and not info_done and not bool(sealed[s]["peek"]) and not covered and not randomized
	var bait: int = int(p.get("bait_obj", -1))
	if bait >= 0 and bait < objects[s].size():
		target = "obj%d" % bait
		dur = CheatRules.PEEK_FIX + 0.3
		p["bait_obj"] = -1
	elif want_peek:
		if bool(p.get("attention", false)) and why_not(s, "attention") == "":
			p["attention"] = false
			attention_by(s)
		target = "obj%d" % peek_obj
		dur = CheatRules.PEEK_FIX + 0.25
	else:
		var seg: Dictionary = b.idle_segment(rng)
		target = str(seg["target"])
		dur = float(seg["dur"])
	_set_gaze(s, target)
	seg_left[s] = dur


func _ai_king_commit(s: int) -> void:
	var card: int = brains[s].choose_card(rng, hands[s], sides[s], {})
	commit_by(s, card)


func _ai_king_defend(s: int, d: Dictionary) -> void:
	if bool(d["random"]) and why_not(s, "random") == "":
		_randomize(s)
		return
	if bool(d["fake"]) and why_not(s, "fake") == "":
		_fake(s)
	if bool(d["cover"]) and why_not(s, "cover") == "":
		_cover(s)


func _ai_slave_commit(s: int) -> void:
	var info := {}
	if info_done:
		info["opp_card"] = shown_card
	var card: int = brains[s].choose_card(rng, hands[s], sides[s], info)
	commit_by(s, card)


func _timeout() -> void:
	var who := actor()
	stats["timeouts"][who] += 1
	var idx := rng.randi_range(0, hands[who].size() - 1)
	var card: int = hands[who][idx]
	GameLog.warn("TIMEOUT", {"seat": who, "t": t, "limit": limit, "auto_card": RankCards.CARD_NAMES[card]})
	_emit({"type": "timeout", "seat": who, "card": card})
	commit_by(who, card)


## 노예가 냄 → 왕의 판단 시간 (사람 왕 5초 · AI 왕 1.2초 — AI 는 시작할 때 한 번 판단)
func _start_judge() -> void:
	phase = Phase.JUDGE
	judge_limit = CheatRules.JUDGE_SECONDS if brains[king] == null else CheatRules.AI_JUDGE_SECONDS
	judge_left = judge_limit
	if brains[slave] != null:
		_set_gaze(slave, "own_card")
	if brains[king] != null:
		_set_gaze(king, "face")
	GameLog.info("JUDGE", {"event": "start", "king": king, "seconds": judge_limit, "marks": str(marks),
		"acc_suspect": acc_suspect[slave], "peeked": peeked, "acc_connected": acc_connected[slave]})
	_emit({"type": "judge_start", "king": king, "limit": judge_limit})
	if brains[king] != null:
		_ai_judge(king)


## AI 왕 판단: '!' 물건 확인 · 협력자 가능성으로 몸 수색 (공개 정보만)
func _ai_judge(k: int) -> void:
	var kb = brains[k]
	var marked: Array = []
	for i in marks.size():
		if bool(marks[i]) and not bool(checked[slave][i]):
			marked.append(i)
	var idx: int = kb.decide_inspect(rng, marked, _inspectable())
	if idx >= 0 and why_not(k, "inspect", str(idx)) == "":
		_inspect(k, idx, "ai")
		if phase != Phase.JUDGE:
			return
	if bool(kb.decide_search(rng, float(acc_suspect[slave]))) and why_not(k, "search") == "":
		_search(k, "ai")


func _tick_judge(dt: float, seat0_gaze: String) -> void:
	if brains[0] == null:
		_set_gaze(0, seat0_gaze if seat0_gaze != "" else "table")
	judge_left -= dt
	if judge_left <= 0.0:
		GameLog.info("JUDGE", {"event": "time_up"})
		_reveal()


# ───────────────────────── 내부: 방어 (낸 뒤) ─────────────────────────

func _cover(s: int) -> void:
	covered = true
	cover_left[s] -= 1
	stats["covers"][s] += 1
	GameLog.info("COVER", {"seat": s, "t": t, "left": cover_left[s]})
	_emit({"type": "cover", "seat": s})


## 섞기: 낸 카드를 안 보고 패와 섞어 무작위 한 장으로 — 이후 엿보기·협력자 안 통함 (왕도 자기 카드를 모름)
func _randomize(s: int) -> void:
	randomized = true
	random_left[s] -= 1
	stats["randoms"][s] += 1
	var idx := rng.randi_range(0, hands[s].size() - 1)
	committed[s] = int(hands[s][idx])
	GameLog.info("RANDOM", {"seat": s, "t": t, "left": random_left[s]})
	_emit({"type": "random", "seat": s})


func _fake(s: int) -> void:
	faked = true
	fake_left[s] -= 1
	stats["fakes"][s] += 1
	GameLog.info("FAKE", {"seat": s, "t": t, "left": fake_left[s]})
	_emit({"type": "fake", "seat": s})   # 노예에게는 보이지 않음 (UI 가 왕 자리에만 보여 줌)


func _fake_of(card: int) -> int:
	if card == RankCards.Card.CITIZEN:
		return RankCards.special_of(int(sides[king]))
	return RankCards.Card.CITIZEN


## 물건 확인 — 그 물건에 반사경이 있으면 적중 (이번 턴에 썼는지와 관계없이: 장치가 증거)
func _inspect(by: int, idx: int, how: String) -> Dictionary:
	var why := why_not(by, "inspect", str(idx))
	if why != "":
		return _refuse("inspect", by, why)
	exposed_turn["inspect"] = true
	inspect_left[by] -= 1
	stats["inspect"][by] += 1
	var s := slave
	var kind := str(objects[s][idx])
	var hit := CheatRules.is_mirror(kind)
	if hit:
		stats["inspect_hit"][by] += 1
		objects[s].remove_at(idx)   # 압수
		checked[s].remove_at(idx)
		if idx < marks.size():
			marks.remove_at(idx)
		sealed[s]["peek"] = true
	else:
		checked[s][idx] = true
	return _expose_result(by, "inspect", hit, how, {"obj": idx, "obj_kind": kind})


## 몸 수색 — 이어폰(협력자 연결·부르는 중)이 있으면 적중
func _search(by: int, how: String) -> Dictionary:
	var why := why_not(by, "search")
	if why != "":
		return _refuse("search", by, why)
	exposed_turn["search"] = true
	search_left[by] -= 1
	stats["search"][by] += 1
	var s := slave
	var hit: bool = bool(acc_connected[s]) or bool(calling[s])
	if hit:
		stats["search_hit"][by] += 1
		sealed[s]["acc"] = true
		acc_connected[s] = false
		calling[s] = false
	return _expose_result(by, "search", hit, how, {"suspect": acc_suspect[s]})


func _expose_result(by: int, kind: String, hit: bool, how: String, extra: Dictionary) -> Dictionary:
	var s := slave
	if hit:
		strikes[s] += 1
		stats["caught"][s] += 1
		pending_time[s] -= CheatRules.EXPOSE_CUT
	else:
		pending_time[by] -= CheatRules.EXPOSE_FAIL_CUT
	if brains[by] != null:
		brains[by].on_expose_result(hit)
	var ev := {"type": "expose", "by": by, "kind": kind, "hit": hit, "how": how, "strikes": strikes.duplicate(),
		"judge": phase == Phase.JUDGE}
	ev.merge(extra)
	GameLog.info("EXPOSE", {"by": by, "kind": kind, "how": how, "hit": hit, "phase": phase, "t": t, "strikes": strikes[s],
		"slave_pending": pending_time[s], "king_pending": pending_time[by], "extra": str(extra)})
	_emit(ev)
	if hit and int(strikes[s]) >= CheatRules.STRIKES_TO_LOSE:
		_end_match(by, "CAUGHT_TWICE")
	elif hit:
		_void_turn(kind)
	return {"ok": true, "hit": hit}


## 밝혀내기 성공 → 그 턴 무효: 낸 카드는 패로 돌아가고 둘 다 다시 고름
func _void_turn(kind: String) -> void:
	stats["voids"][slave] += 1
	GameLog.info("VOID", {"round": round_index + 1, "turn": turn_in_round, "by": kind})
	_emit({"type": "turn_void", "kind": kind})
	_begin_turn(true)


# ───────────────────────── 내부: 시선·협력자 ─────────────────────────

func _obj_index(seat: int, g: String) -> int:
	if not g.begins_with("obj"):
		return -1
	var idx := int(g.substr(3))
	return idx if idx >= 0 and idx < objects[seat].size() else -1


func _inspectable() -> Array:
	var out: Array = []
	for i in objects[slave].size():
		if not bool(checked[slave][i]):
			out.append(i)
	return out


## seat 를 상대가 지금 주시하나 (얼굴·손을 보고 있고, 고개 돌리는 중이 아니고, 시선 끌기 중이 아님)
func _watched_by_opp(seat: int) -> bool:
	var other := 1 - seat
	return CheatRules.is_watching(str(gaze[other])) and not _turning(other) and t >= blind_until


## 노예 턴: 정보(반사경) · '!' 표시
func _update_fixation() -> void:
	var s := slave
	var k := king
	var idx := _obj_index(s, str(gaze[s]))
	if idx < 0:
		return
	var dur: float = t - float(gaze_since[s])
	var vis: float = t - maxf(float(gaze_since[s]), blind_until)
	var kind := str(objects[s][idx])
	var real: bool = CheatRules.is_mirror(kind) and not bool(sealed[s]["peek"])
	if real and not info_done and dur >= CheatRules.PEEK_FIX:
		if randomized or covered:
			if not blocked_sent:
				blocked_sent = true
				_emit({"type": "info_blocked", "seat": s, "source": "peek", "why": "random" if randomized else "cover"})
		else:
			_give_info("peek")
			peeked = true
	if vis >= CheatRules.PEEK_FIX and idx < marks.size() and not bool(marks[idx]):
		marks[idx] = true
		stats["marks"][s] += 1
		if not CheatRules.is_mirror(kind):
			stats["baits"][s] += 1
		GameLog.info("MARK", {"slave": s, "obj": idx, "kind": kind, "t": t})
		_emit({"type": "mark", "seat": s, "obj": idx})
		if brains[k] != null:
			brains[k].on_seen("mark")


## 이어폰 정보: 노예 턴에 연결돼 있으면 ACC_INFO_DELAY 뒤 (섞기면 막힘, 가리기는 못 막음)
func _update_acc_info(dt: float) -> void:
	if acc_wait < 0.0:
		return
	acc_wait -= dt
	if acc_wait > 0.0:
		return
	acc_wait = -1.0
	if not bool(acc_connected[slave]) or bool(sealed[slave]["acc"]) or info_done:
		return
	if randomized:
		_emit({"type": "info_blocked", "seat": slave, "source": "acc", "why": "random"})
		return
	_give_info("acc")


func _give_info(source: String) -> void:
	info_done = true
	info_source = source
	info_t = t
	shown_card = _fake_of(int(committed[king])) if faked else int(committed[king])
	stats["info_peek" if source == "peek" else "info_acc"][slave] += 1
	if faked:
		stats["info_fake"][slave] += 1
	GameLog.info("INFO", {"seat": slave, "source": source, "shown": RankCards.CARD_NAMES[shown_card], "fake": faked, "t": t})
	_emit({"type": "info", "seat": slave, "source": source, "card": shown_card})


## 부르는 중: 진행 · 상대가 보고 있으면 협력자 가능성 ↑ · 다 되면 연결
func _update_calls(dt: float) -> void:
	for s in 2:
		if not bool(calling[s]):
			continue
		call_progress[s] = float(call_progress[s]) + dt
		var other := 1 - s
		if _watched_by_opp(s):
			var perc: float = float(brains[other].perception) if brains[other] != null else 1.0
			var before := float(acc_suspect[s])
			acc_suspect[s] = minf(before + CheatRules.ACC_SUSPECT_RATE * perc * dt, 1.0)
			if before < 0.5 and float(acc_suspect[s]) >= 0.5:
				if brains[other] != null:
					brains[other].on_seen("call_seen")
				_emit({"type": "call_seen", "seat": s, "suspect": acc_suspect[s]})
		if float(call_progress[s]) >= CheatRules.ACC_CALL_SECONDS:
			calling[s] = false
			acc_connected[s] = true
			stats["acc_connects"][s] += 1
			GameLog.info("CALL", {"seat": s, "event": "connected", "t": t, "suspect": acc_suspect[s]})
			_emit({"type": "acc_connected", "seat": s})
			if phase == Phase.SLAVE_TURN and s == slave and acc_wait < 0.0 and not info_done:
				acc_wait = CheatRules.ACC_INFO_DELAY


func _set_gaze(seat: int, target: String) -> void:
	if gaze[seat] == target:
		return
	gaze_prev[seat] = gaze[seat]
	gaze[seat] = target
	gaze_since[seat] = t
	GameLog.debug("GAZE", {"seat": seat, "from": gaze_prev[seat], "to": target, "t": t})


func _turning(seat: int) -> bool:
	return (t - float(gaze_since[seat])) < CheatRules.TURN_TIME


# ───────────────────────── 내부: 공개·끝 ─────────────────────────

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
	GameLog.info("REVEAL", {"round": round_index + 1, "turn": turn_in_round, "card0": RankCards.CARD_NAMES[c0],
		"card1": RankCards.CARD_NAMES[c1], "result": res, "faked": faked, "info": info_source})
	_emit({"type": "reveal", "cards": [c0, c1], "result": res, "faked": faked, "info": info_source, "shown": shown_card,
		"randomized": randomized})
	if res == 0:
		return
	var w := 0 if res > 0 else 1
	var pts: int = RankCards.WIN_POINTS[sides[w]]
	scores[w] += pts
	last_award = {"seat": w, "points": pts}
	round_over = true
	GameLog.info("ROUND", {"round": round_index + 1, "winner": w, "points": pts, "score0": scores[0], "score1": scores[1]})
	_emit({"type": "round_end", "winner": w, "points": pts, "scores": scores.duplicate()})
	var kb = brains[king]
	if kb != null:
		var delta: float = kb.on_round_result(w != king, sides[slave], turn_in_round)
		GameLog.debug("SUSPECT", {"seat": king, "delta": delta, "suspicion": kb.suspicion})


func _emit_turn_summary() -> void:
	if _summary_sent:
		return
	_summary_sent = true
	_emit({"type": "turn_summary", "marks": marks.duplicate(), "peeked": peeked, "info": info_source, "faked": faked,
		"covered": covered, "randomized": randomized, "slave": slave, "acc_connected": acc_connected[slave],
		"acc_suspect": acc_suspect[slave], "objects": objects[slave].duplicate()})


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


func _set_objects_raw(seat: int, kinds: Array) -> void:
	var out: Array = []
	for k in kinds:
		if CheatRules.OBJECTS.has(str(k)) and out.size() < CheatRules.OBJECT_SLOTS:
			out.append(str(k))
	objects[seat] = out
	var chk: Array = []
	for i in out.size():
		chk.append(false)
	checked[seat] = chk


func _emit(ev: Dictionary) -> void:
	ev["round"] = round_index
	ev["turn"] = global_turn
	events.append(ev)


func _refuse(action: String, seat: int, why: String) -> Dictionary:
	GameLog.warn("REFUSE", {"action": action, "seat": seat, "why": why})
	return {"ok": false, "why": why}


func _brain_name(seat: int) -> String:
	return "human" if brains[seat] == null else str(brains[seat].display_name)
