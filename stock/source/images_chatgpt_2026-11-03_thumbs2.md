# 주식 롱폼 1~4편 썸네일 그림 4장 (다시) — 실사 · 얼굴 안 보임 · 4장이 서로 다르게 (ChatGPT용)

작성: 2026-11-03 (Claude) — 사용자 지시 2026-11-03 "배경이나 구도 등 이미지 상으로 비슷하지 않게 해봐" (앞 지시 "아니 그냥 실사로 해 사람 얼굴을 보이지 않게 뒷모습 등과 같은 구도로하고 실제 일처럼 장소, 주식 앱 등 요소 구성해서 리얼하게 상황 묘사해 막 과장되게 하진 말고" 도 그대로)

**이것만 만든다:** 썸네일 그림 4장 (`TH-PHOTO2.jpg`). 먼저 받은 `TH-PHOTO.jpg` 4장은 네 장 모두 '밤 · 어두운 방 · 스탠드 · 가운데 뒷모습'이라 서로 너무 닮아 쓰지 않는다. 소품 14장도 다시 만들지 않는다. 같은 그림의 가운데를 세로로 잘라 쇼츠 첫 장면에도 쓴다.
**색:** 한국 주식 앱처럼 **오르면 빨강 · 내리면 파랑**.

| 번호 | 파일 (1536×864 JPEG) | 장소 | 시간·빛 | 구도 | 색감 | 쓰는 곳 |
|---|---|---|---|---|---|---|
| 1 | `stock/source/ppalli-test-2026-11/images/TH-PHOTO2.jpg` | 아침 출근 지하철 안 | 평일 아침 · 밝은 흰 햇빛·형광등 | 어깨 너머 아주 가까이 — 휴대전화 화면이 크게 | 흰·회색·남색 (밝음) | 1편 「주식 투자 실패하는 사람들은 절대 통과 못하는 테스트」 · '-50%, -70% 손실' · '설마 나도?' |
| 2 | `stock/source/daebi-test-2026-11/images/TH-PHOTO2.jpg` | 주말 오후 카페 창가 | 오후 · 따뜻한 금빛 햇살 | 비스듬히 뒤 (왼쪽 어깨 뒤 45°) 중간 거리 — 카페가 보임 | 베이지·햇빛·연초록 (밝음) | 2편 「주식 투자 수익나도 결국엔 손실인 사람들은 절대 통과 못하는 테스트」 · '+10%가 -20%로...' · '주식 잘하는 줄 알았는데...' |
| 3 | `stock/source/signal-test-2026-11/images/TH-PHOTO2.jpg` | 책상 위 (위에서 내려다봄) | 흐린 낮 · 창으로 드는 부드러운 빛 | 바로 위에서 내려다본 탑뷰 — 손만 보임 | 회색·종이색·흐린 파랑 (중간 밝기) | 3편 「주식 시장 위험 신호 몰라 손실보는 사람들은 절대 통과 못하는 테스트」 · '나만 손해봤네...' · '미리 공부할걸...' |
| 4 | `stock/source/gongpo-test-2026-11/images/TH-PHOTO2.jpg` | 새벽 고층 아파트 큰 창가 (미국 장 마감 확인) | 해 뜨기 직전 · 창 밖 역광 (짙은 파랑 + 주황 띠) | 서 있는 사람 허리 위 실루엣 — 창과 도시가 보임 | 짙은 파랑·주황 (역광) | 4편 「주식 폭락 공포에 매수 못하는 사람들은 통과 못하는 테스트」 · '그 때 살걸...' · '손실만 봤네...' |

