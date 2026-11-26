# VERSION: v0.8.0 — 2026-11-26 — 내가 고를 땐 내 테이블 / 상대가 고를 땐 상대 테이블 · 상대 시선 불빛·게이지·'!' · 협력자 부르기 = 버튼·키 2 누르고 있기 · 밝혀내기 = 물건 클릭(확인)·상대 클릭(몸 수색) · 의심 표시 칸 · 제스처 없앰
# 이전 VERSION: v0.7.0 — 2026-11-26 — 기록 창(채팅식) 없앰 → 가운데 알림·턴 결과 창·테이블 표시 · 점수판·지금 할 일·큰 시간 막대 · 큰 행동 버튼 · 버튼 위에선 시선 유지 · 규칙 창
# 이전 VERSION: v0.6.0 — 2026-11-26 — 기능마다 버튼(노예 열·왕 열, 못 쓰면 흐리게·남은 횟수·단축키) · 판단 시간 안내·타이머·'판단 끝·공개'
# 이전 VERSION: v0.5.0 — 2026-11-26 — 사전 설정(책상 위 물건 3자리) · 왕 턴/노예 턴 · 진영별 키 · 가능성 불 두 개 · 새 이벤트 기록
# 이전 VERSION: v0.4.0 — 2026-11-26 — 키 행동: 라이터 놓기 · 협력자 부르기 · 카드 덮개 · 블러핑 · 안내·기록
#
# 화면 구성 (1280×800):
#   왼쪽 위 점수판 · 가운데 위 '지금 할 일' + 시간 막대 · 오른쪽 위 설정 · 오른쪽 '의심 표시'(내가 왕: 상대 '!'·협력자 가능성 / 내가 노예: 내 상태)
#   왼쪽 큰 행동 버튼 (지금 역할 것만) · 왼쪽 아래 알림 · 공개되면 턴 결과 창
#   테이블: 내가 고르는 중 = 내 테이블(mine), 그 밖 = 상대 테이블(theirs) — scenes/table_view.gd
# 조작: 마우스 = 내 시선 · 카드 클릭 = 내기 · 상대 테이블에서 (내가 낸 뒤) 물건 클릭 = 물건 확인, 상대 클릭 = 몸 수색
#   협력자 부르기 = 버튼이나 키 2 를 2.5초 누르고 있기 (떼면 실패) · 버튼·설정 위에선 시선이 마지막 자리 그대로
# 버튼을 쓸 수 있는지는 core/match.gd why_not() 하나로 판정. 연구·교육용 데모 — 실제 돈과 관계없음.
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
	["lighter_plain", "slave", "빈 라이터 놓기", "3", "미끼 — '!' 만 뜸"],
	["call", "slave", "협력자 부르기 (누르고 있기)", "2", "2.5초 귀 만지기 → 이어폰 연결"],
	["attention", "slave", "시선 끌기", "F", "3초간 상대가 내 시선·행동을 못 봄"],
	["cover", "king", "가리기", "C", "낸 카드 위 칩 — 반사경 막기"],
	["random", "king", "섞기", "R", "낸 카드를 안 보고 섞음 — 둘 다 막기"],
	["fake", "king", "바꿔치기", "X", "엿보면 가짜가 보임"],
	["inspect", "king", "물건 확인", "Q", "물건을 클릭 — 반사경이면 적중"],
	["search", "king", "몸 수색", "W", "이어폰이 있으면 적중"],
	["judge_done", "king", "판단 끝 · 공개", "Enter", "바로 카드 공개"],
]
const RULES_BB := "[font_size=20][b]한 턴의 흐름[/b][/font_size]\n" \
	+ "[color=#8cc8ff]왕[/color]이 카드를 고름 (내 테이블)  →  [color=#ffb35a]노예[/color]가 엿보고 고름  →  왕이 판단  →  공개   · 차례마다 30초\n" \
	+ "내가 고를 땐 [b]내 테이블[/b], 상대가 고를 땐 [b]상대 테이블[/b]과 상대 시선([color=#ffdc73]불빛[/color])이 보여요.\n\n" \
	+ "[color=#ffb35a][b]노예 (공격)[/b][/color]  반사경 물건을 [b]1.5초[/b] 계속 보면 상대 카드 — 그 물건에 게이지가 차고, 다 차면 상대에게 [color=#ffc81f][b]'!'[/b][/color]\n" \
	+ "   협력자: [b]'협력자 부르기'를 2.5초 누르고 있기[/b](귀 만지기) → 이어폰으로 카드를 알려 줌. 상대가 보고 있으면 협력자 가능성 ↑\n" \
	+ "[color=#8cc8ff][b]왕 (방어)[/b][/color]  카드를 [u]낸 뒤에만[/u] 방어: 가리기·섞기·바꿔치기 · [b]물건 클릭 = 물건 확인[/b] · [b]상대 클릭 = 몸 수색[/b]\n" \
	+ "밝혀내기 성공: 상대 [color=#ff5a5a]경고[/color] +1 · 그 속임수 봉인 · [b]그 턴 무효 → 다시 고름[/b] / 실패: 내 다음 차례 −10초\n\n" \
	+ "[color=#ff5a5a][b]경고 2개 = 즉시 패배[/b][/color] · 카드: 왕 > 시민 > 암살자 > 왕 · 점수: 왕 측 승 +1, 노예 측 승 +4 · 6판\n" \
	+ "[color=#aaaaaa]마우스 = 내 시선 · 버튼 위에선 시선이 그대로 · 연구·교육용 데모, 실제 돈과 무관[/color]"
