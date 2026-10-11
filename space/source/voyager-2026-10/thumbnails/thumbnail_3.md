# voyager-2026-10 썸네일 3 — 대비 (끝났다는 쇼츠 / 지금도 신호)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `space/guides/thumbnail_rules.md` v1.0), 대본 v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 쇼츠가 준 인상('끝났다')과 실제 기록('지금도 신호', 11월 18일)을 좌우로 맞세운 대비가 가장 클릭을 부른다 |
| 짝 제목 | `titles.md` **T3 (짧은 변형)** "다섯 달 만에 살아난 보이저 1호. 끝났다던 영상이 틀린 진짜 이유" — T1과도 어울림 |
| 숫자 근거 | 문장 1 "보이저 1호가 끝났다는 1분짜리 쇼츠를 봤어요" (0:00) · 문장 8 "그 탐사선은 지금도 신호를 보내며 2026년 11월 18일 빛으로 하루 거리에 닿는대요" (0:47~0:55) → 1분 안 |

## 화면 구성
- 화면을 세로로 반씩 나눔
- 왼쪽 절반 (빨강 쪽): 빨강 테두리 안에 세로로 긴 단순한 휴대폰 화면 하나 — 짧은 영상 화면처럼 어둡고, 가운데에 큰 **"끝났다"** (흰 글자 + 빨강 상자). 앱 이름·버튼·로고·채널 이름 없음
- 오른쪽 절반 (파랑 쪽): 다크 네이비 우주, 안테나 접시가 달린 작은 탐사선 일러스트(로고 없음)에서 왼쪽으로 가는 가는 신호선. 그 아래 파랑 상자 **"지금도 신호"** (흰 글자, 가장 큰 글자 덩어리), 그 아래 작게 **"11월 18일"** (흰 글자)
- 가운데 경계선에 노랑 화살표 하나 (왼쪽 → 오른쪽)
- 오른쪽 아래 구석(약 220×70px)은 비움 · 인물 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 (쇼츠 인상) | 끝났다 | 흰색 (빨강 #E63B2E 상자) | — |
| 오른쪽 (실제 기록) | 지금도 신호 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |
| 오른쪽 아래 | 11월 18일 | 흰색 (네이비 위) | — |
| (그림) | 가운데 화살표 | 노랑 #FFD400 | 유일한 노랑 강조 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact blue #2D6CDF, wrong-information red #E63B2E, cream #F2EBDD.
Bottom-right corner kept empty (video length badge).
Clean flat illustrated style (clearly an illustration, not a photo). The frame is split vertically into two halves.
Left half: a red-tinted panel with a thick red (#E63B2E) border containing one simple tall smartphone screen that looks
like a dark generic short-video screen, with no app name, no buttons, no logos, no channel name; in its center the big
white bold text "끝났다" on a solid red box. Right half: dark navy (#14213D) deep space with a few faint stars and a small
generic space probe illustration with a dish antenna (intact, no logos, no letters, no flags) sending a thin glowing
dotted signal line toward the left; below it a wide solid blue (#2D6CDF) rounded box with the large white bold text
"지금도 신호", the largest text block, and under that box the smaller white bold text "11월 18일". On the dividing line
in the center, one bright yellow (#FFD400) arrow pointing from left to right. Keep all text inside the central 16:9 safe
area. Minimal, nothing decorative, no people.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, highlight yellow #FFD400, fact blue #2D6CDF, wrong-information red #E63B2E.
Clean flat illustrated style, not a photo. Frame split vertically in two halves. Left half: red-tinted panel with a thick
red border and one simple dark tall smartphone screen with an empty solid red box in its center, no app name, no buttons,
no logos. Right half: dark navy space with a few faint stars and a small generic probe with a dish antenna sending a thin
glowing dotted line to the left, an empty wide solid blue rounded box below it and empty space under the box for a short
date. One bright yellow arrow on the center dividing line pointing left to right. No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "끝났다" · "지금도 신호" · "11월 18일"이 한 글자도 틀리지 않음 (문장 1·8과 같은 말·날짜)
- [ ] 휴대폰 화면이 실제 앱(쇼츠·릴스 등)처럼 보이지 않음 — 앱 이름·버튼 배치·로고·채널 이름 없음
- [ ] 탐사선에 로고·글자·국기 없음 · 실제 사진처럼 보이지 않음
- [ ] 320px 축소본에서 "끝났다"와 "지금도 신호"가 바로 읽힘 · 노랑 강조 1곳 · 빨강 = 틀린 인상, 파랑 = 실제 기록
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
