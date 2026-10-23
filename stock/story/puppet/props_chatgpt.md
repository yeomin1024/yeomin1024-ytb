# 개미 재기 일지 — 설명 소품 그림 21장 (ChatGPT 에 넘기는 파일)

이 파일 판: v1.0 — 2026-10-23 — 1화 설명 소품 21장 (사용자 지시 2026-10-23 "설명에 필요한 이미지 요소들은 왜 생성안해?"). 그림체는 인형 파일 `stock/story/protagonist_chatgpt.md` v3.0 의 STYLE·CUTOUT 문단과 같다 (한 무대의 종이 소품).

쓰임: 영상 화면에는 글자가 없다(외국인 시청자 — 말은 언어별 자막). 그래서 **어려운 말·비유를 그림 한 장으로** 보여 준다 — 무대 위에 인형처럼 세우는 **종이 소품**이다. 숫자는 코드가 그림 위에 따로 띄운다. 장면 표 문법은 `stock/guides/quick_story.md` D-2 (`*이름`), 무대 코드 `video/render/story.js` v1.4. 다음 화에서 새 소품이 필요하면 이 표 끝에 번호를 이어 더한다 (같은 소품은 여러 화에서 다시 써도 된다 — 겹치면 안 되는 것은 경험·근거·숫자·문장).

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다.** 답의 첫 줄에 위 '이 파일 판' 줄을 그대로 적는다.
1. 아래 21장을 **1번부터 차례로 모두** 만든다. 질문하지 말고 바로 만든다. **한 장에 프롬프트에 적힌 것만** 그린다 (사람·인형을 같이 그리지 않는다).
   - 이미지 한도로 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 아래 **STYLE**·**CUTOUT**·**PROP** 세 문단을 그대로 붙인다.
