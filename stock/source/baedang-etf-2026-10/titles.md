# baedang-etf-2026-10 제목 (title_guide v3.0 + stock/guides/README.md 2번)

버전: v1.0.3 — 2026-10-17 — 대본 v1.3 (페르소나 검토 2차) 문장 번호만 고침 — 제목·언어별 제목은 그대로.
버전 v1.0.2 — 2026-10-17 — 대본 v1.2 (페르소나 피드백 반영) 문장 번호만 고침 — 제목·언어별 제목은 그대로 (결말 없음 확인).
버전 v1.0.1 — 2026-10-17 — 대본 v1.1 문장 번호만 고침 (도입 + 규칙 30초 안 — 제목은 그대로).
버전 v1.0 — 2026-10-16 — 최초. 잣대 = **같은 날 같은 금액을 매달 모은 뒤 남은 돈 (배당세 15% 떼고 다시 매수)** · 비교 상대 = **S&P 500 을 따라가는 SPY 에 같은 돈을 모은 계좌** · 2011-11 ~ 2026-10 (`backtest/run.py` v1.0). 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐".

- 대본: `baedang-etf-2026-10.txt` v1.3 (95문장 — 도입 s1~3·규칙 s4~5 는 결과를 말하지 않음, 결과는 '15년 결과' s22~ 와 각 확인 장 끝).
- 결과: `backtest/results.json`. ※ 연구·교육용 — 투자 권유 아님.

## 1. 제목이 지킬 것 (`stock/guides/README.md` 2번)
| 규칙 | 이 제목에서 |
|---|---|
| 결말을 말하지 않고 질문으로 끝낸다 | '…보다 더 남을까?' — 어느 쪽이 남았는지·얼마인지 쓰지 않음 |
| 맨 앞(첫 12자) = 시청자 니즈 낱말 | **'배당 ETF'** — 댓글 배당·월배당 ETF 묶음 40개, '배당주' 작은 채널이 뚫은 비율 1위 |
| 조건·기준점·비교 대상·잣대를 분명히 | 조건 = '매달 모으면' · 기준점 = '배당세 15%를 떼고도' · 비교 대상 = '같은 돈을 모은 S&P 500' · 잣대 = '더 남을까' (남은 돈) |
| 사다 → 매수, 팔다 → 매도 | 해당 낱말 없음 |
| 피할 낱말 | '전략·방법'·'투자'·'이렇게'·'vs·비교·차이'·'이유' 없음 · 맨 앞 '주식'·'S&P' 없음 (S&P 500 은 뒤쪽 비교 대상) |
| 숫자 | '15%' (본 실험 세율) |

- 한계: '배당 ETF'가 맨 앞인 제목·세율을 넣은 제목의 성공 비율은 표본이 없다 (근거 없음).

## 2. 제목 3개
| # | 제목 | 글자 | 무엇이 분명한가 / 호기심 |
|---|---|---|---|
| **R1 (추천)** | **배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까?** | 53 | 니즈 낱말 + 조건(매달) + 세금(15%) + 같은 돈 비교 대상 / 답은 질문 |
| R2 | 배당 ETF SCHD, 15년 매달 1,000달러 모으면 세금 떼고 SPY보다 더 많이 남을까? | 46 | 상품·금액·기간이 분명 / 세율이 빠짐 |
| R3 | 배당 많이 주는 ETF가 결국 더 남을까? 배당세 15% 떼고 지수 ETF와 15년 적립하면? | 49 | 시청자 말 그대로 / 질문 두 개 |

## 3. 언어별 제목 (R1의 뜻 그대로 — `upload.md` 5번)
| 코드 | 제목 | 글자 |
|---|---|---|
| ko (기본) | 배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까? | 53 |
| en | Dividend ETF saved monthly: after 15% dividend tax, is more left than the same money in the S&P 500? | 100 |
| hi | डिविडेंड ETF हर महीने जमा करें: 15% टैक्स के बाद क्या S&P 500 में उतने ही पैसे से ज़्यादा बचेगा? | 96 |
| id | ETF dividen tiap bulan: setelah pajak dividen 15%, sisa lebih banyak dari S&P 500 dengan uang sama? | 99 |
| pt | ETF de dividendos todo mês: com 15% de imposto, sobra mais que o mesmo dinheiro no S&P 500? | 91 |
| es-419 | ETF de dividendos cada mes: con 15% de impuesto, ¿queda más que el mismo dinero en el S&P 500? | 94 |
| ja | 高配当ETFを毎月積み立てると、配当税15%を引いても同じ額のS&P 500より多く残る？ | 45 |
| de | Dividenden-ETF monatlich sparen: Bleibt nach 15 % Steuer mehr als mit gleichem Geld im S&P 500? | 95 |
| vi | Tích lũy ETF cổ tức mỗi tháng: sau thuế cổ tức 15%, có còn nhiều hơn S&P 500 với cùng số tiền? | 94 |
| tr | Temettü ETF'si her ay biriktirilirse %15 vergiden sonra aynı parayla S&P 500'den fazla kalır mı? | 96 |

- 모두 100자 이하 · 결과를 말하지 않음 (모두 질문) — `tools/youtube_upload.py stock baedang-etf-2026-10 --dry-run` 으로 확인.

## 4. 짝 썸네일
- [x] R1 — 짝 썸네일: thumbnail_1 (글자 없음 — `thumbnails/README.md` v1.0).

## 5. 결과 (업로드 후)
| 날짜 | 노출 클릭률 | 평균 시청 지속 | 나라·언어별 조회 | 메모 |
|---|---|---|---|---|
