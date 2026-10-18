# 새 채널 분야 비교 — math · 롱폼 (숫자·원문만)

만든 때: 2026-10-18T16:10+09:00 · 도구: `tools/niche_scan.py v1.1 report` (할당량 0 — 탐색 목록·캐시만 읽음) · 탐색: 2026-10-18T16:10:03+09:00 · 최근 26주 · 받은 검색 22번 · 못 한 검색 0번

※ 연구·교육용. 해석·추천은 이 파일에 없다 (추천은 `math/README.md` 가 가리키는 문서 — 판단을 따로 적음).

## 0. 읽는 법·한계 (먼저)

- **표본** = 분야 검색어로 찾은 롱폼(4~20분·20분 넘음 검색, 각각 **최근 기간 조회수 순 상위 50개**, 라이브 아님) 중 올린 지 7일 넘고 4분 이상·광고 의심 아님, **한 채널은 최근 5개까지** (`[compare] PER_CHANNEL` — 한 채널이 비율을 덮지 않게). → '그 분야에서 **가장 많이 본 영상들**'이다 (분야 전체가 아님).
- **성공** = CLAUDE.md 성공 기준 그대로 (`math/analysis_rules.toml` [success]): 180일 안 · 구독자 50,000 이하 · 조회수 10,000 이상 · 조회수 ≥ 구독자 × 3. **성공 비율** = 성공 ÷ 표본 → '작은 채널이 그 분야 조회수 상위에 끼는 정도'. **성공 채널 몫** = 성공 영상이 하나라도 있는 채널 ÷ 표본 채널.
- **하루 조회수** = 조회수 ÷ 올린 뒤 날 수. **작은 채널 하루 조회수** = 구독자 5만 이하 채널 영상만 — 작은 채널이 그 분야에서 받는 수요.
- **새 채널** = 개설 24개월 안 · 구독자 1,000~200,000 (`[growth]`). **2년 안 1만** = 그중 구독자 10,000 이상 — 비율은 그 분야 표본 채널 수로 나눔. 월 증가 = 구독자 ÷ 개설 뒤 달 수 (평균 — 최근 속도 아님).
- **검색 결과 수** = YouTube 가 주는 totalResults (추정치 — 공급의 대략적인 크기, 정확하지 않음).
- **참고 점수** = 성공 비율 · 작은 채널 하루 조회수 · 2년 안 1만 비율의 분야 안 백분위 평균 × 100. 줄 세우기용이지 규칙이 아니다. 광고 단가(RPM)·제작 비용·경쟁 채널의 질은 들어 있지 않다.
- **만들기(판단)** 칸은 측정이 아니라 Claude 판단 (`niches.toml` make — 지금 제작 방식: 얼굴 없음·AI 내레이션 하나·HTML 애니메이션).
- 한 영상이 두 분야 검색어에 걸리면 두 분야에 다 셈. A 분야는 검색어 2개(표본 최대 200), B·기준은 1개(최대 100) — 그래서 개수 대신 비율로 견줌.
- 표본 30개 미만 분야는 ⚠️ (차이가 우연일 수 있음). 검색어 하나가 분야를 다 대표하지 못함 — 좋은 분야는 그 분야 폴더를 따로 만들어 태그로 다시 본다.
- 한국어·외국 영상 모두 (`INCLUDE_FOREIGN = true` — 검색은 언어 지정 없이, 분야마다 '외국 영상 몫'). 구독자 수는 지금 값(올린 때 값이 아님).
- **주제 관련 몫** = 표본 중 `keywords.toml` 관련어에 맞는 영상 몫 — 검색어가 그 주제 영상을 실제로 찾았는지 (낮으면 다른 뜻 영상이 섞임).

## 1. 분야 비교 (참고 점수 순)

