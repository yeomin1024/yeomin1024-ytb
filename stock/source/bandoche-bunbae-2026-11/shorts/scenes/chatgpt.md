# bandoche-bunbae-2026-11 장면 그림 8장 — ChatGPT용 (읽고 1번부터 차례로 모두 만들기)

자동 생성 — `python3 tools/scene_clips.py build` v1.4.0 (2026-11-06 09:52). 이 파일은 고치지 말고 `stock/source/bandoche-bunbae-2026-11/shorts/scenes/plan.json` 을 고친 뒤 다시 만든다.

이 파일 주소(최신): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/stock/source/bandoche-bunbae-2026-11/shorts/scenes/chatgpt.md

쓰임: 영상에서 **사연 장면**마다 이 그림을 첫 장면으로 짧은 움직이는 클립(약 2~5초)을 만든다 (Kaggle videogen). 숫자·계산 설명은 Claude 가 코드로 그린 화면이라 여기 없다.

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다.** 답의 첫 줄에 이 파일 맨 위 '자동 생성' 줄의 시각을 그대로 적는다. **올리는 파일은 모두 JPEG(.jpg) 700KB 이하** — 2026-10-20 PNG 37장을 그대로 올렸다가 모두 768KB 에서 잘려 깨졌다 (8번).
1. 먼저 **0번 인물 설정표** 한 장을 만든다 (영상에는 쓰지 않음 — 모든 장면의 얼굴·머리·옷을 맞추는 기준).
2. 그다음 **1번부터 8번까지 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
3. 각 장은 그 칸의 **프롬프트(``` 안)를 그대로** 쓴다. 모든 장이 **같은 그림체·같은 인물**이다 (프롬프트마다 그림체와 그 장의 인물 설명이 들어 있음 — 장마다 다른 얼굴·옷으로 바꾸지 않는다).
4. 크기: **9:16 세로** (864×1536 — 안 되면 가장 긴 세로형). 얼굴과 중요한 물건은 프롬프트의 'Format' 줄대로 (잘리는 가장자리·자막 자리를 피함).
5. **그림 속 글자·숫자·기호·로고·워터마크는 하나도 없다.** 서류·통장·계산기·화면·간판은 빈칸이나 회색 줄만.
6. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다. 표정·몸짓은 프롬프트에 적힌 그대로 (감정이 작은 화면에서도 보이게).
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `1. stock/source/bandoche-bunbae-2026-11/shorts/scenes/S01.jpg`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. **GitHub 앱으로 장마다 그 경로에 커밋한다** — 이 계정의 ChatGPT 는 저장소에 파일을 올릴 수 있다 (2026-10-19 사용자 확인). 커밋 메시지 `[장면] bandoche-bunbae-2026-11 <이름> 그림`. 파일 이름·폴더는 저장 경로와 한 글자도 다르지 않게. 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다 (Claude 가 그 목록으로 검수).
   - **올리기 전에 JPEG(.jpg)로 바꿔 700KB 이하로 만든다** — 파이썬(PIL)으로 RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장. GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다 (2026-10-19 썸네일 PNG 4장이 786,444바이트에서 잘려 열리지 않음). 올린 뒤 GitHub 에 있는 그 파일의 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
   - **올리기가 실패한 장만** (권한·연결 오류) 묻지 말고: 그 그림을 번호 순서대로 다시 보여 주고(그림마다 위에 번호와 저장 경로), 마지막에 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 그림체 (모든 장 공통 — 프롬프트에 이미 들어 있음)

Art style: a polished stylized 3D cartoon render in the look of a typical casual mobile-game video advertisement — generic, do NOT copy any existing game's characters, logos, interface or art. Chunky big-headed proportions (head about one third of the body height), large glossy expressive eyes, exaggerated rubbery facial expressions and poses that read instantly on a small phone screen, smooth plastic-like skin and fabric with soft subsurface shading, bold saturated but clean colors, bright soft studio lighting with a warm rim light, simple uncluttered background with soft depth of field, crisp clean shapes, high detail. It is a 3D render — not a photo and not flat 2D.

## 인물

- **반도체만 산 까불이** — A — a hyperactive, goofy young man in his mid-20s who never stands still: spiky bright-orange dyed hair sticking straight up, a backwards lime-green baseball cap, an oversized neon-orange hoodie with a big plain dark square microchip-shaped patch on the chest (a square with little metal pin legs, no text or logo), baggy black cargo shorts, chunky white sneakers, a thin gold chain. Big toothy grin, mischievous raised eyebrows, cocky show-off body language.
- **나눠 담는 차분이** — B — a calm, composed man in his late 30s: neat dark-brown side-parted hair, thin round glasses, clean-shaven, a soft navy-blue knit sweater over a white collared shirt, beige chinos, brown loafers, a slim silver wristwatch. Relaxed upright posture, gentle half-lidded eyes, a small steady smile; he moves slowly and deliberately.

## 장소

- **A의 방** — A's bedroom-studio: bright and a little messy, purple-and-pink LED strip lights, a gaming chair, plain energy-drink cans with no logos, wall posters that show only abstract shapes. On the desk stands a waist-high glossy black-and-gold computer-chip sculpture (a big square chip with shiny metal pin legs) with a coin slot on top — A uses it like a giant piggy bank.
- **B의 서재** — B's tidy sunny home study: a light wooden desk by a large window with soft daylight, a potted plant, a cup of tea. On the desk, four clear glass jars filled with gold coins, each with a different lid: a green lid (cash, also holding folded plain green bills), a blue lid, a gold lid (small gold nuggets), and one jar with a tiny black-and-gold chip charm on its lid (his modest stock share). On the wall, a round dial like a weather gauge with three pictures — a sun, a cloud, and a dark storm cloud with lightning — and one needle.
- **둘이 나란한 무대** — A simple split set: one continuous soft studio backdrop; the left half is lit warm orange-pink (A's side), the right half cool teal-blue (B's side); a glossy pale floor. On the left stands A's waist-high black-and-gold chip piggy bank. On the right, a small round table with B's four coin jars (green, blue, gold lids and the chip-charm jar) and a cup of tea, and B's round weather dial (sun, cloud, storm-cloud pictures, one needle) on a short stand beside the table.

## 0. 인물 설정표 (영상에는 안 씀)

**저장 경로: `stock/source/bandoche-bunbae-2026-11/shorts/scenes/characters.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

```
Art style: a polished stylized 3D cartoon render in the look of a typical casual mobile-game video advertisement — generic, do NOT copy any existing game's characters, logos, interface or art. Chunky big-headed proportions (head about one third of the body height), large glossy expressive eyes, exaggerated rubbery facial expressions and poses that read instantly on a small phone screen, smooth plastic-like skin and fabric with soft subsurface shading, bold saturated but clean colors, bright soft studio lighting with a warm rim light, simple uncluttered background with soft depth of field, crisp clean shapes, high detail. It is a 3D render — not a photo and not flat 2D.
A character reference sheet: these characters standing side by side in a row, full body, front view, neutral friendly expressions, plain light background, evenly lit:
- A — a hyperactive, goofy young man in his mid-20s who never stands still: spiky bright-orange dyed hair sticking straight up, a backwards lime-green baseball cap, an oversized neon-orange hoodie with a big plain dark square microchip-shaped patch on the chest (a square with little metal pin legs, no text or logo), baggy black cargo shorts, chunky white sneakers, a thin gold chain. Big toothy grin, mischievous raised eyebrows, cocky show-off body language.
- B — a calm, composed man in his late 30s: neat dark-brown side-parted hair, thin round glasses, clean-shaven, a soft navy-blue knit sweater over a white collared shirt, beige chinos, brown loafers, a slim silver wristwatch. Relaxed upright posture, gentle half-lidded eyes, a small steady smile; he moves slowly and deliberately.
Below the two full-body figures, add one row of six small head-only expression studies, three per character, same faces: A cheering wildly, A smugly mocking, A sobbing with cartoon tears; B calm and neutral, B annoyed side-eye, B quietly confident half-smile.
16:9 landscape. Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines. Do not write names or labels.
```

## 1. S01 — A 소개 — 까불까불, 돈을 전부 반도체 칩 저금통 하나에 쏟아붓는다

**저장 경로: `stock/source/bandoche-bunbae-2026-11/shorts/scenes/S01.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

클립 약 5초의 첫 장면

```
Art style: a polished stylized 3D cartoon render in the look of a typical casual mobile-game video advertisement — generic, do NOT copy any existing game's characters, logos, interface or art. Chunky big-headed proportions (head about one third of the body height), large glossy expressive eyes, exaggerated rubbery facial expressions and poses that read instantly on a small phone screen, smooth plastic-like skin and fabric with soft subsurface shading, bold saturated but clean colors, bright soft studio lighting with a warm rim light, simple uncluttered background with soft depth of field, crisp clean shapes, high detail. It is a 3D render — not a photo and not flat 2D.
Format: 9:16 vertical (864×1536, or the tallest vertical size). Keep faces between 12% and 60% of the height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple and calm with no faces or key objects (subtitles and the app's buttons go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- A — a hyperactive, goofy young man in his mid-20s who never stands still: spiky bright-orange dyed hair sticking straight up, a backwards lime-green baseball cap, an oversized neon-orange hoodie with a big plain dark square microchip-shaped patch on the chest (a square with little metal pin legs, no text or logo), baggy black cargo shorts, chunky white sneakers, a thin gold chain. Big toothy grin, mischievous raised eyebrows, cocky show-off body language.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A's bedroom-studio: bright and a little messy, purple-and-pink LED strip lights, a gaming chair, plain energy-drink cans with no logos, wall posters that show only abstract shapes. On the desk stands a waist-high glossy black-and-gold computer-chip sculpture (a big square chip with shiny metal pin legs) with a coin slot on top — A uses it like a giant piggy bank.
Scene: A bursts with goofy excitement: standing on his gaming chair with one sneaker up on the desk, he hugs the giant chip piggy bank with one arm and pours a whole bucket of gold coins into its slot with the other hand, winking with his tongue cheekily sticking out, coins splashing everywhere. His smartphone pokes out of his hoodie pocket with a bright glowing screen. It must be obvious that ALL his money goes into this one chip.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 2. S02 — B 소개 — 차분하게 날씨 바늘(국면)을 보며 돈을 현금·여러 병에 나눠 담는다

**저장 경로: `stock/source/bandoche-bunbae-2026-11/shorts/scenes/S02.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

클립 약 5초의 첫 장면

```
Art style: a polished stylized 3D cartoon render in the look of a typical casual mobile-game video advertisement — generic, do NOT copy any existing game's characters, logos, interface or art. Chunky big-headed proportions (head about one third of the body height), large glossy expressive eyes, exaggerated rubbery facial expressions and poses that read instantly on a small phone screen, smooth plastic-like skin and fabric with soft subsurface shading, bold saturated but clean colors, bright soft studio lighting with a warm rim light, simple uncluttered background with soft depth of field, crisp clean shapes, high detail. It is a 3D render — not a photo and not flat 2D.
Format: 9:16 vertical (864×1536, or the tallest vertical size). Keep faces between 12% and 60% of the height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple and calm with no faces or key objects (subtitles and the app's buttons go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- B — a calm, composed man in his late 30s: neat dark-brown side-parted hair, thin round glasses, clean-shaven, a soft navy-blue knit sweater over a white collared shirt, beige chinos, brown loafers, a slim silver wristwatch. Relaxed upright posture, gentle half-lidded eyes, a small steady smile; he moves slowly and deliberately.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: B's tidy sunny home study: a light wooden desk by a large window with soft daylight, a potted plant, a cup of tea. On the desk, four clear glass jars filled with gold coins, each with a different lid: a green lid (cash, also holding folded plain green bills), a blue lid, a gold lid (small gold nuggets), and one jar with a tiny black-and-gold chip charm on its lid (his modest stock share). On the wall, a round dial like a weather gauge with three pictures — a sun, a cloud, and a dark storm cloud with lightning — and one needle.
Scene: B sits calmly at his desk and, with an unhurried hand, places gold coins one by one into the four glass jars so they fill evenly — the chip-charm jar holds only a modest part. He glances up at the weather dial on the wall, whose needle points to the sun. Serene expression: relaxed half-lidded eyes, a small steady smile, tea steaming beside him. It must be obvious that he splits his money into several jars, including cash.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 3. S03 — 오르는 시기 — A 환호하며 더 사서 비중을 늘림 · B 아무 일 없다는 듯 차분히 대응

**저장 경로: `stock/source/bandoche-bunbae-2026-11/shorts/scenes/S03.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

클립 약 5초의 첫 장면 · 구도 `duo_chart`

```
Art style: a polished stylized 3D cartoon render in the look of a typical casual mobile-game video advertisement — generic, do NOT copy any existing game's characters, logos, interface or art. Chunky big-headed proportions (head about one third of the body height), large glossy expressive eyes, exaggerated rubbery facial expressions and poses that read instantly on a small phone screen, smooth plastic-like skin and fabric with soft subsurface shading, bold saturated but clean colors, bright soft studio lighting with a warm rim light, simple uncluttered background with soft depth of field, crisp clean shapes, high detail. It is a 3D render — not a photo and not flat 2D.
Format: 9:16 vertical (864×1536, or the tallest vertical size). The TOP 40% of the picture is ONLY a plain, softly lit empty backdrop — no faces, hands, objects or details there (a chart panel will be placed over it). The two characters stand side by side in the middle band: A always on the LEFT half, B always on the RIGHT half, both seen from about the waist up, faces between 42% and 60% of the height, big and clearly readable expressions. Keep them away from the left and right 10% (the picture will be cropped). The bottom 30%: only their lower bodies, the floor and simple props, no faces (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- A — a hyperactive, goofy young man in his mid-20s who never stands still: spiky bright-orange dyed hair sticking straight up, a backwards lime-green baseball cap, an oversized neon-orange hoodie with a big plain dark square microchip-shaped patch on the chest (a square with little metal pin legs, no text or logo), baggy black cargo shorts, chunky white sneakers, a thin gold chain. Big toothy grin, mischievous raised eyebrows, cocky show-off body language.
- B — a calm, composed man in his late 30s: neat dark-brown side-parted hair, thin round glasses, clean-shaven, a soft navy-blue knit sweater over a white collared shirt, beige chinos, brown loafers, a slim silver wristwatch. Relaxed upright posture, gentle half-lidded eyes, a small steady smile; he moves slowly and deliberately.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A simple split set: one continuous soft studio backdrop; the left half is lit warm orange-pink (A's side), the right half cool teal-blue (B's side); a glossy pale floor. On the left stands A's waist-high black-and-gold chip piggy bank. On the right, a small round table with B's four coin jars (green, blue, gold lids and the chip-charm jar) and a cup of tea, and B's round weather dial (sun, cloud, storm-cloud pictures, one needle) on a short stand beside the table.
Scene: Good times: the weather dial on B's side points to the sun. A (left) leaps into the air cheering with both fists up, mouth wide open in a triumphant shout, eyes sparkling, while stuffing even more coins and his whole wallet into the chip piggy bank — clearly raising his bet. B (right) sits calmly at his small table sipping tea with a neutral, unbothered face, and with two fingers moves just one coin from the chip-charm jar into the green-lid cash jar.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 4. S04 — 조롱 — A가 B를 '거북이'라며 비웃음 · B 못마땅한 표정

**저장 경로: `stock/source/bandoche-bunbae-2026-11/shorts/scenes/S04.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

클립 약 5초의 첫 장면 · 구도 `duo_chart`

```
Art style: a polished stylized 3D cartoon render in the look of a typical casual mobile-game video advertisement — generic, do NOT copy any existing game's characters, logos, interface or art. Chunky big-headed proportions (head about one third of the body height), large glossy expressive eyes, exaggerated rubbery facial expressions and poses that read instantly on a small phone screen, smooth plastic-like skin and fabric with soft subsurface shading, bold saturated but clean colors, bright soft studio lighting with a warm rim light, simple uncluttered background with soft depth of field, crisp clean shapes, high detail. It is a 3D render — not a photo and not flat 2D.
Format: 9:16 vertical (864×1536, or the tallest vertical size). The TOP 40% of the picture is ONLY a plain, softly lit empty backdrop — no faces, hands, objects or details there (a chart panel will be placed over it). The two characters stand side by side in the middle band: A always on the LEFT half, B always on the RIGHT half, both seen from about the waist up, faces between 42% and 60% of the height, big and clearly readable expressions. Keep them away from the left and right 10% (the picture will be cropped). The bottom 30%: only their lower bodies, the floor and simple props, no faces (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- A — a hyperactive, goofy young man in his mid-20s who never stands still: spiky bright-orange dyed hair sticking straight up, a backwards lime-green baseball cap, an oversized neon-orange hoodie with a big plain dark square microchip-shaped patch on the chest (a square with little metal pin legs, no text or logo), baggy black cargo shorts, chunky white sneakers, a thin gold chain. Big toothy grin, mischievous raised eyebrows, cocky show-off body language.
- B — a calm, composed man in his late 30s: neat dark-brown side-parted hair, thin round glasses, clean-shaven, a soft navy-blue knit sweater over a white collared shirt, beige chinos, brown loafers, a slim silver wristwatch. Relaxed upright posture, gentle half-lidded eyes, a small steady smile; he moves slowly and deliberately.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A simple split set: one continuous soft studio backdrop; the left half is lit warm orange-pink (A's side), the right half cool teal-blue (B's side); a glossy pale floor. On the left stands A's waist-high black-and-gold chip piggy bank. On the right, a small round table with B's four coin jars (green, blue, gold lids and the chip-charm jar) and a cup of tea, and B's round weather dial (sun, cloud, storm-cloud pictures, one needle) on a short stand beside the table.
Scene: A (left) points at B and laughs mockingly, bending over and holding his belly, tongue out, holding up a little toy turtle in his other hand to tease B for being slow. B (right) has stopped with his teacup halfway up, eyes narrowed in a sideways glare, mouth pressed into a displeased flat line, one eyebrow twitching — clearly annoyed, but he stays seated and composed.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 5. S05 — 오르다 떨어짐 — A 굳은 웃음·식은땀 · B 꾸준히, 칩 병에서 현금 병으로 조금 옮김

**저장 경로: `stock/source/bandoche-bunbae-2026-11/shorts/scenes/S05.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

클립 약 5초의 첫 장면 · 구도 `duo_chart`

```
Art style: a polished stylized 3D cartoon render in the look of a typical casual mobile-game video advertisement — generic, do NOT copy any existing game's characters, logos, interface or art. Chunky big-headed proportions (head about one third of the body height), large glossy expressive eyes, exaggerated rubbery facial expressions and poses that read instantly on a small phone screen, smooth plastic-like skin and fabric with soft subsurface shading, bold saturated but clean colors, bright soft studio lighting with a warm rim light, simple uncluttered background with soft depth of field, crisp clean shapes, high detail. It is a 3D render — not a photo and not flat 2D.
Format: 9:16 vertical (864×1536, or the tallest vertical size). The TOP 40% of the picture is ONLY a plain, softly lit empty backdrop — no faces, hands, objects or details there (a chart panel will be placed over it). The two characters stand side by side in the middle band: A always on the LEFT half, B always on the RIGHT half, both seen from about the waist up, faces between 42% and 60% of the height, big and clearly readable expressions. Keep them away from the left and right 10% (the picture will be cropped). The bottom 30%: only their lower bodies, the floor and simple props, no faces (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- A — a hyperactive, goofy young man in his mid-20s who never stands still: spiky bright-orange dyed hair sticking straight up, a backwards lime-green baseball cap, an oversized neon-orange hoodie with a big plain dark square microchip-shaped patch on the chest (a square with little metal pin legs, no text or logo), baggy black cargo shorts, chunky white sneakers, a thin gold chain. Big toothy grin, mischievous raised eyebrows, cocky show-off body language.
- B — a calm, composed man in his late 30s: neat dark-brown side-parted hair, thin round glasses, clean-shaven, a soft navy-blue knit sweater over a white collared shirt, beige chinos, brown loafers, a slim silver wristwatch. Relaxed upright posture, gentle half-lidded eyes, a small steady smile; he moves slowly and deliberately.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A simple split set: one continuous soft studio backdrop; the left half is lit warm orange-pink (A's side), the right half cool teal-blue (B's side); a glossy pale floor. On the left stands A's waist-high black-and-gold chip piggy bank. On the right, a small round table with B's four coin jars (green, blue, gold lids and the chip-charm jar) and a cup of tea, and B's round weather dial (sun, cloud, storm-cloud pictures, one needle) on a short stand beside the table.
Scene: The mood shifts: the weather dial on B's side now points to the cloud, and the left half of the backdrop has turned a duller, grayer orange. A (left) stares at his phone with a frozen, too-wide nervous grin, big sweat drops on his forehead, one eye twitching, knees slightly shaking — his cheering is gone. B (right) calmly moves a few coins from the chip-charm jar into the green-lid cash jar, steady and relaxed, with a faint confident smile.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 6. S06 — 폭락 — A 무릎 꿇고 펑펑 욺(망함) · B 조금만 잃어 자신만만 — 조롱 장면과 반대 자리

**저장 경로: `stock/source/bandoche-bunbae-2026-11/shorts/scenes/S06.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

클립 약 5초의 첫 장면 · 구도 `duo_chart`

```
Art style: a polished stylized 3D cartoon render in the look of a typical casual mobile-game video advertisement — generic, do NOT copy any existing game's characters, logos, interface or art. Chunky big-headed proportions (head about one third of the body height), large glossy expressive eyes, exaggerated rubbery facial expressions and poses that read instantly on a small phone screen, smooth plastic-like skin and fabric with soft subsurface shading, bold saturated but clean colors, bright soft studio lighting with a warm rim light, simple uncluttered background with soft depth of field, crisp clean shapes, high detail. It is a 3D render — not a photo and not flat 2D.
Format: 9:16 vertical (864×1536, or the tallest vertical size). The TOP 40% of the picture is ONLY a plain, softly lit empty backdrop — no faces, hands, objects or details there (a chart panel will be placed over it). The two characters stand side by side in the middle band: A always on the LEFT half, B always on the RIGHT half, both seen from about the waist up, faces between 42% and 60% of the height, big and clearly readable expressions. Keep them away from the left and right 10% (the picture will be cropped). The bottom 30%: only their lower bodies, the floor and simple props, no faces (subtitles go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- A — a hyperactive, goofy young man in his mid-20s who never stands still: spiky bright-orange dyed hair sticking straight up, a backwards lime-green baseball cap, an oversized neon-orange hoodie with a big plain dark square microchip-shaped patch on the chest (a square with little metal pin legs, no text or logo), baggy black cargo shorts, chunky white sneakers, a thin gold chain. Big toothy grin, mischievous raised eyebrows, cocky show-off body language.
- B — a calm, composed man in his late 30s: neat dark-brown side-parted hair, thin round glasses, clean-shaven, a soft navy-blue knit sweater over a white collared shirt, beige chinos, brown loafers, a slim silver wristwatch. Relaxed upright posture, gentle half-lidded eyes, a small steady smile; he moves slowly and deliberately.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A simple split set: one continuous soft studio backdrop; the left half is lit warm orange-pink (A's side), the right half cool teal-blue (B's side); a glossy pale floor. On the left stands A's waist-high black-and-gold chip piggy bank. On the right, a small round table with B's four coin jars (green, blue, gold lids and the chip-charm jar) and a cup of tea, and B's round weather dial (sun, cloud, storm-cloud pictures, one needle) on a short stand beside the table.
Scene: Crash: the weather dial points to the storm cloud with lightning; the left half of the set is now dark stormy purple-gray with a small rain cloud over A. A (left) has collapsed onto his knees on the floor, crying huge cartoon waterfalls of tears, mouth wide in a wail, hugging the chip piggy bank which is now cracked, dull and empty, his empty pockets turned inside out. B (right) now stands up straight, chin raised, arms crossed, a calm confident half-smile and one raised eyebrow, looking down at A; his jars are still mostly full and the green-lid cash jar is the fullest. Their positions are the reverse of the earlier teasing scene: now B is the one standing tall.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 7. S07 — A 혼자 — 불 꺼진 방에서 깨진 칩 저금통을 안고 욺

**저장 경로: `stock/source/bandoche-bunbae-2026-11/shorts/scenes/S07.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

클립 약 5초의 첫 장면

```
Art style: a polished stylized 3D cartoon render in the look of a typical casual mobile-game video advertisement — generic, do NOT copy any existing game's characters, logos, interface or art. Chunky big-headed proportions (head about one third of the body height), large glossy expressive eyes, exaggerated rubbery facial expressions and poses that read instantly on a small phone screen, smooth plastic-like skin and fabric with soft subsurface shading, bold saturated but clean colors, bright soft studio lighting with a warm rim light, simple uncluttered background with soft depth of field, crisp clean shapes, high detail. It is a 3D render — not a photo and not flat 2D.
Format: 9:16 vertical (864×1536, or the tallest vertical size). Keep faces between 12% and 60% of the height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple and calm with no faces or key objects (subtitles and the app's buttons go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- A — a hyperactive, goofy young man in his mid-20s who never stands still: spiky bright-orange dyed hair sticking straight up, a backwards lime-green baseball cap, an oversized neon-orange hoodie with a big plain dark square microchip-shaped patch on the chest (a square with little metal pin legs, no text or logo), baggy black cargo shorts, chunky white sneakers, a thin gold chain. Big toothy grin, mischievous raised eyebrows, cocky show-off body language.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: A's bedroom-studio: bright and a little messy, purple-and-pink LED strip lights, a gaming chair, plain energy-drink cans with no logos, wall posters that show only abstract shapes. On the desk stands a waist-high glossy black-and-gold computer-chip sculpture (a big square chip with shiny metal pin legs) with a coin slot on top — A uses it like a giant piggy bank.
Scene: A sits alone on the floor of his now-dark room (LED lights off, gloomy gray-blue light), hugging his knees and the cracked, empty chip piggy bank, crying with trembling lips, tears and a runny nose, a tiny rain cloud drizzling over his head. Exaggerated cartoon sadness, framed from the chest up.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```

## 8. S08 — B 마무리 — 햇살 창가에서 차를 들고 자신만만하게 끄덕임

**저장 경로: `stock/source/bandoche-bunbae-2026-11/shorts/scenes/S08.jpg`** — **JPEG(.jpg) 700KB 이하로 바꿔 올림** (PNG 그대로는 768KB 에서 잘려 깨짐)

클립 약 5초의 첫 장면

```
Art style: a polished stylized 3D cartoon render in the look of a typical casual mobile-game video advertisement — generic, do NOT copy any existing game's characters, logos, interface or art. Chunky big-headed proportions (head about one third of the body height), large glossy expressive eyes, exaggerated rubbery facial expressions and poses that read instantly on a small phone screen, smooth plastic-like skin and fabric with soft subsurface shading, bold saturated but clean colors, bright soft studio lighting with a warm rim light, simple uncluttered background with soft depth of field, crisp clean shapes, high detail. It is a 3D render — not a photo and not flat 2D.
Format: 9:16 vertical (864×1536, or the tallest vertical size). Keep faces between 12% and 60% of the height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple and calm with no faces or key objects (subtitles and the app's buttons go there).
Characters (draw them exactly like this, same face, hair and clothes in every picture):
- B — a calm, composed man in his late 30s: neat dark-brown side-parted hair, thin round glasses, clean-shaven, a soft navy-blue knit sweater over a white collared shirt, beige chinos, brown loafers, a slim silver wristwatch. Relaxed upright posture, gentle half-lidded eyes, a small steady smile; he moves slowly and deliberately.
Only these characters may appear as recognizable people. Any background people must look clearly different from all the other main characters of this story (different faces, hair and clothes).
Place: B's tidy sunny home study: a light wooden desk by a large window with soft daylight, a potted plant, a cup of tea. On the desk, four clear glass jars filled with gold coins, each with a different lid: a green lid (cash, also holding folded plain green bills), a blue lid, a gold lid (small gold nuggets), and one jar with a tiny black-and-gold chip charm on its lid (his modest stock share). On the wall, a round dial like a weather gauge with three pictures — a sun, a cloud, and a dark storm cloud with lightning — and one needle.
Scene: B stands by the sunny window holding his cup of tea, his four jars intact on the desk behind him, and turns to the viewer with a calm, self-assured smile and a small confident nod — relaxed shoulders, warm daylight. The weather dial on the wall points back toward the sun.
Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.
```
