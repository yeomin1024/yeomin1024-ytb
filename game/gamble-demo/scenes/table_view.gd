# VERSION: v0.8.0 — 2026-11-26 — 두 화면: 내가 고를 땐 내 테이블만 / 상대가 고를 땐 상대 테이블만 · 상대 시선 = 불빛 · 물건에 머물면 게이지 → 다 차면 '!' · 협력자 = 귀 만지기(수상한 행동) · 클릭 대상(물건 확인·몸 수색) 표시
# 이전 VERSION: v0.7.0 — 2026-11-26 — 직관 표시: 엿본 카드를 테이블에 그림 · 노예 턴 할 일 안내 · 보는 물건 노란 고리 · 상대 상태 글을 턱 아래로
# 이전 VERSION: v0.5.0 — 2026-11-26 — 물건 3자리(라이터·담뱃갑·술잔·휴대폰) · 내 협력자(상대 뒤)·상대 협력자 그림자 · 시선 끌기 가림 · 덮개·무작위 표시
#
# 화면 1280×800 기준 좌표. 규칙은 없고 game(core/match.gd) 상태를 그리기만 함. 사람 = 자리 0, AI = 자리 1.
# view = "mine"  : 내 테이블 (내 물건·내 패·내가 낸 카드, 위쪽 = 상대 쪽). 사람 시선: 위쪽 "face"(상대를 봄) · 내 물건 "objN" · 패 "own_card"
# view = "theirs": 상대 테이블 (상대·상대 물건·상대 패). 사람 시선: 얼굴 "face" · 몸·손 "hands" · 상대 물건 "objN"
extends Control

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")
const GambleMatch = preload("res://core/match.gd")

const HAND_Y := 728.0
const HAND_CARD := Vector2(92, 128)
const HAND_GAP := 106.0
const HAND_ZONE_Y := 655.0
const OBJ_ZONE := Vector2(46, 62)
const SLOT_SIZE := Vector2(70, 100)
# 상대 테이블
const HEAD := Vector2(640, 196)
const HEAD_R := 62.0
const EYE_L := Vector2(615, 190)
const EYE_R := Vector2(665, 190)
const FACE_ZONE_R := 92.0
const BODY_ZONE := Rect2(410, 290, 460, 190)
const T_OBJ := [Vector2(850, 600), Vector2(960, 610), Vector2(1070, 600)]
const T_SLOT := Vector2(640, 525)
const T_MY_CARD := Vector2(640, 705)
const T_LOOK := {"own_card": Vector2(640, 445), "face": Vector2(640, 790), "hands": Vector2(640, 790),
	"away": Vector2(1180, 330), "table": Vector2(640, 570)}
# 내 테이블
const M_TOP_Y := 300.0
const M_OBJ := [Vector2(430, 440), Vector2(640, 420), Vector2(850, 440)]
const M_SLOT := Vector2(640, 595)
const M_OPP_CARD := Vector2(640, 220)

const C_SKIN := Color(0.86, 0.72, 0.60)
const C_HAIR := Color(0.16, 0.12, 0.10)
const C_SUIT := Color(0.13, 0.14, 0.20)
const C_SHIRT := Color(0.85, 0.84, 0.80)
const C_FELT := Color(0.11, 0.33, 0.22)
const C_WOOD := Color(0.36, 0.22, 0.12)
const C_LIGHT := Color(1.0, 0.86, 0.45)
const C_MARK := Color(1.0, 0.78, 0.12)

var game = null
var view := "theirs"
var hover_index := -1
var my_gaze := "table"
var hover_pick := ""          # 상대 테이블에서 클릭할 대상 ("obj0".. / "body") — main.gd 가 방어 때만 넣음
var seen_card := -1           # 이번 턴 내가 엿본 카드
var seen_source := ""         # "peek" / "acc"
var hide_my_card := false     # 내가 섞기를 써서 내 카드도 모름
var clock := 0.0
var _light := Vector2(640, 420)


