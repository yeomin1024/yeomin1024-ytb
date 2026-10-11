# heater-2026-10 썸네일 1 — 숫자 반전 (고지서 카드)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) · `lifetips/guides/thumbnail_rules.md` v1.1, 대본 heater-2026-10.txt v1.0 기준 (v1.0: 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 평소 전기요금이 한 달 만에 6배 넘게 뛴 **고지서 숫자 반전**(2만 원 → 13만 원)이 가장 클릭을 부른다 |
| 짝 제목 | `titles.md` **T1 (채택)** "보일러보다 싸다는 말에 온풍기만 틀었다가 전기요금 2만원이 13만원이 됐습니다. …" — T2·T3과도 어울림 |
| 숫자 근거 | 문장 9 "고지서에는 13만 원이 찍혀 있었어요" (0:40) · 문장 10 "평소에는 2만 원 남짓 나오던 요금이었죠" (0:45) → 모두 1분 안. 검산 22,160원 → 130,500원 (`README.md`) |

## 화면 구성
- **위쪽 약 60% (y 0~430)** — 크림 배경 위, 가운데에 줄여 놓은 흰 종이 카드 한 장 (얇은 잉크색 테두리, 살짝 기울어짐) — 실제 고지서 서식·로고·고객번호·바코드·QR 없이 숫자와 단어만
  - 카드 위쪽: 펀치 문구 "전기요금 2만 원" (잉크, 중간 크기) — "전기요금"에만 노랑 형광펜
  - 그 아래 굵은 잉크색 아래 화살표 하나 (빨강은 숫자에만 씀)
  - 카드 아래쪽: 넓은 빨강 상자 안에 **"13만 원"** (흰색, 가장 큰 글자, 화면 높이의 25% 안팎 — 하단 2줄보다 크게)
- **아래쪽 약 35% (y 약 450~690)** — 아래에서 위로 옅어지는 다크 네이비 띠 위에 하단 제목 2줄, 왼쪽 정렬(x 48부터): "보일러보다 싸다는 말에" / "온풍기 틀었다가 13만 원" ("13만 원"만 빨강)
- 인물 없음 · 온풍기·불꽃 없음 · 오른쪽 아래 구석(약 220×70px) 비움 — 2번째 줄은 x 1040 안에서 끝남 · 중요한 글자는 가운데 16:9 안

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 펀치 (카드 위) | 전기요금 2만 원 | 잉크 #1E1E1E | "전기요금"에 노랑 형광펜 #FFD400 (글자 전체 높이) |
| 위쪽 핵심 숫자 | 13만 원 | 흰색 (빨강 #E63B2E 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 보일러보다 싸다는 말에 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | — |
| 하단 2줄 | 온풍기 틀었다가 13만 원 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "13만 원"만 빨강 #E63B2E (더 나간 돈) |

- 길이: 펀치 9자 · 하단 1줄 12자 · 하단 2줄 14자 (2줄 합 26자)
- 하단 2줄은 채택 제목 앞 문장을 줄인 것 ("온풍기만 틀었다가" → "온풍기 틀었다가", "전기요금 2만원이 13만원이 됐습니다" → "13만 원" — 2만 원·전기요금은 위쪽 카드에 있음)
- 강조 합 3곳: 노랑 형광펜 "전기요금" · 빨강 상자 "13만 원" · 하단 빨강 "13만 원"

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
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

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
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

## 검수
- [ ] "전기요금 2만 원" · "13만 원" · "보일러보다 싸다는 말에" · "온풍기 틀었다가 13만 원"이 한 글자도 틀리지 않음 (문장 9·10, 제목 T1과 같은 숫자)
- [ ] 아래쪽 약 35% 안에 하단 2줄이 크게 있음 (12자·14자, 한 줄 14자·합 26자 이내) · 줄바꿈 위치가 "문구" 표와 같음 · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 위쪽 펀치 문구는 "전기요금 2만 원" 1개(9자)뿐이고 하단 2줄과 같은 말이 없음 · 카드와 숫자가 위쪽 60% 안에 있어 하단 2줄을 가리지 않음
- [ ] 320px 축소본에서 "13만 원"과 하단 2줄이 바로 읽힘 · 노랑·빨강 강조 합 3곳 (노랑 형광펜 1곳, "전기요금") · 더 나간 돈은 빨강
- [ ] 실제 고지서처럼 보이지 않음 (전력회사 이름·로고·고객번호·바코드·QR·표 서식 없음)
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
