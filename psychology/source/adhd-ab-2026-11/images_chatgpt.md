# adhd-ab-2026-11 — 일상툰 그림 41장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.0 — 2026-11-23 — 사용자 지시 "그럼 모든 이미지 생성 명령 알려줘 지시사항은 저장소에서 읽으라하고 업로드하라고해" · "썸네일 이미지도 만들어 A, B 사람 반반 나눠서 대비되도록". 기준 대본 = `psychology/source/adhd-ab-2026-11/대본_초안.txt` v1.0 · 영상 「ADHD 알고 치료한 A씨 vs 모르고 산 B씨」.

**어떻게 쓰는가 — 일상툰 꼴 코드 애니메이션**
- Claude 가 코드로 만든다: 배경 그림 위에 인물·소품 조각을 올리고, 동작마다 이어지는 원화 3장(키 → 중간 → 키)을 바꿔 끼워 움직이게 한다. 화면 반반(왼쪽 A · 오른쪽 B)·말풍선·자막·시계 바늘·그래프는 코드가 얹는다 → **그림에는 글자가 하나도 없어야 한다.**
- **그림체 기준 = 1번 A-REF** — 이 편은 바깥 기준 그림이 없다. 1번이 정한 그림체를 2번부터 모두 똑같이 따른다. 사람 기준 = 1번 A-REF · 2번 B-REF · 3번 W-POSES · 4번 T-POSES · 5번 D-POSES · 6번 S-POSES · 7번 K-POSES · 8번 F-POSES.
- 썸네일 그림(마지막 장)은 **A·B 반반 대비** 그림만 — 문구 (제목이 정해지면 Claude 가 코드로 얹음 — 아래 35% 어두운 띠).
- A·B 는 가상 인물. ※ 연구·교육용 영상 — 의학적 진단·처방이 아니다. 누구도 나쁜 사람으로 그리지 않는다.

