# gungmin-sigi-2026-10 썸네일 2 — 실험안 ①: 본안과 같은 장면, 낱말만 '조기수령'

버전: v2.0 — 2026-10-19 — 대본 v2.1(사연형 — 각색 인물 김 씨)·`titles.md` v2.0 R1 기준으로 다시. `guides/thumbnail_guide.md` v3.14. 근거: `README.md`. 옛 v1.0 은 git 이력.

| 항목 | 값 |
|---|---|
| 역할 | 실험안 ① — 공개 뒤 '테스트 및 비교' |
| 시험하는 가설 | 그림 낱말을 방법 낱말 '조기수령'으로 바꾸면(무엇을 신청했는지 썸네일이 말하면) 검색 낱말과 맞아 클릭이 느는가, 호기심이 줄어 덜 누르는가 (본안과 낱말 한 가지만 다름) |
| 짝 제목 | titles.md v2.0 R1 「은퇴 후 국민연금 신청 한 번에 평생 손해봤어요. 꼭 보세요」 |
| 문구 | 제목 R1에서 당부 '꼭 보세요'를 빼고 나머지는 제목 글자 그대로 — 시청자층 '은퇴 후'는 흰색 맨 앞 (`README.md` 2번) |
| 근거 (`README.md` 3번) | 노후·연금·절세 묶음: 걱정 표정 23% vs 7% · 실사 인물 성공 배수 상위 16개 중 56% · 빨강 글자 48% vs 32% · 손해 낱말 43% vs 18% (v1.0 과 같은 자료) |
| 그림 낱말 | '조기수령' — 댓글 '국민연금 + 받는 시기' 119개에서 가장 많이 쓴 낱말 (v1.0 3-3) |
| 숫자 근거 | '평생' = 5년 당긴 30% 감액이 평생(국민연금법 제61조②·제63조②, 대본 문장 15·19~22) · '30% 깎임' = 1년 6% × 5년 (문장 15) |
| 인물 나이 | 본안과 같은 인물·장면 |
| 저장 경로 | `economic/source/gungmin-sigi-2026-10/thumbnails/thumbnail_2.png` |

## 화면 구성
- 본안(`thumbnail_1.md`)과 **같은 인물·옷·곳·몸짓·빛**. 다른 것은 왼쪽 빨강 꼬리표의 낱말 하나 — '조기수령'.

## 문구 (그대로 사용)
| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 은퇴 후 국민연금 신청 한 번에 | '은퇴 후' 흰색 · **'국민연금 신청 한 번에' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 평생 손해봤어요 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 크게 |

- 노랑은 중요한 것(국민연금 신청 한 번), 빨강은 나쁜 상황(평생 손해 · 조기수령)에 쓴다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 55% of the width): a Korean man aged 60 who looks youthful for his age, like his mid-50s (short neat black hair with gray at the temples, navy cotton shirt with the sleeves rolled up), sitting on the edge of a sofa in his living room at night, shown from the chest up and large in the frame. In his lower hand he holds an open blank bank passbook with nothing printed on it. He has just found out that his early pension cut lasts for the rest of his life, and he is crushed: one hand pressed against his forehead, head bowed, eyes squeezed shut, brows knitted, shoulders slumped — clear frustration, regret and despair that read even at small thumbnail size. Keep most of his face visible (the hand must not cover his eyes and mouth completely). Realistic, not cartoonish, not exaggerated. Fictional person, not resembling any real or famous person.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "조기수령" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the man.
- Background: a modest apartment living room at night, a sofa and a floor lamp, blurred window lights, cool blue tones; warm lamp light only on the man's face.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "은퇴 후 국민연금 신청 한 번에" — "은퇴 후" in white and "국민연금 신청 한 번에" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 88% of the image width, but keep it at least 4% away from the right edge);
line 2 "평생 손해봤어요" — all in bright red #FF2A2A with a thick white outline, clearly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the man and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No money, no bills, no coins, no documents with writing, no phones, no calendars, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집 프로그램으로)
```
YouTube thumbnail background, 16:9 landscape (1280x720), photorealistic, high contrast.
Upper 62%: on the right, a Korean man aged 60 who looks youthful for his age, like his mid-50s (short neat black hair with gray at the temples, navy cotton shirt with the sleeves rolled up), on the edge of a sofa at night, chest up and large in the frame, holding an open blank passbook in his lower hand, the other hand pressed against his forehead, head bowed, eyes squeezed shut, brows knitted in frustration and regret, shoulders slumped (most of the face visible). Fictional person, not resembling any real or famous person. On the left, one empty solid bright red rounded box with two thick red arrows pointing down toward the man. Background: modest apartment living room at night, sofa and floor lamp, blurred window lights, cool blue tones, warm lamp light on his face.
Lower third: a dark band fading upward from the bottom edge, left empty for a two-line headline.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
- 글자 얹기 (캔바·미리캔버스 등):
  - 빨강 상자 안: 조기수령 (흰색, 굵은 고딕)
  - 하단 2줄: Noto Sans KR Black(또는 Pretendard Black), 1줄 약 88px (x 48~약 1,120) · 2줄 약 120px (x 48~약 848 — 가로 80% = 1,024 앞), 색은 위 '문구' 표대로

## 검수
- [ ] 글자가 한 글자도 틀리지 않았는가: 조기수령 · 은퇴 후 국민연금 신청 한 번에 · 평생 손해봤어요 ('퇴'의 ㅚ, '번에'의 ㄴ 받침, '봤어요'의 ㅘ·ㅆ 받침까지 확대해서)
- [ ] '국민연금 신청 한 번에'만 노랑, '평생 손해봤어요'만 빨강인가 · '은퇴 후'가 흰색으로 맨 앞에 있는가
- [ ] **좌절로 보이는가** — 고개를 떨구고 이마를 짚은 얼굴 (놀라 굳은 얼굴·고민하는 얼굴 아님), 가로 240px 로 줄여도
- [ ] 가로 320px로 줄여도 2줄과 그림 낱말이 읽히는가
- [ ] 얼굴(또는 통장)과 글자가 가운데 16:9 안에 있는가 · 2줄째가 가로 80% 앞에서 끝나고 오른쪽 아래 구석이 비어 있는가
- [ ] 실존 인물을 닮지 않았는가 · 통장·벽에 글자·로고가 없는가 · 공단 로고·지폐가 없는가

## 이미지 검수 (Claude — 지시사항 10번)

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
