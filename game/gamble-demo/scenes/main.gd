# VERSION: v0.5.0 — 2026-11-26 — 사전 설정(책상 위 물건 3자리) · 왕 턴/노예 턴 · 진영별 키 · 가능성 불 두 개 · 새 이벤트 기록
# 이전 VERSION: v0.4.0 — 2026-11-26 — 키 행동: 라이터 놓기 · 협력자 부르기 · 카드 덮개 · 블러핑 · 안내·기록
# 이전 VERSION: v0.3.0 — 2026-11-26 — 안내 문구: 노예(암살자) 측 판 = 속임수 판, 왕 측 판 = 감시 판
# 이전 VERSION: v0.2.0 — 2026-11-26 — 실시간 화면: 마우스 = 시선 · 시야 제한(보는 곳만 밝게) · 스페이스 = 잡았다
#
# 조작: 마우스가 가리키는 곳 = 내 시선 · 카드 클릭 = 내기 · 행동은 키보드 (마우스를 움직이면 시선이 바뀌므로)
#   노예(공격): 1 반사경 라이터 놓기 · 3 빈 라이터 놓기 · 2 협력자 부르기 · F 시선 끌기 · G 제스처
#   왕(방어)  : C 가리기 · R 무작위로 내기 · X 바꿔치기 · Q 엿보기 밝혀내기 · W 협력자 밝혀내기
#   Enter 다음
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
## 사전 설정 고르기 — "" = 비움
const SETUP_KINDS := ["", "lighter", "lighter_plain", "cigcase", "cigcase_plain", "glass", "phone"]
const SETUP_NAMES := ["없음", "라이터 (반사경)", "라이터 (빈 것)", "담뱃갑 (반사경)", "담뱃갑 (빈 것)", "술잔", "휴대폰"]
const SETUP_DEFAULT := [1, 4, 0]
const MAX_DT := 0.1   # 프레임이 끊겨도 한 번에 0.1초 넘게 흐르지 않게 (들킴 확률이 튀지 않게)
const LAMP_OFF := Color(0.18, 0.18, 0.2, 0.85)
const LAMP_ON := Color(1.0, 0.72, 0.15, 0.95)
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
var timer_label: Label
var status_label: Label
var keys_label: Label
var log_view: RichTextLabel
var opp_option: OptionButton
var spot_check: CheckBox
var helper_check: CheckBox
var next_btn: Button
var lamp_caption: Label
var lamp_rects: Dictionary = {}
var lamp_labels: Dictionary = {}
var setup_panel: Control
var setup_options: Array = []


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
	timer_label = _label(Vector2(850, 54), Vector2(140, 24), 15)
	ui.add_child(timer_label)

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
	keys_label = _label(Vector2(14, 214), Vector2(330, 170), 14)
	ui.add_child(keys_label)

	var log_bg := ColorRect.new()
	log_bg.color = Color(0, 0, 0, 0.55)
	log_bg.position = Vector2(996, 70)
	log_bg.size = Vector2(276, 360)
	log_bg.mouse_filter = Control.MOUSE_FILTER_IGNORE
	ui.add_child(log_bg)
	log_view = RichTextLabel.new()
	log_view.bbcode_enabled = true
	log_view.scroll_following = true
	log_view.position = Vector2(1002, 74)
	log_view.size = Vector2(266, 352)
	log_view.mouse_filter = Control.MOUSE_FILTER_IGNORE
	log_view.add_theme_font_size_override("normal_font_size", 13)
	log_view.add_theme_font_size_override("bold_font_size", 13)
	ui.add_child(log_view)

	# 가능성 불 두 개 — 노예 시선이 1.5초(물건)/1.8초(협력자 자리) 고정되면 켜짐 (진짜든 미끼든)
	lamp_caption = _label(Vector2(996, 434), Vector2(276, 22), 13)
	ui.add_child(lamp_caption)
	var lx := 996.0
	for kind in ["peek", "acc"]:
		var r := ColorRect.new()
		r.position = Vector2(lx, 458)
		r.size = Vector2(134, 40)
		r.color = LAMP_OFF
		r.mouse_filter = Control.MOUSE_FILTER_IGNORE
		ui.add_child(r)
		var l := _label(Vector2(lx, 458), Vector2(134, 40), 15)
		l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		l.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
		l.text = "엿보기 가능성" if kind == "peek" else "협력자 가능성"
		ui.add_child(l)
		lamp_rects[kind] = r
		lamp_labels[kind] = l
		lx += 142.0

	next_btn = _button("다음 ▶ (Enter)", Vector2(1110, 744), _on_next)
	ui.add_child(next_btn)
	_build_setup(ui)


