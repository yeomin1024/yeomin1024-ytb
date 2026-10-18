# gungmin-sigi-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py economic gungmin-sigi-2026-10` (2026-10-18 05:15). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **국민연금 5년 당기면 77세부터 손해, 미루면 84세부터 이득**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 93 / 자막 93, 길이 8:35 (SRT 추정) |
| 제목 3개 | ✅ |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 진행자 1–93 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/gungmin-sigi-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

(없음)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 본안(클릭률 최대): 밤 식탁에서 이마를 짚고 고개를 떨군 57세 남성 + '조기수령' 낱말

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 손해를 알고 좌절한 실사 얼굴과 손해를 만드는 '조기수령' 낱말이 가장 클릭을 부른다

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50대 국민연금 5년 당기면 | '50대' 흰색 · **'국민연금 5년 당기면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 77세부터 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 조금 크게 |

- 노랑은 중요한 것(국민연금을 5년 당기는 것), 빨강은 나쁜 상황(77세부터 손해와 손해를 만드는 조기수령)에 쓴다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 55% of the width): a Korean man aged 57 who looks youthful for his age, like his early 50s (short neat black hair with a little gray at the temples, dark gray knit cardigan over a white T-shirt), sitting at the dining table of his apartment living room at night, shown from the chest up and large in the frame. He has just realized how much pension money he will lose, and he is crushed: one hand pressed against his forehead, head bowed, eyes squeezed shut, brows knitted, shoulders slumped — clear frustration, regret and despair that read even at small thumbnail size. Keep most of his face visible (the hand must not cover his eyes and mouth completely). Realistic, not cartoonish, not exaggerated. On the table only an empty tea cup and one blank white sheet of paper with nothing printed on it. Fictional person, not resembling any real or famous person.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "조기수령" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the man.
- Background: an apartment living room at night with blurred city lights through the window, cool blue tones; warm pendant-lamp light only on the man's face.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "50대 국민연금 5년 당기면" — "50대" in white and "국민연금 5년 당기면" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 90% of the image width, but keep it at least 4% away from the right edge);
line 2 "77세부터 손해" — all in bright red #FF2A2A with a thick white outline, slightly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the man and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No money, no bills, no coins, no documents with writing, no phones, no calendars, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 실험안 ①: 같은 장면, 좌절한 남편 + 어깨에 손을 얹은 아내 (부부)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 대본 예시가 1969년생 동갑 부부라서, 부부가 함께 있으면 '우리 얘기'로 읽혀 더 누르는가

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50대 국민연금 5년 당기면 | '50대' 흰색 · **'국민연금 5년 당기면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 77세부터 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 조금 크게 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 60% of the width): a Korean married couple, both aged 57 but looking youthful, like their early 50s, at the dining table of their apartment living room at night, shown from the chest up and large in the frame. The husband (short neat black hair with a little gray at the temples, dark gray knit cardigan over a white T-shirt) has just realized how much pension money they will lose and is crushed: one hand pressed against his forehead, head bowed, eyes squeezed shut, brows knitted, shoulders slumped. The wife beside him on the right (shoulder-length dark hair, light beige blouse) rests one hand on his shoulder and covers her mouth with the other, looking down at him with worry and regret. Both faces stay visible. Clear frustration and despair that read even at small thumbnail size; realistic, not cartoonish. On the table only an empty tea cup and one blank white sheet of paper with nothing printed on it. Fictional people, not resembling any real or famous person.
- Left side (about 40% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "조기수령" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the couple.
- Background: an apartment living room at night with blurred city lights through the window, cool blue tones; warm pendant-lamp light only on their faces.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "50대 국민연금 5년 당기면" — "50대" in white and "국민연금 5년 당기면" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 90% of the image width, but keep it at least 4% away from the right edge);
line 2 "77세부터 손해" — all in bright red #FF2A2A with a thick white outline, slightly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the couple and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No money, no bills, no coins, no documents with writing, no phones, no calendars, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 실험안 ②: 사람 없이, 동전이 새는 모래시계 + '조기수령' 낱말

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 사람 없이, 시간(나이)과 새는 돈을 한 물건으로 보여 줘도 같은가 — 노후·연금 묶음 '사람 없음' 18% vs 7% (성공 쪽이 조금 많음), 국민연금 받는 시기 성공 썸네일 중 사람 없음 0

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50대 국민연금 5년 당기면 | '50대' 흰색 · **'국민연금 5년 당기면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 77세부터 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 조금 크게 |