| 번호 | 저장 경로 (모두 `psychology/source/adhd-ab-2026-11/` 아래) | 무엇 | 대본 |
|---|---|---|---|
| 1 | `puppet/motion/A-REF.png` | A 기준 그림 (앞 · 4분의 3 · 옆) — 이 편 그림체 기준 | 전체 |
| 2 | `puppet/motion/B-REF.png` | B 기준 그림 (앞 · 4분의 3 · 옆) | 전체 |
| 3 | `puppet/motion/W-POSES.png` | 아내 자세 3: 따짐 · 빈손을 가리킴 · 베란다 통화 | 4장 |
| 4 | `puppet/motion/T-POSES.png` | 팀장 자세 3: 회의 중 '듣고 있어요?' · 서류 읽기 · 엄지 척 | 3장 |
| 5 | `puppet/motion/D-POSES.png` | A씨 주치의 자세 3: 질문 · 기록부 보기 · 끄덕임 (앉은 자세) | 2장 |
| 6 | `puppet/motion/S-POSES.png` | 아들 자세 3 (앉은 자세): 손 꼼지락 · 아빠 쳐다봄 · 수줍은 웃음 | 마무리 |
| 7 | `puppet/motion/K-POSES.png` | 소아청소년과 의사 자세 3 (앉은 자세): 설명 · 아버지에게 질문 · 따뜻한 미소 | 마무리 |
| 8 | `puppet/motion/F-POSES.png` | 친구 자세 3 (술집, 앉은 자세): 휴대폰 보여 주기 · 크게 웃기 · 잔 들기 | 6장 |
| 9 | `puppet/BG-OFFICE.jpg` | A씨 사무실 자리 (낮) — 1장 · 3장 | 1장 · 3장 |
| 10 | `puppet/BG-B-LIVING.jpg` | B씨 집 거실 (저녁) — 1장 · 2장(밤은 코드로 어둡게) · 4장 | 1장 · 2장 · 4장 |
| 11 | `puppet/BG-A-BED.jpg` | A씨 원룸 침실 (새벽 3시) | 1장 · 2장 |
| 12 | `puppet/BG-CLINIC.jpg` | A씨가 간 정신건강의학과 진료실 | 2장 |
| 13 | `puppet/BG-RESTROOM.jpg` | 회사 화장실 세면대 | 3장 |
| 14 | `puppet/BG-MEETING.jpg` | 회사 회의실 | 3장 |
| 15 | `puppet/BG-B-ROOM.jpg` | B씨 침실 (밤) — 다툰 뒤 혼자 | 4장 |
| 16 | `puppet/BG-VERANDA.jpg` | 아파트 베란다 (저녁) | 4장 |
| 17 | `puppet/BG-B-OFFICE.jpg` | B씨 회사 — 왼쪽 책상 · 오른쪽 빈 게시판 | 4장 |
| 18 | `puppet/BG-PUB.jpg` | 동네 술집 테이블 (밤) | 6장 |
| 19 | `puppet/BG-PEDS.jpg` | 소아청소년 정신건강의학과 진료실 | 마무리 |
| 20 | `puppet/BG-RECEPTION.jpg` | 병원 접수대 | 마무리 |
| 21 | `puppet/motion/A01.png` | A: 모니터 보며 한숨 → 휴대폰을 들고 멍함 → 시계를 보고 화들짝 (땀방울) | 1장 |
| 22 | `puppet/motion/A02.png` | A: (침대에 앉아) 드라마에 빠져 키득 → 화면에 몰입 → 하품하면서도 다음 편 누름 | 1장 |
| 23 | `puppet/motion/A03.png` | A: (밤, 침대) 영상을 진지하게 봄 → 입을 가리며 '내 얘기네' → 결심한 얼굴로 화면을 누름 | 2장 |
| 24 | `puppet/motion/A04.png` | A: (진료실 의자) 긴장해 듣기 → 빈 기록부를 펼쳐 보여 줌 → 안도하며 가슴에 손 | 2장 |
| 25 | `puppet/motion/A05.png` | A: (사무실) 집중해 타자 → 마우스 클릭 → 놀라 멍하니 굳음 | 3장 |
| 26 | `puppet/motion/A06.png` | A: (세면대 앞에 서서) 눈물을 참음 → 눈물을 손등으로 닦음 → 슬프게 옅은 미소 | 3장 |
| 27 | `puppet/motion/A07.png` | A: (회의 중) 멍하니 허공 → 불리자 화들짝 → 이마를 짚으며 '아침 약…' | 3장 |
| 28 | `puppet/motion/A08.png` | A: (1년 뒤) 휴대폰을 서랍에 넣음 → 차분히 일함 → 기대앉아 만족한 미소 | 3장 |
| 29 | `puppet/motion/B01.png` | B: (거실 소파) 고지서를 보며 인상 → 고지서를 놓고 휴대폰에 멍함 → 시계를 보고 화들짝 | 1장 |
| 30 | `puppet/motion/B02.png` | B: (밤, 소파) 낚시 영상에 신나 주먹 → 화면에 몰입 → 하품하면서도 계속 봄 | 1장 |
| 31 | `puppet/motion/B03.png` | B: (밤, 소파) 영상을 진지하게 봄 → 불편하게 인상 → 손을 내저으며 화면을 끔 | 2장 |
| 32 | `puppet/motion/B04.png` | B: (거실에 서서) 손바닥을 들어 방어 → 답답해 소리침 → 등을 돌려 방으로 감 | 4장 |
| 33 | `puppet/motion/B05.png` | B: (침대 끝에 앉아) 두 손으로 머리를 감쌈 → 한숨 쉬며 바닥을 봄 → 얼굴을 쓸어내림 | 4장 |
| 34 | `puppet/motion/B06.png` | B: (회사 책상) 화면을 읽음 → 충격에 굳음 → 눈을 감고 이마를 짚음 | 4장 |
| 35 | `puppet/motion/B07.png` | B: (게시판 앞에 서서) 기대하며 훑어봄 → 실망 → 어깨가 처지고 고개 숙임 | 4장 |
| 36 | `puppet/motion/B08.png` | B: (술집에 앉아) 내민 휴대폰을 봄 → 따라 웃음 → 어색하게 잔을 듦 | 6장 |
| 37 | `puppet/motion/B09.png` | B: (진료실 의자) 진지하게 듣기 → 자기를 가리키며 '저요?' → 턱을 괴고 생각 | 마무리 |
| 38 | `puppet/motion/B10.png` | B: (접수대 앞에 서서) 머뭇거리며 뒷목을 만짐 → 손을 살짝 들고 물음 → 어색하지만 희망찬 미소 | 마무리 |
| 39 | `puppet/motion/PROPS-A.png` | 소품 4: 휴대폰 · 고지서 · 요일 약통과 물컵 · 바늘 없는 벽시계 | 1장 · 3장 |
| 40 | `puppet/motion/PROPS-B.png` | 소품 4: 세탁소 비닐 속 양복 · 생활기록부 · 재생 버튼 화면 · 빈 달력 | 2장 · 4장 |
| 41 | `images/TH-CHAR.jpg` | 썸네일 그림: 왼쪽 A(환한 낮 · 일을 끝내고 안도) | 오른쪽 B(어두운 밤 · 머리를 감쌈) 반반 대비 | 썸네일 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
   **★ 1번 A-REF 가 이 편 그림체의 기준이다 — 2번부터 모든 그림은 1번과 같은 사람이 그린 것처럼 (선 굵기·색·얼굴 꼴·약 3등신 비율).** 사람은 1번 A-REF · 2번 B-REF · 3번 W-POSES · 4번 T-POSES · 5번 D-POSES · 6번 S-POSES · 7번 K-POSES · 8번 F-POSES 이 기준 — 그 뒤 같은 사람은 얼굴·머리·옷·색·비율이 똑같아야 한다. 다르게 나오면 다시 만든다.
