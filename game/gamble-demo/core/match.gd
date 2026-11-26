# VERSION: v0.1.0 — 2026-11-26 — 매치 흐름(판·턴·공개·연장) + 속임수·고발 판정 + 이벤트 기록
#
# 자리(seat): 0 = 먼저 카드를 내는 쪽 (사람, 또는 시뮬레이션에선 AI)
#             1 = AI. 정보 없이 카드를 미리 정해 두고, 엿보기를 했을 때만 자리 0 카드를 보고 다시 정함
# 흐름: start() → [CHOOSE: cheat() · accuse() · commit()] → [REVEALED: accuse() · next()] → … → MATCH_OVER
# 판정 규칙:
#   - 들킴은 자동이 아님. 상대가 accuse() 를 해야 하고, 그 순간 증거가 남아 있어야 적중.
#   - 적중: 경고 +1 · 그 사람 증거 몰수 · 이번 판 몰수(고발한 쪽이 자기 진영 점수) · 벌금 CAUGHT_FINE · 경고 2개면 즉시 패배
#   - 헛고발: 고발 토큰 −1 · 벌금(점수)을 상대에게
# 이벤트: events 배열 (UI 는 pop_events() 로 읽음). 자리 1 의 "cheat" 이벤트는 정답이라
#         UI 가 바로 보여 주지 않고 판 끝 리플레이에만 쓴다.
# 연구·교육용 데모 — 실제 돈과 관계없음.
extends RefCounted

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const GameLog = preload("res://core/game_log.gd")

const ROUNDS := 6
const EXTRA_ROUNDS := 2              # 6판 뒤 동점이면 연장 (최대 2판)
const HUMAN_PERCEPTION := 1.0
const FACE_CUE_IF_SPECIAL := 0.6    # AI 가 특수 카드를 골랐을 때 표정이 굳을 확률
const FACE_CUE_IF_CITIZEN := 0.25   # 시민인데도 굳는(허세) 확률
const AUTO_GUARD := 1000            # run_auto 무한 반복 막기

enum Phase { IDLE, CHOOSE, REVEALED, MATCH_OVER }

var rng := RandomNumberGenerator.new()
var seed_value := 0
var brains: Array = [null, null]
var gaze: Array = ["face", "face"]
var hands: Array = [[], []]
var sides: Array = [RankCards.Side.KING_SIDE, RankCards.Side.ASSASSIN_SIDE]
var scores: Array = [0, 0]
var strikes: Array = [0, 0]
var tokens: Array = [CheatRules.TOKENS_PER_MATCH, CheatRules.TOKENS_PER_MATCH]
var uses: Array = [{}, {}]
var evidence: Array = []            # {"owner": 자리, "cheat": id, "expires": global_turn}
var marked: Array = [false, false]  # 자리 i 가 상대 특수 카드 뒷면에 표시를 해 둠
var peeked_now: Array = [false, false]
var round_index := -1
var turn_in_round := 0
var global_turn := 0
var phase: int = Phase.IDLE
var winner := -1                    # -1 진행 중 · 0/1 자리 · 2 무승부
var end_reason := ""
var tentative_ai_card := -1         # 자리 1 이 정보 없이 정해 둔 카드
var ai_late_peek := false           # 자리 1 이 이번 턴 엿봄 → 자리 0 이 낸 뒤 다시 정함
var mark_seen := false              # 이번 턴 자리 0 이 뒷면 표시를 읽었나
var round_over := false
var last_award := {"seat": -1, "points": 0}
var events: Array = []
var stats := {"cheats": [0, 0], "fakes": [0, 0], "accusations": [0, 0], "hits": [0, 0]}
var _cursor := 0


