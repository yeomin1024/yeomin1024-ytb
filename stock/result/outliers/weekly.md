# 주식 — 주별 분석 (최근 1주부터 한 주씩 넓힘)

자동 생성 — `tools/weekly_analysis.py` v1.4 (2026-10-28 07:54 UTC). 웹 화면에서 승인해 자료를 받은 영상 723개 (`W_<영상ID>` 폴더). 성공 사례 = 구독자 50,000 이하 · 조회수 10,000 이상 · 구독자당 하루 조회수 ≥ 0.1 (하루 조회수 ÷ 구독자). ※ 연구·교육용 — 투자 권유가 아님.

> 이 표는 승인한 영상 **전부**의 주별 추세다 (한 채널을 통째로 추가하면 그 채널 쪽으로 쏠림). 성공 사례만 골라 주제·제목·썸네일·구성·시청자 니즈를 비교한 분석은 **`analysis.md`** (지시사항 재료).

## 한눈에 (누적: 최근 k주 안에 올라온 영상)

| 창 | 영상 | 채널 | 이번 주 새로 | 조회수 중앙값 | 하루 조회수 중앙값 | 배수 중앙값 | 성공 사례 | 길이(분) | 제목 글자 | 글 출처 자막·음성·설명 | 댓글 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 최근 1주 | 0 | 0 | 0 | – | – | – | 0 | – | – | 0·0·0 | 0 |
| 최근 2주 | 307 | 219 | 307 | 164,995 | 36,513.5 | 0.4 | 52 | 18.9 | 56.8 | 0·0·286 | 88,534 |
| 최근 3주 | 415 | 252 | 108 | 181,950 | 33,807.0 | 0.4 | 69 | 18.9 | 55.7 | 1·0·385 | 128,589 |
| 최근 4주 | 462 | 274 | 47 | 200,141.0 | 32,590.5 | 0.5 | 73 | 18.9 | 55.4 | 1·1·429 | 149,792 |
| 최근 5주 | 491 | 289 | 29 | 205,736 | 30,827.5 | 0.5 | 76 | 18.8 | 55.1 | 1·3·456 | 159,781 |
| 최근 6주 | 516 | 298 | 25 | 213,673.5 | 29,738.5 | 0.5 | 81 | 18.9 | 55.1 | 2·4·479 | 173,315 |
| 최근 7주 | 540 | 306 | 24 | 223,076.0 | 28,959.5 | 0.5 | 88 | 18.9 | 54.9 | 2·5·501 | 183,853 |
| 최근 8주 | 562 | 316 | 22 | 226,604.0 | 27,837.5 | 0.5 | 94 | 18.9 | 55.1 | 2·6·522 | 190,297 |
| 최근 9주 | 582 | 324 | 20 | 227,902.0 | 27,425.3 | 0.6 | 102 | 19.1 | 55.0 | 2·7·539 | 198,432 |
| 최근 10주 | 596 | 330 | 14 | 225,809.5 | 26,647.7 | 0.6 | 110 | 18.9 | 54.9 | 4·8·550 | 204,033 |
| 최근 11주 | 603 | 332 | 7 | 225,932 | 26,539.4 | 0.6 | 113 | 19.0 | 54.9 | 5·8·556 | 210,470 |
| 최근 12주 | 610 | 338 | 7 | 225,248.5 | 26,463.2 | 0.6 | 117 | 18.9 | 54.8 | 7·9·560 | 211,856 |
| 최근 13주 | 619 | 345 | 9 | 225,687 | 26,301.9 | 0.6 | 123 | 19.0 | 54.7 | 7·11·567 | 227,351 |
| 최근 14주 | 626 | 351 | 7 | 224,574.0 | 25,889.4 | 0.6 | 126 | 18.9 | 54.7 | 7·11·574 | 231,201 |
| 최근 15주 | 637 | 355 | 11 | 224,810 | 25,487.5 | 0.6 | 131 | 19.1 | 54.7 | 8·12·583 | 244,908 |
| 최근 16주 | 646 | 360 | 9 | 223,076.0 | 25,248.2 | 0.6 | 135 | 19.1 | 54.7 | 9·13·590 | 251,151 |
| 최근 17주 | 652 | 364 | 6 | 224,324.0 | 25,064.5 | 0.6 | 137 | 19.1 | 54.6 | 9·14·595 | 253,792 |
| 최근 18주 | 658 | 368 | 6 | 223,076.0 | 24,876.1 | 0.7 | 138 | 19.1 | 54.6 | 9·14·600 | 257,624 |
| 최근 19주 | 665 | 371 | 7 | 224,310 | 24,700.0 | 0.7 | 140 | 19.1 | 54.7 | 11·15·604 | 260,407 |
| 최근 20주 | 669 | 372 | 4 | 221,842 | 24,439.3 | 0.7 | 142 | 19.1 | 54.6 | 14·15·605 | 261,554 |
| 최근 21주 | 673 | 376 | 4 | 221,842 | 24,330.3 | 0.7 | 142 | 19.1 | 54.6 | 14·15·609 | 270,835 |
| 최근 22주 | 679 | 380 | 6 | 221,842 | 24,259.9 | 0.7 | 147 | 19.1 | 54.5 | 14·15·615 | 273,981 |
| 최근 23주 | 688 | 386 | 9 | 221,579.5 | 23,992.5 | 0.7 | 147 | 19.1 | 54.5 | 16·15·622 | 284,595 |
| 최근 24주 | 695 | 389 | 7 | 220,596 | 23,662.8 | 0.7 | 148 | 19.1 | 54.5 | 16·15·629 | 285,959 |
| 최근 25주 | 706 | 397 | 11 | 219,611.0 | 23,298.5 | 0.7 | 150 | 19.1 | 54.5 | 19·15·637 | 300,763 |
| 최근 26주 | 711 | 397 | 5 | 220,596 | 23,178.4 | 0.7 | 152 | 19.1 | 54.5 | 20·15·641 | 301,944 |
| 최근 27주 | 717 | 401 | 6 | 216,672 | 22,759.1 | 0.7 | 153 | 19.1 | 54.4 | 22·15·645 | 304,578 |
| 최근 28주 | 723 | 406 | 6 | 216,672 | 22,423.9 | 0.8 | 153 | 19.0 | 54.4 | 24·15·649 | 306,609 |

## 최근 1주

이 기간에 올라온 승인 영상 없음.

## 최근 2주

