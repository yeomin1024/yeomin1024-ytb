# VERSION: v0.7.0 — 2026-11-26 — 기록 창(채팅식) 없앰 → 가운데 알림·턴 결과 창·테이블 표시 · 점수판·지금 할 일·큰 시간 막대 · 큰 행동 버튼(지금 역할만, 못 쓰는 까닭, 불 켜지면 깜빡) · 버튼 위에선 시선 유지 · 규칙 창
# 이전 VERSION: v0.6.0 — 2026-11-26 — 기능마다 버튼(노예 열·왕 열, 못 쓰면 흐리게·남은 횟수·단축키) · 판단 시간 안내·타이머·'판단 끝·공개'
# 이전 VERSION: v0.5.0 — 2026-11-26 — 사전 설정(책상 위 물건 3자리) · 왕 턴/노예 턴 · 진영별 키 · 가능성 불 두 개 · 새 이벤트 기록
# 이전 VERSION: v0.4.0 — 2026-11-26 — 키 행동: 라이터 놓기 · 협력자 부르기 · 카드 덮개 · 블러핑 · 안내·기록
# 이전 VERSION: v0.3.0 — 2026-11-26 — 안내 문구: 노예(암살자) 측 판 = 속임수 판, 왕 측 판 = 감시 판
# 이전 VERSION: v0.2.0 — 2026-11-26 — 실시간 화면: 마우스 = 시선 · 시야 제한(보는 곳만 밝게) · 스페이스 = 잡았다
#
# 화면 구성 (1280×800):
#   왼쪽 위 점수판(판·점수·내 역할·경고) · 가운데 위 '지금 할 일' + 시간 막대 · 오른쪽 위 설정 · 오른쪽 가능성 불 두 개 + 협력자 상태
#   왼쪽 큰 행동 버튼 (지금 역할 것만 · 못 쓰면 까닭 · 단축키 칩) · 가운데 알림(잠깐 떴다 사라짐) · 공개되면 턴 결과 창
# 조작: 마우스가 가리키는 곳 = 내 시선 · 카드 클릭 = 내기 · 행동 = 왼쪽 버튼 또는 단축키
#   버튼·설정 위에 마우스가 있는 동안엔 시선이 마지막 자리 그대로 (엿보다 버튼을 눌러도 고정이 안 끊김)
# 버튼을 쓸 수 있는지는 core/match.gd why_not() 하나로 판정. 규칙은 core/, 그림은 scenes/table_view.gd.
# 연구·교육용 데모 — 실제 돈과 관계없음.
extends Control

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const AiBrain = preload("res://core/ai_brain.gd")
const GambleMatch = preload("res://core/match.gd")
const TableView = preload("res://scenes/table_view.gd")

const OPPONENTS := ["cheater", "watcher", "gambler"]
const OPP_NAMES := {"cheater": "손버릇 나쁜 딜러", "watcher": "눈이 매서운 노인", "gambler": "대담한 도박꾼"}
const SETUP_KINDS := ["", "lighter", "lighter_plain", "cigcase", "cigcase_plain", "glass", "phone"]
const SETUP_NAMES := ["없음", "라이터 (반사경)", "라이터 (빈 것)", "담뱃갑 (반사경)", "담뱃갑 (빈 것)", "술잔", "휴대폰"]
const SETUP_DEFAULT := [1, 4, 0]
## 행동 버튼: [id, 역할, 이름, 단축키, 짧은 설명]
const ACTIONS := [
	["lighter", "slave", "반사경 라이터 놓기", "1", "1.5초 보면 상대 카드"],
	["lighter_plain", "slave", "빈 라이터 놓기", "3", "미끼 — 상대에게 불만 켜짐"],
	["accomplice", "slave", "협력자 부르기", "2", "상대 뒤에 섬"],
	["attention", "slave", "시선 끌기", "F", "3초간 상대가 내 눈을 못 봄"],
	["gesture", "slave", "제스처", "G", "상대 왕 시간 −5초"],
	["cover", "king", "가리기", "C", "반사경 막기"],
	["random", "king", "무작위로 내기", "R", "엿보기·협력자 둘 다 막기"],
	["fake", "king", "바꿔치기", "X", "엿보면 가짜가 보임"],
	["expose_peek", "king", "엿보기 밝혀내기", "Q", "맞히면 상대 경고, 틀리면 내 −5초"],
	["expose_acc", "king", "협력자 밝혀내기", "W", "맞히면 상대 경고, 틀리면 내 −5초"],
	["judge_done", "king", "판단 끝 · 공개", "Enter", "바로 카드 공개"],
]
const RULES_BB := "[font_size=20][b]한 턴의 흐름[/b][/font_size]\n" \
	+ "[color=#8cc8ff]왕[/color]이 먼저 카드를 엎어 냄  →  [color=#ffb35a]노예[/color]가 엿보고 냄  →  왕이 5초 판단  →  공개\n\n" \
	+ "[color=#ffb35a][b]노예 (공격)[/b][/color]  반사경이 든 물건을 [b]1.5초[/b], 상대 뒤 협력자의 손을 [b]1.8초[/b] [u]계속[/u] 보면 상대 카드가 보여요. 눈을 떼면 처음부터.\n" \
	+ "[color=#8cc8ff][b]왕 (방어)[/b][/color]  노예 시선이 그만큼 머물면 [color=#ffc83d]가능성 불[/color]이 켜져요 (미끼일 수도). 의심되면 [b]밝혀내기[/b].\n" \
	+ "밝혀내기: 맞히면 상대 [color=#ff5a5a]경고[/color] +1·그 속임수 봉인·상대 −5초 / 틀리면 내 다음 차례 −5초\n\n" \
	+ "[color=#ff5a5a][b]경고 2개 = 즉시 패배[/b][/color] · 카드: 왕 > 시민 > 암살자 > 왕 · 점수: 왕 측 승 +1, 노예 측 승 +4 · 6판\n" \
	+ "[color=#aaaaaa]마우스 = 내 시선 · 행동은 왼쪽 버튼(버튼 위에선 시선이 그대로) 또는 단축키 · 연구·교육용 데모, 실제 돈과 무관[/color]"
const TOAST_SECONDS := 2.6
const TOAST_MAX := 3
const TOAST_COLORS := {"good": Color(0.08, 0.42, 0.2, 0.93), "bad": Color(0.58, 0.08, 0.08, 0.93),
	"warn": Color(0.6, 0.4, 0.04, 0.93), "info": Color(0.1, 0.2, 0.4, 0.93)}
