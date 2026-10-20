# test 종이인형극 이미지 14장 (3판) — ChatGPT용 (일본 전통 축제 롱폼·쇼츠 · 잘린 그림 다시 · 읽고 그대로 만들고 저장 경로에 올리기)

작성: 2026-10-20 (Claude, 3판) — 짝 문서 `test/일본축제_사망사고_제작안.txt` (v8.7) · 장면 `video/episodes/ilbon-chukje-2026-10/index.html`

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/test/puppet/images_chatgpt.md

**왜 다시 만드나:** 2판의 4개 묶음 그림(P-PEOPLE·P-ICONS·P-ICONS2)은 물건끼리 닿아 있어서, 영상에서 하나씩 떼어 쓸 때 옆 물건 조각이 붙거나 손끝·가장자리가 잘렸다. 가마꾼(P-LIFT)도 12명이 겹쳐 있어 두 무리로 가를 때 한 사람이 반으로 잘렸다.
→ 이번에는 **한 장에 하나씩**(가마꾼은 6명씩 두 장) 그린다. 그 밖의 그림(1판·2판의 P-BG·P-FLOAT·P-CROWD·P-DANJIRI·P-HADAKA·P-PEOPLE2·배경들)은 그대로 쓴다 — **다시 만들지 않는다.**

