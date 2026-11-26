# VERSION: v0.5.0 — 2026-11-26 — 왕 턴 → 노예 턴 · 물건(사전·게임 중) · 시선 고정 엿보기·협력자 · 가능성 불 · 시선 끌기·제스처 · 가리기·무작위·바꿔치기·밝혀내기
# 이전 VERSION: v0.4.0 — 2026-11-26 — 준비 동작(라이터 놓기·협력자 부르기) · 반사경 엿보기 · 협력자 신호 · 카드 덮개 · 블러핑(시간)
#
# 자리(seat): 0 = 사람(시뮬레이션에선 AI), 1 = AI. 판마다 진영이 바뀜 (1·3·5판 자리 0 = 왕 측).
# 한 턴 = 왕 턴 → 노예 턴 (각 TURN_SECONDS, 깎이거나 늘 수 있음)
#   왕 턴  : 왕이 카드를 엎어 놓음. 방어 — cover(가리기) · play_random(무작위로 바로 냄) · fake(바꿔치기).
#            노예는 이때 gesture(제스처: 왕 턴이 10초 이상 남았으면 −5초) · call_accomplice · place_object 가능.
#   노예 턴: 노예가 엿보고 카드를 냄. 공격 — 자기 물건(objN)에 시선 1.5초 고정(반사경이면 카드) ·
#            협력자("accomplice")에 1.8초 고정 · attention(시선 끌기, 매치 1번: 3초 동안 왕이 못 봄).
#            왕은 expose(밝혀내기: "peek"/"acc") — 이번 턴에 진짜를 쓴 적이 있으면 적중.
# 가능성 불(lights): 진짜든 미끼든 노예 시선이 1.5초(물건)/1.8초(협력자 자리) 고정되면 왕에게 켜짐 (시선 끌기 중엔 안 켜짐).
# 밝혀내기: 적중 → 노예 경고 +1 · 그 속임수 봉인(매치) · 노예 지금 턴 −5초 / 헛짚음 → 왕의 다음 턴 −5초. 경고 2개 = 즉시 패배.
# 연구·교육용 데모 — 실제 돈과 관계없음.
extends RefCounted

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const GameLog = preload("res://core/game_log.gd")

const ROUNDS := 6
const EXTRA_ROUNDS := 2
const SIM_DT := 0.05
const AUTO_GUARD := 400000

enum Phase { IDLE, KING_TURN, SLAVE_TURN, REVEALED, MATCH_OVER }

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
var t := 0.0                          # 지금 차례(왕 턴·노예 턴) 경과 시간
var limit := CheatRules.TURN_SECONDS  # 지금 차례 제한 시간
var committed: Array = [-1, -1]
var shown_card := -1                  # 노예에게 보인 왕 카드 (바꿔치기면 가짜)
var gaze: Array = ["own_card", "own_card"]
var gaze_prev: Array = ["own_card", "own_card"]
var gaze_since: Array = [0.0, 0.0]
var seg_left: Array = [0.0, 0.0]
var objects: Array = [[], []]         # 자리마다 책상 위 물건 (최대 OBJECT_SLOTS)
var covered := false
var randomized := false
var faked := false
var cover_left: Array = [CheatRules.COVERS_PER_MATCH, CheatRules.COVERS_PER_MATCH]
var random_left: Array = [CheatRules.RANDOMS_PER_MATCH, CheatRules.RANDOMS_PER_MATCH]
var fake_left: Array = [CheatRules.FAKES_PER_MATCH, CheatRules.FAKES_PER_MATCH]
var attention_left: Array = [CheatRules.ATTENTION_PER_MATCH, CheatRules.ATTENTION_PER_MATCH]
var sealed: Array = [{"peek": false, "acc": false}, {"peek": false, "acc": false}]
var acc_state: Array = ["none", "none"]   # 자리마다 자기 협력자 (상대 뒤): none · walking · present · out
var acc_walk_left: Array = [0.0, 0.0]
var acc_calls_left: Array = [CheatRules.ACC_CALLS_PER_MATCH, CheatRules.ACC_CALLS_PER_MATCH]
var blind_until := -1.0               # 이 시각까지 왕이 노예 시선을 못 봄 (시선 끌기)
var gesture_used := false
var king_rushed := false
var pending_time: Array = [0.0, 0.0]  # 자리마다 다음 자기 차례에 더하거나 뺄 초
var lights := {"peek": false, "acc": false}
var tried := {"peek": false, "acc": false}
var exposed_turn := {"peek": false, "acc": false}
var blocked_sent := false
var info_done := false
var info_source := ""
var info_t := 0.0                     # 정보를 얻은 시각
var plan: Array = [{}, {}]
var round_over := false
var revealed := false
var last_award := {"seat": -1, "points": 0}
var events: Array = []
var stats := {"info_peek": [0, 0], "info_acc": [0, 0], "info_fake": [0, 0], "lights": [0, 0], "baits": [0, 0],
	"expose": [0, 0], "expose_hit": [0, 0], "caught": [0, 0], "covers": [0, 0], "randoms": [0, 0], "fakes": [0, 0],
	"attentions": [0, 0], "gestures": [0, 0], "acc_calls": [0, 0], "objects_placed": [0, 0], "timeouts": [0, 0]}
