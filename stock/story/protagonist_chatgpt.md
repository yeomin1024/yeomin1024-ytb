# 주인공 종이인형 7장 — ChatGPT용 (읽고 1번부터 차례로 모두 만들어 저장소에 올리기)

이 파일 판: v2.0 — 2026-10-21 14:11 UTC (KST 23:11) — 종이인형극. 사람이 고치는 파일 — 인물 설명은 `stock/story/protagonist.md` 8번과 같아야 한다.

쓰임: 주식 이야기 영상은 **종이인형극**으로 만든다. 일본 축제 영상(`video/episodes/ilbon-chukje-2026-10/`)과 같은 방식이다.
- 무대 = 배경 그림 1장 + 인형마다 **투명 그림 1장**.
- 걷기·흔들림·기울기·뒤집기 같은 움직임은 모두 코드로 준다 (`video/render/puppet.js`).
- 그래서 주인공 **구본석**(가상 인물)을 **자세마다 한 장씩** 그린다.
- 7장 모두 **같은 종이인형**이다 — 같은 비율, 같은 색종이, 같은 안경·점퍼·머리.

참고 그림 (옷·머리·안경·체형만 참고): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/e49a4733606040e19a907f49ce2e3bdbb3f8addb/stock/story/images/protagonist_sheet.jpg
- 그림체와 얼굴은 따르지 않는다. 종이인형은 얼굴이 없다 — 안경만 있다.

| 번호 | 파일 | 크기 | 자세 (쓰는 곳) |
|---|---|---|---|
| 1 | `stock/story/puppet/P-BONSEOK.png` | 정사각 1024×1024 · 투명 | 기본 — 서서 말하기 (모든 장면의 기본 인형) |
| 2 | `stock/story/puppet/P-BONSEOK-WALK.png` | 정사각 1024×1024 · 투명 | 걷기 — 옆모습 (출근·이동) |
| 3 | `stock/story/puppet/P-BONSEOK-PHONE.png` | 정사각 1024×1024 · 투명 | 휴대폰으로 계좌를 보고 무너짐 (도입 ① 상황) |
| 4 | `stock/story/puppet/P-BONSEOK-DESPAIR.png` | 정사각 1024×1024 · 투명 | 바닥에 주저앉아 무릎에 얼굴을 묻음 (도입 ② 답답함) |
| 5 | `stock/story/puppet/P-BONSEOK-RESOLVE.png` | 정사각 1024×1024 · 투명 | 주먹을 쥐고 고개를 듦 (도입 ③ 다짐 · 마무리) |
| 6 | `stock/story/puppet/P-BONSEOK-STUDY.png` | 정사각 1024×1024 · 투명 | 낮은 상 앞에서 노트북·공책으로 복기 (도입 ④ · 방법 찾기) |
| 7 | `stock/story/puppet/P-BONSEOK-BACK.png` | 정사각 1024×1024 · 투명 | 뒷모습 — 큰 화면(코드로 그린 차트)을 올려다봄 (백테스트 결과) |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다.**
   - 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 특히 v1.0 의 2D 애니메이션 그림체는 쓰지 않는다.
   - 답의 첫 줄에 이 파일 맨 위 '이 파일 판' 줄을 그대로 적는다.
1. 아래 7장을 **1번부터 차례로 모두** 만든다. 질문하지 말고 바로 만든다. **한 장에 프롬프트에 적힌 것만** 그린다 (다른 사람·물건을 같이 그리지 않는다).
   - 이미지 한도로 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다. 모든 프롬프트 맨 앞에 아래 **STYLE**·**CUTOUT**·**CHARACTER** 세 문단을 그대로 붙인다.
3. **7장 모두 같은 인형이다.** 2번부터는 1번 그림과 머리 크기·몸 비율·색종이 색·안경·점퍼·뻗친 머리가 같아야 한다. 다르면 다시 그린다.
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
5. 그림에 글자·숫자·기호·로고·워터마크를 넣지 않는다. 휴대폰·노트북 화면과 공책은 아무것도 없는 빈 면이다. 인형은 눈·코·입이 없고 안경만 쓴다.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (예: `1. stock/story/puppet/P-BONSEOK.png`). 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 경로는 표의 파일 이름 그대로 (`stock/story/puppet/` 폴더, 대소문자·하이픈까지 같게).
   - **올리기 전에 700KB 이하로 만든다.**
     - GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다.
     - 올린 뒤 GitHub 에 있는 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     - **PNG(투명 유지)** 로 올린다 — JPEG 로 바꾸지 않는다 (JPEG 는 투명이 없어짐). 아래 코드 그대로.
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
   - **GitHub 앱으로 커밋한다.** 커밋 메시지: `[주인공] puppet <파일 이름> 이미지` (예: `[주인공] puppet P-BONSEOK.png 이미지`). 올린 뒤 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패하면** (권한·연결 오류) 묻지 말고 이렇게 한다:
     1. 그림을 한 번 더 보여 준다.
     2. 이 문장을 그대로 쓴다: **"이 그림을 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 표의 파일 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/story/puppet 에 끌어다 놓고 Commit changes"

## 공통 문단 (모든 프롬프트 맨 앞에 그대로 붙임)

```
STYLE: paper-cut puppet theater (layered papercraft), like a hand-made paper puppet show. Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited calm palette: deep indigo #1E2A4A, warm cream #F2E6CF, charcoal #2B2B2B, gold ochre #D9A441, muted crimson #B3202A, soft teal #3E8E87, plus the character colors below. Flat stage view, like a stage seen from the audience. People are simple paper puppets with round plain heads and NO facial features (no eyes, nose or mouth), not recognizable as any real person. Modern everyday Korean life today. No text, letters, numbers, logos or watermarks anywhere.
```

