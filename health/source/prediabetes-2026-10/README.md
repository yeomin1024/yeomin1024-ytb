# 당뇨 전단계 영상 대본 소스 (prediabetes-2026-10)

버전: v1.1 — 2026-10-11 — 1900년대 자료 근거 교체(사용자 지시 2026-10-10: 사례·연구는 최신): 미국 당뇨병 예방 연구(DPP, 1996~2001년 자료)·15년 후속 연구(DPPOS) 6문장을 빼고 영국 국가 당뇨병 예방 프로그램(PLoS Med 2023, 2016~2020년 자료) 5문장으로, 방법 여섯째 '정상 숫자로 돌아가기'(독일 PLIS, Lancet Diabetes Endocrinol 2023, 2012~2016년 자료) 8문장 추가, 식후 걷기 연구에 10명 한계 문장 추가(건강 규칙 3-2), 마무리 "다섯 가지" → "여섯 가지". 문장 86 → 94, 자막 103 → 117, 추정 끝 8:12.7 → 9:03.4. 다른 문장은 그대로 (v1.0: 2026-10-10 최초 작성, 사용자 지시: 다른 주제 새로 골라 영상 빼고 다 만들기)

> 건강 정보 제공용 원고입니다. 의사의 진단과 치료를 대신하지 않습니다.

## 파일

| 파일 | 내용 |
|---|---|
| `prediabetes-2026-10.txt` | 대본 v1.1 — **문장 94**. 파트 라벨, `[장면] 의학적 진단이 아닙니다` (문장 23 뒤). 문제 4개 / 방법 6개 |
| `prediabetes-2026-10.srt` | **문장 94 / 자막 117** (1432px 넘는 23문장은 앞줄·뒷줄), 문장 23 뒤 고지 공백 8.0초, 끝 **9:03.4** (추정치). v1.0 SRT를 `--reuse`로 다시 써서 글자가 같은 문장은 옛 길이·나눈 위치 그대로 (새로 계산 15개) |
| `titles.md` | 제목 3개 v1.1 (T1 채택, T2 결말 장치 교체) |
| `thumbnails/thumbnail_1.md` ~ `_3.md` | 썸네일 이미지 AI 프롬프트 3개 (2번만 v1.1: 짝 제목·문구 "멀쩡했는데") |
| `upload.md` | 업로드 시트 v1.1 (설명란·챕터 13개·태그·고정 댓글) |
| `summary.md` | 요약 문서 (`python3 tools/make_summary.py health prediabetes-2026-10`로 자동 생성) |

검사: `python3 tools/srt_tool.py check health/source/prediabetes-2026-10/prediabetes-2026-10.txt health/source/prediabetes-2026-10/prediabetes-2026-10.srt --expect 94/117`
→ `문장 94 / 자막 117 (나뉜 문장 23개) / SRT–TXT 일치 ✅ / 고지 공백 문장 23 뒤 8.0초 ✅ / 끝 00:09:03,377` · `✅ 이상 없음` (50자 넘는 문장 없음)
만든 명령: `python3 tools/srt_tool.py build <txt> <srt> --reuse <v1.0 SRT 사본>`
녹음 후: `video/`에서 `npm run align-audio -- health prediabetes-2026-10` (오디오는 고치지 않음, 문장 23 뒤 3.5초 이상 쉼)

## 주제를 고른 이유
- 분석(`health/result/` 실행 20261011_120552, `health/guides/data_insights.md` v1.0):
  - 키워드 **`당뇨 전단계 증상` 기회점수 59** (수집 13개 중 공동 3위), 카테고리 1. 혈당·당뇨 롱폼 성공 **5/13**, 성공 제목 단어 '혈당' 1.38배·'스파이크' 1.66배.
  - 작은 채널 성공: 「이 신호가 보인다면 이미 '당뇨 전단계'입니다ㅣ…정상으로 돌아가는 5가지 방법」 구독자 3.2천 채널 **29.6배, 10:15**.
  - 결과지 숫자 → 카테고리 3. 건강검진·나이대 관리(51점, 경쟁 채널 구독자 중앙값 1.4만)와도 겹친다.
  - 시청자 댓글(`audience_comments.csv`): "공복혈당은 잠을 잘 못자서 그런지 109로 좀 높게 나오는데", "당뇨 전단계로 6'1에서 5'8로 … 공복 혈당이 매우 불규칙하게 나와요" — 사연(108 '경계'를 넘김)과 같은 고민.
  - 롱폼 제목에 숫자가 있으면 성공 54.5% vs 18.2% (q=0.010) — 제목의 108·131과 맞음.