const TOAST_SECONDS := 2.8
const TOAST_MAX := 3
const TOAST_COLORS := {"good": Color(0.08, 0.42, 0.2, 0.93), "bad": Color(0.58, 0.08, 0.08, 0.93),
	"warn": Color(0.6, 0.4, 0.04, 0.93), "info": Color(0.1, 0.2, 0.4, 0.93)}
const C_KING := Color(0.55, 0.8, 1.0)
const C_SLAVE := Color(1.0, 0.7, 0.35)
const ACTION_PANEL := Rect2(8, 140, 304, 384)
const SETTINGS_RECT := Rect2(970, 6, 304, 116)
const SUSPECT_RECT := Rect2(970, 130, 304, 200)
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
var pick_mode := false        # '물건 확인' 버튼을 눌러 물건 고르는 중

var spot: ColorRect
var spot_mat: ShaderMaterial
var score_text: RichTextLabel
var title_label: Label
var sub_label: Label
var timer_bar: ProgressBar
var timer_label: Label
var timer_fill: Dictionary = {}
var sus_title: Label
var sus_lines: Label
var sus_bar: ProgressBar
var sus_bar_label: Label
var call_bar: ProgressBar
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
	_build_suspect(ui)
	_build_actions(ui)
	toast_box = Control.new()
	toast_box.mouse_filter = Control.MOUSE_FILTER_IGNORE
	toast_box.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	ui.add_child(toast_box)
	_build_result(ui)
	_build_setup(ui)
	_build_help(ui)


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
	p.add_child(_small_button("새 매치", Vector2(196, 6), Vector2(100, 32), _on_new_match))
	p.add_child(_small_button("규칙 (H)", Vector2(196, 44), Vector2(100, 32), _toggle_help))
	spot_check = CheckBox.new()
	spot_check.text = "시야 제한"
	spot_check.button_pressed = false
	spot_check.position = Vector2(8, 44)
	spot_check.focus_mode = Control.FOCUS_NONE
	p.add_child(spot_check)


## 오른쪽 '의심 표시' — 내가 왕: 상대의 '!' 수·협력자 가능성 / 내가 노예: 상대가 본 것·이어폰 상태
func _build_suspect(ui: Control) -> void:
	var p := _panel(SUSPECT_RECT, Color(0, 0, 0, 0.6))
	ui.add_child(p)
	sus_title = _label(Vector2(12, 6), Vector2(282, 26), 18, Color.WHITE)
	p.add_child(sus_title)
	sus_bar_label = _label(Vector2(12, 36), Vector2(282, 22), 15, Color(0.9, 0.9, 0.9))
	p.add_child(sus_bar_label)
	sus_bar = ProgressBar.new()
	sus_bar.position = Vector2(12, 60)
	sus_bar.size = Vector2(280, 18)
	sus_bar.show_percentage = false
	sus_bar.mouse_filter = Control.MOUSE_FILTER_IGNORE
	sus_bar.add_theme_stylebox_override("background", _sb(Color(0.15, 0.15, 0.18), 5))
	sus_bar.add_theme_stylebox_override("fill", _sb(Color(1.0, 0.45, 0.3), 5))
	p.add_child(sus_bar)
	sus_lines = _label(Vector2(12, 84), Vector2(282, 84), 15, Color(0.9, 0.9, 0.9))
	sus_lines.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	p.add_child(sus_lines)
	call_bar = ProgressBar.new()
	call_bar.position = Vector2(12, 172)
	call_bar.size = Vector2(280, 16)
	call_bar.show_percentage = false
	call_bar.mouse_filter = Control.MOUSE_FILTER_IGNORE
	call_bar.add_theme_stylebox_override("background", _sb(Color(0.15, 0.15, 0.18), 5))
	call_bar.add_theme_stylebox_override("fill", _sb(Color(0.4, 0.85, 1.0), 5))
	p.add_child(call_bar)


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
		if id == "call":
			b.button_down.connect(_call_down)
			b.button_up.connect(_call_up)
		else:
			b.pressed.connect(_act.bind(id))
		var tl := _label(Vector2(12, 2), Vector2(214, 26), 17, Color.WHITE)
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