| # | 분야 | 갈래 | 만들기(판단) | 표본 | 채널 | 외국 영상 몫 (성공 중 외국) | 주제 관련 몫 | 하루 조회수 중앙값 | 작은 채널 몫 | 큰 채널(100만↑) 몫 | 작은 채널 하루 조회수 (영상 수) | 작은 채널 배수 중앙값 | 성공 (채널) | **성공 비율** | 성공 채널 몫 | 성공 영상 길이(분) | 새 채널 | 2년 안 1만 (비율) | 새 채널 월 증가 중앙값 | 참고 점수 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 07. Mental math (영어) | A | 상 | 53 | 34 | 96% (15) | 66% | 2,910.9 | 30% | 30% | 4,267.9 (16) | 15 | 15 (11) | **28%** | 32% | 9.6 | 10 | 8 (24%) | 1,795 | 91.7 |
| 2 | 05. Math puzzle (영어) | A | 상 | 93 | 62 | 98% (38) | 84% | 3,259.3 | 46% | 27% | 3,561.2 (43) | 35.8 | 40 (27) | **43%** | 44% | 8.4 | 20 | 7 (11%) | 1,048.5 | 81.9 |
| 3 | 06. Math olympiad (영어) | A | 상 | 54 | 28 | 91% (21) | 98% | 617.6 | 48% | 9% | 1,365.7 (26) | 8 | 21 (10) | **39%** | 36% | 12.9 | 4 | 4 (14%) | 1,939.5 | 80.6 |
| 4 | 08. (기준) 재테크 | 기준 | 상 | 73 | 39 | 10% (1) | 1% | 5,191.7 | 3% | 56% | 6,304 (2 ⚠️) | 33.4 | 2 (2) | **3%** | 5% | 11.8 | 5 | 5 (13%) | 10,147 | 56.2 |
| 5 | 03. IQ·두뇌 퀴즈 | A | 상 | 34 | 29 | 29% (0) | 44% | 60.5 | 53% | 15% | 25.2 (18) | 0.8 | 1 (1) | **3%** | 3% | 9.2 | 6 | 2 (7%) | 343.5 | 50 |
| 6 | 09. (기준) stock market (영어) | 기준 | 상 | 61 | 45 | 100% (3) | 0% | 13,582.2 | 5% | 62% | 6,523 (3 ⚠️) | 87.9 | 3 (3) | **5%** | 7% | 27 | 2 | 2 (4%) | 5,324 | 37.5 |
| 7 | 01. 수학·계산 퀴즈 | A | 상 | 46 | 31 | 35% (0) | 100% | 13.1 | 80% | 6% | 10.5 (37) | 0.2 | 1 (1) | **2%** | 3% | 9.7 | 7 | 2 (6%) | 314 | 31.9 |
| 8 | 02. 암산 | A | 상 | 91 | 78 | 2% (0) | 100% | 10.1 | 89% | 7% | 8.2 (81) | 0.5 | 1 (1) | **1%** | 1% | 25.1 | 9 | 1 (1%) | 441 | 9.7 |
| 9 | 04. 교양 수학 (설명형) | A | 상 | 59 | 38 | 8% (0) | 92% | 4.4 | 83% | 7% | 2.7 (49) | 0.4 | 0 (0) | **0%** | 0% | - | 4 | 2 (5%) | 938.5 | 8.3 |

(갈래: A = 지금 제작 방식으로 만들 수 있음 · B = 촬영 필요(비교용) · 기준 = 지금 채널. 점수를 나눠 본 값은 아래 2번 표. 작은 채널 영상이 10개 미만이면 ⚠️ — 그 분야 점수는 작은 채널 하루 조회수를 빼고 나머지 두 숫자로)

## 2. 점수 나눠 보기 · 뺀 영상

백분위 0~100 (분야 안 순위 — 100 이 가장 높음, '-' = 점수에 안 씀).

