# prediabetes-2026-10 썸네일 1 — 결과지 숫자 반전

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3). 결과지 카드를 위쪽 약 60%로 줄이고, 그림 영역 글자를 펀치 "공복혈당" + 숫자 108 → 131로 줄임 ("경계"·"당뇨" 상자와 화살표 위 "3년"은 빼고 하단 2줄로 옮김), 하단 2줄 "'경계'라 넘겼다가 / 3년 만에 당뇨가 됐다" 추가 (`guides/thumbnail_guide.md` v1.3, `health/guides/thumbnail_rules.md` v1.2), 대본 prediabetes-2026-10.txt v1.1 기준 (v1.0: 2026-10-10 최초 작성, `guides/thumbnail_guide.md` v1.1, `health/guides/thumbnail_rules.md` v1.0, 대본 v1.0)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 결과지 숫자가 '경계'에서 '당뇨'로 뒤집힌 장면이 가장 빨리 읽힌다 (주식의 계좌 숫자 반전과 같은 축) |
| 짝 제목 | `titles.md` T1 (채택) "공복혈당 108 '경계'라 괜찮다고 넘겼다가 3년 만에 당뇨가 됐습니다 …" — 하단 2줄 = 이 앞 문장을 줄인 것 |
| 숫자 근거 | 문장 1~2 "3년 전 … 공복혈당 108 … '공복혈당장애 의심'" (0:00) · 문장 5 "아직 경계라며 웃어넘겼어요" (0:20) · 문장 8 "공복혈당 131, '당뇨병 의심'" (0:33) · 문장 9 "당뇨병이라는 진단" (0:39) → 모두 1분 안 |

## 화면 구성
- **위쪽 약 60% (y 0~430):** 크림 배경, 단순한 평면 그림
  - 맨 위 가운데: 노랑 상자 안 잉크 글자 **"공복혈당"** (펀치 문구, 유일한 노랑)
  - 그 아래 단순한 건강검진 결과지 카드 2장이 겹쳐 놓여 있다 (기관 로고·이름·바코드·환자 정보·작은 글씨 없음, 글자는 아래 문구뿐)
  - 왼쪽 뒤 카드 (작게): 잉크 **"108"** · 오른쪽 앞 카드 (더 크게): 빨강 **"131"** — 화면에서 가장 큰 요소 (화면 높이의 약 25%, 하단 2줄보다 큼)
  - 두 카드 사이 굵은 잉크 화살표 (왼쪽 → 오른쪽, 화살표 위 글자 없음)
- **아래쪽 약 35% (y 약 450~690):** 아래에서 위로 옅어지는 다크 네이비 띠 위에 하단 2줄. 왼쪽 정렬 x 48부터, 흰 글자 + 두꺼운 검정 외곽선, 글자 높이 약 80~100px. "당뇨"만 빨강. 2번째 줄은 x 1040 안에서 끝남
- 오른쪽 아래 구석(약 220×70)은 비움. 글자는 가운데 16:9 안에

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위 가운데) | 공복혈당 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 노랑) |
| 처음 숫자 | 108 | 잉크 #1E1E1E | 중간 크기, 왼쪽 뒤 카드 |
| 결과 숫자 | 131 | 빨강 #E63B2E | 가장 큰 글자, 오른쪽 앞 카드 |
| 하단 1줄 | '경계'라 넘겼다가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 없음 |
| 하단 2줄 | 3년 만에 당뇨가 됐다 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "당뇨"만 빨강 #E63B2E (나빠진 결과) |

- 하단 2줄 = 채택 제목 앞 문장 "공복혈당 108 '경계'라 괜찮다고 넘겼다가 3년 만에 당뇨가 됐습니다"를 줄인 것 (제목 단어를 그대로 씀). 1줄 10자 · 2줄 12자, 합 22자 (띄어쓰기 포함)
- 펀치 "공복혈당"(4자)은 하단 2줄에 없는 말이다. 108 → 131 숫자는 그림 쪽에만 있다
- 강조 합 3곳: 노랑 상자 "공복혈당", 빨강 "131", 빨강 "당뇨". 파랑 글자 없음

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: clean flat illustration on a cream (#F2EBDD) background. At the top center, a solid bright yellow
(#FFD400) box with the black bold text "공복혈당". Below it, two simple white medical checkup result cards overlap in the
center, with no logos, no institution names, no barcodes, no personal data and no small print. On the smaller card at the
back left, the black number "108" in medium size. A thick black arrow points from the left card to the right card, with
nothing written on or above the arrow. On the larger card in front on the right, the huge red (#E63B2E) number "131", the
largest element in the image (about 25% of the image height). No people, no needles, no blood, no hospital scenes.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "'경계'라 넘겼다가", line 2 "3년 만에 당뇨가 됐다". The word "당뇨" is red #E63B2E. The second line ends well before the bottom-right corner.
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
card for a big number. No logos, no barcodes, no people, no medical scenes.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, completely empty, reserved for two lines of
headline text. Nothing from the picture reaches into this band. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "공복혈당" · "108" · "131" · "'경계'라 넘겼다가" · "3년 만에 당뇨가 됐다"가 한 글자도 틀리지 않음, 그 밖의 글자 없음 (그림 쪽에 "경계"·"당뇨"·"3년"이 따로 나오지 않음)
- [ ] 숫자가 대본(문장 1·8·9)·제목과 같음 — 108, 131, 3년
- [ ] 결과지 카드에 기관 로고·이름·바코드·환자 정보 없음
- [ ] 카드·숫자가 위쪽 약 60% 안에 있어 하단 2줄을 가리지 않음 · 그림 영역 문구는 펀치 "공복혈당" 1개뿐
- [ ] 하단 2줄이 아래쪽 약 35%에 크게 있음, 왼쪽 정렬, 2번째 줄이 오른쪽 아래 구석 전에 끝남 · 한 줄 14자 이내(10자·12자), 2줄 합 26자 이내(22자)
- [ ] "131"이 가장 크고(하단 2줄보다 큼) 빨강 · 강조는 노랑 상자 "공복혈당", 빨강 "131"·"당뇨" 3곳 · 파랑 글자 없음
- [ ] 320px 축소본에서 "108 → 131"과 하단 2줄이 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
