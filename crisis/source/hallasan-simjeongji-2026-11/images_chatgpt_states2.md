# hallasan-simjeongji-2026-11 — 추가 그림 3장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.0 — 2026-11-27 — 사용자 지시 "영상도 맘에 안들어 … 인물 대화 같은 건 말풍선 … 최대한 이미지들, 포커스, 화면 효과(빨개지거나), 이펙트 요소들 등 모든 기술 사용해서 애니메이션 처럼 동적으로 만들어 … 추가 이미지 더 필요하면 명령 알려주고" — 대본 v4.1 의 새 장 '혼자 산에 가야 한다면'과 '발견' 장면용.

**어떻게 쓰는가** — 앞 요청 파일(`images_chatgpt_states.md`)과 같은 꼴: 실루엣 시트는 Claude 가 흰 바탕을 지워 칸을 바꿔 움직이게 하고(`tools/sil_sheet.py`), 배경판 위에 얹는다. 그림이 오기 전에는 장면 파일이 다른 그림으로 대신한다.
※ 안전 교육 영상(연구·교육용). 피·상처·시신·공포 연출 없음. 그림 속 글자·숫자 없음.

| 번호 | 저장 경로 (모두 `crisis/source/hallasan-simjeongji-2026-11/` 아래) | 칸 | 무엇 | 대본 (v4.1) |
|---|---|---|---|---|
| 1 | `images/SIL-12-SOLO.jpg` | 3×2 | 혼자 산에 가는 등산객: 출발 전 휴대폰으로 연락 · 표지판 앞에서 확인 · 큰 길을 걸음 · 멈춰 가슴에 손 · 앉아서 전화(신고) · 지나가는 사람에게 손을 들어 부름 | '혼자 산에 가야 한다면' 장 |
| 2 | `images/PLT-09-DROPPED.jpg` | 배경 | 숲길 가장자리 낙엽 위에 떨어진 모자와 작은 배낭 (사람 없음) | 3장 '쓰러진 김 씨를 찾았습니다' |
| 3 | `images/PLT-10-SIGNPOST.jpg` | 배경 | 옆에서 본 숲길 · 길가에 빈 판이 달린 위치 표지 기둥 하나 (글자·숫자 없음) | 점검 장 '위치 표지판 번호' · 혼자 장 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성:' 줄을 그대로 옮겨 적는다.
1. 아래 1~3번 **3장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 앞에 블록을 붙인다 — 1번: 실루엣 시트 화풍 → 인물 윤곽 → 프롬프트 · 2·3번: 다큐 재연 화풍 → 프롬프트.
3. **실루엣 시트(1번)**: 바탕은 완전한 흰색 하나(#FFFFFF), 사람과 물건은 완전한 검정 하나(#000000) — 안쪽 선·회색·그림자·얼굴·바닥선·칸 나눔 선 없음. 칸마다 한 동작, 칸 가운데, 가장자리에서 40픽셀 넘게 떨어지고 옆 칸과 닿지 않게. 모든 칸에서 같은 사람·같은 크기·발바닥은 칸 높이 90% 선. 어기면 다시 만든다.
4. **배경판(2·3번)**: 옆에서 본 장면 · 사람·동물 없음 · 글자·숫자·로고 없음 (표지 기둥의 판은 빈 판) · 앞 요청 파일의 둘레길 숲(제주 중산간 삼나무·화산석·고사리)과 같은 숲으로 보이게.
5. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다. 그림 안에는 쓰지 않는다.
6. **다 만들면 저장소에 넣는다 — 저장 경로 그대로** (저장소 `yeomin1024/yeomin1024-ytb` main · 대소문자·하이픈까지 같게). **JPEG `.jpg` · RGB · 700KB 이하** — 시트 1536×1024(자르지 않고 맞춰 넣고 남는 곳은 흰색) · 배경판 1536×864(가운데를 잘라 맞춤). 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지. 저장 코드는 앞 요청 파일 `images_chatgpt_states.md` 7번과 같다 (`save_jpg(src, dst, (1536, 1024), True)` · `save_jpg(src, dst, (1536, 864), False)`). GitHub 앱으로 장마다 커밋 — 메시지 `[crisis] hallasan-simjeongji-2026-11 <파일 이름> 이미지`. 다 올리면 경로와 커밋 링크를 목록으로.
   - **올리기가 실패한 장만** 그림을 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 실루엣 시트 화풍 (1번 — 맨 앞에 그대로 붙임)

```
SPRITE-SHEET STYLE: a clean production sprite sheet of human silhouettes for a documentary animation. Canvas exactly 1536x1024, landscape. Background: one flat pure white (#FFFFFF) everywhere — no floor, no ground line, no cast shadow, no gradient, no texture, no vignette, no frame, no grid lines, no borders. Every figure and every object is one solid flat pure black (#000000) shape with crisp clean edges — no inner lines, no gray shading, no highlights, no face, no visible clothing details inside the shape; only the outer outline shows the cap, clothing, backpack and posture. Realistic adult human proportions (about 7.5 heads tall) and natural, believable posture like a real person filmed from the side — not cartoon, not chibi, not a stick figure. The canvas is divided into an invisible grid of equal cells (the grid is NOT drawn). Each cell holds exactly one pose, centered horizontally in its cell, fully inside the cell with at least 40 pixels of white margin on every side, never touching or overlapping a neighboring cell. In every cell the same character is drawn at exactly the same size, and the soles of the feet rest on the same invisible horizontal line at 90% of the cell height (sitting poses rest on that same line). Absolutely no text, letters, numbers, labels, arrows, logos or watermarks.
```

## 인물 윤곽 (1번 — 실루엣 시트 화풍 다음에 그대로 붙임)

```
CHARACTER (outline only — identical in every cell):
SOLO HIKER — an adult hiker hiking alone: a plain baseball cap, a zip-up outdoor jacket, straight trousers, hiking shoes, a small daypack on the back, one trekking pole only where described.
```

## 다큐 재연 화풍 (2·3번 — 맨 앞에 그대로 붙임)

```
STYLE: a photorealistic documentary reenactment still, like a frame from a serious Korean TV news report or investigative documentary. Full-bleed landscape 1536x864, cinematic 16:9 composition, eye-level or slightly low camera, shallow depth of field, natural light only, calm and slightly dark muted colors with low saturation, soft contrast, a subtle film grain. Setting: Korea — Jeju island's mid-mountain forests and Korean mountain trails — but no identifiable real landmark. The mood is quiet, serious and respectful, never horror or action-movie drama. Absolutely no text, letters, numbers, logos, emblems or watermarks anywhere: trail signs, direction posts, vehicles, uniforms, phone screens, papers and medicine packets are blank or show only plain shapes. No blood, no injuries, no dead body, nothing gruesome.
```

## 1. SIL-12-SOLO — 혼자 산에 가는 등산객

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/SIL-12-SOLO.jpg`** — JPEG 700KB 이하 · 1536×1024

```
GRID: 3 columns x 2 rows, each cell 512x512. Cell order: top row left to right = 1, 2, 3; bottom row left to right = 4, 5, 6.
The SOLO HIKER, seen from the side, the same person and size in every cell:
1 — standing, facing RIGHT, looking down at a phone held in both hands (sending a message before starting).
2 — standing beside a plain trail marker post (the post and its blank plate are also solid black shapes) on the right, one hand raised toward the plate, looking at it.
3 — walking at an easy pace, facing RIGHT, mid-step, with one trekking pole.
4 — stopped, facing RIGHT, one hand pressed flat on the center of the chest, shoulders tense.
5 — sitting on a low rock (the rock is also a solid black shape), holding a phone to the ear with one hand, the other hand on the chest (calling for help).
6 — sitting on the same low rock, one arm raised high and waving toward the RIGHT (calling to someone passing by).
```

## 2. PLT-09-DROPPED — 숲길에 떨어진 모자와 배낭 (3장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/PLT-09-DROPPED.jpg`** — JPEG 700KB 이하 · 1536×864

```
A low, close camera at the edge of the same flat Jeju forest trail in the afternoon: on dry fallen leaves and moss beside the packed-earth path lie a plain dark baseball cap and a small black daypack, as if dropped there, in sharp focus in the lower middle of the picture. Behind them the path and the cedar trunks fade into soft blur, cool gray-green light. No person, no body, no hand, no blood — only the cap and the daypack. A quiet, heavy, respectful mood.
```

## 3. PLT-10-SIGNPOST — 길가의 위치 표지 기둥 (점검 장 · 혼자 장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/PLT-10-SIGNPOST.jpg`** — JPEG 700KB 이하 · 1536×864

```
Side view of the same flat Jeju forest trail at midday. The camera looks straight across the path, which runs horizontally across the picture with its near edge at about 82% of the image height. On the right third of the picture, at the edge of the path, stands one plain trail marker: a slim metal post with a small blank rectangular plate on top, at about chest height of an adult — the plate is completely blank, no letters, no numbers, no symbols. Cedar trunks, mossy black volcanic stones and ferns behind, soft light from behind the trees. No people, no animals.
```
