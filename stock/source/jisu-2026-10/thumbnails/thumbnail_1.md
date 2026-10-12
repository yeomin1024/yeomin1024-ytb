# jisu-2026-10 썸네일 1 — 숫자 반전 (갈림길 계좌 카드)

버전: v1.1 — 2026-10-12 — 사연 종목 변경(알테오젠 → 네이버)에 따라 손실 숫자 -1,200만 → -900만 원 (v1.0 — 2026-10-12 — 최초 작성, `guides/thumbnail_guide.md` v1.3.1, `stock/guides/thumbnail_rules.md` v2.0), 대본 jisu-2026-10.txt v1.1 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 같은 4,500만 원이 **지수에 남았으면 +2,800만 원, 갈아탔더니 -900만 원**으로 갈린 **두 숫자의 대비**가 가장 클릭을 부른다 |
| 짝 제목 | `titles.md` **T1 (채택)** "지수는 느리다며 갈아탔다가 +2,800만원 대신 900만원을 잃었습니다. …" — T2·T3과도 어울림 |
| 숫자 근거 | 문장 1 "지수에 뒀으면 +2,800만 원이었을 돈이, -900만 원이 됐어요" (0:00) · 문장 2 "3년 모은 지수 ETF 4,500만 원" (0:07) → 사연 30초 안 (추정 SRT 기준, 오디오에 맞춘 뒤 다시 확인). 검산: README "사연 검산" (+2,801.8만 원, -906.5만 원) |

## 화면 구성
- 크림 배경. 인물 없음.
- **위쪽 약 60%** (y 0~430): 가로로 긴 밝은 크림색 카드 (얇은 검정 테두리, 둥근 모서리) — 영상의 계좌 카드와 같은 모양
  - 카드 왼쪽: 작은 동그란 출발점 하나에서 선이 두 갈래로 갈린다 (갈림길)
    - 위로 올라가는 굵은 **빨강 선** 끝: 작은 라벨 "지수" + **"+2,800만 원"** (빨강, 중간 크기)
    - 아래로 꺾여 내려가는 굵은 **파랑 선** 끝: 작은 라벨 "내 종목" + 파랑 상자 안 **"-900만 원"** (흰색, 가장 큰 글자 — 화면 높이 약 20%)
  - 갈림길 출발점 위에 펀치 **"같은 돈인데"** (검정 글자 + 노랑 형광펜)
- **아래쪽 약 35%** (y 약 450~690): 아래에서 위로 옅어지는 다크 네이비 띠 위에 하단 제목 2줄
  - 왼쪽 정렬 x 48부터, 글자 크기 약 92px. 2번째 줄 끝은 x 약 800 → x 1040 안
- 오른쪽 아래 구석은 비움 · 종목명·상품명·티커 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 위 갈래 | 지수 (작은 라벨) / +2,800만 원 | 라벨 잉크 #1E1E1E / 숫자 빨강 #E63B2E | 수익(지수에 뒀다면) = 빨강 |
| 펀치 (위쪽) | 같은 돈인데 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (노랑 상자는 이 1곳만) |
| 카드 아래 갈래 | 내 종목 (작은 라벨) / -900만 원 | 라벨 잉크 / 숫자 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 지수 느리다며 갈아탔다가 | 흰색 + 검정 외곽선 | — (13자) |
| 하단 2줄 | 900만원 잃었습니다 | 흰색 + 검정 외곽선 | "900만원"만 노랑 #FFD400 (11자, 2줄 합 24자) |

- 강조색 3곳: 빨강 "+2,800만 원"(수익 쪽), 노랑 형광펜 "같은 돈인데", 노랑 글자 "900만원". 손실 숫자는 빨강으로 쓰지 않는다 (카드는 파랑 상자, 하단은 노랑 — `stock/guides/thumbnail_rules.md` 1번).
- 하단 2줄은 T1 앞 문장("지수는 느리다며 갈아탔다가 +2,800만원 대신 900만원을 잃었습니다")을 줄인 것. "+2,800만원 대신"은 카드 숫자로 넘기고 하단에서는 뺐다.
- 작은 라벨 "지수"·"내 종목"은 카드의 일부(작은 잉크 글자)다. 펀치 문구는 "같은 돈인데" 1개.
- 하단 2줄은 제목 표기("900만원"), 카드는 영상 계좌 카드 표기("+2,800만 원", "-900만 원")다. 값은 같다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos, no stock or fund names). Inside the card, on the left, one small
black dot where a single line splits into two branches like a fork in the road: one thick red (#E63B2E) branch rises up to the
upper right and ends at the small ink label "지수" and the red bold text "+2,800만 원"; the other thick blue (#2D6CDF) branch
drops steeply down to the lower right and ends at the small ink label "내 종목" next to a solid blue (#2D6CDF) rounded box
with the huge white bold text "-900만 원", the largest element in the image. Just above the split point, the words
"같은 돈인데" in black bold letters over a bright yellow (#FFD400) highlighter stripe. No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "지수 느리다며 갈아탔다가", line 2 "900만원 잃었습니다". The word "900만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. In the upper 60% of the frame, a wide
light-cream rounded rectangle card with a thin black outline. Inside: on the left a small black dot where one line splits
into two branches, a thick red branch rising to the upper right with empty space at its end for a number, and a thick blue
branch dropping steeply to the lower right ending next to an empty solid blue (#2D6CDF) rounded box; a short bright yellow
highlighter stripe just above the split point. No people. The lower third is a dark navy (#14213D) band that fades upward
from the bottom edge, with clean empty space for two lines of large text; nothing else in the band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "지수" · "+2,800만 원" · "같은 돈인데" · "내 종목" · "-900만 원" · "지수 느리다며 갈아탔다가" · "900만원 잃었습니다"가 한 글자도 틀리지 않음 (문장 1·2, 제목 T1과 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음 (한 줄 14자 이내: 13자·11자, 2줄 합 26자 이내) · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 카드는 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 펀치 문구는 "같은 돈인데" 1개
- [ ] 320px 축소본에서 "-900만 원"과 하단 2줄이 바로 읽힘
- [ ] 강조색 3곳 이하 (빨강 "+2,800만 원", 노랑 형광펜 "같은 돈인데", 노랑 "900만원") · 손실은 파랑·노랑, 빨강 없음
- [ ] 증권사 앱처럼 보이지 않음 (앱 이름·로고·실제 화면 배치 없음) · 종목명·상품명·티커 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
