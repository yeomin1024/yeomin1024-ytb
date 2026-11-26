# VERSION: v0.4.0 — 2026-11-26 — 준비 동작 · 반사경(라이터) · 협력자 신호 · 카드 덮개 · 블러핑 시험
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
		["peek_math", _t_peek_math],
		["turn_roles", _t_turn_roles],
		["lighter_needed_then_reveals", _t_lighter_needed_then_reveals],
		["caught_when_watched", _t_caught_when_watched],
		["setup_seen", _t_setup_seen],
		["accomplice", _t_accomplice],
		["cover_blocks_shiner", _t_cover_blocks_shiner],
		["bluff_time", _t_bluff_time],
		["detect_accuse", _t_detect_accuse],
		["ai_peek_best_response", _t_ai_peek_best_response],
		["ai_ignores_hidden_card", _t_ai_ignores_hidden_card],
		["two_strikes", _t_two_strikes],
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


func _near(a: float, b: float, tol: float, msg: String) -> void:
	_check(absf(a - b) <= tol, "%s (got %.6f, want %.6f ±%.6f)" % [msg, a, b, tol])


func _brain(kind: String):
	var b = AiBrain.new()
	b.configure(kind)
	return b


func _human_match(p_seed: int, ai):
	var m = GambleMatch.new()
	m.setup(p_seed, null, ai)
	return m


## 사람이 노예(암살자) 측인 판(2판)에서 시작 → 속임수 턴
func _start_cheat(m) -> void:
	m.round_index = 0
	m.start()


## seconds 동안 사람 시선을 gaze 로 두고 진행. 단계가 바뀌면 멈춤.
func _run(m, seconds: float, gaze: String) -> void:
	var steps := int(ceil(seconds / DT))
	var ph: int = m.phase
	for i in steps:
		m.tick(DT, gaze)
		if int(m.phase) != ph:
			return


func _first_event(m, type_name: String) -> Dictionary:
	for ev in m.events:
		if ev["type"] == type_name:
			return ev
	return {}


# ───────────────────────── 시험 ─────────────────────────

func _t_rules_table() -> void:
	var king: int = RankCards.Card.KING
	var cit: int = RankCards.Card.CITIZEN
	var asn: int = RankCards.Card.ASSASSIN
	_check(RankCards.resolve(king, cit) == 1 and RankCards.resolve(cit, asn) == 1 and RankCards.resolve(asn, king) == 1, "왕 > 시민 > 암살자 > 왕")
	_check(RankCards.resolve(cit, cit) == 0, "시민 = 시민")


func _t_peek_math() -> void:
	_near(CheatRules.peek_step(0.0, true, 0.9, 1.8), 0.5, 1e-9, "0.9초 보면 절반")
	_near(CheatRules.peek_step(0.5, false, 1.0, 1.8), 0.5 - CheatRules.PEEK_DECAY, 1e-9, "눈 떼면 줄어듦")
	_near(CheatRules.hazard_rate(CheatRules.HAZARD_SHINER, "face", false, 1.0), float(CheatRules.HAZARD_SHINER["face"]), 1e-9, "반사경 · 얼굴 위험률")
	_near(CheatRules.hazard_rate(CheatRules.HAZARD_SIGNAL, "behind", false, 1.0), float(CheatRules.HAZARD_SIGNAL["behind"]), 1e-9, "신호 · 뒤돌아봄 위험률")
	_near(CheatRules.hazard_rate(CheatRules.HAZARD_SHINER, "face", true, 1.0), 0.0, 1e-9, "고개 돌리는 중엔 0")


