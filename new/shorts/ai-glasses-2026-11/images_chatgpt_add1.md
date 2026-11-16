# AI 안경 수능 늑장 대응 쇼츠 — 추가 실사 이미지 2장 (ChatGPT용)

작성: 2026-11-16 add1 v1.0 (Claude) — 사용자 지시 2026-11-16 "대본은 이렇게 수정했고 추가 이미지 생성 명령 알려줘" (대본 v1.5 에서 새로 생긴 두 문장 — 중국 기관이 한꺼번에 움직임 · '감독관 눈에만 맡기는')

**이것만 만든다:** `S11.jpg`·`S12.jpg` 2장. 앞서 만든 `S00`~`S10` 11장은 다시 만들지 않는다 (이미 저장소에 있음).

**배치 (앞 11장과 같음 — 1080×1920 '세 칸'):** 위 칸 검정 + 문구 · **가운데 칸 1080×691 = 이 사진** · 아래 칸 검정 + 자막 → 사진은 **가로 3:2 (1536×1024)**, 중요한 것은 가운데에, 위아래 끝 5% 안에는 두지 않는다. 사진에 검은 테두리·여백 ✗.

| 번호 | 파일 (1536×1024 JPEG · 가로) | 대본 문장 | 장면 |
|---|---|---|---|
| 11 | `new/shorts/ai-glasses-2026-11/images/S11.jpg` | 중국은 … 교육부랑 전파 당국, 경찰에 AI 회사까지 한꺼번에 움직였음 | 큰 상황실 — 시험장 화면·신호 그래프 모니터 벽, 제복·정장 차림 사람들 뒷모습 |
| 12 | `new/shorts/ai-glasses-2026-11/images/S12.jpg` | 감독관 눈에만 맡기는 지경까진 안 왔을 거임 | 시험실에서 감독관이 장비 없이 맨눈으로 수험생 안경을 들여다봄 (둘 다 뒷모습) |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 11·12번 **2장을 번호 순서대로 모두** 만든다. 질문하지 말고 멈추지 말고 다음 장으로.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다. **가로 3:2 (1536×1024) 실사 사진** — 세로 ✗ · 그림·만화·일러스트 ✗ · 위아래 검은 띠 ✗.
3. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 모니터 화면·종이·벽 글씨도 흐려서 읽히지 않게. 확대해 글자가 읽히면 다시 만든다.
4. **사람의 이목구비(눈·코·입)가 하나도 보이지 않게 한다** — 뒷모습·손·실루엣만. 옆모습·흐린 얼굴도 ✗. 실제 사람·연예인·정치인을 닮게 그리지 않고, 국기·기관 문장·경찰 표지 글자를 그리지 않는다.
5. 앞 11장과 이어지게 **차갑고 차분한 뉴스 다큐 톤**으로 (과장된 표정·포즈 ✗).
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다. 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다** — `yeomin1024/yeomin1024-ytb` **main** 브랜치, 표의 경로 그대로 (`S00`~`S10` 은 건드리지 않음). **올리기 전에 JPEG 700KB 이하로** (RGB · 크기 그대로 1536×1024 · 품질 90부터 5씩 낮춰 700KB 아래가 되는 첫 값). 커밋 메시지: `AI 안경 쇼츠 이미지 S11·S12 (ChatGPT)`.
   - **올리기가 실패한 장만** 그림을 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 11. S11 — 중국은 위험을 빠르게 파악해서 교육부랑 전파 당국, 경찰에 AI 회사까지 한꺼번에 움직였음

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S11.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders. Looks like a real news photograph, no illustration. A large, dim government operations command center during a national exam: a huge wall of monitors shows live overhead CCTV views of many exam halls with rows of students, plus several screens with glowing radio-signal waveform graphs. In front, rows of desks with people working together — some in dark police-style uniforms, some in dark suits, some in plain office clothes — all seen only from behind, wearing headsets, pointing at screens and talking on phones, a sense of many agencies moving at once. Blue screen glow, cool tones, urgent but organized atmosphere. No human facial features visible. No readable text, no numbers, no logos, no flags, no emblems, no watermark.
```

## 12. S12 — 감독관 눈에만 맡기는 지경까진 안 왔을 거임

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S12.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders. Looks like a real documentary photograph, no illustration. Inside a Korean high school exam classroom on exam day: an exam proctor, seen from behind, bends down close beside a seated student and squints at the student's thick black-framed eyeglasses with bare eyes only — no device, no detector, just holding a pen and a clipboard. The seated student is also seen from behind, head down over an exam paper (unreadable). Rows of other students in the background, heads bowed, faces hidden. Flat daylight from windows, cool gray tones, the feeling of an impossible task done by eye alone. No human facial features visible. No readable text, no numbers, no logos, no watermark.
```

## 장면 순서 (대본 v1.5 — 편집용, ChatGPT 는 할 일 없음)

| 대본 줄 | 사진 |
|---|---|
| (첫 장면) | S00 |
| 1 또 일 못하는 정부 때문에 … | S01 |
| 2 최초 적발 사례는 5월 중순 … | S02 |
| 3 걸린 사람은 벌금형 … 한 줄 넣은 게 다였음 | S03 |
| 4 다른 나라엔 이미 선례가 있었음 | S04 |
| 5 중국은 … 한꺼번에 움직였음 | **S11** |
| 6 그래서 … 안경을 벗겨서 검사하고, 시험장 전파까지 | S05 → S06 |
| 7 수능이 코앞인데 이제서야 … 대책 논의 | S07 |
| 8 "난 몰라, 니들이 알아서 해" | S08 |
| 9 만약 5월에 … 감독관 눈에만 맡기는 지경까진 | **S12** |
| 10 세무사 수석 합격자가 자백 안 했으면 … | S09 |
| 11 무능도 정도가 있지 … | S10 |
