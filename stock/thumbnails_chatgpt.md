# stock 썸네일 4장 — ChatGPT용 (모든 영상 · 읽고 그대로 만들고 각 저장 경로에 올리기)

자동 생성 — `python tools/make_summary.py --chatgpt-all stock` (2026-10-23 08:34). 이 파일은 고치지 말고 영상마다 `thumbnail_N.md`를 고친 뒤 다시 만든다.

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/stock/thumbnails_chatgpt.md

| 영상 | 만들 시안 | 저장 폴더 |
|---|---|---|
| pogi-sonjeol-2026-10 | thumbnail_1, thumbnail_2, thumbnail_3 | `stock/source/pogi-sonjeol-2026-10/thumbnails/` |
| pogi-sonjeol-2026-10-shorts | thumbnail_1 | `stock/source/pogi-sonjeol-2026-10/shorts/thumbnails/` |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 썸네일 파일·프롬프트가 있어도 쓰지 않는다 (2026-10-17 옛 프롬프트로 4장을 다시 그린 일이 있었음). 답의 첫 줄에 이 파일 맨 위 '자동 생성' 줄의 시각을 그대로 적는다 (Claude 가 어느 판으로 그렸는지 확인).
1. 아래 썸네일 4장(2개 영상)을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다. 장마다 서로 다른 그림이다 — 앞 장의 인물·구도·색을 이어 쓰지 않는다.
3. 크기는 **장마다 '크기' 줄대로**: 롱폼 썸네일 = 가로형 16:9 (1280×720 — 안 되면 가장 넓은 가로형, 그림은 끝까지, 글자와 얼굴은 가운데, 위아래 8%에는 두지 않음) · **쇼츠 썸네일(영상 ID 끝이 `-shorts`) = 세로형 9:16 (1080×1920)** — **사진 한 장이 네 가장자리까지 꽉 찬다 — 빈 남색·검정 띠, 테두리, 여백, 가운데만 사진인 꼴은 안 된다** (v1.8.0 — 띠가 있으면 영상에서 비율이 틀린 것처럼 보임). 프롬프트가 '글자·얼굴을 두지 않는 자리'(위·오른쪽·아래)를 말해도 그 자리에도 사진(배경·앞쪽 물건)이 이어진다. 안 되면 세로 2:3, 그때는 글자와 얼굴을 가운데에 두고 2:3 그림의 양옆 8%에는 두지 않음 (잘리는 자리 — 사진은 이어짐).
4. 그림 속 글자는 프롬프트의 따옴표 안 글자만(한글, 그리고 프롬프트가 적은 영문 — 예: ISA), 글자·띄어쓰기·조사 그대로 쓴다 (조사 하나도 빼거나 바꾸지 않는다 — '세금으로'를 '세금'으로 줄이면 뜻이 달라짐). **줄 수·줄바꿈·정렬·글자 크기도 프롬프트대로** — 프롬프트가 '2줄, 줄마다 가운데, 긴 줄이 너비 4~96%'라고 하면 그만큼 크게·가운데로, 작게 줄이거나 한쪽으로 몰지 않는다 (v1.8.4·v1.9.0). 다른 글자·숫자·로고·워터마크는 넣지 않는다.
5. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다. **표정·몸짓은 프롬프트에 적힌 그대로** — 손해를 알고 좌절한 장면을 놀란 얼굴·담담한 얼굴·웃는 얼굴로 바꾸지 않고, 작은 화면에서도 그 감정이 보이게 그린다 (v1.8.3).
6. 한 장을 만들 때마다 그 칸의 '문구' 표와 그림 속 한글을 한 글자씩 맞춰 본다. 크게 확대해서 받침과 모음 획(예: '료'의 ㄹ, '보'의 ㅗ)·조사(예: '1년에'의 '에', '세금으로'의 '으로')가 빠지거나 가려지지 않았는지도 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다. 쇼츠 그림(세로)은 **그 장의 배치대로인지**도 본다 — '세 칸'이면 위·아래 칸이 순검정·사진 칸이 가로 끝까지·문구 2줄이 줄마다 가운데(어긋남 없음)·사진과 붙지 않음·글자와 얼굴이 높이 15~85% 안, 그 밖(사진 끝까지)이면 빈 남색·검정 띠가 없는지. 다르면 다시 만든다 (v1.8.0·v1.9.0).
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `3. stock/source/pogi-sonjeol-2026-10/thumbnails/thumbnail_3.jpg`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게 (`thumbnail_N.jpg`).
   - **올리기 전에 JPEG(.jpg)로 바꿔 700KB 이하로 만든다** — 파이썬(PIL)으로 RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장. GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다 (2026-10-19 PNG 4장이 786,444바이트에서 잘려 열리지 않음). 올린 뒤 GitHub 에 있는 그 파일의 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
   - **GitHub 앱으로 장마다 그 경로에 커밋한다** — 이 계정의 ChatGPT 는 저장소에 파일을 올릴 수 있다 (2026-10-19 사용자 확인). 커밋 메시지: `[썸네일] <영상ID> thumbnail_N 이미지`. 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 이 파일의 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"이 그림 4장을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 thumbnail_N.jpg 이름으로 내려받아 폴더마다 아래 링크에 끌어다 놓고 Commit changes" + 아래 '폴더별 올리기 링크' 목록

