# economic 썸네일 4장 — ChatGPT용 (모든 영상 · 읽고 그대로 만들고 각 저장 경로에 올리기)

자동 생성 — `python tools/make_summary.py --chatgpt-all economic` (2026-10-17 15:28). 이 파일은 고치지 말고 영상마다 `thumbnail_N.md`를 고친 뒤 다시 만든다.

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/economic/thumbnails_chatgpt.md

| 영상 | 만들 시안 | 저장 폴더 |
|---|---|---|
| eunte-kkeonaeseugi-2026-10-shorts | thumbnail_1 | `economic/source/eunte-kkeonaeseugi-2026-10/shorts/thumbnails/` |
| gicho-yeongeum-2026-10-shorts | thumbnail_1 | `economic/source/gicho-yeongeum-2026-10/shorts/thumbnails/` |
| isa-mangi-2026-10-shorts | thumbnail_1 | `economic/source/isa-mangi-2026-10/shorts/thumbnails/` |
| toejik-geonbo-2026-10-shorts | thumbnail_1 | `economic/source/toejik-geonbo-2026-10/shorts/thumbnails/` |

## ChatGPT에게 — 이 파일을 읽으면 할 일
1. 아래 썸네일 4장(4개 영상)을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다. 장마다 서로 다른 그림이다 — 앞 장의 인물·구도·색을 이어 쓰지 않는다.
3. 크기는 **세로형 9:16 (1080×1920)** — 쇼츠 썸네일이자 쇼츠 첫 화면이다. **사진 한 장이 네 가장자리까지 꽉 찬다 — 빈 남색·검정 띠, 테두리, 여백, 가운데만 사진인 꼴은 안 된다** (v1.8.0 — 띠가 있으면 영상에서 비율이 틀린 것처럼 보임). 프롬프트가 '글자·얼굴을 두지 않는 자리'(위·오른쪽·아래)를 말해도 그 자리에도 사진(배경·앞쪽 물건)이 이어진다. 9:16이 안 되면 세로 2:3으로 만들고(가운데를 9:16으로 잘라 씀), 글자와 얼굴은 가운데에 두고 양옆 가장자리 8%에는 두지 않는다 (사진은 이어짐).
4. 그림 속 글자는 프롬프트의 따옴표 안 글자만(한글, 그리고 프롬프트가 적은 영문 — 예: ISA), 글자·띄어쓰기·조사 그대로 쓴다 (조사 하나도 빼거나 바꾸지 않는다 — '세금으로'를 '세금'으로 줄이면 뜻이 달라짐). 다른 글자·숫자·로고·워터마크는 넣지 않는다.
5. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다.
6. 한 장을 만들 때마다 그 칸의 '문구' 표와 그림 속 한글을 한 글자씩 맞춰 본다. 크게 확대해서 받침과 모음 획(예: '료'의 ㄹ, '보'의 ㅗ)·조사(예: '1년에'의 '에', '세금으로'의 '으로', '세금을'의 '을')가 빠지거나 가려지지 않았는지도 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다. 쇼츠 그림(세로)은 **위·아래·양옆 가장자리까지 사진인지**도 본다 — 빈 남색·검정 띠가 보이면 띠 없이 다시 만든다 (v1.8.0).
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `3. economic/source/isa-mangi-2026-10/shorts/thumbnails/thumbnail_1.png`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게 (`thumbnail_N.png`).
   - GitHub 에 쓸 수 있으면(쓰기 권한이 있는 GitHub 앱) 장마다 그 경로에 커밋한다. 커밋 메시지: `[썸네일] <영상ID> thumbnail_N 이미지`
   - **쓸 수 없으면 (이 계정의 ChatGPT 는 GitHub 를 읽기만 함 — 2026-10-15 확인)** 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 이 파일의 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"이 그림 4장을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 thumbnail_N.png 이름으로 내려받아 폴더마다 아래 링크에 끌어다 놓고 Commit changes" + 아래 '폴더별 올리기 링크' 목록

## 폴더별 올리기 링크 (ChatGPT가 못 올릴 때 사람이 쓰는 길)

