# eonje-maesu-2026-10 업로드 시트

버전: v3.4 — 2026-10-18 — **기본 언어 en** — 제목·설명란(부호 + 아주 쉬운 영어, 결말 없음)·태그·챕터 이름·고정 댓글을 영어로, 한국어 제목은 언어별 ko, 언어별 설명은 모두 같은 쉬운 영어 · 오디오 언어 ko (사용자 지시 2026-10-18 "설명은 부호, 정말 간단한 영어로 간략하게 표현하도록 해봐 그리고 태그 같은 것도 영어로 하고 한국어로 쓰여진 곳은 정말 간단한 영어로 수정할 수 있어? 모든 영상").
(v3.3.1 — 2026-10-17 — 업로드 설정 '자막 올리기' = **언어별** (한국어 + 9개 언어 CC — 화면에는 굽지 않음, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") · 자막 대본 `subs/<영상ID>.<언어>.txt` 9개.)
(v3.3 — 2026-10-17 — 대본 v3.3 (티커 설명 (사용자 지시 2026-10-17 "일단 티커에 대한 설명도 추가해 예를 들어 'S&P500을 추종하는 ETF인 SPY' 이런식으로 다 수정해보고")) — 챕터·문장 수 다시.)
(v3.2 — 2026-10-17 — 대본 v3.2 (사용자가 붙인 ChatGPT 페르소나 검토 2차 '네 영상에 공통으로 반복되는 문제 5개'): 2번 설명란과 5번 언어별 설명 9개에 **재현 조건** 한 단락 (가격 자료·배당 처리·매수 날·무작위 추출 방법·ETF 보수) · 챕터 다시 계산.)
(v3.1 — 2026-10-17 — 대본 v3.1 (사용자가 붙인 ChatGPT 페르소나 검토 2026-10-17 '네 영상에 반복되는 문제 5개' — 경주 해설은 대표 장면만, 조건을 앞에서 분명히, 숫자와 뜻을 한 문장에, 말하는 금액은 어림(만 단위 하나), 한계에 결정 조건): 챕터 다시 계산 (문장 번호 바뀜) · 설명란·언어별 설명의 무작위 계좌 문구(같은 매도 규칙 · 매수 날짜만 무작위 · 기다린 날 수는 그 신호의 실제 기록에서 — 예전 "같은 횟수"는 정확하지 않아 뺌)와 넣지 않은 것(물가·현금 이자 · 성공률만 봄).)
(v3.0 — 2026-10-16 — 다시 만듦: 잣대 = 성공률(매수한 값보다 +5% 종가가 −2% 종가보다 먼저) · 비교 상대 = 신호 없이 무작위 날짜에 매수한 계좌 2천 개 · 자주 나오는 매수 신호 10가지 (`backtest/barrier/run.py` v2.0). 사용자 지시 2026-10-16 "그럼 신호 없이 무작위로 매수 했을 때랑 비교하는 거지? 그게 맞는거 같은데 그리고 m을 1~2%로 해야 엄격하게 봐서 성공 확률이 줄지 m은 내가 말한 범위에서 적절하게 정해서 영상 만들어봐". `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음.)
(v2.1 — 끝 값 비교·매도 = 산 뒤 최고 −10% — 커밋 28e1b7b. v1.0 — `stock/source/_old/eonje-maesu-2026-10-v1/upload.md`)
기준 파일: 대본 v3.3 (126문장) · SRT 문장 126 (추정 시각 — 오디오가 생기면 다시) · 결과 `backtest/barrier/results.json` · 올릴 영상 = 렌더 원본 `stock/out/eonje-maesu-2026-10/final_1080p.mp4` (오디오가 생긴 뒤 — 지금 있는 `preview_estimated_silent.mp4` 는 소리 없는 미리보기라 올리지 않음)

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json` — 업로드 도구 v1.7 이 채널이 다르면 올리지 않음)로 `python tools/youtube_upload.py stock eonje-maesu-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (기본 언어 en — 아주 쉬운 영어 · 한국어 제목 「매수 타이밍, 저점·RSI·신고가 신호는 2% 떨어지기 전 5% 오를 확률이 무작위 매수보다 높을까?」은 5번 ko 로)

```
When to buy? 10 buy signals vs random buys — +5% before −2%?
```

## 2. 설명란 (부호 + 아주 쉬운 영어 — 결말 없음 · 챕터 시각은 업로드 도구가 SRT 로 다시 계산)

```
Bought, and then the price fell? So… when should you buy?
10 popular buy signals vs random buys · SPY (S&P 500 ETF)
✓ win = close is +5% above the buy price first
✗ lose = close is −2% first
Sell the next day · buy again on the next signal
🎲 2,000 random accounts · same sell rule · random buy days
Jan 2016 → Oct 2026 · fee 0.25%

■ Chapters
0:00 When to buy?
0:28 1 First trading day of the month
1:26 2 New 20-day high
2:14 3 1-month momentum
2:51 4 Cross above 20-day average
3:33 5 Golden cross 5/20
4:19 6 Day after a −1% day
5:05 7 RSI under 40
5:54 8 VIX 20 or more
6:41 9 20-day high −5%
7:19 10 All-time high −5%
8:11 All 10 results
8:43 Other rules & periods
9:16 Summary
9:41 Limits

■ How
SPY daily close (split-adjusted) · Jan 4, 2016 → Oct 15, 2026
Signal = that day's close · buy = next day's close · no new buy while holding
−2% picked before the results (normal day ≈ 1.1%) · also checked: 1%, 1.5%, 1994–2015
Random accounts: wait days drawn from each signal's real record (seed 20261016 + n)
Returns with dividends · ETF fee is in the price
No tax, FX, inflation or cash interest · win rate only, not profit size
Code: AI-made Python (tested: no future data) · Voice: AI
Data: Yahoo Finance chart API (SPY, VIX)

Past ≠ future · Not investment advice
#SPY #backtest #WhenToBuy
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/eonje-maesu-2026-10/eonje-maesu-2026-10.txt stock/source/eonje-maesu-2026-10/eonje-maesu-2026-10.srt --chapters "1=언제 매수할까;7=1 매달 첫 거래일;18=2 20일 신고가 돌파;28=3 1개월 모멘텀;35=4 20일 이동평균선 돌파;43=5 골든 크로스 5·20일;53=6 하루 −1% 하락 다음 날;62=7 RSI 40 아래;72=8 공포지수 VIX 20 이상;81=9 20일 고점 −5%;89=10 최고 종가 −5%;99=10가지 결과;106=실패 기준·기간을 바꾸면;113=정리;119=이 실험의 한계"
```
- 2026-10-17 추정 시각(오디오 전, 대본 v3.3)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 올릴 때 오디오에 맞춘 SRT로 다시 계산해 2번 설명란에 넣는다.
- 챕터 이름에 결과를 쓰지 않는다 (진행 막대에 미리 보이므로). 번호는 영상에 나오는 순서 (장 카드의 노란 번호와 같음).

## 4. 태그 (영어)

```
SPY, S&P 500, when to buy, buy signal, market timing, RSI, VIX, moving average, golden cross, momentum, backtest, Python backtest, stock market, investing
```

## 5. 언어별 제목·설명 (localizations — ko + 8개 언어 제목, 설명은 모두 2번과 같은 쉬운 영어 · 기본 언어 en 은 1·2번)

`stock/guides/README.md` 2번의 9개 언어 (기본 언어 ko 는 1·2번). JSON — 업로드 도구가 그대로 읽는다 (고칠 때 따옴표·쉼표 주의). 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜). 만든 스크립트가 제목 100자 이하·`< >` 없음을 확인했다.

```
{
 "ko": {
  "title": "매수 타이밍, 저점·RSI·신고가 신호는 2% 떨어지기 전 5% 오를 확률이 무작위 매수보다 높을까?",
  "description": "Bought, and then the price fell? So… when should you buy?\n10 popular buy signals vs random buys · SPY (S&P 500 ETF)\n✓ win = close is +5% above the buy price first\n✗ lose = close is −2% first\nSell the next day · buy again on the next signal\n🎲 2,000 random accounts · same sell rule · random buy days\nJan 2016 → Oct 2026 · fee 0.25%\n\n■ Chapters\n0:00 When to buy?\n0:28 1 First trading day of the month\n1:26 2 New 20-day high\n2:14 3 1-month momentum\n2:51 4 Cross above 20-day average\n3:33 5 Golden cross 5/20\n4:19 6 Day after a −1% day\n5:05 7 RSI under 40\n5:54 8 VIX 20 or more\n6:41 9 20-day high −5%\n7:19 10 All-time high −5%\n8:11 All 10 results\n8:43 Other rules & periods\n9:16 Summary\n9:41 Limits\n\n■ How\nSPY daily close (split-adjusted) · Jan 4, 2016 → Oct 15, 2026\nSignal = that day's close · buy = next day's close · no new buy while holding\n−2% picked before the results (normal day ≈ 1.1%) · also checked: 1%, 1.5%, 1994–2015\nRandom accounts: wait days drawn from each signal's real record (seed 20261016 + n)\nReturns with dividends · ETF fee is in the price\nNo tax, FX, inflation or cash interest · win rate only, not profit size\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API (SPY, VIX)\n\nPast ≠ future · Not investment advice\n#SPY #backtest #WhenToBuy"
 },
 "hi": {
  "title": "कब खरीदें: क्या डिप, RSI और ब्रेकआउट संकेत रैंडम खरीद से ज़्यादा बार −2% से पहले +5% छूते हैं?",
  "description": "Bought, and then the price fell? So… when should you buy?\n10 popular buy signals vs random buys · SPY (S&P 500 ETF)\n✓ win = close is +5% above the buy price first\n✗ lose = close is −2% first\nSell the next day · buy again on the next signal\n🎲 2,000 random accounts · same sell rule · random buy days\nJan 2016 → Oct 2026 · fee 0.25%\n\n■ Chapters\n0:00 When to buy?\n0:28 1 First trading day of the month\n1:26 2 New 20-day high\n2:14 3 1-month momentum\n2:51 4 Cross above 20-day average\n3:33 5 Golden cross 5/20\n4:19 6 Day after a −1% day\n5:05 7 RSI under 40\n5:54 8 VIX 20 or more\n6:41 9 20-day high −5%\n7:19 10 All-time high −5%\n8:11 All 10 results\n8:43 Other rules & periods\n9:16 Summary\n9:41 Limits\n\n■ How\nSPY daily close (split-adjusted) · Jan 4, 2016 → Oct 15, 2026\nSignal = that day's close · buy = next day's close · no new buy while holding\n−2% picked before the results (normal day ≈ 1.1%) · also checked: 1%, 1.5%, 1994–2015\nRandom accounts: wait days drawn from each signal's real record (seed 20261016 + n)\nReturns with dividends · ETF fee is in the price\nNo tax, FX, inflation or cash interest · win rate only, not profit size\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API (SPY, VIX)\n\nPast ≠ future · Not investment advice\n#SPY #backtest #WhenToBuy"
 },
 "id": {
  "title": "Kapan beli: sinyal dip, RSI, breakout lebih sering naik 5% sebelum turun 2% dibanding beli acak?",
  "description": "Bought, and then the price fell? So… when should you buy?\n10 popular buy signals vs random buys · SPY (S&P 500 ETF)\n✓ win = close is +5% above the buy price first\n✗ lose = close is −2% first\nSell the next day · buy again on the next signal\n🎲 2,000 random accounts · same sell rule · random buy days\nJan 2016 → Oct 2026 · fee 0.25%\n\n■ Chapters\n0:00 When to buy?\n0:28 1 First trading day of the month\n1:26 2 New 20-day high\n2:14 3 1-month momentum\n2:51 4 Cross above 20-day average\n3:33 5 Golden cross 5/20\n4:19 6 Day after a −1% day\n5:05 7 RSI under 40\n5:54 8 VIX 20 or more\n6:41 9 20-day high −5%\n7:19 10 All-time high −5%\n8:11 All 10 results\n8:43 Other rules & periods\n9:16 Summary\n9:41 Limits\n\n■ How\nSPY daily close (split-adjusted) · Jan 4, 2016 → Oct 15, 2026\nSignal = that day's close · buy = next day's close · no new buy while holding\n−2% picked before the results (normal day ≈ 1.1%) · also checked: 1%, 1.5%, 1994–2015\nRandom accounts: wait days drawn from each signal's real record (seed 20261016 + n)\nReturns with dividends · ETF fee is in the price\nNo tax, FX, inflation or cash interest · win rate only, not profit size\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API (SPY, VIX)\n\nPast ≠ future · Not investment advice\n#SPY #backtest #WhenToBuy"
 },
 "pt": {
  "title": "Quando comprar: queda, RSI e rompimento sobem 5% antes de cair 2% mais que compras aleatórias?",
  "description": "Bought, and then the price fell? So… when should you buy?\n10 popular buy signals vs random buys · SPY (S&P 500 ETF)\n✓ win = close is +5% above the buy price first\n✗ lose = close is −2% first\nSell the next day · buy again on the next signal\n🎲 2,000 random accounts · same sell rule · random buy days\nJan 2016 → Oct 2026 · fee 0.25%\n\n■ Chapters\n0:00 When to buy?\n0:28 1 First trading day of the month\n1:26 2 New 20-day high\n2:14 3 1-month momentum\n2:51 4 Cross above 20-day average\n3:33 5 Golden cross 5/20\n4:19 6 Day after a −1% day\n5:05 7 RSI under 40\n5:54 8 VIX 20 or more\n6:41 9 20-day high −5%\n7:19 10 All-time high −5%\n8:11 All 10 results\n8:43 Other rules & periods\n9:16 Summary\n9:41 Limits\n\n■ How\nSPY daily close (split-adjusted) · Jan 4, 2016 → Oct 15, 2026\nSignal = that day's close · buy = next day's close · no new buy while holding\n−2% picked before the results (normal day ≈ 1.1%) · also checked: 1%, 1.5%, 1994–2015\nRandom accounts: wait days drawn from each signal's real record (seed 20261016 + n)\nReturns with dividends · ETF fee is in the price\nNo tax, FX, inflation or cash interest · win rate only, not profit size\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API (SPY, VIX)\n\nPast ≠ future · Not investment advice\n#SPY #backtest #WhenToBuy"
 },
 "es-419": {
  "title": "¿Cuándo comprar? ¿Caída, RSI y ruptura suben 5% antes de caer 2% más seguido que comprar al azar?",
  "description": "Bought, and then the price fell? So… when should you buy?\n10 popular buy signals vs random buys · SPY (S&P 500 ETF)\n✓ win = close is +5% above the buy price first\n✗ lose = close is −2% first\nSell the next day · buy again on the next signal\n🎲 2,000 random accounts · same sell rule · random buy days\nJan 2016 → Oct 2026 · fee 0.25%\n\n■ Chapters\n0:00 When to buy?\n0:28 1 First trading day of the month\n1:26 2 New 20-day high\n2:14 3 1-month momentum\n2:51 4 Cross above 20-day average\n3:33 5 Golden cross 5/20\n4:19 6 Day after a −1% day\n5:05 7 RSI under 40\n5:54 8 VIX 20 or more\n6:41 9 20-day high −5%\n7:19 10 All-time high −5%\n8:11 All 10 results\n8:43 Other rules & periods\n9:16 Summary\n9:41 Limits\n\n■ How\nSPY daily close (split-adjusted) · Jan 4, 2016 → Oct 15, 2026\nSignal = that day's close · buy = next day's close · no new buy while holding\n−2% picked before the results (normal day ≈ 1.1%) · also checked: 1%, 1.5%, 1994–2015\nRandom accounts: wait days drawn from each signal's real record (seed 20261016 + n)\nReturns with dividends · ETF fee is in the price\nNo tax, FX, inflation or cash interest · win rate only, not profit size\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API (SPY, VIX)\n\nPast ≠ future · Not investment advice\n#SPY #backtest #WhenToBuy"
 },
 "ja": {
  "title": "買うタイミング：押し目・RSI・高値更新のシグナルは、ランダムに買うより−2%の前に+5%に届く確率が高い？",
  "description": "Bought, and then the price fell? So… when should you buy?\n10 popular buy signals vs random buys · SPY (S&P 500 ETF)\n✓ win = close is +5% above the buy price first\n✗ lose = close is −2% first\nSell the next day · buy again on the next signal\n🎲 2,000 random accounts · same sell rule · random buy days\nJan 2016 → Oct 2026 · fee 0.25%\n\n■ Chapters\n0:00 When to buy?\n0:28 1 First trading day of the month\n1:26 2 New 20-day high\n2:14 3 1-month momentum\n2:51 4 Cross above 20-day average\n3:33 5 Golden cross 5/20\n4:19 6 Day after a −1% day\n5:05 7 RSI under 40\n5:54 8 VIX 20 or more\n6:41 9 20-day high −5%\n7:19 10 All-time high −5%\n8:11 All 10 results\n8:43 Other rules & periods\n9:16 Summary\n9:41 Limits\n\n■ How\nSPY daily close (split-adjusted) · Jan 4, 2016 → Oct 15, 2026\nSignal = that day's close · buy = next day's close · no new buy while holding\n−2% picked before the results (normal day ≈ 1.1%) · also checked: 1%, 1.5%, 1994–2015\nRandom accounts: wait days drawn from each signal's real record (seed 20261016 + n)\nReturns with dividends · ETF fee is in the price\nNo tax, FX, inflation or cash interest · win rate only, not profit size\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API (SPY, VIX)\n\nPast ≠ future · Not investment advice\n#SPY #backtest #WhenToBuy"
 },
 "de": {
  "title": "Wann kaufen: Erreichen Dip-, RSI- und Ausbruchssignale öfter +5 % vor −2 % als zufällige Käufe?",
  "description": "Bought, and then the price fell? So… when should you buy?\n10 popular buy signals vs random buys · SPY (S&P 500 ETF)\n✓ win = close is +5% above the buy price first\n✗ lose = close is −2% first\nSell the next day · buy again on the next signal\n🎲 2,000 random accounts · same sell rule · random buy days\nJan 2016 → Oct 2026 · fee 0.25%\n\n■ Chapters\n0:00 When to buy?\n0:28 1 First trading day of the month\n1:26 2 New 20-day high\n2:14 3 1-month momentum\n2:51 4 Cross above 20-day average\n3:33 5 Golden cross 5/20\n4:19 6 Day after a −1% day\n5:05 7 RSI under 40\n5:54 8 VIX 20 or more\n6:41 9 20-day high −5%\n7:19 10 All-time high −5%\n8:11 All 10 results\n8:43 Other rules & periods\n9:16 Summary\n9:41 Limits\n\n■ How\nSPY daily close (split-adjusted) · Jan 4, 2016 → Oct 15, 2026\nSignal = that day's close · buy = next day's close · no new buy while holding\n−2% picked before the results (normal day ≈ 1.1%) · also checked: 1%, 1.5%, 1994–2015\nRandom accounts: wait days drawn from each signal's real record (seed 20261016 + n)\nReturns with dividends · ETF fee is in the price\nNo tax, FX, inflation or cash interest · win rate only, not profit size\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API (SPY, VIX)\n\nPast ≠ future · Not investment advice\n#SPY #backtest #WhenToBuy"
 },
 "vi": {
  "title": "Khi nào mua: tín hiệu giảm sâu, RSI, phá đỉnh có lên 5% trước khi xuống 2% nhiều hơn mua ngẫu nhiên?",
  "description": "Bought, and then the price fell? So… when should you buy?\n10 popular buy signals vs random buys · SPY (S&P 500 ETF)\n✓ win = close is +5% above the buy price first\n✗ lose = close is −2% first\nSell the next day · buy again on the next signal\n🎲 2,000 random accounts · same sell rule · random buy days\nJan 2016 → Oct 2026 · fee 0.25%\n\n■ Chapters\n0:00 When to buy?\n0:28 1 First trading day of the month\n1:26 2 New 20-day high\n2:14 3 1-month momentum\n2:51 4 Cross above 20-day average\n3:33 5 Golden cross 5/20\n4:19 6 Day after a −1% day\n5:05 7 RSI under 40\n5:54 8 VIX 20 or more\n6:41 9 20-day high −5%\n7:19 10 All-time high −5%\n8:11 All 10 results\n8:43 Other rules & periods\n9:16 Summary\n9:41 Limits\n\n■ How\nSPY daily close (split-adjusted) · Jan 4, 2016 → Oct 15, 2026\nSignal = that day's close · buy = next day's close · no new buy while holding\n−2% picked before the results (normal day ≈ 1.1%) · also checked: 1%, 1.5%, 1994–2015\nRandom accounts: wait days drawn from each signal's real record (seed 20261016 + n)\nReturns with dividends · ETF fee is in the price\nNo tax, FX, inflation or cash interest · win rate only, not profit size\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API (SPY, VIX)\n\nPast ≠ future · Not investment advice\n#SPY #backtest #WhenToBuy"
 },
 "tr": {
  "title": "Ne zaman almalı: düşüş, RSI ve kırılım sinyali, rastgele alımdan sık mı %2 düşmeden %5 çıkar?",
  "description": "Bought, and then the price fell? So… when should you buy?\n10 popular buy signals vs random buys · SPY (S&P 500 ETF)\n✓ win = close is +5% above the buy price first\n✗ lose = close is −2% first\nSell the next day · buy again on the next signal\n🎲 2,000 random accounts · same sell rule · random buy days\nJan 2016 → Oct 2026 · fee 0.25%\n\n■ Chapters\n0:00 When to buy?\n0:28 1 First trading day of the month\n1:26 2 New 20-day high\n2:14 3 1-month momentum\n2:51 4 Cross above 20-day average\n3:33 5 Golden cross 5/20\n4:19 6 Day after a −1% day\n5:05 7 RSI under 40\n5:54 8 VIX 20 or more\n6:41 9 20-day high −5%\n7:19 10 All-time high −5%\n8:11 All 10 results\n8:43 Other rules & periods\n9:16 Summary\n9:41 Limits\n\n■ How\nSPY daily close (split-adjusted) · Jan 4, 2016 → Oct 15, 2026\nSignal = that day's close · buy = next day's close · no new buy while holding\n−2% picked before the results (normal day ≈ 1.1%) · also checked: 1%, 1.5%, 1994–2015\nRandom accounts: wait days drawn from each signal's real record (seed 20261016 + n)\nReturns with dividends · ETF fee is in the price\nNo tax, FX, inflation or cash interest · win rate only, not profit size\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API (SPY, VIX)\n\nPast ≠ future · Not investment advice\n#SPY #backtest #WhenToBuy"
 }
}
```

## 6. 고정 댓글 (아주 쉬운 영어)

```
Which buy signal do you use? Do you think it beats random buying?
Give us your next idea to test with a backtest 👇
(Info only · not investment advice)
```

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올리고 **1시간 뒤 예약 공개** (`--publish-at +1h`) |
| 썸네일 | `thumbnails/thumbnail_1.*` (본안 — 글자 없음). 공개 뒤 '테스트 및 비교'에 thumbnail_1~3 |
| 기본 언어 | en (제목·설명·태그 = 부호 + 아주 쉬운 영어 — 한국어 제목은 언어별 ko) |
| 오디오 언어 | ko (내레이션 — 업로드 도구 v1.13) |
| 자막 올리기 | **언어별** (한국어 + en·hi·id·pt·es-419·ja·de·vi·tr — 화면에는 굽지 않고 CC 로, `subs/` 대본 → 오디오 뒤 `python3 tools/subs_tool.py build stock eonje-maesu-2026-10` · 업로드 도구 v1.12 가 자막 하나 400단위 — 할당량이 모자라면 `--captions-only` 로 다음 날, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 (내레이션) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 (전 세계 대상) |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — 사용자 지시 2026-10-11) |

## 8. 점검

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과(무작위보다 높은 신호가 있었는지·성공률·순위)를 쓰지 않았다. 결과는 영상 각 장의 끝과 '10가지 결과'(s141~)에서만.
- 설명란·언어별 설명의 숫자(2016-01-04·2026-10-15·5%·2%·0.25%·2천 개·1.1%·1%·1.5%·1994~2015·20·21·5·14·40·30·1%)는 대본·`backtest/barrier/results.json`·`run.py` 설정에 있는 것만 썼다 (하루 보통 움직임 1.1% = results.json choose_m.daily_std 1.12%).
- 제목 56자 · 언어별 제목 54~100자 (모두 100자 이하) · `< >` 없음 — `python tools/youtube_upload.py stock eonje-maesu-2026-10 --dry-run` 으로 확인.
- 사다 → 매수, 팔다 → 매도.

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, 시청 지속 그래프에서 크게 떨어지는 장(1~10), **나라·언어별 조회수**
