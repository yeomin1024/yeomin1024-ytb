# economic 썸네일 4장 — ChatGPT용 (모든 영상 · 읽고 그대로 만들고 각 저장 경로에 올리기)

자동 생성 — `python tools/make_summary.py --chatgpt-all economic` (2026-10-19 13:21). 이 파일은 고치지 말고 영상마다 `thumbnail_N.md`를 고친 뒤 다시 만든다.

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/economic/thumbnails_chatgpt.md

| 영상 | 만들 시안 | 저장 폴더 |
|---|---|---|
| gungmin-sigi-2026-10 | thumbnail_1, thumbnail_2, thumbnail_3 | `economic/source/gungmin-sigi-2026-10/thumbnails/` |
| gungmin-sigi-2026-10-shorts | thumbnail_1 | `economic/source/gungmin-sigi-2026-10/shorts/thumbnails/` |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 썸네일 파일·프롬프트가 있어도 쓰지 않는다 (2026-10-17 옛 프롬프트로 4장을 다시 그린 일이 있었음). 답의 첫 줄에 이 파일 맨 위 '자동 생성' 줄의 시각을 그대로 적는다 (Claude 가 어느 판으로 그렸는지 확인).
1. 아래 썸네일 4장(2개 영상)을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다. 장마다 서로 다른 그림이다 — 앞 장의 인물·구도·색을 이어 쓰지 않는다.
3. 크기는 **장마다 '크기' 줄대로**: 롱폼 썸네일 = 가로형 16:9 (1280×720 — 안 되면 가장 넓은 가로형, 그림은 끝까지, 글자와 얼굴은 가운데, 위아래 8%에는 두지 않음) · **쇼츠 썸네일(영상 ID 끝이 `-shorts`) = 세로형 9:16 (1080×1920)** — 배치는 장마다 '크기' 줄대로 ('세 칸'이면 **세 칸 배치** — 위 0~36% 는 평평한 순검정(#000000)에 문구 2줄만, 가운데 36~72% 는 사진 한 장(가로 끝까지, 위아래 경계는 곧은 가로선), 아래 72~100% 는 순검정 빈 칸. 칸 사이 그라데이션·사진 테두리 없음. 문구 2줄은 줄마다 가운데 정렬(두 줄 가운데 축이 같음)·최대 크기, 사진과 붙거나 겹치지 않는다. **글자·얼굴·꼬리표는 높이 15~85% 안** (일부 피드가 쇼츠 썸네일을 4:5 로 잘라 위아래 약 15%씩 안 보임), 그 밖은 **사진 한 장이 네 가장자리까지 꽉 찬다 — 빈 남색·검정 띠, 테두리, 여백, 가운데만 사진인 꼴은 안 된다** (v1.8.0 — 띠가 있으면 영상에서 비율이 틀린 것처럼 보임). 프롬프트가 '글자·얼굴을 두지 않는 자리'(위·오른쪽·아래)를 말해도 그 자리에도 사진(배경·앞쪽 물건)이 이어진다). 안 되면 세로 2:3, 그때는 글자와 얼굴을 가운데에 두고 2:3 그림의 양옆 8%에는 두지 않음 (잘리는 자리 — 사진은 이어짐).
4. 그림 속 글자는 프롬프트의 따옴표 안 글자만(한글, 그리고 프롬프트가 적은 영문 — 예: ISA), 글자·띄어쓰기·조사 그대로 쓴다 (조사 하나도 빼거나 바꾸지 않는다 — '세금으로'를 '세금'으로 줄이면 뜻이 달라짐). **줄 수·줄바꿈·정렬·글자 크기도 프롬프트대로** — 프롬프트가 '2줄, 줄마다 가운데, 긴 줄이 너비 4~96%'라고 하면 그만큼 크게·가운데로, 작게 줄이거나 한쪽으로 몰지 않는다 (v1.8.4·v1.9.0). 다른 글자·숫자·로고·워터마크는 넣지 않는다.
5. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다. **표정·몸짓은 프롬프트에 적힌 그대로** — 손해를 알고 좌절한 장면을 놀란 얼굴·담담한 얼굴·웃는 얼굴로 바꾸지 않고, 작은 화면에서도 그 감정이 보이게 그린다 (v1.8.3).
6. 한 장을 만들 때마다 그 칸의 '문구' 표와 그림 속 한글을 한 글자씩 맞춰 본다. 크게 확대해서 받침과 모음 획(예: '료'의 ㄹ, '보'의 ㅗ)·조사(예: '1년에'의 '에', '세금으로'의 '으로')가 빠지거나 가려지지 않았는지도 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다. 쇼츠 그림(세로)은 **그 장의 배치대로인지**도 본다 — '세 칸'이면 위·아래 칸이 순검정·사진 칸이 가로 끝까지·문구 2줄이 줄마다 가운데(어긋남 없음)·사진과 붙지 않음·글자와 얼굴이 높이 15~85% 안, 그 밖(사진 끝까지)이면 빈 남색·검정 띠가 없는지. 다르면 다시 만든다 (v1.8.0·v1.9.0).
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `3. economic/source/gungmin-sigi-2026-10/thumbnails/thumbnail_3.png`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게 (`thumbnail_N.png`).
   - GitHub 에 쓸 수 있으면(쓰기 권한이 있는 GitHub 앱) 장마다 그 경로에 커밋한다. 커밋 메시지: `[썸네일] <영상ID> thumbnail_N 이미지`
   - **쓸 수 없으면 (이 계정의 ChatGPT 는 GitHub 를 읽기만 함 — 2026-10-15 확인)** 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 이 파일의 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"이 그림 4장을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 thumbnail_N.png 이름으로 내려받아 폴더마다 아래 링크에 끌어다 놓고 Commit changes" + 아래 '폴더별 올리기 링크' 목록

## 폴더별 올리기 링크 (ChatGPT가 못 올릴 때 사람이 쓰는 길)

- gungmin-sigi-2026-10: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/gungmin-sigi-2026-10/thumbnails
- gungmin-sigi-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/gungmin-sigi-2026-10/shorts/thumbnails

## 1. gungmin-sigi-2026-10 · thumbnail_1 — 본안(클릭률 최대): 밤 거실 소파에서 빈 통장을 들고 이마를 짚은 60세 남성 + '30% 깎임' 낱말

**저장 경로: `economic/source/gungmin-sigi-2026-10/thumbnails/thumbnail_1.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 30% 깎임 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 은퇴 후 국민연금 신청 한 번에 | '은퇴 후' 흰색 · **'국민연금 신청 한 번에' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 평생 손해봤어요 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 크게 |

- 노랑은 중요한 것(국민연금 신청 한 번), 빨강은 나쁜 상황(평생 손해 · 30% 깎임)에 쓴다.

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 55% of the width): a Korean man aged 60 who looks youthful for his age, like his mid-50s (short neat black hair with gray at the temples, navy cotton shirt with the sleeves rolled up), sitting on the edge of a sofa in his living room at night, shown from the chest up and large in the frame. In his lower hand he holds an open blank bank passbook with nothing printed on it. He has just found out that his early pension cut lasts for the rest of his life, and he is crushed: one hand pressed against his forehead, head bowed, eyes squeezed shut, brows knitted, shoulders slumped — clear frustration, regret and despair that read even at small thumbnail size. Keep most of his face visible (the hand must not cover his eyes and mouth completely). Realistic, not cartoonish, not exaggerated. Fictional person, not resembling any real or famous person.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "30% 깎임" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the man.
- Background: a modest apartment living room at night, a sofa and a floor lamp, blurred window lights, cool blue tones; warm lamp light only on the man's face.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "은퇴 후 국민연금 신청 한 번에" — "은퇴 후" in white and "국민연금 신청 한 번에" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 88% of the image width, but keep it at least 4% away from the right edge);
line 2 "평생 손해봤어요" — all in bright red #FF2A2A with a thick white outline, clearly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the man and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No money, no bills, no coins, no documents with writing, no phones, no calendars, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 2. gungmin-sigi-2026-10 · thumbnail_2 — 실험안 ①: 본안과 같은 장면, 낱말만 '조기수령'

**저장 경로: `economic/source/gungmin-sigi-2026-10/thumbnails/thumbnail_2.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 은퇴 후 국민연금 신청 한 번에 | '은퇴 후' 흰색 · **'국민연금 신청 한 번에' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 평생 손해봤어요 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 크게 |

- 노랑은 중요한 것(국민연금 신청 한 번), 빨강은 나쁜 상황(평생 손해 · 조기수령)에 쓴다.

프롬프트:

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

## 3. gungmin-sigi-2026-10 · thumbnail_3 — 실험안 ②: 사람 없이, 오른쪽 3분의 1이 잘려 나간 빈 통장 + '30% 깎임' 낱말

**저장 경로: `economic/source/gungmin-sigi-2026-10/thumbnails/thumbnail_3.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 30% 깎임 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 은퇴 후 국민연금 신청 한 번에 | '은퇴 후' 흰색 · **'국민연금 신청 한 번에' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 평생 손해봤어요 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 크게 |

- 노랑은 중요한 것(국민연금 신청 한 번), 빨강은 나쁜 상황(평생 손해 · 30% 깎임)에 쓴다.

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Center-right (about 55% of the width): close-up still life on a dark wooden coffee table at night — an open blank bank passbook with nothing printed on it, its right third cut away with a ragged edge, the cut piece lying a little apart, a pair of scissors beside it and a single desk lamp casting a hard warm light on it. No hands, no people.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "30% 깎임" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag toward the cut-away piece of the passbook.
- Background: a dark living room at night, blurred and out of focus, cool blue tones.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "은퇴 후 국민연금 신청 한 번에" — "은퇴 후" in white and "국민연금 신청 한 번에" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 88% of the image width, but keep it at least 4% away from the right edge);
line 2 "평생 손해봤어요" — all in bright red #FF2A2A with a thick white outline, clearly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the passbook and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No money, no bills, no coins, no documents with writing, no phones, no calendars, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 4. gungmin-sigi-2026-10-shorts · thumbnail_1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 동창 모임 식당에서 친구의 말을 듣고 두 손으로 머리를 감싸 쥔 60세 김 씨 + '평생 30%' 꼬리표

**저장 경로: `economic/source/gungmin-sigi-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠 · 세 칸 (위 0~36% 순검정 + 문구 2줄 · 가운데 36~72% 사진 · 아래 72~100% 순검정, 글자·얼굴은 높이 15~85%)**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 평생 30% | 흰 평면 글자 on 빨강 말풍선 #FF2A2A |
| 위 1줄 | 국민연금 신청서 한 장에 | **'국민연금' 노랑 #FFD400** · '신청서 한 장에' 흰색 — 두꺼운 검정 외곽선 없이 검정 바탕 위 평면 글자 |
| 위 2줄 | 평생 매달 27만 원 덜 받는다 | **전부 빨강 #FF2A2A** (나쁜 상황) — 1줄과 같은 크기 |

프롬프트:

```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), high contrast. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
LAYOUT — three full-width zones: 0–36% of the height flat solid pure black (#000000) with only the headline; 36–72% one photorealistic photograph edge to edge with straight top and bottom edges; 72–100% flat solid pure black, empty. No gradient, fade or border.
SAFE AREA: some feeds crop to about 4:5 — all text, faces and word tags stay between 15% and 85% of the height.
Headline: exactly TWO lines of very large heavy bold Korean text, same size, EACH LINE CENTERED on the same axis, the longer line from about 4% to 96% of the width, the block between about 19% and 32% of the height and at least 3% above the photo; flat letters, no glow, no 3D.
line 1 "국민연금 신청서 한 장에" — "국민연금" in bright yellow #FFD400 and "신청서 한 장에" in white;
line 2 "평생 매달 27만 원 덜 받는다" — all in bright red #FF2A2A.
Photo zone: a warm, softly lit Korean restaurant in the evening, a reunion dinner of old classmates with blurred friends in the background. At the table sits a Korean man aged 60 who looks youthful for his age, like his mid-50s (short black hair with gray at the temples, beige knit sweater), shown from the chest up, centered slightly right (about 30–82% of the width). A friend has just told him his early pension cut lasts for life, and he is crushed: both hands clutching his head, head bowed, eyes squeezed shut, brows knitted — clear frustration, regret and despair that read even at small size. Keep most of his face visible (hands must not cover his eyes and mouth completely). Realistic, not cartoonish. On the table only small soju glasses and side dishes with no labels. Fictional person, not resembling any real or famous person.
On the left of the photo (about 7–28% of the width, 40–56% of the height): one speech-bubble tag, a solid bright red (#FF2A2A) rounded box with the Korean text "평생 30%" printed in large flat heavy bold white letters on its flat front face (flat print, not carved or 3D), its tail pointing from a blurred friend toward the man. Keep the right 16% of the width below 45% of the height free of faces and tags (Shorts buttons).
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536) with the same zones and keep the headline between 12% and 88% of the width.
No money, no bills, no documents with writing, no phones, no logos of any institution or restaurant.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
