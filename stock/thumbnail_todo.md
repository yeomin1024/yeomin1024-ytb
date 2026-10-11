# stock 썸네일 만들 목록 (이미지 없는 것)

자동 생성 — `python tools/make_summary.py --thumb-todo stock` (2026-10-11 08:41)

1. [A] 프롬프트를 이미지 AI에 넣는다. 한글이 틀리면 [B]로 만들고 문구표대로 글자를 얹는다.
2. 이미지를 아래 '저장 위치'로 GitHub에 올린다 (크기는 업로드 때 1280×720으로 자동 변환).

남은 썸네일: 12개

## bittu-2026-10 · thumbnail_1 — 숫자 반전 (계좌 카드)

저장 위치: `stock/source/bittu-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 시작 숫자 | +1,500만 원 | 빨강 #E63B2E (수익) | — |
| 카드 결과 숫자 | -2,500만 원 | 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 신용까지 써서 번 돈 | 흰색 + 검정 외곽선 | — (11자) |
| 하단 2줄 | 반대매매에 -2,500만원 | 흰색 + 검정 외곽선 | "반대매매"만 노랑 #FFD400 (14자, 2줄 합 25자) |

- 강조색은 2곳: 빨강 "+1,500만 원"(수익), 노랑 "반대매매". 손실 숫자는 빨강으로 쓰지 않는다 (카드는 파랑 상자, 하단은 흰색).
- 하단 2줄은 제목 표기("-2,500만원"), 카드는 영상 계좌 카드 표기("-2,500만 원")다. 값은 같다 (`stock/guides/thumbnail_rules.md` 1번).

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos). Inside the card, on the left: the text "+1,500만 원" in large
red (#E63B2E) bold letters. In the middle: a thick blue (#2D6CDF) arrow pointing right and slightly down. On the right: a
solid blue (#2D6CDF) rounded box with the huge white bold text "-2,500만 원", the largest element in the image.
No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "신용까지 써서 번 돈", line 2 "반대매매에 -2,500만원". The word "반대매매" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, loss blue #2D6CDF, gain red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. In the upper 60% of the frame, a wide
light-cream rounded rectangle card with a thin black outline. Inside: empty space on the left for a number, a thick blue
arrow pointing right and slightly down in the middle, and an empty solid blue (#2D6CDF) rounded box on the right.
No people. The lower third is a dark navy (#14213D) band that fades upward from the bottom edge, with clean empty space
for two lines of large text; nothing else in the band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## bittu-2026-10 · thumbnail_2 — 인물·감정 장면 (담보 부족 문자)

저장 위치: `stock/source/bittu-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 담보 부족 | 검정 #1E1E1E | 노랑 상자 #FFD400 (글자 전체 높이, 노랑 상자는 이 1곳만) |
| 결과 숫자 (위쪽) | -2,500만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |
| 하단 1줄 | 내 돈만 넣기 아까워 | 흰색 + 검정 외곽선 | — (11자) |
| 하단 2줄 | 빚 냈다가 -2,500만원 | 흰색 + 검정 외곽선 | "빚"만 노랑 #FFD400 (14자, 2줄 합 25자) |

