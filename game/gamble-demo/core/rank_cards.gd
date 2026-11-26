# VERSION: v0.1.1 — 2026-11-26 — 전역 enum Side 와 겹치던 enum 이름을 Team 으로
# 이전 VERSION: v0.1.0 — 2026-11-26 — 계급 카드 규칙(왕·시민·암살자) + 공정 플레이 기준 확률
#
# 규칙: 왕 > 시민, 시민 > 암살자, 암살자 > 왕, 시민 = 시민(비김 → 다음 턴)
# 패: 왕 측 = 시민 4 + 왕, 암살자 측 = 시민 4 + 암살자. 늦어도 5턴에 승부가 남.
# (원작 이름·테마를 쓰지 않으려고 '노예' 대신 '암살자' — 최종 테마는 출시 전에 다시 정함)
extends RefCounted

enum Card { CITIZEN, KING, ASSASSIN }
enum Team { KING_SIDE, ASSASSIN_SIDE }

const HAND_SIZE := 5
const CITIZENS_PER_HAND := 4
const CARD_NAMES := {Card.CITIZEN: "시민", Card.KING: "왕", Card.ASSASSIN: "암살자"}
const SIDE_NAMES := {Team.KING_SIDE: "왕 측", Team.ASSASSIN_SIDE: "암살자 측"}
## 판 승리 점수 — 둘 다 무작위로 둬도 기대 점수가 같게: 왕 측 0.8 × 1 = 암살자 측 0.2 × 4
const WIN_POINTS := {Team.KING_SIDE: 1, Team.ASSASSIN_SIDE: 4}


static func special_of(side: int) -> int:
	return Card.KING if side == Team.KING_SIDE else Card.ASSASSIN


static func other_side(side: int) -> int:
	return Team.ASSASSIN_SIDE if side == Team.KING_SIDE else Team.KING_SIDE


static func new_hand(side: int) -> Array:
	var hand: Array = []
	for i in CITIZENS_PER_HAND:
		hand.append(Card.CITIZEN)
	hand.append(special_of(side))
	return hand


## a 가 이기면 1, b 가 이기면 -1, 비기면 0 (시민 대 시민)
static func resolve(a: int, b: int) -> int:
	if a == b:
		return 0
	if _beats(a, b):
		return 1
	return -1


static func _beats(x: int, y: int) -> bool:
	return (
		(x == Card.KING and y == Card.CITIZEN)
		or (x == Card.CITIZEN and y == Card.ASSASSIN)
		or (x == Card.ASSASSIN and y == Card.KING)
	)


## 두 사람 모두 정보 없이 무작위로 둘 때(특수 카드를 '남은 장 수 분의 1' 확률로),
## winner_side 진영이 turn 번째 턴(1~5)에 이길 확률.
##   왕이 k 턴, 암살자가 j 턴에 나온다고 하면 k, j 는 1~5 균등·독립.
##   암살자 측 승 = j == k  → 턴마다 1/25
##   왕 측 승     = 먼저 나온 특수 카드가 시민과 만남 → 2·(5 − t)/25
static func p_fair_win_at(winner_side: int, turn: int) -> float:
	if turn < 1 or turn > HAND_SIZE:
		return 0.0
	var n := float(HAND_SIZE)
	if winner_side == Team.ASSASSIN_SIDE:
		return 1.0 / (n * n)
	return 2.0 * (n - turn) / (n * n)


## 상대 카드를 늘 아는 사람(winner_side)이 공정한 상대에게 turn 번째 턴에 이길 확률
##   왕 측: 첫 턴에 늘 이김 (상대가 시민이면 왕, 암살자면 시민)
##   암살자 측: 상대 왕이 나오는 턴에 이김 → 턴마다 1/5
static func p_perfect_win_at(winner_side: int, turn: int) -> float:
	if turn < 1 or turn > HAND_SIZE:
		return 0.0
	if winner_side == Team.KING_SIDE:
		return 1.0 if turn == 1 else 0.0
	return 1.0 / HAND_SIZE