| 번호 | 파일 | 크기 | 무엇 |
|---|---|---|---|
| 1 | `test/puppet/P-MEN-L.png` | 가로 1536×1024 · 투명 | 가마꾼 6명 (두 팔을 머리 위로 쭉 뻗음) — 왼쪽 무리 |
| 2 | `test/puppet/P-MEN-R.png` | 가로 1536×1024 · 투명 | 가마꾼 6명 (같은 자세) — 오른쪽 무리 |
| 3 | `test/puppet/P-PEOPLE-1.png` | 정사각 1024×1024 · 투명 | 어린이 (줄을 잡음) |
| 4 | `test/puppet/P-PEOPLE-2.png` | 정사각 1024×1024 · 투명 | 청년 (주먹을 듦) |
| 5 | `test/puppet/P-PEOPLE-3.png` | 정사각 1024×1024 · 투명 | 젊은 리더 (부채를 들고 앞을 가리킴) |
| 6 | `test/puppet/P-PEOPLE-4.png` | 정사각 1024×1024 · 투명 | 원로 (기모노·하오리, 뒷짐) |
| 7 | `test/puppet/P-ICONS-1.png` | 정사각 1024×1024 · 투명 | 료칸 (작은 여관) |
| 8 | `test/puppet/P-ICONS-2.png` | 정사각 1024×1024 · 투명 | 축제 포장마차 |
| 9 | `test/puppet/P-ICONS-3.png` | 정사각 1024×1024 · 투명 | 두 칸짜리 전철 |
| 10 | `test/puppet/P-ICONS-4.png` | 정사각 1024×1024 · 투명 | 시청 건물 |
| 11 | `test/puppet/P-ICONS2-1.png` | 정사각 1024×1024 · 투명 | 경주용 차 (F1) |
| 12 | `test/puppet/P-ICONS2-2.png` | 정사각 1024×1024 · 투명 | AED 상자 |
| 13 | `test/puppet/P-ICONS2-3.png` | 정사각 1024×1024 · 투명 | 방송 카메라 + 마이크 |
| 14 | `test/puppet/P-ICONS2-4.png` | 정사각 1024×1024 · 투명 | 경찰차 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 14장을 1번부터 차례로 만든다. 질문하지 말고 바로 만든다. **한 장에 프롬프트에 적힌 것만** 그린다 (다른 사람·물건을 같이 그리지 않는다).
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다. 모든 프롬프트 맨 앞에 아래 **공통 화풍** 문단과 **CUTOUT** 문단을 그대로 붙인다 (1·2판 그림과 같은 화풍 — 한 무대의 인형처럼).
3. **잘림 검사 (필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`이면 그림을 더 작게(여백을 더 넓게) 다시 만들고 다시 검사한다. 투명이 아니면(귀퉁이 알파가 0 이 아님) 배경을 **순초록 #00FF00 한 색 평면**으로 다시 만든다 (그때는 초록 바탕 기준으로 여백을 본다).
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
4. 그림에 글자·숫자·로고·워터마크를 넣지 않는다. 사람은 얼굴 이목구비가 없는 종이 인형으로 그리고, 피·다친 사람은 그리지 않는다.
5. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`3. test/puppet/P-PEOPLE-1.png`). 그림 안에는 쓰지 않는다.
6. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (`test/puppet/` 폴더, 대소문자·하이픈까지 같게).
   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다. 올린 뒤 GitHub 에 있는 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다. PNG(투명 유지)는 아래 코드 그대로.
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
   - **GitHub 앱으로 커밋한다.** 커밋 메시지: `[test] puppet <파일 이름> 이미지` (예: `[test] puppet P-MEN-L.png 이미지`). 올린 뒤 파일 경로와 커밋 링크를 적는다.
   - **올리기가 실패하면** (권한·연결 오류) 묻지 말고 그림을 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"이 그림을 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 저장 경로에 올립니다."** 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 표의 파일 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/test/puppet 에 끌어다 놓고 Commit changes"
7. 이미지 한도로 멈추면 사용자가 "계속"이라고 보낸다 — 그때 다음 번호부터 이어서 만든다.

## 공통 화풍 (모든 프롬프트 맨 앞에 그대로 붙임)

```
STYLE: Japanese paper-cut puppet theater (kiri-e papercraft). Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited warm dusk palette: deep indigo #1E2A4A, crimson #B3202A, gold ochre #D9A441, warm cream #F2E6CF, charcoal #2B2B2B, lantern orange #F08A2E. Flat side view, like a stage seen from the audience. People are simple paper puppets with round plain heads and NO facial features (no eyes, nose or mouth), not recognizable as any real person. No text, letters, numbers, logos or watermarks anywhere.
```

```
CUTOUT: the described subject only, as an isolated paper puppet cutout on a fully transparent background (PNG with alpha channel) — no ground, no cast shadow on the ground, no scenery, no frame, no other objects or people. A thin cream (#F2E6CF) paper border about 6 px wide runs around the outer silhouette, like a hand-cut puppet. The WHOLE subject must be fully visible with generous empty margin: nothing may touch or cross the canvas edges — keep at least 8% empty transparent space on every side (left, right, top and bottom). If a transparent background is impossible, make the whole background one flat pure chroma green #00FF00 with no shading, and use no green at all on the subject.
```

## 1. P-MEN-L — 가마꾼 6명 (왼쪽 무리)

**저장 경로: `test/puppet/P-MEN-L.png`** — PNG 투명 700KB 이하 · 가로 1536×1024

```
Landscape 1536x1024, side view. A row of SIX festival float carriers walking in step, all facing right, close together in one tight group (they may overlap each other slightly), each pushing both arms fully stretched straight up above his head with open hands at the same height, as if holding up a heavy wooden pole overhead — but draw NO pole and NO float, only the men. Each man wears a white happi coat with an indigo wave pattern on the lower part, a white twisted headband, dark indigo pants and dark split-toe tabi shoes, and has tan skin. All six are the same height; their raised hands form one flat line at about 12% of the canvas height and their feet stand on one flat line at about 90% of the height. The group spans from about 10% to 90% of the width, with at least 8% empty margin on the left and right.
```

## 2. P-MEN-R — 가마꾼 6명 (오른쪽 무리)

**저장 경로: `test/puppet/P-MEN-R.png`** — PNG 투명 700KB 이하 · 가로 1536×1024

```
Landscape 1536x1024, side view. Exactly the same kind of group as before: a row of SIX festival float carriers walking in step, all facing right, close together in one tight group (they may overlap each other slightly), each pushing both arms fully stretched straight up above his head with open hands at the same height, as if holding up a heavy wooden pole overhead — but draw NO pole and NO float, only the men. Same clothes, same colors and same size as the previous image: white happi coat with an indigo wave pattern on the lower part, white twisted headband, dark indigo pants, dark split-toe tabi shoes, tan skin. Raised hands on one flat line at about 12% of the canvas height, feet on one flat line at about 90%. The group spans from about 10% to 90% of the width, with at least 8% empty margin on the left and right. Slightly different poses from the previous group so they do not look copied.
```

## 3. P-PEOPLE-1 — 어린이

**저장 경로: `test/puppet/P-PEOPLE-1.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, side view facing right, standing. ONE small child (about 8 years old) in a small red happi coat with a white pattern, a red-and-white twisted headband and dark shorts, holding a thick red-and-white festival rope with both hands, leaning forward as if pulling. Only a short piece of the rope, fully inside the canvas. The child is centered and fills about 70% of the canvas height, with at least 8% empty margin on every side.
```

## 4. P-PEOPLE-2 — 청년

**저장 경로: `test/puppet/P-PEOPLE-2.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, side view facing right, standing. ONE young man in his early 20s in a white happi coat with a red crest, a black-and-white patterned obi belt, white shorts and a white twisted headband, one fist raised high with energy. Centered, fills about 75% of the canvas height, with at least 8% empty margin on every side (the raised fist must not touch the top).
```

## 5. P-PEOPLE-3 — 젊은 리더

**저장 경로: `test/puppet/P-PEOPLE-3.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, side view facing right, standing in a wide confident stance. ONE man in his 30s, the young leader, in an indigo happi coat with gold wave patterns and a white crest, a white headband, holding a round paper fan (red and gold crest design) up high in one hand and pointing forward with the other hand. The whole fan and the pointing fingertips must be fully inside the canvas. Centered, fills about 75% of the canvas height, with at least 8% empty margin on every side.
```

## 6. P-PEOPLE-4 — 원로

**저장 경로: `test/puppet/P-PEOPLE-4.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, side view facing right, standing calmly. ONE elderly man in his 70s, the respected elder of the neighborhood, grey hair tied back, in a dark black kimono with a black haori jacket bearing a small gold crest and a brown striped hakama, hands behind his back. Centered, fills about 72% of the canvas height, with at least 8% empty margin on every side.
```

## 7. P-ICONS-1 — 료칸

**저장 경로: `test/puppet/P-ICONS-1.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, front-side view. ONE small traditional Japanese inn (ryokan): a two-story wooden building with dark tiled roofs, a short indigo noren curtain at the entrance with no letters, warm glowing windows and a small paper lantern by the door. Centered, fills about 70% of the canvas width and height, with at least 8% empty margin on every side.
```

## 8. P-ICONS-2 — 축제 포장마차

**저장 경로: `test/puppet/P-ICONS-2.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, front view. ONE festival food stall (yatai) with a red-and-white striped awning, two small red paper lanterns, a steaming pot and skewers on the counter, and a faceless cook in a white headband behind the counter. Centered, fills about 70% of the canvas width and height, with at least 8% empty margin on every side (the lanterns and awning must not touch the edges).
```

## 9. P-ICONS-3 — 전철

**저장 경로: `test/puppet/P-ICONS-3.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, side view. ONE short local train of exactly two cars, cream with an indigo band, windows lit, seen from the side, with a tiny bit of rail under the wheels. The whole train, both ends included, is fully inside the canvas: it spans about 10% to 90% of the width, vertically centered, with at least 8% empty margin on every side.
```

## 10. P-ICONS-4 — 시청 건물

**저장 경로: `test/puppet/P-ICONS-4.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, front view. ONE modern city hall building, plain white and light grey, several floors of windows, a flat roof with a flag pole and a plain white flag (no symbols, no letters), two small round trees at the sides. Centered, fills about 70% of the canvas height (flag included), with at least 8% empty margin on every side.
```

## 11. P-ICONS2-1 — 경주용 차

**저장 경로: `test/puppet/P-ICONS2-1.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, side view. ONE red Formula-1 style racing car seen from the side, with no numbers, sponsors or letters. The whole car, front wing and rear wing included, spans about 10% to 90% of the width, vertically centered, with at least 8% empty margin on every side.
```

## 12. P-ICONS2-2 — AED 상자

**저장 경로: `test/puppet/P-ICONS2-2.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, front view. ONE orange wall-mounted AED defibrillator box with only a simple white heart-and-lightning symbol, no letters, with a small dark wall bracket. Centered, fills about 65% of the canvas height, with at least 8% empty margin on every side.
```

## 13. P-ICONS2-3 — 방송 카메라

**저장 경로: `test/puppet/P-ICONS2-3.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, side view. ONE TV news camera on a black tripod, with a handheld microphone leaning against one tripod leg, no letters or logos. Centered, fills about 75% of the canvas height, with at least 8% empty margin on every side.
```

## 14. P-ICONS2-4 — 경찰차

**저장 경로: `test/puppet/P-ICONS2-4.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, side view. ONE Japanese-style black-and-white police car seen from the side with a red light on the roof, no letters or emblems. The whole car spans about 10% to 90% of the width, vertically centered, with at least 8% empty margin on every side.
```
