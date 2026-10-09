# multagi-2026-10 썸네일 3 — 대비 (평단 ↓ vs 손실)

버전: v1.1 — 2026-10-09 — 이미지 AI용 프롬프트 형식으로 변경 (`guides/thumbnail_guide.md` v1.1, `stock/guides/thumbnail_rules.md` v1.1), 대본 v1.3 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "평단은 내려갔는데 손실은 커졌다"는 **기대와 결과의 대비**가 물타기 해 본 사람에게 가장 와닿는다 (문제 분석 첫 번째 메시지) |
| 짝 제목 | `titles.md` T3 (짧은 변형) "물타기 두 번에 -200만원이 -2천만원이 됐습니다 …" — T1(채택)·T2와도 어울림 |
| 숫자 근거 | 자막 8 "평단이 내려갔으니 조금만 반등해도 본전이라고" (0:38) · 자막 10 "-2천만 원" (0:47) → 1분 안. ※ "평단 3%"(자막 26, 2:09)는 1분 뒤라 숫자로 쓰지 않고 "↓"로만 보여 줌 |

## 화면 구성
- 세로로 찢어진 종이 경계로 화면을 나눈다. 왼쪽 45%는 크림, 오른쪽 55%는 다크 네이비.
- 왼쪽 (기대): "평단" (검정, 크게) + 그 아래 큰 웜 그레이 아래 화살표
  - 평단이 내려간 것은 사연자가 기대한 쪽이라 손실 색(파랑)을 쓰지 않는다.
- 오른쪽 (결과): "손실" (노랑 상자 + 검정 글자) + 그 아래 파랑 상자 안 "-2,000만 원" (흰 글자)
- 인물 없음 · 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 평단 | 검정 #1E1E1E | — (화살표는 웜 그레이 #9A968E) |
| 오른쪽 | 손실 | 검정 (노랑 상자 위) | 노랑 상자 #FFD400 (유일한 강조) |
| 결과 | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | — |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat editorial paper-collage graphic. The frame is split by a vertical torn-paper edge slightly left of center.
Left side: cream paper (#F2EBDD) with the large black bold text "평단" near the top and a big warm-gray (#9A968E)
paper-cut arrow pointing straight down below it. Right side: dark navy paper (#14213D) with the large text "손실" in black
on a solid bright yellow (#FFD400) box near the top, and below it a wide solid blue (#2D6CDF) rounded box with a thin white
border containing the white bold text "-2,000만 원". No people. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, highlight yellow #FFD400, loss blue #2D6CDF, warm gray #9A968E.
Flat editorial paper-collage graphic split by a vertical torn-paper edge slightly left of center. Left: cream paper with
empty space at the top and one large warm-gray paper-cut arrow pointing straight down. Right: dark navy paper with an
empty bright yellow box near the top and an empty solid blue rounded box with a thin white border below it.
No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "평단" · "손실" · "-2,000만 원"이 한 글자도 틀리지 않음 · "3%" 같은 1분 뒤 숫자 없음
- [ ] 노랑 강조 1곳("손실") · 손실은 파랑, 평단 화살표는 웜 그레이
- [ ] 320px 축소본에서 대비가 한눈에 읽힘 · 오른쪽 아래 비어 있음
- [ ] 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
