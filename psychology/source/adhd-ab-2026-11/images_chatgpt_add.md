# adhd-ab-2026-11 — 일상툰 추가 그림 2장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.1 — 2026-11-24 — 추가 요청. 까닭: 도입부 「할 일을 미루고 휴대폰만 보다가 하루가 지나감 → 밤에 '나는 왜 이렇게 게으를까' 자책」 장면 — 지금은 배경 없는 화면 (사용자 지시 2026-11-24 "나는 왜 이렇게 게으를까 부분에 배경이 없는데 내용에 맞는 이미지를 넣고").

- **그림체 기준 = 이미 저장소에 올린 A-REF 그림** — https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/psychology/source/adhd-ab-2026-11/puppet/motion/A-REF.png
  이 그림(약 3등신 어른 · 둥근 선 · 부드러운 파스텔 · 갈색 선)과 **같은 사람이 그린 것처럼** 그린다. 이 대화에서 앞서 이 편 그림을 만들었다면 그 그림체 그대로. 주소를 열 수 없으면 사용자에게 A-REF 그림을 붙여 달라고 한 번만 말한다.
- 그림에는 글자·숫자·로고가 하나도 없다 (말풍선·자막·시계 바늘은 코드). 누구도 나쁜 사람으로 그리지 않는다. 가상 인물. ※ 연구·교육용 영상 — 의학적 진단·처방이 아니다.

| 번호 | 저장 경로 (모두 `psychology/source/adhd-ab-2026-11/` 아래) | 무엇 | 대본 |
|---|---|---|---|
| 1 | `puppet/BG-INTRO-ROOM.jpg` | 도입 무대: 혼자 사는 원룸 (늦은 오후 — 밤은 코드로 어둡게) | 도입 1~2 |
| 2 | `puppet/motion/V01.png` | V: (침대 끝에 앉아) 휴대폰 보며 웃음 → 화면에 빠져 멍함 → 휴대폰을 내려놓고 이마를 짚으며 자책 | 도입 1~2 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. 이 주소를 지금 새로 열어 그 내용만 쓴다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 1~2번 **2장을 번호 순서대로 모두** 만든다. 질문하지 말고 멈추지 않는다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 앞에 아래 블록을 이 순서로 붙인다.
   - **배경(1번)**: 공통 화풍 → 배경판 → 프롬프트.
   - **동작 그림(2번)**: 공통 화풍 → 인물 → CUTOUT → MOTION STRIP → 프롬프트.
3. **동작 그림은 한 장에 같은 사람을 3번** — 왼쪽 → 가운데 → 오른쪽이 한 동작을 이어 그린 3장. 같은 크기·같은 자리·같은 방향·같은 옷, 앉은 자리(엉덩이·발바닥)가 같은 높이, 움직이는 부분만 바뀐다. 서로 겹치거나 칸(가로 3등분)을 넘지 않는다. 다른 사람·배경·바닥 그림자 없음.
4. **검사 (동작 그림, 올리기 전에):** 아래 코드로 `check(경로, cols=3, feet=True)` 가 `OK` 여야 올린다. 투명이 아니면 배경을 순자홍 #FF00FF 한 색 평면으로 다시 만든다.
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
   # 기준 그림·동작 그림: check(경로, cols=3, feet=True) · 소품 판: check(경로, cols=4, margin=0.02)
   ```
5. 화면·휴대폰·종이·포스트잇·시계에도 글자·숫자가 없다. 만든 뒤 확대해 글자가 보이면 다시 만든다.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. psychology/source/adhd-ab-2026-11/puppet/BG-INTRO-ROOM.jpg`).
7. **저장소 `yeomin1024/yeomin1024-ytb` main 에 저장 경로 그대로 올린다** — 700KB 이하 (배경 JPEG: 1536×864 · 품질 90부터 5씩 낮춤 · 동작 PNG: 아래 코드).
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
   - GitHub 앱으로 장마다 커밋: `[psychology] adhd-ab-2026-11 <파일 이름> 이미지`. 다 올리면 파일 경로와 커밋 링크를 목록으로 적는다.
   - 올리기가 실패한 장만: "올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."

## 공통 화풍 (모든 프롬프트 맨 앞에 그대로 붙임)

```
STYLE: a simple, warm Korean daily-life webtoon (일상툰) look for a YouTube animation. Rounded simple shapes, thin clean dark-brown outlines, soft flat pastel colors with at most one light shading tone, very little detail. People are about 3 heads tall — a little cute but clearly adults (children smaller). Simple faces: small oval eyes, short eyebrows that carry the emotion, a small mouth; light pink cheeks only when embarrassed or crying. Simple comic marks are allowed only as shapes (one sweat drop, small sparkle lines, a little gloomy cloud scribble). Expressions must read instantly on a small phone screen. From picture 2 on, match EXACTLY the drawing style, line weight, colors and proportions of picture 1. Warm, gentle, emotionally honest mood — no horror, no violence, nobody is a villain. 2D drawing only — not 3D, not a photo, not glossy anime. Absolutely no text, letters, numbers, logos or watermarks anywhere — screens, phones, papers, books, boards, signs, clocks and packages are blank or show only simple shapes. Do not imitate any specific existing webtoon or artist.
```

