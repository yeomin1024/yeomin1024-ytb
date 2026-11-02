# 주식 롱폼 1편 「빨리 벌고 싶은 사람은 절대 통과 못하는 주식 테스트」 종이인형극 그림 13장 — ChatGPT용 (읽고 그대로 만들고 저장 경로에 올리기)

작성: 2026-11-02 (Claude, v1.1 — 대본 v8 · 제작안 v1.1 · **만들 그림 13장** (1~13번): 주인공 흰둥이 7 · 얼굴 없는 흰둥이 3 · 빈 무대 2 · 썸네일 그림 1. 낮 사무실·밤 거실 무대와 남색 한지는 이미 저장소에 있으니 **만들지 않는다**.) — 사용자 지시 2026-11-01 "1편만 영상 관련 소스 만들어봐 이미지 chatgpt 말할거 알려주고" · 2026-11-02 "일본 축제 영상처럼 종이인형극에 필요한 이미지 생성한거 맞아? 다시 확인해서 알려줘" · 짝 문서 `stock/source/ppalli-test-2026-11/제작안.txt` · 같은 꼴 옛 편 `stock/source/simri-test-2026-10/images_chatgpt.md` · 일본 축제 편 `test/puppet/images_chatgpt.md`

v1.1 에서 바뀐 것 (v1.0 = 8장, 커밋 051ec095 — 아직 만들지 않았다면 v1.0 은 버리고 이 파일만 쓴다):
- **8·10번 동료·무리를 새로 만든다** — v1.0 은 옛 편 그림을 다시 쓰려 했는데, 그 그림은 머리가 크고 둥근 **귀여운 비율**이라 옛 편에서도 '다시 만듦'으로 적혀 있던 것 (어른 비율 약 6.5등신 — 2026-10-26 사용자 지시).
- **9번 지인 · 11번 지하철 무대 · 12번 카페 무대를 더한다** — 일본 축제 편처럼 이야기 장면마다 자기 무대와 인물이 있게 (선택 3 = 지하철에서 폭락을 봄 · 선택 4 = 카페에서 지인이 종목을 추천).
- **2번·6번 주인공이 오른쪽을 본다** — 주인공은 늘 화면 왼쪽에 서고 동료·카드가 오른쪽에 나오므로.

이 파일 주소: Claude 가 알려 준 **커밋 고정 주소** (`https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/<커밋>/stock/source/ppalli-test-2026-11/images_chatgpt.md`) — 그림은 아래 저장 경로대로 **main** 에 올린다.

**무엇을 만드나:** 영상은 일본 축제 편과 같은 **종이인형극**이다 — **빈 무대 배경 1장** 위에 **오린 종이 인형(투명 그림)** 을 올리고, 움직임(들어옴·흔들림·떨림)과 숫자·그래프·A·B 보기 카드·도장 같은 글자는 **영상 코드가 만든다.**
→ 인형은 **한 장에 하나(무리는 한 무리), 한 가지 모습만** 그린다. 상태마다 그림을 따로 만들지 않는다.
→ 주인공 '투자자'(= 시청자 자신, 대본의 김씨)만 눈·눈썹·입이 있어 표정이 보인다. 나머지는 **얼굴 없는 흰둥이** — 둘 다 **귀엽지 않은 어른 비율**.
→ **그림 13장 모두 글자·숫자·로고를 하나도 넣지 않는다** — 한글은 자막과 A·B 보기 카드(코드)에만, 영어·숫자(NASDAQ·ETF·%)도 코드가 얹는다.
→ **썸네일 그림(13번)에도 글자를 넣지 않는다** — 제목 2줄·말풍선은 Claude 가 코드로 얹는다 (그림 1장으로 썸네일 3안).