3. **글자·숫자·기호(₩ $ % 등)·로고·국기를 그림에 넣지 않는다.** 휴대폰 화면·신문·종이·간판은 빈 면이다. 숫자는 영상 코드가 따로 띄운다.
4. **잘림 검사 (필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다.
   - `잘림`이면 그림을 더 작게(여백을 더 넓게) 다시 만들고 다시 검사한다.
   - 투명이 아니면(귀퉁이 알파가 0 이 아님) 배경을 **순초록 #00FF00 한 색 평면**으로 다시 만든다 (그때는 초록 바탕 기준으로 여백을 본다).
   ```python
   from PIL import Image
   import numpy as np
   def check(path, margin=0.06):
       a = np.array(Image.open(path).convert("RGBA"))
       h, w = a.shape[:2]
       if a[2, 2, 3] > 0:                       # 투명이 아니면 순초록 바탕을 빈 곳으로 봄
           g = a[:, :, 1].astype(int) - np.maximum(a[:, :, 0], a[:, :, 2]).astype(int)
           filled = ~((g > 80) & (a[:, :, 1] > 150))
       else:
           filled = a[:, :, 3] > 40
       ys, xs = np.where(filled)
       box = (xs.min() / w, ys.min() / h, xs.max() / w, ys.max() / h)
       ok = box[0] >= margin and box[1] >= margin and box[2] <= 1 - margin and box[3] <= 1 - margin
       print(path, "OK" if ok else "잘림 — 더 작게 다시", [round(v, 3) for v in box])
       return ok
   ```
5. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (예: `1. stock/story/puppet/props/PHONE-ALERT.png`). 그림 안에는 쓰지 않는다.
6. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, `stock/story/puppet/props/` 폴더, 파일 이름은 표 그대로 (대문자·하이픈까지 같게).
   - **PNG(투명 유지) 700KB 이하**로 올린다 — GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다. JPEG 로 바꾸지 않는다 (투명이 없어짐). 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다. 아래 코드 그대로:
   ```python
   from PIL import Image
   import os
   Q = getattr(Image, "Quantize", Image).FASTOCTREE
   def save_png(src, dst, limit=700_000):
       im = Image.open(src).convert("RGBA")
       w, h = im.size
       s = min(1.0, 1400 / max(w, h))
       while True:
           cur = im.resize((round(w * s), round(h * s)), Image.LANCZOS) if s < 1 else im
           cur.save(dst, optimize=True)
           if os.path.getsize(dst) > limit:
               cur.quantize(colors=256, method=Q).save(dst, optimize=True)   # 256색 (투명 유지)
           if os.path.getsize(dst) <= limit or max(cur.size) <= 800:
               break
           s *= 0.9
       print(dst, os.path.getsize(dst), cur.size)
   ```
   - **GitHub 앱으로 커밋한다.** 커밋 메시지: `[주인공] puppet props <파일 이름> 소품` (예: `[주인공] puppet props PHONE-ALERT.png 소품`). 올린 뒤 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패하면** (권한·연결 오류) 묻지 말고: 그림을 한 번 더 보여 주고, 이 문장을 그대로 쓴다 — **"이 그림을 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 저장 경로에 올립니다."** 직접 올리는 길: 그림을 표의 파일 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/story/puppet/props 에 끌어다 놓고 Commit changes.

## 공통 문단 (프롬프트 맨 앞에 그대로 붙임 — 21장 모두)

```
STYLE: paper-cut puppet theater (layered papercraft), like a hand-made paper puppet show. Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited calm palette: deep indigo #1E2A4A, warm cream #F2E6CF, charcoal #2B2B2B, gold ochre #D9A441, muted crimson #B3202A, soft teal #3E8E87, plus the character colors below. Flat stage view, like a stage seen from the audience. People are paper puppets WITH clearly readable facial expressions: every face is built from small cut-paper pieces — almond-shaped dark eyes with a tiny white highlight, thin dark-brown paper eyebrows, a simple mouth cut from darker paper, and soft pink paper cheek circles. The expression must read at a glance even when the picture is small. Fictional people, not recognizable as any real person. Modern everyday Korean life today. No text, letters, numbers, logos or watermarks anywhere.
```

```
CUTOUT: the described subject only, as an isolated paper puppet cutout on a fully transparent background (PNG with alpha channel) — no ground, no cast shadow on the ground, no scenery, no frame, no other objects or people. A thin cream (#F2E6CF) paper border about 6 px wide runs around the outer silhouette, like a hand-cut puppet. The WHOLE subject must be fully visible with generous empty margin: nothing may touch or cross the canvas edges — keep at least 8% empty transparent space on every side (left, right, top and bottom). If a transparent background is impossible, make the whole background one flat pure chroma green #00FF00 with no shading, and use no green at all on the subject.
```

```
PROP: ONE single stage prop for the same paper puppet show (an object, not a person), as simple and bold as a puppet-theater prop so it reads at a glance when small on a stage. Seen from the front or a slight three-quarter view, standing on an invisible floor (its bottom edge flat). NO text, letters, numbers, digits, currency symbols, percent signs, logos, brand marks or flags anywhere — every screen, page, sign and label is completely blank.
```

## 21장

| 번호 | 저장 경로 | 무엇 (쓰는 곳) |
|---|---|---|
| 1 | `stock/story/puppet/props/PHONE-ALERT.png` | 빚부터 강제로 빠져나감 (반대매매) (1화 2) |
| 2 | `stock/story/puppet/props/PIGGY.png` | 노후 자금이 조금만 남음 (1화 4) |
| 3 | `stock/story/puppet/props/NOTEBOOK.png` | 지킬 것을 적은 노트 · 원칙 (1화 8 · 72) |
| 4 | `stock/story/puppet/props/ONE-BASKET.png` | 한 업종에 몰빵 (반도체만) (1화 13~15 · 50~51) |
| 5 | `stock/story/puppet/props/BARRIER.png` | 거래가 20분 멈춤 (1화 16) |
| 6 | `stock/story/puppet/props/BOX.png` | 박스피 — 오랫동안 상자 안에 갇힌 지수 (1화 22) |
| 7 | `stock/story/puppet/props/BIG-BASKET.png` | 500개 회사를 나눠 담은 지수 (1화 23 · 27~28 · 44) |
| 8 | `stock/story/puppet/props/TRASH.png` | 주식 앱을 지울 생각 (1화 31) |
| 9 | `stock/story/puppet/props/STAMP.png` | 떠나는 순간 손실이 확정됨 (1화 32) |
| 10 | `stock/story/puppet/props/RUIN.png` | 한 종목은 끝내 회복 못 할 수도 (1화 45) |
| 11 | `stock/story/puppet/props/WAVE.png` | 거시 경제 — 시장 전체를 움직이는 큰 흐름 (1화 47) |
| 12 | `stock/story/puppet/props/NEWS.png` | 종목 뉴스·호재 기사만 봄 (1화 48~49) |
| 13 | `stock/story/puppet/props/STORM.png` | 여러 걱정이 한꺼번에 덮침 (1화 52) |
| 14 | `stock/story/puppet/props/BANK.png` | 금리가 오르면 돈이 예금으로 (1화 53) |
| 15 | `stock/story/puppet/props/BALLOON.png` | 시장 전체가 빚으로 달림 (1화 58) |
| 16 | `stock/story/puppet/props/GAUGE.png` | 내가 무리하는지 점검 (1화 59~61) |
| 17 | `stock/story/puppet/props/CHAT.png` | 리딩방·단톡방에서 들은 종목 (1화 64~65) |
| 18 | `stock/story/puppet/props/ANCHOR.png` | 원칙이 있으면 흔들리지 않음 (1화 77~78) |
| 19 | `stock/story/puppet/props/TORTOISE.png` | 리스크를 줄이며 천천히 (1화 79~81 · 92) |
| 20 | `stock/story/puppet/props/TREE.png` | 천천히 쌓아 넣은 돈의 1.6배 (1화 87~88) |
| 21 | `stock/story/puppet/props/ROCKET.png` | 빨리 가려다 아예 못 감 (3배 레버리지) (1화 91) |

## 1. PHONE-ALERT — 빚부터 강제로 빠져나감 (반대매매)

**저장 경로: `stock/story/puppet/props/PHONE-ALERT.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 2

```
Square 1024x1024. ONE large smartphone standing upright, seen from the front. Its screen is plain glowing red with one big white warning-triangle shape on it (a plain triangle with a short bar and a dot inside — a warning sign, not a letter). Three plain paper banknotes (blank pale green-grey rectangles with no printing at all) are flying up out of the top of the screen and away to the right, as if the money is being pulled out.
Centered, with at least 8% empty transparent margin on every side.
```

## 2. PIGGY — 노후 자금이 조금만 남음

**저장 경로: `stock/story/puppet/props/PIGGY.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 4

```
Square 1024x1024. ONE small pale-pink paper piggy bank sitting alone, with a thin crack line on its side and only two plain gold coins (no marks) beside its feet. No face on the piggy bank — just a simple snout and ears.
Centered, with at least 8% empty transparent margin on every side.
```

## 3. NOTEBOOK — 지킬 것을 적은 노트 · 원칙

**저장 경로: `stock/story/puppet/props/NOTEBOOK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 8 · 72

```
Square 1024x1024. ONE open spiral notebook lying slightly tilted toward the viewer, its pages showing exactly five short blank lines, each line starting with an empty square checkbox; nothing is written. A yellow pencil rests across the pages.
Centered, with at least 8% empty transparent margin on every side.
```

## 4. ONE-BASKET — 한 업종에 몰빵 (반도체만)

**저장 경로: `stock/story/puppet/props/ONE-BASKET.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 13~15 · 50~51

```
Square 1024x1024. ONE small woven basket overloaded with a tall wobbly pile of identical dark-green computer chips (square chips with tiny silver legs on their sides), the pile leaning dangerously to one side, with two chips already falling off the top. Only one kind of item in the basket.
Centered, with at least 8% empty transparent margin on every side.
```

## 5. BARRIER — 거래가 20분 멈춤

**저장 경로: `stock/story/puppet/props/BARRIER.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 16

```
Square 1024x1024. ONE lowered red-and-white striped barrier arm (like a railway-crossing gate) fixed to its post, blocking the way, with a round red stop light glowing on top of the post. Next to the post stands a small round paper stopwatch with a plain dial and one hand — no numbers or tick marks.
Centered, with at least 8% empty transparent margin on every side.
```

## 6. BOX — 박스피 — 오랫동안 상자 안에 갇힌 지수

**저장 경로: `stock/story/puppet/props/BOX.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 22

```
Square 1024x1024. ONE open cardboard box seen from the front, with its flaps open. Inside the box a thick teal paper zigzag line (like a stock-chart line) bounces up and down, but every peak only bumps against the box rim — the line is trapped inside and cannot get out.
Centered, with at least 8% empty transparent margin on every side.
```

## 7. BIG-BASKET — 500개 회사를 나눠 담은 지수

**저장 경로: `stock/story/puppet/props/BIG-BASKET.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 23 · 27~28 · 44

```
Square 1024x1024. ONE large sturdy woven basket filled with many small, different paper buildings packed tightly together and all standing upright: factories with chimneys, office towers, small shops, a hospital, a warehouse, in many different colors — like a basket holding a whole small city.
Centered, with at least 8% empty transparent margin on every side.
```

## 8. TRASH — 주식 앱을 지울 생각

**저장 경로: `stock/story/puppet/props/TRASH.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 31

```
Square 1024x1024. ONE open metal trash can, and a smartphone standing tilted beside it. A small plain gold rounded square (an app icon with nothing on it) is shown in mid-air falling from the phone toward the trash can.
Centered, with at least 8% empty transparent margin on every side.
```

## 9. STAMP — 떠나는 순간 손실이 확정됨

**저장 경로: `stock/story/puppet/props/STAMP.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 32

```
Square 1024x1024. ONE big wooden rubber stamp with a round handle, pressing down onto a sheet of cream paper (part of the prop); on the paper, next to the stamp, there is one large stamped mark: a plain solid red circle ring with nothing inside it.
Centered, with at least 8% empty transparent margin on every side.
```

## 10. RUIN — 한 종목은 끝내 회복 못 할 수도

**저장 경로: `stock/story/puppet/props/RUIN.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 45

```
Square 1024x1024. ONE single small office building standing alone, cracked from the roof down the middle, its top floors crumbling with small paper pieces falling off. Faded grey and dull ochre colors.
Centered, with at least 8% empty transparent margin on every side.
```

## 11. WAVE — 거시 경제 — 시장 전체를 움직이는 큰 흐름

**저장 경로: `stock/story/puppet/props/WAVE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 47

```
Square 1024x1024. ONE huge curling ocean wave in deep indigo and soft teal paper layers, lifting many small paper boats of different colors up all at once.
Centered, with at least 8% empty transparent margin on every side.
```

## 12. NEWS — 종목 뉴스·호재 기사만 봄

**저장 경로: `stock/story/puppet/props/NEWS.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 48~49

```
Square 1024x1024. ONE folded newspaper whose columns are only blank grey bars (no letters at all), with one small picture of a dark-green computer chip printed on it, and a magnifying glass held close over that chip picture.
Centered, with at least 8% empty transparent margin on every side.
```

## 13. STORM — 여러 걱정이 한꺼번에 덮침

**저장 경로: `stock/story/puppet/props/STORM.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 52

```
Square 1024x1024. ONE big dark storm cloud with three white lightning bolts and slanted rain, hanging over a tiny cluster of small paper buildings below it.
Centered, with at least 8% empty transparent margin on every side.
```

## 14. BANK — 금리가 오르면 돈이 예금으로

**저장 경로: `stock/story/puppet/props/BANK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 53

```
Square 1024x1024. ONE classical bank building with four columns and a triangular roof (no sign, no writing), and a curving stream of plain gold coins flowing from the left into its open front door.
Centered, with at least 8% empty transparent margin on every side.
```

## 15. BALLOON — 시장 전체가 빚으로 달림

**저장 경로: `stock/story/puppet/props/BALLOON.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 58

```
Square 1024x1024. ONE huge over-inflated red balloon, stretched thin and shiny, tied with a string to a small stack of plain paper banknotes (blank rectangles), with one sharp silver pin floating close to the balloon.
Centered, with at least 8% empty transparent margin on every side.
```

## 16. GAUGE — 내가 무리하는지 점검

**저장 경로: `stock/story/puppet/props/GAUGE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 59~61

```
Square 1024x1024. ONE large round dashboard gauge like a car speedometer, with a green, a yellow and a red arc and one needle pointing into the red part. No numbers, no tick labels, no letters.
Centered, with at least 8% empty transparent margin on every side.
```

## 17. CHAT — 리딩방·단톡방에서 들은 종목

**저장 경로: `stock/story/puppet/props/CHAT.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 64~65

```
Square 1024x1024. ONE smartphone standing upright with many overlapping blank speech bubbles bursting out of its screen; some bubbles contain a small plain gold coin or a small green upward arrow, none contain any letters.
Centered, with at least 8% empty transparent margin on every side.
```

## 18. ANCHOR — 원칙이 있으면 흔들리지 않음

**저장 경로: `stock/story/puppet/props/ANCHOR.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 77~78

```
Square 1024x1024. ONE heavy dark iron ship anchor with a short thick rope, resting firmly upright, with a few small wavy paper lines around it suggesting moving water while the anchor stays still.
Centered, with at least 8% empty transparent margin on every side.
```

## 19. TORTOISE — 리스크를 줄이며 천천히

**저장 경로: `stock/story/puppet/props/TORTOISE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 79~81 · 92

```
Square 1024x1024. ONE calm tortoise walking steadily to the right, carrying a small neat stack of plain gold coins on its shell. Simple friendly animal, no clothes.
Centered, with at least 8% empty transparent margin on every side.
```

## 20. TREE — 천천히 쌓아 넣은 돈의 1.6배

**저장 경로: `stock/story/puppet/props/TREE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 87~88

```
Square 1024x1024. ONE young tree growing from a terracotta pot; its leaves are plain round gold coins.
Centered, with at least 8% empty transparent margin on every side.
```

## 21. ROCKET — 빨리 가려다 아예 못 감 (3배 레버리지)

**저장 경로: `stock/story/puppet/props/ROCKET.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024 · 쓰는 곳 1화 91

```
Square 1024x1024. ONE small toy rocket that has crashed nose-down into a small heap of brown paper earth (part of the prop), its body bent and broken, with a puff of grey smoke and a few torn paper pieces around it.
Centered, with at least 8% empty transparent margin on every side.
```

## 변경 이력

| 판 | 날짜 | 바꾼 것 |
|---|---|---|
| v1.0 | 2026-10-23 | 처음 만듦 — 1화 설명 소품 21장 (장면 표 `stock/source/pogi-sonjeol-2026-10/scenes.txt` 의 `*이름`) |