func _build_setup(ui: Control) -> void:
	setup_panel = _panel(Rect2(200, 120, 880, 560), Color(0.04, 0.04, 0.07, 0.97), Color(1, 1, 1, 0.25), 2)
	setup_panel.mouse_filter = Control.MOUSE_FILTER_STOP
	ui.add_child(setup_panel)
	var title := _label(Vector2(24, 12), Vector2(832, 40), 28, Color.WHITE)
	title.text = "게임 준비"
	setup_panel.add_child(title)
	var rules := _rich(Vector2(24, 56), Vector2(832, 300), 16)
	rules.text = RULES_BB
	setup_panel.add_child(rules)
	var ot := _label(Vector2(24, 362), Vector2(832, 28), 18, Color(1.0, 0.9, 0.5))
	ot.text = "책상 위에 둘 물건 (반사경이 든 것과 빈 것은 상대 눈엔 똑같아 보여요 · 확인당하면 반사경은 들킴)"
	setup_panel.add_child(ot)
	setup_options.clear()
	for i in CheatRules.OBJECT_SLOTS:
		var lab := _label(Vector2(24 + i * 280, 396), Vector2(260, 22), 14, Color(0.8, 0.8, 0.8))
		lab.text = "자리 %d" % (i + 1)
		setup_panel.add_child(lab)
		var ob := OptionButton.new()
		for n in SETUP_NAMES:
			ob.add_item(n)
		ob.selected = int(SETUP_DEFAULT[i])
		ob.position = Vector2(24 + i * 280, 420)
		ob.size = Vector2(260, 40)
		ob.focus_mode = Control.FOCUS_NONE
		ob.add_theme_font_size_override("font_size", 17)
		setup_panel.add_child(ob)
		setup_options.append(ob)
	var note := _label(Vector2(24, 466), Vector2(832, 22), 13, Color(0.7, 0.7, 0.7))
	note.text = "게임 중에도 왼쪽 버튼으로 라이터를 %d번 더 놓을 수 있어요" % CheatRules.PLACES_PER_MATCH
	setup_panel.add_child(note)
	setup_panel.add_child(_big_button("시작 ▶", Vector2(330, 494), Vector2(220, 54), _on_setup_start))


func _build_help(ui: Control) -> void:
	help_panel = _panel(Rect2(200, 120, 880, 430), Color(0.04, 0.04, 0.07, 0.97), Color(1, 1, 1, 0.25), 2)
	help_panel.mouse_filter = Control.MOUSE_FILTER_STOP
	ui.add_child(help_panel)
	var title := _label(Vector2(24, 12), Vector2(600, 40), 26, Color.WHITE)
	title.text = "규칙 한눈에 (보는 동안 시간 멈춤)"
	help_panel.add_child(title)
	var rules := _rich(Vector2(24, 56), Vector2(832, 300), 16)
	rules.text = RULES_BB
	help_panel.add_child(rules)
	help_panel.add_child(_big_button("닫기", Vector2(350, 364), Vector2(180, 50), _toggle_help))
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
	table.hide_my_card = false
	turn_notes.clear()
	last_reveal = {}
	last_round_end = {}
	last_match_end = {}
	result_mode = ""
	pick_mode = false
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


