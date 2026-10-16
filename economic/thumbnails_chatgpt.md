# economic 썸네일 8장 — ChatGPT용 (모든 영상 · 읽고 그대로 만들고 각 저장 경로에 올리기)

자동 생성 — `python tools/make_summary.py --chatgpt-all economic` (2026-10-16 19:08). 이 파일은 고치지 말고 영상마다 `thumbnail_N.md`를 고친 뒤 다시 만든다.

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/economic/thumbnails_chatgpt.md

| 영상 | 만들 시안 | 저장 폴더 |
|---|---|---|
| isa-mangi-2026-10 | thumbnail_1, thumbnail_2 | `economic/source/isa-mangi-2026-10/thumbnails/` |
| toejik-geonbo-2026-10 | thumbnail_1, thumbnail_3 | `economic/source/toejik-geonbo-2026-10/thumbnails/` |
| eunte-kkeonaeseugi-2026-10-shorts | thumbnail_1 | `economic/source/eunte-kkeonaeseugi-2026-10/shorts/thumbnails/` |
| gicho-yeongeum-2026-10-shorts | thumbnail_1 | `economic/source/gicho-yeongeum-2026-10/shorts/thumbnails/` |
| isa-mangi-2026-10-shorts | thumbnail_1 | `economic/source/isa-mangi-2026-10/shorts/thumbnails/` |
| toejik-geonbo-2026-10-shorts | thumbnail_1 | `economic/source/toejik-geonbo-2026-10/shorts/thumbnails/` |

## ChatGPT에게 — 이 파일을 읽으면 할 일
1. 아래 썸네일 8장(6개 영상)을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다. 장마다 서로 다른 그림이다 — 앞 장의 인물·구도·색을 이어 쓰지 않는다.
3. 크기는 **장마다 '크기' 줄대로**: 롱폼 썸네일 = 가로형 16:9 (1280×720 — 안 되면 가장 넓은 가로형, 글자와 얼굴은 가운데, 위아래 8% 비움) · **쇼츠 썸네일(영상 ID 끝이 `-shorts`) = 세로형 9:16 (1080×1920)** — 안 되면 세로 2:3, 글자와 얼굴은 가운데, 양옆 8% 비움.
4. 그림 속 글자는 프롬프트의 따옴표 안 글자만(한글, 그리고 프롬프트가 적은 영문 — 예: ISA), 글자·띄어쓰기 그대로 쓴다. 다른 글자·숫자·로고·워터마크는 넣지 않는다.
5. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다.
6. 한 장을 만들 때마다 그 칸의 '문구' 표와 그림 속 한글을 한 글자씩 맞춰 본다. 크게 확대해서 받침과 모음 획(예: '료'의 ㄹ, '보'의 ㅗ)이 빠지거나 가려지지 않았는지도 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다.
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `3. economic/source/toejik-geonbo-2026-10/thumbnails/thumbnail_1.png`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게 (`thumbnail_N.png`).
   - GitHub 에 쓸 수 있으면(쓰기 권한이 있는 GitHub 앱) 장마다 그 경로에 커밋한다. 커밋 메시지: `[썸네일] <영상ID> thumbnail_N 이미지`
   - **쓸 수 없으면 (이 계정의 ChatGPT 는 GitHub 를 읽기만 함 — 2026-10-15 확인)** 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 이 파일의 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"이 그림 8장을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 thumbnail_N.png 이름으로 내려받아 폴더마다 아래 링크에 끌어다 놓고 Commit changes" + 아래 '폴더별 올리기 링크' 목록

## 폴더별 올리기 링크 (ChatGPT가 못 올릴 때 사람이 쓰는 길)

- isa-mangi-2026-10: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/isa-mangi-2026-10/thumbnails
- toejik-geonbo-2026-10: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/toejik-geonbo-2026-10/thumbnails
- eunte-kkeonaeseugi-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/eunte-kkeonaeseugi-2026-10/shorts/thumbnails
- gicho-yeongeum-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/gicho-yeongeum-2026-10/shorts/thumbnails
- isa-mangi-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/isa-mangi-2026-10/shorts/thumbnails
- toejik-geonbo-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/toejik-geonbo-2026-10/shorts/thumbnails

## 1. isa-mangi-2026-10 · thumbnail_1 — 본안(클릭률 최대): 밤 사무실에서 머리를 감싸 쥔 60세 안팎 직장인 + '세금' 낱말

