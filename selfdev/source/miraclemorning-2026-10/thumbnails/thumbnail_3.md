# miraclemorning-2026-10 썸네일 3 — 대비 (새벽 5시의 나 vs 오후의 나)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `selfdev/guides/thumbnail_rules.md` v1.0 2번: 왼쪽 기대 / 오른쪽 결과), 대본 `miraclemorning-2026-10.txt` v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 같은 사람의 **새벽(기대)과 오후(결과)를 나란히** 보여 주면, 문제 분석 첫 번째 메시지("아침 2시간은 잠에서 빌린 시간")가 한눈에 전해진다 |
| 짝 제목 | `titles.md` T3 (짧은 변형) "잠 줄여 새벽 5시 100일, 잃은 잠 200시간 …" |
| 숫자 근거 | 문장 1 "새벽 5시" (0:00) · 문장 2 "100일 동안 매일 인증" (0:06) · 문장 11 "200시간" (0:50) · 문장 13 오후 회의 졸음 (0:59) → 1분 안 |

## 화면 구성
- 화면을 가운데 세로선으로 반씩 나눔 (얇은 크림 선)
- **왼쪽 = 기대:** 새벽, 창밖은 짙은 네이비. 따뜻한 스탠드 불빛 아래 책상, 펼친 책, 글자 없는 노트, 단순한 숫자 알람 시계 "05:00". **같은 가상 인물**(30대 한국인 여성 직장인)이 의욕 있게 앉아 책을 보는 모습. 아래쪽에 크림 #F2EBDD 상자 + 잉크 글자 **"인증 100일"** (기대라서 '좋아짐'의 파랑을 쓰지 않음)
- **오른쪽 = 결과:** 밝은 오후 사무실, 같은 인물이 모니터 앞에서 꾸벅 조는 모습, 피곤한 얼굴. 아래쪽에 빨강 #E63B2E 상자 + 흰 글자 **"잠 -200시간"** (왼쪽 문구보다 크게)
- 노랑 강조: 왼쪽 시계 화면 "05:00" 한 곳 (노랑 화면 + 잉크 숫자)
- 오른쪽 아래 구석은 비움 (오른쪽 문구 상자는 그보다 위에)

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 시계 | 05:00 | 잉크 #1E1E1E (노랑 시계 화면 위) | 노랑 #FFD400 (유일한 강조) |
| 왼쪽 | 인증 100일 | 잉크 #1E1E1E 글자 (크림 #F2EBDD 상자) | — |
| 오른쪽 | 잠 -200시간 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Split-screen comparison divided vertically in the middle by a thin cream line. Realistic photo style. The SAME fictional Korean woman in her mid-thirties, office worker, appears on both sides.
LEFT HALF (expectation): before sunrise, the window behind is deep navy (#14213D); a desk lit by a warm desk lamp, an open book and a plain notebook with no readable writing, and a simple generic digital alarm clock (no brand) whose display is a bright yellow (#FFD400) panel showing ink-black digits "05:00". The woman sits upright, motivated, reading. At the bottom of the left half, a solid cream (#F2EBDD) box with ink-black bold text "인증 100일".
RIGHT HALF (result): a bright afternoon office; the same woman dozing at her desk in front of a blurred monitor, chin on her hand, eyes closed, tired and drained expression. In the lower-middle of the right half (not in the bottom-right corner), a solid red (#E63B2E) box with huge white bold text "잠 -200시간", larger than the left label.
Fictional person, not resembling any real or famous person, natural Korean features. No doctor, no hospital, no pills, no crying. No phone screens, no app interfaces, no book covers with titles, no brain imagery. Keep faces and text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Split-screen divided vertically by a thin cream line. Realistic photo style. The same fictional Korean woman in her mid-thirties, office worker, on both sides; not resembling any real or famous person.
Left half: before sunrise, deep navy window, warm desk lamp, open book, plain notebook, a generic digital alarm clock with a blank bright yellow display; the woman reading, motivated. An empty solid cream (#F2EBDD) box at the bottom of the left half.
Right half: bright afternoon office, the same woman dozing at her desk in front of a blurred monitor, tired expression. An empty solid red (#E63B2E) box in the lower-middle of the right half, larger than the cream box.
Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "05:00" · "인증 100일" · "잠 -200시간"이 한 글자도 틀리지 않음 (문장 1·2·11과 같은 숫자, 제목 T3과 같은 값)
- [ ] 양쪽 인물이 같은 사람으로 보임 · 실존 인물·유명인을 닮지 않음 · 표정은 의욕/피곤 수준
- [ ] 책 표지 제목·챌린지 앱·인증 앱 화면 없음 · 시계 브랜드 없음
- [ ] 320px 축소본에서 "잠 -200시간"이 바로 읽힘 · 노랑 강조 1곳 · 기대는 크림(중립), 잃은 것은 빨강
- [ ] 문구 2줄(시계 숫자 제외) 20자 이내 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