var _summary_sent := false
var _cursor := 0


func setup(p_seed: int, brain0, brain1) -> void:
	assert(brain1 != null, "자리 1 은 AI 여야 함")
	seed_value = p_seed
	rng.seed = p_seed
	brains = [brain0, brain1]
	for s in 2:
		if brains[s] != null:
			objects[s] = _clean_objects(brains[s].objects)
	GameLog.info("MATCH", {"event": "setup", "seed": p_seed, "seat0": _brain_name(0), "seat1": _brain_name(1),
		"rounds": ROUNDS, "peek_fix": CheatRules.PEEK_FIX, "acc_fix": CheatRules.ACC_FIX, "turn_seconds": CheatRules.TURN_SECONDS})


## 사전 설정: 시작 전에 책상 위 물건 (최대 OBJECT_SLOTS)
func set_objects(seat: int, kinds: Array) -> Dictionary:
	if phase != Phase.IDLE:
		return _refuse("set_objects", seat, "started")
	objects[seat] = _clean_objects(kinds)
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


## 한 걸음. seat0_gaze = 사람이 지금 보는 곳 (자리 0 이 AI 면 무시)
func tick(dt: float, seat0_gaze: String = "") -> void:
	if not _active():
		return
	t += dt
	_advance_accomplices(dt)
	if brains[0] == null:
		_set_gaze(0, seat0_gaze if seat0_gaze != "" else "table")
	for s in 2:
		if brains[s] != null:
			_ai_tick(s, dt)
			if not _active():
				return
	if phase == Phase.SLAVE_TURN:
		_update_fixation(dt)
		if not _active():
			return
	if t >= limit:
		_timeout()


# ───────────────────────── 사람(자리 0) 행동 ─────────────────────────

func commit(card: int) -> Dictionary:
	if brains[0] != null or actor() != 0:
		return _refuse("commit", 0, "not_your_turn")
	return commit_by(0, card)


## 물건 놓기 — 게임 중 언제든 (빈자리)
func place_object(kind: String) -> Dictionary:
	return place_object_by(0, kind)


func call_accomplice() -> Dictionary:
	return call_accomplice_by(0)


func attention() -> Dictionary:
	return attention_by(0)


func gesture() -> Dictionary:
	return gesture_by(0)


func cover() -> Dictionary:
	if king != 0:
		return _refuse("cover", 0, "not_king")
	if not _active() or covered or int(cover_left[0]) <= 0:
		return _refuse("cover", 0, "unavailable")
	_cover(0)
	return {"ok": true}


func play_random() -> Dictionary:
	if king != 0 or phase != Phase.KING_TURN:
		return _refuse("random", 0, "not_king_turn")
	if int(random_left[0]) <= 0:
		return _refuse("random", 0, "no_uses")
	_randomize(0)
	return {"ok": true}


func fake() -> Dictionary:
	if king != 0:
		return _refuse("fake", 0, "not_king")
	if not _active() or faked or info_done or int(fake_left[0]) <= 0:
		return _refuse("fake", 0, "unavailable")
	_fake(0)
	return {"ok": true}