func gaze_target(p: Vector2) -> String:
	if game == null:
		return "table"
	if view == "mine":
		for i in mini(game.objects[0].size(), 3):
			if _in_obj(p, M_OBJ[i]):
				return "obj%d" % i
		if p.y < M_TOP_Y:
			return "face"
		if p.y >= HAND_ZONE_Y:
			return "own_card"
		return "table"
	if p.distance_to(HEAD) <= FACE_ZONE_R:
		return "face"
	for i in mini(game.objects[1].size(), 3):
		if _in_obj(p, T_OBJ[i]):
			return "obj%d" % i
	if BODY_ZONE.has_point(p):
		return "hands"
	return "table"


## 상대 테이블에서 클릭 대상: 물건 "objN" (물건 확인) / 상대 "body" (몸 수색)
func pick_target(p: Vector2) -> String:
	if game == null or view != "theirs":
		return ""
	for i in mini(game.objects[1].size(), 3):
		if _in_obj(p, T_OBJ[i]):
			return "obj%d" % i
	if p.distance_to(HEAD) <= FACE_ZONE_R or BODY_ZONE.has_point(p):
		return "body"
	return ""


func hand_rect(i: int, n: int) -> Rect2:
	var cx := 640.0 + (float(i) - float(n - 1) / 2.0) * HAND_GAP
	var lift := 16.0 if i == hover_index else 0.0
	return Rect2(Vector2(cx - HAND_CARD.x / 2.0, HAND_Y - HAND_CARD.y / 2.0 - lift), HAND_CARD)


func card_at(p: Vector2) -> int:
	if game == null or view != "mine":
		return -1
	var n: int = game.hands[0].size()
	for i in n:
		if hand_rect(i, n).has_point(p):
			return i
	return -1


func _in_obj(p: Vector2, c: Vector2) -> bool:
	return absf(p.x - c.x) <= OBJ_ZONE.x and absf(p.y - (c.y - 15.0)) <= OBJ_ZONE.y


# ───────────────────────── 그리기 ─────────────────────────

func _draw() -> void:
	draw_rect(Rect2(0, 0, 1280, 800), Color(0.06, 0.05, 0.07))
	if game == null:
		return
	if view == "mine":
		_draw_mine()
	else:
		_draw_theirs()


## 노예 시선이 상대에게 보이나 (시선 끌기 중이면 안 보임)
func _slave_visible() -> bool:
	return float(game.t) >= float(game.blind_until)


# ───────── 상대 테이블 ─────────

func _draw_theirs() -> void:
	draw_circle(Vector2(640, 40), 300.0, Color(0.15, 0.11, 0.09, 0.55))
	var ai_slave: bool = int(game.slave) == 1
	var blind: bool = ai_slave and int(game.phase) == GambleMatch.Phase.SLAVE_TURN and not _slave_visible()
	_draw_opponent(blind)
	draw_colored_polygon(PackedVector2Array([Vector2(190, 440), Vector2(1090, 440), Vector2(1280, 800), Vector2(0, 800)]), C_FELT)
	draw_line(Vector2(190, 440), Vector2(1090, 440), C_WOOD, 10.0)
	_draw_opponent_hands()
	# 상대 물건 (+ 게이지 · '!' · 확인됨)
	var dwell_idx := -1
	if ai_slave and not blind:
		dwell_idx = _dwell_index(1)
	for i in mini(game.objects[1].size(), 3):
		var c: Vector2 = T_OBJ[i]
		_draw_object(c, str(game.objects[1][i]), false, hover_pick == "obj%d" % i, 1.0)
		if bool(game.checked[1][i]):
			_text(c + Vector2(0, 58), "빈 것 (확인됨)", 13, Color(0.7, 0.9, 0.7))
		if i == dwell_idx:
			_gauge(c + Vector2(0, -8), float(game.dwell_progress()))
		if ai_slave and i < game.marks.size() and bool(game.marks[i]):
			_mark(c)
	# 상대가 낸 카드 · 내가 낸 카드
	if int(game.committed[1]) != -1:
		var r := Rect2(T_SLOT - SLOT_SIZE / 2.0, SLOT_SIZE)
		_draw_card(r, int(game.committed[1]), bool(game.revealed), false)
		if int(game.king) == 1 and not bool(game.revealed):
			_draw_king_marks(r)
	if int(game.committed[0]) != -1:
		_draw_my_card(T_MY_CARD, Vector2(64, 92))
	# 상대 시선 불빛
	if not blind:
		_draw_light_theirs()
	# 클릭 대상 표시
	if hover_pick == "body":
		draw_arc(HEAD, FACE_ZONE_R, 0.0, TAU, 48, Color(1, 0.5, 0.3, 0.8), 3.0)
		draw_rect(BODY_ZONE, Color(1, 0.5, 0.3, 0.8), false, 3.0)
		_text(HEAD + Vector2(0, -80), "클릭: 몸 수색 (이어폰 찾기)", 18, Color(1, 0.7, 0.5))
	elif hover_pick.begins_with("obj"):
		var idx := int(hover_pick.substr(3))
		if idx >= 0 and idx < 3:
			_text(T_OBJ[idx] + Vector2(0, -112), "클릭: 물건 확인", 17, Color(1, 0.7, 0.5))


