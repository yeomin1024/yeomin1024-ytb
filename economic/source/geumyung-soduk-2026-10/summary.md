# geumyung-soduk-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py economic geumyung-soduk-2026-10` (2026-10-18 05:18). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **은퇴 부부 배당·이자 한 사람이 받으면 건보료 월 26만 원 손해**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 94 / 자막 94, 길이 8:56 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 진행자 1–94 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/geumyung-soduk-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1 = R1 (추천 — 업로드 시트 1번)** 은퇴 부부 배당·이자 한 사람이 받으면 건보료 월 26만 원 손해 `36자` — 짝 썸네일: thumbnail_1
- [ ] **T2 = R2** 은퇴 후 배당·이자 2천만 원 넘으면 건보료 월 26만 원 손해 `35자`
- [ ] **T3 = R3** 배당·이자 한 사람 이름이면, 은퇴 후 건보료 월 26만 원 손해 `36자`

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 본안(클릭률 최대): 늦은 오후 부엌 식탁에서 휴대폰을 보다 좌절한 58세 부부 + '건보료' 낱말

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 손해를 알고 좌절한 실사 부부와 그들을 내리누르는 '건보료' 낱말이 가장 클릭을 부른다

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 건보료 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50·60대 배당·이자 한 사람이 받으면 | '50·60대' 흰색 · **'배당·이자 한 사람이 받으면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 건보료 월 26만 원 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

