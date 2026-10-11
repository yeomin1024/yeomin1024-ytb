# 도파민 디톡스 영상 대본 소스 (dopaminedetox-2026-10)

버전: v1.0 — 2026-10-11 — 최초 작성 (사용자 지시: 주식 밖 주제 오디오 전까지 주제마다 3개)

> 자기계발 정보 제공용 원고입니다. 의사나 상담 전문가의 진단을 대신하지 않습니다.
> 사연은 실제 연구와 통계를 바탕으로 재구성한 이야기입니다 (영상 화면 캡션: "실제 연구와 통계를 바탕으로 재구성한 사연").

## 파일

| 파일 | 내용 |
|---|---|
| `dopaminedetox-2026-10.txt` | 대본 v1.0 — **문장 122**. 파트 라벨 `-사연 파트`(문장 1–22, 사연자 목소리) · `-진행자 파트` · `-문제 분석 파트` · `-올바른 방법 파트` · `-마무리`(진행자 목소리), `[장면] 정보 제공용 영상입니다` (문장 36 뒤) |
| `dopaminedetox-2026-10.srt` | **문장 122 / 자막 162** (1432px 넘는 40문장은 앞줄·뒷줄), **문장 36 뒤 고지 공백 8.0초**, **끝 11:57.4** (추정치, 약 3,400음절) |
| `titles.md` | 제목 3개 (T1 채택) |
| `thumbnails/thumbnail_1.md` ~ `_3.md` | 썸네일 이미지 AI 프롬프트 3개 (이미지는 만들지 않음) |
| `upload.md` | 업로드 시트 (설명란·챕터 13개·태그·고정 댓글·설정) |
| `summary.md` | 자동 생성 (`python3 tools/make_summary.py selfdev dopaminedetox-2026-10`) |

검사: `python3 tools/srt_tool.py check selfdev/source/dopaminedetox-2026-10/dopaminedetox-2026-10.txt selfdev/source/dopaminedetox-2026-10/dopaminedetox-2026-10.srt --expect 122/162`
→ `문장 122 / 자막 162 (나뉜 문장 40개) / SRT–TXT 일치 ✅ / 고지 공백 문장 36 뒤 8.0초 ✅ / 끝 00:11:57,377` · `✅ 이상 없음`
- 50자 넘는 문장 없음 (대본 단계에서 모두 나눔).
- 제목 숫자 "월요일 9시간"은 문장 12 (0:55.8 시작, 1분 안). "48시간"은 문장 5 (0:20)·9 (0:43).
- 녹음 후: `video/`에서 `npm run align-audio -- selfdev dopaminedetox-2026-10` (오디오는 고치지 않음, 문장 36 뒤 3.5초 이상 쉼).

## 주제를 고른 이유 (`selfdev/guides/data_insights.md` v1.0, 실행 20261011_120632)

- 카테고리 "스마트폰·도파민 중독" 기회점수 43(6위)이지만 **롱폼 성공 2/5 (40%)** — 카테고리 중 롱폼 성공 비율 최고. 성공 롱폼: EBS 컬렉션 "하루종일 유튜브 보느라 다른 일을 할 수 없는 나…"(104만 회, 채널 평소의 31.9배), 데일리어썸 "무의식적으로 보는 핸드폰이 뇌를…"(23.9만 회, 8.7배).
- 키워드 "스마트폰 중독 뇌" 46점: 검색 상위 중 주제에 맞는 영상 45%뿐 → **콘텐츠 공백 점수 1.0 (키워드 중 최고)**.
- 댓글 반응 최다 (`audience_comments.csv`): "숏폼이 없는 어린 시절이 축복"(좋아요 1,440), "스크린타임 6시간따리가 뭔 중독"(1,332 → 사연 숫자 6시간의 근거), "영화 한 편도 부담, 숏폼만 봄"(1,193), "21분짜리 영상을 끝까지 못 봄"(1,045), "앱 숨기기는 괜찮았고 흑백모드는 불편해서 그만둠"(126 → 방법 셋째의 "불편하면 밤에만").
- 유행하는 유사과학 표현("도파민 리셋")을 2020년대 연구로 바로잡을 수 있다 (`script_rules.md` 3-3, 통념 깨기 제목 롱폼 성공 3/7).
- 사연자: 30대 직장인 여성 (카테고리 1위 "나이대·직장인 고민" 70점을 사연자 설정으로 반영, `title_rules.md` 3번).

