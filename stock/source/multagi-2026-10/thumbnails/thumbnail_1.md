# multagi-2026-10 썸네일 1 — 숫자 반전 (계좌 카드)

버전: v1.0 — 2026-10-09 — 대본 `multagi-2026-10.txt` v1.2 기준 (`guides/thumbnail_guide.md` v1.0, `stock/guides/thumbnail_rules.md` v1.0)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 작은 손실이 10배로 커진 **계좌 숫자 반전**이 가장 클릭을 부른다 (성공 썸네일 중 인물 없는 3개가 모두 이 형태) |
| 짝 제목 | `titles.md` T1 "평단 낮추면 된다는 말만 믿고 물타서 …" — T2·T3과도 어울림 (숫자가 같음) |
| 숫자 근거 | 자막 5 "일주일 만에 -200만 원이 됐어요" (0:24) · 자막 6·7 1,500만 원씩 두 번 물타기 (0:28·0:34) · 자막 10 "-2천만 원이 찍혀 있었어요" (0:47) → 모두 영상 1분 안에 나옴 |
| 배경 | 크림 #F2EBDD |

## 화면 구성 (1280×720)
```
┌───────────────────────────────────────────────────────────────┐
│ ┌───────────────────────────────────────────────────────────┐ │
│ │ 내 계좌                                                    │ │
│ │ -200만 원        ↓  [물타기 2번] ← 노랑 형광펜             │ │
│ │ ┌───────────────────────────────────────────────────────┐ │ │
│ │ │              -2,000만 원   (파랑 상자, 흰 글자)         │ │ │
│ │ └───────────────────────────────────────────────────────┘ │ │
│ └───────────────────────────────────────────────────────────┘ │
│                                                   (비움: 길이 표시) │
└───────────────────────────────────────────────────────────────┘
```
- 계좌 카드: x 64~1216, y 56~610. 밝은 크림 #FAF6EE, 잉크 테두리 4px, 모서리 28px. **영상 S02의 계좌 카드와 같은 모양**이다 (증권사 앱처럼 보이면 안 됨, 앱 이름·로고 없음).
- 카드 라벨 "내 계좌": (112, 96), 40px, 웜 그레이
- 시작 숫자 "-200만 원": 왼쪽 위 (112, 140~260), 120px, 파랑 #2D6CDF
- 아래 화살표: 시작 숫자 아래에서 큰 숫자 상자 쪽으로. 파랑, 굵기 18px
- 화살표 오른쪽 라벨 "물타기 2번": (330, 270), 84px, 잉크, **노랑 형광펜 #FFD400 (이 썸네일의 유일한 강조)** — 숫자 상자 윗변(y 390)과 16px 이상 띄움
- 큰 숫자 상자: x 96~1184, y 390~590. 파랑 #2D6CDF, 모서리 20px. 안에 "-2,000만 원" 200px, 흰색 #FFFFFF, 가운데 (글자 폭 약 5.2em ≈ 1,040px → 상자 1,088px 안, 넘치면 190px)
- 오른쪽 아래 1060~1280 × 650~720은 비운다.

## 문구 (그대로 사용)
| 줄 | 문구 | 크기 | 색 | 강조 |
|---|---|---|---|---|
| 카드 라벨 | 내 계좌 | 40px / 700 | 웜 그레이 #9A968E | — |
| 시작 | -200만 원 | 120px / 900 | 파랑 #2D6CDF | — |
| 화살표 라벨 | 물타기 2번 | 84px / 900 | 잉크 #1E1E1E | 노랑 형광펜 |
| 결과 | -2,000만 원 | 200px / 900 | 흰색 (파랑 상자 위) | 가장 큰 글자 |

## [A] Claude Code 지시 (방법 1 — Remotion Still)
1. `guides/thumbnail_guide.md` 5번 방법 1을 따른다.
2. 공통 컴포넌트를 쓴다. 영상 제작 때 만든 것이 있으면 그대로 쓰고, 없으면 만들어 영상에서도 재사용한다.
   - `video/src/components/AccountCard.tsx` (계좌 카드)
   - `HighlightText.tsx` (노랑 형광펜)
   - `NumberBox.tsx` (색 상자 + 큰 숫자)
3. `video/src/episodes/multagi-2026-10/thumbnails/Thumb1.tsx`에 위 좌표대로 배치한다.
   - 폰트: `@remotion/google-fonts/NotoSansKR` (700, 900)
   - 숫자는 `fontVariantNumeric: "tabular-nums"`
   - 애니메이션은 없다 (정지 이미지).
4. `video/src/Root.tsx`에 등록: `<Still id="multagi-2026-10-thumb-1" component={Thumb1} width={1280} height={720} />`
5. 렌더 (`video/`에서): `npx remotion still multagi-2026-10-thumb-1 ../stock/out/multagi-2026-10/thumbnails/thumbnail_1.png`
6. 320×180으로 줄인 사본에서 "-2,000만 원"과 "물타기 2번"이 읽히는지 확인한다.

## [B] 이미지 AI 프롬프트 (방법 2 — 글자 없음)
```
YouTube thumbnail background, 16:9 landscape (1280x720). Editorial explainer collage style: printed paper cut-out look,
subtle paper grain and fine halftone texture, thick white sticker border around cut-out objects, flat soft lighting.
Limited palette only: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, red #E63B2E, blue #2D6CDF,
warm gray #9A968E, dark navy #14213D. Large empty area reserved for big headline text.
No people, no faces, no hands, no characters. Absolutely no text, letters, numbers, logos, or watermarks.
Scene: a large blank light-cream paper card filling most of the frame like a simple account summary card with an ink outline,
a wide empty solid blue (#2D6CDF) rectangle across its lower half, and a thick blue paper-cut arrow pointing down from the
upper-left area toward the blue rectangle. Keep all areas blank for text to be added later.
```
- 만든 이미지 위에 "문구" 표의 4가지를 같은 위치·크기로 얹는다.

## 검수
- [ ] 숫자 -200만 원 / -2,000만 원 / 2번 = 자막 5·10·6~7과 같음
- [ ] 문구 덩어리 3개(+카드 라벨) · 노랑 강조 1곳 · 손실은 파랑
- [ ] 320px 축소본에서 읽힘 · 오른쪽 아래 비어 있음 · 48px 여백 안
- [ ] 종목명·증권사 앱 모양·로고·인물 없음
- [ ] 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