func expose(kind: String) -> Dictionary:
	if king != 0:
		return _refuse("expose", 0, "not_king")
	return _expose(0, kind, "manual")


func next() -> void:
	if phase != Phase.REVEALED:
		_refuse("next", -1, "phase=%d" % phase)
		return
	if round_over:
		_begin_round()
	else:
		_begin_turn()


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


# ───────────────────────── 자리 공통 행동 ─────────────────────────

func commit_by(seat: int, card: int) -> Dictionary:
	if not _active() or seat != actor():
		return _refuse("commit", seat, "not_your_turn")
	if not hands[seat].has(card):
		return _refuse("commit", seat, "card_not_in_hand=%d" % card)
	committed[seat] = card
	GameLog.info("COMMIT", {"seat": seat, "role": "king" if seat == king else "slave", "t": t, "limit": limit,
		"card": RankCards.CARD_NAMES[card], "info": info_source})
	if phase == Phase.KING_TURN:
		_start_phase(Phase.SLAVE_TURN)
	else:
		_reveal()
	return {"ok": true}


func place_object_by(seat: int, kind: String) -> Dictionary:
	if not _active():
		return _refuse("object", seat, "not_active")
	if not CheatRules.OBJECTS.has(kind):
		return _refuse("object", seat, "unknown=" + kind)
	if objects[seat].size() >= CheatRules.OBJECT_SLOTS:
		return _refuse("object", seat, "full")
	objects[seat].append(kind)
	stats["objects_placed"][seat] += 1
	var other := 1 - seat
	var seen: bool = (gaze[other] == "hands" or gaze[other] == "face") and not _turning(other)
	if seen and brains[other] != null:
		brains[other].on_seen("object")
	GameLog.info("OBJECT", {"seat": seat, "kind": kind, "slot": objects[seat].size() - 1, "seen": seen})
	_emit({"type": "object", "seat": seat, "kind": kind, "slot": objects[seat].size() - 1, "seen": seen})
	return {"ok": true, "seen": seen}


func call_accomplice_by(seat: int) -> Dictionary:
	if seat != slave or not _active():
		return _refuse("accomplice", seat, "not_slave")
	if acc_state[seat] != "none" or int(acc_calls_left[seat]) <= 0 or bool(sealed[seat]["acc"]):
		return _refuse("accomplice", seat, "unavailable")
	acc_calls_left[seat] -= 1
	acc_state[seat] = "walking"
	acc_walk_left[seat] = CheatRules.ACC_WALK_SECONDS
	stats["acc_calls"][seat] += 1
	GameLog.info("ACCOMPLICE", {"seat": seat, "event": "called", "t": t})
	_emit({"type": "acc_called", "seat": seat})
	return {"ok": true}


## 시선 끌기 — 노예 턴, 매치 1번: ATTENTION_SECONDS 동안 왕이 노예 시선을 못 봄 (AI 왕은 딴 곳을 봄)
func attention_by(seat: int) -> Dictionary:
	if seat != slave or phase != Phase.SLAVE_TURN:
		return _refuse("attention", seat, "not_slave_turn")
	if int(attention_left[seat]) <= 0:
		return _refuse("attention", seat, "no_uses")
	attention_left[seat] -= 1
	blind_until = t + CheatRules.ATTENTION_SECONDS
	stats["attentions"][seat] += 1
	if brains[king] != null:
		_set_gaze(king, "away")
		seg_left[king] = 0.0
	GameLog.info("ATTENTION", {"seat": seat, "t": t, "until": blind_until})
	_emit({"type": "attention", "seat": seat, "until": blind_until})
	return {"ok": true}


