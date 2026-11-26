# VERSION: v0.6.0 — 2026-11-26 — 판단 시간(노예가 낸 뒤 밝혀내기·일찍 공개·AI 왕 1.2초) · 버튼 활성 조건 = 실제 규칙 시험
# 이전 VERSION: v0.5.0 — 2026-11-26 — 왕 턴/노예 턴 · 시선 고정 엿보기·협력자 · 가능성 불(진짜·미끼) · 가리기·무작위·바꿔치기 · 밝혀내기 · 시선 끌기 · 제스처 시험
# 이전 VERSION: v0.4.0 — 2026-11-26 — 준비 동작 · 반사경(라이터) · 협력자 신호 · 카드 덮개 · 블러핑 시험
# 이전 VERSION: v0.3.0 — 2026-11-26 — 속임수는 노예 측만: 진영별 턴 종류 시험 · 왕 측은 엿볼 수 없음
#
# 실행 (저장소 맨 위에서):
#   godot --headless --path game/gamble-demo --script res://tests/run_tests.gd
# 실패가 하나라도 있으면 종료 코드 1.
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
		["judge", _t_judge],
		["buttons_match_rules", _t_buttons_match_rules],
		["objects", _t_objects],
		["peek_continuous", _t_peek_continuous],
		["lights_regardless", _t_lights_regardless],
		["accomplice", _t_accomplice],
		["human_expose", _t_human_expose],
		["ai_expose", _t_ai_expose],
		["sealed", _t_sealed],
		["defenses", _t_defenses],
		["attention", _t_attention],
		["gesture", _t_gesture],
		["two_strikes", _t_two_strikes],
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


func _run_until(m, cond: Callable, gaze: String, seconds: float = 20.0) -> bool:
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
	_check(str(CheatRules.OBJECTS["lighter"]["look"]) == str(CheatRules.OBJECTS["lighter_plain"]["look"]), "반사경 라이터와 빈 라이터는 겉모양이 같음")


func _t_phases() -> void:
	var m = _hm(1, _brain("inert"))
	m.start()
	_check(int(m.king) == 0 and int(m.phase) == GambleMatch.Phase.KING_TURN and m.actor() == 0, "1판: 사람 왕 턴")
	m.commit(int(m.hands[0][0]))
	_check(int(m.phase) == GambleMatch.Phase.SLAVE_TURN and m.actor() == 1, "그다음 AI 노예 턴")
	_run(m, 8.0, "table")
	_check(int(m.phase) == GambleMatch.Phase.JUDGE, "AI 노예가 냄 → 판단 시간")
	_run(m, 5.1, "table")
	_check(int(m.phase) == GambleMatch.Phase.REVEALED, "판단 시간이 끝나면 공개")
	var m2 = _hm(2, _brain("inert"))
	m2.round_index = 0
	m2.start()
	_check(int(m2.king) == 1 and int(m2.phase) == GambleMatch.Phase.KING_TURN and m2.actor() == 1, "2판: AI 왕 턴")
	_run(m2, 6.0, "table")
	_check(int(m2.phase) == GambleMatch.Phase.SLAVE_TURN and m2.actor() == 0 and int(m2.committed[1]) != -1, "그다음 사람 노예 턴")


