# 주식 이야기 영상 종이인형 9장 — ChatGPT용 (읽고 1번부터 차례로 모두 만들어 저장소에 올리기)

이 파일 판: v3.0 — 2026-10-21 19:49 UTC (KST 04:49) — 표정 있는 종이인형. 사람이 고치는 파일 — 인물 설명은 `stock/story/protagonist.md` 8번과 같아야 한다.

쓰임: 주식 이야기 영상 '개미 재기 일지'는 **종이인형극**으로 만든다. 일본 축제 영상과 같은 방식이다.
- 무대 = 배경 그림 1장 + 인형마다 **투명 그림 1장**.
- 걷기·흔들림·기울기·뒤집기 같은 움직임은 코드로 준다 (`video/render/puppet.js`).
- **인형은 모두 표정이 있다.** 표정은 코드로 바꿀 수 없어서, **자세와 표정마다 한 장씩** 그린다.
- 1~8번은 모두 주인공 **구본석**(가상 인물)이다 — 같은 비율, 같은 색종이, 같은 얼굴·안경·점퍼·머리. 표정과 자세만 다르다.
- 9번은 4화의 개미 투자자 무리다.

참고 그림 (얼굴 생김새·옷·머리·안경·체형 참고): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/e49a4733606040e19a907f49ce2e3bdbb3f8addb/stock/story/images/protagonist_sheet.jpg
- 그림체는 따르지 않는다 — 이 파일의 종이인형 그림체로 그린다. 얼굴 생김새(둥근 얼굴·눈썹·안경)는 비슷하게 그린다.

| 번호 | 파일 | 크기 | 자세 · 표정 (쓰는 곳) |
|---|---|---|---|
| 1 | `stock/story/puppet/P-BONSEOK.png` | 정사각 1024×1024 · 투명 | 서서 말하기 · 지쳤지만 다정한 옅은 미소 (모든 장면의 기본) |
| 2 | `stock/story/puppet/P-BONSEOK-WALK.png` | 정사각 1024×1024 · 투명 | 걷기(옆) · 담담하고 차분한 얼굴 (출근·이동) |
| 3 | `stock/story/puppet/P-BONSEOK-PHONE.png` | 정사각 1024×1024 · 투명 | 휴대폰 계좌를 보고 무너짐 · 손해를 알고 좌절한 얼굴 (도입 ① 상황) |
| 4 | `stock/story/puppet/P-BONSEOK-DESPAIR.png` | 정사각 1024×1024 · 투명 | 바닥에 주저앉아 이마를 짚음 · 질끈 감은 눈, 답답한 얼굴 (도입 ② 답답함) |
| 5 | `stock/story/puppet/P-BONSEOK-RESOLVE.png` | 정사각 1024×1024 · 투명 | 주먹을 쥐고 고개를 듦 · 굳게 다문 입, 결심한 눈 (도입 ③ 다짐 · 마무리) |
| 6 | `stock/story/puppet/P-BONSEOK-STUDY.png` | 정사각 1024×1024 · 투명 | 낮은 상 앞 노트북·공책 · 집중한 얼굴 (도입 ④ · 방법 찾기) |
| 7 | `stock/story/puppet/P-BONSEOK-BACK.png` | 정사각 1024×1024 · 투명 | 비스듬한 뒷모습 + 옆얼굴 · 큰 화면을 올려다보며 놀라고 깨닫는 얼굴 (백테스트 결과) |
| 8 | `stock/story/puppet/P-BONSEOK-SMILE.png` | 정사각 1024×1024 · 투명 | 손을 들어 응원 · 환하고 따뜻한 웃음 (마무리 '여러분의 투자도…') |
| 9 | `stock/story/puppet/P-CROWD.png` | 가로 1536×1024 · 투명 | 휴대폰을 들고 환호하는 개미 투자자 6명 · 신난 얼굴 (4화 FOMO) |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다.**
   - 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 특히 v2.0 의 '얼굴 없는 인형'과 v1.0 의 2D 애니메이션 그림체는 쓰지 않는다.
   - 답의 첫 줄에 이 파일 맨 위 '이 파일 판' 줄을 그대로 적는다.
1. 아래 9장을 **1번부터 차례로 모두** 만든다. 질문하지 말고 바로 만든다. **한 장에 프롬프트에 적힌 것만** 그린다 (다른 사람·물건을 같이 그리지 않는다).
   - 이미지 한도로 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다.
   - 모든 프롬프트 맨 앞에 아래 **STYLE**·**CUTOUT** 두 문단을 그대로 붙인다.
   - 1~8번에는 **CHARACTER** 문단도 붙인다.
3. **1~8번은 모두 같은 인형이다.**
   - 2번부터는 1번 그림과 얼굴 모양·머리 크기·몸 비율·색종이 색·안경·점퍼·뻗친 머리가 같아야 한다. 다르면 다시 그린다.
