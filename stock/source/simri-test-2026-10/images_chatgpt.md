# 주식 '습관 테스트' 편 종이인형극 그림 20장 — ChatGPT용 (읽고 그대로 만들고 저장 경로에 올리기)

작성: 2026-10-27 (Claude, v1.2 — 20번 썸네일 그림을 **짝 쇼츠 썸네일에도** 씀: 오른쪽 세로 띠(가로 62.5~100%)를 9:16 으로 잘라 씀 → 주인공 머리·두 손·답안지를 그 띠 안에 (사용자 지시 2026-10-27 "쇼츠 관련 소스 모두 생성해" — `shorts/shorts.md` 6번). 만들 그림 수는 그대로 13장.)
(v1.1 — 2026-10-26 — **만들 그림 13장**: 1~8번 주인공 · 11번 낯선 사람 · 13~15번 쥐덫·바구니·새는 양동이 · 20번 썸네일 그림. 9·10·12·16·17·18·19번 7장은 옛 빨리 부자 편 그림을 그대로 다시 씀 — 이미 저장소에 있으니 **만들지 않는다**) 
(v1.0 — 인물 기준표 1 + 주인공 흰둥이 7 + 얼굴 없는 흰둥이 3 + 소품 6 + 배경 2 + 썸네일 그림 1 = 20장 · 남색 한지 배경은 다시 씀, 주제 '주식 투자 실패할 사람들은 절대 통과 못하는 습관 테스트') — 짝 문서 `stock/source/simri-test-2026-10/제작안.txt` · 같은 꼴 옛 빨리 부자 편 `git show 7de247ff:stock/source/ppalli-buja-2026-10/images_chatgpt.md`

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/stock/source/simri-test-2026-10/images_chatgpt.md

**무엇을 만드나:** 영상은 일본 축제 편과 같은 **종이인형극**이다 — 빈 무대 배경 1장 위에 **오린 종이 인형(투명 그림)** 을 올리고, 움직임(들어옴·흔들림·고개 떨굼·튀어나옴)과 숫자·그래프·A·B·C 보기 카드·점수 같은 글자는 **영상 코드가 만든다.**
→ 그림은 **사람·물건·장소만.** 인형은 **한 장에 하나, 한 가지 모습만** 그린다.
→ 사람은 모두 **흰 종이 인형(흰둥이)** 이다. **주인공 '투자자'(= 시청자 자신)만 눈·눈썹·입이 있어 표정이 보이고**, 나머지 사람은 모두 **이목구비가 없는 흰둥이**다.
→ **그림 20장 모두 글자·숫자·로고를 하나도 넣지 않는다** — 외국인 시청자도 보는 영상이라, 한글은 자막과 A·B·C 보기 카드(코드)에만 쓴다. 영어·숫자(BUY·SELL·KOSPI·%)도 그림에는 넣지 않는다 — 필요한 곳은 코드가 얹는다.
→ 숫자·해설 장면 배경은 축제 편의 `test/puppet/P-PAPER.jpg`(남색 한지)를 그대로 쓴다 — **다시 만들지 않는다.**
→ **썸네일 그림(20번)에도 글자를 넣지 않는다** — 제목 2줄·말풍선은 Claude 가 코드로 얹는다 (그림 1장으로 썸네일 3안).

