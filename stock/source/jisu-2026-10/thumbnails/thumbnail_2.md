# jisu-2026-10 썸네일 2 — 인물·감정 장면

버전: v1.1 — 2026-10-12 — 사연 종목 변경(알테오젠 → 네이버)에 따라 숫자·펀치 교체, 인물을 사연자 목소리(S07, 40대 초반 남성 직장인 — 코디네이터 지시)에 맞춰 40대 초반 남성으로 (v1.0 — 2026-10-12 — 최초 작성), 대본 jisu-2026-10.txt v1.1 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 지수는 두 배가 됐는데 내 계좌만 마이너스인 걸 확인한 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (옛 자료: 작은 채널 성공 썸네일 15개 중 사람·캐릭터 14개 — `stock/guides/thumbnail_rules.md` 2번) |
| 짝 제목 | `titles.md` T2 "남들 수익 인증에 3년 모은 지수를 깨고 900만원을 잃었습니다. …" — T1(채택)·T3과도 어울림 |
| 숫자 근거 | 문장 1 "-900만 원이 됐어요" (0:00) · 문장 4 "코스피가 두 배를 넘은 6월 19일, 제 계좌는 마이너스였어요" (0:17) → 사연 30초 안 (추정 SRT 기준) |

> **인물:** 사연자 목소리가 S07 "40대 초반 남성 직장인"으로 정해졌다 (`voices/storyteller.json`, 코디네이터 지시 2026-10-12). 가상의 40대 초반 한국인 남성 직장인으로 그린다. 대본에 가족·노후 설정은 없다 (노후·퇴직금 설정 금지 — `stock/guides/script_rules.md` 1번).

## 화면 구성
- 다크 네이비 배경. 밤, 책상 스탠드 불빛만 있는 방
- **위쪽 약 60%** (y 0~430)
  - 왼쪽 40~45%: **가상 인물** — 40대 초반 한국인 남성 직장인(셔츠 차림), 휴대폰을 든 채 다른 손으로 이마를 짚고 굳은 표정 (당황·후회)
    - 얼굴과 휴대폰은 위쪽 60% 안. 상반신 아래쪽은 하단 띠 속으로 어둡게 사라진다 (하단 2줄이 얼굴을 가리지 않게).
    - 휴대폰 불빛이 얼굴을 비춘다. 휴대폰 화면에는 파랗게 흘러내리는 선 하나만 있다 (앱 화면·글자 없음).
  - 오른쪽: 위에 펀치 **"코스피는 두 배"** (흰 글자, "두 배"만 빨강 — 상승 = 빨강), 아래에 파랑 상자 안 **"-900만 원"** (흰 글자, 가장 큼)
- **아래쪽 약 35%** (y 약 450~690): 아래에서 위로 옅어지는 어두운 띠 위에 하단 제목 2줄
  - 왼쪽 정렬 x 48부터, 글자 크기 약 92px. 2번째 줄 끝은 x 약 900 → x 1040 안
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 코스피는 두 배 | 흰색 #F7F3EA ("두 배"만 빨강) | "두 배" 빨강 #E63B2E (지수 상승 = 빨강) |
| 결과 숫자 (위쪽) | -900만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |
| 하단 1줄 | 남들 인증에 지수 깨고 | 흰색 + 검정 외곽선 | — (12자) |
| 하단 2줄 | 900만원을 잃었습니다 | 흰색 + 검정 외곽선 | "900만원"만 노랑 #FFD400 (12자, 2줄 합 24자) |

- 강조색 2곳: 빨강 "두 배"(지수 상승), 노랑 "900만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (위쪽은 파랑 상자, 하단은 노랑).
- 하단 2줄은 T2 앞 문장("남들 수익 인증에 3년 모은 지수를 깨고 900만원을 잃었습니다")을 줄인 것.
- 펀치 "코스피는 두 배"는 사연 문장 4("코스피가 두 배를 넘은 6월 19일")의 말이다. 손실은 금액("-900만 원")을 가장 크게 썼다 (`stock/guides/thumbnail_rules.md` 1번).

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned room late at night, lit only by a small desk lamp. On the left 40% of the frame,
a fictional Korean man office worker in his early 40s (plain dress shirt), sitting and holding a smartphone, the other hand
pressed to his forehead, frozen stunned and regretful expression, face lit by the phone's cold light. The face and the phone
are in the upper 60% of the frame; the lower body fades into darkness at the bottom. The phone screen shows only a simple
blue line sliding down, no app interface, no text. Fictional person, not resembling any real or famous person, natural
Korean features, realistic photo style. In the upper right area, large bold text "코스피는 두 배" in off-white, where only
"두 배" is red (#E63B2E). Below it, still in the upper 60%, a wide solid blue (#2D6CDF) rounded box with a thin white border
containing the huge white bold text "-900만 원", the largest element. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "남들 인증에 지수 깨고", line 2 "900만원을 잃었습니다". The word "900만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Realistic photo style. Dark navy-toned room late at night, lit only by a small desk lamp. On the left 40% of the frame, a
fictional Korean man office worker in his early 40s, holding a smartphone, the other hand pressed to his forehead, stunned
and regretful expression, face lit by the phone's cold light; the phone screen shows only a simple blue line sliding down.
The face and the phone are in the upper 60% of the frame. Fictional person, not resembling any real or famous person.
In the upper right area, calm dark empty space for a short headline, and below it an empty solid blue (#2D6CDF) rounded box
with thin white border, both in the upper 60%. The lower third is a dark band (black to dark navy) that fades upward from the
bottom edge, with clean empty space for two lines of large text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "코스피는 두 배" · "-900만 원" · "남들 인증에 지수 깨고" · "900만원을 잃었습니다"가 한 글자도 틀리지 않음 (문장 1·4, 제목 T2와 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음 (한 줄 14자 이내: 12자·12자, 2줄 합 26자 이내) · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 얼굴·휴대폰·펀치·숫자 상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 펀치 문구는 "코스피는 두 배" 1개
- [ ] 인물이 40대 초반 남성(사연자 목소리와 같음)이고 실존 인물·유명인을 닮지 않음 · 표정은 당황·후회 수준 (울음·극단적 공포 없음) · 노후 연상 없음
- [ ] 휴대폰 화면에 앱 이름·로고·글자 없음 · 종목명·상품명·티커 없음
- [ ] 320px 축소본에서 얼굴 표정, "-900만 원", 하단 2줄이 읽힘
- [ ] 강조색 3곳 이하 (빨강 "두 배", 노랑 "900만원") · 손실 숫자에 빨강 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
