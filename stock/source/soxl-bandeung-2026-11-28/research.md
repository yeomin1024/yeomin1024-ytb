# SOXL 반등, 지금 사도 될까 — 사기 전 확인할 것 · 자료 조사 (대본 근거)

VERSION: v1.1 — 2026-11-28 — 6번 더함 (대본 v10 — 사용자 구성: 시장 상황 → 호재 → 악재 → 변수 → 비중): 경제 지표 · 이란 · AI 의구심 · 하락 구간 안 큰 반등 (calc/market_check.py v1.1) — 사용자 지시 2026-11-28 "…야 대본 이런식으로 내가 만든 구성대로 다시 수정해봐".
이전 v1.0 — 2026-11-28 — 최초. 사용자 지시 2026-11-28 "이거 순서를 주제 탐색 -> 대본 작성으로 가야겠다 1번으로 대본 만들어봐" · "변수 발생할 수 있는 이벤트 일정, 전문가 스탠스, 현재 호재와 악재, 기술적 지표, 과거 사례 모두 확인해서 해야돼".
※ 연구·교육용 — 투자 권유가 아님. 주제 = `stock/result/next_topic/next_topic.md` A-E 1번 (사용자 주제).

숫자(가격·하락률·지표·과거 사례·사는 방법 비교)는 모두 계산 코드 `calc/soxl_check.py` v1.5 출력 `calc/soxl_check_2026-11-27.json` (Yahoo Finance 일별 종가 10년 · 2026-11-27 마감까지). 아래 1~3번(일정·전문가·호재와 악재)은 웹 자료 — 출처와 확실한 정도를 같이 적음. 대본·화면에는 출처를 쓰지 않고 설명란에만 (CLAUDE.md).

## 1. 다가오는 일정 (미국 시간)

