# gungmin-sigi-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py economic gungmin-sigi-2026-10` (2026-10-19 13:20). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **은퇴 후 국민연금 신청 한 번에 평생 손해봤어요. 꼭 보세요**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 102 / 자막 102, 길이 8:21 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 진행자 1–102 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/gungmin-sigi-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1 = R1 (사용자 선택 — 업로드 시트 1번)** 은퇴 후 국민연금 신청 한 번에 평생 손해봤어요. 꼭 보세요 `33자` — 짝 썸네일: thumbnail_1
- [ ] **T2 = R2** 국민연금 신청 한 번에 평생 손해봤어요. 은퇴 전 꼭 아세요 `33자`
- [ ] **T3 = R3** 은퇴 후 국민연금 6,480만 원 날린 줄 알았는데 진짜는 따로 `35자`

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 본안(클릭률 최대): 밤 거실 소파에서 빈 통장을 들고 이마를 짚은 60세 남성 + '30% 깎임' 낱말

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 손해를 알고 좌절한 실사 얼굴 + 방법을 말하지 않는 손해 낱말 '30% 깎임'이 가장 클릭을 부른다 (제목처럼 '무엇을 신청했나'는 영상이 밝힘)

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 30% 깎임 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 은퇴 후 국민연금 신청 한 번에 | '은퇴 후' 흰색 · **'국민연금 신청 한 번에' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 평생 손해봤어요 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 크게 |

- 노랑은 중요한 것(국민연금 신청 한 번), 빨강은 나쁜 상황(평생 손해 · 30% 깎임)에 쓴다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 55% of the width): a Korean man aged 60 who looks youthful for his age, like his mid-50s (short neat black hair with gray at the temples, navy cotton shirt with the sleeves rolled up), sitting on the edge of a sofa in his living room at night, shown from the chest up and large in the frame. In his lower hand he holds an open blank bank passbook with nothing printed on it. He has just found out that his early pension cut lasts for the rest of his life, and he is crushed: one hand pressed against his forehead, head bowed, eyes squeezed shut, brows knitted, shoulders slumped — clear frustration, regret and despair that read even at small thumbnail size. Keep most of his face visible (the hand must not cover his eyes and mouth completely). Realistic, not cartoonish, not exaggerated. Fictional person, not resembling any real or famous person.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "30% 깎임" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the man.
- Background: a modest apartment living room at night, a sofa and a floor lamp, blurred window lights, cool blue tones; warm lamp light only on the man's face.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "은퇴 후 국민연금 신청 한 번에" — "은퇴 후" in white and "국민연금 신청 한 번에" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 88% of the image width, but keep it at least 4% away from the right edge);
line 2 "평생 손해봤어요" — all in bright red #FF2A2A with a thick white outline, clearly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the man and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No money, no bills, no coins, no documents with writing, no phones, no calendars, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 실험안 ①: 본안과 같은 장면, 낱말만 '조기수령'

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 그림 낱말을 방법 낱말 '조기수령'으로 바꾸면(무엇을 신청했는지 썸네일이 말하면) 검색 낱말과 맞아 클릭이 느는가, 호기심이 줄어 덜 누르는가 (본안과 낱말 한 가지만 다름)

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 은퇴 후 국민연금 신청 한 번에 | '은퇴 후' 흰색 · **'국민연금 신청 한 번에' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 평생 손해봤어요 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 크게 |

