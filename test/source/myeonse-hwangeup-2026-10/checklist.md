# 확인표 — myeonse-hwangeup-2026-10 (일본 면세 11월부터 — 가장 빠르게 면세 받는 방법)

v5.1 — 2026-10-24 (Claude) — 사용자 지시 "시간만 확정짓기 어려운 시간들만 대략적인 수치로 수정해" — 모의실험 값을 말하는 시간만 어림수로(막대 길이·계산 값은 `sim/results.md` 그대로): 세관 창구 52→**약 50분** · 현금 단말기 46→**약 50분** · 합계 1시간 38분→**약 1시간 40분** · 단말기 줄만 94→**약 90분** · 휴대전화 3분 반→**약 3분** · 과자만 따로 49→**약 50분** · 시계 오후 4시 22분→**4시 20분쯤** · 3시 32분→**3시 반을 조금 넘겼습니다** · 빨강 4시 20분→**4시 20분쯤**. 그대로: 약 2분 · 약 50분(빨강) · 카드 약 40분 · 평균 약 8분 · 한산 약 12분 · 1시간 40분 남음. 아래 표의 숫자 칸은 v5.0 값(계산 근거)이고 대본 문장은 어림수 — 둘의 차이는 반올림(98.2→100 · 51.8→50 · 46.4→50 · 93.7→90).
v5.0 — 2026-10-24 (Claude) — 사용자가 대본을 고치다 멈춤(커밋 4daed060·0e2840f5) + 지시 "먼저 나쁜 케이스로 진행하다가 실수부분에서 딱 그렇게 하면 안된다고 하고 이유 말하고 좋은 케이스를 설명하도록 해 … 나머지 부분 그렇게 수정해봐": 출국 전 → 쇼핑할 때 → 공항에서 실수마다 '첫 번째~여섯 번째' 바른 방법 → 다 지킨 당신 → 차이 → 정리. 도착 공항 나리타(사용자 수정). 롱폼 97 → 95문장 (2,512음절 ≈ 7분 2초~7분 10초, 도입 약 28초).
- 사용자 수정본에서 빠졌던 '모의실험·가정' 안내를 공항 장면 앞(40~41)에 짧게 되살림 — 공항 시간 숫자가 실제 측정으로 읽히지 않게.
(v4.0) — 2026-10-24 (Claude) — 사용자 지시: 제목 '일본 면세 방법 변경되면 골치 아파집니다. 가장 빠르게 면세 받는 방법', 썸네일 2줄 '11월 일본 면세 변경되면 골치 아파집니다 / 가장 빠르게 면세 받는 방법', 보조 '모르면 면세 줄 n시간 / 알면 면세 줄 X!' · "너가 실제로 면세 받아야 하는 입장에서 출국 시간, 도착 구체적으로 상황 정해서 시뮬레이션 하듯이 · 도입부는 30초 이내 · 나쁜 케이스를 좋은 케이스를 비교 · 당신은 ~ 해야합니다". 롱폼 102 → 97문장, 쇼츠 11 → 9문장.
(v3.0) — 2026-10-24 — 사용자 수정·피드백(60bc17c1) 구성 · (v2.0) — 2026-10-23 · (v1.0) — 2026-10-20.

- **공항 시간 숫자는 모두 모의실험 출력** — `sim/refund_sim.py` v1.2 (`results.md` '대본에 쓰는 숫자' 표, 반복 200번, 씨앗 20261101). 단말기·창구 대수·처리 시간·빨간색 비율은 공개된 숫자가 없어 가정 → 대본 40~41에서 '실제로 잰 것이 아니라 모의실험 · 가정이라 실제와 다를 수 있음'을 말함.
- 제도(영수증 단위·짐 맡기기 전·90일·초록/빨강·휴대전화 수속·수수료)는 관광청·국세청·세관 공식 안내.
- 상태: ✅ 공식·원문 · ✅² 여러 자료가 일치 · ⚠️ 한 곳 또는 공식 아님 · 🧮 모의실험(가정) 출력
- 길이: 롱폼 2,512음절 → H17 실제 속도(0.168~0.171초/음절)로 **약 7분 2초~7분 10초**, 도입(1~6) 약 28초, 쇼츠 약 39초.
- 제목 `title_fit`: 사용자 제목은 모바일·PC 홈·검색은 2줄 안, **PC '다음 동영상'은 3줄** (❌) — 2줄 안 대안 '일본 면세 바뀌면 골치 아파요, 가장 빠르게 받는 법' (29자 ✅). 쇼츠 '일본 면세 바뀌면 공항 줄 1시간 반, 알면 2분' ✅.

