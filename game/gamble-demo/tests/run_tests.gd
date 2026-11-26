# VERSION: v0.8.0 — 2026-11-26 — 30초 턴 · 방어는 낸 뒤에만 · '!' 표시·게이지 · 협력자 부르기(주시 → 가능성)·이어폰 정보 · 물건 확인/몸 수색 · 성공 시 그 턴 무효 · 횟수 제한 시험
# 이전 VERSION: v0.6.0 — 2026-11-26 — 판단 시간(노예가 낸 뒤 밝혀내기·일찍 공개·AI 왕 1.2초) · 버튼 활성 조건 = 실제 규칙 시험
# 이전 VERSION: v0.5.0 — 2026-11-26 — 왕 턴/노예 턴 · 시선 고정 엿보기·협력자 · 가능성 불(진짜·미끼) · 가리기·무작위·바꿔치기 · 밝혀내기 · 시선 끌기 · 제스처 시험
#
# 실행 (저장소 맨 위에서):
#   godot --headless --path game/gamble-demo --script res://tests/run_tests.gd
# 실패가 하나라도 있으면 종료 코드 1. (같은 시험을 파이썬 사본으로 먼저 돌려 46개 통과 확인)
extends SceneTree

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const AiBrain = preload("res://core/ai_brain.gd")
const GambleMatch = preload("res://core/match.gd")
const GameLog = preload("res://core/game_log.gd")

const DT := 0.05

var _passes := 0
var _fails := 0


func _initialize() -> void:
	GameLog.level = GameLog.Level.ERROR   # 시험 중 거절(REFUSE) 경고는 일부러 내는 것이라 숨김
	var tests: Array = [
		["rules_table", _t_rules_table],
		["phases", _t_phases],
		["defense_after_commit", _t_defense_after_commit],
		["objects", _t_objects],
		["peek_gauge", _t_peek_gauge],
		["marks_regardless", _t_marks_regardless],
		["call", _t_call],
		["inspect", _t_inspect],
		["search", _t_search],
		["defenses", _t_defenses],
		["attention", _t_attention],
		["ai_judge", _t_ai_judge],
		["two_strikes", _t_two_strikes],
		["judge", _t_judge],
		["buttons_match_rules", _t_buttons_match_rules],
		["ai_ignores_hidden_card", _t_ai_ignores_hidden_card],
		["timeout", _t_timeout],
		["tiebreak", _t_tiebreak],
		["determinism", _t_determinism],
		["auto_match_sane", _t_auto_match_sane],
	]
	var t0 := Time.get_ticks_msec()
	for t in tests:
		var before := _fails
		var fn: Callable = t[1]
		fn.call()
		print("[TEST] name=%s result=%s" % [t[0], "PASS" if _fails == before else "FAIL"])
	print("[TEST] checks_passed=%d checks_failed=%d ms=%d" % [_passes, _fails, Time.get_ticks_msec() - t0])
	quit(1 if _fails > 0 else 0)


# ───────────────────────── 도우미 ─────────────────────────

func _check(cond: bool, msg: String) -> void:
	if cond:
		_passes += 1
	else:
		_fails += 1
		printerr("  FAIL: " + msg)


func _brain(kind: String):
	var b = AiBrain.new()
	b.configure(kind)
	return b


func _hm(p_seed: int, ai, objs = null):
	var m = GambleMatch.new()
	m.setup(p_seed, null, ai)
	if objs != null:
		m.set_objects(0, objs)
	return m


## seconds 만큼 (DT 단위) 흘림 — 단계가 바뀌면 멈춤
func _run(m, seconds: float, gaze: String) -> void:
	var ph: int = int(m.phase)
	for i in ceili(seconds / DT):
		m.tick(DT, gaze)
		if int(m.phase) != ph:
			return


func _run_until(m, cond: Callable, gaze: String, seconds: float = 40.0) -> bool:
	for i in int(seconds / DT):
		if bool(cond.call()):
			return true
		m.tick(DT, gaze)
	return bool(cond.call())