func setup(p_seed: int, brain0, brain1) -> void:
	assert(brain1 != null, "자리 1 은 AI 여야 함")
	seed_value = p_seed
	rng.seed = p_seed
	brains = [brain0, brain1]
	GameLog.info("MATCH", {"event": "setup", "seed": p_seed, "seat0": _brain_name(0), "seat1": _brain_name(1),
		"rounds": ROUNDS, "strikes_to_lose": CheatRules.STRIKES_TO_LOSE, "tokens": CheatRules.TOKENS_PER_MATCH})


func start() -> void:
	_begin_round()


func is_over() -> bool:
	return phase == Phase.MATCH_OVER


func pop_events() -> Array:
	var out := events.slice(_cursor)
	_cursor = events.size()
	return out


func uses_left(seat: int) -> Dictionary:
	var left := {}
	for id in CheatRules.CHEATS:
		left[id] = int(CheatRules.CHEATS[id]["uses"]) - int(uses[seat].get(id, 0))
	return left


## 자리 0 (사람) 또는 시험 코드가 부름
func cheat(seat: int, kind: String, qte: float) -> Dictionary:
	if phase != Phase.CHOOSE:
		return _refuse("cheat", seat, "phase=%d" % phase)
	if not CheatRules.CHEATS.has(kind):
		return _refuse("cheat", seat, "unknown=" + kind)
	if int(uses_left(seat)[kind]) <= 0:
		return _refuse("cheat", seat, "no_uses=" + kind)
	if kind == "mark" and marked[seat]:
		return _refuse("cheat", seat, "already_marked")
	if kind == "peek" and peeked_now[seat]:
		return _refuse("cheat", seat, "already_peeked")
	_do_cheat(seat, kind, qte)
	return {"ok": true}


func accuse(accuser: int) -> Dictionary:
	if phase != Phase.CHOOSE and phase != Phase.REVEALED:
		return _refuse("accuse", accuser, "phase=%d" % phase)
	if int(tokens[accuser]) <= 0:
		return _refuse("accuse", accuser, "no_token")
	var accused := 1 - accuser
	stats["accusations"][accuser] += 1
	var found: Array = []
	for e in evidence:
		if int(e["owner"]) == accused and int(e["expires"]) >= global_turn:
			found.append(e["cheat"])
	var hit := not found.is_empty()
	if hit:
		stats["hits"][accuser] += 1
		strikes[accused] += 1
		# 증거 몰수 — 같은 증거로 두 번 경고하지 않음
		var kept: Array = []
		for e in evidence:
			if int(e["owner"]) != accused:
				kept.append(e)
		evidence = kept
		if found.has("mark"):
			marked[accused] = false
		if accused == 1:
			ai_late_peek = false
		scores[accused] -= CheatRules.CAUGHT_FINE
		scores[accuser] += CheatRules.CAUGHT_FINE
	else:
		tokens[accuser] -= 1
		scores[accuser] -= CheatRules.FALSE_ACCUSE_FINE
		scores[accused] += CheatRules.FALSE_ACCUSE_FINE
	if brains[accuser] != null:
		brains[accuser].on_accuse_result(hit)
	GameLog.info("ACCUSE", {"accuser": accuser, "accused": accused, "hit": hit,
		"found": ",".join(PackedStringArray(found)), "strikes": strikes[accused],
		"tokens_left": tokens[accuser], "score0": scores[0], "score1": scores[1]})
	_emit({"type": "accuse", "accuser": accuser, "hit": hit, "found": found.duplicate(),
		"strikes": strikes.duplicate(), "tokens": tokens.duplicate(), "scores": scores.duplicate()})
	if hit:
		_forfeit_round(accuser)
		if int(strikes[accused]) >= CheatRules.STRIKES_TO_LOSE:
			_end_match(accuser, "CAUGHT_TWICE")
	return {"ok": true, "hit": hit, "found": found}


