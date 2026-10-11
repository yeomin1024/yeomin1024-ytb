# dopaminedetox-2026-10 썸네일 1 — 숫자 반전 (서랍 속 휴대폰 → 월요일 9시간)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `selfdev/guides/thumbnail_rules.md` v1.0), 대본 `dopaminedetox-2026-10.txt` v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 서랍에 넣은 휴대폰 "48시간 끊고"가 **"월요일 9시간"**으로 뒤집히는 숫자 반전이 가장 빨리 읽히고 클릭을 부른다 |
| 짝 제목 | `titles.md` **T1 (채택)** "도파민 디톡스 한다고 주말 48시간 폰을 끊었는데 월요일에만 9시간을 봤습니다 …" — T3과도 어울림 |
| 숫자 근거 | 문장 7 "5월 8일 금요일 밤 10시, 휴대폰을 서랍에 넣고 …" (0:32) · 문장 9 "일요일 밤 10시, 48시간을 채우자 …" (0:43) · 문장 12 "월요일 하루에만 화면 시간이 9시간" (0:55.8) → 모두 1분 안 |

## 화면 구성
- 다크 네이비 배경(#14213D), 장식 없음
- 왼쪽 40%: 반쯤 열린 나무 책상 서랍 안에 **엎어 놓은 휴대폰** 한 대 (화면 꺼짐). 서랍 위에 파랑 상자 + 흰 글자 **"48시간 끊고"** (되찾으려던 것 = 파랑)
- 가운데: 굵은 흰색 화살표(→)
- 오른쪽 50%: 화면이 켜진 휴대폰 한 대 — 화면에는 **앱 이름·로고·글자 없는 단순한 막대 몇 개**만 있고 마지막 막대만 빨강으로 아주 높음
  - 휴대폰 옆(또는 위)에 노랑 상자 + 잉크 글자 **"월요일"** (유일한 노랑 강조), 그 아래 아주 큰 빨강 **"9시간"** (흰 테두리, 화면에서 가장 큰 글자, 화면 높이의 약 30%)
- 인물 없음 · 뇌 그림 없음 · 오른쪽 아래 구석 비움 · 글자와 휴대폰은 가운데 16:9 안

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 시작 | 48시간 끊고 | 흰색 | 파랑 #2D6CDF 상자 |
| 결과 1 | 월요일 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (유일한 강조) |
| 결과 2 | 9시간 | 빨강 #E63B2E (잃은 것), 흰 테두리 | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, blue #2D6CDF (what was hoped for), red #E63B2E (what was lost).
Bottom-right corner kept empty (video length badge).
Clean semi-flat illustration on a plain dark navy (#14213D) background. On the left 40% of the frame, a half-open wooden
desk drawer seen from the front, with one smartphone lying face-down inside, screen off. Above the drawer, a solid blue
(#2D6CDF) rounded box with white bold text "48시간 끊고". In the center, a thick white arrow pointing right. On the right
50% of the frame, one upright smartphone with its screen on; the screen shows only five or six plain flat vertical bars
with no labels, no numbers, no icons and no app interface, and the last bar is red (#E63B2E) and much taller than the
others. Next to the phone, a solid bright yellow (#FFD400) box with black bold text "월요일", and directly below it the
huge red (#E63B2E) bold text "9시간" with a thin white outline, the largest element in the image. No people, no brain
images, no app logos, no real phone operating system screens. Keep all text and both phones inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, blue #2D6CDF, red #E63B2E.
Clean semi-flat illustration on a plain dark navy background. On the left 40%, a half-open wooden desk drawer with one
smartphone lying face-down inside, screen off, and an empty solid blue rounded box above the drawer. A thick white arrow
in the center pointing right. On the right, one upright smartphone whose screen shows only five or six plain flat vertical
bars with no labels or icons, the last bar red and much taller. Next to the phone, an empty solid yellow box, and large
empty dark space below it for a huge number. No people, no brain images, no logos. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "48시간 끊고" · "월요일" · "9시간"이 한 글자도 틀리지 않음, 그 밖의 글자·숫자 없음 (막대그래프에 눈금·요일·숫자 없음)
- [ ] 숫자가 대본(문장 9 "48시간", 문장 12 "9시간")·제목 T1과 같음
- [ ] "9시간"이 가장 크고 빨강, 노랑 강조는 "월요일" 한 곳, "48시간 끊고"는 파랑 상자
- [ ] 휴대폰 화면이 실제 운영체제의 화면 시간 기능·숏폼 앱처럼 보이지 않음 (로고·아이콘·레이아웃 없음) · 뇌 그림 없음
- [ ] 320px 축소본에서 "9시간"과 "48시간 끊고"가 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