## 2판(사람 = 노예 측)을 시작해 노예 턴까지
func _start_slave(m) -> void:
	m.round_index = 0
	m.start()
	_run_until(m, func(): return int(m.phase) == GambleMatch.Phase.SLAVE_TURN, "table")


func _first(m, type_name: String) -> Dictionary:
	for ev in m.events:
		if str(ev["type"]) == type_name:
			return ev
	return {}


# ───────────────────────── 시험 ─────────────────────────

func _t_rules_table() -> void:
	var king: int = RankCards.Card.KING
	var cit: int = RankCards.Card.CITIZEN
	var asn: int = RankCards.Card.ASSASSIN
	_check(RankCards.resolve(king, cit) == 1 and RankCards.resolve(cit, asn) == 1 and RankCards.resolve(asn, king) == 1, "왕 > 시민 > 암살자 > 왕")
	_check(RankCards.resolve(cit, cit) == 0, "시민 = 시민")
	_check(CheatRules.is_mirror("lighter") and not CheatRules.is_mirror("lighter_plain") and not CheatRules.is_mirror("glass"), "반사경 여부")
	_check(CheatRules.TURN_SECONDS == 30.0, "턴 30초")


func _t_phases() -> void:
	var m = _hm(1, _brain("inert"))
	m.start()
	_check(int(m.king) == 0 and int(m.phase) == GambleMatch.Phase.KING_TURN and m.actor() == 0 and float(m.limit) == 30.0, "1판: 사람 왕 턴 30초")
	m.commit(int(m.hands[0][0]))
	_check(int(m.phase) == GambleMatch.Phase.SLAVE_TURN and m.actor() == 1, "그다음 AI 노예 턴")
	_run(m, 15.0, "table")
	_check(int(m.phase) == GambleMatch.Phase.JUDGE, "AI 노예가 냄 → 판단 시간")
	_run(m, 5.1, "table")
	_check(int(m.phase) == GambleMatch.Phase.REVEALED, "판단 시간이 끝나면 공개")
	var m2 = _hm(2, _brain("inert"))
	m2.round_index = 0
	m2.start()
	_check(int(m2.king) == 1 and int(m2.phase) == GambleMatch.Phase.KING_TURN and m2.actor() == 1, "2판: AI 왕 턴")
	_run(m2, 7.0, "table")
	_check(int(m2.phase) == GambleMatch.Phase.SLAVE_TURN and m2.actor() == 0 and int(m2.committed[1]) != -1, "그다음 사람 노예 턴")


func _t_defense_after_commit() -> void:
	var m = _hm(3, _brain("inert"), ["lighter"])
	m.start()
	var all_blocked := true
	for a in ["cover", "random", "fake", "inspect", "search"]:
		if str(m.why_not(0, a)) != "after_commit":
			all_blocked = false
	_check(all_blocked, "카드를 고르는 중엔 방어 행동 못 함")
	m.commit(int(m.hands[0][0]))
	_check(bool(m.cover()["ok"]) and bool(m.fake()["ok"]), "낸 뒤엔 가리기·바꿔치기")
	_check(bool(m.play_random()["ok"]) and m.hands[0].has(int(m.committed[0])) and bool(m.randomized), "낸 뒤 섞기 (낸 카드가 패 중 하나로)")


func _t_objects() -> void:
	var m = _hm(20, _brain("inert"), ["lighter", "glass", "phone", "cigcase"])
	_check(m.objects[0].size() == CheatRules.OBJECT_SLOTS, "사전 설정은 3개까지")
	var m2 = _hm(21, _brain("inert"), [])
	m2.start()
	_check(not bool(m2.set_objects(0, ["glass"])["ok"]), "시작 뒤엔 사전 설정 불가")
	_check(bool(m2.place_object("lighter")["ok"]) and bool(m2.place_object("lighter_plain")["ok"]), "게임 중 두 번 놓기")
	var r: Dictionary = m2.place_object("glass")
	_check(not bool(r["ok"]) and str(r["why"]) == "no_uses", "게임 중 놓기는 매치 %d번" % CheatRules.PLACES_PER_MATCH)