| 번호 | 파일 | 크기 | 무엇 | 쓰는 곳 (제작안 장면) |
|---|---|---|---|---|
| 1 | `stock/source/simri-test-2026-10/puppet/HERO-SHEET.jpg` | 가로 1536×1024 | 주인공 인물 기준표 (네 방향 + 얼굴 넷) | 영상에는 안 씀 — 2~8번·21번이 이 얼굴·몸을 그대로 따름 |
| 2 | `stock/source/simri-test-2026-10/puppet/HERO-PHONE.png` | 정사각 1024 · 투명 | 주인공 — 서서 휴대전화를 두 손으로, 궁금한 얼굴 | 항목 1·2·5·6 (커뮤니티·메신저·알림·매수 준비) |
| 3 | `stock/source/simri-test-2026-10/puppet/HERO-THINK.png` | 정사각 1024 · 투명 | 주인공 — 턱에 손, 고민하는 얼굴 | 항목 1~10 보기 장면 (매번) · 통과 기준 '주의' |
| 4 | `stock/source/simri-test-2026-10/puppet/HERO-PROUD.png` | 정사각 1024 · 투명 | 주인공 — 두 주먹을 들고 가슴을 편 과신 | 항목 3·4 · 해설 3·4 |
| 5 | `stock/source/simri-test-2026-10/puppet/HERO-SHOCK.png` | 정사각 1024 · 투명 | 주인공 — 휴대전화를 얼굴 앞에, 놀라 굳음 | 항목 7·8·9 · 해설 8 |
| 6 | `stock/source/simri-test-2026-10/puppet/HERO-DESPAIR.png` | 정사각 1024 · 투명 | 주인공 — 바닥에 앉아 머리를 감싸 쥠 | 항목 10 · 통과 기준 '불통과' · 해설 9·10 |
| 7 | `stock/source/simri-test-2026-10/puppet/HERO-PLAN.png` | 정사각 1024 · 투명 | 주인공 — 빈 클립보드와 연필, 차분한 미소 | 해설마다 끝 문장 '그래서 …' (10점 답) · 통과 기준 '통과' · 정리 |
| 8 | `stock/source/simri-test-2026-10/puppet/HERO-BOW.png` | 정사각 1024 · 투명 | 주인공 — 허리 굽혀 인사 | 마무리 |
| 9 | **있음 — 만들지 않음 (옛 그림 다시 씀)** `stock/source/simri-test-2026-10/puppet/W-COLLEAGUE.png` | 정사각 1024 · 투명 | 얼굴 없는 흰둥이 — 휴대전화를 내밀어 자랑 | 항목 1·3 · 해설 1 |
| 10 | **있음 — 만들지 않음 (옛 그림 다시 씀)** `stock/source/simri-test-2026-10/puppet/W-CROWD.png` | 가로 1536×1024 · 투명 | 얼굴 없는 흰둥이 열 명쯤 — 모두 고개 숙여 휴대전화 | 도입 · 항목 1·9 · 통과 기준 · 해설 1 |
| 11 | `stock/source/simri-test-2026-10/puppet/W-SCAMMER.png` | 정사각 1024 · 투명 | 얼굴 없는 흰둥이 — 검은 긴 코트·챙 넓은 모자, 손짓으로 부름 | 항목 2 · 해설 2 |
| 12 | **있음 — 만들지 않음 (옛 그림 다시 씀)** `stock/source/simri-test-2026-10/puppet/P-CASH.png` | 정사각 1024 · 투명 | 지폐 다발 (숫자·초상 없음) | 도입 · 항목 6·10 · 해설 9·10 |
| 13 | `stock/source/simri-test-2026-10/puppet/P-TRAP.png` | 정사각 1024 · 투명 | 금화 미끼를 올린 쥐덫 (사기 단체방의 비유) | 항목 2 · 해설 2 |
| 14 | `stock/source/simri-test-2026-10/puppet/P-BASKET.png` | 정사각 1024 · 투명 | 달걀이 가득 든 바구니 하나 (한 종목에 몰아 넣기의 비유) | 항목 4 · 해설 4 |
| 15 | `stock/source/simri-test-2026-10/puppet/P-LEAKBUCKET.png` | 정사각 1024 · 투명 | 구멍 난 양동이에서 금화가 샘 (돈이 새는 곳) | 통과 기준 · 해설 5 |
| 16 | **있음 — 만들지 않음 (옛 그림 다시 씀)** `stock/source/simri-test-2026-10/puppet/P-CHAIN.png` | 가로 1536×1024 · 투명 | 쇠공·사슬·열린 발목 고리 (빚) | 항목 9 · 통과 기준 · 해설 9 |
| 17 | **있음 — 만들지 않음 (옛 그림 다시 씀)** `stock/source/simri-test-2026-10/puppet/P-GRAB.png` | 가로 1536×1024 · 투명 | 커다란 흰 종이 손이 주권 더미를 낚아챔 (강제 매도) | 도입 · 해설 9 |
| 18 | **있음 — 만들지 않음 (옛 그림 다시 씀)** `stock/source/simri-test-2026-10/puppet/S-OFFICE.jpg` | 가로 1536×1024 | 빈 무대 — 낮의 사무실 | 항목 1·3·5 · 해설 1 |
| 19 | **있음 — 만들지 않음 (옛 그림 다시 씀)** `stock/source/simri-test-2026-10/puppet/S-HOME-NIGHT.jpg` | 가로 1536×1024 | 빈 무대 — 밤 아파트 거실 | 항목 2·4·6~10 |
| 20 | `stock/source/simri-test-2026-10/images/TH-ART.jpg` | 가로 3:2 (1536×1024) | 썸네일 그림 (글자 없음 — 문구·말풍선은 코드) | 롱폼 썸네일 3안 · 쇼츠 썸네일(오른쪽 세로 띠 — v1.2) |
| 21 | (없음 — 다시 씀) `test/puppet/P-PAPER.jpg` | — | 남색 한지 (숫자·해설 장면 배경) | **만들지 않는다** |