## 폴더별 올리기 링크 (ChatGPT가 못 올릴 때 사람이 쓰는 길)

- pogi-sonjeol-2026-10: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/pogi-sonjeol-2026-10/thumbnails
- pogi-sonjeol-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/pogi-sonjeol-2026-10/shorts/thumbnails

## 1. pogi-sonjeol-2026-10 · thumbnail_1 — 롱폼 (본안)

**저장 경로: `stock/source/pogi-sonjeol-2026-10/thumbnails/thumbnail_1.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

크기: 가로 16:9 (1280×720) — 롱폼

프롬프트:

```
STYLE: paper-cut puppet theater (layered papercraft), like a hand-made paper puppet show. Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited calm palette: deep indigo #1E2A4A, warm cream #F2E6CF, charcoal #2B2B2B, gold ochre #D9A441, muted crimson #B3202A, soft teal #3E8E87, plus the character colors below. Flat stage view, like a stage seen from the audience. People are paper puppets WITH clearly readable facial expressions: every face is built from small cut-paper pieces — almond-shaped dark eyes with a tiny white highlight, thin dark-brown paper eyebrows, a simple mouth cut from darker paper, and soft pink paper cheek circles. The expression must read at a glance even when the picture is small. Fictional people, not recognizable as any real person. Modern everyday Korean life today.
CHARACTER (exactly the same paper puppet in every image — same face shape, proportions and paper colors; only the pose and the expression change): Gu Bonseok, a 44-year-old Korean office worker. Average height with a slightly soft build and a small round belly; his head is about one sixth of his height. Kind round face of warm beige skin paper #E8C39E, with the cut-paper face described in STYLE: dark almond eyes, thick-ish dark-brown eyebrows, a simple mouth, soft pink cheeks, slightly tired faint shadows under the eyes. Thin black rectangular glasses frames sit over his eyes (the eyes stay visible through the frames). Short neat black hair paper #1F1F1F parted on the left, a few light gray paper strands #A6A6A6 at the temples, and ONE small upturned cowlick sticking up at the crown. Gray-navy zip-up work jacket #3B4763 with no logo and a slightly lighter collar, over a light blue collared shirt #AFC6E3; dark charcoal-gray slacks #4A4D52; black sneakers #222222 with thin white soles.
SCENE: a paper puppet theater stage; the backdrop is a small Korean apartment living room at night — sofa, low table, a window with distant apartment lights, deep indigo tones. Gu Bonseok puppet holding a smartphone and staring at its screen, having just realized he lost the money — knitted eyebrows, eyes wide with dismay, mouth slightly open, shoulders slumped (a defeated, frustrated face, not a frozen surprised face), on the left half, facing slightly right, his whole upper body large, about 60% of the picture height.
TEXT: numbers and symbols only — NO words or letters of any language (no English, no Korean), exactly these characters, very large bold rounded numerals with a thick dark navy outline, one line across the bottom, 60–90% of the width: line 1 "−70%" in muted-red #E0302A. Nothing else written except the tag.
TAG: a small rounded navy tag "#1" with yellow characters in the top-left corner.
FORMAT: landscape 16:9 (1280×720). Save as JPEG (.jpg) under 700 KB.
```

## 2. pogi-sonjeol-2026-10 · thumbnail_2 — 롱폼 (실험안)

**저장 경로: `stock/source/pogi-sonjeol-2026-10/thumbnails/thumbnail_2.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