## 제스처 — 왕 턴에 노예가: 왕 턴이 10초 이상 남았으면 −5초 (왕 턴마다 1번)
func gesture_by(seat: int) -> Dictionary:
	if seat != slave or phase != Phase.KING_TURN:
		return _refuse("gesture", seat, "not_king_turn")
	if gesture_used:
		return _refuse("gesture", seat, "used")
	if limit - t < CheatRules.GESTURE_MIN_LEFT:
		return _refuse("gesture", seat, "under_10s")
	gesture_used = true
	limit -= CheatRules.GESTURE_CUT
	king_rushed = true
	stats["gestures"][seat] += 1
	GameLog.info("GESTURE", {"seat": seat, "t": t, "king_limit": limit})
	_emit({"type": "gesture", "seat": seat, "limit": limit})
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
		if acc_state[s] == "walking" or acc_state[s] == "present":
			acc_state[s] = "none"   # 협력자는 판이 끝나면 돌아감 (쫓겨났으면 그대로)
	GameLog.info("DEAL", {"round": round_index + 1, "king": king, "slave": slave})
	_emit({"type": "round_start", "sides": sides.duplicate(), "king": king})
	_begin_turn()


func _begin_turn() -> void:
	if hands[0].is_empty() or hands[1].is_empty():
		GameLog.warn("TURN", {"problem": "empty_hand"})
		round_over = true
		phase = Phase.REVEALED
		return
	global_turn += 1
	turn_in_round += 1
	committed = [-1, -1]
	shown_card = -1
	covered = false
	randomized = false
	faked = false
	revealed = false
	_summary_sent = false
	GameLog.info("TURN", {"round": round_index + 1, "turn": turn_in_round, "global_turn": global_turn})
	_emit({"type": "turn_start", "turn_in_round": turn_in_round})
	_start_phase(Phase.KING_TURN)


func _start_phase(ph: int) -> void:
	phase = ph
	t = 0.0
	var who := actor()
	limit = maxf(CheatRules.TURN_SECONDS + float(pending_time[who]), 3.0)
	pending_time[who] = 0.0
	gaze_since = [0.0, 0.0]
	seg_left = [0.0, 0.0]
	blind_until = -1.0
	gesture_used = false
	king_rushed = false
	if ph == Phase.SLAVE_TURN:
		lights = {"peek": false, "acc": false}
		tried = {"peek": false, "acc": false}
		exposed_turn = {"peek": false, "acc": false}
		blocked_sent = false
		info_done = false
		info_source = ""
	GameLog.info("PHASE", {"phase": "king" if ph == Phase.KING_TURN else "slave", "actor": who, "limit": limit})
	_emit({"type": "phase_start", "phase": ph, "actor": who, "limit": limit})
	for s in 2:
		plan[s] = _make_plan(s, ph) if brains[s] != null else {}


func _make_plan(s: int, ph: int) -> Dictionary:
	var b = brains[s]
	if ph == Phase.KING_TURN:
		if s == king:
			return {"commit_at": float(b.king_think(rng))}
		var p := {"call_acc": false, "call_at": 0.0, "gesture": false, "gesture_at": 0.0}
		if turn_in_round == 1 and acc_state[s] == "none" and int(acc_calls_left[s]) > 0 and not bool(sealed[s]["acc"]):
			p["call_acc"] = bool(b.decide_call(rng))
			p["call_at"] = rng.randf_range(0.3, 1.5)
		p["gesture"] = bool(b.decide_gesture(rng))
		p["gesture_at"] = rng.randf_range(0.5, 4.0)
		return p
	if s == king:
		return {}
	return b.slave_plan(rng, {"objects": objects[s], "sealed_peek": sealed[s]["peek"], "sealed_acc": sealed[s]["acc"],
		"covered": covered, "randomized": randomized, "acc_present": acc_state[s] == "walking" or acc_state[s] == "present",
		"strikes": strikes[s], "attention_left": attention_left[s]})


func _ai_tick(s: int, dt: float) -> void:
	var p: Dictionary = plan[s]
	if phase == Phase.KING_TURN:
		_seg_gaze(s, dt, false)
		if s == king:
			if t >= minf(float(p.get("commit_at", 2.0)), limit - 0.5):
				_ai_king_commit(s)
			return
		if bool(p.get("call_acc", false)) and t >= float(p.get("call_at", 0.0)):
			p["call_acc"] = false
			call_accomplice_by(s)
		if bool(p.get("gesture", false)) and t >= float(p.get("gesture_at", 0.0)):
			p["gesture"] = false
			gesture_by(s)
		return
	# 노예 턴
	if s == king:
		if t < blind_until:
			return   # 시선 끌기에 딴 곳을 보는 중
		_seg_gaze(s, dt, true)
		return
	_ai_slave_gaze(s, dt)
	if t >= minf(float(p.get("commit_at", 5.0)), limit - 0.3) or (info_done and t >= info_t + 0.4):
		_ai_slave_commit(s)