- eunte-kkeonaeseugi-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/eunte-kkeonaeseugi-2026-10/shorts/thumbnails
- gicho-yeongeum-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/gicho-yeongeum-2026-10/shorts/thumbnails
- isa-mangi-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/isa-mangi-2026-10/shorts/thumbnails
- toejik-geonbo-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/toejik-geonbo-2026-10/shorts/thumbnails

## 1. eunte-kkeonaeseugi-2026-10-shorts · thumbnail_1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 휴대폰 글을 보고 굳은 65세 김씨 부부 + '세금'·'건보료' 낱말

**저장 경로: `economic/source/eunte-kkeonaeseugi-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 1 | 세금 | 흰 평면 글자 on 빨강 꼬리표 #FF2A2A |
| 그림 낱말 2 | 건보료 | 흰 평면 글자 on 빨강 꼬리표 #FF2A2A |
| 위 1줄 | 연금 꺼내 쓴 첫해에 | **'연금' 노랑 #FFD400** · '꺼내 쓴 첫해에' 흰색 — 모두 두꺼운 검정 외곽선 |
| 위 2줄 | 세금으로 200만 원 날린다 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

- 노랑은 중요한 것(주제 낱말 '연금'), 빨강은 나쁜 상황(날리는 돈 — 2줄, 손해를 만드는 '세금'·'건보료' 꼬리표)에만 쓴다.

프롬프트:

```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), photorealistic, high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
FULL-BLEED: one continuous photograph fills the entire 9:16 canvas edge to edge. The top edge, bottom edge, left edge and right edge all show the scene. No solid-color bands, no empty navy or black areas, no borders, no frames, no letterbox bars, no picture-in-picture, and no fade to a flat color anywhere.
The same image is also the full-screen opening frame of the Short, and a subtitle is added later over the lower part. Place things like this (fractions of the image height from the top, and of the image width from the left):
- All text and all faces stay between 13% and 66% of the height and between 6% and 84% of the width.
- The top 13%, the right 16% of the width and the bottom 34% still show the photo (the upper wall and the window with sheer curtains of the living room at the top, the window and curtains on the right, the front of the beige sofa and a low wooden coffee table with a teacup in the foreground at the bottom), just without text, faces or important objects.
- The bottom 34% is naturally a little darker (soft shadow and shallow depth of field in the foreground) so white subtitles stay readable, but it remains a detailed part of the photo, never an empty dark area.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536); it will be center-cropped to 9:16, cutting about 8% from the left and right edges, so keep all text and faces well inside the middle of the width.
Text (from 14% to 33% of the height), printed directly over the photo; the background behind it is softly blurred and slightly darker so the letters pop, with no solid box or band behind the text: two lines of huge heavy bold Korean text, both the same size, left-aligned starting at about 7% from the left edge, each line ending before 84% of the width (if a line does not fit, make both lines a little smaller rather than letting it pass 84%):
line 1 "연금 꺼내 쓴 첫해에" — "연금" in bright yellow #FFD400 and "꺼내 쓴 첫해에" in white, both with a thick black outline;
line 2 "세금으로 200만 원 날린다" — all in bright red #FF2A2A with a thick white outline.
Scene (people and the main objects between 33% and 66% of the height; the photo itself fills the whole image), a living room lit by warm late-afternoon sunlight from a window, background softly blurred; the photo continues to every edge of the image:
- Center-right (between about 35% and 82% of the width): a Korean married couple aged 65 who look youthful for their age, like their early 60s, sitting close together on a beige sofa, shown from the chest up. The husband (short neat black hair with a little gray at the temples, light gray cardigan over a white collared shirt) holds a smartphone in both hands at chest height and stares at it, frozen in disbelief, eyebrows raised and lips slightly parted. The wife (chin-length dark brown hair, soft coral knit top) leans toward him with one hand on his shoulder, looking at the phone with a worried frown. The phone screen faces the couple, not the viewer; only its soft glow lights their faces. Natural, realistic expressions, not exaggerated. Fictional people, not resembling any real or famous person.
- Left side (between about 7% and 33% of the width, at about 36% to 58% of the height): two word tags floating up out of the phone like pop-up badges, stacked vertically with a small gap, each linked back to the phone by a faint dotted trail. Each tag is a solid bright red (#FF2A2A) rounded rectangle with the Korean word printed in huge flat heavy bold white letters on its flat front face: "세금" (upper tag) and "건보료" (lower tag). The letters are flat print, not carved, embossed or 3D letter shapes. No arrows. Nothing overlaps or covers the tags or the letters.
No bank books, no charts, no money, no app screens, no website interface, no documents.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 2. gicho-yeongeum-2026-10-shorts · thumbnail_1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 거실에서 '우린 안 돼' 하며 손사래 치는 67세 부부 + '집 한 채'·'국민연금' 생각 꼬리표

**저장 경로: `economic/source/gicho-yeongeum-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 1 | 집 한 채 | 검정 평면 글자 on 연회색 꼬리표 #D9DEE6 (짙은 회색 테두리) |
| 그림 낱말 2 | 국민연금 | 검정 평면 글자 on 연회색 꼬리표 #D9DEE6 (짙은 회색 테두리) |
| 위 1줄 | 기초연금 포기하면 | **'기초연금' 노랑 #FFD400** · '포기하면' 흰색 — 모두 두꺼운 검정 외곽선 |
| 위 2줄 | 1년에 500만 원 날린다 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

- 노랑은 중요한 것(주제 낱말 '기초연금'), 빨강은 나쁜 상황(잃는 돈)에만. 회색 꼬리표 = 남편의 생각 (손해 자체가 아니라 빨강이 아님).

프롬프트:

```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), photorealistic, high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
FULL-BLEED: one continuous photograph fills the entire 9:16 canvas edge to edge. The top edge, bottom edge, left edge and right edge all show the scene. No solid-color bands, no empty navy or black areas, no borders, no frames, no letterbox bars, no picture-in-picture, and no fade to a flat color anywhere.
The same image is also the full-screen opening frame of the Short, and a subtitle is added later over the lower part. Place things like this (fractions of the image height from the top, and of the image width from the left):
- All text and all faces stay between 13% and 66% of the height and between 6% and 84% of the width.
- The top 13%, the right 16% of the width and the bottom 34% still show the photo (the upper wall and curtains at the top, the room and window on the right, a low coffee table with two teacups in the foreground at the bottom), just without text, faces or important objects.
- The bottom 34% is naturally a little darker (soft shadow and shallow depth of field in the foreground) so white subtitles stay readable, but it remains a detailed part of the photo, never an empty dark area.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536); it will be center-cropped to 9:16, cutting about 8% from the left and right edges, so keep all text and faces well inside the middle of the width.
Text (from 14% to 33% of the height), printed directly over the photo; the wall behind it is softly blurred and slightly darker so the letters pop, with no solid box or band behind the text: two lines of huge heavy bold Korean text, both the same size, left-aligned starting at about 7% from the left edge, each line ending before 84% of the width:
line 1 "기초연금 포기하면" — "기초연금" in bright yellow #FFD400 and "포기하면" in white, both with a thick black outline;
line 2 "1년에 500만 원 날린다" — all in bright red #FF2A2A with a thick white outline.
Scene: a bright Korean apartment living room in the late afternoon, warm sunlight from a large window with sheer curtains, background softly blurred:
- Center-right (between about 30% and 82% of the width, chest up, faces between 34% and 60% of the height): a Korean married couple aged 67 who look youthful for their age, like their early 60s, sitting side by side on a light gray sofa. The husband (short neat hair with gray streaks, light blue checked button-up shirt) raises one hand with the palm facing forward in a dismissive "no, that's not for us" wave, shaking his head slightly with a confident, mistaken expression. The wife (shoulder-length dark hair, soft pink knit top) turns toward him with an unsure, worried look, as if doubting him. Natural, realistic expressions, not exaggerated. Fictional people, not resembling any real or famous person. No other people.
- Left side (between about 7% and 30% of the width, at about 36% to 56% of the height): two word tags like thought labels, stacked vertically with a small gap, linked to the husband's head by a short trail of small light-gray dots (they show why he believes they cannot get it). Each tag is a solid light gray (#D9DEE6) rounded rectangle with a thick dark gray border and the Korean words printed in huge flat heavy bold black letters on its flat front face: "집 한 채" (upper tag) and "국민연금" (lower tag). The letters are flat print, not carved, embossed or 3D letter shapes. No arrows. Nothing overlaps or covers the tags or the letters.
No money, no flying bills, no envelopes, no documents, no forms, no application papers, no phones, no calculators, no calendars, no buildings or signs, no charts.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 3. isa-mangi-2026-10-shorts · thumbnail_1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 점심시간 동료의 휴대폰을 보고 굳은 61세 이씨 + '세금' 낱말

