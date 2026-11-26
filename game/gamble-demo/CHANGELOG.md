# CHANGELOG — Gamble Mind Demo

## v0.1.1 — 2026-11-26 — F5 실행 오류 고침 (v0.1.0 → v0.1.1)

사용자 보고: `Failed to load script "res://scenes/main.gd" with error "Parse error"`.

- **원인** `scenes/main.gd` `_refresh()` 속임수 버튼 줄: `var blocked := … (id == "mark" and …)` — `id` 가 타입 없는 값(Dictionary 키)이라 식 전체가 Variant 로 추론됨 → Godot 4 기본 설정에서 `INFERENCE_ON_VARIANT` 는 경고가 아니라 **오류**라 스크립트를 못 읽음.
- **고침** `cid: String`·`n_left: int`·`blocked: bool` 로 타입을 적음 (`scenes/main.gd` 386~390줄).
- 같은 꼴: `tools/simulate.gd` `_parse_args()` 의 `var kv := a.substr(2)…` → `arg: String`·`kv: PackedStringArray`.
- `rank_cards.gd` `enum Side` → `enum Team` (Godot 전역 enum `Side` 와 이름이 겹쳐 경고) — `RankCards.Side.*` 를 쓰던 `ai_brain.gd`·`match.gd`·`main.gd`·`run_tests.gd` 함께 바꿈 (39곳).
- 규칙·숫자는 그대로 (밸런스 결과 변화 없음).
- 확인: `gdparse` 8개 통과 · `:=` 로 비교·and·or 를 받는 줄 다시 찾음 → 남은 1곳(`ai_brain.gd` 113줄)은 타입이 정해진 값이라 문제없음. Godot 실행 확인은 여전히 PC 에서.

## v0.1.0 — 2026-11-26 — 첫 데모 (v0.0.0 → v0.1.0)

새로 만듦 (사용자 지시 "고닷으로 간단하게 테스트 데모 만들어봐"):

| 파일 | 내용 |
|---|---|
| `core/rank_cards.gd` | 계급 카드 규칙(왕·시민·암살자) · `p_fair_win_at` · `p_perfect_win_at` |
| `core/cheat_rules.gd` | 속임수 표(엿보기·뒷면 표시·가짜 동작) · `compute_tell` · `notice_probability` · `p_at_least` |
| `core/ai_brain.gd` | 성격 묶음(honest·cheater·watcher·bluffer·inert) · 시선 · 카드 선택 · 속임수 결정 · 의심 갱신 · 고발 |
| `core/match.gd` | 매치 흐름 · 고발 판정 · 경고 2개 패배 · 연장 · 이벤트 |
| `core/game_log.gd` | `[STAGE] [t=…ms] key=value` 로그 |
| `scenes/main.gd` | 화면 (손기술 막대 · 시선 토글 · 고발 · 리플레이) |
| `tests/run_tests.gd` · `tools/simulate.gd` | 시험 15묶음 · AI 대 AI 밸런스 |

### 튜닝 (첫 초안 → v0.1.0) — 시뮬레이션 근거
⚠️ **위험·벌칙 규칙을 바꾼 것** (설계 때 말한 규칙과 다름):
- **들켰을 때 벌금 1점 추가** (`CheatRules.CAUGHT_FINE`, `match.gd` `accuse()`): 설계는 '그 판 몰수 + 경고'만이었음. 벌금이 없으면 속임수형이 정직형을 80 대 20으로 이김(연장·문턱 바꾼 뒤 기준) → 벌금 1점이면 61 대 39. 2점이어도 거의 같아서 1점.
- **뒷면 표시는 다음 턴부터, 턴마다 60%만 보임** (`CheatRules.MARK_READ_CHANCE`, `match.gd` `_begin_turn()`): 100% 면 속임수 1회당 적발률이 0.47로 너무 높고(다 알고 두니 결과가 티 남), 0.6 이면 0.36 (설계 목표 0.25~0.35 근처).

그 밖:
- **동점이면 연장 최대 2판, 진영은 동전 던지기** (`match.gd` `EXTRA_ROUNDS`, `_begin_round()`): 정직 대 정직 무승부 40% → 0%. 처음엔 연장 판을 자리 0 왕 측으로 고정했더니 정직 대 정직이 62 대 38로 기울어서 동전으로 바꿈 → 49 대 51.
- **AI 고발 문턱 기본값 1.0 → 0.0** (`AiBrain.ACCUSE_THRESHOLD_BASE`): 문턱이 높으면 AI 가 거의 고발하지 않아 속임수가 공짜였음. 0.0 에서 정직 대 정직 헛고발은 자리마다 매치당 0.11번.
- **AI 가 손을 볼 기본 확률 0.35 → 0.45** (`AiBrain.GAZE_HANDS_BASE`).

### 확인한 것 / 못 한 것
- 문법: `gdtoolkit` 4.5 `gdparse` 로 `.gd` 8개 모두 통과 (`gdlint` 는 줄 길이·순서 스타일 경고만).
- 로직·밸런스: 같은 규칙을 한 줄씩 옮긴 **파이썬 사본**으로 시험 59개 통과 + 3,000 매치 시뮬레이션 (README 5번).
- **Godot 로 실제 실행은 못 함**: 이 클라우드 환경에서 GitHub 배포 파일 받기가 막혀 있고, 다른 경로(Docker 이미지)로 받는 것은 권한 검사에서 거절됨 → PC 에서 `run_tests.gd` 를 먼저 돌려 주세요.
