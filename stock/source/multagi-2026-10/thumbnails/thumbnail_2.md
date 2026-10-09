# multagi-2026-10 썸네일 2 — 결정적 장면 (노후 자금 통장)

버전: v1.0 — 2026-10-09 — 대본 `multagi-2026-10.txt` v1.2 기준 (`guides/thumbnail_guide.md` v1.0, `stock/guides/thumbnail_rules.md` v1.0)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "잃으면 안 되는 돈(노후 자금)"이 무너지는 장면이 숫자 반전보다 감정을 더 끈다 (50·60대·노후 롱폼 성공 31% vs 19%) |
| 짝 제목 | `titles.md` T2 "노후 자금이라 본전 찾으려고 물타서 …" — T1·T3과도 어울림 |
| 숫자 근거 | 자막 4 "노후 자금으로 모아 둔 8천만 원" (0:19) · 자막 8 "조금만 반등해도 본전이라고 생각했어요" (0:38) · 자막 10 "-2천만 원" (0:47) → 모두 1분 안 |
| 배경 | 다크 네이비 #14213D (위기 장면) |

## 화면 구성 (1280×720)
```
┌───────────────────────────────────────────────────────────────┐
│  ┌────────────┐                                                │
│  │  노후 자금   │        본전 찾다가                              │
│  │  8천만 원   │                                                │
│  └────────────┘     ┌───────────────────────────┐              │
│        ╲  파랑 화살표  │       -2,000만 원          │              │
│         ╲↘           └───────────────────────────┘              │
│                                                   (비움: 길이 표시) │
└───────────────────────────────────────────────────────────────┘
```
- 통장(예금 통장 모양, 일반 디자인): x 72~460, y 72~430. 크림 #F2EBDD, 잉크 테두리 5px, 살짝 기울임 (-6°).
  - 표지 글자: "노후 자금" 64px, 그 아래 "8천만 원" 72px, 잉크
  - **은행 이름·로고 없음**
- 파랑 화살표: 통장 아래에서 오른쪽 아래로 꺾여 떨어지는 굵은 화살표 (영상의 손실 화살표와 같은 모양), 파랑 #2D6CDF, 끝점 (520, 600)
- 오른쪽 위 문구 "본전 찾다가": (560, 110), 100px, #F7F3EA, **노랑 강조는 "본전"에만 — 네이비 배경이라 글자 전체 높이의 노랑 상자 + 잉크 #1E1E1E 글자** (흰 글자·절반 형광펜은 안 읽힘)
- 큰 숫자 상자: x 520~1216, y 300~520. 파랑 #2D6CDF + 흰 테두리 4px (네이비 위에서 구분되게), 안에 "-2,000만 원" 125px, 흰색 (글자 폭 약 5.2em ≈ 650px → 상자 696px 안)
- 오른쪽 아래 1060~1280 × 650~720은 비운다.

## 문구 (그대로 사용)
| 줄 | 문구 | 크기 | 색 | 강조 |
|---|---|---|---|---|
| 통장 표지 | 노후 자금 / 8천만 원 | 64px / 72px · 900 | 잉크 | — |
| 속마음 | 본전 찾다가 | 100px / 900 | #F7F3EA ("본전"만 잉크) | "본전"에 노랑 형광펜 |
| 결과 | -2,000만 원 | 125px / 900 | 흰색 (파랑 상자 위) | 가장 큰 글자 |

## [A] Claude Code 지시 (방법 1 — Remotion Still)
1. `video/src/episodes/multagi-2026-10/thumbnails/Thumb2.tsx`를 만든다.
   - 통장은 코드 도형으로 그린다 (`video/src/components/Passbook.tsx` 새 공통 컴포넌트, 표지 글자 2줄 props).
   - 화살표·숫자 상자·형광펜은 썸네일 1과 같은 공통 컴포넌트를 쓴다.
2. 등록: `<Still id="multagi-2026-10-thumb-2" component={Thumb2} width={1280} height={720} />`
3. 렌더 (`video/`에서): `npx remotion still multagi-2026-10-thumb-2 ../stock/out/multagi-2026-10/thumbnails/thumbnail_2.png`
4. 네이비 배경에서 파랑 상자가 묻히지 않는지(흰 테두리) 320px 축소본으로 확인한다.

## [B] 이미지 AI 프롬프트 (방법 2 — 글자 없음)
```
YouTube thumbnail background, 16:9 landscape (1280x720). Editorial explainer collage style: printed paper cut-out look,
subtle paper grain and fine halftone texture, thick white sticker border around cut-out objects, flat soft lighting.
Limited palette only: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, red #E63B2E, blue #2D6CDF,
warm gray #9A968E, dark navy #14213D. Large empty area reserved for big headline text.
No people, no faces, no hands, no characters. Absolutely no text, letters, numbers, logos, or watermarks.
Scene: dark navy (#14213D) paper background with subtle vignette. In the upper-left, a generic cream savings passbook
(plain cover, no bank name, no logo, blank) cut-out, slightly tilted, with a thick blue (#2D6CDF) paper-cut arrow
falling from it down and to the right like money draining away. The right half is mostly empty dark space for large text.
```
- 만든 이미지 위에 "문구" 표의 3가지를 얹는다 (통장 표지 글자 포함).

## 검수
- [ ] 노후 자금·8천만 원·-2,000만 원 = 자막 4·10과 같음, "본전" = 자막 8
- [ ] 문구 덩어리 3개 · 노랑 강조 1곳("본전") · 손실은 파랑(네이비 위에서 흰 테두리)
- [ ] 320px 축소본에서 읽힘 · 오른쪽 아래 비어 있음 · 48px 여백 안
- [ ] 은행 이름·로고·실제 통장 디자인·인물 없음
- [ ] 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
