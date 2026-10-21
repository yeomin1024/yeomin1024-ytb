# 제목으로 삼을 만한 댓글 — 그리고 같은 내용의 영상 제목이 이미 있는지

자동 생성 — `tools/comment_title_ideas.py` v1.0 (2026-10-21T09:29+00:00 UTC). ※ 연구·교육용 — 투자 권유가 아님.

## 0. 자료와 한계 (먼저 읽기)

- **댓글** = 승인해 자료를 받은 영상의 시청자 댓글 (답글·채널 주인·도배 꼴·정치 댓글 뺌) 중 투자 낱말이 든 **질문·요청**(시청자가 알고 싶은 것)과 **주장·믿음**(시청자가 믿는 방법 — 백테스트로 확인할 만한 것). 좋아요 순 후보 `comment_title_candidates.tsv` 에서 제목감을 골라 `comment_title_picks.tsv` 에 적음 (고른 이 = Claude).
- **같은 내용의 영상 제목** = 탐색에서 본 영상 9,641개(검색 결과 + 채널 평소 영상, 라이브 뺌)의 제목 중 고른 댓글마다 적은 '찾을 말'(정규식)에 맞는 것. **유튜브 전체가 아니다** — 0개여도 '세상에 없다'가 아니라 '탐색에서 본 것 중엔 없다'. 같은 나라만 셈 (한국 = 한국어 영상 · 미국 = 채널 나라 US 인 영어 영상). 나라별 제목 수: 한국 6,383, 그 밖 2,201, 미국 1,057.
- 최근 = 올린 지 180일 안. 조회수는 받은 때 값. 댓글 좋아요는 그 영상 크기에 따라 다르다 (큰 채널 댓글이 좋아요가 많음).

## 1. 한눈에

