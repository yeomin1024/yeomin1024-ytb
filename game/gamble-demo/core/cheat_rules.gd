# VERSION: v0.1.0 — 2026-11-26 — 속임수 정의표 · 단서 공식 · 알아챌 확률 · 이항 확률
#
# 속임수 한 번 = 선택 → 실행(손기술 QTE 0~1) → 단서(상대가 그 순간 볼 수 있는 신호) + 증거(남는 물건)
#              → 상대가 고발하면 '고발 시점에 증거가 남아 있는지'로만 판정
extends RefCounted

## 데이터만 바꿔 튜닝 (나중에 .tres 리소스로 옮길 자리)
## evidence_turns: 지금 턴 + N 턴까지 증거가 남음 · -1 = 매치 끝까지
## fake = true 는 '가짜 동작'(블러핑) — 단서만 있고 증거·효과 없음 → 고발하면 늘 헛고발
const CHEATS := {
	"peek": {"name": "엿보기", "base_tell": 0.45, "evidence_turns": 1, "uses": 3, "fake": false},
	"mark": {"name": "뒷면 표시", "base_tell": 0.55, "evidence_turns": -1, "uses": 1, "fake": false},
	"fake": {"name": "가짜 동작", "base_tell": 0.50, "evidence_turns": 0, "uses": 3, "fake": true},
}

const QTE_REDUCTION := 0.6    # 손기술 1.0 이면 단서 60% 줄어듦
const WATCHED_MULT := 1.5     # 상대가 내 손을 보고 있을 때
const UNWATCHED_MULT := 0.5   # 상대가 얼굴을 보고 있을 때
const REPEAT_STEP := 0.25     # 이번 매치에 같은 트릭을 쓴 횟수마다 +25%
const MARKED_MULT := 1.3      # 경고 1개(낙인) 상태
const NOTICE_K := 2.0         # 알아챌 확률 = 1 − exp(−K × 단서 × 주의력)
const TOKENS_PER_MATCH := 3   # 고발 토큰
const FALSE_ACCUSE_FINE := 1  # 헛고발 벌금 (점수, 상대에게 줌)
const CAUGHT_FINE := 1        # 들켰을 때 벌금 (판 몰수와 별도, 고발한 쪽에게) — 시뮬레이션으로 넣음 (CHANGELOG)
const MARK_READ_CHANCE := 0.6 # 뒷면 표시가 그 턴에 보일 확률 — 표시는 다음 턴부터
const STRIKES_TO_LOSE := 2    # 경고 2개 = 즉시 패배
const EVIDENCE_FOREVER := 1 << 30


static func compute_tell(base_tell: float, qte: float, watched: bool, prior_uses: int, strikes: int) -> float:
	var q := clampf(qte, 0.0, 1.0)
	var tell := base_tell * (1.0 - QTE_REDUCTION * q)
	tell *= WATCHED_MULT if watched else UNWATCHED_MULT
	tell *= 1.0 + REPEAT_STEP * prior_uses
	if strikes >= 1:
		tell *= MARKED_MULT
	return clampf(tell, 0.0, 1.0)


static func notice_probability(tell: float, perception: float) -> float:
	return 1.0 - exp(-NOTICE_K * tell * maxf(perception, 0.0))


static func evidence_expiry(cheat_id: String, global_turn: int) -> int:
	var turns: int = CHEATS[cheat_id]["evidence_turns"]
	if turns < 0:
		return EVIDENCE_FOREVER
	return global_turn + turns


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
