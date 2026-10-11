# supplement-liver-2026-10 썸네일 1 — 결과지 숫자 반전

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3). 결과지 카드를 위쪽 약 60%로 줄이고, 그림 영역 글자를 펀치 "몸에 좋다길래" + 숫자 24 → 89로 줄임 ("간수치(ALT)"는 하단 2줄의 "간수치"와 겹쳐 펀치를 채택 제목의 속마음 훅으로 바꿈, 화살표 위 "2년"은 뺌), 하단 2줄 "영양제 9가지로 늘렸다가 / 간수치 89가 됐다" 추가 (`guides/thumbnail_guide.md` v1.3, `health/guides/thumbnail_rules.md` v1.2), 대본 supplement-liver-2026-10.txt v1.0 기준 (v1.0: 2026-10-11 최초 작성, `guides/thumbnail_guide.md` v1.2, `health/guides/thumbnail_rules.md` v1.1)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 결과지 간수치가 24에서 89로 뛴 **숫자 반전** 하나가 가장 빨리 읽힌다 (롱폼 숫자 제목 54.5% — `data_insights.md` 3번) |
| 짝 제목 | `titles.md` T1 (채택) "몸에 좋다길래 영양제를 9가지로 늘렸다가 간수치 24가 89가 됐습니다 …" — 하단 2줄 = 이 앞 문장을 줄인 것. T2·T3과도 어울림 (세 제목 모두 24→89) |
| 숫자 근거 | 문장 1 "2년 전 … 간수치는 24" (0:00) · 문장 5 "몸에 좋다는 영양제를 보면 하나씩" (0:18) · 문장 8 "2년 만에 9가지, 하루 14알" (0:35) · 문장 11 "올해 결과지의 간수치는 89" (0:51) → 모두 1분 안 |

## 화면 구성
- **위쪽 약 60% (y 0~430):** 크림 배경, 단순한 평면 그림
  - 맨 위 가운데: 노랑 상자 안 잉크 글자 **"몸에 좋다길래"** (펀치 문구 = 믿었던 말, 유일한 노랑)
  - 그 아래 단순한 건강검진 결과지 카드 2장이 겹쳐 놓여 있다 (기관 로고·이름·바코드·환자 정보·작은 글씨 없음, 글자는 아래 문구뿐)
  - 왼쪽 뒤 카드 (작게): 잉크 **"24"** · 오른쪽 앞 카드 (더 크게): 빨강 **"89"** — 화면에서 가장 큰 요소 (화면 높이의 약 25%, 하단 2줄보다 큼)
  - 두 카드 사이 굵은 잉크 화살표 (왼쪽 → 오른쪽, 화살표 위 글자 없음)
  - 간 그림·해부도·알약·인물 없음
- **아래쪽 약 35% (y 약 450~690):** 아래에서 위로 옅어지는 다크 네이비 띠 위에 하단 2줄. 왼쪽 정렬 x 48부터, 흰 글자 + 두꺼운 검정 외곽선, 글자 높이 약 80~100px. "89"만 빨강. 2번째 줄은 x 1040 안에서 끝남
- 오른쪽 아래 구석(약 220×70)은 비움. 글자는 가운데 16:9 안에

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위 가운데) | 몸에 좋다길래 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 노랑) |
| 처음 숫자 | 24 | 잉크 #1E1E1E | 중간 크기, 왼쪽 뒤 카드 |
| 결과 숫자 | 89 | 빨강 #E63B2E | 가장 큰 글자, 오른쪽 앞 카드 |
| 하단 1줄 | 영양제 9가지로 늘렸다가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 없음 |
| 하단 2줄 | 간수치 89가 됐다 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "89"만 빨강 #E63B2E (높아진 수치) |

- 하단 2줄 = 채택 제목 앞 문장 "몸에 좋다길래 영양제를 9가지로 늘렸다가 간수치 24가 89가 됐습니다"를 줄인 것 (제목 단어를 그대로 씀). 1줄 13자 · 2줄 10자, 합 23자 (띄어쓰기 포함)
- 펀치 "몸에 좋다길래"(7자)는 하단 2줄에 없는 말이다. 89는 위아래 모두 나온다 (숫자 반복은 허용)
- 강조 합 3곳: 노랑 상자 "몸에 좋다길래", 빨강 "89"(카드), 빨강 "89"(하단). 파랑 글자 없음

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: clean flat illustration on a cream (#F2EBDD) background. At the top center, a solid bright yellow
(#FFD400) box with the black bold text "몸에 좋다길래". Below it, two simple white medical checkup result cards overlap in
the center, with no logos, no institution names, no barcodes, no personal data and no small print. On the smaller card at
the back left, the black number "24" in medium size. A thick black arrow points from the left card to the right card, with
nothing written on or above the arrow. On the larger card in front on the right, the huge red (#E63B2E) number "89", the
largest element in the image (about 25% of the image height). No pills, no bottles, no liver or organ drawings, no people,
no needles, no hospital scenes.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "영양제 9가지로 늘렸다가", line 2 "간수치 89가 됐다". The word "89" is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, gain red #E63B2E.
Upper 60% of the frame: clean flat illustration on a cream background. An empty solid yellow box at the top center. Below
it, two simple blank white checkup result cards overlap in the center, the right one larger and in front, with a thick
black arrow from the left card to the right card. Smaller empty space on the left card and large empty space on the right
card for a big number. No logos, no barcodes, no pills, no organs, no people, no medical scenes.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, completely empty, reserved for two lines of
headline text. Nothing from the picture reaches into this band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "몸에 좋다길래" · "24" · "89" · "영양제 9가지로 늘렸다가" · "간수치 89가 됐다"가 한 글자도 틀리지 않음, 그 밖의 글자 없음 (그림 쪽에 "간수치(ALT)"·"2년"이 나오지 않음)
- [ ] 숫자가 대본(문장 1·8·11)·제목과 같음 — 24, 9가지, 89
- [ ] 결과지 카드에 기관 로고·이름·바코드·환자 정보 없음 (실제 결과통보서 서식처럼 보이지 않음) · 간 그림·해부도·알약·주사·병원 장면 없음
- [ ] 카드·숫자가 위쪽 약 60% 안에 있어 하단 2줄을 가리지 않음 · 그림 영역 문구는 펀치 "몸에 좋다길래" 1개뿐
- [ ] 하단 2줄이 아래쪽 약 35%에 크게 있음, 왼쪽 정렬, 2번째 줄이 오른쪽 아래 구석 전에 끝남 · 한 줄 14자 이내(13자·10자), 2줄 합 26자 이내(23자)
- [ ] "89"(카드)가 가장 크고 빨강 · 강조는 노랑 상자 "몸에 좋다길래", 빨강 "89" 두 곳, 합 3곳 · 파랑 글자 없음
- [ ] 320px 축소본에서 "24 → 89"와 하단 2줄이 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
