# 주식 영상 설명 그림 — 코드로 표현하기 힘들 때만 (ChatGPT 에 넘기는 파일)

이 파일 판: v4.0 — 2026-10-24 — **그림은 꼭 필요할 때만** (사용자 지시 2026-10-24 "비유해서 설명하는 것도 아니고 황소,곰, 바구니 이런건 생성할 필요없어 더 직관적으로 의미 전달 되도록 3D, 모션 그래픽으로 표현할 수 있잖아 표현 힘든데 꼭 필요한 것만 이미지 요소로 하라고 다시 수정해"): 뜻은 코드 모션 그래픽(`video/render/story_mg.js` — 매매 앱 PHONE · 캔들+거래 정지 CANDLE · 시가총액 블록 TREEMAP · 박스권 BOXRANGE · 두 선 경주 RACE · 점 그리드 GRID · 돈의 흐름 FLOW · 악재 충돌 HIT · 계기판 GAUGE · 적립 DCA · 바닥 매도 SELLBOTTOM · 장 카드 RULE) 으로 보여 준다. 아래 26장은 모두 **보류** (만들지 않음 — 1화는 그림 0장). 새 그림은 코드로 표현하기 힘든데 꼭 필요한 것만 표에 '만들 것'으로 더한다 (비유 그림 금지 — 황소·곰·바구니 같은 것).

**ChatGPT 에게: 지금 이 파일에 '만들 것' 상태인 그림이 없으면 아무것도 만들지 말고 "만들 그림 없음"이라고만 답한다.**

