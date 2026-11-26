# VERSION: v0.4.0 — 2026-11-26 — 뒤돌아보기 시선 · 라이터 놓기·카드 덮개·블러핑 결정 · 준비 동작을 보면 의심
# 이전 VERSION: v0.3.0 — 2026-11-26 — 엿보기는 노예(암살자) 측일 때만
#
# 공정성 규칙: 상대 카드는 엿보기(반사경)를 끝냈을 때만 info["opp_card"] 로 들어온다 (match.gd 가 넣음).
#   AI 가 보는 것 = 공개 정보뿐 (사람의 시선 = 마우스 위치, 테이블 위 물건, 판 결과).
# p0_* 함수는 시뮬레이션에서 사람 자리(0)를 대신하는 정책 — 사람 플레이에는 쓰지 않음.
extends RefCounted

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")

const PRIOR_LOGODDS := -1.7      # 처음 의심 ≈ 15%
const SUSPICION_MIN := -4.0
const SUSPICION_MAX := 6.0
const CHEATER_MIX := 0.5
const WATCH_FACE_BASE := 0.35    # 지켜볼 때 당신 얼굴을 볼 기본 확률

var display_name := "AI"
var cheat_rate := 0.3            # 노예 판에 라이터를 놓을 확률 · 감시 턴에 엿볼 확률
var skill := 0.6                 # 엿보는 속도: 필요 시간 = PEEK_SECONDS × (1.15 − 0.5 × skill)
var perception := 1.0            # 눈치: 들킬 위험률 배수 · 반응 속도
var paranoia := 1.0              # 의심 성향
var boldness := 0.1              # 쳐다보는 걸 알면서도 반사경을 보는 정도
var bluff_rate := 0.3            # 엿볼 때 블러핑(여유 부리기)을 쓸 확률
var cover_rate := 0.3            # 왕 측일 때 자기 카드에 덮개를 올릴 정도
var suspicion := PRIOR_LOGODDS
var force_watch := ""            # 시험용: 지켜보는 곳을 고정 ("" = 보통)


## 성격 묶음. 모르는 이름이면 정직형 + 경고.
func configure(kind: String) -> void:
	display_name = kind
	match kind:
		"honest":
			_apply(0.0, 0.6, 1.0, 1.0, 0.0, 0.3, 0.3)
		"cheater":
			_apply(0.6, 0.75, 0.8, 0.8, 0.35, 0.5, 0.2)
		"watcher":
			_apply(0.25, 0.5, 1.4, 1.3, 0.05, 0.2, 0.5)
		"gambler":
			_apply(0.45, 0.6, 1.0, 1.0, 0.6, 0.7, 0.3)
		"inert":
			_apply(0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0)   # 시험용: 아무것도 안 함
		_:
			push_warning("[AI] unknown preset=%s → honest" % kind)
			_apply(0.0, 0.6, 1.0, 1.0, 0.0, 0.3, 0.3)


func _apply(p_cheat: float, p_skill: float, p_perception: float, p_paranoia: float, p_bold: float, p_bluff: float, p_cover: float) -> void:
	cheat_rate = p_cheat
	skill = p_skill
	perception = p_perception
	paranoia = p_paranoia
	boldness = p_bold
	bluff_rate = p_bluff
	cover_rate = p_cover


# ───────── 지켜보기 (속임수 턴: 사람이 반사경·협력자를 볼 수 있음) ─────────

## 다음 시선 묶음 {target, dur}. 의심이 클수록·상대가 낙인이면 얼굴을, 뒤에 누가 오는 기척이 있으면 뒤를 더 봄.
func watch_segment(rng: RandomNumberGenerator, opp_strikes: int, someone_behind: bool) -> Dictionary:
	if force_watch != "":
		return {"target": force_watch, "dur": 99.0}
	var extra := maxf(suspicion - PRIOR_LOGODDS, 0.0)
	var bonus := 0.2 if opp_strikes >= 1 else 0.0
	var p_face := clampf(WATCH_FACE_BASE + 0.12 * extra * paranoia + bonus, 0.1, 0.85)
	var p_behind := 0.05
	if someone_behind:
		p_behind = clampf(0.2 + 0.05 * extra, 0.0, 0.45)
	var w_behind := (1.0 - p_face) * p_behind
	var r := rng.randf()
	var target := "away"
	if r < p_face:
		target = "face"
	elif r < p_face + w_behind:
		target = "behind"
	else:
		var rest := (r - p_face - w_behind) / maxf(1.0 - p_face - w_behind, 0.001)
		if rest < 0.4:
			target = "hands"
		elif rest < 0.65:
			target = "own_card"
	var dur := 0.0
	if target == "face":
		dur = rng.randf_range(0.6, 1.6)
	elif target == "behind":
		dur = rng.randf_range(0.5, 1.2)
	else:
		dur = rng.randf_range(0.7, 2.2)
	dur /= clampf(0.6 + 0.4 * perception, 0.5, 1.5)
	return {"target": target, "dur": dur}