## 자리 0 이 카드를 냄 → 자리 1 카드 확정 → 공개
func commit(card0: int) -> Dictionary:
	if phase != Phase.CHOOSE:
		return _refuse("commit", 0, "phase=%d" % phase)
	if not hands[0].has(card0):
		return _refuse("commit", 0, "card_not_in_hand=%d" % card0)
	var card1 := tentative_ai_card
	if ai_late_peek:
		card1 = brains[1].choose_card(rng, hands[1], sides[1], {"opp_card": card0})
		GameLog.info("AI_LATE", {"seen": RankCards.CARD_NAMES[card0],
			"tentative": RankCards.CARD_NAMES[tentative_ai_card], "final": RankCards.CARD_NAMES[card1]})
	if not hands[1].has(card1):
		GameLog.warn("REVEAL", {"problem": "ai_card_not_in_hand", "card": card1})
		card1 = int(hands[1][0])
	hands[0].erase(card0)
	hands[1].erase(card1)
	var res := RankCards.resolve(card0, card1)
	phase = Phase.REVEALED
	GameLog.info("REVEAL", {"round": round_index + 1, "turn": turn_in_round,
		"card0": RankCards.CARD_NAMES[card0], "card1": RankCards.CARD_NAMES[card1], "result": res})
	_emit({"type": "reveal", "cards": [card0, card1], "result": res})
	if res == 0:
		return {"ok": true, "result": 0}
	var w := 0 if res > 0 else 1
	var pts: int = RankCards.WIN_POINTS[sides[w]]
	scores[w] += pts
	last_award = {"seat": w, "points": pts}
	round_over = true
	GameLog.info("ROUND", {"round": round_index + 1, "winner": w, "points": pts, "by": "cards",
		"decided_turn": turn_in_round, "score0": scores[0], "score1": scores[1]})
	_emit({"type": "round_end", "winner": w, "points": pts, "by": "cards", "scores": scores.duplicate()})
	# 결과(공개 정보)로 AI 의심을 고치고, 문턱을 넘으면 고발
	for seat in [1, 0]:
		var brain = brains[seat]
		if brain == null or phase == Phase.MATCH_OVER:
			continue
		var before: float = brain.suspicion
		var delta: float = brain.on_round_result(w != seat, sides[1 - seat], turn_in_round)
		GameLog.info("SUSPECT", {"seat": seat, "by": "outcome", "delta": delta,
			"before": before, "after": brain.suspicion, "threshold": brain.accuse_threshold(tokens[seat])})
		if brain.should_accuse(tokens[seat]):
			accuse(seat)
	return {"ok": true, "result": res}


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
		next()
		guard += 1
	if guard >= AUTO_GUARD:
		GameLog.warn("MATCH", {"problem": "auto_guard", "seed": seed_value, "phase": phase})


# ───────────────────────── 내부 ─────────────────────────

