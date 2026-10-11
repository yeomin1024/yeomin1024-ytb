# prediabetes-2026-10 썸네일 2 — 인물·감정 장면

버전: v1.2 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3). 인물·숫자를 위쪽 약 60%로 올리고, 그림 영역 글자를 빨강 상자 "공복혈당 131" 하나로 줄임 ("멀쩡했는데"는 하단 1줄 "아픈 데 없다며 넘긴"과 같은 뜻이라 뺌), 하단 2줄 "아픈 데 없다며 넘긴 / 108이 3년 만에 131" 추가 (`guides/thumbnail_guide.md` v1.3, `health/guides/thumbnail_rules.md` v1.2), 대본 v1.1 기준 (v1.1: 2026-10-11 짝 제목을 새 T2로, 문구 "괜찮다고?" → "멀쩡했는데" — `thumbnail_rules.md` v1.1 6번: 물음표·느낌표 금지 / v1.0: 2026-10-10 최초 작성, `thumbnail_rules.md` v1.0 3번: 가상 인물, 의사·병원 장면 금지)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 결과지를 든 **사람의 표정**이 숫자 카드보다 감정을 더 끈다 |
| 짝 제목 | `titles.md` T2 "아픈 데 없다며 넘긴 공복혈당 108이 3년 만에 131이 됐습니다. 당뇨 전단계 무시한 사람들의 후회" — 하단 2줄 = 이 앞 문장을 줄인 것 |
| 숫자 근거 | 문장 1 "3년 전 … 공복혈당 108" (0:00) · 문장 4 "아픈 데도 없고" (0:15) · 문장 28 "사연자도 3년 동안 아픈 곳이 한 군데도 없었죠" · 문장 8 "공복혈당 131" (0:33) |

## 화면 구성
- **위쪽 약 60% (y 0~430):** 크림색 사무실 배경을 흐리게
  - 왼쪽 40~45%: **가상 인물** — 50대 초반 한국인 남성 직장인(셔츠, 넥타이 느슨하게), 건강검진 결과지 한 장을 가슴 높이에서 두 손으로 들고 놀라고 걱정스러운 표정. 허리 위까지만 보이게 잡아 얼굴·손·종이가 모두 위쪽 60% 안에 온다 (그 아래는 하단 띠 밑으로 어두워짐)
    - 종이에는 글자가 보이지 않는다 (뒷면 또는 흐림)
  - 오른쪽 위: 빨강 둥근 상자 안 흰 글자 **"공복혈당 131"** — "131"이 화면에서 가장 큰 글자 (하단 2줄보다 큼). "공복혈당"이 그림 영역의 유일한 펀치 문구
- **아래쪽 약 35% (y 약 450~690):** 아래에서 위로 옅어지는 다크 네이비 띠 위에 하단 2줄. 왼쪽 정렬 x 48부터, 흰 글자 + 두꺼운 검정 외곽선, 글자 높이 약 80~100px. "108"만 노랑. 2번째 줄은 x 1040 안에서 끝남
- 오른쪽 아래 구석(약 220×70)은 비움. 얼굴과 글자는 가운데 16:9 안에

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 + 결과 숫자 (오른쪽 위) | 공복혈당 131 | 흰 글자 (빨강 #E63B2E 상자) | "131"을 가장 크게 |
| 하단 1줄 | 아픈 데 없다며 넘긴 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 없음 |
| 하단 2줄 | 108이 3년 만에 131 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "108"만 노랑 #FFD400 (처음 숫자) |

- 하단 2줄 = 짝 제목 T2 앞 문장 "아픈 데 없다며 넘긴 공복혈당 108이 3년 만에 131이 됐습니다"를 줄인 것 (제목 단어를 그대로 씀, "공복혈당"은 그림 쪽 상자에). 1줄 11자 · 2줄 14자, 합 25자 (띄어쓰기 포함)
- 펀치 "공복혈당"(4자)은 하단 2줄에 없는 말이다. 131은 위아래 모두 나온다 (숫자 반복은 허용)
- 강조 합 2곳: 빨강 상자 "공복혈당 131", 노랑 "108". 노랑 상자 없음, 파랑 글자 없음

## [A] 완성형 프롬프트
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Softly blurred bright office background in warm cream tones. On the left 40% of the frame, a
fictional Korean man in his early 50s, office-worker look (white shirt, loosened tie), shown from the waist up, holding a
single health checkup result sheet with both hands at chest height, the sheet facing away or blurred so no text is
readable, surprised and worried expression looking at the paper. His face, hands and the sheet are all in the upper 60%
of the frame. Fictional person, not resembling any real or famous person, natural Korean features. Not a doctor, no white
coat, no hospital, no needles. On the upper right side, a wide solid red (#E63B2E) rounded box containing the white bold
text "공복혈당 131", with the number "131" much larger than the word, the largest text in the image. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "아픈 데 없다며 넘긴", line 2 "108이 3년 만에 131". The word "108" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, gain red #E63B2E.
Realistic photo style. Softly blurred bright office background. On the left 40% of the frame, a fictional Korean man in
his early 50s, office-worker look, shown from the waist up, holding a blank health checkup sheet with both hands at chest
height, surprised and worried expression, his face and hands in the upper 60% of the frame. Fictional person, not
resembling any real or famous person. Not a doctor, no hospital. On the upper right, an empty solid red (#E63B2E) rounded
box with calm empty space around it.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, completely empty, reserved for two lines of
headline text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "공복혈당 131" · "아픈 데 없다며 넘긴" · "108이 3년 만에 131"이 한 글자도 틀리지 않음 · 결과지에 읽히는 글자 없음 · 물음표·느낌표 없음 · 그 밖의 글자 없음
- [ ] 숫자가 대본(문장 1·8)·제목 T2와 같음 — 108, 131, 3년
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 의사·흰 가운·병원·주사 없음 · 표정은 놀람·걱정 수준
- [ ] 얼굴·종이·빨강 상자가 위쪽 약 60% 안에 있어 하단 2줄을 가리지 않음 · 그림 영역 문구는 "공복혈당 131" 상자 1개뿐
- [ ] 하단 2줄이 아래쪽 약 35%에 크게 있음, 왼쪽 정렬, 2번째 줄이 오른쪽 아래 구석 전에 끝남 · 한 줄 14자 이내(11자·14자), 2줄 합 26자 이내(25자)
- [ ] "131"(빨강 상자)이 가장 큼 · 강조는 빨강 상자 1곳, 노랑 "108" 1곳 · 파랑 글자 없음
- [ ] 320px 축소본에서 표정, "131", 하단 2줄이 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