→ **네 장의 장소·시간·빛·구도·색이 모두 다르다** (밤 실내 둘, 같은 크기 뒷모습 둘이 되면 안 됨).

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트(종이 인형극, 앞의 TH-PHOTO 포함)가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 1~4번 **4장을 번호 순서대로 모두** 만든다. 질문하지 말고 멈추지 말고 다음 장으로.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다. 화풍 문단을 따로 붙이지 않는다 (실사).
3. **얼굴이 보이면 다시 만든다** (뒷모습·어깨 너머·손만). 실제 사람·연예인을 닮게 그리지 않는다.
4. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 화면은 그래프 모양과 색만, 글씨는 흐려서 읽히지 않게. 실제 증권사 앱·회사 로고를 닮게 그리지 않는다. 확대해 글자가 읽히면 다시 만든다.
5. **4장을 다 만든 뒤 나란히 놓고 본다** — 두 장이 비슷하면(같은 어두운 실내 밤 · 같은 크기의 가운데 뒷모습 · 같은 스탠드 불빛) 위 표와 다른 쪽을 다시 만든다.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다. 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다** — `yeomin1024/yeomin1024-ytb` main 브랜치, 표의 경로 그대로 (새 파일 `TH-PHOTO2.jpg` — 예전 `TH-PHOTO.jpg` 는 덮어쓰지 않음). **올리기 전에 JPEG 700KB 이하로** (RGB · 크기 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지) — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기가 내 파일과 같은지 확인. 커밋 메시지 `[stock] <편 폴더> TH-PHOTO2.jpg 이미지`.
   - **올리기가 실패한 장만** 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 1. TH-PHOTO2 (ppalli) — 아침 출근 지하철 안 · 평일 아침 · 어깨 너머 아주 가까이

**저장 경로: `stock/source/ppalli-test-2026-11/images/TH-PHOTO2.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Photorealistic YouTube thumbnail background photo, landscape 16:9 (1536x864), looks like a real candid photo, calm and believable — not exaggerated, no dramatic poses, no cartoon, no illustration, no paper-cut style. A bright weekday morning inside a Seoul subway car, cool white daylight mixed with fluorescent light; a few standing commuters far in the background, heavily blurred and turned away. Tight over-the-shoulder close-up from behind and slightly above the right shoulder of a man in a navy suit jacket who holds the overhead strap with one hand and a smartphone with the other; only the back of his head and his shoulder are in frame, the face is completely out of frame. The phone screen is large and sharp in the middle of the image and shows a generic stock trading app with a steep blue falling line chart. Shallow depth of field. Palette: cool white, light grey and navy — a bright image, not a dark one. Bottom 34%: the soft, out-of-focus navy fabric of his jacket shoulder and sleeve. NO face visible anywhere: the main person is seen only from behind, over the shoulder or as hands, and any other people are far away, turned away and heavily blurred; nobody resembles a real individual. The main subject (the phone or laptop screen, and the person's head or hands) must sit between 38% and 66% of the image width, so a narrow vertical crop of the middle still shows it. KEEP THESE AREAS CALM AND SIMPLE (text will be added later by code): the upper-left area (0–60% of the width, 0–30% of the height) and the whole bottom 34% of the image. No readable text, letters, numbers, logos, brand marks or watermarks anywhere — screens show only chart shapes and colored blocks with blurred unreadable labels. Korean stock app colors: rising = red, falling = blue.
```

## 2. TH-PHOTO2 (daebi) — 주말 오후 카페 창가 · 오후 · 비스듬히 뒤 (왼쪽 어깨 뒤 45°) 중간 거리

**저장 경로: `stock/source/daebi-test-2026-11/images/TH-PHOTO2.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Photorealistic YouTube thumbnail background photo, landscape 16:9 (1536x864), looks like a real candid photo, calm and believable — not exaggerated, no dramatic poses, no cartoon, no illustration, no paper-cut style. A sunny weekend afternoon in a bright, ordinary Korean café with large windows; warm golden sunlight, a few green plants, the street outside softly blurred. Medium shot from behind and to the side, about 45 degrees behind the left shoulder, of a woman in her 30s in a beige knit sweater sitting at the window counter, her head turned toward the laptop so only her hair and the back of her shoulder are visible. The laptop screen shows a generic stock trading app whose line first climbs in red and then falls below the starting level in blue. An iced coffee and a small closed notebook sit on the counter. Palette: warm beige, sunlight and soft green — airy and bright. Bottom 34%: the plain light-wood counter surface, softly out of focus. NO face visible anywhere: the main person is seen only from behind, over the shoulder or as hands, and any other people are far away, turned away and heavily blurred; nobody resembles a real individual. The main subject (the phone or laptop screen, and the person's head or hands) must sit between 38% and 66% of the image width, so a narrow vertical crop of the middle still shows it. KEEP THESE AREAS CALM AND SIMPLE (text will be added later by code): the upper-left area (0–60% of the width, 0–30% of the height) and the whole bottom 34% of the image. No readable text, letters, numbers, logos, brand marks or watermarks anywhere — screens show only chart shapes and colored blocks with blurred unreadable labels. Korean stock app colors: rising = red, falling = blue.
```

