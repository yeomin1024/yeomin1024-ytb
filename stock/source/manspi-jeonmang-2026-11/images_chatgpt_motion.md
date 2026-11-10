# manspi-jeonmang-2026-11 롱폼 — 움직임용 보충 그림 36장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.0 — 2026-11-10 — 사용자 지시 "아니 내말은 원래 방식으로 하되 진짜 애니메이션 처럼 움직이는 효과를 재현하라고 뭔 소린지 알겠어? 더 보충할 이미지가 필요하면 그걸 만들라고". 기준 대본 = main 커밋 ac40a5e3 의 `manspi-jeonmang-2026-11.txt` (5장 61문장). 앞 요청 `images_chatgpt.md` v1.0 의 17장(배경 5 · 인물 자세 8 · 소품 4)은 **그대로 쓴다** — 이 파일은 거기에 **더하는** 그림이다. `images_chatgpt_anim.md`(키 장면 39장)는 쓰지 않는다.

**왜 더 필요한가 — 코드 애니메이션 방식 (원래 방식 그대로)**
- 영상은 지금처럼 Claude 가 코드로 만든다: 배경 그림 위에 인물·소품 조각을 올리고 움직인다. 지난 영상이 '대충'이었던 까닭은 조각이 **동작 하나에 그림 한 장**뿐이라 인물이 미끄러지기만 하고, 물건을 손에 들지 않았기 때문이다.
- 그래서 **동작마다 이어지는 그림 3장**(애니메이터의 키 → 중간 → 키 그림)을 한 장에 받는다. Claude 가 1→2→3(→2→1)을 초당 8~12장으로 바꿔 끼우면 팔·몸·얼굴이 실제로 움직인다. 그 위에 코드가 예비 동작·튕김·늘었다 줄었다·따라 흔들림·숨쉬기·카메라 밀기를 더한다.
- 물건은 **손에 든 채로** 그린다 (저금통·유리병·리모컨·체·돋보기·저울·도장·달력판) — 손과 물건이 같이 움직여 '들고 있는' 것이 보인다.
- 동전·지폐·땀·말풍선처럼 날아가는 것은 따로 조각(FX)으로 받아 코드가 포물선·중력으로 날린다.
- 숫자(10,000 · 8,000)·BUY·화살표·그래프는 그림 속 빈 판·빈 화면 위에 코드가 얹는다.

