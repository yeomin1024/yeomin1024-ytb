# AI 안경 수능 늑장 대응 쇼츠 — 실사 이미지 11장 (ChatGPT용)

작성: 2026-11-16 v1.2 (Claude) — 면세 쇼츠처럼 '세 칸' 배치: 위·아래는 문구 칸(검정), 사진은 가운데 칸에만 → 모든 사진을 가로 3:2 (1536×1024)로 (사용자 지시 2026-11-16 "면세 쇼츠처럼 위아래 문구 영역있고 중간에만 이미지넣을 거야 다시 수정해")
(이전 v1.1 — 모든 장면에서 사람 이목구비(눈·코·입)가 안 보이게 (사용자 확인 2026-11-16 "사람 이목구비는 안나오게 하는거지?") · S00 눈 클로즈업 → 뒤에서 본 안경 · S02·S07 옆모습·흐린 얼굴 → 뒷모습만)
(이전 v1.0 — 사용자 지시 2026-11-16 "다시 지시사항 파일을 만들고 그걸 참고해서 저장소에 이미지 업로드 하도록 명령 알려줘" · 앞 지시 "지시사항은 신경쓰지말고 그냥 어울리는 실사사진 만들면 돼")

**이것만 만든다:** 세로 쇼츠의 **가운데 칸에만** 넣을 가로 실사 사진 11장 (`S00.jpg` ~ `S10.jpg`). 대본 문장마다 한 장이다.

**배치 (면세 쇼츠와 같은 '세 칸' — 1080×1920):** 위 칸 y 0~691 = 검정 바탕 + 문구 (Claude 가 코드로) · **가운데 칸 y 691~1382 = 이 사진 (가로 끝까지 1080×691)** · 아래 칸 y 1382~1920 = 검정 바탕 + 자막. 그래서 사진은 **가로 3:2 (1536×1024)** 로 만들고, 가운데 칸 비율(약 1.56:1)에 맞춰 위아래가 조금(각 약 1.5%) 잘린다 → **중요한 물건·사람은 사진 가운데에, 위아래 끝 5% 안에는 두지 않는다.** 사진에 검은 테두리·여백을 넣지 않는다 (가장자리까지 사진으로 채움). 대본은 이 파일 맨 아래에 있다.
※ 정보 전달용 시사 쇼츠 — 실제 인물·기관을 그리지 않는다.

