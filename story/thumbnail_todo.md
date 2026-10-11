# story 썸네일 만들 목록 (이미지 없는 것)

자동 생성 — `python tools/make_summary.py --thumb-todo story` (2026-10-11 08:41)

1. [A] 프롬프트를 이미지 AI에 넣는다. 한글이 틀리면 [B]로 만들고 문구표대로 글자를 얹는다.
2. 이미지를 아래 '저장 위치'로 GitHub에 올린다 (크기는 업로드 때 1280×720으로 자동 변환).

남은 썸네일: 9개

## chayongjeung-2026-10 · thumbnail_1 — 숫자 반전 (3,000만 원 → 90만 원)

저장 위치: `story/source/chayongjeung-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 시작 숫자 (위 왼쪽) | 3,000만 원 | 네이비 #14213D (흰 쪽지) | 큰 글자 |
| 핵심 숫자 (위 오른쪽) | 90만 원 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |
| 하단 1줄 | 차용증 없이 빌려준 돈 | 흰색 + 검정 외곽선 | "차용증 없이" 노랑 #FFD400 글자 |
| 하단 2줄 | 돌려받은 건 90만 원 | 흰색 + 검정 외곽선 | — |

- 하단 2줄 = 채택 제목 앞 문장("친구라서 차용증 없이 빌려준 3천만 원, 돌려받은 건 90만 원이었습니다")을 줄인 것. 글자 수(띄어쓰기 포함) 12 · 12, 합 24
- 위쪽은 숫자 2개(시작 → 끝)뿐, 펀치 문구 없음. "90만 원"이 위아래에 두 번 나오는 것은 숫자라 허용. "3,000만 원"은 대본 표기(주제 규칙 1번), 하단에는 넣지 않아 표기가 섞이지 않는다
- 강조 1곳(노랑 글자 "차용증 없이"). 빨강 없음 (잃은 돈은 파랑 상자)

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat clean graphic style on a plain cream (#F2EBDD) background, no decorations. Upper 60% of the frame: on the left, a
plain white paper money-transfer slip with no bank name, no logo, no account number, no other writing, showing only the
large dark navy bold text "3,000만 원". A thick dark navy arrow points right to a solid blue (#2D6CDF) rounded box with a
thin white border containing the huge white bold text "90만 원", the largest element in the image. Keep all text inside
the central 16:9 safe area, at least 48px from the edges. No people, no banknotes, no coins, no real money designs,
no app screens.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "차용증 없이 빌려준 돈", line 2 "돌려받은 건 90만 원". The word "차용증 없이" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, loss blue #2D6CDF.
Flat clean graphic style on a plain cream background. All elements in the upper 60% of the frame: on the left, a blank
plain white paper money-transfer slip with no bank name, no logo and no writing; a thick dark navy arrow pointing right
to an empty solid blue (#2D6CDF) rounded box with a thin white border on the right. The lower third is a plain dark navy
(#14213D) band fading upward from the bottom edge, kept clean and empty for two lines of headline. No people, no
banknotes, no coins. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## chayongjeung-2026-10 · thumbnail_2 — 인물·감정 장면 (30년 친구였는데)

저장 위치: `story/source/chayongjeung-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위 오른쪽) | 30년 친구였는데 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (글자 전체 높이, 노랑 상자는 이 1곳) |
| 핵심 숫자 (위 오른쪽) | 90만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |
| 하단 1줄 | 꼭 갚겠다는 말만 믿고 | 흰색 + 검정 외곽선 | — |
| 하단 2줄 | 보낸 3천만 원 | 흰색 + 검정 외곽선 | "3천만 원" 노랑 #FFD400 글자 (잃은 돈 → 빨강 금지) |

- 하단 2줄 = T2 앞 문장("연말까지 꼭 갚겠다는 카톡만 믿고 보낸 3천만 원")을 줄인 것. 글자 수(띄어쓰기 포함) 12 · 8, 합 20
  - 제목의 "카톡"은 "말"로 바꿨다: 휴대폰 말풍선 옆에 앱 이름을 두지 않기 위해서다 (주제 규칙 4번 "앱 이름·로고 없음")
  - "3천만 원"은 제목 표기 그대로 (값은 대본 "3천만 원"과 같음). 위쪽 "90만 원"과는 다른 숫자라 표기가 섞이지 않는다