| 번호 | 저장 경로 (모두 `stock/source/manspi-jeonmang-2026-11/puppet/motion/`) | 무엇 (왼쪽 → 가운데 → 오른쪽 = 동작 순서) | 대본 문장 |
|---|---|---|---|
| 1 | `V01.png` | 시청자: 돼지저금통을 꼭 안고 설렘 → 발끝으로 들썩 → 1번과 같고 눈만 감은 미소 | 1 |
| 2 | `V02.png` | 시청자: 저금통을 거꾸로 들어 올림 → 흔듦 → 반대로 기울여 더 세게 흔듦 | 1 |
| 3 | `V03.png` | 시청자: 은퇴 자금 유리병(흔들의자 그림 스티커)을 망설이며 안음 → 병을 기울여 쏟음 → 거의 빈 병을 거꾸로 흔듦 | 2 |
| 4 | `V04.png` | 시청자: 밤에 휴대전화를 얼굴 가까이 보며 걱정 → 눈을 비빔 → 더 지친 얼굴로 다시 들여다봄 | 2 |
| 5 | `V05.png` | 시청자: 옆모습 걷기 3장 (화가 나서 휴대전화를 쥐고 오른쪽으로 걸어감) | 4 |
| 6 | `V06.png` | 시청자: 휴대전화 화면을 앞으로 내밀며 따짐 → 흔들며 다른 손바닥을 펴 '이건요?' → 두 팔을 떨구고 허탈 | 4 |
| 7 | `V07.png` | 시청자: 리모컨을 TV 쪽으로 겨눔 → 엄지가 멈칫 → 리모컨을 내리고 턱을 괴고 고민 | 5 |
| 8 | `V08.png` | 시청자: 큰 체를 가슴 앞에 들고 위를 봄 → 1번과 같고 눈만 감음 → 체 안을 내려다봄 | 6 · 15 · 16~54 |
| 9 | `V09.png` | 시청자: 체를 왼쪽으로 기울여 흔듦 → 무릎을 굽혀 튕김 → 오른쪽으로 기울여 흔듦 | 18 · 23 · 28 · 33 |
| 10 | `V10.png` | 시청자: 체 속에서 무언가를 집음 → 팔을 뒤로 젖혀 던질 준비 → 왼쪽으로 던지고 팔이 따라감 | 18 · 23 · 28 · 33 |
| 11 | `V11.png` | 시청자: 체 아래로 빠져나가는 것을 봄 → 오른쪽을 보며 미소 끄덕 → 체를 든 채 엄지 척 | 38 · 42 · 47 · 51 |
| 12 | `V12.png` | 시청자: 큰 빈 판을 껴안고 반한 눈 (왼쪽으로 기움) → 오른쪽으로 기움 → 1번과 같고 눈 감고 황홀 | 12 |
| 13 | `V13.png` | 시청자: 몸을 숙여 큰 돋보기로 오른쪽을 살핌 → 돋보기를 낮추며 눈을 찡그림 → 몸을 펴고 턱을 괴고 의심 | 14 |
| 14 | `V14.png` | 시청자: 오른손 검지가 앞쪽 버튼으로 다가감 → 왼손이 자기 오른손목을 붙잡아 당김 → 숨을 내쉬며 안도 | 24 |
| 15 | `V15.png` | 시청자: 휴대전화를 보며 무표정 → 위(시계)를 올려다보며 지침 → 어깨를 떨구고 한숨 | 29 |
| 16 | `V16.png` | 시청자: 메모장에 적음 → 펜을 멈추고 오른쪽(TV)을 보며 들음 → 눈을 감고 미소 짓으며 끄덕 | 55~58 |
| 17 | `V17.png` | 시청자: 오른손을 들어 인사 → 손을 반대로 흔듦 → 손을 가슴에 얹고 살짝 고개 숙임 | 60~61 |
| 18 | `E01.png` | 전문가: 주먹을 높이 들고 입을 크게 벌려 외침 → 주먹을 어깨로 당김(입 반쯤) → 다른 주먹을 앞으로 내지르며 외침 | 1 · 3 · 17 · 31 |
| 19 | `E02.png` | 전문가: 큰 빈 달력판을 한 손에 들고 다른 손을 높이 듦 → 손바닥으로 달력판을 탕 침 → 달력판을 가리키며 씩 웃음 | 16~19 |
| 20 | `E03.png` | 전문가: 손목시계를 보여 줌 → 검지로 시계를 톡톡 → 다른 손으로 '어서' 손짓 | 20~24 |
| 21 | `E04.png` | 전문가: 주먹을 뒤로 당기고 턱을 듦 → 주먹으로 가슴을 탕 (눈 감고 뿌듯) → 엄지 척 + 윙크 | 25~28 |
| 22 | `E05.png` | 전문가: 진땀 흘리며 주먹 들고 외침 → 어깨 너머 뒤를 힐끗 보며 억지 미소 → 앞으로 돌아 더 크게 외침 (땀이 튐) | 30~33 |
| 23 | `E06.png` | 전문가 (왼쪽을 봄): 차렷 → 어깨 으쓱·손바닥 위로·눈 피함 → 고개 갸웃·눈 감고 능청 미소 | 4 |
| 24 | `E07.png` | 전문가: 뒷모습 걷기 3장 (화면 안쪽으로 걸어 나감) | 4 |
| 25 | `E08.png` | 전문가: 계산기를 두드림 → 왼쪽 위를 보며 생각 → 오른쪽을 보며 다시 두드림 | 7~8 |
| 26 | `E09.png` | 전문가: 수정 구슬을 두 손에 들고 봄 → 얼굴 가까이 들어 한쪽 눈으로 들여다봄 → 머리를 긁으며 갸웃 | 9 |
| 27 | `E10.png` | 전문가: 서류 묶음을 읽음 → 깜짝 놀라 어깨가 솟고 서류가 손에서 튀어 오름 → 빈손을 든 채 진땀·입 벌림 | 10 |
| 28 | `E11.png` | 전문가 (왼쪽 판을 봄): 지우개로 왼쪽 위를 닦음 → 왼쪽 아래를 닦음 → 마커로 더 낮은 자리에 선을 그으며 어깨 너머로 봄 | 11 · 45~48 |
| 29 | `E12.png` | 전문가: 큰 고무도장을 높이 듦 → 아래로 쾅 찍음 (몸이 숙여짐) → 도장을 들어 올리며 다른 손 엄지 척 | 13 |
| 30 | `E13.png` | 전문가 (차분): 왼쪽 판을 검지로 가리키며 말함 → 카메라를 보며 손바닥을 펴고 말함(입 벌림) → 2번과 같고 입만 다묾 | 34 · 36~39 · 45~48 |
| 31 | `E14.png` | 전문가: 저울을 들고 수평 → 왼쪽 접시가 내려감 → 오른쪽 접시가 내려감 | 40~44 |
| 32 | `E15.png` | 전문가: 두 손바닥을 위로 펴고 솔직한 미소 → 눈 감고 고개를 살짝 저음 → 손을 가슴에 얹고 살짝 고개 숙임 | 49~54 |
| 33 | `BG-SIEVE0.jpg` | 배경: 거름망 무대에서 **체·받침대·쟁반만 뺀** 같은 그림 (시청자가 체를 직접 듦) | 6 · 15~54 |
| 34 | `BG-STUDIO0.jpg` | 배경: 스튜디오에서 **뒤 화면의 빨간 화살표만 뺀** 같은 그림 (빈 파란 화면) | 3~4 · 16~34 |
| 35 | `PROPS2.png` | 소품 4: 노부부 사진 액자 · 동전 가득한 유리병(3번과 같은 병) · 바늘 없는 벽시계 · 빈 벽달력 | 2 · 29 |
| 36 | `FX.png` | 움직임 조각 8 (4×2): 금화 앞면 · 금화 옆으로 기운 것 · 지폐(무늬만) · 땀방울 · 눈물 · 휙 선 · 반짝임 · 먼지 구름 | 효과 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
   **★ 먼저 기준 그림을 열어 본다 — 새 그림은 모두 이 그림들과 같은 사람이 그린 것처럼 (그림체·선 굵기·색·얼굴 꼴·비율·옷까지 같게). 인물 크기도 이 자세 시트들과 같게.**
   - 썸네일: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/1bcbf5532537e13ce5b1c1cd1402ffe328c59371/stock/source/manspi-jeonmang-2026-11/images/TH-CHAR.jpg (왼쪽 '-50%' 글자는 따라 그리지 않음)
   - 시청자(V): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/V-CALM.png · https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/V-NIGHT.png
   - 전문가(E): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/E-HYPE.png · https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/E-CALM.png
   - 33번 원본(체 무대): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/BG-SIEVE.jpg
   - 34번 원본(스튜디오): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/BG-STUDIO.jpg
   - 소품 그림체(돋보기·휴대전화·저울·수정 구슬 등): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/P-DOCS.png · https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/P-MARKS.png · https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/P-CHART.png
   그림을 열 수 없으면 아래 '공통 화풍'과 '인물' 설명대로 그린다.