| # | 나라 | 갈래 | 주제 | 👍 | 같은 내용 제목 (같은 나라) | 그중 최근 180일 | 가장 최근 |
|---|---|---|---|---|---|---|---|
| K01 | 한국 | 주장·믿음 | 빚내서(신용·대출) 투자하면 어떻게 되나 — '여윳돈으로만' | 1,631 | 32 | 31 | 2026-10-19 |
| K02 | 한국 | 주장·믿음 | 실적이 좋아도 주가는 왜 빠지나 | 1,010 | 8 | 8 | 2026-10-16 |
| K03 | 한국 | 주장·믿음 | 번 다음에도 계속 사고팔면 결국 잃나 — 매매 횟수와 수익 | 474 | 15 | 15 | 2026-10-17 |
| K04 | 한국 | 주장·믿음 | 나스닥·S&P 는 몇 년 들고 있어야 손실이 안 나나 | 308 | 4 | 3 | 2026-10-13 |
| K05 | 한국 | 주장·믿음 | 매달 적립식이 예금·물가를 이기나 | 138 | 4 | 3 | 2026-05-10 |
| K06 | 한국 | 주장·믿음 | 유튜브 전문가 '지금 사라·폭락 온다' 예측, 맞았나 (사과영상 요청 … | 211 | 1 | 1 | 2026-10-19 |
| K07 | 한국 | 주장·믿음 | 섹터 몰빵 vs 지수 분산 — 하락장에서 얼마나 차이 | 162 | 17 | 16 | 2026-10-16 |
| K08 | 한국 | 주장·믿음 | 5~10% 오르면 팔고 다시 사기 — 정말 100전 80승인가 | 46 | 2 | 2 | 2026-10-14 |
| K09 | 한국 | 주장·믿음 | 결국 배당주가 답인가 — 배당주 vs 지수(성장) | 49 | 30 | 29 | 2026-10-16 |
| K10 | 한국 | 주장·믿음 | 레버리지(QLD·TQQQ)는 횡보장·하락장에 정말 녹나 | 41 | 21 | 20 | 2026-10-18 |
| K11 | 한국 | 주장·믿음 | 고점에 물려도 버티면 이기나 — 본전까지 몇 년 | 59 | 32 | 29 | 2026-10-19 |
| K12 | 한국 | 질문·요청 | 폭락 때만 사기 vs 매달 사기 | 11 | 2 | 2 | 2026-10-11 |
| K13 | 한국 | 주장·믿음 | 분할매수 vs 한 번에(일시금) — 목돈은 어떻게 | 58 | 24 | 23 | 2026-10-19 |
| K14 | 한국 | 질문·요청 | 폭락장, 팔아야 하나 버텨야 하나 — 어떻게 해야 하나 | 58 | 70 | 68 | 2026-10-19 |
| K15 | 한국 | 질문·요청 | ISA 3년 만기 때 ETF 는 어떻게 — 팔아야 하나·연금 이전 | 31 | 14 | 12 | 2026-10-17 |
| K16 | 한국 | 질문·요청 | 수익률 7·10% 에 배당이 들었나 — 총수익(배당 재투자) | 26 | 6 | 6 | 2026-10-17 |
| K17 | 한국 | 질문·요청 | 환율이 내리면 미국 ETF 는 손해인가 — 환노출 vs 환헤지 (환율 … | 20 | 19 | 19 | 2026-10-20 |
| K18 | 한국 | 질문·요청 | 배당 받으면 건보료·금융소득 종합과세는 얼마 | 24 | 42 | 36 | 2026-10-19 |
| K19 | 한국 | 질문·요청 | 커버드콜(JEPQ 등)은 횡보장·하락장에 정말 유리한가 | 10 | 20 | 20 | 2026-10-19 |
| U01 | 미국 | 질문·요청 | Borrowing against stocks — what if the … | 216 | 0 | 0 | - |
| U02 | 미국 | 주장·믿음 | Never sell (2008·2020) — is buy-and-hol… | 237 | 3 | 3 | 2026-10-16 |
| U03 | 미국 | 주장·믿음 | Buy every dip vs falling knives — does … | 150 | 21 | 21 | 2026-10-19 |
| U04 | 미국 | 질문·요청 | Reinvesting dividends for 30 years — sh… | 109 | 11 | 9 | 2026-10-04 |
| U05 | 미국 | 주장·믿음 | Do IPO buyers lose — returns after buyi… | 2,373 | 8 | 8 | 2026-10-06 |
| U06 | 미국 | 주장·믿음 | Just buy the country ETF (EWY) instead … | 150 | 0 | 0 | - |
| U07 | 미국 | 주장·믿음 | Lump sum vs buying a little every quart… | 37 | 8 | 7 | 2026-10-15 |
| U08 | 미국 | 주장·믿음 | Dividend yield vs total return — growth… | 39 | 28 | 26 | 2026-10-19 |
| U09 | 미국 | 질문·요청 | Does swing/day trading make money vs ju… | 29 | 5 | 5 | 2026-10-19 |
| U10 | 미국 | 질문·요청 | Is October really scary for stocks — th… | 8 | 1 | 1 | 2026-10-18 |

## 2. 댓글과 같은 내용의 영상 제목

### K01. 빚내서(신용·대출) 투자하면 어떻게 되나 — '여윳돈으로만' — 한국 · 주장·믿음

- 👍1,631 “돈없으면 주식하지마세요 여윳돈으로 하는거임”
  - 댓글이 달린 영상: [남들 다 벌었다는데 나도 주식 한번 해봐..!?](https://www.youtube.com/watch?v=3wDg-1Lso24)
- 찾을 말: `빚 ?내서|빚투|대출.{0,10}(받아|내서)? ?(주식|투자|ETF)|신용 ?(융자|거래|매수|잔고)|반대매매|여윳돈|여유 ?자금` → 같은 나라 제목 **32개** (최근 180일 31개, 다른 나라 포함 32개)
  - [[한눈에 경제] 빚내서 주식 샀는데 '강제 처분'…비명도 안 나오는 개미들 / KBS 2026.10.19.](https://www.youtube.com/watch?v=mC4ic5oiHRE) — KBS News · 구독자 3,720,000 · 조회수 523,827 · 2026-10-19
  - [[경제쏙] -9.99% 폭락‥"자기 돈 아닌 빚투는 순식간 증발 우려" (2026.06.23/뉴스외전/MBC)](https://www.youtube.com/watch?v=fwpJU36DM0g) — MBCNEWS · 구독자 6,200,000 · 조회수 475,384 · 2026-06-23
  - [[7월 30일 목요일 한국시황] 삼성전자 특별배당 과연 얼마? ∣ 외국인도 당한 반대매매, 왜 이렇게까지 크게 터질까?](https://www.youtube.com/watch?v=bY4VbUTXf0o) — 증시각도기TV · 구독자 482,000 · 조회수 179,589 · 2026-07-30
  - [[8월 10일 월요일 한국시황] 코스닥 +6.97%!! 코스피도 오른 종목 697개! ∣ 신용잔고로 보는 코스피, 코스닥 저점 신호? ∣ 사모신용 위험은 확대중?](https://www.youtube.com/watch?v=Mq5wVgcbtlQ) — 증시각도기TV · 구독자 482,000 · 조회수 121,764 · 2026-08-10

### K02. 실적이 좋아도 주가는 왜 빠지나 — 한국 · 주장·믿음

- 👍1,010 “하이닉스에 3천만원 잃었네요 돈 잃고 치질 심해지고 나서 많이 깨닳았습니다 아무리 호재가 좋고 영업이익 매출 돈을 많이 벌어도 결국에는 세력 마음대로 주가가 달라진다는것을 많이 깨닫습니다 특히 국장은 더 심하다는것도요..”
  - 댓글이 달린 영상: [내 주변에 주식으로 돈 번 사람이 '진짜' 단 1명도 없는 소름 돋는 이유 ∣ 교수 정선용 (통합본)](https://www.youtube.com/watch?v=SwW4n0ERlS8)
- 찾을 말: `(실적|영업이익|돈을?).{0,15}(좋|최고|역대|많이 ?버).{0,25}(주가|주식).{0,10}(빠|떨어|하락|폭락|왜)|호실적.{0,10}(폭락|하락|급락|주가)` → 같은 나라 제목 **8개** (최근 180일 8개, 다른 나라 포함 8개)
  - [실적이 이렇게 좋은데, 주가는 왜 빠져요?](https://www.youtube.com/watch?v=4DQP7bVU41M) — 슈카월드 · 구독자 3,730,000 · 조회수 837,896 · 2026-07-13
  - [회사가 돈을 이렇게 많이 버는데 주식은 왜 떨어지나요?! [주식 기초 특강 2탄]](https://www.youtube.com/watch?v=Z7xsFLBl8NM) — 우정잉 · 구독자 924,000 · 조회수 469,868 · 2026-10-16
  - [호실적에도 주가 폭락? 외국인이 국장 던지는 진짜 속사정.."지금 100년 만에 딱 두 번 온 기회입니다" 폭등하던 금리 잡힐 변곡점? #이춘광 #투자전략 #뉴…](https://www.youtube.com/watch?v=MFgPnxV5DII) — SBS Biz 뉴스 · 구독자 459,000 · 조회수 175,065 · 2026-10-12
  - [삼성전자 잠정실적 100조 달성. 실적은 전세계 최고인데 주가는 왜..](https://www.youtube.com/watch?v=g0fWUHvOexQ) — 잘되라대한민국 · 구독자 5,960 · 조회수 46,604 · 2026-10-08

### K03. 번 다음에도 계속 사고팔면 결국 잃나 — 매매 횟수와 수익 — 한국 · 주장·믿음

- 👍474 “주식으로 돈 벌 수는 있는데. .. 문제는 벌고 평생 다시는 주식 안해야 되는데.. 그게 안됨. . 결국 잃을때까지 계속 하게됨. .”
  - 댓글이 달린 영상: [내 주변에 주식으로 돈 번 사람이 '진짜' 단 한 명도 없는 소름 돋는 이유 ∣ 교수 정선용 (3부)](https://www.youtube.com/watch?v=k9be9TSs41s)
- 찾을 말: `단타.{0,20}(함정|손실|잃|망|실패|못 ?버|진실|개미)|잦은 ?매매|매매 ?(횟수|빈도)|아무것도 ?하지 ?않|가만히 ?(있|계)|자주 ?(사고 ?팔|매매)` → 같은 나라 제목 **15개** (최근 180일 15개, 다른 나라 포함 15개)
  - [주식 잘하는 사람들은 의외로 아무것도 하지 않습니다 ∣ 존리 존리의부자학교 대표 [얘기좀합시다]](https://www.youtube.com/watch?v=_g3WfiDtVmw) — 머니인더트랩 · 구독자 110,000 · 조회수 476,357 · 2026-10-17
  - ["단타" 개미 60%가 모르는 단타의 진짜 함정 (자본시장연구원 충격 보고서)](https://www.youtube.com/watch?v=ynzKagjNqnc) — 경제가머니 · 구독자 22,500 · 조회수 321,107 · 2026-05-12
  - [단타 5년차가 알려준 ＂잃지 않는 법＂ 딱 3가지 ｜ 코스피 9000시대 생존법](https://www.youtube.com/watch?v=WnuVkKRjcuI) — 돈의흐름도 · 구독자 1,380 · 조회수 153,221 · 2026-08-09
  - [1,118% 수익률, 실전투자대회 1위, 단타로 크게 잃고 바꾼 이 매매법으로 돈 많이 벌었습니다.ㅣ굿트레이더의 압도적 수익의 주식투자법](https://www.youtube.com/watch?v=gLuAK_cr1jc) — 부자회사원 · 구독자 409,000 · 조회수 111,795 · 2026-04-26

### K04. 나스닥·S&P 는 몇 년 들고 있어야 손실이 안 나나 — 한국 · 주장·믿음

- 👍308 “5년이상 투자못할분들은 마이너스네 어쩌네 하지 마시고 그냥 적금드셈 꼴랑 몇개월도 유지못하면서 무슨 나스닥을 투자한다고”
  - 댓글이 달린 영상: ["나스닥100은 매년 상위 100개 종목을 자동으로 갈아 끼웁니다"...제가 나스닥만 고집하는 이유"](https://www.youtube.com/watch?v=IahaFGIdxhE)
- 찾을 말: `(나스닥|S&P ?500|에스앤피|지수|QQQ|QLD|TQQQ).{0,30}(몇 ?년|기간|보유|장기|\d+ ?년).{0,25}(손실|안전|확률|마이너스|원금|0%)|(손실|원금).{0,10}(확률|0%).{0,20}(나스닥|S&P|QLD)` → 같은 나라 제목 **4개** (최근 180일 3개, 다른 나라 포함 4개)
  - [S&P500, '이 기간'만 버티면 손실 거의 없습니다!](https://www.youtube.com/watch?v=977RTNsMvqo) — 원원 - 파이어 준비생 · 구독자 16,900 · 조회수 14,664 · 2025-10-19
  - [QLD는 몇 년 들고 있어야 안전할까? 20년치 모든 매수 시점을 계산해봤습니다.](https://www.youtube.com/watch?v=PWr2oclRWKs) — 여의도 아빠 · 구독자 2,290 · 조회수 10,561 · 2026-10-13
  - [TQQQ 3배 레버리지 6년 보유하면서 느낀점, 투자 수익률 430% 계좌 공개 #TQQQ #레버리지etf](https://www.youtube.com/watch?v=Zf35FbuIPLg) — 50대 투자 라이프 · 구독자 2,560 · 조회수 2,738 · 2026-05-23
  - [S&P500·QQQ 대신 ‘이 포트폴리오' 15년 수익률 +400% 차이 충격](https://www.youtube.com/watch?v=3jSzBKtaw5Q) — 미국회계사 샘돌이 투자연구소 · 구독자 1,660 · 조회수 919 · 2026-08-22

### K05. 매달 적립식이 예금·물가를 이기나 — 한국 · 주장·믿음

- 👍138 “무지성 적립해도 인플레는 이깁니다 은행도 이기구요 공부를 하는것도 좋고 다 좋은데 매일 초심으로 돌아가는 마음수련이 제일 중요합니다 은행에 돈 넣고는 계좌 확인 하루종일 안하면서 주식은 맨날 보게되는 그게 마구니자 실패원인입니다”
  - 댓글이 달린 영상: [[월가아재] 수익률 2% 차이? 40년 뒤에는 140억이 됩니다.](https://www.youtube.com/watch?v=ZYcLMbx2t0Y)
- 찾을 말: `(적립|매달|매월|모아|모으).{0,30}(예금|적금|물가|인플레|은행).{0,20}(vs|이기|보다|비교)|(예금|적금|예적금).{0,10}(vs|대신|보다|말고|하면 ?바보)` → 같은 나라 제목 **4개** (최근 180일 3개, 다른 나라 포함 4개)
  - [“요즘 예적금하면 바보라고?” 1000~5000만 원 놀고있는 목돈 안전하게 투자하는방법 (S&P 500 아님)](https://www.youtube.com/watch?v=V1NE7th1ugU) — 김짠부 · 구독자 1,150,000 · 조회수 1,059,831 · 2026-04-29
  - ["제발 적금대신 이거하세요" 미친듯 오를 국내 테마 ETF 추천](https://www.youtube.com/watch?v=tGKnowrjLy8) — 데일리대일 · 구독자 97,400 · 조회수 20,870 · 2026-05-10
  - [투자하고 남는 현금은 무조건 여기에 넣어두세요. 현금비중 가져갈 때 예적금보다 좋은 현금 보관법](https://www.youtube.com/watch?v=Ck-bFb3NboU) — MZ파이어족 · 구독자 20,700 · 조회수 3,649 · 2026-05-02
  - [2026년 금리 인하 시기 채권 투자 방법: 예금보다 유리한 장기 국채 ETF 전략](https://www.youtube.com/watch?v=9ZIQlaXdoog) — 맛스토리 · 구독자 3,000 · 조회수 460 · 2026-04-20

### K06. 유튜브 전문가 '지금 사라·폭락 온다' 예측, 맞았나 (사과영상 요청 포함) — 한국 · 주장·믿음

- 👍211 “앞전에는 삼전 30만원 이하에는 무조건 사라며. 현대차 60만원 이하라면 사라했고 지금 손실이 5천만원이다”
  - 댓글이 달린 영상: [[🚨긴급진단] 코스피 7000 붕괴...충격의 오늘 시장 왜 이러나?ㅣ이권희 대표 전화연결ㅣ경제시그널](https://www.youtube.com/watch?v=g5v83RNywMQ)
- 찾을 말: `(전문가|유튜버|애널리스트|증권사).{0,25}(예측|전망|목표가|말).{0,20}(맞|틀|적중|검증|따라)|적중률|예측.{0,10}(검증|맞았|틀렸)` → 같은 나라 제목 **1개** (최근 180일 1개, 다른 나라 포함 1개)
  - [한국증시 대폭락, 다음은? ∣ 주린이와 전문가의 엇갈린 전망 [검증 1주차] #코스피 #코스닥](https://www.youtube.com/watch?v=w25b-zT8lNo) — 픽 트레이더 · 구독자 46 · 조회수 324 · 2026-10-19

### K07. 섹터 몰빵 vs 지수 분산 — 하락장에서 얼마나 차이 — 한국 · 주장·믿음

- 👍162 “이번 하락장을 겪으며 특정 섹터 쏠림이 아닌 '분산투자'의 중요성을 뼈저리게 느꼈습니다. 장기 투자에서 흔들리지 않는 심리적 안정을 위해 지수추종(S&P 500), 안전자산(금), 그리고 기회를 잡기 위한 현금 비중을 가져가는 전략이 왜 필요한지 명확히 깨달았습니다. 미래를 예측하려 하기보다 불확실성에 대비하는 것이 본질임을 다시금 배웁니다. 좋은 인사이트 나눠주셔서 진심으로 감사드립니다!”
  - 댓글이 달린 영상: [강세장에도 분산투자 안 하면 결국 돈 잃는 이유ㅣ지식인초대석 EP.160 (오건영 단장 1부)](https://www.youtube.com/watch?v=mm3nI9TZymg)
- 찾을 말: `분산 ?투자|몰빵|한 ?종목.{0,10}(올인|몰빵)|분산.{0,10}(vs|효과|중요)` → 같은 나라 제목 **17개** (최근 180일 16개, 다른 나라 포함 17개)
  - [테슬라 투자 몰빵한 한 직장인의 최후 ∣ 북언더스탠딩 ∣ 절대 실패하지 않는 미국 주식 ETF 투자 ∣ 김성동 저자](https://www.youtube.com/watch?v=sgu3lNOwjZo) — 언더스탠딩 : 세상의 모든 지식 · 구독자 1,400,000 · 조회수 207,507 · 2026-05-05
  - [아파트 팔고 QQQ 20억 몰빵합니다](https://www.youtube.com/watch?v=cUSK5abDLow) — 잼투리 · 구독자 252,000 · 조회수 175,833 · 2026-08-06
  - [노후를 위해 월배당 ETF에 몰빵했다면? 지금 당장 '이것' 점검하세요 I 김수정 I 유용주 I 염승환 I ETF아는형](https://www.youtube.com/watch?v=RNt4ctgoUsY) — ETF 아는 형 · 구독자 157,000 · 조회수 173,161 · 2026-05-29
  - [[월가아재] "버블 8회 말이다" 30년 무패 거장이 AI 대장주 전량 청산하고 몰빵한 이 종목 (Q1 13f 분석)](https://www.youtube.com/watch?v=SgPL3kBb4TM) — 월가아재의 과학적 투자 · 구독자 284,000 · 조회수 172,435 · 2026-05-20

### K08. 5~10% 오르면 팔고 다시 사기 — 정말 100전 80승인가 — 한국 · 주장·믿음

- 👍46 “한국에서 장타하지 마세요. 무조건 5~10프로 오르면 매도 후 다시 매수하세요~ 분할매수 분할매도만 하면 100전 80승 이상됨”
  - 댓글이 달린 영상: [내 주변에 주식으로 돈 번 사람이 '진짜' 단 1명도 없는 소름 돋는 이유 ∣ 교수 정선용 (통합본)](https://www.youtube.com/watch?v=SwW4n0ERlS8)
- 찾을 말: `(\d+ ?%|퍼센트).{0,10}(오르면|수익 ?나면|먹고).{0,15}(팔|매도|익절)|익절 ?(기준|타이밍|라인)|분할 ?매도` → 같은 나라 제목 **2개** (최근 180일 2개, 다른 나라 포함 2개)
  - [​[주식초보] 한 번에 다 사면 위험한 이유? '분할 매수·분할 매도'의 정석 ∣ 김민성 전문가](https://www.youtube.com/watch?v=Sxcv0-Fg7N8) — 모아경제TV · 구독자 58,900 · 조회수 3,769 · 2026-10-14
  - [주식기초 심화 9편｜분할매수·분할매도 실전 설계, 평단보다 비중과 현금 관리](https://www.youtube.com/watch?v=M-vsn5oDxeE) — investmentyoo · 구독자 7 · 조회수 6 · 2026-10-13

### K09. 결국 배당주가 답인가 — 배당주 vs 지수(성장) — 한국 · 주장·믿음

- 👍49 “난 주식 20년차인데 결국 배당주가 답이라는걸 찾음”
  - 댓글이 달린 영상: [더이상 배당주는 사지 않아요/40대 워킹맘](https://www.youtube.com/watch?v=P0j4XK5PaJY)
- 찾을 말: `배당 ?(주|ETF).{0,20}(vs|보다|지수|S&P|성장|나스닥)|(S&P|나스닥|지수|성장주).{0,20}(vs|보다).{0,10}배당|SCHD.{0,10}(vs|보다)` → 같은 나라 제목 **30개** (최근 180일 29개, 다른 나라 포함 51개)
  - [🔥성장주/배당주, 코스피/S&P500, 자가/월세 등 주식과 부동산 전략 대토론 @Tamgu​](https://www.youtube.com/watch?v=1_8Z4disq9M) — 미키피디아 · 구독자 377,000 · 조회수 475,508 · 2026-09-27
  - [월배당 ETF 1등의 반전 "나스닥 아닌 '이것' 삽니다 ∣ 절세미녀](https://www.youtube.com/watch?v=y-cIp2qsOBQ) — 절세미녀 김희연 회계사 · 구독자 188,000 · 조회수 370,732 · 2026-09-22
  - [배당주·성장주·채권, 어떤 비율로 담아야 할까? 월배당을 키운 자산배분 전략 I 평온 I ETF아는형](https://www.youtube.com/watch?v=tV--Sdcd6zk) — ETF 아는 형 · 구독자 157,000 · 조회수 246,205 · 2026-09-18
  - [환율 계속 빠지는데 S&P500 사도 되나요? 멘탈 잡고 완주하는 QQQ+SCHD 보다 나은 장기투자 포트폴리오 #리치노마드](https://www.youtube.com/watch?v=AKV7ZfGORDg) — 리치노마드 Rich Nomad · 구독자 57,100 · 조회수 191,088 · 2026-09-08

### K10. 레버리지(QLD·TQQQ)는 횡보장·하락장에 정말 녹나 — 한국 · 주장·믿음

- 👍41 “QLD 6년차, 만5년 매도 없이 모아가는 중입니다. 여러분, 레버리지는 하락장 횡보장에 다 녹는 다는 말에 너무 매몰 되지 마세요. 하락후 반드시 찾아오게 되는 긴 상승장에서의 양의 복리는 퍼포먼스가 두배가 아닙니다. 속된말로 존나 오릅니다. 횡보, 하락장에서 추종 지수 보다 녹은 원금을 보상 해주고도 남습니다. 우리가 가져야 할 건 야수의 심장이죠”
  - 댓글이 달린 영상: [나스닥 투자하기 전에 이 영상 꼭 보세요 ∣ QLD만 모아가는 이유](https://www.youtube.com/watch?v=g10Y6ZA7rng)
- 찾을 말: `(레버리지|QLD|TQQQ|SOXL|SSO|UPRO|[23] ?배).{0,25}(녹|음의 ?복리|횡보|장기 ?(보유|투자)|장투|함정|위험)` → 같은 나라 제목 **21개** (최근 180일 20개, 다른 나라 포함 21개)
  - [수익률 50배 만드는 미국 지수 레버리지 ETF 장기 투자 전략[2026 싱글파이어 머니쇼]](https://www.youtube.com/watch?v=CWmi_raK-0M) — 싱글파이어 · 구독자 513,000 · 조회수 727,675 · 2026-06-16
  - [QLD 투자가 정답이 된 요즘 (무지성의 함정)](https://www.youtube.com/watch?v=prPEoEWl_n0) — 잼투리 · 구독자 252,000 · 조회수 210,693 · 2026-09-09
  - [배당 파이어족 SCHD+QLD 장기투자 근황](https://www.youtube.com/watch?v=uXYMeS0iNBc) — 잼투리 · 구독자 252,000 · 조회수 176,349 · 2026-05-09
  - [어디서도 말 안해주는 레버리지의 진짜 함정 I 스튜디오경향](https://www.youtube.com/watch?v=2PkoXbr6RD4) — 스튜디오 경향 · 구독자 109,000 · 조회수 152,486 · 2026-07-23

### K11. 고점에 물려도 버티면 이기나 — 본전까지 몇 년 — 한국 · 주장·믿음

- 👍59 “이런 위기때마다 갈아타면 답없다 존버만 하면 이기는 싸움이다”
  - 댓글이 달린 영상: [위기에 빠진 SCHD 계속 모아가도 될까?](https://www.youtube.com/watch?v=ZYatUkqCZ8M)
- 찾을 말: `존버|버티면|물린 ?(개미|사람|투자자)|고점.{0,15}(회복|본전|물)|본전.{0,10}(몇 ?년|언제|까지)` → 같은 나라 제목 **32개** (최근 180일 29개, 다른 나라 포함 32개)
  - [⚠️당신의 장기투자가 실패하는 이유? 구조대도 존버도 답이 아닙니다!](https://www.youtube.com/watch?v=RZ6lKACddVI) — 미키피디아 · 구독자 377,000 · 조회수 551,818 · 2026-04-19
  - [삼성전자·SK하이닉스, 무작정 버티면 위험합니다…반등 시 꼭 확인할 것 (Feat. 박병창 MP파트너스 대표) [딥플 Deep-ple]](https://www.youtube.com/watch?v=DXOxnvraHiA) — 핀플 - Finple · 구독자 45,900 · 조회수 320,025 · 2026-10-18
  - [[문남중 출연] "코스피 바닥, 7월29일에 이미 확인 끝! 전고점 회복 근거? '이것' 보시면 됩니다" #문남중 _261019](https://www.youtube.com/watch?v=btSUFhvYPwk) — 경제통마늘 · 구독자 11,500 · 조회수 309,310 · 2026-10-19
  - [삼전닉스 물린 투자자들 '이익의 저점'을 봐야합니다 - 곽상준 대표 (매트릭스투자자문) [성공예감 이대호입니다]｜KBS 261012 방송](https://www.youtube.com/watch?v=TERduRgYsGo) — KBS 1라디오 · 구독자 1,400,000 · 조회수 286,755 · 2026-10-12

### K12. 폭락 때만 사기 vs 매달 사기 — 한국 · 질문·요청

- 👍11 “1년에 3-4번 오는 폭락장만 노리면 되는데 현실에 저는 아직 초보네요. 많은 도움 많은 생각을 해봅니다. 좋은 영상 꾸준히 올려주세요.”
  - 댓글이 달린 영상: [퇴직금 반토막 나고 깨달은 '상위 2%'의 주식투자자 생존법 6가지! ∣ 노후자금사연 ∣ 오디오북](https://www.youtube.com/watch?v=r-tcC-ZmMBE)
- 찾을 말: `(폭락|하락|급락|조정).{0,15}(때만|만).{0,10}(사|매수)|저점 ?매수.{0,15}(vs|적립|비교|백테스트)|(폭락|하락)장?.{0,10}(매수|사면).{0,20}(vs|적립|비교|백테스트|결과)` → 같은 나라 제목 **2개** (최근 180일 2개, 다른 나라 포함 2개)
  - [[9월결산] S&P500 3개월 연속 하락, 그럼에도 629만원 매수했습니다 ∣ 2주 일본 휴가에 300만원 쓰고 느낀점](https://www.youtube.com/watch?v=AnPUIRvmNXc) — 원원 - 파이어 준비생 · 구독자 16,900 · 조회수 14,324 · 2026-10-11
  - [폭락장에 매달 100만원 계속 산 사람, 10년 뒤 통장에 벌어진 일 [ 재테크/미국주식/배당주식/슈드/노후대책 ]](https://www.youtube.com/watch?v=6q2CcE4DSE0) — 경제기상도 · 구독자 4,320 · 조회수 13,249 · 2026-09-19

### K13. 분할매수 vs 한 번에(일시금) — 목돈은 어떻게 — 한국 · 주장·믿음

- 👍58 “분할매수 조건이 잘못되었네요 무조건 눌림이 온다는 가정에서만 분할매수한다는건데 이번처럼 반도체가 마구 오를땐 한번에 사는게 유리하죠”
  - 댓글이 달린 영상: ["단타" 개미 60%가 모르는 단타의 진짜 함정 (자본시장연구원 충격 보고서)](https://www.youtube.com/watch?v=ynzKagjNqnc)
- 찾을 말: `거치식|분할 ?매수|(한 ?번에|한방에).{0,10}(할까|vs|넣을까|살까)|일시 ?(투자|매수)|적립식.{0,10}(vs|으로 ?할까|이냐)|목돈.{0,15}(투자|넣)` → 같은 나라 제목 **24개** (최근 180일 23개, 다른 나라 포함 24개)
  - [“요즘 예적금하면 바보라고?” 1000~5000만 원 놀고있는 목돈 안전하게 투자하는방법 (S&P 500 아님)](https://www.youtube.com/watch?v=V1NE7th1ugU) — 김짠부 · 구독자 1,150,000 · 조회수 1,059,831 · 2026-04-29
  - [💰 초보투자자의 목돈 1억 투자하기 ∣ 한방에 할까요, 적립식으로 할까요?ㅣ구독자사연 ∣ 곰희상담소#1](https://www.youtube.com/watch?v=WJYWW_XXbSM) — 박곰희TV · 구독자 1,270,000 · 조회수 202,323 · 2026-04-19
  - [나스닥100 1배수, 2배수, 3배수 20년 어떤 성과 보여주나(거치식, 적립식, 리벨런싱) ㅣ QQQ, QLD, TQQQ,](https://www.youtube.com/watch?v=dQdACzI6nKE) — 레버리지 하는 미국회계사 장기투자 여정 · 구독자 13,100 · 조회수 86,062 · 2026-06-20
  - [나스닥 2배 QLD 무지성 적립식매수 vs. 공포탐욕지수 활용 매수 I QQQ, QLD, TQQQ, SOXL](https://www.youtube.com/watch?v=V_RecmLncz4) — 레버리지 하는 미국회계사 장기투자 여정 · 구독자 13,100 · 조회수 74,758 · 2026-08-20

### K14. 폭락장, 팔아야 하나 버텨야 하나 — 어떻게 해야 하나 — 한국 · 질문·요청

- 👍58 “수페님. 현재 주식시장이 끝났다. 망했다. 매도해야겠다 등등 많은 소음과 노이즈가 있는데 이에 관련되어서 우리 투자자들은 어떻게해야 할 지 만들어 주시면 좋을 것 같습니다. 이럴 때 수페님의 영상이 매우 필요합니다~”
  - 댓글이 달린 영상: [반도체 급락에 패닉셀, 월가 거물은 이 때를 경고했다.](https://www.youtube.com/watch?v=qjrAdBB7h5U)
- 찾을 말: `(폭락|급락|하락장|패닉).{0,25}(팔아야|매도해야|버텨|대응|어떻게)|팔아야 ?(할까|하나|될까)|버텨야 ?(할|하나)` → 같은 나라 제목 **70개** (최근 180일 68개, 다른 나라 포함 70개)
  - [주식시장 폭락, 지금 팔아야 할까? 존리가 말하는 하락장 대응 원칙 ∣ 존리 존리의부자학교 대표 [얘기좀합시다]](https://www.youtube.com/watch?v=GNyTjCfCA1s) — 머니인더트랩 · 구독자 110,000 · 조회수 868,947 · 2026-10-15
  - [ETF는 언제 팔아야 할까? 존리가 ETF를 추천하는 이유 ∣ 존리의 머니스쿨](https://www.youtube.com/watch?v=Oe4WizYWqNw) — 존리의 부자학교 · 구독자 586,000 · 조회수 585,843 · 2026-09-11
  - [삼전닉스 팔아야 할까? 고민중이라면 보세요 / #채널A #shorts #경제시그널](https://www.youtube.com/watch?v=dMHOpTtibdY) — 경제시그널 · 구독자 27,800 · 조회수 553,330 · 2026-09-23
  - [나스닥 급락 쇼크… 반도체주가 폭락한 이유 / 삼성전자·SK하이닉스 다음 주 어떻게 대응할까?ㅣ이권희 대표](https://www.youtube.com/watch?v=-3hlQU3C0oA) — 815머니톡 · 구독자 1,290,000 · 조회수 461,697 · 2026-06-06

### K15. ISA 3년 만기 때 ETF 는 어떻게 — 팔아야 하나·연금 이전 — 한국 · 질문·요청

- 👍31 “ISA계좌 개설후 ETF 투자하면 3년뒤 해지할때 ETF도 모두 매도하고 끝내야 되나요?”
  - 댓글이 달린 영상: [50대 노후준비 1억을 20억으로 만드는 가장 현실적인 3가지 전략 ∣ (ISA 계좌, S&P500)](https://www.youtube.com/watch?v=hbBABRmu93Q)
- 찾을 말: `ISA.{0,25}(만기|3년|해지|연장|이전|전환|끝)` → 같은 나라 제목 **14개** (최근 180일 12개, 다른 나라 포함 14개)
  - [“ISA 계좌로 ETF 잘못 사면 큰일납니다” 3년 만기 전에 꼭 알아야하는 것 (S&P500 살때 주의점)](https://www.youtube.com/watch?v=5f8EtDUXgoQ) — 김짠부 · 구독자 1,150,000 · 조회수 881,430 · 2026-06-09
  - ["ISA는 가입했다고 끝이 아닙니다"...만들어놓고 멈춰버린 계좌를 채우는 '가장 단순한 조합'](https://www.youtube.com/watch?v=nttINf-CD18) — 이효석아카데미 · 구독자 729,000 · 조회수 496,232 · 2026-10-10
  - [ISA 개설부터 만기 해지까지 부자되는 전략 총정리](https://www.youtube.com/watch?v=SLmxz2IOa_k) — 경제해적단 · 구독자 121,000 · 조회수 252,533 · 2026-08-19
  - [ISA 계좌, S&P500 하나로 3년 굴리면 얼마 벌까? (ft. 향후 계획 포함)](https://www.youtube.com/watch?v=3mIsnHTgylg) — 원원 - 파이어 준비생 · 구독자 16,900 · 조회수 196,499 · 2026-05-24

### K16. 수익률 7·10% 에 배당이 들었나 — 총수익(배당 재투자) — 한국 · 질문·요청

- 👍26 “초보 질문 하나 드려도 될까요?? 첫번째로 수익률이 7%, 10%라고 말씀을 하시는데 그 수익률이 주가 상승을 말하는걸까요? 주가상승+배당금?? 근데 주가상승이면 팔지않으면 일단 수익은 아니지 않나요? 두번째, 계좌별 수익에대한 세금을 계산할때 주식 매매에 대한 금액도 포함하나요? 사고팔고해서 이득본건 제외고 배당에 대한 이득을 수익으로 보는거 아닌가요?? 고수님들 알려주시면 감사하겠습니다!”
  - 댓글이 달린 영상: ["달러 약세라는데.." S&P500 계속 사모아도 되는 걸까?ㅣ돈크라테스 EP. 27](https://www.youtube.com/watch?v=NJtszuRxre8)
- 찾을 말: `총수익|배당 ?재투자|토탈 ?리턴|total return` → 같은 나라 제목 **6개** (최근 180일 6개, 다른 나라 포함 16개)
  - [2026년 자녀 주식 증여 방법: 세금 0원? 신고부터 현대차2우B 배당 재투자 전략! 현대차 주가를 올리는 진짜 이유? 자율주행, 생각보다 훨씬 빨리 옵니다!](https://www.youtube.com/watch?v=726prdVDzEU) — 집구석 경제학 · 구독자 133,000 · 조회수 121,195 · 2026-04-26
  - [주식 수는 더 많은데 돈은 절반, 배당 재투자 30년의 반전 (고배당 JEPI vs 배당성장 SCHD) [ 재테크/미국주식/ETF/배당주/노후준비 ]](https://www.youtube.com/watch?v=rzRmhHvS4No) — 박대리와 황과장의 경제이야기 · 구독자 1,930 · 조회수 10,961 · 2026-09-30
  - [국내 대표 커버드콜 3종 vs KODEX 200 배당재투자 백테스트 비교 (ft. 커버드콜의 역할)](https://www.youtube.com/watch?v=3iEq9yCz8do) — 재테크메이트TV · 구독자 20,300 · 조회수 9,806 · 2026-10-15
  - [배당왕 SCHD가 총수익에서 진 이유 (SCHD vs DGRO 5라운드) [ 재테크/미국주식/배당주식/슈드/노후대책 ]](https://www.youtube.com/watch?v=Gtkr6sZKyVg) — 경제기상도 · 구독자 4,320 · 조회수 3,942 · 2026-09-20

### K17. 환율이 내리면 미국 ETF 는 손해인가 — 환노출 vs 환헤지 (환율 900원대 시뮬레이션 요청 포함) — 한국 · 질문·요청

- 👍20 “국내상장 1500대에서 샀는데 본주는 많이 상승했는데 환율이 떨어져 현재10% 손실입니다 지금 저같은 사람많은데 환율과의 관계도 설명해 주셨으면 좋았을거같습니다 이 상태에도 그냥 묻어두면 회복이 될지”
  - 댓글이 달린 영상: ["달러 약세라는데.." S&P500 계속 사모아도 되는 걸까?ㅣ돈크라테스 EP. 27](https://www.youtube.com/watch?v=NJtszuRxre8)
- 찾을 말: `환율.{0,25}(ETF|S&P|나스닥|미국 ?주식|손실|손해|먹)|환헤지|환노출|\(H\)` → 같은 나라 제목 **19개** (최근 180일 19개, 다른 나라 포함 19개)
  - [환율 1,380원 밑에서 무조건 담아야 하는 ETF 2종목｜저는 달러 투자 이렇게 합니다](https://www.youtube.com/watch?v=Bds93gdgJYc) — ETF읽어주는남자 : 이읽남 · 구독자 126,000 · 조회수 462,258 · 2026-08-27
  - [환율 1380원, 미국주식 ETF 달러 투자 기회일까?](https://www.youtube.com/watch?v=jSP16zTrEHY) — 수페TV · 구독자 839,000 · 조회수 404,665 · 2026-08-29
  - [환율 1300원대 추락.. 지금 미국주식 사도 될까?](https://www.youtube.com/watch?v=Nl5MlGHr_8s) — 재테크읽어주는 파일럿 · 구독자 1,280,000 · 조회수 334,762 · 2026-09-10
  - ["환율 1500원인데 S&P500 사도 되나요?” ETF 적립식 투자할때 꼭 알아야하는 3가지](https://www.youtube.com/watch?v=VXpUleIos1k) — 김짠부 · 구독자 1,150,000 · 조회수 291,341 · 2026-06-05

### K18. 배당 받으면 건보료·금융소득 종합과세는 얼마 — 한국 · 질문·요청

- 👍24 “퇴직하고 지역보험가입자로서의 배당금 관리 궁금해요. 건보료나 종합 소득세에 대한 내용도 말해주셨음 좋겠어요.”
  - 댓글이 달린 영상: [47억 자산가 포트폴리오 공개 "5060은 이것만 죽어라 사 모으세요" 가격도 싼데 배당까지 퍼줍니다. 전 이걸로 은퇴했어요 ∣ 쭈압 1…](https://www.youtube.com/watch?v=UKXh9WlW9QA)
- 찾을 말: `건보료|건강보험료|종합과세|금융소득` → 같은 나라 제목 **42개** (최근 180일 36개, 다른 나라 포함 42개)
  - [월배당 ETF 10억 투자하면 정말 배당금 얼마? ∣ 종합소득세·건강보험료 계산법 (은퇴 현금흐름 설계)](https://www.youtube.com/watch?v=yRDpbgaZahc) — 은퇴머니 - 은퇴 현금흐름 설계 · 구독자 30,000 · 조회수 755,091 · 2026-05-31
  - [배당 ETF에 10억 투자하면 종합소득세·건보료 다 떼고 매달 이만큼 들어옵니다 (ft. SCHD, JEPQ, 커버드콜 etf 배당금)](https://www.youtube.com/watch?v=CB6ibr4KEcc) — 똑재TV · 구독자 172,000 · 조회수 409,380 · 2026-08-12
  - [배당 ETF에 10억 넣으면 매달 얼마 들어올까? (세금·건보료까지 전부 계산해봤습니다)](https://www.youtube.com/watch?v=sUZZ7KAbnEQ) — 경제학 똑똑 · 구독자 257,000 · 조회수 342,140 · 2026-08-27
  - [S&P500·나스닥100 ETF 이렇게 모으면 은퇴 때 세금 건보료 폭탄 맞습니다 (ft. 금융소득종합과세)](https://www.youtube.com/watch?v=bwi1a3WpmJk) — 똑재TV · 구독자 172,000 · 조회수 223,621 · 2026-06-30

### K19. 커버드콜(JEPQ 등)은 횡보장·하락장에 정말 유리한가 — 한국 · 질문·요청

- 👍10 “어머나♡ 이거 완전 궁금했어요~~ 감사합니다♡ 커버드콜은,횡보장일때 유리한게 맞나요?? 어려운 주식 ㅜ”
  - 댓글이 달린 영상: [3억원으로 월 300만원 평생 받는 법 (커버드콜 vs 나스닥100)](https://www.youtube.com/watch?v=XbXfph9KUXY)
- 찾을 말: `커버드콜.{0,40}(횡보|하락|함정|원금|녹|vs|비교|백테스트|수익률|진실)|(횡보|하락)장?.{0,20}커버드콜` → 같은 나라 제목 **20개** (최근 180일 20개, 다른 나라 포함 20개)
  - ["연 12% 배당에 속지 마세요" 매월 배당금 준다는 커버드콜의 숨겨진 함정ㅣ머니리포트](https://www.youtube.com/watch?v=qmTwtRhnFqo) — 머니인사이드 · 구독자 2,170,000 · 조회수 539,125 · 2026-04-24
  - [매달 200만 원 배당 받으려면 ∣ 투자금은 얼마나 필요할까요 ∣ 커버드콜 수익률](https://www.youtube.com/watch?v=GbbllwA2Db0) — 쁘띠리치 운아, 일상이 재테크가 되는 곳 · 구독자 30,200 · 조회수 80,297 · 2026-05-26
  - [KODEX·TIGER·RISE 완벽 비교 고변동성·횡보장에서 유리한 커버드콜은? ㅣ신얼｜김세종｜ETF아는형](https://www.youtube.com/watch?v=dZc1Tt7ZwGg) — ETF 아는 형 · 구독자 157,000 · 조회수 48,347 · 2026-07-20
  - [코스피200 액티브 커버드콜 ETF, 둘 중에 뭐 사요?｜KODEX 200커버드콜액티브 vs PLUS 200커버드콜액티브](https://www.youtube.com/watch?v=qkjFvEgi91Q) — ETF읽어주는남자 : 이읽남 · 구독자 126,000 · 조회수 47,313 · 2026-08-18

### U01. Borrowing against stocks — what if the market drops 20–40% for years — 미국 · 질문·요청

- 👍216 “What happens when the market drops 20-40% and stays down 2-3 years?”
  - 댓글이 달린 영상: [How to Borrow Against Your Stock Portfolio: Buy, Borrow, Die](https://www.youtube.com/watch?v=NPcgV0dq03Q)
- 찾을 말: `^(?!.*(bitcoin|crypto)).*(borrow(ing)? against|margin (loan|debt|call)|on margin|securities[- ]based|pledged asset|\bSBLOC|buy borrow die)` → 같은 나라 제목 **0개** (최근 180일 0개, 다른 나라 포함 1개)
  - (탐색에서 본 제목 중엔 없음)

### U02. Never sell (2008·2020) — is buy-and-hold always the winner — 미국 · 주장·믿음

- 👍237 “conclusion: never sell. thats the only way to win and have peace. if you never sold in 2008 or 2020 or both you would be way up. invest. dont trade...”
  - 댓글이 달린 영상: [The UNTHINKABLE is About to Happen to the Stock Market (& Why AI Stocks are Nex…](https://www.youtube.com/watch?v=gLwAhfTnJfE)
- 찾을 말: `never sell|don'?t sell|buy and hold|stay invested|time in the market|hold(ing)? through|should (you|i) sell` → 같은 나라 제목 **3개** (최근 180일 3개, 다른 나라 포함 9개)
  - [Best Fidelity Funds to Buy and Hold FOREVER (Simple Investing for Financial Freedom)](https://www.youtube.com/watch?v=b6h2d1pcQ7A) — Investing Simplified - … · 구독자 477,000 · 조회수 132,762 · 2026-06-16
  - [The FOREVER Portfolio: 5 Dividend ETFs I Will Never Sell](https://www.youtube.com/watch?v=rkOc616ZdmI) — Harry's Financial Fitne… · 구독자 36,900 · 조회수 68,361 · 2026-08-15
  - [The 6 BEST Fidelity Index Funds for F.I.R.E. (NEVER SELL!)](https://www.youtube.com/watch?v=fuWKmKmPwPU) — Jacob Wade (Roadmap Mon… · 구독자 25,100 · 조회수 8,141 · 2026-10-16

### U03. Buy every dip vs falling knives — does buying dips beat steady buying — 미국 · 주장·믿음

- 👍150 “Tom Lee will never find a dip that you shouldn’t buy”
  - 댓글이 달린 영상: [Fundamental AI story and drivers are still intact, says Fundstrat's Tom Lee](https://www.youtube.com/watch?v=EPDnXjX_JYM)
- 찾을 말: `buy(ing)? (the|every) dip|\bdip\b|falling knife|pullback|on sale` → 같은 나라 제목 **21개** (최근 180일 21개, 다른 나라 포함 28개)
  - [AI Stocks Are on Sale. It Won’t Last](https://www.youtube.com/watch?v=k1xJbNAGmFg) — BWB - Business With Bri… · 구독자 446,000 · 조회수 290,858 · 2026-10-18
  - [This Pullback is a Gift. I'm Buying These Stocks NOW.](https://www.youtube.com/watch?v=GQm2sHqU0kg) — Ticker Symbol: YOU · 구독자 666,000 · 조회수 287,396 · 2026-10-19
  - [This Market Dip is a GIFT (6 Stocks to Buy NOW)](https://www.youtube.com/watch?v=wsAPdABbe4Y) — Investing Simplified - … · 구독자 477,000 · 조회수 273,943 · 2026-10-13
  - [This Market Dip is a GIFT (7 Stocks to Buy NOW)](https://www.youtube.com/watch?v=pGa5NivEWy8) — Tom Nash · 구독자 698,000 · 조회수 267,322 · 2026-10-19

### U04. Reinvesting dividends for 30 years — show the real result — 미국 · 질문·요청

- 👍109 “Can you show us your portfolio chart for last 30 years??”
  - 댓글이 달린 영상: [I Reinvested Dividends for 30 Years — Here's What Actually Happened](https://www.youtube.com/watch?v=oZqWOuMZwdA)
- 찾을 말: `reinvest|\bdrip\b|(20|25|30|40) years` → 같은 나라 제목 **11개** (최근 180일 9개, 다른 나라 포함 20개)
  - [I've Invested in Dividends for 30 Years. Here's What Most People Get Wrong](https://www.youtube.com/watch?v=M7l-A6Mk9zQ) — BudgetMoney · 구독자 2,550 · 조회수 52,759 · 2026-07-21
  - [I Turned On QQQI DRIP... Then I Saw the Tax Problem](https://www.youtube.com/watch?v=m3NpYEBvxKc) — Mikey Moran · 구독자 11,900 · 조회수 41,858 · 2026-09-15
  - [S&P 500 vs. High-Dividend Portfolio: What 20 Years of Data Actually Proves](https://www.youtube.com/watch?v=Jedd-rsUdDU) — Finance Simplified · 구독자 3,520 · 조회수 28,907 · 2026-09-10
  - [Is JEPQ a Good Decision? How Many Shares of JEPQ I Get From Reinvesting Dividends & What …](https://www.youtube.com/watch?v=Kqpr6L2duRs) — Grounded Life Investmen… · 구독자 5,350 · 조회수 17,108 · 2025-06-07

### U05. Do IPO buyers lose — returns after buying at the IPO — 미국 · 주장·믿음

- 👍2,373 “The only thing stopping every IPO from being an immediate liquidation event are the broker rules to ban dumpers, lockup periods, and other interventions in the "free market"”
  - 댓글이 달린 영상: [The Stock Market Is Being Used as a Dumping Ground](https://www.youtube.com/watch?v=roe3SgezmmU)
- 찾을 말: `\bIPO` → 같은 나라 제목 **8개** (최근 180일 8개, 다른 나라 포함 30개)
  - [The SpaceX IPO... It's Worse Than You Think](https://www.youtube.com/watch?v=-X6YzlY_8tM) — Casual Finance · 구독자 418,000 · 조회수 1,711,053 · 2026-05-21
  - [The SpaceX IPO Is About To Flip Your 401k - Most People Are Not Ready](https://www.youtube.com/watch?v=DsqK41WkF7I) — Minority Mindset · 구독자 2,530,000 · 조회수 396,458 · 2026-06-09
  - [SpaceX: The Most Tragic IPO In Stock Market History](https://www.youtube.com/watch?v=TEimEZVjN9o) — Ticker Symbol: YOU · 구독자 666,000 · 조회수 249,277 · 2026-06-07
  - [SpaceX IPO Is Coming… 3 Tiny Stocks to Buy Before The Launch](https://www.youtube.com/watch?v=g8gTVIeMkys) — Ross Givens · 구독자 190,000 · 조회수 161,834 · 2026-05-18

### U06. Just buy the country ETF (EWY) instead of picking Samsung·SK Hynix — 미국 · 주장·믿음

- 👍150 “Better just buy EWY, which is an ETF that contains 21% SK Hynix and 22% Samsung with no premium. Just wish it was more than 1 3/4 % Hyundai, which owns Boston Dynamics.”
  - 댓글이 달린 영상: [If You Missed NVIDIA Stock, This is Way Bigger.](https://www.youtube.com/watch?v=elD62rk5Ijo)
- 찾을 말: `\bEWY\b|korea(n)? (etf|stock)|south korea|samsung|sk hynix` → 같은 나라 제목 **0개** (최근 180일 0개, 다른 나라 포함 2개)
  - (탐색에서 본 제목 중엔 없음)

### U07. Lump sum vs buying a little every quarter (DCA) — 미국 · 주장·믿음

- 👍37 “I never seem to have luck with lump sum investments. I would rather buy 250 shares per quarter and keep the divi's qualified along the way.”
  - 댓글이 달린 영상: [I Just Bought 1,000 Shares Of SCHD: Here's The Dividends It Pays Me](https://www.youtube.com/watch?v=fPU6Gefdad8)
- 찾을 말: `^(?!.*(bitcoin|crypto)).*(lump[- ]sum|dollar[- ]cost|\bDCA\b|every (week|month))` → 같은 나라 제목 **8개** (최근 180일 7개, 다른 나라 포함 27개)
  - [Buy 1 Share of SCHD Every Week—Here’s the Retirement Math](https://www.youtube.com/watch?v=qFFwr4zsDKQ) — Mikey Moran · 구독자 11,900 · 조회수 165,377 · 2026-10-01
  - [I Bought 1,000 Shares of JEPQ. Here’s What It Pays Me Every Month](https://www.youtube.com/watch?v=gC-_mODu2gI) — Grounded Life Investmen… · 구독자 5,350 · 조회수 31,572 · 2026-10-13
  - [SCHD New All-Time High: I've Paused My DCA & What I'm Buying Instead](https://www.youtube.com/watch?v=r6_aIK6Hfw0) — Grounded Life Investmen… · 구독자 5,350 · 조회수 11,317 · 2026-07-29
  - [I Invested $300,000 in Dividend Stocks — How Much Would I Get Every Month?](https://www.youtube.com/watch?v=9llK4SmzPLM) — Finance Simplified · 구독자 3,520 · 조회수 8,604 · 2026-09-22

### U08. Dividend yield vs total return — growth or dividend — 미국 · 주장·믿음

- 👍39 “The biggest mistake investors make is looking only at the dividend yield or the stock price. Total return is where the real math begins.”
  - 댓글이 달린 영상: [Dividend Stocks vs. Growth Stocks: The Math Most Investors Ignore](https://www.youtube.com/watch?v=4bg3bjvjCjE)
- 찾을 말: `total return|dividend.{0,30}(vs|growth)|growth.{0,20}vs.{0,20}dividend` → 같은 나라 제목 **28개** (최근 180일 26개, 다른 나라 포함 45개)
  - [Stop Guessing! Growth vs Dividend Stocks Explained in 20 Minutes](https://www.youtube.com/watch?v=hkRXzD3CH3c) — Finance Simplified · 구독자 3,520 · 조회수 117,798 · 2026-07-24
  - [Top 10 Monthly Income ETFs With NO NAV Erosion! based on Total Returns (growth & Income )](https://www.youtube.com/watch?v=kok2jmce5gw) — Doug The Retirement Guy… · 구독자 21,200 · 조회수 67,022 · 2026-05-26
  - [I Just Bought 2 Undervalued Dividend Growth Stocks!](https://www.youtube.com/watch?v=hj1k05kenic) — Dividendology · 구독자 263,000 · 조회수 48,294 · 2026-09-09
  - [Top 8 Monthly Income ETFs for 2026 — Ranked by Total Return, NOT Just Yield!](https://www.youtube.com/watch?v=9sWFRXQ5rl4) — Doug The Retirement Guy… · 구독자 21,200 · 조회수 26,309 · 2026-09-03

### U09. Does swing/day trading make money vs just holding an index — 미국 · 질문·요청

- 👍29 “Does anyone actually make money doing this? I’ve been at it for a year, bought 3 different courses, and I’m still just blowing accounts. Every time I think I’ve figured out a strategy, the market does the exact opposite. I’m literally one loss away from just deleting my broker app and quitting for …”
  - 댓글이 달린 영상: [These 4 Stocks Pulled Back. The Spring Is Loaded](https://www.youtube.com/watch?v=I3tyDUSTRq4)
- 찾을 말: `day trad|swing trad|trading (strategy|course|system)|options trad` → 같은 나라 제목 **5개** (최근 180일 5개, 다른 나라 포함 39개)
  - [The 2 Swing Trading Strategies That Made me Millions](https://www.youtube.com/watch?v=k-X0164r66U) — TheOneLanceB · 구독자 147,000 · 조회수 197,201 · 2026-05-27
  - [How To Day Trade: The Ultimate Beginner Guide](https://www.youtube.com/watch?v=j3684ELatt0) — TradingLab · 구독자 2,050,000 · 조회수 26,225 · 2026-10-19
  - [Options Trading for Beginners ($100M Trader Explains)](https://www.youtube.com/watch?v=xHNwbqnrtdo) — TheOneLanceB · 구독자 147,000 · 조회수 14,700 · 2026-10-17
  - [I Closed My First Options Trade (72% Profit in 1 Day)](https://www.youtube.com/watch?v=ikqMFJqfnaQ) — The Dividend Nomad · 구독자 15,200 · 조회수 1,409 · 2026-07-26

### U10. Is October really scary for stocks — the October effect — 미국 · 질문·요청

- 👍8 “What is it about October that scares investors every single year? I’m not a sheep—I like to think outside the box—and it drives me crazy how these people behave.”
  - 댓글이 달린 영상: [The AI Sell-Off Continues (3 Stocks to Buy Now)](https://www.youtube.com/watch?v=6NOUMblSxqY)
- 찾을 말: `october (effect|crash)|crash in october|september (effect|curse)|seasonal|sell in may|worst month\b|best month\b|month of the year` → 같은 나라 제목 **1개** (최근 180일 1개, 다른 나라 포함 1개)
  - [Stock Market Crash in October? Why I Don’t Buy It](https://www.youtube.com/watch?v=qDCFlFrpdb0) — Gareth Soloway · 구독자 299,000 · 조회수 174,272 · 2026-10-18

