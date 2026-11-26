# jakku-juneun-2026-11-25 — 새 썸네일 그림 1장 (ChatGPT용)

> 2026-11-26 · 영상 제작 공통 규칙 `guides/production_rules.md` 2번 (사용자 지시 "썸네일 이미지 - 영상 내용 중 가장 자극적인 부분을 찾아 사용하고 반전을 숨겨 호기심을 유발하도록 표현").
> 고른 장면 = 대본에서 가장 자극적인 부분: **받는 사람 품에 쌓여 가는 반찬통 + 또 하나를 내미는 이웃 + 문 안쪽 쓰레기통** (대본 이유 1 — 받은 집에서 버리게 될 수 있음 · 받는 쪽 부담). 숨긴 반전 = 왜 자꾸 주는지(이유 3가지)·결국 버리는지 — 그림에는 답 없음.
> 사람·그림체는 이 편 기준 그림 그대로: `puppet/motion/R-REF.png` · `puppet/motion/G-REF.png` · 지금 썸네일 `images/TH-CHAR.jpg` (같은 복도·같은 사람). 문구·말풍선은 Claude 가 코드로 얹음 — 그림에 글자 없음.

| 번호 | 저장 경로 | 무엇 |
|---|---|---|
| 1 | `psychology/source/jakku-juneun-2026-11-25/images/TH-CHAR2.jpg` | 썸네일 그림: 복도 — 반찬통 탑을 턱까지 안은 R · 하나 더 내미는 G · R 의 문 안쪽 쓰레기통 (화면 끝까지) |

## ChatGPT에게 — 이 파일을 읽으면 할 일

1. 저장소의 기준 그림 세 장을 먼저 연다: `psychology/source/jakku-juneun-2026-11-25/puppet/motion/R-REF.png` · `…/puppet/motion/G-REF.png` · `…/images/TH-CHAR.jpg` — **이 세 장과 같은 그림체·같은 사람**으로 그린다.
2. 아래 프롬프트(공통 화풍 + 인물 + 썸네일 + 장면)를 그대로 써서 1장을 만든다. 가로 1536×864 · 글자·숫자·말풍선 없음.
3. **JPEG `.jpg` 700KB 이하**로 저장 경로 그대로 GitHub 에 올린다. 커밋 메시지: `[psychology] jakku-juneun-2026-11-25 TH-CHAR2.jpg 이미지`. 올리기가 실패하면 그림을 보여 주고 "올리지 못한 그림입니다"라고만 쓴다.

## 1. TH-CHAR2

**저장 경로: `psychology/source/jakku-juneun-2026-11-25/images/TH-CHAR2.jpg`** — JPEG 700KB 이하 · 가로 1536×864 · 글자 없음

```
STYLE: a simple, warm Korean daily-life webtoon (일상툰) look for a YouTube animation. Rounded simple shapes, thin clean dark-brown outlines, soft flat pastel colors with at most one light shading tone, very little detail. People are about 3 heads tall — a little cute but clearly adults (children smaller). Simple faces: small oval eyes, short eyebrows that carry the emotion, a small mouth; light pink cheeks only when embarrassed or crying. Simple comic marks are allowed only as shapes (one sweat drop, small sparkle lines, a little gloomy cloud scribble). Expressions must read instantly on a small phone screen. From picture 2 on, match EXACTLY the drawing style, line weight, colors and proportions of picture 1. Warm, gentle, emotionally honest mood — no horror, no violence, nobody is a villain. 2D drawing only — not 3D, not a photo, not glossy anime. Absolutely no text, letters, numbers, logos or watermarks anywhere — screens, phones, papers, books, boards, signs, clocks and packages are blank or show only simple shapes. Do not imitate any specific existing webtoon or artist.

CHARACTERS — draw each person exactly like their reference or pose sheet (pictures 1, 2, 3). The same face, hair, clothes, colors and proportions in every picture:
R — the receiver, main person: a 34-year-old Korean man who lives alone, office worker. Neat short black hair with a soft side part, thin black rectangular glasses, a slim face. At home: a mustard-yellow knit cardigan over a white T-shirt, beige cotton pants, gray house slippers. Polite, a little awkward, kind; he never looks disgusted.
G — the giver, next-door neighbor: a 63-year-old Korean woman. Short curly permed hair, dark brown with some gray, a round warm face with smile lines, a coral-pink quilted vest over a white-and-navy striped long-sleeve shirt, dark green pants, white sneakers. Energetic, generous and warm — a kind neighbor, never a villain or a nag.
H — R's team leader at work: a 52-year-old Korean man, short black hair, thick eyebrows, a cheerful round face, a navy knit vest over a light-blue shirt, gray slacks. Cheerful and generous.

THUMBNAIL PICTURE for a video cover: full-bleed landscape 1536x864, ONE complete scene that fills the whole frame edge to edge — no flat color band, no border, no empty strip at the top or bottom. The people and their faces sit in the upper 60% of the picture. The lower 35% simply continues the same scene (floor, doormat, shoes, bags) with simple shapes and slightly darker, calm tones so that large white title text added later by code stays readable over it — keep faces and hands out of that lower part. Leave empty space beside each person's head (not over any face, hand or body) where speech bubbles will be added later. Strong, readable emotion for a small phone screen. Absolutely no text, no letters, no numbers, no symbols, no speech bubbles drawn.

One scene in the apartment corridor in daylight, the same corridor and the same two people as in the reference pictures. LEFT side (from about 8% to 45% of the width): G, three-quarter view facing right, cheerfully holding out ONE MORE plastic food container wrapped in a small cloth bundle, a big warm, kind smile. RIGHT side (from about 52% to 92% of the width): R standing at his open front door, three-quarter view facing left, both arms hugging a tall, wobbling stack of plastic food containers and two bulging plastic bags that reaches up to his chin — clearly more than he can hold. R has an awkward polite smile, worried eyebrows and one sweat drop — kind and embarrassed, never disgusted or angry. Just inside R's open door behind him, a small kitchen trash bin with its lid half open is visible (simple shape, no garbage drawn). Both faces are clearly visible in the upper 60% of the picture. Leave empty wall space to the right of G's head (above the gap between the two people) and to the right of R's head (on the door frame) for speech bubbles — not over any face, hand or the container stack. The floor, the doormat and a few more bags at their feet continue to the bottom edge.
```
