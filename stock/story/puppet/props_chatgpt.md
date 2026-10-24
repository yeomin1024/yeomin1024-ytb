# 주식 영상 공통 설명 소품 — 종이 소품 그림 (ChatGPT 에 넘기는 파일)

이 파일 판: v2.0 — 2026-10-24 — **공통 소품으로 다시 씀** (사용자 지시 2026-10-24 "소품 요소를 좀 되도록 다른 주식 관련 영상에서 재사용할 수 있도록 공통된 걸 만들도록 해봐 물론 재사용 불가능해도 꼭 필요하면 만들어도 되고"): 그림은 특정 화·종목·장면이 아니라 **일반적인 뜻**(몰빵·분산·손실 확정·거품…)으로 — 1화만의 묘사(바구니 속 반도체 칩·신문 속 칩 그림·체크칸 5개·풍선에 묶인 지폐·차단기 옆 초시계)는 뺌. 1·2번은 이미 올라와 검수 통과 → 3번부터 만든다. (v1.0 — 2026-10-23 — 1화 설명 소품 21장, 사용자 지시 "설명에 필요한 이미지 요소들은 왜 생성안해?")

쓰임: 영상 화면에는 글자가 없다(외국인 시청자 — 말은 언어별 자막). 어려운 말·비유를 **그림 한 장**으로 보여 주는 무대 위 종이 소품이다. 숫자는 코드가 그림 위에 따로 띄운다. 주인공 인형과 같은 그림체라 '개미 재기 일지' 모든 화에서 다시 쓰고, 투명 PNG 라 다른 주식 영상 장면(HTML)에서도 `<img>` 로 쓸 수 있다.

**Claude 에게 (소품 고르는 법)**: 새 화 장면 표를 쓸 때 `python3 tools/story_kit.py props [낱말]` 로 이 목록을 먼저 본다 → 뜻이 맞는 소품을 다시 쓴다 → 없을 때만 새 소품을 표 끝에 더한다. 새 소품도 **일반적인 뜻**으로 그린다 (특정 회사·나라·화 숫자·장면 묘사 금지). 그 화에만 꼭 필요한 그림이면 '쓴 화'에 `전용`을 붙인다. 아래 '후보'는 2~4화 대본에서 뽑은 다음 소품 — 그 화 장면 표에 쓸 때 표로 옮겨 만든다.

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 소품 파일(v1.0)이 있어도 쓰지 않는다. 답의 첫 줄에 위 '이 파일 판' 줄을 그대로 적는다.
1. 아래 표에서 **상태가 '만들 것'인 장만** 번호 차례로 모두 만든다 ('있음'은 건너뛴다). 질문하지 말고 바로 만든다. **한 장에 프롬프트에 적힌 것만** 그린다 (사람·인형을 같이 그리지 않는다).
   - 이미지 한도로 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 아래 **STYLE**·**CUTOUT**·**PROP** 세 문단을 그대로 붙인다.
3. **글자·숫자·기호(₩ $ % 등)·로고·국기를 그림에 넣지 않는다.** 휴대폰 화면·신문·종이·간판은 빈 면이다.
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
5. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (예: `3. stock/story/puppet/props/NOTEBOOK.png`). 그림 안에는 쓰지 않는다.
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
   - **GitHub 앱으로 커밋한다.** 커밋 메시지: `[주인공] puppet props <파일 이름> 소품` (예: `[주인공] puppet props NOTEBOOK.png 소품`). 올린 뒤 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패하면** (권한·연결 오류) 묻지 말고: 그림을 한 번 더 보여 주고, 이 문장을 그대로 쓴다 — **"이 그림을 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 저장 경로에 올립니다."** 직접 올리는 길: 그림을 표의 파일 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/story/puppet/props 에 끌어다 놓고 Commit changes.

## 공통 문단 (프롬프트 맨 앞에 그대로 붙임 — 모든 장)

```
STYLE: paper-cut puppet theater (layered papercraft), like a hand-made paper puppet show. Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited calm palette: deep indigo #1E2A4A, warm cream #F2E6CF, charcoal #2B2B2B, gold ochre #D9A441, muted crimson #B3202A, soft teal #3E8E87, plus the character colors below. Flat stage view, like a stage seen from the audience. People are paper puppets WITH clearly readable facial expressions: every face is built from small cut-paper pieces — almond-shaped dark eyes with a tiny white highlight, thin dark-brown paper eyebrows, a simple mouth cut from darker paper, and soft pink paper cheek circles. The expression must read at a glance even when the picture is small. Fictional people, not recognizable as any real person. Modern everyday Korean life today. No text, letters, numbers, logos or watermarks anywhere.
```