func _t_turn_roles() -> void:
	var m = _human_match(1, _brain("inert"))
	m.start()   # 1판: 사람 = 왕 측
	_check(int(m.turn_type) == GambleMatch.TurnType.DETECT and int(m.committed[1]) == -1, "왕 측 판 = 감시 턴, 내가 먼저 냄")
	_check(not bool(m.place_lighter()["ok"]), "왕 측은 라이터를 못 놓음")
	_run(m, 3.0, "shiner")
	_check(float(m.peek_progress[0]) == 0.0 and int(m.strikes[0]) == 0, "왕 측은 엿보기 없음")
	var all_detect := true
	var guard := 0
	while int(m.round_index) == 0 and guard < 60:
		guard += 1
		if int(m.turn_type) != GambleMatch.TurnType.DETECT:
			all_detect = false
		if int(m.phase) == GambleMatch.Phase.PLAYER_CHOOSE:
			m.commit(int(m.hands[0][0]))
		elif int(m.phase) == GambleMatch.Phase.AI_THINK:
			_run(m, 8.0, "table")
		elif int(m.phase) == GambleMatch.Phase.REVEALED:
			m.next()
	_check(all_detect, "1판 모든 턴 = 감시 턴")
	_check(int(m.turn_type) == GambleMatch.TurnType.CHEAT and int(m.committed[1]) != -1, "2판(노예 측) = 속임수 턴, 상대가 먼저 냄")


func _t_lighter_needed_then_reveals() -> void:
	var m = _human_match(2, _brain("inert"))   # 눈치 0 → 들키지 않음
	_start_cheat(m)
	_run(m, 2.5, "shiner")
	_check(float(m.peek_progress[0]) == 0.0 and _first_event(m, "peek_info").is_empty(), "라이터를 놓기 전엔 엿볼 수 없음")
	_check(bool(m.place_lighter()["ok"]), "라이터 놓기")
	_check(not bool(m.place_lighter()["ok"]), "판마다 한 번")
	_run(m, 1.0, "shiner")
	_check(_first_event(m, "peek_info").is_empty(), "1초로는 안 보임")
	_run(m, 1.0, "shiner")
	var ev := _first_event(m, "peek_info")
	_check(not ev.is_empty() and int(ev["card"]) == int(m.committed[1]) and str(ev["source"]) == "shiner", "1.8초 넘게 보면 반사경에 상대 카드")


func _t_caught_when_watched() -> void:
	var caught_face := 0
	var caught_away := 0
	var n := 200
	for s in n:
		var w = _brain("inert")
		w.perception = 1.0
		w.force_watch = "face"
		var m = _human_match(1000 + s, w)
		_start_cheat(m)
		m.place_lighter()
		_run(m, CheatRules.PEEK_SECONDS, "shiner")
		if int(m.strikes[0]) == 1:
			caught_face += 1
		var w2 = _brain("inert")
		w2.perception = 1.0
		w2.force_watch = "away"
		var m2 = _human_match(2000 + s, w2)
		_start_cheat(m2)
		m2.place_lighter()
		_run(m2, CheatRules.PEEK_SECONDS, "shiner")
		if int(m2.strikes[0]) == 1:
			caught_away += 1
	# 얼굴: 1 − exp(−2.0 × 1.35) ≈ 93% · 딴 곳: 1 − exp(−0.05 × 1.35) ≈ 7% (처음 0.45초는 고개 돌리는 중)
	_check(float(caught_face) / n > 0.85, "상대가 얼굴을 보면 거의 들킴 (%d/%d)" % [caught_face, n])
	_check(float(caught_away) / n < 0.15, "상대가 딴 곳을 보면 잘 안 들킴 (%d/%d)" % [caught_away, n])
	var w3 = _brain("inert")
	w3.perception = 1.0
	w3.force_watch = "face"
	var m3 = _human_match(7, w3)
	_start_cheat(m3)
	m3.place_lighter()
	_run(m3, 3.0, "shiner")
	_check(int(m3.strikes[0]) == 1 and int(m3.phase) == GambleMatch.Phase.REVEALED and not bool(m3.lighter[0]), "들키면 경고 + 판 몰수 + 라이터 몰수")


