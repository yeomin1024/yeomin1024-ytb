# VERSION: v0.8.0 — 2026-11-26 — 턴 30초 · 제스처 없앰 · 협력자 = 원격 + 이어폰(부르기 = 수상한 행동 2.5초, 보고 있으면 가능성 ↑) · 밝혀내기 = 물건 확인 / 몸 수색 · 성공하면 그 턴 무효 · 모든 행동 횟수 제한
# 이전 VERSION: v0.6.0 — 2026-11-26 — 판단 시간 값: 노예가 낸 뒤 사람 왕 5초 · AI 왕 1.2초
# 이전 VERSION: v0.5.0 — 2026-11-26 — 물건(반사경·미끼) · 시선 고정 엿보기 1.5초·협력자 1.8초 · 가능성 불 · 시선 끌기 · 제스처 · 가리기·무작위·바꿔치기·밝혀내기 값
#
# 사용자 규칙 (2026-11-26, v0.8.0):
#   턴 30초 · 내가 고를 땐 내 테이블만, 상대가 고를 땐 상대 테이블만 + 상대 시선이 불빛으로 보임
#   시선이 물건에 머물면 게이지가 차고 다 차면 '!' (그 물건에 의심 표시)
#   제스처 없앰 · 협력자는 현장이 아닌 통신 도구(이어폰)로 정보를 줌
#   밝혀내기: 물건을 고르면 물건 확인(반사경이 있으면 적중), 상대를 고르면 몸 수색(이어폰이 있으면 적중)
#   협력자 부르기 = 수상한 행동을 일정 시간 · 상대가 보고 있으면 '협력자 가능성'이 오름
#   카드를 고르는 중엔 방어 행동(밝혀내기 등) 못 함 — 낸 뒤에만
#   밝혀내기 성공 → 그 턴 무효, 둘 다 다시 고름 (경고 +1 · 그 속임수 봉인은 그대로, 경고 2개 = 패배)
#   행동 횟수 제한은 Claude 가 밸런스를 보고 정함 (아래 *_PER_MATCH)
# 연구·교육용 데모 — 실제 돈과 관계없음.
extends RefCounted

const PEEK_FIX := 1.5              # 반사경 물건을 계속 봐야 하는 시간 (게이지가 다 차는 시간)
const TURN_SECONDS := 30.0         # 왕 턴·노예 턴 기본 시간
const MIN_TURN_SECONDS := 5.0      # 깎여도 남는 최소 차례 시간
const EXPOSE_CUT := 10.0           # 밝혀내기 성공: 노예가 다시 고르는 노예 턴 −10초
const EXPOSE_FAIL_CUT := 10.0      # 밝혀내기 실패: 왕의 다음 차례 −10초
const ATTENTION_SECONDS := 3.0     # 시선 끌기: 상대가 내 시선·행동을 못 보는 시간
const ATTENTION_PER_MATCH := 1     # 사용자 규칙 "한번만 가능"
const COVERS_PER_MATCH := 3        # 가리기 (낸 카드 위 칩 → 반사경 안 통함)
const RANDOMS_PER_MATCH := 2       # 섞기 (낸 카드를 안 보고 패와 섞음 → 엿보기·협력자 안 통함)
const FAKES_PER_MATCH := 2         # 바꿔치기 (엿본 쪽에 가짜를 보여 줌)
const PLACES_PER_MATCH := 2        # 게임 중 물건 놓기
const INSPECTS_PER_MATCH := 3      # 물건 확인
const SEARCHES_PER_MATCH := 2      # 몸 수색
const ACC_CALLS_PER_MATCH := 2     # 협력자 부르기 시도 (시작하면 1번 씀, 중간에 멈춰도)
const ACC_CALL_SECONDS := 2.5      # 수상한 행동(귀를 만지며 신호)을 이만큼 계속해야 연결
const ACC_INFO_DELAY := 3.0        # 연결된 협력자가 이어폰으로 상대 카드를 알려 주기까지 (노예 턴 안)
const ACC_SUSPECT_RATE := 0.4      # 상대가 보고 있을 때 초당 '협력자 가능성' 증가 (0~1, 2.5초면 100%) — 시뮬레이션으로 0.5→0.4
const OBJECT_SLOTS := 3
const TURN_TIME := 0.4             # 시선을 옮기는 시간 (이동 중엔 '주시'가 아님)
const STRIKES_TO_LOSE := 2
const JUDGE_SECONDS := 5.0         # 노예가 낸 뒤 사람 왕이 판단하는 시간
const AI_JUDGE_SECONDS := 1.2      # AI 왕의 판단 시간 (판단은 시작할 때 한 번)
const AI_DEFEND_DELAY := [0.4, 1.2]   # AI 왕이 낸 뒤 방어(가리기·섞기·바꿔치기)를 쓰기까지
## 물건 — mirror = 속에 반사경 (엿보기 가능 · 확인하면 들킴), 없으면 미끼. look = 겉모양 (반사경이 있든 없든 같음)
const OBJECTS := {
	"lighter": {"name": "라이터", "mirror": true, "look": "lighter"},
	"lighter_plain": {"name": "라이터", "mirror": false, "look": "lighter"},
	"cigcase": {"name": "담뱃갑", "mirror": true, "look": "cigcase"},
	"cigcase_plain": {"name": "담뱃갑", "mirror": false, "look": "cigcase"},
	"glass": {"name": "술잔", "mirror": false, "look": "glass"},
	"phone": {"name": "휴대폰", "mirror": false, "look": "phone"},
}
## AI 가 수상한 것을 봤을 때 오르는 의심 (로그 오즈)
const SUSPICION_ADD := {"object": 0.5, "call_seen": 0.4, "mark": 0.3}


static func is_mirror(kind: String) -> bool:
	return bool(OBJECTS.get(kind, {}).get("mirror", false))


## 이 시선이면 상대를 '주시' 중 (협력자 부르기·물건 놓기를 알아챔)
static func is_watching(target: String) -> bool:
	return target == "face" or target == "hands"
