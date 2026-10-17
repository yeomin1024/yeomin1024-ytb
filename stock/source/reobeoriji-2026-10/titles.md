# reobeoriji-2026-10 제목 (title_guide v3.0 + stock/guides/README.md 2번)

버전: v1.0.3 — 2026-10-17 — 대본 v1.3 (페르소나 검토 2차) 문장 번호만 고침 — 제목·언어별 제목은 그대로.
버전 v1.0.2 — 2026-10-17 — 대본 v1.2 (페르소나 피드백 반영) 문장 번호만 고침 — 제목·언어별 제목은 그대로 (결말 없음 확인).
버전 v1.0.1 — 2026-10-17 — 대본 v1.1 문장 번호만 고침 (도입 + 규칙 30초 안 — 제목은 그대로).
버전 v1.0 — 2026-10-16 — 최초. 잣대 = **매달 같은 돈($500)을 27년 모은 뒤 남은 돈** · 비교 상대 = **1배 QQQ 계좌** · 1999-04 ~ 2026-10 (닷컴 폭락 포함, `backtest/run.py` v1.0). 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐".

- 대본: `reobeoriji-2026-10.txt` v1.3 (102문장 — 도입 s1~3·규칙 s4~5 는 결과를 말하지 않음, 결과는 '27년 결과' s34~ 와 각 확인 장 끝).
- 결과: `backtest/results.json`. ※ 연구·교육용 — 투자 권유 아님.

## 1. 제목이 지킬 것 (`stock/guides/README.md` 2번)
| 규칙 | 이 제목에서 |
|---|---|
| 결말을 말하지 않고 질문으로 끝낸다 | '…보다 더 남을까?' — 얼마나·몇 배인지 쓰지 않음 ('얼마나 더'처럼 답을 깔지 않음) |
| 맨 앞(첫 12자) = 시청자 니즈 낱말 | **'레버리지 ETF'** — 댓글 레버리지 묶음 56개 + 백테스트 요청 4개, 제목 '레버리지' 비교 +7%p |
| 조건·기준점·비교 대상·잣대를 분명히 | 조건 = '닷컴 폭락부터 27년 매달 모으면' · 대상 = 'QLD·TQQQ' · 비교 대상 = '1배 QQQ' · 잣대 = '더 남을까' |
| 사다 → 매수, 팔다 → 매도 | 해당 낱말 없음 |
| 피할 낱말 | '전략·방법'·'투자'·'이렇게'·'vs·비교·차이'·'이유' 없음 · 맨 앞 '주식'·'S&P' 없음 |
| 숫자 | '27년' (기간 27.5년) |

- 한계: '레버리지 ETF'가 맨 앞인 제목의 성공 비율은 표본이 없다 (근거 없음).

## 2. 제목 3개
| # | 제목 | 글자 | 무엇이 분명한가 / 호기심 |
|---|---|---|---|
| **R1 (추천)** | **레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까?** | 54 | 니즈 낱말 + 닷컴 폭락(위험) + 27년 적립 + 비교 대상 / 답은 질문 |
| R2 | 레버리지 2배·3배, 1999년부터 매달 500달러씩 모으면 나스닥100 1배보다 더 남을까? | 47 | 금액·시작 해가 분명 / 상품 이름이 빠짐 |
| R3 | TQQQ·QLD 장기 적립, 폭락을 두 번 겪어도 1배보다 더 남을까? 27년 백테스트하면? | 46 | 상품 이름이 맨 앞 / 질문 두 개 |

## 3. 언어별 제목 (R1의 뜻 그대로 — `upload.md` 5번)
| 코드 | 제목 | 글자 |
|---|---|---|
| ko (기본) | 레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까? | 54 |
| en | Leveraged ETFs from the dot-com crash: buying QLD and TQQQ monthly for 27 years, more than 1x QQQ? | 98 |
| hi | डॉट-कॉम गिरावट से लीवरेज ETF: 27 साल हर महीने QLD·TQQQ खरीदें तो क्या 1x QQQ से ज़्यादा बचेगा? | 94 |
| id | ETF leverage sejak krisis dot-com: beli QLD·TQQQ tiap bulan 27 tahun, sisa lebih dari 1x QQQ? | 93 |
| pt | ETFs alavancados desde a bolha pontocom: comprar QLD e TQQQ todo mês por 27 anos rende mais que QQQ? | 100 |
| es-419 | ETF apalancados desde la burbuja puntocom: ¿comprar QLD y TQQQ cada mes 27 años deja más que QQQ? | 97 |
| ja | レバレッジETF、ITバブル崩壊から27年毎月積み立てると、QLD・TQQQは1倍のQQQより多く残る？ | 52 |
| de | Hebel-ETFs ab dem Dotcom-Crash: QLD und TQQQ 27 Jahre monatlich kaufen – mehr als 1x QQQ? | 89 |
| vi | ETF đòn bẩy từ bong bóng dot-com: mua QLD, TQQQ mỗi tháng suốt 27 năm có hơn QQQ 1x không? | 90 |
| tr | Dotcom çöküşünden kaldıraçlı ETF: 27 yıl her ay QLD ve TQQQ almak 1x QQQ'dan fazla bırakır mı? | 94 |

- 모두 100자 이하 · 결과를 말하지 않음 (모두 질문) — `tools/youtube_upload.py stock reobeoriji-2026-10 --dry-run` 으로 확인.

## 4. 짝 썸네일
- [x] R1 — 짝 썸네일: thumbnail_1 (글자 없음 — `thumbnails/README.md` v1.0).

## 5. 결과 (업로드 후)
| 날짜 | 노출 클릭률 | 평균 시청 지속 | 나라·언어별 조회 | 메모 |
|---|---|---|---|---|
