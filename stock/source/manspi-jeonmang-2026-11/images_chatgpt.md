# manspi-jeonmang-2026-11 롱폼 — 영상 그림 17장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.0 — 2026-11-10 — 최초. 사용자 지시 2026-11-10 "만스피 대본 완성했으니 그걸로 영상 만들 준비 하자 썸네일 그림체로 만들거니 필요한 이미지 만들도록 챗지피티한테 명령 알려줘". 기준 대본 = main 커밋 ac40a5e3 의 `manspi-jeonmang-2026-11.txt` (사용자 완성본 · 5장 61문장).

쓰임: Claude 가 이 그림들을 잘라 **코드 모션그래픽**(배경 위에 인물·소품을 움직이고, 자세 그림을 바꿔 끼우고, 말 카드·숫자·BUY 같은 글은 모두 코드로)으로 영상을 만든다. 인물은 **한 장에 같은 사람의 연속 동작 3개**(자세 시트)로 그려 같은 얼굴·옷이 유지되게 한다 — Claude 가 칸마다 잘라 쓴다. **그림 속 글자·숫자는 없다.**
이 편의 중심 장치 = **거름망(체)** — 전문가의 말 카드가 위에서 떨어져, 걸러야 할 말은 체에 걸려 왼쪽 버리는 통으로, 믿어도 되는 말은 체를 통과해 오른쪽 보관함으로 간다 (다른 편과 겹치지 않는 무대 — quick_board 규칙 43).

