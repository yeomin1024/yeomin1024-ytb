# bonjeon-2026-10 썸네일 1 — 숫자 반전 (계좌 카드)

버전: v1.0 — 2026-10-12 — 최초 작성 (`guides/thumbnail_guide.md` v1.3.1, `stock/guides/thumbnail_rules.md` v2.0), 대본 bonjeon-2026-10.txt v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 작은 손실 **-200만 원이 반년 만에 -1,600만 원**(8배)으로 커진 **계좌 숫자 반전**이 가장 클릭을 부른다 |
| 짝 제목 | `titles.md` **T1 (채택)** "본전만 오면 팔겠다고 버티다가 -200만원이 -1,600만원이 됐습니다. …" — T2·T3과도 어울림 |
| 숫자 근거 | 문장 1 "본전만 오면 판다던 -200만 원이, -1,600만 원이 됐어요" (0:00) · 문장 3 "2주 만에 -200만 원" (0:10) · 문장 6 "반년을 버텼을까요" (0:23) → 모두 사연 30초 안 (추정 SRT 기준, 오디오에 맞춘 뒤 다시 확인). 검산: README "사연 검산" (-200.3만 원, -1,602.2만 원) |

## 화면 구성
- 크림 배경.
- **위쪽 약 60%** (y 0~430): 가로로 긴 밝은 크림색 카드 (얇은 검정 테두리, 둥근 모서리) — 영상의 계좌 카드와 같은 모양
  - 카드 왼쪽: **"-200만 원"** (파랑 글자 #2D6CDF, 중간 크기 — 작은 손실)
  - 카드 가운데: 오른쪽 아래로 길게 미끄러져 내려가는 굵은 파랑 화살표 (계단처럼 몇 번 꺾이며 내려감 — "계단식 하락"), 화살표 위에 펀치 "반년 만에" (검정 글자 + 노랑 형광펜)
  - 카드 오른쪽: 파랑 상자 안 **"-1,600만 원"** (흰색, 가장 큰 글자 — 화면 높이 약 20%)
- **아래쪽 약 35%** (y 약 450~690): 아래에서 위로 옅어지는 다크 네이비 띠 위에 하단 제목 2줄
  - 왼쪽 정렬 x 48부터, 글자 크기 약 95px. 2번째 줄 끝은 x 약 800 → x 1040 안
- 오른쪽 아래 구석은 비움 · 인물 없음 · 종목명·티커 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 시작 숫자 | -200만 원 | 파랑 #2D6CDF | 손실 = 파랑 (빨강 금지) |
| 펀치 (위쪽) | 반년 만에 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (노랑 상자는 이 1곳만) |
| 카드 결과 숫자 | -1,600만 원 | 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 본전 기다린 -200만원이 | 흰색 + 검정 외곽선 | — (14자) |
| 하단 2줄 | -1,600만원이 됐다 | 흰색 + 검정 외곽선 | "-1,600만원"만 노랑 #FFD400 (12자, 2줄 합 26자) |

- 강조색 2곳: 노랑 형광펜 "반년 만에", 노랑 글자 "-1,600만원". 손실 숫자는 빨강으로 쓰지 않는다 (카드는 파랑, 하단은 노랑 — `stock/guides/thumbnail_rules.md` 1번).
- 하단 2줄은 T1 앞 문장("본전만 오면 팔겠다고 버티다가 -200만원이 -1,600만원이 됐습니다")을 줄인 것. 2줄 합 26자 안에 넣으려고 "본전만 오면 팔겠다고 버티다가"를 "본전 기다린"으로 줄였다.
- 하단 2줄은 제목 표기("-200만원", "-1,600만원"), 카드는 영상 계좌 카드 표기("-200만 원", "-1,600만 원")다. 값은 같다.
- 펀치 "반년 만에"는 문장 6 "반년을 버텼을까요"와 실제 기간(2025-07-01 매수 → 12-30 매도)이다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos, no stock names). Inside the card, on the left: the text
"-200만 원" in medium-size blue (#2D6CDF) bold letters. In the middle: a thick blue (#2D6CDF) arrow that steps down
like a staircase several times toward the lower right, with the label "반년 만에" in black bold letters over a bright
yellow (#FFD400) highlighter stripe just above the arrow. On the right: a solid blue (#2D6CDF) rounded box with the huge
white bold text "-1,600만 원", the largest element in the image. No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "본전 기다린 -200만원이", line 2 "-1,600만원이 됐다". The word "-1,600만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. In the upper 60% of the frame, a wide
light-cream rounded rectangle card with a thin black outline. Inside: empty space on the left for a number, a thick blue
arrow in the middle that steps down like a staircase several times toward the lower right, with a short bright yellow
highlighter stripe just above it, and an empty solid blue (#2D6CDF) rounded box on the right. No people. The lower third
is a dark navy (#14213D) band that fades upward from the bottom edge, with clean empty space for two lines of large text;
nothing else in the band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "-200만 원" · "반년 만에" · "-1,600만 원" · "본전 기다린 -200만원이" · "-1,600만원이 됐다"가 한 글자도 틀리지 않음 (문장 1·3·6, 제목 T1과 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음 (한 줄 14자 이내: 14자·12자, 2줄 합 26자) · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 카드는 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 펀치 문구는 "반년 만에" 1개
- [ ] 320px 축소본에서 "-1,600만 원"과 하단 2줄이 바로 읽힘
- [ ] 강조색 3곳 이하 (노랑 형광펜 "반년 만에", 노랑 "-1,600만원") · 손실은 파랑·노랑, 빨강 없음
- [ ] 증권사 앱처럼 보이지 않음 (앱 이름·로고·실제 화면 배치 없음) · 종목명·티커 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