- 노랑은 중요한 것(국민연금 신청 한 번), 빨강은 나쁜 상황(평생 손해 · 조기수령)에 쓴다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 55% of the width): a Korean man aged 60 who looks youthful for his age, like his mid-50s (short neat black hair with gray at the temples, navy cotton shirt with the sleeves rolled up), sitting on the edge of a sofa in his living room at night, shown from the chest up and large in the frame. In his lower hand he holds an open blank bank passbook with nothing printed on it. He has just found out that his early pension cut lasts for the rest of his life, and he is crushed: one hand pressed against his forehead, head bowed, eyes squeezed shut, brows knitted, shoulders slumped — clear frustration, regret and despair that read even at small thumbnail size. Keep most of his face visible (the hand must not cover his eyes and mouth completely). Realistic, not cartoonish, not exaggerated. Fictional person, not resembling any real or famous person.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "조기수령" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the man.
- Background: a modest apartment living room at night, a sofa and a floor lamp, blurred window lights, cool blue tones; warm lamp light only on the man's face.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "은퇴 후 국민연금 신청 한 번에" — "은퇴 후" in white and "국민연금 신청 한 번에" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 88% of the image width, but keep it at least 4% away from the right edge);
line 2 "평생 손해봤어요" — all in bright red #FF2A2A with a thick white outline, clearly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the man and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No money, no bills, no coins, no documents with writing, no phones, no calendars, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 실험안 ②: 사람 없이, 오른쪽 3분의 1이 잘려 나간 빈 통장 + '30% 깎임' 낱말

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 사람 얼굴 없이 '평생 깎인 통장' 한 장면만으로도 클릭을 부르는가 (본안과 사람 유무 한 가지만 다름 — 국민연금 성공 썸네일에 사람 없는 것은 없었음)

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 30% 깎임 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 은퇴 후 국민연금 신청 한 번에 | '은퇴 후' 흰색 · **'국민연금 신청 한 번에' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 평생 손해봤어요 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 크게 |

- 노랑은 중요한 것(국민연금 신청 한 번), 빨강은 나쁜 상황(평생 손해 · 30% 깎임)에 쓴다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Center-right (about 55% of the width): close-up still life on a dark wooden coffee table at night — an open blank bank passbook with nothing printed on it, its right third cut away with a ragged edge, the cut piece lying a little apart, a pair of scissors beside it and a single desk lamp casting a hard warm light on it. No hands, no people.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "30% 깎임" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag toward the cut-away piece of the passbook.
- Background: a dark living room at night, blurred and out of focus, cool blue tones.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "은퇴 후 국민연금 신청 한 번에" — "은퇴 후" in white and "국민연금 신청 한 번에" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 88% of the image width, but keep it at least 4% away from the right edge);
line 2 "평생 손해봤어요" — all in bright red #FF2A2A with a thick white outline, clearly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the passbook and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No money, no bills, no coins, no documents with writing, no phones, no calendars, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
5년 당겨 받은 국민연금, 월 90만 원이 63만 원이 됐습니다. 김 씨는 평생 6,480만 원을 잃는다고 계산했는데, 정말 그럴까요?
받기 시작하고 16년 8개월이라는 기준, 연금이 늘리는 건보료, 이미 신청했을 때 멈추는 방법까지 김 씨의 이야기로 계산했습니다.

■ 이 영상에서 다루는 것
- 1년 당길 때마다 6%씩 평생 덜 받는다 — 그래도 손해가 되는 건 받기 시작하고 16년 8개월 뒤부터
- 연금이 늘리는 지역 건보료는 소득 몫뿐 (국민연금은 절반만 소득) — 김 씨는 한 달에 2,810원
- 얼마나 당길지는 버틸 돈이 정한다 — 3년을 버틴 동창은 85세까지 2,203만 원 더 받음
- 이미 신청했다면: 원래 받을 나이 전에 지급 정지 → 받은 달 수 × 0.5%만 깎임

■ 챕터
0:00 신청서 한 장의 값
0:24 원래대로 돌아올 줄 알았다
2:06 아들이 찾은 구멍
3:40 건보료 폭탄의 정체
5:14 동창 박 씨의 통장
6:37 공단 창구에서 들은 말
7:51 정리

