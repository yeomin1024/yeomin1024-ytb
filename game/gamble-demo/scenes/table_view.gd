# VERSION: v0.7.0 — 2026-11-26 — 직관 표시: 엿본 카드를 테이블에 그림 · 노예 턴 할 일 안내(물건·협력자 옆) · 보는 물건 노란 고리 · 상대 상태 글을 턱 아래로(위쪽 안내 막대와 안 겹치게)
# 이전 VERSION: v0.5.0 — 2026-11-26 — 물건 3자리(라이터·담뱃갑·술잔·휴대폰) · 내 협력자(상대 뒤)·상대 협력자 그림자 · 시선 끌기 가림 · 덮개·무작위 표시
# 이전 VERSION: v0.4.0 — 2026-11-26 — 라이터(뚜껑 안 반사경) · 상대 뒤 협력자(손 신호) · 카드 덮개 칩 · 뒤돌아보는 상대
#
# 화면 1280×800 기준 좌표. 규칙은 없고 game(core/match.gd) 상태를 그리기만 함.
# 사람 시선 영역: 상대 얼굴 = "face" · (내가 노예일 때) 내 물건 = "obj0~2" · 상대 뒤 협력자 자리 = "accomplice"
#                · 아래 내 패 = "own_card" · 나머지 = "table"
extends Control

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const GambleMatch = preload("res://core/match.gd")

const HEAD := Vector2(640, 196)
const HEAD_R := 62.0
const EYE_L := Vector2(615, 190)
const EYE_R := Vector2(665, 190)
const FACE_ZONE_R := 92.0
const MY_SLOTS := [Vector2(230, 600), Vector2(320, 600), Vector2(410, 600)]   # 내 물건 (왼쪽)
const AI_SLOTS := [Vector2(870, 600), Vector2(960, 600), Vector2(1050, 600)]  # 상대 물건 (오른쪽)
const OBJ_ZONE := Vector2(42, 58)            # 물건 시선 영역 반폭·반높이
const ACC_POS := Vector2(880, 250)           # 내 협력자가 서는 자리 (상대 오른쪽 뒤)
const ACC_ZONE_R := 80.0
const ACC_START := Vector2(1340, 250)
const AI_SLOT := Vector2(640, 500)
const AI_SLOT_SIZE := Vector2(64, 92)
const MY_SLOT := Vector2(640, 602)
const MY_SLOT_SIZE := Vector2(74, 104)
const HAND_Y := 728.0
const HAND_CARD := Vector2(92, 128)
const HAND_GAP := 106.0
const HAND_ZONE_Y := 655.0
## AI 눈이 향하는 곳 — 왕일 때: hands·own_card·away·behind / 노예일 때: objN·accomplice(당신 머리 너머)
const LOOK_AT := {"hands": Vector2(640, 760), "own_card": Vector2(640, 505), "away": Vector2(1150, 320),
	"behind": Vector2(1200, 120), "accomplice": Vector2(760, -200), "table": Vector2(640, 560)}

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
var seen_card := -1          # 이번 턴 내가 엿본 카드 (main.gd 가 info 이벤트로 넣음, 턴마다 비움)
var seen_source := ""        # "peek" / "acc"


func gaze_target(p: Vector2) -> String:
	if p.distance_to(HEAD) <= FACE_ZONE_R:
		return "face"
	if game != null and int(game.slave) == 0:
		var objs: Array = game.objects[0]
		for i in objs.size():
			var c: Vector2 = MY_SLOTS[i]
			if absf(p.x - c.x) <= OBJ_ZONE.x and absf(p.y - (c.y - 15.0)) <= OBJ_ZONE.y:
				return "obj%d" % i
		if p.distance_to(ACC_POS) <= ACC_ZONE_R:
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
		_draw_my_accomplice()
	_draw_opponent_body()
	_draw_table()
	if game == null:
		return
	_draw_opponent_hands()
	for i in game.objects[0].size():
		_draw_object(MY_SLOTS[i], str(game.objects[0][i]), true, my_gaze == "obj%d" % i)
	for i in game.objects[1].size():
		_draw_object(AI_SLOTS[i], str(game.objects[1][i]), false, false)
	_draw_ai_accomplice_shadow()
	_draw_slots()
	_draw_seen()
	_draw_hand()
	_draw_hints()
	if show_helper:
		_draw_helper()


func _ai_blind() -> bool:
	# 상대(AI 노예)가 시선 끌기를 쓰면 그동안 상대 눈이 안 보임
	return int(game.slave) == 1 and int(game.phase) == GambleMatch.Phase.SLAVE_TURN and float(game.t) < float(game.blind_until)


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
	if game != null and _ai_blind():
		# 시선 끌기: 쓰러진 술잔을 닦느라 고개를 숙임 — 눈이 안 보임
		draw_rect(Rect2(h.x - 52, h.y - 26, 104, 30), C_HAIR)
		_text(h + Vector2(0, 92), "술잔을 닦는 중 — 눈이 안 보임", 16, Color(1, 0.7, 0.5))
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


