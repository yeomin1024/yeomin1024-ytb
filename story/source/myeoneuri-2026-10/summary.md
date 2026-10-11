# myeoneuri-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py story myeoneuri-2026-10` (2026-10-11 07:39). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **아버님 말씀만 믿고 8년을 모셨는데 며느리 몫은 0원이었습니다. 시부모 간병한 며느리들이 모르는 불편한 진실**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 132 / 자막 164, 길이 12:13 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–20 · 진행자 21–132 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/myeoneuri-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 아버님 말씀만 믿고 8년을 모셨는데 며느리 몫은 0원이었습니다. 시부모 간병한 며느리들이 모르는 불편한 진실 `속마음 · 기간→0원 · 불편한 진실` 60자 — 짝 썸네일: thumbnail_1 (8년 간병 → 0원)
- [ ] **T2.** (말줄임 변형) 이 집은 너희 내외 몫이라는 손글씨 한 장 믿고 8년을 모셨는데… 시부모 모신 며느리들이 마지막에 꼭 하는 후회 `장면 · 기간→결과 숨김 · 마지막에 꼭 하는 후회` 62자 — 짝 썸네일: thumbnail_2 (메모를 든 사연자)
- [ ] **T3.** (짧은 변형, 금액 없음) 8년 모신 시아버지 집에 제 몫은 없었습니다. 시부모 간병한 며느리들의 공통점 `행동 · 기간→없음 · 공통점` 43자 — 짝 썸네일: thumbnail_3 (그때 들은 말 / 결과 대비)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (8년 간병 → 0원)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 간병 기간(8년)이 결과 0원으로 뒤집힌 **숫자 반전**이 인물 없이도 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 시작 | 8년 간병 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (유일한 강조) |
| 결과 | 0원 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat graphic design on a cream (#F2EBDD) background with a faint paper texture. On the left, a solid bright yellow
(#FFD400) rectangle containing the large black bold text "8년 간병". In the middle, one thick ink-black arrow pointing right.
On the right, a large solid blue (#2D6CDF) rounded box containing the huge white bold text "0원", the biggest element,
about 30% of the image height. At the bottom center, a small prop: one old torn-off calendar sheet seen from the back,
with faint illegible handwritten pen strokes only (no readable words, not a legal form). No people, no money bills,
no buildings, no gavel. Keep all text inside the central 16:9 safe area, at least 48px from the edges.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (메모를 든 사연자)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 손글씨 메모를 든 채 빈 집에 선 **사연자의 허탈한 표정**이 숫자 카드보다 감정을 더 끈다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1 | 8년 모셨는데 | 잉크 #1E1E1E | 노랑 띠 #FFD400 (글자 전체 높이, 유일한 강조) |
| 2 | 제 몫은 0원 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A half-empty Korean apartment living room in soft afternoon light, a few taped cardboard moving
boxes on the floor, pale marks where furniture used to be. On the left 45% of the frame, a fictional Korean woman in her
mid 50s wearing a plain cardigan, holding one old calendar sheet in both hands and looking down at it with a hollow,
quietly hurt expression (no tears). Fictional person, not resembling any real or famous person, natural Korean features.
On the wall behind her, a small framed photo showing only a blurred silhouette of an elderly man, face not recognizable.
The calendar sheet shows only faint illegible handwriting strokes. On the right side, a full-height bright yellow (#FFD400)
band containing the black bold text "8년 모셨는데", and below it a solid blue (#2D6CDF) rounded box containing
the huge white bold text "제 몫은 0원", the largest element. No romance, no funeral, no court, no gavel, no legal form.
Keep the face and all text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (그때 들은 말 / 결과)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 그때 들은 약속("이 집은 너희 내외 몫")과 결과(며느리 몫 0원)를 **나란히 놓은 대비**가 "왜?"라는 궁금증을 가장 크게 만든다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 말풍선 | 이 집은 너희 내외 몫 | 잉크 #1E1E1E (흰 말풍선) | 말풍선 테두리 노랑 #FFD400 (유일한 강조) |
| 오른쪽 결과 | 며느리 몫 0원 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Split-screen composition divided vertically by a thin white line. LEFT HALF: a warm, sunlit Korean living room in cream
and soft orange tones with one empty old armchair (no person visible). Above the armchair, a white speech bubble with a
thick bright yellow (#FFD400) outline containing the black bold text "이 집은 너희 내외 몫". RIGHT HALF: a cold dark-navy
(#14213D) toned empty room with a single cardboard moving box on the floor, and in the center a large solid blue (#2D6CDF)
rounded box containing the huge white bold text "며느리 몫 0원", the largest element. No people, no court, no gavel,
no legal document, no money bills. Keep all text inside the central 16:9 safe area, at least 48px from the edges.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
8년을 모신 시아버지의 집, 상속이 시작되자 며느리 몫은 0원이었습니다.
며느리는 왜 상속인이 아닌지, 부모님을 모시는 가족이 지금 남겨야 할 기록과 서류를 정리했습니다.

■ 이 영상에서 다루는 것
- 며느리는 법적으로 상속인이 아니다 (상속 순서, 대습상속, 기여분은 상속인만 청구)
- 손글씨 메모는 방식 하나만 어긋나도 유언으로 인정받기 어렵다 (자필 유언의 요건, 2014년 대법원 판결)
- 오래 모셨다는 사실만으로는 더 받기 어렵다 (2019년 대법원 전원합의체 결정, 2023년 간병비 월평균 370만 원)
- 상속 다툼은 늘고, 한번 찍은 도장은 되돌리기 어렵다 (상속재산 분할 사건 2014년 771건 → 2022년 2,776건)
- 모시는 가족이 남길 것 5가지: 형제와의 약속을 글로, 하루 한 줄 간병 기록, 법이 정한 방식의 유언, 바뀐 유류분 법, 도장 찍기 전 상담

■ 챕터
0:00 사연: 8년 모신 시아버지 집, 며느리 몫은 0원
1:43 모시는 가족이 흔히 하는 생각
2:47 문제 01 며느리는 상속인이 아니다
3:47 문제 02 손글씨 메모는 유언이 아니었다
4:45 문제 03 오래 모신 것만으로는 부족하다
6:20 문제 04 한번 찍은 도장은 되돌리기 어렵다
7:13 방법 첫째: 형제와의 약속을 글로
8:03 방법 둘째: 간병은 하루 한 줄 기록
8:46 방법 셋째: 부모님 뜻은 법이 정한 유언으로
9:56 방법 넷째: 바뀐 유류분 법 알기
10:53 방법 다섯째: 도장 찍기 전에 상담
11:35 정리

■ 사연에 대해
이 영상의 사연은 실제 법과 통계를 바탕으로 재구성한 이야기이며, 등장인물은 실존 인물이 아닙니다.
사연 속 금액(아파트와 예금 3억 7,500만 원, 1인 1억 2,500만 원, 월 30만 원 분담 예시)은 이해를 돕기 위한 예시입니다.

■ 출처
- 민법(상속 순위 제1000조·대습상속 제1001조·배우자 제1003조·기여분 제1008조의2·법정상속분 제1009조·유언 방식 제1060조·제1066조·제1068조·증인 결격 제1072조·부양 순위와 방법 제976조·제977조), 국가법령정보센터: https://www.law.go.kr/법령/민법
- 대법원 2019. 11. 21.자 2014스44, 45 전원합의체 결정(배우자 간호와 기여분): https://www.scourt.go.kr/sjudge/1574324747351_172547.pdf
- 대법원 2014. 9. 26. 선고 2012다71688 판결(주소를 자서하지 않은 자필 유언): 대법원 종합법률정보 https://glaw.scourt.go.kr 에서 사건번호로 검색
- 헌법재판소 2024. 4. 25. 2020헌가4 등 결정(유류분 위헌·헌법불합치): 헌법재판소 https://www.ccourt.go.kr 에서 사건번호로 검색
- 유류분 민법 개정안 국회 통과(2026년, 헌재 결정 반영): https://www.heraldk.com/article/2026021202000020185
- 2024년 사회조사(통계청, 부모 노후는 가족이 돌봐야 18.2%): https://biz.sbs.co.kr/amp/article/20000201265
- 한국은행 BOK 이슈노트(2024. 3. 5., 2023년 간병비 월평균 370만 원): https://biz.sbs.co.kr/amp/article/20000159971
- 상속재산 분할 사건 접수(대법원 사법연감 인용): https://www.mt.co.kr/economy/2026/02/14/2026021404250543644

■ 법률 자문이 아닙니다
이 영상의 사연은 실제 법과 통계를 바탕으로 재구성한 이야기이며, 등장인물은 실존 인물이 아닙니다.
이 영상은 법률 정보를 알려 드리기 위한 것이며, 법률 자문을 대신하지 않습니다.
같은 일이라도 사정마다 결과가 다르니, 실제 사건은 변호사나 대한법률구조공단(국번 없이 132)과 상담하세요.
영상 속 법 조문과 통계는 2026년 10월 기준이며, 출처는 설명란에 있습니다.

#노후사연 #상속 #며느리
```

**태그**: 시아버지 며느리 사연, 며느리 상속, 노후사연, 시니어사연, 인생사연, 유산상속 분쟁, 형제간 재산 다툼, 상속, 상속재산 분할, 자필 유언장, 유언 공증, 기여분, 유류분, 간병

**고정 댓글**

```
부모님을 모시고 있다면 이 두 가지부터 챙겨 보세요.
1. 형제와 나눈 약속(누가 모시고, 매달 얼마를 보탤지)은 글로 남기기
2. 간병은 하루 한 줄 기록과 영수증으로 남기기

부모님을 모시면서 형제와 약속을 글로 남겨 두신 적 있나요?
※ 개별 사건은 변호사나 대한법률구조공단(국번 없이 132)과 상담해 주세요. 댓글에 실명·연락처·계좌·주소는 쓰지 마세요.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 2017년 3월, 혼자 사시던 시아버지가 뇌경색으로 쓰러지셨어요.
2. 오른쪽 몸이 마비돼 혼자서는 화장실도 못 가시게 됐죠.
3. 요양병원은 싫다며 우시는 아버님을 두고 볼 수 없었어요.
4. 저희 부부는 살던 전셋집을 빼고 아버님 댁으로 들어갔어요.
5. 그때 제 나이 마흔일곱이었어요.
6. 아버님은 이 집은 너희 내외 몫이라고 여러 번 말씀하셨죠.
7. 2022년 설날에는 그 말을 달력 뒷장에 직접 써 주셨고요.
8. 그 종이 한 장으로 8년을 버텼어요.
9. 하지만 그 종이는 아무것도 지켜 주지 못했습니다.
10. 2025년 3월 아버님이 돌아가시고 한 달 뒤, 시누이가 법대로 나누자고 했어요.
11. 아파트와 예금을 합친 3억 7,500만 원, 남편 몫은 1억 2,500만 원이었어요.
12. 8년을 모신 제 몫은 0원이었고요.
13. 명절에만 다녀가던 시누이와 시동생도 똑같이 1억 2,500만 원씩이었죠.
14. 알고 보니 며느리는 처음부터 상속인이 아니었어요.
15. 아버님 메모에는 날짜와 이름은 있었지만, 주소도 도장도 없었어요.
16. 그래서 유언으로 인정받기 어렵다는 말을 들었고요.
17. 남편이 모신 걸로라도 인정받아 보려 했지만, 8년 동안 남긴 기록이 하나도 없었어요.
18. 결국 그해 여름 남편은 협의서에 도장을 찍었고, 가을에 그 집을 팔고 나왔죠.
19. 기저귀를 갈아 드린 8년이 서류 위에서는 아무 숫자도 아니었어요.
20. 아버님 말씀만 믿고 기록 한 줄 남기지 않은 제가 너무 어리석었어요.

**진행자 파트** — 🎙 진행자

21. 부모님을 모시게 될 때 많은 분들이 이런 생각을 하죠.
22. 가족끼리 무슨 서류까지 써.
23. 모신 사람이 더 받는 게 당연하지.
24. 아버님이 직접 써 주셨으니 그걸로 됐겠지.
25. 이런 식으로 정과 말에 기대다 보면, 법이 보는 증거는 남지 않게 됩니다.
26. 2024년 통계청 사회조사에서 부모 노후를 가족이 돌봐야 한다는 응답은 18.2%였습니다.
27. 10년 전 31.7%에서 절반 가까이 줄어든 숫자죠.
28. 부양을 가족 모두의 몫으로 보는 생각이 그만큼 옅어지고 있다는 뜻입니다.
29. 그럴수록 한 사람이 떠안은 간병은 그 사람의 선택으로만 여겨질 수 있습니다.
30. 사연 속 이야기가 결코 남의 일이 아닌 이유입니다.
31. 그럼 사연자가 왜 8년을 모시고도 아무것도 받지 못했는지 하나씩 짚어 보겠습니다.

> 🟨 [장면] 법률 자문이 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상의 사연은 실제 법과 통계를 바탕으로 재구성한 이야기이며, 등장인물은 실존 인물이 아닙니다.
> 이 영상은 법률 정보를 알려 드리기 위한 것이며, 법률 자문을 대신하지 않습니다.
> 같은 일이라도 사정마다 결과가 다르니, 실제 사건은 변호사나 대한법률구조공단(국번 없이 132)과 상담하세요.
> 영상 속 법 조문과 통계는 2026년 10월 기준이며, 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

32. 첫 번째 문제는 며느리는 법적으로 상속인이 아니라는 것입니다.
33. 민법이 정한 상속 순서는 자녀와 손주, 부모, 형제자매, 4촌 이내 혈족입니다.
34. 여기에 돌아가신 분의 배우자가 함께 상속인이 되죠.
35. 아들의 아내인 며느리는 이 순서 어디에도 없습니다.
36. 며느리가 상속인이 되는 건 주로 남편이 시부모님보다 먼저 세상을 떠난 경우입니다.
37. 그때는 먼저 간 남편의 자리를 이어받는데, 이것을 대습상속이라고 합니다.
38. 사연자의 남편은 살아 있었으니, 상속인은 아버님의 자녀 세 명이었습니다.
39. 같은 순위의 상속인은 똑같이 나누기 때문에 한 사람 몫이 1억 2,500만 원이 된 거죠.
40. 더 부양한 사람이 더 받게 하는 기여분 제도도 있지만, 상속인만 청구할 수 있습니다.
41. 8년을 모신 며느리 본인은 더 달라고 청구할 자격조차 없었던 겁니다.
42. 두 번째는 그렇다면 아버님이 직접 쓰신 메모는 왜 소용이 없었느냐는 것입니다.
43. 민법은 법이 정한 방식을 따르지 않은 유언은 효력이 없다고 정해 두었습니다.
44. 손으로 쓰는 자필 유언이라면 내용 전부와 날짜, 주소, 이름을 직접 써야 합니다.
45. 그리고 도장까지 찍어야 하죠.
46. 법원은 이 방식을 엄격하게 봅니다.
47. 2014년 대법원은 주소를 제대로 적지 않은 자필 유언장을 무효로 봤습니다.
48. 누가 쓴 유언인지 분명하더라도 방식을 지키지 않았다는 이유였죠.
49. 사연자의 메모에는 날짜와 이름은 있었지만, 주소도 도장도 없었습니다.
50. 유언이 아닌 다른 약속으로라도 인정받으려면 소송에서 따로 다퉈야 합니다.
51. 그 결과도 장담하기 어렵습니다.
52. 아버님이 직접 써 주셨으니 됐다는 믿음이 여기서 무너진 거죠.
53. 세 번째는 오래 모셨다는 사실만으로는 더 받기 어렵다는 것입니다.
54. 기여분은 상속인이 돌아가신 분을 특별히 부양했을 때 인정됩니다.
55. 재산을 지키거나 늘리는 데 특별히 기여했을 때도 마찬가지고요.
56. 2019년 대법원은 약 5년 동안 아픈 남편 곁을 지킨 아내의 사건을 판단했습니다.
57. 남편이 통원과 입원 치료를 받는 동안 곁에서 간호한 아내였죠.
58. 아내는 그 간호를 이유로 상속을 30% 더 인정해 달라고 했습니다.
59. 대법원은 오래 간호했다는 사실만으로는 부족하다고 봤습니다.
60. 간호한 기간과 방법, 정도, 그리고 비용을 누가 부담했는지까지 따져야 한다는 거였죠.
61. 결국 아내의 청구는 받아들여지지 않았습니다.
62. 물론 배우자의 간호였던 사건이고, 반대 의견을 낸 대법관도 있었습니다.
63. 법원이 따지는 건 얼마나, 어떻게 모셨는지를 보여 주는 증거라는 뜻입니다.
64. 며느리의 간병을 상속인인 남편의 기여로 주장해 볼 여지는 있습니다.
65. 하지만 그때도 간병일지나 병원비 내역 같은 증거가 있어야 합니다.
66. 간병의 값은 결코 작지 않습니다.
67. 한국은행은 2023년 간병인을 쓰는 비용이 한 달 평균 370만 원이라고 분석했습니다.
68. 65세 이상 가구 중간 소득의 1.7배나 되는 돈이죠.
69. 그런데 기록하지 않은 간병은 법원에서 숫자로 남지 않습니다.
70. 네 번째는 상속 다툼은 늘고 있는데, 한번 찍은 도장은 되돌리기 어렵다는 것입니다.
71. 법원에 온 상속재산 분할 사건은 2014년 771건에서 2022년 2,776건이 됐습니다.
72. 그사이 3.6배가 된 거죠.
73. 형제끼리 상속을 두고 법원까지 가는 일이 이제 드물지 않다는 뜻입니다.
74. 그런데 기여분은 상속재산을 나누는 협의나 법원 심판 때 함께 주장해야 합니다.
75. 협의서에 도장을 찍어 나누기를 마치면, 기여분만 따로 청구하기는 어렵습니다.
76. 사연자의 남편도 장례 넉 달 만에 협의서에 도장을 찍었죠.
77. 슬픔이 가시기도 전에 내린 결정이 8년을 정리해 버린 셈입니다.
78. 그렇다면 부모님을 모시는 가족은 무엇을 남겨야 할까요?

**올바른 방법 파트** — 🎙 진행자

79. 첫째, 부모님을 모시기 전에 형제와 나눈 약속을 글로 남기세요.
80. 누가 모실지, 다른 형제가 매달 얼마를 보탤지, 집은 어떻게 할지를 적는 겁니다.
81. 민법도 부양할 자녀가 여럿이면 누가 어떻게 부양할지를 먼저 당사자끼리 정하게 합니다.
82. 정하지 못하면 그때 법원이 정하게 되어 있죠.
83. 시누이와 시동생이 매달 30만 원씩만 보탰어도, 8년이면 한 사람당 2,880만 원입니다.
84. 이 글은 상속을 미리 나누는 문서가 아닙니다.
85. 누가 얼마나 부양했는지를 보여 주는 증거가 되는 거죠.
86. 가족끼리 무슨 서류냐는 생각이 들 수도 있습니다.
87. 하지만 서류는 의심이 아니라, 사이가 좋을 때의 약속을 남기는 일입니다.
88. 둘째, 간병은 하루 한 줄이라도 기록으로 남기세요.
89. 날짜와 그날 한 일, 병원에 모시고 간 날을 간병일지에 적는 겁니다.
90. 약값과 기저귀값, 병원비 영수증도 모아 두시고요.
91. 간병 비용은 되도록 상속인인 남편 이름으로 내고, 그 내역을 남겨 두세요.
92. 법원이 간병의 기간과 방법, 비용을 누가 냈는지를 본다는 걸 떠올려 보시면 됩니다.
93. 사연자가 모신 8년은 2,900일이 넘습니다.
94. 하루 한 줄이면 2,900줄이 넘는 증거가 되는 셈이죠.
95. 날짜가 찍힌 사진이나 가족 대화방에 남긴 간병 소식도 기록이 될 수 있습니다.
96. 셋째, 부모님의 뜻은 판단력이 있으실 때 법이 정한 방식의 유언으로 남기시게 하세요.
97. 자필로 쓰신다면 내용과 날짜, 주소, 이름을 모두 손으로 쓰고 도장을 찍으셔야 합니다.
98. 더 안전한 방법은 공증인 앞에서 하는 공정증서 유언입니다.
99. 증인 두 명이 함께한 자리에서 부모님이 유언 내용을 말로 전하시는 방식이죠.
100. 공증인이 이를 받아 적어 읽어 드리고, 부모님과 증인이 확인한 뒤 서명합니다.
101. 이때 유언으로 재산을 받을 사람은 증인이 될 수 없습니다.
102. 그 배우자와 자녀, 부모 같은 직계 가족도 마찬가지입니다.
103. 아버님이 큰아들에게 집을 남기셨다면, 큰아들 부부는 증인이 될 수 없는 거죠.
104. 아버님 메모에 주소 한 줄과 도장만 있었어도 결과는 달라졌을 수 있습니다.
105. 다만 유언이 있어도 다른 자녀에게는 유류분이 남을 수 있습니다.
106. 법이 자녀에게 보장하는 최소한의 몫이죠.
107. 그래서 유언을 준비할 때는 변호사 같은 전문가와 함께 살펴보는 게 좋습니다.
108. 넷째, 최근 바뀐 법도 알아 두세요.
109. 2024년 4월 헌법재판소는 유류분 제도의 일부가 헌법에 맞지 않는다고 결정했습니다.
110. 특별히 부양한 상속인의 기여를 유류분 계산에 반영하지 않는 부분도 그중 하나였죠.
111. 이 결정에 따라 올해 국회를 통과한 개정 민법에는 달라진 점이 있습니다.
112. 바로 특별히 부양하거나 재산에 기여한 상속인에 대한 부분입니다.
113. 그 보상으로 받은 증여는 유류분 반환 대상에서 빠질 수 있게 된 겁니다.
114. 아버님이 8년 간병의 보답이라며 큰아들에게 집을 미리 넘기셨다면 어땠을까요?
115. 그랬다면 동생들이 유류분으로 돌려 달라고 하기는 예전보다 어려워졌을 수 있습니다.
116. 물론 무엇이 보상으로 인정될지는 사정마다 다릅니다.
117. 그 보상을 뒷받침하는 것도 결국 간병의 기록입니다.
118. 다섯째, 상속이 시작되면 협의서에 도장을 찍기 전에 먼저 상담을 받으세요.
119. 협의 자리에서 먼저 간병한 몫을 이야기해 보세요.
120. 합의가 되지 않으면 가정법원에 분할 심판과 함께 기여분을 청구할 수 있습니다.
121. 사연자 부부처럼 슬픔 속에서 서두르면, 주장할 기회 자체를 놓칠 수 있습니다.
122. 국번 없이 132, 대한법률구조공단이나 변호사와 먼저 상담하세요.
123. 상담하러 갈 때는 간병일지와 영수증, 형제와 나눈 약속을 적은 종이를 함께 챙기시고요.
124. 기록이 있어야 전문가도 도울 수 있는 게 많아집니다.
125. 부모님을 모시는 선택 자체는 정말 귀한 일입니다.
126. 형제와의 약속은 글로, 간병은 기록으로, 부모님의 뜻은 유언으로 남기는 것.
127. 이 세 가지를 갖춘 뒤라면 마음 놓고 정성을 다하셔도 됩니다.

**마무리** — 🎙 진행자

128. 이렇게 해서 8년을 모신 며느리가 빈손이 된 이유를 알아보았습니다.
129. 그리고 부모님을 모시는 가족이 미리 남겨야 할 것들도 살펴봤죠.
130. 부모님을 모시기로 했다면, 오늘부터 하루 한 줄 기록부터 시작해 보세요.
131. 소중한 관계도, 소중한 돈도 지키셨으면 좋겠습니다.
132. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
