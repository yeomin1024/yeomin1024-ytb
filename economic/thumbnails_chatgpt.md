# economic 썸네일 8장 — ChatGPT용 (모든 영상 · 읽고 그대로 만들고 각 저장 경로에 올리기)

자동 생성 — `python tools/make_summary.py --chatgpt-all economic` (2026-10-18 05:18). 이 파일은 고치지 말고 영상마다 `thumbnail_N.md`를 고친 뒤 다시 만든다.

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/economic/thumbnails_chatgpt.md

| 영상 | 만들 시안 | 저장 폴더 |
|---|---|---|
| geumyung-soduk-2026-10 | thumbnail_1, thumbnail_2, thumbnail_3 | `economic/source/geumyung-soduk-2026-10/thumbnails/` |
| gungmin-sigi-2026-10 | thumbnail_1, thumbnail_2, thumbnail_3 | `economic/source/gungmin-sigi-2026-10/thumbnails/` |
| geumyung-soduk-2026-10-shorts | thumbnail_1 | `economic/source/geumyung-soduk-2026-10/shorts/thumbnails/` |
| gungmin-sigi-2026-10-shorts | thumbnail_1 | `economic/source/gungmin-sigi-2026-10/shorts/thumbnails/` |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 썸네일 파일·프롬프트가 있어도 쓰지 않는다 (2026-10-17 옛 프롬프트로 4장을 다시 그린 일이 있었음). 답의 첫 줄에 이 파일 맨 위 '자동 생성' 줄의 시각을 그대로 적는다 (Claude 가 어느 판으로 그렸는지 확인).
1. 아래 썸네일 8장(4개 영상)을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다. 장마다 서로 다른 그림이다 — 앞 장의 인물·구도·색을 이어 쓰지 않는다.
3. 크기는 **장마다 '크기' 줄대로**: 롱폼 썸네일 = 가로형 16:9 (1280×720 — 안 되면 가장 넓은 가로형, 그림은 끝까지, 글자와 얼굴은 가운데, 위아래 8%에는 두지 않음) · **쇼츠 썸네일(영상 ID 끝이 `-shorts`) = 세로형 9:16 (1080×1920)** — 배치는 장마다 '크기' 줄대로 ('세 칸'이면 **세 칸 배치** — 위 0~36% 는 평평한 순검정(#000000)에 문구 2줄만, 가운데 36~72% 는 사진 한 장(가로 끝까지, 위아래 경계는 곧은 가로선), 아래 72~100% 는 순검정 빈 칸. 칸 사이 그라데이션·사진 테두리 없음. 문구 2줄은 줄마다 가운데 정렬(두 줄 가운데 축이 같음)·최대 크기, 사진과 붙거나 겹치지 않는다. **글자·얼굴·꼬리표는 높이 15~85% 안** (일부 피드가 쇼츠 썸네일을 4:5 로 잘라 위아래 약 15%씩 안 보임), 그 밖은 **사진 한 장이 네 가장자리까지 꽉 찬다 — 빈 남색·검정 띠, 테두리, 여백, 가운데만 사진인 꼴은 안 된다** (v1.8.0 — 띠가 있으면 영상에서 비율이 틀린 것처럼 보임). 프롬프트가 '글자·얼굴을 두지 않는 자리'(위·오른쪽·아래)를 말해도 그 자리에도 사진(배경·앞쪽 물건)이 이어진다). 안 되면 세로 2:3, 그때는 글자와 얼굴을 가운데에 두고 2:3 그림의 양옆 8%에는 두지 않음 (잘리는 자리 — 사진은 이어짐).
4. 그림 속 글자는 프롬프트의 따옴표 안 글자만(한글, 그리고 프롬프트가 적은 영문 — 예: ISA), 글자·띄어쓰기·조사 그대로 쓴다 (조사 하나도 빼거나 바꾸지 않는다 — '세금으로'를 '세금'으로 줄이면 뜻이 달라짐). **줄 수·줄바꿈·정렬·글자 크기도 프롬프트대로** — 프롬프트가 '2줄, 줄마다 가운데, 긴 줄이 너비 4~96%'라고 하면 그만큼 크게·가운데로, 작게 줄이거나 한쪽으로 몰지 않는다 (v1.8.4·v1.9.0). 다른 글자·숫자·로고·워터마크는 넣지 않는다.
5. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다. **표정·몸짓은 프롬프트에 적힌 그대로** — 손해를 알고 좌절한 장면을 놀란 얼굴·담담한 얼굴·웃는 얼굴로 바꾸지 않고, 작은 화면에서도 그 감정이 보이게 그린다 (v1.8.3).
6. 한 장을 만들 때마다 그 칸의 '문구' 표와 그림 속 한글을 한 글자씩 맞춰 본다. 크게 확대해서 받침과 모음 획(예: '료'의 ㄹ, '보'의 ㅗ)·조사(예: '1년에'의 '에', '세금으로'의 '으로')가 빠지거나 가려지지 않았는지도 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다. 쇼츠 그림(세로)은 **그 장의 배치대로인지**도 본다 — '세 칸'이면 위·아래 칸이 순검정·사진 칸이 가로 끝까지·문구 2줄이 줄마다 가운데(어긋남 없음)·사진과 붙지 않음·글자와 얼굴이 높이 15~85% 안, 그 밖(사진 끝까지)이면 빈 남색·검정 띠가 없는지. 다르면 다시 만든다 (v1.8.0·v1.9.0).
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `3. economic/source/geumyung-soduk-2026-10/thumbnails/thumbnail_3.png`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게 (`thumbnail_N.png`).
   - GitHub 에 쓸 수 있으면(쓰기 권한이 있는 GitHub 앱) 장마다 그 경로에 커밋한다. 커밋 메시지: `[썸네일] <영상ID> thumbnail_N 이미지`
   - **쓸 수 없으면 (이 계정의 ChatGPT 는 GitHub 를 읽기만 함 — 2026-10-15 확인)** 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 이 파일의 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"이 그림 8장을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 thumbnail_N.png 이름으로 내려받아 폴더마다 아래 링크에 끌어다 놓고 Commit changes" + 아래 '폴더별 올리기 링크' 목록

## 폴더별 올리기 링크 (ChatGPT가 못 올릴 때 사람이 쓰는 길)

- geumyung-soduk-2026-10: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/geumyung-soduk-2026-10/thumbnails
- gungmin-sigi-2026-10: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/gungmin-sigi-2026-10/thumbnails
- geumyung-soduk-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/geumyung-soduk-2026-10/shorts/thumbnails
- gungmin-sigi-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/gungmin-sigi-2026-10/shorts/thumbnails

## 1. geumyung-soduk-2026-10 · thumbnail_1 — 본안(클릭률 최대): 늦은 오후 부엌 식탁에서 휴대폰을 보다 좌절한 58세 부부 + '건보료' 낱말

**저장 경로: `economic/source/geumyung-soduk-2026-10/thumbnails/thumbnail_1.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 건보료 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50·60대 배당·이자 한 사람이 받으면 | '50·60대' 흰색 · **'배당·이자 한 사람이 받으면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 건보료 월 26만 원 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

- 노랑은 중요한 것(손해를 부르는 조건 — 배당·이자를 한 사람이 받음), 빨강은 나쁜 상황(건보료 손해와 손해를 만드는 건보료 꼬리표)에 쓴다.

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 58% of the width): a Korean married couple aged 58 who look youthful for their age, like their mid 50s, sitting side by side at their home kitchen table in warm late-afternoon window light, shown from the chest up and large in the frame. The husband (on the right; short neat black hair with a little gray at the temples, gray short-sleeve knit polo shirt) limply holds a smartphone in one hand with its screen facing away from the viewer (the screen only glows, no text), head bowed, eyes squeezed shut, brows knitted in pain, jaw clenched, shoulders slumped: he has just realized how much money they are losing, crushed with frustration and regret. The wife (just to his left and slightly behind; shoulder-length dark brown hair, cream blouse) covers her mouth with one hand and looks down toward his phone, devastated, inner brows raised, eyes teary. Their faces stay clearly visible (only the wife's mouth is covered). The despair must read clearly even at small thumbnail size, but stay realistic, not cartoonish, not exaggerated. Fictional people, not resembling any real or famous person.
- Left side (about 42% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "건보료" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the couple.
- Background: a cozy apartment kitchen softly blurred (sink, window), warm golden late-afternoon light; two plain mugs on the table with no text.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 배당·이자 한 사람이 받으면" — "50·60대" in white and "배당·이자 한 사람이 받으면" in bright yellow #FFD400, all with a thick black outline (keep both middle dots "·" — between 50 and 60, and between 배당 and 이자 — line 1 is the longer line: it may run to about 92% of the image width, but keep it at least 4% away from the right edge);
line 2 "건보료 월 26만 원 손해" — all in bright red #FF2A2A with a thick white outline.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the couple and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No bank, brokerage or government logos, no app screens, no charts, no account books, no piggy banks, no real banknote designs.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 2. geumyung-soduk-2026-10 · thumbnail_2 — 실험안 ①: 같은 부엌 장면, 휴대폰을 보다 좌절한 남편 한 사람 + '건보료' 낱말

**저장 경로: `economic/source/geumyung-soduk-2026-10/thumbnails/thumbnail_2.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 건보료 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50·60대 배당·이자 한 사람이 받으면 | '50·60대' 흰색 · **'배당·이자 한 사람이 받으면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 건보료 월 26만 원 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 58% of the width): a Korean man aged 58 who looks youthful for his age, like his mid 50s (short neat black hair with a little gray at the temples, gray short-sleeve knit polo shirt), sitting alone at his home kitchen table in warm late-afternoon window light, shown from the chest up and very large in the frame. He limply holds a smartphone in one hand with its screen facing away from the viewer (the screen only glows, no text) and grips the back of his neck with the other hand, head bowed, eyes squeezed shut, brows knitted in pain, jaw clenched, shoulders slumped: he has just realized how much money he and his wife are losing, crushed with frustration and regret. His face stays clearly visible, not covered by his hands. The despair must read clearly even at small thumbnail size, but stay realistic, not cartoonish, not exaggerated. Fictional person, not resembling any real or famous person.
- Left side (about 42% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "건보료" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the man.
- Background: a cozy apartment kitchen softly blurred (sink, window), warm golden late-afternoon light; one plain mug on the table with no text.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 배당·이자 한 사람이 받으면" — "50·60대" in white and "배당·이자 한 사람이 받으면" in bright yellow #FFD400, all with a thick black outline (keep both middle dots "·" — between 50 and 60, and between 배당 and 이자 — line 1 is the longer line: it may run to about 92% of the image width, but keep it at least 4% away from the right edge);
line 2 "건보료 월 26만 원 손해" — all in bright red #FF2A2A with a thick white outline.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the man and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and the face inside the central 16:9 area, at least 8% away from the top and bottom edges.
No bank, brokerage or government logos, no app screens, no charts, no account books, no piggy banks, no real banknote designs.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 3. geumyung-soduk-2026-10 · thumbnail_3 — 실험안 ②: 사람 없이, 식탁 위 지폐 더미를 짓누르는 빨강 '건보료' 덩어리

**저장 경로: `economic/source/geumyung-soduk-2026-10/thumbnails/thumbnail_3.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 건보료 | 흰 글자 on 빨강 덩어리 앞면 #FF2A2A |
| 하단 1줄 | 50·60대 배당·이자 한 사람이 받으면 | '50·60대' 흰색 · **'배당·이자 한 사람이 받으면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 건보료 월 26만 원 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size. No people.
Upper 62% of the frame:
- Center to right: on a wooden kitchen table in warm late-afternoon window light, one neat bundled stack of plain generic banknotes with no portraits and no numbers. A heavy solid bright red (#FF2A2A) block presses down on the stack from above, crushing it so the stack bends and a few loose plain bills scatter on the table. On the flat front face of the red block, the Korean word "건보료" is printed in huge flat heavy bold white letters (flat print, not carved or 3D letter shapes), facing the viewer and fully visible.
- Upper left: two thick bright red arrows pointing down onto the red block.
- Background: a cozy apartment kitchen softly blurred (sink, window), warm golden late-afternoon light; two plain mugs at the far end of the table with no text.
- Only ONE stack of money (do not split it into two piles).
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 배당·이자 한 사람이 받으면" — "50·60대" in white and "배당·이자 한 사람이 받으면" in bright yellow #FFD400, all with a thick black outline (keep both middle dots "·" — between 50 and 60, and between 배당 and 이자 — line 1 is the longer line: it may run to about 92% of the image width, but keep it at least 4% away from the right edge);
line 2 "건보료 월 26만 원 손해" — all in bright red #FF2A2A with a thick white outline.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the money and the red block in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and the red block inside the central 16:9 area, at least 8% away from the top and bottom edges.
No bank, brokerage or government logos, no app screens, no charts, no account books, no piggy banks, no real banknote designs.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 4. gungmin-sigi-2026-10 · thumbnail_1 — 본안(클릭률 최대): 밤 식탁에서 이마를 짚고 고개를 떨군 57세 남성 + '조기수령' 낱말

**저장 경로: `economic/source/gungmin-sigi-2026-10/thumbnails/thumbnail_1.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50대 국민연금 5년 당기면 | '50대' 흰색 · **'국민연금 5년 당기면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 77세부터 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 조금 크게 |

- 노랑은 중요한 것(국민연금을 5년 당기는 것), 빨강은 나쁜 상황(77세부터 손해와 손해를 만드는 조기수령)에 쓴다.

프롬프트:

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

## 5. gungmin-sigi-2026-10 · thumbnail_2 — 실험안 ①: 같은 장면, 좌절한 남편 + 어깨에 손을 얹은 아내 (부부)

**저장 경로: `economic/source/gungmin-sigi-2026-10/thumbnails/thumbnail_2.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50대 국민연금 5년 당기면 | '50대' 흰색 · **'국민연금 5년 당기면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 77세부터 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 조금 크게 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 60% of the width): a Korean married couple, both aged 57 but looking youthful, like their early 50s, at the dining table of their apartment living room at night, shown from the chest up and large in the frame. The husband (short neat black hair with a little gray at the temples, dark gray knit cardigan over a white T-shirt) has just realized how much pension money they will lose and is crushed: one hand pressed against his forehead, head bowed, eyes squeezed shut, brows knitted, shoulders slumped. The wife beside him on the right (shoulder-length dark hair, light beige blouse) rests one hand on his shoulder and covers her mouth with the other, looking down at him with worry and regret. Both faces stay visible. Clear frustration and despair that read even at small thumbnail size; realistic, not cartoonish. On the table only an empty tea cup and one blank white sheet of paper with nothing printed on it. Fictional people, not resembling any real or famous person.
- Left side (about 40% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "조기수령" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the couple.
- Background: an apartment living room at night with blurred city lights through the window, cool blue tones; warm pendant-lamp light only on their faces.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "50대 국민연금 5년 당기면" — "50대" in white and "국민연금 5년 당기면" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 90% of the image width, but keep it at least 4% away from the right edge);
line 2 "77세부터 손해" — all in bright red #FF2A2A with a thick white outline, slightly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the couple and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No money, no bills, no coins, no documents with writing, no phones, no calendars, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 6. gungmin-sigi-2026-10 · thumbnail_3 — 실험안 ②: 사람 없이, 동전이 새는 모래시계 + '조기수령' 낱말

**저장 경로: `economic/source/gungmin-sigi-2026-10/thumbnails/thumbnail_3.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50대 국민연금 5년 당기면 | '50대' 흰색 · **'국민연금 5년 당기면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 77세부터 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 조금 크게 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size. No people.
Upper 62% of the frame:
- Right side (about 55% of the width): one large glass hourglass standing on a dark wooden dining table at night, fully inside the upper 62% of the frame. Instead of sand, small plain gold coins with no numbers, letters, portraits or patterns fall in a thin stream from the upper bulb into the lower bulb; the glass at the bottom of the lower bulb is cracked, and a few plain gold coins have leaked out and lie scattered on the table. Warm light only on the hourglass.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "조기수령" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes), standing upright and leaning against the hourglass. Two thick bright red arrows point from the tag down toward the leaking coins.
- Background: an apartment living room at night with blurred city lights through the window, cool blue tones.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "50대 국민연금 5년 당기면" — "50대" in white and "국민연금 5년 당기면" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 90% of the image width, but keep it at least 4% away from the right edge);
line 2 "77세부터 손해" — all in bright red #FF2A2A with a thick white outline, slightly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the hourglass and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and objects inside the central 16:9 area, at least 8% away from the top and bottom edges.
No banknotes, no documents, no phones, no calendars, no clocks with numbers, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 7. geumyung-soduk-2026-10-shorts · thumbnail_1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 밤 거실 소파에서 첫 건보료 고지서를 보고 좌절한 58세 정씨 부부 + '건보료' 낱말

**저장 경로: `economic/source/geumyung-soduk-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠 · 세 칸 (위 0~36% 순검정 + 문구 2줄 · 가운데 36~72% 사진 · 아래 72~100% 순검정, 글자·얼굴은 높이 15~85%)**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 (봉투 앞면) | 건보료 | 흰 평면 글자 on 빨강 띠 #FF2A2A |
| 위 1줄 | 배당으로 사는 부부 건보료로 | **'배당' 노랑 #FFD400** · '으로 사는 부부' 흰색 · **'건보료로' 노랑 #FFD400** — 검은 바탕, 가운데 정렬 |
| 위 2줄 | 1년에 320만 원 날린다 | **전부 빨강 #FF2A2A + 얇은 흰 외곽선**. 1줄과 같은 크기, 가운데 정렬 |

- 노랑은 중요한 것(주제 낱말 '배당'·니즈 낱말 '건보료로'), 빨강은 나쁜 상황(날리는 돈 — 2줄, 봉투 띠 '건보료')에만 쓴다.
- 두 줄이 따로 읽혀도 뜻이 같다: 1줄 '배당으로 사는 부부 건보료로' → 2줄 '1년에 320만 원 날린다' (무엇을 날리나? 내 돈 320만 원 · 무엇으로? 건보료로 — 피드백 21).

프롬프트:

```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
LAYOUT — three stacked zones, each spanning the full width of the canvas:
1. Top zone, from 0% to 36% of the height: flat solid pure black (#000000), with only the headline text on it.
2. Photo panel, from 36% to 72% of the height: one photorealistic photograph filling the full width edge to edge (a wide horizontal picture, about 3:2), with straight horizontal top and bottom edges.
3. Bottom zone, from 72% to 100% of the height: flat solid pure black (#000000), completely empty (a subtitle is added there later in the video).
No gradient or fade between the zones, no border or frame around the photo, no other bands or panels.
SAFE AREA: YouTube crops Shorts thumbnails to about 4:5 in some feeds on phones and PCs, cutting about 15% from the top and 15% from the bottom. Every important thing — all text, every face and word tag — must stay between 15% and 85% of the height.
Headline in the top black zone: exactly TWO lines of very large, heavy, bold Korean text, both lines the same letter size, EACH LINE CENTERED horizontally on the same center axis (the two lines must not be shifted left or right against each other). Make the letters as large as possible: the longer line (line 1) spans from about 4% to 96% of the width (each letter about 4.4% of the image height tall, roughly 84 px on a 1080x1920 canvas). Vertically, the two-line block is centered between the 15% line and the top of the photo — it sits between about 20% and 31% of the height — with a black gap of at least 3% of the height between the text and the photo. The text never touches or overlaps the photo. Flat letters on the black, no glow, no 3D, no shadow boxes:
line 1 "배당으로 사는 부부 건보료로" — "배당" in bright yellow #FFD400, "으로 사는 부부" in white, and "건보료로" in bright yellow #FFD400 (keep the last letter "로" of 건보료로);
line 2 "1년에 320만 원 날린다" — all in bright red #FF2A2A with a thin white outline.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536) with the same three zones (it will be center-cropped to 9:16, cutting about 8% from the left and right), and keep the headline between 12% and 88% of the width.
Scene inside the photo panel (from 36% to 72% of the height, full width), the living room of a Korean apartment at night, lit by one warm floor lamp, the window behind dark:
- Center-right (between about 42% and 80% of the width): a Korean man aged 58 who looks youthful for his age, like his mid 50s (short neat black hair with a little gray, navy knit sweater), shown from the chest up, leaning forward on the sofa. He holds an unfolded letter low in both hands with its blank back side toward the viewer and stares down at it, crushed: he has just realized how much money they are losing, brows knitted in pain, jaw clenched, shoulders slumped, eyes heavy with frustration and regret (face clearly visible, not covered by his hands). To his left (about 22% to 48% of the width), his wife aged 58 who looks like her mid 50s (shoulder-length dark hair, gray cardigan) rests one hand on his back and covers her mouth with the other, looking down at the letter, devastated, brows drawn up, eyes teary. The despair must read clearly even at small thumbnail size, but stay realistic, not cartoonish. Natural, realistic expressions, not exaggerated. Fictional people, not resembling any real or famous person.
- Lower left of the scene (between about 8% and 34% of the width, at about 56% to 66% of the height): on the low coffee table, an opened plain white envelope with its front facing the viewer. On the front there is one flat bright red (#FF2A2A) band with the Korean word "건보료" printed in huge flat heavy bold white letters. The letters are flat print, not carved, embossed or 3D letter shapes. Nothing else on the envelope: no logos, no institution names, no addresses, no stamps, no barcodes, no numbers.
- Keep the right 16% of the width free of faces and of the envelope (the photo simply continues there).
No children, no ID cards, no forms, no calendars, no money, no bank books, no phones showing screens, no charts, no arrows.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 8. gungmin-sigi-2026-10-shorts · thumbnail_1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 회사 동기 모임 식당에서 두 손으로 머리를 감싸 쥔 57세 김씨 + '조기수령' 생각 꼬리표

**저장 경로: `economic/source/gungmin-sigi-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠 · 세 칸 (위 0~36% 순검정 + 문구 2줄 · 가운데 36~72% 사진 · 아래 72~100% 순검정, 글자·얼굴은 높이 15~85%)**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 검정 평면 글자 on 연회색 꼬리표 #D9DEE6 (짙은 회색 테두리) |
| 위 1줄 | 국민연금 5년 당기면 평생 | **'국민연금' 노랑 #FFD400** · '5년 당기면 평생' 흰색 — 검은 바탕, 가운데 정렬 |
| 위 2줄 | 매달 39만 원 덜 받는다 | **전부 빨강 #FF2A2A + 얇은 흰 외곽선**. 1줄과 같은 크기, 가운데 정렬 |

- 노랑은 중요한 것(주제 낱말 '국민연금'), 빨강은 나쁜 상황(덜 받는 돈)에만. 회색 꼬리표 = 김씨의 생각.

프롬프트:

```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
LAYOUT — three stacked zones, each spanning the full width of the canvas:
1. Top zone, from 0% to 36% of the height: flat solid pure black (#000000), with only the headline text on it.
2. Photo panel, from 36% to 72% of the height: one photorealistic photograph filling the full width edge to edge (a wide horizontal picture, about 3:2), with straight horizontal top and bottom edges.
3. Bottom zone, from 72% to 100% of the height: flat solid pure black (#000000), completely empty (a subtitle is added there later in the video).
No gradient or fade between the zones, no border or frame around the photo, no other bands or panels.
SAFE AREA: YouTube crops Shorts thumbnails to about 4:5 in some feeds on phones and PCs, cutting about 15% from the top and 15% from the bottom. Every important thing — all text, every face and word tag — must stay between 15% and 85% of the height.
Headline in the top black zone: exactly TWO lines of very large, heavy, bold Korean text, both lines the same letter size, EACH LINE CENTERED horizontally on the same center axis (the two lines must not be shifted left or right against each other). Make the letters as large as possible: the longer line spans from about 4% to 96% of the width (each letter about 4.9% of the image height tall, roughly 95 px on a 1080x1920 canvas). Vertically, the two-line block is centered between the 15% line and the top of the photo — it sits between about 19% and 32% of the height — with a black gap of at least 3% of the height between the text and the photo. The text never touches or overlaps the photo. Flat letters on the black, no glow, no 3D, no shadow boxes:
line 1 "국민연금 5년 당기면 평생" — "국민연금" in bright yellow #FFD400 and "5년 당기면 평생" in white;
line 2 "매달 39만 원 덜 받는다" — all in bright red #FF2A2A with a thin white outline.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536) with the same three zones (it will be center-cropped to 9:16, cutting about 8% from the left and right), and keep the headline between 12% and 88% of the width.
Scene inside the photo panel (from 36% to 72% of the height, full width), a warmly lit Korean restaurant in the evening, background softly blurred:
- Center-right (between about 30% and 82% of the width, chest up, face between 40% and 64% of the height): a Korean man aged 57 who looks youthful for his age, like his early 50s (short neat black hair with a little gray at the temples, navy checked button-up shirt), sitting at a restaurant table. He has just realized that he would get less pension every month for the rest of his life, and he is crushed: both hands gripping the sides of his head, head bowed, eyes squeezed shut and brows knitted in pain — clear frustration, regret and despair that read even at small thumbnail size. His face stays visible (the hands are on the sides of his head, not covering his eyes or mouth). Realistic, not cartoonish. From the lower left edge, only the hand of a friend (no face) slides one blank white sheet of paper with nothing printed on it across the table toward him. Fictional person, not resembling any real or famous person. No other people.
- Left side (between about 7% and 28% of the width, at about 40% to 56% of the height): one word tag like a thought label, linked to the man's head by a short trail of small light-gray dots (it shows what he had planned). The tag is a solid light gray (#D9DEE6) rounded rectangle with a thick dark gray border and the Korean word printed in huge flat heavy bold black letters on its flat front face: "조기수령". The letters are flat print, not carved, embossed or 3D letter shapes. No arrows. Nothing overlaps or covers the tag or the letters.
No money, no bills, no coins, no documents with writing, no phones, no calculators, no calendars, no menus or signs with writing, no logos, no charts.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
