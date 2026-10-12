# panicsell-2026-10 썸네일 2 — 인물·감정 장면 (다 판 다음 날)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `guides/thumbnail_guide.md` v1.3, `stock/guides/thumbnail_rules.md` v1.2, 대본 v1.1 기준. 인물·숫자를 위쪽 60%로 올리고 하단 2줄 추가. "다 판 다음 날"은 하단 2줄("팔았는데", "다음 날")과 같은 말이라 뺌 (이 시안은 펀치 문구 없이 큰 숫자만) (v1.0: 2026-10-10 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 다 판 다음 날 오른 주가를 본 **사람의 허탈한 표정**이 숫자 카드보다 감정을 더 끈다 (성공 썸네일 24개 중 약 20개가 얼굴) |
| 짝 제목 | `titles.md` T2 "서킷브레이커 걸린 날 -800만원에 전부 팔았는데 다음 날 +11% 올랐습니다 …" — T1(채택)과도 어울림 |
| 숫자 근거 | 문장 8 "서킷브레이커로 시장 전체의 거래가 20분 동안 멈췄어요" (0:33) · 문장 11 "장 마감 직전 모두 팔았어요" (0:50) · 문장 12 "바로 다음 날 … 11% 넘게 올랐습니다" (0:55) · 문장 16 "다음 날 빨갛게 오른 주가를 보면서" (1:18) → 장면·숫자 모두 1분 안 (오디오에 맞춘 SRT 기준) |

## 화면 구성
- 다크 네이비 배경. 아침, 출근 전 부엌 식탁
- **위쪽 약 60%** (y 0~430)
  - 왼쪽 40~45%: **가상 인물** — 30대 후반 한국인 여성 직장인, 식탁에 앉아 휴대폰을 보며 입을 살짝 벌린 허탈한 표정
    - 얼굴과 휴대폰은 위쪽 60% 안. 상반신 아래쪽은 하단 띠 속으로 어둡게 사라진다 (하단 2줄이 얼굴을 가리지 않게).
    - 휴대폰 불빛이 얼굴을 비춘다. 휴대폰 화면에는 크게 올라가는 빨강 선만 있다 (앱 화면·글자 없음).
  - 오른쪽: **"+11%"** (빨강, 얇은 흰 외곽선, 가장 큰 글자 — 화면 높이 약 25%)
  - 펀치 문구 없음
- **아래쪽 약 35%** (y 약 450~690): 아래에서 위로 옅어지는 어두운 띠 위에 하단 제목 2줄
  - 왼쪽 정렬 x 48부터, 글자 크기 약 95px (한글 높이 약 90px). 1번째 줄이 가장 길다 (x 약 1,050까지 — 1번째 줄은 오른쪽 아래 구석과 겹치지 않음). 2번째 줄 끝은 x 약 900 → x 1040 안
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 결과 숫자 (위쪽) | +11% | 빨강 #E63B2E (상승, 얇은 흰 외곽선) | 가장 큰 글자 |
| 하단 1줄 | 서킷브레이커 날 팔았는데 | 흰색 + 검정 외곽선 | "서킷브레이커"만 노랑 #FFD400 (13자) |
| 하단 2줄 | 다음 날 +11% 올랐다 | 흰색 + 검정 외곽선 | — (13자, 2줄 합 26자) |

- 강조색은 2곳: 빨강 "+11%"(위쪽, 상승), 노랑 "서킷브레이커". 하단의 "+11%"는 흰색으로 둔다 (위쪽 빨강 "+11%"가 이미 가장 크다).
- 하단 2줄은 T2 앞 문장("서킷브레이커 걸린 날 -800만원에 전부 팔았는데 다음 날 +11% 올랐습니다")을 줄인 것. 2줄 합 26자 한도 때문에 "걸린"·"-800만원에 전부"를 뺐다 ("-800만원"은 T1·T3 썸네일에 있음).

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned kitchen in the early morning before work. On the left 40% of the frame, a fictional
Korean woman in her late 30s, office-worker look (plain blouse), sitting at a kitchen table and staring at a smartphone,
mouth slightly open, blank regretful expression, face lit by the phone's light. Her face and the phone are in the upper 60%
of the frame; her lower body fades into darkness at the bottom. The phone screen shows only a simple red line rising
sharply, no app interface, no text. Fictional person, not resembling any real or famous person, natural Korean features,
realistic photo style. In the upper right area, the huge red (#E63B2E) bold text "+11%" with a thin white outline, the
largest element, kept in the upper 60%. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "서킷브레이커 날 팔았는데", line 2 "다음 날 +11% 올랐다". The word "서킷브레이커" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, gain red #E63B2E.
Realistic photo style. Dark navy-toned kitchen in the early morning. On the left 40% of the frame, a fictional Korean woman
in her late 30s, office-worker look, sitting at a kitchen table staring at a smartphone, mouth slightly open, blank
regretful expression, face lit by the phone's light; the phone screen shows only a simple red line rising sharply.
Her face and the phone are in the upper 60% of the frame. Fictional person, not resembling any real or famous person.
The upper right area is calm dark empty space for one big number. The lower third is a dark band (black to dark navy) that
fades upward from the bottom edge, with clean empty space for two lines of large text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "+11%" · "서킷브레이커 날 팔았는데" · "다음 날 +11% 올랐다"가 한 글자도 틀리지 않음 (문장 8·11·12, 제목 T2와 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음 (한 줄 14자 이내: 13자·13자, 2줄 합 26자) · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 얼굴·휴대폰·"+11%"가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽에 숫자 말고 다른 문구 없음 (펀치 문구 0개)
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 표정은 허탈·후회 수준 (울음·극단적 공포 없음)
- [ ] 휴대폰 화면에 앱 이름·로고·글자 없음 · 종목명 없음
- [ ] 320px 축소본에서 얼굴 표정, "+11%", 하단 2줄이 읽힘
- [ ] 강조색 2곳 (빨강 "+11%" = 상승, 노랑 "서킷브레이커")
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