const C_KING := Color(0.55, 0.8, 1.0)
const C_SLAVE := Color(1.0, 0.7, 0.35)
const C_LAMP := Color(1.0, 0.78, 0.24)
const ACTION_PANEL := Rect2(8, 140, 304, 384)
const SETTINGS_RECT := Rect2(970, 6, 304, 116)
const MAX_DT := 0.1   # 프레임이 끊겨도 한 번에 0.1초 넘게 흐르지 않게
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
var last_game_mouse := Vector2(640, 400)
var clock := 0.0

var spot: ColorRect
var spot_mat: ShaderMaterial
var score_text: RichTextLabel
var title_label: Label
var sub_label: Label
var timer_bar: ProgressBar
var timer_label: Label
var timer_fill: Dictionary = {}
var lamp_caption: Label
var lamp_panels: Dictionary = {}
var lamp_states: Dictionary = {}
var lamp_cache: Dictionary = {}
var acc_label: Label
var action_header: Label
var action_buttons: Dictionary = {}
var toast_box: Control
var toasts: Array = []
var result_panel: Panel
var result_title: Label
var result_body: RichTextLabel
var result_btn: Button
var result_mode := ""
var setup_panel: Panel
var setup_options: Array = []
var help_panel: Panel
var opp_option: OptionButton
var spot_check: CheckBox
var helper_check: CheckBox
var turn_notes: Array = []
var last_reveal: Dictionary = {}
var last_round_end: Dictionary = {}
var last_match_end: Dictionary = {}
var _score_cache := ""
var _timer_cache := ""


func _ready() -> void:
	_build()
	_new_match()


# ───────────────────────── 화면 만들기 ─────────────────────────

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

	_build_top(ui)
	_build_settings(ui)
	_build_lamps(ui)
	_build_actions(ui)
	toast_box = Control.new()
	toast_box.mouse_filter = Control.MOUSE_FILTER_IGNORE
	toast_box.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	ui.add_child(toast_box)
	_build_result(ui)
	_build_setup(ui)
	_build_help(ui)


## 왼쪽 위 점수판 · 가운데 위 '지금 할 일' + 시간 막대
func _build_top(ui: Control) -> void:
	var sp := _panel(Rect2(8, 6, 316, 128), Color(0, 0, 0, 0.62))
	ui.add_child(sp)
	score_text = _rich(Vector2(12, 6), Vector2(296, 118), 16)
	sp.add_child(score_text)

	var bp := _panel(Rect2(336, 6, 624, 116), Color(0, 0, 0, 0.62))
	ui.add_child(bp)
	title_label = _label(Vector2(12, 6), Vector2(600, 36), 24, Color.WHITE)
	title_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	bp.add_child(title_label)
	sub_label = _label(Vector2(12, 42), Vector2(600, 26), 15, Color(0.85, 0.85, 0.85))
	sub_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	bp.add_child(sub_label)
	timer_bar = ProgressBar.new()
	timer_bar.position = Vector2(20, 78)
	timer_bar.size = Vector2(500, 22)
	timer_bar.show_percentage = false
	timer_bar.mouse_filter = Control.MOUSE_FILTER_IGNORE
	timer_bar.add_theme_stylebox_override("background", _sb(Color(0.15, 0.15, 0.18), 6))
	for k in ["mine", "theirs", "hurry"]:
		var c := Color(1.0, 0.82, 0.25)
		if k == "theirs":
			c = Color(0.45, 0.55, 0.7)
		elif k == "hurry":
			c = Color(0.95, 0.25, 0.2)
		timer_fill[k] = _sb(c, 6)
	bp.add_child(timer_bar)
	timer_label = _label(Vector2(528, 72), Vector2(90, 32), 20, Color.WHITE)
	bp.add_child(timer_label)


## 오른쪽 위: 상대 고르기 · 새 매치 · 규칙 · 시야 제한 · 보조선
func _build_settings(ui: Control) -> void:
	var p := _panel(SETTINGS_RECT, Color(0, 0, 0, 0.5))
	ui.add_child(p)
	opp_option = OptionButton.new()
	for k in OPPONENTS:
		opp_option.add_item(OPP_NAMES[k])
	opp_option.position = Vector2(8, 6)
	opp_option.size = Vector2(180, 32)
	opp_option.focus_mode = Control.FOCUS_NONE
	p.add_child(opp_option)
	var nb := _small_button("새 매치", Vector2(196, 6), Vector2(100, 32), _on_new_match)
	p.add_child(nb)
	var hb := _small_button("규칙 (H)", Vector2(196, 44), Vector2(100, 32), _toggle_help)
	p.add_child(hb)
	spot_check = CheckBox.new()
	spot_check.text = "시야 제한"
	spot_check.button_pressed = true
	spot_check.position = Vector2(8, 44)
	spot_check.focus_mode = Control.FOCUS_NONE
	p.add_child(spot_check)
	helper_check = CheckBox.new()
	helper_check.text = "상대 시선 보조선"
	helper_check.position = Vector2(8, 78)
	helper_check.focus_mode = Control.FOCUS_NONE
	p.add_child(helper_check)


## 오른쪽: 가능성 불 두 개 + 협력자 상태
func _build_lamps(ui: Control) -> void:
	lamp_caption = _label(Vector2(976, 130), Vector2(294, 24), 15, Color(0.9, 0.9, 0.9))
	ui.add_child(lamp_caption)
	var y := 156.0
	for kind in ["peek", "acc"]:
		var p := _panel(Rect2(976, y, 294, 58), Color(0.15, 0.15, 0.18, 0.9))
		ui.add_child(p)
		var t := _label(Vector2(14, 4), Vector2(270, 28), 20, Color.WHITE)
		t.text = "엿보기 가능성" if kind == "peek" else "협력자 가능성"
		p.add_child(t)
		var st := _label(Vector2(14, 32), Vector2(270, 22), 14, Color(0.8, 0.8, 0.8))
		p.add_child(st)
		lamp_panels[kind] = p
		lamp_states[kind] = st
		y += 66.0
	acc_label = _label(Vector2(976, 292), Vector2(294, 50), 15, Color(0.9, 0.9, 0.9))
	acc_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	ui.add_child(acc_label)


