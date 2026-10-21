# gungmin-sigi-2026-10-shorts 장면 그림 7장 — ChatGPT용 (읽고 1번부터 차례로 모두 만들기)

자동 생성 — `python3 tools/scene_clips.py build` v1.3.0 (2026-10-21 03:01). 이 파일은 고치지 말고 `economic/source/gungmin-sigi-2026-10/shorts/scenes/plan.json` 을 고친 뒤 다시 만든다.

이 파일 주소(최신): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/economic/source/gungmin-sigi-2026-10/shorts/scenes/chatgpt.md

쓰임: 영상에서 **사연 장면**마다 이 그림을 첫 장면으로 짧은 움직이는 클립(약 2~5초)을 만든다 (Kaggle videogen). 숫자·계산 설명은 Claude 가 코드로 그린 화면이라 여기 없다.

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다.** 답의 첫 줄에 이 파일 맨 위 '자동 생성' 줄의 시각을 그대로 적는다. **올리는 파일은 모두 JPEG(.jpg) 700KB 이하** — 2026-10-20 PNG 37장을 그대로 올렸다가 모두 768KB 에서 잘려 깨졌다 (8번). 이 파일은 같은 영상 롱폼 그림을 만든 **같은 대화에서 이어서** 만든다 (인물을 같게).
1. 롱폼에서 만든 인물 설정표의 인물과 **똑같은 얼굴·머리·옷**으로 그린다 (설정표는 다시 만들지 않음).
2. 그다음 **1번부터 7번까지 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
3. 각 장은 그 칸의 **프롬프트(``` 안)를 그대로** 쓴다. 모든 장이 **같은 그림체·같은 인물**이다 (프롬프트마다 그림체와 그 장의 인물 설명이 들어 있음 — 장마다 다른 얼굴·옷으로 바꾸지 않는다).
4. 크기: **9:16 세로** (864×1536 — 안 되면 가장 긴 세로형). 얼굴과 중요한 물건은 프롬프트의 'Format' 줄대로 (잘리는 가장자리·자막 자리를 피함).
5. **그림 속 글자·숫자·기호·로고·워터마크는 하나도 없다.** 서류·통장·계산기·화면·간판은 빈칸이나 회색 줄만.
6. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다. 표정·몸짓은 프롬프트에 적힌 그대로 (감정이 작은 화면에서도 보이게).
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `1. economic/source/gungmin-sigi-2026-10/shorts/scenes/S02.jpg`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. **GitHub 앱으로 장마다 그 경로에 커밋한다** — 이 계정의 ChatGPT 는 저장소에 파일을 올릴 수 있다 (2026-10-19 사용자 확인). 커밋 메시지 `[장면] gungmin-sigi-2026-10-shorts <이름> 그림`. 파일 이름·폴더는 저장 경로와 한 글자도 다르지 않게. 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다 (Claude 가 그 목록으로 검수).
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

## 1. S02 — 59세 퇴직 — 짐 상자를 들고 회사를 나서는 김 씨 (세로)

**저장 경로: `economic/source/gungmin-sigi-2026-10/shorts/scenes/S02.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 2): 「김 씨는 59세에 퇴직했는데, 연금은 64세부터였어요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 9:16 vertical (864×1536, or the tallest vertical size). Keep faces between 12% and 60% of the height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple and calm with no faces or key objects (subtitles and the app's buttons go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Scene: Daytime in front of an office building's glass doors (no signs). Mr. Kim walks out toward the viewer carrying a cardboard box of his belongings — a small potted plant, a mug and a photo frame — and glances back at the building with a bittersweet expression. Vertical full-body shot, his face in the upper-middle of the frame.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 2. S03 — 퇴직한 다음 달, 공단 창구에서 신청서에 서명하는 김 씨 (세로)

**저장 경로: `economic/source/gungmin-sigi-2026-10/shorts/scenes/S03.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 3): 「5년 동안 월급도 연금도 없어서, 퇴직한 다음 달 바로 신청했죠.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 9:16 vertical (864×1536, or the tallest vertical size). Keep faces between 12% and 60% of the height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple and calm with no faces or key objects (subtitles and the app's buttons go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A clean, bright public pension office: service counters with clear glass partitions, potted plants, rows of waiting chairs; no signs, no logos, no number displays.
Scene: At a pension office counter, Mr. Kim signs a blank form with a pen, about to slide it under the glass partition; a clerk's hand reaches out from the other side. Mr. Kim looks calm and a little hurried. Vertical medium shot, his face in the upper-middle of the frame.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 3. S05 — 64세면 돌아올 줄 — 소파에서 차를 마시며 여유로운 김 씨 (세로)

**저장 경로: `economic/source/gungmin-sigi-2026-10/shorts/scenes/S05.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 5): 「그래도 64세가 되면, 원래대로 돌아올 줄 알았어요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 9:16 vertical (864×1536, or the tallest vertical size). Keep faces between 12% and 60% of the height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple and calm with no faces or key objects (subtitles and the app's buttons go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Daytime in the living room. Mr. Kim leans back comfortably on the gray sofa holding a warm cup of tea, smiling with relaxed confidence. Soft sunlight through the curtains. Vertical medium shot, his face in the upper-middle of the frame.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 4. S06 — 1년 뒤 동창 모임 — 웃으며 잔을 부딪치는 친구들 (세로)

**저장 경로: `economic/source/gungmin-sigi-2026-10/shorts/scenes/S06.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 6): 「그런데 1년쯤 지나, 동창 모임에서 친구가 물었습니다.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 9:16 vertical (864×1536, or the tallest vertical size). Keep faces between 12% and 60% of the height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple and calm with no faces or key objects (subtitles and the app's buttons go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Mr. Kim's old school friend — Korean man aged 60, round cheerful face, short gray crew cut, olive-green jacket over a red-and-white checked shirt.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A cozy Korean restaurant: a wooden table with a bubbling stew pot and small side dishes, warm yellow lights, no menu boards or signs.
Scene: Evening at the cozy Korean restaurant: Mr. Kim and his friend with the gray crew cut (and two other friends partly visible) laugh and clink glasses over the table with a bubbling stew pot. Vertical medium shot, faces in the upper-middle of the frame.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 5. S07 — 친구가 진지하게 묻고, 잔을 든 채 굳은 김 씨 (세로)

**저장 경로: `economic/source/gungmin-sigi-2026-10/shorts/scenes/S07.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 7): 「너, 그거 평생 30% 깎이는 거 알고 신청했어?」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 9:16 vertical (864×1536, or the tallest vertical size). Keep faces between 12% and 60% of the height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple and calm with no faces or key objects (subtitles and the app's buttons go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
- Mr. Kim's old school friend — Korean man aged 60, round cheerful face, short gray crew cut, olive-green jacket over a red-and-white checked shirt.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A cozy Korean restaurant: a wooden table with a bubbling stew pot and small side dishes, warm yellow lights, no menu boards or signs.
Scene: Same restaurant, close two-shot: the friend with the gray crew cut leans in and asks something seriously with his index finger raised; Mr. Kim freezes with his glass halfway to his mouth, eyes wide, smile fading. Vertical shot, both faces in the upper-middle of the frame.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 6. S09 — 밤 식탁, 신청서를 내려다보며 이마를 짚고 좌절한 김 씨 (세로)

**저장 경로: `economic/source/gungmin-sigi-2026-10/shorts/scenes/S09.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 9): 「신청서 한 장 때문에, 평생 손해를 봤다는 거예요.」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 9:16 vertical (864×1536, or the tallest vertical size). Keep faces between 12% and 60% of the height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple and calm with no faces or key objects (subtitles and the app's buttons go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Night at the dining table under a warm lamp. Mr. Kim looks down at a single blank application form, one hand pressed to his forehead, head bowed, brows knitted, shoulders slumped — crushed and regretful. Vertical medium shot, his face in the upper-middle of the frame.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 7. S10 — 서류 더미에서 고개를 들어 결심한 눈빛으로 앞을 보는 김 씨 (세로)

**저장 경로: `economic/source/gungmin-sigi-2026-10/shorts/scenes/S10.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

내레이션 (문장 10): 「정말 그만큼 잃은 걸까요, 지금이라도 덜 깎이게 할 수 있을까요?」

```
Warm, friendly 2D animation still, like a frame from a gentle family animated film: clean hand-drawn line art, soft cel shading, warm pastel colors, rounded friendly shapes, cozy natural light, expressive but natural faces. Everyday Korean setting today. Fictional people who do not resemble any real or famous person.
Format: 9:16 vertical (864×1536, or the tallest vertical size). Keep faces between 12% and 60% of the height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple and calm with no faces or key objects (subtitles and the app's buttons go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- Mr. Kim — Korean man, 60 years old but looks youthful like his mid-50s; short neat black hair with gray at the temples; kind round face with thick dark eyebrows; no glasses; navy cotton shirt with the sleeves rolled up over a white T-shirt, beige trousers.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: Mr. Kim's modest Korean apartment: a wooden dining table under a warm pendant lamp, beige walls, a gray fabric sofa in the living room, a wooden cabinet with drawers, framed family photos on a shelf, a window with a city view.
Scene: Night at the dining table covered with blank papers and a calculator: Mr. Kim lifts his head and looks straight ahead with a questioning, determined look — he is not giving up. Vertical medium close-up, his face in the upper-middle of the frame.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```
