# test 종이인형극 이미지 9장 — ChatGPT용 (일본 전통 축제 롱폼 도입 첫 문장 · 읽고 그대로 만들고 저장 경로에 올리기)

작성: 2026-10-20 (Claude, 1판) — 짝 문서 `test/일본축제_사망사고_제작안.txt` (v8.4) · 장면 `video/episodes/ilbon-chukje-2026-10/test_puppet.html`

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/test/puppet/images_chatgpt.md

종이인형극처럼 **배경 1장 + 따로 오린 인형 8장**을 만든다. 영상 코드가 인형을 움직이고, 상태가 바뀌면(메기 → 들어 올리기 → 떨어짐) 그 상태의 그림으로 갈아 끼운다.

| 번호 | 파일 | 크기 | 무엇 | 만드는 법 |
|---|---|---|---|---|
| 1 | `test/puppet/P-BG.jpg` | 가로 1536×1024 | 빈 무대 배경 — 해질녘 강변 | 새로 |
| 2 | `test/puppet/P-CROWD.png` | 가로 1536×1024 · 투명 | 구경꾼 한 줄 (뒷모습) — 환호 | 새로 |
| 3 | `test/puppet/P-CROWD2.png` | 가로 1536×1024 · 투명 | 같은 구경꾼 — 놀라 뒤로 물러섬 | **2번을 고쳐서** |
| 4 | `test/puppet/P-CARRY.png` | 가로 1536×1024 · 투명 | 태고대(가마) + 어깨에 멘 가마꾼들 | 새로 |
| 5 | `test/puppet/P-LIFT.png` | 가로 1536×1024 · 투명 | 같은 가마 — 머리 위로 높이 들어 올림 | **4번을 고쳐서** |
| 6 | `test/puppet/P-FLOAT.png` | 가로 1536×1024 · 투명 | 5번의 가마만 (사람 없음) | **5번을 고쳐서** |
| 7 | `test/puppet/P-SCATTER.png` | 가로 1536×1024 · 투명 | 5번의 가마꾼만 — 흩어짐 (가마 없음) | **5번을 고쳐서** |
| 8 | `test/puppet/P-DUST.png` | 가로 1536×1024 · 투명 | 흙먼지 덩어리 | 새로 |
| 9 | `test/puppet/P-FLOWER.png` | 정사각 1024×1024 · 투명 | 흰 국화 한 송이 | 새로 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 9장을 1번부터 차례로 만든다. 질문하지 말고 바로 만든다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다. 모든 프롬프트 맨 앞에 아래 **공통 화풍** 문단을 그대로 붙인다 (9장이 한 무대의 인형처럼 같은 화풍이어야 한다).
3. **'고쳐서' 만드는 그림(3·5·6·7번)은 표에 적힌 앞 그림을 편집해서 만든다** — 새로 그리지 않는다. 캔버스 크기·인물 수·옷·색·크기·발 위치가 앞 그림과 같아야 한다 (영상에서 두 그림을 같은 자리에 겹쳐 갈아 끼운다). 바뀌는 것은 프롬프트에 적힌 자세·있고 없음뿐이다.
4. **투명 배경**: 2~9번은 PNG 투명 배경(알파)으로 만든다 — 인형만 있고 땅·그림자·풍경·액자 없음. 다 만들면 파이썬으로 네 귀퉁이 픽셀의 알파가 0인지 확인한다. 투명이 안 되면 **배경을 순초록 #00FF00 한 색 평면**으로 다시 만든다 (인형에는 초록을 쓰지 않음 — Claude 가 코드로 초록을 뺀다).
5. 그림에 글자·숫자·로고·워터마크를 넣지 않는다. 사람은 얼굴 이목구비가 없는 종이 인형으로 그리고, 피·다친 사람·깔린 사람은 그리지 않는다.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`4. test/puppet/P-CARRY.png`). 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (`test/puppet/` 폴더, 대소문자까지 같게).
   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다. 올린 뒤 GitHub 에 있는 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     - 1번(JPEG): RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.
     - 2~9번(PNG, 투명 유지): 아래 코드 그대로.
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
   - **GitHub 앱으로 커밋한다.** 커밋 메시지: `[test] puppet <파일 이름> 이미지` (예: `[test] puppet P-CARRY.png 이미지`). 올린 뒤 파일 경로와 커밋 링크를 적는다.
   - **올리기가 실패하면** (권한·연결 오류) 묻지 말고 그림을 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"이 그림을 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 저장 경로에 올립니다."** 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 표의 파일 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/test/puppet 에 끌어다 놓고 Commit changes"