4. **표정이 핵심이다.** 장마다 프롬프트의 EXPRESSION 줄대로 그린다.
   - 표정은 작은 화면에서도 한눈에 읽혀야 한다 — 눈썹 모양·눈·입 모양을 또렷하게.
   - 좌절은 놀란 얼굴이 아니라 **손해를 알고 무너진 얼굴**이다 (미간을 찌푸림·처진 입꼬리·떨군 고개·처진 어깨).
5. **잘림 검사 (필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다.
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
6. 그림에 글자·숫자·기호·로고·워터마크를 넣지 않는다. 휴대폰·노트북 화면과 공책은 아무것도 없는 빈 면이다. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다.
7. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (예: `1. stock/story/puppet/P-BONSEOK.png`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
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

## 공통 문단 (프롬프트 맨 앞에 그대로 붙임 — STYLE·CUTOUT 은 모든 장, CHARACTER 는 1~8번)

```
STYLE: paper-cut puppet theater (layered papercraft), like a hand-made paper puppet show. Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited calm palette: deep indigo #1E2A4A, warm cream #F2E6CF, charcoal #2B2B2B, gold ochre #D9A441, muted crimson #B3202A, soft teal #3E8E87, plus the character colors below. Flat stage view, like a stage seen from the audience. People are paper puppets WITH clearly readable facial expressions: every face is built from small cut-paper pieces — almond-shaped dark eyes with a tiny white highlight, thin dark-brown paper eyebrows, a simple mouth cut from darker paper, and soft pink paper cheek circles. The expression must read at a glance even when the picture is small. Fictional people, not recognizable as any real person. Modern everyday Korean life today. No text, letters, numbers, logos or watermarks anywhere.
```

```
CUTOUT: the described subject only, as an isolated paper puppet cutout on a fully transparent background (PNG with alpha channel) — no ground, no cast shadow on the ground, no scenery, no frame, no other objects or people. A thin cream (#F2E6CF) paper border about 6 px wide runs around the outer silhouette, like a hand-cut puppet. The WHOLE subject must be fully visible with generous empty margin: nothing may touch or cross the canvas edges — keep at least 8% empty transparent space on every side (left, right, top and bottom). If a transparent background is impossible, make the whole background one flat pure chroma green #00FF00 with no shading, and use no green at all on the subject.
```

```
CHARACTER (exactly the same paper puppet in every image — same face shape, proportions and paper colors; only the pose and the expression change): Gu Bonseok, a 44-year-old Korean office worker. Average height with a slightly soft build and a small round belly; his head is about one sixth of his height. Kind round face of warm beige skin paper #E8C39E, with the cut-paper face described in STYLE: dark almond eyes, thick-ish dark-brown eyebrows, a simple mouth, soft pink cheeks, slightly tired faint shadows under the eyes. Thin black rectangular glasses frames sit over his eyes (the eyes stay visible through the frames). Short neat black hair paper #1F1F1F parted on the left, a few light gray paper strands #A6A6A6 at the temples, and ONE small upturned cowlick sticking up at the crown. Gray-navy zip-up work jacket #3B4763 with no logo and a slightly lighter collar, over a light blue collared shirt #AFC6E3; dark charcoal-gray slacks #4A4D52; black sneakers #222222 with thin white soles.
```

## 1. P-BONSEOK — 기본 (서서 말하기)

**저장 경로: `stock/story/puppet/P-BONSEOK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE standing paper puppet of Gu Bonseok in a three-quarter view turned slightly to the right, toward the audience, both arms relaxed at his sides, head very slightly tilted forward as if he is talking to the viewer.
EXPRESSION: kind and a little tired — eyebrows relaxed, eyes soft and looking at the viewer, a faint gentle smile with the mouth slightly open as if speaking.
Centered; the top of his head (cowlick included) at about 12% of the canvas height and his feet at about 88%, with at least 8% empty margin on every side.
```

## 2. P-BONSEOK-WALK — 걷기 (옆모습)

**저장 경로: `stock/story/puppet/P-BONSEOK-WALK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE paper puppet of Gu Bonseok seen from the side, facing right, walking mid-stride: front leg forward, back heel lifted, one arm swinging forward and the other hand holding a small black smartphone down by his side (a plain dark shape, no screen content). His face is seen in profile.
EXPRESSION: calm and steady — eyebrows level, eyes looking straight ahead, mouth closed in a small neutral line.
Same size as a standing puppet: the top of his head at about 12% of the canvas height and his feet at about 88%. Centered, with at least 8% empty margin on every side.
```

## 3. P-BONSEOK-PHONE — 계좌를 보고 무너짐

**저장 경로: `stock/story/puppet/P-BONSEOK-PHONE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE paper puppet of Gu Bonseok standing in a three-quarter view facing right, staring down at a smartphone held in both hands at chest height, as if he has just seen a huge loss in his stock account. His head hangs low, his shoulders slump forward, his back is rounded and his knees are slightly bent. The phone screen is a plain pale blue glowing rectangle with nothing on it; its glow lights his face from below.
EXPRESSION: crushed by the loss he has just understood — eyebrows knitted together and tilted up in the middle, eyes wide and fixed on the phone, the corners of the mouth pulled down with the lips slightly parted. Not simply surprised: devastated and hopeless. The whole face stays clearly visible.
Centered; the top of his head at about 16% of the canvas height and his feet at about 88%, with at least 8% empty margin on every side.
```

## 4. P-BONSEOK-DESPAIR — 주저앉아 이마를 짚음

**저장 경로: `stock/story/puppet/P-BONSEOK-DESPAIR.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE paper puppet of Gu Bonseok sitting on the floor (do not draw the floor) in a three-quarter view facing right: knees pulled up, one forearm resting on his knee, the other hand pressed against his forehead with the fingers in his hair, back curled. His face is turned slightly toward the viewer and stays clearly visible below the hand.
EXPRESSION: frustrated and stuck — eyes squeezed shut, eyebrows knitted hard, mouth pressed into a tight downturned line, as if sighing "what did I do wrong".
His glasses are still on and the cowlick still sticks up. Centered; the figure fills about 60% of the canvas height and its bottom is at about 84%, with at least 8% empty margin on every side.
```

## 5. P-BONSEOK-RESOLVE — 다짐

**저장 경로: `stock/story/puppet/P-BONSEOK-RESOLVE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE standing paper puppet of Gu Bonseok in a three-quarter view turned slightly to the right, standing tall with his chest out and his head up: one fist clenched firmly in front of his chest, the other arm straight at his side with a closed hand.
EXPRESSION: quiet, steady determination to start again — eyebrows lowered and straight, eyes bright and looking forward, lips pressed together into a firm small smile.
Centered; the top of his head at about 12% of the canvas height and his feet at about 88%, with at least 8% empty margin on every side.
```

## 6. P-BONSEOK-STUDY — 복기·공부

**저장 경로: `stock/story/puppet/P-BONSEOK-STUDY.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE paper puppet of Gu Bonseok seen in a three-quarter side view facing right, sitting cross-legged on the floor (do not draw the floor) behind a small low wooden folding table. On the table: an open laptop whose screen is a plain pale blank glowing panel, and an open notebook with blank pages. He holds a pen over the notebook in one hand and rests his chin on the other hand, head tilted down, his face clearly visible.
EXPRESSION: deep concentration — eyebrows slightly knitted, eyes looking down at the notebook, lips pressed into a small thoughtful pout.
The table, laptop and notebook are part of this one cutout and fully inside the canvas. Centered; the whole group spans about 15% to 85% of the width and fills about 62% of the canvas height, with at least 8% empty margin on every side.
```

## 7. P-BONSEOK-BACK — 비스듬한 뒷모습 (큰 화면을 올려다봄)

**저장 경로: `stock/story/puppet/P-BONSEOK-BACK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE standing paper puppet of Gu Bonseok seen from behind at a three-quarter angle (back and left shoulder toward the viewer), his head turned up and to the left so that his face is clearly visible in profile, looking up at a big screen high in front of him (do not draw the screen). Both arms relaxed at his sides. We see the back of the gray-navy work jacket, the charcoal slacks, the black sneakers, the black hair with gray strands at the temple, the cowlick at the crown and the glasses on his profile.
EXPRESSION: surprised realization — eyebrows raised, eyes wide and fixed upward, mouth slightly open, as if he has just understood something important.
Centered; the top of his head at about 12% of the canvas height and his feet at about 88%, with at least 8% empty margin on every side.
```

## 8. P-BONSEOK-SMILE — 응원 (환한 웃음)

**저장 경로: `stock/story/puppet/P-BONSEOK-SMILE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE standing paper puppet of Gu Bonseok facing the viewer in a slight three-quarter view, one hand raised to shoulder height with an open palm as if cheering the viewer on, the other hand relaxed at his side.
EXPRESSION: warm, bright and hopeful — eyes curved into happy crescents behind the glasses, eyebrows relaxed and slightly raised, a wide genuine smile showing a little row of white paper teeth, rosy cheeks.
Centered; the top of his head at about 12% of the canvas height and his feet at about 88%, with at least 8% empty margin on every side (the raised hand must not touch the edge).
```

## 9. P-CROWD — 환호하는 개미 투자자 6명 (4화)

**저장 경로: `stock/story/puppet/P-CROWD.png`** — PNG 투명 700KB 이하 · 가로 1536×1024

CHARACTER 문단은 붙이지 않는다 — 주인공이 아닌 다른 사람들이다.

```
Landscape 1536x1024, front-side view. ONE tight group of SIX different Korean retail investors standing close together in a row (they may overlap each other slightly): men and women in their 20s to 50s in everyday clothes (a hoodie, an office shirt and tie, a cardigan, a padded vest, a polo shirt, a blouse) in muted paper colors — none of them wears glasses with a gray-navy work jacket, so none looks like Gu Bonseok. Each holds up a smartphone (plain blank glowing screens) and cheers: some raise a fist, some hold the phone high toward the viewer.
EXPRESSION: every face is excited and thrilled — big open-mouthed smiles, raised eyebrows, eyes shining, as if they have all just made money.
All six are about the same height; their heads at about 18% and their feet at about 88% of the canvas height. The group spans about 10% to 90% of the width, with at least 8% empty margin on every side.
```
