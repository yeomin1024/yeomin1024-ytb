# VERSION: v0.3.0 — 2026-11-26 — 엿보기는 노예(암살자) 측일 때만 (decide_peek 의 진영 배수 뺌 — 늘 노예 측이라)
# 이전 VERSION: v0.2.0 — 2026-11-26 — 시선 AI: 속임수 턴엔 당신을 지켜보고(얼굴·손·자기 카드·딴 곳), 감시 턴엔 잔을 몰래 봄
#
# 공정성 규칙: 상대 카드는 잔 엿보기를 끝냈을 때만 info["opp_card"] 로 들어온다 (match.gd 가 넣음).
#   AI 가 보는 것 = 공개 정보뿐 (사람의 시선 = 마우스가 가리키는 곳, 판 결과).
# p0_* 함수는 시뮬레이션에서 사람 자리(0)를 대신하는 정책 — 사람 플레이에는 쓰지 않음.
extends RefCounted

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")

const PRIOR_LOGODDS := -1.7      # 처음 의심 ≈ 15%
const SUSPICION_MIN := -4.0
const SUSPICION_MAX := 6.0
const CHEATER_MIX := 0.5         # '속이는 사람'도 절반은 정직하게 둔다고 보고 가능도 비를 셈
const WATCH_FACE_BASE := 0.35    # 지켜볼 때 당신 얼굴을 볼 기본 확률

var display_name := "AI"
var cheat_rate := 0.3            # 감시 턴에 잔을 엿볼 확률
var skill := 0.6                 # 엿보는 속도: 필요 시간 = PEEK_SECONDS × (1.15 − 0.5 × skill)
var perception := 1.0            # 눈치: 들킬 위험률 배수 · 반응 속도
var paranoia := 1.0              # 의심 성향: 판 결과가 수상하면 얼굴을 더 자주 봄
var boldness := 0.1              # 쳐다보는 걸 알면서도 잔을 보는 정도
var suspicion := PRIOR_LOGODDS   # '상대가 속이고 있다'의 로그 오즈
var force_watch := ""            # 시험용: 지켜보는 곳을 고정 ("" = 보통)


## 성격 묶음. 모르는 이름이면 정직형 + 경고.
func configure(kind: String) -> void:
	display_name = kind
	match kind:
		"honest":
			_apply(0.0, 0.6, 1.0, 1.0, 0.0)
		"cheater":
			_apply(0.6, 0.75, 0.8, 0.8, 0.35)
		"watcher":
			_apply(0.25, 0.5, 1.4, 1.3, 0.05)
		"gambler":
			_apply(0.45, 0.6, 1.0, 1.0, 0.6)
		"inert":
			_apply(0.0, 0.5, 0.0, 0.0, 0.0)   # 시험용: 엿보지도, 알아채지도 않음
		_:
			push_warning("[AI] unknown preset=%s → honest" % kind)
			_apply(0.0, 0.6, 1.0, 1.0, 0.0)


func _apply(p_cheat: float, p_skill: float, p_perception: float, p_paranoia: float, p_bold: float) -> void:
	cheat_rate = p_cheat
	skill = p_skill
	perception = p_perception
	paranoia = p_paranoia
	boldness = p_bold


# ───────── 지켜보기 (속임수 턴: 사람이 잔을 볼 수 있음) ─────────

## 다음 시선 묶음 {target, dur}. 의심이 클수록·상대가 낙인(경고 1)이면 얼굴을 더 봄. 눈치가 빠르면 자주 바꿈.
func watch_segment(rng: RandomNumberGenerator, opp_strikes: int) -> Dictionary:
	if force_watch != "":
		return {"target": force_watch, "dur": 99.0}
	var bonus := 0.2 if opp_strikes >= 1 else 0.0
	var p_face := clampf(WATCH_FACE_BASE + 0.12 * maxf(suspicion - PRIOR_LOGODDS, 0.0) * paranoia + bonus, 0.1, 0.85)
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


## 할 일 없을 때 (사람이 카드를 고르는 중 · 엿보기를 안 하거나 끝냈을 때)
func idle_segment(rng: RandomNumberGenerator) -> Dictionary:
	var r := rng.randf()
	var target := "face"
	if r >= 0.4:
		target = "own_card" if r < 0.75 else "away"
	return {"target": target, "dur": rng.randf_range(0.6, 1.8)}


# ───────── 엿보기 (감시 턴: AI 가 잔을 몰래 봄) ─────────

func decide_peek(rng: RandomNumberGenerator, my_side: int, my_strikes: int) -> bool:
	var rate := cheat_rate
	if my_strikes >= 1:
		rate *= 0.3    # 한 번 더 걸리면 매치 패배
	if my_side != RankCards.Team.ASSASSIN_SIDE:
		return false   # v0.3.0: 속임수는 노예 측만
	return rng.randf() < rate


func peek_need_seconds() -> float:
	return CheatRules.PEEK_SECONDS * clampf(1.15 - 0.5 * skill, 0.6, 1.4)


func think_seconds(rng: RandomNumberGenerator) -> float:
	return rng.randf_range(5.0, 7.0)


## 잔을 보다가 사람이 자기 얼굴을 보면 이만큼 뒤에 눈을 돌림
func reaction_seconds() -> float:
	return 0.35 / clampf(perception, 0.3, 2.0)


## 감시 턴 시선 묶음: 잔을 짧게 보고 → 사람 얼굴을 확인 → 다시 잔 … (사람이 얼굴을 보면 대담한 만큼만 잔으로)
func cheat_segment(rng: RandomNumberGenerator, opp_watching_face: bool, peek_done: bool, will_peek: bool, current: String) -> Dictionary:
	if not will_peek or peek_done:
		return idle_segment(rng)
	if current == "glass":
		return {"target": "face", "dur": rng.randf_range(0.35, 0.7)}
	if not opp_watching_face or rng.randf() < boldness:
		return {"target": "glass", "dur": rng.randf_range(0.6, 1.1) * (1.2 - 0.4 * skill)}
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
	# 정보가 없으면 특수 카드를 '남은 장 수 분의 1' 확률로 — 무작위 순서와 같은 분포
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


## 판이 끝났을 때 결과(공개 정보)로 의심을 고침 — 의심이 크면 다음 속임수 턴에 얼굴을 더 봄.
## 가능도 비 = CHEATER_MIX × P(결과 | 다 앎) / P(결과 | 공정) + (1 − CHEATER_MIX)  (v0.2.0: 근사 — 엿보기는 속임수 턴에만 가능)
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

## 상대 시선이 바뀐 걸 알아채는 데 걸리는 시간 (얼굴을 보고 있으면 빠르고, 잔을 보면 곁눈이라 느림)
func p0_reaction(watching_face: bool) -> float:
	var base := 0.25 if watching_face else 0.4
	return base / clampf(perception, 0.3, 2.0)


func p0_watch_segment(rng: RandomNumberGenerator) -> Dictionary:
	var p_face := clampf(0.45 + 0.3 * perception, 0.3, 0.95)
	var target := "face" if rng.randf() < p_face else "own_card"
	return {"target": target, "dur": rng.randf_range(0.5, 1.5)}


func p0_commit_delay(rng: RandomNumberGenerator) -> float:
	return rng.randf_range(0.8, 2.0)
