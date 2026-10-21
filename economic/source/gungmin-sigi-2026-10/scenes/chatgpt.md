# gungmin-sigi-2026-10 장면 그림 29장 — ChatGPT용 (읽고 1번부터 차례로 모두 만들기)

자동 생성 — `python3 tools/scene_clips.py build` v1.3.0 (2026-10-21 03:03). 이 파일은 고치지 말고 `economic/source/gungmin-sigi-2026-10/scenes/plan.json` 을 고친 뒤 다시 만든다.

이 파일 주소(최신): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/economic/source/gungmin-sigi-2026-10/scenes/chatgpt.md

쓰임: 영상에서 **사연 장면**마다 이 그림을 첫 장면으로 짧은 움직이는 클립(약 2~5초)을 만든다 (Kaggle videogen). 숫자·계산 설명은 Claude 가 코드로 그린 화면이라 여기 없다.

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다.** 답의 첫 줄에 이 파일 맨 위 '자동 생성' 줄의 시각을 그대로 적는다. **올리는 파일은 모두 JPEG(.jpg) 700KB 이하** — 2026-10-20 PNG 37장을 그대로 올렸다가 모두 768KB 에서 잘려 깨졌다 (8번).
1. 먼저 **0번 인물 설정표** 한 장을 만든다 (영상에는 쓰지 않음 — 모든 장면의 얼굴·머리·옷을 맞추는 기준).
2. 그다음 **1번부터 29번까지 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
3. 각 장은 그 칸의 **프롬프트(``` 안)를 그대로** 쓴다. 모든 장이 **같은 그림체·같은 인물**이다 (프롬프트마다 그림체와 그 장의 인물 설명이 들어 있음 — 장마다 다른 얼굴·옷으로 바꾸지 않는다).
4. 크기: **16:9 가로** (1536×864 — 안 되면 가장 넓은 가로형). 얼굴과 중요한 물건은 프롬프트의 'Format' 줄대로 (잘리는 가장자리·자막 자리를 피함).
5. **그림 속 글자·숫자·기호·로고·워터마크는 하나도 없다.** 서류·통장·계산기·화면·간판은 빈칸이나 회색 줄만.
6. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다. 표정·몸짓은 프롬프트에 적힌 그대로 (감정이 작은 화면에서도 보이게).
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `1. economic/source/gungmin-sigi-2026-10/scenes/L01.jpg`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. **GitHub 앱으로 장마다 그 경로에 커밋한다** — 이 계정의 ChatGPT 는 저장소에 파일을 올릴 수 있다 (2026-10-19 사용자 확인). 커밋 메시지 `[장면] gungmin-sigi-2026-10 <이름> 그림`. 파일 이름·폴더는 저장 경로와 한 글자도 다르지 않게. 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다 (Claude 가 그 목록으로 검수).
   - **올리기 전에 JPEG(.jpg)로 바꿔 700KB 이하로 만든다** — 파이썬(PIL)으로 RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장. GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다 (2026-10-19 썸네일 PNG 4장이 786,444바이트에서 잘려 열리지 않음). 올린 뒤 GitHub 에 있는 그 파일의 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
   - **올리기가 실패한 장만** (권한·연결 오류) 묻지 말고: 그 그림을 번호 순서대로 다시 보여 주고(그림마다 위에 번호와 저장 경로), 마지막에 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 그림체 (모든 장 공통 — 프롬프트에 이미 들어 있음)

Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.

## 인물

- **김 씨 (주인공)** — Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- **아들 (취업 준비)** — Mr. Kim's son — Korean man in his late 20s, slim, messy short black hair, light gray hoodie, blue jeans.
- **동창 친구 (모임에서 물은 사람)** — Mr. Kim's old school friend — Korean man aged 60, round cheerful face, short gray crew cut, olive-green jacket over a red-and-white checked shirt.
- **동창 박 씨** — Mr. Park — another school friend, Korean man aged 60, slim and calm, silver hair neatly combed back, beige jacket over a dark brown turtleneck.
- **공단 상담 직원** — Pension office counselor — Korean woman in her 40s, shoulder-length dark hair, white blouse with a navy vest, a blank lanyard card, warm professional smile.

## 장소

- **김 씨 집** — Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
- **동창 모임 식당** — A cozy Korean restaurant: a wooden table with a bubbling stew pot and small side dishes, warm yellow lights, no menu boards or signs.
- **카페** — A quiet, bright café with a window seat, a wooden table and coffee cups.
- **국민연금공단 지사** — A clean, bright public pension office: service counters with clear glass partitions, potted plants, rows of waiting chairs; no signs, no logos, no number displays.

## 0. 인물 설정표 (영상에는 안 씀)

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/characters.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
A character reference sheet: these characters standing side by side in a row, full body, front view, neutral friendly expressions, plain light background, evenly lit:
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Mr. Kim's son — Korean man in his late 20s, slim, messy short black hair, light gray hoodie, blue jeans.
- Mr. Kim's old school friend — Korean man aged 60, round cheerful face, short gray crew cut, olive-green jacket over a red-and-white checked shirt.
- Mr. Park — another school friend, Korean man aged 60, slim and calm, silver hair neatly combed back, beige jacket over a dark brown turtleneck.
- Pension office counselor — Korean woman in her 40s, shoulder-length dark hair, white blouse with a navy vest, a blank lanyard card, warm professional smile.
16:9 landscape. Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines. Do not write names or labels.
```

## 1. L01 — 밤 식탁, 통장을 내려다보며 이마를 짚고 고개 떨군 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L01.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 1): 「국민연금 신청 한 번에, 평생 손해봤어요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Night at the dining table. Mr. Kim sits under the warm lamp looking down at an open blank bankbook, one hand pressed to his forehead, head bowed, brows knitted, shoulders slumped — clearly crushed and regretful. A few blank papers on the table. Medium shot, eye level.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 2. L02 — 식탁 위 신청서 한 장 클로즈업, 김 씨의 손

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L02.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 2): 「60세 김 씨가 1년 전에 낸 신청서를 두고 한 말입니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Extreme close-up from above of a single application form lying on the dining table under warm lamp light: only empty boxes, gray lines and a signature line, no readable text. A ballpoint pen beside it. Only Mr. Kim's hand and forearm in his navy shirt sleeve rest heavily on the edge of the paper — NO face in the picture (the camera does not show his head). The mood is heavy and regretful: dim warm light, the form looks like the cause of his trouble. Shallow depth of field.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 3. L03 — 서류·계산기를 펼쳐 놓고 돋보기로 따져 보는 김 씨 (탐정처럼)

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L03.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 4): 「그런데 하나씩 따져 보던 김 씨는, 전혀 다른 범인을 찾아냅니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Mr. Kim at the dining table with papers, a calculator and notes spread out (all blank), holding a magnifying glass and leaning forward, eyes narrowed like a detective about to find a clue. Determined expression. Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 4. L04 — 회사 유리문을 나서며 뒤돌아보는 김 씨 (짐 상자)

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L04.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 9): 「김 씨는 59세에 회사를 나왔어요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Scene: Daytime in front of an office building's glass doors (no signs). Mr. Kim walks out carrying a cardboard box of his belongings — a small potted plant, a mug and a photo frame — and glances back at the building with a bittersweet expression. Full-body shot, the building behind him.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 5. L05 — 퇴직금 통장을 서랍 깊이 넣고 잠그는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L05.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 11): 「퇴직금은 있었지만, 손대면 안 되는 돈이라고 생각했습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Mr. Kim kneels by the wooden cabinet and places a blank bankbook deep inside an open drawer, a small key in the lock, with a protective, determined look — this money must not be touched. Close-medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 6. L06 — 공단 창구에서 신청서에 서명해 내미는 김 씨 (다음 달)

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L06.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 12): 「그래서 퇴직한 다음 달, 국민연금을 5년 당겨 신청했어요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A clean, bright public pension office: service counters with clear glass partitions, potted plants, rows of waiting chairs; no signs, no logos, no number displays.
Scene: At a pension office counter, Mr. Kim sits and signs a blank form with a pen, about to slide it under the glass partition; a clerk on the other side is seen from behind, reaching out a hand. Mr. Kim looks calm and a little hurried. Medium shot from the side.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 7. L07 — 거실 소파에서 차를 마시며 여유롭게 웃는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L07.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 16): 「그래도 김 씨는 괜찮다고 생각했어요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Daytime in the living room. Mr. Kim leans back comfortably on the gray sofa holding a warm cup of tea, looking out the window with a relaxed, content smile. Soft sunlight through the curtains. Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 8. L08 — 1년 뒤 동창 모임 — 넷이 웃으며 잔을 부딪침

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L08.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 18): 「그런데 1년쯤 지나, 동창 모임에서 친구가 물었습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Mr. Kim's old school friend — Korean man aged 60, round cheerful face, short gray crew cut, olive-green jacket over a red-and-white checked shirt.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A cozy Korean restaurant: a wooden table with a bubbling stew pot and small side dishes, warm yellow lights, no menu boards or signs.
Scene: Evening at the cozy Korean restaurant. Four men around 60 sit at the wooden table laughing and clinking glasses at a school reunion. Mr. Kim is in the middle, the friend with the gray crew cut sits across from him. Warm lights, steam from the stew. Medium-wide shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 9. L09 — 친구가 진지하게 묻고, 잔을 든 채 굳은 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L09.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 19): 「너, 그거 평생 30% 깎이는 거 알고 신청했어?」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Mr. Kim's old school friend — Korean man aged 60, round cheerful face, short gray crew cut, olive-green jacket over a red-and-white checked shirt.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A cozy Korean restaurant: a wooden table with a bubbling stew pot and small side dishes, warm yellow lights, no menu boards or signs.
Scene: Same restaurant, closer side view of two men. The friend with the gray crew cut leans forward and asks something seriously with his index finger slightly raised; Mr. Kim freezes with his glass halfway to his mouth, eyes wide, smile fading. Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 10. L10 — 밤, 집에 와 계산기를 꺼내 두드리는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L10.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 23): 「집에 온 김 씨는 계산기를 꺼냈어요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Night at the dining table. Mr. Kim, just back home, puts a calculator down next to some blank papers and starts pressing its keys with a worried face. The calculator display is blank. Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 11. L11 — 어깨 너머로 계산기를 보며 고개를 갸웃하는 아들

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L11.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 26): 「그런데 이 숫자를 본 아들이, 고개를 갸웃했습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Mr. Kim's son — Korean man in his late 20s, slim, messy short black hair, light gray hoodie, blue jeans.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Same table at night. Mr. Kim stares at the calculator, discouraged. Behind him, his son in a gray hoodie peers over his shoulder at the calculator (blank display, just a soft glow) and tilts his head curiously. Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 12. L12 — 옆에 앉아 종이를 가리키며 말하는 아들, 고개 드는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L12.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 27): 「아빠, 이거 반만 계산하신 것 같은데요?」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Mr. Kim's son — Korean man in his late 20s, slim, messy short black hair, light gray hoodie, blue jeans.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: The son sits down next to Mr. Kim at the table and points at a blank sheet of paper beside the calculator while talking; Mr. Kim looks up at his son in surprise. Warm lamp light. Medium two-shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 13. L13 — 안도의 숨을 쉬다 무언가 떠올라 눈을 크게 뜨는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L13.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 45): 「조금 마음이 놓인 김 씨에게, 친구가 한 말이 하나 더 남아 있었습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Mr. Kim leans back in his dining chair holding a cup of tea, exhaling in relief — and in this moment something suddenly comes back to his mind: his eyes are opening wide. Medium shot, warm light.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 14. L14 — 회상 — 경고하듯 말하는 친구, 옆에 작은 만화 폭탄

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L14.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 46): 「연금 받으면, 건보료 폭탄 맞는다더라.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim's old school friend — Korean man aged 60, round cheerful face, short gray crew cut, olive-green jacket over a red-and-white checked shirt.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A cozy Korean restaurant: a wooden table with a bubbling stew pot and small side dishes, warm yellow lights, no menu boards or signs.
Scene: A flashback scene in warm sepia tones with soft blurred edges: at the restaurant table the friend with the gray crew cut raises one hand and talks with a warning look. A small, cute cartoon bomb with a sparkling lit fuse floats beside his head (a simple icon, no text). Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 15. L15 — 자기 방에서 채용 공고를 넘기며 한숨 쉬는 아들

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L15.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 48): 「아들은 아직 취업을 준비하고 있어서, 피부양자로 들어갈 곳도 없었죠.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim's son — Korean man in his late 20s, slim, messy short black hair, light gray hoodie, blue jeans.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: The son's small bedroom. He sits at a desk in front of a laptop scrolling through job listings (the screen shows only blank cards, no text), chin resting on his hand, sighing. A stack of blank résumé papers on the desk. Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 16. L16 — 노트북을 함께 들여다보며 찾아보는 김 씨와 아들

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L16.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 49): 「두 사람은 건보료가 어떻게 매겨지는지부터 찾아봤어요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Mr. Kim's son — Korean man in his late 20s, slim, messy short black hair, light gray hoodie, blue jeans.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Mr. Kim and his son lean together toward a laptop on the dining table, searching for information; the son points at the screen (blank charts and cards only) and Mr. Kim looks closely. Medium two-shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 17. L17 — 창가에서 팔짱 끼고 '진짜 범인'을 고민하는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L17.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 62): 「그렇다면 김 씨를 손해 보게 만든 진짜 범인은, 도대체 뭘까요?」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Mr. Kim stands by the living room window with his arms crossed, head tilted, tapping his chin, deep in thought as if solving a mystery. Daylight, clouds outside. Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 18. L18 — 카페에서 통장을 펼쳐 보이는 박 씨, 들여다보는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L18.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 63): 「답은 같은 해에 퇴직한, 동창 박 씨의 통장에 있었습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Mr. Park — another school friend, Korean man aged 60, slim and calm, silver hair neatly combed back, beige jacket over a dark brown turtleneck.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A quiet, bright café with a window seat, a wooden table and coffee cups.
Scene: At the café window table, Mr. Park (silver combed-back hair, beige jacket) opens his blank bankbook and shows it to Mr. Kim with a calm, confident smile; Mr. Kim leans in to look, surprised. Coffee cups on the table. Medium two-shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 19. L19 — 박 씨의 퇴직 날 — 꽃다발을 받고 동료들이 박수

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L19.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 65): 「박 씨도 59세에 퇴직했어요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Park — another school friend, Korean man aged 60, slim and calm, silver hair neatly combed back, beige jacket over a dark brown turtleneck.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Scene: Mr. Park's last day at his own office: he holds a bouquet of flowers and smiles while several of his office coworkers around him clap. The coworkers are unnamed background people in plain office clothes who look clearly different from Mr. Kim, his son, the old friend and the pension counselor — none of those four appear in this picture; Mr. Park is the only main character. Bright office, no signs. Medium-wide shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 20. L20 — 신청서를 옆으로 밀어 두고 펜을 내려놓는 박 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L20.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 66): 「그런데 박 씨는 연금을 바로 신청하지 않았습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Park — another school friend, Korean man aged 60, slim and calm, silver hair neatly combed back, beige jacket over a dark brown turtleneck.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Scene: Mr. Park's tidy study at home: he sits at a desk, a blank application form in front of him, and calmly pushes it aside and puts his pen down, leaning back with a relaxed smile. Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 21. L21 — 카페 창가에 나란히 앉은 두 사람 — 생각에 잠긴 김 씨, 편안한 박 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L21.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 75): 「두 사람을 가른 건 신청서가 아니었습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Mr. Park — another school friend, Korean man aged 60, slim and calm, silver hair neatly combed back, beige jacket over a dark brown turtleneck.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A quiet, bright café with a window seat, a wooden table and coffee cups.
Scene: Mr. Kim and Mr. Park sit side by side at the café window counter: Mr. Kim looks down thoughtfully at his cup, Mr. Park sips his coffee calmly. Soft afternoon light. Medium two-shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 22. L22 — 회상 — 퇴직 전 공책에 계획을 적고 계산기를 두드리는 박 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L22.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 76): 「퇴직하기 전에, 받는 나이까지 버틸 돈을 정해 뒀느냐였습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Park — another school friend, Korean man aged 60, slim and calm, silver hair neatly combed back, beige jacket over a dark brown turtleneck.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Scene: A soft-lit flashback: before retiring, Mr. Park sits at his desk writing a plan in a notebook (blank lines only) and using a calculator (blank display), a wall calendar with no numbers behind him. Calm, organized expression. Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 23. L23 — 결심한 얼굴로 공단 건물 입구로 걸어가는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L23.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 79): 「이 사실을 안 김 씨는, 마지막으로 국민연금공단을 찾아갔습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A clean, bright public pension office: service counters with clear glass partitions, potted plants, rows of waiting chairs; no signs, no logos, no number displays.
Scene: Daytime outside the pension office building: glass entrance doors and potted plants, no signs or logos. Mr. Kim walks toward the entrance holding a document envelope, with a determined face. Full-body shot from slightly behind and to the side.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 24. L24 — 대기석에서 번호표를 쥐고 불안하게 기다리는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L24.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 80): 「이미 낸 신청서, 정말 되돌릴 방법이 없을까요?」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A clean, bright public pension office: service counters with clear glass partitions, potted plants, rows of waiting chairs; no signs, no logos, no number displays.
Scene: Inside the pension office waiting area: Mr. Kim sits on a waiting chair clutching a small blank ticket, his knee bouncing, glancing anxiously toward the counters. Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 25. L25 — 친절히 설명하는 상담 직원, 몸을 내밀며 놀라는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L25.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 82): 「원래 받을 나이 전이라면, 연금을 멈출 수 있다는 거예요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Pension office counselor — Korean woman in her 40s, shoulder-length dark hair, white blouse with a navy vest, a blank lanyard card, warm professional smile.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A clean, bright public pension office: service counters with clear glass partitions, potted plants, rows of waiting chairs; no signs, no logos, no number displays.
Scene: At the service counter, the counselor (shoulder-length dark hair, navy vest) points at a blank document and explains kindly; across from her Mr. Kim leans forward, eyes wide with surprise and hope. Medium two-shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 26. L26 — 밤 식탁, 공책을 펴고 손가락 두 개를 펴며 따져 보는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L26.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 91): 「김 씨는 집에 와서 두 가지를 따져 봤습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Night at the dining table: Mr. Kim sits with an open notebook (blank lines) and a pen, holding up two fingers as he weighs two things, thoughtful and focused. Warm lamp light. Medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 27. L27 — 장식장의 가족사진 — 아흔 넘은 어른들 사진을 보며 미소 짓는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L27.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 92): 「집안 어른들은 대부분 90세 넘게 사셨어요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Living room shelf with framed family photos of very old, smiling relatives in their nineties (a grandmother and grandfather). Mr. Kim holds one frame and looks at it fondly with a gentle smile. Medium close shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 28. L28 — 서랍에서 아껴 둔 퇴직금 통장을 꺼내 보며 고개를 끄덕이는 김 씨

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L28.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 93): 「그리고 아껴 둔 퇴직금으로, 4년은 버틸 수 있었습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Mr. Kim kneels by the same wooden cabinet, the drawer open, and holds up the blank bankbook he saved, looking at it with a calm, confident nod. Close-medium shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 29. L29 — 다음 날 창구에 서류를 내는 김 씨, 웃으며 받는 상담 직원

**저장 경로: `economic/source/gungmin-sigi-2026-10/scenes/L29.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 94): 「김 씨는 다음 날, 지급 정지를 신청했습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 16:9 landscape (1536×864, or the widest landscape size). Keep faces and key objects in the central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom 20% simple and calm with no faces or key objects (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Pension office counselor — Korean woman in her 40s, shoulder-length dark hair, white blouse with a navy vest, a blank lanyard card, warm professional smile.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A clean, bright public pension office: service counters with clear glass partitions, potted plants, rows of waiting chairs; no signs, no logos, no number displays.
Scene: The next day at the pension office counter: Mr. Kim hands a blank form across the counter, the counselor receives it with a smile, and Mr. Kim smiles with relief. Bright morning light. Medium two-shot.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```