## 근거 공식 자료
- 財務省「令和7年度税制改正」소비과세 팸플릿 https://www.mof.go.jp/tax_policy/publication/brochure/zeisei2025_pdf/zeisei25_03.pdf
- 財務省 令和7年度 税制改正大綱 https://www.mof.go.jp/tax_policy/tax_reform/outline/fy2025/07taikou_04.htm
- 国税庁「リファンド方式のイメージ」https://www.nta.go.jp/publication/pamph/shohi/menzei/201805/pdf/0025003-110_01.pdf · Q&A(概要編) https://www.nta.go.jp/publication/pamph/shohi/menzei/201805/pdf/0025003-110_02.pdf · 리플릿 https://www.nta.go.jp/publication/pamph/shohi/menzei/201805/pdf/caution_en.pdf
- 観光庁 여행자 특설 페이지 https://www.mlit.go.jp/kankocho/tax-free/page01_000001_00021.html · FAQ https://www.mlit.go.jp/kankocho/tax-free/page01_000001_00023.html · 면세점용 FAQ https://www.mlit.go.jp/kankocho/tax-free/page01_000001_00024.html
- 재무성 작성 자료 (관광청 게재) https://www.mlit.go.jp/kankocho/content/001858413.pdf
- 国税庁 タックスアンサー No.6303 (세율) https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6303.htm

### v2.0 에 더한 근거
- 외국인관광객 등에 대한 부가가치세 및 개별소비세 특례규정 [시행 2026-01-02] [대통령령 제35947호, 2025-12-30 공포] — legalize-kr 미러 9e88a7978e (`kr/외국인관광객등에대한부가가치세및개별소비세특례규정/대통령령.md`) · 같은 이름 시행규칙 [시행 2026-01-02]
- 관세법 시행규칙 [시행 2026-07-31] — legalize-kr e5af9ea9a6, 제48조
- 영국: 런던시 데이터 블로그 https://data.london.gov.uk/blog/the-impact-of-ending-tax-free-shopping-on-the-uk-and-london-economies/ · ICAEW https://www.icaew.com/insights/tax-news/2020/Sep-2020/Changes-to-retail-exports-and-duty-free-shopping
- 싱가포르: 세관 https://www.customs.gov.sg/at-customs/departing-singapore/tourist-refund-scheme/ · IRAS https://www.iras.gov.sg/irashome/Schemes/GST/Tourist-Refund-Scheme/
- 프랑스: 세관 PABLO https://www.douane.gouv.fr/fiche/eligibility-vat-refunds-pablo · 최소 금액(비공식) https://lepetitjournal.com/expat-pratique/installation/detaxer-achats-france-5-nouveautes-de-2021-302722 · https://www.westfield.com/fr/france/forumdeshalles/services/detaxe
- 일본 공항 현금 환급 단말기: 트래블보이스 2026-10-21 https://www.travelvoice.jp/20261021-160714 (일본공항빌딩·글로리 발표 기사)
- 댓글: YouTube Data API 2026-10-23 — 면세 영상 12개 (7J_X2F-kFOY 카모아 · VcWMzpmJIlI 모르면 알려줄게 · cMithrJqVi8 우미관 · TqPH1y67kU0 나루호도군 · lfygDKVi7zU · myFweT6GL1A · sWbpcdfpB_8 · BO__u6TmLzQ · dfIa61k5y9g · 3iYH7now4K8 · VLPS7j6pKoc · _-8nQi4x6e8), 관련도 순 댓글 504개, 작성자 이름 저장 안 함

