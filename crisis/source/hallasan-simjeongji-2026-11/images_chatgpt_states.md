# hallasan-simjeongji-2026-11 — 움직이는 실루엣용 상태 그림 20장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.0 — 2026-11-26 — 사용자 지시 "그리고 지금 영상이 고정 이미지만 나오잖아 검은색 실루엣이 움직이는 효과 내도록 따로 여러 상태 이미지 생성해야지 다른 이외에 것도 필요한 상태별 이미지 생성하고 다시 이미지 생성 명령 알려줘" — 대본 v3.2 (`hallasan-simjeongji-2026-11.txt`).

**어떻게 쓰는가 — 배경 위를 실루엣이 움직임**
- **실루엣 시트 (1~11번)**: 흰 바탕 한 장에 같은 인물의 동작을 칸마다 하나씩(걷기 한 바퀴 · 멈춤 · 가슴에 손 · 돌아섬 · 신고 · 수색 · 가슴 압박…). 한 장 안에서 그려야 칸끼리 같은 사람으로 보인다. Claude 가 흰 바탕을 지워 **투명한 검은 실루엣**으로 바꾸고, 영상에서 칸을 차례로 바꿔 보여 주며(1초에 8번 안팎) 배경 위를 옮겨 **걷고·멈추고·돌아서는 움직임**을 만든다.
- **의학 상태 시트 (12번)**: 혈관이 좁아지는 단계 · 찬 공기 · 끈끈한 피 — 칸을 차례로 겹쳐 바뀌는 모습으로.
- **배경판 (13~20번)**: 사람이 없는 **옆에서 본** 장면 — 실루엣이 걸어갈 **평평한 길 선**이 정해진 높이에 가로로(경사 길은 정해진 기울기로) 놓인다. 실루엣이 역광으로 검게 보이도록 빛은 뒤에서.
- 이미 있는 24장(`images_chatgpt.md` v1.0)은 그대로 함께 쓴다 (통계 배경·의학 그림·구급차 등).
- ※ 안전 교육 영상(연구·교육용) — 의학적 진단이 아니다. 피·상처·시신·공포 연출 없음. 실제 사건의 김 씨(가명)·일행·구조대원을 닮게 그리지 않는다(재연).

