# test 종이인형극 이미지 10장 (2판) — ChatGPT용 (일본 전통 축제 롱폼·쇼츠 나머지 장면 · 읽고 그대로 만들고 저장 경로에 올리기)

작성: 2026-10-20 (Claude, 2판) — 짝 문서 `test/일본축제_사망사고_제작안.txt` (v8.4) · 장면 `video/episodes/ilbon-chukje-2026-10/index.html`

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/test/puppet/images_chatgpt.md

1판 9장(P-BG·P-CROWD·P-CROWD2·P-CARRY·P-LIFT·P-FLOAT·P-SCATTER·P-DUST·P-FLOWER)은 이미 올라와 있다 — **다시 만들지 않는다.**
이번 2판은 **배경 4장 + 오린 인형 6장**이다. 인형은 한 가지 모습만 그린다 (움직임은 영상 코드가 만든다). 7~10번은 **한 장에 4개를 한 줄로** 그린다 (코드가 넷으로 잘라 씀).

| 번호 | 파일 | 크기 | 무엇 |
|---|---|---|---|
| 1 | `test/puppet/P-PAPER.jpg` | 가로 1536×1024 | 빈 남색 한지 바탕 (숫자·지도 장면 배경) |
| 2 | `test/puppet/P-TOWN.jpg` | 가로 1536×1024 | 빈 무대 — 축제 날 동네 골목 |
| 3 | `test/puppet/P-SHRINE.jpg` | 가로 1536×1024 | 빈 무대 — 숲속 신사 |
| 4 | `test/puppet/P-TEMPLE.jpg` | 가로 1536×1024 | 빈 무대 — 겨울밤 절 본당 앞마당 |
| 5 | `test/puppet/P-DANJIRI.png` | 가로 1536×1024 · 투명 | 단지리(나무 수레) + 지붕 위 한 사람 |
| 6 | `test/puppet/P-HADAKA.png` | 가로 1536×1024 · 투명 | 알몸 축제 남자들 무리 (훈도시) |
| 7 | `test/puppet/P-PEOPLE.png` | 가로 1536×1024 · 투명 | 한 줄에 4명: 어린이 · 청년 · 젊은 리더 · 원로 |
| 8 | `test/puppet/P-PEOPLE2.png` | 가로 1536×1024 · 투명 | 한 줄에 4개: 노장 참가자 · 고개 숙인 부부 · 정장 평론가 · 휴대폰 보는 사람 |
| 9 | `test/puppet/P-ICONS.png` | 가로 1536×1024 · 투명 | 한 줄에 4개: 료칸 · 포장마차 · 전철 · 시청 |
| 10 | `test/puppet/P-ICONS2.png` | 가로 1536×1024 · 투명 | 한 줄에 4개: 경주용 차 · AED 상자 · 방송 카메라 · 경찰차 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 10장을 1번부터 차례로 만든다. 질문하지 말고 바로 만든다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다. 모든 프롬프트 맨 앞에 아래 **공통 화풍** 문단을 그대로 붙인다 (1판 9장과 같은 화풍 — 한 무대의 인형처럼).
3. **투명 배경**: 5~10번은 PNG 투명 배경(알파)으로 만든다 — 인형만 있고 땅·그림자·풍경·액자 없음. 다 만들면 파이썬으로 네 귀퉁이 픽셀의 알파가 0인지 확인한다. 투명이 안 되면 **배경을 순초록 #00FF00 한 색 평면**으로 다시 만든다 (인형에는 초록을 쓰지 않음).
4. **7~10번은 4개를 한 줄로** — 왼쪽부터 프롬프트의 1)→4) 차례, 각각 가로 4등분한 칸의 가운데에(중심 12.5%·37.5%·62.5%·87.5%), **서로 닿거나 겹치지 않게** 사이에 투명한 빈 틈(가로 3% 이상)을 둔다. 바닥 줄은 모두 높이 88%.
5. 그림에 글자·숫자·로고·워터마크를 넣지 않는다. 사람은 얼굴 이목구비가 없는 종이 인형으로 그리고, 피·다친 사람은 그리지 않는다.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`5. test/puppet/P-DANJIRI.png`). 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (`test/puppet/` 폴더, 대소문자까지 같게).
   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다. 올린 뒤 GitHub 에 있는 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     - 1~4번(JPEG): RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.
     - 5~10번(PNG, 투명 유지): 아래 코드 그대로.
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
   - **GitHub 앱으로 커밋한다.** 커밋 메시지: `[test] puppet <파일 이름> 이미지` (예: `[test] puppet P-TOWN.jpg 이미지`). 올린 뒤 파일 경로와 커밋 링크를 적는다.
   - **올리기가 실패하면** (권한·연결 오류) 묻지 말고 그림을 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"이 그림을 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 저장 경로에 올립니다."** 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 표의 파일 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/test/puppet 에 끌어다 놓고 Commit changes"