### v3.0 에 더한 근거
- 재무성 작성 자료 (관광청 게재 PDF 001858413) 같은 표: 「1億円以上の高額購入者の9割近くが捕捉できておらず」(사람 기준 → 대본 '10명 중 9명 가까이') · 「税関の検査は任意で、検査を受けないことを理由に出国を止めることはできない」
- 자민당 의원 면세 폐지 제안 · 당시 재무상 반론: 가나가와신문 https://www.kanaloco.jp/news/government/article-1134547.html (중의원 재무금융위원회) · 후속 질의 https://www.kanaloco.jp/news/government/article-1147788.html
- 업계 공동 제언서 (2025-09-30, 일본백화점협회·전국면세점협회 등): https://www.depart.or.jp/upload/files/menzeikyodo.pdf · 보도 https://honichi.com/news/2025/10/10/tax-exemption-system/ ('폐지하면 방일객 소비 1조 4,304억 엔 감소' 추산)
- 미즈호은행 산업조사부 보고서 (트래블보이스 2025-09-24): https://www.travelvoice.jp/20250924-158373 (2024년 면세 구매액 약 1.2조 엔 → 새 제도로 1.7조 엔 정도까지 가능, '여행자 편의는 떨어지지만 면세점 비율이 늘어 제도 소구력↑')
- 영국 폐지 뒤 주장: 포천 2024-05 https://fortune.com/europe/2024/05/09/shoppers-tax-free-london-paris-milan-post-brexit · BoF https://businessoffashion.com/news/retail/thousands-of-shoppers-swapped-london-for-eu-since-tourist-tax/ (정부 '세수 도움·관광객 안 줄어' vs 업계·글로벌블루 '프랑스·이탈리아로')
- 싱가포르 창이공항 출국 안내 https://www.changiairport.com/en/airport-guide/departing/immigration-and-customs.html (부칠 물건은 체크인 전 출국장 단말기 · 카드 환급 10일 안 · 수수료 뗄 수 있음)
- 프랑스 세관 PABLO 안내 https://douane.gouv.fr/sites/default/files/2024-07/01/la-detaxe-avec-pablo.pdf (매장 면세 서류 bordereau 를 단말기에)
- 호주 ABF·ATO 관광객 환급(TRS) https://www.abf.gov.au/entering-and-leaving-australia/tourist-refund-scheme · https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/international-transactions/gst-free-sales-to-travellers-departing-australia/tourist-refund-scheme (한 ABN 300호주달러 이상 · 출국 60일 안 구매 · 출국 심사 뒤 TRS 창구 · 출발 30분 전까지 · 현금 환급 없음)

### v4.0 에 더한 근거
- 관광청 리판드 방식 안내(영문) https://www.mlit.go.jp/kankocho/tax-free/page01_000001_00028.html · 여행자 FAQ https://www.mlit.go.jp/kankocho/tax-free/page01_000001_00027.html — 휴대전화(비지트 재팬 웹) 수속은 일곱 개 공항, 국제선 출발 로비 전용 와이파이(보안 검사장 전), 미리 설정해야 함, 안 되면 단말기 · 초록 = 끝 / 빨강 = 세관 검사장
- 관광청 자료 PDF https://www.mlit.go.jp/kankocho/tax-free/content/001978459.pdf — 초록·빨강 판정 (기준은 공개 안 됨)
- 하네다 3터미널 현금 환급 단말기 = 3층 출발 콘코스 출국 후 구역 · 24시간, 나리타는 출국 전 구역: 트래블보이스 https://www.travelvoice.jp/20261021-160714 · 에어라인와이어 https://www.aviationwire.jp/?p=352831 (일본공항빌딩·글로리 발표)
- 모의실험: `test/source/myeonse-hwangeup-2026-10/sim/refund_sim.py` v1.1 · `results.md`

