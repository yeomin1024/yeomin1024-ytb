# video/ 변경 이력 (guides/video_guide.md 2번 규칙)

## 2026-10-10 — 최신 사례로 장면 교체 (multagi-2026-10 · panicsell-2026-10), 스토리보드 삭제
- 사용자 지시 "사례는 되도록 최신, 1900년도는 너무 옛날"에 맞춰 대본이 바뀐 장면만 다시 만듦 (문장 수 그대로, subtitles.ts 다시 내보냄)
- `panicsell-2026-10` (자막 111): S28·S29 탈러 1997 실험 → 자본시장연구원 2021 (2020년 개인투자자 20만 명 카드, 거래 빈도 막대 "두 배 가까이"(비율만, 숫자 표시 없음), 수수료·세금 뺀 수익률 기존 +15% / 신규 -1.2%, "자주 사고팔수록 시장보다 덜 벎 · 기존·신규 각각"(인과 화살표 없음), 문장 85 휴대폰 4개 "팔까?·살까?"). `facts.ts` 구분에 "출처" 추가, `local.tsx` `MiniPhone`
- `multagi-2026-10` (자막 107): S17(40–43)·S18(44–45) 오딘 1998 → 자본시장연구원 2022 (산 다음 날 판 비율 41% vs 22%·78% 보유, 들고 있던 종목 -9.8% vs +4.9%), S20·S21 베어링스 1995 → 카카오 2021~2026 실제 주가 흐름 선(날짜 간격은 실제와 다름 표시), 개인 순매수 막대 1조·2조 원, 소액주주 206만 명, 2026년 10월 3만 2천 원대. 문제 03 장면 경계를 40–42/43–45 → 40–43/44–45로
- 검수: 바뀐 문장마다 still(뒷줄 자막 3프레임 전 포함)과 앞뒤 장면을 video_guide 7번 검수표로 확인, `tsc --noEmit` 통과
- 스토리보드 삭제 (사용자 지시): `stock/out/*/storyboard/`·`scene_plan.md` 지움. `scripts/storyboard.mjs`는 저장소 밖 임시 폴더에 점검용 still을 렌더할 때만 쓴다

## 2026-10-10 — bittu-2026-10 · panicsell-2026-10 (새 영상 2개) · 공통 v1.2
- 새 영상 `src/episodes/bittu-2026-10/` (빚투·반대매매): 30장면, 문장 88 / 자막 105, 8:20.2. `local.tsx`에 빚 계좌 카드(내 돈·빌린 돈), 담보 막대(140% 선), 날짜 칸 등. 스토리보드 51장
- 새 영상 `src/episodes/panicsell-2026-10/` (하락장 패닉셀): 31장면, 문장 92 / 자막 109, 8:21. `local.tsx`에 계좌 카드, 10×10 와플, 공포 게이지(개념도), 달력 등. 스토리보드 53장. 검수 뒤 S05 하락 구간 선을 회색 → 파랑(하락 색)으로
- `Root.tsx`: 두 컴포지션 등록
- `components/ui.tsx` `Strike`: 그어지기 전(p = 0)에 12px 조각이 먼저 보이던 버그 수정
- `components/charts.tsx` `Bars`: 바닥선이 막대보다 먼저 보이던 것 → 첫 막대와 함께 등장
- `scripts/storyboard.mjs` v1.1: 재구성 사연 캡션 범위를 `plan.ts`의 `STORY_LAST`로 (물타기 14, 새 영상 16)
- `scripts/align-audio.mjs` v1.1: '-숫자'로 시작하는 대본 줄을 파트 라벨로 보지 않음 (`tools/srt_tool.py` v1.4와 같은 규칙)
- 검수: 두 영상 모든 still을 video_guide 7번 검수표로 확인, 나뉜 문장(각 17개)의 뒷줄 요소가 뒷줄 자막 3프레임 전에 보이지 않음 확인, `tsc --noEmit` 통과(물타기 포함)

## 2026-10-10 — 공통 v1.1 · multagi-2026-10 (사용자 지시: 문장 번호·자막 한 줄·고지 공백·align-audio)
- `components/timeline.ts`: SRT 번호 → **대본 문장 번호** 기준. 문장마다 앞줄·뒷줄(parts), `t.b(n)` = 뒷줄 자막 시작. 고지 카드를 코드에서 밀던 계산 삭제 → SRT 안의 공백(cards.start~end)에 카드
- `components/overlays.tsx`: 자막 늘 한 줄 (띠 좌우 여백 34px → 글자 폭 1432px)
- `scripts/align-audio.mjs` (신규, `npm run align-audio`): ffmpeg 쉼 찾기 + 동적 계획법으로 SRT를 내레이션에 맞춤 (오디오는 고치지 않음, 고지 공백 3.5초 확인, 옛 SRT 백업, check·내보내기까지). 가짜 내레이션 시험: 문장 시작 오차 평균 0.002초·최대 0.10초(91문장 2회), 뒷줄 시작 오차 평균 0.09~0.12초, 카드 쉼이 짧으면 멈춤
- `scripts/storyboard.mjs`: 문장 번호 기준 표기, `npm run storyboard`
- `episodes/multagi-2026-10/Episode.tsx`: 내레이션이 있으면 `Html5Audio`로 넣음 (subtitles.ts의 audio)
- multagi-2026-10 뒷줄 내용 동기화: 문장 2·11·20·28·32·33·41·51·52·54·68·72·79·81·82·84·86·87·88의 뒷줄 내용 요소를 `b(n)`으로 옮김. 문장 84 앞줄의 "관세 충격"이 문장 83에 먼저 나오던 것도 고침. 뒷줄 자막 시작 3프레임 전 still로 확인(문장 32·79·87)

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