func _begin_round() -> void:
	round_index += 1
	if round_index >= ROUNDS:
		var tied: bool = int(scores[0]) == int(scores[1])
		if not tied or round_index >= ROUNDS + EXTRA_ROUNDS:
			round_index -= 1   # 마지막으로 둔 판
			_finish_by_score()
			return
	# 판마다 진영을 바꿈 — 자리 0 은 1·3·5판에 왕 측. 연장 판은 동전 던지기 (왕 측 승률 80% 라 한쪽에 몰리지 않게)
	var s0: int = RankCards.Side.KING_SIDE if round_index % 2 == 0 else RankCards.Side.ASSASSIN_SIDE
	if round_index >= ROUNDS:
		s0 = RankCards.Side.KING_SIDE if rng.randf() < 0.5 else RankCards.Side.ASSASSIN_SIDE
		GameLog.info("DEAL", {"extra_round": round_index - ROUNDS + 1, "reason": "tie", "score": scores[0],
			"coin_seat0_side": RankCards.SIDE_NAMES[s0]})
	sides = [s0, RankCards.other_side(s0)]
	hands = [RankCards.new_hand(sides[0]), RankCards.new_hand(sides[1])]
	turn_in_round = 0
	round_over = false
	last_award = {"seat": -1, "points": 0}
	GameLog.info("DEAL", {"round": round_index + 1, "seat0_side": RankCards.SIDE_NAMES[sides[0]],
		"seat1_side": RankCards.SIDE_NAMES[sides[1]], "hand_size": RankCards.HAND_SIZE})
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
	phase = Phase.CHOOSE
	ai_late_peek = false
	mark_seen = false
	peeked_now = [false, false]
	_prune_evidence()
	# 1) 시선 — AI 자리만 정함 (사람 자리는 UI 토글 값 그대로)
	for seat in 2:
		if brains[seat] != null:
			gaze[seat] = brains[seat].pick_gaze(rng, int(strikes[1 - seat]))
	GameLog.info("TURN", {"round": round_index + 1, "turn": turn_in_round, "global_turn": global_turn,
		"gaze0": gaze[0], "gaze1": gaze[1]})
	_emit({"type": "turn_start", "turn_in_round": turn_in_round, "gaze": gaze.duplicate()})
	# 2) 자리 1 은 정보 없이 카드를 먼저 정함 (자리 0 카드를 보지 않음)
	tentative_ai_card = brains[1].choose_card(rng, hands[1], sides[1], {})
	GameLog.debug("AI_CARD", {"seat": 1, "tentative": RankCards.CARD_NAMES[tentative_ai_card]})
	# 3) 자리 1 속임수 — 엿보기면 자리 0 이 낸 뒤 카드를 다시 정함
	var ai_kind: String = brains[1].decide_cheat(rng, ["peek", "fake"], uses_left(1), sides[1],
		int(strikes[1]), gaze[0] == "hands", bool(marked[1]))
	if ai_kind != "":
		_do_cheat(1, ai_kind, brains[1].qte_quality(rng))
		if phase != Phase.CHOOSE:
			return   # 고발로 판이 끝남
	# 4) 자리 0 이 볼 수 있는 정보 — 뒷면 표시, 표정
	if marked[0]:
		mark_seen = rng.randf() < CheatRules.MARK_READ_CHANCE
		if mark_seen:
			_emit({"type": "mark_info", "seen": true, "special": tentative_ai_card != RankCards.Card.CITIZEN})
		else:
			_emit({"type": "mark_info", "seen": false})
	if gaze[0] == "face":
		var special: bool = tentative_ai_card != RankCards.Card.CITIZEN
		var p := FACE_CUE_IF_SPECIAL if special else FACE_CUE_IF_CITIZEN
		_emit({"type": "face_cue", "nervous": rng.randf() < p})
	# 5) 자리 0 이 AI 면 바로 둠 (시뮬레이션)
	if brains[0] != null:
		_auto_seat0()


func _auto_seat0() -> void:
	var b = brains[0]
	var kind: String = b.decide_cheat(rng, ["peek", "mark", "fake"], uses_left(0), sides[0],
		int(strikes[0]), gaze[1] == "hands", bool(marked[0]))
	if kind != "":
		_do_cheat(0, kind, b.qte_quality(rng))
		if phase != Phase.CHOOSE:
			return
	var info := {}
	if peeked_now[0] or (marked[0] and mark_seen):
		info["opp_card"] = tentative_ai_card
	var card: int = b.choose_card(rng, hands[0], sides[0], info)
	commit(card)


