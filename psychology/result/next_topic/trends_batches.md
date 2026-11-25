# 구글 트렌드 묶음 (유튜브 검색 · 한국 · 최근 12개월)

> `next_topic.py` v1.0 — 이 환경에서 trends.google.com 이 자동 요청에 HTTP 429 (구글이 막음) → 사람이 브라우저로 받는다.
> 한 번에 5개까지라 묶음마다 기준 낱말 「심리」를 넣고 4개씩 → 기준 낱말 값으로 묶음끼리 이어 붙인다 (`next_topic.py trends`).
> 받는 법: 주소 열기 → '시간 흐름에 따른 관심도' 오른쪽 위 ⤓(CSV) → 파일 이름을 `batch_NN.csv` 로 → `psychology/result/next_topic/trends/` 에 올리거나 채팅에 붙임.

01. 선물 심리, 허세, 뒷담화, 강약약강 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%EC%84%A0%EB%AC%BC%20%EC%8B%AC%EB%A6%AC%2C%ED%97%88%EC%84%B8%2C%EB%92%B7%EB%8B%B4%ED%99%94%2C%EA%B0%95%EC%95%BD%EC%95%BD%EA%B0%95&hl=ko
02. 밥값, 말꼬리, 의자 심리, 자기 얘기만 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%EB%B0%A5%EA%B0%92%2C%EB%A7%90%EA%BC%AC%EB%A6%AC%2C%EC%9D%98%EC%9E%90%20%EC%8B%AC%EB%A6%AC%2C%EC%9E%90%EA%B8%B0%20%EC%96%98%EA%B8%B0%EB%A7%8C&hl=ko
03. 나르시시스트, 가스라이팅, 손절, 자존감 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%EB%82%98%EB%A5%B4%EC%8B%9C%EC%8B%9C%EC%8A%A4%ED%8A%B8%2C%EA%B0%80%EC%8A%A4%EB%9D%BC%EC%9D%B4%ED%8C%85%2C%EC%86%90%EC%A0%88%2C%EC%9E%90%EC%A1%B4%EA%B0%90&hl=ko
04. 열등감, 눈치, 불안, 우울증 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%EC%97%B4%EB%93%B1%EA%B0%90%2C%EB%88%88%EC%B9%98%2C%EB%B6%88%EC%95%88%2C%EC%9A%B0%EC%9A%B8%EC%A6%9D&hl=ko
05. 공황장애, ADHD, 번아웃, 무기력 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%EA%B3%B5%ED%99%A9%EC%9E%A5%EC%95%A0%2CADHD%2C%EB%B2%88%EC%95%84%EC%9B%83%2C%EB%AC%B4%EA%B8%B0%EB%A0%A5&hl=ko
06. 외로움, 회피형, 애착, 이별 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%EC%99%B8%EB%A1%9C%EC%9B%80%2C%ED%9A%8C%ED%94%BC%ED%98%95%2C%EC%95%A0%EC%B0%A9%2C%EC%9D%B4%EB%B3%84&hl=ko
07. 부부싸움, 엄마, 시어머니, 사춘기 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%EB%B6%80%EB%B6%80%EC%8B%B8%EC%9B%80%2C%EC%97%84%EB%A7%88%2C%EC%8B%9C%EC%96%B4%EB%A8%B8%EB%8B%88%2C%EC%82%AC%EC%B6%98%EA%B8%B0&hl=ko
08. 친구 관계, 직장 상사, 트라우마, 분노조절 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%EC%B9%9C%EA%B5%AC%20%EA%B4%80%EA%B3%84%2C%EC%A7%81%EC%9E%A5%20%EC%83%81%EC%82%AC%2C%ED%8A%B8%EB%9D%BC%EC%9A%B0%EB%A7%88%2C%EB%B6%84%EB%85%B8%EC%A1%B0%EC%A0%88&hl=ko
09. 예민, 내향인, MBTI, 심리테스트 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%EC%98%88%EB%AF%BC%2C%EB%82%B4%ED%96%A5%EC%9D%B8%2CMBTI%2C%EC%8B%AC%EB%A6%AC%ED%85%8C%EC%8A%A4%ED%8A%B8&hl=ko
10. 거짓말, 도파민, 습관, 불면증 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%EA%B1%B0%EC%A7%93%EB%A7%90%2C%EB%8F%84%ED%8C%8C%EB%AF%BC%2C%EC%8A%B5%EA%B4%80%2C%EB%B6%88%EB%A9%B4%EC%A6%9D&hl=ko
11. 행복, 노후, 멘탈, 말투 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%ED%96%89%EB%B3%B5%2C%EB%85%B8%ED%9B%84%2C%EB%A9%98%ED%83%88%2C%EB%A7%90%ED%88%AC&hl=ko
12. 인간관계, 소시오패스 — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q=%EC%8B%AC%EB%A6%AC%2C%EC%9D%B8%EA%B0%84%EA%B4%80%EA%B3%84%2C%EC%86%8C%EC%8B%9C%EC%98%A4%ED%8C%A8%EC%8A%A4&hl=ko