■ 예시에 대해
영상 속 김 씨(1966년생, 64세 예상 연금 월 90만 원)와 친구·아들·동창 박 씨·공단 상담 직원은 신문 기사 사례를 바탕으로 지금 법에 맞게 각색한 가상 인물입니다. 금액은 지금 돈 가치이고, 연금소득세와 건보료 재산 몫은 넣지 않았습니다. 숫자는 2026년 10월 기준이며, 받는 나이는 태어난 해에 따라 다릅니다(1965~1968년생 64세, 1969년생부터 65세).
이 영상의 내레이션은 AI 음성으로 만들었습니다.

■ 근거
2026년 10월 19일 시행 중인 법령 원문으로 확인: 국민연금법(제61조 조기노령연금, 제63조 노령연금액, 제66조 조기노령연금 지급 정지, 부칙 법률 제8541호 제8조 지급연령), 국민건강보험법(제69조 지역가입자 보험료), 국민건강보험법 시행령(제41조 소득, 제44조 보험료율), 국민건강보험법 시행규칙(제44조 소득월액, 별표 1의2 피부양자), 노인장기요양보험법 시행령(제4조)

■ 알려 드립니다
이 영상은 정보 제공을 위한 것이며 연금 상담·법률 자문이나 투자 권유가 아닙니다.
건보료율·최저 금액·피부양자 기준은 바뀔 수 있으니, 신청하기 전에 국민연금공단(1355)·국민건강보험공단(1577-1000)에서 내 금액을 확인하세요.

#국민연금 #조기수령 #지급정지
```

**태그**: 국민연금, 국민연금 조기수령, 조기노령연금, 국민연금 손익분기, 국민연금 지급정지, 국민연금 수령 나이, 국민연금 당겨 받기, 국민연금 건보료, 지역가입자 건보료, 은퇴 후 국민연금, 퇴직 후 연금, 노후 연금, 60대 노후

**고정 댓글**

```
국민연금을 당겨 받기 전이라면, 또는 이미 받고 있다면 이 두 가지부터 확인해 보세요.
1. 원래 받을 나이까지 버틸 돈이 몇 년인지 (그만큼 덜 당기면 평생 덜 깎임)
2. 이미 받고 있다면, 원래 받을 나이 전에는 지급 정지로 멈출 수 있다는 것
여러분은 국민연금을 언제 받으실 생각인가요?
정보 제공용이며 연금 상담이 아닙니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**신청서 한 장의 값** — 🎙 진행자

1. 국민연금 신청 한 번에, 평생 손해봤어요.
2. 60세 김 씨가 1년 전에 낸 신청서를 두고 한 말입니다.
3. 김 씨는 이 한 장 때문에, 6,480만 원을 잃었다고 믿었습니다.
4. 그런데 하나씩 따져 보던 김 씨는, 전혀 다른 범인을 찾아냅니다.
5. 김 씨가 알아낸 순서 그대로, 끝까지 따라가 보겠습니다.

**원래대로 돌아올 줄 알았다** — 🎙 진행자

6. 김 씨는 1966년생입니다.
7. 1966년생은 국민연금을 64세부터 받습니다.
8. 태어난 해에 따라 다르고, 1969년생부터는 65세입니다.
9. 김 씨는 59세에 회사를 나왔어요.
10. 64세까지 5년 동안, 월급도 연금도 없었죠.
11. 퇴직금은 있었지만, 손대면 안 되는 돈이라고 생각했습니다.
12. 그래서 퇴직한 다음 달, 국민연금을 5년 당겨 신청했어요.
13. 이렇게 일찍 받는 연금을 조기노령연금이라고 합니다.
14. 64세부터 받을 연금은 월 90만 원이었는데, 통장에는 63만 원이 들어왔습니다.
15. 1년 당길 때마다 6%, 5년이면 30%를 덜 받기 때문입니다.
16. 그래도 김 씨는 괜찮다고 생각했어요.
17. 64세가 되면, 원래 금액인 90만 원으로 돌아올 거라 믿었거든요.
18. 그런데 1년쯤 지나, 동창 모임에서 친구가 물었습니다.
19. 너, 그거 평생 30% 깎이는 거 알고 신청했어?
20. 친구 말이 맞았습니다.
21. 당겨 받은 비율은 64세가 돼도, 80세가 돼도 그대로입니다.
22. 그 뒤로는 63만 원에서 물가만큼만 오릅니다.
23. 집에 온 김 씨는 계산기를 꺼냈어요.
24. 84세까지 20년 동안, 매달 27만 원씩 덜 받으면 6,480만 원입니다.
25. 신청서 한 장에 6,480만 원이 날아간 거예요.
26. 그런데 이 숫자를 본 아들이, 고개를 갸웃했습니다.
27. 아빠, 이거 반만 계산하신 것 같은데요?

