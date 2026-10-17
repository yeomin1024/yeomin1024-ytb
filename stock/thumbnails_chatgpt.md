# stock 썸네일 16장 — ChatGPT용 (모든 영상 · 읽고 그대로 만들고 각 저장 경로에 올리기)

자동 생성 — `python tools/make_summary.py --chatgpt-all stock` (2026-10-17 12:22). 이 파일은 고치지 말고 영상마다 `thumbnail_N.md`를 고친 뒤 다시 만든다.

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/stock/thumbnails_chatgpt.md

| 영상 | 만들 시안 | 저장 폴더 |
|---|---|---|
| baedang-etf-2026-10 | thumbnail_1, thumbnail_2, thumbnail_3 | `stock/source/baedang-etf-2026-10/thumbnails/` |
| eonje-maesu-2026-10 | thumbnail_1, thumbnail_2, thumbnail_3 | `stock/source/eonje-maesu-2026-10/thumbnails/` |
| keobeodeu-kol-2026-10 | thumbnail_1, thumbnail_2, thumbnail_3 | `stock/source/keobeodeu-kol-2026-10/thumbnails/` |
| reobeoriji-2026-10 | thumbnail_1, thumbnail_2, thumbnail_3 | `stock/source/reobeoriji-2026-10/thumbnails/` |
| baedang-etf-2026-10-shorts | thumbnail_1 | `stock/source/baedang-etf-2026-10/shorts/thumbnails/` |
| eonje-maesu-2026-10-shorts | thumbnail_1 | `stock/source/eonje-maesu-2026-10/shorts/thumbnails/` |
| keobeodeu-kol-2026-10-shorts | thumbnail_1 | `stock/source/keobeodeu-kol-2026-10/shorts/thumbnails/` |
| reobeoriji-2026-10-shorts | thumbnail_1 | `stock/source/reobeoriji-2026-10/shorts/thumbnails/` |

## ChatGPT에게 — 이 파일을 읽으면 할 일
1. 아래 썸네일 16장(8개 영상)을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다. 장마다 서로 다른 그림이다 — 앞 장의 인물·구도·색을 이어 쓰지 않는다.
3. 크기는 **장마다 '크기' 줄대로**: 롱폼 썸네일 = 가로형 16:9 (1280×720 — 안 되면 가장 넓은 가로형, 글자와 얼굴은 가운데, 위아래 8% 비움) · **쇼츠 썸네일(영상 ID 끝이 `-shorts`) = 세로형 9:16 (1080×1920)** — 안 되면 세로 2:3, 글자와 얼굴은 가운데, 양옆 8% 비움.
4. 그림 속 글자는 프롬프트가 따옴표로 적은 **영어 낱말·숫자·기호·티커만** (예: BUY, TAX, QQQ, −15%, $100,000, 1×, →, ?, 그리고 비교·수식 기호 >, <, =, +, vs) — 철자·기호·띄어쓰기 그대로, 납작하고 굵은 글씨. 다른 글자·숫자·로고·워터마크는 넣지 않는다 (동전·상자·화면에도). 한국어·문장은 쓰지 않는다 (전 세계 시청자용).
5. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다.
6. 한 장을 만들 때마다 그 칸의 '문구' 표와 그림 속 글자를 **한 글자씩** 맞춰 본다 — 마이너스 '−'·'%'·'$'·쉼표·소수점·'×'·'→'·'>'·'<'·'='·'+'·'?' 가 빠지거나 바뀌거나 방향이 뒤집히지 않았는지(특히 '>' 와 '<'), 표에 없는 가짜 글자·숫자가 생기지 않았는지 크게 확대해서 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다.
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `3. stock/source/baedang-etf-2026-10/thumbnails/thumbnail_3.png`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게 (`thumbnail_N.png`).
   - GitHub 에 쓸 수 있으면(쓰기 권한이 있는 GitHub 앱) 장마다 그 경로에 커밋한다. 커밋 메시지: `[썸네일] <영상ID> thumbnail_N 이미지`
   - **쓸 수 없으면 (이 계정의 ChatGPT 는 GitHub 를 읽기만 함 — 2026-10-15 확인)** 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 이 파일의 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"이 그림 16장을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 thumbnail_N.png 이름으로 내려받아 폴더마다 아래 링크에 끌어다 놓고 Commit changes" + 아래 '폴더별 올리기 링크' 목록

## 폴더별 올리기 링크 (ChatGPT가 못 올릴 때 사람이 쓰는 길)

