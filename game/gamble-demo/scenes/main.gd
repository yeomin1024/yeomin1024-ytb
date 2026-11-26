# VERSION: v0.1.1 — 2026-11-26 — 속임수 버튼 줄의 타입 추론 오류 고침(INFERENCE_ON_VARIANT) · Side→Team
# 이전 VERSION: v0.1.0 — 2026-11-26 — 데모 화면: 카드 · 속임수(손기술 QTE) · 고발 · 시선 · 기록 · 판 끝 리플레이 · 연장 표시
#
# 화면은 코드로 만듦 (씬 파일은 루트 하나) — 규칙은 모두 core/match.gd 에 있고 여기선 보여 주기만.
# 연구·교육용 데모 — 실제 돈과 관계없음.
extends Control

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const AiBrain = preload("res://core/ai_brain.gd")
const GambleMatch = preload("res://core/match.gd")
const GameLog = preload("res://core/game_log.gd")

const OPPONENTS := ["cheater", "watcher", "bluffer"]
const OPP_NAMES := {"cheater": "손버릇 나쁜 딜러", "watcher": "눈이 매서운 노인", "bluffer": "허세꾼"}
const QTE_TIMEOUT := 2.5   # 초 — 안 누르면 손기술 0 (단서 최대)
const QTE_SPEED := 1.1     # 막대 왕복 횟수/초

var game = null
var opponent_kind := "cheater"
var round_secrets: Array = []   # 이번 판 상대 속임수 (판 끝 리플레이용 — 진행 중엔 안 보임)

var status_label: Label
var gaze_label: Label
var hand_box: HBoxContainer
var cheat_box: HBoxContainer
var accuse_btn: Button
var next_btn: Button
var gaze_hands_btn: Button
var gaze_face_btn: Button
var opp_option: OptionButton
var qte_panel: PanelContainer
var qte_bar: ProgressBar
var qte_label: Label
var log_view: RichTextLabel

var qte_active := false
var qte_kind := ""
var qte_t := 0.0


func _ready() -> void:
	_build_ui()
	_new_match()


# ───────────────────────── 화면 만들기 ─────────────────────────

func _build_ui() -> void:
	set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var bg := ColorRect.new()
	bg.color = Color(0.07, 0.10, 0.08)
	bg.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	add_child(bg)
	var margin := MarginContainer.new()
	margin.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	for edge in ["left", "right", "top", "bottom"]:
		margin.add_theme_constant_override("margin_" + edge, 18)
	add_child(margin)
	var col := VBoxContainer.new()
	col.add_theme_constant_override("separation", 10)
	margin.add_child(col)

	var top := HBoxContainer.new()
	col.add_child(top)
	top.add_child(_label("상대:"))
	opp_option = OptionButton.new()
	for k in OPPONENTS:
		opp_option.add_item(OPP_NAMES[k])
	opp_option.add_theme_font_size_override("font_size", 18)
	top.add_child(opp_option)
	top.add_child(_button("새 매치", _on_new_match))
	top.add_child(_label("   규칙: 왕 > 시민 > 암살자 > 왕 · 시민끼리는 비김 · 경고 2개면 패배", 16))

	status_label = _label("", 22)
	col.add_child(status_label)
	gaze_label = _label("", 18)
	col.add_child(gaze_label)

	var gaze_row := HBoxContainer.new()
	col.add_child(gaze_row)
	gaze_row.add_child(_label("내 시선 (다음 턴부터):"))
	gaze_hands_btn = _button("상대 손 보기 — 속임수가 잘 보임", _on_gaze.bind("hands"))
	gaze_face_btn = _button("상대 얼굴 보기 — 표정이 보임", _on_gaze.bind("face"))
	gaze_row.add_child(gaze_hands_btn)
	gaze_row.add_child(gaze_face_btn)

	col.add_child(_label("내 패 (눌러서 내기):"))
	hand_box = HBoxContainer.new()
	hand_box.add_theme_constant_override("separation", 8)
	col.add_child(hand_box)

	col.add_child(_label("속임수 (누르면 손기술 막대):"))
	cheat_box = HBoxContainer.new()
	cheat_box.add_theme_constant_override("separation", 8)
	col.add_child(cheat_box)

	var act := HBoxContainer.new()
	act.add_theme_constant_override("separation", 8)
	col.add_child(act)
	accuse_btn = _button("잡았다! (고발)", _on_accuse)
	next_btn = _button("다음 ▶", _on_next)
	act.add_child(accuse_btn)
	act.add_child(next_btn)

	qte_panel = PanelContainer.new()
	col.add_child(qte_panel)
	var qv := VBoxContainer.new()
	qte_panel.add_child(qv)
	qte_label = _label("", 18)
	qv.add_child(qte_label)
	qte_bar = ProgressBar.new()
	qte_bar.min_value = 0.0
	qte_bar.max_value = 100.0
	qte_bar.show_percentage = false
	qte_bar.custom_minimum_size = Vector2(640, 28)
	qv.add_child(qte_bar)
	qv.add_child(_button("지금! (스페이스)", _on_qte_press))
	qte_panel.visible = false

	log_view = RichTextLabel.new()
	log_view.bbcode_enabled = true
	log_view.scroll_following = true
	log_view.size_flags_vertical = Control.SIZE_EXPAND_FILL
	log_view.add_theme_font_size_override("normal_font_size", 17)
	log_view.add_theme_font_size_override("bold_font_size", 17)
	col.add_child(log_view)