※ 번호는 만드는 순서다 — **1번(인물 기준표)을 가장 먼저** 만들고, 2~8번과 20번은 1번의 주인공과 머리 모양·눈·눈썹·목수건이 똑같아야 한다. 배경(18~19번)은 소품 다음에 만든다. 21번은 만들지 않는다 (이미 있음).

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 1~20번 가운데 **표에 '있음'이라고 적힌 7장(9·10·12·16·17·18·19번)을 뺀 13장**을 **번호 순서대로 모두** 만든다 (1~8·11·13·14·15·20번). 있음 7장은 저장소에 이미 있으니 만들지도 올리지도 않는다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. **한 장에 프롬프트에 적힌 것만** 그린다 (다른 사람·물건을 같이 그리지 않는다).
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다.
   - **1~19번:** 프롬프트 맨 앞에 아래 **공통 화풍** 문단을 그대로 붙인다 (한 무대의 인형처럼 — 같은 종이 질감·같은 색). **20번**도 공통 화풍을 붙인다.
   - **1~8번·20번(주인공):** 공통 화풍 다음에 **주인공** 문단을 그대로 붙이고, 1번 기준표와 머리·눈·눈썹·목수건을 똑같이 맞춘다.
   - **9~11번(얼굴 없는 흰둥이):** 공통 화풍 다음에 **얼굴 없는 흰둥이** 문단을 그대로 붙인다.
   - **2~17번(투명 인형·소품):** 마지막에 **CUTOUT** 문단도 그대로 붙인다.
