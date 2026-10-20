# 재일교포도 일본 영주권을 잃을까? — 이미지 9장 ChatGPT용 (읽고 그대로 만들고 각 저장 경로에 올리기)

작성: 2026-10-20 (Claude, v1.0) — 짝 문서 `test/재일교포_영주권_제작안.txt`

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/test/source/jaeil-yeongju-2026-10/images_chatgpt.md

| 번호 | 파일 | 크기 | 쓰는 곳 |
|---|---|---|---|
| 1 | `test/source/jaeil-yeongju-2026-10/images/IMG-L1.jpg` | 가로 16:9 | 롱폼 배경 — 도쿄 코리아타운 골목 (신오쿠보 느낌) |
| 2 | `test/source/jaeil-yeongju-2026-10/images/IMG-L2.jpg` | 가로 16:9 | 롱폼 배경 — 1950년대 일본 동네 골목 (역사) |
| 3 | `test/source/jaeil-yeongju-2026-10/images/IMG-L3.jpg` | 가로 16:9 | 롱폼 배경 — 출입국 관청 창구 앞 대기 의자 |
| 4 | `test/source/jaeil-yeongju-2026-10/images/IMG-L4.jpg` | 가로 16:9 | 롱폼 배경 — 책상 위 세금 고지서와 계산기 |
| 5 | `test/source/jaeil-yeongju-2026-10/images/IMG-L5.jpg` | 가로 16:9 | 롱폼 배경 — 창구에 낸 신청서와 지폐 |
| 6 | `test/source/jaeil-yeongju-2026-10/images/IMG-L6.jpg` | 가로 16:9 | 롱폼 배경 — 문 닫은 한식당 앞의 사장 |
| 7 | `test/source/jaeil-yeongju-2026-10/images/IMG-L7.jpg` | 가로 16:9 | 롱폼 배경 — 집 앞의 3대 가족 |
| 8 | `test/source/jaeil-yeongju-2026-10/images/THUMB-L.jpg` | 가로 16:9 | 롱폼 썸네일 (한글 문구 포함) |
| 9 | `test/source/jaeil-yeongju-2026-10/images/SHORTS-OPEN.jpg` | 세로 9:16 · 세 칸 | 쇼츠 첫 장면 (= 쇼츠 썸네일, 0초 장면) |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 9장을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다.
   - 1~7번은 같은 영상의 배경이라 **그림체·색감이 모두 같아야 한다** (프롬프트마다 같은 그림체 문장이 들어 있음).