- 이번 주에 새로 들어온 영상 307개: [어바웃 뉴욕] 내 QQQ 비용, 누가 받나…운영비의 (2026-10-17) · 주식은 하락장에 구매해야 하는 이유(2026-10-19) · 내일부터 미국주식도 큰일났다네요(2026-10-18) · [경제쏙] 증시 폭락에 ‘패닉셀’‥실적 좋은데 왜 빠지(2026-10-15) · सारे काम छोड़ो ये खबर देखो😱, St(2026-10-19) · "실시간 초비상, 위기의 한국 경제" 갈수록 엉망이 되(2026-10-15) …
- 제목 특징: 물음표 ? 28% · 코스피·폭락·급락·하락장 22% · S&P500·ETF·지수·나스닥 15% · 느낌표 ! 12% · AI 12% · 패턴형(공통점·특징·이유·N가지·착각·과정) 10%
- 자주 쓴 제목 낱말: 코스피(34), Market(33), Stocks(29), 이유(25), Stock(25), AI(22), to(21), 대표(20), ETF(19), 주식(19)
- 글 출처: 자막 0 · 음성인식 0 · 설명으로 대신 286 · 없음 21 · 타임라인 있는 영상 36%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(101), is(96), in(92), of(92), on(87), this(81), or(75), are(75), investment(69), not(68), financial(67), market(64)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 88,534개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 9% · 원칙·정답(시청자가 스스로 씀) 6% · 2026 시장(폭락·불장·서킷) 6% · 경험(내 얘기·나도 잃음) 4% · 칭찬·감사 4% · **어느 갈래에도 안 듦 61%** (모든 댓글 유형은 `comment_types.md`)
  - 👍2,745 “뭐야 인공지능이 아녔어?”
  - 👍2,461 “아니 이형 재워야되는데 왜 여깄어”
  - 👍2,219 “국민연금을 정치적 이용 . 특검필요
