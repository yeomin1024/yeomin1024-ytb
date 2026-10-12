# panicsell-2026-10 썸네일 1 — 숫자 반전 (판 금액 → 판 뒤 반등)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `guides/thumbnail_guide.md` v1.3, `stock/guides/thumbnail_rules.md` v1.2, 대본 v1.1 기준. 카드를 위쪽 60%로 줄이고, "전부 매도"는 하단 2줄의 "다 팔았는데"와 같은 말이라 뺌 (이 시안은 펀치 문구 없이 숫자 2개만) (v1.0: 2026-10-10 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "-800만 원에 팔았는데 그 뒤 +30%"라는 **판 뒤 반등의 숫자 대비**가 가장 클릭을 부른다 (판 사람의 후회를 숫자 두 개로) |
| 짝 제목 | `titles.md` **T1 (채택)** "하락장이 무서워 -800만원에 다 팔았는데 …" — T3과도 어울림 |
| 숫자 근거 | 문장 9 "-800만 원이 넘어" (0:40) · 문장 11 "장 마감 직전 모두 팔았어요" (0:50) · 문장 13 "판 가격보다 30% 넘게" (1:01) — 오디오에 맞춘 SRT 기준. ※ "+30%"는 1분을 1초 넘는다 (오디오를 맞추기 전 SRT로는 0:58). 채택 제목의 숫자라 그대로 둔다 |

## 화면 구성
- 크림 배경.
- **위쪽 약 60%** (y 0~430): 가로로 긴 밝은 크림색 카드 (얇은 검정 테두리, 둥근 모서리) — 영상의 계좌 카드와 같은 모양
  - 카드 왼쪽: 파랑 상자 안 **"-800만 원"** (흰 글자, 크게)
  - 카드 오른쪽: 왼쪽 아래에서 오른쪽 위로 크게 올라가는 굵은 빨강 화살표 + 그 끝에 **"+30%"** (빨강, 가장 큰 글자 — 화면 높이 약 25%)
  - 펀치 문구 없음: 전에 있던 "전부 매도"는 하단 2줄 "다 팔았는데"와 같은 말이라 뺐다.
- **아래쪽 약 35%** (y 약 450~690): 아래에서 위로 옅어지는 다크 네이비 띠 위에 하단 제목 2줄
  - 왼쪽 정렬 x 48부터, 글자 크기 약 95px (한글 높이 약 90px). 2번째 줄 끝은 x 약 990 → x 1040 안
- 오른쪽 아래 구석은 비움 · 인물 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 판 금액 | -800만 원 | 흰색 (파랑 #2D6CDF 상자 위) | — |
| 카드 판 뒤 | +30% | 빨강 #E63B2E (상승) | 가장 큰 글자 |
| 하단 1줄 | 하락장이 무서워 | 흰색 + 검정 외곽선 | — (8자) |
| 하단 2줄 | 다 팔았는데 +30% 반등 | 흰색 + 검정 외곽선 | "다 팔았는데"만 노랑 #FFD400 (14자, 2줄 합 22자) |

- 강조색은 2곳: 빨강 "+30%"(카드, 상승), 노랑 "다 팔았는데". 하단의 "+30%"는 흰색으로 둔다 (위쪽 빨강 "+30%"가 이미 가장 크다).
- 하단 2줄은 T1 앞 문장("하락장이 무서워 -800만원에 다 팔았는데 그 뒤 +30% 반등했습니다")을 줄인 것. "-800만원"은 카드에 있어 하단에서 뺐다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos). On the left half of the card: a solid blue (#2D6CDF) rounded
box with the large white bold text "-800만 원". On the right half of the card: a thick red (#E63B2E) arrow rising steeply
from the lower left to the upper right, ending at the huge red bold text "+30%", the largest element in the image.
No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "하락장이 무서워", line 2 "다 팔았는데 +30% 반등". The word "다 팔았는데" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, loss blue #2D6CDF, gain red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. In the upper 60% of the frame, a wide
light-cream rounded rectangle card with a thin black outline. Left half: an empty solid blue (#2D6CDF) rounded box. Right
half: a thick red arrow rising steeply from lower left to upper right, with empty space at its tip for a number.
No people. The lower third is a dark navy (#14213D) band that fades upward from the bottom edge, with clean empty space
for two lines of large text; nothing else in the band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "-800만 원" · "+30%" · "하락장이 무서워" · "다 팔았는데 +30% 반등"이 한 글자도 틀리지 않음 (문장 9·11·13, 제목 T1과 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음 (한 줄 14자 이내: 8자·14자, 2줄 합 22자) · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 카드는 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽에 숫자 말고 다른 문구 없음 (펀치 문구 0개)
- [ ] 320px 축소본에서 "+30%"·"-800만 원"과 하단 2줄이 바로 읽힘
- [ ] 강조색 2곳 (빨강 "+30%" = 상승, 노랑 "다 팔았는데") · 손실은 파랑 상자, 손실 숫자에 빨강 없음
- [ ] 증권사 앱처럼 보이지 않음 (앱 이름·로고·실제 화면 배치 없음) · 종목명 없음
- [ ] 오른쪽 아래 비어 있음 (화살표 끝 "+30%"는 카드 오른쪽 위) · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