크기: 가로 16:9 (1280×720) — 롱폼

프롬프트:

```
STYLE: paper-cut puppet theater (layered papercraft), like a hand-made paper puppet show. Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited calm palette: deep indigo #1E2A4A, warm cream #F2E6CF, charcoal #2B2B2B, gold ochre #D9A441, muted crimson #B3202A, soft teal #3E8E87, plus the character colors below. Flat stage view, like a stage seen from the audience. People are paper puppets WITH clearly readable facial expressions: every face is built from small cut-paper pieces — almond-shaped dark eyes with a tiny white highlight, thin dark-brown paper eyebrows, a simple mouth cut from darker paper, and soft pink paper cheek circles. The expression must read at a glance even when the picture is small. Fictional people, not recognizable as any real person. Modern everyday Korean life today.
CHARACTER (exactly the same paper puppet in every image — same face shape, proportions and paper colors; only the pose and the expression change): Gu Bonseok, a 44-year-old Korean office worker. Average height with a slightly soft build and a small round belly; his head is about one sixth of his height. Kind round face of warm beige skin paper #E8C39E, with the cut-paper face described in STYLE: dark almond eyes, thick-ish dark-brown eyebrows, a simple mouth, soft pink cheeks, slightly tired faint shadows under the eyes. Thin black rectangular glasses frames sit over his eyes (the eyes stay visible through the frames). Short neat black hair paper #1F1F1F parted on the left, a few light gray paper strands #A6A6A6 at the temples, and ONE small upturned cowlick sticking up at the crown. Gray-navy zip-up work jacket #3B4763 with no logo and a slightly lighter collar, over a light blue collared shirt #AFC6E3; dark charcoal-gray slacks #4A4D52; black sneakers #222222 with thin white soles.
SCENE: a paper puppet theater stage; the backdrop is a small Korean apartment living room at night — sofa, low table, a window with distant apartment lights, deep indigo tones. Gu Bonseok puppet sitting slumped on the floor with one hand on his forehead and head bowed, eyes shut tight, deeply frustrated and defeated after the loss, on the left half, facing slightly right, his whole upper body large, about 60% of the picture height.
TEXT: numbers and symbols only — NO words or letters of any language (no English, no Korean), exactly these characters, very large bold rounded numerals with a thick dark navy outline, one line across the bottom, 60–90% of the width: line 1 "−70%" in muted-red #E0302A. Nothing else written except the tag.
TAG: a small rounded navy tag "#1" with yellow characters in the top-left corner.
FORMAT: landscape 16:9 (1280×720). Save as JPEG (.jpg) under 700 KB.
```

## 3. pogi-sonjeol-2026-10 · thumbnail_3 — 롱폼 (실험안)