**저장 경로: `economic/source/isa-mangi-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 세금 | 흰 평면 글자 on 빨강 꼬리표 #FF2A2A |
| 위 1줄 | ISA 만기 돈 잘못 두면 | **'ISA 만기 돈' 노랑 #FFD400** · '잘못 두면' 흰색 — 모두 두꺼운 검정 외곽선 (ISA 는 라틴 대문자) |
| 위 2줄 | 세금을 96만 원 더 낸다 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

- 노랑은 중요한 것(주제 낱말 'ISA 만기 돈'), 빨강은 나쁜 상황(더 내는 세금 — 2줄과 꼬리표 '세금')에만 쓴다.

프롬프트:

```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), photorealistic, high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
FULL-BLEED: one continuous photograph fills the entire 9:16 canvas edge to edge. The top edge, bottom edge, left edge and right edge all show the scene. No solid-color bands, no empty navy or black areas, no borders, no frames, no letterbox bars, no picture-in-picture, and no fade to a flat color anywhere.
The same image is also the full-screen opening frame of the Short, and a subtitle is added later over the lower part. Place things like this (fractions of the image height from the top, and of the image width from the left):
- All text and all faces stay between 13% and 66% of the height and between 6% and 84% of the width.
- The top 13%, the right 16% of the width and the bottom 34% still show the photo (the cafeteria ceiling lights and the upper part of the large windows at the top, the cafeteria and windows on the right, the cafeteria table edge and the lunch tray in the foreground at the bottom), just without text, faces or important objects.
- The bottom 34% is naturally a little darker (soft shadow and shallow depth of field in the foreground) so white subtitles stay readable, but it remains a detailed part of the photo, never an empty dark area.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536); it will be center-cropped to 9:16, cutting about 8% from the left and right edges, so keep all text and faces well inside the middle of the width.
Text (from 14% to 33% of the height), printed directly over the photo; the background behind it is softly blurred and slightly darker so the letters pop, with no solid box or band behind the text: two lines of huge heavy bold Korean text, both the same size, left-aligned starting at about 7% from the left edge, each line ending before 84% of the width (if a line does not fit, make both lines a little smaller rather than letting it pass 84%):
line 1 "ISA 만기 돈 잘못 두면" — "ISA 만기 돈" in bright yellow #FFD400 and "잘못 두면" in white, both with a thick black outline (write ISA in capital Latin letters);
line 2 "세금을 96만 원 더 낸다" — all in bright red #FF2A2A with a thick white outline.
Scene (people and the main objects between 33% and 66% of the height; the photo itself fills the whole image), a bright company cafeteria at lunchtime with daylight from large windows, background softly blurred; the photo continues to every edge of the image:
- Center-right (between about 38% and 82% of the width): a Korean office worker aged 61 who looks youthful for his age, like his mid 50s (short neat black hair with a little gray, light blue open-collar dress shirt, no tie, no ID badge), seated at a table in front of a plain lunch tray, shown from the chest up. He holds a spoon paused in mid-air and leans forward toward a smartphone, staring at its screen, frozen in disbelief, eyebrows raised and lips slightly parted. Natural, realistic expression, not exaggerated. Fictional person, not resembling any real or famous person.
- Left side (between about 4% and 36% of the width, at about 50% to 60% of the height): only the forearm and hand of a colleague in a white shirt sleeve, reaching in from the left edge and holding the smartphone out toward him; no face of the colleague. The phone screen faces the man, not the viewer; only its soft glow is visible.
- Above the phone (between about 8% and 32% of the width, at about 37% to 47% of the height): one word tag floating up out of the phone like a pop-up badge, linked back to the phone by a faint dotted trail. The tag is a solid bright red (#FF2A2A) rounded rectangle with the Korean word "세금" printed in huge flat heavy bold white letters on its flat front face. The letters are flat print, not carved, embossed or 3D letter shapes. No arrows. Nothing overlaps or covers the tag or the letters.
No bank books, no money, no calendars, no boxes, no charts, no app screens, no company names or logos.
Render ONLY the text given in quotes (Korean, plus the Latin letters ISA), exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 4. toejik-geonbo-2026-10-shorts · thumbnail_1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 현관에서 첫 건보료 고지서를 열어 보고 굳은 60세 최씨 부부

**저장 경로: `economic/source/toejik-geonbo-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 (봉투 앞면) | 건보료 고지서 | 흰 평면 글자 on 빨강 띠 #FF2A2A |
| 위 1줄 | 건보료 고지서대로 내면 | **'건보료' 노랑 #FFD400** · '고지서대로 내면' 흰색 — 모두 두꺼운 검정 외곽선 |
| 위 2줄 | 3년에 860만 원 날린다 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

- 노랑은 중요한 것(주제 낱말 '건보료' — 1줄), 빨강은 나쁜 상황(날리는 돈 — 2줄, 봉투 띠 '건보료 고지서')에만 쓴다.

프롬프트:

```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), photorealistic, high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
FULL-BLEED: one continuous photograph fills the entire 9:16 canvas edge to edge. The top edge, bottom edge, left edge and right edge all show the scene. No solid-color bands, no empty navy or black areas, no borders, no frames, no letterbox bars, no picture-in-picture, and no fade to a flat color anywhere.
The same image is also the full-screen opening frame of the Short, and a subtitle is added later over the lower part. Place things like this (fractions of the image height from the top, and of the image width from the left):
- All text and all faces stay between 13% and 66% of the height and between 6% and 84% of the width.
- The top 13%, the right 16% of the width and the bottom 34% still show the photo (the upper part of the front door, the wall and a ceiling light at the top, the hallway wall on the right, the shoe cabinet top and the entrance floor in the foreground at the bottom), just without text, faces or important objects.
- The bottom 34% is naturally a little darker (soft shadow and shallow depth of field in the foreground) so white subtitles stay readable, but it remains a detailed part of the photo, never an empty dark area.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536); it will be center-cropped to 9:16, cutting about 8% from the left and right edges, so keep all text and faces well inside the middle of the width.
Text (from 14% to 33% of the height), printed directly over the photo; the background behind it is softly blurred and slightly darker so the letters pop, with no solid box or band behind the text: two lines of huge heavy bold Korean text, both the same size, left-aligned starting at about 7% from the left edge, each line ending before 84% of the width (if a line does not fit, make both lines a little smaller rather than letting it pass 84%):
line 1 "건보료 고지서대로 내면" — "건보료" in bright yellow #FFD400 and "고지서대로 내면" in white, both with a thick black outline;
line 2 "3년에 860만 원 날린다" — all in bright red #FF2A2A with a thick white outline.
Scene (people and the main objects between 33% and 66% of the height; the photo itself fills the whole image), the entrance hall of a Korean apartment in bright daytime, soft daylight, front door and shoe cabinet softly blurred; the photo continues to every edge of the image:
- Center-right (between about 40% and 80% of the width): a Korean man aged 60, just retired, who looks youthful for his age, like his mid 50s (short neat black hair with a little gray, beige knit zip-up cardigan over a white T-shirt), shown from the chest up. He holds an unfolded letter up in one hand with its blank back side toward the viewer and stares at it, frozen in disbelief, eyebrows raised and lips slightly parted. Just behind his left shoulder (about 30% to 55% of the width), his wife aged 60 who looks like her mid 50s (shoulder-length dark hair, light lavender blouse) rests a hand on his arm and peers at the letter with a worried frown. Natural, realistic expressions, not exaggerated. Fictional people, not resembling any real or famous person.
- Lower left of the scene (between about 8% and 38% of the width, at about 48% to 62% of the height): in his other hand, held by its edge so no finger covers the words, an opened plain white envelope with its front facing the viewer. On the front there is one flat bright red (#FF2A2A) band with the Korean words "건보료 고지서" printed in huge flat heavy bold white letters. The letters are flat print, not carved, embossed or 3D letter shapes. Nothing else on the envelope: no logos, no institution names, no addresses, no stamps, no barcodes, no numbers.
No children, no ID cards, no forms, no calendars, no money, no charts, no arrows.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
