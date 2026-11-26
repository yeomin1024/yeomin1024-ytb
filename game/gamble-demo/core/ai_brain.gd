# VERSION: v0.8.0 — 2026-11-26 — 제스처 없앰 · 협력자 부르기(안 보일 때 시작, 보이면 대담함만큼 계속) · 왕: 낸 뒤 방어 · 판단 때 '!' 물건 확인·협력자 가능성으로 몸 수색
# 이전 VERSION: v0.5.0 — 2026-11-26 — 역할별 AI: 노예(물건 고정 엿보기·협력자·미끼·시선 끌기·제스처) / 왕(지켜보기·가리기·무작위·바꿔치기·밝혀내기)
# 이전 VERSION: v0.4.0 — 2026-11-26 — 뒤돌아보기 시선 · 라이터 놓기·카드 덮개·블러핑 결정 · 준비 동작을 보면 의심
#
# 공정성 규칙: 상대 카드는 엿보기·협력자로 '보인 카드'(바꿔치기면 가짜)를 info["opp_card"] 로만 받는다.
#   AI 가 아는 것 = 공개 정보뿐 (상대 시선·'!' 표시·협력자 가능성·책상 위 물건·판 결과). 물건 속 반사경 여부는 확인 전엔 모름.
# 시뮬레이션에선 자리 0 도 같은 AI 로 돌림 (사람 대신).
extends RefCounted

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")

const PRIOR_LOGODDS := -1.7
const SUSPICION_MIN := -4.0
const SUSPICION_MAX := 6.0
const CHEATER_MIX := 0.5
const WATCH_FACE_BASE := 0.35
const CAUTION := 0.15       # 경고 1개를 받은 뒤 속임수(엿보기·협력자) 확률 배수 — 시뮬레이션으로 정함

var display_name := "AI"
# 노예일 때
var cheat_rate := 0.3        # 이번 노예 턴에 반사경으로 엿볼 확률
var acc_rate := 0.2          # 왕 턴마다 협력자를 부르려 할 확률 (연결 안 됐을 때)
var bluff_rate := 0.2        # 미끼 물건을 1.5초 넘게 봐서 '!' 를 띄울 확률
var attention_rate := 0.3    # 엿보기 직전에 시선 끌기를 쓸 확률
var boldness := 0.1          # 부르는 중 상대가 보면 그래도 계속할 확률
# 왕일 때
var cover_rate := 0.3
var random_rate := 0.1
var fake_rate := 0.2
var expose_rate := 0.5       # '!' 가 뜬 물건을 확인할 확률 (협력자 가능성이면 몸 수색에도 씀)
# 공통
var perception := 1.0        # 눈치: 보고 있을 때 협력자 가능성이 오르는 속도 배수 · 반응 속도
var paranoia := 1.0
var objects: Array = []      # 사전 설정 물건
var suspicion := PRIOR_LOGODDS
var force_watch := ""        # 시험용: 지켜보는 곳 고정


func configure(kind: String) -> void:
	display_name = kind
	match kind:
		"honest":
			_apply([0.0, 0.0, 0.0, 0.0, 0.0], [0.3, 0.1, 0.2, 0.5], 1.0, 1.0, ["glass"])
		"cheater":
			_apply([0.7, 0.4, 0.3, 0.5, 0.3], [0.2, 0.05, 0.2, 0.5], 0.8, 0.8, ["lighter", "lighter_plain"])
		"watcher":
			_apply([0.25, 0.1, 0.1, 0.3, 0.05], [0.5, 0.2, 0.3, 0.6], 1.4, 1.3, ["cigcase_plain", "cigcase"])
		"gambler":
			_apply([0.5, 0.3, 0.6, 0.5, 0.6], [0.3, 0.1, 0.4, 0.4], 1.0, 1.0, ["cigcase_plain", "cigcase", "glass"])
		"inert":
			_apply([0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], 0.0, 0.0, [])
		_:
			push_warning("[AI] unknown preset=%s → honest" % kind)
			_apply([0.0, 0.0, 0.0, 0.0, 0.0], [0.3, 0.1, 0.2, 0.5], 1.0, 1.0, ["glass"])


