# VERSION: v0.4.0 — 2026-11-26 — 라이터(뚜껑 안 반사경) · 상대 뒤 협력자(손 신호) · 카드 덮개 칩 · 뒤돌아보는 상대
# 이전 VERSION: v0.2.0 — 2026-11-26 — 테이블 장면 그리기 (상대 인물·눈동자·잔·술병·카드) + 시선 판정 영역
#
# 화면 1280×800 기준 좌표. 규칙은 없고 game(core/match.gd) 상태를 그리기만 함.
# 시선 영역: 상대 얼굴 = "face" · 내 라이터(놓았을 때) = "shiner" · 상대 뒤 협력자(서 있을 때) = "accomplice"
#            · 아래 내 패 = "own_card" · 나머지 = "table"
extends Control

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const GambleMatch = preload("res://core/match.gd")

const HEAD := Vector2(640, 196)
const HEAD_R := 62.0
const EYE_L := Vector2(615, 190)
const EYE_R := Vector2(665, 190)
const FACE_ZONE_R := 92.0
const MY_LIGHTER := Vector2(330, 575)        # 내 라이터 (왼쪽, 상대 카드 쪽으로 기울여 놓음)
const MY_LIGHTER_ZONE := Rect2(270, 505, 120, 130)
const AI_LIGHTER := Vector2(950, 575)        # 상대 라이터 (오른쪽, 내 카드 쪽)
const ACC_POS := Vector2(880, 250)           # 협력자가 서는 자리 (상대 오른쪽 뒤)
const ACC_ZONE_R := 80.0
const ACC_START := Vector2(1340, 250)        # 걸어 들어오기 시작하는 곳 (화면 밖 오른쪽)
const AI_SLOT := Vector2(640, 500)
const AI_SLOT_SIZE := Vector2(64, 92)
const MY_SLOT := Vector2(640, 602)
const MY_SLOT_SIZE := Vector2(74, 104)
const HAND_Y := 728.0
const HAND_CARD := Vector2(92, 128)
const HAND_GAP := 106.0
const HAND_ZONE_Y := 655.0
## AI 눈이 향하는 화면 위치 ("face" = 화면 밖의 사람 = 정면)
const LOOK_AT := {"hands": Vector2(640, 760), "own_card": Vector2(640, 505), "away": Vector2(1150, 320),
	"shiner": Vector2(950, 575), "behind": Vector2(1200, 120)}

const C_SKIN := Color(0.86, 0.72, 0.60)
const C_HAIR := Color(0.16, 0.12, 0.10)
const C_SUIT := Color(0.13, 0.14, 0.20)
const C_SHIRT := Color(0.85, 0.84, 0.80)
const C_FELT := Color(0.11, 0.33, 0.22)
const C_WOOD := Color(0.36, 0.22, 0.12)
const C_COAT := Color(0.22, 0.20, 0.18)

var game = null
var hover_index := -1
var my_gaze := "table"
var show_helper := false


func gaze_target(p: Vector2) -> String:
	if p.distance_to(HEAD) <= FACE_ZONE_R:
		return "face"
	if game != null:
		if bool(game.lighter[0]) and MY_LIGHTER_ZONE.has_point(p):
			return "shiner"
		if str(game.acc_state) == "present" and p.distance_to(ACC_POS) <= ACC_ZONE_R:
			return "accomplice"
	if p.y >= HAND_ZONE_Y:
		return "own_card"
	return "table"


func hand_rect(i: int, n: int) -> Rect2:
	var cx := 640.0 + (float(i) - float(n - 1) / 2.0) * HAND_GAP
	var lift := 16.0 if i == hover_index else 0.0
	return Rect2(Vector2(cx - HAND_CARD.x / 2.0, HAND_Y - HAND_CARD.y / 2.0 - lift), HAND_CARD)


func card_at(p: Vector2) -> int:
	if game == null:
		return -1
	var n: int = game.hands[0].size()
	for i in n:
		if hand_rect(i, n).has_point(p):
			return i
	return -1


# ───────────────────────── 그리기 ─────────────────────────