## 물건 — 반사경이 있든 없든 겉모양은 같음 (내 것엔 작은 표시)
func _draw_object(c: Vector2, kind: String, mine: bool, looking: bool) -> void:
	var look := str(CheatRules.OBJECTS[kind]["look"])
	if look == "lighter":
		draw_rect(Rect2(c.x - 17, c.y - 10, 34, 48), Color(0.72, 0.72, 0.75))
		draw_rect(Rect2(c.x - 17, c.y - 10, 34, 48), Color(0.3, 0.3, 0.32), false, 2.0)
		draw_colored_polygon(PackedVector2Array([c + Vector2(-17, -10), c + Vector2(17, -10), c + Vector2(13, -40), c + Vector2(-21, -40)]), Color(0.8, 0.8, 0.84))
		draw_rect(Rect2(c.x - 13, c.y - 36, 22, 22), Color(0.75, 0.88, 1.0, 0.6))
	elif look == "cigcase":
		draw_rect(Rect2(c.x - 26, c.y - 6, 52, 40), Color(0.75, 0.68, 0.40))
		draw_rect(Rect2(c.x - 26, c.y - 6, 52, 40), Color(0.35, 0.3, 0.15), false, 2.0)
		draw_rect(Rect2(c.x - 22, c.y - 2, 44, 10), Color(0.9, 0.85, 0.6, 0.7))
	elif look == "glass":
		draw_colored_polygon(PackedVector2Array([c + Vector2(-22, -30), c + Vector2(22, -30), c + Vector2(17, 34), c + Vector2(-17, 34)]), Color(0.75, 0.85, 0.95, 0.25))
		draw_rect(Rect2(c.x - 17, c.y + 6, 34, 26), Color(0.6, 0.35, 0.1, 0.6))
	else:
		draw_rect(Rect2(c.x - 18, c.y - 30, 36, 64), Color(0.08, 0.08, 0.1))
		draw_rect(Rect2(c.x - 15, c.y - 26, 30, 54), Color(0.15, 0.2, 0.3))
	if mine:
		var mark := "반사경" if CheatRules.is_mirror(kind) else "빈 것"
		_text(c + Vector2(0, 54), mark, 12, Color(1, 1, 1, 0.45))
	if looking:
		draw_arc(c + Vector2(0, -5), 58.0, 0.0, TAU, 40, Color(1, 0.9, 0.3, 0.55), 3.0)


func _draw_my_accomplice() -> void:
	var state := str(game.acc_state[0])
	if state != "walking" and state != "present":
		return
	var pos := ACC_POS
	if state == "walking":
		var k := clampf(1.0 - float(game.acc_walk_left[0]) / CheatRules.ACC_WALK_SECONDS, 0.0, 1.0)
		pos = ACC_START.lerp(ACC_POS, k)
	draw_colored_polygon(PackedVector2Array([pos + Vector2(-60, -60), pos + Vector2(60, -60), pos + Vector2(75, 190), pos + Vector2(-75, 190)]), C_COAT)
	draw_circle(pos + Vector2(0, -95), 34.0, C_SKIN.darkened(0.25))
	_cap(pos + Vector2(0, -95), 37.0, PI * 1.05, PI * 1.95, C_HAIR)
	var hand := pos + Vector2(25, 15)
	draw_circle(hand, 13.0, C_SKIN.darkened(0.15))
	if state == "present" and my_gaze == "accomplice":
		for i in 3:
			draw_line(hand + Vector2(-8 + i * 8, -6), hand + Vector2(-10 + i * 10, -24), C_SKIN.darkened(0.15), 4.0)
		draw_arc(pos, ACC_ZONE_R, 0.0, TAU, 48, Color(1, 1, 1, 0.12), 2.0)


## 상대 협력자는 내 뒤에 있어 안 보임 — 테이블에 비친 그림자로만
func _draw_ai_accomplice_shadow() -> void:
	var state := str(game.acc_state[1])
	if state != "walking" and state != "present":
		return
	var a := 0.35 if state == "present" else 0.18
	_ellipse(Vector2(150, 760), 120.0, 34.0, Color(0, 0, 0, a))
	_text(Vector2(150, 788), "(내 뒤에 누군가 서 있다)", 13, Color(1, 1, 1, 0.5))


func _draw_slots() -> void:
	if int(game.committed[1]) != -1:
		var ra := Rect2(AI_SLOT - AI_SLOT_SIZE / 2.0, AI_SLOT_SIZE)
		_draw_card(ra, int(game.committed[1]), bool(game.revealed), false)
		if int(game.king) == 1 and not bool(game.revealed):
			_draw_king_marks(ra)
	if int(game.committed[0]) != -1:
		var rm := Rect2(MY_SLOT - MY_SLOT_SIZE / 2.0, MY_SLOT_SIZE)
		_draw_card(rm, int(game.committed[0]), true, false)
		if int(game.king) == 0 and not bool(game.revealed):
			_draw_king_marks(rm)
			if bool(game.faked):
				_text(Vector2(MY_SLOT.x + 110, MY_SLOT.y + 28), "바꿔치기 준비됨", 13, Color(1, 0.8, 0.4))
		if not bool(game.revealed):
			_text(Vector2(MY_SLOT.x + 110, MY_SLOT.y + 5), "← 내 카드 (상대에겐 뒷면)", 13, Color(1, 1, 1, 0.6))


