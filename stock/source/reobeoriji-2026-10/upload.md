# reobeoriji-2026-10 업로드 시트

버전: v1.5 — 2026-10-18 — **기본 언어 en** — 제목·설명란(부호 + 아주 쉬운 영어, 결말 없음)·태그·챕터 이름·고정 댓글을 영어로, 한국어 제목은 언어별 ko, 언어별 설명은 모두 같은 쉬운 영어 · 오디오 언어 ko (사용자 지시 2026-10-18 "설명은 부호, 정말 간단한 영어로 간략하게 표현하도록 해봐 그리고 태그 같은 것도 영어로 하고 한국어로 쓰여진 곳은 정말 간단한 영어로 수정할 수 있어? 모든 영상").
(v1.4.1 — 2026-10-17 — 업로드 설정 '자막 올리기' = **언어별** (한국어 + 9개 언어 CC — 화면에는 굽지 않음, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") · 자막 대본 `subs/<영상ID>.<언어>.txt` 9개.)
(v1.4 — 2026-10-17 — 대본 v1.4 (티커 설명 (사용자 지시 2026-10-17 "일단 티커에 대한 설명도 추가해 예를 들어 'S&P500을 추종하는 ETF인 SPY' 이런식으로 다 수정해보고")) — 챕터·문장 수 다시.)
(v1.3 — 2026-10-17 — 대본 v1.3 (사용자가 붙인 ChatGPT 페르소나 검토 2차 '네 영상에 공통으로 반복되는 문제 5개'): 2번 설명란과 5번 언어별 설명 9개에 **재현 조건** 한 단락 (가격 자료·배당 처리·매수 날·보정 기간·ETF 보수) · 챕터 다시 계산.)
(v1.2 — 2026-10-17 — 대본 v1.2 (사용자가 붙인 ChatGPT 페르소나 검토 2026-10-17 '네 영상에 반복되는 문제 5개' — 경주 해설은 대표 장면만, 조건을 앞에서 분명히, 숫자와 뜻을 한 문장에, 말하는 금액은 어림(만 단위 하나), 한계에 결정 조건): 챕터 다시 계산 (문장 번호 바뀜).)
(v1.1 — 2026-10-17 — 대본 v1.1 (도입 + 규칙 약 24초 — 사용자 지시 2026-10-17 "야 너 내가 테스트 들어가지 전 도입 및 규칙 설명 30초 넘기지 말라고 했잖아 근데 왜 안지켜 다시 수정해"): 챕터 다시 계산 — 규칙 챕터는 첫 챕터에 합침(10초 미만이 될 수 있어서), 설명 챕터는 결과 뒤. (v1.0 — 2026-10-16 — 최초 (주식 4번 레버리지 1·2·3배 — `backtest/run.py` v1.0). 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐". `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음.))
기준 파일: 대본 v1.4 (102문장) · SRT 문장 102 (추정 시각 — 오디오가 생기면 다시) · 결과 `backtest/results.json` · 올릴 영상 = 렌더 원본 `stock/out/reobeoriji-2026-10/final_1080p.mp4` (오디오가 생긴 뒤 — 지금 있는 `preview_estimated_silent.mp4` 는 소리 없는 미리보기라 올리지 않음)

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json`)로 `python tools/youtube_upload.py stock reobeoriji-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (기본 언어 en — 아주 쉬운 영어 · 한국어 제목 「레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까?」은 5번 ko 로)

```
3× leverage for 27 years: $500 a month in QQQ vs QLD vs TQQQ — more money?
```

## 2. 설명란 (부호 + 아주 쉬운 영어 — 결말 없음 · 챕터 시각은 업로드 도구가 SRT 로 다시 계산)

```
QLD (2×) and TQQQ (3×) follow the Nasdaq-100. Buy every month for years — far more money? And in a crash? 📉
QQQ (1×) vs 2× vs 3×
$500 each month · first trading day · Apr 1999 (dot-com crash) → Oct 2026 · fee 0.25%
Chart: one step on the scale = ×10
Watch the 3 accounts, day by day.

■ Chapters
0:00 Leverage for years?
0:27 From 1999, day by day
1:19 The 2008 crisis and after
2:09 2022: a long fall
2:43 27-year result
3:28 Daily reset, explained
4:11 One lump sum?
4:52 Other start months
5:44 2×/3× math vs real QLD/TQQQ
6:54 Summary
7:24 Limits

■ How
QQQ, QLD, TQQQ daily close + payouts (split-adjusted) · 13-week T-bill rate · Mar 10, 1999 → Oct 15, 2026
1× = QQQ with dividends
2× / 3× = daily Nasdaq-100 return × 2 / × 3 − fee 0.95% − borrowed part × (T-bill + 1.02%)
1.02% set once so 2× = real QLD (Jun 21, 2006 → Oct 15, 2026) · same math: TQQQ 0.57% / year below real
1999–2010 values for 2× and 3× are calculated
Also checked: one $10,000 buy at the start · other start months (211 × 10 years, 31 × 25 years) · real QQQ/QLD/TQQQ from Mar 2010 · +10% / −10% example · 2018
No tax or FX
Code: AI-made Python (tested: no future data) · Voice: AI
Data: Yahoo Finance chart API

Past ≠ future · Not investment advice
#TQQQ #QQQ #LeveragedETF
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/reobeoriji-2026-10/reobeoriji-2026-10.txt stock/source/reobeoriji-2026-10/reobeoriji-2026-10.srt --chapters "1=레버리지, 오래 모으면?;6=1999년부터 날짜를 흘려 보면;18=2008년 금융위기와 그 뒤;27=2022년 긴 하락;34=27년 결과;43=매일 배수를 맞춘다는 것;53=처음에 한 번만 넣었다면;62=시작한 달을 바꾸면;73=2·3배 계산과 실제 QLD·TQQQ;88=정리;95=이 실험의 한계"
```
- 2026-10-17 추정 시각(오디오 전, 대본 v1.4)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 오디오에 맞춘 SRT로 다시 계산한다. 챕터 이름에 결과를 쓰지 않는다.

## 4. 태그 (영어)

```
TQQQ, QLD, QQQ, leveraged ETF, 3x leverage, 2x leverage, Nasdaq 100, dot com crash, volatility decay, dollar cost averaging, backtest, Python backtest, investing
```

## 5. 언어별 제목·설명 (localizations — ko + 8개 언어 제목, 설명은 모두 2번과 같은 쉬운 영어 · 기본 언어 en 은 1·2번)

JSON — 업로드 도구가 그대로 읽는다. 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜).

```
{
 "ko": {
  "title": "레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까?",
  "description": "QLD (2×) and TQQQ (3×) follow the Nasdaq-100. Buy every month for years — far more money? And in a crash? 📉\nQQQ (1×) vs 2× vs 3×\n$500 each month · first trading day · Apr 1999 (dot-com crash) → Oct 2026 · fee 0.25%\nChart: one step on the scale = ×10\nWatch the 3 accounts, day by day.\n\n■ Chapters\n0:00 Leverage for years?\n0:27 From 1999, day by day\n1:19 The 2008 crisis and after\n2:09 2022: a long fall\n2:43 27-year result\n3:28 Daily reset, explained\n4:11 One lump sum?\n4:52 Other start months\n5:44 2×/3× math vs real QLD/TQQQ\n6:54 Summary\n7:24 Limits\n\n■ How\nQQQ, QLD, TQQQ daily close + payouts (split-adjusted) · 13-week T-bill rate · Mar 10, 1999 → Oct 15, 2026\n1× = QQQ with dividends\n2× / 3× = daily Nasdaq-100 return × 2 / × 3 − fee 0.95% − borrowed part × (T-bill + 1.02%)\n1.02% set once so 2× = real QLD (Jun 21, 2006 → Oct 15, 2026) · same math: TQQQ 0.57% / year below real\n1999–2010 values for 2× and 3× are calculated\nAlso checked: one $10,000 buy at the start · other start months (211 × 10 years, 31 × 25 years) · real QQQ/QLD/TQQQ from Mar 2010 · +10% / −10% example · 2018\nNo tax or FX\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#TQQQ #QQQ #LeveragedETF"
 },
 "hi": {
  "title": "डॉट-कॉम गिरावट से लीवरेज ETF: 27 साल हर महीने QLD·TQQQ खरीदें तो क्या 1x QQQ से ज़्यादा बचेगा?",
  "description": "QLD (2×) and TQQQ (3×) follow the Nasdaq-100. Buy every month for years — far more money? And in a crash? 📉\nQQQ (1×) vs 2× vs 3×\n$500 each month · first trading day · Apr 1999 (dot-com crash) → Oct 2026 · fee 0.25%\nChart: one step on the scale = ×10\nWatch the 3 accounts, day by day.\n\n■ Chapters\n0:00 Leverage for years?\n0:27 From 1999, day by day\n1:19 The 2008 crisis and after\n2:09 2022: a long fall\n2:43 27-year result\n3:28 Daily reset, explained\n4:11 One lump sum?\n4:52 Other start months\n5:44 2×/3× math vs real QLD/TQQQ\n6:54 Summary\n7:24 Limits\n\n■ How\nQQQ, QLD, TQQQ daily close + payouts (split-adjusted) · 13-week T-bill rate · Mar 10, 1999 → Oct 15, 2026\n1× = QQQ with dividends\n2× / 3× = daily Nasdaq-100 return × 2 / × 3 − fee 0.95% − borrowed part × (T-bill + 1.02%)\n1.02% set once so 2× = real QLD (Jun 21, 2006 → Oct 15, 2026) · same math: TQQQ 0.57% / year below real\n1999–2010 values for 2× and 3× are calculated\nAlso checked: one $10,000 buy at the start · other start months (211 × 10 years, 31 × 25 years) · real QQQ/QLD/TQQQ from Mar 2010 · +10% / −10% example · 2018\nNo tax or FX\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#TQQQ #QQQ #LeveragedETF"
 },
 "id": {
  "title": "ETF leverage sejak krisis dot-com: beli QLD·TQQQ tiap bulan 27 tahun, sisa lebih dari 1x QQQ?",
  "description": "QLD (2×) and TQQQ (3×) follow the Nasdaq-100. Buy every month for years — far more money? And in a crash? 📉\nQQQ (1×) vs 2× vs 3×\n$500 each month · first trading day · Apr 1999 (dot-com crash) → Oct 2026 · fee 0.25%\nChart: one step on the scale = ×10\nWatch the 3 accounts, day by day.\n\n■ Chapters\n0:00 Leverage for years?\n0:27 From 1999, day by day\n1:19 The 2008 crisis and after\n2:09 2022: a long fall\n2:43 27-year result\n3:28 Daily reset, explained\n4:11 One lump sum?\n4:52 Other start months\n5:44 2×/3× math vs real QLD/TQQQ\n6:54 Summary\n7:24 Limits\n\n■ How\nQQQ, QLD, TQQQ daily close + payouts (split-adjusted) · 13-week T-bill rate · Mar 10, 1999 → Oct 15, 2026\n1× = QQQ with dividends\n2× / 3× = daily Nasdaq-100 return × 2 / × 3 − fee 0.95% − borrowed part × (T-bill + 1.02%)\n1.02% set once so 2× = real QLD (Jun 21, 2006 → Oct 15, 2026) · same math: TQQQ 0.57% / year below real\n1999–2010 values for 2× and 3× are calculated\nAlso checked: one $10,000 buy at the start · other start months (211 × 10 years, 31 × 25 years) · real QQQ/QLD/TQQQ from Mar 2010 · +10% / −10% example · 2018\nNo tax or FX\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#TQQQ #QQQ #LeveragedETF"
 },
 "pt": {
  "title": "ETFs alavancados desde a bolha pontocom: comprar QLD e TQQQ todo mês por 27 anos rende mais que QQQ?",
  "description": "QLD (2×) and TQQQ (3×) follow the Nasdaq-100. Buy every month for years — far more money? And in a crash? 📉\nQQQ (1×) vs 2× vs 3×\n$500 each month · first trading day · Apr 1999 (dot-com crash) → Oct 2026 · fee 0.25%\nChart: one step on the scale = ×10\nWatch the 3 accounts, day by day.\n\n■ Chapters\n0:00 Leverage for years?\n0:27 From 1999, day by day\n1:19 The 2008 crisis and after\n2:09 2022: a long fall\n2:43 27-year result\n3:28 Daily reset, explained\n4:11 One lump sum?\n4:52 Other start months\n5:44 2×/3× math vs real QLD/TQQQ\n6:54 Summary\n7:24 Limits\n\n■ How\nQQQ, QLD, TQQQ daily close + payouts (split-adjusted) · 13-week T-bill rate · Mar 10, 1999 → Oct 15, 2026\n1× = QQQ with dividends\n2× / 3× = daily Nasdaq-100 return × 2 / × 3 − fee 0.95% − borrowed part × (T-bill + 1.02%)\n1.02% set once so 2× = real QLD (Jun 21, 2006 → Oct 15, 2026) · same math: TQQQ 0.57% / year below real\n1999–2010 values for 2× and 3× are calculated\nAlso checked: one $10,000 buy at the start · other start months (211 × 10 years, 31 × 25 years) · real QQQ/QLD/TQQQ from Mar 2010 · +10% / −10% example · 2018\nNo tax or FX\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#TQQQ #QQQ #LeveragedETF"
 },
 "es-419": {
  "title": "ETF apalancados desde la burbuja puntocom: ¿comprar QLD y TQQQ cada mes 27 años deja más que QQQ?",
  "description": "QLD (2×) and TQQQ (3×) follow the Nasdaq-100. Buy every month for years — far more money? And in a crash? 📉\nQQQ (1×) vs 2× vs 3×\n$500 each month · first trading day · Apr 1999 (dot-com crash) → Oct 2026 · fee 0.25%\nChart: one step on the scale = ×10\nWatch the 3 accounts, day by day.\n\n■ Chapters\n0:00 Leverage for years?\n0:27 From 1999, day by day\n1:19 The 2008 crisis and after\n2:09 2022: a long fall\n2:43 27-year result\n3:28 Daily reset, explained\n4:11 One lump sum?\n4:52 Other start months\n5:44 2×/3× math vs real QLD/TQQQ\n6:54 Summary\n7:24 Limits\n\n■ How\nQQQ, QLD, TQQQ daily close + payouts (split-adjusted) · 13-week T-bill rate · Mar 10, 1999 → Oct 15, 2026\n1× = QQQ with dividends\n2× / 3× = daily Nasdaq-100 return × 2 / × 3 − fee 0.95% − borrowed part × (T-bill + 1.02%)\n1.02% set once so 2× = real QLD (Jun 21, 2006 → Oct 15, 2026) · same math: TQQQ 0.57% / year below real\n1999–2010 values for 2× and 3× are calculated\nAlso checked: one $10,000 buy at the start · other start months (211 × 10 years, 31 × 25 years) · real QQQ/QLD/TQQQ from Mar 2010 · +10% / −10% example · 2018\nNo tax or FX\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#TQQQ #QQQ #LeveragedETF"
 },
 "ja": {
  "title": "レバレッジETF、ITバブル崩壊から27年毎月積み立てると、QLD・TQQQは1倍のQQQより多く残る？",
  "description": "QLD (2×) and TQQQ (3×) follow the Nasdaq-100. Buy every month for years — far more money? And in a crash? 📉\nQQQ (1×) vs 2× vs 3×\n$500 each month · first trading day · Apr 1999 (dot-com crash) → Oct 2026 · fee 0.25%\nChart: one step on the scale = ×10\nWatch the 3 accounts, day by day.\n\n■ Chapters\n0:00 Leverage for years?\n0:27 From 1999, day by day\n1:19 The 2008 crisis and after\n2:09 2022: a long fall\n2:43 27-year result\n3:28 Daily reset, explained\n4:11 One lump sum?\n4:52 Other start months\n5:44 2×/3× math vs real QLD/TQQQ\n6:54 Summary\n7:24 Limits\n\n■ How\nQQQ, QLD, TQQQ daily close + payouts (split-adjusted) · 13-week T-bill rate · Mar 10, 1999 → Oct 15, 2026\n1× = QQQ with dividends\n2× / 3× = daily Nasdaq-100 return × 2 / × 3 − fee 0.95% − borrowed part × (T-bill + 1.02%)\n1.02% set once so 2× = real QLD (Jun 21, 2006 → Oct 15, 2026) · same math: TQQQ 0.57% / year below real\n1999–2010 values for 2× and 3× are calculated\nAlso checked: one $10,000 buy at the start · other start months (211 × 10 years, 31 × 25 years) · real QQQ/QLD/TQQQ from Mar 2010 · +10% / −10% example · 2018\nNo tax or FX\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#TQQQ #QQQ #LeveragedETF"
 },
 "de": {
  "title": "Hebel-ETFs ab dem Dotcom-Crash: QLD und TQQQ 27 Jahre monatlich kaufen – mehr als 1x QQQ?",
  "description": "QLD (2×) and TQQQ (3×) follow the Nasdaq-100. Buy every month for years — far more money? And in a crash? 📉\nQQQ (1×) vs 2× vs 3×\n$500 each month · first trading day · Apr 1999 (dot-com crash) → Oct 2026 · fee 0.25%\nChart: one step on the scale = ×10\nWatch the 3 accounts, day by day.\n\n■ Chapters\n0:00 Leverage for years?\n0:27 From 1999, day by day\n1:19 The 2008 crisis and after\n2:09 2022: a long fall\n2:43 27-year result\n3:28 Daily reset, explained\n4:11 One lump sum?\n4:52 Other start months\n5:44 2×/3× math vs real QLD/TQQQ\n6:54 Summary\n7:24 Limits\n\n■ How\nQQQ, QLD, TQQQ daily close + payouts (split-adjusted) · 13-week T-bill rate · Mar 10, 1999 → Oct 15, 2026\n1× = QQQ with dividends\n2× / 3× = daily Nasdaq-100 return × 2 / × 3 − fee 0.95% − borrowed part × (T-bill + 1.02%)\n1.02% set once so 2× = real QLD (Jun 21, 2006 → Oct 15, 2026) · same math: TQQQ 0.57% / year below real\n1999–2010 values for 2× and 3× are calculated\nAlso checked: one $10,000 buy at the start · other start months (211 × 10 years, 31 × 25 years) · real QQQ/QLD/TQQQ from Mar 2010 · +10% / −10% example · 2018\nNo tax or FX\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#TQQQ #QQQ #LeveragedETF"
 },
 "vi": {
  "title": "ETF đòn bẩy từ bong bóng dot-com: mua QLD, TQQQ mỗi tháng suốt 27 năm có hơn QQQ 1x không?",
  "description": "QLD (2×) and TQQQ (3×) follow the Nasdaq-100. Buy every month for years — far more money? And in a crash? 📉\nQQQ (1×) vs 2× vs 3×\n$500 each month · first trading day · Apr 1999 (dot-com crash) → Oct 2026 · fee 0.25%\nChart: one step on the scale = ×10\nWatch the 3 accounts, day by day.\n\n■ Chapters\n0:00 Leverage for years?\n0:27 From 1999, day by day\n1:19 The 2008 crisis and after\n2:09 2022: a long fall\n2:43 27-year result\n3:28 Daily reset, explained\n4:11 One lump sum?\n4:52 Other start months\n5:44 2×/3× math vs real QLD/TQQQ\n6:54 Summary\n7:24 Limits\n\n■ How\nQQQ, QLD, TQQQ daily close + payouts (split-adjusted) · 13-week T-bill rate · Mar 10, 1999 → Oct 15, 2026\n1× = QQQ with dividends\n2× / 3× = daily Nasdaq-100 return × 2 / × 3 − fee 0.95% − borrowed part × (T-bill + 1.02%)\n1.02% set once so 2× = real QLD (Jun 21, 2006 → Oct 15, 2026) · same math: TQQQ 0.57% / year below real\n1999–2010 values for 2× and 3× are calculated\nAlso checked: one $10,000 buy at the start · other start months (211 × 10 years, 31 × 25 years) · real QQQ/QLD/TQQQ from Mar 2010 · +10% / −10% example · 2018\nNo tax or FX\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#TQQQ #QQQ #LeveragedETF"
 },
 "tr": {
  "title": "Dotcom çöküşünden kaldıraçlı ETF: 27 yıl her ay QLD ve TQQQ almak 1x QQQ'dan fazla bırakır mı?",
  "description": "QLD (2×) and TQQQ (3×) follow the Nasdaq-100. Buy every month for years — far more money? And in a crash? 📉\nQQQ (1×) vs 2× vs 3×\n$500 each month · first trading day · Apr 1999 (dot-com crash) → Oct 2026 · fee 0.25%\nChart: one step on the scale = ×10\nWatch the 3 accounts, day by day.\n\n■ Chapters\n0:00 Leverage for years?\n0:27 From 1999, day by day\n1:19 The 2008 crisis and after\n2:09 2022: a long fall\n2:43 27-year result\n3:28 Daily reset, explained\n4:11 One lump sum?\n4:52 Other start months\n5:44 2×/3× math vs real QLD/TQQQ\n6:54 Summary\n7:24 Limits\n\n■ How\nQQQ, QLD, TQQQ daily close + payouts (split-adjusted) · 13-week T-bill rate · Mar 10, 1999 → Oct 15, 2026\n1× = QQQ with dividends\n2× / 3× = daily Nasdaq-100 return × 2 / × 3 − fee 0.95% − borrowed part × (T-bill + 1.02%)\n1.02% set once so 2× = real QLD (Jun 21, 2006 → Oct 15, 2026) · same math: TQQQ 0.57% / year below real\n1999–2010 values for 2× and 3× are calculated\nAlso checked: one $10,000 buy at the start · other start months (211 × 10 years, 31 × 25 years) · real QQQ/QLD/TQQQ from Mar 2010 · +10% / −10% example · 2018\nNo tax or FX\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#TQQQ #QQQ #LeveragedETF"
 }
}
```

## 6. 고정 댓글 (아주 쉬운 영어)

```
1×, 2× or 3× — which one would you buy every month for 27 years? Why?
Do you hold TQQQ or QLD now? Tell us 👇 · Next idea to test? Comment!
(Info only · not investment advice)
```

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올리고 **1시간 뒤 예약 공개** (`--publish-at +1h`) |
| 썸네일 | `thumbnails/thumbnail_1.*` (본안 — 글자 없음). 공개 뒤 '테스트 및 비교'에 thumbnail_1~3 |
| 기본 언어 | en (제목·설명·태그 = 부호 + 아주 쉬운 영어 — 한국어 제목은 언어별 ko) |
| 오디오 언어 | ko (내레이션 — 업로드 도구 v1.13) |
| 자막 올리기 | **언어별** (한국어 + en·hi·id·pt·es-419·ja·de·vi·tr — 화면에는 굽지 않고 CC 로, `subs/` 대본 → 오디오 뒤 `python3 tools/subs_tool.py build stock reobeoriji-2026-10` · 업로드 도구 v1.12 가 자막 하나 400단위 — 할당량이 모자라면 `--captions-only` 로 다음 날, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 (내레이션) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성) |

## 8. 점검

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과(어느 계좌가 많았는지·배수·금액)를 쓰지 않았다.
- 설명란 숫자(1999-04·2026-10·500달러·0.95%·13주·0.25%·1만 달러·211·31·10년·25년·2010-03·10%·2018·1999-03-10)는 대본·`backtest/results.json`·`run.py` 설정에 있는 것만.
- 언어별 제목 100자 이하 · `< >` 없음 — `python tools/youtube_upload.py stock reobeoriji-2026-10 --dry-run` 으로 확인.
- 사다 → 매수, 팔다 → 매도.

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, 시청 지속 그래프에서 크게 떨어지는 장, **나라·언어별 조회수**