func _draw_opponent(blind: bool) -> void:
	var shift := _pupil_offset() * 1.4
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
	var furrow := clampf((float(game.brains[1].suspicion) + 1.7) / 4.0, 0.0, 1.0) * 6.0
	draw_line(EYE_L + shift + Vector2(-14, -17), EYE_L + shift + Vector2(12, -17 + furrow), C_HAIR, 4.0)
	draw_line(EYE_R + shift + Vector2(-12, -17 + furrow), EYE_R + shift + Vector2(14, -17), C_HAIR, 4.0)
	draw_line(h + Vector2(-16, 36), h + Vector2(16, 36), Color(0.45, 0.20, 0.20), 3.0)
	if blind:
		draw_rect(Rect2(h.x - 52, h.y - 26, 104, 30), C_HAIR)
		_text(h + Vector2(0, 92), "술잔을 쏟았다 — 3초간 상대 눈이 안 보임", 16, Color(1, 0.7, 0.5))
	elif bool(game.calling[1]):
		# 수상한 행동: 귀를 만지작
		var ear := h + Vector2(HEAD_R + 6.0, 0)
		draw_line(Vector2(790, 330), ear + Vector2(10, 18), C_SUIT, 18.0)
		draw_circle(ear + Vector2(6, 6), 16.0, C_SKIN.darkened(0.1))
		var k := 0.5 + 0.5 * sin(clock * 9.0)
		_text(ear + Vector2(40, -30), "?", 34, Color(1, 0.4 + 0.4 * k, 0.3))
		_text(h + Vector2(0, 92), "귀를 만지작거린다…", 16, Color(1, 0.6, 0.4))


func _draw_opponent_hands() -> void:
	for hc in [Vector2(505, 462), Vector2(775, 462)]:
		draw_rect(Rect2(hc.x - 26, hc.y - 34, 52, 18), C_SUIT)
		draw_circle(hc, 22.0, C_SKIN)
	var n: int = game.hands[1].size()
	if int(game.committed[1]) != -1 and not bool(game.revealed):
		n -= 1
	for i in n:
		_draw_card(Rect2(Vector2(452 + i * 14, 400 - i * 2), Vector2(34, 50)), -1, false, false)


## 상대 시선 불빛 — 상대가 보는 자리가 밝아짐 (나를 보면 아래쪽이 밝아지고 글)
func _draw_light_theirs() -> void:
	var g := str(game.gaze[1])
	var target: Vector2 = T_LOOK.get(g, Vector2(640, 570))
	if g.begins_with("obj"):
		var idx := int(g.substr(3))
		if idx >= 0 and idx < 3:
			target = T_OBJ[idx]
	_light = _light.lerp(target, 0.22)
	if g == "face" or g == "hands":
		_glow(Vector2(640, 800), 260.0, Color(1.0, 0.45, 0.35, 0.5))
		_text(Vector2(640, 662), "상대가 당신을 보는 중", 18, Color(1, 0.55, 0.45))
		return
	if g == "away":
		_text(Vector2(1120, 300), "딴 곳을 봄", 15, Color(1, 1, 1, 0.5))
		return
	_glow(_light, 95.0, Color(C_LIGHT.r, C_LIGHT.g, C_LIGHT.b, 0.55))


# ───────── 내 테이블 ─────────

