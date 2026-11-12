# bandeung-maesu-2026-11 롱폼 — 만화 무대·움직임 그림 17장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.0 — 2026-11-12 — 사용자 지시 "오디오 만들었으니 반등 영상 만들어봐" → 화면 방식 질문에 "만스피처럼 만화 인물". 기준 대본 = main 커밋 29521c16 의 `bandeung-maesu-2026-11.txt` (도입 v7.2 · 8장 129문장 · 오디오 9:13).

**어떻게 쓰는가 — 만스피 편과 같은 코드 애니메이션**
- Claude 가 코드로 만든다: 배경 그림 위에 인물·소품 조각을 올리고, **동작마다 이어지는 원화 3장**(키 → 중간 → 키)을 초당 8~12장으로 바꿔 끼워 팔·몸·얼굴이 실제로 움직이게 한다. 숫자·BUY·SELL·그래프·카드 글자는 그림 속 빈 판·빈 칸 위에 코드가 얹는다.
- 주인공은 **만스피 편의 시청자 V 그대로** (같은 얼굴·머리·옷). 만스피 편에서 이미 받은 V 동작(밤 휴대전화 V04 · 화나서 걸음 V05 · 돋보기 V13 · 매수 손목 붙잡기 V14 · 지쳐 기다림 V15 · 메모·끄덕 V16 · 인사 V17 · 저금통 V01)은 **다시 그리지 않는다** — 이 파일은 반등 편에만 필요한 것만.
- **무대는 만스피 편과 겹치지 않게 새로** (유튜브 '반복 콘텐츠' 정책 — 주식 규칙 43): 밤 편의점 앞 · 같은 곳 새벽 · 기록 보관실 · 돌계단 광장 · 지하철 승강장.