<details><summary>[A] 완성형 프롬프트</summary>

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
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
65세부터 한 달 130만 원을 받을 국민연금을 60세로 당기면 91만 원, 70세로 미루면 약 177만 원입니다. 받은 돈 합계는 5년 당긴 쪽이 약 77세, 5년 미룬 쪽이 약 84세에 제때 받은 쪽과 뒤집힙니다.
국민연금을 언제 받을지, 일하면서 받을 때와 건보료 피부양자 기준까지 50대 부부 예시로 계산했습니다.

■ 이 영상에서 다루는 것
- 원칙 1: 1년 당기면 6% 덜, 1년 미루면 7.2% 더 — 정해진 비율은 평생
- 원칙 2: 일하는 동안은 당기지 않는다 — 당겨 받는 연금은 소득이 A값보다 많으면 못 받음
- 원칙 3: 연금은 건보료와 함께 본다 — 피부양자 소득 기준 연 2,000만 원, 부부 모두
- 할 일: 가입 기간(10년이 안 되면 추납) → 60~65세 5년 생활비 → 받는 나이
- 이미 연금을 받기 시작한 분이 할 일

■ 챕터
0:00 같은 국민연금, 다른 평생 합계
0:57 동갑 부부, 57세의 국민연금
1:57 원칙 1 1년 당기면 6% 덜, 1년 미루면 7.2% 더
3:08 원칙 2 일하는 동안은 당기지 않는다
4:03 원칙 3 연금은 건보료와 함께 본다
5:17 할 일 가입 기간 → 5년 생활비 → 받는 나이
6:43 세 가지 선택의 결과
7:23 이미 받기 시작했다면
7:56 정리

■ 예시에 대해
영상 속 부부(1969년생 57세, 남편 65세 예상 연금 월 130만 원)는 계산용 가상 사례입니다. 금액은 지금 돈 가치이고 세금·건보료 재산 몫은 넣지 않았습니다. 숫자는 2026년 10월 기준이며, 1965~1968년생은 나이가 모두 한 살씩 빠릅니다.
이 영상의 내레이션은 AI 음성으로 만들었습니다.

■ 근거
2026년 10월 18일 시행 중인 법령 원문으로 확인: 국민연금법(제61조 조기노령연금, 제62조 연기, 제63조 노령연금액, 제63조의2 소득활동 감액 — 2025.12.16 개정, 제66조 지급 정지, 제77조 반환일시금, 제92조 추후 납부)·같은 법 시행령(제45조), 국민건강보험법 시행령(제41조)·시행규칙(제44조·별표 1의2 피부양자 기준), 소득세법(제47조)

■ 알려 드립니다
이 영상은 정보 제공을 위한 것이며 연금 상담·법률 자문이나 투자 권유가 아닙니다.
A값·피부양자 기준·감액 기준은 바뀔 수 있으니, 신청하기 전에 국민연금공단(1355)·국민건강보험공단(1577-1000)에서 내 금액을 확인하세요.

#국민연금 #조기수령 #연기연금
```

**태그**: 국민연금, 국민연금 조기수령, 국민연금 연기연금, 국민연금 언제 받을까, 국민연금 수령 나이, 조기노령연금, 연기연금, 국민연금 추납, 국민연금 손익분기, 건보료 피부양자, 50대 노후, 노후 연금, 은퇴 준비, 재테크

**고정 댓글**

```
국민연금을 언제 받을지 정하기 전에 이 두 가지부터 확인해 보세요.
1. 부부의 가입 기간 (10년이 안 되면 추납으로 채울 수 있는지)
2. 60세부터 65세까지 5년 동안 일할 계획이 있는지 (일하면 당겨 받는 연금이 멈춤)
여러분은 당겨 받을 생각이신가요, 미룰 생각이신가요?
정보 제공용이며 연금 상담이 아닙니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**같은 국민연금, 다른 평생 합계** — 🎙 진행자

1. 국민연금 받을 날이 다가오는 50대라면, 이 숫자부터 보세요.
2. 65세부터 한 달 130만 원을 받을 남편이 있습니다.
3. 이 연금을 60세로 당기면 91만 원, 70세로 미루면 약 177만 원이 됩니다.
4. 그럼 어느 쪽이 이득일까요?
5. 답은 몇 살까지 받느냐에 달려 있습니다.
6. 5년 당긴 쪽은 약 77세, 미룬 쪽은 약 84세에 제때 받은 쪽과 합계가 뒤집힙니다.
7. 결론부터 말씀드리겠습니다.
8. 받는 나이는 77세와 84세를 기준으로 고르고, 일하는 동안은 당기지 않는다.
9. 그리고 미룰 땐 연금이 피부양자 기준 연 2,000만 원을 넘지 않게 한다.
10. 이 세 가지입니다.
11. 가입 기간이 10년이 안 되는 분과 이미 받는 분이 할 일도 끝까지 보여드릴게요.
12. 먼저 한 부부의 경우를 통해 알아보겠습니다.

