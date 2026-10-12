# stock 썸네일 만들 목록 (이미지 없는 것)

자동 생성 — `python tools/make_summary.py --thumb-todo stock` (2026-10-12 09:39)

1. [A] 프롬프트를 이미지 AI에 넣는다. 한글이 틀리면 [B]로 만들고 문구표대로 글자를 얹는다.
2. 이미지를 아래 '저장 위치'로 GitHub에 올린다 (크기는 업로드 때 1280×720으로 자동 변환).

남은 썸네일: 3개

## chugyeok-2026-10 · thumbnail_1 — 숫자 반전 (계좌 카드)

저장 위치: `stock/source/chugyeok-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 시작 숫자 | +380만 원 | 빨강 #E63B2E | 수익 금액 = 빨강 |
| 펀치 (위쪽) | 일주일 만에 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (노랑 상자는 이 1곳만) |
| 카드 결과 숫자 | -1,000만 원 | 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 나만 못 탈까 봐 샀다가 | 흰색 + 검정 외곽선 | — (13자) |
| 하단 2줄 | +380만원이 -1천만원 | 흰색 + 검정 외곽선 | "-1천만원"만 노랑 #FFD400 (13자, 2줄 합 26자) |

- 강조색 3곳: 빨강 "+380만 원"(카드, 수익), 노랑 형광펜 "일주일 만에", 노랑 글자 "-1천만원". 손실 숫자는 빨강으로 쓰지 않는다 (카드는 파랑 상자, 하단은 노랑).
- 하단 2줄은 T1 앞 문장("나만 못 탈까 봐 따라 산 급등주에서 번 380만원이 -1천만원이 됐습니다")을 줄인 것. 2줄 합 26자 안에 넣으려고 "따라 산 급등주에서 번"을 "샀다가"로 줄였다. "+"는 380만원이 손실이 아니라 수익이라는 걸 한눈에 보이게 붙였다 (값은 제목과 같음).
- 하단 2줄은 제목 표기("380만원", "-1천만원"), 카드는 영상 계좌 카드 표기("+380만 원", "-1,000만 원")다. 값은 같다 (`stock/guides/thumbnail_rules.md` 1번).

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos, no stock names). Inside the card, on the left: the text
"+380만 원" in large red (#E63B2E) bold letters. In the middle: a thick blue (#2D6CDF) arrow that goes up a little and then
plunges steeply down to the right, with the label "일주일 만에" in black bold letters over a bright yellow (#FFD400)
highlighter stripe just above the arrow. On the right: a solid blue (#2D6CDF) rounded box with the huge white bold text
"-1,000만 원", the largest element in the image. No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "나만 못 탈까 봐 샀다가", line 2 "+380만원이 -1천만원". The word "-1천만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. In the upper 60% of the frame, a wide
light-cream rounded rectangle card with a thin black outline. Inside: empty space on the left for a number, a thick blue
arrow in the middle that goes up a little and then plunges steeply down to the right, with a short bright yellow
highlighter stripe just above it, and an empty solid blue (#2D6CDF) rounded box on the right. No people. The lower third
is a dark navy (#14213D) band that fades upward from the bottom edge, with clean empty space for two lines of large text;
nothing else in the band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## chugyeok-2026-10 · thumbnail_2 — 인물·감정 장면

저장 위치: `stock/source/chugyeok-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 일곱 배에 샀다 | 흰색 #F7F3EA ("일곱 배"만 검정) | "일곱 배"에 노랑 상자 (글자 전체 높이, 노랑 상자는 이 1곳만) |
| 결과 숫자 (위쪽) | -1,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |
| 하단 1줄 | 말만 듣고 올라탄 주식 | 흰색 + 검정 외곽선 | — (12자) |
| 하단 2줄 | +380만원에서 -1천만원 | 흰색 + 검정 외곽선 | "+380만원" 빨강 #E63B2E(수익), "-1천만원" 노랑 #FFD400(손실) (14자, 2줄 합 26자) |