## 배경판 (배경 — 공통 화풍 다음에 그대로 붙임)

```
BACKGROUND PLATE for a 2D daily-life webtoon animation: full-bleed landscape 1536x864, eye-level camera, NO people and no animals anywhere. Simple, clean webtoon background in the same style as the characters: few objects, soft pastel colors, light outlines. Leave a clear empty area in the front-center where characters will be placed later (a standing adult there would be about 75% of the picture height, feet near 92% of the height; a sitting person sits on the furniture described). Keep the middle calm and uncluttered.
```

## 인물 (동작 그림 — 공통 화풍 다음에 그대로 붙임)

```
CHARACTERS — the same face, hair, clothes, colors and proportions in every frame:
V — the 'viewer' of the opening: a 29-year-old Korean man living alone, short messy black hair, an oversized light gray sweatshirt, navy sweatpants, white socks. Ordinary and relatable, a little tired. He must look clearly different from A (32-year-old woman), B (51-year-old man) and S (14-year-old boy in a navy hoodie).
```

## CUTOUT (동작 그림 — 그다음에 그대로 붙임 · 배경에는 붙이지 않음)

```
CUTOUT: only the described subjects, as isolated cutouts on a fully transparent background (PNG with alpha channel) — no ground, no floor line, no cast shadow, no scenery, no frame, no other objects or people. Clean hard edges with the dark outline. Every subject must be fully visible with empty margin: nothing may touch or cross the canvas edges — keep at least 5% empty transparent space on every side. If a transparent background is impossible, make the whole background one flat pure magenta #FF00FF with no shading, and use no magenta, purple or hot pink at all on the subjects.
```

## MOTION STRIP (동작 그림 — CUTOUT 다음에 그대로 붙임)

```
MOTION STRIP: landscape 1536x1024, divided into three equal invisible columns. The three figures are three consecutive animation drawings of ONE continuous movement by the SAME person, like an animator's key pose, in-between and key pose: frame 1 in the left column, frame 2 in the center column, frame 3 in the right column. Between the frames keep everything identical except the moving parts: same scale, same camera angle, same facing direction, same clothes, colors and line weight, and the soles of the feet (or the legs of the stool, when sitting) on exactly the same invisible baseline at about 92% of the canvas height, at the same horizontal spot in each column — the body stays in place and only the arms, hands, head, face, torso lean and held objects move. A standing adult is about 70% of the canvas height (top of the head near 22%) — a sitting adult or a child is smaller in the same scale. Any object held in the hands keeps the same design and size in all three frames and stays inside the same column. Each figure is centered in its column, full body from head to shoes, and never crosses a column border; leave clear empty space between the columns. No motion lines, no effects, no flying objects unless the prompt asks for them.
```

## 1. BG-INTRO-ROOM — 도입 무대: 혼자 사는 원룸 (늦은 오후 — 밤은 코드로 어둡게)

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-INTRO-ROOM.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
A small one-room studio apartment of a young office worker who lives alone, seen straight from the front. LEFT third: a desk against the wall with a closed laptop, a messy stack of blank papers, a few blank yellow sticky notes on the wall above the desk (no writing at all), a desk lamp. CENTER and RIGHT: a single bed with a rumpled light-blue blanket and two pillows, its long side facing us, the mattress top at about 55% of the picture height; a small side table with a phone charger cable. A window on the back wall above the bed shows a warm late-afternoon sky (orange and pink) over city buildings. A plain wall area at the upper right (about 15% wide) is empty — a wall clock will be added there by code. Leave the floor in front of the bed and the bed itself empty of people. No text anywhere.
```

## 2. V01 — V: (침대 끝에 앉아) 휴대폰 보며 웃음 → 화면에 빠져 멍함 → 휴대폰을 내려놓고 이마를 짚으며 자책

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/V01.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, sitting on the edge of an invisible bed, facing the viewer, feet on the floor, both shoes off (socks). Frame 1: holding a phone with both hands, smiling at the screen, relaxed. Frame 2: completely absorbed in the phone, empty eyes, face lit by the screen's glow, slouching. Frame 3: the phone dropped face-down on his lap, one hand on his forehead, eyes closed, a guilty sigh — blaming himself.
```

## 받은 뒤 (Claude)
- 확대 검수(그림체·글자 없음·발 높이) → `psychology/source/puppet_slice.py adhd-ab-2026-11` → 장면 파일 도입 장면에 넣고 다시 렌더.