## 왼쪽: 큰 행동 버튼 — 지금 역할 것만 보이고, 못 쓰면 흐리게 + 까닭
func _build_actions(ui: Control) -> void:
	var ap := _panel(ACTION_PANEL, Color(0, 0, 0, 0.55))
	ui.add_child(ap)
	action_header = _label(Vector2(12, 6), Vector2(282, 28), 19, Color.WHITE)
	ap.add_child(action_header)
	var hint := _label(Vector2(12, 34), Vector2(282, 18), 12, Color(0.7, 0.7, 0.7))
	hint.text = "버튼 위에선 시선이 그대로 — 엿보다 눌러도 돼요"
	ap.add_child(hint)
	action_buttons.clear()
	for a in ACTIONS:
		var id := str(a[0])
		var base := C_SLAVE if str(a[1]) == "slave" else C_KING
		var b := Button.new()
		b.size = Vector2(288, 48)
		b.focus_mode = Control.FOCUS_NONE
		b.add_theme_stylebox_override("normal", _sb(base.darkened(0.55), 10, base.darkened(0.1), 2))
		b.add_theme_stylebox_override("hover", _sb(base.darkened(0.35), 10, Color.WHITE, 2))
		b.add_theme_stylebox_override("pressed", _sb(base.darkened(0.7), 10, Color.WHITE, 3))
		b.add_theme_stylebox_override("disabled", _sb(Color(0.16, 0.16, 0.18, 0.9), 10, Color(0.3, 0.3, 0.32), 1))
		b.add_theme_stylebox_override("focus", StyleBoxEmpty.new())
		b.pressed.connect(_act.bind(id))
		var tl := _label(Vector2(12, 2), Vector2(214, 26), 18, Color.WHITE)
		tl.text = str(a[2])
		b.add_child(tl)
		var sl := _label(Vector2(12, 26), Vector2(214, 20), 12, Color(0.85, 0.85, 0.85))
		b.add_child(sl)
		var key := str(a[3])
		var chip := _panel(Rect2(232, 8, 48, 32), Color(1, 1, 1, 0.14))
		var kl := _label(Vector2.ZERO, Vector2(48, 32), 16 if key.length() <= 1 else 12, Color.WHITE)
		kl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		kl.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
		kl.text = key
		chip.add_child(kl)
		b.add_child(chip)
		ap.add_child(b)
		action_buttons[id] = {"button": b, "sub": sl, "role": str(a[1]), "desc": str(a[4])}


## 공개되면 뜨는 턴 결과 창 (매치 끝도 여기)
func _build_result(ui: Control) -> void:
	result_panel = _panel(Rect2(340, 128, 600, 304), Color(0.04, 0.04, 0.07, 0.96), Color(1, 1, 1, 0.25), 2)
	result_panel.mouse_filter = Control.MOUSE_FILTER_STOP
	ui.add_child(result_panel)
	result_title = _label(Vector2(20, 12), Vector2(560, 46), 34, Color.WHITE)
	result_title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	result_panel.add_child(result_title)
	result_body = _rich(Vector2(28, 62), Vector2(544, 166), 17)
	result_panel.add_child(result_body)
	result_btn = _big_button("다음 ▶", Vector2(170, 236), Vector2(260, 54), _on_result_btn)
	result_panel.add_child(result_btn)
	result_panel.visible = false


## 시작 전 준비 창: 규칙 한눈에 + 책상 위 물건 3자리
func _build_setup(ui: Control) -> void:
	setup_panel = _panel(Rect2(220, 128, 840, 520), Color(0.04, 0.04, 0.07, 0.97), Color(1, 1, 1, 0.25), 2)
	setup_panel.mouse_filter = Control.MOUSE_FILTER_STOP
	ui.add_child(setup_panel)
	var title := _label(Vector2(24, 14), Vector2(792, 40), 28, Color.WHITE)
	title.text = "게임 준비"
	setup_panel.add_child(title)
	var rules := _rich(Vector2(24, 60), Vector2(792, 250), 16)
	rules.text = RULES_BB
	setup_panel.add_child(rules)
	var ot := _label(Vector2(24, 318), Vector2(792, 28), 18, Color(1.0, 0.9, 0.5))
	ot.text = "책상 위에 둘 물건 (반사경이 든 것과 빈 것은 상대 눈엔 똑같아 보여요)"
	setup_panel.add_child(ot)
	setup_options.clear()
	for i in CheatRules.OBJECT_SLOTS:
		var lab := _label(Vector2(24 + i * 268, 354), Vector2(250, 22), 14, Color(0.8, 0.8, 0.8))
		lab.text = "자리 %d" % (i + 1)
		setup_panel.add_child(lab)
		var ob := OptionButton.new()
		for n in SETUP_NAMES:
			ob.add_item(n)
		ob.selected = int(SETUP_DEFAULT[i])
		ob.position = Vector2(24 + i * 268, 378)
		ob.size = Vector2(250, 40)
		ob.focus_mode = Control.FOCUS_NONE
		ob.add_theme_font_size_override("font_size", 17)
		setup_panel.add_child(ob)
		setup_options.append(ob)
	var note := _label(Vector2(24, 424), Vector2(792, 22), 13, Color(0.7, 0.7, 0.7))
	note.text = "게임 중에도 왼쪽 버튼으로 라이터를 더 놓을 수 있어요"
	setup_panel.add_child(note)
	setup_panel.add_child(_big_button("시작 ▶", Vector2(310, 452), Vector2(220, 56), _on_setup_start))


func _build_help(ui: Control) -> void:
	help_panel = _panel(Rect2(220, 128, 840, 380), Color(0.04, 0.04, 0.07, 0.97), Color(1, 1, 1, 0.25), 2)
	help_panel.mouse_filter = Control.MOUSE_FILTER_STOP
	ui.add_child(help_panel)
	var title := _label(Vector2(24, 14), Vector2(600, 40), 26, Color.WHITE)
	title.text = "규칙 한눈에 (보는 동안 시간 멈춤)"
	help_panel.add_child(title)
	var rules := _rich(Vector2(24, 60), Vector2(792, 250), 16)
	rules.text = RULES_BB
	help_panel.add_child(rules)
	help_panel.add_child(_big_button("닫기", Vector2(330, 312), Vector2(180, 50), _toggle_help))
	help_panel.visible = false


# ───────────────────────── 만들기 도우미 ─────────────────────────