## 사전 설정 창: 책상 위 물건 3자리 (반사경이 든 것 / 빈 것은 겉모양이 같음)
func _build_setup(ui: Control) -> void:
	setup_panel = Control.new()
	setup_panel.position = Vector2(390, 240)
	setup_panel.size = Vector2(500, 290)
	ui.add_child(setup_panel)
	var bg := ColorRect.new()
	bg.color = Color(0.05, 0.05, 0.07, 0.94)
	bg.size = setup_panel.size
	setup_panel.add_child(bg)
	var title := _label(Vector2(20, 14), Vector2(460, 30), 19)
	title.text = "사전 설정 — 책상 위에 둘 물건 (최대 %d개)" % CheatRules.OBJECT_SLOTS
	setup_panel.add_child(title)
	var help := _label(Vector2(20, 48), Vector2(460, 60), 13)
	help.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	help.text = "반사경이 든 물건을 %.1f초 계속 보면 상대 카드가 비침. 빈 물건은 미끼 — 오래 봐도 상대에겐 똑같이 '엿보기 가능성' 불이 켜짐. 상대 눈엔 둘이 똑같이 보임." % CheatRules.PEEK_FIX
	setup_panel.add_child(help)
	setup_options.clear()
	for i in CheatRules.OBJECT_SLOTS:
		var lab := _label(Vector2(20, 118 + i * 40), Vector2(90, 30), 15)
		lab.text = "자리 %d" % (i + 1)
		setup_panel.add_child(lab)
		var ob := OptionButton.new()
		for n in SETUP_NAMES:
			ob.add_item(n)
		ob.selected = int(SETUP_DEFAULT[i])
		ob.position = Vector2(110, 114 + i * 40)
		ob.focus_mode = Control.FOCUS_NONE
		setup_panel.add_child(ob)
		setup_options.append(ob)
	var start_btn := _button("시작", Vector2(380, 236), _on_setup_start)
	setup_panel.add_child(start_btn)
	var note := _label(Vector2(20, 240), Vector2(340, 30), 12)
	note.text = "게임 중에도 키 1·3 으로 더 놓을 수 있음"
	setup_panel.add_child(note)


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
	_log("한 턴 = [color=skyblue]왕 턴[/color](왕이 먼저 엎어 냄) → [color=orange]노예 턴[/color](노예가 엿보고 냄) · 각 %.0f초" % CheatRules.TURN_SECONDS)
	_log("노예: 반사경 물건 %.1f초 · 협력자 %.1f초 계속 보면 상대 카드. 눈을 떼면 처음부터" % [CheatRules.PEEK_FIX, CheatRules.ACC_FIX])
	_log("왕: 노예 시선이 그만큼 고정되면 가능성 불이 켜짐 (진짜든 미끼든) → 밝혀내기")
	_log("밝혀내기 적중 = 상대 경고 +1 · 그 속임수 봉인 · 상대 턴 −%.0f초 / 헛짚음 = 내 다음 턴 −%.0f초 · 경고 %d개면 패배" % [
		CheatRules.EXPOSE_CUT, CheatRules.EXPOSE_FAIL_CUT, CheatRules.STRIKES_TO_LOSE])
	_log("[color=gray]연구·교육용 데모입니다. 실제 돈과 관계없습니다.[/color]")
	_log("[color=yellow]가운데 창에서 책상 위 물건을 고르고 '시작'[/color]")
	setup_panel.visible = true
	_drain()


