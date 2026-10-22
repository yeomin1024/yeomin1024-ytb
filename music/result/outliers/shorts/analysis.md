# 쇼츠 분석 — 음악 (`music`)

만든 시각 2026-10-22T08:00:49+00:00 UTC · `shorts_analysis.py v1.2.1` · 규칙 `music/analysis_rules.toml` v1.5

> **AI 가 쇼츠 지시사항을 만들 재료** — 숫자와 원문만 있고 해석·규칙은 없다. 0번 '한계'를 먼저 읽고, 표본이 작은 차이·대본 없는 사례로 규칙을 만들지 않는다.
> 롱폼 분석은 `../analysis.md` (같은 시청자 — 롱폼 댓글 요청은 거기 8-1). ※ 연구·교육용 — 투자 권유가 아님.

## 0. 자료와 한계

- 받은 쇼츠(사례 폴더 `S_<영상ID>`) 191개 · 쇼츠 탐색에서 본 영상 5,974개 (그중 쇼츠 5,128) · 쇼츠 검색 57개 · 채널 쇼츠 목록 110곳
- 비교 집단 708개 (성공 72, 10%) — 채널당 최근 5개 (잘린 2588)
- 글 출처 (받은 쇼츠 전부): 설명 163 · 없음 28 · 표지: oar2.jpg 163 · hqdefault.jpg 28