func _t_peek_gauge() -> void:
	var m = _hm(4, _brain("inert"), ["lighter", "glass"])
	_start_slave(m)
	_run(m, 1.0, "obj0")
	var g: float = m.dwell_progress()
	_check(_first(m, "info").is_empty() and g > 0.5 and g < 0.8, "1초: 카드 안 보임, 게이지 약 0.67")
	_run(m, 0.1, "table")
	_run(m, 1.0, "obj0")
	_check(_first(m, "info").is_empty(), "눈을 떼면 처음부터")
	_run(m, 0.6, "obj0")
	var ev := _first(m, "info")
	_check(not ev.is_empty() and int(ev["card"]) == int(m.committed[m.king]) and str(ev["source"]) == "peek" and bool(m.marks[0]),
		"1.5초 계속 보면 카드 + '!'")


func _t_marks_regardless() -> void:
	var m = _hm(5, _brain("inert"), ["lighter", "glass"])
	_start_slave(m)
	_run(m, 1.6, "obj1")
	_check(bool(m.marks[1]) and not bool(m.marks[0]) and _first(m, "info").is_empty() and int(m.stats["baits"][0]) == 1,
		"미끼 물건도 1.5초면 '!' (카드는 안 보임)")


func _t_call() -> void:
	var w = _brain("inert")
	w.perception = 1.0
	w.force_watch = "face"
	var m = _hm(6, w, [])
	_start_slave(m)
	_check(bool(m.start_call()["ok"]) and bool(m.calling[0]), "부르기 시작")
	_run(m, 2.6, "table")
	_check(bool(m.acc_connected[0]) and float(m.acc_suspect[0]) >= 0.8, "2.5초면 연결 · 보고 있었으니 가능성 높음")
	_run(m, 3.1, "table")
	var ev := _first(m, "info")
	_check(not ev.is_empty() and str(ev["source"]) == "acc" and int(ev["card"]) == int(m.committed[m.king]), "3초 뒤 이어폰으로 카드")
	var w2 = _brain("inert")
	w2.perception = 1.0
	w2.force_watch = "away"
	var m2 = _hm(7, w2, [])
	_start_slave(m2)
	m2.start_call()
	_run(m2, 2.6, "table")
	_check(bool(m2.acc_connected[0]) and float(m2.acc_suspect[0]) == 0.0, "안 볼 때 부르면 가능성 0")
	var m3 = _hm(8, w, [])
	_start_slave(m3)
	m3.start_call()
	_run(m3, 1.0, "table")
	m3.stop_call()
	_check(not bool(m3.acc_connected[0]) and int(m3.acc_calls_left[0]) == CheatRules.ACC_CALLS_PER_MATCH - 1 and float(m3.acc_suspect[0]) > 0.0,
		"중간에 멈추면 연결 안 됨 · 횟수는 씀 · 가능성은 남음")