| 번호 | 파일 | 크기 | 무엇 | 쓰는 곳 (제작안 장면) |
|---|---|---|---|---|
| 1 | `stock/source/ppalli-test-2026-11/puppet/HERO-SHEET.jpg` | 가로 1536×1024 | 주인공 인물 기준표 (네 방향 + 얼굴 넷) | 영상에는 안 씀 — 2~7번·13번이 이 얼굴·몸을 그대로 따름 |
| 2 | `stock/source/ppalli-test-2026-11/puppet/HERO-PHONE.png` | 정사각 1024 · 투명 | 주인공 — 서서 휴대전화를 두 손으로, 궁금한 얼굴 (**오른쪽을 봄**) | 선택 1·4·5 이야기 장면 |
| 3 | `stock/source/ppalli-test-2026-11/puppet/HERO-THINK.png` | 정사각 1024 · 투명 | 주인공 — 턱에 손, 고민하는 얼굴 | 도입 · 선택 1~5 보기 장면 · 선택 2 이야기 · 해설 '물론…하지만' · 결과 '주의' |
| 4 | `stock/source/ppalli-test-2026-11/puppet/HERO-SHOCK.png` | 정사각 1024 · 투명 | 주인공 — 휴대전화를 얼굴 앞에, 놀라 굳음 | 선택 3 (지하철 — 나스닥 −32%) |
| 5 | `stock/source/ppalli-test-2026-11/puppet/HERO-DESPAIR.png` | 정사각 1024 · 투명 | 주인공 — 바닥에 앉아 머리를 감싸 쥠 | 도입 (1억 → 180만 원) · 결과 '불통과' |
| 6 | `stock/source/ppalli-test-2026-11/puppet/HERO-PLAN.png` | 정사각 1024 · 투명 | 주인공 — 빈 클립보드와 연필, 차분한 미소 (**오른쪽을 봄**) | 해설 정답 카드 · '그래서 정답은…' · 결과 '통과' · 정리 |
| 7 | `stock/source/ppalli-test-2026-11/puppet/HERO-BOW.png` | 정사각 1024 · 투명 | 주인공 — 허리 굽혀 인사 | 마무리 인사 |
| 8 | `stock/source/ppalli-test-2026-11/puppet/W-COLLEAGUE.png` | 정사각 1024 · 투명 | 얼굴 없는 흰둥이 — 회사 동료, 휴대전화를 내밀어 수익 자랑 (**왼쪽을 봄**) | 선택 1 (낮 사무실) |
| 9 | `stock/source/ppalli-test-2026-11/puppet/W-FRIEND.png` | 정사각 1024 · 투명 | 얼굴 없는 흰둥이 — 평상복 지인, 휴대전화를 내밀며 엄지 척 (**왼쪽을 봄**) | 선택 4 (카페) |
| 10 | `stock/source/ppalli-test-2026-11/puppet/W-CROWD.png` | 가로 1536×1024 · 투명 | 얼굴 없는 흰둥이 여덟 명쯤 — 모두 휴대전화를 들고 들뜬 무리 (**왼쪽을 봄**) | 선택 1 · 선택 5 |
| 11 | `stock/source/ppalli-test-2026-11/puppet/S-SUBWAY.jpg` | 가로 1536×1024 | 빈 무대 — 지하철 객차 안 | 선택 3 (영상 코드가 어둡게 깔고 그래프를 얹음) |
| 12 | `stock/source/ppalli-test-2026-11/puppet/S-CAFE.jpg` | 가로 1536×1024 | 빈 무대 — 저녁 카페 | 선택 4 |
| 13 | `stock/source/ppalli-test-2026-11/images/TH-ART.jpg` | 가로 3:2 (1536×1024) | 썸네일 그림 (글자 없음 — 제목 2줄·말풍선은 코드) | 롱폼 썸네일 3안 |
| — | **있음 — 만들지 않음** `stock/source/simri-test-2026-10/puppet/S-OFFICE.jpg` · `S-HOME-NIGHT.jpg` | — | 빈 무대 — 낮 사무실 · 밤 거실 | 선택 1 · 선택 2·5 |
| — | **있음 — 만들지 않음** `test/puppet/P-PAPER.jpg` | — | 남색 한지 (숫자·해설 장면 배경 — 일본 축제 편과 같음) | 도입 · 보기 · 해설 · 결과 · 정리 |

