# bandeung-maesu-2026-11 롱폼 썸네일 그림 — 만스피 편처럼 만화 캐릭터 (1장 · ChatGPT용)

작성: v1.0 — 2026-11-12 — 사용자 지시 "썸네일은 이제 만스피처럼 할거니까 챗지피한테 생성할 명령 알려줘".
- 만스피 편 썸네일과 같은 길: **ChatGPT 만화 캐릭터 그림 1장(글자 없음)** + 문구는 Claude 가 코드(`video/render/thumb.mjs`)로 얹음. 영상(장면 v1.3)도 같은 그림체 · 같은 인물 V 라서 클릭한 뒤 화면과 이어짐.
- ⚠ 주식 롱폼 썸네일 기본 규칙(2026-11-03 '실사 · 얼굴 안 보임')과 다름 — 만스피 편처럼 사용자 지시로 만화 캐릭터, 얼굴이 보임.
- 문구 3안은 그대로 (upload.md v1.7 — 피드 시험 18회차): ① 「또 속는 거 아냐? / 팔자니 오를 것 같고」 ② 「30% 넘게 물렸는데 / 반등에 팔까 버틸까」 + 말풍선 「팔자니 오를 것 같고..」 ③ 「팔면 오를 것 같고 / 버티면 또 떨어지고」 · 꼬리표 「코스피 137번 중 98번」·「미국 83번 중 56번」(오른쪽 위).
  → 그림은 **'반등이 왔는데 매도할까 버틸까 망설이는 얼굴'** (손해를 이미 본 좌절보다 '또 속을까' 불안·갈등). 자리는 지금 썸네일과 같게: 아래 35% 큰 글자 두 줄 · 오른쪽 위 꼬리표.

| 번호 | 저장 경로 (JPEG 700KB 이하) | 크기 | 무엇 |
|---|---|---|---|
| 1 | `stock/source/bandeung-maesu-2026-11/images/TH-CHAR.jpg` | 가로 1536×864 | 밤 편의점 앞 · V 가 반등한 그래프를 보며 매도 단추 위에서 엄지가 멈칫 · 망설이는 얼굴 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트(실사 사진 TH-PHOTO 포함)가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
   **★ 먼저 기준 그림을 열어 본다 — 새 그림은 이 그림들과 같은 사람이 그린 것처럼 (그림체·선 굵기·색·얼굴 꼴·비율·옷까지 같게).**
   - 썸네일 그림체 (만스피 편 썸네일 — 왼쪽 곱슬머리·올리브색 재킷이 V. 왼쪽 위 '-50%' 글자는 따라 그리지 않음): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/1bcbf5532537e13ce5b1c1cd1402ffe328c59371/stock/source/manspi-jeonmang-2026-11/images/TH-CHAR.jpg
   - 인물 V: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/ca6e82abfeca0c5dd90591ad8d0a6cd5bbf34343/stock/source/manspi-jeonmang-2026-11/puppet/V-CALM.png · 고민하는 동작 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/c26185fd592f5ac4c99a082db5e6e197b05c4e85/stock/source/bandeung-maesu-2026-11/puppet/motion/V23.png · 휴대전화 든 모습 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/26f736388651c318e6676a7af80ac0dbf6062539/stock/source/bandeung-maesu-2026-11/puppet/motion/V26.png
   - 장소 (영상 첫 장면 — 이 편의점 앞을 같은 모습으로): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/f44ece384111d5d527c53b5776e117edca9bf058/stock/source/bandeung-maesu-2026-11/puppet/BG-STORE.jpg
   그림을 열 수 없으면 아래 설명대로 그린다.
