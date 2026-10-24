# 쇼츠 분석 — 음악 (`music`)

만든 시각 2026-10-24T07:43:50+00:00 UTC · `shorts_analysis.py v1.2.1` · 규칙 `music/analysis_rules.toml` v1.5

> **AI 가 쇼츠 지시사항을 만들 재료** — 숫자와 원문만 있고 해석·규칙은 없다. 0번 '한계'를 먼저 읽고, 표본이 작은 차이·대본 없는 사례로 규칙을 만들지 않는다.
> 롱폼 분석은 `../analysis.md` (같은 시청자 — 롱폼 댓글 요청은 거기 8-1). ※ 연구·교육용 — 투자 권유가 아님.

## 0. 자료와 한계

- 받은 쇼츠(사례 폴더 `S_<영상ID>`) 191개 · 쇼츠 탐색에서 본 영상 5,974개 (그중 쇼츠 5,128) · 쇼츠 검색 57개 · 채널 쇼츠 목록 110곳
- 비교 집단 701개 (성공 69, 9.8%) — 채널당 최근 5개 (잘린 2604)
- 글 출처 (받은 쇼츠 전부): 설명 163 · 없음 28 · 표지: oar2.jpg 163 · hqdefault.jpg 28

- 대본(자막·음성인식)이 없는 성공 쇼츠 108개 (#1, #2, #3, #4, #5, #6, #7, #8, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26, #27, #28, #29, #30 …) — 첫 3초·말 속도·끝 문장은 대본이 있는 쇼츠로만 셌다 (음성인식은 쇼츠부터 — 끝나면 다시 셈). '말 없음'은 음성인식 결과가 없는 쇼츠(음악·화면 글자만)
- 비교 집단 701개 = 쇼츠 검색(조회수 순 — 잘된 쇼츠 쪽으로 치우침)·채널 쇼츠 목록 387개 (치우침 없음) 에서 올린 지 3~180일·구독자 50,000 이하, 성공 비율 10% — 실제 시장 비율이 아니다. '있음/없음' 차이로만 보고, '무엇이 먹혔나'는 1-2번(같은 채널 안)을 먼저 보라
- 쇼츠인데 성공·비교에서 뺀 것: 주제 밖 958개, 뺀 주제 79개, 조회수 부풀림 의심 77개, 음악 아님 — 연예 73개, 음악 아님 — 공식 음원 자동 채널  46개, 라이브 방송 40개, 음악 아님 — 밈·코미디 26개, 음악 아님 — 명상 기법·호흡법 13개, 음악 아님 — 영화·드라마 장면 편집 9개, 음악 아님 — 그 밖 9개, 음악 아님 — 강좌·악기 손질·장비 8개, 음악 아님 — 공부 동기부여 3개, 음악 아님 — 이야기 3개, 음악 아님 — 경전 낭송 2개 — 조회수 부풀림·광고 의심 77개의 길이 중앙값 16초·조회수 중앙값 536,307회. 조회수는 많은데 좋아요가 거의 없음 = 광고로 조회수를 샀거나 아주 짧은 쇼츠가 반복 재생됨 (어느 쪽인지 API 로는 모름 — 5-2번에 따로). 조회수 순 검색 위쪽을 덮는다 (2026-10-15 '연금' 검색: 6초짜리 7개)
- 쇼츠 판별: 3분 이하 + 세로·정사각(화면비 = API embed 크기) — 쇼츠가 아니라서 뺀 것: 3분 넘음 389개, 가로 영상 232개, 길이 모름 225개. 화면비를 모르는 예전 캐시는 '#shorts' 표시·60초 이하로 추정
- 외국 영상을 넣음 (주제 설정 INCLUDE_FOREIGN = true) — 성공 쇼츠 중 외국 쇼츠 71개 (#1, #2, #3, #4, #5, #7, #8, #11, #13, #15, #16, #17, #18, #19, #20, #21, #23, #25, #26, #27, #28, #30, #31, #32, #33, #34, #35, #36, #37, #38). 첫 3초 음절·말 속도(한글 음절)는 한국어 쇼츠만으로 셌고, 제목·댓글 낱말 규칙은 한국어 기준이라 외국 쇼츠에는 거의 걸리지 않는다
- 같은 채널 기준선: 성공 쇼츠 101/108개만 '채널 평소 쇼츠 대비'가 있음 (채널 쇼츠가 5개 넘게 있어야 셈)
- 쇼츠 수요·공급의 '시장'은 쇼츠 검색(조회수 순)에서 본 최근 90일 쇼츠 434개 — 조회수 적은 쇼츠가 덜 잡힌다. 주제 묶음 사이의 상대 비교(지수)로만 보라. 검색어별 '결과 수'는 4분 미만 전체(가로 영상 포함) 추정이다
- 말 비교(6·7번)는 대본이 있는 성공 쇼츠 0개 · 나머지 0개로 셌다 — 표본이 작다
- 쇼츠 조회수는 2025-03-31 부터 '재생·다시 재생 횟수'(시청 시간 하한 없음)다 — 그 전 쇼츠와 숫자를 바로 비교하지 말 것. 쇼츠의 핵심 신호(피드에서 '본 비율 vs 넘긴 비율'·평균 시청 비율·다시 재생)는 YouTube API 로 볼 수 없다 — 대신 조회수·배수·같은 채널 대비·참여율(좋아요·댓글 ÷ 조회수)·대본의 첫 3초·끝 문장을 본다
- 형식·첫 줄·끝 줄 유형·댓글 갈래는 낱말 규칙이라 거칠다 (한 쇼츠가 여러 유형에 들 수 있음). 자동 자막은 문장 부호가 없어 '줄' = 자막 조각. 원문을 함께 보라
- 화면 글자(자막 띠·제목 카드)·음악·편집 속도는 영상을 받지 않으므로 셀 수 없다 — 표지 그림(thumbs_NN.jpg)과 대본으로만 가늠한다
- '눈에 띔'은 차이가 크고 표본이 충분하다는 표시일 뿐 원인이 아니다

## 1. 성공 쇼츠 108개

기준: 받은 쇼츠 중 올린 지 3~180일 · 구독자 50,000 이하 · 조회수 50,000 이상 · 조회수 ≥ 구독자 × 3.0 · 180초 이하 세로·정사각 · 채널당 2개 (배수 큰 순). 통과 174 − 뺀 것 35 − 채널당 제한 31

| # | 제목 | 채널 | 구독자 | 조회수 | 배수 | 채널 평소 쇼츠 대비 | 하루 조회수 | 길이 | 좋아요/1천 | 올린 때(한국) | 주제 | 형식 | 글 출처 | 첫 줄(첫 3초) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [I know I should sleep, but the voices in my head …](https://www.youtube.com/shorts/17UP7J8Ri3E) | NOVAE | 13,600 | 25,628,478 | ×1884.45 | ×10076.1 | 164,704.5 | 12초 | 3.5 | 금 2시 | 1. 수면·명상·힐링 | 그 밖 | 없음 |  |
| 2 | [#shorts #lowcortisol #satisfying #chill #fypシ #he…](https://www.youtube.com/shorts/Gcb9eQDRJH4) | slasherbabyboom… | 9,850 | 13,578,369 | ×1378.51 | – | 89,426.9 | 20초 | 8.34 | 월 20시 | 1. 수면·명상·힐링 | 그 밖 | 없음 |  |
| 3 | [Bheema love bgm ...💞💥#lovestatus #bgm #trending #…](https://www.youtube.com/shorts/XvjJJ625eHM) | miracle_mix | 5,330 | 6,151,734 | ×1154.17 | ×2580.4 | 41,836.3 | 35초 | 17.86 | 토 15시 | 기타 | 그 밖 | 없음 |  |
| 4 | [Turning a Bad Day Into Piano Music 🎹💔 (AI Music T…](https://www.youtube.com/shorts/5bC_3ftzlh0) | Deep piano | 4,550 | 4,635,526 | ×1018.8 | ×2675.6 | 32,043.1 | 22초 | 13.36 | 화 0시 | 14. AI 음악 | AI 음악 | 설명 |  |
| 5 | [Relaxing Aquarium 4K 🐠 Beautiful Fish Tank Ambien…](https://www.youtube.com/shorts/pElnrfPGV1I) | Zing Shots | 170 | 151,906 | ×893.56 | ×279.5 | 1,013.1 | 11초 | 5.25 | 수 18시 | 2. 자연 소리·백색… | 그 밖 | 설명 |  |
| 6 | [피아노 단 하나의 음으로 모두를 얼어붙게한 곡 ∣ Kanye West - Runaway …](https://www.youtube.com/shorts/QOMO1DPI2Mo) | 페이브노트 Fave. | 12,700 | 9,030,930 | ×711.1 | ×73.0 | 56,506.2 | 25초 | 4.77 | 일 21시 | 6. 피아노·클래식·… | 그 밖 | 설명 |  |
| 7 | [Relaxing Heavy Rain Camping with Dog 🌧️ ∣ Inflata…](https://www.youtube.com/shorts/zGp1ymVBzqs) | 90s Aura Cozy V… | 20,800 | 14,756,551 | ×709.45 | ×439.8 | 254,049.2 | 23초 | 7.34 | 목 14시 | 2. 자연 소리·백색… | 그 밖 | 설명 |  |
| 8 | [What sound does a piano make? (ft. TCU Choir Camp…](https://www.youtube.com/shorts/bWhG1Fq7X8k) | Elijah Ong - Mu… | 22,100 | 15,414,076 | ×697.47 | ×355.3 | 147,515.6 | 35초 | 34.35 | 일 4시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 없음 |  |
| 9 | [연대별 시대곡 피아노 챌린지](https://www.youtube.com/shorts/s1hYfDOB5O0) | 패밀리모먼츠 | 12,700 | 7,499,203 | ×590.49 | ×293.6 | 94,439.8 | 53초 | 11.89 | 목 6시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 10 | [랜덤으로 지목 당해 노래 부르는 Happy](https://www.youtube.com/shorts/nb6TL41nJpQ) | FreshCutFarm | 35,700 | 20,431,132 | ×572.3 | ×5181.0 | 127,837.4 | 50초 | 14.3 | 일 21시 | 기타 | 클립·발췌 (방송·무… | 설명 |  |
| 11 | [Premada Oorali ∣ Official Animated Teaser ∣Soothi…](https://www.youtube.com/shorts/spkM9pTzGnc) | Royalediting143… | 1,770 | 1,004,236 | ×567.36 | ×3188.1 | 55,028.4 | 23초 | 14.15 | 화 10시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 12 | [#머무르 #꿈꾸던어른이되었나요 #커버 #장재혁 #보컬리스트장재혁#커버곡 #노래커버 #보컬…](https://www.youtube.com/shorts/av5KCoUA0K8) | 장재혁 Jang Jae Hy… | 230 | 115,760 | ×503.3 | ×86.6 | 2,907.7 | 57초 | 7.81 | 월 21시 | 12. 커버·노래 부… | 커버·직접 부른 노래 | 없음 |  |
| 13 | [A Dinosaur’s Love Story #piano #google #game #pia…](https://www.youtube.com/shorts/imH34A_Y-3I) | 영펭 yeongpin | 35,100 | 17,359,043 | ×494.56 | ×889.0 | 384,197.5 | 16초 | 7.88 | 수 12시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 없음 |  |
| 14 | [랜덤으로 지목 당해 노래 부르는 보헤미안 랩소디](https://www.youtube.com/shorts/xotW9olN4TU) | FreshCutFarm | 35,700 | 16,470,513 | ×461.36 | ×4176.6 | 101,596.3 | 59초 | 7.35 | 금 13시 | 기타 | 클립·발췌 (방송·무… | 설명 |  |
| 15 | ["Barsaat" song multi singer version 🔥❤️‍🩹 #barsaa…](https://www.youtube.com/shorts/sfCmfZP514k) | Indi Echo 🌿 | 3,880 | 1,579,183 | ×407.01 | – | 24,339.9 | 27초 | 13.4 | 목 19시 | 기타 | 그 밖 | 설명 |  |
| 16 | [💝 Ishq De Fanniyar ∣ Slowed + Reverb ∣ Lofi Aesth…](https://www.youtube.com/shorts/K0dMrCnd5Jw) | Jazzy Love Acti… | 46,400 | 18,763,672 | ×404.39 | ×755.8 | 384,662.4 | 44초 | 0.0 | 토 22시 | 8. 로파이·시티팝·칠 | 그 밖 | 설명 |  |
| 17 | [Best Reggae Songs 2026🌴 Pacific Island Reggae Col…](https://www.youtube.com/shorts/xGqYECoBV6w) | Reggaeneration … | 1,050 | 377,051 | ×359.1 | ×1118.8 | 3,090.6 | 31초 | 3.28 | 수 16시 | 8. 로파이·시티팝·칠 | 그 밖 | 설명 |  |
| 18 | [Try With Your Own Voice 💜✨ - Sammi Meri Waar [Lyr…](https://www.youtube.com/shorts/fzacLxIL_fI) | Lyrics Corner | 7,120 | 2,341,897 | ×328.92 | ×70.5 | 124,011.4 | 27초 | 0.0 | 월 19시 | 6. 피아노·클래식·… | 한 곡 일부 (음원·… | 없음 |  |
| 19 | [🎬: Musafir Cafe New Series 💗 #love #chillwavelofi…](https://www.youtube.com/shorts/y_8PunZgJws) | Chillwave lofi⚡ | 10,900 | 3,529,575 | ×323.81 | ×187.5 | 42,028.2 | 23초 | 10.22 | 토 17시 | 8. 로파이·시티팝·칠 | 그 밖 | 설명 |  |
| 20 | [🌿첫 소절부터 빠져드는 가을에 듣고 싶은 감성 팝송 ∣ 7080 추억의 올드팝](https://www.youtube.com/shorts/efkKPe_vNHQ) | Oldies Salon | 1,050 | 335,920 | ×319.92 | ×150.5 | 7,405.1 | 46초 | 3.49 | 수 8시 | 9. 가요·발라드·트… | 추천·모음 (N곡·순… | 설명 |  |
| 21 | [Musafir Cafe: Kaafi Hai Na (Song)∣ Vikrant Massey…](https://www.youtube.com/shorts/T6kiyfOI3xA) | Loop-e Shono | 2,570 | 777,726 | ×302.62 | ×272.5 | 8,380.7 | 30초 | 17.9 | 목 21시 | 4. 카페·매장·라운지 | 그 밖 | 설명 |  |
| 22 | [지휘자까지 춤추게 만든 손열음(피아노에서 빛이 난다면 이런 느낌일까?✨)](https://www.youtube.com/shorts/z76Om6wO-RA) | 사건의뒷면 | 23,300 | 6,651,330 | ×285.46 | – | 43,418.3 | 16초 | 5.81 | 일 12시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 23 | [ANIRUDH vs SAI ABHYANKKAR ∣ RECENT BGM & SONGS RA…](https://www.youtube.com/shorts/CDr5WeEZ5I0) | Tune ladder | 23,800 | 6,127,453 | ×257.46 | ×48.5 | 254,906.7 | 59초 | 0.0 | 수 15시 | 기타 | 그 밖 | 설명 |  |
| 24 | [옴 마니 반메 훔 🙏 잠들기 전 듣는 부처님의 기도](https://www.youtube.com/shorts/_edUsvdpI9A) | 마음한줄기 | 9,740 | 2,455,899 | ×252.15 | ×1875.4 | 15,648.1 | 18초 | 21.97 | 수 18시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 25 | [Summer Hits 2026 ☀️ Chill Deep House Mix for Rela…](https://www.youtube.com/shorts/IcxZ1gydQZQ) | Sea Breeze Music | 3,840 | 865,696 | ×225.44 | ×116.3 | 7,163.9 | 32초 | 2.82 | 목 20시 | 8. 로파이·시티팝·칠 | 추천·모음 (N곡·순… | 없음 |  |
| 26 | [Yoshi’s Island- Map BGM](https://www.youtube.com/shorts/PoRX7a-7dbQ) | Matsuzawa Aoi T… | 18,900 | 4,251,380 | ×224.94 | ×217.7 | 39,972.8 | 14초 | 8.89 | 금 8시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 27 | [KALYANI ∣ Shreya Ghoshal ∣ ARJN, KDS, FIFTY4 & RO…](https://www.youtube.com/shorts/XeIYQ5dfRBg) | WaveTune | 3,060 | 656,556 | ×214.56 | ×35.4 | 25,995.5 | 14초 | 7.91 | 화 10시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 28 | [Rihanna - Work ft. Drake ∣ Lyrics ∣ Edit ∣ Aesthe…](https://www.youtube.com/shorts/C1qxYvKH3UA) | Cᵒᵗᵗᵒᴺ ᴸʸʳⁱᶜˢ | 6,060 | 1,282,130 | ×211.57 | ×247.3 | 41,205.9 | 12초 | 19.5 | 수 13시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 29 | [🎧 Relax Lounge Music 🍷 #loungemusic #deephouse #c…](https://www.youtube.com/shorts/j4OomQ5nnJQ) | 뮤직인유 Music in U | 10,300 | 2,094,586 | ×203.36 | ×511.9 | 41,271.3 | 13초 | 12.98 | 목 22시 | 4. 카페·매장·라운지 | 클립·발췌 (방송·무… | 설명 |  |
| 30 | [Calming ASMR sounds for sleep and relaxation 01 #…](https://www.youtube.com/shorts/HVy_kywEeFU) | Spiral Men | 33,100 | 6,351,771 | ×191.9 | ×253.5 | 129,278.6 | 31초 | 5.61 | 토 13시 | 1. 수면·명상·힐링 | 그 밖 | 없음 |  |
| 31 | [432Hz - Deep Sleep Healing ∣ Alpha Waves for Comp…](https://www.youtube.com/shorts/TIiqFNACNJI) | Spiritual Heali… | 3,650 | 681,361 | ×186.67 | ×346.0 | 26,558.2 | 165초 | 6.26 | 화 1시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 32 | [Nonstop Pinoy Reggae 2026 ∣ Bagong Umaga ☀️ Relax…](https://www.youtube.com/shorts/065qRsHIZBw) | SoundTrip | 7,250 | 1,288,623 | ×177.74 | ×728.4 | 16,475.9 | 170초 | 3.91 | 금 11시 | 8. 로파이·시티팝·칠 | 추천·모음 (N곡·순… | 설명 |  |
| 33 | [RELAXING MUSIC - STRESS RELIEF🌿Soothing Piano & W…](https://www.youtube.com/shorts/4qEZq-8ZIfc) | Soul Soothing H… | 2,120 | 371,289 | ×175.14 | ×97.0 | 7,938.2 | 60초 | 5.14 | 월 22시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 34 | [Ibiza Summer Mix 2026 🍓 Best Tropical Deep House …](https://www.youtube.com/shorts/EfQeZ53iXSk) | Sea Breeze Music | 3,840 | 663,372 | ×172.75 | ×89.1 | 5,399.7 | 32초 | 3.41 | 화 20시 | 8. 로파이·시티팝·칠 | 추천·모음 (N곡·순… | 없음 |  |
| 35 | [Rihanna - Work ft. Drake ∣ Lyrics ∣ Edit ∣ Aesthe…](https://www.youtube.com/shorts/Hs3VpEMI-ks) | SUKUNA X lyrics | 5,060 | 856,681 | ×169.3 | ×169.6 | 30,891.4 | 12초 | 19.04 | 토 23시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 36 | [Beautiful Relaxing Piano Music & Water Sounds 💦 C…](https://www.youtube.com/shorts/GMrFw9KD5pA) | Soul Soothing H… | 2,120 | 349,209 | ×164.72 | ×91.2 | 8,075.2 | 60초 | 4.68 | 금 10시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 37 | [🎧 KUNG STRESS KA, PAKINGGAN MO ’TO! TANGGAL PAGOD…](https://www.youtube.com/shorts/9mQXTN8O_yE) | ISLANG REGGAE PH | 5,980 | 944,215 | ×157.9 | ×108.6 | 22,605.8 | 169초 | 4.8 | 토 22시 | 기타 | 그 밖 | 설명 |  |
| 38 | ["Deewana Deewana" song multi singer version ✨🗿∣∣ …](https://www.youtube.com/shorts/vqa0ki41KHM) | Indi Echo 🌿 | 3,880 | 584,096 | ×150.54 | – | 6,776.2 | 34초 | 12.96 | 목 11시 | 기타 | 그 밖 | 설명 |  |
| 39 | [Ajeeb Dastan Hai Yeh #multiplayer #music #retro #…](https://www.youtube.com/shorts/dbtBr8IQpt4) | Ashish Mithari | 37,300 | 5,274,561 | ×141.41 | ×858.0 | 51,335.1 | 40초 | 21.84 | 월 22시 | 6. 피아노·클래식·… | 그 밖 | 없음 |  |
| 40 | [90s Best Romantic Saxophone of All Time 🎷 Soulful…](https://www.youtube.com/shorts/GFRyA57h8O8) | FREEDOM MUSIC L… | 7,080 | 864,968 | ×122.17 | ×575.1 | 6,418.6 | 179초 | 6.93 | 목 22시 | 7. 재즈·보사노바 | 그 밖 | 설명 |  |
| 41 | [Top 10 Best Mass BGM Of South Movies 2026. #massb…](https://www.youtube.com/shorts/iTelMvTQHFY) | Aura Cinefy | 6,090 | 717,081 | ×117.75 | ×44.0 | 9,350.5 | 44초 | 27.97 | 일 0시 | 기타 | 추천·모음 (N곡·순… | 없음 |  |
| 42 | [🍁 가을팝송 너무 좋다 ∣ 첫 곡부터 편안한 70&80 올드팝 🎶 #oldpop #올드팝…](https://www.youtube.com/shorts/V1fX11NiQJ0) | ouroldpop | 1,160 | 133,987 | ×115.51 | ×168.3 | 2,773.2 | 57초 | 3.16 | 일 9시 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 설명 |  |
| 43 | [아무도 생각 못한 소리로 서부의 아이콘이 된 음악 #석양의무법자](https://www.youtube.com/shorts/2ZKxQjF1V0I) | 클래식한소절 | 45,800 | 5,179,216 | ×113.08 | ×37.3 | 120,801.1 | 52초 | 11.87 | 금 19시 | 6. 피아노·클래식·… | 그 밖 | 설명 |  |
| 44 | [힐링](https://www.youtube.com/shorts/MBibKwN7oLA) | +82정 | 12,300 | 1,217,362 | ×98.97 | ×27.0 | 8,872.8 | 60초 | 8.38 | 화 11시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 45 | [한때 라디오만 켜면 흘러나오던 전설의 ‘외로운 양치기’ #팬플루트](https://www.youtube.com/shorts/QG2blK1FVyg) | 클래식한소절 | 45,800 | 4,530,509 | ×98.92 | ×32.6 | 55,328.1 | 38초 | 13.59 | 월 19시 | 9. 가요·발라드·트… | 연주 (직접 연주) | 설명 |  |
| 46 | [🎧 Luxury Lounge Music 🍷 #loungemusic #deephouse #…](https://www.youtube.com/shorts/NQrsgRLPKFs) | 뮤직인유 Music in U | 10,300 | 877,053 | ×85.15 | ×214.3 | 18,977.6 | 11초 | 13.42 | 화 11시 | 4. 카페·매장·라운지 | 클립·발췌 (방송·무… | 설명 |  |
| 47 | [Sohnea Song Lyrics – Miss Pooja ft. Millind Gaba …](https://www.youtube.com/shorts/vazUHUAfuKI) | LyriVoice | 5,490 | 465,060 | ×84.71 | ×228.1 | 3,181.5 | 49초 | 0.0 | 일 12시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 48 | [Night Oud Relaxing Arabic Music Melodies #oud #ud…](https://www.youtube.com/shorts/OfDQoPCZaYo) | Azqara | 31,800 | 2,516,084 | ×79.12 | ×76.6 | 20,491.0 | 29초 | 11.31 | 화 21시 | 기타 | 그 밖 | 없음 |  |
| 49 | [Barsaat (Lyrics) ~ Banjaare ∣🌧️🥀 Aesthetic Lyrics…](https://www.youtube.com/shorts/-oOlND34r8c) | nature-lyrics-P… | 9,460 | 657,405 | ×69.49 | ×43.1 | 13,125.6 | 26초 | 19.58 | 금 14시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 50 | [감성 뮤직/Emotional music #healing #love #lifeisbutad…](https://www.youtube.com/shorts/Jm4-p0mQjBk) | JEONGAM Media A… | 38,100 | 2,579,612 | ×67.71 | ×1203.7 | 15,417.9 | 31초 | 10.59 | 일 9시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 51 | [인연의 술잔 ∣ 감성 트로트 ∣ 추억 속의 위로 음악 #트로트 #감성 #중년음악#shor…](https://www.youtube.com/shorts/iJ8agTK7wBw) | 노래로 가보자(어제보다 나은… | 9,800 | 625,924 | ×63.87 | ×409.1 | 3,813.0 | 129초 | 9.55 | 수 13시 | 9. 가요·발라드·트… | 커버·직접 부른 노래 | 설명 |  |
| 52 | [Aakashame Nuvvani Full Lyrical Video ∣ Diamond Ra…](https://www.youtube.com/shorts/wuYBw0iMUvo) | Rakesh edits | 32,500 | 2,028,305 | ×62.41 | ×45.1 | 16,863.6 | 15초 | 18.96 | 금 10시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 53 | [Aakashame Nuvvani ❤️✨ ∣ Diamond Raja ∣ Sid Sriram…](https://www.youtube.com/shorts/lGOry4snFDg) | KD Creation | 19,200 | 1,174,032 | ×61.15 | ×64.2 | 32,834.9 | 13초 | 16.85 | 금 22시 | 기타 | 그 밖 | 설명 |  |
| 54 | [Jaane meriye main tera haan song ❤ ∣ Trending 🙈 w…](https://www.youtube.com/shorts/Ch6fbOogn3E) | R.K Music 7 | 48,200 | 2,831,232 | ×58.74 | ×136.1 | 19,764.7 | 29초 | 0.0 | 수 10시 | 기타 | 그 밖 | 설명 |  |
| 55 | [Suno Nand Lal ਤਨਖ਼ਾਹ ਨਾਮਾ : ਭਾਈ ਨੰਦ ਲਾਲ #meditati…](https://www.youtube.com/shorts/qUAwuEQa61U) | Tere Bande | 13,400 | 746,947 | ×55.74 | ×83.3 | 4,208.0 | 73초 | 18.59 | 목 4시 | 1. 수면·명상·힐링 | AI 음악 | 설명 |  |
| 56 | [Masya Alloh!!❤Udah Ganteng Sholih juga😍 #muharram…](https://www.youtube.com/shorts/X9B_mhJWP_I) | Peaceful Ummah … | 42,000 | 2,225,558 | ×52.99 | ×132.2 | 18,050.2 | 36초 | 0.0 | 화 9시 | 기타 | 그 밖 | 설명 |  |
| 57 | [빈손...퓨전국악/인생노래/불교/감성트롯/위로. ..](https://www.youtube.com/shorts/XfqDLZGv0-k) | 숨소리 가요 | 11,000 | 582,149 | ×52.92 | ×324.1 | 3,422.1 | 65초 | 8.74 | 목 14시 | 9. 가요·발라드·트… | 한 곡 일부 (음원·… | 설명 |  |
| 58 | [part 2 of turning sad pieces happy #piano #music …](https://www.youtube.com/shorts/N003UbT7HVc) | piano.mp3 | 26,200 | 1,252,481 | ×47.8 | ×54.2 | 30,974.9 | 22초 | 37.96 | 월 6시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 없음 |  |
| 59 | [Barsaat (Lyrics) - Banjaare ∣ ✨Aesthetic Lyrics V…](https://www.youtube.com/shorts/pcBPXx3yN80) | LYRICAL YT 94 | 12,000 | 517,570 | ×43.13 | ×68.8 | 10,121.8 | 17초 | 23.07 | 목 13시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 60 | [🍂9월의 일요일, 가을 아침에 듣기 좋은 노래 ∣ 편안한 추억의 올드팝송 ∣ 9월 카페음…](https://www.youtube.com/shorts/-IxTh4fUxyc) | 나무감성 NAMUVIBE | 2,470 | 101,817 | ×41.22 | ×79.2 | 2,100.3 | 54초 | 3.29 | 일 5시 | 4. 카페·매장·라운지 | 추천·모음 (N곡·순… | 설명 |  |
| 61 | [Golden Sunset in Andalusia 🌅 ∣ Relaxing Oud & Spa…](https://www.youtube.com/shorts/8hosf0uYb-Q) | Andalusian Oud … | 26,700 | 1,086,101 | ×40.68 | ×86.7 | 7,575.9 | 61초 | 11.4 | 수 8시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 62 | [🍂 Cozy Autumn Coffee Ambience ☕ Relaxing Guitar I…](https://www.youtube.com/shorts/kbM0eMDlxbQ) | Guitar Coffee M… | 13,700 | 542,181 | ×39.58 | – | 6,676.5 | 154초 | 3.74 | 화 11시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 63 | [같은 노래 맞아...? [이창섭 (LEECHANGSUB) - 사계, 그리고 너]](https://www.youtube.com/shorts/giN8f3Pxp4k) | 바코드 플레이리스트 | 24,400 | 959,294 | ×39.32 | ×86.1 | 38,414.9 | 43초 | 6.52 | 화 17시 | 기타 | 추천·모음 (N곡·순… | 없음 |  |
| 64 | [[불교음악] 흐르는 강물처럼 — 인생의 끝에서 부처님께 묻다 ∣ 나무아미타불 관세음보살 …](https://www.youtube.com/shorts/3zbiRtRhRHY) | 연꽃선율 | 21,500 | 838,827 | ×39.02 | ×88.1 | 4,744.3 | 169초 | 12.28 | 목 21시 | 기타 | 그 밖 | 설명 |  |
| 65 | [Rihanna - Work (Lyrics) ft. Drake](https://www.youtube.com/shorts/b9SFUlKKIDw) | Fantazia Music | 25,900 | 951,904 | ×36.75 | ×17.5 | 20,423.8 | 13초 | 11.23 | 화 2시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 66 | [put on the losercore playlist](https://www.youtube.com/shorts/JsN-vShHpIM) | Bro Archive | 6,800 | 245,269 | ×36.07 | ×9.0 | 19,718.9 | 15초 | 13.53 | 월 6시 | 기타 | 추천·모음 (N곡·순… | 설명 |  |
| 67 | [The Most Beautiful Adagio You'll Hear Today ∣ Rel…](https://www.youtube.com/shorts/lvDGMqpTS_c) | Adagio Maestro | 22,300 | 789,097 | ×35.39 | ×216.4 | 8,694.3 | 177초 | 30.55 | 토 22시 | 1. 수면·명상·힐링 | AI 음악 | 설명 |  |
| 68 | [[동요] 수업 준비 노래 ∣ 주의집중 ∣ 손유희 ∣ 공립유치원교사 🏫🎵](https://www.youtube.com/shorts/q66lMjvhItc) | 현클래스 | 1,500 | 50,941 | ×33.96 | – | 514.7 | 28초 | 9.09 | 금 17시 | 3. 공부·집중·작업 | 그 밖 | 설명 |  |
| 69 | [Relaxing Piano Music – Deep Sleep Music with Bamb…](https://www.youtube.com/shorts/SjTXZ_K2si0) | Relaxing Gen Mu… | 3,570 | 116,030 | ×32.5 | ×41.3 | 652.3 | 60초 | 9.51 | 수 19시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 70 | [[BLACK SCREEN] Anxiety Relief Music 432Hz + 528Hz…](https://www.youtube.com/shorts/w50gRv2lvNA) | Tranquil Sounds… | 40,200 | 1,289,349 | ×32.07 | ×233.5 | 13,202.0 | 145초 | 8.06 | 일 0시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 71 | [🌊 하루종일 듣기 좋은 부드러운 카페 음악 ☕ 오션뷰 감성팝](https://www.youtube.com/shorts/FdKCaSIsKMM) | Moasway | 7,890 | 226,691 | ×28.73 | ×53.8 | 1,404.5 | 51초 | 2.6 | 토 7시 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 |  |
| 72 | [☕Coffee Time ∣ Relaxing Piano Music (☕커피 한잔할 때 듣기…](https://www.youtube.com/shorts/LOufJXnJB6k) | 마음의 휴식 | 3,240 | 81,058 | ×25.02 | ×1102.8 | 833.0 | 178초 | 12.16 | 일 9시 | 4. 카페·매장·라운지 | 연주 (직접 연주) | 없음 |  |
| 73 | [Put on that LimbusCore playlist #limbuscompany #m…](https://www.youtube.com/shorts/aNtWKQPTxaQ) | Not Na | 6,260 | 145,101 | ×23.18 | ×15.4 | 16,616.4 | 20초 | 36.13 | 목 23시 | 기타 | 추천·모음 (N곡·순… | 설명 |  |
| 74 | [💖 Ayyare Ayyare ∣ Romantic Melody Song ∣ Vijay & …](https://www.youtube.com/shorts/GPqdnSDRZ9U) | Vibe With Giree… | 46,100 | 1,057,603 | ×22.94 | ×31.9 | 18,312.5 | 21초 | 15.29 | 목 22시 | 기타 | 그 밖 | 설명 |  |
| 75 | [포세이큰 LMS ost 플레이리스트](https://www.youtube.com/shorts/ddwhcZffLBU) | 백설탕 | 3,330 | 75,635 | ×22.71 | ×9.5 | 639.4 | 25초 | 31.78 | 일 9시 | 13. OST·사운드… | 추천·모음 (N곡·순… | 없음 |  |
| 76 | [풀버전듣기⬆️아침에 듣기좋은 잔잔한 팝송 ∣ Best Nostalgia 70s 80s O…](https://www.youtube.com/shorts/o5bPkIQ8OyY) | Nostalgic Old P… | 2,950 | 64,357 | ×21.82 | ×46.7 | 401.1 | 28초 | 3.29 | 일 6시 | 10. 팝송·K팝·J팝 | 클립·발췌 (방송·무… | 설명 |  |
| 77 | [Cosmic Soul Healing 🌠 432Hz + 528Hz + 963Hz](https://www.youtube.com/shorts/5vuNKdYVZd4) | Tranquil Sounds… | 40,200 | 857,819 | ×21.34 | ×155.4 | 8,515.7 | 137초 | 9.73 | 수 23시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 78 | [Peaceful Streets of Cordoba ∣ Relaxing Oud & Span…](https://www.youtube.com/shorts/GlP9I-o0usQ) | Andalusian Oud … | 26,700 | 539,597 | ×20.21 | ×43.1 | 3,816.2 | 96초 | 12.16 | 금 7시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 79 | [[림버스 컴퍼니] 림버스 플레이리스트](https://www.youtube.com/shorts/c9NFDK2aQZw) | Da대행자 | 2,910 | 58,764 | ×20.19 | ×1.4 | 417.1 | 41초 | 52.57 | 금 19시 | 기타 | 추천·모음 (N곡·순… | 없음 |  |
| 80 | [듣는 순간 가슴이 무너지는 명곡｜바람에 구름가듯 _ 이은하 #7080 #감성음악 #추억소환](https://www.youtube.com/shorts/4byi4WW3kYM) | 뮤직 에세이 수필 _ Soo… | 20,900 | 421,395 | ×20.16 | ×51.1 | 3,147.7 | 47초 | 9.96 | 금 19시 | 9. 가요·발라드·트… | 추천·모음 (N곡·순… | 설명 |  |
| 81 | [어머니의 고무신 ∣ 산사에 새긴 그 기도, 이제야 압니다 #불교음악](https://www.youtube.com/shorts/jwCa6iqW5XA) | 연꽃선율 | 21,500 | 430,641 | ×20.03 | ×45.3 | 2,575.3 | 157초 | 16.52 | 일 11시 | 기타 | 그 밖 | 설명 |  |
| 82 | [🙏스님이 부른 노래 한 곡, 모두의 마음을 울리다 #불교음악 #관세음보살 #소원성취 #깊…](https://www.youtube.com/shorts/pgvUxeoYESA) | 연꽃 아래서 | 13,000 | 259,049 | ×19.93 | ×11.6 | 1,915.8 | 28초 | 13.71 | 목 11시 | 15. CCM·찬양·… | 그 밖 | 없음 |  |
| 83 | [🙏 불교노래｜상처를 내려놓으리｜명상음악｜국악트롯 #관세음보살 #불교음악 #위로](https://www.youtube.com/shorts/ZyP0PyN0NV8) | 마음의쉼터 | 5,920 | 113,844 | ×19.23 | ×7.5 | 1,193.3 | 74초 | 26.4 | 화 7시 | 1. 수면·명상·힐링 | 그 밖 | 없음 |  |
| 84 | [Top 5 Peaceful Night Songs 🌙 ∣ सोने से पहले ज़रूर…](https://www.youtube.com/shorts/H2hBVIzRVGs) | SK facts YT | 10,700 | 191,007 | ×17.85 | ×12.3 | 1,805.4 | 42초 | 23.36 | 금 21시 | 기타 | 추천·모음 (N곡·순… | 설명 |  |
| 85 | [Relax Your Mind 🌼 Soft Piano & Violin with Beauti…](https://www.youtube.com/shorts/UkjpAZW4eFQ) | Quick Anxiety R… | 43,100 | 767,359 | ×17.8 | ×14.5 | 6,454.4 | 134초 | 16.78 | 토 19시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 86 | [Ambient Ocean Drums 🌊 ∣ The Most Beautiful Nordic…](https://www.youtube.com/shorts/tGQVITlgDBQ) | Nordic Fjord Ha… | 8,350 | 141,761 | ×16.98 | ×81.4 | 955.4 | 16초 | 12.85 | 금 7시 | 기타 | 그 밖 | 설명 |  |
| 87 | [💖 Ayyare Ayyare ∣ Romantic Melody Song ∣ Vijay & …](https://www.youtube.com/shorts/Jsc6FFKw_E4) | Vibe With Giree… | 46,100 | 757,148 | ×16.42 | ×22.9 | 17,536.3 | 20초 | 14.4 | 금 12시 | 기타 | 그 밖 | 설명 |  |
| 88 | [Deep Sleep with Peaceful Piano Music: Binh Yen Pi…](https://www.youtube.com/shorts/6b8oWfvd6dw) | BINH YEN PIANO | 31,100 | 491,580 | ×15.81 | ×35.4 | 6,202.3 | 9초 | 2.87 | 목 10시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 89 | [Deep Sleep Music (No Ads) ∣ Stop Overthinking, He…](https://www.youtube.com/shorts/ToJBmQ0LZtU) | Dreamy Calm Mus… | 26,600 | 399,743 | ×15.03 | – | 3,411.5 | 56초 | 7.6 | 월 12시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 90 | [🙏신나는 찬양 ∣ 마음이 참 편안합니다.. 주님 안에서 누리는 평안 🎵 중년 힐링 찬양 …](https://www.youtube.com/shorts/ZXKo0P0atPs) | 은혜의 멜로디 | 11,100 | 157,738 | ×14.21 | ×7.4 | 2,375.4 | 178초 | 11.23 | 수 7시 | 5. 운동·드라이브·… | 그 밖 | 설명 |  |
| 91 | [Best Relaxing Music Saxophone #relaxingmusic #sax…](https://www.youtube.com/shorts/A8JCdVa6Vb0) | Radha Krishna S… | 8,530 | 114,942 | ×13.48 | ×15.1 | 2,117.8 | 40초 | 10.26 | 월 10시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 92 | [Tere Sang Yaara ~ Astif Aslam ∣ Aesthetic Lyrics …](https://www.youtube.com/shorts/TpGaLxvtICk) | HarmonicVibez | 48,100 | 618,252 | ×12.85 | ×13.1 | 5,632.8 | 16초 | 0.0 | 월 22시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 93 | [Relax Your Mind 🐦 Piano & Violin with Birds and B…](https://www.youtube.com/shorts/FXSTlxwJP0Y) | Quick Anxiety R… | 43,100 | 550,055 | ×12.76 | ×11.0 | 9,187.1 | 172초 | 18.05 | 화 19시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 94 | [🙏 불교노래｜가는 길 밝혀주소서｜명상음악｜국악트롯 #관세음보살 #불교음악 #위로](https://www.youtube.com/shorts/nv_yiPwhH5o) | 마음의쉼터 | 5,920 | 75,311 | ×12.72 | ×4.9 | 708.9 | 96초 | 24.39 | 금 10시 | 1. 수면·명상·힐링 | 그 밖 | 없음 |  |
| 95 | [#relaxingmusic](https://www.youtube.com/shorts/p4dSlB1-18k) | veerpulse | 44,600 | 512,693 | ×11.5 | ×7.3 | 47,043.4 | 6초 | 0.0 | 화 19시 | 기타 | 그 밖 | 설명 |  |
| 96 | [Calm Guzheng & Flute in Crystal Temple Ruins ∣ Ze…](https://www.youtube.com/shorts/aveC_SEj_xY) | Pure Chinese In… | 19,300 | 203,258 | ×10.53 | ×86.5 | 1,236.3 | 116초 | 23.66 | 수 7시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 97 | [10월에 듣는 카페음악☕🍂 #가을에듣기좋은음악 #카페음악 #힐링음악 #shorts Vol…](https://www.youtube.com/shorts/_pTWZdK_Lgw) | 노래의 조각들 | 18,400 | 192,019 | ×10.44 | ×8.2 | 8,226.1 | 57초 | 2.96 | 목 8시 | 1. 수면·명상·힐링 | 추천·모음 (N곡·순… | 설명 |  |
| 98 | [Deep Sleep with Peaceful Piano Music: Binh Yen Pi…](https://www.youtube.com/shorts/LiC8OATiDFw) | BINH YEN PIANO | 31,100 | 305,639 | ×9.83 | ×22.0 | 11,637.9 | 9초 | 2.62 | 월 10시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 99 | [🙏 천수경｜비구니 스님의 맑은 목소리에 눈물이 납니다 #불교음악 #깊은기도음악 #스님 #…](https://www.youtube.com/shorts/y1h3ne5BUTE) | 연꽃 아래서 | 13,000 | 127,356 | ×9.8 | ×5.7 | 1,220.3 | 30초 | 17.54 | 일 8시 | 15. CCM·찬양·… | 그 밖 | 설명 |  |
| 100 | [티없이 맑은 비구니 스님의 금강경 사구게 첫 번째와 두 번째 게송｜머문 바 없이 그 마음…](https://www.youtube.com/shorts/B3vGWKWShgA) | 인생은 트롯이지 | 20,200 | 187,996 | ×9.31 | ×115.3 | 1,234.0 | 70초 | 16.1 | 월 8시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 101 | [옴 마니 반메 훔 🙏 Om Mani Padme Hum 唵嘛呢叭咪吽 플루트 & 피아노 불교…](https://www.youtube.com/shorts/HA0Eotjrhcs) | Lotus of the Bu… | 18,500 | 172,008 | ×9.3 | ×27.7 | 1,558.0 | 161초 | 32.07 | 월 7시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 102 | [🍋 그냥 틀어두기 좋은 여름 카페 음악 🌿 편안한 감성팝 #카페 #힐링 #배경음악](https://www.youtube.com/shorts/HifHEgRTBMk) | Moasway | 7,890 | 68,649 | ×8.7 | ×16.4 | 492.4 | 60초 | 3.0 | 일 7시 | 1. 수면·명상·힐링 | 추천·모음 (N곡·순… | 설명 |  |
| 103 | [9월에 듣는 카페음악☕🍂 #가을에듣기좋은음악 #카페음악 #힐링음악 #shorts Vol.…](https://www.youtube.com/shorts/jox06rqLQL0) | 노래의 조각들 | 18,400 | 156,778 | ×8.52 | ×6.7 | 3,732.0 | 59초 | 3.0 | 토 16시 | 1. 수면·명상·힐링 | 추천·모음 (N곡·순… | 설명 |  |
| 104 | [♥️✨🌷#karolinaprostenko #relaxingmusic #instrument…](https://www.youtube.com/shorts/yo0BqCXA3dI) | violin girls | 20,900 | 126,736 | ×6.06 | ×63.3 | 922.6 | 16초 | 18.21 | 화 8시 | 6. 피아노·클래식·… | 그 밖 | 없음 |  |
| 105 | [마음치유](https://www.youtube.com/shorts/iZtyEXngfdU) | +82정 | 12,300 | 70,014 | ×5.69 | ×1.6 | 517.1 | 27초 | 16.48 | 목 7시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 106 | [[감성트로트] 기댈 곳 하나 없는🍂 #인생가 #트로트신곡 #한국트로트 #감성음악 #노래추…](https://www.youtube.com/shorts/P_CVL87cbjI) | 규규티비 | 37,800 | 211,887 | ×5.61 | ×34.5 | 1,490.9 | 142초 | 14.28 | 목 13시 | 9. 가요·발라드·트… | 한 곡 일부 (음원·… | 설명 |  |
| 107 | [아침마다 새로운 은혜 🌿 오늘도 감사로 시작합니다 ∣ 마음이 편안해지는 찬양 #shorts](https://www.youtube.com/shorts/LaS3Aq4yWm8) | 은혜의 멜로디 | 11,100 | 55,858 | ×5.03 | ×2.6 | 1,178.3 | 180초 | 11.67 | 월 7시 | 15. CCM·찬양·… | 그 밖 | 설명 |  |
| 108 | [옴 마니 반메 훔 🙏 Om Mani Padme Hum ∣ 唵嘛呢叭咪吽 한국 가야금 불교 …](https://www.youtube.com/shorts/y7LKZ9HwUBc) | Lotus of the Bu… | 18,500 | 90,273 | ×4.88 | ×14.6 | 810.3 | 162초 | 57.03 | 일 7시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |

기준은 넘었지만 뺀 것: WORK (FUNK) (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Deep Sleep with Peaceful Pian… (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생)); 일할때 듣기좋은 발라드 추천 광고없는 노래모음 - 유… (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생)); 9월에 듣는 카페음악☕🍂 #가을에듣기좋은음악 #카페음… (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생)); Bloody Band (From "DC") (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Soft Smiles Only (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); One Name - Theme (From "Jaile… (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); 비가오니까 (밤의무희cover) (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Lemon Tang (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); REDRED (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Jum jum jhumthaara (From "Zom… (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); 모락산 #정설허브 #감성음악 #힐링음악 (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생)); BOOMPALA (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Love is in the Air, Pt. 1 (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); ICONIC BY MISTAKE (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Namaste (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Thaalam Trip (Instrumental) (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); The Rose (Instrumental) (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); 【RELAXING PIANO BGM】溫柔鋼琴曲｜讓心情… (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생)); Kalyani Song 🍁∣ Whatsapp stat… (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생))

### 1-2. 같은 채널 기준선 (채널 쇼츠 목록 96곳 — 채널 크기·구독층이 같은 쇼츠끼리)

성공 쇼츠 101/108개에 '채널 평소 쇼츠 대비'(그 채널의 올린 지 3~180일 쇼츠 조회수 중앙값, 쇼츠 5개 넘을 때). 채널 89곳의 잘된 쇼츠(중앙값 ×3.0 이상) 376개 vs 평소 쇼츠(×0.5~1.5) 416개 — 채널당 5개씩

- 길이 중앙값: 잘된 36초 · 평소 38초 · 제목 글자 중앙값: 잘된 73.5 · 평소 68.0 · 해시태그 수 중앙값: 잘된 10.0 · 평소 8.0

| 제목 특징 | 잘된 쇼츠 | 평소 쇼츠 | 차이 |
|---|---|---|---|
| 구분 기호(ㅣ·｜·/)로 나눔 | 50% | 42% | 8.1% |
| 숫자가 들어감 | 31% | 26% | 5.6% |
| 따옴표·괄호로 강조 | 7.2% | 11% | -4% |
| '#shorts' 표시 | 14% | 18% | -4% |
| vs 비교 | 3.5% | 1.2% | 2.3% |
| 물음표 ? | 3.2% | 2.2% | 1.0% |
| 느낌표 ! | 3.2% | 4.1% | -1% |
| 과정·벌어진 일·결말·결국 | 0.5% | 0% | 0.5% |
| 말줄임 …·... | 2.4% | 1.9% | 0.5% |
| 사연·오디오북·실화·고백 | 0.3% | 0% | 0.3% |
| AI | 6.1% | 5.8% | 0.3% |
| 패턴형(공통점·특징·이유·N가지·착각·과정) | 0.5% | 0.7% | -0% |
| 이유 | 0.5% | 0.7% | -0% |
| 노후·퇴직금·은퇴·50~70대 | 0% | 0.2% | -0% |

| 주제 묶음 | 잘된 | 평소 | 차이 |
|---|---|---|---|
| 기타 | 44% | 50% | -6% |
| 8. 로파이·시티팝·칠 | 5.9% | 2.2% | 3.7% |
| 4. 카페·매장·라운지 | 4.3% | 1.7% | 2.6% |
| 12. 커버·노래 부르기 | 1.1% | 3.4% | -2% |
| 5. 운동·드라이브·신나는 | 1.9% | 0.7% | 1.2% |
| 1. 수면·명상·힐링 | 14% | 15% | -1% |
| 3. 공부·집중·작업 | 0.8% | 0.2% | 0.6% |
| 6. 피아노·클래식·연주곡 | 16% | 15% | 0.6% |
| 7. 재즈·보사노바 | 0.5% | 0% | 0.5% |
| 9. 가요·발라드·트로트 | 6.9% | 6.5% | 0.4% |

| 형식 | 잘된 | 평소 | 차이 |
|---|---|---|---|
| 한 곡 일부 (음원·뮤비·가사·티저) | 17% | 15% | 2.2% |
| 그 밖 | 47% | 49% | -2% |
| 연주 (직접 연주) | 15% | 16% | -1% |
| AI 음악 | 1.3% | 0.2% | 1.1% |
| 커버·직접 부른 노래 | 3.7% | 4.3% | -1% |
| 클립·발췌 (방송·무대·직캠) | 3.7% | 3.1% | 0.6% |
| 추천·모음 (N곡·순위·플리) | 12% | 12% | 0.2% |

같은 채널에서 잘된 쇼츠 (채널 평소 대비 큰 순):

- ×3162.9 · 1,004,236회 · 23초 · Royalediting143… — Premada Oorali ∣ Official Animated Teaser ∣Soothing Title Song (https://www.youtube.com/shorts/spkM9pTzGnc)
- ×2511.9 · 6,151,734회 · 35초 · miracle_mix — Bheema love bgm ...💞💥#lovestatus #bgm #trending #love (https://www.youtube.com/shorts/XvjJJ625eHM)
- ×1027.9 · 124,381회 · 99초 · 정설허브 — 모락산 #정설허브 #감성음악 #힐링음악 (https://www.youtube.com/shorts/Gh92mQKihOY)
- ×930.2 · 112,554회 · 89초 · 정설허브 — 해질녁 단상 #노래 #music #감성 (https://www.youtube.com/shorts/4HF-MBQWcH8)
- ×873.5 · 17,359,043회 · 16초 · 영펭 yeongpin — A Dinosaur’s Love Story #piano #google #game #pianocover #pianotutori… (https://www.youtube.com/shorts/imH34A_Y-3I)
- ×806.6 · 97,603회 · 84초 · 정설허브 — 추억을 삼키다 (https://www.youtube.com/shorts/a_21qqkufng)
- ×684.5 · 1,916,491회 · 14초 · Akshuu Beats — Kalyani Song 🍁∣ Whatsapp status 🌿 ∣#lyrics #edit #shorts #status #tre… (https://www.youtube.com/shorts/ZWYIJzAnGZ8)
- ×659.1 · 1,288,623회 · 170초 · SoundTrip — Nonstop Pinoy Reggae 2026 ∣ Bagong Umaga ☀️ Relaxing Island Vibes ∣ M… (https://www.youtube.com/shorts/065qRsHIZBw)
- ×390.5 · 47,256회 · 71초 · 정설허브 — 태을봉 정상에 올라 (https://www.youtube.com/shorts/QyCKIPQyDpI)
- ×328.3 · 14,756,551회 · 23초 · 90s Aura Cozy V… — Relaxing Heavy Rain Camping with Dog 🌧️ ∣ Inflatable Tent ASMR Time-L… (https://www.youtube.com/shorts/zGp1ymVBzqs)
- ×325.1 · 681,361회 · 165초 · Spiritual Heali… — 432Hz - Deep Sleep Healing ∣ Alpha Waves for Complete Body and Spirit… (https://www.youtube.com/shorts/TIiqFNACNJI)
- ×279.2 · 151,906회 · 11초 · Zing Shots — Relaxing Aquarium 4K 🐠 Beautiful Fish Tank Ambience with Sleep Music … (https://www.youtube.com/shorts/pElnrfPGV1I)
- ×265.9 · 15,414,076회 · 35초 · Elijah Ong - Mu… — What sound does a piano make? (ft. TCU Choir Camp) #shorts (https://www.youtube.com/shorts/bWhG1Fq7X8k)
- ×258.6 · 554,167회 · 129초 · JEONGAM Media A… — World · Humanity · Story ∣ Emotional story/감성 스토리 World · Humanity · … (https://www.youtube.com/shorts/vJ7M38clmHs)
- ×244.5 · 864,968회 · 179초 · FREEDOM MUSIC L… — 90s Best Romantic Saxophone of All Time 🎷 Soulful Smooth Jazz Love So… (https://www.youtube.com/shorts/GFRyA57h8O8)
- ×237.9 · 194,608회 · 59초 · ouroldpop — 🍁 가을엔 역시 이런 목소리가 좋다 ∣ 오래 듣고 싶은 올드팝 #oldpop #music (https://www.youtube.com/shorts/lL2T8FIbIzM)
- ×228.1 · 1,282,130회 · 12초 · Cᵒᵗᵗᵒᴺ ᴸʸʳⁱᶜˢ — Rihanna - Work ft. Drake ∣ Lyrics ∣ Edit ∣ Aesthetic ∣ #Rihanna #Work… (https://www.youtube.com/shorts/C1qxYvKH3UA)
- ×216.3 · 4,251,380회 · 14초 · Matsuzawa Aoi T… — Yoshi’s Island- Map BGM (https://www.youtube.com/shorts/PoRX7a-7dbQ)
- ×212.4 · 1,820,180회 · 55초 · 뮤직 에세이 수필 _ Soo… — 세월이 훅~ 지나간 흔적! 새벽비 _ 혜은이 #7080 #추억소환 #세련미 (https://www.youtube.com/shorts/amCIsWqkIq4)
- ×209.4 · 197,120회 · 36초 · Justin 放鬆音樂 — 【RELAXING PIANO BGM】溫柔鋼琴曲｜讓心情瞬間變好 (https://www.youtube.com/shorts/XebWlrpCnOc)

성공 쇼츠와 같은 채널 평소 쇼츠 짝 (표지): [`thumbs_pairs_01.jpg`](thumbs_pairs_01.jpg) (#1~), [`thumbs_pairs_02.jpg`](thumbs_pairs_02.jpg) (#12~)

### 1-3. 자료를 받지 않은 성공 후보 45개 (웹 화면 [쇼츠] 목록에서 승인하면 분석에 들어감 — 채널 자리가 찬 것 300개는 뺌)

| 제목 | 채널 | 구독자 | 조회수 | 배수 | 길이 | 올린 날 | 주제 |
|---|---|---|---|---|---|---|---|
| [공포 브금으로 유명한데 사실은 사랑 노래 ∣ The Lennon Sisters - Ton…](https://www.youtube.com/shorts/Unc6T08ta98) | 페이브노트 Fave. | 12,700 | 9,366,699 | ×737.54 | 16초 | 2026-05-07 | 기타 |
| [KALYANI ∣ Shreya Ghoshal ∣ ARJN, KDS, FIFTY4 & RO…](https://www.youtube.com/shorts/lb5HxezKf9E) | WaveTune | 3,060 | 1,043,505 | ×341.01 | 11초 | 2026-10-04 | 기타 |
| [🍁 가을엔 역시 이런 목소리가 좋다 ∣ 오래 듣고 싶은 올드팝 #oldpop #music](https://www.youtube.com/shorts/lL2T8FIbIzM) | ouroldpop | 1,160 | 194,608 | ×167.77 | 59초 | 2026-09-08 | 1. 수면·명상·힐링 |
| [💝 Ishq De Fanniyar ∣ Slowed + Reverb ∣ Lofi Aesth…](https://www.youtube.com/shorts/DF-BBMCHDg8) | Janny Love Acti… | 19,300 | 3,062,351 | ×158.67 | 32초 | 2026-09-18 | 8. 로파이·시티팝·칠 |
| [KALYANI ❤️✨Full Lyrics ∣∣ Trending Malayalam Song…](https://www.youtube.com/shorts/EyK5d_TX-wM) | nature-lyrics-P… | 9,460 | 1,441,819 | ×152.41 | 14초 | 2026-09-05 | 기타 |
| [Verity’s from minecraft (instrumental)](https://www.youtube.com/shorts/z3hhEIqj6lM) | Bro Archive | 6,800 | 886,229 | ×130.33 | 8초 | 2026-10-02 | 6. 피아노·클래식·연주곡 |
| [Rata lambiya kaliya ne sami ∣ Sammi meri waar ∣ M…](https://www.youtube.com/shorts/6jfq510fX0Q) | Loop-e Shono | 2,570 | 319,249 | ×124.22 | 16초 | 2026-09-10 | 기타 |
| [Kalyani ✨ ∣ Full Song ∣ Beautiful Hindi Song ∣ Tr…](https://www.youtube.com/shorts/XAM2w0kPuQE) | LYRICAL YT 94 | 12,000 | 1,363,320 | ×113.61 | 14초 | 2026-09-20 | 기타 |
| [A Dinosaur's Love Story with piano #piano #google…](https://www.youtube.com/shorts/fMplxZP-Hbk) | 영펭 yeongpin | 35,100 | 3,469,262 | ×98.84 | 16초 | 2026-09-27 | 6. 피아노·클래식·연주곡 |
| [90s Coffee Jazz ☀️ Morning Café Ritual ∣ Smooth J…](https://www.youtube.com/shorts/rP9aLCtUGMM) | FREEDOM MUSIC L… | 7,080 | 622,461 | ×87.92 | 180초 | 2026-07-16 | 4. 카페·매장·라운지 |
| [세월이 훅~ 지나간 흔적! 새벽비 _ 혜은이 #7080 #추억소환 #세련미](https://www.youtube.com/shorts/amCIsWqkIq4) | 뮤직 에세이 수필 _ Soo… | 20,900 | 1,820,180 | ×87.09 | 55초 | 2026-06-11 | 9. 가요·발라드·트로트 |
| [🎬:Musafir Cafe Series (2026)💞∣∣ #viral #love #mus…](https://www.youtube.com/shorts/dqhg5_iVQbM) | Chillwave lofi⚡ | 10,900 | 758,752 | ×69.61 | 16초 | 2026-09-11 | 4. 카페·매장·라운지 |
| [Top 10 Most Viewed Sai Abhyankkar Songs on YouTub…](https://www.youtube.com/shorts/fmms0jbqSUM) | Aura Cinefy | 6,090 | 349,324 | ×57.36 | 46초 | 2026-08-04 | 기타 |
| [🌿우연히 들었는데...첫 소절부터 너무 좋은 가을에 듣기 좋은 노래 ∣ 7080 추억의 …](https://www.youtube.com/shorts/jOuzt9dUHlQ) | Oldies Salon | 1,050 | 58,778 | ×55.98 | 51초 | 2026-09-11 | 9. 가요·발라드·트로트 |
| [528Hz + 432Hz • Fall Into Deep Healing Sleep • An…](https://www.youtube.com/shorts/CHYYnlkVr0M) | Spiritual Heali… | 3,650 | 183,843 | ×50.37 | 174초 | 2026-09-19 | 1. 수면·명상·힐링 |
| [Nonstop Pinoy Reggae 2026🌴🎶 ∣ May Pag-Asa, Tuloy …](https://www.youtube.com/shorts/q8eEnsgaqIw) | SoundTrip | 7,250 | 311,211 | ×42.93 | 180초 | 2026-09-10 | 8. 로파이·시티팝·칠 |
| [RANKING ALL SONGS FROM HANUMAN ANSH ∣ BEST SONGS](https://www.youtube.com/shorts/XHPekcmMajA) | Tune ladder | 23,800 | 939,778 | ×39.49 | 55초 | 2026-09-13 | 기타 |
| [ARJN, KDS, Fifty4, Shreya Ghoshal - Kalyani (Remi…](https://www.youtube.com/shorts/fsZwF4IlhfA) | Lyrics Corner | 7,120 | 255,289 | ×35.86 | 50초 | 2026-08-23 | 기타 |
| [Aisa Bhi Kya Re ∣ Mann Mera - Gajendra Verma ∣ Ae…](https://www.youtube.com/shorts/uBbmdQH_9aE) | HarmonicVibez | 48,100 | 1,669,734 | ×34.71 | 22초 | 2026-05-17 | 12. 커버·노래 부르기 |
| [Mera Dil Yeh Pukare Aaja ∣ Baba Mudassar 🇵🇰 vs An…](https://www.youtube.com/shorts/mrGeXj2vrIQ) | SK facts YT | 10,700 | 370,046 | ×34.58 | 50초 | 2026-09-04 | 기타 |

## 2. 주제 묶음 · 형식 (비교 집단 성공 비율 · 성공 쇼츠 몫)

| 주제 묶음 | 비교 집단 (성공 비율) | 조회수 중앙값 | 하루 조회수 중앙값 | 성공 쇼츠 # |
|---|---|---|---|---|
| 기타 | 172 (19%) | 9,965.5 | 565.2 | 3, 10, 11, 14, 15, 23, 27, 28, 35, 37, 38, 41, 47, 48, 49 |
| 6. 피아노·클래식·연주곡 | 93 (12%) | 3,021 | 200.6 | 6, 8, 9, 13, 18, 22, 26, 39, 43, 58, 62, 85, 91, 93, 104 |
| 1. 수면·명상·힐링 | 149 (8.1%) | 2,697 | 92.8 | 1, 2, 24, 30, 31, 33, 36, 44, 50, 55, 61, 67, 69, 70, 77 |
| 8. 로파이·시티팝·칠 | 26 (7.7%) | 2,917.0 | 230.1 | 16, 17, 19, 25, 32, 34 |
| 12. 커버·노래 부르기 | 16 (6.2%) | 1,594.5 | 113.1 | 12 |
| 9. 가요·발라드·트로트 | 56 (3.6%) | 1,958.5 | 178.2 | 20, 45, 51, 57, 80, 106 |
| 4. 카페·매장·라운지 | 61 (3.3%) | 2,737 | 37.8 | 21, 29, 46, 60, 71, 72 |
| 3. 공부·집중·작업 | 60 (1.7%) | 1,713.5 | 22.6 | 68 |
| 2. 자연 소리·백색소음 | 17 (0%) | 1,950 | 37.2 | 5, 7 |
| 13. OST·사운드트랙 | 1 (100%) (표본 적음) | 75,635 | 639.4 | 75 |
| 7. 재즈·보사노바 | 5 (40%) (표본 적음) | 25,346 | 313.8 | 40 |
| 15. CCM·찬양·국악·동요 | 12 (17%) (표본 적음) | 11,782.5 | 162.8 | 82, 99, 107 |
| 5. 운동·드라이브·신나는 | 5 (0%) (표본 적음) | 6,325 | 1,170.1 | 90 |
| 10. 팝송·K팝·J팝 | 12 (0%) (표본 적음) | 1,757.5 | 12.4 | 42, 76 |
| 11. 힙합·R&B·EDM | 13 (0%) (표본 적음) | 1,962 | 17.2 | – |
| 14. AI 음악 | 3 (0%) (표본 적음) | 4,928 | 36.9 | 4 |

| 형식 | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 몫 | 성공 쇼츠 # |
|---|---|---|---|---|
| 클립·발췌 (방송·무대·직캠) | 25 (16%) | 134.3 | 4.6% | 10, 14, 29, 46, 76 |
| 연주 (직접 연주) | 116 (12%) | 213.6 | 21% | 8, 9, 13, 22, 26, 33, 36, 44, 45, 58, 61, 62, 69, 72, 78 |
| 그 밖 | 263 (11%) | 135.8 | 41% | 1, 2, 3, 5, 6, 7, 15, 16, 17, 19, 21, 23, 24, 30, 31 |
| 한 곡 일부 (음원·뮤비·가사·티저) | 103 (9.7%) | 379.8 | 12% | 11, 18, 27, 28, 35, 47, 49, 52, 57, 59, 65, 92, 106 |
| 추천·모음 (N곡·순위·플리) | 146 (6.8%) | 64.8 | 15% | 20, 25, 32, 34, 41, 60, 63, 66, 73, 75, 79, 80, 84, 97, 102 |
| 커버·직접 부른 노래 | 36 (2.8%) | 84.8 | 3.7% | 12, 42, 51, 71 |
| AI 음악 | 12 (0%) (표본 적음) | 31.0 | 2.8% | 4, 55, 67 |

## 3. 수요와 공급 (최근 90일 쇼츠 434개 — 쇼츠 검색으로 찾은 것, 채널 크기 상관없음)

지수 = 하루 조회수 몫 ÷ 쇼츠 수 몫 (1 보다 크면 쇼츠 하나가 평균보다 많이 봄 = 공급이 모자라 보임)

| 주제 묶음 | 쇼츠 | 채널 | 수요 몫 | 공급 몫 | 지수 | 하루 조회수 중앙값 |
|---|---|---|---|---|---|---|
| 6. 피아노·클래식·연주곡 | 59 | 46 | 50% | 14% | **3.71** | 53,922.2 |
| 기타 | 65 | 57 | 26% | 15% | **1.76** | 35,124.9 |
| 9. 가요·발라드·트로트 | 44 | 29 | 3.8% | 10% | **0.38** | 2,257.2 |
| 3. 공부·집중·작업 | 41 | 37 | 2.4% | 9.4% | **0.25** | 95.0 |
| 7. 재즈·보사노바 | 19 | 2 | 0.5% | 4.4% | **0.12** | 2,714.4 |
| 1. 수면·명상·힐링 | 141 | 58 | 3.2% | 32% | **0.1** | 387.6 |
| 4. 카페·매장·라운지 | 31 | 20 | 0.4% | 7.1% | **0.05** | 125.4 |
| 8. 로파이·시티팝·칠 | 11 | 9 | 7.9% | 2.5% | **3.13** (표본 적음) | 42,028.2 |
| 12. 커버·노래 부르기 | 8 | 7 | 2.7% | 1.8% | **1.44** (표본 적음) | 27,357.0 |
| 2. 자연 소리·백색소음 | 5 | 4 | 1.3% | 1.2% | **1.14** (표본 적음) | 95.4 |
| 10. 팝송·K팝·J팝 | 6 | 4 | 1.0% | 1.4% | **0.69** (표본 적음) | 7,823.6 |
| 5. 운동·드라이브·신나는 | 1 | 1 | 0% | 0.2% | **0.05** (표본 적음) | 2,375.4 |
| 15. CCM·찬양·국악·동요 | 2 | 2 | 0% | 0.5% | **0.01** (표본 적음) | 606.0 |
| 11. 힙합·R&B·EDM | 1 | 1 | 0% | 0.2% | **0.0** (표본 적음) | 17.3 |

검색어별 (쇼츠 검색 — videoDuration=short, 조회수 순 50개):

| 검색어 | 찾음 | 그중 쇼츠 | 결과 수(4분 미만 추정) | 최근 30일 | 조회수 중앙값 | 하루 조회수 중앙값 | 큰 채널 몫 | 작은 채널 성공 | 지금 검색어 |
|---|---|---|---|---|---|---|---|---|---|
| chill music | 50 | 8 (16%) | 1,000,000 | 0 | 1,077,159.5 | 11,819.9 | 0% | 4/4 | ○ |
| 카페음악 | 50 | 16 (32%) | 1,000,000 | 2 | 98,618.5 | 2,158.9 | 7.1% | 12/13 | ○ |
| 힐링음악 | 50 | 21 (42%) | 610,205 | 0 | 582,149 | 4,744.3 | 15% | 11/11 | ○ |
| deep sleep music | 50 | 7 (14%) | 1,000,000 | 1 | 578,863.0 | 6,986.1 | 17% | 5/5 | ○ |
| relaxing piano | 50 | 27 (54%) | 807,686 | 5 | 292,715 | 6,454.4 | 14% | 16/18 | ○ |
| relaxing piano music | 50 | 25 (50%) | 1,000,000 | 9 | 119,985 | 7,938.2 | 12% | 12/15 | ○ |
| stress relief music | 50 | 27 (54%) | 408,242 | 2 | 371,289 | 6,069.4 | 40% | 15/15 | ○ |
| soothing music | 50 | 32 (64%) | 1,000,000 | 2 | 1,039,380.5 | 15,848.0 | 41% | 19/19 | ○ |
| work music | 50 | 24 (48%) | 1,000,000 | 2 | 1,282,130 | 41,205.9 | 44% | 5/5 | ○ |
| Sleep Music | 50 | 3 (6.0%) | 1,000,000 | 0 | 14,328,930.0 | 100,160.6 | 50% | 1/1 | ○ |
| cafe music | 50 | 7 (14%) | 1,000,000 | 0 | 2,728,694.0 | 36,635.6 | 50% | 2/2 | ○ |
| calming music | 50 | 11 (22%) | 1,000,000 | 0 | 1,051,952.5 | 13,683.5 | 50% | 4/4 | ○ |
| 노래 | 50 | 23 (46%) | 1,000,000 | 1 | 13,045,647 | 127,837.4 | 57% | 3/3 | ○ |
| relaxation music | 50 | 8 (16%) | 1,000,000 | 0 | 1,017,804 | 13,202.0 | 57% | 3/3 | ○ |
| 명상음악 | 50 | 41 (82%) | 354,598 | 2 | 48,678.5 | 490.1 | 12% | 15/35 | ○ |
| 플레이리스트 | 50 | 16 (32%) | 1,000,000 | 6 | 158,547 | 16,616.4 | 55% | 4/5 | ○ |
| RelaxingMusic | 50 | 44 (88%) | 1,000,000 | 5 | 290,120.5 | 5,507.9 | 64% | 15/15 | ○ |
| peaceful music | 50 | 18 (36%) | 1,000,000 | 0 | 1,125,563 | 18,050.2 | 67% | 5/5 | ○ |
| BGM | 50 | 38 (76%) | 1,000,000 | 1 | 6,139,593.5 | 58,303.4 | 70% | 3/3 | ○ |
| ambient music | 50 | 15 (30%) | 1,000,000 | 4 | 223,082.0 | 12,806.6 | 70% | 3/3 | ○ |
| 편안한음악 | 50 | 33 (66%) | 199,263 | 8 | 17,949.5 | 363.6 | 3.3% | 8/29 | ○ |
| background music | 50 | 28 (56%) | 1,000,000 | 1 | 2,466,030.0 | 43,499.8 | 75% | 2/2 | ○ |
| calm music | 50 | 12 (24%) | 1,000,000 | 1 | 1,264,108.0 | 15,654.2 | 75% | 2/2 | ○ |
| MeditationMusic | 50 | 48 (96%) | 446,004 | 1 | 228,256 | 3,962.2 | 76% | 5/5 | ○ |
| 잔잔한음악 | 50 | 34 (68%) | 307,826 | 5 | 11,845 | 84.2 | 3.0% | 7/32 | ○ |
| 감성음악 | 50 | 29 (58%) | 1,000,000 | 4 | 448,775.0 | 5,035.1 | 81% | 5/5 | ○ |
| study music | 50 | 23 (46%) | 1,000,000 | 3 | 985,441 | 35,616.8 | 87% | 2/2 | ○ |
| 발라드 | 50 | 38 (76%) | 1,000,000 | 1 | 2,260,615.5 | 41,439.4 | 88% | 1/1 | ○ |
| 피아노 | 50 | 50 (100%) | 1,000,000 | 2 | 10,309,960.5 | 125,418.1 | 92% | 3/3 | ○ |
| 음악 | 50 | 28 (56%) | 1,000,000 | 1 | 5,271,679.0 | 101,965.1 | 92% | 1/1 | ○ |
| 수면 명상 | 50 | 45 (90%) | 114,521 | 1 | 7,753.5 | 118.0 | 12% | 2/21 | ○ |
| lofi | 50 | 19 (38%) | 1,000,000 | 1 | 2,096,342 | 32,749.4 | 92% | 1/1 | ○ |
| 감성발라드 | 50 | 26 (52%) | 677,280 | 1 | 72,097 | 606.0 | 62% | 1/5 | ○ |
| pianomusic | 50 | 44 (88%) | 1,000,000 | 0 | 3,874,282.0 | 39,130.2 | 93% | 2/2 | ○ |
| piano | 50 | 43 (86%) | 1,000,000 | 2 | 16,386,559.5 | 180,880.7 | 94% | 2/2 | ○ |
| instrumental music | 50 | 25 (50%) | 1,000,000 | 2 | 3,630,124 | 43,080.5 | 94% | 1/1 | ○ |
| healingmusic | 50 | 39 (78%) | 334,374 | 9 | 5,819 | 141.6 | 46% | 2/20 | ○ |
| 마음이편안해지는음악 | 50 | 41 (82%) | 52,297 | 3 | 2,946.5 | 22.2 | 5.0% | 2/38 | ○ |
| 집중음악 | 50 | 37 (74%) | 399,799 | 5 | 1,368.5 | 12.4 | 2.8% | 1/35 | ○ |
| 휴식음악 | 50 | 41 (82%) | 395,130 | 11 | 1,594 | 40.7 | 0% | 1/39 | ○ |
| music | 50 | 6 (12%) | 1,000,000 | 0 | 52,663,689 | 546,799.7 | 100% | 0/0 | ○ |
| playlist | 50 | 7 (14%) | 1,000,000 | 0 | 12,298,514 | 115,224.5 | 100% | 0/0 | ○ |
| 트로트 | 50 | 30 (60%) | 1,000,000 | 0 | 4,053,689 | 40,163.6 | 100% | 0/0 | ○ |
| 플리 | 50 | 30 (60%) | 1,000,000 | 0 | 1,999,517 | 32,852.6 | 100% | 0/0 | ○ |
| 노래모음 | 50 | 17 (34%) | 1,000,000 | 0 | 3,582,915.5 | 20,855.8 | 100% | 0/0 | ○ |
| yoga music | 50 | 20 (40%) | 1,000,000 | 1 | 499,046 | 4,711.3 | 100% | 0/0 | ○ |
| focus music | 50 | 14 (28%) | 1,000,000 | 3 | 12,900.0 | 197.2 | 50% | 0/4 | ○ |
| 공부음악 | 50 | 28 (56%) | 772,040 | 10 | 1,502 | 52.3 | 0% | 0/21 | ○ |
| 수면유도음악 | 50 | 34 (68%) | 45,367 | 10 | 1,833 | 51.8 | 3.2% | 0/30 | ○ |
| 잠잘때 듣는 | 50 | 37 (74%) | 91,614 | 0 | 4,190 | 33.3 | 0% | 0/3 | ○ |

사람들이 찾는 말(YouTube 자동완성) 중 최근 쇼츠가 적은 말 — 틈 = 자동완성 점수 ÷ (1 + 최근 쇼츠 수), 전체 541개 중 위 30개 · 뺀 것: 실시간·전망 등 12, 채널 이름 20

| 말 | 자동완성 점수 | 씨앗 검색어 | 최근 쇼츠 | 하루 조회수 중앙값 | 틈 |
|---|---|---|---|---|---|
| meditation music for positive… | 1.8 | meditation music, MeditationM… | 0 | – | 1.8 |
| healing music kks | 1.8 | healing music, healingmusic | 0 | – | 1.8 |
| piano music bros | 1.8 | piano music, pianomusic | 0 | – | 1.8 |
| bgm 모음 | 1.8 | bgm, BGM | 0 | – | 1.8 |
| 수면음악 3시간 | 1.7 | 수면음악, 숙면음악 | 0 | – | 1.7 |
| meditation music no ads | 1.6 | meditation music, MeditationM… | 0 | – | 1.6 |
| healing music studio | 1.6 | healing music, healingmusic | 0 | – | 1.6 |
| piano music for studying | 1.6 | piano music, pianomusic | 0 | – | 1.6 |
| bgm 무료 | 1.6 | bgm, BGM | 0 | – | 1.6 |
| 수면음악 지브리 | 1.4 | 수면음악, 숙면음악 | 0 | – | 1.4 |
| meditation music 20 minutes | 1.4 | meditation music, MeditationM… | 0 | – | 1.4 |
| bgmer awaken | 1.4 | bgm, BGM | 0 | – | 1.4 |
| 수면음악 10분 | 1.2 | 수면음악, 숙면음악 | 0 | – | 1.2 |
| meditation music 5 minutes | 1.2 | meditation music, MeditationM… | 0 | – | 1.2 |
| healing music cafe | 1.2 | healing music, healingmusic | 0 | – | 1.2 |
| sleep music live | 1.2 | sleep music, Sleep Music | 0 | – | 1.2 |
| relaxing piano music for sleep | 1.2 | relaxing piano music, relaxin… | 0 | – | 1.2 |
| piano music bros chopin | 1.1 | piano music, pianomusic | 0 | – | 1.1 |
| bgm 추천 | 1.1 | bgm, BGM | 0 | – | 1.1 |
| 수면음악 클래식 | 1.0 | 수면음악, 숙면음악 | 0 | – | 1.0 |
| healing music playlist | 1.0 | healing music, healingmusic | 0 | – | 1.0 |
| sleep music playlist | 1.0 | sleep music, Sleep Music | 0 | – | 1.0 |
| piano man | 1.0 | piano | 0 | – | 1.0 |
| peaceful music for studying | 1.0 | peaceful music | 0 | – | 1.0 |
| 힐링음악 피아노 | 0.9 | 힐링음악 | 0 | – | 0.9 |
| 명상음악 5분 | 0.9 | 명상음악 | 0 | – | 0.9 |
| sleep music dark screen | 0.9 | sleep music | 0 | – | 0.9 |
| deep sleep music live | 0.9 | deep sleep music | 0 | – | 0.9 |
| 자장가동화 | 0.9 | 자장가 | 0 | – | 0.9 |
| 수면유도음악 4시간 | 0.9 | 수면유도음악 | 0 | – | 0.9 |

## 4. 제목 · 해시태그 (비교 집단)

| 제목 특징 | 있음 (성공 비율) | 없음 | 차이 | 성공 쇼츠 몫 |
|---|---|---|---|---|
| 25자 미만 | 49 (22%) | 652 (8.9%) | +14% ⚑ | 7.4% |
| vs 비교 | 10 (20%) | 691 (9.7%) | +10% (표본 적음) | 0.9% |
| 패턴형(공통점·특징·이유·N가지·착각·과정) | 8 (0%) | 693 (10%) | -10% (표본 적음) | 0% |
| 이유 | 8 (0%) | 693 (10%) | -10% (표본 적음) | 0% |
| 과정·벌어진 일·결말·결국 | 1 (0%) | 700 (9.9%) | -10% (표본 적음) | 0% |
| 손실 낱말(망하·날린·잃은·반토막) | 1 (0%) | 700 (9.9%) | -10% (표본 적음) | 0% |
| 직접·해보니·N년 기록 | 6 (0%) | 695 (9.9%) | -10% (표본 적음) | 0% |
| S&P500·ETF·지수·나스닥 | 1 (0%) | 700 (9.9%) | -10% (표본 적음) | 0% |
| 빚투·신용·미수·레버리지·대출 | 1 (0%) | 700 (9.9%) | -10% (표본 적음) | 0% |
| 물음표 ? | 18 (17%) | 683 (9.7%) | +7.0% | 2.8% |
| 말줄임 …·... | 16 (6.2%) | 685 (9.9%) | -4% | 3.7% |
| 40자 이상 | 560 (9.1%) | 141 (13%) | -4% | 83% |
| '#shorts' 표시 | 116 (6.9%) | 585 (10%) | -4% | 13% |
| 숫자가 들어감 | 186 (11%) | 515 (9.3%) | +2.0% | 22% |
| AI | 63 (11%) | 638 (9.7%) | +1.4% | 6.5% |
| 따옴표·괄호로 강조 | 89 (9.0%) | 612 (10%) | -1% | 13% |
| 구분 기호(ㅣ·｜·/)로 나눔 | 290 (10%) | 411 (9.5%) | +0.8% | 44% |
| 느낌표 ! | 30 (10%) | 671 (9.8%) | +0.2% | 1.9% |

성공 비율이 높은 제목 낱말: 노래 (53 (21%) vs 9.0% ⚑), Relaxing (24 (21%) vs 9.5% ⚑), Sleep (33 (18%) vs 9.4%), Lyrics (30 (17%) vs 9.5%), song (45 (13%) vs 9.6%), Deep (39 (13%) vs 9.7%), relaxingmusic (26 (12%) vs 9.8%), Aesthetic (27 (11%) vs 9.8%), love (27 (11%) vs 9.8%)

성공 비율이 낮은 제목 낱말: 음악 (72 (0%) vs 11%), 노동요 (38 (0%) vs 10%), 카페음악 (36 (0%) vs 10%), 좋은 (39 (0%) vs 10%), 편안해지 (31 (0%) vs 10%), 감성 (31 (0%) vs 10%), 가을 (28 (0%) vs 10%), 매장음악 (28 (0%) vs 10%), 카페 (34 (0%) vs 10%), 듣기 (32 (0%) vs 10%)

| 제목 길이 | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 # |
|---|---|---|---|
| 20자 미만 | 24 (29%) | 234.8 | 9, 44, 75, 95, 105 |
| 20~29자 | 50 (14%) | 108.6 | 10, 14, 24, 26, 57, 66, 79 |
| 30~39자 | 67 (6.0%) | 85.6 | 43, 45, 65, 68, 71, 81 |
| 40자 이상 | 560 (9.1%) | 162.5 | 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 15, 16, 17, 18 |

| 해시태그 수 (제목+설명) | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 # |
|---|---|---|---|
| 해시태그 없음 | 44 (20%) | 220.9 | 6, 10, 14, 21, 69, 72, 75 |
| 1~2개 | 36 (11%) | 135.2 | 8, 85, 89 |
| 3~5개 | 120 (10%) | 96.2 | 1, 3, 4, 9, 13, 25, 26, 34, 39, 43, 48, 58, 63, 66, 73 |
| 6개 이상 | 501 (8.8%) | 159.5 | 2, 5, 7, 11, 12, 15, 16, 17, 18, 19, 20, 22, 23, 24, 27 |

많이 쓴 해시태그 (비교 집단 쇼츠 수 · 그 쇼츠의 성공 비율 · 성공 쇼츠 수): #shorts 208 (12%·32), #relaxingmusic 136 (12%·33), #힐링음악 112 (3.6%·20), #music 79 (8.9%·13), #카페음악 72 (0%·7), #플레이리스트 54 (1.9%·1), #song 51 (5.9%·9), #healingmusic 49 (0%·5), #youtubeshorts 48 (15%·7), #trending 46 (20%·13), #명상음악 43 (2.3%·9), #수면음악 43 (0%·3), #meditationmusic 42 (9.5%·13), #lyrics 41 (9.8%·6), #playlist 41 (2.4%·3), #cafemusic 40 (0%·4), #감성음악 38 (0%·4), #매장음악 37 (0%·2), #stressrelief 36 (11%·11), #love 34 (8.8%·8), #노동요 34 (0%·0), #집중음악 32 (0%·0), #viral 31 (13%·5), #sleepmusic 31 (13%·11), #감성팝송 30 (0%·3)

## 5. 길이 (초)

- 중앙값: 성공 쇼츠 39초 · 비교 집단 성공 36초 · 나머지 41초

| 길이 | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 # |
|---|---|---|---|
| 0~14초 | 50 (12%) | 554.2 | 1, 5, 26, 27, 28, 29, 35, 46, 53, 65, 88, 95, 98 |
| 15~29초 | 157 (15%) | 294.8 | 2, 4, 6, 7, 11, 13, 15, 18, 19, 22, 24, 48, 49, 52, 54 |
| 30~44초 | 176 (6.2%) | 65.6 | 3, 8, 16, 17, 21, 25, 30, 34, 38, 39, 41, 45, 50, 56, 63 |
| 45~59초 | 114 (13%) | 138.3 | 9, 10, 12, 14, 20, 23, 42, 43, 47, 60, 71, 80, 89, 97, 103 |
| 60~89초 | 92 (6.5%) | 88.8 | 33, 36, 44, 55, 57, 61, 69, 83, 100, 102 |
| 90~180초 | 112 (6.2%) | 130.7 | 31, 32, 37, 40, 51, 62, 64, 67, 70, 72, 77, 78, 81, 85, 90 |

### 5-2. 아주 짧은 쇼츠 (15초 미만 — 한 장 정보·반복 재생형?) — 주제 관련 쇼츠 전부 (조회수 부풀림 의심 포함)

조회수는 2025-03-31 부터 다시 재생도 셈 → 아주 짧은 쇼츠는 한 사람이 여러 번 셀 수 있다. 광고로 산 조회수와 API 로 가를 수 없다

| 묶음 | 쇼츠 | 그중 부풀림 의심 | 채널 | 조회수 중앙값 | 좋아요/1천 | 길이 중앙값 |
|---|---|---|---|---|---|---|
| 15초 미만 | 385 | 35 | 76 | 27,657 | 7.8 | 11초 |
| 15초 이상 | 3474 | 42 | 475 | 7,568.0 | 13.6 | 50초 |

15초 미만 쇼츠 (조회수 순):

- 11초 · 30,605,417회 · 좋아요/1천 7.5 · 구독자 543,000 · Muso Method Ped… — Can you play PERFECT time? 🤯🎹 #piano #pianoteacher #pianolessons #cla… (https://www.youtube.com/shorts/9jbrElKajNo)
- 7초 · 29,257,755회 · 좋아요/1천 1.72 · 구독자 2,740 · ChauBeo · 부풀림 의심 — Submit your funny videos if you need background music!#trend #funny #… (https://www.youtube.com/shorts/ZhUWXhYqV6g)
- 12초 · 26,002,192회 · 좋아요/1천 0.0 · 구독자 65,900 · Asthetic_Lyrics — Misery ∣ Puppies Lyrics Edit Asthetic Theme Soul soothing Sound. (https://www.youtube.com/shorts/idTjtnPe5cM)
- 12초 · 25,697,937회 · 좋아요/1천 3.63 · 구독자 206,000 · SmartBaby — She took her first piano lesson WAY too seriously! 🎹 🤣 (https://www.youtube.com/shorts/-pS0IVbmcZo)
- 12초 · 25,628,478회 · 좋아요/1천 3.5 · 구독자 13,600 · NOVAE — I know I should sleep, but the voices in my head go… Arirang tour ver… (https://www.youtube.com/shorts/17UP7J8Ri3E)
- 7초 · 13,665,615회 · 좋아요/1천 7.12 · 구독자 107,000 · Leo — Who designed this Oreo?!😳#shorts #funny #memes #piano (https://www.youtube.com/shorts/cqh7psgif6Y)
- 13초 · 12,465,919회 · 좋아요/1천 6.24 · 구독자 225,000 · 살림아리 — 혼자 어떻게 찍냐고? 2탄 (https://www.youtube.com/shorts/-EbDCbATPDk)
- 10초 · 11,091,081회 · 좋아요/1천 19.17 · 구독자 1,980,000 · Matt Storer — Alien meets the President #comedy #music #parody of Work It by Missy … (https://www.youtube.com/shorts/fM71BRVXv1E)
- 14초 · 10,090,992회 · 좋아요/1천 5.08 · 구독자 50,100 · 아쮸 — 음악방송에 카메라 들고 올라간 아이돌 #kpop #shorts (https://www.youtube.com/shorts/Nw6ROTIJSaA)
- 12초 · 5,521,573회 · 좋아요/1천 13.41 · 구독자 100,000 · Maks Rayvan Sho… — Chinese tune #piano #pianist #pianomusic #pianotutorial #shortsviral … (https://www.youtube.com/shorts/4Q-ZlGppJmI)
- 5초 · 5,010,639회 · 좋아요/1천 10.17 · 구독자 53,700 · Lem2Viral — #instrumental (https://www.youtube.com/shorts/NGYAnuzyQFo)
- 4초 · 4,551,666회 · 좋아요/1천 2.08 · 구독자 766,000 · Herlyne Ven 🇨🇦 · 부풀림 의심 — Cute & Fun CoComeon Hippo Piano 🪗 #trending #pianomusic #music #toys … (https://www.youtube.com/shorts/aYxI0o751G0)

## 6. 첫 3초 · 7. 말과 끝맺음 (자료를 받은 쇼츠 — 대본이 있는 것)

성공 쇼츠 108개 (대본 0 · 말 없음 0) vs 나머지 받은 쇼츠 83개 (대본 0 · 말 없음 0) — 중앙값·몫

| 항목 | 성공 쇼츠 | 나머지 받은 쇼츠 |
|---|---|---|
| 첫 말까지 걸린 시간 | –초 | –초 |
| 첫 3초 안 음절 | – | – |
| 말 속도 (음절/초, 말하는 구간) | – | – |
| 말이 차지한 비율 | – | – |
| 자막 줄 수 | – | – |
| 말 없는 쇼츠 (음악·화면 글자만) | 0% | 0% |
| 첫 줄: 질문으로 시작 | – | – |
| 첫 줄: 숫자·금액으로 시작 | – | – |
| 첫 줄: 단정·경고 먼저 | – | – |
| 첫 줄: 반전·의외 | – | – |
| 첫 줄: 시청자 부르기 | – | – |
| 첫 줄: 내 이야기·사연 | – | – |
| 첫 줄: 위 유형 없음 | – | – |
| 끝 줄: 구독·좋아요 부탁 | – | – |
| 끝 줄: 댓글 유도 | – | – |
| 끝 줄: 저장·공유 | – | – |
| 끝 줄: 풀영상·다음 편 안내 | – | – |
| 끝 줄: 질문으로 끝 | – | – |
| 끝 줄: 위 유형 없음 | – | – |
| 끝 줄이 문장 끝맺음(다·요·까…) 없이 끝남 | – | – |

- 설명란에 롱폼·풀영상 연결(유튜브 영상 주소·'풀영상'·'본편'): 성공 쇼츠 3.7% · 나머지 받은 쇼츠 3.6% · 비교 집단 성공 0% · 나머지 7.0%

성공 쇼츠의 첫 줄·끝 줄 (원문):


## 8. 참여율 (조회수 1,000회당 — 중앙값)

| 묶음 | 수 | 좋아요/1천 | 댓글/1천 | 하루 조회수 |
|---|---|---|---|---|
| 비교 집단 성공 | 69 | 8.16 | 0.15 | 10,158.3 |
| 비교 집단 나머지 | 632 | 11.46 | 0.39 | 105.5 |
| 성공 쇼츠 (받은 것) | 108 | 11.23 | 0.16 | 8,605.0 |

## 9. 올린 요일 · 시각 (한국 시간 — 비교 집단, 표본이 작으면 흔들림)

| 요일 | 비교 집단 (성공 비율) | 성공 쇼츠 # |
|---|---|---|
| 월요일 | 117 (6.8%) | 2, 12, 18, 33, 39, 45, 58, 66, 89, 91, 92, 98 |
| 화요일 | 107 (11%) | 4, 11, 27, 31, 34, 44, 46, 48, 56, 62, 63, 65 |
| 수요일 | 84 (8.3%) | 5, 13, 17, 20, 23, 24, 28, 51, 54, 61, 69, 77 |
| 목요일 | 103 (16%) | 7, 9, 15, 21, 25, 29, 38, 40, 55, 57, 59, 64 |
| 금요일 | 81 (9.9%) | 1, 14, 26, 32, 36, 43, 49, 52, 53, 68, 78, 79 |
| 토요일 | 100 (7.0%) | 3, 16, 19, 30, 35, 37, 67, 71, 85, 103 |
| 일요일 | 109 (10%) | 6, 8, 10, 22, 41, 42, 47, 50, 60, 70, 72, 75 |

| 시각 | 비교 집단 (성공 비율) | 성공 쇼츠 # |
|---|---|---|
| 0~5시 | 59 (8.5%) | 1, 4, 8, 31, 41, 55, 60, 65, 70 |
| 6~8시 | 116 (6.9%) | 9, 20, 26, 58, 61, 66, 71, 76, 78, 83, 86, 90 |
| 9~11시 | 98 (12%) | 11, 27, 32, 36, 38, 42, 44, 46, 50, 52, 54, 56 |
| 12~14시 | 80 (11%) | 7, 13, 14, 22, 28, 30, 47, 49, 51, 57, 59, 87 |
| 15~17시 | 86 (5.8%) | 3, 17, 19, 23, 63, 68, 103 |
| 18~20시 | 132 (14%) | 2, 5, 15, 18, 24, 25, 34, 43, 45, 69, 79, 80 |
| 21~23시 | 130 (9.2%) | 6, 10, 12, 16, 21, 29, 33, 35, 37, 39, 40, 48 |

## 10. 채널 유형 · 빨리 크는 쇼츠 채널

채널 유형 = 채널 쇼츠 수(UUSH 목록) ÷ 채널 영상 수. 채널 쇼츠 수를 모르는 비교 집단 쇼츠 282개는 비율에서 뺐다 (평소 쇼츠는 승인한 쇼츠의 채널만 받으므로 모르는 채널은 거의 다 성공이 아님 — 넣으면 '쇼츠만 하는 채널'이 잘 되는 것처럼 보임). 아래도 승인한 쇼츠의 채널 쪽으로 치우쳐 있다

| 채널 유형 | 비교 집단 (성공 비율) | 채널 | 성공 쇼츠 # |
|---|---|---|---|
| 쇼츠만 (90% 이상) | 161 (20%) | 37 | 2, 4, 5, 6, 9, 10, 14, 15, 16, 21, 23, 24 |
| 쇼츠 위주 (50~90%) | 189 (13%) | 40 | 1, 3, 8, 11, 12, 13, 17, 18, 19, 20, 22, 26 |
| 롱폼 위주 (쇼츠 50% 미만) | 69 (14%) | 17 | 7, 25, 31, 34, 37, 55, 61, 62, 64, 65, 67, 68 |

빨리 크는 쇼츠 채널 (개설 24개월 안·구독자 1,000~200,000·쇼츠 몫 50% 이상 — 월 구독자 증가 순, 471곳 중):

| 채널 | 개설 | 구독자 | 월 구독자 증가 | 영상 수 | 쇼츠 몫 | 본 쇼츠 길이 중앙값 | 주로 다룬 주제 | 대표 쇼츠 |
|---|---|---|---|---|---|---|---|---|
| 𝐑𝐚𝐣𝐞𝐬𝐡_𝐞𝐝𝐢𝐭𝐳𝐳 💫 | 2026-07-15 | 138,000 | 42,007 | 144 | – | 16초 | 8. 로파이·시티팝·칠 | [chhoti bhen (lo-fi) song ∣ br…](https://www.youtube.com/shorts/PQD2n5CcoGk) 1,949,427회 |
| veerpulse | 2026-07-28 | 44,600 | 15,605 | 216 | 100% | 6초 | 기타 | [#relaxingmusic](https://www.youtube.com/shorts/p4dSlB1-18k) 512,693회 |
| Jazzy Love Active | 2026-07-24 | 46,400 | 15,521 | 105 | 100% | 20초 | 8. 로파이·시티팝·칠 | [💝 Ishq De Fanniyar ∣ Slowed +…](https://www.youtube.com/shorts/K0dMrCnd5Jw) 18,763,672회 |
| 명곡부활단 | 2026-03-21 | 107,000 | 15,010 | 329 | – | 52초 | 9. 가요·발라드·트로트 | [열애#열애 #윤시내 #추억의명곡 #추억의노래 #감성음…](https://www.youtube.com/shorts/lvEIFwI6VPk) 223,190회 |
| 연예뉴스_TV1 | 2025-12-17 | 130,000 | 12,724 | 416 | – | 62초 | 9. 가요·발라드·트로트 | [#미스터미스터 #뉴스#트로트](https://www.youtube.com/shorts/KSGNJijOoqk) 3,456,245회 |
| Late Hours ∣ Rela… | 2025-12-30 | 121,000 | 12,360 | 223 | – | 31초 | 1. 수면·명상·힐링 | [30s to Perfect Sleep Starts H…](https://www.youtube.com/shorts/w1JbQdML0XE) 60,811회 |
| Cafe Mellow | 2026-04-26 | 65,000 | 10,992 | 345 | – | 175초 | 7. 재즈·보사노바, 3. 공부·집중·작업 | [Soulful Saxophone That Touche…](https://www.youtube.com/shorts/vQE0PJTSWY0) 2,428,006회 |
| 클래식한소절 | 2026-06-15 | 45,800 | 10,724 | 78 | 100% | 34초 | 6. 피아노·클래식·연주곡, 7. 재즈·보… | [아무도 생각 못한 소리로 서부의 아이콘이 된 음악 #…](https://www.youtube.com/shorts/2ZKxQjF1V0I) 5,179,216회 |
| StudySmart with A… | 2025-10-08 | 131,000 | 10,494 | 171 | – | 51초 | 기타 | [Kya Music Sunte Sunte Padhai …](https://www.youtube.com/shorts/lr2FKwb7Sd4) 406,010회 |
| 하루순간 | 2026-05-10 | 55,500 | 10,116 | 188 | – | 8초 | 10. 팝송·K팝·J팝 | [이정도 거리면 해볼만 한데? #jpop](https://www.youtube.com/shorts/LwG3o0PKAww) 1,515,998회 |
| 로드차트 | 2026-02-13 | 81,600 | 9,857 | 242 | – | 61초 | 9. 가요·발라드·트로트 | [밴드 붕괴 직전, 고독이 만든 역대급 록발라드/Alw…](https://www.youtube.com/shorts/1AeJeaZoC3I) 2,564,851회 |
| シャドウビート | 2025-10-29 | 116,000 | 9,808 | 266 | – | 43초 | 11. 힙합·R&B·EDM | [電車が空いてるのに隣に座る男の末路 #パラ高 #LoFi …](https://www.youtube.com/shorts/dsUym1tu7G4) 1,880,190회 |
| Psych Theory | 2026-03-23 | 67,700 | 9,630 | 38 | – | 40초 | 3. 공부·집중·작업 | [3 Music Types That Can Boost …](https://www.youtube.com/shorts/t2cFkPUmTYs) 17,297회 |
| Darky lyrics | 2026-03-28 | 61,700 | 8,944 | 202 | – | 24초 | 6. 피아노·클래식·연주곡 | [Catwoman - Instrumental ∣ Moo…](https://www.youtube.com/shorts/ILcCxODj_eQ) 3,290,058회 |
| 영펭 yeongpin | 2026-06-25 | 35,100 | 8,830 | 111 | 85% | 20초 | 6. 피아노·클래식·연주곡, 1. 수면·명… | [A Dinosaur’s Love Story #pian…](https://www.youtube.com/shorts/imH34A_Y-3I) 17,359,043회 |
| 랭킹감자 | 2025-09-19 | 112,000 | 8,545 | 189 | – | 47초 | 기타 | [음악 전공자들이 노는 법 모음집](https://www.youtube.com/shorts/mVv07KPi1pA) 5,188,893회 |
| Lyric Suman Editz | 2026-01-25 | 73,600 | 8,267 | 152 | – | 16초 | 8. 로파이·시티팝·칠 | [Jeene Laga Hoon 💔 (Slowed + R…](https://www.youtube.com/shorts/L920dSnKVM0) 1,977,342회 |
| unlockroom | 2025-06-26 | 119,000 | 7,469 | 369 | – | 60초 | 기타 | [점점 산으로 간다는 송소희의 음악세계](https://www.youtube.com/shorts/7ihxCzpOwkk) 5,354,465회 |
| 숏플래시 | 2025-11-17 | 79,800 | 7,144 | 625 | – | 28초 | 기타 | [평생 아빠의 플레이리스트만 듣고 자란 딸의 최후](https://www.youtube.com/shorts/TOUASe0Fhvw) 1,890,707회 |
| 나야나클래식 | 2026-01-12 | 66,200 | 7,071 | 324 | – | 53초 | 6. 피아노·클래식·연주곡 | [버려질 뻔한 음악이 영화의 얼굴이 됩니다 #비하인드 …](https://www.youtube.com/shorts/WnXs8FFrXxk) 4,161,674회 |
| Lem2Viral | 2026-03-04 | 53,700 | 7,016 | 558 | – | 5초 | 6. 피아노·클래식·연주곡 | [#instrumental](https://www.youtube.com/shorts/NGYAnuzyQFo) 5,010,639회 |
| 7080 음악 감성트롯 | 2025-10-02 | 89,100 | 7,008 | 659 | – | 58초 | 9. 가요·발라드·트로트 | [혼자 걷던 길도 당신과 함께라면 외롭지 않습니다...…](https://www.youtube.com/shorts/2jKHWmTT7GM) 575,742회 |
| 추억의 음악다방 | 2025-10-21 | 81,800 | 6,766 | 302 | – | 56초 | 9. 가요·발라드·트로트 | [전화 잘못 걸었다고 차마 말을 못해서 나온 레전드 감…](https://www.youtube.com/shorts/-j-BAy76Frc) 82,321회 |
| Janny Love Active | 2026-07-22 | 19,300 | 6,317 | 79 | 100% | 20초 | 8. 로파이·시티팝·칠 | [💝 Ishq De Fanniyar ∣ Slowed +…](https://www.youtube.com/shorts/DF-BBMCHDg8) 3,062,351회 |
| Spreading Carlo's… | 2025-09-08 | 82,000 | 6,073 | 963 | – | 176초 | 1. 수면·명상·힐링 | [Catholic Healing Music For In…](https://www.youtube.com/shorts/NwzFY_3Y2OM) 61,931회 |

## 11. 시청자 니즈 (성공 쇼츠 댓글 — 시청자 댓글 43,956개, 도배 19개 뺌, 채널 주인 댓글 뺌, 정보 요청이 아닌 부탁(띠·로또·노래 등) 0개는 질문·요청에서 뺌)

| 갈래 | 댓글 | 몫 | 좋아요 합 |
|---|---|---|---|
| 좋은 점 — 영상 (도움·설명·정리·공감) | 58 | 0.1% | 7,207 |
| 감사·응원 (일반) | 343 | 0.8% | 1,745 |
| 더 알고 싶은 것 (질문·요청) | 40 | 0.1% | 193 |
| 아쉬운 점 — 영상 (제목·광고·길이·정보 오류·목소리) | 38 | 0.1% | 237 |
| 반박·불만 — 의견 다름 (내용) | 44 | 0.1% | 194 |
| 정치·사회 (영상과 무관한 의견) | 39 | 0.1% | 59,476 |
| 경험 공유 (내 이야기) | 235 | 0.5% | 4,420 |
| 구독·다음 기대 | 8 | 0% | 17 |
| 더 자세히·긴 영상 요청 (풀영상·2탄·자세히) | 32 | 0.1% | 6,262 |

### 11-1. 요청 — '다뤄 주세요·알려 주세요' 16개 (다음 쇼츠·롱폼 주제 후보)

- #22 👍4 “손열음은 집중해서 깊이 들어갈 때 늘 항상 뭐라고 말을 하는것 같은데.... 넘 궁금해요^^ 뭐라고 하는 걸까요?ㅎ”
- #44 👍2 “여기애 나오는 억기즐 전부 다 궁금합니다”
- #51 👍2 “멋진곡 입니다 잘 감상했습니다 계속 올려주세요😊”
- #12 👍1 “노래를 듣고 어떤 생각을 하셨는지, 어떤 마음으로 노래를 부르시는지 궁금합니다🤔”
- #44 👍1 “작곡가 누구신지요? 알고싶어요”
- #51 👍1 “감사합니다 이럭해 예절한 노래을🎉🎉🎉 더조은 만이부탁드려요”
- #9 👍0 “피아노 보다 저거 떨구면 어떻게 될까 궁금해서 봤는데, 속았당.”
- #10 👍0 “보라색 가디건 입으신 여성 분 풀버전 궁금하다 😮”
- #14 👍0 “이런방송 너무좋아 많이 올려주세요 감사합니다❤”
- #14 👍0 “진찌 너무나 좋네요❤❤한국도 이 프로 사와서 방송 해 주세요”
- #45 👍0 “여름비 도 부탁드려요 😂😂”

### 11-2. 더 자세히·긴 영상 요청 (풀영상·2탄·자세히)

- #10 👍5272 “정보) 원본영상은 7만1000조회수 이지만 이 쇼츠는 154만2300조회수 이다”
- #43 👍72 “핸드폰의 순기능 올초 이곡 전체영상 보고 감탄 여자분의 휫파람이 일품”
- #43 👍11 “와. 진짜 잘 만든 음악이네. 자세히 들으니 훨씬 구성이 장난아님이 느껴진다”
- #44 👍9 “이분 이름이 뭘까요? 전체 영상을 보고 싶습니다.”
- #75 👍1 “애원 원본분 맨날 보는 사람으로서 정말 좋은🥰”
- #10 👍0 “풀영상이 시급합니다❤”
- #14 👍0 “봐도봐도 레전드!! 몇번을 보는지 몰라... 이거 풀 영상 없나요?”
- #14 👍0 “풀영상 보고싶네”

### 11-3. 물음표 질문

- #22 👍11 “혹시 이 협주곡은 몇 번일까요?!”
- #100 👍5 “이노래 어떻게 다운받나요?”
- #44 👍3 “전체음악을 어디서 들을수있을까요?”
- #12 👍1 “아파트단지 같은데 유리창 하나 두고 혹시 방음이 되나요? 노래는 잘 들었습니다”
- #44 👍1 “이건어느나라인가요????”
- #76 👍1 “이노래 풀버전 어떻게 듣나요?”
- #14 👍0 “풀 영상 어디서 보나요?😅”
- #14 👍0 “어디서 볼수 있나요?”
- #22 👍0 “그대의 아름다움을 어떻게 표현 해야 할까요? 그냥 ….. 귀만 열어 두고 있기가 송구 할 뿐 …”
- #43 👍0 “황야의 무법자 장고 햇갈리네요 장고 맞나요?”
- #43 👍0 “서부 영화와 이렇게 잘 어울리는 음악이 있을까요? 리반클리프,클린트이스트우드도 최고였는데...”
- #45 👍0 “펨풀륫은 루마니아가 아니라 아메리카 원주민 고유악기입니다. 원조라고 할수있겠습니다. 그런데요, 아메리카 원주민(인디언)은 어디서왔을까요? 명백한 동양인이고 동양인 조상은 고려입니다. 참역사적 팩트입니다.”
- #45 👍0 “비교적 최근에 어디서 들었지 했는데 영화 킬빌에도 나오지 않나요?”
- #68 👍0 “선생님~~이노래 악보 구할 수 있을까요?”
- #68 👍0 “안녕하세요 혹시 이 음악 악보도 있을까요??”

### 11-4. 아쉬운 점 — 영상

- #10 👍115 “​@j43nfromss ㅋㅋㅋㅋㅋ ㅈㄴ 호들갑 떠는 자막이랑 출연진 하나하나 클로즈업하면서 계속 반복하는 연출ㅋㅋㅋㅋㅋㅋㅋ 진짜 채널 바로 돌려버림ㅋㅋㅋ”
- #14 👍29 “​@sonhj3949그러기엔 그냥 예능도 무한반복인디”
- #43 👍24 “방갤리스. 엔리오모리꼬네. 이 두분 음악만 남은 인생 평생 들어도 인생이 지루하지 않을것같음.”
- #64 👍20 “정말 스님입니까? 아님 AI목소리 인가요~~넘 잘부르시네요??목소리도 좋고요 감사합니다 잘듣고 갑니다~”
- #10 👍18 “ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ진짜 제발 편집방식 좀 바꿔 같은 장면 반복해서 보여주는 거 누가 먼저 시작했냐”
- #68 👍10 “선생님 안녕하세요.저 주은이에요. 아이들 목소리가 너무 귀여워요.”
- #14 👍7 “인정 ㅋㅋㅋㅋㅋㅋ 게스트 반응 관심 ㅈ도 없는데 자꾸 게스트만 두 세 번 쳐 반복해서 보여줌”
- #80 👍3 “넘 복스럽고 넘 좋아했는데 넘 아쉽네요❤❤”
- #6 👍1 “​@twosoul_real 댓글에 틀린 정보가 많네요”
- #9 👍1 “마지막 댓 ai 같노”
- #45 👍1 “지금 이 지휘자가 병원에 입원했다고 해서 마음이... 세월이 아쉽네요”
- #6 👍0 “아 이거 full reaction 뭐 그런건 줄 알았더니 look at ya 반복이네.”
- #9 👍0 “화질만 봐도 ai”
- #22 👍0 “손열음 이란 피아니스트 유투브 영상으로 첨봤는데 유명하단 피아니스트 좀지루한면 있어서 별흥미를 못느꼈는데 신기하고 겨ㅣ속 보고싶네요”
- #22 👍0 “피아노 소리는 밴드였을때가 멋지지 지루한 클래식”

### 11-x. 좋은 점 — 영상 (도움·설명·정리·공감)

- #10 👍5158 “3번째분 스페이스할때 듣기좋다”
- #14 👍1516 “이거뭔가 묘한게..뚱딴지같이 노래보다 더 먼저 와닿는게 삶은 이렇게 살아야겠다 라는게 느껴짐 어두워도 언제빛을 볼지 모른다는 마음으로 준비하고, 기회가 왔을때 힘껏 내가가진 기량를 펼친뒤 타인에게도 그 기회가 돌아갔을때 최선을 다해 박수쳐주는거. 이…”
- #63 👍334 “이성경이 젤 듣기좋다;;”
- #10 👍36 “3번째가 진짜 레전드네”
- #43 👍19 “휘파람 소리가 진짜 레전드 지~”
- #12 👍11 “커버중에 가장 듣기 좋습니다”
- #57 👍9 “청아한 목소리로 한이 실린 가사를 한올 한올 풀듯이 엮어내는 소리는 만인의 심금을 울려 줍니다 좋은영상 감사드립니다 구독과 좋아요 누르고 갑니다”
- #94 👍8 “감사합니다 감사합니다 넘좋아 요가슴애 와닿는 것이 눈물이나 네요 감 사합니다 성불하십시요 ❤❤❤❤❤❤❤”

### 11-x. 경험 공유 (내 이야기)

- #14 👍1516 “이거뭔가 묘한게..뚱딴지같이 노래보다 더 먼저 와닿는게 삶은 이렇게 살아야겠다 라는게 느껴짐 어두워도 언제빛을 볼지 모른다는 마음으로 준비하고, 기회가 왔을때 힘껏 내가가진 기량를 펼친뒤 타인에게도 그 기회가 돌아갔을때 최선을 다해 박수쳐주는거. 이…”
- #43 👍814 “어릴때 저음악을 내 입으로 와와와 했었는데, 정말 입소리였구나..”
- #63 👍307 “이성경이 왜 제일좋은가 생각해봤더니 노래 자체가 뮤지컬이랑 어울려서 그런듯”
- #43 👍266 “기타소리 시작될 때 나도 모르게 "크으...!" 감탄함”
- #6 👍67 “내가 항상 카니에 음악을 초창기부터 들으면서 느낀 부분은 트렌드를 선구하기도 하고 앞서간 뮤지션이라고 늘 생각했음. 천재들중 천재라고 생각함. 거기다가 실행력 및 도전정신까지..... 대단한 사람임”
- #45 👍26 “눈물 나도록 환상 입니다”
- #45 👍19 “내가 세상을 떠나고 흙으로 돌아가도 이 음악은 새로운 사람들에게 감동을 줄겁니다. 그래서 음악이 존경스러워요....”
- #81 👍11 “관세음보살 관세응보살 관세음보살 우리엄마 어기까지만 아프고 더이상은 아프지마시길 ()()() 우리아버지도 더이상은 아프지마시길 ()()() 우리 부모님 사랑합니다♡♡♡”

### 11-x. 구독·다음 기대

- #45 👍12 “잠안올때 들어면 너무좋은 명곡연주입니다..외로운 양치기 팬입니다😊😊🎉🎉”
- #12 👍1 “와진짜 미쳤다 .. 소름돋을정도로 잘하셔서 듣고 구독했어요ㅠㅜㅜㅜ 초반부분에 반가성? 어떻게 내시는건가요,, ??!?!”
- #43 👍1 “와우~어릴적 재밌게 보던 토요명화 생각납니다 그때는 서부영화들 정말 기다리며 보았지요 이 음악이 이렇게 만들어졌다니 신기하고 놀라워요^^ 구독합니다 🍂”
- #44 👍1 “고등학교 다닐때 중앙대다니던 대학생오빠가 매일듣던곡인데 벌써 40년전이네. 내가 제목이 뭐냐고묻자 엘콘돌파사 라고.”
- #51 👍1 “한쪽 가슴이 찡하고 아려요 아파요 진심으로 부르는 모습에 감동을 받고 힘찬박수 보냅니다 방금 구독완료 하였습니다 열렬히 응원합니다”
- #75 👍1 “애원이랑 너와나이랑 증오의 창조물 내가 엄청좋아하는 lms인데 감사해요 너무 잘만드셨어요 구독 좋아요 알림설정하고갈께요 🎉”
- #6 👍0 “좋은 노래 네요. 같이 공유하고 싶어서 구독했어요. 대단해요❤❤”
- #14 👍0 “한국에서도 이런 프로했으면 좋겠습니다 아마추어들로 진짜 가수말구요 대박날듯 기대됩니다 노래 실력들이 다 좋아서 보는 재미가 있네요 멋져!!!”

## 12. 사례별 · 표지

사례별 (대본 전문·첫 3초·끝 줄·설명·댓글): [`cases_01.md`](cases_01.md) (#1~#15), [`cases_02.md`](cases_02.md) (#16~#30), [`cases_03.md`](cases_03.md) (#31~#45), [`cases_04.md`](cases_04.md) (#46~#60), [`cases_05.md`](cases_05.md) (#61~#75), [`cases_06.md`](cases_06.md) (#76~#90), [`cases_07.md`](cases_07.md) (#91~#105), [`cases_08.md`](cases_08.md) (#106~#108)

성공 쇼츠 표지 (번호 = 1번 표의 #): [`thumbs_01.jpg`](thumbs_01.jpg) (#1~#24), [`thumbs_02.jpg`](thumbs_02.jpg) (#25~#48), [`thumbs_03.jpg`](thumbs_03.jpg) (#49~#72), [`thumbs_04.jpg`](thumbs_04.jpg) (#73~#96), [`thumbs_05.jpg`](thumbs_05.jpg) (#97~#108)

받은 쇼츠 전부 (업로드 최근 순·글 출처·댓글): [`approved.md`](approved.md) · 비교 집단 숫자: [`compare.csv`](compare.csv)