func _t_judge() -> void:
	var b = _brain("inert")
	b.cheat_rate = 10.0
	b.objects = ["lighter"]
	var m = _hm(30, b)
	m.start()
	m.commit(int(m.hands[0][0]))
	var ok := _run_until(m, func(): return int(m.phase) == GambleMatch.Phase.JUDGE, "table", 12.0)
	_check(ok and bool(m.tried["peek"]) and float(m.judge_limit) == CheatRules.JUDGE_SECONDS, "AI 노예가 엿보고 냄 → 사람 왕 판단 시간 5초")
	_run(m, 2.0, "face")
	_check(int(m.phase) == GambleMatch.Phase.JUDGE, "5초 전엔 저절로 공개되지 않음")
	var r: Dictionary = m.expose("peek")
	_check(bool(r["ok"]) and bool(r["hit"]) and int(m.strikes[1]) == 1 and float(m.pending_time[1]) == -CheatRules.EXPOSE_CUT,
		"판단 시간 밝혀내기 적중 → 경고 + 노예의 다음 차례 −5초")
	var r2: Dictionary = m.expose("acc")
	_check(bool(r2["ok"]) and not bool(r2["hit"]) and float(m.pending_time[0]) == -CheatRules.EXPOSE_FAIL_CUT, "안 쓴 협력자를 밝혀내면 헛짚음 → 내 다음 턴 −5초")
	_check(bool(m.judge_done()["ok"]) and int(m.phase) == GambleMatch.Phase.REVEALED and not bool(m.judge_done()["ok"]), "판단 끝 → 바로 공개")
	var m2 = _hm(31, _brain("inert"))
	m2.start()
	m2.commit(int(m2.hands[0][0]))
	_run_until(m2, func(): return int(m2.phase) == GambleMatch.Phase.JUDGE, "table", 12.0)
	m2.sealed[1]["acc"] = true
	_check(not bool(m2.expose("acc")["ok"]), "봉인된 속임수는 밝혀내기 불가 (버튼 흐림)")
	var m3 = _hm(32, _brain("inert"))
	m3.round_index = 0
	m3.start()
	_run_until(m3, func(): return int(m3.phase) == GambleMatch.Phase.SLAVE_TURN, "table")
	m3.commit(int(m3.hands[0][0]))
	_check(int(m3.phase) == GambleMatch.Phase.JUDGE and float(m3.judge_limit) == CheatRules.AI_JUDGE_SECONDS
		and not bool(m3.expose("peek")["ok"]) and not bool(m3.judge_done()["ok"]), "내가 노예로 내면 AI 왕 판단 1.2초 · 나는 판단 못 함")
	_run(m3, 1.3, "table")
	_check(int(m3.phase) == GambleMatch.Phase.REVEALED, "AI 판단 끝 → 공개")


## 화면 버튼이 켜지는 조건(why_not == "")과 실제 행동 결과가 같은지 — 상태 5가지 × 행동 11가지
func _t_buttons_match_rules() -> void:
	var ids := ["lighter", "lighter_plain", "accomplice", "attention", "gesture", "cover", "random", "fake", "expose_peek", "expose_acc", "judge_done"]
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
	var m = _hm(40, _brain("inert"), ["lighter"])
	if kind.begins_with("slave"):
		m.round_index = 0
	m.start()
	if kind == "king_slave_turn":
		m.commit(int(m.hands[0][0]))
	elif kind == "king_judge":
		m.commit(int(m.hands[0][0]))
		_run_until(m, func(): return int(m.phase) == GambleMatch.Phase.JUDGE, "table", 12.0)
	elif kind == "slave_slave_turn":
		_run_until(m, func(): return int(m.phase) == GambleMatch.Phase.SLAVE_TURN, "table")
	return m


func _rule_of(id: String) -> Array:
	if id == "lighter" or id == "lighter_plain":
		return ["object", id]
	if id == "expose_peek":
		return ["expose", "peek"]
	if id == "expose_acc":
		return ["expose", "acc"]
	return [id, ""]


func _call_action(m, id: String) -> bool:
	var r: Dictionary = {}
	if id == "lighter" or id == "lighter_plain":
		r = m.place_object(id)
	elif id == "accomplice":
		r = m.call_accomplice()
	elif id == "attention":
		r = m.attention()
	elif id == "gesture":
		r = m.gesture()
	elif id == "cover":
		r = m.cover()
	elif id == "random":
		r = m.play_random()
	elif id == "fake":
		r = m.fake()
	elif id == "expose_peek":
		r = m.expose("peek")
	elif id == "expose_acc":
		r = m.expose("acc")
	elif id == "judge_done":
		r = m.judge_done()
	return bool(r.get("ok", false))


func _t_objects() -> void:
	var m = _hm(20, _brain("inert"), ["lighter", "glass", "phone", "cigcase"])
	_check(m.objects[0].size() == CheatRules.OBJECT_SLOTS, "사전 설정은 %d개까지" % CheatRules.OBJECT_SLOTS)
	var m2 = _hm(21, _brain("inert"), ["lighter"])
	m2.start()
	_check(not bool(m2.set_objects(0, ["glass"])["ok"]), "시작 뒤엔 사전 설정 불가")
	_check(bool(m2.place_object("lighter_plain")["ok"]) and bool(m2.place_object("cigcase")["ok"]), "게임 중 놓기")
	_check(not bool(m2.place_object("phone")["ok"]) and m2.objects[0].size() == 3, "자리가 다 차면 못 놓음")
	_check(int(m2.stats["objects_placed"][0]) == 2, "게임 중 놓은 수 기록")