func _on_setup_start() -> void:
	if game == null or int(game.phase) != GambleMatch.Phase.IDLE:
		return
	var kinds: Array = []
	for ob in setup_options:
		var k := str(SETUP_KINDS[int(ob.selected)])
		if k != "":
			kinds.append(k)
	game.set_objects(0, kinds)
	setup_panel.visible = false
	_log("내 책상 위: %s" % _object_list(game.objects[0], true))
	_log("상대 책상 위: %s" % _object_list(game.objects[1], false))
	game.start()
	_drain()


func _object_list(kinds: Array, mine: bool) -> String:
	if kinds.is_empty():
		return "없음"
	var parts := PackedStringArray()
	for k in kinds:
		var n := str(CheatRules.OBJECTS[str(k)]["name"])
		if mine:
			n += "(반사경)" if CheatRules.is_mirror(str(k)) else "(빈 것)"
		parts.append(n)
	return ", ".join(parts)


func _process(delta: float) -> void:
	if game == null:
		return
	var mp: Vector2 = get_local_mouse_position()
	current_gaze = table.gaze_target(mp)
	table.my_gaze = current_gaze
	var hover: int = table.card_at(mp) if _my_card_turn() else -1
	table.hover_index = hover
	table.show_helper = helper_check.button_pressed
	game.tick(minf(delta, MAX_DT), current_gaze)
	_drain()
	spot.visible = spot_check.button_pressed and not setup_panel.visible
	spot_mat.set_shader_parameter("center_px", mp)
	spot_mat.set_shader_parameter("rect_size", size)
	_refresh()
	table.queue_redraw()


func _my_card_turn() -> bool:
	var ph := int(game.phase)
	return (ph == GambleMatch.Phase.KING_TURN or ph == GambleMatch.Phase.SLAVE_TURN) and game.actor() == 0 and int(game.committed[0]) == -1


func _gui_input(event: InputEvent) -> void:
	var mb := event as InputEventMouseButton
	if mb == null or not mb.pressed or mb.button_index != MOUSE_BUTTON_LEFT:
		return
	if game == null or not _my_card_turn():
		return
	var idx: int = table.card_at(mb.position)
	if idx >= 0:
		game.commit(int(game.hands[0][idx]))
		_drain()


func _unhandled_input(event: InputEvent) -> void:
	var k := event as InputEventKey
	if k == null or not k.pressed or k.echo or game == null:
		return
	if k.keycode == KEY_ENTER or k.keycode == KEY_KP_ENTER or k.keycode == KEY_N:
		_on_next()
		return
	var r := {}
	match k.keycode:
		KEY_1:
			r = game.place_object("lighter")
		KEY_3:
			r = game.place_object("lighter_plain")
		KEY_2:
			r = game.call_accomplice()
		KEY_F:
			r = game.attention()
		KEY_G:
			r = game.gesture()
		KEY_C:
			r = game.cover()
		KEY_R:
			r = game.play_random()
		KEY_X:
			r = game.fake()
		KEY_Q:
			r = game.expose("peek")
		KEY_W:
			r = game.expose("acc")
		_:
			return
	if r.has("ok") and not bool(r["ok"]):
		_log("[color=gray]지금은 못 함 (%s)[/color]" % _why(str(r.get("why", ""))))
	_drain()


