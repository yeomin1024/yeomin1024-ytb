# 새 채널 분야 비교 — math · 쇼츠 (숫자·원문만)

만든 때: 2026-10-18T16:10+09:00 · 도구: `tools/niche_scan.py v1.1 report --shorts` (할당량 0 — 탐색 목록·캐시만 읽음) · 탐색: 2026-10-18T16:10:16+09:00 · 최근 26주 · 받은 검색 11번 · 못 한 검색 0번

※ 연구·교육용. 해석·추천은 이 파일에 없다 (추천은 `math/README.md` 가 가리키는 문서 — 판단을 따로 적음).

## 0. 읽는 법·한계 (먼저)

- **표본** = 분야 검색어로 찾은 **쇼츠**(4분 미만 검색 · **최근 기간 조회수 순 상위 50개** → 180초 이하·세로만, 라이브 아님) 중 올린 지 3일 넘음 · **조회수 부풀림 의심**(조회수 5만↑인데 좋아요 0.2% 미만 — 광고·반복 재생)·쇼츠 아님? 뺌, **한 채널은 최근 5개까지** (`[shorts_compare] PER_CHANNEL`). → '그 분야에서 **가장 많이 본 쇼츠들**'이다.
- **성공** = 쇼츠 성공 기준 (`math/analysis_rules.toml` [shorts]): 3~180일 · 구독자 50,000 이하 · 조회수 50,000 이상 · 조회수 ≥ 구독자 × 3. 쇼츠 조회수는 다시 재생도 셈 (2025-03-31~). **성공 비율** = 성공 ÷ 표본. **성공 채널 몫** = 성공 쇼츠가 하나라도 있는 채널 ÷ 표본 채널.
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

| # | 분야 | 갈래 | 만들기(판단) | 표본 | 채널 | 외국 영상 몫 (성공 중 외국) | 주제 관련 몫 | 하루 조회수 중앙값 | 작은 채널 몫 | 큰 채널(100만↑) 몫 | 작은 채널 하루 조회수 (영상 수) | 작은 채널 배수 중앙값 | 성공 (채널) | **성공 비율** | 성공 채널 몫 | 성공 쇼츠 길이(초) | 새 채널 | 2년 안 1만 (비율) | 새 채널 월 증가 중앙값 | 참고 점수 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 05. Math puzzle (영어) | A | 상 | 90 | 64 | 99% (18) | 74% | 20,813.3 | 20% | 22% | 40,574 (18) | 81.6 | 18 (16) | **20%** | 25% | 31 | 19 | 15 (23%) | 2,953 | 75 |
| 2 | 03. IQ·두뇌 퀴즈 | A | 상 | 40 | 30 | 52% (8) | 48% | 5,262.9 | 42% | 8% | 3,866.1 (17) | 19.5 | 16 (11) | **40%** | 37% | 32.5 | 10 | 7 (23%) | 3,028.5 | 72.1 |
| 3 | 02. 암산 | A | 상 | 45 | 42 | 4% (1) | 98% | 2,120.2 | 76% | 13% | 1,573.9 (34) | 8.8 | 15 (15) | **33%** | 36% | 19 | 30 | 17 (40%) | 1,049 | 71.7 |
| 4 | 08. (기준) 재테크 | 기준 | 상 | 41 | 35 | 0% (0) | 0% | 15,873.7 | 34% | 20% | 30,239 (14) | 131.3 | 14 (14) | **34%** | 40% | 52.5 | 11 | 7 (20%) | 2,772 | 68.3 |
| 5 | 06. Math olympiad (영어) ⚠️ | A | 상 | 29 | 16 | 100% (5) | 93% | 9,699.1 | 17% | 3% | 1,514.9 (5 ⚠️) | 13.1 | 5 (5) | **17%** | 31% | 58 | 6 | 5 (31%) | 3,641 | 62.5 |
| 6 | 07. Mental math (영어) | A | 상 | 36 | 30 | 92% (8) | 75% | 35,441.3 | 25% | 14% | 49,103.6 (9 ⚠️) | 127.6 | 9 (9) | **25%** | 30% | 39 | 9 | 7 (23%) | 5,098 | 59.4 |
| 7 | 01. 수학·계산 퀴즈 | A | 상 | 74 | 46 | 8% (2) | 96% | 186.1 | 89% | 3% | 169.5 (66) | 9.5 | 8 (7) | **11%** | 15% | 21.5 | 14 | 6 (13%) | 896 | 23.3 |
| 8 | 09. (기준) stock market (영어) | 기준 | 상 | 42 | 25 | 98% (4) | 0% | 25,039.2 | 10% | 67% | 33,518.7 (4 ⚠️) | 257.3 | 4 (4) | **10%** | 16% | 32 | 3 | 0 (0%) | 847 | 6.2 |
| 9 | 04. 교양 수학 (설명형) | A | 상 | 44 | 21 | 7% (0) | 100% | 84.4 | 98% | 0% | 86.7 (43) | 8.9 | 4 (1) | **9%** | 5% | 58.5 | 3 | 1 (5%) | 467 | 4.2 |

