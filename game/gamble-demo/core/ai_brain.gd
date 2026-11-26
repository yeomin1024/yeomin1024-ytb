# VERSION: v0.1.0 — 2026-11-26 — AI 성격값 · 시선 · 카드 선택 · 속임수 결정 · 의심(로그 오즈) 갱신 · 고발 결정
#
# 공정성 규칙: 이 파일의 어떤 함수도 상대의 숨은 카드를 받지 않는다.
#   상대 카드는 엿보기·뒷면 표시를 했을 때만 info["opp_card"] 로 들어온다 (match.gd 가 넣음).
#   의심은 공개 정보만으로 고친다 — 알아챈 단서, 판 결과, 상대 시선.
extends RefCounted

const RankCards = preload("res://core/rank_cards.gd")
const CheatRules = preload("res://core/cheat_rules.gd")

const PRIOR_LOGODDS := -1.7      # 처음 의심 ≈ 15%
const SUSPICION_MIN := -4.0
const SUSPICION_MAX := 6.0
const CHEATER_MIX := 0.5         # '속이는 사람'도 절반은 정직하게 둔다고 보고 가능도 비를 셈
const GAZE_HANDS_BASE := 0.45    # 손을 볼 기본 확률 (v0.1.0 튜닝: 0.35 → 0.45)
const ACCUSE_THRESHOLD_BASE := 0.0  # 고발 문턱 기본값 = 의심 50% (v0.1.0 튜닝: 1.0 → 0.0)

var display_name := "AI"
var cheat_rate := 0.3            # 속임수 빈도 (기본 시도 확률)
var skill := 0.6                 # 손기술 평균 (QTE 품질)
var perception := 1.0            # 주의력 (단서를 알아채는 정도)
var paranoia := 1.0              # 의심 성향 (결과 가중·고발 문턱)
var bluff_rate := 0.15           # 가짜 동작 빈도

var suspicion := PRIOR_LOGODDS   # '상대가 속이고 있다'의 로그 오즈
var tell_weight := 1.0           # 헛고발 뒤엔 단서를 덜 믿음


## 성격 묶음. 모르는 이름이면 정직형 + 경고.
func configure(kind: String) -> void:
	display_name = kind
	match kind:
		"honest":
			_apply(0.0, 0.6, 1.0, 1.0, 0.0)
		"cheater":
			_apply(0.45, 0.75, 0.9, 0.8, 0.1)
		"watcher":
			_apply(0.1, 0.5, 1.5, 1.3, 0.05)
		"bluffer":
			_apply(0.2, 0.6, 1.0, 1.0, 0.5)
		"inert":
			_apply(0.0, 0.5, 0.0, 0.0, 0.0)   # 시험용: 속이지도, 알아채지도, 고발하지도 않음
		_:
			push_warning("[AI] unknown preset=%s → honest" % kind)
			_apply(0.0, 0.6, 1.0, 1.0, 0.0)


func _apply(p_cheat: float, p_skill: float, p_perception: float, p_paranoia: float, p_bluff: float) -> void:
	cheat_rate = p_cheat
	skill = p_skill
	perception = p_perception
	paranoia = p_paranoia
	bluff_rate = p_bluff


## 이번 턴에 볼 곳: "hands"(상대 손) 또는 "face"(상대 얼굴). 의심이 클수록, 상대가 낙인이면 손을 봄.
func pick_gaze(rng: RandomNumberGenerator, opp_strikes: int) -> String:
	var p := GAZE_HANDS_BASE + 0.15 * maxf(suspicion - PRIOR_LOGODDS, 0.0) * paranoia
	if opp_strikes >= 1:
		p += 0.25
	p = clampf(p, 0.1, 0.9)
	return "hands" if rng.randf() < p else "face"


## info: {} (정보 없음) 또는 {"opp_card": 카드} (엿보기·뒷면 표시로 안 것)
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