func _draw_mine() -> void:
	# 위쪽 = 상대 쪽 (어둡게 · 상대가 낸 카드)
	draw_rect(Rect2(0, 120, 1280, M_TOP_Y - 120), Color(0.09, 0.07, 0.08))
	draw_colored_polygon(PackedVector2Array([Vector2(520, 300), Vector2(760, 300), Vector2(720, 150), Vector2(560, 150)]), Color(0.11, 0.11, 0.15))
	draw_circle(Vector2(640, 128), 46.0, Color(0.13, 0.12, 0.14))
	_text(Vector2(640, 290), "▲ 위쪽 = 상대를 봄", 13, Color(1, 1, 1, 0.35))
	draw_rect(Rect2(0, M_TOP_Y, 1280, 800 - M_TOP_Y), C_FELT)
	draw_line(Vector2(0, M_TOP_Y), Vector2(1280, M_TOP_Y), C_WOOD, 10.0)
	if int(game.committed[1]) != -1:
		var r := Rect2(M_OPP_CARD - Vector2(28, 40), Vector2(56, 80))
		_draw_card(r, int(game.committed[1]), bool(game.revealed), false)
		if int(game.king) == 1 and not bool(game.revealed):
			_draw_king_marks(r)
	if seen_card >= 0 and not bool(game.revealed):
		var sr := Rect2(M_OPP_CARD + Vector2(48, -40), Vector2(56, 80))
		draw_rect(sr.grow(4.0), Color(0.3, 0.9, 1.0, 0.35))
		_draw_card(sr, seen_card, true, false)
		_text(Vector2(sr.get_center().x, sr.position.y - 8), "엿본 카드" if seen_source == "peek" else "이어폰", 14, Color(0.5, 0.95, 1.0))
	# 내 물건 (+ 내 게이지 · '!' = 상대가 봄)
	var me_slave: bool = int(game.slave) == 0
	var dwell_idx := _dwell_index(0) if me_slave else -1
	for i in mini(game.objects[0].size(), 3):
		var c: Vector2 = M_OBJ[i]
		_draw_object(c, str(game.objects[0][i]), true, my_gaze == "obj%d" % i, 1.25)
		if i == dwell_idx:
			var k := float(game.dwell_progress())
			_gauge(c + Vector2(0, -8), k)
			if k >= 1.0 and not _slave_visible():
				_text(c + Vector2(0, -92), "안 들킴", 16, Color(0.5, 1.0, 0.6))
		if me_slave and i < game.marks.size() and bool(game.marks[i]):
			_mark(c)
	if int(game.committed[0]) != -1:
		_draw_my_card(M_SLOT, SLOT_SIZE)
	_draw_hand()
	_draw_hints()
	_draw_light_mine()


## 상대(지켜보는 쪽) 시선 — 내 테이블 위 불빛 / 나를 보면 위쪽이 붉게
func _draw_light_mine() -> void:
	if int(game.slave) == 0 and int(game.phase) == GambleMatch.Phase.SLAVE_TURN and not _slave_visible():
		_text(Vector2(640, 172), "시선 끌기 중 — 상대가 당신을 못 봄", 17, Color(0.5, 1.0, 0.6))
		return
	var g := str(game.gaze[1])
	if g == "face":
		_glow(Vector2(640, 150), 240.0, Color(1.0, 0.4, 0.3, 0.55))
		_text(Vector2(640, 168), "상대가 당신을 보는 중", 19, Color(1, 0.6, 0.5))
	elif g == "hands":
		_light = _light.lerp(Vector2(640, 715), 0.22)
		_glow(_light, 170.0, Color(1.0, 0.45, 0.35, 0.45))
		_text(Vector2(640, 168), "상대가 당신 손을 보는 중", 17, Color(1, 0.6, 0.5))
	elif g == "own_card":
		_text(Vector2(640, 168), "상대: 자기 카드를 봄", 15, Color(1, 1, 1, 0.55))
	else:
		_text(Vector2(640, 168), "상대: 딴 곳을 봄", 15, Color(1, 1, 1, 0.55))
	# 위쪽을 보고 있으면 상대의 수상한 행동이 보임
	if my_gaze == "face" and bool(game.calling[1]):
		_text(Vector2(640, 246), "상대가 귀를 만지작거린다!", 18, Color(1, 0.7, 0.3))