| 번호 | 저장 경로 (모두 `crisis/source/hallasan-simjeongji-2026-11/` 아래) | 칸 | 무엇 | 대본 (v3.2 장) |
|---|---|---|---|---|
| 1 | `images/SIL-01-KIM-WALK.jpg` | 3×2 | 김 씨 걷기 한 바퀴 6단계 (오른쪽으로) | 1장 산행 · 마무리 |
| 2 | `images/SIL-02-KIM-STATES.jpg` | 3×2 | 김 씨 상태 변화: 걷기 → 멈춤·가슴에 손 → 무릎 짚음 → 일행에게 손 들어 말함 → 돌아섬 → 고개 숙이고 왼쪽으로 | 2장 결정 |
| 3 | `images/SIL-03-KIM-WALK-BACK.jpg` | 3×2 | 김 씨 혼자 천천히 돌아가는 걷기 6단계 (왼쪽으로, 고개 숙임) | 2장 · 6장 혼자 |
| 4 | `images/SIL-04-COMP-WALK.jpg` | 2×2 | 일행 셋이 함께 걷기 4단계 (오른쪽으로) | 1장 · 2장 · 마무리 |
| 5 | `images/SIL-05-COMP-STATES.jpg` | 2×2 | 일행: 뒤돌아봄 · 두리번 · 휴대폰으로 신고 · 숲을 가리킴 | 2장 · 3장 신고 |
| 6 | `images/SIL-06-RESCUER.jpg` | 3×2 | 구조대원 수색 걷기 4단계 · 무전 · 가리키며 부름 | 3장 수색 |
| 7 | `images/SIL-07-STRETCHER.jpg` | 2×2 | 구조대원 둘이 담요 덮인 들것을 들고 빠르게 걷기 4단계 (왼쪽으로) | 3장 |
| 8 | `images/SIL-08-SIGNS.jpg` | 3×2 | 등산객의 몸 신호: 걷기 · 가슴에 손 · 명치에 손 · 팔·어깨 문지름 · 이마 땀 · 바위에 앉아 쉼 | 도입 · 5장 신호 · 9장 |
| 9 | `images/SIL-09-SLOPE.jpg` | 3×2 | 등산객 오르막 3단계 (오른쪽) + 내리막 3단계 (왼쪽) | 8장 반복 사례 |
| 10 | `images/SIL-10-CPR.jpg` | 2×2 | 가슴 압박 위·아래 (번갈아 = 압박) · 신고하며 곁에 · 자동심장충격기 들고 달려옴 | 6장 · 9장 |
| 11 | `images/SIL-11-PREP.jpg` | 3×2 | 산행 전 점검: 혈압 재기 · 진료 상담 · 배낭 싸기 · 날씨 확인 · 가족에게 전화 · 물 마시기 | 9장 점검 |
| 12 | `images/MED-S-STATES.jpg` | 3×2 | 의학 상태: 혈관 단면 정상 → 좁아짐 → 피떡 · 혈관 보통 → 찬 공기에 좁아짐 · 끈끈한 피 | 4장 이유 |
| 13 | `images/PLT-01-TRAIL-SIDE.jpg` | 배경 | 옆에서 본 평평한 둘레길 (한낮 · 길 선 가로) | 도입 · 1·2·5·6·9장 · 마무리 |
| 14 | `images/PLT-02-ENTRANCE-SIDE.jpg` | 배경 | 옆에서 본 둘레길 입구 공터 (이른 오후) | 3장 신고 |
| 15 | `images/PLT-03-SEARCH-SIDE.jpg` | 배경 | 옆에서 본 숲 안쪽 덤불 (늦은 오후 빛) | 3장 수색 |
| 16 | `images/PLT-04-SLOPE-UP.jpg` | 배경 | 옆에서 본 초봄 돌길 오르막 (오른쪽으로 오름) | 8장 2025년 3월 |
| 17 | `images/PLT-05-SLOPE-DOWN.jpg` | 배경 | 옆에서 본 늦가을 하산길 (왼쪽으로 내려감) | 8장 2026년 10월 |
| 18 | `images/PLT-06-CLEARING.jpg` | 배경 | 숲길 옆 평평한 빈터 (응급처치 장면 자리) | 6장 · 9장 |
| 19 | `images/PLT-07-CLINIC.jpg` | 배경 | 옆에서 본 밝은 진료실 (빈 의자 둘) | 9장 첫째 점검 |
| 20 | `images/PLT-08-LIVING.jpg` | 배경 | 옆에서 본 산행 전날 밤 거실 (탁자에 배낭) | 9장 둘째~넷째 점검 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트(다른 편의 웹툰·만화·종이 인형극·실사 사진, 이 편의 1~24번 재연 사진 포함)가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성:' 줄을 그대로 옮겨 적어, 지금 읽은 판이 맞는지 보이게 한다.
1. 아래 1~20번 **20장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 앞에 아래 블록을 이 순서로 붙인다.
   - **실루엣 시트(1~11번)**: 실루엣 시트 화풍 → 인물 윤곽 → 프롬프트.
   - **의학 상태 시트(12번)**: 의학 시트 화풍 → 프롬프트.
   - **배경판(13~20번)**: 다큐 재연 화풍 → 프롬프트. (배경판에는 사람·동물이 하나도 없다.)
