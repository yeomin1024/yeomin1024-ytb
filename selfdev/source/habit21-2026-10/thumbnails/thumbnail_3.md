# habit21-2026-10 썸네일 3 — 대비 (21일 성공 vs 사흘 뒤)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `selfdev/guides/thumbnail_rules.md` v1.0), 대본 `habit21-2026-10.txt` v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "21일 성공"이라는 기대와 "사흘 뒤 0일"이라는 결과를 **한 화면에 나란히** 놓으면 "21일이면 끝"이라는 통념이 깨지는 게 한눈에 보인다 |
| 짝 제목 | `titles.md` T3 (짧은 변형) "21일 챌린지 꼬박 채우고 사흘 만에 0일 …" — T1(채택)과도 어울림 |
| 숫자 근거 | 문장 5~6 "매일 아침 7시, 거실 매트 위에서 30분씩" · "21일 동안 하루도 빠지지 않았고" (0:23~0:35) · 문장 11 "딱 사흘 만에 … 0일이 됐어요" (0:54) · 문장 12 "매트는 그대로 말려 있었어요" (0:59) → 모두 1분 안 |

## 화면 구성
- 화면을 가운데 세로선으로 반반 나눔
- **왼쪽 = 기대 (밝은 크림 톤):** 아침 햇살이 드는 거실, 펼쳐진 운동 매트 위에서 스트레칭하는 **가상 인물**(30대 한국인 여성, 뒷모습 또는 옆모습, 얼굴 작게). 위쪽에 파랑 상자 + 흰 글자 **"21일 성공"**
- **오른쪽 = 결과 (어두운 네이비 톤):** 같은 거실 구석, 사람 없이 벽에 기대 세워 둔 **말아 둔 매트**에 옅은 먼지. 아래쪽에 큰 빨강 **"사흘 뒤 0일"**, 그중 "0일"만 노랑 상자 강조
- 오른쪽 아래 구석(약 220×70px) 비움 — "사흘 뒤 0일"은 오른쪽 절반의 가운데 아래에 두되 구석은 피함

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 21일 성공 | 흰색 (파랑 #2D6CDF 상자) — 되찾은 것·좋아짐 | — |
| 오른쪽 | 사흘 뒤 0일 | 빨강 #E63B2E ("0일"만 노랑 상자 #FFD400 위 잉크 글자) | 가장 큰 글자, 유일한 노랑 강조 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Split-screen image divided vertically down the middle by a clean straight line. LEFT HALF (the hope): a bright,
cream-toned living room in warm morning sunlight; a fictional Korean woman in her mid 30s, seen from the side or back with
her face small, stretching on an unrolled exercise mat. Fictional person, not resembling any real or famous person,
natural Korean features. At the top of the left half, a solid blue (#2D6CDF) box with the white bold text "21일 성공".
RIGHT HALF (the result): the same corner of the living room in a dark navy (#14213D) tone, nobody there, the exercise mat
rolled up and standing against the wall with a light layer of dust. In the lower middle of the right half (not in the
bottom-right corner), large red (#E63B2E) bold text "사흘 뒤" followed by "0일" in ink-black on a bright yellow (#FFD400)
box, the largest text in the image. Realistic photo style, no brand logos on the mat, no phones, no apps.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF.
Split-screen image divided vertically down the middle. LEFT HALF: a bright cream-toned living room in warm morning
sunlight, a fictional Korean woman in her mid 30s seen from the side or back, face small, stretching on an unrolled
exercise mat; fictional person, not resembling any real or famous person; an empty solid blue box at the top of the left
half. RIGHT HALF: the same corner in a dark navy tone, nobody there, the exercise mat rolled up against the wall with a
light layer of dust; an empty dark area in the lower middle of the right half for a large headline. No brand logos.
Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "21일 성공" · "사흘 뒤 0일"이 한 글자도 틀리지 않음 (문장 6·11과 같은 숫자)
- [ ] 문구 2덩어리, 20자 이내 · 제목을 그대로 반복하지 않음
- [ ] 색의 뜻: 성공(되찾은 것) 파랑, 0일(잃은 것) 빨강 · 노랑 강조는 "0일" 한 곳
- [ ] 인물이 실존 인물을 닮지 않음 · 매트에 브랜드 없음 · 챌린지·인증 앱 화면 없음
- [ ] 320px 축소본에서 "0일"이 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
