# 21일 습관·작심삼일 영상 대본 소스 (habit21-2026-10)

버전: v1.0 — 2026-10-11 — 최초 작성 (사용자 지시: 주식 밖 주제 오디오 전까지 주제마다 3개)

> 자기계발 정보 제공용 원고입니다. 의사나 상담 전문가의 진단을 대신하지 않습니다. 사연은 실제 연구와 통계를 바탕으로 재구성한 이야기입니다.

## 파일

| 파일 | 내용 |
|---|---|
| `habit21-2026-10.txt` | 대본 v1.0 — **문장 105**. 파트 라벨(`-사연 파트` `-진행자 파트` `-문제 분석 파트` `-올바른 방법 파트` `-마무리`), `[장면] 정보 제공용 영상입니다` (문장 28 뒤). 50자 넘는 문장 없음 |
| `habit21-2026-10.srt` | **문장 105 / 자막 138** (46px 폭 1432px을 넘는 33문장은 앞줄·뒷줄), **문장 28 뒤 고지 공백 8.0초**, 끝 **10:37.1** (추정치, 3,019음절) |
| `titles.md` | 제목 3개 (T1 채택) |
| `thumbnails/thumbnail_1.md` ~ `_3.md` | 썸네일 이미지 AI 프롬프트 3개 (숫자 반전 / 인물·감정 / 대비) |
| `upload.md` | 업로드 시트 (설명란·챕터 14개·태그 15개·고정 댓글) |
| `summary.md` | 한눈에 보기 (자동 생성 — `python3 tools/make_summary.py selfdev habit21-2026-10`) |

검사: `python3 tools/srt_tool.py check selfdev/source/habit21-2026-10/habit21-2026-10.txt selfdev/source/habit21-2026-10/habit21-2026-10.srt --expect 105/138`
→ `문장 105 / 자막 138 (나뉜 문장 33개) / SRT–TXT 일치 ✅ / 고지 공백 문장 28 뒤 8.0초 ✅ / 끝 00:10:37,127` · `✅ 이상 없음`

- 분량: 3,019음절로 목표(3,100~3,700음절)보다 조금 적지만, 쉼표 쉼·고지 공백을 넣은 추정 길이는 10분 37초로 목표 10~12분 안이다 (`script_rules.md` 6-1).
- 녹음 후: `video/`에서 `npm run align-audio -- selfdev habit21-2026-10` (오디오는 고치지 않음, 문장 28 뒤 3.5초 이상 쉼).
- 내레이션 역할: 사연자(Sohee) 문장 1–16 · 진행자 문장 17–105.

## 주제를 고른 이유 (`selfdev/guides/data_insights.md`, `title_rules.md` 3-1)

- 카테고리 "미루기·작심삼일·습관" 기회점수 **55 (3위)**, 키워드 "미루는 습관 극복" **71 (2위)**.
- 이 소재의 롱폼 성공 2개가 작은 채널에서 나왔다: "부자들이 실천하는 '2분 법칙'…"(구독자 1.25만, 39.6만 회, **246배**), "아무리 미루던 사람도 오늘부터 달라집니다…"(1.96만, 11.9만 회, **190배**).
- 댓글: "미루" 39건·"습관" 40건, "매일 같은 시간에 반복하면 66일 후 자동화"(좋아요 120) → 시청자가 이미 아는 21일·66일을 **연구로 확인된 범위**로 바로잡는 수요.
- 통념 깨기 제목 롱폼 성공 3/7 (43%) vs 7/30 (23%) → 문제 01에서 "21일"을 바로잡는다 (`script_rules.md` 6-2).
- 근거: 2021~2024 대규모 연구(습관 기간 문헌고찰 2024, 헬스장 출입 기록 2023, 4주 프로그램 54가지 2021, 연속 기록 실험 2023, 실행 의도 642개 실험 2024).

## 사연 검산 (재구성 — 날짜·일수 계산)

사연 인물은 가상이다 (서른여섯, 사무실 직장인 여성 — 사연자 목소리 Sohee와 같음). 영상 화면 캡션: "실제 연구와 통계를 바탕으로 재구성한 사연". 몸 수치(체중 등)는 쓰지 않았다 (`script_rules.md` 1번).

