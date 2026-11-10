# manspi-jeonmang-2026-11 롱폼 — 애니메이션 키 장면 39장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.0 — 2026-11-10 — 사용자 지시 "너는 왜 영상을 왤케 대충 만들어 전 재산, 은퇴 자금은 이런건 이미지 만들어서 글씨로 표시한 다음 넣는건 움직이는 걸로 다 표현할 수 있잖아 … 최대한 애니메이션 느낌 나도록 요소 위치, 배경, 캐릭터 어우러지게, 동작 표현 하라고 다시 이미지 생성 명령 알려줘봐". 기준 대본 = main 커밋 ac40a5e3 의 `manspi-jeonmang-2026-11.txt` (5장 61문장). 앞 요청(`images_chatgpt.md` v1.0 — 빈 배경 + 따로 자른 인물)은 쓰지 않는다.

**무엇이 바뀌나 — 애니메이션 콘티 방식**
- **키 장면 = 완성된 한 컷**: 배경·인물·소품이 한 그림 안에서 함께 그려진다 (같은 빛·그림자·원근 · 인물이 물건을 실제로 들고·쏟고·던짐). 카메라도 장면마다 넓게·중간·가까이를 바꾼다.
- **동작 = 연속 그림**: '(○번을 고쳐서)'라고 적힌 장은 **바로 앞 그림을 그대로 두고 적힌 부분만 바꿔** 만든다 (같은 카메라·같은 배경·같은 자리) — Claude 가 두 장을 이어 붙여 움직임을 만든다.
- **글자 대신 그림**: '전 재산' = 돼지저금통을 통째로 쏟아붓는 모습 · '은퇴 자금' = 노부부 사진 액자 옆에서 비어 가는 유리 저금병 · '확신에 찬 전망' = 주먹 쥐고 외치는 전문가와 같은 화살표를 띄운 여러 화면.
- **숫자만 코드로**: 그림 속 TV·휴대전화·모니터·판·말풍선은 **비워 두고**, Claude 가 그 화면 위에 숫자(10,000 · 8,000 등)와 짧은 말을 원근에 맞춰 얹는다.