**저장 경로: `stock/source/pogi-sonjeol-2026-10/thumbnails/thumbnail_3.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

크기: 가로 16:9 (1280×720) — 롱폼

프롬프트:

```
STYLE: paper-cut puppet theater (layered papercraft), like a hand-made paper puppet show. Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited calm palette: deep indigo #1E2A4A, warm cream #F2E6CF, charcoal #2B2B2B, gold ochre #D9A441, muted crimson #B3202A, soft teal #3E8E87, plus the character colors below. Flat stage view, like a stage seen from the audience. People are paper puppets WITH clearly readable facial expressions: every face is built from small cut-paper pieces — almond-shaped dark eyes with a tiny white highlight, thin dark-brown paper eyebrows, a simple mouth cut from darker paper, and soft pink paper cheek circles. The expression must read at a glance even when the picture is small. Fictional people, not recognizable as any real person. Modern everyday Korean life today.
CHARACTER (exactly the same paper puppet in every image — same face shape, proportions and paper colors; only the pose and the expression change): Gu Bonseok, a 44-year-old Korean office worker. Average height with a slightly soft build and a small round belly; his head is about one sixth of his height. Kind round face of warm beige skin paper #E8C39E, with the cut-paper face described in STYLE: dark almond eyes, thick-ish dark-brown eyebrows, a simple mouth, soft pink cheeks, slightly tired faint shadows under the eyes. Thin black rectangular glasses frames sit over his eyes (the eyes stay visible through the frames). Short neat black hair paper #1F1F1F parted on the left, a few light gray paper strands #A6A6A6 at the temples, and ONE small upturned cowlick sticking up at the crown. Gray-navy zip-up work jacket #3B4763 with no logo and a slightly lighter collar, over a light blue collared shirt #AFC6E3; dark charcoal-gray slacks #4A4D52; black sneakers #222222 with thin white soles.
SCENE: a paper puppet theater stage; the backdrop is a small Korean apartment living room at night — sofa, low table, a window with distant apartment lights, deep indigo tones. Gu Bonseok puppet holding a smartphone and staring at its screen, having just realized he lost the money — knitted eyebrows, eyes wide with dismay, mouth slightly open, shoulders slumped (a defeated, frustrated face, not a frozen surprised face), on the left half, facing slightly right, a close-up of his head and shoulders filling about 70% of the height.
TEXT: numbers and symbols only — NO words or letters of any language (no English, no Korean), exactly these characters, very large bold rounded numerals with a thick dark navy outline, one line across the bottom, 60–90% of the width: line 1 "−70%" in muted-red #E0302A. Nothing else written except the tag.
TAG: a small rounded navy tag "#1" with yellow characters in the top-left corner.
FORMAT: landscape 16:9 (1280×720). Save as JPEG (.jpg) under 700 KB.
```

## 4. pogi-sonjeol-2026-10-shorts · thumbnail_1 — 쇼츠 (쇼츠)

**저장 경로: `stock/source/pogi-sonjeol-2026-10/shorts/thumbnails/thumbnail_1.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

크기: **세로 9:16 (1080×1920) — 쇼츠**

프롬프트:

```
STYLE: paper-cut puppet theater (layered papercraft), like a hand-made paper puppet show. Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited calm palette: deep indigo #1E2A4A, warm cream #F2E6CF, charcoal #2B2B2B, gold ochre #D9A441, muted crimson #B3202A, soft teal #3E8E87, plus the character colors below. Flat stage view, like a stage seen from the audience. People are paper puppets WITH clearly readable facial expressions: every face is built from small cut-paper pieces — almond-shaped dark eyes with a tiny white highlight, thin dark-brown paper eyebrows, a simple mouth cut from darker paper, and soft pink paper cheek circles. The expression must read at a glance even when the picture is small. Fictional people, not recognizable as any real person. Modern everyday Korean life today.
CHARACTER (exactly the same paper puppet in every image — same face shape, proportions and paper colors; only the pose and the expression change): Gu Bonseok, a 44-year-old Korean office worker. Average height with a slightly soft build and a small round belly; his head is about one sixth of his height. Kind round face of warm beige skin paper #E8C39E, with the cut-paper face described in STYLE: dark almond eyes, thick-ish dark-brown eyebrows, a simple mouth, soft pink cheeks, slightly tired faint shadows under the eyes. Thin black rectangular glasses frames sit over his eyes (the eyes stay visible through the frames). Short neat black hair paper #1F1F1F parted on the left, a few light gray paper strands #A6A6A6 at the temples, and ONE small upturned cowlick sticking up at the crown. Gray-navy zip-up work jacket #3B4763 with no logo and a slightly lighter collar, over a light blue collared shirt #AFC6E3; dark charcoal-gray slacks #4A4D52; black sneakers #222222 with thin white soles.
SCENE: a paper puppet theater stage; the backdrop is a small Korean apartment living room at night — sofa, low table, a window with distant apartment lights, deep indigo tones. Gu Bonseok puppet holding a smartphone and staring at its screen, having just realized he lost the money — knitted eyebrows, eyes wide with dismay, mouth slightly open, shoulders slumped (a defeated, frustrated face, not a frozen surprised face), in the middle, the text above him in the upper third, his whole upper body large, about 60% of the picture height.
TEXT: numbers and symbols only — NO words or letters of any language (no English, no Korean), exactly these characters, very large bold rounded numerals with a thick dark navy outline, one line in the upper part: line 1 "−70%" in muted-red #E0302A. Nothing else written except the tag.
TAG: a small rounded navy tag "#1" with yellow characters in the top-left corner.
FORMAT: vertical 9:16 (1080×1920), the picture fills the whole frame to every edge — no empty bands. Save as JPEG (.jpg) under 700 KB.
```