| 분야 | 성공 비율 백분위 | 작은 채널 하루 조회수 백분위 | 2년 안 1만 비율 백분위 | 뺀 영상 (까닭:수) | 개설일 모르는 채널 |
|---|---|---|---|---|---|
| 07. Mental math (영어) | 75 | 100 | 100 | 올린 지 7일 안 됨:3, 광고 의심:1, 채널당 5개 넘음:10 | 0 |
| 05. Math puzzle (영어) | 100 | 83 | 62 | 광고 의심:4, 채널당 5개 넘음:7 | 0 |
| 06. Math olympiad (영어) | 88 | 67 | 88 | 올린 지 7일 안 됨:1, 채널당 5개 넘음:12 | 0 |
| 08. (기준) 재테크 | 38 | - | 75 | 올린 지 7일 안 됨:5, 채널당 5개 넘음:22 | 0 |
| 03. IQ·두뇌 퀴즈 | 50 | 50 | 50 | 채널당 5개 넘음:4 | 0 |
| 09. (기준) stock market (영어) | 62 | - | 12 | 올린 지 7일 안 됨:3, 채널당 5개 넘음:2 | 0 |
| 01. 수학·계산 퀴즈 | 25 | 33 | 38 | 올린 지 7일 안 됨:5, 광고 의심:1, 채널당 5개 넘음:11 | 0 |
| 02. 암산 | 12 | 17 | 0 | 올린 지 7일 안 됨:1 | 0 |
| 04. 교양 수학 (설명형) | 0 | 0 | 25 | 올린 지 7일 안 됨:2, 채널당 5개 넘음:4 | 0 |

## 3. 검색어별 (분야 안에서 검색어끼리 결과가 맞는지)

| 분야 | 검색어 | 4~20분 결과 | 20분 넘음 결과 | 표본에 든 영상 | 성공 (비율) | 유튜브 결과 수(추정, 4~20분 / 20분 넘음) | 못 한 검색 | 받은 때 |
|---|---|---|---|---|---|---|---|---|
| 01. 수학·계산 퀴즈 | 계산 퀴즈 | 6 | 2 | 7 | 0 (0%) | 67,832 / 120,976 | 0 | 2026-10-18T06:29 |
| 01. 수학·계산 퀴즈 | 수학 퀴즈 | 50 | 24 | 39 | 1 (3%) | 81,236 / 114,370 | 0 | 2026-10-18T06:29 |
| 02. 암산 | 암산 | 50 | 50 | 91 | 1 (1%) | 93,404 / 75,514 | 0 | 2026-10-18T06:29 |
| 03. IQ·두뇌 퀴즈 | IQ 테스트 | 50 | 50 | 34 | 1 (3%) | 46,075 / 19,788 | 0 | 2026-10-18T06:29 |
| 04. 교양 수학 (설명형) | 수학 이야기 | 50 | 50 | 59 | 0 (0%) | 443,112 / 950,133 | 0 | 2026-10-18T06:29 |
| 05. Math puzzle (영어) | can you solve this | 50 | 50 | 53 | 29 (55%) | 1,000,000 / 1,000,000 | 0 | 2026-10-18T07:10 |
| 05. Math puzzle (영어) | math puzzle | 50 | 50 | 42 | 11 (26%) | 179,891 / 405,515 | 0 | 2026-10-18T06:29 |
| 06. Math olympiad (영어) | math olympiad | 50 | 50 | 54 | 21 (39%) | 106,693 / 166,873 | 0 | 2026-10-18T06:29 |
| 07. Mental math (영어) | mental math | 50 | 50 | 53 | 15 (28%) | 237,489 / 558,421 | 0 | 2026-10-18T06:29 |
| 08. (기준) 재테크 | 재테크 | 50 | 50 | 73 | 2 (3%) | 820,738 / 1,000,000 | 0 | 2026-10-18T06:29 |
| 09. (기준) stock market (영어) | stock market | 50 | 50 | 61 | 3 (5%) | 1,000,000 / 1,000,000 | 0 | 2026-10-18T07:10 |

## 4. 분야를 넘나드는 빨리 큰 새 채널 (개설 24개월 안 · 월 구독자 증가 순 30곳)

이름만 보고 연예인·방송사·브랜드 채널을 다 가려내지 못함 (`[growth] BRAND_HINT` 낱말만 표시) — 유명인 덕에 큰 채널이 섞여 있다.