1. 아래 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 써서 **1장**을 만든다. 질문하지 말고 바로 만든다.
2. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 간판·유리창·상품·휴대전화 화면에도 없음 (화면은 그래프 선과 빈 단추만). 실제 편의점·증권사·앱의 이름·로고·색 조합을 닮게 그리지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.
3. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. stock/source/bandeung-maesu-2026-11/images/TH-CHAR.jpg`). 그림 안에는 쓰지 않는다.
4. **저장소에 넣는다** — `yeomin1024/yeomin1024-ytb` main 브랜치, 경로 `stock/source/bandeung-maesu-2026-11/images/TH-CHAR.jpg`. **올리기 전에 JPEG 700KB 이하로** (RGB · 크기 1536×864 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지) — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기가 내 파일과 같은지 확인. 커밋 메시지 `[stock] bandeung-maesu-2026-11 TH-CHAR.jpg 이미지`. 올린 주소를 알려 준다.
   - **올리기가 실패하면** 그림을 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 저장 경로에 올립니다."**

## 1. TH-CHAR — 밤 편의점 앞 · 반등에 매도할까 버틸까 망설임

**저장 경로: `stock/source/bandeung-maesu-2026-11/images/TH-CHAR.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
YouTube thumbnail illustration, landscape 16:9 (1536x864), full-bleed — no border, no frame. Match exactly the art style of the reference thumbnail and reference character sheets: a polished flat 2D cartoon with bold clean dark outlines, flat colors with one simple cel-shading tone and small highlights, expressive exaggerated face, easy to read on a small phone screen. It is a 2D drawing — not a 3D render, not a photo.

CHARACTER: only one person — V from the reference sheets, exactly the same face, messy curly medium-brown hair, olive-green casual button jacket with flap pockets over a beige checked shirt, brown trousers. Do not invent a new character.

SCENE: late night just after rain, in front of the same small convenience store as the reference background picture: glowing glass window with softly blurred colorful shelves (color shapes only, no labels), a plain dark awning with no sign text, wet shiny pavement with warm reflections and a few puddles. V stands on the sidewalk, upper body large in the frame (from the waist up), holding a smartphone in his right hand at chest height, the screen tilted toward the viewer so it is clearly visible. On the phone screen: a simple line chart — a long steep fall drawn in blue, then one short sharp bounce up drawn in red at the right end — and below it one large plain solid BLUE rounded button with nothing written on it. His right thumb hovers just above the blue button, frozen, not pressing it. His left hand is raised beside his head, fingers touching his temple. His face is torn and anxious, not crying: eyebrows knitted and raised in the middle, eyes darting sideways at the red bounce, lips pressed and pulled to one side, one small light-blue sweat drop on his forehead — the feeling "if I sell now it may go up, if I hold it may fall again".

COMPOSITION:
- V's head and the phone are inside the horizontal 22%–60% of the width and the vertical 8%–62% of the height; his face is NOT in the bottom 35% of the picture.
- The top-right area (from 63% to 97% of the width, from the top down to 46% of the height) is calm, out-of-focus background only — the store window corner and the dark rainy street — no face, no hands, no phone there (small labels will be placed there later).
- The bottom 35% of the picture is simple: his jacket body and the dark wet pavement, no important details (two lines of large text will be placed there later).
- Cool night blue around him, warm light from the store window on one side of his face, the red and blue of the phone screen as the brightest accents. Calm and believable — no lightning, no explosions, no tears flood, no exaggerated effects.

FORBIDDEN: absolutely no text, letters, numbers, logos or watermarks anywhere — not on the awning, the window, the products, the phone screen, the button or anywhere else.
```

## 받은 뒤 (Claude)
- 확대해서 검수: V 가 영상·만스피 편과 같은 사람인지 · 그림 속 글자·로고 없음 · 머리·휴대전화 자리(가로 22~60% · 세로 8~62%) · 오른쪽 위(꼬리표 자리)와 아래 35%(큰 글자 자리)가 비었는지 · 망설이는 얼굴인지.
- `thumbnails/thumbnail_{1,2,3}.json` 의 그림을 `../images/TH-CHAR.jpg` 로 바꿔 `thumb.mjs` 로 다시 그림 — 문구·꼬리표 자리는 그림의 빈 자리에 맞춤 · 보조 문구는 사람을 가리지 않게 (quick_board 규칙 47).
- 짝 쇼츠를 다시 만들면 첫 장면(세 칸 band 가운데 칸)에도 같은 그림 (`tools/cover_check.py`).

---
※ 연구·교육용 영상의 썸네일 그림 — 투자 권유가 아님.
