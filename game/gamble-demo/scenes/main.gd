# VERSION: v0.4.0 — 2026-11-26 — 키 행동: [1] 라이터 놓기 · [2] 협력자 부르기 · [C] 카드 덮개 · [B] 블러핑 · 안내·기록
# 이전 VERSION: v0.3.0 — 2026-11-26 — 안내 문구: 노예(암살자) 측 판 = 속임수 판, 왕 측 판 = 감시 판
# 이전 VERSION: v0.2.0 — 2026-11-26 — 실시간 화면: 마우스 = 시선 · 시야 제한(보는 곳만 밝게) · 스페이스 = 잡았다
#
# 조작: 마우스가 가리키는 곳 = 내 시선 · 카드 클릭 = 내기 · 행동은 키보드 (마우스를 움직이면 시선이 바뀌므로)
#   [1] 라이터 놓기(반사경 준비) · [2] 협력자 부르기 · [C] 카드 덮개 · [B] 블러핑(여유 부리기) · [스페이스] 잡았다 · [Enter] 다음
# 규칙은 core/match.gd 에, 그림은 scenes/table_view.gd 에. 여기선 연결·안내·기록만.
# 연구·교육용 데모 — 실제 돈과 관계없음.
extends Control

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const AiBrain = preload("res://core/ai_brain.gd")
const GambleMatch = preload("res://core/match.gd")
const TableView = preload("res://scenes/table_view.gd")

const OPPONENTS := ["cheater", "watcher", "gambler"]
const OPP_NAMES := {"cheater": "손버릇 나쁜 딜러", "watcher": "눈이 매서운 노인", "gambler": "대담한 도박꾼"}
const MAX_DT := 0.1   # 프레임이 끊겨도 한 번에 0.1초 넘게 흐르지 않게 (들킴 확률이 튀지 않게)
const SPOT_SHADER := """
shader_type canvas_item;
uniform vec2 center_px = vec2(640.0, 400.0);
uniform vec2 rect_size = vec2(1280.0, 800.0);
uniform float radius = 210.0;
uniform float dim = 0.62;
void fragment() {
	float d = distance(UV * rect_size, center_px);
	COLOR = vec4(0.0, 0.0, 0.0, dim * smoothstep(radius * 0.55, radius, d));
}
"""

var game = null
var table = null
var opponent_kind := "cheater"
var current_gaze := "table"

var spot: ColorRect
var spot_mat: ShaderMaterial
var banner: Label
var timer_bar: ProgressBar
var status_label: Label
var keys_label: Label
var log_view: RichTextLabel
var opp_option: OptionButton
var spot_check: CheckBox
var helper_check: CheckBox
var next_btn: Button


func _ready() -> void:
	_build()
	_new_match()


# ───────────────────────── 화면 ─────────────────────────

func _build() -> void:
	set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	table = TableView.new()
	table.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	table.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(table)

	spot = ColorRect.new()
	spot.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	spot.mouse_filter = Control.MOUSE_FILTER_IGNORE
	var sh := Shader.new()
	sh.code = SPOT_SHADER
	spot_mat = ShaderMaterial.new()
	spot_mat.shader = sh
	spot.material = spot_mat
	add_child(spot)

	var layer := CanvasLayer.new()
	layer.layer = 2
	add_child(layer)
	var ui := Control.new()
	ui.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	ui.mouse_filter = Control.MOUSE_FILTER_IGNORE
	layer.add_child(ui)

	banner = _label(Vector2(250, 6), Vector2(780, 52), 17)
	banner.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	banner.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	ui.add_child(banner)
	timer_bar = ProgressBar.new()
	timer_bar.position = Vector2(440, 62)
	timer_bar.size = Vector2(400, 10)
	timer_bar.show_percentage = false
	timer_bar.mouse_filter = Control.MOUSE_FILTER_IGNORE
	ui.add_child(timer_bar)

	status_label = _label(Vector2(14, 10), Vector2(330, 96), 16)
	ui.add_child(status_label)
	opp_option = OptionButton.new()
	for k in OPPONENTS:
		opp_option.add_item(OPP_NAMES[k])
	opp_option.position = Vector2(14, 110)
	opp_option.focus_mode = Control.FOCUS_NONE
	ui.add_child(opp_option)
	ui.add_child(_button("새 매치", Vector2(230, 110), _on_new_match))
	spot_check = CheckBox.new()
	spot_check.text = "시야 제한 (보는 곳만 밝게)"
	spot_check.button_pressed = true
	spot_check.position = Vector2(14, 148)
	spot_check.focus_mode = Control.FOCUS_NONE
	ui.add_child(spot_check)
	helper_check = CheckBox.new()
	helper_check.text = "상대 시선 보조선 (연습용)"
	helper_check.position = Vector2(14, 178)
	helper_check.focus_mode = Control.FOCUS_NONE
	ui.add_child(helper_check)
	keys_label = _label(Vector2(14, 214), Vector2(250, 150), 14)
	ui.add_child(keys_label)

	var log_bg := ColorRect.new()
	log_bg.color = Color(0, 0, 0, 0.55)
	log_bg.position = Vector2(996, 70)
	log_bg.size = Vector2(276, 384)
	log_bg.mouse_filter = Control.MOUSE_FILTER_IGNORE
	ui.add_child(log_bg)
	log_view = RichTextLabel.new()
	log_view.bbcode_enabled = true
	log_view.scroll_following = true
	log_view.position = Vector2(1002, 74)
	log_view.size = Vector2(266, 376)
	log_view.mouse_filter = Control.MOUSE_FILTER_IGNORE
	log_view.add_theme_font_size_override("normal_font_size", 13)
	log_view.add_theme_font_size_override("bold_font_size", 13)
	ui.add_child(log_view)

	next_btn = _button("다음 ▶ (Enter)", Vector2(1110, 744), _on_next)
	ui.add_child(next_btn)


