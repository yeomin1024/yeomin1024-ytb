# Gamble Mind (웹판) — Godot 데모 v0.8.0 을 브라우저로

VERSION: v0.8.0-web.1 — 2026-11-27 (Godot `game/gamble-demo/` v0.8.0 규칙·화면을 HTML·자바스크립트로 그대로 옮김)

> 연구·교육용 데모입니다. 실제 돈·현금화·유료 칩과 관계없습니다.
> 사용자 지시 (2026-11-27): "일단 웹 게임 기반으로 똑같이 만들어볼 수 있어? 그럼 이 환경에서 실행해볼 수 있잖아" — Godot 는 이 클라우드 환경에서 받을 수 없지만 브라우저(Chromium)는 있어서, 웹판은 여기서 직접 눌러 보며 확인할 수 있음.

## 1. 해 보기
- **바로 하기 (claude.ai 페이지)**: https://claude.ai/artifact/Hw9MGAT1zeDYszi9d55ZD3 — 고치면 `Artifact` 로 같은 주소에 다시 올림 (`index.html` + `core.js` · `game.js`)
- `index.html` 을 브라우저로 열면 끝 (설치 없음, 인터넷이 없으면 글꼴만 기본 글꼴로).
- 규칙·조작·화면은 Godot 판과 같음 → `game/gamble-demo/README.md` 1번 (턴 30초 · 내 테이블/상대 테이블 · 상대 시선 불빛 · 게이지 → '!' · 협력자 = 2.5초 누르고 있기 + 이어폰 · 물건 클릭 = 물건 확인 · 상대 클릭 = 몸 수색 · 성공하면 그 턴 무효 · 경고 2개 = 패배).
- 단축키는 키 자리(`e.code`)로 받아서 한글 입력 상태여도 1·2·3·F·C·R·X·Q·W·H·Enter 가 먹음. 2 는 누르고 있기.
- 휴대폰: 화면이 통째로 줄어듦 (가로 스크롤 없음). 터치한 자리 = 시선. PC 마우스 권장.

## 2. 확인 (이 환경에서 돌림)
```bash
node game/gamble-web/tests/core.test.js
```
```bash
node game/gamble-web/tools/sim.js 1000
```
```bash
node game/gamble-web/tests/e2e.js /tmp/shots
```
- `core.test.js`: Godot `tests/run_tests.gd` 와 같은 20묶음 (56개 확인) — 규칙만, 화면 없이.
- `sim.js`: AI 대 AI 밸런스 (Godot `tools/simulate.gd` 와 같은 조합).
- `e2e.js`: Playwright Chromium 으로 페이지를 열어 **사람처럼 눌러** 한 매치를 끝까지 (준비 → 왕 카드 고르기 → 상대 테이블 지켜보기 → '!' 물건 확인 → 판단 → 결과 → 협력자 부르기(버튼 누르고 있기) → 반사경 엿보기(게이지·'!') → … → 매치 끝) · 페이지 오류 0 · 폰 너비 가로 스크롤 없음 · 화면 12장 저장. 시험 때만 4배속(`window.__gm.setSpeed`).

## 3. 구조
```
index.html   화면 뼈대 (점수판 · 지금 할 일 · 설정 · 의심 표시 · 행동 버튼 · 알림 · 결과/준비/규칙 창) + 스타일
core.js      규칙 — Godot core/{rank_cards,cheat_rules,ai_brain,match}.gd 를 이름·순서 그대로 (브라우저·Node 공용, window.GambleCore)
game.js      화면 — Godot scenes/{main,table_view}.gd 를 캔버스 + HTML 로 (window.__gm = 시험용 손잡이)
tests/       core.test.js (규칙) · e2e.js (브라우저)
tools/sim.js 밸런스
```
- 규칙을 바꿀 땐 **Godot `core/*.gd` 와 `core.js` 를 같이** 고치고 두 시험을 모두 돌림.
- 난수: 시드 고정 mulberry32 — 같은 시드면 같은 매치. Godot 와 난수 생성기가 달라 같은 시드라도 결과는 다름 (승률은 같은 범위).
- 로그: 브라우저 개발자 도구 콘솔에 `[STAGE] [t=…ms] key=value` (Godot 와 같은 단계 이름: MATCH·DEAL·TURN·PHASE·CALL·MARK·INFO·COMMIT·JUDGE·EXPOSE·VOID·REVEAL·ROUND). 수준은 `GambleCore.GameLog.level` (0 DEBUG ~ 3 ERROR).

## 4. 밸런스 (웹판 1,000 매치, 자리 0 → 1 승률 %)
| 조합 | 웹판 | Godot 판 (파이썬 사본) |
|---|---|---|
| 정직 → 정직 | 50.0 / 50.0 | 50.7 / 49.3 |
| 딜러 → 정직 | 55.7 / 44.3 | 53.8 / 46.2 |
| 정직 → 딜러 | 44.7 / 55.3 | 45.1 / 54.9 |
| 딜러 → 노인 | 43.2 / 56.8 | 41.2 / 58.8 |
| 노인 → 딜러 | 57.8 / 42.2 | 57.4 / 42.6 |
| 도박꾼 → 노인 | 49.5 / 50.5 | 45.8 / 54.2 |
| 딜러 ↔ 딜러 | 47.7 / 52.3 | 49.0 / 51.0 |

모든 조합 42.2~57.8% · 두 번 들켜 짐 ≤ 15% (난수 생성기만 달라 차이는 2~4%p).