```
CUTOUT: the described subject only, as an isolated paper puppet cutout on a fully transparent background (PNG with alpha channel) — no ground, no cast shadow on the ground, no scenery, no frame, no other objects or people. A thin cream (#F2E6CF) paper border about 6 px wide runs around the outer silhouette, like a hand-cut puppet. The WHOLE subject must be fully visible with generous empty margin: nothing may touch or cross the canvas edges — keep at least 8% empty transparent space on every side (left, right, top and bottom). If a transparent background is impossible, make the whole background one flat pure chroma green #00FF00 with no shading, and use no green at all on the subject.
```

```
PROP: ONE single stage prop for the same paper puppet show (an object, not a person), as simple and bold as a puppet-theater prop so it reads at a glance when small on a stage. It must be a GENERAL symbol that can be reused in many different stock-market stories — no specific company, product, country or scene details. Seen from the front or a slight three-quarter view, standing on an invisible floor (its bottom edge flat). NO text, letters, numbers, digits, currency symbols, percent signs, logos, brand marks or flags anywhere — every screen, page, sign and label is completely blank.
```

## 공통 소품 21장 (만들 것 19장)

| 번호 | 저장 경로 | 뜻 (어느 영상에나) | 이야기 예 | 쓴 화 | 상태 |
|---|---|---|---|---|---|
| 1 | `stock/story/puppet/props/PHONE-ALERT.png` | 경고 · 강제 매도(반대매매) · 계좌 위험 알림 | 빚낸 돈이 강제로 빠져나감 | 1화 | 있음 |
| 2 | `stock/story/puppet/props/PIGGY.png` | 줄어든 저축 · 노후 자금 · 비상금이 모자람 | 노후 자금이 조금만 남음 | 1화 | 있음 |
| 3 | `stock/story/puppet/props/NOTEBOOK.png` | 원칙 · 매매 일지 · 규칙 적기 | 지킬 것을 노트에 적음 | 1화 | 만들 것 |
| 4 | `stock/story/puppet/props/ONE-BASKET.png` | 몰빵 · 한 종목·한 업종에 집중 | 반도체에만 넣음 | 1화 | 만들 것 |
| 5 | `stock/story/puppet/props/BARRIER.png` | 거래 정지 · 멈춤 · 매매 중단 | 거래가 20분 멈춤 | 1화 | 만들 것 |
| 6 | `stock/story/puppet/props/BOX.png` | 박스권 · 오래 제자리인 지수 | 박스피 | 1화 | 만들 것 |
| 7 | `stock/story/puppet/props/BIG-BASKET.png` | 지수 · 분산 투자 (여러 회사를 나눠 담음) | 500개 회사를 담은 지수 | 1화 | 만들 것 |
| 8 | `stock/story/puppet/props/TRASH.png` | 앱 삭제 · 시장을 떠남 · 포기 | 주식 앱을 지울 생각 | 1화 | 만들 것 |
| 9 | `stock/story/puppet/props/STAMP.png` | 손실 확정 · 되돌릴 수 없는 결정 | 떠나는 순간 손실이 확정 | 1화 | 만들 것 |
| 10 | `stock/story/puppet/props/RUIN.png` | 한 회사가 무너짐 · 회복 못 하는 종목 · 상장 폐지 | 한 종목은 끝내 회복 못 할 수도 | 1화 | 만들 것 |
| 11 | `stock/story/puppet/props/WAVE.png` | 시장 전체를 움직이는 큰 흐름 (금리·경기) | 거시 경제 | 1화 | 만들 것 |
| 12 | `stock/story/puppet/props/NEWS.png` | 뉴스 · 호재 기사 · 정보만 쫓음 | 호재 기사만 골라 읽음 | 1화 | 만들 것 |
| 13 | `stock/story/puppet/props/STORM.png` | 악재가 한꺼번에 · 위기 · 폭락장 | 여러 우려가 한꺼번에 덮침 | 1화 | 만들 것 |
| 14 | `stock/story/puppet/props/BANK.png` | 금리 · 예금 · 돈이 은행으로 감 | 금리가 오르면 돈이 예금으로 | 1화 | 만들 것 |
| 15 | `stock/story/puppet/props/BALLOON.png` | 거품 · 과열 · 빚으로 부푼 시장 | 시장 전체가 빚으로 달림 | 1화 | 만들 것 |
| 16 | `stock/story/puppet/props/GAUGE.png` | 위험 점검 · 과열 · 무리하는지 | 경제 지표로 내가 무리하는지 점검 | 1화 | 만들 것 |
| 17 | `stock/story/puppet/props/CHAT.png` | 남의 말 · 리딩방 · 단톡방 · 수익 인증 | 들은 종목을 따라 매수 | 1화 | 만들 것 |
| 18 | `stock/story/puppet/props/ANCHOR.png` | 원칙 · 흔들리지 않음 | 원칙이 있으면 덜 흔들림 | 1화 | 만들 것 |
| 19 | `stock/story/puppet/props/TORTOISE.png` | 천천히 · 꾸준히 · 장기 투자 | 리스크를 줄이며 천천히 | 1화 | 만들 것 |
| 20 | `stock/story/puppet/props/TREE.png` | 복리 · 꾸준히 쌓여 자람 | 매달 넣은 돈이 1.6배 | 1화 | 만들 것 |
| 21 | `stock/story/puppet/props/ROCKET.png` | 빨리 가려다 실패 · 레버리지 · 한 방 | 3배 레버리지로 메우려다 | 1화 | 만들 것 |