| 번호 | 저장 경로 (모두 `stock/source/bandeung-maesu-2026-11/puppet/` 아래) | 무엇 | 대본 문장 |
|---|---|---|---|
| 1 | `BG-STORE.jpg` | 배경: 비 그친 밤, 편의점 앞 (플라스틱 탁자·의자 · 젖은 바닥) | 1~3 · 7~8 · 33~35 · 69~75 |
| 2 | `BG-DAWN.jpg` | 배경: 1번과 같은 곳 · 새벽 | 115~129 |
| 3 | `BG-ARCHIVE.jpg` | 배경: 기록 보관실 (가운데 큰 빈 게시판 · 앞쪽 긴 책상) | 4~6 · 9~17 · 24~32 · 38~57 · 76~114 |
| 4 | `BG-STAIRS.jpg` | 배경: 광장의 넓은 돌계단 (옆에서 봄 · 왼쪽 위 → 오른쪽 아래) | 18~23 · 36~37 |
| 5 | `BG-PLATFORM.jpg` | 배경: 빈 지하철 승강장 (옆에서 봄 · 가운데 선로) | 58~68 |
| 6 | `motion/V18.png` | V: 큰 장부를 펴 들고 읽음 → 한 장 넘김 → 고개를 들고 놀람 | 13~17 · 36 |
| 7 | `motion/V19.png` | V: 왼쪽 게시판을 검지로 가리킴 → 카메라를 보며 손바닥 펴고 말함 → 같은 자세 입 다묾 | 데이터 장면 전체 |
| 8 | `motion/V20.png` | V: 아래를 보며 기대 → 위로 따라 보며 눈 반짝 → 다시 아래, 실망해 어깨 처짐 | 18~23 |
| 9 | `motion/V21.png` | V: 주머니에 손 넣고 기다림 → 오른쪽으로 팔을 뻗으며 "잠깐!" → 팔을 떨구고 뒷머리를 짚으며 후회 | 58~68 |
| 10 | `motion/V22.png` | V: 꽉 찬 동전 병과 빈 병을 듦 → 반을 빈 병에 붓기 → 반씩 찬 두 병을 같은 높이로 들고 차분히 | 10 · 72~73 · 85~88 · 99~102 |
| 11 | `motion/V23.png` | V: 왼손바닥을 보며 고민 → 오른손바닥을 보며 고민 → 두 손으로 머리를 감싸 쥠 | 7~8 · 74 · 103~105 · 116 |
| 12 | `motion/V24.png` | V: 베개를 안고 잠 못 이룸 → 크게 하품 → 베개를 내리고 눈 감고 안도 | 100 |
| 13 | `motion/V25.png` | V: 옆모습 걷기 3장 (지친 얼굴 · 오른쪽으로 걸어감) | 36~37 · 42~46 |
| 14 | `motion/V26.png` | V: 휴대전화를 보며 풀 죽음 → 고개를 들고 놀란 듯 안도 → 가슴에 손을 얹고 옅은 미소 | 33~34 · 106 |
| 15 | `motion/PROPS-B.png` | 소품 4: 고무공 · 압정 꽂힌 빈 카드 · 빈 초시계 · 빈 유리병 | 18~23 · 카드 · 95~98 |
| 16 | `motion/TRAIN.png` | 지하철 객차 한 칸 (옆모습 · 오른쪽을 향함) | 59~68 |
| 17 | `motion/BLDG.png` | 회사 건물 4채 (모양이 다른 빌딩 · 로고 없음) | 52~56 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트(실사 사진·종이 인형극 포함)가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
   **★ 먼저 기준 그림을 열어 본다 — 새 그림은 모두 이 그림들과 같은 사람이 그린 것처럼 (그림체·선 굵기·색·얼굴 꼴·비율·옷까지 같게). 인물 크기도 이 동작 시트들과 같게.**
   - 시청자 V (만스피 편): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/ca6e82abfeca0c5dd90591ad8d0a6cd5bbf34343/stock/source/manspi-jeonmang-2026-11/puppet/V-CALM.png · 동작 시트 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/c412f51386184ee1da397840117ba49e8db3a408/stock/source/manspi-jeonmang-2026-11/puppet/motion/V04.png · https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/93e68393dbff118c6a6b14db0503fe30e56f190e/stock/source/manspi-jeonmang-2026-11/puppet/motion/V16.png
   - 배경 그림체 (만스피 편 — 이 장소들은 따라 그리지 않음, 그림체·빛·선만): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/8e67c85fe803b9ed8720e5a0953aece4d72118d5/stock/source/manspi-jeonmang-2026-11/puppet/BG-NIGHT.jpg · https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/d455e9f4f1d66d0370fe083552c7b99ff6ce06cb/stock/source/manspi-jeonmang-2026-11/puppet/BG-STUDIO.jpg
   - 썸네일 그림체: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/1bcbf5532537e13ce5b1c1cd1402ffe328c59371/stock/source/manspi-jeonmang-2026-11/images/TH-CHAR.jpg (왼쪽 '-50%' 글자는 따라 그리지 않음)
   그림을 열 수 없으면 아래 '공통 화풍'과 '인물' 설명대로 그린다.
1. 아래 1~17번 **17장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 **공통 화풍** 문단을 붙인다.
   - **1~5번(배경)**: 공통 화풍 → **배경판** → 프롬프트. 2번은 **1번 그림을 편집해서** 만든다 (구도·물건·자리를 그대로 두고 시간·빛만 바꿈). 편집이 안 되면 1번과 같은 구도로 새로 그린다.
   - **6~14번(동작 그림)**: 공통 화풍 → **인물** → **CUTOUT** → **MOTION STRIP** → 프롬프트.
   - **15~17번(소품)**: 공통 화풍 → **CUTOUT** → 프롬프트.