func _label(pos: Vector2, box: Vector2, font_size: int) -> Label:
	var l := Label.new()
	l.position = pos
	l.size = box
	l.add_theme_font_size_override("font_size", font_size)
	l.add_theme_color_override("font_outline_color", Color(0, 0, 0))
	l.add_theme_constant_override("outline_size", 6)
	l.mouse_filter = Control.MOUSE_FILTER_IGNORE
	return l


func _button(text: String, pos: Vector2, cb: Callable) -> Button:
	var b := Button.new()
	b.text = text
	b.position = pos
	b.focus_mode = Control.FOCUS_NONE
	b.add_theme_font_size_override("font_size", 16)
	b.pressed.connect(cb)
	return b


# ───────────────────────── 매치 ─────────────────────────

func _on_new_match() -> void:
	opponent_kind = OPPONENTS[opp_option.selected]
	_new_match()


func _new_match() -> void:
	var brain = AiBrain.new()
	brain.configure(opponent_kind)
	game = GambleMatch.new()
	var s := int(Time.get_unix_time_from_system()) % 1000000
	game.setup(s, null, brain)
	table.game = game
	log_view.clear()
	_log("[b]새 매치[/b] — 상대: %s · 시드 %d" % [OPP_NAMES[opponent_kind], s])
	_log("노예(암살자) 측 판 = [color=orange]속임수 판[/color]: 키 1 라이터를 놓고 뚜껑 안 반사경을 %.1f초, 또는 키 2 협력자를 불러 손 신호를 %.1f초 보면 상대 카드" % [CheatRules.PEEK_SECONDS, CheatRules.SIGNAL_SECONDS])
	_log("왕 측 판 = [color=skyblue]감시 판[/color]: 상대 눈이 오른쪽 라이터로 가면 스페이스 · 키 C 카드 덮개로 막기")
	_log("키 B 블러핑: 내 시간 +, 상대 시간 − (매치 %d번)" % CheatRules.BLUFFS_PER_MATCH)
	_log("들키면 그 판 몰수 + 벌금 %d점 · 경고 %d개면 패배 · 헛고발은 토큰 −1 + 벌금 %d점" % [
		CheatRules.CAUGHT_FINE, CheatRules.STRIKES_TO_LOSE, CheatRules.FALSE_ACCUSE_FINE])
	_log("[color=gray]연구·교육용 데모입니다. 실제 돈과 관계없습니다.[/color]")
	game.start()
	_drain()


func _process(delta: float) -> void:
	if game == null:
		return
	var mp: Vector2 = get_local_mouse_position()
	current_gaze = table.gaze_target(mp)
	table.my_gaze = current_gaze
	var choosing: bool = int(game.phase) == GambleMatch.Phase.PLAYER_CHOOSE
	var hover: int = table.card_at(mp) if choosing else -1
	table.hover_index = hover
	table.show_helper = helper_check.button_pressed
	game.tick(minf(delta, MAX_DT), current_gaze)
	_drain()
	spot.visible = spot_check.button_pressed
	spot_mat.set_shader_parameter("center_px", mp)
	spot_mat.set_shader_parameter("rect_size", size)
	_refresh()
	table.queue_redraw()