func _label(text: String, font_size: int = 18) -> Label:
	var l := Label.new()
	l.text = text
	l.add_theme_font_size_override("font_size", font_size)
	return l


func _button(text: String, cb: Callable) -> Button:
	var b := Button.new()
	b.text = text
	b.add_theme_font_size_override("font_size", 18)
	b.pressed.connect(cb)
	return b


# ───────────────────────── 매치 ─────────────────────────

func _on_new_match() -> void:
	opponent_kind = OPPONENTS[opp_option.selected]
	_new_match()


func _new_match() -> void:
	qte_active = false
	qte_panel.visible = false
	var brain = AiBrain.new()
	brain.configure(opponent_kind)
	game = GambleMatch.new()
	var s := int(Time.get_unix_time_from_system()) % 1000000
	game.setup(s, null, brain)
	game.gaze[0] = "face"
	round_secrets.clear()
	log_view.clear()
	_log("[b]새 매치[/b] — 상대: %s · 시드 %d · %d판(동점이면 연장 최대 %d판) · 경고 %d개면 패배 · 고발 토큰 %d개" % [
		OPP_NAMES[opponent_kind], s, GambleMatch.ROUNDS, GambleMatch.EXTRA_ROUNDS, CheatRules.STRIKES_TO_LOSE,
		CheatRules.TOKENS_PER_MATCH])
	_log("들키면: 그 판 몰수 + 벌금 %d점 · 헛고발: 토큰 −1 + 벌금 %d점" % [CheatRules.CAUGHT_FINE, CheatRules.FALSE_ACCUSE_FINE])
	_log("[color=gray]연구·교육용 데모입니다. 실제 돈과 관계없습니다.[/color]")
	game.start()
	_drain_events()
	_refresh()


func _on_gaze(where: String) -> void:
	game.gaze[0] = where
	_refresh()


func _on_card(card: int) -> void:
	if qte_active:
		return
	game.commit(card)
	_after_action()


func _on_cheat(kind: String) -> void:
	if qte_active or game.phase != GambleMatch.Phase.CHOOSE:
		return
	qte_active = true
	qte_kind = kind
	qte_t = 0.0
	qte_label.text = "%s — 막대가 가운데 올 때 누르세요 (가운데일수록 단서가 작음)" % CheatRules.CHEATS[kind]["name"]
	qte_panel.visible = true
	_refresh()


func _on_accuse() -> void:
	if qte_active:
		return
	game.accuse(0)
	_after_action()


func _on_next() -> void:
	if qte_active:
		return
	game.next()
	_after_action()


func _after_action() -> void:
	_drain_events()
	_refresh()


# ───────────────────────── 손기술 막대 ─────────────────────────

func _process(delta: float) -> void:
	if not qte_active:
		return
	qte_t += delta
	qte_bar.value = _qte_pos() * 100.0
	if qte_t >= QTE_TIMEOUT:
		_finish_qte(0.0)


func _qte_pos() -> float:
	return 0.5 - 0.5 * cos(qte_t * TAU * QTE_SPEED)   # 0 에서 출발해 0~1 왕복


func _input(event: InputEvent) -> void:
	if not qte_active:
		return
	var key := event as InputEventKey
	if key != null and key.pressed and not key.echo and key.keycode == KEY_SPACE:
		get_viewport().set_input_as_handled()
		_on_qte_press()


func _on_qte_press() -> void:
	if not qte_active:
		return
	_finish_qte(1.0 - absf(_qte_pos() - 0.5) / 0.5)