**저장 경로: `economic/source/isa-mangi-2026-10/thumbnails/thumbnail_1.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 세금 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50·60대 ISA 만기 돈 연금저축 | '50·60대' 흰색 · **'ISA 만기 돈 연금저축' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 안 옮기면 3년에 96만 원 손해 | '안 옮기면' 흰색 + 검정 외곽선 · **'3년에 96만 원 손해' 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

- 노랑은 중요한 것(ISA 만기 돈을 연금저축으로), 빨강은 나쁜 상황(손해와 손해를 만드는 세금)에 쓴다.

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 55% of the width): a Korean office worker around 60 who looks youthful for his age, like his late 50s (short neat black hair with a little gray at the temples, white dress shirt with a loosened navy tie), sitting at his office desk at night with a laptop whose screen only glows (no text on it), shown from the chest up and large in the frame. He grips his head with both hands, head slightly bowed, eyes squeezed shut in frustration and regret. Natural, realistic expression, not exaggerated. Fictional person, not resembling any real or famous person.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "세금" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the man.
- Background: an office at night with blurred city lights through the window, cool blue tones; warm desk-lamp light only on the man's face.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 ISA 만기 돈 연금저축" — "50·60대" in white and "ISA 만기 돈 연금저축" in bright yellow #FFD400, all with a thick black outline (keep the middle dot "·" between 50 and 60, and write ISA in capital Latin letters);
line 2 "안 옮기면 3년에 96만 원 손해" — "안 옮기면" in white with a thick black outline, and "3년에 96만 원 손해" in bright red #FF2A2A with a thick white outline.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the second line does not fit, make both lines a little smaller rather than letting it run into that corner. Keep the man and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and the face inside the central 16:9 area, at least 8% away from the top and bottom edges.
Render ONLY the text given in quotes (Korean, plus the Latin letters ISA), exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 2. isa-mangi-2026-10 · thumbnail_2 — 실험안 ①: 얼굴 없이, 밤 사무실 책상 위 꽉 쥔 두 주먹 + '세금' 낱말

**저장 경로: `economic/source/isa-mangi-2026-10/thumbnails/thumbnail_2.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 세금 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50·60대 ISA 만기 돈 연금저축 | '50·60대' 흰색 · **'ISA 만기 돈 연금저축' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 안 옮기면 3년에 96만 원 손해 | '안 옮기면' 흰색 + 검정 외곽선 · **'3년에 96만 원 손해' 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 60% of the width): a Korean office worker shown only from the neck down, his face outside the frame (white dress shirt with a loosened navy tie), sitting at his office desk at night with both fists clenched tightly on the desk in frustration. Beside his fists: a laptop whose screen only glows (no text) and a few blank white sheets of paper (no writing). Realistic hands. Fictional person.
- Left side (about 40% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "세금" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward his fists.
- Background: an office at night with blurred city lights through the window, cool blue tones; warm desk-lamp light on his fists and shirt.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 ISA 만기 돈 연금저축" — "50·60대" in white and "ISA 만기 돈 연금저축" in bright yellow #FFD400, all with a thick black outline (keep the middle dot "·" between 50 and 60, and write ISA in capital Latin letters);
line 2 "안 옮기면 3년에 96만 원 손해" — "안 옮기면" in white with a thick black outline, and "3년에 96만 원 손해" in bright red #FF2A2A with a thick white outline.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the second line does not fit, make both lines a little smaller rather than letting it run into that corner. Keep the hands, the desk items and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text inside the central 16:9 area, at least 8% away from the top and bottom edges.
Render ONLY the text given in quotes (Korean, plus the Latin letters ISA), exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 3. toejik-geonbo-2026-10 · thumbnail_1 — 본안(클릭률 최대): 걱정하는 60세 안팎 부부 + '지역가입자' 낱말

**저장 경로: `economic/source/toejik-geonbo-2026-10/thumbnails/thumbnail_1.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 지역가입자 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50·60대 건보료 0원 되는 순서 | '50·60대' 흰색 · **'건보료 0원 되는 순서' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 은퇴 후 그냥 두면 월 30만 원 | '은퇴 후 그냥 두면' 흰색 + 검정 외곽선 · **'월 30만 원' 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

- 노랑은 중요한 것(건보료 0원 되는 순서), 빨강은 나쁜 상황(월 30만 원과 그 원인 지역가입자)에 쓴다.

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 60% of the width): a Korean married couple around 60 who look youthful for their age, sitting side by side on a living-room sofa at night, shown from the chest up and large in the frame. The husband (short neat black hair with a little gray at the temples, gray knit sweater) presses one hand to his forehead with his eyes closed, at a loss. The wife (short black bob, light pink blouse) covers her mouth with one hand and looks ahead with shocked, worried eyes. Natural, realistic expressions, not exaggerated. Fictional people, not resembling any real or famous person.
- Left side (about 40% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "지역가입자" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the couple.
- Background: a dim living room at night, softly blurred, cool blue tones; warm light only on the couple's faces.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 건보료 0원 되는 순서" — "50·60대" in white and "건보료 0원 되는 순서" in bright yellow #FFD400, all with a thick black outline (keep the middle dot "·" between 50 and 60);
line 2 "은퇴 후 그냥 두면 월 30만 원" — "은퇴 후 그냥 두면" in white with a thick black outline, and "월 30만 원" in bright red #FF2A2A with a thick white outline.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the second line does not fit, make both lines a little smaller rather than letting it run into that corner. Keep the couple and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 4. toejik-geonbo-2026-10 · thumbnail_3 — 실험안 ②: 사람 없이, '지역가입자'가 거실 탁자 위 지폐 더미를 내리누름

**저장 경로: `economic/source/toejik-geonbo-2026-10/thumbnails/thumbnail_3.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 지역가입자 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50·60대 건보료 0원 되는 순서 | '50·60대' 흰색 · **'건보료 0원 되는 순서' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 은퇴 후 그냥 두면 월 30만 원 | '은퇴 후 그냥 두면' 흰색 + 검정 외곽선 · **'월 30만 원' 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, dramatic, high contrast, bold and readable at small size. No people in the image.
Upper 62% of the frame:
- Center-right: a neat stack of plain generic banknotes with no portraits, no numbers and no patterns on a low living-room coffee table at night. The stack is being crushed from above: it is squashed and a few banknotes burst out to the sides, with motion streaks. Beside the table, the end of a sofa and a pair of reading glasses (no writing anywhere).
- Upper left: one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "지역가입자" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down onto the stack, pressing it down.
- Background: a dim living room at night, softly blurred, cool blue tones; a warm spotlight on the banknote stack.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 건보료 0원 되는 순서" — "50·60대" in white and "건보료 0원 되는 순서" in bright yellow #FFD400, all with a thick black outline (keep the middle dot "·" between 50 and 60);
line 2 "은퇴 후 그냥 두면 월 30만 원" — "은퇴 후 그냥 두면" in white with a thick black outline, and "월 30만 원" in bright red #FF2A2A with a thick white outline.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the second line does not fit, make both lines a little smaller rather than letting it run into that corner. Keep the banknotes and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text inside the central 16:9 area, at least 8% away from the top and bottom edges.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 5. eunte-kkeonaeseugi-2026-10-shorts · thumbnail_1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 휴대폰 글을 보고 굳은 65세 김씨 부부 + '세금'·'건보료' 낱말

**저장 경로: `economic/source/eunte-kkeonaeseugi-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 1 | 세금 | 흰 평면 글자 on 빨강 꼬리표 #FF2A2A |
| 그림 낱말 2 | 건보료 | 흰 평면 글자 on 빨강 꼬리표 #FF2A2A |
| 위 1줄 | 은퇴 첫해에만 | '은퇴' 흰색 · **'첫해에만' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 위 2줄 | 200만 원 넘게 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 조금 크게 |

- 노랑은 중요한 것(언제 — '첫해에만'), 빨강은 나쁜 상황(손해와 손해를 만드는 '세금'·'건보료')에만 쓴다.

프롬프트:

```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), photorealistic, high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
The same image is also used as a full-screen video frame: it is shown at the very start of the Short while the first sentence is narrated, and a subtitle is added later over the bottom area. So keep these safe areas exactly (fractions of the image height from the top, and of the image width from the left):
- Top 13%: plain very dark navy (#0C1424) background only, nothing else.
- All text and all faces stay between 13% and 66% of the height and between 6% and 84% of the width. The right 16% of the width has no text and no faces (on-screen buttons go there).
- Bottom 34% (from 66% of the height down to the bottom edge): a quiet, empty, very dark navy area that fades toward near black. No text, no faces, no important objects there.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536); it will be center-cropped to 9:16, cutting about 8% from the left and right edges, so keep all text and faces well inside the middle of the width.
Text area (from 14% to 33% of the height, on the plain dark navy background): two lines of huge heavy bold Korean text, left-aligned starting at about 7% from the left edge, each line ending before 84% of the width:
line 1 "은퇴 첫해에만" — "은퇴" in white and "첫해에만" in bright yellow #FFD400, both with a thick black outline;
line 2 "200만 원 넘게 손해", slightly larger than line 1 — all in bright red #FF2A2A with a thick white outline.
Scene (from 33% to 66% of the height), a living room lit by warm late-afternoon sunlight from a window, background softly blurred; the scene blends smoothly upward into the dark navy text area and downward into the dark bottom area:
- Center-right (between about 35% and 82% of the width): a Korean married couple aged 65 who look youthful for their age, like their early 60s, sitting close together on a beige sofa, shown from the chest up. The husband (short neat black hair with a little gray at the temples, light gray cardigan over a white collared shirt) holds a smartphone in both hands at chest height and stares at it, frozen in disbelief, eyebrows raised and lips slightly parted. The wife (chin-length dark brown hair, soft coral knit top) leans toward him with one hand on his shoulder, looking at the phone with a worried frown. The phone screen faces the couple, not the viewer; only its soft glow lights their faces. Natural, realistic expressions, not exaggerated. Fictional people, not resembling any real or famous person.
- Left side (between about 7% and 33% of the width, at about 36% to 58% of the height): two word tags floating up out of the phone like pop-up badges, stacked vertically with a small gap, each linked back to the phone by a faint dotted trail. Each tag is a solid bright red (#FF2A2A) rounded rectangle with the Korean word printed in huge flat heavy bold white letters on its flat front face: "세금" (upper tag) and "건보료" (lower tag). The letters are flat print, not carved, embossed or 3D letter shapes. No arrows. Nothing overlaps or covers the tags or the letters.
No bank books, no charts, no money, no app screens, no website interface, no documents.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 6. gicho-yeongeum-2026-10-shorts · thumbnail_1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 이웃집 저녁 자리에서 놀라 굳은 67세 박씨 부부 + '집 한 채'·'국민연금' 생각 꼬리표

**저장 경로: `economic/source/gicho-yeongeum-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 1 | 집 한 채 | 검정 평면 글자 on 연회색 꼬리표 #D9DEE6 (짙은 회색 테두리) |
| 그림 낱말 2 | 국민연금 | 검정 평면 글자 on 연회색 꼬리표 #D9DEE6 (짙은 회색 테두리) |
| 위 1줄 | 67세 부부 기초연금 | '67세 부부' 흰색 · **'기초연금' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 위 2줄 | 매달 41만 원 넘게 놓침 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

- 노랑은 중요한 것(주제 낱말 '기초연금'), 빨강은 나쁜 상황(놓치는 돈)에만 쓴다. 회색 꼬리표 = 박씨의 생각 (손해 자체가 아니라 빨강이 아님).

프롬프트:

```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), photorealistic, high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
The same image is also used as a full-screen video frame: it is shown at the very start of the Short while the first sentence is narrated, and a subtitle is added later over the bottom area. So keep these safe areas exactly (fractions of the image height from the top, and of the image width from the left):
- Top 13%: plain very dark navy (#0C1424) background only, nothing else.
- All text and all faces stay between 13% and 66% of the height and between 6% and 84% of the width. The right 16% of the width has no text and no faces (on-screen buttons go there).
- Bottom 34% (from 66% of the height down to the bottom edge): a quiet, empty, very dark navy area that fades toward near black. No text, no faces, no important objects there.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536); it will be center-cropped to 9:16, cutting about 8% from the left and right edges, so keep all text and faces well inside the middle of the width.
Text area (from 14% to 33% of the height, on the plain dark navy background): two lines of huge heavy bold Korean text, both the same size, left-aligned starting at about 7% from the left edge, each line ending before 84% of the width:
line 1 "67세 부부 기초연금" — "67세 부부" in white and "기초연금" in bright yellow #FFD400, both with a thick black outline;
line 2 "매달 41만 원 넘게 놓침" — all in bright red #FF2A2A with a thick white outline.
Scene (from 33% to 66% of the height), a cozy dining room in a neighbor's apartment in the evening, lit by a warm golden pendant lamp, background softly blurred; the scene blends smoothly upward into the dark navy text area and downward into the dark bottom area:
- Center-right (between about 35% and 82% of the width): a Korean married couple aged 67 who look youthful for their age, like their early 60s, sitting side by side at a dinner table set with many small dishes of Korean home food in plain bowls and plates, shown from the chest up. The husband (short neat black hair with gray streaks, olive-green crew-neck sweater) has stopped with his chopsticks frozen in mid-air, eyebrows raised and lips slightly parted, staring in disbelief toward someone off-frame on the left. The wife (dark hair tied back, cream blouse with a light beige cardigan) rests one hand lightly on her chest, eyes wide, looking the same way, surprised and worried. Natural, realistic expressions, not exaggerated. Fictional people, not resembling any real or famous person. No other people visible.
- Left side (between about 7% and 33% of the width, at about 36% to 56% of the height): two word tags like thought labels, stacked vertically with a small gap, linked to the husband's head by a short trail of small light-gray dots (they show what he had believed). Each tag is a solid light gray (#D9DEE6) rounded rectangle with a thick dark gray border and the Korean words printed in huge flat heavy bold black letters on its flat front face: "집 한 채" (upper tag) and "국민연금" (lower tag). The letters are flat print, not carved, embossed or 3D letter shapes. No arrows. Nothing overlaps or covers the tags or the letters.
No money, no envelopes, no documents or forms, no calculators, no calendars, no buildings or signs, no charts.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 7. isa-mangi-2026-10-shorts · thumbnail_1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 점심시간 동료의 휴대폰을 보고 굳은 61세 이씨 + '세금' 낱말