※ 번호는 만드는 순서다 — **1번(인물 기준표)을 가장 먼저** 만들고, 2~7번·13번 주인공은 1번과 머리 모양·몸 비율·눈·눈썹·넥타이가 똑같아야 한다. 8~10번 흰둥이도 1번과 **같은 어른 비율**이다.

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 1~13번 **13장을 번호 순서대로 모두** 만든다. '있음'이라고 적힌 그림은 만들지도 올리지도 않는다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. **한 장에 프롬프트에 적힌 것만** 그린다 (다른 사람·물건을 같이 그리지 않는다).
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다. 붙이는 문단:
   | 번호 | 맨 앞 | 그다음 | 맨 끝 |
   |---|---|---|---|
   | 1~7 | 공통 화풍 | 주인공 | (2~7번만) CUTOUT |
   | 8~10 | 공통 화풍 | 얼굴 없는 흰둥이 | CUTOUT |
   | 11~12 | 공통 화풍 | — | — |
   | 13 | 공통 화풍 | 주인공 + 얼굴 없는 흰둥이 | — |
3. 사람 인형은 실존 인물이나 만화 캐릭터를 닮게 그리지 않는다 (특히 흰 강아지·유명 캐릭터처럼 보이면 안 된다 — 단순한 흰 종이 사람). 휴대전화·클립보드·지하철·카페는 실제 회사·노선의 모양·색·로고를 닮게 그리지 않는다.
4. **잘림 검사 (2~10번 필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`이면 그림을 더 작게(여백을 더 넓게) 다시 만들고 다시 검사한다. 투명이 아니면(귀퉁이 알파가 0 이 아님) 배경을 **순초록 #00FF00 한 색 평면**으로 다시 만든다 (그때는 초록 바탕 기준으로 여백을 본다).
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
5. **13장 모두 글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 휴대전화 화면·클립보드·지하철 노선도·광고판·카페 메뉴판에도 없음 (빈 칸, 단색, 또는 뜻 없는 가는 줄로). 만든 뒤 그림을 확대해 글자·숫자·로고처럼 보이는 것이 하나라도 있으면 다시 만든다.
   - 주인공(2~7·13번)은 **1번과 같은 머리·몸 비율·눈·눈썹·연하늘 넥타이**인지 나란히 놓고 본다. 다르면 다시 만든다.
   - **귀엽지 않은지** 본다 (1~10·13번 모든 사람): 머리가 몸에 비해 크거나(어른 비율 약 6.5등신이 아님), 머리가 동그란 공 모양이거나, 눈이 크고 둥글거나, 눈에 흰 반짝임·볼에 분홍 볼터치가 있으면 다시 만든다 — 마스코트·인형 장난감처럼 보이면 안 된다.
   - 8~10번 흰둥이는 **얼굴이 전혀 없고 넥타이가 없는지** 본다 (넥타이는 주인공만).
   - **보는 방향**을 본다: 2·6번 주인공은 오른쪽, 8·9·10번 흰둥이는 왼쪽.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`2. stock/source/ppalli-test-2026-11/puppet/HERO-PHONE.png`). 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게). 1~12번은 `stock/source/ppalli-test-2026-11/puppet/` 폴더, 13번은 `stock/source/ppalli-test-2026-11/images/` 폴더.
   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다. 올린 뒤 GitHub 에 있는 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     - 1·11·12·13번(JPEG): RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.
     - 2~10번(PNG, 투명 유지): 아래 코드 그대로.
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
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[stock] ppalli 1편 <파일 이름> 이미지` (예: `[stock] ppalli 1편 HERO-SHEET.jpg 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 묻지 말고 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."** 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 표의 파일 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/ppalli-test-2026-11/puppet (13번은 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/ppalli-test-2026-11/images) 에 끌어다 놓고 Commit changes"

## 공통 화풍 (1~13번 프롬프트 맨 앞에 그대로 붙임)
```
STYLE: Korean paper-cut puppet theater (hanji papercraft), like a festival paper puppet show. Everything is made of flat layered colored paper with a visible fine hanji-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Palette: deep navy #1B2440, slate blue #3A4A6B, warm cream #F2E6CF, off-white #F7F3EA, charcoal #2B2B2B, office gray #8A8F98, muted light blue #A9C1D9, with small accents only of loss red #D92B2B, teal #1FA79A and signal yellow #F2C230. Flat side view, like a stage seen from the audience. ABSOLUTELY NO text, letters, numbers, logos, brand marks or watermarks anywhere — phone screens, papers, clipboards, banknotes, coins, certificates and monitors are blank, single-colored, or carry only simple meaningless lines.
```

## 주인공 (1~7번·13번 — 공통 화풍 다음에 그대로 붙임)
```
CHARACTER — "the Investor" (fictional, gender-neutral adult office worker; not resembling any real person or any existing cartoon character), the ONLY puppet with a face. NOT cute, NOT chibi, NOT a mascot, NOT a toy doll: realistic ADULT proportions — about 6.5 heads tall, a small slightly oval head, a visible neck, shoulders clearly wider than the head, long legs. Head and hands cut from off-white paper (#F7F3EA) with very light gray layer shadows, no hair; simple paper hands with a thumb (not round mittens). Clothes in flat paper layers: a plain gray office suit jacket (#8A8F98), dark navy trousers (#2E3A57), a white shirt and a narrow light-blue (#A9C1D9) necktie — the necktie is the Investor's recognizable mark in every scene. Face: small and restrained like an adult — two small dark navy almond-shaped eyes WITHOUT white highlights, thin straight navy eyebrows, a short simple nose line, and a thin navy mouth line whose shape shows the emotion; NO blush, NO pink cheeks, NO big round eyes, NO sweat drops or cartoon symbols. Emotion is shown by the eyebrows, the mouth and the posture (head angle, shoulders, hands), not by exaggerated cartoon features. Keep exactly the same head shape, body proportions, eyes, eyebrows, suit and necktie as the character reference sheet.
```

## 얼굴 없는 흰둥이 (8~10번·13번 — 공통 화풍 다음에(13번은 주인공 다음에) 그대로 붙임)
```
FIGURE — plain white paper human figures with the SAME realistic adult proportions as the Investor (about 6.5 heads tall, a small slightly oval head, a visible neck, long legs) — NOT cute, NOT chibi, NOT round-headed mascots. Head and hands cut from off-white paper (#F7F3EA) with only very light gray layer shadows; NO facial features at all (no eyes, eyebrows, nose, mouth, cheeks, ears or hair) and NO necktie; simple flat paper office clothes (a light-gray or slate-blue jacket and dark trousers, varied slightly between figures) unless the prompt says otherwise; simple paper hands. They must look clearly different from the Investor, who is the only figure with a face and the only one with a light-blue necktie.
```

## CUTOUT (2~10번 — 맨 마지막에 그대로 붙임)
```
CUTOUT: the described subject only, as an isolated paper puppet cutout on a fully transparent background (PNG with alpha channel) — no ground, no cast shadow on the ground, no scenery, no frame, no other objects or people. A thin cream (#F2E6CF) paper border about 6 px wide runs around the outer silhouette, like a hand-cut puppet. The WHOLE subject must be fully visible with generous empty margin: nothing may touch or cross the canvas edges — keep at least 8% empty transparent space on every side (left, right, top and bottom). If a transparent background is impossible, make the whole background one flat pure chroma green #00FF00 with no shading, and use no green at all on the subject.
```

## 1. HERO-SHEET — 주인공 인물 기준표
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/HERO-SHEET.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (영상에는 안 쓰고, 다른 그림의 기준)
```
Character reference sheet on a plain flat warm cream (#F2E6CF) paper background. Top row: the same Investor paper puppet standing in a relaxed neutral pose four times, evenly spaced with clear gaps — front view, three-quarter view, side view facing right, back view. Bottom row: four large head-and-shoulders close-ups of the same Investor, evenly spaced — calm slight smile, proud confident grin with the mouth open, shocked with eyes opened wider, eyebrows raised high and the mouth slightly open, worried despair with eyebrows tilted up in the middle and the mouth turned down. Same adult head, small eyes, thin eyebrows, gray suit and light-blue necktie in every view; no blush, no eye highlights. No labels, no text, no numbers.
```

## 2. HERO-PHONE — 서서 휴대전화를 두 손으로, 궁금한 얼굴 (오른쪽을 봄)
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/HERO-PHONE.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor standing, body in three-quarter view facing RIGHT, holding a smartphone in front of the chest with both hands, the blank back of the phone toward the viewer and its screen toward the Investor. Eyebrows raised, eyes fixed on the screen, a small curious open smile — interested and a little tempted. Full body.
```

## 3. HERO-THINK — 턱에 손, 고민하는 얼굴
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/HERO-THINK.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor standing, body in three-quarter view facing right, right hand raised to the chin, left arm folded across the body supporting the right elbow. Eyes glancing up to the side, eyebrows slightly knit, mouth a small straight line — thinking hard about which choice to make. Full body.
```

## 4. HERO-SHOCK — 휴대전화를 얼굴 앞에, 놀라 굳음
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/HERO-SHOCK.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor standing and leaning back, holding a smartphone close in front of the face with both hands (blank back of the phone toward the viewer, the face still visible above it), eyes opened wide, eyebrows shot up, mouth hanging slightly open, shoulders stiff — frozen in shock at a sudden loss. Full body.
```

## 5. HERO-DESPAIR — 바닥에 앉아 머리를 감싸 쥠
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/HERO-DESPAIR.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor sitting on the floor with knees pulled up, both hands holding the sides of the head, head bowed, eyes squeezed shut, eyebrows tilted up in the middle, mouth turned down, shoulders slumped — despair after a big loss. Full body, sitting.
```

## 6. HERO-PLAN — 빈 클립보드와 연필, 차분한 미소 (오른쪽을 봄)
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/HERO-PLAN.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor standing calm and upright, body in three-quarter view facing RIGHT, holding a clipboard in front of the body with its blank cream paper turned toward the viewer — the paper shows only four simple empty square boxes in a column, three of them with small teal check marks, no letters and no numbers — and a short pencil in the other hand. Relaxed eyebrows, eyes open and steady, a gentle confident smile — calm and prepared. Full body.
```

## 7. HERO-BOW — 허리 굽혀 인사
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/HERO-BOW.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
The Investor in side view facing left, bowing politely from the waist at about 45 degrees, both hands together in front of the body, eyes lowered, a polite slight smile — thanking the audience. Full body.
```

## 8. W-COLLEAGUE — 휴대전화를 내밀어 수익을 자랑하는 회사 동료 (왼쪽을 봄 · 어른 비율로 새로)
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/W-COLLEAGUE.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
One faceless white figure (a coworker in a light-gray office jacket and dark trousers) standing in three-quarter view facing LEFT, proudly stretching one arm forward to the left and holding up a smartphone with its blank screen facing left, the other hand on the hip, chest puffed out and head tilted back a little — showing off a profit. Full body.
```

## 9. W-FRIEND — 휴대전화를 내밀며 종목을 추천하는 지인 (왼쪽을 봄)
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/W-FRIEND.png`** — PNG 투명 700KB 이하 · 정사각 1024
```
One faceless white figure (an acquaintance, clearly not a coworker) in casual clothes — a slate-blue (#3A4A6B) zip-up jacket over a cream T-shirt and dark navy jeans, no necktie — standing in three-quarter view facing LEFT, leaning forward eagerly, one hand holding out a smartphone with its blank screen turned toward the left as if showing a tip, the other hand giving a thumbs-up — confidently recommending something. Full body.
```

## 10. W-CROWD — 모두 휴대전화를 들고 들뜬 무리 (왼쪽을 봄 · 어른 비율로 새로)
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/W-CROWD.png`** — PNG 투명 700KB 이하 · 가로 1536×1024
```
About eight faceless white figures standing in a loose cluster with small gaps, slightly overlapping, all facing LEFT, holding smartphones up in front of their chests and looking at them eagerly (phones blank), two of them raising a fist in excitement, varied heights, each with a slightly different light-gray or slate-blue jacket layer — everyone following the same hype. Full bodies, side by side like a crowd on a stage.
```

## 11. S-SUBWAY — 빈 무대: 지하철 객차 안
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/S-SUBWAY.jpg`** — JPEG 700KB 이하 · 가로 1536×1024
```
Empty stage backdrop: the inside of a generic city subway train car seen straight from the side — a long row of empty seats along the back wall under dark tunnel windows, metal poles and hanging hand straps, cool pale fluorescent light, slate-blue and gray paper layers. No route maps, no signs, no advertisements. The floor begins at about 70% of the picture height. The center of the stage is open and uncluttered (room for puppets). No people. No text, letters, numbers or logos anywhere.
```

## 12. S-CAFE — 빈 무대: 저녁 카페
**저장 경로: `stock/source/ppalli-test-2026-11/puppet/S-CAFE.jpg`** — JPEG 700KB 이하 · 가로 1536×1024
```
Empty stage backdrop: a small cozy café in the early evening seen straight from the front — a counter with a plain coffee machine and cups at the back left, a big window at the back right showing a dusky navy street with warm city lights, small round tables with chairs pushed to the far left and far right edges, warm pendant lamps. No menu boards with writing, no signs. The floor begins at about 70% of the picture height. The center of the stage is open and uncluttered (room for two puppets standing). No people. No text, letters, numbers or logos anywhere.
```

## 13. TH-ART — 썸네일 그림 (글자 없음)
**저장 경로: `stock/source/ppalli-test-2026-11/images/TH-ART.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (코드가 16:9 로 자르고 제목 2줄·말풍선을 얹음 — 위아래 80px 은 잘릴 수 있음)
```
Thumbnail illustration, landscape. Background: a deep navy (#1B2440) hanji paper backdrop with a large bold red (#D92B2B) paper zigzag line crashing down from the upper left to the lower right like a falling stock chart (no axes, no grid labels, no numbers). The Investor puppet with its face is shown from the knees up on the RIGHT third of the picture, the head at about 30–38% from the top of the picture: holding a smartphone low in the left hand with its blank back toward the viewer, the right hand covering the mouth; eyebrows tilted up and knit in the middle, worried eyes looking down at the phone, head slightly lowered, shoulders drooped — realizing that following the crowd lost almost all the money. Behind on the left, in dim shadow, a small crowd of five faceless white figures all raising their phones up excitedly toward the same direction (following the hype). Keep the bottom 35% of the picture and the area to the left of the Investor's head calm, dark and uncluttered navy (title text and speech bubbles will be added there later by code). The Investor's head, hands and the phone stay between 12% and 60% of the picture height; below 60% only the body and legs. The Investor's head, both hands and the phone must also stay fully inside the right vertical strip from 62.5% to 100% of the picture width, roughly centered in that strip (the strip may be cut out for a vertical 9:16 version) — do not let the head or hands cross to the left of 62.5% width. ABSOLUTELY NO text, letters, numbers or logos anywhere.
```

※ 연구·교육용 — 투자 권유가 아님.
