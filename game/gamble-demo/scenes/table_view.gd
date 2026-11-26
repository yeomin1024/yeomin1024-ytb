# VERSION: v0.2.0 — 2026-11-26 — 테이블 장면 그리기 (상대 인물·눈동자·잔·술병·카드) + 시선 판정 영역
#
# 화면 1280×800 기준 좌표. 규칙은 없고 game(core/match.gd) 상태를 그리기만 함.
# 시선 영역: 상대 얼굴(원) = "face" · 왼쪽 잔 = "glass" · 아래 내 패 = "own_card" · 나머지 = "table"
extends Control

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const GambleMatch = preload("res://core/match.gd")

const HEAD := Vector2(640, 196)
const HEAD_R := 62.0
const EYE_L := Vector2(615, 190)
const EYE_R := Vector2(665, 190)
const FACE_ZONE_R := 92.0
const GLASS := Vector2(330, 560)
const GLASS_ZONE := Rect2(270, 480, 120, 160)
const DRINK := Vector2(950, 505)
const AI_SLOT := Vector2(640, 500)
const AI_SLOT_SIZE := Vector2(64, 92)
const MY_SLOT := Vector2(640, 602)
const MY_SLOT_SIZE := Vector2(74, 104)
const HAND_Y := 728.0
const HAND_CARD := Vector2(92, 128)
const HAND_GAP := 106.0
const HAND_ZONE_Y := 655.0
## AI 눈이 향하는 화면 위치 ("face" = 화면 밖의 사람 = 정면)
const LOOK_AT := {"hands": Vector2(640, 760), "own_card": Vector2(640, 505), "away": Vector2(950, 470), "glass": Vector2(330, 545)}

const C_SKIN := Color(0.86, 0.72, 0.60)
const C_HAIR := Color(0.16, 0.12, 0.10)
const C_SUIT := Color(0.13, 0.14, 0.20)
const C_SHIRT := Color(0.85, 0.84, 0.80)
const C_FELT := Color(0.11, 0.33, 0.22)
const C_WOOD := Color(0.36, 0.22, 0.12)

var game = null
var hover_index := -1
var my_gaze := "table"
var show_helper := false


func gaze_target(p: Vector2) -> String:
	if p.distance_to(HEAD) <= FACE_ZONE_R:
		return "face"
	if GLASS_ZONE.has_point(p):
		return "glass"
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
	_draw_opponent_body()
	_draw_table()
	if game == null:
		return
	_draw_opponent_hands()
	_draw_drink()
	_draw_glass()
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
	_cap(h, HEAD_R + 4.0, PI * 1.12, PI * 1.88, C_HAIR)   # 머리선이 눈썹 위에 오게
	# 눈
	var off := _pupil_offset()
	for e in [EYE_L, EYE_R]:
		var ec: Vector2 = e + shift
		_ellipse(ec, 13.0, 9.0, Color(0.97, 0.97, 0.95))
		draw_circle(ec + off, 5.5, Color(0.12, 0.09, 0.07))
		draw_circle(ec + off + Vector2(-1.5, -1.5), 1.6, Color(1, 1, 1, 0.8))
	# 눈썹 — 의심이 클수록 찌푸림
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
	# 손에 든 남은 카드 (뒷면)
	var n: int = game.hands[1].size()
	if int(game.committed[1]) != -1 and not bool(game.revealed):
		n -= 1
	for i in n:
		var r := Rect2(Vector2(452 + i * 14, 400 - i * 2), Vector2(34, 50))
		_draw_card(r, -1, false, false)


func _draw_drink() -> void:
	draw_rect(Rect2(DRINK.x - 20, DRINK.y - 30, 40, 80), Color(0.55, 0.30, 0.08, 0.85))
	draw_rect(Rect2(DRINK.x - 7, DRINK.y - 62, 14, 34), Color(0.45, 0.24, 0.06, 0.9))
	draw_rect(Rect2(DRINK.x - 14, DRINK.y - 5, 28, 24), Color(0.92, 0.88, 0.75))


func _draw_glass() -> void:
	var c := GLASS
	var top_y := c.y - 55.0
	var bot_y := c.y + 55.0
	var poly := PackedVector2Array([Vector2(c.x - 35, top_y), Vector2(c.x + 35, top_y), Vector2(c.x + 27, bot_y), Vector2(c.x - 27, bot_y)])
	draw_colored_polygon(poly, Color(0.75, 0.85, 0.95, 0.18))
	var outline := poly.duplicate()
	outline.append(poly[0])
	draw_polyline(outline, Color(0.85, 0.92, 1.0, 0.6), 2.0)
	_ellipse(Vector2(c.x, top_y), 35.0, 7.0, Color(0.85, 0.92, 1.0, 0.25))
	draw_line(Vector2(c.x - 22, top_y + 12), Vector2(c.x - 16, bot_y - 14), Color(1, 1, 1, 0.35), 3.0)
	var cheat_turn: bool = int(game.turn_type) == GambleMatch.TurnType.CHEAT and int(game.phase) == GambleMatch.Phase.PLAYER_CHOOSE
	if cheat_turn:
		var p := float(game.peek_progress[0])
		if bool(game.peek_done[0]):
			draw_rect(Rect2(c.x - 22, c.y - 30, 44, 62), Color(0.98, 0.96, 0.9, 0.55))
			_text(Vector2(c.x, c.y + 8), str(RankCards.CARD_NAMES[int(game.committed[1])]), 18, Color(0.1, 0.1, 0.1))
		elif p > 0.0:
			draw_arc(c, 78.0, -PI / 2.0, -PI / 2.0 + TAU * p, 48, Color(1.0, 0.85, 0.3, 0.9), 5.0)
	if my_gaze == "glass":
		draw_arc(c, 86.0, 0.0, TAU, 48, Color(1, 1, 1, 0.12), 2.0)


func _draw_slots() -> void:
	if int(game.committed[1]) != -1:
		_draw_card(Rect2(AI_SLOT - AI_SLOT_SIZE / 2.0, AI_SLOT_SIZE), int(game.committed[1]), bool(game.revealed), false)
	if int(game.committed[0]) != -1:
		_draw_card(Rect2(MY_SLOT - MY_SLOT_SIZE / 2.0, MY_SLOT_SIZE), int(game.committed[0]), true, false)
		if not bool(game.revealed):
			_text(Vector2(MY_SLOT.x + 170, MY_SLOT.y + 5), "← 내가 낸 카드 (상대에겐 뒷면)", 13, Color(1, 1, 1, 0.6))


func _draw_hand() -> void:
	var n: int = game.hands[0].size()
	var choosing: bool = int(game.phase) == GambleMatch.Phase.PLAYER_CHOOSE
	for i in n:
		var card: int = game.hands[0][i]
		if int(game.committed[0]) != -1 and i == game.hands[0].find(game.committed[0]):
			continue   # 이미 낸 카드는 패에서 숨김
		_draw_card(hand_rect(i, n), card, true, choosing and i == hover_index)


## 시선 보조선 (연습용): AI 눈에서 보는 곳까지
func _draw_helper() -> void:
	var target := str(game.gaze[1])
	if target == "face":
		_text(HEAD + Vector2(0, -78), "▼ 당신을 보는 중", 15, Color(1, 0.4, 0.3))
		return
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
	return Vector2(d.x * 7.0, d.y * 5.5)


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