**저장 경로: `economic/source/isa-mangi-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 세금 | 흰 평면 글자 on 빨강 꼬리표 #FF2A2A |
| 위 1줄 | 61세 ISA 만기 돈 | '61세' 흰색 · **'ISA 만기 돈' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 (ISA 는 라틴 대문자) |
| 위 2줄 | 3년 동안 96만 원 더 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 조금 크게 |

- 노랑은 중요한 것(무엇 — 'ISA 만기 돈'), 빨강은 나쁜 상황(더 내는 돈과 그것을 만드는 '세금')에만 쓴다.

프롬프트:

```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), photorealistic, high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
The same image is also used as a full-screen video frame: it is shown at the very start of the Short while the first sentence is narrated, and a subtitle is added later over the bottom area. So keep these safe areas exactly (fractions of the image height from the top, and of the image width from the left):
- Top 13%: plain very dark navy (#0C1424) background only, nothing else.
- All text and all faces stay between 13% and 66% of the height and between 6% and 84% of the width. The right 16% of the width has no text and no faces (on-screen buttons go there).
- Bottom 34% (from 66% of the height down to the bottom edge): a quiet, empty, very dark navy area that fades toward near black. No text, no faces, no important objects there.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536); it will be center-cropped to 9:16, cutting about 8% from the left and right edges, so keep all text and faces well inside the middle of the width.
Text area (from 14% to 33% of the height, on the plain dark navy background): two lines of huge heavy bold text, left-aligned starting at about 7% from the left edge, each line ending before 84% of the width:
line 1 "61세 ISA 만기 돈" — "61세" in white and "ISA 만기 돈" in bright yellow #FFD400, both with a thick black outline (write ISA in capital Latin letters);
line 2 "3년 동안 96만 원 더", slightly larger than line 1 — all in bright red #FF2A2A with a thick white outline.
Scene (from 33% to 66% of the height), a bright company cafeteria at lunchtime with daylight from large windows, background softly blurred; the scene blends smoothly upward into the dark navy text area and downward into the dark bottom area:
- Center-right (between about 38% and 82% of the width): a Korean office worker aged 61 who looks youthful for his age, like his mid 50s (short neat black hair with a little gray, light blue open-collar dress shirt, no tie, no ID badge), seated at a table in front of a plain lunch tray, shown from the chest up. He holds a spoon paused in mid-air and leans forward toward a smartphone, staring at its screen, frozen in disbelief, eyebrows raised and lips slightly parted. Natural, realistic expression, not exaggerated. Fictional person, not resembling any real or famous person.
- Left side (between about 4% and 36% of the width, at about 50% to 60% of the height): only the forearm and hand of a colleague in a white shirt sleeve, reaching in from the left edge and holding the smartphone out toward him; no face of the colleague. The phone screen faces the man, not the viewer; only its soft glow is visible.
- Above the phone (between about 8% and 32% of the width, at about 37% to 47% of the height): one word tag floating up out of the phone like a pop-up badge, linked back to the phone by a faint dotted trail. The tag is a solid bright red (#FF2A2A) rounded rectangle with the Korean word "세금" printed in huge flat heavy bold white letters on its flat front face. The letters are flat print, not carved, embossed or 3D letter shapes. No arrows. Nothing overlaps or covers the tag or the letters.
No bank books, no money, no calendars, no boxes, no charts, no app screens, no company names or logos.
Render ONLY the text given in quotes (Korean, plus the Latin letters ISA), exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 8. toejik-geonbo-2026-10-shorts · thumbnail_1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 현관에서 첫 건보료 고지서를 열어 보고 굳은 60세 최씨 부부

**저장 경로: `economic/source/toejik-geonbo-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 (봉투 앞면) | 건보료 고지서 | 흰 평면 글자 on 빨강 띠 #FF2A2A |
| 위 1줄 | 퇴직 후 안 내도 될 건보료 | '퇴직 후' 흰색 · **'안 내도 될 건보료' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 위 2줄 | 매달 약 30만 원씩 낸다 | **'매달 약 30만 원씩' 빨강 #FF2A2A + 두꺼운 흰 외곽선** · '낸다' 흰색 + 검정 외곽선. 1줄보다 조금 크게 |

- 노랑은 중요한 것('안 내도 될 건보료'), 빨강은 나쁜 상황(매달 내는 돈과 고지서)에만 쓴다.

프롬프트:

```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), photorealistic, high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
The same image is also used as a full-screen video frame: it is shown at the very start of the Short while the first sentence is narrated, and a subtitle is added later over the bottom area. So keep these safe areas exactly (fractions of the image height from the top, and of the image width from the left):
- Top 13%: plain very dark navy (#0C1424) background only, nothing else.
- All text and all faces stay between 13% and 66% of the height and between 6% and 84% of the width. The right 16% of the width has no text and no faces (on-screen buttons go there).
- Bottom 34% (from 66% of the height down to the bottom edge): a quiet, empty, very dark navy area that fades toward near black. No text, no faces, no important objects there.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536); it will be center-cropped to 9:16, cutting about 8% from the left and right edges, so keep all text and faces well inside the middle of the width.
Text area (from 14% to 33% of the height, on the plain dark navy background): two lines of huge heavy bold Korean text, left-aligned starting at about 7% from the left edge, each line ending before 84% of the width:
line 1 "퇴직 후 안 내도 될 건보료" — "퇴직 후" in white and "안 내도 될 건보료" in bright yellow #FFD400, all with a thick black outline;
line 2 "매달 약 30만 원씩 낸다", slightly larger than line 1 — "매달 약 30만 원씩" in bright red #FF2A2A with a thick white outline, and "낸다" in white with a thick black outline.
Scene (from 33% to 66% of the height), the entrance hall of a Korean apartment in bright daytime, soft daylight, front door and shoe cabinet softly blurred; the scene blends smoothly upward into the dark navy text area and downward into the dark bottom area:
- Center-right (between about 40% and 80% of the width): a Korean man aged 60, just retired, who looks youthful for his age, like his mid 50s (short neat black hair with a little gray, beige knit zip-up cardigan over a white T-shirt), shown from the chest up. He holds an unfolded letter up in one hand with its blank back side toward the viewer and stares at it, frozen in disbelief, eyebrows raised and lips slightly parted. Just behind his left shoulder (about 30% to 55% of the width), his wife aged 60 who looks like her mid 50s (shoulder-length dark hair, light lavender blouse) rests a hand on his arm and peers at the letter with a worried frown. Natural, realistic expressions, not exaggerated. Fictional people, not resembling any real or famous person.
- Lower left of the scene (between about 8% and 38% of the width, at about 48% to 62% of the height): in his other hand, held by its edge so no finger covers the words, an opened plain white envelope with its front facing the viewer. On the front there is one flat bright red (#FF2A2A) band with the Korean words "건보료 고지서" printed in huge flat heavy bold white letters. The letters are flat print, not carved, embossed or 3D letter shapes. Nothing else on the envelope: no logos, no institution names, no addresses, no stamps, no barcodes, no numbers.
No children, no ID cards, no forms, no calendars, no money, no charts, no arrows.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
