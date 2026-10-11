# washer-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py lifetips washer-2026-10` (2026-10-11 03:58). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **업체비 12만원 아끼려고 세탁기를 직접 분해했다가 수리비 21만원이 나왔습니다. 설명서 없이 뜯은 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 89 / 자막 123, 길이 8:39 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–15 · 진행자 16–89 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/washer-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 업체비 12만원 아끼려고 세탁기를 직접 분해했다가 수리비 21만원이 나왔습니다. 설명서 없이 뜯은 사람들의 공통점 `행동 · 아끼려던 돈→나간 돈 · 공통점` 63자 — 짝 썸네일: thumbnail_1 (영수증 숫자 반전)
- [ ] **T2.** 30분이면 된다는 영상만 믿고 통돌이를 뜯었다가 수리비 21만원을 냈습니다. 세탁기 셀프 분해한 사람들의 불편한 진실 `계기(속마음) · 쉬움→대가 · 불편한 진실` 65자 — 짝 썸네일: thumbnail_2 (인물·나사 몇 개)
- [ ] **T3.** (짧은 변형) 세탁기 청소 방법 따라 하다 수리비 21만원, 마지막에 꼭 하는 후회 `검색어형 · 수리비 21만원 · 마지막에 꼭 하는 후회` 38자 — 짝 썸네일: thumbnail_3 (30분 vs 21만 원 대비)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (영수증 카드)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 아끼려던 돈(12만 원)이 더 큰 수리비(21만 원)로 뒤집힌 **영수증 숫자 반전**이 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1 | 12만 원 아끼려다 | "12만 원" 파랑 #2D6CDF / "아끼려다" 잉크 #1E1E1E | "아끼려다"에 노랑 형광펜 #FFD400 (유일한 강조) |
| 2 | 수리비 21만 원 | 흰색 (빨강 #E63B2E 상자 위) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, saved-money blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the center, a tall plain
white paper receipt with a torn zigzag bottom edge, slightly tilted, filling most of the frame height (a generic receipt,
NOT any real company's service form: no logo, no company name, no barcode, no QR code, no table lines).
Top part of the receipt: the text "12만 원" in large blue (#2D6CDF) bold letters, followed on the same line by the word
"아끼려다" in black bold letters over a bright yellow (#FFD400) highlighter stripe.
Below it, one thick red (#E63B2E) arrow pointing down.
The lower half of the receipt is a wide solid red (#E63B2E) rounded box with the huge white bold text "수리비 21만 원",
the largest element in the image, about a quarter of the frame height.
Optionally, behind the receipt, a soft out-of-focus top of a plain generic white top-loading washing machine with no
brand, no logo and no buttons layout from a real product. No people, no hands, no tools. Keep all text inside the
central 16:9 safe area. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (손바닥의 나사 몇 개)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 다시 조립하고 **남은 나사 몇 개를 보며 당황한 사람의 표정**이 숫자 카드보다 감정을 더 끈다 (주식 성공 썸네일 관찰: 감정이 드러난 얼굴 — 이 주제는 임시 차용, `data_insights.md` 6번)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1 | 드라이버 하나면 된다더니 | 검정 #1E1E1E | 노랑 상자 #FFD400 (유일한 강조, 글자 전체 높이) |
| 2 | 21만 원 | 흰색 (빨강 #E63B2E 상자) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, saved-money blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style, bright small Korean apartment utility room with cream and white tones, soft daylight.
On the left 45% of the frame, a fictional Korean woman in her late 30s wearing simple comfortable homewear, looking down
at her open palm that holds three or four small silver screws, with a puzzled, regretful, slightly deflated expression
(no crying, no fear). Fictional person, not resembling any real or famous person, natural Korean features.
Behind her, a plain generic white top-loading washing machine with its lid open, fully assembled and intact
(no brand, no logo, no copied button layout of any real product). No tools in use, no cables, no water, no mess.
On the right side, a solid bright yellow (#FFD400) box with the black bold text "드라이버 하나면 된다더니", and below it
a wide solid red (#E63B2E) rounded box with the huge white bold text "21만 원", the largest element.
Keep the face and all text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (꿀팁이 약속한 30분 vs 수리비)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 꿀팁이 약속한 **쉬움("혼자서 30분")과 결과(21만 원)를 나란히** 놓으면, 같은 꿀팁을 본 시청자가 "내 얘기다"를 가장 빨리 느낀다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 혼자서 30분 | 파랑 #2D6CDF (크림 배경 위) | — |
| 오른쪽 | 21만 원 | 흰색 (빨강 #E63B2E 상자) | 가장 큰 글자 |
| 가운데 | (글자 없음) 노랑 화살표 → | 노랑 #FFD400 | 유일한 강조 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, saved-money blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Split-screen comparison divided vertically in the middle by a thin white line.
LEFT half: bright cream (#F2EBDD) background, a top-down view into the clean shiny stainless inner drum of a plain
generic top-loading washing machine, a few water droplets, fresh and bright. Above it, the large blue (#2D6CDF) bold
text "혼자서 30분".
RIGHT half: dark navy (#14213D) background, a plain generic white top-loading washing machine standing with its lid
closed, looking switched off and stopped, dim lighting, intact (not broken apart, no parts, no water, no smoke).
Above it, in the upper part of the right half, a solid red (#E63B2E) rounded box with the huge white bold text "21만 원",
the largest element in the image.
On the dividing line in the center, one small bright yellow (#FFD400) arrow pointing from left to right.
Washing machines have no brand, no logo and no copied button layout of any real product. No people, no tools.
Keep all text inside the central 16:9 safe area; leave the bottom-right corner empty.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
혼자서도 30분이면 된다는 영상을 보고 4년 된 통돌이 세탁기를 직접 뜯었더니, 12만 원 견적보다 9만 원 많은 수리비 21만 원이 나왔습니다.
세탁기 청소를 영상만 보고 따라 하면 왜 손해 보기 쉬운지 3가지로, 내 세탁기에 맞게 세탁조를 관리하는 방법을 5가지로 정리했습니다.

■ 이 영상에서 다루는 것
- 영상 속 세탁기는 우리 집 세탁기가 아니다 (같은 세탁조 청소에도 가전 회사마다 정반대인 안내)
- 직접 뜯다 생긴 고장은 내 돈 (서비스 요금 구성, 고객 부주의 유상 기준, 2026년 출장비)
- 분해해야만 깨끗해진다는 믿음 (통세척 주기, 거름망 관리)
- 세탁조 관리 5가지: 모델명으로 설명서부터, 통세척 날짜 정하기, 세척제는 표시된 양만, 직접 할 청소와 맡길 청소 나누기, 맡길 때 보증 조건 묻기

■ 챕터
0:00 사연: 업체비 12만 원 아끼려다 수리비 21만 원
1:22 왜 세탁기를 직접 뜯을까
2:25 문제 01 영상 속 세탁기는 우리 집 세탁기가 아니다
3:27 문제 02 직접 뜯다 생긴 고장은 내 돈
4:18 문제 03 분해해야만 깨끗해진다는 믿음
5:16 첫째: 모델명으로 설명서부터
5:52 둘째: 통세척 날짜 정해 두기
6:20 셋째: 세척제는 표시된 양만
6:59 넷째: 직접 할 청소와 맡길 청소 나누기
7:38 다섯째: 맡길 때 보증 조건 묻기
8:16 정리

■ 사연에 대해
이 영상의 사연은 실제 기준과 공식 자료를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시입니다.

■ 출처 (제조사 공식 안내는 사실 확인용이며 특정 제품을 추천하지 않습니다)
- 삼성전자서비스 고객지원, 세탁조 통세척 권장 세척제: https://www.samsungsvc.co.kr/solution/41381
- 삼성전자서비스 고객지원, 세탁통 녹 원인: https://www.samsungsvc.co.kr/solution/41708
- 삼성전자서비스 고객지원, 세탁기 거름망 청소: https://www.samsungsvc.co.kr/solution/28556
- 삼성전자서비스 서비스 요금 안내(2026년 1월 기준): https://www.samsungsvc.co.kr/info/fee
- 삼성전자서비스 출장비 안내(2026년 1월 8일부터): https://www.samsungsvc.co.kr/solution/1014598
- SBS Biz 2026년 1월 5일, 가전 출장비 인상 보도: https://biz.sbs.co.kr/amp/article/20000282569
- LG전자 고객지원, 세탁조 클리너와 통살균: https://www.lge.co.kr/support/solutions-1779686
- LG전자 고객지원, 통살균 코스 사용 시기: https://www.lge.co.kr/support/solutions-1430888637954
- LG전자 고객지원, 통세척 기능이 없는 모델의 세탁조 청소: https://www.lge.co.kr/support/solutions-1430889036106
- LG전자 고객지원 공지, 세탁기 세척 서비스 무상 A/S 조건(2026년 9월): https://www.lge.co.kr/support/notice-NTC20260907574001
- 채널 조회수·댓글: 이 채널의 유튜브 살림 영상 분석(2025년 10월~2026년 9월 업로드 영상, 2026년 10월 분석)

■ 따라 하기 전에 확인하세요
이 영상은 생활 정보 제공을 위한 것이며, 특정 제품이나 업체를 추천하지 않습니다.
사연은 실제 기준과 공식 자료를 바탕으로 재구성한 이야기이고, 금액과 수치는 예시입니다.
제품과 집 구조마다 방법이 다르니, 제조사 사용설명서와 제품 표시사항을 먼저 따르세요.
세정제와 표백제는 서로 섞지 말고, 환기하면서 표시된 방법대로만 쓰세요.
영상 속 자료의 출처는 설명란에 있습니다.

#생활꿀팁 #세탁기청소 #세탁조청소
```

**태그**: 세탁기 청소 방법, 세탁기 청소, 세탁조 청소, 통돌이 세탁기 청소, 세탁기 분해 청소, 세탁기 셀프 청소, 세탁조 클리너, 통세척, 세탁기 거름망 청소, 세탁기 수리비, 세탁기 고장, 생활꿀팁, 살림꿀팁, 살림 노하우, 청소 꿀팁

**고정 댓글**

```
세탁기를 뜯기 전에 이 두 가지만 확인해 보세요.
1. 세탁기 모델명으로 찾은 사용설명서의 '세탁조 청소' 항목 (세척제 종류·양·코스)
2. 마지막으로 통세척 코스를 돌린 날짜

꿀팁을 따라 했다가 오히려 손해 본 적 있나요? 그때 무엇을 먼저 확인했으면 좋았을까요?
※ 제품마다 방법이 다르니 사용설명서를 먼저 확인해 주세요. 특정 제품 홍보·구매 링크 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 지난 9월부터 빨래마다 미역 같은 검은 찌꺼기가 묻어 나오기 시작했어요.
2. 업체에 물어보니 세탁기 분해 청소에 12만 원이 든다더라고요.
3. 그러다 혼자서도 30분이면 된다는 분해 청소 영상을 봤죠.
4. 저는 서른여덟, 맞벌이에 아이 둘 키우는 엄마라 세탁기를 매일 한 번씩 돌려요.
5. 드라이버 하나면 된다길래 주말에 4년 된 통돌이를 직접 뜯어 보기로 했어요.
6. 세탁조를 들어내니 시커먼 찌꺼기가 한 바가지 나왔어요.
7. 12만 원을 아꼈다는 생각에 정말 뿌듯했죠.
8. 하지만 진짜 비용은 다시 조립한 다음부터 시작됐습니다.
9. 첫 탈수에서 쾅쾅 소리가 나더니 세탁기가 앞으로 밀려 나왔어요.
10. 결국 월요일 낮에 기사님을 불렀는데, 출장비를 합쳐 수리비가 21만 원이 나왔어요.
11. 다시 끼울 때 부품 하나가 제자리에 들어가지 않아 깨졌다는 거예요.
12. 기사님은 통세척을 얼마나 자주 하셨냐고도 물으셨어요.
13. 4년 동안 통세척 코스를 한 번도 돌린 적이 없었는데 말이죠.
14. 12만 원 아끼겠다고 푼 나사 몇 개가 21만 원이 되어 돌아왔어요.
15. 영상은 몇 번이나 돌려 봤으면서, 제 세탁기 설명서는 한 번도 펴 보지 않았네요.

**진행자 파트** — 🎙 진행자

16. 세탁기에서 찌꺼기가 나오기 시작하면 많은 분들이 이런 생각을 하죠.
17. 영상에서 30분이면 된다니까 나도 할 수 있겠지.
18. 세탁기 구조야 다 비슷하겠지.
19. 업체에 12만 원 주는 건 너무 아까워.
20. 이런 식으로 남의 세탁기로 찍은 영상을 내 세탁기 설명서처럼 믿게 됩니다.
21. 이 채널이 최근 1년 동안 올라온 살림 영상을 분석해 봤습니다.
22. 혼자서 통돌이를 분해해 청소하는 영상이 크게 인기를 끌었죠.
23. 구독자 4천 명 남짓한 채널에서도 조회수 100만 회를 넘겼습니다.
24. 그런데 세탁기 꿀팁 영상의 댓글에는 따라 하다 고장 났다는 경험담도 달립니다.
25. 사연 속 이야기가 결코 남의 일이 아닌 이유입니다.
26. 그럼 세탁기를 혼자 분해하면 왜 손해로 이어지기 쉬운지 하나씩 살펴보겠습니다.

> 🟨 [장면] 따라 하기 전에 확인하세요 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 생활 정보 제공을 위한 것이며, 특정 제품이나 업체를 추천하지 않습니다.
> 사연은 실제 기준과 공식 자료를 바탕으로 재구성한 이야기이고, 금액과 수치는 예시입니다.
> 제품과 집 구조마다 방법이 다르니, 제조사 사용설명서와 제품 표시사항을 먼저 따르세요.
> 세정제와 표백제는 서로 섞지 말고, 환기하면서 표시된 방법대로만 쓰세요.
> 영상 속 자료의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

27. 첫 번째 문제는 영상 속 세탁기가 우리 집 세탁기가 아니라는 것입니다.
28. 같은 세탁조 청소를 두고도 가전 회사마다 안내가 정반대인 경우가 있습니다.
29. 한 가전 회사는 통세척에 액체 염소계 표백제나 세탁조 세정제를 넣으라고 안내합니다.
30. 다른 가전 회사의 안내는 반대입니다.
31. 염소계나 산성 클리너로 세탁조를 청소하면 안쪽이 변색되거나 부식될 수 있다는 거죠.
32. 그래서 이 회사는 산소계 세탁조 클리너를 권장량대로 쓰라고 합니다.
33. 같은 회사 제품이라도 통세척 코스가 있는 모델과 없는 모델은 청소 순서가 다릅니다.
34. 세척제 하나도 이렇게 다른데, 나사 위치와 부품 모양까지 같다고 장담하기는 어렵죠.
35. 꿀팁이 틀렸다는 게 아니라, 내 세탁기에 맞는지 확인하는 순서가 빠졌다는 겁니다.
36. 사연자가 본 30분짜리 영상도 그 영상 속 세탁기의 방법이었을 뿐이죠.
37. 두 번째는 직접 분해하다 생긴 고장은 고스란히 내 돈이 된다는 것입니다.
38. 한 가전 회사의 서비스 요금은 출장비와 부품비, 그리고 기술료인 수리비를 더해 정해집니다.
39. 출장비만 해도 올해 9월 평일 낮 기준 2만 8천 원입니다.
40. 부품비와 수리비는 어떤 부품을 얼마나 고쳐야 하는지에 따라 달라지고요.
41. 사용설명서의 주의사항을 지키지 않아 생긴 고장은 고객 부주의로 보고 유상으로 고칩니다.
42. 보증 기간이 남아 있어도 직접 뜯다 생긴 고장은 돈을 내야 할 수 있다는 뜻입니다.
43. 사연자의 21만 원도 출장비 2만 8천 원에 부품비와 수리비가 더해진 금액이었습니다.
44. 12만 원을 아끼려다 업체 견적보다 9만 원을 더 쓴 셈이죠.
45. 세 번째는 분해해야만 깨끗해진다는 믿음입니다.
46. 제조사들이 집에서 하라고 안내하는 건 분해가 아니라 정기적인 통세척과 거름망 관리입니다.
47. 한 가전 회사는 세탁기를 30번 이상 썼다면 통세척 코스를 돌리라고 안내합니다.
48. 화면에 통세척을 알리는 표시가 떠도 마찬가지고요.
49. 하루 한 번 빨래하는 집이라면 한 달에 한 번꼴이죠.
50. 4년이면 50번 가까이 했어야 할 통세척을, 사연자는 한 번도 하지 않았습니다.
51. 다른 가전 회사는 거름망의 구멍이 막히면 빨래에 찌꺼기가 묻어 나올 수 있다고 안내합니다.
52. 그래서 거름망이 절반 넘게 차기 전에, 빨래가 끝날 때마다 확인해 비우라고 하죠.
53. 빨래에 묻어 나온 찌꺼기가 꼭 세탁기를 뜯으라는 신호는 아니었던 겁니다.
54. 그렇다면 세탁기는 어떻게 관리해야 할까요?

**올바른 방법 파트** — 🎙 진행자

55. 첫째, 꿀팁 영상보다 내 세탁기 모델명부터 확인하는 것입니다.
56. 세탁기에 붙은 제품 표시 스티커에서 모델명을 찾아 적어 두세요.
57. 그 모델명으로 제조사 고객지원 홈페이지에서 사용설명서를 찾아보세요.
58. 세탁조 청소 항목에서 어떤 세척제를, 얼마나, 어떤 코스로 쓰는지 확인하세요.
59. 사연자의 통돌이 설명서에 산소계 클리너를 쓰라고 적혀 있다고 해 볼까요?
60. 그렇다면 염소계 표백제를 쓰라는 꿀팁은 그 집 세탁기에는 맞지 않는 방법입니다.
61. 둘째, 통세척 날짜를 미리 정해 두는 것입니다.
62. 설명서에 나온 주기를 빨래 횟수로 바꿔 보면 쉽습니다.
63. 30번마다 하라는 안내라면, 사연자처럼 하루 한 번 빨래하는 집은 한 달에 한 번입니다.
64. 매달 첫 주말처럼 날짜를 정해 휴대폰 달력에 반복 알림을 걸어 두세요.
65. 통세척 중에는 빨래를 넣지 말고, 끝나면 뚜껑을 열어 세탁조를 말려 주세요.
66. 셋째, 세척제는 설명서와 제품에 표시된 양만 쓰는 것입니다.
67. 사연자처럼 찌꺼기가 한 바가지 나오면 세척제를 두세 배 넣고 싶어지죠.
68. 하지만 한 가전 회사는 염소계 표백제를 과하게 쓰면 세탁통에 녹이 생길 수 있다고 합니다.
69. 다른 가전 회사도 세탁조 클리너와 섬유유연제까지 권장량으로 쓰라고 하고요.
70. 염소계 표백제를 식초나 구연산, 산소계 표백제와 섞어 쓰지 말라는 안내도 있습니다.
71. 더 세게 하고 싶을수록 양과 종류는 설명서에 적힌 그대로 지키는 게 먼저입니다.
72. 넷째, 직접 할 청소와 맡길 청소를 나누는 것입니다.
73. 기준은 간단합니다.
74. 설명서에 방법이 나와 있으면 직접 하고, 나와 있지 않으면 맡기는 겁니다.
75. 거름망 비우기와 통세척 코스 돌리기처럼 설명서가 알려 주는 일은 직접 해도 됩니다.
76. 세탁조를 들어내는 분해처럼 설명서에 없는 일은 제조사 서비스나 전문 업체에 맡기세요.
77. 한 가전 회사도 전문 분해 세척이 필요하면 서비스 상담을 받으라고 안내합니다.
78. 사연자도 세탁조를 들어내기 전에 설명서만 펴 봤다면 멈출 수 있었을 겁니다.
79. 다섯째, 맡길 때는 청소 뒤에 고장이 나면 어떻게 되는지까지 물어보는 것입니다.
80. 예를 들어 한 가전 회사의 세척 서비스는 세척을 마친 날부터 1년 동안 보증이 붙습니다.
81. 그사이 고장이 나면 출장비와 수리비, 부품비를 받지 않는다고 안내하죠.
82. 다만 필터 같은 소모품과 고객 과실로 생긴 고장은 빠집니다.
83. 그러니 견적을 받을 때 가격만 비교하지 말고, 보증 기간과 조건을 함께 물어보세요.
84. 12만 원이 아깝게 느껴진다면, 그 값에 무엇이 들었는지부터 따져 보세요.

**마무리** — 🎙 진행자

85. 이렇게 해서 세탁기를 혼자 뜯으면 손해 보기 쉬운 이유와 관리법을 알아보았습니다.
86. 세탁기를 뜯기 전에, 모델명으로 설명서의 세탁조 청소 항목부터 확인해 보세요.
87. 그리고 이번 달 통세척 날짜를 달력에 적어 두세요.
88. 안전하고 알뜰한 살림 하셨으면 좋겠습니다.
89. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