func _sb(bg: Color, radius: int = 10, border: Color = Color(0, 0, 0, 0), bw: int = 0) -> StyleBoxFlat:
	var sb := StyleBoxFlat.new()
	sb.bg_color = bg
	sb.set_corner_radius_all(radius)
	if bw > 0:
		sb.border_color = border
		sb.set_border_width_all(bw)
	return sb


func _panel(r: Rect2, bg: Color, border: Color = Color(0, 0, 0, 0), bw: int = 0) -> Panel:
	var p := Panel.new()
	p.position = r.position
	p.size = r.size
	p.mouse_filter = Control.MOUSE_FILTER_IGNORE
	p.add_theme_stylebox_override("panel", _sb(bg, 10, border, bw))
	return p


func _label(pos: Vector2, box: Vector2, font_size: int, col: Color) -> Label:
	var l := Label.new()
	l.position = pos
	l.size = box
	l.add_theme_font_size_override("font_size", font_size)
	l.add_theme_color_override("font_color", col)
	l.add_theme_color_override("font_outline_color", Color(0, 0, 0))
	l.add_theme_constant_override("outline_size", 5)
	l.mouse_filter = Control.MOUSE_FILTER_IGNORE
	return l


func _rich(pos: Vector2, box: Vector2, font_size: int) -> RichTextLabel:
	var r := RichTextLabel.new()
	r.bbcode_enabled = true
	r.scroll_active = false
	r.position = pos
	r.size = box
	r.mouse_filter = Control.MOUSE_FILTER_IGNORE
	r.add_theme_font_size_override("normal_font_size", font_size)
	r.add_theme_font_size_override("bold_font_size", font_size)
	return r


func _small_button(text: String, pos: Vector2, box: Vector2, cb: Callable) -> Button:
	var b := Button.new()
	b.text = text
	b.position = pos
	b.size = box
	b.focus_mode = Control.FOCUS_NONE
	b.add_theme_font_size_override("font_size", 14)
	b.pressed.connect(cb)
	return b


func _big_button(text: String, pos: Vector2, box: Vector2, cb: Callable) -> Button:
	var b := _small_button(text, pos, box, cb)
	b.add_theme_font_size_override("font_size", 22)
	b.add_theme_stylebox_override("normal", _sb(Color(0.85, 0.62, 0.12), 12))
	b.add_theme_stylebox_override("hover", _sb(Color(1.0, 0.76, 0.22), 12))
	b.add_theme_stylebox_override("pressed", _sb(Color(0.65, 0.45, 0.08), 12))
	b.add_theme_stylebox_override("focus", StyleBoxEmpty.new())
	b.add_theme_color_override("font_color", Color(0.08, 0.06, 0.02))
	b.add_theme_color_override("font_hover_color", Color(0.08, 0.06, 0.02))
	b.add_theme_color_override("font_pressed_color", Color(0.08, 0.06, 0.02))
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
	table.seen_card = -1
	table.seen_source = ""
	turn_notes.clear()
	last_reveal = {}
	last_round_end = {}
	last_match_end = {}
	result_mode = ""
	result_panel.visible = false
	help_panel.visible = false
	_clear_toasts()
	_score_cache = ""
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
	game.start()
	_drain()


func _toggle_help() -> void:
	help_panel.visible = not help_panel.visible


func _on_result_btn() -> void:
	if game == null:
		return
	if int(game.phase) == GambleMatch.Phase.MATCH_OVER:
		_new_match()
		return
	if int(game.phase) == GambleMatch.Phase.REVEALED:
		result_panel.visible = false
		game.next()
		_drain()


func _process(delta: float) -> void:
	if game == null:
		return
	clock += delta
	_update_toasts(delta)
	var mp: Vector2 = get_local_mouse_position()
	var over_ui := _over_ui(mp)
	if not over_ui:
		last_game_mouse = mp
		current_gaze = table.gaze_target(mp)
	table.my_gaze = current_gaze
	table.hover_index = table.card_at(mp) if _my_card_turn() and not over_ui else -1
	table.show_helper = helper_check.button_pressed
	if not help_panel.visible:
		game.tick(minf(delta, MAX_DT), current_gaze)
	_drain()
	spot.visible = spot_check.button_pressed and not setup_panel.visible
	spot_mat.set_shader_parameter("center_px", last_game_mouse)
	spot_mat.set_shader_parameter("rect_size", size)
	_refresh()
	table.queue_redraw()


## 버튼·설정·창 위에서는 시선을 바꾸지 않음 (버튼을 누르러 가도 보던 곳 그대로)
func _over_ui(mp: Vector2) -> bool:
	if setup_panel.visible or help_panel.visible or result_panel.visible:
		return true
	return ACTION_PANEL.has_point(mp) or SETTINGS_RECT.has_point(mp)


func _my_card_turn() -> bool:
	var ph := int(game.phase)
	return (ph == GambleMatch.Phase.KING_TURN or ph == GambleMatch.Phase.SLAVE_TURN) and game.actor() == 0 and int(game.committed[0]) == -1


func _gui_input(event: InputEvent) -> void:
	var mb := event as InputEventMouseButton
	if mb == null or not mb.pressed or mb.button_index != MOUSE_BUTTON_LEFT:
		return
	if game == null or not _my_card_turn() or _over_ui(mb.position):
		return
	var idx: int = table.card_at(mb.position)
	if idx >= 0:
		game.commit(int(game.hands[0][idx]))
		_drain()


func _unhandled_input(event: InputEvent) -> void:
	var k := event as InputEventKey
	if k == null or not k.pressed or k.echo or game == null:
		return
	if k.keycode == KEY_H or (k.keycode == KEY_ESCAPE and help_panel.visible):
		_toggle_help()
		return
	if k.keycode == KEY_ENTER or k.keycode == KEY_KP_ENTER or k.keycode == KEY_N:
		if setup_panel.visible:
			_on_setup_start()
		elif result_panel.visible:
			_on_result_btn()
		elif int(game.phase) == GambleMatch.Phase.JUDGE:
			_act("judge_done")
		return
	var id := ""
	match k.keycode:
		KEY_1:
			id = "lighter"
		KEY_3:
			id = "lighter_plain"
		KEY_2:
			id = "accomplice"
		KEY_F:
			id = "attention"
		KEY_G:
			id = "gesture"
		KEY_C:
			id = "cover"
		KEY_R:
			id = "random"
		KEY_X:
			id = "fake"
		KEY_Q:
			id = "expose_peek"
		KEY_W:
			id = "expose_acc"
		_:
			return
	_act(id)