- 강조색 3곳: 노랑 상자 "일곱 배", 빨강 "+380만원"(수익), 노랑 "-1천만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (위쪽은 파랑 상자, 하단은 노랑).
- 하단 2줄은 T2 앞 문장("일곱 배 올랐다는 말만 듣고 올라탄 주식이 +380만원에서 -1천만원이 됐습니다")을 줄인 것. "일곱 배"는 펀치에 있어 하단에 다시 쓰지 않았다.
- 펀치 "일곱 배에 샀다"는 문장 2(공모가의 일곱 배가 넘은 값에 산 것, 0:06)와 문장 22("공모가 31달러의 일곱 배가 넘는 값")의 말이다.
- 하단 2줄은 제목 표기("+380만원", "-1천만원"), 위쪽 상자는 영상 계좌 카드 표기("-1,000만 원")다. 값은 같다.

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned room late at night, lit only by a small desk lamp. On the left 40% of the frame,
a fictional Korean office worker around 40 years old (plain shirt), sitting and holding a smartphone, the other hand
covering the mouth, frozen stunned and regretful expression, face lit by the phone's cold light. The face and the phone
are in the upper 60% of the frame; the lower body fades into darkness at the bottom. The phone screen shows only a simple
line that rises briefly in red and then turns blue and drops sharply, no app interface, no text. Fictional person, not
resembling any real or famous person, natural Korean features, realistic photo style. In the upper right area, large bold
text "일곱 배에 샀다" in off-white, where only the words "일곱 배" sit on a solid bright yellow (#FFD400) box with black
text. Below it, still in the upper 60%, a wide solid blue (#2D6CDF) rounded box with a thin white border containing the
huge white bold text "-1,000만 원", the largest element. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "말만 듣고 올라탄 주식", line 2 "+380만원에서 -1천만원". In line 2, "+380만원" is red #E63B2E and "-1천만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Realistic photo style. Dark navy-toned room late at night, lit only by a small desk lamp. On the left 40% of the frame, a
fictional Korean office worker around 40 years old, holding a smartphone, the other hand covering the mouth, stunned and
regretful expression, face lit by the phone's cold light; the phone screen shows only a simple line that rises briefly in
red and then turns blue and drops sharply. The face and the phone are in the upper 60% of the frame. Fictional person, not
resembling any real or famous person. In the upper right area, calm dark empty space for a short headline with a small
empty bright yellow box at its left, and below it an empty solid blue (#2D6CDF) rounded box with thin white border, both
in the upper 60%. The lower third is a dark band (black to dark navy) that fades upward from the bottom edge, with clean
empty space for two lines of large text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## chugyeok-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `stock/source/chugyeok-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 나만 못 탈까 봐 따라 산 | 흰색 #FFFFFF | — (14자) |
| 2줄 | 급등주에서 번 380만원이 | "380만원" 빨강 #E63B2E, 나머지 흰색 | 수익 금액 = 빨강 (14자) |
| 3줄 | -1천만원이 됐습니다 | "-1천만원" 노랑 #FFD400, 나머지 흰색 | 손실 금액 = 노랑, 빨강 금지 (11자) |

- 채택 제목 앞 문장 "나만 못 탈까 봐 따라 산 급등주에서 번 380만원이 -1천만원이 됐습니다."를 **글자 그대로** 3줄로 나눴다 (끝 마침표만 뺌). 뒤 문장(결말 장치 "추격매수한 사람들의 불편한 진실")은 넣지 않는다.
- 줄 길이(띄어쓰기 포함): 14자 · 14자 · 11자 — 모두 14자 이내, 어절 단위로 끊음
- 숫자 반전("380만원이 -1천만원이")은 2줄 끝 "380만원이" → 3줄 첫머리 "-1천만원이"로 바로 이어지게 나눴다 (몰빵 thumbnail_3과 같은 방식). 한 줄에 모으면 4줄이 되고 글자가 작아진다.
- 강조 2곳: 빨강 "380만원"(수익), 노랑 "-1천만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (`stock/guides/thumbnail_rules.md` 1번·2번).
- 행동 단어 "따라 산"은 흰색으로 둔다. 바로 아래 줄의 빨강(수익)과 붙어 빨강의 뜻(이 채널에서는 수익)이 섞이지 않게 하기 위해서다 — 같은 상황(수익 금액이 있는 제목)인 몰빵·빚투 thumbnail_3과 같은 선택.

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 3 lines with tight line spacing:
line 1 "나만 못 탈까 봐 따라 산", line 2 "급등주에서 번 380만원이", line 3 "-1천만원이 됐습니다".
All text pure white (#FFFFFF) except "-1천만원" at the start of line 3 in bright yellow (#FFD400) and "380만원" in line 2 in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
