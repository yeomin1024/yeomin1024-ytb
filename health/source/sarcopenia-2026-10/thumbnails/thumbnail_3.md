# sarcopenia-2026-10 썸네일 3 — 대비 (몸무게 -6kg vs 악력 17kg)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `health/guides/thumbnail_rules.md` v1.1 1·2번: 왼쪽 = 믿었던 것, 오른쪽 = 결과, 좋아짐 = 파랑·나빠짐 = 빨강), 대본 sarcopenia-2026-10.txt v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 왼쪽에 **체중계 -6kg**(좋아했던 숫자, 파랑)과 오른쪽 **악력 17kg**(결과, 빨강)을 나란히 놓으면 "몸무게는 줄었는데 힘이 빠졌구나"가 한눈에 읽힌다 — 썸네일 1(걸음 수)과 '믿었던 숫자'만 바꿔 어느 쪽이 더 끄는지 본다 |
| 짝 제목 | `titles.md` T3 (짧은 변형) "몸무게 6kg 빠졌다고 자랑했는데 근감소증이 됐습니다 …" — T1과도 어울림 |
| 숫자 근거 | 문장 6 "2년 사이 몸무게도 58kg에서 52kg으로 6kg이나 빠졌죠" (0:27) · 문장 7 "자랑까지 했어요" (0:34) · 문장 10 "악력은 17kg" (0:46) · 문장 45 "사연자는 6kg이 빠져 좋아했지만, 병원에서 잰 악력은 17kg이었죠" (4:11) → 장면은 모두 1분 안 |

## 화면 구성
- 세로로 찢어진 종이 경계로 화면을 나눈다. 왼쪽 50%는 크림, 오른쪽 50%는 다크 네이비.
- 왼쪽: 상표 없는 단순한 흰 체중계(위에서 비스듬히 본 모습, 표시창은 비어 있음). 체중계 위쪽에 노랑 상자 잉크 글자 **"좋아했는데"**, 그 아래 파랑 큰 글자 **"-6kg"**
- 오른쪽: 작은 흰 글자 **"악력"**, 그 아래 빨강 **"17kg"** (흰 테두리) — 화면에서 가장 큰 요소
- 인물·악력계·운동 기구·병원 장면 없음 · 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 위 | 좋아했는데 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (유일한 노랑) |
| 왼쪽 | -6kg | 파랑 #2D6CDF | 크게 (좋아했던 숫자) |
| 오른쪽 위 | 악력 | 흰색 #F7F3EA | 작게 |
| 오른쪽 | 17kg | 빨강 #E63B2E (흰 테두리) | 가장 큰 글자 |

전체 13자 (2줄 구성: "좋아했는데 -6kg" / "악력 17kg"). 짝 제목 T3("6kg … 근감소증")에 없는 **악력 17kg**을 보태고, "근감소증"은 반복하지 않는다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat editorial paper-collage graphic. The frame is split by a vertical torn-paper edge in the middle.
Left half (cream #F2EBDD): a simple unbranded white bathroom scale seen from slightly above, drawn with thin ink outlines,
its display window blank. Above the scale, the black bold text "좋아했는데" on a solid bright yellow (#FFD400) box, and
below that the large blue (#2D6CDF) text "-6kg". Right half (dark navy #14213D): the small off-white bold word "악력" near
the top, and below it the huge red (#E63B2E) text "17kg" with a thin white outline, the largest element in the image
(about 30% of the image height). No people, no faces, no gym equipment, no hospital scenes, no logos.
Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400.
Flat editorial paper-collage graphic split by a vertical torn-paper edge in the middle. Left half (cream): a simple
unbranded white bathroom scale with thin ink outlines and a blank display, an empty solid yellow box above it and empty
space for a number between them. Right half (dark navy): large calm empty space for a big number and a small word above
it. No people, no logos. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "좋아했는데" · "-6kg" · "악력" · "17kg"이 한 글자도 틀리지 않음, 그 밖의 글자·숫자 없음 (체중계 표시창은 비어 있음)
- [ ] 숫자가 대본(문장 6·10·45)·제목과 같음 — 6kg, 17kg
- [ ] 색의 뜻이 건강 규칙과 같음: -6kg 파랑(그때는 좋아했던 숫자), 17kg 빨강(나빠짐) · 노랑 강조는 "좋아했는데" 한 곳
- [ ] "17kg"이 가장 큼 · 체중계에 상표 없음 · 인물·병원 장면 없음
- [ ] 320px 축소본에서 "-6kg"과 "17kg"이 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