## 문장별 근거 (롱폼 95문장 — v5.0)
| 문장 | 내용 | 근거 | 상태 |
|---|---|---|---|
| 1 | 11/1부터 출국하는 공항에서 세관 확인을 받아야 세금 환급 | 財務省 팸플릿 · 国税庁 이미지 PDF | ✅ |
| 2, 49~50 | 모르면 붐비는 날 면세에만 1시간 반 넘게 (약 1시간 38분 = 세관 창구 약 52분 + 현금 단말기 약 46분) | refund_sim S1 · 붐빔 · 평균 98.2 = 51.8 + 46.4 | 🧮 |
| 3 | 최악의 경우 2시간 반 넘게 | refund_sim S1 · 붐빔 · 상위 10% 153.3분 (씨앗 1·2: 152.0·153.0) | 🧮 |
| 4, 68 | 알면 최소 약 2분 · 오후 3시 32분 | refund_sim S6 · 붐빔 · 초록 가운데값 2.3 | 🧮 |
| 7, 17, 27, 37~38 | 당신 · 도쿄 3박 4일 · 돈키호테 과자+화장품 한 영수증 · 옷 3만 3천 엔 · 오후 6시 출발 · 오후 3시 반 나리타 도착 | 가상 설정 | (설정) |
| 8 | 비지트 재팬 웹 = 입국 심사·세관 신고에도 쓰는 일본 정부 웹 서비스 | 디지털청 비지트 재팬 웹 안내 | ✅ |
| 9~12 | 미리 설정 안 하면 휴대전화 수속 못 씀 · 일곱 개 공항 = 나리타·하네다·간사이·주부·후쿠오카·신치토세·나하 | 관광청 리판드 방식 안내(영문)·FAQ | ✅ |
| 14~15 | 공항 밖에서는 안 됨 · 출발 로비 보안 검사장 전 전용 와이파이에서만 | 관광청 리판드 방식 안내 | ✅ |
| 18~22 | 영수증 단위 · 하나라도 없으면 영수증 전체 환급 X → 화장품까지 X | 国税庁·税関 리플릿 · 관광청 FAQ | ✅ |
| 23~24 | 먹어서 없어진 물건이 있으면 단말기로 확인 불가 → 세관 창구에서 직접 신고 | 国税庁·税関 리플릿 ('일부 소비 → 세관 창구') | ✅ |
| 25~26 | 먹거나 쓸 물건 따로 계산 → 화장품 영수증 그대로 | 영수증 단위 규칙에서 나온 요령 | ✅ (규칙에서 끌어냄) |
| 28 | 3만 3천 엔 중 3천 엔 = 소비세 (10/110, 옷 10%) | タックスアンサー No.6303 | ✅ |
| 31 | 현금 환급 단말기 = 하네다·나리타·나하 다섯 곳 | 트래블보이스·에어라인와이어 2026-10-21 (업계 발표) | ⚠️ |
| 33 | 환급 업체 수수료 법으로 안 정해짐 | 관광청 면세점용 FAQ | ✅ (원문 확인 권장) |
| 34~36 | 살 때 환급 방법 등록 · 카드면 공항 줄 없음 · 입금 날짜 공식 설명 없음 | 관광청 자료 · FAQ | ✅ |
| 39~41 | 붐비는 저녁이라고 정함 · 모의실험 · 가정이라 실제와 다를 수 있음 | refund_sim '가정' 표 | (밝힘) |
| 42 | 세관 확인은 짐 맡기기 전 출발 로비 단말기 | 관광청 특설 페이지 · 세관 안내 | ✅ |
| 44~45 | 세관 창구 → 오후 4시 22분, 약 52분 | refund_sim S1 세관 단계 평균 51.8 | 🧮 |
| 47 | 나리타 현금 환급 단말기 = 출국 심사 전 구역 | 트래블보이스·에어라인와이어 (업계 발표) | ⚠️ |
| 48 | 현금 단말기 약 46분 | refund_sim S1 현금 단계 평균 46.4 | 🧮 |
| 52~54 | 짐부터 맡기면 확인 X · 되찾기 X → 캐리어 속 물건 세금 0 | 国税庁·税関 리플릿 · 관광청 FAQ | ✅ |
| 55~57 | 체크인보다 먼저 · 면세품 가방 하나 · 빨간색이면 그 가방만 | 짐 맡기기 전 규칙 + 빨강 때 물건 보여 줌 | ✅ (규칙에서 끌어냄) |
| 59~60 | 단말기 모자란 공항 가정: 단말기만 약 94분 · 휴대전화로 바꿈 약 3분 반 | refund_sim 민감도 (6대 · 빨강 10%) | 🧮 |
| 62~63 | 줄 짧으면 단말기 / 길면 휴대전화 · 안 되면 단말기 | 관광청 리판드 방식 안내 | ✅ |
| 67 | 초록 = 세관 확인 끝 | 관광청 자료 PDF | ✅ |
| 72~74 | 빨강 = 검사 필요, 기준 비공개 · 휴대전화도 같음 · 세관 검사장 | 관광청 자료 PDF · 리판드 방식 안내 | ✅ |
| 75~76 | 빨강 → 오후 4시 20분, 약 50분, 출발까지 1시간 40분 | refund_sim S6 · 붐빔 · 빨강 가운데값 49.5 | 🧮 |
| 78~79 | 관광청 '시간에 여유' · 비행기 놓쳐도 보상 X | 관광청 FAQ | ✅ |
| 81~85 | 평균 약 1시간 38분 → 과자만 따로 약 49분 · 카드로만 약 40분 줄어듦 · 다 지키면 약 8분 · 한산하면 약 12분 | refund_sim S1 98.2 · S2 48.6 · S3−S4 39.5 · S6 7.9 · S1 한산 11.8 | 🧮 |
| 86 | 붐빌수록 1시간 넘는 차이 | 98.2 − 2.3 = 95.9분 | 🧮 |
| 88~94 | 정리 6가지 + 90일 | 위 문장들 · 国税庁 리플릿 (90일) | ✅ |