- 대본(자막·음성인식)이 없는 성공 쇼츠 111개 (#1, #2, #3, #4, #5, #6, #7, #8, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26, #27, #28, #29, #30 …) — 첫 3초·말 속도·끝 문장은 대본이 있는 쇼츠로만 셌다 (음성인식은 쇼츠부터 — 끝나면 다시 셈). '말 없음'은 음성인식 결과가 없는 쇼츠(음악·화면 글자만)
- 비교 집단 708개 = 쇼츠 검색(조회수 순 — 잘된 쇼츠 쪽으로 치우침)·채널 쇼츠 목록 390개 (치우침 없음) 에서 올린 지 3~180일·구독자 50,000 이하, 성공 비율 10% — 실제 시장 비율이 아니다. '있음/없음' 차이로만 보고, '무엇이 먹혔나'는 1-2번(같은 채널 안)을 먼저 보라
- 쇼츠인데 성공·비교에서 뺀 것: 주제 밖 958개, 뺀 주제 79개, 조회수 부풀림 의심 77개, 음악 아님 — 연예 73개, 음악 아님 — 공식 음원 자동 채널  46개, 라이브 방송 40개, 음악 아님 — 밈·코미디 26개, 음악 아님 — 명상 기법·호흡법 13개, 음악 아님 — 영화·드라마 장면 편집 9개, 음악 아님 — 그 밖 9개, 음악 아님 — 강좌·악기 손질·장비 8개, 음악 아님 — 공부 동기부여 3개, 음악 아님 — 이야기 3개, 음악 아님 — 경전 낭송 2개 — 조회수 부풀림·광고 의심 77개의 길이 중앙값 16초·조회수 중앙값 433,316회. 조회수는 많은데 좋아요가 거의 없음 = 광고로 조회수를 샀거나 아주 짧은 쇼츠가 반복 재생됨 (어느 쪽인지 API 로는 모름 — 5-2번에 따로). 조회수 순 검색 위쪽을 덮는다 (2026-10-15 '연금' 검색: 6초짜리 7개)
- 쇼츠 판별: 3분 이하 + 세로·정사각(화면비 = API embed 크기) — 쇼츠가 아니라서 뺀 것: 3분 넘음 387개, 가로 영상 232개, 길이 모름 227개. 화면비를 모르는 예전 캐시는 '#shorts' 표시·60초 이하로 추정
- 외국 영상을 넣음 (주제 설정 INCLUDE_FOREIGN = true) — 성공 쇼츠 중 외국 쇼츠 74개 (#1, #2, #3, #4, #5, #7, #8, #11, #12, #15, #16, #17, #18, #19, #20, #21, #24, #25, #26, #27, #28, #30, #31, #32, #33, #34, #35, #36, #37, #38). 첫 3초 음절·말 속도(한글 음절)는 한국어 쇼츠만으로 셌고, 제목·댓글 낱말 규칙은 한국어 기준이라 외국 쇼츠에는 거의 걸리지 않는다
- 같은 채널 기준선: 성공 쇼츠 104/111개만 '채널 평소 쇼츠 대비'가 있음 (채널 쇼츠가 5개 넘게 있어야 셈)
- 쇼츠 수요·공급의 '시장'은 쇼츠 검색(조회수 순)에서 본 최근 90일 쇼츠 441개 — 조회수 적은 쇼츠가 덜 잡힌다. 주제 묶음 사이의 상대 비교(지수)로만 보라. 검색어별 '결과 수'는 4분 미만 전체(가로 영상 포함) 추정이다
- 말 비교(6·7번)는 대본이 있는 성공 쇼츠 0개 · 나머지 0개로 셌다 — 표본이 작다
- 쇼츠 조회수는 2025-03-31 부터 '재생·다시 재생 횟수'(시청 시간 하한 없음)다 — 그 전 쇼츠와 숫자를 바로 비교하지 말 것. 쇼츠의 핵심 신호(피드에서 '본 비율 vs 넘긴 비율'·평균 시청 비율·다시 재생)는 YouTube API 로 볼 수 없다 — 대신 조회수·배수·같은 채널 대비·참여율(좋아요·댓글 ÷ 조회수)·대본의 첫 3초·끝 문장을 본다
- 형식·첫 줄·끝 줄 유형·댓글 갈래는 낱말 규칙이라 거칠다 (한 쇼츠가 여러 유형에 들 수 있음). 자동 자막은 문장 부호가 없어 '줄' = 자막 조각. 원문을 함께 보라
- 화면 글자(자막 띠·제목 카드)·음악·편집 속도는 영상을 받지 않으므로 셀 수 없다 — 표지 그림(thumbs_NN.jpg)과 대본으로만 가늠한다
- '눈에 띔'은 차이가 크고 표본이 충분하다는 표시일 뿐 원인이 아니다

## 1. 성공 쇼츠 111개

기준: 받은 쇼츠 중 올린 지 3~180일 · 구독자 50,000 이하 · 조회수 50,000 이상 · 조회수 ≥ 구독자 × 3.0 · 180초 이하 세로·정사각 · 채널당 2개 (배수 큰 순). 통과 182 − 뺀 것 35 − 채널당 제한 36

| # | 제목 | 채널 | 구독자 | 조회수 | 배수 | 채널 평소 쇼츠 대비 | 하루 조회수 | 길이 | 좋아요/1천 | 올린 때(한국) | 주제 | 형식 | 글 출처 | 첫 줄(첫 3초) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [I know I should sleep, but the voices in my head …](https://www.youtube.com/shorts/17UP7J8Ri3E) | NOVAE | 13,600 | 25,623,712 | ×1884.1 | ×10074.2 | 166,805.2 | 12초 | 3.5 | 금 2시 | 1. 수면·명상·힐링 | 그 밖 | 없음 |  |
| 2 | [#shorts #lowcortisol #satisfying #chill #fypシ #he…](https://www.youtube.com/shorts/Gcb9eQDRJH4) | slasherbabyboom… | 9,850 | 13,578,276 | ×1378.51 | – | 90,612.8 | 20초 | 8.34 | 월 20시 | 1. 수면·명상·힐링 | 그 밖 | 없음 |  |
| 3 | [Bheema love bgm ...💞💥#lovestatus #bgm #trending #…](https://www.youtube.com/shorts/XvjJJ625eHM) | miracle_mix | 5,330 | 6,150,877 | ×1154.01 | ×2580.1 | 42,403.8 | 35초 | 17.86 | 토 15시 | 기타 | 그 밖 | 없음 |  |
| 4 | [Turning a Bad Day Into Piano Music 🎹💔 (AI Music T…](https://www.youtube.com/shorts/5bC_3ftzlh0) | Deep piano | 4,550 | 4,635,192 | ×1018.72 | ×2675.4 | 32,487.2 | 22초 | 13.36 | 화 0시 | 14. AI 음악 | AI 음악 | 설명 |  |
| 5 | [Relaxing Aquarium 4K 🐠 Beautiful Fish Tank Ambien…](https://www.youtube.com/shorts/pElnrfPGV1I) | Zing Shots | 170 | 130,116 | ×765.39 | ×239.4 | 879.4 | 11초 | 4.96 | 수 18시 | 2. 자연 소리·백색… | 그 밖 | 설명 |  |
| 6 | [피아노 단 하나의 음으로 모두를 얼어붙게한 곡 ∣ Kanye West - Runaway …](https://www.youtube.com/shorts/QOMO1DPI2Mo) | 페이브노트 Fave. | 12,700 | 9,020,894 | ×710.31 | ×72.9 | 57,154.4 | 25초 | 4.77 | 일 21시 | 6. 피아노·클래식·… | 그 밖 | 설명 |  |
| 7 | [What sound does a piano make? (ft. TCU Choir Camp…](https://www.youtube.com/shorts/bWhG1Fq7X8k) | Elijah Ong - Mu… | 22,100 | 15,085,258 | ×682.59 | ×347.7 | 147,169.0 | 35초 | 34.53 | 일 4시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 없음 |  |
| 8 | [Relaxing Heavy Rain Camping with Dog 🌧️ ∣ Inflata…](https://www.youtube.com/shorts/zGp1ymVBzqs) | 90s Aura Cozy V… | 20,800 | 14,189,520 | ×682.19 | ×422.9 | 252,945.2 | 23초 | 7.38 | 목 14시 | 2. 자연 소리·백색… | 그 밖 | 설명 |  |
| 9 | [연대별 시대곡 피아노 챌린지](https://www.youtube.com/shorts/s1hYfDOB5O0) | 패밀리모먼츠 | 12,700 | 7,302,201 | ×574.98 | ×283.5 | 94,320.5 | 53초 | 11.78 | 목 6시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 10 | [랜덤으로 지목 당해 노래 부르는 Happy](https://www.youtube.com/shorts/nb6TL41nJpQ) | FreshCutFarm | 35,700 | 20,291,788 | ×568.4 | ×5026.5 | 128,564.9 | 50초 | 14.3 | 일 21시 | 기타 | 클립·발췌 (방송·무… | 설명 |  |
| 11 | [Premada Oorali ∣ Official Animated Teaser ∣Soothi…](https://www.youtube.com/shorts/spkM9pTzGnc) | Royalediting143… | 1,770 | 977,313 | ×552.15 | ×3102.6 | 60,100.9 | 23초 | 14.22 | 화 10시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 12 | [A Dinosaur’s Love Story #piano #google #game #pia…](https://www.youtube.com/shorts/imH34A_Y-3I) | 영펭 yeongpin | 35,100 | 17,256,941 | ×491.65 | ×883.7 | 399,518.0 | 16초 | 7.88 | 수 12시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 없음 |  |
| 13 | [랜덤으로 지목 당해 노래 부르는 보헤미안 랩소디](https://www.youtube.com/shorts/xotW9olN4TU) | FreshCutFarm | 35,700 | 16,217,887 | ×454.28 | ×4017.3 | 101,280.1 | 59초 | 7.39 | 금 13시 | 기타 | 클립·발췌 (방송·무… | 설명 |  |
| 14 | [#머무르 #꿈꾸던어른이되었나요 #커버 #장재혁 #보컬리스트장재혁#커버곡 #노래커버 #보컬…](https://www.youtube.com/shorts/av5KCoUA0K8) | 장재혁 Jang Jae Hy… | 230 | 104,256 | ×453.29 | ×78.0 | 2,756.4 | 57초 | 7.99 | 월 21시 | 12. 커버·노래 부… | 커버·직접 부른 노래 | 없음 |  |
| 15 | [💝 Ishq De Fanniyar ∣ Slowed + Reverb ∣ Lofi Aesth…](https://www.youtube.com/shorts/K0dMrCnd5Jw) | Jazzy Love Acti… | 46,400 | 18,716,833 | ×403.38 | ×746.5 | 400,006.0 | 44초 | 0.0 | 토 22시 | 8. 로파이·시티팝·칠 | 그 밖 | 설명 |  |
| 16 | ["Barsaat" song multi singer version 🔥❤️‍🩹 #barsaa…](https://www.youtube.com/shorts/sfCmfZP514k) | Indi Echo 🌿 | 3,880 | 1,527,124 | ×393.59 | – | 24,281.6 | 27초 | 13.53 | 목 19시 | 기타 | 그 밖 | 설명 |  |
| 17 | [Best Reggae Songs 2026🌴 Pacific Island Reggae Col…](https://www.youtube.com/shorts/xGqYECoBV6w) | Reggaeneration … | 1,050 | 370,060 | ×352.44 | ×1098.1 | 3,083.5 | 31초 | 3.3 | 수 16시 | 8. 로파이·시티팝·칠 | 그 밖 | 설명 |  |
| 18 | [Try With Your Own Voice 💜✨ - Sammi Meri Waar [Lyr…](https://www.youtube.com/shorts/fzacLxIL_fI) | Lyrics Corner | 7,120 | 2,246,841 | ×315.57 | ×67.6 | 132,978.1 | 27초 | 0.0 | 월 19시 | 6. 피아노·클래식·… | 한 곡 일부 (음원·… | 없음 |  |
| 19 | [🎬: Musafir Cafe New Series 💗 #love #chillwavelofi…](https://www.youtube.com/shorts/y_8PunZgJws) | Chillwave lofi⚡ | 10,900 | 3,380,914 | ×310.18 | ×179.6 | 41,234.2 | 23초 | 10.2 | 토 17시 | 8. 로파이·시티팝·칠 | 그 밖 | 설명 |  |
| 20 | [Musafir Cafe: Kaafi Hai Na (Song)∣ Vikrant Massey…](https://www.youtube.com/shorts/T6kiyfOI3xA) | Loop-e Shono | 2,570 | 773,094 | ×300.81 | ×256.8 | 8,513.2 | 30초 | 17.85 | 목 21시 | 4. 카페·매장·라운지 | 그 밖 | 설명 |  |
| 21 | [🌿첫 소절부터 빠져드는 가을에 듣고 싶은 감성 팝송 ∣ 7080 추억의 올드팝](https://www.youtube.com/shorts/efkKPe_vNHQ) | Oldies Salon | 1,050 | 315,697 | ×300.66 | ×137.8 | 7,278.3 | 46초 | 3.52 | 수 8시 | 9. 가요·발라드·트… | 추천·모음 (N곡·순… | 설명 |  |
| 22 | [지휘자까지 춤추게 만든 손열음(피아노에서 빛이 난다면 이런 느낌일까?✨)](https://www.youtube.com/shorts/z76Om6wO-RA) | 사건의뒷면 | 23,300 | 6,610,192 | ×283.7 | – | 43,717.2 | 16초 | 5.82 | 일 12시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 23 | [옴 마니 반메 훔 🙏 잠들기 전 듣는 부처님의 기도](https://www.youtube.com/shorts/_edUsvdpI9A) | 마음한줄기 | 9,740 | 2,455,710 | ×252.13 | ×1827.2 | 15,847.6 | 18초 | 21.98 | 수 18시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 24 | [ANIRUDH vs SAI ABHYANKKAR ∣ RECENT BGM & SONGS RA…](https://www.youtube.com/shorts/CDr5WeEZ5I0) | Tune ladder | 23,800 | 5,942,376 | ×249.68 | ×46.8 | 269,497.7 | 59초 | 0.0 | 수 15시 | 기타 | 그 밖 | 설명 |  |
| 25 | [Yoshi’s Island- Map BGM](https://www.youtube.com/shorts/PoRX7a-7dbQ) | Matsuzawa Aoi T… | 18,900 | 4,223,397 | ×223.46 | ×219.5 | 40,466.2 | 14초 | 8.88 | 금 8시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 26 | [Summer Hits 2026 ☀️ Chill Deep House Mix for Rela…](https://www.youtube.com/shorts/IcxZ1gydQZQ) | Sea Breeze Music | 3,840 | 853,776 | ×222.34 | ×114.7 | 7,183.4 | 32초 | 2.83 | 목 20시 | 8. 로파이·시티팝·칠 | 추천·모음 (N곡·순… | 없음 |  |
| 27 | [KALYANI ∣ Shreya Ghoshal ∣ ARJN, KDS, FIFTY4 & RO…](https://www.youtube.com/shorts/XeIYQ5dfRBg) | WaveTune | 3,060 | 645,234 | ×210.86 | ×34.7 | 27,730.2 | 14초 | 7.93 | 화 10시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 28 | [Rihanna - Work ft. Drake ∣ Lyrics ∣ Edit ∣ Aesthe…](https://www.youtube.com/shorts/C1qxYvKH3UA) | Cᵒᵗᵗᵒᴺ ᴸʸʳⁱᶜˢ | 6,060 | 1,266,348 | ×208.97 | ×244.2 | 43,476.8 | 12초 | 19.69 | 수 13시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 29 | [🎧 Relax Lounge Music 🍷 #loungemusic #deephouse #c…](https://www.youtube.com/shorts/j4OomQ5nnJQ) | 뮤직인유 Music in U | 10,300 | 2,093,991 | ×203.3 | ×518.4 | 42,941.9 | 13초 | 12.98 | 목 22시 | 4. 카페·매장·라운지 | 클립·발췌 (방송·무… | 설명 |  |
| 30 | [Calming ASMR sounds for sleep and relaxation 01 #…](https://www.youtube.com/shorts/HVy_kywEeFU) | Spiral Men | 33,100 | 6,148,517 | ×185.76 | ×240.4 | 130,419.3 | 31초 | 5.63 | 토 13시 | 1. 수면·명상·힐링 | 그 밖 | 없음 |  |
| 31 | [432Hz - Deep Sleep Healing ∣ Alpha Waves for Comp…](https://www.youtube.com/shorts/TIiqFNACNJI) | Spiritual Heali… | 3,650 | 652,958 | ×178.89 | ×311.5 | 27,589.1 | 165초 | 6.31 | 화 1시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 32 | [Nonstop Pinoy Reggae 2026 ∣ Bagong Umaga ☀️ Relax…](https://www.youtube.com/shorts/065qRsHIZBw) | SoundTrip | 7,250 | 1,246,909 | ×171.99 | ×637.8 | 16,358.4 | 170초 | 3.93 | 금 11시 | 8. 로파이·시티팝·칠 | 추천·모음 (N곡·순… | 설명 |  |
| 33 | [Rihanna - Work ft. Drake ∣ Lyrics ∣ Edit ∣ Aesthe…](https://www.youtube.com/shorts/Hs3VpEMI-ks) | SUKUNA X lyrics | 5,060 | 853,159 | ×168.61 | ×168.9 | 33,140.3 | 12초 | 19.12 | 토 23시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 34 | [Ibiza Summer Mix 2026 🍓 Best Tropical Deep House …](https://www.youtube.com/shorts/EfQeZ53iXSk) | Sea Breeze Music | 3,840 | 644,264 | ×167.78 | ×86.5 | 5,330.5 | 32초 | 3.43 | 화 20시 | 8. 로파이·시티팝·칠 | 추천·모음 (N곡·순… | 없음 |  |
| 35 | [Beautiful Relaxing Piano Music & Water Sounds 💦 C…](https://www.youtube.com/shorts/GMrFw9KD5pA) | Soul Soothing H… | 2,120 | 330,595 | ×155.94 | ×86.4 | 8,013.2 | 60초 | 4.66 | 금 10시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 36 | [🎧 KUNG STRESS KA, PAKINGGAN MO ’TO! TANGGAL PAGOD…](https://www.youtube.com/shorts/9mQXTN8O_yE) | ISLANG REGGAE PH | 5,980 | 903,282 | ×151.05 | ×103.9 | 22,706.7 | 169초 | 4.83 | 토 22시 | 기타 | 그 밖 | 설명 |  |
| 37 | [RELAXING MUSIC - STRESS RELIEF🌿Soothing Piano & W…](https://www.youtube.com/shorts/4qEZq-8ZIfc) | Soul Soothing H… | 2,120 | 318,996 | ×150.47 | ×83.4 | 7,122.9 | 60초 | 5.24 | 월 22시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 38 | ["Deewana Deewana" song multi singer version ✨🗿∣∣ …](https://www.youtube.com/shorts/vqa0ki41KHM) | Indi Echo 🌿 | 3,880 | 583,655 | ×150.43 | – | 6,931.0 | 34초 | 12.96 | 목 11시 | 기타 | 그 밖 | 설명 |  |
| 39 | [Ajeeb Dastan Hai Yeh #multiplayer #music #retro #…](https://www.youtube.com/shorts/dbtBr8IQpt4) | Ashish Mithari | 37,300 | 5,273,081 | ×141.37 | ×857.8 | 52,333.3 | 40초 | 21.85 | 월 22시 | 6. 피아노·클래식·… | 그 밖 | 없음 |  |
| 40 | [90s Best Romantic Saxophone of All Time 🎷 Soulful…](https://www.youtube.com/shorts/GFRyA57h8O8) | FREEDOM MUSIC L… | 7,080 | 853,553 | ×120.56 | ×567.5 | 6,428.8 | 179초 | 6.98 | 목 22시 | 7. 재즈·보사노바 | 그 밖 | 설명 |  |
| 41 | [Top 10 Best Mass BGM Of South Movies 2026. #massb…](https://www.youtube.com/shorts/iTelMvTQHFY) | Aura Cinefy | 6,090 | 706,606 | ×116.03 | ×43.3 | 9,459.2 | 44초 | 28.19 | 일 0시 | 기타 | 추천·모음 (N곡·순… | 없음 |  |
| 42 | [🍁 가을팝송 너무 좋다 ∣ 첫 곡부터 편안한 70&80 올드팝 🎶 #oldpop #올드팝…](https://www.youtube.com/shorts/V1fX11NiQJ0) | ouroldpop | 1,160 | 122,014 | ×105.18 | ×153.3 | 2,633.8 | 57초 | 3.12 | 일 9시 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 설명 |  |
| 43 | [아무도 생각 못한 소리로 서부의 아이콘이 된 음악 #석양의무법자](https://www.youtube.com/shorts/2ZKxQjF1V0I) | 클래식한소절 | 45,800 | 4,708,612 | ×102.81 | ×28.4 | 115,165.2 | 52초 | 11.83 | 금 19시 | 6. 피아노·클래식·… | 그 밖 | 설명 |  |
| 44 | [힐링](https://www.youtube.com/shorts/MBibKwN7oLA) | +82정 | 12,300 | 1,216,562 | ×98.91 | ×26.8 | 8,997.4 | 60초 | 8.38 | 화 11시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 45 | [한때 라디오만 켜면 흘러나오던 전설의 ‘외로운 양치기’ #팬플루트](https://www.youtube.com/shorts/QG2blK1FVyg) | 클래식한소절 | 45,800 | 4,446,688 | ×97.09 | ×26.8 | 55,655.8 | 38초 | 13.65 | 월 19시 | 9. 가요·발라드·트… | 연주 (직접 연주) | 설명 |  |
| 46 | [🎧 Luxury Lounge Music 🍷 #loungemusic #deephouse #…](https://www.youtube.com/shorts/NQrsgRLPKFs) | 뮤직인유 Music in U | 10,300 | 876,700 | ×85.12 | ×217.1 | 19,822.8 | 11초 | 13.42 | 화 11시 | 4. 카페·매장·라운지 | 클립·발췌 (방송·무… | 설명 |  |
| 47 | [Sohnea Song Lyrics – Miss Pooja ft. Millind Gaba …](https://www.youtube.com/shorts/vazUHUAfuKI) | LyriVoice | 5,490 | 444,096 | ×80.89 | ×217.8 | 3,080.0 | 49초 | 0.0 | 일 12시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 48 | [Night Oud Relaxing Arabic Music Melodies #oud #ud…](https://www.youtube.com/shorts/OfDQoPCZaYo) | Azqara | 31,800 | 2,490,789 | ×78.33 | ×75.8 | 20,618.9 | 29초 | 11.29 | 화 21시 | 기타 | 그 밖 | 없음 |  |
| 49 | [Barsaat (Lyrics) ~ Banjaare ∣🌧️🥀 Aesthetic Lyrics…](https://www.youtube.com/shorts/-oOlND34r8c) | nature-lyrics-P… | 9,460 | 656,664 | ×69.41 | ×43.1 | 13,652.8 | 26초 | 19.6 | 금 14시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 50 | [감성 뮤직/Emotional music #healing #love #lifeisbutad…](https://www.youtube.com/shorts/Jm4-p0mQjBk) | JEONGAM Media A… | 38,100 | 2,579,576 | ×67.71 | ×1203.7 | 15,603.1 | 31초 | 10.59 | 일 9시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 51 | [인연의 술잔 ∣ 감성 트로트 ∣ 추억 속의 위로 음악 #트로트 #감성 #중년음악#shor…](https://www.youtube.com/shorts/iJ8agTK7wBw) | 노래로 가보자(어제보다 나은… | 9,800 | 619,961 | ×63.26 | ×405.2 | 3,823.0 | 129초 | 9.61 | 수 13시 | 9. 가요·발라드·트… | 커버·직접 부른 노래 | 설명 |  |
| 52 | [Jaane meriye main tera haan song ❤ ∣ Trending 🙈 w…](https://www.youtube.com/shorts/Ch6fbOogn3E) | R.K Music 7 | 48,200 | 2,812,525 | ×58.35 | ×135.2 | 19,910.5 | 29초 | 0.0 | 수 10시 | 기타 | 그 밖 | 설명 |  |
| 53 | [Aakashame Nuvvani Full Lyrical Video ∣ Diamond Ra…](https://www.youtube.com/shorts/wuYBw0iMUvo) | Rakesh edits | 32,500 | 1,838,254 | ×56.56 | ×39.7 | 15,540.4 | 15초 | 19.19 | 금 10시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 54 | [Suno Nand Lal ਤਨਖ਼ਾਹ ਨਾਮਾ : ਭਾਈ ਨੰਦ ਲਾਲ #meditati…](https://www.youtube.com/shorts/qUAwuEQa61U) | Tere Bande | 13,400 | 730,048 | ×54.48 | ×81.4 | 4,159.4 | 73초 | 18.88 | 목 4시 | 1. 수면·명상·힐링 | AI 음악 | 설명 |  |
| 55 | [Aakashame Nuvvani ❤️✨ ∣ Diamond Raja ∣ Sid Sriram…](https://www.youtube.com/shorts/lGOry4snFDg) | KD Creation | 19,200 | 1,041,812 | ×54.26 | ×45.7 | 30,852.5 | 13초 | 16.74 | 금 22시 | 기타 | 그 밖 | 설명 |  |
| 56 | [빈손...퓨전국악/인생노래/불교/감성트롯/위로. ..](https://www.youtube.com/shorts/XfqDLZGv0-k) | 숨소리 가요 | 10,900 | 582,060 | ×53.4 | ×290.6 | 3,462.1 | 65초 | 8.74 | 목 14시 | 9. 가요·발라드·트… | 한 곡 일부 (음원·… | 설명 |  |
| 57 | [Masya Alloh!!❤Udah Ganteng Sholih juga😍 #muharram…](https://www.youtube.com/shorts/X9B_mhJWP_I) | Peaceful Ummah … | 42,000 | 2,225,069 | ×52.98 | ×128.3 | 18,342.0 | 36초 | 0.0 | 화 9시 | 기타 | 그 밖 | 설명 |  |
| 58 | [Never Quite Forgotten 잊힌 듯 잊히지 않는 #향수, 감성, 기억](https://www.youtube.com/shorts/a6lOZwrFsqA) | goldenpopsongs | 1,960 | 93,868 | ×47.89 | ×383.1 | 523.6 | 46초 | 11.78 | 일 10시 | 9. 가요·발라드·트… | 커버·직접 부른 노래 | 설명 |  |
| 59 | [part 2 of turning sad pieces happy #piano #music …](https://www.youtube.com/shorts/N003UbT7HVc) | piano.mp3 | 26,200 | 1,243,750 | ×47.47 | ×53.1 | 32,349.6 | 22초 | 37.99 | 월 6시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 없음 |  |
| 60 | [Barsaat (Lyrics) - Banjaare ∣ ✨Aesthetic Lyrics V…](https://www.youtube.com/shorts/pcBPXx3yN80) | LYRICAL YT 94 | 12,000 | 514,765 | ×42.9 | ×68.5 | 10,474.2 | 17초 | 23.06 | 목 13시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 61 | [🍂9월의 일요일, 가을 아침에 듣기 좋은 노래 ∣ 편안한 추억의 올드팝송 ∣ 9월 카페음…](https://www.youtube.com/shorts/-IxTh4fUxyc) | 나무감성 NAMUVIBE | 2,410 | 101,293 | ×42.03 | ×78.8 | 2,178.8 | 54초 | 3.29 | 일 5시 | 4. 카페·매장·라운지 | 추천·모음 (N곡·순… | 설명 |  |
| 62 | [Golden Sunset in Andalusia 🌅 ∣ Relaxing Oud & Spa…](https://www.youtube.com/shorts/8hosf0uYb-Q) | Andalusian Oud … | 26,700 | 1,081,090 | ×40.49 | ×86.3 | 7,647.0 | 61초 | 11.41 | 수 8시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 63 | [[불교음악] 흐르는 강물처럼 — 인생의 끝에서 부처님께 묻다 ∣ 나무아미타불 관세음보살 …](https://www.youtube.com/shorts/3zbiRtRhRHY) | 연꽃선율 | 21,500 | 837,952 | ×38.97 | ×88.0 | 4,793.3 | 169초 | 12.29 | 목 21시 | 기타 | 그 밖 | 설명 |  |
| 64 | [같은 노래 맞아...? [이창섭 (LEECHANGSUB) - 사계, 그리고 너]](https://www.youtube.com/shorts/giN8f3Pxp4k) | 바코드 플레이리스트 | 24,400 | 950,964 | ×38.97 | ×81.7 | 41,375.6 | 43초 | 6.53 | 화 17시 | 기타 | 추천·모음 (N곡·순… | 없음 |  |
| 65 | [Rihanna - Work (Lyrics) ft. Drake](https://www.youtube.com/shorts/b9SFUlKKIDw) | Fantazia Music | 25,900 | 896,315 | ×34.61 | ×16.0 | 20,088.0 | 13초 | 11.33 | 화 2시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 66 | [The Most Beautiful Adagio You'll Hear Today ∣ Rel…](https://www.youtube.com/shorts/lvDGMqpTS_c) | Adagio Maestro | 22,300 | 758,905 | ×34.03 | ×206.7 | 8,548.9 | 177초 | 31.02 | 토 22시 | 1. 수면·명상·힐링 | AI 음악 | 설명 |  |
| 67 | [[동요] 수업 준비 노래 ∣ 주의집중 ∣ 손유희 ∣ 공립유치원교사 🏫🎵](https://www.youtube.com/shorts/q66lMjvhItc) | 현클래스 | 1,500 | 50,157 | ×33.44 | – | 517.2 | 28초 | 9.19 | 금 17시 | 3. 공부·집중·작업 | 그 밖 | 설명 |  |
| 68 | [put on the losercore playlist](https://www.youtube.com/shorts/JsN-vShHpIM) | Bro Archive | 6,800 | 223,665 | ×32.89 | ×8.2 | 21,403.3 | 15초 | 13.63 | 월 6시 | 기타 | 추천·모음 (N곡·순… | 설명 |  |
| 69 | [Relaxing Piano Music – Deep Sleep Music with Bamb…](https://www.youtube.com/shorts/SjTXZ_K2si0) | Relaxing Gen Mu… | 3,570 | 115,838 | ×32.45 | ×40.3 | 658.6 | 60초 | 9.51 | 수 19시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 70 | [🍂 Cozy Autumn Coffee Ambience ☕ Relaxing Guitar I…](https://www.youtube.com/shorts/kbM0eMDlxbQ) | Guitar Coffee M… | 12,800 | 399,072 | ×31.18 | – | 5,037.6 | 154초 | 3.56 | 화 11시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 71 | [[BLACK SCREEN] Anxiety Relief Music 432Hz + 528Hz…](https://www.youtube.com/shorts/w50gRv2lvNA) | Tranquil Sounds… | 40,200 | 1,230,314 | ×30.6 | ×221.8 | 12,859.3 | 145초 | 8.17 | 일 0시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 72 | [🌊 하루종일 듣기 좋은 부드러운 카페 음악 ☕ 오션뷰 감성팝](https://www.youtube.com/shorts/FdKCaSIsKMM) | Moasway | 7,890 | 220,440 | ×27.94 | ×52.4 | 1,382.8 | 51초 | 2.62 | 토 7시 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 |  |
| 73 | [☕Coffee Time ∣ Relaxing Piano Music (☕커피 한잔할 때 듣기…](https://www.youtube.com/shorts/LOufJXnJB6k) | 마음의 휴식 | 3,240 | 81,056 | ×25.02 | ×1102.8 | 850.4 | 178초 | 12.16 | 일 9시 | 4. 카페·매장·라운지 | 연주 (직접 연주) | 없음 |  |
| 74 | [Put on that LimbusCore playlist #limbuscompany #m…](https://www.youtube.com/shorts/aNtWKQPTxaQ) | Not Na | 6,260 | 142,706 | ×22.8 | ×15.1 | 21,159.8 | 20초 | 36.18 | 목 23시 | 기타 | 추천·모음 (N곡·순… | 설명 |  |
| 75 | [💖 Ayyare Ayyare ∣ Romantic Melody Song ∣ Vijay & …](https://www.youtube.com/shorts/GPqdnSDRZ9U) | Vibe With Giree… | 46,100 | 1,044,567 | ×22.66 | ×31.5 | 18,731.6 | 21초 | 15.35 | 목 22시 | 기타 | 그 밖 | 설명 |  |
| 76 | [포세이큰 LMS ost 플레이리스트](https://www.youtube.com/shorts/ddwhcZffLBU) | 백설탕 | 3,330 | 74,046 | ×22.24 | ×9.3 | 636.7 | 25초 | 32.18 | 일 9시 | 13. OST·사운드… | 추천·모음 (N곡·순… | 없음 |  |
| 77 | [Cosmic Soul Healing 🌠 432Hz + 528Hz + 963Hz](https://www.youtube.com/shorts/5vuNKdYVZd4) | Tranquil Sounds… | 40,200 | 833,838 | ×20.74 | ×150.3 | 8,444.3 | 137초 | 9.84 | 수 23시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 78 | [듣는 순간 가슴이 무너지는 명곡｜바람에 구름가듯 _ 이은하 #7080 #감성음악 #추억소환](https://www.youtube.com/shorts/4byi4WW3kYM) | 뮤직 에세이 수필 _ Soo… | 20,900 | 421,323 | ×20.16 | ×51.3 | 3,194.6 | 47초 | 9.96 | 금 19시 | 9. 가요·발라드·트… | 추천·모음 (N곡·순… | 설명 |  |
| 79 | [[림버스 컴퍼니] 림버스 플레이리스트](https://www.youtube.com/shorts/c9NFDK2aQZw) | Da대행자 | 2,910 | 58,628 | ×20.15 | ×1.4 | 422.1 | 41초 | 52.67 | 금 19시 | 기타 | 추천·모음 (N곡·순… | 없음 |  |
| 80 | [어머니의 고무신 ∣ 산사에 새긴 그 기도, 이제야 압니다 #불교음악](https://www.youtube.com/shorts/jwCa6iqW5XA) | 연꽃선율 | 21,500 | 429,754 | ×19.99 | ×45.2 | 2,600.9 | 157초 | 16.54 | 일 11시 | 기타 | 그 밖 | 설명 |  |
| 81 | [🙏스님이 부른 노래 한 곡, 모두의 마음을 울리다 #불교음악 #관세음보살 #소원성취 #깊…](https://www.youtube.com/shorts/pgvUxeoYESA) | 연꽃 아래서 | 13,000 | 258,965 | ×19.92 | ×11.6 | 1,943.8 | 28초 | 13.72 | 목 11시 | 15. CCM·찬양·… | 그 밖 | 없음 |  |
| 82 | [Peaceful Streets of Cordoba ∣ Relaxing Oud & Span…](https://www.youtube.com/shorts/GlP9I-o0usQ) | Andalusian Oud … | 26,700 | 530,937 | ×19.89 | ×42.4 | 3,808.5 | 96초 | 12.28 | 금 7시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 83 | [풀버전듣기⬆️아침에 듣기좋은 잔잔한 팝송 ∣ Best Nostalgia 70s 80s O…](https://www.youtube.com/shorts/o5bPkIQ8OyY) | Nostalgic Old P… | 2,950 | 57,047 | ×19.34 | ×41.4 | 360.0 | 28초 | 3.33 | 일 6시 | 10. 팝송·K팝·J팝 | 클립·발췌 (방송·무… | 설명 |  |
| 84 | [🙏 불교노래｜상처를 내려놓으리｜명상음악｜국악트롯 #관세음보살 #불교음악 #위로](https://www.youtube.com/shorts/ZyP0PyN0NV8) | 마음의쉼터 | 5,920 | 113,687 | ×19.2 | ×7.4 | 1,217.0 | 74초 | 26.43 | 화 7시 | 1. 수면·명상·힐링 | 그 밖 | 없음 |  |
| 85 | [Top 5 Peaceful Night Songs 🌙 ∣ सोने से पहले ज़रूर…](https://www.youtube.com/shorts/H2hBVIzRVGs) | SK facts YT | 10,700 | 190,132 | ×17.77 | ×12.3 | 1,831.6 | 42초 | 23.44 | 금 21시 | 기타 | 추천·모음 (N곡·순… | 설명 |  |
| 86 | [Relax Your Mind 🌼 Soft Piano & Violin with Beauti…](https://www.youtube.com/shorts/UkjpAZW4eFQ) | Quick Anxiety R… | 43,100 | 756,650 | ×17.56 | ×14.3 | 6,472.5 | 134초 | 16.88 | 토 19시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 87 | [Ambient Ocean Drums 🌊 ∣ The Most Beautiful Nordic…](https://www.youtube.com/shorts/tGQVITlgDBQ) | Nordic Fjord Ha… | 8,350 | 141,082 | ×16.9 | ×81.1 | 963.7 | 16초 | 12.89 | 금 7시 | 기타 | 그 밖 | 설명 |  |
| 88 | [💖 Ayyare Ayyare ∣ Romantic Melody Song ∣ Vijay & …](https://www.youtube.com/shorts/Jsc6FFKw_E4) | Vibe With Giree… | 46,100 | 749,514 | ×16.26 | ×22.6 | 18,197.5 | 20초 | 14.42 | 금 12시 | 기타 | 그 밖 | 설명 |  |
| 89 | [Deep Sleep with Peaceful Piano Music: Binh Yen Pi…](https://www.youtube.com/shorts/6b8oWfvd6dw) | BINH YEN PIANO | 31,100 | 473,154 | ×15.21 | ×33.0 | 6,123.4 | 9초 | 2.91 | 목 10시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 90 | [Deep Sleep Music (No Ads) ∣ Stop Overthinking, He…](https://www.youtube.com/shorts/ToJBmQ0LZtU) | Dreamy Calm Mus… | 26,600 | 399,743 | ×15.03 | – | 3,470.4 | 56초 | 7.6 | 월 12시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 91 | [🙏신나는 찬양 ∣ 마음이 참 편안합니다.. 주님 안에서 누리는 평안 🎵 중년 힐링 찬양 …](https://www.youtube.com/shorts/ZXKo0P0atPs) | 은혜의 멜로디 | 11,100 | 153,576 | ×13.84 | ×6.7 | 2,384.1 | 178초 | 11.31 | 수 7시 | 5. 운동·드라이브·… | 그 밖 | 설명 |  |
| 92 | [Best Relaxing Music Saxophone #relaxingmusic #sax…](https://www.youtube.com/shorts/A8JCdVa6Vb0) | Radha Krishna S… | 8,530 | 114,857 | ×13.47 | ×14.9 | 2,196.7 | 40초 | 10.26 | 월 10시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 93 | [Tere Sang Yaara ~ Astif Aslam ∣ Aesthetic Lyrics …](https://www.youtube.com/shorts/TpGaLxvtICk) | HarmonicVibez | 48,100 | 618,137 | ×12.85 | ×13.1 | 5,735.6 | 16초 | 0.0 | 월 22시 | 기타 | 한 곡 일부 (음원·… | 설명 |  |
| 94 | [🙏 불교노래｜가는 길 밝혀주소서｜명상음악｜국악트롯 #관세음보살 #불교음악 #위로](https://www.youtube.com/shorts/nv_yiPwhH5o) | 마음의쉼터 | 5,920 | 75,247 | ×12.71 | ×4.9 | 721.8 | 96초 | 24.41 | 금 10시 | 1. 수면·명상·힐링 | 그 밖 | 없음 |  |
| 95 | [Relax Your Mind 🐦 Piano & Violin with Birds and B…](https://www.youtube.com/shorts/FXSTlxwJP0Y) | Quick Anxiety R… | 43,100 | 517,235 | ×12.0 | ×10.4 | 8,935.7 | 172초 | 18.06 | 화 19시 | 6. 피아노·클래식·… | 연주 (직접 연주) | 설명 |  |
| 96 | [#relaxingmusic](https://www.youtube.com/shorts/p4dSlB1-18k) | veerpulse | 44,600 | 512,616 | ×11.49 | ×7.1 | 57,532.0 | 6초 | 0.0 | 화 19시 | 기타 | 그 밖 | 설명 |  |
| 97 | [Calm Guzheng & Flute in Crystal Temple Ruins ∣ Ze…](https://www.youtube.com/shorts/aveC_SEj_xY) | Pure Chinese In… | 19,300 | 202,573 | ×10.5 | ×83.3 | 1,247.2 | 116초 | 23.69 | 수 7시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 98 | [10월에 듣는 카페음악☕🍂 #가을에듣기좋은음악 #카페음악 #힐링음악 #shorts Vol…](https://www.youtube.com/shorts/_pTWZdK_Lgw) | 노래의 조각들 | 18,400 | 184,511 | ×10.03 | ×7.8 | 8,640.4 | 57초 | 2.94 | 목 8시 | 1. 수면·명상·힐링 | 추천·모음 (N곡·순… | 설명 |  |
| 99 | [Morning Dopamine Reset 🌿 3 Minutes of Healing Ban…](https://www.youtube.com/shorts/p9awkVcQ9p4) | Soulful Breaths… | 49,600 | 489,927 | ×9.88 | ×41.1 | 4,713.7 | 164초 | 10.56 | 금 18시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 100 | [Deep Sleep with Peaceful Piano Music: Binh Yen Pi…](https://www.youtube.com/shorts/LiC8OATiDFw) | BINH YEN PIANO | 31,100 | 304,768 | ×9.8 | ×21.3 | 12,555.2 | 9초 | 2.63 | 월 10시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 101 | [🙏 천수경｜비구니 스님의 맑은 목소리에 눈물이 납니다 #불교음악 #깊은기도음악 #스님 #…](https://www.youtube.com/shorts/y1h3ne5BUTE) | 연꽃 아래서 | 13,000 | 127,071 | ×9.77 | ×5.7 | 1,241.2 | 30초 | 17.58 | 일 8시 | 15. CCM·찬양·… | 그 밖 | 설명 |  |
| 102 | [티없이 맑은 비구니 스님의 금강경 사구게 첫 번째와 두 번째 게송｜머문 바 없이 그 마음…](https://www.youtube.com/shorts/B3vGWKWShgA) | 인생은 트롯이지 | 20,200 | 187,840 | ×9.3 | ×115.7 | 1,249.3 | 70초 | 16.11 | 월 8시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 103 | [🍋 그냥 틀어두기 좋은 여름 카페 음악 🌿 편안한 감성팝 #카페 #힐링 #배경음악](https://www.youtube.com/shorts/HifHEgRTBMk) | Moasway | 7,890 | 68,558 | ×8.69 | ×16.4 | 498.9 | 60초 | 3.0 | 일 7시 | 1. 수면·명상·힐링 | 추천·모음 (N곡·순… | 설명 |  |
| 104 | [옴 마니 반메 훔 🙏 Om Mani Padme Hum 唵嘛呢叭咪吽 플루트 & 피아노 불교…](https://www.youtube.com/shorts/HA0Eotjrhcs) | Lotus of the Bu… | 17,900 | 150,621 | ×8.41 | ×24.4 | 1,389.3 | 161초 | 35.71 | 월 7시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 105 | [9월에 듣는 카페음악☕🍂 #가을에듣기좋은음악 #카페음악 #힐링음악 #shorts Vol.…](https://www.youtube.com/shorts/jox06rqLQL0) | 노래의 조각들 | 18,400 | 154,559 | ×8.4 | ×6.6 | 3,861.9 | 59초 | 3.0 | 토 16시 | 1. 수면·명상·힐링 | 추천·모음 (N곡·순… | 설명 |  |
| 106 | [Morning Cortisol Reset 🌿 Bansuri 432 Hz for Calm …](https://www.youtube.com/shorts/u3MKMNpfxmY) | Soulful Breaths… | 49,600 | 332,117 | ×6.7 | ×27.9 | 4,498.1 | 153초 | 7.77 | 일 20시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |
| 107 | [♥️✨🌷#karolinaprostenko #relaxingmusic #instrument…](https://www.youtube.com/shorts/yo0BqCXA3dI) | violin girls | 20,900 | 126,674 | ×6.06 | ×60.9 | 935.7 | 16초 | 18.21 | 화 8시 | 6. 피아노·클래식·… | 그 밖 | 없음 |  |
| 108 | [마음치유](https://www.youtube.com/shorts/iZtyEXngfdU) | +82정 | 12,300 | 69,924 | ×5.68 | ×1.5 | 524.1 | 27초 | 16.49 | 목 7시 | 1. 수면·명상·힐링 | 연주 (직접 연주) | 설명 |  |
| 109 | [[감성트로트] 기댈 곳 하나 없는🍂 #인생가 #트로트신곡 #한국트로트 #감성음악 #노래추…](https://www.youtube.com/shorts/P_CVL87cbjI) | 규규티비 | 37,800 | 211,526 | ×5.6 | ×34.3 | 1,509.4 | 142초 | 14.3 | 목 13시 | 9. 가요·발라드·트… | 한 곡 일부 (음원·… | 설명 |  |
| 110 | [아침마다 새로운 은혜 🌿 오늘도 감사로 시작합니다 ∣ 마음이 편안해지는 찬양 #shorts](https://www.youtube.com/shorts/LaS3Aq4yWm8) | 은혜의 멜로디 | 11,100 | 53,609 | ×4.83 | ×2.3 | 1,180.4 | 180초 | 11.7 | 월 7시 | 15. CCM·찬양·… | 그 밖 | 설명 |  |
| 111 | [옴 마니 반메 훔 🙏 Om Mani Padme Hum ∣ 唵嘛呢叭咪吽 한국 가야금 불교 …](https://www.youtube.com/shorts/y7LKZ9HwUBc) | Lotus of the Bu… | 17,900 | 84,153 | ×4.7 | ×13.6 | 769.1 | 162초 | 60.39 | 일 7시 | 1. 수면·명상·힐링 | 그 밖 | 설명 |  |

기준은 넘었지만 뺀 것: WORK (FUNK) (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Deep Sleep with Peaceful Pian… (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생)); 일할때 듣기좋은 발라드 추천 광고없는 노래모음 - 유… (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생)); 9월에 듣는 카페음악☕🍂 #가을에듣기좋은음악 #카페음… (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생)); Bloody Band (From "DC") (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Soft Smiles Only (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); One Name - Theme (From "Jaile… (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); 비가오니까 (밤의무희cover) (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Lemon Tang (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); REDRED (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Jum jum jhumthaara (From "Zom… (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); 모락산 #정설허브 #감성음악 #힐링음악 (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생)); BOOMPALA (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Love is in the Air, Pt. 1 (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); ICONIC BY MISTAKE (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Namaste (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); Thaalam Trip (Instrumental) (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); The Rose (Instrumental) (음악 아님 — 공식 음원 자동 채널 (- Topic·VEVO)(- Topic)); 【RELAXING PIANO BGM】溫柔鋼琴曲｜讓心情… (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생)); Kalyani Song 🍁∣ Whatsapp stat… (조회수 부풀림 의심(좋아요·댓글 거의 없음 — 광고 또는 반복 재생))

### 1-2. 같은 채널 기준선 (채널 쇼츠 목록 96곳 — 채널 크기·구독층이 같은 쇼츠끼리)

성공 쇼츠 104/111개에 '채널 평소 쇼츠 대비'(그 채널의 올린 지 3~180일 쇼츠 조회수 중앙값, 쇼츠 5개 넘을 때). 채널 89곳의 잘된 쇼츠(중앙값 ×3.0 이상) 375개 vs 평소 쇼츠(×0.5~1.5) 416개 — 채널당 5개씩

- 길이 중앙값: 잘된 36초 · 평소 38초 · 제목 글자 중앙값: 잘된 73 · 평소 68.0 · 해시태그 수 중앙값: 잘된 10 · 평소 8.0

| 제목 특징 | 잘된 쇼츠 | 평소 쇼츠 | 차이 |
|---|---|---|---|
| 구분 기호(ㅣ·｜·/)로 나눔 | 50% | 41% | 8.6% |
| 숫자가 들어감 | 31% | 25% | 6.2% |
| 따옴표·괄호로 강조 | 7.2% | 11% | -4% |
| '#shorts' 표시 | 14% | 18% | -3% |
| vs 비교 | 3.2% | 1.2% | 2.0% |
| 물음표 ? | 3.2% | 2.2% | 1.0% |
| 느낌표 ! | 3.2% | 4.1% | -1% |
| 과정·벌어진 일·결말·결국 | 0.8% | 0% | 0.8% |
| 말줄임 …·... | 2.4% | 1.9% | 0.5% |
| 25자 미만 | 7.2% | 6.7% | 0.5% |
| 패턴형(공통점·특징·이유·N가지·착각·과정) | 0.8% | 0.5% | 0.3% |
| 사연·오디오북·실화·고백 | 0.3% | 0% | 0.3% |
| 노후·퇴직금·은퇴·50~70대 | 0% | 0.2% | -0% |
| AI | 6.1% | 6.0% | 0.1% |

| 주제 묶음 | 잘된 | 평소 | 차이 |
|---|---|---|---|
| 기타 | 44% | 50% | -6% |
| 8. 로파이·시티팝·칠 | 5.9% | 2.4% | 3.5% |
| 4. 카페·매장·라운지 | 4.3% | 1.9% | 2.4% |
| 12. 커버·노래 부르기 | 1.1% | 3.1% | -2% |
| 5. 운동·드라이브·신나는 | 1.9% | 0.7% | 1.2% |
| 1. 수면·명상·힐링 | 14% | 14% | -1% |
| 9. 가요·발라드·트로트 | 6.9% | 6.2% | 0.7% |
| 3. 공부·집중·작업 | 0.8% | 0.2% | 0.6% |
| 7. 재즈·보사노바 | 0.5% | 0% | 0.5% |
| 11. 힙합·R&B·EDM | 0.5% | 0.2% | 0.3% |

| 형식 | 잘된 | 평소 | 차이 |
|---|---|---|---|
| 한 곡 일부 (음원·뮤비·가사·티저) | 17% | 15% | 2.2% |
| 그 밖 | 47% | 49% | -2% |
| 연주 (직접 연주) | 15% | 16% | -1% |
| AI 음악 | 1.3% | 0.2% | 1.1% |
| 클립·발췌 (방송·무대·직캠) | 3.7% | 3.1% | 0.6% |
| 커버·직접 부른 노래 | 3.7% | 4.1% | -0% |
| 추천·모음 (N곡·순위·플리) | 12% | 12% | -0% |

같은 채널에서 잘된 쇼츠 (채널 평소 대비 큰 순):

- ×3078.2 · 977,313회 · 23초 · Royalediting143… — Premada Oorali ∣ Official Animated Teaser ∣Soothing Title Song (https://www.youtube.com/shorts/spkM9pTzGnc)
- ×2511.6 · 6,150,877회 · 35초 · miracle_mix — Bheema love bgm ...💞💥#lovestatus #bgm #trending #love (https://www.youtube.com/shorts/XvjJJ625eHM)
- ×992.2 · 120,052회 · 99초 · 정설허브 — 모락산 #정설허브 #감성음악 #힐링음악 (https://www.youtube.com/shorts/Gh92mQKihOY)
- ×930.2 · 112,554회 · 89초 · 정설허브 — 해질녁 단상 #노래 #music #감성 (https://www.youtube.com/shorts/4HF-MBQWcH8)
- ×868.4 · 17,256,941회 · 16초 · 영펭 yeongpin — A Dinosaur’s Love Story #piano #google #game #pianocover #pianotutori… (https://www.youtube.com/shorts/imH34A_Y-3I)
- ×806.6 · 97,603회 · 84초 · 정설허브 — 추억을 삼키다 (https://www.youtube.com/shorts/a_21qqkufng)
- ×680.5 · 1,905,378회 · 14초 · Akshuu Beats — Kalyani Song 🍁∣ Whatsapp status 🌿 ∣#lyrics #edit #shorts #status #tre… (https://www.youtube.com/shorts/ZWYIJzAnGZ8)
- ×582.4 · 1,246,909회 · 170초 · SoundTrip — Nonstop Pinoy Reggae 2026 ∣ Bagong Umaga ☀️ Relaxing Island Vibes ∣ M… (https://www.youtube.com/shorts/065qRsHIZBw)
- ×390.5 · 47,256회 · 71초 · 정설허브 — 태을봉 정상에 올라 (https://www.youtube.com/shorts/QyCKIPQyDpI)
- ×315.7 · 14,189,520회 · 23초 · 90s Aura Cozy V… — Relaxing Heavy Rain Camping with Dog 🌧️ ∣ Inflatable Tent ASMR Time-L… (https://www.youtube.com/shorts/zGp1ymVBzqs)
- ×297.1 · 652,958회 · 165초 · Spiritual Heali… — 432Hz - Deep Sleep Healing ∣ Alpha Waves for Complete Body and Spirit… (https://www.youtube.com/shorts/TIiqFNACNJI)
- ×260.2 · 15,085,258회 · 35초 · Elijah Ong - Mu… — What sound does a piano make? (ft. TCU Choir Camp) #shorts (https://www.youtube.com/shorts/bWhG1Fq7X8k)
- ×258.6 · 554,167회 · 129초 · JEONGAM Media A… — World · Humanity · Story ∣ Emotional story/감성 스토리 World · Humanity · … (https://www.youtube.com/shorts/vJ7M38clmHs)
- ×241.3 · 853,553회 · 179초 · FREEDOM MUSIC L… — 90s Best Romantic Saxophone of All Time 🎷 Soulful Smooth Jazz Love So… (https://www.youtube.com/shorts/GFRyA57h8O8)
- ×239.2 · 130,116회 · 11초 · Zing Shots — Relaxing Aquarium 4K 🐠 Beautiful Fish Tank Ambience with Sleep Music … (https://www.youtube.com/shorts/pElnrfPGV1I)
- ×237.9 · 194,608회 · 59초 · ouroldpop — 🍁 가을엔 역시 이런 목소리가 좋다 ∣ 오래 듣고 싶은 올드팝 #oldpop #music (https://www.youtube.com/shorts/lL2T8FIbIzM)
- ×225.2 · 1,266,348회 · 12초 · Cᵒᵗᵗᵒᴺ ᴸʸʳⁱᶜˢ — Rihanna - Work ft. Drake ∣ Lyrics ∣ Edit ∣ Aesthetic ∣ #Rihanna #Work… (https://www.youtube.com/shorts/C1qxYvKH3UA)
- ×220.7 · 1,820,180회 · 55초 · 뮤직 에세이 수필 _ Soo… — 세월이 훅~ 지나간 흔적! 새벽비 _ 혜은이 #7080 #추억소환 #세련미 (https://www.youtube.com/shorts/amCIsWqkIq4)
- ×216.2 · 4,223,397회 · 14초 · Matsuzawa Aoi T… — Yoshi’s Island- Map BGM (https://www.youtube.com/shorts/PoRX7a-7dbQ)
- ×202.1 · 192,363회 · 36초 · Justin 放鬆音樂 — 【RELAXING PIANO BGM】溫柔鋼琴曲｜讓心情瞬間變好 (https://www.youtube.com/shorts/XebWlrpCnOc)

성공 쇼츠와 같은 채널 평소 쇼츠 짝 (표지): [`thumbs_pairs_01.jpg`](thumbs_pairs_01.jpg) (#1~), [`thumbs_pairs_02.jpg`](thumbs_pairs_02.jpg) (#12~)

### 1-3. 자료를 받지 않은 성공 후보 44개 (웹 화면 [쇼츠] 목록에서 승인하면 분석에 들어감 — 채널 자리가 찬 것 300개는 뺌)

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
| 기타 | 170 (21%) | 13,449.0 | 748.2 | 3, 10, 11, 13, 16, 24, 27, 28, 33, 36, 38, 41, 47, 48, 49 |
| 6. 피아노·클래식·연주곡 | 93 (12%) | 3,317 | 400.3 | 6, 7, 9, 12, 18, 22, 25, 39, 43, 59, 70, 86, 92, 95, 107 |
| 1. 수면·명상·힐링 | 155 (8.4%) | 3,360 | 102.8 | 1, 2, 23, 30, 31, 35, 37, 44, 50, 54, 62, 66, 69, 71, 77 |
| 8. 로파이·시티팝·칠 | 26 (7.7%) | 4,038.0 | 277.1 | 15, 17, 19, 26, 32, 34 |
| 12. 커버·노래 부르기 | 18 (5.6%) | 2,022.5 | 171.3 | 14 |
| 9. 가요·발라드·트로트 | 56 (3.6%) | 2,087.5 | 229.5 | 21, 45, 51, 56, 58, 78, 109 |
| 4. 카페·매장·라운지 | 61 (3.3%) | 2,714 | 38.1 | 20, 29, 46, 61, 72, 73 |
| 3. 공부·집중·작업 | 61 (1.6%) | 1,822 | 22.4 | 67 |
| 2. 자연 소리·백색소음 | 17 (0%) | 1,945 | 39.1 | 5, 8 |
| 13. OST·사운드트랙 | 1 (100%) (표본 적음) | 74,046 | 636.7 | 76 |
| 7. 재즈·보사노바 | 5 (40%) (표본 적음) | 25,346 | 321.7 | 40 |
| 15. CCM·찬양·국악·동요 | 13 (15%) (표본 적음) | 12,494 | 222.8 | 81, 101, 110 |
| 5. 운동·드라이브·신나는 | 4 (0%) (표본 적음) | 11,637.0 | 1,007.6 | 91 |
| 10. 팝송·K팝·J팝 | 12 (0%) (표본 적음) | 1,755.5 | 12.5 | 42, 83 |
| 11. 힙합·R&B·EDM | 13 (0%) (표본 적음) | 1,962 | 17.4 | – |
| 14. AI 음악 | 3 (0%) (표본 적음) | 4,928 | 37.5 | 4 |

| 형식 | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 몫 | 성공 쇼츠 # |
|---|---|---|---|---|
| 클립·발췌 (방송·무대·직캠) | 26 (15%) | 161.3 | 4.5% | 10, 13, 29, 46, 83 |
| 연주 (직접 연주) | 116 (12%) | 317.3 | 21% | 7, 9, 12, 22, 25, 35, 37, 44, 45, 59, 62, 69, 70, 73, 82 |
| 그 밖 | 265 (12%) | 172.9 | 41% | 1, 2, 3, 5, 6, 8, 15, 16, 17, 19, 20, 23, 24, 30, 31 |
| 한 곡 일부 (음원·뮤비·가사·티저) | 105 (11%) | 574.0 | 12% | 11, 18, 27, 28, 33, 47, 49, 53, 56, 60, 65, 93, 109 |
| 추천·모음 (N곡·순위·플리) | 148 (6.8%) | 66.2 | 14% | 21, 26, 32, 34, 41, 61, 64, 68, 74, 76, 78, 79, 85, 98, 103 |
| 커버·직접 부른 노래 | 36 (2.8%) | 98.2 | 4.5% | 14, 42, 51, 58, 72 |
| AI 음악 | 12 (0%) (표본 적음) | 32.5 | 2.7% | 4, 54, 66 |

## 3. 수요와 공급 (최근 90일 쇼츠 441개 — 쇼츠 검색으로 찾은 것, 채널 크기 상관없음)

지수 = 하루 조회수 몫 ÷ 쇼츠 수 몫 (1 보다 크면 쇼츠 하나가 평균보다 많이 봄 = 공급이 모자라 보임)

| 주제 묶음 | 쇼츠 | 채널 | 수요 몫 | 공급 몫 | 지수 | 하루 조회수 중앙값 |
|---|---|---|---|---|---|---|
| 6. 피아노·클래식·연주곡 | 62 | 47 | 51% | 14% | **3.63** | 57,282.3 |
| 기타 | 66 | 58 | 26% | 15% | **1.76** | 38,699.3 |
| 9. 가요·발라드·트로트 | 44 | 29 | 3.7% | 10% | **0.37** | 2,453.9 |
| 3. 공부·집중·작업 | 41 | 37 | 2.5% | 9.3% | **0.27** | 109.9 |
| 7. 재즈·보사노바 | 19 | 2 | 0.5% | 4.3% | **0.11** | 2,794.3 |
| 1. 수면·명상·힐링 | 144 | 59 | 3.3% | 33% | **0.1** | 418.3 |
| 4. 카페·매장·라운지 | 31 | 20 | 0.4% | 7.0% | **0.05** | 138.8 |
| 8. 로파이·시티팝·칠 | 11 | 9 | 7.7% | 2.5% | **3.09** (표본 적음) | 41,234.2 |
| 12. 커버·노래 부르기 | 8 | 7 | 2.5% | 1.8% | **1.4** (표본 적음) | 28,509.7 |
| 2. 자연 소리·백색소음 | 5 | 4 | 1.2% | 1.1% | **1.08** (표본 적음) | 86.8 |
| 10. 팝송·K팝·J팝 | 6 | 4 | 0.9% | 1.4% | **0.69** (표본 적음) | 8,578.0 |
| 5. 운동·드라이브·신나는 | 1 | 1 | 0% | 0.2% | **0.05** (표본 적음) | 2,384.1 |
| 15. CCM·찬양·국악·동요 | 2 | 2 | 0% | 0.5% | **0.01** (표본 적음) | 607.6 |
| 11. 힙합·R&B·EDM | 1 | 1 | 0% | 0.2% | **0.0** (표본 적음) | 17.9 |

검색어별 (쇼츠 검색 — videoDuration=short, 조회수 순 50개):

| 검색어 | 찾음 | 그중 쇼츠 | 결과 수(4분 미만 추정) | 최근 30일 | 조회수 중앙값 | 하루 조회수 중앙값 | 큰 채널 몫 | 작은 채널 성공 | 지금 검색어 |
|---|---|---|---|---|---|---|---|---|---|
| chill music | 50 | 8 (16%) | 1,000,000 | 0 | 1,050,342.5 | 11,770.9 | 0% | 4/4 | ○ |
| 카페음악 | 50 | 16 (32%) | 1,000,000 | 2 | 98,337.0 | 2,250.8 | 7.1% | 12/13 | ○ |
| 힐링음악 | 50 | 21 (42%) | 610,205 | 0 | 582,060 | 4,793.3 | 15% | 11/11 | ○ |
| deep sleep music | 50 | 7 (14%) | 1,000,000 | 1 | 558,690.5 | 6,984.7 | 17% | 5/5 | ○ |
| relaxing piano | 50 | 27 (54%) | 807,686 | 5 | 271,784 | 6,472.5 | 14% | 16/18 | ○ |
| stress relief music | 50 | 27 (54%) | 408,242 | 2 | 332,117 | 5,978.0 | 28% | 18/18 | ○ |
| relaxing piano music | 50 | 25 (50%) | 1,000,000 | 9 | 119,125 | 8,013.2 | 12% | 11/15 | ○ |
| soothing music | 50 | 32 (64%) | 1,000,000 | 2 | 1,021,095.5 | 14,830.5 | 41% | 19/19 | ○ |
| work music | 50 | 24 (48%) | 1,000,000 | 3 | 1,266,348 | 42,941.9 | 44% | 5/5 | ○ |
| MeditationMusic | 50 | 48 (96%) | 446,004 | 1 | 218,992 | 3,974.1 | 43% | 11/12 | ○ |
| Sleep Music | 50 | 3 (6.0%) | 1,000,000 | 0 | 14,306,814.5 | 101,399.7 | 50% | 1/1 | ○ |
| cafe music | 50 | 7 (14%) | 1,000,000 | 0 | 2,691,481.0 | 37,143.6 | 50% | 2/2 | ○ |
| calming music | 50 | 11 (22%) | 1,000,000 | 0 | 1,010,983.0 | 13,490.0 | 50% | 4/4 | ○ |
| 노래 | 50 | 23 (46%) | 1,000,000 | 1 | 13,038,949 | 128,564.9 | 57% | 3/3 | ○ |
| relaxation music | 50 | 8 (16%) | 1,000,000 | 0 | 962,318 | 12,859.3 | 57% | 3/3 | ○ |
| RelaxingMusic | 50 | 44 (88%) | 1,000,000 | 5 | 275,964.5 | 5,070.1 | 60% | 17/17 | ○ |
| 명상음악 | 50 | 41 (82%) | 354,598 | 2 | 48,654.5 | 498.1 | 12% | 15/35 | ○ |
| 플레이리스트 | 50 | 16 (32%) | 1,000,000 | 6 | 154,639 | 21,159.8 | 55% | 4/5 | ○ |
| peaceful music | 50 | 18 (36%) | 1,000,000 | 0 | 1,118,525 | 18,342.0 | 67% | 5/5 | ○ |
| yoga music | 50 | 20 (40%) | 1,000,000 | 1 | 489,927 | 4,713.7 | 67% | 1/1 | ○ |
| BGM | 50 | 38 (76%) | 1,000,000 | 1 | 6,046,626.5 | 58,469.8 | 70% | 3/3 | ○ |
| ambient music | 50 | 15 (30%) | 1,000,000 | 4 | 217,803.5 | 13,944.8 | 70% | 3/3 | ○ |
| 편안한음악 | 50 | 33 (66%) | 199,263 | 8 | 17,446.5 | 384.2 | 3.3% | 8/29 | ○ |
| background music | 50 | 28 (56%) | 1,000,000 | 1 | 2,403,838.5 | 44,543.8 | 75% | 2/2 | ○ |
| calm music | 50 | 12 (24%) | 1,000,000 | 1 | 1,227,893.5 | 15,239.5 | 75% | 2/2 | ○ |
| 잔잔한음악 | 50 | 34 (68%) | 307,826 | 5 | 11,845 | 85.3 | 3.0% | 7/32 | ○ |
| 감성음악 | 50 | 29 (58%) | 1,000,000 | 4 | 448,624.0 | 5,095.2 | 81% | 5/5 | ○ |
| study music | 50 | 23 (46%) | 1,000,000 | 3 | 962,318 | 35,994.2 | 87% | 2/2 | ○ |
| 발라드 | 50 | 38 (76%) | 1,000,000 | 1 | 2,158,515.5 | 43,614.7 | 88% | 1/1 | ○ |
| 피아노 | 50 | 50 (100%) | 1,000,000 | 4 | 10,041,900.0 | 127,482.2 | 92% | 3/3 | ○ |
| 음악 | 50 | 28 (56%) | 1,000,000 | 1 | 5,213,079.5 | 100,846.0 | 92% | 1/1 | ○ |
| 수면 명상 | 50 | 45 (90%) | 114,521 | 2 | 7,741.5 | 122.5 | 12% | 2/21 | ○ |
| healingmusic | 50 | 39 (78%) | 334,374 | 9 | 5,607 | 148.5 | 43% | 3/21 | ○ |
| lofi | 50 | 19 (38%) | 1,000,000 | 1 | 2,075,813 | 33,170.2 | 92% | 1/1 | ○ |
| 감성발라드 | 50 | 26 (52%) | 677,280 | 1 | 71,397 | 589.1 | 62% | 1/5 | ○ |
| pianomusic | 50 | 44 (88%) | 1,000,000 | 0 | 3,844,890.5 | 39,319.0 | 93% | 2/2 | ○ |
| piano | 50 | 43 (86%) | 1,000,000 | 4 | 16,171,099.5 | 183,128.8 | 94% | 2/2 | ○ |
| instrumental music | 50 | 25 (50%) | 1,000,000 | 3 | 3,572,187 | 46,012.4 | 94% | 1/1 | ○ |
| 마음이편안해지는음악 | 50 | 41 (82%) | 52,297 | 3 | 2,941.5 | 22.6 | 5.0% | 2/38 | ○ |
| 집중음악 | 50 | 37 (74%) | 399,799 | 6 | 1,368.5 | 12.6 | 2.8% | 1/35 | ○ |
| 휴식음악 | 50 | 41 (82%) | 395,130 | 11 | 1,594 | 44.1 | 0% | 1/39 | ○ |
| music | 50 | 6 (12%) | 1,000,000 | 0 | 51,151,617 | 542,294.8 | 100% | 0/0 | ○ |
| playlist | 50 | 7 (14%) | 1,000,000 | 0 | 12,298,048 | 114,446.9 | 100% | 0/0 | ○ |
| 트로트 | 50 | 30 (60%) | 1,000,000 | 0 | 4,052,840 | 40,692.8 | 100% | 0/0 | ○ |
| 플리 | 50 | 30 (60%) | 1,000,000 | 0 | 1,938,781 | 32,930.4 | 100% | 0/0 | ○ |
| 노래모음 | 50 | 17 (34%) | 1,000,000 | 0 | 3,579,102.0 | 21,078.0 | 100% | 0/0 | ○ |
| focus music | 50 | 14 (28%) | 1,000,000 | 3 | 12,850.5 | 199.8 | 38% | 0/5 | ○ |
| 공부음악 | 50 | 28 (56%) | 772,040 | 11 | 1,502 | 62.9 | 0% | 0/21 | ○ |
| 수면유도음악 | 50 | 34 (68%) | 45,367 | 12 | 1,828 | 54.6 | 3.2% | 0/30 | ○ |
| 잠잘때 듣는 | 50 | 37 (74%) | 91,614 | 0 | 4,185 | 33.8 | 0% | 0/3 | ○ |

사람들이 찾는 말(YouTube 자동완성) 중 최근 쇼츠가 적은 말 — 틈 = 자동완성 점수 ÷ (1 + 최근 쇼츠 수), 전체 532개 중 위 30개 · 뺀 것: 실시간·전망 등 13, 채널 이름 20

| 말 | 자동완성 점수 | 씨앗 검색어 | 최근 쇼츠 | 하루 조회수 중앙값 | 틈 |
|---|---|---|---|---|---|
| 수면음악 3시간 | 1.8 | 수면음악, 숙면음악 | 0 | – | 1.8 |
| meditation music for positive… | 1.8 | meditation music, MeditationM… | 0 | – | 1.8 |
| healing music kks | 1.8 | healing music, healingmusic | 0 | – | 1.8 |
| sleep music dark screen | 1.8 | sleep music, Sleep Music | 0 | – | 1.8 |
| piano music bros | 1.8 | piano music, pianomusic | 0 | – | 1.8 |
| bgm 모음 | 1.8 | bgm, BGM | 0 | – | 1.8 |
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
| bgmi air | 1.2 | bgm, BGM | 0 | – | 1.2 |
| relaxing piano music for sleep | 1.2 | relaxing piano music, relaxin… | 0 | – | 1.2 |
| piano music bros chopin | 1.1 | piano music, pianomusic | 0 | – | 1.1 |
| 수면음악 클래식 | 1.0 | 수면음악, 숙면음악 | 0 | – | 1.0 |
| meditation music 10 minutes | 1.0 | meditation music, MeditationM… | 0 | – | 1.0 |
| healing music playlist | 1.0 | healing music, healingmusic | 0 | – | 1.0 |
| sleep music playlist | 1.0 | sleep music, Sleep Music | 0 | – | 1.0 |
| kpop demon hunters | 1.0 | kpop | 0 | – | 1.0 |
| bgm 추천 | 1.0 | bgm, BGM | 0 | – | 1.0 |
| piano man | 1.0 | piano | 0 | – | 1.0 |
| peaceful music for studying | 1.0 | peaceful music | 0 | – | 1.0 |
| 힐링음악 피아노 | 0.9 | 힐링음악 | 0 | – | 0.9 |
| 명상음악 싱잉볼 | 0.9 | 명상음악 | 0 | – | 0.9 |

## 4. 제목 · 해시태그 (비교 집단)

| 제목 특징 | 있음 (성공 비율) | 없음 | 차이 | 성공 쇼츠 몫 |
|---|---|---|---|---|
| 25자 미만 | 48 (25%) | 660 (9.1%) | +16% ⚑ | 7.2% |
| 패턴형(공통점·특징·이유·N가지·착각·과정) | 7 (0%) | 701 (10%) | -10% (표본 적음) | 0% |
| 이유 | 7 (0%) | 701 (10%) | -10% (표본 적음) | 0% |
| 직접·해보니·N년 기록 | 6 (0%) | 702 (10%) | -10% (표본 적음) | 0% |
| 과정·벌어진 일·결말·결국 | 1 (0%) | 707 (10%) | -10% (표본 적음) | 0% |
| 손실 낱말(망하·날린·잃은·반토막) | 1 (0%) | 707 (10%) | -10% (표본 적음) | 0% |
| S&P500·ETF·지수·나스닥 | 1 (0%) | 707 (10%) | -10% (표본 적음) | 0% |
| 빚투·신용·미수·레버리지·대출 | 1 (0%) | 707 (10%) | -10% (표본 적음) | 0% |
| vs 비교 | 11 (18%) | 697 (10%) | +8.2% (표본 적음) | 0.9% |
| 물음표 ? | 19 (16%) | 689 (10%) | +5.8% | 2.7% |
| 40자 이상 | 567 (9.2%) | 141 (14%) | -5% | 84% |
| 말줄임 …·... | 17 (5.9%) | 691 (10%) | -4% | 3.6% |
| 느낌표 ! | 28 (7.1%) | 680 (10%) | -3% | 1.8% |
| '#shorts' 표시 | 118 (7.6%) | 590 (11%) | -3% | 13% |
| 숫자가 들어감 | 186 (11%) | 522 (9.8%) | +1.5% | 23% |
| 따옴표·괄호로 강조 | 89 (9.0%) | 619 (10%) | -1% | 13% |
| AI | 63 (11%) | 645 (10%) | +1.0% | 6.3% |
| 구분 기호(ㅣ·｜·/)로 나눔 | 292 (10%) | 416 (10%) | +0.2% | 43% |

성공 비율이 높은 제목 낱말: 노래 (54 (20%) vs 9.3% ⚑), Relaxing (24 (21%) vs 9.8% ⚑), Lyrics (30 (20%) vs 9.7% ⚑), Sleep (33 (18%) vs 9.8%), song (45 (16%) vs 9.8%), love (28 (14%) vs 10%), Deep (39 (13%) vs 10%), relaxingmusic (26 (12%) vs 10%), Aesthetic (27 (11%) vs 10%)

성공 비율이 낮은 제목 낱말: 음악 (71 (0%) vs 11%), 노동요 (39 (0%) vs 11%), 좋은 (40 (0%) vs 11%), 편안해지 (32 (0%) vs 11%), 카페음악 (36 (0%) vs 11%), 카페 (35 (0%) vs 11%), 감성 (31 (0%) vs 11%), 가을 (29 (0%) vs 11%), 매장음악 (28 (0%) vs 11%), 힐링음악 (24 (0%) vs 10%)

| 제목 길이 | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 # |
|---|---|---|---|
| 20자 미만 | 23 (30%) | 222.4 | 9, 44, 76, 96, 108 |
| 20~29자 | 51 (16%) | 98.8 | 10, 13, 23, 25, 56, 68, 79 |
| 30~39자 | 67 (7.5%) | 94.6 | 43, 45, 65, 67, 72, 80 |
| 40자 이상 | 567 (9.2%) | 200.8 | 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18 |

| 해시태그 수 (제목+설명) | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 # |
|---|---|---|---|
| 해시태그 없음 | 44 (20%) | 268.4 | 6, 10, 13, 20, 69, 73, 76 |
| 1~2개 | 36 (11%) | 154.1 | 7, 58, 86, 90 |
| 3~5개 | 123 (8.9%) | 104.4 | 1, 3, 4, 9, 12, 25, 26, 34, 39, 43, 48, 59, 64, 68, 74 |
| 6개 이상 | 505 (9.5%) | 197.1 | 2, 5, 8, 11, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 27 |

많이 쓴 해시태그 (비교 집단 쇼츠 수 · 그 쇼츠의 성공 비율 · 성공 쇼츠 수): #shorts 213 (13%·33), #relaxingmusic 138 (12%·35), #힐링음악 110 (3.6%·20), #music 79 (10%·13), #카페음악 72 (0%·7), #플레이리스트 54 (1.9%·1), #youtubeshorts 51 (16%·7), #song 51 (9.8%·9), #healingmusic 51 (0%·7), #trending 46 (22%·13), #명상음악 45 (2.2%·9), #meditationmusic 45 (11%·15), #수면음악 44 (0%·3), #playlist 42 (2.4%·3), #lyrics 41 (12%·6), #cafemusic 40 (0%·4), #stressrelief 39 (13%·13), #감성음악 39 (0%·4), #매장음악 37 (0%·2), #love 35 (11%·8), #노동요 35 (0%·0), #viral 32 (16%·5), #sleepmusic 32 (12%·11), #집중음악 32 (0%·0), #불교음악 31 (9.7%·9)

## 5. 길이 (초)

- 중앙값: 성공 쇼츠 40초 · 비교 집단 성공 36초 · 나머지 41초

| 길이 | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 # |
|---|---|---|---|
| 0~14초 | 51 (12%) | 628.6 | 1, 5, 25, 27, 28, 29, 33, 46, 55, 65, 89, 96, 100 |
| 15~29초 | 159 (16%) | 400.3 | 2, 4, 6, 8, 11, 12, 16, 18, 19, 22, 23, 48, 49, 52, 53 |
| 30~44초 | 176 (6.8%) | 73.7 | 3, 7, 15, 17, 20, 26, 30, 34, 38, 39, 41, 45, 50, 57, 64 |
| 45~59초 | 113 (13%) | 131.3 | 9, 10, 13, 14, 21, 24, 42, 43, 47, 58, 61, 72, 78, 90, 98 |
| 60~89초 | 93 (6.5%) | 102.3 | 35, 37, 44, 54, 56, 62, 69, 84, 102, 103 |
| 90~180초 | 116 (6.9%) | 178.8 | 31, 32, 36, 40, 51, 63, 66, 70, 71, 73, 77, 80, 82, 86, 91 |

### 5-2. 아주 짧은 쇼츠 (15초 미만 — 한 장 정보·반복 재생형?) — 주제 관련 쇼츠 전부 (조회수 부풀림 의심 포함)

조회수는 2025-03-31 부터 다시 재생도 셈 → 아주 짧은 쇼츠는 한 사람이 여러 번 셀 수 있다. 광고로 산 조회수와 API 로 가를 수 없다

| 묶음 | 쇼츠 | 그중 부풀림 의심 | 채널 | 조회수 중앙값 | 좋아요/1천 | 길이 중앙값 |
|---|---|---|---|---|---|---|
| 15초 미만 | 385 | 35 | 76 | 26,917 | 7.8 | 11초 |
| 15초 이상 | 3474 | 42 | 475 | 7,558.0 | 13.6 | 50초 |

15초 미만 쇼츠 (조회수 순):

- 11초 · 30,092,659회 · 좋아요/1천 7.53 · 구독자 543,000 · Muso Method Ped… — Can you play PERFECT time? 🤯🎹 #piano #pianoteacher #pianolessons #cla… (https://www.youtube.com/shorts/9jbrElKajNo)
- 7초 · 29,092,421회 · 좋아요/1천 1.72 · 구독자 2,740 · ChauBeo · 부풀림 의심 — Submit your funny videos if you need background music!#trend #funny #… (https://www.youtube.com/shorts/ZhUWXhYqV6g)
- 12초 · 25,948,818회 · 좋아요/1천 0.0 · 구독자 65,900 · Asthetic_Lyrics — Misery ∣ Puppies Lyrics Edit Asthetic Theme Soul soothing Sound. (https://www.youtube.com/shorts/idTjtnPe5cM)
- 12초 · 25,623,712회 · 좋아요/1천 3.5 · 구독자 13,600 · NOVAE — I know I should sleep, but the voices in my head go… Arirang tour ver… (https://www.youtube.com/shorts/17UP7J8Ri3E)
- 12초 · 25,578,236회 · 좋아요/1천 3.63 · 구독자 206,000 · SmartBaby — She took her first piano lesson WAY too seriously! 🎹 🤣 (https://www.youtube.com/shorts/-pS0IVbmcZo)
- 7초 · 13,611,489회 · 좋아요/1천 7.13 · 구독자 107,000 · Leo — Who designed this Oreo?!😳#shorts #funny #memes #piano (https://www.youtube.com/shorts/cqh7psgif6Y)
- 13초 · 12,465,566회 · 좋아요/1천 6.25 · 구독자 225,000 · 살림아리 — 혼자 어떻게 찍냐고? 2탄 (https://www.youtube.com/shorts/-EbDCbATPDk)
- 10초 · 11,023,747회 · 좋아요/1천 19.2 · 구독자 1,980,000 · Matt Storer — Alien meets the President #comedy #music #parody of Work It by Missy … (https://www.youtube.com/shorts/fM71BRVXv1E)
- 14초 · 10,090,591회 · 좋아요/1천 5.08 · 구독자 50,100 · 아쮸 — 음악방송에 카메라 들고 올라간 아이돌 #kpop #shorts (https://www.youtube.com/shorts/Nw6ROTIJSaA)
- 12초 · 5,517,330회 · 좋아요/1천 13.42 · 구독자 100,000 · Maks Rayvan Sho… — Chinese tune #piano #pianist #pianomusic #pianotutorial #shortsviral … (https://www.youtube.com/shorts/4Q-ZlGppJmI)
- 5초 · 4,947,292회 · 좋아요/1천 10.13 · 구독자 53,700 · Lem2Viral — #instrumental (https://www.youtube.com/shorts/NGYAnuzyQFo)
- 4초 · 4,551,587회 · 좋아요/1천 2.08 · 구독자 766,000 · Herlyne Ven 🇨🇦 · 부풀림 의심 — Cute & Fun CoComeon Hippo Piano 🪗 #trending #pianomusic #music #toys … (https://www.youtube.com/shorts/aYxI0o751G0)

## 6. 첫 3초 · 7. 말과 끝맺음 (자료를 받은 쇼츠 — 대본이 있는 것)

성공 쇼츠 111개 (대본 0 · 말 없음 0) vs 나머지 받은 쇼츠 80개 (대본 0 · 말 없음 0) — 중앙값·몫

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

- 설명란에 롱폼·풀영상 연결(유튜브 영상 주소·'풀영상'·'본편'): 성공 쇼츠 3.6% · 나머지 받은 쇼츠 3.7% · 비교 집단 성공 0% · 나머지 7.1%

성공 쇼츠의 첫 줄·끝 줄 (원문):


## 8. 참여율 (조회수 1,000회당 — 중앙값)

| 묶음 | 수 | 좋아요/1천 | 댓글/1천 | 하루 조회수 |
|---|---|---|---|---|
| 비교 집단 성공 | 72 | 8.36 | 0.15 | 12,624.5 |
| 비교 집단 나머지 | 636 | 11.63 | 0.41 | 121.8 |
| 성공 쇼츠 (받은 것) | 111 | 11.29 | 0.17 | 8,513.2 |

## 9. 올린 요일 · 시각 (한국 시간 — 비교 집단, 표본이 작으면 흔들림)

| 요일 | 비교 집단 (성공 비율) | 성공 쇼츠 # |
|---|---|---|
| 월요일 | 119 (7.6%) | 2, 14, 18, 37, 39, 45, 59, 68, 90, 92, 93, 100 |
| 화요일 | 83 (13%) | 4, 11, 27, 31, 34, 44, 46, 48, 57, 64, 65, 70 |
| 수요일 | 89 (7.9%) | 5, 12, 17, 21, 23, 24, 28, 51, 52, 62, 69, 77 |
| 목요일 | 109 (15%) | 8, 9, 16, 20, 26, 29, 38, 40, 54, 56, 60, 63 |
| 금요일 | 83 (11%) | 1, 13, 25, 32, 35, 43, 49, 53, 55, 67, 78, 79 |
| 토요일 | 110 (7.3%) | 3, 15, 19, 30, 33, 36, 66, 72, 86, 105 |
| 일요일 | 115 (10%) | 6, 7, 10, 22, 41, 42, 47, 50, 58, 61, 71, 73 |

| 시각 | 비교 집단 (성공 비율) | 성공 쇼츠 # |
|---|---|---|
| 0~5시 | 60 (6.7%) | 1, 4, 7, 31, 41, 54, 61, 65, 71 |
| 6~8시 | 116 (7.8%) | 9, 21, 25, 59, 62, 68, 72, 82, 83, 84, 87, 91 |
| 9~11시 | 96 (14%) | 11, 27, 32, 35, 38, 42, 44, 46, 50, 52, 53, 57 |
| 12~14시 | 83 (11%) | 8, 12, 13, 22, 28, 30, 47, 49, 51, 56, 60, 88 |
| 15~17시 | 90 (5.6%) | 3, 17, 19, 24, 64, 67, 105 |
| 18~20시 | 133 (14%) | 2, 5, 16, 18, 23, 26, 34, 43, 45, 69, 78, 79 |
| 21~23시 | 130 (10%) | 6, 10, 14, 15, 20, 29, 33, 36, 37, 39, 40, 48 |

## 10. 채널 유형 · 빨리 크는 쇼츠 채널

채널 유형 = 채널 쇼츠 수(UUSH 목록) ÷ 채널 영상 수. 채널 쇼츠 수를 모르는 비교 집단 쇼츠 284개는 비율에서 뺐다 (평소 쇼츠는 승인한 쇼츠의 채널만 받으므로 모르는 채널은 거의 다 성공이 아님 — 넣으면 '쇼츠만 하는 채널'이 잘 되는 것처럼 보임). 아래도 승인한 쇼츠의 채널 쪽으로 치우쳐 있다

| 채널 유형 | 비교 집단 (성공 비율) | 채널 | 성공 쇼츠 # |
|---|---|---|---|
| 쇼츠만 (90% 이상) | 161 (21%) | 37 | 2, 4, 5, 6, 9, 10, 13, 15, 16, 20, 23, 24 |
| 쇼츠 위주 (50~90%) | 189 (13%) | 40 | 1, 3, 7, 11, 12, 14, 17, 18, 19, 21, 22, 25 |
| 롱폼 위주 (쇼츠 50% 미만) | 74 (16%) | 18 | 8, 26, 31, 34, 36, 54, 62, 63, 65, 66, 67, 70 |

빨리 크는 쇼츠 채널 (개설 24개월 안·구독자 1,000~200,000·쇼츠 몫 50% 이상 — 월 구독자 증가 순, 471곳 중):

| 채널 | 개설 | 구독자 | 월 구독자 증가 | 영상 수 | 쇼츠 몫 | 본 쇼츠 길이 중앙값 | 주로 다룬 주제 | 대표 쇼츠 |
|---|---|---|---|---|---|---|---|---|
| 𝐑𝐚𝐣𝐞𝐬𝐡_𝐞𝐝𝐢𝐭𝐳𝐳 💫 | 2026-07-15 | 138,000 | 42,864 | 144 | – | 16초 | 8. 로파이·시티팝·칠 | [chhoti bhen (lo-fi) song ∣ br…](https://www.youtube.com/shorts/PQD2n5CcoGk) 1,949,164회 |
| veerpulse | 2026-07-28 | 44,600 | 15,972 | 216 | 100% | 6초 | 기타 | [#relaxingmusic](https://www.youtube.com/shorts/p4dSlB1-18k) 512,616회 |
| Jazzy Love Active | 2026-07-24 | 46,400 | 15,870 | 105 | 100% | 20초 | 8. 로파이·시티팝·칠 | [💝 Ishq De Fanniyar ∣ Slowed +…](https://www.youtube.com/shorts/K0dMrCnd5Jw) 18,716,833회 |
| 명곡부활단 | 2026-03-21 | 105,000 | 14,866 | 316 | – | 52초 | 9. 가요·발라드·트로트 | [열애#열애 #윤시내 #추억의명곡 #추억의노래 #감성음…](https://www.youtube.com/shorts/lvEIFwI6VPk) 214,377회 |
| 연예뉴스_TV1 | 2025-12-17 | 130,000 | 12,806 | 416 | – | 62초 | 9. 가요·발라드·트로트 | [#미스터미스터 #뉴스#트로트](https://www.youtube.com/shorts/KSGNJijOoqk) 3,452,059회 |
| Late Hours ∣ Rela… | 2025-12-30 | 121,000 | 12,443 | 223 | – | 31초 | 1. 수면·명상·힐링 | [30s to Perfect Sleep Starts H…](https://www.youtube.com/shorts/w1JbQdML0XE) 60,807회 |
| Cafe Mellow | 2026-04-26 | 65,000 | 11,116 | 345 | – | 175초 | 7. 재즈·보사노바, 3. 공부·집중·작업 | [Soulful Saxophone That Touche…](https://www.youtube.com/shorts/vQE0PJTSWY0) 2,393,045회 |
| 클래식한소절 | 2026-06-15 | 45,800 | 10,892 | 78 | 100% | 34초 | 6. 피아노·클래식·연주곡, 7. 재즈·보… | [아무도 생각 못한 소리로 서부의 아이콘이 된 음악 #…](https://www.youtube.com/shorts/2ZKxQjF1V0I) 4,708,612회 |
| StudySmart with A… | 2025-10-08 | 131,000 | 10,549 | 171 | – | 51초 | 기타 | [Kya Music Sunte Sunte Padhai …](https://www.youtube.com/shorts/lr2FKwb7Sd4) 392,551회 |
| 하루순간 | 2026-05-10 | 55,500 | 10,239 | 188 | – | 8초 | 10. 팝송·K팝·J팝 | [이정도 거리면 해볼만 한데? #jpop](https://www.youtube.com/shorts/LwG3o0PKAww) 1,515,950회 |
| 로드차트 | 2026-02-13 | 81,600 | 9,936 | 242 | – | 61초 | 9. 가요·발라드·트로트 | [밴드 붕괴 직전, 고독이 만든 역대급 록발라드/Alw…](https://www.youtube.com/shorts/1AeJeaZoC3I) 2,361,173회 |
| シャドウビート | 2025-10-29 | 116,000 | 9,863 | 266 | – | 43초 | 11. 힙합·R&B·EDM | [電車が空いてるのに隣に座る男の末路 #パラ高 #LoFi …](https://www.youtube.com/shorts/dsUym1tu7G4) 1,878,357회 |
| Psych Theory | 2026-03-23 | 67,700 | 9,721 | 38 | – | 40초 | 3. 공부·집중·작업 | [3 Music Types That Can Boost …](https://www.youtube.com/shorts/t2cFkPUmTYs) 17,288회 |
| Darky lyrics | 2026-03-28 | 61,700 | 9,030 | 202 | – | 24초 | 6. 피아노·클래식·연주곡 | [Catwoman - Instrumental ∣ Moo…](https://www.youtube.com/shorts/ILcCxODj_eQ) 3,278,012회 |
| 영펭 yeongpin | 2026-06-25 | 35,100 | 8,979 | 111 | 85% | 20초 | 6. 피아노·클래식·연주곡, 1. 수면·명… | [A Dinosaur’s Love Story #pian…](https://www.youtube.com/shorts/imH34A_Y-3I) 17,256,941회 |
| 랭킹감자 | 2025-09-19 | 112,000 | 8,588 | 189 | – | 47초 | 기타 | [음악 전공자들이 노는 법 모음집](https://www.youtube.com/shorts/mVv07KPi1pA) 5,187,797회 |
| Lyric Suman Editz | 2026-01-25 | 73,600 | 8,329 | 152 | – | 16초 | 8. 로파이·시티팝·칠 | [Jeene Laga Hoon 💔 (Slowed + R…](https://www.youtube.com/shorts/L920dSnKVM0) 1,977,289회 |
| unlockroom | 2025-06-26 | 119,000 | 7,500 | 369 | – | 60초 | 기타 | [점점 산으로 간다는 송소희의 음악세계](https://www.youtube.com/shorts/7ihxCzpOwkk) 5,238,362회 |
| 숏플래시 | 2025-11-17 | 79,800 | 7,187 | 625 | – | 28초 | 기타 | [평생 아빠의 플레이리스트만 듣고 자란 딸의 최후](https://www.youtube.com/shorts/TOUASe0Fhvw) 1,833,080회 |
| 나야나클래식 | 2026-01-12 | 66,200 | 7,121 | 324 | – | 53초 | 6. 피아노·클래식·연주곡 | [버려질 뻔한 음악이 영화의 얼굴이 됩니다 #비하인드 …](https://www.youtube.com/shorts/WnXs8FFrXxk) 4,077,819회 |
| Lem2Viral | 2026-03-04 | 53,700 | 7,076 | 558 | – | 5초 | 6. 피아노·클래식·연주곡 | [#instrumental](https://www.youtube.com/shorts/NGYAnuzyQFo) 4,947,292회 |
| 7080 음악 감성트롯 | 2025-10-02 | 89,100 | 7,045 | 659 | – | 58초 | 9. 가요·발라드·트로트 | [혼자 걷던 길도 당신과 함께라면 외롭지 않습니다...…](https://www.youtube.com/shorts/2jKHWmTT7GM) 573,759회 |
| 추억의 음악다방 | 2025-10-21 | 81,800 | 6,803 | 302 | – | 56초 | 9. 가요·발라드·트로트 | [전화 잘못 걸었다고 차마 말을 못해서 나온 레전드 감…](https://www.youtube.com/shorts/-j-BAy76Frc) 81,592회 |
| Janny Love Active | 2026-07-22 | 19,300 | 6,456 | 79 | 100% | 20초 | 8. 로파이·시티팝·칠 | [💝 Ishq De Fanniyar ∣ Slowed +…](https://www.youtube.com/shorts/DF-BBMCHDg8) 3,062,351회 |
| Cartoon Craze | 2025-10-22 | 73,000 | 6,105 | 54 | – | 46초 | 기타 | [The pain in background music …](https://www.youtube.com/shorts/dsNr7EESQU0) 732,284회 |

## 11. 시청자 니즈 (성공 쇼츠 댓글 — 시청자 댓글 44,086개, 도배 19개 뺌, 채널 주인 댓글 뺌, 정보 요청이 아닌 부탁(띠·로또·노래 등) 0개는 질문·요청에서 뺌)

| 갈래 | 댓글 | 몫 | 좋아요 합 |
|---|---|---|---|
| 좋은 점 — 영상 (도움·설명·정리·공감) | 59 | 0.1% | 7,208 |
| 감사·응원 (일반) | 348 | 0.8% | 1,753 |
| 더 알고 싶은 것 (질문·요청) | 41 | 0.1% | 200 |
| 아쉬운 점 — 영상 (제목·광고·길이·정보 오류·목소리) | 38 | 0.1% | 237 |
| 반박·불만 — 의견 다름 (내용) | 44 | 0.1% | 194 |
| 정치·사회 (영상과 무관한 의견) | 39 | 0.1% | 59,476 |
| 경험 공유 (내 이야기) | 235 | 0.5% | 4,420 |
| 구독·다음 기대 | 9 | 0% | 18 |
| 더 자세히·긴 영상 요청 (풀영상·2탄·자세히) | 32 | 0.1% | 6,262 |

### 11-1. 요청 — '다뤄 주세요·알려 주세요' 16개 (다음 쇼츠·롱폼 주제 후보)

- #22 👍4 “손열음은 집중해서 깊이 들어갈 때 늘 항상 뭐라고 말을 하는것 같은데.... 넘 궁금해요^^ 뭐라고 하는 걸까요?ㅎ”
- #44 👍2 “여기애 나오는 억기즐 전부 다 궁금합니다”
- #51 👍2 “멋진곡 입니다 잘 감상했습니다 계속 올려주세요😊”
- #14 👍1 “노래를 듣고 어떤 생각을 하셨는지, 어떤 마음으로 노래를 부르시는지 궁금합니다🤔”
- #44 👍1 “작곡가 누구신지요? 알고싶어요”
- #51 👍1 “감사합니다 이럭해 예절한 노래을🎉🎉🎉 더조은 만이부탁드려요”
- #9 👍0 “피아노 보다 저거 떨구면 어떻게 될까 궁금해서 봤는데, 속았당.”
- #10 👍0 “보라색 가디건 입으신 여성 분 풀버전 궁금하다 😮”
- #13 👍0 “이런방송 너무좋아 많이 올려주세요 감사합니다❤”
- #13 👍0 “진찌 너무나 좋네요❤❤한국도 이 프로 사와서 방송 해 주세요”
- #45 👍0 “여름비 도 부탁드려요 😂😂”

### 11-2. 더 자세히·긴 영상 요청 (풀영상·2탄·자세히)

- #10 👍5272 “정보) 원본영상은 7만1000조회수 이지만 이 쇼츠는 154만2300조회수 이다”
- #43 👍72 “핸드폰의 순기능 올초 이곡 전체영상 보고 감탄 여자분의 휫파람이 일품”
- #43 👍11 “와. 진짜 잘 만든 음악이네. 자세히 들으니 훨씬 구성이 장난아님이 느껴진다”
- #44 👍9 “이분 이름이 뭘까요? 전체 영상을 보고 싶습니다.”
- #76 👍1 “애원 원본분 맨날 보는 사람으로서 정말 좋은🥰”
- #10 👍0 “풀영상이 시급합니다❤”
- #13 👍0 “봐도봐도 레전드!! 몇번을 보는지 몰라... 이거 풀 영상 없나요?”
- #13 👍0 “풀영상 보고싶네”

### 11-3. 물음표 질문

- #22 👍11 “혹시 이 협주곡은 몇 번일까요?!”
- #58 👍7 “50이 되어도 자유롭지 않죠 언제 자유롭게 되나요?”
- #102 👍5 “이노래 어떻게 다운받나요?”
- #44 👍3 “전체음악을 어디서 들을수있을까요?”
- #14 👍1 “아파트단지 같은데 유리창 하나 두고 혹시 방음이 되나요? 노래는 잘 들었습니다”
- #44 👍1 “이건어느나라인가요????”
- #83 👍1 “이노래 풀버전 어떻게 듣나요?”
- #13 👍0 “풀 영상 어디서 보나요?😅”
- #13 👍0 “어디서 볼수 있나요?”
- #22 👍0 “그대의 아름다움을 어떻게 표현 해야 할까요? 그냥 ….. 귀만 열어 두고 있기가 송구 할 뿐 …”
- #43 👍0 “황야의 무법자 장고 햇갈리네요 장고 맞나요?”
- #43 👍0 “서부 영화와 이렇게 잘 어울리는 음악이 있을까요? 리반클리프,클린트이스트우드도 최고였는데...”
- #45 👍0 “펨풀륫은 루마니아가 아니라 아메리카 원주민 고유악기입니다. 원조라고 할수있겠습니다. 그런데요, 아메리카 원주민(인디언)은 어디서왔을까요? 명백한 동양인이고 동양인 조상은 고려입니다. 참역사적 팩트입니다.”
- #45 👍0 “비교적 최근에 어디서 들었지 했는데 영화 킬빌에도 나오지 않나요?”
- #67 👍0 “선생님~~이노래 악보 구할 수 있을까요?”
- #67 👍0 “안녕하세요 혹시 이 음악 악보도 있을까요??”

### 11-4. 아쉬운 점 — 영상

- #10 👍115 “​@j43nfromss ㅋㅋㅋㅋㅋ ㅈㄴ 호들갑 떠는 자막이랑 출연진 하나하나 클로즈업하면서 계속 반복하는 연출ㅋㅋㅋㅋㅋㅋㅋ 진짜 채널 바로 돌려버림ㅋㅋㅋ”
- #13 👍29 “​@sonhj3949그러기엔 그냥 예능도 무한반복인디”
- #43 👍24 “방갤리스. 엔리오모리꼬네. 이 두분 음악만 남은 인생 평생 들어도 인생이 지루하지 않을것같음.”
- #63 👍20 “정말 스님입니까? 아님 AI목소리 인가요~~넘 잘부르시네요??목소리도 좋고요 감사합니다 잘듣고 갑니다~”
- #10 👍18 “ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ진짜 제발 편집방식 좀 바꿔 같은 장면 반복해서 보여주는 거 누가 먼저 시작했냐”
- #67 👍10 “선생님 안녕하세요.저 주은이에요. 아이들 목소리가 너무 귀여워요.”
- #13 👍7 “인정 ㅋㅋㅋㅋㅋㅋ 게스트 반응 관심 ㅈ도 없는데 자꾸 게스트만 두 세 번 쳐 반복해서 보여줌”
- #78 👍3 “넘 복스럽고 넘 좋아했는데 넘 아쉽네요❤❤”
- #6 👍1 “​@twosoul_real 댓글에 틀린 정보가 많네요”
- #9 👍1 “마지막 댓 ai 같노”
- #45 👍1 “지금 이 지휘자가 병원에 입원했다고 해서 마음이... 세월이 아쉽네요”
- #6 👍0 “아 이거 full reaction 뭐 그런건 줄 알았더니 look at ya 반복이네.”
- #9 👍0 “화질만 봐도 ai”
- #22 👍0 “손열음 이란 피아니스트 유투브 영상으로 첨봤는데 유명하단 피아니스트 좀지루한면 있어서 별흥미를 못느꼈는데 신기하고 겨ㅣ속 보고싶네요”
- #22 👍0 “피아노 소리는 밴드였을때가 멋지지 지루한 클래식”

### 11-x. 좋은 점 — 영상 (도움·설명·정리·공감)

- #10 👍5158 “3번째분 스페이스할때 듣기좋다”
- #13 👍1516 “이거뭔가 묘한게..뚱딴지같이 노래보다 더 먼저 와닿는게 삶은 이렇게 살아야겠다 라는게 느껴짐 어두워도 언제빛을 볼지 모른다는 마음으로 준비하고, 기회가 왔을때 힘껏 내가가진 기량를 펼친뒤 타인에게도 그 기회가 돌아갔을때 최선을 다해 박수쳐주는거. 이…”
- #64 👍334 “이성경이 젤 듣기좋다;;”
- #10 👍36 “3번째가 진짜 레전드네”
- #43 👍19 “휘파람 소리가 진짜 레전드 지~”
- #14 👍11 “커버중에 가장 듣기 좋습니다”
- #56 👍9 “청아한 목소리로 한이 실린 가사를 한올 한올 풀듯이 엮어내는 소리는 만인의 심금을 울려 줍니다 좋은영상 감사드립니다 구독과 좋아요 누르고 갑니다”
- #94 👍8 “감사합니다 감사합니다 넘좋아 요가슴애 와닿는 것이 눈물이나 네요 감 사합니다 성불하십시요 ❤❤❤❤❤❤❤”

### 11-x. 경험 공유 (내 이야기)

- #13 👍1516 “이거뭔가 묘한게..뚱딴지같이 노래보다 더 먼저 와닿는게 삶은 이렇게 살아야겠다 라는게 느껴짐 어두워도 언제빛을 볼지 모른다는 마음으로 준비하고, 기회가 왔을때 힘껏 내가가진 기량를 펼친뒤 타인에게도 그 기회가 돌아갔을때 최선을 다해 박수쳐주는거. 이…”
- #43 👍814 “어릴때 저음악을 내 입으로 와와와 했었는데, 정말 입소리였구나..”
- #64 👍307 “이성경이 왜 제일좋은가 생각해봤더니 노래 자체가 뮤지컬이랑 어울려서 그런듯”
- #43 👍266 “기타소리 시작될 때 나도 모르게 "크으...!" 감탄함”
- #6 👍67 “내가 항상 카니에 음악을 초창기부터 들으면서 느낀 부분은 트렌드를 선구하기도 하고 앞서간 뮤지션이라고 늘 생각했음. 천재들중 천재라고 생각함. 거기다가 실행력 및 도전정신까지..... 대단한 사람임”
- #45 👍26 “눈물 나도록 환상 입니다”
- #45 👍19 “내가 세상을 떠나고 흙으로 돌아가도 이 음악은 새로운 사람들에게 감동을 줄겁니다. 그래서 음악이 존경스러워요....”
- #80 👍11 “관세음보살 관세응보살 관세음보살 우리엄마 어기까지만 아프고 더이상은 아프지마시길 ()()() 우리아버지도 더이상은 아프지마시길 ()()() 우리 부모님 사랑합니다♡♡♡”

### 11-x. 구독·다음 기대

- #45 👍12 “잠안올때 들어면 너무좋은 명곡연주입니다..외로운 양치기 팬입니다😊😊🎉🎉”
- #14 👍1 “와진짜 미쳤다 .. 소름돋을정도로 잘하셔서 듣고 구독했어요ㅠㅜㅜㅜ 초반부분에 반가성? 어떻게 내시는건가요,, ??!?!”
- #43 👍1 “와우~어릴적 재밌게 보던 토요명화 생각납니다 그때는 서부영화들 정말 기다리며 보았지요 이 음악이 이렇게 만들어졌다니 신기하고 놀라워요^^ 구독합니다 🍂”
- #44 👍1 “고등학교 다닐때 중앙대다니던 대학생오빠가 매일듣던곡인데 벌써 40년전이네. 내가 제목이 뭐냐고묻자 엘콘돌파사 라고.”
- #51 👍1 “한쪽 가슴이 찡하고 아려요 아파요 진심으로 부르는 모습에 감동을 받고 힘찬박수 보냅니다 방금 구독완료 하였습니다 열렬히 응원합니다”
- #58 👍1 “예전에 듣던 영상 팝송 또 너무 좋아요. 구독하고 또 오겠습니다”
- #76 👍1 “애원이랑 너와나이랑 증오의 창조물 내가 엄청좋아하는 lms인데 감사해요 너무 잘만드셨어요 구독 좋아요 알림설정하고갈께요 🎉”
- #6 👍0 “좋은 노래 네요. 같이 공유하고 싶어서 구독했어요. 대단해요❤❤”

## 12. 사례별 · 표지

사례별 (대본 전문·첫 3초·끝 줄·설명·댓글): [`cases_01.md`](cases_01.md) (#1~#15), [`cases_02.md`](cases_02.md) (#16~#30), [`cases_03.md`](cases_03.md) (#31~#45), [`cases_04.md`](cases_04.md) (#46~#60), [`cases_05.md`](cases_05.md) (#61~#75), [`cases_06.md`](cases_06.md) (#76~#90), [`cases_07.md`](cases_07.md) (#91~#105), [`cases_08.md`](cases_08.md) (#106~#111)

성공 쇼츠 표지 (번호 = 1번 표의 #): [`thumbs_01.jpg`](thumbs_01.jpg) (#1~#24), [`thumbs_02.jpg`](thumbs_02.jpg) (#25~#48), [`thumbs_03.jpg`](thumbs_03.jpg) (#49~#72), [`thumbs_04.jpg`](thumbs_04.jpg) (#73~#96), [`thumbs_05.jpg`](thumbs_05.jpg) (#97~#111)

받은 쇼츠 전부 (업로드 최근 순·글 출처·댓글): [`approved.md`](approved.md) · 비교 집단 숫자: [`compare.csv`](compare.csv)

