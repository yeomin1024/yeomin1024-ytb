# stock 썸네일 4장 — ChatGPT용 (모든 영상 · 읽고 그대로 만들고 각 저장 경로에 올리기)

자동 생성 — `python tools/make_summary.py --chatgpt-all stock` (2026-10-18 06:03). 이 파일은 고치지 말고 영상마다 `thumbnail_N.md`를 고친 뒤 다시 만든다.

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/stock/thumbnails_chatgpt.md

| 영상 | 만들 시안 | 저장 폴더 |
|---|---|---|
| baedang-etf-2026-10-shorts | thumbnail_1 | `stock/source/baedang-etf-2026-10/shorts/thumbnails/` |
| eonje-maesu-2026-10-shorts | thumbnail_1 | `stock/source/eonje-maesu-2026-10/shorts/thumbnails/` |
| keobeodeu-kol-2026-10-shorts | thumbnail_1 | `stock/source/keobeodeu-kol-2026-10/shorts/thumbnails/` |
| reobeoriji-2026-10-shorts | thumbnail_1 | `stock/source/reobeoriji-2026-10/shorts/thumbnails/` |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 썸네일 파일·프롬프트가 있어도 쓰지 않는다 (2026-10-17 옛 프롬프트로 4장을 다시 그린 일이 있었음). 답의 첫 줄에 이 파일 맨 위 '자동 생성' 줄의 시각을 그대로 적는다 (Claude 가 어느 판으로 그렸는지 확인).
1. 아래 썸네일 4장(4개 영상)을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다. 장마다 서로 다른 그림이다 — 앞 장의 인물·구도·색을 이어 쓰지 않는다.
3. 크기는 **세로형 9:16 (1080×1920)** — 쇼츠 썸네일이자 쇼츠 첫 화면이다. **사진 한 장이 네 가장자리까지 꽉 찬다 — 빈 남색·검정 띠, 테두리, 여백, 가운데만 사진인 꼴은 안 된다** (v1.8.0 — 띠가 있으면 영상에서 비율이 틀린 것처럼 보임). 프롬프트가 '글자·얼굴을 두지 않는 자리'(위·오른쪽·아래)를 말해도 그 자리에도 사진(배경·앞쪽 물건)이 이어진다. 9:16이 안 되면 세로 2:3으로 만들고(가운데를 9:16으로 잘라 씀), 그때는 글자와 얼굴을 가운데에 두고 2:3 그림의 양옆 가장자리 8%에는 두지 않는다 (잘리는 자리 — 사진은 이어짐).
4. 그림 속 글자는 프롬프트가 따옴표로 적은 **영어 낱말·숫자·기호·티커만** (예: BUY, TAX, QQQ, −15%, $100,000, 1×, →, ?, 그리고 비교·수식 기호 >, <, =, +, vs) — 철자·기호·띄어쓰기 그대로, 납작하고 굵은 글씨. 다른 글자·숫자·로고·워터마크는 넣지 않는다 (동전·상자·화면에도). 한국어·문장은 쓰지 않는다 (전 세계 시청자용).
5. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다. **표정·몸짓은 프롬프트에 적힌 그대로** — 손해를 알고 좌절한 장면을 놀란 얼굴·담담한 얼굴·웃는 얼굴로 바꾸지 않고, 작은 화면에서도 그 감정이 보이게 그린다 (v1.8.3).
6. 한 장을 만들 때마다 그 칸의 '문구' 표와 그림 속 글자를 **한 글자씩** 맞춰 본다 — 마이너스 '−'·'%'·'$'·쉼표·소수점·'×'·'→'·'>'·'<'·'='·'+'·'?' 가 빠지거나 바뀌거나 방향이 뒤집히지 않았는지(특히 '>' 와 '<'), 표에 없는 가짜 글자·숫자가 생기지 않았는지 크게 확대해서 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다.
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `3. stock/source/keobeodeu-kol-2026-10/shorts/thumbnails/thumbnail_1.png`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게 (`thumbnail_N.png`).
   - GitHub 에 쓸 수 있으면(쓰기 권한이 있는 GitHub 앱) 장마다 그 경로에 커밋한다. 커밋 메시지: `[썸네일] <영상ID> thumbnail_N 이미지`
   - **쓸 수 없으면 (이 계정의 ChatGPT 는 GitHub 를 읽기만 함 — 2026-10-15 확인)** 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 이 파일의 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"이 그림 4장을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 thumbnail_N.png 이름으로 내려받아 폴더마다 아래 링크에 끌어다 놓고 Commit changes" + 아래 '폴더별 올리기 링크' 목록

## 폴더별 올리기 링크 (ChatGPT가 못 올릴 때 사람이 쓰는 길)

- baedang-etf-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/baedang-etf-2026-10/shorts/thumbnails
- eonje-maesu-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/eonje-maesu-2026-10/shorts/thumbnails
- keobeodeu-kol-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/keobeodeu-kol-2026-10/shorts/thumbnails
- reobeoriji-2026-10-shorts: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/reobeoriji-2026-10/shorts/thumbnails