## 사연 검산 (재구성 — 숫자는 시청자 공감 범위와 날짜 계산에 맞춤)

| 항목 | 값 | 계산·기준 | 대본 |
|---|---|---|---|
| 평소 화면 시간 | 하루 평균 6시간, 숏폼 3시간 넘게 | 댓글 "스크린타임 6시간따리가 뭔 중독"(좋아요 1,332) — 시청자가 공감하는 수준. `title_rules.md` 6번 기준값(하루 5~9시간) 안 | 문장 1–2 |
| 사연자 | 서른둘, 출퇴근 왕복 두 시간 직장인 여성 | `script_rules.md` 1번(30대 직장인, 여성 사연자 목소리) | 문장 3 |
| 디톡스 | 2026-05-08(금) 22:00 → 05-10(일) 22:00 = **48시간** | 2026-01-01이 목요일 → 5월 8일은 128일째, (128−1) mod 7 = 1 → 금요일 ✅. 5월 10일 일요일, 5월 11일 월요일 | 문장 7, 9 |
| 월요일 | 2026-05-11(월) **9시간** = 평소 6시간 + **3시간** | 출퇴근 2시간 + 점심 1시간 + 일하는 틈틈이 1시간 + 퇴근 후 침대 5시간 = 9시간 | 문장 12–15 |
| 4주 반복 | 5/8·5/15·5/22·5/29(모두 금요일) 주말 | 주말(토·일) 0시간. 평일 예: 월 9시간 + 화~금 하루 6.4시간 → 평일 평균 (9 + 25.6) ÷ 5 = 6.9시간 → "**하루 7시간 가까이**", 평소 6시간보다 많음 | 문장 19–20 |
| 이 숫자의 성격 | "월요일 9시간"·"평일 7시간 가까이"는 **사연자 한 사람의 경험**으로만 쓴다 | "디톡스를 하면 반동이 온다"는 연구 결과로 말하지 않음. 문장 52에서 "누구나 이렇게 된다는 뜻은 아닙니다"로 밝힘 | 문장 52 |
| 방법 둘째 | 숏폼 3시간 → 하루 30분 = **2시간 30분** 생김 | 180분 − 30분 = 150분 | 문장 89–90 |
| 방법 셋째 | 흑백 화면 연구 평균 하루 약 20분 감소 → 6시간이 **5시간 40분 정도** | 360분 − 20분 = 340분. "연구 평균만큼이면"으로만 (사연자에게 단정하지 않음) | 문장 98 |
| 방법 첫째 | 밤 9시~아침 7시 숏폼 앱 잠금 | 사연자의 숏폼 시간(퇴근 후 침대)과 새벽 1시 취침에 맞춘 예시. 실험(모바일 인터넷 전체 차단)보다 약한 방법임을 문장 85에서 밝힘 | 문장 82–85 |
| 방법 다섯째 | 2주 뒤 6시간 → 5시간, 4시간대 | 점검 기준(연구 수치 아님) | 문장 115 |

## 숫자와 출처 (모두 2026-10-11 웹 검색 결과로 확인 — 클라우드 정책으로 논문 페이지를 직접 열 수 없어 검색 결과의 초록·보도 인용으로 확인)

