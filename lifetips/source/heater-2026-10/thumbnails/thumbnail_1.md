# heater-2026-10 썸네일 1 — 숫자 반전 (고지서 카드)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `lifetips/guides/thumbnail_rules.md` v1.0), 대본 heater-2026-10.txt v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 평소 전기요금이 한 달 만에 6배 넘게 뛴 **고지서 숫자 반전**(2만 원 → 13만 원)이 가장 클릭을 부른다 |
| 짝 제목 | `titles.md` **T1 (채택)** "보일러보다 싸다는 말에 온풍기만 틀었다가 전기요금 2만원이 13만원이 됐습니다. …" — T2·T3과도 어울림 |
| 숫자 근거 | 문장 9 "고지서에는 13만 원이 찍혀 있었어요" (0:40) · 문장 10 "평소에는 2만 원 남짓 나오던 요금이었죠" (0:45) → 모두 1분 안. 검산 22,160원 → 130,500원 (`README.md`) |

## 화면 구성
- 크림 배경 위에 화면 가운데를 크게 채우는 흰 종이 카드 한 장 (얇은 잉크색 테두리, 살짝 기울어짐) — 실제 고지서 서식·로고·고객번호·바코드·QR 없이 숫자와 단어만
- 카드 위쪽: "전기요금" (잉크, 노랑 형광펜 줄 위 — 유일한 노랑) 바로 옆에 "2만 원" (잉크, 중간 크기, 가는 줄로 지워진 느낌 없이 그대로)
- 그 아래 굵은 빨강 아래 화살표
- 카드 아래쪽 절반: 넓은 빨강 상자 안에 **"13만 원"** (흰색, 가장 큰 글자, 화면 높이의 25% 안팎)
- 인물 없음 · 오른쪽 아래 구석 비움 · 중요한 글자는 가운데 16:9 안

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위 | 전기요금 2만 원 | 잉크 #1E1E1E | "전기요금"에 노랑 형광펜 #FFD400 (유일한 강조) |
| 아래 | 13만 원 | 흰색 (빨강 #E63B2E 상자 위) | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, extra-cost red #E63B2E, saved-money blue #2D6CDF.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. A single large white paper
card, slightly tilted, with a thin ink-black outline fills the center of the frame, like a very simple monthly bill
(NOT a real utility bill: no company name, no logo, no customer number, no barcode, no QR code, no table lines).
Top part of the card: the text "전기요금 2만 원" in bold ink-black letters, with a bright yellow (#FFD400)
highlighter stripe behind the word "전기요금" only. Below it, one thick red (#E63B2E) arrow pointing down.
Lower half of the card: a wide solid red (#E63B2E) rounded box with the huge white bold text "13만 원" centered,
the largest element in the image (about a quarter of the image height). No people, no faces, no heater, no fire.
Minimal, nothing decorative. Keep all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, extra-cost red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. A single large white paper card,
slightly tilted, with a thin ink-black outline fills the center of the frame (no company name, no logo, no barcode,
no QR code, no table lines). Top part of the card: empty space for one line of text with a short bright yellow
highlighter stripe at its left. Below it, one thick red arrow pointing down. Lower half of the card: a wide empty
solid red (#E63B2E) rounded box. No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "전기요금 2만 원" · "13만 원"이 한 글자도 틀리지 않음 (문장 9·10, 제목 T1과 같은 숫자)
- [ ] 320px 축소본에서 "13만 원"이 바로 읽힘 · 노랑 강조 1곳("전기요금") · 더 나간 돈은 빨강
- [ ] 실제 고지서처럼 보이지 않음 (전력회사 이름·로고·고객번호·바코드·QR·표 서식 없음)
- [ ] 문구가 제목을 그대로 반복하지 않음 (제목의 "보일러보다 싸다는 말에"·"불편한 진실"은 넣지 않음)
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