1. 아래 1~41번 **41장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 앞에 아래 블록을 이 순서로 붙인다.
   - **기준 그림(1, 2번)**: 공통 화풍 → 인물 → CUTOUT → 기준 시트 → 프롬프트.
   - **조연 자세 그림(3, 4, 5, 6, 7, 8번)**: 공통 화풍 → 인물 → CUTOUT → 자세 시트 → 프롬프트.
   - **배경(12, 13, 14, 15, 16, 17, 18, 19, 20번)**: 공통 화풍 → 배경판 → 프롬프트.
   - **반반 화면 배경(9, 10, 11번)**: 공통 화풍 → 배경판 → 반반 화면 → 프롬프트.
   - **동작 그림(21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38번)**: 공통 화풍 → 인물 → CUTOUT → MOTION STRIP → 프롬프트.
   - **소품(39, 40번)**: 공통 화풍 → CUTOUT → 프롬프트.
   - **썸네일 그림(41번)**: 공통 화풍 → 인물 → 썸네일 → 프롬프트.
3. **동작 그림은 한 장에 같은 사람을 3번** 그린다 — 왼쪽 → 가운데 → 오른쪽이 **한 동작을 이어 그린 3장**(애니메이션 원화)이다. 같은 크기·같은 자리·같은 방향·같은 옷, **발바닥(앉은 자세는 의자·소파 자리)이 같은 높이**, **움직이는 부분(팔·손·머리·얼굴·상체)만** 바뀐다. **자세 그림(POSES)** 은 이어지는 동작이 아니라 서로 다른 자세 3개 — 그래도 크기·발 높이·옷은 같다. 서로 겹치거나 칸(가로 3등분)을 넘지 않는다. 다른 사람·배경·바닥 그림자는 없다.
4. **검사 (기준·자세·동작·소품 필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`·`칸 넘음`·`발 높이 다름`이면 고쳐서 다시 만든다. **투명이 아니면 배경을 순자홍 #FF00FF 한 색 평면으로 다시 만든다.**
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
       if feet:                                  # 동작 그림: 세 사람의 발바닥 높이가 같아야 함
           bottoms = []
           for c in range(cols):
               ys_c = np.where(m[:, w * c // cols:w * (c + 1) // cols].any(axis=1))[0]
               bottoms.append(ys_c.max() / h)
           if max(bottoms) - min(bottoms) > 0.02: bad.append(f"발 높이 다름 {[round(v, 3) for v in bottoms]}")
       print(path, "OK" if not bad else f"다시 — {bad}", [round(float(v), 3) for v in box])
       return not bad
   # 기준·자세·동작 그림: check(경로, cols=3, feet=True) · 소품 판: check(경로, cols=4, margin=0.02)
   ```
5. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 화면·휴대폰·서류·책·게시판·시계·달력·간판에도 없음 (빈 판이나 단순한 줄·도형만). 실제 회사·앱·병원의 이름·로고를 닮게 그리지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.
   **사람을 나쁘게 그리지 않는다** — B 가 소리치는 장면도 답답함이지 폭력이 아니다(주먹·물건 던지기 없음). 아내·팀장·의사는 지치거나 놀란 얼굴은 되지만 무서운 사람처럼 그리지 않는다. 약을 먹는 장면·주사·피는 그리지 않는다.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. psychology/source/adhd-ab-2026-11/puppet/motion/A-REF.png`). 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게 — 배경은 `psychology/source/adhd-ab-2026-11/puppet/`, 기준·자세·동작·소품은 `psychology/source/adhd-ab-2026-11/puppet/motion/`, 썸네일 그림은 `psychology/source/adhd-ab-2026-11/images/`).
   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     - 배경·썸네일(JPEG): RGB · 크기 1536×864 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.
     - 기준·자세·동작·소품(PNG, 투명 유지): 아래 코드 그대로.
       ```python
       from PIL import Image
       import os
       Q = getattr(Image, "Quantize", Image).FASTOCTREE
       def save_png(src, dst, limit=700_000):
           im = Image.open(src).convert("RGBA")
           w, h = im.size
           s = min(1.0, 1536 / max(w, h))
           while True:
               cur = im.resize((round(w * s), round(h * s)), Image.LANCZOS) if s < 1 else im
               cur.save(dst, optimize=True)
               if os.path.getsize(dst) > limit:
                   cur.quantize(colors=256, method=Q).save(dst, optimize=True)   # 256색 (투명 유지)
               if os.path.getsize(dst) <= limit or max(cur.size) <= 900:
                   break
               s *= 0.9
           print(dst, os.path.getsize(dst), cur.size)
       ```
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[psychology] adhd-ab-2026-11 <파일 이름> 이미지` (예: `[psychology] adhd-ab-2026-11 A-REF.png 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 공통 화풍 (모든 프롬프트 맨 앞에 그대로 붙임)

```
STYLE: a simple, warm Korean daily-life webtoon (일상툰) look for a YouTube animation. Rounded simple shapes, thin clean dark-brown outlines, soft flat pastel colors with at most one light shading tone, very little detail. People are about 3 heads tall — a little cute but clearly adults (children smaller). Simple faces: small oval eyes, short eyebrows that carry the emotion, a small mouth; light pink cheeks only when embarrassed or crying. Simple comic marks are allowed only as shapes (one sweat drop, small sparkle lines, a little gloomy cloud scribble). Expressions must read instantly on a small phone screen. From picture 2 on, match EXACTLY the drawing style, line weight, colors and proportions of picture 1. Warm, gentle, emotionally honest mood — no horror, no violence, nobody is a villain. 2D drawing only — not 3D, not a photo, not glossy anime. Absolutely no text, letters, numbers, logos or watermarks anywhere — screens, phones, papers, books, boards, signs, clocks and packages are blank or show only simple shapes. Do not imitate any specific existing webtoon or artist.
```

## 배경판 (배경 — 공통 화풍 다음에 그대로 붙임)

```
BACKGROUND PLATE for a 2D daily-life webtoon animation: full-bleed landscape 1536x864, eye-level camera, NO people and no animals anywhere. Simple, clean webtoon background in the same style as the characters: few objects, soft pastel colors, light outlines. Leave a clear empty area in the front-center where characters will be placed later (a standing adult there would be about 75% of the picture height, feet near 92% of the height; a sitting person sits on the furniture described). Keep the middle calm and uncluttered.
```

## 반반 화면 (반반 화면 배경 — 배경판 다음에 그대로 붙임)

```
SPLIT-SCREEN SAFE: this plate will often be cropped to its central half (from 25% to 75% of the width) for a side-by-side split screen, so put the furniture the person uses inside that central half.
```

## 인물 (기준·자세·동작·썸네일 — 공통 화풍 다음에 그대로 붙임)

```
CHARACTERS — draw each person exactly like their reference or pose sheet (pictures 1, 2, 3, 4, 5, 6, 7, 8). The same face, hair, clothes, colors and proportions in every picture:
A — the main person: a 32-year-old Korean woman, office worker. Shoulder-length dark brown hair in a loose low ponytail with soft side bangs and a few loose strands. Light blue shirt with sleeves rolled up once, navy cardigan, dark gray slacks, white sneakers, a plain blank ID badge on a lanyard. Kind, a bit scattered, relatable; slightly tired eyes when neutral.
B — the other main person: a 51-year-old Korean man, office worker and father. Short black hair neatly combed, gray at the temples, slightly receding hairline, slightly round face with smile lines, a small belly. White shirt, plain navy tie (loosened or removed at home), gray slacks, black shoes; at home a gray knit cardigan over the white shirt. Warm but tired, a little stubborn, clearly early 50s.
W — B's wife: a 50-year-old Korean woman, short wavy dark hair with a few gray strands, a soft pink blouse, beige trousers. Tired and hurt, never angry like a monster.
S — B's son: a 14-year-old Korean boy, messy short black hair, a plain navy school hoodie, gray pants, sneakers. Shy and fidgety.
T — A's team leader: a 45-year-old Korean woman, short bob haircut, glasses, a gray blazer over a white top, black trousers. Strict-looking but fair, never mean.
D — A's psychiatrist: a 40-year-old Korean woman doctor, hair tied back, a white doctor's coat over a light green top, calm and kind.
K — the son's child psychiatrist: a 55-year-old Korean man doctor, short gray hair, round glasses, a white doctor's coat over a light blue shirt, warm grandfatherly smile.
F — B's friend: a 52-year-old Korean man, a little chubby, short hair, a casual dark green jacket over a T-shirt. Cheerful and loud.
```

## CUTOUT (기준·자세·동작·소품 — 그다음에 그대로 붙임 · 배경·썸네일에는 붙이지 않음)

```
CUTOUT: only the described subjects, as isolated cutouts on a fully transparent background (PNG with alpha channel) — no ground, no floor line, no cast shadow, no scenery, no frame, no other objects or people. Clean hard edges with the dark outline. Every subject must be fully visible with empty margin: nothing may touch or cross the canvas edges — keep at least 5% empty transparent space on every side. If a transparent background is impossible, make the whole background one flat pure magenta #FF00FF with no shading, and use no magenta, purple or hot pink at all on the subjects.
```

## 기준 시트 (기준 그림 — CUTOUT 다음에 그대로 붙임)

```
CHARACTER REFERENCE SHEET: landscape 1536x1024, three equal invisible columns, the SAME person three times standing relaxed with a calm, kind face: column 1 front view, column 2 three-quarter view facing left, column 3 pure side view facing left. Same scale, feet on the same invisible baseline at about 92% of the canvas height, standing adult about 70% of the canvas height. This sheet defines this person for every later picture.
```

## 자세 시트 (조연 자세 그림 — CUTOUT 다음에 그대로 붙임)

```
POSE SHEET: landscape 1536x1024, three equal invisible columns, the SAME person three times, one pose per column as described (three separate poses for different scenes — not one continuous movement). Same scale, same clothes and colors, feet (or the chair legs, when sitting) on the same invisible baseline at about 92% of the canvas height, a standing adult about 70% of the canvas height. Each figure centered in its column, full body, never crossing a column border; clear empty space between the columns. This sheet also defines how this person looks in every later picture.
```

## MOTION STRIP (동작 그림 — CUTOUT 다음에 그대로 붙임)

```
MOTION STRIP: landscape 1536x1024, divided into three equal invisible columns. The three figures are three consecutive animation drawings of ONE continuous movement by the SAME person, like an animator's key pose, in-between and key pose: frame 1 in the left column, frame 2 in the center column, frame 3 in the right column. Between the frames keep everything identical except the moving parts: same scale, same camera angle, same facing direction, same clothes, colors and line weight, and the soles of the feet (or the legs of the stool, when sitting) on exactly the same invisible baseline at about 92% of the canvas height, at the same horizontal spot in each column — the body stays in place and only the arms, hands, head, face, torso lean and held objects move. A standing adult is about 70% of the canvas height (top of the head near 22%) — a sitting adult or a child is smaller in the same scale. Any object held in the hands keeps the same design and size in all three frames and stays inside the same column. Each figure is centered in its column, full body from head to shoes, and never crosses a column border; leave clear empty space between the columns. No motion lines, no effects, no flying objects unless the prompt asks for them.
```

## 썸네일 (썸네일 그림 — 인물 다음에 그대로 붙임)

```
THUMBNAIL PICTURE for a video cover: full-bleed landscape 1536x864, a complete scene with background (NOT a cutout). The people and their faces sit in the upper 62% of the picture; the bottom 35% is a calm, simple, darker surface (table, floor or wall) where large title text will be added later by code — nothing important there. Leave one empty space beside the main person's head (not over any face, hand or body) where a speech bubble will be added later. Strong, readable emotion for a small phone screen. Absolutely no text, no letters, no numbers, no symbols, no speech bubbles drawn.
```

## 1. A-REF — A 기준 그림 (앞 · 4분의 3 · 옆) — 이 편 그림체 기준

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/A-REF.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 기준 3면

```
Draw A only. This is A, the main person of this video. Picture 1 also defines the drawing style of every later picture.
```

## 2. B-REF — B 기준 그림 (앞 · 4분의 3 · 옆)

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/B-REF.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 기준 3면

```
Draw B only, in exactly the same style as picture 1. This is B, the other main person of this video.
```

## 3. W-POSES — 아내 자세 3: 따짐 · 빈손을 가리킴 · 베란다 통화

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/W-POSES.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3개

```
Draw W only. Column 1: standing, three-quarter view facing left, arms crossed, asking with a tired, disappointed face. Column 2: standing, facing left, one open palm gesturing toward someone's empty hands, frustrated but not angry-looking. Column 3: standing, facing right, talking on a phone held to her ear, sad eyes looking down.
```

## 4. T-POSES — 팀장 자세 3: 회의 중 '듣고 있어요?' · 서류 읽기 · 엄지 척

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/T-POSES.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3개

```
Draw T only. Column 1: sitting on an office chair, facing left, leaning forward with a puzzled face and one hand slightly raised as if asking a question. Column 2: standing, facing left, reading a blank document. Column 3: standing, facing left, giving a small approving thumbs-up with a warm smile.
```

## 5. D-POSES — A씨 주치의 자세 3: 질문 · 기록부 보기 · 끄덕임 (앉은 자세)

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/D-POSES.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3개

```
Draw D only, sitting on a doctor's office chair, facing left. Column 1: asking a gentle question, one open palm. Column 2: looking down at a blank open booklet in her hands. Column 3: a kind nod with a small smile.
```

## 6. S-POSES — 아들 자세 3 (앉은 자세): 손 꼼지락 · 아빠 쳐다봄 · 수줍은 웃음

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/S-POSES.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3개

```
Draw S only, sitting on a clinic chair, facing right. Column 1: fidgeting with his fingers, looking down. Column 2: glancing up and to the left at his father. Column 3: a small shy smile.
```

## 7. K-POSES — 소아청소년과 의사 자세 3 (앉은 자세): 설명 · 아버지에게 질문 · 따뜻한 미소

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/K-POSES.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3개

```
Draw K only, sitting on a doctor's office chair, facing left. Column 1: explaining with one hand open. Column 2: turning slightly to look up at an adult on the left with a curious, gentle questioning face. Column 3: a warm reassuring smile.
```

## 8. F-POSES — 친구 자세 3 (술집, 앉은 자세): 휴대폰 보여 주기 · 크게 웃기 · 잔 들기

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/F-POSES.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3개

```
Draw F only, sitting on a pub stool, facing left. Column 1: holding up a phone toward the left with its blank screen visible, grinning. Column 2: laughing loudly, head back. Column 3: raising a beer glass.
```

## 9. BG-OFFICE — A씨 사무실 자리 (낮) — 1장 · 3장

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-OFFICE.jpg`** — JPEG 700KB 이하 · 가로 1536×864 · 가운데 절반으로 잘라 반반 화면에도 씀

```
A small open-plan office in the afternoon: a clean desk in the center with a monitor (blank light-blue screen), a keyboard, a mug and a small potted plant; an office chair in front of the desk; soft daylight from a window on the left; other desks blurred in the back.
```

## 10. BG-B-LIVING — B씨 집 거실 (저녁) — 1장 · 2장(밤은 코드로 어둡게) · 4장

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-B-LIVING.jpg`** — JPEG 700KB 이하 · 가로 1536×864 · 가운데 절반으로 잘라 반반 화면에도 씀

```
A cozy Korean apartment living room in the evening: a brown fabric sofa in the center with a low wooden table in front of it, a standing lamp, a TV cabinet on the right (TV off, blank), warm yellow light, wooden floor.
```

## 11. BG-A-BED — A씨 원룸 침실 (새벽 3시)

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-A-BED.jpg`** — JPEG 700KB 이하 · 가로 1536×864 · 가운데 절반으로 잘라 반반 화면에도 씀

```
A small studio-apartment bedroom at 3 a.m.: a single bed with a light-gray blanket and pillows in the center, a bedside table with a small lamp turned off, dark blue night colors, soft cool glow, curtains closed.
```

## 12. BG-CLINIC — A씨가 간 정신건강의학과 진료실

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-CLINIC.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
A calm, bright psychiatry consultation room: a wooden desk on the right with a blank monitor, a doctor's chair behind it facing left, a comfortable patient chair on the left facing right, a potted plant, soft beige walls, a window with light curtains.
```

## 13. BG-RESTROOM — 회사 화장실 세면대

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-RESTROOM.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
A clean company restroom: a row of white sinks with a long mirror above (the mirror shows only soft light reflections, no people), pale mint tiles, warm ceiling light. The front-center floor in front of the middle sink is empty for a standing person.
```

## 14. BG-MEETING — 회사 회의실

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-MEETING.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
A small company meeting room: a long light-wood table seen from the side across the front, office chairs around it, a blank wall screen at the back, glass wall on the right, daylight.
```

## 15. BG-B-ROOM — B씨 침실 (밤) — 다툰 뒤 혼자

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-B-ROOM.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
A Korean apartment bedroom at night: the edge of a double bed in the center (gray-blue bedding), a closed wooden door on the left, a small bedside lamp giving dim warm light, the rest in dark blue.
```

## 16. BG-VERANDA — 아파트 베란다 (저녁)

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-VERANDA.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
An apartment veranda in the early evening: potted plants along the floor, a drying rack folded against the wall, big windows looking out on other apartment buildings with a few lit windows (no signs), soft orange and blue evening light.
```

## 17. BG-B-OFFICE — B씨 회사 — 왼쪽 책상 · 오른쪽 빈 게시판

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-B-OFFICE.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
A quiet company office floor: on the left a desk with a blank monitor and an office chair; on the right wall a large cork notice board with several blank white papers pinned on it (no writing). Neutral gray-blue colors, fluorescent light. The front area in front of the board is empty for a standing person.
```

## 18. BG-PUB — 동네 술집 테이블 (밤)

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-PUB.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
A cozy Korean neighborhood pub at night: a round metal table in the center with small dishes of snacks and two empty beer glasses, low stools on both sides, warm hanging lights, wooden walls with blank paper menus (no writing).
```

## 19. BG-PEDS — 소아청소년 정신건강의학과 진료실

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-PEDS.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
A bright, friendly child and adolescent psychiatry consultation room: a desk on the right with a doctor's chair facing left, two chairs on the left facing right (one for a parent, one for a teenager), soft pastel colors, a few toys and plain picture frames with only color shapes.
```

## 20. BG-RECEPTION — 병원 접수대

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/BG-RECEPTION.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
A clean hospital reception area: a light-wood reception counter on the right (no people behind it), a waiting area with a few chairs on the left, a blank number display on the wall, soft daylight.
```

## 21. A01 — A: 모니터 보며 한숨 → 휴대폰을 들고 멍함 → 시계를 보고 화들짝 (땀방울)

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/A01.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
A, sitting on an office chair, three-quarter view facing RIGHT. Frame 1: looking at an invisible monitor on the right with a heavy sigh, shoulders down. Frame 2: holding a phone up in both hands, zoned out with empty eyes, the phone screen glowing blank. Frame 3: startled, looking up to the upper right at an invisible clock, wide eyes, one sweat drop, the phone still in her hand.
```

## 22. A02 — A: (침대에 앉아) 드라마에 빠져 키득 → 화면에 몰입 → 하품하면서도 다음 편 누름

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/A02.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
A, sitting cross-legged on an invisible bed, hugging a pillow, facing the viewer, holding a phone. Frame 1: giggling at the phone screen. Frame 2: completely absorbed, face lit by the screen's glow, eyes wide. Frame 3: a big yawn with watery eyes, but her thumb taps the screen to keep watching.
```

## 23. A03 — A: (밤, 침대) 영상을 진지하게 봄 → 입을 가리며 '내 얘기네' → 결심한 얼굴로 화면을 누름

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/A03.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
A, sitting on an invisible bed, facing the viewer, holding a phone. Frame 1: watching the phone seriously, eyebrows slightly raised. Frame 2: one hand over her mouth, realizing 'this is me', eyes wide. Frame 3: determined face, tapping the phone screen firmly with one finger.
```

## 24. A04 — A: (진료실 의자) 긴장해 듣기 → 빈 기록부를 펼쳐 보여 줌 → 안도하며 가슴에 손

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/A04.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
A, sitting on a patient chair, three-quarter view facing RIGHT. Frame 1: listening nervously, hands on her knees. Frame 2: holding up an open booklet with blank pages toward the right. Frame 3: a relieved small nod, one hand on her chest.
```

## 25. A05 — A: (사무실) 집중해 타자 → 마우스 클릭 → 놀라 멍하니 굳음

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/A05.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
A, sitting on an office chair, three-quarter view facing RIGHT. Frame 1: typing on an invisible keyboard, very focused, calm face. Frame 2: clicking an invisible mouse with a small decisive nod. Frame 3: frozen, stunned, eyes wide and mouth slightly open, slowly realizing something.
```

## 26. A06 — A: (세면대 앞에 서서) 눈물을 참음 → 눈물을 손등으로 닦음 → 슬프게 옅은 미소

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/A06.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
A, standing, three-quarter view facing LEFT, as if in front of an invisible sink. Frame 1: both hands gripping the edge of an invisible sink, lips pressed, holding back tears. Frame 2: tears falling, wiping her eyes with the back of her hand. Frame 3: a small, sad smile after wiping, shoulders relaxed.
```

## 27. A07 — A: (회의 중) 멍하니 허공 → 불리자 화들짝 → 이마를 짚으며 '아침 약…'

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/A07.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
A, sitting on an office chair, three-quarter view facing LEFT. Frame 1: zoned out, staring into space, mouth slightly open. Frame 2: startled, sitting up straight, one sweat drop. Frame 3: one hand on her forehead, embarrassed, eyes closed, realizing she forgot something.
```

## 28. A08 — A: (1년 뒤) 휴대폰을 서랍에 넣음 → 차분히 일함 → 기대앉아 만족한 미소

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/A08.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
A, sitting on an office chair, three-quarter view facing RIGHT. Frame 1: putting her phone into an open desk drawer at her side with a calm face. Frame 2: typing on an invisible keyboard, focused and relaxed. Frame 3: leaning back in the chair with a satisfied small smile.
```

## 29. B01 — B: (거실 소파) 고지서를 보며 인상 → 고지서를 놓고 휴대폰에 멍함 → 시계를 보고 화들짝

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/B01.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
B, sitting on an invisible sofa, three-quarter view facing LEFT, wearing the gray cardigan. Frame 1: frowning at a blank paper bill in his hand. Frame 2: the bill dropped on his lap, holding a phone, zoned out with empty eyes. Frame 3: startled, looking up to the upper left at an invisible clock, one sweat drop.
```

## 30. B02 — B: (밤, 소파) 낚시 영상에 신나 주먹 → 화면에 몰입 → 하품하면서도 계속 봄

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/B02.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
B, sitting on an invisible sofa, facing the viewer, gray cardigan, holding a phone. Frame 1: excited, a small fist pump, watching the phone. Frame 2: completely absorbed, face lit by the screen's glow. Frame 3: a big yawn, but still holding the phone up and watching.
```

## 31. B03 — B: (밤, 소파) 영상을 진지하게 봄 → 불편하게 인상 → 손을 내저으며 화면을 끔

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/B03.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
B, sitting on an invisible sofa, facing the viewer, gray cardigan, holding a phone. Frame 1: watching seriously with a slight nod. Frame 2: an uneasy frown, lips pressed. Frame 3: waving his free hand dismissively while pressing the phone's side button to turn it off.
```

## 32. B04 — B: (거실에 서서) 손바닥을 들어 방어 → 답답해 소리침 → 등을 돌려 방으로 감

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/B04.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
B, standing, three-quarter view facing LEFT, gray cardigan. Frame 1: both palms raised defensively, an awkward face. Frame 2: shouting in frustration — eyebrows angled, mouth wide — but arms down and no fists (frustrated, not violent). Frame 3: turning away toward the right, starting to walk off, head down.
```

## 33. B05 — B: (침대 끝에 앉아) 두 손으로 머리를 감쌈 → 한숨 쉬며 바닥을 봄 → 얼굴을 쓸어내림

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/B05.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
B, sitting on the edge of an invisible bed, facing the viewer, gray cardigan. Frame 1: head in both hands. Frame 2: a long sigh, elbows on knees, looking at the floor with guilty eyes. Frame 3: rubbing his face with one hand, tired and regretful.
```

## 34. B06 — B: (회사 책상) 화면을 읽음 → 충격에 굳음 → 눈을 감고 이마를 짚음

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/B06.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
B, sitting on an office chair, three-quarter view facing RIGHT, white shirt and navy tie. Frame 1: reading an invisible monitor calmly. Frame 2: frozen in shock, eyes wide, one sweat drop. Frame 3: eyes closed, one hand on his forehead.
```

## 35. B07 — B: (게시판 앞에 서서) 기대하며 훑어봄 → 실망 → 어깨가 처지고 고개 숙임

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/B07.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
B, standing, three-quarter back view facing RIGHT toward an invisible notice board, white shirt and navy tie. Frame 1: scanning the board with a hopeful look. Frame 2: disappointed, mouth tight. Frame 3: shoulders dropped, looking down at the floor.
```

## 36. B08 — B: (술집에 앉아) 내민 휴대폰을 봄 → 따라 웃음 → 어색하게 잔을 듦

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/B08.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
B, sitting on a pub stool, three-quarter view facing RIGHT, gray cardigan. Frame 1: leaning to look at a phone held out from the right. Frame 2: laughing along. Frame 3: raising a beer glass with a slightly forced smile.
```

## 37. B09 — B: (진료실 의자) 진지하게 듣기 → 자기를 가리키며 '저요?' → 턱을 괴고 생각

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/B09.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
B, sitting on a chair, three-quarter view facing RIGHT, white shirt without a tie. Frame 1: listening seriously, hands on his knees. Frame 2: pointing at himself, surprised and confused — a 'who, me?' face. Frame 3: thoughtful, hand on his chin, looking down.
```

## 38. B10 — B: (접수대 앞에 서서) 머뭇거리며 뒷목을 만짐 → 손을 살짝 들고 물음 → 어색하지만 희망찬 미소

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/B10.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
B, standing, three-quarter view facing RIGHT toward an invisible counter, white shirt without a tie. Frame 1: hesitating, rubbing the back of his neck. Frame 2: asking something with one hand slightly raised. Frame 3: an awkward but hopeful smile.
```

## 39. PROPS-A — 소품 4: 휴대폰 · 고지서 · 요일 약통과 물컵 · 바늘 없는 벽시계

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/PROPS-A.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 소품 4

```
Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, similar visual size, each fully inside its column: (1) a smartphone, front view, the screen glowing plain light blue; (2) an opened envelope with a paper bill sticking out, only blank gray lines on it; (3) a weekly pill organizer box with seven small lids and a glass of water beside it; (4) a round wall clock face with tick marks only — NO numbers and NO clock hands (the hands will be added by code).
```

## 40. PROPS-B — 소품 4: 세탁소 비닐 속 양복 · 생활기록부 · 재생 버튼 화면 · 빈 달력

**저장 경로: `psychology/source/adhd-ab-2026-11/puppet/motion/PROPS-B.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 소품 4

```
Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, similar visual size: (1) a dark suit on a hanger inside a clear dry-cleaning plastic bag; (2) a closed school record booklet with a plain light-green cover (no writing); (3) a smartphone showing a video player — a big white play-button triangle and a thin progress bar, nothing else; (4) a wall calendar page that is just a grid of empty squares with one square circled in red (no numbers, no letters).
```

## 41. TH-CHAR — 썸네일 그림: 왼쪽 A(환한 낮 · 일을 끝내고 안도) | 오른쪽 B(어두운 밤 · 머리를 감쌈) 반반 대비

**저장 경로: `psychology/source/adhd-ab-2026-11/images/TH-CHAR.jpg`** — JPEG 700KB 이하 · 가로 1536×864 · 글자 없음

```
SPLIT CONTRAST in one picture, divided exactly in half by a clean vertical line in the middle. LEFT HALF: A at her office desk in bright warm daylight, leaning back with a relieved small smile, her phone put away in an open drawer, the monitor glowing calm, a tidy desk — her face clearly visible. RIGHT HALF: B at night on the edge of his bed in dark blue light, head in his hands, a crumpled blank paper bill and a phone on the floor, a small gloomy cloud scribble above his head — his face visible and tired. The two halves feel like opposites (light vs dark, warm vs cold). Leave empty space beside each person's head (not over any face) for speech bubbles. The bottom 35% of the whole picture is a calm, darker surface (desk front on the left, floor on the right) where large title text will be added later — nothing important there.
```

## 받은 뒤 (Claude)
- main 의 `psychology/source/adhd-ab-2026-11/puppet/`·`images/` 를 가져와 41장을 확대해 검수: 1번 그림체와 같은지 · 같은 사람인지 · 그림 속 글자 없음 · 세 장의 발 높이·크기·옷 · 반반 화면 배경의 가운데 절반 · 사람을 나쁘게 그리지 않았는지.
- `psychology/source/puppet_slice.py adhd-ab-2026-11` 로 자르기 → `puppet/cut/` + `manifest.js` · 장면 `video/episodes/adhd-ab-2026-11/index.html` (공통 엔진 `video/render/psy_anim.js` — 반반 화면·말풍선·시계 바늘은 코드).
- 오디오(`narration.mp3`, 내레이션만 — 말풍선은 소리 없음)가 생기면 align → sync → check·layout-check 문제 0 → 렌더 → 완성 mp4 를 직접 봄.
- 썸네일 = `images/TH-CHAR.jpg` + 문구는 코드(`video/render/thumb.mjs`) — 제목·문구는 `guides/persona_loop.md` 검증 뒤.
