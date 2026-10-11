# 보이저 1호 영상 대본 소스 (voyager-2026-10)

버전: v1.0 — 2026-10-11 — 최초 작성 (사용자 지시: 주식 밖 주제 오디오 전까지 주제마다 3개)

> 과학 정보 제공용 원고입니다. 사연은 실제 발표와 보도를 바탕으로 재구성한 이야기이며, 사연 속 강사·학생·쇼츠는 가상입니다. 나사·제트추진연구소 기술자를 흉내 내지 않습니다.

## 파일

| 파일 | 내용 |
|---|---|
| `voyager-2026-10.txt` | 대본 v1.0 — **문장 122**. 파트 라벨, `[장면] 과학 정보 제공용 재구성 사연입니다` (문장 24 뒤) |
| `voyager-2026-10.srt` | **문장 122 / 자막 166** (1432px 넘는 44문장은 앞줄·뒷줄), 문장 24 뒤 고지 공백 8.0초, **끝 12:14.0** (추정치, 초당 5.2음절) |
| `titles.md` | 제목 3개 (T1 채택) |
| `thumbnails/thumbnail_1.md` ~ `_3.md` | 썸네일 이미지 AI 프롬프트 3개 (숫자 반전·인물·대비) |
| `upload.md` | 업로드 시트 (설명란·챕터 13개·태그·고정 댓글) |
| `tts_lexicon.tsv` | 읽는 소리 사전 (TTS에만 씀 — 시각·소수·단위 숫자 몇 개) |
| `summary.md` | 요약 문서 (자동 생성, `tools/make_summary.py`) |

검사: `python3 tools/srt_tool.py check space/source/voyager-2026-10/voyager-2026-10.txt space/source/voyager-2026-10/voyager-2026-10.srt --expect 122/166`
→ `문장 122 / 자막 166 (나뉜 문장 44개) / SRT–TXT 일치 ✅ / 고지 공백 문장 24 뒤 8.0초 ✅ / 끝 00:12:13,985` · `✅ 이상 없음`
녹음 후: `video/`에서 `npm run align-audio -- space voyager-2026-10` (오디오는 고치지 않음, 문장 24 뒤 3.5초 이상 쉼)

## 주제를 고른 이유 (`space/guides/data_insights.md`, `title_rules.md` 4-1)

- 분류: 탐사선 근황 (`title_rules.md` 3번). 탐사 카테고리 기회점수 55 (2순위 그룹), 키워드 `보이저호 근황` **60**(롱폼 추천), `보이저1호 위치` 50. 보이저·탐사선 클러스터 31개 중 성공 48.4%.
- 작은 채널이 12~20분 해설 영상으로 반복 성공: 우주과학연구소(5,380명) 18분 134.9배·12.8분 27.1배·17.3분 8.8배, 쉬운과학(6,700명) 20.5분 7.8배 → 이 영상 12분 14초.
- 태그 '보이저1호' 성공 영상 과대표집 1.38배.
- 시청자 댓글: "그 응답신호가 오가는 게 저 거리에서도 가능한 게 더 신기한데"(좋아요 83), "왔다갔다… 거의 2일 아닌가?"(16) → 문제 네 번째(송신기·안테나)와 확인법 넷째(왕복 이틀)에서 답함. '벽을 발견했다' 영상의 "썸네일 낚시 영상 보지 마"(41) → 진행자 문장 22, 문제 다섯 번째.
- 시의성: 2026-11-18 1광일 (나사 계산). 업로드는 그 전이 좋다.
- 같은 주제 다른 영상과 나눈 것: 누리호(발사 성공·실패 읽기, 몇 번 중 몇 번), 소행성(확률·등급 읽기) → 이 영상은 **근황 영상의 진위 확인(단정어·날짜·원문·숫자·정정)**.

## 사연 검산 (재구성 — 실제 발표 날짜·숫자에 맞춤)