| 항목 | 값 | 계산·기준 | 대본 |
|---|---|---|---|
| 1차 챌린지 | 2026-01-01(목) ~ 01-21(수) = **21일** | 매일 아침 7시 30분, 21일 연속 | 문장 1·5·6 |
| 22일째 | 01-22(목) 알람을 끔 → 01-23(금) 야근 → 01-24(토) 늦잠 | 사흘 연속 빠짐 → 연속 기록 **0일** | 문장 8~11 |
| 2차·3차 | 04-01(수) ~ 04-21(화), 07-01(수) ~ 07-21(화) = 21일씩 | 같은 패턴으로 무너짐 | 문장 13 |
| 합계 | 21 × 3 = **63일** (동그라미 63개) | (대본에 없음) 30분 × 63일 = 1,890분 = 31시간 30분 | 문장 15 |
| 연구 중간값과 비교 | 21 ÷ 59 = 35.6%, 21 ÷ 66 = 31.8% | "그 중간값의 3분의 1 남짓" | 문장 39 |
| 헬스장 기준과 비교 | 21 ÷ 68 = 30.9%, 21 ÷ 78 = 26.9% | "이 기준의 3분의 1도 안 되는" | 문장 46 |
| 방법 1 석 달 | 01-01 ~ 03-31 = 31 + 28 + 31 = **90일** (2026년 2월은 28일) | 90 − 78 = 12일, 90 − 68 = 22일 → "열흘 넘게 여유" | 문장 67·68 |
| 21일 뒤 계획 | 21 + 69 = 90 | "그다음 69일의 계획" | 문장 99 |
| 1월 한 날 수 | 1월 31일 중 1~21일 = 21일 | "31일 중 21일 운동한 달" | 문장 95 |
| 9센트 | 1달러 1,300~1,500원이면 117~135원 | "우리 돈 백 원 남짓" | 문장 90 |
| 연구 범위 안인지 | 21일은 습관 형성 범위 4~335일 안 → 21일 만에 되는 사람도 있을 수 있다(문장 35)고 인정, 다만 중간값보다 한참 짧음 | | 문장 34·35 |

## 숫자와 출처 (모두 2026-10-11 WebSearch 결과로 확인)

> 클라우드 정책으로 논문 페이지(pnas.org, pmc.ncbi.nlm.nih.gov 등)를 WebFetch로 직접 열 수 없었다 (`getaddrinfo ENOTFOUND`). 아래 "원문 인용"은 **검색 결과에 인용된 초록·정정문·보도자료 문장**이다.

