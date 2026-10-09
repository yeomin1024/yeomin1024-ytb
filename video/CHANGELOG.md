# video/ 변경 이력 (guides/video_guide.md 2번 규칙)

## 2026-10-09 — multagi-2026-10 (첫 영상) · 공통 프로젝트 v1.0
- 프로젝트 생성: Remotion 4.0.534, React 18.3.1, TypeScript 5.6.3, 1920×1080 30fps
- 공통 `src/design/`: `tokens.ts`(색·크기·모션 상수, video_guide 3-1~3-4), `fonts.ts`(로컬 한글 폰트 로드 + delayRender)
- 공통 `src/components/`
  - `timeline.ts`: 자막 번호 → 프레임, 고지 카드만큼 뒤 자막 밀기, 장면 시간 `a(n, frac)`
  - `anim.ts`: spring 등장, 진행, 카운트, 흔들림 / `fmt.ts`: "8,000만 원", "8억 2,700만"
  - `ui.tsx`: 장면 틀(점 질감·1.00→1.03 줌·찢어진 종이 와이프), 글자, 형광펜(네이비에서도 읽히는 2겹 방식), 칩, 화살표, ✓/✗, 취소선, 카드, 개념도 캡션
  - `cards.tsx`: 계좌 카드(간단형 포함), 금액 막대, 뉴스 카드, 생각 말풍선, 번호 타이틀, 메모 카드
  - `charts.tsx`: 꺾은선(stroke-dashoffset), 점·라벨, 기준 점선, 세로 막대 비교, 연도 타임라인
  - `objects.tsx`: 누르는 버튼, 천칭 저울·무게 블록, 스마트폰·스위치, 체크리스트, 쌓이는 블록
  - `overlays.tsx`: 자막(띠 유지 + 글자 4프레임 페이드), 재구성 사연 캡션, 노랑 띠 고지 카드
- `scripts/get-fonts.mjs`(폰트 받기), `scripts/storyboard.mjs`(scene_plan.md + still + index.html)
- 영상 `src/episodes/multagi-2026-10/`: subtitles.ts(자막 91개·카드 1개), facts.ts, plan.ts(31장면), scenes/(story·host·problems·methods), Episode.tsx
- 스토리보드 검수 뒤 고친 장면: S04(라벨 간격), S05(S03의 흐린 손익에서 이어지게), S06(금액이 카드 밖으로 넘침), S13(막대가 머리글과 붙음), S14("이유?"가 선을 가림), S16(라벨 겹침 → 376달러 아래, 평단 라벨 선 끝 위), S24(개념도 캡션 유지), S25(큰 숫자와 질문 카드 겹침), S29(라벨이 선과 겹침)
- 버튼 색: 빨강은 수익 색이라 노랑(그 화면의 강조 한 곳)으로
- 렌더: `stock/out/multagi-2026-10/final_1080p.mp4` — 15,285프레임, 8분 29.5초, 71.9MB, 857초 (4코어). 스토리보드 still 44장은 약 43초