| 번호 | 저장 경로 (모두 `stock/source/manspi-jeonmang-2026-11/anim/`) | 무엇 | 대본 문장 |
|---|---|---|---|
| 1 | `K01.jpg` | 낮 거실 — TV 속 전문가가 외치고, 시청자는 설레며 돼지저금통을 안음 | 1 |
| 2 | `K02.jpg` (1번을 고쳐서) | 시청자가 저금통을 거꾸로 들어 돈을 휴대전화 주식 앱으로 쏟아부음 | 1 |
| 3 | `K03.jpg` | 밤 침실 — 침대 위 시청자, 휴대전화 속 파란 하락 그래프 · 협탁에 노부부 사진과 유리 저금병 | 2 |
| 4 | `K04.jpg` (3번을 고쳐서) | 휴대전화를 이마에 대고 괴로워함 · 저금병이 거의 빔 · 시계는 새벽 | 2 |
| 5 | `K05.jpg` | 회상 — 방송 스튜디오에서 주먹 쥐고 외치는 전문가 + 주변 여러 화면에 같은 상승 화살표 | 3 |
| 6 | `K06.jpg` | 방송국 로비 — 시청자가 하락 화면의 휴대전화를 내밀며 따지고, 전문가는 어깨 으쓱 | 4 |
| 7 | `K07.jpg` (6번을 고쳐서) | 전문가는 등을 돌려 문밖으로 나가고, 시청자만 남음 | 4 |
| 8 | `K08.jpg` | 저녁 거실 — 리모컨으로 TV 를 끄려다 멈칫하며 고민 | 5 |
| 9 | `K09.jpg` | 거실 — 시청자가 큰 거름망(체)을 두 손으로 들고 결의 · 위에서 빈 말풍선 둘이 떨어짐 | 6 |
| 10 | `K10.jpg` | 증권사 분석실 — 전문가가 계산기·서류·빈 모니터 셋과 씨름 | 7~8 |
| 11 | `K11.jpg` (10번을 고쳐서) | 전문가가 수정 구슬을 들여다봄 (안이 뿌옇다) | 9 |
| 12 | `K12.jpg` (10번을 고쳐서) | 모니터 그래프가 아래로 꺾이고, 전문가는 놀라 서류를 떨어뜨림 | 10 |
| 13 | `K13.jpg` | 화이트보드 앞 — 전문가가 목표선을 지우개로 지우고 낮은 자리에 다시 그림 | 11 |
| 14 | `K14.jpg` | 시청자가 커다란 빈 목표 숫자판을 '반드시 된다'는 듯 꼭 껴안음 (반짝이는 눈) | 12 |
| 15 | `K15.jpg` | 리포트 서류 산더미 (같은 모양 도장 자국이 가득) 위에서 전문가가 엄지 척 | 13 |
| 16 | `K16.jpg` | 시청자가 그 서류 산 앞에서 돋보기로 살펴보며 의심 | 14 |
| 17 | `S1.jpg` | 거름망 작업대 — 시청자가 체를 받쳐 들고 위를 봄 · 위에서 빈 말풍선이 떨어지는 중 · 왼쪽 휴지통 · 오른쪽 보관함 | 15~16 · 20 · 25 · 30 · 35~36 · 40 · 45 · 49 |
| 18 | `S2.jpg` (17번을 고쳐서) | 말풍선이 체에 걸리고, 시청자가 체를 흔듦 (움직임 선) | 18 · 23 · 28 · 33 |
| 19 | `S3.jpg` (17번을 고쳐서) | 시청자가 걸린 말풍선을 집어 왼쪽 휴지통에 던짐 | 18 · 23 · 28 · 33 |
| 20 | `S4.jpg` (17번을 고쳐서) | 말풍선이 체를 쏙 통과해 오른쪽 보관함으로 · 시청자 미소 | 38 · 42 · 47 · 51 |
| 21 | `T1.jpg` | TV 스튜디오 가까이 — 전문가가 큰 달력을 손바닥으로 탕 치며 확정하듯 외침 | 16~19 |
| 22 | `T2.jpg` | 전문가가 손목시계를 가리키며 재촉 · 옆 탁자에 모래시계 | 20~24 |
| 23 | `T3.jpg` | 전문가가 가슴을 두드리며 장담 · 한 손에 반짝이는 방패 | 25~29 |
| 24 | `T4.jpg` | 전문가 뒤 큰 화면에 상승 화살표 · 주먹 쥐고 외침 | 30~31 |
| 25 | `T5.jpg` (24번을 고쳐서) | 같은 자리, 뒤 화면은 하락 화살표 · 진땀 흘리며 같은 포즈로 계속 외침 | 31~33 |
| 26 | `T6.jpg` | 전문가가 칠판 앞에서 차분하게 '왜 틀렸는지' 짚어 설명 (빈 칠판에 도형만) | 34 |
| 27 | `K17.jpg` | 시청자가 휴대전화 매수 버튼을 누르려는 자기 손목을 다른 손으로 붙잡아 멈춤 | 24 |
| 28 | `K18.jpg` | 오래 키운 화분(주식 화분)이 시들어 있고 시청자가 물뿌리개를 든 채 낙담 | 29 |
| 29 | `T7.jpg` | 전문가가 칠판에 '조건 상자 → 결과 상자' 화살표 도식을 짚으며 설명 · 옆에서 시청자가 메모 | 36~39 |
| 30 | `T8.jpg` | 전문가가 저울을 들고, 한쪽 접시엔 위 화살표 · 다른 쪽엔 아래 화살표 | 40~43 |
| 31 | `K19.jpg` | 시청자가 '바닥' 표지판(빈 판) 아래로 더 깊게 이어진 구멍을 놀라 내려다봄 | 44 |
| 32 | `T9.jpg` | 전문가가 계획판의 목표선을 손으로 잡아 아래로 옮김 | 45~48 |
| 33 | `T10.jpg` | 전문가가 안개 낀 미래 달력 앞에서 두 손바닥을 펴고 솔직하게 웃음 | 49~52 |
| 34 | `K20.jpg` | 시청자가 반짝이는 트로피를 내려놓고, 두꺼운 설명서와 빈 경고 표지판을 집어 듦 | 53~54 |
| 35 | `K21.jpg` | 아침 거실 — 체를 벽에 걸어 두고, 시청자가 메모장을 들고 차분히 TV 를 봄 | 55~58 |
| 36 | `K22.jpg` | 메모장 가까이 — 빈 두 칸 표 (왼쪽 칸 위 빨간 X 도장, 오른쪽 칸 위 초록 체크 도장, 칸 안은 빈 줄) · 시청자 손이 펜을 듦 | 56~57 |
| 37 | `K23.jpg` | 휴대전화 뉴스 가까이 — 위 굵은 빈 제목 줄 · 아래 빈 본문 줄 여러 개 · 시청자 손가락이 본문을 짚음 | 59 |
| 38 | `K24.jpg` | 아침 창가 — 시청자가 커피를 들고 햇살 속에서 편안히 미소 | 60~61 |
| 39 | `FX.png` (투명 · 소품 8) | 움직임용 조각: 지폐 한 장 · 동전 · 땀방울 · 움직임 선 · 반짝임 · 말풍선 조각 · 먼지 구름 · 작은 하트 | 효과 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
   **★ 먼저 기준 그림 넷을 열어 본다 — 새 그림은 모두 이 그림들과 같은 사람이 그린 것처럼 (그림체·선 굵기·색·얼굴 꼴·비율·옷까지 같게).**
   - 썸네일: https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/1bcbf5532537e13ce5b1c1cd1402ffe328c59371/stock/source/manspi-jeonmang-2026-11/images/TH-CHAR.jpg (왼쪽 '-50%' 글자는 따라 그리지 않음)
   - 시청자(V): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/V-CALM.png · https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/V-NIGHT.png
   - 전문가(E): https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/E-HYPE.png · https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/a73df33de78cbd63cc915a1732de483a75020557/stock/source/manspi-jeonmang-2026-11/puppet/E-CALM.png
   그림을 열 수 없으면 아래 '공통 화풍'과 '인물' 설명대로 그린다.
