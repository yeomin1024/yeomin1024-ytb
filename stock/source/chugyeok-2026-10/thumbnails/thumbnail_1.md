# chugyeok-2026-10 썸네일 1 — 숫자 반전 (계좌 카드)

버전: v1.0 — 2026-10-12 — 최초 작성 (`guides/thumbnail_guide.md` v1.3, `stock/guides/thumbnail_rules.md` v1.2), 대본 chugyeok-2026-10.txt v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 수익 **+380만 원이 일주일 만에 -1,000만 원**으로 뒤집힌 **계좌 숫자 반전**이 가장 클릭을 부른다 (성공 썸네일 중 인물 없는 3개가 모두 이 형태) |
| 짝 제목 | `titles.md` **T1 (채택)** "나만 못 탈까 봐 따라 산 급등주에서 번 380만원이 -1천만원이 됐습니다. …" — T2·T3과도 어울림 |
| 숫자 근거 | 문장 1 "따라 사서 번 380만 원이, 일주일 만에 -1천만 원이 됐어요" (0:00) · 문장 5 "나만 못 탈까 봐 서두른 그 하루가" (0:21) → 모두 사연 30초 안 (추정 SRT 기준, 오디오에 맞춘 뒤 다시 확인). 검산: README "사연 검산" (+386만 원, -996만 원) |

## 화면 구성
- 크림 배경.
- **위쪽 약 60%** (y 0~430): 가로로 긴 밝은 크림색 카드 (얇은 검정 테두리, 둥근 모서리) — 영상의 계좌 카드와 같은 모양
  - 카드 왼쪽: **"+380만 원"** (빨강 — 이 채널에서 빨강 = 수익, 중간 크기)
  - 카드 가운데: 오른쪽 아래로 꺾여 내려가는 굵은 파랑 화살표, 화살표 위에 펀치 "일주일 만에" (검정 글자 + 노랑 형광펜)
  - 카드 오른쪽: 파랑 상자 안 **"-1,000만 원"** (흰색, 가장 큰 글자 — 화면 높이 약 20%)
- **아래쪽 약 35%** (y 약 450~690): 아래에서 위로 옅어지는 다크 네이비 띠 위에 하단 제목 2줄
  - 왼쪽 정렬 x 48부터, 글자 크기 약 95px (한글 높이 약 90px). 2번째 줄 끝은 x 약 910 → x 1040 안
- 오른쪽 아래 구석은 비움 · 인물 없음 · 종목명·티커 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 시작 숫자 | +380만 원 | 빨강 #E63B2E | 수익 금액 = 빨강 |
| 펀치 (위쪽) | 일주일 만에 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (노랑 상자는 이 1곳만) |
| 카드 결과 숫자 | -1,000만 원 | 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 나만 못 탈까 봐 샀다가 | 흰색 + 검정 외곽선 | — (13자) |
| 하단 2줄 | +380만원이 -1천만원 | 흰색 + 검정 외곽선 | "-1천만원"만 노랑 #FFD400 (13자, 2줄 합 26자) |

- 강조색 3곳: 빨강 "+380만 원"(카드, 수익), 노랑 형광펜 "일주일 만에", 노랑 글자 "-1천만원". 손실 숫자는 빨강으로 쓰지 않는다 (카드는 파랑 상자, 하단은 노랑).
- 하단 2줄은 T1 앞 문장("나만 못 탈까 봐 따라 산 급등주에서 번 380만원이 -1천만원이 됐습니다")을 줄인 것. 2줄 합 26자 안에 넣으려고 "따라 산 급등주에서 번"을 "샀다가"로 줄였다. "+"는 380만원이 손실이 아니라 수익이라는 걸 한눈에 보이게 붙였다 (값은 제목과 같음).
- 하단 2줄은 제목 표기("380만원", "-1천만원"), 카드는 영상 계좌 카드 표기("+380만 원", "-1,000만 원")다. 값은 같다 (`stock/guides/thumbnail_rules.md` 1번).

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos, no stock names). Inside the card, on the left: the text
"+380만 원" in large red (#E63B2E) bold letters. In the middle: a thick blue (#2D6CDF) arrow that goes up a little and then
plunges steeply down to the right, with the label "일주일 만에" in black bold letters over a bright yellow (#FFD400)
highlighter stripe just above the arrow. On the right: a solid blue (#2D6CDF) rounded box with the huge white bold text
"-1,000만 원", the largest element in the image. No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "나만 못 탈까 봐 샀다가", line 2 "+380만원이 -1천만원". The word "-1천만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. In the upper 60% of the frame, a wide
light-cream rounded rectangle card with a thin black outline. Inside: empty space on the left for a number, a thick blue
arrow in the middle that goes up a little and then plunges steeply down to the right, with a short bright yellow
highlighter stripe just above it, and an empty solid blue (#2D6CDF) rounded box on the right. No people. The lower third
is a dark navy (#14213D) band that fades upward from the bottom edge, with clean empty space for two lines of large text;
nothing else in the band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "+380만 원" · "일주일 만에" · "-1,000만 원" · "나만 못 탈까 봐 샀다가" · "+380만원이 -1천만원"이 한 글자도 틀리지 않음 (문장 1·5, 제목 T1과 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음 (한 줄 14자 이내: 13자·13자, 2줄 합 26자) · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 카드는 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 펀치 문구는 "일주일 만에" 1개
- [ ] 320px 축소본에서 "-1,000만 원"과 하단 2줄이 바로 읽힘
- [ ] 강조색 3곳 이하 (빨강 "+380만 원", 노랑 형광펜 "일주일 만에", 노랑 "-1천만원") · 손실은 파랑·노랑, 빨강 없음
- [ ] 증권사 앱처럼 보이지 않음 (앱 이름·로고·실제 화면 배치 없음) · 종목명·티커 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
