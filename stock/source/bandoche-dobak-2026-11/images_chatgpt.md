# bandoche-dobak-2026-11 롱폼 — 실사 사진 무대·움직임 그림 23장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.0 — 2026-11-14 — 사용자 지시 "썸네일 및 영상 관련 이미지들 생성 명령 알려줘 영상은 만스피 영상처럼 만들거고 카메라 워크도 대본 내용에 맞춰서 넣어야하니까 고려하고 그리고 만화 인물은 만들지말고 실제 사람 사진으로 할거야". 기준 대본 = `stock/source/bandoche-dobak-2026-11/bandoche-dobak-2026-11.txt` 대본 v8 (53문장) · 영상 「반도체 지금 사도 될까? 젠슨 황 퇴진 뒤 남은 리스크 3가지」.

**어떻게 쓰는가 — 만스피 편과 같은 코드 애니메이션, 그림만 실사 사진**
- Claude 가 코드로 만든다: 배경 사진(사람 없음) 위에 인물·손·소품 조각을 올리고, **동작마다 이어지는 사진 3장**(키 → 중간 → 키)을 바꿔 끼워 몸·손이 실제로 움직이게 한다. 그 위로 **카메라가 움직인다** (천천히 다가가기 · 옆으로 흐르기 · 위아래로 훑기 · 멀어지며 드러내기 — 대본 줄마다 정한 표는 `camera_plan.md`).
- 숫자·카드·주가 그래프·지도·자막은 코드가 얹는다 → **사진에는 글자·숫자·로고가 하나도 없어야 한다.**
- **실제 인물은 찍지 않는다** — 젠슨 황, 의혹의 여성, 정치인·경영자 누구도 사진으로 만들지 않는다 (닮은 사람도 ✗). 사람은 이 영상의 주인공 Y(평범한 한국 직장인) 한 사람뿐이고, **얼굴은 늘 보이지 않는다** (뒷모습·어깨 너머·손만 — 주식 채널 썸네일 규칙과 같음).
- 실제 회사 로고·제품 이름·색 조합(엔비디아·시게이트·화웨이·삼성·SK)을 닮게 만들지 않는다. 칩·하드디스크·상자는 상표 없는 일반 물건.
- 무대는 다른 편과 겹치지 않게 (주식 1~4편 썸네일: 아침 지하철 · 오후 카페 · 흐린 낮 책상 탑뷰 · 새벽 창가 역광 — 이 편은 밤 주차장 차 안 · 밤 소파 · 비 갠 저녁 창가) — 유튜브 '반복 콘텐츠' 정책.
- 썸네일 사진(21~23번)은 **사진만** — 문구는 Claude 가 코드로 얹는다 (`titles.md` 3안).
- ※ 연구·교육용 — 투자 권유가 아님. 수사·의혹은 보도 기준이고, 사진은 상황을 보여 주는 연출이다.