func _t_setup_seen() -> void:
	var w = _brain("honest")
	w.force_watch = "hands"
	var m = _human_match(11, w)
	_start_cheat(m)
	_run(m, 0.6, "table")   # 상대 시선이 손에 자리 잡을 때까지
	var before: float = w.suspicion
	var r: Dictionary = m.place_lighter()
	_check(bool(r["seen"]), "손을 보는 상대는 라이터 놓는 걸 봄")
	_near(float(w.suspicion) - before, float(CheatRules.SETUP_SUSPICION["lighter"]) * 1.0, 1e-9, "의심이 오름 (경고는 아님)")
	_check(int(m.strikes[0]) == 0, "준비 동작만으로는 경고 없음")


func _t_accomplice() -> void:
	var m = _human_match(12, _brain("inert"))
	_start_cheat(m)
	_check(bool(m.call_accomplice()["ok"]) and str(m.acc_state) == "walking", "협력자 부르기 → 걸어옴")
	_check(not bool(m.call_accomplice()["ok"]), "이미 부름")
	_run(m, CheatRules.ACC_WALK_SECONDS + 0.1, "table")
	_check(str(m.acc_state) == "present" and not _first_event(m, "acc_arrived").is_empty(), "상대 뒤에 섬")
	_run(m, CheatRules.SIGNAL_SECONDS + 0.1, "accomplice")
	var ev := _first_event(m, "peek_info")
	_check(not ev.is_empty() and str(ev["source"]) == "accomplice" and int(ev["card"]) == int(m.committed[1]), "손 신호로 상대 카드")
	# 상대가 뒤를 돌아보면 협력자가 들킴 → 쫓겨남
	var w = _brain("inert")
	w.perception = 1.0
	w.force_watch = "behind"
	var m2 = _human_match(13, w)
	_start_cheat(m2)
	m2.call_accomplice()
	_run(m2, CheatRules.ACC_WALK_SECONDS + 0.1, "table")
	_run(m2, 3.0, "accomplice")
	_check(int(m2.strikes[0]) == 1 and str(m2.acc_state) == "out", "뒤돌아본 상대에게 들킴 → 협력자 쫓겨남")
	m2.next()
	for i in 40:
		if int(m2.turn_type) == GambleMatch.TurnType.CHEAT and int(m2.phase) == GambleMatch.Phase.PLAYER_CHOOSE:
			break
		if int(m2.phase) == GambleMatch.Phase.PLAYER_CHOOSE:
			m2.commit(int(m2.hands[0][0]))
		elif int(m2.phase) == GambleMatch.Phase.AI_THINK:
			_run(m2, 8.0, "table")
		elif int(m2.phase) == GambleMatch.Phase.REVEALED:
			m2.next()
	_check(not bool(m2.call_accomplice()["ok"]), "쫓겨난 협력자는 다시 못 부름")


func _t_cover_blocks_shiner() -> void:
	# 상대 덮개 → 반사경 안 비침, 협력자는 됨
	var m = _human_match(14, _brain("inert"))
	_start_cheat(m)
	m._cover(1)
	m.place_lighter()
	_run(m, 3.0, "shiner")
	_check(_first_event(m, "peek_info").is_empty() and float(m.peek_progress[0]) == 0.0, "덮개가 있으면 반사경에 안 비침")
	m.call_accomplice()
	_run(m, CheatRules.ACC_WALK_SECONDS + 0.1, "table")
	_run(m, CheatRules.SIGNAL_SECONDS + 0.1, "accomplice")
	_check(str(_first_event(m, "peek_info").get("source", "")) == "accomplice", "덮개가 있어도 협력자 신호는 됨")
	# 내 덮개 → 상대가 엿보지 못함
	var b = _brain("inert")
	b.cheat_rate = 10.0
	b.boldness = 1.0
	var m2 = _human_match(15, b)
	m2.start()   # 1판: 사람 = 왕 측 · 상대(노예)가 라이터를 놓음
	_check(bool(m2.lighter[1]), "노예 측 상대가 라이터를 놓음 (보이는 준비 동작)")
	_check(bool(m2.cover_card()["ok"]), "내 카드에 덮개")
	m2.commit(int(m2.hands[0][0]))
	_run(m2, 8.0, "table")
	_check(not bool(m2.peek_done[1]) and int(m2.turn_glances) == 0, "덮개가 있으면 상대가 엿보지 않음")
	_check(int(m2.cover_left[0]) == CheatRules.COVERS_PER_MATCH - 1, "덮개 횟수 −1")