func _why(code: String) -> String:
	var table_why := {
		"not_active": "턴 진행 중에만", "full": "물건 자리가 다 참 (%d개)" % CheatRules.OBJECT_SLOTS,
		"not_slave": "노예 측일 때만", "unavailable": "지금은 쓸 수 없음 (이미 씀·남은 횟수 없음·봉인)",
		"not_slave_turn": "노예 턴에만", "no_uses": "남은 횟수 없음", "not_king_turn": "내 왕 턴에만",
		"used": "이번 왕 턴에 이미 씀", "under_10s": "상대 왕 턴이 %.0f초 이상 남았을 때만" % CheatRules.GESTURE_MIN_LEFT,
		"not_king": "왕 측일 때만", "not_king_slave_turn": "왕 측일 때, 노예 턴에만",
		"already_this_turn": "이 속임수는 이번 턴에 이미 밝혀내기 함", "not_your_turn": "내 차례가 아님",
	}
	if table_why.has(code):
		return str(table_why[code])
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
	var me_slave: bool = int(game.slave) == 0
	match kind:
		"round_start":
			var mine: int = ev["sides"][0]
			_log("\n[b]── %s ──[/b] 당신: %s" % [_round_name(int(ev["round"])), RankCards.SIDE_NAMES[mine]])
			if int(ev["king"]) == 0:
				_log("[color=skyblue]왕 측 (방어)[/color] — 내가 먼저 내고, 상대 노예의 눈을 지켜봄 · C 가리기 · R 무작위 · X 바꿔치기 · Q/W 밝혀내기")
			else:
				_log("[color=orange]노예 측 (공격)[/color] — 상대가 먼저 냄 → 물건·협력자를 계속 봐서 카드 확인 · F 시선 끌기 · G 제스처")
		"turn_start":
			_log("%d턴째" % int(ev["turn_in_round"]))
		"phase_start":
			var who := "나" if int(ev["actor"]) == 0 else "상대"
			var ph_name := "왕 턴" if int(ev["phase"]) == GambleMatch.Phase.KING_TURN else "노예 턴"
			var lim := float(ev["limit"])
			var extra := "" if absf(lim - CheatRules.TURN_SECONDS) < 0.01 else " [color=yellow](%+.0f초)[/color]" % (lim - CheatRules.TURN_SECONDS)
			_log("[color=gray]%s — %s · %.0f초%s[/color]" % [ph_name, who, lim, extra])
		"object":
			_render_object(ev)
		"acc_called":
			if int(ev["seat"]) == 0:
				_log("[color=violet]헛기침으로 협력자를 불렀다 — %.1f초 뒤 상대 뒤에 섬[/color]" % CheatRules.ACC_WALK_SECONDS)
			else:
				_log("[color=orange]누군가 당신 뒤로 걸어온다…[/color]")
		"acc_arrived":
			if int(ev["seat"]) == 0:
				_log("[color=cyan]협력자가 상대 뒤에 섰다 — 노예 턴에 그 사람 손을 %.1f초 계속 보면 카드[/color]" % CheatRules.ACC_FIX)
			else:
				_log("[color=orange]당신 뒤에 누군가 서 있다 — 상대 눈이 당신 머리 너머로 가는지 보세요[/color]")
		"attention":
			if int(ev["seat"]) == 0:
				_log("[color=violet]시선 끌기: 술잔을 쓰러뜨렸다 — %.0f초 동안 상대는 내 눈을 못 봄 (불도 안 켜짐)[/color]" % CheatRules.ATTENTION_SECONDS)
			else:
				_log("[color=orange]상대가 술잔을 쓰러뜨렸다! — %.0f초 동안 상대 눈이 안 보임[/color]" % CheatRules.ATTENTION_SECONDS)
		"gesture":
			if int(ev["seat"]) == 0:
				_log("[color=violet]제스처: 손가락으로 테이블을 두드린다 — 상대 왕 턴 −%.0f초[/color]" % CheatRules.GESTURE_CUT)
			else:
				_log("[color=orange]상대가 테이블을 두드리며 재촉한다 — 내 왕 턴 −%.0f초[/color]" % CheatRules.GESTURE_CUT)
		"cover":
			if int(ev["seat"]) == 0:
				_log("[color=skyblue]가리기: 내 카드 위에 칩을 올렸다 — 이번 턴 반사경 엿보기가 안 통함 (협력자는 통함)[/color]")
			else:
				_log("[color=orange]상대가 자기 카드 위에 칩을 올렸다 — 반사경엔 안 비침[/color]")
		"random":
			if int(ev["seat"]) == 0:
				_log("[color=skyblue]무작위: 카드를 보지 않고 냈다 — 엿보기·협력자 둘 다 안 통함[/color]")
			else:
				_log("[color=orange]상대가 카드를 보지도 않고 냈다 (무작위)[/color]")
		"fake":
			if int(ev["seat"]) == 0:
				_log("[color=skyblue]바꿔치기 준비: 엿보는 상대에겐 가짜 카드가 보임[/color]")
			# 상대의 바꿔치기는 숨김 (공개 뒤 알려 줌)
		"info":
			if int(ev["seat"]) == 0:
				var how := "반사경" if str(ev["source"]) == "peek" else "협력자 손 신호"
				_log("[color=cyan]%s: 상대 카드 = %s[/color]" % [how, RankCards.CARD_NAMES[ev["card"]]])
		"info_blocked":
			if int(ev["seat"]) == 0:
				if str(ev["why"]) == "cover":
					_log("[color=gray]반사경에 칩만 비친다 — 가리기에 막힘[/color]")
				else:
					_log("[color=gray]상대도 자기 카드를 안 봤다 — 무작위라 알 수 없음[/color]")
		"light":
			var lk := "엿보기" if str(ev["kind"]) == "peek" else "협력자"
			if int(ev["seat"]) == 1:
				_log("[color=yellow][b]%s 가능성 불![/b] 상대 시선이 고정됐다 — 진짜일까 미끼일까[/color]" % lk)
			else:
				_log("[color=yellow]내 시선이 오래 머물러 상대 쪽 '%s 가능성' 불이 켜졌다[/color]" % lk)
		"timeout":
			_log("[color=yellow]%s 시간 초과 — 무작위 카드를 냈다[/color]" % ("내" if int(ev["seat"]) == 0 else "상대"))
		"expose":
			_render_expose(ev)
		"turn_summary":
			_render_summary(ev)
		"reveal":
			_render_reveal(ev, me_slave)
		"round_end":
			var w := int(ev["winner"])
			_log("판 결과: %s +%d점 · 점수 %d : %d" % ["당신" if w == 0 else "상대", int(ev["points"]),
				int(ev["scores"][0]), int(ev["scores"][1])])
		"match_end":
			var mw := int(ev["winner"])
			var res_text := "무승부"
			if mw == 0:
				res_text = "[color=lime]당신 승리[/color]"
			elif mw == 1:
				res_text = "[color=red]당신 패배[/color]"
			var reason := "두 번 들켜서" if str(ev["reason"]) == "CAUGHT_TWICE" else "점수로"
			_log("\n[b]매치 끝 — %s (%s) · %d : %d[/b]" % [res_text, reason, int(ev["scores"][0]), int(ev["scores"][1])])