1. 아래 1~36번 **36장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 **공통 화풍** 문단을 붙인다.
   - **1~32번(동작 그림)**: 공통 화풍 → **인물** → **CUTOUT** → **MOTION STRIP** → 프롬프트.
   - **33~34번(배경 고치기)**: 공통 화풍 → 프롬프트. **원본 그림을 편집해서** 만든다 (구도·가구·빛·색을 그대로 두고 적힌 것만 뺌). 편집이 안 되면 원본과 같은 구도로 새로 그려도 된다 — Claude 가 그 그림만 쓴다.
   - **35~36번(소품·조각)**: 공통 화풍 → **CUTOUT** → 프롬프트.
3. **1~32번은 한 장에 같은 사람을 3번** 그린다 — 왼쪽 → 가운데 → 오른쪽이 **한 동작을 이어 그린 3장**(애니메이션 원화)이다. 세 사람이 **같은 크기·같은 자리·같은 방향·같은 옷**이고, **발바닥이 같은 높이**에 있고, **움직이는 부분(팔·손·머리·얼굴·상체 기울기·손에 든 물건)만** 바뀐다. 손에 든 물건은 세 장 모두 같은 모양·같은 크기. 서로 겹치거나 칸(가로 3등분)을 넘지 않는다. 다른 사람·배경·바닥 그림자는 없다.
4. **검사 (1~32번·35~36번 필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`·`칸 넘음`·`발 높이 다름`이면 고쳐서 다시 만든다 (더 작게 · 여백을 넓게 · 발을 같은 선에). **투명이 아니면 배경을 순자홍 #FF00FF 한 색 평면으로 다시 만든다.**
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
   # 1~32번: check(경로, cols=3, feet=True) · 35번: check(경로, cols=4, margin=0.02) · 36번: check(경로, cols=4, rows=2, margin=0.02)
   ```
5. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 휴대전화·달력판·빈 판·시계·서류·도장 면·스티커에도 없음 (빈 화면이나 단순한 줄·도형만). 실제 방송사·증권사·은행·앱의 이름·로고·색을 닮게 그리지 않는다. 지폐는 실제 돈 도안·인물·숫자 없이 단순한 무늬만. 날씨(해·구름·비·번개)는 그리지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. stock/source/manspi-jeonmang-2026-11/puppet/motion/V01.png`). 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게, 폴더는 `stock/source/manspi-jeonmang-2026-11/puppet/motion/`).
   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     - 33~34번(JPEG): RGB · 크기 1536×864 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.
     - 1~32번·35~36번(PNG, 투명 유지): 아래 코드 그대로.
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
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[stock] manspi-jeonmang-2026-11 motion <파일 이름> 이미지` (예: `[stock] manspi-jeonmang-2026-11 motion V01.png 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 공통 화풍 (1~36번 모든 프롬프트 맨 앞에 그대로 붙임 — 기준 그림과 같은 그림체)

```
STYLE: Match exactly the art style of the reference thumbnail image and the reference character sheets: a polished flat 2D cartoon illustration with bold clean dark outlines, flat colors with one simple cel-shading tone and small highlights, warm cozy indoor lighting mixed with cool blue screen glow, expressive exaggerated faces (big eyes, clear eyebrows, open mouths, tears when sad) and easy-to-read body language for a small phone screen. Slightly chunky proportions (head about one quarter of the body height). It is a 2D drawing — not a 3D render, not clay or plastic, not a photo. Absolutely no text, letters, numbers, logos or watermarks anywhere — phones, boards, calendars, clocks, papers, stamps and stickers are blank or show only simple lines and shapes. No weather (no sky, sun, clouds, rain or lightning).
```

## 인물 (1~32번 — 공통 화풍 다음에 그대로 붙임)

```
CHARACTERS — draw them exactly like the reference thumbnail and reference character sheets, same face, hair, clothes, colors and proportions in every frame:
V — an ordinary Korean man around 40 who invested his savings: messy curly medium-brown hair, an olive-green casual button jacket with flap pockets over a beige checked shirt, brown trousers with a brown belt, brown shoes. A kind, emotional face that shows feelings strongly (worry, anger, relief).
E — a confident Korean TV stock-market commentator in his 50s: neatly combed dark hair with gray streaks at the temples, a navy-blue suit, white shirt, red tie, black shoes. A smug, self-assured smile and a raised eyebrow when hyping; a calm, honest face in his calm poses. He is a generic fictional person, not any real commentator.
```

## CUTOUT (1~32번 · 35~36번 — 그다음에 그대로 붙임 · 33~34번 배경에는 붙이지 않음)

```
CUTOUT: only the described subjects, as isolated cutouts on a fully transparent background (PNG with alpha channel) — no ground, no floor line, no cast shadow, no scenery, no frame, no other objects or people. Clean hard edges with the dark outline. Every subject must be fully visible with empty margin: nothing may touch or cross the canvas edges — keep at least 5% empty transparent space on every side. If a transparent background is impossible, make the whole background one flat pure magenta #FF00FF with no shading, and use no magenta, purple or hot pink at all on the subjects.
```

## MOTION STRIP (1~32번 — CUTOUT 다음에 그대로 붙임)

```
MOTION STRIP: landscape 1536x1024, divided into three equal invisible columns. The three figures are three consecutive animation drawings of ONE continuous movement by the SAME person, like an animator's key pose, in-between and key pose: frame 1 in the left column, frame 2 in the center column, frame 3 in the right column. Between the frames keep everything identical except the moving parts: same scale, same camera angle, same facing direction, same clothes, colors and line weight, and the soles of the feet on exactly the same invisible baseline at about 92% of the canvas height, at the same horizontal spot in each column — the body stays in place and only the arms, hands, head, face, torso lean and held objects move. The standing figure is about 70% of the canvas height (top of the head near 22%) — the same size as in the reference character sheets. Any object held in the hands keeps the same design and size in all three frames and stays inside the same column. Each figure is centered in its column, full body from head to shoes, and never crosses a column border; leave clear empty space between the columns. No motion lines, no effects, no coins or flying objects unless the prompt asks for them.
```

## 1. V01 — 시청자: 저금통을 안고 설렘

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V01.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture (as if watching a TV on the right). He hugs a chubby piggy bank (soft peach-coral color, a coin slot on its back, small ears and a curly tail) against his chest with both arms. Frame 1: hugging it, eyes shining with excitement, big hopeful smile. Frame 2: the same hug but up on his tiptoes with shoulders lifted, a little bounce of joy, mouth open happily. Frame 3: exactly like frame 1 but with his eyes closed in a happy smile (a blink).
```

## 2. V02 — 시청자: 저금통을 거꾸로 들고 흔듦

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V02.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture. He holds the same peach-coral piggy bank upside down with both hands at chest height, the coin slot pointing down toward the lower right. Frame 1: lifting it upside down, eager grin. Frame 2: shaking it — the piggy bank tilted clockwise, elbows out, teeth showing in excitement. Frame 3: shaking harder — the piggy bank tilted the other way (counter-clockwise), knees slightly bent, determined eager face. Do not draw any coins or money — they are added later.
```

## 3. V03 — 시청자: 은퇴 자금 유리병을 쏟음

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V03.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture. He holds a large clear glass jar with a lid removed; on the jar is a small round sticker showing only a simple picture of a wooden rocking chair (no words) — his retirement savings. Frame 1: hugging the jar full of gold coins close to his chest, hesitant and worried, eyebrows raised. Frame 2: tipping the jar forward and down toward the lower right with both hands, eyes squeezed shut, reluctant; the jar is half full. Frame 3: holding the nearly empty jar upside down and shaking it, sad face with a small tear; only two or three coins remain inside. Do not draw coins falling outside the jar — they are added later.
```

## 4. V04 — 시청자: 밤마다 휴대전화

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V04.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture, late at night, tired. Frame 1: holding a smartphone in both hands close to his face (we see the back of the phone), worried, eyes wide, a faint cool blue glow on his face. Frame 2: lowering the phone to his chest with one hand and rubbing his eyes with the other hand, exhausted. Frame 3: bringing the phone back up close to his face, now more tired — droopy eyelids, dark circles under the eyes, shoulders slumped forward.
```

## 5. V05 — 시청자: 화나서 걸어감 (옆모습 걷기)

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V05.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, side view walking to the right of the picture, angry and determined, a smartphone gripped in his right hand held up at chest height. A three-drawing walk cycle: Frame 1: contact pose — left leg forward with the heel touching the ground, right leg back, right arm swung forward. Frame 2: passing pose — the legs pass each other under the body, the body slightly higher, arms near the body. Frame 3: contact pose — right leg forward with the heel touching the ground, left leg back, the free arm swung forward. Same angry frowning face in all three frames, leaning a little forward.
```

## 6. V06 — 시청자: 휴대전화를 내밀며 따짐

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V06.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture. Frame 1: thrusting his smartphone forward to the right with his arm stretched out, the blank phone screen facing to the right, angry face, teeth clenched. Frame 2: still holding the phone out and shaking it, his other hand open with the palm up as if asking "what about this?", eyebrows raised in frustration. Frame 3: both arms dropped down at his sides, the phone hanging in one hand, shoulders slumped, looking down in disbelief — nobody answered.
```

## 7. V07 — 시청자: 리모컨을 겨누다 멈칫

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V07.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture, in the evening at home. Frame 1: pointing a TV remote control to the right with his arm stretched out, determined to switch the TV off, lips pressed. Frame 2: the same arm still out but his thumb frozen above the button, leaning back slightly, unsure eyes looking sideways. Frame 3: the remote lowered to his waist, his other hand on his chin, thinking hard with a small frown.
```

## 8. V08 — 시청자: 큰 체를 들고 기다림

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V08.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, front view facing the camera. He holds a large round kitchen sieve in front of his chest with both hands on its rim — a wooden rim and a fine gray metal mesh bowl, about as wide as his shoulders, the same design as the big sieve in the reference sieve stage picture. Frame 1: holding the sieve level, looking up above him, alert and ready, a small determined smile. Frame 2: exactly like frame 1 but with his eyes closed (a blink). Frame 3: the same pose but looking down into the sieve, inspecting it carefully, eyebrows slightly raised.
```

## 9. V09 — 시청자: 체를 흔듦

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V09.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, front view facing the camera, holding the same large round sieve (wooden rim, fine gray metal mesh) with both hands. Frame 1: the sieve tilted so its left side is lower, his body leaning to the left, gritting his teeth with effort. Frame 2: the sieve level, his knees bent in a little bounce, cheeks puffed, focused. Frame 3: the sieve tilted so its right side is lower, his body leaning to the right, gritting his teeth.
```

## 10. V10 — 시청자: 체에 걸린 것을 집어 던짐

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V10.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, front view facing the camera, holding the same large round sieve (wooden rim, fine gray metal mesh) at his waist with his left hand only (the sieve on the right side of the picture). Frame 1: his right hand reaching into the sieve, fingers pinching as if picking something up, annoyed frown. Frame 2: wind-up — his right arm pulled back and up beside his head, the hand closed as if holding something, body twisted, determined. Frame 3: follow-through — his right arm swung across toward the LEFT side of the picture, hand open after throwing, a satisfied "good riddance" face. Do not draw what he throws — it is added later.
```

## 11. V11 — 시청자: 통과한 것을 보며 엄지 척

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V11.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, front view facing the camera, holding the same large round sieve (wooden rim, fine gray metal mesh). Frame 1: holding it level with both hands, looking down under the sieve as if watching something slip through, curious. Frame 2: still holding it with both hands, turning his head to the RIGHT side of the picture with a warm smile and a small nod. Frame 3: holding the sieve with his left hand only and giving a happy thumbs-up with his right hand, bright smile facing the camera.
```

## 12. V12 — 시청자: 큰 빈 판을 껴안고 반함

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V12.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, front view facing the camera. He hugs a big blank rectangular sign board (light cream with a thin gold edge, about as wide as his shoulders, completely empty — nothing written on it) upright against his chest with both arms so its front faces the camera, his chin resting on its top edge. Frame 1: swaying to the left, starry admiring eyes and a dreamy smile, little sparkles in his eyes. Frame 2: swaying to the right, same dreamy face. Frame 3: exactly like frame 1 but with his eyes closed in blissful happiness (a blink).
```

## 13. V13 — 시청자: 돋보기로 살피며 의심

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V13.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture. He holds a big magnifying glass (wooden handle, brass rim, clear lens — the same design as the reference prop). Frame 1: leaning forward, holding the magnifying glass out to the right at eye level, examining something, one eye big and curious behind the lens. Frame 2: moving the magnifying glass lower, squinting hard, lips pursed. Frame 3: standing up straight, the magnifying glass lowered, his other hand on his chin, frowning with suspicion and one eyebrow raised.
```

## 14. V14 — 시청자: 매수 버튼으로 가는 손목을 붙잡음

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V14.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture. Frame 1: his right arm reaching forward to the right with the index finger extended as if about to press a big button, eager hurried face, leaning forward. Frame 2: his left hand grabs his own right wrist and pulls it back, his body leaning back, eyes wide in surprise at himself. Frame 3: both hands lowered, one hand resting on his chest, letting out a relieved breath with a small calm smile.
```

## 15. V15 — 시청자: 오래 기다리며 지침

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V15.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture. Frame 1: holding a smartphone at chest height in one hand, looking down at it with a flat, waiting expression. Frame 2: looking up and to the upper left as if at a wall clock, tired eyes, the phone still at his chest. Frame 3: shoulders dropped, head hanging slightly, a long sigh, the phone lowered to his waist.
```

## 16. V16 — 시청자: 메모하며 끄덕

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V16.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, three-quarter view facing to the right of the picture, calm and relaxed in the morning. He holds a small blank notepad in his left hand and a pen in his right hand. Frame 1: writing in the notepad, looking down at it, focused, slight smile. Frame 2: the pen paused on the notepad, looking up to the right as if listening to a TV, attentive. Frame 3: a small nod with his eyes closed in a satisfied smile, head tilted slightly down.
```

## 17. V17 — 시청자: 인사

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/V17.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
V, front view facing the camera, warm and friendly. Frame 1: raising his right hand to wave, the palm facing the camera tilted to the left, a bright smile. Frame 2: the same wave with the hand tilted to the right. Frame 3: his right hand resting on his chest and a small polite bow, eyes closed in a gentle smile.
```

## 18. E01 — 전문가: 주먹 외침 (반복)

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E01.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E, front view facing the camera, hyping the market like on TV. Frame 1: his right fist raised high above his head, mouth wide open shouting, eyebrows up, very confident. Frame 2: the right fist pulled down to his shoulder as if winding up, mouth half open, eyes narrowed with a smug grin. Frame 3: his left fist punched forward toward the camera, mouth wide open shouting, the right fist at his side.
```

## 19. E02 — 전문가: 달력판을 탕 침

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E02.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E, front view facing the camera. He holds a large blank desk calendar board (a rectangle with two metal rings on top and a plain empty page with only faint grid lines, no numbers) upright in his left hand beside his body at chest height, the page facing the camera. Frame 1: his right hand raised high, open palm, eyebrows up, about to slam it. Frame 2: his right palm slamming flat onto the calendar page, eyes squeezed, mouth shouting, the board pressed slightly down. Frame 3: pointing his right index finger at the calendar page with a smug wide grin as if saying "mark this date".
```

## 20. E03 — 전문가: 손목시계로 재촉

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E03.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E, front view facing the camera. He wears a wristwatch with a blank face on his left wrist. Frame 1: raising his left wrist to show the watch toward the camera, eyebrows raised urgently. Frame 2: tapping the watch with his right index finger, leaning forward, an urgent pushy face. Frame 3: his left wrist still raised, his right hand waving toward himself in a fast "hurry, come now" gesture, eager grin.
```

## 21. E04 — 전문가: 가슴을 치며 장담

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E04.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E, front view facing the camera. Frame 1: his right fist pulled back beside his shoulder, chin lifted proudly, about to strike. Frame 2: his right fist striking his own chest, eyes closed, chin up, a proud "trust me" expression. Frame 3: giving a big thumbs-up toward the camera with his right hand and winking, smug smile.
```

## 22. E05 — 전문가: 진땀 흘리며 같은 말

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E05.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E, front view facing the camera, sweating. Frame 1: his right fist raised, shouting confidently, but with two drops of sweat on his forehead. Frame 2: his fist still raised, glancing back over his shoulder nervously, a stiff forced smile, more sweat drops. Frame 3: turned back to the camera and shouting even louder with both fists up, eyes squeezed, sweat drops flying off his head.
```

## 23. E06 — 전문가: 어깨 으쓱 (책임 회피)

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E06.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E, three-quarter view facing to the left of the picture (toward someone standing on the left). Frame 1: standing straight with his hands at his sides, a neutral blank face. Frame 2: shrugging — shoulders raised high, both palms turned up at waist height, eyebrows raised, eyes looking away to the upper right. Frame 3: the same shrug with his head tilted, eyes closed, a smug little smile as if saying "not my problem".
```

## 24. E07 — 전문가: 뒤돌아 걸어 나감 (뒷모습 걷기)

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E07.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E seen from behind, walking straight away from the camera into the distance (we see his back, the back of his head and his navy suit jacket). A three-drawing walk cycle: Frame 1: left foot stepping forward (away from us), right arm swinging forward, left arm back. Frame 2: passing pose — feet together under the body, body slightly higher, arms near the body. Frame 3: right foot stepping forward, left arm swinging forward, right arm back. His hands are relaxed; one hand gives a lazy little wave in frame 2.
```

## 25. E08 — 전문가: 계산기 두드리기

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E08.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E, front view facing the camera, serious analyst mode. He holds a calculator with a blank screen in his left hand at chest height. Frame 1: typing on the calculator with his right index finger, looking down at it, concentrating. Frame 2: his finger paused, looking up to the upper left as if checking a monitor, thinking, lips pursed. Frame 3: looking to the right as if at another monitor while typing again, one eyebrow raised.
```

## 26. E09 — 전문가: 수정 구슬을 들여다봄

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E09.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E, front view facing the camera. He holds a crystal ball (clear glass globe, cloudy gray-blue swirls inside, on a small brown stand — the same design as the reference prop). Frame 1: holding the crystal ball in both hands at chest height, looking into it with curiosity. Frame 2: lifting it up close to his face, peering in with one eye squinted, nose almost touching the glass. Frame 3: the crystal ball held in his left hand at his waist, scratching his head with his right hand, a puzzled embarrassed face — he cannot see clearly.
```

## 27. E10 — 전문가: 놀라서 서류를 떨어뜨림

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E10.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E, front view facing the camera. Frame 1: calmly reading a small stack of blank papers held in both hands at chest height. Frame 2: startled — his shoulders jump up, eyes wide, mouth open, and three or four blank sheets fly up out of his hands into the air just above his head (still inside his column). Frame 3: his hands raised empty in front of him, sweating, mouth open in shock, staring forward. No text on the papers.
```

## 28. E11 — 전문가: 판의 선을 지우고 낮게 다시 그림

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E11.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E, three-quarter view facing to the LEFT of the picture, as if standing to the right of a whiteboard that is outside the picture on the left. Frame 1: his right arm raised up and to the left holding a whiteboard eraser, wiping at shoulder height, focused. Frame 2: the same arm lower to the left, wiping at waist height, lips pursed. Frame 3: now holding a marker in his right hand at waist height on the left as if drawing a line lower down, glancing back over his shoulder toward the camera with a calm, matter-of-fact face. Do not draw the whiteboard.
```

## 29. E12 — 전문가: 고무도장을 쾅

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E12.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E, front view facing the camera, cheerful. He holds a big rubber stamp (a round wooden handle on top, a plain rectangular base, the bottom face blank) in his right hand. Frame 1: the stamp raised high above his head, a big grin. Frame 2: slamming the stamp straight down in front of him at waist height (as if onto a desk), his body bending forward with the impact, eyes squeezed. Frame 3: lifting the stamp back up to his shoulder while giving a thumbs-up with his left hand, winking. Do not draw papers or a desk.
```

## 30. E13 — 전문가: 차분하게 짚어 설명

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E13.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E in his calm, honest mode (gentle eyes, relaxed face, no smugness). Frame 1: three-quarter view turned to the LEFT, pointing with his left index finger at something on the left outside the picture (a board), mouth open as if explaining. Frame 2: turned to face the camera, his right hand open with the palm up at chest height, mouth open, explaining kindly. Frame 3: exactly like frame 2 but with his mouth closed in a calm small smile.
```

## 31. E14 — 전문가: 저울을 들고 양쪽을 보여 줌

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E14.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E in his calm, honest mode, front view facing the camera. He holds a brass balance scale (the same design as the reference prop, two empty round pans hanging from a beam) up in front of his chest by its top handle with his right hand. Frame 1: the beam level, both pans at the same height, a calm neutral face. Frame 2: the beam tilted so the LEFT pan hangs lower, his eyebrows raised slightly, looking at the low pan. Frame 3: the beam tilted so the RIGHT pan hangs lower, a calm nod looking at the low pan. Both pans stay empty.
```

## 32. E15 — 전문가: 모르는 건 모른다

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/E15.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장

```
E in his calm, honest mode, front view facing the camera. Frame 1: both palms open and turned up at waist height, an honest gentle smile. Frame 2: the same hands, his eyes closed and his head shaking slightly (tilted to one side), a humble smile as if saying "nobody can know that". Frame 3: his right hand resting on his chest, a small sincere bow, eyes closed, calm.
```

## 33. BG-SIEVE0 — 배경 고치기: 체를 뺀 거름망 무대

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/BG-SIEVE0.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Edit the reference sieve stage picture (BG-SIEVE). Keep the camera, the room, the shelves, the plant, the lamp, the wall, the colors and the light exactly the same, and keep the reddish discard bin on the LEFT and the teal-green open keep box on the RIGHT exactly where they are. Remove only the big sieve, its wooden stand and the metal tray under it: the table top in the middle is now clear and empty, continuing the same wood. Nothing else changes. Full-bleed landscape 1536x864, no people, no text.
```

## 34. BG-STUDIO0 — 배경 고치기: 화살표 없는 스튜디오

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/BG-STUDIO0.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Edit the reference TV studio picture (BG-STUDIO). Keep the camera, the lights, the floor, the desk on the right, the sofa, the plant and all colors exactly the same. Remove only the red rising arrow (and its reflection on the floor) from the big curved video wall: the video wall becomes plain glowing blue panels with soft light, completely empty. Nothing else changes. Full-bleed landscape 1536x864, no people, no text, no numbers, no logos.
```

## 35. PROPS2 — 소품 4

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/PROPS2.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 소품 4

```
Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a similar visual size, each fully inside its column: (1) a small standing photo frame (light wood) holding a picture of a smiling gray-haired elderly couple relaxing side by side in two beach chairs — a dream of a comfortable retirement; (2) a large clear glass jar full of gold coins, its lid off, with a small round sticker showing only a simple picture of a wooden rocking chair (the same jar as in picture 3); (3) a round wall clock with a white face showing only twelve short tick marks — no numbers and NO clock hands; (4) a wall calendar hanging on a nail, with a blank page showing only faint grid lines — no numbers, no words.
```

## 36. FX — 움직임 조각 (투명 · 4×2)

**저장 경로: `stock/source/manspi-jeonmang-2026-11/puppet/motion/FX.png`** — PNG 700KB 이하 · 투명 · 가로 1536×1024 · 조각 8

```
Effects sheet, landscape 1536x1024, a grid of four equal invisible columns and two equal invisible rows (eight cells), one element centered in each cell, fully inside it, each about one third of the cell size. Top row left to right: (1) one shiny gold coin seen from the front (plain, no symbols); (2) the same gold coin seen tilted almost edge-on; (3) one plain paper banknote in soft green with only a simple border pattern — no numbers, no portrait, no words, not any real currency; (4) one light-blue sweat drop. Bottom row left to right: (5) one light-blue tear drop; (6) three short white speed lines with a thin dark outline; (7) one four-pointed yellow sparkle star; (8) one small puff of light gray dust cloud.
```

## 받은 뒤 (Claude)
- main 에서 `stock/source/manspi-jeonmang-2026-11/puppet/motion/` 을 작업 브랜치로 가져와 36장을 확대해 검수: 썸네일·기존 시트와 같은 사람인지 · 그림 속 글자 없음 · 세 장의 발 높이·크기·옷이 같은지 · 손에 든 물건이 세 장에서 같은지 · 33·34번이 원본과 같은 구도인지.
- `puppet/slice.py` 를 v1.1 로 — `motion/` 시트를 칸마다 잘라 `cut/` 에 (세 장은 같은 배율·같은 발 기준점 — 원화 맞춤), 소품 4·조각 8.
- 장면 파일 `video/episodes/manspi-jeonmang-2026-11/index.html` 을 v2.0 으로 다시 짠다:
  - 동작 = 원화 3장을 초당 8~12장으로 바꿔 끼움(1→2→3→2…) + 코드가 예비 동작·튕김·늘었다 줄었다·숨쉬기 · 눈 감은 장으로 눈 깜빡임.
  - 어우러짐 = 배경 앞 물건(소파 팔걸이·탁자·책상 앞판·작업대 앞)을 배경 그림에서 잘라 인물 앞에 겹침(있는 픽셀만) · 발밑 그림자 · 장면 빛에 맞춘 색(밤 = 푸른빛, 스탠드 쪽 따뜻한 빛) · TV 속 전문가는 TV 화면 모양에 맞춰 넣고 화면 빛이 방에 번짐.
  - 글자 칸 없음 — '전 재산' = 저금통에서 동전이 휴대전화로 쏟아짐 · '은퇴 자금' = 노부부 사진 옆 유리병이 비어 감 · '밤마다' = 시계가 돌고 방이 밤으로 바뀌며 같은 동작이 되풀이됨.
  - 숫자·BUY·화살표·그래프만 코드 (빈 판·빈 화면 위 원근에 맞춰).
- 배치 점검 `node video/scripts/layout-check.mjs manspi-jeonmang-2026-11` 문제 0 → `render.mjs check` → 미리보기 렌더 → 완성 mp4 를 Claude 가 직접 본 뒤 사용자에게.