8. 이미지 한도로 멈추면 사용자가 "계속"이라고 보낸다 — 그때 다음 번호부터 이어서 만든다.

## 공통 화풍 (모든 프롬프트 맨 앞에 그대로 붙임)

```
STYLE: Japanese paper-cut puppet theater (kiri-e papercraft). Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited warm dusk palette: deep indigo #1E2A4A, crimson #B3202A, gold ochre #D9A441, warm cream #F2E6CF, charcoal #2B2B2B, lantern orange #F08A2E. Flat side view, like a stage seen from the audience. People are simple paper puppets with round plain heads and NO facial features (no eyes, nose or mouth), not recognizable as any real person. No text, letters, numbers, logos or watermarks anywhere.
```

투명 인형(2~9번)에는 공통 화풍 다음에 이 문단도 그대로 붙인다:

```
CUTOUT: one isolated paper puppet cutout on a fully transparent background (PNG with alpha channel). Only the described object — no ground, no cast shadow on the ground, no scenery, no frame. A thin cream (#F2E6CF) paper border about 6 px wide runs around the whole outer silhouette, like a hand-cut puppet. Nothing touches the canvas edges: keep at least 3% empty margin on every side. If a transparent background is impossible, make the whole background one flat pure chroma green #00FF00 with no shading, and use no green at all on the object.
```

## 1. P-BG — 빈 무대 배경

**저장 경로: `test/puppet/P-BG.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (영상은 가운데 16:9 를 쓰므로 위아래 8% 는 잘려도 되게)

```
Landscape 1536x1024. An empty paper-theater stage backdrop: a wide, shallow riverbed in a small Japanese town in Ehime at dusk in autumn. Layered paper hills in the far distance, a deep indigo sky fading to warm orange near the horizon with a low paper sun, a small vermilion torii gate and a shrine roof on the far left bank, rows of glowing round paper lanterns strung on tall poles along the far riverbank, a few autumn trees. The bottom 32% of the image is a flat, open gravel riverbed floor made of beige and grey paper pieces. Completely empty: no people, no floats, no animals. Keep the center and lower middle open and calm (puppets will stand there); put the strongest details on the left and right thirds and in the sky. Keep everything important between 8% and 92% of the height.
```

## 2. P-CROWD — 구경꾼 한 줄 (환호)

**저장 경로: `test/puppet/P-CROWD.png`** — PNG 투명 700KB 이하 · 가로 1536×1024

```
Landscape 1536x1024. A long row of about 24 festival spectators seen from BEHIND (we see their backs and the backs of their heads), standing shoulder to shoulder, cheering: many raise one or both arms, a few hold round paper fans or small paper lanterns, two small children on adults' shoulders. Simple paper puppet figures in dark indigo, charcoal, grey and muted crimson clothes, some in light summer kimono. The row spans from 3% to 97% of the width, all feet on one straight line at 92% of the height, the tallest raised hand at about 50% of the height.
```

## 3. P-CROWD2 — 같은 구경꾼, 놀라 물러섬 (2번을 고쳐서)

**저장 경로: `test/puppet/P-CROWD2.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · **2번 그림을 편집**

```
Edit the previous image (P-CROWD): keep exactly the same spectators, same number, same clothes, same colors, same scale, same canvas, same feet line at 92% and the same horizontal positions. Change ONLY their poses: they are shocked and recoiling — leaning backward, hands on their heads, some covering their mouths with both hands, some pulling a child close, fans and lanterns lowered. Still seen from behind. Same transparent background.
```