## slave = [cheat, acc, bluff, attention, boldness] · king = [cover, random, fake, expose]
func _apply(slave: Array, king: Array, p_perception: float, p_paranoia: float, p_objects: Array) -> void:
	cheat_rate = float(slave[0])
	acc_rate = float(slave[1])
	bluff_rate = float(slave[2])
	attention_rate = float(slave[3])
	boldness = float(slave[4])
	cover_rate = float(king[0])
	random_rate = float(king[1])
	fake_rate = float(king[2])
	expose_rate = float(king[3])
	perception = p_perception
	paranoia = p_paranoia
	objects = p_objects.duplicate()


func reaction() -> float:
	return 0.35 / clampf(perception, 0.3, 2.0)


func _extra() -> float:
	return maxf(suspicion - PRIOR_LOGODDS, 0.0)


# ───────── 시선 ─────────

## 고르는 쪽·한가할 때: 상대 얼굴 / 자기 카드 / 딴 곳
func idle_segment(rng: RandomNumberGenerator) -> Dictionary:
	var r := rng.randf()
	var target := "face"
	if r >= 0.4:
		target = "own_card" if r < 0.75 else "away"
	return {"target": target, "dur": rng.randf_range(0.6, 1.8)}


## 왕이 노예를 지켜볼 때: 의심이 클수록 얼굴·손을 봄
func watch_segment(rng: RandomNumberGenerator, opp_strikes: int) -> Dictionary:
	if force_watch != "":
		return {"target": force_watch, "dur": 99.0}
	var bonus := 0.2 if opp_strikes >= 1 else 0.0
	var p_face := clampf(WATCH_FACE_BASE + 0.12 * _extra() * paranoia + bonus, 0.1, 0.85)
	var r := rng.randf()
	var target := "away"
	if r < p_face:
		target = "face"
	else:
		var rest := (r - p_face) / maxf(1.0 - p_face, 0.001)
		if rest < 0.4:
			target = "hands"
		elif rest < 0.65:
			target = "own_card"
	var dur := rng.randf_range(0.6, 1.6) if target == "face" else rng.randf_range(0.7, 2.2)
	dur /= clampf(0.6 + 0.4 * perception, 0.5, 1.5)
	return {"target": target, "dur": dur}


# ───────── 왕 ─────────

func king_think(rng: RandomNumberGenerator) -> float:
	return rng.randf_range(2.0, 6.0)


## 낸 뒤에 쓸 방어 — 늘 난수 세 개를 씀 (재현성)
func king_defense(rng: RandomNumberGenerator, ctx: Dictionary) -> Dictionary:
	var threat: bool = int(ctx["opp_objects"]) > 0 or bool(ctx["opp_acc"])
	var ex := 0.1 * _extra() * paranoia
	var r1 := rng.randf()
	var r2 := rng.randf()
	var r3 := rng.randf()
	var use_random: bool = threat and int(ctx["random_left"]) > 0 and r1 < random_rate + ex * 0.5
	var use_cover: bool = not use_random and int(ctx["opp_objects"]) > 0 and int(ctx["cover_left"]) > 0 and r2 < cover_rate + ex
	var use_fake: bool = not use_random and threat and int(ctx["fake_left"]) > 0 and r3 < fake_rate + ex * 0.5
	return {"random": use_random, "cover": use_cover, "fake": use_fake}


## 판단 때 물건 확인 — '!' 물건 중 하나 (없으면 아주 의심될 때만 아무거나). 늘 난수 두 개를 씀
func decide_inspect(rng: RandomNumberGenerator, marked: Array, unchecked: Array) -> int:
	var r1 := rng.randf()
	var r2 := rng.randf()
	if not marked.is_empty():
		var p := clampf(expose_rate + 0.08 * _extra() * paranoia, 0.0, 0.95)
		if r1 < p:
			return int(marked[mini(int(r2 * marked.size()), marked.size() - 1)])
		return -1
	if unchecked.is_empty():
		return -1
	var p2 := clampf(0.04 * _extra() * paranoia, 0.0, 0.3)
	if r1 < p2:
		return int(unchecked[mini(int(r2 * unchecked.size()), unchecked.size() - 1)])
	return -1