func _seg_gaze(s: int, dt: float, watching: bool) -> void:
	seg_left[s] -= dt
	if float(seg_left[s]) > 0.0:
		return
	var seg: Dictionary
	if watching:
		seg = brains[s].watch_segment(rng, int(strikes[slave]), acc_state[slave] == "walking" or acc_state[slave] == "present")
	else:
		seg = brains[s].idle_segment(rng)
	_set_gaze(s, str(seg["target"]))
	seg_left[s] = float(seg["dur"])


## AI 노예: 진짜 물건·협력자를 '계속' 봄. 왕이 쳐다보면 반응 시간 뒤 눈을 돌리거나 시선 끌기
func _ai_slave_gaze(s: int, dt: float) -> void:
	var b = brains[s]
	var p: Dictionary = plan[s]
	var watched: bool = gaze[king] == "face" and t >= blind_until and not _turning(king)
	var cur := str(gaze[s])
	if (cur.begins_with("obj") or cur == "accomplice") and watched and not info_done:
		var since: float = maxf(float(gaze_since[king]), float(gaze_since[s]))
		if t - since >= float(b.reaction()):
			if bool(p.get("attention", false)) and int(attention_left[s]) > 0:
				p["attention"] = false
				attention_by(s)
			else:
				_set_gaze(s, "face")
				seg_left[s] = rng.randf_range(0.4, 0.9)
				return
	seg_left[s] -= dt
	if float(seg_left[s]) > 0.0:
		return
	var target := ""
	var dur := 0.0
	var want_peek: bool = int(p.get("peek_obj", -1)) >= 0 and not info_done and not bool(sealed[s]["peek"]) and not covered and not randomized
	var want_acc: bool = bool(p.get("acc", false)) and acc_state[s] == "present" and not info_done and not bool(sealed[s]["acc"]) and not randomized
	var bait: int = int(p.get("bait_obj", -1))
	if want_peek and (not watched or rng.randf() < float(b.boldness)):
		target = "obj%d" % int(p["peek_obj"])
		dur = CheatRules.PEEK_FIX + 0.25
	elif want_acc and (not watched or rng.randf() < float(b.boldness)):
		target = "accomplice"
		dur = CheatRules.ACC_FIX + 0.25
	elif bait >= 0 and not bool(lights["peek"]):
		target = "obj%d" % bait
		dur = CheatRules.PEEK_FIX + 0.3
		p["bait_obj"] = -1
	else:
		var seg: Dictionary = b.idle_segment(rng)
		target = str(seg["target"])
		dur = float(seg["dur"])
	_set_gaze(s, target)
	seg_left[s] = dur


func _ai_king_commit(s: int) -> void:
	var d: Dictionary = brains[s].king_defense(rng, {"rushed": king_rushed, "opp_objects": objects[slave].size(),
		"opp_acc": acc_state[slave] == "walking" or acc_state[slave] == "present",
		"random_left": random_left[s], "cover_left": cover_left[s], "fake_left": fake_left[s]})
	if bool(d["random"]):
		_randomize(s)
		return
	var card: int = brains[s].choose_card(rng, hands[s], sides[s], {})
	if bool(d["fake"]):
		_fake(s)
	if bool(d["cover"]):
		_cover(s)
	commit_by(s, card)


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


# ───────────────────────── 내부: 방어 ─────────────────────────

func _cover(s: int) -> void:
	covered = true
	cover_left[s] -= 1
	stats["covers"][s] += 1
	GameLog.info("COVER", {"seat": s, "t": t, "left": cover_left[s]})
	_emit({"type": "cover", "seat": s})


func _randomize(s: int) -> void:
	randomized = true
	random_left[s] -= 1
	stats["randoms"][s] += 1
	var idx := rng.randi_range(0, hands[s].size() - 1)
	var card: int = hands[s][idx]
	GameLog.info("RANDOM", {"seat": s, "t": t, "left": random_left[s]})
	_emit({"type": "random", "seat": s})
	commit_by(s, card)


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