func _t_inspect() -> void:
	var b = _brain("inert")
	b.objects = ["lighter", "glass"]
	var m = _hm(9, b)
	m.start()
	m.commit(int(m.hands[0][0]))
	var r: Dictionary = m.inspect(0)
	_check(bool(r["ok"]) and bool(r["hit"]) and int(m.strikes[1]) == 1 and bool(m.sealed[1]["peek"]) and m.objects[1] == ["glass"],
		"반사경 물건 확인 → 적중 · 압수 · 봉인")
	_check(int(m.phase) == GambleMatch.Phase.KING_TURN and int(m.turn_in_round) == 1 and m.committed == [-1, -1] and not _first(m, "turn_void").is_empty(),
		"그 턴 무효 → 같은 턴 다시 고름")
	m.commit(int(m.hands[0][0]))
	_check(int(m.phase) == GambleMatch.Phase.SLAVE_TURN and float(m.limit) == 20.0, "노예가 다시 고르는 턴 −10초")
	var b2 = _brain("inert")
	b2.objects = ["lighter", "glass"]
	var m2 = _hm(10, b2)
	m2.start()
	m2.commit(int(m2.hands[0][0]))
	var r2: Dictionary = m2.inspect(1)
	_check(bool(r2["ok"]) and not bool(r2["hit"]) and bool(m2.checked[1][1]) and float(m2.pending_time[0]) == -10.0 and int(m2.phase) == GambleMatch.Phase.SLAVE_TURN,
		"빈 물건 → 헛짚음 · 내 다음 차례 −10초")
	_check(not bool(m2.inspect(0)["ok"]), "물건 확인은 턴마다 한 번")


func _t_search() -> void:
	var m = _hm(11, _brain("inert"))
	m.start()
	m.commit(int(m.hands[0][0]))
	m.acc_connected[1] = true
	var r: Dictionary = m.search()
	_check(bool(r["hit"]) and int(m.strikes[1]) == 1 and bool(m.sealed[1]["acc"]) and not bool(m.acc_connected[1]) and int(m.phase) == GambleMatch.Phase.KING_TURN,
		"몸 수색으로 이어폰 발견 → 적중 · 그 턴 무효")
	var m2 = _hm(12, _brain("inert"))
	m2.start()
	m2.commit(int(m2.hands[0][0]))
	var r2: Dictionary = m2.search()
	_check(not bool(r2["hit"]) and float(m2.pending_time[0]) == -10.0, "아무것도 없으면 헛짚음")


func _t_defenses() -> void:
	var m = _hm(13, _brain("inert"), ["lighter"])
	m.round_index = 0
	m.start()
	m.acc_connected[0] = true
	_run_until(m, func(): return int(m.phase) == GambleMatch.Phase.SLAVE_TURN, "table")
	m._cover(m.king)
	_run(m, 1.6, "obj0")
	_check(_first(m, "info").is_empty() and str(_first(m, "info_blocked").get("why", "")) == "cover", "가리기 → 반사경 막힘")
	_run(m, 1.6, "table")
	_check(str(_first(m, "info").get("source", "")) == "acc", "가리기는 이어폰을 못 막음")
	var m2 = _hm(14, _brain("inert"), ["lighter"])
	m2.round_index = 0
	m2.start()
	m2.acc_connected[0] = true
	_run_until(m2, func(): return int(m2.phase) == GambleMatch.Phase.SLAVE_TURN, "table")
	m2._randomize(m2.king)
	_run(m2, 1.6, "obj0")
	_run(m2, 2.0, "table")
	_check(_first(m2, "info").is_empty() and m2.hands[m2.king].has(int(m2.committed[m2.king])), "섞기 → 반사경·이어폰 둘 다 막힘")
	var m3 = _hm(15, _brain("inert"), ["lighter"])
	_start_slave(m3)
	m3._fake(m3.king)
	_run(m3, 1.6, "obj0")
	var ev := _first(m3, "info")
	var real_card: int = int(m3.committed[m3.king])
	_check(not ev.is_empty() and int(ev["card"]) == m3._fake_of(real_card) and int(ev["card"]) != real_card, "바꿔치기 → 가짜 카드가 보임")


func _t_attention() -> void:
	var w = _brain("inert")
	w.perception = 1.0
	w.force_watch = "face"
	var m = _hm(16, w, ["lighter"])
	_start_slave(m)
	_check(bool(m.attention()["ok"]) and str(m.gaze[1]) == "away", "시선 끌기 → 상대가 딴 곳을 봄")
	_run(m, 1.6, "obj0")
	_check(not _first(m, "info").is_empty() and not bool(m.marks[0]), "그동안 엿보면 '!' 가 안 뜸")
	_check(not bool(m.attention()["ok"]), "매치 한 번")


