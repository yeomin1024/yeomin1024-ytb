# prediabetes-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py health prediabetes-2026-10` (2026-10-11 03:55). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **공복혈당 108 '경계'라 괜찮다고 넘겼다가 3년 만에 당뇨가 됐습니다. 검진 결과지 대충 본 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 94 / 자막 117, 길이 9:03 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–13 · 진행자 14–94 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/prediabetes-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 공복혈당 108 '경계'라 괜찮다고 넘겼다가 3년 만에 당뇨가 됐습니다. 검진 결과지 대충 본 사람들의 공통점 `속마음 · 경계→당뇨 · 공통점` 61자 — 짝 썸네일: thumbnail_1
- [ ] **T2.** 아픈 데 없다며 넘긴 공복혈당 108이 3년 만에 131이 됐습니다. 당뇨 전단계 무시한 사람들의 후회 `증상 없음 · 108→131 · 후회("마지막에 꼭 하는 후회"를 줄여 씀)` 57자 — 짝 썸네일: thumbnail_2
- [ ] **T3.** (짧은 변형) 공복혈당 108을 3년 무시했더니 131, 당뇨가 됐습니다. 당뇨 전단계의 불편한 진실 `행동 · 108→131 · 불편한 진실` 48자 — 짝 썸네일: thumbnail_3

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 결과지 숫자 반전

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 결과지 숫자가 '경계'에서 '당뇨'로 뒤집힌 장면이 가장 빨리 읽힌다 (주식의 계좌 숫자 반전과 같은 축)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 처음 | 108 | 잉크 #1E1E1E | 중간 크기 |
| 판정 | 경계 | 검정 글자 | 노랑 #FFD400 상자 (글자 전체 높이) |
| 기간 | 3년 | 잉크 | 작게, 화살표 위 |
| 결과 | 131 | 빨강 #E63B2E | 가장 큰 글자 |
| 판정 | 당뇨 | 흰 글자 | 빨강 상자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat illustration on a cream background. Two simple white medical checkup result sheets overlap in the center,
with no logos, no institution names, no barcodes, no personal data, no small print. On the smaller sheet at the back left,
the number "108" in black, next to a solid bright yellow (#FFD400) box with black text "경계". A thick black arrow points
from left to right, with the small black text "3년" above the arrow. On the larger sheet in front on the right, the huge
red (#E63B2E) number "131" as the largest element, with a solid red box below it containing white bold text "당뇨".
No people, no needles, no blood, no hospital scenes.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 결과지를 든 **사람의 표정**이 숫자 카드보다 감정을 더 끈다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 속마음 | 멀쩡했는데 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이) |
| 결과 | 131 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Softly blurred bright office background in warm cream tones. On the left 40% of the frame, a
fictional Korean man in his early 50s, office-worker look (white shirt, loosened tie), holding a single health checkup
result sheet with both hands, the sheet facing away or blurred so no text is readable, surprised and worried expression
looking at the paper. Fictional person, not resembling any real or famous person, natural Korean features. Not a doctor,
no white coat, no hospital, no needles. On the right side, large bold headline text "멀쩡했는데" in ink black on a solid bright
yellow (#FFD400) box. Below it, a wide solid red (#E63B2E) rounded box containing
the huge white bold number "131", the largest element. No crying, no extreme fear.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (기대 vs 결과)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: "괜찮겠지"라는 기대와 결과를 나란히 놓으면 공감이 빠르다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 숫자 | 108 | 잉크 | 큼 |
| 왼쪽 말 | 괜찮겠지 | 검정 글자 | 노랑 상자 |
| 오른쪽 숫자 | 131 | 흰 글자 (빨강 상자) | 가장 큼 |
| 오른쪽 말 | 당뇨 | 흰 글자 #F7F3EA | 중간 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat graphic design split vertically in two halves with a torn-paper edge in the middle. Left half: cream background with
the large ink-black number "108" and below it the Korean word "괜찮겠지" in black on a solid bright yellow (#FFD400) box.
Right half: dark navy (#14213D) background with a solid red (#E63B2E) rounded box containing the huge white bold number
"131", the largest element, and below it the Korean word "당뇨" in off-white. No people, no medical scenes, no logos.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
건강검진 결과지의 공복혈당 108, '공복혈당장애 의심'을 괜찮다고 넘겼더니 3년 뒤 131, 당뇨병 진단을 받았습니다.
'경계' 판정을 그냥 넘기면 왜 위험한지 4가지로, 당뇨병 전단계에서 할 수 있는 일을 6가지로 정리했습니다.

■ 이 영상에서 다루는 것
- 당뇨병 전단계는 왜 증상이 없을까
- 같은 '경계'라도 숫자는 움직인다 (공복혈당장애의 1년 진행 위험)
- 검진 결과지가 진료로 이어지지 않는 이유
- 당뇨병 전단계에서 할 수 있는 6가지 (결과지 숫자 확인, 당화혈색소, 체중 5~7%, 주 150분과 식후 걷기, 먹는 순서, 정상 숫자로 돌아가기)

■ 챕터
0:00 사연: 공복혈당 108이 3년 만에 당뇨로
1:06 왜 '경계'를 그냥 넘길까
2:00 문제 01 당뇨병 전단계는 증상이 없다
2:34 문제 02 '경계'는 멈춰 있지 않다
3:07 문제 03 결과지가 다음 단계로 안 이어진다
3:44 문제 04 당뇨병이 되면 관리가 어렵다
4:27 첫째: 결과지의 공복혈당 숫자부터
4:56 둘째: 1년 기다리지 말고 상담·당화혈색소
5:36 셋째: 몸무게 5~7% 줄이기
6:27 넷째: 주 150분, 식후 바로 앉지 않기
7:11 다섯째: 채소·단백질 먼저, 밥은 나중에
7:51 여섯째: 정상 숫자로 돌아가기를 목표로
8:41 정리

■ 사연에 대해
이 영상의 사연은 실제 진단 기준과 통계를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 수치는 이해를 돕기 위한 예시입니다.

■ 출처
- 질병관리청 국가건강정보포털 「당뇨병」: https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=5305
- 대한당뇨병학회 Diabetes Fact Sheets in Korea 2024: https://www.e-dmj.org/journal/view.php?doi=10.4093/dmj.2024.0818
- 일반건강검진 결과통보서 서식(국가법령정보센터): https://www.law.go.kr/flDownload.do?flSeq=148392279&flNm=%5B%EB%B3%84%EC%A7%80+6%5D+%EC%9D%BC%EB%B0%98%EA%B1%B4%EA%B0%95%EA%B2%80%EC%A7%84+%EA%B2%B0%EA%B3%BC%ED%86%B5%EB%B3%B4%EC%84%9C&bylClsCd=200203
- 미국 질병통제예방센터(CDC) 당뇨병 전단계: https://www.cdc.gov/diabetes/communication-resources/prediabetes-statistics.html
- 보건복지부 국가건강검진종합계획 브리핑(2026.6.30): https://www.korea.kr/news/policyNewsView.do?newsId=156768891
- 건강보험심사평가원 2023년 당뇨병 진료 통계: https://www.hira.or.kr/bbsDummy.do?brdScnBltNo=4&brdBltNo=11327&pageIndex=1&pgmid=HIRAA020041000100
- 미국당뇨병학회 Standards of Care 2026: https://pmc.ncbi.nlm.nih.gov/articles/PMC12690170
- 영국 국가 당뇨병 예방 프로그램 연결 연구(Ravindrarajah 외), PLoS Medicine 2023: https://doi.org/10.1371/journal.pmed.1004177
- 독일 당뇨병 전단계 생활 습관 연구(PLIS) 분석(Sandforth 외), Lancet Diabetes Endocrinol 2023: https://pubmed.ncbi.nlm.nih.gov/37769677/
- 식후 걷기 연구(DiPietro 외), Diabetes Care 2013: https://pmc.ncbi.nlm.nih.gov/articles/PMC3781561
- 먹는 순서 연구(Shukla 외), Diabetes Obes Metab 2019: https://pmc.ncbi.nlm.nih.gov/articles/PMC7398578/

■ 의학적 진단이 아닙니다
이 영상은 건강 정보 제공을 위한 것이며, 의사의 진단과 치료를 대신하지 않습니다.
사연 속 수치는 실제 진단 기준을 바탕으로 재구성한 예시입니다.
검사 결과와 몸 상태는 사람마다 다르니, 치료와 식단·운동 변화는 의사와 상담하세요.
영상 속 통계와 연구의 출처는 설명란에 있습니다.

#당뇨전단계 #식후걷기 #건강검진
```

**태그**: 당뇨 전단계, 당뇨 전단계 증상, 당뇨 전단계 관리, 공복혈당, 공복혈당장애, 당화혈색소, 건강검진 결과 보는법, 50대 건강관리, 혈당 관리, 당뇨 예방, 식후 걷기, 건강검진, 건강정보

**고정 댓글**

```
건강검진 결과지를 꺼내 이 두 가지만 확인해 보세요.
1. 올해 공복혈당 숫자 (100 미만 정상 / 100~125 공복혈당장애 / 126 이상 당뇨병 의심)
2. 작년 숫자보다 올랐는지

여러분은 '경계' 판정을 받고 어떻게 하셨나요? 바꾼 생활 습관이 있다면 나눠 주세요.
※ 개인 증상·약에 대한 질문은 진료하는 의사와 상담해 주세요. 영상은 진단을 대신하지 않습니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 3년 전 건강검진 결과지에 공복혈당 108이 찍혀 있었어요.
2. 옆에는 '공복혈당장애 의심'이라고 적혀 있었지만 그냥 넘겼죠.
3. 그때 저는 마흔아홉, 매일 야근하는 직장인이었어요.
4. 아픈 데도 없고 당뇨 기준인 126보다는 한참 낮았으니까요.
5. 다음 해 숫자가 조금 올랐을 때도 아직 경계라며 웃어넘겼어요.
6. 술자리를 줄이면 금방 내려갈 거라고 생각했죠.
7. 하지만 그 숫자는 조용히 올라가고 있었습니다.
8. 올해 결과지에는 공복혈당 131, '당뇨병 의심'이 찍혀 있었어요.
9. 확진 검사에서 당화혈색소는 7.1%, 당뇨병이라는 진단을 받았습니다.
10. 3년 사이 몸무게는 6kg 늘어 82kg이 돼 있었고요.
11. 점심을 먹고 나면 하루 종일 앉아만 있던 생활도 그대로였죠.
12. 결과지가 세 번이나 경고를 보냈는데 저는 한 번도 듣지 않았어요.
13. '경계'라는 두 글자를 괜찮다는 뜻으로 읽은 제가 원망스러워요.

**진행자 파트** — 🎙 진행자

14. 건강검진에서 '경계'라는 말을 들으면 많은 분들이 이런 생각을 하죠.
15. 아직 당뇨는 아니니까 괜찮아.
16. 아픈 데도 없는데 뭘.
17. 내년 검진 때 다시 보면 되지.
18. 이런 식으로 '아직'이라는 말에 기대다 보면 경고를 놓치게 됩니다.
19. 실제로 우리나라 30세 이상 성인 열 명 중 네 명이 당뇨병 전단계입니다.
20. 2021년과 2022년 조사를 바탕으로 약 1,410만 명으로 추정되죠.
21. 당뇨병이 있는 사람도 넷 중 한 명은 자신이 당뇨병인 줄 모릅니다.
22. 사연 속 이야기가 결코 남의 일이 아닌 이유입니다.
23. 그럼 '경계' 판정을 그냥 넘기면 왜 위험한지 하나씩 살펴보겠습니다.

> 🟨 [장면] 의학적 진단이 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 건강 정보 제공을 위한 것이며, 의사의 진단과 치료를 대신하지 않습니다.
> 사연 속 수치는 실제 진단 기준을 바탕으로 재구성한 예시입니다.
> 검사 결과와 몸 상태는 사람마다 다르니, 치료와 식단·운동 변화는 의사와 상담하세요.
> 영상 속 통계와 연구의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

24. 첫 번째 문제는 당뇨병 전단계에는 뚜렷한 증상이 없다는 것입니다.
25. 미국 질병통제예방센터는 몇 년 동안 증상 없이 지낼 수 있다고 설명합니다.
26. 건강검진을 받는 날까지 몸은 아무 신호도 보내지 않을 수 있는 거죠.
27. 그래서 미국에서는 당뇨병 전단계인 성인 열 명 중 여덟 명이 그 사실을 모릅니다.
28. 사연자도 3년 동안 아픈 곳이 한 군데도 없었죠.
29. 증상이 없다는 건 괜찮다는 뜻이 아니라, 몸이 아직 말을 안 한다는 뜻입니다.
30. 두 번째는 '경계'가 멈춰 있는 상태가 아니라는 것입니다.
31. 공복혈당 100부터 125까지는 모두 같은 '경계'로 묶입니다.
32. 그래서 108이 116이 돼도 결과지의 말은 바뀌지 않죠.
33. 하지만 같은 경계 안에서도 숫자는 계속 움직입니다.
34. 질병관리청은 공복혈당장애인 사람의 5~8%가 1년 안에 당뇨병이 될 수 있다고 봅니다.
35. 사연자의 숫자도 해마다 조금씩 126을 향해 올라가고 있었던 겁니다.
36. 세 번째는 결과지를 받아도 다음 단계로 이어지지 않는다는 것입니다.
37. 결과지에는 100 미만이면 정상, 100에서 125면 '공복혈당장애 의심'이라고 나옵니다.
38. 126 이상이면 '당뇨병 의심'으로, 확진 검사를 받아야 하는 대상이 되죠.
39. 그런데 당뇨병 의심 판정을 받고도 진단과 치료로 이어지는 사람은 39% 정도입니다.
40. 열 명 중 여섯 명은 진단과 치료로 이어지지 않는다는 뜻이죠.
41. 사연자도 3년 동안 결과지를 받기만 하고 병원에는 가지 않았어요.
42. 네 번째는 당뇨병이 된 뒤에는 관리가 훨씬 어려워진다는 것입니다.
43. 2023년 한 해 당뇨병으로 진료받은 사람은 약 383만 명이었습니다.
44. 그런데 30세 이상 당뇨병 환자 중 당화혈색소가 6.5% 아래인 사람은 32% 정도입니다.
45. 당뇨병이 생기면 목표 수치까지 조절되는 사람은 셋 중 한 명꼴인 셈이죠.
46. 당뇨병이 오래되면 눈과 콩팥, 신경에 합병증이 생길 수 있습니다.
47. 그래서 당뇨병이 되기 전, 전단계에서 멈추는 게 가장 쉬운 길입니다.
48. 그렇다면 '경계' 판정을 받았을 때 무엇부터 해야 할까요?

**올바른 방법 설명 파트** — 🎙 진행자

49. 첫째, 결과지에서 '경계'라는 말 대신 공복혈당 숫자부터 확인하는 것입니다.
50. 100 미만이 정상이고, 100부터 125까지가 공복혈당장애입니다.
51. 사연자의 108은 정상보다 8이 높은, 이미 당뇨병 전단계 숫자였어요.
52. 결과지를 받으면 올해 숫자를 작년 숫자 옆에 적어 두세요.
53. 108에서 116으로 올랐다면 같은 '경계'라도 방향은 분명히 나빠지는 중입니다.
54. 둘째, 숫자가 경계에 있으면 1년을 기다리지 말고 병원에서 상담을 받는 것입니다.
55. 공복혈당장애 의심이 나왔다면 의사와 상담해 당화혈색소 검사도 받아 보세요.
56. 당화혈색소는 최근 두세 달의 평균 혈당을 보여 주는 검사입니다.
57. 5.7%부터 6.4%까지가 당뇨병 전단계, 6.5% 이상이면 당뇨병입니다.
58. '당뇨병 의심'이 나오면 다음 해 1월 31일까지 진료 한 번은 본인 부담이 없습니다.
59. 사연자처럼 131이 나왔다면 미루지 말고 이 진료부터 받아야 하죠.
60. 셋째, 몸무게를 5~7% 줄이는 것을 목표로 잡는 것입니다.
61. 영국은 2016년부터 당뇨병 전단계인 사람을 국가 예방 프로그램에 연결해 왔습니다.
62. 식사와 운동, 체중 관리를 9개월 동안 돕는 무료 프로그램입니다.
63. 프로그램에 연결된 사람은 1만 8천여 명, 비교 대상은 비슷한 조건의 5만여 명이었습니다.
64. 연결된 쪽은 당뇨병으로 넘어갈 위험이 20% 낮았습니다.
65. 다만 실제 참여가 아니라 연결 여부만 비교한 결과입니다.
66. 82kg인 사연자라면 4~6kg 정도가 목표입니다.
67. 3년 동안 늘어난 6kg을 되돌리는 것과 거의 같은 숫자죠.
68. 한 달에 1kg씩 줄이면 반년 안에 닿을 수 있습니다.
69. 넷째, 일주일에 150분 이상 움직이고, 식사 뒤에는 바로 앉지 않는 것입니다.
70. 하루 30분씩 주 5일 빠르게 걸으면 150분이 됩니다.
71. 공복혈당이 105에서 125 사이인 60세 이상 10명을 대상으로 한 연구가 있습니다.
72. 매 식사 30분 뒤 15분씩 걸은 날은 하루 평균 혈당이 129에서 116으로 낮았습니다.
73. 다만 10명이 하루씩 걸어 본 작은 실험이라 오래 했을 때의 효과는 알 수 없습니다.
74. 점심을 먹고 하루 종일 앉아 있던 사연자라면 점심 뒤 15분 걷기부터 시작하면 됩니다.
75. 15분이면 점심시간 안에도 넣을 수 있는 길이죠.
76. 다섯째, 같은 음식이라도 채소와 단백질을 먼저, 밥은 나중에 먹는 것입니다.
77. 당뇨병 전단계인 15명을 대상으로 한 연구에서 먹는 순서만 바꿨습니다.
78. 밥이나 빵 같은 탄수화물을 마지막에 먹었을 때 식후 혈당 최고치가 40% 넘게 낮았습니다.
79. 예를 들어 비빔밥이라면 나물과 계란을 먼저 먹고 밥은 나중에 먹는 식입니다.
80. 물론 15명의 짧은 실험이라 모든 사람에게 같은 효과가 난다고 할 수는 없습니다.
81. 그래도 돈도 시간도 들지 않으니 오늘 저녁부터 해 볼 수 있는 방법이죠.
82. 여섯째, 목표를 '경계 유지'가 아니라 '정상 숫자로 돌아가기'로 잡는 것입니다.
83. 독일에서 당뇨병 전단계인 천백여 명이 1년 동안 참여한 생활 습관 연구가 있습니다.
84. 2023년 발표된 분석은 그중 몸무게를 5% 이상 줄인 298명을 따로 살펴봤습니다.
85. 이 가운데 열 명에 네 명꼴은 혈당이 정상 범위까지 돌아왔습니다.
86. 정상으로 돌아온 사람은 그렇지 못한 사람보다 당뇨병 위험이 73% 낮았습니다.
87. 생활 습관 관리가 끝난 뒤 2년 동안 지켜본 결과입니다.
88. 나중에 따로 나눠 본 분석이라 숫자보다 방향으로 보시면 됩니다.
89. 108을 받았던 사연자라면 다음 검진에서 공복혈당 100 미만이 목표였던 거죠.
90. 이렇게 해서 '경계' 판정을 넘기면 위험한 이유와 여섯 가지 방법을 알아보았습니다.
91. 올해 건강검진 결과지를 꺼내 공복혈당 숫자부터 확인해 보세요.
92. 작년보다 올랐다면 내년 검진을 기다리지 말고 병원 상담부터 받아 보세요.
93. 건강하셨으면 좋겠습니다.
94. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
