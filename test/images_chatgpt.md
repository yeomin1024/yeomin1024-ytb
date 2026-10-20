# test 이미지 11장 — ChatGPT용 (일본 전통 축제 사망 사고 롱폼·쇼츠 · 읽고 그대로 만들고 각 저장 경로에 올리기)

작성: 2026-10-20 (Claude) — 짝 문서 `test/일본축제_사망사고_제작안.txt` (v7)

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/test/images_chatgpt.md

| 번호 | 파일 | 크기 | 쓰는 곳 |
|---|---|---|---|
| 1 | `test/IMG-L1.jpg` | 가로 16:9 | 롱폼 배경 — 사이조 강변, 태고대 |
| 2 | `test/IMG-L2.jpg` | 가로 16:9 | 롱폼 배경 — 오사카 단지리, 밤의 교차로 |
| 3 | `test/IMG-L3.jpg` | 가로 16:9 | 롱폼 배경 — 신사, 붉은 도리이와 등불 |
| 4 | `test/IMG-L4.jpg` | 가로 16:9 | 롱폼 배경 — 축제가 끝난 빈 거리 |
| 5 | `test/IMG-L5.jpg` | 가로 16:9 | 롱폼 배경 — 사이다이지 에요, 밤의 사찰 |
| 6 | `test/IMG-L6.jpg` | 가로 16:9 | 롱폼 배경 — 꺼진 등불이 섞인 등불 줄 |
| 7 | `test/IMG-S1.jpg` | 세로 9:16 | 쇼츠 배경 — 1번의 세로 버전 |
| 8 | `test/IMG-S2.jpg` | 세로 9:16 | 쇼츠 배경 — 4번의 세로 버전 |
| 9 | `test/IMG-S3.jpg` | 세로 9:16 | 쇼츠 배경 — 6번의 세로 버전 |
| 10 | `test/THUMB-L.jpg` | 가로 16:9 | 롱폼 썸네일 (한글 문구 포함) |
| 11 | `test/THUMB-S.jpg` | 세로 9:16 | 쇼츠 썸네일 (한글 문구 포함) |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 11장을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다.
   - 1~9번은 같은 영상의 배경이라 **그림체·색감이 모두 같아야 한다** (프롬프트마다 같은 그림체 문장이 들어 있음). 7~9번은 각각 1·4·6번과 같은 장면을 세로 구도로 다시 그린 것이다.