(v3.0 — 2026-10-24 — 주식과 바로 이어지는 그림으로 새로 (사용자 지시 2026-10-24 "이미지 요소도 뭔가 주식하고 동떨어져 있어 … 다시해봐 이미지도 다시 생성하도록 chatgpt 알려주고"): 차트·캔들(빨강·초록 막대)·매매 앱·황소·곰·반도체 칩·주식 증서로 뜻을 보인다. 그림 속 글자는 BUY·SELL·%·$ 만 (투자자라면 다 아는 말). v2.0 의 21장(달걀 바구니·거북이·닻·파도 …)은 쓰지 않음 — `props/_old/`. (v2.0 — 2026-10-24 — 공통 소품으로 · v1.0 — 2026-10-23 — 1화 21장)

쓰임: 영상 화면에는 한국어가 없다(말은 언어별 자막) — 어려운 말·비유를 **주식 그림 한 장**으로 보여 주는 무대 위 종이 소품. 숫자·지수 이름(KOSPI·S&P 500)은 코드가 그림 위에 띄운다. 주인공 인형과 같은 그림체라 '개미 재기 일지' 모든 화에서 다시 쓰고, 투명 PNG 라 다른 주식 영상(HTML)에서도 `<img>` 로 쓴다.

**Claude 에게 (소품 고르는 법)**: 새 화 장면 표를 쓸 때 `python3 tools/story_kit.py props [낱말]` 로 이 목록을 먼저 본다 → 맞는 소품을 다시 쓴다 → 없을 때만 표 끝에 새로 (주식 그림으로, 일반적인 뜻으로 — 특정 회사·나라·화 숫자 금지, 꼭 그 화 전용이면 '전용'). 아래 '후보'는 2~4화 대본에서 뽑은 다음 소품.

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 소품 파일(v1.0·v2.0)이 있어도 쓰지 않는다. 답의 첫 줄에 위 '이 파일 판' 줄을 그대로 적는다.
1. 아래 표에서 **상태가 '만들 것'인 장만** 번호 차례로 모두 만든다. 질문하지 말고 바로 만든다. **한 장에 프롬프트에 적힌 것만** 그린다 (사람·인형을 같이 그리지 않는다 — 손이 적혀 있으면 종이 손 하나만).
   - 이미지 한도로 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 아래 **STYLE**·**CUTOUT**·**PROP** 세 문단을 그대로 붙인다.
3. **그림 속 글자는 프롬프트가 적은 BUY·SELL·%·$ 만**, 철자 그대로 굵은 대문자로. 그 밖의 글자·숫자·로고·국기는 넣지 않는다 (휴대폰 화면·신문·간판의 나머지는 빈 면).
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
5. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (예: `1. stock/story/puppet/props/MARGIN-CALL.png`). 그림 안에는 쓰지 않는다.
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
   - **GitHub 앱으로 커밋한다.** 커밋 메시지: `[주인공] puppet props <파일 이름> 소품` (예: `[주인공] puppet props MARGIN-CALL.png 소품`). 올린 뒤 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패하면** (권한·연결 오류) 묻지 말고: 그림을 한 번 더 보여 주고, 이 문장을 그대로 쓴다 — **"이 그림을 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 저장 경로에 올립니다."** 직접 올리는 길: 그림을 표의 파일 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/story/puppet/props 에 끌어다 놓고 Commit changes.

## 공통 문단 (프롬프트 맨 앞에 그대로 붙임 — 모든 장)

```
STYLE: paper-cut puppet theater (layered papercraft), like a hand-made paper puppet show. Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited calm palette: deep indigo #1E2A4A, warm cream #F2E6CF, charcoal #2B2B2B, gold ochre #D9A441, muted crimson #B3202A, soft teal #3E8E87, plus the character colors below. Flat stage view, like a stage seen from the audience. People are paper puppets WITH clearly readable facial expressions: every face is built from small cut-paper pieces — almond-shaped dark eyes with a tiny white highlight, thin dark-brown paper eyebrows, a simple mouth cut from darker paper, and soft pink paper cheek circles. The expression must read at a glance even when the picture is small. Fictional people, not recognizable as any real person. Modern everyday Korean life today. No text, letters, numbers, logos or watermarks anywhere except the exact words the prop description asks for.
```

```
CUTOUT: the described subject only, as an isolated paper puppet cutout on a fully transparent background (PNG with alpha channel) — no ground, no cast shadow on the ground, no scenery, no frame, no other objects or people. A thin cream (#F2E6CF) paper border about 6 px wide runs around the outer silhouette, like a hand-cut puppet. The WHOLE subject must be fully visible with generous empty margin: nothing may touch or cross the canvas edges — keep at least 8% empty transparent space on every side (left, right, top and bottom). If a transparent background is impossible, make the whole background one flat pure chroma green #00FF00 with no shading, and use no green at all on the subject.
```

```
PROP: ONE single stage prop for the same paper puppet show (an object or animal, not a person), as simple and bold as a puppet-theater prop so it reads at a glance when small on a stage. It must CLEARLY read as STOCK-MARKET investing — use stock-chart lines, candlesticks (red and green bars), trading-app screens, bull and bear, coins and banknotes as described — and it must be a GENERAL symbol reusable in many stock stories (no real company, brand, logo or country). Seen from the front or a slight three-quarter view, standing on an invisible floor (its bottom edge flat). NO text, letters, digits, logos or flags anywhere, EXCEPT the exact words BUY or SELL, and the symbols % or $, when the description asks for them — spelled exactly, in bold simple capital letters. Every other screen, page, sign and label is blank.
```

## 주식 소품 26장

| 번호 | 저장 경로 | 뜻 (어느 주식 영상에나) | (옛 계획) 1화 자리 | 쓴 화 | 상태 |
|---|---|---|---|---|---|
| 1 | `stock/story/puppet/props/MARGIN-CALL.png` | 반대매매 · 빚낸 돈이 강제로 매도됨 · 계좌 위험 경고 | 문장 2 · 쇼츠 3 | — | 보류 (코드로 대신) |
| 2 | `stock/story/puppet/props/SAVINGS-DROP.png` | 노후 자금·저축이 주식 손실로 줄어듦 | 문장 4 | — | 보류 (코드로 대신) |
| 3 | `stock/story/puppet/props/DELETE-APP.png` | 주식 앱 지우기 · 시장을 떠남 | 문장 5·31 · 쇼츠 6 | — | 보류 (코드로 대신) |
| 4 | `stock/story/puppet/props/RULE-NOTE.png` | 매매 원칙 · 투자 일지 | 문장 8·72 | — | 보류 (코드로 대신) |
| 5 | `stock/story/puppet/props/INDEX-BASKET.png` | 지수 · 분산 투자 (여러 회사를 나눠 담음) | 문장 9·23·27~28·44 | — | 보류 (코드로 대신) |
| 6 | `stock/story/puppet/props/CHIP-ALL-IN.png` | 한 업종·한 종목에 몰빵 (반도체) | 문장 13~15·50~51 | — | 보류 (코드로 대신) |
| 7 | `stock/story/puppet/props/CIRCUIT-BREAKER.png` | 거래 정지 (서킷브레이커) | 문장 16 | — | 보류 (코드로 대신) |
| 8 | `stock/story/puppet/props/BEAR.png` | 하락장 · 폭락 | 문장 18·26 | — | 보류 (코드로 대신) |
| 9 | `stock/story/puppet/props/BOX-RANGE.png` | 박스권 · 오래 제자리인 지수 | 문장 22 | — | 보류 (코드로 대신) |
| 10 | `stock/story/puppet/props/BULL.png` | 상승장 · 불장 | 문장 24 | — | 보류 (코드로 대신) |
| 11 | `stock/story/puppet/props/PAUSE-TRADING.png` | 매매를 잠시 멈춤 (계좌는 그대로 둠) | 문장 29·33 | — | 보류 (코드로 대신) |
| 12 | `stock/story/puppet/props/SELL-BOTTOM.png` | 바닥에서 매도 · 손실 확정 | 문장 32 · 쇼츠 7 | — | 보류 (코드로 대신) |
| 13 | `stock/story/puppet/props/DELISTED.png` | 한 종목이 무너짐 · 끝내 회복 못 함 | 문장 45 | — | 보류 (코드로 대신) |
| 14 | `stock/story/puppet/props/MACRO-DASH.png` | 거시 경제 지표 (금리·환율·경기) | 문장 46 | — | 보류 (코드로 대신) |
| 15 | `stock/story/puppet/props/NEWS-HYPE.png` | 호재 뉴스·차트만 봄 | 문장 48~49 | — | 보류 (코드로 대신) |
| 16 | `stock/story/puppet/props/STORM-CHART.png` | 악재가 한꺼번에 · 폭락장 | 문장 50 | — | 보류 (코드로 대신) |
| 17 | `stock/story/puppet/props/RATE-BANK.png` | 금리가 오르면 돈이 주식에서 예금으로 | 문장 53 | — | 보류 (코드로 대신) |
| 18 | `stock/story/puppet/props/FX-OUTFLOW.png` | 환율 급등 → 외국인 매도 · 돈이 빠져나감 | 문장 54 | — | 보류 (코드로 대신) |
| 19 | `stock/story/puppet/props/DEBT-BUBBLE.png` | 빚으로 부푼 시장 · 거품 | 문장 58 | — | 보류 (코드로 대신) |
| 20 | `stock/story/puppet/props/FEAR-GREED.png` | 과열 점검 · 내가 무리하는지 (공포·탐욕 지수) | 문장 60~61 | — | 보류 (코드로 대신) |
| 21 | `stock/story/puppet/props/RULE-SHIELD.png` | 원칙이 있으면 남의 말에 흔들리지 않음 | 문장 62·77~78 | — | 보류 (코드로 대신) |
| 22 | `stock/story/puppet/props/TIP-CHAT.png` | 리딩방·단톡방 종목 추천 · 수익 인증 | 문장 63~64 | — | 보류 (코드로 대신) |
| 23 | `stock/story/puppet/props/LEVERAGE-CRASH.png` | 레버리지로 빨리 메우려다 실패 | 문장 68·90~91 | — | 보류 (코드로 대신) |
| 24 | `stock/story/puppet/props/SLOW-CLIMB.png` | 천천히 · 꾸준히 · 장기 투자 | 문장 79 | — | 보류 (코드로 대신) |
| 25 | `stock/story/puppet/props/DCA-JAR.png` | 매달 정해진 금액만 매수 (적립식) | 문장 82 | — | 보류 (코드로 대신) |
| 26 | `stock/story/puppet/props/COMPOUND-STAIRS.png` | 꾸준히 쌓여 불어남 (복리) | 문장 92 | — | 보류 (코드로 대신) |

## 1. MARGIN-CALL — 반대매매 · 빚낸 돈이 강제로 매도됨 · 계좌 위험 경고

**저장 경로: `stock/story/puppet/props/MARGIN-CALL.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE smartphone standing upright showing a stock trading app: a red candlestick chart plunging steeply down to the bottom of the screen, and below it a big red button with the word SELL. A grey mechanical claw arm reaches in from the top right and presses the SELL button by itself, and plain paper banknotes (blank rectangles with no printing) fly out of the phone. The only word in the picture is SELL.
Centered, with at least 8% empty transparent margin on every side.
```

## 2. SAVINGS-DROP — 노후 자금·저축이 주식 손실로 줄어듦

**저장 경로: `stock/story/puppet/props/SAVINGS-DROP.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE pale-pink paper piggy bank with a thin crack on its side, sitting on top of a thick red stock-chart arrow that bends sharply downward, with two plain gold coins (no marks) sliding down the red arrow.
Centered, with at least 8% empty transparent margin on every side.
```

## 3. DELETE-APP — 주식 앱 지우기 · 시장을 떠남

**저장 경로: `stock/story/puppet/props/DELETE-APP.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE smartphone standing upright and, beside it, an open metal trash can. A small app icon (a rounded square showing a tiny green and red candlestick chart) is shown in mid-air being dropped from the phone into the trash can.
Centered, with at least 8% empty transparent margin on every side.
```

## 4. RULE-NOTE — 매매 원칙 · 투자 일지

**저장 경로: `stock/story/puppet/props/RULE-NOTE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE open spiral trading notebook: the left page shows a small hand-drawn candlestick chart, the right page shows three short blank lines, each starting with an empty checkbox. A yellow pencil rests across the pages. No writing.
Centered, with at least 8% empty transparent margin on every side.
```

## 5. INDEX-BASKET — 지수 · 분산 투자 (여러 회사를 나눠 담음)

**저장 경로: `stock/story/puppet/props/INDEX-BASKET.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE large sturdy woven basket filled with many small, different company buildings (factories with chimneys, office towers, shops, a hospital, a warehouse) packed tightly together, and above them one wide green stock-chart line rising gently from left to right like an arch over the basket.
Centered, with at least 8% empty transparent margin on every side.
```

## 6. CHIP-ALL-IN — 한 업종·한 종목에 몰빵 (반도체)

**저장 경로: `stock/story/puppet/props/CHIP-ALL-IN.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE large dark-green semiconductor computer chip with silver pins on every side, carrying a tall wobbly tower of gold coins and plain banknotes piled only on it; the tower leans dangerously to one side and a few coins are already falling off. A small red downward arrow next to the chip.
Centered, with at least 8% empty transparent margin on every side.
```

## 7. CIRCUIT-BREAKER — 거래 정지 (서킷브레이커)

**저장 경로: `stock/story/puppet/props/CIRCUIT-BREAKER.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE stock-exchange price-board screen on a stand, showing a red candlestick chart that plunges straight down; over the middle of the screen a big round red sign with a white pause symbol (two vertical bars). No numbers, no letters.
Centered, with at least 8% empty transparent margin on every side.
```

## 8. BEAR — 하락장 · 폭락

**저장 경로: `stock/story/puppet/props/BEAR.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE big dark-brown paper bear standing on its hind legs and swiping one front paw downward, pushing a thick red stock-chart arrow that points steeply down.
Centered, with at least 8% empty transparent margin on every side.
```

## 9. BOX-RANGE — 박스권 · 오래 제자리인 지수

**저장 경로: `stock/story/puppet/props/BOX-RANGE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE open cardboard box seen from the front; inside it a row of small red and green candlestick bars zigzags up and down, but every top only bumps against the box lid and every bottom against the box floor — the chart is trapped inside the box.
Centered, with at least 8% empty transparent margin on every side.
```

## 10. BULL — 상승장 · 불장

**저장 경로: `stock/story/puppet/props/BULL.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE strong golden-brown paper bull charging to the right with its horns lowered, lifting a thick green stock-chart arrow that points steeply up.
Centered, with at least 8% empty transparent margin on every side.
```

## 11. PAUSE-TRADING — 매매를 잠시 멈춤 (계좌는 그대로 둠)

**저장 경로: `stock/story/puppet/props/PAUSE-TRADING.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE smartphone standing upright showing a stock trading app with two big buttons, a green button with the word BUY and a red button with the word SELL; a large gold padlock hangs across both buttons. The only words in the picture are BUY and SELL.
Centered, with at least 8% empty transparent margin on every side.
```

## 12. SELL-BOTTOM — 바닥에서 매도 · 손실 확정

**저장 경로: `stock/story/puppet/props/SELL-BOTTOM.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE red stock-chart line that falls steeply from the top left and reaches its lowest point at the bottom right; exactly at that lowest point a paper cut-out hand presses a big round red button with the word SELL, and a red rubber-stamp ring mark appears beside the button. The only word in the picture is SELL.
Centered, with at least 8% empty transparent margin on every side.
```

## 13. DELISTED — 한 종목이 무너짐 · 끝내 회복 못 함

**저장 경로: `stock/story/puppet/props/DELISTED.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE ornate stock certificate (decorative border and a blank round seal, no writing) torn into two pieces, with a red stock-chart line falling off the torn edge all the way down.
Centered, with at least 8% empty transparent margin on every side.
```

## 14. MACRO-DASH — 거시 경제 지표 (금리·환율·경기)

**저장 경로: `stock/story/puppet/props/MACRO-DASH.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE control-panel dashboard with three big round dials side by side: a percent sign above the first dial, a dollar sign above the second, a small globe above the third; all three needles point high into the red zone. Only the symbols % and $ — no letters.
Centered, with at least 8% empty transparent margin on every side.
```

## 15. NEWS-HYPE — 호재 뉴스·차트만 봄

**저장 경로: `stock/story/puppet/props/NEWS-HYPE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE folded newspaper whose columns are only blank grey bars, with one big picture on the front page: a green stock-chart arrow shooting up with a small rocket at its tip. A magnifying glass is held close over that picture. No letters.
Centered, with at least 8% empty transparent margin on every side.
```

## 16. STORM-CHART — 악재가 한꺼번에 · 폭락장

**저장 경로: `stock/story/puppet/props/STORM-CHART.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE big dark storm cloud with three white lightning bolts striking a red candlestick chart below it that is crashing downward, with slanted rain.
Centered, with at least 8% empty transparent margin on every side.
```

## 17. RATE-BANK — 금리가 오르면 돈이 주식에서 예금으로

**저장 경로: `stock/story/puppet/props/RATE-BANK.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE classical bank building with four columns and a triangular roof, a big upward arrow with a percent sign on top of the roof, and a curving stream of plain gold coins flowing out of a small green stock chart on the left into the bank's open door. Only the % symbol — no letters.
Centered, with at least 8% empty transparent margin on every side.
```

## 18. FX-OUTFLOW — 환율 급등 → 외국인 매도 · 돈이 빠져나감

**저장 경로: `stock/story/puppet/props/FX-OUTFLOW.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE small stock-exchange building with a price board on its front showing only a red downward arrow; plain banknotes stream out of its door and fly away to the right toward a small airplane taking off.
Centered, with at least 8% empty transparent margin on every side.
```

## 19. DEBT-BUBBLE — 빚으로 부푼 시장 · 거품

**저장 경로: `stock/story/puppet/props/DEBT-BUBBLE.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE huge over-inflated red balloon with a green rising stock chart drawn on it, being pumped up by a hand pump whose hose comes from a stack of plain loan papers (blank sheets), and one sharp silver pin floating close to the balloon.
Centered, with at least 8% empty transparent margin on every side.
```

## 20. FEAR-GREED — 과열 점검 · 내가 무리하는지 (공포·탐욕 지수)

**저장 경로: `stock/story/puppet/props/FEAR-GREED.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE large semicircle gauge like the stock-market fear-and-greed meter: the arc goes from red on the left through yellow to green on the right, and the needle points to the far right end; a tiny bear figure sits at the left end of the arc and a tiny bull figure at the right end. No text, no numbers.
Centered, with at least 8% empty transparent margin on every side.
```

## 21. RULE-SHIELD — 원칙이 있으면 남의 말에 흔들리지 않음

**저장 경로: `stock/story/puppet/props/RULE-SHIELD.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE sturdy paper shield with a checklist emblem (three check marks) on its face, blocking many flying chat bubbles that contain small rocket icons and green upward arrows; the bubbles bounce off the shield.
Centered, with at least 8% empty transparent margin on every side.
```

## 22. TIP-CHAT — 리딩방·단톡방 종목 추천 · 수익 인증

**저장 경로: `stock/story/puppet/props/TIP-CHAT.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE smartphone standing upright with many overlapping chat bubbles bursting out of its screen: some contain a small rocket, some a green upward stock arrow, some a gold coin, and two contain the word BUY. The only word in the picture is BUY.
Centered, with at least 8% empty transparent margin on every side.
```

## 23. LEVERAGE-CRASH — 레버리지로 빨리 메우려다 실패

**저장 경로: `stock/story/puppet/props/LEVERAGE-CRASH.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE small toy rocket with three bold stripes painted on its body, crashed nose-down at the bottom of a steep red stock-chart line that falls from the top left; its body is bent and a puff of grey smoke rises.
Centered, with at least 8% empty transparent margin on every side.
```

## 24. SLOW-CLIMB — 천천히 · 꾸준히 · 장기 투자

**저장 경로: `stock/story/puppet/props/SLOW-CLIMB.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE calm tortoise walking steadily up a gently rising green stock-chart line as if it were a slope, carrying a small neat stack of gold coins on its shell.
Centered, with at least 8% empty transparent margin on every side.
```

## 25. DCA-JAR — 매달 정해진 금액만 매수 (적립식)

**저장 경로: `stock/story/puppet/props/DCA-JAR.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE tall glass jar half full of gold coins with a calendar page clipped to its front (a blank grid with one square circled), one coin dropping into the jar from above, and behind the jar a small green stock-chart line rising gently.
Centered, with at least 8% empty transparent margin on every side.
```

## 26. COMPOUND-STAIRS — 꾸준히 쌓여 불어남 (복리)

**저장 경로: `stock/story/puppet/props/COMPOUND-STAIRS.png`** — PNG 투명 700KB 이하 · 정사각 1024×1024

```
Square 1024x1024. ONE row of gold coin stacks growing taller from left to right like a staircase or a bar chart, with a green arrow curving up over them.
Centered, with at least 8% empty transparent margin on every side.
```

## 후보 — 아직 만들지 않음 (그 화 장면 표에 쓸 때 위 표로 옮겨 프롬프트를 쓴다)

- 후보 DICE — 도박 · 한 방 (주사위 + 차트) · 2화
- 후보 LOAN-CHAIN — 빚 · 마이너스 통장 (쇠공 사슬 + 계좌) · 2화
- 후보 AVERAGING-DOWN — 물타기 (떨어지는 차트에 계속 붓는 동전) · 2화
- 후보 REBALANCE-SCALE — 비중 맞추기 · 리밸런싱 (주식·현금 저울) · 3화
- 후보 WAIT-HOURGLASS — 매도 전 하루 기다림 (모래시계 + SELL) · 3화
- 후보 ALERT-OFF — 앱 알림 끄기 (빗금 친 종 + 차트 앱) · 3화
- 후보 EMERGENCY-FUND — 비상금·여윳돈은 따로 (우산 아래 현금) · 4화

## 변경 이력

| 판 | 날짜 | 바꾼 것 |
|---|---|---|
| v4.0 | 2026-10-24 | 그림은 꼭 필요할 때만 — 26장 모두 보류(코드 모션 그래픽으로 대신) · 1화 그림 0장 |
| v3.0 | 2026-10-24 | 주식과 바로 이어지는 그림 26장으로 새로 (차트·캔들·매매 앱·황소·곰·반도체 칩·주식 증서 · 그림 속 글자는 BUY·SELL·%·$ 만) · v2.0 21장은 `props/_old/` · 후보 7개도 주식 그림으로 |
| v2.0 | 2026-10-24 | 공통 소품으로 다시 씀 (뜻 일반화) |
| v1.0 | 2026-10-23 | 처음 만듦 — 1화 설명 소품 21장 |