## 버튼·단축키 공통 — 규칙은 core/match.gd
func _act(id: String) -> void:
	if game == null or help_panel.visible:
		return
	var r := {}
	match id:
		"lighter":
			r = game.place_object("lighter")
		"lighter_plain":
			r = game.place_object("lighter_plain")
		"accomplice":
			r = game.call_accomplice()
		"attention":
			r = game.attention()
		"gesture":
			r = game.gesture()
		"cover":
			r = game.cover()
		"random":
			r = game.play_random()
		"fake":
			r = game.fake()
		"expose_peek":
			r = game.expose("peek")
		"expose_acc":
			r = game.expose("acc")
		"judge_done":
			r = game.judge_done()
		_:
			return
	if r.has("ok") and not bool(r["ok"]):
		_toast("지금은 못 해요 — " + _short_why(id, str(r.get("why", ""))), "info")
	_drain()


## 버튼 id → match.gd why_not(action, arg)
func _rule_of(id: String) -> Array:
	match id:
		"lighter", "lighter_plain":
			return ["object", id]
		"expose_peek":
			return ["expose", "peek"]
		"expose_acc":
			return ["expose", "acc"]
	return [id, ""]


## 못 쓰는 까닭을 짧게 (버튼 아랫줄·알림)
func _short_why(id: String, code: String) -> String:
	match code:
		"not_active":
			return "턴 진행 중에만"
		"full":
			return "물건 자리가 꽉 참"
		"not_slave":
			return "노예일 때만"
		"unavailable":
			if id == "accomplice":
				var st := str(game.acc_state[0])
				if st == "out" or bool(game.sealed[0]["acc"]):
					return "쫓겨남 (봉인)"
				if st != "none":
					return "이미 와 있음"
			if id == "cover" and bool(game.covered):
				return "이미 가림"
			if id == "fake" and bool(game.faked):
				return "이미 준비됨"
			if id == "fake" and bool(game.info_done):
				return "상대가 이미 봄"
			return "남은 횟수 없음 / 지금은 안 됨"
		"not_slave_turn":
			return "내 노예 턴에만"
		"no_uses":
			return "남은 횟수 없음"
		"not_king_turn":
			return "상대 왕 턴에만" if id == "gesture" else "내 왕 턴(내기 전)에만"
		"used":
			return "이번 턴에 이미 씀"
		"under_10s":
			return "상대 시간이 %.0f초 넘게 남았을 때만" % CheatRules.GESTURE_MIN_LEFT
		"not_king":
			return "왕일 때만"
		"not_king_slave_turn":
			return "상대가 엿볼 때·판단 시간에만"
		"already_this_turn":
			return "이번 턴에 이미 함"
		"sealed":
			return "봉인됨 — 상대가 더는 못 씀"
		"not_judge":
			return "판단 시간에만"
	return code


# ───────────────────────── 알림 ─────────────────────────

func _toast(text: String, kind: String = "info") -> void:
	var col: Color = TOAST_COLORS.get(kind, TOAST_COLORS["info"])
	var p := _panel(Rect2(0, 0, 640, 46), col)
	var l := _label(Vector2(10, 0), Vector2(620, 46), 21, Color.WHITE)
	l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	l.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	l.text = text
	p.add_child(l)
	toast_box.add_child(p)
	toasts.append({"node": p, "age": 0.0})
	while toasts.size() > TOAST_MAX:
		var old: Dictionary = toasts.pop_front()
		(old["node"] as Node).queue_free()
	_layout_toasts()


func _update_toasts(delta: float) -> void:
	var i := 0
	var changed := false
	while i < toasts.size():
		var t: Dictionary = toasts[i]
		t["age"] = float(t["age"]) + delta
		var n: Control = t["node"]
		var left := TOAST_SECONDS - float(t["age"])
		if left <= 0.0:
			n.queue_free()
			toasts.remove_at(i)
			changed = true
			continue
		n.modulate.a = clampf(left / 0.5, 0.0, 1.0)
		i += 1
	if changed:
		_layout_toasts()


func _layout_toasts() -> void:
	for i in toasts.size():
		var n: Control = toasts[i]["node"]
		n.position = Vector2(320, 292 + i * 52)


func _clear_toasts() -> void:
	for t in toasts:
		(t["node"] as Node).queue_free()
	toasts.clear()


# ───────────────────────── 이벤트 → 알림·결과 ─────────────────────────

func _drain() -> void:
	for ev in game.pop_events():
		_render(ev)
	var ph := int(game.phase)
	if ph == GambleMatch.Phase.MATCH_OVER and result_mode != "match":
		_show_result("match")
	elif ph == GambleMatch.Phase.REVEALED and result_mode == "":
		_show_result("turn")