**동갑 부부, 57세의 국민연금** — 🎙 진행자

13. 1969년생 동갑 부부가 있습니다.
14. 올해 57세이고, 남편은 60세에 정년퇴직할 예정이에요.
15. 1969년 이후 태어난 분은 국민연금을 65세부터 받습니다.
16. 60세로 당기거나, 70세까지 미룰 수도 있어요.
17. 1965년생부터 1968년생까지는 나이가 모두 한 살씩 빠릅니다.
18. 남편이 65세부터 받을 예상 연금은 한 달 130만 원입니다.
19. 국민연금법의 비율로 계산했고, 금액은 모두 지금 돈 가치입니다.
20. 아내는 결혼 전 7년만 국민연금을 냈어요.
21. 퇴직 뒤에는 부부가 함께, 회사에 다니는 아들의 건강보험 피부양자가 될 생각이에요.
22. 그런데 60세에 퇴직하면, 65세까지 5년 동안 월급도 연금도 없습니다.
23. 언제 받을지는 세 가지 원칙으로 정할 수 있습니다.
24. 하나씩 보겠습니다.

**원칙 하나, 1년 당기면 6% 덜, 1년 미루면 7.2% 더** — 🎙 진행자

25. 첫 번째 원칙은, 당기면 평생 덜 받고 미루면 평생 더 받는다는 것입니다.
26. 1년 당길 때마다 6%씩 깎여서, 5년이면 30%가 깎입니다.
27. 1년 미룰 때마다 7.2%씩 더해져서, 5년이면 36%가 늘어요.
28. 이렇게 정해진 비율은 평생 갑니다.
29. 남편이 60세로 당기면, 65세 전 5년 동안 5,460만 원을 먼저 받아요.
30. 대신 65세부터는 제때 받는 것보다 한 달에 39만 원씩 덜 받습니다.
31. 이 차이가 쌓여서, 76세 8개월이면 받은 돈 합계가 같아집니다.
32. 그 뒤로는 제때 받은 쪽이 더 많아요.
33. 70세로 미룬 쪽은 83세 11개월에 제때 받은 쪽을 따라잡습니다.
34. 이 나이는 연금 금액과 상관없이 같아요.
35. 다만 당기면 연금액이 5년 일찍 정해져, 그 뒤 오르는 가입자 평균 소득이 덜 반영돼요.
36. 그러면 75세 무렵에 뒤집힐 수도 있어요.
37. 한마디로, 당기는 건 77세, 미루는 건 84세를 넘게 살지로 고르는 겁니다.

**원칙 둘, 일하는 동안은 당기지 않는다** — 🎙 진행자

38. 두 번째 원칙은, 일해서 버는 동안에는 당겨 받지 않는다는 것입니다.
39. 당겨 받는 연금은 일해서 버는 소득이 가입자 평균 소득보다 많으면 받을 수 없어요.
40. 이 기준을 A값이라고 하는데, 올해는 한 달 약 319만 원입니다.
41. 월급에서 근로소득공제를 뺀 금액으로 봅니다.
42. 예를 들어 월급이 450만 원이면, 공제를 빼도 약 346만 원이라 기준을 넘어요.
43. 당겨 받던 중에 기준보다 많이 벌게 되면, 그동안 연금이 멈춰요.
44. 제때 받으며 일하면, 올해 6월부터 A값보다 200만 원 이상 더 벌 때만 연금이 깎여요.
45. 올해 기준으로 공제를 뺀 소득이 한 달 약 519만 원보다 적으면 그대로 받습니다.
46. 한마디로, 60세 뒤에도 일할 거라면 당기지 말고 제때 받습니다.

**원칙 셋, 연금은 건보료와 함께 본다** — 🎙 진행자