## 지금 보여 줄 테이블: 내가 고르는 중(내 왕 턴·내 노예 턴)이면 내 테이블, 그 밖은 상대 테이블
func _view() -> String:
	var ph := int(game.phase)
	if ph == GambleMatch.Phase.KING_TURN and int(game.king) == 0:
		return "mine"
	if (ph == GambleMatch.Phase.SLAVE_TURN or ph == GambleMatch.Phase.JUDGE) and int(game.slave) == 0:
		return "mine"
	return "theirs"


func _process(delta: float) -> void:
	if game == null:
		return
	clock += delta
	table.clock = clock
	_update_toasts(delta)
	table.view = _view()
	var mp: Vector2 = get_local_mouse_position()
	var over_ui := _over_ui(mp)
	if not over_ui:
		last_game_mouse = mp
		current_gaze = table.gaze_target(mp)
	table.my_gaze = current_gaze
	table.hover_index = table.card_at(mp) if _my_card_turn() and not over_ui else -1
	table.hover_pick = _pick_at(mp) if not over_ui else ""
	if not help_panel.visible:
		game.tick(minf(delta, MAX_DT), current_gaze)
	_drain()
	spot.visible = spot_check.button_pressed and not setup_panel.visible
	spot_mat.set_shader_parameter("center_px", last_game_mouse)
	spot_mat.set_shader_parameter("rect_size", size)
	_refresh()
	table.queue_redraw()


func _over_ui(mp: Vector2) -> bool:
	if setup_panel.visible or help_panel.visible or result_panel.visible:
		return true
	return ACTION_PANEL.has_point(mp) or SETTINGS_RECT.has_point(mp) or SUSPECT_RECT.has_point(mp)


func _my_card_turn() -> bool:
	var ph := int(game.phase)
	return (ph == GambleMatch.Phase.KING_TURN or ph == GambleMatch.Phase.SLAVE_TURN) and game.actor() == 0 and int(game.committed[0]) == -1


## 상대 테이블에서 지금 클릭하면 되는 대상 (물건 확인·몸 수색이 가능할 때만)
func _pick_at(mp: Vector2) -> String:
	if table.view != "theirs":
		return ""
	var tgt: String = table.pick_target(mp)
	if tgt.begins_with("obj"):
		return tgt if str(game.why_not(0, "inspect", tgt.substr(3))) == "" else ""
	if tgt == "body" and not pick_mode:
		return tgt if str(game.why_not(0, "search")) == "" else ""
	return ""


func _gui_input(event: InputEvent) -> void:
	var mb := event as InputEventMouseButton
	if mb == null or not mb.pressed or mb.button_index != MOUSE_BUTTON_LEFT or game == null:
		return
	if _over_ui(mb.position):
		return
	if _my_card_turn() and table.view == "mine":
		var idx: int = table.card_at(mb.position)
		if idx >= 0:
			game.commit(int(game.hands[0][idx]))
			_drain()
		return
	var tgt := _pick_at(mb.position)
	if tgt.begins_with("obj"):
		pick_mode = false
		game.inspect(int(tgt.substr(3)))
		_drain()
	elif tgt == "body":
		game.search()
		_drain()
	elif pick_mode:
		pick_mode = false
		_toast("물건 확인 취소", "info")


func _unhandled_input(event: InputEvent) -> void:
	var k := event as InputEventKey
	if k == null or k.echo or game == null:
		return
	if k.keycode == KEY_2:
		if k.pressed:
			_call_down()
		else:
			_call_up()
		return
	if not k.pressed:
		return
	if k.keycode == KEY_H or (k.keycode == KEY_ESCAPE and help_panel.visible):
		_toggle_help()
		return
	if k.keycode == KEY_ESCAPE and pick_mode:
		pick_mode = false
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
		KEY_F:
			id = "attention"
		KEY_C:
			id = "cover"
		KEY_R:
			id = "random"
		KEY_X:
			id = "fake"
		KEY_Q:
			id = "inspect"
		KEY_W:
			id = "search"
		_:
			return
	_act(id)


## 협력자 부르기 — 누르는 동안 수상한 행동, 2.5초 채우면 연결 (먼저 떼면 실패)
func _call_down() -> void:
	if game == null or help_panel.visible:
		return
	var r: Dictionary = game.start_call()
	if not bool(r.get("ok", false)):
		_toast("지금은 못 해요 — " + _short_why("call", str(r.get("why", ""))), "info")
	_drain()