func _t_ai_judge() -> void:
	var k = _brain("inert")
	k.expose_rate = 10.0
	var m = _hm(17, k, ["lighter"])
	_start_slave(m)
	_run(m, 1.6, "obj0")
	m.commit(int(m.hands[0][0]))
	_check(int(m.strikes[0]) == 1 and bool(m.sealed[0]["peek"]) and int(m.phase) == GambleMatch.Phase.KING_TURN and m.objects[0].is_empty(),
		"AI 왕이 판단 때 '!' 반사경 물건을 확인 → 적중 · 무효")
	var m2 = _hm(18, _brain("inert"), ["lighter"])
	_start_slave(m2)
	_run(m2, 1.6, "obj0")
	m2.commit(int(m2.hands[0][0]))
	_check(int(m2.strikes[0]) == 0 and int(m2.phase) == GambleMatch.Phase.JUDGE and float(m2.judge_limit) == CheatRules.AI_JUDGE_SECONDS,
		"확인 확률 0 이면 확인 안 함 · AI 판단 1.2초")
	_run(m2, 1.3, "table")
	_check(int(m2.phase) == GambleMatch.Phase.REVEALED, "AI 판단 끝 → 공개")


func _t_two_strikes() -> void:
	var k = _brain("inert")
	k.expose_rate = 10.0
	var m = _hm(19, k, ["lighter"])
	_start_slave(m)
	m.strikes[0] = 1
	_run(m, 1.6, "obj0")
	m.commit(int(m.hands[0][0]))
	_check(m.is_over() and int(m.winner) == 1 and str(m.end_reason) == "CAUGHT_TWICE", "경고 2개 → 즉시 패배")


func _t_judge() -> void:
	var m = _hm(23, _brain("inert"))
	m.start()
	m.commit(int(m.hands[0][0]))
	_run_until(m, func(): return int(m.phase) == GambleMatch.Phase.JUDGE, "table")
	_check(float(m.judge_limit) == CheatRules.JUDGE_SECONDS and str(m.why_not(0, "inspect")) == "no_target" and str(m.why_not(0, "search")) == "",
		"사람 왕 판단 5초 · 몸 수색 가능 (확인할 물건 없음)")
	_check(bool(m.judge_done()["ok"]) and int(m.phase) == GambleMatch.Phase.REVEALED, "판단 끝 → 공개")


## 화면 버튼이 켜지는 조건(why_not == "")과 실제 행동 결과가 같은지 — 상태 5가지 × 행동 10가지
func _t_buttons_match_rules() -> void:
	var ids := ["lighter", "lighter_plain", "call", "attention", "cover", "random", "fake", "inspect", "search", "judge_done"]
	for st in ["king_turn", "king_slave_turn", "king_judge", "slave_king_turn", "slave_slave_turn"]:
		var bad := PackedStringArray()
		for id in ids:
			var m = _state(str(st))
			var rule := _rule_of(str(id))
			var predicted: bool = str(m.why_not(0, str(rule[0]), str(rule[1]))) == ""
			var actual := _call_action(m, str(id))
			if predicted != actual:
				bad.append("%s(버튼 %s, 실제 %s)" % [id, predicted, actual])
		_check(bad.is_empty(), "상태 %s: 버튼과 규칙이 다름 %s" % [st, ", ".join(bad)])


func _state(kind: String):
	var b = _brain("inert")
	b.objects = ["lighter", "glass"]
	var m = _hm(40, b, ["lighter"])
	if kind.begins_with("slave"):
		m.round_index = 0
	m.start()
	if kind == "king_slave_turn":
		m.commit(int(m.hands[0][0]))
	elif kind == "king_judge":
		m.commit(int(m.hands[0][0]))
		_run_until(m, func(): return int(m.phase) == GambleMatch.Phase.JUDGE, "table")
	elif kind == "slave_slave_turn":
		_run_until(m, func(): return int(m.phase) == GambleMatch.Phase.SLAVE_TURN, "table")
	return m