func _finish_qte(q: float) -> void:
	qte_active = false
	qte_panel.visible = false
	_log("[color=violet]손기술 %d점 / 100[/color]" % roundi(q * 100.0))
	game.cheat(0, qte_kind, q)
	_after_action()


# ───────────────────────── 이벤트 → 글 ─────────────────────────

func _drain_events() -> void:
	for ev in game.pop_events():
		_render_event(ev)


func _render_event(ev: Dictionary) -> void:
	match str(ev["type"]):
		"round_start":
			round_secrets.clear()
			var mine: int = ev["sides"][0]
			_log("\n[b]── %s 시작 ──[/b] 당신: %s · 상대: %s" % [_round_name(int(ev["round"])),
				RankCards.SIDE_NAMES[mine], RankCards.SIDE_NAMES[ev["sides"][1]]])
			if mine == RankCards.Team.KING_SIDE:
				_log("왕 측: 왕이 시민을 만나면 +1점. 상대 암살자에게 왕을 내면 짐.")
			else:
				_log("암살자 측: 암살자가 왕을 잡으면 +4점. 시민에게 암살자를 내면 짐.")
		"turn_start":
			var g: Array = ev["gaze"]
			_log("%d턴 — 상대 시선: %s" % [int(ev["turn_in_round"]), "당신의 [b]손[/b]" if g[1] == "hands" else "당신의 얼굴"])
		"tell":
			if int(ev["seat"]) == 1 and bool(ev["noticed"]):
				_log("[color=orange]상대 손이 %s테이블 아래로 움직였다.[/color]" % _tell_word(float(ev["intensity"])))
		"notice":
			if int(ev["observer"]) == 1 and bool(ev["noticed"]):
				_log("[color=orange]상대 눈빛이 날카로워졌다…[/color]")
		"cheat":
			if int(ev["seat"]) == 1:
				round_secrets.append(ev)
			else:
				_log("[color=violet]당신의 %s — 상대 시선이 %s에 있었음 (단서 %.2f)[/color]" % [
					CheatRules.CHEATS[ev["cheat"]]["name"], "손" if bool(ev["watched"]) else "얼굴", float(ev["tell"])])
				if str(ev["cheat"]) == "mark":
					_log("[color=violet]표시를 해 뒀다 — 다음 턴부터, 턴마다 %d%% 확률로 보임[/color]" % roundi(CheatRules.MARK_READ_CHANCE * 100.0))
		"peek_info":
			_log("[color=cyan]엿보기: 상대가 고른 카드 = %s (상대도 엿봤다면 마지막에 바뀔 수 있음)[/color]" % RankCards.CARD_NAMES[ev["card"]])
		"mark_info":
			if not bool(ev["seen"]):
				_log("[color=cyan]뒷면 표시: 이번엔 잘 안 보인다[/color]")
			else:
				_log("[color=cyan]뒷면 표시: 상대 카드에 표시가 %s[/color]" % ("있다 → 특수 카드" if bool(ev["special"]) else "없다 → 시민"))
		"face_cue":
			_log("상대 표정: %s" % ("입술을 깨문다" if bool(ev["nervous"]) else "평온하다"))
		"reveal":
			var c: Array = ev["cards"]
			var r := int(ev["result"])
			var verdict := "비김 — 다음 턴"
			if r > 0:
				verdict = "[color=lime]당신 승[/color]"
			elif r < 0:
				verdict = "[color=red]상대 승[/color]"
			_log("공개: 당신 %s vs 상대 %s → %s" % [RankCards.CARD_NAMES[c[0]], RankCards.CARD_NAMES[c[1]], verdict])
		"accuse":
			var who := "당신" if int(ev["accuser"]) == 0 else "상대"
			var accused := 1 - int(ev["accuser"])
			if bool(ev["hit"]):
				_log("[color=red][b]%s의 고발 적중![/b] 증거: %s · %s 경고 %d/%d · 벌금 %d점[/color]" % [who, _cheat_names(ev["found"]),
					"당신" if accused == 0 else "상대", int(ev["strikes"][accused]), CheatRules.STRIKES_TO_LOSE, CheatRules.CAUGHT_FINE])
			else:
				_log("[color=yellow]%s의 헛고발 — 고발 토큰 −1, 벌금 %d점[/color]" % [who, CheatRules.FALSE_ACCUSE_FINE])
		"round_end":
			var w := int(ev["winner"])
			var how := "몰수" if str(ev["by"]) == "forfeit" else "카드"
			_log("판 결과: %s +%d점 (%s) · 점수 %d : %d" % ["당신" if w == 0 else "상대", int(ev["points"]), how,
				int(ev["scores"][0]), int(ev["scores"][1])])
			_show_replay()
		"match_end":
			var mw := int(ev["winner"])
			var reason := "두 번 들켜서" if str(ev["reason"]) == "CAUGHT_TWICE" else "점수로"
			var res_text := "무승부"
			if mw == 0:
				res_text = "[color=lime]당신 승리[/color]"
			elif mw == 1:
				res_text = "[color=red]당신 패배[/color]"
			_log("\n[b]매치 끝 — %s (%s) · 최종 %d : %d[/b]" % [res_text, reason, int(ev["scores"][0]), int(ev["scores"][1])])