## 밝혀내기: 이번 노예 턴에 그 속임수를 진짜로 썼으면 적중
func _expose(by: int, kind: String, how: String) -> Dictionary:
	if phase != Phase.SLAVE_TURN or by != king:
		return _refuse("expose", by, "not_king_slave_turn")
	if kind != "peek" and kind != "acc":
		return _refuse("expose", by, "kind=" + kind)
	if bool(exposed_turn[kind]):
		return _refuse("expose", by, "already_this_turn")
	exposed_turn[kind] = true
	var s := slave
	stats["expose"][by] += 1
	var hit: bool = bool(tried[kind]) or _live_real(kind)
	if hit:
		stats["expose_hit"][by] += 1
		stats["caught"][s] += 1
		strikes[s] += 1
		sealed[s][kind] = true
		if kind == "acc":
			acc_state[s] = "out"
		limit = maxf(limit - CheatRules.EXPOSE_CUT, t + CheatRules.MIN_TIME_LEFT)
	else:
		pending_time[by] -= CheatRules.EXPOSE_FAIL_CUT
	if brains[by] != null:
		brains[by].on_expose_result(hit)
	GameLog.info("EXPOSE", {"by": by, "kind": kind, "how": how, "hit": hit, "t": t, "strikes": strikes[s],
		"slave_limit": limit, "king_pending": pending_time[by]})
	_emit({"type": "expose", "by": by, "kind": kind, "hit": hit, "how": how, "strikes": strikes.duplicate()})
	if hit and int(strikes[s]) >= CheatRules.STRIKES_TO_LOSE:
		_end_match(by, "CAUGHT_TWICE")
	return {"ok": true, "hit": hit}


func _live_real(kind: String) -> bool:
	var g := str(gaze[slave])
	if t - float(gaze_since[slave]) < CheatRules.EXPOSE_LIVE:
		return false
	if kind == "peek":
		var idx := _obj_index(slave, g)
		return idx >= 0 and CheatRules.is_mirror(str(objects[slave][idx])) and not bool(sealed[slave]["peek"])
	return g == "accomplice" and acc_state[slave] == "present"


# ───────────────────────── 내부: 시선 고정 ─────────────────────────

func _obj_index(seat: int, g: String) -> int:
	if not g.begins_with("obj"):
		return -1
	var idx := int(g.substr(3))
	return idx if idx >= 0 and idx < objects[seat].size() else -1


