# bandoche-bunbae-2026-11 쇼츠 — 모션그래픽 그림 17장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.1 — 2026-11-06 — 3번 S-ROOM-B 국면 계기판을 날씨 그림 대신 색(초록·노랑·빨강)으로 (사용자 지시 "잠깐 국면 계기판은 날씨로 하지말고 그냥 색으로 표현해 수정해서 다시 알려줘 명령") · 이전 v1.0 — 2026-11-06 — 사용자 지시 "배경, 캐릭터, 물체 요소 이미지 만들어서 모션그래픽으로 적절하게 상황 표현해 특히 캐릭터는 행동, 상태, 심리 등 변화 별로 이미지 요소를 만들어서 최대한 자연스럽게 표현해야해 진짜 애니메이션 처럼" (쇼츠 대본 `stock/source/bandoche-bunbae-2026-11/shorts/bandoche-bunbae-2026-11-shorts.txt` v1.0 — 19문장, 표의 '쓰는 대본 문장'은 그 줄 번호)

쓰임: Claude 가 이 그림들을 잘라 **코드 모션그래픽**(배경 위에 인물·소품을 움직이고, 자세 그림을 바꿔 끼우고, 숫자·티커·그래프는 코드로)으로 영상을 만든다. 인물은 **한 장에 같은 사람의 연속 동작 3개**(자세 시트)로 그려 같은 얼굴·옷이 유지되게 한다 — Claude 가 칸마다 잘라 쓴다. 그림 속 글자·숫자는 없다 (티커 NVDA·SOXL 등, 수익률, A·B 이름, 그래프는 모두 코드).

