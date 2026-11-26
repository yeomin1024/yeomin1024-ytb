# VERSION: v0.2.0 — 2026-11-26 — 속임수 = 잔 엿보기 하나 (잔을 본 시간이 쌓여야 카드가 비침) · 상대 시선별 들킬 위험률 · 벌칙 값
# 이전 VERSION: v0.1.0 — 2026-11-26 — 속임수 정의표 · 단서 공식 · 알아챌 확률 · 이항 확률 (뒷면 표시·가짜 동작은 v0.2.0 에서 뺌)
#
# 엿보기 모델
#   진행도 p (0~1): 잔을 보는 동안 dt / 필요 시간 만큼 오르고, 눈을 떼면 초당 PEEK_DECAY 만큼 내려감. p = 1 이면 카드가 비침.
#   들킴: 잔을 보는 동안 매 순간 '위험률 λ = HAZARD[상대 시선] × 상대 눈치' 로 알아챔 → dt 동안 알아챌 확률 = 1 − exp(−λ·dt)
#         상대가 고개를 돌리는 중(TURN_TIME)에는 λ = 0.
#   감시 턴 고발: 상대가 지금 잔을 보고 있거나, 잔에서 눈을 뗀 지 GRACE_SECONDS 안이면 적중.
extends RefCounted

const PEEK_SECONDS := 1.8          # 사람이 잔을 이만큼 보면 상대 카드가 비침
const PEEK_DECAY := 0.15           # 잔에서 눈을 떼면 진행도가 초당 이만큼 줄어듦
const TURN_SECONDS := 15.0         # 먼저 내는 사람이 고르는 시간 — 넘으면 남은 카드 중 아무거나
const GRACE_SECONDS := 0.6         # 상대가 잔에서 눈을 뗀 뒤에도 이만큼은 고발 적중
const TURN_TIME := 0.4             # 시선을 옮기는 시간 (이동 중엔 알아채지 못함) — 튜닝 0.3 → 0.4
## 내가 잔을 볼 때 상대가 어디를 보느냐에 따른 위험률 (초당)
const HAZARD := {"face": 2.0, "hands": 0.5, "own_card": 0.08, "away": 0.05}   # 튜닝: 얼굴 2.4 → 2.0 · 손 0.6 → 0.5
const TOKENS_PER_MATCH := 3        # 고발 토큰
const FALSE_ACCUSE_FINE := 1       # 헛고발 벌금 (점수, 상대에게)
const CAUGHT_FINE := 1             # 들킨 벌금 (판 몰수와 별도)
const STRIKES_TO_LOSE := 2         # 경고 2개 = 즉시 패배


static func peek_step(progress: float, looking: bool, dt: float, need_seconds: float) -> float:
	if looking:
		return minf(progress + dt / maxf(need_seconds, 0.01), 1.0)
	return maxf(progress - PEEK_DECAY * dt, 0.0)


static func hazard_rate(watch_target: String, turning: bool, perception: float) -> float:
	if turning:
		return 0.0
	return float(HAZARD.get(watch_target, 0.0)) * maxf(perception, 0.0)


static func notice_chance(rate: float, dt: float) -> float:
	return 1.0 - exp(-rate * dt)


## n 번 시도하고 한 번마다 걸릴 확률이 p 일 때 k 번 이상 걸릴 확률 (밸런스 계산용)
static func p_at_least(k: int, n: int, p: float) -> float:
	var total := 0.0
	for i in range(k, n + 1):
		total += _binom(n, i) * pow(p, i) * pow(1.0 - p, n - i)
	return total


static func _binom(n: int, r: int) -> float:
	var result := 1.0
	for i in r:
		result = result * float(n - i) / float(i + 1)
	return result