| 번호 | 저장 경로 (모두 `stock/source/bandoche-dobak-2026-11/` 아래) | 무엇 | 대본 줄 | 카메라 (자세히는 camera_plan.md) |
|---|---|---|---|---|
| 1 | `puppet/motion/Y-REF.webp` | Y 기준 사진 (뒷모습 · 4분의 3 뒤 · 옆 뒤) | 전체 | — |
| 2 | `puppet/motion/Y01.webp` | Y(의자에 앉아 뒤에서): 휴대전화를 들고 봄 → 어깨가 처지며 고개 숙임 → 손으로 뒷목을 주무름 | 1 · 43~45 | 모니터 쪽으로 다가가기 |
| 3 | `puppet/motion/Y02.webp` | Y(의자에 앉아 뒤에서): 모니터 쪽으로 몸을 기울여 읽음 → 등을 기대고 팔짱 → 턱에 손을 대고 끄덕임 | 2 · 34 · 49~50 | 옆으로 흐르기 · 멀어지기 |
| 4 | `puppet/motion/H01.webp` | 손(위에서): 검지가 휴대전화 화면 쪽으로 감 → 바로 위에서 멈춤 → 손을 거두어 주먹을 쥠 | 46~48 | 살짝 다가가기 |
| 5 | `puppet/BG-ROOM.jpg` | 밤 원룸 책상 · 모니터의 파란 하락 그래프 빛 · 창밖 도시 불빛 | 1~2 · 34 · 49~50 | 다가가기 · 옆으로 |
| 6 | `puppet/BG-DESKTOP.jpg` | 위에서 본 책상 · 가운데 휴대전화(파란 하락 막대) · 커피잔 · 수첩 | 46~48 | 위에서 살짝 다가가기 |
| 7 | `puppet/BG-CASINO.jpg` | 룰렛 테이블과 칩 더미 · 그 사이에 놓인 휴대전화(그래프 화면) | 3 · 43~45 | 휴대전화에서 물러나며 칩 드러내기 |
| 8 | `puppet/BG-STAGE.jpg` | 불 꺼진 발표 무대 · 조명 하나가 빈 의자를 비춤 | 4~5 · 29 | 천천히 다가가기 |
| 9 | `puppet/BG-PORT.jpg` | 밤 컨테이너 항구 · 크레인 · 쌓인 컨테이너 (글자 없음) | 6 · 9 · 19~20 · 36~37 | 옆으로 흐르기 · 물러나기 |
| 10 | `puppet/BG-SKYLINE.jpg` | 밤 싱가포르 마리나 베이 빌딩숲 · 물에 비친 불빛 (간판 글자 없음) | 7 · 25~28 | 빌딩 쪽으로 다가가기 · 옆으로 |
| 11 | `puppet/BG-EVIDENCE.jpg` | 수사실 · 벽의 빈 카드·빈 사진 틀을 잇는 빨간 실 · 책상 위 봉인 상자와 칩 보드 | 8 · 10 · 18 | 위에서 아래로 훑기 · 상자로 다가가기 |
| 12 | `puppet/BG-HDD.jpg` | 작업대 위에 쌓인 하드디스크 (상표 없음) · 옆에 빈 서류철과 의사봉 | 11~14 | 옆으로 흐르기 · 의사봉으로 다가가기 |
| 13 | `puppet/BG-MONITOR.jpg` | 어두운 거래 책상 · 큰 모니터 하나 (어두운 빈 화면 · 옅은 격자만) — 코드가 주가 그래프를 그림 | 15~17 | 화면으로 다가가기 |
| 14 | `puppet/BG-CAPITOL.jpg` | 해 질 녘 미국 국회의사당 · 빈 광장 | 21 | 아래에서 위로 올려 보기 |
| 15 | `puppet/BG-HEARING.jpg` | 빈 의회 청문회장 · 증인석 마이크·물잔 · 높은 의원석 (이름판 글자 없음) | 21 · 30 · 33 | 증인석을 따라 옆으로 |
| 16 | `puppet/BG-BOARDROOM.jpg` | 빈 이사회 회의실 · 긴 탁자 · 끝자리 의자만 빠져 있음 · 늦은 오후 빛 | 29~32 | 빈 의자로 다가가기 |
| 17 | `puppet/BG-FAB.jpg` | 반도체 클린룸 복도 · 노란 조명 · 장비 (사람 없음) | 38~39 | 복도 안으로 들어가기 |
| 18 | `puppet/BG-DATACENTER.jpg` | 데이터센터 서버 랙 통로 · 파란 불빛 | 35 · 40~42 | 통로 따라 앞으로 · 옆으로 |
| 19 | `puppet/BG-MORNING.jpg` | 아침 식탁 · 작은 바구니 여러 개에 나눠 담긴 달걀 · 커피 · 닫힌 노트북 | 51~53 | 바구니를 따라 옆으로 · 멈춤 |
| 20 | `puppet/motion/PROPS.webp` | 소품 8: AI 칩 보드 · HBM 메모리 칩 · 하드디스크 · 봉인 상자 · 자물쇠와 쇠사슬 · 칩(카지노) 더미 · 돋보기 · 빈 화면 휴대전화 | 9~10 · 12 · 18 · 39 · 45 | (조각 — 코드가 띄움) |
| 21 | `images/TH-PHOTO.jpg` | 썸네일 본안: 밤 주차장 차 안 · 뒷좌석에서 본 운전석 어깨 너머 · 휴대전화의 파란 하락 그래프 | 썸네일 · 0초 | — |
| 22 | `images/TH-PHOTO-B.jpg` | 썸네일 실험안 1: 밤 거실 소파 · 고개 떨군 뒷모습 · 앞 탁자의 휴대전화 파란 그래프 | 썸네일 | — |
| 23 | `images/TH-PHOTO-C.jpg` | 썸네일 실험안 2: 비 갠 저녁 창가 · 어깨 너머 노트북의 파란 하락 그래프 · 창밖 젖은 도시 | 썸네일 | — |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트(만화·종이 인형극·다른 편 실사 포함)가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
   **★ 이 편은 만화가 아니라 실사 사진이다.** 그림체 기준 그림은 없다 — 아래 '공통 사진 규칙'대로 실제 카메라로 찍은 사진처럼 만든다.
   **★ 이 편의 사람은 1번 Y-REF 가 기준이다 — 그 뒤 모든 사진의 Y 는 기준 사진과 머리 모양·옷·몸집·색이 똑같아야 한다.** 다르게 나오면 다시 만든다. 얼굴은 어느 사진에서도 보이지 않는다.