## 내 노예 턴 할 일 안내 (물건 줄 아래)
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
		msg = "엿보기 봉인됨 — 반사경이 압수됨"
		col = Color(1.0, 0.45, 0.4)
	elif bool(game.randomized):
		msg = "상대가 카드를 섞음 — 엿볼 수 없음"
		col = Color(1.0, 0.45, 0.4)
	elif bool(game.covered):
		msg = "상대가 칩으로 가림 — 반사경 안 통함"
		col = Color(1.0, 0.45, 0.4)
	elif has_mirror:
		msg = "반사경 물건을 %.1f초 계속 보면 상대 카드 (게이지가 차면 상대에게 '!')" % CheatRules.PEEK_FIX
	else:
		msg = "반사경 물건이 없음 — 왼쪽 버튼으로 놓기"
	_text(Vector2(640, 530), msg, 15, col)


func _draw_hand() -> void:
	var n: int = game.hands[0].size()
	var my_turn: bool = (int(game.phase) == GambleMatch.Phase.KING_TURN or int(game.phase) == GambleMatch.Phase.SLAVE_TURN) and game.actor() == 0 and int(game.committed[0]) == -1
	var skip := -1
	if int(game.committed[0]) != -1:
		skip = game.hands[0].find(game.committed[0])
	for i in n:
		if i == skip:
			continue
		_draw_card(hand_rect(i, n), int(game.hands[0][i]), true, my_turn and i == hover_index)


# ───────── 공통 그림 ─────────

func _dwell_index(seat: int) -> int:
	if int(game.phase) != GambleMatch.Phase.SLAVE_TURN or int(game.slave) != seat:
		return -1
	var g := str(game.gaze[seat])
	if not g.begins_with("obj"):
		return -1
	var idx := int(g.substr(3))
	return idx if idx >= 0 and idx < game.objects[seat].size() else -1


func _draw_my_card(c: Vector2, sz: Vector2) -> void:
	var r := Rect2(c - sz / 2.0, sz)
	var unknown: bool = hide_my_card and not bool(game.revealed)
	_draw_card(r, -1 if unknown else int(game.committed[0]), not unknown, false)
	if unknown:
		_text(r.get_center() + Vector2(0, 10), "?", 34, Color(1, 1, 1))
	if int(game.king) == 0 and not bool(game.revealed):
		_draw_king_marks(r)
		if bool(game.faked):
			_text(Vector2(r.end.x + 70, r.get_center().y + 26), "바꿔치기 준비됨", 13, Color(1, 0.8, 0.4))
	if not bool(game.revealed):
		_text(Vector2(r.end.x + 70, r.get_center().y + 4), "← 내 카드", 13, Color(1, 1, 1, 0.6))


func _draw_king_marks(r: Rect2) -> void:
	if bool(game.covered):
		var c := r.get_center()
		draw_circle(c, 20.0, Color(0.7, 0.1, 0.1))
		draw_arc(c, 15.0, 0.0, TAU, 24, Color(1, 1, 1, 0.9), 3.0)
		draw_circle(c, 9.0, Color(0.85, 0.15, 0.15))
	if bool(game.randomized):
		_text(Vector2(r.get_center().x, r.position.y - 8), "섞음", 13, Color(1, 0.9, 0.5))