func _call_up() -> void:
	if game == null:
		return
	game.stop_call()
	_drain()


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
		"attention":
			r = game.attention()
		"cover":
			r = game.cover()
		"random":
			r = game.play_random()
		"fake":
			r = game.fake()
		"inspect":
			var why := str(game.why_not(0, "inspect"))
			if why != "":
				r = {"ok": false, "why": why}
			elif table.hover_pick.begins_with("obj"):
				r = game.inspect(int(table.hover_pick.substr(3)))
			else:
				pick_mode = true
				_toast("확인할 물건을 클릭하세요 (Esc 취소)", "info")
				return
		"search":
			r = game.search()
		"judge_done":
			r = game.judge_done()
		_:
			return
	if r.has("ok") and not bool(r["ok"]):
		_toast("지금은 못 해요 — " + _short_why(id, str(r.get("why", ""))), "info")
	_drain()


func _rule_of(id: String) -> Array:
	match id:
		"lighter", "lighter_plain":
			return ["object", id]
	return [id, ""]


func _short_why(id: String, code: String) -> String:
	match code:
		"not_active":
			return "턴 진행 중에만"
		"full":
			return "물건 자리가 꽉 참"
		"no_uses":
			return "남은 횟수 없음"
		"not_slave":
			return "노예일 때만"
		"not_king":
			return "왕일 때만"
		"after_commit":
			return "카드를 낸 뒤에만"
		"done":
			return "이번 턴에 이미 함"
		"already_seen":
			return "상대가 이미 봄"
		"already_this_turn":
			return "이번 턴에 이미 함"
		"no_target":
			return "확인할 물건이 없음"
		"checked":
			return "이미 확인한 물건"
		"sealed":
			return "봉인됨" if id != "search" else "이미 이어폰을 압수함"
		"calling":
			return "부르는 중"
		"connected":
			return "이미 연결됨 (이번 판)"
		"not_judge":
			return "판단 시간에만"
		"not_calling":
			return "부르는 중이 아님"
	return code


# ───────────────────────── 알림 ─────────────────────────

func _toast(text: String, kind: String = "info") -> void:
	var col: Color = TOAST_COLORS.get(kind, TOAST_COLORS["info"])
	var p := _panel(Rect2(0, 0, 304, 54), col)
	var l := _label(Vector2(8, 0), Vector2(288, 54), 16, Color.WHITE)
	l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	l.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
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


## 왼쪽 아래, 최근 것이 맨 위
func _layout_toasts() -> void:
	var n := toasts.size()
	for i in n:
		var node: Control = toasts[i]["node"]
		node.position = Vector2(8, 532 + (n - 1 - i) * 60)


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