1. 아래 1~23번 **23장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 **공통 사진 규칙** 문단을 붙인다.
   - **기준 사진(1번)**: 공통 사진 규칙 → **인물** → **CUTOUT** → **기준 시트** → 프롬프트.
   - **동작 사진(2~4번)**: 공통 사진 규칙 → **인물** → **CUTOUT** → **MOTION STRIP** → 프롬프트.
   - **배경(5~19번)**: 공통 사진 규칙 → **배경판** → **카메라 여유** → 프롬프트.
   - **소품(20번)**: 공통 사진 규칙 → **CUTOUT** → 프롬프트.
   - **썸네일 사진(21~23번)**: 공통 사진 규칙 → **인물** → **썸네일** → 프롬프트.
3. **동작 사진은 한 장에 같은 사람(또는 같은 손)을 3번** 찍은 것처럼 만든다 — 왼쪽 → 가운데 → 오른쪽이 **한 동작을 이어 찍은 3장**(연속 사진)이다. 세 장이 **같은 크기·같은 자리·같은 방향·같은 옷·같은 빛**이고, **의자 다리(손은 손목 끝)가 같은 높이**에 있고, 바뀌는 것은 몸·팔·고개·손의 자세뿐이다. 세 칸 사이는 비워 둔다.
4. **검사 (기준·동작·소품 필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`·`칸 넘음`·`아래 끝 높이 다름`이면 고쳐서 다시 만든다 (더 작게 · 여백을 넓게 · 의자 다리나 손목을 같은 선에). **투명이 아니면 배경을 순자홍 #FF00FF 한 색 평면으로 다시 만든다.**
   ```python
   from PIL import Image
   import numpy as np
   def filled_mask(a):
       if a[2, 2, 3] > 0:                        # 투명이 아니면 순자홍 바탕을 빈 곳으로 봄
           r, g, b = (a[:, :, i].astype(int) for i in range(3))
           return ~((r > 200) & (b > 200) & (g < 90))
       return a[:, :, 3] > 40
   def check(path, cols, rows=1, margin=0.04, gap=0.012, feet=None):
       a = np.array(Image.open(path).convert("RGBA"))
       h, w = a.shape[:2]
       m = filled_mask(a)
       ys, xs = np.where(m)
       box = (xs.min() / w, ys.min() / h, xs.max() / w, ys.max() / h)
       bad = []
       if not (box[0] >= margin and box[1] >= margin and box[2] <= 1 - margin and box[3] <= 1 - margin):
           bad.append("잘림")
       for c in range(1, cols):                  # 칸 경계 둘레는 비어 있어야 함
           x = int(w * c / cols); d = int(w * gap)
           if m[:, x - d:x + d].any(): bad.append(f"칸 넘음 세로 {c}")
       for r in range(1, rows):
           y = int(h * r / rows); d = int(h * gap)
           if m[y - d:y + d, :].any(): bad.append(f"칸 넘음 가로 {r}")
       if feet:                                  # 동작 사진: 세 장의 아래 끝(의자 다리·손목)이 같아야 함
           bottoms = []
           for c in range(cols):
               ys_c = np.where(m[:, w * c // cols:w * (c + 1) // cols].any(axis=1))[0]
               bottoms.append(ys_c.max() / h)
           if max(bottoms) - min(bottoms) > 0.02: bad.append(f"아래 끝 높이 다름 {[round(v, 3) for v in bottoms]}")
       print(path, "OK" if not bad else f"다시 — {bad}", [round(float(v), 3) for v in box])
       return not bad
   # 기준·동작 사진: check(경로, cols=3, feet=True) · 소품 판: check(경로, cols=4, rows=2, margin=0.02)
   ```
5. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 화면·휴대전화·간판·서류·상자·컨테이너·칩·옷에도 없음 (빈 판·단순한 선·도형만). 화면의 주가 그래프는 **글자 없는 막대·선 모양만**, 색은 한국 주식 앱처럼 **오르면 빨강 · 내리면 파랑**. 실제 회사 로고·제품 모양·색 조합을 닮게 만들지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.
   **실제 인물은 만들지 않는다** — 유명인·경영자·정치인·뉴스 속 인물과 닮은 사람도 ✗. Y 의 얼굴은 어느 사진에서도 보이지 않는다 (뒷모습·어깨 너머·손만). 과장하지 않는다 — 우는 얼굴·돈을 태우는 장면·피·폭발 ✗, 실제 일처럼 차분하게.
6. 사진 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. stock/source/bandoche-dobak-2026-11/puppet/motion/Y-REF.webp`). 사진 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈·확장자까지 같게 — 배경은 `stock/source/bandoche-dobak-2026-11/puppet/`, 기준·동작·소품은 `stock/source/bandoche-dobak-2026-11/puppet/motion/`, 썸네일 사진은 `stock/source/bandoche-dobak-2026-11/images/`).
   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     - 배경·썸네일(JPEG): RGB · 크기 1536×1024 그대로 (자르지 않음 — 카메라가 그 안에서 움직임) · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.
     - 기준·동작·소품(**WebP, 투명 유지** — 실사 사진은 PNG 로는 700KB 를 넘고, 256색으로 줄이면 사진이 뭉개짐): 아래 코드 그대로.
       ```python
       from PIL import Image
       import os
       def save_webp(src, dst, limit=700_000):
           im = Image.open(src).convert("RGBA")
           w, h = im.size
           s, q = min(1.0, 1536 / max(w, h)), 90
           while True:
               cur = im.resize((round(w * s), round(h * s)), Image.LANCZOS) if s < 1 else im
               cur.save(dst, "WEBP", quality=q, method=6)            # 투명(알파) 그대로
               if os.path.getsize(dst) <= limit or q <= 60 and max(cur.size) <= 1000:
                   break
               if q > 60: q -= 5
               else: s *= 0.9
           print(dst, os.path.getsize(dst), cur.size, q)
       ```
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[stock] bandoche-dobak-2026-11 <파일 이름> 이미지` (예: `[stock] bandoche-dobak-2026-11 Y-REF.webp 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 사진을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 공통 사진 규칙 (1~23번 모든 프롬프트 맨 앞에 그대로 붙임)

```
PHOTO STYLE: a photorealistic documentary-style photograph that looks like it was really taken with a full-frame camera (35mm or 50mm lens, natural perspective), natural realistic light and color, real textures of skin, fabric, metal, glass and paper, gentle film-like grain. Calm, honest, everyday mood — like a news feature photo, not an advertisement: no exaggeration, no dramatic movie lighting, no fake HDR glow. It is a real photo — not a cartoon, not an illustration, not a painting, not a 3D render. People: only the ordinary anonymous person described below; never show anyone's face (seen from behind, over the shoulder, or hands only); never depict or resemble any real, famous or identifiable person (no business leader, politician, celebrity or person from the news). Absolutely no text, letters, numbers, logos, brand marks or watermarks anywhere — screens, phones, signs, papers, boxes, containers, chips and clothes are blank or show only simple shapes; any stock chart on a screen is only bars and lines without labels, colored like a Korean stock app (rising = red, falling = blue). No crying, no burning money, no blood, no explosions.
```

## 배경판 (5~19번 — 공통 사진 규칙 다음에 그대로 붙임)

```
BACKGROUND PLATE for a photo-based 2D animation: full-bleed landscape photo 1536x1024, NO people and no animals anywhere (unless the prompt says so). Keep the middle of the picture calm and uncluttered so that cutout photos, cards and numbers can be placed on it later.
```

## 카메라 여유 (5~19번 — 배경판 다음에 그대로 붙임)

```
CAMERA ROOM: this photo will be shown through a moving 16:9 video window (slow push-in up to 120%, slow sideways pans up to 10% of the width, gentle tilts that use the extra height). Keep the main subject named in the prompt inside the central 60% of the width and the middle 70% of the height, continue the scene naturally and with real detail all the way to every edge (no empty borders, no vignette, no frame), and keep everything in sharp focus from front to back (deep focus, about f/8) — no lens blur, no bokeh, no motion blur, so the picture stays sharp when the camera moves closer.
```

## 인물 (1~4번 · 21~23번 — 공통 사진 규칙 다음에 그대로 붙임)

```
PERSON — Y, the main person ('you' in this video), exactly the same in every picture (match picture 1): an ordinary Korean office worker in his early 30s, slim average build, short neat black hair with a slightly longer top, a plain charcoal-gray crewneck knit sweater over a white T-shirt collar, dark navy jeans, a simple black wristwatch on the left wrist, no rings. His face is NEVER visible — always seen from behind, from behind over the shoulder, or only his hands. Natural, tired after-work posture; worry is shown only by the shoulders, head and hands.
```

## CUTOUT (1~4번 · 20번 — 그다음에 그대로 붙임 · 배경·썸네일에는 붙이지 않음)

```
CUTOUT: only the described subjects, as isolated photographic cutouts on a fully transparent background (alpha channel) — no floor, no cast shadow, no scenery, no frame, no other objects or people. Clean, natural photo edges (no outline, no white halo). Every subject must be fully visible with empty margin: nothing may touch or cross the canvas edges — keep at least 5% empty transparent space on every side. If a transparent background is impossible, make the whole background one flat pure magenta #FF00FF with no shading, and use no magenta, purple or hot pink at all on the subjects.
```

## 기준 시트 (1번 — CUTOUT 다음에 그대로 붙임)

```
REFERENCE SHEET: landscape 1536x1024, the same person three times side by side, standing straight, full body from head to shoes, the same size, feet on the same level, evenly spaced with clear empty space between them: left = seen straight from behind; middle = three-quarter view from behind (head turned away, face not visible); right = side view from slightly behind (face hidden by the angle). Neutral standing pose, arms relaxed, holding a smartphone in the right hand with its screen dark.
```

## MOTION STRIP (2~4번 — CUTOUT 다음에 그대로 붙임)

```
MOTION STRIP: landscape 1536x1024 — three photos of one continuous movement, shot from exactly the same camera position like a burst of three frames: left = start pose, middle = in-between pose, right = end pose. The same person (or hand), same size, same place, same direction, same clothes and same light in all three; the lowest point (chair legs, or the wrist for a hand) on the same level in all three; only the body, arms, head and hands change. Leave clear empty space between the three frames so they never touch.
```

## 썸네일 (21~23번 — 인물 다음에 그대로 붙임)

```
THUMBNAIL PHOTO: full-bleed landscape photo 1536x1024, used as a YouTube thumbnail (the 16:9 middle band 1536x864 is shown). Put Y's head and the phone or laptop screen inside the horizontal band from 38% to 66% of the width and between 15% and 85% of the height (it will also be cropped to a square and a 4:5 shape). Leave the lower 30% of the picture calm and darker (no bright objects, no busy detail) for two lines of large text added later, and a calm empty area beside Y's head for a small speech label — the label must not cover the person. Real place, real light, not exaggerated. No text anywhere.
```

---

### 1. Y-REF — Y 기준 사진
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/motion/Y-REF.webp`** — WebP 700KB 이하 · 투명 · 가로 1536×1024 · 기준 3면
```
Reference photo sheet of Y as described in PERSON: shot in a soft, even studio light, realistic.
```

### 2. Y01 — 휴대전화를 보다 고개를 떨굼 (대본 1 · 43~45)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/motion/Y01.webp`** — WebP · 투명 · 동작 3장
```
Y seen straight from behind, sitting on a plain black mesh office chair (the chair is part of the cutout, seen from behind, its wheels at the bottom), at desk height, lit by a cool blue screen glow from the front and a little warm lamp light from the left. Left frame: he holds his smartphone up in both hands in front of his face, back straight, looking at it. Middle frame: his shoulders drop and his head lowers, the phone sinking to chest height. Right frame: the phone rests in his left hand on his lap and his right hand rubs the back of his neck, head still lowered.
```

### 3. Y02 — 기사를 읽다 팔짱 끼고 생각 (대본 2 · 34 · 49~50)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/motion/Y02.webp`** — WebP · 투명 · 동작 3장
```
Y seen from behind and slightly to the right, sitting on the same plain black mesh office chair (part of the cutout), lit by a cool blue screen glow from the front and warm lamp light from the left. Left frame: he leans forward toward an unseen screen, forearms on his knees, reading closely. Middle frame: he leans back in the chair and crosses his arms. Right frame: still leaning back, he rests his chin on his right hand and gives a small nod, calm and thoughtful.
```

### 4. H01 — 사려다 멈추고 손을 거둠 (대본 46~48)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/motion/H01.webp`** — WebP · 투명 · 동작 3장
```
Only Y's right hand and forearm in the charcoal knit sleeve (no watch on this wrist — his watch is on the other wrist), seen from directly above as if the camera looks down at a desk, the arm entering from the bottom of each frame, soft warm desk-lamp light. Left frame: the index finger reaches forward and down, about to tap something. Middle frame: the finger stops in mid-air, hovering, the hand frozen. Right frame: the hand pulls back a little and closes into a relaxed fist. The wrist end is at the same bottom level in all three frames.
```

### 5. BG-ROOM — 밤 원룸 책상 (대본 1~2 · 34 · 49~50)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-ROOM.jpg`** — JPEG 700KB 이하 · 가로 1536×1024
```
A small, tidy Korean studio apartment at night, eye-level camera from behind where a person would sit. A plain wooden desk against the far wall in the center with one computer monitor whose screen shows only a simple stock chart of blue falling bars and a thin line (no labels), a small warm desk lamp on the left, a closed notebook and a mug. A window to the right shows soft city lights of apartment towers at night. In front of the desk, the center-bottom area is an empty floor and empty space where a seated person seen from behind will be placed later (his chair would stand there, head at about 45% of the picture height). Main subject for the camera: the monitor.
```

### 6. BG-DESKTOP — 위에서 본 책상과 휴대전화 (대본 46~48)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-DESKTOP.jpg`** — JPEG · 가로 1536×1024
```
Top-down photo looking straight down at a wooden desk at night under warm lamp light. In the exact center a black smartphone lies flat, its screen on, showing only a simple stock chart: blue falling candle bars and a thin line, plus one plain rounded empty button shape near the bottom of the screen (no text in it). Around it, at the edges: a white coffee mug, a closed dark notebook, a pen. The lower-center part of the desk below the phone is clear and empty (a hand will reach in from the bottom later). Main subject for the camera: the phone screen.
```

### 7. BG-CASINO — 룰렛과 칩 사이의 휴대전화 (대본 3 · 43~45)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-CASINO.jpg`** — JPEG · 가로 1536×1024
```
A close, slightly high-angle photo of a green felt casino roulette table in a dim room: a roulette wheel at the upper right, neat stacks of plain casino chips in red, blue and black (no numbers or letters on them) in the middle. In the center, lying flat among the chip stacks, a black smartphone with its screen on, showing only a simple stock chart of red and blue bars without labels. Warm, low light, realistic, no people, no hands. Main subject for the camera: the phone among the chips (the camera starts close on the phone and slowly pulls back to reveal the table).
```

### 8. BG-STAGE — 빈 발표 무대 (대본 4~5 · 29)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-STAGE.jpg`** — JPEG · 가로 1536×1024
```
A large dark conference keynote stage seen from the middle of an empty audience hall, eye level. On the stage, a single soft spotlight lights one empty modern stool in the center; the huge screen behind it is dark and blank. Rows of empty seats in the dark foreground at the bottom edge. Quiet, empty, after the event. No logos, no text, no people. Main subject for the camera: the empty stool in the spotlight.
```

### 9. BG-PORT — 밤 컨테이너 항구 (대본 6 · 9 · 19~20 · 36~37)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-PORT.jpg`** — JPEG · 가로 1536×1024
```
A large Asian container port at night, seen from a slightly raised position: tall ship-to-shore cranes with orange work lights, long rows of stacked shipping containers in muted blue, gray and rust colors (completely plain — no company names, no numbers, no logos), wet asphalt reflecting the lights, a dark calm sea and a distant city skyline glow. No people, no vehicles moving. Main subject for the camera: the stacked containers under the cranes in the center.
```

### 10. BG-SKYLINE — 밤 싱가포르 마리나 베이 (대본 7 · 25~28)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-SKYLINE.jpg`** — JPEG · 가로 1536×1024
```
The Marina Bay financial district skyline in Singapore at night seen across the calm bay water, glass office towers with lit windows, their reflections on the water, a deep blue night sky. The buildings carry no readable signs, names or logos. No people, no boats in the foreground. Main subject for the camera: the cluster of office towers in the center.
```

### 11. BG-EVIDENCE — 수사실 (대본 8 · 10 · 18)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-EVIDENCE.jpg`** — JPEG · 가로 1536×1024
```
A quiet investigation room at night, eye level. On the back wall, a large cork board with blank white index cards and empty photo frames (no faces, no images, no writing) pinned up and connected by red string, lit by one hanging lamp. In front, a gray metal table with three sealed plain cardboard boxes, one opened box showing a stack of generic black computer accelerator boards with metal heat sinks (no brand), and a flashlight. No people. Main subjects for the camera: the cork board (top) and the opened box (center); the camera will tilt from the board down to the box.
```

### 12. BG-HDD — 하드디스크와 의사봉 (대본 11~14)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-HDD.jpg`** — JPEG · 가로 1536×1024
```
A long workbench under cool office light, eye level: neat stacks of many identical bare 3.5-inch hard disk drives with plain silver tops (no labels, no stickers, no text) running from left to center. On the right side of the bench, a closed plain manila document folder and a dark wooden gavel resting on its sound block. No people. Main subjects for the camera: the hard drive stacks (the camera pans across them) and then the gavel.
```

### 13. BG-MONITOR — 어두운 화면 하나 (대본 15~17 · 코드가 주가 그래프를 그림)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-MONITOR.jpg`** — JPEG · 가로 1536×1024
```
A dark trading desk at night, eye level, straight-on: one large widescreen monitor in the center fills about half of the picture width, its screen dark charcoal with only a very faint thin grid (no chart, no text — a chart will be drawn on it later), a keyboard and a mouse in front, a second smaller monitor turned off at the left edge. Dim room, cool light from the screen. The monitor is perfectly front-facing (not angled). No people. Main subject for the camera: the monitor screen.
```

### 14. BG-CAPITOL — 해 질 녘 미국 국회의사당 (대본 21)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-CAPITOL.jpg`** — JPEG · 가로 1536×1024
```
The United States Capitol building in Washington at dusk, seen from the front at a respectful distance across an empty plaza, soft warm lights on the white dome, a deep blue evening sky. Realistic architecture photo. No people, no cars, no signs. Main subject for the camera: the dome (the camera will tilt up from the steps to the dome).
```

### 15. BG-HEARING — 빈 청문회장 (대본 21 · 30 · 33)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-HEARING.jpg`** — JPEG · 가로 1536×1024
```
An empty formal government hearing room, eye level from the back of the room: a long witness table in the middle with several black microphones and glasses of water, empty chairs; behind and above it a raised curved wooden dais with empty leather chairs for committee members. Wood paneling, soft official lighting. No nameplates with text, no flags, no seals, no people. Main subject for the camera: the witness table (the camera slides sideways along it).
```

### 16. BG-BOARDROOM — 빈 이사회 회의실 (대본 29~32)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-BOARDROOM.jpg`** — JPEG · 가로 1536×1024
```
An empty corporate boardroom in late afternoon, eye level from the far end of a long dark wooden table: leather chairs neatly tucked in along both sides, and at the head of the table one larger chair pulled back and left empty, slightly turned. Tall windows with soft golden light, a dark blank screen on the wall. No people, no logos, no papers with text. Main subject for the camera: the empty head chair.
```

### 17. BG-FAB — 반도체 클린룸 복도 (대본 38~39)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-FAB.jpg`** — JPEG · 가로 1536×1024
```
A long semiconductor cleanroom corridor in yellow-filtered light, eye level, one-point perspective: rows of large white wafer-processing machines on both sides, overhead rails, a shiny gray floor. No people, no logos, no signs. Main subject for the camera: the far end of the corridor in the center (the camera moves forward into it).
```

### 18. BG-DATACENTER — 데이터센터 통로 (대본 35 · 40~42)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-DATACENTER.jpg`** — JPEG · 가로 1536×1024
```
A long data center aisle between tall black server racks with small blue and white status lights, eye level, one-point perspective, cool clean light, a perforated floor. No people, no logos, no screens with text. Main subject for the camera: the center of the aisle (the camera moves forward along it).
```

### 19. BG-MORNING — 아침 식탁의 나눠 담은 달걀 (대본 51~53)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/BG-MORNING.jpg`** — JPEG · 가로 1536×1024
```
A calm morning kitchen table by a window, soft natural daylight, eye level slightly from above: five small woven baskets in a gentle row across the middle, each holding two or three brown eggs (the eggs are spread across the baskets, not in one basket), a cup of coffee, a closed laptop, a small plant. Fresh, quiet, hopeful mood. No people, no text. Main subject for the camera: the row of baskets (the camera slides along it).
```

### 20. PROPS — 소품 8 (대본 9~10 · 12 · 18 · 39 · 45)
**저장 경로: `stock/source/bandoche-dobak-2026-11/puppet/motion/PROPS.webp`** — WebP · 투명 · 4×2 칸
```
Eight separate photographic product-style objects in a 4 columns x 2 rows grid, each centered in its own cell with clear empty space around it, the same soft studio light, landscape 1536x1024. Top row, left to right: (1) a generic AI computer accelerator board with a large metal heat sink and fan, black and silver, no brand; (2) a single high-bandwidth memory chip package shown at a slight angle so you can see several thin layers stacked on top of each other on a small green substrate; (3) a bare 3.5-inch hard disk drive with a plain silver top; (4) a sealed plain brown cardboard shipping box with clear tape. Bottom row: (5) a heavy steel padlock with a short loop of chain; (6) a neat stack of plain red, blue and black casino chips with no numbers; (7) a classic magnifying glass with a black handle; (8) a black smartphone standing upright, screen completely dark. No text, numbers or logos on anything.
```

### 21. TH-PHOTO — 썸네일 본안: 밤 주차장 차 안
**저장 경로: `stock/source/bandoche-dobak-2026-11/images/TH-PHOTO.jpg`** — JPEG 700KB 이하 · 가로 1536×1024
```
Night, inside a parked car in a dim underground parking garage. The camera is in the back seat looking over Y's right shoulder: Y sits in the driver's seat, head slightly lowered, holding his smartphone low on the steering wheel; the phone screen shows only a simple stock chart of long blue falling bars and a thin falling line (no text). The blue screen light falls on his hands and the steering wheel; the garage outside the windshield has cold fluorescent lights and empty parking spaces. His face is not visible. Quiet, heavy, realistic mood, not exaggerated.
```

### 22. TH-PHOTO-B — 썸네일 실험안 1: 밤 거실 소파
**저장 경로: `stock/source/bandoche-dobak-2026-11/images/TH-PHOTO-B.jpg`** — JPEG 700KB 이하 · 가로 1536×1024
```
Night, a small Korean apartment living room lit only by a floor lamp. Y is seen from behind, sitting on a gray sofa, leaning forward with his elbows on his knees and his head down, hands loosely joined. On the low coffee table in front of him a smartphone lies face up, its screen showing only blue falling bars (no text). A dark TV on the wall is switched off. His face is not visible. Calm, tired, realistic mood.
```

### 23. TH-PHOTO-C — 썸네일 실험안 2: 비 갠 저녁 창가
**저장 경로: `stock/source/bandoche-dobak-2026-11/images/TH-PHOTO-C.jpg`** — JPEG 700KB 이하 · 가로 1536×1024
```
Early evening just after rain, by a large apartment window high above a city with wet streets and soft blue-gray light. Over-the-shoulder view from behind Y, who sits at a small table by the window with a laptop open; the laptop screen shows only a simple stock chart with a sharp blue drop and a thin line (no text). Raindrops on the window glass, the city lights starting to come on. His face is not visible (seen from behind, head turned toward the screen). Quiet, thoughtful, realistic mood.
```