| 날짜 | 무엇 | 확실한 정도 | 출처 |
|---|---|---|---|
| 12월 1일 (화) | 10월 구인 건수 (JOLTS) | 여러 달력이 같음 | [fedratecalc 12월 달력](https://fedratecalc.com/us-economic-calendar/december-2026/) |
| 12월 4일 (금) 8:30 | 11월 고용 보고서 | 여러 달력이 같음 | [financecalendar](https://www.financecalendar.com/us-jobs-report/) · [alertachart](https://www.alertachart.com/data/fomc-cpi-calendar) |
| 12월 8~9일 · 결정 9일 (수) 14:00 | 연준 금리 결정 (새 경제 전망 포함) · 시장은 0.25%p **인상**을 90% 넘게 반영 (Kalshi 약 94% · 금리 선물 97~99% — 출처·날짜마다 다름) · 회의 전 기준금리 3.75~4.00% | 날짜 확실 · 확률은 바뀜 | [Kalshi](https://kalshi.com/markets/kxfeddecision/fed-meeting/kxfeddecision-26dec) · [Yahoo Finance — FedWatch](https://finance.yahoo.com/economy/policy/articles/fed-rate-hike-bets-deliver-174700533.html) · [rateprobability](https://rateprobability.com/fed) · [Forbes 11-09](https://www.forbes.com/sites/simonmoore/2026/11/09/what-to-expect-from-the-feds-december-meeting/) |
| 12월 9일 (수) 장 마감 뒤 | 브로드컴 4분기 실적 | 회사 발표 (11-09) | [Broadcom IR](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announce-fourth-quarter-and-fiscal-year-2026) |
| 12월 10일 (목) 8:30 | 11월 소비자물가 (CPI) | 여러 달력이 같음 | [eco3min](https://eco3min.fr/en/next-us-cpi-release/) · [fedratecalc](https://fedratecalc.com/us-economic-calendar/december-2026/) |
| 12월 15일 (화) | 11월 생산자물가 (PPI) | 달력 하나 | [fedratecalc](https://fedratecalc.com/us-economic-calendar/december-2026/) — 대본에 안 씀 |
| 12월 17일 (목) 장 마감 뒤 | 마이크론 1분기 실적 | 회사 발표 (11-19) | [Micron 일정](https://days.to/micron-earnings) · [finviz](https://finviz.com/news/397483/micron-forecasts-first-quarter-revenue-above-expectations-on-ai-demand) |
| 12월 23일 (수) | 개인 소비 지출 물가 (PCE) · 국내총생산 | 달력 하나 | [fedratecalc](https://fedratecalc.com/us-economic-calendar/december-2026/) — 대본에 안 씀 |
| 다음 주 | 반도체 수출 통제 관련 의회 증언 | 요약 글 하나 — **대본에 안 씀** | [everhint 11-27](https://www.everhint.com/stock-market-news-november-27-2026-morning-update-last-12-hours-pacific-time/) |

## 2. 전문가 의견 (갈림)

| 누가 | 무엇 | 날짜 | 확실한 정도 | 출처 |
|---|---|---|---|---|
| 골드만삭스 | 반도체는 과매도 · AI 인프라 회사들의 긴 이익 전망은 긍정 | 11월 중순 | 2차 요약 | [beinsure](https://beinsure.com/news/nasdaq-futures-forecast-ai-stocks-rebound/) |
| JP모건 | 첨단 반도체 수요 · 2027년까지 공급 부족 → 긍정 | 11월 중순 | 2차 요약 | 같은 곳 |
| 모건스탠리 마이클 윌슨 | "지난주 저점을 한 번 더 시험하면 연말 반등이 나올 것" · 11-02 에는 반도체 10~15% 더 하락 · 필라델피아 반도체 지수 9,500 안팎 바닥(11월 중순) 전망 | 11-02 · 11-09 | 주요 언론 | [CNBC 11-09](https://www.cnbc.com/2026/11/09/ai-selloff-stock-market-year-end-rally.html) · [TheStreet](https://www.thestreet.com/investing/stocks/morgan-stanley-issues-warning-about-ai-stocks) |
| (분석 — 은행 이름 확인 못 함) | AI 투자(2027년)가 예상보다 20% 줄면 AI 반도체 이익 35~40% 하락 위험 · 기본 시나리오 약 10% 하락, 2027년 1분기 바닥 | 11월 6일 안팎 | **출처가 BofA 라는 것은 2차 기사 하나** → 대본은 '분석도 있습니다'로만 | [Placera](https://placera.se/telegram/advanced-micro-devices-bofa-halvledarsektorn-kan-aterhamta-sig-under-forsta-kvartalet-2027-20261106) · [Odaily](https://www.odaily.news/en/post/5213814) |
| 마이클 버리 | 반도체 ETF 하락 베팅(풋 — 4월 2027년 1월 만기 · 뒤에 2027년 3월로 바꿈)을 이번 반등에 정리했다는 보도 — **상승 베팅이 아님** | 11-28 보도 | 언론 하나 | [서울경제 영문 11-28](https://en.sedaily.com/world/2026/11/28/even-ais-biggest-bear-closes-shorts-as-chip-stocks-rebound) · [Stocktwits — 풋](https://stocktwits.com/news-articles/markets/equity/michael-burry-says-sox-will-return-to-earth-reveals-fresh-puts-on-key-semiconductor-etf/cZBNXiGRe2g) |

## 3. 호재와 악재

| | 무엇 | 날짜 | 출처 |
|---|---|---|---|
| 호재 | 엔비디아 3분기 실적이 예상을 웃돌고 4분기 전망도 높음 (주가는 다음 날 하락) | 11-17 | [Motley Fool 11-17](https://www.fool.com/coverage/stock-market-today/2026/11/17/stock-market-today-nov-17-nvidia-slides-ahead-of-earnings-but-soars-in-after-hours-trading/) · [Yahoo](https://finance.yahoo.com/markets/stocks/articles/nvidia-earnings-live-updates-commentary-213634774.html) |
| 호재 | 엔비디아 최고경영자 11-12 사임 → 11-23 이사회가 만장일치로 복귀 결정 · 그날 엔비디아 하루 +31.5% (계산 출력) | 11-12 · 11-23 | [SEC 8-K 11-23](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000090/nov23pressrelease.htm) · [CNBC 11-12](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html) — 사임 까닭(사생활 보도)은 대본에 쓰지 않음 |
| 호재 | 11-27 반도체 반등 — 마이크론 +7% 넘게 · AMD +4.56% · 퀄컴 +6.29% · 마벨 실적 | 11-27 | [Motley Fool 11-27](https://www.fool.com/coverage/stock-market-today/2026/11/27/stock-market-today-nov-27-chip-stocks-rebound-sharply-on-broad-ai-enthusiasm/) · [Yahoo 11-27](https://finance.yahoo.com/markets/live/stock-market-today-firday-november-27-dow-sp-500-nasdaq-black-friday-holiday-091152065.html) |
| 악재 | 12월 금리 **인상** 가능성 (위 1번) — 물가가 높고 3분기 성장이 강함 · 연준 월러 이사도 인상 쪽 | 11월 | [kcex 정리](https://blog.kcex.com/markets/december-2026-fomc-preview-waller-discount-rate-bitcoin/) · [Forbes](https://www.forbes.com/sites/simonmoore/2026/11/09/what-to-expect-from-the-feds-december-meeting/) |
| 악재 | 트렌드포스 — D램 계약 가격 오름폭이 2027년까지 줄고, 2028년 1분기부터 하락 (나쁜 경우 2027년 4분기부터) · 메모리 3사 주가 9월 말 뒤 약 45% 하락 | 11-27 | [Yahoo 11-27](https://finance.yahoo.com/markets/stocks/articles/sandisk-jumps-10-investors-return-135840469.html) · [techi](https://www.techi.com/trendforce-dram-prices-fall-2028-bear-case-memory-stocks-micron-sandisk/) |
| 악재 | AI 투자가 돈을 벌어 줄지에 대한 의문 (11-05 반도체 지수 −12.2% · 11-20 마이크론 −11%) | 11-05 · 11-20 | [Wolf Street 11-05](https://wolfstreet.com/2026/11/05/bloodletting-in-semiconductor-stocks/) · [Seeking Alpha 11-20](https://seekingalpha.com/news/4675206-micron-leads-semiconductor-and-ai-stocks-down-as-sox-plunges-7) |
| 악재 | 엔비디아 — 정부 조사에 계속 협조한다고 밝힘 (조사가 끝났다는 말 없음) | 11-23 | [SEC 8-K 11-23](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000090/nov23pressrelease.htm) |

## 4. 기술적 지표 · 과거 사례 (계산 출력 — `calc/soxl_check_2026-11-27.json`)

- 지금(11-27): SOXL 36.57달러 · 1년 최고가(06-22, 300.77달러)보다 −87.8% · 다시 그 값까지 8.2배(+722.5%) · 반도체 지수 −37.2% (+59.3% 면 고점).
- 200일 평균 가격: SOXL −70.3% 아래 · 반도체 지수 −16.0% 아래 (20거래일째 아래) · 상대강도지수(14일) SOXL 36.0 (20일 안 가장 낮을 때 26.2) · 반도체 지수 42.1 · 공포 지수(VIX) 23.81 (11-20 35.89).
- 최근 하루 움직임: 11-20 반도체 지수 −10.7% · SOXL −31.8% / 11-23 +14.0% · +39.9% / 11-24 −7.9% · −24.6% / 11-27 +4.7% · +14.2%.
- 과거 1년 최고가보다 70% 넘게 하락한 구간: 2020-02-19 → 03-20 −80.4% (지수 −34.4%) · 2021-12-27 → 2022-10-14 −90.5% (지수 −46.5%) · 2024-07-10 → 2025-04-08 −88.0% (지수 −39.7%) · 이번 2026-06-22 → 11-20 −89.7% (지수 −42.5%).
- 지수가 고점을 되찾은 날 SOXL 은 고점보다: 2020-06-05 −40.5% · 2023-12-14 −58.6% · 2025-09-10 −58.3%.
- 큰 반등 날(1년 최고가보다 80% 넘게 하락한 채 하루 +14% 넘게): 2022-11-10 +30.7% · 2022-11-30 +17.8% · 2025-04-09 +54.8% · 2025-04-24 +16.6% · 2026-11-09 +22.3% · 11-11 +17.8% · 11-23 +39.9% · 11-27 +14.2%.
  - 과거 네 번: 1년 뒤 모두 올랐음 (+65.7% · +66.9% · +530.9% · +928.3%) · 그 사이 가장 낮을 때 −26.7% · −35.9% · −31.8% · −1.2%. 넷 모두 그 구간 바닥 뒤에 나옴.
  - 이번: 11-09 → 11-20 −45.1% (새 저점) · 지금 −34.9% / 11-11 → −53.2% (새 저점) · 지금 −44.6% / 11-23 → −25.9% · 지금 −15.4%.
- 사는 방법 (같은 돈 · 그날부터 1년 — 이번 구간은 지금까지 · calc v1.5): 한 번에 / 가격 기준 나눠 사기(그날 종가 3분의 1 + 첫 매수가 −15%·−30% 에 미리 건 지정가 주문 — 시가가 그 값 아래면 시가에, 아니면 저가가 닿은 날 그 값에 · 안 닿으면 현금) / 날짜 기준 나눠 사기(그날·21·42거래일 뒤 종가 3분의 1씩) / 반도체 지수가 200일 평균을 되찾은 날 한 번에 / 참고 = 반도체 지수 1배.
  - v1.4 까지는 나눠 사기를 '종가가 그 값을 넘은 날 그 종가'에 사서 갭 하락 때 유리하게 나왔음 (페르소나 반론 1회차 K5 지적) → v1.5 지정가 주문으로 고침.
  - 가장 나빴던 때: 가격 나눠 사기가 한 번에보다 덜 하락 7번 중 7번 · 날짜 나눠 사기도 7번 중 7번 · 가격 vs 날짜 = 가격이 덜 하락 7번 중 1번 (3배 상품은 하루 30%씩 움직여 15% 간격 주문이 하루 이틀에 다 사짐 — 2025-04-10·2026-11-24 다음 날 모두 체결) · 끝 결과 가격 나눠 사기 > 한 번에 7번 중 5번.
  - 2022-11-10: 한 번에 +65.7% (가장 나쁠 때 −26.7%) · 가격 +53.7% (−13.4% · 30% 주문은 안 사져 3분의 2만) · 날짜 +58.7% (−19.5%) · 지수 확인 뒤(2022-12-13) +46.9% (−35.0%) · 1배 +33.1% (−8.2%).
  - 2025-04-09: 한 번에 +530.9% (−31.8%) · 가격 +658.1% (−18.0%) · 날짜 +423.3% (−10.6%) · 지수 확인 뒤(2025-05-13) +333.1% (−15.4%) · 1배 +113.7% (−11.3%).
  - 2026-11-09 (지금까지): 한 번에 −34.9% (−45.1%) · 가격 −21.8% (−34.0% · 11-17·11-20 에 모두 체결) · 날짜 −11.6% (−15.0% · 아직 3분의 1만) · 지수 확인 → 아직 사지 않음 · 1배 −8.4% (−16.2%).
  - 2020: 1년 최고가보다 80% 넘게 하락한 날이 이틀(03-18·03-20)뿐 · 다음 날 +14% 넘은 날 없음 → 큰 반등 날 없음.
  - ⚠️ 사용자 규칙(quick_board 4번 규칙 6 '기간이 아니라 가격으로 나눠서')과 다름: 이 계산에서는 날짜로 나눈 쪽이 가장 나쁠 때 손해가 더 작았음(가격 1/7) → 대본은 '한 번에 사지 않고 나눠 산 쪽이 덜 다쳤다'만 말하고 '날짜가 아니라 가격'은 쓰지 않음 (사용자에게 알림).
- 한계: 과거 비슷한 구간은 세 번뿐 · 반도체가 크게 오르던 10년 · 수수료·세금·환율 없음 · 3배 상품은 지수가 오래 하락하면 0에 가까워질 수 있음 → 대본에서 '과거 네 번 모두 올랐다'를 '앞으로도 오른다'로 말하지 않음.
- 지수 주의: SOXL 이 따라가는 지수는 ICE 반도체 지수(2021년부터) — 계산의 '반도체 지수'는 필라델피아 반도체 지수(^SOX, Yahoo 에서 받음)라 둘은 비슷하지만 같지 않음 · 대본은 '반도체 지수'로만 말하고, 설명란에 '필라델피아 반도체 지수 기준'을 적음.
- 계산 조건(설명란에 적을 것): 남은 현금의 이자·환율·세금·수수료는 넣지 않음 — 대본 v2 에서 뺀 줄 (페르소나 반론 1회차 K4 '하' — 설명란으로).
- 설명란에 적을 것 (대본 v6 에서 뺀 줄): 숫자는 달러 기준 · 수수료·환율·세금·남은 현금 이자는 뺌 · 지정가 주문이 며칠 유지되는지는 증권사마다 다름 (반론 3·4·5회차 하).

## 5. (옛) 대본 v9 확정 — v10 에서 구성을 바꿈 (6번) (페르소나 이탈 9회차 ✅ · 반론 9회차 ✅ — 상 0 · 중 1) · 다음 단계에 넘길 메모

- 검증 기록 `persona_loop.json` (이탈 E1~E9 · 반론 K1~K9) · 회차마다 고친 것은 대본 머리 VERSION 줄들.
- 큰 고침: calc v1.5 지정가 주문(1회차 K5 상) · '날짜가 아니라 가격' 뺌(날짜 나눔이 6/7 덜 하락) · 가격 나눔 '덜 하락'은 구조상 당연 → 날짜 나눔 과거 넷으로만 견줌(5회차) · 결론 = 반등한 날 한 번에 사지 말고 얼마를·어떤 돈으로·어떻게 나눌지 먼저(8회차 '답 불분명' 뒤 v9).
- 반론 9회차 남은 지적 (고치면 검증 다시 — 제목·설명란 단계에서 반영할 것):
  - 중: 33·34줄 '바닥이 지난 뒤'와 '산 뒤 35.9% 더 하락' — 과거는 앞선 저점을 지켰고 이번은 새 저점이 나왔다는 차이를 한 문장에 (다음 대본 고칠 때).
  - 하: 정리에 '나눠 사면 바로 오를 때 덜 벌 수 있다' 대가 · 지수 고점 회복까지 걸린 기간 · 14% 기준(전날 80% 넘게 하락)·기준을 바꿔도 같은지 · 530.9% 앞에 '바닥 뒤에 샀다면' · 윌슨 '저점 한 번 더' 경고 먼저 · 달러 기준·환율·세금(→ 설명란).
- 설명란에 꼭: 숫자는 달러 기준 · 수수료·환율·세금·남은 현금 이자는 뺌 · 지정가 주문 유지 기간은 증권사마다 · 반도체 지수 = 필라델피아 반도체 지수(SOXL 기준 지수와 비슷하지만 같지 않음) · 출처(research.md 1~3번 링크) · 투자 권유 아님.
- 제목·썸네일(다음 단계): 이탈 검토자들이 가장 붙잡힌 줄 = 도입 5줄 '앞선 세 번 가운데 두 번은 새 저점' · 38줄 '11월 9일 45.1% · 11일 53.2% 하락' · 17줄 '지수 1.6배, SOXL 8.2배' → 썸네일 장면 후보.

## 6. 대본 v10 자료 (사용자 구성 — 2026-11-28)

숫자는 `calc/market_check.py` v1.1 출력 `calc/market_check_2026-11-27.json` (Yahoo 일별 종가 10년 · 2026-11-27 마감) + 위 4번(`soxl_check`). 6-2~6-4 는 웹 검색 결과 요약(원문 페이지는 이 환경 네트워크 정책으로 못 엶 — 위키백과·알자지라 DNS 막힘) — 날짜가 찍힌 여러 곳이 겹치는 것만 대본에 씀.

### 6-1. 시장 전체 지표 (계산)

| 지표 | 11-27 | 1년 최고 (날짜) | 최고보다 | 1년 최저보다 | 1개월 |
|---|---|---|---|---|---|
| 미국 10년 국채 금리 | 4.94% | 5.31% (10-05) | −7.1% | +24.6% | −0.11%p |
| 브렌트유 | 95.44달러 | 118.35 (03-30) | −19.4% | **+62.0%** (최저 58.92 · 2025-12-16) | −17.2% |
| 달러 지수 | 104.01 | 104.32 (11-23) | −0.3% | +8.1% | +1.8% |
| S&P500 | 7,297 | 7,819 (10-06) | **−6.7%** | +15.0% | −5.8% |
| 나스닥 | 24,130 | 27,600 (10-06) | **−12.6%** | +16.0% | −9.1% |
| 필라델피아 반도체 지수 | 9,187 | 14,635 (06-22) | **−37.2%** | +37.2% | −21.4% |
| 공포 지수(VIX) | 23.81 | 35.89 (11-20) | −33.7% | +76.8% | +38.4% |

- 반도체 지수 하루 하락: 11-05 **−12.2% = 2025-04-10 뒤 가장 큰 하루 하락** (그 뒤 더 큰 날 0) · 11-20 −10.7% (더 큰 날 = 11-05 하나) · 11-24 −7.9%.

### 6-2. 경제 지표 (웹)

| 무엇 | 값 | 날짜 | 확실한 정도 | 출처 |
|---|---|---|---|---|
| 3분기 성장률(속보치) | 연율 3.4% (2분기 2.2%) | 10-29 발표 | 정부 발표 + 여러 곳 | [BEA](https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026) · [Advisor Perspectives](https://www.advisorperspectives.com/dshort/updates/2026/10/29/q3-gdp-advance-estimate-real-gdp-at-3-4) |
| 10월 일자리 | +16만 5천 개 (예상 6만 개 안팎) · 실업률 4.1% (9월 4.2%) | 11-06 발표 | 정부 발표 + 여러 곳 (예상치는 5.9만~6.5만으로 곳마다 다름 → 대본 '예상보다 훨씬 많이') | [BLS](https://www.bls.gov/news.release/empsit.nr0.htm) · [Babypips](https://www.babypips.com/news/headline-us-jobs-report-october-2026-payrolls-beat-fed) |
| 10월 소비자물가 | 한 달 +0.4% (예상보다 높음) · 근원 +0.3% · 에너지 +0.7% (9월 +5.2%) · 1년 상승률은 정부가 안 냄(2025년 셧다운 자료 공백) | 11-10 발표 | 정부 발표 + 여러 곳 · 1년 상승률 추정은 곳마다 달라 **대본에 안 씀** | [CNBC](https://www.cnbc.com/2026/11/10/cpi-inflation-report-october-2026.html) · [Fox Business](https://www.foxbusiness.com/economy/cpi-inflation-october-2026) |
| 기준금리 | 3.75~4.00% (9-16 0.25%p 인상, 12-0) | — | 여러 곳 | [Motley Fool 11-16](https://www.fool.com/investing/2026/11/16/theres-now-100-chance-fed-rate-hike-in-december-thats-not-worst-news-for-wall-street/) · [24/7 Wall St. 11-18](https://247wallst.com/investing/2026/11/18/traders-now-see-a-95-chance-the-fed-hikes-rates-in-december/) |
| 12월 인상 확률 (시장 가격) | 95%~100% (날짜·출처마다 다름 — 11-17 약 95% · 11-25 97.8%·99.8%) · 월러 이사 0.5%p 도 생각해야 · 윌리엄스 총재 0.5%p 는 아님 | 11월 | 여러 곳 → 대본 '95% 넘게' | 같은 곳 · [Gate 11-25](https://www.gate.com/news/detail/cme-fedwatch-978-probability-of-25bp-fed-rate-hike-in-december-2026-25860188) |
| 내년 추가 인상 | 1월 72.5% · 3월 92.4% | ? | 한 곳 → **대본에 숫자 안 씀** ('내년 초에도 더 올릴 거라는 전망') | [Bitrue](https://www.bitrue.com/blog/fed-rate-hike-december-2026) |

### 6-3. 이란 (웹 — 호재 '종전' 현실성)

| 무엇 | 날짜 | 확실한 정도 | 출처 |
|---|---|---|---|
| 2026년 이란 전쟁 · 4월 휴전 · 6-17 양해각서 | 4월 · 6월 | 여러 곳 | [NPR 07-18](https://npr.org/2026/07/18/nx-s1-5898916/us-iran-escalate-strikes) · [Al Jazeera 07-14](https://www.aljazeera.com/amp/news/2026/7/14/us-strikes-new-targets-in-iran-as-tehran-hits-gulf-states-hormuz) |
| 7월 휴전이 깨짐 — 이란이 호르무즈 해협에서 상선 공격 → 미국이 이란 항구 봉쇄를 다시 시작 (07-14 무렵 — 출처마다 하루 다름 · 다른 요약은 7-8) | 7월 | 여러 곳 · **날짜는 '7월'까지만** | [Bloomberg Law](https://news.bloomberglaw.com/international-trade/us-iran-truce-collapses-as-attacks-worsen-and-blockade-returns) · [Boston Globe 07-14](https://www.bostonglobe.com/2026/07/14/world/us-restores-blockade-iran-after-its-attacks-ships-strait-hormuz/) |
| 협상 — 카타르·파키스탄 중재 · 이란 일곱 가지 조건(봉쇄 해제·제재 해제·동결 자금·모든 전선 중단·전쟁 끝 선언 등) · 미국은 받아들이지 않는 쪽 · 경제 압박을 키움 | 11-02 · 11-09 · 11-12 | 한 언론사 여러 날 + ABC | [Al Jazeera 11-12](https://www.aljazeera.com/news/2026/11/12/no-war-no-peace-can-iran-break-the-deadlock-with-the-us) · [Al Jazeera 11-09](https://www.aljazeera.com/news/2026/11/9/iran-stands-by-demands-to-end-the-war-as-us-ramps-up-military-pressure) |
| 논의되는 틀 = 이란이 해협 공격을 멈추고 미국이 항구 봉쇄를 푸는 것 (카타르 중재 두 차례) | '지난주' (날짜 불분명) | AP 한 곳 → 대본 '이야기되는 것은 …' 정도로 | [PBS(AP)](https://www.pbs.org/newshour/world/u-s-strikes-iranian-targets-in-strait-of-hormuz-u-s-official-tells-ap) |
| 11-27 미국이 봉쇄를 뚫으려던 상선을 사격해 멈춤 · 봉쇄 뒤 158척 돌려보냄 | 11-27 | 한 언론사(미 중부사령부 발표 인용) | [Al Jazeera 11-27](https://aljazeera.com/news/2026/11/27/us-military-says-it-disabled-merchant-ship-trying-to-breach-iran-blockade) |
| 유가 — 해협 위험 vs 공급 과잉 (OPEC+ 증산·미국 재고) | 11월 | 여러 곳 · 값은 계산(6-1)만 | [Oilprice](https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Steady-as-Hormuz-Tanker-Threats-Offset-Supply-Glut-Fears.html) · [Invezz 11-24](https://invezz.com/news/2026/11/24/oil-price-today-brent-below-89-supply-glut-hormuz/) |

- 판단 (대본): **전쟁을 끝내는 종전은 아직 가깝지 않음** (조건 차이 · 11-27 에도 봉쇄 사격) · 먼저 나올 수 있는 것은 '해협 공격 중단 ↔ 봉쇄 해제' 같은 한 단계 낮은 합의 — 이것도 확정 아님. 종전·합의가 되면: 유가↓ → 물가 부담↓ → 금리 인상 압력↓ (일반 경로 — 대본은 '~할 수 있습니다').

### 6-4. AI 의구심 더 (웹)

| 무엇 | 날짜 | 확실한 정도 | 출처 |
|---|---|---|---|
| 빚을 내 짓는 데이터센터 투자가 그만큼 돈을 벌어 줄지 의문 | 11월 | 여러 곳 | [Yahoo](https://finance.yahoo.com/energy/articles/oil-data-centre-stocks-sink-023443660.html) · [Investing.com](https://www.investing.com/news/stock-market-news/us-chip-stocks-extend-losses-premarket-as-ai-spending-concerns-resurface-5050161) |
| 11-05 급락 계기 = 퀄컴 실적 실망 (+ 선거 뒤 AI 투자 규제 걱정 — 정치 이름은 대본에 안 씀) | 11-05 | 요약 한 곳 → 대본 '실적 실망' 만 | [BigGo](https://finance.biggo.com/news/e59ff28d-fe4f-48a8-a387-1b4aea5e5e09) |
| 엔비디아 최고경영자 복귀 뒤 반등이 곧 꺾이고 11-24 반도체 지수 −7.9% | 11-23~24 | 여러 곳 + 계산 | [CNBC 11-25](https://cnbc.com/2026/11/25/nvidia-ai-stock-tech-selloff.html) |
| 모건스탠리 '지나친 하락 — 싸게 살 기회' · 제프리스 '근본 변화가 아닌 반응' · 퓨처럼 '2027년 뒤 AI 투자·자금·전력 불확실' | 11월 | 요약 한 곳 → 대본은 2번 표(골드만·JP모건·윌슨)와 함께 '의견이 갈린다' | 같은 곳 |

### 6-5. 하락 구간 안 큰 반등 (계산 — 사용자 문장 "반등을 주면서 하락한다 · 크게 상승한 것 같으면서도 저점을 깨고")

- 정의: SOXL 이 그 하락 구간에서 그때까지 가장 낮은 종가보다 **30% 넘게** 오른 때 = 큰 반등 하나 · 다음 반등은 새 저점이 나온 뒤에만 셈 · '실패' = 그 반등의 시작 저점을 뒤에 종가로 깸. 그날 판정은 그날까지 종가만(앞날 자료 없음) · 실패 여부는 그 뒤 결과.
- **과거 세 구간: 큰 반등 9번 · 6번 실패** — 2020: 1번 · 0 실패 (바닥 3-20 에서 바로) / 2022: 5번 · 4 실패 · 가장 큰 실패 = 07-01 저점에서 **+90.3%** (08-04) → 09-21 저점 깸 → 10-14 까지 꼭대기보다 −68.6% / 2024~25: 3번 · 2 실패 · 가장 큰 실패 +59.2%.
- **이번 구간(06-22 고점 → 진행 중): 큰 반등 4번 · 앞의 3번 모두 실패** — 07-29 저점에서 **+78.6%** (10-05) → 10-22 저점 깸 → 11-20 까지 꼭대기보다 **−81.2%** / 10-22 저점 +30.7% → 10-30 깸 / 11-05 저점 +61.6% (11-11) → 11-20 깸 (꼭대기보다 −53.2%) / 11-20 저점 +39.9% (11-23) = 지금, 아직 모름.
- 고점 → 바닥: 이번 06-22 → 11-20 = **약 5개월**(5.0) · −89.7%.
- 한계: 과거 구간 셋뿐 · 30% 기준을 바꾸면 횟수가 바뀜(이 계산은 30% 하나) · '실패가 많았다'는 앞으로 반등이 실패한다는 뜻이 아님.
- 주의 (결론 '변수가 정해지고 악재가 풀리면서 반등할 때 비중을 늘린다' — 사용자 문장): 반등을 확인하고 사도 다시 빠진 적이 있음 — 2022-12-13(반도체 지수가 200일 평균을 되찾은 날) 산 경우 그 뒤 1년 안 가장 나쁠 때 −35.0% (11-10 한 번에 산 경우 −26.7% 보다 깊음, 4번 표) → 대본 '그때도 손해가 없어지는 것은 아님'을 한 줄 · 사용자에게 알림.

### 6-6. 설명란에 꼭 (v10 추가)

- 위 5번 목록 + 경제 지표·이란·전문가 출처(6-2~6-4 링크) · 금리 인상 확률은 시장 가격이고 출처·날짜마다 다름 · 큰 반등 정의(30% · 새 저점 뒤에만 셈) · 숫자는 2026-11-27 마감 기준.

### 6-7. 메모리 값·메모리 회사 주가 다시 확인 (2026-11-28 — 이탈 검토 10회차 '세 곳 이름')

- 3번 표 '트렌드포스 — 2028년 1분기부터 하락 · 메모리 3사 주가 9월 말 뒤 약 45%' (Yahoo 11-27 한 곳) → 다시 찾았을 때 **트렌드포스 11-18 자료는 '공급 부족 폭이 줄어 계약 가격 오름폭이 분기마다 줄어든다' · 2027년도 오름세 · 새 공장 물량은 2027년 하반기~2028년** — 2028년 하락은 트렌드포스 자료에서 확인 못 함 → **대본에서 2028년 줄을 뺌** · [TrendForce DRAM 11-18](https://www.trendforce.com/research/download/RP261118PS) · [iconnect007 — 2027 메모리 시장](https://iconnect007.com/article/150995/2027-memory-market-sees-diverging-dram-nand-trends/150992/design).
- 주가는 계산(`market_check.py` v1.2 `memory` — Yahoo 종가, 그 나라 통화): 9-30 → 11-27 **마이크론 −39.3% · 삼성전자 −33.3% · SK하이닉스 −37.5%** · 1년 최고가보다 −46.7% · −50.6% · −62.0% → 대본은 이 숫자로 ('45% 안팎' 뺌).