func _t_peek_continuous() -> void:
	var m = _hm(3, _brain("inert"), ["lighter", "glass"])
	_start_slave(m)
	_run(m, 1.0, "obj0")
	_check(_first(m, "info").is_empty(), "1초로는 안 보임")
	_run(m, 0.1, "table")
	_run(m, 1.0, "obj0")
	_check(_first(m, "info").is_empty(), "눈을 떼면 처음부터 (게이지 아님)")
	_run(m, 0.6, "obj0")
	var ev := _first(m, "info")
	_check(not ev.is_empty() and int(ev["card"]) == int(m.committed[m.king]) and str(ev["source"]) == "peek" and bool(m.lights["peek"]),
		"1.5초 계속 보면 카드 + 불")


func _t_lights_regardless() -> void:
	var m = _hm(4, _brain("inert"), ["lighter", "glass"])
	_start_slave(m)
	_run(m, 1.6, "obj1")
	_check(bool(m.lights["peek"]) and _first(m, "info").is_empty() and int(m.stats["baits"][0]) == 1, "미끼 물건도 1.5초면 불 (카드는 안 보임)")
	_run(m, 1.9, "accomplice")
	_check(bool(m.lights["acc"]) and _first(m, "info").is_empty(), "빈 협력자 자리도 1.8초면 불")


func _t_accomplice() -> void:
	var m = _hm(5, _brain("inert"), [])
	_start_slave(m)
	_check(bool(m.call_accomplice()["ok"]) and not bool(m.call_accomplice()["ok"]), "협력자는 한 번 부름")
	_run(m, 2.6, "table")
	_check(str(m.acc_state[0]) == "present", "걸어와서 섬")
	_run(m, 1.9, "accomplice")
	var ev := _first(m, "info")
	_check(not ev.is_empty() and str(ev["source"]) == "acc" and int(ev["card"]) == int(m.committed[m.king]), "1.8초 계속 보면 카드")


func _t_human_expose() -> void:
	var b = _brain("inert")
	b.cheat_rate = 10.0
	b.objects = ["lighter"]
	var m = _hm(6, b)
	m.start()
	m.commit(int(m.hands[0][0]))
	var ok := _run_until(m, func(): return str(m.gaze[1]) == "obj0" and float(m.t) - float(m.gaze_since[1]) >= 0.5, "table", 8.0)
	var r: Dictionary = m.expose("peek")
	_check(ok and bool(r["hit"]) and int(m.strikes[1]) == 1 and bool(m.sealed[1]["peek"]), "진짜 엿보기를 밝혀냄 → 경고·봉인")
	_check(float(m.limit) <= CheatRules.TURN_SECONDS - CheatRules.EXPOSE_CUT + 1e-6, "노예 턴 −5초")
	var m2 = _hm(7, _brain("honest"))
	m2.start()
	m2.commit(int(m2.hands[0][0]))
	_run(m2, 1.0, "face")
	var r2: Dictionary = m2.expose("peek")
	_check(not bool(r2["hit"]) and float(m2.pending_time[0]) == -CheatRules.EXPOSE_FAIL_CUT and not bool(m2.expose("peek")["ok"]),
		"헛짚음 → 내 다음 턴 −5초 · 턴마다 한 번")


func _t_ai_expose() -> void:
	var w = _brain("inert")
	w.perception = 1.0
	w.force_watch = "face"
	var m = _hm(8, w, ["lighter", "glass"])
	_start_slave(m)
	_run(m, 3.0, "obj0")
	_check(int(m.strikes[0]) == 1 and bool(m.sealed[0]["peek"]), "AI 왕이 진짜 엿보기를 밝혀냄")
	var w2 = _brain("inert")
	w2.perception = 1.0
	w2.force_watch = "face"
	var m2 = _hm(9, w2, ["glass"])
	_start_slave(m2)
	_run(m2, 3.0, "obj0")
	_check(int(m2.strikes[0]) == 0 and float(m2.pending_time[1]) == -CheatRules.EXPOSE_FAIL_CUT, "미끼를 밝혀내면 헛짚음 → AI 다음 턴 −5초")


func _t_sealed() -> void:
	var m = _hm(22, _brain("inert"), ["lighter"])
	_start_slave(m)
	m.sealed[0]["peek"] = true
	_run(m, 1.6, "obj0")
	_check(_first(m, "info").is_empty(), "봉인된 속임수는 안 통함")