func _gui_input(event: InputEvent) -> void:
	var mb := event as InputEventMouseButton
	if mb == null or not mb.pressed or mb.button_index != MOUSE_BUTTON_LEFT:
		return
	if game == null or int(game.phase) != GambleMatch.Phase.PLAYER_CHOOSE:
		return
	var idx: int = table.card_at(mb.position)
	if idx >= 0:
		game.commit(int(game.hands[0][idx]))
		_drain()


func _unhandled_input(event: InputEvent) -> void:
	var k := event as InputEventKey
	if k == null or not k.pressed or k.echo or game == null:
		return
	var r := {}
	if k.keycode == KEY_SPACE:
		if int(game.phase) != GambleMatch.Phase.AI_THINK:
			_log("[color=gray]고발은 감시 판에서 상대가 고민할 때만[/color]")
			return
		r = game.accuse()
	elif k.keycode == KEY_1:
		r = game.place_lighter()
	elif k.keycode == KEY_2:
		r = game.call_accomplice()
	elif k.keycode == KEY_C:
		r = game.cover_card()
	elif k.keycode == KEY_B:
		r = game.bluff()
	elif k.keycode == KEY_ENTER or k.keycode == KEY_KP_ENTER or k.keycode == KEY_N:
		_on_next()
		return
	else:
		return
	if r.has("ok") and not bool(r["ok"]):
		_log("[color=gray]지금은 못 함 (%s)[/color]" % _why(str(r.get("why", ""))))
	_drain()


func _why(code: String) -> String:
	if code == "not_cheat_choose":
		return "속임수 판에서 고르는 중에만"
	if code == "not_detect":
		return "감시 판에서만"
	if code == "already":
		return "이미 했음"
	if code == "no_uses" or code == "no_calls":
		return "남은 횟수 없음"
	if code == "no_token":
		return "고발 토큰 없음"
	if code.begins_with("state="):
		return "협력자가 이미 있거나 쫓겨남"
	return code


func _on_next() -> void:
	if game != null and int(game.phase) == GambleMatch.Phase.REVEALED:
		game.next()
		_drain()


# ───────────────────────── 이벤트 → 글 ─────────────────────────

func _drain() -> void:
	for ev in game.pop_events():
		_render(ev)