| 문장 | 대본 표현 | 값 | 출처 (원문 인용) | 자료 연도 |
|---|---|---|---|---|
| 22~26 | 미국 헬스장 체인 회원 6만 1천여 명, 4주짜리 프로그램 54가지 무작위, 절반 가까이가 방문 9~27% 증가, 끝난 뒤 효과가 남은 것 8% | 61,293명, 54개, 45%, 9~27%, 8% | Milkman 외, Nature 600:478–483 (2021-12): "a megastudy with 61,293 members of an American fitness chain … 54 four-week digital programmes", "45% of these interventions significantly increased weekly gym visits by 9% to 27%", "only 8% of interventions induced behaviour change that was significant and measurable after the four-week intervention" | 2021 |
| 89~91 | 1위는 빠진 뒤 돌아오게 하는 방법, 9센트 포인트, 4주 동안 방문 27% 증가 | 125포인트(약 $0.09), 27% | 같은 논문 초록: "the top-performing intervention offered microrewards for returning to the gym after a missed workout". 펜실베이니아대 보도(Penn Today, 2021-12): 빠진 뒤 돌아오면 "125 bonus points (about $0.09)", 그 프로그램이 "a 27% boost in gym visits" | 2021 |
| 30~38 | 2024년 호주 연구진, 연구 20개·2,601명, 중간값 59~66일, 평균 106~154일, 4~335일, 기간을 보고한 연구 4개 | 같음 | Singh·Murphy·Maher·Smith, Healthcare 12(23):2488 (2024-12, 남호주대): "20 studies involving 2601 participants", "Four studies reported the median or mean times to reach habit formation, ranging from 59-66 days (median) and 106-154 days (means), with substantial individual variability (4-335 days)", "Most studies had a high risk of bias rating (n = 11)" | 2024 |
| 36 | 흔히 말하는 66일도 중간값 | 66일 = 중간값 | Lally 외 2010 (아래)에서 나온 66일은 곡선이 잘 맞은 39명의 중간값 (검색 결과: "the famous 66-day figure comes from the 39 participants with good curve fits") — 대본에는 "여러 사람의 중간값"으로만 | 2010 |
| 41~44 | 2023년 한 연구, 4년 치 헬스장 출입 기록, 3만 110명, 손 씻기 기록도 인공지능 기법, 손 씻기는 몇 주, 헬스장은 68~78일·두세 달 | **정정 후 숫자** | Buyalskaya·Ho·Milkman·Li·Duckworth·Camerer, PNAS 120(17):e2216115120 (2023-04-17): "it typically takes months to form the habit of going to the gym but weeks to develop the habit of handwashing in the hospital", 헬스장 N = 30,110명·"over 4 y of gym attendance", 기계학습(Predicting Context Sensitivity). **정정 PNAS 120(34):e2312763120 (2023-08-17):** 본문의 "122 to 226 days, or about 4 to 7 months"는 "68 to 78 days, or about 2 to 3 months"로 바로잡음, Fig. 2·SI Table S8도 정정 (그림 설명: "68 (Left) and 77 (Right) d", 정정 전 121·187일) | 2023 |
| 45 | 연구진은 마법의 숫자 같은 건 없다고 정리 | — | 칼텍 보도자료 제목 "No magic number for time it takes to form habits" (EurekAlert 2023-04-17) | 2023 |
| 48·49·79 | 2010년 영국 연구진, 96명, 12주, 한 번 빠진 건 큰 영향 없음, 꾸준히 한 사람일수록 습관이 자리 잡는 모습이 뚜렷 | 같음 | Lally·van Jaarsveld·Potts·Wardle, European Journal of Social Psychology 40:998–1009 (2010, 유니버시티칼리지런던): "96 volunteers … daily … for 12 weeks", "Missing one opportunity to perform the behaviour did not materially affect the habit formation process", "Performing the behaviour more consistently was associated with better model fit" — 2010년대 자료 (같은 내용의 2020년대 연구를 찾지 못함) | 2010 |
| 51~54·97 | 2023년 소비자 심리 연구, 실험 일곱 개, 이어진 기록 표시 → 더 이어 감 / 끊긴 기록 표시 → 덜 이어 감, 자기 탓이면 차이가 커짐, 끊긴 기록을 메울 수 있으면 영향이 줄어듦 | 실험 7개 | Silverman·Barasch, "On or Off Track: How (Broken) Streaks Affect Consumer Decisions", Journal of Consumer Research 49(6):1095–1117 (2023-04): "In seven studies, we find that intact (vs. broken) streaks highlighted via behavioral logs increase consumers' subsequent engagement in that behavior", "amplified when consumers attribute a break in the streak to themselves rather than to external factors, and attenuated when consumers can 'repair' a broken streak" | 2023 |
| 60~63·84·85 | 2024년 미국과 독일 연구진, 실행 의도 실험 642개, 생각·감정·행동에 효과, 조건(만약)을 붙인 계획·되뇐 계획에서 효과가 더 큼 | d 0.27~0.66 (대본에는 숫자 없음) | Sheeran·Listrom·Gollwitzer, European Review of Social Psychology 36(1) (2025, 온라인 2024): "Across 642 independent tests, forming implementation intentions proved effective for cognitive, affective, and behavioural outcomes (.27 ≤ d ≤ .66)", "Effect sizes were larger when plans had a contingent (if-then) format, participants were highly motivated to pursue the goal, and plans were rehearsed" (노스캐롤라이나대·뉴욕대·콘스탄츠대) | 2024 |
| 72 | 습관 연구들은 며칠을 했는지보다 생각하지 않아도 하게 되는지를 물어서 습관을 잰다 | — | Singh 외 2024: 포함 연구는 "habit or automaticity questionnaires such as the SRHI or SRBAI"를 썼다. Lally 외 2010: 참여자가 "completed the self-report habit index (SRHI) each day". 문장 73·74의 질문 두 개는 이해를 돕는 예시(설문 문항 그대로가 아님) | 2024·2010 |