func _t_bluff_time() -> void:
	var m = _human_match(16, _brain("inert"))
	m.start()   # 1판: 감시 턴 (내가 먼저 고름)
	_near(float(m.turn_limit), CheatRules.TURN_SECONDS, 1e-9, "기본 고르는 시간")
	m.bluff()
	_near(float(m.turn_limit), CheatRules.TURN_SECONDS + CheatRules.CHOOSE_BLUFF_SECONDS, 1e-9, "블러핑 → 내 시간 +5초")
	_near(float(m.pending_time[1]), -CheatRules.THINK_BLUFF_SECONDS, 1e-9, "상대 다음 고민 −2초 대기")
	m.commit(int(m.hands[0][0]))
	_check(float(m.think_total) <= 7.0 - CheatRules.THINK_BLUFF_SECONDS + 1e-6 and float(m.pending_time[1]) == 0.0, "상대 고민 시간이 줄어 시작")
	var before: float = m.think_left
	m.bluff()
	_near(float(m.think_left), maxf(before - CheatRules.THINK_BLUFF_SECONDS, CheatRules.MIN_TIME_LEFT), 1e-9, "고민 중 블러핑 → 바로 −2초")
	_near(float(m.pending_time[0]), CheatRules.CHOOSE_BLUFF_SECONDS, 1e-9, "내 다음 고르는 시간 +5초 대기")
	m.bluff()
	_check(int(m.bluff_left[0]) == 0 and not bool(m.bluff()["ok"]), "매치 3번까지")


func _t_detect_accuse() -> void:
	var b = _brain("inert")
	b.cheat_rate = 10.0
	b.boldness = 1.0
	var m = _human_match(4, b)
	m.start()
	_check(int(m.turn_type) == GambleMatch.TurnType.DETECT and bool(m.lighter[1]), "1판(왕 측) = 감시 턴 · 상대 라이터")
	m.commit(int(m.hands[0][0]))
	var seen := false
	for i in 120:
		m.tick(DT, "face")
		if str(m.gaze[1]) == "shiner":
			seen = true
			break
	_check(seen, "상대가 반사경을 봄")
	var r: Dictionary = m.accuse()
	_check(bool(r["hit"]) and int(m.strikes[1]) == 1 and not bool(m.lighter[1]), "보는 순간 고발 = 적중 · 라이터 몰수")
	_check(int(m.phase) == GambleMatch.Phase.REVEALED and int(m.tokens[0]) == CheatRules.TOKENS_PER_MATCH, "적중이면 판 몰수 · 토큰 그대로")
	var m2 = _human_match(5, _brain("honest"))
	m2.start()
	m2.commit(int(m2.hands[0][0]))
	_run(m2, 1.0, "face")
	var r2: Dictionary = m2.accuse()
	_check(not bool(r2["hit"]) and int(m2.tokens[0]) == CheatRules.TOKENS_PER_MATCH - 1, "헛고발 → 토큰 −1")
	_check(int(m2.scores[0]) == -CheatRules.FALSE_ACCUSE_FINE and int(m2.phase) == GambleMatch.Phase.AI_THINK, "헛고발 벌금 · 턴은 계속")


func _t_ai_peek_best_response() -> void:
	var m = _human_match(6, _brain("inert"))
	m.start()   # 1판: 사람 = 왕 측, AI = 암살자 측
	m.commit(RankCards.Card.KING)
	m.peek_done[1] = true
	_run(m, 8.0, "table")
	var ev := _first_event(m, "reveal")
	_check(not ev.is_empty() and int(ev["cards"][1]) == RankCards.Card.ASSASSIN, "엿본 AI 는 왕에 암살자로 답함")