- 강조색은 2곳: 노랑 상자 "담보 부족", 노랑 글자 "빚". 손실 숫자는 빨강으로 쓰지 않는다 (위쪽은 파랑 상자, 하단은 흰색).
- 펀치 "담보 부족"은 하단 2줄에 없는 말이다. 하단 2줄은 T2 앞 문장("내 돈만 넣기 아까워 빚까지 냈다가 … -2,500만원이 됐습니다")을 줄인 것.
- 하단 2줄은 제목 표기("-2,500만원"), 위쪽 상자는 영상 계좌 카드 표기("-2,500만 원")다. 값은 같다.

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned living room at night, lights off. On the left 40% of the frame, a fictional Korean
man in his mid 30s, office-worker look (plain knit or shirt), sitting on a sofa and staring at a smartphone held in both
hands, frozen stunned expression, face lit by the phone's cold light. His face and the phone are in the upper 60% of the
frame; his lower body fades into darkness at the bottom. The phone screen shows only one simple blank message bubble shape
and a simple blue line dropping sharply, no app interface, no text. Fictional person, not resembling any real or famous
person, natural Korean features, realistic photo style. In the upper right area, a solid bright yellow (#FFD400) box with
the large black bold text "담보 부족". Below it, still in the upper 60%, a wide solid blue (#2D6CDF) rounded box with a thin
white border containing the huge white bold text "-2,500만 원", the largest element. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "내 돈만 넣기 아까워", line 2 "빚 냈다가 -2,500만원". The word "빚" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF.
Realistic photo style. Dark navy-toned living room at night. On the left 40% of the frame, a fictional Korean man in his
mid 30s, office-worker look, sitting on a sofa staring at a smartphone in both hands, stunned expression, face lit by the
phone's cold light; the phone screen shows only a blank message bubble shape and a simple blue line dropping sharply.
His face and the phone are in the upper 60% of the frame. Fictional person, not resembling any real or famous person.
In the upper right area, an empty bright yellow box and below it an empty solid blue (#2D6CDF) rounded box with thin white
border, both in the upper 60%. The lower third is a dark band (black to dark navy) that fades upward from the bottom edge,
with clean empty space for two lines of large text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## bittu-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `stock/source/bittu-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 신용까지 써서 번 | 흰색 #FFFFFF | — (9자) |
| 2줄 | 1,500만원이 | "1,500만원" 빨강 #E63B2E, "이" 흰색 | 수익 금액 = 빨강 (8자) |
| 3줄 | 반대매매 한 번에 | 흰색 #FFFFFF | — (9자) |
| 4줄 | -2,500만원이 됐습니다 | "-2,500만원" 노랑 #FFD400, 나머지 흰색 | 손실 금액 = 노랑 (14자) |

- 강조 2곳: 빨강 "1,500만원"(수익), 노랑 "-2,500만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (`stock/guides/thumbnail_rules.md` 1번·2번).
- "반대매매"는 흰색으로 둔다. 바로 위 줄의 빨강(수익)과 붙어 빨강 뜻이 섞이지 않게 하고, 수익 빨강 → 손실 노랑의 반전만 눈에 띄게 하기 위해서다.
- 4줄을 이으면 채택 제목 앞 문장과 같다: "신용까지 써서 번 1,500만원이 반대매매 한 번에 -2,500만원이 됐습니다"

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "신용까지 써서 번", line 2 "1,500만원이", line 3 "반대매매 한 번에", line 4 "-2,500만원이 됐습니다".
All text pure white (#FFFFFF) except "-2,500만원" in bright yellow (#FFD400) and "1,500만원" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## molppang-2026-10 · thumbnail_1 — 숫자 반전 (계좌 카드)

저장 위치: `stock/source/molppang-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 라벨 (작게) | 내 계좌 | 잉크 #1E1E1E | — |
| 카드 시작 숫자 | +1,000만 원 | 빨강 #E63B2E (수익) | 강조 1 — 빨강 = 수익 |
| 펀치 (가장 큰 숫자) | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 (파랑 = 손실) |
| 하단 1줄 | 한 종목에만 몰빵했다가 | 흰색 + 두꺼운 검정 외곽선 | "몰빵했다가" 노랑 #FFD400 — 강조 2 |
| 하단 2줄 | 천만원 수익이 -2천만원 | 흰색 + 두꺼운 검정 외곽선 | — (손실 숫자는 빨강 금지 → 흰색) |

- 하단 2줄 = T1 앞 문장 "한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다"를 줄인 것: 12자 + 13자 = 25자 (띄어쓰기 포함, 한 줄 14자 이내 · 합 26자 이내)
- 강조색(노랑·빨강) 2곳 · 노랑 상자 없음 · 펀치(위쪽 큰 문구)는 "-2,000만 원" 1개(9자)
- 하단 2줄의 "-2천만원"은 제목 표기, 카드의 "-2,000만 원"은 영상 카드 표기 — 값은 같다 (`stock/guides/thumbnail_rules.md` 1번)

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a solid dark navy (#14213D) background. In the upper 60% of the frame, slightly left of
center, a light-cream (#F2EBDD) rounded rectangle card with a thin ink-black outline, about 70% of the frame width, like a
simple personal account summary card (NOT a real banking or brokerage app: no app name, no logos, no menus, no stock name
or ticker). Inside the card: a small ink-black label "내 계좌" at the top-left; below it the text "+1,000만 원" in
medium-size bold red (#E63B2E); below that a thick blue (#2D6CDF) arrow pointing down; and across the bottom of the card a
wide solid blue (#2D6CDF) rounded box with the huge white bold text "-2,000만 원", the largest text in the image (about one
fifth of the image height). No people, no faces, no chart axes or extra numbers, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "한 종목에만 몰빵했다가", line 2 "천만원 수익이 -2천만원". The word "몰빵했다가" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep all text at least 48px inside the edges, within the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, loss blue #2D6CDF.
Clean flat editorial graphic on a solid dark navy (#14213D) background. In the upper 60% of the frame, slightly left of
center, a light-cream rounded rectangle card with a thin ink-black outline, about 70% of the frame width (no app interface,
no logos). Inside the card: empty space at the top-left for a small label, an empty line below it for a number, a thick
blue (#2D6CDF) arrow pointing down, and a wide empty solid blue (#2D6CDF) rounded box across the bottom of the card.
The lower 35% of the frame is an empty dark band that fades upward from the bottom edge (black, about 85% opacity),
kept completely clear for a two-line title. No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## molppang-2026-10 · thumbnail_2 — 인물·감정 장면 (계좌를 확인한 밤)

저장 위치: `stock/source/molppang-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽, 가장 큰 숫자) | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 (파랑 = 손실) |
| 하단 1줄 | 좋은 종목이라 몰빵했다가 | 흰색 + 두꺼운 검정 외곽선 | "몰빵했다가" 노랑 #FFD400 — 유일한 강조색 |
| 하단 2줄 | 천만원 수익이 -2천만원 | 흰색 + 두꺼운 검정 외곽선 | — (손실 숫자는 빨강 금지 → 흰색) |

- 하단 2줄 = T2 앞 문장 "좋은 종목이라 확신하고 전 재산 몰빵했다가 천만원 수익이 -2천만원이 됐습니다"를 줄인 것: 13자 + 13자 = 26자 (띄어쓰기 포함, 한 줄 14자 이내 · 합 26자 이내)
- 강조색 1곳 · 노랑 상자 없음 · 펀치는 "-2,000만 원" 1개(9자)

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A dim, dark navy-toned kitchen at night, lights mostly off. On the right half of the frame, a
fictional Korean woman in her late 30s with an office-worker look (plain cardigan over a blouse), sitting at a kitchen
table and staring at a smartphone held in both hands, frozen, stunned and regretful expression, lips pressed together,
face lit by the phone's cold light. Her face, hands and the phone are in the upper 60% of the frame; her lower body fades
into the dark bottom band. The phone screen shows only one simple blue line dropping sharply, no app interface, no text.
Fictional person, not resembling any real or famous person, natural Korean features. No crying, no extreme fear.
In the upper-left area, a wide solid blue (#2D6CDF) rounded box with a thin white border containing the huge white bold
text "-2,000만 원", the largest text in the image (about one fifth of the image height).
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "좋은 종목이라 몰빵했다가", line 2 "천만원 수익이 -2천만원". The word "몰빵했다가" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 area, at least 48px from the edges.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, loss blue #2D6CDF.
Realistic photo style. A dim, dark navy-toned kitchen at night. On the right half of the frame, a fictional Korean woman
in her late 30s with an office-worker look, sitting at a kitchen table staring at a smartphone in both hands, stunned and
regretful expression, face lit by the phone's cold light; the phone screen shows only a simple blue line dropping sharply.
Her face, hands and the phone are in the upper 60% of the frame. Fictional person, not resembling any real or famous
person, natural Korean features. In the upper-left area, an empty solid blue (#2D6CDF) rounded box with a thin white
border. The lower 35% of the frame is an empty dark band that fades upward from the bottom edge (black, about 85%
opacity), kept completely clear for a two-line title. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## molppang-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `stock/source/molppang-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 한 종목에만 몰빵해서 | 흰색 #FFFFFF | — (11자) |
| 2줄 | 얻은 천만원 수익이 | "천만원" 빨강 #E63B2E, 나머지 흰색 | 수익 금액 = 빨강 (10자) |
| 3줄 | -2천만원이 됐습니다 | "-2천만원" 노랑 #FFD400, 나머지 흰색 | 손실 금액 = 노랑, 빨강 금지 (11자) |

- 채택 제목 앞 문장 "한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다."를 **글자 그대로** 3줄로 나눴다 (끝 마침표만 뺌). 뒤 문장(결말 장치 "한 종목 올인한 사람들의 최악의 결말")은 넣지 않는다.
- 줄 길이(띄어쓰기 포함): 11자 · 10자 · 11자 — 모두 14자 이내, 어절 단위로 끊음
- 숫자 반전("천만원 수익이 -2천만원이")은 15자라 한 줄에 들어가지 않아 2줄 끝 "천만원 수익이" → 3줄 첫머리 "-2천만원이"로 바로 이어지게 나눴다
- 강조 2곳: 빨강 "천만원"(수익), 노랑 "-2천만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (`stock/guides/thumbnail_rules.md` 1번·2번).
- "몰빵해서"는 흰색으로 둔다. 바로 아래 줄의 빨강(수익)과 붙어 빨강의 뜻(이 채널에서는 수익)이 섞이지 않게 하기 위해서다 — 같은 상황(수익 금액이 있는 제목)인 빚투 thumbnail_3과 같은 선택.

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 3 lines with tight line spacing:
line 1 "한 종목에만 몰빵해서", line 2 "얻은 천만원 수익이", line 3 "-2천만원이 됐습니다".
All text pure white (#FFFFFF) except "-2천만원" at the start of line 3 in bright yellow (#FFD400) and "천만원" in line 2 in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
캔버스: 1280×720, 배경 #000000 한 가지 (그림·도형·그라데이션 없음)
글꼴: Noto Sans KR Black (또는 Pretendard Black), 글자 높이 약 100px, 줄 간격 1.15, 가운데 정렬, 글자 폭은 화면 폭의 85%(약 1088px) 안
1줄: 한 종목에만 몰빵해서   → 모두 #FFFFFF
2줄: 얻은 천만원 수익이     → "천만원" #E63B2E, 나머지 #FFFFFF
3줄: -2천만원이 됐습니다    → "-2천만원" #FFD400, "이 됐습니다" #FFFFFF
효과: 외곽선·그림자·빛 없음 · 다른 글자·로고 없음 · 오른쪽 아래 220×70 비움
저장: thumbnails/thumbnail_3.png (1280×720, 2MB 이하)
```
</details>

## multagi-2026-10 · thumbnail_1 — 숫자 반전 (계좌 카드)

저장 위치: `stock/source/multagi-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 시작 숫자 | -200만 원 | 파랑 #2D6CDF | — |
| 펀치 (위쪽) | 물타기 2번 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (노랑 상자는 이 1곳만) |
| 카드 결과 숫자 | -2,000만 원 | 흰색 (파랑 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 평단 낮추면 된다길래 | 흰색 + 검정 외곽선 | — (11자) |
| 하단 2줄 | -200만원이 -2천만원 | 흰색 + 검정 외곽선 | "-2천만원"만 노랑 #FFD400 (13자, 2줄 합 24자) |

- 강조색은 2곳: 노랑 형광펜 "물타기 2번", 노랑 글자 "-2천만원". 손실 숫자는 빨강으로 쓰지 않는다 (카드는 파랑, 하단은 흰색·노랑).
- 하단 2줄은 T1 앞 문장("평단 낮추면 된다는 말만 믿고 물타서 -200만원이 -2천만원이 됐습니다")을 줄인 것. 펀치 "물타기 2번"과 같은 말("물타")은 하단에 넣지 않았다.
- 하단 2줄은 제목 표기("-200만원", "-2천만원"), 카드는 영상 계좌 카드 표기("-200만 원", "-2,000만 원")다. 값은 같다 (`stock/guides/thumbnail_rules.md` 1번).

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos). Inside the card, on the left: the text "-200만 원" in large
blue (#2D6CDF) bold letters. In the middle: a thick blue arrow pointing right and slightly down, with the label
"물타기 2번" in black bold letters over a bright yellow (#FFD400) highlighter stripe just above the arrow. On the right: a
solid blue (#2D6CDF) rounded box with the huge white bold text "-2,000만 원", the largest element in the image.
No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "평단 낮추면 된다길래", line 2 "-200만원이 -2천만원". The word "-2천만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF.
Clean flat editorial graphic on a cream paper background with subtle paper grain. In the upper 60% of the frame, a wide
light-cream rounded rectangle card with a thin black outline. Inside: empty space on the left for a number, a thick blue
arrow pointing right and slightly down in the middle with a short bright yellow highlighter stripe just above it, and an
empty solid blue (#2D6CDF) rounded box on the right. No people. The lower third is a dark navy (#14213D) band that fades
upward from the bottom edge, with clean empty space for two lines of large text; nothing else in the band.
Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## multagi-2026-10 · thumbnail_2 — 인물·감정 장면

저장 위치: `stock/source/multagi-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 본전 오겠지 | 흰색 #F7F3EA ("본전"만 검정) | "본전"에 노랑 상자 (글자 전체 높이, 노랑 상자는 이 1곳만) |
| 결과 숫자 (위쪽) | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |
| 하단 1줄 | 기준 없이 물타서 | 흰색 + 검정 외곽선 | "기준 없이"만 노랑 #FFD400 (9자) |
| 하단 2줄 | -200만원이 -2천만원 | 흰색 + 검정 외곽선 | — (13자, 2줄 합 22자) |

- 강조색은 2곳: 노랑 상자 "본전", 노랑 글자 "기준 없이". 손실 숫자는 빨강으로 쓰지 않는다 (위쪽은 파랑 상자, 하단은 흰색).
- 하단 2줄은 T2 앞 문장("본전 금방 온다며 기준 없이 물타서 -200만원이 -2천만원이 됐습니다")을 줄인 것. "본전"은 펀치에 있어 하단에 다시 쓰지 않았다.
- "기준 없이"를 노랑으로 고른 이유: 세 제목 모두 "기준 없이"를 넣었다. 물타기 자체가 아니라 기준 없음이 문제라는 메시지다 (`titles.md` 점검).
- 하단 2줄은 제목 표기("-200만원", "-2천만원"), 위쪽 상자는 영상 계좌 카드 표기("-2,000만 원")다. 값은 같다.

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned room in early morning. On the left 40% of the frame, a fictional Korean man in his
early 40s, office-worker look (plain shirt), sitting and holding a smartphone, his other hand on his forehead, frozen
stunned and regretful expression, face lit by the phone's cold light. His face and the phone are in the upper 60% of the
frame; his lower body fades into darkness at the bottom. The phone screen shows only a simple blue line dropping sharply,
no app interface, no text. Fictional person, not resembling any real or famous person, natural Korean features, realistic
photo style. In the upper right area, large bold text "본전 오겠지" in off-white, where only the word "본전" sits on a solid
bright yellow (#FFD400) box with black text. Below it, still in the upper 60%, a wide solid blue (#2D6CDF) rounded box with
a thin white border containing the huge white bold text "-2,000만 원", the largest element. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "기준 없이 물타서", line 2 "-200만원이 -2천만원". The word "기준 없이" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF.
Realistic photo style. Dark navy-toned room in early morning. On the left 40% of the frame, a fictional Korean man in his
early 40s, office-worker look, holding a smartphone, other hand on his forehead, stunned and regretful expression, face lit
by the phone's cold light; the phone screen shows only a simple blue line dropping sharply. His face and the phone are in
the upper 60% of the frame. Fictional person, not resembling any real or famous person. In the upper right area, calm dark
empty space for a short headline with a small empty bright yellow box at its left, and below it an empty solid blue
(#2D6CDF) rounded box with thin white border, both in the upper 60%. The lower third is a dark band (black to dark navy)
that fades upward from the bottom edge, with clean empty space for two lines of large text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## multagi-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `stock/source/multagi-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 평단 낮추면 된다는 | 흰색 #FFFFFF | — (10자) |
| 2줄 | 말만 믿고 물타서 | "물타서" 빨강 #E63B2E, 나머지 흰색 | 손실을 부른 행동 = 빨강 (9자) |
| 3줄 | -200만원이 -2천만원이 | "-200만원"·"-2천만원" 노랑 #FFD400, "이" 흰색 | 손실 금액 = 노랑 (14자) |
| 4줄 | 됐습니다 | 흰색 #FFFFFF | — (4자) |

- 강조 3곳: 빨강 "물타서"(행동 단어 1곳 — `stock/guides/thumbnail_rules.md` 2번의 예), 노랑 "-200만원", 노랑 "-2천만원". 손실 숫자는 빨강으로 쓰지 않는다.
- 4줄을 이으면 채택 제목 앞 문장과 같다: "평단 낮추면 된다는 말만 믿고 물타서 -200만원이 -2천만원이 됐습니다"

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "평단 낮추면 된다는", line 2 "말만 믿고 물타서", line 3 "-200만원이 -2천만원이", line 4 "됐습니다".
All text pure white (#FFFFFF) except "-200만원" and "-2천만원" in bright yellow (#FFD400) and "물타서" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## panicsell-2026-10 · thumbnail_1 — 숫자 반전 (판 금액 → 판 뒤 반등)

저장 위치: `stock/source/panicsell-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 판 금액 | -800만 원 | 흰색 (파랑 #2D6CDF 상자 위) | — |
| 카드 판 뒤 | +30% | 빨강 #E63B2E (상승) | 가장 큰 글자 |
| 하단 1줄 | 하락장이 무서워 | 흰색 + 검정 외곽선 | — (8자) |
| 하단 2줄 | 다 팔았는데 +30% 반등 | 흰색 + 검정 외곽선 | "다 팔았는데"만 노랑 #FFD400 (14자, 2줄 합 22자) |

- 강조색은 2곳: 빨강 "+30%"(카드, 상승), 노랑 "다 팔았는데". 하단의 "+30%"는 흰색으로 둔다 (위쪽 빨강 "+30%"가 이미 가장 크다).
- 하단 2줄은 T1 앞 문장("하락장이 무서워 -800만원에 다 팔았는데 그 뒤 +30% 반등했습니다")을 줄인 것. "-800만원"은 카드에 있어 하단에서 뺐다.

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos). On the left half of the card: a solid blue (#2D6CDF) rounded
box with the large white bold text "-800만 원". On the right half of the card: a thick red (#E63B2E) arrow rising steeply
from the lower left to the upper right, ending at the huge red bold text "+30%", the largest element in the image.
No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "하락장이 무서워", line 2 "다 팔았는데 +30% 반등". The word "다 팔았는데" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, loss blue #2D6CDF, gain red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. In the upper 60% of the frame, a wide
light-cream rounded rectangle card with a thin black outline. Left half: an empty solid blue (#2D6CDF) rounded box. Right
half: a thick red arrow rising steeply from lower left to upper right, with empty space at its tip for a number.
No people. The lower third is a dark navy (#14213D) band that fades upward from the bottom edge, with clean empty space
for two lines of large text; nothing else in the band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## panicsell-2026-10 · thumbnail_2 — 인물·감정 장면 (다 판 다음 날)

저장 위치: `stock/source/panicsell-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 결과 숫자 (위쪽) | +11% | 빨강 #E63B2E (상승, 얇은 흰 외곽선) | 가장 큰 글자 |
| 하단 1줄 | 서킷브레이커 날 팔았는데 | 흰색 + 검정 외곽선 | "서킷브레이커"만 노랑 #FFD400 (13자) |
| 하단 2줄 | 다음 날 +11% 올랐다 | 흰색 + 검정 외곽선 | — (13자, 2줄 합 26자) |

- 강조색은 2곳: 빨강 "+11%"(위쪽, 상승), 노랑 "서킷브레이커". 하단의 "+11%"는 흰색으로 둔다 (위쪽 빨강 "+11%"가 이미 가장 크다).
- 하단 2줄은 T2 앞 문장("서킷브레이커 걸린 날 -800만원에 전부 팔았는데 다음 날 +11% 올랐습니다")을 줄인 것. 2줄 합 26자 한도 때문에 "걸린"·"-800만원에 전부"를 뺐다 ("-800만원"은 T1·T3 썸네일에 있음).

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned kitchen in the early morning before work. On the left 40% of the frame, a fictional
Korean woman in her late 30s, office-worker look (plain blouse), sitting at a kitchen table and staring at a smartphone,
mouth slightly open, blank regretful expression, face lit by the phone's light. Her face and the phone are in the upper 60%
of the frame; her lower body fades into darkness at the bottom. The phone screen shows only a simple red line rising
sharply, no app interface, no text. Fictional person, not resembling any real or famous person, natural Korean features,
realistic photo style. In the upper right area, the huge red (#E63B2E) bold text "+11%" with a thin white outline, the
largest element, kept in the upper 60%. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "서킷브레이커 날 팔았는데", line 2 "다음 날 +11% 올랐다". The word "서킷브레이커" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, gain red #E63B2E.
Realistic photo style. Dark navy-toned kitchen in the early morning. On the left 40% of the frame, a fictional Korean woman
in her late 30s, office-worker look, sitting at a kitchen table staring at a smartphone, mouth slightly open, blank
regretful expression, face lit by the phone's light; the phone screen shows only a simple red line rising sharply.
Her face and the phone are in the upper 60% of the frame. Fictional person, not resembling any real or famous person.
The upper right area is calm dark empty space for one big number. The lower third is a dark band (black to dark navy) that
fades upward from the bottom edge, with clean empty space for two lines of large text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## panicsell-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `stock/source/panicsell-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 하락장이 무서워 | 흰색 #FFFFFF | — (8자) |
| 2줄 | -800만원에 다 팔았는데 | "-800만원" 노랑 #FFD400, "다 팔았는데" 빨강 #E63B2E, "에" 흰색 | 손실 금액 = 노랑, 손실을 부른 행동 = 빨강 (14자) |
| 3줄 | 그 뒤 +30% | "+30%" 빨강 #E63B2E, "그 뒤" 흰색 | 상승 = 빨강 (8자) |
| 4줄 | 반등했습니다 | 흰색 #FFFFFF | — (6자) |

- 강조 3곳: 노랑 "-800만원"(손실), 빨강 "다 팔았는데"(행동 단어 1곳 — `stock/guides/thumbnail_rules.md` 2번의 예), 빨강 "+30%"(상승). 손실 숫자는 빨강으로 쓰지 않는다.
- 4줄을 이으면 채택 제목 앞 문장과 같다: "하락장이 무서워 -800만원에 다 팔았는데 그 뒤 +30% 반등했습니다"

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "하락장이 무서워", line 2 "-800만원에 다 팔았는데", line 3 "그 뒤 +30%", line 4 "반등했습니다".
All text pure white (#FFFFFF) except "-800만원" in bright yellow (#FFD400) and "다 팔았는데" and "+30%" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