## 이벤트마다 짧은 알림 — 상대가 숨긴 것(바꿔치기·얻은 정보·이어폰 연결)은 공개 전엔 안 보여 줌
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
			pick_mode = false
			table.seen_card = -1
			table.seen_source = ""
			table.hide_my_card = false
			if bool(ev.get("replay", false)):
				_toast("이번 턴 무효 — 둘 다 다시 고르세요", "warn")
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
		"call_start":
			if int(ev["seat"]) == 0:
				_toast("귀를 만지며 신호 중… (2.5초 누르고 있기)", "info")
		"call_cancel":
			if int(ev["seat"]) == 0:
				_toast("신호를 멈췄다 — 연결 안 됨", "warn")
		"call_seen":
			if int(ev["seat"]) == 0:
				_toast("상대가 수상한 손짓을 봤다 — 협력자 가능성 ↑", "bad")
			else:
				_toast("상대가 귀를 만지작거린다 — 협력자 가능성 ↑", "warn")
		"acc_connected":
			if int(ev["seat"]) == 0:
				_toast("이어폰 연결! 이번 판 동안 내 차례마다 카드를 알려 줌", "good")
		"attention":
			if int(ev["seat"]) == 0:
				_toast("시선 끌기 — 3초 동안 상대가 못 봄", "good")
			else:
				_toast("상대가 술잔을 쏟았다 — 3초간 상대 시선이 안 보임", "warn")
		"cover":
			if int(ev["seat"]) == 0:
				_toast("칩으로 가렸다 — 반사경 차단", "good")
			else:
				_toast("상대가 칩으로 가렸다 — 반사경 안 통함", "warn")
		"random":
			if int(ev["seat"]) == 0:
				table.hide_my_card = true
				_toast("카드를 섞었다 — 나도 모름, 엿보기·이어폰 차단", "good")
			else:
				_toast("상대가 카드를 섞었다 — 엿볼 수 없음", "warn")
		"fake":
			if int(ev["seat"]) == 0:
				_toast("바꿔치기 준비 — 엿보면 가짜가 보임", "good")
		"info":
			if int(ev["seat"]) == 0:
				var c := str(RankCards.CARD_NAMES[int(ev["card"])])
				table.seen_card = int(ev["card"])
				table.seen_source = str(ev["source"])
				var how := "반사경" if str(ev["source"]) == "peek" else "이어폰"
				_toast("%s: 상대 카드 = %s" % [how, c], "good")
				turn_notes.append("%s로 본 카드: %s" % [how, c])
		"info_blocked":
			if int(ev["seat"]) == 0:
				var msg := "칩에 가려 안 보인다" if str(ev["why"]) == "cover" else "상대가 섞어서 알 수 없다"
				_toast(msg, "warn")
				turn_notes.append(msg)
		"mark":
			if int(ev["seat"]) == 1:
				_toast("상대 시선이 물건에 머물렀다 — '!'", "warn")
			else:
				_toast("상대가 내 시선을 봤다 — 그 물건에 '!'", "warn")
		"judge_start":
			if int(ev["king"]) == 0:
				_toast("상대가 냈다 — %.0f초 안에 판단 (물건·상대 클릭)" % float(ev["limit"]), "info")
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
	var search: bool = str(ev["kind"]) == "search"
	var what := "몸 수색" if search else "물건 확인"
	var msg := ""
	var tone := "info"
	if by == 0 and hit:
		msg = "%s 적중! %s — 상대 경고 %d/%d" % [what, "이어폰 발견" if search else "반사경 발견", int(ev["strikes"][1]), CheatRules.STRIKES_TO_LOSE]
		tone = "good"
	elif by == 0:
		msg = "%s 헛짚음 — 내 다음 차례 −%.0f초" % [what, CheatRules.EXPOSE_FAIL_CUT]
		tone = "bad"
	elif hit:
		msg = "들켰다! 상대가 %s — %s 압수 · 내 경고 %d/%d" % [what, "이어폰" if search else "반사경", int(ev["strikes"][0]), CheatRules.STRIKES_TO_LOSE]
		tone = "bad"
	else:
		msg = "상대 %s 헛짚음 — 상대 다음 차례 −%.0f초" % [what, CheatRules.EXPOSE_FAIL_CUT]
		tone = "good"
	_toast(msg, tone)
	turn_notes.append(msg)


func _note_summary(ev: Dictionary) -> void:
	if int(ev["slave"]) == 0:
		return
	var marks: Array = ev["marks"]
	var n_marks := 0
	for m in marks:
		if bool(m):
			n_marks += 1
	var parts := PackedStringArray()
	if bool(ev["peeked"]):
		parts.append("상대는 반사경으로 진짜 엿봤다")
	elif n_marks > 0:
		parts.append("'!' 는 미끼였다")
	if str(ev["info"]) == "acc":
		parts.append("상대는 이어폰으로 들었다")
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
	_refresh_suspect(ph, me_king)
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
				sub = "고르는 중엔 방어를 못 해요 · 위쪽을 보면 상대를 지켜봄"
				my_move = true
			else:
				title = "상대(왕)가 고르는 중 — 상대 시선을 보세요"
				sub = "상대가 안 볼 때 '협력자 부르기'를 2.5초 누르고 있기"
		GambleMatch.Phase.SLAVE_TURN:
			if me_king:
				title = "상대가 엿보는 중 — 불빛과 '!' 를 보세요"
				sub = "물건 클릭 = 물건 확인 · 상대 클릭 = 몸 수색 · 가리기·섞기·바꿔치기"
			else:
				title = "내 차례 — 엿보고 카드를 내세요"
				sub = "반사경 물건 %.1f초 계속 보기 (상대에게 '!') · 이어폰이 있으면 %.0f초 뒤 알려 줌" % [CheatRules.PEEK_FIX, CheatRules.ACC_INFO_DELAY]
				my_move = true
		GambleMatch.Phase.JUDGE:
			if me_king:
				title = "판단하세요 — 상대가 속임수를 썼을까?"
				sub = "'!' 물건을 클릭해 확인하거나 상대를 클릭해 몸 수색 · 아니면 '판단 끝'"
				my_move = true
			else:
				title = "상대가 판단 중…"
		GambleMatch.Phase.REVEALED:
			title = "공개!"
		GambleMatch.Phase.MATCH_OVER:
			title = "매치 끝"
	if pick_mode:
		title = "확인할 물건을 클릭하세요"
		sub = "Esc 취소"
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


