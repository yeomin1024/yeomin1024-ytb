# sarcopenia-2026-10 썸네일 2 — 인물·감정 장면 (계단 난간을 붙잡은 순간)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3). 인물을 허리 위로 잡아 위쪽 약 60%로 올리고, 그림 영역 글자를 빨강 상자 "악력 17kg" 하나로 줄임 ("매일 걸었는데"는 하단 1줄 "매일 만 보 걷던 60대"와 "매일"이 겹쳐 뺌), 하단 2줄 "매일 만 보 걷던 60대 / 2년 만에 근감소증" 추가 (`guides/thumbnail_guide.md` v1.3, `health/guides/thumbnail_rules.md` v1.2), 대본 sarcopenia-2026-10.txt v1.0 기준 (v1.0: 2026-10-11 최초 작성, `guides/thumbnail_guide.md` v1.2, `health/guides/thumbnail_rules.md` v1.1 4번: 가상 인물, 넘어지는 장면 금지 — 계단 손잡이를 잡고 멈칫하는 정도까지)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 계단에서 다리에 힘이 풀려 난간을 붙잡은 **60대 여성의 당황한 표정**이 숫자 카드보다 감정을 더 끈다 |
| 짝 제목 | `titles.md` T2 "매일 만 보 걷던 60대가 2년 만에 근감소증이 됐습니다. 근력운동 없이 걷기만 한 사람들이 꼭 하는 후회" — 하단 2줄 = 이 앞 문장을 줄인 것. T1과도 어울림 |
| 숫자 근거 | 문장 2 "그때 저는 예순" (0:05) · 문장 5 "하루도 빠짐없이 만 보" (0:23) · 문장 6 "2년 사이" (0:27) · 문장 9 "올봄 계단을 내려가다 다리에 힘이 풀려 난간을 붙잡았어요" (0:41) · 문장 10 "악력은 17kg" (0:46) · 문장 12 "근감소증이라는 진단" (0:57) → 모두 1분 안 |

## 화면 구성
- **위쪽 약 60% (y 0~430):** 밝은 낮, 아파트 단지 바깥 계단. 배경은 크림 톤으로 흐리게
  - 왼쪽 45%: **가상 인물** — 60대 초반 한국인 여성, 단정한 짧은 머리, 무늬·글자·로고 없는 밝은 단색 바람막이. 허리 위까지 잡은 장면: 계단을 내려가다 한 손으로 금속 난간을 꽉 붙잡고 멈춰 선 채 자기 다리 쪽을 내려다보며 놀라고 당황한 표정. 얼굴·난간을 잡은 손이 위쪽 60% 안에 온다 (그 아래는 하단 띠 밑으로 어두워짐)
    - **넘어지거나 주저앉은 모습이 아니다** — 몸을 세운 채 난간을 잡고 서 있다
  - 오른쪽 위: 빨강 둥근 상자 안 흰 글자 **"악력 17kg"** — "17kg"이 화면에서 가장 큰 글자 (하단 2줄보다 큼). "악력"이 그림 영역의 유일한 펀치 문구
- **아래쪽 약 35% (y 약 450~690):** 아래에서 위로 옅어지는 다크 네이비 띠 위에 하단 2줄. 왼쪽 정렬 x 48부터, 흰 글자 + 두꺼운 검정 외곽선, 글자 높이 약 80~100px. "근감소증"만 빨강. 2번째 줄은 x 1040 안에서 끝남
- 오른쪽 아래 구석(약 220×70)은 비움. 얼굴과 글자는 가운데 16:9 안에

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 + 결과 숫자 (오른쪽 위) | 악력 17kg | 흰 글자 (빨강 #E63B2E 상자) | "17kg"을 가장 크게 |
| 하단 1줄 | 매일 만 보 걷던 60대 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 없음 |
| 하단 2줄 | 2년 만에 근감소증 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "근감소증"만 빨강 #E63B2E (나빠진 결과) |

- 하단 2줄 = 짝 제목 T2 앞 문장 "매일 만 보 걷던 60대가 2년 만에 근감소증이 됐습니다"를 줄인 것 (제목 단어를 그대로 씀). 1줄 13자 · 2줄 10자, 합 23자 (띄어쓰기 포함)
- 펀치 "악력"(2자)은 하단 2줄에 없는 말이다. 짝 제목 T2에 없는 **악력 17kg**(문장 10)과 계단 장면(문장 9)을 그림 쪽이 보탠다
- 강조 합 2곳: 빨강 상자 "악력 17kg", 빨강 "근감소증". 노랑 없음, 파랑 글자 없음

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Bright daytime, outdoor concrete stairs in an apartment complex, background softly blurred in warm
cream tones. On the left 45% of the frame, a fictional Korean woman in her early 60s with neat short hair, wearing a plain
light-colored windbreaker with no patterns, no text and no logos, shown from the waist up. She was walking down the stairs
and has suddenly stopped, gripping the metal handrail firmly with one hand, looking down toward her own legs with a
surprised and flustered expression. She is standing upright, not falling, not sitting down, not injured. Her face and the
hand on the handrail are in the upper 60% of the frame. Fictional person, not resembling any real or famous person,
natural Korean features. No doctor, no white coat, no hospital, no walking stick, no gym equipment. On the upper right
side, a wide solid red (#E63B2E) rounded box containing the white bold text "악력 17kg", with "17kg" much larger than the
word, the largest text in the image. No crying, no pain, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "매일 만 보 걷던 60대", line 2 "2년 만에 근감소증". The word "근감소증" is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, gain red #E63B2E.
Realistic photo style. Bright daytime, outdoor concrete stairs in an apartment complex, softly blurred cream background.
On the left 45% of the frame, a fictional Korean woman in her early 60s in a plain light windbreaker with no logos, shown
from the waist up, suddenly stopping on the stairs and gripping the metal handrail with one hand, surprised and flustered
expression, her face and hand in the upper 60% of the frame. Standing upright, not falling. Fictional person, not
resembling any real or famous person. No hospital, no doctor. On the upper right, an empty solid red (#E63B2E) rounded box
with calm empty space around it.
Lower third: a dark navy (#14213D) band that fades upward from the bottom edge, completely empty, reserved for two lines of
headline text. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "악력 17kg" · "매일 만 보 걷던 60대" · "2년 만에 근감소증"이 한 글자도 틀리지 않음 · 옷·배경에 읽히는 글자·로고 없음 · 물음표·느낌표 없음 · 그 밖의 글자 없음
- [ ] 숫자가 대본(문장 2·5·6·10·12)·제목과 같음 — 만 보, 60대(예순 → 예순둘), 2년, 17kg · 인물이 60대 초반 **여성**(사연 목소리와 같음)
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · **넘어지거나 주저앉는 장면 아님**(난간을 잡고 서 있음) · 의사·흰 가운·병원·지팡이 없음 · 표정은 놀람·당황 수준
- [ ] 얼굴·손·빨강 상자가 위쪽 약 60% 안에 있어 하단 2줄을 가리지 않음 · 그림 영역 문구는 "악력 17kg" 상자 1개뿐
- [ ] 하단 2줄이 아래쪽 약 35%에 크게 있음, 왼쪽 정렬, 2번째 줄이 오른쪽 아래 구석 전에 끝남 · 한 줄 14자 이내(13자·10자), 2줄 합 26자 이내(23자)
- [ ] "17kg"이 가장 큼 · 강조는 빨강 상자 1곳, 빨강 "근감소증" 1곳 · 파랑 글자 없음
- [ ] 320px 축소본에서 표정, "17kg", 하단 2줄이 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