| 번호 | 저장 경로 | 크기 · 바탕 | 무엇 | 쓰는 대본 문장 |
|---|---|---|---|---|
| 1 | `stock/source/bandoche-bunbae-2026-11/puppet/S-VS.jpg` | 세로 1024×1536 · 꽉 찬 배경 | 대결 무대 (왼쪽 주황 네온 · 오른쪽 청록) | 1 (누가 더 벌었을까요?) |
| 2 | `stock/source/bandoche-bunbae-2026-11/puppet/S-ROOM-A.jpg` | 세로 1024×1536 · 꽉 찬 배경 | A 의 방 (사람 없음) | 3 · 8~9 |
| 3 | `stock/source/bandoche-bunbae-2026-11/puppet/S-ROOM-B.jpg` | 세로 1024×1536 · 꽉 찬 배경 | B 의 서재 (사람 없음 · 바늘 없는 색 계기판 초록·노랑·빨강) | 4 · 10 · 18~19 |
| 4 | `stock/source/bandoche-bunbae-2026-11/puppet/S-DUO.jpg` | 세로 1024×1536 · 꽉 찬 배경 | 그래프 무대 (위 큰 빈 화면 + 아래 둘이 설 바닥) | 2 · 5~7 · 11~17 |
| 5 | `stock/source/bandoche-bunbae-2026-11/puppet/A-HAPPY.png` | 가로 1536×1024 · 투명 · 자세 3 | A 신남: 서 있기 → 손가락 총 → 점프 환호 | 3 · 5 · 11 |
| 6 | `stock/source/bandoche-bunbae-2026-11/puppet/A-BUY.png` | 가로 1536×1024 · 투명 · 자세 3 | A 매수: 폰 두드림 → 밀어 넣기 → 두 팔 벌려 올인 | 3 · 8 · 9 |
| 7 | `stock/source/bandoche-bunbae-2026-11/puppet/A-MOCK.png` | 가로 1536×1024 · 투명 · 자세 3 | A 조롱: 손가락질 웃음 → 배 잡고 웃음 → 거북이 흔들기 | 6 |
| 8 | `stock/source/bandoche-bunbae-2026-11/puppet/A-PANIC.png` | 가로 1536×1024 · 투명 · 자세 3 | A 불안 → 충격 → 비명 | 12 · 13 |
| 9 | `stock/source/bandoche-bunbae-2026-11/puppet/A-RUIN.png` | 가로 1536×1024 · 투명 · 자세 3 | A 무너짐: 다리 풀림 → 무릎 꿇고 통곡 → 웅크려 흐느낌 | 13 · 14 · 15 |
| 10 | `stock/source/bandoche-bunbae-2026-11/puppet/B-CALM.png` | 가로 1536×1024 · 투명 · 자세 3 | B 차분: 서 있기 → 동전 하나 놓기 → 차 마시기 | 4 · 5 · 10 |
| 11 | `stock/source/bandoche-bunbae-2026-11/puppet/B-REACT.png` | 가로 1536×1024 · 투명 · 자세 3 | B 반응: 못마땅한 곁눈질 → 태블릿 확인 → 우산 쓰고 차분 | 6 · 12 · 13~15 |
| 12 | `stock/source/bandoche-bunbae-2026-11/puppet/B-WIN.png` | 가로 1536×1024 · 투명 · 자세 3 | B 승리: 팔짱 미소 → 엄지 척 → 트로피 들기 | 16 · 17 · 18 |
| 13 | `stock/source/bandoche-bunbae-2026-11/puppet/A-FACE.png` | 가로 1536×1024 · 투명 · 얼굴 3 | A 얼굴: 탐욕 반짝 → 공포 → 오열 | 9 · 11 · 13 · 15 |
| 14 | `stock/source/bandoche-bunbae-2026-11/puppet/B-FACE.png` | 가로 1536×1024 · 투명 · 얼굴 3 | B 얼굴: 차분 → 못마땅 → 자신감 | 6 · 16 · 17 |
| 15 | `stock/source/bandoche-bunbae-2026-11/puppet/P-AI.png` | 가로 1536×1024 · 투명 · 소품 4 | AI 칩 · 금화 더미 · 지폐 다발 · 빈 화면 폰 | 3 · 8~9 |
| 16 | `stock/source/bandoche-bunbae-2026-11/puppet/P-SECTOR.png` | 가로 1536×1024 · 투명 · 배지 8 | 업종 배지 7 (기술·헬스케어·금융·필수소비재·에너지·산업·현금) + 방패 | 4 · 10 · 16 |
| 17 | `stock/source/bandoche-bunbae-2026-11/puppet/P-FX.png` | 가로 1536×1024 · 투명 · 소품 4 | AI 거품 · 터지는 거품 · 폭풍 구름 · 트로피 | 12 · 14 · 17 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
   **★ 먼저 기준 그림 3장을 열어 본다 — 새 그림은 모두 이 그림들과 같은 사람이 그린 것처럼 (그림체·선 굵기·색·얼굴 꼴·비율까지 같게). A·B 는 이 그림 속 두 사람과 똑같은 사람이다.**
   - 인물 기준(설정표): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/7f753d41f29af57a88b8c6fcfc289f0f5d234874/stock/source/bandoche-bunbae-2026-11/shorts/scenes/characters.jpg — 왼쪽 주황 머리 = **A**, 오른쪽 안경 = **B**
   - 장면 기준: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/7f753d41f29af57a88b8c6fcfc289f0f5d234874/stock/source/bandoche-bunbae-2026-11/shorts/scenes/S03.jpg · https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/7f753d41f29af57a88b8c6fcfc289f0f5d234874/stock/source/bandoche-bunbae-2026-11/shorts/scenes/S01.jpg
   그림을 열 수 없으면 아래 '공통 화풍'과 '인물' 설명대로 그린다.
