# gungmin-sigi-2026-10 썸네일 1 — 본안(클릭률 최대): 밤 식탁에서 이마를 짚고 고개를 떨군 57세 남성 + '조기수령' 낱말

버전: v1.0 — 2026-10-18 — 대본 gungmin-sigi-2026-10.txt v1.0 기준. `guides/thumbnail_guide.md` v3.14. 근거: `README.md`.

| 항목 | 값 |
|---|---|
| 역할 | **본안** — 클릭률을 가장 높게. 업로드할 때 기본 썸네일 |
| 시험하는 가설 | 손해를 알고 좌절한 실사 얼굴과 손해를 만드는 '조기수령' 낱말이 가장 클릭을 부른다 |
| 짝 제목 | titles.md R1 「국민연금 5년 당기면 77세부터 손해, 미루면 84세부터 이득」 |
| 문구 | 제목 R1에서 '미루면 84세부터 이득'을 빼고(손해 쪽만), 시청자층 낱말 '50대'를 더했다 (`README.md` 2번) |
| 근거 (`README.md` 3번) | 노후·연금·절세 묶음: 걱정 표정 23% vs 7% · 실사 인물 성공 배수 상위 16개 중 56% · 빨강 글자 48% vs 32% · 손해 낱말 43% vs 18%. 국민연금 받는 시기 성공 썸네일 3개 모두 큰 글자에 나이 숫자 |
| 숫자 근거 | '5년 당기면 77세부터 손해' = 60세 월 91만 원 vs 65세 월 130만 원, 받은 돈 합계가 76세 8개월에 같아지고 그 뒤로 적음 (문장 6·29~32, `calc/calc.py` 2번) |
| 인물 나이 | 대본 예시는 57세 남편. 젊어 보이는 50대 초반처럼 그린다 (시청자 대표) |

## 화면 구성
- **위쪽 약 62%**:
  - 오른쪽 55%: 57세 한국인 남성, 나이보다 젊어 보이고(50대 초반처럼), 짧게 정돈한 검은 머리에 관자놀이만 희끗하다. 진회색 니트 카디건에 흰 티셔츠.
    - 밤, 집 거실 식탁 앞에 앉아 가슴 위까지 크게. 한 손으로 이마를 짚고 고개를 떨궜으며, 눈을 질끈 감고 미간을 찌푸렸다 (손해를 알고 난 좌절·후회). 어깨가 처졌다. 얼굴은 손에 다 가리지 않게. 식탁 위에는 빈 찻잔 하나와 글자 없는 흰 종이 한 장.
  - 왼쪽 45%: 낱말 꼬리표 1개 '조기수령' — 빨강 둥근 상자에 큰 흰 평면 글자. 굵은 빨강 화살표 2개가 꼬리표에서 남성 쪽 아래로 향한다.
  - 배경: 밤의 아파트 거실, 창밖 불빛을 흐리게, 차가운 푸른빛. 얼굴에만 따뜻한 펜던트 조명.
- **아래쪽 약 35%**: 아래에서 위로 옅어지는 검은 띠 위에 큰 글자 2줄, 왼쪽 정렬.
- 오른쪽 아래 구석(약 220×70)은 비운다.

## 문구 (그대로 사용)
| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50대 국민연금 5년 당기면 | '50대' 흰색 · **'국민연금 5년 당기면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 77세부터 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 조금 크게 |

- 노랑은 중요한 것(국민연금을 5년 당기는 것), 빨강은 나쁜 상황(77세부터 손해와 손해를 만드는 조기수령)에 쓴다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 55% of the width): a Korean man aged 57 who looks youthful for his age, like his early 50s (short neat black hair with a little gray at the temples, dark gray knit cardigan over a white T-shirt), sitting at the dining table of his apartment living room at night, shown from the chest up and large in the frame. He has just realized how much pension money he will lose, and he is crushed: one hand pressed against his forehead, head bowed, eyes squeezed shut, brows knitted, shoulders slumped — clear frustration, regret and despair that read even at small thumbnail size. Keep most of his face visible (the hand must not cover his eyes and mouth completely). Realistic, not cartoonish, not exaggerated. On the table only an empty tea cup and one blank white sheet of paper with nothing printed on it. Fictional person, not resembling any real or famous person.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "조기수령" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the man.
- Background: an apartment living room at night with blurred city lights through the window, cool blue tones; warm pendant-lamp light only on the man's face.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "50대 국민연금 5년 당기면" — "50대" in white and "국민연금 5년 당기면" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 90% of the image width, but keep it at least 4% away from the right edge);
line 2 "77세부터 손해" — all in bright red #FF2A2A with a thick white outline, slightly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the man and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No money, no bills, no coins, no documents with writing, no phones, no calendars, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집 프로그램으로)
```
YouTube thumbnail background, 16:9 landscape (1280x720), photorealistic, high contrast.
Upper 62%: on the right, a Korean man aged 57 who looks like his early 50s (short black hair with a little gray at the temples, dark gray knit cardigan over a white T-shirt) at his living-room dining table at night, chest up and large in the frame, one hand pressed against his forehead, head bowed, eyes squeezed shut, brows knitted in frustration and regret, shoulders slumped (most of the face visible). An empty tea cup and one blank white sheet on the table. Fictional person, not resembling any real or famous person. On the left, one empty solid bright red rounded box with two thick red arrows pointing down toward the man. Background: apartment at night, blurred city lights, cool blue tones, warm pendant light on his face.
Lower third: a dark band fading upward from the bottom edge, left empty for a two-line headline.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
- 글자 얹기 (캔바·미리캔버스 등):
  - 빨강 상자 안: 조기수령 (흰색, 굵은 고딕)
  - 하단 2줄: Noto Sans KR Black(또는 Pretendard Black), 1줄 약 96px (x 48~약 1,084) · 2줄 약 112px (x 48~약 725 — 가로 80% = 1,024 앞), 색은 위 '문구' 표대로

## 검수
- [ ] 글자가 한 글자도 틀리지 않았는가: 조기수령 · 50대 국민연금 5년 당기면 · 77세부터 손해 ('령'의 ㅕ·ㅇ, '당기면'의 ㅇ 받침, '손해'의 ㄴ 받침까지 확대해서)
- [ ] '국민연금 5년 당기면'만 노랑, '77세부터 손해'만 빨강인가 · '50대'가 흰색으로 맨 앞에 있는가
- [ ] **좌절로 보이는가** — 고개를 떨구고 이마를 짚은 얼굴 (놀라 굳은 얼굴·고민하는 얼굴 아님), 가로 240px 로 줄여도
- [ ] 가로 320px로 줄여도 2줄과 '조기수령'이 읽히는가
- [ ] 얼굴과 글자가 가운데 16:9 안에 있는가 · 오른쪽 아래 구석이 비어 있는가
- [ ] 실존 인물을 닮지 않았는가 · 종이·벽에 글자·로고가 없는가 · 공단 로고·지폐가 없는가

## 이미지 검수 (Claude — 지시사항 10번)

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
