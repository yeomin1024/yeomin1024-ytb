# chugyeok-2026-10 썸네일 2 — 인물·감정 장면

버전: v1.0 — 2026-10-12 — 최초 작성 (`guides/thumbnail_guide.md` v1.3, `stock/guides/thumbnail_rules.md` v1.2), 대본 chugyeok-2026-10.txt v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 꼭대기 근처에서 따라 산 뒤 손실을 확인한 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (성공 썸네일 24개 중 약 20개가 얼굴) |
| 짝 제목 | `titles.md` T2 "일곱 배 올랐다는 말만 듣고 올라탄 주식이 +380만원에서 -1천만원이 됐습니다. …" — T1(채택)·T3과도 어울림 |
| 숫자 근거 | 문장 1 "번 380만 원이, 일주일 만에 -1천만 원" (0:00) · 문장 2 "상장 보름 만에 일곱 배가 넘은 써클을 4천만 원어치 샀죠" (0:06) → 사연 30초 안 (추정 SRT 기준) |

> **인물 성별은 정하지 않았다.** 사연자 목소리를 사용자가 샘플로 고르는 중이라 대본에서도 성별을 드러내지 않았다 (README "사연 길이"). 프롬프트는 "office worker"로만 썼다. 목소리가 정해지면 [A]·[B]의 "a fictional Korean office worker" 앞에 man/woman을 넣어 사연자와 맞춘다.

## 화면 구성
- 다크 네이비 배경. 밤늦은 방 (미국장은 한국 시간 밤에 열림), 책상 위 스탠드 불빛만
- **위쪽 약 60%** (y 0~430)
  - 왼쪽 40~45%: **가상 인물** — 40살 안팎 한국인 직장인, 휴대폰을 든 채 다른 손으로 입을 가리고 굳은 표정 (당황·후회)
    - 얼굴과 휴대폰은 위쪽 60% 안. 상반신 아래쪽은 하단 띠 속으로 어둡게 사라진다 (하단 2줄이 얼굴을 가리지 않게).
    - 휴대폰 불빛이 얼굴을 비춘다. 휴대폰 화면에는 짧게 오르던 빨간 선이 파랗게 꺾여 떨어지는 선만 있다 (앱 화면·글자 없음).
  - 오른쪽: 위에 펀치 **"일곱 배에 샀다"** (흰 글자, "일곱 배"만 노랑 상자 + 검정 글자), 아래에 파랑 상자 안 **"-1,000만 원"** (흰 글자, 가장 큼)
- **아래쪽 약 35%** (y 약 450~690): 아래에서 위로 옅어지는 어두운 띠 위에 하단 제목 2줄
  - 왼쪽 정렬 x 48부터, 글자 크기 약 90px (한글 높이 약 85px). 2번째 줄 끝은 x 약 950 → x 1040 안
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 일곱 배에 샀다 | 흰색 #F7F3EA ("일곱 배"만 검정) | "일곱 배"에 노랑 상자 (글자 전체 높이, 노랑 상자는 이 1곳만) |
| 결과 숫자 (위쪽) | -1,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |
| 하단 1줄 | 말만 듣고 올라탄 주식 | 흰색 + 검정 외곽선 | — (12자) |
| 하단 2줄 | +380만원에서 -1천만원 | 흰색 + 검정 외곽선 | "+380만원" 빨강 #E63B2E(수익), "-1천만원" 노랑 #FFD400(손실) (14자, 2줄 합 26자) |

- 강조색 3곳: 노랑 상자 "일곱 배", 빨강 "+380만원"(수익), 노랑 "-1천만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (위쪽은 파랑 상자, 하단은 노랑).
- 하단 2줄은 T2 앞 문장("일곱 배 올랐다는 말만 듣고 올라탄 주식이 +380만원에서 -1천만원이 됐습니다")을 줄인 것. "일곱 배"는 펀치에 있어 하단에 다시 쓰지 않았다.
- 펀치 "일곱 배에 샀다"는 문장 2(공모가의 일곱 배가 넘은 값에 산 것, 0:06)와 문장 22("공모가 31달러의 일곱 배가 넘는 값")의 말이다.
- 하단 2줄은 제목 표기("+380만원", "-1천만원"), 위쪽 상자는 영상 계좌 카드 표기("-1,000만 원")다. 값은 같다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned room late at night, lit only by a small desk lamp. On the left 40% of the frame,
a fictional Korean office worker around 40 years old (plain shirt), sitting and holding a smartphone, the other hand
covering the mouth, frozen stunned and regretful expression, face lit by the phone's cold light. The face and the phone
are in the upper 60% of the frame; the lower body fades into darkness at the bottom. The phone screen shows only a simple
line that rises briefly in red and then turns blue and drops sharply, no app interface, no text. Fictional person, not
resembling any real or famous person, natural Korean features, realistic photo style. In the upper right area, large bold
text "일곱 배에 샀다" in off-white, where only the words "일곱 배" sit on a solid bright yellow (#FFD400) box with black
text. Below it, still in the upper 60%, a wide solid blue (#2D6CDF) rounded box with a thin white border containing the
huge white bold text "-1,000만 원", the largest element. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "말만 듣고 올라탄 주식", line 2 "+380만원에서 -1천만원". In line 2, "+380만원" is red #E63B2E and "-1천만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Realistic photo style. Dark navy-toned room late at night, lit only by a small desk lamp. On the left 40% of the frame, a
fictional Korean office worker around 40 years old, holding a smartphone, the other hand covering the mouth, stunned and
regretful expression, face lit by the phone's cold light; the phone screen shows only a simple line that rises briefly in
red and then turns blue and drops sharply. The face and the phone are in the upper 60% of the frame. Fictional person, not
resembling any real or famous person. In the upper right area, calm dark empty space for a short headline with a small
empty bright yellow box at its left, and below it an empty solid blue (#2D6CDF) rounded box with thin white border, both
in the upper 60%. The lower third is a dark band (black to dark navy) that fades upward from the bottom edge, with clean
empty space for two lines of large text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "일곱 배에 샀다" · "-1,000만 원" · "말만 듣고 올라탄 주식" · "+380만원에서 -1천만원"이 한 글자도 틀리지 않음 (문장 1·2, 제목 T2와 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음 (한 줄 14자 이내: 12자·14자, 2줄 합 26자) · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 얼굴·휴대폰·"일곱 배에 샀다"·숫자 상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 펀치 문구는 "일곱 배에 샀다" 1개
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 표정은 당황·후회 수준 (울음·극단적 공포 없음) · 성별은 사연자 목소리와 맞춤 (위 메모)
- [ ] 휴대폰 화면에 앱 이름·로고·글자 없음 · 종목명·티커 없음
- [ ] 320px 축소본에서 얼굴 표정, "-1,000만 원", 하단 2줄이 읽힘
- [ ] 강조색 3곳 이하 (노랑 상자 "일곱 배", 빨강 "+380만원", 노랑 "-1천만원") · 손실 숫자에 빨강 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
