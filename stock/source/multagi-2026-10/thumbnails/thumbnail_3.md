# multagi-2026-10 썸네일 3 — 대비 (평단 ↓ vs 손실)

버전: v1.0 — 2026-10-09 — 대본 `multagi-2026-10.txt` v1.2 기준 (`guides/thumbnail_guide.md` v1.0, `stock/guides/thumbnail_rules.md` v1.0)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "평단은 내려갔는데 손실은 커졌다"는 **기대와 결과의 대비**가 물타기 해 본 사람에게 가장 와닿는다 (문제 분석 첫 번째 메시지) |
| 짝 제목 | `titles.md` T3 (짧은 변형) "물타기 두 번에 -200만원이 -2천만원이 됐습니다 …" — T1·T2와도 어울림 |
| 숫자 근거 | 자막 8 "평단이 내려갔으니 조금만 반등해도 본전이라고" (0:38) · 자막 10 "-2천만 원" (0:47) → 1분 안. ※ "평단 3%"(자막 26, 2:09)는 1분 뒤라 숫자로 쓰지 않고 "↓"로만 보여 줌 |
| 배경 | 왼쪽 크림 #F2EBDD / 오른쪽 다크 네이비 #14213D (찢어진 종이 경계) |

## 화면 구성 (1280×720)
```
┌───────────────────────────┬╱──────────────────────────────────┐
│ (크림)                     │╲ (네이비)                           │
│     평단                   │╱      손실  ← 노랑 형광펜             │
│     ↓  (웜 그레이 큰 화살표) │╲  ┌──────────────────────────┐    │
│                           │╱  │      -2,000만 원          │    │
│                           │╲  └──────────────────────────┘    │
│                           │╱                      (비움: 길이 표시) │
└───────────────────────────┴───────────────────────────────────┘
```
- 경계: x ≈ 560~600 사이 세로로 찢어진 종이 가장자리 (영상의 찢어진 종이 전환과 같은 모양, 가벼운 폴리곤)
- 왼쪽 (기대): "평단" 130px 잉크 (110, 150). 그 아래 큰 아래 화살표, 웜 그레이 #9A968E (x 150~330, y 320~600)
  - 평단이 내려간 것은 사연자가 기대한 쪽이라 손실 색(파랑)을 쓰지 않는다.
- 오른쪽 (결과): "손실" 130px (680, 120), **글자 전체 높이의 노랑 상자 + 잉크 #1E1E1E 글자** (네이비 배경 — 흰 글자·절반 형광펜은 안 읽힘)
- 오른쪽 숫자 상자: x 610~1232, y 330~540. 파랑 #2D6CDF + 흰 테두리 4px, 안에 "-2,000만 원" 110px, 흰색 (글자 폭 약 5.2em ≈ 575px → 상자 622px 안)
- 비교 순서: 왼쪽 = 기대, 오른쪽 = 결과 (`guides/thumbnail_guide.md` 4번)
- 오른쪽 아래 1060~1280 × 650~720은 비운다.

## 문구 (그대로 사용)
| 줄 | 문구 | 크기 | 색 | 강조 |
|---|---|---|---|---|
| 왼쪽 | 평단 | 130px / 900 | 잉크 #1E1E1E | — (화살표는 웜 그레이) |
| 오른쪽 | 손실 | 130px / 900 | 잉크 #1E1E1E (형광펜 위) | 노랑 형광펜 |
| 결과 | -2,000만 원 | 110px / 900 | 흰색 (파랑 상자 위) | — |

## [A] Claude Code 지시 (방법 1 — Remotion Still)
1. `video/src/episodes/multagi-2026-10/thumbnails/Thumb3.tsx`를 만든다.
   - 찢어진 종이 경계는 영상 전환용 공통 컴포넌트(clip-path 폴리곤)를 쓴다.
   - 숫자 상자·형광펜은 썸네일 1과 같은 컴포넌트를 쓴다.
2. 등록: `<Still id="multagi-2026-10-thumb-3" component={Thumb3} width={1280} height={720} />`
3. 렌더 (`video/`에서): `npx remotion still multagi-2026-10-thumb-3 ../stock/out/multagi-2026-10/thumbnails/thumbnail_3.png`
4. 320px 축소본에서 "평단 ↓ / 손실 -2,000만 원" 대비가 한눈에 읽히는지 확인한다.

## [B] 이미지 AI 프롬프트 (방법 2 — 글자 없음)
```
YouTube thumbnail background, 16:9 landscape (1280x720). Editorial explainer collage style: printed paper cut-out look,
subtle paper grain and fine halftone texture, thick white sticker border around cut-out objects, flat soft lighting.
Limited palette only: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, red #E63B2E, blue #2D6CDF,
warm gray #9A968E, dark navy #14213D. Large empty area reserved for big headline text.
No people, no faces, no hands, no characters. Absolutely no text, letters, numbers, logos, or watermarks.
Scene: split composition divided by a vertical torn-paper edge slightly left of center. Left side: cream paper with one
large warm-gray (#9A968E) paper-cut arrow pointing straight down. Right side: dark navy paper with an empty solid blue
(#2D6CDF) rectangle with a thin white border in the lower middle. Leave both upper areas empty for words.
```
- 만든 이미지 위에 "문구" 표의 3가지를 얹는다.

## 검수
- [ ] "-2,000만 원" = 자막 10, "평단 ↓" = 자막 8 (1분 안). "3%" 같은 1분 뒤 숫자 없음
- [ ] 문구 덩어리 3개 · 노랑 강조 1곳("손실") · 손실은 파랑, 평단 화살표는 웜 그레이
- [ ] 320px 축소본에서 읽힘 · 오른쪽 아래 비어 있음 · 48px 여백 안
- [ ] 종목명·로고·인물 없음
- [ ] 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