func _draw() -> void:
	draw_rect(Rect2(0, 0, 1280, 800), Color(0.06, 0.05, 0.07))
	draw_circle(Vector2(640, 40), 300.0, Color(0.15, 0.11, 0.09, 0.55))
	draw_circle(Vector2(640, 40), 160.0, Color(0.24, 0.18, 0.13, 0.45))
	if game != null:
		_draw_accomplice()
	_draw_opponent_body()
	_draw_table()
	if game == null:
		return
	_draw_opponent_hands()
	if bool(game.lighter[0]):
		_draw_lighter(MY_LIGHTER, true)
	if bool(game.lighter[1]):
		_draw_lighter(AI_LIGHTER, false)
	_draw_slots()
	_draw_hand()
	if show_helper:
		_draw_helper()


func _draw_opponent_body() -> void:
	var shift := _head_shift()
	draw_colored_polygon(PackedVector2Array([Vector2(470, 300), Vector2(810, 300), Vector2(870, 470), Vector2(410, 470)]), C_SUIT)
	draw_colored_polygon(PackedVector2Array([Vector2(605, 300), Vector2(675, 300), Vector2(640, 368)]), C_SHIRT)
	draw_rect(Rect2(618, 240, 44, 66), C_SKIN.darkened(0.12))
	var h := HEAD + shift
	draw_circle(h, HEAD_R, C_SKIN)
	_cap(h, HEAD_R + 4.0, PI * 1.12, PI * 1.88, C_HAIR)
	var off := _pupil_offset()
	for e in [EYE_L, EYE_R]:
		var ec: Vector2 = e + shift
		_ellipse(ec, 13.0, 9.0, Color(0.97, 0.97, 0.95))
		draw_circle(ec + off, 5.5, Color(0.12, 0.09, 0.07))
		draw_circle(ec + off + Vector2(-1.5, -1.5), 1.6, Color(1, 1, 1, 0.8))
	var furrow := 0.0
	if game != null:
		furrow = clampf((float(game.brains[1].suspicion) + 1.7) / 4.0, 0.0, 1.0) * 6.0
	draw_line(EYE_L + shift + Vector2(-14, -17), EYE_L + shift + Vector2(12, -17 + furrow), C_HAIR, 4.0)
	draw_line(EYE_R + shift + Vector2(-12, -17 + furrow), EYE_R + shift + Vector2(14, -17), C_HAIR, 4.0)
	draw_line(h + Vector2(0, 2), h + Vector2(-5, 20), C_SKIN.darkened(0.3), 2.0)
	draw_line(h + Vector2(-16, 36), h + Vector2(16, 36), Color(0.45, 0.20, 0.20), 3.0)
	if my_gaze == "face":
		draw_arc(HEAD, FACE_ZONE_R, 0.0, TAU, 48, Color(1, 1, 1, 0.12), 2.0)


func _draw_table() -> void:
	draw_colored_polygon(PackedVector2Array([Vector2(190, 440), Vector2(1090, 440), Vector2(1280, 800), Vector2(0, 800)]), C_FELT)
	draw_line(Vector2(190, 440), Vector2(1090, 440), C_WOOD, 10.0)


func _draw_opponent_hands() -> void:
	for hc in [Vector2(505, 462), Vector2(775, 462)]:
		draw_rect(Rect2(hc.x - 26, hc.y - 34, 52, 18), C_SUIT)
		draw_circle(hc, 22.0, C_SKIN)
	var n: int = game.hands[1].size()
	if int(game.committed[1]) != -1 and not bool(game.revealed):
		n -= 1
	for i in n:
		var r := Rect2(Vector2(452 + i * 14, 400 - i * 2), Vector2(34, 50))
		_draw_card(r, -1, false, false)