1. 아래 1~17번 **17장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 아래 **공통 화풍** 문단을 붙인다. **5~14번(인물 시트)**은 그다음 **인물** 문단과 **CUTOUT** · **SHEET** 문단을, **15~17번(소품)**은 **CUTOUT** · **SHEET** 문단을 붙인다. **1~4번(배경)**은 공통 화풍만.
3. **5~14번은 한 장에 같은 사람을 3번** 그린다 (왼쪽 → 가운데 → 오른쪽 = 연속 동작 순서). 세 사람이 **같은 크기·같은 얼굴·같은 옷**이고, 서로 겹치거나 닿지 않고, 칸(가로 3등분)을 넘지 않는다. 다른 사람·배경·바닥 그림자는 없다.
4. **배경(1~4번)에는 사람이 없다** — 인물은 Claude 가 따로 얹는다. 화면 끝까지 꽉 찬 그림 한 장 (테두리·커튼·틀 없음).
5. **검사 (5~17번 필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`·`칸 넘음`이면 더 작게(여백을 더 넓게) 다시 만든다. **투명이 아니면 배경을 순자홍 #FF00FF 한 색 평면으로 다시 만든다** (A 의 모자가 라임색이라 초록 바탕은 안 됨).
   ```python
   from PIL import Image
   import numpy as np
   def filled_mask(a):
       if a[2, 2, 3] > 0:                        # 투명이 아니면 순자홍 바탕을 빈 곳으로 봄
           r, g, b = (a[:, :, i].astype(int) for i in range(3))
           return ~((r > 200) & (b > 200) & (g < 90))
       return a[:, :, 3] > 40
   def check(path, cols, rows=1, margin=0.05, gap=0.015):
       a = np.array(Image.open(path).convert("RGBA"))
       h, w = a.shape[:2]
       m = filled_mask(a)
       ys, xs = np.where(m)
       box = (xs.min() / w, ys.min() / h, xs.max() / w, ys.max() / h)
       ok = box[0] >= margin and box[1] >= margin and box[2] <= 1 - margin and box[3] <= 1 - margin
       cross = []
       for c in range(1, cols):                  # 칸 경계 둘레(±1.5%)는 비어 있어야 함
           x = int(w * c / cols); d = int(w * gap)
           if m[:, x - d:x + d].any(): cross.append(f"세로 경계 {c}")
       for r_ in range(1, rows):
           y = int(h * r_ / rows); d = int(h * gap)
           if m[y - d:y + d, :].any(): cross.append(f"가로 경계 {r_}")
       ok = ok and not cross
       print(path, "OK" if ok else f"잘림·칸 넘음 — 다시 {cross}", [round(float(v), 3) for v in box])
       return bool(ok)
   # 5~14번: check(경로, cols=3) · 15·17번: check(경로, cols=4, margin=0.02) · 16번: check(경로, cols=4, rows=2, margin=0.02)
   ```
6. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 화면·폰·지폐·간판·배지·트로피에도 없음. 실제 회사(엔비디아·샌디스크 등)·은행·게임의 이름·로고·색을 닮게 그리지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.
7. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. stock/source/bandoche-bunbae-2026-11/puppet/S-VS.jpg`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게).
   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     - 1~4번(JPEG): RGB · 크기 1024×1536 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.
     - 5~17번(PNG, 투명 유지): 아래 코드 그대로.
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
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[stock] bandoche-bunbae-2026-11 <파일 이름> 이미지` (예: `[stock] bandoche-bunbae-2026-11 S-VS.jpg 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 공통 화풍 (1~17번 모든 프롬프트 맨 앞에 그대로 붙임 — 기준 그림과 같은 그림체)

```
STYLE: Match exactly the art style of the reference images: a polished flat 2D cartoon illustration in the look of a typical casual mobile-game video advertisement (generic — do NOT copy any existing game's characters, logos, interface or art). Chunky big-headed proportions (head about one third of the body height), large expressive eyes, exaggerated rubbery facial expressions and poses that read instantly on a small phone screen, bold clean dark outlines, flat cel shading with one simple shadow tone and a small highlight, bold saturated but clean colors, simple shapes, crisp vector-like edges. It is a 2D drawing — not a 3D render, not clay or plastic, not a photo. Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere — screens, phones, banknotes, badges and signs are blank or show only simple shapes.
```

## 인물 (5~14번 — 공통 화풍 다음에 그대로 붙임)