func _show_replay() -> void:
	if round_secrets.is_empty():
		_log("[color=gray]리플레이: 이번 판 상대 속임수 없음[/color]")
		return
	for s in round_secrets:
		var what: String = CheatRules.CHEATS[s["cheat"]]["name"]
		_log("[color=gray]리플레이: %d턴에 상대가 %s — 그때 당신은 %s을 보고 있었음 (단서 %.2f)[/color]" % [
			int(s["turn_in_round"]), what, "손" if bool(s["watched"]) else "얼굴", float(s["tell"])])
	round_secrets.clear()


func _tell_word(i: float) -> String:
	if i < 0.25:
		return "아주 살짝 "
	if i < 0.5:
		return "살짝 "
	if i < 0.75:
		return ""
	return "눈에 띄게 "


func _cheat_names(ids: Array) -> String:
	var names := PackedStringArray()
	for id in ids:
		names.append(str(CheatRules.CHEATS[id]["name"]))
	return ", ".join(names)


func _log(text: String) -> void:
	log_view.append_text(text + "\n")


# ───────────────────────── 상태 표시 ─────────────────────────

func _refresh() -> void:
	var choosing: bool = game.phase == GambleMatch.Phase.CHOOSE and not qte_active
	var over: bool = game.is_over()
	status_label.text = "%s · 당신 %s · 점수 %d : %d · 내 경고 %s · 상대 경고 %s · 고발 토큰 %d" % [
		_round_name(int(game.round_index)), RankCards.SIDE_NAMES[game.sides[0]],
		int(game.scores[0]), int(game.scores[1]), _dots(int(game.strikes[0])), _dots(int(game.strikes[1])),
		int(game.tokens[0])]
	gaze_label.text = "상대 시선: %s · 내 시선: %s" % [
		"당신의 손" if game.gaze[1] == "hands" else "당신의 얼굴",
		"상대 손" if game.gaze[0] == "hands" else "상대 얼굴"]
	gaze_hands_btn.disabled = game.gaze[0] == "hands" or over
	gaze_face_btn.disabled = game.gaze[0] == "face" or over

	_clear(hand_box)
	for card in game.hands[0]:
		var b := _button(RankCards.CARD_NAMES[card], _on_card.bind(int(card)))
		b.custom_minimum_size = Vector2(96, 56)
		b.disabled = not choosing
		hand_box.add_child(b)

	_clear(cheat_box)
	var left: Dictionary = game.uses_left(0)
	for id in CheatRules.CHEATS:
		var cid: String = str(id)
		var n_left: int = int(left[cid])
		var b := _button("%s (남은 %d)" % [CheatRules.CHEATS[cid]["name"], n_left], _on_cheat.bind(cid))
		var blocked: bool = n_left <= 0 or (cid == "mark" and bool(game.marked[0])) or (cid == "peek" and bool(game.peeked_now[0]))
		b.disabled = not choosing or blocked
		cheat_box.add_child(b)

	var can_accuse: bool = game.phase == GambleMatch.Phase.CHOOSE or game.phase == GambleMatch.Phase.REVEALED
	accuse_btn.text = "잡았다! (고발 토큰 %d)" % int(game.tokens[0])
	accuse_btn.disabled = qte_active or not can_accuse or int(game.tokens[0]) <= 0
	next_btn.disabled = qte_active or game.phase != GambleMatch.Phase.REVEALED


func _round_name(idx: int) -> String:
	if idx >= GambleMatch.ROUNDS:
		return "연장 %d판" % (idx - GambleMatch.ROUNDS + 1)
	return "%d/%d판" % [maxi(idx, 0) + 1, GambleMatch.ROUNDS]


func _dots(n: int) -> String:
	return "●".repeat(n) + "○".repeat(maxi(CheatRules.STRIKES_TO_LOSE - n, 0))


func _clear(box: Node) -> void:
	for c in box.get_children():
		box.remove_child(c)
		c.queue_free()
