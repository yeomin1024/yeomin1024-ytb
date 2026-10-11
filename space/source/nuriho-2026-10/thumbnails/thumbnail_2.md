# nuriho-2026-10 썸네일 2 — 인물·감정 장면 (생중계 앞의 엄마)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `space/guides/thumbnail_rules.md` v1.1, 대본 v1.0 기준 (v1.0 — 2026-10-11 — 최초 작성). 위쪽 문구를 "46초에 꺾은 꿈"에서 짝 제목 T2의 숫자 "4번 연속 성공"으로 바꿈 (하단 2줄이 T2의 사연 부분이라 같은 말 "꿈"이 겹치지 않게)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 발사 성공 생중계 앞에서 **후회하는 엄마의 표정**과 등을 돌린 아들이, 숫자 카드보다 '내 얘기'라는 감정을 더 끈다 |
| 짝 제목 | `titles.md` T2 "우리나라는 안 된다며 아들 꿈을 말렸는데 누리호가 4번 연속 성공했습니다 …" — T1(채택)과도 어울림 |
| 숫자 근거 | 문장 5 "우리나라는 아직 안 된다며 현실적인 과를 가라고 했죠" (0:23) · 문장 10 "2022년부터 4번 연속 성공이었죠" (0:52) · 문장 11~12 아들이 생중계를 끝까지 보고 "엄마, 나 원래 저거 하고 싶었잖아" (0:56~1:05) → 장면이 1분 안팎 |

## 화면 구성
- 낮의 거실 (5차 발사는 낮 12시 25분). 전체 톤은 차분한 네이비·크림
- **위쪽 약 60% (y 0~430)** 안에 인물과 숫자를 넣는다
  - 왼쪽 45%: **가상 인물** — 쉰 살 안팎의 한국인 여성 직장인 (단정한 니트), 소파에 앉아 휴대폰을 보며 허탈하고 미안한 표정 (가슴 위까지). 울거나 겁먹은 얼굴이 아님
    - 휴대폰 화면: 로고 없는 단순한 로켓 상승 그림과 파란 ✓ 모양 하나만 (앱 화면·글자 없음)
  - 가운데 뒤쪽: 등을 돌리고 창가에 선 대학생 아들의 흐릿한 실루엣
  - 오른쪽 위: 파랑 상자 안 **"4번 연속 성공"** (흰 글자, 화면에서 가장 큰 글자 = 핵심 숫자이자 펀치 문구)
- **아래쪽 약 35% (y 450~690)**: 아래에서 위로 옅어지는 다크 네이비 띠 위에 하단 제목 2줄 (왼쪽 정렬, x 48부터)
  - 1줄 "우리나라는 안 된다며" ("안 된다며"만 빨강) / 2줄 "아들 꿈을 말렸는데"
- 오른쪽 아래 구석(약 220×70px)은 비움
- 강조색 1곳: 빨강 "안 된다며" (틀린 말). 파랑 상자·✓는 사실 색

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 핵심 숫자·펀치 | 4번 연속 성공 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |
| 하단 1줄 | 우리나라는 안 된다며 | 흰색 + 검정 외곽선 | "안 된다며" 빨강 #E63B2E (틀린 말, 유일한 강조) |
| 하단 2줄 | 아들 꿈을 말렸는데 | 흰색 + 검정 외곽선 | — |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact/success blue #2D6CDF, failure red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style, soft daylight living room with muted navy and cream tones. Everything in this paragraph stays in
the upper 60% of the frame: on the left 45%, a fictional Korean woman around 50 years old, office-worker look (simple
knit top), shown from the chest up, sitting on a sofa and looking down at a smartphone in her hands with a regretful,
deflated, quietly guilty expression (not crying, not scared). The phone screen shows only a simple drawing of a rocket
rising and one small blue check-mark shape, no app interface, no logos, no text. In the soft background behind her, a
blurred silhouette of a college-age young man standing by the window with his back turned. Fictional people, not
resembling any real or famous person, natural Korean features. On the upper right, a solid blue (#2D6CDF) rounded box with
the huge white bold text "4번 연속 성공", the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "우리나라는 안 된다며", line 2 "아들 꿈을 말렸는데". The words "안 된다며" are red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 safe area. No spacesuits, no flags, no logos, no explosion.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Realistic photo style, soft daylight living room with muted navy and cream tones. All picture elements stay in the upper
60% of the frame: on the left 45%, a fictional Korean woman around 50, simple knit top, chest up, sitting on a sofa
looking down at a smartphone with a regretful, deflated expression (not crying). The phone screen shows only a simple
rocket drawing and a small blue check-mark shape, no interface, no text. Blurred silhouette of a college-age young man by
the window in the background, back turned. Fictional people, not resembling any real or famous person, natural Korean
features. On the upper right, an empty solid blue (#2D6CDF) rounded box for a short headline.
The lower third of the frame is a dark navy band fading upward from the bottom edge, completely clean and empty, for two
lines of headline text added later. No spacesuits, no flags, no logos. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "4번 연속 성공" · "우리나라는 안 된다며" · "아들 꿈을 말렸는데"가 한 글자도 틀리지 않음 (문장 5·10과 같은 말·숫자)
- [ ] 아래쪽에 제목 문구 2줄이 크게 있음 (1줄 11자, 2줄 10자 — 한 줄 14자 이내, 합 21자) · 위쪽 펀치 문구는 "4번 연속 성공" 1개(8자)
- [ ] 인물·상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 2줄째 오른쪽 끝이 x 1040 안
- [ ] 인물이 실존 인물·연예인을 닮지 않음 · 우주복·연구원 복장 아님 · 표정은 허탈·후회까지 (우는 얼굴 클로즈업 없음)
- [ ] 휴대폰 화면에 실제 방송·앱 화면 서식·로고 없음
- [ ] 320px 축소본에서 "4번 연속 성공"과 하단 2줄이 읽힘 · 강조색 1곳(빨강 "안 된다며") · 틀린 말 빨강, 성공 파랑
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