3. **6~14번은 한 장에 같은 사람을 3번** 그린다 — 왼쪽 → 가운데 → 오른쪽이 **한 동작을 이어 그린 3장**(애니메이션 원화)이다. 세 사람이 **같은 크기·같은 자리·같은 방향·같은 옷**이고, **발바닥이 같은 높이**에 있고, **움직이는 부분(팔·손·머리·얼굴·상체 기울기·손에 든 물건)만** 바뀐다. 손에 든 물건은 세 장 모두 같은 모양·같은 크기. 서로 겹치거나 칸(가로 3등분)을 넘지 않는다. 다른 사람·배경·바닥 그림자는 없다.
4. **검사 (6~17번 필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`·`칸 넘음`·`발 높이 다름`이면 고쳐서 다시 만든다 (더 작게 · 여백을 넓게 · 발을 같은 선에). **투명이 아니면 배경을 순자홍 #FF00FF 한 색 평면으로 다시 만든다.**
   ```python
   from PIL import Image
   import numpy as np
   def filled_mask(a):
       if a[2, 2, 3] > 0:                        # 투명이 아니면 순자홍 바탕을 빈 곳으로 봄
           r, g, b = (a[:, :, i].astype(int) for i in range(3))
           return ~((r > 200) & (b > 200) & (g < 90))
       return a[:, :, 3] > 40
   def check(path, cols, rows=1, margin=0.04, gap=0.012, feet=None):
       a = np.array(Image.open(path).convert("RGBA"))
       h, w = a.shape[:2]
       m = filled_mask(a)
       ys, xs = np.where(m)
       box = (xs.min() / w, ys.min() / h, xs.max() / w, ys.max() / h)
       bad = []
       if not (box[0] >= margin and box[1] >= margin and box[2] <= 1 - margin and box[3] <= 1 - margin):
           bad.append("잘림")
       for c in range(1, cols):                  # 칸 경계 둘레는 비어 있어야 함
           x = int(w * c / cols); d = int(w * gap)
           if m[:, x - d:x + d].any(): bad.append(f"칸 넘음 세로 {c}")
       for r in range(1, rows):
           y = int(h * r / rows); d = int(h * gap)
           if m[y - d:y + d, :].any(): bad.append(f"칸 넘음 가로 {r}")
       if feet:                                  # 동작 그림: 세 사람의 발바닥 높이가 같아야 함
           bottoms = []
           for c in range(cols):
               ys_c = np.where(m[:, w * c // cols:w * (c + 1) // cols].any(axis=1))[0]
               bottoms.append(ys_c.max() / h)
           if max(bottoms) - min(bottoms) > 0.02: bad.append(f"발 높이 다름 {[round(v, 3) for v in bottoms]}")
       print(path, "OK" if not bad else f"다시 — {bad}", [round(float(v), 3) for v in box])
       return not bad
   # 6~14번: check(경로, cols=3, feet=True) · 15번·17번: check(경로, cols=4, margin=0.02) · 16번: check(경로, cols=1, margin=0.03)
   ```
5. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 편의점 간판·유리창·상품·승강장 벽·안내판·객차·장부·카드·초시계·건물에도 없음 (빈 판이나 단순한 줄·도형만). 실제 편의점·지하철·회사·은행·앱의 이름·로고·색 조합을 닮게 그리지 않는다. 동전은 무늬 없는 금화. 하늘·해·구름·비 내리는 줄은 그리지 않는다 (젖은 바닥·물웅덩이는 됨). 만든 뒤 확대해 글자가 보이면 다시 만든다.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. stock/source/bandeung-maesu-2026-11/puppet/BG-STORE.jpg`). 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게 — 1~5번은 `stock/source/bandeung-maesu-2026-11/puppet/`, 6~17번은 `stock/source/bandeung-maesu-2026-11/puppet/motion/`).
   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     - 1~5번(JPEG): RGB · 크기 1536×864 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.
     - 6~17번(PNG, 투명 유지): 아래 코드 그대로.
       ```python
       from PIL import Image
       import os
       Q = getattr(Image, "Quantize", Image).FASTOCTREE
       def save_png(src, dst, limit=700_000):
           im = Image.open(src).convert("RGBA")
           w, h = im.size
           s = min(1.0, 1536 / max(w, h))
           while True:
               cur = im.resize((round(w * s), round(h * s)), Image.LANCZOS) if s < 1 else im
               cur.save(dst, optimize=True)
               if os.path.getsize(dst) > limit:
                   cur.quantize(colors=256, method=Q).save(dst, optimize=True)   # 256색 (투명 유지)
               if os.path.getsize(dst) <= limit or max(cur.size) <= 900:
                   break
               s *= 0.9
           print(dst, os.path.getsize(dst), cur.size)
       ```
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[stock] bandeung-maesu-2026-11 long <파일 이름> 이미지` (예: `[stock] bandeung-maesu-2026-11 long BG-STORE.jpg 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 공통 화풍 (1~17번 모든 프롬프트 맨 앞에 그대로 붙임 — 기준 그림과 같은 그림체)

```
STYLE: Match exactly the art style of the reference thumbnail image, the reference character sheets and the reference background pictures: a polished flat 2D cartoon illustration with bold clean dark outlines, flat colors with one simple cel-shading tone and small highlights, warm cozy lighting mixed with cool blue screen or night glow, expressive exaggerated faces (big eyes, clear eyebrows, open mouths, tears when sad) and easy-to-read body language for a small phone screen. Slightly chunky proportions (head about one quarter of the body height). It is a 2D drawing — not a 3D render, not clay or plastic, not a photo. Absolutely no text, letters, numbers, logos or watermarks anywhere — signs, shop windows, products, boards, cards, books, phones, clocks, trains and buildings are blank or show only simple lines and shapes. No sky, no sun, no clouds, no falling rain lines.
```

## 배경판 (1~5번 — 공통 화풍 다음에 그대로 붙임)

```
BACKGROUND PLATE for a 2D animation: full-bleed landscape 1536x864, eye-level camera, NO people and no animals anywhere. Leave a clear, flat, empty floor area in the front-center of the picture where cartoon characters will be placed later: a standing adult there would be about 75% of the picture height, feet near 92% of the height. Keep the middle of the picture calm and uncluttered. Same drawing style, outline weight and color richness as the reference background pictures.
```

## 인물 (6~14번 — 공통 화풍 다음에 그대로 붙임)

```
CHARACTER — draw him exactly like the reference character sheets, same face, hair, clothes, colors and proportions in every frame:
V — an ordinary Korean man around 40 who invested his savings: messy curly medium-brown hair, an olive-green casual button jacket with flap pockets over a beige checked shirt, brown trousers with a brown belt, brown shoes. A kind, emotional face that shows feelings strongly (worry, hope, disappointment, relief).
```

## CUTOUT (6~17번 — 그다음에 그대로 붙임 · 1~5번 배경에는 붙이지 않음)

```
CUTOUT: only the described subjects, as isolated cutouts on a fully transparent background (PNG with alpha channel) — no ground, no floor line, no cast shadow, no scenery, no frame, no other objects or people. Clean hard edges with the dark outline. Every subject must be fully visible with empty margin: nothing may touch or cross the canvas edges — keep at least 5% empty transparent space on every side. If a transparent background is impossible, make the whole background one flat pure magenta #FF00FF with no shading, and use no magenta, purple or hot pink at all on the subjects.
```

## MOTION STRIP (6~14번 — CUTOUT 다음에 그대로 붙임)

```
MOTION STRIP: landscape 1536x1024, divided into three equal invisible columns. The three figures are three consecutive animation drawings of ONE continuous movement by the SAME person, like an animator's key pose, in-between and key pose: frame 1 in the left column, frame 2 in the center column, frame 3 in the right column. Between the frames keep everything identical except the moving parts: same scale, same camera angle, same facing direction, same clothes, colors and line weight, and the soles of the feet on exactly the same invisible baseline at about 92% of the canvas height, at the same horizontal spot in each column — the body stays in place and only the arms, hands, head, face, torso lean and held objects move. The standing figure is about 70% of the canvas height (top of the head near 22%) — the same size as in the reference character sheets. Any object held in the hands keeps the same design and size in all three frames and stays inside the same column. Each figure is centered in its column, full body from head to shoes, and never crosses a column border; leave clear empty space between the columns. No motion lines, no effects, no flying objects unless the prompt asks for them.
```

## 1. BG-STORE — 비 그친 밤, 편의점 앞

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/BG-STORE.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Late night just after rain, outside a small neighborhood convenience store, seen from the sidewalk. The store front fills the back of the picture: a wide glowing glass window and a glass door with warm white light inside and softly blurred, colorful shelves of snacks and drinks (only color shapes, no labels), a plain dark awning above with NO sign text. On the LEFT side of the sidewalk: a small green plastic outdoor table with two plastic chairs and a closed umbrella leaning against one chair. The sidewalk floor in the front is dark gray paving, wet and shiny with soft reflections of the warm store light and a few small puddles. The center and right part of the sidewalk in front of the window is open and empty (characters will stand there). A street lamp glow from the right edge. Cool night blue around, warm light from the store. No sky visible — the awning and the building wall fill the top.
```

## 2. BG-DAWN — 같은 곳, 새벽

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/BG-DAWN.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Edit picture 1 (BG-STORE). Keep the camera, the store front, the awning, the table, the chairs, the umbrella and every object exactly in the same place and size. Change only the time: it is early dawn after the night — soft pale pink and light blue morning light, the store lights are still on but weaker, the sidewalk is almost dry with only one small puddle left, the street lamp is off, calm and hopeful mood. Nothing else changes. Full-bleed landscape 1536x864, no people, no text.
```

## 3. BG-ARCHIVE — 기록 보관실

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/BG-ARCHIVE.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
A quiet records archive room, front view. On both the left and the right sides, tall dark-wood shelves full of thick old ledger books and binders with plain colored spines (no labels). In the CENTER of the back wall, one very large empty board: a plain light-cream board in a simple wooden frame, wide and blank, its top near 10% and its bottom near 55% of the picture height, from about 22% to 78% of the width — it is completely empty (no lines, no notes). Two warm brass wall lamps beside the board. In the FRONT, a long wooden table runs across the whole width at the bottom of the picture (its top edge near 80% of the height), with a few closed ledger books stacked at the left and right ends and an empty middle. A character will stand BEHIND this table in the middle, visible from the thighs up. Warm amber light, calm and studious mood.
```

## 4. BG-STAIRS — 광장의 넓은 돌계단

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/BG-STAIRS.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
A wide outdoor stone staircase in a quiet city plaza in late afternoon, seen exactly from the SIDE so every step is clearly visible as a simple zigzag profile. A flat stone landing at the top LEFT (from the left edge to about 28% of the width, its floor near 42% of the picture height), then about ten large equal steps going DOWN to the RIGHT, ending in a flat stone landing at the bottom RIGHT (from about 74% of the width to the right edge, its floor near 90% of the height). Each step is a light warm-gray stone block with a darker front edge. Behind the stairs: a tall plain beige stone wall with a few trimmed green bushes and two old street lamps (off), and warm low sunlight from the left making long soft shadows on the steps. The top of the picture is the stone wall and tree leaves — no sky visible. The steps themselves are empty.
```

## 5. BG-PLATFORM — 빈 지하철 승강장

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/BG-PLATFORM.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
An empty underground subway platform, seen from the SIDE of the track. At the bottom of the picture, the platform floor runs across the whole width (light gray tiles, a bright yellow tactile safety strip along its far edge near 68% of the picture height); characters will stand on this platform. Behind the platform edge, the dark track area runs across the whole width in the middle band (about 40% to 68% of the height) — empty, with two rails — a train will slide in there later. Behind the track, the opposite wall: clean light tiles in soft blue and white, a few large BLANK white wall panels (no text, no maps, no signs), round ceiling lamps. Two square pillars on the platform near the left and right edges. Cool fluorescent light with a slightly lonely late-evening mood. No train, no screen doors, no people.
```

## 6. V18 — 큰 장부를 펴 들고 읽음

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/V18.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the left of the picture. He holds a large, thick, open ledger book with both hands in front of his chest; the pages show only faint ruled lines and tiny tick marks — no letters, no numbers. Frame 1: reading the open book attentively, eyebrows slightly raised. Frame 2: his right hand lifts and turns one page (the page is curved in mid-air), eyes following it. Frame 3: he looks up from the book, eyes wide and mouth open in surprise, the book still open in both hands.
```

## 7. V19 — 게시판을 가리키며 설명

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/V19.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view, his body facing slightly to the left of the picture, calm and focused. Frame 1: his left arm raised, pointing with the index finger up and to the LEFT (toward a board out of frame), looking where he points, mouth closed. Frame 2: he turns his head to look at the viewer, the left hand now held open at chest height palm up, explaining, mouth open as if talking. Frame 3: exactly like frame 2 but with his mouth closed (for lip-sync).
```

## 8. V20 — 튀는 것을 눈으로 따라감

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/V20.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture, both hands clasped together at his chest. He is watching something bounce in front of him. Frame 1: looking DOWN to the right, hopeful eager face. Frame 2: head tilted UP following it upward, eyes sparkling, hopeful open smile, rising slightly on his toes. Frame 3: looking down again, disappointed face, eyebrows sad, shoulders slumped, hands dropping to his stomach.
```

## 9. V21 — 승강장에서 기다리다 놓침

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/V21.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture. Frame 1: standing and waiting with both hands in his jacket pockets, looking to the right, slightly bored, patient face. Frame 2: he suddenly reaches his right arm forward to the right with an open hand as if to say "wait!", eyes wide, mouth open, left hand still in the pocket. Frame 3: the arm dropped, his left hand on the back of his head, regretful frowning face, mouth pulled to one side.
```

## 10. V22 — 동전 병 반을 다른 병에

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/V22.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, front three-quarter view. He holds two identical clear glass jars with no lids and no stickers. Frame 1: his left hand holds a jar FULL of plain gold coins at chest height, his right hand holds an EMPTY jar lower, he looks at the full jar thinking. Frame 2: he tilts the full jar and pours coins into the empty jar (a short stream of a few coins between the jars), concentrating, tongue slightly out. Frame 3: he holds both jars at the same height in front of him, each jar HALF full of coins, calm satisfied small smile.
```

## 11. V23 — 두 손바닥 사이에서 고민

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/V23.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, front view, torn between two choices. Frame 1: his LEFT hand raised to the side at shoulder height palm up, he glances at that hand with a worried face, the other hand down. Frame 2: his RIGHT hand raised to the other side palm up, he glances at that hand with a worried face, the left hand down. Frame 3: both hands holding his head, eyes squeezed, troubled grimace.
```

## 12. V24 — 베개를 안고 잠 못 이룸

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/V24.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, front three-quarter view, standing, hugging a plain light-blue pillow against his chest with both arms (the same pillow in all frames). Frame 1: eyes wide open with dark circles, worried sleepless face. Frame 2: a huge yawn, eyes closed, one hand covering his open mouth, the pillow held in the other arm. Frame 3: the pillow lowered to his waist, eyes closed, a gentle relieved smile, shoulders relaxed.
```

## 13. V25 — 지쳐서 걷기 (옆모습)

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/V25.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, pure side view walking to the RIGHT of the picture, tired and a little hunched, arms swinging loosely, a weary but determined face. Three walking frames of one walk cycle: Frame 1: left leg forward, right leg back (contact pose). Frame 2: legs passing each other under the body, body slightly higher (passing pose). Frame 3: right leg forward, left leg back (opposite contact pose). The soles of the back foot in every frame stay on the same baseline.
```

## 14. V26 — 풀 죽었다가 안도

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/V26.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, front three-quarter view, holding a smartphone in his right hand (blank screen). Frame 1: looking down at the phone, shoulders slumped, sad discouraged face. Frame 2: he lifts his head and looks at the viewer, eyebrows up, a surprised and relieved face, the phone lowered. Frame 3: his left hand on his chest, eyes softly closed, a gentle relieved smile, the phone at his side.
```

## 15. PROPS-B — 소품 4

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/PROPS-B.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 소품 4

```
Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a similar visual size, each fully inside its column: (1) a shiny rubber ball, its top half red and bottom half white with a thin dark line between, a small white highlight; (2) a blank white paper index card pinned at the top center with a round red pushpin, slightly tilted — no writing; (3) a silver stopwatch with a white face showing only short tick marks — no numbers and NO hands; (4) an empty clear glass jar with no lid and no sticker (the same jar as in picture 10).
```

## 16. TRAIN — 지하철 객차 한 칸

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/TRAIN.png`** — PNG 700KB 이하 · 투명 · 가로 1536×512

```
One subway train car, pure side view, facing to the RIGHT (the rounded driver cab is at the right end), landscape 1536x512, the car filling about 90% of the width with empty margin on all sides. Plain silver body with one wide horizontal stripe in calm teal, four sets of closed sliding doors, a row of windows showing only a dark blue-gray glass with soft reflections (nobody inside), small wheels and a thin dark underframe at the bottom. No numbers, no letters, no logos, no route signs.
```

## 17. BLDG — 회사 건물 4채

**저장 경로: `stock/source/bandeung-maesu-2026-11/puppet/motion/BLDG.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 건물 4

```
Building sheet, landscape 1536x1024, four equal invisible columns, one office building centered in each column, all standing on the same invisible ground line near 92% of the height and about 75% of the canvas height tall, each fully inside its column: (1) a tall blue glass skyscraper with a pointed top; (2) a stepped tower in light gray stone that gets narrower toward the top; (3) a solid red-brick office building with rows of windows; (4) a modern white tower with a rounded top and teal window bands. Plain generic buildings — no logos, no names, no letters, no numbers, no flags.
```

## 받은 뒤 (Claude)
- main 의 `stock/source/bandeung-maesu-2026-11/puppet/` 을 작업 브랜치로 가져와 17장을 확대해 검수: 만스피 편 V 와 같은 사람인지 · 그림 속 글자 없음 · 세 장의 발 높이·크기·옷이 같은지 · 손에 든 물건이 세 장에서 같은지 · 2번이 1번과 같은 구도인지 · 배경판의 빈 자리(편의점 앞 바닥 · 보관실 게시판·책상 뒤 · 계단 디딤 · 승강장)가 글대로인지.
- `puppet/slice.py` (만스피 v1.2 를 바탕으로) — 반등 시트 9장(V18~V26) + 만스피 V 시트 중 쓰는 것(V01·V04·V05·V13·V14·V15·V16·V17·V-CALM·V-NIGHT·V-REACT)을 같은 V 키 기준으로 잘라 `cut/` 에 · 소품 4 · 객차 · 건물 4 · 배경 앞 물건 FG(보관실 책상 앞판 · 편의점 탁자 · 승강장 기둥 — 배경 그림의 있는 픽셀만).
- 장면 파일 `video/episodes/bandeung-maesu-2026-11/index.html` (만스피 v3.1 엔진 — 원화 바꿔 끼우기 · 세계 층 카메라 · 영역 표 `window.ZONES`) → `render.mjs check` · `layout-check` · `zone-check --every 0.25` 문제 0 → 렌더 → 완성 mp4 를 직접 봄.
