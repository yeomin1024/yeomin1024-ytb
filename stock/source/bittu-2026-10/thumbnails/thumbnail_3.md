# bittu-2026-10 썸네일 3 — 대비 (주가 -42% vs 내 돈 -83%)

버전: v1.0 — 2026-10-10 — 최초 작성 (`guides/thumbnail_guide.md` v1.1, `stock/guides/thumbnail_rules.md` v1.1), 대본 v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "주가는 절반도 안 빠졌는데 내 돈은 거의 다 사라졌다"는 **빚이 키운 손실의 대비**가 신용을 써 본 사람에게 가장 와닿는다 (문제 분석 첫 번째 메시지) |
| 짝 제목 | `titles.md` T3 (짧은 변형) "반대매매 한 번에 +1,500만원이 -2,500만원이 됐습니다 …" — T1(채택)과도 어울림 |
| 숫자 근거 | 문장 11 "남은 돈은 500만 원, -2,500만 원" (0:53) → 1분 안. ※ "42%·83%"(문장 29·30, 2:37)는 1분 뒤라 숫자 대신 막대 길이로만 보여 주고, 큰 글자는 1분 안의 "-2,500만 원"을 쓴다 |

## 화면 구성
- 세로로 찢어진 종이 경계로 화면을 나눈다. 왼쪽 45%는 크림, 오른쪽 55%는 다크 네이비.
- 왼쪽: "주가" (검정, 크게) + 그 아래 절반에 못 미치게 줄어든 웜 그레이 막대
- 오른쪽: "내 돈" (노랑 상자 + 검정 글자) + 그 아래 거의 다 사라진 파랑 막대, 막대 옆에 파랑 상자 안 "-2,500만 원" (흰 글자)
- 인물 없음 · 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 주가 | 검정 #1E1E1E | — (막대는 웜 그레이 #9A968E) |
| 오른쪽 | 내 돈 | 검정 (노랑 상자 위) | 노랑 상자 #FFD400 (유일한 강조) |
| 결과 | -2,500만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat editorial paper-collage graphic. The frame is split by a vertical torn-paper edge slightly left of center.
Left side (45%, cream #F2EBDD): the large black bold word "주가" at the top, and below it a tall outlined bar where only
a bit more than half remains filled in warm gray (#9A968E). Right side (55%, dark navy #14213D): the word "내 돈" in black
bold letters on a solid bright yellow (#FFD400) box at the top, and below it a tall outlined bar that is almost completely
empty, with only a thin sliver of blue (#2D6CDF) left at the bottom. Next to that bar, a wide solid blue (#2D6CDF) rounded
box with a thin white border containing the huge white bold text "-2,500만 원", the largest element.
No people, no faces, no logos. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, highlight yellow #FFD400, loss blue #2D6CDF, warm gray #9A968E.
Flat editorial paper-collage graphic split by a vertical torn-paper edge slightly left of center. Left (cream): empty space
at the top for a word, below it a tall outlined bar filled a bit more than halfway in warm gray. Right (dark navy): an empty
bright yellow box at the top, below it a tall outlined bar almost completely empty with a thin blue sliver at the bottom,
and an empty solid blue rounded box with thin white border beside it. No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "주가" · "내 돈" · "-2,500만 원"이 한 글자도 틀리지 않음
- [ ] 왼쪽 막대는 절반 남짓 남고(주가 -42%), 오른쪽 막대는 거의 비어 있음(내 돈 -83%) — 눈금 숫자 없음
- [ ] 주가 막대는 웜 그레이(손실 색 아님), 내 돈 막대만 파랑 · 노랑 강조 1곳 · 종목명 없음
- [ ] 320px 축소본에서 두 막대의 차이와 "-2,500만 원"이 읽힘
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
