# keobeodeu-kol-2026-10 업로드 시트

버전: v1.5 — 2026-10-18 — **기본 언어 en** — 제목·설명란(부호 + 아주 쉬운 영어, 결말 없음)·태그·챕터 이름·고정 댓글을 영어로, 한국어 제목은 언어별 ko, 언어별 설명은 모두 같은 쉬운 영어 · 오디오 언어 ko (사용자 지시 2026-10-18 "설명은 부호, 정말 간단한 영어로 간략하게 표현하도록 해봐 그리고 태그 같은 것도 영어로 하고 한국어로 쓰여진 곳은 정말 간단한 영어로 수정할 수 있어? 모든 영상").
(v1.4.1 — 2026-10-17 — 업로드 설정 '자막 올리기' = **언어별** (한국어 + 9개 언어 CC — 화면에는 굽지 않음, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") · 자막 대본 `subs/<영상ID>.<언어>.txt` 9개.)
(v1.4 — 2026-10-17 — 대본 v1.4 (티커 설명 (사용자 지시 2026-10-17 "일단 티커에 대한 설명도 추가해 예를 들어 'S&P500을 추종하는 ETF인 SPY' 이런식으로 다 수정해보고")) — 챕터·문장 수 다시.)
(v1.3 — 2026-10-17 — 대본 v1.3 (사용자가 붙인 ChatGPT 페르소나 검토 2차 '네 영상에 공통으로 반복되는 문제 5개'): 2번 설명란과 5번 언어별 설명 9개에 **재현 조건** 한 단락 (가격 자료·배당 처리·매수 날·ETF 보수) · 챕터 다시 계산.)
(v1.2 — 2026-10-17 — 대본 v1.2 (사용자가 붙인 ChatGPT 페르소나 검토 2026-10-17 '네 영상에 반복되는 문제 5개' — 경주 해설은 대표 장면만, 조건을 앞에서 분명히, 숫자와 뜻을 한 문장에, 말하는 금액은 어림(만 단위 하나), 한계에 결정 조건): 챕터 다시 계산 (문장 번호 바뀜).)
(v1.1 — 2026-10-17 — 대본 v1.1 (도입 + 규칙 약 23초 — 사용자 지시 2026-10-17 "야 너 내가 테스트 들어가지 전 도입 및 규칙 설명 30초 넘기지 말라고 했잖아 근데 왜 안지켜 다시 수정해"): 챕터 다시 계산 — 규칙 챕터는 첫 챕터에 합침(10초 미만이 될 수 있어서), 설명 챕터는 결과 뒤. (v1.0 — 2026-10-16 — 최초 (주식 2번 커버드콜 원금 — `backtest/run.py` v1.0). 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐". `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음.))
기준 파일: 대본 v1.4 (98문장) · SRT 문장 98 (추정 시각 — 오디오가 생기면 다시) · 결과 `backtest/results.json` · 올릴 영상 = 렌더 원본 `stock/out/keobeodeu-kol-2026-10/final_1080p.mp4` (오디오가 생긴 뒤 — 지금 있는 `preview_estimated_silent.mp4` 는 소리 없는 미리보기라 올리지 않음)

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json` — 업로드 도구 v1.7 이 채널이 다르면 올리지 않음)로 `python tools/youtube_upload.py stock keobeodeu-kol-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (기본 언어 en — 아주 쉬운 영어 · 한국어 제목 「커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까?」은 5번 ko 로)

```
Covered call: spend the payout every month — is your $100K safe? QYLD vs QQQ, 13 years
```

## 2. 설명란 (부호 + 아주 쉬운 영어 — 결말 없음 · 챕터 시각은 업로드 도구가 SRT 로 다시 계산)

```
Covered call ETFs pay every month. Spend it all — is your money safe?
QYLD (Nasdaq-100 covered call ETF) vs QQQ (Nasdaq-100 ETF)
$100,000 each · Dec 2013 → Oct 2026
QYLD: spend every payout 💵
QQQ: sell the same $ on the same day (fair test ⚖️)
Watch both accounts, day by day.

■ Chapters
0:00 Covered call: is the money safe?
0:25 From 2013, day by day
1:35 2022: a long fall
2:20 2025 to the end
2:36 13-year result
3:12 How covered calls pay
4:06 Other start months
5:03 XYLD & JEPI too?
6:04 Tax & reinvest
6:43 Summary
7:12 Limits

■ How
Daily close + payouts (split-adjusted) · QYLD: Dec 12, 2013 → Oct 15, 2026
Payout on the ex-date close · QQQ dividends bought again · fee 0.25% per trade · fractional shares
Also checked: other start months (94 × 5 years, 118 × 3 years) · XYLD vs SPY · JEPI vs SPY · 15% tax · payouts bought again
No inflation, FX or local tax
Code: AI-made Python (tested: no future data) · Voice: AI
Data: Yahoo Finance chart API

Past ≠ future · Not investment advice
#QYLD #QQQ #CoveredCall
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/keobeodeu-kol-2026-10/keobeodeu-kol-2026-10.txt stock/source/keobeodeu-kol-2026-10/keobeodeu-kol-2026-10.srt --chapters "1=커버드콜 분배금, 원금은?;7=2013년부터 날짜를 흘려 보면;21=2022년 긴 하락;30=2025년부터 끝까지;33=13년 결과;40=커버드콜은 어떻게 분배금을 만드나;51=시작한 달을 바꾸면;64=XYLD·JEPI도 같을까;76=세금·다시 매수하면;84=정리;90=이 실험의 한계"
```
- 2026-10-17 추정 시각(오디오 전, 대본 v1.4)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 올릴 때 오디오에 맞춘 SRT로 다시 계산해 2번 설명란에 넣는다.
- 챕터 이름에 결과를 쓰지 않는다.

## 4. 태그 (영어)

```
QYLD, QQQ, XYLD, JEPI, covered call, covered call ETF, monthly dividend, dividend income, Nasdaq 100, retirement income, backtest, Python backtest, investing
```

## 5. 언어별 제목·설명 (localizations — ko + 8개 언어 제목, 설명은 모두 2번과 같은 쉬운 영어 · 기본 언어 en 은 1·2번)

JSON — 업로드 도구가 그대로 읽는다. 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜).

```
{
 "ko": {
  "title": "커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까?",
  "description": "Covered call ETFs pay every month. Spend it all — is your money safe?\nQYLD (Nasdaq-100 covered call ETF) vs QQQ (Nasdaq-100 ETF)\n$100,000 each · Dec 2013 → Oct 2026\nQYLD: spend every payout 💵\nQQQ: sell the same $ on the same day (fair test ⚖️)\nWatch both accounts, day by day.\n\n■ Chapters\n0:00 Covered call: is the money safe?\n0:25 From 2013, day by day\n1:35 2022: a long fall\n2:20 2025 to the end\n2:36 13-year result\n3:12 How covered calls pay\n4:06 Other start months\n5:03 XYLD & JEPI too?\n6:04 Tax & reinvest\n6:43 Summary\n7:12 Limits\n\n■ How\nDaily close + payouts (split-adjusted) · QYLD: Dec 12, 2013 → Oct 15, 2026\nPayout on the ex-date close · QQQ dividends bought again · fee 0.25% per trade · fractional shares\nAlso checked: other start months (94 × 5 years, 118 × 3 years) · XYLD vs SPY · JEPI vs SPY · 15% tax · payouts bought again\nNo inflation, FX or local tax\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#QYLD #QQQ #CoveredCall"
 },
 "hi": {
  "title": "कवर्ड कॉल भुगतान हर महीने खर्च करें तो क्या 13 साल बाद QQQ बेचने से ज़्यादा मूलधन बचेगा?",
  "description": "Covered call ETFs pay every month. Spend it all — is your money safe?\nQYLD (Nasdaq-100 covered call ETF) vs QQQ (Nasdaq-100 ETF)\n$100,000 each · Dec 2013 → Oct 2026\nQYLD: spend every payout 💵\nQQQ: sell the same $ on the same day (fair test ⚖️)\nWatch both accounts, day by day.\n\n■ Chapters\n0:00 Covered call: is the money safe?\n0:25 From 2013, day by day\n1:35 2022: a long fall\n2:20 2025 to the end\n2:36 13-year result\n3:12 How covered calls pay\n4:06 Other start months\n5:03 XYLD & JEPI too?\n6:04 Tax & reinvest\n6:43 Summary\n7:12 Limits\n\n■ How\nDaily close + payouts (split-adjusted) · QYLD: Dec 12, 2013 → Oct 15, 2026\nPayout on the ex-date close · QQQ dividends bought again · fee 0.25% per trade · fractional shares\nAlso checked: other start months (94 × 5 years, 118 × 3 years) · XYLD vs SPY · JEPI vs SPY · 15% tax · payouts bought again\nNo inflation, FX or local tax\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#QYLD #QQQ #CoveredCall"
 },
 "id": {
  "title": "Dividen covered call dipakai tiap bulan: apakah modal tersisa lebih banyak dari jual QQQ, 13 tahun?",
  "description": "Covered call ETFs pay every month. Spend it all — is your money safe?\nQYLD (Nasdaq-100 covered call ETF) vs QQQ (Nasdaq-100 ETF)\n$100,000 each · Dec 2013 → Oct 2026\nQYLD: spend every payout 💵\nQQQ: sell the same $ on the same day (fair test ⚖️)\nWatch both accounts, day by day.\n\n■ Chapters\n0:00 Covered call: is the money safe?\n0:25 From 2013, day by day\n1:35 2022: a long fall\n2:20 2025 to the end\n2:36 13-year result\n3:12 How covered calls pay\n4:06 Other start months\n5:03 XYLD & JEPI too?\n6:04 Tax & reinvest\n6:43 Summary\n7:12 Limits\n\n■ How\nDaily close + payouts (split-adjusted) · QYLD: Dec 12, 2013 → Oct 15, 2026\nPayout on the ex-date close · QQQ dividends bought again · fee 0.25% per trade · fractional shares\nAlso checked: other start months (94 × 5 years, 118 × 3 years) · XYLD vs SPY · JEPI vs SPY · 15% tax · payouts bought again\nNo inflation, FX or local tax\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#QYLD #QQQ #CoveredCall"
 },
 "pt": {
  "title": "Renda de covered call gasta todo mês: sobra mais capital em 13 anos do que vendendo QQQ?",
  "description": "Covered call ETFs pay every month. Spend it all — is your money safe?\nQYLD (Nasdaq-100 covered call ETF) vs QQQ (Nasdaq-100 ETF)\n$100,000 each · Dec 2013 → Oct 2026\nQYLD: spend every payout 💵\nQQQ: sell the same $ on the same day (fair test ⚖️)\nWatch both accounts, day by day.\n\n■ Chapters\n0:00 Covered call: is the money safe?\n0:25 From 2013, day by day\n1:35 2022: a long fall\n2:20 2025 to the end\n2:36 13-year result\n3:12 How covered calls pay\n4:06 Other start months\n5:03 XYLD & JEPI too?\n6:04 Tax & reinvest\n6:43 Summary\n7:12 Limits\n\n■ How\nDaily close + payouts (split-adjusted) · QYLD: Dec 12, 2013 → Oct 15, 2026\nPayout on the ex-date close · QQQ dividends bought again · fee 0.25% per trade · fractional shares\nAlso checked: other start months (94 × 5 years, 118 × 3 years) · XYLD vs SPY · JEPI vs SPY · 15% tax · payouts bought again\nNo inflation, FX or local tax\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#QYLD #QQQ #CoveredCall"
 },
 "es-419": {
  "title": "Ingreso de covered call gastado cada mes: ¿queda más capital en 13 años que vendiendo QQQ?",
  "description": "Covered call ETFs pay every month. Spend it all — is your money safe?\nQYLD (Nasdaq-100 covered call ETF) vs QQQ (Nasdaq-100 ETF)\n$100,000 each · Dec 2013 → Oct 2026\nQYLD: spend every payout 💵\nQQQ: sell the same $ on the same day (fair test ⚖️)\nWatch both accounts, day by day.\n\n■ Chapters\n0:00 Covered call: is the money safe?\n0:25 From 2013, day by day\n1:35 2022: a long fall\n2:20 2025 to the end\n2:36 13-year result\n3:12 How covered calls pay\n4:06 Other start months\n5:03 XYLD & JEPI too?\n6:04 Tax & reinvest\n6:43 Summary\n7:12 Limits\n\n■ How\nDaily close + payouts (split-adjusted) · QYLD: Dec 12, 2013 → Oct 15, 2026\nPayout on the ex-date close · QQQ dividends bought again · fee 0.25% per trade · fractional shares\nAlso checked: other start months (94 × 5 years, 118 × 3 years) · XYLD vs SPY · JEPI vs SPY · 15% tax · payouts bought again\nNo inflation, FX or local tax\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#QYLD #QQQ #CoveredCall"
 },
 "ja": {
  "title": "カバードコールの分配金を毎月使うと、同じ額を売るQQQより13年後に元本は多く残る？",
  "description": "Covered call ETFs pay every month. Spend it all — is your money safe?\nQYLD (Nasdaq-100 covered call ETF) vs QQQ (Nasdaq-100 ETF)\n$100,000 each · Dec 2013 → Oct 2026\nQYLD: spend every payout 💵\nQQQ: sell the same $ on the same day (fair test ⚖️)\nWatch both accounts, day by day.\n\n■ Chapters\n0:00 Covered call: is the money safe?\n0:25 From 2013, day by day\n1:35 2022: a long fall\n2:20 2025 to the end\n2:36 13-year result\n3:12 How covered calls pay\n4:06 Other start months\n5:03 XYLD & JEPI too?\n6:04 Tax & reinvest\n6:43 Summary\n7:12 Limits\n\n■ How\nDaily close + payouts (split-adjusted) · QYLD: Dec 12, 2013 → Oct 15, 2026\nPayout on the ex-date close · QQQ dividends bought again · fee 0.25% per trade · fractional shares\nAlso checked: other start months (94 × 5 years, 118 × 3 years) · XYLD vs SPY · JEPI vs SPY · 15% tax · payouts bought again\nNo inflation, FX or local tax\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#QYLD #QQQ #CoveredCall"
 },
 "de": {
  "title": "Covered-Call-Ausschüttung monatlich ausgeben: Bleibt nach 13 Jahren mehr als beim QQQ-Verkauf?",
  "description": "Covered call ETFs pay every month. Spend it all — is your money safe?\nQYLD (Nasdaq-100 covered call ETF) vs QQQ (Nasdaq-100 ETF)\n$100,000 each · Dec 2013 → Oct 2026\nQYLD: spend every payout 💵\nQQQ: sell the same $ on the same day (fair test ⚖️)\nWatch both accounts, day by day.\n\n■ Chapters\n0:00 Covered call: is the money safe?\n0:25 From 2013, day by day\n1:35 2022: a long fall\n2:20 2025 to the end\n2:36 13-year result\n3:12 How covered calls pay\n4:06 Other start months\n5:03 XYLD & JEPI too?\n6:04 Tax & reinvest\n6:43 Summary\n7:12 Limits\n\n■ How\nDaily close + payouts (split-adjusted) · QYLD: Dec 12, 2013 → Oct 15, 2026\nPayout on the ex-date close · QQQ dividends bought again · fee 0.25% per trade · fractional shares\nAlso checked: other start months (94 × 5 years, 118 × 3 years) · XYLD vs SPY · JEPI vs SPY · 15% tax · payouts bought again\nNo inflation, FX or local tax\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#QYLD #QQQ #CoveredCall"
 },
 "vi": {
  "title": "Tiêu cổ tức covered call mỗi tháng: sau 13 năm vốn còn nhiều hơn bán QQQ cùng số tiền không?",
  "description": "Covered call ETFs pay every month. Spend it all — is your money safe?\nQYLD (Nasdaq-100 covered call ETF) vs QQQ (Nasdaq-100 ETF)\n$100,000 each · Dec 2013 → Oct 2026\nQYLD: spend every payout 💵\nQQQ: sell the same $ on the same day (fair test ⚖️)\nWatch both accounts, day by day.\n\n■ Chapters\n0:00 Covered call: is the money safe?\n0:25 From 2013, day by day\n1:35 2022: a long fall\n2:20 2025 to the end\n2:36 13-year result\n3:12 How covered calls pay\n4:06 Other start months\n5:03 XYLD & JEPI too?\n6:04 Tax & reinvest\n6:43 Summary\n7:12 Limits\n\n■ How\nDaily close + payouts (split-adjusted) · QYLD: Dec 12, 2013 → Oct 15, 2026\nPayout on the ex-date close · QQQ dividends bought again · fee 0.25% per trade · fractional shares\nAlso checked: other start months (94 × 5 years, 118 × 3 years) · XYLD vs SPY · JEPI vs SPY · 15% tax · payouts bought again\nNo inflation, FX or local tax\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#QYLD #QQQ #CoveredCall"
 },
 "tr": {
  "title": "Covered call dağıtımını her ay harcarsanız 13 yıl sonra QQQ satmaktan fazla anapara kalır mı?",
  "description": "Covered call ETFs pay every month. Spend it all — is your money safe?\nQYLD (Nasdaq-100 covered call ETF) vs QQQ (Nasdaq-100 ETF)\n$100,000 each · Dec 2013 → Oct 2026\nQYLD: spend every payout 💵\nQQQ: sell the same $ on the same day (fair test ⚖️)\nWatch both accounts, day by day.\n\n■ Chapters\n0:00 Covered call: is the money safe?\n0:25 From 2013, day by day\n1:35 2022: a long fall\n2:20 2025 to the end\n2:36 13-year result\n3:12 How covered calls pay\n4:06 Other start months\n5:03 XYLD & JEPI too?\n6:04 Tax & reinvest\n6:43 Summary\n7:12 Limits\n\n■ How\nDaily close + payouts (split-adjusted) · QYLD: Dec 12, 2013 → Oct 15, 2026\nPayout on the ex-date close · QQQ dividends bought again · fee 0.25% per trade · fractional shares\nAlso checked: other start months (94 × 5 years, 118 × 3 years) · XYLD vs SPY · JEPI vs SPY · 15% tax · payouts bought again\nNo inflation, FX or local tax\nCode: AI-made Python (tested: no future data) · Voice: AI\nData: Yahoo Finance chart API\n\nPast ≠ future · Not investment advice\n#QYLD #QQQ #CoveredCall"
 }
}
```

## 6. 고정 댓글 (아주 쉬운 영어)

```
QYLD or QQQ — after 13 years, which one had more money left? What was your guess?
Do you hold a covered call ETF now? Tell us 👇 · Next idea to test? Comment!
(Info only · not investment advice)
```

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올리고 **1시간 뒤 예약 공개** (`--publish-at +1h`) |
| 썸네일 | `thumbnails/thumbnail_1.*` (본안 — 글자 없음). 공개 뒤 '테스트 및 비교'에 thumbnail_1~3 |
| 기본 언어 | en (제목·설명·태그 = 부호 + 아주 쉬운 영어 — 한국어 제목은 언어별 ko) |
| 오디오 언어 | ko (내레이션 — 업로드 도구 v1.13) |
| 자막 올리기 | **언어별** (한국어 + en·hi·id·pt·es-419·ja·de·vi·tr — 화면에는 굽지 않고 CC 로, `subs/` 대본 → 오디오 뒤 `python3 tools/subs_tool.py build stock keobeodeu-kol-2026-10` · 업로드 도구 v1.12 가 자막 하나 400단위 — 할당량이 모자라면 `--captions-only` 로 다음 날, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 (내레이션) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — 사용자 지시 2026-10-11) |

## 8. 점검

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과(남은 원금·어느 쪽이 많았는지·배수)를 쓰지 않았다. 결과는 영상 '13년 결과'(s58~)와 각 확인 장 끝에서만.
- 설명란·언어별 설명의 숫자(10만 달러·2013-12·2026-10·0.25%·94·118·5년·3년·15%)는 대본·`backtest/results.json`·`run.py` 설정에 있는 것만 썼다.
- 언어별 제목 100자 이하 · `< >` 없음 — `python tools/youtube_upload.py stock keobeodeu-kol-2026-10 --dry-run` 으로 확인.
- 사다 → 매수, 팔다 → 매도 (설명란의 '매도해서').

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, 시청 지속 그래프에서 크게 떨어지는 장, **나라·언어별 조회수**
