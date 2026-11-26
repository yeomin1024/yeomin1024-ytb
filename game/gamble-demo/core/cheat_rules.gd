# VERSION: v0.4.0 — 2026-11-26 — 반사경(라이터 샤이너) 엿보기 + 협력자 신호 · 준비 동작 의심 · 카드 덮개 · 블러핑(시간) 값
# 이전 VERSION: v0.2.0 — 2026-11-26 — 속임수 = 잔 엿보기 하나 · 상대 시선별 들킬 위험률 · 벌칙 값
#
# 속임수 두 가지 (노예 측만, 준비 동작이 먼저):
#   반사경(샤이너): [준비] 라이터를 테이블에 놓음 → 라이터 뚜껑 안 작은 거울을 PEEK_SECONDS 보면 상대 카드가 비침.
#                   들킴 = 상대가 내 얼굴(눈)을 볼 때 크게 (HAZARD_SHINER).  상대가 카드에 덮개를 올리면 안 비침.
#   협력자 신호  : [준비] 협력자를 부름 → ACC_WALK_SECONDS 뒤 상대 뒤에 섬 → 손 신호를 SIGNAL_SECONDS 보면 상대 카드.
#                   들킴 = 상대가 뒤를 돌아볼 때 크게 (HAZARD_SIGNAL). 덮개로 못 막음. 들키면 그 매치에서 쫓겨남.
# 진행도 p (0~1): 보는 동안 dt / 필요 시간 만큼 오르고, 눈을 떼면 초당 PEEK_DECAY 만큼 내려감.
# 알아챌 확률 = 1 − exp(−위험률 × 상대 눈치 × dt), 상대가 시선을 옮기는 중(TURN_TIME)엔 0.
extends RefCounted

const PEEK_SECONDS := 1.8          # 반사경에 비친 카드를 읽는 시간
const SIGNAL_SECONDS := 1.2        # 협력자 손 신호를 읽는 시간
const PEEK_DECAY := 0.15           # 눈을 떼면 진행도가 초당 이만큼 줄어듦
const TURN_SECONDS := 15.0         # 먼저 내는 사람이 고르는 기본 시간
const MIN_TIME_LEFT := 1.5         # 블러핑으로 줄여도 남는 최소 시간
const GRACE_SECONDS := 0.6         # 상대가 반사경에서 눈을 뗀 뒤에도 이만큼은 고발 적중
const TURN_TIME := 0.4             # 시선을 옮기는 시간 (이동 중엔 알아채지 못함)
const ACC_WALK_SECONDS := 2.5      # 협력자가 상대 뒤로 걸어오는 시간
## 반사경을 볼 때 상대 시선별 위험률 (초당)
const HAZARD_SHINER := {"face": 2.0, "hands": 0.5, "own_card": 0.08, "away": 0.05, "behind": 0.05}
## 협력자 신호를 볼 때 — 상대 쪽을 보니 얼굴엔 덜 티 나지만, 뒤를 돌아보면 바로 들킴
const HAZARD_SIGNAL := {"face": 0.7, "hands": 0.25, "own_card": 0.05, "away": 0.05, "behind": 3.5}
## 준비 동작을 상대가 봤을 때 오르는 의심 (로그 오즈 · 경고는 아님)
const SETUP_SUSPICION := {"lighter": 0.8, "accomplice": 0.4, "stranger": 0.6}
const CHOOSE_BLUFF_SECONDS := 5.0  # 블러핑: 고르는 시간 ±5초
const THINK_BLUFF_SECONDS := 2.0   # 블러핑: 고민 시간 ±2초
const BLUFFS_PER_MATCH := 3
const COVERS_PER_MATCH := 2        # 카드 덮개 (칩 올려 두기)
const ACC_CALLS_PER_MATCH := 2     # 협력자 부르기
const TOKENS_PER_MATCH := 3        # 고발 토큰
const FALSE_ACCUSE_FINE := 1       # 헛고발 벌금 (점수, 상대에게)
const CAUGHT_FINE := 1             # 들킨 벌금 (판 몰수와 별도)
const STRIKES_TO_LOSE := 2         # 경고 2개 = 즉시 패배


static func peek_step(progress: float, looking: bool, dt: float, need_seconds: float) -> float:
	if looking:
		return minf(progress + dt / maxf(need_seconds, 0.01), 1.0)
	return maxf(progress - PEEK_DECAY * dt, 0.0)


static func hazard_rate(table: Dictionary, watch_target: String, turning: bool, perception: float) -> float:
	if turning:
		return 0.0
	return float(table.get(watch_target, 0.0)) * maxf(perception, 0.0)


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
