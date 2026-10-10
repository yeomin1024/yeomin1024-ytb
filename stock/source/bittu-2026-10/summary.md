# bittu-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py stock bittu-2026-10` (2026-10-10 07:10). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **신용까지 써서 번 1,500만원이 반대매매 한 번에 -2,500만원이 됐습니다. 빚투한 사람들의 최악의 결말**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 87 / 자막 104, 길이 8:12 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 스토리보드 | ⏳ 영상 코드 제작 전 |
| 오디오 | ⏳ 없음 → `source/bittu-2026-10/narration.mp3`(또는 .wav·.m4a)를 올리면 4단계 시작 |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 신용까지 써서 번 1,500만원이 반대매매 한 번에 -2,500만원이 됐습니다. 빚투한 사람들의 최악의 결말 `행동 · 수익→손실 · 최악의 결말` 60자 — 짝 썸네일: thumbnail_1 (계좌 숫자 반전)
- [ ] **T2.** 내 돈만 넣기 아까워 빚까지 냈다가 1,500만원 수익이 -2,500만원이 됐습니다. 빚으로 주식한 사람들의 공통점 `속마음 · 수익→손실 · 공통점` 64자 — 짝 썸네일: thumbnail_2 (인물·문자 장면)
- [ ] **T3.** (짧은 변형) 반대매매 한 번에 +1,500만원이 -2,500만원이 됐습니다. 빚투한 사람들의 불편한 진실 `장면 · 수익→손실 · 불편한 진실` 51자 — 짝 썸네일: thumbnail_3 (빚 2배 대비)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (계좌 카드)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 수익이 손실로 뒤집힌 **계좌 숫자 반전**과 결정적 장면 한 단어("반대매매")가 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 시작 | +1,500만 원 | 빨강 #E63B2E | — |
| 라벨 | 반대매매 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (유일한 강조) |
| 결과 | -2,500만 원 | 흰색 (파랑 상자 위) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. A large light-cream rounded
rectangle card with a thin black outline fills most of the frame, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos). Inside the card, top-left: the text "+1,500만 원" in large
red (#E63B2E) bold letters. Below it, a thick blue arrow pointing down, and to the right of the arrow the label
"반대매매" in black bold letters over a bright yellow (#FFD400) highlighter stripe. The lower half of the card is a wide
solid blue (#2D6CDF) rounded box with the huge white bold text "-2,500만 원" centered, the largest element in the image.
No people, no faces. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (담보 부족 문자)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 담보 부족 문자를 받은 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (성공 썸네일 24개 중 약 20개가 얼굴)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 장면 | 담보 부족 | 검정 #1E1E1E | 노랑 상자 #FFD400 (유일한 강조) |
| 결과 | -2,500만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned living room at night, lights off. On the left 40% of the frame, a fictional Korean
man in his mid 30s, office-worker look (plain knit or shirt), sitting on a sofa and staring at a smartphone held in both
hands, frozen stunned expression, face lit by the phone's cold light. The phone screen shows only one simple blank
message bubble shape and a simple blue line dropping sharply, no app interface, no text. Fictional person, not resembling
any real or famous person, natural Korean features. On the right side, a solid bright yellow (#FFD400) box with the large
black bold text "담보 부족". Below it, a wide solid blue (#2D6CDF) rounded box with a thin white border containing the huge
white bold text "-2,500만 원", the largest element. No crying, no extreme fear.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (주가 -42% vs 내 돈 -83%)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: "주가는 절반도 안 빠졌는데 내 돈은 거의 다 사라졌다"는 **빚이 키운 손실의 대비**가 신용을 써 본 사람에게 가장 와닿는다 (문제 분석 첫 번째 메시지)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 주가 | 검정 #1E1E1E | — (막대는 웜 그레이 #9A968E) |
| 오른쪽 | 내 돈 | 검정 (노랑 상자 위) | 노랑 상자 #FFD400 (유일한 강조) |
| 결과 | -2,500만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat editorial paper-collage graphic. The frame is split by a vertical torn-paper edge slightly left of center.
Left side (45%, cream #F2EBDD): the large black bold word "주가" at the top, and below it a tall outlined bar where only
a bit more than half remains filled in warm gray (#9A968E). Right side (55%, dark navy #14213D): the word "내 돈" in black
bold letters on a solid bright yellow (#FFD400) box at the top, and below it a tall outlined bar that is almost completely
empty, with only a thin sliver of blue (#2D6CDF) left at the bottom. Next to that bar, a wide solid blue (#2D6CDF) rounded
box with a thin white border containing the huge white bold text "-2,500만 원", the largest element.
No people, no faces, no logos. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
증권사 돈을 빌려 산 주식으로 1,500만원을 벌었는데, 한 달 뒤 반대매매 한 번에 -2,500만원이 됐습니다.
빚을 낸 투자가 왜 위험한지 4가지로, 빚을 쓸 때 꼭 지켜야 할 기준을 5가지로 정리했습니다.

■ 이 영상에서 다루는 것
- 빚은 수익뿐 아니라 손실도 똑같이 키운다 (주가 -42%에 내 돈 -83%)
- 반대매매는 가장 나쁜 때에 가장 나쁜 가격으로 판다 (담보유지비율 140%, 금융감독원 분쟁 사례)
- 신용 이자는 주가와 상관없이 매일 쌓인다
- 하락장에서 신용 계좌가 더 크게 잃었다 (국내 계좌 460만 개 분석, 미국 레버리지 제한 연구)
- 빚투의 기준 5가지: 반대매매 가격 계산, 빌리는 한도, 담보용 현금, 빚부터 갚기, 미수 쓰지 않기

■ 챕터
0:00 사연: 빚투로 번 1,500만 원이 -2,500만 원
1:32 왜 빚을 내서 살까
2:32 문제 01 빚은 손실도 똑같이 키운다
3:02 문제 02 반대매매는 가장 나쁜 가격에 판다
4:01 문제 03 이자는 매일 쌓인다
4:26 문제 04 하락장에서 빚투 계좌가 더 크게 잃었다
5:23 기준 첫째: 반대매매 가격부터 계산
5:57 기준 둘째: 빌리는 돈은 내 돈의 일부만
6:32 기준 셋째: 넣을 현금을 따로 떼어 두기
6:56 기준 넷째: 수익이 나면 빚부터 갚기
7:24 기준 다섯째: 미수는 쓰지 않기
7:57 정리

■ 사연에 대해
이 영상의 사연은 실제 주가 흐름(SK하이닉스, 2026년 5~7월)을 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시입니다.

■ 출처
- SK하이닉스 일별 주가: https://finance.naver.com/item/sise_day.naver?code=000660
- 2026년 7월 28일 코스피 급락·서킷브레이커: https://www.seoul.co.kr/news/economy/securities/2026/07/28/20260728500215
- 2026년 7월 28일 급락 원인: https://m.news.nate.com/view/20260728n26673
- 2026년 7월 31일 반등: https://biz.heraldcorp.com/article/10830714
- 신용융자 잔고 사상 최대(6월 24일): https://biz.sbs.co.kr/amp/article/20000318902
- 증권사 10곳 반대매매 금액(1~6월): https://biz.heraldcorp.com/article/10822748
- 반대매매 절차(신용거래설명서): https://www.myasset.com/myasset/static/agreement/c_08_rule.pdf
- 금융감독원 반대매매 분쟁 사례: https://www.newspim.com/news/view/20260323000701
- 신용 이자율(2026년 5월): https://www.fnnews.com/news/202605111100001641
- 계좌 460만 개 분석: https://www.dt.co.kr/article/12052967
- Heimer & Simsek (2019), Should Retail Investors' Leverage Be Limited?: https://ideas.repec.org/a/eee/jfinec/v132y2019i3p1-21.html
- 미수 반대매매: https://www.fnnews.com/news/202606101746032705

■ 투자 유의 사항
이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
투자 판단과 책임은 투자자 본인에게 있습니다.

#주식 #빚투 #반대매매
```

**태그**: 빚투, 신용거래, 신용융자, 반대매매, 미수, 담보유지비율, 주식 손실, 주식, 주식 투자, 주식 초보, 주식 공부, 국내 주식, SK하이닉스, 코스피 폭락, 서킷브레이커

**고정 댓글**

```
빚을 내기 전에 이 두 가지부터 계산해 보세요.
1. 반대매매 가격 (내 돈만큼 빌리면 산 가격의 70%)
2. 담보가 부족할 때 넣을 수 있는 현금

여러분은 신용이나 미수를 써 본 적이 있나요? 그때 세워 둔 기준이 있었는지 댓글로 나눠 주세요.
※ 이 영상은 투자 권유가 아닙니다. 특정 종목 추천·리딩방 홍보 댓글은 삭제합니다.
```

## 4. 스토리보드

아직 없음 → 3단계에서 영상 코드(`video/src/episodes/bittu-2026-10/`)를 만들고 `node scripts/storyboard.mjs bittu-2026-10 ../<주제폴더>/out/bittu-2026-10`로 still을 렌더하면 여기에 붙는다.


## 5. 대본 (번호 = 대본 문장 번호)

**사연 파트**

1. 2026년 5월, SK하이닉스 주가가 한 달 만에 80% 넘게 올랐어요.
2. 이렇게 오르는 장에 제 돈 3천만 원만 넣기에는 너무 아깝더라고요.
3. 그래서 증권사에서 3천만 원을 빌려 6천만 원어치를 샀죠.
4. 산 주식을 담보로 증권사 돈을 빌리는 신용 거래였어요.
5. 6월 22일 주가가 290만 원을 넘으면서 수익이 1,500만 원이 됐어요.
6. 제 돈만 넣었다면 750만 원이었을 수익이 빚 덕분에 두 배가 된 거죠.
7. 하지만 빚은 수익만 두 배로 키우는 게 아니었습니다.
8. 7월 28일 저녁, 증권사에서 담보가 부족하다는 문자가 왔어요.
9. 추가로 넣을 돈은 없었어요.
10. 이틀 뒤 아침, 장이 열리자마자 제 주식이 전부 강제로 팔렸어요.
11. 빚을 갚고 남은 돈은 500만 원, -2,500만 원이었어요.
12. 7월 28일 하루에만 코스피가 10% 넘게, SK하이닉스는 15% 가까이 떨어졌더라고요.
13. 중국의 메모리 반도체 회사가 상장해 큰돈을 모았다는 소식에 AI 투자 걱정까지 겹쳤대요.
14. 그런데 강제로 팔린 바로 다음 날, 주가는 하루 만에 30% 가까이 올랐어요.
15. 수익을 두 배로 만들어 준 3천만 원의 빚이 제 돈까지 거의 다 가져가 버렸어요.
16. 빚만 없었어도 그 하루를 버틸 수 있었을 텐데요.

**진행자 파트**

17. 주가가 쭉쭉 오를 때면 많은 분들이 이런 생각을 하죠.
18. 조금만 빌렸다가 오르면 바로 갚으면 되지.
19. 내 돈만 넣기엔 이 상승장이 아까워.
20. 설마 반대매매까지 가겠어?
21. 이런 식으로 오르는 장에서는 빚의 무게가 잘 느껴지지 않습니다.
22. 실제로 6월 24일, 신용융자 잔고는 38조 6천억 원으로 사상 최대였습니다.
23. 개인 투자자가 증권사 돈을 빌려 산 주식이 그만큼 많았던 거죠.
24. 6월 한 달 증권사 10곳에서 신용 반대매매로 팔린 주식은 3,935억 원어치였습니다.
25. 1월보다 7배 가까이 늘어난 금액입니다.
26. 빚투가 몇몇 사람만의 이야기가 아니라는 뜻입니다.
27. 그럼 빚을 내서 하는 투자가 왜 위험한지 하나씩 짚어 보겠습니다.

> 🟨 [장면] 투자 권유가 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
> 사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
> 과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
> 투자 판단과 책임은 투자자 본인에게 있습니다.

**문제 분석 파트**

28. 첫 번째 문제는 빚이 수익뿐 아니라 손실도 똑같이 키운다는 것입니다.
29. 사연자의 주식이 팔린 날, 주가는 산 가격보다 42% 가까이 낮았습니다.
30. 그런데 사연자의 돈 3천만 원은 83%가 사라졌죠.
31. 빌린 3천만 원은 주가와 상관없이 그대로 갚아야 하기 때문입니다.
32. 내 돈과 같은 금액을 빌렸다면, 주가가 절반만 떨어져도 내 돈은 하나도 남지 않습니다.
33. 두 번째는 반대매매가 가장 나쁜 때에 가장 나쁜 가격으로 판다는 것입니다.
34. 증권사는 보통 주식 가치가 빌려준 돈의 140% 이상이 되도록 요구합니다.
35. 이 선 아래로 떨어지면 정해진 날까지 돈을 더 넣으라고 하죠.
36. 넣지 못하면 장이 열리자마자 주식을 팔아 빌려준 돈을 거둬 갑니다.
37. 팔 수량은 전날 종가보다 15~30% 낮은 가격을 기준으로 정합니다.
38. 그래서 모자란 돈보다 훨씬 많은 주식이 팔릴 수 있습니다.
39. 금융감독원이 소개한 사례에서는 모자란 담보가 201만 원이었습니다.
40. 그런데 주식 405주, 3,090만 원어치가 전부 팔렸죠.
41. 사연자처럼 다음 날 주가가 30% 가까이 올라도, 이미 팔린 주식은 돌아오지 않습니다.
42. 빚이 없었다면 기다릴지 말지를 스스로 정할 수 있었을 겁니다.
43. 세 번째는 이자가 주가와 상관없이 매일 쌓인다는 것입니다.
44. 2026년 5월 증권사 10곳의 신용 이자는 90일이 넘으면 평균 연 9.38%였습니다.
45. 이 금리로 3천만 원을 1년 빌리면 이자만 280만 원이 넘습니다.
46. 빌린 돈으로 산 부분은 1년에 9% 넘게 오르지 않으면 오히려 손해인 셈이죠.
47. 네 번째는 실제로 빚을 낸 투자자가 하락장에서 훨씬 크게 잃었다는 것입니다.
48. 국내 대형 증권사 두 곳의 개인 계좌 460만 개를 분석한 결과가 있습니다.
49. 2026년 3월 1일부터 9일까지 폭락장에서 신용을 쓴 계좌는 평균 19% 잃었습니다.
50. 신용을 쓰지 않은 계좌의 손실 8.2%보다 2.3배 컸죠.
51. 미국에서는 2010년 개인 외환 거래에 쓸 수 있는 빚의 한도를 줄인 적이 있습니다.
52. 그 뒤 빚을 많이 쓰던 투자자들의 손실이 40% 줄었다는 연구가 나왔죠.
53. 물론 빚 덕분에 크게 번 사람도 있습니다.
54. 사연자도 6월까지는 그랬죠.
55. 문제는 한 번의 폭락이 그동안 번 돈에 내 돈까지 한꺼번에 가져갈 수 있다는 겁니다.
56. 그렇다면 빚을 내서 투자할 때는 어떤 기준을 지켜야 할까요?

**올바른 방법 설명 파트**

57. 첫째, 빌리기 전에 반대매매가 되는 가격부터 계산하는 것입니다.
58. 내 돈만큼 빌렸다면, 주가가 30%만 떨어져도 담보가 140% 아래로 내려갑니다.
59. 사연자라면 233만 3천 원의 70%인 163만 3천 원이 그 가격입니다.
60. SK하이닉스는 6월 23일 하루에만 12% 넘게 떨어졌습니다.
61. 하루에 10% 넘게 움직이는 종목이라면 30%는 생각보다 가까운 거리입니다.
62. 둘째, 빌리는 돈은 내 돈의 일부로만 정하는 것입니다.
63. 예를 들어 내 돈의 20%까지만 빌린다고 정해 두는 겁니다.
64. 사연자가 3천만 원에 600만 원만 빌렸다면 어땠을까요?
65. 주가가 77% 떨어져야 반대매매 가격에 닿습니다.
66. 7월 30일 같은 폭락에도 주식은 강제로 팔리지 않았을 겁니다.
67. 물론 빌린 돈이 적으면 오를 때 수익도 그만큼 줄어듭니다.
68. 하지만 폭락 한 번에 계좌가 끝나지 않는다는 게 훨씬 중요합니다.
69. 셋째, 담보가 부족할 때 넣을 현금을 미리 떼어 두는 것입니다.
70. 문자를 받은 다음 날까지 600만 원을 넣었다면 담보는 다시 140%를 넘었습니다.
71. 그랬다면 주식이 강제로 팔리지 않고, 7월 31일의 반등도 함께 받았을 겁니다.
72. 넣을 현금이 없다면 그만큼 덜 빌리는 게 맞습니다.
73. 넷째, 수익이 나면 빚부터 갚는 것입니다.
74. 수익 1,500만 원이 난 6월 22일에 사연자가 빚부터 갚았다고 해 보겠습니다.
75. 3천만 원어치를 팔아 빌린 돈을 모두 갚는 거죠.
76. 남은 주식은 4,500만 원어치이고, 전부 사연자의 돈입니다.
77. 7월 폭락에도 강제로 팔리지 않았고, 7월 31일 손실은 350만 원 정도였을 겁니다.
78. -2,500만 원과 비교하면 2천만 원 넘게 차이가 나죠.
79. 다섯째, 미수는 쓰지 않는 것입니다.
80. 미수는 이틀 뒤 결제일까지 돈을 채워 넣기로 하고 외상으로 주식을 사는 것입니다.
81. 돈을 못 채우면 그다음 날 아침 바로 반대매매가 됩니다.
82. 그 뒤 30일 동안은 현금이 100% 있어야만 주식을 살 수 있죠.
83. 6월 한 달 증권사 10곳에서 미수 반대매매로 팔린 주식은 8,459억 원어치였습니다.
84. 며칠짜리 외상은 오래 들고 갈 주식을 사는 데 처음부터 맞지 않습니다.

**마무리**

85. 이렇게 해서 빚투가 위험한 이유와 빚을 쓸 때 지킬 기준을 알아보았습니다.
86. 빚을 내기 전에 반대매매가 되는 가격부터 계산해 보세요.
87. 성공 투자 하셨으면 좋겠습니다.
88. 감사합니다.


## 6. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