## 할 일 없을 때 (사람이 카드를 고르는 중 · 엿보기를 안 하거나 끝냈을 때)
func idle_segment(rng: RandomNumberGenerator) -> Dictionary:
	var r := rng.randf()
	var target := "face"
	if r >= 0.4:
		target = "own_card" if r < 0.75 else "away"
	return {"target": target, "dur": rng.randf_range(0.6, 1.8)}


## 준비 동작(라이터·협력자 부르기·뒤의 낯선 사람)을 봤을 때 의심이 오름. 돌려주는 값 = 더한 양.
func on_setup_seen(kind: String) -> float:
	var delta := float(CheatRules.SETUP_SUSPICION.get(kind, 0.0)) * maxf(paranoia, 0.3)
	suspicion = clampf(suspicion + delta, SUSPICION_MIN, SUSPICION_MAX)
	return delta


## 왕 측일 때 자기 카드에 덮개를 올릴지 (상대 라이터가 보이면 크게)
func decide_cover(rng: RandomNumberGenerator, opp_lighter: bool, uses_left: int) -> bool:
	if uses_left <= 0:
		return false
	var p := cover_rate * 0.3
	if opp_lighter:
		p += cover_rate
	p += 0.1 * maxf(suspicion - PRIOR_LOGODDS, 0.0) * paranoia
	return rng.randf() < clampf(p, 0.0, 0.9)


# ───────── 엿보기 (감시 턴: AI 가 노예 측일 때 반사경을 몰래 봄) ─────────

## 노예 판을 시작할 때 라이터를 놓을지 (준비 동작 — 사람에게 보임)
func decide_lighter(rng: RandomNumberGenerator, my_strikes: int) -> bool:
	var rate := cheat_rate
	if my_strikes >= 1:
		rate *= 0.3
	return rng.randf() < rate


func decide_peek(rng: RandomNumberGenerator, my_side: int, my_strikes: int) -> bool:
	var rate := cheat_rate
	if my_strikes >= 1:
		rate *= 0.3    # 한 번 더 걸리면 매치 패배
	if my_side != RankCards.Team.ASSASSIN_SIDE:
		return false   # 속임수는 노예 측만
	return rng.randf() < rate


func decide_bluff(rng: RandomNumberGenerator) -> bool:
	return rng.randf() < bluff_rate


func peek_need_seconds() -> float:
	return CheatRules.PEEK_SECONDS * clampf(1.15 - 0.5 * skill, 0.6, 1.4)


func think_seconds(rng: RandomNumberGenerator) -> float:
	return rng.randf_range(5.0, 7.0)


## 반사경을 보다가 사람이 자기 얼굴을 보면 이만큼 뒤에 눈을 돌림
func reaction_seconds() -> float:
	return 0.35 / clampf(perception, 0.3, 2.0)


## 감시 턴 시선 묶음: 반사경을 짧게 보고 → 사람 얼굴 확인 → 다시 반사경 …
func cheat_segment(rng: RandomNumberGenerator, opp_watching_face: bool, peek_done: bool, will_peek: bool, current: String) -> Dictionary:
	if not will_peek or peek_done:
		return idle_segment(rng)
	if current == "shiner":
		return {"target": "face", "dur": rng.randf_range(0.35, 0.7)}
	if not opp_watching_face or rng.randf() < boldness:
		return {"target": "shiner", "dur": rng.randf_range(0.6, 1.1) * (1.2 - 0.4 * skill)}
	var target := "face" if rng.randf() < 0.6 else "own_card"
	return {"target": target, "dur": rng.randf_range(0.3, 0.6)}


# ───────── 카드 ─────────

## info: {} (정보 없음) 또는 {"opp_card": 카드} (엿보기를 끝냈을 때)
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


## 판 결과(공개 정보)로 의심을 고침 — 상대가 노예 측이었던 판에서만 부름 (match.gd)
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


# ───────── 시뮬레이션용 사람 자리(0) 정책 ─────────

func p0_reaction(watching_face: bool) -> float:
	var base := 0.25 if watching_face else 0.4
	return base / clampf(perception, 0.3, 2.0)


func p0_watch_segment(rng: RandomNumberGenerator) -> Dictionary:
	var p_face := clampf(0.45 + 0.3 * perception, 0.3, 0.95)
	var target := "face" if rng.randf() < p_face else "own_card"
	return {"target": target, "dur": rng.randf_range(0.5, 1.5)}


func p0_commit_delay(rng: RandomNumberGenerator) -> float:
	return rng.randf_range(0.8, 2.0)
