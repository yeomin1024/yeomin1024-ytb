# 당뇨 전단계 영상 대본 소스 (prediabetes-2026-10)

버전: v1.0 — 2026-10-10 — 최초 작성 (사용자 지시: 다른 주제 새로 골라 영상 빼고 다 만들기)

> 건강 정보 제공용 원고입니다. 의사의 진단과 치료를 대신하지 않습니다.

## 파일

| 파일 | 내용 |
|---|---|
| `prediabetes-2026-10.txt` | 대본 v1.0 — **문장 86**. 파트 라벨, `[장면] 의학적 진단이 아닙니다` (문장 23 뒤) |
| `prediabetes-2026-10.srt` | **문장 86 / 자막 103** (1432px 넘는 17문장은 앞줄·뒷줄), 문장 23 뒤 고지 공백 8.0초, 끝 8:12.7 (추정치) |
| `titles.md` | 제목 3개 (T1 채택) |
| `thumbnails/thumbnail_1.md` ~ `_3.md` | 썸네일 이미지 AI 프롬프트 3개 |
| `upload.md` | 업로드 시트 (설명란·챕터 12개·태그·고정 댓글) |

검사: `python tools/srt_tool.py check health/source/prediabetes-2026-10/prediabetes-2026-10.txt health/source/prediabetes-2026-10/prediabetes-2026-10.srt --expect 86/103`
→ `문장 86 / 자막 103 (나뉜 문장 17개) / SRT–TXT 일치 ✅ / 고지 공백 문장 23 뒤 8.0초 ✅`
녹음 후: `video/`에서 `npm run align-audio -- health prediabetes-2026-10` (오디오는 고치지 않음, 문장 23 뒤 3.5초 이상 쉼)

## 주제를 고른 이유
- 분석기 자동완성에서 "당뇨 전단계"가 관리·증상·식단·운동·수치 등 9개 모두 '전단계에서 무엇을 할까'로 이어졌다 → 사연(경계 무시) → 문제 → 방법 구조와 맞음 (`health/guides/data_insights.md`)
- 주식 채널과 같은 40~60대 시청자, 결과지 숫자로 "숫자 반전" 제목을 만들 수 있음
- 숫자 근거가 공공기관·대규모 연구로 확인됨 (아래 출처)

## 사연 검산 (재구성 — 실제 진단 기준에 맞춤)
| 시점 | 나이 | 공복혈당 | 결과지 문구 | 몸무게 | 대본 |
|---|---|---|---|---|---|
| 2023 (3년 전) | 49 | 108 | 공복혈당장애 의심 (100~125) | 76kg | 문장 1~3 |
| 2024 | 50 | 116 (예시) | 공복혈당장애 의심 | — | 문장 5 "조금 올랐을 때도", 문장 32·53 "108이 116이" |
| 2025 | 51 | 122 (예시, 대본에 숫자 없음) | 공복혈당장애 의심 | — | 문장 12 "세 번이나 경고" (2023~2025) |
| 2026 (올해) | 52 | 131 | 당뇨병 의심 (126 이상) | 82kg (+6kg) | 문장 8·10 |
| 확진 검사 | | 당화혈색소 7.1% | 당뇨병 (6.5% 이상) | | 문장 9 |

- 몸무게 목표: 82kg × 5% = 4.1kg, × 7% = 5.74kg → "4~6kg 정도" (문장 67). 한 달 1kg이면 4~6개월 → "반년 안에" (문장 69)
- 주 150분 = 30분 × 5일 (문장 71)
- "넷 중 한 명은 모름" = 100 − 인지율 74.7 = 25.3% (문장 21), "열 명 중 여섯 명은 이어지지 않음" = 100 − 39 = 61% (문장 40), "셋 중 한 명꼴" = 32.4% (문장 45)