3. 크기는 **장마다 '크기' 줄대로**: 가로 = 16:9 (안 되면 가장 넓은 가로형 — 중요한 대상은 위아래 8% 밖에 두지 않음) · 세로 = 9:16 세 칸 (안 되면 세로 2:3). 어느 쪽이든 **그림이 네 가장자리까지 꽉 찬다** — 빈 띠·테두리·여백 없음 (세 칸 그림의 위·아래 순검정 칸은 예외).
4. **1~7번(배경)에는 글자를 하나도 넣지 않는다** — 간판 글씨·숫자·로고·워터마크도 없음. 8·9번(썸네일)은 프롬프트의 따옴표 안 한글만, 글자·띄어쓰기·물음표·쉼표 그대로 쓴다. 줄 수·줄바꿈·색도 프롬프트대로.
5. 배경 그림의 사람은 뒷모습·실루엣·먼 거리로만 그리고, 얼굴을 알아볼 수 있게 그리지 않는다. 실존 인물을 닮게 그리지 않는다. 썸네일의 인물은 지어낸 사람이다.
6. 8·9번은 만들 때마다 그 칸의 '문구' 표와 그림 속 한글을 한 글자씩 맞춰 본다. 크게 확대해서 받침·모음 획·조사가 빠지거나 가려지지 않았는지 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다.
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `1. test/source/jaeil-yeongju-2026-10/images/IMG-L1.jpg`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게.
   - **올리기 전에 JPEG(.jpg)로 바꿔 700KB 이하로 만든다** — 파이썬(PIL)으로 RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장. GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다. 올린 뒤 GitHub 에 있는 그 파일의 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
   - **GitHub 앱으로 장마다 그 경로에 커밋한다.** 커밋 메시지: `[test] jaeil-yeongju-2026-10 <파일 이름> 이미지` (예: `[test] jaeil-yeongju-2026-10 IMG-L1.jpg 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 저장 경로의 파일 이름으로 내려받아 아래 링크에 끌어다 놓고 Commit changes" + https://github.com/yeomin1024/yeomin1024-ytb/upload/main/test/source/jaeil-yeongju-2026-10/images

## 1. IMG-L1 — 도쿄 코리아타운 골목 (신오쿠보 느낌) (그림체 기준)

**저장 경로: `test/source/jaeil-yeongju-2026-10/images/IMG-L1.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, warm late-afternoon light with soft shadows, muted earthy tones, subtle film grain. 16:9 landscape.
A lively Korea-town side street in Tokyo in the late afternoon, small Korean restaurants and grocery shops with lanterns and awnings, people walking seen from behind, warm light, everyday atmosphere. Shop signs are blank shapes with no readable text in any language; no recognizable faces.
Keep the street and the shops in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 2. IMG-L2 — 1950년대 일본 동네 골목 (역사)

**저장 경로: `test/source/jaeil-yeongju-2026-10/images/IMG-L2.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, warm late-afternoon light with soft shadows, muted earthy tones, subtle film grain. 16:9 landscape.
A 1950s Japanese neighborhood alley with low wooden houses and laundry poles, a few families and children seen from behind and far away, soft sepia-tinted warm light, nostalgic and quiet mood. No readable signs or text; no recognizable faces.
Keep the alley and the houses in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 3. IMG-L3 — 출입국 관청 창구 앞 대기 의자

**저장 경로: `test/source/jaeil-yeongju-2026-10/images/IMG-L3.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, warm late-afternoon light with soft shadows, muted earthy tones, subtle film grain. 16:9 landscape.
A clean Japanese government immigration office waiting area, rows of blue chairs, a few foreign residents waiting with document folders seen from behind, numbered-ticket display as a blank glowing panel, service counters in the distance, calm institutional light. No readable signs, numbers or text; no recognizable faces.
Keep the waiting area in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 4. IMG-L4 — 책상 위 세금 고지서와 계산기

**저장 경로: `test/source/jaeil-yeongju-2026-10/images/IMG-L4.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, warm late-afternoon light with soft shadows, muted earthy tones, subtle film grain. 16:9 landscape.
A wooden kitchen table with a stack of official-looking envelopes and payment slips with blank fields, a calculator, reading glasses and a cup of tea, warm lamp light, serious but calm mood. Papers have no readable text, numbers or logos. No people.
Keep the papers and the calculator in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 5. IMG-L5 — 창구에 낸 신청서와 지폐

**저장 경로: `test/source/jaeil-yeongju-2026-10/images/IMG-L5.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, warm late-afternoon light with soft shadows, muted earthy tones, subtle film grain. 16:9 landscape.
Close-up of a government service counter: an application form with blank fields, a residence-card-sized plain card (no text or photo), and a small stack of Japanese yen banknotes shown only as plain paper shapes with no readable printing, a hand pushing them across the counter, cool light.
Keep the form, card and banknotes in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 6. IMG-L6 — 문 닫은 한식당 앞의 사장

**저장 경로: `test/source/jaeil-yeongju-2026-10/images/IMG-L6.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, warm late-afternoon light with soft shadows, muted earthy tones, subtle film grain. 16:9 landscape.
A small Korean restaurant in Tokyo at dusk with its shutter half down, the middle-aged owner seen from behind standing in front of it holding a folder of documents, warm interior light spilling onto the street, thoughtful mood. No readable signs or text; no recognizable face.
Keep the owner and the shop in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 7. IMG-L7 — 집 앞의 3대 가족

**저장 경로: `test/source/jaeil-yeongju-2026-10/images/IMG-L7.jpg`** — JPEG 700KB 이하

크기: 가로 16:9

프롬프트:

```
Cinematic digital painting, semi-realistic, warm late-afternoon light with soft shadows, muted earthy tones, subtle film grain. 16:9 landscape.
Three generations of a family — a grandmother, parents and a child — standing together in front of a modest Japanese house at golden hour, seen from behind, the child holding the grandmother's hand, warm hopeful light. No readable signs; no recognizable faces.
Keep the family and the house in the central area, at least 8% away from the top and bottom edges. The painting fills the whole frame edge to edge.
No text, letters, numbers, signs with writing, logos or watermarks anywhere.
```

## 8. THUMB-L — 롱폼 썸네일

**저장 경로: `test/source/jaeil-yeongju-2026-10/images/THUMB-L.jpg`** — JPEG 700KB 이하

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 꼬리표 | 수수료 20배 | 흰 글자 on 빨강 상자 #FF2A2A — 그림 왼쪽 위 |
| 그림 말풍선 | 2억 못 내면 떠나라? | 검정 글자 on 노랑 말풍선 #FFD400 — 그림 오른쪽 위 |
| 하단 1줄 | 재일교포도 | '재일교포도' 흰색 — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 영주권 잃을까? | '영주권' 노랑 #FFD400 · '잃을까?' 빨강 #FF2A2A · 1줄보다 크게 — 모두 두꺼운 검정 외곽선 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720). Cinematic digital painting, semi-realistic, very high contrast, dramatic, bold and readable at small size.
Upper 62% of the frame:
- Center-right: a Korean restaurant owner in his 50s living in Tokyo (fictional, not resembling any real person) sitting at a table in his small shop after closing, one hand covering his mouth, brows knitted, shoulders dropped, worried while looking at an official letter with blank lines; behind him the warm-lit restaurant interior. Warm light against deep shadows.
- Upper left: one bold tag, a solid bright red (#FF2A2A) rounded box with the Korean text "수수료 20배" printed in huge flat heavy bold white letters.
- Upper right: a bright yellow (#FFD400) speech bubble with the Korean text "2억 못 내면 떠나라?" in heavy bold black letters.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "재일교포도" — '재일교포도' 흰색, all with a thick black outline;
line 2 "영주권 잃을까?" — '영주권' 노랑 #FFD400 ; '잃을까?' 빨강 #FF2A2A ; 1줄보다 크게, all with a thick black outline, clearly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the person, the tag and the bubble in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text inside the central 16:9 area, at least 8% away from the top and bottom edges.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, spacing, comma, apostrophes and question mark, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## 9. SHORTS-OPEN — 쇼츠 첫 장면 (세 칸 · 문구 포함)

**저장 경로: `test/source/jaeil-yeongju-2026-10/images/SHORTS-OPEN.jpg`** — JPEG 700KB 이하

크기: **세로 9:16 (1080×1920) — 쇼츠 · 세 칸 (위 0~36% 순검정 + 문구 2줄 · 가운데 36~72% 그림 · 아래 72~100% 순검정, 글자·꼬리표는 높이 15~85%)**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위 1줄 | 재일교포도 일본 | '재일교포도' 흰색 · '일본' 흰색 — 검정 바탕 위 평면 글자 |
| 위 2줄 | 영주권 잃을까? | '영주권' 노랑 #FFD400 · '잃을까?' 빨강 #FF2A2A — 1줄과 같은 크기 |
| 그림 꼬리표 | 영주 수수료 20배 | 흰 글자 on 빨강 상자 #FF2A2A |

프롬프트:

```
Vertical YouTube Shorts opening frame, 9:16 portrait (1080x1920), high contrast.
LAYOUT — three full-width zones: 0–36% of the height flat solid pure black (#000000) with only the headline; 36–72% one cinematic digital painting edge to edge with straight top and bottom edges; 72–100% flat solid pure black, empty (subtitles will be added there later). No gradient, fade or border between the zones.
SAFE AREA: some feeds crop to about 4:5 — all text and the word tag stay between 15% and 85% of the height.
Headline: exactly TWO lines of very large heavy bold Korean text, the same letter size, EACH LINE CENTERED on the same axis, the longer line from about 4% to 96% of the width, the block between about 18% and 33% of the height and at least 3% above the painting; flat letters, no outline, no glow, no 3D.
line 1 "재일교포도 일본" — '재일교포도' 흰색 ; '일본' 흰색;
line 2 "영주권 잃을까?" — '영주권' 노랑 #FFD400 ; '잃을까?' 빨강 #FF2A2A.
Painting zone (36–72%): Cinematic digital painting, semi-realistic, warm late-afternoon light with soft shadows, muted earthy tones, subtle film grain. A small Korean restaurant in a Tokyo Korea-town street at dusk, its owner seen from behind holding an official envelope in front of the half-closed shutter, warm interior light spilling onto the street. No readable signs or text.
On the upper left of the painting (about 5–45% of the width, 39–47% of the height): one bold tag, a solid bright red (#FF2A2A) rounded box with the Korean text "영주 수수료 20배" printed in large flat heavy bold white letters on its flat front face (flat print, not carved or 3D). Keep the right 16% of the width below 45% of the height free of tags (Shorts buttons).
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536) with the same three zones and keep the headline between 12% and 88% of the width.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, spacing, comma and question mark, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