8. 이미지 한도로 멈추면 사용자가 "계속"이라고 보낸다 — 그때 다음 번호부터 이어서 만든다.

## 공통 화풍 (모든 프롬프트 맨 앞에 그대로 붙임)

```
STYLE: Japanese paper-cut puppet theater (kiri-e papercraft). Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited warm dusk palette: deep indigo #1E2A4A, crimson #B3202A, gold ochre #D9A441, warm cream #F2E6CF, charcoal #2B2B2B, lantern orange #F08A2E. Flat side view, like a stage seen from the audience. People are simple paper puppets with round plain heads and NO facial features (no eyes, nose or mouth), not recognizable as any real person. No text, letters, numbers, logos or watermarks anywhere.
```

투명 인형(5~10번)에는 공통 화풍 다음에 이 문단도 그대로 붙인다:

```
CUTOUT: isolated paper puppet cutout(s) on a fully transparent background (PNG with alpha channel). Only the described object(s) — no ground, no cast shadow on the ground, no scenery, no frame. A thin cream (#F2E6CF) paper border about 6 px wide runs around each outer silhouette, like a hand-cut puppet. Nothing touches the canvas edges: keep at least 3% empty margin on every side. If a transparent background is impossible, make the whole background one flat pure chroma green #00FF00 with no shading, and use no green at all on the objects.
```

4개를 한 줄로 그리는 7~10번에는 이 문단도 그대로 붙인다:

```
ROW OF FOUR: draw exactly four separate cutouts in one horizontal row, in the order 1) to 4) from left to right. Each one is centered in its own quarter of the width (centers at 12.5%, 37.5%, 62.5% and 87.5% of the width), about the same height (about 55% of the canvas height), all standing on one bottom line at 88% of the height. They must NOT touch or overlap: leave a clear transparent gap of at least 3% of the width between neighbors.
```

## 1. P-PAPER — 빈 남색 한지 바탕

**저장 경로: `test/puppet/P-PAPER.jpg`** — JPEG 700KB 이하 · 가로 1536×1024

```
Landscape 1536x1024. A plain backdrop of deep indigo (#1E2A4A) Japanese washi paper filling the whole canvas, with visible long paper fibers and a few faint lighter flecks, a very subtle darker vignette toward the edges. Nothing else at all: no objects, no shapes, no patterns, no text. Even and calm, so graphics can be placed on top.
```

## 2. P-TOWN — 빈 무대: 축제 날 동네 골목

**저장 경로: `test/puppet/P-TOWN.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (위아래 8% 는 잘려도 되게)

```
Landscape 1536x1024. An empty paper-theater stage backdrop: an old narrow street in a small Japanese town on a festival day in the early evening. Two-story wooden houses with dark tiled roofs on both sides, round paper lanterns and plain red-and-white festival bunting strung across the street, a big wooden storehouse on the right with its large doors open showing an empty, dimly lit interior (where the festival float is kept), a small torii gate far away at the end of the street, a warm orange sky. The bottom 30% is the empty street surface of packed earth and stones. No people, no floats, no vehicles. Keep the center and lower middle open; put the details on the left and right thirds. Keep everything important between 8% and 92% of the height.
```

## 3. P-SHRINE — 빈 무대: 숲속 신사

**저장 경로: `test/puppet/P-SHRINE.jpg`** — JPEG 700KB 이하 · 가로 1536×1024

```
Landscape 1536x1024. An empty paper-theater stage backdrop: a Shinto shrine in a cedar forest at dusk. A large vermilion torii gate in the middle distance, a stone path leading to a wooden shrine hall hung with a thick twisted straw rope (shimenawa) and white zigzag paper streamers, tall cedar trees on both sides, a mountain behind, an old sacred tree on the left wrapped with a straw rope, small stone lanterns glowing warm. The bottom 30% is an open gravel courtyard. No people. Calm and sacred. Keep the center and lower middle open. Keep everything important between 8% and 92% of the height.
```

## 4. P-TEMPLE — 빈 무대: 겨울밤 절 본당 앞마당

**저장 경로: `test/puppet/P-TEMPLE.jpg`** — JPEG 700KB 이하 · 가로 1536×1024

```
Landscape 1536x1024. An empty paper-theater stage backdrop: the large wooden main hall of a Japanese Buddhist temple on a cold winter night. The hall has an upper-floor window/balcony at the front center, lit by warm floodlights; a dark blue night sky with a few stars; thin white steam drifting in the cold air; tall wooden pillars and a sweeping tiled roof. The bottom 35% is an open stone courtyard in front of the hall. No people. Keep the upper-center window clearly visible and the lower middle open. Keep everything important between 8% and 92% of the height.
```

## 5. P-DANJIRI — 단지리(나무 수레) + 지붕 위 한 사람

**저장 경로: `test/puppet/P-DANJIRI.png`** — PNG 투명 700KB 이하 · 가로 1536×1024

```
Landscape 1536x1024, side view facing left. A Kishiwada-style danjiri: a heavy, tall wooden festival cart made of unpainted natural wood with richly carved panels, a curved temple-style roof with flared eaves, small red-and-gold tassels, and big solid wooden wheels. Short thick ropes hang from the front and are coiled on the ground in front of the wheels (they do not stretch away). One man in a happi coat and headband stands balancing on the roof with a round fan in each raised hand (the roof dancer). No other people. The cart spans from about 20% to 80% of the width, wheels resting on a line at 90% of the height, the dancer's raised fans reaching about 10% of the height.
```

## 6. P-HADAKA — 알몸 축제 남자들 무리

**저장 경로: `test/puppet/P-HADAKA.png`** — PNG 투명 700KB 이하 · 가로 1536×1024

```
Landscape 1536x1024. A tightly packed crowd of about 20 men at a Japanese naked festival (Hadaka Matsuri), wearing only traditional white loincloths (fundoshi) and white tabi socks, seen mostly from behind and from the side, pushing together in one big mass, many arms raised high reaching upward for something above them, thin white steam rising from their bodies. Tasteful and respectful: nothing beyond the traditional loincloth is shown. Simple paper puppet figures with no facial features. The crowd spans from 4% to 96% of the width, feet on one line at 92% of the height, the highest hands at about 28% of the height.
```

## 7. P-PEOPLE — 한 줄에 4명: 어린이 · 청년 · 젊은 리더 · 원로

**저장 경로: `test/puppet/P-PEOPLE.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · **ROW OF FOUR**