## 1. baedang-etf-2026-10-shorts · thumbnail_1 — 동전을 떨구는 배당 나무와 큰 나무 — 줄다리기 한가운데

**저장 경로: `stock/source/baedang-etf-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 가운데 위 (높이 13~34%) — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `SCHD > SPY ?` | SCHD 보라 · > 노랑 · SPY 파랑 · ? 노랑 |

프롬프트:

```
YouTube Shorts cover, Vertical 9:16 portrait (1080x1920). Keep all important objects and any face between 13% and 66% of the height and between 6% and 84% of the width (top = YouTube icons, right 16% = like/comment buttons, bottom 34% = title and related-video link). The picture fills the whole canvas to every edge — no empty single-color bands, borders, frames or margins anywhere; the top, the right side and the bottom 34% are part of the same scene, only a little darker in soft shadow, with no text, faces or important objects in them. If 9:16 is not available use 2:3 portrait and keep the side 8% free of text and faces.
Semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424).
Upper middle: two trees of exactly the same size growing from two identical pots — the left tree has violet leaves (#B48CFF) and drops plain gold coins, a small red slice (#FF4D5E) chipping off each falling coin; the right tree has blue leaves (#5AB4FF) and drops only a few small plain gold coins, each also chipping a small red slice — both trees pay and both are taxed.
A rope is tied between the two trunks in a tug-of-war; the knot sits exactly in the middle, and the rope continues off into a dark fog on both sides, so the end of the contest is not visible.
Lower middle (still above 66% of the height): a fictional person in their fifties holding the rope in the middle, looking from one tree to the other, thoughtful — not happy, not afraid.
Mood: a close, undecided contest.
Large simple shapes, high contrast, readable when shrunk to 360 pixels tall.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "SCHD > SPY ?" — written as "SCHD" in violet (#B48CFF), then ">" in bright yellow (#FFD400), then "SPY" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the upper-middle area between 13% and 34% of the height, centered inside the left 84% of the width and about 75% of that width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: ">", "×" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. All text stays between 13% and 66% of the height.
```

## 2. eonje-maesu-2026-10-shorts · thumbnail_1 — 언제 사야 할까? — SPY 선이 노란 평균선을 뚫는 순간, BUY 버튼 위 손가락

**저장 경로: `stock/source/eonje-maesu-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 가운데 위 (높이 13~32%) — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `WHEN TO BUY ?` | WHEN TO 흰색 · BUY 초록 · ? 노랑 |
| 초록 선 옆 — 티커 표 | `SPY` | 흰 글자 · 짙은 둥근 표(흰 테두리) |

프롬프트:

```
YouTube Shorts cover, Vertical 9:16 portrait (1080x1920). Keep all important objects and any face between 13% and 66% of the height and between 6% and 84% of the width (top = YouTube icons, right 16% = like/comment buttons, bottom 34% = title and related-video link). The picture fills the whole canvas to every edge — no empty single-color bands, borders, frames or margins anywhere; the top, the right side and the bottom 34% are part of the same scene, only a little darker in soft shadow, with no text, faces or important objects in them. If 9:16 is not available use 2:3 portrait and keep the side 8% free of text and faces.
Semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424).
Middle: a thin glowing yellow horizontal line (a moving-average line) crossing the frame, and a bright green stock price line (#2BE0A0) rising from below and breaking up through it, its tip turning into an upward arrow — nothing marks whether it will succeed. Above the tip the space fades into dark fog, so where it goes next cannot be seen.
Lower middle (still above 66% of the height): a big round glowing green button with nothing written on it, and the index finger of a fictional person in their late forties hovering just above it, not pressing; part of the person's face, tense and uncertain, looks up at the line — not happy, not afraid.
Mood: the moment of hesitation before buying.
Large simple shapes, high contrast, readable when shrunk to 360 pixels tall.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "WHEN TO BUY ?" — written as "WHEN TO" in white, "BUY" in bright green (#2BE0A0), "?" in bright yellow (#FFD400) — across the upper-middle area between 13% and 32% of the height, centered inside the left 84% of the width and about 75% of that width. Make the headline the most eye-catching thing in the image: huge, very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: the fog and the line top sit below it; keep it off the face. Ticker label: "SPY" in large bold white letters on a dark rounded tag with a white outline, right next to the green line. Spell everything exactly as written, character by character. These are the ONLY letters in the whole image — no other text, no numbers, no logos and no watermarks anywhere; the button and every object have nothing else written on them. All text stays between 13% and 66% of the height.
```

## 3. keobeodeu-kol-2026-10-shorts · thumbnail_1 — 금고에서 금화를 매달 꺼내는 손 + 천에 덮인 두 번째 계좌 — `QYLD > QQQ ?`

**저장 경로: `stock/source/keobeodeu-kol-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 가운데 위 (높이 13~34%) — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `QYLD > QQQ ?` | QYLD 주황 · > 노랑 · QQQ 파랑 · ? 노랑 |

프롬프트:

```
YouTube Shorts cover, Vertical 9:16 portrait (1080x1920). Keep all important objects and any face between 13% and 66% of the height and between 6% and 84% of the width (top = YouTube icons, right 16% = like/comment buttons, bottom 34% = title and related-video link). The picture fills the whole canvas to every edge — no empty single-color bands, borders, frames or margins anywhere; the top, the right side and the bottom 34% are part of the same scene (the same room, light and floor continue there), only a little darker in soft shadow, with no text, faces or important objects in them. If 9:16 is not available use 2:3 portrait and keep the side 8% free of text and faces.
Semi-realistic digital illustration with cinematic lighting, deep dark navy mood (#0C1424), a softly lit vault room with dark blue walls and a polished dark floor that runs to the bottom edge.
Upper middle: an open orange-trimmed safe (#FF8A3D) floating in the air; a hand reaches in and pulls out a handful of plain gold coins, and a few coins fall downward like a monthly payout stream.
The safe rests exactly on a glowing yellow dashed line (the original principal level) — not above it, not below it; whether it will stay there cannot be seen.
To the side, a second, identical but fully covered shape under a dark cloth (a second account, hidden) — nothing about it is visible.
Lower middle (still above 66% of the height): a fictional person in their forties, holding the coins, looking from the safe to the covered shape with a curious, questioning look — not worried, not happy.
Mood: curiosity and suspense; nobody is winning.
Large simple shapes, high contrast, readable when shrunk to 360 pixels tall.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "QYLD > QQQ ?" — written as "QYLD" in orange (#FF8A3D), then ">" in bright yellow (#FFD400), then "QQQ" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the upper-middle area between 13% and 34% of the height, centered inside the left 84% of the width and about 75% of that width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: ">" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters and symbols in the whole image — no other text, no numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing written on them. All text stays between 13% and 34% of the height.
```

## 4. reobeoriji-2026-10-shorts · thumbnail_1 — 폭풍 구름으로 막 떠오르는 멀쩡한 로켓 셋 — 큰 3단 로켓에 금화를 연료로 넣는 손

**저장 경로: `stock/source/reobeoriji-2026-10/shorts/thumbnails/thumbnail_1.png`**

크기: **세로 9:16 (1080×1920) — 쇼츠**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 가운데 위 (높이 13~34%) — **큰 머리글 (가장 크게, 굵게, 테두리·빛)** | `TQQQ 3× > QQQ 1× ?` | TQQQ 3× 주황 · > 노랑 · QQQ 1× 파랑 · ? 노랑 |

프롬프트:

```
YouTube Shorts cover, Vertical 9:16 portrait (1080x1920). Keep all important objects and any face between 13% and 66% of the height and between 6% and 84% of the width (top = YouTube icons, right 16% = like/comment buttons, bottom 34% = title and related-video link). The picture fills the whole canvas to every edge — no empty single-color bands, borders, frames or margins anywhere; the top, the right side and the bottom 34% are part of the same scene, only a little darker in soft shadow, with no text, faces or important objects in them. If 9:16 is not available use 2:3 portrait and keep the side 8% free of text and faces.
Semi-realistic digital illustration with cinematic lighting, deep dark navy night sky (#0C1424) with dark storm clouds.
Upper middle: a large orange-striped rocket (#FF8A3D) with three glowing dots on its side, engines lit, lifting off toward dark storm clouds with distant lightning — not damaged.
Beside it, smaller, a violet rocket (#B48CFF, two dots) and a blue rocket (#5AB4FF, one dot), also lifting off — all three intact, all just leaving the pad; the sky above them disappears into the storm clouds, so no one can see how far each will go or what the storm will do.
Lower middle (still above 66% of the height): a fictional person in their mid-thirties in a dark hoodie dropping one plain gold coin into the orange rocket's fuel hatch, hopeful but uneasy, glancing at the storm.
Mood: big hope and a coming storm — suspense; nobody is winning yet.
Large simple shapes, high contrast, readable when shrunk to 360 pixels tall.
Fictional person, not resembling any real or famous person.
Text: ONE big headline "TQQQ 3× > QQQ 1× ?" — written as "TQQQ 3×" in orange (#FF8A3D), then ">" in bright yellow (#FFD400), then "QQQ 1×" in blue (#5AB4FF), then "?" in bright yellow (#FFD400) — placed across the upper-middle area between 13% and 34% of the height, centered inside the left 84% of the width and about 75% of that width. Make the headline the most eye-catching thing in the image: huge (letters about 22% of the image height), very bold flat sans-serif (like Arial Black), with a thick dark outline and a soft glow so it pops off the background; the ">" sign is as big and bold as the letters and bright yellow, and the "?" is bright yellow. Flat 2D lettering — never 3D, never embossed, never curved, never in perspective. Make room for it: anything that would sit in that band (for example a chest or clouds) goes lower and smaller; keep it off any face. Spell everything exactly as written, character by character: ">", "×" and "?" stay exactly as written — never turn ">" into "<". These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs and objects have nothing else written on them. All text stays between 13% and 66% of the height.
```
