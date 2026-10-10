# multagi-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py stock multagi-2026-10` (2026-10-10 14:56). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **평단 낮추면 된다는 말만 믿고 물타서 -200만원이 -2천만원이 됐습니다. 손절 기준 없이 버틴 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 91 / 자막 107, 길이 8:34 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–14 · 진행자 15–91 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle에서 `tts_narration.py all`로 만들어 `source/multagi-2026-10/narration.mp3`에 올리면 영상 제작 시작 |
| 영상 코드 | ✅ `video/src/episodes/multagi-2026-10/` |
| 렌더 | ✅ final_1080p.mp4 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 평단 낮추면 된다는 말만 믿고 물타서 -200만원이 -2천만원이 됐습니다. 손절 기준 없이 버틴 사람들의 공통점 `계기 · 손실→손실 · 공통점` 62자 — 짝 썸네일: thumbnail_1 (계좌 숫자 반전)
- [ ] **T2.** 본전 금방 온다며 기준 없이 물타서 -200만원이 -2천만원이 됐습니다. 추가 매수로 버틴 사람들의 최악의 결말 `속마음 · 손실→손실 · 최악의 결말` 62자 — 짝 썸네일: thumbnail_2 (인물 장면)
- [ ] **T3.** (짧은 변형) 물타기 두 번에 -200만원이 -2천만원이 됐습니다. 기준 없이 추가 매수한 사람들의 불편한 진실 `행동 · 손실→손실 · 불편한 진실` 54자 — 짝 썸네일: thumbnail_3 (평단 ↓ vs 손실)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (계좌 카드)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 작은 손실이 10배로 커진 **계좌 숫자 반전**이 가장 클릭을 부른다 (성공 썸네일 중 인물 없는 3개가 모두 이 형태)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 시작 | -200만 원 | 파랑 #2D6CDF | — |
| 라벨 | 물타기 2번 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (유일한 강조) |
| 결과 | -2,000만 원 | 흰색 (파랑 상자 위) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. A large light-cream rounded
rectangle card with a thin black outline fills most of the frame, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos). Inside the card, top-left: the text "-200만 원" in large
blue (#2D6CDF) bold letters. Below it, a thick blue arrow pointing down, and to the right of the arrow the label
"물타기 2번" in black bold letters over a bright yellow (#FFD400) highlighter stripe. The lower half of the card is a wide
solid blue (#2D6CDF) rounded box with the huge white bold text "-2,000만 원" centered, the largest element in the image.
No people, no faces. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 손실을 확인한 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (성공 썸네일 24개 중 약 20개가 얼굴)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 속마음 | 본전 오겠지 | 흰색 #F7F3EA ("본전"만 검정) | "본전"에 노랑 상자 (글자 전체 높이) |
| 결과 | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned room in early morning. On the left 40% of the frame, a fictional Korean man in his
early 40s, office-worker look (plain shirt), sitting and holding a smartphone, his other hand on his forehead, frozen
stunned and regretful expression, face lit by the phone's cold light. The phone screen shows only a simple blue line
dropping sharply, no app interface, no text. Fictional person, not resembling any real or famous person, natural Korean
features. On the right side, large bold headline text "본전 오겠지" in off-white, where only the word "본전" sits on a
solid bright yellow (#FFD400) box with black text. Below it, a wide solid blue (#2D6CDF) rounded box with a thin white
border containing the huge white bold text "-2,000만 원", the largest element. No crying, no extreme fear.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (평단 ↓ vs 손실)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: "평단은 내려갔는데 손실은 커졌다"는 **기대와 결과의 대비**가 물타기 해 본 사람에게 가장 와닿는다 (문제 분석 첫 번째 메시지)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 평단 | 검정 #1E1E1E | — (화살표는 웜 그레이 #9A968E) |
| 오른쪽 | 손실 | 검정 (노랑 상자 위) | 노랑 상자 #FFD400 (유일한 강조) |
| 결과 | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | — |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat editorial paper-collage graphic. The frame is split by a vertical torn-paper edge slightly left of center.
Left side: cream paper (#F2EBDD) with the large black bold text "평단" near the top and a big warm-gray (#9A968E)
paper-cut arrow pointing straight down below it. Right side: dark navy paper (#14213D) with the large text "손실" in black
on a solid bright yellow (#FFD400) box near the top, and below it a wide solid blue (#2D6CDF) rounded box with a thin white
border containing the white bold text "-2,000만 원". No people. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
평단 낮추면 본전이 금방 온다고 믿고 물타기를 두 번 했더니, -200만 원이던 손실이 -2천만 원이 됐습니다.
기준 없는 물타기가 왜 위험한지 4가지로, 물타기와 손절은 어떤 기준으로 해야 하는지 5가지로 정리했습니다.

■ 이 영상에서 다루는 것
- 평단은 조금 내려가도 한 종목에 걸린 돈은 크게 늘어나는 이유
- 떨어진 가격이 곧 싼 가격은 아닌 이유 (유나이티드헬스 2025년 4~5월)
- 사람은 왜 손실 난 종목을 너무 오래 붙잡을까 (2020년 개인 투자자 20만 명 분석)
- 떨어질수록 더 사들인 돈이 손실을 키운 이유 (카카오 2021~2026년)
- 물타기·손절의 기준 5가지

■ 챕터
0:00 사연: 물타기 두 번에 -2천만 원
1:14 왜 기준 없이 물타기를 할까
2:05 문제 01 평단은 조금, 걸린 돈은 크게
2:40 문제 02 떨어진 가격은 싼 가격이 아니다
3:36 문제 03 손실 종목을 너무 오래 붙잡는다
4:23 문제 04 만회하려는 물타기는 멈추기 어렵다
5:22 기준 첫째: 산 이유를 한 줄로
5:49 기준 둘째: 떨어진 이유부터 확인
6:13 기준 셋째: 평단은 잊고 지금 가격으로
6:45 기준 넷째: 손절 가격을 미리 정하기
7:31 기준 다섯째: 물타기를 해도 되는 조건과 금액
8:17 정리

■ 사연에 대해
이 영상의 사연은 실제 주가 흐름(유나이티드헬스, 2025년 4~5월)을 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시입니다.

■ 출처
- 유나이티드헬스 일별 주가 (2025년 4~5월): https://finance.yahoo.com/quote/UNH/history/?period1=1744243200&period2=1748390400
- 유나이티드헬스 2026년 10월 주가: https://stockanalysis.com/stocks/unh/history/
- 2025년 4월 17일 하락: https://www.barchart.com/story/news/32171033/should-you-buy-the-dip-in-unitedhealth-stock-after-unh-posted-its-worst-day-in-25-years
- 2025년 5월 13일 실적 전망 철회·CEO 사임: https://www.pbs.org/newshour/health/unitedhealth-group-largest-health-insurer-in-u-s-withdraws-financial-outlook-for-2025
- 2025년 5월 15일 법무부 수사 보도: https://www.itiger.com/news/2535842473
- 2025년 5월 서학개미 순매수: https://v.daum.net/v/20250601150238508
- 자본시장연구원 (2022), 국내 개인투자자의 행태적 편의와 거래행태: https://www.kcmi.re.kr/report/report_view?report_no=1481
- 카카오 일별 주가: https://finance.yahoo.com/quote/035720.KS/history/
- 2021년 9월 카카오 급락 주간 개인 순매수: https://news.tf.co.kr/read/ogmeta/1887650.htm
- 2022년 개인 순매수: https://www.fnnews.com/news/202212181004111951
- 카카오 소액주주 수: https://www.sedaily.com/article/14055723
- S&P 500 2025년 4월 하락: https://www.investing.com/news/economy-news/futures-rise-after-heavy-losses-on-hopes-of-talks-over-tariffs-3972893
- S&P 500 2025년 6월 사상 최고치: https://finviz.com/news/92105/sp-500-hits-new-record-close-why-etfs-could-gain-more

■ 투자 유의 사항
이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
투자 판단과 책임은 투자자 본인에게 있습니다.

#주식 #물타기 #손절
```

**태그**: 물타기, 물타기 기준, 손절, 손절 기준, 평단, 평균단가, 추가 매수, 주식 손실, 주식 물림, 주식, 주식 초보, 주식 공부, 미국 주식, 서학개미, 유나이티드헬스, 처분 효과, 카카오

**고정 댓글**

```
물타기 버튼을 누르기 전에 이 두 가지부터 적어 보세요.
1. 이 종목을 산 이유 한 줄
2. 손절 가격 (예: 처음 산 가격에서 -10%)

여러분은 물타기를 해 본 적이 있나요? 그때 정해 둔 기준이 있었는지 댓글로 나눠 주세요.
※ 이 영상은 투자 권유가 아닙니다. 특정 종목 추천·리딩방 홍보 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 2025년 4월, 유나이티드헬스 주가가 하루 만에 22% 넘게 떨어졌어요.
2. 미국 최대 건강보험사인데 의료비가 예상보다 많이 나가 실적 전망을 낮췄대요.
3. 이렇게 큰 회사가 망하진 않을 테니 지금이 싸게 살 때라고 생각했어요.
4. 모아 둔 8천만 원 중 5천만 원으로 먼저 샀죠.
5. 그런데 일주일 만에 -200만 원이 됐어요.
6. 평단을 낮추면 된다는 말만 믿고 그날 바로 1,500만 원을 더 샀어요.
7. 주가가 더 떨어지자 남은 1,500만 원까지 넣었죠.
8. 평단이 내려갔으니 조금만 반등해도 본전이라고 생각했어요.
9. 하지만 반등은 끝내 오지 않았습니다.
10. 5월 14일 아침, 눈을 뜨자마자 계좌를 열었더니 -2천만 원이 찍혀 있었어요.
11. 밤사이 회사가 그해 실적 전망을 아예 거둬들이고 CEO까지 물러났다는 소식이 나왔더라고요.
12. 주가는 하루 만에 18% 가까이 빠졌고요.
13. 평단을 낮추려고 넣은 3천만 원이 오히려 손실만 키운 셈이에요.
14. 물타기 버튼을 누른 제 손가락이 원망스러워요.

**진행자 파트** — 🎙 진행자

15. 산 종목이 계속 떨어질 때 많은 분들이 이런 생각을 하죠.
16. 평단만 낮추면 조금만 올라도 본전이야.
17. 이렇게 큰 회사가 설마 망하겠어?
18. 여기서 팔면 손실이 확정되잖아.
19. 이런 식으로 손실을 인정하기 싫은 마음이 기준 없는 물타기로 이어집니다.
20. 실제로 2025년 5월 한 달간 서학개미는 이 종목을 4,800억 원 넘게 순매수했습니다.
21. 미국 주식에 투자하는 국내 투자자들이 그달 가장 많이 사들인 종목이었죠.
22. 사연 속 이야기가 결코 남의 일이 아닌 이유입니다.
23. 그럼 기준 없는 물타기가 왜 위험한지 하나씩 살펴보겠습니다.

> 🟨 [장면] 투자 권유가 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
> 사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
> 과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
> 투자 판단과 책임은 투자자 본인에게 있습니다.

**문제 분석 파트** — 🎙 진행자

24. 첫 번째 문제는 평단은 조금 내려가도 걸린 돈은 크게 늘어난다는 것입니다.
25. 사연자는 물타기로 3천만 원을 더 넣었습니다.
26. 그 덕에 평단은 428달러에서 415달러로 3% 정도 내려갔습니다.
27. 대신 한 종목에 걸린 돈은 5천만 원에서 8천만 원으로 60%나 늘었죠.
28. 그래서 폭락한 날, 물타기를 안 했을 때보다 손실이 600만 원 넘게 커졌습니다.
29. 평단을 낮춘다는 건 사실 같은 종목에 돈을 더 거는 일입니다.
30. 두 번째는 떨어진 가격이 곧 싼 가격은 아니라는 것입니다.
31. 주가가 떨어지는 데에는 이유가 있을 수 있습니다.
32. 유나이티드헬스는 4월 17일 실적 전망을 낮추면서 하루 만에 22% 떨어졌습니다.
33. 5월 13일에는 전망 철회와 CEO 사임이 겹치며 또 18% 가까이 폭락했습니다.
34. 이틀 뒤에는 11% 가까이 더 빠졌죠.
35. 미국 법무부가 이 회사를 수사 중이라는 보도 때문이었습니다.
36. 미국 정부의 노인 의료보험인 메디케어와 관련된 사기 혐의였죠.
37. 그렇게 585달러이던 주가는 한 달 만에 274달러, 절반 아래로 떨어졌습니다.
38. 1년 반이 지난 2026년 10월에도 주가는 376달러 정도입니다.
39. 사연자의 평단 415달러보다 여전히 아래죠.
40. 세 번째는 사람이 원래 손실 난 종목을 너무 오래 붙잡는다는 것입니다.
41. 자본시장연구원이 2020년 개인 투자자 약 20만 명의 거래를 분석했습니다.
42. 산 다음 날 수익이 난 종목은 41%를 팔았습니다.
43. 그런데 손실 난 종목은 22%만 팔고, 78%는 그대로 들고 있었죠.
44. 이 습관이 가장 강한 투자자들은 들고 있던 종목이 평균 9.8% 손실이었습니다.
45. 반대로 손실 종목부터 정리한 투자자들은 평균 4.9% 수익이었죠.
46. 본전을 기다리는 마음이 오히려 수익을 깎아 먹은 겁니다.
47. 물타기는 이렇게 붙잡고 있는 종목에 돈까지 더 얹는 일입니다.
48. 네 번째는 손실을 만회하려는 물타기는 갈수록 멈추기 어렵다는 것입니다.
49. 2021년 6월, 카카오 주가는 16만 9,500원까지 올랐습니다.
50. 그해 9월 금융당국의 빅테크 규제 소식에 일주일 만에 17% 가까이 빠졌죠.
51. 그런데 그 한 주 동안 개인 투자자는 1조 원 넘게 사들였습니다.
52. 주가가 반 토막 난 2022년에도 2조 원 넘게 더 샀죠.
53. 그해 소액주주는 오히려 15만 명 가까이 늘어 206만 명이 됐습니다.
54. 하지만 2026년 10월 주가는 3만 2천 원대, 고점의 5분의 1도 안 됩니다.
55. 떨어질수록 더 사들인 돈만큼 손실도 함께 커진 겁니다.
56. 물론 물타기가 통한 경우도 있습니다.
57. 하지만 결과를 미리 알고 물타기를 할 수는 없습니다.
58. 그렇다면 물타기와 손절은 어떤 기준으로 해야 할까요?

**올바른 방법 설명 파트** — 🎙 진행자

59. 첫째, 사기 전에 이 종목을 사는 이유를 한 줄로 적어 두는 것입니다.
60. 사연자의 이유는 큰 회사라 망하지 않는다는 것이었습니다.
61. 이 이유로는 지금 가격이 싼지, 언제 다시 오를지 판단할 수 없습니다.
62. 반대로 실적이 다시 좋아질 것이라고 적었다면 기준이 생깁니다.
63. 5월 13일 회사가 실적 전망을 철회한 순간, 그 이유는 깨진 겁니다.
64. 둘째, 주가가 떨어지면 물타기 전에 떨어진 이유부터 확인하는 것입니다.
65. 시장 전체가 함께 빠진 건지, 그 회사에만 문제가 생긴 건지 나눠 봐야 합니다.
66. 사연자가 처음 산 4월 23일은 실적 전망을 낮춘 지 엿새 뒤였습니다.
67. 회사에 문제가 생겨 떨어지는 중이라면 물타기는 하지 않습니다.
68. 셋째, 물타기를 하기 전에 평단은 잊고 지금 가격에서 다시 판단하는 것입니다.
69. 사연자가 마지막 물타기를 한 5월 9일 주가는 381달러였습니다.
70. 그때 평단 424달러는 회사의 앞날과 아무 상관이 없는 숫자입니다.
71. 381달러인 이 회사를 처음 본다면 1,500만 원을 새로 넣을지 물어보는 거죠.
72. 실적 전망을 낮춘 회사라는 걸 알고도 사겠다는 답이 나올 때만 물타기를 합니다.
73. 넷째, 손절 가격을 미리 정해 두고 지키는 것입니다.
74. 예를 들어 처음 산 가격보다 10% 떨어지면 판다고 정하는 겁니다.
75. 사연자라면 손절 가격은 428달러보다 10% 낮은 385달러입니다.
76. 주가는 5월 9일 이 가격 아래로 내려갔습니다.
77. 물타기 없이 이 기준대로 팔았다면 손실은 500만 원에서 멈췄을 겁니다.
78. 공교롭게도 사연자가 마지막 물타기를 한 바로 그날이었죠.
79. 기준이 있었다면 500만 원에서 멈췄을 그날, 사연자는 -2천만 원 쪽으로 들어선 겁니다.
80. 증권사 앱에 자동 매도 기능이 있다면 걸어 두는 것도 방법입니다.
81. 다섯째, 물타기는 세 가지가 모두 맞을 때만, 정해 둔 금액 안에서 하는 것입니다.
82. 산 이유가 그대로이고, 시장 전체가 함께 빠졌고, 지금 가격에서 새로 사도 될 때입니다.
83. 시장 전체가 빠진 예로는 2025년 4월 초가 있습니다.
84. 미국 대표 지수인 S&P 500이 관세 충격으로 2월 고점보다 19% 가까이 떨어졌죠.
85. 이 하락은 석 달이 안 돼 회복돼, 6월 말 사상 최고치를 다시 넘었습니다.
86. 같은 시기 유나이티드헬스는 회사 문제로 떨어졌고, 그 뒤로도 회복하지 못했습니다.
87. 금액은 예를 들어 5천만 원으로 시작했다면 1,500만 원 한 번까지로 정해 둡니다.

**마무리** — 🎙 진행자

88. 이렇게 해서 기준 없는 물타기가 위험한 이유와 물타기·손절의 기준을 알아보았습니다.
89. 물타기 버튼을 누르기 전에 산 이유와 손절 가격부터 다시 확인하세요.
90. 성공 투자 하셨으면 좋겠습니다.
91. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
