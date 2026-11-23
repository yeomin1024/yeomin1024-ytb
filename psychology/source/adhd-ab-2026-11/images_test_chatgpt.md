# 일상툰 캐릭터 테스트 — ChatGPT 그림 요청 (A씨 · B씨)

VERSION: v0.1 — 2026-11-23 — 사용자 지시 "일상 툰처럼 영상 만들건데 어떻게 만들지 알지? 한번 말해보고 테스트용 chatgpt 캐릭터 이미지 생성 명령 알려줘"
대본: `대본_초안.txt` v1.0 · 그림 규칙은 심리 만스피 꼴(`psychology/source/images_build.py` v1.0)을 따르되 그림체만 일상툰으로.
> 그림에는 글자 0 (말풍선·자막·숫자는 코드가 얹음) · 특정 웹툰·작가 이름을 따라 하지 않음 · 가상 인물.

## 쓰는 법
1. ChatGPT **새 대화**를 열고, 아래 **명령 1 (A씨)** 을 그대로 붙여 넣는다.
2. 그림이 나오면 같은 대화에서 **명령 2 (B씨)** 를 붙여 넣는다 — 같은 대화여야 그림체가 맞는다.
3. 두 장을 Claude 대화에 올리면 → 그림체·비율·표정을 보고 고칠 점을 정한 뒤, 본 요청 파일(배경판 · 동작 원화 · 소품 · 조연 · 썸네일)을 만든다.

## 명령 1 — A씨 (32세 여성 회사원)

```
Draw a CHARACTER REFERENCE SHEET for a Korean daily-life webtoon (일상툰) style YouTube animation.

STYLE: simple, warm Korean daily-life webtoon look. Rounded simple shapes, thin clean dark-brown outlines, soft flat pastel colors with at most one light shading tone, very little detail. Characters are about 3 heads tall — a little cute but clearly adults. Faces are simple: small oval eyes, short eyebrows that carry the emotion, a small mouth. Light pink cheeks only when embarrassed or crying. 2D drawing only — not 3D, not a photo, not anime-glossy.

CHARACTER "A": a 32-year-old Korean woman, office worker. Shoulder-length dark brown hair in a loose low ponytail with soft side bangs, a few loose strands. Light blue shirt with sleeves rolled up once, navy cardigan, dark gray slacks, white sneakers. A plain ID badge on a lanyard (completely blank card). Slightly tired eyes in the neutral face. Kind, a bit scattered, relatable.

LAYOUT (landscape 1536x1024, pure white background, no floor, no shadows):
- Top row: full body FRONT view, full body 3/4 view, full body BACK view, all the same height and standing on the same invisible line.
- Bottom row: six head-and-shoulders EXPRESSIONS of the same person, same size, left to right:
  1) neutral, 2) zoned out staring at a phone (empty eyes), 3) panic — wide eyes and one sweat drop, 4) crying with tears but trying to hold it in, 5) relieved small smile, 6) embarrassed — hand on the back of the head.
- Comic effect marks (sweat drops, small sparkle lines) are allowed, but drawn only as shapes.

Absolutely NO text anywhere: no names, no labels, no numbers, no letters, no speech bubbles, no logos. The ID badge, phone screen and any paper are blank.
```

## 명령 2 — B씨 (51세 남성 회사원, 같은 대화에서)

```
Using EXACTLY the same art style, line weight, colors, proportions and sheet layout as the previous sheet, draw a CHARACTER REFERENCE SHEET for CHARACTER "B".

CHARACTER "B": a 51-year-old Korean man, office worker and father. Short black hair neatly combed, gray at the temples, slightly receding hairline. Slightly round face with a few smile lines, a small belly. White shirt with a loosened plain navy tie, gray slacks, black shoes. At home he would wear the same clothes without the tie. Warm but tired, a little stubborn, clearly early 50s (not elderly, not young).

LAYOUT: same as before — top row full body FRONT, 3/4 and BACK views at the same height; bottom row six head-and-shoulders EXPRESSIONS, left to right:
  1) neutral, 2) zoned out staring at a phone, 3) shouting in frustration (eyebrows angled, mouth wide), 4) guilty and sad — head down, hand on forehead, 5) shocked and confused — "who, me?" face, 6) awkward hopeful smile.

Pure white background, no floor, no shadows. Absolutely NO text anywhere: no names, labels, numbers, letters, speech bubbles or logos.
```

## 테스트에서 볼 것 (Claude 검수)
- 두 장의 그림체·선 굵기·비율이 같은가 (같은 사람이 그린 것처럼)
- 휴대폰 화면 크기에서 표정이 바로 읽히는가 (특히 '멍함'·'참는 눈물'·'저요?')
- B씨가 50대로 보이는가 · A씨가 30대 회사원으로 보이는가
- 글자·숫자·라벨이 0인가 (이름표·사원증·휴대폰 화면)
- 앞·옆·뒤 키가 같은가 (나중에 잘라 쓸 때 크기가 맞아야 함)