## 숫자와 출처
| 문장 | 대본 표현 | 값 | 출처 (원문 인용) |
|---|---|---|---|
| 4, 31, 37~38, 50, 57 | 진단 기준 | 공복혈당 100~125 공복혈당장애 / 126 이상 당뇨병, 당화혈색소 5.7~6.4% 전단계 / 6.5% 이상 당뇨병 | 질병관리청 국가건강정보포털 「당뇨병」(2026-09-16): "공복 혈장 포도당 100~125 mg/dL로 정상(100 mg/dL 미만)보다 높지만 당뇨병(126 mg/dL 이상)은 아닌 경우", "당화혈색소가 5.7~6.4% 범위에 든다면 당뇨병 전단계" |
| 2, 8, 37~38 | 결과지 문구 | "공복혈당장애 의심", "당뇨병 의심" / 126 이상은 확진검사 대상 | 일반건강검진 결과통보서 [별지 제6호서식] (2025.1.1 개정), 질병관리청 안내: "당뇨병 의심: 공복혈당이 126 이상인 경우로, 확진검사 대상자가 됩니다." |
| 58 | 당뇨병 의심 시 무료 진료 | 다음 해 1월 31일까지 최초 1회 본인부담 없음 | 결과통보서: "검진받은 연도의 다음연도 1월 31일까지 최초 1회 본인부담 없이 진료" |
| 19~20 | 열 명 중 네 명, 약 1,410만 명 | 30세 이상 전단계 41.1%, 14,099,002명 (2021~2022 국민건강영양조사) | Diabetes Fact Sheets in Korea 2024, DMJ 2025;49:24-33: "approximately 14.09 million, or 41.1%" |
| 21 | 넷 중 한 명은 모름 | 당뇨병 인지율 74.7% | 같은 자료: "74.7% of adults with diabetes were aware of their condition" |
| 44~45 | 32% 정도, 셋 중 한 명꼴 | 조절률(HbA1c < 6.5%) 32.4% | 같은 자료 |
| 25, 27 | 몇 년 증상 없음, 10명 중 8명 모름 | — | CDC: "You can have prediabetes for years but have no clear symptoms." / "8 in 10 adults with prediabetes don't know they have it." (2026-02-17) |
| 34 | 5~8%가 1년 안에 | — | 질병관리청 「당뇨병」: "공복혈당장애가 있는 사람의 5~8%는 1년 안에 당뇨병으로 진행될 수 있습니다." |
| 39~40 | 39% 정도 | 당뇨병 의심 판정 후 진단·치료 연계율 | 보건복지부 제4차 국가건강검진종합계획 브리핑 (2026-06-30): "진단과 치료 연계율은 고혈압 22%, 당뇨 39% 수준" |
| 43 | 약 383만 명 | 2023년 당뇨병 환자 382만 8,682명 | 건강보험심사평가원 보도자료 2024-11-14 |
| 46 | 눈·콩팥·신경 합병증 | 망막병증, 신경병증, 신장병증 | 질병관리청 「당뇨병」: "대표적인 당뇨병 합병증은 망막병증, 신경병증, 신장병증, 동맥경화로 인한 뇌졸중, 협심증, 심근경색증 등입니다." |
| 56 | 최근 두세 달 평균 혈당 | — | 질병관리청 「당뇨병」: "당화혈색소는 최근 2~3개월의 평균 혈당을 반영합니다." |
| 60 | 5~7% 감량 목표 | 5~7%, 주 150분 이상 | ADA Standards of Care 2026 (Diabetes Care 49 Suppl 1) 권고 3.3: "a weight reduction of at least 5–7% … and ≥150 min/week of moderate-intensity physical activity" |
| 61~65 | 3,234명, 2.8년, 7%·150분, 58%, 31% | 위약 대비 발생 감소 | Knowler et al., NEJM 2002 (DPP): "The average follow-up was 2.8 years." 감소율 "58 percent", "31 percent" |
| 66 | 15년, 27% | 생활 습관 −27% | DPPOS, Lancet Diabetes Endocrinol 2015;3:866-75: "reduced diabetes incidence rates by 27%" |
| 72~73 | 60세 이상 10명, 105~125, 식후 30분 뒤 15분, 129 → 116 | 24시간 평균혈당 | DiPietro et al., Diabetes Care 2013: "129 ± 24 vs. 116 ± 13 mg dL−1" |
| 77~79 | 전단계 15명, 최고치 40% 넘게 | 탄수화물 마지막 | Shukla et al., Diabetes Obes Metab 2019;21:377 (전단계 대상) — **당뇨병 대상인 2015 연구(−73%)는 쓰지 않음** |

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
- DPP (NEJM 2002): https://pmc.ncbi.nlm.nih.gov/articles/PMC1370926
- DPPOS 15년: https://pmc.ncbi.nlm.nih.gov/articles/PMC4623946
- DiPietro 2013: https://pmc.ncbi.nlm.nih.gov/articles/PMC3781561
- Shukla 2019: https://pmc.ncbi.nlm.nih.gov/articles/PMC7398578/

### 쓰지 않은 것 (확인 못 했거나 대상이 다름)
- 한국 전단계 인지율, 공복혈당장애 판정 후 재검률 (자료 없음)
- "3~5년 안에 25%" (질병관리청 페이지에서 확인 안 됨), 2024년 진료 인원(미발표)
- Buffey 2022(앉아 있는 시간 끊기 — 식후 산책 연구가 아님), Shukla 2015 −73%(당뇨병 환자 대상)
- 당뇨병 유병률 15.5%와 14.8%(서로 다른 기준)를 섞어 쓰기

## 지시사항 적용 메모
- 사연 7비트: ① 결과지 108 ② 마흔아홉 야근 직장인(공감 대상) ③ (손실형 변형) 작은 경고 + "술자리 줄이면 내려가겠지" 기대 ④ "조용히 올라가고 있었습니다" ⑤ 131·당뇨 진단 (0:33, 1분 안) ⑥ 6kg·앉아 있는 생활 ⑦ 한탄 2문장
- 문제 4개 / 방법 5개, 방법마다 사연 숫자 예시 (108→116, 131, 82kg→4~6kg, 점심 뒤 15분, 비빔밥)
- 50자 넘는 문장 없음. 1432px 넘는 17문장은 자막 앞줄·뒷줄