## 협력자: 상대 오른쪽 뒤에 서서 가슴 앞 손으로 신호 (걸어오는 중엔 오른쪽에서 들어옴)
func _draw_accomplice() -> void:
	var state := str(game.acc_state)
	if state != "walking" and state != "present":
		return
	var pos := ACC_POS
	if state == "walking":
		var k := clampf(1.0 - float(game.acc_walk_left) / CheatRules.ACC_WALK_SECONDS, 0.0, 1.0)
		pos = ACC_START.lerp(ACC_POS, k)
	draw_colored_polygon(PackedVector2Array([pos + Vector2(-60, -60), pos + Vector2(60, -60), pos + Vector2(75, 190), pos + Vector2(-75, 190)]), C_COAT)
	draw_circle(pos + Vector2(0, -95), 34.0, C_SKIN.darkened(0.25))
	_cap(pos + Vector2(0, -95), 37.0, PI * 1.05, PI * 1.95, C_HAIR)   # 모자
	var hand := pos + Vector2(25, 15)
	draw_circle(hand, 13.0, C_SKIN.darkened(0.15))
	if state == "present":
		var reading: bool = my_gaze == "accomplice" and int(game.turn_type) == GambleMatch.TurnType.CHEAT
		if reading:
			for i in 3:
				draw_line(hand + Vector2(-8 + i * 8, -6), hand + Vector2(-10 + i * 10, -24), C_SKIN.darkened(0.15), 4.0)
		var p := float(game.signal_progress)
		if p > 0.0 and not bool(game.peek_done[0]):
			draw_arc(pos, ACC_ZONE_R - 6.0, -PI / 2.0, -PI / 2.0 + TAU * p, 48, Color(0.5, 0.9, 1.0, 0.9), 5.0)
		if bool(game.peek_done[0]) and str(game.peek_source) == "accomplice":
			_text(hand + Vector2(0, -40), str(RankCards.CARD_NAMES[int(game.committed[1])]), 18, Color(0.6, 1.0, 1.0))
		if my_gaze == "accomplice":
			draw_arc(pos, ACC_ZONE_R, 0.0, TAU, 48, Color(1, 1, 1, 0.12), 2.0)


## 라이터 — 뚜껑 안쪽에 작은 반사경. 내 것이면 읽기 진행도·비친 카드
func _draw_lighter(c: Vector2, mine: bool) -> void:
	draw_rect(Rect2(c.x - 17, c.y - 10, 34, 48), Color(0.72, 0.72, 0.75))       # 몸통
	draw_rect(Rect2(c.x - 17, c.y - 10, 34, 48), Color(0.3, 0.3, 0.32), false, 2.0)
	draw_colored_polygon(PackedVector2Array([c + Vector2(-17, -10), c + Vector2(17, -10), c + Vector2(13, -40), c + Vector2(-21, -40)]), Color(0.8, 0.8, 0.84))   # 열린 뚜껑
	draw_rect(Rect2(c.x - 13, c.y - 36, 22, 22), Color(0.75, 0.88, 1.0, 0.85))   # 뚜껑 안 반사경
	if not mine:
		return
	var cheat_choose: bool = int(game.turn_type) == GambleMatch.TurnType.CHEAT and int(game.phase) == GambleMatch.Phase.PLAYER_CHOOSE
	if not cheat_choose:
		return
	if bool(game.covered[1]) and my_gaze == "shiner":
		_text(c + Vector2(0, -52), "덮개 — 안 비침", 14, Color(1, 0.6, 0.5))
	var p := float(game.peek_progress[0])
	if bool(game.peek_done[0]) and str(game.peek_source) == "shiner":
		draw_rect(Rect2(c.x - 13, c.y - 36, 22, 22), Color(1, 1, 1, 0.9))
		_text(c + Vector2(0, -52), str(RankCards.CARD_NAMES[int(game.committed[1])]), 18, Color(0.6, 1.0, 1.0))
	elif p > 0.0:
		draw_arc(c + Vector2(0, -5), 62.0, -PI / 2.0, -PI / 2.0 + TAU * p, 48, Color(1.0, 0.85, 0.3, 0.9), 5.0)
	if my_gaze == "shiner":
		draw_arc(c + Vector2(0, -5), 70.0, 0.0, TAU, 48, Color(1, 1, 1, 0.12), 2.0)


func _draw_slots() -> void:
	if int(game.committed[1]) != -1:
		var ra := Rect2(AI_SLOT - AI_SLOT_SIZE / 2.0, AI_SLOT_SIZE)
		_draw_card(ra, int(game.committed[1]), bool(game.revealed), false)
		if bool(game.covered[1]) and not bool(game.revealed):
			_draw_chip(ra.get_center())
	if int(game.committed[0]) != -1:
		var rm := Rect2(MY_SLOT - MY_SLOT_SIZE / 2.0, MY_SLOT_SIZE)
		_draw_card(rm, int(game.committed[0]), true, false)
		if bool(game.covered[0]) and not bool(game.revealed):
			_draw_chip(rm.get_center())
		if not bool(game.revealed):
			_text(Vector2(MY_SLOT.x + 170, MY_SLOT.y + 5), "← 내가 낸 카드 (상대에겐 뒷면)", 13, Color(1, 1, 1, 0.6))


func _draw_chip(c: Vector2) -> void:
	draw_circle(c, 20.0, Color(0.7, 0.1, 0.1))
	draw_arc(c, 15.0, 0.0, TAU, 24, Color(1, 1, 1, 0.9), 3.0)
	draw_circle(c, 9.0, Color(0.85, 0.15, 0.15))