```
CUTOUT: the described subject only, as an isolated paper puppet cutout on a fully transparent background (PNG with alpha channel) — no ground, no cast shadow on the ground, no scenery, no frame, no other objects or people. A thin cream (#F2E6CF) paper border about 6 px wide runs around the outer silhouette, like a hand-cut puppet. The WHOLE subject must be fully visible with generous empty margin: nothing may touch or cross the canvas edges — keep at least 8% empty transparent space on every side (left, right, top and bottom). If a transparent background is impossible, make the whole background one flat pure chroma green #00FF00 with no shading, and use no green at all on the subject.
```

```
CHARACTER (exactly the same paper puppet in every image — same proportions, shapes and paper colors; only the pose changes): Gu Bonseok, a 44-year-old Korean office worker. Average height with a slightly soft build and a small round belly; his head is about one sixth of his height. Round plain head with NO eyes, NO nose and NO mouth, warm beige skin paper #E8C39E. Short neat black hair paper #1F1F1F parted on the left, a few light gray paper strands #A6A6A6 at the temples, and ONE small upturned cowlick sticking up at the crown. Thin black rectangular glasses frames sit on the blank face — the glasses are the only thing on the face. Gray-navy zip-up work jacket #3B4763 with no logo and a slightly lighter collar, over a light blue collared shirt #AFC6E3; dark charcoal-gray slacks #4A4D52; black sneakers #222222 with thin white soles.
```

## 1. P-BONSEOK — 기본 (서서 말하기)

**저장 경로: `stock/story/puppet/P-BONSEOK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE standing paper puppet of Gu Bonseok in a three-quarter view turned slightly to the right, toward the audience. Calm and natural: both arms relaxed at his sides, head very slightly tilted forward as if he is about to speak. Centered; the top of his head (cowlick included) at about 12% of the canvas height and his feet at about 88%, with at least 8% empty margin on every side.
```

## 2. P-BONSEOK-WALK — 걷기 (옆모습)

**저장 경로: `stock/story/puppet/P-BONSEOK-WALK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE paper puppet of Gu Bonseok seen from the side, facing right, walking mid-stride: front leg forward, back heel lifted, one arm swinging forward and the other hand holding a small black smartphone down by his side (the phone is a plain dark shape, no screen content). Same size as a standing puppet: the top of his head at about 12% of the canvas height and his feet at about 88%. Centered, with at least 8% empty margin on every side.
```

## 3. P-BONSEOK-PHONE — 계좌를 보고 무너짐

**저장 경로: `stock/story/puppet/P-BONSEOK-PHONE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE paper puppet of Gu Bonseok standing, seen from the side, facing right, staring down at a smartphone held in both hands at chest height, as if he has just seen a huge loss in his stock account. His head hangs low, his shoulders slump forward, his back is rounded and his knees are slightly bent — completely deflated. The phone screen is a plain pale blue glowing rectangle with nothing on it. Centered; the top of his head at about 16% of the canvas height and his feet at about 88%, with at least 8% empty margin on every side.
```

## 4. P-BONSEOK-DESPAIR — 주저앉아 얼굴을 묻음

**저장 경로: `stock/story/puppet/P-BONSEOK-DESPAIR.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE paper puppet of Gu Bonseok sitting on the floor (do not draw the floor), seen in a three-quarter side view facing right: knees pulled up, both arms wrapped around his knees, his forehead resting on his arms, back curled — completely defeated and stuck. His glasses are still visible at the side of his head, and the cowlick still sticks up. Centered; the figure fills about 58% of the canvas height and its bottom is at about 84%, with at least 8% empty margin on every side.
```

## 5. P-BONSEOK-RESOLVE — 다짐

**저장 경로: `stock/story/puppet/P-BONSEOK-RESOLVE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE standing paper puppet of Gu Bonseok in a three-quarter view turned slightly to the right, standing tall with his chest out and his head up, looking forward: one fist clenched firmly in front of his chest, the other arm straight at his side with a closed hand — quiet, steady determination to start again. Centered; the top of his head at about 12% of the canvas height and his feet at about 88%, with at least 8% empty margin on every side.
```

## 6. P-BONSEOK-STUDY — 복기·공부

**저장 경로: `stock/story/puppet/P-BONSEOK-STUDY.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE paper puppet of Gu Bonseok seen from the side, facing right, sitting cross-legged on the floor (do not draw the floor) behind a small low wooden folding table. On the table: an open laptop whose screen is a plain pale blank glowing panel, and an open notebook with blank pages. He holds a pen over the notebook in one hand and rests his chin on the other hand, head tilted down — thinking hard. The table, laptop and notebook are part of this one cutout and fully inside the canvas. Centered; the whole group spans about 15% to 85% of the width and fills about 62% of the canvas height, with at least 8% empty margin on every side.
```

## 7. P-BONSEOK-BACK — 뒷모습 (큰 화면을 올려다봄)

**저장 경로: `stock/story/puppet/P-BONSEOK-BACK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE standing paper puppet of Gu Bonseok seen from behind (back view), his head tilted slightly up as if looking at a big screen high in front of him (do not draw the screen). Both arms relaxed at his sides. From behind we see the back of his black hair with the gray strands at the temples, the cowlick at the crown, the arms of his glasses over his ears, the gray-navy work jacket, the charcoal slacks and the black sneakers. Centered; the top of his head at about 12% of the canvas height and his feet at about 88%, with at least 8% empty margin on every side.
```
