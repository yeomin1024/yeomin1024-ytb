# miraclemorning-2026-10 썸네일 2 — 인물·감정 장면 (오후 회의 전 꾸벅)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `selfdev/guides/thumbnail_rules.md` v1.0 4번: 30대 한국인 여성 직장인 가상 인물), 대본 `miraclemorning-2026-10.txt` v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 잠을 줄인 결과를 마주한 **사람의 표정**(오후 사무실에서 꾸벅 조는 모습)이 숫자 카드보다 "내 얘기다"를 더 끈다 |
| 짝 제목 | `titles.md` T2 "새벽 5시 인증 100일 만에 잠 200시간이 사라졌습니다 …" |
| 숫자 근거 | 문장 10 "100일째인 4월 14일" (0:45) · 문장 11 "200시간" (0:50) · 문장 13 "바로 그날 오후 회의에서 저는 꾸벅꾸벅 졸았어요" (0:59) → 1분 안. 빈 커피 잔은 문장 16 (1:14)의 소품이라 작게만 |

## 화면 구성
- 배경: 밝은 오후 사무실을 흐리게 (크림·회색 톤, 창으로 오후 햇빛)
- 왼쪽 45%: **가상 인물** — 30대 한국인 여성 직장인(단정한 블라우스나 니트, 사원증 끈은 글자 없음), 모니터 앞 책상에 턱을 괴고 눈이 감긴 채 고개가 떨어지는 순간, 피곤하고 허탈한 표정. 책상에 빈 종이 커피 잔 몇 개(로고 없음), 모니터 화면은 흐려서 글자 없음
- 오른쪽 위: **"100일째, 무너졌다"** (흰 글자, 네이비 #14213D 상자)
- 오른쪽 아래: 빨강 #E63B2E 상자 안 흰 글자 **"잠 -200시간"** — 가장 큰 글자
- 노랑 강조는 "100일째" 세 글자 뒤 노랑 상자 한 곳(잉크 글자)
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 장면 | 100일째, 무너졌다 | "100일째"는 잉크 #1E1E1E 글자 + 노랑 #FFD400 상자, ", 무너졌다"는 흰 글자 + 네이비 상자 | 노랑 상자 (글자 전체 높이, 유일한 강조) |
| 결과 | 잠 -200시간 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Softly blurred bright afternoon office background in warm cream and grey tones, afternoon sunlight through a window.
On the left 45% of the frame, a fictional Korean woman in her mid-thirties, office worker (neat blouse or knit top, plain lanyard with no text), sitting at her desk in front of a monitor, chin resting on her hand, eyes closed, head drooping as she dozes off; tired, drained, slightly regretful expression.
On the desk, a few empty plain paper coffee cups with no logos; the monitor screen is blurred with nothing readable.
Fictional person, not resembling any real or famous person, natural Korean features, realistic photo style. Not a doctor, no hospital, no pills, no crying, no collapse.
On the right side, upper headline "100일째, 무너졌다": the part "100일째" in ink-black letters on a solid bright yellow (#FFD400) box covering the full letter height, and the part ", 무너졌다" in white letters on a dark navy (#14213D) box.
Below it, a wide solid red (#E63B2E) rounded box with the huge white bold text "잠 -200시간", the largest element.
Keep the face and all text inside the central 16:9 safe area. No app screens, no phone interfaces, no brain imagery.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss red #E63B2E.
Realistic photo style. Softly blurred bright afternoon office background, afternoon sunlight.
On the left 45% of the frame, a fictional Korean woman in her mid-thirties, office worker, dozing off at her desk in front of a blurred monitor, chin on her hand, eyes closed, tired and drained expression, a few empty plain paper coffee cups with no logos on the desk.
Fictional person, not resembling any real or famous person, natural Korean features. Not a doctor, no hospital.
The right 50% of the frame is calm empty space for headline text, with an empty short yellow (#FFD400) box and an empty dark navy (#14213D) box in the upper right, and an empty wide solid red (#E63B2E) rounded box in the lower right-middle.
Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "100일째, 무너졌다" · "잠 -200시간"이 한 글자도 틀리지 않음 (문장 10·11과 같은 숫자, 제목 T2와 같은 값)
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 의사·병원·약 없음 · 표정은 피곤·허탈 수준(우는 얼굴·쓰러진 모습 없음)
- [ ] 커피 잔·모니터·사원증에 로고·글자 없음 · 실제 앱 화면 없음
- [ ] 320px 축소본에서 졸고 있는 얼굴과 "잠 -200시간"이 읽힘 · 노랑 강조 1곳 · 잃은 것은 빨강
- [ ] 문구 2줄 20자 이내 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