| 번호 | 저장 경로 | 크기 · 바탕 | 무엇 | 쓰는 대본 문장 |
|---|---|---|---|---|
| 1 | `stock/source/manspi-jeonmang-2026-11/puppet/BG-NIGHT.jpg` | 가로 1536×864 · 꽉 찬 배경 | 밤 거실 (사람 없음) | 1~2 · 4~5 |
| 2 | `stock/source/manspi-jeonmang-2026-11/puppet/BG-STUDIO.jpg` | 가로 1536×864 · 꽉 찬 배경 | 경제 방송 스튜디오 (사람 없음) | 3 · 17 · 21~22 · 26~27 · 31 |
| 3 | `stock/source/manspi-jeonmang-2026-11/puppet/BG-OFFICE.jpg` | 가로 1536×864 · 꽉 찬 배경 | 증권사 분석실 책상 (사람 없음) | 7~14 · 45~48 |
| 4 | `stock/source/manspi-jeonmang-2026-11/puppet/BG-SIEVE.jpg` | 가로 1536×864 · 꽉 찬 배경 | 거름망 무대 — 가운데 큰 체 · 왼쪽 버리는 통 · 오른쪽 보관함 (사람 없음) | 6 · 15~54 |
| 5 | `stock/source/manspi-jeonmang-2026-11/puppet/BG-MORNING.jpg` | 가로 1536×864 · 꽉 찬 배경 | 아침 거실 (1번과 같은 방, 사람 없음) | 55~61 |
| 6 | `stock/source/manspi-jeonmang-2026-11/puppet/V-NIGHT.png` | 가로 1536×1024 · 투명 · 자세 3 | 시청자: 휴대전화 보고 충격 → 머리 감싸기 → 처진 어깨로 고개 떨굼 | 1~2 · 4 |
| 7 | `stock/source/manspi-jeonmang-2026-11/puppet/V-REACT.png` | 가로 1536×1024 · 투명 · 자세 3 | 시청자: 화나서 손가락질 → 팔짱 끼고 의심 → 손바닥 내밀어 '멈춰' | 3 · 16~34 |
| 8 | `stock/source/manspi-jeonmang-2026-11/puppet/V-CALM.png` | 가로 1536×1024 · 투명 · 자세 3 | 시청자: 빈 메모장에 적기 → 끄덕이며 미소 → 편안히 휴대전화를 주머니에 | 36~61 |
| 9 | `stock/source/manspi-jeonmang-2026-11/puppet/E-HYPE.png` | 가로 1536×1024 · 투명 · 자세 3 | 전문가: 위를 가리키며 자신만만 → 주먹 쥐고 외침 → 가슴 두드리며 장담 | 3 · 17 · 26~27 |
| 10 | `stock/source/manspi-jeonmang-2026-11/puppet/E-PUSH.png` | 가로 1536×1024 · 투명 · 자세 3 | 전문가: 손목시계 톡톡 → 손짓으로 '어서' → 두 팔 벌려 재촉 | 20~24 |
| 11 | `stock/source/manspi-jeonmang-2026-11/puppet/E-DODGE.png` | 가로 1536×1024 · 투명 · 자세 3 | 전문가: 어깨 으쓱 → 시선 피하며 딴청 → 등 돌려 걸어감 | 4 · 30~34 |
| 12 | `stock/source/manspi-jeonmang-2026-11/puppet/E-CALM.png` | 가로 1536×1024 · 투명 · 자세 3 | 전문가(차분): 손가락 두 개로 조건 설명 → 두 손을 저울처럼 위아래 → 손바닥 펴고 솔직하게 | 36~44 · 49~54 |
| 13 | `stock/source/manspi-jeonmang-2026-11/puppet/E-DESK.png` | 가로 1536×1024 · 투명 · 자세 3 | 전문가: 계산기 두드리기 → 서류 보며 고개 갸웃 → 연필로 종이를 고쳐 적기 | 7~11 · 45~48 |
| 14 | `stock/source/manspi-jeonmang-2026-11/puppet/P-QUOTE.png` | 가로 1536×1024 · 투명 · 소품 4 | 빈 말풍선 카드 4 (둥근 · 뾰족한 외침 · 네모 종이 카드 · 구겨진 말풍선) | 16~54 (말 카드 — 글은 코드) |
| 15 | `stock/source/manspi-jeonmang-2026-11/puppet/P-DOCS.png` | 가로 1536×1024 · 투명 · 소품 4 | 빈 리포트 서류 더미 · 계산기(빈 화면) · 돋보기 · 빈 화면 휴대전화 | 2 · 7~14 |
| 16 | `stock/source/manspi-jeonmang-2026-11/puppet/P-MARKS.png` | 가로 1536×1024 · 투명 · 소품 4 | 빨간 X 도장 · 초록 체크 도장 · 모래시계 · 저울 | 18~54 |
| 17 | `stock/source/manspi-jeonmang-2026-11/puppet/P-CHART.png` | 가로 1536×1024 · 투명 · 소품 4 | 빈 차트판(축만) · 위로 솟는 빨간 화살표 · 아래로 꺾이는 파란 화살표 · 안이 뿌연 수정 구슬 | 7~12 · 40~44 · 49~52 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
   **★ 먼저 기준 그림을 열어 본다 — 새 그림은 모두 이 그림과 같은 사람이 그린 것처럼 (그림체·선 굵기·색·얼굴 꼴·비율까지 같게). 시청자(V)와 전문가(E)는 이 그림 속 두 사람과 똑같은 사람이다.**
   - 기준 그림(썸네일): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/1bcbf5532537e13ce5b1c1cd1402ffe328c59371/stock/source/manspi-jeonmang-2026-11/images/TH-CHAR.jpg — 왼쪽 곱슬머리·올리브색 재킷 = **V(시청자)**, 오른쪽 남색 정장·빨간 넥타이 = **E(전문가)**. 이 그림 왼쪽 위의 '-50%' 글자는 따라 그리지 않는다.
   그림을 열 수 없으면 아래 '공통 화풍'과 '인물' 설명대로 그린다.