## 이벤트마다 짧은 알림 — 상대가 숨긴 것(바꿔치기·상대가 얻은 정보)은 공개 전엔 안 보여 줌
func _render(ev: Dictionary) -> void:
	var kind := str(ev["type"])
	match kind:
		"round_start":
			var me_king: bool = int(ev["king"]) == 0
			_toast("%s — 당신은 %s" % [_round_name(int(ev["round"])), "왕 (방어)" if me_king else "노예 (공격)"], "info")
		"turn_start":
			turn_notes.clear()
			last_reveal = {}
			last_round_end = {}
			result_mode = ""
			table.seen_card = -1
			table.seen_source = ""
		"phase_start":
			var lim := float(ev["limit"])
			if lim < CheatRules.TURN_SECONDS - 0.01:
				var mine_turn: bool = int(ev["actor"]) == 0
				_toast("%s 이번 차례 시간 %.0f초 (깎임)" % ["내" if mine_turn else "상대", lim], "bad" if mine_turn else "good")
		"object":
			var n := str(CheatRules.OBJECTS[str(ev["kind"])]["name"])
			if int(ev["seat"]) == 1:
				_toast("상대가 %s%s 책상에 놓았다" % [n, _eul(n)], "warn")
			elif bool(ev["seen"]):
				_toast("%s%s 놓았다 — 상대가 봤다, 의심 ↑" % [n, _eul(n)], "warn")
			else:
				_toast("%s%s 놓았다 (%s)" % [n, _eul(n), "반사경" if CheatRules.is_mirror(str(ev["kind"])) else "빈 것"], "info")
		"acc_called":
			if int(ev["seat"]) == 0:
				_toast("협력자를 불렀다 — 곧 상대 뒤에 섬", "info")
			else:
				_toast("누군가 당신 뒤로 걸어온다…", "warn")
		"acc_arrived":
			if int(ev["seat"]) == 0:
				_toast("협력자 도착 — 노예 턴에 그 손을 1.8초 보기", "good")
			else:
				_toast("당신 뒤에 누군가 서 있다!", "warn")
		"attention":
			if int(ev["seat"]) == 0:
				_toast("시선 끌기 성공 — 3초 동안 상대가 못 봄", "good")
			else:
				_toast("상대가 술잔을 쓰러뜨렸다 — 3초간 눈이 안 보임", "warn")
		"gesture":
			if int(ev["seat"]) == 0:
				_toast("제스처 — 상대 시간 −%.0f초" % CheatRules.GESTURE_CUT, "good")
			else:
				_toast("상대가 재촉한다 — 내 시간 −%.0f초" % CheatRules.GESTURE_CUT, "bad")
		"cover":
			if int(ev["seat"]) == 0:
				_toast("칩으로 가렸다 — 반사경 차단", "good")
			else:
				_toast("상대가 칩으로 가렸다 — 반사경 안 통함", "warn")
		"random":
			if int(ev["seat"]) == 0:
				_toast("안 보고 냈다 — 엿보기·협력자 차단", "good")
			else:
				_toast("상대가 카드를 안 보고 냈다 — 엿볼 수 없음", "warn")
		"fake":
			if int(ev["seat"]) == 0:
				_toast("바꿔치기 준비 — 엿보면 가짜가 보임", "good")
		"info":
			if int(ev["seat"]) == 0:
				var c := str(RankCards.CARD_NAMES[int(ev["card"])])
				table.seen_card = int(ev["card"])
				table.seen_source = str(ev["source"])
				_toast("보였다! 상대 카드 = %s" % c, "good")
				turn_notes.append("엿본 카드: %s (%s)" % [c, "반사경" if str(ev["source"]) == "peek" else "협력자"])
		"info_blocked":
			if int(ev["seat"]) == 0:
				var msg := "칩에 가려 안 보인다" if str(ev["why"]) == "cover" else "상대도 안 보고 냈다 — 알 수 없음"
				_toast(msg, "warn")
				turn_notes.append(msg)
		"light":
			var lk := "엿보기" if str(ev["kind"]) == "peek" else "협력자"
			if int(ev["seat"]) == 1:
				_toast("%s 가능성 불! 상대 시선이 머물렀다" % lk, "warn")
			else:
				_toast("내 시선 때문에 상대에게 '%s' 불이 켜졌다" % lk, "warn")
		"judge_start":
			if int(ev["king"]) == 0:
				_toast("상대가 냈다 — %.0f초 안에 판단하세요" % float(ev["limit"]), "info")
		"timeout":
			var mine := int(ev["seat"]) == 0
			_toast("%s 시간 초과 — 아무 카드나 냈다" % ("내" if mine else "상대"), "bad" if mine else "info")
			if mine:
				turn_notes.append("시간 초과로 아무 카드나 냄")
		"expose":
			_render_expose(ev)
		"turn_summary":
			_note_summary(ev)
		"reveal":
			last_reveal = ev
		"round_end":
			last_round_end = ev
		"match_end":
			last_match_end = ev


func _render_expose(ev: Dictionary) -> void:
	var by := int(ev["by"])
	var hit := bool(ev["hit"])
	var what := "엿보기" if str(ev["kind"]) == "peek" else "협력자"
	var msg := ""
	var tone := "info"
	if by == 0 and hit:
		msg = "밝혀냈다! 상대 경고 %d/%d · %s 봉인" % [int(ev["strikes"][1]), CheatRules.STRIKES_TO_LOSE, what]
		tone = "good"
	elif by == 0:
		msg = "헛짚음 — 상대는 %s를 안 썼다 · 내 다음 차례 −%.0f초" % [what, CheatRules.EXPOSE_FAIL_CUT]
		tone = "bad"
	elif hit:
		msg = "들켰다! 내 경고 %d/%d · %s 봉인" % [int(ev["strikes"][0]), CheatRules.STRIKES_TO_LOSE, what]
		tone = "bad"
	else:
		msg = "상대가 헛짚었다 — 상대 다음 차례 −%.0f초" % CheatRules.EXPOSE_FAIL_CUT
		tone = "good"
	_toast(msg, tone)
	turn_notes.append(msg)


## 턴 끝 사실 (공개 뒤라 숨길 필요 없음) — 내가 왕이었을 때 상대가 진짜로 했는지
func _note_summary(ev: Dictionary) -> void:
	if int(ev["slave"]) == 0:
		return
	var lights: Dictionary = ev["lights"]
	var tried: Dictionary = ev["tried"]
	var parts := PackedStringArray()
	for k in ["peek", "acc"]:
		var what := "반사경" if k == "peek" else "협력자"
		if bool(tried[k]):
			parts.append("상대는 %s를 진짜로 봤다" % what)
		elif bool(lights[k]):
			parts.append("%s 불은 미끼였다" % what)
	if parts.is_empty():
		parts.append("상대는 이번 턴 속임수를 안 썼다")
	turn_notes.append(" · ".join(parts))


