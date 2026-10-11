# molppang-2026-10 썸네일 1 — 숫자 반전 (계좌 카드)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.3, `stock/guides/thumbnail_rules.md` v1.2), 대본 molppang-2026-10.txt v2.1 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 천만 원 수익(빨강)이 -2천만 원 손실(파랑)로 뒤집힌 **계좌 숫자 반전**이 가장 클릭을 부른다 (성공 썸네일 중 인물 없는 3개가 모두 이 형태) |
| 짝 제목 | `titles.md` **T1 (채택)** "한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다. …" — T2·T3과도 어울림 |
| 숫자 근거 | 문장 3 "전 재산 7천만 원을 이 종목에 몰빵" (0:15) · 문장 4 "천만 원 정도 수익" (0:21) · 문장 7 "갑자기 -2천만 원이 찍힌 겁니다" (0:34) → 모두 1분 안. 영상 S03·S04의 계좌 카드도 평가손익 +1,000만 원 → -2,000만 원 |

## 화면 구성
- 배경: 다크 네이비 #14213D 한 가지 (영상 S04 "어느 날" 장면과 같은 색)
- 위쪽 약 60% (y 48~420), 가운데에서 조금 왼쪽: 크림 계좌 카드 (가로 약 70%, 잉크 얇은 테두리, 둥근 모서리 — 영상의 계좌 카드와 같은 모양)
  - 카드 왼쪽 위: 작은 라벨 "내 계좌"
  - 그 아래: "+1,000만 원" (빨강, 중간 크기)
  - 그 아래: 굵은 파랑 아래 화살표
  - 카드 아래쪽: 넓은 파랑 상자 안에 **"-2,000만 원"** (흰 글자, 가장 큰 글자 — 화면 높이 약 20%)
- 아래쪽 약 35% (y 450~690): 아래에서 위로 옅어지는 검정 띠 + **하단 제목 2줄** (왼쪽 정렬 x 48부터, 2번째 줄은 x 1040 안에서 끝남)
- 인물 없음 · 종목명·티커·증권사 앱 모양 없음 · 오른쪽 아래 구석(약 220×70) 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 라벨 (작게) | 내 계좌 | 잉크 #1E1E1E | — |
| 카드 시작 숫자 | +1,000만 원 | 빨강 #E63B2E (수익) | 강조 1 — 빨강 = 수익 |
| 펀치 (가장 큰 숫자) | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 (파랑 = 손실) |
| 하단 1줄 | 한 종목에만 몰빵했다가 | 흰색 + 두꺼운 검정 외곽선 | "몰빵했다가" 노랑 #FFD400 — 강조 2 |
| 하단 2줄 | 천만원 수익이 -2천만원 | 흰색 + 두꺼운 검정 외곽선 | — (손실 숫자는 빨강 금지 → 흰색) |

- 하단 2줄 = T1 앞 문장 "한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다"를 줄인 것: 12자 + 13자 = 25자 (띄어쓰기 포함, 한 줄 14자 이내 · 합 26자 이내)
- 강조색(노랑·빨강) 2곳 · 노랑 상자 없음 · 펀치(위쪽 큰 문구)는 "-2,000만 원" 1개(9자)
- 하단 2줄의 "-2천만원"은 제목 표기, 카드의 "-2,000만 원"은 영상 카드 표기 — 값은 같다 (`stock/guides/thumbnail_rules.md` 1번)

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a solid dark navy (#14213D) background. In the upper 60% of the frame, slightly left of
center, a light-cream (#F2EBDD) rounded rectangle card with a thin ink-black outline, about 70% of the frame width, like a
simple personal account summary card (NOT a real banking or brokerage app: no app name, no logos, no menus, no stock name
or ticker). Inside the card: a small ink-black label "내 계좌" at the top-left; below it the text "+1,000만 원" in
medium-size bold red (#E63B2E); below that a thick blue (#2D6CDF) arrow pointing down; and across the bottom of the card a
wide solid blue (#2D6CDF) rounded box with the huge white bold text "-2,000만 원", the largest text in the image (about one
fifth of the image height). No people, no faces, no chart axes or extra numbers, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "한 종목에만 몰빵했다가", line 2 "천만원 수익이 -2천만원". The word "몰빵했다가" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep all text at least 48px inside the edges, within the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, loss blue #2D6CDF.
Clean flat editorial graphic on a solid dark navy (#14213D) background. In the upper 60% of the frame, slightly left of
center, a light-cream rounded rectangle card with a thin ink-black outline, about 70% of the frame width (no app interface,
no logos). Inside the card: empty space at the top-left for a small label, an empty line below it for a number, a thick
blue (#2D6CDF) arrow pointing down, and a wide empty solid blue (#2D6CDF) rounded box across the bottom of the card.
The lower 35% of the frame is an empty dark band that fades upward from the bottom edge (black, about 85% opacity),
kept completely clear for a two-line title. No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
- [B]로 만들면 편집 프로그램에서 "문구" 표대로 얹는다: 하단 2줄은 Noto Sans KR Black(또는 Pretendard Black) 약 90px, 흰색 + 검정 외곽선 8px 안팎, x 48부터 왼쪽 정렬, y 약 470~680.

## 검수
- [ ] "내 계좌" · "+1,000만 원" · "-2,000만 원" · "한 종목에만 몰빵했다가" · "천만원 수익이 -2천만원"이 한 글자도 틀리지 않음 (문장 4·7과 같은 숫자)
- [ ] 아래쪽 제목 2줄이 크게 있고, 위쪽 카드·숫자가 2줄을 가리지 않음
- [ ] +1,000만 원은 빨강(수익), -2,000만 원은 파랑 상자(손실) — 손실 숫자에 빨강 없음 · 강조색 2곳
- [ ] 320px 축소본에서 "-2,000만 원"과 하단 2줄이 읽힘
- [ ] 증권사 앱처럼 보이지 않음 (앱 이름·로고·실제 화면 배치 없음) · 종목명·티커 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하 (아니면 업로드 도구가 자동 변환)

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
