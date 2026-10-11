# dopaminedetox-2026-10 썸네일 2 — 인물·감정 장면 (월요일 밤 침대에서 휴대폰을 보는 얼굴)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `guides/thumbnail_guide.md` v1.3 1번 2·3항·4-2, `selfdev/guides/thumbnail_rules.md` v1.1, 대본 `dopaminedetox-2026-10.txt` v1.0 기준 (v1.0: 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "리셋 완료"라고 적은 다음 날 밤, 침대에서 또 휴대폰 빛을 받고 있는 **지친 얼굴**이 숫자 카드보다 시청자 자신의 밤을 더 떠올리게 한다 |
| 짝 제목 | `titles.md` **T2** "48시간만 참으면 리셋된다길래 버텼는데 월요일에 9시간을 봤습니다 …" — 하단 2줄 = 이 제목 앞 문장을 줄인 것. T1(채택)과도 어울림 |
| 숫자 근거 | 문장 9 "일요일 밤 10시, 48시간을 채우자 …" (0:43) · 문장 11 "하지만 그 리셋은 하루도 가지 않았습니다." (0:52) · 문장 12 "월요일 하루에만 화면 시간이 9시간" (0:55.8) · 문장 15 "퇴근하고 침대에 누워서도 멈추지 못했어요" (1:12) |

## 화면 구성
- 어두운 침실, 밤. 전체 톤은 다크 네이비(#14213D)
- **위쪽 약 60% (y 약 40~420) = 그림 영역** — 하단 2줄을 가리지 않게 줄여서 배치
  - 왼쪽 45~50%: **가상 인물** — 30대 초반 한국인 여성 직장인, 퇴근 후 아직 단정한 사무용 블라우스를 입은 채 침대에 옆으로 누워 휴대폰을 얼굴 가까이 들고 있음. 얼굴과 휴대폰은 위쪽 60% 안
    - 휴대폰의 차가운 빛이 얼굴을 비춘다. 표정은 피곤하고 허탈함 (울음·극단적 불안 없음)
    - 휴대폰은 뒷면이 보이거나 화면이 은은한 빛만 보이게 (앱 화면·글자 없음)
  - 오른쪽 위: 노랑 상자 + 잉크 글자 **"리셋은 없었다"** (펀치 문구 1개, 7자)
  - 그 아래: 빨강 상자 + 흰 글자 **"9시간"** — 핵심 숫자, 화면에서 가장 큰 글자 (하단 2줄보다 크게)
- **아래쪽 약 35% (y 약 450~690) = 하단 제목 2줄** — 아래에서 위로 옅어지는 검정 띠(불투명 약 80%)가 이불을 덮고, 그 위에 왼쪽 정렬 x 48부터, 흰 글자 + 두꺼운 검정 외곽선, 글자 높이 약 90px
  - 1줄 "48시간을 버텼는데" — "48시간"만 노랑 (처음 목표 숫자)
  - 2줄 "월요일에 9시간을 봤다" — 오른쪽 끝은 x 1040 안
- 강조 3곳: 노랑 상자 "리셋은 없었다" · 빨강 상자 "9시간" · 하단 "48시간" 노랑 글자
- 뇌 그림·약·병원·의사 없음 · 오른쪽 아래 구석 비움 · 얼굴과 글자는 가운데 16:9 안

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 문구 | 리셋은 없었다 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 노랑 상자 1곳) |
| 핵심 숫자 | 9시간 | 흰색 | 빨강 #E63B2E 상자 (잃은 것), 가장 큰 글자 |
| 하단 1줄 (10자) | 48시간을 버텼는데 | 흰색 + 두꺼운 검정 외곽선 | "48시간"만 노랑 #FFD400 글자 (처음 목표 숫자) |
| 하단 2줄 (12자) | 월요일에 9시간을 봤다 | 흰색 + 두꺼운 검정 외곽선 | — (빨강은 위쪽 상자에 이미 있음) |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, blue #2D6CDF (what was hoped for), red #E63B2E (what was lost).
Bottom-right corner kept empty (video length badge).
Realistic photo style. A dark bedroom at night, overall dark navy tone.
Upper 60% of the frame: on the left 45%, a fictional Korean woman in her early 30s, an office worker still wearing a plain office blouse after work, lying on her side in bed and holding a smartphone close to her face. The phone's cold blue-white light illuminates her face. Her expression is tired, drained and regretful, not crying, not panicked. The phone shows only its back or a soft blank glow, no app interface, no text. Her face and the phone stay in the upper 60% of the frame.
Fictional person, not resembling any real or famous person, natural Korean features.
On the upper right, a solid bright yellow (#FFD400) box covering the full letter height with black bold text "리셋은 없었다". Below it, a solid red (#E63B2E) box with the huge white bold text "9시간", the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "48시간을 버텼는데", line 2 "월요일에 9시간을 봤다". The word "48시간" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
No brain images, no hospital, no pills, no logos. Keep the face and all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, red #E63B2E.
Realistic photo style. A dark bedroom at night, dark navy tone.
Upper 60% of the frame: on the left 45%, a fictional Korean woman in her early 30s, office worker still in a plain office blouse, lying on her side in bed, holding a smartphone close to her face, cold phone light on her tired, drained expression, not crying. The phone shows only its back or a soft blank glow; her face and the phone stay in the upper 60%. Fictional person, not resembling any real or famous person. On the upper right, an empty solid yellow box and an empty solid red box below it.
Lower third: a dark band (black, about 80% opaque, fading upward from the bottom edge) covering the blanket, with clean empty space for two lines of headline text starting near the left edge.
Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "리셋은 없었다" · "9시간" · "48시간을 버텼는데" · "월요일에 9시간을 봤다"가 한 글자도 틀리지 않음, 그 밖의 글자 없음
- [ ] 숫자가 대본 문장 9 "48시간"·문장 12 "9시간"·제목 T2와 같음
- [ ] 아래쪽 약 35%에 하단 2줄이 크게 있음 (10자·12자, 합 22자 — 한 줄 14자 이내, 합 26자 이내) · 어두운 띠 위 흰 글자 + 검정 외곽선 · 2줄 오른쪽 끝이 구석 앞에서 끝남
- [ ] 얼굴·휴대폰·두 상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 펀치 문구는 "리셋은 없었다" 1개(10자 이내, 하단 2줄과 겹치는 말 없음)
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 30대 여성 직장인으로 보임 · 표정은 피곤·허탈 수준 (울음·극단적 불안·쓰러진 모습 없음)
- [ ] 휴대폰 화면에 앱 이름·로고·숏폼 앱 레이아웃 없음 · 뇌 그림·의사·약 없음
- [ ] 강조 3곳(노랑 상자 · 빨강 상자 · 하단 "48시간" 노랑) · 320px 축소본에서 얼굴 표정, "9시간", 하단 2줄이 읽힘
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
