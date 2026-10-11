# voyager-2026-10 썸네일 1 — 숫자 반전 (끝났다 → 빛으로 하루 거리)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `space/guides/thumbnail_rules.md` v1.1, 대본 v1.0 기준 (v1.0 — 2026-10-11 — 최초 작성). 지운 말 "끝났다"는 하단 1줄의 빨강 단어로 옮김

| 항목 | 값 |
|---|---|
| 시험하는 가설 | '끝났다'는 판정이 **빛으로 하루 거리**까지 간 실제 기록으로 뒤집힌 거리 반전이 가장 클릭을 부른다 |
| 짝 제목 | `titles.md` **T1 (채택)** "보이저 1호는 끝났다고 가르쳤는데 아직 살아서 빛으로 하루 거리에 닿습니다 …" — T3과도 어울림 |
| 숫자 근거 | 문장 1 "보이저 1호가 끝났다는 1분짜리 쇼츠" (0:00) · 문장 4 "보이저 1호는 사실상 끝났고 … 그대로 전했어요" (0:13~0:27) · 문장 8 "그 탐사선은 지금도 신호를 보내며 2026년 11월 18일 빛으로 하루 거리에 닿는대요" (0:47~0:54) → 1분 안 |

## 화면 구성
- 다크 네이비 우주 배경, 별은 드물게 (그림·일러스트 느낌, 실제 사진처럼 보이지 않게)
- **위쪽 약 60% (y 0~430)** 안에 그림을 줄여 넣는다
  - 왼쪽: 작고 파란 지구 (단순한 원, 대륙은 흐릿하게)
  - 오른쪽 위: 안테나 접시가 달린 작은 탐사선 일러스트 (로고·글자·국기 없음, 부서진 모습 아님)
  - 지구와 탐사선을 잇는 가늘고 밝은 신호선 (점선 물결), 신호선 가운데에 노랑 짧은 띠 하나
  - 가운데: 파랑 상자 안 **"빛으로 하루 거리"** (흰 글자, 화면에서 가장 큰 글자 = 핵심 숫자이자 펀치 문구)
- **아래쪽 약 35% (y 450~690)**: 아래에서 위로 옅어지는 어두운 띠 위에 하단 제목 2줄 (왼쪽 정렬, x 48부터)
  - 1줄 "끝났다고 가르쳤는데" ("끝났다고"만 빨강) / 2줄 "보이저는 아직 살아 있다"
- 오른쪽 아래 구석(약 220×70px)은 비움 · 인물 없음
- 강조색 2곳: 빨강 "끝났다고" (틀린 말) · 노랑 신호선 띠 (글자 없음). 파랑 상자는 사실 색

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 핵심 숫자·펀치 | 빛으로 하루 거리 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |
| (그림) | 신호선 가운데 노랑 띠 | 노랑 #FFD400 | 글자 없음 |
| 하단 1줄 | 끝났다고 가르쳤는데 | 흰색 + 검정 외곽선 | "끝났다고" 빨강 #E63B2E (틀린 말) |
| 하단 2줄 | 보이저는 아직 살아 있다 | 흰색 + 검정 외곽선 | — |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact blue #2D6CDF, wrong-information red #E63B2E, cream #F2EBDD.
Bottom-right corner kept empty (video length badge).
Clean flat illustrated style (clearly an illustration, not a photo). Dark navy (#14213D) deep-space background with only a
few small faint stars. Everything in this paragraph stays in the upper 60% of the frame: on the left, a small simple blue
Earth; on the upper right, a small generic space probe illustration with a large dish antenna and thin booms, intact, no
logos, no letters, no flags. A thin glowing dotted wave line connects the Earth and the probe, with one short bright
yellow (#FFD400) band in the middle of the line. In the center, a wide solid blue (#2D6CDF) rounded box with the huge
white bold text "빛으로 하루 거리", the largest text in the image. No people.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "끝났다고 가르쳤는데", line 2 "보이저는 아직 살아 있다". The word "끝났다고" is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep all text inside the central 16:9 safe area. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, highlight yellow #FFD400, fact blue #2D6CDF, wrong-information red #E63B2E.
Clean flat illustrated style, not a photo. Dark navy deep-space background with a few faint stars. All picture elements
stay in the upper 60% of the frame: a small simple blue Earth on the left, a small generic space probe with a large dish
antenna on the upper right (intact, no logos, no letters, no flags), a thin glowing dotted wave line connecting them with
one short bright yellow band in the middle, and an empty wide solid blue rounded box in the center. No people.
The lower third of the frame is a dark band (black to dark navy) fading upward from the bottom edge, completely clean and
empty, for two lines of headline text added later. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "빛으로 하루 거리" · "끝났다고 가르쳤는데" · "보이저는 아직 살아 있다"가 한 글자도 틀리지 않음 (문장 1·4·8과 같은 말)
- [ ] 아래쪽에 제목 문구 2줄이 크게 있음 (1줄 10자, 2줄 13자 — 한 줄 14자 이내, 합 23자) · 위쪽 펀치 문구는 "빛으로 하루 거리" 1개(9자)
- [ ] 지구·탐사선·파랑 상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 2줄째 오른쪽 끝이 x 1040 안
- [ ] 320px 축소본에서 "빛으로 하루 거리"와 하단 2줄이 바로 읽힘 · 강조색 2곳(빨강 "끝났다고", 노랑 띠) · 틀린 말은 빨강, 실제 기록은 파랑
- [ ] 탐사선에 로고·글자·국기 없음 · 부서지거나 폭발하는 장면 없음 · 나사 사진처럼 보이지 않음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