| 문장 | 대본 표현 | 값 · 계산 | 근거 |
|---|---|---|---|
| 1 | 2023년 12월, 50년 가까이 날아간 보이저 1호가 끝났다는 1분짜리 쇼츠 | 쇼츠는 **가상**. 고장 시작 2023-11-14의 약 한 달 뒤, 원인 발표(2024-04-04)보다 넉 달 앞. 발사(1977-09-05) → 2023-12 = 46년 3개월 → "50년 가까이" (발사 연도는 대본에 쓰지 않음) | 나사 보이저 블로그, CNN(KTVZ) |
| 2 | 마지막 신호는 아무도 못 읽는다, 외계 신호일지도 | 가상 쇼츠의 말 (실제로는 "같은 패턴이 되풀이되는 알아볼 수 없는 데이터") — 문장 27·33~42에서 바로잡음 | CNN, 나사 |
| 3 | 서른넷 학원 과학 강사, 중학교 2학년 스물네 명 | 2023년 34세 → 2026년 37세. 인원은 예시 | 설정 |
| 7 | 2024년 4월, 다섯 달 만에 살아났다는 기사 | 2023-11-14 → 2024-04-20 상태 정보 복구 = 5개월 6일. 나사 발표(2024-04-22): "for the first time in five months" | 나사 2024-04, The Register |
| 8 | 지금도 신호를 보내며 2026년 11월 18일 빛으로 하루 거리 | 나사: 2026-11-18 오전 2시 16분 07초(미국 태평양 표준시) 160억 9,400만 마일 = 1광일. 160.94억 × 1.609344 = **약 259억 km**. 10:16 UTC = **한국 시간 저녁 7시 16분** (계산, 문장 117) | 나사 위치 페이지, EarthSky, IFLScience |
| 10 | 스물네 명 가운데 여섯 명이 학원을 옮김 | 25%. 예시 | 설정 |
| 11~12 | 칩 하나가 고장, 기술자들이 지구에서 코드를 옮겨 고침 | 비행 데이터 컴퓨터 메모리 칩 하나(메모리 약 3%), 코드를 나눠 다른 자리에 저장. 4월 18일 명령 → 4월 20일 확인 | 나사 2024-04-04·04-22, The Register |
| 88~89 | 쇼츠는 고장 한 달쯤 뒤, 원인을 찾은 2024년 4월보다 넉 달 앞 | 2023-12 → 2024-04 = 4개월 | 위와 같음 |
| 105 | 259억 ÷ 30만 ≈ 8만 6천 초, 꼬박 하루 | 259억 ÷ 30만 = 86,333초(23.98시간). 정확히는 25,901,000,000 ÷ 299,792.458 = 86,396초 ≈ 24시간 (계산) | 나사 위치 페이지 |
| 106~107 | 2024년 4월 신호 편도 22시간 반, 4월 18일 명령 → 4월 20일 확인 | 편도 약 22.5시간 → 왕복 약 45시간 → 18일 명령, 20일 결과 확인과 맞음 (계산) | 나사 2024-04-22 |
| 108 | 11월 18일부터 명령·답 왕복 꼬박 이틀 | 1광일 × 2 = 48시간 (나사 보이저 프로젝트 책임자 수잔 도드: 명령이 닿는 데 하루, 답이 오는 데 하루) | EarthSky |
| 67 | 40년 넘게 쓰지 않던 예비 송신기 | S밴드 송신기 1981년 이후 미사용 → 2024년 = 43년 | CNN 2024-11-01, Smithsonian |
| 70 | 21년 동안 못 쓰던 주 추진기, 2025년 3월 | 2004년 히터 고장으로 멈춤 → 2025-03-20 작동 확인 = 21년 | CNN 2025-05-14 |
| 77~78 | 1세제곱센티미터에 전자 0.08개 → 1센티미터 상자 열두 개에 전자 하나 | 1 ÷ 0.08 = 12.5 → 12개 × 0.08 = 0.96 ≈ 1개 (계산) | 나사 2013-09, Science News |

- **1광일 날짜가 보도마다 다르다:** 2025년 보도는 11월 13일(Gigazine — IFLScience 초기 보도 인용)·15일(PopSci), 일부 국내 보도도 13~15일. 나사가 2026-06-17 계산해 발표한 **11월 18일**로 통일했다 (문장 8·91~92). EarthSky는 시각을 "12:16 a.m. CST"로 적었는데 나사 페이지의 "2:16 a.m. PST"와 맞지 않아 나사 값을 썼다.

## 숫자와 출처 (확인 방법: 2026-10-11 웹 검색 결과로 확인 — 이 환경은 원문 페이지를 열지 못함)