- 펀치 "30년 친구였는데"(9자)는 하단 2줄과 겹치는 말이 없다
- 강조 2곳: 노랑 상자 "30년 친구였는데", 노랑 글자 "3천만 원". 빨강 없음

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A dim dark navy-toned living room in the evening, soft warm lamp light. On the left 45% of the frame,
a fictional Korean woman around 50 years old, neat short hair, plain knit sweater, sitting at a dining table and holding a
smartphone in both hands, looking at it with a hollow, hurt, disappointed expression, as if betrayed by an old friend;
no tears, no anger. Her face and the phone are in the upper 60% of the frame. The phone screen shows only two simple blank
message bubble shapes, no app interface, no logo, no text.
Fictional person, not resembling any real or famous person, natural Korean features, realistic photo style. No other people in the scene.
In the upper right area, a solid bright yellow (#FFD400) box with large black bold text "30년 친구였는데". Below it, a wide
solid blue (#2D6CDF) rounded box with a thin white border containing the huge white bold text "90만 원", the largest element.
Keep the face and all text inside the central 16:9 safe area.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "꼭 갚겠다는 말만 믿고", line 2 "보낸 3천만 원". The word "3천만 원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF.
Realistic photo style. A dim dark navy-toned living room in the evening, soft lamp light. On the left 45% of the frame, a
fictional Korean woman around 50, plain knit sweater, sitting at a dining table holding a smartphone in both hands, hollow,
hurt, disappointed expression, no tears; her face and the phone are in the upper 60% of the frame; the phone screen shows
only blank message bubble shapes. Fictional person, not resembling any real or famous person. In the upper right area, an
empty bright yellow box and an empty solid blue (#2D6CDF) rounded box with thin white border below it. The lower third is
covered by a dark band that fades upward from the bottom edge, kept clean and empty for two lines of headline.
Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## chayongjeung-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `story/source/chayongjeung-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1 | 친구라서 차용증 없이 | 흰색 #FFFFFF | "차용증 없이" 빨강 #E63B2E (결정적 행동 — 숫자 아님) |
| 2 | 빌려준 3천만 원, | 흰색 #FFFFFF | "3천만 원" 노랑 #FFD400 (잃은 돈 → 빨강 금지) |
| 3 | 돌려받은 건 | 흰색 #FFFFFF | — |
| 4 | 90만 원이었습니다 | 흰색 #FFFFFF | "90만 원" 노랑 #FFD400 |

- 채택 제목 앞 문장과 한 글자도 다르지 않다 (쉼표 포함, 문장 끝 마침표만 뺌). 줄 글자 수(띄어쓰기 포함): 11 · 10 · 6 · 10
- 강조 3곳 (빨강 1 · 노랑 2). 외곽선·그림자·노랑 상자 없음

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "친구라서 차용증 없이", line 2 "빌려준 3천만 원,", line 3 "돌려받은 건", line 4 "90만 원이었습니다".
All text pure white (#FFFFFF) except "3천만 원" and "90만 원" in bright yellow (#FFD400) and "차용증 없이" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## jeungyeo-2026-10 · thumbnail_1 — 숫자 반전 (4억 아파트 → 월세방)

저장 위치: `story/source/jeungyeo-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 + 핵심 숫자 (위 왼쪽) | 4억 아파트 | 잉크 #1E1E1E (크림 배경) | 위쪽에서 가장 큰 글자 |
| 하단 1줄 | 미리 넘긴 4억 집 | 흰색 + 검정 외곽선 | — |
| 하단 2줄 | 제게 남은 건 월세방 | 흰색 + 검정 외곽선 | "월세방" 노랑 #FFD400 글자 |

- 하단 2줄 = 채택 제목 앞 문장("어차피 줄 거라며 미리 넘긴 4억 집, 제게 남은 건 월세방이었습니다")을 줄인 것. 글자 수(띄어쓰기 포함) 10 · 11, 합 21
- 펀치 "4억 아파트"(6자)는 하단 2줄과 겹치는 말이 없다 ("4억"은 숫자라 반복 허용, "아파트"·"집"은 다른 말). 대본 문장 1은 "4억 원짜리 아파트"
- 강조 2곳: 노랑 열쇠 아이콘, 노랑 글자 "월세방". 빨강 없음 (잃은 재산 4억은 잉크 글자)

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat-photo hybrid style on a warm cream (#F2EBDD) background. Upper 60% of the frame: on the left 40%, an ordinary
mid-rise Korean apartment building (modest, not luxury), bright daylight. Above it, large heavy black bold text "4억 아파트",
the biggest text in the upper area. In the center, one thick dark navy arrow with a white outline pointing from left to
right, with a small simple yellow (#FFD400) house key icon at the arrow's tip. On the right 40%, a small, dim, empty
one-room studio seen through a single small window: bare walls, one small potted plant on the sill, no people, no text.
No people, no documents, no logos, no money bills.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "미리 넘긴 4억 집", line 2 "제게 남은 건 월세방". The word "월세방" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400.
Warm cream background. All elements in the upper 60% of the frame. Left 40%: an ordinary mid-rise Korean apartment
building (modest, not luxury) in daylight, with empty cream space above it for a label. Center: one thick dark navy arrow
with white outline pointing right, a small simple yellow house key icon at its tip. Right 40%: a small dim empty one-room
studio seen through one small window, one potted plant on the sill, no people. The lower third is a plain dark navy
(#14213D) band fading upward from the bottom edge, kept clean and empty for two lines of headline. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## jeungyeo-2026-10 · thumbnail_2 — 인물·감정 장면 (원룸 창가, 끊긴 전화)

저장 위치: `story/source/jeungyeo-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위 오른쪽) | 전화도 끊겼다 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 위쪽에서 가장 큰 글자 |
| 하단 1줄 | 모시겠다는 말만 믿고 | 흰색 + 검정 외곽선 | — |
| 하단 2줄 | 4억 집을 넘겼는데 | 흰색 + 검정 외곽선 | "4억" 노랑 #FFD400 글자 (잃은 재산 → 빨강 금지) |

- 하단 2줄 = T2 앞 문장("모시고 살겠다는 말만 믿고 4억 집 명의를 넘겼는데")을 줄인 것. 글자 수(띄어쓰기 포함) 11 · 10, 합 21. "모시겠다는"은 대본 문장 3 "모시겠다고 했어요"의 말
- 펀치 "전화도 끊겼다"(7자)는 하단 2줄과 겹치는 말이 없다. 대본 문장 14 "아들의 전화도 끊겼고"의 말 (전에 쓰던 "모시겠다더니"는 하단 1줄과 같은 말이라 뺐다)
- 강조 1곳(노랑 글자 "4억"). 핵심 숫자 "4억"은 하단 2줄에 있고 위쪽 펀치는 숫자 없는 결과 장면이다

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A small, bare, dark navy-toned one-room studio in the evening, faint light from one small window.
On the left 45% of the frame, a fictional Korean woman in her early 70s with short gray-streaked hair and a plain
cardigan, sitting on a thin floor mattress, holding a smartphone in both hands and looking down at it with a quiet,
empty, deeply disappointed expression (not crying); her face and the phone are in the upper 60% of the frame. The phone
screen shows only a plain blank call-screen shape with round button shapes, no app interface, no text, no numbers.
Fictional person, not resembling any real or famous person, natural Korean features, realistic photo style.
In the upper right area, a wide solid blue (#2D6CDF) rounded box with a thin white border containing huge white bold
text "전화도 끊겼다". No other people in the scene.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "모시겠다는 말만 믿고", line 2 "4억 집을 넘겼는데". The word "4억" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, loss blue #2D6CDF.
Realistic photo style. A small bare dark navy-toned one-room studio in the evening, faint light from one small window.
On the left 45% of the frame, a fictional Korean woman in her early 70s, short gray-streaked hair, plain cardigan,
sitting on a thin floor mattress holding a smartphone in both hands, looking down with a quiet, deeply disappointed
expression (not crying); her face and the phone are in the upper 60% of the frame; the phone screen shows only a blank
call-screen shape with no text. Fictional person, not resembling any real or famous person. In the upper right area, an
empty solid blue (#2D6CDF) rounded box with thin white border. The lower third is covered by a dark band that fades
upward from the bottom edge, kept clean and empty for two lines of headline. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## jeungyeo-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `story/source/jeungyeo-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1 | 어차피 줄 거라며 | 흰색 #FFFFFF | — |
| 2 | 미리 넘긴 4억 집, | 흰색 #FFFFFF | "미리 넘긴" 빨강 #E63B2E (결정적 행동 — 숫자 아님) · "4억 집" 노랑 #FFD400 (잃은 재산 → 빨강 금지) |
| 3 | 제게 남은 건 | 흰색 #FFFFFF | — |
| 4 | 월세방이었습니다 | 흰색 #FFFFFF | "월세방" 노랑 #FFD400 |

- 채택 제목 앞 문장과 한 글자도 다르지 않다 (쉼표 포함, 문장 끝 마침표만 뺌). 줄 글자 수(띄어쓰기 포함): 9 · 11 · 7 · 8
- 강조 3곳 (빨강 1 · 노랑 2). 외곽선·그림자·노랑 상자 없음

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "어차피 줄 거라며", line 2 "미리 넘긴 4억 집,", line 3 "제게 남은 건", line 4 "월세방이었습니다".
All text pure white (#FFFFFF) except "4억 집" and "월세방" in bright yellow (#FFD400) and "미리 넘긴" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## myeoneuri-2026-10 · thumbnail_1 — 숫자 반전 (8년 간병 → 0원)

저장 위치: `story/source/myeoneuri-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위 왼쪽) | 8년 간병 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (노랑 상자는 이 1곳) |
| 핵심 숫자 (위 오른쪽) | 0원 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |
| 하단 1줄 | 말씀만 믿고 8년 모셨는데 | 흰색 + 검정 외곽선 | "말씀만 믿고" 노랑 #FFD400 글자 |
| 하단 2줄 | 며느리 몫은 0원 | 흰색 + 검정 외곽선 | — |

- 하단 2줄 = 채택 제목 앞 문장("아버님 말씀만 믿고 8년을 모셨는데 며느리 몫은 0원이었습니다")을 줄인 것. 글자 수(띄어쓰기 포함) 14 · 9, 합 23
- 펀치 "8년 간병"(5자)은 하단 2줄과 겹치는 말이 없다 ("8년"은 숫자라 반복 허용)
- 강조 2곳: 노랑 상자 "8년 간병", 노랑 글자 "말씀만 믿고". 빨강 없음 (잃은 몫 0원은 파랑 상자)

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat graphic design on a cream (#F2EBDD) background with a faint paper texture. Upper 60% of the frame: on the left,
a solid bright yellow (#FFD400) rectangle containing the large black bold text "8년 간병". In the middle, one thick
ink-black arrow pointing right. On the right, a solid blue (#2D6CDF) rounded box containing the huge white bold text "0원",
the biggest element, about 25% of the image height. Below the arrow, a small prop: one old torn-off calendar sheet seen
from the back, with faint illegible handwritten pen strokes only (no readable words, not a legal form). No people, no money
bills, no buildings, no gavel. Keep all text inside the central 16:9 safe area, at least 48px from the edges.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "말씀만 믿고 8년 모셨는데", line 2 "며느리 몫은 0원". The word "말씀만 믿고" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF.
Clean flat graphic design on a cream background with a faint paper texture. All elements in the upper 60% of the frame:
an empty solid bright yellow rectangle on the left, one thick ink-black arrow pointing right in the middle, and a large
empty solid blue (#2D6CDF) rounded box on the right; below the arrow, one old torn-off calendar sheet seen from the back
with faint illegible pen strokes. The lower third is a plain dark navy (#14213D) band fading upward from the bottom edge,
kept completely clean and empty for two lines of headline. No people, no money bills, no gavel. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## myeoneuri-2026-10 · thumbnail_2 — 인물·감정 장면 (메모를 든 사연자)

저장 위치: `story/source/myeoneuri-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 + 핵심 숫자 (위 오른쪽) | 제 몫은 0원 | 흰색 (파랑 #2D6CDF 상자) | "0원"이 가장 큰 글자 |
| 하단 1줄 | 손글씨 한 장 믿고 | 흰색 + 검정 외곽선 | "손글씨 한 장" 노랑 #FFD400 글자 |
| 하단 2줄 | 8년을 모셨는데 | 흰색 + 검정 외곽선 | — |

- 하단 2줄 = T2 앞 문장("이 집은 너희 내외 몫이라는 손글씨 한 장 믿고 8년을 모셨는데")을 줄인 것. 글자 수(띄어쓰기 포함) 10 · 8, 합 18. 결과는 위쪽 "제 몫은 0원"이 보여 준다
- 펀치 "제 몫은 0원"(7자)은 하단 2줄과 겹치는 말이 없다
- 강조 1곳(노랑 글자 "손글씨 한 장"). 빨강 없음 (잃은 몫 0원은 파랑 상자)

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A half-empty Korean apartment living room in soft afternoon light, a few taped cardboard moving
boxes on the floor, pale marks where furniture used to be. On the left 45% of the frame, a fictional Korean woman in her
mid 50s wearing a plain cardigan, chest-up framing, holding one old calendar sheet in both hands and looking down at it
with a hollow, quietly hurt expression (no tears); her face, hands and the sheet are all in the upper 60% of the frame.
Fictional person, not resembling any real or famous person, natural Korean features, realistic photo style.
On the wall behind her, a small framed photo showing only a blurred silhouette of an elderly man, face not recognizable.
The calendar sheet shows only faint illegible handwriting strokes. In the upper right area, one solid blue (#2D6CDF)
rounded box containing white bold text: a smaller line "제 몫은" above a huge "0원", the largest element.
No romance, no funeral, no court, no gavel, no legal form. Keep the face and all text inside the central 16:9 safe area.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "손글씨 한 장 믿고", line 2 "8년을 모셨는데". The word "손글씨 한 장" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, loss blue #2D6CDF.
Realistic photo style. A half-empty Korean apartment living room in soft afternoon light with a few taped moving boxes.
On the left 45% of the frame, a fictional Korean woman in her mid 50s in a plain cardigan, chest-up framing, holding one
old calendar sheet in both hands, looking down at it with a hollow, quietly hurt expression (no tears); her face and the
sheet are in the upper 60% of the frame. Fictional person, not resembling any real or famous person. A small framed photo
on the wall shows only a blurred silhouette of an elderly man. In the upper right area, one empty solid blue (#2D6CDF)
rounded box. The lower third is covered by a dark band that fades upward from the bottom edge, kept clean and empty for
two lines of headline. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## myeoneuri-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `story/source/myeoneuri-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1 | 아버님 말씀만 믿고 | 흰색 #FFFFFF | "말씀만 믿고" 빨강 #E63B2E (결정적 말·행동 — 숫자 아님) |
| 2 | 8년을 모셨는데 | 흰색 #FFFFFF | "8년" 노랑 #FFD400 |
| 3 | 며느리 몫은 | 흰색 #FFFFFF | — |
| 4 | 0원이었습니다 | 흰색 #FFFFFF | "0원" 노랑 #FFD400 (잃은 몫 → 빨강 금지) |

- 채택 제목 앞 문장과 한 글자도 다르지 않다 (문장 끝 마침표만 뺌). 줄 글자 수(띄어쓰기 포함): 10 · 8 · 6 · 7
- 강조 3곳 (빨강 1 · 노랑 2). 외곽선·그림자·노랑 상자 없음

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "아버님 말씀만 믿고", line 2 "8년을 모셨는데", line 3 "며느리 몫은", line 4 "0원이었습니다".
All text pure white (#FFFFFF) except "8년" and "0원" in bright yellow (#FFD400) and "말씀만 믿고" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