| 번호 | 파일 (1536×1024 JPEG · 가로) | 대본 문장 | 장면 |
|---|---|---|---|
| 0 | `new/shorts/ai-glasses-2026-11/images/S00.jpg` | (첫 장면·썸네일) | 뒤에서 본 수험생 — 안경다리의 작은 카메라·렌즈 안쪽 희미한 빛 |
| 1 | `new/shorts/ai-glasses-2026-11/images/S01.jpg` | 애꿎은 수험생들만 피해 보게 생겼음 | 밤 교실, 머리 감싼 학생 뒷모습 |
| 2 | `new/shorts/ai-glasses-2026-11/images/S02.jpg` | 최초 적발 사례는 5월 중순, 자격증 시험과 토익 | 성인 시험장, 감독관이 한 응시자 안경을 의심 |
| 3 | `new/shorts/ai-glasses-2026-11/images/S03.jpg` | 벌금형, 금지 물품 목록에 한 줄 넣은 게 다 | 판사봉 + 스마트 안경 + 흐린 종이 한 장 |
| 4 | `new/shorts/ai-glasses-2026-11/images/S04.jpg` | 다른 나라엔 이미 선례가 있었음 | 큰 시험 날 아침, 시험장 정문 보안 검색 줄 |
| 5 | `new/shorts/ai-glasses-2026-11/images/S05.jpg` | 중국은 안경을 벗겨서 검사 | 검사대 위 벗어 놓은 안경들, 장갑 낀 손이 살핌 |
| 6 | `new/shorts/ai-glasses-2026-11/images/S06.jpg` | 시험장 전파까지 막았음 | 학교 옆 안테나 달린 전파 감시 차량 |
| 7 | `new/shorts/ai-glasses-2026-11/images/S07.jpg` | 수능이 코앞인데 이제서야 대책 논의 | 자정 무렵 정부 회의실, 서류 더미 |
| 8 | `new/shorts/ai-glasses-2026-11/images/S08.jpg` | "난 몰라, 니들이 알아서 해" | 혼자 선 학생 너머로 등 돌리고 걸어가는 정장 차림 |
| 9 | `new/shorts/ai-glasses-2026-11/images/S09.jpg` | 세무사 수석 합격자가 자백 안 했으면 | 셔츠 단추로 위장한 초소형 카메라 클로즈업 |
| 10 | `new/shorts/ai-glasses-2026-11/images/S10.jpg` | 무능도 정도가 있지 | 수능 날 아침 텅 빈 시험실, 차가운 겨울 햇빛 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 0~10번 **11장을 번호 순서대로 모두** 만든다. 질문하지 말고 멈추지 말고 다음 장으로.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓴다. 모두 **가로 3:2 (1536×1024) 실사 사진** — 세로로 만들지 않는다 · 그림·만화·일러스트 ✗ · 사진 안에 위아래 검은 띠나 여백을 만들지 않는다 (띠는 영상에서 붙임).
3. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 종이·화면·현수막·벽시계 숫자도 흐려서 읽히지 않게. 확대해 글자가 읽히면 다시 만든다.
4. **모든 장면에서 사람의 이목구비(눈·코·입)가 하나도 보이지 않게 한다** — 뒷모습·손·실루엣·멀리 작은 사람만. 옆모습·흐린 얼굴도 ✗. 확대해 눈·코·입이 보이면 다시 만든다. 실제 사람·연예인·정치인을 닮게 그리지 않고, 실제 기관 로고·국기·제품 상표(메타·레이밴 등)를 그리지 않는다.
5. 11장이 한 영상에 이어지므로 **색감은 모두 차갑고 차분한 뉴스 다큐 톤**으로 맞춘다 (과장된 표정·포즈 ✗).
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다. 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다** — `yeomin1024/yeomin1024-ytb` **main** 브랜치, 표의 경로 그대로. **올리기 전에 JPEG 700KB 이하로** (RGB · 크기 그대로 1536×1024 · 품질 90부터 5씩 낮춰 700KB 아래가 되는 첫 값 — GitHub 앱이 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다). 커밋 메시지: `AI 안경 쇼츠 이미지 S00~S10 (ChatGPT)`.
   - **올리기가 실패한 장만** 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 0. S00 — 첫 장면·썸네일

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S00.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders, looks like a real news photograph, no illustration, no cartoon. Close-up taken from directly behind and slightly to one side of a Korean high school student sitting an exam: only the back of the head, short dark hair, one ear and the temple arm of thick black-framed eyeglasses are visible. A tiny camera lens is visible on the front corner of the glasses frame, and the inner side of one lens glows faintly like a hidden display. Beyond the student, a blurred exam paper on the desk (unreadable) and a blurred classroom with rows of desks. The face is completely hidden: no eyes, nose or mouth visible. Tense mood, cool blue-gray tones, shallow depth of field. No text, no numbers, no logos, no watermark.
```

## 1. S01 — 애꿎은 수험생들만 피해 보게 생겼음

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S01.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders, looks like a real documentary photograph, no illustration. Late night before Korea's college entrance exam: a Korean high school student in a school uniform, seen from behind, sits alone at a desk in a dark classroom with both hands holding their head. Only a small desk lamp is on, lighting open workbooks with unreadable pages. Dark windows behind. Lonely, anxious, quiet mood, cool tones. No human facial features visible. No text, no numbers, no logos, no watermark.
```

## 2. S02 — 최초 적발 사례는 5월 중순, 자격증 시험과 토익

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S02.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders, looks like a real news photograph, no illustration. A large exam hall for adults taking a certification test, rows of desks with answer sheets (unreadable). In the foreground, an exam proctor seen from behind stands still and looks suspiciously at one adult test-taker's thick-framed eyeglasses; the test-taker is also seen only from behind, face completely hidden. Daylight from high windows, neutral gray tones, tense quiet atmosphere. No human facial features visible. No readable text, no numbers, no logos, no watermark.
```

## 3. S03 — 걸린 사람은 벌금형, 금지 물품 목록에 한 줄 넣은 게 다

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S03.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape still-life photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders, no illustration. On a dark wooden desk: a wooden judge's gavel lies next to a pair of black smart glasses with a tiny camera lens on the frame. Beside them is a single sheet of paper with a short list, the writing completely blurred and unreadable. Cold, dim side lighting, gray-blue tones, a sense of something small and insufficient. No human facial features visible. No readable text, no numbers, no logos, no brand marks, no watermark.
```