func _render_object(ev: Dictionary) -> void:
	var k := str(ev["kind"])
	var n := str(CheatRules.OBJECTS[k]["name"])
	if int(ev["seat"]) == 1:
		_log("[color=orange]상대가 %s%s 꺼내 책상에 놓았다…[/color]" % [n, _eul(n)])
		return
	_log("[color=violet]%s%s 책상에 놓았다 (%s) — 자리 %d[/color]" % [n, _eul(n), "반사경" if CheatRules.is_mirror(k) else "빈 것", int(ev["slot"]) + 1])
	if bool(ev["seen"]):
		_log("[color=orange]…상대가 그걸 봤다. 의심이 커짐[/color]")


func _render_expose(ev: Dictionary) -> void:
	var by := int(ev["by"])
	var kind := str(ev["kind"])
	var hit := bool(ev["hit"])
	var what := "엿보기" if kind == "peek" else "협력자"
	if by == 0:
		if hit:
			var extra := " · 협력자 쫓겨남" if kind == "acc" else ""
			_log("[color=lime][b]밝혀냈다! 상대 %s 적중[/b] — 상대 경고 %d/%d · %s 봉인%s · 상대 턴 −%.0f초[/color]" % [
				what, int(ev["strikes"][1]), CheatRules.STRIKES_TO_LOSE, what, extra, CheatRules.EXPOSE_CUT])
		else:
			_log("[color=yellow]헛짚음 — 상대는 진짜 %s를 쓰지 않았다 · 내 다음 턴 −%.0f초[/color]" % [what, CheatRules.EXPOSE_FAIL_CUT])
		return
	var how := "불을 보고" if str(ev["how"]) == "light" else "눈을 보고"
	if hit:
		var say := "\"그 물건 속에 뭐가 있지?\"" if kind == "peek" else "\"뒤에 그 사람 누구야?\""
		_log("[color=red][b]상대가 %s 밝혀냈다: %s[/b] 내 경고 %d/%d · %s 봉인 · 내 턴 −%.0f초[/color]" % [
			how, say, int(ev["strikes"][0]), CheatRules.STRIKES_TO_LOSE, what, CheatRules.EXPOSE_CUT])
	else:
		_log("[color=lime]상대가 %s 밝혀내기를 했지만 헛짚었다 (미끼였다) — 상대 다음 턴 −%.0f초[/color]" % [what, CheatRules.EXPOSE_FAIL_CUT])