func _render(ev: Dictionary) -> void:
	var kind := str(ev["type"])
	if kind == "round_start":
		var mine: int = ev["sides"][0]
		_log("\n[b]── %s ──[/b] 당신: %s" % [_round_name(int(ev["round"])), RankCards.SIDE_NAMES[mine]])
		if mine == RankCards.Team.KING_SIDE:
			_log("왕 측: 왕이 시민을 만나면 +1 · 상대 암살자에게 왕을 내면 짐")
			_log("[color=skyblue]감시 판[/color] — 매 턴 당신이 먼저 내고, 상대가 라이터 반사경을 보는지 지켜보세요")
		else:
			_log("암살자(노예) 측: 암살자가 왕을 잡으면 +4 · 시민에게 암살자를 내면 짐")
			_log("[color=orange]속임수 판[/color] — 매 턴 상대가 먼저 냄 · 키 1 라이터 / 키 2 협력자")
	elif kind == "turn_start":
		_log("%d턴째 · 제한 %.0f초" % [int(ev["turn_in_round"]), float(ev["limit"])])
	elif kind == "setup":
		_render_setup(ev)
	elif kind == "acc_arrived":
		_log("[color=cyan]협력자가 상대 뒤에 섰다 — 오른쪽 뒤 사람의 손을 보세요[/color]")
	elif kind == "stranger_seen":
		_log("[color=orange]상대가 뒤를 돌아보다 협력자를 봤다… 의심이 커짐[/color]")
	elif kind == "cover":
		if int(ev["seat"]) == 1:
			_log("[color=orange]상대가 자기 카드 위에 칩을 올렸다 — 반사경에 안 비침 (협력자는 됨)[/color]")
		else:
			_log("[color=skyblue]내 카드 위에 칩을 올렸다 — 이번 턴 상대 반사경이 안 비침[/color]")
	elif kind == "bluff":
		if int(ev["seat"]) == 0:
			_log("[color=violet]블러핑: 여유를 부린다 — 내 시간 +, 상대 시간 −[/color]")
		else:
			_log("[color=orange]상대가 여유를 부린다 — 상대 고민 +%.0f초 · 당신 다음 턴 −%.0f초[/color]" % [CheatRules.THINK_BLUFF_SECONDS, CheatRules.CHOOSE_BLUFF_SECONDS])
	elif kind == "peek_info":
		var how := "라이터 반사경" if str(ev["source"]) == "shiner" else "협력자 손 신호"
		_log("[color=cyan]%s: 상대 카드 = %s[/color]" % [how, RankCards.CARD_NAMES[ev["card"]]])
	elif kind == "ai_think_start":
		_log("상대가 고민한다 (약 %.0f초) — 눈을 지켜보세요" % float(ev["seconds"]))
	elif kind == "timeout":
		_log("[color=yellow]시간 초과 — %s 를 냈다[/color]" % RankCards.CARD_NAMES[ev["card"]])
	elif kind == "accuse":
		_render_accuse(ev)
	elif kind == "turn_summary":
		_render_summary(ev)
	elif kind == "reveal":
		var c: Array = ev["cards"]
		var r := int(ev["result"])
		var verdict := "비김 — 다음 턴"
		if r > 0:
			verdict = "[color=lime]당신 승[/color]"
		elif r < 0:
			verdict = "[color=red]상대 승[/color]"
		_log("공개: 당신 %s vs 상대 %s → %s" % [RankCards.CARD_NAMES[c[0]], RankCards.CARD_NAMES[c[1]], verdict])
	elif kind == "round_end":
		var w := int(ev["winner"])
		var how2 := "몰수" if str(ev["by"]) == "forfeit" else "카드"
		_log("판 결과: %s +%d점 (%s) · 점수 %d : %d" % ["당신" if w == 0 else "상대", int(ev["points"]), how2,
			int(ev["scores"][0]), int(ev["scores"][1])])
	elif kind == "match_end":
		var mw := int(ev["winner"])
		var res_text := "무승부"
		if mw == 0:
			res_text = "[color=lime]당신 승리[/color]"
		elif mw == 1:
			res_text = "[color=red]당신 패배[/color]"
		var reason := "두 번 들켜서" if str(ev["reason"]) == "CAUGHT_TWICE" else "점수로"
		_log("\n[b]매치 끝 — %s (%s) · %d : %d[/b]" % [res_text, reason, int(ev["scores"][0]), int(ev["scores"][1])])


func _render_setup(ev: Dictionary) -> void:
	var seen := bool(ev["seen"])
	if int(ev["seat"]) == 1:
		_log("[color=orange]상대가 라이터를 꺼내 테이블 오른쪽에 놓았다…[/color]")
		return
	if str(ev["kind"]) == "lighter":
		_log("[color=violet]라이터를 테이블에 놓았다 (뚜껑 안에 작은 반사경)[/color]")
	else:
		_log("[color=violet]헛기침으로 협력자를 불렀다 — %.1f초 뒤 상대 뒤에 섬[/color]" % CheatRules.ACC_WALK_SECONDS)
	if seen:
		_log("[color=orange]…상대가 그걸 봤다. 의심이 커짐[/color]")


func _render_accuse(ev: Dictionary) -> void:
	var who := int(ev["accuser"])
	var by := str(ev["by"])
	if not bool(ev["hit"]):
		_log("[color=yellow]헛고발 — 상대는 반사경을 보고 있지 않았다 · 토큰 −1 · 벌금 %d점[/color]" % CheatRules.FALSE_ACCUSE_FINE)
	elif who == 1 and by == "accomplice":
		_log("[color=red][b]상대가 뒤를 돌아봤다 — 협력자 들킴! 쫓겨남[/b] 경고 %d/%d · 벌금 %d점[/color]" % [
			int(ev["strikes"][0]), CheatRules.STRIKES_TO_LOSE, CheatRules.CAUGHT_FINE])
	elif who == 1:
		_log("[color=red][b]상대: \"라이터는 왜 봐?\" — 들켰다! 라이터 몰수[/b] 경고 %d/%d · 벌금 %d점[/color]" % [
			int(ev["strikes"][0]), CheatRules.STRIKES_TO_LOSE, CheatRules.CAUGHT_FINE])
	else:
		_log("[color=lime][b]잡았다! 상대가 반사경을 보고 있었다 — 라이터 몰수[/b] 상대 경고 %d/%d · 벌금 %d점[/color]" % [
			int(ev["strikes"][1]), CheatRules.STRIKES_TO_LOSE, CheatRules.CAUGHT_FINE])


