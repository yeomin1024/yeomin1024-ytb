# prediabetes-2026-10 썸네일 2 — 인물·감정 장면

버전: v1.0 — 2026-10-10 — 최초 작성 (`health/guides/thumbnail_rules.md` v1.0 3번: 가상 인물, 의사·병원 장면 금지)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 결과지를 든 **사람의 표정**이 숫자 카드보다 감정을 더 끈다 |
| 짝 제목 | `titles.md` T2 "아픈 데 없다며 넘긴 공복혈당 108이 3년 만에 131이 됐습니다 …" |
| 숫자 근거 | 문장 4 "아픈 데도 없고" · 문장 8 "공복혈당 131" (0:33) |

## 화면 구성
- 크림색 사무실 배경을 흐리게. 왼쪽 40~45%: **가상 인물** — 50대 초반 한국인 남성 직장인(셔츠, 넥타이 느슨하게), 건강검진 결과지 한 장을 두 손으로 들고 놀라고 걱정스러운 표정
  - 종이에는 글자가 보이지 않는다 (뒷면 또는 흐림)
- 오른쪽: 위에 **"괜찮다고?"** (잉크 글자, "괜찮다고"만 노랑 상자), 아래에 빨강 상자 안 흰 글자 **"131"** (가장 큼)
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 속마음 | 괜찮다고? | 잉크 #1E1E1E ("괜찮다고"만 노랑 상자) | 노랑 상자 (글자 전체 높이) |
| 결과 | 131 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |

## [A] 완성형 프롬프트
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Softly blurred bright office background in warm cream tones. On the left 40% of the frame, a
fictional Korean man in his early 50s, office-worker look (white shirt, loosened tie), holding a single health checkup
result sheet with both hands, the sheet facing away or blurred so no text is readable, surprised and worried expression
looking at the paper. Fictional person, not resembling any real or famous person, natural Korean features. Not a doctor,
no white coat, no hospital, no needles. On the right side, large bold headline text "괜찮다고?" in ink black, where only
the word "괜찮다고" sits on a solid bright yellow (#FFD400) box. Below it, a wide solid red (#E63B2E) rounded box containing
the huge white bold number "131", the largest element. No crying, no extreme fear.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, gain red #E63B2E.
Realistic photo style. Softly blurred bright office background. On the left 40% of the frame, a fictional Korean man in
his early 50s, office-worker look, holding a blank health checkup sheet with both hands, surprised and worried
expression. Fictional person, not resembling any real or famous person. Not a doctor, no hospital. The right 55% of the
frame is calm empty space for headline text, with an empty solid red (#E63B2E) rounded box in the lower right-middle.
Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "괜찮다고?" · "131"이 한 글자도 틀리지 않음 · 결과지에 읽히는 글자 없음
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 의사·흰 가운·병원·주사 없음 · 표정은 놀람·걱정 수준
- [ ] 320px 축소본에서 표정과 "131"이 읽힘 · 노랑 강조 1곳 · 오른쪽 아래 비어 있음

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