1. 아래 1~39번 **39장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 **공통 화풍** 문단을 붙인다. 인물이 나오는 장(39번 빼고 모두)은 그다음 **인물** 문단, 그다음 **장면 규칙** 문단을 붙인다. 39번은 공통 화풍 + **FX** 문단만.
3. **'(○번을 고쳐서)' 장은 반드시 그 번호 그림을 편집해서** 만든다 — 카메라·배경·가구·빛·인물의 자리와 크기를 그대로 두고, 프롬프트에 적힌 부분만 바꾼다. 처음부터 새로 그리지 않는다.
4. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — TV·휴대전화·모니터·칠판·판·말풍선·달력·서류·도장 자국·표지판에도 없음 (빈 화면이나 단순한 선·도형만). 화살표·X·체크 같은 그림 기호는 됨. 실제 방송사·증권사·은행·앱의 이름·로고·색을 닮게 그리지 않는다. 날씨(해·구름·비·번개 · 창밖 하늘)는 그리지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.
5. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. stock/source/manspi-jeonmang-2026-11/anim/K01.jpg`). 그림 안에는 쓰지 않는다.
6. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자까지 같게, 폴더는 `stock/source/manspi-jeonmang-2026-11/anim/`).
   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     - 1~38번(JPEG): RGB · 크기 1536×864 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.
     - 39번(PNG, 투명 유지): 256색으로 줄여서라도 700KB 아래로 (크기 1536×1024 그대로).
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[stock] manspi-jeonmang-2026-11 anim <파일 이름> 이미지` (예: `[stock] manspi-jeonmang-2026-11 anim K01.jpg 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 공통 화풍 (1~39번 모든 프롬프트 맨 앞에 그대로 붙임)

```
STYLE: Match exactly the art style of the reference images: a polished flat 2D cartoon animation still with bold clean dark outlines, flat colors with one simple cel-shading tone and small highlights, expressive exaggerated faces (big eyes, clear eyebrows, open mouths, tears or sweat when needed) and strong, readable body language, like a keyframe from a high-quality 2D animated series. Slightly chunky proportions (head about one quarter of the body height). It is a 2D drawing — not a 3D render, not clay, not a photo. Absolutely no text, letters, numbers, logos or watermarks anywhere — TVs, phones, monitors, boards, papers, calendars, signs and speech bubbles are blank or show only simple shapes, lines and arrows. No weather and no sky (no sun, clouds, rain, lightning; windows show only soft light or blurred indoor reflections).
```

## 인물 (인물이 나오는 장 — 공통 화풍 다음에 그대로 붙임)

```
CHARACTERS — draw them exactly like the reference images, same face, hair, clothes and proportions:
V (the viewer) — an ordinary Korean man around 40 who invested his savings: messy curly medium-brown hair, an olive-green casual button jacket with flap pockets over a beige checked shirt, brown trousers with a brown belt, brown shoes. A kind, emotional face that shows feelings strongly.
E (the expert) — a Korean TV stock-market commentator in his 50s: neatly combed dark hair with gray streaks at the temples, navy-blue suit, white shirt, red tie, black shoes. Smug and loud when hyping; calm and sincere in his calm scenes. A generic fictional person, not any real commentator.
```

## 장면 규칙 (인물이 나오는 장 — 인물 문단 다음에 그대로 붙임)

```
SCENE: landscape 1536x864, one complete illustrated animation frame. The characters are drawn INSIDE the scene, not pasted on: same lighting and color temperature as the room, soft contact shadows under feet and objects, correct scale and perspective for where they stand, hands really holding, pouring, throwing or touching the props. Clear staging with one main action that reads instantly; keep the face and the main action inside the middle 80% of the frame. Leave the bottom 15% of the frame free of faces and important hands (subtitles go there). Any screen, board or paper that would show numbers or words stays blank and clearly visible (it will be filled later).
```

## FX (39번만 — 공통 화풍 다음에 그대로 붙임)

```
FX SHEET: landscape 1536x1024, 4 columns x 2 rows of equal invisible cells, one isolated small effect element centered in each cell, on a fully transparent background (PNG with alpha) — no background, no shadows, nothing touching the cell borders. If transparency is impossible, use one flat pure magenta #FF00FF background and no magenta or pink on the elements.
```

## 1. K01 — 낮 거실: TV 속 전문가 · 설레는 시청자

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K01.jpg`** — JPEG 700KB 이하 · 1536×864

```
Wide shot of a bright small Korean apartment living room in the daytime. On the left wall a large flat TV shows E in a studio, pointing up and shouting confidently, with a big red arrow rising behind him (no text). In the center-right, V stands on the rug facing the TV, eyes sparkling with excitement and a hopeful open-mouthed smile, hugging a big pink piggy bank to his chest with both arms. A smartphone lies on the coffee table in front of him with its blank screen glowing. Warm, hopeful mood.
```

## 2. K02 — (1번을 고쳐서) 전 재산을 쏟아붓기

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K02.jpg`** — JPEG 700KB 이하 · 1536×864

```
Edit picture 1: keep the same room, camera, TV and V's position. Now V holds the piggy bank upside down with both hands above the coffee table and shakes it hard; a big stream of paper banknotes and coins pours out and flies into the glowing smartphone screen on the table, which shows a simple red rising line. V's face is determined and eager, motion lines around the piggy bank. The piggy bank is almost empty.
```

## 3. K03 — 밤 침실: 은퇴 자금 · 하락

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K03.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot of a dark bedroom late at night, lit only by a small bedside lamp and the cold blue glow of a phone. V sits on the edge of the bed in pajama pants and his olive jacket thrown over his shoulders, staring at his smartphone; the screen shows a big blue line falling steeply (no numbers). On the bedside table: a framed photo of a smiling elderly couple (retirement dream) and a glass savings jar with only a few coins left at the bottom, a round alarm clock without numbers. V's face is pale and worried, dark circles under his eyes.
```

## 4. K04 — (3번을 고쳐서) 밤마다 계좌

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K04.jpg`** — JPEG 700KB 이하 · 1536×864

```
Edit picture 3: keep the same bedroom, camera, lamp and furniture. Now V presses the glowing phone against his forehead with both hands, eyes squeezed shut, shoulders slumped, a small tear; the glass savings jar on the bedside table is now completely empty; the alarm clock hands point to very late night.
```

## 5. K05 — 회상: 확신에 찬 전망이 쏟아짐

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K05.jpg`** — JPEG 700KB 이하 · 1536×864

```
Wide shot of a glossy TV economics studio. E stands in the center under bright spotlights, both fists clenched, shouting with excitement. Around him float several screens of different sizes — a TV, a smartphone, a tablet and a folded newspaper page — and every one of them shows the same big red rising arrow (no text, no numbers). Slightly soft, dreamy edges around the frame to show it is a memory. Loud, overconfident mood.
```

## 6. K06 — 방송국 로비: 따지는 시청자 · 으쓱하는 전문가

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K06.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium-wide shot of a broadcasting building lobby with glass doors on the right. On the left, V leans forward holding out his smartphone toward E; the screen shows a blue falling line; V's face is angry and pleading, his other hand holding an empty piggy bank. On the right, E faces V and shrugs with both palms up and an awkward fake smile, a briefcase at his feet. Tense mood.
```

## 7. K07 — (6번을 고쳐서) 아무도 책임지지 않음

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K07.jpg`** — JPEG 700KB 이하 · 1536×864

```
Edit picture 6: keep the same lobby, camera and V's position. Now E is seen from behind, walking out through the glass doors on the right with his briefcase, one hand raised in a casual wave without looking back. V stands alone on the left, arms dropped, the phone hanging from one hand and the empty piggy bank in the other, mouth slightly open in disbelief.
```

## 8. K08 — 저녁 거실: 끄려다 멈칫

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K08.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot of the same living room as picture 1 in the warm evening lamp light. V sits on the sofa holding the TV remote out toward the TV, about to switch it off, but he pauses with his thumb above the button, eyebrows knitted, thinking hard. On the TV, E is talking with a calm explaining gesture. A notepad and pen lie on the coffee table.
```

## 9. K09 — 거실: 거름망을 든 결의

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K09.jpg`** — JPEG 700KB 이하 · 1536×864

```
Low-angle heroic medium shot in the living room. V stands firmly with a determined smile, holding a big round kitchen sieve (wooden rim, fine metal mesh) with both hands in front of his chest like a tool. Above him, two blank white speech bubbles are falling toward the sieve — one spiky shouting bubble and one round calm bubble. A red trash bin stands on the floor to his left and a green wooden box to his right. Bright, motivated mood.
```

## 10. K10 — 증권사 분석실: 계산하는 전문가

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K10.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium-wide shot of a securities firm analyst office during the day. E sits at a long desk, rolling up his sleeves, pressing a calculator with one hand and holding a paper report in the other, surrounded by stacks of blank paper reports and coffee cups. Three monitors stand on the desk in a row facing the viewer, each showing only a blank pale screen with a simple empty chart frame. A whiteboard on the side wall is blank. Busy, focused mood.
```

## 11. K11 — (10번을 고쳐서) 예상일 뿐

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K11.jpg`** — JPEG 700KB 이하 · 1536×864

```
Edit picture 10: keep the same office, camera, desk and monitors. Now E leans forward and peers into a glass crystal ball on the desk with a puzzled squint; inside the ball there is only swirling fog and faint arrows pointing in different directions. The calculator lies aside.
```

## 12. K12 — (10번을 고쳐서) 실적이 나빠지면

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K12.jpg`** — JPEG 700KB 이하 · 1536×864

```
Edit picture 10: keep the same office, camera, desk and E's chair. Now the three monitors each show a line that drops sharply downward in blue (no numbers), and E jumps half up from his chair in surprise, eyes wide, the paper report slipping out of his hands with sheets flying in the air.
```

## 13. K13 — 화이트보드: 목표를 고쳐 그림

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K13.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot of E standing at a large whiteboard in the analyst office. On the board: a simple chart with an upper dashed target line half-erased and a new dashed line drawn lower. E holds an eraser in one hand and a marker in the other, calmly redrawing the lower line, with a sincere, slightly embarrassed but responsible expression. Calm mood.
```

## 14. K14 — 목표 숫자를 맹신

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K14.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot in the living room. V hugs a huge blank golden target board (a big plain rectangular plaque with a shiny frame, nothing written on it) with both arms as if it were a treasure, cheek pressed against it, eyes shining with stars of blind belief, little sparkles around. Slightly comical mood.
```

## 15. K15 — 매수 의견 서류 산더미

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K15.jpg`** — JPEG 700KB 이하 · 1536×864

```
Wide shot: an enormous mountain of paper reports piled up in the analyst office, nearly touching the ceiling; almost every sheet has the same round red stamp mark (an empty round stamp, no text) and only one small sheet near the bottom has a different blue stamp mark. E stands on top of the paper mountain giving a big confident thumbs-up and grinning. Comical, exaggerated mood.
```

## 16. K16 — 돋보기로 의심

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K16.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot at the foot of the same paper mountain. V leans in with a big magnifying glass, examining the red-stamped papers with one eyebrow raised and a suspicious squint, his other hand on his chin. The paper mountain fills the background. Curious, skeptical mood.
```

## 17. S1 — 거름망 작업대: 떨어지는 말

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/S1.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium-wide shot of a cozy workshop corner with a long wooden workbench. V stands behind the bench in the center holding a big round kitchen sieve (wooden rim, fine metal mesh) with both hands at chest height, looking up attentively. One blank white speech bubble is falling from the top of the frame toward the sieve. On the floor at the left end of the bench a red trash bin; at the right end a green wooden keep box with its lid open. Keep the upper-center area above the sieve open (bubbles fall there). Lively mood.
```

## 18. S2 — (17번을 고쳐서) 체에 걸림

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/S2.jpg`** — JPEG 700KB 이하 · 1536×864

```
Edit picture 17: keep the same workshop, camera, bench, bin and box, and V's position. Now the blank white speech bubble is caught on top of the sieve mesh and cannot pass through; V shakes the sieve hard with a frowning "no way" face, motion lines around the sieve.
```

## 19. S3 — (17번을 고쳐서) 휴지통에 던짐

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/S3.jpg`** — JPEG 700KB 이하 · 1536×864

```
Edit picture 17: keep the same workshop, camera, bench, bin and box. Now V holds the sieve in one hand and with the other hand throws the crumpled blank speech bubble into the red trash bin on the left; the crumpled bubble flies in an arc with motion lines; V's face is firm and satisfied.
```

## 20. S4 — (17번을 고쳐서) 통과해 보관함으로

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/S4.jpg`** — JPEG 700KB 이하 · 1536×864

```
Edit picture 17: keep the same workshop, camera, bench, bin and box, and V's position. Now a small neat blank white card passes down through the sieve mesh and slides into the green keep box on the right with a soft glow; V watches it with a warm, approving smile.
```

## 21. T1 — TV 스튜디오: 날짜를 못 박는 말

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/T1.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium close-up in the TV studio. E slams his palm onto a big wall calendar page beside him (a plain grid with no numbers, one square circled in red) and shouts with total certainty, other fist raised, a blank spiky speech bubble coming out of his mouth. Bright studio lights. Overconfident mood.
```

## 22. T2 — TV 스튜디오: 재촉하는 말

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/T2.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium close-up in the TV studio. E taps his wristwatch urgently with one finger and leans toward the viewer with an eager pushy grin, as if saying "now or never"; on the desk beside him an hourglass with sand running fast; a blank round speech bubble near his mouth. Hurried mood.
```

## 23. T3 — TV 스튜디오: 장담하는 말

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/T3.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium close-up in the TV studio. E pats his chest proudly with one hand and holds up a shiny golden shield in the other, winking with a smug "trust me" grin; a blank spiky speech bubble near his mouth. Boastful mood.
```

## 24. T4 — TV 스튜디오: 상승 화면 앞 외침

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/T4.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot in the TV studio. Behind E a big screen shows a thick red arrow rising to the top right (no numbers). E stands in front of it pointing up with one hand, the other fist clenched, shouting confidently.
```

## 25. T5 — (24번을 고쳐서) 하락 화면 앞에서도 같은 말

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/T5.jpg`** — JPEG 700KB 이하 · 1536×864

```
Edit picture 24: keep the same studio, camera and E's exact pose and position. Only change: the big screen behind him now shows a thick blue arrow falling to the bottom right, and E is sweating heavily with big sweat drops while still shouting the same way with a forced grin.
```

## 26. T6 — 칠판: 왜 틀렸는지 설명

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/T6.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot. E stands calmly at a green chalkboard, pointing with a stick at a simple diagram drawn in chalk: a line that went up, then a break mark, then a line going down, with two empty boxes next to the break (no words). His face is honest and serious. Calm, trustworthy mood.
```

## 27. K17 — 조급한 손을 멈춤

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K17.jpg`** — JPEG 700KB 이하 · 1536×864

```
Close-up from the side: V holds his smartphone; his right index finger is about to press a big blank red button on the screen, but his own left hand grabs his right wrist to stop it. His face, visible at the edge, shows a tense, self-restraining expression with a drop of sweat. Dramatic but slightly comical mood.
```

## 28. K18 — 시든 화분

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K18.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot by a windowsill indoors. A potted plant that V has been raising for a long time is wilted and drooping, with fallen leaves around the pot; a small blank tag stick is in the soil. V stands next to it holding a watering can, shoulders slumped, looking down at it sadly. Quiet, melancholy mood.
```

## 29. T7 — 조건을 붙이는 말

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/T7.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium-wide shot. E stands at a whiteboard pointing calmly at a simple diagram: an empty box on the left, an arrow, and an empty box on the right (no words). V sits at a small table on the right side of the frame, writing in a notepad and nodding. Calm, clear mood.
```

## 30. T8 — 하락 가능성도 말하는 말

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/T8.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot. E holds up a brass balance scale in front of him; on one pan sits a small red arrow pointing up, on the other pan a small blue arrow pointing down, the scale nearly level. E's face is calm and balanced, eyebrows relaxed. Plain, softly lit studio background.
```

## 31. K19 — 바닥이 바닥이 아님

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K19.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot: V stands at the edge of a big hole in a cartoon ground; a blank signpost labeled with nothing (just a plain board) is stuck at the rim marking "the bottom", but the hole clearly continues much deeper below it into darkness. V leans over, looking down with wide surprised eyes, one hand on his head. Slightly comical, cautionary mood.
```

## 32. T9 — 바꿀 기준을 말하는 말

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/T9.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot. E stands next to a large plan board on an easel showing a simple chart with a horizontal target line; with one hand he grips the target line and moves it downward (motion lines), while his other hand points to a small empty box at the corner of the board. His expression is calm and businesslike.
```

## 33. T10 — 모르는 것은 모른다는 말

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/T10.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot. E stands in front of a big wall calendar whose future pages fade into thick fog (plain grids, no numbers); he shows both open palms toward the viewer with an honest, humble smile, as if saying "I don't know that". Soft gentle lighting.
```

## 34. K20 — 결과보다 근거와 위험

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K20.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot on a table in the living room: V sets a shiny golden trophy down to the side with one hand and with the other hand picks up a thick plain manual book and a small blank yellow warning-triangle sign. His face is thoughtful and wise, a small knowing smile.
```

## 35. K21 — 아침 거실: 차분하게 TV 를 봄

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K21.jpg`** — JPEG 700KB 이하 · 1536×864

```
Wide shot of the same living room as picture 1, now in fresh morning light, tidy and calm. The big round sieve hangs on the wall like a trusted tool. V sits relaxed on the sofa holding a notepad and pen, watching the TV calmly; on the TV, E is talking (small, blank speech bubble). A cup of coffee on the table. Peaceful, confident mood.
```

## 36. K22 — 메모장 두 칸

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K22.jpg`** — JPEG 700KB 이하 · 1536×864

```
Close-up from above of an open notepad on the coffee table, filling most of the frame. The page is divided into two columns by a line: at the top of the left column a red X stamp mark, at the top of the right column a green check stamp mark; under each, three empty ruled lines (no writing). V's hand holds a pen at the right edge of the page. Morning light.
```

## 37. K23 — 뉴스 제목보다 본문

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K23.jpg`** — JPEG 700KB 이하 · 1536×864

```
Close-up of V's hand holding a smartphone showing a news article layout: a bold blank headline bar at the top (no letters, just a thick block shape), and many thin blank text lines below; V's index finger points to the body lines below the headline. Background softly blurred living room in morning light.
```

## 38. K24 — 아침 창가 미소

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/K24.jpg`** — JPEG 700KB 이하 · 1536×864

```
Medium shot by a large window indoors in warm morning light (the window shows only soft bright light, no sky). V holds a mug of coffee with both hands and smiles peacefully, eyes gently closed for a moment, shoulders relaxed. Hopeful, calm ending mood.
```

## 39. FX — 움직임용 조각 (투명)

**저장 경로: `stock/source/manspi-jeonmang-2026-11/anim/FX.png`** — PNG 700KB 이하 · 투명 · 1536×1024 · 8칸

```
Eight effect elements in order, left to right then top to bottom: (1) a single green paper banknote, slightly curved, no text; (2) a single gold coin seen at an angle, no symbols; (3) a big cartoon sweat drop; (4) a small set of three curved motion lines; (5) a four-pointed sparkle; (6) a small torn piece of a white speech bubble; (7) a small puff of cartoon dust; (8) a small red heart.
```

## 받은 뒤 (Claude)
- 장마다 확대해서 검수한다: 기준 그림과 같은 사람·그림체 · 글자·숫자 없음 · '고쳐서' 장이 앞 그림과 같은 카메라·자리인지.
- 영상: 키 장면을 문장 시각에 맞춰 놓고, 카메라 움직임(천천히 밀기·옮기기) · 연속 그림 바꾸기(1→2, 3→4, 6→7, 10→11→12, 17→18→19, 17→20, 24→25) · FX 조각(떨어지는 지폐·땀·반짝임) · 그림 속 빈 화면에 숫자(10,000 · 8,000 등)와 짧은 말을 원근에 맞춰 얹기 — `video/episodes/manspi-jeonmang-2026-11/index.html` v2.0.