**아들이 찾은 구멍** — 🎙 진행자

28. 아들이 짚은 건, 김 씨가 이미 받고 있는 돈이었습니다.
29. 김 씨는 59세부터 5년 동안, 남들보다 먼저 연금을 받습니다.
30. 월 63만 원씩 60개월이면, 3,780만 원이에요.
31. 공정하게 비교하려면, 이 돈도 같이 세야 합니다.
32. 두 사람은 5년 당긴 경우와, 64세에 제때 받는 경우를 나란히 놓았습니다.
33. 국민연금법의 비율로, 금액은 모두 지금 돈 가치로 계산했어요.
34. 64세부터는 제때 받는 쪽이 매달 27만 원씩 더 받습니다.
35. 그만큼, 김 씨가 먼저 받은 3,780만 원의 차이가 줄어들어요.
36. 다 따라잡히는 데 11년 8개월이 걸립니다.
37. 김 씨가 75세 8개월이 되는 때예요.
38. 그 전에 세상을 떠나면, 오히려 일찍 받은 김 씨가 이득입니다.
39. 김 씨가 걱정한 84세까지로 다시 셈해 봤어요.
40. 손해는 6,480만 원이 아니라 2,700만 원이었습니다.
41. 아들이 한 가지를 더 찾아냈습니다.
42. 이 기준은 연금이 얼마든, 몇 년을 당기든 똑같다는 겁니다.
43. 받기 시작하고 16년 8개월이 지나야, 그때부터 손해가 됩니다.
44. 한마디로, 평생 손해인지는 몇 살까지 사느냐에 달려 있습니다.
45. 조금 마음이 놓인 김 씨에게, 친구가 한 말이 하나 더 남아 있었습니다.
46. 연금 받으면, 건보료 폭탄 맞는다더라.

**건보료 폭탄의 정체** — 🎙 진행자

47. 김 씨는 퇴직하면서 회사 건강보험에서 나와, 지역가입자가 됐습니다.
48. 아들은 아직 취업을 준비하고 있어서, 피부양자로 들어갈 곳도 없었죠.
49. 두 사람은 건보료가 어떻게 매겨지는지부터 찾아봤어요.
50. 지역가입자 건보료는 소득 몫과 재산 몫을 더해서 냅니다.
51. 집 같은 재산 몫은, 연금을 언제 받든 똑같습니다.
52. 달라지는 건 소득 몫뿐이에요.
53. 그리고 국민연금은, 이 소득 몫에 절반만 잡힙니다.
54. 1년 756만 원 가운데, 378만 원만 소득이 되는 거죠.
55. 그런데 연금이 없을 때도, 소득 몫에는 최저 금액 월 2만 160원이 붙어 있었습니다.
56. 연금을 받은 뒤 김 씨의 소득 몫은 2만 2,640원입니다.
57. 장기요양보험료까지 더해도, 연금 때문에 늘어난 건보료는 한 달에 2,810원이었어요.
58. 아들이 취업해 아들의 피부양자가 되면, 이마저도 0원입니다.
59. 연금이 1년 756만 원이라, 피부양자 소득 기준 2,000만 원보다 적기 때문이에요.
60. 건보료율과 최저 금액은 해마다 바뀌지만, 연금이 절반만 잡히는 규칙은 그대로입니다.
61. 건보료 폭탄은, 김 씨의 연금 이야기가 아니었습니다.
62. 그렇다면 김 씨를 손해 보게 만든 진짜 범인은, 도대체 뭘까요?
63. 답은 같은 해에 퇴직한, 동창 박 씨의 통장에 있었습니다.

