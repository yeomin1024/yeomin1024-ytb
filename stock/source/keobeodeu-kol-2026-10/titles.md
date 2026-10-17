# keobeodeu-kol-2026-10 제목 (title_guide v3.0 + stock/guides/README.md 2번)

버전: v1.0.2 — 2026-10-17 — 대본 v1.2 (페르소나 피드백 반영) 문장 번호만 고침 — 제목·언어별 제목은 그대로 (결말 없음 확인).
버전 v1.0.1 — 2026-10-17 — 대본 v1.1 문장 번호만 고침 (도입 + 규칙 30초 안 — 제목은 그대로).
버전 v1.0 — 2026-10-16 — 최초. 잣대 = **같은 금액을 꺼내 쓴 뒤 남은 원금** · 비교 상대 = **같은 나스닥100을 따라가는 QQQ 에서 같은 날 같은 금액을 매도한 계좌** · QYLD 첫 거래일 2013-12-12 ~ 2026-10-15 (`backtest/run.py` v1.0). 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐".

- 대본: `keobeodeu-kol-2026-10.txt` v1.2 (97문장 — 도입 s1~3·규칙 s4~6 은 결과를 말하지 않음, 결과는 경주가 끝난 '결과' s33~ 와 각 확인 장 끝).
- 결과: `backtest/results.json`. ※ 연구·교육용 — 투자 권유 아님.

## 1. 제목이 지킬 것 (`stock/guides/README.md` 2번)
| 규칙 | 이 제목에서 |
|---|---|
| 결말을 말하지 않고 질문으로 끝낸다 | '…원금이 더 남을까?' — 어느 쪽이 남았는지·얼마인지 쓰지 않음 |
| 맨 앞(첫 12자) = 시청자 니즈 낱말 | **'커버드콜 분배금'** — 댓글 커버드콜 묶음 50개 (분배금·원금·총수익), 검색어 '커버드콜ETF' 영상당 하루 조회수 1위 |
| 조건·기준점·비교 대상·잣대를 분명히 | 조건 = '매달 꺼내 쓰면' · 비교 대상 = '같은 금액을 매도한 QQQ' · 잣대 = '13년 뒤 원금' |
| 사다 → 매수, 팔다 → 매도 | '매도한 QQQ' |
| 피할 낱말 (`data_insights.md` 2번) | '전략·방법'·'투자'·'이렇게'·'vs·비교·차이'·'이유' 없음 · 맨 앞 '주식'·'S&P' 없음 |
| 숫자 | '13년' (기간 12.8년 — 대본 '12.8년 뒤') |

- 한계: '커버드콜'이 맨 앞인 제목의 성공 비율은 표본이 없다 (근거 없음). 같은 금액을 꺼내 견주는 제목의 근거도 없다.

## 2. 제목 3개
| # | 제목 | 글자 | 무엇이 분명한가 / 호기심 |
|---|---|---|---|
| **R1 (추천)** | **커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까?** | 51 | 니즈 낱말 + 조건(매달 꺼내 씀) + 공정한 비교 대상(같은 금액 매도) + 잣대(13년 뒤 원금) / 답은 질문 |
| R2 | 커버드콜 QYLD, 분배금을 13년 동안 꺼내 쓰면 원금은 지켜질까? 같은 돈을 꺼낸 QQQ와 백테스트하면? | 58 | 상품 이름이 분명 / 질문 두 개 |
| R3 | 커버드콜 ETF 원금, 분배금을 받아 써도 안 깎일까? QYLD·XYLD·JEPI를 지수 ETF와 백테스트하면? | 60 | 확인 상품 3개 / 비교 기준(같은 금액)이 빠짐 |

## 3. 언어별 제목 (R1의 뜻 그대로 — `upload.md` 5번)
| 코드 | 제목 | 글자 |
|---|---|---|
| ko (기본) | 커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까? | 52 |
| en | Covered call payouts spent monthly: is more principal left after 13 years than selling QQQ? | 91 |
| hi | कवर्ड कॉल भुगतान हर महीने खर्च करें तो क्या 13 साल बाद QQQ बेचने से ज़्यादा मूलधन बचेगा? | 88 |
| id | Dividen covered call dipakai tiap bulan: apakah modal tersisa lebih banyak dari jual QQQ, 13 tahun? | 99 |
| pt | Renda de covered call gasta todo mês: sobra mais capital em 13 anos do que vendendo QQQ? | 88 |
| es-419 | Ingreso de covered call gastado cada mes: ¿queda más capital en 13 años que vendiendo QQQ? | 90 |
| ja | カバードコールの分配金を毎月使うと、同じ額を売るQQQより13年後に元本は多く残る？ | 42 |
| de | Covered-Call-Ausschüttung monatlich ausgeben: Bleibt nach 13 Jahren mehr als beim QQQ-Verkauf? | 94 |
| vi | Tiêu cổ tức covered call mỗi tháng: sau 13 năm vốn còn nhiều hơn bán QQQ cùng số tiền không? | 92 |
| tr | Covered call dağıtımını her ay harcarsanız 13 yıl sonra QQQ satmaktan fazla anapara kalır mı? | 93 |

- 모두 100자 이하 · 결과를 말하지 않음 (모두 질문) — `tools/youtube_upload.py stock keobeodeu-kol-2026-10 --dry-run` 으로 확인.

## 4. 짝 썸네일
- [x] R1 — 짝 썸네일: thumbnail_1 (글자 없음 — `thumbnails/README.md` v1.0).

## 5. 결과 (업로드 후)
| 날짜 | 노출 클릭률 | 평균 시청 지속 | 나라·언어별 조회 | 메모 |
|---|---|---|---|---|
