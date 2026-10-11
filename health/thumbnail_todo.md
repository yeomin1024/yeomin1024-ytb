# health 썸네일 만들 목록 (이미지 없는 것)

자동 생성 — `python tools/make_summary.py --thumb-todo health` (2026-10-11 08:41)

1. [A] 프롬프트를 이미지 AI에 넣는다. 한글이 틀리면 [B]로 만들고 문구표대로 글자를 얹는다.
2. 이미지를 아래 '저장 위치'로 GitHub에 올린다 (크기는 업로드 때 1280×720으로 자동 변환).

남은 썸네일: 9개

## prediabetes-2026-10 · thumbnail_1 — 결과지 숫자 반전

저장 위치: `health/source/prediabetes-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위 가운데) | 공복혈당 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 노랑) |
| 처음 숫자 | 108 | 잉크 #1E1E1E | 중간 크기, 왼쪽 뒤 카드 |
| 결과 숫자 | 131 | 빨강 #E63B2E | 가장 큰 글자, 오른쪽 앞 카드 |
| 하단 1줄 | '경계'라 넘겼다가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 없음 |
| 하단 2줄 | 3년 만에 당뇨가 됐다 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "당뇨"만 빨강 #E63B2E (나빠진 결과) |

- 하단 2줄 = 채택 제목 앞 문장 "공복혈당 108 '경계'라 괜찮다고 넘겼다가 3년 만에 당뇨가 됐습니다"를 줄인 것 (제목 단어를 그대로 씀). 1줄 10자 · 2줄 12자, 합 22자 (띄어쓰기 포함)
- 펀치 "공복혈당"(4자)은 하단 2줄에 없는 말이다. 108 → 131 숫자는 그림 쪽에만 있다
- 강조 합 3곳: 노랑 상자 "공복혈당", 빨강 "131", 빨강 "당뇨". 파랑 글자 없음

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: clean flat illustration on a cream (#F2EBDD) background. At the top center, a solid bright yellow
(#FFD400) box with the black bold text "공복혈당". Below it, two simple white medical checkup result cards overlap in the
center, with no logos, no institution names, no barcodes, no personal data and no small print. On the smaller card at the
back left, the black number "108" in medium size. A thick black arrow points from the left card to the right card, with
nothing written on or above the arrow. On the larger card in front on the right, the huge red (#E63B2E) number "131", the
largest element in the image (about 25% of the image height). No people, no needles, no blood, no hospital scenes.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "'경계'라 넘겼다가", line 2 "3년 만에 당뇨가 됐다". The word "당뇨" is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, gain red #E63B2E.
Upper 60% of the frame: clean flat illustration on a cream background. An empty solid yellow box at the top center. Below
it, two simple blank white checkup result cards overlap in the center, the right one larger and in front, with a thick
black arrow from the left card to the right card. Smaller empty space on the left card and large empty space on the right
card for a big number. No logos, no barcodes, no people, no medical scenes.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, completely empty, reserved for two lines of
headline text. Nothing from the picture reaches into this band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## prediabetes-2026-10 · thumbnail_2 — 인물·감정 장면

저장 위치: `health/source/prediabetes-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 + 결과 숫자 (오른쪽 위) | 공복혈당 131 | 흰 글자 (빨강 #E63B2E 상자) | "131"을 가장 크게 |
| 하단 1줄 | 아픈 데 없다며 넘긴 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 없음 |
| 하단 2줄 | 108이 3년 만에 131 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "108"만 노랑 #FFD400 (처음 숫자) |

- 하단 2줄 = 짝 제목 T2 앞 문장 "아픈 데 없다며 넘긴 공복혈당 108이 3년 만에 131이 됐습니다"를 줄인 것 (제목 단어를 그대로 씀, "공복혈당"은 그림 쪽 상자에). 1줄 11자 · 2줄 14자, 합 25자 (띄어쓰기 포함)
- 펀치 "공복혈당"(4자)은 하단 2줄에 없는 말이다. 131은 위아래 모두 나온다 (숫자 반복은 허용)
- 강조 합 2곳: 빨강 상자 "공복혈당 131", 노랑 "108". 노랑 상자 없음, 파랑 글자 없음

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Softly blurred bright office background in warm cream tones. On the left 40% of the frame, a
fictional Korean man in his early 50s, office-worker look (white shirt, loosened tie), shown from the waist up, holding a
single health checkup result sheet with both hands at chest height, the sheet facing away or blurred so no text is
readable, surprised and worried expression looking at the paper. His face, hands and the sheet are all in the upper 60%
of the frame. Fictional person, not resembling any real or famous person, natural Korean features. Not a doctor, no white
coat, no hospital, no needles. On the upper right side, a wide solid red (#E63B2E) rounded box containing the white bold
text "공복혈당 131", with the number "131" much larger than the word, the largest text in the image. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "아픈 데 없다며 넘긴", line 2 "108이 3년 만에 131". The word "108" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, gain red #E63B2E.
Realistic photo style. Softly blurred bright office background. On the left 40% of the frame, a fictional Korean man in
his early 50s, office-worker look, shown from the waist up, holding a blank health checkup sheet with both hands at chest
height, surprised and worried expression, his face and hands in the upper 60% of the frame. Fictional person, not
resembling any real or famous person. Not a doctor, no hospital. On the upper right, an empty solid red (#E63B2E) rounded
box with calm empty space around it.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, completely empty, reserved for two lines of
headline text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## prediabetes-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `health/source/prediabetes-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 공복혈당 108 | 흰색 #FFFFFF | 없음 |
| 2줄 | '경계'라 괜찮다고 | 흰색 #FFFFFF | "'경계'"(작은따옴표 포함)만 노랑 #FFD400 — 믿었던 말 |
| 3줄 | 넘겼다가 3년 만에 | 흰색 #FFFFFF | 없음 |
| 4줄 | 당뇨가 됐습니다 | 흰색 #FFFFFF | "당뇨"만 빨강 #E63B2E — 나빠진 결과 |

- 줄 길이 8자 · 10자 · 10자 · 8자 (띄어쓰기 포함, 모두 14자 이내). 어절 사이에서만 줄을 바꿨다
- 이어 붙이면 채택 제목 앞 문장과 한 글자도 다르지 않다: "공복혈당 108 '경계'라 괜찮다고 넘겼다가 3년 만에 당뇨가 됐습니다". 뒤 문장("검진 결과지 대충 본 사람들의 공통점")은 넣지 않는다
- 숫자 덩어리 "공복혈당 108"과 결과 "당뇨가 됐습니다"가 각각 한 줄에 온다
- 강조 합 2곳 (3곳 이하). 파랑 글자 없음 (검정 위 파랑 금지)

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "공복혈당 108", line 2 "'경계'라 괜찮다고", line 3 "넘겼다가 3년 만에", line 4 "당뇨가 됐습니다".
All text pure white (#FFFFFF) except "'경계'" in bright yellow (#FFD400) and "당뇨" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## sarcopenia-2026-10 · thumbnail_1 — 숫자 반전 (걸음 수 10,000 → 악력 17kg)

저장 위치: `health/source/sarcopenia-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 처음 숫자 | 10,000 | 잉크 #1E1E1E | 휴대폰 화면 안, 중간 크기 |
| 펀치 (악력계 위) | 악력 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 노랑) |
| 결과 숫자 | 17kg | 빨강 #E63B2E | 가장 큰 글자 |
| 하단 1줄 | 만 보만 걸으면 된다고 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 없음 |
| 하단 2줄 | 믿다가 근감소증이 됐다 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "근감소증"만 빨강 #E63B2E (나빠진 결과) |

- 하단 2줄 = 채택 제목 앞 문장 "만 보만 걸으면 된다고 믿다가 2년 만에 악력 17kg, 근감소증이 됐습니다"를 줄인 것 (제목 단어를 그대로 씀, "악력 17kg"은 그림 쪽에). 1줄 12자 · 2줄 12자, 합 24자 (띄어쓰기 포함)
- 펀치 "악력"(2자)은 하단 2줄에 없는 말이다. 10,000 → 17kg 숫자는 그림 쪽에만 있다
- 강조 합 3곳: 노랑 상자 "악력", 빨강 "17kg", 빨강 "근감소증". 파랑 글자 없음

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: clean flat illustration on a cream (#F2EBDD) background. On the left, a simple generic smartphone
seen from the front, its plain white screen showing only the big black number "10,000". No app name, no icons, no logos,
no status bar, no other words or interface elements, so it does not look like any real app. In the middle, a thick black
arrow pointing from the phone to the right, with nothing written on or above the arrow. On the right, a simple unbranded
hand grip dynamometer (a handle with a round analog dial and a needle, the dial has no printed numbers or text). Above the
dynamometer, the black bold text "악력" on a solid bright yellow (#FFD400) box. Next to the dynamometer, the huge red
(#E63B2E) text "17kg", the largest element in the image (about 25% of the image height). No people, no hands, no gym
equipment brands, no hospital scenes, no falling.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "만 보만 걸으면 된다고", line 2 "믿다가 근감소증이 됐다". The word "근감소증" is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, gain red #E63B2E.
Upper 60% of the frame: clean flat illustration on a cream background. On the left, a simple generic smartphone with a
blank white screen (empty space for a number), no app name, no icons, no logos, no status bar. In the middle, a thick
black arrow pointing right. On the right, a simple unbranded hand grip dynamometer with a round analog dial and a needle,
no numbers on the dial. An empty solid yellow box above the dynamometer, and large calm empty space next to it for a big
number. No people, no hands, no brands, no hospital scenes.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, completely empty, reserved for two lines of
headline text. Nothing from the picture reaches into this band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## sarcopenia-2026-10 · thumbnail_2 — 인물·감정 장면 (계단 난간을 붙잡은 순간)

저장 위치: `health/source/sarcopenia-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 + 결과 숫자 (오른쪽 위) | 악력 17kg | 흰 글자 (빨강 #E63B2E 상자) | "17kg"을 가장 크게 |
| 하단 1줄 | 매일 만 보 걷던 60대 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 없음 |
| 하단 2줄 | 2년 만에 근감소증 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "근감소증"만 빨강 #E63B2E (나빠진 결과) |

- 하단 2줄 = 짝 제목 T2 앞 문장 "매일 만 보 걷던 60대가 2년 만에 근감소증이 됐습니다"를 줄인 것 (제목 단어를 그대로 씀). 1줄 13자 · 2줄 10자, 합 23자 (띄어쓰기 포함)
- 펀치 "악력"(2자)은 하단 2줄에 없는 말이다. 짝 제목 T2에 없는 **악력 17kg**(문장 10)과 계단 장면(문장 9)을 그림 쪽이 보탠다
- 강조 합 2곳: 빨강 상자 "악력 17kg", 빨강 "근감소증". 노랑 없음, 파랑 글자 없음

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Bright daytime, outdoor concrete stairs in an apartment complex, background softly blurred in warm
cream tones. On the left 45% of the frame, a fictional Korean woman in her early 60s with neat short hair, wearing a plain
light-colored windbreaker with no patterns, no text and no logos, shown from the waist up. She was walking down the stairs
and has suddenly stopped, gripping the metal handrail firmly with one hand, looking down toward her own legs with a
surprised and flustered expression. She is standing upright, not falling, not sitting down, not injured. Her face and the
hand on the handrail are in the upper 60% of the frame. Fictional person, not resembling any real or famous person,
natural Korean features. No doctor, no white coat, no hospital, no walking stick, no gym equipment. On the upper right
side, a wide solid red (#E63B2E) rounded box containing the white bold text "악력 17kg", with "17kg" much larger than the
word, the largest text in the image. No crying, no pain, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "매일 만 보 걷던 60대", line 2 "2년 만에 근감소증". The word "근감소증" is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, gain red #E63B2E.
Realistic photo style. Bright daytime, outdoor concrete stairs in an apartment complex, softly blurred cream background.
On the left 45% of the frame, a fictional Korean woman in her early 60s in a plain light windbreaker with no logos, shown
from the waist up, suddenly stopping on the stairs and gripping the metal handrail with one hand, surprised and flustered
expression, her face and hand in the upper 60% of the frame. Standing upright, not falling. Fictional person, not
resembling any real or famous person. No hospital, no doctor. On the upper right, an empty solid red (#E63B2E) rounded box
with calm empty space around it.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, completely empty, reserved for two lines of
headline text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## sarcopenia-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `health/source/sarcopenia-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 만 보만 걸으면 | 흰색 #FFFFFF | "만 보만"만 노랑 #FFD400 — 믿었던 말 |
| 2줄 | 된다고 믿다가 | 흰색 #FFFFFF | 없음 |
| 3줄 | 2년 만에 악력 17kg, | 흰색 #FFFFFF | 없음 |
| 4줄 | 근감소증이 됐습니다 | 흰색 #FFFFFF | "근감소증"만 빨강 #E63B2E — 나빠진 결과 |

- 줄 길이 8자 · 7자 · 14자 · 10자 (띄어쓰기 포함, 모두 14자 이내). 어절 사이에서만 줄을 바꿨다
- 이어 붙이면 채택 제목 앞 문장과 한 글자도 다르지 않다: "만 보만 걸으면 된다고 믿다가 2년 만에 악력 17kg, 근감소증이 됐습니다" (3줄 끝 쉼표 포함). 뒤 문장("걷기만 하는 사람들의 공통점")은 넣지 않는다
- 숫자 덩어리 "2년 만에 악력 17kg,"와 결과 "근감소증이 됐습니다"가 각각 한 줄에 온다
- 강조 합 2곳 (3곳 이하). 파랑 글자 없음 (검정 위 파랑 금지)

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "만 보만 걸으면", line 2 "된다고 믿다가", line 3 "2년 만에 악력 17kg,", line 4 "근감소증이 됐습니다".
All text pure white (#FFFFFF) except "만 보만" in bright yellow (#FFD400) and "근감소증" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## supplement-liver-2026-10 · thumbnail_1 — 결과지 숫자 반전

저장 위치: `health/source/supplement-liver-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위 가운데) | 몸에 좋다길래 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 노랑) |
| 처음 숫자 | 24 | 잉크 #1E1E1E | 중간 크기, 왼쪽 뒤 카드 |
| 결과 숫자 | 89 | 빨강 #E63B2E | 가장 큰 글자, 오른쪽 앞 카드 |
| 하단 1줄 | 영양제 9가지로 늘렸다가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 없음 |
| 하단 2줄 | 간수치 89가 됐다 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "89"만 빨강 #E63B2E (높아진 수치) |

- 하단 2줄 = 채택 제목 앞 문장 "몸에 좋다길래 영양제를 9가지로 늘렸다가 간수치 24가 89가 됐습니다"를 줄인 것 (제목 단어를 그대로 씀). 1줄 13자 · 2줄 10자, 합 23자 (띄어쓰기 포함)
- 펀치 "몸에 좋다길래"(7자)는 하단 2줄에 없는 말이다. 89는 위아래 모두 나온다 (숫자 반복은 허용)
- 강조 합 3곳: 노랑 상자 "몸에 좋다길래", 빨강 "89"(카드), 빨강 "89"(하단). 파랑 글자 없음

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: clean flat illustration on a cream (#F2EBDD) background. At the top center, a solid bright yellow
(#FFD400) box with the black bold text "몸에 좋다길래". Below it, two simple white medical checkup result cards overlap in
the center, with no logos, no institution names, no barcodes, no personal data and no small print. On the smaller card at
the back left, the black number "24" in medium size. A thick black arrow points from the left card to the right card, with
nothing written on or above the arrow. On the larger card in front on the right, the huge red (#E63B2E) number "89", the
largest element in the image (about 25% of the image height). No pills, no bottles, no liver or organ drawings, no people,
no needles, no hospital scenes.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "영양제 9가지로 늘렸다가", line 2 "간수치 89가 됐다". The word "89" is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, gain red #E63B2E.
Upper 60% of the frame: clean flat illustration on a cream background. An empty solid yellow box at the top center. Below
it, two simple blank white checkup result cards overlap in the center, the right one larger and in front, with a thick
black arrow from the left card to the right card. Smaller empty space on the left card and large empty space on the right
card for a big number. No logos, no barcodes, no pills, no organs, no people, no medical scenes.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, completely empty, reserved for two lines of
headline text. Nothing from the picture reaches into this band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## supplement-liver-2026-10 · thumbnail_2 — 인물·감정 장면

저장 위치: `health/source/supplement-liver-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (오른쪽 위) | 영양제 9가지 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 노랑) |
| 결과 숫자 (오른쪽) | 89 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |
| 하단 1줄 | 결과지의 간수치 24가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 없음 |
| 하단 2줄 | 2년 만에 89가 됐다 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "89"만 빨강 #E63B2E (높아진 수치) |

- 하단 2줄 = 짝 제목 T2 앞 문장 "검진 결과지의 간수치 24가 2년 만에 89가 됐습니다"를 줄인 것 (제목 단어를 그대로 씀). 1줄 12자 · 2줄 12자, 합 24자 (띄어쓰기 포함)
- 펀치 "영양제 9가지"(7자)는 하단 2줄에 없는 말이다 (T2 뒤 문장의 말). 89는 위아래 모두 나온다 (숫자 반복은 허용)
- 강조 합 3곳: 노랑 상자 "영양제 9가지", 빨강 상자 "89", 빨강 "89"(하단). 파랑 글자 없음

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A bright home kitchen table in the morning, background softly blurred in warm cream tones.
On the left 45% of the frame, a fictional Korean woman in her early 50s, office-worker look (neat blouse), seated behind
the table and shown from the waist up, holding a single health checkup result sheet in her hands, the sheet facing away
or blurred so no text is readable, surprised and worried expression looking at the paper. Her face, hands and the sheet
are all in the upper 60% of the frame. Fictional person, not resembling any real or famous person, natural Korean
features. Not a doctor, no white coat, no hospital, no needles. On the table in front of her, at about the middle height
of the frame: about nine plain white plastic supplement bottles with absolutely no labels, no text, no logos and no
brand-like colors, and a small saucer with a modest handful of pills (no pills pouring or spilling). On the upper right
side, the bold text "영양제 9가지" in ink black on a solid bright yellow (#FFD400) box. Below it, a solid red (#E63B2E)
rounded box containing the huge white bold number "89", the largest text in the image. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "결과지의 간수치 24가", line 2 "2년 만에 89가 됐다". The word "89" is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, gain red #E63B2E.
Realistic photo style. A bright home kitchen table in the morning, softly blurred cream background. On the left 45% of
the frame, a fictional Korean woman in her early 50s seated behind the table, shown from the waist up, holding a blank
health checkup sheet, surprised and worried expression, her face and hands in the upper 60% of the frame. Fictional
person, not resembling any real or famous person. Not a doctor, no hospital. On the table at about the middle height of
the frame, about nine plain white unlabeled supplement bottles and a small saucer with a modest handful of pills. On the
upper right, an empty solid yellow box and an empty solid red rounded box below it, with calm empty space around them.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, completely empty, reserved for two lines of
headline text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## supplement-liver-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `health/source/supplement-liver-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 몸에 좋다길래 | 노랑 #FFD400 (줄 전체) | 믿었던 말 |
| 2줄 | 영양제를 9가지로 | 흰색 #FFFFFF | 없음 |
| 3줄 | 늘렸다가 간수치 | 흰색 #FFFFFF | 없음 |
| 4줄 | 24가 89가 됐습니다 | 흰색 #FFFFFF | "89"만 빨강 #E63B2E — 나빠진(높아진) 결과 숫자 |

- 줄 길이 7자 · 9자 · 8자 · 12자 (띄어쓰기 포함, 모두 14자 이내). 어절 사이에서만 줄을 바꿨다
- 이어 붙이면 채택 제목 앞 문장과 한 글자도 다르지 않다: "몸에 좋다길래 영양제를 9가지로 늘렸다가 간수치 24가 89가 됐습니다". 뒤 문장("영양제 겹쳐 먹는 사람들의 공통점")은 넣지 않는다
- 숫자 반전 "24가 89가 됐습니다"가 한 줄에 온다 (마지막 줄, 가장 긴 줄)
- 강조 합 2곳 (3곳 이하). 파랑 글자 없음 (검정 위 파랑 금지)

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "몸에 좋다길래", line 2 "영양제를 9가지로", line 3 "늘렸다가 간수치", line 4 "24가 89가 됐습니다".
All text pure white (#FFFFFF) except "몸에 좋다길래" in bright yellow (#FFD400) and "89" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