```
Landscape 1536x1024, side view, all four facing right, standing. 1) a small child (about 8 years old) in a small happi coat, holding a thick festival rope with both hands; 2) a young man in his early 20s in a white happi coat and white headband, one fist raised with energy; 3) a man in his 30s, the young leader, in an indigo happi coat, holding a round paper fan up high and pointing forward; 4) an elderly man in his 70s, the respected elder of the neighborhood, in a dark kimono with a haori jacket, standing calmly with his hands behind his back. Natural relative heights (the child clearly smallest, the others adult height).
```

## 8. P-PEOPLE2 — 한 줄에 4개: 노장 참가자 · 고개 숙인 부부 · 정장 평론가 · 휴대폰 보는 사람

**저장 경로: `test/puppet/P-PEOPLE2.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · **ROW OF FOUR**

```
Landscape 1536x1024, side view, standing. 1) a festival veteran in his late 60s in an indigo happi coat and a twisted headband, arms crossed firmly, proud stance, facing right; 2) a middle-aged married couple, husband and wife side by side in plain dark clothes, both bowing deeply at the waist in apology, facing right (the two of them together are one cutout); 3) a commentator in a dark suit and glasses, facing right, one hand raised in an explaining gesture; 4) a young person in casual clothes, facing left, looking down at a glowing smartphone held in both hands.
```

## 9. P-ICONS — 한 줄에 4개: 료칸 · 포장마차 · 전철 · 시청

**저장 경로: `test/puppet/P-ICONS.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · **ROW OF FOUR**

```
Landscape 1536x1024, side view, four objects of about the same height. 1) a small traditional Japanese inn (ryokan): a two-story wooden building with a tiled roof, a short curtain (noren) at the entrance with no letters, and a warm glowing window; 2) a festival food stall (yatai) with a red-and-white striped awning, a steaming pot and skewers on the counter; 3) a short local train of two cars, cream and indigo, seen from the side; 4) a modern city hall building, plain white and grey, with a flag pole and a plain flag (no symbols, no letters).
```

## 10. P-ICONS2 — 한 줄에 4개: 경주용 차 · AED 상자 · 방송 카메라 · 경찰차

**저장 경로: `test/puppet/P-ICONS2.png`** — PNG 투명 700KB 이하 · 가로 1536×1024 · **ROW OF FOUR**

```
Landscape 1536x1024, side view, four objects of about the same height. 1) a red Formula-1 style racing car seen from the side, with no numbers, sponsors or letters; 2) an orange wall-mounted AED defibrillator box with only a simple white heart-and-lightning symbol, no letters; 3) a TV news camera on a tripod with a handheld microphone leaning against it; 4) a Japanese-style black-and-white police car seen from the side with a red light on the roof, no letters or emblems.
```
