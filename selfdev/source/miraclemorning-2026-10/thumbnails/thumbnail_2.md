# miraclemorning-2026-10 썸네일 2 — 인물·감정 장면 (오후 회의 전 꾸벅)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `guides/thumbnail_guide.md` v1.3 1번 2·3항·4-2, `selfdev/guides/thumbnail_rules.md` v1.1 4번: 30대 한국인 여성 직장인 가상 인물, 대본 `miraclemorning-2026-10.txt` v1.0 기준 (v1.0: 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 잠을 줄인 결과를 마주한 **사람의 표정**(오후 사무실에서 꾸벅 조는 모습)이 숫자 카드보다 "내 얘기다"를 더 끈다 |
| 짝 제목 | `titles.md` T2 "새벽 5시 인증 100일 만에 잠 200시간이 사라졌습니다 …" — 하단 2줄 = 이 제목 앞 문장을 줄인 것 |
| 숫자 근거 | 문장 1 "알람을 새벽 5시로 바꿨어요" (0:00) · 문장 2 "100일 동안 매일 인증" (0:06) · 문장 10 "100일째인 4월 14일" (0:45) · 문장 11 "200시간" (0:50) · 문장 13 "바로 그날 오후 회의에서 저는 꾸벅꾸벅 졸았어요" (0:59) → 1분 안. 빈 커피 잔은 문장 16 (1:14)의 소품이라 작게만 |

## 화면 구성
- 배경: 밝은 오후 사무실을 흐리게 (크림·회색 톤, 창으로 오후 햇빛)
- **위쪽 약 60% (y 약 40~420) = 그림 영역** — 하단 2줄을 가리지 않게 줄여서 배치
  - 왼쪽 45%: **가상 인물** — 30대 한국인 여성 직장인(단정한 블라우스나 니트, 사원증 끈은 글자 없음), 모니터 앞 책상에 턱을 괴고 눈이 감긴 채 고개가 떨어지는 순간, 피곤하고 허탈한 표정. 얼굴과 책상 윗면은 위쪽 60% 안. 책상에 빈 종이 커피 잔 몇 개(로고 없음), 모니터 화면은 흐려서 글자 없음
  - 오른쪽: 넓은 빨강 #E63B2E 상자 안 흰 글자 **"잠 -200시간"** — 핵심 숫자, 위쪽에서 가장 큰 글자 (하단 2줄보다 크게)
  - 펀치 문구는 두지 않는다 (전에 있던 "100일째, 무너졌다"는 하단 2줄과 겹쳐 뺌 — 조는 얼굴이 그 말을 대신함)
- **아래쪽 약 35% (y 약 450~690) = 하단 제목 2줄** — 아래에서 위로 옅어지는 검정 띠(불투명 약 80%)가 책상 아래쪽을 덮고, 그 위에 왼쪽 정렬 x 48부터, 흰 글자 + 두꺼운 검정 외곽선, 글자 높이 약 90px
  - 1줄 "새벽 5시 인증 100일" — "100일"만 노랑 (챌린지 목표 일수)
  - 2줄 "잠 200시간 사라졌다" — 오른쪽 끝은 x 1040 안
- 강조 2곳: 빨강 상자 "잠 -200시간" · 하단 "100일" 노랑
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 핵심 숫자 | 잠 -200시간 | 흰 글자 (빨강 #E63B2E 상자) | 위쪽에서 가장 큰 글자 — 잃은 것 = 빨강 |
| 하단 1줄 (13자) | 새벽 5시 인증 100일 | 흰색 + 두꺼운 검정 외곽선 | "100일"만 노랑 #FFD400 |
| 하단 2줄 (12자) | 잠 200시간 사라졌다 | 흰색 + 두꺼운 검정 외곽선 | — (빨강은 위쪽 상자에 이미 있음) |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Softly blurred bright afternoon office background in warm cream and grey tones, afternoon sunlight through a window.
Upper 60% of the frame: on the left 45%, a fictional Korean woman in her mid-thirties, office worker (neat blouse or knit top, plain lanyard with no text), sitting at her desk in front of a monitor, chin resting on her hand, eyes closed, head drooping as she dozes off; tired, drained, slightly regretful expression. Her face and the desktop stay in the upper 60% of the frame.
On the desk, a few empty plain paper coffee cups with no logos; the monitor screen is blurred with nothing readable.
Fictional person, not resembling any real or famous person, natural Korean features, realistic photo style. Not a doctor, no hospital, no pills, no crying, no collapse.
On the right side of the upper 60%, a wide solid red (#E63B2E) rounded box with the huge white bold text "잠 -200시간", the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "새벽 5시 인증 100일", line 2 "잠 200시간 사라졌다". The word "100일" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 safe area. No app screens, no phone interfaces, no brain imagery.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss red #E63B2E.
Realistic photo style. Softly blurred bright afternoon office background, afternoon sunlight.
Upper 60% of the frame: on the left 45%, a fictional Korean woman in her mid-thirties, office worker, dozing off at her desk in front of a blurred monitor, chin on her hand, eyes closed, tired and drained expression, a few empty plain paper coffee cups with no logos on the desk; her face and the desktop stay in the upper 60%.
Fictional person, not resembling any real or famous person, natural Korean features. Not a doctor, no hospital.
On the right side of the upper 60%, an empty wide solid red (#E63B2E) rounded box.
Lower third: a dark band (black, about 80% opaque, fading upward from the bottom edge) covering the lower part of the desk, with clean empty space for two lines of headline text starting near the left edge.
Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "잠 -200시간" · "새벽 5시 인증 100일" · "잠 200시간 사라졌다"가 한 글자도 틀리지 않음, 그 밖의 글자 없음 (문장 1·2·11과 같은 숫자, 제목 T2와 같은 값)
- [ ] 아래쪽 약 35%에 하단 2줄이 크게 있음 (13자·12자, 합 25자 — 한 줄 14자 이내, 합 26자 이내) · 어두운 띠 위 흰 글자 + 검정 외곽선 · 2줄 오른쪽 끝이 구석 앞에서 끝남
- [ ] 얼굴·빨강 상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 글자는 "잠 -200시간" 하나 (펀치 문구 없음)
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 의사·병원·약 없음 · 표정은 피곤·허탈 수준(우는 얼굴·쓰러진 모습 없음)
- [ ] 커피 잔·모니터·사원증에 로고·글자 없음 · 실제 앱 화면 없음
- [ ] 320px 축소본에서 졸고 있는 얼굴, "잠 -200시간", 하단 2줄이 읽힘 · 강조 2곳(빨강 상자 · 하단 "100일" 노랑) · 잃은 것은 빨강
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
