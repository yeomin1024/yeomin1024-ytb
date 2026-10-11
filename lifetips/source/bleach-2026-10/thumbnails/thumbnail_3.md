# bleach-2026-10 썸네일 3 — 대비 (꿀팁이 약속한 것 vs 결과)

버전: v1.0 — 2026-10-11 — 최초 작성 (`lifetips/guides/thumbnail_rules.md` v1.0 2번: 왼쪽 = 꿀팁이 약속한 것, 오른쪽 = 결과)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 화면을 둘로 나눠 **"1분이면 끝"이라는 약속**과 **"응급실 4시간"이라는 결과**를 나란히 놓으면 결과가 궁금해 클릭한다 |
| 짝 제목 | `titles.md` T3 (짧은 변형) "화장실 곰팡이 1분 꿀팁이 응급실 4시간 됐습니다 …" |
| 숫자 근거 | 문장 1 "1분이면 곰팡이가 녹는다" (0:00) · 문장 7 "까맣던 줄눈이 하얗게" (0:34) · 문장 10 "응급실에서 4시간" (0:53) |

## 화면 구성
- 세로로 반씩 나눈 화면, 가운데 굵은 크림색 세로 띠
- 왼쪽 반: 밝은 실사 느낌의 흰 타일 벽 클로즈업, 줄눈이 깨끗하게 하얀 상태. 위쪽에 파랑 상자 안 흰 글자 **"1분이면 끝"**
- 오른쪽 반: 다크 네이비 배경 위에 숫자 없는 단순한 벽시계 선 그림(눈금만), 그 아래 빨강 상자 안 흰 글자 **"응급실 4시간"** (가장 큼)
- "끝" 한 글자만 노랑 밑줄 강조 · 인물·병·병원 없음 · 오른쪽 아래 구석은 비움 (빨강 상자는 구석보다 위에)

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 (약속) | 1분이면 끝 | 흰 글자 (파랑 #2D6CDF 상자), "끝" 아래 노랑 밑줄 | 노랑 #FFD400 (유일한 강조) |
| 오른쪽 (결과) | 응급실 4시간 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |

## [A] 완성형 프롬프트
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, safe blue #2D6CDF, cost red #E63B2E.
Bottom-right corner kept empty (video length badge).
Split-screen composition divided vertically into two equal halves by a thick cream (#F2EBDD) vertical stripe.
Left half: realistic close-up of a bright white bathroom tile wall with perfectly clean white grout lines, soft light.
At the top of the left half, a solid blue (#2D6CDF) rounded box with the white bold text "1분이면 끝", with a short bright
yellow (#FFD400) underline under the last character "끝" only. Right half: flat dark navy (#14213D) background with a
simple line-drawing wall clock (hour tick marks only, no numerals) in cream, and below it a wide solid red (#E63B2E)
rounded box with the huge white bold text "응급실 4시간", the largest element in the image, placed above the
bottom-right corner. No people, no bottles, no spray, no smoke, no hospital, no ambulance, no medical cross.
Keep all text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, highlight yellow #FFD400, safe blue #2D6CDF, cost red #E63B2E.
Split-screen divided vertically into two halves by a thick cream vertical stripe. Left half: realistic close-up of a
bright white bathroom tile wall with clean white grout lines, with an empty solid blue (#2D6CDF) rounded box at the top.
Right half: flat dark navy (#14213D) background with a simple cream line-drawing wall clock with tick marks only, and an
empty wide solid red (#E63B2E) rounded box below it, above the bottom-right corner. No people, no bottles, no smoke,
no hospital. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "1분이면 끝" · "응급실 4시간"이 한 글자도 틀리지 않음 · 시계에 숫자 없음
- [ ] 약속은 파랑, 결과는 빨강 · 노랑 강조 1곳("끝" 밑줄)
- [ ] 세정제 병·분무기·연기·병원·구급차 없음
- [ ] 320px 축소본에서 두 문구가 모두 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