### 출처 링크
- Singh 외 2024 (Healthcare): https://doi.org/10.3390/healthcare12232488 · https://digital.library.adelaide.edu.au/items/fe6ba93e-1d6b-42b8-9ee7-a231a64ff006
- Buyalskaya 외 2023 (PNAS): https://doi.org/10.1073/pnas.2216115120
- 위 논문 정정 (PNAS 2023-08-17): https://doi.org/10.1073/pnas.2312763120 · https://pubmed.ncbi.nlm.nih.gov/37590420/
- 칼텍 보도자료 "No magic number…" (2023-04-17): https://www.eurekalert.org/news-releases/986381
- Milkman 외 2021 (Nature): https://doi.org/10.1038/s41586-021-04128-4 · https://www.hks.harvard.edu/publications/megastudies-improve-impact-applied-behavioural-science · https://www.scimex.org/newsfeed/which-programs-give-gym-goers-the-biggest-boost
- 9센트 보너스·27% (Penn Today): https://penntoday.upenn.edu/news/wharton-study-best-ways-boost-workout-habits
- Lally 외 2010: https://doi.org/10.1002/ejsp.674
- Silverman·Barasch 2023 (JCR): https://doi.org/10.1093/jcr/ucac029 · https://www.insead.edu/faculty-research/publications/journal-articles/or-track-how-broken-streaks-affect-consumer
- Sheeran·Listrom·Gollwitzer 2025 (온라인 2024): https://doi.org/10.1080/10463283.2024.2334563

### 쓰지 않은 것 (확인 못 했거나 규칙에 맞지 않음)
- **헬스장 습관 "4~7달·6달"** (Buyalskaya 2023 처음 발표·보도 숫자) — 2023-08 정정으로 68~78일이 됐다. 대본·설명란에는 정정 후 숫자만 쓴다.
- **병원 직원 3,124명** (기획서) — 논문의 3,124가 손 씻기 인원인지 검색 결과로 확인하지 못해 인원 수 없이 "병원 직원들"로만 썼다.
- **연속 기록 연구의 66% vs 58%** (Psychology Today 요약) — 원문 확인을 못 해서 숫자 없이 방향만 썼다.
- **Singh 2024의 요인(아침 시간·즐거움·스스로 고른 습관)** — 보도 요약에만 있고 초록 원문을 확인하지 못했다.
- **Lally 2010 "아주 들쭉날쭉한 사람은 습관이 되지 않았다"** (기획서 표현) — 초록 원문은 "더 꾸준히 할수록 모델 적합도가 좋았다"라서 문장 79를 그 범위로 썼다.
- **"21일"의 출처로 알려진 1960년 책** — 1900년대 자료라 소개하지 않았다 (`script_rules.md` 3-2).
- **"두 번 연속 빠지지 않기"를 책 이름과 함께** — 책에서 나온 요령이라 연구 결과처럼 말하지 않았다. 근거로는 헬스장 실험(빠진 뒤 돌아오면 보상)만 썼다 (`script_rules.md` 3-3).
- 미루기와 건강(Johansson 외, JAMA Network Open 2023) — 이 대본은 미루기보다 습관 기간·복귀가 주제라 쓰지 않았다 (미사용 후보로 남김).
- 다른 두 영상 배정 근거(수면 연구 — miraclemorning, '하기' 목표·스마트폰 연구 — dopaminedetox)는 쓰지 않았다.

## 기획서와 달라진 점

| 기획서 | 대본 | 이유 |
|---|---|---|
| 방법 5개 | **방법 6개** — 둘째 "날짜 대신 저절로 되는지로 확인" 추가 | 석 달 뒤에 무엇을 보는지 답하고, 분량(10분 이상)을 문장이 아니라 항목으로 채움 (공통 0-1의 12번) |
| "연속 기록이 끊기면 그만두기 쉽다"(2023) 확인 못 함 | **Silverman·Barasch, JCR 2023 확인 후 사용** (문제 03, 방법 여섯째) | 검색으로 초록 확인. 사연의 "0일이 된 달력 앞에서 멈춤"과 바로 이어짐 |
| 문제 04 "사연자의 계획은 '21일 동안 매일 30분'뿐" | "잘 풀리는 날에만 맞춘 계획" — 시간·장소(아침 7시·거실)는 있었고 **바쁜 날의 '만약' 계획**이 없었음 | 사연자가 이미 시간·장소를 정해 두었기 때문. 메타분석의 "조건(if-then) 형식에서 효과가 더 큼"과 맞춤 |
| 방법 4 근거 "작은 보상만으로 27%" 식 표현 가능성 | "이 작은 보상을 넣은 프로그램은 … 27% 늘렸다" | 27%는 기본 프로그램 + 보상 전체의 효과라서 |
| 썸네일 3 "남은 습관 0개" | "사흘 뒤 0일" | "63개·남은 습관 0개"는 문장 15(1:17)로 1분 밖 (`thumbnail_guide.md` 1-5) |
| T2 "22일째 딱 하루 쉬었을 뿐인데 … 63일이 0이 됐습니다" | "22일째 하루쯤 괜찮다며 알람을 껐더니 21일 기록이 0일이 됐습니다" | 63일은 1분 밖, 59자로 길이 맞춤 |
| 태그 "미루는 습관·미루는 습관 극복" | 빼고 "21일 챌린지·홈트 습관·습관 연구" | 영상이 미루기를 직접 다루지 않음 (`upload_guide.md` 4번: 영상에 없는 태그 금지) |

