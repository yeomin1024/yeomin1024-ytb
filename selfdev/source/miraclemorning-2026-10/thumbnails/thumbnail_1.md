# miraclemorning-2026-10 썸네일 1 — 숫자 반전 (알람 시계 기록 카드)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `guides/thumbnail_guide.md` v1.3 1번 2·3항·4-2, `selfdev/guides/thumbnail_rules.md` v1.1, 대본 `miraclemorning-2026-10.txt` v1.0 기준 (v1.0: 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 얻으려던 숫자(하루 2시간)가 100배 큰 잃은 숫자(잠 -200시간)로 뒤집힌 **생활 숫자 반전**이 가장 클릭을 부른다 |
| 짝 제목 | `titles.md` **T1 (채택)** "하루 2시간 벌겠다고 새벽 5시에 일어났다가 잠 200시간을 잃었습니다 …" — 하단 2줄 = 이 제목 앞 문장을 줄인 것. T3과도 어울림 |
| 숫자 근거 | 문장 1 "알람을 새벽 5시로 바꿨어요" (0:00) · 문장 6·7 "아침 2시간", "하루가 2시간 늘어난 기분" (0:24~0:36) · 문장 11 "줄어든 잠이 모두 200시간이었어요" (0:50) → 모두 1분 안 |

## 화면 구성
- 배경: 다크 네이비 #14213D의 새벽 방 분위기 (창밖은 짙은 남색, 아주 은은한 빛 번짐). 장식 없음
- **위쪽 약 60% (y 약 40~420) = 그림 영역** — 하단 2줄을 가리지 않게 줄여서 배치
  - 왼쪽 30%: 단순한 탁상용 숫자 알람 시계(브랜드·로고 없음). 화면에 큰 숫자 **"05:00"** — 노랑 #FFD400 화면 위 잉크 #1E1E1E 숫자 (노랑 상자는 이곳 하나)
  - 가운데: 굵은 크림색 #F2EBDD 화살표(→)
  - 오른쪽 45%: 넓은 빨강 #E63B2E 상자 안 흰 글자 **"잠 -200시간"** — 핵심 숫자, 화면 높이의 약 25% (하단 2줄보다 크게)
  - 펀치 문구는 두지 않는다 (전에 있던 "하루 +2시간"은 하단 1줄로 옮김)
- **아래쪽 약 35% (y 약 450~690) = 하단 제목 2줄** — 아래에서 위로 옅어지는 검정 띠(불투명 약 80%) 위, 왼쪽 정렬 x 48부터, 흰 글자 + 두꺼운 검정 외곽선, 글자 높이 약 90px
  - 1줄 "하루 2시간 벌겠다고" — "2시간"만 노랑 (얻으려던 숫자)
  - 2줄 "잠 200시간을 잃었다" — 오른쪽 끝은 x 1040 안
- 강조 3곳: 시계 노랑 화면 · 빨강 상자 "잠 -200시간" · 하단 "2시간" 노랑
- 오른쪽 아래 구석(약 220×70px)은 비움 · 인물 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 시계 (그림 속 숫자) | 05:00 | 잉크 #1E1E1E (노랑 시계 화면 위) | 노랑 #FFD400 화면 (노랑 상자 1곳) |
| 핵심 숫자 | 잠 -200시간 | 흰색 (빨강 #E63B2E 상자 위) | 위쪽에서 가장 큰 글자 — 잃은 것 = 빨강 |
| 하단 1줄 (11자) | 하루 2시간 벌겠다고 | 흰색 + 두꺼운 검정 외곽선 | "2시간"만 노랑 #FFD400 (얻으려던 숫자) |
| 하단 2줄 (12자) | 잠 200시간을 잃었다 | 흰색 + 두꺼운 검정 외곽선 | — (빨강은 위쪽 상자에 이미 있음) |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic. Dark navy (#14213D) pre-dawn background, like a quiet bedroom before sunrise, with a very soft glow; nothing decorative.
Upper 60% of the frame: on the left, a simple generic tabletop digital alarm clock (no brand, no logo) whose display is a bright yellow (#FFD400) panel showing large ink-black digits "05:00". In the middle, a thick cream (#F2EBDD) arrow pointing right. On the right, a wide solid red (#E63B2E) rounded box containing the huge white bold text "잠 -200시간", the largest text in the image, about a quarter of the image height.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "하루 2시간 벌겠다고", line 2 "잠 200시간을 잃었다". The word "2시간" in line 1 is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep all text and the clock inside the central 16:9 safe area. No people, no faces, no phone screens, no app interfaces, no brain imagery.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss red #E63B2E.
Clean flat editorial graphic. Dark navy (#14213D) pre-dawn bedroom background with a very soft glow.
Upper 60% of the frame: on the left, a simple generic tabletop digital alarm clock (no brand, no logo) with a blank bright yellow (#FFD400) display panel; in the middle, a thick cream arrow pointing right; on the right, a wide empty solid red (#E63B2E) rounded box.
Lower third: a dark band (black, about 80% opaque, fading upward from the bottom edge) with clean empty space for two lines of headline text starting near the left edge. Nothing else in the lower third.
No people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "05:00" · "잠 -200시간" · "하루 2시간 벌겠다고" · "잠 200시간을 잃었다"가 한 글자도 틀리지 않음, 그 밖의 글자 없음 (문장 1·6·11과 같은 숫자, 제목 T1과 같은 값)
- [ ] 아래쪽 약 35%에 하단 2줄이 크게 있음 (11자·12자, 합 23자 — 한 줄 14자 이내, 합 26자 이내) · 어두운 띠 위 흰 글자 + 검정 외곽선 · 2줄 오른쪽 끝이 구석 앞에서 끝남
- [ ] 시계·화살표·빨강 상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 글자는 "잠 -200시간"과 시계 숫자뿐 (펀치 문구 없음)
- [ ] 320px 축소본에서 "잠 -200시간"과 하단 2줄이 바로 읽힘
- [ ] 강조 3곳(시계 노랑 화면 · 빨강 상자 · 하단 "2시간" 노랑) · 잃은 것은 빨강 · 노랑 상자는 시계 화면 1곳
- [ ] 실제 알람 앱·시계 브랜드처럼 보이지 않음 · 뇌 그림·휴대폰 화면 없음
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