## 4. P-CARRY — 태고대(가마) + 어깨에 멘 가마꾼들

**저장 경로: `test/puppet/P-CARRY.png`** — PNG 투명 700KB 이하 · 가로 1536×1024

```
Landscape 1536x1024, side view. A huge Japanese festival float (taikodai): a tall boxy wooden float about twice the height of a man, a crimson body with large gold embroidered panels showing a dragon and waves as flat paper shapes, a roof made of five thick stacked crimson cushion layers with gold edges, gold ornaments and long gold tassels at the corners, small paper lanterns hanging at the four corners. It rests on two long, thick, horizontal wooden carrying poles that stick out far to both sides. About 12 carriers in white happi coats with an indigo wave pattern and white headbands stand in one row under the poles, the poles resting on their shoulders, walking in step, one hand up holding the pole. The whole group spans from 6% to 94% of the width. All carriers' feet stand on one straight line at 90% of the height. The top of the float reaches about 30% of the height, so there is empty space above it.
```

## 5. P-LIFT — 같은 가마, 머리 위로 높이 들어 올림 (4번을 고쳐서)

**저장 경로: `test/puppet/P-LIFT.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · **4번 그림을 편집**

```
Edit the previous image (P-CARRY): keep exactly the same float, the same 12 carriers, the same clothes and colors, the same scale, the same canvas, the same feet line at 90% of the height and the same horizontal positions. Change ONLY the pose: every carrier now pushes the poles high above his head with both arms fully stretched straight up, so the poles and the whole float are raised about one head-height higher than before (the top of the float now at about 14% of the height). Carriers lean slightly forward, straining, energetic. Same transparent background.
```

## 6. P-FLOAT — 5번의 가마만, 사람 없음 (5번을 고쳐서)

**저장 경로: `test/puppet/P-FLOAT.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · **5번 그림을 편집**

```
Edit the previous image (P-LIFT): remove ALL the people completely, including their arms and hands. Keep ONLY the float with its two long carrying poles, with exactly the same size, shape, colors and position on the canvas as in the previous image (still in the raised position, nothing moved). Where the people were is now transparent background. Same cream cutout border around the float.
```

## 7. P-SCATTER — 5번의 가마꾼만, 흩어짐 (5번을 고쳐서)

**저장 경로: `test/puppet/P-SCATTER.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · **5번 그림(P-LIFT)을 편집 — 6번이 아님**

```
Edit the P-LIFT image (the one with the raised float and the carriers): remove the float and both carrying poles completely. Keep the same 12 carriers with the same clothes, colors and scale, feet near the same line at 90% of the height. Change their poses: the float is falling onto the middle, so they scatter away from the center — the carriers on the left half dive or stumble to the left, the carriers on the right half fall back or crouch to the right with their arms up shielding their heads. The middle of the canvas (from about 38% to 66% of the width) is now empty. Dynamic and urgent, but no injuries, no blood, nobody lying under anything. Same transparent background.
```

## 8. P-DUST — 흙먼지 덩어리

**저장 경로: `test/puppet/P-DUST.png`** — PNG 투명 700KB 이하 · 가로 1536×1024

```
Landscape 1536x1024. A big burst of dust and gravel made of flat layered paper shapes: a wide, low cloud of rounded beige, sand and warm grey paper puffs spreading sideways from the center, with small paper pebbles and splinters flying outward. Much wider than tall: it spans from 5% to 95% of the width and from 40% to 92% of the height, flat along the bottom. Slightly lighter and semi-solid looking at the top edges. Nothing else.
```

## 9. P-FLOWER — 흰 국화 한 송이

**저장 경로: `test/puppet/P-FLOWER.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. A single white chrysanthemum, the Japanese flower of mourning, made of many layered white and warm cream paper petals with a pale gold center, on a short dark green (#2F5D3A) stem with two leaves, lying diagonally from lower left to upper right. Centered, filling about 70% of the canvas. Quiet and respectful.
```