## 상대 카드를 알 때 가장 좋은 답
static func best_response(hand: Array, side: int, opp_card: int) -> int:
	var citizen: int = RankCards.Card.CITIZEN
	var special := RankCards.special_of(side)
	var want: int
	if side == RankCards.Side.KING_SIDE:
		# 상대가 암살자면 시민으로 잡고, 시민이면 왕으로 이김
		want = citizen if opp_card == RankCards.Card.ASSASSIN else special
	else:
		# 상대가 왕이면 암살자, 시민이면 시민으로 비김 (암살자를 내면 짐)
		want = special if opp_card == RankCards.Card.KING else citizen
	if hand.has(want):
		return want
	return special if hand.has(special) else citizen


## 속임수를 쓸지. allowed = 이 자리에서 쓸 수 있는 id, left = 남은 횟수.
## 돌려주는 값: "" (안 씀) 또는 속임수 id
## 데모용 휴리스틱: 성격 빈도 × (상대가 내 손을 보면 0.4) × (내가 낙인이면 0.25) × (암살자 측이면 1.3)
func decide_cheat(rng: RandomNumberGenerator, allowed: Array, left: Dictionary, my_side: int, my_strikes: int, opp_watching_hands: bool, already_marked: bool) -> String:
	var rate := cheat_rate
	if opp_watching_hands:
		rate *= 0.4
	if my_strikes >= 1:
		rate *= 0.25   # 한 번 더 걸리면 매치 패배
	if my_side == RankCards.Side.ASSASSIN_SIDE:
		rate *= 1.3    # 걸린 점수(4)가 큼
	var roll := rng.randf()
	if not already_marked:
		if allowed.has("mark") and int(left.get("mark", 0)) > 0 and roll < rate * 0.5:
			return "mark"
		if allowed.has("peek") and int(left.get("peek", 0)) > 0 and roll < rate:
			return "peek"
	var roll2 := rng.randf()
	var bluff := bluff_rate * (1.0 if my_strikes == 0 else 0.5)
	if allowed.has("fake") and int(left.get("fake", 0)) > 0 and roll2 < bluff:
		return "fake"
	return ""


func qte_quality(rng: RandomNumberGenerator) -> float:
	return clampf(rng.randfn(skill, 0.15), 0.0, 1.0)


## 상대 단서가 나왔을 때. 알아챘으면 true 이고 의심이 오름 (강한 단서일수록 크게).
func on_tell(rng: RandomNumberGenerator, tell: float) -> bool:
	var p := CheatRules.notice_probability(tell, perception)
	var noticed := rng.randf() < p
	if noticed:
		suspicion = clampf(suspicion + tell_weight * log(1.0 + 4.0 * tell), SUSPICION_MIN, SUSPICION_MAX)
	return noticed


## 판이 끝났을 때 결과(공개 정보)만 보고 의심을 고침. 돌려주는 값 = 이번에 더한 양.
## 가능도 비 = P(결과 | 가끔 다 아는 사람) / P(결과 | 공정하게 둔 사람)
##           = CHEATER_MIX × P_다_앎 / P_공정 + (1 − CHEATER_MIX)
func on_round_result(opp_won: bool, opp_side: int, decided_turn: int) -> float:
	var lr := 1.0 - CHEATER_MIX   # 다 아는 사람은 지지 않음 → 상대가 지면 의심이 줄어듦
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


## 고발 문턱(로그 오즈). 의심 성향이 크면 낮고, 토큰이 적으면 높음(신중).
func accuse_threshold(tokens_left: int) -> float:
	return ACCUSE_THRESHOLD_BASE - 0.6 * (paranoia - 1.0) + 0.5 * (CheatRules.TOKENS_PER_MATCH - tokens_left)


func should_accuse(tokens_left: int) -> bool:
	return tokens_left > 0 and suspicion > accuse_threshold(tokens_left)


func on_accuse_result(hit: bool) -> void:
	if hit:
		suspicion = PRIOR_LOGODDS
	else:
		suspicion = clampf(suspicion - 1.5, SUSPICION_MIN, SUSPICION_MAX)
		tell_weight *= 0.8   # 본 단서가 가짜였던 셈 — 상대 버릇을 배움
