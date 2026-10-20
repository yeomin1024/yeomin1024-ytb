# test 이미지 1장 — ChatGPT용 (일본 전통 축제 쇼츠 첫 장면 · 읽고 그대로 만들고 저장 경로에 올리기)

작성: 2026-10-20 (Claude, 2판) — 짝 문서 `test/일본축제_사망사고_제작안.txt` (v8)

이 파일 주소: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/test/images_chatgpt.md

| 번호 | 파일 | 크기 | 쓰는 곳 |
|---|---|---|---|
| 1 | `test/SHORTS-OPEN.jpg` | 세로 9:16 · 세 칸 | 쇼츠 첫 장면 (= 쇼츠 썸네일, 0초 장면) |

롱폼 이미지 7장(IMG-L1~L6, THUMB-L)은 이미 올라와 있다 — **다시 만들지 않는다.**

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 1장을 만든다. 질문하지 말고 바로 만든다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다.
3. 크기: **세로 9:16 (1080×1920) · 세 칸 배치** — 위 0~36% 는 평평한 순검정(#000000)에 문구 2줄만, 가운데 36~72% 는 그림 한 장(가로 끝까지, 위아래 경계는 곧은 가로선), 아래 72~100% 는 순검정 빈 칸(나중에 자막이 들어감). 칸 사이 그라데이션·그림 테두리 없음. 문구 2줄은 줄마다 가운데 정렬(두 줄 가운데 축이 같음)·최대 크기, 그림과 붙거나 겹치지 않는다. **글자·꼬리표는 높이 15~85% 안.** 안 되면 세로 2:3 에 같은 세 칸, 글자는 양옆 8% 밖에 두지 않음.
4. 그림 속 글자는 프롬프트의 따옴표 안 한글만, 글자·띄어쓰기·쉼표·물음표 그대로 쓴다. 줄 수·줄바꿈·색도 프롬프트대로. 다른 글자·숫자·로고·워터마크는 넣지 않는다.
5. 사람은 뒷모습·실루엣으로만 그리고, 얼굴을 알아볼 수 있게 그리지 않는다. 피·다친 사람은 그리지 않는다.
6. 다 만들면 아래 '문구' 표와 그림 속 한글을 한 글자씩 맞춰 본다. 크게 확대해서 받침·모음 획·조사('사망자'의 '자', '반응이'의 '이')가 빠지거나 가려지지 않았는지, 세 칸 배치대로인지(위·아래 칸이 순검정, 그림 칸이 가로 끝까지, 문구 2줄이 줄마다 가운데) 본다. 다르면 다시 만든다.
7. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. test/SHORTS-OPEN.jpg`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로 `test/SHORTS-OPEN.jpg` (한 글자도 다르지 않게).
   - **올리기 전에 JPEG(.jpg)로 바꿔 700KB 이하로 만든다** — 파이썬(PIL)으로 RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장. GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다. 올린 뒤 GitHub 에 있는 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
   - **GitHub 앱으로 커밋한다.** 커밋 메시지: `[test] SHORTS-OPEN.jpg 이미지`. 올린 뒤 파일 경로와 커밋 링크를 적는다.
   - **올리기가 실패하면** (권한·연결 오류) 묻지 말고 그림을 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"이 그림을 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 저장 경로에 올립니다."** 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 SHORTS-OPEN.jpg 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/test 에 끌어다 놓고 Commit changes"

## 1. SHORTS-OPEN — 쇼츠 첫 장면 (세 칸 · 문구 포함)

**저장 경로: `test/SHORTS-OPEN.jpg`** — JPEG 700KB 이하

크기: **세로 9:16 (1080×1920) — 쇼츠 · 세 칸 (위 0~36% 순검정 + 문구 2줄 · 가운데 36~72% 그림 · 아래 72~100% 순검정, 글자·꼬리표는 높이 15~85%)**

문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):

| 자리 | 문구 | 색 |
|---|---|---|
| 위 1줄 | 매년 사망자 나와도 안 멈춘다? | '매년' 흰색 · **'사망자' 빨강 #FF2A2A** · '나와도' 흰색 · **'안 멈춘다?' 노랑 #FFD400** — 검정 바탕 위 평면 글자 |
| 위 2줄 | 일본 축제, 현지 반응이 더 충격 | '일본 축제,' 흰색 · **'현지 반응이 더 충격' 노랑 #FFD400** — 1줄과 같은 크기 |
| 그림 꼬리표 | 8일 만에 3명 사망 | 흰 평면 글자 on 빨강 상자 #FF2A2A |

프롬프트:

```
Vertical YouTube Shorts opening frame, 9:16 portrait (1080x1920), high contrast.
LAYOUT — three full-width zones: 0–36% of the height flat solid pure black (#000000) with only the headline; 36–72% one cinematic digital painting edge to edge with straight top and bottom edges; 72–100% flat solid pure black, empty (subtitles will be added there later). No gradient, fade or border between the zones.
SAFE AREA: some feeds crop to about 4:5 — all text and the word tag stay between 15% and 85% of the height.
Headline: exactly TWO lines of very large heavy bold Korean text, the same letter size, EACH LINE CENTERED on the same axis, the longer line from about 4% to 96% of the width, the block between about 18% and 33% of the height and at least 3% above the painting; flat letters, no outline, no glow, no 3D.
line 1 "매년 사망자 나와도 안 멈춘다?" — "매년" in white, "사망자" in bright red #FF2A2A, "나와도" in white, "안 멈춘다?" in bright yellow #FFD400;
line 2 "일본 축제, 현지 반응이 더 충격" — "일본 축제," in white and "현지 반응이 더 충격" in bright yellow #FFD400.
Painting zone (36–72%): cinematic digital painting, semi-realistic, very high contrast, dramatic. A huge ornate Japanese festival float with gold and crimson embroidered panels and glowing paper lanterns, tilting dangerously to one side at dusk on a festival street, silhouettes of carriers straining beneath its long wooden poles, dramatic backlight from the setting sun, dust in the air, intense red-orange and deep navy contrast. The float is centered slightly right (about 35–85% of the width). Carriers only in silhouette or from behind; no recognizable faces. No blood, no injured people.
On the upper left of the painting (about 5–45% of the width, 39–47% of the height): one bold tag, a solid bright red (#FF2A2A) rounded box with the Korean text "8일 만에 3명 사망" printed in large flat heavy bold white letters on its flat front face (flat print, not carved or 3D). Keep the right 16% of the width below 45% of the height free of tags (Shorts buttons).
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536) with the same three zones and keep the headline between 12% and 88% of the width.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, spacing, comma and question mark, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
