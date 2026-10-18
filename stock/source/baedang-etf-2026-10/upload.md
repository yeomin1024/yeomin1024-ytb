# baedang-etf-2026-10 업로드 시트

버전: v1.5 — 2026-10-18 — **기본 언어 en** — 제목·설명란(부호 + 아주 쉬운 영어, 결말 없음)·태그·챕터 이름·고정 댓글을 영어로, 한국어 제목은 언어별 ko, 언어별 설명은 모두 같은 쉬운 영어 · 오디오 언어 ko (사용자 지시 2026-10-18 "설명은 부호, 정말 간단한 영어로 간략하게 표현하도록 해봐 그리고 태그 같은 것도 영어로 하고 한국어로 쓰여진 곳은 정말 간단한 영어로 수정할 수 있어? 모든 영상").
(v1.4.1 — 2026-10-17 — 업로드 설정 '자막 올리기' = **언어별** (한국어 + 9개 언어 CC — 화면에는 굽지 않음, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") · 자막 대본 `subs/<영상ID>.<언어>.txt` 9개.)
(v1.4 — 2026-10-17 — 대본 v1.4 (티커 설명 (사용자 지시 2026-10-17 "일단 티커에 대한 설명도 추가해 예를 들어 'S&P500을 추종하는 ETF인 SPY' 이런식으로 다 수정해보고")) — 챕터·문장 수 다시.)
(v1.3 — 2026-10-17 — 대본 v1.3 (사용자가 붙인 ChatGPT 페르소나 검토 2차 '네 영상에 공통으로 반복되는 문제 5개'): 2번 설명란과 5번 언어별 설명 9개에 **재현 조건** 한 단락 (가격 자료·배당 처리·매수 날·ETF 보수) · 챕터 다시 계산.)
(v1.2 — 2026-10-17 — 대본 v1.2 (사용자가 붙인 ChatGPT 페르소나 검토 2026-10-17 '네 영상에 반복되는 문제 5개' — 경주 해설은 대표 장면만, 조건을 앞에서 분명히, 숫자와 뜻을 한 문장에, 말하는 금액은 어림(만 단위 하나), 한계에 결정 조건): 챕터 다시 계산 (문장 번호 바뀜).)
(v1.1 — 2026-10-17 — 대본 v1.1 (도입 + 규칙 약 24초 — 사용자 지시 2026-10-17 "야 너 내가 테스트 들어가지 전 도입 및 규칙 설명 30초 넘기지 말라고 했잖아 근데 왜 안지켜 다시 수정해"): 챕터 다시 계산 — 규칙 챕터는 첫 챕터에 합침(10초 미만이 될 수 있어서), 설명 챕터는 결과 뒤. (v1.0 — 2026-10-16 — 최초 (주식 3번 배당 ETF vs 지수 세후 — `backtest/run.py` v1.0). 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐". `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음.))
기준 파일: 대본 v1.4 (95문장) · SRT 문장 95 (추정 시각 — 오디오가 생기면 다시) · 결과 `backtest/results.json` · 올릴 영상 = 렌더 원본 `stock/out/baedang-etf-2026-10/final_1080p.mp4` (오디오가 생긴 뒤 — 지금 있는 `preview_estimated_silent.mp4` 는 소리 없는 미리보기라 올리지 않음)

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json`)로 `python tools/youtube_upload.py stock baedang-etf-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (기본 언어 en — 아주 쉬운 영어 · 한국어 제목 「배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까?」은 5번 ko 로)

```
Dividend ETF vs S&P 500: $1,000 a month, 15% tax — which leaves more? SCHD vs SPY
```

## 2. 설명란 (부호 + 아주 쉬운 영어 — 결말 없음 · 챕터 시각은 업로드 도구가 SRT 로 다시 계산)

```
Dividends feel good 💵 — but tax is taken every time. After tax, does a dividend ETF leave more?
SCHD (US dividend ETF) vs SPY (S&P 500 ETF)
$1,000 each month · first trading day · Nov 2011 → Oct 2026
Every dividend: −15% tax (common US withholding rate) → buy again the same day
Fee 0.25% · watch both accounts, day by day.

■ Chapters
0:00 Dividend ETF vs S&P 500
0:26 From 2011, day by day
1:14 The 2022 fall and after
1:45 15-year result
2:36 Where dividends come from
3:35 Yearly returns
4:17 Tax, selling, lump sum
5:06 Other start months
5:42 VYM from 2006
6:34 Summary
7:10 Limits

■ How
Daily close + dividends (split-adjusted) · Nov 1, 2011 → Oct 15, 2026 (VYM from Dec 1, 2006)
Dividend on the ex-date close · fractional shares · ETF fee is in the price
Also checked: tax 0% / 30% · sell all at the end + 15% on the gain · one $100,000 buy at the start · other start months (120 × 5 years, 60 × 10 years) · VYM vs SPY (with 2008)
No FX, inflation or health insurance · tax rules differ by country and account
Code: AI-made Python (tested: no future data) · Voice: AI
Data: Yahoo Finance chart API

Past ≠ future · Not investment advice
#SCHD #SPY #DividendETF
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/baedang-etf-2026-10/baedang-etf-2026-10.txt stock/source/baedang-etf-2026-10/baedang-etf-2026-10.srt --chapters "1=배당 ETF, 세금 떼고도 더 남을까;6=2011년부터 날짜를 흘려 보면;16=2022년 하락장과 그 뒤;22=15년 결과;32=배당은 어디서 나오나;46=해마다 1년 수익률;53=세금·매도·한 번에 넣으면;63=시작한 달을 바꾸면;71=2006년부터 VYM으로;80=정리;88=이 실험의 한계"
```
- 2026-10-17 추정 시각(오디오 전, 대본 v1.4)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 오디오에 맞춘 SRT로 다시 계산한다. 챕터 이름에 결과를 쓰지 않는다.

## 4. 태그 (영어)

```
SCHD, SPY, VYM, dividend ETF, dividend investing, dividend tax, withholding tax, S&P 500, index fund, dollar cost averaging, backtest, Python backtest, investing
```

## 5. 언어별 제목·설명 (localizations — ko + 8개 언어 제목, 설명은 모두 2번과 같은 쉬운 영어 · 기본 언어 en 은 1·2번)

JSON — 업로드 도구가 그대로 읽는다. 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜).

```
{
 "ko": {
  "title": "배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까?",
  "description": "Dividends feel good 💵 — but tax is taken every time. After tax, does a dividend ETF leave more?\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 each month · first trading day · Nov 2011 → Oct 2026\nEvery dividend: −15% tax (common US withholding rate) → buy again the same day\nFee 0.25% · watch both accounts, day by day.\n\n■ Chapters\n0:00 Dividend ETF vs S&P 500\n0:26 From 2011, day by day\n1:14 The 2022 fall and after\n1:45 15-year result\n2:36 Where dividends come from\n3:35 Yearly returns\n4:17 Tax, selling, lump sum\n5:06 Other start months\n5:42 VYM from 2006\n6:34 Summary\n7:10 Limits\n\n■ How\nDaily close + dividends (split-adjusted) · Nov 1, 2011 → Oct 15, 2026 (VYM from Dec 1, 2006)\nDividend on the ex-date close · fractional shares · ETF fee is in the price\nAlso checked: tax 0% / 30% · sell all at the end + 15% on the gain · one $100,000 buy at the start · other start months (120 × 5 years, 60 × 10 years) · VYM vs SPY (with 2008)\nNo FX, inflation or health insurance · tax rules differ by country and account\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#SCHD #SPY #DividendETF"
 },
 "hi": {
  "title": "डिविडेंड ETF हर महीने जमा करें: 15% टैक्स के बाद क्या S&P 500 में उतने ही पैसे से ज़्यादा बचेगा?",
  "description": "Dividends feel good 💵 — but tax is taken every time. After tax, does a dividend ETF leave more?\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 each month · first trading day · Nov 2011 → Oct 2026\nEvery dividend: −15% tax (common US withholding rate) → buy again the same day\nFee 0.25% · watch both accounts, day by day.\n\n■ Chapters\n0:00 Dividend ETF vs S&P 500\n0:26 From 2011, day by day\n1:14 The 2022 fall and after\n1:45 15-year result\n2:36 Where dividends come from\n3:35 Yearly returns\n4:17 Tax, selling, lump sum\n5:06 Other start months\n5:42 VYM from 2006\n6:34 Summary\n7:10 Limits\n\n■ How\nDaily close + dividends (split-adjusted) · Nov 1, 2011 → Oct 15, 2026 (VYM from Dec 1, 2006)\nDividend on the ex-date close · fractional shares · ETF fee is in the price\nAlso checked: tax 0% / 30% · sell all at the end + 15% on the gain · one $100,000 buy at the start · other start months (120 × 5 years, 60 × 10 years) · VYM vs SPY (with 2008)\nNo FX, inflation or health insurance · tax rules differ by country and account\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#SCHD #SPY #DividendETF"
 },
 "id": {
  "title": "ETF dividen tiap bulan: setelah pajak dividen 15%, sisa lebih banyak dari S&P 500 dengan uang sama?",
  "description": "Dividends feel good 💵 — but tax is taken every time. After tax, does a dividend ETF leave more?\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 each month · first trading day · Nov 2011 → Oct 2026\nEvery dividend: −15% tax (common US withholding rate) → buy again the same day\nFee 0.25% · watch both accounts, day by day.\n\n■ Chapters\n0:00 Dividend ETF vs S&P 500\n0:26 From 2011, day by day\n1:14 The 2022 fall and after\n1:45 15-year result\n2:36 Where dividends come from\n3:35 Yearly returns\n4:17 Tax, selling, lump sum\n5:06 Other start months\n5:42 VYM from 2006\n6:34 Summary\n7:10 Limits\n\n■ How\nDaily close + dividends (split-adjusted) · Nov 1, 2011 → Oct 15, 2026 (VYM from Dec 1, 2006)\nDividend on the ex-date close · fractional shares · ETF fee is in the price\nAlso checked: tax 0% / 30% · sell all at the end + 15% on the gain · one $100,000 buy at the start · other start months (120 × 5 years, 60 × 10 years) · VYM vs SPY (with 2008)\nNo FX, inflation or health insurance · tax rules differ by country and account\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#SCHD #SPY #DividendETF"
 },
 "pt": {
  "title": "ETF de dividendos todo mês: com 15% de imposto, sobra mais que o mesmo dinheiro no S&P 500?",
  "description": "Dividends feel good 💵 — but tax is taken every time. After tax, does a dividend ETF leave more?\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 each month · first trading day · Nov 2011 → Oct 2026\nEvery dividend: −15% tax (common US withholding rate) → buy again the same day\nFee 0.25% · watch both accounts, day by day.\n\n■ Chapters\n0:00 Dividend ETF vs S&P 500\n0:26 From 2011, day by day\n1:14 The 2022 fall and after\n1:45 15-year result\n2:36 Where dividends come from\n3:35 Yearly returns\n4:17 Tax, selling, lump sum\n5:06 Other start months\n5:42 VYM from 2006\n6:34 Summary\n7:10 Limits\n\n■ How\nDaily close + dividends (split-adjusted) · Nov 1, 2011 → Oct 15, 2026 (VYM from Dec 1, 2006)\nDividend on the ex-date close · fractional shares · ETF fee is in the price\nAlso checked: tax 0% / 30% · sell all at the end + 15% on the gain · one $100,000 buy at the start · other start months (120 × 5 years, 60 × 10 years) · VYM vs SPY (with 2008)\nNo FX, inflation or health insurance · tax rules differ by country and account\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#SCHD #SPY #DividendETF"
 },
 "es-419": {
  "title": "ETF de dividendos cada mes: con 15% de impuesto, ¿queda más que el mismo dinero en el S&P 500?",
  "description": "Dividends feel good 💵 — but tax is taken every time. After tax, does a dividend ETF leave more?\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 each month · first trading day · Nov 2011 → Oct 2026\nEvery dividend: −15% tax (common US withholding rate) → buy again the same day\nFee 0.25% · watch both accounts, day by day.\n\n■ Chapters\n0:00 Dividend ETF vs S&P 500\n0:26 From 2011, day by day\n1:14 The 2022 fall and after\n1:45 15-year result\n2:36 Where dividends come from\n3:35 Yearly returns\n4:17 Tax, selling, lump sum\n5:06 Other start months\n5:42 VYM from 2006\n6:34 Summary\n7:10 Limits\n\n■ How\nDaily close + dividends (split-adjusted) · Nov 1, 2011 → Oct 15, 2026 (VYM from Dec 1, 2006)\nDividend on the ex-date close · fractional shares · ETF fee is in the price\nAlso checked: tax 0% / 30% · sell all at the end + 15% on the gain · one $100,000 buy at the start · other start months (120 × 5 years, 60 × 10 years) · VYM vs SPY (with 2008)\nNo FX, inflation or health insurance · tax rules differ by country and account\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#SCHD #SPY #DividendETF"
 },
 "ja": {
  "title": "高配当ETFを毎月積み立てると、配当税15%を引いても同じ額のS&P 500より多く残る？",
  "description": "Dividends feel good 💵 — but tax is taken every time. After tax, does a dividend ETF leave more?\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 each month · first trading day · Nov 2011 → Oct 2026\nEvery dividend: −15% tax (common US withholding rate) → buy again the same day\nFee 0.25% · watch both accounts, day by day.\n\n■ Chapters\n0:00 Dividend ETF vs S&P 500\n0:26 From 2011, day by day\n1:14 The 2022 fall and after\n1:45 15-year result\n2:36 Where dividends come from\n3:35 Yearly returns\n4:17 Tax, selling, lump sum\n5:06 Other start months\n5:42 VYM from 2006\n6:34 Summary\n7:10 Limits\n\n■ How\nDaily close + dividends (split-adjusted) · Nov 1, 2011 → Oct 15, 2026 (VYM from Dec 1, 2006)\nDividend on the ex-date close · fractional shares · ETF fee is in the price\nAlso checked: tax 0% / 30% · sell all at the end + 15% on the gain · one $100,000 buy at the start · other start months (120 × 5 years, 60 × 10 years) · VYM vs SPY (with 2008)\nNo FX, inflation or health insurance · tax rules differ by country and account\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#SCHD #SPY #DividendETF"
 },
 "de": {
  "title": "Dividenden-ETF monatlich sparen: Bleibt nach 15 % Steuer mehr als mit gleichem Geld im S&P 500?",
  "description": "Dividends feel good 💵 — but tax is taken every time. After tax, does a dividend ETF leave more?\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 each month · first trading day · Nov 2011 → Oct 2026\nEvery dividend: −15% tax (common US withholding rate) → buy again the same day\nFee 0.25% · watch both accounts, day by day.\n\n■ Chapters\n0:00 Dividend ETF vs S&P 500\n0:26 From 2011, day by day\n1:14 The 2022 fall and after\n1:45 15-year result\n2:36 Where dividends come from\n3:35 Yearly returns\n4:17 Tax, selling, lump sum\n5:06 Other start months\n5:42 VYM from 2006\n6:34 Summary\n7:10 Limits\n\n■ How\nDaily close + dividends (split-adjusted) · Nov 1, 2011 → Oct 15, 2026 (VYM from Dec 1, 2006)\nDividend on the ex-date close · fractional shares · ETF fee is in the price\nAlso checked: tax 0% / 30% · sell all at the end + 15% on the gain · one $100,000 buy at the start · other start months (120 × 5 years, 60 × 10 years) · VYM vs SPY (with 2008)\nNo FX, inflation or health insurance · tax rules differ by country and account\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#SCHD #SPY #DividendETF"
 },
 "vi": {
  "title": "Tích lũy ETF cổ tức mỗi tháng: sau thuế cổ tức 15%, có còn nhiều hơn S&P 500 với cùng số tiền?",
  "description": "Dividends feel good 💵 — but tax is taken every time. After tax, does a dividend ETF leave more?\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 each month · first trading day · Nov 2011 → Oct 2026\nEvery dividend: −15% tax (common US withholding rate) → buy again the same day\nFee 0.25% · watch both accounts, day by day.\n\n■ Chapters\n0:00 Dividend ETF vs S&P 500\n0:26 From 2011, day by day\n1:14 The 2022 fall and after\n1:45 15-year result\n2:36 Where dividends come from\n3:35 Yearly returns\n4:17 Tax, selling, lump sum\n5:06 Other start months\n5:42 VYM from 2006\n6:34 Summary\n7:10 Limits\n\n■ How\nDaily close + dividends (split-adjusted) · Nov 1, 2011 → Oct 15, 2026 (VYM from Dec 1, 2006)\nDividend on the ex-date close · fractional shares · ETF fee is in the price\nAlso checked: tax 0% / 30% · sell all at the end + 15% on the gain · one $100,000 buy at the start · other start months (120 × 5 years, 60 × 10 years) · VYM vs SPY (with 2008)\nNo FX, inflation or health insurance · tax rules differ by country and account\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#SCHD #SPY #DividendETF"
 },
 "tr": {
  "title": "Temettü ETF'si her ay biriktirilirse %15 vergiden sonra aynı parayla S&P 500'den fazla kalır mı?",
  "description": "Dividends feel good 💵 — but tax is taken every time. After tax, does a dividend ETF leave more?\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 each month · first trading day · Nov 2011 → Oct 2026\nEvery dividend: −15% tax (common US withholding rate) → buy again the same day\nFee 0.25% · watch both accounts, day by day.\n\n■ Chapters\n0:00 Dividend ETF vs S&P 500\n0:26 From 2011, day by day\n1:14 The 2022 fall and after\n1:45 15-year result\n2:36 Where dividends come from\n3:35 Yearly returns\n4:17 Tax, selling, lump sum\n5:06 Other start months\n5:42 VYM from 2006\n6:34 Summary\n7:10 Limits\n\n■ How\nDaily close + dividends (split-adjusted) · Nov 1, 2011 → Oct 15, 2026 (VYM from Dec 1, 2006)\nDividend on the ex-date close · fractional shares · ETF fee is in the price\nAlso checked: tax 0% / 30% · sell all at the end + 15% on the gain · one $100,000 buy at the start · other start months (120 × 5 years, 60 × 10 years) · VYM vs SPY (with 2008)\nNo FX, inflation or health insurance · tax rules differ by country and account\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#SCHD #SPY #DividendETF"
 }
}
```

## 6. 고정 댓글 (아주 쉬운 영어)

```
SCHD or SPY — after 15 years and 15% tax, which one did you think would leave more?
Do you buy a dividend ETF every month? Tell us 👇 · Next idea to test? Comment!
(Info only · not investment advice)
```

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올리고 **1시간 뒤 예약 공개** (`--publish-at +1h`) |
| 썸네일 | `thumbnails/thumbnail_1.*` (본안 — 글자 없음). 공개 뒤 '테스트 및 비교'에 thumbnail_1~3 |
| 기본 언어 | en (제목·설명·태그 = 부호 + 아주 쉬운 영어 — 한국어 제목은 언어별 ko) |
| 오디오 언어 | ko (내레이션 — 업로드 도구 v1.13) |
| 자막 올리기 | **언어별** (한국어 + en·hi·id·pt·es-419·ja·de·vi·tr — 화면에는 굽지 않고 CC 로, `subs/` 대본 → 오디오 뒤 `python3 tools/subs_tool.py build stock baedang-etf-2026-10` · 업로드 도구 v1.12 가 자막 하나 400단위 — 할당량이 모자라면 `--captions-only` 로 다음 날, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 (내레이션) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성) |

## 8. 점검

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과(어느 계좌가 많았는지·배수·금액)를 쓰지 않았다.
- 설명란 숫자(2011-11·2026-10·1,000달러·15%·0.25%·0%·30%·10만 달러·120·60·5년·10년·2006·2008)는 대본·`backtest/results.json`·`run.py` 설정에 있는 것만.
- 언어별 제목 100자 이하 · `< >` 없음 — `python tools/youtube_upload.py stock baedang-etf-2026-10 --dry-run` 으로 확인.
- 사다 → 매수, 팔다 → 매도.

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, 시청 지속 그래프에서 크게 떨어지는 장, **나라·언어별 조회수**
