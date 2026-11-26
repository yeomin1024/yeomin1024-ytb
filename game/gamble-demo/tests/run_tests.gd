# VERSION: v0.2.0 — 2026-11-26 — 실시간 규칙 시험: 턴 번갈아 · 잔 엿보기 시간 · 들킴 위험률 · 감시 턴 고발 · 숨은 정보
# 이전 VERSION: v0.1.1 — 2026-11-26 — 전역 enum Side 와 겹치던 enum 이름을 Team 으로
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
		["fair_odds", _t_fair_odds],
		["peek_math", _t_peek_math],
		["turn_alternation", _t_turn_alternation],
		["peek_reveals_card", _t_peek_reveals_card],
		["caught_when_watched", _t_caught_when_watched],
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


func _count_events(m, type_name: String) -> int:
	var n := 0
	for ev in m.events:
		if ev["type"] == type_name:
			n += 1
	return n


# ───────────────────────── 시험 ─────────────────────────

func _t_rules_table() -> void:
	var king: int = RankCards.Card.KING
	var cit: int = RankCards.Card.CITIZEN
	var asn: int = RankCards.Card.ASSASSIN
	_check(RankCards.resolve(king, cit) == 1 and RankCards.resolve(cit, king) == -1, "왕 > 시민")
	_check(RankCards.resolve(cit, asn) == 1 and RankCards.resolve(asn, cit) == -1, "시민 > 암살자")
	_check(RankCards.resolve(asn, king) == 1 and RankCards.resolve(king, asn) == -1, "암살자 > 왕")
	_check(RankCards.resolve(cit, cit) == 0, "시민 = 시민")


func _t_fair_odds() -> void:
	var assassin := 0.0
	for t in range(1, RankCards.HAND_SIZE + 1):
		assassin += RankCards.p_fair_win_at(RankCards.Team.ASSASSIN_SIDE, t)
	_near(assassin, 0.2, 1e-9, "암살자 측 승률 = 1/5")
	var rng := RandomNumberGenerator.new()
	rng.seed = 12345
	var b = _brain("honest")
	var n := 20000
	var wins := 0
	for i in n:
		var hk := RankCards.new_hand(RankCards.Team.KING_SIDE)
		var ha := RankCards.new_hand(RankCards.Team.ASSASSIN_SIDE)
		for t in RankCards.HAND_SIZE:
			var ck: int = b.choose_card(rng, hk, RankCards.Team.KING_SIDE, {})
			var ca: int = b.choose_card(rng, ha, RankCards.Team.ASSASSIN_SIDE, {})
			hk.erase(ck)
			ha.erase(ca)
			var r := RankCards.resolve(ck, ca)
			if r != 0:
				if r < 0:
					wins += 1
				break
	_near(float(wins) / n, 0.2, 0.015, "AI 무작위 선택 = 공정 분포")


func _t_peek_math() -> void:
	_near(CheatRules.peek_step(0.0, true, 0.9, 1.8), 0.5, 1e-9, "0.9초 보면 절반")
	_near(CheatRules.peek_step(0.5, false, 1.0, 1.8), 0.5 - CheatRules.PEEK_DECAY, 1e-9, "눈 떼면 줄어듦")
	_near(CheatRules.peek_step(0.95, true, 1.0, 1.8), 1.0, 1e-9, "1 을 넘지 않음")
	_near(CheatRules.hazard_rate("face", false, 1.0), float(CheatRules.HAZARD["face"]), 1e-9, "얼굴을 보면 위험률 = HAZARD.face")
	_near(CheatRules.hazard_rate("face", true, 1.0), 0.0, 1e-9, "고개 돌리는 중엔 0")
	_near(CheatRules.notice_chance(2.0, 0.5), 1.0 - exp(-1.0), 1e-9, "알아챌 확률 공식")
	_near(CheatRules.p_at_least(2, 5, 0.3), 0.47178, 1e-5, "5번 속이면 2번 이상 들킬 확률")


