# 주인공 고정 그림 3장 — ChatGPT용 (읽고 1번부터 차례로 모두 만들어 저장소에 올리기)

이 파일 판: v1.0 — 2026-10-21 12:59 UTC (KST 21:59). 사람이 고치는 파일 — 인물 설명은 `stock/story/protagonist.md` 8번과 같아야 한다.

쓰임: 주식 이야기 영상의 주인공 **구본석**(가상 인물)을 모든 영상·장면에서 **같은 얼굴·머리·옷**으로 그리기 위한 기준 그림이다. 영상에 바로 쓰지 않는다. 앞으로 장면 그림을 그릴 때 이 그림을 함께 보고 똑같이 그린다.

| 번호 | 그림 | 크기 | 저장 경로 |
|---|---|---|---|
| 1 | 인물 설정표 (앞·비스듬히·옆·뒤) | 가로 16:9 (1536×864) | `stock/story/images/protagonist_sheet.jpg` |
| 2 | 표정 6개 | 가로 16:9 (1536×864) | `stock/story/images/protagonist_faces.jpg` |
| 3 | 기준 얼굴 (가슴 위) | 정사각 1:1 (1024×1024) | `stock/story/images/protagonist_portrait.jpg` |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다.** 이 대화에서 예전에 읽은 인물·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '이 파일 판' 줄을 그대로 적는다. **올리는 파일은 모두 JPEG(.jpg) 700KB 이하** (8번).
1. 아래 3장을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 그대로** 쓴다.
3. **3장 모두 같은 사람이다.**
   - 2·3번은 1번 그림의 얼굴·머리·안경·옷과 똑같이 그린다.
   - 알아보는 표시 세 가지는 모든 장에 있어야 한다: 검은 각진 얇은 안경 · 회색빛 남색 작업 점퍼 · 정수리의 뻗친 머리 한 가닥.
4. 크기는 표의 '크기'대로 그린다. 안 되면 가장 가까운 같은 방향(가로·정사각) 크기로 그린다.
5. **그림 속 글자·숫자·기호·로고·워터마크는 하나도 없다.** 점퍼에도 회사 로고나 이름표가 없다.
6. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다. 표정은 프롬프트에 적힌 그대로 그린다.
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `1. stock/story/images/protagonist_sheet.jpg`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. **GitHub 앱으로 장마다 그 경로에 커밋한다** — 이 계정의 ChatGPT 는 저장소에 파일을 올릴 수 있다 (2026-10-19 사용자 확인).
     - 커밋 메시지: `[주인공] 구본석 <파일 이름> 그림`.
     - 파일 이름·폴더는 저장 경로와 한 글자도 다르지 않게.
     - 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다 (Claude 가 그 목록으로 검수).
   - **올리기 전에 JPEG(.jpg)로 바꿔 700KB 이하로 만든다.**
     - 파이썬(PIL)으로 RGB·크기 그대로·품질 90부터 5씩 낮춰, 700KB 아래가 될 때까지 저장한다.
     - 까닭: GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다 (2026-10-19 PNG 4장이 786,444바이트에서 잘려 열리지 않음).
     - 올린 뒤 GitHub 에 있는 그 파일의 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
   - **올리기가 실패한 장만** (권한·연결 오류) 묻지 말고 이렇게 한다:
     1. 그 그림을 번호 순서대로 다시 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 저장 경로의 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/story/images 에 끌어다 놓고 Commit changes"

## 그림체 (모든 장 공통 — 프롬프트에 이미 들어 있음)

Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.

## 인물

- **구본석 (주인공, 44세 중소기업 차장 · 개미 투자자 6년 반)** — Gu Bonseok — Korean man, 44 years old; average height with a slightly soft build and a small belly; short neat black hair parted on the left with a few gray strands at the temples and one small cowlick at the crown; slightly tired kind eyes with faint dark circles; thin black rectangular-frame glasses; clean-shaven; wears a gray-navy zip-up work jacket with no logo over a light blue collared shirt, dark gray slacks and black sneakers.

## 1. 인물 설정표 — 앞·비스듬히·옆·뒤 (전신)

**저장 경로: `stock/story/images/protagonist_sheet.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

크기: 가로 16:9 (1536×864)

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
A character reference sheet (turnaround) of ONE man drawn four times side by side in a row, evenly spaced, same size, full body from head to shoes, standing straight with arms relaxed: 1) front view, 2) three-quarter view facing left, 3) side profile facing left, 4) back view.
The man: Gu Bonseok — Korean man, 44 years old; average height with a slightly soft build and a small belly; short neat black hair parted on the left with a few gray strands at the temples and one small cowlick at the crown; slightly tired kind eyes with faint dark circles; thin black rectangular-frame glasses; clean-shaven; wears a gray-navy zip-up work jacket with no logo over a light blue collared shirt, dark gray slacks and black sneakers.
All four figures are exactly the same person with the same face, hair, glasses, clothes and colors. Calm neutral expression with a faint polite smile.
Plain light warm-gray background, soft even studio lighting, a soft shadow under each figure. 16:9 landscape (1536x864).
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture. Do not write names, labels or arrows.
```

## 2. 표정 6개 — 가슴 위 (2줄 × 3칸)

**저장 경로: `stock/story/images/protagonist_faces.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

크기: 가로 16:9 (1536×864)

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
An expression sheet of ONE man: six chest-up portraits arranged in a neat grid of 2 rows x 3 columns, same size, each on its own plain soft pastel background panel separated by thin white gaps. Exactly the same person in all six — same face, hair, glasses and clothes as described:
Gu Bonseok — Korean man, 44 years old; slightly soft build; short neat black hair parted on the left with a few gray strands at the temples and one small cowlick at the crown; slightly tired kind eyes with faint dark circles; thin black rectangular-frame glasses; clean-shaven; gray-navy zip-up work jacket with no logo over a light blue collared shirt.
Top row, left to right:
1) Neutral — calm, slight polite smile, looking at the viewer.
2) Crushed despair after seeing his huge investment loss — head bowed, one hand pressed against his forehead, eyes squeezed shut, brows knitted, shoulders slumped.
3) Frustrated and stuck — a heavy sigh with puffed cheeks, eyes half-closed, rubbing his temple with two fingers.
Bottom row, left to right:
4) Determined — lips pressed together, eyes looking straight ahead with quiet resolve, fist lightly clenched at chest height.
5) Focused studying — looking down at an open notebook with blank pages, holding a pen, brows slightly raised in concentration.
6) Relieved warm smile — shoulders relaxed, eyes soft, a gentle hopeful smile.
Soft even lighting. 16:9 landscape (1536x864).
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — the notebook pages are blank. Do not write names, labels or numbers on the panels.
```

## 3. 기준 얼굴 — 가슴 위 한 사람 (정사각)

**저장 경로: `stock/story/images/protagonist_portrait.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

크기: 정사각 1:1 (1024×1024)

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
A single chest-up portrait of the same man, three-quarter view turned slightly to the left, looking at the viewer, centered and large in the frame with his head in the upper middle:
Gu Bonseok — Korean man, 44 years old; slightly soft build; short neat black hair parted on the left with a few gray strands at the temples and one small cowlick at the crown; slightly tired kind eyes with faint dark circles; thin black rectangular-frame glasses; clean-shaven; gray-navy zip-up work jacket with no logo over a light blue collared shirt.
Expression: tired but quietly determined — a small hopeful smile, eyes steady.
Background: a soft blurred evening kitchen of a modest Korean apartment, warm lamp light on his face. 1:1 square (1024x1024).
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture.
```