## 4. S04 — 이게 말이 안 되는 게, 다른 나라엔 이미 선례가 있었음

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S04.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders, looks like a real news photograph taken from a distance, no illustration. Early morning of a huge national exam day in an East Asian city: a long line of students waits at a school gate while security staff in uniforms stand beside walk-through metal detector gates and inspection tables. People appear small and anonymous, no clear faces. Overcast sky, cool tones, orderly and strict atmosphere. Any banners or signs are blank or blurred. No human facial features visible. No readable text, no numbers, no logos, no flags, no watermark.
```

## 5. S05 — 중국은 수능과 비슷한 큰 시험에서도 안경을 벗겨서 검사하고

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S05.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape close-up photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders, looks like a real news photograph, no illustration. At an exam venue entrance, many pairs of ordinary eyeglasses removed by students are lined up neatly on a gray inspection table. A security inspector's gloved hands hold up one pair of glasses, carefully examining the lenses and temple arms. Background softly blurred with a queue of students. Bright but cool daylight, strict and meticulous mood. No human facial features visible. No readable text, no numbers, no logos, no watermark.
```

## 6. S06 — 시험장 전파까지 막았음

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S06.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders, documentary style, no illustration. A white radio-signal monitoring van with several antennas on its roof is parked beside a school building on exam day. Through the open side door, a monitor inside shows a glowing signal waveform graph without any readable labels. Overcast sky, cool gray-blue tones, serious atmosphere. No human facial features visible. No readable text, no numbers, no logos, no license plate text, no watermark.
```

## 7. S07 — 근데 우리나라는 수능이 코앞인데 이제서야 구체적인 대책 논의 하고 있음

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S07.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders, looks like a real news photograph, no illustration. A government conference room late at night: a long meeting table covered with piles of documents, open folders and cold paper coffee cups. Several people in dark suits, seen only from behind with no faces visible, hurriedly flip through papers. A wall clock shows near midnight but its numbers are not readable. Harsh fluorescent light, tired and rushed atmosphere, cool tones. No human facial features visible. No readable text, no numbers, no logos, no flags, no name plates with text, no watermark.
```

## 8. S08 — 이건 그냥 수험생들한테 "난 몰라, 니들이 알아서 해" 하는 수준임

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S08.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders, cinematic documentary style, no illustration. In a long empty corridor of a public building, a Korean high school student in a school uniform stands alone in the foreground, seen from behind, holding a backpack strap. Far down the corridor, a person in a dark suit walks away with their back turned, not looking back. Long shadows, cold lonely light, feeling of being abandoned. No faces visible. No human facial features visible. No readable text, no numbers, no logos, no signs, no watermark.
```

## 9. S09 — 더 놀라운 건, 세무사 수석 합격자가 자백 안 했으면

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S09.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape macro photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders, looks like a forensic evidence photograph, no illustration. Extreme close-up of a dark navy shirt where one of the buttons is actually a tiny hidden camera, its small lens catching a glint of light. Shallow depth of field, the other buttons blurred. Dark, tense, investigative mood. No person's face, no readable text, no numbers, no logos, no watermark.
```

## 10. S10 — 무능도 정도가 있지, 이건 너무 심한 거 아님?

**저장 경로: `new/shorts/ai-glasses-2026-11/images/S10.jpg`** — JPEG 700KB 이하 · 가로 1536×1024 (쇼츠 가운데 칸)

```
Photorealistic landscape photo, 3:2 (1536x1024), framed for a wide horizontal band in the middle of a vertical video — main subject centered, nothing important near the top or bottom edges, image fills the whole frame with no borders, documentary style, no illustration. Early morning of Korea's college entrance exam day: an empty exam classroom with neat rows of wooden desks and chairs, nobody inside. Cold winter sunlight slants through the windows across the desks, dust visible in the light. Heavy, bitter, quiet mood, muted cool tones. No human facial features visible. No readable text, no numbers, no logos, no watermark.
```

## 대본 (참고 — 사용자 문장 그대로, 2026-11-16)

```
또 일 못하는 정부 때문에 애꿎은 수험생들만 피해 보게 생겼음.
우리나라 AI 안경 최초 적발 사례는 5월 중순, 자격증 시험과 토익이었는데
걸린 사람은 벌금형, 수능 금지 물품 목록에 AI 안경 한 줄 넣은 게 다였음.
이게 말이 안 되는 게, 다른 나라엔 이미 선례가 있었음.
중국은 6월 수능과 비슷한 큰 시험에서도 모든 안경을 벗겨서 검사하고, 시험장 전파까지 막았음.
근데 우리나라는 수능이 코앞인데 이제서야 구체적인 대책 논의 하고 있음
이건 그냥 수험생들한테 "난 몰라, 니들이 알아서 해" 하는 수준임.
더 놀라운 건, 세무사 수석 합격자가 자백 안 했으면 공론화 되지도 않아서 대책 논의도 안했을 거임
무능도 정도가 있지, 이건 너무 심한 거 아님?
```