func _t_ai_ignores_hidden_card() -> void:
	var same := true
	for s in range(100, 140):
		if _ai_detect_card(s, RankCards.Card.KING) != _ai_detect_card(s, RankCards.Card.CITIZEN):
			same = false
	_check(same, "엿보지 않으면 AI 카드 = 내 카드와 무관 (40개 시드)")


func _ai_detect_card(p_seed: int, my_card: int) -> int:
	var m = _human_match(p_seed, _brain("honest"))
	m.start()
	m.commit(my_card)
	_run(m, 8.0, "table")
	var ev := _first_event(m, "reveal")
	return int(ev["cards"][1]) if not ev.is_empty() else -1


func _t_two_strikes() -> void:
	var w = _brain("inert")
	w.perception = 1.0
	w.force_watch = "face"
	var m = _human_match(8, w)
	_start_cheat(m)
	m.place_lighter()
	_run(m, 3.0, "shiner")
	_check(int(m.strikes[0]) == 1 and not m.is_over(), "한 번 들키면 계속")
	for i in 60:
		if m.is_over():
			break
		if int(m.phase) == GambleMatch.Phase.REVEALED:
			m.next()
			continue
		if int(m.turn_type) == GambleMatch.TurnType.CHEAT:
			if not bool(m.lighter[0]):
				m.place_lighter()
			_run(m, 3.0, "shiner")
		elif int(m.phase) == GambleMatch.Phase.PLAYER_CHOOSE:
			m.commit(int(m.hands[0][0]))
		else:
			_run(m, 8.0, "table")
	_check(m.is_over() and int(m.winner) == 1 and str(m.end_reason) == "CAUGHT_TWICE", "두 번 들키면 즉시 패배")


func _t_timeout() -> void:
	var m = _human_match(9, _brain("inert"))
	_start_cheat(m)
	_run(m, CheatRules.TURN_SECONDS + 0.5, "table")
	_check(not _first_event(m, "timeout").is_empty() and int(m.phase) == GambleMatch.Phase.REVEALED, "시간이 지나면 아무 카드나 냄")


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
	var e1 := _auto_events(777, "cheater", "watcher")
	var e2 := _auto_events(777, "cheater", "watcher")
	var e3 := _auto_events(778, "cheater", "watcher")
	_check(e1 == e2, "같은 시드 → 같은 매치")
	_check(e1 != e3, "다른 시드 → 다른 매치")


func _auto_events(p_seed: int, k0: String, k1: String) -> String:
	var m = GambleMatch.new()
	m.setup(p_seed, _brain(k0), _brain(k1))
	m.run_auto()
	return JSON.stringify(m.events)


func _t_auto_match_sane() -> void:
	var all_over := true
	var strikes_ok := true
	var turns_ok := true
	var caught_twice := 0
	for s in range(1, 101):
		var m = GambleMatch.new()
		m.setup(s, _brain("cheater"), _brain("cheater"))
		m.run_auto()
		if not m.is_over() or not [0, 1, 2].has(int(m.winner)):
			all_over = false
		if int(m.strikes[0]) > 2 or int(m.strikes[1]) > 2:
			strikes_ok = false
		if str(m.end_reason) == "CAUGHT_TWICE":
			caught_twice += 1
		var side0 := -1
		for ev in m.events:
			if ev["type"] == "round_start":
				side0 = int(ev["sides"][0])
			elif ev["type"] == "turn_start":
				var want: int = GambleMatch.TurnType.CHEAT if side0 == RankCards.Team.ASSASSIN_SIDE else GambleMatch.TurnType.DETECT
				if int(ev["turn_type"]) != want:
					turns_ok = false
	_check(all_over, "100 매치 모두 끝남")
	_check(strikes_ok, "경고는 2개를 넘지 않음")
	_check(turns_ok, "턴 종류 = 그 판 진영 (노예 측만 속임수)")
	print("[TEST] auto_matches=100 caught_twice=%d" % caught_twice)
