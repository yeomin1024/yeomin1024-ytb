# bandeung-maesu-2026-11 쇼츠 — 실사 사진 6장 (배경 5 + 쇼츠 썸네일 1) · 얼굴 안 보임 · 글자 없음 (ChatGPT용)

작성: v1.0 — 2026-11-07 (Claude) — 사용자 지시 2026-11-07 "디자인은 이미지 요소를 써도 돼니까 좀 AI 모션 그래픽 티 안나게 해봐 배경도 좀 넣고 이미지 생성 명령도 알려줘"

쓰임: 쇼츠 「폭락 뒤 반등, 어떻게 사야 덜 잃을까」 (세 칸 — 위 두 줄 문구 · **가운데 칸 = 이 사진 위에 코드 그래프 카드** · 아래 자막). Claude 가 사진을 어둡게 깔고 천천히 확대하며
그 위에 그래프·수익률을 코드로 얹는다. 그래서 **사진 가운데~오른쪽은 비교적 단순하고 초점이 흐려야** 한다 (사람·물건은 왼쪽 1/3 쪽).
**색:** 한국 주식 앱처럼 **오르면 빨강 · 내리면 파랑**. 다른 편 썸네일(아침 지하철 · 주말 카페 창가 · 책상 위에서 내려다봄 · 새벽 창가 실루엣)과 장소·빛이 겹치지 않게.

| 번호 | 저장 경로 (JPEG 700KB 이하) | 크기 | 무엇 | 쓰는 대본 문장 |
|---|---|---|---|---|
| 1 | `stock/source/bandeung-maesu-2026-11/images/BG-HOOK.jpg` | 가로 1536×1024 | 비 오는 저녁 창턱 위 휴대전화 — 파랑으로 꺾였다 빨강으로 튀는 그래프 (사람 없음) | 1 |
| 2 | `stock/source/bandeung-maesu-2026-11/images/BG-ANT.jpg` | 가로 1536×1024 | 밤 원룸 침대 끝에 앉은 20대 뒷모습 · 휴대전화 빛 | 2 · 9 |
| 3 | `stock/source/bandeung-maesu-2026-11/images/BG-ANT-SELL.jpg` | 가로 1536×1024 | 손만 — 떨리는 엄지가 파란 매도 단추 위 (글자 없음) | 3 · 10~11 |
| 4 | `stock/source/bandeung-maesu-2026-11/images/BG-MASTER.jpg` | 가로 1536×1024 | 맑은 아침 서재 · 60대 어깨 너머 · 노트에 손으로 그린 계단 선 | 4~8 · 12 |
| 5 | `stock/source/bandeung-maesu-2026-11/images/BG-RESULT.jpg` | 가로 1536×1024 | 사람 없는 낮 책상 · 모니터 두 대에 작은 그래프 여러 개 (흐림) | 13~15 |
| 6 | `stock/source/bandeung-maesu-2026-11/shorts/thumbnails/TH-PHOTO.jpg` | 가로 1536×864 | 쇼츠 썸네일 가운데 칸 — 밤 편의점 앞 야외 탁자 · 어깨 너머 · 반등한 그래프 앞 멈칫한 엄지 | 0초 장면 (썸네일) |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트(종이 인형극, 다른 편 TH-PHOTO 포함)가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 1~6번 **6장을 번호 순서대로 모두** 만든다. 질문하지 말고 멈추지 말고 다음 장으로. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다. 화풍 문단을 따로 붙이지 않는다 (모두 실사).
3. **얼굴이 보이면 다시 만든다** (뒷모습·어깨 너머·손만). 실제 사람·연예인을 닮게 그리지 않는다.
4. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 화면은 그래프 모양과 색만, 글씨는 흐려서 읽히지 않게. 실제 증권사 앱·회사 로고를 닮게 그리지 않는다. 확대해 글자가 읽히면 다시 만든다.
5. **6장을 다 만든 뒤 나란히 놓고 본다** — 2번과 6번이 비슷하면(같은 밤 실내·같은 크기 뒷모습) 6번을 다시 만든다. 1·5번에는 사람이 없어야 한다.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다. 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다** — `yeomin1024/yeomin1024-ytb` main 브랜치, 표의 경로 그대로. **올리기 전에 JPEG 700KB 이하로** (RGB · 크기 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지) — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기가 내 파일과 같은지 확인. 커밋 메시지 `[stock] bandeung-maesu-2026-11 실사 배경·썸네일 사진 <번호>`.
   - **올리기가 실패한 장만** 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 1. BG-HOOK — 비 오는 저녁 창턱 위 휴대전화 (사람 없음)

**저장 경로: `stock/source/bandeung-maesu-2026-11/images/BG-HOOK.jpg`** — JPEG 700KB 이하 · 가로 1536×1024

```
Photorealistic background photo, landscape 3:2 (1536x1024), looks like a real candid photo taken with a 35mm lens, calm and believable — not exaggerated, no cartoon, no illustration, no 3D render look. Early evening, blue hour, rain on a large apartment window; city lights outside are soft round bokeh in deep navy and amber. On the left third of the frame, a smartphone lies face-up on the white windowsill, slightly angled toward the camera; its screen glows and shows only a simple stock line chart shape: a long steep fall drawn in blue, then one short sharp bounce drawn in red at the right end. No numbers, no letters, no app interface text, no logos anywhere on the screen or in the room. Raindrops and their soft shadows on the sill. The center and right half of the frame are mostly the out-of-focus rainy window and dark city bokeh, simple and uncluttered. Natural low light, slight film grain, shallow depth of field. No people.
```

## 2. BG-ANT — 밤 원룸 · 침대 끝에 앉은 20대 뒷모습

