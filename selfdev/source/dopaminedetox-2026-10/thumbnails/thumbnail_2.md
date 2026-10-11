# dopaminedetox-2026-10 썸네일 2 — 인물·감정 장면 (월요일 밤 침대에서 휴대폰을 보는 얼굴)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `selfdev/guides/thumbnail_rules.md` v1.0), 대본 `dopaminedetox-2026-10.txt` v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "리셋 완료"라고 적은 다음 날 밤, 침대에서 또 휴대폰 빛을 받고 있는 **지친 얼굴**이 숫자 카드보다 시청자 자신의 밤을 더 떠올리게 한다 |
| 짝 제목 | `titles.md` **T2** "48시간만 참으면 리셋된다길래 버텼는데 월요일에 9시간을 봤습니다 …" — T1(채택)과도 어울림 |
| 숫자 근거 | 문장 11 "하지만 그 리셋은 하루도 가지 않았습니다." (0:52) · 문장 12 "월요일 하루에만 화면 시간이 9시간" (0:55.8) · 문장 15 "퇴근하고 침대에 누워서도 멈추지 못했어요" (1:12) |

## 화면 구성
- 어두운 침실, 밤. 전체 톤은 다크 네이비(#14213D)
- 왼쪽 45~50%: **가상 인물** — 30대 초반 한국인 여성 직장인, 퇴근 후 아직 단정한 사무용 블라우스를 입은 채 침대에 옆으로 누워 휴대폰을 얼굴 가까이 들고 있음
  - 휴대폰의 차가운 빛이 얼굴을 비춘다. 표정은 피곤하고 허탈함 (울음·극단적 불안 없음)
  - 휴대폰은 뒷면이 보이거나 화면이 은은한 빛만 보이게 (앱 화면·글자 없음)
- 오른쪽: 위에 노랑 상자 + 잉크 글자 **"리셋은 없었다"** (유일한 노랑 강조), 아래에 빨강 상자 + 흰 글자 **"월요일 9시간"** ("9시간"이 가장 큰 글자)
- 뇌 그림·약·병원·의사 없음 · 오른쪽 아래 구석 비움 · 얼굴과 글자는 가운데 16:9 안

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 감정 | 리셋은 없었다 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 강조) |
| 결과 | 월요일 9시간 | 흰색 | 빨강 #E63B2E 상자 (잃은 것), "9시간"을 가장 크게 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, blue #2D6CDF (what was hoped for), red #E63B2E (what was lost).
Bottom-right corner kept empty (video length badge).
Realistic photo style. A dark bedroom at night, overall dark navy tone. On the left 45% of the frame, a fictional Korean
woman in her early 30s, an office worker still wearing a plain office blouse after work, lying on her side in bed and
holding a smartphone close to her face. The phone's cold blue-white light illuminates her face. Her expression is tired,
drained and regretful, not crying, not panicked. The phone shows only its back or a soft blank glow, no app interface, no
text. Fictional person, not resembling any real or famous person, natural Korean features. On the right side, a solid
bright yellow (#FFD400) box with black bold text "리셋은 없었다". Below it, a solid red (#E63B2E) box with white bold text
"월요일 9시간", where "9시간" is the largest text in the image. No brain images, no hospital, no pills, no logos.
Keep the face and all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, red #E63B2E.
Realistic photo style. A dark bedroom at night, dark navy tone. On the left 45% of the frame, a fictional Korean woman in
her early 30s, office worker still in a plain office blouse, lying on her side in bed, holding a smartphone close to her
face, cold phone light on her tired, drained expression, not crying. The phone shows only its back or a soft blank glow.
Fictional person, not resembling any real or famous person. The right 50% of the frame is calm dark empty space with an
empty solid yellow box near the top and an empty solid red box below it. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "리셋은 없었다" · "월요일 9시간"이 한 글자도 틀리지 않음
- [ ] 숫자가 대본 문장 12 "9시간"·제목과 같음
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 30대 여성 직장인으로 보임 · 표정은 피곤·허탈 수준 (울음·극단적 불안·쓰러진 모습 없음)
- [ ] 휴대폰 화면에 앱 이름·로고·숏폼 앱 레이아웃 없음 · 뇌 그림·의사·약 없음
- [ ] 노랑 강조 1곳 · 320px 축소본에서 얼굴 표정과 "9시간"이 읽힘
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