연기금은 지수 방어용으로 쓰던거  지수 뻥튀기용으로 활용한거는 도박아니고 뭐냐”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [AI bubble fears: Could a crash trigger a global fi](https://www.youtube.com/watch?v=tGRB8ECyEJ0) | DW News | 1,262,899 | 235,141.8 | 2026-10-15 |
| [[한눈에 경제] 빚내서 주식 샀는데 '강제 처분'…비명도 안 나오는 개미들 / KBS 20](https://www.youtube.com/watch?v=mC4ic5oiHRE) | KBS News | 523,827 | 231,764.1 | 2026-10-19 |

## 최근 3주

- 이번 주에 새로 들어온 영상 108개: 코스피 6000 붕괴, 지금 팔아야 하나? 이광수가 '(2026-10-13) · "이러면, 지옥문 열릴 것" 지금 하락은 진짜 공포일까(2026-10-13) · How BAD Are Stock Valuations R(2026-10-09) · 20년 차 베테랑 투자자가 이야기하는 초보도 주식 시장(2026-10-10) · 삼성전자 폭락한 진짜 이유. 가진 주식 전부 '이렇게'(2026-10-12) · 코스피 6000 붕괴, 사이드카가 두달만에 울린 이유(2026-10-13) …
- 제목 특징: 물음표 ? 29% · 코스피·폭락·급락·하락장 22% · S&P500·ETF·지수·나스닥 14% · 느낌표 ! 11% · AI 10% · 패턴형(공통점·특징·이유·N가지·착각·과정) 10%
- 자주 쓴 제목 낱말: 코스피(46), Market(38), Stocks(34), 이유(33), Stock(29), to(27), 주식(24), ETF(24), 대표(24), AI(23)
- 글 출처: 자막 1 · 음성인식 0 · 설명으로 대신 385 · 없음 29 · 말 속도 중앙값 5.9 음절/초 (자막·음성인식) · 타임라인 있는 영상 35%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(127), is(121), in(115), of(114), on(106), this(101), are(94), or(93), investment(84), not(83), financial(82), video(78)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 128,589개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 10% · 2026 시장(폭락·불장·서킷) 7% · 원칙·정답(시청자가 스스로 씀) 6% · 경험(내 얘기·나도 잃음) 4% · 칭찬·감사 4% · **어느 갈래에도 안 듦 61%** (모든 댓글 유형은 `comment_types.md`)
  - 👍4,560 “India needs its own social media”
  - 👍3,110 “Social Media is enemy of India”
  - 👍2,766 “deepstate is not just a theory now 💀”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [AI bubble fears: Could a crash trigger a global fi](https://www.youtube.com/watch?v=tGRB8ECyEJ0) | DW News | 1,262,899 | 235,141.8 | 2026-10-15 |

## 최근 4주

- 이번 주에 새로 들어온 영상 47개: SCHD ETF 연이은 하락.. 지금이라도 갈아타야 할(2026-10-05) · 코스닥 10월부터 대반전! "주도주 '이 순서'로 뜹니(2026-10-02) · [차트 강의] 100조 운용역이 신입 펀드매니저에게 가(2026-10-03) · 인도 옵션 투자 광풍, 50조 털린 인도 개미들(2026-10-03) · 【高配当株8選】10万円なら何を買う？53銘柄保有のふゆこが(2026-10-03) · Market CRASH - Don’t Do Anythi(2026-10-02) …
- 제목 특징: 물음표 ? 29% · 코스피·폭락·급락·하락장 20% · S&P500·ETF·지수·나스닥 14% · 느낌표 ! 11% · AI 10% · 패턴형(공통점·특징·이유·N가지·착각·과정) 10%
- 자주 쓴 제목 낱말: 코스피(47), Market(42), Stocks(39), 이유(35), Stock(33), to(30), ETF(27), 주식(27), 대표(26), AI(24)
- 글 출처: 자막 1 · 음성인식 1 · 설명으로 대신 429 · 없음 31 · 말 속도 중앙값 5.9 음절/초 (자막·음성인식) · 타임라인 있는 영상 35%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(146), is(135), in(132), of(131), on(121), this(120), or(107), are(107), video(96), not(96), investment(94), financial(92)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 149,792개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 6% · 2026 시장(폭락·불장·서킷) 6% · 경험(내 얘기·나도 잃음) 4% · 칭찬·감사 4% · **어느 갈래에도 안 듦 61%** (모든 댓글 유형은 `comment_types.md`)
  - 👍4,560 “India needs its own social media”
  - 👍3,443 “Companies used to IPO to grow, now they IPO to cash out.”
  - 👍3,110 “Social Media is enemy of India”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 5주

- 이번 주에 새로 들어온 영상 29개: 🔥성장주/배당주, 코스피/S&P500, 자가/월세 등 (2026-09-27) · Corporate Media is Starting To(2026-09-30) · ETF-Papst sieht “Rezept für ei(2026-09-29) · So würde ich 2027 starten! 500(2026-09-27) · '이 ETF 두 가지'만 하면 평생 부자로 살 수 있습(2026-09-24) · The Truth About Leveraged ETFs(2026-09-27) …
- 제목 특징: 물음표 ? 29% · 코스피·폭락·급락·하락장 19% · S&P500·ETF·지수·나스닥 16% · 느낌표 ! 11% · 패턴형(공통점·특징·이유·N가지·착각·과정) 9% · AI 9%
- 자주 쓴 제목 낱말: 코스피(48), Market(44), Stocks(40), 이유(36), Stock(34), to(34), 주식(33), ETF(31), 대표(28), AI(24)
- 글 출처: 자막 1 · 음성인식 3 · 설명으로 대신 456 · 없음 31 · 말 속도 중앙값 5.9 음절/초 (자막·음성인식) · 타임라인 있는 영상 36%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(155), in(145), is(143), of(139), on(129), this(129), or(114), are(114), video(102), not(101), investment(99), financial(98)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 159,781개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 6% · 2026 시장(폭락·불장·서킷) 6% · 경험(내 얘기·나도 잃음) 4% · 칭찬·감사 4% · **어느 갈래에도 안 듦 61%** (모든 댓글 유형은 `comment_types.md`)
  - 👍4,560 “India needs its own social media”
  - 👍3,443 “Companies used to IPO to grow, now they IPO to cash out.”
  - 👍3,110 “Social Media is enemy of India”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 6주

- 이번 주에 새로 들어온 영상 25개: J’ai Investi toutes mes Économ(2026-09-17) · 'Big Short' investor Steve Eis(2026-09-17) · 금리인상에도 나스닥이 떡상한 진짜 이유(2026-09-17) · Market has 'all the ingredient(2026-09-21) · “1000주면 460만 원?”…삼성전자 배당, 28일까(2026-09-22) · "그냥 이거 사"...트럼프와 미국이 대놓고 밀어주고 (2026-09-19) …
- 제목 특징: 물음표 ? 28% · 코스피·폭락·급락·하락장 18% · S&P500·ETF·지수·나스닥 16% · 느낌표 ! 11% · 패턴형(공통점·특징·이유·N가지·착각·과정) 10% · AI 10%
- 자주 쓴 제목 낱말: 코스피(48), Market(47), Stocks(42), 이유(40), Stock(36), to(36), ETF(34), 주식(33), 대표(31), AI(25)
- 글 출처: 자막 2 · 음성인식 4 · 설명으로 대신 479 · 없음 31 · 말 속도 중앙값 2.9 음절/초 (자막·음성인식) · 타임라인 있는 영상 37%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(162), in(153), is(150), of(147), on(136), this(135), or(119), are(116), video(108), not(106), investment(104), financial(102)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 173,315개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 6% · 2026 시장(폭락·불장·서킷) 6% · 경험(내 얘기·나도 잃음) 4% · 칭찬·감사 4% · **어느 갈래에도 안 듦 61%** (모든 댓글 유형은 `comment_types.md`)
  - 👍4,560 “India needs its own social media”
  - 👍3,443 “Companies used to IPO to grow, now they IPO to cash out.”
  - 👍3,110 “Social Media is enemy of India”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 7주

- 이번 주에 새로 들어온 영상 24개: "당신이 주식으로 망할 수밖에 없던 이유" 개미 99%(2026-09-10) · "환율 완전히 뒤집혔다" 지금부터 봐야할 수혜주ㅣ지식인(2026-09-13) · ETF 이 '2가지'만 사두면 됩니다. '나머지는 필요(2026-09-14) · HDFC Bank Stock: A BIG Trigger(2026-09-12) · 분배금이 따박따박 나온다고 다 좋은 게 아닙니다. 커버(2026-09-12) · 退場者発生、でも生き残れ！【S&P500, NASDAQ10(2026-09-12) …
- 제목 특징: 물음표 ? 28% · 코스피·폭락·급락·하락장 18% · S&P500·ETF·지수·나스닥 17% · 느낌표 ! 11% · 패턴형(공통점·특징·이유·N가지·착각·과정) 10% · AI 10%
- 자주 쓴 제목 낱말: Market(49), 코스피(48), Stocks(44), 이유(43), Stock(38), to(38), ETF(36), 주식(36), 대표(33), S&P500(25)
- 글 출처: 자막 2 · 음성인식 5 · 설명으로 대신 501 · 없음 32 · 말 속도 중앙값 2.9 음절/초 (자막·음성인식) · 타임라인 있는 영상 36%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(169), in(160), is(157), of(153), on(141), this(140), or(125), are(120), video(113), not(108), investment(107), financial(106)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 183,853개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 6% · 2026 시장(폭락·불장·서킷) 6% · 경험(내 얘기·나도 잃음) 4% · 칭찬·감사 4% · **어느 갈래에도 안 듦 61%** (모든 댓글 유형은 `comment_types.md`)
  - 👍4,560 “India needs its own social media”
  - 👍3,443 “Companies used to IPO to grow, now they IPO to cash out.”
  - 👍3,110 “Social Media is enemy of India”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 8주

- 이번 주에 새로 들어온 영상 22개: 주식 공부부터 하면 지칩니다. 6년 투자 후 깨달은 것(2026-09-08) · Michael Burry Just Bet on a $3(2026-09-07) · 나스닥 최악의 달 9월, “그런데… 또 놀라서 파실거예(2026-09-02) · 【NASDAQ100vsFANG+】FANG+一択のハセンが(2026-09-07) · 다음주 코스피 심상치 않습니다 '이때' 팔고 바로 현금(2026-09-03) · '2가지' ETF만 모아도 됩니다. 100억 자산관리사(2026-09-02) …
- 제목 특징: 물음표 ? 28% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 17% · 느낌표 ! 11% · 패턴형(공통점·특징·이유·N가지·착각·과정) 11% · AI 10%
- 자주 쓴 제목 낱말: Market(51), 코스피(49), 이유(46), Stocks(44), ETF(40), Stock(39), 주식(38), to(38), 대표(34), S&P500(27)
- 글 출처: 자막 2 · 음성인식 6 · 설명으로 대신 522 · 없음 32 · 말 속도 중앙값 2.9 음절/초 (자막·음성인식) · 타임라인 있는 영상 36%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(175), in(165), is(163), of(159), on(146), this(145), or(130), are(126), video(118), not(113), investment(112), market(110)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 190,297개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 6% · 2026 시장(폭락·불장·서킷) 6% · 경험(내 얘기·나도 잃음) 4% · 칭찬·감사 4% · **어느 갈래에도 안 듦 61%** (모든 댓글 유형은 `comment_types.md`)
  - 👍4,560 “India needs its own social media”
  - 👍3,443 “Companies used to IPO to grow, now they IPO to cash out.”
  - 👍3,110 “Social Media is enemy of India”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 9주

- 이번 주에 새로 들어온 영상 20개: 부동산 버블이 터지고, 주식 시장으로 몰려가는 중국인들(2026-08-29) · [주식차트보는법] 단타말고 이 '차트패턴' 하나로 꾸준(2026-08-30) · Dividend Stocks vs. Growth Sto(2026-08-31) · 강제 장기투자로 들어간 K-개미들(2026-08-31) · "반도체 폭락해도 안 팔아" 25년 주식 해보니 이것만(2026-08-27) · 40대 은퇴 후 월급 대신 배당 받으며 사는 법｜실제 (2026-08-31) …
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 17% · 패턴형(공통점·특징·이유·N가지·착각·과정) 11% · 느낌표 ! 10% · AI 10%
- 자주 쓴 제목 낱말: Market(51), 코스피(49), 이유(47), Stocks(46), 주식(41), ETF(40), Stock(39), to(38), 대표(35), S&P500(29)
- 글 출처: 자막 2 · 음성인식 7 · 설명으로 대신 539 · 없음 34 · 말 속도 중앙값 2.9 음절/초 (자막·음성인식) · 타임라인 있는 영상 37%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(179), in(168), is(165), of(162), on(147), this(147), or(132), are(129), video(120), not(115), investment(114), financial(112)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 198,432개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 6% · 2026 시장(폭락·불장·서킷) 5% · 경험(내 얘기·나도 잃음) 4% · 칭찬·감사 4% · **어느 갈래에도 안 듦 61%** (모든 댓글 유형은 `comment_types.md`)
  - 👍4,560 “India needs its own social media”
  - 👍3,443 “Companies used to IPO to grow, now they IPO to cash out.”
  - 👍3,110 “Social Media is enemy of India”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 10주

- 이번 주에 새로 들어온 영상 14개: S&P500 ETF 좋다고 투자해도 90%가 망하는 이(2026-08-26) · I Let AI Invest for Me on Trad(2026-08-21) · Gold अभी खरीदे या रुके? | SAGA(2026-08-22) · 삼성전자 100조 환원 발표 임박, 자사주 소각 못 하(2026-08-21) · 나스닥 2배 QLD 무지성 적립식매수 vs. 공포탐욕지(2026-08-20) · I Own 2,444 Shares of SCHD. He(2026-08-20) …
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 11% · 느낌표 ! 10% · AI 10%
- 자주 쓴 제목 낱말: Market(51), 이유(50), 코스피(49), Stocks(46), ETF(42), 주식(42), Stock(40), to(38), 대표(35), S&P500(30)
- 글 출처: 자막 4 · 음성인식 8 · 설명으로 대신 550 · 없음 34 · 말 속도 중앙값 2.6 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(183), in(171), is(169), of(166), on(151), this(151), or(136), are(133), video(123), not(119), investment(117), financial(115)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 204,033개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 6% · 2026 시장(폭락·불장·서킷) 5% · 경험(내 얘기·나도 잃음) 4% · 칭찬·감사 4% · **어느 갈래에도 안 듦 61%** (모든 댓글 유형은 `comment_types.md`)
  - 👍4,560 “India needs its own social media”
  - 👍3,443 “Companies used to IPO to grow, now they IPO to cash out.”
  - 👍3,110 “Social Media is enemy of India”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 11주

- 이번 주에 새로 들어온 영상 7개: 배당으로 사는 은퇴자가 3년 동안 겪게 되는 일 (은퇴(2026-08-17) · Plot vs Gold vs SIP vs Home Lo(2026-08-12) · 내 주변에 주식으로 돈 번 사람이 '진짜' 단 1명도 (2026-08-14) · 4200억 단타 일본 천재가 초간단 매매법, 죽어라 이(2026-08-15) · 강세장에도 분산투자 안 하면 결국 돈 잃는 이유ㅣ지식인(2026-08-15) · 라오어 무한매수법, 정말 계속 해도 될까? TQQQ·Q(2026-08-13) …
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 17% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 11% · 느낌표 ! 10% · AI 10%
- 자주 쓴 제목 낱말: 이유(52), Market(51), 코스피(49), Stocks(46), ETF(42), 주식(42), Stock(40), to(38), 대표(35), S&P500(30)
- 글 출처: 자막 5 · 음성인식 8 · 설명으로 대신 556 · 없음 34 · 말 속도 중앙값 0.0 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(185), in(173), is(171), of(168), on(153), this(153), or(138), are(134), video(125), not(121), investment(119), market(116)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 210,470개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 7% · 2026 시장(폭락·불장·서킷) 5% · 칭찬·감사 4% · 경험(내 얘기·나도 잃음) 4% · **어느 갈래에도 안 듦 61%** (모든 댓글 유형은 `comment_types.md`)
  - 👍4,560 “India needs its own social media”
  - 👍3,443 “Companies used to IPO to grow, now they IPO to cash out.”
  - 👍3,110 “Social Media is enemy of India”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 12주

- 이번 주에 새로 들어온 영상 7개: 最先端のイノベーションを先取る⁉　インベスコTV　「インベス(2026-08-05) · Ben Felix: Stock Picking Is De(2026-08-06) · 10 Stocks To Buy Before The Ne(2026-08-10) · 월 100만원 ETF 투자하면, 60대에 "진짜 부자"(2026-08-11) · THIS New 20% Dividend ETF Just(2026-08-11) · 단타 5년차가 알려준 ＂잃지 않는 법＂ 딱 3가지 ｜ (2026-08-09) …
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 10% · AI 10%
- 자주 쓴 제목 낱말: 이유(53), Market(51), 코스피(50), Stocks(47), ETF(44), 주식(42), Stock(41), to(38), 대표(35), S&P500(30)
- 글 출처: 자막 7 · 음성인식 9 · 설명으로 대신 560 · 없음 34 · 말 속도 중앙값 0.0 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(187), in(176), is(174), of(171), on(156), this(156), or(141), are(137), video(127), not(124), investment(122), market(119)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 211,856개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 7% · 2026 시장(폭락·불장·서킷) 5% · 칭찬·감사 4% · 경험(내 얘기·나도 잃음) 4% · **어느 갈래에도 안 듦 61%** (모든 댓글 유형은 `comment_types.md`)
  - 👍4,560 “India needs its own social media”
  - 👍3,443 “Companies used to IPO to grow, now they IPO to cash out.”
  - 👍3,110 “Social Media is enemy of India”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 13주

- 이번 주에 새로 들어온 영상 9개: 어떤 투자는 '도박'이다? 주식 투자 때문에 인생이 무(2026-08-02) · "27년까지 오른다" 현금 1천만원 있다면 '딱 3개만(2026-08-02) · 물린 주식 10년, 결국 전부 팔았습니다 (feat. (2026-08-02) · 불기둥 세운 코스피, 코스닥! 폭등한 이유와 향후 전략(2026-07-31) · '5천피' 예언적중한 문남중 "코스피 저점? 5040 (2026-07-30) · I Own 300 Shares of SCHD - Her(2026-07-30) …
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 17% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 10% · AI 9%
- 자주 쓴 제목 낱말: 이유(54), 코스피(52), Market(52), Stocks(47), ETF(45), 주식(44), Stock(42), to(38), 대표(35), S&P500(31)
- 글 출처: 자막 7 · 음성인식 11 · 설명으로 대신 567 · 없음 34 · 말 속도 중앙값 0.0 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(189), in(177), is(175), of(172), on(156), this(156), or(141), are(137), video(128), not(125), investment(122), market(119)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 227,351개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 10% · 원칙·정답(시청자가 스스로 씀) 7% · 2026 시장(폭락·불장·서킷) 5% · 경험(내 얘기·나도 잃음) 4% · 칭찬·감사 4% · **어느 갈래에도 안 듦 60%** (모든 댓글 유형은 `comment_types.md`)
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”
  - 👍5,417 “My favorite thing about marketing Mondays are they’re every Monday you can always count on the consistency”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 14주

- 이번 주에 새로 들어온 영상 7개: 남들 다 벌었다는데 나도 주식 한번 해봐..!?(2026-07-24) · "안정을 기대한다"더니 하루만에 코스피 -10.84%🔥(2026-07-28) · 복리가 부를 만드는 진짜 시작점｜언제부터 돈이 스스로 (2026-07-22) · Kriz Dinlemeyen Liste: Her Ay (2026-07-26) · 본격 실전투자! 주린이 탈출하기 「주식투자는 처음이라 (2026-07-27) · Stop Guessing! Growth vs Divid(2026-07-24) …
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 17% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · AI 9%
- 자주 쓴 제목 낱말: 이유(54), 코스피(53), Market(52), Stocks(48), ETF(46), 주식(45), Stock(42), to(38), 대표(35), S&P500(31)
- 글 출처: 자막 7 · 음성인식 11 · 설명으로 대신 574 · 없음 34 · 말 속도 중앙값 0.0 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(190), in(179), is(176), of(173), on(157), this(157), or(142), are(138), video(130), not(126), investment(123), market(120)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 231,201개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 10% · 원칙·정답(시청자가 스스로 씀) 7% · 2026 시장(폭락·불장·서킷) 5% · 경험(내 얘기·나도 잃음) 5% · 칭찬·감사 5% · **어느 갈래에도 안 듦 60%** (모든 댓글 유형은 `comment_types.md`)
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”
  - 👍5,417 “My favorite thing about marketing Mondays are they’re every Monday you can always count on the consistency”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 15주

- 이번 주에 새로 들어온 영상 11개: 5년째 마이너스인데 왜 안 파나요? 배당투자, 커버드콜(2026-07-21) · 【資産公開】S&P500に1000万入れて5年間放置した結果(2026-07-18) · I've Invested in Dividends for(2026-07-21) · 레버리지 ETF 상장폐지 논란🔥도박판 코스피 알고도 레(2026-07-17) · S&P500 하나로 채운 ISA 3년 투자 총정리 | (2026-07-19) · 생활비 한 달 5만원..10년 만에 배당금 월 300만(2026-07-17) …
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · 이유 9%
- 자주 쓴 제목 낱말: 이유(57), 코스피(54), Market(52), Stocks(48), ETF(47), 주식(45), Stock(42), to(38), 대표(35), S&P500(33)
- 글 출처: 자막 8 · 음성인식 12 · 설명으로 대신 583 · 없음 34 · 말 속도 중앙값 0.0 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(193), in(182), is(179), of(176), this(160), on(159), or(145), are(141), video(133), not(129), investment(125), financial(123)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 244,908개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 10% · 원칙·정답(시청자가 스스로 씀) 8% · 칭찬·감사 5% · 2026 시장(폭락·불장·서킷) 5% · 경험(내 얘기·나도 잃음) 5% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 16주

- 이번 주에 새로 들어온 영상 9개: 사형수 박정희, 그를 살린 28세 정보국장 백선엽의 위(2026-07-10) · "역대급 저평가라던 코스피" 하루 만에 620조 추락.(2026-07-13) · 수익 -60%에서 멘탈 관리하는 법..?? 주식 물린 (2026-07-12) · 일 안하고, 배당금으로 살아가는 현실(2026-07-11) · If I started investing in Oct (2026-07-12) · 주식 고수들은 폭락장에 '이렇게' 행동합니다ㅣ지식인초대(2026-07-14) …
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 17% · 코스피·폭락·급락·하락장 17% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · 이유 9%
- 자주 쓴 제목 낱말: 이유(57), 코스피(57), Market(52), Stocks(48), ETF(47), 주식(47), Stock(42), to(38), 대표(36), S&P500(33)
- 글 출처: 자막 9 · 음성인식 13 · 설명으로 대신 590 · 없음 34 · 말 속도 중앙값 0.0 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(194), in(183), is(180), of(177), this(161), on(159), or(146), are(141), video(134), not(130), investment(126), financial(124)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 251,151개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 10% · 원칙·정답(시청자가 스스로 씀) 8% · 칭찬·감사 5% · 2026 시장(폭락·불장·서킷) 5% · 경험(내 얘기·나도 잃음) 5% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 17주

- 이번 주에 새로 들어온 영상 6개: What Happens If You Invest $10(2026-07-06) · [월가아재] 수익률 2% 차이? 40년 뒤에는 140억(2026-07-07) · "S&P500 ETF, 종목보다 '계좌'가 20년 뒤를(2026-07-07) · 월급없는 현실, 일하지않고 배당금만 받고 살아가는 미혼(2026-07-04) · "원금 안 깎여요" 진화형 커버드콜 ETF 황금 포트폴(2026-07-02) · The Story Behind India's Bigge(2026-07-05)
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · 이유 9%
- 자주 쓴 제목 낱말: 이유(58), 코스피(57), Market(53), ETF(49), Stocks(48), 주식(47), Stock(43), to(38), 대표(36), S&P500(34)
- 글 출처: 자막 9 · 음성인식 14 · 설명으로 대신 595 · 없음 34 · 말 속도 중앙값 0.0 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(196), in(183), is(182), of(179), this(163), on(159), or(147), are(142), video(136), not(131), investment(126), financial(125)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 253,792개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 10% · 원칙·정답(시청자가 스스로 씀) 8% · 칭찬·감사 5% · 2026 시장(폭락·불장·서킷) 5% · 경험(내 얘기·나도 잃음) 5% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 18주

- 이번 주에 새로 들어온 영상 6개: 원금 손실 우려 없는 최고의 커버드콜 ETF를 드디어 (2026-06-28) · 삼성전자 지금 시작인가? 노무라가 목표주가 67만원 제(2026-06-27) · 한국 아파트 싹 다 물갈이 된다, 2027년부터 집값 (2026-06-28) · 라오어님의 TQQQ, SOXL 무한매수법 정말 좋아합니(2026-07-01) · 코스피 9,000에도 웃지 못하는 | 고독한 ITZY((2026-06-26) · 단타 천재가 개발한 초간단 매매법(기본 차트 분석법)(2026-06-26)
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 10% · 이유 9%
- 자주 쓴 제목 낱말: 이유(58), 코스피(58), Market(53), ETF(49), Stocks(48), 주식(47), Stock(43), to(38), 대표(36), S&P500(34)
- 글 출처: 자막 9 · 음성인식 14 · 설명으로 대신 600 · 없음 35 · 말 속도 중앙값 0.0 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(196), in(183), is(182), of(179), this(163), on(159), or(147), are(142), video(136), not(131), investment(126), financial(125)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 257,624개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 10% · 원칙·정답(시청자가 스스로 씀) 8% · 칭찬·감사 5% · 2026 시장(폭락·불장·서킷) 5% · 경험(내 얘기·나도 잃음) 5% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 19주

- 이번 주에 새로 들어온 영상 7개: 삼성전자 투자자분들 주목하셔야합니다 실적은 사상 최대인(2026-06-21) · AI로 주식 자동 매매하면 어떻게 될까?(2026-06-20) · How to Borrow Against Your Sto(2026-06-20) · Best CASH Parking ETF?! Mulvih(2026-06-17) · ISA 3년마다 연금저축 이전, 진짜 이득일까? 아니면(2026-06-22) · 나스닥100 1배수, 2배수, 3배수 20년 어떤 성과(2026-06-20) …
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · AI 10%
- 자주 쓴 제목 낱말: 이유(58), 코스피(58), Market(53), ETF(50), 주식(49), Stocks(48), Stock(45), to(39), 대표(37), S&P500(34)
- 글 출처: 자막 11 · 음성인식 15 · 설명으로 대신 604 · 없음 35 · 말 속도 중앙값 0.0 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(198), in(185), is(184), of(181), this(165), on(161), or(149), are(144), video(137), not(133), investment(128), financial(127)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 260,407개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 10% · 원칙·정답(시청자가 스스로 씀) 8% · 칭찬·감사 5% · 2026 시장(폭락·불장·서킷) 5% · 경험(내 얘기·나도 잃음) 5% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 20주

- 이번 주에 새로 들어온 영상 4개: 🚀스페이스X 2700조 역대급 상장, '3번'의 매수 (2026-06-11) · 주식 상위 2%만 아는 10가지 절대 생존 원칙 (돈의(2026-06-10) · I Reinvested Dividends for 30 (2026-06-11) · QLD 직투 vs ISA, 잘 못 선택하면 10년 뒤 (2026-06-15)
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · AI 9%
- 자주 쓴 제목 낱말: 이유(58), 코스피(58), Market(53), ETF(50), 주식(50), Stocks(48), Stock(45), to(39), 대표(37), S&P500(34)
- 글 출처: 자막 14 · 음성인식 15 · 설명으로 대신 605 · 없음 35 · 말 속도 중앙값 2.6 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(199), in(186), is(185), of(182), this(166), on(162), or(150), are(145), video(138), not(134), investment(128), you(128)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 261,554개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 10% · 원칙·정답(시청자가 스스로 씀) 8% · 칭찬·감사 5% · 2026 시장(폭락·불장·서킷) 5% · 경험(내 얘기·나도 잃음) 5% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 21주

- 이번 주에 새로 들어온 영상 4개: 주식으로 전재산 날리는 사람들이 공통적으로 하는 착각 (2026-06-05) · 股市最愛修理聰明人？華爾街操盤手教你「最笨卻最賺」的投資法｜(2026-06-03) · 5 High Dividend Stocks That Co(2026-06-04) · Best Trading Strategy For Begi(2026-06-07)
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 17% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 10% · AI 9%
- 자주 쓴 제목 낱말: 이유(58), 코스피(58), Market(53), ETF(50), 주식(50), Stocks(49), Stock(45), to(39), 대표(37), S&P500(34)
- 글 출처: 자막 14 · 음성인식 15 · 설명으로 대신 609 · 없음 35 · 말 속도 중앙값 2.6 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(201), in(187), is(186), of(183), this(166), on(163), or(151), are(146), video(139), not(135), investment(129), you(129)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 270,835개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 7% · 칭찬·감사 5% · 경험(내 얘기·나도 잃음) 5% · 2026 시장(폭락·불장·서킷) 5% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 22주

- 이번 주에 새로 들어온 영상 6개: 단타 천재가 개발한 하이킨아시 스캘핑 매매법, 죽어라 (2026-06-02) · The BEST 3 ETF Portfolio for F(2026-05-27) · 매일 아침 7시, 내 포트폴리오를 관리해주는 AI 주식(2026-05-28) · [슬기로운 금융생활] 국장 복귀하면 양도세 감면?! –(2026-05-29) · 나스닥 투자하기 전에 이 영상 꼭 보세요 | QLD만 (2026-06-02) · 월배당 ETF 10억 투자하면 정말 배당금 얼마? | (2026-05-31)
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · AI 9%
- 자주 쓴 제목 낱말: 이유(59), 코스피(58), Market(53), ETF(52), 주식(51), Stocks(49), Stock(45), to(39), 대표(37), S&P500(34)
- 글 출처: 자막 14 · 음성인식 15 · 설명으로 대신 615 · 없음 35 · 말 속도 중앙값 2.6 음절/초 (자막·음성인식) · 타임라인 있는 영상 39%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(202), is(187), in(187), of(184), this(167), on(163), or(152), are(146), video(140), not(135), you(130), investment(129)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 273,981개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 8% · 칭찬·감사 5% · 경험(내 얘기·나도 잃음) 5% · 2026 시장(폭락·불장·서킷) 5% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 23주

- 이번 주에 새로 들어온 영상 9개: ISA 계좌, S&P500 하나로 3년 굴리면 얼마 벌(2026-05-24) · QLD로 10억 만들고 싶다면, 적어도 이 영상 정도는(2026-05-27) · 【オルカンvsS&P500】2026年どっちが正解？｜乗り換(2026-05-23) · "노후는 완벽하게 해결됩니다" 월급에서 딱 50만 원만(2026-05-20) · ETF 2개 + 절세 계좌 3개, 이 순서대로 채우면 (2026-05-22) · This $85,000 Portfolio Helps M(2026-05-23) …
- 제목 특징: 물음표 ? 27% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · AI 9%
- 자주 쓴 제목 낱말: 이유(59), 코스피(58), Market(54), ETF(53), 주식(51), Stocks(49), Stock(45), to(39), 대표(37), S&P500(35)
- 글 출처: 자막 16 · 음성인식 15 · 설명으로 대신 622 · 없음 35 · 말 속도 중앙값 5.3 음절/초 (자막·음성인식) · 타임라인 있는 영상 39%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(205), is(191), in(191), of(188), this(170), on(165), or(155), are(149), video(144), not(139), you(133), investment(132)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 284,595개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 7% · 칭찬·감사 5% · 경험(내 얘기·나도 잃음) 5% · 2026 시장(폭락·불장·서킷) 5% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 24주

- 이번 주에 새로 들어온 영상 7개: 트럼프의 폭탄 선언으로 삼성전자와 한국 주식시장, 조정(2026-05-16) · 배당 10%를 주면서 동시에 주가도 20% 오른 단 6(2026-05-15) · 한국 투자자 실전 가이드 한국에서 SpaceX 주식 사(2026-05-19) · "삼성전자 SK하이닉스 2배 레버리지 ETF", 사도 (2026-05-15) · 초등학생도 이해하는 차트 기초 15분 정리(2026-05-16) · 월 100만 원으로 QLD 적립식 투자하면 10억 은퇴(2026-05-20) …
- 제목 특징: 물음표 ? 26% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 16% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · 이유 9%
- 자주 쓴 제목 낱말: 이유(60), 코스피(58), ETF(55), Market(54), 주식(52), Stocks(49), Stock(45), to(39), 대표(37), S&P500(35)
- 글 출처: 자막 16 · 음성인식 15 · 설명으로 대신 629 · 없음 35 · 말 속도 중앙값 5.3 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(206), is(192), in(192), of(188), this(171), on(165), or(155), are(150), video(145), not(139), 투자(134), you(134)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 285,959개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 11% · 원칙·정답(시청자가 스스로 씀) 7% · 칭찬·감사 6% · 경험(내 얘기·나도 잃음) 5% · 2026 시장(폭락·불장·서킷) 5% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 25주

- 이번 주에 새로 들어온 영상 11개: 주식 AI 비서 4명 만들었더니 공부가 쉬워졌어요 (제(2026-05-11) · 나이키 옷 추천하고 Nike 주식도 줍줍(2026-05-07) · 배당 ETF 10억 투자하면 진짜 배당금 얼마? | 공(2026-05-08) · 경제신문 무료로 보는법 📰 (경제공부 초보 읽는 방법 (2026-05-10) · 삼전·하이닉스 '2배 레버리지 ETF', 5월 22일 (2026-05-07) · "삼성전자 SK하이닉스 2배 레버리지 ETF" 5월 2(2026-05-08) …
- 제목 특징: 물음표 ? 26% · S&P500·ETF·지수·나스닥 18% · 코스피·폭락·급락·하락장 15% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · AI 9%
- 자주 쓴 제목 낱말: 이유(60), 코스피(58), ETF(58), Market(54), 주식(53), Stocks(49), Stock(45), to(39), 대표(37), S&P500(36)
- 글 출처: 자막 19 · 음성인식 15 · 설명으로 대신 637 · 없음 35 · 말 속도 중앙값 5.3 음절/초 (자막·음성인식) · 타임라인 있는 영상 38%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(208), in(194), is(193), of(190), this(173), on(167), or(157), are(151), video(146), not(140), 투자(137), you(136)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 300,763개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 12% · 원칙·정답(시청자가 스스로 씀) 7% · 칭찬·감사 5% · 경험(내 얘기·나도 잃음) 5% · 2026 시장(폭락·불장·서킷) 5% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 26주

- 이번 주에 새로 들어온 영상 5개: These 2 NEW Weekly Dividend ET(2026-05-01) · 국민연금 빈칸 메우는 한국 ETF 3개 — 월 200만(2026-04-29) · The ONLY 5 ETFs You Need for F(2026-04-29) · 노후 걱정 끝, 커버드콜로 평생 월급받는 법 | 커버드(2026-04-30) · 경제공부 시작하는 법 | 하루 10분이면 됩니다! (해(2026-05-03)
- 제목 특징: 물음표 ? 26% · S&P500·ETF·지수·나스닥 19% · 코스피·폭락·급락·하락장 15% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · 이유 9%
- 자주 쓴 제목 낱말: 이유(61), ETF(60), 코스피(58), Market(54), 주식(53), Stocks(49), Stock(45), to(39), 대표(37), S&P500(36)
- 글 출처: 자막 20 · 음성인식 15 · 설명으로 대신 641 · 없음 35 · 말 속도 중앙값 5.3 음절/초 (자막·음성인식) · 타임라인 있는 영상 39%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(210), in(196), is(195), of(191), this(175), on(169), or(159), are(152), video(148), not(141), 투자(139), you(138)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 301,944개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 12% · 원칙·정답(시청자가 스스로 씀) 7% · 칭찬·감사 5% · 경험(내 얘기·나도 잃음) 5% · 2026 시장(폭락·불장·서킷) 4% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 27주

- 이번 주에 새로 들어온 영상 6개: I Got Rich Off NVIDIA. This Is(2026-04-27) · 5월 나스닥 폭락설? 아무도 안 알려준 돈의 이동설(2026-04-28) · Dividen Rp1 Juta Sebulan: Moda(2026-04-27) · 배당 연 1억 받아도 건보료 0원? 피부양자 지키는 2(2026-04-27) · Better Than VOO? 9 ETFs That B(2026-04-25) · Before You Buy Covered Call ET(2026-04-28)
- 제목 특징: 물음표 ? 26% · S&P500·ETF·지수·나스닥 19% · 코스피·폭락·급락·하락장 15% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · AI 9%
- 자주 쓴 제목 낱말: 이유(61), ETF(60), 코스피(58), Market(55), 주식(53), Stocks(49), Stock(45), to(39), 대표(37), S&P500(36)
- 글 출처: 자막 22 · 음성인식 15 · 설명으로 대신 645 · 없음 35 · 말 속도 중앙값 5.1 음절/초 (자막·음성인식) · 타임라인 있는 영상 39%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(213), in(199), is(198), of(194), this(178), on(172), or(162), are(154), video(152), not(144), you(141), 투자(140)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 304,578개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 12% · 원칙·정답(시청자가 스스로 씀) 7% · 칭찬·감사 5% · 경험(내 얘기·나도 잃음) 5% · 2026 시장(폭락·불장·서킷) 4% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |

## 최근 28주

- 이번 주에 새로 들어온 영상 6개: '4개 주식' 꼭 보세요. "지금이 제일 저렴합니다" (2026-04-22) · 2026년 월배당 ETF 추천 TOP 5 총정리 (커버(2026-04-21) · 스페이스X 상장 전 주가 '10배' 터질 수혜주 TOP(2026-04-17) · '외국인 프로그램 매매' 원리 모르고 주식 투자하면 호(2026-04-20) · 50대 노후준비 1억을 20억으로 만드는 가장 현실적인(2026-04-21) · "지금이 가장 저렴하다" 전쟁 직후 의외로 수혜 볼 국(2026-04-18)
- 제목 특징: 물음표 ? 26% · S&P500·ETF·지수·나스닥 19% · 코스피·폭락·급락·하락장 15% · 패턴형(공통점·특징·이유·N가지·착각·과정) 12% · 느낌표 ! 11% · 이유 9%
- 자주 쓴 제목 낱말: 이유(62), ETF(61), 코스피(58), 주식(56), Market(55), Stocks(49), Stock(45), to(39), 대표(38), S&P500(37)
- 글 출처: 자막 24 · 음성인식 15 · 설명으로 대신 649 · 없음 35 · 말 속도 중앙값 5.1 음절/초 (자막·음성인식) · 타임라인 있는 영상 39%
- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): to(213), in(199), is(198), of(195), this(178), on(172), or(162), are(154), video(152), not(144), 투자(142), you(141)
  - 설명 앞부분 — 개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초: “매주 수요일 저녁 8시 45분 tvN에서! we’re :DIGGLE family”
  - 설명 앞부분 — Stocks Have Done THIS After Ev: “⭐ See What I'm Investing In ⭐ Trade Alerts ⭐ Get Your Questions Answered ⭐ Join Our Private Chatroom ⭐ Exclusive Content About Markets 📘 My Book on Wealth-Build”
  - 설명 앞부분 — 국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실: “18일 에프앤가이드에 따르면, 지난 15일 기준 국민연금이 기분 5% 이상을 보유했다고 공시한 상장사 287곳의 주식 평가액이 333조 5330억 원으로 나타났습니다. 이는 지난 6월 말 기준 515조 9293억 원) 대비 182조 3963억 원(35.3%) 감소한 수치입니다. 사상 최”
- 댓글 306,609개 니즈: 질문 15% · 비판(가짜·AI·뻔함) 12% · 원칙·정답(시청자가 스스로 씀) 7% · 칭찬·감사 5% · 경험(내 얘기·나도 잃음) 5% · 2026 시장(폭락·불장·서킷) 4% · **어느 갈래에도 안 듦 59%** (모든 댓글 유형은 `comment_types.md`)
  - 👍16,810 “The AI bubble just K-Popped.”
  - 👍12,048 “Thank god I was starting to have my own thoughts and opinions”
  - 👍7,419 “엄청 사연있는것처럼 연출하지만 결국 빚내서한 도박”

| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |
|---|---|---|---|---|
| [한국 증시 또 급락, 언제 반등할까? (박종훈의 지식한방)](https://www.youtube.com/watch?v=hTRG4ehA6NU) | 박종훈의 지식한방 | 1,500,722 | 442,846.6 | 2026-10-12 |
| [개인 투자자도 투자하기 좋은 시대⁉️ AI를 활용한 초특급 투자 전략 공개✨ #유퀴즈](https://www.youtube.com/watch?v=jk61l5VCSGM) | 디글 클래식 :Diggle C | 2,433,812 | 392,473.4 | 2026-10-15 |
| [Stocks Have Done THIS After Every Midterm Election](https://www.youtube.com/watch?v=LaBiYw1ZKF4) | ClearValue Tax | 528,835 | 318,065.2 | 2026-10-19 |
| [국민연금 182조가 녹았다… 코스피 폭락에 대규모 손실 발생 [뉴스플레이리스트] / 채널A](https://www.youtube.com/watch?v=xQ8IpN0iQnU) | 채널A News | 891,652 | 279,939.3 | 2026-10-18 |
| [2026년 꼭 담아야 할 최고의 배당ETF 조합 ㅣ지식인 클래스 EP.29 (박곰희 작가)](https://www.youtube.com/watch?v=PaN27YpsfIU) | 지식인사이드 | 3,819,711 | 257,284.4 | 2026-10-01 |