- 노랑은 중요한 것(손해를 부르는 조건 — 배당·이자를 한 사람이 받음), 빨강은 나쁜 상황(건보료 손해와 손해를 만드는 건보료 꼬리표)에 쓴다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 58% of the width): a Korean married couple aged 58 who look youthful for their age, like their mid 50s, sitting side by side at their home kitchen table in warm late-afternoon window light, shown from the chest up and large in the frame. The husband (on the right; short neat black hair with a little gray at the temples, gray short-sleeve knit polo shirt) limply holds a smartphone in one hand with its screen facing away from the viewer (the screen only glows, no text), head bowed, eyes squeezed shut, brows knitted in pain, jaw clenched, shoulders slumped: he has just realized how much money they are losing, crushed with frustration and regret. The wife (just to his left and slightly behind; shoulder-length dark brown hair, cream blouse) covers her mouth with one hand and looks down toward his phone, devastated, inner brows raised, eyes teary. Their faces stay clearly visible (only the wife's mouth is covered). The despair must read clearly even at small thumbnail size, but stay realistic, not cartoonish, not exaggerated. Fictional people, not resembling any real or famous person.
- Left side (about 42% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "건보료" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the couple.
- Background: a cozy apartment kitchen softly blurred (sink, window), warm golden late-afternoon light; two plain mugs on the table with no text.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 배당·이자 한 사람이 받으면" — "50·60대" in white and "배당·이자 한 사람이 받으면" in bright yellow #FFD400, all with a thick black outline (keep both middle dots "·" — between 50 and 60, and between 배당 and 이자 — line 1 is the longer line: it may run to about 92% of the image width, but keep it at least 4% away from the right edge);
line 2 "건보료 월 26만 원 손해" — all in bright red #FF2A2A with a thick white outline.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the couple and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No bank, brokerage or government logos, no app screens, no charts, no account books, no piggy banks, no real banknote designs.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 실험안 ①: 같은 부엌 장면, 휴대폰을 보다 좌절한 남편 한 사람 + '건보료' 낱말

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 얼굴이 큰 한 사람이 부부 둘보다 클릭을 더 부르는가 — 배당·건보료 묶음 성공 19개 중 가상 실사 인물은 1개(S13 부부)뿐이라 근거가 적음

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 건보료 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50·60대 배당·이자 한 사람이 받으면 | '50·60대' 흰색 · **'배당·이자 한 사람이 받으면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 건보료 월 26만 원 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Right side (about 58% of the width): a Korean man aged 58 who looks youthful for his age, like his mid 50s (short neat black hair with a little gray at the temples, gray short-sleeve knit polo shirt), sitting alone at his home kitchen table in warm late-afternoon window light, shown from the chest up and very large in the frame. He limply holds a smartphone in one hand with its screen facing away from the viewer (the screen only glows, no text) and grips the back of his neck with the other hand, head bowed, eyes squeezed shut, brows knitted in pain, jaw clenched, shoulders slumped: he has just realized how much money he and his wife are losing, crushed with frustration and regret. His face stays clearly visible, not covered by his hands. The despair must read clearly even at small thumbnail size, but stay realistic, not cartoonish, not exaggerated. Fictional person, not resembling any real or famous person.
- Left side (about 42% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "건보료" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down toward the man.
- Background: a cozy apartment kitchen softly blurred (sink, window), warm golden late-afternoon light; one plain mug on the table with no text.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 배당·이자 한 사람이 받으면" — "50·60대" in white and "배당·이자 한 사람이 받으면" in bright yellow #FFD400, all with a thick black outline (keep both middle dots "·" — between 50 and 60, and between 배당 and 이자 — line 1 is the longer line: it may run to about 92% of the image width, but keep it at least 4% away from the right edge);
line 2 "건보료 월 26만 원 손해" — all in bright red #FF2A2A with a thick white outline.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the man and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and the face inside the central 16:9 area, at least 8% away from the top and bottom edges.
No bank, brokerage or government logos, no app screens, no charts, no account books, no piggy banks, no real banknote designs.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 실험안 ②: 사람 없이, 식탁 위 지폐 더미를 짓누르는 빨강 '건보료' 덩어리

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 사람 없이 '건보료'가 돈을 짓누르는 장면만으로도 같은가 — 노후·연금·절세 묶음 사람 없음 18% vs 7%, 배당·건보료 묶음 성공 19개 중 사람 없음 2 + 손만 2

| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 건보료 | 흰 글자 on 빨강 덩어리 앞면 #FF2A2A |
| 하단 1줄 | 50·60대 배당·이자 한 사람이 받으면 | '50·60대' 흰색 · **'배당·이자 한 사람이 받으면' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 건보료 월 26만 원 손해 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size. No people.
Upper 62% of the frame:
- Center to right: on a wooden kitchen table in warm late-afternoon window light, one neat bundled stack of plain generic banknotes with no portraits and no numbers. A heavy solid bright red (#FF2A2A) block presses down on the stack from above, crushing it so the stack bends and a few loose plain bills scatter on the table. On the flat front face of the red block, the Korean word "건보료" is printed in huge flat heavy bold white letters (flat print, not carved or 3D letter shapes), facing the viewer and fully visible.
- Upper left: two thick bright red arrows pointing down onto the red block.
- Background: a cozy apartment kitchen softly blurred (sink, window), warm golden late-afternoon light; two plain mugs at the far end of the table with no text.
- Only ONE stack of money (do not split it into two piles).
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 배당·이자 한 사람이 받으면" — "50·60대" in white and "배당·이자 한 사람이 받으면" in bright yellow #FFD400, all with a thick black outline (keep both middle dots "·" — between 50 and 60, and between 배당 and 이자 — line 1 is the longer line: it may run to about 92% of the image width, but keep it at least 4% away from the right edge);
line 2 "건보료 월 26만 원 손해" — all in bright red #FF2A2A with a thick white outline.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the money and the red block in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and the red block inside the central 16:9 area, at least 8% away from the top and bottom edges.
No bank, brokerage or government logos, no app screens, no charts, no account books, no piggy banks, no real banknote designs.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
1년에 배당과 이자를 2,400만 원씩 받는 58세 부부가 둘인데, 한 부부는 건보료가 한 달 26만 원이 넘고 다른 부부는 0원입니다. 6억 원을 남편 한 사람 이름으로 두었는지, 부부가 나눠 두었는지가 달랐을 뿐입니다.
배당·이자로 생활비를 받는 분이 금융소득 2,000만 원 기준과 건보료 피부양자 기준을 어떻게 지키는지 순서대로 정리했습니다.

■ 이 영상에서 다루는 것
- 원칙 1: 금융소득(이자+배당)은 사람마다 1년 합계로 따로 센다 — 다른 소득이 없으면 2,000만 원을 넘어도 소득세는 거의 그대로, 차이는 건보료(피부양자 소득 기준 2,000만 원, 부부 모두)
- 원칙 2: 계좌마다 세는 법이 다르다 — ISA·연금저축 안의 이자·배당은 2,000만 원 합계에 들어가지 않음, 2,000만 원을 넘긴 해가 있으면 3년 동안 ISA를 새로 못 만듦, 2026년 고배당 기업 배당 분리과세
- 원칙 3: 건보료는 1년 늦게 잡힌다 — 올해 이자·배당은 내년 11월부터 1년
- 할 일: 합계 확인 → 나누기 → ISA
- 이미 2,000만 원을 넘긴 분, 피부양자가 될 곳이 없어 지역 보험료를 내는 분이 할 일

■ 챕터
0:00 같은 2,400만 원, 다른 건보료
0:57 두 부부의 조건
1:57 원칙 1 금융소득은 사람마다 따로 센다
3:49 원칙 2 계좌마다 세는 법이 다르다
5:02 원칙 3 건보료는 1년 늦게 잡힌다
5:49 할 일 합계 확인 → 나누기 → ISA
6:26 두 부부의 결과
7:29 이미 2,000만 원을 넘겼다면
8:16 정리

■ 예시에 대해
영상 속 두 부부(58세 동갑, 금융자산 6억 원, 이자·배당 연 4%, 집 재산세 과세표준 3억 원, 직장인 자녀의 피부양자)는 계산용 가상 사례입니다. 숫자는 2026년 10월 기준이며, 건보료에는 장기요양보험료를 넣지 않았습니다.
이 영상의 내레이션은 AI 음성으로 만들었습니다.

■ 근거
2026년 10월 18일 시행 중인 법령 원문으로 확인: 소득세법(제14조 금융소득 종합과세 기준·제62조 세액 계산 특례)·같은 법 시행령, 조세특례제한법(제91조의18 개인종합자산관리계좌·제104조의27 고배당기업 배당소득 과세특례·제129조의2)·같은 법 시행령, 국민건강보험법·같은 법 시행령(제41조 소득월액·제44조 보험료율)·같은 법 시행규칙(제44조·별표 1의2 피부양자 기준), 지방세법, 상속세 및 증여세법(제53조 배우자 증여재산 공제)

■ 알려 드립니다
이 영상은 정보 제공을 위한 것이며 세무·보험·투자 상담이나 권유가 아닙니다. 특정 종목이나 상품을 추천하지 않습니다.
제도와 기준 금액은 바뀔 수 있으니, 실제로 옮기거나 신고하기 전에 국세청·건강보험공단에서 내 금액을 확인하세요.

#건보료 #금융소득종합과세 #은퇴
```

**태그**: 금융소득 종합과세, 금융소득 2천만원, 배당 건보료, 이자 건보료, 건보료 피부양자, 피부양자 소득 기준, 은퇴 후 건보료, 배당 생활비, ISA 건보료, 부부 증여, 50대 노후, 60대 노후, 재테크

**고정 댓글**

```
배당·이자로 생활비를 받는다면 이 두 가지부터 확인해 보세요.
1. 올해 받은 이자·배당 합계 — 부부 각자, 모든 은행·증권 계좌를 합쳐서 (한 사람 2,000만 원, 지역가입자는 1,000만 원)
2. 내 이름 ISA가 있는지 (금융소득이 2,000만 원을 넘긴 해가 있으면 3년 동안 새로 못 만듦)
올해 받은 이자·배당은 부부가 각각 얼마쯤 되시나요?
정보 제공용이며 세무·보험 상담이 아닙니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**같은 2,400만 원, 다른 건보료** — 🎙 진행자

1. 배당과 이자로 생활비를 받고 계시다면, 이 숫자부터 보세요.
2. 1년에 배당과 이자를 2,400만 원씩 받는 58세 부부가 둘 있습니다.
3. 그런데 한 부부는 건보료가 한 달 26만 원이 넘고, 다른 부부는 0원입니다.
4. 왜 이렇게 차이가 날까요?
5. 6억 원을 남편 한 사람 이름으로 두었는지, 부부가 나눠 두었는지가 달랐을 뿐이에요.
6. 두 부부가 3년 동안 받으면, 세금과 건보료를 합친 차이가 1,000만 원이 넘습니다.
7. 결론부터 말씀드리겠습니다.
8. 이자와 배당은 부부가 나눠서 받고, ISA부터 채우고, 12월 전에 사람마다 1년 합계를 확인한다.
9. 이 세 가지입니다.
10. 이미 이자와 배당이 1년 2,000만 원을 넘긴 분이 할 일도 끝까지 보여드릴게요.
11. 먼저 두 부부의 경우를 통해 알아보겠습니다.

**두 부부의 조건** — 🎙 진행자

12. 두 부부는 모두 58세 동갑이고, 남편이 56세에 퇴직해 둘 다 일하지 않습니다.
13. 국민연금은 아직 받지 않고, 지금은 직장에 다니는 자녀의 피부양자예요.
14. 집은 남편 이름의 아파트 한 채이고, 재산세 과세표준은 3억 원입니다.
15. 금융자산 6억 원에서 이자와 배당이 1년에 4%, 2,400만 원 나온다고 봤습니다.
16. A 부부는 6억 원을 모두 남편 이름의 일반 은행·증권 계좌에 둡니다.
17. B 부부는 3억 원을 아내 이름으로 옮기고, 부부가 각자 ISA에 해마다 2,000만 원씩 넣습니다.
18. 돈과 수익률, 집은 똑같고, 누구 이름의 어느 계좌인지만 다릅니다.
19. 세금과 건보료는 지금 시행 중인 소득세법과 건강보험 규정의 계산식으로 계산했습니다.
20. 두 부부의 차이는 세 가지 원칙에서 나옵니다.
21. 하나씩 보겠습니다.

**원칙 하나, 금융소득은 사람마다 따로 센다** — 🎙 진행자

22. 첫 번째 원칙은, 금융소득은 사람마다 1년 합계로 따로 센다는 것입니다.
23. 금융소득은 이자와 배당을 합친 돈이에요.
24. 한 사람의 금융소득이 1년 2,000만 원을 넘으면, 다른 소득과 합쳐 세금을 다시 계산합니다.
25. 2,000만 원을 넘으면 세금 폭탄이라고 걱정하시는 분이 많은데요.
26. A 부부의 남편처럼 다른 소득이 없으면, 5월에 신고는 해도 소득세는 더 늘지 않습니다.
27. 다시 계산한 세금과 받을 때 뗀 15.4% 중 큰 쪽을 내는데, 뗀 쪽이 더 크기 때문이에요.
28. 다른 소득이 없다면, 금융소득이 1년 약 8천만 원이 될 때까지 그렇습니다.
29. 진짜 차이는 건보료에서 납니다.
30. 피부양자 소득 기준도 1년 2,000만 원입니다.
31. 금융소득은 1,000만 원을 넘으면 전부 소득으로 잡혀요.
32. A 부부는 남편이 2,400만 원이라 이 기준을 넘습니다.
33. 부부가 둘 다 지켜야 하는 기준이라, 소득이 없는 아내까지 피부양자에서 빠집니다.
34. 둘 다 건보료를 따로 내는 지역가입자가 돼요.
35. 이자와 배당에 약 14만 4천 원, 집에 약 12만 4천 원이 붙습니다.
36. 건보료가 한 달 26만 원이 넘어요.
37. B 부부는 한 사람이 1,200만 원씩이라, 전부 소득으로 잡혀도 둘 다 2,000만 원 안이에요.
38. 집도 재산 기준인 과세표준 5억 4천만 원 안이라, 건보료는 0원입니다.
39. 2,000만 원 기준이 사람마다 하나씩이라, 부부가 나누면 바구니가 두 개가 되는 셈이죠.
40. 부부 사이에는 10년에 6억 원까지 증여세 없이 옮길 수 있어요.
41. 한마디로, 이자와 배당은 부부가 나눠서 받으세요.

**원칙 둘, 계좌마다 세는 법이 다르다** — 🎙 진행자

42. 두 번째 원칙은, 같은 배당이라도 계좌마다 세는 법이 다르다는 것입니다.
43. ISA 안에서 받은 이자와 배당은 2,000만 원 합계에 들어가지 않습니다.
44. 건보료 1,000만 원 기준을 셀 때도 빠져요.
45. 세금도 해지할 때 이익 200만 원까지는 없고, 넘는 몫에 9.9%만 냅니다.
46. ISA는 한 사람 하나씩, 1년에 2,000만 원까지 넣을 수 있어요.
47. 연금저축 계좌 안에서 받은 이자와 배당도, 꺼내기 전에는 금융소득이 아닙니다.
48. 55세가 넘어 연금으로 꺼낼 때는 5.5%에서 3.3%만 내요.
49. 다만 금융소득이 2,000만 원을 넘긴 해가 있으면, 그 사람은 3년 동안 ISA를 새로 못 만듭니다.
50. 올해부터는 요건을 갖춘 고배당 기업 주식의 배당도, 5월 신고 때 신청하면 합계에서 빼고 따로 세금을 냅니다.
51. 다만 건보료에서도 빠지는지는 공단 확인이 필요해, 예시 계산에는 넣지 않았습니다.
52. 한마디로, 일반 계좌의 이자와 배당을 줄이려면 ISA부터 채우세요.

**원칙 셋, 건보료는 1년 늦게 잡힌다** — 🎙 진행자

53. 세 번째 원칙은, 건보료는 1년 늦게 잡힌다는 것입니다.
54. 올해 받은 이자와 배당은, 내년 11월부터 1년 동안 건보료에 잡힙니다.
55. 예를 들어 1억 원을 연 3.5%, 3년 만기 예금에 넣었다고 해 보죠.
56. 이자를 만기에 한꺼번에 받으면, 3년치 이자 약 1,050만 원이 받은 해에 다 잡힙니다.
57. 다른 이자와 배당이 1,000만 원만 있어도, 그해는 2,000만 원을 넘어요.
58. 그래서 예금은 만기가 해마다 오도록 나눠 넣는 쪽이 안전합니다.
59. 한마디로, 12월이 오기 전에 올해 받은 이자와 배당을 사람마다 확인하세요.
60. 그럼 이 세 가지 원칙으로 할 일을 순서대로 정해 보겠습니다.

**할 일, 합계 확인 → 나누기 → ISA** — 🎙 진행자

61. 1단계, 올해 부부가 받은 이자와 배당을 사람마다 더해 봅니다.
62. 혹시 은행 이자와 증권사 배당을 따로따로 보고 계시진 않나요?
63. 기준은 모든 계좌를 합친 금액이에요.
64. 2단계, 한 사람이 2,000만 원을 넘을 것 같으면, 예금이나 주식 일부를 배우자 이름으로 옮깁니다.
65. 3단계, 부부가 각자 ISA에 해마다 2,000만 원씩 옮깁니다.
66. ISA에 다 못 넣는 돈은 연금저축에 넣으세요.
67. 그럼 두 부부의 결과는 얼마나 달라졌을까요?

**두 부부의 결과** — 🎙 진행자

68. 두 부부가 3년 동안 받으면, A 부부는 세금 약 1,109만 원에 건보료 약 964만 원을 냅니다.
69. B 부부는 세금 약 1,019만 원이고, 건보료는 0원이에요.
70. 차이는 1,000만 원이 넘고, 그중 약 960만 원이 건보료입니다.
71. 세금은 ISA 덕분에 B 부부가 약 90만 원 덜 냈어요.
72. A 부부의 건보료는 1년에 약 320만 원이고, 남편 이름으로 받는 동안 해마다 나옵니다.
73. 이 건보료에는 장기요양보험료를 넣지 않았습니다.
74. 피부양자가 될 곳이 없어 지역 보험료를 내는 부부는, 기준이 한 사람 1,000만 원입니다.
75. 이때는 나누고 ISA와 연금저축까지 써서, 한 사람 1,000만 원 아래로 낮추세요.
76. 예시 금액이라면 건보료가 한 달 약 12만 원 줄어요.
77. 그런데 이미 올해 이자와 배당이 2,000만 원을 넘긴 분들도 계실 텐데요.
78. 그럼 어떻게 해야 할까요?

**이미 2,000만 원을 넘겼다면** — 🎙 진행자

79. 늦지 않았습니다.
80. 올해 받은 이자와 배당 때문에, 내년 11월부터 1년 동안은 지역 보험료가 나옵니다.
81. 하지만 내년에 받을 이자와 배당부터 부부가 나눠 보세요.
82. 그러면 그다음 해 11월에는 자녀가 다시 피부양자로 올릴 수 있어요.
83. 건보료는 1년, 약 320만 원으로 끝납니다.
84. 3년 동안 그대로 받을 때보다 약 640만 원 덜 내요.
85. 2,000만 원을 넘긴 남편은 3년 동안 ISA를 새로 못 만드니, 아내 ISA부터 채우세요.
86. 남편 몫은 연금저축으로 옮겨, 일반 계좌의 이자와 배당을 줄이면 됩니다.
87. 자, 마지막으로 오늘 내용을 정리하겠습니다.

**정리, 바뀌어도 그대로인 것** — 🎙 진행자

88. 2,000만 원과 1,000만 원 기준, 건보료율, 고배당 특례는 바뀔 수 있습니다.
89. 그래도 이 세 가지는 그대로입니다.
90. 첫째, 금융소득은 사람마다 따로 세니, 이자와 배당은 부부가 나눠서 받으세요.
91. 둘째, ISA와 연금저축 안의 이자와 배당은 합계에 들어가지 않으니, ISA부터 채우세요.
92. 셋째, 건보료는 1년 늦게 잡히니, 12월 전에 사람마다 1년 합계를 확인하세요.
93. 오늘 은행과 증권사 앱에서 올해 받은 이자와 배당부터 더해 보세요.
94. 시청해주셔서 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
