# hallasan-simjeongji-2026-11 — 썸네일 그림 2장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.1 — 2026-11-27 — 2장으로 (사용자 지시 "이미지를 기존 만들고 있는거 1개 먼저 내려가는 모습, 사고 모습 대비하는거랑 2개 만들어봐") — 1 사고 장면 · 2 대비(먼저 내려가는 모습 | 사고 모습).
이전 v1.0 — 2026-11-27 — 사용자 지시 "등산 힘들어서 먼저 내려갔는데... / 고작 1시간만에 싸늘한 시체로 발견됐다 이렇게 문구, 제목 변경하고 이미지도 사고 난 이미지로 해" — 썸네일 그림을 '사고 장면'으로 (사용자가 '새 그림 요청'을 고름). 문구는 그림에 넣지 않고 Claude 가 코드로 얹음(`video/render/thumb.mjs` — 「등산 힘들어서 먼저 내려갔는데... / 고작 1시간 만에 심정지로 발견됐다」).

**어떻게 쓰는가** — 그림이 오면 Claude 가 썸네일 설정의 그림을 바꿔 다시 만든다: 1번 → `thumbnail_1`(본안) · 2번 → `thumbnail_2`(실험 1 — 대비). 오기 전에는 1번 = `images/DOC-10-STRETCHER.jpg`(담요 덮인 들것) · 2번 = `DOC-05-TURN`(혼자 내려감) | `DOC-10` 을 코드로 반반 붙인 것.
※ 안전 교육 영상(연구·교육용). 실제 사고의 재연 — 피·상처·공포 연출 없음 · 쓰러진 사람과 구조대원의 얼굴이 보이지 않음 · 그림 속 글자·숫자·로고 없음.

| 번호 | 저장 경로 (`crisis/source/hallasan-simjeongji-2026-11/` 아래) | 크기 | 무엇 |
|---|---|---|---|
| 1 | `images/TH-ACCIDENT.jpg` | 1536×864 (16:9) | 숲길에서 쓰러진 등산객에게 구조대원이 가슴 압박을 하는 사고 장면 — 위쪽 55% 에 사람, 아래 40% 는 어두운 흙길(글자 자리) |
| 2 | `images/TH-CONTRAST.jpg` | 1536×864 (16:9) | 대비 두 칸: 왼쪽 = 혼자 먼저 산길을 내려가는 등산객(멀리 반대로 가는 일행) · 오른쪽 = 같은 숲길의 사고 장면(구조대원 가슴 압박) — 가운데 가는 흰 세로줄 · 아래 40% 는 글자 자리 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성:' 줄을 그대로 옮겨 적는다.
1. 아래 그림 **2장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 앞에 '다큐 재연 화풍' 블록을 붙인다.
3. 얼굴이 보이거나, 피·상처가 보이거나, 그림 속에 글자가 생기면 다시 만든다.
4. 그림 바로 위에 저장 경로를 한 줄 적는다. 그림 안에는 쓰지 않는다.
5. **다 만들면 저장소에 넣는다 — 저장 경로 그대로** (저장소 `yeomin1024/yeomin1024-ytb` main · 대소문자·하이픈까지 같게). **JPEG `.jpg` · RGB · 700KB 이하 · 1536×864**(가운데를 잘라 맞춤). 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지. GitHub 앱으로 장마다 커밋 — 메시지 `[crisis] hallasan-simjeongji-2026-11 <파일 이름> 이미지`. 다 올리면 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패하면** 그림을 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 다큐 재연 화풍 (맨 앞에 그대로 붙임)

```
STYLE: a photorealistic documentary reenactment still, like a frame from a serious Korean TV news report or investigative documentary. Full-bleed landscape 1536x864, cinematic 16:9 composition, eye-level camera, shallow depth of field, natural light only, calm and slightly dark muted colors with low saturation, soft contrast, a subtle film grain. Setting: Korea — Jeju island's mid-mountain cedar forest — but no identifiable real landmark. The mood is quiet, serious and respectful, never horror or action-movie drama. Absolutely no text, letters, numbers, logos, emblems or watermarks anywhere: uniforms, helmets, bags and equipment are plain. No blood, no injuries, nothing gruesome.
```

## 1. TH-ACCIDENT — 숲길의 사고 장면

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/TH-ACCIDENT.jpg`** — JPEG 700KB 이하 · 1536×864

```
On a flat packed-earth forest trail among tall cedar trunks, mossy black volcanic stones and ferns, an adult hiker lies on his back across the path, collapsed. Two rescue workers in dark navy uniforms with reflective stripes and plain helmets kneel beside him: the nearer rescuer, seen from behind and slightly from the side, gives chest compressions with both arms straight and hands stacked on the center of the hiker's chest; the second rescuer kneels at the far side holding a small radio, head lowered. The hiker's head and face are completely hidden behind the nearer rescuer's back and shoulder — only his legs in dark trousers and his hiking shoes are visible on the ground. A plain dark baseball cap and a small black daypack lie on the leaves at the edge of the path. Late afternoon cool gray-green light from behind the trees, a faint mist between the trunks. Composition: all the people are in the upper-middle and right part of the picture, roughly between 15% and 60% of the image height; the bottom 40% of the image is the dark, plain, slightly out-of-focus dirt path with nothing important on it (it will be covered by large text later). No faces visible at all — every face is turned away, in shadow or hidden. No blood, no wounds, no medical gore, no crowd, no text.
```

## 2. TH-CONTRAST — 먼저 내려가는 모습 | 사고 모습 (대비)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/TH-CONTRAST.jpg`** — JPEG 700KB 이하 · 1536×864

```
One single 16:9 image made of two side-by-side panels of equal width, separated by a thin straight vertical white line in the exact center. Both panels show the same flat Jeju cedar forest trail with mossy black volcanic stones and ferns, so the two moments clearly belong together. LEFT PANEL — "before": a lone adult hiker in a plain dark cap, a dark zip-up jacket and a small daypack walks down the trail alone toward the lower left, seen from the side and slightly behind, head lowered, one hand pressed on his chest; far behind him, small and out of focus, three companions walk the other way up the trail. Soft daylight, slightly warmer green tones. RIGHT PANEL — "after": the same trail a little further on, colder and darker gray-green light with a faint mist; two rescue workers in dark navy uniforms with reflective stripes and plain helmets kneel on the path, the nearer one giving chest compressions to a hiker lying on his back; the lying hiker's head and face are completely hidden behind the rescuer's back — only his legs and hiking shoes are visible; a dropped plain dark cap and small daypack lie at the edge of the path. In both panels, all people are between about 15% and 60% of the image height, and the bottom 40% of the whole image is the dark, plain, slightly out-of-focus dirt path with nothing important on it (it will be covered by large text later). No faces visible anywhere — every face is turned away, in shadow or hidden. No blood, no wounds, no gore, no text, no labels, no arrows.
```
