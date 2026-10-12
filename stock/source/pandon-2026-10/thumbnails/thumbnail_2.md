# pandon-2026-10 썸네일 2 — 인물·감정 장면

버전: v1.0 — 2026-10-12 — 최초 작성 (`guides/thumbnail_guide.md` v1.3.1, `stock/guides/thumbnail_rules.md` v2.0), 대본 pandon-2026-10.txt v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 판돈을 키운 뒤 하루 -22%를 확인한 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (작은 채널 성공 썸네일 15개 중 14개에 사람·캐릭터 — `stock/guides/thumbnail_rules.md` 2번) |
| 짝 제목 | `titles.md` T2 "500만원으로 번 285만원 믿고 판돈 12배 키웠다가 1,288만원 잃었습니다. …" — T1(채택)·T3과도 어울림 |
| 숫자 근거 | 문장 1 "번 285만 원이, 판돈 키운 뒤 -1,288만 원" (0:00) · 문장 4 "기대보다 작은 계약 하나에, 하루 22%가 빠졌어요" (0:18.0) → 사연 30초 안 (추정 SRT 기준). 22% = 2026-01-21 -22.35% (README 검산) |

> **인물은 여성으로 정했다.** 사연자 목소리가 여성(Sohee, `voices/storyteller.json`)이라 사연자와 맞췄다. 대본에 나이·직업을 쓰지 않았으므로 "30대 후반 직장인" 정도로만 그린다 (노후 등 대본에 없는 설정은 넣지 않음 — `thumbnail_rules.md` 4번).

## 화면 구성
- 다크 네이비 배경. 사무실 책상 앞 (점심시간 같은 낮 장면 — 국내 장중), 창밖 빛은 흐리게
- **위쪽 약 60%** (y 0~430)
  - 왼쪽 40~45%: **가상 인물** — 30대 후반 한국인 여성 직장인, 휴대폰을 든 채 다른 손으로 이마를 짚고 굳은 표정 (허탈·후회)
    - 얼굴과 휴대폰은 위쪽 60% 안. 상반신 아래쪽은 하단 띠 속으로 어둡게 사라진다 (하단 2줄이 얼굴을 가리지 않게).
    - 휴대폰 화면에는 오르던 선이 파랗게 뚝 떨어지는 선만 있다 (앱 화면·글자 없음).
  - 오른쪽: 펀치 **"하루 -22%"** (흰 글자, "-22%"만 노랑 상자 + 검정 글자), 가장 큰 글자
- **아래쪽 약 35%** (y 약 450~690): 아래에서 위로 옅어지는 어두운 띠 위에 하단 제목 2줄
  - 왼쪽 정렬 x 48부터, 글자 크기 약 92px (한글 높이 약 87px). 2번째 줄 끝은 x 약 880 → x 1040 안
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 하루 -22% | 흰색 #F7F3EA ("-22%"만 검정) | "-22%"에 노랑 상자 (글자 전체 높이, 노랑 상자는 이 1곳만) |
| 하단 1줄 | 번 돈 믿고 키운 판돈 | 흰색 + 검정 외곽선 | — (12자) |
| 하단 2줄 | 1,288만원 잃었습니다 | 흰색 + 검정 외곽선 | "1,288만원"만 노랑 #FFD400 (13자, 2줄 합 25자) |

- 강조색 2곳: 노랑 상자 "-22%", 노랑 "1,288만원"(손실). 빨강은 쓰지 않는다 (이 채널에서 빨강 = 수익).
- 하단 2줄은 T2 앞 문장("500만원으로 번 285만원 믿고 판돈 12배 키웠다가 1,288만원 잃었습니다")을 줄인 것. "번 285만원 믿고 판돈 키웠다가"를 "번 돈 믿고 키운 판돈"으로 줄였다.
- 펀치 "하루 -22%"는 문장 4(0:18.0)와 문장 79 "1월 21일, 주가는 22.35% 떨어진 37만 3,500원"의 말이다. 대본·제목의 손실 금액 표기 "1,288만원"과 값이 같다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A navy-toned office desk scene in the daytime, soft window light. On the left 40% of the frame,
a fictional Korean woman office worker in her late 30s (plain blouse), sitting and holding a smartphone, the other hand
pressed against her forehead, frozen stunned and regretful expression, face lit by the phone. The face and the phone are
in the upper 60% of the frame; the lower body fades into darkness at the bottom. The phone screen shows only a simple line
that rises and then turns blue and drops sharply, no app interface, no text. Fictional person, not resembling any real or
famous person, natural Korean features, realistic photo style. In the upper right area, the huge bold text "하루 -22%" in
off-white, where only "-22%" sits on a solid bright yellow (#FFD400) box with black text; it is the largest text in the
upper area. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "번 돈 믿고 키운 판돈", line 2 "1,288만원 잃었습니다". The word "1,288만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF.
Realistic photo style. A navy-toned office desk scene in the daytime, soft window light. On the left 40% of the frame, a
fictional Korean woman office worker in her late 30s, holding a smartphone, the other hand pressed against her forehead,
stunned and regretful expression; the phone screen shows only a simple line that rises and then turns blue and drops
sharply. The face and the phone are in the upper 60% of the frame. Fictional person, not resembling any real or famous
person. In the upper right area, calm dark empty space for a short headline with a small empty bright yellow box at its
right end, in the upper 60%. The lower third is a dark band (black to dark navy) that fades upward from the bottom edge,
with clean empty space for two lines of large text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "하루 -22%" · "번 돈 믿고 키운 판돈" · "1,288만원 잃었습니다"가 한 글자도 틀리지 않음 (문장 1·4, 제목 T2와 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음 (한 줄 14자 이내: 12자·13자, 2줄 합 25자) · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 얼굴·휴대폰·"하루 -22%"가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 펀치 문구는 "하루 -22%" 1개
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 표정은 허탈·후회 수준 (울음·극단적 공포 없음) · 여성 (사연자 목소리와 같음)
- [ ] 휴대폰 화면에 앱 이름·로고·글자 없음 · 종목명·티커 없음
- [ ] 320px 축소본에서 얼굴 표정, "하루 -22%", 하단 2줄이 읽힘
- [ ] 강조색 3곳 이하 (노랑 상자 "-22%", 노랑 "1,288만원") · 손실 숫자에 빨강 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