## 물건 — 반사경이 있든 없든 겉모양은 같음 (내 것엔 작은 표시)
func _draw_object(c: Vector2, kind: String, mine: bool, looking: bool, sc: float) -> void:
	var look := str(CheatRules.OBJECTS[kind]["look"])
	var tr := Transform2D(0.0, Vector2(sc, sc), 0.0, c)
	draw_set_transform_matrix(tr)
	if look == "lighter":
		draw_rect(Rect2(-17, -10, 34, 48), Color(0.72, 0.72, 0.75))
		draw_rect(Rect2(-17, -10, 34, 48), Color(0.3, 0.3, 0.32), false, 2.0)
		draw_colored_polygon(PackedVector2Array([Vector2(-17, -10), Vector2(17, -10), Vector2(13, -40), Vector2(-21, -40)]), Color(0.8, 0.8, 0.84))
		draw_rect(Rect2(-13, -36, 22, 22), Color(0.75, 0.88, 1.0, 0.6))
	elif look == "cigcase":
		draw_rect(Rect2(-26, -6, 52, 40), Color(0.75, 0.68, 0.40))
		draw_rect(Rect2(-26, -6, 52, 40), Color(0.35, 0.3, 0.15), false, 2.0)
		draw_rect(Rect2(-22, -2, 44, 10), Color(0.9, 0.85, 0.6, 0.7))
	elif look == "glass":
		draw_colored_polygon(PackedVector2Array([Vector2(-22, -30), Vector2(22, -30), Vector2(17, 34), Vector2(-17, 34)]), Color(0.75, 0.85, 0.95, 0.25))
		draw_rect(Rect2(-17, 6, 34, 26), Color(0.6, 0.35, 0.1, 0.6))
	else:
		draw_rect(Rect2(-18, -30, 36, 64), Color(0.08, 0.08, 0.1))
		draw_rect(Rect2(-15, -26, 30, 54), Color(0.15, 0.2, 0.3))
	draw_set_transform_matrix(Transform2D.IDENTITY)
	if mine:
		_text(c + Vector2(0, 54 * sc), "반사경" if CheatRules.is_mirror(kind) else "빈 것", 13, Color(1, 1, 1, 0.55))
	if looking:
		draw_arc(c + Vector2(0, -5), 58.0 * sc, 0.0, TAU, 40, Color(1, 0.9, 0.3, 0.6), 3.0)


## 머묾 게이지 — 시선이 머무는 동안 고리가 참 (떼면 처음부터)
func _gauge(c: Vector2, k: float) -> void:
	if k < 0.0:
		return
	var col := C_MARK if k < 1.0 else Color(1.0, 0.35, 0.25)
	draw_arc(c, 56.0, 0.0, TAU, 48, Color(0, 0, 0, 0.55), 9.0)
	draw_arc(c, 56.0, -PI / 2.0, -PI / 2.0 + TAU * clampf(k, 0.0, 1.0), 48, col, 9.0)


## '!' — 시선이 다 머문 물건 (이번 턴 동안)
func _mark(c: Vector2) -> void:
	var p := c + Vector2(0, -86 + sin(clock * 6.0) * 3.0)
	draw_circle(p, 22.0, C_MARK)
	draw_arc(p, 22.0, 0.0, TAU, 32, Color(0.35, 0.18, 0.0), 3.0)
	_text(p + Vector2(0, 11), "!", 32, Color(0.25, 0.08, 0.0))


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


## 상대 눈동자 — 보는 곳 쪽으로 (0.4초에 걸쳐)
func _look_vec(target: String) -> Vector2:
	if target == "face" or target == "hands" or target == "":
		return Vector2(0, 1.5)
	var to: Vector2 = T_LOOK.get(target, Vector2(640, 900))
	if target.begins_with("obj"):
		var idx := int(target.substr(3))
		if idx >= 0 and idx < 3:
			to = T_OBJ[idx]
	var d: Vector2 = (to - HEAD).normalized()
	return Vector2(d.x * 7.0, d.y * 5.5)


func _pupil_offset() -> Vector2:
	var k := clampf((float(game.t) - float(game.gaze_since[1])) / CheatRules.TURN_TIME, 0.0, 1.0)
	return _look_vec(str(game.gaze_prev[1])).lerp(_look_vec(str(game.gaze[1])), k)


func _glow(c: Vector2, r: float, col: Color) -> void:
	for i in 6:
		var k := 1.0 - float(i) / 6.0
		draw_circle(c, r * k, Color(col.r, col.g, col.b, col.a * 0.2))


func _text(center_baseline: Vector2, s: String, font_size: int, col: Color) -> void:
	var font: Font = ThemeDB.fallback_font
	var w := 520.0
	draw_string_outline(font, Vector2(center_baseline.x - w / 2.0, center_baseline.y), s, HORIZONTAL_ALIGNMENT_CENTER, w, font_size, 4, Color(0, 0, 0, 0.8))
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
