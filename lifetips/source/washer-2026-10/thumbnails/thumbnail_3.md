# washer-2026-10 썸네일 3 — 대비 (꿀팁이 약속한 30분 vs 수리비)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `lifetips/guides/thumbnail_rules.md` v1.0), 대본 v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 꿀팁이 약속한 **쉬움("혼자서 30분")과 결과(21만 원)를 나란히** 놓으면, 같은 꿀팁을 본 시청자가 "내 얘기다"를 가장 빨리 느낀다 |
| 짝 제목 | `titles.md` T3 (짧은 변형) "세탁기 청소 방법 따라 하다 수리비 21만원, …" — T2와도 어울림 |
| 숫자 근거 | 문장 3 "혼자서도 30분이면 된다는 분해 청소 영상을 봤죠" (0:11) · 문장 10 "수리비가 21만 원이 나왔어요" (0:48~0:55) → 1분 안 |

## 화면 구성
- 화면을 세로로 반씩 나눔, 가운데에 얇은 흰 세로선
- **왼쪽 (기대)** — 밝은 크림 배경, 깨끗하게 반짝이는 일반형 통돌이 세탁조 안쪽을 위에서 본 모습(스테인리스 통, 물방울 정도). 위에 파랑 글자 **"혼자서 30분"**
- **오른쪽 (결과)** — 다크 네이비 배경, 뚜껑 닫힌 채 멈춘 일반형 흰색 통돌이 세탁기(조명이 꺼진 느낌, 분해·파손 장면 없음). 위에 빨강 상자 + 흰 글자 **"21만 원"** (가장 큼)
- 노랑 강조는 왼쪽·오른쪽 사이 가운데 작은 화살표 하나(→)에만
- 인물 없음 · 공구·물·전선 없음 · 오른쪽 아래 구석은 비움 (오른쪽 그림은 위쪽에 배치)

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 혼자서 30분 | 파랑 #2D6CDF (크림 배경 위) | — |
| 오른쪽 | 21만 원 | 흰색 (빨강 #E63B2E 상자) | 가장 큰 글자 |
| 가운데 | (글자 없음) 노랑 화살표 → | 노랑 #FFD400 | 유일한 강조 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, saved-money blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Split-screen comparison divided vertically in the middle by a thin white line.
LEFT half: bright cream (#F2EBDD) background, a top-down view into the clean shiny stainless inner drum of a plain
generic top-loading washing machine, a few water droplets, fresh and bright. Above it, the large blue (#2D6CDF) bold
text "혼자서 30분".
RIGHT half: dark navy (#14213D) background, a plain generic white top-loading washing machine standing with its lid
closed, looking switched off and stopped, dim lighting, intact (not broken apart, no parts, no water, no smoke).
Above it, in the upper part of the right half, a solid red (#E63B2E) rounded box with the huge white bold text "21만 원",
the largest element in the image.
On the dividing line in the center, one small bright yellow (#FFD400) arrow pointing from left to right.
Washing machines have no brand, no logo and no copied button layout of any real product. No people, no tools.
Keep all text inside the central 16:9 safe area; leave the bottom-right corner empty.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, highlight yellow #FFD400, saved-money blue #2D6CDF, loss red #E63B2E.
Split-screen divided vertically by a thin white line. Left half: bright cream background, top-down view into the clean
shiny stainless inner drum of a plain generic top-loading washing machine, with empty space above it for a headline.
Right half: dark navy background, a plain generic white top-loading washing machine with its lid closed, looking
switched off, dim light, intact; an empty wide solid red (#E63B2E) rounded box in the upper part of the right half.
One small bright yellow arrow on the center line pointing right. No brand, no logo, no people, no tools.
Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "혼자서 30분" · "21만 원"이 한 글자도 틀리지 않음 (문장 3·10)
- [ ] 왼쪽(약속) 파랑, 오른쪽(결과) 빨강 · 노랑은 가운데 화살표 1곳뿐
- [ ] 두 세탁기 모두 상표·로고 없는 일반형 · 분해·파손·공구 장면 없음 (`thumbnail_rules.md` 4·6번)
- [ ] 문구가 제목(T3)을 그대로 반복하지 않음 ("수리비 21만원" 대신 "21만 원"만)
- [ ] 320px 축소본에서 "21만 원"이 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