func _t_turn_alternation() -> void:
	var m = _human_match(1, _brain("inert"))
	m.start()
	_check(int(m.turn_type) == GambleMatch.TurnType.CHEAT and int(m.committed[1]) != -1, "1턴 = 속임수 턴, 상대가 먼저 냄")
	_check(int(m.phase) == GambleMatch.Phase.PLAYER_CHOOSE, "1턴 내가 고름")
	m.commit(RankCards.Card.CITIZEN)
	_check(int(m.phase) == GambleMatch.Phase.REVEALED, "속임수 턴은 내가 내면 바로 공개")
	m.next()
	_check(int(m.turn_type) == GambleMatch.TurnType.DETECT and int(m.committed[1]) == -1, "2턴 = 감시 턴, 상대는 아직 안 냄")
	m.commit(int(m.hands[0][0]))
	_check(int(m.phase) == GambleMatch.Phase.AI_THINK, "감시 턴은 내가 낸 뒤 상대가 고민")
	_run(m, 8.0, "table")
	_check(int(m.phase) == GambleMatch.Phase.REVEALED and int(m.committed[1]) != -1, "고민이 끝나면 상대가 내고 공개")


func _t_peek_reveals_card() -> void:
	var m = _human_match(2, _brain("inert"))   # 눈치 0 → 들키지 않음
	m.start()
	_run(m, 1.0, "glass")
	_check(_first_event(m, "peek_info").is_empty(), "1초로는 안 보임")
	_run(m, 1.0, "glass")
	var ev := _first_event(m, "peek_info")
	_check(not ev.is_empty() and int(ev["card"]) == int(m.committed[1]), "1.8초 넘게 보면 상대 카드가 비침")
	# 나눠 보기: 1초 보고 1초 쉬고 → 진행도가 줄어든 만큼 더 봐야 함
	var m2 = _human_match(3, _brain("inert"))
	m2.start()
	_run(m2, 1.0, "glass")
	_run(m2, 1.0, "table")
	var want := 1.0 / CheatRules.PEEK_SECONDS - CheatRules.PEEK_DECAY
	_near(float(m2.peek_progress[0]), want, 0.04, "쉬면 줄어듦")


func _t_caught_when_watched() -> void:
	var caught_face := 0
	var caught_away := 0
	var n := 200
	for s in n:
		var w = _brain("honest")
		w.force_watch = "face"
		var m = _human_match(1000 + s, w)
		m.start()
		_run(m, CheatRules.PEEK_SECONDS, "glass")
		if int(m.strikes[0]) == 1:
			caught_face += 1
		var w2 = _brain("honest")
		w2.force_watch = "away"
		var m2 = _human_match(2000 + s, w2)
		m2.start()
		_run(m2, CheatRules.PEEK_SECONDS, "glass")
		if int(m2.strikes[0]) == 1:
			caught_away += 1
	# 얼굴: 1 − exp(−2.0 × 1.35) ≈ 93% · 딴 곳: 1 − exp(−0.05 × 1.35) ≈ 7% (처음 0.45초는 고개 돌리는 중)
	_check(float(caught_face) / n > 0.85, "상대가 얼굴을 보면 거의 들킴 (%d/%d)" % [caught_face, n])
	_check(float(caught_away) / n < 0.15, "상대가 딴 곳을 보면 잘 안 들킴 (%d/%d)" % [caught_away, n])
	var w3 = _brain("honest")
	w3.force_watch = "face"
	var m3 = _human_match(7, w3)
	m3.start()
	_run(m3, 3.0, "glass")
	_check(int(m3.strikes[0]) == 1 and int(m3.phase) == GambleMatch.Phase.REVEALED and bool(m3.round_over), "들키면 경고 + 판 몰수")
	var a := _first_event(m3, "accuse")
	_check(not a.is_empty() and int(a["accuser"]) == 1 and str(a["by"]) == "notice", "상대가 알아챈 고발")


func _t_detect_accuse() -> void:
	# 상대가 늘 엿봄 → 잔을 보는 순간 고발하면 적중
	var b = _brain("inert")
	b.cheat_rate = 10.0
	b.boldness = 1.0
	var m = _human_match(4, b)
	m.global_turn = 1   # 첫 턴을 감시 턴(2)으로
	m.start()
	_check(int(m.turn_type) == GambleMatch.TurnType.DETECT, "감시 턴에서 시작")
	m.commit(int(m.hands[0][0]))
	var seen := false
	for i in 120:
		m.tick(DT, "face")
		if str(m.gaze[1]) == "glass":
			seen = true
			break
	_check(seen, "상대가 잔을 봄")
	var r: Dictionary = m.accuse()
	_check(bool(r["hit"]) and int(m.strikes[1]) == 1, "잔을 보는 순간 고발 = 적중")
	_check(int(m.phase) == GambleMatch.Phase.REVEALED and int(m.tokens[0]) == CheatRules.TOKENS_PER_MATCH, "적중이면 판 몰수 · 토큰 그대로")
	# 정직한 상대에게 고발 → 헛고발
	var m2 = _human_match(5, _brain("honest"))
	m2.global_turn = 1
	m2.start()
	m2.commit(int(m2.hands[0][0]))
	_run(m2, 1.0, "face")
	var r2: Dictionary = m2.accuse()
	_check(not bool(r2["hit"]) and int(m2.tokens[0]) == CheatRules.TOKENS_PER_MATCH - 1, "헛고발 → 토큰 −1")
	_check(int(m2.scores[0]) == -CheatRules.FALSE_ACCUSE_FINE and int(m2.phase) == GambleMatch.Phase.AI_THINK, "헛고발 벌금 · 턴은 계속")
	_check(not bool(m2.commit(RankCards.Card.CITIZEN)["ok"]), "고민 중엔 카드 못 냄")


