# stock 썸네일 3장 — ChatGPT용 (모든 영상 · 읽고 그대로 만들고 각 저장 경로에 올리기)

자동 생성 — `python tools/make_summary.py --chatgpt-all stock` (2026-10-16 17:46). 이 파일은 고치지 말고 영상마다 `thumbnail_N.md`를 고친 뒤 다시 만든다.

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/stock/thumbnails_chatgpt.md

| 영상 | 만들 시안 | 저장 폴더 |
|---|---|---|
| eonje-maesu-2026-10 | thumbnail_1, thumbnail_2, thumbnail_3 | `stock/source/eonje-maesu-2026-10/thumbnails/` |

## ChatGPT에게 — 이 파일을 읽으면 할 일
1. 아래 썸네일 3장(1개 영상)을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다. 장마다 서로 다른 그림이다 — 앞 장의 인물·구도·색을 이어 쓰지 않는다.
3. 크기는 가로형 16:9 (1280×720). 16:9가 안 되면 가장 넓은 가로형으로 만들고, 글자와 얼굴은 가운데에 두고 위아래 가장자리 8%는 비운다.
4. **그림 속에 글자·숫자·기호·로고·워터마크를 하나도 넣지 않는다** — 전 세계 시청자용이라 그림만으로 뜻을 전한다. 지폐·화면·간판·그래프 눈금에도 글자나 숫자가 없어야 한다.
5. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다.
6. 한 장을 만들 때마다 그림을 크게 확대해 **글자처럼 보이는 것**(가짜 글자, 숫자, 지폐 무늬 속 숫자, 화면 속 글)이 없는지 본다. 있으면 그 부분만 지운 그림으로 다시 만든다.
7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `3. stock/source/eonje-maesu-2026-10/thumbnails/thumbnail_3.png`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게 (`thumbnail_N.png`).
   - GitHub 에 쓸 수 있으면(쓰기 권한이 있는 GitHub 앱) 장마다 그 경로에 커밋한다. 커밋 메시지: `[썸네일] <영상ID> thumbnail_N 이미지`
   - **쓸 수 없으면 (이 계정의 ChatGPT 는 GitHub 를 읽기만 함 — 2026-10-15 확인)** 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 이 파일의 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"이 그림 3장을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 thumbnail_N.png 이름으로 내려받아 폴더마다 아래 링크에 끌어다 놓고 Commit changes" + 아래 '폴더별 올리기 링크' 목록

## 폴더별 올리기 링크 (ChatGPT가 못 올릴 때 사람이 쓰는 길)

- eonje-maesu-2026-10: https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/source/eonje-maesu-2026-10/thumbnails

## 1. eonje-maesu-2026-10 · thumbnail_1 — 본안(클릭률 최대): 같은 크기의 두 받침대 — 매수 신호 버튼 10개 vs 주사위 — 사이에서 망설이는 사람, 뒤에는 초록(+5%)·빨강(−2%) 점선 사이의 가격 선, 위에 닫힌 상자