func _t_defenses() -> void:
	var m = _hm(10, _brain("inert"), ["lighter"])
	_start_slave(m)
	m._cover(m.king)
	_run(m, 1.6, "obj0")
	_check(_first(m, "info").is_empty() and str(_first(m, "info_blocked").get("why", "")) == "cover", "가리기 → 엿보기 막힘")
	m.call_accomplice()
	_run(m, 2.6, "table")
	_run(m, 1.9, "accomplice")
	_check(str(_first(m, "info").get("source", "")) == "acc", "가리기는 협력자를 못 막음")
	var m2 = _hm(11, _brain("inert"), ["lighter"])
	m2.round_index = 0
	m2.start()
	m2.call_accomplice()
	m2._randomize(m2.king)
	_check(int(m2.phase) == GambleMatch.Phase.SLAVE_TURN and bool(m2.randomized), "무작위 → 바로 냄")
	_run(m2, 2.6, "table")
	_run(m2, 1.6, "obj0")
	_run(m2, 1.9, "accomplice")
	_check(_first(m2, "info").is_empty(), "무작위 → 엿보기·협력자 둘 다 막힘")
	var m3 = _hm(12, _brain("inert"), ["lighter"])
	_start_slave(m3)
	m3._fake(m3.king)
	_run(m3, 1.6, "obj0")
	var ev := _first(m3, "info")
	var real_card: int = int(m3.committed[m3.king])
	_check(not ev.is_empty() and int(ev["card"]) != real_card and int(ev["card"]) == m3._fake_of(real_card), "바꿔치기 → 가짜 카드가 보임")


func _t_attention() -> void:
	var w = _brain("inert")
	w.perception = 1.0
	w.force_watch = "face"
	var m = _hm(13, w, ["lighter"])
	_start_slave(m)
	_check(bool(m.attention()["ok"]) and str(m.gaze[1]) == "away", "시선 끌기 → 왕이 딴 곳을 봄")
	_run(m, 1.6, "obj0")
	_check(not _first(m, "info").is_empty() and not bool(m.lights["peek"]) and int(m.strikes[0]) == 0, "그동안 엿보기: 불도 밝혀내기도 없음")
	_check(not bool(m.attention()["ok"]), "매치 한 번")


func _t_gesture() -> void:
	var m = _hm(14, _brain("inert"))
	m.round_index = 0
	m.start()
	_check(int(m.phase) == GambleMatch.Phase.KING_TURN and bool(m.gesture()["ok"]) and absf(float(m.limit) - 10.0) < 1e-9 and bool(m.king_rushed),
		"제스처 → AI 왕 턴 −5초")
	_check(not bool(m.gesture()["ok"]), "왕 턴마다 한 번")
	var b2 = _brain("inert")
	b2.gesture_rate = 10.0
	var m2 = _hm(15, b2)
	m2.start()
	_run(m2, 4.5, "table")
	_check(int(m2.phase) == GambleMatch.Phase.KING_TURN and absf(float(m2.limit) - 10.0) < 1e-9, "AI 제스처 → 내 왕 턴 −5초")
	var m3 = _hm(16, _brain("inert"))
	m3.round_index = 0
	m3.start()
	m3.t = 5.5
	_check(not bool(m3.gesture()["ok"]), "왕 턴이 10초 미만 남으면 못 씀")


func _t_two_strikes() -> void:
	var w = _brain("inert")
	w.perception = 1.5
	w.force_watch = "face"
	var m = _hm(16, w, ["lighter"])
	m.round_index = 0
	m.start()
	m.call_accomplice()
	_run_until(m, func(): return int(m.phase) == GambleMatch.Phase.SLAVE_TURN, "table")
	_run(m, 3.0, "obj0")
	_check(int(m.strikes[0]) == 1 and not m.is_over(), "경고 1")
	_run_until(m, func(): return str(m.acc_state[0]) == "present", "table", 3.0)
	_run(m, 6.0, "accomplice")
	_check(m.is_over() and int(m.winner) == 1 and str(m.end_reason) == "CAUGHT_TWICE", "경고 2 → 즉시 패배")


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
	var m = _hm(17, _brain("inert"))
	m.start()
	_run(m, 15.5, "table")
	_check(not _first(m, "timeout").is_empty() and int(m.phase) == GambleMatch.Phase.SLAVE_TURN, "왕 턴 시간 초과 → 무작위 카드")


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
		var last := -1
		for e in m.events:
			if str(e["type"]) == "phase_start":
				ok = ok and int(e["phase"]) != last
				last = int(e["phase"])
			elif str(e["type"]) == "turn_start":
				last = -1
	_check(ok, "AI 대 AI 100판: 끝까지 가고, 경고 ≤ 2, 단계 순서 정상")
	print("[TEST] auto_matches=100 caught_twice=%d" % caught2)