3. **실루엣 시트는 그림이 아니라 '부품'이다** — 영상에서 칸을 잘라 차례로 바꿔 보여 준다. 그래서 반드시:
   - 바탕은 **완전한 흰색 하나**(#FFFFFF) — 바닥선·그림자·질감·테두리·칸 나눔 선 없음.
   - 사람(과 들것·바위·상자 같은 물건)은 **완전한 검정 하나**(#000000)로 칠한 실루엣 — 안쪽 선·회색 음영·하이라이트·얼굴 없음. 바깥 윤곽만으로 모자·배낭·자세가 보이게.
   - 칸(보이지 않는 격자)마다 **정확히 한 동작**, 칸 가운데, 칸 가장자리에서 40픽셀 넘게 떨어지고 옆 칸과 닿거나 겹치지 않는다.
   - **같은 인물은 모든 칸에서 크기가 같고 발바닥이 같은 높이**(칸 높이의 90% 선)에 — 칸을 바꿔도 사람이 튀거나 커졌다 작아졌다 하지 않게.
   - 걷기 칸은 **번호 순서대로 이어 보면 걷는 한 바퀴**가 되게 (다리가 엇갈리는 차례를 지킨다).
   - 하나라도 어기면(회색 바탕·그림자·얼굴·칸이 붙음·크기가 다름) 그 장은 다시 만든다.
4. **배경판은 옆에서 본 장면** — 카메라가 길 옆에 서서 길을 똑바로 가로질러 본다. 프롬프트가 정한 높이(그림 높이의 몇 %)에 길 선이 놓이고, 그 선 위에는 돌·뿌리·나뭇가지 없이 비워 둔다(실루엣이 걸어갈 자리). 13~15·18번은 같은 둘레길 숲(제주 중산간 삼나무·화산석·고사리)으로 보이게. 빛은 뒤쪽에서 — 길 위에 사람이 서면 역광 실루엣이 되도록.
5. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 안내판·휴대폰 화면·모니터·상자에도 없음 (빈 판이나 단순한 모양만). 만든 뒤 확대해 글자처럼 보이는 것이 있으면 다시 만든다.
   **피·상처·시신·공포 연출 없음** — 응급처치 칸(10번)의 누운 사람은 차분한 단순 실루엣, 들것(7번) 위는 담요로 덮인 매끈한 형체만.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. crisis/source/hallasan-simjeongji-2026-11/images/SIL-01-KIM-WALK.jpg`). 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게 — 모두 `crisis/source/hallasan-simjeongji-2026-11/images/`).
   - **JPEG `.jpg` · RGB · 700KB 이하** — 크기는 **시트(1~12번) 1536×1024 · 배경판(13~20번) 1536×864**. 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장한다 (GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다). **시트는 자르지 않는다**(칸이 잘림) — 크기가 다르면 비율을 지켜 줄이고 남는 곳을 흰색(12번은 그림 바탕색)으로 채운다. 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     ```python
     from PIL import Image
     import os
     def save_jpg(src, dst, size, sheet, pad=(255, 255, 255), limit=700_000):
         W, H = size
         im = Image.open(src).convert("RGB")
         if im.size != (W, H):
             w, h = im.size
             if sheet:   # 시트: 자르지 않고 맞춰 넣음
                 s = min(W / w, H / h)
                 im2 = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
                 im = Image.new("RGB", (W, H), pad)
                 im.paste(im2, ((W - im2.width) // 2, (H - im2.height) // 2))
             else:       # 배경판: 가운데를 잘라 맞춤
                 s = max(W / w, H / h)
                 im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
                 l, t = (im.width - W) // 2, (im.height - H) // 2
                 im = im.crop((l, t, l + W, t + H))
         q = 90
         while True:
             im.save(dst, "JPEG", quality=q, optimize=True, progressive=True)
             if os.path.getsize(dst) <= limit or q <= 50: break
             q -= 5
         print(dst, os.path.getsize(dst), im.size, "q", q)
     # 시트: save_jpg(src, dst, (1536, 1024), True)   · 12번은 pad=(8, 14, 32)
     # 배경판: save_jpg(src, dst, (1536, 864), False)
     ```
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[crisis] hallasan-simjeongji-2026-11 <파일 이름> 이미지` (예: `[crisis] hallasan-simjeongji-2026-11 SIL-01-KIM-WALK.jpg 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 실루엣 시트 화풍 (1~11번 — 맨 앞에 그대로 붙임)

```
SPRITE-SHEET STYLE: a clean production sprite sheet of human silhouettes for a documentary animation. Canvas exactly 1536x1024, landscape. Background: one flat pure white (#FFFFFF) everywhere — no floor, no ground line, no cast shadow, no gradient, no texture, no vignette, no frame, no grid lines, no borders. Every figure and every object is one solid flat pure black (#000000) shape with crisp clean edges — no inner lines, no gray shading, no highlights, no face, no visible clothing details inside the shape; only the outer outline shows the cap, clothing, backpack and posture. Realistic adult human proportions (about 7.5 heads tall) and natural, believable posture like a real person filmed from the side — not cartoon, not chibi, not a stick figure. The canvas is divided into an invisible grid of equal cells (the grid is NOT drawn). Each cell holds exactly one pose (one figure, or one small group when described), centered horizontally in its cell, fully inside the cell with at least 40 pixels of white margin on every side, never touching or overlapping a neighboring cell. In every cell the same character is drawn at exactly the same size, and the soles of the feet rest on the same invisible horizontal line at 90% of the cell height (sitting, kneeling or lying poses rest on that same line). Absolutely no text, letters, numbers, labels, arrows, logos or watermarks.
```

## 인물 윤곽 (실루엣 시트 — 실루엣 시트 화풍 다음에 그대로 붙임)

```
CHARACTERS (outline only — keep each one identical in every cell and on every sheet):
KIM — a Korean man in his 50s, medium build, a plain baseball cap, a zip-up outdoor jacket, straight trousers, hiking shoes, a small daypack on his back, no hiking poles.
COMPANIONS — three hikers in their 50s: two men and one woman, outdoor jackets, small daypacks; the taller man wears a wide-brimmed hiking hat; the woman has shoulder-length hair tied back.
RESCUER — a Korean mountain rescue worker: a rounded rescue helmet, a fitted uniform jacket and trousers, boots, a medium rescue backpack.
HIKER — an anonymous adult hiker with a cap and a daypack; a single trekking pole only where described.
```

## 의학 시트 화풍 (12번 — 맨 앞에 그대로 붙임)

```
STYLE-MED-SHEET: a clean, realistic 3D medical visualization for a TV health documentary, laid out as a sheet of six panels. Canvas exactly 1536x1024, landscape, one continuous deep navy-to-black background (no lines, frames or gaps drawn between panels). The canvas is divided into an invisible grid of 3 columns x 2 rows (cells 512x512); each panel's subject is centered in its cell with dark margin around it and never touches a neighboring cell. Soft rim light and gentle glow, realistic tissue rendered tastefully (not bloody, not gory), red tones for blood, warm yellow for fatty deposits, cool blue for cold. The same camera angle, scale and lighting in panels that show the same subject, so that switching between them looks like one thing changing. Absolutely no text, labels, arrows, numbers, logos or watermarks.
```

## 다큐 재연 화풍 (배경판 13~20번 — 맨 앞에 그대로 붙임)

```
STYLE: a photorealistic documentary reenactment still, like a frame from a serious Korean TV news report or investigative documentary. Full-bleed landscape 1536x864, cinematic 16:9 composition, eye-level or slightly low camera, shallow depth of field, natural light only, calm and slightly dark muted colors with low saturation, soft contrast, a subtle film grain. Setting: Korea — Jeju island's mid-mountain forests and Korean mountain trails — but no identifiable real landmark. The mood is quiet, serious and respectful, never horror or action-movie drama. Absolutely no text, letters, numbers, logos, emblems or watermarks anywhere: trail signs, direction posts, vehicles, uniforms, phone screens, papers and medicine packets are blank or show only plain shapes. No blood, no injuries, no dead body, nothing gruesome.
```

## 1. SIL-01-KIM-WALK — 김 씨 걷기 한 바퀴 (1장 · 마무리)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-01-KIM-WALK.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 3 columns x 2 rows, each cell 512x512. Cell order: top row left to right = 1, 2, 3; bottom row left to right = 4, 5, 6.
KIM walking at an easy pace on flat ground, seen exactly from the side, facing RIGHT. One complete walking cycle split into six phases, so that showing the cells in order 1 to 6 and repeating looks like smooth walking:
1 — right heel touching down in front, left leg behind, left arm forward and right arm back.
2 — weight on the right leg, body slightly lowered, left foot lifting off behind.
3 — left leg swinging past the right leg, body upright, arms near the sides.
4 — left heel touching down in front, right leg behind, right arm forward and left arm back.
5 — weight on the left leg, body slightly lowered, right foot lifting off behind.
6 — right leg swinging past the left leg, body upright, arms near the sides.
Same size and the same head height in all six cells.
```

## 2. SIL-02-KIM-STATES — 김 씨의 상태 변화 (2장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-02-KIM-STATES.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 3 columns x 2 rows, each cell 512x512. Cell order: top row left to right = 1, 2, 3; bottom row left to right = 4, 5, 6.
KIM's changing condition on a flat forest trail, seen from the side, the same size in every cell:
1 — walking normally, facing RIGHT, mid-step.
2 — stopped, facing RIGHT, shoulders slightly lowered, one hand pressed flat on the center of his chest.
3 — stopped, facing RIGHT, bent forward with one hand on his knee, head lowered, catching his breath.
4 — standing upright again, facing RIGHT, one hand raised to shoulder height as if telling the people ahead of him something.
5 — turning around: body now facing LEFT, taking the first step toward the left, head slightly down.
6 — walking toward the LEFT, head down, shoulders slumped, a slow heavy step.
```

## 3. SIL-03-KIM-WALK-BACK — 김 씨 혼자 천천히 돌아가는 걷기 (2장 · 6장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-03-KIM-WALK-BACK.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 3 columns x 2 rows, each cell 512x512. Cell order: top row left to right = 1, 2, 3; bottom row left to right = 4, 5, 6.
KIM walking alone, slowly, back the way he came, seen exactly from the side, facing LEFT. Head slightly lowered, shoulders a little slumped, short tired steps. One complete slow walking cycle in six phases, so that showing the cells in order 1 to 6 and repeating looks like slow walking:
1 — left heel touching down in front, right leg behind.
2 — weight on the left leg, right foot lifting off behind.
3 — right leg swinging past the left leg.
4 — right heel touching down in front, left leg behind.
5 — weight on the right leg, left foot lifting off behind.
6 — left leg swinging past the right leg.
Same size and the same head height in all six cells.
```

## 4. SIL-04-COMP-WALK — 일행 셋이 함께 걷기 (1장 · 2장 · 마무리)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-04-COMP-WALK.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 2 columns x 2 rows, each cell 768x512. Cell order: top row left to right = 1, 2; bottom row left to right = 3, 4.
The three COMPANIONS walking together on flat ground in a loose single line, seen exactly from the side, all facing RIGHT, slightly overlapping in depth but each outline still readable. The same order in every cell: the woman in front, the man with the wide-brimmed hat in the middle, the other man last. Four phases of a relaxed walking cycle, so that showing the cells in order 1 to 4 and repeating looks like the group walking:
1 — each person's right leg reaching forward.
2 — legs passing each other, bodies upright.
3 — each person's left leg reaching forward.
4 — legs passing each other, bodies upright.
Same size in all four cells.
```

## 5. SIL-05-COMP-STATES — 일행: 뒤돌아봄 · 두리번 · 신고 · 가리킴 (2장 · 3장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-05-COMP-STATES.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 2 columns x 2 rows, each cell 768x512. Cell order: top row left to right = 1, 2; bottom row left to right = 3, 4.
The three COMPANIONS in four moments, seen from the side, the same size as when walking:
1 — all three have stopped and turned their heads and shoulders back to look toward the LEFT, behind them.
2 — standing in place and looking around in different directions; the man with the hat shades his eyes with one hand.
3 — the woman holds a phone to her ear, calling for help; the two men stand beside her looking around.
4 — the man with the hat points with an outstretched arm toward the LEFT, into the forest; the other two turn to look where he points.
```

## 6. SIL-06-RESCUER — 구조대원 수색 (3장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-06-RESCUER.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 3 columns x 2 rows, each cell 512x512. Cell order: top row left to right = 1, 2, 3; bottom row left to right = 4, 5, 6.
One RESCUER searching a forest, seen from the side, the same size in every cell.
Cells 1 to 4 — a careful searching walk facing RIGHT, body leaning slightly forward, head turned a little as if scanning the bushes; shown 1 to 4 and repeated it looks like walking: 1 right foot forward, 2 legs passing, 3 left foot forward, 4 legs passing.
5 — standing still, facing RIGHT, holding a small radio near the side of the helmet, talking into it.
6 — facing RIGHT, one arm stretched out pointing low and ahead, the other hand cupped beside the mouth, calling to colleagues.
```

## 7. SIL-07-STRETCHER — 담요 덮인 들것을 든 구조대원 둘 (3장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-07-STRETCHER.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 2 columns x 2 rows, each cell 768x512. Cell order: top row left to right = 1, 2; bottom row left to right = 3, 4.
Two RESCUERS carrying a rescue stretcher between them, walking quickly to the LEFT, seen exactly from the side. On the stretcher is a smooth shape completely covered by a blanket — nothing else visible. Four phases of a quick, steady walking cycle, so that showing the cells in order 1 to 4 and repeating looks like steady carrying:
1 — the front rescuer's left foot forward, the back rescuer's right foot forward.
2 — legs passing.
3 — the front rescuer's right foot forward, the back rescuer's left foot forward.
4 — legs passing.
The stretcher stays level and at the same height in all four cells.
```

## 8. SIL-08-SIGNS — 등산객의 몸이 보내는 신호 (도입 · 5장 · 9장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-08-SIGNS.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 3 columns x 2 rows, each cell 512x512. Cell order: top row left to right = 1, 2, 3; bottom row left to right = 4, 5, 6.
One HIKER (no trekking pole) on a trail showing warning signs of the body, seen from the side, facing RIGHT, the same person and size in every cell:
1 — walking normally, mid-step.
2 — stopped, one hand pressed on the center of the chest, shoulders tense.
3 — one hand pressed on the upper stomach just below the chest, body bent slightly forward.
4 — rubbing the left upper arm and shoulder with the right hand, head tilted.
5 — wiping the forehead with the back of one hand, chest lifted, breathing hard.
6 — sitting on a low rock (the rock is also a solid black shape), resting, both hands on the knees.
```

## 9. SIL-09-SLOPE — 오르막·내리막 등산객 (8장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-09-SLOPE.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 3 columns x 2 rows, each cell 512x512. Cell order: top row left to right = 1, 2, 3; bottom row left to right = 4, 5, 6.
One HIKER with one trekking pole, seen from the side, the same person and size in every cell.
Top row (cells 1 to 3) — climbing a steep uphill path, facing RIGHT, body leaning forward, the pole planted ahead; three phases of a slow climbing step: 1 right foot stepping up, 2 legs passing, 3 left foot stepping up. Keep the feet on the cell's 90% line even though the posture shows climbing.
Bottom row (cells 4 to 6) — walking down a steep path, facing LEFT, body leaning slightly back, knees bent, the pole planted ahead and below; three phases of a careful downhill step: 4 left foot reaching down, 5 legs passing, 6 right foot reaching down.
```

## 10. SIL-10-CPR — 가슴 압박 · 신고 · 자동심장충격기 (6장 · 9장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-10-CPR.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 2 columns x 2 rows, each cell 768x512. Cell order: top row left to right = 1, 2; bottom row left to right = 3, 4.
A first-aid scene for a public safety lesson, seen exactly from the side. In every cell: a person lying flat on the back on the ground, head to the LEFT, calm and simple (no injury, no detail), and a HIKER kneeling beside the chest. Both are solid black silhouettes; the same size and position in all four cells.
1 — the kneeling helper's arms straight and locked, both hands stacked on the center of the lying person's chest, shoulders directly above the hands, body high (the top of a chest compression).
2 — exactly the same, but the helper's shoulders pushed a little lower with the arms still straight (the bottom of a chest compression). Cells 1 and 2 alternate to show chest compressions.
3 — the helper kneeling beside the chest, one hand resting on the lying person's shoulder, the other hand holding a phone to the ear (calling for help).
4 — the helper compressing as in cell 1, while a second HIKER runs in from the RIGHT carrying a small boxy case with a handle (a defibrillator case — plain, no symbols).
```

## 11. SIL-11-PREP — 산행 전 점검하는 사람 (9장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-11-PREP.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 3 columns x 2 rows, each cell 512x512. Cell order: top row left to right = 1, 2, 3; bottom row left to right = 4, 5, 6.
Everyday preparation before a mountain hike, seen from the side. One adult in casual clothes (no cap) as a solid black silhouette, with simple objects that are also solid black shapes; the same person and size in every cell:
1 — sitting at a small table with a blood-pressure cuff on the upper arm, a small monitor box on the table.
2 — sitting on a chair, facing RIGHT, talking with a doctor who sits across a small desk on the right (the doctor wears a knee-length coat).
3 — kneeling beside an open daypack, putting in a water bottle and a jacket.
4 — standing, looking down at a phone held in one hand (checking the weather).
5 — standing, a phone held to the ear, the other hand gesturing while talking (telling family the route and the return time).
6 — standing with a daypack on, drinking from a water bottle.
```

## 12. MED-S-STATES — 혈관이 좁아지고 피가 끈끈해지는 단계 (4장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/MED-S-STATES.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 3 columns x 2 rows, each cell 512x512. Cell order: top row left to right = 1, 2, 3; bottom row left to right = 4, 5, 6.
Top row — the same cross-section of a heart artery, the same size, angle and lighting in all three panels, seen straight on as a round tube cut open:
1 — healthy: a wide, round, open channel with red blood cells flowing through it.
2 — the same artery with a thick, warm yellowish fatty layer built up on the inner wall, the open channel clearly narrowed.
3 — the same narrowed artery with a dark red blood clot filling most of the remaining channel.
Bottom row:
4 — a short straight artery segment seen from the side, horizontal, normal width, red blood inside.
5 — exactly the same segment, visibly squeezed narrower along its length, with a faint cold blue frosty haze around it (cold air tightening the vessel).
6 — a close view inside a vessel crowded densely with red blood cells, packed together and moving slowly (blood thickened by losing water).
```

## 13. PLT-01-TRAIL-SIDE — 옆에서 본 평평한 둘레길 (도입 · 1·2·5·6·9장 · 마무리)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/PLT-01-TRAIL-SIDE.jpg`** — JPEG 700KB 이하 · 1536×864

```
Side view of a flat Jeju mid-mountain forest trail at about 700 meters above sea level, early spring, around midday. The camera stands beside the path and looks straight across it, so the packed-earth path runs perfectly horizontally from the left edge to the right edge of the picture: the near edge of the path at about 82% of the image height and the far edge at about 72%, flat and level — people will be added walking along it later. Behind the path: tall Japanese cedar trunks and leafless broadleaf trees; moss-covered black volcanic stones, ferns and low bamboo grass along both edges. Soft overcast light coming from behind the trees, so that anything standing on the path would be backlit. Keep the walking line on the path clear: no stones, roots or branches on it. No people, no animals.
```

## 14. PLT-02-ENTRANCE-SIDE — 옆에서 본 둘레길 입구 공터 (3장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/PLT-02-ENTRANCE-SIDE.jpg`** — JPEG 700KB 이하 · 1536×864

```
Side view of the trailhead at the edge of the same Jeju mid-mountain forest, early afternoon. A small open gravel area: the forest begins on the left third of the picture (cedar trunks, the dark mouth of the trail), and an open grassy field with a pale sky fills the right side. A plain wooden post with a blank board stands at the forest edge. The flat ground runs horizontally across the whole picture at about 82% of the image height, clear for people to be added standing on it later. Brighter sky behind, soft backlight. No people, no cars, no animals.
```

## 15. PLT-03-SEARCH-SIDE — 옆에서 본 숲 안쪽 덤불 (3장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/PLT-03-SEARCH-SIDE.jpg`** — JPEG 700KB 이하 · 1536×864

```
Side view deep inside the same Jeju forest in mid-afternoon, away from the main path: dense low bamboo grass and shrubs, cedar trunks, mossy black volcanic rocks. A narrow, faint footpath runs horizontally across the picture at about 84% of the image height, clear for figures to be added walking on it. Long shafts of light fall through the trees from the upper right, a slightly warmer late light, a quiet feeling of searching. No people, no animals, nothing lying on the ground.
```

## 16. PLT-04-SLOPE-UP — 옆에서 본 초봄 돌길 오르막 (8장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/PLT-04-SLOPE-UP.jpg`** — JPEG 700KB 이하 · 1536×864

```
Side view of a stony mountain trail in early spring on a cold, windy morning. The camera looks straight across a steep path paved with black volcanic stones that rises in one straight line from the lower left (about 86% of the image height at the left edge) to the upper right (about 60% of the image height at the right edge), clear for a climbing figure to be added later. Bare low shrubs and windswept dwarf trees around the path, a gray cloudy sky, thin mist, light from the upper right behind the slope. No people.
```

## 17. PLT-05-SLOPE-DOWN — 옆에서 본 늦가을 하산길 (8장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/PLT-05-SLOPE-DOWN.jpg`** — JPEG 700KB 이하 · 1536×864

```
Side view of a late-autumn forest descent on a Korean mountain, on a gray, damp day. The camera looks straight across a stone-and-earth path that falls in one straight line from the upper right (about 60% of the image height at the right edge) down to the lower left (about 86% of the image height at the left edge), clear for a figure walking down toward the left to be added later. Thinning trees with the last red and brown leaves, fallen leaves on both sides of the path, a light drizzle haze, soft light from behind the trees. No people.
```

## 18. PLT-06-CLEARING — 숲길 옆 평평한 빈터 (6장 · 9장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/PLT-06-CLEARING.jpg`** — JPEG 700KB 이하 · 1536×864

```
Side view of a small, flat clearing beside the same Jeju forest trail on a calm afternoon. Level ground with short grass and a few fallen leaves runs horizontally across the picture at about 84% of the image height; the middle of the picture is open, empty space for a first-aid scene to be added later. Cedar trunks and ferns stand softly out of focus behind, gentle light from behind the trees. No people, no objects on the ground.
```

## 19. PLT-07-CLINIC — 옆에서 본 밝은 진료실 (9장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/PLT-07-CLINIC.jpg`** — JPEG 700KB 이하 · 1536×864

```
Side view of a small, clean, bright Korean doctor's consultation room in the daytime: a plain desk with a monitor turned away from the camera, two empty chairs facing each other across the desk, a window with soft daylight behind them. The floor line runs horizontally at about 86% of the image height, with open floor space so that seated people can be added later. Calm, neutral colors. No people, no text on anything.
```

## 20. PLT-08-LIVING — 옆에서 본 산행 전날 밤 거실 (9장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/PLT-08-LIVING.jpg`** — JPEG 700KB 이하 · 1536×864

```
Side view of a quiet Korean apartment living room at night, the evening before a hike: a low wooden table on the right half with a small daypack, a water bottle and a folded outdoor jacket on it; warm lamp light from behind; a window with blurred city night lights. The floor line runs horizontally at about 86% of the image height, with open floor space on the left half where a person can be added later. No people, no text.
```