## 경력 시청자 예상 반론과 대본의 답 (`script_rules.md` 5번)

| 반론 | 대본 위치 |
|---|---|
| 66일이면 습관 된다던데? | 문장 36: 66일도 중간값일 뿐, 누구에게나 맞는 숫자가 아님 |
| 나는 21일 만에 됐는데? | 문장 34·35: 4일 만에 된 사람도 있지만 그게 내 기준이 될 수는 없음 |
| 결국 의지가 약해서 그런 거 아니야? | 문제 04(문장 57~64): 의지보다 '만약' 계획의 형식이 연구로 효과가 확인됨 / 문장 54: 자기 탓을 할수록 끊긴 기록의 영향이 커짐 |
| 그 연구는 외국인(헬스장 회원)이잖아 | 문장 37: 기간을 보고한 연구가 4개뿐이라 숫자를 외울 필요 없다고 한계를 먼저 밝힘. 방법은 모두 돈·시간이 들지 않는 것 |
| 하루 빠져도 괜찮다며? | 문장 49: 한 번 빠진 건 괜찮음 → 방법 다섯째: 대신 두 번 연속은 빠지지 않기 |
| 21일 챌린지는 쓸모없다는 거냐? | 문장 98~100: 챌린지 자체는 나쁘지 않고, 그다음 69일 계획·최소 버전·만약 계획을 정하면 좋은 출발 |

## 지시사항 적용 메모
- 사연 7비트: ① 2026-01-01 달력 21칸·21일 영상 ② 서른여섯 사무실 직장인, 늘 작심삼일 ③ 21일 연속·동그라미 21개·계단 숨 덜 참 ④ "진짜 시험은 22일째부터" ⑤ 알람 끔 → 야근 → 늦잠, **사흘 만에 0일 (0:54, 1분 안)** ⑥ 4월·7월에도 같은 패턴, 21일 뒤 계획 없음 ⑦ 한탄 2문장(동그라미 63개, 결승선 착각)
- 진행자 혼잣말 3개 → 문제 01·02(21일이면 저절로), 03(하루 빠졌으니 망했어), 04(다음 달 1일부터)로 각각 답함
- 문제 4개 / 방법 6개, 방법마다 사연 숫자 예시(1월 1일~3월 31일 90일, 30분 → 5분, 아침 7시 양치 후 스쿼트 20개, 22·23일째, 1월 31일 중 21일, 한 달 20일). "해도 되는 때"는 문장 98~100
- 연구 종류 (`script_rules.md` 3-4): 무작위 실험(Milkman 2021, Silverman 2023)은 "~하게 했더니", 관찰·추적 자료(Lally 2010 — 참여자가 행동을 스스로 고름, Buyalskaya 2023 — 출입·손 씻기 기록)는 "~했습니다"로만 쓰고 원인처럼 말하지 않았다. 문헌고찰·메타분석(Singh 2024, Sheeran 2024)은 한계(기간 보고 연구 4개)를 문장 37에 밝혔다
- 영문 약어·학술지 이름은 대본에서 쓰지 않았다 (TTS). 연구자 이름 없이 "2024년 호주 연구진"처럼

---

## used_content 추가분

### 1. 21일 습관·작심삼일 — `habit21-2026-10` (v1.0)
원본: `selfdev/source/habit21-2026-10/habit21-2026-10.txt`, `.srt` (문장 105 / 자막 138)
제목: 21일만 버티면 습관이 된다길래 꼬박 채웠는데 사흘 만에 0일이 됐습니다. 작심삼일 반복하는 사람들의 공통점