## 턴 끝 리플레이 — 그 턴에 실제로 무슨 일이 있었는지 (공개 뒤라 숨길 필요 없음)
func _render_summary(ev: Dictionary) -> void:
	var lights: Dictionary = ev["lights"]
	var tried: Dictionary = ev["tried"]
	if int(ev["slave"]) == 0:
		return
	var parts := PackedStringArray()
	for kind in ["peek", "acc"]:
		var what := "엿보기" if kind == "peek" else "협력자"
		if bool(tried[kind]):
			parts.append("%s 진짜로 함" % what)
		elif bool(lights[kind]):
			parts.append("%s 불은 미끼" % what)
	if parts.is_empty():
		_log("[color=gray]  └ 리플레이: 상대는 이번 턴 속임수를 쓰지 않았다[/color]")
	else:
		_log("[color=gray]  └ 리플레이: %s[/color]" % ", ".join(parts))


func _render_reveal(ev: Dictionary, me_slave: bool) -> void:
	var c: Array = ev["cards"]
	var r := int(ev["result"])
	var verdict := "비김 — 다음 턴"
	if r > 0:
		verdict = "[color=lime]당신 승[/color]"
	elif r < 0:
		verdict = "[color=red]상대 승[/color]"
	_log("공개: 당신 %s vs 상대 %s → %s" % [RankCards.CARD_NAMES[c[0]], RankCards.CARD_NAMES[c[1]], verdict])
	var faked := bool(ev["faked"])
	var got := str(ev["info"]) != ""
	if not faked:
		return
	if me_slave and got:
		_log("[color=red]속았다 — 비친 카드(%s)는 바꿔치기한 가짜였다[/color]" % RankCards.CARD_NAMES[int(ev["shown"])])
	elif me_slave:
		_log("[color=gray]  └ 상대는 바꿔치기를 준비해 두었었다[/color]")
	elif got:
		var fake_name := str(RankCards.CARD_NAMES[int(ev["shown"])])
		_log("[color=lime]바꿔치기 성공 — 상대는 가짜 %s%s 봤다[/color]" % [fake_name, _eul(fake_name)])


## 받침 있으면 '을', 없으면 '를'
func _eul(word: String) -> String:
	if word.is_empty():
		return "를"
	var code := word.unicode_at(word.length() - 1)
	if code < 0xAC00 or code > 0xD7A3:
		return "를"
	return "을" if (code - 0xAC00) % 28 != 0 else "를"


func _log(text: String) -> void:
	log_view.append_text(text + "\n")


# ───────────────────────── 상태 표시 ─────────────────────────