## 턴 끝 리플레이 — 그 턴에 실제로 무슨 일이 있었는지
func _render_summary(ev: Dictionary) -> void:
	var look: Array = ev["look"]
	if int(ev["turn_type"]) == GambleMatch.TurnType.CHEAT:
		if float(look[0]) > 0.0:
			_log("[color=gray]  └ 당신이 반사경·신호를 본 시간 %.1f초 · 그동안 상대가 당신 얼굴을 본 시간 %.1f초[/color]" % [float(look[0]), float(ev["watched"])])
		return
	var done: Array = ev["peek_done"]
	if int(ev["glances"]) == 0:
		_log("[color=gray]  └ 리플레이: 상대는 이번 턴 반사경을 보지 않았다[/color]")
	else:
		_log("[color=gray]  └ 리플레이: 상대가 반사경을 %d번 · %.1f초 봄 (당신이 그 순간 얼굴을 본 시간 %.1f초) · 엿보기 %s[/color]" % [
			int(ev["glances"]), float(look[1]), float(ev["watched"]), "성공" if bool(done[1]) else "실패"])


func _log(text: String) -> void:
	log_view.append_text(text + "\n")


# ───────────────────────── 상태 표시 ─────────────────────────

func _refresh() -> void:
	var ph := int(game.phase)
	var cheat_turn: bool = int(game.turn_type) == GambleMatch.TurnType.CHEAT
	var text := ""
	if ph == GambleMatch.Phase.PLAYER_CHOOSE and cheat_turn:
		text = "속임수 판 — [1] 라이터를 놓고 반사경을 %.1f초 · 또는 [2] 협력자 손 신호를 %.1f초. 상대가 당신 얼굴(반사경)·뒤(협력자)를 보면 들킴" % [CheatRules.PEEK_SECONDS, CheatRules.SIGNAL_SECONDS]
	elif ph == GambleMatch.Phase.PLAYER_CHOOSE:
		text = "감시 판 — 카드를 고르세요 · [C] 카드 덮개로 상대 반사경을 막을 수 있음"
	elif ph == GambleMatch.Phase.AI_THINK:
		text = "감시 판 — 상대가 고민 중. 상대 눈이 오른쪽 라이터로 가면 [스페이스] · [B] 블러핑으로 상대 시간 줄이기"
	elif ph == GambleMatch.Phase.REVEALED:
		text = "[Enter] 다음"
	elif ph == GambleMatch.Phase.MATCH_OVER:
		text = "매치 끝 — '새 매치'"
	banner.text = text
	var left := 0.0
	if ph == GambleMatch.Phase.PLAYER_CHOOSE:
		left = 1.0 - float(game.t) / maxf(float(game.turn_limit), 0.01)
	elif ph == GambleMatch.Phase.AI_THINK:
		left = float(game.think_left) / maxf(float(game.think_total), 0.01)
	timer_bar.value = clampf(left, 0.0, 1.0) * 100.0
	status_label.text = "%s · 당신 %s\n점수 %d : %d\n내 경고 %s · 상대 경고 %s · 고발 토큰 %d" % [
		_round_name(int(game.round_index)), RankCards.SIDE_NAMES[game.sides[0]],
		int(game.scores[0]), int(game.scores[1]), _dots(int(game.strikes[0])), _dots(int(game.strikes[1])),
		int(game.tokens[0])]
	var acc_text := "협력자 %d번" % int(game.acc_calls_left)
	if str(game.acc_state) == "out":
		acc_text = "협력자 쫓겨남"
	keys_label.text = "[1] 라이터 놓기 (판마다)\n[2] 협력자 부르기 (%s)\n[C] 카드 덮개 (%d번)\n[B] 블러핑 (%d번)\n[스페이스] 잡았다 · [Enter] 다음" % [
		acc_text, int(game.cover_left[0]), int(game.bluff_left[0])]
	next_btn.disabled = ph != GambleMatch.Phase.REVEALED


func _round_name(idx: int) -> String:
	if idx >= GambleMatch.ROUNDS:
		return "연장 %d판" % (idx - GambleMatch.ROUNDS + 1)
	return "%d/%d판" % [maxi(idx, 0) + 1, GambleMatch.ROUNDS]


func _dots(n: int) -> String:
	return "●".repeat(n) + "○".repeat(maxi(CheatRules.STRIKES_TO_LOSE - n, 0))