| 문장 | 대본 표현 | 원문 인용 (검색 결과) | 출처 · 자료 연도 |
|---|---|---|---|
| 20~22 | 최근 1년 사이 보이저 영상 제목에 우주 미아·소름·벽을 발견했다·종료하기로 했다, 댓글 "썸네일 낚시 영상 보지 마" | 분석 대상(2025-10-11~2026-09-26) 보이저 영상 제목 31개 중 "50년째 우주 미아? … 소름돋는 근황"(2026-05), "… 태양계 끝에서 벽을 발견했다"(2026-07), "NASA가 보이저 1호를 종료하기로 한 이유"(2026-08). 댓글 좋아요 41 | `space/result/data/videos.csv`, `audience_comments.csv` (채널·영상 이름은 대본에 쓰지 않음) |
| 26~27 | 2023년 11월 14일부터 알아볼 수 없는 신호, 같은 패턴 반복 | "ceased sending readable science and engineering data back to Earth on November 14, 2023"; "an indecipherable repeating pattern of code" | [CNN(KTVZ) 2024-06-18](https://ktvz.com/cnn-other/2024/06/18/voyager-1-sends-back-science-data-from-more-than-15-billion-miles-away-after-nasa-fix/) · 2023~2024 |
| 28, 83 | 12월, 나사: 명령은 받아 실행 중 | "The spacecraft is receiving and executing commands sent from Earth; however, the FDS is not communicating properly with … the telemetry modulation unit" | [나사 보이저 블로그 목록](https://science.nasa.gov/blogs/voyager/page/2) (2023-12 글) · 2023 |
| 30 | 2024년 4월 20일, 다섯 달 만에 상태 정보 | "received the first coherent data about the health and status of Voyager 1's engineering systems on April 20"; "for the first time in five months" | [나사 2024-04](https://blogs.nasa.gov/voyager/2024/04), [astrobiology.com 2024-04-22](https://astrobiology.com/2024/04/22/voyager-1-interstellar-probe-resumes-sending-engineering-updates-to-earth/) · 2024 |
| 31 | 6월, 과학 장비 네 개 자료 모두 | "returns data from all 4 instruments" (나사 2024-06-13 발표) | [Space.com](https://www.space.com/voyager-1-fully-operational), [Scientific American](https://www.scientificamerican.com/article/voyager-1-is-back-nasa-spacecraft-safely-resumes-all-science-observations) · 2024 |
| 34~35 | 컴퓨터 세 대 중 하나, 자료를 묶어 보내는 비행 데이터 컴퓨터 | "the flight data subsystem (FDS), one of the spacecraft's three onboard computers, which packages science and engineering data before transmission" | [The Register 2024-04-23](https://www.theregister.com/2024/04/23/voyager_1_engineering_updates/) · 2024 |
| 36~38 | 3월 1일 메모리 통째로 보내라는 명령, 이틀 뒤 신호, 4월 초 원인: 메모리 약 3%, 칩 하나 | "poke" 명령 3월 1일, 새 신호 3월 3일, 심우주통신망 기술자가 해독 → "about 3% of the FDS memory has been corrupted", "a single chip responsible for storing a portion of the affected memory" | [나사 블로그 2024-03-15](https://science.nasa.gov/blogs/voyager/2024/03/15/nasa-engineers-make-progress-toward-understanding-voyager-1-issue), [나사 블로그 2024-04-04](https://science.nasa.gov/blogs/voyager/2024/04/04/engineers-pinpoint-cause-of-voyager-1-issue-are-working-on-solution/), [EarthSky](https://earthsky.org/space/voyager-1-message-decipher-progress/) · 2024 |
| 39 | 강한 우주 입자 또는 낡음, 확실히 알 수 없음 | "an energetic particle from space, or wear after 46 years" — 확실히 알 수 없다 | 나사 블로그 2024-04-04 · 2024 |
| 40~41 | 칩을 갈 수 없어 코드를 나눠 다른 자리에 | "No spare location could hold the lost code whole, so the team divided the affected code into sections and stored those sections in different places in the FDS" | The Register 2024-04-23 · 2024 |
| 44~45 | 플루토늄 원자력 전지, 해마다 약 4와트 감소 | "both lose about 4 watts of power each year"; "radioisotope generator, which turns heat from decaying plutonium into electricity" | [제트추진연구소 2025-03-05](https://www.jpl.nasa.gov/news/nasa-turns-off-two-voyager-science-instruments-to-extend-mission/) · 2025 |
| 47~49 | 2025-02-25 우주 방사선 측정 장비 끔, 책임자: 지금 안 끄면 몇 달 뒤 임무 종료 선언 | "turned off Voyager 1's cosmic ray subsystem on February 25"; 수잔 도드(보이저 프로젝트 책임자): "If we don't turn off an instrument on each Voyager now, they would probably have only a few more months of power before we would need to declare end of mission." | 제트추진연구소 2025-03-05, [Scientific American](https://www.scientificamerican.com/article/nasas-voyager-probes-lose-one-instrument-each-as-power-wanes/) · 2025 |
| 50~53 | 2026-02-27 방향 돌리는 작업 중 전력 하락, 전압 보호 기능, 4월 17일 저에너지 입자 장비 끔, 약 1년 여유, 남은 장비 플라스마 파동·자기장 2개 | "a drop on February 27, 2026, during a planned roll maneuver"; "undervoltage fault protection"; "commands to switch off the Low-energy Charged Particles"; "about a year of breathing room"; 남은 장비 "one for plasma waves and one for magnetic fields" | [제트추진연구소 2026-04](https://www.jpl.nasa.gov/news/nasa-shuts-off-instrument-on-voyager-1-to-keep-spacecraft-operating/), [나사 블로그 2026-04-17](https://science.nasa.gov/blogs/voyager/2026/04/17/nasa-shuts-off-instrument-on-voyager-1-to-keep-spacecraft-operating/), [Universe Today](https://www.universetoday.com/articles/another-instrument-shut-down-on-voyager-1-to-extend-its-interstellar-mission) · 2026 |
| 56 | 2025년 프로젝트 과학자: 매일이 마지막일 수 있다 | 린다 스필커(보이저 프로젝트 과학자) "every day could be our last" | [The Debrief 2025-03](https://thedebrief.org/every-day-could-be-our-last-voyager-instruments-shut-down-as-iconic-spacecraft-continue-farthest-ever-journey-from-earth/) · 2025 |
| 58~61 | 2026년 8월 발표: 보이저 2호 히터 등 한꺼번에 끄고 저전력 장치로, 장비 세 개 적어도 1년 더, 보이저 1호에도 계획 | 'Big Bang': 히터 2개와 열을 내려고 켜 둔 기록 장치를 끄고 전기를 덜 쓰는 장치를 켬, 연료관이 얼지 않게. "keep Voyager 2's three surviving science instruments operating for at least one additional year"; "JPL engineers also plan to perform the same operation on Voyager 1" | [나사 블로그 2026-08-04](https://science.nasa.gov/blogs/voyager/2026/08/04/nasa-engineers-help-prolong-voyager-2s-science-mission/), [Space.com](https://space.com/space-exploration/voyager/nasa-figured-out-how-to-keep-its-48-year-old-voyager-2-probe-running-for-yet-another-year) · 2026 |
| 63 | 송신기 약 23와트, 냉장고 전구 | "about 23 watts, the power of a refrigerator light bulb" (제트추진연구소 글. 보도마다 20~23와트) | [제트추진연구소 보이저 글](https://voyager.jpl.nasa.gov/news/details.php?article_id=50) · 2010년대 (탐사선 사양이라 사례가 아님) |
| 64~65 | 미국·스페인·호주 지름 70m 안테나, 지구가 돌아도 한 곳은 보이게 | 심우주통신망 골드스톤·마드리드·캔버라, "located 120 degrees apart around the world to ensure continuous communication despite Earth's rotation", 70m 안테나 | [제트추진연구소 심우주통신망](https://jpl.nasa.gov/deep-space-network-now), [행성협회](https://planetary.org/space-images/deep-space-network) · 현행 |
| 66~69 | 2024년 10월 히터 명령 뒤 보호 기능으로 주 송신기 꺼짐, 40년 넘게 안 쓰던 예비 송신기, 며칠 만에 연락, 11월 복구 | "the X-band transmitter had been shut off by the spacecraft's fault protection system when engineers activated a heater"; S밴드 1981년 이후 미사용; 10월 22일 확인·24일 재연결; 11월 중순 X밴드·과학 자료 재개 | [CNN 2024-11-01](https://edition.cnn.com/2024/11/01/science/voyager-1-transmitter-issue/index.html), [Smithsonian](https://www.smithsonianmag.com/smart-news/voyager-1-breaks-its-silence-with-nasa-via-a-radio-transmitter-not-used-since-1981-180985399/) · 2024 |
| 70 | 21년 못 쓰던 방향 조절용 주 추진기, 2025년 3월 | 주 방향(롤) 추진기 2004년부터 미사용 → 3월 20일 작동 확인 (2025-05-14 발표) | [CNN 2025-05-14](https://edition.cnn.com/2025/05/14/science/voyager-1-thruster-fix), [IFLScience](https://iflscience.com/after-21-years-voyager-1-fires-its-thrusters-again-thanks-to-long-distance-servicing-79235) · 2025 |
| 73~75 | 2012년 8월 25일 태양풍이 끝나는 경계, 이듬해 9월 나사 발표 | 2013-09 나사 발표 (Gurnett 외, Science): 헬리오포즈 통과 2012-08-25 | [제트추진연구소 2013](https://www.jpl.nasa.gov/news/nasa-spacecraft-embarks-on-historic-journey-into-interstellar-space/), [Science News](https://www.sciencenews.org/article/last-voyager-1-slips-interstellar-space) · 2013 (2010년대 — 2020년대 대체 자료 없음, 아래 메모) |
| 76 | 경계 근처 입자는 아주 뜨겁지만 너무 드물어 탐사선을 데우지 못함 | "wall of fire isn't a literal barrier"; "incredibly sparse … little chance of heat transferring to the spacecraft" | [IFLScience](https://iflscience.com/nasas-voyager-spacecraft-found-a-30000-50000-kelvin-wall-at-the-edge-of-our-solar-system-81411), [BGR](https://bgr.com/1984386/nasa-voyager-1-discovery-wall-of-fire/) · 2025 보도 |
| 77 | 2013년 전자 1세제곱센티미터에 0.08개 | "an electron density of about 0.08 per cubic centimeter" (2013-04-09~05-22 측정) | Science News, [AAAS](https://www.aaas.org/news/science-voyager-1-now-probing-unexplored-region-space) · 2013 |
| 84 | 임무 종료는 공식 선언 | 위 도드 인용 "declare end of mission" | 제트추진연구소 2025-03-05 |
| 91~92 | 기사마다 11월 13일·15일, 나사 2026년 6월 계산 11월 18일 | "NASA said on June 17, 2026, that Voyager 1 will reach 1 light-day"; 이전 예상: 11월 15일(PopSci), 11월 13일(Gigazine) | [EarthSky](https://earthsky.org/space/voyager-1-1-light-day-from-earth-november-17-18-2026/), [IFLScience](https://iflscience.com/its-official-voyager-1-will-cross-the-1-light-day-threshold-on-november-18-2026-82733), [PopSci](https://popsci.com/science/voyager-one-light-day-earth), [Gigazine 2025-11-13](https://gigazine.net/gsc_news/en/20251113-voyager-light-day-away-from-earth) · 2025~2026 |
| 95~96 | 나사 보이저 블로그, 2026-04-17 글 제목 | "NASA Shuts Off Instrument on Voyager 1 to Keep Spacecraft Operating" | 나사 블로그 2026-04-17 |
| 104, 117 | 11월 18일 약 259억 km, 한국 시간 저녁 7시 16분쯤 | "On Wednesday, Nov. 18, 2026, at 2:16:07 a.m. PST, NASA's Voyager 1 spacecraft will be 16.094 billion miles away, which is one light-day" | [나사 위치 페이지](https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/) · 2026 |
| 106 | 2024년 4월 편도 22시간 반 | "radio signals take about 22.5 hours each way" | 나사 2024-04-22, The Register · 2024 |
| 108 | 11월 18일부터 왕복 이틀 | 도드: 명령이 닿는 데 하루, 답이 오는 데 하루 → 왕복 약 48시간 | EarthSky · 2026 |

### 쓰지 않은 것 (확인 못 했거나 근거가 약함)
- 저에너지 입자 장비를 끄면서 회전 모터(0.5와트)는 켜 둔다는 숫자 (기획서) — 검색 결과에서 확인하지 못함
- 2026년 7월 거리 약 255억 km·왕복 약 47시간 (기획서의 KeepTrack) — 공식 기관 자료로 확인하지 못해 쓰지 않음. 대신 나사의 1광일 값과 2024년 4월 편도 22.5시간을 씀
- 보이저 1호 'Big Bang' 결과 — 2026-10-11 검색에서 찾지 못함 → "같은 방법을 보이저 1호에도 쓸 계획"(2026-08 발표 기준)까지만 씀
- 2030년대 중반까지 임무 전망(뉴닉) — 나사 원문 확인 못 함. 2025년 보도(Scientific American·The Register)에 "2030년대까지 장비 하나라도"가 있으나 대본에는 넣지 않음
- '불의 벽'의 온도 3만~5만 켈빈 — 보도마다 측정 출처가 달라(2025 보도, 원 논문 미확인) 숫자는 쓰지 않고 "아주 뜨겁지만 드물다"만 씀
- 수신 전력(10의 −18제곱 와트 등) — 보도마다 달라 쓰지 않음
- "사람이 만든 물체로 처음 1광일" — 2차 보도라 쓰지 않음
- 발사(1977)·행성 사진·골든 레코드 등 1900년대 사건 — 쓰지 않음 ("50년 가까이" 한 번, "40년 넘게 쓰지 않던" 한 번만)

### 2010년대 자료를 쓴 이유
- 문제 다섯 번째 '벽을 발견했다'는 2026년에도 영상 제목에 나온 말(분석 데이터)이라 바로잡아야 한다. 그 '벽'(헬리오포즈) 통과 자체가 2012년 사건이고 2020년대에 같은 내용의 새 측정이 없어서, 나사 2013 발표(2010년대)를 짧게 썼다. 기획서에 "미확인 — 확인되면 짧게"로 적힌 후보이며 이번에 확인했다.

## 지시사항 적용 메모
- 사연 7비트: ① 2023년 12월 '끝났다' 쇼츠(문장 1~2) ② 서른넷 학원 과학 강사, 지루해하던 중2 스물네 명에게 그대로 전함(3~4) ③ 반응 최고·수강 문의(5) ④ "과학이 아니라 낚시 제목"(6) ⑤ 2024년 4월 다섯 달 만에 복구 기사(7, **0:40**) + 지금도 신호·빛으로 하루(8, **0:47~0:55**) + 단톡방·여섯 명 이동(9~10) ⑥ 칩 하나·지구에서 고침(11~12) ⑦ 한탄 2문장(13~14)
- 제목이 약속한 장면(다섯 달 만에 복구, 빛으로 하루 거리)이 모두 1분 안.
- 문제(오해) 5개 / 확인법 5개. 확인법마다 사연 숫자(2023년 12월 쇼츠, 넉 달, 4월 18일 → 20일, 스물네 명, 11월 18일 저녁 7시 16분)로 예시.
- 경력 시청자 반론 "어차피 곧 꺼진다"(`script_rules.md` 6번) → 문장 54~61: 인정("맞습니다") → 끝났다와 아껴 쓰는 중은 다르다 → 2026년 8월 보이저 2호 사례.
- 실존 인물은 3인칭 역할로만(보이저 프로젝트 책임자·프로젝트 과학자). 대본에는 이름을 넣지 않음 (TTS 발음, 사실 확인 범위).
- 50자 넘는 문장 없음. 1432px 넘는 44문장은 자막 앞줄·뒷줄 (쉼표로 나뉠 자리를 정함).
- 목표 분량 12~14분 → 12분 14초. 억지로 늘리지 않았다 (문제 5·확인법 5, 항목마다 5~19문장).

## 기획서와 달라진 점
- **T1 제목:** "빛으로 하루 거리에서 아직 신호가 옵니다" → "아직 살아서 빛으로 하루 거리에 닿습니다" (11월 18일 전 업로드 때 앞서 나간 말이 되지 않게). T2는 61자 → 58자("제목에 속은"), T3은 훅이 T1과 같아 장면 훅으로 바꿈.
- **사연 순서:** "빛으로 하루 거리"를 ⑥에서 ⑤(문장 8)로 앞당김 — 제목 장면이 1분 안에 나오도록. 사연자가 지금(2026년) 말하는 시점이라 "지금도"로 씀.
- **문제 분석:** 기획서 4개 + 선택 1개 → 5개 모두 씀. 네 번째에 2024년 10월 예비 송신기·2025년 추진기 복구를 더함 (2020년대 사례, '연락 끊김 = 끝' 오해와 바로 이어짐).
- **숫자:** 7월 255억 km(KeepTrack)·0.5와트 모터는 확인 못 해 뺌. 송신기는 기획서 22~23와트 → 제트추진연구소 글의 약 23와트.

## used_content 추가분

`space/source/used_content.md` "영상별 사용 내용"에 아래 줄을 옮긴다.

### 2. 보이저 1호 — `voyager-2026-10` (v1.0)
원본: `space/source/voyager-2026-10/voyager-2026-10.txt`, `.srt` (문장 122 / 자막 166, 12분 14초)
제목: 보이저 1호는 끝났다고 가르쳤는데 아직 살아서 빛으로 하루 거리에 닿습니다. 낚시 영상 믿은 사람들의 공통점

| 구분 | 쓴 내용 |
|---|---|
| 사연 소재·사건 | 가상 쇼츠 "보이저 1호가 끝났다·마지막 신호는 아무도 못 읽는다·외계 신호일지도"(2023-12)를 학원 과학 강사가 중2 반에 그대로 가르침 → 2024-04 학생이 내민 "다섯 달 만에 복구" 기사 → 학부모 단톡방 → 학생 이동 |
| 사연 인물·숫자 | 서른넷(2023) 여성 학원 과학 강사, 중학교 2학년 스물네 명, 여섯 명이 학원을 옮김. 돈 없음 |
| 사연 문장 | "하지만 제가 가르친 건 과학이 아니라 낚시 제목이었어요" / "확인도 안 했는데 반응은 최고였고, 재미있는 선생님이라는 소문에 수강 문의도 늘었죠" / 한탄: "확인 한 번 안 한 1분짜리 영상이, 아이들 스물네 명의 과학 시간을 틀리게 만들었어요", "제가 선생님이라고 불릴 자격이 있었나 싶어요" |
| 진행자 연결 | "보이저 1호처럼 오래된 탐사선 소식을 들으면 많은 분들이 이런 생각을 하죠" / "날짜와 숫자로 하나씩 짚어 보겠습니다" / "그렇다면 다음에 보이저 소식을 볼 때는 무엇을 확인하면 될까요?" |
| 혼잣말 | 그렇게 오래됐으면 고장 나는 게 당연하지 / 그렇게 먼 데서 고장 난 걸 어떻게 고쳐 / 이상한 신호가 왔다면 뭔가 있는 거 아냐? |
| 사례 | 보이저 1호 고장·복구(2023-11-14 → 2024-03-01 메모리 읽기 명령 → 2024-04-04 원인 → 04-18 명령 → 04-20 상태 정보 → 06 과학 장비 4개) / 2024-10 예비 송신기(40년 넘게 미사용) 전환·11월 복구 / 2025-03 주 추진기 21년 만에 복구 / 2025-02-25 우주 방사선 측정 장비 끔 / 2026-02-27 전력 하락 → 04-17 저에너지 입자 장비 끔(약 1년 여유, 남은 장비 2개) / 2026-08 보이저 2호 히터 교체(장비 3개 1년 더) / 2012-08-25 헬리오포즈 통과(2013-09 발표) / 분석 데이터의 보이저 영상 제목 단정어(우주 미아·소름·벽을 발견했다·종료하기로 했다)와 "썸네일 낚시" 댓글 |
| 연구·통계 | 메모리 약 3%·칩 하나 / 전력 해마다 약 4와트 감소 / 송신기 약 23와트(냉장고 전구) / 지름 70m 안테나 3곳(미국·스페인·호주, 지구 자전에도 늘 한 곳) / 전자 밀도 1세제곱센티미터에 0.08개(2013) / 2024-04 편도 22.5시간 / 1광일 2026-11-18 약 259억 km(나사 2026-06 계산, 보도마다 13·15·18일) |
| 인용 | 보이저 프로젝트 책임자(2025): "지금 장비를 끄지 않으면 몇 달 뒤 임무 종료를 선언해야 할 수도" / 프로젝트 과학자(2025): "매일이 마지막일 수 있다" (대본엔 이름 없이 역할만) |
| 계산·개념 | "끝났다와 아껴 쓰는 중은 다르다" / "멈춘 게 아니라 말을 알아들을 수 없게 된 상태" / 거리 ÷ 빛의 속도 = 신호 시간(259억 ÷ 30만 ≈ 8만 6천 초 = 하루), 4월 18일 명령 → 20일 확인, 11월 18일부터 왕복 이틀 / 1센티미터 상자 열두 개에 전자 하나(비유) / 한국 시간 11월 18일 저녁 7시 16분쯤 |
| 올바른 방법 | 근황 영상 확인법: 제목의 단정하는 말 의심(나사는 임무 종료를 공식 선언) / 영상 날짜와 사건 날짜 맞추기(쇼츠는 원인 발표 넉 달 전, 1광일 날짜 13·15 → 18일) / 원문 찾기(나사 보이저 블로그, 번역기로 제목·첫 문단) / 숫자로 대조하기 / 틀렸으면 같은 자리에서 고치기(스물네 명 앞, 칠판 한 줄 "2024년 4월 20일, 나사, 다섯 달 만에 상태 정보 복구", 단톡방에 원문 링크, 11월 18일 함께 기다리기) |
| 마무리 당부 | "끝났다는 제목을 보면, 공유하기 전에 나사의 원문부터 찾아보세요" |

비슷한 유형이라 다음에 피할 것: 학원 강사·교사 사연자 / "쇼츠를 그대로 남에게 전한" 사연 / 확인법 '단정어·날짜·원문·숫자·정정' 묶음 / 신호 시간 계산(거리 ÷ 빛의 속도)

## 근거 자료 은행 추가분

`space/guides/script_rules.md` 9번 표: 기존 보이저 4줄의 "사용한 영상"을 `voyager-2026-10`으로 바꾸고, 아래 줄을 더한다.

| 주제 | 내용 | 출처 | 사용한 영상 |
|---|---|---|---|
| 보이저 1호 고장·복구(2023~2024) — 세부 | 2023-12 나사: 명령은 받아 실행 중(비행 데이터 컴퓨터와 송신 장치 사이 문제) / 2024-03-01 메모리 읽기 명령 → 03-03 새 신호 / 2024-04-04 메모리 약 3% 손상·칩 하나(원인: 고에너지 입자 또는 낡음, 확실하지 않음) / 코드를 나눠 여러 자리에 저장 / 편도 약 22.5시간 / "다섯 달 만에" | [나사 블로그 2024-03-15](https://science.nasa.gov/blogs/voyager/2024/03/15/nasa-engineers-make-progress-toward-understanding-voyager-1-issue), [나사 블로그 2024-04-04](https://science.nasa.gov/blogs/voyager/2024/04/04/engineers-pinpoint-cause-of-voyager-1-issue-are-working-on-solution/), [나사 2024-04](https://blogs.nasa.gov/voyager/2024/04), [Space.com 2024-06](https://www.space.com/voyager-1-fully-operational) | `voyager-2026-10` |
| 보이저 1호 송신기 전환(2024) | 2024-10 히터 명령 뒤 보호 기능으로 X밴드 송신기 꺼짐 → 1981년 이후 안 쓰던 S밴드로 신호 → 10-22 확인·10-24 재연결 → 11월 중순 X밴드·과학 자료 재개 | [CNN 2024-11-01](https://edition.cnn.com/2024/11/01/science/voyager-1-transmitter-issue/index.html), [Smithsonian](https://www.smithsonianmag.com/smart-news/voyager-1-breaks-its-silence-with-nasa-via-a-radio-transmitter-not-used-since-1981-180985399/) | `voyager-2026-10` |
| 보이저 1호 주 추진기 복구(2025) | 2004년 히터 전원 문제로 멈춘 주 방향(롤) 추진기를 2025-03-20 되살림(2025-05-14 발표). 예비 추진기 연료관 막힘 우려, 캔버라 70m 안테나 정비(2025-05~2026-02) 전 | [CNN 2025-05-14](https://edition.cnn.com/2025/05/14/science/voyager-1-thruster-fix), [IFLScience](https://iflscience.com/after-21-years-voyager-1-fires-its-thrusters-again-thanks-to-long-distance-servicing-79235) | `voyager-2026-10` |
| 보이저 2호 'Big Bang' 전력 절약(2026) | 2026-08-04 나사: 히터 2개·열용 기록 장치를 끄고 저전력 장치를 켬 → 남은 과학 장비 3개 적어도 1년 더(안 하면 2026년 안에 하나 꺼야 했음). 보이저 1호에도 계획 | [나사 블로그 2026-08-04](https://science.nasa.gov/blogs/voyager/2026/08/04/nasa-engineers-help-prolong-voyager-2s-science-mission/), [Space.com](https://space.com/space-exploration/voyager/nasa-figured-out-how-to-keep-its-48-year-old-voyager-2-probe-running-for-yet-another-year) | `voyager-2026-10` |
| 보이저 인용(2025) | 수잔 도드(프로젝트 책임자): 지금 장비를 안 끄면 몇 달 뒤 임무 종료 선언 / 린다 스필커(프로젝트 과학자): "매일이 마지막일 수 있다" | [제트추진연구소 2025-03-05](https://www.jpl.nasa.gov/news/nasa-turns-off-two-voyager-science-instruments-to-extend-mission/), [The Debrief](https://thedebrief.org/every-day-could-be-our-last-voyager-instruments-shut-down-as-iconic-spacecraft-continue-farthest-ever-journey-from-earth/) | `voyager-2026-10` |
| 심우주통신망·송신기 | 송신기 약 23와트(냉장고 전구, 보도마다 20~23와트) / 골드스톤·마드리드·캔버라 120도 간격, 70m 안테나 | [제트추진연구소 보이저 글](https://voyager.jpl.nasa.gov/news/details.php?article_id=50), [제트추진연구소 심우주통신망](https://jpl.nasa.gov/deep-space-network-now) | `voyager-2026-10` |
| 헬리오포즈·'불의 벽'(2012~2013, 2025 보도) | 2012-08-25 통과(2013-09 나사 발표, Gurnett 외 Science), 2013-04~05 전자 밀도 약 0.08개/cm³. 2025년 '불의 벽' 보도: 벽이 아니라 경계, 아주 뜨겁지만 희박해 탐사선을 데우지 못함 (온도 3만~5만 K는 원 논문 미확인) | [제트추진연구소 2013](https://www.jpl.nasa.gov/news/nasa-spacecraft-embarks-on-historic-journey-into-interstellar-space/), [Science News](https://www.sciencenews.org/article/last-voyager-1-slips-interstellar-space), [IFLScience](https://iflscience.com/nasas-voyager-spacecraft-found-a-30000-50000-kelvin-wall-at-the-edge-of-our-solar-system-81411) | `voyager-2026-10` |
| 보이저 1호 1광일 — 정정 | 나사 위치 페이지: 2026-11-18 2:16:07 a.m. PST(10:16 UTC = 한국 19:16), 160억 9,400만 마일. EarthSky의 "12:16 a.m. CST"는 시간대 표기 오류로 보임. 이전 예상 11월 13일(Gigazine 2025-11)·15일(PopSci). 1광일 왕복 약 48시간(도드) | [나사 위치 페이지](https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/), [EarthSky](https://earthsky.org/space/voyager-1-1-light-day-from-earth-november-17-18-2026/), [PopSci](https://popsci.com/science/voyager-one-light-day-earth) | `voyager-2026-10` |

## 변경 이력

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-10-11 | 최초 작성 (대본·SRT·제목 3개·썸네일 프롬프트 3개·업로드 시트·읽는 소리 사전) |
