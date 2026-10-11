# supplement-liver-2026-10 썸네일 2 — 인물·감정 장면

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `health/guides/thumbnail_rules.md` v1.1 4·5번: 가상 인물, 의사·병원 장면 금지, 라벨 없는 흰 통), 대본 supplement-liver-2026-10.txt v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 식탁 위 영양제 통 앞에서 결과지를 든 **50대 여성의 걱정스러운 표정**이 숫자 카드보다 감정을 더 끈다 |
| 짝 제목 | `titles.md` T2 "검진 결과지의 간수치 24가 2년 만에 89가 됐습니다. 영양제 9가지 챙겨 먹은 50대의 불편한 진실" — T1과도 어울림 |
| 숫자 근거 | 문장 3 "그때 저는 쉰하나 … 직장인" · 문장 5 "몸에 좋다는 영양제를 보면 하나씩" · 문장 9 "아침저녁으로 한 줌씩" · 문장 11 "올해 결과지의 간수치는 89" (0:51) |

## 화면 구성
- 밝은 아침 식탁, 크림 톤 배경을 흐리게. 왼쪽 45%: **가상 인물** — 50대 초반 한국인 여성 직장인(단정한 블라우스), 건강검진 결과지 한 장을 들고 놀라고 걱정스러운 표정
  - 종이는 뒷면이거나 흐려서 글자가 보이지 않는다
- 인물 앞 식탁: **라벨·글자·로고가 없는 흰 플라스틱 통 여러 개**(6~9개, 모양 단순)와 손바닥만 한 접시에 알약 한 줌 (쏟아붓는 연출 없음)
- 오른쪽: 위에 **"좋다길래"** (잉크 글자, 노랑 상자), 아래 빨강 상자 안 흰 글자 **"간수치 89"** ("89"가 가장 큼)
- 오른쪽 아래 구석은 비움. 얼굴과 글자는 가운데 16:9 안에

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 속마음 | 좋다길래 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 노랑) |
| 결과 | 간수치 89 | 흰 글자 (빨강 #E63B2E 상자) | "89"를 가장 크게 |

전체 8자. 짝 제목 T2에 없는 속마음 "좋다길래"를 보탠다.

## [A] 완성형 프롬프트
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A bright home kitchen table in the morning, background softly blurred in warm cream tones.
On the left 45% of the frame, a fictional Korean woman in her early 50s, office-worker look (neat blouse), holding a
single health checkup result sheet in her hands, the sheet facing away or blurred so no text is readable, surprised and
worried expression looking at the paper. Fictional person, not resembling any real or famous person, natural Korean
features. Not a doctor, no white coat, no hospital, no needles. On the table in front of her: several plain white plastic
supplement bottles with absolutely no labels, no text, no logos and no brand-like colors, and a small saucer with a modest
handful of pills (no pills pouring or spilling). On the right side, large bold headline text "좋다길래" in ink black on a
solid bright yellow (#FFD400) box. Below it, a wide solid red (#E63B2E) rounded box containing the white bold text
"간수치 89", with the number "89" much larger than the word. No crying, no extreme fear.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, gain red #E63B2E.
Realistic photo style. A bright home kitchen table in the morning, softly blurred cream background. On the left 45% of
the frame, a fictional Korean woman in her early 50s holding a blank health checkup sheet, surprised and worried
expression. Fictional person, not resembling any real or famous person. Not a doctor, no hospital. On the table, several
plain white unlabeled supplement bottles and a small saucer with a modest handful of pills. The right 50% of the frame is
calm empty space for headline text, with an empty solid yellow box at the upper right and an empty solid red rounded box
below it. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "좋다길래" · "간수치 89"가 한 글자도 틀리지 않음 · 결과지·통에 읽히는 글자 없음 · 물음표·느낌표 없음
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 의사·흰 가운·병원·주사 없음 · 표정은 놀람·걱정 수준
- [ ] 영양제 통에 라벨·상표·제품 같은 색 조합이 없음 · 알약을 쏟아붓는 과장 없음
- [ ] 320px 축소본에서 표정과 "89"가 읽힘 · 노랑 강조 1곳 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