**저장 경로: `stock/source/bandeung-maesu-2026-11/images/BG-ANT.jpg`** — JPEG 700KB 이하 · 가로 1536×1024

```
Photorealistic background photo, landscape 3:2 (1536x1024), looks like a real candid photo, calm and believable — not exaggerated, no dramatic pose, no cartoon, no illustration. Late night inside a small, slightly messy Korean one-room studio apartment: a single bed with a wrinkled gray blanket, a folding drying rack with a few clothes, an empty instant noodle cup and an energy drink can on a small side table. A young man in his twenties wearing a light gray hoodie sits on the edge of the bed on the LEFT third of the frame, seen from behind and slightly to the side (back of head and shoulders only — his face is NOT visible), hunched forward, holding a smartphone close with both hands. The phone screen casts a cool blue light on his hands and hood; on the screen only a blurry candlestick chart shape with many blue falling candles and a couple of red candles, nothing readable. The only other light is a dim warm desk lamp out of frame. The center and right half of the frame are the dim, out-of-focus room wall and window blinds — simple, dark, uncluttered. Slight film grain, natural color, shallow depth of field. No text, no numbers, no logos anywhere.
```

## 3. BG-ANT-SELL — 손만 · 떨리는 엄지가 파란 매도 단추 위

**저장 경로: `stock/source/bandeung-maesu-2026-11/images/BG-ANT-SELL.jpg`** — JPEG 700KB 이하 · 가로 1536×1024

```
Photorealistic background photo, landscape 3:2 (1536x1024), real candid close-up, calm and believable — not exaggerated, no cartoon, no illustration. Extreme close-up of two hands holding a smartphone at night, positioned in the LEFT third of the frame; only hands and part of a gray hoodie sleeve are visible, no face. The right thumb hovers just above a large solid BLUE rounded button at the bottom of the phone screen, slightly tense, as if hesitating to press it; the rest of the screen shows a blurry blue downward line chart. The button and screen have no letters, no numbers, no icons, no logos. Cool blue screen light on the fingers, a dark blurred bedroom behind. The center and right half of the frame are a very dark, softly out-of-focus background, simple and uncluttered. Slight motion softness on the thumb, film grain, shallow depth of field. No text anywhere.
```

## 4. BG-MASTER — 맑은 아침 서재 · 60대 어깨 너머 · 노트의 손그림 계단 선

**저장 경로: `stock/source/bandeung-maesu-2026-11/images/BG-MASTER.jpg`** — JPEG 700KB 이하 · 가로 1536×1024

```
Photorealistic background photo, landscape 3:2 (1536x1024), looks like a real candid photo, calm and believable — not exaggerated, no cartoon, no illustration. A quiet, tidy home study on a clear morning: soft natural sunlight from a window on the left, wooden desk, a wall of books slightly out of focus. On the LEFT third of the frame, an older man in his sixties with neat gray hair and a navy knit cardigan sits at the desk, seen over his right shoulder from behind (face NOT visible). On the desk in front of him: an open paper notebook where he has drawn by pencil a few horizontal dashed lines and a simple descending staircase-shaped line with small dots at each step — only lines and dots, no letters, no numbers; a pencil, reading glasses, a white coffee cup; a closed laptop. Relaxed, patient posture, one hand resting on the notebook. The center and right half of the frame are the softly blurred bookshelves and warm sunlit wall, simple and uncluttered. Warm neutral colors (wood, cream, navy), gentle film grain, shallow depth of field. No readable text, no numbers, no logos anywhere.
```

## 5. BG-RESULT — 사람 없는 낮 책상 · 모니터 두 대 (흐림)

**저장 경로: `stock/source/bandeung-maesu-2026-11/images/BG-RESULT.jpg`** — JPEG 700KB 이하 · 가로 1536×1024

```
Photorealistic background photo, landscape 3:2 (1536x1024), real candid photo, calm and believable, no cartoon, no illustration, no 3D render look. A clean, modern home desk in soft overcast daylight, no people. Two monitors side by side, seen from a low angle slightly to the left; each screen shows a grid of many small, blurry line charts in red and blue — only shapes and colors, no numbers, no letters, no app interface. A mechanical keyboard, a small plant, a notebook closed. Muted gray-blue color palette with a few red and blue screen accents. The whole image is gently out of focus beyond the front edge of the desk so it works as a calm background; the center of the frame is simple. Film grain, natural light. No text, no numbers, no logos anywhere.
```

## 6. TH-PHOTO — 쇼츠 썸네일 가운데 칸 · 밤 편의점 앞 야외 탁자 · 어깨 너머

**저장 경로: `stock/source/bandeung-maesu-2026-11/shorts/thumbnails/TH-PHOTO.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Photorealistic YouTube thumbnail background photo, landscape 16:9 (1536x864), looks like a real candid photo, calm and believable — not exaggerated, no dramatic pose, no cartoon, no illustration. Late night outside a Korean convenience store: a small plastic outdoor table under bright white fluorescent light from the store window, wet asphalt reflecting light after rain, an umbrella leaning on the chair. Over-the-shoulder close-up from behind the left shoulder of a man in his thirties wearing a dark padded jacket (face NOT visible), holding a smartphone in his right hand; his thumb is frozen just above the screen, hesitating. The phone screen shows only a simple line chart: a long steep fall in blue, then a small sharp bounce up in red at the right end — no numbers, no letters, no logos, no app text. Keep the man's head and the phone screen inside the middle of the frame horizontally (between 38% and 66% of the width) and between 15% and 85% of the height. Cool white and deep navy colors with the red and blue of the screen as accents, slight film grain, shallow depth of field. No text, no numbers, no logos anywhere.
```

---
※ 연구·교육용 영상의 배경 사진 — 투자 권유가 아님.
