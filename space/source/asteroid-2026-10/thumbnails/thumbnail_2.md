# asteroid-2026-10 썸네일 2 — 인물·감정 장면

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `space/guides/thumbnail_rules.md` v1.1, 대본 asteroid-2026-10.txt v1.0 기준 (v1.0 — 2026-10-11 — 최초 작성). 위쪽 문구 "150만 원 썼는데"는 뺐다 (짝 제목 T2에 없는 숫자이고, 하단 2줄이 T2의 사연 부분을 맡음). 쓴 돈은 상자·배낭으로 보여 준다

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 딸 걱정에 짐을 다 싼 뒤 휴대폰을 보는 **사람의 허탈한 표정**이 숫자 카드보다 감정을 더 끈다 |
| 짝 제목 | `titles.md` T2 "딸 걱정에 짐부터 쌌는데 충돌 확률은 엿새 뒤 0.004%가 됐습니다 …" — T1(채택)과도 어울림 |
| 숫자 근거 | 문장 4 "2032년이면 딸이 열여섯 살이 되는 해라는 생각부터 들었어요" (0:17) · 문장 11 "엿새 뒤, 충돌 확률은 0.004%, 2만 5천분의 1로 떨어져 있었어요" (0:52) · 문장 12 "딸과 함께 배낭까지 싸 둔 뒤였죠" (0:59) → 모두 1분 안 |

## 화면 구성
- 밝은 거실을 부드럽게 흐리게
- **위쪽 약 60% (y 0~430)** 안에 인물과 숫자를 넣는다
  - 왼쪽 55%: **가상 인물** — 마흔 안팎 한국인 여성 직장인(편한 니트), 바닥에 앉아 휴대폰을 내려다보며 허탈하고 머쓱한 표정 (가슴 위까지)
    - 옆에 뜯긴 택배 상자 몇 개와 꽉 찬 배낭 두 개, 상표·글자 없음
    - 휴대폰 화면은 거의 보이지 않거나 흐림 (실제 앱 화면 없음)
  - 오른쪽 위: 파랑 상자 안 흰 글자 **"0.004%"** (화면에서 가장 큰 글자 = 핵심 숫자). 펀치 문구는 따로 넣지 않는다
- **아래쪽 약 35% (y 450~690)**: 아래에서 위로 옅어지는 어두운 띠 위에 하단 제목 2줄 (왼쪽 정렬, x 48부터)
  - 1줄 "딸 걱정에 짐부터 쌌는데" / 2줄 "엿새 뒤 확률이 떨어졌다" ("엿새 뒤"만 노랑)
- 오른쪽 아래 구석은 비움
- 강조색 1곳: 노랑 "엿새 뒤". 파랑 상자는 사실 색

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 핵심 숫자 | 0.004% | 흰 글자 (파랑 #2D6CDF 상자) | 가장 큰 글자 |
| 하단 1줄 | 딸 걱정에 짐부터 쌌는데 | 흰색 + 검정 외곽선 | — |
| 하단 2줄 | 엿새 뒤 확률이 떨어졌다 | 흰색 + 검정 외곽선 | "엿새 뒤" 노랑 #FFD400 (유일한 강조) |

## [A] 완성형 프롬프트
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact blue #2D6CDF, risk red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Softly blurred bright Korean apartment living room in warm cream tones. Everything in this
paragraph stays in the upper 60% of the frame: on the left 55%, a fictional Korean woman around 40, office-worker casual
look (plain knit sweater), shown from the chest up, sitting on the floor and looking down at her smartphone with a
deflated, sheepish, regretful expression, a small tired half-smile, not crying, not scared. Beside her: a few opened
cardboard delivery boxes and two fully packed plain backpacks, with no brand names, no labels and no printed text on
anything. The phone screen faces away or is blurred, no app interface visible. Fictional person, not resembling any real
or famous person, natural Korean features. On the upper right, a wide solid blue (#2D6CDF) rounded box containing the
huge white bold text "0.004%", the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "딸 걱정에 짐부터 쌌는데", line 2 "엿새 뒤 확률이 떨어졌다". The word "엿새 뒤" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep face and text inside the central 16:9 safe area. No space suit, no astronaut, no asteroid impact, no fire.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, fact blue #2D6CDF, risk red #E63B2E.
Realistic photo style. Softly blurred bright Korean apartment living room. All picture elements stay in the upper 60% of
the frame: on the left 55%, a fictional Korean woman around 40 in a plain knit sweater, chest up, sitting on the floor
looking down at her smartphone with a deflated, sheepish, regretful expression, not crying. Beside her a few opened
cardboard boxes and two packed plain backpacks with no brand names or text. Phone screen facing away. Fictional person,
not resembling any real or famous person. On the upper right, an empty wide solid blue (#2D6CDF) rounded box.
The lower third of the frame is a dark band (black to dark navy) fading upward from the bottom edge, completely clean and
empty, for two lines of headline text added later. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "0.004%" · "딸 걱정에 짐부터 쌌는데" · "엿새 뒤 확률이 떨어졌다"가 한 글자도 틀리지 않음 (문장 4·11·12와 같은 말·숫자)
- [ ] 아래쪽에 제목 문구 2줄이 크게 있음 (1줄 13자, 2줄 13자 — 한 줄 14자 이내, 합 26자) · 위쪽 문구는 핵심 숫자 "0.004%" 하나뿐
- [ ] 인물·상자·배낭·파랑 상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 2줄째 오른쪽 끝이 x 1040 안
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 우주복 없음 · 표정은 허탈·머쓱 수준 (우는 얼굴·비명 없음)
- [ ] 배낭·상자·휴대폰에 상표·글자·실제 앱 화면 없음 (특정 제품 광고처럼 보이지 않음)
- [ ] 320px 축소본에서 표정과 "0.004%", 하단 2줄이 읽힘 · 강조색 1곳(노랑 "엿새 뒤") · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