3. 크기는 **장마다 '크기' 줄대로**: 가로 = 16:9 (안 되면 가장 넓은 가로형 — 중요한 대상은 위아래 8% 밖에 두지 않음) · 세로 = 9:16 (안 되면 세로 2:3 — 중요한 대상은 양옆 8% 밖에 두지 않음). 어느 쪽이든 **그림이 네 가장자리까지 꽉 찬다** — 빈 띠·테두리·여백 없음.
4. **1~9번(배경)에는 글자를 하나도 넣지 않는다** — 간판 글씨·숫자·로고·워터마크도 없음. 10·11번(썸네일)은 프롬프트의 따옴표 안 한글만, 글자·띄어쓰기·물음표·쉼표 그대로 쓴다. 줄 수·줄바꿈·색도 프롬프트대로.
5. 사람은 뒷모습·실루엣·먼 거리로만 그리고, 얼굴을 알아볼 수 있게 그리지 않는다. 실존 인물을 닮게 그리지 않는다. 피·다친 사람·사고 순간은 그리지 않는다.
6. 10·11번은 만들 때마다 그 칸의 '문구' 표와 그림 속 한글을 한 글자씩 맞춰 본다. 크게 확대해서 받침·모음 획·조사('사망자가'의 '가', '축제를'의 '를')가 빠지거나 가려지지 않았는지 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다.
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `1. test/IMG-L1.jpg`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게.
   - **올리기 전에 JPEG(.jpg)로 바꿔 700KB 이하로 만든다** — 파이썬(PIL)으로 RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장. GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다. 올린 뒤 GitHub 에 있는 그 파일의 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
   - **GitHub 앱으로 장마다 그 경로에 커밋한다.** 커밋 메시지: `[test] <파일 이름> 이미지` (예: `[test] IMG-L1.jpg 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 저장 경로의 파일 이름으로 내려받아 아래 링크에 끌어다 놓고 Commit changes" + https://github.com/yeomin1024/yeomin1024-ytb/upload/main/test

## 1. IMG-L1 — 사이조 강변, 태고대 (그림체 기준)

**저장 경로: `test/IMG-L1.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, moody dusk lighting, warm lantern glow against deep navy shadows, subtle film grain. 16:9 landscape.
A towering ornate Japanese festival float called taikodai, about five meters tall, with gold and crimson embroidered panels and stacked red cushions on top, lifted high on long wooden poles by a crowd of carriers in matching happi coats, on a wide riverbed at dusk, the river reflecting an orange sky, festival lanterns in the distance. The crowd is seen from behind; no recognizable faces.
Keep the float in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere. No blood, no injured people, no accident.
```

## 2. IMG-L2 — 오사카 단지리, 밤의 교차로

**저장 경로: `test/IMG-L2.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, moody dusk lighting, warm lantern glow against deep navy shadows, subtle film grain. 16:9 landscape.
A massive wooden danjiri festival cart with intricate wood carvings and a two-tiered roof, paper lanterns glowing, at a narrow intersection in an old Japanese town at night. Long ropes stretch forward and people in happi coats pull them with motion blur, all seen from behind; no recognizable faces. Slightly low camera angle.
Keep the cart in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere. No blood, no injured people, no accident.
```

## 3. IMG-L3 — 신사, 붉은 도리이와 등불

**저장 경로: `test/IMG-L3.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, moody dusk lighting, warm lantern glow against deep navy shadows, subtle film grain. 16:9 landscape.
A Shinto shrine with a large red torii gate at twilight, rows of glowing paper lanterns along a stone approach path, a thick sacred straw rope (shimenawa), light mist. No people. Calm and solemn atmosphere.
Keep the torii gate in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, writing on the lanterns, logos or watermarks anywhere.
```

## 4. IMG-L4 — 축제가 끝난 빈 거리

**저장 경로: `test/IMG-L4.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, moody dusk lighting, warm lantern glow against deep navy shadows, subtle film grain. 16:9 landscape.
An empty Japanese festival street late at night after the festival. A single paper lantern is still glowing, scattered paper streamers lie on wet asphalt, and a lone festival happi coat is draped over a wooden barrier. Rain-slick reflections, deep shadows, melancholic mood. No people.
Keep the lantern and the happi coat in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, writing on the lantern, logos or watermarks anywhere.
```

## 5. IMG-L5 — 사이다이지 에요, 밤의 사찰

**저장 경로: `test/IMG-L5.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, moody dusk lighting, warm lantern glow against deep navy shadows, subtle film grain. 16:9 landscape.
Night at a Japanese Buddhist temple courtyard during a traditional winter festival (Saidaiji Eyo in Okayama). A huge crowd of men in traditional white festival loincloths packed tightly together, seen from far above and behind, steam rising from the crowd under bright floodlights, the silhouette of a large temple roof. Distant view; no individual faces visible. Chaotic yet solemn.
Keep the crowd and the temple roof in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, logos or watermarks anywhere. No blood, no injured people, no accident.
```

이 프롬프트로 만들 수 없다고 나오면 **이 장만** 아래 프롬프트로 바꿔 만든다 (저장 경로는 같음):

```
Cinematic digital painting, semi-realistic, moody dusk lighting, warm lantern glow against deep navy shadows, subtle film grain. 16:9 landscape.
Night at a Japanese Buddhist temple courtyard during a traditional winter festival. Steam and mist rise under bright floodlights, a large dark crowd silhouette is visible in the distance, and the silhouette of a large temple roof stands behind it. No individual people visible. Solemn atmosphere.
Keep the temple roof in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, logos or watermarks anywhere.
```

## 6. IMG-L6 — 꺼진 등불이 섞인 등불 줄

**저장 경로: `test/IMG-L6.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, moody dusk lighting, warm lantern glow against deep navy shadows, subtle film grain. 16:9 landscape.
A long row of Japanese paper lanterns (chochin) hanging along a dark festival street at night. Most lanterns glow warmly, but several lanterns in the row have gone dark. Shallow depth of field focused on one dark lantern in the center. Somber and quiet mood. No people.
Keep the dark lantern in the center, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, writing on the lanterns, logos or watermarks anywhere.
```

## 7. IMG-S1 — 1번의 세로 버전

**저장 경로: `test/IMG-S1.jpg`** — JPEG 700KB 이하

크기: 세로 9:16

프롬프트:

```
Cinematic digital painting, semi-realistic, moody dusk lighting, warm lantern glow against deep navy shadows, subtle film grain. 9:16 vertical.
The same scene as image 1, recomposed vertically: a towering ornate Japanese festival float called taikodai with gold and crimson embroidered panels and stacked red cushions on top, lifted high on long wooden poles by a crowd of carriers in matching happi coats, on a wide riverbed at dusk. The float and the crowd are in the lower 60% of the frame; the upper 40% is a dark orange-to-navy dusk sky. The crowd is seen from behind; no recognizable faces.
Keep the float at least 8% away from the left and right edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere. No blood, no injured people, no accident.
```

## 8. IMG-S2 — 4번의 세로 버전

**저장 경로: `test/IMG-S2.jpg`** — JPEG 700KB 이하

크기: 세로 9:16

프롬프트:

```
Cinematic digital painting, semi-realistic, moody dusk lighting, warm lantern glow against deep navy shadows, subtle film grain. 9:16 vertical.
The same scene as image 4, recomposed vertically: an empty Japanese festival street late at night after the festival, a single glowing paper lantern about one third from the top, a lone festival happi coat draped over a wooden barrier, scattered paper streamers and rain-slick reflections on wet asphalt in the lower part. Deep shadows, melancholic mood. No people.
Keep the lantern and the happi coat at least 8% away from the left and right edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, writing on the lantern, logos or watermarks anywhere.
```

## 9. IMG-S3 — 6번의 세로 버전

**저장 경로: `test/IMG-S3.jpg`** — JPEG 700KB 이하

크기: 세로 9:16

프롬프트:

```
Cinematic digital painting, semi-realistic, moody dusk lighting, warm lantern glow against deep navy shadows, subtle film grain. 9:16 vertical.
The same scene as image 6, recomposed vertically: a row of Japanese paper lanterns (chochin) running from the top to the bottom of the frame along a dark festival street at night. Most lanterns glow warmly, but several have gone dark. Shallow depth of field focused on one dark lantern in the center. Somber and quiet mood. No people.
Keep the dark lantern at least 8% away from the left and right edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, writing on the lanterns, logos or watermarks anywhere.
```

## 10. THUMB-L — 롱폼 썸네일

**저장 경로: `test/THUMB-L.jpg`** — JPEG 700KB 이하

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 꼬리표 | 8일 만에 3명 사망 | 흰 글자 on 빨강 상자 #FF2A2A |
| 그림 말풍선 | 현지 반응은? | 검정 글자 on 노랑 말풍선 #FFD400 |
| 하단 1줄 | 사망자가 나와도 | '사망자' 빨강 #FF2A2A · '가 나와도' 흰색 — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 일본이 축제를 안 멈추는 이유 | '일본이 축제를' 흰색 · '안 멈추는 이유' 노랑 #FFD400 — 모두 두꺼운 검정 외곽선. 1줄보다 크게 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720). Cinematic digital painting, semi-realistic, very high contrast, dramatic, bold and readable at small size.
Upper 62% of the frame:
- Center-right: a huge ornate Japanese festival float with gold and crimson embroidered panels, tilting dangerously to one side at dusk, silhouettes of carriers straining beneath its long wooden poles, dramatic backlight from the setting sun and paper lanterns, dust in the air, low camera angle, intense red-orange and deep navy contrast. Carriers only in silhouette; no recognizable faces. No blood, no injured people.
- Upper left: one bold tag, a solid bright red (#FF2A2A) rounded box with the Korean text "8일 만에 3명 사망" printed in huge flat heavy bold white letters.
- Next to the float, upper right: a bright yellow (#FFD400) speech bubble with the Korean text "현지 반응은?" in heavy bold black letters.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "사망자가 나와도" — "사망자" in bright red #FF2A2A and "가 나와도" in white, all with a thick black outline;
line 2 "일본이 축제를 안 멈추는 이유" — "일본이 축제를" in white and "안 멈추는 이유" in bright yellow #FFD400, all with a thick black outline, clearly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the float, the tag and the bubble in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text inside the central 16:9 area, at least 8% away from the top and bottom edges.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, spacing and question mark, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 11. THUMB-S — 쇼츠 썸네일

**저장 경로: `test/THUMB-S.jpg`** — JPEG 700KB 이하

크기: 세로 9:16 (1080×1920) — 쇼츠. 그림이 화면 끝까지 꽉 차고(빈 띠 없음), 글자는 높이 15~85% 안.

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 1줄 | 매년 사고 사망자가 나와도 | 흰색 · '사망자' 빨강 #FF2A2A — 두꺼운 검정 외곽선 |
| 2줄 | 안 멈춘다? | 전부 노랑 #FFD400 + 두꺼운 검정 외곽선. 가장 크게 |
| 3줄 | 일본 전통 축제, 현지 반응이 더 충격 | 흰색 · '현지 반응이 더 충격' 노랑 #FFD400 — 두꺼운 검정 외곽선 |
| 그림 꼬리표 | 8일 만에 3명 사망 | 흰 글자 on 빨강 상자 #FF2A2A |

프롬프트:

```
YouTube Shorts thumbnail, 9:16 vertical (1080x1920). Cinematic digital painting, semi-realistic, very high contrast, dramatic, bold and readable at small size.
The painting fills the whole frame edge to edge — no empty bands, borders or margins.
Background scene: a dark orange-to-navy dusk sky in the upper half, and in the lower half a huge ornate Japanese festival float with gold and crimson embroidered panels tilting dangerously to one side, silhouettes of carriers straining beneath its long wooden poles, backlit by the sunset and paper lanterns, dust in the air. Carriers only in silhouette; no recognizable faces. No blood, no injured people.
Text, all centered horizontally, each line centered on the same axis, in heavy bold sans-serif Korean font with a thick black outline, placed over the sky between 15% and 50% of the image height:
line 1 "매년 사고 사망자가 나와도" — white, with "사망자" in bright red #FF2A2A;
line 2 "안 멈춘다?" — all bright yellow #FFD400, the largest line;
line 3 "일본 전통 축제, 현지 반응이 더 충격" — white, with "현지 반응이 더 충격" in bright yellow #FFD400; make this line smaller so it fits within 4% to 96% of the width.
Just below the text, centered: one solid bright red (#FF2A2A) rounded box with the Korean text "8일 만에 3명 사망" in heavy bold white letters.
All text must stay between 15% and 85% of the image height (some feeds crop the top and bottom 15%).
If 9:16 is not available, use a 2:3 vertical canvas and keep all text at least 8% away from the left and right edges.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, spacing, comma and question mark. No other text, letters, numbers, watermarks or logos anywhere.
```