- 분석기 자동완성(PC 실행)에서도 "당뇨 전단계"가 관리·증상·식단·운동·수치로 이어졌다 → 사연(경계 무시) → 문제 → 방법 구조와 맞음 (v1.0 판단, 분석 뒤에도 유지 — `health/guides/title_rules.md` 4-1 후보 1위 28점)
- 주식 채널과 같은 40~60대 시청자, 결과지 숫자로 "숫자 반전" 제목을 만들 수 있음

## 사연 검산 (재구성 — 실제 진단 기준에 맞춤, v1.1에서 바뀌지 않음)
| 시점 | 나이 | 공복혈당 | 결과지 문구 | 몸무게 | 대본 |
|---|---|---|---|---|---|
| 2023 (3년 전) | 49 | 108 | 공복혈당장애 의심 (100~125) | 76kg | 문장 1~3 |
| 2024 | 50 | 116 (예시) | 공복혈당장애 의심 | — | 문장 5 "조금 올랐을 때도", 문장 32·53 "108이 116이" |
| 2025 | 51 | 122 (예시, 대본에 숫자 없음) | 공복혈당장애 의심 | — | 문장 12 "세 번이나 경고" (2023~2025) |
| 2026 (올해) | 52 | 131 | 당뇨병 의심 (126 이상) | 82kg (+6kg) | 문장 8·10 |
| 확진 검사 | | 당화혈색소 7.1% | 당뇨병 (6.5% 이상) | | 문장 9 |

- 몸무게 목표: 82kg × 5% = 4.1kg, × 7% = 5.74kg → "4~6kg 정도" (문장 66). 한 달 1kg이면 4~6개월 → "반년 안에" (문장 68)
- 주 150분 = 30분 × 5일 (문장 70)
- "넷 중 한 명은 모름" = 100 − 인지율 74.7 = 25.3% (문장 21), "열 명 중 여섯 명은 이어지지 않음" = 100 − 39 = 61% (문장 40), "셋 중 한 명꼴" = 32.4% (문장 45)
- (v1.1) 영국: 18,470명 → "1만 8천여 명", 51,331명 → "5만여 명", 위험비 0.80 → "20% 낮았습니다" (문장 63~64)
- (v1.1) 독일: 298명 중 128명 = 43.0% → "열 명에 네 명꼴" (문장 84). 모집 인원은 자료마다 1,160명(이 분석의 초록)·1,105명(다른 PLIS 보고)이라 둘 다 맞는 "천백여 명"으로 씀 (문장 82)
- (v1.1) 여섯째의 사연 예시: 108을 받았던 3년 전 사연자의 목표 = PLIS의 '정상' 기준 공복혈당 100 미만 (문장 89, 첫째 문장 50의 정상 기준과 같음)

## 숫자와 출처
"확인" 칸: **원문** = v1.0 README(2026-10-10)에 적은 원문 인용 그대로 — v1.1에서 바뀌지 않은 문장이라 다시 확인하지 않음, **검색** = 2026-10-11 이 환경에서 원문 페이지를 열 수 없어(WebFetch·curl 차단) 웹 검색 결과가 인용한 원문·초록·보도자료로 확인.

