# multagi-2026-10 썸네일 2 — 인물·감정 장면

버전: v1.2 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `guides/thumbnail_guide.md` v1.3, `stock/guides/thumbnail_rules.md` v1.2, 대본 v1.4 기준. 인물·"본전 오겠지"·숫자를 위쪽 60%로 올리고 하단 2줄 추가 (v1.1: 2026-10-09 사용자 지시로 인물 사용, 사연에 없는 설정의 통장 장면 삭제 → 가상 인물 장면 / v1.0: 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 손실을 확인한 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (성공 썸네일 24개 중 약 20개가 얼굴) |
| 짝 제목 | `titles.md` T2 "본전 금방 온다며 기준 없이 물타서 …" — T1(채택)·T3과도 어울림 |
| 숫자 근거 | 문장 5 "일주일 만에 -200만 원이 됐어요" (0:24) · 문장 8 "조금만 반등해도 본전이라고 생각했어요" (0:41) · 문장 10 "아침, 눈을 뜨자마자 계좌를 열었더니 -2천만 원이 찍혀 있었어요" (0:51) → 1분 안 (오디오에 맞춘 SRT 기준) |

## 화면 구성
- 다크 네이비 배경. 이른 아침의 어두운 방
- **위쪽 약 60%** (y 0~430)
  - 왼쪽 40~45%: **가상 인물** — 40대 초반 한국인 남성 직장인, 휴대폰을 든 채 다른 손으로 이마를 짚고 굳은 표정
    - 얼굴과 휴대폰은 위쪽 60% 안. 상반신 아래쪽은 하단 띠 속으로 어둡게 사라진다 (하단 2줄이 얼굴을 가리지 않게).
    - 휴대폰 불빛이 얼굴을 비춘다. 휴대폰 화면에는 파란 하락 선만 있다 (앱 화면·글자 없음).
  - 오른쪽: 위에 펀치 **"본전 오겠지"** (흰 글자, "본전"만 노랑 상자 + 검정 글자), 아래에 파랑 상자 안 **"-2,000만 원"** (흰 글자, 가장 큼)
- **아래쪽 약 35%** (y 약 450~690): 아래에서 위로 옅어지는 어두운 띠 위에 하단 제목 2줄
  - 왼쪽 정렬 x 48부터, 글자 크기 약 95px (한글 높이 약 90px). 2번째 줄 끝은 x 약 900 → x 1040 안
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 본전 오겠지 | 흰색 #F7F3EA ("본전"만 검정) | "본전"에 노랑 상자 (글자 전체 높이, 노랑 상자는 이 1곳만) |
| 결과 숫자 (위쪽) | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |
| 하단 1줄 | 기준 없이 물타서 | 흰색 + 검정 외곽선 | "기준 없이"만 노랑 #FFD400 (9자) |
| 하단 2줄 | -200만원이 -2천만원 | 흰색 + 검정 외곽선 | — (13자, 2줄 합 22자) |

- 강조색은 2곳: 노랑 상자 "본전", 노랑 글자 "기준 없이". 손실 숫자는 빨강으로 쓰지 않는다 (위쪽은 파랑 상자, 하단은 흰색).
- 하단 2줄은 T2 앞 문장("본전 금방 온다며 기준 없이 물타서 -200만원이 -2천만원이 됐습니다")을 줄인 것. "본전"은 펀치에 있어 하단에 다시 쓰지 않았다.
- "기준 없이"를 노랑으로 고른 이유: 세 제목 모두 "기준 없이"를 넣었다. 물타기 자체가 아니라 기준 없음이 문제라는 메시지다 (`titles.md` 점검).
- 하단 2줄은 제목 표기("-200만원", "-2천만원"), 위쪽 상자는 영상 계좌 카드 표기("-2,000만 원")다. 값은 같다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned room in early morning. On the left 40% of the frame, a fictional Korean man in his
early 40s, office-worker look (plain shirt), sitting and holding a smartphone, his other hand on his forehead, frozen
stunned and regretful expression, face lit by the phone's cold light. His face and the phone are in the upper 60% of the
frame; his lower body fades into darkness at the bottom. The phone screen shows only a simple blue line dropping sharply,
no app interface, no text. Fictional person, not resembling any real or famous person, natural Korean features, realistic
photo style. In the upper right area, large bold text "본전 오겠지" in off-white, where only the word "본전" sits on a solid
bright yellow (#FFD400) box with black text. Below it, still in the upper 60%, a wide solid blue (#2D6CDF) rounded box with
a thin white border containing the huge white bold text "-2,000만 원", the largest element. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "기준 없이 물타서", line 2 "-200만원이 -2천만원". The word "기준 없이" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF.
Realistic photo style. Dark navy-toned room in early morning. On the left 40% of the frame, a fictional Korean man in his
early 40s, office-worker look, holding a smartphone, other hand on his forehead, stunned and regretful expression, face lit
by the phone's cold light; the phone screen shows only a simple blue line dropping sharply. His face and the phone are in
the upper 60% of the frame. Fictional person, not resembling any real or famous person. In the upper right area, calm dark
empty space for a short headline with a small empty bright yellow box at its left, and below it an empty solid blue
(#2D6CDF) rounded box with thin white border, both in the upper 60%. The lower third is a dark band (black to dark navy)
that fades upward from the bottom edge, with clean empty space for two lines of large text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "본전 오겠지" · "-2,000만 원" · "기준 없이 물타서" · "-200만원이 -2천만원"이 한 글자도 틀리지 않음 (문장 5·10, 제목 T2와 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음 (한 줄 14자 이내: 9자·13자, 2줄 합 22자) · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 얼굴·휴대폰·"본전 오겠지"·숫자 상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 펀치 문구는 "본전 오겠지" 1개
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 표정은 당황·후회 수준 (울음·극단적 공포 없음)
- [ ] 휴대폰 화면에 앱 이름·로고·글자 없음 · 종목명 없음
- [ ] 320px 축소본에서 얼굴 표정, "-2,000만 원", 하단 2줄이 읽힘
- [ ] 강조색 2곳 (노랑 상자 "본전", 노랑 "기준 없이") · 손실 숫자에 빨강 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