| 구분 | 쓴 내용 |
|---|---|
| 사연 소재·사건 | 서른여섯 사무실 직장인 여성, 2026-01-01 "21일만 버티면 습관" 영상을 보고 21일 홈트 챌린지(매일 아침 7시 거실 매트 30분) → 21일 연속·동그라미 21개 → 1/22 "하루쯤" 알람 끔 → 야근 → 늦잠 → 사흘 만에 연속 기록 0일 → 4월·7월에도 반복 |
| 사연 숫자 | 21일 → 0일 / 22일째 / 사흘 / 세 번 = 동그라미 63개 → 남은 습관 0개 |
| 사연 문장 | "저는 거실 달력에 21칸을 그렸어요" / "21일이면 끝난다니 이번엔 될 것 같았어요" / "회사 계단을 올라도 숨이 덜 찼고" / "그런데 진짜 시험은 22일째부터였습니다" / "다시 1일부터 세야 한다는 생각에 매트는 그대로 말려 있었어요" / 한탄: "동그라미를 63개나 그렸는데, 제 몸에 남은 습관은 하나도 없어요", "21일을 결승선으로 착각한 바람에 세 번이나 출발선으로 돌아온 셈이에요" |
| 진행자 연결 | "새해나 월초가 되면 많은 분들이 이런 생각을 하죠" / "정해진 기간 안에서는 잘 되다가, 기간이 끝나면 대부분 원래대로" / "사연 속 21일 챌린지가 남의 이야기가 아닌 이유입니다" |
| 혼잣말 | 21일만 버티면 그다음엔 저절로 되겠지 / 하루 빠졌으니 이번에도 망했어 / 이번 달은 바쁘니까 다음 달 1일부터 다시 하자 |
| 연구·통계 | Milkman 2021 헬스장 회원 6만 1천여 명·4주 프로그램 54가지(45%가 9~27% 증가, 끝난 뒤 효과 8%, 1위 = 빠진 뒤 돌아오면 9센트 보너스, 27%) / Singh 2024 연구 20개·2,601명(중간값 59~66일, 평균 106~154일, 4~335일, 기간 보고 연구 4개) / Buyalskaya 2023 + 정정(헬스장 3만 110명 4년 치, 68~78일·두세 달, 손 씻기 몇 주, "마법의 숫자는 없다") / Lally 2010 96명 12주(한 번 빠진 건 큰 영향 없음, 꾸준할수록 뚜렷) / Silverman·Barasch 2023 연속 기록 실험 7개(끊긴 기록 표시 → 덜 이어 감, 자기 탓이면 커짐, 메울 수 있으면 줄어듦) / Sheeran 2024 실행 의도 642개(조건 붙인 계획·되뇐 계획에서 효과 큼) |
| 계산·개념 | 중간값 설명("줄 세웠을 때 한가운데 사람의 값") / 21일 = 중간값의 3분의 1 남짓, 헬스장 기준의 3분의 1도 안 됨 / 66일도 중간값일 뿐 / 실행 의도 = 언제·어디서·어떻게 / "빠진 날보다 빠진 다음 날이 승부처" |
| 올바른 방법 | 목표 석 달(1/1~3/31 = 90일, 68~78일보다 열흘 넘게 여유, 석 달째는 점검하는 날) / 날짜 대신 저절로 되는지 확인(매트를 펼지 고민하지 않는지, 알람 전에 몸이 먼저 가는지) / 바쁜 날 최소 버전(30분 → 매트 위 5분 스트레칭, "웃음이 날 만큼 작게") / 언제·어디서 한 문장 + 만약 계획(아침 7시 양치 후 스쿼트 20개, 야근하면 자기 전 5분, 냉장고·매트 옆에 붙이고 소리 내어 읽기) / 두 번 연속 빠지지 않기 + 돌아온 날 작은 보상(좋아하는 차 한 잔) / 연속 일수 대신 이번 달 한 날 수(1월 31일 중 21일, 한 달 20일 이상) / 해도 되는 때: 21일을 첫 단계로, 그다음 69일 계획 |
| 비유·특징 문장 | "21일은 결승선이 아니라 출발선" / "졸업 날이 아니라 점검하는 날" |
| 마무리 당부 | "오늘 달력에 바쁜 날의 5분 계획부터 적어 보세요" |