1. 아래 1~17번 **17장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 아래 **공통 화풍** 문단을 붙인다. **6~13번(인물 시트)**은 그다음 **인물** 문단과 **CUTOUT** · **SHEET** 문단을, **14~17번(소품)**은 **CUTOUT** · **SHEET** 문단을 붙인다. **1~5번(배경)**은 공통 화풍만.
3. **6~13번은 한 장에 같은 사람을 3번** 그린다 (왼쪽 → 가운데 → 오른쪽 = 연속 동작 순서). 세 사람이 **같은 크기·같은 얼굴·같은 옷**이고, 서로 겹치거나 닿지 않고, 칸(가로 3등분)을 넘지 않는다. 다른 사람·배경·바닥 그림자는 없다.
4. **배경(1~5번)에는 사람이 없다** — 인물은 Claude 가 따로 얹는다. 화면 끝까지 꽉 찬 그림 한 장 (테두리·틀 없음).
5. **검사 (6~17번 필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`·`칸 넘음`이면 더 작게(여백을 더 넓게) 다시 만든다. **투명이 아니면 배경을 순자홍 #FF00FF 한 색 평면으로 다시 만든다.**
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
       ok = ok and not cross
       print(path, "OK" if ok else f"잘림·칸 넘음 — 다시 {cross}", [round(float(v), 3) for v in box])
       return bool(ok)
   # 6~13번: check(경로, cols=3) · 14~17번: check(경로, cols=4, margin=0.02)
   ```
6. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — TV·모니터·휴대전화·서류·말풍선·차트판·계산기에도 없음 (빈 화면이나 단순한 줄·도형만). 실제 방송사·증권사·은행의 이름·로고·색을 닮게 그리지 않는다. 날씨(해·구름·비·번개)는 그리지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.
7. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. stock/source/manspi-jeonmang-2026-11/puppet/BG-NIGHT.jpg`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게).
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
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[stock] manspi-jeonmang-2026-11 <파일 이름> 이미지` (예: `[stock] manspi-jeonmang-2026-11 BG-NIGHT.jpg 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 공통 화풍 (1~17번 모든 프롬프트 맨 앞에 그대로 붙임 — 기준 그림과 같은 그림체)

```
STYLE: Match exactly the art style of the reference thumbnail image: a polished flat 2D cartoon illustration with bold clean dark outlines, flat colors with one simple cel-shading tone and small highlights, warm cozy indoor lighting mixed with cool blue screen glow, expressive exaggerated faces (big eyes, clear eyebrows, open mouths, tears when sad) and easy-to-read body language for a small phone screen. Slightly chunky proportions (head about one quarter of the body height). It is a 2D drawing — not a 3D render, not clay or plastic, not a photo. Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere — TVs, monitors, phones, papers, speech bubbles, charts and calculators are blank or show only simple lines and shapes. No weather (no sky, sun, clouds, rain or lightning).
```

## 인물 (6~13번 — 공통 화풍 다음에 그대로 붙임)

```
CHARACTERS — draw them exactly like the reference thumbnail, same face, hair, clothes and proportions in every pose:
V — an ordinary Korean man around 40 who invested his savings: messy curly medium-brown hair, an olive-green casual button jacket with flap pockets over a beige checked shirt, brown trousers with a brown belt, brown shoes. A kind, emotional face that shows feelings strongly (worry, anger, relief).
E — a confident Korean TV stock-market commentator in his 50s: neatly combed dark hair with gray streaks at the temples, a navy-blue suit, white shirt, red tie, black shoes. A smug, self-assured smile and a raised eyebrow when hyping; a calm, honest face in his calm poses. He is a generic fictional person, not any real commentator.
```

## CUTOUT (6~17번 — 그다음에 그대로 붙임 · 1~5번 배경에는 붙이지 않음)

```
CUTOUT: only the described subjects, as isolated cutouts on a fully transparent background (PNG with alpha channel) — no ground, no floor line, no cast shadow, no scenery, no frame, no other objects or people. Clean hard edges with the dark outline. Every subject must be fully visible with generous empty margin: nothing may touch or cross the canvas edges — keep at least 6% empty transparent space on every side. If a transparent background is impossible, make the whole background one flat pure magenta #FF00FF with no shading, and use no magenta or pink at all on the subjects.
```

## SHEET (6~17번 — 그다음에 그대로 붙임)

```
SHEET: landscape 1536x1024. The canvas is divided into equal invisible cells (3 columns for character sheets, 4 columns for prop sheets). Put exactly one subject in the center of each cell, in the order given (left to right). Subjects never overlap, never touch each other and never cross a cell border — leave clear transparent space between them. For character sheets: all three figures are the SAME person at the SAME scale, full body from head to shoes, standing on the same invisible baseline at about 90% of the canvas height, heads below the top 8%. Prop sheets: all props at a similar visual size, each fully inside its cell.
```

## 1. BG-NIGHT — 배경: 밤 거실

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/BG-NIGHT.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Landscape 1536x864. A full-bleed background that fills the whole canvas edge to edge, no people: a small Korean apartment living room late at night, seen from a low side angle (different from the reference thumbnail's angle). A gray fabric sofa along the back wall on the left, a low wooden coffee table with an empty mug, a warm floor lamp on the right casting a soft pool of light, a large dark window behind with faint blurred city lights (only small dots of light, no buildings with signs). The TV on the wall is switched off (plain dark rectangle). The open floor in the center and center-right (from about 40% to 80% of the width, 45% to 95% of the height) is empty — a character will stand there. Calm, lonely, late-night mood in deep blues with warm lamp light.
```

## 2. BG-STUDIO — 배경: 경제 방송 스튜디오

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/BG-STUDIO.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Landscape 1536x864. A full-bleed background, no people: a bright TV economics talk-show studio. A large curved blank video wall behind (glowing soft blue with only abstract rising line shapes, no numbers, no text, no logos), a sleek glossy news desk on the right third, bright studio spotlights at the top edge, a polished reflective floor. The center of the floor (from about 30% to 65% of the width, 40% to 95% of the height) is open and empty — a presenter will stand there. Upbeat, glossy, slightly overconfident mood. No cameras with brand names, no tickers, no text.
```

## 3. BG-OFFICE — 배경: 증권사 분석실 책상

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/BG-OFFICE.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Landscape 1536x864. A full-bleed background, no people: a tidy analyst's office desk area in a securities firm during the day. A long desk across the lower part of the frame with two monitors showing only blank pale screens with simple abstract lines, neat stacks of blank paper reports, a desk lamp, a mug, a window with soft daylight and a plain office wall behind. Leave the area just behind the desk in the center (from about 35% to 65% of the width) open — a person will be placed there working at the desk. Calm, professional mood in light grays, soft blues and warm wood. No text, no numbers, no logos.
```

## 4. BG-SIEVE — 배경: 거름망 무대 (이 편의 중심 화면)

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/BG-SIEVE.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Landscape 1536x864. A full-bleed background, no people: a clean, simple stage like a tidy workshop table seen from the front. In the exact center stands one very large round mesh sieve (a kitchen strainer with a wooden rim and a fine metal mesh) held on a simple stand, its top rim at about 30% of the height and its mesh bowl reaching about 60% of the height. Directly under the sieve, an empty shallow tray on the table. On the LEFT side of the table a plain metal discard bin with a slightly reddish tint; on the RIGHT side a neat open wooden keep box with a soft teal-green tint. The upper part above the sieve (top 25%) is plain and open — cards will fall from there. Soft warm neutral background wall, gentle even light. No text, no numbers, no symbols, no logos.
```

## 5. BG-MORNING — 배경: 아침 거실 (1번과 같은 방)

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/BG-MORNING.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Landscape 1536x864. A full-bleed background, no people: the SAME small apartment living room as picture 1 (same gray sofa on the left, same wooden coffee table, same floor lamp on the right, same window), but now in fresh morning light — curtains open, bright soft daylight pouring in, a small green plant on the table, tidy and calm. The open floor in the center and center-right (from about 40% to 80% of the width, 45% to 95% of the height) is empty — a character will stand there. Hopeful, relieved mood in warm cream, light wood and soft green. No text, no numbers, no logos, no sky view (the window shows only soft bright light).
```

## 6. V-NIGHT — 시청자 자세 시트: 충격 → 머리 감싸기 → 고개 떨굼

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/V-NIGHT.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3

```
Character sheet of V, three poses left to right, full body standing: (1) holding a smartphone with both hands close to his face, staring at the blank screen in shock — eyes wide, mouth open; (2) the phone in one hand hanging down, the other hand clutching his curly hair, eyes squeezed, a small tear; (3) shoulders slumped forward, head hanging low, arms limp, the phone dangling from his fingers — exhausted despair. The phone screen is blank.
```

## 7. V-REACT — 시청자 자세 시트: 손가락질 → 팔짱 의심 → '멈춰' 손짓

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/V-REACT.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3

```
Character sheet of V, three poses left to right, full body standing: (1) angry, leaning forward and pointing his index finger to the right as if at a TV, eyebrows furrowed, teeth clenched; (2) arms crossed over his chest, one eyebrow raised, squinting with suspicion; (3) one arm stretched forward with the palm out in a firm "stop" gesture, serious determined face.
```

## 8. V-CALM — 시청자 자세 시트: 메모 → 끄덕임 → 편안함

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/V-CALM.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3

```
Character sheet of V, three poses left to right, full body standing: (1) writing in a small blank notepad with a pen, focused, slight smile; (2) nodding with a relieved, understanding smile, one hand on his chin; (3) relaxed and calm, putting his smartphone into his jacket pocket, shoulders loose, a gentle confident smile. The notepad and phone are blank.
```

## 9. E-HYPE — 전문가 자세 시트: 위를 가리킴 → 주먹 외침 → 가슴 두드리며 장담

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/E-HYPE.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3

```
Character sheet of E, three poses left to right, full body standing: (1) pointing his index finger straight up with a smug, confident smile and a raised eyebrow, like in the reference; (2) both fists clenched in front of his chest, mouth wide open shouting with excitement, leaning forward; (3) patting his chest with one hand and winking, the other hand giving a confident thumbs-up — an "I guarantee it" pose.
```

## 10. E-PUSH — 전문가 자세 시트: 손목시계 → '어서' 손짓 → 두 팔 벌려 재촉

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/E-PUSH.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3

```
Character sheet of E, three poses left to right, full body standing: (1) tapping his wristwatch with one finger, raising his eyebrows urgently; (2) waving one hand toward himself in a "hurry, come now" beckoning gesture, eager grin; (3) both arms spread wide open, leaning forward, an excited pushy expression as if saying "now or never". The watch face is blank.
```

## 11. E-DODGE — 전문가 자세 시트: 어깨 으쓱 → 딴청 → 등 돌려 걸어감

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/E-DODGE.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3

```
Character sheet of E, three poses left to right, full body standing: (1) shrugging both shoulders with palms up and an awkward fake smile; (2) looking away to the side, whistling innocently with pursed lips, hands in his trouser pockets; (3) seen from behind, walking away to the right, one hand raised in a casual wave without looking back.
```

## 12. E-CALM — 전문가 자세 시트(차분): 조건 설명 → 저울 → 솔직하게

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/E-CALM.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3

```
Character sheet of E in his calm, honest mode (no smug grin, a sincere gentle expression), three poses left to right, full body standing: (1) holding up two fingers while explaining calmly, other hand open; (2) both hands held out at his sides like a balance scale, one hand slightly higher than the other, a thoughtful face; (3) both palms open toward the viewer in an honest "I don't know for sure" gesture, a small humble smile.
```

## 13. E-DESK — 전문가 자세 시트: 계산기 → 갸웃 → 고쳐 적기

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/E-DESK.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3

```
Character sheet of E working as an analyst, three poses left to right, full body standing (no desk drawn): (1) holding a small calculator in one hand and pressing its buttons with the other, concentrating; (2) holding a blank paper report and tilting his head with a puzzled frown; (3) holding a blank sheet of paper against a clipboard and correcting it with a pencil, a serious, slightly embarrassed face. The calculator screen and papers are blank.
```

## 14. P-QUOTE — 소품 시트: 빈 말풍선 카드 4

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/P-QUOTE.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 소품 4

```
Prop sheet, four props left to right, each large and fully blank inside (text will be added later): (1) a round white speech bubble with a small tail; (2) a spiky white "shouting" speech bubble with jagged edges; (3) a clean white rectangular paper card with slightly rounded corners and a soft shadow line; (4) a crumpled, wrinkled white speech bubble, slightly torn, as if rejected. All white with the dark outline, nothing written inside.
```

## 15. P-DOCS — 소품 시트: 서류 더미 · 계산기 · 돋보기 · 휴대전화

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/P-DOCS.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 소품 4

```
Prop sheet, four props left to right: (1) a neat stack of blank paper reports held by a binder clip; (2) a simple desk calculator with a blank screen and plain buttons without symbols; (3) a round magnifying glass with a wooden handle; (4) a smartphone standing upright with a blank glowing screen.
```

## 16. P-MARKS — 소품 시트: 빨간 X 도장 · 초록 체크 도장 · 모래시계 · 저울

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/P-MARKS.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 소품 4

```
Prop sheet, four props left to right: (1) a bold red X mark shaped like a rubber stamp print with slightly rough edges; (2) a bold green check mark shaped like a rubber stamp print; (3) an hourglass with sand running down; (4) a classic brass balance scale with two empty pans, level.
```

## 17. P-CHART — 소품 시트: 빈 차트판 · 빨간 상승 화살표 · 파란 하락 화살표 · 수정 구슬

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/P-CHART.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 소품 4

```
Prop sheet, four props left to right: (1) a blank chart board on a small easel showing only two plain axis lines, no grid numbers; (2) a thick red arrow zigzagging upward to the top right; (3) a thick blue arrow zigzagging downward to the bottom right; (4) a glass crystal ball on a small stand, its inside cloudy and foggy so nothing can be seen clearly.
```

## 받은 뒤 (Claude)
- 장마다 확대해서 검수한다: 기준 그림과 같은 사람·그림체인지 · 글자·숫자가 없는지 · 칸 넘음 · 투명/자홍 바탕.
- 통과한 것만 쓰고, 영상 장면 파일(`video/episodes/manspi-jeonmang-2026-11/`)의 배치 표에 넣는다 (`video_guide.md` 3-1-1 · layout-check).
