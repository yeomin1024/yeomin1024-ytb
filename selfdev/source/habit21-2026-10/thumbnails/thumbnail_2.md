# habit21-2026-10 썸네일 2 — 인물·감정 장면 (22일째 아침)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `guides/thumbnail_guide.md` v1.3 1번 2·3항·4-2, `selfdev/guides/thumbnail_rules.md` v1.1, 대본 `habit21-2026-10.txt` v1.0 기준 (v1.0: 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 말아 둔 운동 매트 앞에서 허탈해하는 **30대 여성 직장인의 표정**이 숫자 카드보다 "내 얘기다"를 더 끈다 (성공 썸네일 대부분이 감정이 드러난 얼굴 — 주식 결과 임시 근거) |
| 짝 제목 | `titles.md` T2 "22일째 하루쯤 괜찮다며 알람을 껐더니 21일 기록이 0일이 됐습니다 …" — 하단 2줄 = 이 제목 앞 문장을 줄인 것. T1(채택)과도 어울림 |
| 숫자 근거 | 문장 8 "진짜 시험은 22일째부터였습니다" (0:40) · 문장 9 "하루쯤은 괜찮겠다며 알람을 껐어요" (0:44) · 문장 11 "딱 사흘 만에 21일이던 연속 기록이 0일이 됐어요" (0:54) · 문장 12 "매트는 그대로 말려 있었어요" (0:59) → 모두 1분 안 |

## 화면 구성
- 다크 네이비 톤(#14213D)의 이른 아침 거실, 창으로 희미한 아침빛
- **위쪽 약 60% (y 약 40~420) = 그림 영역** — 하단 2줄을 가리지 않게 줄여서 배치
  - 왼쪽 45%: **가상 인물** — 30대 중반 한국인 여성 직장인, 출근 전 편한 차림(맨투맨), 거실 바닥에 앉아 벽에 기대 세워 둔 **말아 둔 운동 매트**를 허탈하게 바라봄. 한 손에 휴대폰(화면은 꺼져 있음). 얼굴과 매트는 위쪽 60% 안
    - 표정: 피곤·허탈·후회 (울음 없음)
  - 오른쪽 위: 노랑 상자 + 잉크 글자 **"22일째"** — 핵심 숫자, 위쪽에서 가장 큰 글자 (하단 2줄보다 크게)
  - 펀치 문구는 두지 않는다 (전에 있던 "멈췄다"는 하단 2줄이 대신함)
- **아래쪽 약 35% (y 약 450~690) = 하단 제목 2줄** — 아래에서 위로 옅어지는 검정 띠(불투명 약 80%)가 바닥을 덮고, 그 위에 왼쪽 정렬 x 48부터, 흰 글자 + 두꺼운 검정 외곽선, 글자 높이 약 90px
  - 1줄 "하루쯤 알람을 껐더니"
  - 2줄 "21일 기록이 0일이 됐다" — "0일"만 빨강 (무너진 결과), 오른쪽 끝은 x 1040 안
- 강조 2곳: 노랑 상자 "22일째" · 하단 "0일" 빨강
- 오른쪽 아래 구석 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 핵심 숫자 | 22일째 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (글자 전체 높이, 노랑 상자 1곳) — 위쪽에서 가장 큰 글자 |
| 하단 1줄 (11자) | 하루쯤 알람을 껐더니 | 흰색 + 두꺼운 검정 외곽선 | — |
| 하단 2줄 (14자) | 21일 기록이 0일이 됐다 | 흰색 + 두꺼운 검정 외곽선 | "0일"만 빨강 #E63B2E (무너진 결과) |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A dim, dark navy-toned living room in the early morning, faint pale light through a window.
Upper 60% of the frame: on the left 45%, a fictional Korean woman in her mid 30s, office-worker look, wearing a plain sweatshirt before work, sitting on the living-room floor and staring with a tired, deflated, regretful expression at a rolled-up exercise mat standing against the wall next to her. She loosely holds a smartphone with its screen turned off. Her face and the mat stay in the upper 60% of the frame.
Fictional person, not resembling any real or famous person, natural Korean features. No crying, no extreme emotion.
On the upper right, a solid bright yellow (#FFD400) box covering the full letter height with the huge black bold text "22일째", the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "하루쯤 알람을 껐더니", line 2 "21일 기록이 0일이 됐다". The word "0일" in line 2 is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 safe area. No brand logos on the mat, no app screens.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400.
Realistic photo style. A dim, dark navy-toned living room in the early morning, faint pale light through a window.
Upper 60% of the frame: on the left 45%, a fictional Korean woman in her mid 30s, office-worker look, plain sweatshirt, sitting on the floor and staring with a tired, deflated expression at a rolled-up exercise mat standing against the wall; she loosely holds a smartphone with the screen off; her face and the mat stay in the upper 60%. Fictional person, not resembling any real or famous person. On the upper right, an empty bright yellow box.
Lower third: a dark band (black, about 80% opaque, fading upward from the bottom edge) covering the floor, with clean empty space for two lines of headline text starting near the left edge.
Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "22일째" · "하루쯤 알람을 껐더니" · "21일 기록이 0일이 됐다"가 한 글자도 틀리지 않음, 그 밖의 글자 없음 (문장 8·9·11과 같은 숫자, 제목 T2와 같은 값)
- [ ] 아래쪽 약 35%에 하단 2줄이 크게 있음 (11자·14자, 합 25자 — 한 줄 14자 이내, 합 26자 이내) · 어두운 띠 위 흰 글자 + 검정 외곽선 · 2줄 오른쪽 끝이 구석 앞에서 끝남
- [ ] 얼굴·매트·"22일째"가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 위쪽 글자는 "22일째" 하나 (펀치 문구 없음)
- [ ] 인물이 실존 인물·유명 자기계발 유튜버를 닮지 않음 · 표정은 피곤·허탈 수준 (울음·쓰러짐 없음)
- [ ] 휴대폰 화면은 꺼져 있음 (앱·알람 앱 화면·로고 없음) · 운동 매트에 브랜드 없음
- [ ] 320px 축소본에서 얼굴 표정, "22일째", 하단 2줄이 읽힘 · 강조 2곳(노랑 "22일째" 상자 · 하단 "0일" 빨강) · 잃은 것은 빨강
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