3. 사람 인형은 실존 인물이나 만화 캐릭터를 닮게 그리지 않는다 (특히 흰 강아지·유명 캐릭터처럼 보이면 안 된다 — 단순한 흰 종이 사람). 물건은 실제 회사(은행·증권사·앱) 모양·색·로고를 닮게 그리지 않는다.
4. **잘림 검사 (2~17번 필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`이면 그림을 더 작게(여백을 더 넓게) 다시 만들고 다시 검사한다. 투명이 아니면(귀퉁이 알파가 0 이 아님) 배경을 **순초록 #00FF00 한 색 평면**으로 다시 만든다 (그때는 초록 바탕 기준으로 여백을 본다).
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
5. **20장 모두 글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 휴대전화 화면·클립보드·시험지·지폐·주권·금화에도 없음 (빈 칸, 단색, 또는 뜻 없는 가는 줄로). 만든 뒤 그림을 확대해 글자·숫자·로고처럼 보이는 것이 하나라도 있으면 다시 만든다.
   - 주인공(2~8번·20번)은 **1번과 같은 머리·눈·눈썹·연하늘 목수건**인지 나란히 놓고 본다. 다르면 다시 만든다.
   - 얼굴 없는 흰둥이(9~11번)에게 눈·눈썹·코·입·머리카락이 조금이라도 생기면 다시 만든다. 목수건도 달지 않는다 (주인공과 헷갈림).
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`2. stock/source/simri-test-2026-10/puppet/HERO-PHONE.png`). 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게). 1~19번은 `stock/source/simri-test-2026-10/puppet/` 폴더, 20번은 `stock/source/simri-test-2026-10/images/` 폴더.
   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다. 올린 뒤 GitHub 에 있는 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     - 1·18·19·20번(JPEG): RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.
     - 2~17번(PNG, 투명 유지): 아래 코드 그대로.
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
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[stock] simri <파일 이름> 이미지` (예: `[stock] simri HERO-SHEET.jpg 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 묻지 말고 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."** 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 표의 파일 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/simri-test-2026-10/puppet (20번은 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/simri-test-2026-10/images) 에 끌어다 놓고 Commit changes"

## 공통 화풍 (1~20번 프롬프트 맨 앞에 그대로 붙임)
```
STYLE: Korean paper-cut puppet theater (hanji papercraft), like a festival paper puppet show. Everything is made of flat layered colored paper with a visible fine hanji-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Palette: deep navy #1B2440, slate blue #3A4A6B, warm cream #F2E6CF, off-white #F7F3EA, charcoal #2B2B2B, office gray #8A8F98, muted light blue #A9C1D9, with small accents only of loss red #D92B2B, teal #1FA79A and signal yellow #F2C230. Flat side view, like a stage seen from the audience. ABSOLUTELY NO text, letters, numbers, logos, brand marks or watermarks anywhere — phone screens, papers, clipboards, banknotes, coins, certificates and monitors are blank, single-colored, or carry only simple meaningless lines.
```

## 주인공 (1~8번·20번 — 공통 화풍 다음에 그대로 붙임)
```
CHARACTER — "the Investor" (fictional, gender-neutral adult; not resembling any real person or any existing cartoon character), the ONLY puppet with a face. Body: a plain white paper figure built exactly like the faceless white crowd figures — a round head and a simple rounded body cut from off-white paper (#F7F3EA) with very light gray layer shadows, simple mitten-shaped hands, no hair, no ears, no nose. Face: a clear, expressive paper-cut face — two dark navy oval eyes with small white highlights, bold expressive navy eyebrows, and a simple navy mouth whose shape shows the emotion, plus two soft pink paper cheeks. The only clothing detail is a small light-blue (#A9C1D9) neckerchief tied at the neck, so the Investor is recognizable in every scene. Keep exactly the same head shape, body proportions, eyes, eyebrows and neckerchief as the character reference sheet.
```

## 얼굴 없는 흰둥이 (9~11번 — 공통 화풍 다음에 그대로 붙임)
```
FIGURE — plain white paper human figures: a round head and a simple rounded body cut from off-white paper (#F7F3EA) with only very light gray layer shadows; NO facial features at all (no eyes, eyebrows, nose, mouth, cheeks, ears or hair) and NO neckerchief; no clothing details except a soft light-gray paper layer suggesting a jacket, unless the prompt says otherwise; hands are simple mitten shapes. They must look clearly different from the Investor, who is the only figure with a face.
```

## CUTOUT (2~17번 — 맨 마지막에 그대로 붙임)
```
CUTOUT: the described subject only, as an isolated paper puppet cutout on a fully transparent background (PNG with alpha channel) — no ground, no cast shadow on the ground, no scenery, no frame, no other objects or people. A thin cream (#F2E6CF) paper border about 6 px wide runs around the outer silhouette, like a hand-cut puppet. The WHOLE subject must be fully visible with generous empty margin: nothing may touch or cross the canvas edges — keep at least 8% empty transparent space on every side (left, right, top and bottom). If a transparent background is impossible, make the whole background one flat pure chroma green #00FF00 with no shading, and use no green at all on the subject.
```

## 1. HERO-SHEET — 주인공 인물 기준표
**저장 경로: `stock/source/simri-test-2026-10/puppet/HERO-SHEET.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (영상에는 안 쓰고, 다른 그림의 기준)
```
Character reference sheet on a plain flat warm cream (#F2E6CF) paper background. Top row: the same Investor paper puppet standing in a relaxed neutral pose four times, evenly spaced with clear gaps — front view, three-quarter view, side view facing right, back view. Bottom row: four large head-and-shoulders close-ups of the same Investor, evenly spaced — calm gentle smile, big proud open-mouthed grin, shocked with wide round eyes and a small open O mouth, worried despair with eyebrows tilted up in the middle and the mouth turned down. Same head, eyes, eyebrows, pink cheeks and light-blue neckerchief in every view. No labels, no text, no numbers.
```

## 2. HERO-PHONE — 서서 휴대전화를 두 손으로, 궁금한 얼굴
**저장 경로: `stock/source/simri-test-2026-10/puppet/HERO-PHONE.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor standing, body in three-quarter view facing left, holding a smartphone in front of the chest with both hands, the blank back of the phone toward the viewer and its screen toward the Investor. Eyebrows raised, eyes fixed on the screen, a small curious open smile — interested and a little tempted. Full body.
```

## 3. HERO-THINK — 턱에 손, 고민하는 얼굴
**저장 경로: `stock/source/simri-test-2026-10/puppet/HERO-THINK.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor standing, body in three-quarter view facing right, right hand raised to the chin, left arm folded across the body supporting the right elbow. Eyes glancing up to the side, eyebrows slightly knit, mouth a small straight line — thinking hard about which choice to make. Full body.
```

## 4. HERO-PROUD — 두 주먹을 들고 가슴을 편 과신
**저장 경로: `stock/source/simri-test-2026-10/puppet/HERO-PROUD.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor standing tall facing the viewer, chest pushed out, both fists raised above the shoulders in triumph, a huge open-mouthed grin, eyes closed in happy upside-down arcs, eyebrows high — overconfident, sure of being a genius. Full body.
```

## 5. HERO-SHOCK — 휴대전화를 얼굴 앞에, 놀라 굳음
**저장 경로: `stock/source/simri-test-2026-10/puppet/HERO-SHOCK.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor standing and leaning back, holding a smartphone close in front of the face with both hands (blank back of the phone toward the viewer, the face still visible above it), eyes wide and round, eyebrows shot up, mouth a small open O, one small paper sweat drop beside the head — frozen in shock at a sudden loss. Full body.
```

## 6. HERO-DESPAIR — 바닥에 앉아 머리를 감싸 쥠
**저장 경로: `stock/source/simri-test-2026-10/puppet/HERO-DESPAIR.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor sitting on the floor with knees pulled up, both hands holding the sides of the head, head bowed, eyes squeezed shut, eyebrows tilted up in the middle, mouth turned down, shoulders slumped — despair after a big loss. Full body, sitting.
```

## 7. HERO-PLAN — 빈 클립보드와 연필, 차분한 미소
**저장 경로: `stock/source/simri-test-2026-10/puppet/HERO-PLAN.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor standing calm and upright, body in three-quarter view facing left, holding a clipboard in the left hand with its blank cream paper turned toward the viewer — the paper shows only four simple empty square boxes in a column, three of them with small teal check marks, no letters and no numbers — and a short pencil in the right hand. Relaxed eyebrows, eyes open and steady, a gentle confident smile — calm and prepared. Full body.
```

## 8. HERO-BOW — 허리 굽혀 인사
**저장 경로: `stock/source/simri-test-2026-10/puppet/HERO-BOW.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor in side view facing left, bowing politely from the waist at about 45 degrees, both mitten hands together in front of the body, eyes closed in gentle happy arcs, a soft smile — thanking the audience. Full body.
```

## 9. W-COLLEAGUE — 휴대전화를 내밀어 자랑하는 동료 — **있음 (만들지 않음 · 옛 빨리 부자 편 그림을 다시 씀)**
**저장 경로: `stock/source/simri-test-2026-10/puppet/W-COLLEAGUE.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
One faceless white figure (a coworker) standing in three-quarter view facing right, proudly stretching the right arm forward and holding up a smartphone with its blank screen facing right, the left hand on the hip, chest puffed out and head tilted back a little — showing off a profit. Full body.
```

## 10. W-CROWD — 모두 고개 숙여 휴대전화를 보는 사람들 — **있음 (만들지 않음 · 옛 빨리 부자 편 그림을 다시 씀)**
**저장 경로: `stock/source/simri-test-2026-10/puppet/W-CROWD.png`** — PNG 투명 700KB 이하 · 가로 1536×1024
```
About ten faceless white figures standing in a loose cluster with small gaps, slightly overlapping, all bending their heads down to look at smartphones held in their hands (phones blank), varied heights, each with a slightly different light-gray jacket layer. Full bodies, side-by-side like a crowd on a stage.
```

## 11. W-SCAMMER — 검은 코트와 모자, 손짓으로 부르는 사람
**저장 경로: `stock/source/simri-test-2026-10/puppet/W-SCAMMER.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
One faceless white figure wearing a long dark charcoal (#2B2B2B) coat with the collar turned up and a wide-brim charcoal hat pulled low (the head under the hat is still plain white with no features), leaning forward slightly in three-quarter view facing left, the left hand holding out a smartphone (blank back toward the viewer), the right hand beckoning with one curled finger — a suspicious stranger inviting someone in. Full body.
```

## 12. P-CASH — 지폐 다발 — **있음 (만들지 않음 · 옛 빨리 부자 편 그림을 다시 씀)**
**저장 경로: `stock/source/simri-test-2026-10/puppet/P-CASH.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
A thick bundle of paper banknotes held together by a cream paper band, the top notes slightly fanned out; the banknotes are muted sage green-gray with only simple meaningless decorative lines — no numbers, no portraits, no symbols.
```

## 13. P-TRAP — 금화 미끼를 올린 쥐덫
**저장 경로: `stock/source/simri-test-2026-10/puppet/P-TRAP.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
A wooden spring mousetrap seen from the front at a slight angle, the metal snap bar pulled back and set, with one shiny gold coin (plain, no symbols) placed on the bait plate as bait — an obvious trap that looks tempting.
```

## 14. P-BASKET — 달걀이 가득 든 바구니 하나
**저장 경로: `stock/source/simri-test-2026-10/puppet/P-BASKET.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
One woven light-brown paper basket with an arched handle, side view, filled to the top with about eight white eggs.
```

## 15. P-LEAKBUCKET — 구멍 난 양동이에서 금화가 샘
**저장 경로: `stock/source/simri-test-2026-10/puppet/P-LEAKBUCKET.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
A slate-blue metal bucket seen from the front, filled to the rim with plain gold coins, with three round holes in its side; from each hole a short stream of small plain gold coins is spilling out and falling downward — money leaking away.
```

## 16. P-CHAIN — 쇠공과 사슬 (빚) — **있음 (만들지 않음 · 옛 빨리 부자 편 그림을 다시 씀)**
**저장 경로: `stock/source/simri-test-2026-10/puppet/P-CHAIN.png`** — PNG 투명 700KB 이하 · 가로 1536×1024
```
A heavy dark iron ball on the left connected by a short thick chain to an open iron ankle shackle on the right, lying in a horizontal row.
```

## 17. P-GRAB — 주권 더미를 낚아채는 커다란 손 (강제 매도) — **있음 (만들지 않음 · 옛 빨리 부자 편 그림을 다시 씀)**
**저장 경로: `stock/source/simri-test-2026-10/puppet/P-GRAB.png`** — PNG 투명 700KB 이하 · 가로 1536×1024
```
A giant plain off-white paper hand (mitten-like, no nails, no sleeve details) swooping in from the upper right and grabbing a stack of blank cream stock certificates (only decorative border lines, no text) from below, with three certificates flying loose to the left.
```

## 18. S-OFFICE — 빈 무대: 낮의 사무실 — **있음 (만들지 않음 · 옛 빨리 부자 편 그림을 다시 씀)**
**저장 경로: `stock/source/simri-test-2026-10/puppet/S-OFFICE.jpg`** — JPEG 700KB 이하 · 가로 1536×1024
```
Empty stage backdrop: a modern open-plan office in daylight seen straight from the front — two rows of desks with blank dark monitors and office chairs on the left and right sides, a long window with soft daylight and pale city buildings in the back, a few potted plants. The floor begins at about 70% of the picture height. The center of the stage is open and uncluttered (room for puppets). No people. No text on monitors, windows or walls.
```

## 19. S-HOME-NIGHT — 빈 무대: 밤 아파트 거실 — **있음 (만들지 않음 · 옛 빨리 부자 편 그림을 다시 씀)**
**저장 경로: `stock/source/simri-test-2026-10/puppet/S-HOME-NIGHT.jpg`** — JPEG 700KB 이하 · 가로 1536×1024
```
Empty stage backdrop: an apartment living room at night seen straight from the front — a low sofa on the left, a small side desk with a warm lamp on the right, a big window in the back showing a dark navy night sky and distant city lights. Warm lamp light mixed with cool night blue. The floor begins at about 70% of the picture height. The center of the stage is open and uncluttered (room for puppets). No people. No text anywhere.
```

## 20. TH-ART — 썸네일 그림 (글자 없음)
**저장 경로: `stock/source/simri-test-2026-10/images/TH-ART.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (코드가 16:9 로 자르고 제목 2줄·말풍선을 얹음 — 위아래 80px 은 잘릴 수 있음 · v1.2 쇼츠는 오른쪽 세로 띠 x 960~1536 을 9:16 으로 씀)
```
Thumbnail illustration, landscape. Background: a deep navy (#1B2440) hanji paper backdrop with a large bold red (#D92B2B) paper zigzag line crashing down from the upper left to the lower right like a falling stock chart (no axes, no grid labels, no numbers). The Investor puppet with its face is shown from the knees up on the RIGHT third of the picture, the head at about 30–38% from the top of the picture: holding a blank answer sheet low in the left hand (the sheet shows only a column of empty square boxes and three big red X marks — no letters, no numbers) while looking down at it, the right hand covering the mouth; eyebrows tilted up and knit in the middle, worried eyes looking down, head slightly lowered, shoulders drooped — realizing the test is failed and money was lost. Behind on the left, three small faceless white figures in dim shadow looking at their phones. Keep the bottom 35% of the picture and the area to the left of the Investor's head calm, dark and uncluttered navy (title text and speech bubbles will be added there later by code). The Investor's head, hands and the answer sheet stay between 12% and 60% of the picture height; below 60% only the body and legs. The Investor's head, both hands and the answer sheet must also stay fully inside the right vertical strip from 62.5% to 100% of the picture width, roughly centered in that strip (the strip is cut out for a vertical 9:16 version) — do not let the head or hands cross to the left of 62.5% width. ABSOLUTELY NO text, letters, numbers or logos anywhere.
```