## 3. TH-PHOTO2 (signal) — 책상 위 (위에서 내려다봄) · 흐린 낮 · 바로 위에서 내려다본 탑뷰

**저장 경로: `stock/source/signal-test-2026-11/images/TH-PHOTO2.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Photorealistic YouTube thumbnail background photo, landscape 16:9 (1536x864), looks like a real candid photo, calm and believable — not exaggerated, no dramatic poses, no cartoon, no illustration, no paper-cut style. Overcast daytime with soft, diffuse window light. A straight top-down (bird's-eye) view of a plain grey desk. In the middle of the frame two hands in a grey sweater hold a smartphone; the phone shows a generic stock trading app with a blue falling line chart. On the right side of the desk only: a folded newspaper business section with chart graphics (all print blurred and unreadable), a brand-new economics study book still in its plastic wrap (no readable title), a pen and a half-finished cup of coffee. Only the hands and forearms are visible — no head, no face. Palette: neutral grey, paper white and muted blue. The left side and the bottom of the desk are empty plain surface. NO face visible anywhere: the main person is seen only from behind, over the shoulder or as hands, and any other people are far away, turned away and heavily blurred; nobody resembles a real individual. The main subject (the phone or laptop screen, and the person's head or hands) must sit between 38% and 66% of the image width, so a narrow vertical crop of the middle still shows it. KEEP THESE AREAS CALM AND SIMPLE (text will be added later by code): the upper-left area (0–60% of the width, 0–30% of the height) and the whole bottom 34% of the image. No readable text, letters, numbers, logos, brand marks or watermarks anywhere — screens show only chart shapes and colored blocks with blurred unreadable labels. Korean stock app colors: rising = red, falling = blue.
```

## 4. TH-PHOTO2 (gongpo) — 새벽 고층 아파트 큰 창가 (미국 장 마감 확인) · 해 뜨기 직전 · 서 있는 사람 허리 위 실루엣

**저장 경로: `stock/source/gongpo-test-2026-11/images/TH-PHOTO2.jpg`** — JPEG 700KB 이하 · 가로 1536×864

```
Photorealistic YouTube thumbnail background photo, landscape 16:9 (1536x864), looks like a real candid photo, calm and believable — not exaggerated, no dramatic poses, no cartoon, no illustration, no paper-cut style. Blue-hour dawn just before sunrise in a high-rise Korean apartment; a large floor-to-ceiling window shows a quiet city skyline with a thin orange glow on the horizon under a deep blue sky. A man in a plain dark t-shirt stands by the window, seen from behind from the waist up as a soft backlit silhouette, head slightly lowered toward the smartphone in his hand (no face visible). The phone's glow lights his hand; the screen shows a generic stock trading app whose line plunges in blue and then rebounds high in red. The room is dim and still. Palette: deep blue and soft orange dawn light, backlit — no lamps. Upper-left: plain dawn sky. Bottom 34%: the plain dark floor and the lower window frame, out of focus. NO face visible anywhere: the main person is seen only from behind, over the shoulder or as hands, and any other people are far away, turned away and heavily blurred; nobody resembles a real individual. The main subject (the phone or laptop screen, and the person's head or hands) must sit between 38% and 66% of the image width, so a narrow vertical crop of the middle still shows it. KEEP THESE AREAS CALM AND SIMPLE (text will be added later by code): the upper-left area (0–60% of the width, 0–30% of the height) and the whole bottom 34% of the image. No readable text, letters, numbers, logos, brand marks or watermarks anywhere — screens show only chart shapes and colored blocks with blurred unreadable labels. Korean stock app colors: rising = red, falling = blue.
```