func _do_cheat(seat: int, kind: String, qte: float) -> void:
	var cdef: Dictionary = CheatRules.CHEATS[kind]
	var observer := 1 - seat
	var watched: bool = gaze[observer] == "hands"
	var prior: int = int(uses[seat].get(kind, 0))
	var tell := CheatRules.compute_tell(float(cdef["base_tell"]), qte, watched, prior, int(strikes[seat]))
	uses[seat][kind] = prior + 1
	var is_fake: bool = cdef["fake"]
	if is_fake:
		stats["fakes"][seat] += 1
	else:
		stats["cheats"][seat] += 1
		evidence.append({"owner": seat, "cheat": kind, "expires": CheatRules.evidence_expiry(kind, global_turn)})
	match kind:
		"peek":
			peeked_now[seat] = true
			if seat == 1:
				ai_late_peek = true
			else:
				_emit({"type": "peek_info", "card": tentative_ai_card})
		"mark":
			marked[seat] = true   # 다음 턴부터 보임 (MARK_READ_CHANCE)
	GameLog.info("CHEAT", {"seat": seat, "cheat": kind, "fake": is_fake, "qte": qte, "watched": watched,
		"prior_uses": prior, "strikes": strikes[seat], "tell": tell})
	_emit({"type": "cheat", "seat": seat, "cheat": kind, "fake": is_fake, "tell": tell, "watched": watched,
		"turn_in_round": turn_in_round})
	_observe_tell(observer, seat, tell)


## 관찰자에게는 '단서'만 감 — 진짜인지 가짜 동작인지는 모름
func _observe_tell(observer: int, actor: int, tell: float) -> void:
	var brain = brains[observer]
	if brain != null:
		var before: float = brain.suspicion
		var noticed: bool = brain.on_tell(rng, tell)
		GameLog.info("NOTICE", {"observer": observer, "tell": tell, "noticed": noticed,
			"before": before, "after": brain.suspicion})
		# 상대 표정 변화는 누구나 볼 수 있는 정보
		_emit({"type": "notice", "observer": observer, "noticed": noticed})
		if noticed and brain.should_accuse(int(tokens[observer])):
			accuse(observer)
	else:
		var p := CheatRules.notice_probability(tell, HUMAN_PERCEPTION)
		var seen := rng.randf() < p
		GameLog.info("NOTICE", {"observer": observer, "tell": tell, "p": p, "noticed": seen})
		_emit({"type": "tell", "seat": actor, "noticed": seen, "intensity": tell})


func _forfeit_round(winner_seat: int) -> void:
	if round_over and int(last_award["seat"]) >= 0:
		scores[int(last_award["seat"])] -= int(last_award["points"])   # 방금 끝난 판 결과를 되돌림
	var pts: int = RankCards.WIN_POINTS[sides[winner_seat]]
	scores[winner_seat] += pts
	last_award = {"seat": winner_seat, "points": pts}
	round_over = true
	phase = Phase.REVEALED
	GameLog.info("ROUND", {"round": round_index + 1, "winner": winner_seat, "points": pts, "by": "forfeit",
		"score0": scores[0], "score1": scores[1]})
	_emit({"type": "round_end", "winner": winner_seat, "points": pts, "by": "forfeit", "scores": scores.duplicate()})


func _end_match(w: int, reason: String) -> void:
	winner = w
	end_reason = reason
	phase = Phase.MATCH_OVER
	GameLog.info("MATCH", {"event": "end", "winner": w, "reason": reason, "score0": scores[0], "score1": scores[1],
		"strikes0": strikes[0], "strikes1": strikes[1], "cheats0": stats["cheats"][0], "cheats1": stats["cheats"][1]})
	_emit({"type": "match_end", "winner": w, "reason": reason, "scores": scores.duplicate()})


func _finish_by_score() -> void:
	var w := 2
	if int(scores[0]) > int(scores[1]):
		w = 0
	elif int(scores[1]) > int(scores[0]):
		w = 1
	_end_match(w, "SCORE")


func _prune_evidence() -> void:
	var kept: Array = []
	for e in evidence:
		if int(e["expires"]) >= global_turn:
			kept.append(e)
	evidence = kept


func _emit(ev: Dictionary) -> void:
	ev["round"] = round_index
	ev["turn"] = global_turn
	events.append(ev)


func _refuse(action: String, seat: int, why: String) -> Dictionary:
	GameLog.warn("REFUSE", {"action": action, "seat": seat, "why": why})
	return {"ok": false, "why": why}


func _brain_name(seat: int) -> String:
	return "human" if brains[seat] == null else str(brains[seat].display_name)
