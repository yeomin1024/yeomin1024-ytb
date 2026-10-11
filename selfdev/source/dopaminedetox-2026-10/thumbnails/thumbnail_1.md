# dopaminedetox-2026-10 썸네일 1 — 숫자 반전 (서랍 속 휴대폰 → 월요일 9시간)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `guides/thumbnail_guide.md` v1.3 1번 2·3항·4-2, `selfdev/guides/thumbnail_rules.md` v1.1, 대본 `dopaminedetox-2026-10.txt` v1.0 기준 (v1.0: 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 서랍에 넣은 휴대폰(주말 48시간 끊음)이 **"9시간"**으로 뒤집히는 숫자 반전이 가장 빨리 읽히고 클릭을 부른다 |
| 짝 제목 | `titles.md` **T1 (채택)** "도파민 디톡스 한다고 주말 48시간 폰을 끊었는데 월요일에만 9시간을 봤습니다 …" — 하단 2줄 = 이 제목 앞 문장을 줄인 것. T3과도 어울림 |
| 숫자 근거 | 문장 7 "5월 8일 금요일 밤 10시, 휴대폰을 서랍에 넣고 …" (0:32) · 문장 9 "일요일 밤 10시, 48시간을 채우자 …" (0:43) · 문장 12 "월요일 하루에만 화면 시간이 9시간" (0:55.8) → 모두 1분 안 |

## 화면 구성
- 다크 네이비 배경(#14213D), 장식 없음
- **위쪽 약 60% (y 약 40~420) = 그림 영역** — 하단 2줄을 가리지 않게 줄여서 배치
  - 왼쪽 35%: 반쯤 열린 나무 책상 서랍 안에 **엎어 놓은 휴대폰** 한 대 (화면 꺼짐)
  - 가운데: 굵은 흰색 화살표(→)
  - 오른쪽 50%: 화면이 켜진 휴대폰 한 대 — 화면에는 **앱 이름·로고·글자 없는 단순한 막대 몇 개**만 있고 마지막 막대만 빨강으로 아주 높음
    - 휴대폰 바로 옆에 아주 큰 빨강 **"9시간"** (핵심 숫자, 흰 테두리, 화면에서 가장 큰 글자, 화면 높이의 약 28%)
  - 펀치 문구는 두지 않는다 (전에 있던 "48시간 끊고"·"월요일"은 하단 2줄로 옮김)
- **아래쪽 약 35% (y 약 450~690) = 하단 제목 2줄** — 아래에서 위로 옅어지는 검정 띠(불투명 약 80%) 위, 왼쪽 정렬 x 48부터, 흰 글자 + 두꺼운 검정 외곽선, 글자 높이 약 90px
  - 1줄 "주말 48시간 폰 끊고" — "48시간"만 노랑 (처음 목표 숫자)
  - 2줄 "월요일에만 9시간 봤다" — 오른쪽 끝은 x 1040 안
- 강조 3곳: 빨강 막대 · 큰 빨강 "9시간" · 하단 "48시간" 노랑
- 인물 없음 · 뇌 그림 없음 · 오른쪽 아래 구석 비움 · 글자와 휴대폰은 가운데 16:9 안

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 핵심 숫자 | 9시간 | 빨강 #E63B2E (잃은 것), 흰 테두리 | 위쪽에서 가장 큰 글자 |
| 하단 1줄 (12자) | 주말 48시간 폰 끊고 | 흰색 + 두꺼운 검정 외곽선 | "48시간"만 노랑 #FFD400 (처음 목표 숫자) |
| 하단 2줄 (12자) | 월요일에만 9시간 봤다 | 흰색 + 두꺼운 검정 외곽선 | — (빨강은 위쪽 "9시간"에 이미 있음) |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, blue #2D6CDF (what was hoped for), red #E63B2E (what was lost).
Bottom-right corner kept empty (video length badge).
Clean semi-flat illustration on a plain dark navy (#14213D) background.
Upper 60% of the frame: on the left 35%, a half-open wooden desk drawer seen from the front, with one smartphone lying face-down inside, screen off. In the center, a thick white arrow pointing right. On the right half, one upright smartphone with its screen on; the screen shows only five or six plain flat vertical bars with no labels, no numbers, no icons and no app interface, and the last bar is red (#E63B2E) and much taller than the others. Right next to the phone, the huge red (#E63B2E) bold text "9시간" with a thin white outline, the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "주말 48시간 폰 끊고", line 2 "월요일에만 9시간 봤다". The word "48시간" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
No people, no brain images, no app logos, no real phone operating system screens. Keep all text and both phones inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, red #E63B2E.
Clean semi-flat illustration on a plain dark navy background.
Upper 60% of the frame: on the left 35%, a half-open wooden desk drawer with one smartphone lying face-down inside, screen off. A thick white arrow in the center pointing right. On the right half, one upright smartphone whose screen shows only five or six plain flat vertical bars with no labels or icons, the last bar red and much taller; large empty dark space right next to the phone for a huge number.
Lower third: a dark band (black, about 80% opaque, fading upward from the bottom edge) with clean empty space for two lines of headline text starting near the left edge.
No people, no brain images, no logos. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "9시간" · "주말 48시간 폰 끊고" · "월요일에만 9시간 봤다"가 한 글자도 틀리지 않음, 그 밖의 글자·숫자 없음 (막대그래프에 눈금·요일·숫자 없음)
- [ ] 숫자가 대본(문장 9 "48시간", 문장 12 "9시간")·제목 T1과 같음
- [ ] 아래쪽 약 35%에 하단 2줄이 크게 있음 (12자·12자, 합 24자 — 한 줄 14자 이내, 합 26자 이내) · 어두운 띠 위 흰 글자 + 검정 외곽선 · 2줄 오른쪽 끝이 구석 앞에서 끝남
- [ ] 서랍·화살표·휴대폰·"9시간"이 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 글자는 "9시간" 하나 (펀치 문구 없음)
- [ ] 강조 3곳(빨강 막대 · 빨강 "9시간" · 하단 "48시간" 노랑) · "9시간"이 가장 크고 빨강
- [ ] 휴대폰 화면이 실제 운영체제의 화면 시간 기능·숏폼 앱처럼 보이지 않음 (로고·아이콘·레이아웃 없음) · 뇌 그림 없음
- [ ] 320px 축소본에서 "9시간"과 하단 2줄이 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