## 의심 표시 — 내가 왕: 상대의 '!' 수 · 협력자 가능성 / 내가 노예: 상대에게 보인 것 · 이어폰 상태
func _refresh_suspect(ph: int, me_king: bool) -> void:
	if ph == GambleMatch.Phase.IDLE:
		sus_title.text = "의심 표시"
		sus_bar_label.text = ""
		sus_bar.value = 0.0
		sus_lines.text = ""
		call_bar.visible = false
		return
	var marks_n := 0
	for m in game.marks:
		if bool(m):
			marks_n += 1
	var slave_seat := int(game.slave)
	var sus := float(game.acc_suspect[slave_seat]) * 100.0
	sus_bar.value = sus
	if me_king:
		sus_title.text = "상대 의심 표시"
		sus_title.add_theme_color_override("font_color", C_KING)
		sus_bar_label.text = "협력자 가능성 %.0f%%  (상대 부르는 걸 봤을 때 ↑)" % sus
		var lines := "엿보기 '!' : 물건 %d개\n남은 횟수 — 물건 확인 %d · 몸 수색 %d" % [marks_n, int(game.inspect_left[0]), int(game.search_left[0])]
		if bool(game.sealed[1]["peek"]):
			lines += "\n반사경 압수함 (봉인)"
		if bool(game.sealed[1]["acc"]):
			lines += "\n이어폰 압수함 (봉인)"
		sus_lines.text = lines
		call_bar.visible = false
	else:
		sus_title.text = "내 속임수 상태"
		sus_title.add_theme_color_override("font_color", C_SLAVE)
		sus_bar_label.text = "상대가 느낀 협력자 가능성 %.0f%%" % sus
		var ear := "이어폰: 연결 안 됨 (부르기 %d번 남음)" % int(game.acc_calls_left[0])
		if bool(game.sealed[0]["acc"]):
			ear = "이어폰: 압수됨"
		elif bool(game.calling[0]):
			ear = "이어폰: 부르는 중… 손 떼지 마세요"
		elif bool(game.acc_connected[0]):
			ear = "이어폰: 연결됨 (이번 판)"
		sus_lines.text = "상대에게 보인 '!' : 물건 %d개\n%s" % [marks_n, ear]
		call_bar.visible = bool(game.calling[0])
		call_bar.value = clampf(float(game.call_progress[0]) / CheatRules.ACC_CALL_SECONDS, 0.0, 1.0) * 100.0


## 행동 버튼: 지금 역할 것만 · 못 쓰면 흐리게 + 까닭 · '!'·협력자 가능성이 있으면 밝혀내기 버튼이 깜빡
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
		if id == "call" and bool(game.calling[0]):
			why = ""   # 누르고 있는 중엔 켜 둠
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
			return "%s · %d번 남음" % [desc, int(game.place_left[0])]
		"call":
			if bool(game.calling[0]):
				return "신호 중 %.0f%% — 손 떼지 마세요" % (clampf(float(game.call_progress[0]) / CheatRules.ACC_CALL_SECONDS, 0.0, 1.0) * 100.0)
			return "%s · %d번 남음" % [desc, int(game.acc_calls_left[0])]
		"attention":
			return "%s · %d번" % [desc, int(game.attention_left[0])]
		"cover":
			return "%s · %d번 남음" % [desc, int(game.cover_left[0])]
		"random":
			return "%s · %d번 남음" % [desc, int(game.random_left[0])]
		"fake":
			return "%s · %d번 남음" % [desc, int(game.fake_left[0])]
		"inspect":
			return "%s · %d번 남음" % [desc, int(game.inspect_left[0])]
		"search":
			return "%s · %d번 남음" % [desc, int(game.search_left[0])]
		"judge_done":
			return "%s · %.1f초 남음" % [desc, maxf(float(game.judge_left), 0.0)]
	return desc


func _recommended(id: String) -> bool:
	if id == "inspect":
		for m in game.marks:
			if bool(m):
				return true
		return false
	if id == "search":
		return float(game.acc_suspect[int(game.slave)]) >= 0.3
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
