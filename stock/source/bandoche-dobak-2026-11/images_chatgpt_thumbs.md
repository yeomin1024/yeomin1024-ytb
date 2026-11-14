# bandoche-dobak-2026-11 롱폼 썸네일 배경 3장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.0 — 2026-11-14 — 사용자 지시 "썸네일 이미지는 인물은 젠슨 황 이미지 말고는 넣지마 그리고 제목에 상황에 맞춰서 수정하고 다시 명령 알려줘". 제목 3안 = `titles.md` v1.1 (1안 채택).

**어떻게 쓰는가**
- ChatGPT 는 **사람이 하나도 없는 배경 사진만** 만든다 (제목마다 1장 — 3장).
- 젠슨 황은 **AI 로 만들지 않는다** — 실존 인물을 진짜 같은 가짜 사진으로 만들면(특히 불륜·간첩 의혹과 함께) 명예훼손·초상권 위험이 크고, 유튜브 합성 콘텐츠 규정에도 걸린다. 사용자가 **이용 허락(라이선스)이 있는 실제 사진**을 저장소에 넣으면, Claude 가 코드로 배경 위에 그 사진과 문구를 합친다 (`video/render/thumb.mjs`).
- 그래서 배경은 **오른쪽 절반을 비워 둔다** (실제 사진 자리) · 아래 28% 는 문구 자리.
- 앞서 만든 Y 썸네일 사진(`images/TH-PHOTO*.jpg`)은 썸네일로 쓰지 않고, 영상 안 장면으로만 쓸 수 있게 남겨 둔다.

| 번호 | 저장 경로 (모두 `stock/source/bandoche-dobak-2026-11/` 아래) | 제목 안 | 무엇 |
|---|---|---|---|
| 1 | `images/TH-BG-1.jpg` | 1안(채택) 「젠슨 황 불륜으로 하락한 반도체 AI 주식, 매수 기회일까? 다시 폭락할까?」 | 빈 거래실의 큰 화면 — 급락한 파란 선이 끝에서 빨간 반등 갈래와 파란 추가 하락 갈래로 갈림 |
| 2 | `images/TH-BG-2.jpg` | 2안 「엔비디아 문제만이 아니다? 젠슨 황 불륜이 반도체 전체를 흔드는 이유」 | 도미노처럼 줄지어 선 반도체 칩 — 앞쪽부터 넘어지는 순간 |
| 3 | `images/TH-BG-3.jpg` | 3안 「반도체 AI 주식 매수 생각한다면 꼭 보세요, 젠슨 황이 만든 리스크 3가지」 | 빈 이사회실 — 비어 있는 끝자리 의자(CEO 공백) · 앞 탁자에 의사봉(수사)과 자물쇠·쇠사슬(판매 제한) |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 1~3번 **3장을 번호 순서대로 모두** 만든다. 질문하지 말고 한 장을 만든 뒤 바로 다음 장으로 넘어간다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 **공통 사진 규칙** → **썸네일 배경** 문단을 차례로 붙인다.
3. **사람을 하나도 넣지 않는다** — 사람·얼굴·손·실루엣·사람 모양 그림자·사진 속 사진 모두 ✗. 실제 인물(젠슨 황 포함)을 만들거나 닮게 만들지 않는다.
4. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 화면·칩·서류·상자에도 없음. 실제 회사 로고·제품 모양·색 조합(엔비디아의 초록 등)을 닮게 만들지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.
5. 사진 바로 위에 번호와 저장 경로를 한 줄 적는다. 사진 안에는 쓰지 않는다.
6. **다 만들면 저장소에 넣는다** — 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 표의 경로 그대로. **JPEG · RGB · 1536×1024 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장** (GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올림 — 올린 뒤 바이트 크기가 같은지 확인). 장마다 커밋: `[stock] bandoche-dobak-2026-11 <파일 이름> 이미지`. 다 올리면 경로와 커밋 링크를 적는다.
   - **올리기가 실패한 장만** 사진을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 공통 사진 규칙 (1~3번 맨 앞에 그대로 붙임)

```
PHOTO STYLE: a photorealistic documentary-style photograph that looks like it was really taken with a full-frame camera, natural realistic light and color, real textures of metal, glass, wood and paper, gentle film-like grain. Strong but honest mood like a serious news feature photo — no cartoon, no illustration, no 3D render look, no fake HDR glow. NO people at all: no person, face, hand, silhouette, human-shaped shadow or photo of a person anywhere; never depict or resemble any real or famous person. Absolutely no text, letters, numbers, logos, brand marks or watermarks anywhere — screens, chips, papers and objects are blank or show only simple shapes; any stock chart is only lines and bars without labels, colored like a Korean stock app (rising = red, falling = blue). No company product designs or brand colors.
```

