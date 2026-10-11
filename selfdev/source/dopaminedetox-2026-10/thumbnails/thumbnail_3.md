# dopaminedetox-2026-10 썸네일 3 — 대비 (일요일 밤 '리셋 완료' vs 월요일 출근길 9시간)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `selfdev/guides/thumbnail_rules.md` v1.0), 대본 `dopaminedetox-2026-10.txt` v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 왼쪽 기대(다이어리의 "리셋 완료")와 오른쪽 결과(월요일 출근길의 "9시간")를 한 화면에 나란히 두면, 문제 분석 첫 메시지("리셋은 일어나지 않는다")가 한눈에 읽힌다 |
| 짝 제목 | `titles.md` **T3 (짧은 변형)** "폰 끊은 주말 48시간, 월요일엔 9시간. 도파민 디톡스의 불편한 진실" — T1·T2와도 어울림 |
| 숫자 근거 | 문장 8 "산책을 두 번 하고, 책도 반 권이나 읽었죠" (0:39) · 문장 10 "다이어리에는 '리셋 완료'라고 적었죠" (0:49) · 문장 12 "월요일 하루에만 화면 시간이 9시간" (0:55.8) · 문장 14 "출근길 지하철에서 … 숏폼으로 넘어갔죠" (1:06) |

## 화면 구성
- 화면을 세로로 반씩 나눔 (가운데 얇은 흰 선)
- **왼쪽 (일요일 밤, 따뜻한 크림 #F2EBDD 톤):** 책상 위에 펼친 종이 다이어리 — 손글씨 **"리셋 완료"**와 체크 표시 하나, 옆에 반쯤 읽은 책(표지 글자 없음)과 운동화 한 켤레. 휴대폰은 보이지 않음 (닫힌 서랍)
- **오른쪽 (월요일 아침, 차가운 다크 네이비 #14213D 톤):** 출근길 지하철 안, 손잡이를 잡고 서서 휴대폰을 들여다보는 **30대 여성 직장인의 뒷모습** (얼굴 보이지 않음, 가상 인물). 휴대폰 화면은 은은한 빛만 (앱 화면 없음). 지하철 안에 노선도·광고·표지판·글자 없음
  - 오른쪽 위에 아주 큰 빨강 **"9시간"** (흰 테두리, 가장 큰 글자)
- 노랑 강조는 왼쪽 "리셋 완료" 아래 형광펜 줄 한 곳
- 오른쪽 아래 구석 비움 · 글자는 가운데 16:9 안

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 기대 (왼쪽) | 리셋 완료 | 잉크 #1E1E1E 손글씨 느낌의 굵은 글자 | 아래에 노랑 #FFD400 형광펜 줄 (유일한 강조) |
| 결과 (오른쪽) | 9시간 | 빨강 #E63B2E (잃은 것), 흰 테두리 | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, blue #2D6CDF (what was hoped for), red #E63B2E (what was lost).
Bottom-right corner kept empty (video length badge).
Split-screen image divided vertically in the middle by a thin white line.
LEFT HALF, warm cream (#F2EBDD) lamplight, Sunday night: a desk with an open paper diary; on the page, the large bold
hand-lettered black Korean text "리셋 완료" with one check mark, and a bright yellow (#FFD400) highlighter stroke under the
text. Beside the diary, a half-read book with a blank cover and a pair of clean sneakers. No phone visible.
RIGHT HALF, cool dark navy (#14213D) tone, Monday morning: inside a commuter subway car, the back view of a fictional
Korean woman in her early 30s in office clothes, standing and holding a hand strap, looking down at a smartphone held
close, the phone giving off a soft glow with no visible interface. Her face is not visible. No route maps, no ads, no
signs, no text anywhere in the subway. In the upper part of the right half, the huge red (#E63B2E) bold text "9시간" with
a thin white outline, the largest element in the image. Fictional person, not resembling any real or famous person.
No brain images, no logos. Keep all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, red #E63B2E.
Split-screen divided vertically by a thin white line. LEFT HALF, warm cream lamplight: a desk with an open blank paper
diary page (large empty area on the page for handwriting), a half-read book with a blank cover and a pair of clean
sneakers, no phone. RIGHT HALF, cool dark navy tone: inside a commuter subway car with no signs or ads, the back view of a
fictional Korean woman in her early 30s in office clothes holding a hand strap and looking down at a softly glowing
smartphone, face not visible; large empty dark space in the upper right for a big number. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "리셋 완료" · "9시간"이 한 글자도 틀리지 않음, 다이어리·책·지하철 안에 다른 글자 없음
- [ ] 숫자가 대본 문장 12 "9시간"·제목과 같음 · 왼쪽 소품(산책 운동화·책 반 권·다이어리)이 대본 문장 8·10과 맞음
- [ ] 인물은 뒷모습만, 실존 인물을 닮지 않음 · 지하철 노선도·광고·실제 회사 로고 없음 · 휴대폰에 앱 화면 없음
- [ ] 노랑 강조 1곳("리셋 완료" 형광펜) · "9시간"이 가장 크고 빨강
- [ ] 320px 축소본에서 "9시간"과 "리셋 완료"가 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