```
CHARACTERS — draw them exactly like the reference character sheet, same face, hair, clothes and proportions in every pose:
A — a hyperactive, goofy young man in his mid-20s: spiky bright-orange dyed hair sticking straight up, a backwards lime-green baseball cap, an oversized neon-orange hoodie with a big plain dark square microchip-shaped patch on the chest (a square with little metal pin legs, no text), a thin gold chain, baggy black cargo shorts, white socks, chunky white sneakers. Big toothy grin, mischievous eyebrows, cocky show-off body language.
B — a calm, composed man in his late 30s: neat dark-brown side-parted hair, thin round glasses, clean-shaven, a soft navy-blue knit sweater over a white collared shirt, beige chinos, brown loafers, a slim silver wristwatch. Relaxed upright posture, gentle half-lidded eyes, a small steady smile; he moves slowly and deliberately.
```

## CUTOUT (5~17번 — 그다음에 그대로 붙임 · 1~4번 배경에는 붙이지 않음)

```
CUTOUT: only the described subjects, as isolated cutouts on a fully transparent background (PNG with alpha channel) — no ground, no floor line, no cast shadow, no scenery, no frame, no other objects or people. Clean hard edges with the dark outline. Every subject must be fully visible with generous empty margin: nothing may touch or cross the canvas edges — keep at least 6% empty transparent space on every side. If a transparent background is impossible, make the whole background one flat pure magenta #FF00FF with no shading, and use no magenta or pink at all on the subjects.
```

## SHEET (5~17번 — 그다음에 그대로 붙임)

```
SHEET: landscape 1536x1024. The canvas is divided into equal invisible cells (3 columns for character and face sheets, 4 columns for prop sheets, 4 columns x 2 rows for the badge sheet). Put exactly one subject in the center of each cell, in the order given (left to right, then top to bottom). Subjects never overlap, never touch each other and never cross a cell border — leave clear transparent space between them. For character sheets: all three figures are the SAME person at the SAME scale, full body from head to shoes, standing on the same invisible baseline at about 90% of the canvas height (a jumping pose may float above it), heads below the top 8%. Face sheets: head and shoulders, same scale, all facing the viewer.
```

## 1. S-VS — 배경: 대결 무대

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/S-VS.jpg`** — JPEG 700KB 이하 · 세로 1024×1536

```
Portrait 1024x1536. A full-bleed background that fills the whole canvas edge to edge: a flashy mobile-game "versus" arena split vertically down the middle by a jagged bright energy seam. LEFT half: hot neon orange and red with glowing abstract circuit-board lines and sparks (an AI-chip power vibe). RIGHT half: calm cool teal and sky blue with soft clouds, gentle light rays and a few small green leaves (a calm, balanced vibe). At the bottom of each half a round glossy pedestal platform where a character will stand (left pedestal centered at about 27% width, right one at about 73% width, both at about 80% of the height). Keep the top 25% simple and open (a title goes there) and the center seam area clear. No people, no text, no letters, no "VS" letters, no numbers, no logos.
```

## 2. S-ROOM-A — 배경: A 의 방

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/S-ROOM-A.jpg`** — JPEG 700KB 이하 · 세로 1024×1536

```
Portrait 1024x1536. A full-bleed background, no people: A's bright, slightly messy gamer bedroom like the reference scene — purple-and-pink LED strip lights along the ceiling, wall posters that show only abstract shapes, a pink-and-black gaming chair pushed to the left side, a desk on the right with two monitors showing only blank glowing color, a few plain energy-drink cans with no logos. The middle of the floor (center, from about 55% to 95% of the height) is open and empty — a character will stand there. Keep the top 20% simple. No people, no text, no numbers, no logos.
```

## 3. S-ROOM-B — 배경: B 의 서재

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/S-ROOM-B.jpg`** — JPEG 700KB 이하 · 세로 1024×1536

```
Portrait 1024x1536. A full-bleed background, no people: B's tidy sunny home study like the reference scene — a large window with soft daylight and green trees outside, a light wooden desk against the right wall with a potted plant and a cup of tea, bookshelves with plain spines. High on the left wall (upper-left quarter) hangs a big semicircular gauge meter (like a speedometer) in a simple round frame: its arc is divided into three plain flat color zones — green on the left, yellow in the middle, red on the right — with NO needle (the pivot at the bottom center is a plain empty circle), no pictures, no icons, no tick labels and no numbers. The middle of the floor (center, from about 55% to 95% of the height) is open and empty — a character will stand there. No people, no text, no numbers, no logos.
```

## 4. S-DUO — 배경: 그래프 무대

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/S-DUO.jpg`** — JPEG 700KB 이하 · 세로 1024×1536