func _t_ai_peek_best_response() -> void:
	var m = _human_match(6, _brain("inert"))
	m.global_turn = 1
	m.start()   # 1판: 사람 = 왕 측, AI = 암살자 측
	m.commit(RankCards.Card.KING)
	m.peek_done[1] = true   # 엿보기를 끝냈다고 가정
	_run(m, 8.0, "table")
	var ev := _first_event(m, "reveal")
	_check(not ev.is_empty() and int(ev["cards"][1]) == RankCards.Card.ASSASSIN, "엿본 AI 는 왕에 암살자로 답함")
	_check(int(m.scores[1]) == int(RankCards.WIN_POINTS[RankCards.Team.ASSASSIN_SIDE]), "암살자 측 +4")


## 엿보지 않은 AI 의 카드는 사람 카드와 무관해야 함 (숨은 정보를 몰래 읽지 않음)
func _t_ai_ignores_hidden_card() -> void:
	var same := true
	for s in range(100, 140):
		if _ai_detect_card(s, RankCards.Card.KING) != _ai_detect_card(s, RankCards.Card.CITIZEN):
			same = false
	_check(same, "엿보지 않으면 AI 카드 = 내 카드와 무관 (40개 시드)")


func _ai_detect_card(p_seed: int, my_card: int) -> int:
	var m = _human_match(p_seed, _brain("honest"))
	m.global_turn = 1
	m.start()
	m.commit(my_card)
	_run(m, 8.0, "table")
	var ev := _first_event(m, "reveal")
	return int(ev["cards"][1]) if not ev.is_empty() else -1


func _t_two_strikes() -> void:
	var w = _brain("honest")
	w.force_watch = "face"
	var m = _human_match(8, w)
	m.start()
	_run(m, 3.0, "glass")
	_check(int(m.strikes[0]) == 1 and not m.is_over(), "한 번 들키면 계속")
	for i in 40:
		if m.is_over():
			break
		if int(m.phase) == GambleMatch.Phase.REVEALED:
			m.next()
			continue
		if int(m.turn_type) == GambleMatch.TurnType.CHEAT:
			_run(m, 3.0, "glass")   # 다시 잔을 봄
		elif int(m.phase) == GambleMatch.Phase.PLAYER_CHOOSE:
			m.commit(int(m.hands[0][0]))
		else:
			_run(m, 8.0, "table")
	_check(m.is_over() and int(m.winner) == 1 and str(m.end_reason) == "CAUGHT_TWICE", "두 번 들키면 즉시 패배")
	_check(not bool(m.commit(RankCards.Card.CITIZEN)["ok"]), "끝난 뒤 카드 거절")


func _t_timeout() -> void:
	var m = _human_match(9, _brain("inert"))
	m.start()
	_run(m, CheatRules.TURN_SECONDS + 0.5, "table")
	_check(not _first_event(m, "timeout").is_empty() and int(m.phase) == GambleMatch.Phase.REVEALED, "시간이 지나면 아무 카드나 냄")
	_check(int(m.stats["timeouts"][0]) == 1, "시간 초과 기록")


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
	var caught_twice := 0
	var turns_ok := true
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
		for ev in m.events:
			if ev["type"] == "turn_start":
				var want: int = GambleMatch.TurnType.CHEAT if int(ev["turn"]) % 2 == 1 else GambleMatch.TurnType.DETECT
				if int(ev["turn_type"]) != want:
					turns_ok = false
	_check(all_over, "100 매치 모두 끝남")
	_check(strikes_ok, "경고는 2개를 넘지 않음")
	_check(turns_ok, "턴 종류가 번갈아 감")
	print("[TEST] auto_matches=100 caught_twice=%d" % caught_twice)
