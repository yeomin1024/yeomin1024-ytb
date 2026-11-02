# 주식 롱폼 1편 「빨리 벌고 싶은 사람은 절대 통과 못하는 주식 테스트」 — 대본 v11 에 더할 소품 4장 (ChatGPT용)

작성: 2026-11-02 (Claude, v11 추가분 — 23~26번 4장만) — 사용자 지시 2026-11-02 "이미지 만들 것도 알려주고"

**왜:** 그림 1~22번(`images_chatgpt.md` v2.0)은 대본 v8 기준으로 이미 만들어 main 에 있다. 대본이 v11(S&P 500 · 업스타트 · 관세 하락장 · C3.ai · 아이온큐)로 바뀌며 **새 물건 4개**가 생겼다 → 이 4장만 만든다. 1~22번은 다시 만들지 않는다. v8 의 19번 P-COINS(비트코인)는 v11 에서 쓰지 않는다 (지우지 않음).
화풍·크기·투명·올리는 법은 1~22번과 똑같다 (같은 무대의 소품처럼).

| 번호 | 파일 | 크기 | 무엇 | 쓰는 곳 (대본 v11 문장) |
|---|---|---|---|---|
| 23 | `stock/source/ppalli-test-2026-11/puppet/P-LOAN.png` | 정사각 1024 · 투명 | 대출 서류 더미 | 선택 1 'AI로 대출을 심사하는 회사' · '이 회사 대출을 대량으로 사기로 한 날' (10~11) · 해설 1 '그 종목은 업스타트' (45) — 코드가 UPST·×5·+35% 를 얹음 |
| 24 | `stock/source/ppalli-test-2026-11/puppet/P-CONTAINERS.png` | 정사각 1024 · 투명 | 수출입 컨테이너와 내려진 차단기 | 선택 3 '관세 걱정에 S&P 500 지수가 … 하락' (23) · 해설 3 (62) — 코드가 −10% 를 얹음 |
| 25 | `stock/source/ppalli-test-2026-11/puppet/P-CRACK.png` | 정사각 1024 · 투명 | 금이 간 기둥 (회사의 기본 체력 = 펀더멘탈) | 선택 4 '회사의 기본 체력, 즉 펀더멘탈에 문제가 생긴 겁니다' (31) · 해설 4 '주가를 받쳐 주던 실적이 무너졌다면' (82) — 어려운 말 = 그림 하나 |
| 26 | `stock/source/ppalli-test-2026-11/puppet/P-QUANTUM.png` | 정사각 1024 · 투명 | 양자 컴퓨터 (금빛 샹들리에 모양) | 선택 5 '양자 컴퓨터 종목들이 연일 사상 최고가' (36~37) · 해설 5 '양자 컴퓨터를 만드는 아이온큐' (88) — 코드가 IONQ·×7 을 얹음 (v8 의 P-COINS 대신) |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 23~26번 **4장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. **한 장에 프롬프트에 적힌 것만** 그린다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 아래 **공통 화풍** 문단, 그다음 **CUTOUT** 문단을 그대로 붙인다.
3. **잘림 검사 (올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`이면 그림을 더 작게(여백을 더 넓게) 다시 만들고 다시 검사한다. 투명이 아니면(귀퉁이 알파가 0 이 아님) 배경을 **순초록 #00FF00 한 색 평면**으로 다시 만든다.
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
4. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 서류·컨테이너·기계에도 없음 (빈 칸이나 회색 줄로). 실제 회사의 기계·로고를 닮게 그리지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.
5. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`23. stock/source/ppalli-test-2026-11/puppet/P-LOAN.png`). 그림 안에는 쓰지 않는다.
6. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게) — `stock/source/ppalli-test-2026-11/puppet/` 폴더.
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
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[stock] ppalli 1편 <파일 이름> 이미지` (예: `[stock] ppalli 1편 P-LOAN.png 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 묻지 말고 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."** 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 표의 파일 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/ppalli-test-2026-11/puppet 에 끌어다 놓고 Commit changes"

## 공통 화풍 (23~26번 프롬프트 맨 앞에 그대로 붙임)

```
STYLE: Japanese paper-cut puppet theater (kiri-e papercraft). Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited warm dusk palette: deep indigo #1E2A4A, crimson #B3202A, gold ochre #D9A441, warm cream #F2E6CF, charcoal #2B2B2B, lantern orange #F08A2E, with grey-blue #5B6B8C for modern offices, trains and screens. Flat side view, like a stage seen from the audience. People are simple paper puppets with adult proportions and simple small facial features (small dot eyes, short brows, a simple mouth line), not recognizable as any real person. No text, letters, numbers, logos or watermarks anywhere — screens, papers, banknotes, coins and signs are blank or carry only plain lines.
```

## CUTOUT (23~26번 — 공통 화풍 다음에 그대로 붙임)

```
CUTOUT: the described subject only, as an isolated paper puppet cutout on a fully transparent background (PNG with alpha channel) — no ground, no cast shadow on the ground, no scenery, no frame, no other objects or people. A thin cream (#F2E6CF) paper border about 6 px wide runs around the outer silhouette, like a hand-cut puppet. The WHOLE subject must be fully visible with generous empty margin: nothing may touch or cross the canvas edges — keep at least 8% empty transparent space on every side (left, right, top and bottom). If a transparent background is impossible, make the whole background one flat pure chroma green #00FF00 with no shading, and use no green at all on the subject.
```

## 23. P-LOAN — 대출 서류 더미

**저장 경로: `stock/source/ppalli-test-2026-11/puppet/P-LOAN.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, front view. ONE neat tall stack of blank loan application papers tied with a crimson ribbon, with one small round teal badge resting on top that shows only simple circuit lines (to suggest computer screening). Papers are blank or carry only plain grey lines; no stamps, no letters, no numbers, no logos. Centered, fills about 70% of the canvas height, with at least 8% empty margin on every side.
```

## 24. P-CONTAINERS — 수출입 컨테이너와 내려진 차단기

**저장 경로: `stock/source/ppalli-test-2026-11/puppet/P-CONTAINERS.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, side view. ONE small pile of three stacked shipping containers (deep indigo, crimson, gold ochre) with corrugated paper texture, and a red-and-cream striped barrier gate arm lowered in front of them — a worry about trade tariffs. No letters, no numbers, no logos on the containers or the gate. Centered, fills about 75% of the canvas width, with at least 8% empty margin on every side.
```

## 25. P-CRACK — 금이 간 기둥 (회사의 기본 체력 = 펀더멘탈)

**저장 경로: `stock/source/ppalli-test-2026-11/puppet/P-CRACK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, front view. ONE cream paper stone pillar on a short base, holding up a small flat roof slab, with one large jagged crack running down the middle of the pillar and a few small paper chips falling from it — a company's foundation breaking. No letters, no numbers. Centered, fills about 80% of the canvas height, with at least 8% empty margin on every side.
```

## 26. P-QUANTUM — 양자 컴퓨터 (금빛 샹들리에 모양)

**저장 경로: `stock/source/ppalli-test-2026-11/puppet/P-QUANTUM.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024, front view. ONE quantum computer in the familiar 'golden chandelier' form: a hanging column of four stacked gold-ochre discs that get smaller toward the bottom, linked by many thin coiled copper-gold tubes, with a faint cool grey-blue glow around it — generic, not resembling any specific company's machine. No letters, no numbers, no logos. Centered, fills about 80% of the canvas height, with at least 8% empty margin on every side.
```
