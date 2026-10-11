# habit21-2026-10 썸네일 1 — 숫자 반전 (달력 기록 카드)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `guides/thumbnail_guide.md` v1.3 1번 2·3항·4-2, `selfdev/guides/thumbnail_rules.md` v1.1, 대본 `habit21-2026-10.txt` v1.0 기준 (v1.0: 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 동그라미 21개가 꽉 찬 달력이 **"0일"**로 뒤집히는 숫자 반전이 가장 클릭을 부른다 (시청자가 아는 "21일"을 노랑으로 강조) |
| 짝 제목 | `titles.md` **T1 (채택)** "21일만 버티면 습관이 된다길래 꼬박 채웠는데 사흘 만에 0일이 됐습니다 …" — 하단 2줄 = 이 제목 앞 문장을 줄인 것. T3과도 어울림 |
| 숫자 근거 | 문장 6 "21일 동안 하루도 빠지지 않았고, 달력에는 동그라미 21개가 생겼죠" (0:28) · 문장 11 "딱 사흘 만에 21일이던 연속 기록이 0일이 됐어요" (0:54) → 모두 1분 안 |

## 화면 구성
- 크림 배경(#F2EBDD), 옅은 종이 질감. 장식 없음
- **위쪽 약 60% (y 약 40~420) = 그림 영역** — 하단 2줄을 가리지 않게 줄여서 배치
  - 왼쪽 50%: **종이 벽걸이 달력 한 장** (날짜 숫자는 흐릿하게 처리, 월 이름·글자 없음)
    - 첫 세 줄 칸(21칸)에 잉크색 손글씨 동그라미가 하나씩, 그다음 칸들은 비어 있음
    - 달력 위쪽에 노랑 상자 + 잉크 글자 **"21일"** (위쪽의 짧은 문구 1개, 노랑 상자는 이곳 하나)
  - 오른쪽 40%: 굵은 잉크색 화살표(→) 끝에 아주 큰 빨강 **"0일"** (핵심 숫자, 화면에서 가장 큰 글자, 화면 높이의 약 30%)
- **아래쪽 약 35% (y 약 450~690) = 하단 제목 2줄** — 아래에서 위로 옅어지는 다크 네이비 #14213D 띠(불투명 약 85%) 위, 왼쪽 정렬 x 48부터, 흰 글자 + 두꺼운 검정 외곽선, 글자 높이 약 90px
  - 1줄 "21일 꼬박 채웠는데"
  - 2줄 "사흘 만에 0일이 됐다" — "0일"만 빨강 (무너진 결과), 오른쪽 끝은 x 1040 안
- 강조 3곳: 노랑 상자 "21일" · 큰 빨강 "0일" · 하단 "0일" 빨강
- 인물 없음 · 오른쪽 아래 구석 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 문구 (시작) | 21일 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (노랑 상자 1곳) |
| 핵심 숫자 (결과) | 0일 | 빨강 #E63B2E (잃은 것) | 가장 큰 글자 |
| 하단 1줄 (11자) | 21일 꼬박 채웠는데 | 흰색 + 두꺼운 검정 외곽선 | — |
| 하단 2줄 (12자) | 사흘 만에 0일이 됐다 | 흰색 + 두꺼운 검정 외곽선 | "0일"만 빨강 #E63B2E (무너진 결과) |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain.
Upper 60% of the frame: on the left half, a single sheet of a simple paper wall calendar with a plain grid of boxes (date numbers very faint and blurred, no month name, no brand, no printed words). The first 21 boxes, the top three rows, each have a hand-drawn ink-black circle; all the remaining boxes are empty. Above the calendar, a solid bright yellow (#FFD400) box with the large ink-black bold text "21일". On the right 40%, a thick ink-black arrow points from the calendar to a huge red (#E63B2E) bold text "0일", the largest element in the image, about 30% of the image height.
Bottom title: in the lower third, over a dark navy (#14213D) band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "21일 꼬박 채웠는데", line 2 "사흘 만에 0일이 됐다". The word "0일" in line 2 is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
No people, no faces, no apps, no phones. Minimal, nothing decorative. Keep all text and the calendar inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain.
Upper 60% of the frame: on the left half, a single sheet of a simple paper wall calendar with a plain grid of boxes (no date numbers, no month name, no brand). The first 21 boxes, the top three rows, each have a hand-drawn ink-black circle; the remaining boxes are empty. Above the calendar, an empty solid bright yellow box. On the right 40%, a thick ink-black arrow pointing right toward a large empty cream area where a huge red number will be placed.
Lower third: a dark navy (#14213D) band, about 85% opaque, fading upward from the bottom edge, with clean empty space for two lines of headline text starting near the left edge.
No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "21일" · "0일" · "21일 꼬박 채웠는데" · "사흘 만에 0일이 됐다"가 한 글자도 틀리지 않음, 그 밖의 글자 없음 (문장 6·11과 같은 숫자, 제목 T1과 같은 값)
- [ ] 아래쪽 약 35%에 하단 2줄이 크게 있음 (11자·12자, 합 23자 — 한 줄 14자 이내, 합 26자 이내) · 어두운 띠 위 흰 글자 + 검정 외곽선 · 2줄 오른쪽 끝이 구석 앞에서 끝남
- [ ] 달력·화살표·"0일"이 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 짧은 문구는 "21일" 하나
- [ ] 동그라미가 21개(세 줄)이고 나머지 칸은 비어 있음
- [ ] 320px 축소본에서 "0일"과 하단 2줄이 바로 읽힘 · 강조 3곳(노랑 "21일" 상자 · 빨강 "0일" · 하단 "0일" 빨강) · 잃은 것은 빨강
- [ ] 달력에 월 이름·브랜드·실제 앱 화면 없음 · 챌린지 앱·인증 앱처럼 보이지 않음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
