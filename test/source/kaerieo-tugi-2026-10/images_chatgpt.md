# 깨끗한 일본 길거리에 캐리어가 버려지는 이유 — 이미지 8장 ChatGPT용 (읽고 그대로 만들고 각 저장 경로에 올리기)

작성: 2026-10-20 (Claude, v1.1) — 짝 문서 `test/일본_캐리어투기_제작안.txt`

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/test/source/kaerieo-tugi-2026-10/images_chatgpt.md

| 번호 | 파일 | 크기 | 쓰는 곳 |
|---|---|---|---|
| 1 | `test/source/kaerieo-tugi-2026-10/images/IMG-L1.jpg` | 가로 16:9 | 롱폼 배경 — 이케부쿠로 밤 골목, 집적소 앞 홀로 선 캐리어 |
| 2 | `test/source/kaerieo-tugi-2026-10/images/IMG-L2.jpg` | 가로 16:9 | 롱폼 배경 — 일본 매장의 새 캐리어 진열대 |
| 3 | `test/source/kaerieo-tugi-2026-10/images/IMG-L3.jpg` | 가로 16:9 | 롱폼 배경 — 아침의 대형 쓰레기 수거장 |
| 4 | `test/source/kaerieo-tugi-2026-10/images/IMG-L4.jpg` | 가로 16:9 | 롱폼 배경 — 호텔 창고에 쌓인 캐리어 |
| 5 | `test/source/kaerieo-tugi-2026-10/images/IMG-L5.jpg` | 가로 16:9 | 롱폼 배경 — 쓰레기통 없는 깨끗한 역 플랫폼 |
| 6 | `test/source/kaerieo-tugi-2026-10/images/IMG-L6.jpg` | 가로 16:9 | 롱폼 배경 — 공항 출국장 카운터 |
| 7 | `test/source/kaerieo-tugi-2026-10/images/THUMB-L.jpg` | 가로 16:9 | 롱폼 썸네일 (한글 문구 포함) |
| 8 | `test/source/kaerieo-tugi-2026-10/images/SHORTS-OPEN.jpg` | 세로 9:16 · 세 칸 | 쇼츠 첫 장면 (= 쇼츠 썸네일, 0초 장면) |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 8장을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다.
   - 1~6번은 같은 영상의 배경이라 **그림체·색감이 모두 같아야 한다** (프롬프트마다 같은 그림체 문장이 들어 있음).