**동창 박 씨의 통장** — 🎙 진행자

64. 박 씨도 1966년생이고, 64세부터 받을 연금도 김 씨와 같은 월 90만 원입니다.
65. 박 씨도 59세에 퇴직했어요.
66. 그런데 박 씨는 연금을 바로 신청하지 않았습니다.
67. 퇴직금에서 매달 63만 원씩, 3년을 꺼내 썼거든요.
68. 김 씨가 받은 연금과 같은 금액이라, 두 사람의 생활비는 똑같습니다.
69. 3년이면 2,268만 원이에요.
70. 그리고 62세에, 2년만 당겨 신청했습니다.
71. 12%만 덜 받아서, 월 79만 2천 원입니다.
72. 김 씨보다 매달 16만 2천 원 많아요.
73. 85세까지 계산하면, 박 씨가 받는 국민연금이 김 씨보다 2,203만 원 더 많습니다.
74. 73세 8개월이 지나면, 그때부터 박 씨가 앞서기 시작하는 거예요.
75. 두 사람을 가른 건 신청서가 아니었습니다.
76. 퇴직하기 전에, 받는 나이까지 버틸 돈을 정해 뒀느냐였습니다.
77. 한마디로, 연금을 얼마나 당길지는 버틸 돈이 정합니다.
78. 1년을 덜 당길 때마다, 평생 덜 받는 비율이 6%씩 줄어들어요.
79. 이 사실을 안 김 씨는, 마지막으로 국민연금공단을 찾아갔습니다.
80. 이미 낸 신청서, 정말 되돌릴 방법이 없을까요?

**공단 창구에서 들은 말** — 🎙 진행자

81. 상담 직원의 대답은 뜻밖이었습니다.
82. 원래 받을 나이 전이라면, 연금을 멈출 수 있다는 거예요.
83. 지급 정지를 신청하면, 연금은 원래 받을 나이인 64세에 다시 나옵니다.
84. 이때는 이미 받은 달 수만큼만, 한 달에 0.5%씩 깎습니다.
85. 김 씨는 1년을 받았으니, 6%만 덜 받게 됩니다.
86. 64세부터 월 84만 6천 원, 지금보다 21만 6천 원 많아요.
87. 대신 멈춘 4년 동안은 연금이 나오지 않습니다.
88. 4년 동안 못 받는 연금은 3,024만 원입니다.
89. 이 돈을 다 메우는 때는, 이번에도 75세 8개월이었어요.
90. 90세까지 산다면, 멈춘 쪽이 3,715만 원 더 받습니다.
91. 김 씨는 집에 와서 두 가지를 따져 봤습니다.
92. 집안 어른들은 대부분 90세 넘게 사셨어요.
93. 그리고 아껴 둔 퇴직금으로, 4년은 버틸 수 있었습니다.
94. 김 씨는 다음 날, 지급 정지를 신청했습니다.
95. 64세가 지나면, 더는 멈출 수 없기 때문입니다.
96. 김 씨가 알아낸 것을, 짧게 정리하겠습니다.

**정리** — 🎙 진행자

97. 김 씨를 손해 보게 한 건 신청서 한 장이 아니라, 버틸 돈 없이 맞은 5년이었습니다.
98. 신청서를 내기 전에도, 낸 뒤에도 이 세 가지를 꼭 보세요.
99. 첫째, 받기 시작하고 16년 8개월보다 오래 살 것 같다면 덜 당기세요.
100. 둘째, 버틸 돈이 있는 해만큼 덜 당기세요.
101. 셋째, 이미 신청했다면 받는 나이 전에 멈춰 덜 깎이게 할 수 있습니다.
102. 시청해주셔서 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