(갈래: A = 지금 제작 방식으로 만들 수 있음 · B = 촬영 필요(비교용) · 기준 = 지금 채널. 점수를 나눠 본 값은 아래 2번 표. 작은 채널 영상이 10개 미만이면 ⚠️ — 그 분야 점수는 작은 채널 하루 조회수를 빼고 나머지 두 숫자로)

## 2. 점수 나눠 보기 · 뺀 영상

백분위 0~100 (분야 안 순위 — 100 이 가장 높음, '-' = 점수에 안 씀).

| 분야 | 성공 비율 백분위 | 작은 채널 하루 조회수 백분위 | 2년 안 1만 비율 백분위 | 뺀 영상 (까닭:수) | 개설일 모르는 채널 |
|---|---|---|---|---|---|
| 05. Math puzzle (영어) | 50 | 100 | 75 | 올린 지 3일 안 됨:3, 부풀림 의심:1 | 0 |
| 03. IQ·두뇌 퀴즈 | 100 | 60 | 56 | 부풀림 의심:2, 올린 지 3일 안 됨:3 | 0 |
| 02. 암산 | 75 | 40 | 100 | 올린 지 3일 안 됨:2 | 0 |
| 08. (기준) 재테크 | 88 | 80 | 38 | 부풀림 의심:5 | 0 |
| 06. Math olympiad (영어) | 38 | - | 88 | 채널당 5개 넘음:20 | 0 |
| 07. Mental math (영어) | 62 | - | 56 | 채널당 5개 넘음:14 | 0 |
| 01. 수학·계산 퀴즈 | 25 | 20 | 25 | 올린 지 3일 안 됨:3, 채널당 5개 넘음:20 | 0 |
| 09. (기준) stock market (영어) | 12 | - | 0 | 채널당 5개 넘음:1 | 0 |
| 04. 교양 수학 (설명형) | 0 | 0 | 12 | 채널당 5개 넘음:4 | 0 |

## 3. 검색어별 (분야 안에서 검색어끼리 결과가 맞는지)

| 분야 | 검색어 | 쇼츠 검색 결과 | 표본에 든 영상 | 성공 (비율) | 유튜브 결과 수(추정) | 못 한 검색 | 받은 때 |
|---|---|---|---|---|---|---|---|
| 01. 수학·계산 퀴즈 | 계산 퀴즈 | 50 | 38 | 0 (0%) | 113,448 | 0 | 2026-10-18T07:10 |
| 01. 수학·계산 퀴즈 | 수학 퀴즈 | 50 | 36 | 8 (22%) | 251,809 | 0 | 2026-10-18T07:10 |
| 02. 암산 | 암산 | 50 | 45 | 15 (33%) | 448,579 | 0 | 2026-10-18T07:10 |
| 03. IQ·두뇌 퀴즈 | IQ 테스트 | 50 | 40 | 16 (40%) | 39,837 | 0 | 2026-10-18T07:10 |
| 04. 교양 수학 (설명형) | 수학 이야기 | 50 | 44 | 4 (9%) | 1,000,000 | 0 | 2026-10-18T07:10 |
| 05. Math puzzle (영어) | can you solve this | 50 | 45 | 9 (20%) | 1,000,000 | 0 | 2026-10-18T07:10 |
| 05. Math puzzle (영어) | math puzzle | 50 | 46 | 10 (22%) | 974,920 | 0 | 2026-10-18T07:10 |
| 06. Math olympiad (영어) | math olympiad | 50 | 29 | 5 (17%) | 434,215 | 0 | 2026-10-18T07:10 |
| 07. Mental math (영어) | mental math | 50 | 36 | 9 (25%) | 993,949 | 0 | 2026-10-18T07:10 |
| 08. (기준) 재테크 | 재테크 | 50 | 41 | 14 (34%) | 1,000,000 | 0 | 2026-10-18T07:10 |
| 09. (기준) stock market (영어) | stock market | 50 | 42 | 4 (10%) | 1,000,000 | 0 | 2026-10-18T07:10 |