## 썸네일 배경 (1~3번 — 공통 사진 규칙 다음에 그대로 붙임)

```
THUMBNAIL BACKGROUND: full-bleed landscape photo 1536x1024 used as a YouTube thumbnail background (the 16:9 middle band 1536x864 is what people see). Put the main subject in the LEFT part of the picture, between 4% and 50% of the width. Keep the RIGHT part, from 50% to 95% of the width, calm, darker and uncluttered with only soft out-of-focus depth — a real photo of a person will be placed there later (head at about 25% to 45% of the height), so nothing important may be there. Keep the lower 28% of the picture calm and darker for two lines of large text added later. Clean, strong contrast that still reads on a small phone screen; realistic, not exaggerated.
```

---

### 1. TH-BG-1 — 1안(채택): 하락 뒤 갈림길 — 매수 기회? 다시 폭락?
**저장 경로: `stock/source/bandoche-dobak-2026-11/images/TH-BG-1.jpg`** — JPEG 700KB 이하 · 1536×1024
```
An empty, dim stock trading room at night. On the left half, a huge wall display shows one thick chart line that has fallen steeply in blue; at its right end the line splits into two branches — a thinner red branch turning upward and a blue branch dropping even further — with a faint question-like gap between them (no symbols, no labels, no numbers, no grid text). The display's cool blue and small red glow reflect on a glossy dark floor and empty desks. The right part of the room fades into soft darkness.
```

### 2. TH-BG-2 — 2안: 엔비디아만의 문제가 아니다 — 반도체 도미노
**저장 경로: `stock/source/bandoche-dobak-2026-11/images/TH-BG-2.jpg`** — JPEG 700KB 이하 · 1536×1024
```
A long row of identical generic computer chip packages (plain gray metal lids on green substrates, no markings) standing on edge like dominoes on a glossy black surface, the row running diagonally from the front-left toward the middle of the picture. The first few chips at the front are toppling into the next ones, frozen in sharp focus at the moment of falling; the rest of the row still stands. Cool blue rim light from behind, a soft warm key light from the left, realistic studio photo. The right part of the picture is dark empty space with soft blue haze.
```

### 3. TH-BG-3 — 3안: 젠슨 황이 만든 리스크 3가지 — 빈 의자·의사봉·자물쇠
**저장 경로: `stock/source/bandoche-dobak-2026-11/images/TH-BG-3.jpg`** — JPEG 700KB 이하 · 1536×1024
```
An empty corporate boardroom at night, seen from low across the end of a long dark wooden table. In the left half: at the far head of the table, a large black leather executive chair stands empty, pulled back and lit by one cold overhead spotlight; on the table in the left foreground, a dark wooden judge's gavel resting on its block and a heavy steel padlock with a short loop of chain lying next to it, each catching the light. The right part of the room falls into soft darkness with faint window reflections.
```

---

## 사용자 할 일 — 젠슨 황 실제 사진 1장 (이용 허락 있는 것만)
1. 위키미디어 공용 https://commons.wikimedia.org/wiki/Category:Jensen_Huang 에서 사진을 고른다. **파일 페이지의 '라이선스'가 CC BY 또는 CC BY-SA 인 사진만** (예: 'Josep Borrell with NVIDIA CEO and founder Jensen Huang (2024).jpg' 같은 공식 행사 사진 — 라이선스 칸을 꼭 확인). 'fair use'·'저작권 있음'·게티이미지·연합뉴스 사진은 쓰지 않는다.
   - 얼굴이 정면 또는 4분의 3으로 크게 나온 사진 · 다른 사람이 함께 나오면 젠슨 황만 잘라 씀 (다른 사람은 넣지 않음).
   - 웃는 사진보다 무표정·진지한 사진 (뉴스 썸네일처럼 — 표정을 고치거나 합성하지 않는다).
2. 저장소에 올린다: `stock/source/bandoche-dobak-2026-11/images/jensen/JENSEN.jpg` (700KB 이하).
3. 같은 폴더 `SOURCE.md` 에 세 줄: 파일 페이지 주소 · 저작자 · 라이선스 (예: `CC BY 4.0`). → 업로드 설명란에 출처 줄로 넣는다 (CC BY 조건).
4. 그다음 Claude 가: 배경 3장 검수 → 젠슨 황 사진 배경 지우기(또는 뉴스식 사진 칸) → 오른쪽 자리에 배치 → 문구(`titles.md`) → 썸네일 3장 → Claude 가 직접 보고 확인.
