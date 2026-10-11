# habit21-2026-10 썸네일 1 — 숫자 반전 (달력 기록 카드)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `selfdev/guides/thumbnail_rules.md` v1.0), 대본 `habit21-2026-10.txt` v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 동그라미 21개가 꽉 찬 달력이 **"0일"**로 뒤집히는 숫자 반전이 가장 클릭을 부른다 (시청자가 아는 "21일"을 노랑으로 강조) |
| 짝 제목 | `titles.md` **T1 (채택)** "21일만 버티면 습관이 된다길래 꼬박 채웠는데 사흘 만에 0일이 됐습니다 …" — T3과도 어울림 |
| 숫자 근거 | 문장 6 "21일 동안 하루도 빠지지 않았고, 달력에는 동그라미 21개가 생겼죠" (0:28) · 문장 11 "딱 사흘 만에 21일이던 연속 기록이 0일이 됐어요" (0:54) → 모두 1분 안 |

## 화면 구성
- 크림 배경(#F2EBDD) 위, 화면 왼쪽 55~60%에 **종이 벽걸이 달력 한 장** (날짜 숫자는 흐릿하게 처리, 월 이름·글자 없음)
  - 첫 세 줄 칸(21칸)에 잉크색 손글씨 동그라미가 하나씩, 그다음 칸들은 비어 있음
  - 달력 위쪽에 노랑 상자 + 잉크 글자 **"21일"** (유일한 노랑 강조)
- 오른쪽 40%: 굵은 잉크색 화살표(→) 끝에 아주 큰 빨강 **"0일"** (화면에서 가장 큰 글자, 화면 높이의 약 30%)
- 인물 없음 · 오른쪽 아래 구석 비움 · 장식 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 시작 | 21일 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (유일한 강조) |
| 결과 | 0일 | 빨강 #E63B2E (잃은 것) | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. On the left 55% of the frame,
a single sheet of a simple paper wall calendar with a plain grid of boxes (date numbers very faint and blurred, no month
name, no brand, no printed words). The first 21 boxes, the top three rows, each have a hand-drawn ink-black circle; all
the remaining boxes are empty. Above the calendar, a solid bright yellow (#FFD400) box with the large ink-black bold text
"21일". On the right 40% of the frame, a thick ink-black arrow points from the calendar to a huge red (#E63B2E) bold
text "0일", the largest element in the image, about 30% of the image height. No people, no faces, no apps, no phones.
Minimal, nothing decorative. Keep all text and the calendar inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, gain red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. On the left 55% of the frame, a single
sheet of a simple paper wall calendar with a plain grid of boxes (no date numbers, no month name, no brand). The first 21
boxes, the top three rows, each have a hand-drawn ink-black circle; the remaining boxes are empty. Above the calendar, an
empty solid bright yellow box. On the right 40%, a thick ink-black arrow pointing right toward a large empty cream area
where a huge red headline will be placed. No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "21일" · "0일"이 한 글자도 틀리지 않음 (문장 6·11과 같은 숫자)
- [ ] 동그라미가 21개(세 줄)이고 나머지 칸은 비어 있음
- [ ] 320px 축소본에서 "0일"이 바로 읽힘 · 노랑 강조 1곳("21일") · 잃은 것은 빨강
- [ ] 달력에 월 이름·브랜드·실제 앱 화면 없음 · 챌린지 앱·인증 앱처럼 보이지 않음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
