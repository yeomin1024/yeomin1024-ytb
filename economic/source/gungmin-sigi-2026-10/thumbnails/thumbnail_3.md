# gungmin-sigi-2026-10 썸네일 3 — 실험안 ②: 사람 없이, 동전이 새는 모래시계 + '조기수령' 낱말

버전: v1.0 — 2026-10-18 — 대본 gungmin-sigi-2026-10.txt v1.0 기준. `guides/thumbnail_guide.md` v3.14. 근거: `README.md`.

| 항목 | 값 |
|---|---|
| 역할 | 실험안 ② — 본안(`thumbnail_1.md`)과 **사람 있음/없음만** 다름 (낱말 꼬리표·문구·밤 식탁·색은 같음) |
| 시험하는 가설 | 사람 없이, 시간(나이)과 새는 돈을 한 물건으로 보여 줘도 같은가 — 노후·연금 묶음 '사람 없음' 18% vs 7% (성공 쪽이 조금 많음), 국민연금 받는 시기 성공 썸네일 중 사람 없음 0 |
| 짝 제목 | titles.md R1 「국민연금 5년 당기면 77세부터 손해, 미루면 84세부터 이득」 |
| 문구 | 본안과 같음 (`README.md` 2번) |
| 근거 (`README.md` 3번) | 3-1 사람 없음 18% vs 7% · 빨강 글자 48% vs 32% · 손해 낱말 43% vs 18% |
| 숫자 근거 | 본안과 같음 (문장 6·29~32) |
| 은유 | 모래시계 = 시간이 갈수록(오래 살수록) 당긴 연금의 손해가 쌓임 (문장 30~32 '이 차이가 쌓여서'). 영상 내용(당기기·미루기 비율)을 물건으로 그리지는 않음 (5번 3) |

## 화면 구성
- **위쪽 약 62%**:
  - 오른쪽 55%: 어두운 나무 식탁 위의 큰 유리 모래시계 하나 (가운데보다 오른쪽, 위 62% 안에 다 들어오게). 모래 대신 **글자·무늬 없는 작은 금빛 동전**이 위 칸에서 가는 줄기로 아래 칸으로 떨어지는데, 아래 칸 밑의 유리에 금이 가서 동전 몇 개가 식탁 위로 새어 나와 흩어져 있다.
  - 왼쪽 45%: 낱말 꼬리표 1개 '조기수령' — 빨강 둥근 상자에 큰 흰 평면 글자, 모래시계에 기대어 서 있고, 굵은 빨강 화살표 2개가 새어 나온 동전 쪽 아래로.
  - 배경: 본안과 같은 밤 거실(흐린 창밖 불빛, 차가운 푸른빛), 모래시계에만 따뜻한 조명.
- **아래쪽 약 35%**: 본안과 같은 하단 2줄. 오른쪽 아래 구석 비움.

## 문구 (그대로 사용)
| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50대 국민연금 5년 당기면 | '50대' 흰색 · **'국민연금 5년 당기면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 77세부터 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 조금 크게 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size. No people.
Upper 62% of the frame:
- Right side (about 55% of the width): one large glass hourglass standing on a dark wooden dining table at night, fully inside the upper 62% of the frame. Instead of sand, small plain gold coins with no numbers, letters, portraits or patterns fall in a thin stream from the upper bulb into the lower bulb; the glass at the bottom of the lower bulb is cracked, and a few plain gold coins have leaked out and lie scattered on the table. Warm light only on the hourglass.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "조기수령" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes), standing upright and leaning against the hourglass. Two thick bright red arrows point from the tag down toward the leaking coins.
- Background: an apartment living room at night with blurred city lights through the window, cool blue tones.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "50대 국민연금 5년 당기면" — "50대" in white and "국민연금 5년 당기면" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 90% of the image width, but keep it at least 4% away from the right edge);
line 2 "77세부터 손해" — all in bright red #FF2A2A with a thick white outline, slightly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the hourglass and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and objects inside the central 16:9 area, at least 8% away from the top and bottom edges.
No banknotes, no documents, no phones, no calendars, no clocks with numbers, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집 프로그램으로)
```
YouTube thumbnail background, 16:9 landscape (1280x720), photorealistic, high contrast. No people.
Upper 62%: on the right, one large glass hourglass on a dark wooden dining table at night; plain gold coins (no numbers, letters or patterns) fall from the upper bulb into the lower bulb, the lower bulb is cracked and a few coins have leaked out onto the table; warm light on the hourglass. On the left, one empty solid bright red rounded box leaning against the hourglass, with two thick red arrows pointing down toward the leaking coins. Background: apartment at night, blurred city lights, cool blue tones.
Lower third: a dark band fading upward from the bottom edge, left empty for a two-line headline.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
- 글자 얹기: 본안(`thumbnail_1.md`)과 같음.

## 검수
- [ ] 글자가 한 글자도 틀리지 않았는가: 조기수령 · 50대 국민연금 5년 당기면 · 77세부터 손해
- [ ] '국민연금 5년 당기면'만 노랑, '77세부터 손해'만 빨강인가
- [ ] 사람이 없는가 · 동전에 숫자·글자·초상이 없는가 · 모래시계가 위 62% 안에 다 들어오는가
- [ ] 가로 320px로 줄여도 2줄과 '조기수령'이 읽히는가 · 모래시계와 새는 동전이 보이는가
- [ ] 글자가 가운데 16:9 안 · 오른쪽 아래 구석이 비어 있는가

## 이미지 검수 (Claude — 지시사항 10번)

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