## 판단 때 몸 수색 — 협력자 가능성(0~1)이 높을수록. 늘 난수 하나를 씀
func decide_search(rng: RandomNumberGenerator, acc_suspect: float) -> bool:
	var r := rng.randf()
	if acc_suspect <= 0.0:
		return r < clampf(0.02 * _extra() * paranoia, 0.0, 0.2)
	return r < clampf(acc_suspect * (0.4 + expose_rate) + 0.05 * _extra(), 0.0, 0.9)


func on_seen(kind: String) -> float:
	var delta := float(CheatRules.SUSPICION_ADD.get(kind, 0.0)) * maxf(paranoia, 0.3)
	suspicion = clampf(suspicion + delta, SUSPICION_MIN, SUSPICION_MAX)
	return delta


func on_expose_result(hit: bool) -> void:
	if hit:
		suspicion = PRIOR_LOGODDS
	else:
		suspicion = clampf(suspicion - 1.0, SUSPICION_MIN, SUSPICION_MAX)


# ───────── 노예 ─────────

func decide_call(rng: RandomNumberGenerator, strikes: int) -> bool:
	return rng.randf() < acc_rate * (CAUTION if strikes >= 1 else 1.0)


## 노예 턴 계획 — 늘 난수 네 개를 씀 (재현성)
func slave_plan(rng: RandomNumberGenerator, ctx: Dictionary) -> Dictionary:
	var objs: Array = ctx["objects"]
	var mirror_idx := -1
	var decoy_idx := -1
	for i in objs.size():
		var m := CheatRules.is_mirror(str(objs[i]))
		if m and mirror_idx < 0:
			mirror_idx = i
		if not m and decoy_idx < 0:
			decoy_idx = i
	var rate := cheat_rate * (CAUTION if int(ctx["strikes"]) >= 1 else 1.0)
	var can_peek: bool = mirror_idx >= 0 and not bool(ctx["sealed_peek"]) and not bool(ctx["covered"]) and not bool(ctx["randomized"])
	var plan := {"peek_obj": -1, "bait_obj": -1, "attention": false, "commit_at": 0.0}
	var r_peek := rng.randf()
	var r_bait := rng.randf()
	var r_att := rng.randf()
	if can_peek and r_peek < rate:
		plan["peek_obj"] = mirror_idx
	if decoy_idx >= 0 and r_bait < bluff_rate:
		plan["bait_obj"] = decoy_idx
	plan["attention"] = r_att < attention_rate and int(ctx["attention_left"]) > 0
	plan["commit_at"] = rng.randf_range(5.0, 12.0)
	return plan


# ───────── 카드 ─────────

## info: {} 또는 {"opp_card": 보인 카드}
func choose_card(rng: RandomNumberGenerator, hand: Array, side: int, info: Dictionary) -> int:
	if info.has("opp_card"):
		return best_response(hand, side, int(info["opp_card"]))
	var special := RankCards.special_of(side)
	if not hand.has(special):
		return RankCards.Card.CITIZEN
	if not hand.has(RankCards.Card.CITIZEN):
		return special
	return special if rng.randf() < 1.0 / hand.size() else RankCards.Card.CITIZEN


static func best_response(hand: Array, side: int, opp_card: int) -> int:
	var citizen: int = RankCards.Card.CITIZEN
	var special := RankCards.special_of(side)
	var want: int
	if side == RankCards.Team.KING_SIDE:
		want = citizen if opp_card == RankCards.Card.ASSASSIN else special
	else:
		want = special if opp_card == RankCards.Card.KING else citizen
	if hand.has(want):
		return want
	return special if hand.has(special) else citizen


## 판 결과(공개 정보)로 의심 — 상대가 노예 측이었던 판에서만 (match.gd)
func on_round_result(opp_won: bool, opp_side: int, decided_turn: int) -> float:
	var lr := 1.0 - CHEATER_MIX
	if opp_won:
		var p_fair := RankCards.p_fair_win_at(opp_side, decided_turn)
		var p_perfect := RankCards.p_perfect_win_at(opp_side, decided_turn)
		if p_fair > 0.0:
			lr = CHEATER_MIX * p_perfect / p_fair + (1.0 - CHEATER_MIX)
		else:
			lr = 1.0
	var delta := paranoia * log(lr)
	suspicion = clampf(suspicion + delta, SUSPICION_MIN, SUSPICION_MAX)
	return delta
