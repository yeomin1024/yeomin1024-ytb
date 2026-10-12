# bonjeon-2026-10 썸네일 2 — 인물·감정 장면

버전: v1.0 — 2026-10-12 — 최초 작성 (`guides/thumbnail_guide.md` v1.3.1, `stock/guides/thumbnail_rules.md` v2.0), 대본 bonjeon-2026-10.txt v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 반년 동안 계좌를 외면하다 결국 손실을 마주한 순간의 **사람 표정**이 숫자 카드보다 "내 얘기"라는 감정을 더 끈다 (작은 채널 성공 썸네일 15개 중 14개에 사람·캐릭터 — `stock/guides/thumbnail_rules.md` 2번) |
| 짝 제목 | `titles.md` T2 "-200만원일 때 못 팔고 버티다 반년 만에 1,600만원을 날렸습니다. …" — T1(채택)·T3과도 어울림 |
| 숫자 근거 | 문장 1 "-200만 원이, -1,600만 원이 됐어요" (0:00) · 문장 3 "2주 만에 -200만 원" (0:10) · 문장 6 "반년을 버텼을까요" (0:23) → 사연 30초 안 (추정 SRT 기준) |

> **인물 = 사연자: 40대 초반 한국인 남성 직장인 (가상 인물).** 사연자 목소리가 S07 "40대 초반 남성 직장인"으로 정해졌다 (`voices/storyteller.json`, 2026-10-12). 노후·은퇴를 떠올리게 하는 설정(백발, 은퇴 소품)은 넣지 않는다 (`stock/guides/script_rules.md` 1번).

## 화면 구성
- 다크 네이비 톤의 늦은 밤 거실, 소파 옆 스탠드 불빛만
- **위쪽 약 60%** (y 0~430)
  - 왼쪽 40~45%: **가상 인물** — 40대 초반 한국인 남성 직장인 (셔츠 차림, 넥타이를 느슨하게 푼 퇴근 후 모습), 오랫동안 안 열어 본 휴대폰을 이제야 들여다보며 이마를 짚은 굳은 표정 (허탈·후회)
    - 얼굴과 휴대폰은 위쪽 60% 안. 상반신 아래는 하단 띠 속으로 어둡게 사라진다 (하단 2줄이 얼굴을 가리지 않게).
    - 휴대폰 불빛이 얼굴을 비춘다. 휴대폰 화면에는 계단처럼 꺾이며 길게 내려가는 파란 선만 있다 (앱 화면·글자 없음).
  - 오른쪽: 위에 펀치 **"반년을 버텼다"** (흰 글자, "반년"만 노랑 상자 + 검정 글자), 아래에 파랑 상자 안 **"-1,600만 원"** (흰 글자, 가장 큼)
- **아래쪽 약 35%** (y 약 450~690): 아래에서 위로 옅어지는 어두운 띠 위에 하단 제목 2줄
  - 왼쪽 정렬 x 48부터, 글자 크기 약 90px. 2번째 줄 끝은 x 약 760 → x 1040 안
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 반년을 버텼다 | 흰색 #F7F3EA ("반년"만 검정) | "반년"에 노랑 상자 (글자 전체 높이, 노랑 상자는 이 1곳만) |
| 결과 숫자 (위쪽) | -1,600만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |
| 하단 1줄 | -200만원일 때 못 팔고 | 흰색 + 검정 외곽선 | — (14자) |
| 하단 2줄 | 1,600만원 날렸다 | 흰색 + 검정 외곽선 | "1,600만원"만 노랑 #FFD400 (11자, 2줄 합 25자) |

- 강조색 2곳: 노랑 상자 "반년", 노랑 "1,600만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (위쪽은 파랑 상자, 하단은 노랑).
- 하단 2줄은 T2 앞 문장("-200만원일 때 못 팔고 버티다 반년 만에 1,600만원을 날렸습니다")을 줄인 것. "반년"은 펀치에 있어 하단에 다시 쓰지 않았다.
- 펀치 "반년을 버텼다"는 문장 6 "반년을 버텼을까요"의 말이다.
- 하단 2줄은 제목 표기("-200만원", "1,600만원"), 위쪽 상자는 영상 계좌 카드 표기("-1,600만 원")다. 값은 같다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned living room late at night, lit only by a small floor lamp next to a sofa. On the
left 40% of the frame, a fictional Korean man in his early 40s, an office worker just home from work (white shirt, loosened
tie), sitting on the sofa edge and finally looking at his smartphone after avoiding it for months, one hand pressed to his
forehead, frozen stunned and regretful expression, face lit by the phone's cold light. The face and the phone are in the
upper 60% of the frame; the lower body fades into darkness at the bottom. The phone screen shows only a simple blue line
that steps down like a staircase and keeps falling, no app interface, no text. Fictional person, not resembling any real
or famous person, natural Korean features, realistic photo style. No gray hair, no retirement props. In the upper right
area, large bold text "반년을 버텼다" in off-white, where only the word "반년" sits on a solid bright yellow (#FFD400) box
with black text. Below it, still in the upper 60%, a wide solid blue (#2D6CDF) rounded box with a thin white border
containing the huge white bold text "-1,600만 원", the largest element. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "-200만원일 때 못 팔고", line 2 "1,600만원 날렸다". In line 2, "1,600만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Realistic photo style. Dark navy-toned living room late at night, lit only by a small floor lamp. On the left 40% of the
frame, a fictional Korean man in his early 40s, an office worker in a white shirt with a loosened tie, holding a smartphone,
one hand pressed to his forehead, stunned and regretful expression, face lit by the phone's cold light; the phone screen
shows only a simple blue line that steps down like a staircase. The face and the phone are in the upper 60% of the frame.
Fictional person, not resembling any real or famous person, no gray hair, no retirement props. In the upper right area,
calm dark empty space for a short headline with a small empty bright yellow box at its left, and below it an empty solid
blue (#2D6CDF) rounded box with thin white border, both in the upper 60%. The lower third is a dark band (black to dark
navy) that fades upward from the bottom edge, with clean empty space for two lines of large text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "반년을 버텼다" · "-1,600만 원" · "-200만원일 때 못 팔고" · "1,600만원 날렸다"가 한 글자도 틀리지 않음 (문장 1·3·6, 제목 T2와 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음 (한 줄 14자 이내: 14자·11자, 2줄 합 25자) · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 얼굴·휴대폰·"반년을 버텼다"·숫자 상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 펀치 문구는 "반년을 버텼다" 1개
- [ ] 인물이 40대 초반 남성 직장인(사연자 목소리와 같음)이고 실존 인물·유명인을 닮지 않음 · 표정은 허탈·후회 수준 (울음·극단적 공포 없음) · 노후 설정 없음
- [ ] 휴대폰 화면에 앱 이름·로고·글자 없음 · 종목명·티커 없음
- [ ] 320px 축소본에서 얼굴 표정, "-1,600만 원", 하단 2줄이 읽힘
- [ ] 강조색 3곳 이하 (노랑 상자 "반년", 노랑 "1,600만원") · 손실 숫자에 빨강 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