func _show_result(mode: String) -> void:
	result_mode = mode
	_clear_toasts()
	var body := PackedStringArray()
	if mode == "match":
		var w := int(last_match_end.get("winner", game.winner))
		var reason := str(last_match_end.get("reason", game.end_reason))
		if w == 0:
			result_title.text = "매치 승리!"
			result_title.add_theme_color_override("font_color", Color(0.45, 1.0, 0.5))
		elif w == 1:
			result_title.text = "매치 패배"
			result_title.add_theme_color_override("font_color", Color(1.0, 0.4, 0.35))
		else:
			result_title.text = "무승부"
			result_title.add_theme_color_override("font_color", Color.WHITE)
		if reason == "CAUGHT_TWICE":
			body.append("[center][font_size=22]%s[/font_size][/center]" % ("상대가 두 번 들켰다" if w == 0 else "두 번 들켰다 — 즉시 패배"))
		body.append("[center][font_size=22]최종 점수  나 %d : %d 상대[/font_size][/center]" % [int(game.scores[0]), int(game.scores[1])])
		if reason == "CAUGHT_TWICE":
			for note in turn_notes:
				body.append("[center][color=#cccccc]%s[/color][/center]" % str(note))
		result_btn.text = "새 매치 ▶"
	else:
		var r := int(last_reveal.get("result", 0))
		if r > 0:
			result_title.text = "이겼다!"
			result_title.add_theme_color_override("font_color", Color(0.45, 1.0, 0.5))
		elif r < 0:
			result_title.text = "졌다"
			result_title.add_theme_color_override("font_color", Color(1.0, 0.4, 0.35))
		else:
			result_title.text = "비김"
			result_title.add_theme_color_override("font_color", Color(0.85, 0.85, 0.85))
		var cards: Array = last_reveal.get("cards", [-1, -1])
		body.append("[center][font_size=22]나 [b]%s[/b]   vs   상대 [b]%s[/b][/font_size][/center]" % [_card_name(int(cards[0])), _card_name(int(cards[1]))])
		if not last_round_end.is_empty():
			var w2 := int(last_round_end["winner"])
			body.append("[center]%s +%d점 → 점수 [b]%d : %d[/b][/center]" % ["내가" if w2 == 0 else "상대가", int(last_round_end["points"]),
				int(last_round_end["scores"][0]), int(last_round_end["scores"][1])])
		else:
			body.append("[center][color=#cccccc]같은 판, 남은 카드로 다음 턴[/color][/center]")
		for note in turn_notes:
			body.append("[center][color=#cccccc]%s[/color][/center]" % str(note))
		var faked := bool(last_reveal.get("faked", false))
		var got := str(last_reveal.get("info", "")) != ""
		if faked and got and int(game.slave) == 0:
			body.append("[center][color=#ff6b6b]속았다 — 본 카드는 바꿔치기한 가짜[/color][/center]")
		elif faked and got:
			body.append("[center][color=#7dff8a]바꿔치기 성공 — 상대는 가짜를 봤다[/color][/center]")
		elif faked and int(game.slave) == 0:
			body.append("[center][color=#cccccc]상대는 바꿔치기를 준비해 두었었다[/color][/center]")
		result_btn.text = "다음 판 ▶" if bool(game.round_over) else "다음 턴 ▶"
	result_body.text = "\n".join(body)
	result_panel.visible = true


# ───────────────────────── 매 프레임 표시 ─────────────────────────

func _refresh() -> void:
	var ph := int(game.phase)
	var me_king: bool = int(game.king) == 0
	_refresh_score(ph, me_king)
	_refresh_banner(ph, me_king)
	_refresh_lamps(ph, me_king)
	_refresh_actions(ph, me_king)


func _refresh_score(ph: int, me_king: bool) -> void:
	var role := "-"
	if ph != GambleMatch.Phase.IDLE:
		role = "[color=#8cc8ff][b]왕 (방어)[/b][/color]" if me_king else "[color=#ffb35a][b]노예 (공격)[/b][/color]"
	var pend := ""
	if float(game.pending_time[0]) < 0.0:
		pend = "   [color=#ff6b6b]다음 내 차례 %+.0f초[/color]" % float(game.pending_time[0])
	var txt := "[color=#aaaaaa]%s · 상대: %s[/color]\n[font_size=26]나 [b]%d[/b] : [b]%d[/b] 상대[/font_size]\n당신: %s%s\n경고  나 %s   상대 %s" % [
		_round_name(int(game.round_index)), OPP_NAMES[opponent_kind], int(game.scores[0]), int(game.scores[1]), role, pend,
		_dots_bb(int(game.strikes[0])), _dots_bb(int(game.strikes[1]))]
	if txt != _score_cache:
		_score_cache = txt
		score_text.text = txt


func _refresh_banner(ph: int, me_king: bool) -> void:
	var title := ""
	var sub := ""
	var my_move := false
	match ph:
		GambleMatch.Phase.IDLE:
			title = "책상 위 물건을 고르고 시작하세요"
		GambleMatch.Phase.KING_TURN:
			if me_king:
				title = "내 차례 — 카드를 골라 엎으세요"
				sub = "엿보기를 막으려면: 가리기 · 무작위로 내기 · 바꿔치기"
				my_move = true
			else:
				title = "상대(왕)가 카드를 고르는 중"
				sub = "제스처로 상대 시간 줄이기 · 협력자 부르기 · 라이터 놓기"
		GambleMatch.Phase.SLAVE_TURN:
			if me_king:
				title = "상대가 엿보는 중 — 눈을 지켜보세요"
				sub = "불이 켜지면 밝혀내기 · 상대가 내도 %.0f초 판단 시간이 있어요" % CheatRules.JUDGE_SECONDS
			else:
				title = "내 차례 — 엿보고 카드를 내세요"
				sub = "반사경 물건 %.1f초 · 협력자 손 %.1f초 계속 보기 → 카드 클릭" % [CheatRules.PEEK_FIX, CheatRules.ACC_FIX]
				my_move = true
		GambleMatch.Phase.JUDGE:
			if me_king:
				title = "판단하세요 — 상대가 속임수를 썼을까?"
				sub = "썼다고 보면 밝혀내기 · 아니면 '판단 끝 · 공개'"
				my_move = true
			else:
				title = "상대가 판단 중…"
		GambleMatch.Phase.REVEALED:
			title = "공개!"
		GambleMatch.Phase.MATCH_OVER:
			title = "매치 끝"
	if title_label.text != title:
		title_label.text = title
		title_label.add_theme_color_override("font_color", Color(1.0, 0.88, 0.35) if my_move else Color(0.92, 0.92, 0.95))
	if sub_label.text != sub:
		sub_label.text = sub
	var active: bool = ph == GambleMatch.Phase.KING_TURN or ph == GambleMatch.Phase.SLAVE_TURN
	var judging: bool = ph == GambleMatch.Phase.JUDGE
	var left := 0.0
	var total := 1.0
	if active:
		left = float(game.time_left())
		total = float(game.limit)
	elif judging:
		left = maxf(float(game.judge_left), 0.0)
		total = float(game.judge_limit)
	timer_bar.value = clampf(left / maxf(total, 0.01), 0.0, 1.0) * 100.0 if (active or judging) else 0.0
	timer_label.text = ("%.1f초" % left) if (active or judging) else ""
	var fill := "theirs"
	if my_move:
		fill = "hurry" if left < 5.0 else "mine"
	if fill != _timer_cache:
		_timer_cache = fill
		timer_bar.add_theme_stylebox_override("fill", timer_fill[fill])


