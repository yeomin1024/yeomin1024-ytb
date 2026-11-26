# VERSION: v0.1.0 — 2026-11-26 — 핵심 규칙 시험 (화면 없이)
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

var _passes := 0
var _fails := 0


func _initialize() -> void:
	GameLog.level = GameLog.Level.ERROR   # 시험 중 거절(REFUSE) 경고는 일부러 내는 것이라 숨김
	var tests: Array = [
		["rules_table", _t_rules_table],
		["fair_odds_analytic", _t_fair_odds_analytic],
		["fair_odds_montecarlo", _t_fair_odds_montecarlo],
		["tell_formula", _t_tell_formula],
		["binomial_claim", _t_binomial_claim],
		["accuse_hit", _t_accuse_hit],
		["evidence_expiry_and_false_accuse", _t_evidence_expiry_and_false_accuse],
		["two_strikes", _t_two_strikes],
		["mark_persists_then_confiscated", _t_mark_persists_then_confiscated],
		["ai_ignores_hidden_card", _t_ai_ignores_hidden_card],
		["ai_late_peek", _t_ai_late_peek],
		["ai_bayes", _t_ai_bayes],
		["determinism", _t_determinism],
		["tiebreak", _t_tiebreak],
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


func _human_match(p_seed: int, ai_kind: String):
	var m = GambleMatch.new()
	m.setup(p_seed, null, _brain(ai_kind))
	return m


func _first_event(m, type_name: String) -> Dictionary:
	for ev in m.events:
		if ev["type"] == type_name:
			return ev
	return {}


func _last_event(m, type_name: String) -> Dictionary:
	var found := {}
	for ev in m.events:
		if ev["type"] == type_name:
			found = ev
	return found


# ───────────────────────── 시험 ─────────────────────────

func _t_rules_table() -> void:
	var king: int = RankCards.Card.KING
	var cit: int = RankCards.Card.CITIZEN
	var asn: int = RankCards.Card.ASSASSIN
	_check(RankCards.resolve(king, cit) == 1, "왕 > 시민")
	_check(RankCards.resolve(cit, king) == -1, "시민 < 왕")
	_check(RankCards.resolve(cit, asn) == 1, "시민 > 암살자")
	_check(RankCards.resolve(asn, cit) == -1, "암살자 < 시민")
	_check(RankCards.resolve(asn, king) == 1, "암살자 > 왕")
	_check(RankCards.resolve(king, asn) == -1, "왕 < 암살자")
	_check(RankCards.resolve(cit, cit) == 0, "시민 = 시민")
	var hk := RankCards.new_hand(RankCards.Side.KING_SIDE)
	var ha := RankCards.new_hand(RankCards.Side.ASSASSIN_SIDE)
	_check(hk.size() == 5 and hk.count(cit) == 4 and hk.has(king), "왕 측 패 = 시민 4 + 왕")
	_check(ha.size() == 5 and ha.count(cit) == 4 and ha.has(asn), "암살자 측 패 = 시민 4 + 암살자")


func _t_fair_odds_analytic() -> void:
	var total := 0.0
	var assassin := 0.0
	for t in range(1, RankCards.HAND_SIZE + 1):
		var pa := RankCards.p_fair_win_at(RankCards.Side.ASSASSIN_SIDE, t)
		assassin += pa
		total += pa + RankCards.p_fair_win_at(RankCards.Side.KING_SIDE, t)
	_near(total, 1.0, 1e-9, "공정 결과 확률 합 = 1")
	_near(assassin, 0.2, 1e-9, "암살자 측 승률 = 1/5")
	var ev_king: float = (1.0 - assassin) * int(RankCards.WIN_POINTS[RankCards.Side.KING_SIDE])
	var ev_assassin: float = assassin * int(RankCards.WIN_POINTS[RankCards.Side.ASSASSIN_SIDE])
	_near(ev_king, ev_assassin, 1e-9, "두 진영 기대 점수가 같음 (0.8)")


## AI 의 '정보 없을 때' 카드 선택이 무작위 순서와 같은 분포인지 (특수 카드 턴이 1~5 균등)
func _t_fair_odds_montecarlo() -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = 12345
	var b = _brain("honest")
	var n := 20000
	var assassin_wins := 0
	for i in n:
		var hk := RankCards.new_hand(RankCards.Side.KING_SIDE)
		var ha := RankCards.new_hand(RankCards.Side.ASSASSIN_SIDE)
		for t in RankCards.HAND_SIZE:
			var ck: int = b.choose_card(rng, hk, RankCards.Side.KING_SIDE, {})
			var ca: int = b.choose_card(rng, ha, RankCards.Side.ASSASSIN_SIDE, {})
			hk.erase(ck)
			ha.erase(ca)
			var r := RankCards.resolve(ck, ca)
			if r != 0:
				if r < 0:
					assassin_wins += 1
				break
	_near(float(assassin_wins) / n, 0.2, 0.015, "무작위 대 무작위 암살자 측 승률")
	var king_turn := [0, 0, 0, 0, 0]
	for i in n:
		var h := RankCards.new_hand(RankCards.Side.KING_SIDE)
		for t in RankCards.HAND_SIZE:
			var c: int = b.choose_card(rng, h, RankCards.Side.KING_SIDE, {})
			h.erase(c)
			if c == RankCards.Card.KING:
				king_turn[t] += 1
				break
	for t in RankCards.HAND_SIZE:
		_near(float(king_turn[t]) / n, 0.2, 0.015, "왕이 %d턴에 나올 확률" % (t + 1))


func _t_tell_formula() -> void:
	# 0.45 × (1 − 0.6×0.8) × 1.5 = 0.351
	_near(CheatRules.compute_tell(0.45, 0.8, true, 0, 0), 0.351, 1e-9, "엿보기·손기술 0.8·손을 봄")
	_near(CheatRules.compute_tell(0.45, 0.8, false, 0, 0), 0.117, 1e-9, "얼굴을 봄 → 3분의 1")
	# 반복 2번(+50%) · 낙인(×1.3) → 0.351 × 1.5 × 1.3
	_near(CheatRules.compute_tell(0.45, 0.8, true, 2, 1), 0.68445, 1e-9, "반복·낙인 가중")
	_near(CheatRules.compute_tell(0.9, 0.0, true, 3, 1), 1.0, 1e-9, "1 을 넘으면 1")
	_near(CheatRules.notice_probability(0.351, 1.0), 1.0 - exp(-0.702), 1e-9, "알아챌 확률 공식")
	_near(CheatRules.notice_probability(0.351, 0.0), 0.0, 1e-9, "주의력 0 이면 못 봄")


## 설계 문서 숫자: 한 번마다 걸릴 확률 0.3 → 5번 속이면 2번 이상 들킬 확률 47.2%, 3번이면 21.6%
func _t_binomial_claim() -> void:
	_near(CheatRules.p_at_least(2, 5, 0.3), 0.47178, 1e-5, "5번 시도")
	_near(CheatRules.p_at_least(2, 3, 0.3), 0.216, 1e-9, "3번 시도")
	var rng := RandomNumberGenerator.new()
	rng.seed = 99
	var n := 20000
	var lost := 0
	for i in n:
		var caught := 0
		for k in 5:
			if rng.randf() < 0.3:
				caught += 1
		if caught >= 2:
			lost += 1
	_near(float(lost) / n, 0.47178, 0.015, "몬테카를로 5번 시도")


func _t_accuse_hit() -> void:
	var m = _human_match(1, "inert")
	m.start()
	_check(m.phase == GambleMatch.Phase.CHOOSE, "시작하면 CHOOSE")
	_check(m.cheat(0, "peek", 1.0)["ok"], "엿보기 실행")
	_check(not _first_event(m, "peek_info").is_empty(), "엿보기 정보 이벤트")
	_check(m.evidence.size() == 1 and int(m.evidence[0]["expires"]) == m.global_turn + 1, "엿보기 증거 = 다음 턴까지")
	var a: Dictionary = m.accuse(1)
	_check(bool(a["hit"]), "증거가 있으면 적중")
	_check(m.strikes[0] == 1, "경고 1")
	_check(m.evidence.is_empty(), "증거 몰수")
	_check(m.tokens[1] == CheatRules.TOKENS_PER_MATCH, "적중이면 토큰 그대로")
	# 1판: 자리 0 = 왕 측, 자리 1 = 암살자 측 → 몰수 점수 4 + 들킨 벌금
	var want1 := int(RankCards.WIN_POINTS[RankCards.Side.ASSASSIN_SIDE]) + CheatRules.CAUGHT_FINE
	_check(m.scores[1] == want1 and m.scores[0] == -CheatRules.CAUGHT_FINE, "판 몰수 + 벌금")
	_check(m.phase == GambleMatch.Phase.REVEALED and m.round_over, "판 끝")
	_check(not m.cheat(0, "fake", 0.5)["ok"], "판이 끝나면 속임수 거절")


func _t_evidence_expiry_and_false_accuse() -> void:
	var m = _human_match(2, "inert")
	m.start()
	m.cheat(0, "peek", 1.0)
	m.global_turn += 2   # 증거(다음 턴까지)가 사라질 만큼 시간이 흘렀다고 가정
	var a: Dictionary = m.accuse(1)
	_check(not bool(a["hit"]), "증거가 사라지면 헛고발")
	_check(m.tokens[1] == CheatRules.TOKENS_PER_MATCH - 1, "헛고발 → 토큰 −1")
	_check(m.scores[1] == -CheatRules.FALSE_ACCUSE_FINE and m.scores[0] == CheatRules.FALSE_ACCUSE_FINE, "벌금이 상대에게")
	_check(m.strikes[0] == 0, "헛고발은 경고 없음")
	_check(m.phase == GambleMatch.Phase.CHOOSE, "헛고발은 판을 끝내지 않음")
	var m2 = _human_match(3, "inert")
	m2.start()
	m2.cheat(0, "fake", 0.0)
	_check(m2.evidence.is_empty(), "가짜 동작은 증거 없음")
	_check(not bool(m2.accuse(1)["hit"]), "가짜 동작을 고발하면 헛고발")
	m2.accuse(1)
	m2.accuse(1)
	_check(m2.tokens[1] == 0 and not bool(m2.accuse(1)["ok"]), "토큰 0 → 고발 거절")


func _t_two_strikes() -> void:
	var m = _human_match(4, "inert")
	m.start()
	m.cheat(0, "peek", 1.0)
	m.accuse(1)
	_check(m.strikes[0] == 1 and not m.is_over(), "한 번 들키면 계속")
	m.next()
	_check(m.round_index == 1 and m.phase == GambleMatch.Phase.CHOOSE, "다음 판으로")
	_check(m.cheat(0, "peek", 1.0)["ok"], "두 번째 엿보기")
	var ev := _last_event(m, "cheat")
	_near(float(ev["tell"]), CheatRules.compute_tell(0.45, 1.0, bool(ev["watched"]), 1, 1), 1e-9, "두 번째 단서 = 반복 + 낙인 공식")
	var a: Dictionary = m.accuse(1)
	_check(bool(a["hit"]) and m.strikes[0] == 2, "경고 2")
	_check(m.is_over() and m.winner == 1 and m.end_reason == "CAUGHT_TWICE", "두 번 들키면 즉시 패배")
	_check(not m.commit(RankCards.Card.CITIZEN)["ok"], "끝난 뒤 카드 거절")
	_check(not _last_event(m, "match_end").is_empty(), "매치 끝 이벤트")


func _t_mark_persists_then_confiscated() -> void:
	var m = _human_match(5, "inert")
	m.start()
	_check(m.cheat(0, "mark", 0.5)["ok"], "뒷면 표시")
	_check(_last_event(m, "mark_info").is_empty(), "표시는 다음 턴부터")
	_check(not m.cheat(0, "mark", 0.5)["ok"], "뒷면 표시는 매치당 1번")
	# 턴을 넘기며 표시 정보가 맞는지 (보인 턴만)
	var seen := 0
	var shown := 0
	var correct := true
	for i in 12:
		var card: int = RankCards.Card.CITIZEN if m.hands[0].has(RankCards.Card.CITIZEN) else int(m.hands[0][0])
		m.commit(card)
		m.next()
		if m.is_over():
			break
		var ev := _last_event(m, "mark_info")
		if ev.is_empty() or int(ev["turn"]) != m.global_turn:
			correct = false   # 표시가 있으면 턴마다 보였든 아니든 이벤트가 있어야 함
			continue
		shown += 1
		if bool(ev["seen"]):
			seen += 1
			if bool(ev["special"]) != (m.tentative_ai_card != RankCards.Card.CITIZEN):
				correct = false
	_check(correct and shown > 0 and seen > 0 and seen <= shown, "표시 정보 = 상대 카드가 특수인지 (보인 %d / %d턴)" % [seen, shown])
	m.global_turn += 20
	var a: Dictionary = m.accuse(1)
	_check(bool(a["hit"]) and a["found"].has("mark"), "뒷면 표시 증거는 매치 끝까지")
	_check(not m.marked[0], "들키면 표시 카드 몰수")
	_check(not bool(m.accuse(1)["hit"]), "같은 증거로 두 번 경고하지 않음")
	_check(m.strikes[0] == 1, "경고는 1개만")


## 엿보지 않은 AI 의 카드는 사람 카드와 무관해야 함 (숨은 정보를 몰래 읽지 않음)
func _t_ai_ignores_hidden_card() -> void:
	var same := true
	for s in range(100, 160):
		if _ai_first_card(s, RankCards.Card.KING) != _ai_first_card(s, RankCards.Card.CITIZEN):
			same = false
	_check(same, "엿보지 않으면 AI 카드 = 내 카드와 무관 (60개 시드)")


func _ai_first_card(p_seed: int, my_card: int) -> int:
	var m = _human_match(p_seed, "honest")
	m.start()
	m.commit(my_card)
	var ev := _first_event(m, "reveal")
	return int(ev["cards"][1]) if not ev.is_empty() else -1


func _t_ai_late_peek() -> void:
	var b = _brain("inert")
	b.cheat_rate = 10.0   # 늘 엿봄
	var m = GambleMatch.new()
	m.setup(6, null, b)
	m.start()
	_check(m.ai_late_peek, "AI 가 엿봄")
	_check(not _first_event(m, "tell").is_empty(), "사람에게 단서 이벤트 (알아챘든 못 했든)")
	m.commit(RankCards.Card.KING)
	var ev := _first_event(m, "reveal")
	_check(int(ev["cards"][1]) == RankCards.Card.ASSASSIN, "엿본 AI 는 왕에 암살자로 답함")
	_check(m.scores[1] == int(RankCards.WIN_POINTS[RankCards.Side.ASSASSIN_SIDE]), "암살자 측 +4")
	# 사람이 바로 고발하면 적중 · AI 엿보기 취소 · 판 몰수
	var b2 = _brain("inert")
	b2.cheat_rate = 10.0
	var m2 = GambleMatch.new()
	m2.setup(7, null, b2)
	m2.start()
	var a: Dictionary = m2.accuse(0)
	_check(bool(a["hit"]) and m2.strikes[1] == 1 and not m2.ai_late_peek, "AI 엿보기 적발")
	_check(m2.scores[0] == int(RankCards.WIN_POINTS[RankCards.Side.KING_SIDE]) + CheatRules.CAUGHT_FINE, "몰수 + 벌금 → 사람 +2")


func _t_ai_bayes() -> void:
	var b = _brain("honest")   # 의심 성향 1.0
	_near(b.on_round_result(true, RankCards.Side.ASSASSIN_SIDE, 3), log(3.0), 1e-9, "상대가 암살자 측으로 이기면 +ln 3")
	_near(b.on_round_result(true, RankCards.Side.KING_SIDE, 1), log(2.0625), 1e-9, "상대가 왕 측으로 첫 턴에 이기면 +ln 2.0625")
	_near(b.on_round_result(true, RankCards.Side.KING_SIDE, 3), log(0.5), 1e-9, "왕 측이 늦게 이기면 ln 0.5")
	_near(b.on_round_result(false, RankCards.Side.KING_SIDE, 2), log(0.5), 1e-9, "상대가 지면 ln 0.5")
	var b2 = _brain("honest")
	_check(not b2.should_accuse(3), "처음엔 고발 안 함")
	b2.suspicion = 0.7   # 문턱: 토큰 3 → 0.0 · 토큰 1 → 1.0
	_check(b2.should_accuse(3) and not b2.should_accuse(1) and not b2.should_accuse(0), "토큰이 적을수록 신중 · 0 이면 못 함")


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


## 6판 뒤 동점이면 연장, 연장에서 갈리면 끝
func _t_tiebreak() -> void:
	var m = GambleMatch.new()
	m.setup(8, _brain("honest"), _brain("honest"))
	m.round_index = GambleMatch.ROUNDS - 1
	m.scores = [3, 3]
	m.round_over = true
	m.phase = GambleMatch.Phase.REVEALED
	m.next()
	_check(m.round_index == GambleMatch.ROUNDS and not m.is_over(), "동점 → 연장 1판")
	m.scores = [5, 4]
	m.round_over = true
	m.phase = GambleMatch.Phase.REVEALED
	m.next()
	_check(m.is_over() and m.winner == 0 and m.end_reason == "SCORE", "연장에서 갈리면 끝")
	var m2 = GambleMatch.new()
	m2.setup(9, _brain("honest"), _brain("honest"))
	m2.round_index = GambleMatch.ROUNDS + GambleMatch.EXTRA_ROUNDS - 1
	m2.scores = [2, 2]
	m2.round_over = true
	m2.phase = GambleMatch.Phase.REVEALED
	m2.next()
	_check(m2.is_over() and m2.winner == 2, "연장을 다 해도 같으면 무승부")


func _t_auto_match_sane() -> void:
	var all_over := true
	var strikes_ok := true
	var reason_ok := true
	var caught_twice := 0
	for s in range(1, 301):
		var m = GambleMatch.new()
		m.setup(s, _brain("cheater"), _brain("watcher"))
		m.run_auto()
		if not m.is_over() or not [0, 1, 2].has(m.winner):
			all_over = false
		if m.strikes[0] > 2 or m.strikes[1] > 2:
			strikes_ok = false
		if m.end_reason == "CAUGHT_TWICE":
			caught_twice += 1
			if m.strikes[1 - m.winner] != 2:
				reason_ok = false
		elif m.end_reason != "SCORE":
			reason_ok = false
	_check(all_over, "300 매치 모두 끝남")
	_check(strikes_ok, "경고는 2개를 넘지 않음")
	_check(reason_ok, "끝난 이유와 경고 수가 맞음")
	print("[TEST] auto_matches=300 caught_twice=%d" % caught_twice)