3. 크기는 **장마다 '크기' 줄대로**: 가로 = 16:9 (안 되면 가장 넓은 가로형 — 중요한 대상은 위아래 8% 밖에 두지 않음) · 세로 = 9:16 세 칸 (안 되면 세로 2:3). 어느 쪽이든 **그림이 네 가장자리까지 꽉 찬다** — 빈 띠·테두리·여백 없음 (세 칸 그림의 위·아래 순검정 칸은 예외).
4. **1~6번(배경)에는 글자를 하나도 넣지 않는다** — 간판 글씨·숫자·로고·워터마크도 없음. 7·8번(썸네일)은 프롬프트의 따옴표 안 한글만, 글자·띄어쓰기·물음표·쉼표 그대로 쓴다. 줄 수·줄바꿈·색도 프롬프트대로.
5. 배경 그림의 사람은 뒷모습·실루엣·먼 거리로만 그리고, 얼굴을 알아볼 수 있게 그리지 않는다. 실존 인물을 닮게 그리지 않는다. 썸네일의 인물은 지어낸 사람이다.
6. 7·8번은 만들 때마다 그 칸의 '문구' 표와 그림 속 한글을 한 글자씩 맞춰 본다. 크게 확대해서 받침·모음 획·조사가 빠지거나 가려지지 않았는지 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다.
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `1. test/source/kaerieo-tugi-2026-10/images/IMG-L1.jpg`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게.
   - **올리기 전에 JPEG(.jpg)로 바꿔 700KB 이하로 만든다** — 파이썬(PIL)으로 RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장. GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다. 올린 뒤 GitHub 에 있는 그 파일의 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
   - **GitHub 앱으로 장마다 그 경로에 커밋한다.** 커밋 메시지: `[test] kaerieo-tugi-2026-10 <파일 이름> 이미지` (예: `[test] kaerieo-tugi-2026-10 IMG-L1.jpg 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 저장 경로의 파일 이름으로 내려받아 아래 링크에 끌어다 놓고 Commit changes" + https://github.com/yeomin1024/yeomin1024-ytb/upload/main/test/source/kaerieo-tugi-2026-10/images

## 1. IMG-L1 — 이케부쿠로 밤 골목, 집적소 앞 홀로 선 캐리어 (그림체 기준)

**저장 경로: `test/source/kaerieo-tugi-2026-10/images/IMG-L1.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, night-time Tokyo street light, cool teal shadows with warm sodium-lamp highlights, subtle film grain. 16:9 landscape.
A narrow back street in Ikebukuro, Tokyo, late at night, a clean neighborhood garbage collection point with a folded green net, and one abandoned hard-shell suitcase standing alone in front of it with a plain yellow warning sticker (no writing) on its side, wet asphalt reflecting vending-machine light, quiet and lonely mood. No people. No readable signs.
Keep the suitcase in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 2. IMG-L2 — 일본 매장의 새 캐리어 진열대

**저장 경로: `test/source/kaerieo-tugi-2026-10/images/IMG-L2.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, night-time Tokyo street light, cool teal shadows with warm sodium-lamp highlights, subtle film grain. 16:9 landscape.
A bright Japanese department-store luggage section with rows of shiny new hard-shell suitcases in many colors, a tourist couple with an old worn suitcase and shopping bags looking at the new ones, seen from behind, warm retail lighting. No readable signs, tags or brand logos.
Keep the suitcases and the couple in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 3. IMG-L3 — 아침의 대형 쓰레기 수거장

**저장 경로: `test/source/kaerieo-tugi-2026-10/images/IMG-L3.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, night-time Tokyo street light, cool teal shadows with warm sodium-lamp highlights, subtle film grain. 16:9 landscape.
Early morning at a Japanese residential oversized-garbage pickup spot: an old chair, a small cabinet and a suitcase lined up neatly on the curb, each with a plain colored paper sticker attached (no writing), a small white garbage truck arriving in the distance, soft blue morning light. No people. No readable signs.
Keep the curb items in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 4. IMG-L4 — 호텔 창고에 쌓인 캐리어

**저장 경로: `test/source/kaerieo-tugi-2026-10/images/IMG-L4.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, night-time Tokyo street light, cool teal shadows with warm sodium-lamp highlights, subtle film grain. 16:9 landscape.
A cramped back storage room of a Japanese hotel, a pile of abandoned suitcases of different sizes stacked up to the ceiling next to cleaning carts, a single bare ceiling light, a staff member seen from behind standing with hands on hips; no recognizable face. No readable labels.
Keep the pile of suitcases in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 5. IMG-L5 — 쓰레기통 없는 깨끗한 역 플랫폼

**저장 경로: `test/source/kaerieo-tugi-2026-10/images/IMG-L5.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, night-time Tokyo street light, cool teal shadows with warm sodium-lamp highlights, subtle film grain. 16:9 landscape.
A spotless Japanese train station platform at night, polished floor, neat yellow tactile paving, benches, vending machines, and noticeably no trash bins anywhere, a few commuters far away seen from behind, cool fluorescent light, calm and orderly mood. No readable signs.
Keep the platform in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 6. IMG-L6 — 공항 출국장 카운터

**저장 경로: `test/source/kaerieo-tugi-2026-10/images/IMG-L6.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, night-time Tokyo street light, cool teal shadows with warm sodium-lamp highlights, subtle film grain. 16:9 landscape.
A bright Japanese international airport departure hall, a small service counter where a traveler seen from behind hands over an empty old suitcase to a staff member, large windows with an airplane outside, clean modern interior; no recognizable faces, no readable signs or logos.
Keep the counter and the traveler in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 7. THUMB-L — 롱폼 썸네일

**저장 경로: `test/source/kaerieo-tugi-2026-10/images/THUMB-L.jpg`** — JPEG 700KB 이하

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 꼬리표 | 한 구에서만 1년 290개 | 흰 글자 on 빨강 상자 #FF2A2A — 그림 왼쪽 위 |
| 그림 말풍선 | 그냥 버리면 안 돼? | 검정 글자 on 노랑 말풍선 #FFD400 — 그림 오른쪽 위 |
| 하단 1줄 | 깨끗한 일본 길거리에 | '깨끗한' 노랑 #FFD400 · 나머지 흰색 — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 캐리어가 버려지는 이유 | '버려지는 이유' 빨강 #FF2A2A · '캐리어가' 흰색 · 1줄보다 크게 — 모두 두꺼운 검정 외곽선 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720). Cinematic digital painting, semi-realistic, very high contrast, dramatic, bold and readable at small size.
Upper 62% of the frame:
- Center-right: a tourist in his 30s (fictional, not resembling any real person) standing on a clean Tokyo back street at night next to an old suitcase, holding a brand-new suitcase handle, hand on the back of his head, brows knitted, looking around helplessly for somewhere to throw the old one away; behind him a spotless street with no trash bins and a neat garbage collection point. Cool teal night with warm vending-machine light.
- Upper left: one bold tag, a solid bright red (#FF2A2A) rounded box with the Korean text "한 구에서만 1년 290개" printed in huge flat heavy bold white letters.
- Upper right: a bright yellow (#FFD400) speech bubble with the Korean text "그냥 버리면 안 돼?" in heavy bold black letters.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "깨끗한 일본 길거리에" — '깨끗한' 노랑 #FFD400 ; 나머지 흰색, all with a thick black outline;
line 2 "캐리어가 버려지는 이유" — '버려지는 이유' 빨강 #FF2A2A ; '캐리어가' 흰색 ; 1줄보다 크게, all with a thick black outline, clearly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the person, the tag and the bubble in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text inside the central 16:9 area, at least 8% away from the top and bottom edges.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, spacing, comma, apostrophes and question mark, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 8. SHORTS-OPEN — 쇼츠 첫 장면 (세 칸 · 문구 포함)

**저장 경로: `test/source/kaerieo-tugi-2026-10/images/SHORTS-OPEN.jpg`** — JPEG 700KB 이하

크기: **세로 9:16 (1080×1920) — 쇼츠 · 세 칸 (위 0~36% 순검정 + 문구 2줄 · 가운데 36~72% 그림 · 아래 72~100% 순검정, 글자·꼬리표는 높이 15~85%)**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위 1줄 | 깨끗한 일본 길거리에 | '깨끗한' 노랑 #FFD400 · 나머지 흰색 — 검정 바탕 위 평면 글자 |
| 위 2줄 | 버려진 캐리어, 왜? | '버려진 캐리어,' 흰색 · '왜?' 빨강 #FF2A2A — 1줄과 같은 크기 |
| 그림 꼬리표 | 도시마구 1년 290개 | 흰 글자 on 빨강 상자 #FF2A2A |

프롬프트:

```
Vertical YouTube Shorts opening frame, 9:16 portrait (1080x1920), high contrast.
LAYOUT — three full-width zones: 0–36% of the height flat solid pure black (#000000) with only the headline; 36–72% one cinematic digital painting edge to edge with straight top and bottom edges; 72–100% flat solid pure black, empty (subtitles will be added there later). No gradient, fade or border between the zones.
SAFE AREA: some feeds crop to about 4:5 — all text and the word tag stay between 15% and 85% of the height.
Headline: exactly TWO lines of very large heavy bold Korean text, the same letter size, EACH LINE CENTERED on the same axis, the longer line from about 4% to 96% of the width, the block between about 18% and 33% of the height and at least 3% above the painting; flat letters, no outline, no glow, no 3D.
line 1 "깨끗한 일본 길거리에" — '깨끗한' 노랑 #FFD400 ; 나머지 흰색;
line 2 "버려진 캐리어, 왜?" — '버려진 캐리어,' 흰색 ; '왜?' 빨강 #FF2A2A.
Painting zone (36–72%): Cinematic digital painting, semi-realistic, night-time Tokyo street light, cool teal shadows with warm sodium-lamp highlights, subtle film grain. One abandoned hard-shell suitcase standing alone in front of a clean garbage collection point on a narrow Tokyo back street at night, a plain yellow warning sticker (no writing) on its side, wet asphalt reflecting vending-machine light. No people.
On the upper left of the painting (about 5–45% of the width, 39–47% of the height): one bold tag, a solid bright red (#FF2A2A) rounded box with the Korean text "도시마구 1년 290개" printed in large flat heavy bold white letters on its flat front face (flat print, not carved or 3D). Keep the right 16% of the width below 45% of the height free of tags (Shorts buttons).
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536) with the same three zones and keep the headline between 12% and 88% of the width.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, spacing, comma and question mark, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
