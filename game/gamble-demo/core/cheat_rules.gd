# VERSION: v0.5.0 — 2026-11-26 — 물건(반사경·미끼) · 시선 고정 엿보기 1.5초·협력자 1.8초 · 가능성 불 · 시선 끌기 · 제스처 · 가리기·무작위·바꿔치기·밝혀내기 값
# 이전 VERSION: v0.4.0 — 2026-11-26 — 반사경(라이터 샤이너) 엿보기 + 협력자 신호 · 준비 동작 의심 · 카드 덮개 · 블러핑(시간) 값
#
# 사용자 규칙 (2026-11-26):
#   물건: 사전 설정으로 책상 위에 놓을 수 있고, 게임 중에도 놓을 수 있다. 반사경이 든 물건 / 그냥 물건(미끼).
#   엿보기: 물건 속 반사경을 1.5초 '계속' 보면 카드 확인 (눈을 떼면 처음부터 — 쌓이는 게이지가 아님)
#   협력자: 상대 뒤에 사람이 옴 → 1.8초 '계속' 보면 카드 확인
#   가능성 불: 실제로 썼든 아니든, 시선이 그 시간 동안 고정되면 상대에게 불이 들어옴
#   시선 끌기: 한 번만 · 그동안 상대는 내 시선 움직임이나 제스처를 못 봄
#   제스처: 상대 턴 시간 깎임 (상대 턴이 10초 이상 남았을 때만)
#   가리기: 엿보기 안 통함 · 무작위: 엿보기·협력자 안 통함 · 바꿔치기: 속이는 상대에게 가짜를 보여 줌
#   밝혀내기: 성공 → 경고 1 + 그 속임수 봉인 + 상대 턴 시간 깎임 / 실패 → 내 (다음) 턴 시간 깎임
#   경고 2개 = 즉시 패배 (처음 규칙 유지)
#   공격 도구는 노예 측, 방어 도구는 왕 측 (진영별)
extends RefCounted

const PEEK_FIX := 1.5              # 반사경을 계속 봐야 하는 시간
const ACC_FIX := 1.8               # 협력자를 계속 봐야 하는 시간
const TRY_MARK := 0.5              # 진짜 장치를 이만큼 넘게 보면 '시도함' (밝혀내기 적중 근거)
const EXPOSE_LIVE := 0.3           # 지금 진짜 장치를 이만큼 넘게 보고 있어도 적중
const TURN_SECONDS := 15.0         # 왕 턴·노예 턴 기본 시간
const MIN_TIME_LEFT := 1.5         # 깎여도 남는 최소 시간
const GESTURE_MIN_LEFT := 10.0     # 제스처: 상대 턴이 이만큼 이상 남았을 때만
const GESTURE_CUT := 5.0           # 제스처: 상대 턴 −5초
const EXPOSE_CUT := 5.0            # 밝혀내기 성공: 상대(노예) 지금 턴 −5초
const EXPOSE_FAIL_CUT := 5.0       # 밝혀내기 실패: 내 다음 턴 −5초
const ATTENTION_SECONDS := 3.0     # 시선 끌기가 가리는 시간
const ATTENTION_PER_MATCH := 1
const COVERS_PER_MATCH := 3        # 가리기 (칩 덮개)
const RANDOMS_PER_MATCH := 2       # 무작위 (카드를 안 보고 무작위로 냄)
const FAKES_PER_MATCH := 2         # 바꿔치기 (가짜를 보여 줌)
const ACC_CALLS_PER_MATCH := 2
const ACC_WALK_SECONDS := 2.5
const OBJECT_SLOTS := 3
const TURN_TIME := 0.4             # 시선을 옮기는 시간 (이동 중엔 못 알아챔)
const STRIKES_TO_LOSE := 2
## 물건 — mirror = 속에 반사경이 있음 (엿보기 가능), 없으면 미끼. look = 겉모양 (반사경이 있든 없든 똑같이 보임)
const OBJECTS := {
	"lighter": {"name": "라이터", "mirror": true, "look": "lighter"},
	"lighter_plain": {"name": "라이터", "mirror": false, "look": "lighter"},
	"cigcase": {"name": "담뱃갑", "mirror": true, "look": "cigcase"},
	"cigcase_plain": {"name": "담뱃갑", "mirror": false, "look": "cigcase"},
	"glass": {"name": "술잔", "mirror": false, "look": "glass"},
	"phone": {"name": "휴대폰", "mirror": false, "look": "phone"},
}
## AI 왕이 '진행 중인' 고정을 보고 바로 밝혀낼 위험률 (초당, 왕의 시선별) — 진짜인지 미끼인지는 모름
const HAZARD_EXPOSE_OBJ := {"face": 1.6, "hands": 0.4, "own_card": 0.05, "away": 0.03, "behind": 0.03}
const HAZARD_EXPOSE_ACC := {"face": 0.6, "hands": 0.2, "own_card": 0.03, "away": 0.03, "behind": 2.5}
## 준비 동작·불을 봤을 때 오르는 의심 (로그 오즈)
const SUSPICION_ADD := {"object": 0.5, "accomplice": 0.4, "stranger": 0.6, "light": 0.4}


static func is_mirror(kind: String) -> bool:
	return bool(OBJECTS.get(kind, {}).get("mirror", false))


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
