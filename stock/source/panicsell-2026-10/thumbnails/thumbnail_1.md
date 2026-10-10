# panicsell-2026-10 썸네일 1 — 숫자 반전 (판 금액 → 판 뒤 반등)

버전: v1.0 — 2026-10-10 — 최초 작성 (`guides/thumbnail_guide.md` v1.1, `stock/guides/thumbnail_rules.md` v1.1), 대본 v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "-800만 원에 팔았는데 그 뒤 +30%"라는 **판 뒤 반등의 숫자 대비**가 가장 클릭을 부른다 (판 사람의 후회를 숫자 두 개로) |
| 짝 제목 | `titles.md` **T1 (채택)** "하락장이 무서워 -800만원에 다 팔았는데 …" — T3과도 어울림 |
| 숫자 근거 | 문장 9 "-800만 원이 넘어" (0:39) · 문장 11 "장 마감 직전 모두 팔았어요" (0:49) · 문장 13 "판 가격보다 30% 넘게" (0:59) → 모두 1분 안 |

## 화면 구성
- 크림 배경 위에 화면의 대부분을 채우는 밝은 크림색 카드 (얇은 검정 테두리, 둥근 모서리) — 영상의 계좌 카드와 같은 모양
- 카드 왼쪽 절반: 파랑 상자 안 **"-800만 원"** (흰 글자, 크게) + 그 아래 "전부 매도" (검정 글자 + 노랑 형광펜)
- 카드 오른쪽 절반: 왼쪽 아래에서 오른쪽 위로 크게 올라가는 굵은 빨강 화살표 + 그 끝에 **"+30%"** (빨강, 가장 큰 글자)
- 오른쪽 아래 구석은 비움 · 인물 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 판 금액 | -800만 원 | 흰색 (파랑 #2D6CDF 상자 위) | — |
| 라벨 | 전부 매도 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (유일한 강조) |
| 판 뒤 | +30% | 빨강 #E63B2E | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. A large light-cream rounded
rectangle card with a thin black outline fills most of the frame, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos). On the left half of the card: a solid blue (#2D6CDF) rounded
box with the large white bold text "-800만 원", and below it the label "전부 매도" in black bold letters over a bright
yellow (#FFD400) highlighter stripe. On the right half of the card: a thick red (#E63B2E) arrow rising steeply from the
lower left to the upper right, ending at the huge red bold text "+30%", the largest element in the image.
No people, no faces. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. A large light-cream rounded rectangle
card with a thin black outline fills most of the frame. Left half: an empty solid blue (#2D6CDF) rounded box and a short
bright yellow highlighter stripe below it. Right half: a thick red arrow rising steeply from lower left to upper right,
with empty space at its tip for a number. No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "-800만 원" · "전부 매도" · "+30%"가 한 글자도 틀리지 않음 (문장 9·11·13과 같은 숫자)
- [ ] 320px 축소본에서 "+30%"와 "-800만 원"이 바로 읽힘 · 노랑 강조 1곳 · 손실은 파랑, 상승은 빨강
- [ ] 증권사 앱처럼 보이지 않음 (앱 이름·로고·실제 화면 배치 없음) · 종목명 없음
- [ ] 오른쪽 아래 비어 있음 (화살표 끝 "+30%"는 오른쪽 위) · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