func _draw_hand() -> void:
	var n: int = game.hands[0].size()
	var choosing: bool = int(game.phase) == GambleMatch.Phase.PLAYER_CHOOSE
	for i in n:
		var card: int = game.hands[0][i]
		if int(game.committed[0]) != -1 and i == game.hands[0].find(game.committed[0]):
			continue
		_draw_card(hand_rect(i, n), card, true, choosing and i == hover_index)


## 시선 보조선 (연습용): AI 눈에서 보는 곳까지
func _draw_helper() -> void:
	var target := str(game.gaze[1])
	if target == "face":
		_text(HEAD + Vector2(0, -78), "▼ 당신을 보는 중", 15, Color(1, 0.4, 0.3))
		return
	if target == "behind":
		_text(HEAD + Vector2(0, -78), "▶ 뒤를 돌아보는 중", 15, Color(1, 0.4, 0.3))
	if LOOK_AT.has(target):
		var to: Vector2 = LOOK_AT[target]
		draw_dashed_line(HEAD + _head_shift(), to, Color(1, 0.4, 0.3, 0.7), 2.0, 8.0)


func _draw_card(r: Rect2, card: int, face_up: bool, glow: bool) -> void:
	if glow:
		draw_rect(r.grow(5.0), Color(1.0, 0.85, 0.3, 0.8))
	draw_rect(r, Color(0.98, 0.96, 0.90) if face_up else Color(0.55, 0.10, 0.12))
	draw_rect(r, Color(0.08, 0.08, 0.08), false, 2.0)
	if not face_up or card < 0:
		draw_rect(r.grow(-6.0), Color(0.80, 0.25, 0.25), false, 2.0)
		return
	draw_circle(r.get_center() + Vector2(0, -r.size.y * 0.1), r.size.x * 0.22, _card_color(card))
	_text(Vector2(r.get_center().x, r.end.y - r.size.y * 0.12), str(RankCards.CARD_NAMES[card]), int(r.size.x * 0.2), Color(0.1, 0.1, 0.1))


func _card_color(card: int) -> Color:
	if card == RankCards.Card.KING:
		return Color(0.85, 0.65, 0.15)
	if card == RankCards.Card.ASSASSIN:
		return Color(0.45, 0.08, 0.10)
	return Color(0.35, 0.45, 0.60)


# ───────────────────────── 눈·머리 방향 ─────────────────────────

func _look_vec(target: String) -> Vector2:
	if not LOOK_AT.has(target):
		return Vector2(0, 1.5)   # "face": 정면 (사람을 봄)
	var to: Vector2 = LOOK_AT[target]
	var d: Vector2 = (to - HEAD).normalized()
	var v := Vector2(d.x * 7.0, d.y * 5.5)
	if target == "behind":
		v *= 1.6   # 뒤돌아보기: 고개를 크게 돌림
	return v


func _pupil_offset() -> Vector2:
	if game == null:
		return Vector2(0, 1.5)
	var cur := str(game.gaze[1])
	var prev := str(game.gaze_prev[1])
	var k := clampf((float(game.t) - float(game.gaze_since[1])) / CheatRules.TURN_TIME, 0.0, 1.0)
	return _look_vec(prev).lerp(_look_vec(cur), k)


func _head_shift() -> Vector2:
	return _pupil_offset() * 1.4


# ───────────────────────── 도우미 ─────────────────────────

func _text(center_baseline: Vector2, s: String, font_size: int, col: Color) -> void:
	var font: Font = ThemeDB.fallback_font
	var w := 420.0
	draw_string(font, Vector2(center_baseline.x - w / 2.0, center_baseline.y), s, HORIZONTAL_ALIGNMENT_CENTER, w, font_size, col)


func _ellipse(c: Vector2, rx: float, ry: float, col: Color) -> void:
	var pts := PackedVector2Array()
	for i in 24:
		var a := TAU * float(i) / 24.0
		pts.append(c + Vector2(cos(a) * rx, sin(a) * ry))
	draw_colored_polygon(pts, col)


func _cap(c: Vector2, r: float, a0: float, a1: float, col: Color) -> void:
	var pts := PackedVector2Array()
	for i in 21:
		var a := lerpf(a0, a1, float(i) / 20.0)
		pts.append(c + Vector2(cos(a), sin(a)) * r)
	draw_colored_polygon(pts, col)
