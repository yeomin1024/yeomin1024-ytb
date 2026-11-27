# 주제 밖이라 뺀 승인 영상 — `shopping/`

VERSION: v1.0 — 2026-11-27 — 첫 승인 목록(316개)을 읽고 뺌. 자료(`result/outliers/W_<ID>/`)는 받았지만 분석(성공 사례·비교 집단)에서 빠지도록 `analysis_rules.toml` [exclude] OFF_TOPIC 에 낱말을 더함.

| 영상 ID | 제목 (앞부분) | 까닭 | OFF_TOPIC 낱말 |
|---|---|---|---|
| K8EEj1qNJAQ | 전 국민이 뜯어말린 엄마뻘 아내와 살림 합친 스타 부부 충격 근황 TOP10 | 연예 소식 ('살림' 낱말만 겹침) | 충격 근황 · 스타 부부 |
| -nCoyJxG__w | 해외 골프여행 패키지 내돈내산｜중국 연태 골프장 솔직 후기 | 여행 상품 (쿠팡 살림·생활 아님) | 골프 |
| V1AN6Ma5b5Y | 50대 주부의 여름 밑반찬 7가지 | 상품 없는 레시피 | 밑반찬 |

탐색 단계에서 푼 74개(조회수 10만 아래 46 · 남성·아이돌·20대 뷰티·사연·테크 리뷰어·자취 28)는 `result/web/dismissed.json` (cloud_run uncheck 기록).
되살리기: OFF_TOPIC 에서 낱말을 지우고 `python3 tools/cloud_run.py shopping analyze`.