## 3. NOTEBOOK — 원칙 · 매매 일지 · 규칙 적기

**저장 경로: `stock/story/puppet/props/NOTEBOOK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE open spiral notebook lying slightly tilted toward the viewer, its pages showing three short blank lines, each line starting with an empty square checkbox; nothing is written. A yellow pencil rests across the pages.
Centered, with at least 8% empty transparent margin on every side.
```

## 4. ONE-BASKET — 몰빵 · 한 종목·한 업종에 집중

**저장 경로: `stock/story/puppet/props/ONE-BASKET.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE small woven basket overloaded with a tall wobbly pile of identical white eggs, the pile leaning dangerously to one side, with one egg already falling off the top and a crack in another. Only eggs in the basket.
Centered, with at least 8% empty transparent margin on every side.
```

## 5. BARRIER — 거래 정지 · 멈춤 · 매매 중단

**저장 경로: `stock/story/puppet/props/BARRIER.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE lowered red-and-white striped barrier arm (like a railway-crossing gate) fixed to its post, blocking the way, with a round red stop light glowing on top of the post.
Centered, with at least 8% empty transparent margin on every side.
```

## 6. BOX — 박스권 · 오래 제자리인 지수

**저장 경로: `stock/story/puppet/props/BOX.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE open cardboard box seen from the front, with its flaps open. Inside the box a thick teal paper zigzag line (like a stock-chart line) bounces up and down, but every peak only bumps against the box rim — the line is trapped inside and cannot get out.
Centered, with at least 8% empty transparent margin on every side.
```

## 7. BIG-BASKET — 지수 · 분산 투자 (여러 회사를 나눠 담음)

**저장 경로: `stock/story/puppet/props/BIG-BASKET.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE large sturdy woven basket filled with many small, different paper buildings packed tightly together and all standing upright: factories with chimneys, office towers, small shops, a hospital, a warehouse, in many different colors — like a basket holding a whole small city.
Centered, with at least 8% empty transparent margin on every side.
```

## 8. TRASH — 앱 삭제 · 시장을 떠남 · 포기

**저장 경로: `stock/story/puppet/props/TRASH.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE open metal trash can, and a smartphone standing tilted beside it. A small plain gold rounded square (an app icon with nothing on it) is shown in mid-air falling from the phone toward the trash can.
Centered, with at least 8% empty transparent margin on every side.
```

## 9. STAMP — 손실 확정 · 되돌릴 수 없는 결정

**저장 경로: `stock/story/puppet/props/STAMP.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE big wooden rubber stamp with a round handle, pressing down onto a sheet of cream paper (part of the prop); on the paper, next to the stamp, there is one large stamped mark: a plain solid red circle ring with nothing inside it.
Centered, with at least 8% empty transparent margin on every side.
```

## 10. RUIN — 한 회사가 무너짐 · 회복 못 하는 종목 · 상장 폐지

**저장 경로: `stock/story/puppet/props/RUIN.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE single small office building standing alone, cracked from the roof down the middle, its top floors crumbling with small paper pieces falling off. Faded grey and dull ochre colors.
Centered, with at least 8% empty transparent margin on every side.
```

## 11. WAVE — 시장 전체를 움직이는 큰 흐름 (금리·경기)

**저장 경로: `stock/story/puppet/props/WAVE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE huge curling ocean wave in deep indigo and soft teal paper layers, lifting many small paper boats of different colors up all at once.
Centered, with at least 8% empty transparent margin on every side.
```

## 12. NEWS — 뉴스 · 호재 기사 · 정보만 쫓음

**저장 경로: `stock/story/puppet/props/NEWS.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE folded newspaper whose columns are only blank grey bars and one blank picture box (no letters, no picture content), with a magnifying glass held close over the front page.
Centered, with at least 8% empty transparent margin on every side.
```

