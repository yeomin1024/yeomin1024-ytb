# bittu-2026-10 썸네일 1 — 숫자 반전 (계좌 카드)

버전: v1.0 — 2026-10-10 — 최초 작성 (`guides/thumbnail_guide.md` v1.1, `stock/guides/thumbnail_rules.md` v1.1), 대본 v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 수익이 손실로 뒤집힌 **계좌 숫자 반전**과 결정적 장면 한 단어("반대매매")가 가장 클릭을 부른다 |
| 짝 제목 | `titles.md` **T1 (채택)** "신용까지 써서 번 1,500만원이 반대매매 한 번에 …" — T3과도 어울림 |
| 숫자 근거 | 문장 5 "수익이 1,500만 원이 됐어요" (0:22) · 문장 10 "제 주식이 전부 강제로 팔렸어요" (0:47) · 문장 11 "-2,500만 원이었어요" (0:53) → 모두 1분 안 |

## 화면 구성
- 크림 배경 위에 화면의 대부분을 채우는 밝은 크림색 카드 (얇은 검정 테두리, 둥근 모서리) — 영상의 계좌 카드와 같은 모양
- 카드 왼쪽 위: "+1,500만 원" (빨강, 중간 크기)
- 그 아래 굵은 파랑 아래 화살표, 화살표 옆에 "반대매매" (검정 글자 + 노랑 형광펜)
- 카드 아래쪽 절반: 넓은 파랑 상자 안에 **"-2,500만 원"** (흰색, 가장 큰 글자)
- 오른쪽 아래 구석은 비움 · 인물 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 시작 | +1,500만 원 | 빨강 #E63B2E | — |
| 라벨 | 반대매매 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (유일한 강조) |
| 결과 | -2,500만 원 | 흰색 (파랑 상자 위) | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. A large light-cream rounded
rectangle card with a thin black outline fills most of the frame, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos). Inside the card, top-left: the text "+1,500만 원" in large
red (#E63B2E) bold letters. Below it, a thick blue arrow pointing down, and to the right of the arrow the label
"반대매매" in black bold letters over a bright yellow (#FFD400) highlighter stripe. The lower half of the card is a wide
solid blue (#2D6CDF) rounded box with the huge white bold text "-2,500만 원" centered, the largest element in the image.
No people, no faces. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. A large light-cream rounded rectangle
card with a thin black outline fills most of the frame. Inside: empty space at the top-left for a number, a thick blue
arrow pointing down below it, a short bright yellow highlighter stripe to the right of the arrow, and a wide empty solid
blue (#2D6CDF) rounded box across the lower half of the card. No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "+1,500만 원" · "반대매매" · "-2,500만 원"이 한 글자도 틀리지 않음 (문장 5·10·11과 같은 숫자)
- [ ] 320px 축소본에서 "-2,500만 원"이 바로 읽힘 · 노랑 강조 1곳 · 수익은 빨강, 손실은 파랑
- [ ] 증권사 앱처럼 보이지 않음 (앱 이름·로고·실제 화면 배치 없음) · 종목명 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