```
Portrait 1024x1536. A full-bleed background, no people: a stylish game-show studio. The upper part is one huge wall-mounted display screen spanning almost the full width, from about 6% to 46% of the height, with a thin glowing rim: the screen surface is deep navy-black glass with a very faint fine grid and a soft vignette — completely EMPTY inside (a chart will be drawn there by code). Below the screen, a glossy studio floor split in two moods: the left half lit warm orange, the right half lit cool teal, each with a soft round spotlight on the floor where a character will stand (left spot centered at about 27% width, right spot at about 73% width, both around 85% of the height). The area from 48% to 95% of the height is open space for the two characters. No people, no text, no numbers, no logos, nothing drawn on the screen.
```

## 5. A-HAPPY — A 신남 (자세 3)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/A-HAPPY.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=3)`

```
Three poses of A, left to right as one bouncy animation: (1) standing with a cocky grin, hands in his hoodie pocket, weight on one leg; (2) bouncing up on his toes, both hands making finger-guns pointing forward, winking with his tongue cheekily out; (3) jumping in the air cheering, both fists raised high above his head, mouth wide open in a triumphant shout, knees bent, sparkling eyes.
```

## 6. A-BUY — A 매수·올인 (자세 3)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/A-BUY.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=3)`

```
Three poses of A, left to right: (1) holding a smartphone with both hands close to his face and tapping the blank glowing screen eagerly with a thumb, grinning with excitement; (2) leaning forward and pushing both open palms forward hard, as if shoving a huge pile of money across a table (the pile is NOT drawn), determined greedy grin; (3) arms flung wide open, chest out, head tilted back, laughing in triumph with sparkling star-like highlights in his eyes — an "all-in" pose.
```

## 7. A-MOCK — A 조롱 (자세 3)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/A-MOCK.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=3)`

```
Three poses of A mocking someone standing to his right (the viewer's right), left to right: (1) pointing his index finger to the right and laughing loudly with eyes squeezed shut; (2) bent over holding his belly with both hands, laughing so hard his tongue sticks out, one knee lifted; (3) holding up a small green toy turtle in one hand toward the right and wiggling it, with a smug teasing smirk and raised eyebrows.
```

## 8. A-PANIC — A 불안 → 충격 → 비명 (자세 3)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/A-PANIC.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=3)`

```
Three poses of A, left to right as his mood collapses: (1) staring at a smartphone in his hands with a frozen, too-wide nervous grin, big cartoon sweat drops on his forehead, knees slightly shaking; (2) shocked: jaw dropped wide open, both hands pressed to his cheeks, eyes popping with tiny pupils, the phone falling from his hand; (3) screaming in panic, hair standing even more on end, both arms flailing up, cap tilted.
```

## 9. A-RUIN — A 무너짐 (자세 3)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/A-RUIN.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=3)`

```
Three poses of A, left to right as he breaks down: (1) knees buckling inward, shoulders sagging, staring down in disbelief with an empty, pale face; (2) kneeling on both knees, sobbing loudly with huge cartoon waterfalls of tears, mouth wide in a wail, both fists clenched near his knees, his empty pockets turned inside out; (3) sitting slumped on the ground hugging his knees, head down, crying quietly with a runny nose, his whole figure slightly grayer and gloomier.
```

## 10. B-CALM — B 차분 (자세 3)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/B-CALM.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=3)`

```
Three poses of B, left to right: (1) standing calmly upright with hands clasped behind his back, a gentle small smile; (2) holding a single gold coin between two fingers of one raised hand and calmly placing it to his side, as if dividing money into separate boxes (the boxes are NOT drawn), relaxed focused face; (3) sipping tea from a white cup held with both hands, eyes half closed, peaceful.
```

