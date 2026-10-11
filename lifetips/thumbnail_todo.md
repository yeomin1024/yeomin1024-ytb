# lifetips 썸네일 만들 목록 (이미지 없는 것)

자동 생성 — `python tools/make_summary.py --thumb-todo lifetips` (2026-10-11 08:41)

1. [A] 프롬프트를 이미지 AI에 넣는다. 한글이 틀리면 [B]로 만들고 문구표대로 글자를 얹는다.
2. 이미지를 아래 '저장 위치'로 GitHub에 올린다 (크기는 업로드 때 1280×720으로 자동 변환).

남은 썸네일: 9개

## bleach-2026-10 · thumbnail_1 — 숫자 반전 (1분 → 응급실 4시간)

저장 위치: `lifetips/source/bleach-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 펀치 (작은 카드) | 1분 꿀팁 | "1분" 파랑 #2D6CDF / "꿀팁" 잉크 #1E1E1E | "꿀팁"에 노랑 형광펜 #FFD400 (글자 전체 높이) |
| 위쪽 핵심 숫자 | 응급실 4시간 | 흰색 (빨강 #E63B2E 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 락스에 세정제까지 뿌렸다가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | — |
| 하단 2줄 | 응급실에서 4시간 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 줄 전체 "응급실에서 4시간" 빨강 #E63B2E (위험 결과) |

- 길이: 펀치 5자 · 하단 1줄 14자 · 하단 2줄 9자 (2줄 합 23자)
- 강조 합 3곳: 노랑 형광펜 "꿀팁" · 빨강 상자 "응급실 4시간" · 하단 빨강 "응급실에서 4시간"

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, safe blue #2D6CDF, cost red #E63B2E.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain.
Upper-left area: a small light-cream rounded card with a thin black outline, containing a simple line-drawing stopwatch
icon (no numerals, no marks with digits) and next to it the text "1분 꿀팁" in bold blue (#2D6CDF); only the word "꿀팁"
is in ink black on a bright yellow (#FFD400) highlighter box of full letter height. A single thick ink-black arrow goes
from the small card down to the right. Upper-right area, still inside the upper 60%: a wide solid red (#E63B2E) rounded
box with the huge white bold text "응급실 4시간", the largest text in the image, with "4시간" slightly larger.
No people, no faces, no hospital, no ambulance, no medical cross, no bottles, no spray, no pouring, no smoke.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "락스에 세정제까지 뿌렸다가", line 2 "응급실에서 4시간". The words "응급실에서 4시간" in line 2 are red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Minimal, nothing decorative. Keep all text and key elements inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, safe blue #2D6CDF, cost red #E63B2E.
Upper 60% of the frame: clean flat editorial graphic on a cream paper background with subtle paper grain. Upper-left:
a small light-cream rounded card with a thin black outline containing a simple line-drawing stopwatch icon without
numerals, with empty space to its right for a short headline. A single thick ink-black arrow goes down to the right.
Upper-right, inside the upper 60%: a wide empty solid red (#E63B2E) rounded box. No people, no hospital, no ambulance,
no bottles, no smoke.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, with clean empty space for two lines of
large left-aligned headline text. Nothing else in the lower third. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## bleach-2026-10 · thumbnail_2 — 인물·감정 장면 (욕실 문 앞)

저장 위치: `lifetips/source/bleach-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 핵심 숫자 | 응급실 4시간 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |
| 하단 1줄 | 문 닫고 락스 뿌렸다가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | — |
| 하단 2줄 | 1분 꿀팁이 응급실 4시간 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "1분"만 노랑 #FFD400 글자 (꿀팁이 약속한 시간) |