## 쇼츠 (9문장)
| 문장 | 근거 |
|---|---|
| 1 | 롱폼 1 |
| 2~4 | 롱폼 37~38·17~24 (가상 설정 — 쇼츠도 나리타) |
| 5~6 | 롱폼 49 · 39~40 (모의실험 · 붐빔) 🧮 |
| 7 | 롱폼 68 🧮 |
| 8 | 롱폼 50~55 요약 (쇼핑할 때 + 공항 도착 첫 1분 — 체크인 전 줄 보고 고르기) |

## 썸네일 문구
| 문구 | 근거 |
|---|---|
| 모르면 면세 줄 1시간 반 | 롱폼 49 '약 1시간 38분' (모의실험 평균) 🧮 — '면세 줄'은 세관 창구 + 현금 단말기 줄 |
| 알면 면세 줄 X! | 롱폼 62·68 — 줄이 짧으면 단말기, 길면 휴대전화로 줄 없이 약 2분 (빨강이면 검사장 줄은 있음 — 롱폼 63~68) |

## 대본에서 뺀 것 (v4.0)
- 일본에 이득인지 손해인지(의원 폐지 제안·업계 추산·미즈호은행·영국)·다른 나라 비교·우리나라 — 사용자가 '가장 빠르게 면세 받는 방법' 중심으로 바꿈 (v3.0 문장은 git 기록에)
- 50만 엔 상한·특수 포장 폐지, 690명 자료 — 같은 까닭

## 확인 필요 (올리기 전에)
| 무엇을 | 어디서 |
|---|---|
| 하네다 3터미널 현금 환급 단말기 위치·운영 (출국 후 구역) | 하네다 공항 공식 안내 (문장 28·34) |
| 11월 1일 시행 뒤 실제 대기 시간 — 나오면 refund_sim PARAMS 고쳐 다시 | 관광청·공항 발표, 보도 |
| 관광청 면세점용 FAQ 수수료 문구 | 문장 49 |