| 문장 | 대본 표현 | 값 | 출처 (원문 인용) | 자료 연도 | 확인 |
|---|---|---|---|---|---|
| 4, 31, 37~38, 50, 57 | 진단 기준 | 공복혈당 100~125 공복혈당장애 / 126 이상 당뇨병, 당화혈색소 5.7~6.4% 전단계 / 6.5% 이상 당뇨병 | 질병관리청 국가건강정보포털 「당뇨병」(2026-09-16): "공복 혈장 포도당 100~125 mg/dL로 정상(100 mg/dL 미만)보다 높지만 당뇨병(126 mg/dL 이상)은 아닌 경우", "당화혈색소가 5.7~6.4% 범위에 든다면 당뇨병 전단계" | 기관 최신 안내 (2026) | 원문 |
| 2, 8, 37~38 | 결과지 문구 | "공복혈당장애 의심", "당뇨병 의심" / 126 이상은 확진검사 대상 | 일반건강검진 결과통보서 [별지 제6호서식] (2025.1.1 개정), 질병관리청 안내: "당뇨병 의심: 공복혈당이 126 이상인 경우로, 확진검사 대상자가 됩니다." | 2025 서식 | 원문 |
| 58 | 당뇨병 의심 시 무료 진료 | 다음 해 1월 31일까지 최초 1회 본인부담 없음 | 결과통보서: "검진받은 연도의 다음연도 1월 31일까지 최초 1회 본인부담 없이 진료" | 2025 서식 | 원문 |
| 19~20 | 열 명 중 네 명, 약 1,410만 명 | 30세 이상 전단계 41.1%, 14,099,002명 | Diabetes Fact Sheets in Korea 2024, DMJ 2025;49:24-33: "approximately 14.09 million, or 41.1%" | 2021~2022 국민건강영양조사 | 원문 |
| 21 | 넷 중 한 명은 모름 | 당뇨병 인지율 74.7% | 같은 자료: "74.7% of adults with diabetes were aware of their condition" | 2021~2022 | 원문 |
| 44~45 | 32% 정도, 셋 중 한 명꼴 | 조절률(HbA1c < 6.5%) 32.4% | 같은 자료 | 2021~2022 | 원문 |
| 25, 27 | 몇 년 증상 없음, 10명 중 8명 모름 | — | CDC: "You can have prediabetes for years but have no clear symptoms." / "8 in 10 adults with prediabetes don't know they have it." (2026-02-17) | 기관 최신 안내 (2026) | 원문 |
| 34 | 5~8%가 1년 안에 | — | 질병관리청 「당뇨병」: "공복혈당장애가 있는 사람의 5~8%는 1년 안에 당뇨병으로 진행될 수 있습니다." | 기관 최신 안내 (2026) | 원문 |
| 39~40 | 39% 정도 | 당뇨병 의심 판정 후 진단·치료 연계율 | 보건복지부 제4차 국가건강검진종합계획 브리핑 (2026-06-30): "진단과 치료 연계율은 고혈압 22%, 당뇨 39% 수준" | 2026 발표 | 원문 |
| 43 | 약 383만 명 | 2023년 당뇨병 환자 382만 8,682명 | 건강보험심사평가원 보도자료 2024-11-14 | 2023 | 원문 |
| 46 | 눈·콩팥·신경 합병증 | 망막병증, 신경병증, 신장병증 | 질병관리청 「당뇨병」: "대표적인 당뇨병 합병증은 망막병증, 신경병증, 신장병증, 동맥경화로 인한 뇌졸중, 협심증, 심근경색증 등입니다." | 기관 최신 안내 | 원문 |
| 56 | 최근 두세 달 평균 혈당 | — | 질병관리청 「당뇨병」: "당화혈색소는 최근 2~3개월의 평균 혈당을 반영합니다." | 기관 최신 안내 | 원문 |
| 60, 69~70 | 5~7% 감량 목표, 주 150분 | 5~7%, 주 150분 이상 | ADA Standards of Care 2026 (Diabetes Care 49 Suppl 1) 권고 3.3: "a weight reduction of at least 5–7% … and ≥150 min/week of moderate-intensity physical activity" | 지침 2026 (최신 지침 — 건강 규칙 3-7) | 원문 |
| **61~62** (v1.1) | 영국은 2016년부터 국가 예방 프로그램에 연결, 식사·운동·체중 관리를 9개월 동안 돕는 무료 프로그램 | Healthier You: NHS Diabetes Prevention Programme | NHS England 「Healthier You」 안내 (검색 결과 인용): "personalised support on healthy eating, increasing physical activity and managing weight, which is free for eligible people" (https://www.england.nhs.uk/long-read/healthier-you-nhs-diabetes-prevention-programme-gdm/). NHS England 「NHS Diabetes Prevention Programme」 (검색 결과 인용): "refers them onto a nine-month, evidence-based lifestyle change programme", 그룹 과정은 체중 관리·식사·활동을 돕는다 (https://www.england.nhs.uk/diabetes/diabetes-prevention/). 2016년 시작: Diabetes & Primary Care 글(검색 결과 요약: 2016년에 시작한 첫 전국 규모 프로그램, https://diabetesonthenet.com/diabetes-primary-care/nhs-diabetes-prevention-programme-here-support-our-population-high-risk-type-2-diabetes/), 연구 자료도 "2016-04-01(프로그램 시작)부터" | 2016~ (현재 안내) | 검색 |
| **63~65** (v1.1) | 1만 8천여 명 / 비슷한 조건의 5만여 명, 20% 낮음, 참여가 아니라 연결 여부 비교 | 의뢰 18,470명 vs 의뢰하지 않는 병원의 51,331명(나이·성별·전단계 진단 뒤 기간으로 짝지음), 보정 위험비 0.80 | Ravindrarajah R, et al. "Referral to the NHS Diabetes Prevention Programme and conversion from nondiabetic hyperglycaemia to type 2 diabetes mellitus in England: A matched cohort analysis." *PLoS Med* 2023;20(2):e1004177. 맨체스터대 보도: "18,470 patients referred to NDPP were matched to 51,331 similar patients not referred", "the risk of Diabetes progression was 20 per cent lower"; 초록: "Patients were matched based on age, sex, and ≥365 days of NDH diagnosis"; 저자 한계: "they examined the impact of referral, rather than attendance or completion of the intervention"; Diabetes & Primary Care(검색 결과 인용): "with an adjusted HR of 0.80" | **2016-04 ~ 2020-03** (영국 1차 의료 기록 CPRD) | 검색 |
| 71~72 | 60세 이상 10명, 105~125, 식후 30분 뒤 15분, 129 → 116 | 24시간 평균혈당 | DiPietro et al., *Diabetes Care* 2013;36(10):3262-3268: "inactive older (≥60 years of age) participants (N = 10) … fasting glucose between 105 and 125", "postmeal walking (129 ± 24 vs. 116 ± 13 mg dL−1)" | 2013 발표 (2010년대 초 모집 — 2010년대, 쓸 수 있음) | 원문, 2026-10-11 검색으로 다시 확인 |
| **73** (v1.1) | 10명이 하루씩 걸어 본 작은 실험, 오래 했을 때의 효과는 알 수 없음 | — | 같은 연구: 참가자마다 48시간 호흡 측정실에서 첫날 대조, 둘째 날 걷기(4주 간격으로 세 가지 방식) — 장기 효과는 시험하지 않음 (건강 규칙 3-2 한계 문장) | 같음 | 검색 |
| 77~80 | 전단계 15명, 최고치 40% 넘게 | 탄수화물 마지막 | Shukla et al., *Diabetes Obes Metab* 2019;21:377 (전단계 대상) — **당뇨병 대상인 2015 연구(−73%)는 쓰지 않음**. 15명 한계 문장(문장 80) 있음 | 2019 발표 (2010년대) | 원문 |
| **82~88** (v1.1) | 독일 천백여 명 1년 생활 습관 연구, 2023년 분석, 5% 이상 줄인 298명, 열 명에 네 명꼴 정상, 73% 낮음, 끝난 뒤 2년, 나중에 나눠 본 분석 | 298명 중 128명(43%) 관해(공복혈당 100 미만·2시간 혈당 140 미만·당화혈색소 5.7% 미만), 관해한 사람의 당뇨병 위험 −73% | Sandforth A, et al. "Mechanisms of weight loss-induced remission in people with prediabetes: a post-hoc analysis of the randomised, controlled, multicentre Prediabetes Lifestyle Intervention Study (PLIS)." *Lancet Diabetes Endocrinol* 2023;11(11):798-810 (PubMed 37769677). 초록: "Between March 1, 2012, and Aug 31, 2016, participants were recruited from eight clinical study centres … randomised to a control intervention, a standard lifestyle intervention, or an intensified lifestyle intervention for 12 months", "Of 1160 participants recruited to PLIS, 298 (25·7%) had weight loss of 5% or more", "128 (43%) of 298 participants were responders"; 독일당뇨병연구센터(DZD) 보도자료: "participants who had achieved remission showed a 73% reduced risk of developing T2D even two years after the end of the lifestyle intervention"; 튀빙겐대 보도자료: 관해 = 공복혈당 100 mg/dl 미만, 2시간 혈당 140 mg/dl 미만, 당화혈색소 5.7% 미만; HealthDay: "in the two years after the intervention, responders had a 73 percent lower risk … than nonresponders". 사후 분석(post hoc) | **2012-03 ~ 2016-08** 모집, 12개월 + 2년 추적 | 검색 |

### 출처 링크
- 질병관리청 「당뇨병」: https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=5305
- 질병관리청 「고혈당」: https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=5304
- 질병관리청 검진 결과 안내: https://health.kdca.go.kr/healthinfo/biz/health/ntcnInfo/healthSourc/thtimtCntnts/thtimtCntntsView.do?thtimt_cntnts_sn=7
- 일반건강검진 결과통보서 서식: https://www.law.go.kr/flDownload.do?flSeq=148392279&flNm=%5B%EB%B3%84%EC%A7%80+6%5D+%EC%9D%BC%EB%B0%98%EA%B1%B4%EA%B0%95%EA%B2%80%EC%A7%84+%EA%B2%B0%EA%B3%BC%ED%86%B5%EB%B3%B4%EC%84%9C&bylClsCd=200203
- Diabetes Fact Sheets in Korea 2024: https://www.e-dmj.org/journal/view.php?doi=10.4093/dmj.2024.0818 (정정 표 https://pmc.ncbi.nlm.nih.gov/articles/PMC12086556)
- CDC: https://www.cdc.gov/diabetes/prevention-type-2/prediabetes-prevent-type-2.html , https://www.cdc.gov/diabetes/communication-resources/prediabetes-statistics.html
- 보건복지부 브리핑(연계율): https://www.korea.kr/news/policyNewsView.do?newsId=156768891
- 건강보험심사평가원 보도자료: https://www.hira.or.kr/bbsDummy.do?brdScnBltNo=4&brdBltNo=11327&pageIndex=1&pgmid=HIRAA020041000100
- ADA Standards of Care 2026 (3장): https://pmc.ncbi.nlm.nih.gov/articles/PMC12690170
- (v1.1) 영국 NDPP 연결 연구 (PLoS Med 2023): https://doi.org/10.1371/journal.pmed.1004177 · DOAJ https://doaj.org/article/c35170997458459d87b50a82fc30ab5b · 맨체스터대 보도 https://www.manchester.ac.uk/about/news/nhs-programme-linked-to-20-reduction-in-risk-of-diabetes/ · NIHR 요약 https://evidence.nihr.ac.uk/alert/how-effective-are-referrals-to-the-nhs-diabetes-prevention-programme/
- (v1.1) NHS England 「Healthier You」 안내: https://www.england.nhs.uk/diabetes/diabetes-prevention/ · https://www.england.nhs.uk/long-read/healthier-you-nhs-diabetes-prevention-programme-gdm/ · https://healthcheck.nhs.uk/commissioners-and-providers/delivery/healthier-you-nhs-diabetes-prevention-programme/
- (v1.1) 독일 PLIS 관해 분석 (Lancet Diabetes Endocrinol 2023): https://pubmed.ncbi.nlm.nih.gov/37769677/ · https://www.thelancet.com/journals/landia/article/PIIS2213-8587(23)00235-8/abstract · DZD 보도 https://www.dzd-ev.de/en/press/press-releases/press-releases-archive/press-releases-2023/new-study-advocates-remission-as-therapeutic-goal-in-prediabetes · 튀빙겐대 보도 https://uni-tuebingen.de/en/university/news-and-publications/press-releases/archive/archivfullview-press-releases/article/new-study-advocates-remission-as-therapeutic-goal-in-prediabetes · HealthDay https://www.healthday.com/healthpro-news/conditions/physician-s-briefing-prediabetes-2665798578.html · 후속 리뷰(Diabetologia 2024) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11344004/
- DiPietro 2013: https://pmc.ncbi.nlm.nih.gov/articles/PMC3781561
- Shukla 2019: https://pmc.ncbi.nlm.nih.gov/articles/PMC7398578/

### 쓰지 않은 것 (확인 못 했거나 대상이 다름)
- **(v1.1에서 삭제) 미국 당뇨병 예방 연구(DPP, Knowler NEJM 2002 — 3,234명·2.8년·생활 습관 −58%·약 −31%)와 15년 후속 연구(DPPOS, Lancet Diabetes Endocrinol 2015 — −27%)**: 대상자 모집·추적이 1996~2001년(후속은 1996년부터)인 1900년대 자료 — 사용자 지시 2026-10-10, 건강 규칙 3-7
- 영국 NDPP: 36개월 뒤 당뇨병이 안 된 비율 87.3% vs 84.6%(기획서) — 검색 결과에서는 전환 확률 12.7% vs 15.4%만 보이고, NIHR 요약은 6.2% vs 6.4%로 다른 계산이라 섞지 않으려고 쓰지 않음. 프로그램을 끝까지 한 사람의 평균 체중 감소 3.3kg(완료자만)도 쓰지 않음
- 독일 PLIS: 위험비 0.27·95% 구간 0.08~0.90(기획서) — 검색 결과에서 숫자를 직접 확인하지 못함(73%만 확인) → 대본은 "73% 낮았습니다"와 "나중에 따로 나눠 본 분석"까지만. 같은 연구팀 Nature Medicine 2025(체중이 안 줄어도 관해하면 위험 약 71% 낮음)는 원문 미확인
- 공복혈당장애가 해마다 반복될수록 당뇨병 위험이 커진다는 국내 연구(Kim MK 외, Diabetes Res Clin Pract 2021, 251만 명, 4년 연속 '경계'면 위험비 9.77): 사연("결과지가 세 번이나 경고")과 잘 맞지만 2006~2007년부터 받은 검진 자료(추적 2016년까지)라 "2020년대 먼저, 없으면 2010년대" 기준에 못 미쳐 쓰지 않음 — 사용자가 2000년대 자료를 허락하면 문제 분석 다섯 번째 항목 후보
- 보건소 대사증후군 무료 검사·상담: 대상 나이·운영이 지역마다 달라(서울 자치구 안내만 확인) 전국 기준으로 말할 수 없음
- 한국 전단계 인지율, 공복혈당장애 판정 후 재검률 (자료 없음)
- "3~5년 안에 25%" (질병관리청 페이지에서 확인 안 됨), 2024년 진료 인원(미발표)
- Buffey 2022(앉아 있는 시간 끊기 — 식후 산책 연구가 아님, 대상 대부분 건강인), Shukla 2015 −73%(당뇨병 환자 대상)
- 당뇨병 유병률 15.5%와 14.8%(서로 다른 기준)를 섞어 쓰기
- 다른 두 건강 영상에 배정된 근거(간기능 검사 판정·영양제 관련 — supplement-liver, 근감소증·근력운동·WHO 지침·단백질 — sarcopenia)

## 지시사항 적용 메모
- 사연 7비트: ① 결과지 108 ② 마흔아홉 야근 직장인(공감 대상) ③ (손실형 변형) 작은 경고 + "술자리 줄이면 내려가겠지" 기대 ④ "조용히 올라가고 있었습니다" ⑤ 131·당뇨 진단 (0:33, 1분 안) ⑥ 6kg·앉아 있는 생활 ⑦ 한탄 2문장
- 문제 4개 / **방법 6개**, 방법마다 사연 숫자 예시 (108→116, 131, 82kg→4~6kg, 점심 뒤 15분, 비빔밥, 108→100 미만)
- v1.1 고친 범위 (공통 0번 원칙: 최소 수정): 1900년대 자료 6문장 삭제 → 영국 5문장, 식후 걷기 한계 1문장, 여섯째 8문장, 마무리 한 단어("다섯" → "여섯"). 나머지 85문장은 v1.0 그대로
- 연구마다 한계 한 문장 (건강 규칙 3-2): 영국 "실제 참여가 아니라 연결 여부만 비교"(문장 65), 식후 걷기 "10명이 하루씩 걸어 본 작은 실험"(73), 먹는 순서 "15명의 짧은 실험"(80), 독일 "나중에 따로 나눠 본 분석"(88)
- 처음 나오는 이름의 정체 (공통 0-1의 10번): 영국 "국가 예방 프로그램 … 식사와 운동, 체중 관리를 9개월 동안 돕는 무료 프로그램", 독일 "당뇨병 전단계인 천백여 명이 1년 동안 참여한 생활 습관 연구"
- 맥락 검수 (공통 0-1의 5·9·10번): 셋째 = 체중 목표 → 그 목표를 돕는 영국 프로그램 → 82kg 예시. 여섯째 = 다섯째 끝("오늘 저녁부터") 다음에 목표 바꾸기 → 독일 연구 → 108 사연자의 목표 100 미만. 연속 문장의 같은 표현("그중"·"다만"·"1년 동안") 겹침을 고침. 효과는 "~% 낮았습니다"로만 말하고 단정하지 않음
- 50자 넘는 문장 없음. 1432px 넘는 23문장은 자막 앞줄·뒷줄
- **분량: 추정 9:03 — 건강 규칙 6번 목표(10~12분)보다 약 1분 짧다.** 공통 0-1의 12번("억지로 늘리지 않는다")과 기획서 8번에 따라, 2010년대 이후 자료로 확인한 새 항목을 찾지 못해 더 늘리지 않음 (후보였던 국내 '경계' 반복 연구는 2006년부터의 자료 — 위 "쓰지 않은 것"). 녹음 뒤 실제 길이는 숫자·검사 이름 때문에 추정보다 길 수 있다(`data_insights.md` 2번)

## used_content 추가분 (v1.1 변경분)
`health/source/used_content.md`의 "1. 당뇨 전단계" 절을 아래처럼 바꾼다 (Claude가 모아서 반영).
- 머리줄: 대본 `source/prediabetes-2026-10/prediabetes-2026-10.txt` **v1.1 (문장 94 / 자막 117)**
- **연구** 줄 교체: ~~DPP 58%·31%, DPPOS 27%~~ (v1.1 삭제 — 1900년대 자료) → 영국 국가 당뇨병 예방 프로그램 연결 20% 낮음(1만 8천여 명 vs 5만여 명, PLoS Med 2023) / 독일 PLIS 5% 이상 감량 298명 중 열 명에 네 명꼴(43%) 정상 복귀, 정상 복귀한 사람 2년 동안 당뇨병 위험 73% 낮음(Lancet Diabetes Endocrinol 2023) / DiPietro 식후 15분 걷기 129→116 (10명 한계 문장) / Shukla 2019 먹는 순서 최고치 40%+
- **방법** 줄에 추가: … / 채소·단백질 먼저(비빔밥 예) / **목표를 '경계 유지'가 아니라 '정상 숫자로 돌아가기'로 (108 → 다음 검진 100 미만)**
- 새 줄 **비유·특징 있는 문장**: "목표를 '경계 유지'가 아니라 '정상 숫자로 돌아가기'로" / "다만 실제 참여가 아니라 연결 여부만 비교한 결과입니다" / "나중에 따로 나눠 본 분석이라 숫자보다 방향으로 보시면 됩니다"
- 사연·한탄·혼잣말·통계 줄은 그대로

| 구분 | 쓴 내용 (v1.1 기준 전체) |
|---|---|
| 사연 | 마흔아홉 직장인, 공복혈당 108 '공복혈당장애 의심'을 넘김 → 다음 해 조금 오름 → 3년 뒤 131 '당뇨병 의심', 당화혈색소 7.1%로 당뇨병 진단. 3년 사이 76→82kg(+6kg), 점심 뒤 하루 종일 앉아 있음 |
| 한탄 | "결과지가 세 번이나 경고를 보냈는데 저는 한 번도 듣지 않았어요" / "'경계'라는 두 글자를 괜찮다는 뜻으로 읽은 제가 원망스러워요" |
| 혼잣말 | 아직 당뇨는 아니니까 괜찮아 / 아픈 데도 없는데 뭘 / 내년 검진 때 다시 보면 되지 |
| 통계 | 전단계 열 명 중 네 명(41.1%)·약 1,410만 명 / 당뇨병 넷 중 한 명은 모름(인지율 74.7%) / CDC 10명 중 8명 모름 / 질병관리청 공복혈당장애 1년 5~8% 진행 / 당뇨 의심 후 연계율 39% / 2023 진료 383만 명 / 조절률 32% |
| 연구 | 영국 국가 당뇨병 예방 프로그램 연결 −20% (2016~2020) / 독일 PLIS 5% 감량 298명 중 43% 정상 복귀, 2년 위험 −73% (2012~2016) / DiPietro 식후 15분 걷기 129→116 / Shukla 2019 먹는 순서 최고치 40%+ |
| 방법 | 결과지 숫자 확인·작년과 비교 / 1년 기다리지 말고 상담·당화혈색소, 당뇨 의심 시 무료 진료 / 체중 5~7%(82kg → 4~6kg, 한 달 1kg) / 주 150분(30분×5일), 점심 뒤 15분 / 채소·단백질 먼저(비빔밥 예) / 목표는 '정상 숫자로 돌아가기'(108 → 100 미만) |
| 특징 있는 문장 | "증상이 없다는 건 괜찮다는 뜻이 아니라, 몸이 아직 말을 안 한다는 뜻입니다" / "목표를 '경계 유지'가 아니라 '정상 숫자로 돌아가기'로" / "나중에 따로 나눠 본 분석이라 숫자보다 방향으로 보시면 됩니다" |

## 근거 자료 은행 추가분
`health/guides/script_rules.md` 8번 표에 반영할 줄 (Claude가 모아서 반영). 확인 방법은 모두 2026-10-11 웹 검색 결과(원문 인용)로.

| 주제 | 내용 | 출처 (자료 연도) | 사용한 영상 |
|---|---|---|---|
| 전단계 관해 (PLIS) | 기존 줄의 "배정"을 사용으로 바꿈. 보탤 것: 이 분석 초록의 모집 인원은 **1,160명**(다른 PLIS 보고는 1,105명 — 대본은 "천백여 명"). 73%는 DZD 보도자료·HealthDay로 확인, 위험비 0.27·구간 0.08~0.90은 검색으로 확인 못 함(대본 미사용) | Sandforth et al., Lancet Diabetes Endocrinol 2023;11(11):798-810, PubMed 37769677 (2012~2016) | 당뇨 전단계 v1.1 (문장 82~88) |
| 국가 예방 프로그램 (영국) | 기존 줄의 "배정"을 사용으로 바꿈. 보탤 것: 프로그램 = NHS England 「Healthier You」, 2016년 시작, 식사·운동·체중 관리를 돕는 9개월 무료 지원(NHS England 안내). 87.3% vs 84.6%는 검색으로 확인 못 함(전환 12.7% vs 15.4%만 보임, NIHR 요약은 6.2% vs 6.4%로 계산이 달라 섞지 않음) | Ravindrarajah et al., PLoS Med 2023;20(2):e1004177 (2016~2020) · NHS England 안내 | 당뇨 전단계 v1.1 (문장 61~65) |
| ~~DPP~~ · ~~DPPOS~~ | 사용 불가 표시 그대로, "사용한 영상"을 "당뇨 전단계 v1.0 (v1.1에서 삭제함)"으로 | Knowler NEJM 2002 · Lancet Diabetes Endocrinol 2015 (1996~) | 당뇨 전단계 v1.0만 |
| 식후 걷기 | 기존 줄 그대로. "10명 한계 명시" = v1.1 문장 73 "다만 10명이 하루씩 걸어 본 작은 실험이라 오래 했을 때의 효과는 알 수 없습니다" | DiPietro et al., Diabetes Care 2013 (2010년대) | 당뇨 전단계 |
| 공복혈당장애 반복 (국내) | 4년 연속 검진 251만 명: 공복혈당장애 횟수가 많을수록 당뇨병 위험이 커짐(점수 0 대비 2점 위험비 3.75, 4점 9.77, 용량-반응) | Kim MK, Han K, Koh ES 외, Diabetes Res Clin Pract 2021;175:108799 — **2006~2007년부터의 검진 자료(추적 2016년까지)라 미사용**, 2000년대 자료를 쓸 수 있을 때 후보 | 미사용 |