**저장 경로: `stock/source/eonje-maesu-2026-10/thumbnails/thumbnail_1.png`**

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424) with a soft glow behind the center.
Background: a huge three-dimensional stock-price wall seen in perspective, rising gently from the left to the right with several small dips. The wall's front face is glowing deep blue (#3E8FE0) fading to dark at the bottom and its top edge is a bright white glowing line. Just above the end of the wall floats a glowing green dashed horizontal line (#2BE0A0), and just below it a glowing red dashed horizontal line (#FF4D5E) — the price line runs between the two dashed lines and has not touched either one yet. There are no axes, no grid lines and no labels.
Between the green dashed line and the top of the image floats a heavy closed wooden treasure chest, its lid shut tight, with warm golden light leaking out through the gaps; what is inside cannot be seen.
Foreground, bottom: two identical glowing pedestals of exactly the same size and height, side by side. On the left pedestal: ten small identical round glowing buttons in two rows of five, and above each button floats one small glowing icon: a blank calendar square, a small flag on a pole, an arrow bending upward, a line rising over a smooth yellow line, two smooth lines crossing each other, a red arrow bending downward, a semicircle gauge dial with a needle and no markings, a sharp red mountain-shaped zigzag line, a yellow star above a dashed yellow line, and a yellow star just above a dashed yellow line. On the right pedestal: one big glowing white die with only round pips, taking up exactly the same space as the group of ten buttons.
Center: a fictional person in their late thirties in a dark jacket stands between the two pedestals, one hand hovering above the buttons and the other hand hovering above the die, touching neither; the face looks from one to the other, thoughtful and hesitant — not happy, not worried.
Neither side is highlighted, pressed or brighter; nobody is winning. The mood is suspense: which one reaches the green line first?
Color accents: green only on the upper dashed line, red only on the lower dashed line, the down arrow and the zigzag icon, yellow only on the stars and dashed icon lines, blue on the price wall, warm gold only from the chest. Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the face, the pedestals and the chest inside the central 16:9 area, at least 8% away from the top and bottom edges.
Fictional person, not resembling any real or famous person.
Absolutely no text, no letters, no numbers, no symbols, no percent signs, no question marks, no logos and no watermarks anywhere in the image. The buttons are plain with nothing written on them; the die shows only round pips; the calendar is an empty square; the gauge has no numbers or tick labels; the price wall and the dashed lines have no labels; there are no screens, no papers and no signs.
```

## 2. eonje-maesu-2026-10 · thumbnail_2 — 실험안 ①(사람 없음): 같은 크기의 두 받침대 — 매수 신호 버튼 10개 vs 주사위 — 와 두 점선 사이의 가격 선, 위에 닫힌 상자

**저장 경로: `stock/source/eonje-maesu-2026-10/thumbnails/thumbnail_2.png`**

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424) with a soft glow behind the center.
Background: a huge three-dimensional stock-price wall seen in perspective, rising gently from the left to the right with several small dips. The wall's front face is glowing deep blue (#3E8FE0) fading to dark at the bottom and its top edge is a bright white glowing line. Just above the end of the wall floats a glowing green dashed horizontal line (#2BE0A0), and just below it a glowing red dashed horizontal line (#FF4D5E) — the price line runs between the two dashed lines and has not touched either one yet. There are no axes, no grid lines and no labels.
Between the green dashed line and the top of the image floats a heavy closed wooden treasure chest, its lid shut tight, with warm golden light leaking out through the gaps; what is inside cannot be seen.
Foreground, bottom: two identical glowing pedestals of exactly the same size and height, side by side. On the left pedestal: ten small identical round glowing buttons in two rows of five, and above each button floats one small glowing icon: a blank calendar square, a small flag on a pole, an arrow bending upward, a line rising over a smooth yellow line, two smooth lines crossing each other, a red arrow bending downward, a semicircle gauge dial with a needle and no markings, a sharp red mountain-shaped zigzag line, a yellow star above a dashed yellow line, and a yellow star just above a dashed yellow line. On the right pedestal: one big glowing white die with only round pips, taking up exactly the same space as the group of ten buttons.
There is no person in the image.
Neither side is highlighted, pressed or brighter; nobody is winning. The mood is suspense: which one reaches the green line first?
Color accents: green only on the upper dashed line, red only on the lower dashed line, the down arrow and the zigzag icon, yellow only on the stars and dashed icon lines, blue on the price wall, warm gold only from the chest. Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the pedestals and the chest inside the central 16:9 area, at least 8% away from the top and bottom edges.
Absolutely no text, no letters, no numbers, no symbols, no percent signs, no question marks, no logos and no watermarks anywhere in the image. The buttons are plain with nothing written on them; the die shows only round pips; the calendar is an empty square; the gauge has no numbers or tick labels; the price wall and the dashed lines have no labels; there are no screens, no papers and no signs.
```

## 3. eonje-maesu-2026-10 · thumbnail_3 — 실험안 ②(클로즈업): 신호 버튼과 주사위 위에 떠 있는 두 손과 망설이는 얼굴, 뒤로 흐린 두 점선 사이의 가격 선과 닫힌 상자

**저장 경로: `stock/source/eonje-maesu-2026-10/thumbnails/thumbnail_3.png`**

프롬프트:

```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration, close-up composition with shallow depth of field, deep dark navy background (#0C1424).
Center foreground, large: two hands of a fictional person hovering in the air, touching nothing. Under the left hand: a cluster of small round glowing buttons, each with one small glowing icon floating above it (a blank calendar square, a small flag on a pole, an arrow bending upward, a line rising over a smooth yellow line, two smooth lines crossing each other, a red arrow bending downward, a semicircle gauge dial with a needle and no markings, a sharp red mountain-shaped zigzag line, a yellow star above a dashed yellow line, and a yellow star just above a dashed yellow line). Under the right hand: one big glowing white die with only round pips, the same overall size as the button cluster.
Upper left: the side of the person's face, thoughtful and hesitant, eyes moving between the buttons and the die — not happy, not worried.
Blurred background: a white glowing price line running to the right between a glowing green dashed line above (#2BE0A0) and a glowing red dashed line below (#FF4D5E), touching neither; small and far away near the top, a closed wooden treasure chest with warm golden light leaking from its lid.
Neither choice is highlighted, pressed or brighter; nobody is winning. Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the hands, the face, the die and the buttons inside the central 16:9 area, at least 8% away from the top and bottom edges.
Fictional person, not resembling any real or famous person.
Absolutely no text, no letters, no numbers, no symbols, no percent signs, no question marks, no logos and no watermarks anywhere in the image. The buttons are plain with nothing written on them; the die shows only round pips; the calendar is an empty square; the gauge has no numbers or tick labels; the price wall and the dashed lines have no labels; there are no screens, no papers and no signs.
```