| 문장 | 대본 표현 | 원문·검색 결과 인용 | 출처 (자료 연도) |
|---|---|---|---|
| 29–34 | 2026년 3월 발표 2025년 스마트폰 과의존 실태조사, 이용자의 22.7%가 과의존 위험군, 고위험군 4.1% | "전체 스마트폰 이용자 중 과의존 위험군 비율은 22.7%로 집계됐다"(전년 대비 0.2%p 감소), "스마트폰 없이는 일상이 불가능하다고 여기는 고위험군 비율도 4.1%" / KDI 정리: "스마트폰 과의존 위험군 비율은 22.7%로 전년 대비 0.2%p 감소했으나 청소년(43.0%)과 유·아동(26.0%)에서 높은 수준" | 과학기술정보통신부·한국지능정보사회진흥원 「2025년 스마트폰 과의존 실태조사」 2026-03-26 발표 — [머니투데이 2026-03-27](https://www.mt.co.kr/tech/2026/03/27/2026032710122977237), [KDI 경제교육·정보센터](https://eiec.kdi.re.kr/policy/materialView.do?num=278528) |
| 31 | 과의존 = 사용을 조절하기 어려워 생활에 문제가 생기는 상태 | "과도한 스마트폰 이용으로 스마트폰에 대한 현저성이 증가하고, 이용 조절력이 감소하여 문제적 결과를 경험하는 상태" | e-나라지표 스마트폰 과의존 지표 설명 — [index.go.kr](https://www.index.go.kr/unify/idx-info.do?idxCd=3061) |
| 38–43 | 하버드 의대 건강 블로그(2020): '도파민 단식'은 단식·도파민과 거의 관계없음. 처음 알린 심리 전문가도 글자 그대로 믿지 말라고 함. 원래는 자극에 바로 반응하는 습관을 줄이는 인지행동치료식 방법 | 블로그 첫머리(검색 결과 요약): 도파민 단식은 단식과도 도파민과도 거의 관계가 없다. 세파(Cameron Sepah)의 말: "Dopamine is just a mechanism that explains how addictions can become reinforced, and makes for a catchy title. The title's not to be taken literally." 원래 방법(검색 결과 인용): "a method, based on cognitive behavioral therapy, by which we can become less dominated by the unhealthy stimuli"(알림 등). 글쓴이 그린스푼(하버드 의대 강사, 의사): "you can't 'fast' from a naturally occurring brain chemical"(보도 인용) | Grinspoon P., "Dopamine fasting: Misunderstanding science spawns a maladaptive fad", Harvard Health Blog 2020-02-26 — [Harvard Health](https://www.health.harvard.edu/blog/dopamine-fasting-misunderstanding-science-spawns-a-maladaptive-fad-2020022618917). ※ 세파의 직함은 자료마다 psychologist/psychiatrist로 달라 대본은 "미국의 심리 전문가"로 씀 |
| 46–49 | 2022년 논문: 디지털 디톡스 연구 21개, 3,625명, 무작위 실험 12개, 효과 있음·없음·나빠짐이 섞임 | 초록: 21 studies (N = 3,625), 12 RCTs. "Some studies found positive intervention effects, whereas others found no effect or even negative consequences for well-being" | Radtke T., Apel T., Schenkel K., Keller J., von Lindern E., "Digital detox: An effective solution in the smartphone era? A systematic literature review", Mobile Media & Communication 2022;10(2):190–215 (온라인 2021) — [DOI 10.1177/20501579211028647](https://doi.org/10.1177/20501579211028647), [베를린자유대 저장소](https://refubium.fu-berlin.de/handle/fub188/38053) |
| 55–59 | 2025년 미국심리학회 학술지, 숏폼 연구 71개·9만 8천여 명, 많이 볼수록 주의력·충동 억제가 낮은 경향, 보는 시간보다 '그만두기 어려운 정도'로 잰 연구에서 관련이 더 큼, 상관관계 | "Increased SFV use was associated with poorer cognition (r = −.34), with attention (r = −.38) and inhibitory control (r = −.41)…", 71 studies, 98,299 participants. 보도: 앱 사용 시간은 인지와 약하게만 관련, "addiction-style" 척도는 "markedly stronger associations". 저자들은 인과를 밝히려면 종단·실험 연구가 더 필요하다고 함 | Nguyen L. 외, "Feeds, Feelings, and Focus: A Systematic Review and Meta-Analysis Examining the Cognitive and Mental Health Correlates of Short-Form Video Use", Psychological Bulletin 2025;151(9):1125–1146 — [PubMed 41231585](https://pubmed.ncbi.nlm.nih.gov/41231585/), [DOI 10.1037/bul0000498](https://doi.org/10.1037/bul0000498), [PsyPost 요약](https://www.psypost.org/large-meta-analysis-links-tiktok-and-instagram-reels-to-poorer-cognitive-and-mental-health/). 대본에는 상관계수 숫자를 쓰지 않음 |
| 62–64, 87–88 | 2022년 미국경제학회 학술지, 스마트폰 사용자 2천여 명 실험, 소셜미디어 사용의 31% 정도가 자기 통제 문제(추정), 참가자들이 그 어려움을 다 알아차리지 못함, 한도를 미리 정하게 하자 사용이 크게 줄었고, 잠깐의 보상 효과가 끝난 뒤에도 이어짐 | 초록: "Temporary incentives to reduce social media use have persistent effects, suggesting social media are habit forming. Allowing people to set limits on their future screen time substantially reduces use, suggesting self-control problems. … self-control problems cause 31 percent of social media use … people are inattentive to habit formation and partially unaware of self-control problems." 실험 참가자 "more than 2,000 smartphone users"(워킹페이퍼) | Allcott H., Gentzkow M., Song L., "Digital Addiction", American Economic Review 2022;112(7):2424–2463 — [AEA](https://www.aeaweb.org/articles?id=10.1257/aer.20210867), [NBER w28936](https://www.nber.org/papers/w28936). 실험 자료 2020년 |
| 67–69, 106 | 스웨덴 스톡홀름대 연구진, 새해 결심 1,066명 1년, '하겠다' 목표 58.9% vs '끊겠다' 목표 47.1%가 지켰다고 답함 | 초록: "Participants with approach-oriented goals were significantly more successful than those with avoidance-oriented goals (58.9% vs. 47.1%)." 1년 뒤 응답자의 55%가 스스로 지켰다고 답함 | Oscarsson M., Carlbring P., Andersson G., Rozental A., PLOS ONE 2020-12-09 — [DOI 10.1371/journal.pone.0234097](https://doi.org/10.1371/journal.pone.0234097), [스톡홀름대 보도](https://www.su.se/english/news/articles/2022-02-07-how-to-succeed-in-keeping-your-new-years-resolution). ※ 모집 2016년 12월, 추적 2017년 (2010년대 자료 — 1900년대 아님) |
| 74–80, 85 | 캐나다 앨버타대 연구진 2025년 실험, 18~74세 467명, 2주 모바일 인터넷 차단(전화·문자 가능), 주의력이 나이 10년 치만큼 좋아짐, 91%가 행복감·정신건강·주의력 중 하나 이상 나아짐, 사람 만나기·운동·바깥 시간 늘어남, 10일 이상 지킨 사람 네 명 중 한 명 | 467 adults aged 18–74, app blocked mobile internet but "permitted text messages and phone calls" for 2 weeks; attention improvement "comparable to … 10 years of age-related decline"; "91% of participants improved on at least one" of well-being, mental health, sustained attention; 차단 중 "spent more time socializing in person, exercising, and being in nature"; "119 (25.5% of those who committed) met the preregistered definition of 'compliant'" (14일 중 10일 이상 차단) | Castelo N., Kushlev K., Ward A. F., Esterman M., Reiner P. B., "Blocking mobile internet on smartphones improves sustained attention, mental health, and subjective well-being", PNAS Nexus 2025;4(2):pgaf017 — [DOI 10.1093/pnasnexus/pgaf017](https://doi.org/10.1093/pnasnexus/pgaf017), [NPR 보도 2025-02-24](https://www.keranews.org/2025-02-24/a-break-from-your-smartphone-can-reboot-your-mood-heres-how-long-you-need), [earth.com 요약](https://earth.com/news/taking-a-smartphone-break-can-improve-your-life-in-surprising-ways). ※ 연구에 쓴 차단 앱 이름은 대본에 쓰지 않음 (유료 앱 추천 금지) |
| 94–97 | 2023년 네덜란드의 작은 실험, 84명, 일주일 흑백 화면, 하루 화면 시간 20분 정도 감소, 통제감↑·스트레스↓, 잠금 해제 횟수 그대로, 생산성·수면의 질 변화 없음 | "Participants' smartphone use was tracked for 2 weeks (N = 84). The first week served as a baseline measure, followed by a 1-week grayscale intervention." "daily screen time was significantly reduced by 20 min, yet the daily number of phone unlocks did not change", "improved perceived control … reduced perceived overuse, online vigilance, and stress, but did not affect productivity or sleep quality" | Dekker C. A., Baumgartner S. E., "Is life brighter when your phone is not? The efficacy of a grayscale smartphone intervention addressing digital well-being", Mobile Media & Communication 2024;12(3):688–708 (온라인 2023-11-09), 암스테르담대 — [SAGE](https://journals.sagepub.com/doi/10.1177/20501579231212062), [암스테르담대 저장소](https://dare.uva.nl/id/aabe2259-4c55-4b25-968f-43fbcdf1ed8e) |

### 쓰지 않은 것 (확인 못 했거나 규칙에 맞지 않음)
- **과의존 위험군 인원 "약 1,003만 명"** (기획서 "확인 필요"): 검색에서 원문 수치를 찾지 못해 뺐다.
- **성인(만 20~59세) 위험군 22.3%**: 한 검색 요약에만 나오고 다른 검색에서 확인되지 않아 뺐다 (다른 기사의 22.4%는 2024년 조사 수치로 보임).
- 모바일 인터넷 차단 실험의 화면 시간 변화(하루 314분 → 161분, 끝난 뒤 265분): 보도 요약 하나에서만 확인되어 대본에 쓰지 않았다.
- 숏폼 메타분석의 사용 시간·중독 척도별 상관계수(−.20, −.37 등): 정확한 값을 원문으로 확인하지 못해 대본은 "관련이 더 컸다"로만 썼다.
- 미국 미시간대 베리지 교수의 "쉬어도 리셋되지 않는다" 발언: 건강 매체 인터뷰(2019년)라 연구 근거가 아니어서 쓰지 않았다.
- 소셜미디어 7일 끊기 연구(Stieger 2018, 끝난 뒤 반동은 크지 않음): 2010년대 자료이고 사연의 "월요일 9시간"을 연구로 반박·지지하지 않기 위해 쓰지 않았다. 대신 문장 52에서 사연자 한 사람의 경험이라고 밝힘.
- 수면 연구: `miraclemorning-2026-10` 배정이라 인용하지 않음. 흑백 화면 연구의 "수면의 질 변화 없음"은 그 연구의 결과라 한 마디로만 씀(문장 97).
- 습관 기간·실행 의도(언제·어디서 계획) 연구: `habit21-2026-10` 배정이라 쓰지 않음. 방법 넷째는 "할 일 하나"까지만 말하고 실행 의도 연구를 인용하지 않음.

## 기획서와 달라진 점

| 기획서 | 대본 | 이유 |
|---|---|---|
| 문제 분석 4개 (3번 = 숏폼 메타분석 + 자기 통제 실험) | **5개** — 3번 "멈추기 어려움"(숏폼 메타분석), 4번 "마음먹기만으로는 어렵다"(자기 통제 실험)로 나눔 | 진행자 혼잣말 2·3번에 하나씩 답하게 했다. 분량도 10~12분 목표에 맞음 (항목을 더해 늘림) |
| ⑤ 월요일 9시간이 출근길·점심·퇴근 후 장면 뒤에 | 반전 예고 바로 뒤(문장 12)에 9시간을 먼저 말하고 장면을 이어 붙임 | 제목 숫자가 1분 안(0:55.8)에 나오게 |
| ⑦ "한 달 평균 6시간 그대로" | "주말은 0시간이었지만, 평일은 하루 7시간 가까이로 늘어 있었죠" | 주말 이틀이 0시간이면 일주일 평균 6시간이 그대로일 수 없어서(검산 표), 평일 평균으로 바꿈 |
| 국내 통계에 위험군 인원 | 인원 뺌, 22.7%·4.1%만 | 1,003만 명 확인 못 함 |
| 모바일 인터넷 차단 실험 "준수 비율 확인 필요" | 확인됨 → "2주 중 10일 이상 지킨 사람은 네 명 중 한 명 정도"(문장 80) | 검색 결과 여러 곳에서 119명(25.5%) 확인. "지킬 수 있는 크기부터"의 근거로 씀 |
| — | 차단 중 사람 만나기·운동·바깥 시간이 늘었다는 결과 추가(문장 79) | 방법 넷째("할 일")와 이어짐 |

## 경력 시청자 예상 반론과 대본의 답 (`script_rules.md` 5번)

| 반론 | 대본 위치 |
|---|---|
| 다 끊는 게 제일 확실하지 | 문제 2(문장 45–53: 연구 결과가 엇갈림, 돌아온 평일이 그대로), 방법 다섯째(문장 108–113: 쉬는 건 괜찮다, 돌아온 다음 날 규칙이 기준) |
| 나는 중독까진 아니야 | 문장 31(과의존의 뜻은 시간보다 조절), 문장 58–60(멈출 수 있는지가 더 중요) |
| 결국 의지가 약해서 그런 거 아니야? | 문장 61–65(사용의 31%는 줄이고 싶어도 못 줄인 몫, 참가자들도 다 알아차리지 못함) |
| 상관관계일 뿐이잖아 | 문장 59에서 먼저 인정. 원인처럼 말하는 곳은 무작위 실험(차단 실험·흑백 화면·한도 설정)만 |
| 그 연구는 외국인이잖아 | 국내 통계(문장 29–34)를 먼저 보여 주고, 외국 연구는 나라·규모를 밝힘. 방법은 모두 돈이 들지 않는 휴대폰 기본 기능 |
| 흑백 모드 불편하던데 (댓글 126) | 문장 98–100: 효과가 작다고 먼저 인정, 보조 수단, 밤에만 쓰는 방법 |

## used_content 추가분

`selfdev/source/used_content.md` "영상별 사용 내용"에 옮길 내용:

### `dopaminedetox-2026-10` — 주말 48시간 휴대폰을 끊고 월요일 하루 9시간 (도파민 디톡스·숏폼)
- **사연 소재:** 서른둘, 출퇴근 왕복 두 시간 직장인 여성. 2026년 5월 하루 평균 화면 시간 6시간(숏폼 3시간 넘게), 퇴근 후 침대에서 숏폼·새벽 1시 넘어 잠. "48시간만 끊으면 뇌가 리셋된다"는 도파민 디톡스 영상 → 5월 8일(금) 밤 10시 휴대폰을 서랍에 넣고 음악·단 음식까지 끊음 → 산책 두 번·책 반 권, 일요일 밤 10시 48시간 채움, 다이어리에 '리셋 완료' → 월요일 하루 화면 시간 9시간(평소 +3시간): 밀린 알림 → 출근길 숏폼 → 점심·틈틈이·퇴근 후 침대 → 4주 반복, 주말 0시간·평일 하루 7시간 가까이
- **사연 숫자:** 6시간 / 숏폼 3시간 / 왕복 두 시간 / 새벽 1시 / 48시간 / 금요일 밤 10시~일요일 밤 10시 / 월요일 9시간(+3시간) / 4주 / 평일 7시간 가까이
- **한탄 문장:** "주말 이틀을 참은 대가로 평일을 통째로 내준 셈이에요." / "제가 리셋한 건 뇌가 아니라 한 주의 시작이었나 봐요."
- **진행자 혼잣말:** 주말에 한 번 확 끊으면 리셋되겠지 / 나는 중독까진 아니야, 심심해서 보는 거지 / 마음만 먹으면 언제든 끊을 수 있어
- **통계·연구:** 2025 스마트폰 과의존 실태조사(위험군 22.7%, 고위험군 4.1%, 과의존 정의), 하버드 의대 건강 블로그 '도파민 단식'(2020), 디지털 디톡스 문헌고찰 21개·3,625명(2022), 숏폼 메타분석 71개·9만 8천여 명(2025), 자기 통제 31%·한도 설정·보상 지속 효과(2022), 새해 결심 1,066명 '하기' 58.9% vs '끊기' 47.1%(2020), 모바일 인터넷 2주 차단 467명·주의력 10년·91%·준수 네 명 중 한 명(2025), 흑백 화면 84명·하루 20분(2023/2024)
- **문제 분석 5개:** '도파민 디톡스'는 과학 용어가 아니다 / 다 끊는 방법의 효과는 엇갈린다 / 시간보다 멈추기 어려움 / 마음먹기만으로는 줄이기 어렵다 / '끊기'만 있고 할 일이 없었다
- **올바른 방법 5개와 예시 숫자:** 2주 동안 설정으로 막기(밤 9시~아침 7시 숏폼 앱 잠금, 충전기는 거실) / 하루 한도 미리 정하기(숏폼 30분 → 하루 2시간 30분 생김, 1시간에서 시작해 2주마다 줄이기, 전날 정하기) / 흑백 화면은 보조(6시간 → 5시간 40분 정도, 밤에만) / 안 보기 대신 할 일(퇴근 지하철 책 10쪽, 자기 전 20분 스트레칭, 주말 산책·책을 평일로) / 쉬는 날은 돌아온 다음 날 규칙 먼저(출근길 알림 10분, 숏폼 퇴근 후 30분, 일요일 밤 다이어리에 '리셋 완료' 대신 규칙, 2주 뒤 6시간 → 5시간·4시간대 점검)
- **비유·특징 있는 문장:** "뇌가 리셋된 게 아니라, 휴대폰이 이틀 동안 서랍에 있었을 뿐입니다." / "끊었던 이틀이 지나자, 그대로인 평일이 기다리고 있었던 겁니다." / "중독인지 아닌지보다, 멈추고 싶을 때 멈출 수 있는지가 더 중요합니다." / "이 규칙을 일요일 밤 다이어리에 '리셋 완료' 대신 적어 두세요."
- **제목 숫자:** 48시간 → 월요일 9시간

## 근거 자료 은행 추가분

`selfdev/guides/script_rules.md` 8번 표: 기존 배정 줄 8개의 "배정" → **"사용한 영상: dopaminedetox-2026-10"** 으로 바꾸고, 아래 내용으로 갱신·추가한다.

| 주제 | 내용 | 출처 (자료 연도) | 사용한 영상 |
|---|---|---|---|
| 도파민 단식이라는 말 | 하버드 의대 건강 블로그: '도파민 단식'은 단식과도 도파민과도 거의 관계가 없다. 널리 알린 세파도 "글자 그대로 받아들이지 말라", 원래는 인지행동치료식으로 알림 같은 자극에 덜 휘둘리게 하는 방법 (세파 직함은 자료마다 psychologist/psychiatrist) | Grinspoon, Harvard Health Blog 2020-02-26 — [Harvard Health](https://www.health.harvard.edu/blog/dopamine-fasting-misunderstanding-science-spawns-a-maladaptive-fad-2020022618917) | dopaminedetox-2026-10 |
| 디지털 디톡스 연구 | 연구 21개(3,625명, 무작위 실험 12개) 체계적 문헌고찰: 효과 있음·없음·오히려 나빠짐이 섞여 있다 | Radtke 외, Mobile Media & Communication 2022;10(2):190–215 (온라인 2021) — [DOI](https://doi.org/10.1177/20501579211028647) | dopaminedetox-2026-10 |
| 숏폼과 주의력 | 연구 71개(98,299명) 메타분석: 숏폼을 많이 볼수록 인지 기능이 낮았고(r −0.34), 주의력(−0.38)·충동 억제(−0.41). 사용 시간보다 중독 척도로 잰 연구에서 관련이 더 큼(보도 기준, 계수 미확인). 상관관계 | Nguyen 외, Psychological Bulletin 2025;151(9):1125–1146 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/41231585/) | dopaminedetox-2026-10 |
| 의지의 한계와 한도 설정 | 스마트폰 사용자 2천여 명 무작위 실험(2020년 자료): 소셜미디어 사용의 31%가 자기 통제 문제(모형 추정), 사람들은 이를 일부만 알아차림. 앞으로의 사용 한도를 정하게 하자 사용이 크게 줄었고, 잠깐의 보상 효과가 끝난 뒤에도 이어짐 | Allcott·Gentzkow·Song, American Economic Review 2022;112(7):2424–2463 — [AEA](https://www.aeaweb.org/articles?id=10.1257/aer.20210867) | dopaminedetox-2026-10 |
| 설정으로 막기 | 467명(18~74세) 무작위 실험: 2주 모바일 인터넷 차단(통화·문자 가능) → 주의력이 나이 10년 차이만큼 좋아짐, 91%가 행복감·정신건강·주의력 중 하나 이상 나아짐, 사람 만나기·운동·바깥 시간 늘어남. **준수: 14일 중 10일 이상 차단을 지킨 사람 119명(25.5%)** — 확인됨 (2026-10-11 검색 결과 여러 곳) | Castelo 외(앨버타대 등), PNAS Nexus 2025;4(2):pgaf017 — [DOI](https://doi.org/10.1093/pnasnexus/pgaf017), [NPR](https://www.keranews.org/2025-02-24/a-break-from-your-smartphone-can-reboot-your-mood-heres-how-long-you-need) | dopaminedetox-2026-10 |
| 흑백 화면 | 84명, 1주 평소대로 → 1주 흑백: 하루 화면 시간 약 20분 감소, 잠금 해제 횟수 그대로, 통제감↑·스트레스↓, 생산성·수면 효과 없음 | Dekker·Baumgartner(암스테르담대), Mobile Media & Communication 2024;12(3):688–708 (온라인 2023-11-09) — [SAGE](https://journals.sagepub.com/doi/10.1177/20501579231212062) | dopaminedetox-2026-10 |
| '끊기'보다 '하기' 목표 | 새해 결심 1,066명 1년 추적 실험(스톡홀름대 등): 1년 뒤 55%가 지켰다고 답함. 접근 목표 58.9% vs 회피 목표 47.1% | Oscarsson 외, PLOS ONE 2020 (2016-12 모집, 2017 추적) — [DOI](https://doi.org/10.1371/journal.pone.0234097) | dopaminedetox-2026-10 |
| 국내 스마트폰 과의존 | 2025 스마트폰 과의존 실태조사: 과의존 위험군 22.7%(전년 22.9%, −0.2%p), 고위험군 4.1%, 청소년 43.0%, 유·아동 26.0%. 과의존 정의(현저성↑·조절력↓·문제적 결과). **위험군 인원 1,003만 명·성인 22.3%는 확인 못 함 — 쓰지 않음** | 과학기술정보통신부·한국지능정보사회진흥원 2026-03-26 발표 — [머니투데이](https://www.mt.co.kr/tech/2026/03/27/2026032710122977237), [KDI](https://eiec.kdi.re.kr/policy/materialView.do?num=278528), 정의 [e-나라지표](https://www.index.go.kr/unify/idx-info.do?idxCd=3061) | dopaminedetox-2026-10 |
| 미사용 후보 (추가) | 모바일 인터넷 차단 실험의 화면 시간: 준수 그룹 하루 314분 → 161분, 차단이 끝난 뒤 265분 (보도 요약 하나에서만 확인 — 쓰려면 원문 확인) | earth.com·The Debrief 요약 (2025) | 미사용 |