func _refresh() -> void:
	var ph := int(game.phase)
	var me_king: bool = int(game.king) == 0
	var text := ""
	if ph == GambleMatch.Phase.IDLE:
		text = "사전 설정 — 책상 위 물건을 고르고 '시작'"
	elif ph == GambleMatch.Phase.KING_TURN and me_king:
		text = "내 왕 턴 — 카드를 클릭해 엎어 내기 · C 가리기 · R 무작위로 내기 · X 바꿔치기"
	elif ph == GambleMatch.Phase.KING_TURN:
		text = "상대(왕)가 카드를 고르는 중 — G 제스처(상대 시간 −%.0f초, %.0f초 이상 남았을 때) · 2 협력자 부르기 · 1/3 물건 놓기" % [CheatRules.GESTURE_CUT, CheatRules.GESTURE_MIN_LEFT]
	elif ph == GambleMatch.Phase.SLAVE_TURN and me_king:
		text = "노예 턴 — 상대 눈을 지켜보세요. 불이 켜지면 Q 엿보기 / W 협력자 밝혀내기 (헛짚으면 내 다음 턴 −%.0f초)" % CheatRules.EXPOSE_FAIL_CUT
	elif ph == GambleMatch.Phase.SLAVE_TURN:
		text = "내 노예 턴 — 반사경 물건을 %.1f초, 협력자를 %.1f초 '계속' 보면 상대 카드 · F 시선 끌기 · 카드 클릭으로 내기" % [CheatRules.PEEK_FIX, CheatRules.ACC_FIX]
	elif ph == GambleMatch.Phase.REVEALED:
		text = "Enter 다음"
	elif ph == GambleMatch.Phase.MATCH_OVER:
		text = "매치 끝 — '새 매치'"
	banner.text = text
	var active: bool = ph == GambleMatch.Phase.KING_TURN or ph == GambleMatch.Phase.SLAVE_TURN
	var left: float = float(game.time_left()) if active else 0.0
	timer_bar.value = clampf(left / maxf(float(game.limit), 0.01), 0.0, 1.0) * 100.0 if active else 0.0
	timer_label.text = "%.1f초" % left if active else ""
	var role := "왕 측(방어)" if me_king else "노예 측(공격)"
	if ph == GambleMatch.Phase.IDLE:
		role = "-"
	var pend := ""
	if float(game.pending_time[0]) < 0.0:
		pend = "\n다음 내 턴 %+.0f초" % float(game.pending_time[0])
	status_label.text = "%s · %s\n점수 %d : %d\n내 경고 %s · 상대 경고 %s%s" % [
		_round_name(int(game.round_index)), role, int(game.scores[0]), int(game.scores[1]),
		_dots(int(game.strikes[0])), _dots(int(game.strikes[1])), pend]
	keys_label.text = _keys_text(me_king)
	# 가능성 불
	var show_lamps: bool = ph == GambleMatch.Phase.SLAVE_TURN or ph == GambleMatch.Phase.REVEALED
	lamp_caption.text = "상대 노예의 속임수 가능성" if me_king else "내 시선이 상대에게 켠 불"
	for kind in ["peek", "acc"]:
		var on: bool = show_lamps and bool(game.lights[kind])
		var sealed_txt := ""
		var slave_seat := int(game.slave)
		if bool(game.sealed[slave_seat][kind]):
			sealed_txt = " (봉인)"
		lamp_rects[kind].color = LAMP_ON if on else LAMP_OFF
		lamp_labels[kind].text = ("엿보기 가능성" if kind == "peek" else "협력자 가능성") + sealed_txt
		lamp_labels[kind].add_theme_color_override("font_color", Color(0.1, 0.05, 0.0) if on else Color(0.8, 0.8, 0.8))
	next_btn.disabled = ph != GambleMatch.Phase.REVEALED


func _keys_text(me_king: bool) -> String:
	if me_king:
		return "왕일 때 (방어)\n클릭: 카드 엎어 내기\nC 가리기 %d번 — 반사경 막음\nR 무작위로 내기 %d번 — 둘 다 막음\nX 바꿔치기 %d번 — 가짜를 보여 줌\nQ 엿보기 / W 협력자 밝혀내기\nEnter 다음" % [
			int(game.cover_left[0]), int(game.random_left[0]), int(game.fake_left[0])]
	var acc := "%d번" % int(game.acc_calls_left[0])
	if str(game.acc_state[0]) == "out" or bool(game.sealed[0]["acc"]):
		acc = "봉인"
	elif str(game.acc_state[0]) != "none":
		acc = "와 있음"
	var peek := " (봉인)" if bool(game.sealed[0]["peek"]) else ""
	return "노예일 때 (공격)\n1 반사경 라이터 · 3 빈 라이터 놓기%s\n2 협력자 부르기 (%s)\nF 시선 끌기 %d번 (노예 턴)\nG 제스처 (상대 왕 턴)\n클릭: 카드 내기 · Enter 다음" % [
		peek, acc, int(game.attention_left[0])]


func _round_name(idx: int) -> String:
	if idx >= GambleMatch.ROUNDS:
		return "연장 %d판" % (idx - GambleMatch.ROUNDS + 1)
	return "%d/%d판" % [maxi(idx, 0) + 1, GambleMatch.ROUNDS]


func _dots(n: int) -> String:
	return "●".repeat(n) + "○".repeat(maxi(CheatRules.STRIKES_TO_LOSE - n, 0))
