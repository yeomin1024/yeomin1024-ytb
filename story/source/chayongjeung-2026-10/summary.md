# chayongjeung-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py story chayongjeung-2026-10` (2026-10-11 04:03). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **친구라서 차용증 없이 빌려준 3천만 원, 돌려받은 건 90만 원이었습니다. 정 때문에 돈 빌려준 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 120 / 자막 144, 길이 11:12 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–26 · 진행자 27–120 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/chayongjeung-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 친구라서 차용증 없이 빌려준 3천만 원, 돌려받은 건 90만 원이었습니다. 정 때문에 돈 빌려준 사람들의 공통점 `속마음·행동 · 금액→금액 · 공통점` 62자 — 짝 썸네일: thumbnail_1 (숫자 반전)
- [ ] **T2.** 연말까지 꼭 갚겠다는 카톡만 믿고 보낸 3천만 원… 차용증 없이 돈 빌려준 사람들이 모르는 불편한 진실 `계기 · 결과 숨김 · 불편한 진실` 57자 — 짝 썸네일: thumbnail_2 (인물·감정)
- [ ] **T3.** (짧은 변형, 금액 없음) 30년 우정이 돈 때문에 3년 만에 끝났습니다. 친구에게 돈 빌려준 사람들의 최악의 결말 `장면 · 기간→단절 · 최악의 결말` 49자 — 짝 썸네일: thumbnail_3 (대비)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (3,000만 원 → 90만 원)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 빌려준 돈과 돌려받은 돈의 **금액 차이(3,000만 원 → 90만 원)** 한 장면이 가장 클릭을 부른다 (주식 성공 썸네일 중 인물 없는 것은 모두 숫자 반전형 — 임시 근거)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1 | 차용증 없이 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (유일한 강조) |
| 2 | 3,000만 원 → 90만 원 | "3,000만 원"은 네이비 #14213D, "90만 원"은 흰색(파랑 #2D6CDF 상자) | "90만 원"이 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat clean graphic style on a plain cream (#F2EBDD) background, no decorations. At the top center, a small solid bright
yellow (#FFD400) box with black bold text "차용증 없이". In the center-left, a plain white paper money-transfer slip with
no bank name, no logo, no account number, no other writing, showing only the large dark navy bold text "3,000만 원".
A thick dark navy arrow points right to a solid blue (#2D6CDF) rounded box with a thin white border containing the huge
white bold text "90만 원", the largest element in the image. Keep all text inside the central 16:9 safe area, at least
48px from the edges. No people, no banknotes, no coins, no real money designs, no app screens.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (30년 친구였는데)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 30년 친구에게 돈을 떼인 **사연자의 허탈한 얼굴**이 숫자 카드보다 감정을 더 끈다 (주식 성공 썸네일 24개 중 약 20개가 얼굴 — 임시 근거)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1 | 30년 친구였는데 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (유일한 강조) |
| 2 | 90만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A dim dark navy-toned living room in the evening, soft warm lamp light. On the left 45% of the frame,
a fictional Korean woman around 50 years old, neat short hair, plain knit sweater, sitting at a dining table and holding a
smartphone in both hands, looking at it with a hollow, hurt, disappointed expression, as if betrayed by an old friend;
no tears, no anger. The phone screen shows only two simple blank message bubble shapes, no app interface, no logo, no text.
Fictional person, not resembling any real or famous person, natural Korean features. No other people in the scene.
On the right side, a solid bright yellow (#FFD400) box with large black bold text "30년 친구였는데". Below it, a wide solid
blue (#2D6CDF) rounded box with a thin white border containing the huge white bold text "90만 원", the largest element.
Keep the face and all text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (꼭 갚을게 / 축하금 아니었어?)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 돈을 빌릴 때 들은 말과 3년 뒤 들은 말의 **대비**가 숫자 없이도 문제 분석 첫 번째(빌려준 돈이라는 증명)를 한눈에 보여 준다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 연말까지 꼭 갚을게 | 잉크 #1E1E1E (흰 말풍선) | 말풍선 테두리 노랑 #FFD400 (유일한 강조) |
| 오른쪽 | 축하금 아니었어? | 흰색 (파랑 #2D6CDF 말풍선) | 오른쪽 글자를 조금 더 크게 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat clean graphic style, split screen with a clean vertical divider in the middle. Left half: bright cream (#F2EBDD)
background with one large white chat speech bubble outlined in thick bright yellow (#FFD400), containing black bold text
"연말까지 꼭 갚을게"; below it a small blank paper note with no writing. Right half: dark navy (#14213D) background with one
large solid blue (#2D6CDF) chat speech bubble containing slightly bigger white bold text "축하금 아니었어?".
Generic speech bubble shapes only: no phone interface, no messenger app design, no logos, no names, no profile pictures,
no people. Keep all text inside the central 16:9 safe area, at least 48px from the edges.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
30년 친구에게 차용증 없이 보낸 3천만 원 중 돌려받은 건 90만 원, 3년 뒤에는 축하금 아니었냐는 말까지 들었습니다.
빌려준 돈을 돌려받기 어려워지는 이유 3가지와, 차용증 쓰는 법부터 지급명령·소액사건까지 지금 할 수 있는 일 5가지를 정리했습니다.

■ 이 영상에서 다루는 것
- 차용증이 없으면 빌려준 돈이라는 걸 빌려준 사람이 증명해야 한다
- 받을 수 있는 기간(소멸시효)에는 끝이 있다: 개인 간 10년, 장사를 준비하려고 빌린 돈이면 5년일 수도 (2012년 대법원 판결)
- 독촉 메시지·내용증명만으로는 소멸시효가 멈추지 않는다
- 지금 할 수 있는 일 5가지: 차용증 쓰는 법, 이자 적기(연 20% 상한), 기록 모으기, 시효 날짜와 지급명령, 132 상담과 소액사건
- 돈을 빌려줘도 되는 기준 3가지

■ 챕터
0:00 사연: 차용증 없이 빌려준 3천만 원, 돌려받은 건 90만 원
2:06 왜 친구에게는 차용증을 안 쓸까
3:08 문제 01 빌려준 돈이라는 증명은 빌려준 사람 몫
4:05 문제 02 받을 수 있는 기간에는 끝이 있다
5:06 문제 03 독촉 카톡만으로는 시효가 멈추지 않는다
6:02 첫째: 빌려줄 땐 차용증 한 장
7:01 둘째: 이자는 받든 안 받든 글로
7:43 셋째: 이미 빌려줬다면 기록부터
8:28 넷째: 시효 날짜와 지급명령
9:34 다섯째: 132 상담과 소액사건
10:25 언제 빌려줘도 될까
10:53 정리

■ 사연에 대해
이 영상의 사연은 실제 법과 통계를 바탕으로 재구성한 이야기이며, 등장인물은 실존 인물이 아닙니다.

■ 출처
- 민법 제162조(소멸시효 10년)·제168조(승인)·제174조(독촉과 6개월)·제598조(소비대차), 국가법령정보센터: https://www.law.go.kr/법령/민법
- 상법 제64조(상거래 채권 소멸시효 5년), 국가법령정보센터: https://www.law.go.kr/법령/상법
- 이자제한법 제2조(최고이자율 연 20%), 국가법령정보센터: https://www.law.go.kr/법령/이자제한법
- 대법원 2012. 4. 13. 선고 2011다104246 판결(학원 준비 자금으로 빌린 돈, 5년 시효): https://www.nepla.ai/case/대법원/2011다104246
- 대법원 2019. 7. 25. 선고 2018다42538 판결(빌려준 사실은 주장하는 사람이 증명): https://www.nepla.ai/case/대법원/2018다42538
- 대법원 2015. 2. 12. 선고 2014다228440 판결(지급명령 신청 때 시효 중단): https://www.nepla.ai/case/대법원/2014다228440
- 법제처 찾기쉬운 생활법령정보 「금전거래 — 차용증 작성하기」: https://www.easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=272&ccfNo=2&cciNo=2&cnpClsNo=1
- 법제처 찾기쉬운 생활법령정보 「금전거래 — 채무불이행에 대한 대응」: https://www.easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=272&ccfNo=4&cciNo=1&cnpClsNo=1&menuType=qna
- 지급명령(민사소송법 제462조~제474조, 민사소송 등 인지법 제7조): https://korea.legal/wiki/%ec%a7%80%ea%b8%89%eb%aa%85%eb%a0%b9/
- 소액사건과 이행권고결정(소액사건심판법 제5조의3·제5조의4·제5조의7): https://korea.legal/wiki/%ec%9d%b4%ed%96%89%ea%b6%8c%ea%b3%a0%ea%b2%b0%ec%a0%95/
- 법원행정처 2025 사법연감(2024년 1심 민사 본안 80만 5,366건 중 소액사건 50만 7,804건), 법률신문: https://www.lawtimes.co.kr/news/211755
- 대한법률구조공단 법률구조 안내: https://klac.or.kr/legalstruct/legalRescueGuide.do?codeValue=INC003

■ 법률 자문이 아닙니다
이 영상의 사연은 실제 법과 통계를 바탕으로 재구성한 이야기이며, 등장인물은 실존 인물이 아닙니다.
이 영상은 법률 정보를 알려 드리기 위한 것이며, 법률 자문을 대신하지 않습니다.
같은 일이라도 사정마다 결과가 다르니, 실제 사건은 변호사나 대한법률구조공단(국번 없이 132)과 상담하세요.
영상 속 법 조문과 통계는 2026년 10월 기준이며, 출처는 설명란에 있습니다.

#인간관계 #차용증 #빌려준돈
```

**태그**: 돈 빌려주고 못받을때, 빌려준 돈 받는 법, 떼인 돈 받기, 친구 돈 빌려줌, 차용증, 차용증 없이 빌려준 돈, 대여금, 인간관계, 인생조언, 인생사연, 소멸시효, 지급명령, 소액소송, 대한법률구조공단

**고정 댓글**

```
가까운 사람에게 돈을 건네기 전에 이 두 가지만 확인해 보세요.
1. 못 받아도 내 생활이 흔들리지 않는 금액인지
2. 차용증 한 장 (이름·금액·빌려준 날·갚을 날·이자·서명)

가까운 사람에게 돈을 빌려줄 때, 차용증을 써 보신 적 있나요?
※ 개별 사건은 변호사나 대한법률구조공단(국번 없이 132)과 상담해 주세요. 댓글에 실명·연락처·계좌·주소는 쓰지 마세요.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 2021년 3월, 30년 지기 친구에게 3천만 원을 보냈어요.
2. 오랜 꿈이던 반찬가게를 여는데 상가 보증금이 모자란다고 했죠.
3. 그때 제 나이 마흔다섯, 딸 대학 등록금으로 모아 둔 돈이었어요.
4. 보내기 전날 친구한테서 카톡이 왔어요.
5. 연말까지 꼭 갚을게.
6. 30년 친구에게 차용증 얘기를 꺼내기가 너무 민망했어요.
7. 그래서 차용증도 없이, 이체 메모 칸도 비워 둔 채 보냈습니다.
8. 7월부터 석 달 동안은 매달 30만 원씩 돈이 들어왔어요.
9. 조금씩이라도 먼저 갚겠다는 메시지와 함께였죠.
10. 역시 내 친구구나, 괜한 걱정을 했구나 싶었어요.
11. 하지만 9월에 들어온 30만 원이 마지막이었습니다.
12. 그렇게 3천만 원 중에 제가 돌려받은 건 90만 원이 전부였어요.
13. 약속한 연말이 지나도 친구는 메시지를 읽기만 하고 답이 없었어요.
14. 2023년에는 손님이 줄어 가게가 문을 닫았다는 소식을 들었어요.
15. 2024년 봄, 조심스럽게 그 돈 얘기를 다시 꺼냈어요.
16. 그런데 친구가 이렇게 되묻더라고요.
17. 그거 개업 축하금 아니었어?
18. 빌려준 지 3년 만에, 그 말을 끝으로 연락이 끊겼습니다.
19. 올해 9월에 무료 법률 상담을 받으러 갔다가 더 놀랐어요.
20. 차용증이 없으니 빌려준 돈이라는 걸 제가 증명해야 한대요.
21. 가게 차릴 돈인 걸 알고 빌려줬으니 받을 수 있는 기간이 5년일 수도 있대요.
22. 보통은 10년인데, 5년이면 갚기로 한 2021년 말부터 올해 12월 말까지예요.
23. 그동안 보낸 독촉 카톡만으로는 그 시간이 멈추지 않는다고 했어요.
24. 30년 우정에 차용증 한 장 내밀기가 민망했을 뿐인데요.
25. 그 민망함의 값이 남은 돈 2,910만 원이 될 줄은 몰랐어요.
26. 딸 등록금은 결국 학자금 대출로 메웠고, 친구도 돈도 한꺼번에 잃었어요.

**진행자 파트** — 🎙 진행자

27. 가까운 사람이 돈을 빌려 달라고 하면 많은 분들이 이런 생각을 하시죠.
28. 30년 친구인데 설마 떼먹겠어.
29. 차용증을 내밀면 친구를 못 믿는 것 같잖아.
30. 카톡이랑 이체 내역이 있으니 언제든 받을 수 있겠지.
31. 이런 식으로 정을 믿고 넘긴 돈 문제는 결국 법원까지 가기도 합니다.
32. 법원이 해마다 펴내는 사법연감을 보면 그 규모가 보입니다.
33. 2024년 법원에 접수된 1심 민사 본안 사건은 80만 5천여 건이었습니다.
34. 그중 63%인 50만 7천여 건이 3천만 원 이하를 다투는 소액사건이었죠.
35. 법원까지 가는 민사 다툼의 절반 이상이 이렇게 크지 않은 돈 문제라는 뜻입니다.
36. 그럼 사연자가 왜 2,910만 원을 돌려받기 어려워졌는지 하나씩 짚어 보겠습니다.

> 🟨 [장면] 법률 자문이 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상의 사연은 실제 법과 통계를 바탕으로 재구성한 이야기이며, 등장인물은 실존 인물이 아닙니다.
> 이 영상은 법률 정보를 알려 드리기 위한 것이며, 법률 자문을 대신하지 않습니다.
> 같은 일이라도 사정마다 결과가 다르니, 실제 사건은 변호사나 대한법률구조공단(국번 없이 132)과 상담하세요.
> 영상 속 법 조문과 통계는 2026년 10월 기준이며, 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

37. 첫 번째 문제는 빌려준 돈이라는 걸 빌려준 사람이 증명해야 한다는 것입니다.
38. 돈을 빌려주는 약속은 차용증 없이 말로만 해도 계약으로 성립합니다.
39. 그런데 상대가 빌린 게 아니라고 다투기 시작하면 이야기가 달라집니다.
40. 대법원은 상대가 대여를 다투면, 빌려줬다는 쪽이 증명해야 한다고 봅니다.
41. 돈이 오간 사실이 분명해도 그게 빌려준 돈이었는지는 따로 보여 줘야 하는 거죠.
42. 계좌로 보낸 돈은 빌려준 돈일 수도, 선물이나 투자일 수도 있기 때문입니다.
43. 사연자가 메모 칸을 비워 둔 채 보낸 3천만 원도 마찬가지였습니다.
44. 친구가 개업 축하금이라고 말하는 순간, 사연자가 그 반대를 보여 줘야 하는 겁니다.
45. 차용증 한 장이 없다는 건, 증명의 짐을 빌려준 사람이 고스란히 진다는 뜻이죠.
46. 두 번째는 빌려준 돈을 받을 수 있는 기간에 끝이 있다는 것입니다.
47. 이 기간을 소멸시효라고 합니다.
48. 개인끼리 빌려준 돈은 갚기로 한 날부터 10년이 기준입니다.
49. 그런데 장사를 준비하려고 빌린 돈이라면 이 기간이 5년으로 줄어들 수 있습니다.
50. 상법은 상거래로 생긴 돈의 소멸시효를 5년으로 정하고 있기 때문이죠.
51. 2012년 대법원은 학원을 차릴 돈을 빌린 사건에서 이 문제를 다뤘습니다.
52. 빌린 사람은 학원 준비 자금으로 빌렸고, 빌려준 사람도 그걸 알고 있었습니다.
53. 대법원은 이 돈에도 상법을 적용해 소멸시효를 5년으로 봤습니다.
54. 사연자도 친구가 가게 보증금으로 쓸 걸 알고 3천만 원을 빌려줬습니다.
55. 그래서 10년이 아니라 올해 12월 말까지로 볼 여지가 생긴 겁니다.
56. 물론 누가 무슨 목적으로 빌렸는지에 따라 결론은 사건마다 달라집니다.
57. 세 번째는 독촉 메시지만으로는 이 시간이 멈추지 않는다는 것입니다.
58. 내용증명을 보내 독촉해도 그것만으로는 부족합니다.
59. 민법은 독촉한 뒤 6개월 안에 소송 같은 법원 절차를 밟아야 시효가 멈춘다고 정합니다.
60. 반대로 상대가 일부라도 갚거나 빚을 인정하면 시효는 그때부터 새로 시작됩니다.
61. 친구가 마지막으로 30만 원을 보낸 건 갚기로 한 연말보다 앞선 2021년 9월이었습니다.
62. 그 뒤로 친구는 빚을 인정하는 말을 한 번도 하지 않았죠.
63. 사연자가 2년 넘게 보낸 독촉 카톡은 시간을 멈추지 못했습니다.
64. 정에 기대 기다려 주는 동안에도 법이 정한 시계는 계속 가고 있었던 겁니다.
65. 그렇다면 가까운 사람에게 돈을 빌려줄 때, 그리고 이미 빌려줬을 때 무엇을 해야 할까요?

**올바른 방법 파트** — 🎙 진행자

66. 첫째, 빌려줄 때는 차용증 한 장을 꼭 남기세요.
67. 법제처 생활법령 안내도 말로 한 약속은 다툼이 생기면 풀기 어렵다고 설명합니다.
68. 차용증에는 빌려준 사람과 빌린 사람의 이름과 연락처를 적습니다.
69. 금액은 착오가 없도록 한글과 숫자로 나란히 씁니다.
70. 빌려준 날과 갚을 날, 갚는 방법도 정확히 적습니다.
71. 빌린 사람이 자기 이름과 주소를 직접 손으로 쓰고 서명하면 더 확실합니다.
72. 사연이라면 3천만 원, 빌려준 날 2021년 3월, 갚을 날 2021년 12월 31일.
73. 이 몇 줄이면 충분했습니다.
74. 이런 종이가 있었다면 개업 축하금이라는 말은 나오기 어려웠을 겁니다.
75. 돈을 보낼 때는 이체 메모 칸에 대여금이라고 적어 두세요.
76. 차용증은 친구를 의심하는 서류가 아니라, 그날의 약속을 함께 적어 두는 종이입니다.
77. 둘째, 이자는 받든 안 받든 차용증에 적어 두세요.
78. 이자를 따로 정하지 않으면 빌려준 기간의 이자는 청구할 수 없습니다.
79. 이자를 받기로 했다면 지금은 연 20%가 상한입니다.
80. 2021년 7월 7일 이후 맺은 계약부터 적용되는 기준이죠.
81. 20%를 넘게 약속해도 넘는 부분은 효력이 없습니다.
82. 예를 들어 3천만 원에 연 5%로 정하면 1년 이자는 150만 원입니다.
83. 이자를 받지 않을 거라면 이자 없음이라고 분명히 적으면 됩니다.
84. 그래야 나중에 이자 문제로 서로 얼굴 붉힐 일이 줄어듭니다.
85. 셋째, 이미 차용증 없이 빌려줬다면 지금 남아 있는 기록부터 모으세요.
86. 생활법령 안내도 차용증이 없으면 계좌 거래 내역 같은 자료로 대신할 수 있다고 합니다.
87. 빌려 달라고 한 메시지와 갚겠다고 약속한 메시지가 가장 먼저입니다.
88. 상대가 조금이라도 갚은 이체 기록도 중요합니다.
89. 사연자에게는 연말까지 꼭 갚겠다는 카톡이 있었죠.
90. 30만 원씩 세 번, 조금씩 먼저 갚겠다며 들어온 입금 기록도 있었고요.
91. 이 기록들은 축하금이 아니라 빌려준 돈이라는 걸 보여 주는 데 도움이 될 수 있습니다.
92. 휴대폰을 바꾸면 대화가 사라질 수 있으니 캡처하고 백업해 두세요.
93. 넷째, 갚기로 한 날이 지나면 시효가 끝나는 날을 달력에 적어 두세요.
94. 사연이라면 갚기로 한 날이 2021년 12월 31일입니다.
95. 5년으로 보면 2026년 12월 말, 10년으로 보면 2031년 12월 말이죠.
96. 날짜가 다가오는데 연락이 없다면 법원의 지급명령을 생각해 볼 수 있습니다.
97. 지급명령은 법원이 상대를 부르지 않고 서류만 보고 갚으라고 명령하는 절차입니다.
98. 법원에 내는 인지대는 소송의 10분의 1이라, 2,910만 원이면 1만 원대입니다.
99. 상대가 받은 날부터 2주 안에 이의하지 않으면 판결을 받은 것과 같은 효력이 생깁니다.
100. 이의하면 소송으로 넘어가지만, 시효는 지급명령을 신청한 날 멈춘 것으로 봅니다.
101. 다만 상대 주소를 모르면 지급명령 대신 소송으로 가야 할 수 있습니다.
102. 독촉 내용증명을 보냈다면 6개월 안에 이런 절차를 밟아야 한다는 것도 기억하세요.
103. 다섯째, 혼자 하기 어렵다면 무료 법률 상담부터 받으세요.
104. 대한법률구조공단은 국번 없이 132로 전화 상담을 받습니다.
105. 법률 상담은 소득과 상관없이 무료입니다.
106. 기준 중위소득 125% 이하라면 공단 심사를 거쳐 소송 지원을 받을 수도 있습니다.
107. 상대가 빌린 적 없다고 다투면 결국 법원에서 따져야 합니다.
108. 3천만 원 이하를 청구하는 소송은 소액사건이라 절차가 비교적 간단합니다.
109. 법원이 먼저 갚으라는 이행권고결정을 보낼 수 있습니다.
110. 상대가 2주 안에 이의하지 않으면 이 결정도 판결과 같은 효력이 생깁니다.
111. 사연자가 청구할 2,910만 원도 소액사건 기준인 3천만 원 안에 들어갑니다.
112. 그렇다고 돈을 빌려주는 것 자체가 잘못은 아닙니다.
113. 못 받아도 내 생활이 흔들리지 않는 금액까지만 빌려주세요.
114. 등록금이나 생활비처럼 쓸 곳이 정해진 돈은 빌려주지 않는 게 좋습니다.
115. 그래도 빌려준다면 차용증 한 장, 이 세 가지면 우정도 돈도 지키기 쉬워집니다.
116. 더 큰돈이 필요하다고 하면, 도와주고 싶은 만큼만 정해서 건네는 것도 방법입니다.

**마무리** — 🎙 진행자

117. 이렇게 해서 차용증 없이 빌려준 돈이 왜 돌려받기 어려운지 알아보았습니다.
118. 돈을 건네기 전에 못 받아도 괜찮은 금액인지, 차용증은 남겼는지 확인하세요.
119. 소중한 관계도, 소중한 돈도 지키셨으면 좋겠습니다.
120. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