비슷한 유형이라 다음에 피할 것: 사연자가 30대 여성 직장인(세 영상 공통), 달력 동그라미·운동 매트 소품, "결승선/출발선" 비유.

## 근거 자료 은행 추가분 (`selfdev/guides/script_rules.md` 8번 — "배정" → "사용한 영상"으로)

| 주제 | 내용 | 출처 (자료 연도) | 사용한 영상 |
|---|---|---|---|
| 습관이 되는 기간 | 연구 20개(2,601명) 체계적 문헌고찰: 기간을 보고한 4개 연구에서 중간값 59~66일, 평균 106~154일, 사람에 따라 4~335일. 포함 연구 11개가 비뚤림 위험 높음 | Singh 외, Healthcare 2024;12(23):2488 — [DOI](https://doi.org/10.3390/healthcare12232488) | habit21-2026-10 |
| 운동·손 씻기 습관 | 헬스장 이용자 30,110명(4년 출입 기록)·병원 손 씻기 기록 기계학습 분석: 손 씻기는 몇 주, 헬스장 출석은 **68~78일(약 2~3달)**. 보도자료 "No magic number". ※ 2023-08-17 정정: 본문 "122~226일(약 4~7달)" → "68~78일(약 2~3달)", Fig. 2·SI Table S8 정정. **기획서의 "병원 직원 3,124명"은 확인 못 함 — 인원 없이 쓴다** | Buyalskaya 외, PNAS 2023;120(17):e2216115120 + 정정 120(34):e2312763120 — [논문](https://doi.org/10.1073/pnas.2216115120), [정정](https://doi.org/10.1073/pnas.2312763120), [보도자료](https://www.eurekalert.org/news-releases/986381) | habit21-2026-10 |
| 하루 빠져도 | 96명 12주: 한 번 빠진 것은 습관 형성에 큰 영향을 주지 않았다. 더 꾸준히 할수록 습관 곡선이 잘 맞았다(초록: "better model fit"). 자동성까지 18~254일, 66일은 곡선이 잘 맞은 39명의 중간값 | Lally 외, European Journal of Social Psychology 2010;40:998–1009 — [DOI](https://doi.org/10.1002/ejsp.674) | habit21-2026-10 (2010년대 — 2020년대 근거를 못 찾음) |
| 4주 프로그램의 한계 | 헬스장 회원 61,293명, 4주 프로그램 54개 무작위: 45%가 주간 방문을 9~27% 늘렸지만 끝난 뒤에도 효과가 남은 것은 8%. 1위는 "빠진 다음 다시 오면 주는 작은 보상"(125포인트 ≈ 9센트, 방문 27% 증가) | Milkman 외, Nature 2021;600:478–483 — [DOI](https://doi.org/10.1038/s41586-021-04128-4), [Penn Today](https://penntoday.upenn.edu/news/wharton-study-best-ways-boost-workout-habits) | habit21-2026-10 |
| 언제·어디서 계획 | 642개 실험 메타분석: 실행 의도가 생각·감정·행동 결과에 효과(d 0.27~0.66). 조건(if-then) 형식, 목표 동기가 높을 때, 계획을 되뇌었을 때 효과가 더 컸다 | Sheeran·Listrom·Gollwitzer, European Review of Social Psychology 2025;36(1) (온라인 2024) — [DOI](https://doi.org/10.1080/10463283.2024.2334563) | habit21-2026-10 |
| **(새 줄)** 끊긴 연속 기록 | 실험 7개: 행동 기록에서 이어진 연속 기록을 보여 주면 끊긴 연속 기록을 보여 줄 때보다 그 행동을 더 이어 갔다. 끊긴 이유를 자기 탓으로 돌리면 효과가 커지고, 끊긴 기록을 "메울" 수 있으면 줄었다. (보도 요약의 66% vs 58%는 원문 확인 못 함) | Silverman·Barasch, Journal of Consumer Research 2023;49(6):1095–1117 — [DOI](https://doi.org/10.1093/jcr/ucac029) | habit21-2026-10 |
| 미사용 후보 (그대로) | 미루기와 건강 — Johansson 외, JAMA Network Open 2023 | — | 미사용 |