func _rule_of(id: String) -> Array:
	if id == "lighter" or id == "lighter_plain":
		return ["object", id]
	if id == "inspect":
		return ["inspect", "0"]
	return [id, ""]


func _call_action(m, id: String) -> bool:
	var r: Dictionary = {}
	if id == "lighter" or id == "lighter_plain":
		r = m.place_object(id)
	elif id == "call":
		r = m.start_call()
	elif id == "attention":
		r = m.attention()
	elif id == "cover":
		r = m.cover()
	elif id == "random":
		r = m.play_random()
	elif id == "fake":
		r = m.fake()
	elif id == "inspect":
		r = m.inspect(0)
	elif id == "search":
		r = m.search()
	elif id == "judge_done":
		r = m.judge_done()
	return bool(r.get("ok", false))


## AI 는 사람이 낸 (안 보이는) 카드를 몰래 읽지 않음: 같은 시드면 사람 카드가 달라도 AI 카드가 같음
func _t_ai_ignores_hidden_card() -> void:
	var same := true
	for s in range(100, 140):
		if _ai_card(s, RankCards.Card.KING) != _ai_card(s, RankCards.Card.CITIZEN):
			same = false
	_check(same, "AI 는 숨긴 카드를 모름")


func _ai_card(p_seed: int, my_card: int) -> int:
	var m = _hm(p_seed, _brain("honest"))
	m.start()
	m.commit(my_card)
	_run_until(m, func(): return int(m.phase) == GambleMatch.Phase.REVEALED, "table")
	var ev := _first(m, "reveal")
	return int(ev["cards"][1]) if not ev.is_empty() else -1


func _t_timeout() -> void:
	var m = _hm(24, _brain("inert"))
	m.start()
	_run(m, 30.5, "table")
	_check(not _first(m, "timeout").is_empty() and int(m.phase) == GambleMatch.Phase.SLAVE_TURN, "왕 턴 30초 초과 → 무작위 카드")


func _t_tiebreak() -> void:
	var m = GambleMatch.new()
	m.setup(10, _brain("honest"), _brain("honest"))
	m.round_index = GambleMatch.ROUNDS - 1
	m.scores = [3, 3]
	m.round_over = true
	m.phase = GambleMatch.Phase.REVEALED
	m.next()
	_check(int(m.round_index) == GambleMatch.ROUNDS and not m.is_over(), "동점 → 연장")
	m.scores = [5, 4]
	m.round_over = true
	m.phase = GambleMatch.Phase.REVEALED
	m.next()
	_check(m.is_over() and int(m.winner) == 0 and str(m.end_reason) == "SCORE", "연장에서 갈리면 끝")


func _t_determinism() -> void:
	_check(_auto_events(777) == _auto_events(777) and _auto_events(777) != _auto_events(778), "같은 시드 = 같은 매치")


func _auto_events(p_seed: int) -> String:
	var m = GambleMatch.new()
	m.setup(p_seed, _brain("cheater"), _brain("watcher"))
	m.run_auto()
	return str(m.events)


func _t_auto_match_sane() -> void:
	var ok := true
	var caught2 := 0
	for s in range(1, 101):
		var m = GambleMatch.new()
		m.setup(s, _brain("cheater"), _brain("gambler"))
		m.run_auto()
		ok = ok and m.is_over() and maxi(int(m.strikes[0]), int(m.strikes[1])) <= CheatRules.STRIKES_TO_LOSE
		if str(m.end_reason) == "CAUGHT_TWICE":
			caught2 += 1
	_check(ok, "AI 대 AI 100판: 끝까지 가고, 경고 ≤ 2")
	print("[TEST] auto_matches=100 caught_twice=%d" % caught2)