47. 세 번째 원칙은, 연금 금액은 건강보험료와 함께 봐야 한다는 것입니다.
48. 자녀의 건강보험 피부양자가 되려면, 소득이 1년에 2,000만 원 이하여야 합니다.
49. 국민연금은 이 피부양자 소득 기준에 전부 들어가요.
50. 그리고 부부는 한 사람만 넘어도 둘 다 피부양자에서 빠집니다.
51. 남편이 70세로 미루면 연금이 1년에 2,121만 6천 원이에요.
52. 피부양자 기준 2,000만 원을 넘어서, 부부가 함께 지역가입자로 건강보험료를 냅니다.
53. 소득 몫만 쳐도 한 달 약 7만 2천 원이고, 집이 있으면 재산 몫이 더해져요.
54. 연금에서 이 건보료를 빼고 보면, 미룬 쪽이 따라잡는 나이는 86세 무렵으로 늦어집니다.
55. 3년만 미루면 연금이 1년에 1,897만 원이라 기준 안이에요.
56. 다만 연금은 물가만큼 오르고 기준은 그대로라, 기준에 가까우면 몇 년 뒤 넘을 수 있어요.
57. 한마디로, 미룰 땐 연 2,000만 원을 넘기지 않을 만큼만 미룹니다.
58. 그럼 이 세 가지 원칙으로 부부가 할 일을 순서대로 정해 보겠습니다.

**할 일, 가입 기간 → 5년 생활비 → 받는 나이** — 🎙 진행자

59. 1단계, 부부의 가입 기간과 예상 연금부터 확인합니다.
60. 가입 기간이 10년이 안 되면 노령연금 없이, 60세에 낸 보험료와 이자만 돌려받아요.
61. 아내는 7년이라, 10년까지 36개월이 모자랍니다.
62. 이럴 때 내지 않은 기간의 보험료를 나중에 내는 게 추납이에요.
63. 아내처럼 소득 없이 쉬던 기간도, 스스로 가입하는 임의가입을 한 뒤 추납할 수 있습니다.
64. 월 소득 100만 원 기준으로 잡으면, 올해 36개월 추납액은 342만 원이에요.
65. 보험료율이 해마다 올라서, 내년에 내면 360만 원으로 18만 원 더 듭니다.
66. 2단계, 60세부터 65세까지 5년 동안의 생활비를 무엇으로 쓸지 정합니다.
67. 계속 일할 거라면 당기지 않고, 퇴직금이나 예금으로 버틸 수 있으면 제때 받아요.
68. 버틸 돈이 모자라도, 5년 대신 2년만 당기면 12%만 깎입니다.
69. 63세부터 한 달 114만 4천 원이고, 같아지는 나이도 79세 8개월로 늦어져요.
70. 3단계, 65세가 되기 전에 받는 나이를 정해 신청합니다.
71. 건강에 자신이 있으면 미루는 쪽을, 건강이 걱정되면 제때나 당기는 쪽을 봅니다.
72. 그럼 세 가지 선택의 결과는 얼마나 달라질까요?

**세 가지 선택의 결과** — 🎙 진행자

73. 75세까지 산다면, 받은 돈 합계는 당긴 쪽이 1억 6,380만 원으로 가장 많습니다.
74. 제때 받은 쪽은 1억 5,600만 원, 미룬 쪽은 1억 608만 원이에요.
75. 80세까지 살면 제때 받은 쪽이 앞서, 당긴 쪽보다 1,560만 원 많습니다.
76. 90세까지 살면 미룬 쪽이 가장 많아, 당긴 쪽보다 약 9,700만 원 더 받습니다.
77. 모두 지금 돈 가치이고, 세금과 건보료는 넣지 않은 숫자입니다.
78. 그런데 이미 연금을 받기 시작하신 분들도 계실 텐데요.
79. 그럼 어떻게 해야 할까요?

**이미 받기 시작했다면** — 🎙 진행자

80. 당겨 받는 중이라도, 원래 받을 나이 전이면 연금을 멈춰 달라고 신청할 수 있습니다.
81. 그러면 그 나이부터 다시 받을 때, 이미 받은 달 수만큼만 깎아요.
82. 한 달에 0.5%씩이라, 1년 받고 멈췄다면 6%만 깎입니다.
83. 다만 멈춘 동안은 연금이 없으니, 생활비가 있을 때만 하세요.
84. 제때 받기 시작했어도, 70세 전이면 남은 기간을 미룰 수 있습니다.
85. 자, 마지막으로 오늘 내용을 정리하겠습니다.

**정리, 바뀌어도 그대로인 것** — 🎙 진행자

86. A값과 피부양자 기준 2,000만 원, 일하면서 깎이는 기준은 바뀔 수 있습니다.
87. 그래도 이 세 가지는 그대로입니다.
88. 첫째, 1년 당기면 6% 덜, 1년 미루면 7.2% 더 받습니다.
89. 5년이면 77세와 84세가 기준이에요.
90. 둘째, 일해서 버는 동안에는 당기지 마세요.
91. 셋째, 미룰 때는 연 2,000만 원 피부양자 기준을 넘기지 마세요.
92. 오늘 국민연금공단에서 부부의 가입 기간과 예상 연금부터 확인해 보세요.
93. 시청해주셔서 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
