# 구글 트렌드 묶음 (유튜브 검색 · 한국 · 최근 12개월) — 재테크 (미국주식)

> `tools/next_topic.py stock` v1.3 — 클라우드는 trends.google.com 이 막힘 (환경 허용 목록 밖이면 프록시 403 · 허용해도 구글이 서버 주소 자동 요청에 HTTP 429).
> 받는 방법 둘: ① PC 에서 `powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Trends -Folder stock` (tools/pc_trends.py — 묶음을 차례로 받아 GitHub 에) ② 아래 주소를 브라우저로 열기 → '시간 흐름에 따른 관심도' 오른쪽 위 ⤓(CSV) → 파일 이름을 `batch_NN.csv` 로 → `stock/result/next_topic/trends/` 에 올리거나 채팅에 붙임.
> 한 번에 5개까지라 묶음마다 기준 낱말 「S&P500」를 넣고 4개씩 → 기준 낱말 값으로 묶음끼리 이어 붙인다 (`next_topic.py stock trends`).

01. S&P500, 미국주식, ETF, 나스닥 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=S%26P500%2CS%26P500%2C%EB%AF%B8%EA%B5%AD%EC%A3%BC%EC%8B%9D%2CETF%2C%EB%82%98%EC%8A%A4%EB%8B%A5&hl=ko
02. 엔비디아, 반도체, 환율, 배당주 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=S%26P500%2C%EC%97%94%EB%B9%84%EB%94%94%EC%95%84%2C%EB%B0%98%EB%8F%84%EC%B2%B4%2C%ED%99%98%EC%9C%A8%2C%EB%B0%B0%EB%8B%B9%EC%A3%BC&hl=ko
03. SCHD, 커버드콜, 월배당, 배당ETF — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=S%26P500%2CSCHD%2C%EC%BB%A4%EB%B2%84%EB%93%9C%EC%BD%9C%2C%EC%9B%94%EB%B0%B0%EB%8B%B9%2C%EB%B0%B0%EB%8B%B9ETF&hl=ko
04. 월배당ETF, JEPI, JEPQ, QQQ — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=S%26P500%2C%EC%9B%94%EB%B0%B0%EB%8B%B9ETF%2CJEPI%2CJEPQ%2CQQQ&hl=ko
05. 나스닥100, VOO, 미국ETF, 테슬라 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=S%26P500%2C%EB%82%98%EC%8A%A4%EB%8B%A5100%2CVOO%2C%EB%AF%B8%EA%B5%ADETF%2C%ED%85%8C%EC%8A%AC%EB%9D%BC&hl=ko
06. 레버리지, 애플, ISA, 연금저축 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=S%26P500%2C%EB%A0%88%EB%B2%84%EB%A6%AC%EC%A7%80%2C%EC%95%A0%ED%94%8C%2CISA%2C%EC%97%B0%EA%B8%88%EC%A0%80%EC%B6%95&hl=ko
07. 연금저축펀드, ISA계좌, 해외주식, 배당소득세 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=S%26P500%2C%EC%97%B0%EA%B8%88%EC%A0%80%EC%B6%95%ED%8E%80%EB%93%9C%2CISA%EA%B3%84%EC%A2%8C%2C%ED%95%B4%EC%99%B8%EC%A3%BC%EC%8B%9D%2C%EB%B0%B0%EB%8B%B9%EC%86%8C%EB%93%9D%EC%84%B8&hl=ko
08. 미국직투 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=S%26P500%2C%EB%AF%B8%EA%B5%AD%EC%A7%81%ED%88%AC&hl=ko