func _refresh_lamps(ph: int, me_king: bool) -> void:
	var show_lamps: bool = ph == GambleMatch.Phase.SLAVE_TURN or ph == GambleMatch.Phase.JUDGE or ph == GambleMatch.Phase.REVEALED
	lamp_caption.text = "상대 속임수 가능성" if me_king else "내 시선 때문에 상대에게 켜진 불"
	var slave_seat := int(game.slave)
	for kind in ["peek", "acc"]:
		var state := "off"
		if bool(game.sealed[slave_seat][kind]):
			state = "sealed"
		elif show_lamps and bool(game.lights[kind]):
			state = "on"
		var p: Panel = lamp_panels[kind]
		if state == "on":
			var a := 0.75 + 0.25 * sin(clock * 8.0)
			p.modulate = Color(1, 1, 1, 1).lerp(Color(1.25, 1.2, 1.0, 1), a - 0.5)
		else:
			p.modulate = Color(1, 1, 1, 1)
		if lamp_cache.get(kind, "") == state:
			continue
		lamp_cache[kind] = state
		var need := CheatRules.PEEK_FIX if kind == "peek" else CheatRules.ACC_FIX
		var st: Label = lamp_states[kind]
		if state == "on":
			p.add_theme_stylebox_override("panel", _sb(C_LAMP, 10, Color.WHITE, 2))
			st.text = "켜짐! 시선이 %.1f초 머물렀다" % need
			st.add_theme_color_override("font_color", Color(0.12, 0.08, 0.0))
		elif state == "sealed":
			p.add_theme_stylebox_override("panel", _sb(Color(0.35, 0.08, 0.08, 0.9), 10))
			st.text = "봉인됨 — 이 매치에선 못 씀"
			st.add_theme_color_override("font_color", Color(1.0, 0.7, 0.7))
		else:
			p.add_theme_stylebox_override("panel", _sb(Color(0.15, 0.15, 0.18, 0.9), 10))
			st.text = "꺼짐 (시선이 %.1f초 머물면 켜짐)" % need
			st.add_theme_color_override("font_color", Color(0.75, 0.75, 0.75))
	var acc_txt := ""
	if ph != GambleMatch.Phase.IDLE:
		if me_king:
			var st1 := str(game.acc_state[1])
			acc_txt = "상대 협력자: " + {"none": "없음", "walking": "당신 뒤로 오는 중…", "present": "당신 뒤에 서 있음!", "out": "쫓겨남"}.get(st1, st1)
		else:
			var st0 := str(game.acc_state[0])
			acc_txt = "내 협력자: " + {"none": "없음 (버튼으로 부르기)", "walking": "오는 중…", "present": "상대 뒤에 있음 — 손 1.8초 보기", "out": "쫓겨남"}.get(st0, st0)
	if acc_label.text != acc_txt:
		acc_label.text = acc_txt


## 행동 버튼: 지금 역할 것만 · 못 쓰면 흐리게 + 까닭 · 가능성 불이 켜지면 밝혀내기 버튼이 깜빡
func _refresh_actions(ph: int, me_king: bool) -> void:
	var role := "king" if me_king else "slave"
	var head := "내 행동 — 왕 (방어)" if me_king else "내 행동 — 노예 (공격)"
	if ph == GambleMatch.Phase.IDLE:
		head = "내 행동"
	if action_header.text != head:
		action_header.text = head
		action_header.add_theme_color_override("font_color", C_KING if me_king else C_SLAVE)
	var y := 58.0
	for a in ACTIONS:
		var id := str(a[0])
		var e: Dictionary = action_buttons[id]
		var b: Button = e["button"]
		var visible_now: bool = str(e["role"]) == role and ph != GambleMatch.Phase.IDLE
		b.visible = visible_now
		if not visible_now:
			continue
		b.position = Vector2(8, y)
		y += 54.0
		var rule := _rule_of(id)
		var why := str(game.why_not(0, str(rule[0]), str(rule[1])))
		b.disabled = why != ""
		var sub := _sub_text(id, str(e["desc"])) if why == "" else _short_why(id, why)
		var sl: Label = e["sub"]
		if sl.text != sub:
			sl.text = sub
		if why != "":
			b.modulate = Color(1, 1, 1, 0.5)
		elif _recommended(id):
			var k := 0.5 + 0.5 * sin(clock * 7.0)
			b.modulate = Color(1.0 + 0.35 * k, 1.0 + 0.3 * k, 1.0, 1.0)
		else:
			b.modulate = Color(1, 1, 1, 1)


func _sub_text(id: String, desc: String) -> String:
	match id:
		"lighter", "lighter_plain":
			return "%s · 빈자리 %d" % [desc, CheatRules.OBJECT_SLOTS - int(game.objects[0].size())]
		"accomplice":
			return "%s · %d번 남음" % [desc, int(game.acc_calls_left[0])]
		"attention":
			return "%s · %d번 남음" % [desc, int(game.attention_left[0])]
		"cover":
			return "%s · %d번 남음" % [desc, int(game.cover_left[0])]
		"random":
			return "%s · %d번 남음" % [desc, int(game.random_left[0])]
		"fake":
			return "%s · %d번 남음" % [desc, int(game.fake_left[0])]
		"judge_done":
			return "%s · %.1f초 남음" % [desc, maxf(float(game.judge_left), 0.0)]
	return desc


func _recommended(id: String) -> bool:
	if id == "expose_peek":
		return bool(game.lights["peek"])
	if id == "expose_acc":
		return bool(game.lights["acc"])
	return false


# ───────────────────────── 작은 도우미 ─────────────────────────

func _card_name(card: int) -> String:
	if card < 0:
		return "?"
	return str(RankCards.CARD_NAMES[card])


## 받침 있으면 '을', 없으면 '를'
func _eul(word: String) -> String:
	if word.is_empty():
		return "를"
	var code := word.unicode_at(word.length() - 1)
	if code < 0xAC00 or code > 0xD7A3:
		return "를"
	return "을" if (code - 0xAC00) % 28 != 0 else "를"


func _round_name(idx: int) -> String:
	if idx >= GambleMatch.ROUNDS:
		return "연장 %d판" % (idx - GambleMatch.ROUNDS + 1)
	return "%d/%d판" % [maxi(idx, 0) + 1, GambleMatch.ROUNDS]


func _dots_bb(n: int) -> String:
	return "[color=#ff4d4d]" + "●".repeat(n) + "[/color]" + "○".repeat(maxi(CheatRules.STRIKES_TO_LOSE - n, 0))
