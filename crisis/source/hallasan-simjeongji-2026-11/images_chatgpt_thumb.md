# hallasan-simjeongji-2026-11 — 썸네일 그림 2장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v2.0 — 2026-11-27 — 영상과 같은 꼴로 다시 (사용자 지시 "이미지 좀 영상처럼 검은 실루엣, 이펙트로 표현해야지 실사 말고 다시 명령 알려줘") — 사람은 모두 **납작한 검은 실루엣**, 배경은 영상의 재연 숲길, 그 위에 **빨간 빛·심전도 같은 화면 효과**. 1 사고 장면 · 2 대비(먼저 내려가는 모습 | 사고 모습).
이전 v1.1 — 2026-11-27 — 실사 2장(TH-ACCIDENT · TH-CONTRAST) — 쓰지 않음.

문구는 그림에 넣지 않고 Claude 가 코드로 얹는다(`video/render/thumb.mjs` — 「등산 힘들어서 먼저 내려갔는데 / 심정지로 발견된 충격적인 사고」 + 꼬리표 「2023년 한라산 실제 사고」). 그래서 **그림 아래 40% 는 글자 자리**(어두운 흙길만).
**어떻게 쓰는가** — 1번 → `thumbnail_1`(본안) · 2번 → `thumbnail_2`(실험 1 — 대비). 오기 전에는 완성 영상 장면(자막 없이 다시 찍은 프레임)으로 대신한다.
※ 안전 교육 영상(연구·교육용). 실제 사고의 재연 — 피·상처·공포 연출 없음 · 얼굴 없음(사람은 모두 검은 실루엣) · 그림 속 글자·숫자·로고 없음.

| 번호 | 저장 경로 (`crisis/source/hallasan-simjeongji-2026-11/` 아래) | 크기 | 무엇 |
|---|---|---|---|
| 1 | `images/TH-SIL-ACCIDENT.jpg` | 1536×864 (16:9) | 사고 장면: 숲길에 쓰러진 실루엣 + 가슴을 누르는 구조대원 실루엣 둘 · 빨간 가장자리 빛 · 가슴 위 빨간 빛 · 평평해진 심전도 빛줄 |
| 2 | `images/TH-SIL-CONTRAST.jpg` | 1536×864 (16:9) | 대비 두 칸: 왼쪽 = 가슴에 손을 얹고 혼자 내려가는 실루엣(멀리 반대로 가는 일행 실루엣) · 오른쪽 = 같은 숲길, 빨갛게 물든 사고 장면 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트(실사 그림 요청 포함)가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성:' 줄을 그대로 옮겨 적는다.
1. 아래 그림 **2장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 앞에 '실루엣 재연 화풍' 블록을 붙인다.
3. **사람이 실사로 그려지거나(얼굴·옷 주름·피부가 보이면), 피·상처가 보이거나, 그림 속에 글자·숫자가 생기면 다시 만든다.** 사람은 반드시 안쪽 무늬가 없는 완전한 검정 실루엣.
4. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다. 그림 안에는 쓰지 않는다.
5. **다 만들면 저장소에 넣는다 — 저장 경로 그대로** (저장소 `yeomin1024/yeomin1024-ytb` main · 대소문자·하이픈까지 같게). **JPEG `.jpg` · RGB · 700KB 이하 · 1536×864**(가운데를 잘라 맞춤). 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지. GitHub 앱으로 장마다 커밋 — 메시지 `[crisis] hallasan-simjeongji-2026-11 <파일 이름> 이미지`. 다 올리면 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** 그림을 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 실루엣 재연 화풍 (맨 앞에 그대로 붙임)

```
STYLE: a dramatic documentary-animation thumbnail frame in the exact look of a Korean safety-education video: a realistic, slightly dark photographic background of a flat Jeju mid-mountain cedar forest trail (packed-earth path, tall straight cedar trunks, mossy black volcanic stones, ferns, faint mist), and ALL people drawn as completely flat, solid pure black silhouettes with crisp clean edges — no faces, no skin, no clothing folds, no inner lines or highlights inside the shapes; only the outer outline shows caps, helmets, jackets, small daypacks and posture, with realistic adult proportions. Over the scene, glowing motion-graphic effects like those in the video: a soft red pulsing vignette darkening the edges of the frame, warm red glow spots, and thin neon light lines. Full-bleed landscape 1536x864, cinematic 16:9. Serious, tense and respectful mood — not horror, not cartoon, not cute. Absolutely no text, letters, numbers, logos, symbols, arrows or watermarks anywhere. No blood, no wounds, nothing gruesome.
```

## 1. TH-SIL-ACCIDENT — 사고 장면 (실루엣 + 효과)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/TH-SIL-ACCIDENT.jpg`** — JPEG 700KB 이하 · 1536×864

```
On the forest trail, slightly right of center, one hiker silhouette lies flat on his back across the path, collapsed, his dropped cap and small daypack silhouettes on the ground beside him. Two rescue-worker silhouettes with helmet outlines kneel beside him: the nearer one, seen from the side, gives chest compressions with both arms straight and hands stacked on the center of his chest; the other kneels on the far side with one hand raised to a small radio near the helmet. A small bright red glow pulses on the lying hiker's chest under the stacked hands. Effects: a strong red pulsing vignette closing in from all four edges; the background photo is darkened and tinted cold gray-red; faint alternating red and blue emergency light washing in from the right side through the trees; across the upper right sky between the trunks, a thin glowing red heartbeat line that runs with two sharp peaks and then goes completely flat. Composition: all silhouettes sit between about 18% and 60% of the image height; the bottom 40% of the image is the dark, plain, slightly blurred dirt path with nothing important on it (large text will be placed there later). No faces, no blood, no text.
```

## 2. TH-SIL-CONTRAST — 먼저 내려가는 모습 | 사고 모습 (대비)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/TH-SIL-CONTRAST.jpg`** — JPEG 700KB 이하 · 1536×864

```
One single 16:9 image made of two side-by-side panels of equal width, separated by a thin straight glowing white vertical line in the exact center; both panels show the same flat cedar forest trail so the two moments clearly belong together. LEFT PANEL — "before": daylight, natural slightly muted green colors; a lone hiker silhouette with a cap outline and small daypack walks down the trail toward the lower left, head lowered, one hand pressed on his chest, where a small red glow shines; far behind him, small, three companion silhouettes walk the other way up the trail; a thin red dashed line stretches on the ground between him and them. RIGHT PANEL — "after": the same trail a little further on, darkened and soaked in red light with a strong red vignette; the same hiker silhouette lies collapsed on his back across the path while two rescue-worker silhouettes with helmet outlines kneel beside him, the nearer one giving chest compressions; a thin glowing red heartbeat line runs across the upper part of the right panel and goes completely flat. In both panels all silhouettes sit between about 15% and 60% of the image height, and the bottom 40% of the whole image is the dark, plain, slightly blurred dirt path with nothing important on it (large text will be placed there later). All people are completely flat pure black silhouettes — no faces, no inner detail. No blood, no text, no labels, no arrows.
```