- baedang-etf-2026-10: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/baedang-etf-2026-10/thumbnails
- eonje-maesu-2026-10: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/eonje-maesu-2026-10/thumbnails
- keobeodeu-kol-2026-10: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/keobeodeu-kol-2026-10/thumbnails
- reobeoriji-2026-10: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/reobeoriji-2026-10/thumbnails
- baedang-etf-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/baedang-etf-2026-10/shorts/thumbnails
- eonje-maesu-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/eonje-maesu-2026-10/shorts/thumbnails
- keobeodeu-kol-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/keobeodeu-kol-2026-10/shorts/thumbnails
- reobeoriji-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/reobeoriji-2026-10/shorts/thumbnails

## 1. baedang-etf-2026-10 · thumbnail_1 — 본안(클릭률 최대): 같은 크기의 선택 사이에서 망설이는 사람 + 가린 결과(흐린 유리·닫힌 상자)

**저장 경로: `stock/source/baedang-etf-2026-10/thumbnails/thumbnail_1.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위쪽 가운데 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `SCHD > SPY ?` | SCHD 보라 · > 노랑 · SPY 파랑 · ? 노랑 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424).
Background: deep dark navy (#0C1424) with a soft glow behind the center and faint thin rising lines far behind, no axes.
Foreground center: two identical large glass jars of exactly the same size on two identical glowing pedestals, side by side. The left jar has a glowing violet rim (#B48CFF), the right jar a glowing blue rim (#5AB4FF). From above, an identical stream of plain gold coins falls into each jar at the same rate. From a small slot on the side of each jar, an identical thin trickle of coins slides down a short chute into one small red box (#FF4D5E) standing between the jars. The front glass of both jars is frosted, so how full they are cannot be seen; a glowing yellow dashed line (#FFD400) crosses both jars at the same height. Above the jars floats a heavy closed wooden treasure chest with warm golden light leaking out of the lid; what is inside cannot be seen.
Center: A fictional person in their early forties in a dark jacket stands beside the jars holding one plain gold coin between two fingers, looking from one jar to the other, thoughtful and hesitant — not happy, not worried. 
Neither side is highlighted or brighter; nobody is winning. The mood is suspense.
Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the main objects inside the central 16:9 area, at least 8% away from the top and bottom edges.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "SCHD > SPY ?" — written as "SCHD" in violet (#B48CFF), then ">" in bright yellow (#FFD400), then "SPY" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the top of the image, centered, between 6% and 34% of the height and about 70% of the width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 2. baedang-etf-2026-10 · thumbnail_2 — 실험안 ①: 같은 장면에서 사람만 뺌

**저장 경로: `stock/source/baedang-etf-2026-10/thumbnails/thumbnail_2.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위쪽 가운데 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `SCHD > SPY ?` | SCHD 보라 · > 노랑 · SPY 파랑 · ? 노랑 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424).
Background: deep dark navy (#0C1424) with a soft glow behind the center and faint thin rising lines far behind, no axes.
Foreground center: two identical large glass jars of exactly the same size on two identical glowing pedestals, side by side. The left jar has a glowing violet rim (#B48CFF), the right jar a glowing blue rim (#5AB4FF). From above, an identical stream of plain gold coins falls into each jar at the same rate. From a small slot on the side of each jar, an identical thin trickle of coins slides down a short chute into one small red box (#FF4D5E) standing between the jars. The front glass of both jars is frosted, so how full they are cannot be seen; a glowing yellow dashed line (#FFD400) crosses both jars at the same height. Above the jars floats a heavy closed wooden treasure chest with warm golden light leaking out of the lid; what is inside cannot be seen.
No people. Neither side is highlighted or brighter; nobody is winning. The mood is suspense.
Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the main objects inside the central 16:9 area, at least 8% away from the top and bottom edges.
Text: ONE big headline "SCHD > SPY ?" — written as "SCHD" in violet (#B48CFF), then ">" in bright yellow (#FFD400), then "SPY" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the top of the image, centered, between 6% and 34% of the height and about 70% of the width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 3. baedang-etf-2026-10 · thumbnail_3 — 실험안 ②: 손·얼굴 클로즈업 (구도)

**저장 경로: `stock/source/baedang-etf-2026-10/thumbnails/thumbnail_3.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위쪽 가운데 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `SCHD > SPY ?` | SCHD 보라 · > 노랑 · SPY 파랑 · ? 노랑 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting and shallow depth of field, deep dark navy background (#0C1424).
Close-up: one hand holding a single plain gold coin above two jar openings, a violet-rimmed jar and a blue-rimmed jar of the same size; below, two identical thin trickles of coins slide into a small red box; the frosted glass hides how full the jars are. 
The face of a fictional person is partly visible at the edge, thoughtful and hesitant. Neither side is highlighted or brighter; nobody is winning.
Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the main objects inside the central 16:9 area, at least 8% away from the top and bottom edges.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "SCHD > SPY ?" — written as "SCHD" in violet (#B48CFF), then ">" in bright yellow (#FFD400), then "SPY" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the top of the image, centered, between 6% and 34% of the height and about 70% of the width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 4. eonje-maesu-2026-10 · thumbnail_1 — 본안(클릭률 최대): 같은 크기의 두 받침대 — 매수 신호 버튼 10개 vs 주사위 — 사이에서 망설이는 사람, 뒤에는 초록(+5%)·빨강(−2%) 점선 사이의 가격 선, 위에 닫힌 상자

**저장 경로: `stock/source/eonje-maesu-2026-10/thumbnails/thumbnail_1.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위쪽 가운데 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | (그림)버튼 `>` (그림)주사위 `?` — 글자는 `>`·`?` 뿐 | 버튼 그림 · > 노랑 · 주사위 그림 · ? 노랑 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424) with a soft glow behind the center.
Background: a huge three-dimensional stock-price wall seen in perspective, rising gently from the left to the right with several small dips. The wall's front face is glowing deep blue (#3E8FE0) fading to dark at the bottom and its top edge is a bright white glowing line. Just above the end of the wall floats a glowing green dashed horizontal line (#2BE0A0), and just below it a glowing red dashed horizontal line (#FF4D5E) — the price line runs between the two dashed lines and has not touched either one yet. There are no axes and no grid lines.
Between the green dashed line and the top of the image floats a heavy closed wooden treasure chest, its lid shut tight, with warm golden light leaking out through the gaps; what is inside cannot be seen.
Foreground, bottom: two identical glowing pedestals of exactly the same size and height, side by side. On the left pedestal: ten small identical round glowing buttons in two rows of five, and above each button floats one small glowing icon: a blank calendar square, a small flag on a pole, an arrow bending upward, a line rising over a smooth yellow line, two smooth lines crossing each other, a red arrow bending downward, a semicircle gauge dial with a needle and no markings, a sharp red mountain-shaped zigzag line, a yellow star above a dashed yellow line, and a yellow star just above a dashed yellow line. On the right pedestal: one big glowing white die with only round pips, taking up exactly the same space as the group of ten buttons.
Center: a fictional person in their late thirties in a dark jacket stands between the two pedestals, one hand hovering above the buttons and the other hand hovering above the die, touching neither; the face looks from one to the other, thoughtful and hesitant — not happy, not worried.
Neither side is highlighted, pressed or brighter; nobody is winning. The mood is suspense: which one reaches the green line first?
Color accents: green only on the upper dashed line, red only on the lower dashed line, the down arrow and the zigzag icon, yellow only on the stars and dashed icon lines, blue on the price wall, warm gold only from the chest. Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the face, the pedestals and the chest inside the central 16:9 area, at least 8% away from the top and bottom edges.
Fictional person, not resembling any real or famous person.
Text: ONE big headline row made of: a big glowing green round button icon (the same style as the buttons in the picture), then ">" in bright yellow (#FFD400), then a big white die icon with round pips, then "?" in bright yellow (#FFD400) — the icons are drawn pictures, the only characters are ">" and "?" — placed across the top of the image, centered, between 6% and 34% of the height and about 70% of the width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 5. eonje-maesu-2026-10 · thumbnail_2 — 실험안 ①(사람 없음): 같은 크기의 두 받침대 — 매수 신호 버튼 10개 vs 주사위 — 와 두 점선 사이의 가격 선, 위에 닫힌 상자

**저장 경로: `stock/source/eonje-maesu-2026-10/thumbnails/thumbnail_2.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위쪽 가운데 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | (그림)버튼 `>` (그림)주사위 `?` — 글자는 `>`·`?` 뿐 | 버튼 그림 · > 노랑 · 주사위 그림 · ? 노랑 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424) with a soft glow behind the center.
Background: a huge three-dimensional stock-price wall seen in perspective, rising gently from the left to the right with several small dips. The wall's front face is glowing deep blue (#3E8FE0) fading to dark at the bottom and its top edge is a bright white glowing line. Just above the end of the wall floats a glowing green dashed horizontal line (#2BE0A0), and just below it a glowing red dashed horizontal line (#FF4D5E) — the price line runs between the two dashed lines and has not touched either one yet. There are no axes and no grid lines.
Between the green dashed line and the top of the image floats a heavy closed wooden treasure chest, its lid shut tight, with warm golden light leaking out through the gaps; what is inside cannot be seen.
Foreground, bottom: two identical glowing pedestals of exactly the same size and height, side by side. On the left pedestal: ten small identical round glowing buttons in two rows of five, and above each button floats one small glowing icon: a blank calendar square, a small flag on a pole, an arrow bending upward, a line rising over a smooth yellow line, two smooth lines crossing each other, a red arrow bending downward, a semicircle gauge dial with a needle and no markings, a sharp red mountain-shaped zigzag line, a yellow star above a dashed yellow line, and a yellow star just above a dashed yellow line. On the right pedestal: one big glowing white die with only round pips, taking up exactly the same space as the group of ten buttons.
There is no person in the image.
Neither side is highlighted, pressed or brighter; nobody is winning. The mood is suspense: which one reaches the green line first?
Color accents: green only on the upper dashed line, red only on the lower dashed line, the down arrow and the zigzag icon, yellow only on the stars and dashed icon lines, blue on the price wall, warm gold only from the chest. Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the pedestals and the chest inside the central 16:9 area, at least 8% away from the top and bottom edges.
Text: ONE big headline row made of: a big glowing green round button icon (the same style as the buttons in the picture), then ">" in bright yellow (#FFD400), then a big white die icon with round pips, then "?" in bright yellow (#FFD400) — the icons are drawn pictures, the only characters are ">" and "?" — placed across the top of the image, centered, between 6% and 34% of the height and about 70% of the width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 6. eonje-maesu-2026-10 · thumbnail_3 — 실험안 ②(클로즈업): 신호 버튼과 주사위 위에 떠 있는 두 손과 망설이는 얼굴, 뒤로 흐린 두 점선 사이의 가격 선과 닫힌 상자

**저장 경로: `stock/source/eonje-maesu-2026-10/thumbnails/thumbnail_3.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 오른쪽 위 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | (그림)버튼 `>` (그림)주사위 `?` — 글자는 `>`·`?` 뿐 | 버튼 그림 · > 노랑 · 주사위 그림 · ? 노랑 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration, close-up composition with shallow depth of field, deep dark navy background (#0C1424).
Center foreground, large: two hands of a fictional person hovering in the air, touching nothing. Under the left hand: a cluster of small round glowing buttons, each with one small glowing icon floating above it (a blank calendar square, a small flag on a pole, an arrow bending upward, a line rising over a smooth yellow line, two smooth lines crossing each other, a red arrow bending downward, a semicircle gauge dial with a needle and no markings, a sharp red mountain-shaped zigzag line, a yellow star above a dashed yellow line, and a yellow star just above a dashed yellow line). Under the right hand: one big glowing white die with only round pips, the same overall size as the button cluster.
Upper left: the side of the person's face, thoughtful and hesitant, eyes moving between the buttons and the die — not happy, not worried.
Blurred background: a white glowing price line running to the right between a glowing green dashed line above (#2BE0A0) and a glowing red dashed line below (#FF4D5E), touching neither; small and far away near the top, a closed wooden treasure chest with warm golden light leaking from its lid.
Neither choice is highlighted, pressed or brighter; nobody is winning. Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the hands, the face, the die and the buttons inside the central 16:9 area, at least 8% away from the top and bottom edges.
Fictional person, not resembling any real or famous person.
Text: ONE big headline row made of: a big glowing green round button icon (the same style as the buttons in the picture), then ">" in bright yellow (#FFD400), then a big white die icon with round pips, then "?" in bright yellow (#FFD400) — the icons are drawn pictures, the only characters are ">" and "?" — placed across the upper-right part of the image, beside the face and never over it (between 6% and 34% of the height). Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 7. keobeodeu-kol-2026-10 · thumbnail_1 — 본안(클릭률 최대): 같은 크기의 선택 사이에서 망설이는 사람 + 가린 결과(흐린 유리·닫힌 상자)

**저장 경로: `stock/source/keobeodeu-kol-2026-10/thumbnails/thumbnail_1.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위쪽 가운데 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `QYLD > QQQ ?` | QYLD 주황 · > 노랑 · QQQ 파랑 · ? 노랑 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424).
Background: deep dark navy (#0C1424) with a soft glow behind the center and faint thin rising price lines far behind, no axes.
Foreground center: two identical tall glass treasure boxes of exactly the same size and height standing on two identical glowing pedestals, side by side. The left box has a glowing orange rim (#FF8A3D), the right box has a glowing blue rim (#5AB4FF). The front glass of both boxes is frosted, so how much gold is inside cannot be seen. A glowing yellow dashed horizontal line (#FFD400) crosses both boxes at exactly the same height (the starting level). From a small golden tap at the bottom of each box, an identical stream of plain gold coins pours out at the same rate into one shared tray in front, the two streams equally thick. Above the boxes floats a heavy closed wooden treasure chest with warm golden light leaking out of the lid; what is inside cannot be seen.
Center: A fictional person in their early sixties in a warm cardigan stands between the two boxes holding a small empty purse, looking from one box to the other, thoughtful and hesitant — not happy, not worried. 
Neither side is highlighted or brighter; nobody is winning. The mood is suspense.
Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the main objects inside the central 16:9 area, at least 8% away from the top and bottom edges.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "QYLD > QQQ ?" — written as "QYLD" in orange (#FF8A3D), then ">" in bright yellow (#FFD400), then "QQQ" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the top of the image, centered, between 6% and 34% of the height and about 70% of the width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 8. keobeodeu-kol-2026-10 · thumbnail_2 — 실험안 ①: 같은 장면에서 사람만 뺌

**저장 경로: `stock/source/keobeodeu-kol-2026-10/thumbnails/thumbnail_2.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위쪽 가운데 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `QYLD > QQQ ?` | QYLD 주황 · > 노랑 · QQQ 파랑 · ? 노랑 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424).
Background: deep dark navy (#0C1424) with a soft glow behind the center and faint thin rising price lines far behind, no axes.
Foreground center: two identical tall glass treasure boxes of exactly the same size and height standing on two identical glowing pedestals, side by side. The left box has a glowing orange rim (#FF8A3D), the right box has a glowing blue rim (#5AB4FF). The front glass of both boxes is frosted, so how much gold is inside cannot be seen. A glowing yellow dashed horizontal line (#FFD400) crosses both boxes at exactly the same height (the starting level). From a small golden tap at the bottom of each box, an identical stream of plain gold coins pours out at the same rate into one shared tray in front, the two streams equally thick. Above the boxes floats a heavy closed wooden treasure chest with warm golden light leaking out of the lid; what is inside cannot be seen.
No people. Neither side is highlighted or brighter; nobody is winning. The mood is suspense.
Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the main objects inside the central 16:9 area, at least 8% away from the top and bottom edges.
Text: ONE big headline "QYLD > QQQ ?" — written as "QYLD" in orange (#FF8A3D), then ">" in bright yellow (#FFD400), then "QQQ" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the top of the image, centered, between 6% and 34% of the height and about 70% of the width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 9. keobeodeu-kol-2026-10 · thumbnail_3 — 실험안 ②: 손·얼굴 클로즈업 (구도)

**저장 경로: `stock/source/keobeodeu-kol-2026-10/thumbnails/thumbnail_3.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위쪽 가운데 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `QYLD > QQQ ?` | QYLD 주황 · > 노랑 · QQQ 파랑 · ? 노랑 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting and shallow depth of field, deep dark navy background (#0C1424).
Close-up: two hands under the two golden taps, one under the orange-rimmed box and one under the blue-rimmed box, each catching an identical stream of plain gold coins; behind them the frosted glass of both boxes hides how much gold is left, and a yellow dashed line runs across both at the same height. 
The face of a fictional person is partly visible at the edge, thoughtful and hesitant. Neither side is highlighted or brighter; nobody is winning.
Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the main objects inside the central 16:9 area, at least 8% away from the top and bottom edges.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "QYLD > QQQ ?" — written as "QYLD" in orange (#FF8A3D), then ">" in bright yellow (#FFD400), then "QQQ" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the top of the image, centered, between 6% and 34% of the height and about 70% of the width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 10. reobeoriji-2026-10 · thumbnail_1 — 본안(클릭률 최대): 같은 크기의 선택 사이에서 망설이는 사람 + 가린 결과(흐린 유리·닫힌 상자)

**저장 경로: `stock/source/reobeoriji-2026-10/thumbnails/thumbnail_1.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위쪽 가운데 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `3× > 1× ?` | 3× 주황 · > 노랑 · 1× 파랑 · ? 노랑 |
| 파랑 로켓(점 1) (작게) | `1×` | 파랑 |
| 보라 로켓(점 2) (작게) | `2×` | 보라 |
| 주황 로켓(점 3) (작게) | `3×` | 주황 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424).
Background: deep dark navy night sky (#0C1424) with a soft glow behind the center, no axes.
Foreground center: three identical small rockets of exactly the same size standing side by side on three identical launch pads, none of them has launched. The first rocket has a glowing blue stripe (#5AB4FF) and one glowing dot on its side, the second a violet stripe (#B48CFF) and two glowing dots, the third an orange stripe (#FF8A3D) and three glowing dots. A thin stream of plain gold coins drops into a small hatch on each rocket at the same rate. Above them the sky is split: dark storm clouds with sharp lightning bolts in the middle height, and higher up, above the clouds, a heavy closed wooden treasure chest glowing softly; what is inside cannot be seen.
Center: A fictional person in their mid-thirties in a dark hoodie stands in front of the three launch pads holding one plain gold coin, looking up at the storm and the chest, thoughtful and hesitant — not happy, not afraid. 
Neither side is highlighted or brighter; nobody is winning. The mood is suspense.
Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the main objects inside the central 16:9 area, at least 8% away from the top and bottom edges.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "3× > 1× ?" — written as "3×" in orange (#FF8A3D), then ">" in bright yellow (#FFD400), then "1×" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the top of the image, centered, between 6% and 34% of the height and about 70% of the width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Small extra labels: "1×" on the launch pad (or hatch) of the blue rocket with one dot, in blue (#5AB4FF); "2×" on the launch pad (or hatch) of the violet rocket with two dots, in violet (#B48CFF); "3×" on the launch pad (or hatch) of the orange rocket with three dots, in orange (#FF8A3D). Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 11. reobeoriji-2026-10 · thumbnail_2 — 실험안 ①: 같은 장면에서 사람만 뺌

**저장 경로: `stock/source/reobeoriji-2026-10/thumbnails/thumbnail_2.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위쪽 가운데 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `3× > 1× ?` | 3× 주황 · > 노랑 · 1× 파랑 · ? 노랑 |
| 파랑 로켓(점 1) (작게) | `1×` | 파랑 |
| 보라 로켓(점 2) (작게) | `2×` | 보라 |
| 주황 로켓(점 3) (작게) | `3×` | 주황 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424).
Background: deep dark navy night sky (#0C1424) with a soft glow behind the center, no axes.
Foreground center: three identical small rockets of exactly the same size standing side by side on three identical launch pads, none of them has launched. The first rocket has a glowing blue stripe (#5AB4FF) and one glowing dot on its side, the second a violet stripe (#B48CFF) and two glowing dots, the third an orange stripe (#FF8A3D) and three glowing dots. A thin stream of plain gold coins drops into a small hatch on each rocket at the same rate. Above them the sky is split: dark storm clouds with sharp lightning bolts in the middle height, and higher up, above the clouds, a heavy closed wooden treasure chest glowing softly; what is inside cannot be seen.
No people. Neither side is highlighted or brighter; nobody is winning. The mood is suspense.
Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the main objects inside the central 16:9 area, at least 8% away from the top and bottom edges.
Text: ONE big headline "3× > 1× ?" — written as "3×" in orange (#FF8A3D), then ">" in bright yellow (#FFD400), then "1×" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the top of the image, centered, between 6% and 34% of the height and about 70% of the width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Small extra labels: "1×" on the launch pad (or hatch) of the blue rocket with one dot, in blue (#5AB4FF); "2×" on the launch pad (or hatch) of the violet rocket with two dots, in violet (#B48CFF); "3×" on the launch pad (or hatch) of the orange rocket with three dots, in orange (#FF8A3D). Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 12. reobeoriji-2026-10 · thumbnail_3 — 실험안 ②: 손·얼굴 클로즈업 (구도)

**저장 경로: `stock/source/reobeoriji-2026-10/thumbnails/thumbnail_3.png`**

크기: 가로 16:9 (1280×720) — 롱폼

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위쪽 가운데 — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `3× > 1× ?` | 3× 주황 · > 노랑 · 1× 파랑 · ? 노랑 |
| 파랑 로켓(점 1) (작게) | `1×` | 파랑 |
| 보라 로켓(점 2) (작게) | `2×` | 보라 |
| 주황 로켓(점 3) (작게) | `3×` | 주황 |

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting and shallow depth of field, deep dark navy background (#0C1424).
Close-up: a hand holding a single plain gold coin in front of three identical rocket hatches marked only with one, two and three glowing dots (blue, violet, orange); behind them, out of focus, storm clouds with lightning and a closed chest above. 
The face of a fictional person is partly visible at the edge, thoughtful and hesitant. Neither side is highlighted or brighter; nobody is winning.
Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the main objects inside the central 16:9 area, at least 8% away from the top and bottom edges.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "3× > 1× ?" — written as "3×" in orange (#FF8A3D), then ">" in bright yellow (#FFD400), then "1×" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the top of the image, centered, between 6% and 34% of the height and about 70% of the width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Small extra labels: "1×" on the launch pad (or hatch) of the blue rocket with one dot, in blue (#5AB4FF); "2×" on the launch pad (or hatch) of the violet rocket with two dots, in violet (#B48CFF); "3×" on the launch pad (or hatch) of the orange rocket with three dots, in orange (#FF8A3D). Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. Keep the bottom-right corner empty.
```

## 13. baedang-etf-2026-10-shorts · thumbnail_1 — 동전을 떨구는 배당 나무와 큰 나무 — 줄다리기 한가운데

**저장 경로: `stock/source/baedang-etf-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 가운데 위 (높이 13~34%) — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `SCHD > SPY ?` | SCHD 보라 · > 노랑 · SPY 파랑 · ? 노랑 |
| 매듭 바로 위 (작게) | `+$33K` | 보라 |

프롬프트:

```
YouTube Shorts cover, Vertical 9:16 portrait (1080x1920). Keep all important objects and any face between 13% and 66% of the height and between 6% and 84% of the width (top = YouTube icons, right 16% = like/comment buttons, bottom 34% = title and related-video link). The bottom 34% is a quiet, dark, empty background. If 9:16 is not available use 2:3 portrait and keep the side 8% empty.
Semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424).
Upper middle: two trees of exactly the same size growing from two identical pots — the left tree has violet leaves (#B48CFF) and drops plain gold coins, a small red slice (#FF4D5E) chipping off each falling coin; the right tree has blue leaves (#5AB4FF) and no coins.
A rope is tied between the two trunks in a tug-of-war; the knot in the middle sits just slightly toward the violet tree, and the rope continues off into a dark fog on both sides, so the end of the contest is not visible.
Lower middle (still above 66% of the height): a fictional person in their fifties holding the rope in the middle, looking from one tree to the other, thoughtful — not happy, not afraid.
Mood: a close, undecided contest.
Large simple shapes, high contrast, readable when shrunk to 360 pixels tall.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "SCHD > SPY ?" — written as "SCHD" in violet (#B48CFF), then ">" in bright yellow (#FFD400), then "SPY" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the upper-middle area between 13% and 34% of the height, centered inside the left 84% of the width and about 75% of that width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Small extra labels: "+$33K" just above the knot in the middle of the rope, medium size, in violet (#B48CFF). Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. All text stays between 13% and 66% of the height.
```

## 14. eonje-maesu-2026-10-shorts · thumbnail_1 — 평균선 신호 vs 주사위 — 높이 올라간 화살표가 금이 간 순간

**저장 경로: `stock/source/eonje-maesu-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 가운데 위 (높이 13~34%) — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | (그림)초록 화살표 `>` (그림)주사위 `?` — 글자는 `>`·`?` 뿐 | 초록 화살표 그림 · > 노랑 · 주사위 그림 · ? 노랑 |

프롬프트:

```
YouTube Shorts cover, Vertical 9:16 portrait (1080x1920). Keep all important objects and any face between 13% and 66% of the height and between 6% and 84% of the width (top = YouTube icons, right 16% = like/comment buttons, bottom 34% = title and related-video link). The bottom 34% is a quiet, dark, empty background. If 9:16 is not available use 2:3 portrait and keep the side 8% empty.
Semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424).
Upper middle: a thin glowing yellow horizontal line (a moving-average line) crossing the frame, and a tall bright green arrow (#2BE0A0) shooting upward through it — near its tip a fresh red crack (#FF4D5E) is spreading across the arrow, small red shards breaking off.
Beside the arrow, at exactly the same height as the arrow tip, a neat stack of many plain white dice (no pips) glowing softly grey — neither the arrow nor the dice is brighter; nobody is winning.
Lower middle (still above 66% of the height): a fictional person in their late forties in a dark jacket, seen from the side, looking up at the cracking arrow and the dice, tense and uncertain — not happy, not afraid.
Mood: suspense, as if the result is about to be revealed.
Large simple shapes, high contrast, readable when shrunk to 360 pixels tall.
Fictional person, not resembling any real or famous person.
Text: ONE big headline row made of: a big bright green upward arrow icon, then ">" in bright yellow (#FFD400), then a big white die icon with round pips, then "?" in bright yellow (#FFD400) — the icons are drawn pictures, the only characters are ">" and "?" — placed across the upper-middle area between 13% and 34% of the height, centered inside the left 84% of the width and about 75% of that width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. All text stays between 13% and 66% of the height.
```

## 15. keobeodeu-kol-2026-10-shorts · thumbnail_1 — 금고에서 동전을 매달 꺼내는 사람 — 금고가 점점 가벼워짐

**저장 경로: `stock/source/keobeodeu-kol-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 가운데 위 (높이 13~34%) — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `QYLD > QQQ ?` | QYLD 주황 · > 노랑 · QQQ 파랑 · ? 노랑 |
| 가라앉은 금고 옆 빨간 틈 (작게) | `−17.5%` | 빨강 |

프롬프트:

```
YouTube Shorts cover, Vertical 9:16 portrait (1080x1920). Keep all important objects and any face between 13% and 66% of the height and between 6% and 84% of the width (top = YouTube icons, right 16% = like/comment buttons, bottom 34% = title and related-video link). The bottom 34% is a quiet, dark, empty background. If 9:16 is not available use 2:3 portrait and keep the side 8% empty.
Semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424).
Upper middle: an open orange-trimmed safe (#FF8A3D) floating in the air; a hand reaches in and pulls out a handful of plain gold coins, and a few coins fall downward like a monthly payout stream.
Under the safe, a glowing yellow dashed line (the original principal level) — the safe has sunk a little below this dashed line and a soft red glow (#FF4D5E) shows the gap.
To the side, a second, identical but fully covered shape under a dark cloth (a second account, hidden) — nothing about it is visible.
Lower middle (still above 66% of the height): a fictional person in their sixties, holding the coins, glancing down at the dashed line with a worried, questioning look — not crying, not happy.
Mood: quiet worry and suspense.
Large simple shapes, high contrast, readable when shrunk to 360 pixels tall.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "QYLD > QQQ ?" — written as "QYLD" in orange (#FF8A3D), then ">" in bright yellow (#FFD400), then "QQQ" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the upper-middle area between 13% and 34% of the height, centered inside the left 84% of the width and about 75% of that width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Small extra labels: "−17.5%" next to the sinking safe, in the red gap under the yellow dashed line, medium size, in red (#FF4D5E). Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. All text stays between 13% and 66% of the height.
```

## 16. reobeoriji-2026-10-shorts · thumbnail_1 — 번개에 부서진 3단 로켓 — 그래도 다시 연료를 넣는 손

**저장 경로: `stock/source/reobeoriji-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 가운데 위 (높이 13~34%) — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `3× > 1× ?` | 3× 주황 · > 노랑 · 1× 파랑 · ? 노랑 |
| 부서진 주황 로켓 옆 (작게) | `−92.3%` | 빨강 |

프롬프트:

```
YouTube Shorts cover, Vertical 9:16 portrait (1080x1920). Keep all important objects and any face between 13% and 66% of the height and between 6% and 84% of the width (top = YouTube icons, right 16% = like/comment buttons, bottom 34% = title and related-video link). The bottom 34% is a quiet, dark, empty background. If 9:16 is not available use 2:3 portrait and keep the side 8% empty.
Semi-realistic digital illustration with cinematic lighting, deep dark navy night sky (#0C1424) with dark storm clouds.
Upper middle: a large orange-striped rocket (#FF8A3D) with three glowing dots on its side, badly damaged — a lightning bolt has just struck it, cracks and sparks, most of its body broken away, smoke rising.
Behind it, smaller and dimmer, a violet rocket (#B48CFF, two dots) and a blue rocket (#5AB4FF, one dot), both scratched by the storm but less damaged — none of the three is flying high; the sky above them disappears into clouds, so no one can see how far they will go.
Lower middle (still above 66% of the height): a fictional person in their mid-thirties in a dark hoodie calmly dropping one plain gold coin into the broken orange rocket's fuel hatch anyway, determined but uneasy.
Mood: storm, damage and stubborn suspense.
Large simple shapes, high contrast, readable when shrunk to 360 pixels tall.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "3× > 1× ?" — written as "3×" in orange (#FF8A3D), then ">" in bright yellow (#FFD400), then "1×" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the upper-middle area between 13% and 34% of the height, centered inside the left 84% of the width and about 75% of that width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Small extra labels: "−92.3%" right next to the broken orange rocket, medium size, in red (#FF4D5E). Spell everything exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", ">", "+" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. All text stays between 13% and 66% of the height.
```
