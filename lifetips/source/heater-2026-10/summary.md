# heater-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py lifetips heater-2026-10` (2026-10-11 04:02). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **보일러보다 싸다는 말에 온풍기만 틀었다가 전기요금 2만원이 13만원이 됐습니다. 전기 난방으로 버틴 사람들의 불편한 진실**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 90 / 자막 113, 길이 8:43 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–14 · 진행자 15–90 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/heater-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 보일러보다 싸다는 말에 온풍기만 틀었다가 전기요금 2만원이 13만원이 됐습니다. 전기 난방으로 버틴 사람들의 불편한 진실 `속마음 · 작은 돈→큰 돈 · 불편한 진실` 67자 — 짝 썸네일: thumbnail_1 (고지서 숫자 반전)
- [ ] **T2.** 가스비 3만원 아끼려고 켠 온풍기 하나에 전기요금이 13만원 나왔습니다. 누진제 모르고 전기 난방한 사람들의 공통점 `행동 · 아낀 돈→나간 돈 · 공통점` 64자 — 짝 썸네일: thumbnail_2 (인물·고지서 장면)
- [ ] **T3.** (짧은 변형) 난방비 절약 꿀팁 따라 했다가 전기요금 13만원, 마지막에 꼭 하는 후회 `계기 · 결과 금액 · 마지막에 꼭 하는 후회` 40자 — 짝 썸네일: thumbnail_3 (꿀팁 약속 vs 결과 대비)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (고지서 카드)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 평소 전기요금이 한 달 만에 6배 넘게 뛴 **고지서 숫자 반전**(2만 원 → 13만 원)이 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위 | 전기요금 2만 원 | 잉크 #1E1E1E | "전기요금"에 노랑 형광펜 #FFD400 (유일한 강조) |
| 아래 | 13만 원 | 흰색 (빨강 #E63B2E 상자 위) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, extra-cost red #E63B2E, saved-money blue #2D6CDF.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. A single large white paper
card, slightly tilted, with a thin ink-black outline fills the center of the frame, like a very simple monthly bill
(NOT a real utility bill: no company name, no logo, no customer number, no barcode, no QR code, no table lines).
Top part of the card: the text "전기요금 2만 원" in bold ink-black letters, with a bright yellow (#FFD400)
highlighter stripe behind the word "전기요금" only. Below it, one thick red (#E63B2E) arrow pointing down.
Lower half of the card: a wide solid red (#E63B2E) rounded box with the huge white bold text "13만 원" centered,
the largest element in the image (about a quarter of the image height). No people, no faces, no heater, no fire.
Minimal, nothing decorative. Keep all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (고지서를 본 사연자)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 온풍기 옆에서 고지서를 보고 굳은 **또래 인물의 표정**이 "내 얘기다"를 더 크게 느끼게 한다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위 | 온풍기 한 달 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (유일한 강조, 글자 전체 높이) |
| 아래 | 13만 원 | 빨강 #E63B2E (네이비 위, 흰 외곽선) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, extra-cost red #E63B2E, saved-money blue #2D6CDF.
Bottom-right corner kept empty (video length badge).
Left 55% of the frame: a realistic photo of a small, plain studio apartment in winter. A fictional Korean woman in her
late twenties (fictional person, not resembling any real or famous person, natural Korean features, realistic photo style)
sits on the floor with a gray blanket wrapped around her shoulders, holding a single sheet of blank white paper with
both hands and staring at it, frozen in shock and regret, mouth slightly open. Beside her on the floor is a generic plain
white box-shaped electric fan heater with no brand, no logo and no visible buttons, giving off only a faint warm orange
glow (no flames, no fire, no smoke). Soft natural indoor light.
Right 45% of the frame: solid dark navy (#14213D) panel with two lines of large Korean text, stacked:
top line "온풍기 한 달" in bold ink-black letters on a bright yellow (#FFD400) box that covers the full height of the letters;
bottom line "13만 원" in huge bold red (#E63B2E) letters with a thin white outline, the largest element in the image.
Keep her face and all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (꿀팁이 약속한 것 vs 결과)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 꿀팁이 약속한 **"난방비 반값"**과 실제 결과 **"전기요금 13만 원"**을 나란히 놓은 대비가 검색해서 들어온 시청자를 붙잡는다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 꼬리표 | 꿀팁 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (유일한 강조) |
| 왼쪽 | 난방비 반값 | 파랑 #2D6CDF (꿀팁이 약속한 절약) | 크게 |
| 오른쪽 | 전기요금 13만 원 | "전기요금" 흰색 · "13만 원" 빨강 #E63B2E | "13만 원"이 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, extra-cost red #E63B2E, saved-money blue #2D6CDF.
Bottom-right corner kept empty (video length badge).
Clean flat editorial split-screen graphic divided down the middle by a thick ink-black vertical line.
Left half on a cream (#F2EBDD) background: a small tag at the top with the text "꿀팁" in ink-black bold letters on a
bright yellow (#FFD400) box; below it the large bold blue (#2D6CDF) text "난방비 반값"; at the bottom a simple flat
illustration of a generic plain white box-shaped electric fan heater with no brand, no logo and no visible buttons
(no flames, no fire).
Right half on a solid dark navy (#14213D) background: the text "전기요금" in bold white letters, and below it the huge
bold red (#E63B2E) text "13만 원" with a thin white outline, the largest element in the image.
No people, no faces. Minimal, nothing decorative. Keep all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
평소 2만 원 남짓이던 전기요금이, 난방비를 아끼려고 온풍기를 켠 한 달 만에 13만 원이 됐습니다.
겨울 전기 난방이 왜 요금을 키우는지 누진제 요금표로 계산해 보고, 전기 난방기를 켜기 전에 확인할 것 5가지를 정리했습니다.

■ 이 영상에서 다루는 것
- 전기요금은 쓸수록 단가가 뛴다 (주택용 누진제 3단계, 겨울에는 200·400kWh가 문턱)
- 온풍기 한 대가 집 전체 전기보다 많이 쓴다 (2천 와트 × 하루 6시간 = 한 달 372kWh)
- 같은 열이라도 3단계 전기는 가스 보일러보다 세 배 넘게 비싸다
- 쓰는 동안에는 누진 단계가 바뀐 걸 모른다
- 확인할 것 5가지: 누진 구간 확인, 소비전력 × 시간 계산, 누진 3단계 알림, 보일러 20도와 보온 옷, 전기 난방을 써도 되는 기준

■ 챕터
0:00 사연: 전기요금 2만 원이 13만 원
1:13 왜 전기 난방으로 버틸까
2:18 문제 01 쓸수록 단가가 뛰는 누진제
3:26 문제 02 온풍기 한 대가 집 전체보다 많이 쓴다
3:56 문제 03 같은 열이라도 전기가 훨씬 비싸다
4:39 문제 04 쓰는 동안에는 단계가 바뀐 걸 모른다
5:07 방법 첫째: 우리 집 누진 구간 확인
5:34 방법 둘째: 소비전력에 시간을 곱해 미리 계산
6:05 방법 셋째: 누진 3단계 알림 받기
6:59 방법 넷째: 보일러는 20도, 몸은 옷으로
7:31 방법 다섯째: 전기 난방을 써도 되는 기준
8:19 정리

■ 사연에 대해
이 영상의 사연은 실제 기준과 공식 자료를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시입니다.
요금은 주택용 저압 전기요금(7~8월 밖, 2023년 5월 16일 시행 요금표, 2026년 4분기까지 동결)에 기후환경요금 kWh당 9원, 연료비조정요금 kWh당 5원, 부가가치세 10%, 전력산업기반기금 2.7%를 더해 계산했습니다. 집마다 계약 종류와 할인에 따라 다를 수 있습니다.

■ 출처
- 한국전력 주택용 전기요금표(2023년 5월 16일 시행): https://files-scs.pstatic.net/2024/01/24/JLskqjrATZ/23.05.16%20%EC%8B%9C%ED%96%89%20%EC%A0%84%EA%B8%B0%EC%9A%94%EA%B8%88%ED%91%9C_%EC%A2%85%ED%95%A9.pdf
- 2026년 3분기 전기요금 동결(2026년 6월 22일): https://www.etoday.co.kr/news/view/2595748
- 2026년 4분기 전기요금 동결(2026년 9월 21일): https://news.mtn.co.kr/news-detail/2026092111090432619
- 2023년 1분기 기후환경요금 조정: https://www.news1.kr/amp/economy/policy/4910565
- 전력산업기반기금 요율 인하(2.7%): https://www.etoday.co.kr/news/view/2375003
- 한국전력 누진 3단계 알림 서비스(2026년 7월 21일): https://biz.sbs.co.kr/amp/article/20000323574
- 2023년 1월 소비자물가(통계청): https://www.newsis.com/view/NISX20230130_0002174432
- 2023년 1월 방한용품 판매: https://www.ytn.co.kr/_ln/0103_202301271043265585
- 겨울철 난방온도 20도 캠페인(2025년 12월): https://www.heraldk.com/article/2025120304400050601
- 대구 주택용 도시가스 요금(2026년 8월): https://kbmaeil.com/article/20260730500508
- 보일러 열효율(서울시): https://news.seoul.go.kr/env/archives/501345

■ 따라 하기 전에 확인하세요
이 영상은 생활 정보 제공을 위한 것이며, 특정 제품이나 업체를 추천하지 않습니다.
사연은 실제 기준과 공식 자료를 바탕으로 재구성한 이야기이고, 금액과 수치는 예시입니다.
제품과 집 구조마다 방법이 다르니, 제조사 사용설명서와 제품 표시사항을 먼저 따르세요.
영상 속 자료의 출처는 설명란에 있습니다.

#생활꿀팁 #난방비절약 #전기요금누진제
```

**태그**: 난방비 절약 꿀팁, 전기요금 누진제, 온풍기 전기세, 전기세 절약 방법, 가스비 절약방법, 겨울 난방비 줄이는 법, 누진제 3단계, 전기히터 전기요금, 난방비 폭탄, 원룸 난방, 자취 꿀팁, 생활꿀팁, 난방비절약, 누진 3단계 알림

**고정 댓글**

```
전기 난방기를 켜기 전에 이 두 가지만 계산해 보세요.
1. 지난달 사용량에서 400kWh(겨울 누진 3단계 문턱)까지 남은 양
2. 제품의 소비전력(W) ÷ 1,000 × 하루 쓸 시간 × 30일

꿀팁을 따라 했다가 오히려 요금이 더 나온 적 있나요? 그때 무엇을 먼저 확인했으면 좋았을까요?
※ 제품마다 방법이 다르니 사용설명서를 먼저 확인해 주세요. 특정 제품 홍보·구매 링크 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 지난겨울, 보일러 대신 온풍기를 쓰면 난방비가 반으로 준다는 영상을 봤어요.
2. 원룸이라면 온풍기 하나로 충분하다고 하더라고요.
3. 저는 스물아홉, 원룸에 혼자 사는 직장인이에요.
4. 퇴근하고 잘 때까지만 따뜻하면 됐으니 딱 맞는 방법 같았죠.
5. 그래서 보일러는 외출로 돌려 두고 온풍기를 하나 들였어요.
6. 2천 와트짜리 온풍기를 가장 센 단으로 매일 여섯 시간씩 틀었죠.
7. 그달 가스 요금이 평소보다 3만 원 가까이 줄어서 잘했다 싶었어요.
8. 하지만 줄어든 건 가스 요금뿐이었습니다.
9. 며칠 뒤 받은 전기요금 고지서에는 13만 원이 찍혀 있었어요.
10. 평소에는 2만 원 남짓 나오던 요금이었죠.
11. 찾아보니 전기요금은 많이 쓸수록 단가가 올라가는 누진제였어요.
12. 한 달에 400킬로와트시를 넘긴 부분에는 처음 단가의 2.5배가 넘는 요금이 붙더라고요.
13. 가스비 3만 원을 아끼려다 전기요금을 11만 원 가까이 더 낸 셈이에요.
14. 온풍기에 적힌 소비전력 숫자를 한 번만 들여다봤어도 이러지 않았을 텐데요.

**진행자 파트** — 🎙 진행자

15. 난방비를 아끼려고 전기 난방기를 켤 때 많은 분들이 이런 생각을 하죠.
16. 보일러는 집 전체를 데우니까 온풍기 하나가 더 싸겠지.
17. 전기는 쓴 만큼만 내는 거잖아.
18. 퇴근하고 몇 시간 트는 건데 얼마나 나오겠어.
19. 이런 식으로 전기 난방을 가볍게 보다 보면 고지서를 받고 나서야 놀라게 됩니다.
20. 2023년 1월 난방비 폭탄 때, 도시가스 요금은 1년 전보다 36% 넘게 올랐습니다.
21. 그때 한 대형마트에서는 온풍기 같은 방한용품이 1년 전보다 40% 가까이 더 팔렸죠.
22. 그런데 같은 달 전기요금도 1년 전보다 30% 가까이 올라 있었습니다.
23. 가스비를 피해 전기 난방으로 옮겨 가는 사연이 남의 일이 아닌 이유입니다.
24. 그럼 전기 난방으로 버티면 왜 요금이 커지는지 하나씩 살펴보겠습니다.

> 🟨 [장면] 따라 하기 전에 확인하세요 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 생활 정보 제공을 위한 것이며, 특정 제품이나 업체를 추천하지 않습니다.
> 사연은 실제 기준과 공식 자료를 바탕으로 재구성한 이야기이고, 금액과 수치는 예시입니다.
> 제품과 집 구조마다 방법이 다르니, 제조사 사용설명서와 제품 표시사항을 먼저 따르세요.
> 영상 속 자료의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

25. 첫 번째 문제는 전기요금이 쓸수록 단가가 뛰는 누진제라는 것입니다.
26. 주택용 전기요금은 한 달에 쓴 전기의 양, 킬로와트시를 세 단계로 나눠 계산합니다.
27. 200킬로와트시까지는 킬로와트시당 120원, 그다음 400까지는 214.6원입니다.
28. 400을 넘는 부분에는 307.3원이 붙어 처음 단가의 2.5배가 넘습니다.
29. 기본요금도 3단계로 넘어가는 순간 1,600원에서 7,300원으로 뜁니다.
30. 누진제를 여름 에어컨 이야기로만 아는 분이 많습니다.
31. 하지만 구간이 300과 450으로 넓어지는 건 7월과 8월뿐입니다.
32. 겨울에는 200과 400이라는 문턱이 그대로라서 3단계에 더 빨리 닿습니다.
33. 사연자는 평소 140킬로와트시를 쓰다가 온풍기를 켠 달에 512킬로와트시를 썼습니다.
34. 쓴 양은 3.7배인데 요금은 6배 가까이 늘었죠.
35. 200을 넘긴 부분부터 단가가 차례로 뛰었기 때문입니다.
36. 두 번째는 온풍기 한 대가 집 전체 전기보다 많이 쓴다는 것입니다.
37. 2천 와트는 한 시간에 2킬로와트시를 쓴다는 뜻입니다.
38. 하루 여섯 시간이면 12킬로와트시, 31일이면 372킬로와트시가 되죠.
39. 사연자의 원룸이 평소 한 달 동안 쓰던 140킬로와트시의 2.6배입니다.
40. 냉장고와 조명, 휴대폰 충전까지 다 합친 것보다 온풍기 하나가 더 많이 쓴 셈이죠.
41. 세 번째는 같은 열을 내도 전기가 가스보다 훨씬 비싸다는 것입니다.
42. 온풍기는 쓴 전기를 거의 그대로 열로 바꿉니다.
43. 하지만 3단계에서는 전기 1킬로와트시에 기후환경요금 등을 더해 321원이 넘게 듭니다.
44. 도시가스 요금은 지역마다 조금 다르지만, 대구의 주택용 요금으로 계산해 보면 이렇습니다.
45. 같은 열을 가스 보일러로 내면, 열효율 80%인 일반 보일러로도 3분의 1이 안 듭니다.
46. 온풍기가 한 달 동안 낸 열을 가스 보일러로 냈다면 4만 원 안팎이면 됐습니다.
47. 그 열을 전기로 사느라 11만 원 가까이를 더 낸 거죠.
48. 네 번째는 쓰는 동안에는 단계가 바뀐 걸 알 수 없다는 것입니다.
49. 전기요금은 한 달 사용량을 모아 한 번에 계산되고, 고지서는 다 쓴 뒤에 옵니다.
50. 사연자는 열사흘째에 2단계, 스물닷새째에 3단계로 넘어갔습니다.
51. 하지만 온풍기는 마지막 날까지 똑같이 돌아갔죠.
52. 그렇다면 겨울에 전기 난방기를 쓸 때는 무엇부터 확인해야 할까요?

**올바른 방법 파트** — 🎙 진행자

53. 첫째, 우리 집의 누진 구간부터 확인하는 것입니다.
54. 고지서나 한국전력 앱에서 지난달 사용량을 확인해 보세요.
55. 겨울에는 200과 400킬로와트시가 문턱입니다.
56. 사연자처럼 평소 140을 쓰는 집이라면 400까지 260킬로와트시가 남아 있습니다.
57. 2천 와트 온풍기를 하루 4시간 남짓 틀면 한 달 만에 이 여유를 다 씁니다.
58. 둘째, 소비전력에 쓰는 시간을 곱해 요금을 미리 계산하는 것입니다.
59. 제품에 적힌 소비전력을 1,000으로 나누고 시간을 곱하면 킬로와트시가 나옵니다.
60. 같은 온풍기라도 하루 2시간이면 한 달 청구액이 약 4만 8천 원입니다.
61. 하루 4시간이면 약 8만 원, 6시간이면 사연자처럼 13만 원이 되죠.
62. 4시간에서 6시간으로 늘린 마지막 두 시간에만 5만 원이 더 붙는 겁니다.
63. 셋째, 누진 3단계 알림을 받아 두는 것입니다.
64. 한국전력은 올해 7월부터 한 달 사용량이 3단계 기준의 80%에 이르면 알림을 보냅니다.
65. 겨울이라면 320킬로와트시에서 알림이 오는 거죠.
66. 지금은 한국전력 앱 가입자를 대상으로 시범 운영하고 있습니다.
67. 12월부터는 원격으로 검침하는 주택 1,100만 호로 넓힐 계획입니다.
68. 그때부터는 앱이 없어도 메신저로 알림을 받을 수 있다고 합니다.
69. 사연자가 이 알림을 받았다면 스무날째쯤 320을 넘었다는 걸 알았을 겁니다.
70. 남은 열하루 동안 온풍기를 껐다면 사용량은 380킬로와트시에서 멈췄을 겁니다.
71. 보일러 가스비는 조금 더 들었겠지만, 전기요금은 8만 원 가까이로 5만 원 넘게 줄었겠죠.
72. 넷째, 넓은 공간은 보일러로 20도에 맞추고 몸은 옷으로 데우는 것입니다.
73. 기후에너지환경부는 지난겨울 난방온도 20도 지키기 캠페인을 벌였습니다.
74. 캠페인에서는 난방온도를 1도만 낮춰도 에너지 소비가 7%쯤 줄 수 있다고 설명합니다.
75. 그 대신 내복과 수면양말 같은 보온 옷을 입자고 권하죠.
76. 보일러를 20도에 맞추고, 온풍기는 잠깐만 쓰는 쪽이 같은 열을 더 싸게 얻습니다.
77. 다섯째, 전기 난방은 조건이 맞을 때만 쓰는 것입니다.
78. 전기 난방이 무조건 손해라는 뜻은 아닙니다.
79. 기준은 한 달 사용량이 400킬로와트시 안에서 끝나고, 짧게 쓰는 것입니다.
80. 데우는 곳도 사람 가까이, 좁은 자리로 정합니다.
81. 예를 들어 아침 출근 준비 30분만 온풍기를 켜면, 한 달 31킬로와트시입니다.
82. 사연자의 집이라면 171킬로와트시로 여전히 1단계입니다.
83. 요금은 평소보다 5천 원 가까이 늘어나는 정도죠.
84. 여섯 시간씩 켰을 때 늘어난 11만 원 가까이와 비교하면 차이가 큽니다.
85. 온풍기 꿀팁이 틀렸다기보다, 우리 집 사용량을 확인하는 순서가 빠졌던 겁니다.

**마무리** — 🎙 진행자

86. 이렇게 해서 전기 난방이 요금을 키우는 이유와, 다섯 가지 방법을 알아보았습니다.
87. 전기 난방기를 켜기 전에 지난달 사용량과 누진 구간부터 확인해 보세요.
88. 제품에 적힌 소비전력에 하루 쓸 시간을 곱해 보는 것도 잊지 마시고요.
89. 안전하고 알뜰한 살림 하셨으면 좋겠습니다.
90. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