## 4. 분야를 넘나드는 빨리 큰 새 채널 (개설 24개월 안 · 월 구독자 증가 순 30곳)

이름만 보고 연예인·방송사·브랜드 채널을 다 가려내지 못함 (`[growth] BRAND_HINT` 낱말만 표시) — 유명인 덕에 큰 채널이 섞여 있다.

| # | 채널 | 분야 | 구독자 | 개설 뒤 달 | 월 증가 | 채널 영상 수 | 표본에서 가장 많이 본 영상 | 조회수 |
|---|---|---|---|---|---|---|---|---|
| 1 | 손승아 SEUNG | 03. IQ·두뇌 퀴즈 | 195,000 | 6.7 | 28,955 | 230 | [IQ TEST dance Challenge?? What Will the Results Be??](https://youtu.be/-gu1QwJ3fN4) | 88,871 |
| 2 | Priya L story | 05. Math puzzle (영어) | 186,000 | 6.8 | 27,220 | 180 | [Can You Solve This? 🤯🔥#tiktok #bts #shorts #funny](https://youtu.be/oyvyxWGvDzg) | 356,962 |
| 3 | INDIAN MANGO  | 05. Math puzzle (영어) | 138,000 | 5.4 | 25,459 | 164 | [Can You Solve the 14-Piece Wooden Hexagon Puzzle in 60 Secon](https://youtu.be/PmUrlt3F7Bs) | 2,206,194 |
| 4 | Learn With Shakil | 07. Mental math (영어) | 154,000 | 8.4 | 18,383 | 441 | [USA method VS Japan method Solving (5+3)^2 😮🥶🔥](https://youtu.be/JurLM1SnnaY) | 1,005,982 |
| 5 | Myst Editz | 05. Math puzzle (영어), 06. Math olympiad (영어), 07. Mental math (영어) | 150,000 | 9.8 | 15,271 | 218 | [The Japanese Method of Division 🇯🇵🧠 #maths](https://youtu.be/lSvqIdunp6A) | 4,740,532 |
| 6 | Mr Random Talks | 05. Math puzzle (영어) | 143,000 | 10.1 | 14,133 | 300 | [Can You Solve This Impossible Coin Puzzle? #shortvideo](https://youtu.be/ZbEDbAvGORo) | 439,969 |
| 7 | Thalis P | 05. Math puzzle (영어) | 113,000 | 8.0 | 14,097 | 157 | [Você consegue resolver este enigma do dinheiro roubado?](https://youtu.be/RaAvGNNIpEw) | 1,181,258 |
| 8 | Almost Athletes with Dude Perfect | 05. Math puzzle (영어) | 185,000 | 14.4 | 12,857 | 584 | [Can You Solve This Before Mark Rober? 🤯](https://youtu.be/2_7cWEJ0oWI) | 1,188,040 |
| 9 | マイブーム【Myboom】 | 07. Mental math (영어) | 110,000 | 9.6 | 11,428 | 173 | [フラッシュ暗算、適当に答えててもバレない説](https://youtu.be/Iy7fhpVKE8c) | 725,214 |
| 10 | The Kushwaha Sir | 07. Mental math (영어) | 103,000 | 9.6 | 10,701 | 230 | [Cube of ANY Number in Seconds! 💎🔥 / Calculator se bhi Tez! ⚡](https://youtu.be/019pUC6YqDU) | 224,265 |
| 11 | ETF 아는 형 | 08. (기준) 재테크 | 158,000 | 15.6 | 10,147 | 963 | [ETF 잘 모르면 S&P500만 투자하면 된다?](https://youtu.be/12SwPjznlyE) | 637,262 |
| 12 | 오늘마셋(TODAY MINDSET) | 03. IQ·두뇌 퀴즈 | 111,000 | 11.2 | 9,909 | 299 | [이지영쌤 아이큐 98점 IQ의 숨겨진 사실](https://youtu.be/o8HngCCDwCU) | 6,258,708 |
| 13 | Primary Hub | 05. Math puzzle (영어) | 70,900 | 8.2 | 8,633 | 91 | [Make 5 squares with 2moves // Cognitive Development #educati](https://youtu.be/lU8SkVmz4p8) | 351,796 |
| 14 | 펜앤경제TV | 08. (기준) 재테크 | 121,000 | 16.4 | 7,366 | 2,569 | [100억 자산가의 경고... 이럴거면 "주식 하지 마세요" / 함익병 원장 / 권재홍의 아는게 힘](https://youtu.be/nGxEwhsW5rA) | 3,509,154 |
| 15 | MOVIESTARWA | 08. (기준) 재테크 | 81,300 | 11.5 | 7,091 | 345 | [(🚨신동엽썰) 김경식은 "재테크의 귀재", 길가다 홧 김에 계약했을 뿐인데.. #짠한형 #신동엽 #김경식 #](https://youtu.be/_5oIhmMczy0) | 6,831,247 |
| 16 | 펫파라치 | 02. 암산 | 81,200 | 12.0 | 6,790 | 749 | [초딩보다 더 똑똑한 물고기의 암산 실력ㅋㅋ #동물 #물고기](https://youtu.be/3WucJjfCixk) | 25,950 |
| 17 | Quickmath shorts | 06. Math olympiad (영어) | 22,900 | 3.6 | 6,395 | 204 | [Old Method vs New Trick 🤯 Which one is easier? 👇#Math #MathT](https://youtu.be/ISgmjsGxpUM) | 106,690 |
| 18 | 위키타카 | 08. (기준) 재테크 | 75,200 | 11.8 | 6,376 | 1,671 | [아무리 주식 공부해도 돈 못 버는 충격적인 이유 #주식 #투자 #재테크 #박시동](https://youtu.be/_FsBnjFaZqo) | 1,038,826 |
| 19 | Troll Aura 69 | 03. IQ·두뇌 퀴즈 | 32,700 | 5.6 | 5,821 | 89 | [Check Your Of IQ 💀  #trollface #edit #troll](https://youtu.be/fntkQjmdow0) | 11,208,469 |
| 20 | WhyNot Science | 06. Math olympiad (영어) | 105,000 | 18.1 | 5,801 | 88 | [Maths Olympiad Question !](https://youtu.be/iUmUyrt8TRk) | 74,448 |
| 21 | History Roots | 07. Mental math (영어) | 40,700 | 8.0 | 5,098 | 382 | [This Mental Math Competition Looks Unreal 🧠😳](https://youtu.be/AvYStKeRUK8) | 5,193,305 |
| 22 | 손가락월드 | 02. 암산 | 83,300 | 16.4 | 5,092 | 421 | [암산 천재들의 숨막히는 대결](https://youtu.be/Fi0zdhkSwrQ) | 42,949 |
| 23 | GPT 연대경영 | 03. IQ·두뇌 퀴즈 | 77,900 | 15.3 | 5,078 | 79 | [클로드로 내 지능 수준 알아내는 법](https://youtu.be/KHAFRkF3NTg) | 247,390 |
| 24 | Toppers Adda  | 05. Math puzzle (영어), 07. Mental math (영어) | 95,600 | 19.2 | 4,974 | 110 | [Maths Magic Trick / दोस्तों को करें हैरान😱/ गणित का जादू 🔥#s](https://youtu.be/g5vAOvfjnMI) | 3,167,308 |
| 25 | 뇌빼영 | 02. 암산 | 46,100 | 11.1 | 4,152 | 157 | [전국 천재들 압도하는 7살 수학 천재](https://youtu.be/OImFr69U84Y) | 5,571,842 |
| 26 | 하루세번지식쌓기 | 08. (기준) 재테크 | 40,500 | 11.7 | 3,473 | 519 | [집에 있으면 꼭 확인해야 할 희귀동전 10개, 500원이 500만원?](https://youtu.be/c_iYrfFjaiI) | 1,644,700 |
| 27 | 퍼터키컨충 | 02. 암산, 07. Mental math (영어) | 34,300 | 10.2 | 3,346 | 139 | [수능 수학 문제 암산](https://youtu.be/81mGnHBcdyA) | 1,726,714 |
| 28 | 나도그림 | 03. IQ·두뇌 퀴즈 | 21,600 | 6.8 | 3,176 | 797 | [천재들만 맞춘다는 구글 IQ 입사 시험 문제;; #그림 #미술 #아트 #유머 #쇼츠 #수학 #아이큐테스트](https://youtu.be/zjLftsNrggQ) | 94,889 |
| 29 | RKSAS TUTORIAL | 05. Math puzzle (영어) | 39,400 | 12.5 | 3,156 | 1,140 | [🤩😎Genius Math Hack🧠😊🔥 #mathpuzzle#mathsshorts](https://youtu.be/B8Ylprj9Pb4) | 5,889,659 |
| 30 | Just Jane | 05. Math puzzle (영어) | 6,500 | 2.2 | 2,953 | 41 | [Can you Solve this case like Patrick Jane?](https://youtu.be/Pk6cM_OYPh0) | 281,241 |

## 5. 분야별 예 (성공 영상 배수 순 · 빨리 큰 새 채널)

### 05. Math puzzle (영어) — 표본 90 · 성공 18 (20%) · 검색어 math puzzle, can you solve this

| 성공 쇼츠 | 채널 | 구독자 | 조회수 | 배수 | 초 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [Can You Solve This Ring & Rubber Band Puzzle ✅🙏 #shorts #lifehacks #vi](https://www.youtube.com/shorts/2iPGFdOdiis) | Craftsman facts | 15,800 | 54,354,379 | 3,440.2 | 5 | 93 | 외국 |
| [Squishy Dumplings Can You Solve This Puzzle?  #shorts #diy](https://www.youtube.com/shorts/z_BqPpqv24s) | Cardboard Lab | 4,690 | 1,860,274 | 396.6 | 26 | 4 | 외국 |
| [No 🖊️ Pen. No 📄 Paper. Just 🧠 Brain! / 9-5+4=?#MathChallenge #MathPuzz](https://www.youtube.com/shorts/5KZc0aB7yqc) | MATHXGROWTH | 3,030 | 657,036 | 216.8 | 7 | 17 | 외국 |
| [🤩😎Genius Math Hack🧠😊🔥 #mathpuzzle#mathsshorts](https://www.youtube.com/shorts/B8Ylprj9Pb4) | RKSAS TUTORIAL | 39,400 | 5,889,659 | 149.5 | 19 | 50 | 외국 |
| [SHIVAM NOOB: Only 1% GENIUS Can Solve This... 😱🧠 (Can You?) 🔥 / PART 1](https://www.youtube.com/shorts/v0PCxt8H5qU) | HITESHIFLY ⚡ | 6,670 | 979,873 | 146.9 | 55 | 29 | 외국 |

빨리 큰 새 채널: Priya L story (구독자 186,000, 7개월, 월 27,220) · INDIAN MANGO  (구독자 138,000, 5개월, 월 25,459) · Myst Editz (구독자 150,000, 10개월, 월 15,271) · Mr Random Talks (구독자 143,000, 10개월, 월 14,133) · Thalis P (구독자 113,000, 8개월, 월 14,097)

### 03. IQ·두뇌 퀴즈 — 표본 40 · 성공 16 (40%) · 검색어 IQ 테스트

| 성공 쇼츠 | 채널 | 구독자 | 조회수 | 배수 | 초 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [IQ Test. #quiz #triviatricks #quizchallenge #mindbendingquiz](https://www.youtube.com/shorts/t7jaju-YYaI) | EnglishQuizeTime | 5,330 | 4,079,186 | 765.3 | 65 | 140 | 외국 |
| [Check Your Of IQ 💀  #trollface #edit #troll](https://www.youtube.com/shorts/fntkQjmdow0) | Troll Aura 69 | 32,700 | 11,208,469 | 342.8 | 22 | 83 | 외국 |
| [IQ 1위 보더콜리, 숨막히는 집중력 테스트 ㄷㄷ](https://www.youtube.com/shorts/C_zeXCBdNZE) | 판다픽 | 8,280 | 2,497,793 | 301.7 | 31 | 121 |  |
| [미달이가 유치원 IQ 1등 찍은 진짜 이유](https://www.youtube.com/shorts/4rbUlibLcnE) | 해피포코 | 1,710 | 275,071 | 160.9 | 179 | 17 | 외국 |
| [IQ Test. #quiz #triviatricks #mindbendingquiz #quizchallenge](https://www.youtube.com/shorts/lVrmjhHjpI4) | EnglishQuizeTime | 5,330 | 436,112 | 81.8 | 65 | 108 | 외국 |

빨리 큰 새 채널: 손승아 SEUNG (구독자 195,000, 7개월, 월 28,955) · 오늘마셋(TODAY MINDSET) (구독자 111,000, 11개월, 월 9,909) · Troll Aura 69 (구독자 32,700, 6개월, 월 5,821) · GPT 연대경영 (구독자 77,900, 15개월, 월 5,078) · 나도그림 (구독자 21,600, 7개월, 월 3,176)

### 02. 암산 — 표본 45 · 성공 15 (33%) · 검색어 암산

| 성공 쇼츠 | 채널 | 구독자 | 조회수 | 배수 | 초 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [눈보다 빠른 손가락으로 완성하는 기적의 암산 능력](https://www.youtube.com/shorts/Pn--FBnaIxM) | 공감멍 | 188 | 1,354,165 | 7,203.0 | 25 | 48 |  |
| [암산 하다가 고장 남 @ootb STUDIO  #이창섭](https://www.youtube.com/shorts/mmZol6heILg) | 웃참쉼터 | 1,710 | 1,020,424 | 596.7 | 13 | 63 |  |
| [이건 암산 잘해도 어려울 듯](https://www.youtube.com/shorts/2NSE8o2Uhw4) | 말랑타임 | 4,180 | 1,040,871 | 249.0 | 17 | 29 |  |
| [전국 천재들 압도하는 7살 수학 천재](https://www.youtube.com/shorts/OImFr69U84Y) | 뇌빼영 | 46,100 | 5,571,842 | 120.9 | 60 | 146 |  |
| [암산 천재라면 이정도는 해야함](https://www.youtube.com/shorts/KfTkfVy23Cs) | 오늘의릴스타 | 16,100 | 1,809,581 | 112.4 | 25 | 56 |  |

빨리 큰 새 채널: 펫파라치 (구독자 81,200, 12개월, 월 6,790) · 손가락월드 (구독자 83,300, 16개월, 월 5,092) · 뇌빼영 (구독자 46,100, 11개월, 월 4,152) · 퍼터키컨충 (구독자 34,300, 10개월, 월 3,346) · 꽃피는인생 - 드라마사연 (구독자 6,460, 2개월, 월 2,850)

### 08. (기준) 재테크 — 표본 41 · 성공 14 (34%) · 검색어 재테크

| 성공 쇼츠 | 채널 | 구독자 | 조회수 | 배수 | 초 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [청년 사회초년생 재테크 티어](https://www.youtube.com/shorts/ZDrVLO2hcwo) | 프쌤 / 프라임로드 | 235 | 370,733 | 1,577.6 | 34 | 11 |  |
| [재테크 강연대상이 신세계 손녀일 때](https://www.youtube.com/shorts/gNNhiknw81s) | 아이돌다이뜌  | 7,500 | 4,920,079 | 656.0 | 21 | 39 |  |
| [포르쉐 자랑하면서 강의파는 20대 사업가, 재테크 유튜버 옌마드 회사에 가봤습니다 #성공팔이 #사업가 #재테크 #유튜버 #옌마](https://www.youtube.com/shorts/fsQ10IF0p7s) | 에디터조 | 896 | 373,614 | 417.0 | 54 | 125 |  |
| [주식 오래 한 사람들이 결국 깨닫는 투자 원칙 10가지 #주식투자 #재테크 #투자원칙](https://www.youtube.com/shorts/HpOLbLM9AOk) | 만복보감 | 2,190 | 885,305 | 404.2 | 12 | 33 |  |
| [대출받아 집짓고 6천짜리 리스차 끄는 무일푼 남친. #jtbc #연애전쟁 #사랑](https://www.youtube.com/shorts/9KX85VWcjEI) | 꿀영 | 6,990 | 1,762,387 | 252.1 | 59 | 25 |  |

빨리 큰 새 채널: ETF 아는 형 (구독자 158,000, 16개월, 월 10,147) · 펜앤경제TV (구독자 121,000, 16개월, 월 7,366) · MOVIESTARWA (구독자 81,300, 12개월, 월 7,091) · 위키타카 (구독자 75,200, 12개월, 월 6,376) · 하루세번지식쌓기 (구독자 40,500, 12개월, 월 3,473)

### 06. Math olympiad (영어) — 표본 29 · 성공 5 (17%) · 검색어 math olympiad

| 성공 쇼츠 | 채널 | 구독자 | 조회수 | 배수 | 초 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [Maths olympiad question // best algebra question // maths algebra // j](https://www.youtube.com/shorts/-SRLSs6chcQ) | KISHAN SIR  | 3,100 | 81,251 | 26.2 | 101 | 144 | 외국 |
| [Trickiest math Olympiad question?!? #maths #matholympiad #mathclass #e](https://www.youtube.com/shorts/XCk1EZDkPFg) | Math Tutor Junhyun Um  | 10,000 | 148,043 | 14.8 | 58 | 60 | 외국 |
| [How to Simplify "Impossible" Nested Surds in Math Olympiads](https://www.youtube.com/shorts/an842ZeRqew) | Marcus Smith | 9,140 | 119,607 | 13.1 | 130 | 139 | 외국 |
| [Maths Olympiad ya JEE ki Taiyari Karte Time Main Yeh Advice Nahi Deta ](https://www.youtube.com/shorts/PHk71uB2Z8c) | Pankaj Joshi Sir Maths (PJ Sir) | 32,700 | 154,522 | 4.7 | 25 | 102 | 외국 |
| [Old Method vs New Trick 🤯 Which one is easier? 👇#Math #MathTricks #Mat](https://www.youtube.com/shorts/ISgmjsGxpUM) | Quickmath shorts | 22,900 | 106,690 | 4.7 | 25 | 11 | 외국 |

빨리 큰 새 채널: Myst Editz (구독자 150,000, 10개월, 월 15,271) · Quickmath shorts (구독자 22,900, 4개월, 월 6,395) · WhyNot Science (구독자 105,000, 18개월, 월 5,801) · Pankaj Joshi Sir Maths (PJ Sir) (구독자 32,700, 22개월, 월 1,481) · Math Tutor Junhyun Um  (구독자 10,000, 8개월, 월 1,194)

### 07. Mental math (영어) — 표본 36 · 성공 9 (25%) · 검색어 mental math

| 성공 쇼츠 | 채널 | 구독자 | 조회수 | 배수 | 초 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [HE SOLVED 100 MATH PROBLEMS IN 1 SECOND 🤯🧠#shorts #youtubeshorts #tren](https://www.youtube.com/shorts/Xo0z48LH-lQ) | 𝕲𝖃090_𝕰𝖉𝖎𝖙 ★ | 18,800 | 23,167,666 | 1,232.3 | 16 | 140 | 외국 |
| [✨ Table of 21 Made Easy / Fast Multiplication Trick for Kids](https://www.youtube.com/shorts/hjMNo8tI5-0) | Ansa Root  | 23,700 | 9,899,504 | 417.7 | 75 | 113 | 외국 |
| [SKILL DEWA TERCEPAT MENGHITUNG DI ANGKRINGAN JOGJA!](https://www.youtube.com/shorts/7BxuGqTDDjo) | Joko Pramono | 3,860 | 1,010,689 | 261.8 | 39 | 5 | 외국 |
| [No 🖊️ Pen. No 📄 Paper. Just 🧠 Brain! / 9-5+4=?#MathChallenge #MathPuzz](https://www.youtube.com/shorts/5KZc0aB7yqc) | MATHXGROWTH | 3,030 | 657,036 | 216.8 | 7 | 17 | 외국 |
| [This Mental Math Competition Looks Unreal 🧠😳](https://www.youtube.com/shorts/AvYStKeRUK8) | History Roots | 40,700 | 5,193,305 | 127.6 | 7 | 90 | 외국 |

빨리 큰 새 채널: Learn With Shakil (구독자 154,000, 8개월, 월 18,383) · Myst Editz (구독자 150,000, 10개월, 월 15,271) · マイブーム【Myboom】 (구독자 110,000, 10개월, 월 11,428) · The Kushwaha Sir (구독자 103,000, 10개월, 월 10,701) · History Roots (구독자 40,700, 8개월, 월 5,098)

### 01. 수학·계산 퀴즈 — 표본 74 · 성공 8 (11%) · 검색어 수학 퀴즈, 계산 퀴즈

| 성공 쇼츠 | 채널 | 구독자 | 조회수 | 배수 | 초 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [7+7+7+7×0=?? #mathchallenge #mathquiz #mathshorts #mathematics](https://www.youtube.com/shorts/qR5AS3Fv-lQ) | Learn with srijan | 1,300 | 1,045,428 | 804.2 | 16 | 34 | 외국 |
| [수학 퀴즈 내다가 나온 찐텐 리액션ㅋㅋㅋ](https://www.youtube.com/shorts/EYb6fE4-fmY) | 무비여라 | 12,700 | 2,075,658 | 163.4 | 19 | 128 |  |
| [Only 10% can solve this!! #mathchallenge #mathshorts #mathquiz #mathem](https://www.youtube.com/shorts/mEtOBoR83Es) | Learn with srijan | 1,300 | 117,228 | 90.2 | 36 | 41 | 외국 |
| [수학 문제 풀다가 갑자기 상대방 숫자를 훔쳐버리는 코미디언들의 황당한 문제 풀이 #shorts #쇼츠 #8outof10cats](https://www.youtube.com/shorts/a4sUzNOP2vU) | 복어극장 | 2,140 | 172,968 | 80.8 | 61 | 79 |  |
| [댓글창 싸움 난 수학 문제 ㅋㅋ](https://www.youtube.com/shorts/P6pdH6X9N7k) | 밈노트 | 1,190 | 65,952 | 55.4 | 6 | 6 |  |

빨리 큰 새 채널: 개짜가족 (구독자 45,700, 18개월, 월 2,511) · 키프레 (구독자 15,600, 6개월, 월 2,448) · 덕질인생🕺 (구독자 45,100, 21개월, 월 2,165) · 루가 (구독자 24,300, 12개월, 월 2,016) · 별별숏 (구독자 19,100, 12개월, 월 1,606)

### 09. (기준) stock market (영어) — 표본 42 · 성공 4 (10%) · 검색어 stock market

| 성공 쇼츠 | 채널 | 구독자 | 조회수 | 배수 | 초 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [Harshad Mehta yahin chook gaya. 🔥  #HarshadMehta #StockMarket #Busines](https://www.youtube.com/shorts/vD5_4E7OFBQ) | Inspire with bashes gala | 1,330 | 971,262 | 730.3 | 43 | 38 | 외국 |
| [Scalper Move 50 Lakh View #trading #cryptotrading#stockmarket #nifty #](https://www.youtube.com/shorts/kKyVB7EC-6s) | Trade STPC | 20,300 | 5,972,810 | 294.2 | 20 | 144 | 외국 |
| [How GTA Players Recreated the 1929 Stock Market Crash](https://www.youtube.com/shorts/G1j4m1hfBT4) | OuterStories  | 4,870 | 1,073,497 | 220.4 | 28 | 5 | 외국 |
| [Ep7: Trading with stranger #nifty #crudeoil #stockmarket #trending #tr](https://www.youtube.com/shorts/YkakLSsVkLg) | The FinLabX | 8,350 | 1,221,836 | 146.3 | 36 | 149 | 외국 |

빨리 큰 새 채널: The FinLabX (구독자 8,350, 5개월, 월 1,589) · OuterStories  (구독자 4,870, 6개월, 월 847) · Inspire with bashes gala (구독자 1,330, 4개월, 월 355)

### 04. 교양 수학 (설명형) — 표본 44 · 성공 4 (9%) · 검색어 수학 이야기

| 성공 쇼츠 | 채널 | 구독자 | 조회수 | 배수 | 초 | 올린 지(일) | 외국 |
|---|---|---|---|---|---|---|---|
| [참된 스승을 만나는 게 중요한 이유 #이상한나라의수학자](https://www.youtube.com/shorts/vdQO9bcVOCc) | 무비한방울 | 16,300 | 835,771 | 51.3 | 59 | 105 |  |
| [수학문제에 대한 팩폭에 답을 우기는 노답 교사 ㄷㄷ #이상한나라의수학자](https://www.youtube.com/shorts/ynyyQKcmAuk) | 무비한방울 | 16,300 | 460,958 | 28.3 | 58 | 106 |  |
| [수학 9등급이 상위 1% 영재학교에 다니면? #이상한나라의수학자](https://www.youtube.com/shorts/uIjLL5XnLwM) | 무비한방울 | 16,300 | 335,000 | 20.6 | 61 | 110 |  |
| [수포자가 수학을 포기하는 이유 #영화 #이상한나라의수학자](https://www.youtube.com/shorts/WZGk67quYII) | 무비한방울 | 16,300 | 182,064 | 11.2 | 54 | 108 |  |

빨리 큰 새 채널: 무비한방울 (구독자 16,300, 13개월, 월 1,253) · 역사의별들[Stars of History] (구독자 6,730, 14개월, 월 467) · 수파민 (구독자 4,380, 14개월, 월 324)

