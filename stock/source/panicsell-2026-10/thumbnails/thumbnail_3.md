# panicsell-2026-10 썸네일 3 — 대비 (판 날 vs 7주 뒤)

버전: v1.0 — 2026-10-10 — 최초 작성 (`guides/thumbnail_guide.md` v1.1, `stock/guides/thumbnail_rules.md` v1.1), 대본 v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "판 날"과 "7주 뒤"를 나란히 놓은 **시간 대비**가, 폭락장에 다 팔고 싶었던 사람에게 가장 와닿는다 (문제 분석 세 번째 "바닥은 지나고 나서야 보인다") |
| 짝 제목 | `titles.md` T3 (짧은 변형) "폭락한 날 -800만원에 다 팔았더니 7주 뒤 +30%였습니다 …" — T1(채택)과도 어울림 |
| 숫자 근거 | 문장 9 "-800만 원이 넘어" (0:39) · 문장 13 "7주 뒤에는 제가 판 가격보다 30% 넘게" (0:59) → 1분 안 |

## 화면 구성
- 세로로 찢어진 종이 경계로 화면을 나눈다. 왼쪽 45%는 다크 네이비, 오른쪽 55%는 크림.
- 왼쪽 (판 날): "판 날" (흰 글자) + 그 아래 크게 꺾여 내려가는 파랑 선 + 파랑 상자 안 "-800만 원" (흰 글자)
- 오른쪽 (7주 뒤): "7주 뒤" (노랑 상자 + 검정 글자) + 그 아래 크게 올라가는 빨강 선 + "+30%" (빨강, 가장 큰 글자)
- 인물 없음 · 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 판 날 | 흰색 #F7F3EA | — |
| 왼쪽 숫자 | -800만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | — |
| 오른쪽 | 7주 뒤 | 검정 (노랑 상자 위) | 노랑 상자 #FFD400 (유일한 강조) |
| 오른쪽 숫자 | +30% | 빨강 #E63B2E | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat editorial paper-collage graphic. The frame is split by a vertical torn-paper edge slightly left of center.
Left side (45%, dark navy #14213D): the off-white bold text "판 날" at the top, below it a thick blue (#2D6CDF) line
plunging sharply downward, and under it a solid blue rounded box with a thin white border containing the white bold text
"-800만 원". Right side (55%, cream #F2EBDD): the black bold text "7주 뒤" on a solid bright yellow (#FFD400) box at the
top, below it a thick red (#E63B2E) line rising steeply, ending at the huge red bold text "+30%", the largest element,
placed in the upper-middle of the right side. No people, no faces, no logos. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Flat editorial paper-collage graphic split by a vertical torn-paper edge slightly left of center. Left (dark navy): empty
space at the top for a word, a thick blue line plunging sharply downward, and an empty solid blue rounded box with thin
white border below it. Right (cream): an empty bright yellow box at the top and a thick red line rising steeply, with empty
space at its tip for a number. No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "판 날" · "-800만 원" · "7주 뒤" · "+30%"가 한 글자도 틀리지 않음
- [ ] 선은 개념도라 눈금·축 숫자 없음 · 하락 선은 파랑, 상승 선은 빨강 · 노랑 강조 1곳 · 종목명 없음
- [ ] 320px 축소본에서 "+30%"와 두 선의 방향이 바로 읽힘
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
