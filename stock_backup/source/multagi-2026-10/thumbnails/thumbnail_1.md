# multagi-2026-10 썸네일 1 — 숫자 반전 (계좌 카드)

버전: v1.2 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `guides/thumbnail_guide.md` v1.3, `stock/guides/thumbnail_rules.md` v1.2, 대본 v1.4 기준. 카드를 위쪽 60%로 줄이고 하단 2줄 추가, 펀치는 "물타기 2번" 1개 (v1.1: 2026-10-09 이미지 AI용 프롬프트 형식으로 변경 / v1.0: 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 작은 손실이 10배로 커진 **계좌 숫자 반전**이 가장 클릭을 부른다 (성공 썸네일 중 인물 없는 3개가 모두 이 형태) |
| 짝 제목 | `titles.md` **T1 (채택)** "평단 낮추면 된다는 말만 믿고 물타서 …" — T2·T3과도 어울림 |
| 숫자 근거 | 문장 5 "일주일 만에 -200만 원이 됐어요" (0:24) · 문장 6·7 1,500만 원씩 두 번 물타기 (0:30·0:36) · 문장 10 "-2천만 원이 찍혀 있었어요" (0:51) → 모두 1분 안 (오디오에 맞춘 SRT 기준. 문장 2가 자막 2개로 나뉘어 자막 번호는 문장 번호 +1) |

## 화면 구성
- 크림 배경.
- **위쪽 약 60%** (y 0~430): 가로로 긴 밝은 크림색 카드 (얇은 검정 테두리, 둥근 모서리) — 영상의 계좌 카드와 같은 모양
  - 카드 왼쪽: "-200만 원" (파랑, 중간 크기)
  - 카드 가운데: 오른쪽 아래로 향하는 굵은 파랑 화살표, 화살표 위에 펀치 "물타기 2번" (검정 글자 + 노랑 형광펜)
  - 카드 오른쪽: 파랑 상자 안 **"-2,000만 원"** (흰색, 가장 큰 글자 — 화면 높이 약 20%)
- **아래쪽 약 35%** (y 약 450~690): 아래에서 위로 옅어지는 다크 네이비 띠 위에 하단 제목 2줄
  - 왼쪽 정렬 x 48부터, 글자 크기 약 95px (한글 높이 약 90px). 2번째 줄 끝은 x 약 900 → x 1040 안
- 오른쪽 아래 구석은 비움 · 인물 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 시작 숫자 | -200만 원 | 파랑 #2D6CDF | — |
| 펀치 (위쪽) | 물타기 2번 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (노랑 상자는 이 1곳만) |
| 카드 결과 숫자 | -2,000만 원 | 흰색 (파랑 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 평단 낮추면 된다길래 | 흰색 + 검정 외곽선 | — (11자) |
| 하단 2줄 | -200만원이 -2천만원 | 흰색 + 검정 외곽선 | "-2천만원"만 노랑 #FFD400 (13자, 2줄 합 24자) |

- 강조색은 2곳: 노랑 형광펜 "물타기 2번", 노랑 글자 "-2천만원". 손실 숫자는 빨강으로 쓰지 않는다 (카드는 파랑, 하단은 흰색·노랑).
- 하단 2줄은 T1 앞 문장("평단 낮추면 된다는 말만 믿고 물타서 -200만원이 -2천만원이 됐습니다")을 줄인 것. 펀치 "물타기 2번"과 같은 말("물타")은 하단에 넣지 않았다.
- 하단 2줄은 제목 표기("-200만원", "-2천만원"), 카드는 영상 계좌 카드 표기("-200만 원", "-2,000만 원")다. 값은 같다 (`stock/guides/thumbnail_rules.md` 1번).

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos). Inside the card, on the left: the text "-200만 원" in large
blue (#2D6CDF) bold letters. In the middle: a thick blue arrow pointing right and slightly down, with the label
"물타기 2번" in black bold letters over a bright yellow (#FFD400) highlighter stripe just above the arrow. On the right: a
solid blue (#2D6CDF) rounded box with the huge white bold text "-2,000만 원", the largest element in the image.
No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "평단 낮추면 된다길래", line 2 "-200만원이 -2천만원". The word "-2천만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF.
Clean flat editorial graphic on a cream paper background with subtle paper grain. In the upper 60% of the frame, a wide
light-cream rounded rectangle card with a thin black outline. Inside: empty space on the left for a number, a thick blue
arrow pointing right and slightly down in the middle with a short bright yellow highlighter stripe just above it, and an
empty solid blue (#2D6CDF) rounded box on the right. No people. The lower third is a dark navy (#14213D) band that fades
upward from the bottom edge, with clean empty space for two lines of large text; nothing else in the band.
Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "-200만 원" · "물타기 2번" · "-2,000만 원" · "평단 낮추면 된다길래" · "-200만원이 -2천만원"이 한 글자도 틀리지 않음 (문장 5·6~7·10, 제목 T1과 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음 (한 줄 14자 이내: 11자·13자, 2줄 합 24자) · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 카드는 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 펀치 문구는 "물타기 2번" 1개
- [ ] 320px 축소본에서 "-2,000만 원"과 하단 2줄이 바로 읽힘
- [ ] 강조색 2곳 (노랑 형광펜 "물타기 2번", 노랑 "-2천만원") · 손실은 파랑·흰색·노랑, 빨강 없음
- [ ] 증권사 앱처럼 보이지 않음 (앱 이름·로고·실제 화면 배치 없음) · 종목명 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