| # | 채널 | 분야 | 구독자 | 개설 뒤 달 | 월 증가 | 채널 영상 수 | 표본에서 가장 많이 본 영상 | 조회수 |
|---|---|---|---|---|---|---|---|---|
| 1 | 강지영의 동그라미 | 08. (기준) 재테크 | 146,000 | 7.6 | 19,323 | 89 | [20대에 돈 가장 빨리 모으는 현실적인 방법 (ISA, ETF 활용법)](https://youtu.be/1AFnKX2-rt0) | 1,055,121 |
| 2 | 경제해적단 | 08. (기준) 재테크 | 122,000 | 7.0 | 17,435 | 53 | [돈이 스스로 일하기 시작하는 시작점](https://youtu.be/PEnNxbBd5eY) | 808,761 |
| 3 | Mini Genios TV | 07. Mental math (영어) | 105,000 | 6.8 | 15,441 | 121 | [¡Reto de Sumas para Niños de 5 a 6 Años! 31 Ejercicios Diver](https://youtu.be/gnGsJaK3NLc) | 1,601,812 |
| 4 | MenteQuiz | 05. Math puzzle (영어) | 26,700 | 1.9 | 14,013 | 41 | [¿Puedes Resolverlos Todos? ¡15 Acertijos Visuales Para Mente](https://youtu.be/VZTqnJYaLQ8) | 172,601 |
| 5 | 알아봤음 | 03. IQ·두뇌 퀴즈 | 81,600 | 6.5 | 12,482 | 54 | [IQ 70부터 초월까지, 지능의 10단계를 알아봤음](https://youtu.be/FjorC6IBfxI) | 5,986 |
| 6 | ETF 아는 형 | 08. (기준) 재테크 | 158,000 | 15.6 | 10,147 | 963 | [노후 자금 주식에 올인했다간 큰일 납니다, 은퇴자가 무조건 사서 묻어둬야 할 ETF 종목 / 존리 / ETF](https://youtu.be/e3EY2JJMgDw) | 960,840 |
| 7 | Prof. Lorena Salviano / Alfabetização | 07. Mental math (영어), 05. Math puzzle (영어) | 141,000 | 15.9 | 8,850 | 160 | [DESAFIO DE MATEMÁTICA ⏰ Resolva antes do tempo acabar / Adiç](https://youtu.be/XZgCQ_YyenQ) | 1,006,002 |
| 8 | Zyla and Myla | 03. IQ·두뇌 퀴즈 | 53,000 | 6.7 | 7,947 | 565 | [ONLY GENIUSES CAN BEAT THIS ROBLOX IQ TEST! ..😱🚫/ #roblox #t](https://youtu.be/uApNAthlCfM) | 609 |
| 9 | Moneytalks by Groww | 09. (기준) stock market (영어) | 136,000 | 17.6 | 7,738 | 234 | [What 40 Years in the Stock Market Taught Him / Story of Tita](https://youtu.be/qx6BQ2m_azY) | 1,235,919 |
| 10 | Turing | 06. Math olympiad (영어) | 107,000 | 19.8 | 5,410 | 100 | [How USA Beat China at Math Olympiad After 20 Years](https://youtu.be/g-SGCAul4RY) | 93,053 |
| 11 | Riddle Detective | 05. Math puzzle (영어) | 9,900 | 2.0 | 5,023 | 10 | [Only 1% Can Solve All 26 Detective Riddles! Are You One of T](https://youtu.be/xVNyiHHWJXA) | 396,482 |
| 12 | One Theorem | 05. Math puzzle (영어) | 31,500 | 7.5 | 4,187 | 38 | [เกมที่ใช้เวลาเล่นจบนานกว่าอายุของจักรวาล / Tower of Hanoi](https://youtu.be/jpLFFTO_lf8) | 190,262 |
| 13 | Quiz Patrol | 05. Math puzzle (영어) | 14,400 | 3.7 | 3,914 | 15 | [Only Real Detectives Can Solve All 20 Riddles! / Quiz Patrol](https://youtu.be/USIP4xK-mMQ) | 737,481 |
| 14 | Chips drama | 06. Math olympiad (영어) | 69,600 | 22.0 | 3,162 | 1,823 | [My daughter's perfect math score got zeroed — I called the f](https://youtu.be/Us4rBD73cR8) | 26,834 |
| 15 | Films Vibee | 09. (기준) stock market (영어) | 32,600 | 11.2 | 2,910 | 89 | [Ek Bewakoof Ladka Stock Market Hack Karke Ban Gaya Crorepati](https://youtu.be/rjPzSHuNpuQ) | 427,383 |
| 16 | 꽃피는인생 - 드라마사연 | 02. 암산 | 6,460 | 2.3 | 2,850 | 16 | ["그 재무제표는 조작됐습니다!" 고졸 청소부 천재소녀가 암산 하나로 5조 사기매각을 뒤집는데...](https://youtu.be/vlun7R0BXqQ) | 13,477 |
| 17 | 술술 경제학 | 08. (기준) 재테크 | 17,600 | 6.3 | 2,790 | 52 | [국민연금 빈칸 메우는 한국 ETF 3개 — 월 200만 원 평생 월급 만들기](https://youtu.be/7rtO_hfLvF8) | 608,643 |
| 18 | 무신극장 | 02. 암산 | 20,700 | 7.6 | 2,716 | 430 | [[한국어 더빙]무신이 암산 후 400근 뚱뚱이 폐물에 빙의해, 종문대회서 사승과 사주 무괴를 연파하고 무림맹](https://youtu.be/gzKYj6lMh34) | 5,777 |
| 19 | Zye the Fish | 05. Math puzzle (영어), 01. 수학·계산 퀴즈 | 34,600 | 13.6 | 2,544 | 14 | [How my question got in a math competition in Germany](https://youtu.be/FI1o6w3AApo) | 254,924 |
| 20 | Latest drama's | 07. Mental math (영어) | 13,100 | 5.3 | 2,477 | 300 | [[ENG DUB]A Poor Student, A Math Genius, and a Revenge That S](https://youtu.be/mZIBFPjno7Y) | 90,865 |
| 21 | Growth In Silence | 07. Mental math (영어) | 16,500 | 6.9 | 2,380 | 58 | [The Math Secret Top Students Never Share — Learn So Fast It ](https://youtu.be/BefAUlKrj3s) | 300,053 |
| 22 | Simplicrack Maths | 07. Mental math (영어) | 22,500 | 9.8 | 2,306 | 71 | [Practice this Daily 30 Minutes and your Calculations are Sor](https://youtu.be/nJyqT0ZblNI) | 106,440 |
| 23 | M-Quiz | 05. Math puzzle (영어) | 16,200 | 7.1 | 2,283 | 23 | [20 mind-bending riddles that only highly intelligent people ](https://youtu.be/E8J0lbZSkeE) | 1,774,843 |
| 24 | Brain Burst 🧠⚡ | 05. Math puzzle (영어) | 6,110 | 2.8 | 2,163 | 72 | [Can You Solve All 10 Puzzles? 🧠 / Only Geniuses Can Get 10/1](https://youtu.be/mlqxa12F1UE) | 257,793 |
| 25 | Sleeping Philosophy | 04. 교양 수학 (설명형) | 31,900 | 18.0 | 1,769 | 114 | [The Story Of Mathematics: Definition, History, Importance & ](https://youtu.be/fvjLw9NCSuM) | 8,730 |
| 26 | Faza 1 Online Tutor | 01. 수학·계산 퀴즈 | 34,200 | 20.6 | 1,658 | 510 | [🔥 Mixed Paper 1 Maths Questions / Exam Preparation & Practic](https://youtu.be/KrKeMXBiN70) | 2,759 |
| 27 | Math Puzzle 2.0 | 05. Math puzzle (영어) | 8,790 | 5.5 | 1,602 | 144 | [Math Puzzle 19-09-2026](https://youtu.be/u-dWzQfMEHU) | 81,081 |
| 28 | Perfect Tricky Math | 07. Mental math (영어) | 29,600 | 23.1 | 1,284 | 707 | [⚡ 10 सेकंड में जोड़ की ट्रिक / दिमाग हिला देने वाला तरीका #M](https://youtu.be/WK_zHlNoPAQ) | 346,600 |
| 29 | 정밀쌤의 아무튼 결론은 | 04. 교양 수학 (설명형) | 5,660 | 4.6 | 1,222 | 144 | [수학이 인생에 주는 영향｜원론적으로 이야기해 봐야 소용없고 경험담](https://youtu.be/l4W13je4M8U) | 9,091 |
| 30 | Can You Solve? | 05. Math puzzle (영어) | 3,210 | 2.9 | 1,110 | 34 | [Only 1% Can Solve All 15 Riddles! Test Your Brain Now 🧠](https://youtu.be/T7BbwrbKwfg) | 278,346 |

## 5. 분야별 예 (성공 영상 배수 순 · 빨리 큰 새 채널)

### 07. Mental math (영어) — 표본 53 · 성공 15 (28%) · 검색어 mental math

| 성공 롱폼 | 채널 | 구독자 | 조회수 | 배수 | 분 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [Only a genius can solve this Algebra equation / Math Olympiad Mathemat](https://youtu.be/-OXRYeXQ8bQ) | Math Booth | 9,530 | 4,988,403 | 523.4 | 9.9 | 43 | 외국 |
| [1 बार सीख लिया तो गणित कभी नहीं भूलोगे 😱 / 24 Maths Topics / Basic to ](https://youtu.be/PAlIeA06H6k) | JMB Maths Academy  | 3,810 | 329,456 | 86.5 | 93.5 | 65 | 외국 |
| [USA/ Olympiad Math Challenge/ Exponential Algebra Problem/ Can you fin](https://youtu.be/xfVjrRGHFmI) | Shorif Sir  | 13,400 | 946,880 | 70.7 | 13.2 | 78 | 외국 |
| [Can You Pass This Addition Quiz? ➕🧠 Easy to Hard / Math Quiz for Kinde](https://youtu.be/Mmez8R53CCU) | Tiny Math Genius | 48,900 | 1,478,423 | 30.2 | 9 | 90 | 외국 |
| [¿Eres Rápido CALCULANDO MENTALMENTE? 🤔⏰️🧠 / Quiz de MATEMÁTICAS para G](https://youtu.be/MacVhAoVphw) | La Cabra Quiz 🔢 | 4,020 | 92,775 | 23.1 | 9.6 | 155 | 외국 |

빨리 큰 새 채널: Mini Genios TV (구독자 105,000, 7개월, 월 15,441) · Prof. Lorena Salviano / Alfabetização (구독자 141,000, 16개월, 월 8,850) · Latest drama's (구독자 13,100, 5개월, 월 2,477) · Growth In Silence (구독자 16,500, 7개월, 월 2,380) · Simplicrack Maths (구독자 22,500, 10개월, 월 2,306)

### 05. Math puzzle (영어) — 표본 93 · 성공 40 (43%) · 검색어 math puzzle, can you solve this

| 성공 롱폼 | 채널 | 구독자 | 조회수 | 배수 | 분 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [Only a genius can solve this Algebra equation / Math Olympiad Mathemat](https://youtu.be/-OXRYeXQ8bQ) | Math Booth | 9,530 | 4,988,403 | 523.4 | 9.9 | 43 | 외국 |
| [Only Geniuses Can Solve These 15 Tricky Detective Riddles with Answers](https://youtu.be/zgIz6YPNrRc) | Quiz Rush 🧠⚡ | 3,170 | 709,236 | 223.7 | 7.8 | 114 | 외국 |
| [Find the Killer 🕵️ Only 1% Can Solve This + 20 Riddles](https://youtu.be/b-8selVlXBs) | Cluevora | 983 | 217,586 | 221.3 | 6.6 | 171 | 외국 |
| [🤔99% People Fail / Brain Challenge Can You Solve This Puzzle / The Gam](https://youtu.be/yecLVn0TtmQ) | The Game Challengers | 880 | 177,149 | 201.3 | 13.6 | 127 | 외국 |
| [15 Riddles Only Geniuses Can Solve! (95% Fail 😱)](https://youtu.be/BtUD8y6m29s) | Quiz Rush | 1,040 | 178,655 | 171.8 | 6.7 | 155 | 외국 |

빨리 큰 새 채널: MenteQuiz (구독자 26,700, 2개월, 월 14,013) · Prof. Lorena Salviano / Alfabetização (구독자 141,000, 16개월, 월 8,850) · Riddle Detective (구독자 9,900, 2개월, 월 5,023) · One Theorem (구독자 31,500, 8개월, 월 4,187) · Quiz Patrol (구독자 14,400, 4개월, 월 3,914)

### 06. Math olympiad (영어) — 표본 54 · 성공 21 (39%) · 검색어 math olympiad

| 성공 롱폼 | 채널 | 구독자 | 조회수 | 배수 | 분 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [USA/ Olympiad Math Challenge/ Exponential Algebra Problem/ Can you fin](https://youtu.be/xfVjrRGHFmI) | Shorif Sir  | 13,400 | 946,880 | 70.7 | 13.2 | 78 | 외국 |
| [Germany / Can You Solve This Math Olympiad Problem?](https://youtu.be/W9pB5RdZprM) | ALL ABOUT MATH | 826 | 39,033 | 47.3 | 16.9 | 100 | 외국 |
| [Nice math olympiad Simplification l Calculator Not Allowed ](https://youtu.be/4Ziw62lWHuA) | J Educational Tutorials  | 7,060 | 231,987 | 32.9 | 6.4 | 67 | 외국 |
| [I gave myself a year to win a medal on the International Math Olympiad](https://youtu.be/Bpmjk_oWXng) | Art of Olympiad Mathematics | 12,100 | 276,778 | 22.9 | 22.4 | 57 | 외국 |
| [The Journey to the International Maths Olympiad](https://youtu.be/HO-xnaabsho) | Narein | 4,210 | 68,832 | 16.4 | 16.6 | 103 | 외국 |

빨리 큰 새 채널: Turing (구독자 107,000, 20개월, 월 5,410) · Chips drama (구독자 69,600, 22개월, 월 3,162) · Shorif Sir  (구독자 13,400, 19개월, 월 717) · Art of Olympiad Mathematics (구독자 12,100, 20개월, 월 608)

### 08. (기준) 재테크 — 표본 73 · 성공 2 (3%) · 검색어 재테크

| 성공 롱폼 | 채널 | 구독자 | 조회수 | 배수 | 분 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [국민연금 빈칸 메우는 한국 ETF 3개 — 월 200만 원 평생 월급 만들기](https://youtu.be/7rtO_hfLvF8) | 술술 경제학 | 17,600 | 608,643 | 34.6 | 16.8 | 171 |  |
| [26살에 1억 모으기까지, 제가 실제로 했던 것들](https://youtu.be/h0VxOzLb_oc) | 돈모으는 단곰 | 18,000 | 579,114 | 32.2 | 6.8 | 64 | 외국 |

빨리 큰 새 채널: 강지영의 동그라미 (구독자 146,000, 8개월, 월 19,323) · 경제해적단 (구독자 122,000, 7개월, 월 17,435) · ETF 아는 형 (구독자 158,000, 16개월, 월 10,147) · 술술 경제학 (구독자 17,600, 6개월, 월 2,790) · 돈모으는 단곰 (구독자 18,000, 17개월, 월 1,048)

### 03. IQ·두뇌 퀴즈 — 표본 34 · 성공 1 (3%) · 검색어 IQ 테스트

| 성공 롱폼 | 채널 | 구독자 | 조회수 | 배수 | 분 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [상위 1% 두뇌를 가진 44명의 연예인 아이큐 순위 총정리 /  연예인 멘사 회원 리스트](https://youtu.be/hLo2WBmjW3Y) | 스타쇼 | 12,800 | 101,200 | 7.9 | 9.2 | 159 |  |

빨리 큰 새 채널: 알아봤음 (구독자 81,600, 6개월, 월 12,482) · Zyla and Myla (구독자 53,000, 7개월, 월 7,947) · StickToons (구독자 3,230, 7개월, 월 487) · 눈박사 임태형 [클리어서울안과] (구독자 3,440, 17개월, 월 200) · AUGMUNT (구독자 1,960, 14개월, 월 135)

### 09. (기준) stock market (영어) — 표본 61 · 성공 3 (5%) · 검색어 stock market

| 성공 롱폼 | 채널 | 구독자 | 조회수 | 배수 | 분 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [गरीब किसान का करोड़पति बेटा / Stock Market Success Story / प्रेरणादायक](https://youtu.be/eQ5fJ6YttKo) | Shonty Tales | 573 | 310,111 | 541.2 | 26.2 | 71 | 외국 |
| [The Story Behind India's Biggest Stock Market Scam / Scam 1992 Explain](https://youtu.be/zay8CuiBUQ8) | DOKio | 7,720 | 678,396 | 87.9 | 27 | 104 | 외국 |
| [Ek Bewakoof Ladka Stock Market Hack Karke Ban Gaya Crorepati! / Money ](https://youtu.be/rjPzSHuNpuQ) | Films Vibee | 32,600 | 427,383 | 13.1 | 31.5 | 28 | 외국 |

빨리 큰 새 채널: Moneytalks by Groww (구독자 136,000, 18개월, 월 7,738) · Films Vibee (구독자 32,600, 11개월, 월 2,910)

### 01. 수학·계산 퀴즈 — 표본 46 · 성공 1 (2%) · 검색어 수학 퀴즈, 계산 퀴즈

| 성공 롱폼 | 채널 | 구독자 | 조회수 | 배수 | 분 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [독일 대학 경시대회에 내 수학문제 나옴](https://youtu.be/1uVa_U4jQDk) | Zye the Fish | 34,600 | 646,941 | 18.7 | 9.7 | 118 |  |

빨리 큰 새 채널: Zye the Fish (구독자 34,600, 14개월, 월 2,544) · Faza 1 Online Tutor (구독자 34,200, 21개월, 월 1,658) · 퀴즈월드Tv (구독자 7,770, 22개월, 월 351) · Quiz Point (구독자 5,820, 19개월, 월 314) · 이공 수학 연구소 (구독자 2,470, 16개월, 월 155)

### 02. 암산 — 표본 91 · 성공 1 (1%) · 검색어 암산

| 성공 롱폼 | 채널 | 구독자 | 조회수 | 배수 | 분 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [제암산 (보성)](https://youtu.be/tIDrRXNOxqY) | 진유산악  | 2,260 | 11,947 | 5.3 | 25.1 | 139 |  |

빨리 큰 새 채널: 꽃피는인생 - 드라마사연 (구독자 6,460, 2개월, 월 2,850) · 무신극장 (구독자 20,700, 8개월, 월 2,716) · 김PD의 너만 산이냐 나도 산이다 (구독자 4,780, 8개월, 월 573) · 외로운사랑 극장 (구독자 2,230, 4개월, 월 534) · 핫타임트롯TV (구독자 2,810, 6개월, 월 441)

### 04. 교양 수학 (설명형) — 표본 59 · 성공 0 (0%) · 검색어 수학 이야기

성공 롱폼 없음.

빨리 큰 새 채널: Sleeping Philosophy (구독자 31,900, 18개월, 월 1,769) · 정밀쌤의 아무튼 결론은 (구독자 5,660, 5개월, 월 1,222) · 지혜의 조각 (구독자 11,100, 17개월, 월 655) · KST MATHEMATICS BY SHEETAL SINGH  (구독자 1,720, 5개월, 월 340)