## 노예 턴: 시도 표시 · 가능성 불 · 정보 · AI 왕의 현장 밝혀내기
func _update_fixation(dt: float) -> void:
	var s := slave
	var k := king
	var g := str(gaze[s])
	var idx := _obj_index(s, g)
	var is_obj: bool = idx >= 0
	var is_acc: bool = g == "accomplice"
	if not is_obj and not is_acc:
		return
	var kind := "peek" if is_obj else "acc"
	var dur: float = t - float(gaze_since[s])
	var vis: float = t - maxf(float(gaze_since[s]), blind_until)
	var real: bool = CheatRules.is_mirror(str(objects[s][idx])) if is_obj else acc_state[s] == "present"
	var need: float = CheatRules.PEEK_FIX if is_obj else CheatRules.ACC_FIX
	var is_sealed: bool = bool(sealed[s][kind])
	if real and not is_sealed and dur >= CheatRules.TRY_MARK:
		tried[kind] = true
	# 정보 — 진짜 장치를 끝까지 봄 (불·밝혀내기보다 먼저: 끝까지 봤으면 카드는 얻음, 들키면 경고·봉인)
	if real and not is_sealed and not info_done and dur >= need:
		var why := ""
		if randomized:
			why = "random"
		elif kind == "peek" and covered:
			why = "cover"
		if why != "":
			if not blocked_sent:
				blocked_sent = true
				_emit({"type": "info_blocked", "seat": s, "kind": kind, "why": why})
		else:
			info_done = true
			info_source = kind
			info_t = t
			shown_card = _fake_of(int(committed[k])) if faked else int(committed[k])
			stats["info_peek" if kind == "peek" else "info_acc"][s] += 1
			if faked:
				stats["info_fake"][s] += 1
			GameLog.info("INFO", {"seat": s, "source": kind, "shown": RankCards.CARD_NAMES[shown_card], "fake": faked, "t": t})
			_emit({"type": "info", "seat": s, "source": kind, "card": shown_card})
	# 가능성 불 — 진짜든 미끼든 (시선 끌기 중엔 안 보임) → 왕은 불을 보고 밝혀낼 수 있음
	if vis >= need and not bool(lights[kind]):
		lights[kind] = true
		stats["lights"][s] += 1
		if not real:
			stats["baits"][s] += 1
		GameLog.info("LIGHT", {"kind": kind, "slave": s, "real": real, "t": t})
		_emit({"type": "light", "kind": kind, "seat": s})
		var kb = brains[k]
		if kb != null:
			kb.on_seen("light")
			if not is_sealed and not bool(exposed_turn[kind]) and bool(kb.decide_expose_on_light(rng)):
				_expose(k, kind, "light")
				if phase != Phase.SLAVE_TURN:
					return
	is_sealed = bool(sealed[s][kind])
	# AI 왕: 진행 중인 고정을 보고 현장 밝혀내기 (미끼인지 모름)
	var kb2 = brains[k]
	if kb2 != null and vis > 0.0 and not is_sealed and not bool(exposed_turn[kind]):
		var table: Dictionary = CheatRules.HAZARD_EXPOSE_OBJ if is_obj else CheatRules.HAZARD_EXPOSE_ACC
		var rate := CheatRules.hazard_rate(table, str(gaze[k]), _turning(k), float(kb2.perception))
		if rate > 0.0 and rng.randf() < CheatRules.notice_chance(rate, dt):
			_expose(k, kind, "watch")


func _advance_accomplices(dt: float) -> void:
	for s in 2:
		if acc_state[s] != "walking":
			continue
		acc_walk_left[s] -= dt
		if float(acc_walk_left[s]) <= 0.0:
			acc_state[s] = "present"
			GameLog.info("ACCOMPLICE", {"seat": s, "event": "arrived", "t": t})
			_emit({"type": "acc_arrived", "seat": s})


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
	_emit({"type": "reveal", "cards": [c0, c1], "result": res, "faked": faked, "info": info_source, "shown": shown_card})
	if res == 0:
		return
	var w := 0 if res > 0 else 1
	var pts: int = RankCards.WIN_POINTS[sides[w]]
	scores[w] += pts
	last_award = {"seat": w, "points": pts}
	round_over = true
	GameLog.info("ROUND", {"round": round_index + 1, "winner": w, "points": pts, "score0": scores[0], "score1": scores[1]})
	_emit({"type": "round_end", "winner": w, "points": pts, "scores": scores.duplicate()})
	for seat in [1, 0]:
		var brain = brains[seat]
		if brain == null or int(seat) != king:
			continue   # 왕 측이 노예의 결과로 의심
		var delta: float = brain.on_round_result(w != seat, sides[slave], turn_in_round)
		GameLog.debug("SUSPECT", {"seat": seat, "delta": delta, "suspicion": brain.suspicion})


func _emit_turn_summary() -> void:
	if _summary_sent:
		return
	_summary_sent = true
	_emit({"type": "turn_summary", "lights": lights.duplicate(), "tried": tried.duplicate(), "info": info_source,
		"faked": faked, "covered": covered, "randomized": randomized, "slave": slave})


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


func _clean_objects(kinds: Array) -> Array:
	var out: Array = []
	for k in kinds:
		if CheatRules.OBJECTS.has(str(k)) and out.size() < CheatRules.OBJECT_SLOTS:
			out.append(str(k))
	return out


func _emit(ev: Dictionary) -> void:
	ev["round"] = round_index
	ev["turn"] = global_turn
	events.append(ev)


func _refuse(action: String, seat: int, why: String) -> Dictionary:
	GameLog.warn("REFUSE", {"action": action, "seat": seat, "why": why})
	return {"ok": false, "why": why}


func _brain_name(seat: int) -> String:
	return "human" if brains[seat] == null else str(brains[seat].display_name)