## 엿본 카드 — 상대가 엎은 카드 옆에 반투명하게 (바꿔치기면 가짜일 수 있음)
func _draw_seen() -> void:
	if seen_card < 0 or bool(game.revealed):
		return
	var r := Rect2(Vector2(692, 466), Vector2(48, 68))
	draw_rect(r.grow(4.0), Color(0.3, 0.9, 1.0, 0.35))
	_draw_card(r, seen_card, true, false)
	_text(Vector2(r.get_center().x, r.position.y - 8), "엿본 카드" if seen_source == "peek" else "협력자 신호", 14, Color(0.5, 0.95, 1.0))


## 노예 턴 할 일 안내 — 물건 줄 위·협력자 옆 (내가 노예이고 아직 안 냈을 때)
func _draw_hints() -> void:
	if int(game.slave) != 0 or int(game.phase) != GambleMatch.Phase.SLAVE_TURN or int(game.committed[0]) != -1:
		return
	var msg := ""
	var col := Color(1.0, 0.9, 0.45)
	var has_mirror := false
	for k in game.objects[0]:
		if CheatRules.is_mirror(str(k)):
			has_mirror = true
	if bool(game.sealed[0]["peek"]):
		msg = "엿보기 봉인됨 — 반사경을 봐도 소용없음"
		col = Color(1.0, 0.45, 0.4)
	elif bool(game.randomized):
		msg = "상대가 카드를 안 보고 냄 — 엿볼 수 없음"
		col = Color(1.0, 0.45, 0.4)
	elif bool(game.covered):
		msg = "상대가 칩으로 가림 — 반사경 안 통함"
		col = Color(1.0, 0.45, 0.4)
	elif has_mirror:
		msg = "반사경 물건을 1.5초 계속 보면 상대 카드"
	else:
		msg = "반사경 물건이 없음 — 왼쪽 버튼으로 놓기"
	_text(Vector2(330, 546), msg, 15, col)
	if str(game.acc_state[0]) == "present" and not bool(game.sealed[0]["acc"]) and not bool(game.randomized):
		_text(Vector2(880, 470), "협력자 손을 1.8초 계속 보기", 15, Color(1.0, 0.9, 0.45))


func _draw_king_marks(r: Rect2) -> void:
	if bool(game.covered):
		var c := r.get_center()
		draw_circle(c, 20.0, Color(0.7, 0.1, 0.1))
		draw_arc(c, 15.0, 0.0, TAU, 24, Color(1, 1, 1, 0.9), 3.0)
		draw_circle(c, 9.0, Color(0.85, 0.15, 0.15))
	if bool(game.randomized):
		_text(Vector2(r.get_center().x, r.position.y - 8), "무작위", 13, Color(1, 0.9, 0.5))


func _draw_hand() -> void:
	var n: int = game.hands[0].size()
	var my_turn: bool = (int(game.phase) == GambleMatch.Phase.KING_TURN or int(game.phase) == GambleMatch.Phase.SLAVE_TURN) and game.actor() == 0
	for i in n:
		var card: int = game.hands[0][i]
		if int(game.committed[0]) != -1 and i == game.hands[0].find(game.committed[0]):
			continue
		_draw_card(hand_rect(i, n), card, true, my_turn and i == hover_index)


func _draw_helper() -> void:
	if _ai_blind():
		return
	var target := str(game.gaze[1])
	if target == "face":
		_text(HEAD + Vector2(0, 92), "▼ 당신을 보는 중", 15, Color(1, 0.4, 0.3))
		return
	var to := _look_point(target)
	if target == "behind":
		_text(HEAD + Vector2(0, 92), "▶ 뒤를 돌아보는 중", 15, Color(1, 0.4, 0.3))
	elif target == "accomplice":
		_text(HEAD + Vector2(0, 92), "▲ 당신 뒤를 보는 중", 15, Color(1, 0.4, 0.3))
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

func _look_point(target: String) -> Vector2:
	if target.begins_with("obj"):
		var idx := int(target.substr(3))
		if idx >= 0 and idx < AI_SLOTS.size():
			return AI_SLOTS[idx]
	if LOOK_AT.has(target):
		return LOOK_AT[target]
	return Vector2(640, 900)


func _look_vec(target: String) -> Vector2:
	if target == "face" or target == "":
		return Vector2(0, 1.5)   # 정면 (사람을 봄)
	var to := _look_point(target)
	var d: Vector2 = (to - HEAD).normalized()
	var v := Vector2(d.x * 7.0, d.y * 5.5)
	if target == "behind":
		v *= 1.6
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
