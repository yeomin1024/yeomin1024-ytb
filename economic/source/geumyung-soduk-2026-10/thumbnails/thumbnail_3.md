# geumyung-soduk-2026-10 썸네일 3 — 실험안 ②: 사람 없이, 식탁 위 지폐 더미를 짓누르는 빨강 '건보료' 덩어리

버전: v1.0 — 2026-10-18 — 대본 geumyung-soduk-2026-10.txt v1.0 기준. `guides/thumbnail_guide.md` v3.14. 근거: `README.md`.

| 항목 | 값 |
|---|---|
| 역할 | 실험안 ② — 본안과 **사람 있음/없음만** 다름. 문구·색·'건보료' 낱말·부엌 빛은 본안과 같음 |
| 시험하는 가설 | 사람 없이 '건보료'가 돈을 짓누르는 장면만으로도 같은가 — 노후·연금·절세 묶음 사람 없음 18% vs 7%, 배당·건보료 묶음 성공 19개 중 사람 없음 2 + 손만 2 |
| 짝 제목 | titles.md R1 「은퇴 부부 배당·이자 한 사람이 받으면 건보료 월 26만 원 손해」 |
| 문구 | 본안과 같음 (`README.md` 2번) |
| 근거 (`README.md` 3번) | 사람 없음 18% vs 7% (노후·연금·절세) · 빨강 상자에 손해 낱말 (배당 묶음 S13·S14·S19) |
| 숫자 근거 | '건보료 월 26만 원' = A 부부 지역 보험료 267,739원 (문장 3·32~36) |
| 인물 | 없음 |
| 저장 경로 | `economic/source/geumyung-soduk-2026-10/thumbnails/thumbnail_3.png` |

## 화면 구성
- **위쪽 약 62%**:
  - 가운데~오른쪽: 늦은 오후 부엌 나무 식탁 위, 가지런히 묶은 지폐 더미 하나(초상·숫자 없는 일반 지폐). 위에서 무거운 빨강 덩어리(앞면에 '건보료' 큰 흰 평면 글자)가 내리눌러 더미가 찌그러지고 지폐 몇 장이 흩어짐.
  - 왼쪽 위: 굵은 빨강 화살표 2개가 덩어리를 아래로 누르는 방향.
  - 배경: 본안과 같은 따뜻한 늦은 오후 부엌(흐리게), 식탁 끝에 머그잔 2개(글자 없음 — 부부의 자리).
- **아래쪽 약 35%**: 아래에서 위로 옅어지는 검은 띠 위에 큰 글자 2줄, 왼쪽 정렬.
- 오른쪽 아래 구석(약 220×70)은 비운다.
- 지폐 더미는 **하나만** — 두 더미로 나누면 영상의 방법(나눠 받기)을 그림으로 말하게 됨 (피드백 5).

## 문구 (그대로 사용)
| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 건보료 | 흰 글자 on 빨강 덩어리 앞면 #FF2A2A |
| 하단 1줄 | 50·60대 배당·이자 한 사람이 받으면 | '50·60대' 흰색 · **'배당·이자 한 사람이 받으면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 건보료 월 26만 원 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size. No people.
Upper 62% of the frame:
- Center to right: on a wooden kitchen table in warm late-afternoon window light, one neat bundled stack of plain generic banknotes with no portraits and no numbers. A heavy solid bright red (#FF2A2A) block presses down on the stack from above, crushing it so the stack bends and a few loose plain bills scatter on the table. On the flat front face of the red block, the Korean word "건보료" is printed in huge flat heavy bold white letters (flat print, not carved or 3D letter shapes), facing the viewer and fully visible.
- Upper left: two thick bright red arrows pointing down onto the red block.
- Background: a cozy apartment kitchen softly blurred (sink, window), warm golden late-afternoon light; two plain mugs at the far end of the table with no text.
- Only ONE stack of money (do not split it into two piles).
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 배당·이자 한 사람이 받으면" — "50·60대" in white and "배당·이자 한 사람이 받으면" in bright yellow #FFD400, all with a thick black outline (keep both middle dots "·" — between 50 and 60, and between 배당 and 이자 — line 1 is the longer line: it may run to about 92% of the image width, but keep it at least 4% away from the right edge);
line 2 "건보료 월 26만 원 손해" — all in bright red #FF2A2A with a thick white outline.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the money and the red block in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and the red block inside the central 16:9 area, at least 8% away from the top and bottom edges.
No bank, brokerage or government logos, no app screens, no charts, no account books, no piggy banks, no real banknote designs.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집 프로그램으로)
```
YouTube thumbnail background, 16:9 landscape (1280x720), photorealistic, high contrast. No people.
Upper 62%: on a wooden kitchen table in warm late-afternoon light, one neat stack of plain generic banknotes (no portraits, no numbers) crushed from above by a heavy solid bright red block with an empty flat front face; a few loose plain bills scattered; two thick red arrows pointing down onto the block from the upper left. Background: softly blurred kitchen, golden window light, two plain mugs at the far end of the table. Only one stack of money.
Lower third: a dark band fading upward from the bottom edge, left empty for a two-line headline.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
- 글자 얹기: 빨강 덩어리 앞면에 '건보료'(흰색, 굵은 고딕) · 하단 2줄은 본안(`thumbnail_1.md`)과 같음

## 검수
- [ ] 글자가 한 글자도 틀리지 않았는가: 건보료 · 50·60대 배당·이자 한 사람이 받으면 · 건보료 월 26만 원 손해
- [ ] 색이 본안과 같은가
- [ ] 지폐에 초상·숫자 같은 무늬가 없는가 · 지폐 더미가 하나뿐인가 (두 더미 ✗)
- [ ] '건보료' 글자가 빨강 덩어리 앞면의 평면 글자인가 (입체 글자 ✗ — 획이 틀리기 쉬움)
- [ ] 가로 320px로 줄여도 2줄과 '건보료'가 읽히는가 · 오른쪽 아래 구석이 비어 있는가
- [ ] 로고·앱 화면·저금통·통장이 없는가

## 이미지 검수 (Claude — 지시사항 10번)

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