## 11. B-REACT — B 반응 (자세 3)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/B-REACT.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=3)`

```
Three poses of B, left to right: (1) holding a teacup halfway up, giving a long annoyed side-eye toward his right (the viewer's left), lips pressed into a flat displeased line, one eyebrow twitching — annoyed but composed; (2) checking a small tablet held in one hand (its screen faces away from the viewer), calm and focused, the other hand lightly touching his chin; (3) standing calmly under an open navy-blue umbrella held over his head with one hand, relaxed shoulders and a steady small smile — calm in a storm (no rain drawn).
```

## 12. B-WIN — B 승리 (자세 3)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/B-WIN.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=3)`

```
Three poses of B, left to right: (1) arms crossed, standing tall, a calm confident half-smile with one eyebrow slightly raised; (2) a gentle thumbs-up toward the viewer with a warm calm smile; (3) holding a small plain golden trophy cup (no text, no engraving) at chest height with one hand, modest proud smile.
```

## 13. A-FACE — A 얼굴 (얼굴 3)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/A-FACE.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=3)`

```
Three head-and-shoulders close-ups of A facing the viewer, left to right: (1) greedy euphoria — a huge grin, eyes shining with big sparkle highlights, cheeks flushed; (2) terror — eyes wide with tiny pupils, mouth open in a silent scream, sweat drops; (3) devastated crying — streams of tears, trembling lips, runny nose, eyebrows pushed up in despair.
```

## 14. B-FACE — B 얼굴 (얼굴 3)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/B-FACE.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=3)`

```
Three head-and-shoulders close-ups of B facing the viewer, left to right: (1) calm — a gentle small smile, relaxed half-lidded eyes; (2) annoyed — a sideways glare, mouth pressed flat, a small cartoon anger mark near his temple; (3) quietly confident — a calm knowing half-smile, one eyebrow slightly raised.
```

## 15. P-AI — 소품: AI 칩 · 금화 · 지폐 · 폰 (4개)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/P-AI.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=4, margin=0.02)`

```
Four separate objects in four equal columns, left to right: (1) a glossy black-and-gold computer chip block — a big square chip with shiny gold metal pin legs on all four sides and a soft glow (the symbol of AI semiconductors), no text; (2) a big heaped pile of shiny gold coins; (3) a thick bundle of plain green banknotes tied with a paper band, no numbers or text on the notes; (4) a modern smartphone seen from the front, its screen a blank glowing gradient with nothing on it.
```

## 16. P-SECTOR — 소품: 업종 배지 8개

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/P-SECTOR.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=4, rows=2, margin=0.02)`

```
Eight round glossy game-style badge tokens of the same size and style (thick colored rim, soft highlight), arranged in 4 columns x 2 rows, each with one simple picture in the middle and no text: top row left to right — (1) a laptop (technology, blue rim), (2) a red heart with a white plus sign (healthcare, red rim), (3) a classical bank building with columns (finance, purple rim), (4) a shopping basket with bread and a milk bottle (consumer staples, green rim); bottom row left to right — (5) a lightning bolt beside an oil drop (energy, orange rim), (6) a big gear (industrials, gray rim), (7) a neat stack of green banknotes (cash, gold rim), (8) a sturdy shield (protection, teal rim).
```

## 17. P-FX — 소품: AI 거품 · 터지는 거품 · 폭풍 구름 · 트로피 (4개)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/puppet/P-FX.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · 검사 `check(경로, cols=4, margin=0.02)`

```
Four separate objects in four equal columns, left to right: (1) a big shiny iridescent soap bubble with a small glowing computer chip floating inside it (an "AI bubble"); (2) the same bubble bursting — a ring of popping droplets and splash fragments flying outward, the little chip falling; (3) a dark gray storm cloud with heavy rain streaks below it and a yellow lightning bolt; (4) a plain shiny golden trophy cup with two handles, no text or engraving.
```