- 길이: 하단 1줄 12자 · 하단 2줄 14자 (2줄 합 26자) · 펀치 없음
- 하단 2줄은 짝 제목 T2 앞 문장을 줄인 것 ("욕실 문 닫고 락스를 뿌렸다가" → "문 닫고 락스 뿌렸다가", "응급실 4시간이 됐습니다" → "응급실 4시간")
- 강조 합 2곳: 빨강 상자 "응급실 4시간" · 하단 노랑 "1분"

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, safe blue #2D6CDF, cost red #E63B2E.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: realistic photo style, soft natural light. A home hallway right outside a small bright
white-tiled bathroom; the bathroom door is half open behind her and the clean white tile grout inside is softly blurred.
On the left 45% of the frame, a fictional Korean woman in her late 40s in comfortable home clothes, shown from the chest
up, covering her mouth with one hand while coughing, eyes slightly watery, embarrassed and regretful expression.
Fictional person, not resembling any real or famous person, natural Korean features. She is standing upright and steady.
No cleaning bottles, no spray bottles, no pouring, no mixing, no smoke, no fumes, no hospital, no ambulance, no oxygen
mask, nobody lying down. On the right side, inside the upper 60%, a wide solid red (#E63B2E) rounded box containing the
huge white bold text "응급실 4시간", the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "문 닫고 락스 뿌렸다가", line 2 "1분 꿀팁이 응급실 4시간". The word "1분" in line 2 is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep face and text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, cost red #E63B2E.
Upper 60% of the frame: realistic photo style, soft natural light. A home hallway right outside a small bright
white-tiled bathroom, the door half open behind her with clean white tile grout softly blurred. On the left 45% of the
frame, a fictional Korean woman in her late 40s in comfortable home clothes, shown from the chest up, covering her mouth
with one hand while coughing, eyes slightly watery, embarrassed and regretful expression, standing upright.
Fictional person, not resembling any real or famous person. No bottles, no smoke, no hospital, no oxygen mask.
On the right, inside the upper 60%, an empty wide solid red (#E63B2E) rounded box.
Lower third: a dark band that fades upward from the bottom edge across the full width, with clean empty space for two
lines of large left-aligned headline text. Nothing else in the lower third. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## bleach-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `lifetips/source/bleach-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 글자 수 | 색 |
|---|---|---|---|
| 1 | 1분이면 녹는다는 말에 | 12 | 흰색 #FFFFFF, **"1분"만 노랑 #FFD400** (꿀팁이 약속한 시간) |
| 2 | 락스에 세정제까지 뿌렸다가 | 14 | 흰색 #FFFFFF |
| 3 | 응급실에서 4시간을 | 10 | 흰색 #FFFFFF, **"응급실에서 4시간"만 빨강 #E63B2E** (위험 결과, 조사 "을"은 흰색) |
| 4 | 보냈습니다 | 5 | 흰색 #FFFFFF |

- 4줄을 띄어쓰기 하나로 이으면 "1분이면 녹는다는 말에 락스에 세정제까지 뿌렸다가 응급실에서 4시간을 보냈습니다" = 채택 제목 앞 문장 (끝 "." 제외)
- 강조 2곳 (노랑 "1분" · 빨강 "응급실에서 4시간") — 3곳 이하. 2줄(행동)은 강조하지 않는다 (섞는 행동을 눈에 띄게 하지 않음). 파랑 글자는 쓰지 않는다 (검정 위에서 안 읽힘)

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "1분이면 녹는다는 말에", line 2 "락스에 세정제까지 뿌렸다가", line 3 "응급실에서 4시간을", line 4 "보냈습니다".
All text pure white (#FFFFFF) except "1분" in bright yellow (#FFD400) and "응급실에서 4시간" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## heater-2026-10 · thumbnail_1 — 숫자 반전 (고지서 카드)

저장 위치: `lifetips/source/heater-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 펀치 (카드 위) | 전기요금 2만 원 | 잉크 #1E1E1E | "전기요금"에 노랑 형광펜 #FFD400 (글자 전체 높이) |
| 위쪽 핵심 숫자 | 13만 원 | 흰색 (빨강 #E63B2E 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 보일러보다 싸다는 말에 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | — |
| 하단 2줄 | 온풍기 틀었다가 13만 원 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "13만 원"만 빨강 #E63B2E (더 나간 돈) |

- 길이: 펀치 9자 · 하단 1줄 12자 · 하단 2줄 14자 (2줄 합 26자)
- 하단 2줄은 채택 제목 앞 문장을 줄인 것 ("온풍기만 틀었다가" → "온풍기 틀었다가", "전기요금 2만원이 13만원이 됐습니다" → "13만 원" — 2만 원·전기요금은 위쪽 카드에 있음)
- 강조 합 3곳: 노랑 형광펜 "전기요금" · 빨강 상자 "13만 원" · 하단 빨강 "13만 원"

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, extra-cost red #E63B2E, saved-money blue #2D6CDF.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain.
A single white paper card, slightly tilted, with a thin ink-black outline, scaled down so it fits entirely inside the
upper 60% of the frame, like a very simple monthly bill (NOT a real utility bill: no company name, no logo, no customer
number, no barcode, no QR code, no table lines).
Top part of the card: the text "전기요금 2만 원" in bold ink-black letters, with a bright yellow (#FFD400) highlighter
box of full letter height behind the word "전기요금" only. Below it, one thick ink-black arrow pointing down.
Lower part of the card: a wide solid red (#E63B2E) rounded box with the huge white bold text "13만 원" centered,
the largest text in the image (about a quarter of the image height). No people, no faces, no heater, no fire.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "보일러보다 싸다는 말에", line 2 "온풍기 틀었다가 13만 원". The word "13만 원" in line 2 is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Minimal, nothing decorative. Keep all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, extra-cost red #E63B2E.
Upper 60% of the frame: clean flat editorial graphic on a cream paper background with subtle paper grain. A single white
paper card, slightly tilted, with a thin ink-black outline, scaled down to fit inside the upper 60% (no company name,
no logo, no barcode, no QR code, no table lines). Top part of the card: empty space for one line of text with a short
bright yellow highlighter box at its left. Below it, one thick ink-black arrow pointing down. Lower part of the card:
a wide empty solid red (#E63B2E) rounded box. No people.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, with clean empty space for two lines of
large left-aligned headline text. Nothing else in the lower third. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## heater-2026-10 · thumbnail_2 — 인물·감정 장면 (고지서를 본 사연자)

저장 위치: `lifetips/source/heater-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 펀치 | 온풍기 한 달 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (글자 전체 높이, 노랑 상자는 이곳만) |
| 위쪽 핵심 숫자 | 13만 원 | 빨강 #E63B2E (네이비 위, 흰 외곽선) | 가장 큰 글자 |
| 하단 1줄 | 가스비 3만 원 아끼려다 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "3만 원"만 노랑 #FFD400 글자 (아끼려던 돈) |
| 하단 2줄 | 전기요금 13만 원 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | — |

- 길이: 펀치 7자 · 하단 1줄 13자 · 하단 2줄 10자 (2줄 합 23자)
- 하단 2줄은 짝 제목 T2 앞 문장을 줄인 것 ("아끼려고 켠 온풍기 하나에" → "아끼려다", 대본 문장 13과 같은 말)
- 강조 합 3곳: 노랑 상자 "온풍기 한 달" · 빨강 "13만 원" · 하단 노랑 "3만 원"

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, extra-cost red #E63B2E, saved-money blue #2D6CDF.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame, left 55%: a realistic photo of a small, plain studio apartment in winter. A fictional Korean woman
in her late twenties (fictional person, not resembling any real or famous person, natural Korean features, realistic
photo style), shown from the chest up, with a gray blanket wrapped around her shoulders, holding a single sheet of blank
white paper with both hands and staring at it, frozen in shock and regret, mouth slightly open. Beside her is a generic
plain white box-shaped electric fan heater with no brand, no logo and no visible buttons, giving off only a faint warm
orange glow (no flames, no fire, no smoke). Soft natural indoor light.
Upper 60% of the frame, right 45%: solid dark navy (#14213D) panel with two stacked blocks of Korean text:
top "온풍기 한 달" in bold ink-black letters on a bright yellow (#FFD400) box that covers the full height of the letters;
below it "13만 원" in huge bold red (#E63B2E) letters with a thin white outline, the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "가스비 3만 원 아끼려다", line 2 "전기요금 13만 원". The word "3만 원" in line 1 is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep her face and all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, extra-cost red #E63B2E.
Upper 60% of the frame, left 55%: a realistic photo of a small plain studio apartment in winter. A fictional Korean woman
in her late twenties (fictional person, not resembling any real or famous person, natural Korean features, realistic
photo style), shown from the chest up, with a gray blanket around her shoulders, holding a single blank white sheet of
paper with both hands, frozen in shock and regret. Beside her, a generic plain white box-shaped electric fan heater with
no brand or logo and only a faint warm orange glow (no flames, no fire, no smoke).
Upper 60% of the frame, right 45%: an empty solid dark navy (#14213D) panel with a short empty bright yellow box near the
top and wide empty space below it for a large number.
Lower third: a dark band that fades upward from the bottom edge across the full width, with clean empty space for two
lines of large left-aligned headline text. Nothing else in the lower third. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## heater-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `lifetips/source/heater-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 글자 수 | 색 |
|---|---|---|---|
| 1 | 보일러보다 싸다는 말에 | 12 | 흰색 #FFFFFF |
| 2 | 온풍기만 틀었다가 전기요금 | 14 | 흰색 #FFFFFF |
| 3 | 2만원이 13만원이 | 10 | 흰색 #FFFFFF, **"2만원"만 노랑 #FFD400** (평소 요금 — 반전 전 숫자), **"13만원"만 빨강 #E63B2E** (더 나간 돈) |
| 4 | 됐습니다 | 4 | 흰색 #FFFFFF |

- 4줄을 띄어쓰기 하나로 이으면 "보일러보다 싸다는 말에 온풍기만 틀었다가 전기요금 2만원이 13만원이 됐습니다" = 채택 제목 앞 문장 (끝 "." 제외)
- 강조 2곳 (노랑 "2만원" · 빨강 "13만원") — 3곳 이하. 파랑 글자는 쓰지 않는다 (검정 위에서 안 읽힘)

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "보일러보다 싸다는 말에", line 2 "온풍기만 틀었다가 전기요금", line 3 "2만원이 13만원이", line 4 "됐습니다".
All text pure white (#FFFFFF) except "2만원" in bright yellow (#FFD400) and "13만원" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## washer-2026-10 · thumbnail_1 — 숫자 반전 (영수증 카드)

저장 위치: `lifetips/source/washer-2026-10/thumbnails/thumbnail_1.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 펀치 (영수증 위) | 12만 원 아끼려다 | "12만 원" 파랑 #2D6CDF / "아끼려다" 잉크 #1E1E1E | "아끼려다"에 노랑 형광펜 #FFD400 (글자 전체 높이) |
| 위쪽 핵심 숫자 | 21만 원 | 흰색 (빨강 #E63B2E 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 세탁기 직접 분해했다가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | — |
| 하단 2줄 | 수리비 21만 원 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "21만 원"만 빨강 #E63B2E (더 나간 돈) |

- 길이: 펀치 10자 · 하단 1줄 12자 · 하단 2줄 9자 (2줄 합 21자)
- 강조 합 3곳: 노랑 형광펜 "아끼려다" · 빨강 상자 "21만 원" · 하단 빨강 "21만 원"

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, saved-money blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain.
In the upper center, a plain white paper receipt with a torn zigzag bottom edge, slightly tilted, scaled down so it
fits entirely inside the upper 60% of the frame (a generic receipt, NOT any real company's service form: no logo,
no company name, no barcode, no QR code, no table lines).
Top part of the receipt: the text "12만 원" in large blue (#2D6CDF) bold letters, followed on the same line by the word
"아끼려다" in black bold letters over a bright yellow (#FFD400) highlighter box covering the full letter height.
Below it, one thick ink-black arrow pointing down.
The lower part of the receipt is a wide solid red (#E63B2E) rounded box with the huge white bold text "21만 원",
the largest text in the image, about a quarter of the frame height.
Optionally, behind the receipt, a soft out-of-focus top of a plain generic white top-loading washing machine with no
brand, no logo and no button layout from a real product. No people, no hands, no tools.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "세탁기 직접 분해했다가", line 2 "수리비 21만 원". The word "21만 원" in line 2 is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep all text inside the central 16:9 safe area. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, saved-money blue #2D6CDF, loss red #E63B2E.
Upper 60% of the frame: clean flat editorial graphic on a cream paper background with subtle paper grain. In the upper
center, a plain white paper receipt with a torn zigzag bottom edge, slightly tilted, scaled down to fit inside the
upper 60%, with no logo, no barcode, no QR code and no form lines. Top part of the receipt: empty space for one line of
text and a short bright yellow highlighter box on the right of that line. Below it one thick ink-black arrow pointing
down. The lower part of the receipt is a wide empty solid red (#E63B2E) rounded box. Optionally a soft out-of-focus top
of a plain generic white top-loading washing machine behind it, no brand. No people, no tools.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, with clean empty space for two lines of
large left-aligned headline text. Nothing else in the lower third. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## washer-2026-10 · thumbnail_2 — 인물·감정 장면 (손바닥의 나사 몇 개)

저장 위치: `lifetips/source/washer-2026-10/thumbnails/thumbnail_2.png`

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 펀치 | 30분이면 된다더니 | 검정 #1E1E1E | 노랑 상자 #FFD400 (글자 전체 높이, 노랑은 이곳만) |
| 위쪽 핵심 숫자 | 21만 원 | 흰색 (빨강 #E63B2E 상자) | 가장 큰 글자 |
| 하단 1줄 | 영상만 믿고 뜯었다가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | — |
| 하단 2줄 | 통돌이 수리비 21만 원 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "21만 원"만 빨강 #E63B2E (더 나간 돈) |

- 길이: 펀치 10자 · 하단 1줄 11자 · 하단 2줄 13자 (2줄 합 24자)
- 강조 합 3곳: 노랑 상자 "30분이면 된다더니" · 빨강 상자 "21만 원" · 하단 빨강 "21만 원"

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, saved-money blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style, bright small Korean apartment utility room with cream and white tones, soft daylight.
On the left 45% of the frame, in the upper 60% of the image, a fictional Korean woman in her late 30s wearing simple
comfortable homewear, shown from the chest up, looking down at her open palm that holds three or four small silver screws,
with a puzzled, regretful, slightly deflated expression (no crying, no fear).
Fictional person, not resembling any real or famous person, natural Korean features.
Behind her, a plain generic white top-loading washing machine with its lid open, fully assembled and intact
(no brand, no logo, no copied button layout of any real product). No tools in use, no cables, no water, no mess.
In the upper right, a solid bright yellow (#FFD400) box with the black bold text "30분이면 된다더니", and below it
a wide solid red (#E63B2E) rounded box with the huge white bold text "21만 원", the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "영상만 믿고 뜯었다가", line 2 "통돌이 수리비 21만 원". The word "21만 원" in line 2 is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

<details><summary>[B] 글자 없는 프롬프트</summary>

```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, loss red #E63B2E.
Realistic photo style, bright small Korean apartment utility room with cream and white tones, soft daylight.
On the left 45% of the frame, in the upper 60% of the image, a fictional Korean woman in her late 30s in simple homewear,
shown from the chest up, looking down at her open palm holding three or four small silver screws, puzzled and regretful
expression. Fictional person, not resembling any real or famous person. Behind her a plain generic white top-loading
washing machine with its lid open, fully assembled, no brand or logo. No tools in use, no water. The upper right of the
frame is calm empty wall space, with an empty bright yellow box near the top right and an empty wide solid red (#E63B2E)
rounded box below it, both inside the upper 60%.
Lower third: a dark band that fades upward from the bottom edge, with clean empty space for two lines of large
left-aligned headline text. Nothing else in the lower third. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
</details>

## washer-2026-10 · thumbnail_3 — 검은 배경 제목형 (채택 제목 문구)

저장 위치: `lifetips/source/washer-2026-10/thumbnails/thumbnail_3.png`

| 줄 | 문구 | 글자 수 | 색 |
|---|---|---|---|
| 1 | 업체비 12만원 아끼려고 | 13 | 흰색 #FFFFFF, **"12만원"만 노랑 #FFD400** (아끼려던 돈) |
| 2 | 세탁기를 직접 분해했다가 | 13 | 흰색 #FFFFFF |
| 3 | 수리비 21만원이 | 9 | 흰색 #FFFFFF, **"21만원"만 빨강 #E63B2E** (더 나간 돈) |
| 4 | 나왔습니다 | 5 | 흰색 #FFFFFF |

- 4줄을 띄어쓰기 하나로 이으면 "업체비 12만원 아끼려고 세탁기를 직접 분해했다가 수리비 21만원이 나왔습니다" = 채택 제목 앞 문장 (끝 "." 제외)
- 강조 2곳 (노랑 "12만원" · 빨강 "21만원") — 3곳 이하. 파랑 글자는 쓰지 않는다 (검정 위에서 안 읽힘)
- 이 문장은 4줄에 한 줄 14자 이내로 나뉜다. 3줄로는 마지막 줄이 "수리비 21만원이 나왔습니다"(15자)가 되어 4줄로 했다. "수리비 21만원이"는 한 줄에 둔다

[A] 완성형 프롬프트

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "업체비 12만원 아끼려고", line 2 "세탁기를 직접 분해했다가", line 3 "수리비 21만원이", line 4 "나왔습니다".
All text pure white (#FFFFFF) except "12만원" in bright yellow (#FFD400) and "21만원" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