## 13. STORM — 악재가 한꺼번에 · 위기 · 폭락장

**저장 경로: `stock/story/puppet/props/STORM.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE big dark storm cloud with three white lightning bolts and slanted rain, hanging over a tiny cluster of small paper buildings below it.
Centered, with at least 8% empty transparent margin on every side.
```

## 14. BANK — 금리 · 예금 · 돈이 은행으로 감

**저장 경로: `stock/story/puppet/props/BANK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE classical bank building with four columns and a triangular roof (no sign, no writing), and a curving stream of plain gold coins flowing from the left into its open front door.
Centered, with at least 8% empty transparent margin on every side.
```

## 15. BALLOON — 거품 · 과열 · 빚으로 부푼 시장

**저장 경로: `stock/story/puppet/props/BALLOON.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE huge over-inflated red balloon, stretched thin and shiny, on a short hanging string, with one sharp silver pin floating close to the balloon — a bubble about to pop.
Centered, with at least 8% empty transparent margin on every side.
```

## 16. GAUGE — 위험 점검 · 과열 · 무리하는지

**저장 경로: `stock/story/puppet/props/GAUGE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE large round dashboard gauge like a car speedometer, with a green, a yellow and a red arc and one needle pointing into the red part. No numbers, no tick labels, no letters.
Centered, with at least 8% empty transparent margin on every side.
```

## 17. CHAT — 남의 말 · 리딩방 · 단톡방 · 수익 인증

**저장 경로: `stock/story/puppet/props/CHAT.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE smartphone standing upright with many overlapping blank speech bubbles bursting out of its screen; some bubbles contain a small plain gold coin or a small green upward arrow, none contain any letters.
Centered, with at least 8% empty transparent margin on every side.
```

## 18. ANCHOR — 원칙 · 흔들리지 않음

**저장 경로: `stock/story/puppet/props/ANCHOR.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE heavy dark iron ship anchor with a short thick rope, resting firmly upright, with a few small wavy paper lines around it suggesting moving water while the anchor stays still.
Centered, with at least 8% empty transparent margin on every side.
```

## 19. TORTOISE — 천천히 · 꾸준히 · 장기 투자

**저장 경로: `stock/story/puppet/props/TORTOISE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE calm tortoise walking steadily to the right, carrying a small neat stack of plain gold coins on its shell. Simple friendly animal, no clothes.
Centered, with at least 8% empty transparent margin on every side.
```

## 20. TREE — 복리 · 꾸준히 쌓여 자람

**저장 경로: `stock/story/puppet/props/TREE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE young tree growing from a terracotta pot; its leaves are plain round gold coins.
Centered, with at least 8% empty transparent margin on every side.
```

## 21. ROCKET — 빨리 가려다 실패 · 레버리지 · 한 방

**저장 경로: `stock/story/puppet/props/ROCKET.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE small toy rocket that has crashed nose-down into a small heap of brown paper earth (part of the prop), its body bent and broken, with a puff of grey smoke and a few torn paper pieces around it.
Centered, with at least 8% empty transparent margin on every side.
```

## 후보 — 아직 만들지 않음 (그 화 장면 표에 쓸 때 위 표로 옮겨 프롬프트를 쓴다)

- 후보 DICE — 도박 · 한 방 · 2화
- 후보 CHAIN — 빚 · 마이너스 통장 (쇠공 달린 사슬) · 2화
- 후보 HOLE — 메우려고 계속 넣는 돈 · 물타기 (밑 빠진 구멍에 떨어지는 동전) · 2화
- 후보 SCALE — 비중 맞추기 · 리밸런싱 (양팔 저울) · 3화
- 후보 HOURGLASS — 기다림 · 하루 기다리기 · 시간 · 3화
- 후보 BELL-OFF — 알림 끄기 (빗금 친 종) · 3화
- 후보 UMBRELLA — 비상금 · 여윳돈 (비 막는 우산) · 4화

## 변경 이력

| 판 | 날짜 | 바꾼 것 |
|---|---|---|
| v2.0 | 2026-10-24 | 공통 소품으로 다시 씀 — 뜻을 일반화(표에 '뜻·이야기 예·쓴 화·상태'), 1화만의 묘사 뺌(ONE-BASKET 칩 → 달걀 · NEWS 칩 그림 · NOTEBOOK 체크칸 5 → 3 · BALLOON 지폐 · BARRIER 초시계), 1·2번 '있음'(검수 통과), 2~4화 후보 7개 |
| v1.0 | 2026-10-23 | 처음 만듦 — 1화 설명 소품 21장 |
