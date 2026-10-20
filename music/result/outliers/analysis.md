# 음악 — 성공 사례 분석 (지시사항 재료)

자동 생성 — `tools/success_analysis.py` v1.4.1 (2026-10-20 07:59 UTC), 규칙 `music/analysis_rules.toml` v1.4. **이 문서는 숫자와 원문만 담는다 — 해석·지시사항은 이것을 읽는 AI 가 만든다.** 주별 추세는 `weekly.md`, 승인한 영상 전부는 `approved.md`. ※ 연구·교육용 — 투자 권유가 아님.

## 0. 자료와 한계

| 자료 | 수 |
|---|---|
| 사례 폴더 (설명·자막·댓글·썸네일을 받은 영상) | 1426 (웹 승인 1426) |
| **성공 사례** — 180일 안·구독자 50,000 이하·조회수 ≥ 구독자 × 3·10,000회 이상·4분 이상, 채널당 2개 | **1114** (기준 통과 1300 − 뺀 것 47 − 채널당 제한 139) |
| 성공 사례의 글 출처 (자막·음성인식·설명·없음) | 설명 1038 · 없음 76 |
| 성공 사례 대본 — 전체 · 앞부분만(음성인식 1차) · 없음 | 0 · 0 · 1114 |
| 같은 채널 기준선 (채널 평소 영상) | 성공 사례 992/1114 · 채널 1018곳 (잘된 영상 3485 · 평소 영상 4098) |
| 성공 사례 댓글 (받은 / 달린) | 437,275 / 453,104 |
| 성공 사례 썸네일 | 1114 |
| 비교 집단 — 탐색에서 본 영상 중 구독자 50,000 이하·4분 이상·365일 안·주제 관련, 채널당 최근 5개 | 5810 (성공 1197 = 21%, 채널당 제한으로 뺀 22035) |
| 자료를 받지 않은 성공 후보 (웹 화면에서 승인하면 들어감 — 채널당 자리가 남은 것만) | 684 (자리가 찬 채널의 2,819개 뺌) |
| 수요·공급 시장 — 최근 90일 영상 (채널 크기 상관없음) | 921 · 검색어 61 · 자동완성 말 505 (공급 확인 0) |
| 채널 성장 자료 (개설일이 있는 채널) | 2150 (빨리 크는 작은 채널 25) |

성공 기준은 넘었지만 뺀 영상: Main Kabhi Bhoolunga Na Tujhe… (광고 의심(좋아요·댓글 거의 없음)) · Noah Kahan - Haircut (Officia… (광고 의심(좋아요·댓글 거의 없음)) · SAD LO-FI 🥺 💔 2026 Ultimate M… (광고 의심(좋아요·댓글 거의 없음)) · Repvblik - Sandiwara Cinta (K… (광고 의심(좋아요·댓글 거의 없음)) · Baby Bear ∣ Colorful Caterpil… (광고 의심(좋아요·댓글 거의 없음)) · "Free" Cover ∣ Rumi Was Left … (광고 의심(좋아요·댓글 거의 없음)) · 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 틀기만 해도 기분이 좋아지는 가을 플… (광고 의심(좋아요·댓글 거의 없음)) · Nain Tere 🖤 Slowed + Reverb ∣… (광고 의심(좋아요·댓글 거의 없음)) · মন ছুঁয়ে যাওয়া বাংলা ∣∣ Bes… (광고 의심(좋아요·댓글 거의 없음)) · Dupatta Sarak Raha Hai 💕 ∣ Sl… (광고 의심(좋아요·댓글 거의 없음)) · I’d Rather – Acoustic + Saxop… (광고 의심(좋아요·댓글 거의 없음)) · SAD LO-FI 🥺 💔 2026 Ultimate M… (광고 의심(좋아요·댓글 거의 없음))

**한계**

- 대본(자막·음성인식)이 없는 성공 사례 1114개 (#1, #2, #3, #4, #5, #6, #7, #8, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26, #27, #28, #29, #30 …) — 설명란·챕터만 있음. 도입부·구성·말 속도는 대본이 있는 0개로만 셌다 (음성인식이 끝나면 다시 셈)
- 비교 집단 5810개 = 검색(조회수 순 — 잘된 영상 쪽으로 치우침)·추가한 채널·성공 사례 채널의 평소 영상 4548개 (치우침 없음) 에서 올린 지 7~365일 영상, 성공 비율 21% — 실제 시장 비율이 아니다. 같은 집단 안의 '있음/없음' 차이로만 보고, '무엇이 먹혔나'는 1-2번(같은 채널 안)을 먼저 보라
- 외국 영상을 넣음 (주제 설정 INCLUDE_FOREIGN = true) — 성공 사례 중 외국 영상 736개 (#1, #4, #5, #6, #7, #8, #9, #10, #13, #14, #15, #17, #18, #19, #21, #22, #23, #25, #29, #30, #32, #34, #35, #38, #39, #40, #41, #42, #43, #44). 말 속도(한글 음절)는 한국어 영상만으로 셌고, 제목 특징·댓글 갈래(질문·요청 등)는 한국어 낱말 규칙이라 외국 영상에는 거의 걸리지 않는다 — 외국 사례는 원문을 직접 읽어라
- 같은 채널 기준선이 있는 성공 사례 992/1114개 (채널 영상이 5개 미만이거나 아직 못 받음)
- 수요·공급의 '시장'은 탐색·검색에서 본 최근 90일 영상 921개 — 검색이 조회수 순이라 조회수 적은 영상이 덜 잡힌다. 주제 묶음 사이의 상대 비교(지수)로만 보라
- 자동완성 말의 '최근 영상 수'는 우리가 본 영상만 셌다 — 실제 공급은 웹 화면 [공급 확인](말 하나에 검색 1번 = 100단위)으로 확인
- 자동완성 말에는 책·방송·사람·채널 이름도 섞인다 (예: '…를 찾아서'·'…지침서') — 영상 주제가 아닌 말은 건너뛰고 읽어라
- 채널의 최근 구독자 증가는 구독자 수를 3일 넘게 사이를 두고 두 번 이상 받아야 나온다 (7일마다 다시 받음)
- '구독자가 많이 모이는가'는 YouTube API 로 영상별 구독 증가를 볼 수 없다 — 대신 채널 성장(7번: 개설 뒤 월 구독자·받을 때마다 남긴 기록), '구독·다음 기대' 댓글, 배수(조회수÷구독자)로 본다
- 댓글 갈래·제목 특징은 낱말 규칙이라 거칠다 (물음표 반문도 '질문', 한 댓글이 여러 갈래). 원문 인용을 함께 보라
- '눈에 띔'은 차이가 크고 표본이 충분하다는 표시일 뿐 원인이 아니다

## 1. 성공 사례 (1114개 — 배수 큰 순)

배수 = 조회수 ÷ 구독자. **채널 평소 대비** = 조회수 ÷ 그 채널 최근 롱폼 조회수 중앙값 (같은 채널 기준선 — 클수록 그 영상만의 힘). 썸네일은 5번(장마다 20개, 번호 = #), 사례별 자세히는 **`analysis_cases_01.md` …** (9번).

| # | 제목 | 채널 | 구독자 | 조회수 | 배수 | 채널 평소 대비 | 하루 조회수 | 길이 | 업로드 | 주제 묶음 | 형식 | 글 출처 | 댓글 받은/달린 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Jay Wheeler, Omar Courtz - De Lejitos (Remix) (Video Oficia…](https://www.youtube.com/watch?v=xCkf2L7gFnI) | JayWheelerVEVO | 6,750 | 120,974,274 | 17,922.1 | ×161.3 | 844,559.2 | 4.7분 | 2026-05-30 | 기타 | 음악 | 설명 | 4,024/4,031 |
| 2 | [너의 차선](https://www.youtube.com/watch?v=B9zWtLub7tk) | 조선힙합 - Topic | 25 | 1,504,015 | 15,040.1 | ×98.7 | 13,665.6 | 4.2분 | 2026-07-02 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 0/50 |
| 3 | [노엘 IT'S YOU (한요한 없는 버전 10m)](https://www.youtube.com/watch?v=82Li_A-cPWA) | 갱갱 | 77 | 456,066 | 4,560.7 | – | 2,785.3 | 10.3분 | 2026-05-09 | 기타 | 플레이리스트·모음 | 설명 | 123/123 |
| 4 | [Tìm Em](https://www.youtube.com/watch?v=PnGk00MuNM4) | Hngle - Topic | 1,350 | 4,516,129 | 3,345.3 | – | 36,481.8 | 4.6분 | 2026-06-18 | 기타 | 음악 | 설명 | 0/226 |
| 5 | [ขึ้นใจ (3am call)](https://www.youtube.com/watch?v=r1Eb1qnqLzA) | Mirrr - Topic | 4,290 | 12,407,651 | 2,892.2 | ×714.8 | 139,153.2 | 4.4분 | 2026-07-23 | 기타 | 음악 | 설명 | 0/280 |
| 6 | [Veer Hanumana Ati Balwana Ram Ram Ratiyo Re ∣ Arji Hamari M…](https://www.youtube.com/watch?v=DJjel4bCD8A) | Studio Hariom | 1,180 | 2,433,772 | 2,062.5 | ×2,140.5 | 16,420.1 | 6.8분 | 2026-05-25 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 137/137 |
| 7 | [Ye Tune Kya Kiya (Slowed + Reverb) 🎧 ∣ Lofi Version ∣ Once …](https://www.youtube.com/watch?v=jqVvhD8Bps4) | Vɪʙᴇ Bʏ Lᴏғɪ | 2,500 | 4,987,053 | 1,994.8 | ×4,094.5 | 58,628.3 | 4.8분 | 2026-07-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 363/363 |
| 8 | [झूमका झूलनिया Slowed + Reverb ∣ KhesariLal Yadav ∣ Bhojpuri…](https://www.youtube.com/watch?v=UgjIqEE-Eok) | officialprince | 1,910 | 3,693,206 | 1,933.6 | ×738.6 | 51,503.4 | 4.5분 | 2026-08-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 327/327 |
| 9 | [Khat navajot Ahuja / BGM THE BEST SONG 🥰#viral](https://www.youtube.com/watch?v=KdCRd8wTjaA) | ANSHU FF 1M | 389 | 705,659 | 1,814.0 | ×5,556.4 | 5,429.0 | 4.9분 | 2026-06-12 | 기타 | 음악 | 없음 | 26/26 |
| 10 | [Tera Hua Sahiba](https://www.youtube.com/watch?v=43sXuUq5N08) | Garvit Soni -… | 1,440 | 2,460,353 | 1,708.6 | – | 23,188.2 | 4.7분 | 2026-07-06 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/74 |
| 11 | [그대 사랑하는사람 나였으면](https://www.youtube.com/watch?v=E0EJikB3jg4) | ㅠㅁㅠ | 191 | 323,292 | 1,692.6 | – | 5,578.8 | 27.9분 | 2026-08-23 | 기타 | 정보·해설 | 없음 | 79/88 |
| 12 | [[playlist] 일하다 어깨 들썩이는 케이팝 노동요 ∣∣ 4K MV](https://www.youtube.com/watch?v=whggKiGBSx4) | 노래듣는 고영희 | 2,390 | 3,849,689 | 1,610.8 | ×1,612.4 | 50,536.8 | 148.4분 | 2026-08-05 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 193/196 |
| 13 | [When men loves you harder😭🌷](https://www.youtube.com/watch?v=2q4x4Ftz7mg) | wavy~ | 1,660 | 2,378,841 | 1,433.0 | ×177.7 | 66,431.8 | 9.3분 | 2026-09-14 | 기타 | 플레이리스트·모음 | 설명 | 487/507 |
| 14 | [DARKHAAST ❤️ ∣ Arijit Singh ∣ Slowed + Reverb ∣ LoFi Chill …](https://www.youtube.com/watch?v=DV1zd-C_Sms) | softtune 🎧 | 228 | 319,858 | 1,402.9 | ×484.6 | 4,978.9 | 6.9분 | 2026-08-17 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 18/18 |
| 15 | [Playlist for how a villain in love sounds like 🎧🔥✨.](https://www.youtube.com/watch?v=4NVS6d5eGyA) | Fictional Hea… | 2,920 | 4,092,694 | 1,401.6 | – | 74,520.3 | 9.7분 | 2026-08-26 | 기타 | 플레이리스트·모음 | 설명 | 324/325 |
| 16 | [ℙ𝕝𝕒𝕪𝕃𝕚𝕤𝕥 : 늙크크들 원기 회복시킬 애니 플리](https://www.youtube.com/watch?v=RbGKWnzZ0zI) | 연하네의 쓸만한 플레이리… | 826 | 1,142,441 | 1,383.1 | ×1,080.8 | 19,063.2 | 124.7분 | 2026-08-21 | 기타 | 플레이리스트·모음 | 설명 | 348/354 |
| 17 | [Cigarettes After Sex — late night playlist](https://www.youtube.com/watch?v=G5SAO7jS8xk) | ahmet | 1,130 | 1,547,866 | 1,369.8 | ×376.6 | 26,832.0 | 55.8분 | 2026-08-23 | 기타 | 플레이리스트·모음 | 설명 | 180/188 |
| 18 | [RAIM LAODE FULL ALBUM LAGU TERBAIK INDONESIA THE BEST MUSIC…](https://www.youtube.com/watch?v=plAW6z1Ex-w) | Playlist musi… | 2,260 | 3,034,153 | 1,342.5 | – | 25,793.2 | 18.2분 | 2026-06-24 | 기타 | 플레이리스트·모음 | 없음 | 306/312 |
| 19 | [JENNIE - FALLEN ANGEL (Official Video)](https://www.youtube.com/watch?v=s466YCiHfKw) | JennieRubyJan… | 24,500 | 32,524,835 | 1,327.5 | – | 611,755.9 | 5.7분 | 2026-08-28 | 10. 팝송·K팝·J팝 | 한 곡 | 설명 | 93,592/93,702 |
| 20 | [[Playlist] 코로나 전 오묘한 케이팝](https://www.youtube.com/watch?v=u7X8DqyBr64) | 원영 | 275 | 357,426 | 1,299.7 | – | 4,104.5 | 16.4분 | 2026-07-25 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 331/332 |
| 21 | [Achhi lagti ho (slowed + reverb ) lofi varsion 🎧](https://www.youtube.com/watch?v=AMg46cfQH8A) | lofi song 45 | 1,540 | 1,993,943 | 1,294.8 | ×346.7 | 29,837.2 | 5.1분 | 2026-08-14 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 182/182 |
| 22 | [Deltarune Ch. 5: Egg Room (FULL VERSION)](https://www.youtube.com/watch?v=I0S5CyJoZpw) | Clowd | 1,180 | 1,479,213 | 1,253.6 | – | 12,771.5 | 7.6분 | 2026-06-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,544/1,544 |
| 23 | [Kalyani [slowed & Reverb] ∣∣ With Shreya Ghoshal ∣∣Arjn / K…](https://www.youtube.com/watch?v=rbt6SjoZlWU) | TRL Lofi | 3,880 | 4,801,927 | 1,237.6 | ×1,978.5 | 49,075.1 | 4.4분 | 2026-07-14 | 기타 | 음악 | 설명 | 156/156 |
| 24 | [𝐑 𝐄 𝐙 𝐄](https://www.youtube.com/watch?v=mkRnOwNkpaQ) | iamkorean | 767 | 947,893 | 1,235.8 | – | 5,755.1 | 17분 | 2026-05-08 | 기타 | 음악 | 설명 | 211/212 |
| 25 | [Tum Ho Toh - Mashup 2026 ∣ Romantic Love Song ∣ Bollywood S…](https://www.youtube.com/watch?v=EmsrY9EQSSE) | VS Lofi Offic… | 2,230 | 2,718,405 | 1,219.0 | ×846.3 | 49,183.1 | 5.2분 | 2026-08-26 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 43/43 |
| 26 | [𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 가을 설레발 플리](https://www.youtube.com/watch?v=ams0ZufCafU) | 또잉 | 224 | 263,291 | 1,175.4 | ×727.3 | 4,989.5 | 19.6분 | 2026-08-28 | 기타 | 플레이리스트·모음 | 없음 | 17/18 |
| 27 | [별로 좋지 않은 하루를 보냈다고 생각할게](https://www.youtube.com/watch?v=wEwVgzsbqH4) | 니똥칼라똥 | 454 | 532,524 | 1,173.0 | – | 4,169.7 | 18.9분 | 2026-06-14 | 기타 | 플레이리스트·모음 | 없음 | 111/112 |
| 28 | [어른여자.mp3](https://www.youtube.com/watch?v=Ir8CBRecz7g) | 리 세이 | 510 | 595,690 | 1,168.0 | ×1,456.5 | 3,700.9 | 16분 | 2026-05-12 | 기타 | 플레이리스트·모음 | 설명 | 83/83 |
| 29 | [uMoya 2.0 (Tycoon Remix)](https://www.youtube.com/watch?v=HropgeYirpE) | Darque - Topic | 1,330 | 1,551,636 | 1,166.6 | ×15.2 | 38,874.0 | 8.7분 | 2026-09-10 | 기타 | 음악 | 설명 | 0/371 |
| 30 | [Hey Paaro - Full Song Bgm Raj The Show Man Puneeth Rajkumar…](https://www.youtube.com/watch?v=sj0JDjmC3es) | Mmusicworld46 | 322 | 370,282 | 1,149.9 | ×27.6 | 5,153.7 | 5.3분 | 2026-08-09 | 기타 | 음악 | 설명 | 7/7 |
| 31 | [[ 2024~2026 K-POP ] 최신곡 포함❗️ 랜덤 플레이 댄스 #랜덤플레이댄스 #kpop #2024…](https://www.youtube.com/watch?v=JnuZqf_O2N0) | 메이플 | 1,120 | 1,234,441 | 1,102.2 | – | 14,659.9 | 12.6분 | 2026-07-28 | 10. 팝송·K팝·J팝 | 한 곡 | 없음 | 86/93 |
| 32 | [🌙 Late Night Hindi Playlist ∣ Relax • Study • Sleep ∣ Mysti…](https://www.youtube.com/watch?v=1eFr1phNoxQ) | Mystic Scenery | 1,860 | 1,980,856 | 1,065.0 | – | 26,883.1 | 25.2분 | 2026-08-07 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 74/75 |
| 33 | [어 난데 여기 핫플이야](https://www.youtube.com/watch?v=JcIBpx-tGdA) | 햄 | 673 | 715,592 | 1,063.3 | ×1,233.8 | 4,368.4 | 24.1분 | 2026-05-09 | 기타 | 정보·해설 | 없음 | 84/84 |
| 34 | [Andekhi Anjaani si ∣ Slowed x Reverb ∣ lofi song ∣ lofi ver…](https://www.youtube.com/watch?v=FrqyfSyxOc4) | Midnight lofi… | 4,050 | 4,140,683 | 1,022.4 | ×776.7 | 86,494.6 | 6분 | 2026-09-02 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 132/132 |
| 35 | [THEN・❥・ Sweet Dreams ∣ Cinematic Techno](https://www.youtube.com/watch?v=0QAKKYJJ2l0) | THEN | 9,750 | 9,835,942 | 1,008.8 | ×2,234.9 | 73,591.5 | 4.4분 | 2026-06-08 | 기타 | 커버·직접 부른 노래 | 설명 | 491/491 |
| 36 | [3분 안에 잠드는 수면 음악 (30분) Fall Asleep in 3 Minutes (30 Min)](https://www.youtube.com/watch?v=E96njddrM5o) | 수면과학연구소 Sleep… | 89 | 99,756 | 997.6 | ×151.6 | 727.1 | 30분 | 2026-06-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/12 |
| 37 | [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 사랑한다고 속삭여줘](https://www.youtube.com/watch?v=Tt_TimRh73Q) | 뜨신아아 | 1,060 | 1,041,376 | 982.4 | ×282.1 | 8,028.6 | 23.4분 | 2026-06-12 | 기타 | 플레이리스트·모음 | 설명 | 60/63 |
| 38 | [🎧 Le Main Saiyaan Aa Gayi (Lofi) ∣ Mohabbatein ∣ Shah Rukh …](https://www.youtube.com/watch?v=NVf0GhbUmAw) | BOYS KING 99.… | 2,470 | 2,385,909 | 966.0 | ×654.2 | 26,727.7 | 7.5분 | 2026-07-23 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 175/175 |
| 39 | [POV You're back in the 90s 💗📻 ∣ Old hindi songs ∣ Bollywood…](https://www.youtube.com/watch?v=4GMIMevMn6Y) | Manii | 2,510 | 2,335,680 | 930.5 | ×61.6 | 41,287.7 | 8.2분 | 2026-08-24 | 기타 | 음악 | 설명 | 803/835 |
| 40 | [Toota Rahunga](https://www.youtube.com/watch?v=qN9Vw9v2nLY) | Garvit Soni -… | 1,440 | 1,330,706 | 924.1 | – | 14,646.2 | 4.1분 | 2026-07-21 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/48 |
| 41 | [Teri yaadon me khoya rahta hu song mind relax lofi song (sl…](https://www.youtube.com/watch?v=JJy3EqcgJdI) | VNS HIMANSHU … | 6,120 | 5,547,045 | 906.4 | – | 85,551.0 | 5.7분 | 2026-08-16 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 306/305 |
| 42 | [Baddies playlist🫦💋](https://www.youtube.com/watch?v=iwtL-agF0LQ) | Music-cholic | 1,230 | 1,063,699 | 864.8 | – | 7,263.0 | 18.9분 | 2026-05-26 | 기타 | 플레이리스트·모음 | 설명 | 56/56 |
| 43 | [Top Hits Indonesia 2026 ∣ Top Hits Spotify Indonesia 2026 ∣…](https://www.youtube.com/watch?v=ANPUoFuWpEo) | ShadowBrief | 9,720 | 8,267,756 | 850.6 | – | 51,535.7 | 65분 | 2026-05-12 | 기타 | 정보·해설 | 설명 | 998/1,000 |
| 44 | [MOOD : FIRST LOVE { Desi playlist }](https://www.youtube.com/watch?v=zVH3YHdvXHY) | xukiyo | 3,230 | 2,714,024 | 840.3 | ×86.1 | 16,757.8 | 11.8분 | 2026-05-11 | 기타 | 플레이리스트·모음 | 없음 | 71/71 |
| 45 | [DANGRANGTO Playlist Hay Nhất ∣ Xương Rồng, Vùng Vẫy, Wrong …](https://www.youtube.com/watch?v=okmN02_PnaM) | hiệu ứng đám … | 1,660 | 1,342,471 | 808.7 | ×6.1 | 14,122.7 | 24.9분 | 2026-07-17 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 58/58 |
| 46 | [🎧 Le Main Saiyaan Aa Gayi (Lofi) ∣ Mohabbatein ∣ Shah Rukh …](https://www.youtube.com/watch?v=iOdAwvF0kmk) | lofi.slowed_02 | 5,670 | 4,536,259 | 800.0 | ×885.1 | 48,725.6 | 7.5분 | 2026-07-19 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 291/291 |
| 47 | [Tu Chahiye [lyrics] Atif Aslam](https://www.youtube.com/watch?v=AJ0KTHkTGYA) | Chill Beats H… | 1,890 | 1,499,558 | 793.4 | ×389.1 | 24,260.7 | 4.5분 | 2026-08-19 | 기타 | 한 곡 | 설명 | 74/74 |
| 48 | [Tera Sang Yaara - Slowed Reverb ∣∣ Atif Aslam ∣∣ Dopohor Lo…](https://www.youtube.com/watch?v=QcR63bT06iE) | Dopohor Lofi | 3,430 | 2,700,773 | 787.4 | ×227.7 | 67,980.1 | 5분 | 2026-09-10 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 219/219 |
| 49 | [Hanuman Chalisa ∣ Peaceful & Divine ∣ Powerful Bhajan for P…](https://www.youtube.com/watch?v=pmQtkBTtzLw) | Shri Music St… | 1,410 | 1,097,156 | 778.1 | ×1,471.7 | 6,526.9 | 6.4분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 601/601 |
| 50 | [Những Bản Nhạc LoFi Chill Hay Nhất 2026 ∣ TikTok Viral Triệ…](https://www.youtube.com/watch?v=4vl5hS0oXH0) | Kvyzz Music | 1,260 | 959,134 | 761.2 | – | 11,100.3 | 26.1분 | 2026-07-25 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 185/185 |
| 51 | [Barsaat 🌧️ ∣ All Trending Songs 🎧∣ Taare x Samjho Na x Safa…](https://www.youtube.com/watch?v=xGPm2j1dDr4) | LOFI XP VIBES | 2,490 | 1,839,161 | 738.6 | ×240.5 | 47,483.5 | 23분 | 2026-09-11 | 기타 | 음악 | 설명 | 193/199 |
| 52 | [POV: You Own The Dance Floor💃🏻🪩✨ ∣∣Song Playlist+ Timestamp…](https://www.youtube.com/watch?v=HRGB0HnXdOs) | Author_Shreyuu | 6,200 | 4,446,380 | 717.2 | – | 30,013.7 | 8분 | 2026-05-25 | 기타 | 플레이리스트·모음 | 설명 | 617/619 |
| 53 | [[Playlist Tâm Trạng]#1 - Xương Rồng, Vết Thương, Tìm Em, Ng…](https://www.youtube.com/watch?v=DcZ75tBPfa4) | Cà Chuaa | 2,410 | 1,719,077 | 713.3 | ×72.6 | 20,065.2 | 15.5분 | 2026-07-26 | 기타 | 플레이리스트·모음 | 설명 | 344/344 |
| 54 | [Hanuman Chalisa Sleep Version 🕉️ ∣ Sleep In 5 Minutes 😴 ∣ S…](https://www.youtube.com/watch?v=RgmRMA0Bs34) | Ananta Rhythm | 4,510 | 3,168,070 | 702.5 | ×5,927.2 | 19,639.4 | 7.1분 | 2026-05-12 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,523/1,527 |
| 55 | [Yeh Raatein Yeh Mausam - Soft Acoustic Cover ∣ Beautiful Ni…](https://www.youtube.com/watch?v=IrLRtCGI2Oc) | Divine Soul R… | 8,280 | 5,712,633 | 689.9 | ×356.7 | 35,657.6 | 5.1분 | 2026-05-13 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 277/277 |
| 56 | [Pov: certified Baddie playlist 🔥# playlist # baddie](https://www.youtube.com/watch?v=vzNOiBV_W6g) | it's GAURAV P… | 7,850 | 5,381,277 | 685.5 | – | 42,988.8 | 8.3분 | 2026-06-17 | 기타 | 플레이리스트·모음 | 설명 | 696/701 |
| 57 | [Tere Liye [Slowed+Reverb+Lofi] Song ∣ Atif Aslam, Shreya Gh…](https://www.youtube.com/watch?v=zwDQAObOpx4) | DK LOFI | 3,590 | 2,445,278 | 681.1 | ×396.5 | 25,668.3 | 4.5분 | 2026-07-17 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 415/428 |
| 58 | [7 मिनट में बच्चा गहरी नींद सोए🌙 सो जा मेरे चाँद से लाल ∣ Hi…](https://www.youtube.com/watch?v=IxnmH8QjS_A) | deep sleep vi… | 898 | 607,076 | 676.0 | ×10,466.8 | 3,826.9 | 6.8분 | 2026-05-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 152/152 |
| 59 | ['pov: bạn mở lại một tab ký ức năm 2018 ♪♪](https://www.youtube.com/watch?v=8ljpWVIINTs) | chalye | 2,330 | 1,546,937 | 663.9 | ×131.6 | 11,762.5 | 27.4분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 설명 | 331/331 |
| 60 | [Mind Relax Lofi Mashup ∣ Mind Relaxing Songs ∣ Mind Relax L…](https://www.youtube.com/watch?v=JyM_L7ZZ9xw) | SONGS ZONE | 3,000 | 1,991,073 | 663.7 | – | 14,066.3 | 28.7분 | 2026-05-31 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 357/357 |
| 61 | [Steve Lacy - the feeling (Official Video)](https://www.youtube.com/watch?v=Qw20tg1v7Fc) | SteveLacyVEVO | 8,430 | 5,560,223 | 659.6 | – | 40,536.3 | 4.6분 | 2026-06-05 | 기타 | 플레이리스트·모음 | 설명 | 5,393/5,393 |
| 62 | [POV: you discovered that ✨South Indian and Hindi ✨songs hit…](https://www.youtube.com/watch?v=lbT4VY3UKkY) | Arena | 3,490 | 2,300,755 | 659.2 | ×457.5 | 34,931.8 | 14.6분 | 2026-08-15 | 12. 커버·노래 부르기 | 음악 | 설명 | 406/426 |
| 63 | [Darmiyaan](https://www.youtube.com/watch?v=v2TsWj3wxHM) | Rekha Bhardwa… | 8,590 | 5,537,265 | 644.6 | – | 60,169.2 | 4.5분 | 2026-07-20 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/238 |
| 64 | [이게 삶이더라고｜세월 끝에 깨닫는 인생 이야기｜감성 발라드](https://www.youtube.com/watch?v=QalAq2cvw8U) | 웃음콘서트TV | 2,660 | 1,703,113 | 640.3 | ×501.0 | 11,328.9 | 5.4분 | 2026-05-23 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 334/348 |
| 65 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=XLtdtHJExEY) | Clsxzff | 1,860 | 1,189,430 | 639.5 | – | 41,225.8 | 19.6분 | 2026-09-21 | 1. 수면·명상·힐링 | 음악 | 설명 | 173/177 |
| 66 | [Hangova (From "DC")](https://www.youtube.com/watch?v=B6ppp6WBCKg) | Anirudh Ravic… | 31,700 | 20,083,381 | 633.5 | ×968.0 | 189,722.8 | 4.1분 | 2026-07-06 | 기타 | 정보·해설 | 설명 | 0/1,466 |
| 67 | [POV: You are ✨ Self Obsessed women💅 Playlist hindi bollywood](https://www.youtube.com/watch?v=wOy_aMJqDgo) | 𝐌𝐫. | 2,670 | 1,687,027 | 631.9 | ×1,391.9 | 15,626.3 | 14.4분 | 2026-07-04 | 기타 | 플레이리스트·모음 | 설명 | 841/843 |
| 68 | [Om Namah Shivaya 🕉 #hanumanansh #backgroundmusic #trendings…](https://www.youtube.com/watch?v=YnhFtBGO2zI) | Rudree Aarya … | 2,470 | 1,543,222 | 624.8 | – | 35,437.8 | 15.5분 | 2026-09-06 | 기타 | 음악 | 없음 | 385/385 |
| 69 | [MKAstro – Darkness Chill ∣ Club Banger Trap ∣ (Visualizer)](https://www.youtube.com/watch?v=emsqrCS0yiw) | MKAstro Studio | 3,570 | 2,222,773 | 622.6 | ×2,773.3 | 20,025.1 | 5.8분 | 2026-07-01 | 8. 로파이·시티팝·칠 | AI 음악 | 설명 | 154/154 |
| 70 | [[𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 띵곡들만 모아놓은 애니 노동요 OST 플리💿](https://www.youtube.com/watch?v=16zIXIea0_U) | ASMRuru_루루 | 890 | 551,509 | 619.7 | ×878.2 | 4,143.5 | 54.4분 | 2026-06-09 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 91/93 |
| 71 | [Achchi Lagti Ho (Slowed + Reverb) ∣ Lofi Version 🎧](https://www.youtube.com/watch?v=fc8Mab9zGkg) | GTAvexo9 | 24,100 | 14,907,456 | 618.6 | – | 159,084.2 | 6.5분 | 2026-07-18 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 2,047/2,046 |
| 72 | [𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 느좋 인스타 감성](https://www.youtube.com/watch?v=RG-8iv6ORFY) | 알수없는 사용자 | 1,730 | 1,048,304 | 606.0 | ×29.0 | 15,165.6 | 27분 | 2026-08-12 | 기타 | 플레이리스트·모음 | 설명 | 94/100 |
| 73 | [Heartbreak Chillout ∣ Vishal Mishra ∣ Arijit singh ∣ Soulfu…](https://www.youtube.com/watch?v=XlYh9K0UNXI) | Nilay Kumar M… | 2,400 | 1,453,174 | 605.5 | ×18,051.9 | 8,660.3 | 8분 | 2026-05-05 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 137/137 |
| 74 | [Barsaat 🌧️∣ All Trending Songs ∣ Taare x Samjho Na x Safar …](https://www.youtube.com/watch?v=41HX_5G6eqQ) | Voxwaves | 13,600 | 8,113,845 | 596.6 | ×404.7 | 187,514.9 | 22.9분 | 2026-09-07 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,062/1,124 |
| 75 | [Peace of Mind : Sufi Bollywood Nonstop ∣ Rahat Fateh Ali Kh…](https://www.youtube.com/watch?v=RlyVCMHCuqc) | Aures Music S… | 3,720 | 2,208,105 | 593.6 | ×4,295.9 | 28,010.0 | 57.1분 | 2026-08-02 | 기타 | 음악 | 설명 | 124/124 |
| 76 | [Twinkle Twinkle - Best Lullabies for Babies To Sleep ∣ Litt…](https://www.youtube.com/watch?v=PE3jMxJjyB0) | KiddoBeatz | 850 | 503,546 | 592.4 | ×610.4 | 2,991.4 | 10.7분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 77 | [Mann mera (Original Version) ∣ Slowed + Reverb ∣ Gajendra V…](https://www.youtube.com/watch?v=4ObYNh1TOHY) | LOFI ZONE 990K | 16,900 | 9,948,335 | 588.7 | ×1,380.9 | 116,794.4 | 5분 | 2026-07-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,591/1,591 |
| 78 | [DUDE 30 Min Loop 🎧 ∣ Orchestral Suite • Metro Proposal • Pl…](https://www.youtube.com/watch?v=rNkUDAFaFbM) | Zontyx | 1,860 | 1,092,219 | 587.2 | ×6,188.2 | 7,440.0 | 29.7분 | 2026-05-26 | 기타 | 긴 한 곡·반복 | 설명 | 974/983 |
| 79 | [Playlist Song Inggris Gamon Santai...∣∣ The Winner Takes It…](https://www.youtube.com/watch?v=E9Nm4xOU-tk) | musik gen z | 1,990 | 1,164,067 | 585.0 | ×131.8 | 13,686.9 | 31.1분 | 2026-07-27 | 기타 | 플레이리스트·모음 | 설명 | 467/463 |
| 80 | [Old Punjabi Bangers ∣ Punjabi Hits Playlist ∣ Still Cookin](https://www.youtube.com/watch?v=rJgcNE-7emM) | STILL COOKIN | 3,420 | 1,963,916 | 574.2 | – | 18,990.9 | 14.1분 | 2026-07-08 | 기타 | 플레이리스트·모음 | 설명 | 107/109 |
| 81 | [Premada Oorali Kannada LO-FI Song By Nitro plus kannada](https://www.youtube.com/watch?v=LEqTIHGB7_g) | NITRO PLUS KA… | 4,530 | 2,595,138 | 572.9 | ×17,654.0 | 25,129.5 | 11.5분 | 2026-07-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 240/240 |
| 82 | [Phonk/funk playlist bcz I’m bored (Timestaps)](https://www.youtube.com/watch?v=8AXBNw3EGu8) | 1vy_x | 5,110 | 2,893,014 | 566.1 | ×10.3 | 19,215.4 | 9.8분 | 2026-05-22 | 기타 | 플레이리스트·모음 | 설명 | 304/306 |
| 83 | [Autumn Fireplace Jazz ∣ Cozy Crackling Fire Ambience](https://www.youtube.com/watch?v=q87NJ-696WM) | Midnight Fika | 4,060 | 2,276,545 | 560.7 | ×3,454.5 | 61,944.4 | 129.6분 | 2026-09-13 | 2. 자연 소리·백색소음 | 음악 | 설명 | 207/212 |
| 84 | [DESI PUNJABI PLAYLIST THAT GETS YOUR VIBE 😌🎧](https://www.youtube.com/watch?v=JQ922u24pH8) | Your April | 3,210 | 1,798,932 | 560.4 | ×113.8 | 12,296.6 | 11.4분 | 2026-05-27 | 기타 | 플레이리스트·모음 | 설명 | 393/396 |
| 85 | [🍂 가을이 오면 생각나는 노래 ∣ 커피 한 잔과 함께 듣는 가을 감성 플레이리스트 ☕](https://www.youtube.com/watch?v=Fc7JJxJBgJA) | enuscento-에뉴센토 | 710 | 397,788 | 560.3 | ×1,258.8 | 8,475.9 | 114.3분 | 2026-09-03 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 62/69 |
| 86 | [Overthinking? Listen To This Krishna Flute Music & Stop Wor…](https://www.youtube.com/watch?v=Pckh0r0bGAM) | Dhwani | 1,420 | 783,741 | 551.9 | – | 5,945.9 | 8분 | 2026-06-10 | 기타 | 음악 | 설명 | 134/134 |
| 87 | [𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩 slavic](https://www.youtube.com/watch?v=49A1aj-uIcs) | aa | 1,540 | 842,879 | 547.3 | ×316.5 | 8,455.9 | 16.8분 | 2026-07-12 | 기타 | 플레이리스트·모음 | 설명 | 191/199 |
| 88 | [○ Bollywood navratri song playlist ○ #navratri #garbasongs …](https://www.youtube.com/watch?v=g9nj1SDsXng) | july_luna | 4,540 | 2,483,060 | 546.9 | ×94.7 | 83,897.8 | 18.9분 | 2026-09-20 | 기타 | 플레이리스트·모음 | 없음 | 102/118 |
| 89 | [Sanson Ki Mala Pe (Slowed & Emotional Version) ∣ Hindi Love…](https://www.youtube.com/watch?v=7y_L2sW-3J4) | Karela Records | 4,360 | 2,378,660 | 545.6 | ×2,040.9 | 17,455.5 | 7.3분 | 2026-06-06 | 기타 | 음악 | 설명 | 92/92 |
| 90 | [Relaxing Jazz Café in Paris ∣ Rainy Evening Jazz Ambience w…](https://www.youtube.com/watch?v=eR37WB9IE9E) | European Jazz… | 1,240 | 675,437 | 544.7 | ×1,160.5 | 5,033.1 | 14.4분 | 2026-06-08 | 2. 자연 소리·백색소음 | 음악 | 설명 | 24/26 |
| 91 | [You’ll Sleep Like a Child in Hanuman’s Protection ∣ Soft Ha…](https://www.youtube.com/watch?v=oSeh-sXFCTM) | Sanatan Jug | 5,540 | 2,975,270 | 537.0 | ×7,346.3 | 17,833.8 | 111.6분 | 2026-05-06 | 1. 수면·명상·힐링 | 한 곡 | 설명 | 399/398 |
| 92 | [Baddie playlist 💋✨Aura+99999∣ SanviEditz #songplaylist](https://www.youtube.com/watch?v=p8u1URNm4ao) | ♡𝑺𝒂𝒏𝒗𝒊𝑬𝒅𝒊𝒕𝒛♡ | 4,820 | 2,583,301 | 536.0 | – | 58,747.6 | 8.1분 | 2026-09-06 | 기타 | 플레이리스트·모음 | 없음 | 2,195/2,277 |
| 93 | [✨️𝐬𝐨𝐧𝐠𝐬 𝐭𝐡𝐚𝐭 𝐦𝐚𝐤𝐞 𝐥𝐢𝐟𝐞 𝐟𝐞𝐞𝐥 𝐥𝐢𝐤𝐞 𝐚 𝐥𝐨𝐯𝐞 𝐬𝐭𝐨𝐫𝐲 ∣ aesthetic h…](https://www.youtube.com/watch?v=GMF0FN2nrBw) | Echoess of un… | 6,140 | 3,273,950 | 533.2 | ×19.0 | 23,425.6 | 18.6분 | 2026-06-02 | 기타 | 플레이리스트·모음 | 설명 | 409/409 |
| 94 | [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 그리고 난 다시 사랑에 빠질수 밖에 없었어](https://www.youtube.com/watch?v=cIlJK2Pfhm8) | 느좋을 추구합니다 | 1,030 | 543,141 | 527.3 | – | 9,215.3 | 18.1분 | 2026-08-22 | 기타 | 플레이리스트·모음 | 없음 | 177/177 |
| 95 | [Me Sunti Rahu 💭🎶 ∣ Heart Touching Lofi Song (Slowed + Rever…](https://www.youtube.com/watch?v=TKMu6Wg396c) | 𝕃𝕠𝕤𝕥_𝕗𝕖𝕖𝕝𝕚𝕟𝕘𝕤… | 4,620 | 2,422,094 | 524.3 | ×652.1 | 17,324.0 | 5.7분 | 2026-06-02 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 389/389 |
| 96 | [If you want to dance...🩰✨watch this playlist💃❣️ #bollywood …](https://www.youtube.com/watch?v=x0br2Hc-4G8) | LyricVibes~ | 6,060 | 3,155,353 | 520.7 | – | 21,476.5 | 24.4분 | 2026-05-26 | 기타 | 플레이리스트·모음 | 설명 | 380/380 |
| 97 | [💋 A Chatpati Playlist Only For Chatpata People 😋✨ ∣ Ultimat…](https://www.youtube.com/watch?v=3FhXwFGVaDE) | JellyBloxify | 33,100 | 17,206,844 | 519.8 | ×9,683.1 | 126,423.3 | 7.5분 | 2026-06-06 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 2,208/2,219 |
| 98 | [Ankhiyon Ke Jharokhon Se ∣ Soft Classic Instrumental 🎶 ∣ Ol…](https://www.youtube.com/watch?v=KCgBk52MuY8) | Saaz-e-Dil | 1,930 | 1,002,296 | 519.3 | ×363.8 | 7,845.3 | 4.5분 | 2026-06-14 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 127/127 |
| 99 | [Noah Kahan - Orbiter (Official Lyric Video)](https://www.youtube.com/watch?v=OFcKm-5jSQE) | NoahKahanVEVO | 29,700 | 15,220,212 | 512.5 | ×3.3 | 85,347.2 | 4.8분 | 2026-04-25 | 기타 | 한 곡 | 설명 | 1,405/1,405 |
| 100 | [Arijit Singh - Tujhko (from Cocktail 2) Rashmika Mandanna, …](https://www.youtube.com/watch?v=WWIfHemqSEA) | iPop Superhits | 47,300 | 24,066,819 | 508.8 | – | 174,267.7 | 5.6분 | 2026-06-04 | 기타 | 한 곡 | 설명 | 1,133/1,136 |
| 101 | [Parindey (Slowed + Reverb) ∣ Haryanvi Lofi Song 🎧 Chill Vib…](https://www.youtube.com/watch?v=v8CKkI20B2s) | AS LO-FI Musi… | 3,740 | 1,897,352 | 507.3 | ×737.1 | 10,887.4 | 4.1분 | 2026-04-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 150/150 |
| 102 | [Ishq x Pal Pal Endless Mashup (Slowed + Reverb) - Afusic x …](https://www.youtube.com/watch?v=h231qlqI-dg) | Lost In Lyrics | 1,090 | 546,184 | 501.1 | ×142.1 | 5,363.5 | 27.6분 | 2026-07-10 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 109/109 |
| 103 | [Devik - Muje tumse x tu tu hai wahi DJ remix (BGM) music 🎶 …](https://www.youtube.com/watch?v=FPuJuLyZmJI) | Newworldbeats… | 729 | 364,754 | 500.4 | – | 7,418.9 | 9.7분 | 2026-09-01 | 기타 | 음악 | 설명 | 137/137 |
| 104 | [I'm Tired Of Loving You - Golden Lace Ballads ∣ Classic Cou…](https://www.youtube.com/watch?v=URrqbWhzzMU) | Golden Lace B… | 3,140 | 1,568,504 | 499.5 | ×1,479.7 | 10,535.1 | 5.8분 | 2026-05-24 | 기타 | 한 곡 | 설명 | 361/366 |
| 105 | [THE WEEKND ∣ Late Night Drive Playlist](https://www.youtube.com/watch?v=DgBM12cGM-Q) | Jostynsc | 10,300 | 5,136,117 | 498.6 | ×19.8 | 42,691.4 | 40.8분 | 2026-06-22 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 304/306 |
| 106 | [धनियां बनबू कनियाँ - Lofi Song ∣∣ Khesari Lal Yadav ∣∣ Dilw…](https://www.youtube.com/watch?v=s-1MerBYomA) | ꧁༒乙x°᭄Ᏼᴀʙᴜ࿐ | 3,840 | 1,877,687 | 489.0 | ×327.3 | 33,947.3 | 5.1분 | 2026-08-26 | 8. 로파이·시티팝·칠 | 음악 | 없음 | 267/267 |
| 107 | [✨Best Bollywood LoFi Mashup 2026 🌙✨ lofi song](https://www.youtube.com/watch?v=ohHqAaHYlLI) | Soul Beats | 4,790 | 2,302,644 | 480.7 | ×1,053.8 | 23,327.7 | 25.8분 | 2026-07-13 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 122/122 |
| 108 | [[𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 저 정말 바라는 거 없어요](https://www.youtube.com/watch?v=ZUW47tZkwkg) | 음악저장소 | 1,820 | 867,425 | 476.6 | ×55.5 | 29,116.7 | 27.3분 | 2026-09-20 | 기타 | 플레이리스트·모음 | 없음 | 88/88 |
| 109 | [[ 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ] 적당히 신나는 그루브 힙합 플레이리스트 ∣ Chill R&B • Cafe Music](https://www.youtube.com/watch?v=p3tvSF3BgYM) | SSoundW | 4,020 | 1,914,311 | 476.2 | ×464.5 | 32,011.3 | 89.9분 | 2026-08-21 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 253/253 |
| 110 | [GTA 6 Raul Batista Mission Theme Music - Clean Audio - Exte…](https://www.youtube.com/watch?v=Lu2v0EWc0-0) | GAMING Benchm… | 1,350 | 642,107 | 475.6 | ×4,901.6 | 12,167.9 | 5.3분 | 2026-08-28 | 기타 | 음악 | 설명 | 864/871 |
| 111 | [Mind relaxing lofi song Arijit Singh ∣ Soft songs ∣ Arijit …](https://www.youtube.com/watch?v=43y5rT7YjQY) | Y Music 2 | 36,300 | 17,149,587 | 472.4 | ×125,179.5 | 121,556.2 | 27.9분 | 2026-06-01 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,372/1,384 |
| 112 | [Idea 22 - Depressed in 448Hz (Cello cry & Piano & slow) @Gi…](https://www.youtube.com/watch?v=zMMuayoF_o4) | WORRIES | 403 | 187,189 | 464.5 | ×93.9 | 2,245.4 | 12.9분 | 2026-07-28 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 116/116 |
| 113 | [🎶Spotify Hits Music 2026 ∣∣ Top Music Playlist -- Best 100 …](https://www.youtube.com/watch?v=0gvy7v6GTMo) | Soft Feelings | 5,900 | 2,739,041 | 464.2 | ×176.7 | 40,346.1 | 138.6분 | 2026-08-13 | 기타 | 플레이리스트·모음 | 설명 | 188/191 |
| 114 | [🎀Students fav playlist👀 ∣next comment∣](https://www.youtube.com/watch?v=yx9rhLzbY0A) | @vibe_withe_me | 5,400 | 2,506,093 | 464.1 | ×392.8 | 34,862.0 | 7분 | 2026-08-09 | 기타 | 플레이리스트·모음 | 없음 | 1,169/1,198 |
| 115 | [One playlist. A thousand imaginary love stories. ❤️](https://www.youtube.com/watch?v=aIYTT2ihwvM) | soul wali vib… | 2,410 | 1,088,459 | 451.6 | ×99.0 | 19,223.9 | 22.1분 | 2026-08-24 | 기타 | 플레이리스트·모음 | 없음 | 354/355 |
| 116 | [𓍢ִ໋🌾 chatpate punjabi bangers](https://www.youtube.com/watch?v=neQ8CUHH7WQ) | b࣪ ִֶָ☾. | 6,870 | 3,069,703 | 446.8 | – | 22,567.1 | 12.2분 | 2026-06-06 | 기타 | 플레이리스트·모음 | 설명 | 277/281 |
| 117 | [Michael Jackson Greatest Hits Mix ∣ Celebrating MICHAEL (20…](https://www.youtube.com/watch?v=F2-83E_iNb4) | IONEMusic | 10,700 | 4,762,804 | 445.1 | ×4,143.4 | 46,878.2 | 94.5분 | 2026-07-10 | 기타 | 음악 | 설명 | 1,177/1,185 |
| 118 | [कर्पूरगौरं करुणावतारं ∣ Shiva Lingam Divine Prayer ∣ Karpur…](https://www.youtube.com/watch?v=5I7pQfjbUHo) | Darshan Dhara | 4,020 | 1,779,175 | 442.6 | ×1,369.6 | 10,946.2 | 8.4분 | 2026-05-10 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 139/139 |
| 119 | [모르는 노래 없는!! 2026 랜덤플레이댄스🍋 ∣ 랜플댄 ∣ 랜플💫 ∣ 모르는 노래 없는 랜플댄🩷 ∣ 케이…](https://www.youtube.com/watch?v=tAJM1fttdG0) | 바나나한 바냐 | 577 | 255,371 | 442.6 | – | 3,737.5 | 5.1분 | 2026-08-13 | 10. 팝송·K팝·J팝 | 음악 | 없음 | 36/36 |
| 120 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 nên nghe gì khi gió Thu tràn về? 🍂📻 Playlist Nhạc …](https://www.youtube.com/watch?v=Pg39V_-aNPY) | chill out | 4,530 | 1,998,400 | 441.1 | ×41.8 | 66,770.8 | 83.5분 | 2026-09-20 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 236/238 |
| 121 | [Pov :- Bhojpuri playlist 🔥 ∣∣ chill guys and enjoy 😎∣∣ Ansh…](https://www.youtube.com/watch?v=4mnrtxd_GhE) | Anshika | 19,600 | 8,591,962 | 438.4 | ×61.3 | 111,999.0 | 11.6분 | 2026-08-04 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,684/1,706 |
| 122 | [Top Bhojpuri Hits Mix 2026 ∣ Nonstop Bhojpuri Mashup 🎧🔥](https://www.youtube.com/watch?v=7v8NIUwR1No) | Anivix | 6,070 | 2,654,598 | 437.3 | ×1,099.4 | 24,434.3 | 6분 | 2026-07-03 | 기타 | 음악 | 설명 | 483/486 |
| 123 | [🌊 여름에 듣기 좋은 노래☀️ 하루 종일 듣기 좋은 여름 플레이리스트 🌴 바다로 떠나고 싶어지는 여름 노래…](https://www.youtube.com/watch?v=L-pbTsp8AH8) | 마음선곡 | 844 | 368,453 | 436.6 | ×404.4 | 2,594.7 | 119분 | 2026-05-31 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 67/67 |
| 124 | [katseye (clean) playlist ⊹ ࣪ ˖](https://www.youtube.com/watch?v=_VEtnBXtUNs) | 𝟑𝟎𝟑.𝐧𝐞𝐰.𝐞𝐫𝐚 | 7,780 | 3,366,462 | 432.7 | – | 41,973.9 | 25.3분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 설명 | 2,599/2,602 |
| 125 | [One Playlist. Endless Feelings. ∣ Soft Love Songs for Late …](https://www.youtube.com/watch?v=Auvd4NPXHnI) | Unrequited Lo… | 5,760 | 2,480,912 | 430.7 | – | 23,661.3 | 23.2분 | 2026-07-07 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 436/437 |
| 126 | ["𝐖𝐞 𝐚𝐫𝐞 𝐣𝐮𝐬𝐭 𝐟𝐫𝐢𝐞𝐧𝐝𝐬... 𝐑𝐢𝐠𝐡𝐭.?"/ 𝐀 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐟𝐨𝐫 𝐬𝐨𝐦𝐞𝐨𝐧𝐞 𝐲𝐨…](https://www.youtube.com/watch?v=A_yQZns_YGk) | 𝗩𝗮𝗺𝗽𝗶𝗿𝗲 𓂃⋆.˚ | 2,410 | 1,034,142 | 429.1 | ×41.2 | 10,053.6 | 20.4분 | 2026-07-09 | 기타 | 플레이리스트·모음 | 설명 | 610/610 |
| 127 | [Stay With Me Now..](https://www.youtube.com/watch?v=mT2U96LfO3g) | AERIN - Proje… | 571 | 242,467 | 424.6 | ×1,405.6 | 1,528.0 | 4.6분 | 2026-05-14 | 기타 | 음악 | 설명 | 31/31 |
| 128 | [𝑮𝒐𝒍𝒅𝒆𝒏 𝑩𝒓𝒐𝒘𝒏 - 𝑻𝒉𝒆 𝑺𝒕𝒓𝒂𝒏𝒈𝒍𝒆𝒓𝒔 ∣ ⚔︎ 𝑩𝒆𝒔𝒕 𝒑𝒂𝒓𝒕 𝒍𝒐𝒐𝒑𝒆𝒅 ⚔︎](https://www.youtube.com/watch?v=9MLxTIPaoTQ) | Medieval Anem… | 2,410 | 1,019,602 | 423.1 | ×2,258.3 | 13,880.0 | 11.8분 | 2026-08-07 | 기타 | 정보·해설 | 설명 | 417/417 |
| 129 | [Dance playlist for chatpati girls 🥂💅🏻🍷#dance #viral#trendin…](https://www.youtube.com/watch?v=wh1wOQrBIrk) | soft girl 🦋💫 | 4,010 | 1,681,357 | 419.3 | ×83.2 | 12,772.2 | 8.5분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 없음 | 110/110 |
| 130 | [Playlist cuz you're in love 💌#playlist #love #2026](https://www.youtube.com/watch?v=gbf3ZYx6EbU) | it's GAURAV P… | 7,850 | 3,286,856 | 418.7 | – | 20,173.4 | 10.6분 | 2026-05-10 | 기타 | 플레이리스트·모음 | 설명 | 531/530 |
| 131 | [ALL TRENDING HINDI SONGS 2026...PLAYLIST #asthetic #trend #…](https://www.youtube.com/watch?v=xI0IEWIxUBQ) | Rb Lofi | 23,700 | 9,921,293 | 418.6 | ×1,098.2 | 171,100.3 | 7.9분 | 2026-08-23 | 기타 | 플레이리스트·모음 | 없음 | 1,565/1,634 |
| 132 | [[Playlist] Music is my drug](https://www.youtube.com/watch?v=msoR3EhPNAA) | Hugs | 6,470 | 2,667,761 | 412.3 | – | 57,178.5 | 20.9분 | 2026-09-03 | 기타 | 플레이리스트·모음 | 설명 | 538/540 |
| 133 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Chi…](https://www.youtube.com/watch?v=ki362-gbdjs) | Qais Music St… | 2,170 | 889,537 | 409.9 | ×4,006.9 | 44,722.0 | 7.3분 | 2026-09-30 | 3. 공부·집중·작업 | 음악 | 설명 | 10/10 |
| 134 | [Throwback R&B Classics 📺 Chris Brown, Rihanna, Akon, Usher,…](https://www.youtube.com/watch?v=gCUbxsTWZ18) | R&B Afterglow | 14,400 | 5,874,965 | 408.0 | ×4,534.9 | 61,896.4 | 193.5분 | 2026-07-17 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 698/732 |
| 135 | [𝙅 𝙋𝙤𝙥 𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩 저기, 나 지금 사랑에 빠지고 있어](https://www.youtube.com/watch?v=-_t34PClPSE) | 이로하 | 1,850 | 749,853 | 405.3 | – | 4,878.5 | 20.9분 | 2026-05-19 | 기타 | 플레이리스트·모음 | 설명 | 165/168 |
| 136 | ["some aesthetic desi song's you'll absolutely love"🌊✨😭//par…](https://www.youtube.com/watch?v=6D1sq3Y-hB0) | Anushri | 7,070 | 2,863,028 | 404.9 | ×15.3 | 26,643.3 | 12.5분 | 2026-07-04 | 기타 | 음악 | 설명 | 503/506 |
| 137 | [katseye playlist✨💋](https://www.youtube.com/watch?v=H40nuw4mebU) | maiia | 20,400 | 8,187,721 | 401.4 | – | 162,731.3 | 21.3분 | 2026-08-31 | 기타 | 플레이리스트·모음 | 없음 | 4,330/4,509 |
| 138 | [/KATSEYE PLAYLIST💫/ All Songs In One Video / ICONIC BY MIST…](https://www.youtube.com/watch?v=wQHy50dFnfY) | 𝓔𝓵𝓵𝓲𝔁𝔁𝓺 🤍🎀 | 2,610 | 1,046,744 | 401.1 | – | 9,207.5 | 43분 | 2026-06-28 | 기타 | 플레이리스트·모음 | 설명 | 950/946 |
| 139 | [Haryanvi playlist that walk up your inner dancer 🔥💋#lifewit…](https://www.youtube.com/watch?v=tYuLhTnHgOQ) | Venus Yadav | 11,800 | 4,725,514 | 400.5 | – | 59,353.9 | 11분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 없음 | 570/592 |
| 140 | [Heartbreaking 💔 Lofi Mashup 🎧Slowed + Reverb Songs ∣ Relax,…](https://www.youtube.com/watch?v=gCuJrBYRJpM) | Fiaz Baloch O… | 6,880 | 2,745,994 | 399.1 | ×4,244.2 | 62,081.5 | 8분 | 2026-09-06 | 3. 공부·집중·작업 | 음악 | 설명 | 154/154 |
| 141 | [Attract Peace & Positive Energy ∣ Raag Malhar Morning Medit…](https://www.youtube.com/watch?v=c45OwnC599Y) | Tatva Meditat… | 208 | 82,829 | 398.2 | ×696.0 | 590.3 | 15분 | 2026-06-02 | 1. 수면·명상·힐링 | 음악 | 설명 | 9/9 |
| 142 | [Emraan hashmi playlist #emraanhashmi](https://www.youtube.com/watch?v=zZzA1Hp30uE) | july_luna | 4,540 | 1,783,677 | 392.9 | ×68.0 | 29,897.6 | 7.2분 | 2026-08-21 | 기타 | 플레이리스트·모음 | 없음 | 22/25 |
| 143 | [CHILL NIGHT MOOD🌙 R&B Mix Playlist ∣ Late Night Vibes, Rela…](https://www.youtube.com/watch?v=zA04SiNiLYk) | Late Night Rn… | 2,610 | 1,023,153 | 392.0 | – | 6,253.1 | 158.2분 | 2026-05-09 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 54/54 |
| 144 | [[playlist] 잔잔한 안건호 보컬 모음 플레이리스트 ∣ 커버곡 ∣ 코르티스](https://www.youtube.com/watch?v=WHHQaKlBtZk) | W | 22 | 38,801 | 388.0 | – | 244.3 | 13.3분 | 2026-05-14 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 12/12 |
| 145 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Stu…](https://www.youtube.com/watch?v=MvV7_DKFZQA) | peacefulvibes… | 12,300 | 4,737,610 | 385.2 | ×13,307.9 | 84,508.5 | 16.3분 | 2026-08-25 | 3. 공부·집중·작업 | 음악 | 설명 | 284/284 |
| 146 | [Barsaat ∣ All Trending Hindi Songs 2026 ∣ Safar × Bairan × …](https://www.youtube.com/watch?v=-hXkiB-eLfs) | SukumusicHindi | 3,390 | 1,296,516 | 382.4 | ×698.9 | 32,606.7 | 22.9분 | 2026-09-10 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 161/161 |
| 147 | [Dopamine Reset ∣ Indian Classical Flute Music for Relaxatio…](https://www.youtube.com/watch?v=gSOocWITTT4) | Desert Harmon… | 2,190 | 834,905 | 381.2 | ×1,211.8 | 8,193.6 | 8.4분 | 2026-07-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 132/133 |
| 148 | [너 때문에 하루를 살아 #이별 #이별노래 #이별감성 #새벽감성 #OST #감성발라드 #kpop #kpopb…](https://www.youtube.com/watch?v=hhbJfI8dJ9o) | 글쓰는여자🎀 | 620 | 233,964 | 377.4 | ×543.5 | 1,966.8 | 5.3분 | 2026-06-23 | 10. 팝송·K팝·J팝 | 한 곡 | 없음 | 105/105 |
| 149 | [왜 이제 와｜음색 미쳤다는 반응 나온 새벽 감성 발라드 ｜ なぜ今になって｜音色がすごいという反応が出た、深夜の…](https://www.youtube.com/watch?v=TWunCWy98FU) | Faded Love No… | 1,130 | 421,530 | 373.0 | ×377.7 | 2,686.3 | 4.3분 | 2026-05-16 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 84/85 |
| 150 | [[Playlist] When music is all you need](https://www.youtube.com/watch?v=XXKXpf7xFC4) | encore. | 7,210 | 2,673,428 | 370.8 | ×221.7 | 89,177.7 | 20.9분 | 2026-09-20 | 기타 | 플레이리스트·모음 | 설명 | 518/547 |
| 151 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 (가사X) 후회 없는 미래를 위해 ✍️ 새벽공부 집중 로파이 BGM🎧 유리숲 플리 🌙](https://www.youtube.com/watch?v=hZLVePYp9Z0) | Yurisoop | 1,240 | 457,609 | 369.0 | ×262.4 | 6,441.4 | 132분 | 2026-08-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 42/45 |
| 152 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 : 딱딱 나 틀딱 ∣ 보카로 근본 플리 1탄](https://www.youtube.com/watch?v=W_G2W0nTGYY) | 윤슬자 | 1,060 | 390,869 | 368.7 | ×14.2 | 2,466.1 | 245.8분 | 2026-05-14 | 기타 | 플레이리스트·모음 | 설명 | 333/333 |
| 153 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 🍁 설레는 바람이 부는 가을이 왔나봐 ∣ 틀어두기 좋은 감성 팝송 모음](https://www.youtube.com/watch?v=jmU_fq-iTSE) | Melly Moood | 6,230 | 2,270,310 | 364.4 | ×330.6 | 62,342.9 | 188.2분 | 2026-09-13 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 283/292 |
| 154 | [Teri Meri Prem Kahani 💖 Slowed + Reverb ∣ Romantic Lofi Son…](https://www.youtube.com/watch?v=Njmb7oBzkpM) | 🌙 MoonVerse | 7,090 | 2,578,704 | 363.7 | – | 24,269.7 | 6.3분 | 2026-07-06 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 755/755 |
| 155 | [• playlist 순애](https://www.youtube.com/watch?v=Av29750WaJs) | ros!e | 446 | 161,970 | 363.2 | ×12.8 | 3,171.0 | 18.4분 | 2026-08-30 | 기타 | 플레이리스트·모음 | 없음 | 56/56 |
| 156 | [Desi baddie playlist 💅💌 @desi_diva12 #playlist #baddie #des…](https://www.youtube.com/watch?v=Y3q1y6M79EU) | Desi_.Diva12 | 6,090 | 2,207,171 | 362.4 | ×37.9 | 19,415.0 | 7.3분 | 2026-06-28 | 기타 | 플레이리스트·모음 | 설명 | 207/207 |
| 157 | [Viral Songs Playlist 2026 ∣ Barsaat, Sheesha, Parvati, Roots](https://www.youtube.com/watch?v=nmc4ScFV3j4) | Vijay Garje | 3,540 | 1,268,888 | 358.4 | ×11,229.1 | 80,248.0 | 31.3분 | 2026-10-04 | 기타 | 플레이리스트·모음 | 설명 | 320/344 |
| 158 | [Perfect South Indian Playlist 🪷🦢 (+timestamps)](https://www.youtube.com/watch?v=ROBjw6FcYxs) | Being Diva 💅🏻 | 5,720 | 2,020,596 | 353.2 | ×16.7 | 60,078.4 | 7.7분 | 2026-09-16 | 기타 | 플레이리스트·모음 | 설명 | 266/280 |
| 159 | [2026 최신곡 랜덤플레이댄스∣ K-pop Random Play Dance 2026 #랜덤플레이댄스 #랜플…](https://www.youtube.com/watch?v=bliX1fxHkKk) | 샤파 | 909 | 318,869 | 350.8 | ×3.0 | 18,769.5 | 6.1분 | 2026-10-03 | 10. 팝송·K팝·J팝 | 한 곡 | 설명 | 46/47 |
| 160 | [Sonata in the Dark 🎹 Beethoven-Inspired Melancholic Classic…](https://www.youtube.com/watch?v=sakrZHnzs6k) | Elysian Class… | 189 | 66,082 | 349.6 | ×112.4 | 961.1 | 16분 | 2026-08-12 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 17/17 |
| 161 | [90’S Old Hindi Songs🥰 90s Love Song💘 Udit Narayan, Alka Yag…](https://www.youtube.com/watch?v=qDOFK8SfKmA) | 90s Lovers Po… | 17,600 | 6,146,633 | 349.2 | ×1,195.6 | 95,561.1 | 27.4분 | 2026-08-17 | 기타 | 음악 | 설명 | 217/217 |
| 162 | [Golden Brown x Love Story - Relaxing Celtic Fantasy Medieva…](https://www.youtube.com/watch?v=hzPdVFw768A) | The Knight Sa… | 3,090 | 1,076,941 | 348.5 | – | 8,270.5 | 16.9분 | 2026-06-12 | 2. 자연 소리·백색소음 | 음악 | 설명 | 536/540 |
| 163 | [CORTIS PLAYLIST (코르티스 플레이리스트) 머니머니머니부터 나니까지](https://www.youtube.com/watch?v=2byCD3x_vPY) | 우울 대신 우웅! | 2,260 | 783,467 | 346.7 | – | 13,928.7 | 41.5분 | 2026-08-25 | 기타 | 플레이리스트·모음 | 없음 | 187/187 |
| 164 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Study / Focus …](https://www.youtube.com/watch?v=KU7PfC9i9cE) | Focus Music 2… | 4,270 | 1,477,055 | 345.9 | ×3,090.1 | 70,665.7 | 13.8분 | 2026-09-29 | 3. 공부·집중·작업 | 음악 | 설명 | 92/92 |
| 165 | [PLAYLIST I it's like supernatural I 느좋 팝송 기모띠 야르 찹찹 플리](https://www.youtube.com/watch?v=1huhmKD8P7U) | 자세히알아보기 | 551 | 190,399 | 345.6 | ×405.1 | 2,446.8 | 19.6분 | 2026-08-03 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 101/101 |
| 166 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 느좋](https://www.youtube.com/watch?v=3lY_H67eQl4) | 고김 | 539 | 185,658 | 344.4 | – | 1,616.0 | 15.3분 | 2026-06-27 | 기타 | 플레이리스트·모음 | 없음 | 52/52 |
| 167 | [Ama hem hem](https://www.youtube.com/watch?v=rPmZucO77sg) | Thatohatsi - … | 36,400 | 12,533,226 | 344.3 | ×69.4 | 121,783.7 | 7.5분 | 2026-07-09 | 기타 | 정보·해설 | 설명 | 0/2,577 |
| 168 | [[PLAYLIST] Biển Đảo Và Em, Fallin Flower, Người Yêu Bỏ Lỡ,……](https://www.youtube.com/watch?v=dMaqYNGvzmA) | wenjin. | 2,560 | 877,743 | 342.9 | ×18.6 | 8,664.9 | 26.2분 | 2026-07-11 | 기타 | 플레이리스트·모음 | 설명 | 442/442 |
| 169 | [하우스룰즈가 최고야](https://www.youtube.com/watch?v=V0mzAQ7z3D0) | Yeon | 948 | 322,530 | 340.2 | ×218.2 | 6,735.1 | 18.1분 | 2026-09-02 | 기타 | 플레이리스트·모음 | 설명 | 232/249 |
| 170 | [한국 드라마 OST 황금기 모음💗마음을 울리는 인기 노래 모음 하루 종일 들어도 좋은 발라드🎧20-26년 …](https://www.youtube.com/watch?v=Vxw1QiXjDvs) | K-Drama Memor… | 2,670 | 900,235 | 337.2 | ×663.6 | 18,201.9 | 74.3분 | 2026-08-31 | 13. OST·사운드트랙 | 플레이리스트·모음 | 설명 | 140/140 |
| 171 | [【BGM】置いていかないで｜1分後に涙が溢れてくる曲](https://www.youtube.com/watch?v=e9ArzLcNNbw) | 1分後に〇〇する曲🎧 | 1,200 | 404,530 | 337.1 | ×88.7 | 3,112.2 | 4.3분 | 2026-06-12 | 기타 | 음악 | 설명 | 61/63 |
| 172 | [새벽 2시, 잠이 깼다면 다시 자세요 ∣ 6분 후 다시 잠드는 피아노 명상음악 for Deep Sleep …](https://www.youtube.com/watch?v=ViCEPJCOgy4) | 단잠TV | 2,510 | 845,278 | 336.8 | ×1,179.7 | 5,919.2 | 181.7분 | 2026-05-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 216/219 |
| 173 | [Lahore Diya ✨ Slowed Reverb ∣ Late Night Vibes ∣ Punjabi Lo…](https://www.youtube.com/watch?v=-rNlgODrgjo) | Arun music 100 | 9,450 | 3,168,929 | 335.3 | ×87.6 | 24,348.7 | 4.2분 | 2026-06-12 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 252/252 |
| 174 | [𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 틱톡 그 느좋 노래 모음](https://www.youtube.com/watch?v=NG6SQIGv3-Y) | 뭐야 | 1,720 | 573,591 | 333.5 | ×51.0 | 5,805.8 | 8.9분 | 2026-07-13 | 기타 | 플레이리스트·모음 | 설명 | 112/112 |
| 175 | [💿 마음이 따뜻해지는 감성 발라드 🌸 광고없이 듣는 명곡 🌸 SG워너비, 김범수, 허각](https://www.youtube.com/watch?v=d68bRNKlMQA) | 서울 소울 발라드-Seo… | 899 | 298,608 | 332.2 | ×438.8 | 5,071.9 | 156.2분 | 2026-08-22 | 9. 가요·발라드·트로트 | 음악 | 설명 | 48/48 |
| 176 | [Prasanna Vadanam – Enigma Style ∣ Lord Vishnu Peaceful Medi…](https://www.youtube.com/watch?v=QeF_NFcmxt4) | devinebeatsst… | 1,360 | 449,940 | 330.8 | ×2,902.8 | 4,775.0 | 5.1분 | 2026-07-18 | 1. 수면·명상·힐링 | 음악 | 설명 | 116/116 |
| 177 | [The Complete "Love Is in the Air" Theme by Rock Burwell ∣ O…](https://www.youtube.com/watch?v=ipCco3jw504) | NR ENTERTAINM… | 2,810 | 927,816 | 330.2 | ×3,092.7 | 6,252.1 | 4.5분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 614/614 |
| 178 | [DARKHAAST ❤️‍🩹 slowed x reverb Arijit Singh (Lyrics) Ft. Su…](https://www.youtube.com/watch?v=7u9GjyI2yxg) | GK lofi song | 9,720 | 3,200,455 | 329.3 | ×545.7 | 28,073.1 | 6.9분 | 2026-06-28 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 264/264 |
| 179 | [나그네](https://www.youtube.com/watch?v=FFwUpZZGqnc) | 여산일거 | 4,270 | 1,401,005 | 328.1 | ×211.8 | 8,419.5 | 8.9분 | 2026-05-06 | 기타 | 한 곡 | 설명 | 372/375 |
| 180 | [Rabba Tu Na Naraz Hovi ❤️ ∣ Soulful Heart Touching Punjabi …](https://www.youtube.com/watch?v=Zh-3CGV7BwQ) | Sufi Usman | 4,740 | 1,555,085 | 328.1 | ×956.4 | 19,182.4 | 5.9분 | 2026-07-31 | 기타 | 음악 | 설명 | 214/214 |
| 181 | [듣기만 해도 설레는 그시절 1990~2026년 사랑하고 슬퍼했던 노래- 휘성,프리스타일,조장혁,임재범,이승…](https://www.youtube.com/watch?v=dCB0KQI7qfU) | 감정 작사가 | 600 | 196,550 | 327.6 | ×1,803.2 | 1,261.4 | 118.5분 | 2026-05-17 | 기타 | 음악 | 설명 | 46/46 |
| 182 | [JANANAYAGAN - Forest BGM ∣ The Ultimate Cinematic Experienc…](https://www.youtube.com/watch?v=uVuVb5CdEC8) | Massplix | 1,330 | 432,969 | 325.5 | – | 2,582.9 | 4.5분 | 2026-05-05 | 기타 | 음악 | 설명 | 167/167 |
| 183 | [Banjaara 🥀 Slowed + Reverb ∣ Best Hindi Lofi Song 🎧 ∣ Anime…](https://www.youtube.com/watch?v=uxMeJy4JMS8) | Broken Sky01 | 6,750 | 2,196,267 | 325.4 | ×731.6 | 26,088.0 | 6.3분 | 2026-07-28 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 857/856 |
| 184 | [𝐵𝑒𝓈𝓉 𝒮𝑜𝓊𝓉𝒽 𝐼𝓃𝒹𝒾𝒶𝓃 𝒮𝑜𝓃𝑔𝓈 𝒫𝓁𝒶𝓎𝓁𝒾𝓈𝓉 🎶 𝒯𝒶𝓂𝒾𝓁 • 𝒯𝑒𝓁𝓊𝑔𝓊 • 𝑀𝒶𝓁𝒶𝓎𝒶𝓁…](https://www.youtube.com/watch?v=GAXYvJx8rD4) | Nyxelune | 5,650 | 1,835,907 | 324.9 | – | 19,998.5 | 10.3분 | 2026-07-20 | 기타 | 정보·해설 | 설명 | 1,056/1,069 |
| 185 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=29EWidvY0b8) | AR BROTHER | 7,190 | 2,331,578 | 324.3 | – | 52,941.0 | 18.6분 | 2026-09-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 87/89 |
| 186 | [LEO ROJAS - Top 16 Andean Pan Flute Melodies ★ Full Album -…](https://www.youtube.com/watch?v=wR5yxMCTZA0) | Andean Flute … | 4,840 | 1,540,166 | 318.2 | ×522.1 | 30,277.8 | 98.3분 | 2026-08-30 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 233/233 |
| 187 | ["Comfort song's - All in one playlist"😭✨🌷//part-4//edit by …](https://www.youtube.com/watch?v=617yn663oeA) | Anushri | 7,070 | 2,237,283 | 316.4 | ×12.0 | 31,001.2 | 7.6분 | 2026-08-09 | 기타 | 플레이리스트·모음 | 설명 | 293/298 |
| 188 | [Sad lo_fi🥺💔2026 ultimate](https://www.youtube.com/watch?v=q-iefUnWPCY) | mr prakash 😊 | 5,320 | 1,678,843 | 315.6 | – | 43,341.6 | 18.6분 | 2026-09-11 | 기타 | 음악 | 설명 | 143/147 |
| 189 | [𝙋𝙤𝙫 :- 𝘽𝙝𝙤𝙟𝙥𝙪𝙧𝙞 𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩 ∣∣ 𝙘𝙝𝙞𝙡𝙡 𝙜𝙪𝙮𝙨 𝙖𝙣𝙙 𝙚𝙣𝙟𝙤𝙮 ∣∣ 𝙂𝘼𝙇𝘼𝙓𝘼𝙔…](https://www.youtube.com/watch?v=areWocW1pXI) | AYUSH | 4,310 | 1,359,402 | 315.4 | ×182.6 | 31,683.7 | 8분 | 2026-09-07 | 기타 | 플레이리스트·모음 | 설명 | 180/180 |
| 190 | [Playlist For You To Create Fake Scenarios In Your Mind 🤍 ∣ …](https://www.youtube.com/watch?v=0gUwbTCQ78k) | NOXTUNE | 20,700 | 6,498,348 | 313.9 | ×1,069.2 | 89,401.5 | 12.6분 | 2026-08-08 | 기타 | 플레이리스트·모음 | 설명 | 1,399/1,423 |
| 191 | [𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 1](https://www.youtube.com/watch?v=rRxojiPo0SU) | 헿 | 630 | 196,339 | 311.6 | – | 2,121.1 | 10.6분 | 2026-07-19 | 기타 | 플레이리스트·모음 | 없음 | 40/40 |
| 192 | [Hallucination Journey ∣ Stoner Music & Trippy Visuals🌿](https://www.youtube.com/watch?v=QbWDBeBn_OY) | RYNO | 550 | 171,244 | 311.4 | ×209.9 | 1,315.6 | 10분 | 2026-06-12 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 13/13 |
| 193 | [🎹 Your Name (君の名は。) Relaxing Piano BGM ∣ Anime Piano Lounge](https://www.youtube.com/watch?v=Gv3qOVcC5X8) | AnimeBeats | 1,270 | 394,665 | 310.8 | ×191.9 | 2,217.3 | 57.6분 | 2026-04-25 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 | 19/19 |
| 194 | [𝘊𝘦𝘳𝘵𝘪𝘧𝘪𝘦𝘥 𝘋𝘦𝘴𝘪 𝘉𝘢𝘯𝘨𝘦𝘳𝘴 𝘵𝘩𝘢𝘵 𝘴𝘭𝘢𝘱 (+𝘵𝘪𝘮𝘦𝘴𝘵𝘢𝘮𝘱𝘴) 💅🔥](https://www.youtube.com/watch?v=PZcsGXrrBGY) | A BEE Editz | 10,200 | 3,164,633 | 310.3 | ×56.1 | 53,827.6 | 12.9분 | 2026-08-22 | 기타 | 플레이리스트·모음 | 설명 | 363/374 |
| 195 | [Tum Jo Aaye ✨ ∣∣ Kitab Song ∣∣ Bairan ( Slowed X Reverb ) M…](https://www.youtube.com/watch?v=xyL4vZnw5xs) | Mix Facto 02 | 40,300 | 12,487,210 | 309.9 | ×7,058.9 | 77,191.2 | 20.3분 | 2026-05-11 | 기타 | 음악 | 설명 | 2,719/2,730 |
| 196 | [Jazz Cover Indonesia ∣ Lagu Santai Untuk Bekerja 🎷](https://www.youtube.com/watch?v=kwqjENclcyE) | Ide Rahayu | 4,500 | 1,387,273 | 308.3 | ×767.7 | 13,552.4 | 74.5분 | 2026-07-09 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 152/152 |
| 197 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=099F7hK6c8c) | Song verse Hi… | 9,700 | 2,965,412 | 305.7 | – | 81,760.3 | 13분 | 2026-09-14 | 3. 공부·집중·작업 | 음악 | 설명 | 186/189 |
| 198 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ Q. 여전히 잊지 못했나요?](https://www.youtube.com/watch?v=ObbsVpc8iRM) | 청춘 | 1,360 | 415,352 | 305.4 | ×5.1 | 3,148.2 | 24분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 설명 | 491/491 |
| 199 | [Sands of Cairo at Night ∣ Egyptian Jazz & Relaxing Arabic L…](https://www.youtube.com/watch?v=k74U2uUB67s) | Moonlit Cairo | 4,110 | 1,246,980 | 303.4 | ×619.2 | 20,442.4 | 69.8분 | 2026-08-20 | 4. 카페·매장·라운지 | 음악 | 설명 | 127/127 |
| 200 | [Positive September 🍂 Relaxing Coffee Melody & Acoustic Chil…](https://www.youtube.com/watch?v=Bq4sPMz6fUk) | Chill Moments | 4,420 | 1,340,067 | 303.2 | ×239.0 | 25,343.9 | 142.9분 | 2026-08-28 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 98/98 |
| 201 | [🍂 알록달록 가을 음악이야기 ∣ Autumn Collection Vol.](https://www.youtube.com/watch?v=o3DojrmPMbs) | little step m… | 85 | 30,031 | 300.3 | ×36.0 | 1,573.4 | 206.4분 | 2026-10-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 3/3 |
| 202 | [Karpur Gauram ∣ कर्पूर गौरम् ∣ Shiva Stotram Trance Remix ∣…](https://www.youtube.com/watch?v=d47X_wGxFnY) | DigitalDeepDe… | 4,130 | 1,233,935 | 298.8 | ×1,301.6 | 7,919.4 | 11.1분 | 2026-05-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 337/337 |
| 203 | [pov: you're blushing while listening to this 🎧✨](https://www.youtube.com/watch?v=MOpFDe87RBM) | NIKKU | 9,120 | 2,724,306 | 298.7 | ×3,334.5 | 20,684.4 | 13.4분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 설명 | 1,534/1,537 |
| 204 | [💖 मेरा चाँद मुझे आया नजर ∣ New Hindi Song 2026 ∣ Romantic S…](https://www.youtube.com/watch?v=FxNQw0BRhWg) | Feel The Music | 3,320 | 985,019 | 296.7 | ×583.5 | 29,137.4 | 16.1분 | 2026-09-16 | 기타 | 음악 | 설명 | 65/65 |
| 205 | [Nhạc Thiền Tĩnh Tâm 🌿 Giải Tỏa Căng Thẳng, Buông Bỏ Muộn Ph…](https://www.youtube.com/watch?v=qTOqj4r0FNg) | Thiền Sen Trúc | 2,050 | 607,753 | 296.5 | ×152.7 | 5,848.5 | 58.6분 | 2026-07-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 433/433 |
| 206 | [난 아직 어린데](https://www.youtube.com/watch?v=Zo3DsQ9j2J0) | 맹묘 | 1,580 | 467,442 | 295.9 | – | 3,566.2 | 20.1분 | 2026-06-11 | 기타 | 플레이리스트·모음 | 없음 | 990/997 |
| 207 | [[グラブル] Granblue Fantasy OST - Last Salvation (vs. Raskeid &…](https://www.youtube.com/watch?v=TFsAT5TtzSg) | Decim | 1,650 | 485,696 | 294.4 | ×430.2 | 5,362.6 | 7분 | 2026-07-21 | 기타 | 음악 | 설명 | 416/417 |
| 208 | [LOVEIN & Ismail Uluçay - Drafting (Original Mix)](https://www.youtube.com/watch?v=clQARvetnyk) | LOVEIN | 40,500 | 11,884,118 | 293.4 | ×184.3 | 70,844.6 | 7.3분 | 2026-05-05 | 4. 카페·매장·라운지 | 음악 | 설명 | 422/422 |
| 209 | [90s Romantic Hits DJ Mix ∣ Hindi Love Song ∣ 90s Romantic B…](https://www.youtube.com/watch?v=Lk2qE-YdhS8) | AM MUSIC HUB | 4,000 | 1,170,815 | 292.7 | ×2,399.2 | 17,679.4 | 16분 | 2026-08-15 | 기타 | 음악 | 설명 | 50/50 |
| 210 | [Omnia vincit](https://www.youtube.com/watch?v=5yKI8IQNzAo) | Soul Beyond S… | 460 | 133,775 | 290.8 | – | 1,164.3 | 4.2분 | 2026-06-27 | 기타 | 정보·해설 | 설명 | 38/38 |
| 211 | [Patar Bashori ∣ পাতার বাঁশরী ∣ Lofi Bangla Song ∣ Emotional…](https://www.youtube.com/watch?v=rgKNbCrC-cc) | Jasu LOFI | 26,700 | 7,754,679 | 290.4 | ×3,912.6 | 94,870.5 | 4.1분 | 2026-07-30 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 1,081/1,081 |
| 212 | [🤍Golden brown x Love story (Piano Cover)🤍](https://www.youtube.com/watch?v=dK4RoOPXQ0Q) | Solaceful Keys | 212 | 61,208 | 288.7 | – | 647.3 | 4.1분 | 2026-07-17 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 82/82 |
| 213 | [Cozy Rainy Autumn Café 🍁 Relaxing Day with Warm Jazz Music …](https://www.youtube.com/watch?v=1wyP0BN_jqI) | Tiny Café Jazz | 3,900 | 1,125,330 | 288.6 | ×579.8 | 11,732.4 | 231.1분 | 2026-07-16 | 4. 카페·매장·라운지 | 음악 | 설명 | 457/464 |
| 214 | [Golden Melodies for the Soul (Sax & Violin Lounge)](https://www.youtube.com/watch?v=0shfF2LDgmI) | Timeless Echo | 5,700 | 1,643,724 | 288.4 | ×176.8 | 11,955.0 | 6.7분 | 2026-06-04 | 4. 카페·매장·라운지 | 음악 | 설명 | 356/356 |
| 215 | [Vintage Vibes: Best of 80s with Cyndi Lauper, Modern Talkin…](https://www.youtube.com/watch?v=1n5pMgUPYnk) | Disco Paradis… | 24,500 | 6,982,256 | 285.0 | ×2,799.6 | 104,668.9 | 117.2분 | 2026-08-14 | 기타 | 플레이리스트·모음 | 설명 | 523/532 |
| 216 | ["수고했어..오늘은 푹 자! 😴 마음을 편하게 해주는 피아노 수면음악 (10 Hours)](https://www.youtube.com/watch?v=3br0mkww4do) | jazzyang 재즈냥 | 1,370 | 389,109 | 284.0 | ×1,425.3 | 4,109.0 | 616.6분 | 2026-07-17 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 91/124 |
| 217 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 l 연모(戀慕)](https://www.youtube.com/watch?v=uVbmoXg5YvI) | 미니악단 | 643 | 179,372 | 279.0 | ×726.2 | 1,504.8 | 69분 | 2026-06-23 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 88/90 |
| 218 | [[커버곡] 가는세월 🎧 락발라드로 다시 태어난 불후의 명곡 🎶두둥치 DUDUNGCHI](https://www.youtube.com/watch?v=0J4iOmTGAgo) | 두둥치 | 255 | 70,711 | 277.3 | ×456.2 | 441.0 | 4.2분 | 2026-05-12 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 26/26 |
| 219 | [Peni Me Chheni Satai Diyo -Instagram Trending Lofi Song ∣ A…](https://www.youtube.com/watch?v=gJyWm3GFFik) | Tushar Music … | 5,660 | 1,569,234 | 277.2 | ×1,307.7 | 19,569.7 | 6.1분 | 2026-08-01 | 8. 로파이·시티팝·칠 | 음악 | 없음 | 87/87 |
| 220 | [𝐀𝐋𝐋 𝐓𝐑𝐄𝐍𝐃𝐈𝐍𝐆 𝐇𝐈𝐍𝐃𝐈 𝐒𝐎𝐍𝐆𝐒 𝟐𝟎𝟐𝟔 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 🎀 ∣COZI](https://www.youtube.com/watch?v=HNdauINck9s) | cozi_music | 29,400 | 8,086,546 | 275.1 | ×68.8 | 91,958.1 | 15.2분 | 2026-07-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 2,887/2,923 |
| 221 | [🏨 Luxury Hotel Lounge ∣ Smooth Jazz & Elegant Background Mu…](https://www.youtube.com/watch?v=GBLcMvTFGyg) | AMBER&OAK | 7,170 | 1,971,434 | 275.0 | ×896.1 | 14,297.6 | 100.4분 | 2026-06-04 | 4. 카페·매장·라운지 | 음악 | 설명 | 249/254 |
| 222 | [Shri Krishna Govind Hare Murari - Non Stop Krishna Bhajans …](https://www.youtube.com/watch?v=Tqr5PqrzeQw) | Bhajan World … | 33,000 | 9,069,848 | 274.8 | ×122.8 | 80,397.9 | 29.8분 | 2026-06-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,540/1,540 |
| 223 | [Rest Your Mind ∣ Your Brain Needs Silence ∣ Dopamine Reset …](https://www.youtube.com/watch?v=UWZ_QQNKmes) | Essential Ind… | 19,100 | 5,242,650 | 274.5 | ×3,583.5 | 45,570.9 | 20.7분 | 2026-06-27 | 1. 수면·명상·힐링 | 음악 | 설명 | 833/843 |
| 224 | [😱NEW VIRAL😱SOBRANG SIKAT SA DISCO DJ MIX KABA-KABA NONSTOP …](https://www.youtube.com/watch?v=EF2Bbs1GWm0) | VIRAL MIX COL… | 16,700 | 4,581,418 | 274.3 | ×20,138.1 | 25,981.6 | 29.8분 | 2026-04-27 | 기타 | 음악 | 설명 | 606/606 |
| 225 | [Hum Tere Hote Toh ( Official Music ) Musafir cafe ....](https://www.youtube.com/watch?v=V_UCyoYIWEo) | Music Covers … | 1,750 | 479,234 | 273.9 | ×418.2 | 5,695.6 | 4.4분 | 2026-07-28 | 4. 카페·매장·라운지 | 음악 | 설명 | 79/79 |
| 226 | [Heartbreaking 💔 songs + lofi Mashup songs Slowed Reverb son…](https://www.youtube.com/watch?v=swi-om1VW34) | JR buzdar off… | 16,400 | 4,476,229 | 272.9 | ×12,538.5 | 79,638.0 | 8분 | 2026-08-25 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 202/203 |
| 227 | [[ Playlist ] 어떻게 너가 다른 남자를 만나](https://www.youtube.com/watch?v=0USEQaYCf78) | 하온 | 1,700 | 462,610 | 272.1 | – | 5,459.3 | 20.9분 | 2026-07-27 | 기타 | 플레이리스트·모음 | 설명 | 48/48 |
| 228 | [.•♫•♬•𝙁𝙄𝙉𝙀𝙎𝙃𝙔𝙏 PLAYLIST•♬•♫](https://www.youtube.com/watch?v=wYiyAR_dBDU) | loverswift | 4,870 | 1,324,314 | 271.9 | ×31.8 | 14,894.1 | 16.8분 | 2026-07-23 | 기타 | 플레이리스트·모음 | 설명 | 112/113 |
| 229 | [Vachindamma (Lyrics + English Translation) ∣ Geetha Govinda…](https://www.youtube.com/watch?v=DliA185LSPU) | LYRICS FOR YOU | 5,220 | 1,417,140 | 271.5 | ×236.7 | 8,251.9 | 4.1분 | 2026-05-01 | 기타 | 한 곡 | 설명 | 240/240 |
| 230 | [조영버 노동요](https://www.youtube.com/watch?v=twTedu4I1mg) | 궈바오러우 | 498 | 134,570 | 270.2 | – | 801.9 | 19.7분 | 2026-05-05 | 3. 공부·집중·작업 | 플레이리스트·모음 | 없음 | 205/205 |
| 231 | [[Playlist] 드라마 OST 모음](https://www.youtube.com/watch?v=h_2uk2pTQQA) | playlistsilya… | 771 | 206,420 | 267.7 | ×13.4 | 3,916.2 | 17.5분 | 2026-08-28 | 13. OST·사운드트랙 | 플레이리스트·모음 | 없음 | 17/17 |
| 232 | [우리들의 발라드2 1회 플레이리스트｜가을밤 마음을 울린 발라드 7곡 #우리들의발라드 #우발2](https://www.youtube.com/watch?v=wPEmG4xfTLE) | 우낄라꼬 | 1,190 | 317,500 | 266.8 | – | 25,084.2 | 30.4분 | 2026-10-07 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 63/64 |
| 233 | [🌊2000년 넘게 전해진 가장 슬픈 노래 ∣ 님아, 그 강을 건너지 마오 ∣ 역사노래 ∣ 사랑노래](https://www.youtube.com/watch?v=4q22526wbNM) | 노래말싸미 | 273 | 72,796 | 266.6 | ×320.7 | 568.9 | 4.6분 | 2026-06-14 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 38/38 |
| 234 | [Om Namo Bhagavate Vasudevaya ∣ 1 Hour Divine Vishnu Meditat…](https://www.youtube.com/watch?v=OfDob7wO9OU) | Zynora | 4,450 | 1,179,504 | 265.1 | ×222.4 | 7,769.5 | 77.8분 | 2026-05-21 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 317/316 |
| 235 | [별일 없던 하루였는데, 괜히 마음이 시끄러운 밤](https://www.youtube.com/watch?v=mc73qn75vMs) | 리듬다방(김리다) | 1,360 | 357,406 | 262.8 | ×742.3 | 2,693.7 | 7.5분 | 2026-06-09 | 기타 | 음악 | 설명 | 207/209 |
| 236 | [⛈️(No Ads) WARNING: YOU MAY SLEEP FAST 😴 NYC Rain on Window…](https://www.youtube.com/watch?v=HLp0t2jZlKQ) | Dreamy Raining | 3,810 | 992,292 | 260.4 | ×42.9 | 5,860.0 | 600분 | 2026-05-04 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 90/94 |
| 237 | [Sunday Morning Coffee Club ∣ R&B, Hip Hop, Afrobeats ∣ Feat…](https://www.youtube.com/watch?v=2zzgY6uxZ6o) | EChen | 7,820 | 2,034,173 | 260.1 | ×44.4 | 12,576.1 | 59.4분 | 2026-05-11 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 215/214 |
| 238 | [탈북할 때 듣는 플리](https://www.youtube.com/watch?v=rrgoyhVFJ68) | 비둘기 | 2,920 | 758,371 | 259.7 | ×251.3 | 9,518.9 | 57.6분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 없음 | 1,536/1,536 |
| 239 | [A playlist cuz kanhi is your safe place 🦚🪷🪈🦢 ∣∣ Song playli…](https://www.youtube.com/watch?v=vH7kCnulptw) | Lily⋆.𐙚 ̊ | 9,350 | 2,412,710 | 258.0 | – | 18,593.8 | 17.5분 | 2026-06-12 | 기타 | 플레이리스트·모음 | 설명 | 843/856 |
| 240 | [🌼 Sawan Shiv Bhajan 2026 ∣ Peaceful Mahadev Bhakti Song ∣ B…](https://www.youtube.com/watch?v=I_vnh6nZW6c) | Bhajan Soul C… | 8,590 | 2,208,363 | 257.1 | ×288.1 | 21,267.6 | 5.8분 | 2026-07-08 | 기타 | 음악 | 설명 | 612/612 |
| 241 | [[𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 삶에 무뎌지는 법](https://www.youtube.com/watch?v=8KGuQMhnb14) | 꾹팅 | 1,220 | 311,726 | 255.5 | ×61.7 | 2,333.1 | 19.4분 | 2026-06-08 | 기타 | 플레이리스트·모음 | 설명 | 363/379 |
| 242 | [𝐬𝐭𝐮𝐝𝐲 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 이번엔 아무한테도 말 안 하고 준비한다 🤫 전문직·수험생 시험공부 집중 로파이 …](https://www.youtube.com/watch?v=eRQFKz_nigU) | loni pli 로니플리 | 1,450 | 366,814 | 253.0 | ×109.6 | 9,201.5 | 137.3분 | 2026-09-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 85/84 |
| 243 | [The Shiva Reset ∣ Shiva Trance for the Overstimulated Mind …](https://www.youtube.com/watch?v=N95edHAuFzA) | Nirvana Beats | 7,030 | 1,774,365 | 252.4 | ×342.7 | 24,523.4 | 6.8분 | 2026-08-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 295/295 |
| 244 | [Zindagi ∣ Chal Thora Aur ∣ Na Kwahish Na Koi Tamana Mujhe (…](https://www.youtube.com/watch?v=dyOp23A-i_o) | cefur studio | 11,400 | 2,867,950 | 251.6 | ×601.5 | 22,994.7 | 4.8분 | 2026-06-17 | 기타 | 음악 | 설명 | 1,835/1,846 |
| 245 | [MIMIFY - I Waited too Long (Original Mix)](https://www.youtube.com/watch?v=F2Iga1V4cqo) | MIMIFY | 18,500 | 4,608,819 | 249.1 | ×414.9 | 46,150.4 | 7.8분 | 2026-07-12 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 675/675 |
| 246 | [జీవితంలో ఒక్కసారైనా ఆ ఏడుకొండలు ఎక్కాలయ్యా ∣Soulful Sri Ven…](https://www.youtube.com/watch?v=sfnGhZdoNQk) | Surendra's Mu… | 5,100 | 1,266,787 | 248.4 | ×742.5 | 10,190.1 | 5.3분 | 2026-06-18 | 기타 | 음악 | 설명 | 554/554 |
| 247 | [𝐒𝐨𝐧𝐠𝐬 𝐭𝐡𝐚𝐭 𝐟𝐞𝐞𝐥 𝐥𝐢𝐤𝐞 𝐚 𝐛𝐨𝐥𝐥𝐲𝐰𝐨𝐨𝐝 𝐦𝐨𝐯𝐢𝐞 🦢🪷🪐∣∣ songs playlist…](https://www.youtube.com/watch?v=r88MexwnbMA) | ⋆.ʚଓ ּ𝐋𝗒𝗋𝗂𝖼αᥣ… | 6,790 | 1,668,453 | 245.7 | ×17.0 | 19,454.0 | 10.5분 | 2026-07-26 | 기타 | 플레이리스트·모음 | 설명 | 291/291 |
| 248 | [All Stress Disappears When This Music Starts Playing 🎶 Emot…](https://www.youtube.com/watch?v=mtelE3vg758) | Nature Healin… | 7,390 | 1,810,621 | 245.0 | ×5,309.7 | 11,048.9 | 99.6분 | 2026-05-09 | 1. 수면·명상·힐링 | 음악 | 설명 | 482/479 |
| 249 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐅𝐨𝐫 𝐘𝐨𝐮 𝐓𝐨 𝐂𝐫𝐞𝐚𝐭𝐞 𝐅𝐚𝐤𝐞 𝐒𝐜𝐞𝐧𝐚𝐫𝐢𝐨𝐬 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐌𝐢𝐧𝐝 🤍 ∣ …](https://www.youtube.com/watch?v=flQgOwg4jLI) | Ashik's Cloud… | 15,600 | 3,805,234 | 243.9 | ×6.3 | 37,349.4 | 15.2분 | 2026-07-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 965/970 |
| 250 | [Relax Cha Cha Music 🪘 Havana Cafe Music - Cha Cha Son Cubano](https://www.youtube.com/watch?v=poj2d6YKC6w) | Cha Cha Havan… | 1,610 | 390,924 | 242.8 | ×2,832.8 | 2,362.7 | 6.4분 | 2026-05-07 | 4. 카페·매장·라운지 | 음악 | 설명 | 96/97 |
| 251 | [Viral Pop Songs Cover 2026 🎙 Top Music Playlist Hits](https://www.youtube.com/watch?v=JKRRl5-5-hw) | Acoustic Ther… | 21,000 | 5,079,427 | 241.9 | ×8,990.1 | 34,704.0 | 57.4분 | 2026-05-26 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 설명 | 512/518 |
| 252 | [Relaxing Piano Music with Rain Sounds for Deep Sleep - Calm…](https://www.youtube.com/watch?v=dzRT9vqg9xs) | RainwoodPiano… | 1,270 | 306,686 | 241.5 | ×195.8 | 14,618.7 | 110분 | 2026-09-29 | 2. 자연 소리·백색소음 | 음악 | 설명 | 38/39 |
| 253 | [Bedroom R&B After Hours ∣ Obsessive Love Playlist ∣ Dark ro…](https://www.youtube.com/watch?v=WRi5W4B2vgQ) | afterlove. | 7,490 | 1,808,238 | 241.4 | ×235.5 | 67,835.9 | 81.7분 | 2026-09-23 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 177/181 |
| 254 | [Put Your Baby to Sleep in 2 Minutes 😴 3 Hours Deep Lullaby …](https://www.youtube.com/watch?v=2W9Y6KcJK1E) | Calm Baby Lul… | 4,190 | 1,006,903 | 240.3 | ×1,910.6 | 5,867.5 | 183.3분 | 2026-05-01 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 0/0 |
| 255 | [Heartbreaking Lofi Mashup 💔 (Slowed + Reverb) ∣ Study, Focu…](https://www.youtube.com/watch?v=6mgb7GxwLvA) | stylish offic… | 12,100 | 2,889,364 | 238.8 | – | 42,343.5 | 7.8분 | 2026-08-13 | 3. 공부·집중·작업 | 음악 | 설명 | 132/135 |
| 256 | [Rain and Soft Piano Music for Deep Sleep - Calm Sleep and S…](https://www.youtube.com/watch?v=8DzndrjZi18) | RainwoodPiano… | 1,270 | 301,777 | 237.6 | ×192.6 | 6,038.1 | 31.9분 | 2026-08-31 | 1. 수면·명상·힐링 | 음악 | 설명 | 40/40 |
| 257 | [MUSIK SANTAI VIRAL 2026 🎧 Lagu Pop Indonesia Akustik Terbai…](https://www.youtube.com/watch?v=bZEwYquV6Kg) | Akustik Cantik | 10,500 | 2,470,417 | 235.3 | ×441.1 | 26,211.4 | 78.5분 | 2026-07-18 | 기타 | 정보·해설 | 설명 | 182/175 |
| 258 | [🌼 Soulful Shiv Bhajan 2026 ∣ Peaceful Mahadev Bhakti Song ∣…](https://www.youtube.com/watch?v=soTUDFUagOU) | Divine Bhajan… | 5,950 | 1,378,226 | 231.6 | ×342.9 | 14,543.0 | 6.6분 | 2026-07-17 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 395/395 |
| 259 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=FB8QuMi3fTs) | Z B Official … | 21,200 | 4,908,118 | 231.5 | ×22,618.1 | 80,309.4 | 7.7분 | 2026-08-20 | 3. 공부·집중·작업 | 음악 | 설명 | 203/203 |
| 260 | [Heartbreaking💔 mashup lofi Songs ∣ Slowed + Reverb ∣ Late N…](https://www.youtube.com/watch?v=z3H-p4r9EC4) | Soulmate Song… | 7,510 | 1,722,783 | 229.4 | ×5,733.1 | 31,769.5 | 8분 | 2026-08-27 | 3. 공부·집중·작업 | 음악 | 설명 | 139/139 |
| 261 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 틀기만 해도 기분이 좋아지는 플리☀️🌿 (광고없음) 국내 노래 모음](https://www.youtube.com/watch?v=mg5OWdP3DL8) | 오늘의 플리 | 6,700 | 1,522,659 | 227.3 | ×163.9 | 22,346.1 | 603.4분 | 2026-08-13 | 기타 | 플레이리스트·모음 | 없음 | 150/154 |
| 262 | [Music Therapy Helps Restore the Nervous System 🌿 Relaxing M…](https://www.youtube.com/watch?v=yP0NAC8Hzy8) | Clara Monica … | 3,500 | 789,908 | 225.7 | ×24.1 | 7,065.9 | 19.7분 | 2026-06-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 236/239 |
| 263 | [Slow and Reverb Pashto Tappy 🎧 ∣ New Pashto Song ∣ Relaxing…](https://www.youtube.com/watch?v=88J0afFBt3s) | MarjanMusic | 4,460 | 1,006,434 | 225.7 | ×537.3 | 8,009.0 | 13분 | 2026-06-16 | 기타 | 음악 | 설명 | 81/81 |
| 264 | [MEGA BASS 🔊🔥 EXTREME NONSTOP EDM REMIX 💯 MONSTER DROP ⚠️ CL…](https://www.youtube.com/watch?v=Kc071SEvHgc) | Street Bass C… | 27,100 | 6,111,463 | 225.5 | ×8,718.2 | 41,480.6 | 42.7분 | 2026-05-26 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 1,383/1,396 |
| 265 | [Hyperfocus ∣ LOCK IN for 3 Hours ∣ Deep Work Study With Me …](https://www.youtube.com/watch?v=UXwJ9RwdyHs) | Work With Paul | 18,000 | 4,058,360 | 225.5 | ×27.2 | 94,198.3 | 172분 | 2026-09-07 | 3. 공부·집중·작업 | 긴 한 곡·반복 | 설명 | 492/507 |
| 266 | [[PLAYLIST] 할머니가 돼서도 들을 노래](https://www.youtube.com/watch?v=Oomy8ijLJxQ) | 당무 | 2,590 | 583,331 | 225.2 | ×91.8 | 3,584.3 | 23.7분 | 2026-05-10 | 기타 | 플레이리스트·모음 | 없음 | 131/131 |
| 267 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Sad…](https://www.youtube.com/watch?v=KjFcRYZBKs0) | Music Nest HD | 11,800 | 2,656,453 | 225.1 | ×4,883.2 | 114,715.8 | 8.9분 | 2026-09-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 101/103 |
| 268 | [The Love Playlist You’ve Been Looking For😌🤍](https://www.youtube.com/watch?v=G4M-E29DlAE) | Melovo tunes | 3,320 | 743,337 | 223.9 | – | 5,311.5 | 10.4분 | 2026-06-02 | 기타 | 플레이리스트·모음 | 설명 | 800/800 |
| 269 | [VIVANT ᐸMain themeᐳ](https://www.youtube.com/watch?v=MuGFcUggtDs) | Akira Senju -… | 7,280 | 1,629,345 | 223.8 | ×24.9 | 19,120.6 | 4.6분 | 2026-07-27 | 13. OST·사운드트랙 | 정보·해설 | 설명 | 0/0 |
| 270 | [🍂편안해지는 따뜻한 가을 노래 ∣ 추억의 올드팝송 ∣ 가을 카페 팝송 감미로운 여친 목소리∣ Oldies …](https://www.youtube.com/watch?v=yfKtKmmUsoQ) | 나무감성 NAMUVIBE | 2,410 | 529,194 | 219.6 | ×35.4 | 25,814.8 | 135분 | 2026-09-29 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 173/173 |
| 271 | [worry (Instrumental Ultra Slowed)](https://www.youtube.com/watch?v=zF_hN38VVzY) | LONOWN - Topic | 6,620 | 1,449,134 | 218.9 | ×5.5 | 8,054.5 | 4.3분 | 2026-04-23 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 0/364 |
| 272 | [Playlist ∣ Start Your Work with This 😎 Light Focus, Solid R…](https://www.youtube.com/watch?v=PF7MEHrmFjQ) | Noirvoya | 371 | 80,931 | 218.1 | ×335.1 | 611.8 | 16.4분 | 2026-06-10 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 30/30 |
| 273 | [[𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁] 행운이 따라올 것 같은 여름 플리 🌊🚃 ∣ 괜히 여행 가고 싶어지는 음악 ∣ 카페 BG…](https://www.youtube.com/watch?v=sdyu1kMXQPw) | HIWAVA | 2,080 | 450,955 | 216.8 | ×387.8 | 3,211.6 | 165.3분 | 2026-06-01 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 157/158 |
| 274 | [Top Spotify Hits 2026 🎵 Trending English Love Songs ∣ Acous…](https://www.youtube.com/watch?v=FPlJt2A0yYo) | Chill Chord | 11,900 | 2,577,455 | 216.6 | ×138.7 | 27,603.4 | 54.8분 | 2026-07-18 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 282/286 |
| 275 | [Asiwafuni](https://www.youtube.com/watch?v=9c1b0JLxKG4) | Benzoo - Topic | 11,900 | 2,542,749 | 213.7 | ×11.0 | 31,040.8 | 6.7분 | 2026-07-30 | 기타 | 음악 | 설명 | 0/1,364 |
| 276 | [이선희 노래 〈잘가요, 내사랑〉 ∣ Goodbye, The One I Loved ∣ 再见了，我曾爱过的人 ∣…](https://www.youtube.com/watch?v=Ibdr_7ukGyI) | AI음악으로멜론1위찍습니다 | 3,080 | 651,857 | 211.6 | ×993.7 | 4,168.6 | 4.8분 | 2026-05-16 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 707/713 |
| 277 | [Sad Song Playlist (+ with timestamps) !!](https://www.youtube.com/watch?v=q48Y5Hf83Bk) | Mood Tapes 🎶 | 17,900 | 3,785,269 | 211.5 | ×85.9 | 28,528.2 | 14.7분 | 2026-06-09 | 기타 | 플레이리스트·모음 | 설명 | 1,520/1,544 |
| 278 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 안 붙잡을게, 진짜로](https://www.youtube.com/watch?v=mgSfxFVkmv4) | 탱이 | 1,680 | 354,226 | 210.8 | ×34.0 | 2,884.1 | 18.3분 | 2026-06-19 | 기타 | 플레이리스트·모음 | 설명 | 150/151 |
| 279 | [[Playlist] 스트레이 키즈 노래 모음 연속 듣기 🔥 Stray Kids Best Songs 2026…](https://www.youtube.com/watch?v=Lj8FLAC9h58) | 내귀에 PLY | 2,300 | 483,211 | 210.1 | ×1,421.2 | 7,062.8 | 120.4분 | 2026-08-12 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 164/174 |
| 280 | [일할 때 듣기 좋은 발라드 베스트 100곡 🌸 광고 없는 감성 플레이리스트 왁스, 소울스타, 원티드, 임창…](https://www.youtube.com/watch?v=aJ61beIT3qc) | Dragon Melody | 1,260 | 259,532 | 206.0 | ×548.7 | 2,075.6 | 138.7분 | 2026-06-17 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 30/31 |
| 281 | [#등불 - #영사운드(1972년) Covered by sMUSIC#영사운드 #Reinterpreting K…](https://www.youtube.com/watch?v=tW_gZzlbg-4) | sMusic 7080_명… | 6,860 | 1,407,280 | 205.1 | ×437.2 | 8,616.4 | 4.2분 | 2026-05-10 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 없음 | 296/303 |
| 282 | [Odysseus](https://www.youtube.com/watch?v=WCxx_OVOVUw) | Ludwig Görans… | 43,300 | 8,838,833 | 204.1 | ×18.2 | 92,151.3 | 8.7분 | 2026-07-16 | 13. OST·사운드트랙 | 음악 | 설명 | 0/5,594 |
| 283 | [A playlist of nusrat fateh ali khan all popular qawaali's 💝💘](https://www.youtube.com/watch?v=idCpl6LfnKo) | preet_slaylist | 49,800 | 10,142,363 | 203.7 | ×60.0 | 64,810.3 | 9.2분 | 2026-05-16 | 기타 | 플레이리스트·모음 | 설명 | 4,952/5,021 |
| 284 | [Gladiator Ambience — Cinematic & Emotional Music for Honor …](https://www.youtube.com/watch?v=iBofqYaXA_U) | sleyvenn | 5,050 | 1,019,143 | 201.8 | ×231.2 | 7,075.7 | 120분 | 2026-05-29 | 2. 자연 소리·백색소음 | 음악 | 설명 | 284/284 |
| 285 | [सुकून देने वाली धुन 🏔️ ∣ Mind Relaxing Music ∣ Flute Music](https://www.youtube.com/watch?v=dLdXYN50hgQ) | Soulful Music… | 4,510 | 904,871 | 200.6 | ×12,311.2 | 6,615.9 | 5.9분 | 2026-06-05 | 기타 | 음악 | 설명 | 331/331 |
| 286 | [🍉 아침에 커피 마시면서 혼자 듣는데 너무좋다. ∣ 하루 종일 틀어 놓으세요🎵7080추억의 올드팝 #감성팝…](https://www.youtube.com/watch?v=iRAcLZyPbsA) | woozune | 5,780 | 1,154,763 | 199.8 | ×102.4 | 13,681.5 | 74.3분 | 2026-07-27 | 9. 가요·발라드·트로트 | 음악 | 설명 | 187/197 |
| 287 | [☀️ Top Acoustic Love Hits 2026 💚 Relaxing Pop Covers for Pe…](https://www.youtube.com/watch?v=r0t7mEWAGyY) | Acoustic Pulse | 9,650 | 1,921,656 | 199.1 | ×39.1 | 18,778.4 | 51.8분 | 2026-07-10 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 166/168 |
| 288 | [राग भैरव ∣ भगवान शिव का पवित्र प्रभात राग ∣ Raga Bhairav ∣ …](https://www.youtube.com/watch?v=3kgbzavVRiY) | मनतरंग ∣ ManT… | 1,950 | 387,317 | 198.6 | – | 8,879.3 | 11.7분 | 2026-09-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 82/82 |
| 289 | [Iske da faniyaar song Slowed + Reverb Lofi Music Mix ∣ Chil…](https://www.youtube.com/watch?v=yoLa1Xlkhvo) | @sanjumusic | 5,440 | 1,078,801 | 198.3 | ×595.4 | 10,096.4 | 5.1분 | 2026-07-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 217/217 |
| 290 | [들꽃처럼 살다가](https://www.youtube.com/watch?v=1vBXiLsHZrs) | 소은뮤직 | 583 | 115,471 | 198.1 | ×446.7 | 1,007.4 | 4.7분 | 2026-06-27 | 기타 | 음악 | 설명 | 108/114 |
| 291 | [Samadhi in the Stone ∣ Shiva Meditation Music ∣ Himalayan C…](https://www.youtube.com/watch?v=yp10IdD2SxY) | Divya vaani m… | 217 | 42,503 | 195.9 | ×99.4 | 2,874.9 | 6.1분 | 2026-10-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 11/11 |
| 292 | [빗속 파리의 라흐마니노프 🌧️ In the Style of Rachmaninoff , 깊고 잔잔한 클래식 …](https://www.youtube.com/watch?v=msDBphyeZIc) | Moonlight rep… | 2,390 | 466,789 | 195.3 | ×754.1 | 4,782.9 | 65.6분 | 2026-07-14 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 116/116 |
| 293 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 듣자마자 흥 폭발하는🔥 최신 K-POP 노래 모음 노동요](https://www.youtube.com/watch?v=yngpCQNKY_M) | 클로버 플레이리스트 | 3,580 | 696,552 | 194.6 | ×9.3 | 5,952.5 | 40.9분 | 2026-06-25 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 69/70 |
| 294 | [Lagu Pop Santai Indonesia 2026 ☕ Lagu Pop Indonesia Terbaik…](https://www.youtube.com/watch?v=MoghOkKhNFk) | MITRO MUSIC | 5,450 | 1,060,009 | 194.5 | ×212.1 | 6,760.6 | 83.7분 | 2026-05-16 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 178/176 |
| 295 | [애매모호한 첫사랑](https://www.youtube.com/watch?v=A6rImTTl348) | na tsu | 933 | 181,463 | 194.5 | – | 1,953.8 | 19.3분 | 2026-07-19 | 기타 | 플레이리스트·모음 | 설명 | 419/419 |
| 296 | [🔥 𝗔𝗟𝗟 𝗧𝗥𝗘𝗡𝗗𝗜𝗡𝗚 𝗣𝗔𝗞𝗜𝗦𝗧𝗔𝗡𝗜 𝗦𝗢𝗡𝗚𝗦 🎶 ∣ 𝗩𝗜𝗥𝗔𝗟 𝗛𝗜𝗧𝗦 𝟮𝟬𝟮𝟲 🎧 ∣ 𝗧𝗢𝗣 …](https://www.youtube.com/watch?v=XL5PUUwrztg) | cozi_music | 29,400 | 5,695,105 | 193.7 | ×48.5 | 86,372.0 | 19.6분 | 2026-08-15 | 1. 수면·명상·힐링 | AI 음악 | 설명 | 2,153/2,236 |
| 297 | [Könül Xasıyeva - Yaralayırsan ∣ Piano Version by Xeqan](https://www.youtube.com/watch?v=Fqfo2bGkZik) | Xeqan | 5,780 | 1,102,030 | 190.7 | ×26.2 | 6,493.3 | 5.5분 | 2026-05-03 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 428/428 |
| 298 | [lock the f*** in. (playlist)](https://www.youtube.com/watch?v=1mAMpmFvceY) | lucent | 7,670 | 1,460,403 | 190.4 | ×193.3 | 23,781.7 | 240분 | 2026-08-19 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 394/394 |
| 299 | [일할때 듣기좋은 발라드 추천 광고없는 노래모음 유튜브 베스트곡 TOP BEST 100 임창정,성시경,더원,…](https://www.youtube.com/watch?v=YVeqKohQmuw) | LeafVibe 4K | 1,380 | 261,976 | 189.8 | ×327.9 | 2,019.0 | 71.8분 | 2026-06-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 13/13 |
| 300 | [Navkar mantra's Golden Shield ∣ Feel the Ancient Jain Power…](https://www.youtube.com/watch?v=FEQe99gciwU) | Navkarbhakti … | 4,350 | 821,108 | 188.8 | – | 4,795.7 | 8.1분 | 2026-05-02 | 1. 수면·명상·힐링 | 음악 | 설명 | 197/197 |
| 301 | [아득히 먼 곳 ∣ 이별 감성 발라드 ∣ 커버 노래 편곡 수노 AI](https://www.youtube.com/watch?v=8l6a5DRZqHU) | 엄마의 세월 - 한국 발… | 1,110 | 209,114 | 188.4 | ×349.7 | 1,411.2 | 4분 | 2026-05-25 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 20/20 |
| 302 | [【洋楽Playlist】何も考えずに聴きたい心地いいChill R&B｜Relax｜Smooth Vibes](https://www.youtube.com/watch?v=6qkUHaRXvtE) | Ethereal TIME | 4,720 | 888,777 | 188.3 | ×445.1 | 7,741.9 | 65.2분 | 2026-06-27 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 63/63 |
| 303 | [♫ 𝗔𝗹𝗹 𝗛𝗶𝗻𝗱𝗶 𝗧𝗿𝗲𝗻𝗱𝗶𝗻𝗴 𝗦𝗼𝗻𝗴𝘀 𝗼𝗳 2026 ♫🎧🤍#HindiSongs#Playlist](https://www.youtube.com/watch?v=eC61t3Nw-vs) | 𝐌𝐚𝐧𝐬𝐢~ | 8,620 | 1,608,608 | 186.6 | ×6.8 | 14,897.2 | 11.9분 | 2026-07-04 | 기타 | 플레이리스트·모음 | 없음 | 506/506 |
| 304 | [2026 Ultimate Mind Relaxing Lofi Beats ∣ Study Sleep & Chil…](https://www.youtube.com/watch?v=FYePEj0IZC8) | Ace LoFi | 9,400 | 1,752,870 | 186.5 | ×4,600.7 | 17,247.3 | 28.2분 | 2026-07-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 140/140 |
| 305 | [I Am a Child of God ∣ Afrobeat Kids Gospel Song for Kids](https://www.youtube.com/watch?v=qxH8aOt45xE) | Kidsgobible | 20,800 | 3,864,459 | 185.8 | ×72.9 | 21,632.0 | 6.8분 | 2026-04-24 | 15. CCM·찬양·국악… | 음악 | 설명 | 0/0 |
| 306 | [[ 𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕 ] 전남친 잊는 플리](https://www.youtube.com/watch?v=bLYI4NHve9Y) | 아야 | 1,300 | 241,360 | 185.7 | – | 3,022.6 | 17.4분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 없음 | 55/57 |
| 307 | [Peaceful Piano with Rain Sounds ∣ Relaxing Sleep Music for …](https://www.youtube.com/watch?v=Ral_oDb724k) | Soft Rain Pia… | 2,690 | 496,093 | 184.4 | ×85.6 | 3,854.4 | 47.1분 | 2026-06-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 104/104 |
| 308 | [POV: The ultimate south indian dance🪩 playlist to blast at …](https://www.youtube.com/watch?v=Hh_Vewjk7wo) | Ethereal Echo… | 12,700 | 2,337,763 | 184.1 | ×7.4 | 17,296.3 | 18.6분 | 2026-06-07 | 기타 | 플레이리스트·모음 | 설명 | 299/300 |
| 309 | [🌧️ Relaxing Piano & Bird Sounds ∣ Rainy Nature Ambience for…](https://www.youtube.com/watch?v=O0goqFNLWDs) | Solace Birdso… | 1,790 | 329,397 | 184.0 | ×54.9 | 3,708.9 | 92.3분 | 2026-07-23 | 2. 자연 소리·백색소음 | 음악 | 설명 | 223/223 |
| 310 | [🎶 2026 Ultimate Mind Relaxing Lofi Beats ∣∣ Study, Sleep & …](https://www.youtube.com/watch?v=453LJJX0ncc) | Hindi Lofi So… | 12,700 | 2,335,168 | 183.9 | ×6,504.6 | 20,446.0 | 30.7분 | 2026-06-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 199/199 |
| 311 | [ĐẾN KHI NÀO (Hot Trend)...Mặt Trời Ngừng Chiếu ∣ Những Bản …](https://www.youtube.com/watch?v=pB64u5qBd5g) | Chà Là Chill | 38,900 | 7,137,035 | 183.5 | ×53.3 | 145,785.3 | 91.8분 | 2026-09-01 | 8. 로파이·시티팝·칠 | 긴 한 곡·반복 | 설명 | 509/509 |
| 312 | [Relax Cha Cha Music 🪘 Havana Cafe Music - Cha Cha Son Cuban…](https://www.youtube.com/watch?v=sUO0XTpAiCY) | Cha Cha Havan… | 1,610 | 294,448 | 182.9 | ×2,133.7 | 1,996.8 | 5.5분 | 2026-05-25 | 4. 카페·매장·라운지 | 음악 | 설명 | 20/20 |
| 313 | [Viral OPM Hits 2026 🇵🇭 Trending Tagalog Love Songs 🎧 Spotif…](https://www.youtube.com/watch?v=au1ycoHD9cY) | Calm Guitar | 11,600 | 2,119,667 | 182.7 | ×102.7 | 28,499.9 | 64.6분 | 2026-08-06 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 199/201 |
| 314 | [(NO MID-ROLL ADS) Cozy Rainy & Spooky Halloween 🍂 Fall Jazz…](https://www.youtube.com/watch?v=p1b2tWu4XkE) | Relaxing Chri… | 4,360 | 796,664 | 182.7 | ×301.8 | 50,198.9 | 249.2분 | 2026-10-04 | 7. 재즈·보사노바 | 음악 | 설명 | 383/389 |
| 315 | [가을이 머무는 호숫가 ∣ 피아노·첼로·바이올린으로 듣는 고요한 클래식](https://www.youtube.com/watch?v=zNMH3ua74tE) | 순례자 우물 | 939 | 171,424 | 182.6 | ×484.2 | 3,989.5 | 122분 | 2026-09-07 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 36/39 |
| 316 | [Peaceful Piano, Flute & Water Sounds 💧 ∣ Relaxing Music for…](https://www.youtube.com/watch?v=NO0Y0KepgZw) | Cozy Flow Rel… | 763 | 139,267 | 182.5 | ×167.9 | 3,013.7 | 14.6분 | 2026-09-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 78/78 |
| 317 | [Happy Morning Jazz 🎶 January Bossa Nova Instrumental and Re…](https://www.youtube.com/watch?v=qZjNyrGF4pk) | FunToon Rhymes | 9,570 | 1,745,648 | 182.4 | ×88.5 | 124,615.6 | 15.4분 | 2026-10-06 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 0/0 |
| 318 | [Calm Work Music ∣ High Concentration Music for Studying, Fo…](https://www.youtube.com/watch?v=qXQ6wEipSug) | Calm Work Stu… | 5,770 | 1,031,195 | 178.7 | ×287.0 | 9,836.5 | 130.8분 | 2026-07-07 | 3. 공부·집중·작업 | 음악 | 설명 | 296/301 |
| 319 | [이수연, K-trot, [감성노래 탑7 메들리]](https://www.youtube.com/watch?v=wz-ZkvuAdTg) | 통기타 한석 TV | 2,620 | 467,922 | 178.6 | – | 2,846.6 | 26.3분 | 2026-05-08 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 없음 | 311/320 |
| 320 | [सुनते ही नींद आएगी 😴 ∣ दिव्य निद्रा संगीत ∣ Himalayan Deep …](https://www.youtube.com/watch?v=R_LBzRfzBBo) | Sanatan Bodh | 3,060 | 532,165 | 173.9 | ×1,081.6 | 5,287.5 | 40분 | 2026-07-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 157/158 |
| 321 | [안들으면후회함 playlist](https://www.youtube.com/watch?v=_eAnA8TgKWM) | 서른마흔오백다섯살 | 3,410 | 591,466 | 173.4 | ×43.4 | 4,296.2 | 24분 | 2026-06-04 | 기타 | 플레이리스트·모음 | 없음 | 169/169 |
| 322 | [Heartbreaking 💔 Lofi Mashup 🎧Slowed +Reverb Songs ∣ Study,F…](https://www.youtube.com/watch?v=mw6hxi9NJwc) | Peaceful Vibe… | 5,320 | 918,785 | 172.7 | ×4,101.7 | 15,854.4 | 7.3분 | 2026-08-23 | 3. 공부·집중·작업 | 음악 | 설명 | 105/105 |
| 323 | [눈 뜨면 아침인 숲속 평온한 빗소리 ∣ 🌲 깊은 수면을 위한 평온한 백색소음 (Rain Sounds for…](https://www.youtube.com/watch?v=ri10d9TXXGE) | Cozy Rain on … | 3,290 | 566,383 | 172.2 | ×125.3 | 5,849.1 | 210분 | 2026-07-15 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 127/134 |
| 324 | [ANDEAN PAN FLUTE 🌿 Gentle Healing Music to Calm the Mind l …](https://www.youtube.com/watch?v=1NjCSdhJnjo) | Ginevra Melod… | 186 | 31,948 | 171.8 | ×111.1 | 1,711.3 | 94.5분 | 2026-10-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 6/6 |
| 325 | [Zen Flute Therapy 🎶 ∣ Dopamine Reset Music for Stress & Anx…](https://www.youtube.com/watch?v=ldZHxztiahU) | Osen Moonlight | 10,100 | 1,697,504 | 168.1 | ×555.2 | 23,979.0 | 113.8분 | 2026-08-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 444/459 |
| 326 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 첫 비트부터 심박수 폭발 ❤️ 미친 텐션 운동 플리 ∣ 헬스 · 러닝 · EDM · 힙…](https://www.youtube.com/watch?v=XrUNOYMFd58) | Grind Vibe | 5,550 | 928,287 | 167.3 | ×134.4 | 7,087.9 | 80.7분 | 2026-06-11 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 337/340 |
| 327 | [Om Shanti Om - Climax BGM ∣ Cineforge Records](https://www.youtube.com/watch?v=eGnTmVPO--k) | Cineforge Rec… | 3,120 | 519,737 | 166.6 | ×59.4 | 3,589.1 | 9.8분 | 2026-05-28 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 111/112 |
| 328 | [Hindi Lofi Nights ∣ Yeh Tune Kya Kiya x Ishq Risk x Ishq x …](https://www.youtube.com/watch?v=oHrvGKhcW4s) | Songhalo | 11,000 | 1,831,161 | 166.5 | ×21.9 | 11,112.1 | 23.8분 | 2026-05-08 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 907/907 |
| 329 | [얼마나 들었는지 감도 안 옴](https://www.youtube.com/watch?v=1vELYr_nSxI) | shhh... | 6,860 | 1,140,977 | 166.3 | ×209.6 | 20,227.3 | 24.8분 | 2026-08-24 | 기타 | 음악 | 설명 | 169/174 |
| 330 | [Spa & Healing Music · 3 Hours 🌺 Luxury Relaxation for Massa…](https://www.youtube.com/watch?v=uzHIWyuadHM) | Halcyon Hours | 364 | 60,303 | 165.7 | ×942.2 | 533.3 | 180분 | 2026-06-29 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 5/5 |
| 331 | [살면서 한 번쯤 들어봐야 할 클래식 15곡 ∣ 공부·휴식·카페에서 듣기 좋은 클래식 음악](https://www.youtube.com/watch?v=hDepOWqLbXI) | canvasclassics | 183 | 30,239 | 165.2 | – | 254.5 | 152.1분 | 2026-06-23 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 3/3 |
| 332 | [새벽 2시~4시 재입면 음악 ∣ 생각 멈추고 다시 잠드는 BGM [중간광고없음]](https://www.youtube.com/watch?v=KBdCHv2UpRU) | 단잠TV | 2,510 | 411,588 | 164.0 | ×574.4 | 2,592.0 | 191.6분 | 2026-05-14 | 2. 자연 소리·백색소음 | 음악 | 설명 | 62/63 |
| 333 | [Playlist ∣ 어때 그 남잔 나보다 더 나?](https://www.youtube.com/watch?v=Eh4ZRMyh8vo) | 안개 | 3,200 | 524,009 | 163.8 | ×16.4 | 4,030.9 | 25.6분 | 2026-06-12 | 기타 | 플레이리스트·모음 | 설명 | 69/69 |
| 334 | [💃🔥𝐀 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐓𝐡𝐚𝐭 𝐖𝐢𝐥𝐥 𝐖𝐚𝐤𝐞 𝐔𝐩 𝐘𝐨𝐮𝐫 𝐈𝐧𝐧𝐞𝐫 𝐃𝐚𝐧𝐜𝐞𝐫 🎶⚡{+timest…](https://www.youtube.com/watch?v=ASY7vTTB-wo) | 𝙏𝙖𝙣𝙭 𝙀𝙙𝙞𝙩𝙯 🦋 | 13,200 | 2,157,957 | 163.5 | ×10.1 | 15,880.8 | 14.5분 | 2026-06-06 | 기타 | 플레이리스트·모음 | 설명 | 281/282 |
| 335 | [20 Of The Most Beautiful Classical Adagios for Relaxation a…](https://www.youtube.com/watch?v=t-scHKetq7I) | Classical Ins… | 13,700 | 2,234,578 | 163.1 | ×83.2 | 12,711.6 | 120분 | 2026-04-27 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 946/946 |
| 336 | [DIFFERENT ROAD - Melodic Viking Music for Focus & Deep Study](https://www.youtube.com/watch?v=pP54saekswg) | Jonas & Ida | 2,610 | 424,310 | 162.6 | ×104.6 | 4,330.9 | 6.5분 | 2026-07-14 | 3. 공부·집중·작업 | 음악 | 설명 | 87/87 |
| 337 | [99% DEEP SLEEP in 3 Minutes (NO ADS) • Brain Massage While …](https://www.youtube.com/watch?v=ZqzEQHOrvPw) | Awakened Soul | 5,060 | 815,048 | 161.1 | ×250.7 | 28,308.9 | 711분 | 2026-09-21 | 1. 수면·명상·힐링 | 음악 | 설명 | 439/460 |
| 338 | [A Few Minutes of Mahadev ∣ Feel His Presence Instantly ∣ Ga…](https://www.youtube.com/watch?v=hsGWmUi1TQc) | Sacred Vedic … | 10,800 | 1,737,436 | 160.9 | ×466.8 | 9,830.2 | 37.9분 | 2026-04-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 462/462 |
| 339 | [ENIGMA Style Music🔥Mystic River🔥2026](https://www.youtube.com/watch?v=5m7k60JKkLc) | VoiceLine Mus… | 4,020 | 644,723 | 160.4 | ×3,562.0 | 3,629.7 | 5.2분 | 2026-04-25 | 기타 | 음악 | 설명 | 199/199 |
| 340 | [[스페인 감성] "Hermano Sócrates ∣ 테스형 - 나훈아 " Korean OldPop 한국명곡](https://www.youtube.com/watch?v=FMwiMkgcfW8) | 스페인 감성 한국 올드송 | 1,420 | 226,803 | 159.7 | ×6.1 | 10,955.2 | 5.1분 | 2026-09-29 | 12. 커버·노래 부르기 | 음악 | 설명 | 68/69 |
| 341 | [Back To Chennai – Chennai Express Theme Music ∣ Shah Rukh K…](https://www.youtube.com/watch?v=g40bXb0KIFs) | Octave Valley | 1,360 | 217,185 | 159.7 | ×34.4 | 1,331.9 | 13.6분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 39/40 |
| 342 | [Relaxing Guzheng & Bamboo Flute 🌸Ancient Chinese Music 🌸 #a…](https://www.youtube.com/watch?v=N4y79JaFBeo) | Yuzira Music | 4,270 | 677,087 | 158.6 | ×2,976.2 | 4,345.1 | 64.1분 | 2026-05-17 | 기타 | 음악 | 설명 | 290/290 |
| 343 | [노래방차트 발라드 2026년 7월 1차 🎤 최신 인기차트 노래모음 ∣ 발라드 플레이리스트](https://www.youtube.com/watch?v=uedFUZ1kMjk) | 오늘의 음악 | 1,130 | 178,540 | 158.0 | ×419.1 | 2,659.8 | 83.2분 | 2026-08-14 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 8/8 |
| 344 | [#장터에핀작은꽃#인생트로트#감성트로트#눈물나는노래#가족사랑#엄마생각#할머니사랑#추억의노래#7080감성#중년…](https://www.youtube.com/watch?v=U-J6pNop1bU) | 인생 감성 트롯트노래 | 1,780 | 281,016 | 157.9 | ×498.3 | 2,729.5 | 4.8분 | 2026-07-09 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 18/18 |
| 345 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 도경수 느좋 노래 모음](https://www.youtube.com/watch?v=9GtuEDTdFus) | 오느레 | 112 | 17,641 | 157.5 | ×14.2 | 99.1 | 11.3분 | 2026-04-25 | 기타 | 플레이리스트·모음 | 없음 | 2/2 |
| 346 | [5 Minute Deep Meditation Music for Positive Energy • Relax …](https://www.youtube.com/watch?v=6-FPw2wSYsw) | Christmas Hav… | 289 | 45,007 | 155.7 | ×56.9 | 314.1 | 5.3분 | 2026-05-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 5/5 |
| 347 | [[기절수면/중간광고없음] 10분후 검은화면/ 듣자마자 잠드는 대나무숲 빗소리 🌧️잎 끝에 떨어지는 편안한 …](https://www.youtube.com/watch?v=l89z7BzLSmI) | 신가네숲 빗소리 | 1,350 | 208,645 | 154.6 | ×29.6 | 1,851.2 | 420분 | 2026-06-29 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 41/41 |
| 348 | [THE ULTIMATE HARYANVI PLAYLIST 🔥 !! #playlist #haryanvisong…](https://www.youtube.com/watch?v=SoVJljRBGMw) | 𐙚 𝒦𝒽𝓊𝓈𝒽𝒷𝓊𝓊 | 19,500 | 3,007,471 | 154.2 | ×5.9 | 27,064.3 | 6.9분 | 2026-07-01 | 기타 | 플레이리스트·모음 | 설명 | 305/306 |
| 349 | [[Playlist] ENHYPEN (엔하이픈)-'THE SIN : BLISS'丨2026 Full Album](https://www.youtube.com/watch?v=kG-CrsJXx5w) | κööκκ | 1,870 | 288,179 | 154.1 | ×56.3 | 4,816.4 | 15.9분 | 2026-08-21 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 240/241 |
| 350 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 야르한 제이팝](https://www.youtube.com/watch?v=3QaZldwEZ3g) | 탱이 | 1,680 | 258,668 | 154.0 | ×24.8 | 2,008.6 | 18.3분 | 2026-06-13 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 59/59 |
| 351 | [HEART BREAK 💔 SAD 😭 LOFI MASHUP ∣∣ HEART BROKEN 💔 HINDI SON…](https://www.youtube.com/watch?v=rXZRZ5z0Oqo) | Adnan Official | 10,000 | 1,533,872 | 153.4 | – | 11,175.8 | 18.8분 | 2026-06-05 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 107/107 |
| 352 | [[90 Phút Lạc Trong Không Gian Huyền Ảo] Mixset Chillout Hoà…](https://www.youtube.com/watch?v=5BxoSQw9tOo) | Bee Chill | 8,860 | 1,353,421 | 152.8 | ×12.9 | 18,550.7 | 92.3분 | 2026-08-08 | 8. 로파이·시티팝·칠 | 긴 한 곡·반복 | 설명 | 115/115 |
| 353 | [Könül Xasıyeva - Sən Məndən Xəbərsiz ∣ Piano Version by Xeq…](https://www.youtube.com/watch?v=ECMO19Ykny4) | Xeqan | 5,780 | 879,878 | 152.2 | ×20.9 | 5,312.5 | 6.1분 | 2026-05-07 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 379/379 |
| 354 | [SONGS THAT’LL MAKE YOU DANCE AT 3AM ✨🔥 FT. DESI SONGS ❤️‍🔥💋…](https://www.youtube.com/watch?v=oIXkjb_FPC4) | Dramanique⋆.𐙚… | 31,800 | 4,802,213 | 151.0 | ×10.2 | 30,224.6 | 29.3분 | 2026-05-14 | 기타 | 음악 | 설명 | 746/747 |
| 355 | [김동률 명곡 모음 🎵 베스트 발라드 20곡 연속듣기 ∣ 다시 사랑한다 말할까 · 감사 · 기억의 습작 ∣ …](https://www.youtube.com/watch?v=9kIULv7grWs) | 노래모음 | 2,130 | 319,169 | 149.8 | – | 2,328.5 | 75.3분 | 2026-06-05 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 49/49 |
| 356 | [Disney Sleep Piano Collection 🧜‍♀️ ∣ Ariel’s Peaceful Night…](https://www.youtube.com/watch?v=kPPtBzS0hbE) | Fairy Door | 1,830 | 273,962 | 149.7 | ×39.4 | 3,304.9 | 196.9분 | 2026-07-29 | 2. 자연 소리·백색소음 | 커버·직접 부른 노래 | 설명 | 26/26 |
| 357 | [바흐의 파사칼리아](https://www.youtube.com/watch?v=MQf3ajxEFfQ) | 홍준 뮤직 TV | 4,490 | 671,032 | 149.4 | ×1,232.4 | 5,034.4 | 40분 | 2026-06-09 | 기타 | 정보·해설 | 설명 | 662/668 |
| 358 | [playlist ∣ 우리 사랑은 필름 같았으면 해요](https://www.youtube.com/watch?v=k8giKQV4a40) | 웨일 | 3,400 | 505,137 | 148.6 | ×30.0 | 3,801.4 | 21.5분 | 2026-06-09 | 기타 | 플레이리스트·모음 | 없음 | 58/58 |
| 359 | [Relaxing Jazz Café in Paris ∣ Cozy Rainy Evening Jazz Ambie…](https://www.youtube.com/watch?v=3mNYh_27x5k) | European Jazz… | 1,240 | 183,782 | 148.2 | ×315.8 | 2,751.6 | 14.5분 | 2026-08-14 | 2. 자연 소리·백색소음 | 음악 | 설명 | 1/1 |
| 360 | [Peaceful Autumn Escape 🍂 Colorful Forest Scenery with Natur…](https://www.youtube.com/watch?v=kpm3m2Afk18) | Gentle Nature… | 5,840 | 862,013 | 147.6 | ×33.1 | 10,923.1 | 142.2분 | 2026-08-02 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 143/143 |
| 361 | [A CHATPATI PLAYLIST FOR CHATPATE PEOPLE 💅😜 #playlist #song …](https://www.youtube.com/watch?v=H0yLhDLJWuI) | 𐙚 𝒦𝒽𝓊𝓈𝒽𝒷𝓊𝓊 | 19,500 | 2,873,588 | 147.4 | ×5.6 | 27,410.0 | 11.2분 | 2026-07-07 | 기타 | 플레이리스트·모음 | 설명 | 300/302 |
| 362 | [Nhạc Thiền Tịnh Tâm An Lạc 🌿 Nhạc Thiền Chữa Lành Giúp Thư …](https://www.youtube.com/watch?v=I6stAluj1OI) | Hơi Thở Chánh… | 3,490 | 509,592 | 146.0 | ×535.8 | 2,865.4 | 64.3분 | 2026-04-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 119/119 |
| 363 | [Hanuman Chalisa 🔥 Listen Can Change Your Energy ∣ Peace, Po…](https://www.youtube.com/watch?v=v7ezfXE074I) | bhakti offici… | 4,960 | 720,945 | 145.3 | ×1,938.0 | 4,296.5 | 6.7분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 582/584 |
| 364 | [@노노뮤직#피아노연주곡 #플루트연주곡#명상음악 #휴식음악 #뉴에이지 #감성음악 #숲길 #자연음악 #마음치유…](https://www.youtube.com/watch?v=8Fiore1srWM) | 노노스튜디오 | 462 | 67,117 | 145.3 | ×409.2 | 483.0 | 32.1분 | 2026-06-03 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 11/11 |
| 365 | [Coffee Shop Love Songs ∣ Relaxing Acoustic 70s 80s 90s Coll…](https://www.youtube.com/watch?v=p4zynVVTYpA) | Acoustic Memo… | 10,000 | 1,452,043 | 145.2 | ×37.4 | 57,294.5 | 80.3분 | 2026-09-24 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 130/130 |
| 366 | [Sleep & Reset Your Vagus Nerve ∣ Singing Bowl Sound Bath Me…](https://www.youtube.com/watch?v=l91ztcnXYPM) | Echo Bowls | 504 | 73,044 | 144.9 | ×967.5 | 691.9 | 15.3분 | 2026-07-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 13/13 |
| 367 | [POV: You found the ultimate South Indian aesthetic🪷 playlis…](https://www.youtube.com/watch?v=oQz6Wt4qb3w) | Ethereal Echo… | 12,700 | 1,838,383 | 144.8 | ×5.8 | 12,411.2 | 13.3분 | 2026-05-25 | 기타 | 플레이리스트·모음 | 설명 | 356/357 |
| 368 | [Enigma - Eternity of Love (Enigmatic Ambient / New Age 4K)](https://www.youtube.com/watch?v=2ohn3S5VafQ) | 5TH FREQUENCY | 1,040 | 150,520 | 144.7 | ×176.5 | 2,281.8 | 5.4분 | 2026-08-15 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 60/60 |
| 369 | [𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 ∣ 일할때 틀어놓기 좋은 지브리 x 픽사 x 디즈니 재즈🔥🎺 ∣ #NoAImusic ∣ G…](https://www.youtube.com/watch?v=ayKr-gtJQIQ) | 오늘은 재즈데이 ∣ Ja… | 3,360 | 485,668 | 144.5 | ×434.6 | 3,613.2 | 379.1분 | 2026-06-07 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 40/41 |
| 370 | [If You Feel It in Your Blood… You’re a Viking ⚔️ ∣ Valhalla…](https://www.youtube.com/watch?v=uPK4MWJvxMk) | Viking Army | 9,580 | 1,384,664 | 144.5 | ×1,386.1 | 7,876.8 | 9.2분 | 2026-04-27 | 13. OST·사운드트랙 | 음악 | 설명 | 587/587 |
| 371 | [Good Morning Vibes 💕 Best Acoustic Love Songs to Start Your…](https://www.youtube.com/watch?v=fxrrC6UCItY) | NiceOne | 10,900 | 1,574,204 | 144.4 | ×871.2 | 23,705.7 | 91.9분 | 2026-08-14 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 | 146/143 |
| 372 | [Thankful Hearts ∣ Gratitude Sing Along Song with Lyrics 💗](https://www.youtube.com/watch?v=K-c4pzbzBzE) | Purely Positi… | 245 | 35,265 | 143.9 | ×218.4 | 630.7 | 4.5분 | 2026-08-25 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 21/25 |
| 373 | [【靜謐時光】 古箏竹笛療癒音樂｜超好聽的中國古典音樂 古箏、琵琶、竹笛、二胡｜療癒音樂 深度睡眠 - Chinese …](https://www.youtube.com/watch?v=7QV9JIx-euE) | Gentle Zen Me… | 9,590 | 1,379,032 | 143.8 | ×594.9 | 8,904.8 | 232분 | 2026-05-18 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,844/2,877 |
| 374 | [Calm Work Music ∣ Ambient Deep Work for Focus, Productivity…](https://www.youtube.com/watch?v=PBwiQgdwJdc) | Calm Work Stu… | 5,770 | 822,414 | 142.5 | ×228.9 | 7,770.9 | 130.2분 | 2026-07-06 | 3. 공부·집중·작업 | 음악 | 설명 | 202/203 |
| 375 | [Happy Morning Jazz 🎶 January Bossa Nova Instrumental and Re…](https://www.youtube.com/watch?v=cwBj4t1V_FY) | Little Masti … | 10,300 | 1,460,856 | 141.8 | ×16.2 | 70,056.1 | 14.5분 | 2026-09-29 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 0/0 |
| 376 | [𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 요즘 인스타 부계 감성](https://www.youtube.com/watch?v=WBabiGZluh8) | 알수없는 사용자 | 1,730 | 244,957 | 141.6 | ×6.8 | 3,277.5 | 17.5분 | 2026-08-06 | 기타 | 플레이리스트·모음 | 설명 | 52/53 |
| 377 | [Mind Relaxing Flute Tabla and Sitar ∣ Hindustani Instrument…](https://www.youtube.com/watch?v=ZHwM82TaZFg) | Mystic Sitar | 2,540 | 358,530 | 141.2 | ×190.9 | 2,099.0 | 71.2분 | 2026-05-02 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 87/87 |
| 378 | [Relaxing Jazz Saxophone instrument Relax & Slow Down 🌿 Soft…](https://www.youtube.com/watch?v=AaXKINtzSGI) | Peaceful Sax … | 13,800 | 1,942,813 | 140.8 | ×634.3 | 13,609.9 | 69.9분 | 2026-05-30 | 7. 재즈·보사노바 | 음악 | 설명 | 394/394 |
| 379 | [자비의 빛, 신묘장구대다라니](https://www.youtube.com/watch?v=oZyrd47zI6o) | 부다야나마하 | 2,860 | 402,359 | 140.7 | ×264.9 | 5,387.4 | 6.6분 | 2026-08-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 228/234 |
| 380 | [Eldorado — Hypnotic Dream Trance & Tribal Ambient Music👑✨](https://www.youtube.com/watch?v=ggbo8YTXRrw) | ARTechnoMusic | 3,810 | 535,523 | 140.6 | ×34.5 | 5,372.2 | 5.8분 | 2026-07-12 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 69/69 |
| 381 | [[오마주 OST] 모두가 자신의 무가치함과 싸우고 있다 Inspired Playlist ∣ 포켓라디오 #넷…](https://www.youtube.com/watch?v=CSIUAghSOPo) | pocketradio | 572 | 80,278 | 140.3 | ×256.5 | 452.5 | 16.3분 | 2026-04-25 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 93/93 |
| 382 | [মন ছুঁয়ে যাওয়া বাংলা Lo-Fi Romantic Songs ∣ Relaxing Bangla…](https://www.youtube.com/watch?v=rwiGXAhqrfU) | RESHMI LO-FI … | 24,000 | 3,356,414 | 139.8 | ×850.4 | 19,961.4 | 22.5분 | 2026-05-05 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 989/989 |
| 383 | [Le Café de Minuit 🇫🇷 Une Chanson Romantique Inspirée par le…](https://www.youtube.com/watch?v=D4-ltf3Tdh8) | Bistrot de Mi… | 3,400 | 474,999 | 139.7 | ×1,097.0 | 3,597.3 | 5.9분 | 2026-06-10 | 4. 카페·매장·라운지 | 음악 | 설명 | 101/102 |
| 384 | [[playlist] skrrrr….](https://www.youtube.com/watch?v=20mvF_OP0FY) | le | 12,300 | 1,711,567 | 139.2 | ×45.1 | 9,947.5 | 26.1분 | 2026-05-01 | 기타 | 플레이리스트·모음 | 없음 | 276/283 |
| 385 | [music that will get you to flowstate.](https://www.youtube.com/watch?v=72YoraTjNI0) | Pure Grit Stu… | 20,400 | 2,825,886 | 138.5 | ×124.2 | 28,401.0 | 145.4분 | 2026-07-12 | 기타 | 음악 | 설명 | 1,503/1,508 |
| 386 | [Positive Jazz Music ☕ Bossa Nova instrumental for Stress Re…](https://www.youtube.com/watch?v=T2HdICk7_6M) | Golden Roast … | 10,900 | 1,499,879 | 137.6 | ×1,227.9 | 10,868.7 | 71.2분 | 2026-06-04 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 235/239 |
| 387 | [Jo Tere Sang KaTi RaTe 💔 Lofi Remix ∣ Emotional Slowed + Re…](https://www.youtube.com/watch?v=XKcT9t0tgbY) | Abidpro | 46,100 | 6,343,090 | 137.6 | ×1,130.0 | 41,233.6 | 6.3분 | 2026-05-19 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 809/809 |
| 388 | [Deep Sleep & Chill Lofi : Bhojpuri Slowed & Reverb Songs 🎧✨…](https://www.youtube.com/watch?v=zW8T1B9Fzd0) | VLOGDIPESH | 5,220 | 716,901 | 137.3 | ×3,446.6 | 58,925.9 | 17.1분 | 2026-10-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 33/33 |
| 389 | [Fall Into Sleep Instantly • Healing Stress, Anxiety, and De…](https://www.youtube.com/watch?v=ZIGKQlrOEV0) | Brainwave Res… | 13,800 | 1,890,676 | 137.0 | ×2,938.1 | 13,167.8 | 480분 | 2026-05-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,028/1,034 |
| 390 | [বিধি এমন ভাগ্য কেন দিলা ∣ Bidhi Amon Vaggo Keno Dila ∣ Bang…](https://www.youtube.com/watch?v=PGkwfiSxmJU) | আঁখি Lo-Fi | 11,400 | 1,559,254 | 136.8 | ×251.1 | 15,798.0 | 13.8분 | 2026-07-13 | 기타 | 음악 | 설명 | 194/194 |
| 391 | [Midnight in Beirut 🌙 ∣ Lebanese Jazz & Oud Melodies for Rel…](https://www.youtube.com/watch?v=pdSDzQVDYXk) | Arabic Jazz L… | 17,600 | 2,401,767 | 136.5 | ×1,072.0 | 14,128.1 | 25.3분 | 2026-05-03 | 3. 공부·집중·작업 | 음악 | 설명 | 767/768 |
| 392 | [Shri Krishna Govind Hare Murari - Non Stop Krishna Bhajans …](https://www.youtube.com/watch?v=yl8by0hGZKE) | Hare Murare M… | 22,600 | 3,056,821 | 135.3 | ×1,001.3 | 21,315.9 | 59.2분 | 2026-05-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 419/419 |
| 393 | [[playlist] 내 주위는 온통 lovely day](https://www.youtube.com/watch?v=m-xuokRyfvQ) | 지륭 | 1,210 | 162,765 | 134.5 | ×3.8 | 992.0 | 19.9분 | 2026-05-09 | 기타 | 플레이리스트·모음 | 없음 | 20/20 |
| 394 | [Relax in Bikini Bottom 🛟 Calming Tropical Music 🌊 ∣ SpongeB…](https://www.youtube.com/watch?v=US8lFJPAWR0) | Vynture | 4,260 | 572,939 | 134.5 | ×428.0 | 6,465.6 | 249.3분 | 2026-07-23 | 1. 수면·명상·힐링 | 음악 | 설명 | 160/160 |
| 395 | [🎶Mind and body healing Music ∣ Bansuri flute + Esraj ∣ 1 ho…](https://www.youtube.com/watch?v=l1DL2JWYcyA) | Indian-Soulsc… | 279 | 37,500 | 134.4 | ×213.1 | 313.5 | 61.4분 | 2026-06-22 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 10/10 |
| 396 | [Autumn Morning Jazz In A Cozy Garden Lounge ∣ Gentle Piano …](https://www.youtube.com/watch?v=tiqZDLIBbHg) | Indoor Jazz M… | 5,400 | 720,838 | 133.5 | ×371.9 | 10,939.1 | 207.9분 | 2026-08-15 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 120/120 |
| 397 | [📝 1 HOUR OF FOCUS ∣ 🌧️ Relaxing Piano & Rain Sounds for Stu…](https://www.youtube.com/watch?v=yMcznSINsFs) | Melodies of C… | 4,500 | 600,667 | 133.5 | ×48.2 | 7,244.3 | 60.4분 | 2026-07-29 | 2. 자연 소리·백색소음 | 긴 한 곡·반복 | 설명 | 152/155 |
| 398 | [재생하자마자 텐션 터지는 2026 남녀돌 믹스업 (과제, 청소, 운동할 때 듣는 플리)](https://www.youtube.com/watch?v=x09m3Lgzc-A) | MxJin06 | 5,040 | 672,682 | 133.5 | ×10.2 | 8,305.8 | 99.2분 | 2026-07-31 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 없음 | 30/30 |
| 399 | [99% Fall Into Sleep Instantly (No Ads) • Eliminate Stress &…](https://www.youtube.com/watch?v=iVZPLhAlXUw) | Bedtime Calm … | 12,200 | 1,625,035 | 133.2 | ×258.5 | 32,746.4 | 237.9분 | 2026-08-31 | 1. 수면·명상·힐링 | 음악 | 설명 | 43/43 |
| 400 | [Bangla Old Is Gold Romantic Song ∣ Bangla Lo-Fi ∣ 1970-1990…](https://www.youtube.com/watch?v=OP2DddRRTKI) | Moner Tune | 24,300 | 3,218,669 | 132.5 | ×249.6 | 23,031.6 | 15.8분 | 2026-06-02 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 313/313 |
| 401 | [Classical Morning Energy - Relaxing, Uplifting Classical Mu…](https://www.youtube.com/watch?v=DPXTKDyBQEU) | Raaga Indian … | 6,900 | 912,940 | 132.3 | ×1,650.9 | 5,118.4 | 24.3분 | 2026-04-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 195/195 |
| 402 | [김상민 – YOU (2001) ∣ 폭발적인 고음의 여자 보컬 리메이크/커버 2 Keys+](https://www.youtube.com/watch?v=-GVdD_Onszw) | AuraAPT | 13,100 | 1,731,999 | 132.2 | ×99.5 | 20,408.5 | 4.1분 | 2026-07-27 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 269/284 |
| 403 | [Hanuman Chalisa for Deep Sleep ∣ Divine Protection for Peac…](https://www.youtube.com/watch?v=XKK7ewgprws) | Inner Bhakti | 7,180 | 947,799 | 132.0 | – | 10,001.2 | 114.8분 | 2026-07-17 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 156/158 |
| 404 | [choose peace](https://www.youtube.com/watch?v=eIY-Pgg-b1E) | sleepwalker | 14,200 | 1,873,757 | 131.9 | ×165.7 | 11,035.7 | 60분 | 2026-05-03 | 기타 | 긴 한 곡·반복 | 설명 | 1,135/1,141 |
| 405 | [Cortisol Reset । 432Hz Krishna Bansuri Therapy for a Calm M…](https://www.youtube.com/watch?v=D5NHvEVAbWY) | Healing Raga … | 23,700 | 3,113,886 | 131.4 | ×204.7 | 33,531.6 | 65.7분 | 2026-07-19 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,970/1,999 |
| 406 | [Playlist ∣ 틀어놓으면 그냥 계속 리듬 타게 되는 그루브 😎 집중 끊기지 않는 리듬 🎧 ∣ JAZZ…](https://www.youtube.com/watch?v=wsB8ej3Jon4) | Hush Chords | 19,500 | 2,560,566 | 131.3 | ×482.4 | 15,765.5 | 318.1분 | 2026-05-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 722/725 |
| 407 | [𝙿𝚕𝚊𝚢𝚕𝚒𝚜𝚝 중국 가오 노래들](https://www.youtube.com/watch?v=-h0dUUluarY) | 진구달려 | 5,710 | 748,833 | 131.1 | ×14.9 | 16,520.9 | 14.1분 | 2026-09-05 | 기타 | 플레이리스트·모음 | 없음 | 225/257 |
| 408 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 듣자마자 텐션 업🔥K-POP 여돌 노래 모음 노동요](https://www.youtube.com/watch?v=xtfreKB54KQ) | 클로버 플레이리스트 | 3,580 | 467,749 | 130.7 | ×6.2 | 4,159.3 | 53분 | 2026-06-29 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 39/39 |
| 409 | [Sholey Title Music ∣ Music Maker Abani ∣ Instrumental Cover](https://www.youtube.com/watch?v=ajRxp64xcN8) | MUSIC MAKER A… | 5,850 | 760,456 | 130.0 | – | 6,573.8 | 4.7분 | 2026-06-26 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 1,423/1,423 |
| 410 | [💖💖💖The Café by the Sea©](https://www.youtube.com/watch?v=7jPXHB9Ohus) | M's Music Lou… | 2,070 | 269,053 | 130.0 | ×706.2 | 2,190.6 | 4.2분 | 2026-06-19 | 4. 카페·매장·라운지 | 음악 | 설명 | 195/193 |
| 411 | [hard work pays off, let's be productive (focus playlist to …](https://www.youtube.com/watch?v=IS6yiMGlYkE) | taami study. | 9,660 | 1,254,169 | 129.8 | ×151.5 | 12,078.7 | 189.8분 | 2026-07-08 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 196/198 |
| 412 | [[空靈鼓療癒音樂🎶]｜放鬆、舒壓、冥想、安眠｜Steel Tongue Drum Healing Music｜SUNO…](https://www.youtube.com/watch?v=a_8Hi2u43Q4) | AIMF Music Fa… | 1,250 | 162,047 | 129.6 | ×958.9 | 1,224.9 | 93.1분 | 2026-06-10 | 1. 수면·명상·힐링 | AI 음악 | 설명 | 12/12 |
| 413 | [Deep Focus Music – Flow State for Study & Work](https://www.youtube.com/watch?v=9xYZzgG2EuI) | Deep365 | 4,180 | 538,915 | 128.9 | ×128.0 | 5,144.8 | 63.7분 | 2026-07-07 | 3. 공부·집중·작업 | 음악 | 설명 | 150/150 |
| 414 | [Awaken Your Power 🔱 Shiva Mantra Lofi](https://www.youtube.com/watch?v=Eq3mwBFjnec) | Lofi Shraddha… | 22,100 | 2,817,008 | 127.5 | ×496.4 | 15,710.1 | 85.1분 | 2026-04-24 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 2,878/2,878 |
| 415 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 비에 젖은 와인향](https://www.youtube.com/watch?v=Pt3nGKCTF2U) | 유월 | 3,770 | 479,340 | 127.2 | ×13.8 | 3,402.6 | 21.1분 | 2026-06-01 | 기타 | 플레이리스트·모음 | 설명 | 124/124 |
| 416 | [🎵 전체듣기 ∣ 에헤야~ 막걸리 한 잔 하세 🍶 ∣힐링 국악](https://www.youtube.com/watch?v=KYXF2WEd2Ew) | 에헤라디여 5060 | 357 | 44,809 | 125.5 | ×119.8 | 327.4 | 4.2분 | 2026-06-05 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 30/30 |
| 417 | [당신의 피아노 레벨은? (Lv.1~Lv.8 + 라캄파넬라) ∣ What is your Piano Level…](https://www.youtube.com/watch?v=1E5Zi3Gs1ys) | Bony_Musician | 674 | 84,463 | 125.3 | – | 620.8 | 6.5분 | 2026-06-06 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 340/340 |
| 418 | [Không Buông x Từng Là Của Nhau x Tìm Em - HNGLE x BẢO ANH ∣…](https://www.youtube.com/watch?v=wVLhvXB2flE) | Chà Là Chill | 38,900 | 4,869,045 | 125.2 | ×33.9 | 52,952.8 | 91.8분 | 2026-07-20 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 609/608 |
| 419 | [Happy Jazz Music ☕ Bossa Nova background for Relaxing, Grea…](https://www.youtube.com/watch?v=YTpDlQvvT3Q) | Golden Roast … | 10,900 | 1,354,226 | 124.2 | ×1,108.7 | 8,442.0 | 70.6분 | 2026-05-12 | 7. 재즈·보사노바 | 음악 | 설명 | 189/193 |
| 420 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 오늘 텐션 폭발🔥쌈뽕 노동요🕺🏻 출퇴근·운동용 Feel Good Groove Pop F…](https://www.youtube.com/watch?v=oyx0lS5I-TY) | melohour | 1,380 | 171,332 | 124.2 | ×145.6 | 954.9 | 622.8분 | 2026-04-23 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 30/31 |
| 421 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 그냥 네 눈동자가 예뻤어](https://www.youtube.com/watch?v=FOjiqNxjDDw) | 유월 | 3,770 | 466,094 | 123.6 | ×13.4 | 3,010.3 | 21.9분 | 2026-05-18 | 기타 | 플레이리스트·모음 | 설명 | 67/67 |
| 422 | [듣자 마자 바로 잠드는 숲속 시원한 빗소리 ASMR (Rain Sounds), 불면증 완화, 힐링 빗소리](https://www.youtube.com/watch?v=berSZ8YAKP8) | Cozy Rain on … | 3,290 | 404,572 | 123.0 | ×88.0 | 2,893.5 | 180분 | 2026-06-02 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 144/144 |
| 423 | [NAAD ∣ Powerful Instrumental Invocation #SpiritualMusic #Dr…](https://www.youtube.com/watch?v=bc4vTfxeLZk) | shivam sarasw… | 3,380 | 415,570 | 123.0 | ×1,505.7 | 2,900.7 | 7.9분 | 2026-05-30 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 60/60 |
| 424 | [TANGGAL STRESS MO DITO 🔥🎶 ∣ DUB REGGAE MIX 🎶🔥🇵🇭](https://www.youtube.com/watch?v=0m7BLfBl2f8) | RELAX REGGAE … | 13,800 | 1,691,396 | 122.6 | ×1,822.6 | 23,478.1 | 74.8분 | 2026-08-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 256/256 |
| 425 | [지금 다시 들어도 좋은 2000년대 명곡 모음 (SG워너비·티아라·씨야) 🎧 그 시절 우리가 사랑했던 노래…](https://www.youtube.com/watch?v=vBIWuORF8vI) | 그때 그 가락 | 2,450 | 298,744 | 121.9 | ×4.3 | 22,198.0 | 101.5분 | 2026-10-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 40/53 |
| 426 | [Without You Lord, I Am Nothing ∣ Inspirational Christian Wo…](https://www.youtube.com/watch?v=4TI0GkgfvKk) | Music of Faith | 28,000 | 3,407,891 | 121.7 | ×710.6 | 22,178.6 | 6분 | 2026-05-19 | 15. CCM·찬양·국악… | 음악 | 설명 | 2,138/2,138 |
| 427 | [Nhạc không lời Piano & Mưa Vol.1 ∣ Piano Thư Giãn, Học Bài,…](https://www.youtube.com/watch?v=tddKxQYCNlM) | Trí Nhật Piano | 8,640 | 1,037,374 | 120.1 | ×358.2 | 6,570.9 | 123분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 250/251 |
| 428 | [Sarap Sa Tenga To VOL. 3 🌿(IBA TO!) ∣ Spiritual Roots Regga…](https://www.youtube.com/watch?v=9w_QNH2ju3A) | Just Reggae S… | 45,800 | 5,423,189 | 118.4 | ×275.3 | 33,485.2 | 64.6분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,674/2,675 |
| 429 | [Dragon Ball GT Celtic Fantasy Music ∣ Relax Music for Focus…](https://www.youtube.com/watch?v=fJ6rnqkvyCk) | Medieval Echo… | 1,190 | 140,573 | 118.1 | ×551.3 | 795.4 | 9분 | 2026-04-26 | 3. 공부·집중·작업 | 음악 | 설명 | 202/202 |
| 430 | [Best Morning Powerful Mantras ∣ Shiva, Ganesh, Hanuman, Vis…](https://www.youtube.com/watch?v=CFV27iuas7Q) | Sacred Naad | 22,300 | 2,628,396 | 117.9 | ×3,236.9 | 39,059.9 | 15.7분 | 2026-08-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 973/972 |
| 431 | [쇼팽, 첼로로 물들다 ∣ 피아노와 첼로로 듣는 녹턴의 밤 (Chopin for Cello & Piano)](https://www.youtube.com/watch?v=HV7WBsQq-Ms) | EmberClassic | 4,830 | 569,336 | 117.9 | ×87.5 | 6,216.6 | 71.3분 | 2026-07-20 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 170/171 |
| 432 | [The Most Trending OPM Acoustic Songs on Spotify 2026 ✨ ∣ Vi…](https://www.youtube.com/watch?v=MbnaF3T2450) | Calm Guitar | 11,600 | 1,362,802 | 117.5 | ×66.0 | 19,365.0 | 63.8분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 121/123 |
| 433 | [⟨𝐜𝐚𝐟𝐞 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓⟩🩵맑은 초여름의 어느 날, 카페 피아노 10시간 [중간광고없음] ∣ 작업·공부·…](https://www.youtube.com/watch?v=nm_Mh-VIWvY) | Daily BGM plus | 1,350 | 157,888 | 117.0 | ×17.5 | 1,093.7 | 602.7분 | 2026-05-28 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 27/27 |
| 434 | [Dark Jazz Noir for Deep Focus, Work & Night Study ∣ Floatin…](https://www.youtube.com/watch?v=eFl7QIAYHHw) | What can I ge… | 12,600 | 1,468,269 | 116.5 | ×56.8 | 16,428.2 | 32분 | 2026-07-22 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 272/276 |
| 435 | [Relax Your Mind with Tabla & Bansuri Meditation Music ∣ Dee…](https://www.youtube.com/watch?v=OU-pcEjsoxs) | Raga Instrume… | 3,750 | 435,689 | 116.2 | ×2,672.9 | 2,692.3 | 93.3분 | 2026-05-11 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 138/138 |
| 436 | [My Soundscape for Sleeping at the Edge of the Universe](https://www.youtube.com/watch?v=fsxvm6W4EoY) | Polarity Ambi… | 8,820 | 1,020,891 | 115.8 | ×143.3 | 9,579.7 | 35.9분 | 2026-07-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 884/884 |
| 437 | [Dopamine Music 🎶 Peaceful Bansuri & Tabla Instrumental ∣ Me…](https://www.youtube.com/watch?v=6HPjmWDf0Q8) | KrishxBeats | 11,700 | 1,348,991 | 115.3 | ×672.5 | 18,556.2 | 27.9분 | 2026-08-08 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 646/654 |
| 438 | [{playlist} 할렐야루한 노래만 갖고옴...](https://www.youtube.com/watch?v=cnBMqI-z8q8) | 밤티플리 | 1,280 | 147,568 | 115.3 | ×27.3 | 1,033.4 | 18.8분 | 2026-05-30 | 기타 | 플레이리스트·모음 | 없음 | 30/30 |
| 439 | [【心整うBGM】聴くだけで疲れた一日がふっと和らぐ音楽✨｜心ほどけるピアノ２時間🌙｜作業,読書,睡眠用 / Sooth…](https://www.youtube.com/watch?v=-MEjaHzrcuU) | Kigokoro Café… | 6,480 | 737,430 | 113.8 | ×260.2 | 4,826.8 | 132.3분 | 2026-05-20 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 102/102 |
| 440 | [Greatest Classic Reggae Old Songs 70s-90s 🌴 RIVERS OF BABYL…](https://www.youtube.com/watch?v=1MPtYI4ExEo) | Zee | 11,600 | 1,313,539 | 113.2 | ×121.0 | 19,199.2 | 57.4분 | 2026-08-12 | 12. 커버·노래 부르기 | 플레이리스트·모음 | 설명 | 129/129 |
| 441 | [Music to Rest Your Mind.](https://www.youtube.com/watch?v=-igpcHqULS0) | dark serenity… | 6,690 | 753,883 | 112.7 | ×91.6 | 4,716.7 | 57.3분 | 2026-05-13 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 241/241 |
| 442 | [Kabhi Shaam Dhale ∣ Romantic Recreated Version ∣ Soulful Hi…](https://www.youtube.com/watch?v=jHw-Ivg2bLc) | Deepak Pandey | 39,000 | 4,314,672 | 110.6 | ×868.8 | 25,114.2 | 4.7분 | 2026-05-01 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 449/449 |
| 443 | [Painful - Emotional Cinematic Storytelling Music ∣ Orchestr…](https://www.youtube.com/watch?v=yk_jaCUz91M) | BynD Epic | 1,210 | 133,810 | 110.6 | ×71.1 | 971.6 | 4.9분 | 2026-06-04 | 13. OST·사운드트랙 | 음악 | 설명 | 64/64 |
| 444 | [🌸New Trending Acoustic Love Songs 2026 Cover🎧Best Trending …](https://www.youtube.com/watch?v=58xMPYKYcPg) | Calm Strings | 7,090 | 780,149 | 110.0 | ×59.6 | 8,632.4 | 49.7분 | 2026-07-21 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 103/103 |
| 445 | [나무에 내리는 부드러운 빗소리/ 듣자마자 기절수면 나무 빗소리/ 이명 치료 효과/ 빗소리 1시간/ 5분후 …](https://www.youtube.com/watch?v=otpGN7l-8mo) | 아늑한 빗소리 - Coz… | 4,200 | 460,754 | 109.7 | ×47.6 | 5,763.9 | 64분 | 2026-08-01 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 34/34 |
| 446 | [ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ](https://www.youtube.com/watch?v=MsjHOAq7WH0) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 14,700 | 1,610,394 | 109.5 | ×329.0 | 32,949.4 | 67.7분 | 2026-09-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,119/1,119 |
| 447 | [Tomay Pelam Elo Mone ∣ তোমায় পেলাম এলো মনে হাজার আলোর বন্য…](https://www.youtube.com/watch?v=rPi4ScyrzIM) | Sudip Lo-Fi M… | 20,100 | 2,201,565 | 109.5 | ×2,387.8 | 12,889.4 | 4.3분 | 2026-05-02 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 165/165 |
| 448 | [임영웅 콘서트 명곡 22곡 모음 💙 가장 사랑받는 감성 트로트·추억 발라드 연속듣기 #임영웅 #임영웅노래모…](https://www.youtube.com/watch?v=532qBV3Bs9o) | 별빛 영웅 뮤직 | 2,920 | 319,118 | 109.3 | ×1,619.9 | 2,863.1 | 75.3분 | 2026-06-30 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 113/114 |
| 449 | [[𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩]🔥달려보자 2010년 아이돌 띵곡 노동요 모음.zip 플레이리스트💿](https://www.youtube.com/watch?v=_zFB1047_Ek) | 이꿈치 | 1,330 | 144,673 | 108.8 | ×4.3 | 1,720.5 | 73.5분 | 2026-07-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 20/20 |
| 450 | [Darmiyaan - Unplugged](https://www.youtube.com/watch?v=f5vaem1fvGk) | Raghav Kaushi… | 9,810 | 1,063,738 | 108.4 | – | 12,269.6 | 5분 | 2026-07-25 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/29 |
| 451 | [🎻 바흐에게서 영감을 받은 바로크 듀엣 – 첼로와 오보에](https://www.youtube.com/watch?v=NxDxvXUWyFQ) | yoon acacia | 1,690 | 182,681 | 108.1 | ×306.5 | 2,321.0 | 69.7분 | 2026-08-02 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 35/35 |
| 452 | [💖신나게 미친(positive) 최신 걸그룹 노래 모음 ∣ 최신 여자아이돌 플레이리스트 [ Girl Gro…](https://www.youtube.com/watch?v=PiKPf0T7I84) | 띠잉뮤직 | 20,900 | 2,244,580 | 107.4 | ×189.5 | 13,408.8 | 120.5분 | 2026-05-05 | 기타 | 플레이리스트·모음 | 설명 | 270/270 |
| 453 | [Pokémon Café Jazz Lofi ∣ ☕ Smooth Beats for Study & Focus S…](https://www.youtube.com/watch?v=t6yrxjE7HSM) | Rest Point Lo… | 4,080 | 435,596 | 106.8 | ×71.5 | 2,532.8 | 104.2분 | 2026-05-01 | 3. 공부·집중·작업 | 음악 | 설명 | 74/74 |
| 454 | [Soft Acoustic Playlist 🎵 ∣ Best Relax & Chill Vibes Songs 2…](https://www.youtube.com/watch?v=MPT9v9MIod0) | Cozy Strings | 9,610 | 1,022,117 | 106.4 | ×313.0 | 6,687.8 | 69.8분 | 2026-05-20 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 84/84 |
| 455 | [🌧️ (No Ads) Real Heavy Rain & Powerful Thunderstorm ⛈️ ∣ De…](https://www.youtube.com/watch?v=tAd_vs_Ej_I) | Rain Drop's | 7,790 | 827,056 | 106.2 | ×22.0 | 10,037.7 | 95.1분 | 2026-07-29 | 2. 자연 소리·백색소음 | 음악 | 설명 | 287/284 |
| 456 | [99% DEEP SLEEP in 3 Minutes (NO ADS) • Relieves Stress • In…](https://www.youtube.com/watch?v=E0hQGUOAhrQ) | Fall Asleep S… | 9,540 | 1,008,974 | 105.8 | ×103.1 | 13,941.6 | 116.9분 | 2026-08-08 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 281/284 |
| 457 | [Sera Se Cosera - One Name (Extended) ∣ Jailer 2 BGM ∣ Super…](https://www.youtube.com/watch?v=0EcRBvWCmhQ) | JB RagaMix | 16,400 | 1,727,124 | 105.3 | ×21.5 | 16,133.8 | 5분 | 2026-07-05 | 기타 | 음악 | 설명 | 324/335 |
| 458 | [RUMI ∣ If You Want to Let Go of the Pain, Listen to This ∣ …](https://www.youtube.com/watch?v=p4VN5_1HW20) | Rumi Mystic S… | 1,440 | 150,939 | 104.8 | ×77.1 | 3,381.6 | 26.1분 | 2026-09-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 56/55 |
| 459 | [(BGM) 432Hz Ultimate Healing Music ∣ Alpha Wave for Body an…](https://www.youtube.com/watch?v=3odCe4Ry-EY) | Serenę Sound | 6,880 | 714,337 | 103.8 | ×582.7 | 4,476.3 | 73.5분 | 2026-05-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 228/228 |
| 460 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 라흐마니노프 - 지독한 슬픔 끝에 피어난 환희에 대하여ㅣRachmaninoff Style](https://www.youtube.com/watch?v=w5nhvxPli3E) | Moonlight Cla… | 8,360 | 865,394 | 103.5 | ×687.4 | 9,364.1 | 180분 | 2026-07-19 | 기타 | 플레이리스트·모음 | 설명 | 791/789 |
| 461 | [Quiet Night Playlist 🌙 ∣ Soft Love Songs for Deep Feelings …](https://www.youtube.com/watch?v=EvU4QgmjhMY) | Cozy Strings | 9,610 | 987,755 | 102.8 | ×302.5 | 7,218.7 | 134.1분 | 2026-06-05 | 기타 | 플레이리스트·모음 | 설명 | 162/165 |
| 462 | [옛날 시골집 슬레이트 빗소리ㅣ고향의 향수ㅣ추억ㅣ수면유도](https://www.youtube.com/watch?v=IHYnumQGS2o) | 빗소리 Healing S… | 1,350 | 138,708 | 102.8 | ×49.6 | 1,011.1 | 300분 | 2026-06-05 | 1. 수면·명상·힐링 | 자연 소리·백색소음 | 설명 | 47/47 |
| 463 | [Waheguru Jaap Before Sleep 🌙 Relaxing Meditation Kids, Babi…](https://www.youtube.com/watch?v=gT1SH3nqnuw) | Nanak Naam Ch… | 348 | 35,469 | 101.9 | – | 253.6 | 10.2분 | 2026-06-02 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 33/33 |
| 464 | [[Playlist] 조용히 혼자 듣고 싶다… 천상의 감성 보이스 7080 올드팝 🎧 ∣ 카페·휴식·감성 B…](https://www.youtube.com/watch?v=HBx4T1dadhI) | TrueOldies 70… | 5,550 | 564,867 | 101.8 | ×221.3 | 3,709.6 | 140.2분 | 2026-05-21 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 346/348 |
| 465 | [Summer Deep House Mix 2026 ∣ Luxury Chillout Lounge Music f…](https://www.youtube.com/watch?v=ZZjKsakgbgw) | Surfboard Dee… | 5,770 | 584,523 | 101.3 | ×503.5 | 3,827.8 | 65.2분 | 2026-05-20 | 4. 카페·매장·라운지 | 음악 | 설명 | 248/248 |
| 466 | [힐링음악 ∣ 쉬어 가도 괜찮아 (It’s Okay to Rest) ∣ 지친 마음을 쉬게 하는 국악 힙합 ∣…](https://www.youtube.com/watch?v=OTmG9c33c1M) | 풍그루 | 598 | 60,321 | 100.9 | ×19.8 | 717.3 | 5.1분 | 2026-07-28 | 1. 수면·명상·힐링 | 한 곡 | 설명 | 10/10 |
| 467 | [Romantic Instrumental Playlist 💖 ∣ Saxophone & Flute Love M…](https://www.youtube.com/watch?v=dHqp0WOzSns) | Video Music S… | 6,080 | 607,319 | 99.9 | ×27.5 | 6,201.1 | 13.3분 | 2026-07-14 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 34/34 |
| 468 | [Beautiful Sad Love Songs 2026 English Love Songs Playlist M…](https://www.youtube.com/watch?v=vKMy_Q_1wbc) | MusicLouds | 24,700 | 2,464,057 | 99.8 | ×1,716.5 | 14,613.0 | 71.4분 | 2026-05-04 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 870/869 |
| 469 | [Anirudh's new 2026 Mass songs ∣ Best Anirudh Songs #trending](https://www.youtube.com/watch?v=NV2bXZ4H4gA) | Musical Haven | 2,090 | 208,200 | 99.6 | – | 1,656.1 | 16.7분 | 2026-06-16 | 기타 | 음악 | 설명 | 15/15 |
| 470 | [​🎧 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 아무 걱정 없이 쉬고 싶은 날, 편안하고 아늑한 어쿠스틱 빈티지 재즈](https://www.youtube.com/watch?v=Py3IKxJcbAA) | MONA mood | 9,840 | 978,833 | 99.5 | ×40.7 | 9,381.8 | 84.4분 | 2026-07-08 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 94/95 |
| 471 | [[4K HDR Lofi ] Tokyo Night Drive Ginza Marunouchi Aoyama Sh…](https://www.youtube.com/watch?v=NRqZ5g1qEDQ) | Tokyo Vibes | 12,600 | 1,249,757 | 99.2 | ×186.4 | 6,972.2 | 95.8분 | 2026-04-24 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 525/525 |
| 472 | [If You Are Fall In Love Then Listen Romantic Indian Instrum…](https://www.youtube.com/watch?v=rCFoSTwT1GU) | Veena Meditat… | 2,390 | 236,458 | 98.9 | ×737.8 | 2,070.0 | 81.8분 | 2026-06-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 26/26 |
| 473 | [CHÌM VÀO GIẤC NGỦ SAY - Nhạc Lofi Chill Nhẹ Nhàng Thư Giãn …](https://www.youtube.com/watch?v=PJGgU7H4ruA) | Xóm Chill | 6,220 | 614,823 | 98.8 | ×143.0 | 8,331.9 | 156.2분 | 2026-08-07 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 82/82 |
| 474 | [[Playlist] 만약에 그날, 널 붙잡았다면│감성 발라드 플리](https://www.youtube.com/watch?v=KtjdGajPw_8) | 심야플리 | 2,310 | 227,711 | 98.6 | ×51.8 | 1,302.5 | 67.3분 | 2026-04-28 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 179/179 |
| 475 | [If You Feel Stressed, Listen to This ∣ Deep Sufi Healing Mu…](https://www.youtube.com/watch?v=tGNczX2LApU) | Rumi Mystic S… | 1,440 | 141,872 | 98.5 | ×72.5 | 3,351.3 | 30.2분 | 2026-09-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 25/25 |
| 476 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=ca4K-2vlfvA) | KKR rahul 09 | 16,000 | 1,574,386 | 98.4 | ×587.8 | 59,875.7 | 18.2분 | 2026-09-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 69/70 |
| 477 | [🌿 Возвращение к себе ∣ Музыка покоя 💦 Вода и тибетские чаши…](https://www.youtube.com/watch?v=eFje9j9VLZ0) | МУДРЫЕ МЕДИТА… | 6,810 | 663,742 | 97.5 | ×11.8 | 5,788.5 | 30.1분 | 2026-06-27 | 1. 수면·명상·힐링 | 음악 | 설명 | 162/162 |
| 478 | [Mere Mehboob Qayamat Hogi ✨ ∣ Slowed Reverb + LoFi ∣ Sad Hi…](https://www.youtube.com/watch?v=AHo0xW8RYTQ) | Abidpro | 46,100 | 4,475,814 | 97.1 | ×797.3 | 29,310.6 | 9.4분 | 2026-05-20 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 350/350 |
| 479 | [Classic Rock Songs 70's 80's 90's Playlist 🔥 Guns N Roses, …](https://www.youtube.com/watch?v=erfv9QasZAw) | 80s90s Rock R… | 21,800 | 2,112,805 | 96.9 | ×4,834.8 | 26,465.3 | 106.5분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 설명 | 171/178 |
| 480 | [Ganga Dharaye Shiv 🙏 ∣ Om Namah Shivaya ∣ Powerful Shiva Bh…](https://www.youtube.com/watch?v=FTzC_e5FQZA) | Spiritual Tun… | 29,200 | 2,789,404 | 95.5 | ×7,152.3 | 15,911.1 | 66.4분 | 2026-04-28 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 492/492 |
| 481 | [Dear God, Can You Hear Me ? - Ethereal Celtic ambient Track…](https://www.youtube.com/watch?v=7c2GwOr5NGc) | Dreamstatic E… | 4,120 | 393,180 | 95.4 | ×209.6 | 3,010.6 | 7분 | 2026-06-11 | 14. AI 음악 | AI 음악 | 설명 | 584/584 |
| 482 | [신나는 뽕짝·트로트 14곡 연속듣기 🎵 관광버스 필수곡 ∣ 신나는 뽕짝 메들리 ∣ 고속도로 트롯 BEST](https://www.youtube.com/watch?v=LxWOrfUcQlY) | 뽕친놈 | 4,710 | 446,707 | 94.8 | ×162.4 | 4,433.9 | 50.7분 | 2026-07-11 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 77/79 |
| 483 | [Playlist l 우리는 너무 어렸고 서툴렀다, 가사없는음악](https://www.youtube.com/watch?v=DN0T_nrFf6o) | Freemu 프리뮤 | 3,610 | 339,237 | 94.0 | ×876.6 | 5,237.5 | 60.2분 | 2026-08-16 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 56/59 |
| 484 | [회심곡(回心曲) - 쉬운 우리말로 풀어낸 한마음 회심곡, 불교음악, 부모은중경,부모은혜 ,인생무상 , 나무…](https://www.youtube.com/watch?v=0_QIhEcEiq0) | Dragonsong | 593 | 55,699 | 93.9 | ×55.3 | 925.6 | 7.5분 | 2026-08-21 | 기타 | 음악 | 설명 | 39/43 |
| 485 | [Vivaldi x Paganini x Bach Inspired 🎻 Fast & Relaxing Violin…](https://www.youtube.com/watch?v=0Jdy1C_QqvE) | Classical Vio… | 24,600 | 2,306,171 | 93.8 | ×2,888.1 | 15,764.2 | 74.7분 | 2026-05-27 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,656/1,673 |
| 486 | [Playlist ✍️집중력 1등 공부 플레이리스트 BGM ∣ 공부할때 듣기 좋은 음악🎧 focus&stud…](https://www.youtube.com/watch?v=wouMGz1k7K8) | obne music 오브… | 7,110 | 665,979 | 93.7 | ×91.3 | 11,515.5 | 122.1분 | 2026-08-23 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 49/54 |
| 487 | [#나는너를 - #장현 (1974년) Covered by sMUSIC #7080가요명곡 #리메이크명곡](https://www.youtube.com/watch?v=3F3vaZpv1ik) | sMusic 7080_명… | 6,860 | 640,244 | 93.3 | ×198.9 | 4,383.6 | 4.5분 | 2026-05-27 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 없음 | 80/80 |
| 488 | [Kur pata një lule t'bukur Alb Smooth Cover](https://www.youtube.com/watch?v=GES0QOroepY) | Alb Smooth Ca… | 4,990 | 464,266 | 93.0 | ×13.9 | 2,609.5 | 4.9분 | 2026-04-25 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 116/116 |
| 489 | [Silver Moon — Hypnotic Vocal Ambient (Enigma & Schiller Sty…](https://www.youtube.com/watch?v=hJd8GIUEOog) | ARTechnoMusic | 3,810 | 352,255 | 92.5 | ×22.7 | 3,128.7 | 6분 | 2026-06-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 114/114 |
| 490 | [All RED EVIL JACK MUSIC REJ儀式付【作業用/For work】](https://www.youtube.com/watch?v=_QAOzonmqh8) | イヴch🍳🥚 | 2,450 | 226,190 | 92.3 | – | 2,988.5 | 11.8분 | 2026-08-05 | 기타 | 음악 | 없음 | 132/132 |
| 491 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 틀자마자 시원해지는 당도보장 여름플리🩵(중간광고❌) Feel Good Chill Pop🎧카…](https://www.youtube.com/watch?v=t1i4n4SvtkE) | OurmuseMusic | 848 | 78,071 | 92.1 | ×24.0 | 622.5 | 607.7분 | 2026-06-16 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 68/68 |
| 492 | [Cheema Y Best Songs Playlist ∣ Punjabi Hits 2026 ∣ Jukebox …](https://www.youtube.com/watch?v=LFpVqIlmn00) | Radio Level L… | 37,900 | 3,475,020 | 91.7 | – | 30,742.1 | 27.9분 | 2026-06-29 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,003/1,032 |
| 493 | [🎧 2000s Nostalgia Mashup ∣ Tu Tu Hai Wahi (BGM) x Mujhse Mo…](https://www.youtube.com/watch?v=0K8bNaPHiWk) | VibesWithAni | 3,250 | 297,868 | 91.7 | ×4,137.1 | 5,067.7 | 6.5분 | 2026-08-22 | 기타 | 음악 | 설명 | 66/67 |
| 494 | [endless dream](https://www.youtube.com/watch?v=g33LSGLwLzo) | TaTa_Chan | 22,100 | 2,018,969 | 91.4 | ×268.7 | 14,551.2 | 165.3분 | 2026-06-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,317/2,373 |
| 495 | [Summer Café Bleu Lounge ∣ Luxury Originals](https://www.youtube.com/watch?v=_nmkwn2A8GI) | DeluxeChill | 7,030 | 640,815 | 91.2 | ×156.7 | 3,993.9 | 65.8분 | 2026-05-12 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 199/202 |
| 496 | [Healing Music for Anxiety, Fears and Depression 🌿 Heals the…](https://www.youtube.com/watch?v=AcfJRtYtSZU) | Nature Aura | 3,940 | 358,776 | 91.1 | ×288.4 | 5,528.5 | 105.2분 | 2026-08-16 | 1. 수면·명상·힐링 | 음악 | 설명 | 32/32 |
| 497 | [Sunrise Serenity ∣ Raag Ahir Bhairav inspired Music with bi…](https://www.youtube.com/watch?v=LLFxvwEOEGs) | Music for Life | 6,120 | 556,603 | 91.0 | ×346.4 | 4,084.2 | 40.2분 | 2026-06-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 259/259 |
| 498 | [PIANO INSTRUMENTAL PARA ORAR - TU FIDELIDAD - FONDO MUSICAL](https://www.youtube.com/watch?v=SADBZgzxwo0) | Sonido Del Ci… | 1,240 | 112,683 | 90.9 | ×150.6 | 639.3 | 14.4분 | 2026-04-27 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 5/5 |
| 499 | [Relaxing Meditation Music & Waterfall Sounds 🌿Calm, Deep Sl…](https://www.youtube.com/watch?v=gfulfnnJ3lY) | Celestial Rel… | 11,400 | 1,034,935 | 90.8 | ×318.2 | 19,565.7 | 126.5분 | 2026-08-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 116/117 |
| 500 | [Viral Chill Songs Playlist 2026🔥I MidnightVibes ∣ Non-Stop …](https://www.youtube.com/watch?v=SNx32obvuEk) | Viralics | 8,770 | 795,533 | 90.7 | ×76.1 | 5,059.7 | 17.1분 | 2026-05-16 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 116/116 |
| 501 | [Indian Instrumental Fusion Music 🎶 Flute, Tabla, Veena & Si…](https://www.youtube.com/watch?v=646h8c7sUSw) | FLUTE TABLA A… | 6,030 | 546,049 | 90.6 | ×522.5 | 3,738.7 | 18.1분 | 2026-05-27 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 153/154 |
| 502 | [Lullaby for Babies 💤 Sleep instantly in 3 minutes ♥ Sleep m…](https://www.youtube.com/watch?v=BUvu6tA9VTM) | Starfish and … | 7,970 | 717,154 | 90.0 | ×160.4 | 4,362.9 | 123.9분 | 2026-05-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 503 | [life](https://www.youtube.com/watch?v=8TjeO3AFTbM) | sleepwalker | 14,200 | 1,272,903 | 89.6 | ×112.5 | 8,022.0 | 60분 | 2026-05-14 | 기타 | 긴 한 곡·반복 | 설명 | 970/970 |
| 504 | [7 Pieces by Hans Zimmer \\ Iconic Soundtracks \\ Relaxing P…](https://www.youtube.com/watch?v=28vfE8VR2aE) | Yurii Salukha | 5,880 | 524,225 | 89.2 | ×399.3 | 7,883.1 | 33.3분 | 2026-08-14 | 13. OST·사운드트랙 | 음악 | 설명 | 57/59 |
| 505 | [Patar Bashori 🥀 ∣ পাতার বাঁশরী ∣ Female Version ∣ Bangla No…](https://www.youtube.com/watch?v=kQ3IwNRzLMM) | Lofix Dj Fusi… | 31,100 | 2,747,506 | 88.3 | ×2,517.2 | 33,937.5 | 18.4분 | 2026-07-31 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 976/976 |
| 506 | [BEST REGGAE RELAXING 2026 💕 ROMANTIC REGGAE LOVE SONGS 2026…](https://www.youtube.com/watch?v=vTSsC2D6EmQ) | OPM Chill Reg… | 15,300 | 1,349,661 | 88.2 | ×43.3 | 7,564.8 | 39.2분 | 2026-04-24 | 기타 | 음악 | 설명 | 1,965/1,965 |
| 507 | [the playlist to actually enter flowstate.](https://www.youtube.com/watch?v=wdDhTr_M7kA) | Pure Grit Stu… | 20,400 | 1,796,342 | 88.1 | ×86.4 | 34,880.7 | 123분 | 2026-08-29 | 기타 | 플레이리스트·모음 | 설명 | 545/545 |
| 508 | [🔥 JOSHHH BOOSTING BOLLYWOOD SONGS 🎧 ∣ Study Motivation Play…](https://www.youtube.com/watch?v=5BLt-lBa0gQ) | Echoess of un… | 6,140 | 539,186 | 87.8 | ×3.1 | 3,778.4 | 6.9분 | 2026-05-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 217/217 |
| 509 | [The Wild Theme (EXTENDED REMIX) ∣ OM First Strike ∣ Sai Abh…](https://www.youtube.com/watch?v=IoJerPi947U) | JB RagaMix | 16,400 | 1,438,716 | 87.7 | ×17.9 | 14,134.5 | 4.3분 | 2026-07-10 | 기타 | 음악 | 설명 | 214/216 |
| 510 | [Enya - Miracles (Official Music Video)](https://www.youtube.com/watch?v=9hNpytudWRo) | Alternate Pop | 19,300 | 1,686,739 | 87.4 | ×146.7 | 13,226.1 | 8.1분 | 2026-06-14 | 1. 수면·명상·힐링 | 한 곡 | 설명 | 836/840 |
| 511 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 😎 회사 생각 안나는 방법 찾았음 ⚡ 이 음악 재생 필수! Groove JazzHop ㅣC…](https://www.youtube.com/watch?v=Lv02AFsUrN8) | grooveonpli | 986 | 86,086 | 87.3 | ×92.1 | 588.0 | 372.4분 | 2026-05-26 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 73/73 |
| 512 | [Saxophone Instrumental Love Songs 🎷 Timeless Romantic Hits …](https://www.youtube.com/watch?v=y8IS36i_yOc) | MEMORIES PATH | 5,980 | 522,094 | 87.3 | ×412.4 | 5,507.5 | 56분 | 2026-07-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 109/109 |
| 513 | [🎧 Tanveer Evan: The Ultimate Love & Soulful Hits ∣ Emotiona…](https://www.youtube.com/watch?v=wHpNUy_W4GM) | Song Lyrics | 25,100 | 2,183,096 | 87.0 | ×175.2 | 15,810.6 | 23.6분 | 2026-06-04 | 기타 | 플레이리스트·모음 | 설명 | 890/890 |
| 514 | [The Calm After the Storm - Classical Music for Emotional He…](https://www.youtube.com/watch?v=AkVSmWxf6WA) | Reverie Class… | 8,340 | 718,209 | 86.1 | ×385.3 | 8,996.4 | 57.2분 | 2026-08-01 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 401/401 |
| 515 | [Soft Background Acoustic 🌿 Best Acoustic Covers Playlist 20…](https://www.youtube.com/watch?v=KoTsEko_7c8) | Afterhours Ac… | 15,400 | 1,305,209 | 84.8 | ×462.7 | 12,626.0 | 102분 | 2026-07-08 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 82/82 |
| 516 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 너도 지금 이 노래 듣고 있을까? 🤍 ∣ Chill R&B · 매장음악 · 카페 플레이리스트](https://www.youtube.com/watch?v=AM8WMi8_1cE) | mellomoodyy | 6,240 | 527,303 | 84.5 | ×147.7 | 5,790.3 | 90.1분 | 2026-07-21 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 185/185 |
| 517 | [腦子太吵時，先聽3分鐘｜2026最寧靜太極禪音精選｜讓呼吸慢下來，腦中的雜音也慢慢散去｜夜晚放空・晨間靜坐冥想・正念呼…](https://www.youtube.com/watch?v=KR1ZjmufbOE) | 清心樂坊Taiji Zen | 2,750 | 229,093 | 83.3 | ×34.1 | 3,253.4 | 59.3분 | 2026-08-10 | 기타 | 정보·해설 | 없음 | 24/24 |
| 518 | [싸이월드 감성 발라드 💿 그 시절 MP3에 꼭 있던 노래 ∣ 2000년대 발라드 명곡 모음 🎧 SG워너비,…](https://www.youtube.com/watch?v=5T42ApT_D-o) | 그때 그 가락 | 2,450 | 203,984 | 83.3 | ×2.9 | 7,167.9 | 105.1분 | 2026-09-21 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 16/17 |
| 519 | [Smoke Mood - Just Relax ∣ Chill House & Deep House Mix 🎧 Ch…](https://www.youtube.com/watch?v=SMsadBMPWQU) | ChillNight Me… | 23,400 | 1,946,026 | 83.2 | ×528.8 | 14,097.4 | 67.5분 | 2026-06-04 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 317/316 |
| 520 | [[playlist] 다신 사랑하지 않을 다짐](https://www.youtube.com/watch?v=xNrmomdWeqk) | le | 12,300 | 1,022,658 | 83.1 | ×26.9 | 5,957.7 | 25.4분 | 2026-05-01 | 기타 | 플레이리스트·모음 | 없음 | 655/666 |
| 521 | [🎧요즘 들은 플리 중에 제일 느낌 좋다… 느좋 감성힙합 Chill 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 🌙](https://www.youtube.com/watch?v=9iqkcoMV39k) | 𝐅𝐞𝐞𝐥𝐿𝐲𝐧 | 5,020 | 415,614 | 82.8 | ×46.7 | 2,918.3 | 70.3분 | 2026-05-30 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 281/281 |
| 522 | [듣는 순간 마음이 편안해지는 첼로와 오보에 🎻 ∣ 공부, 휴식, 감성 힐링 음악](https://www.youtube.com/watch?v=aha1_5ENidU) | 따뜻한 휴식 Studio | 1,990 | 164,722 | 82.8 | ×377.8 | 1,160.7 | 33.4분 | 2026-05-31 | 1. 수면·명상·힐링 | 음악 | 설명 | 100/100 |
| 523 | [if this background music found you, life will get better](https://www.youtube.com/watch?v=l3UmhyVCF90) | Ksu4000 | 22,600 | 1,864,521 | 82.5 | ×161.8 | 26,763.5 | 60.5분 | 2026-08-11 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 2,014/2,020 |
| 524 | [마음이 편안해져요, 가을 아침 클래식 ㅣ듣기만 해도 행복해지는 클래식 명곡](https://www.youtube.com/watch?v=XOiUmptBDVk) | Aria classic … | 2,510 | 206,843 | 82.4 | ×37.2 | 4,264.8 | 68분 | 2026-09-01 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 18/18 |
| 525 | [Smoke Mood - Just Relax ∣ Chill House & Deep House Mix 🎧 Ch…](https://www.youtube.com/watch?v=yEASFhtzSMQ) | Chill Night H… | 28,600 | 2,341,551 | 81.9 | ×5,382.9 | 13,320.1 | 68.7분 | 2026-04-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 317/323 |
| 526 | [Relaxing Classic Rock 2026 🎸 Greatest Soft Rock Hits for Dr…](https://www.youtube.com/watch?v=m1zUF6E51kw) | Enchoes Of Cl… | 16,800 | 1,357,885 | 80.8 | ×1,820.2 | 8,740.8 | 81.6분 | 2026-05-17 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 1,040/1,055 |
| 527 | [108 Hare Krishna Mahamantra Chants ∣ Harinam Kirtan for Pea…](https://www.youtube.com/watch?v=_AXkyLABNdw) | Pinakin Music | 10,400 | 836,045 | 80.4 | ×512.9 | 7,753.1 | 18.2분 | 2026-07-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 422/422 |
| 528 | [33 Koti Devi Devta हरेक विहानको मन्त्र ∣ हर हर महादेव ∣ जय …](https://www.youtube.com/watch?v=7fiSZtq8nHs) | Bhajan Hub Ne… | 33,400 | 2,681,491 | 80.3 | ×376.7 | 18,787.3 | 11.5분 | 2026-05-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,375/1,374 |
| 529 | [하루를 밝게 만드는 찬송가 모음 10곡 ∣ 기분 좋아지는 찬송가 모음 10곡 ∣ 어쿠스틱 기타 찬양 ∣ 듣…](https://www.youtube.com/watch?v=AOyN15yGFrs) | 주님곁에 | 18,700 | 1,498,963 | 80.2 | ×33.7 | 10,255.2 | 70.5분 | 2026-05-27 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 1,229/1,239 |
| 530 | [Mozart Style ∣ 아침 공기처럼 가볍게 흐르는 모차르트풍 스트링 앙상블 ✿중간광고 없음 ∣ 잔잔한…](https://www.youtube.com/watch?v=8SUfn18vz_U) | Lucerna Harmo… | 18,200 | 1,457,258 | 80.1 | ×201.5 | 12,165.0 | 132분 | 2026-06-22 | 4. 카페·매장·라운지 | 음악 | 설명 | 1,123/1,142 |
| 531 | [Peaceful Chill Playlist 🌙 Trending English Songs 2026 🎧 Bes…](https://www.youtube.com/watch?v=td6iCrK4MHc) | Morning Seren… | 15,600 | 1,234,151 | 79.1 | ×28.8 | 45,084.0 | 70.7분 | 2026-09-22 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 137/137 |
| 532 | [𝘠𝘰𝘶 𝘢𝘤𝘤𝘪𝘥𝘦𝘯𝘵𝘢𝘭𝘭𝘺 𝘧𝘦𝘭𝘭 𝘪𝘯 𝘭𝘰𝘷𝘦 𝘸𝘪𝘵𝘩 𝘚𝘰𝘶𝘵𝘩 𝘐𝘯𝘥𝘪𝘢𝘯 𝘴𝘰𝘯𝘨𝘴 (+ 𝘵𝘪…](https://www.youtube.com/watch?v=JgO5ly6YvGI) | 𝙏𝙪𝙭𝙡𝙞𝙥𝙨 🌷 | 41,600 | 3,290,020 | 79.1 | ×5.9 | 21,797.6 | 19.5분 | 2026-05-22 | 기타 | 음악 | 설명 | 950/954 |
| 533 | [10 Minutes Deep Meditation Music for Positive Energy • Free…](https://www.youtube.com/watch?v=PtUp1X2POmU) | TRUEMÖ Musics | 296 | 23,289 | 78.7 | ×439.4 | 1,385.2 | 10.1분 | 2026-10-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 1/1 |
| 534 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Study / Focus …](https://www.youtube.com/watch?v=aJsXjVL43xI) | Chill Vibes H… | 7,920 | 621,042 | 78.4 | ×3,943.1 | 9,241.1 | 8분 | 2026-08-14 | 3. 공부·집중·작업 | 음악 | 설명 | 65/65 |
| 535 | [영혼을 울리는 집시 바이올린 🎻 ∣ 감성 바이올린 · 집시 음악 · 휴식 플레이리스트 ∣ 보라빛 음악정원](https://www.youtube.com/watch?v=7xQeXJwhFh8) | 보랏빛 음악정원 | 174 | 13,589 | 78.1 | ×43.6 | 247.6 | 87.7분 | 2026-08-26 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 16/16 |
| 536 | [A K I R A - Floating High (original mix)](https://www.youtube.com/watch?v=cp_EDM8pS0Q) | AKIRA CLOUD | 7,870 | 614,173 | 78.0 | ×119.3 | 6,958.0 | 6.4분 | 2026-07-24 | 기타 | 음악 | 설명 | 122/122 |
| 537 | [요즘 이 노래에 빠졌다 🎧 중독성 리듬 락트로트 17곡 2시간 10분 연속듣기 ∣ I’m Addicted …](https://www.youtube.com/watch?v=rDvH1El0H3k) | 인생은 트로트 | 9,120 | 709,965 | 77.8 | ×48.5 | 16,170.8 | 130.3분 | 2026-09-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 338/338 |
| 538 | [Batman’s Solitude ∣ Dark Jazz Noir for Late Night Reflection](https://www.youtube.com/watch?v=s87k34ud3Kc) | Saturday Nigh… | 17,300 | 1,345,069 | 77.8 | ×119.5 | 8,416.4 | 60분 | 2026-05-13 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 590/591 |
| 539 | [মন ছুঁয়ে যাওয়া বাংলা Lo-Fi Romantic Songs _ Relaxing Bang…](https://www.youtube.com/watch?v=WX8EbRSHQYo) | Harano Kabita | 26,400 | 2,051,517 | 77.7 | ×451.6 | 28,607.8 | 17.6분 | 2026-08-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 255/251 |
| 540 | [Sitar for Dopamine Reset ∣ Indian Classical Music for Mindf…](https://www.youtube.com/watch?v=SEw8IsSXRSU) | Raga Focus | 37,500 | 2,898,355 | 77.3 | ×1,933.5 | 16,679.2 | 90분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,247/1,247 |
| 541 | [somehow this became your background music](https://www.youtube.com/watch?v=GTx1UYV9Y-o) | Ksu4000 | 22,600 | 1,745,927 | 77.2 | ×151.5 | 22,194.1 | 61.8분 | 2026-08-02 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 1,583/1,588 |
| 542 | [Do not listen to her music. She can hypnotise you in 4.49 m…](https://www.youtube.com/watch?v=0tBUIo44w-A) | Dream Weaver … | 18,900 | 1,457,093 | 77.1 | ×1,659.6 | 8,690.8 | 5.7분 | 2026-05-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 796/796 |
| 543 | [2 Hours Super Relaxing Baby Music ♥♥♥ Bedtime Lullaby For S…](https://www.youtube.com/watch?v=e_-uzFi6JlI) | Deep Calm Whi… | 31,500 | 2,418,963 | 76.8 | ×122.0 | 14,070.2 | 120.1분 | 2026-05-01 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 481/481 |
| 544 | [Positive Energy 2026 🌞 Feel Good Deep House Music for Morni…](https://www.youtube.com/watch?v=Dg9ePUDm4Vs) | ChillMorning … | 12,300 | 943,560 | 76.7 | ×277.3 | 6,604.1 | 65.7분 | 2026-05-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 331/331 |
| 545 | [jazz before i reach flow state](https://www.youtube.com/watch?v=fQIJb1h1RkA) | Defunct | 11,100 | 851,061 | 76.7 | ×189.3 | 5,319.1 | 127.8분 | 2026-05-13 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 944/946 |
| 546 | [MOOD OFF 💔Sad 😭 LOFI SONG MASHUP ∣∣ SAD HEART BROKEN 💔 MOOD…](https://www.youtube.com/watch?v=kjV1sVljycI) | Hindi sad son… | 41,700 | 3,195,857 | 76.6 | – | 20,200.5 | 19.6분 | 2026-05-15 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 330/330 |
| 547 | [【作業用BGM】名探偵コナン 夜ジャズメドレー☔️｜雨音とともに聴く Relaxing Jazz BGM](https://www.youtube.com/watch?v=ZoLpYGeZkn0) | Ken's Cafe&Ja… | 6,330 | 484,024 | 76.5 | ×21.9 | 3,044.8 | 167.6분 | 2026-05-14 | 7. 재즈·보사노바 | 음악 | 설명 | 175/174 |
| 548 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=p8BH-D_YiQY) | Sani Music Of… | 8,880 | 677,614 | 76.3 | ×820.4 | 7,512.3 | 8분 | 2026-07-22 | 3. 공부·집중·작업 | 음악 | 설명 | 53/53 |
| 549 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=WH_pNjVfkCY) | Click Bollywo… | 10,700 | 815,321 | 76.2 | ×6,909.5 | 8,500.6 | 8분 | 2026-07-16 | 3. 공부·집중·작업 | 음악 | 설명 | 118/118 |
| 550 | [𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 들으면 행복해지는 노래 모음 🫧 하루종일 듣기 좋은 팝송 플레이리스트](https://www.youtube.com/watch?v=lQrhgr4_dKg) | seroma room | 16,600 | 1,258,439 | 75.8 | ×132.6 | 7,434.5 | 542.2분 | 2026-05-04 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 167/169 |
| 551 | [TAI CHI MUSIC - Ancient Tao Healing ∣ Chinese Zen Music for…](https://www.youtube.com/watch?v=FDUj2q61rQ8) | Nebula Dreams | 6,080 | 460,758 | 75.8 | ×31.2 | 3,993.2 | 85.3분 | 2026-06-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 192/192 |
| 552 | [NIGHT PROTOCOL ∣ Dark Cyberpunk Music for Deep Work & Focus](https://www.youtube.com/watch?v=zXGb3k-A1Vo) | SoundFlow Lab | 8,950 | 678,241 | 75.8 | ×20.6 | 11,525.1 | 94.2분 | 2026-08-22 | 3. 공부·집중·작업 | 음악 | 설명 | 344/338 |
| 553 | [POV: YOU ARE A DESI BADDIE 💋😭 (PART-2) ✨ (+TIMESTAMPS) 😋 TH…](https://www.youtube.com/watch?v=9avHQt7MnK4) | Dramanique⋆.𐙚… | 31,800 | 2,406,302 | 75.7 | ×5.1 | 14,076.7 | 26.6분 | 2026-05-02 | 기타 | 정보·해설 | 설명 | 584/584 |
| 554 | [Melepasmu - Drive (Waktu Luang Version) ∣ Ambient Pop Melan…](https://www.youtube.com/watch?v=CfyEhCWn45o) | Waktu Luang | 18,700 | 1,410,324 | 75.4 | ×24.6 | 9,868.2 | 4.3분 | 2026-05-30 | 5. 운동·드라이브·신나는 | 커버·직접 부른 노래 | 설명 | 108/107 |
| 555 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=8vwZSZcOPtM) | Click Bollywo… | 10,700 | 806,060 | 75.3 | ×6,831.0 | 7,446.6 | 7.9분 | 2026-07-04 | 3. 공부·집중·작업 | 음악 | 설명 | 91/91 |
| 556 | [하츠투하츠 Hearts2Hearts 'RUDE!+Lemon Tang' 2026 한국대중음악상(KM Char…](https://www.youtube.com/watch?v=ddGnUiIjrgo) | poptforming | 5,870 | 441,699 | 75.2 | – | 5,088.8 | 6.6분 | 2026-07-25 | 기타 | 음악 | 없음 | 314/314 |
| 557 | [Heartbreaking 💔 songs + lofi Mashup songs Slowed Reverb son…](https://www.youtube.com/watch?v=u6gVi3TsKTM) | JR buzdar off… | 16,400 | 1,231,857 | 75.1 | ×3,450.6 | 15,152.4 | 7.8분 | 2026-07-31 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 53/51 |
| 558 | [Enya Inspired - Tears Of The Rain (Ai Music)](https://www.youtube.com/watch?v=ZqRhMKrbk58) | Sonic Beatz | 5,870 | 440,655 | 75.1 | ×102.8 | 2,891.1 | 7.5분 | 2026-05-20 | 14. AI 음악 | AI 음악 | 설명 | 412/411 |
| 559 | [Relajación Profunda, Claridad Mental 🌿 Reduce El Estrés Y L…](https://www.youtube.com/watch?v=j8hCioy51LU) | Healing Soul … | 10,700 | 802,123 | 75.0 | ×299.4 | 6,421.5 | 226.2분 | 2026-06-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 132/129 |
| 560 | [Afro House Mix 2026 🔥 Tribal Afro House Energy ∣ Emotional …](https://www.youtube.com/watch?v=UIzQAbsrlRk) | Jungle Pulse … | 27,000 | 2,019,190 | 74.8 | ×1,328.4 | 13,298.8 | 99.4분 | 2026-05-21 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 279/277 |
| 561 | [ENIGMA Style Music 🔥 Whisper of My Angel 🔥 2026](https://www.youtube.com/watch?v=ELv5bUhS-Qw) | VoiceLine Mus… | 4,020 | 299,347 | 74.5 | ×1,653.9 | 1,787.6 | 5.6분 | 2026-05-05 | 기타 | 음악 | 설명 | 95/95 |
| 562 | [15 Min Self Healing Music 🌿 Heal From Within & Find Inner P…](https://www.youtube.com/watch?v=wi3auWpIaZY) | Inner Healing… | 1,240 | 91,902 | 74.1 | ×62.0 | 2,150.8 | 16.5분 | 2026-09-07 | 1. 수면·명상·힐링 | 음악 | 설명 | 53/51 |
| 563 | [Life before Social Media - CHILL BRAZIL ∣ Samba, Luxury Bos…](https://www.youtube.com/watch?v=NHZXCzKGDQc) | Golden Smile | 6,570 | 485,842 | 74.0 | ×144.8 | 3,475.9 | 152.4분 | 2026-06-02 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 55/55 |
| 564 | [दिमाग को शांत करने वाला संगीत ∣ बांसुरी + संतूर + जलतरंग + …](https://www.youtube.com/watch?v=z6QYtZlFvb4) | Shanti univer… | 713 | 52,500 | 73.6 | ×164.6 | 419.8 | 14.6분 | 2026-06-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 17/17 |
| 565 | [모차르트에서 영감을 받은 아침 힐링 클래식 🌿 첼로 & 오보에 ∣ 평온한 산속 일출과 함께하는 휴식 음악](https://www.youtube.com/watch?v=tr3LEDt_p88) | Korean Rock B… | 4,750 | 348,991 | 73.5 | ×10.4 | 2,914.5 | 42.2분 | 2026-06-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 83/84 |
| 566 | [Ocean Chillout - Sunset Lounge Melodies and Luxury Lounge V…](https://www.youtube.com/watch?v=hFaOxrQmaQ4) | Afterglow Lou… | 10,700 | 785,897 | 73.5 | ×199.9 | 7,608.6 | 125.2분 | 2026-07-09 | 4. 카페·매장·라운지 | 음악 | 설명 | 231/231 |
| 567 | ["सुकून भरी रातें 🌙 ∣ Romantic Hindi LoFi Songs ∣ Relaxing S…](https://www.youtube.com/watch?v=DU0Swx5GKB4) | Hindi Tuning | 25,200 | 1,845,856 | 73.2 | ×255.9 | 71,976.3 | 104분 | 2026-09-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 61/61 |
| 568 | [Flora's Garden 🌸🌷✨ soft waltz piano for studying, reading &…](https://www.youtube.com/watch?v=J8Qi6W8t0Ek) | rumi. | 12,700 | 930,148 | 73.2 | ×285.2 | 6,820.5 | 251.5분 | 2026-06-05 | 3. 공부·집중·작업 | 음악 | 설명 | 467/468 |
| 569 | [My Heart And Soul ∣ Romantic Emotional Love Song ∣ Soft Emo…](https://www.youtube.com/watch?v=f2LgAVp301Q) | Soft Emotion … | 13,700 | 998,132 | 72.9 | ×105.7 | 7,585.6 | 5.8분 | 2026-06-10 | 기타 | 한 곡 | 설명 | 179/179 |
| 570 | [스튜디오 지브리 풍 클래식🍃 신비로운 정원에서 듣는 음악 ∣ 따뜻한 피아노와 플루트](https://www.youtube.com/watch?v=KIunwCFWDUE) | Little DoReMi | 4,200 | 304,048 | 72.4 | ×393.6 | 2,313.6 | 136.3분 | 2026-06-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 39/39 |
| 571 | [🎬 듣는 순간 지나온 세월이 생각나 울컥했습니다. 🎼 너무 많은 것들을 책임지며 살아온 당신을 위한 노래 …](https://www.youtube.com/watch?v=f9qBfvwQ9Ak) | 가슴을 울리는 락카페 | 10,900 | 785,129 | 72.0 | ×96.8 | 5,390.0 | 4분 | 2026-05-27 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 | 198/205 |
| 572 | [Morning Coffee Indie Folk – Warm Acoustic Music for Peacefu…](https://www.youtube.com/watch?v=wFy9kud8FHE) | Silver Coast | 28,700 | 2,063,605 | 71.9 | ×37.3 | 17,983.5 | 65.3분 | 2026-06-27 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 369/370 |
| 573 | [Lord Heal Me -Inspired By Enya (2026 Ai Music Video)](https://www.youtube.com/watch?v=Q-JjRkFbFhU) | SOUNDIASM | 10,700 | 768,538 | 71.8 | ×3,608.2 | 5,347.1 | 5.2분 | 2026-05-29 | 14. AI 음악 | AI 음악 | 설명 | 326/325 |
| 574 | [【星河入夢】 Ancient Chinese Healing Music 🎵 ∣ Qixi Star River 🌌 …](https://www.youtube.com/watch?v=pFttQ6MZ9d8) | Tianhe Harmony | 879 | 63,020 | 71.7 | ×152.4 | 693.5 | 77.8분 | 2026-07-21 | 1. 수면·명상·힐링 | 음악 | 설명 | 48/48 |
| 575 | [playlist l 틀자마자 집중 잘 되는 느좋 노동요 🎧 chill • r&b • vibes ☾](https://www.youtube.com/watch?v=ese2bIvjZGU) | luroom | 8,190 | 586,834 | 71.7 | ×73.9 | 10,318.9 | 248.2분 | 2026-08-24 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 175/179 |
| 576 | [Unlock Brain Power in 3 Minutes ∣ Classical Music for Focus…](https://www.youtube.com/watch?v=-zNMRToG5Vw) | Classical Mind | 22,600 | 1,613,419 | 71.4 | ×743.2 | 10,190.5 | 138.7분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 457/462 |
| 577 | [10 Most Powerful Morning Mantras ∣ Remove All Negativity ∣ …](https://www.youtube.com/watch?v=rH2JDVys2Os) | Adhyatmik Dhw… | 28,900 | 2,058,605 | 71.2 | ×1,472.5 | 13,879.2 | 20.7분 | 2026-05-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,753/1,753 |
| 578 | [Playlist ∣ 가을밤에는 남자발라드를 들어요 🍂 ∣ 한국 감성 발라드 모음 🔥](https://www.youtube.com/watch?v=iaEax89R7fQ) | 이짐땡 | 2,860 | 203,497 | 71.2 | ×19.4 | 6,151.1 | 167.7분 | 2026-09-17 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 8/8 |
| 579 | [Paris Night Chanson 🌙 1960s Vintage French Café Music (Roma…](https://www.youtube.com/watch?v=8LyppqPNDns) | AtelierChanson | 15,600 | 1,104,855 | 70.8 | ×921.1 | 6,318.0 | 23.9분 | 2026-04-28 | 4. 카페·매장·라운지 | 음악 | 설명 | 941/942 |
| 580 | [옛추억에 눈물나는 노래 '세월' #감성발라드 #감성가요](https://www.youtube.com/watch?v=zNbEjZxdswM) | 고구려TV🍒음악방송 | 4,140 | 292,497 | 70.7 | ×925.6 | 2,771.9 | 67.3분 | 2026-07-06 | 9. 가요·발라드·트로트 | 음악 | 설명 | 196/198 |
| 581 | [Музыкальная терапия🌿успокаивает нервную систему и освежает …](https://www.youtube.com/watch?v=iBs7kGH9KhA) | МЕЛОДИЯ ДЛЯ Д… | 15,600 | 1,097,842 | 70.4 | ×451.6 | 7,096.0 | 60.2분 | 2026-05-18 | 6. 피아노·클래식·연주곡 | 음악 | 없음 | 912/914 |
| 582 | [🎧 Relax & Enjoy Playlist ∣ Best Trending Pop Music Collecti…](https://www.youtube.com/watch?v=vDs2KPkfw8Q) | Morning Seren… | 15,600 | 1,094,907 | 70.2 | ×25.6 | 14,526.2 | 67.4분 | 2026-08-05 | 3. 공부·집중·작업 | 커버·직접 부른 노래 | 설명 | 126/118 |
| 583 | [soft pastel flowers 🌸🌷 relaxing piano for dreamy & peaceful…](https://www.youtube.com/watch?v=9NxQWqVtHRA) | She of the Va… | 11,700 | 809,603 | 69.2 | ×123.9 | 4,631.0 | 37.8분 | 2026-04-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 358/360 |
| 584 | [Groove Playlist ∣ ∣ Let your worries melt into the rhythm ∣…](https://www.youtube.com/watch?v=PjyT13hITqM) | DRDR | 13,800 | 943,348 | 68.4 | ×255.8 | 6,087.8 | 206.3분 | 2026-05-18 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 218/218 |
| 585 | [ㅤㅤㅤㅤㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤ](https://www.youtube.com/watch?v=UHHSdhBSfgQ) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 22,900 | 1,565,315 | 68.3 | ×277.2 | 19,940.4 | 93.6분 | 2026-08-02 | 기타 | 음악 | 설명 | 956/953 |
| 586 | [The Most Beautiful And Emotional Cinematic Adagio ∣ Cello &…](https://www.youtube.com/watch?v=6AKklMjtK8M) | CLASSICAL SPA… | 11,200 | 761,814 | 68.0 | ×513.4 | 4,870.2 | 61.9분 | 2026-05-16 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 981/969 |
| 587 | [Playlist 🎤 노래방 발라드 인기차트 & 애창곡](https://www.youtube.com/watch?v=4ZLxFva_K5I) | 필청 | 2,150 | 144,709 | 67.3 | ×15.7 | 974.7 | 165분 | 2026-05-24 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 20/20 |
| 588 | [[KPOP playlist] 마법처럼 빠져드는 케이팝 노동요](https://www.youtube.com/watch?v=uuZiS5xRAVw) | 오이는빼주세요 | 13,100 | 875,543 | 66.8 | ×66.5 | 5,513.8 | 59.7분 | 2026-05-14 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 70/70 |
| 589 | [Too Much on Your Mind? Stay Here for a While ∣ Arabic Oud A…](https://www.youtube.com/watch?v=uDCjW-9mE2k) | Sahara Echo M… | 14,100 | 937,657 | 66.5 | ×296.6 | 5,421.3 | 64.4분 | 2026-04-30 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 442/442 |
| 590 | [Deepest Sleep Healing - Release Melatonin, Calm Anxiety & S…](https://www.youtube.com/watch?v=J64B8xhHEbs) | Deep Sleep Ha… | 12,800 | 848,645 | 66.3 | ×424.6 | 7,021.6 | 225.4분 | 2026-06-21 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 232/234 |
| 591 | [𝐂𝐡𝐚𝐭𝐩𝐚𝐭𝐢 𝐇𝐨𝐧𝐞𝐲 𝐬𝐢𝐧𝐠𝐡 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐜𝐮𝐳 𝐲𝐨𝐮 𝐫𝐞𝐚𝐥𝐥𝐲 𝐧𝐞𝐞𝐝 𝐭𝐡𝐢𝐬. 𝐛𝐲 …](https://www.youtube.com/watch?v=eXNfz_Rs-KQ) | 𝐫𝐢𝐞 | 28,900 | 1,910,526 | 66.1 | ×840.7 | 12,675.3 | 14.8분 | 2026-05-22 | 기타 | 플레이리스트·모음 | 없음 | 211/212 |
| 592 | [하늘을 닮은 여름 🌸 여름 감성 피아노 플레이리스트 ∣ BGM ∣ 힐링·작업·집중](https://www.youtube.com/watch?v=Os2XdhfzZdo) | Mellow Season | 2,870 | 189,636 | 66.1 | ×23.9 | 1,987.5 | 120.9분 | 2026-07-16 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 31/31 |
| 593 | [a quiet playlist for a quiet heart (calm/relax piano)](https://www.youtube.com/watch?v=BBz7-F9mdUE) | Little Thing | 30,600 | 2,016,687 | 65.9 | ×181.8 | 13,542.4 | 89.5분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 314/315 |
| 594 | [Chinese Night Music: Soft Guzheng & Erhu ∣ Sleep Like Ancie…](https://www.youtube.com/watch?v=rw5yQGIQuwE) | Lotus Echo 莲之… | 16,500 | 1,086,178 | 65.8 | ×276.1 | 6,149.6 | 240.2분 | 2026-04-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 378/380 |
| 595 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Stu…](https://www.youtube.com/watch?v=Koo5Xgqn_zE) | Stylish Offic… | 15,000 | 985,453 | 65.7 | ×2,105.7 | 17,838.4 | 8분 | 2026-08-26 | 3. 공부·집중·작업 | 음악 | 설명 | 99/101 |
| 596 | [Clear Yourself of Everything That Drains You ∣ Calm Your Mi…](https://www.youtube.com/watch?v=Ww-tZVjkI9Y) | Frequencies o… | 46,400 | 3,045,115 | 65.6 | ×24.6 | 25,884.8 | 68.4분 | 2026-06-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,284/1,278 |
| 597 | [[Playlist] "아침에 듣기 좋은 산뜻한 클래식 왈츠" ∣ Summer Palace Waltz 🌿](https://www.youtube.com/watch?v=D2WezFoeswI) | okply | 15,500 | 1,008,196 | 65.0 | ×127.9 | 6,464.5 | 148.9분 | 2026-05-17 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 578/583 |
| 598 | [Deep Chill Mix 2026 🌌 Emotional House & Soulful Vibes for S…](https://www.youtube.com/watch?v=5FQsa5nWaW0) | Rhythm Flow | 23,700 | 1,538,700 | 64.9 | ×262.1 | 14,527.5 | 60.8분 | 2026-07-06 | 3. 공부·집중·작업 | 정보·해설 | 설명 | 323/317 |
| 599 | [😊 아침부터 기분 좋게 행복해지는 노래 모음 🎧 가볍게 흥얼거리는 기분 좋게 행복한 노래 모음](https://www.youtube.com/watch?v=r0jtXc1Y-jE) | 행복 | 7,010 | 454,307 | 64.8 | ×114.5 | 7,646.2 | 116.4분 | 2026-08-21 | 14. AI 음악 | AI 음악 | 설명 | 152/158 |
| 600 | [मोहे मोर बनइय्यो राधा ∣ Mohe Mor Banaiyo Radha Apne Vrindav…](https://www.youtube.com/watch?v=CPGQtKem4Cc) | Rangilo Gurja… | 25,000 | 1,619,371 | 64.8 | ×1,409.4 | 12,909.8 | 19.4분 | 2026-06-16 | 1. 수면·명상·힐링 | 음악 | 설명 | 375/375 |
| 601 | [샹송이 이렇게 까지 좋은줄 몰랐습니다. 아랑드롱이 사랑하던 멜로디가 아름다운 그 음악 ∣ Songs Tha…](https://www.youtube.com/watch?v=MHgCWNV-eKY) | Yesterday SOU… | 6,060 | 390,031 | 64.4 | ×765.5 | 2,485.3 | 43.9분 | 2026-05-16 | 기타 | 음악 | 설명 | 203/203 |
| 602 | [3小時宅家Lofi音樂合集｜累了，你只想宅在家裡｜超長版為一個人獨處而生的放鬆音樂，適合发呆或什么都不做](https://www.youtube.com/watch?v=kiClDrAsuqE) | SeaU Lofi | 14,200 | 910,162 | 64.1 | ×66.7 | 5,902.1 | 191.8분 | 2026-05-19 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 238/237 |
| 603 | [Richard Clayderman Tribute 🎹 ∣ Timeless Romantic Piano Music](https://www.youtube.com/watch?v=ZwlhZLzFxtk) | SONELIUM | 7,370 | 471,725 | 64.0 | ×1,218.9 | 6,591.3 | 29.4분 | 2026-08-09 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 178/179 |
| 604 | [मन को शांत करने वाली धुन ∣ राजयोग ध्यान की सहज विधि ∣ Brahm…](https://www.youtube.com/watch?v=ux3QNU3AaII) | Bhakti Naad | 771 | 49,293 | 63.9 | ×46.1 | 430.9 | 6.8분 | 2026-06-27 | 1. 수면·명상·힐링 | 음악 | 설명 | 27/27 |
| 605 | [Amélie ☕️ A Slow Weekend in Paris ∣ Piano Music for Relaxin…](https://www.youtube.com/watch?v=oToDtW7Gaas) | Peter Pan's L… | 5,950 | 380,237 | 63.9 | ×34.0 | 7,272.5 | 61.4분 | 2026-08-29 | 3. 공부·집중·작업 | 음악 | 설명 | 213/213 |
| 606 | [Put This On and Calm Your Brain... (No Ads)🌧️ Soft Piano Mu…](https://www.youtube.com/watch?v=vhJgRiH31bQ) | Cozy Attic Ni… | 5,880 | 375,779 | 63.9 | ×358.1 | 3,090.7 | 716.8분 | 2026-06-20 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 182/181 |
| 607 | [공부할 때 듣는 판타지 음악 ∣ playlist](https://www.youtube.com/watch?v=d8sLNlVAuxE) | Flow Trigger. | 6,540 | 417,052 | 63.8 | ×25.7 | 6,704.1 | 130.3분 | 2026-08-19 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 58/54 |
| 608 | [생각보다 좋게 풀리는 날 🎵마음에 초록빛을 채우는 힐링 피아노 ∣ 스트레스 해소 · 편안한 휴식 · 카페음…](https://www.youtube.com/watch?v=QC3xgG-dZJg) | Romua 로무아 | 3,370 | 214,789 | 63.7 | ×30.8 | 1,799.6 | 180.7분 | 2026-06-22 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 33/33 |
| 609 | [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 불교는 날 판단하지 않아 ∣ 불교 재즈 Playlist](https://www.youtube.com/watch?v=M4sdkiasFdA) | nuehaus | 6,090 | 386,300 | 63.4 | ×115.6 | 2,165.7 | 395.4분 | 2026-04-24 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 322/322 |
| 610 | [모든 일이 잘 풀리는 아침을 여는 음악 ∣ 막혔던 일이 시원하게 풀리는 기분](https://www.youtube.com/watch?v=6MQT5DkZTEU) | LazyFlow | 10,700 | 672,407 | 62.8 | ×119.1 | 3,992.5 | 90.4분 | 2026-05-04 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 167/168 |
| 611 | [Hyperfocus ∣ Lock In for 2 Hours ∣ Deep Work Study With Me …](https://www.youtube.com/watch?v=Rk0yG_dT0iI) | Work With Paul | 18,000 | 1,130,358 | 62.8 | ×7.6 | 16,602.7 | 111.4분 | 2026-08-13 | 3. 공부·집중·작업 | 긴 한 곡·반복 | 설명 | 138/138 |
| 612 | [🌙 Relaxing Gospel R&B Worship Music 2026 – Peaceful Midnigh…](https://www.youtube.com/watch?v=SKYFRvhTL4A) | Sacred worshi… | 13,200 | 827,976 | 62.7 | ×1,788.3 | 5,323.2 | 61.2분 | 2026-05-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 355/353 |
| 613 | [Ludovico Einaudi – 6 Piano Pieces ∣ Relaxing Music for Stud…](https://www.youtube.com/watch?v=nFJCWUpe2w4) | Yurii Salukha | 5,880 | 367,859 | 62.6 | ×280.2 | 4,743.1 | 29.7분 | 2026-08-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 54/54 |
| 614 | [Dark Jazz & Late Night Trip-Hop // Atmospheric Music for La…](https://www.youtube.com/watch?v=pGuvWU_1j-o) | Jazz Haze | 32,900 | 2,043,693 | 62.1 | ×825.4 | 12,795.6 | 94.2분 | 2026-05-13 | 5. 운동·드라이브·신나는 | 음악 | 없음 | 480/481 |
| 615 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 너도 나 좋아했으면 좋겠다](https://www.youtube.com/watch?v=4mAxMsNJAMI) | .happy | 228 | 14,140 | 62.0 | ×3.1 | 112.4 | 18.4분 | 2026-06-16 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 2/2 |
| 616 | [바흐와 모차르트의 감성을 담은 아침 클래식 🌿 하루를 여는 평화로운 힐링 연주](https://www.youtube.com/watch?v=9_HXWyP1MsE) | Korean Rock B… | 4,750 | 293,992 | 61.9 | ×8.8 | 3,047.9 | 40.3분 | 2026-07-15 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 40/42 |
| 617 | [빈예서 신곡 공개! 듣자마자 눈물 터졌다… “나훈아의 감성이 그대로” 😭🎵](https://www.youtube.com/watch?v=noMxR6lohxM) | 서울 뮤직 | 1,160 | 71,540 | 61.7 | ×84.4 | 5,868.0 | 6.9분 | 2026-10-08 | 기타 | 한 곡 | 설명 | 19/30 |
| 618 | [Dolce Vita 🇮🇹 Luxury Italian Lounge Music ∣ Elegant Café Ja…](https://www.youtube.com/watch?v=oiG7xIAgCFw) | ITALIAN MAFIA… | 14,300 | 876,710 | 61.3 | ×865.9 | 8,701.2 | 86.5분 | 2026-07-11 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 346/347 |
| 619 | [행운이 찾아오는 아침 🎵마음에 건강한 에너지를 채우는 힐링 피아노 ∣ 스트레스 해소 · 편안한 휴식 · 카…](https://www.youtube.com/watch?v=Xp2bSO5r5Os) | Romua 로무아 | 3,370 | 206,554 | 61.3 | ×29.6 | 1,548.9 | 180분 | 2026-06-08 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 37/37 |
| 620 | [7080 추억의 노래 광고없음🎶 7080노래모음 주옥같은노래 ✨7080 추억의 노래 한국인이 가장 좋아하는…](https://www.youtube.com/watch?v=3tshpfOljYs) | 7080 감성 선율 | 7,460 | 455,374 | 61.0 | ×15.6 | 11,540.8 | 118.6분 | 2026-09-10 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 63/66 |
| 621 | [우연히 들었는데..너무 좋은 찬양 🌱 희망의 봄 찬양모음 BEST 🌸 클래식 기타 찬양 연속듣기](https://www.youtube.com/watch?v=s1AkO_dWLp8) | 🎵 찬양의 시간속에 | 9,860 | 599,113 | 60.8 | ×359.4 | 3,357.2 | 65.7분 | 2026-04-24 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 796/796 |
| 622 | [15 Minute Meditation Music • Raise Your Vibration • Relax M…](https://www.youtube.com/watch?v=e8EVg-NJCng) | Soul Waves - … | 2,620 | 158,899 | 60.6 | ×180.3 | 924.7 | 15.4분 | 2026-05-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 16/16 |
| 623 | [Spiritual Temple Music ∣ 30 Minutes Stress Relief & Inner P…](https://www.youtube.com/watch?v=NF4gjQzGetw) | Shashwat Swar | 15,300 | 927,489 | 60.6 | ×77.8 | 6,450.6 | 34.2분 | 2026-05-29 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 146/145 |
| 624 | [2000년대 발라드 명곡 30곡 💿 그 시절 우리가 사랑했던 노래｜SG워너비·김동률·씨야·티아라·양파 ✔ …](https://www.youtube.com/watch?v=IZ6NgLQjStY) | 추억음악다방 | 3,430 | 207,609 | 60.5 | ×54.1 | 2,245.4 | 117.8분 | 2026-07-19 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 17/17 |
| 625 | [The Knight Who Chose Peace ⚔️ ∣ Relaxing Fantasy Music](https://www.youtube.com/watch?v=u8xCmb7KbA0) | Melody of the… | 14,000 | 846,232 | 60.5 | ×174.0 | 5,309.0 | 74.5분 | 2026-05-13 | 기타 | 음악 | 설명 | 516/518 |
| 626 | [달빛 아래 흐르는 색소폰 🌙 밤하늘의 멜로디 ∣ 숙면 음악 1시간 Vol.16](https://www.youtube.com/watch?v=7cZOU-bDgx8) | 고향 가는 나그네 | 2,670 | 160,890 | 60.3 | ×48.7 | 898.8 | 61.4분 | 2026-04-24 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 77/77 |
| 627 | [【異世界ケルト】路地裏で流れる安らぎのファンタジーBGM｜静かな街のかすかな余韻 [睡眠用BGM・リラックス用BGM・…](https://www.youtube.com/watch?v=w2XZiZpAYZg) | Roran Baron | 8,840 | 532,241 | 60.2 | ×51.5 | 3,197.7 | 182.9분 | 2026-05-06 | 기타 | 정보·해설 | 설명 | 261/261 |
| 628 | [【作業用BGM】ちいかわ Instrumental Jazz 2時間 ∣ 深夜のジャズラウンジ ∣ ひとりごつ, 島の…](https://www.youtube.com/watch?v=CJEgDVcFy80) | GINZA Midnight | 22,000 | 1,320,189 | 60.0 | ×50.9 | 24,004.9 | 126.6분 | 2026-08-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 324/330 |
| 629 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 세종대왕이 경복궁에서 야근하며 듣던 가야금 재즈](https://www.youtube.com/watch?v=q3oC3zdfyw4) | 조선재즈 | 9,970 | 597,548 | 59.9 | ×116.6 | 4,596.7 | 180.7분 | 2026-06-12 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 468/472 |
| 630 | [Your Productive Office Playlist 🤍 Soft Acoustic Covers to S…](https://www.youtube.com/watch?v=h2cVkEu99eI) | Afterhours Ac… | 15,400 | 921,309 | 59.8 | ×326.6 | 9,088.2 | 116.7분 | 2026-07-10 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 54/53 |
| 631 | [[스페인 감성] "Frente a Tu Casa ∣ 그집앞 - 이재성" Korean OldPop 한국명곡](https://www.youtube.com/watch?v=IXEpsuBWbg8) | 스페인 감성 한국 올드송 | 1,420 | 84,599 | 59.6 | ×2.3 | 1,235.5 | 4.5분 | 2026-08-12 | 12. 커버·노래 부르기 | 음악 | 설명 | 14/14 |
| 632 | [The Most Beautiful Rachmaninoff-Inspired Adagios ∣ Quiet Ce…](https://www.youtube.com/watch?v=ZdzITqD4vlM) | Adagio Melanc… | 9,930 | 591,463 | 59.6 | ×65.7 | 8,355.0 | 61.6분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,106/1,095 |
| 633 | [Bollywood+ Bhojpuri mix songs playlist (💗⚡💃🏻) ∣ @songplayli…](https://www.youtube.com/watch?v=sLPyIfOvPRQ) | xthetic._.vib… | 36,500 | 2,159,016 | 59.1 | – | 13,495.0 | 16.9분 | 2026-05-13 | 기타 | 플레이리스트·모음 | 설명 | 319/319 |
| 634 | [the best classical music for deep concentration ∣ string qu…](https://www.youtube.com/watch?v=Px1HC9ExXOk) | FocusSpace | 8,990 | 531,174 | 59.1 | ×91.5 | 5,979.5 | 64.6분 | 2026-07-23 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 444/443 |
| 635 | [[COVER] 한오백년 _ 어버이날을 맞이하여...](https://www.youtube.com/watch?v=W40yM35SfWc) | 감성메아리 | 5,320 | 313,812 | 59.0 | ×592.1 | 1,867.4 | 4.8분 | 2026-05-05 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 58/58 |
| 636 | [Fresh Mind Relaxing 💗 ∣ Slowed + Reverb Lofi Mix for Calm, …](https://www.youtube.com/watch?v=ACcuQVFbfnI) | Vansh Lofi | 29,200 | 1,716,916 | 58.8 | – | 13,704.3 | 16분 | 2026-06-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 88/88 |
| 637 | [나는 어디로 가나 - (국악 발라드)](https://www.youtube.com/watch?v=hd_rjKroAqM) | Rok Bi | 8,520 | 497,404 | 58.4 | ×53.9 | 3,109.6 | 5분 | 2026-05-13 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 203/205 |
| 638 | [途中広告なし[BGM]癒しの森カフェで何も考えない朝☕Gentle Morning Piano Jazz｜心地よく一日…](https://www.youtube.com/watch?v=qDJ8LG4noFk) | Aurora Tune | 19,200 | 1,119,741 | 58.3 | ×17.0 | 6,533.9 | 92.5분 | 2026-05-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 116/116 |
| 639 | [SAXOPHONE LOVE SONGS ❤️ Best Romantic Saxophone Music ∣ Bea…](https://www.youtube.com/watch?v=QpBzIwJPEoo) | Sax Chill Vib… | 27,700 | 1,611,613 | 58.2 | – | 23,960.9 | 57.6분 | 2026-08-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 225/227 |
| 640 | [Sade Morning Coffee ☕ Vol.3 ∣ Luxury ChillMix ∣ Soulful Jaz…](https://www.youtube.com/watch?v=mp4oA2JflBQ) | Setsukin | 43,100 | 2,489,355 | 57.8 | ×164.2 | 15,283.9 | 114.5분 | 2026-05-10 | 4. 카페·매장·라운지 | 음악 | 설명 | 780/783 |
| 641 | [처음부터 신나서 환장하는! ❤️ 신나는 트로트리믹스 고속도로메들리 ∣ 최신트로트 ∣ 트로트메들리 ∣ 감성트…](https://www.youtube.com/watch?v=zt45-jow7lo) | 다솜이의 트로트책방 | 7,710 | 444,228 | 57.6 | ×46.1 | 2,685.5 | 71.2분 | 2026-05-07 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 139/142 |
| 642 | [[중간광고없음] 🌿 잠시, 아무 생각도 하지 말아요. ∣ 숲속에서 듣는 잔잔한 피아노 ∣ BGM ∣ 휴식,…](https://www.youtube.com/watch?v=ebDKy0szHC8) | Riae & Piano | 12,400 | 714,333 | 57.6 | ×45.7 | 7,412.1 | 181.3분 | 2026-07-15 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 191/195 |
| 643 | [【眠れない夜のBGM】頭の中がうるさい夜に。考えすぎて眠れない夜のギターLofi｜睡眠・リラックス・深夜BGM ∣ s…](https://www.youtube.com/watch?v=IZRmwcM2974) | gentle night … | 14,000 | 806,371 | 57.6 | ×227.7 | 4,560.1 | 125.2분 | 2026-04-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 173/174 |
| 644 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 초여름 별사탕 𖤐ˊ˗](https://www.youtube.com/watch?v=aW-TYu5rwAY) | Horu | 3,550 | 204,296 | 57.5 | ×6.1 | 1,188.1 | 19.8분 | 2026-05-01 | 기타 | 플레이리스트·모음 | 없음 | 42/42 |
| 645 | [Gentle Rain Outside, Warm Piano Inside (No Ads) 🌧️ Helps Yo…](https://www.youtube.com/watch?v=G9iosi2cIh4) | Cozy Attic Ni… | 5,880 | 338,157 | 57.5 | ×322.2 | 3,003.6 | 717.9분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 178/178 |
| 646 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 교토의 작은 카페, 말차향 재즈 🍵🎧 抹茶オーツラテ](https://www.youtube.com/watch?v=vLX3-MrBXFk) | 아오링고 잡화점 AORI… | 10,500 | 598,466 | 57.0 | ×27.7 | 9,591.1 | 292.4분 | 2026-08-18 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 114/119 |
| 647 | [Rainy Day in the Treehouse:Cooking Beef Stew Bread Bowl & B…](https://www.youtube.com/watch?v=_Mugeu0ne3M) | Ghibli - ASMR… | 4,820 | 274,394 | 56.9 | ×976.5 | 1,541.5 | 6.5분 | 2026-04-25 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 71/71 |
| 648 | [50대이상이 들으면 정말 좋아할 노래 추천곡✨중년들이 사랑하는 겨울 노래 모음💕박인희/배따라기/여진/휘버스…](https://www.youtube.com/watch?v=TTkoF883bC8) | KTrot Melody | 10,100 | 573,366 | 56.8 | – | 7,038.8 | 126분 | 2026-07-30 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 103/103 |
| 649 | [Paganini (Vivaldi x Beethoven) House Music Mix – Hypnotic V…](https://www.youtube.com/watch?v=Q9TSg4bKjcs) | Velvet Freque… | 5,600 | 317,380 | 56.7 | ×320.6 | 1,989.2 | 7분 | 2026-05-13 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 212/212 |
| 650 | [비와 당신 (라디오스타 OST) - 가연이와 함께 듣는 비 오는 감성](https://www.youtube.com/watch?v=WmHI_XkpO2E) | GAYEON YOON | 28,600 | 1,619,240 | 56.6 | ×60.6 | 15,128.7 | 4.3분 | 2026-07-05 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 237/242 |
| 651 | [✨💖요즘 폼 미친(positive) 최신 아이돌 노래 모음 ∣ 신나는 ∣ 최신곡 ∣ 여돌 ∣ 남돌 ∣ 아이…](https://www.youtube.com/watch?v=eLiTRGAnmyk) | 띠잉뮤직 | 20,900 | 1,178,361 | 56.4 | ×99.5 | 8,005.7 | 121.8분 | 2026-05-26 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 162/162 |
| 652 | [[MIXSET] 늙크크의 여름 HipHop & R&B](https://www.youtube.com/watch?v=_o3psN6OCTk) | 떵신 tteongshin | 8,140 | 458,561 | 56.3 | – | 4,785.0 | 22.1분 | 2026-07-16 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 204/204 |
| 653 | [숲속에 내리는 잔잔한 빗소리 🌧️ 명상, 깊은 수면, 편안한 소리](https://www.youtube.com/watch?v=4Xl4kMOmGY8) | 숲 속 빗소리 | 1,800 | 100,425 | 55.8 | ×49.6 | 1,274.6 | 187.7분 | 2026-08-02 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 41/41 |
| 654 | [A Regular Day on the Journey ∣ Medieval Fantasy Music for D…](https://www.youtube.com/watch?v=TACRmufLfko) | Tales of Velm… | 17,700 | 984,807 | 55.6 | ×169.6 | 5,801.0 | 129.7분 | 2026-05-03 | 3. 공부·집중·작업 | 음악 | 설명 | 374/374 |
| 655 | [Dopamine Boost Music ∣ Flute, Sitar & Tabla for Positive En…](https://www.youtube.com/watch?v=kY7GcKagdjI) | CLASSICAL FUS… | 19,000 | 1,052,840 | 55.4 | ×205.1 | 8,335.2 | 27.8분 | 2026-06-16 | 3. 공부·집중·작업 | 음악 | 설명 | 717/719 |
| 656 | [background music.](https://www.youtube.com/watch?v=gOwbMN0JswA) | quiet please. | 34,900 | 1,929,199 | 55.3 | ×11.6 | 11,444.5 | 60분 | 2026-05-04 | 8. 로파이·시티팝·칠 | 음악 | 없음 | 205/205 |
| 657 | [첫 곡부터 너무 좋다 🍂 하루종일 듣게 되는 가을 올드팝 ∣ Vol.228 ∣ 7080 추억의 팝송 ∣ A…](https://www.youtube.com/watch?v=naLL7CGOC-8) | moka melody | 14,600 | 804,147 | 55.1 | ×42.2 | 13,099.3 | 367.3분 | 2026-08-19 | 4. 카페·매장·라운지 | 음악 | 설명 | 301/301 |
| 658 | [Heals You While You Sleep (No Ads) • Increases Deep Sleep •…](https://www.youtube.com/watch?v=f68XXr9BDYw) | Serene Dreams… | 16,600 | 909,507 | 54.8 | ×431.5 | 11,869.6 | 226.8분 | 2026-08-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 311/312 |
| 659 | [The Little Forest Concert Vol.2 ∣ Cozy String Quartet for R…](https://www.youtube.com/watch?v=0DvSj6DAKDM) | 그루잠 Gurujam | 27,400 | 1,498,430 | 54.7 | ×179.3 | 11,326.7 | 45.1분 | 2026-06-10 | 3. 공부·집중·작업 | 음악 | 설명 | 364/370 |
| 660 | [90년대 2000년대 락발라드 명곡 모음 🎧 남자라면 한 번쯤 울컥했던 추억의 감성 노래 ∣ 버즈, 김경호…](https://www.youtube.com/watch?v=oB4-QrY7Vcc) | 발라드 홈 / BALLA… | 10,200 | 556,150 | 54.5 | ×58.4 | 5,831.2 | 187.4분 | 2026-07-16 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 79/80 |
| 661 | [Krishna Mantra ∣ Pregnancy Music ∣ Music for pregnant women…](https://www.youtube.com/watch?v=TuMDXAiXlf0) | Be Listener M… | 18,500 | 1,008,373 | 54.5 | ×80.1 | 7,479.8 | 12.4분 | 2026-06-07 | 기타 | 음악 | 설명 | 384/385 |
| 662 | [a playlist to make your brain shut up](https://www.youtube.com/watch?v=xIX_A2PRoW0) | HIGHWIND | 40,200 | 2,188,541 | 54.4 | ×141.1 | 34,229.6 | 62.1분 | 2026-08-17 | 1. 수면·명상·힐링 | 연주 | 설명 | 811/782 |
| 663 | [PAMPATANGGAL STRESS 🌴NON-STOP PINOY DUB REGGAE 2026 ∣ Relax…](https://www.youtube.com/watch?v=m4vweFMrdzw) | Evo Reggae Mix | 19,000 | 1,031,900 | 54.3 | ×157.3 | 8,193.8 | 74.8분 | 2026-06-16 | 기타 | 정보·해설 | 설명 | 429/429 |
| 664 | [I’M COVERED NOT BROKEN ∣ R&B Gospel Soul Song (Healing, Str…](https://www.youtube.com/watch?v=H2lPB-NdhcM) | JESUS HEALS P… | 18,000 | 975,513 | 54.2 | ×868.7 | 5,495.9 | 4.2분 | 2026-04-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 580/580 |
| 665 | [(중간 광고 없음) 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 그때의 우린 왜 그리 서툴렀을까 ｜ 밤에 듣는 시린 첫사랑 발라드 …](https://www.youtube.com/watch?v=O-wm0ZSF2KU) | SonaWave | 12,300 | 663,314 | 53.9 | ×138.6 | 4,392.8 | 125.1분 | 2026-05-22 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 674/678 |
| 666 | [Chinese Zen Music🎵: Bamboo flute, erhu & Guzheng ∣ Relaxing…](https://www.youtube.com/watch?v=yGbaHLXUZWY) | ZenFlute | 32,700 | 1,746,963 | 53.4 | ×250.6 | 9,821.3 | 91.4분 | 2026-04-25 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,271/1,272 |
| 667 | [그 집 앞 (스페인어 버전 뮤직비디오) ∣ 이재성 원곡 라틴팝 리메이크 ∣ 한국어/스페인어 가사 자막 ∣ …](https://www.youtube.com/watch?v=T1fdlthH7Fw) | J.K.M | 37,500 | 2,000,361 | 53.3 | – | 13,071.6 | 4.2분 | 2026-05-20 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 설명 | 1,077/1,078 |
| 668 | [KUMAMICHI（熊道） — Japanese Zen Music Along the Bear’s Path](https://www.youtube.com/watch?v=vFJuk4U-V7Q) | Aether Journey | 34,200 | 1,824,386 | 53.3 | ×484.2 | 34,395.5 | 347분 | 2026-08-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 235/231 |
| 669 | [If You Can’t Sleep, Play This 🌙 Instant Deep Sleep Music & …](https://www.youtube.com/watch?v=PFn7jFxLbhE) | Deep Sleep Ha… | 12,800 | 681,819 | 53.3 | ×341.2 | 9,503.3 | 181.2분 | 2026-08-09 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 237/237 |
| 670 | [카페음악 ∣ 최고 다방 음악❤️ 카페에서 듣기 좋은 노래 ❤️ 50대-60대가 좋아하는 중년가요 ∣ 아침 …](https://www.youtube.com/watch?v=_h8CNlmPkjo) | Korean Cafe M… | 3,280 | 174,006 | 53.0 | ×2,949.3 | 1,212.9 | 10.8분 | 2026-05-29 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 22/22 |
| 671 | [HEAVEN-GIVEN VOICE ∣ Sad Love Songs ∣ soft rock ballad ∣ 슬픈…](https://www.youtube.com/watch?v=ySdeFYT0ohc) | Woori Sound | 13,000 | 688,947 | 53.0 | ×96.9 | 4,346.4 | 127.9분 | 2026-05-14 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 567/567 |
| 672 | [첫 곡부터 감성 미쳐버린🎧8090 레전드 플레이리스트](https://www.youtube.com/watch?v=i4uJ7c6b9gw) | Ceci Pop | 29,500 | 1,561,554 | 52.9 | ×103.4 | 11,454.2 | 112.8분 | 2026-06-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 1,362/1,363 |
| 673 | [[Playlist] 초록빛 향기 머무는 여름날과 어울리는 음악 ∣ 잔잔한 감성팝 카페음악 ∣ Healing…](https://www.youtube.com/watch?v=l3rA0WjsaNM) | 낡은 레코드 | 8,870 | 467,167 | 52.7 | ×46.6 | 3,108.4 | 77.9분 | 2026-05-23 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 71/71 |
| 674 | [1990~2026 한국 감성 발라드 명곡 100 🎵 마음을 울리는 인기 노래 모음 하루 종일 들어도 좋은 …](https://www.youtube.com/watch?v=l3FyvUQUgSA) | 바람의 발라드 | 21,000 | 1,104,139 | 52.6 | ×610.4 | 8,595.3 | 130.5분 | 2026-06-13 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 121/123 |
| 675 | [22 Beautiful Serenity Adagios That Will Touch Your Soul ∣ R…](https://www.youtube.com/watch?v=-kXB3QJb1Vs) | Silent Adagio | 11,400 | 598,493 | 52.5 | – | 3,941.8 | 120분 | 2026-05-21 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 297/297 |
| 676 | [여자력 상승하는 플리](https://www.youtube.com/watch?v=KSeIkQ_dpsg) | 무한우주에순간의빛일지라도 | 3,250 | 170,132 | 52.4 | ×10.1 | 3,642.5 | 15.4분 | 2026-09-03 | 기타 | 플레이리스트·모음 | 설명 | 12/13 |
| 677 | [😴 Baby Sleep Music That Works in 3 Minutes! 💤 Newborn Sleep…](https://www.youtube.com/watch?v=22SPWR7nyfM) | Mother & Baby… | 17,700 | 925,423 | 52.3 | ×24.4 | 7,732.6 | 122.7분 | 2026-06-22 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 678 | [Evergreen ghazal ∣ कभी फुर्सत मिले तो बैठ कर ये सोचता हूँ म…](https://www.youtube.com/watch?v=CiqRihLd68Q) | SOUL VIBES IN… | 30,000 | 1,555,898 | 51.9 | ×24.3 | 15,281.0 | 5.3분 | 2026-07-10 | 기타 | 음악 | 설명 | 298/297 |
| 679 | [[Masterpiece Series] Handel Passacaglia – The Eternal Bond …](https://www.youtube.com/watch?v=PF-v0MEo2AU) | WilliamPoetic… | 40,600 | 2,103,728 | 51.8 | ×176.3 | 11,803.5 | 17.8분 | 2026-04-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 3,222/3,224 |
| 680 | [🎧 Samz Vai: The Ultimate Sad & Emotional Hits 💔 ∣ Bengali L…](https://www.youtube.com/watch?v=kizXE5FXIFc) | Bangla Lofi 3… | 39,000 | 2,018,319 | 51.8 | ×72.8 | 22,989.9 | 26.9분 | 2026-07-24 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 239/237 |
| 681 | [2026년 6월 여돌 노래모음 ∣ 🔥 KPOP PLAYLIST](https://www.youtube.com/watch?v=a_19lS2wwOw) | 달플리 𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕 | 12,000 | 619,166 | 51.6 | ×38.0 | 4,414.7 | 64.9분 | 2026-06-02 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 53/53 |
| 682 | [7080 감성 포크송 ∣ 듣기 좋은 통기타 포크 15곡](https://www.youtube.com/watch?v=Hpsm6Kn5TM4) | ***7080가요산책*** | 4,730 | 244,043 | 51.6 | ×24.8 | 2,791.7 | 64.5분 | 2026-07-24 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 105/105 |
| 683 | [💚 초여름맛 메론소다 ☆・. ‘ . ꒰ 가사없는 집중 음악 ꒱](https://www.youtube.com/watch?v=FkmrHoP4xSk) | 둥실 ︵☆ | 1,190 | 61,149 | 51.4 | ×174.7 | 375.2 | 171.3분 | 2026-05-10 | 3. 공부·집중·작업 | 한 곡 | 설명 | 60/60 |
| 684 | [Piano Sleep Music with Relaxing Rain 🎶 Calm Your Mind, Reli…](https://www.youtube.com/watch?v=pFL8mgVoxnc) | Piano Rain Re… | 29,900 | 1,527,790 | 51.1 | ×109.0 | 17,287.6 | 203.6분 | 2026-07-23 | 1. 수면·명상·힐링 | 음악 | 설명 | 327/327 |
| 685 | [𝙋𝙇𝘼𝙔𝙇𝙄𝙎𝙏 찻집 리틀 포레스트](https://www.youtube.com/watch?v=9NAEMS-BJT0) | off frame | 3,300 | 167,762 | 50.8 | ×81.3 | 1,333.0 | 78.8분 | 2026-06-16 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 129/133 |
| 686 | [🎵 내려놓아라 ∣ 신나는 불교 EDM 트로트 ∣ 근심 걱정 다 내려놔라](https://www.youtube.com/watch?v=-y3mLSiAcU0) | 극락가요 | 393 | 19,877 | 50.6 | ×13.5 | 157.8 | 4.5분 | 2026-06-16 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 7/7 |
| 687 | [50대이상이 들으면 기분좋아지는 7080노래모음, 베스트 7080노래모음, 광고 없는 7080 좋은노래 모음](https://www.youtube.com/watch?v=L0rtQ0ZFr7o) | VibeTune | 11,400 | 576,558 | 50.6 | ×463.1 | 3,594.1 | 72.7분 | 2026-05-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 85/85 |
| 688 | [Fall Asleep In 3 Minutes 😴 Mozart For Babies 💤 Extra Relaxi…](https://www.youtube.com/watch?v=P87LUaYiD34) | Mother & Baby… | 17,700 | 894,817 | 50.5 | ×23.6 | 16,044.6 | 150.1분 | 2026-08-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 689 | [Elevate yourself - Bhagavad Gita ∣ Dark Trip-Hop X Downtemp…](https://www.youtube.com/watch?v=vrn7QzaHsbk) | SUR-SPIRITUAL | 7,910 | 398,879 | 50.4 | ×137.0 | 16,075.9 | 5.3분 | 2026-09-25 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 97/97 |
| 690 | [2 Hour Sitar for Clean Your Brain Instantly ∣ Indian Classi…](https://www.youtube.com/watch?v=PVGFHGLRjK4) | Sacred Mind H… | 8,290 | 417,540 | 50.4 | ×299.3 | 2,402.9 | 120.4분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 206/206 |
| 691 | [[감동음악]🎵듣는 순간 가슴이 먹먹해진다… 김호중 × 이애숙 《나의 조국은》 감동 실황 ∣ 천상의 목소리 …](https://www.youtube.com/watch?v=FAMrq6SXxys) | 🎧 Sound Rest | 2,710 | 135,857 | 50.1 | ×463.7 | 838.7 | 4.5분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 612/613 |
| 692 | [Ithaca](https://www.youtube.com/watch?v=8DVfI_Muv_A) | Ludwig Görans… | 43,300 | 2,169,396 | 50.1 | ×4.5 | 22,617.6 | 5.7분 | 2026-07-16 | 13. OST·사운드트랙 | 음악 | 설명 | 0/796 |
| 693 | [(No Ads) Relaxing Music For Deep Sleep • Anxiety Relief, Me…](https://www.youtube.com/watch?v=UhQANX3rKzA) | Bedtime Calm … | 12,200 | 609,824 | 50.0 | ×95.6 | 3,868.5 | 94.3분 | 2026-05-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 68/69 |
| 694 | [Deep work focus music for productivity ~ Ambient study musi…](https://www.youtube.com/watch?v=Bk-0NZHRPFA) | Work Mode Aud… | 11,100 | 552,593 | 49.8 | ×106.6 | 4,113.7 | 91분 | 2026-06-08 | 3. 공부·집중·작업 | 음악 | 설명 | 254/256 |
| 695 | [Morning Coffee & Relaxing Italian Music ∣ Mediterranean Vib…](https://www.youtube.com/watch?v=Uu_fZV9xXRM) | Onda di Relax | 25,900 | 1,261,879 | 48.7 | ×474.0 | 7,127.6 | 141.2분 | 2026-04-26 | 4. 카페·매장·라운지 | 음악 | 설명 | 141/141 |
| 696 | [Beautiful September Autumn Forest 4K 🍁 Peaceful Nature Soun…](https://www.youtube.com/watch?v=RJma4cwfqIY) | Nature's Have… | 2,730 | 132,230 | 48.4 | ×32.9 | 3,394.2 | 154.8분 | 2026-09-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 49/49 |
| 697 | [𝗽𝗹𝗮𝘆𝗹𝗶𝘀𝘁🎧"이번 주말은 집이 아니라 오션뷰 카페입니다" ∣ 여유를 200% 충전하는 주말 아침 플레…](https://www.youtube.com/watch?v=ayGgFCSVB30) | velvetvoice | 7,010 | 339,000 | 48.4 | ×58.5 | 1,900.3 | 53.9분 | 2026-04-24 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 250/250 |
| 698 | [“사는 게 힘들수록, 그 시절 노래가 더 그립습니다…”｜가슴 저리는 7080 추억의 명곡모음｜슬로우 블루스…](https://www.youtube.com/watch?v=uS61Sf1rAsQ) | 추억의 멜로디 | 4,300 | 207,809 | 48.3 | ×20.8 | 2,991.9 | 85.9분 | 2026-08-11 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 84/86 |
| 699 | [𝑃𝑙𝑎𝑦𝑙𝑖𝑠𝑡 느좋 도우인 플리](https://www.youtube.com/watch?v=muaiYrT3glM) | 진구달려 | 5,710 | 275,729 | 48.3 | ×5.5 | 3,533.9 | 14.7분 | 2026-08-03 | 기타 | 플레이리스트·모음 | 없음 | 52/55 |
| 700 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=3k0BBE7e6TA) | Z B Official … | 21,200 | 1,018,821 | 48.1 | ×4,695.0 | 13,934.4 | 8분 | 2026-08-08 | 3. 공부·집중·작업 | 음악 | 설명 | 75/73 |
| 701 | [【Playlist】Shamisen Rock You’ll Want to Replay ∣ Female Voca…](https://www.youtube.com/watch?v=skyHiOHKUJI) | Geisha Girl | 15,200 | 729,613 | 48.0 | ×61.8 | 4,421.9 | 111.1분 | 2026-05-08 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 193/193 |
| 702 | [9 Adagios in Romantic Style ∣ AI Music ∣ Cello & Piano](https://www.youtube.com/watch?v=N4UaovHvFPE) | Vesper Classi… | 16,400 | 785,138 | 47.9 | ×1,215.4 | 4,676.9 | 28분 | 2026-05-05 | 14. AI 음악 | AI 음악 | 설명 | 421/421 |
| 703 | [ᴘʟᴀʏʟɪsᴛ ∣ 🌊푸른 바다처럼 시원한 7월 여돌 뮤직비디오 플리 ∣ 여름 청량 최신 걸그룹 인기곡 뮤…](https://www.youtube.com/watch?v=2EbdnZvOSwc) | 마쁠(MA-PLE·KPO… | 24,800 | 1,186,577 | 47.9 | ×7.3 | 13,045.3 | 127.2분 | 2026-07-21 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 84/84 |
| 704 | [[KPOP playlist] 난리도 아닌 감다살 케이팝 노동요](https://www.youtube.com/watch?v=AnsLD0Klc6s) | 오이는빼주세요 | 13,100 | 624,377 | 47.7 | ×47.5 | 4,773.9 | 59.1분 | 2026-06-11 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 47/47 |
| 705 | [업장을 소멸하고 복을 부르는 천수경 노래 ∣ 힐링 불교 음악](https://www.youtube.com/watch?v=AT2MDa7WctU) | 진서연의 세월한곡 | 9,450 | 448,162 | 47.4 | ×1,297.1 | 2,526.6 | 14.1분 | 2026-04-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 391/393 |
| 706 | [Romantic Era Adagios (Cello, Violin & Piano) — Most Beautif…](https://www.youtube.com/watch?v=Dd3djaUS3Fw) | Classical Ada… | 13,100 | 620,759 | 47.4 | ×1,412.4 | 4,029.8 | 256.8분 | 2026-05-19 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 187/187 |
| 707 | [Cinematic Piano Meets Melodic Techno 🌌 ∣ Neo Classic Pulse …](https://www.youtube.com/watch?v=gSn_K5j9uB8) | Neo Classic P… | 4,720 | 222,052 | 47.0 | ×69.1 | 2,714.4 | 45.2분 | 2026-07-30 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 166/166 |
| 708 | [Bamboo Water + Tibetan Zen Sounds ∣ Cleanse Aura & Space ∣ …](https://www.youtube.com/watch?v=oA7EmuZ7JCU) | Serene Vibes | 15,700 | 737,542 | 47.0 | ×79.0 | 4,585.8 | 184.3분 | 2026-05-12 | 1. 수면·명상·힐링 | 음악 | 설명 | 204/204 |
| 709 | [조용히 틀어뒀는데 끝까지 듣게 되는 노래 ㅣ오늘 고생한 당신을 위한 편안한 올드팝 라디오 ㅣ 7080 감성…](https://www.youtube.com/watch?v=ej-ck75-Nps) | Plain Pop | 4,250 | 199,584 | 47.0 | ×44.7 | 1,345.1 | 85.2분 | 2026-05-24 | 9. 가요·발라드·트로트 | 음악 | 설명 | 156/156 |
| 710 | [카페음악 ☕ 5월의 카페에서 잔잔하게 듣기 좋은 음악 🌿 7080 카페음악모음 🎶 중년을 위한 감성 카페 …](https://www.youtube.com/watch?v=5-b-PY1I2ss) | Cozy Cafe Mus… | 3,870 | 180,351 | 46.6 | ×22.0 | 1,070.9 | 12.8분 | 2026-05-04 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 19/19 |
| 711 | [𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩 ∣ 상큼하게 톡 터지는 딸기 에이드와 느린 독서 *'~*-⋆._.-*~⋆ ∣ 카페 플리 ∣…](https://www.youtube.com/watch?v=L1E4rkvGo-Y) | BlueDot Diary | 6,520 | 303,784 | 46.6 | ×109.4 | 2,691.1 | 123.4분 | 2026-06-29 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 75/75 |
| 712 | [듣다 보면 끝까지 듣게 되는 명품 보컬 ∣ 7080 슬로우 레게・레트로 락발라드・Love Song・Vint…](https://www.youtube.com/watch?v=V9FOduIEv6w) | afterparis | 7,200 | 334,354 | 46.4 | ×25.4 | 3,055.8 | 82.8분 | 2026-07-02 | 9. 가요·발라드·트로트 | 음악 | 설명 | 183/183 |
| 713 | [[playlist] 상큼 달콤 행복의 피아노 음악🍋 아이의 정서발달을 위한 멜로디🎹 행복해지는 마법같은 영…](https://www.youtube.com/watch?v=PxIbP-Lv3EQ) | 베베집 bebe zip | 8,240 | 380,914 | 46.2 | ×51.9 | 3,418.8 | 91분 | 2026-06-30 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 0/0 |
| 714 | ["सुकून भरी रातें 🌙 ∣ Romantic Hindi LoFi Songs ∣ Relaxing S…](https://www.youtube.com/watch?v=YtyLIn9mrcw) | Hindi Tuning | 25,200 | 1,164,083 | 46.2 | ×156.7 | 7,376.4 | 110분 | 2026-05-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 160/158 |
| 715 | [LiL Baby - Work For Money ( Official Music Video)](https://www.youtube.com/watch?v=3FclEMAiJ6Q) | Vibes World R… | 225 | 10,375 | 46.1 | ×6.2 | 218.4 | 7분 | 2026-09-02 | 기타 | 한 곡 | 설명 | 3/3 |
| 716 | [비 오는 밤의 라흐마니노프 ∣ 깊고 잔잔한 아다지오 1시간](https://www.youtube.com/watch?v=HNgBqMnvUcU) | Minimal Class… | 7,640 | 352,271 | 46.1 | ×43.3 | 2,448.3 | 60.2분 | 2026-05-29 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 341/341 |
| 717 | [Lightning — Romantic Ambient Pop & 80s Synth Ballad ∣ Thoma…](https://www.youtube.com/watch?v=2x_gLGrUdoY) | Thomas J. Cole | 4,040 | 186,137 | 46.1 | ×75.4 | 6,936.8 | 5분 | 2026-09-23 | 12. 커버·노래 부르기 | 음악 | 설명 | 94/94 |
| 718 | [💖 최고의 트로트 명곡 30곡 ∣ 중장년 애창곡 ∣ 운전·카페·휴식 음악 ∣ 안동역에서 미운사랑 홍시 진또…](https://www.youtube.com/watch?v=Tbtq8pWkeEk) | 달빛머문 새벽세시 | 1,040 | 47,884 | 46.0 | – | 1,925.8 | 98.2분 | 2026-09-25 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 6/6 |
| 719 | [途中広告なし【カフェBGM】ひとり静かな喫茶店｜のんびり過ごす午後の時間｜作業用・読書・リラックス｜Cafe Musi…](https://www.youtube.com/watch?v=QgtDgADXHS4) | Kokoro Music … | 21,100 | 968,888 | 45.9 | ×47.0 | 8,281.1 | 120.9분 | 2026-06-25 | 2. 자연 소리·백색소음 | 음악 | 설명 | 166/166 |
| 720 | [마음이 편안해지는 명품 아침 클래식 ㅣ듣기만 해도 행복해지는 클래식 명곡](https://www.youtube.com/watch?v=jhz1rDyH7gc) | Aria classic … | 2,510 | 114,334 | 45.5 | ×20.6 | 1,263.9 | 59.4분 | 2026-07-21 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 18/18 |
| 721 | [마음도 휴식이 필요해요 BGM (플루트 연주) 🎵 조용한 숲과 호수의 휴식](https://www.youtube.com/watch?v=pzBSdxT3Bp4) | 느린풍경이야기 | 1,060 | 47,769 | 45.1 | ×876.5 | 321.2 | 39.6분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 21/21 |
| 722 | [🎵듣는 순간 소름… 김호중·허종훈·임경택·임창한 남성4중창 레전드 공연 ∣ 김호중의 폭발적 테너… ‘오 나…](https://www.youtube.com/watch?v=ypW1MoCFDA8) | 🎧 Sound Rest | 2,710 | 121,289 | 44.8 | ×414.0 | 815.1 | 13.9분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 182/183 |
| 723 | [𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 듣자마자 행복해질거야🍦☀️ 요즘 감성 노래 모음 ∣ 하루 종일 듣기 좋은 팝송 플레이리스트](https://www.youtube.com/watch?v=4zc4GyIQPco) | seroma room | 16,600 | 742,836 | 44.8 | ×78.3 | 5,657.9 | 599.4분 | 2026-06-11 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 62/62 |
| 724 | [여인 – 우리 가슴속 깊이 박혀 있던 그 노래, 듣는 순간 그 시절로 돌아갑니다, 이어폰 필수… 👉 첫 소…](https://www.youtube.com/watch?v=yQSP0R8pDqg) | 혼자 듣는 노래 | 8,130 | 358,319 | 44.1 | ×55.5 | 3,216.0 | 109.5분 | 2026-06-30 | 기타 | 음악 | 설명 | 104/104 |
| 725 | [Deep Work Music ~ Midnight City Ambience for Deep Focus ~ C…](https://www.youtube.com/watch?v=czMO-L42nnc) | Focus Room | 25,100 | 1,104,687 | 44.0 | ×126.5 | 6,956.9 | 132.4분 | 2026-05-14 | 2. 자연 소리·백색소음 | 음악 | 설명 | 112/113 |
| 726 | [ㅤㅤㅤ](https://www.youtube.com/watch?v=8k5vqajrHVw) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 38,800 | 1,695,684 | 43.7 | ×295.0 | 25,741.0 | 120.7분 | 2026-08-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 4,300/4,286 |
| 727 | [TIME ALONE WITH GOD - Soaking worship instrumental ∣ Prayer…](https://www.youtube.com/watch?v=uqC91GqvvQg) | Calm Divine F… | 21,100 | 920,325 | 43.6 | ×53.2 | 10,483.1 | 67.1분 | 2026-07-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 515/520 |
| 728 | [[𝑬𝑽𝑬𝑹𝒀𝑫𝑨𝒀, 𝑷𝑰𝑨𝑵𝑶] 몽글몽글🩵 여름에 듣기 좋은 피아노 연주곡 10시간 모음 (중간광고없음, …](https://www.youtube.com/watch?v=5lWOn3zHsI0) | Everyday, Pia… | 5,430 | 236,722 | 43.6 | ×10.2 | 1,788.3 | 614.5분 | 2026-06-09 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 20/20 |
| 729 | [Playlist ∣ 매장을 세련되게 만드는 명품 그루브 🖤🎧 ∣ HIPHOP∙R&B MIX ∣ 매장음악∙카…](https://www.youtube.com/watch?v=h84x1mhg5C4) | hipnb groove | 4,550 | 198,383 | 43.6 | ×31.1 | 1,171.1 | 152.2분 | 2026-05-03 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 32/32 |
| 730 | [사랑했어요 - 김현식 ∣ 가슴 깊이 남은 진한 그리움과 아련한 추억 #윤가연 COVER](https://www.youtube.com/watch?v=2VFOp-WbafE) | GAYEON YOON | 28,600 | 1,244,083 | 43.5 | ×46.5 | 8,885.7 | 5.2분 | 2026-06-02 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 115/117 |
| 731 | [유어아너 허남준이 말아주는 나쁜남자 PLAYLIST 🖤 ㅣ A Dark Bad Boy Playlist In…](https://www.youtube.com/watch?v=0YV2RKwLls0) | 허남준 팬페이지 허남준독… | 5,000 | 217,387 | 43.5 | – | 1,567.2 | 18.4분 | 2026-06-03 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 493/493 |
| 732 | [[Playlist] 기분 좋아지는 산뜻한 유럽 아침 앙상블 ∣ Morning Classical Ensemb…](https://www.youtube.com/watch?v=fdPFoR4XjNQ) | okply | 15,500 | 670,047 | 43.2 | ×85.0 | 4,165.0 | 80.8분 | 2026-05-12 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 325/327 |
| 733 | [👉듣는 순간 마음이 차분해지는 성경 찬양 ∣ Calm Scripture Worship (공부·집중·묵상)](https://www.youtube.com/watch?v=kdn9w1w3v_I) | 생명타임 | 4,690 | 202,347 | 43.1 | ×60.9 | 1,145.1 | 227.7분 | 2026-04-26 | 15. CCM·찬양·국악… | 음악 | 설명 | 178/179 |
| 734 | [[Playlist] 로제 재즈 플레이리스트 🌹🎷 ∣ ROSÉ Jazz Playlist ∣ 재즈 커버](https://www.youtube.com/watch?v=ZqL7hDxAlis) | PLYINK 플링크 | 8,050 | 346,392 | 43.0 | ×5.1 | 4,488.9 | 110.8분 | 2026-08-04 | 7. 재즈·보사노바 | 커버·직접 부른 노래 | 설명 | 116/117 |
| 735 | [The Quiet Night Medieval Village ∣ Relaxing Fantasy Medieva…](https://www.youtube.com/watch?v=dJ5VtIE3kwU) | Fantasy Medie… | 20,700 | 887,751 | 42.9 | ×126.7 | 7,600.9 | 146.7분 | 2026-06-25 | 3. 공부·집중·작업 | 음악 | 설명 | 189/191 |
| 736 | [그냥 틀어두기 좋은 감성 팝송 ☕🌿 12hr Cozy Cafe BGM • ep.110](https://www.youtube.com/watch?v=sDuu-v_gUjw) | winterbudz | 5,370 | 230,141 | 42.9 | ×61.0 | 1,417.3 | 699.6분 | 2026-05-10 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 300/300 |
| 737 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 틀기만 해도 기분이 좋아지는 플리☀️🌿 (광고없음) 국내 노래 모음](https://www.youtube.com/watch?v=9aeCgBBnmYI) | 오늘의 플리 | 6,700 | 286,503 | 42.8 | ×30.8 | 1,745.9 | 617.4분 | 2026-05-09 | 기타 | 플레이리스트·모음 | 없음 | 27/27 |
| 738 | [The Last Dance Before Dawn ∣ Dark Neoclassical music](https://www.youtube.com/watch?v=wy2IX-zmEXo) | Kingdom of Da… | 13,900 | 594,233 | 42.8 | ×144.1 | 3,825.7 | 107.1분 | 2026-05-18 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 653/653 |
| 739 | [Craig David – INSOMNIA 🌙 ∣ Deep Bass EDM Remix ∣ Feel The N…](https://www.youtube.com/watch?v=hymSZZ0mX5U) | musik story🎧 | 12,000 | 511,922 | 42.7 | ×42.5 | 7,393.9 | 4분 | 2026-08-12 | 11. 힙합·R&B·EDM | 음악 | 설명 | 76/75 |
| 740 | [그레고리오성가*한국어* 주여 자비를 베푸소서 #가톨릭성가#그레고리오성가#성가미사#기도음악#묵상음악#천주교성…](https://www.youtube.com/watch?v=9qbqShZRPYw) | DIMOTEO RECOR… | 4,450 | 189,419 | 42.6 | ×101.4 | 1,114.5 | 82.1분 | 2026-05-03 | 15. CCM·찬양·국악… | 음악 | 설명 | 516/521 |
| 741 | [Relaxing Cha-Cha-Cha Swing on the Beautiful Beach – Latin R…](https://www.youtube.com/watch?v=f3zh_3lwiEI) | Grateful For … | 16,800 | 712,809 | 42.4 | ×628.0 | 4,515.0 | 63.8분 | 2026-05-15 | 기타 | 정보·해설 | 설명 | 194/194 |
| 742 | [Sneher Chayay Bhalobasay - স্নেহের ছায়ায় ভালোবাসায় ∣∣ Relax…](https://www.youtube.com/watch?v=uWinY9AA2Z8) | Aruhi Media | 26,500 | 1,123,623 | 42.4 | ×1,079.4 | 6,356.0 | 5.7분 | 2026-04-26 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 108/107 |
| 743 | [그냥 틀어만 놓아도 아침까지 푹 자요/ 이명치료효과/ 듣자마자 바로 잠오는 폭우 빗소리/ 깊은 잠을 위한 …](https://www.youtube.com/watch?v=ASEKIYKzzEc) | 비오는날 ASMR | 21,800 | 921,907 | 42.3 | ×48.7 | 5,209.7 | 180.8분 | 2026-04-26 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 162/167 |
| 744 | [전율 돋는 폭발적 감성 ⚡ 대한민국 락발라드 끝판왕! M.C The Max '잠시만 안녕' 커버 ∣ 김별이](https://www.youtube.com/watch?v=QK3Mxw--VFg) | 김별이 | 5,800 | 244,295 | 42.1 | ×45.4 | 4,573.4 | 5.4분 | 2026-08-27 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 32/34 |
| 745 | [Golden Horizon ∣ Cinematic Sci-Fi Ambient Music — Utopian F…](https://www.youtube.com/watch?v=QcVRYKcCIZ8) | Cosmic Infini… | 3,060 | 128,876 | 42.1 | ×153.6 | 791.5 | 13.2분 | 2026-05-10 | 3. 공부·집중·작업 | 음악 | 설명 | 109/109 |
| 746 | [[무명트롯 2회차] 덕수스님 - 여보 나 아직 여기있어](https://www.youtube.com/watch?v=0CYSvQy42Es) | 무명트롯 | 19,800 | 827,053 | 41.8 | ×94.6 | 4,596.9 | 4.6분 | 2026-04-23 | 9. 가요·발라드·트로트 | 음악 | 설명 | 265/263 |
| 747 | [Ancient Chinese Zen Music🍃Bamboo Flute, Erhu & Guzheng🍃Rela…](https://www.youtube.com/watch?v=CKQuvdIKXgU) | Sound to Peac… | 45,900 | 1,893,554 | 41.2 | ×767.7 | 11,898.5 | 184.4분 | 2026-05-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 592/594 |
| 748 | [Harmony Of Seasons ∣ DVE ∣ Ultimate Classical Piano Collect…](https://www.youtube.com/watch?v=P4H9CSSCuQg) | DVE | 2,360 | 96,984 | 41.1 | ×2,552.2 | 1,977.9 | 15.8분 | 2026-09-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 180/177 |
| 749 | [ENIGMA VOICES IN THE DARK 🌑 Mystical Ambient Music](https://www.youtube.com/watch?v=fOqrhVkQOh4) | The Sound Pal… | 9,630 | 395,731 | 41.1 | ×108.7 | 2,449.3 | 8분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 169/167 |
| 750 | [@노노뮤직#피아노협주곡 #힐링음악 #감성피아노 #클래식음악 #휴식음악#명상음악 #잔잔한음악 #오케스트라 #…](https://www.youtube.com/watch?v=aLyOUOXr5F4) | 노노스튜디오 | 462 | 18,976 | 41.1 | ×115.7 | 132.7 | 30분 | 2026-05-30 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 9/9 |
| 751 | [디지몬 OST - 날 지켜줘 (벅차오르는 파워 락 발라드 어레인지 커버) ∣ GrangChe.Ver](https://www.youtube.com/watch?v=iWfeWC28USw) | GrangChe | 21,500 | 882,548 | 41.0 | ×82.0 | 5,613.2 | 4.8분 | 2026-05-16 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 233/235 |
| 752 | [Clear Negative Thoughts: Krishna Flute & Sitar to Quiet Min…](https://www.youtube.com/watch?v=ugG3qiHWEak) | Healing Raga … | 23,700 | 966,869 | 40.8 | ×68.6 | 13,755.1 | 65.3분 | 2026-08-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 144/142 |
| 753 | [듣자마자 학창시절 떠오르는 노래 🎧 싸이월드 감성 PART 4](https://www.youtube.com/watch?v=F-0JE3Byo9U) | 소꿀 TV | 18,200 | 740,647 | 40.7 | – | 4,619.1 | 82.6분 | 2026-05-12 | 기타 | 플레이리스트·모음 | 설명 | 50/51 |
| 754 | [the best classical music for concentration ∣ deep meditatio…](https://www.youtube.com/watch?v=ViZf4iovMMk) | StillSpace | 32,800 | 1,327,024 | 40.5 | ×326.3 | 8,174.7 | 61.4분 | 2026-05-11 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 608/608 |
| 755 | [ray 【カフェ風アレンジ】 / Remix / 超かぐや姫！](https://www.youtube.com/watch?v=js2syT4l9lc) | Remix中谷 | 5,530 | 222,132 | 40.2 | ×2.6 | 1,640.4 | 12분 | 2026-06-06 | 기타 | 정보·해설 | 설명 | 162/162 |
| 756 | [일상에 틀어 놓는 잔잔한 찬송가 연속 듣기ㅣ어쿠스틱 편곡ㅣ3시간ㅣ중간 광고 없음ㅣ내 영혼이 은총 입어·내 …](https://www.youtube.com/watch?v=EwY1Z6_6H3I) | ALL THAT HYMN… | 7,240 | 289,608 | 40.0 | ×107.6 | 6,007.5 | 197.6분 | 2026-09-02 | 15. CCM·찬양·국악… | 커버·직접 부른 노래 | 설명 | 152/150 |
| 757 | [Beautiful girl and inspiring piano music that help you love…](https://www.youtube.com/watch?v=6oZwrM-i8XU) | Benjamin Elie | 295 | 11,785 | 40.0 | ×1.6 | 361.2 | 4.8분 | 2026-09-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 4/4 |
| 758 | [🎧"세상에서 가장 애절한 목소리" 한 편의 영화 같은 무대, 그리고 가슴을 울리는 목소리…🎙️ 김정호 - …](https://www.youtube.com/watch?v=tjA0yWEZnu8) | 가슴을 울리는 락카페 | 10,900 | 431,825 | 39.6 | ×53.2 | 2,704.1 | 4.4분 | 2026-05-13 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 | 90/90 |
| 759 | [【崩壊スターレイル】満願『極楽顛倒・邪願蓮主』戦BGM〘Illwish Archlotus Boss Theme〙](https://www.youtube.com/watch?v=b_nAKcMiFLI) | ナラかずき(ت) | 5,330 | 210,971 | 39.6 | ×1,159.2 | 1,172.5 | 10.1분 | 2026-04-23 | 기타 | 음악 | 설명 | 141/141 |
| 760 | [Fresh Mind Relaxing 💗 ∣ Slowed + Reverb Lofi Mix for Calm, …](https://www.youtube.com/watch?v=70p4fSeLZ3I) | Vansh Lofi | 29,200 | 1,155,307 | 39.6 | – | 8,325.0 | 15분 | 2026-06-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 46/46 |
| 761 | [백 번을 들어도 후회없을 노래🎵트로트 거친 보이스 @1980통기타 음악 @1980guitar playlis…](https://www.youtube.com/watch?v=ZVTFRwA3r14) | 1980통기타 | 11,900 | 469,049 | 39.4 | ×52.8 | 4,621.2 | 29.9분 | 2026-07-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 107/108 |
| 762 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 우린 아직 흑백영화처럼 사랑하고](https://www.youtube.com/watch?v=71_AXp38B7M) | 세봄 | 14,300 | 562,118 | 39.3 | ×13.7 | 3,790.5 | 17.1분 | 2026-05-25 | 기타 | 플레이리스트·모음 | 설명 | 28/29 |
| 763 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=lXbnhKzEQl8) | Click Bollywo… | 25,800 | 1,000,038 | 38.8 | – | 13,655.6 | 8.1분 | 2026-08-08 | 3. 공부·집중·작업 | 음악 | 설명 | 73/66 |
| 764 | [Melodies from Ancient China – Flute & Guzheng for Relaxatio…](https://www.youtube.com/watch?v=tFhO2omUavw) | Shen Harmony | 25,800 | 998,511 | 38.7 | ×89.5 | 5,572.9 | 64.7분 | 2026-04-24 | 3. 공부·집중·작업 | 음악 | 설명 | 1,321/1,317 |
| 765 | [Rest Tonight In God's Love ∣ Christian Deep Sleep Worship M…](https://www.youtube.com/watch?v=nzc_yRoaBRI) | Midnight Sanc… | 22,200 | 855,269 | 38.5 | ×85.3 | 9,743.1 | 122.5분 | 2026-07-24 | 15. CCM·찬양·국악… | 음악 | 설명 | 332/334 |
| 766 | [Relaxing Piano Music for Inner Peace, Meditation, Stress Re…](https://www.youtube.com/watch?v=dljV0oqDztU) | Celestial Rel… | 11,400 | 436,652 | 38.3 | ×134.3 | 8,414.1 | 127.7분 | 2026-08-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 236/233 |
| 767 | [途中広告なし【カフェBGM】涼やかな夏カフェ｜木漏れ日の、心ほどける森カフェ時間｜作業用・読書・リラックス｜Cafe …](https://www.youtube.com/watch?v=3QKdiHlK6c4) | Kokoro Music … | 21,100 | 804,510 | 38.1 | ×39.0 | 8,744.7 | 122.5분 | 2026-07-20 | 2. 자연 소리·백색소음 | 음악 | 설명 | 73/73 |
| 768 | [[No Ads] Uplifting Morning Piano Music 🌿 ∣ Fresh & Positive…](https://www.youtube.com/watch?v=D8dWbYNFXKc) | Elise Piano ∣… | 24,900 | 944,391 | 37.9 | ×43.9 | 8,877.1 | 183.7분 | 2026-07-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 123/127 |
| 769 | [Oscar & Deep - Feeling Flow](https://www.youtube.com/watch?v=b_DXB1Dj4l8) | Oscar & Deep | 24,400 | 912,380 | 37.4 | ×32.3 | 5,535.3 | 7.5분 | 2026-05-08 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 90/90 |
| 770 | [Soulful Sufi Ghazal - सफर की धूप में साया तलाशते रह गए ∣ He…](https://www.youtube.com/watch?v=JI1OFbt7jRM) | SOUL VIBES IN… | 30,000 | 1,116,356 | 37.2 | ×17.4 | 7,264.8 | 6.4분 | 2026-05-19 | 기타 | 정보·해설 | 설명 | 345/345 |
| 771 | [🪷 이 노래 들으면 막힌 재물운이 술술 풀립니다 ∣ 부처님 대운 명호·진언 13곡 ∣ 관세음·지장·아미타 …](https://www.youtube.com/watch?v=ztFLgJ5idWI) | 연꽃법음 | 3,540 | 131,665 | 37.2 | ×148.0 | 825.9 | 55.7분 | 2026-05-13 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 827/827 |
| 772 | [Dreams Never Sleep （映画『仮面ライダーゼッツ...](https://www.youtube.com/watch?v=9nOX0zxrLfw) | YUTA - Topic | 24,300 | 901,259 | 37.1 | – | 10,160.2 | 4.4분 | 2026-07-23 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 773 | [hyper-focus. ∣ deep house music for coding](https://www.youtube.com/watch?v=uNw_a7HFwvg) | deep archive | 25,200 | 932,572 | 37.0 | ×93.8 | 6,989.9 | 148.4분 | 2026-06-08 | 3. 공부·집중·작업 | 음악 | 설명 | 274/275 |
| 774 | [기분이 산뜻해지는 재즈 찬송가 ∣ Hymn Jazz Playlist ∣ 공부·휴식·카페 BGM [2H] (…](https://www.youtube.com/watch?v=AZCxtUAYrUw) | DearHymn | 11,800 | 436,188 | 37.0 | ×10.6 | 2,621.8 | 120.5분 | 2026-05-06 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 107/107 |
| 775 | [Saxophone Love Songs ❤️ Best Romantic Saxophone Covers ∣ Re…](https://www.youtube.com/watch?v=Uea_DclFKjw) | Sax Chill Vib… | 27,700 | 1,011,193 | 36.5 | – | 14,208.9 | 61분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 97/98 |
| 776 | [【ケルト音楽】家事スイッチが入る🌿 朝の光が気持ちいいBGM｜Relax · Cafe Time](https://www.youtube.com/watch?v=TqiJnA1qm4s) | よもぎの作業用BGM | 12,400 | 451,199 | 36.4 | ×41.0 | 3,540.0 | 63.3분 | 2026-06-14 | 4. 카페·매장·라운지 | 음악 | 설명 | 172/172 |
| 777 | [Healing Music for Anxiety, Fears and Depression 🌿 Heals the…](https://www.youtube.com/watch?v=_SGd39jlrR8) | Peaceful Natu… | 2,920 | 106,212 | 36.4 | ×76.9 | 1,497.1 | 99.2분 | 2026-08-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 60/60 |
| 778 | [Music for meditation, relaxation focus vibe ∣ deep sleep ∣ …](https://www.youtube.com/watch?v=Gsenq8igMJ0) | Healer of Bro… | 9,070 | 329,788 | 36.4 | ×689.9 | 1,907.7 | 61.5분 | 2026-04-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 192/192 |
| 779 | [A Morning at a Paris Café, Feeling Just a Little Lighter ∣ …](https://www.youtube.com/watch?v=OlrHsQ9QexE) | lento | 20,300 | 736,818 | 36.3 | ×77.9 | 4,167.5 | 233.7분 | 2026-04-26 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 116/116 |
| 780 | [𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 ∣ Vinyl Jazz Hiphop ∣ TOKYO ∣ Nujabes / MF Doom / …](https://www.youtube.com/watch?v=2bEmWCwdCds) | ICYFOG | 45,500 | 1,646,807 | 36.2 | ×114.8 | 13,572.6 | 206.5분 | 2026-06-21 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 102/102 |
| 781 | ["매력있다 이 음색"#휴식음악#7080노래#어쿠스틱음악#힐링음악#수면음악#카페음악#7080발라드#명상음악#…](https://www.youtube.com/watch?v=CG3XI3D6gHg) | 7080 마로니에 통기타… | 390 | 14,114 | 36.2 | ×153.4 | 85.2 | 40.9분 | 2026-05-07 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 20/20 |
| 782 | [Sweetest Best Friends Lullaby 🐶🐱💤∣ Calm Sleep Music for Kid…](https://www.youtube.com/watch?v=P5zkPSvY368) | Kidz Wonder T… | 20,000 | 723,823 | 36.2 | ×1.7 | 4,319.2 | 9분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 783 | [이 세상 미련 없이 가련다 [국악 트로트] 가슴 시린 중년 트토르](https://www.youtube.com/watch?v=XcyHeiPdmDc) | 인생트로트 라운지 | 4,140 | 148,908 | 36.0 | – | 946.6 | 5.8분 | 2026-05-16 | 9. 가요·발라드·트로트 | 음악 | 설명 | 19/19 |
| 784 | [music for overthinkers ∣ felt piano & cello for deep focus](https://www.youtube.com/watch?v=EZeW4Sfy8CE) | OTIUM | 27,500 | 986,372 | 35.9 | ×125.9 | 9,599.7 | 60.8분 | 2026-07-09 | 3. 공부·집중·작업 | 음악 | 설명 | 428/430 |
| 785 | [🎵 신나는 복고댄스 Playlist ∣ 추억 감성 뉴트로 댄스곡 모음🎧](https://www.youtube.com/watch?v=WjxmNnlQ8LU) | 7080 정미의 가요방 | 9,040 | 322,587 | 35.7 | ×21.5 | 1,991.6 | 15분 | 2026-05-11 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 217/217 |
| 786 | [African Healing Music ∣ Zulu Sounds for Anxiety Relief](https://www.youtube.com/watch?v=zqsllaGR-gg) | Golden Savann… | 3,380 | 120,345 | 35.6 | ×450.7 | 669.5 | 83.8분 | 2026-04-23 | 1. 수면·명상·힐링 | 한 곡 | 설명 | 123/123 |
| 787 | ["술 한잔 생각나는 깊은 목소리..." 첫 소절 부터 아련해지는 님은 먼 곳에(블루스 Ver.)](https://www.youtube.com/watch?v=M-8Z69t7Smo) | 세월블루스 | 20,900 | 742,836 | 35.5 | ×7.4 | 4,371.7 | 4.4분 | 2026-05-03 | 기타 | 한 곡 | 설명 | 193/194 |
| 788 | [Snowy Russian Night ❄️ Tchaikovsky-Inspired Winter Orchestr…](https://www.youtube.com/watch?v=R3xYX9LJ_hs) | 모노로그 레코드 | 25,600 | 907,398 | 35.5 | ×56.6 | 5,814.5 | 61분 | 2026-05-17 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 1,150/1,158 |
| 789 | [Morning Anxiety? 🌿 ∣ Raag Bhairavi inspired Bansuri (Comple…](https://www.youtube.com/watch?v=FOCy0Ip96rs) | Soulful Breat… | 49,600 | 1,754,936 | 35.4 | ×161.0 | 9,786.5 | 34.4분 | 2026-04-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,399/1,403 |
| 790 | [Bach Style ∣ 마음이 편안해지는 바흐풍 잔잔한 클래식 🌿 [중간광고없음] ∣ 힐링음악, 일상 BG…](https://www.youtube.com/watch?v=hbmQRFw1InE) | Elise Piano ∣… | 24,900 | 880,838 | 35.4 | ×41.0 | 5,424.7 | 130.9분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 341/353 |
| 791 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 텐션 MAX🔥핫한 걸그룹 인기곡 노동요 뮤비 플리☀️여자아이돌 노래모음 ∣ 4K UHD](https://www.youtube.com/watch?v=u7Mu1aDSaR4) | 마쁠(MA-PLE·KPO… | 24,800 | 871,555 | 35.1 | ×5.3 | 6,080.6 | 135.4분 | 2026-05-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 74/74 |
| 792 | [붓꽃잎 편지∣[감성 음악]∣댄스 트로트∣서정적인 트로트](https://www.youtube.com/watch?v=K82Wh68Jvjc) | MusubiRain | 1,310 | 45,795 | 35.0 | ×128.6 | 472.3 | 5분 | 2026-07-15 | 9. 가요·발라드·트로트 | 음악 | 설명 | 26/26 |
| 793 | [𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩 ∣ 아말피 테라스에서 봉골레와 와인 한 잔 ∣ 𝘚𝘰𝘧𝘵 𝘉𝘰𝘴𝘴𝘢 𝘑𝘢𝘻𝘻🍋🥂 ∣ 카페 플…](https://www.youtube.com/watch?v=ZgR4pGSybaw) | BlueDot Diary | 6,520 | 227,693 | 34.9 | ×82.0 | 2,212.4 | 142.8분 | 2026-07-09 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 45/45 |
| 794 | [Barbaad (Dream Rock Remix) ∣ Soulful Atmospheric Cover](https://www.youtube.com/watch?v=FGvMCTLKFjo) | Dhun Tadka | 2,890 | 100,737 | 34.9 | ×22.0 | 604.5 | 4.8분 | 2026-05-06 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 21/21 |
| 795 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 여름 새벽향 낭만 플리](https://www.youtube.com/watch?v=9qwdolh_Jow) | 세봄 | 14,300 | 497,352 | 34.8 | ×12.1 | 3,546.4 | 18.9분 | 2026-06-02 | 기타 | 플레이리스트·모음 | 설명 | 17/17 |
| 796 | [JESUS CALM MY HEART - Instrumental Worship Music For Prayer](https://www.youtube.com/watch?v=GKDVqIGZ5GI) | One Thing | 17,700 | 614,543 | 34.7 | ×65.1 | 4,186.5 | 63.4분 | 2026-05-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 186/186 |
| 797 | [쏟아지는 빗소리에 복잡한 생각은 내려 놓으세요 ∣ 수면유도 백색소음 힐링 ASMR](https://www.youtube.com/watch?v=9TqDVzWADgQ) | Cozy Rainy Da… | 9,320 | 323,254 | 34.7 | ×42.3 | 2,379.8 | 360.1분 | 2026-06-06 | 1. 수면·명상·힐링 | 자연 소리·백색소음 | 설명 | 97/102 |
| 798 | [【夜のリラックスBGM】星空にひたるだけの夜。/A night in starlight｜ピアノ 1時間](https://www.youtube.com/watch?v=wIaFkPnk9oA) | FeelTone | 26,200 | 908,315 | 34.7 | ×126.8 | 5,226.5 | 62분 | 2026-04-29 | 기타 | 정보·해설 | 설명 | 179/179 |
| 799 | [Rest Your Mind ∣ Soothing Indian Classical Music for Stress…](https://www.youtube.com/watch?v=56ymDCWXGZk) | Essential Ind… | 19,100 | 661,884 | 34.6 | ×452.4 | 4,836.4 | 17.7분 | 2026-06-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 93/93 |
| 800 | [AMAPIANO MIX 2026 ∣ 🔥DEEP HOUSE MUSIC VIBES ∣ BEST AFRO PIA…](https://www.youtube.com/watch?v=pyDSBs4URas) | YANOS NATION | 22,600 | 781,893 | 34.6 | ×356.7 | 5,220.6 | 20.9분 | 2026-05-23 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 160/160 |
| 801 | [Best Acoustic Songs of the 80s 🎸 Romantic Classics & Nostal…](https://www.youtube.com/watch?v=9tAdobkt1N0) | 80s Guitar Lo… | 23,800 | 822,882 | 34.6 | ×10.4 | 12,579.2 | 58.5분 | 2026-08-15 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 115/114 |
| 802 | [[중간광고없음] 감정을 다독여주는 따뜻한 피아노 ∣ Warm Piano Music for Emotional…](https://www.youtube.com/watch?v=qDyoLL6XXpU) | Piano Haven | 5,100 | 175,886 | 34.5 | ×38.5 | 980.6 | 195.3분 | 2026-04-23 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 26/26 |
| 803 | ["첫 소절 듣자마자 가슴 한쪽이 먹먹해지네요.." 세월 묻은 목소리로 다시부른 연인(블루스 Ver.)](https://www.youtube.com/watch?v=y7CUK-q-f1s) | 세월블루스 | 20,900 | 715,535 | 34.2 | ×7.1 | 4,138.3 | 4.6분 | 2026-04-30 | 기타 | 정보·해설 | 설명 | 274/274 |
| 804 | [임영웅, 신곡 〈그대 행복이면 됐소〉 발표! 그대만 행복하면 됐소…](https://www.youtube.com/watch?v=p8MCdXUSFmI) | 감성트롯다방 | 4,910 | 166,913 | 34.0 | ×141.1 | 1,543.7 | 6.4분 | 2026-07-04 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 262/265 |
| 805 | [2000~2010 K-POP 감성 모음 🎶 ∣ 듣자마자 떠오르는 그 시절 노래들 – Geuri-um Stu…](https://www.youtube.com/watch?v=9CHBQsxSNa4) | Geuri-um Stud… | 8,720 | 295,892 | 33.9 | ×75.9 | 1,706.3 | 87.5분 | 2026-04-29 | 10. 팝송·K팝·J팝 | 음악 | 설명 | 41/41 |
| 806 | [Oscar & Deep - Closer To My Dreams](https://www.youtube.com/watch?v=YVYkI9z2Evk) | Oscar & Deep | 24,400 | 827,732 | 33.9 | ×29.5 | 9,322.5 | 9.8분 | 2026-07-23 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 45/45 |
| 807 | [Persian & Spanish Fusion Relaxing Music 4K ∣ Persian Gulf &…](https://www.youtube.com/watch?v=UH3bfZ6Rb9E) | WolfRelaxMusi… | 25,400 | 856,519 | 33.7 | ×269.2 | 4,987.0 | 63.7분 | 2026-05-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 857/857 |
| 808 | [The Sound Your Brain Needs Right Now 🌿 Deep Healing Music ∣…](https://www.youtube.com/watch?v=rQ5bIFKQoUc) | Osen Moonlight | 10,100 | 339,270 | 33.6 | ×111.0 | 6,081.0 | 107분 | 2026-08-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 128/112 |
| 809 | [[Playlist] 라흐마니노프의 깊은 그리움 ∣ 멀리서 들려오는 서정적인 선율 (Rachmaninoff …](https://www.youtube.com/watch?v=vcpBmyFBJos) | The Clavis | 19,800 | 662,578 | 33.5 | ×27.9 | 5,366.4 | 97.2분 | 2026-06-18 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 551/555 |
| 810 | [Chinese Zen Music🎵: Bamboo flute, erhu & Guzheng ∣ Relaxing…](https://www.youtube.com/watch?v=6UtPuJcUsyI) | ZenFlute | 32,700 | 1,086,384 | 33.2 | ×155.8 | 7,711.7 | 90.2분 | 2026-06-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 744/750 |
| 811 | [주부들이 엄선한 감성 팝송 Best 26 ∣ EverPop 레트로 팝 컬렉션 ∣ 7080 올드팝송 ∣ 추억…](https://www.youtube.com/watch?v=JZH9pZhtl9I) | 추억의 올드팝 EverP… | 15,800 | 522,696 | 33.1 | ×23.5 | 5,684.4 | 97.8분 | 2026-07-20 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 125/129 |
| 812 | [비 오는 날 듣기 좋은 화란 락발라드 모음 Vol.1 ☔7080 감성 Cover Collection](https://www.youtube.com/watch?v=c4hjZfzxkMM) | ​화란사운드® ∣ 보컬화란 | 16,800 | 551,975 | 32.9 | ×15.6 | 3,837.3 | 34분 | 2026-05-29 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 285/286 |
| 813 | [Zulu Spirit — African Spiritual Ambient Music for Healing &…](https://www.youtube.com/watch?v=cOLt_w3nBx4) | Echo Sanctum | 9,200 | 301,949 | 32.8 | ×21.9 | 1,893.9 | 180.8분 | 2026-05-13 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 228/226 |
| 814 | [Best Romantic Flute Instrumental Collection ❤️ ∣ Tum Aa Gay…](https://www.youtube.com/watch?v=taYeLCeWCd8) | Mansa Music W… | 10,400 | 338,559 | 32.5 | ×138.5 | 2,887.0 | 19.6분 | 2026-06-25 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 84/84 |
| 815 | [🌺 सर्व देवता हरेक बिहानको मन्त्र ∣ Morning Nepali Bhakti So…](https://www.youtube.com/watch?v=U984EoUC8Jo) | Bhajan Hub Ne… | 33,400 | 1,086,157 | 32.5 | ×152.6 | 7,300.9 | 13.6분 | 2026-05-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 760/760 |
| 816 | [하루 끝에 듣는 힐링 발라드 🎶 광고 없는 감성 명곡 모음｜백지영, 성시경, 더원, 이승기, 김필, 양파,…](https://www.youtube.com/watch?v=85w3xNdP09U) | N Melody Ball… | 23,800 | 772,677 | 32.5 | ×128.1 | 5,746.6 | 49.8분 | 2026-06-07 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 없음 | 138/138 |
| 817 | [𝐈𝐬 𝐭𝐢𝐦𝐞 𝐭𝐨 𝐫𝐞𝐥𝐚𝐱⎛˶’ᵕ’˶ ⎞♡.*･ﾟ](https://www.youtube.com/watch?v=a7psAnInAcI) | iamnotcute유유 | 13,800 | 444,222 | 32.2 | ×73.4 | 3,073.3 | 99.8분 | 2026-05-28 | 기타 | 정보·해설 | 설명 | 223/221 |
| 818 | [A Quiet Rainy Afternoon in a 1958 Vermont Town ∣ Relaxing V…](https://www.youtube.com/watch?v=zjgFke-YGZk) | The Serene So… | 34,000 | 1,093,901 | 32.2 | ×57.0 | 6,400.2 | 64분 | 2026-05-02 | 기타 | 음악 | 설명 | 1,843/1,837 |
| 819 | [조선힙합 OFFICIAL 발표곡 중 인기곡만 모았습니다.](https://www.youtube.com/watch?v=fjjiznDoNEQ) | 조선힙합 Official | 28,600 | 910,125 | 31.8 | ×123.5 | 6,629.1 | 28.4분 | 2026-06-05 | 11. 힙합·R&B·EDM | 한 곡 | 설명 | 1,039/1,051 |
| 820 | [Peaceful Adventist Hymns Instrumental ∣ SDA Prayer Music fo…](https://www.youtube.com/watch?v=tj1FpWQsyCg) | Adventist Hym… | 37,500 | 1,175,853 | 31.4 | ×5.8 | 7,216.6 | 61분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 570/571 |
| 821 | [The Beatles on Abbey Road ∣ Greatest Hits in Quartet [No Mi…](https://www.youtube.com/watch?v=VGZ-Xzu73gg) | Golden Harmony | 19,500 | 610,589 | 31.3 | ×71.2 | 5,548.4 | 114.4분 | 2026-07-02 | 기타 | 음악 | 설명 | 299/300 |
| 822 | [🍀 7월, 바다를 보며 들으니 이 노래 너무 좋다 ☕ 커피 한 잔과 함께하는 7080 추억의 올드팝 🎧](https://www.youtube.com/watch?v=q3iHXzi_Qn0) | 행운을담은 올드팝 | 6,160 | 191,687 | 31.1 | ×14.7 | 1,751.8 | 85.7분 | 2026-07-02 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 160/160 |
| 823 | [QUIET WITH JESUS - Instrumental Worship Music For Prayer](https://www.youtube.com/watch?v=2JsArLBjn70) | One Thing | 17,700 | 549,891 | 31.1 | ×58.2 | 3,962.0 | 60.3분 | 2026-06-03 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 119/119 |
| 824 | [celestial bloom 🌿∣ dreamy piano music reflected in dreamy w…](https://www.youtube.com/watch?v=coDaaicD9zM) | She of the Va… | 11,700 | 363,420 | 31.1 | ×55.6 | 4,336.3 | 36.4분 | 2026-07-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 124/126 |
| 825 | [😭 나훈아, 아들의 노래를 듣고 끝내 눈물을 흘리다… 가족 모두가 오열한 순간25](https://www.youtube.com/watch?v=keP33Q5JU_A) | 나훈아AI Korean … | 1,450 | 44,993 | 31.0 | ×79.8 | 461.7 | 6.5분 | 2026-07-14 | 기타 | 음악 | 설명 | 25/25 |
| 826 | [Deep Work Music – CEO Mode ∣ Strategic Clarity, Controlled …](https://www.youtube.com/watch?v=uX6jCay0c6I) | Deep Idle Room | 26,300 | 814,726 | 31.0 | ×206.9 | 5,266.2 | 92.4분 | 2026-05-18 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 475/478 |
| 827 | [Sky - 영원 ∣ 여성보컬 COVER ∣ 다시 들어도 가슴이 무너지는 명곡](https://www.youtube.com/watch?v=ETq8E35CSwk) | 연애상황극 | 11,100 | 343,808 | 31.0 | ×192.5 | 2,121.1 | 4.6분 | 2026-05-11 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 180/179 |
| 828 | [[Playlist] 초록빛 싱그러운 아침에 듣는 모차르트 ∣ 독서와 사색을 위한 평온한 클래식 (Mozar…](https://www.youtube.com/watch?v=wMHsFC7-kUE) | The Clavis | 19,800 | 607,498 | 30.7 | ×25.6 | 4,517.4 | 94.3분 | 2026-06-07 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 315/319 |
| 829 | [Anvarbek Xamroyev - Hayronman 2 (piano version)](https://www.youtube.com/watch?v=q-oZ8xry4MM) | Anvarbek Xamr… | 32,000 | 981,232 | 30.7 | – | 9,932.4 | 4.2분 | 2026-07-13 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 205/205 |
| 830 | [막힌 운을 여는 산신기도｜백호 산신 가피로 액운소멸·복덕성취·재물운 발원](https://www.youtube.com/watch?v=ez0HnQ7tuPM) | 풍요와복덕의노래 | 2,480 | 75,429 | 30.4 | ×14.6 | 578.9 | 4.9분 | 2026-06-12 | 1. 수면·명상·힐링 | 음악 | 설명 | 584/589 |
| 831 | [Peaceful Piano with Rain Sounds 🎶 Relaxing Sleep Music & In…](https://www.youtube.com/watch?v=eUslSNm96D4) | Piano Rain Re… | 29,900 | 904,064 | 30.2 | ×64.5 | 6,727.9 | 206.7분 | 2026-06-07 | 1. 수면·명상·힐링 | 음악 | 설명 | 168/168 |
| 832 | [GOD IN ME - Soaking Worship Instrumental Presence of God ∣ …](https://www.youtube.com/watch?v=L-SoDe2nKoE) | Calm Divine F… | 21,100 | 637,833 | 30.2 | ×36.3 | 3,670.1 | 63.4분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 213/213 |
| 833 | [Chinese Sleep Music: Soft Guzheng & Ambient Pads ∣ Deep Nig…](https://www.youtube.com/watch?v=0ykSzpX6rzg) | Lotus Echo 莲之… | 16,500 | 497,631 | 30.2 | ×126.5 | 3,348.2 | 240.1분 | 2026-05-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 111/111 |
| 834 | [BEST AMAPIANO MIX 2026 ∣ 1hr Of Deep House Amapiano Mix 35 …](https://www.youtube.com/watch?v=3-c885KEOaM) | AMAPIANO SANC… | 19,200 | 578,810 | 30.1 | ×42.1 | 3,846.1 | 65.5분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 137/137 |
| 835 | [DUNE Music for Meditation, Rest & Focus ∣ 3 Hours ∣ No Ads](https://www.youtube.com/watch?v=qTdgu2POFlw) | Empyreal Ambi… | 14,700 | 443,155 | 30.1 | ×18.8 | 6,525.0 | 180분 | 2026-08-13 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 74/74 |
| 836 | [1 Hour Uplifting Morning Music ∣ Veena & Mridangam Indian C…](https://www.youtube.com/watch?v=7z7ol63jaGw) | Nadam | 19,300 | 578,799 | 30.0 | ×306.1 | 3,800.7 | 60.3분 | 2026-05-21 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 303/303 |
| 837 | [Relaxing Piano Music & Rain Sounds for Deep Sleep, Stress R…](https://www.youtube.com/watch?v=e95CjJh6AWc) | Relaxing Slee… | 23,100 | 690,426 | 29.9 | ×669.3 | 3,871.6 | 211.9분 | 2026-04-25 | 2. 자연 소리·백색소음 | 긴 한 곡·반복 | 설명 | 76/77 |
| 838 | [잘 지내💬 아직 네가 있어 / I Hope You’re Doing Well ∣ Sad Korean Ball…](https://www.youtube.com/watch?v=PSnEIoFQB-0) | MusicSong | 7,390 | 220,334 | 29.8 | ×548.1 | 1,305.1 | 4.1분 | 2026-05-04 | 기타 | 음악 | 설명 | 94/94 |
| 839 | [샹송이 이렇게 까지 좋은줄 몰랐습니다. 아침부터 저녁까지 듣게되는 7080올드팝 샹송 ∣ 감성이 폭발한다](https://www.youtube.com/watch?v=ubP0xqEZxYo) | Midnight Melo… | 28,000 | 835,027 | 29.8 | ×233.5 | 5,098.5 | 81.5분 | 2026-05-09 | 9. 가요·발라드·트로트 | 정보·해설 | 설명 | 283/284 |
| 840 | [Chopin — Nocturne Op.9 No.2 (432Hz) ∣ Soothing Piano for Sl…](https://www.youtube.com/watch?v=YrhvsD_nqFk) | Rain Whisper … | 40,800 | 1,215,675 | 29.8 | ×44.4 | 6,758.5 | 61.2분 | 2026-04-23 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 594/596 |
| 841 | [Chandrashekara Pahimam ∣ Lord Shiva Meditation Music ∣ Powe…](https://www.youtube.com/watch?v=9sk0msSGgfA) | Satya Devotio… | 3,390 | 100,518 | 29.6 | ×2.7 | 1,887.0 | 6.8분 | 2026-08-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 23/23 |
| 842 | [Study Focus Enhancement ∣ Classical Music for Deep Concentr…](https://www.youtube.com/watch?v=hUUBG_Nlwh4) | Classical Mind | 22,600 | 669,291 | 29.6 | ×308.3 | 4,423.0 | 139.4분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 184/184 |
| 843 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=634i1Q0C5UI) | Majnukhan | 36,300 | 1,071,391 | 29.5 | – | 7,066.7 | 15.7분 | 2026-05-21 | 3. 공부·집중·작업 | 음악 | 설명 | 100/100 |
| 844 | [music for overthinkers — when the mind goes quiet ∣ deep fo…](https://www.youtube.com/watch?v=IsGUh_yMxDg) | StillSpace | 32,800 | 962,313 | 29.3 | ×236.6 | 5,551.8 | 85.2분 | 2026-04-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 310/310 |
| 845 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=RXYyvE4qRqs) | Click Bollywo… | 25,800 | 754,589 | 29.2 | – | 8,209.7 | 7.8분 | 2026-07-20 | 3. 공부·집중·작업 | 음악 | 설명 | 46/46 |
| 846 | [[Playlist] 여름향기 가득한 카페에서 듣기 좋은 음악 ∣ 잔잔한 감성팝 카페음악 🎧 ∣ Healin…](https://www.youtube.com/watch?v=hlxPD1XBS-A) | 낡은 레코드 | 8,870 | 258,192 | 29.1 | ×25.7 | 1,765.0 | 77.9분 | 2026-05-27 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 33/33 |
| 847 | [마지막 약속(1995) - 김정민 ∣ 여자보컬 리메이크 [원곡감성] Cover](https://www.youtube.com/watch?v=L7EUtPDVddY) | AuraAPT | 13,100 | 379,829 | 29.0 | ×21.8 | 4,180.3 | 5분 | 2026-07-21 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 41/42 |
| 848 | [【GamePiano90min】「時の回廊」クロノ・トリガーゆっくり聴く432Hz Breathing Piano V…](https://www.youtube.com/watch?v=0sJ4qqIp3kk) | 水面こは(Minamo K… | 21,000 | 608,110 | 29.0 | ×183.6 | 3,702.3 | 90.5분 | 2026-05-09 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 200/200 |
| 849 | [𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩.°• 야호-!★⊹⋅ ˚💖 듣자마자 신나는 최신 여돌 플레이리스트](https://www.youtube.com/watch?v=v_AYwiX_XgI) | eon | 5,080 | 146,128 | 28.8 | ×8.1 | 1,108.1 | 81.8분 | 2026-06-10 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 16/16 |
| 850 | [그대 그리고 나(1988) - 소리새 ∣ Acoustic Cover ∣ 레트로카페](https://www.youtube.com/watch?v=CMDXDnLx3QA) | 레트로 카페 (Retro… | 11,600 | 330,384 | 28.5 | ×62.2 | 2,105.4 | 4분 | 2026-05-16 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 55/58 |
| 851 | [🔥5 Musik Instrumen Sunda Modern yang Bikin Nagih ∣ BASS_DRUM](https://www.youtube.com/watch?v=zIrcdA2el3w) | BASS_DRUM | 16,700 | 473,543 | 28.4 | ×154.6 | 2,903.9 | 13.3분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 295/295 |
| 852 | [#singer #kishan #maldhari માં મેલડી તારી કૃપા અપરંપાર #medi…](https://www.youtube.com/watch?v=by0Ok3JgV3o) | Maa Sikotar O… | 1,670 | 47,292 | 28.3 | ×27.6 | 367.7 | 10.2분 | 2026-06-13 | 1. 수면·명상·힐링 | 음악 | 없음 | 16/16 |
| 853 | [Paint It, Black – Dark Gothic Orchestral Cover ∣ Epic Cinem…](https://www.youtube.com/watch?v=zWArs5bT_Nc) | Mimousic | 27,300 | 768,224 | 28.1 | ×21.6 | 4,371.1 | 4.5분 | 2026-04-27 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 410/408 |
| 854 | [A Peaceful Moment with God 🌿 Relaxing Christian Music ∣ Kot…](https://www.youtube.com/watch?v=IIVkaj0R_Gk) | Haven of Faith | 9,260 | 259,424 | 28.0 | ×62.7 | 1,470.9 | 45.9분 | 2026-04-26 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 73/73 |
| 855 | [(WCS2026) VGC Masters Finals Battle Music - Pokémon Champio…](https://www.youtube.com/watch?v=B9Vi8BjqFoc) | RezyMania | 13,000 | 363,624 | 28.0 | ×64.6 | 7,716.6 | 5분 | 2026-09-03 | 기타 | 음악 | 설명 | 355/354 |
| 856 | [마음이 맑아지는 클래식 찬송가 🌿 ∣ 아침에 듣기 좋은 Morning Hymns for Peace & Co…](https://www.youtube.com/watch?v=j6H9mPj769A) | DearHymn | 11,800 | 327,376 | 27.7 | ×7.9 | 2,053.6 | 130.2분 | 2026-05-13 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 455/459 |
| 857 | [잠 안 오 새벽, 깊은 허스키 보컬이 주는 위로 🌧️ 70s 빈티지 어쿠스틱 기타 BGM](https://www.youtube.com/watch?v=BQoJJ8V8TMg) | 조용한 그리움 | 21,400 | 592,665 | 27.7 | ×223.2 | 6,868.2 | 129.5분 | 2026-07-26 | 12. 커버·노래 부르기 | 음악 | 없음 | 106/113 |
| 858 | [[Playlist]고급스러운 카페의 여유로움 ☕️[중간광고없음]카페 매장 음악 🎧 그냥 틀어두세요, 차마실…](https://www.youtube.com/watch?v=lEcJTeg9gCQ) | BGMBUCKS | 19,800 | 545,757 | 27.6 | – | 3,095.9 | 64분 | 2026-04-27 | 4. 카페·매장·라운지 | 연주 | 설명 | 83/83 |
| 859 | [드루와자기 트로트 커버리믹스 총집합! 신나는 트로트 35곡 연속 듣기 🎶추억의 히트송 리믹스,레전드 트로트…](https://www.youtube.com/watch?v=al3dfBmH620) | 드루와자기 | 19,700 | 535,043 | 27.2 | ×1,594.8 | 3,574.9 | 136분 | 2026-05-23 | 5. 운동·드라이브·신나는 | 커버·직접 부른 노래 | 설명 | 236/236 |
| 860 | [🎤 고단한 하루 끝, 막걸리 한잔하며 듣는 눈물 나는 중년 위로가 — 인생막걸리 (가수 창)🎶 인생 트롯 …](https://www.youtube.com/watch?v=4EkREEo9LXQ) | 우리인생뮤직 | 19,700 | 530,831 | 26.9 | ×192.4 | 3,022.2 | 6분 | 2026-04-27 | 9. 가요·발라드·트로트 | 음악 | 설명 | 309/309 |
| 861 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 서울숲 카페에서 하루종일 듣기좋은 팝송 𝟏𝟎시간 (중간광고없음) ☀️🌿 기분 좋아지는 카페…](https://www.youtube.com/watch?v=2eFGY53k350) | With Lofi Cafe | 4,980 | 134,154 | 26.9 | ×14.3 | 1,013.4 | 616.3분 | 2026-06-09 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 9/9 |
| 862 | [비 오는 날 카페에서 듣기 좋은 추억의 노래 ∣ 계속 듣게 되는 7080 라디오 감성 올드팝](https://www.youtube.com/watch?v=riMgzQ7B4JA) | morgellia(모르겔… | 18,100 | 484,789 | 26.8 | ×58.9 | 3,160.8 | 165.9분 | 2026-05-19 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 313/313 |
| 863 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 요즘 연남동 카페에서 듣기좋은 가을 감성 팝송 𝟏𝟎시간 (중간광고없음) 🍂☕ 작업 · 휴식…](https://www.youtube.com/watch?v=asmDdv4Dfig) | With Lofi Cafe | 4,980 | 133,052 | 26.7 | ×14.3 | 5,944.7 | 647.2분 | 2026-09-27 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 15/15 |
| 864 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 이게 극락 사운드인가?🪷 ∣ 속세 탈출용 불교 재즈🎧](https://www.youtube.com/watch?v=EQzDJeyYNX0) | chill potato … | 15,500 | 411,007 | 26.5 | ×59.5 | 2,546.3 | 123.1분 | 2026-05-11 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 282/282 |
| 865 | [𝐘𝐨𝐠𝐚 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 바람이 살랑 우붓의 요가 샬라ㅣ허밍 요가 음악](https://www.youtube.com/watch?v=34ESzO9DdwQ) | 김샨티(Shanti Ki… | 5,070 | 134,076 | 26.4 | ×11.8 | 1,097.9 | 61.5분 | 2026-06-20 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 45/46 |
| 866 | [【4K/途中広告なし】がんばった自分を、休ませる夜｜自律神経を整える癒しのピアノBGM｜睡眠・リラックス用｜3時間](https://www.youtube.com/watch?v=TlPKpR7on9o) | Starry Note | 22,000 | 580,817 | 26.4 | ×54.8 | 5,145.7 | 192.8분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 199/196 |
| 867 | [1 Hour Relaxing Piano ∣ Piano Therapy (پیانو درمانی) ∣ ۱ سا…](https://www.youtube.com/watch?v=rhfCDOTWNs0) | amir moradi | 7,130 | 187,781 | 26.3 | ×33.2 | 1,060.7 | 61.3분 | 2026-04-26 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 386/386 |
| 868 | [Arabic Deep House Mix & arabic Oud - The Last Pharaoh (Offi…](https://www.youtube.com/watch?v=zEA4nqtiy94) | Deep Tune Fan… | 20,200 | 530,177 | 26.2 | ×55.3 | 3,359.1 | 8분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 113/113 |
| 869 | [All RED EVIL JACK MUSIC【作業用/For work】](https://www.youtube.com/watch?v=hruX5UfVTYw) | イヴch🍳🥚 | 2,450 | 64,028 | 26.1 | – | 771.9 | 8.6분 | 2026-07-29 | 기타 | 음악 | 설명 | 49/49 |
| 870 | [Your Soul Will Thank You For This ∣∣ DIVINE Krishna Dhun & …](https://www.youtube.com/watch?v=-gGLDLqN03M) | Krishna Lovers | 49,800 | 1,295,912 | 26.0 | ×348.4 | 8,417.3 | 30.6분 | 2026-05-19 | 기타 | 정보·해설 | 설명 | 1,350/1,350 |
| 871 | [[playlist] 신기하네, 이런 빈티지재즈 좋아하는 걸 어떻게 알고 틀어줬지? ∣ 중간 광고 없음 Ja…](https://www.youtube.com/watch?v=aZRegDWuCEo) | 포 시즌 플리 Four … | 39,200 | 1,018,491 | 26.0 | ×44.1 | 15,424.5 | 75.1분 | 2026-08-15 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 416/434 |
| 872 | [Mortal Shell 2 [OST] - Ambient Music [HQ]](https://www.youtube.com/watch?v=0xjJ71Vcqc0) | Taneomi | 5,760 | 149,417 | 25.9 | ×33.3 | 1,120.3 | 5.8분 | 2026-06-08 | 13. OST·사운드트랙 | 음악 | 설명 | 258/258 |
| 873 | [Soothe Station - Andamanaya - Tagalog Version (Pakaranon Ba…](https://www.youtube.com/watch?v=4SWpVSbm4Qo) | Soothe Sta. | 28,900 | 747,299 | 25.9 | ×5.4 | 5,458.1 | 4.4분 | 2026-06-05 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 168/167 |
| 874 | [지렸다... 심장마비 🔥 선넘은 여성보컬 락발라드 COVER 33곡 모음 ∣ 전율돋는 초고음 소름주의보 3…](https://www.youtube.com/watch?v=tol8QOlOsPo) | 아무노래개조소 | 9,460 | 243,608 | 25.8 | ×27.8 | 1,918.2 | 133.5분 | 2026-06-15 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 143/148 |
| 875 | [Spirit Of Wolf ∣ Native Inspired Healing Music for Deep Cal…](https://www.youtube.com/watch?v=SUgiw7VzoUY) | Ancestral Ech… | 5,010 | 128,269 | 25.6 | ×151.8 | 1,097.4 | 8.1분 | 2026-06-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 318/318 |
| 876 | [Naagin All Seasons - ‘The Origin of Revenge‘ MV ∣ Naagin Em…](https://www.youtube.com/watch?v=-yEf-59hqRs) | 𝐍𝐚𝐚𝐠𝐢𝐧 𝐇𝐏 𝐎𝐟𝐟… | 24,100 | 616,756 | 25.6 | – | 4,464.4 | 11.4분 | 2026-06-04 | 기타 | 한 곡 | 설명 | 163/163 |
| 877 | [15 Min 528Hz Self Healing Music 🌿 Calm Your Nervous System …](https://www.youtube.com/watch?v=HFW4awIfBmo) | Inner Healing… | 1,240 | 31,687 | 25.6 | ×21.4 | 1,142.7 | 15.5분 | 2026-09-22 | 1. 수면·명상·힐링 | 음악 | 설명 | 14/14 |
| 878 | [Drifting Low (Ethereal Deep House) — Club Nights](https://www.youtube.com/watch?v=YtprplnFUpc) | Club Nights | 28,400 | 724,537 | 25.5 | ×23.6 | 6,052.9 | 6.4분 | 2026-06-22 | 기타 | 정보·해설 | 설명 | 47/47 |
| 879 | [💿 노릇노릇 빵아저씨가 만든 브금🍞](https://www.youtube.com/watch?v=2bUpv56PbMw) | 프륀 Pruiin | 11,400 | 287,314 | 25.2 | ×19.2 | 2,194.1 | 123.7분 | 2026-06-11 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 90/91 |
| 880 | [Stress Relief Jazz 🌙 Smooth Sax for Calm, Relaxation & Anxi…](https://www.youtube.com/watch?v=YPsVWworsbc) | JazzAyo Lounge | 37,700 | 949,374 | 25.2 | ×694.5 | 5,558.7 | 133.2분 | 2026-05-02 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 387/385 |
| 881 | [playlist ∣ 여름, 레몬과 재즈에 대하여](https://www.youtube.com/watch?v=Gr7ZxTdL8XA) | centralgrocer… | 27,200 | 684,159 | 25.1 | ×50.0 | 6,376.9 | 236.8분 | 2026-07-05 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 207/209 |
| 882 | [Relaxing Country Gospel ∣ Call Upon the Name of Jesus ∣ Hea…](https://www.youtube.com/watch?v=R38UIWZtjkQ) | Breathing Pla… | 35,000 | 871,138 | 24.9 | ×245.1 | 6,835.8 | 6.4분 | 2026-06-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 863/859 |
| 883 | [Into the Misty Scottish Highlands｜Celtic Music for Deep Foc…](https://www.youtube.com/watch?v=7JojfPKvTM4) | Echoes of Alba | 44,800 | 1,114,471 | 24.9 | ×44.0 | 6,338.2 | 143.4분 | 2026-04-27 | 3. 공부·집중·작업 | 음악 | 설명 | 480/481 |
| 884 | [눈물 없이는 못 듣는 감성 락발라드 트로트 12곡｜중년 가슴을 울리는 인생 노래 모음｜55분 연속듣기](https://www.youtube.com/watch?v=0rFs08Wz1Xw) | 인생은 트로트 | 9,120 | 226,496 | 24.8 | ×15.5 | 2,866.6 | 55.5분 | 2026-08-02 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 96/96 |
| 885 | [Chike & Tiwa Savage - We Go Make Am Work (2026 Afro Music) …](https://www.youtube.com/watch?v=0PVF8lImHNs) | Afro Music So… | 2,600 | 64,422 | 24.8 | ×82.5 | 525.4 | 6분 | 2026-06-19 | 14. AI 음악 | AI 음악 | 설명 | 10/10 |
| 886 | [듣는 순간 마음이 편안해지는 첼로 음악 🎻 ∣ 공부, 휴식, 감성 힐링 음악](https://www.youtube.com/watch?v=QmJoFjq-aWE) | 따뜻한 휴식 Studio | 1,990 | 49,094 | 24.7 | ×112.6 | 329.7 | 51.4분 | 2026-05-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 37/37 |
| 887 | [Música espiritual hebrea - Melodías antiguas de Israel para…](https://www.youtube.com/watch?v=A7ZlOXV_CrU) | Sacred Hebrew… | 20,200 | 494,694 | 24.5 | ×276.1 | 3,277.9 | 63.5분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 749/752 |
| 888 | [Arabic Oud & Flamenco Guitar – Gentle Instrumental Music fo…](https://www.youtube.com/watch?v=4HR2eB5p8WI) | Andalusian Ou… | 26,700 | 642,262 | 24.1 | ×166.7 | 4,293.1 | 90.8분 | 2026-05-23 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 264/264 |
| 889 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭☕ Let the Day Start Softly with Coffee and Korean C…](https://www.youtube.com/watch?v=FUrT7LN9VRU) | Seoul Flow AI | 23,700 | 564,115 | 23.8 | ×48.6 | 3,701.1 | 166.6분 | 2026-05-20 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 133/133 |
| 890 | [내 삶에 임하소서 ∣ 주기도문 기반 잔잔한 찬양, 조용한 기도 ∣ Let Your Presence Fill…](https://www.youtube.com/watch?v=HzyxKZ_w2_8) | 쉼이 되는 찬양 | 3,030 | 71,265 | 23.5 | ×13.8 | 408.6 | 5.3분 | 2026-04-28 | 15. CCM·찬양·국악… | 음악 | 설명 | 27/27 |
| 891 | [KWUBAKA (AMAPIANO remix) by ABASHAZANGENDO (BGM remix)](https://www.youtube.com/watch?v=3TgKlzPGh6Y) | Burundi Golde… | 16,700 | 383,707 | 23.0 | ×13.2 | 2,620.7 | 4.4분 | 2026-05-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 90/90 |
| 892 | [पहाड़ों में गूंजती जादुई बाँसुरी 🎋 Magical Mountain Flute M…](https://www.youtube.com/watch?v=orUOWfIkmM4) | Vibe Without … | 26,600 | 608,874 | 22.9 | ×198.3 | 3,824.4 | 46.8분 | 2026-05-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 416/415 |
| 893 | [10-Minute Divine Flute Meditation ∣ Inner Peace & Healing ∣…](https://www.youtube.com/watch?v=_3PmWQ0lENE) | Sri Ganapathy… | 45,500 | 1,039,812 | 22.9 | – | 9,839.6 | 10.6분 | 2026-07-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,480/1,482 |
| 894 | [Morning Serenity 🌿 Raag Alhaiya Bilawal inspired Healing In…](https://www.youtube.com/watch?v=7RR_x4Tu7EE) | Soulful Breat… | 49,600 | 1,130,719 | 22.8 | ×103.7 | 7,279.8 | 66.2분 | 2026-05-18 | 1. 수면·명상·힐링 | 음악 | 설명 | 278/274 |
| 895 | [Playlist✍️ 수험생 초집중모드 공부 플레이리스트 ∣ 틀어놓는 순간 공부에 빠져드는 공부플리 BGM🎧…](https://www.youtube.com/watch?v=vuYrODP_RTE) | obne music 오브… | 7,110 | 161,939 | 22.8 | ×22.2 | 3,062.7 | 120.2분 | 2026-08-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 4/6 |
| 896 | [Calm Morning Music ∣ Relaxing Flute for Anxiety Relief](https://www.youtube.com/watch?v=P1aHG6IqCtM) | Moksha Sounds… | 37,000 | 836,488 | 22.6 | ×135.5 | 4,850.1 | 40.2분 | 2026-04-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 293/293 |
| 897 | [Spirit Of Eagle Native American Healing Music for Vision, F…](https://www.youtube.com/watch?v=j3OaU9N8uIU) | Ancestral Ech… | 5,010 | 112,823 | 22.5 | ×133.5 | 1,000.4 | 9.1분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 215/213 |
| 898 | [Playlist ∣ Smooth Hip Hop Groove 😎 ∣ GROOVE · JAZZHOP ∣ Caf…](https://www.youtube.com/watch?v=ru-PF195pR0) | PoponWave | 23,000 | 517,917 | 22.5 | ×35.0 | 2,986.9 | 215.2분 | 2026-04-29 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 177/177 |
| 899 | [【あつ森】Lofi Night｜雨降る夜に部屋でゆっくりと過ごす☔雨音｜作業・勉強【1時間】](https://www.youtube.com/watch?v=2SV-ueN0hxA) | Tsumugi's Coz… | 24,800 | 556,541 | 22.4 | ×53.5 | 4,185.8 | 60.2분 | 2026-06-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 104/104 |
| 900 | [[Playlist] 오늘은 일본 카페에 앉아 있는 기분으로](https://www.youtube.com/watch?v=fDk1BeVbz_4) | JazzBrown | 15,900 | 352,807 | 22.2 | ×61.1 | 2,497.2 | 70.5분 | 2026-06-01 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 30/31 |
| 901 | [【在喧囂中尋回本心，伴隨天籟美聲聆聽千年的清静】 靈魂淨化｜清静經 ｜Taoist Healing Music・ヒーリ…](https://www.youtube.com/watch?v=AqSDuxZWMHk) | YUCHIN'S TAOI… | 3,500 | 77,638 | 22.2 | ×15.8 | 615.8 | 4.6분 | 2026-06-16 | 1. 수면·명상·힐링 | 음악 | 설명 | 73/73 |
| 902 | [👑💎 Beautiful Princesses, Magical Animals & Relaxing Piano M…](https://www.youtube.com/watch?v=LGexlV5skko) | Princesses Pa… | 7,620 | 168,253 | 22.1 | ×28.4 | 1,457.9 | 5.7분 | 2026-06-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 181/182 |
| 903 | [[중간광고없음] 🌲✨ 복잡한 마음은 잠시 내려놓자 ∣ 위로와 휴식의 피아노 ∣ BGM ∣ 휴식, 힐링, 위로](https://www.youtube.com/watch?v=ADirqRo8IyI) | Riae & Piano | 12,400 | 270,178 | 21.8 | ×17.6 | 3,785.3 | 180.9분 | 2026-08-09 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 33/35 |
| 904 | [LOVE 💚 ∣ 639Hz Heart Chakra Healing Music ∣ Self-Love, Comp…](https://www.youtube.com/watch?v=DZYgNIUjkH4) | Sound of the … | 1,570 | 34,202 | 21.8 | ×17.8 | 620.6 | 5.4분 | 2026-08-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 130/130 |
| 905 | [Nine Inch Nails x Hans Zimmer - Right Where Time Belongs (D…](https://www.youtube.com/watch?v=QqyWPg0fM_E) | Dreams Of Col… | 14,300 | 310,958 | 21.8 | ×8.2 | 2,535.0 | 7분 | 2026-06-19 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,321/1,320 |
| 906 | [불(佛)빛사운드 - 물처럼, 바람처럼 M/V 4K #불교음악](https://www.youtube.com/watch?v=G7P3BWOH67s) | 불佛빛사운드 | 3,990 | 86,361 | 21.6 | ×10.3 | 595.6 | 5.8분 | 2026-05-28 | 1. 수면·명상·힐링 | AI 음악 | 설명 | 118/119 |
| 907 | [途中広告なし[BGM]心が晴れる朝🌿Gentle Morning Piano & Guitar Music](https://www.youtube.com/watch?v=OSXpI32ZlQI) | Aurora Tune | 19,200 | 415,428 | 21.6 | ×6.3 | 3,068.7 | 123.5분 | 2026-06-06 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 50/50 |
| 908 | [music to stay locked in](https://www.youtube.com/watch?v=eL5rWVPguoc) | Productivity … | 39,000 | 844,072 | 21.6 | ×36.3 | 11,923.4 | 115.6분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 208/207 |
| 909 | [[playlist] 희한하네, 살면서 이렇게 좋은 재즈는 처음 들어. 이렇게 오래 살았는데도 말이야. ∣ …](https://www.youtube.com/watch?v=cHC2M0hdKCU) | 포 시즌 플리 Four … | 39,200 | 842,742 | 21.5 | ×36.5 | 11,096.3 | 65분 | 2026-08-05 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 299/300 |
| 910 | [[60만뷰 감사합니다]가왕의 명곡을 락발라드로! 조용필 - 그 겨울의 찻집 (AI Cover / 알고보니 …](https://www.youtube.com/watch?v=_GrNoR-QyMQ) | 알고보니 혼비백산 | 42,900 | 920,105 | 21.4 | ×98.7 | 6,095.5 | 5.4분 | 2026-05-22 | 14. AI 음악 | AI 음악 | 설명 | 249/256 |
| 911 | [고양이 카페에 놀러 올래?](https://www.youtube.com/watch?v=ifT02Y1gbuI) | 꾸양이 | 14,800 | 313,219 | 21.2 | ×14.0 | 2,143.5 | 63.6분 | 2026-05-27 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 152/154 |
| 912 | [TAI CHI MUSIC – MELODIES OF THE TAO ∣ Chinese Relaxing Musi…](https://www.youtube.com/watch?v=PcSZ9tCBFQ0) | VibrArte Music | 17,100 | 361,608 | 21.1 | ×64.9 | 2,156.8 | 58.9분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 162/162 |
| 913 | [머리가 맑아지고🌳마음이 평온해져요. 피아노와 플루트 선율 ∣ 3시간, 힐링음악, 명상음악 ∣ Relaxin…](https://www.youtube.com/watch?v=QPa9L5TDD-4) | 살구사운드 SalguSo… | 10,700 | 226,297 | 21.1 | ×18.3 | 1,895.9 | 188분 | 2026-06-22 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 129/129 |
| 914 | [Bombay BGM ∣ 80-Piece Orchestra](https://www.youtube.com/watch?v=ssC6VM6GQ-4) | Australian In… | 32,100 | 676,973 | 21.1 | – | 4,341.4 | 13.3분 | 2026-05-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 234/236 |
| 915 | [🍂하루종일 듣기 좋은 기분 좋은 클래식 명곡 ∣ 중간광고❌∣ 쇼팽, 리스트, 슈만, 바흐 ∣ 명상, 휴식,…](https://www.youtube.com/watch?v=zG6O9a_rRpY) | 퓨얼리 피아노 클래식 𝚋… | 22,200 | 463,183 | 20.9 | ×16.0 | 11,189.2 | 180.7분 | 2026-09-08 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 112/117 |
| 916 | [【洋楽Playlist】疲れた夜に聴きたい、やさしく包まれるチルR&B 🌆✨｜途中広告なし【作業用BGM】](https://www.youtube.com/watch?v=kf0crw-vh4g) | Moo'in Nights | 25,000 | 518,969 | 20.8 | ×16.2 | 3,582.2 | 66.2분 | 2026-05-28 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 35/35 |
| 917 | [10 Most Beautiful Melodies Ever Written for Piano](https://www.youtube.com/watch?v=vmbG0x1jq_s) | Lisztopher | 9,580 | 198,661 | 20.7 | ×40.5 | 1,334.0 | 15.9분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 269/269 |
| 918 | [🍉 냉장고를 열었더니 수박만 있는 브금](https://www.youtube.com/watch?v=h6oskIb0ASU) | 프륀 Pruiin | 11,400 | 235,916 | 20.7 | ×15.9 | 2,408.6 | 146.4분 | 2026-07-14 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 100/101 |
| 919 | [Enya - I know Your Pain (2026 Official Music Video)](https://www.youtube.com/watch?v=1AZagg8LCDw) | Celestine Echo | 14,700 | 303,921 | 20.7 | ×58.3 | 2,876.7 | 6.3분 | 2026-07-06 | 기타 | 한 곡 | 설명 | 97/97 |
| 920 | [싱그러운 아침, 고요한 클래식 선율 속에서 마음의 평화를 느껴보세요. Healing Classics와 함께…](https://www.youtube.com/watch?v=gtHsO8taxgo) | 클래식힐링 | 14,600 | 301,806 | 20.7 | ×48.9 | 1,852.3 | 125.2분 | 2026-05-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 127/127 |
| 921 | [#Zumba Work out 💪🏽..Full energy...Best music for Work out..](https://www.youtube.com/watch?v=cuzHvFb2It0) | Zumbique | 1,210 | 24,874 | 20.6 | ×8.9 | 224.7 | 7.8분 | 2026-07-01 | 기타 | 음악 | 설명 | 4/4 |
| 922 | [[찬송가 모음]주님 앞에 펑펑 울고 싶을 때 듣는 찬양ㅣ눈물의 찬송가 10곡ㅣ깊은 울림 바리톤 찬양ㅣHYM…](https://www.youtube.com/watch?v=giFgcjlR4Co) | 골방 찬양 | 26,000 | 534,541 | 20.6 | ×5.1 | 3,394.8 | 81.4분 | 2026-05-15 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 1,318/1,318 |
| 923 | [가슴을 울리는 감성 트로트 5곡 모음 ∣ 깊은 밤 듣기 좋은 노래](https://www.youtube.com/watch?v=o_RE1dPuUoo) | 트로트 작은 음악실 | 23,500 | 482,871 | 20.6 | ×79.6 | 3,114.9 | 24.4분 | 2026-05-18 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 209/214 |
| 924 | [Lingashtakam Shiva Meditation Music ∣ Powerful Healing Mant…](https://www.youtube.com/watch?v=TehHNpaUk0s) | Satya Devotio… | 3,390 | 69,152 | 20.4 | ×1.8 | 514.7 | 5.7분 | 2026-06-07 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 30/30 |
| 925 | [🎹 Corazón Silente ∣ Piano para Calmar la Mente](https://www.youtube.com/watch?v=3jUY4NFO9sg) | El Piano de E… | 14,200 | 288,723 | 20.3 | ×395.5 | 3,401.8 | 4.1분 | 2026-07-27 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 25/25 |
| 926 | [피아노 다니엘 린데만 Pf. Daniel Lindeman - 차이콥스키 [사계] 작품번호37a 4월 Tch…](https://www.youtube.com/watch?v=yhDdH93H4Tc) | HalmaCineTokk… | 15,000 | 302,970 | 20.2 | ×1,942.1 | 1,687.4 | 5.8분 | 2026-04-23 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 377/377 |
| 927 | [Whispers of the Ancient Forest｜Mystical Celtic Music for De…](https://www.youtube.com/watch?v=DQ_KPUXyY7o) | Echoes of Alba | 44,800 | 899,628 | 20.1 | ×35.5 | 5,964.4 | 140.2분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 129/126 |
| 928 | [고고프렌즈 “국어별동대” 피아노커버](https://www.youtube.com/watch?v=IkZ1vxE2GeQ) | MUJINS 뮤진스 | 19,200 | 378,881 | 19.7 | ×54.7 | 3,947.1 | 7.5분 | 2026-07-16 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 521/525 |
| 929 | [Habias X Filho Do Zua - Se a Vida Decide Me Levar](https://www.youtube.com/watch?v=SnGHZcvK2TA) | Habias | 31,400 | 618,711 | 19.7 | ×33.9 | 7,679.2 | 4.2분 | 2026-07-31 | 기타 | 음악 | 설명 | 245/243 |
| 930 | [【作業用BGM】流すだけで前向きになれる洋楽 House Pop Mix｜リラックス・集中・気分転換](https://www.youtube.com/watch?v=Kk1n4AZQyws) | Lucky Clover … | 39,600 | 768,874 | 19.4 | ×93.1 | 5,576.6 | 105.5분 | 2026-06-04 | 기타 | 음악 | 설명 | 66/66 |
| 931 | [🍃Xanh Playlist 2🍃TAN LÀM, BẬT NHẠC∣ Nhạc R&B Lofi Chill Yêu…](https://www.youtube.com/watch?v=lkotmZNWq5I) | Xanh | 46,200 | 891,250 | 19.3 | ×9.3 | 16,829.4 | 50.4분 | 2026-08-28 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 217/212 |
| 932 | [Sleep Instantly with Soft Piano and Rain 🌧️ Relaxing Music …](https://www.youtube.com/watch?v=PclKQrQuR7U) | Relaxing Piano | 37,000 | 706,711 | 19.1 | ×121.3 | 9,027.7 | 181.6분 | 2026-08-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 79/79 |
| 933 | [(Free For Profit) Melodic Type Beat - "ANGEL"](https://www.youtube.com/watch?v=LgS91RB_BDk) | Nocturnn | 36,000 | 684,696 | 19.0 | ×19.6 | 5,573.3 | 4분 | 2026-06-19 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 229/229 |
| 934 | [It's TV Time! – Deltarune Piano Collections, Vol. 2 (Offici…](https://www.youtube.com/watch?v=44Dh4Vb8Wtk) | Trevor Alan G… | 18,200 | 345,540 | 19.0 | – | 18,816.0 | 5.6분 | 2026-10-01 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 993/993 |
| 935 | [네가 내게 알려줬어💕｜『 四季の笑顔 (사계절 미소)』｜가사해석/Lyrics](https://www.youtube.com/watch?v=T7gBckYYJug) | Nonohara | 1,240 | 23,517 | 19.0 | ×10.7 | 481.6 | 4.9분 | 2026-09-01 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 22/23 |
| 936 | [💔K- 락 발라드 초강력 허스키 여신 떳다 l 2곡 연속 목소리 소름 미쳤다😱"사랑이 나를 죽인다" ㅣ원곡…](https://www.youtube.com/watch?v=EpXINywBT1M) | 음악의 정원 [Garde… | 16,800 | 317,621 | 18.9 | ×95.7 | 1,795.1 | 7.7분 | 2026-04-26 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 106/106 |
| 937 | [Healing Music for Anxiety, Fears and Depression 🌿 Heals the…](https://www.youtube.com/watch?v=RUowd-_b72Y) | Nature Aura | 3,940 | 74,402 | 18.9 | ×59.8 | 702.2 | 104.8분 | 2026-07-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 51/51 |
| 938 | [𝓅𝓁𝒶𝓎𝓁𝒾𝓈𝓉 𖤐₊˚ 앙큼 미소녀 브금 │ 공부·작업·집중 BGM ✦](https://www.youtube.com/watch?v=8rE90EGyCbY) | 오늘은 무슨 컨셉? | 3,010 | 56,044 | 18.6 | ×15.8 | 403.3 | 29.2분 | 2026-06-03 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 39/39 |
| 939 | [(No Ads)Rain Ambience and Calm Piano Music – Peaceful Sleep…](https://www.youtube.com/watch?v=oa4PEL3kHLo) | Relaxing Piano | 37,000 | 686,094 | 18.5 | ×117.7 | 7,599.1 | 183.7분 | 2026-07-22 | 2. 자연 소리·백색소음 | 음악 | 설명 | 228/229 |
| 940 | [Walking Past an Old Library in Autumn Boston 🍂 Warm Jazz, F…](https://www.youtube.com/watch?v=0KCrdROdw4g) | Dreams Jazz M… | 48,200 | 889,578 | 18.5 | ×26.5 | 25,477.4 | 209분 | 2026-09-15 | 7. 재즈·보사노바 | 음악 | 설명 | 72/71 |
| 941 | [7080 카페음악 베스트🌺50대이상이 들으면 기분좋아지는 7080노래모음 ∣ 베스트 7080노래모음 ∣ 광…](https://www.youtube.com/watch?v=IZmsMTzrWDY) | Korean Cafe M… | 3,280 | 60,041 | 18.3 | ×1,017.6 | 663.7 | 10.3분 | 2026-07-21 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 3/3 |
| 942 | [90년대 00년대 락발라드 명곡 모음 ∣ 샤우팅 넘치며 감동적인 락발라드 40곡 연속듣기 ∣ 엠씨더맥스, …](https://www.youtube.com/watch?v=5c_EJyjOdWQ) | 발라드 홈 / BALLA… | 10,200 | 185,172 | 18.1 | ×18.3 | 1,694.9 | 154.9분 | 2026-07-03 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 23/23 |
| 943 | [Deep Sleep Music ∣ 528hz Whole Body Healing Frequency, Mela…](https://www.youtube.com/watch?v=9tczYViDUak) | Healing Sleep… | 28,100 | 509,659 | 18.1 | ×110.3 | 4,540.4 | 698.1분 | 2026-06-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 283/283 |
| 944 | [트로트 모음 50곡 #트로트 메들리 #인기트로트 🎶 하루 종일 듣기 좋은 노래 모음 🎶 추억의 트로트 명곡…](https://www.youtube.com/watch?v=5GO9R1-U5OM) | SonicVista | 26,900 | 483,693 | 18.0 | ×2,740.5 | 3,766.6 | 78.9분 | 2026-06-13 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 77/79 |
| 945 | [밤바다 보이는 카페 창가, 조용히 듣기 좋은 7080 라디오 감성 올드팝](https://www.youtube.com/watch?v=9x53vG82_Ao) | morgellia(모르겔… | 18,100 | 322,801 | 17.8 | ×39.2 | 2,205.3 | 159.8분 | 2026-05-26 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 151/151 |
| 946 | [가슴 뭉클한 옛날 노래 🍂 백마강·해운대 엘레지·동숙의 노래｜중년·어르신을 위한 추억의 트로트 50곡 🍁 …](https://www.youtube.com/watch?v=F9mzexxZOVo) | 추억의 K트롯 | 14,700 | 261,084 | 17.8 | ×70.3 | 3,128.3 | 137.7분 | 2026-07-28 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 104/105 |
| 947 | [Chopin for Autumn Nights — Peaceful Piano for Relaxation (4…](https://www.youtube.com/watch?v=AkZrzHCfivc) | Rain Whisper … | 40,800 | 718,071 | 17.6 | ×26.2 | 16,019.9 | 78.5분 | 2026-09-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 143/145 |
| 948 | [Morning Energy Music ∣ Dilruba Raga Yaman ∣ 1.5 Hours](https://www.youtube.com/watch?v=DMcoOLvmAyQ) | Raga Focus | 37,500 | 657,501 | 17.5 | ×438.6 | 4,003.1 | 90분 | 2026-05-09 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 166/166 |
| 949 | [NGWIZA (BGM Remix) Ballet Royal du Burundi](https://www.youtube.com/watch?v=ho_IGrAkUSs) | Burundi Golde… | 16,700 | 292,587 | 17.5 | ×10.1 | 1,807.4 | 4.2분 | 2026-05-11 | 기타 | 음악 | 설명 | 206/206 |
| 950 | [Lofi Summer Vibes 🌊 Seaside Coffee & Relaxing Lofi for a Se…](https://www.youtube.com/watch?v=ovS27OGTajs) | Little Lofi C… | 26,000 | 453,690 | 17.4 | ×52.4 | 2,623.8 | 205.8분 | 2026-04-30 | 11. 힙합·R&B·EDM | 음악 | 설명 | 112/112 |
| 951 | [[외모지상주의 BGM] Jekyll (Edit Ver.) ∣ Lookism BGM](https://www.youtube.com/watch?v=qWtQ9DAscjA) | 루트레이블 (ROUTEL… | 13,200 | 230,232 | 17.4 | ×8.0 | 1,280.9 | 4.5분 | 2026-04-23 | 기타 | 음악 | 설명 | 125/126 |
| 952 | [[커버(cover)송] 카페 - "등불" 원곡 : 영사운드 / 밤에 들으면 더 좋은 노래 ∣ 가요 ∣ kp…](https://www.youtube.com/watch?v=v9Vq9kW0NUI) | 음악과 여행 | 26,100 | 454,935 | 17.4 | ×426.8 | 2,538.7 | 4.5분 | 2026-04-24 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 53/53 |
| 953 | [Soft Telugu Songs for your SOUL ♡](https://www.youtube.com/watch?v=17nDtmG2PRU) | With Love Ash… | 36,500 | 632,944 | 17.3 | – | 4,621.4 | 9.8분 | 2026-06-05 | 기타 | 플레이리스트·모음 | 설명 | 23/23 |
| 954 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 올해 내내 듣게 될 시원한 청량팝 모음🐶🩵 첫 곡부터 기분 좋아지는 여름 플리👙 카페음…](https://www.youtube.com/watch?v=DwlYkGuixsw) | OOOffi | 25,600 | 443,427 | 17.3 | ×15.8 | 3,070.5 | 657.9분 | 2026-05-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 59/59 |
| 955 | [🌿🍁 미사리에서 듣는 최고의 가을 카페음악｜2026 가을 감성 플레이리스트 ☕ 마음이 편안해지는 음악](https://www.youtube.com/watch?v=sDs-SBQlNCw) | Cozy Cafe Mus… | 3,870 | 66,514 | 17.2 | ×8.1 | 1,687.5 | 62.6분 | 2026-09-10 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 0/13 |
| 956 | [샹송이 이렇게 까지 좋은줄 몰랐습니다 ∣ 너무 좋아서 아침부터 듣게 되는 7080 올드팝 ∣ 감성이 터진](https://www.youtube.com/watch?v=KFu4Y2j652w) | Midnight Melo… | 28,000 | 478,857 | 17.1 | ×133.9 | 2,818.5 | 119.9분 | 2026-05-03 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 157/157 |
| 957 | [Mind Relaxing Music – Peaceful Flute Meditation Music, Esca…](https://www.youtube.com/watch?v=bx_QXhMb5xM) | CLASSICAL FUS… | 19,000 | 320,438 | 16.9 | ×62.4 | 2,283.1 | 40.1분 | 2026-06-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 76/75 |
| 958 | [Morning Anxiety Calms ∣ Prana Vihara — Bansuri 432Hz for Cl…](https://www.youtube.com/watch?v=Ae8IzAhMcYY) | Shunya SoundS… | 20,400 | 342,230 | 16.8 | ×306.9 | 1,974.2 | 34.2분 | 2026-04-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 189/189 |
| 959 | [You Are Already Connected 🌿​ Return to Source](https://www.youtube.com/watch?v=ZvfaZlFIzqY) | Zaly Soul | 20,700 | 346,623 | 16.8 | ×53.6 | 1,928.9 | 26.8분 | 2026-04-23 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,232/1,229 |
| 960 | [[눈물주의]세상에서 가장 슬픈 노래 😢 어미의 한 [판소리]💔The Saddest Song Ever Wri…](https://www.youtube.com/watch?v=DhredFI94dc) | Nana Music | 10,000 | 165,979 | 16.6 | ×195.7 | 1,886.6 | 6분 | 2026-07-24 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 99/103 |
| 961 | [TAO — 道 ∣ Japanese Zen Music for Deep Meditation & Inner Ca…](https://www.youtube.com/watch?v=SepvquaFWAY) | Hikari Zen | 27,300 | 452,568 | 16.6 | ×96.2 | 2,728.4 | 237.6분 | 2026-05-07 | 1. 수면·명상·힐링 | 음악 | 설명 | 107/107 |
| 962 | [[연속듣기] 눈물 나게 가슴 뭉클한 옛날 노래 45곡 🎵 세월이 흘러도 잊을 수 없는 추억의 트로트 🎵 흘…](https://www.youtube.com/watch?v=xj8SEIUhbjY) | 추억의 K트롯 | 14,700 | 243,138 | 16.5 | ×65.5 | 1,694.8 | 132.4분 | 2026-05-29 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 78/78 |
| 963 | [Instrumental Christian Piano for Focus ∣ 2 Hours Worship Pi…](https://www.youtube.com/watch?v=q7ooKtFTYMk) | In His Presen… | 17,200 | 284,066 | 16.5 | ×25.6 | 1,974.4 | 121.4분 | 2026-05-29 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 16/16 |
| 964 | [The Little Forest Concert Vol.3 🌿 ∣ Warm BGM for Reading, S…](https://www.youtube.com/watch?v=_zmbIUADeMw) | 그루잠 Gurujam | 27,400 | 451,889 | 16.5 | ×63.1 | 6,808.2 | 32.6분 | 2026-08-14 | 3. 공부·집중·작업 | 음악 | 설명 | 71/70 |
| 965 | [딸에게 한 번도 하지 못했던 말... 오늘 이 노래로 전합니다 / 내딸아 / 도연스님 / 만복감성트롯 / …](https://www.youtube.com/watch?v=k5oAx-igPIU) | 만복 낭만트롯 | 2,500 | 41,094 | 16.4 | ×15.8 | 513.4 | 5분 | 2026-08-01 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 30/30 |
| 966 | [Deep meditation ∣ use headphones for better results ∣ mindf…](https://www.youtube.com/watch?v=HR4UkS5H-kk) | Modern Yogii | 711 | 11,629 | 16.4 | – | 71.0 | 15.2분 | 2026-05-09 | 1. 수면·명상·힐링 | 음악 | 설명 | 7/7 |
| 967 | [[𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 정병 제대로 터져버린 멘헤라남 플리](https://www.youtube.com/watch?v=N2zEbM5dIH4) | 안평화 | 17,100 | 276,938 | 16.2 | ×9.8 | 6,190.0 | 15.6분 | 2026-09-05 | 기타 | 플레이리스트·모음 | 없음 | 168/174 |
| 968 | [🍉여름에 듣기 좋은 카페 음악 ☕ 상쾌한 여름 바닷가 처럼 기분좋은 Playlist ∣ 중간 광고 없음 ∣…](https://www.youtube.com/watch?v=ZSVnVZ0-ROg) | 오늘의 멜로디 Today… | 19,700 | 318,365 | 16.2 | ×65.0 | 1,997.6 | 120.4분 | 2026-05-13 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 57/57 |
| 969 | [너에플리 리메이크 모음｜CHAPTER 1](https://www.youtube.com/watch?v=iSJD2jZwB8E) | 너에플리 | 28,600 | 455,597 | 15.9 | – | 3,191.5 | 34분 | 2026-05-30 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 184/184 |
| 970 | [[평안 찬송] 마음에 평안과 기쁨을 채워주는 은혜의 찬송가 모음 ∣ 들을수록 마음이 편안해지는 찬송가 연속…](https://www.youtube.com/watch?v=GaBxDi7Eg3M) | 주님곁에 | 18,700 | 297,563 | 15.9 | ×6.7 | 3,994.1 | 71.2분 | 2026-08-06 | 15. CCM·찬양·국악… | 커버·직접 부른 노래 | 설명 | 277/281 |
| 971 | [[찬송가 연속듣기] 마음이 복잡할 때 듣는 잔잔한 찬송가 20곡 ∣ 잠들기 전 평안을 주는 찬양 메들리 (…](https://www.youtube.com/watch?v=Tt9qwuoMPtI) | 골방 찬양 | 26,000 | 413,281 | 15.9 | ×3.9 | 2,693.4 | 246.6분 | 2026-05-19 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 622/631 |
| 972 | [【あつ森BGM】夜のリラックスタイム🌙 心落ち着くLo-fi Chill Hop & ASMR｜作業・勉強・睡眠用](https://www.youtube.com/watch?v=YgEA5Ow6mk4) | Chill Mori BGM | 29,300 | 462,728 | 15.8 | ×5.3 | 2,691.6 | 180.1분 | 2026-05-01 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 51/51 |
| 973 | [🎵그냥 틀어놨는데 눈물이 났네요...주님은 다 아시죠ㅣ은혜로운 찬양모음 ㅣCCM플레이리스트 ㅣ위로CCM ㅣ…](https://www.youtube.com/watch?v=aY-zdL2QUBk) | 평화로운음악 찬양카페 | 12,900 | 201,743 | 15.6 | ×23.9 | 1,183.7 | 36.8분 | 2026-05-02 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 257/257 |
| 974 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 가을은 이런 노래 들으려고 있는 거잖아🍃 🚲아침부터 설레는 느좋 팝송.zip🎧 카페음악…](https://www.youtube.com/watch?v=h03aGRBo6m8) | OOOffi | 25,600 | 399,692 | 15.6 | ×14.2 | 5,928.7 | 631.4분 | 2026-08-13 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 42/47 |
| 975 | [[PLAYLIST] 비 오는 날 계속 듣게 되는 발라드 7곡 ☔ ∣ 감성발라드 · 사랑노래 · 여름 플레이…](https://www.youtube.com/watch?v=fG0GudU56S0) | 뮤직앤라이트 Music&… | 8,640 | 134,693 | 15.6 | ×19.1 | 1,265.5 | 27.9분 | 2026-07-05 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 112/112 |
| 976 | [국악딴따라 노래모음｜30곡 연속듣기](https://www.youtube.com/watch?v=VctWdCriD_k) | 국악딴따라 | 35,000 | 543,969 | 15.5 | ×11.0 | 10,915.8 | 91.7분 | 2026-08-31 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 344/361 |
| 977 | [[Playlist] 마음이 편안해지는 힐링 피아노 ∣ Healing Piano Music for Stres…](https://www.youtube.com/watch?v=o0F2bvcNLMc) | Piano Haven | 5,100 | 79,163 | 15.5 | ×17.3 | 451.4 | 194.8분 | 2026-04-27 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 16/16 |
| 978 | [[외모지상주의 BGM] Jekyll & Unconscious 3 ∣ Lookism BGM](https://www.youtube.com/watch?v=7FcjatxdDXo) | 루트레이블 (ROUTEL… | 13,200 | 203,699 | 15.4 | ×7.1 | 1,342.3 | 5.7분 | 2026-05-21 | 기타 | 음악 | 설명 | 126/126 |
| 979 | [Playlist ∣ 틀자마자 기분 좋아지는 힙합 그루브 😎 ∣ GROOVE · JAZZHOP ∣ 카페 · …](https://www.youtube.com/watch?v=5ThjSEl5Dvs) | PoponWave | 23,000 | 354,075 | 15.4 | ×23.9 | 1,996.0 | 223.3분 | 2026-04-25 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 121/121 |
| 980 | [ボサノバ カフェ 朝カフェ｜気分が晴れる心地よい女性ボーカル リラックス音楽 海の見えるカフェ（作業用BGM・波音）（…](https://www.youtube.com/watch?v=UJ00ifFN3jQ) | Relax Lofi Li… | 33,400 | 508,992 | 15.2 | ×58.4 | 3,254.1 | 180.3분 | 2026-05-16 | 3. 공부·집중·작업 | 음악 | 설명 | 53/52 |
| 981 | [매일 듣기 좋은 편안한 클래식🌿∣행복한 힐링 클래식 음악☕∣클래식 명곡 18곡 모음🎵](https://www.youtube.com/watch?v=DTVWGGI7nKE) | 클래식라이프Classic | 23,600 | 358,433 | 15.2 | ×54.1 | 2,711.1 | 68분 | 2026-06-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 99/99 |
| 982 | [가장 편안하고 깊은 잠에 빠지게 만드는 부드러운 빗소리 ASMR ∣ 수면유도 백색소음](https://www.youtube.com/watch?v=qOwxf0IAk_E) | Cozy Rainy Da… | 9,320 | 141,559 | 15.2 | ×18.5 | 1,524.9 | 360분 | 2026-07-19 | 1. 수면·명상·힐링 | 자연 소리·백색소음 | 설명 | 27/30 |
| 983 | [지금 꼭 들으세요 🙏 아들 일이 잘 풀립니다 ∣ 경주 불국사의 기도 음악 #불교음악 #자녀기도노래](https://www.youtube.com/watch?v=QmfOTgF-Akw) | 연등 아래서 | 11,300 | 170,960 | 15.1 | ×34.2 | 1,027.0 | 35.6분 | 2026-05-06 | 기타 | 음악 | 설명 | 4,056/4,083 |
| 984 | [Easy Listening Music for Relaxation, Study, Work & Stress R…](https://www.youtube.com/watch?v=W-QDYTQch9c) | Luxenza Music | 4,610 | 69,303 | 15.0 | – | 588.4 | 18.6분 | 2026-06-24 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 2/2 |
| 985 | [Rumi Sufi Healing Music for Anxiety Relief & Inner Peace ∣ …](https://www.youtube.com/watch?v=Whuol6tvJ5w) | Whispering Sp… | 4,360 | 65,489 | 15.0 | ×19.7 | 1,458.0 | 88.1분 | 2026-09-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 5/5 |
| 986 | [[커버송 모음 50곡] (중간 광고 없어요^^:) /그 시절 추억의 노래 50곡/ 구독자 선정곡 1위~50…](https://www.youtube.com/watch?v=av1_naa9D2o) | 음악과 여행 | 26,100 | 388,855 | 14.9 | ×364.8 | 4,848.7 | 214.9분 | 2026-08-01 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 238/240 |
| 987 | [ボサノバ カフェ 朝カフェ｜優しい風と海に癒される女性ボーカル リラックス音楽 海カフェ（作業用BGM）（3時間）](https://www.youtube.com/watch?v=Q-Jys6HQ_gg) | Relax Lofi Li… | 33,400 | 496,346 | 14.9 | ×57.0 | 2,773.9 | 180.6분 | 2026-04-24 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 84/82 |
| 988 | [Cafe Reggae 🌴 Chill Island Vibes ∣ Relaxing Reggae Music fo…](https://www.youtube.com/watch?v=407QqF8EBko) | AI IRIE FM | 39,500 | 585,361 | 14.8 | ×29.1 | 3,488.1 | 61분 | 2026-05-05 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 129/129 |
| 989 | [African Healing Music ∣ Zulu Voices for Anxiety Relief & Em…](https://www.youtube.com/watch?v=Nt0so0uLUoI) | africavoices | 4,770 | 70,663 | 14.8 | ×39.8 | 1,263.7 | 92.4분 | 2026-08-25 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 22/22 |
| 990 | [💎 "신이내린 목소리네요..." 100년에 한번 있을까 말까 한 희귀한 음색 ㄷㄷ;; 귀한 노래만 엄선 ∣…](https://www.youtube.com/watch?v=5vdkZXq8IVY) | 7080사랑해요 | 33,500 | 489,379 | 14.6 | ×75.7 | 3,341.2 | 68.1분 | 2026-05-26 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 358/358 |
| 991 | [여름 바닷가 테라스카페 커피한잔 너무좋다 ∣Vol.177∣ 7080 라디오 l 올드팝송 명곡 ∣ Coffe…](https://www.youtube.com/watch?v=NczlNLq6beY) | moka melody | 14,600 | 212,684 | 14.6 | ×10.6 | 1,594.4 | 661.1분 | 2026-06-08 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 77/77 |
| 992 | [BGMで巡る東京ディズニーランド&ディズニーシー 【総集編 2 】](https://www.youtube.com/watch?v=PQH90HnjyO4) | ネンサウンド | 37,600 | 533,500 | 14.2 | ×3.8 | 3,074.3 | 240.1분 | 2026-04-29 | 기타 | 정보·해설 | 설명 | 52/51 |
| 993 | [눕자마자 바로 기절 숙면 빗소리, [중간광고없음]10분후 검은화면, "머리 대자마자 5분 만에 기절했어요"…](https://www.youtube.com/watch?v=MGtgljKRiaI) | 빗소리 자장가 Rain … | 22,300 | 314,232 | 14.1 | ×22.6 | 2,332.7 | 420분 | 2026-06-07 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 54/54 |
| 994 | [기분전환 200%🔥 도파민 터지는, 신나는 노래들🎧 ∣ EDM ∣ Playlist ∣ 클럽음악 ∣ 노동요 …](https://www.youtube.com/watch?v=Tr5-cBvP22g) | DJ Corgi | 13,300 | 186,278 | 14.0 | ×20.6 | 1,281.0 | 150.8분 | 2026-05-27 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 31/31 |
| 995 | [Relaxing Healing Music for Stress, Anxiety, and Depression …](https://www.youtube.com/watch?v=Pxc3SMtKGPo) | Clara Monica … | 3,500 | 48,846 | 14.0 | ×1.5 | 1,022.1 | 25.3분 | 2026-09-02 | 1. 수면·명상·힐링 | 음악 | 설명 | 18/18 |
| 996 | [[Playlist]공간의 분위기 채우는☕️[중간광고없음]카페 매장 음악 🎧그냥 틀어두세요, 차 마실 때, …](https://www.youtube.com/watch?v=kqvHu52KHmQ) | BGMBUCKS | 19,800 | 275,629 | 13.9 | – | 1,698.8 | 69.3분 | 2026-05-11 | 4. 카페·매장·라운지 | 연주 | 설명 | 82/82 |
| 997 | [Garbh Sanskar Deep Sleep Music 🌙 शांत संगीत ∣ Pregnancy Rel…](https://www.youtube.com/watch?v=r-WZM4San-c) | Swarmaa | 16,200 | 224,152 | 13.8 | ×518.9 | 1,609.5 | 5.5분 | 2026-06-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 39/39 |
| 998 | [주부들의 휴식 시간을 채워줄 팝송 Best 100 ∣ EverPop 명곡팝 컬렉션 ∣ 올드팝송 ∣ 7080…](https://www.youtube.com/watch?v=D4H7ItMDIGU) | 추억의 올드팝 EverP… | 15,800 | 216,181 | 13.7 | ×9.7 | 1,659.2 | 117.5분 | 2026-06-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 57/57 |
| 999 | [💃🏼노동요 들으면서 파라파라나 춰야겠다ㅣK-POP PLAYLISTㅣRESCENE, AESPA, CORTIS…](https://www.youtube.com/watch?v=uAE7TcPSJn0) | Tezz Boyz 서테즈… | 38,900 | 532,154 | 13.7 | ×61.4 | 4,617.4 | 76.1분 | 2026-06-27 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 23/23 |
| 1000 | [매일듣는 편안한 클래식 음악🎵∣🌿힐링 클래식 명곡 모음 #클래식 #클래식 음악 #편안한 클래식](https://www.youtube.com/watch?v=ek_Tc24cziw) | 클래식라이프Classic | 23,600 | 321,580 | 13.6 | ×48.6 | 1,889.6 | 55.6분 | 2026-05-03 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 64/65 |
| 1001 | [☀️108𝐓𝐈𝐌𝐄𝐒 Activate High Intelligence: Gayatri Mantra Medit…](https://www.youtube.com/watch?v=_7EQF3GWDIM) | Inner Harmony… | 24,500 | 333,528 | 13.6 | ×100.3 | 1,889.1 | 60분 | 2026-04-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 117/117 |
| 1002 | [⠀](https://www.youtube.com/watch?v=mDkyPzypfuo) | islistening | 32,400 | 437,704 | 13.5 | ×7.5 | 3,585.7 | 21.9분 | 2026-06-20 | 기타 | 플레이리스트·모음 | 설명 | 125/127 |
| 1003 | [새벽에 듣기좋은 메이플 로파이 재즈 ∣ 1시간 작업·공부 음악](https://www.youtube.com/watch?v=N5AE0jDAY2o) | DOKANG | 20,400 | 271,448 | 13.3 | ×24.3 | 1,708.1 | 63.9분 | 2026-05-14 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 155/156 |
| 1004 | [[Masterpiece Series] Albinoni Adagio – 4 Variations Songs o…](https://www.youtube.com/watch?v=OFfc765eTgY) | WilliamPoetic… | 40,600 | 539,505 | 13.3 | ×45.2 | 3,085.8 | 17.4분 | 2026-04-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 781/781 |
| 1005 | [“프린세스 티니핑송“ 피아노 커버(Princess Teenieping Song Piano Cover)](https://www.youtube.com/watch?v=BS-GSU9dLqk) | MUJINS 뮤진스 | 19,200 | 253,449 | 13.2 | ×32.9 | 1,850.1 | 6.9분 | 2026-06-05 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 49/50 |
| 1006 | [아침까지 기절 숙면 잠 잘 오는 빗소리, [중간광고없음]10분후 검은화면, "눈 뜨니 개운한 아침이에요" …](https://www.youtube.com/watch?v=pkUgoZ7h_2M) | 빗소리 자장가 Rain … | 22,300 | 290,463 | 13.0 | ×20.9 | 1,830.2 | 420분 | 2026-05-14 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 40/40 |
| 1007 | [【Nhất Định Phải Nghe Dành Cho Người Mất Ngủ!】Nhạc Piano Nhẹ…](https://www.youtube.com/watch?v=1-OgDgY_peU) | Nhạc Ngủ Thư … | 48,900 | 622,503 | 12.7 | ×18.8 | 4,871.3 | 182.7분 | 2026-06-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 184/182 |
| 1008 | [Faith: You Were Never Walking Alone ∣ Heavenly Meditation M…](https://www.youtube.com/watch?v=_psuP3ukwOY) | Healing Ether | 45,400 | 557,374 | 12.3 | ×59.5 | 3,437.1 | 71.2분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 376/376 |
| 1009 | [우연히 들었는데 첫 곡부터... 너무 좋다 ∣ 7080 추억의 올드 팝송 모음 Old Pop Song Pl…](https://www.youtube.com/watch?v=ktav8W-fW8I) | theoldpopsong | 40,800 | 483,534 | 11.8 | ×29.0 | 2,740.9 | 58.3분 | 2026-04-26 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 287/287 |
| 1010 | [Kiven Mukhre Ton Nazraan ∣ Ustad Nusrat Fateh Ali Khan ∣ Da…](https://www.youtube.com/watch?v=PMqkvHE1cm0) | XAN | 24,700 | 292,441 | 11.8 | ×29.7 | 1,979.4 | 4.9분 | 2026-05-25 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 158/158 |
| 1011 | [가을이 오면... 커피향이 가득한 카페에서 듣고 싶은 음악](https://www.youtube.com/watch?v=4lPZuU2kCbA) | EverOldies | 44,800 | 529,822 | 11.8 | ×64.7 | 11,411.2 | 96.9분 | 2026-09-03 | 4. 카페·매장·라운지 | 음악 | 설명 | 292/316 |
| 1012 | [Awit ng Paghahangad by Bukas Palad Music Ministry ∣ Senti P…](https://www.youtube.com/watch?v=5yDRTUMvk3I) | Clyde Pianist… | 12,000 | 141,394 | 11.8 | ×24.2 | 1,246.4 | 7.2분 | 2026-06-28 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 102/102 |
| 1013 | [Mama Said ∣ Ogryn Chain Gang Blues Work Song ∣ Warhammer 40…](https://www.youtube.com/watch?v=H6yrpYWMyRs) | Solar Void | 20,800 | 245,096 | 11.8 | ×26.1 | 1,450.9 | 6분 | 2026-05-04 | 2. 자연 소리·백색소음 | 음악 | 설명 | 395/395 |
| 1014 | [정서안정과 고운 마음을 위한 잔잔하고 아름다운 음악 l 어린이집 유치원 교실 편안한 배경 음악](https://www.youtube.com/watch?v=ONTpCdvC9mo) | 조이멜로디 JOY MEL… | 21,600 | 249,862 | 11.6 | ×26.5 | 1,492.5 | 82.3분 | 2026-05-05 | 기타 | 음악 | 설명 | 0/0 |
| 1015 | [싱그러운 여름 아침, 꽃향기가 스며드는 기분좋은 카페음악 ∣ 계속 듣게 되는 감성팝송 ∣ Old Pop P…](https://www.youtube.com/watch?v=EnD2m1z3fkM) | 선율향기 | 11,500 | 131,924 | 11.5 | ×39.6 | 1,019.4 | 91.5분 | 2026-06-12 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 72/72 |
| 1016 | [한 줌 흙으로 돌아가는 길 ∣ 황혼길의 깨달음 국악 판소리트로트](https://www.youtube.com/watch?v=Vb3VooJUgyk) | Nana Music | 10,000 | 114,613 | 11.5 | ×135.2 | 956.8 | 7.6분 | 2026-06-22 | 9. 가요·발라드·트로트 | 음악 | 설명 | 106/110 |
| 1017 | [숲에서 쉬는 효과🌳머리가 맑아지는 치유명상음악 ∣ 3시간, 힐링음악, 명상음악 ∣ Relaxing Musi…](https://www.youtube.com/watch?v=yq-lSVEu7U0) | 살구사운드 SalguSo… | 10,700 | 122,181 | 11.4 | ×9.9 | 4,307.6 | 191.9분 | 2026-09-21 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 43/46 |
| 1018 | [[𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁] 인스타에서 한번쯤 들어본 느@좋 플리](https://www.youtube.com/watch?v=4qcGtkqrfMk) | 프리다앤 / FRIDA-… | 41,500 | 473,086 | 11.4 | ×49.6 | 2,800.0 | 60.8분 | 2026-05-04 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 19/19 |
| 1019 | [The Odyssey - Odysseus (EPIC Piano Cover)](https://www.youtube.com/watch?v=jtUq7gMr-7k) | Laurie Théber… | 46,000 | 522,433 | 11.4 | ×39.2 | 5,630.2 | 6.3분 | 2026-07-19 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 192/192 |
| 1020 | [🔥한 번 들으면 멈출 수 없는 역설적 감성🔥 락트롯 ∣ 가슴속 응어리를 뻥~ 뚫어버리는 사이다 보컬 ∣ 도…](https://www.youtube.com/watch?v=LmEOZx2IH9M) | 노래마실 [ Music … | 2,790 | 31,490 | 11.3 | ×58.6 | 256.1 | 4.3분 | 2026-06-19 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 19/19 |
| 1021 | [Rod Wave - It Will All Work Out - (Official Music Video)](https://www.youtube.com/watch?v=OHYv2zYBdfU) | Street Empire… | 1,570 | 17,717 | 11.3 | ×27.5 | 136.5 | 13분 | 2026-06-12 | 기타 | 한 곡 | 없음 | 5/5 |
| 1022 | [🌈Album Preview ∣ Find the Full Album in the Playlist ∣ Cele…](https://www.youtube.com/watch?v=2qh-NuD0YMs) | Calm Music & … | 3,470 | 39,070 | 11.3 | ×356.8 | 1,244.5 | 4.8분 | 2026-09-18 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 1/1 |
| 1023 | [Enthiran BGM ∣ A.R. Rahman ∣ 80-Piece Symphony Orchestra](https://www.youtube.com/watch?v=swMgOH67TdI) | Australian In… | 32,100 | 347,042 | 10.8 | – | 2,459.5 | 8.5분 | 2026-06-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 486/486 |
| 1024 | [「영화 〈애수〉, 다시 노래가 되다｜세월이 지나도 남는 영화](https://www.youtube.com/watch?v=cIBIrAEYVZM) | 절로 가는 이야기 | 2,560 | 27,576 | 10.8 | ×9.8 | 1,937.2 | 4.6분 | 2026-10-06 | 기타 | 음악 | 설명 | 43/43 |
| 1025 | [【ドッカンバトル】超サイヤ人孫悟空 変身 bgm](https://www.youtube.com/watch?v=nwzLO39prTs) | メガゲン | 21,200 | 222,481 | 10.5 | ×7.9 | 1,446.5 | 10.1분 | 2026-05-19 | 기타 | 음악 | 없음 | 374/374 |
| 1026 | [🌸나훈아 - 무시로 (Blues Remix) – 이 감성 뭐냐… l 🎙️별이트로트](https://www.youtube.com/watch?v=bBz2DSGQSIw) | 별이트로트 | 8,030 | 83,255 | 10.4 | ×26.5 | 480.8 | 4.3분 | 2026-04-30 | 9. 가요·발라드·트로트 | 음악 | 설명 | 29/29 |
| 1027 | [듣자마자 어깨춤 터지는 신명나는 트로트 찬불가 14곡 #불교음악 #트로트찬불가](https://www.youtube.com/watch?v=EYh7Yz748vs) | 연꽃선율 | 21,500 | 221,417 | 10.3 | ×375.9 | 1,375.7 | 61.5분 | 2026-05-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 289/289 |
| 1028 | [슈베르트가 생의 끝에서 남긴 가장 아름다운 노래 ∣ 슈베르트 '세레나데' D.957 (Franz Schub…](https://www.youtube.com/watch?v=15GfRzMd3qw) | 클래식 여행자 (Clas… | 13,400 | 137,880 | 10.3 | ×1.9 | 836.2 | 4.2분 | 2026-05-08 | 기타 | 음악 | 설명 | 38/38 |
| 1029 | [The Throne Room ∣ House of The Dragon Season 3 Episode 2 En…](https://www.youtube.com/watch?v=s2GxTf1Ft4s) | Jeremy Brauns… | 29,300 | 300,246 | 10.2 | ×6.9 | 2,664.1 | 4.1분 | 2026-06-29 | 13. OST·사운드트랙 | 커버·직접 부른 노래 | 설명 | 163/163 |
| 1030 | [2000년대 히트곡 모음 추억의 노동요 playlist](https://www.youtube.com/watch?v=C4rRsOUQMRg) | 플리 말아주는 주모 | 25,800 | 262,530 | 10.2 | ×2.3 | 1,807.8 | 189.9분 | 2026-05-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 322/322 |
| 1031 | [권태 [감성트롯 끝판왕]연속4번재생](https://www.youtube.com/watch?v=07n66F10ofY) | 리듬다방(김리다) | 1,360 | 13,795 | 10.1 | ×28.7 | 104.0 | 12분 | 2026-06-09 | 9. 가요·발라드·트로트 | 음악 | 설명 | 17/17 |
| 1032 | [【ドッカンバトル】超サイヤ人孫悟空 本気 bgm](https://www.youtube.com/watch?v=rr_DEN34wp0) | メガゲン | 21,200 | 213,255 | 10.1 | ×7.6 | 4,107.6 | 10.1분 | 2026-08-29 | 기타 | 음악 | 없음 | 175/170 |
| 1033 | [Pan Flute Healing Music ∣ Sacred Andean Melodies for 2 Hours](https://www.youtube.com/watch?v=zq_vdOfFzlc) | Andean Flute … | 4,970 | 49,711 | 10.0 | ×53.3 | 396.2 | 144.8분 | 2026-06-16 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 13/13 |
| 1034 | [가질수 없는 너(1995) - 뱅크 ∣ Acoustic Cover ∣ 레트로카페](https://www.youtube.com/watch?v=FLzOl-Y5jiw) | 레트로 카페 (Retro… | 11,600 | 115,640 | 10.0 | ×21.8 | 673.6 | 4.6분 | 2026-05-01 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 9/11 |
| 1035 | [Wake Up with Krishna 🌿 Peaceful Dawn Meditation Music](https://www.youtube.com/watch?v=1A7xEA1j_Qg) | Moksha Sounds… | 37,000 | 355,761 | 9.6 | ×57.6 | 2,688.2 | 69분 | 2026-06-09 | 1. 수면·명상·힐링 | 음악 | 설명 | 176/176 |
| 1036 | [Jaxson Blue - Honest Work (Official Music Video)](https://www.youtube.com/watch?v=Sbs0YyDhlDI) | Jaxson Blue | 29,300 | 279,724 | 9.6 | – | 2,097.3 | 4.2분 | 2026-06-08 | 기타 | 한 곡 | 설명 | 73/72 |
| 1037 | [【美しいクラシック60分】思わず聴き入る名曲集｜読書・作業・リラックスBGM｜ショパン・ベートーヴェン・バッハ](https://www.youtube.com/watch?v=Us79QrAAa70) | クラシックの森 – Cal… | 49,300 | 461,220 | 9.4 | ×15.8 | 4,138.1 | 62.6분 | 2026-06-30 | 기타 | 정보·해설 | 설명 | 35/35 |
| 1038 | [농도 99%, 취향 좋은 사장님이 아껴둔 흔하지 않은 카페 플리 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 · Minimal Ca…](https://www.youtube.com/watch?v=PyA6gUmJW34) | Radear | 31,200 | 287,809 | 9.2 | ×14.7 | 1,664.4 | 236.8분 | 2026-04-30 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 96/96 |
| 1039 | [선선한 가을 밤 잠잘때 듣는 메이플 브금 (풀벌래 ASMR ) ∣ 수면유도음악 8시간](https://www.youtube.com/watch?v=mkpa_vCH-Aw) | DOKANG | 20,400 | 187,563 | 9.2 | ×16.8 | 1,312.4 | 480분 | 2026-05-30 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 61/62 |
| 1040 | [Hebt Euch #himmelfahrt #healingmusic #vikingmusic #selbsthe…](https://www.youtube.com/watch?v=QIXGLP6vZgQ) | VikingHealing | 2,610 | 23,771 | 9.1 | ×40.3 | 149.1 | 4분 | 2026-05-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 15/15 |
| 1041 | [아름다운 것도 아파 (Beautiful Things Hurt Too) ∣ 여자 듀엣 감성 발라드 Sad E…](https://www.youtube.com/watch?v=jwUGSmtsSIs) | MusicSong | 7,390 | 66,977 | 9.1 | ×166.6 | 401.4 | 4.4분 | 2026-05-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 43/43 |
| 1042 | [🏡 평생 잊지 못할 내 마음의 고향 ∣ 힐링 트로트 ∣ 혜영스님](https://www.youtube.com/watch?v=Dx4ewFSkxSg) | 혜영스님 ∣ 힐링트로트 | 7,600 | 68,022 | 8.9 | ×11.4 | 648.5 | 5.7분 | 2026-07-07 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 26/26 |
| 1043 | ["카페 음악 때문에 또 왔어요" 단골들이 숨겨두고 듣는 미니멀 팝 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 · Minimal C…](https://www.youtube.com/watch?v=fYmDt5bWDxg) | Radear | 31,200 | 278,433 | 8.9 | ×14.2 | 1,820.3 | 243.6분 | 2026-05-20 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 63/63 |
| 1044 | [중년 남자의 눈물 쏙 빼는 미친 호소력. '님은 먼곳에' (AI커버블루스 락 Ver.)#김추자 #님은먼곳에…](https://www.youtube.com/watch?v=A0SSBzDh-Ew) | 알고보니 혼비백산 | 42,900 | 374,582 | 8.7 | ×40.2 | 2,178.5 | 5.7분 | 2026-05-01 | 14. AI 음악 | AI 음악 | 설명 | 244/245 |
| 1045 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 그대여, -BM](https://www.youtube.com/watch?v=YDESKcB9ppA) | Artist BM | 8,660 | 75,624 | 8.7 | ×2.3 | 1,556.2 | 4분 | 2026-09-01 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 22/23 |
| 1046 | [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 나른 야르한 제이팝 플리](https://www.youtube.com/watch?v=6Kd2P_Pu5Ug) | Nonohara | 1,240 | 10,778 | 8.7 | ×4.9 | 158.9 | 14.7분 | 2026-08-13 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 28/28 |
| 1047 | [One Lifetime Wasn't Enough ∣ Emotional Piano Love Ballad ∣ …](https://www.youtube.com/watch?v=b5N4DQLrfAg) | Soft Emotion … | 13,700 | 116,913 | 8.5 | ×12.4 | 1,105.9 | 6분 | 2026-07-06 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 15/15 |
| 1048 | [너와 걸으며/달달한노래/아련한노래/달콤한노래/잔잔한노래/편안한노래/가을노래/자기전에 듣기좋은 노래/여행갈때…](https://www.youtube.com/watch?v=bzVlQQuegBc) | 황금밴드 / Golden… | 1,880 | 16,032 | 8.5 | ×2.6 | 277.7 | 4.2분 | 2026-08-23 | 9. 가요·발라드·트로트 | 음악 | 설명 | 16/16 |
| 1049 | [텐션폭발! 운동성공! 오늘부터 내 노동요는 이거다!! [90~2000년대] 클럽 리믹스 35곡 [텐션업 플…](https://www.youtube.com/watch?v=t5GX_3shfEw) | 드루와자기 | 19,700 | 165,866 | 8.4 | ×494.4 | 1,472.5 | 125.2분 | 2026-06-29 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 63/63 |
| 1050 | [㉖대한민국 정통 트로트 60선 (Korean Trot 60) ∣ 전설의 거장들이 빚어낸 정통 명곡 메들리 …](https://www.youtube.com/watch?v=75u_o8j9V0s) | 트로트의 맛! | 39,600 | 331,609 | 8.4 | – | 2,006.2 | 188.5분 | 2026-05-08 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 174/176 |
| 1051 | [10. 그리스 이타카, 무화과맛 재즈 ∣ playlist](https://www.youtube.com/watch?v=Nxeex1L0sYU) | dansoonhee | 16,300 | 135,944 | 8.3 | ×13.8 | 1,779.0 | 280.3분 | 2026-08-04 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 74/74 |
| 1052 | [In der Walpurgisnacht brennt mein altes Ich #walpurgisnacht…](https://www.youtube.com/watch?v=jugVBYVn8ag) | VikingHealing | 2,610 | 21,150 | 8.1 | ×35.8 | 122.0 | 4.6분 | 2026-04-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 12/12 |
| 1053 | [This Will Reset Your Nervous System in Minutes ∣ Deep India…](https://www.youtube.com/watch?v=5YnCFwtGK28) | Sacred Mind H… | 8,290 | 66,999 | 8.1 | ×48.0 | 376.8 | 36.6분 | 2026-04-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 40/40 |
| 1054 | [위로와 평안의 찬송 ∣ 지친 당신을 위한 깊은 위로의 찬송가 10곡 (1만 구독자 기념 플레이리스트)ㅣ위로…](https://www.youtube.com/watch?v=bUyzotGJlfs) | Worship Chann… | 21,300 | 172,207 | 8.1 | ×94.5 | 957.8 | 45.6분 | 2026-04-23 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 149/149 |
| 1055 | [Om Namah Shivaya Chanting ∣ Divine Shiva Meditation Music f…](https://www.youtube.com/watch?v=UsiJNIk0F88) | Echoes of Shi… | 1,620 | 13,056 | 8.1 | ×3.5 | 73.5 | 7.3분 | 2026-04-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 16/15 |
| 1056 | [🎵Do You Hear Me… — A Story of Love & Loss ∣ Full Emotional …](https://www.youtube.com/watch?v=BwNZ573NSVs) | HeartEcho AI … | 29,500 | 236,099 | 8.0 | ×36.7 | 1,358.4 | 57.9분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 364/364 |
| 1057 | [432 Hz Reiki Music for Healing and Cleansing Negativity - 2…](https://www.youtube.com/watch?v=auzLrS12AUo) | Reiki Healing… | 20,000 | 159,611 | 8.0 | ×19.2 | 1,415.4 | 20분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 22/21 |
| 1058 | [우리 행복하자 (Let's Just Be Happy) ∣ 미안하단 말보다 우리 행복하자 ∣ KR/ROM/E…](https://www.youtube.com/watch?v=d0jaFafrkkM) | 한그루브 | 50,000 | 389,519 | 7.8 | ×26.5 | 3,479.2 | 5.5분 | 2026-06-30 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 319/319 |
| 1059 | [Odysseus ∣ Epic Orchestral Cover ∣ The Odyssey Ludwig Goran…](https://www.youtube.com/watch?v=Qx1hmx1Fsmc) | Jeremy Brauns… | 29,300 | 227,698 | 7.8 | ×5.3 | 2,461.9 | 8.4분 | 2026-07-19 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 79/79 |
| 1060 | [한여름 밤의 꿈](https://www.youtube.com/watch?v=t87CPyEGmHQ) | 오레 ooree | 18,700 | 144,302 | 7.7 | ×19.2 | 1,126.8 | 119.7분 | 2026-06-14 | 기타 | 플레이리스트·모음 | 설명 | 88/88 |
| 1061 | [Work Music, Deep Focus Music for ADHD Relief and Concentrat…](https://www.youtube.com/watch?v=CQ7p1pOOwrA) | Greenred Prod… | 8,540 | 65,133 | 7.6 | ×22.9 | 455.7 | 9.8분 | 2026-05-30 | 3. 공부·집중·작업 | 음악 | 설명 | 0/0 |
| 1062 | [[Fanmade OST] 하루의 끝에서/이안대군 테마 **21세기 대군부인** 감성 발라드](https://www.youtube.com/watch?v=sf5dMF71cg4) | ycmusic25 | 13,700 | 102,680 | 7.5 | ×163.5 | 618.7 | 4.1분 | 2026-05-07 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 79/79 |
| 1063 | [OUR LADY OF FATIMA HEALING HYMNS ∣ Catholic Prayer Music fo…](https://www.youtube.com/watch?v=kL-iJ_qbbms) | Marian Morning | 35,100 | 261,104 | 7.4 | ×199.8 | 1,631.2 | 183.4분 | 2026-05-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 395/392 |
| 1064 | [🎵 견디고 또 견딘 당신에게 전하는 메시지 ∣ 너의 봄이 온다 - AIIN](https://www.youtube.com/watch?v=9r7SCZtxgLQ) | 박PD 음악다방 | 9,820 | 73,007 | 7.4 | ×24.7 | 529.2 | 5.8분 | 2026-06-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 48/48 |
| 1065 | [playlist ∣ 여름과 가을사이, 내 독서용 브금](https://www.youtube.com/watch?v=zSUHxG9TGeQ) | centralgrocer… | 27,200 | 202,189 | 7.4 | ×14.8 | 2,033.8 | 225.8분 | 2026-07-12 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 50/50 |
| 1066 | [가시리 ∣ 조선힙합(Official Music Video)](https://www.youtube.com/watch?v=_uYBH28d_ys) | 조선힙합 Official | 28,600 | 212,227 | 7.4 | ×28.8 | 1,299.9 | 4.6분 | 2026-05-10 | 11. 힙합·R&B·EDM | 한 곡 | 설명 | 47/46 |
| 1067 | [VITAL ENERGY ∣ 432Hz • Clear Overthinking & Awaken Inner Cl…](https://www.youtube.com/watch?v=8EBBcZFo4PU) | Zen Celesta | 49,000 | 360,102 | 7.3 | ×31.2 | 5,308.7 | 60분 | 2026-08-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 102/101 |
| 1068 | [Playlist 2016 그곳으로](https://www.youtube.com/watch?v=JXJWz7Ky8KA) | 느좋모음집 | 29,100 | 211,851 | 7.3 | ×8.4 | 1,841.8 | 18.2분 | 2026-06-27 | 기타 | 플레이리스트·모음 | 없음 | 75/75 |
| 1069 | [🍂 Cozy September Jazz (NO MID-ROLL ADS) – Warm Piano Music …](https://www.youtube.com/watch?v=zw5ml1zLxPs) | Chill Jazz St… | 24,900 | 181,391 | 7.3 | ×15.8 | 3,950.5 | 376.4분 | 2026-09-04 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 39/39 |
| 1070 | [Samtang Ako May Kinabuhi Pa - Piano Jazz Version ∣ jazz it …](https://www.youtube.com/watch?v=JqWXP8WjhX4) | jazz it back | 7,540 | 54,590 | 7.2 | ×6.8 | 345.1 | 4.2분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 7/7 |
| 1071 | [시작하면 시작된다 ٩(๑❛ᴗ❛๑)۶](https://www.youtube.com/watch?v=gjtaovTAbMU) | 톤톤 tonton | 20,200 | 145,520 | 7.2 | ×22.9 | 1,137.5 | 266.2분 | 2026-06-14 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 72/73 |
| 1072 | [창문으로 여름이 실려오는 브금 𓇼 ⋆.˚](https://www.youtube.com/watch?v=wStibHhXn1A) | 톤톤 tonton | 20,200 | 143,842 | 7.1 | ×22.6 | 846.5 | 250.8분 | 2026-05-03 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 58/58 |
| 1073 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 주황색, -BM](https://www.youtube.com/watch?v=63-irShSXR0) | Artist BM | 8,660 | 61,532 | 7.1 | ×1.9 | 804.7 | 4.2분 | 2026-08-04 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 23/23 |
| 1074 | [푸른 여름 사이로 🌸 여름 감성 피아노 플레이리스트 ∣ BGM ∣ 휴식·힐링·집중](https://www.youtube.com/watch?v=rHuz5RflH24) | Mellow Season | 2,870 | 20,235 | 7.0 | ×2.5 | 228.9 | 135.7분 | 2026-07-23 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 2/2 |
| 1075 | [임재현 - 웃어주지마요 Official MV](https://www.youtube.com/watch?v=L4aOBuPkpLg) | 임재현 Official | 39,100 | 273,847 | 7.0 | – | 2,659.8 | 4.4분 | 2026-07-09 | 기타 | 한 곡 | 없음 | 156/160 |
| 1076 | [🎤 이놈아 나좀 살여줘~ / 트롯가수 창 🎶 사랑도 체력이다 인생 풍자 트롯 ✔️](https://www.youtube.com/watch?v=WFt570kk21o) | 우리인생뮤직 | 19,700 | 137,729 | 7.0 | ×49.9 | 798.1 | 4.1분 | 2026-04-30 | 9. 가요·발라드·트로트 | 음악 | 설명 | 137/137 |
| 1077 | [✨ Музыка восстановления 🕯️ Тибетские поющие чаши для глубок…](https://www.youtube.com/watch?v=hivuH3iFJRw) | МУДРЫЕ МЕДИТА… | 6,810 | 47,452 | 7.0 | ×0.7 | 457.7 | 30.3분 | 2026-07-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 29/29 |
| 1078 | [운동러들이 환장하는 '비트 깡패' 플리 ∣ 파상풍맛 외힙 노동요 playlist](https://www.youtube.com/watch?v=pNmK5x-0bkA) | 플리메이커 | 48,700 | 336,391 | 6.9 | ×7.9 | 2,164.7 | 57.1분 | 2026-05-17 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 142/144 |
| 1079 | [깊은밤 색소폰 Vol.35 ∣ 시원한 파도 휴식 🌊 ∣ 2시간 힐링 색소폰 연주 ∣ Ocean Waves …](https://www.youtube.com/watch?v=1jrUOOVjFpE) | 고향 가는 나그네 | 2,670 | 18,420 | 6.9 | ×5.6 | 209.4 | 128.2분 | 2026-07-24 | 1. 수면·명상·힐링 | 연주 | 설명 | 22/22 |
| 1080 | [김상민 - You ∣ 여성보컬 개사 커버 ∣ 폭발적인 감성 발라드](https://www.youtube.com/watch?v=uCvyMW60AD4) | 연애상황극 | 11,100 | 75,246 | 6.8 | ×42.1 | 450.2 | 4.2분 | 2026-05-06 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 17/17 |
| 1081 | [술탄 오브 더 디스코 - 신나는 음악, 잘못된 인생 Good Beats,…](https://www.youtube.com/watch?v=UMinXZIMfQc) | Sultan Of The… | 39,500 | 264,861 | 6.7 | – | 3,786.0 | 4분 | 2026-08-11 | 기타 | 한 곡 | 설명 | 632/632 |
| 1082 | [☕️ 다시 듣고 싶은 추억의 애창곡 ∣ 유튜브 발라드 애창곡 20곡 연속듣기 ∣ 김광석 임재범 신승훈 이문…](https://www.youtube.com/watch?v=ZJHh-chAUSQ) | Korean Ballad… | 43,700 | 292,814 | 6.7 | ×240.8 | 2,650.9 | 117.5분 | 2026-07-01 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 40/41 |
| 1083 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 요즘 제일 핫한 노동요 다 모아놨어요..🤍 (중간광고없음) 10시간 ∣ 감성힙합 R&B 플…](https://www.youtube.com/watch?v=LFFmtspEl8Q) | 중간광고없음 | 18,700 | 125,103 | 6.7 | ×4.3 | 1,213.0 | 601.7분 | 2026-07-09 | 3. 공부·집중·작업 | 플레이리스트·모음 | 없음 | 10/10 |
| 1084 | [Fall 🍂 5 Minute Autumn Timer with Relaxing Piano Music 🍁 (N…](https://www.youtube.com/watch?v=2PQoOVZmxnY) | Timers Box | 2,920 | 18,927 | 6.5 | ×74.4 | 968.5 | 5분 | 2026-09-30 | 3. 공부·집중·작업 | 음악 | 설명 | 1/1 |
| 1085 | [🍉여름에 듣기 좋은 카페 음악 🌊 여름 바닷가 카페처럼 기분 좋은 Playlist ∣ 중간 광고 없음 ∣ …](https://www.youtube.com/watch?v=SDGqz6SUFKY) | 오늘의 멜로디 Today… | 19,700 | 125,968 | 6.4 | ×25.7 | 775.8 | 121.5분 | 2026-05-10 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 31/31 |
| 1086 | [㉝대한민국 정통 트로트 100선(Vol.1)(Korean Authentic Trot 100) 한 번 틀면 …](https://www.youtube.com/watch?v=PrpsrGzD3Ag) | 트로트의 맛! | 39,600 | 252,719 | 6.4 | – | 1,924.9 | 311.1분 | 2026-06-11 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 201/210 |
| 1087 | [Healing Music ∣ Indian Classical Devotional Meditation ∣ Si…](https://www.youtube.com/watch?v=08mQREpo8HM) | RAGA FUSION | 2,100 | 13,299 | 6.3 | – | 104.4 | 18.5분 | 2026-06-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 10/10 |
| 1088 | [서러워 마라 ∣ 구름 같은 인연이더라](https://www.youtube.com/watch?v=X43yOI7dXDI) | 인생트로트 라운지 | 4,140 | 25,413 | 6.1 | – | 169.2 | 5분 | 2026-05-23 | 기타 | 음악 | 설명 | 13/13 |
| 1089 | [조선힙합🔥연실🔥듣자마자 오늘은 이 리듬🔥오늘의힐링🔥국악힙합🔥노동요🔥퓨전국악🔥Korea Joseon Hip-…](https://www.youtube.com/watch?v=iQkMFMSQVOc) | sisovibe | 2,810 | 17,143 | 6.1 | ×5.5 | 781.3 | 5.2분 | 2026-09-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 24/24 |
| 1090 | [[뮤직비디오] 🎵 사의 찬미 ∣ 원곡 윤심덕 ∣ 감성 리메이크](https://www.youtube.com/watch?v=Au2qy-W1WNA) | 초이스 라이브카페 | 2,160 | 12,645 | 5.8 | ×22.6 | 142.5 | 4.5분 | 2026-07-23 | 4. 카페·매장·라운지 | 한 곡 | 설명 | 6/6 |
| 1091 | [Playlist ∣ 여름, 토마토, 재즈](https://www.youtube.com/watch?v=fl5G97CMAvU) | 야채상회 Vege Mar… | 44,400 | 258,559 | 5.8 | ×17.7 | 2,344.8 | 133.1분 | 2026-07-02 | 7. 재즈·보사노바 | AI 음악 | 설명 | 55/55 |
| 1092 | [Multo by Cup of Joe ∣ Senti Piano Cover ∣ Clyde Pianist ∣ 4K](https://www.youtube.com/watch?v=Sz9HlKCn8Gs) | Clyde Pianist… | 12,000 | 68,346 | 5.7 | ×11.6 | 465.3 | 5.6분 | 2026-05-26 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 44/46 |
| 1093 | [Sanctum of Roots: The Sanctuary That Calls You Back to Your…](https://www.youtube.com/watch?v=Lh-IDUyiSCc) | Healing Ether | 45,400 | 253,074 | 5.6 | ×27.0 | 1,631.0 | 71.2분 | 2026-05-18 | 1. 수면·명상·힐링 | 음악 | 설명 | 55/55 |
| 1094 | [인생 뭐 있어 (In-saeng Mwo It-eo) ∣ 왔다 가는 바람 같은 것이지 ∣ KR/ROM/EN …](https://www.youtube.com/watch?v=h0r9xLYF474) | 한그루브 | 50,000 | 275,219 | 5.5 | ×18.7 | 1,823.1 | 4.1분 | 2026-05-22 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 125/125 |
| 1095 | [✨ Divine Royal Guanyin: Sacred Protection & Healing Music ∣…](https://www.youtube.com/watch?v=5UT5XqVBEfs) | Eternal Frequ… | 7,510 | 40,322 | 5.4 | ×3.6 | 781.1 | 29.6분 | 2026-08-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 62/62 |
| 1096 | [Arknights OST - Battleplan Obliteration ∣ アークナイツ/明日方舟 危機契約 …](https://www.youtube.com/watch?v=cY-y4dU2xTk) | RiverV | 49,500 | 262,962 | 5.3 | – | 2,267.3 | 4.1분 | 2026-06-26 | 기타 | 음악 | 설명 | 95/95 |
| 1097 | [🌿 𝑯𝒆𝒂𝒍𝒊𝒎𝒂𝒍𝒔 ∣ 🧘 숲속 호텔의 저녁 명상 클래스 ∣ 싱잉볼 & 잔잔한 피아노 ∣ Meditati…](https://www.youtube.com/watch?v=GjtPZpv7iKo) | 힐리멀스 | 23,000 | 121,261 | 5.3 | ×2.0 | 1,781.4 | 148분 | 2026-08-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 122/124 |
| 1098 | [노동요로 들으려고 만든 House 하우스 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭](https://www.youtube.com/watch?v=-ExhSbJTkj8) | 노마카세 | 46,200 | 240,960 | 5.2 | ×5.6 | 6,892.8 | 52.1분 | 2026-09-15 | 3. 공부·집중·작업 | 플레이리스트·모음 | 없음 | 143/142 |
| 1099 | [𝙋𝙇𝘼𝙔𝙇𝙄𝙎𝙏 이상한 가을밤 (Halloween)](https://www.youtube.com/watch?v=rSj2Sx4vx5w) | off frame | 3,300 | 17,225 | 5.2 | ×8.3 | 2,187.4 | 15.3분 | 2026-10-12 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 41/41 |
| 1100 | [🙏 기도가 잘되는 팬플룻 찬송가 3시간 ∣ 마음이 평안해지는 독서 · 묵상 · 휴식 음악 ∣ Pan Flu…](https://www.youtube.com/watch?v=QOTgCp4r7fo) | 히솝워십 ∣ Hyssop… | 36,300 | 185,459 | 5.1 | ×11.8 | 1,066.9 | 191.8분 | 2026-04-29 | 15. CCM·찬양·국악… | 긴 한 곡·반복 | 설명 | 290/290 |
| 1101 | [[Playlist] 예의 없는 조선 디바들의 노동요 🌶️💃 #어우동 #신사임당 #장화홍련 #성춘향 #바리공…](https://www.youtube.com/watch?v=2bp_rmtK96o) | 조선노래꾼 | 6,470 | 32,440 | 5.0 | – | 185.4 | 13.7분 | 2026-04-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 60/60 |
| 1102 | [🌙 잠들기 전 듣는 하프 찬송가 3시간 VOL.2 ∣ 마음이 평안해지는 수면 찬송가 · 기도 · 묵상 ∣ …](https://www.youtube.com/watch?v=XqAFJ0UXfNM) | 히솝워십 ∣ Hyssop… | 36,300 | 176,966 | 4.9 | ×11.3 | 1,373.2 | 186.7분 | 2026-06-13 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 376/378 |
| 1103 | [Divine Royal Guanyin: Golden Phoenix Blessing & Healing Mus…](https://www.youtube.com/watch?v=W__4-TezX9M) | Eternal Frequ… | 7,510 | 35,048 | 4.7 | ×3.1 | 785.4 | 32분 | 2026-09-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 68/66 |
| 1104 | [Dopamine Music 🧘‍♂️ मन को शांत करने वाला संगीत ∣ Bansuri & …](https://www.youtube.com/watch?v=h6ERD2c1c0E) | KrishxBeats | 11,700 | 53,464 | 4.6 | ×28.4 | 806.1 | 8.2분 | 2026-08-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 12/10 |
| 1105 | [Relaxing Piano Collection ∣ Best of Tyron James ∣ Passacagl…](https://www.youtube.com/watch?v=KbMFv0FHgrY) | tyron james | 24,900 | 113,237 | 4.5 | – | 1,648.5 | 19.8분 | 2026-08-12 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,221/1,254 |
| 1106 | [Dark Violin Focus Techno 🎻 Deep Work Music for Intense Conc…](https://www.youtube.com/watch?v=lC8EFwtdyyw) | INSTRUMENTAL … | 6,000 | 25,402 | 4.2 | ×18.8 | 220.7 | 17.4분 | 2026-06-27 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 37/37 |
| 1107 | [주옥같은 7080 명곡모음 🎶 7080 내 생애 가장 아름다운 추억 🎶 광고 없는 7080 좋은노래 37곡…](https://www.youtube.com/watch?v=VAQ3RjZh_9w) | Enjoy life | 10,400 | 38,624 | 3.7 | ×281.9 | 492.3 | 16.8분 | 2026-08-02 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 9/10 |
| 1108 | [SABILULUNGAN Version 2🌿 Sunda Instrumental Reggae Chill ∣ R…](https://www.youtube.com/watch?v=xtm29OfGf7w) | BASS_DRUM | 16,700 | 59,847 | 3.6 | ×19.5 | 423.7 | 4.6분 | 2026-06-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 14/14 |
| 1109 | [송골매 - 세상만사 (스토리 뮤직) / 8090명곡/ 감성음악](https://www.youtube.com/watch?v=2AfpfnGCaw4) | 스토리 뮤직 ( Stor… | 6,910 | 24,512 | 3.5 | ×24.9 | 147.3 | 4.7분 | 2026-05-06 | 9. 가요·발라드·트로트 | 음악 | 설명 | 6/6 |
| 1110 | [Mashup Không buông x Tìm em (Hngle) ∣ Alice Piano cover …](https://www.youtube.com/watch?v=Myx39SJ5uQs) | Alice Piano | 20,400 | 72,245 | 3.5 | ×17.8 | 758.6 | 8분 | 2026-07-17 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 24/24 |
| 1111 | [minimalist deep house for elevated concentration](https://www.youtube.com/watch?v=SSCthKXaAZQ) | deep archive | 25,200 | 87,524 | 3.5 | ×8.8 | 639.1 | 148.2분 | 2026-06-05 | 2. 자연 소리·백색소음 | 음악 | 설명 | 16/16 |
| 1112 | [출근길 텐션 끌어올릴 때 듣는 노래 ∣ 국악퓨전 노동요 ∣ 달려](https://www.youtube.com/watch?v=L_l_mIXqCOc) | 저승팝 - 묘령강림 | 9,460 | 30,811 | 3.3 | ×13.2 | 204.2 | 4.9분 | 2026-05-22 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 52/52 |
| 1113 | [우연히 들었는데 이 노래 ... 정말 너무 좋다 ∣ 7080 추억의 올드 팝송 모음 Old Pop Song…](https://www.youtube.com/watch?v=0H6Hqq-H7Y4) | theoldpopsong | 40,800 | 130,324 | 3.2 | ×7.8 | 1,091.3 | 84분 | 2026-06-22 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 109/109 |
| 1114 | [Reason (OST Trái tim mùa thu ) ∣ Alice Piano cover x Synt…](https://www.youtube.com/watch?v=htWfvXUplM4) | Alice Piano | 20,400 | 62,595 | 3.1 | ×15.4 | 761.2 | 10.8분 | 2026-07-30 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 10/10 |

### 자료를 받지 않은 성공 후보 (684개 중 배수 큰 40개 — 웹 화면 탐색 목록에서 승인하면 분석에 들어감, 성공 사례가 이미 채널당 2개인 채널은 뺌)

| 제목 | 채널 | 구독자 | 조회수 | 배수 | 길이 | 업로드 | 주제 묶음 |
|---|---|---|---|---|---|---|---|
| [Raga of Revenge (Extended Version) ∣ DC ∣ Lokesh Kanagraj ∣…](https://www.youtube.com/watch?v=jEOcIJ4B950) | No Username | 663 | 1,653,715 | 2,494.3 | 4.5분 | 2026-06-01 | 기타 |
| [한 시간만](https://www.youtube.com/watch?v=W0sYhOnCJko) | 조선힙합 - Topic | 25 | 248,191 | 2,481.9 | 4.4분 | 2026-09-14 | 11. 힙합·R&B·EDM |
| [ANDAMANAYA with lyrics (Tagalog Female Version)#ChazzyMusic…](https://www.youtube.com/watch?v=MlM2clMwF0s) | Chazzy Music … | 12,800 | 16,422,297 | 1,283.0 | 5.3분 | 2026-05-02 | 기타 |
| [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 제니 노래 모음 ∣ Jennie playlist](https://www.youtube.com/watch?v=Bv5Ed9dWBaw) | 오느레 | 112 | 104,622 | 934.1 | 27.3분 | 2026-08-30 | 기타 |
| [𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐓𝐫𝐞𝐧𝐝𝐢𝐧𝐠 [𝐍𝐨𝐧𝐬𝐭𝐨𝐩 𝐌𝐚𝐬𝐡𝐮𝐩] 𝐁𝐚𝐢𝐫𝐚𝐧 ∣ 𝐒𝐚𝐡𝐢𝐛𝐚 ∣ 𝐁𝐚𝐫𝐬𝐚…](https://www.youtube.com/watch?v=ASasDfNFPAo) | 𝐀𝐄𝐑Ø™ | 1,420 | 1,176,274 | 828.4 | 22.9분 | 2026-09-15 | 기타 |
| [Alok & Alan Walker - Headlights (feat. KIDDO) ∣ Flipside De…](https://www.youtube.com/watch?v=jW-ysI71WY0) | The Flipside | 18,100 | 14,302,930 | 790.2 | 8.4분 | 2026-05-09 | 5. 운동·드라이브·신나는 |
| [HNGLE Playlist Hay Nhất ∣ Tìm Em, Buông, Không Buông, Cô Đơ…](https://www.youtube.com/watch?v=rHNlIOPIdSM) | hiệu ứng đám … | 1,660 | 1,285,472 | 774.4 | 17분 | 2026-07-09 | 기타 |
| [Thodi Der — Farhan Saeed & Shreya Ghoshal (Half Girlfriend)…](https://www.youtube.com/watch?v=x9wfmi3SyRc) | @Lofi_7ff | 2,020 | 1,473,473 | 729.4 | 5.4분 | 2026-07-20 | 8. 로파이·시티팝·칠 |
| [​🌧️ Dard Dilo Ke -[ Mohammed Irfan] Lofi Flip / Slowed + Re…](https://www.youtube.com/watch?v=iCJoTAtGH0Q) | Lofi__dust | 1,890 | 1,338,764 | 708.3 | 6.6분 | 2026-08-06 | 8. 로파이·시티팝·칠 |
| [Sautin Ke Leke[Slowed+Reverb] Awadesh Premi∣ New Song∣∣ Bho…](https://www.youtube.com/watch?v=6yo2grovVA8) | LofiKosh | 779 | 547,375 | 702.7 | 5.8분 | 2026-10-01 | 8. 로파이·시티팝·칠 |
| [Jay Wheeler - Rubio (Official Video)](https://www.youtube.com/watch?v=_6B2s5psSmQ) | JayWheelerVEVO | 6,750 | 4,196,028 | 621.6 | 4.8분 | 2026-05-29 | 기타 |
| [when you are living your DELULU MOMENTS 💗∣ perfect playlist…](https://www.youtube.com/watch?v=qRGQ3ruB7g8) | Shikhaa Thakur | 1,970 | 1,147,726 | 582.6 | 20.8분 | 2026-08-24 | 기타 |
| [Brown Eyes (Acoustic Jazz Soul Version) ∣ Destiny's Child ∣…](https://www.youtube.com/watch?v=SiSiPtkAY3Y) | SoulPH | 1,930 | 936,470 | 485.2 | 4.6분 | 2026-06-25 | 7. 재즈·보사노바 |
| [2026 랜덤플레이댄스🎀 ∣ 다드루와!!💗 ∣ 2026 랜플댄🍌 ∣ 모르는 노래 없을걸? ∣ 최신곡 다 모…](https://www.youtube.com/watch?v=SaUdZK10Hws) | 바나나한 바냐 | 577 | 264,603 | 458.6 | 5.9분 | 2026-04-27 | 10. 팝송·K팝·J팝 |
| [Songs that make you want to dance ~ 2AM party playlist](https://www.youtube.com/watch?v=ClaVtLtnDsY) | hot nights | 3,240 | 1,455,364 | 449.2 | 26.7분 | 2026-06-24 | 기타 |
| [Beautiful October Autumn Forest 4K 🍁 Peaceful Nature Sounds…](https://www.youtube.com/watch?v=7qgQpr-fyTo) | Nature Harmon… | 2,420 | 1,080,956 | 446.7 | 83.2분 | 2026-09-03 | 1. 수면·명상·힐링 |
| [he is obsessed with you — after all this? — dark romance pl…](https://www.youtube.com/watch?v=TUFYkfqHsEI) | obsessed with… | 2,170 | 959,736 | 442.3 | 32.3분 | 2026-07-14 | 기타 |
| [Meraki Alchemy - WILL IT ALL WORK OUT?? (Official Music Vid…](https://www.youtube.com/watch?v=Yh-RDFyFQKg) | MerakiAlchemy… | 0 | 43,002 | 430.0 | 4분 | 2026-04-24 | 기타 |
| [Aesthetic Road Trip Playlist 🌄 Arijit Singh Songs ∣ Calm Vi…](https://www.youtube.com/watch?v=DZIRWgMYL9g) | VibeHaven | 2,590 | 1,110,846 | 428.9 | 27.9분 | 2026-06-18 | 기타 |
| [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 전주만 들어도 심장이 뛰는 애니 OST 플리💿](https://www.youtube.com/watch?v=M16IXOXLGAI) | ASMRuru_루루 | 890 | 339,756 | 381.8 | 58.7분 | 2026-06-12 | 13. OST·사운드트랙 |
| [Noah Kahan - Willing and Able (Official Lyric Video)](https://www.youtube.com/watch?v=2f4gu97XWFg) | NoahKahanVEVO | 29,700 | 10,944,745 | 368.5 | 5분 | 2026-04-24 | 기타 |
| [Chahun main ya naa 🥺💔 Ultimate#lofimusic #trendingsong #vir…](https://www.youtube.com/watch?v=7UzXVqnuKqY) | Midnight Mons… | 2,200 | 809,221 | 367.8 | 5.7분 | 2026-08-03 | 8. 로파이·시티팝·칠 |
| [The Sound of Silence ∣ Like You've Never Felt Before ∣ Blue…](https://www.youtube.com/watch?v=cmRcndB-xE8) | PulsedBlues | 18,700 | 6,535,810 | 349.5 | 5.2분 | 2026-07-20 | 6. 피아노·클래식·연주곡 |
| [Heartbreaking 💔 LoFi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=LOXCRBImgw4) | Sammo lagh of… | 2,670 | 903,087 | 338.2 | 8분 | 2026-08-18 | 3. 공부·집중·작업 |
| [✦ 𝐀 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐜𝐮𝐳 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐨𝐛𝐬𝐞𝐬𝐬𝐞𝐝 𝐰𝐢𝐭𝐡 𝐒𝐨𝐮𝐭𝐡 𝐢𝐧𝐝𝐢𝐚𝐧 𝐝𝐢𝐯𝐚𝐬 ✦](https://www.youtube.com/watch?v=WGnsvuBwsE4) | 𝐏ᝰ.ᐟ | 3,160 | 984,517 | 311.6 | 11.3분 | 2026-05-14 | 기타 |
| [Kotigobba 2 ∣ Salutilave song video ∣ Kannada Movie 2016 ∣ …](https://www.youtube.com/watch?v=tvAFGclCE24) | Mmusicworld46 | 322 | 97,842 | 303.9 | 4.7분 | 2026-07-20 | 기타 |
| [Playlist Hot Lana Del Rey 🎧 ∣ Top Songs Collection](https://www.youtube.com/watch?v=H86JZTaEnHM) | PA Nè | 4,710 | 1,429,899 | 303.6 | 23.3분 | 2026-06-02 | 기타 |
| [🌌 If memories had a soundtrack, this would be it.🤧](https://www.youtube.com/watch?v=pRi7ZNEqlOk) | soul wali vib… | 2,410 | 715,820 | 297.0 | 25.3분 | 2026-07-28 | 13. OST·사운드트랙 |
| [𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩 b**ch](https://www.youtube.com/watch?v=Ev0TvXow-24) | aa | 1,540 | 454,015 | 294.8 | 16.1분 | 2026-08-03 | 기타 |
| [Thodi der [lyrics] Farhan saeed & Sherya ghosal](https://www.youtube.com/watch?v=dg7FXktqe1c) | Chill Beats H… | 1,890 | 554,527 | 293.4 | 5분 | 2026-09-01 | 기타 |
| [Chirodini Adhare Kete Gelo E Jibon(Female Version) ∣Relaxin…](https://www.youtube.com/watch?v=CkslS6ahuyA) | Hasanur Ai so… | 12,100 | 3,520,712 | 291.0 | 5.6분 | 2026-05-02 | 8. 로파이·시티팝·칠 |
| [Đến Khi Nào (Hot Trend) Mặt Trời Ngừng Chiếu ∣ NHỮNG BẢN…](https://www.youtube.com/watch?v=FxUWM0QblFY) | chill out | 4,530 | 1,302,798 | 287.6 | 80분 | 2026-09-16 | 8. 로파이·시티팝·칠 |
| [Tei Ankho Me Bo Jadu Hai (Slowed & Reverb)New Lofi Song](https://www.youtube.com/watch?v=2VQYOk8CJZk) | Ss raj 67 | 5,050 | 1,439,428 | 285.0 | 6분 | 2026-05-13 | 8. 로파이·시티팝·칠 |
| [Just Listen to the Song](https://www.youtube.com/watch?v=GdP7Z11cm3E) | iamkorean | 767 | 208,114 | 271.3 | 45.8분 | 2026-06-21 | 기타 |
| [Ek Mulaqat (Slowed + Reverb) Mashup - Arijit Singh x Jubin …](https://www.youtube.com/watch?v=ZQ4JgVWHPwM) | Lost In Lyrics | 1,090 | 293,659 | 269.4 | 14.7분 | 2026-06-29 | 8. 로파이·시티팝·칠 |
| [ℙ𝕝𝕒𝕪𝕃𝕚𝕤𝕥 : 늙크크들 회춘시킬 애니 플리](https://www.youtube.com/watch?v=H6TQETWqS6I) | 연하네의 쓸만한 플레이리… | 826 | 220,917 | 267.4 | 131.8분 | 2026-08-17 | 기타 |
| [Ishq Risk 🔥 ∣ Ishq ∣ Ishqa Ve ∣ Ishq E Jaan ∣ Sajde ❤️ ∣ Sl…](https://www.youtube.com/watch?v=iOQi_K5ERfg) | SukumusicHindi | 3,390 | 882,165 | 260.2 | 25.4분 | 2026-09-09 | 8. 로파이·시티팝·칠 |
| [김추자 석양 1986년 공연, 원본 영상 오디오 그대로 ∣ 가사 자막 ∣ 이별 감성 발라드](https://www.youtube.com/watch?v=EquV6m5VTdY) | 엄마의 세월 - 한국 발… | 1,110 | 286,983 | 258.5 | 5분 | 2026-07-16 | 9. 가요·발라드·트로트 |
| [Luke’s Diner ∣ Gilmore Girls Ambience ∣ Cozy Acoustic Music…](https://www.youtube.com/watch?v=cT0I4tqsqB8) | Portal to Els… | 3,030 | 777,498 | 256.6 | 124.7분 | 2026-08-25 | 2. 자연 소리·백색소음 |
| [BHOJPURI PLAYLIST 🌼✨ ~{Timestamp}~ @Desi_.Diva12 #music #ae…](https://www.youtube.com/watch?v=GL7Y0gmUzG0) | Desi_.Diva12 | 6,090 | 1,553,546 | 255.1 | 12.8분 | 2026-07-05 | 기타 |

## 1-2. 같은 채널 안에서 — 잘된 영상 vs 평소 영상 (채널 크기·구독층을 뺀 비교)

채널 909곳의 최근 롱폼(7~365일)에서, 그 채널 조회수 중앙값의 ×3 넘은 **잘된 영상 3485개**와 ×0.5~1.5 인 **평소 영상 4098개** (채널당 5개씩). 같은 채널이니 차이는 채널 크기가 아니라 영상(주제·제목·썸네일·길이) 쪽이다.

### 1-2-1. 제목 특징 (잘된 영상 중 비율 vs 평소 영상 중 비율)

| 제목 특징 | 잘된 영상 | 평소 영상 | 차이 | 표시 |
|---|---|---|---|---|
| 숫자가 들어감 | 36% | 33% | +3%p |  |
| 40자 이상 | 85% | 84% | +1%p |  |
| 따옴표·괄호로 강조 | 17% | 17% | +1%p |  |
| vs 비교 | 1.5% | 1.1% | +0%p |  |
| 물음표 ? | 1.4% | 1.7% | -0%p |  |
| 말줄임 …·... | 3.4% | 3.1% | +0%p |  |
| 느낌표 ! | 1.6% | 1.8% | -0%p |  |
| 25자 미만 | 5.8% | 6.0% | -0%p |  |
| 패턴형(공통점·특징·이유·N가지·착각·과정) | 0.1% | 0.2% | -0%p |  |
| 과정·벌어진 일·결말·결국 | 0.1% | 0.2% | -0%p |  |
| 직접·해보니·N년 기록 | 0% | 0.1% | -0%p |  |
| 빚투·신용·미수·레버리지·대출 | 0.1% | 0% | +0%p |  |
| AI | 8.8% | 8.9% | -0%p |  |
| 이유 | 0.1% | 0.1% | +0%p |  |
| 손실 낱말(망하·날린·잃은·반토막) | 0.1% | 0.1% | +0%p |  |
| 노후·퇴직금·은퇴·50~70대 | 0.3% | 0.3% | +0%p |  |
| 사연·오디오북·실화·고백 | 0.1% | 0.1% | +0%p |  |
| 구분 기호(ㅣ·｜·/)로 나눔 | 62% | 62% | +0%p |  |

### 1-2-2. 주제 묶음 (잘된 영상 중 비율 vs 평소 영상 중 비율)

| 주제 묶음 | 잘된 영상 | 평소 영상 | 차이 |
|---|---|---|---|
| 6. 피아노·클래식·연주곡 | 16% | 15% | +1%p |
| 기타 | 22% | 21% | +0%p |
| 10. 팝송·K팝·J팝 | 2.2% | 1.8% | +0%p |
| 12. 커버·노래 부르기 | 3.0% | 2.7% | +0%p |
| 1. 수면·명상·힐링 | 17% | 17% | +0%p |
| 4. 카페·매장·라운지 | 3.9% | 3.7% | +0%p |
| 2. 자연 소리·백색소음 | 2.8% | 2.7% | +0%p |
| 8. 로파이·시티팝·칠 | 9.4% | 9.3% | +0%p |
| 13. OST·사운드트랙 | 1.1% | 1.1% | +0%p |
| 7. 재즈·보사노바 | 2.2% | 2.4% | -0%p |
| 9. 가요·발라드·트로트 | 7.1% | 7.3% | -0%p |
| 14. AI 음악 | 0.9% | 1.1% | -0%p |
| 15. CCM·찬양·국악·동요 | 2.2% | 2.4% | -0%p |
| 11. 힙합·R&B·EDM | 2.2% | 2.5% | -0%p |
| 5. 운동·드라이브·신나는 | 1.7% | 2.1% | -0%p |
| 3. 공부·집중·작업 | 6.6% | 7.5% | -1%p |

### 1-2-3. 제목 낱말 (같은 채널 안 — 잘된 영상에 더 자주 / 덜 나온 말, 합쳐 5번 이상)

| 낱말 | 잘된 영상 | 평소 영상 | 차이 |
|---|---|---|---|
| Best | 3.0% | 1.8% | +1%p |
| song | 1.6% | 0.9% | +1%p |
| playlist | 3.3% | 2.6% | +1%p |
| Relaxing | 8.3% | 7.5% | +1%p |
| of | 4.0% | 3.3% | +1%p |
| Songs | 6.1% | 5.5% | +1%p |
| BGM | 5.0% | 4.3% | +1%p |
| Playlist | 8.0% | 7.4% | +1%p |
| Hits | 1.9% | 1.3% | +1%p |
| Mix | 3.6% | 3.0% | +1%p |
| Collection | 0.9% | 0.4% | +0%p |
| 플리 | 2.2% | 1.7% | +0%p |
| 가을 | 3.0% | 4.6% | -2%p |
| Music | 19% | 20% | -1%p |
| Study | 3.6% | 4.5% | -1%p |
| Rain | 1.3% | 2.0% | -1%p |
| Focus | 3.9% | 4.6% | -1%p |
| 사람 | 0.2% | 0.8% | -1%p |
| Deep | 8.3% | 8.9% | -1%p |
| Piano | 5.5% | 6.1% | -1%p |

- 길이 중앙값: 잘된 영상 58.5분 · 평소 영상 55.9분
- 제목 글자 수 중앙값: 잘된 영상 72 · 평소 영상 72.0
- 타임라인(챕터) 있는 영상: 잘된 영상 29% · 평소 영상 26%

### 1-2-4. 성공 사례와 같은 채널의 평소 영상 (제목 짝 — 썸네일 짝은 5번)

| # | 성공 사례 (채널 평소 대비) | 같은 채널 평소 영상 1 | 같은 채널 평소 영상 2 |
|---|---|---|---|
| 1 | Jay Wheeler, Omar Courtz - De Lejitos (Remix) (Vi… (×161.3) | Jay Wheeler, Kennyy - Corazón De Lego (Offic… (986,185회) | Jay Wheeler, Luar La L, Torrres, Remers - Sh… (513,814회) |
| 2 | 너의 차선 (×98.7) | 한 시간만 (Instrumental) (6,550회) | 형이 말해줄게 (Instrumental) (4,776회) |
| 5 | ขึ้นใจ (3am call) (×714.8) | ขึ้นใจ (3am call) (22,558회) | กี่เหตุผล ( 1000REASONS ) (12,160회) |
| 6 | Veer Hanumana Ati Balwana Ram Ram Ratiyo Re ∣ Arj… (×2,140.5) | Jai Ganesh Jai Ganesh Deva Aarti ∣ Ganpati A… (1,151회) | Peaceful Siya Ram Dhun ∣ सियाराम धुन ∣ Sitar… (1,123회) |
| 7 | Ye Tune Kya Kiya (Slowed + Reverb) 🎧 ∣ Lofi Versi… (×4,094.5) | Late Night Sad Songs Mashup 💔 ∣ Arijit Singh… (1,218회) | Saude Bazi - Lofi ∣ Feel the pain of this so… (1,261회) |
| 8 | झूमका झूलनिया Slowed + Reverb ∣ KhesariLal Yadav … (×738.6) | Le Me Saiya Aa Gai Sari DuniyaChhod KelNew T… (5,000회) | Dheere Dheere Se Meri Zindagi (4K Video) Meh… (6,014회) |
| 9 | Khat navajot Ahuja / BGM THE BEST SONG 🥰#viral (×5,556.4) | AFGHAN JALEBI MASUK FAREBI SLOW MOTION THE B… (133회) | Tu HI MERA THE BEST SONG FEEL THE MUSIC 💝#vi… (121회) |
| 12 | [playlist] 일하다 어깨 들썩이는 케이팝 노동요 ∣∣ 4K MV (×1,612.4) | [PlayList] 무슨 감성이지 (2,427회) | [playlist] 오늘은 그냥 누워 있을래 (2,348회) |
| 13 | When men loves you harder😭🌷 (×177.7) | 𝑷𝒐𝒗 : 𝒋𝒖𝒔𝒕 𝒔𝒍𝒂𝒚𝒚 𝒊𝒕.. (𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 𝒄𝒂𝒖𝒔𝒆 𝒊𝒕𝒔 𝒚𝒐… (24,985회) | They love you beyond your imagination 🌷😭🫣 (66,112회) |
| 14 | DARKHAAST ❤️ ∣ Arijit Singh ∣ Slowed + Reverb ∣ L… (×484.6) | Gehra Hua ❤️ ∣ Official Music Video ∣ Heart … (660회) | Mero Man Lagyo Vrindavan Dham 🙏❤️ ∣ Full Son… (710회) |
| 16 | ℙ𝕝𝕒𝕪𝕃𝕚𝕤𝕥 : 늙크크들 원기 회복시킬 애니 플리 (×1,080.8) | 질주 / 이도형 - 오란고교 사교클럽 [한국판 ED] (1,057회) | [노래방] 질주 / 이도형 - 오란고교 사교클럽 [한국판 ED] (610회) |
| 17 | Cigarettes After Sex — late night playlist (×376.6) | fall in love again ∣ playlist ∣ (4,110회) | songs that feel like a memory ∣ nostalgic pl… (4,145회) |
| 21 | Achhi lagti ho (slowed + reverb ) lofi varsion 🎧 (×346.7) | Tere maste maste do nen ! ( Slowed - tere) (6,001회) | Main Rang Sharbaton Ka [Slowed+Reverb] Lyric… (5,501회) |
| 23 | Kalyani [slowed & Reverb] ∣∣ With Shreya Ghoshal … (×1,978.5) | Sitaare [Slowed & Reverb] ∣∣ Arijit Singh ∣∣… (2,651회) | Lutt Le Gaya [Slowed & Reverb] ∣∣ Dhurandhar… (2,203회) |
| 25 | Tum Ho Toh - Mashup 2026 ∣ Romantic Love Song ∣ B… (×846.3) | Ek Mulaqat x Mohabbat - Mashup 2026 ∣ Romant… (3,212회) | Haara x Itna Tera Intezaar Kiya - Mashup 202… (3,319회) |
| 26 | 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 가을 설레발 플리 (×727.3) | 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 우리가 영원을 말하면 여름이 될거야 (362회) | 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 우주를 줄게 (315회) |
| 28 | 어른여자.mp3 (×1,456.5) | 살며시 눈 뜨면 집 근처 코너를 돌던 아빠 차 안 (409회) | 애니 속 히로인, 출동 준비 완★료 (423회) |
| 29 | uMoya 2.0 (Tycoon Remix) (×15.2) | Open Your Eyes (101,893회) | Unembeza (Extended Mix) (108,242회) |
| 30 | Hey Paaro - Full Song Bgm Raj The Show Man Puneet… (×27.6) | Navagraha ∣ Kan Kanna Salige ∣ HD Song BGM ∣… (13,397회) | Usire Usire Song Video ∣ Kiccha Sudeep ∣ Rek… (14,801회) |
| 33 | 어 난데 여기 핫플이야 (×1,233.8) | 파워워킹 처하자 (750회) | 흔하지 않은 하우스 케이팝 (410회) |

## 2. 주제 — 주제 묶음별 성공 비율 (비교 집단)

주제 묶음 = `tag_rules.toml` TAG_THEMES (제목에서 맞는 글자가 가장 긴 묶음, 없으면 태그). 비교 집단 성공 비율 21% 과 견주어 본다. 영상 15개 미만은 '표본 적음'.

| 주제 묶음 | 영상 | 성공 | 성공 비율 | 배수 중앙값 | 조회수 중앙값 | 성공 사례 # |
|---|---|---|---|---|---|---|
| 13. OST·사운드트랙 | 56 | 20 | 36% | 1.3 | 6,518.0 | 170, 231, 269, 282, 370, 443, 504, 692, 872, 1029 |
| 기타 | 1311 | 465 | 36% | 1.4 | 7,199 | 1, 3, 4, 5, 9, 11, 13, 15, 16, 17, 18, 23, 24, 26, 27, 28, 29, 30, 33, 35, 37, 39, 42, 43, 44, 47, 51, 52, 53, 56, 59, 61, 66, 67, 68, 72, 75, 78, 79, 80, 82, 84, 86, 87, 88, 89, 92, 93, 94, 96, 99, 100, 103, 104, 108, 110, 113, 114, 115, 116, 117, 122, 124, 126, 127, 128, 129, 130, 131, 132, 135, 136, 137, 138, 139, 142, 150, 152, 155, 156, 157, 158, 161, 163, 166, 167, 168, 169, 171, 174, 179, 180, 181, 182, 184, 187, 188, 189, 190, 191, 194, 195, 198, 203, 204, 206, 207, 209, 210, 215, 224, 227, 228, 229, 235, 238, 239, 240, 241, 244, 246, 247, 257, 261, 263, 266, 268, 275, 277, 278, 283, 285, 290, 295, 303, 306, 308, 321, 329, 333, 334, 339, 342, 345, 348, 354, 357, 358, 361, 367, 376, 384, 385, 390, 393, 404, 407, 415, 421, 438, 452, 457, 460, 461, 469, 479, 484, 490, 493, 503, 506, 507, 509, 513, 517, 520, 532, 536, 553, 556, 561, 569, 585, 591, 601, 617, 625, 627, 633, 644, 661, 663, 676, 678, 699, 715, 724, 737, 741, 753, 755, 759, 762, 770, 787, 795, 798, 803, 817, 818, 821, 825, 838, 855, 869, 870, 876, 878, 919, 921, 929, 930, 949, 951, 953, 967, 978, 983, 992, 1002, 1014, 1021, 1024, 1025, 1028, 1032, 1036, 1037, 1060, 1068, 1075, 1081, 1088, 1096 |
| 10. 팝송·K팝·J팝 | 115 | 34 | 30% | 1.5 | 8,321 | 19, 20, 31, 119, 148, 153, 159, 165, 251, 279, 281, 293, 349, 350, 408, 468, 550, 588, 651, 667, 681, 701, 703, 704, 723, 731, 805, 935, 999, 1009, 1046, 1050, 1086, 1113 |
| 5. 운동·드라이브·신나는 | 106 | 29 | 27% | 1.2 | 5,996.5 | 105, 123, 125, 264, 398, 471, 482, 554, 610, 614, 641, 686, 769, 785, 806, 849, 859, 1058, 1094 |
| 8. 로파이·시티팝·칠 | 481 | 116 | 24% | 0.8 | 5,136 | 6, 7, 8, 14, 21, 25, 34, 38, 41, 45, 46, 48, 50, 57, 60, 69, 71, 73, 74, 77, 81, 95, 101, 102, 106, 107, 109, 111, 118, 120, 121, 146, 151, 154, 173, 178, 183, 192, 211, 219, 222, 226, 242, 245, 249, 258, 267, 274, 302, 311, 313, 328, 351, 352, 380, 382, 387, 392, 400, 406, 414, 418, 420, 424, 454, 473, 478, 489, 491, 492, 500, 505, 516, 519, 521, 525, 526, 531, 539, 546, 557, 575, 602, 656, 680, 899, 931, 972, 1003, 1071, 1072 |
| 11. 힙합·R&B·EDM | 167 | 39 | 23% | 0.7 | 7,174 | 2, 134, 237, 253, 326, 652, 729, 739, 780, 819, 879, 898, 916, 918, 950, 1018, 1066 |
| 12. 커버·노래 부르기 | 165 | 38 | 23% | 0.7 | 6,386 | 55, 62, 144, 196, 287, 340, 402, 440, 442, 444, 447, 487, 488, 631, 635, 650, 717, 730, 742, 794, 812, 827, 847, 850, 853, 857, 873, 874, 952, 969, 1010, 1034, 1059 |
| 7. 재즈·보사노바 | 115 | 23 | 20% | 0.5 | 7,521 | 314, 369, 378, 419, 470, 538, 545, 547, 609, 629, 734, 864, 871, 880, 881, 909, 940, 979, 1051, 1091 |
| 2. 자연 소리·백색소음 | 139 | 24 | 17% | 0.8 | 4,800 | 83, 90, 162, 252, 284, 309, 323, 332, 347, 356, 359, 397, 422, 445, 455, 653, 719, 725, 743, 767, 837, 939, 993, 1006, 1013, 1111 |
| 6. 피아노·클래식·연주곡 | 849 | 144 | 17% | 0.5 | 3,095 | 22, 98, 112, 160, 177, 186, 212, 220, 271, 292, 297, 315, 317, 327, 331, 335, 341, 353, 360, 364, 368, 372, 375, 377, 386, 395, 401, 409, 417, 423, 427, 431, 432, 433, 435, 437, 439, 441, 446, 451, 467, 472, 483, 485, 498, 501, 512, 514, 515, 523, 524, 535, 540, 541, 542, 559, 565, 570, 576, 581, 583, 586, 589, 592, 593, 597, 603, 606, 608, 616, 619, 621, 623, 628, 632, 634, 638, 639, 642, 643, 647, 649, 666, 675, 685, 689, 690, 706, 707, 713, 720, 721, 722, 727, 728, 732, 738, 747, 748, 750, 757, 761, 768, 774, 775, 781, 788, 790, 796, 799, 800, 801, 802, 807, 809, 810, 814, 820, 823, 824, 826, 828, 829, 832, 834, 836, 842, 848, 851, 854, 867, 868, 887, 888, 891, 892, 902, 903, 907, 908, 914, 915, 917, 925, 926, 927, 928, 933, 934, 947, 963, 981, 987, 1000, 1004, 1005, 1007, 1012, 1019, 1022, 1023, 1047, 1056, 1069, 1070, 1074, 1092, 1099, 1105, 1106, 1108, 1110, 1114 |
| 4. 카페·매장·라운지 | 213 | 29 | 14% | 0.5 | 2,853 | 10, 40, 63, 85, 193, 199, 200, 208, 213, 214, 221, 225, 250, 270, 312, 365, 371, 383, 396, 410, 450, 465, 495, 511, 530, 560, 566, 571, 572, 579, 618, 640, 646, 657, 670, 695, 697, 736, 758, 776, 779, 793, 858, 861, 889, 900, 911, 955, 968, 988, 991, 996, 1011, 1015, 1038, 1043, 1085, 1090 |
| 14. AI 음악 | 69 | 9 | 13% | 0.2 | 1,922 | 481, 558, 573, 599, 702, 885, 910, 1044 |
| 9. 가요·발라드·트로트 | 371 | 47 | 13% | 0.4 | 1,745 | 64, 149, 175, 218, 232, 233, 276, 280, 286, 299, 301, 319, 343, 344, 355, 425, 448, 464, 474, 518, 537, 578, 580, 587, 620, 624, 637, 648, 660, 665, 671, 672, 674, 682, 687, 698, 709, 710, 712, 718, 744, 746, 751, 783, 792, 804, 811, 816, 822, 839, 860, 862, 884, 923, 936, 941, 942, 944, 945, 946, 956, 962, 965, 975, 986, 990, 998, 1016, 1020, 1026, 1027, 1031, 1041, 1042, 1045, 1048, 1062, 1073, 1076, 1080, 1082, 1107, 1109 |
| 3. 공부·집중·작업 | 417 | 51 | 12% | 0.5 | 2,530 | 12, 70, 133, 140, 143, 145, 164, 197, 217, 230, 255, 259, 260, 265, 272, 273, 294, 298, 318, 322, 336, 374, 391, 411, 413, 429, 434, 449, 453, 486, 508, 534, 544, 548, 549, 552, 555, 563, 568, 582, 584, 595, 598, 605, 607, 611, 615, 630, 654, 655, 659, 683, 694, 700, 711, 735, 745, 763, 764, 773, 784, 791, 843, 844, 845, 863, 883, 895, 938, 954, 964, 974, 980, 984, 994, 1030, 1049, 1061, 1065, 1078, 1083, 1084, 1089, 1098, 1101, 1112 |
| 15. CCM·찬양·국악·동요 | 118 | 13 | 11% | 0.5 | 3,160.0 | 305, 426, 529, 733, 740, 756, 765, 771, 856, 890, 922, 960, 970, 971, 973, 976, 1054, 1100 |
| 1. 수면·명상·힐링 | 1118 | 116 | 10% | 0.5 | 1,607.0 | 32, 36, 49, 54, 58, 65, 76, 91, 97, 141, 147, 172, 176, 185, 201, 202, 205, 216, 223, 234, 236, 243, 248, 254, 256, 262, 288, 289, 291, 296, 300, 304, 307, 310, 316, 320, 324, 325, 330, 337, 338, 346, 362, 363, 366, 373, 379, 381, 388, 389, 394, 399, 403, 405, 412, 416, 428, 430, 436, 456, 458, 459, 462, 463, 466, 475, 476, 477, 480, 494, 496, 497, 499, 502, 510, 522, 527, 528, 533, 543, 551, 562, 564, 567, 574, 577, 590, 594, 596, 600, 604, 612, 613, 622, 626, 636, 645, 658, 662, 664, 668, 669, 673, 677, 679, 684, 688, 691, 693, 696, 705, 708, 714, 716, 726, 749, 752, 754, 760, 766, 772, 777, 778, 782, 786, 789, 797, 808, 813, 815, 830, 831, 833, 835, 840, 841, 846, 852, 865, 866, 875, 877, 882, 886, 893, 894, 896, 897, 901, 904, 905, 906, 912, 913, 920, 924, 932, 937, 943, 948, 957, 958, 959, 961, 966, 977, 982, 985, 989, 995, 997, 1001, 1008, 1017, 1033, 1035, 1039, 1040, 1052, 1053, 1055, 1057, 1063, 1064, 1067, 1077, 1079, 1087, 1093, 1095, 1097, 1102, 1103, 1104 |

## 2-2. 형식(포맷) — 어떤 모양의 영상인가 (제목·채널 이름·태그 낱말로 나눔)

형식 규칙 = `analysis_rules.toml` [format] (위에서부터 먼저 맞는 것 하나, 낱말 규칙이라 거칠다). **성공 사례 몫**은 성공 사례 중 그 형식 비율, **시장 지수**는 3번과 같은 수요 몫 ÷ 공급 몫 (1보다 크면 영상 하나가 평균보다 많이 봄), **같은 채널**은 1-2번의 잘된 영상 중 비율 vs 평소 영상 중 비율. 원인이 아니라 묶음이다.

| 형식 | 비교 집단 영상 (성공 비율) | 배수 중앙값 | 성공 사례 몫 (#) | 시장 영상 · 지수 | 같은 채널 잘된 vs 평소 |
|---|---|---|---|---|---|
| AI 음악 | 172 (9.3%) | 0.4 | 2.9% (69, 112, 149, 276, 296, 301, 412, 481, 558, 573, 599, 635 …) | 48 · 0.1 | 2.6% vs 2.6% |
| 커버·직접 부른 노래 | 295 (23%) | 0.6 | 5.7% (35, 55, 144, 193, 196, 212, 218, 251, 274, 281, 287, 297 …) | 45 · 0.7 | 5.4% vs 5.2% |
| 연주 (직접 연주하는 영상) | 69 (25%) | 0.9 | 1.3% (364, 417, 515, 524, 621, 662, 720, 721, 728, 750, 781, 858 …) | 13 · 0.3 (표본 적음) | 1.0% vs 1.0% |
| 플레이리스트·모음 (여러 곡) | 1817 (28%) | 1.1 | 34% (3, 12, 13, 15, 16, 17, 18, 20, 26, 27, 28, 32 …) | 269 · 0.7 | 32% vs 30% |
| 자연 소리·백색소음 (음악 낱말 없는 제목) | 58 (16%) | 1.2 | 1.0% (323, 347, 422, 445, 462, 653, 743, 797, 982, 993, 1006) | 2 · 0.1 (표본 적음) | 1.1% vs 1.2% |
| 긴 한 곡·반복 (N시간) | 150 (17%) | 0.4 | 3.3% (78, 234, 236, 254, 265, 311, 330, 352, 377, 395, 397, 404 …) | 16 · 0.9 | 3.4% vs 2.9% |
| 한 곡 (뮤직비디오·음원·가사) | 246 (20%) | 0.7 | 3.7% (19, 31, 41, 47, 64, 91, 99, 100, 102, 104, 148, 159 …) | 48 · 6.1 | 3.7% vs 4.3% |
| 음악 (그 밖 모양 — 한 편짜리 BGM 등) | 2738 (16%) | 0.4 | 44% (1, 4, 5, 6, 7, 8, 9, 14, 21, 22, 23, 24 …) | 450 · 0.8 | 46% vs 46% |
| 정보·해설 (그 밖) | 265 (26%) | 1.0 | 4.0% (2, 10, 11, 33, 40, 43, 63, 66, 98, 128, 134, 167 …) | 30 · 1.3 | 4.8% vs 6.1% |

## 3. 수요와 공급 — 찾는 사람에 비해 영상이 적은 곳

### 3-1. 주제 묶음별 (최근 90일 영상 921개 — 채널 크기 상관없음)

수요 몫 = 그 묶음 영상들의 하루 조회수 합 ÷ 전체, 공급 몫 = 영상 수 ÷ 전체. **지수 = 수요 몫 ÷ 공급 몫** — 1 보다 크면 영상 하나가 평균보다 많이 보임(공급이 모자라 보임), 작으면 영상이 넘침. 작은 채널 성공 비율 = 2번 표. 시청자 질문 = 사례 댓글 중 그 묶음 낱말이 든 질문·요청.

| 주제 묶음 | 영상(공급) | 채널 | 수요 몫 | 공급 몫 | 지수 | 영상당 하루 조회수 중앙값 | 작은 채널 성공 비율 | 시청자 질문 |
|---|---|---|---|---|---|---|---|---|
| 기타 | 186 | 133 | 52% | 20% | **2.6** | 11,149.0 | 36% | 0 |
| 8. 로파이·시티팝·칠 | 50 | 46 | 9.9% | 5.4% | **1.8** | 26,407.8 | 24% | 2 |
| 10. 팝송·K팝·J팝 | 42 | 27 | 5.5% | 4.6% | **1.2** | 3,921.0 | 30% | 21 |
| 9. 가요·발라드·트로트 | 62 | 45 | 7.5% | 6.7% | **1.1** | 4,369.5 | 13% | 112 |
| 12. 커버·노래 부르기 | 26 | 18 | 1.8% | 2.8% | **0.6** | 5,545.8 | 23% | 29 |
| 6. 피아노·클래식·연주곡 | 178 | 123 | 9.5% | 19% | **0.5** | 5,193.0 | 17% | 30 |
| 3. 공부·집중·작업 | 79 | 67 | 3.9% | 8.6% | **0.5** | 1,430.1 | 12% | 27 |
| 4. 카페·매장·라운지 | 53 | 37 | 2.6% | 5.8% | **0.5** | 3,756.5 | 14% | 12 |
| 1. 수면·명상·힐링 | 184 | 136 | 4.3% | 20% | **0.2** | 280.1 | 10% | 20 |
| 11. 힙합·R&B·EDM (표본 적음) | 9 | 9 | 0.7% | 1.0% | **0.7** | 1,829.7 | 23% | 3 |
| 7. 재즈·보사노바 (표본 적음) | 11 | 8 | 0.6% | 1.2% | **0.5** | 11,096.3 | 20% | 9 |
| 2. 자연 소리·백색소음 (표본 적음) | 11 | 11 | 0.4% | 1.2% | **0.4** | 3,708.9 | 17% | 2 |
| 13. OST·사운드트랙 (표본 적음) | 8 | 8 | 0.3% | 0.9% | **0.4** | 6,110.1 | 36% | 2 |
| 5. 운동·드라이브·신나는 (표본 적음) | 12 | 11 | 0.3% | 1.3% | **0.2** | 3,744.9 | 27% | 10 |
| 15. CCM·찬양·국악·동요 (표본 적음) | 7 | 7 | 0.1% | 0.8% | **0.2** | 3,994.1 | 11% | 36 |
| 14. AI 음악 (표본 적음) | 3 | 3 | 0% | 0.3% | **0.1** | 193.7 | 13% | 12 |

### 3-2. 검색어별 (탐색·검색 캐시 — 검색어마다 조회수 순 상위 결과)

결과 수 = YouTube 가 알려 준 그 기간 영상 수 추정(공급). 영상당 하루 조회수 = 상위 결과 하루 조회수 합 ÷ 결과 수 (클수록 영상에 비해 찾는 사람이 많음). 큰 채널 비율 = 상위 결과 중 구독자 5만 넘는 채널 (클수록 들어가기 어려움). **작은 채널이 뚫은 비율** = 상위 결과 중 작은 채널(5만 이하)의 성공 영상(×3·1만) 비율 — 클수록 새 채널도 상위에 들 수 있음. 지금 검색어(keywords.txt)가 먼저, 예전 검색어는 '(예전)'.

| 검색어 | 기간(일) | 본 영상 | 결과 수(공급) | 최근 30일 | 조회수 중앙값 | 하루 조회수 중앙값 | 영상당 하루 조회수 | 큰 채널 비율 | 작은 채널이 뚫은 비율 |
|---|---|---|---|---|---|---|---|---|---|
| playlist | 182 | 100 | 2,000,000 | 6 | 2,472,484.5 | 27,237.2 | 1.9 | 11% | 89% (78개) |
| 플리 | 182 | 100 | 1,253,238 | 1 | 550,153 | 4,279.7 | 0.5 | 12% | 88% (80개) |
| study music | 182 | 100 | 2,000,000 | 2 | 2,109,372.0 | 16,154.5 | 1.4 | 15% | 85% (66개) |
| stress relief music | 182 | 100 | 1,247,946 | 4 | 1,226,839.0 | 10,598.9 | 1.4 | 17% | 83% (68개) |
| deep sleep music | 182 | 100 | 1,373,573 | 5 | 1,047,884.5 | 10,258.8 | 1.0 | 19% | 81% (60개) |
| ambient music | 182 | 100 | 1,973,196 | 4 | 867,157 | 6,304.4 | 0.4 | 20% | 80% (62개) |
| lofi | 182 | 100 | 2,000,000 | 1 | 2,120,029.0 | 24,309.2 | 1.7 | 21% | 79% (68개) |
| peaceful music | 182 | 100 | 1,988,001 | 2 | 1,555,898 | 11,035.7 | 0.8 | 24% | 76% (62개) |
| calm music | 182 | 100 | 2,000,000 | 2 | 1,752,928.0 | 13,811.5 | 0.8 | 24% | 76% (56개) |
| focus music | 182 | 100 | 2,000,000 | 2 | 1,135,161.0 | 9,732.3 | 0.7 | 24% | 76% (56개) |
| BGM | 182 | 100 | 2,000,000 | 1 | 532,870.5 | 4,512.2 | 0.9 | 26% | 74% (67개) |
| MeditationMusic | 182 | 100 | 877,295 | 3 | 346,623 | 2,225.1 | 0.4 | 22% | 74% (57개) |
| soothing music | 182 | 100 | 1,548,676 | 2 | 1,179,312.0 | 10,887.0 | 1.1 | 26% | 74% (59개) |
| yoga music | 182 | 100 | 2,000,000 | 0 | 1,737,436 | 12,476.8 | 0.5 | 28% | 72% (34개) |
| calming music | 182 | 100 | 2,000,000 | 2 | 1,343,429.0 | 12,104.6 | 0.7 | 29% | 71% (54개) |
| Sleep Music | 182 | 100 | 2,000,000 | 3 | 1,536,124 | 14,841.7 | 0.8 | 30% | 70% (44개) |
| 힐링음악 | 182 | 100 | 387,758 | 1 | 301,806 | 1,945.7 | 1.0 | 24% | 70% (66개) |
| 감성발라드 | 182 | 100 | 254,101 | 2 | 421,530 | 4,223.3 | 2.2 | 34% | 66% (63개) |
| cafe music | 182 | 100 | 2,000,000 | 4 | 1,125,330 | 11,732.4 | 0.8 | 35% | 65% (50개) |
| chill music | 182 | 100 | 2,000,000 | 2 | 2,341,551 | 23,705.7 | 3.1 | 35% | 65% (46개) |
| 감성음악 | 182 | 100 | 1,090,278 | 5 | 348,129.5 | 2,985.8 | 0.4 | 26% | 63% (59개) |
| relaxing music | 365 | 100 | 1,722,502 | 0 | 3,794,957.0 | 18,777.2 | 1.3 | 38% | 62% (45개) |
| 플레이리스트 | 182 | 100 | 1,520,777 | 8 | 556,135.5 | 5,451.3 | 0.7 | 38% | 62% (57개) |
| work music | 182 | 100 | 2,000,000 | 4 | 279,724 | 2,988.5 | 0.3 | 15% | 61% (48개) |
| relaxation music | 182 | 100 | 1,658,036 | 2 | 1,090,142.5 | 9,833.4 | 0.8 | 40% | 60% (48개) |
| instrumental music | 182 | 100 | 2,000,000 | 3 | 873,512.5 | 8,388.6 | 0.5 | 43% | 57% (43개) |
| healingmusic | 182 | 100 | 516,429 | 6 | 48,733 | 533.3 | 0.2 | 8.7% | 56% (39개) |
| 카페음악 | 182 | 100 | 534,014 | 0 | 275,629 | 1,997.6 | 0.6 | 33% | 56% (53개) |
| relaxing piano | 182 | 100 | 1,363,317 | 9 | 449,805.5 | 4,918.2 | 0.5 | 45% | 54% (46개) |
| RelaxingMusic | 182 | 100 | 1,218,528 | 6 | 802,123 | 8,632.4 | 0.9 | 49% | 51% (44개) |
| piano | 182 | 100 | 2,000,000 | 4 | 953,630.5 | 9,320.2 | 0.9 | 50% | 50% (35개) |
| background music | 182 | 100 | 2,000,000 | 6 | 882,230.5 | 9,646.5 | 0.6 | 51% | 49% (39개) |
| piano music | 365 | 100 | 2,000,000 | 0 | 2,078,967 | 9,343.9 | 0.7 | 52% | 48% (30개) |
| pianomusic | 182 | 100 | 563,594 | 13 | 141,394 | 1,060.7 | 0.3 | 20% | 47% (39개) |
| 명상음악 | 182 | 100 | 542,059 | 2 | 127,668.5 | 982.0 | 0.3 | 17% | 45% (38개) |
| 발라드 | 182 | 100 | 572,147 | 10 | 799,399 | 6,283.6 | 3.0 | 56% | 44% (41개) |
| relaxing piano music | 182 | 100 | 2,000,000 | 13 | 491,497.0 | 6,856.1 | 0.4 | 56% | 44% (36개) |
| 음악 | 182 | 100 | 2,000,000 | 5 | 838,476.0 | 7,215.1 | 0.7 | 57% | 43% (36개) |
| 편안한음악 | 182 | 100 | 420,824 | 14 | 126,566 | 785.9 | 0.4 | 13% | 42% (41개) |
| 마음이편안해지는음악 | 182 | 100 | 152,118 | 5 | 107,737 | 957.8 | 1.2 | 20% | 40% (37개) |
| … 나머지 21개는 analysis.json |  |  |  |  |  |  |  |  |  |

### 3-3. 사람들이 찾는 말 (YouTube 자동완성) 중 최근 영상이 적은 말

수요 점수 = 검색어를 넣었을 때 자동완성에 앞쪽에 나올수록·여러 검색어에서 나올수록 큼. 최근 영상 = 우리가 본 최근 영상 중 제목에 그 말의 낱말이 다 든 수. 틈 = 수요 점수 ÷ (1 + 최근 영상). **공급 확인** = 웹 화면 [공급 확인]으로 그 말을 직접 검색한 결과 (최근 90일 결과 수·상위 영상).

| 말 | 수요 점수 | 나온 검색어 | 최근 영상(우리가 본) | 틈 | 공급 확인: 결과 수 | 영상당 하루 조회수 | 작은 채널 비율 | 최근 30일 |
|---|---|---|---|---|---|---|---|---|
| 수면음악 3시간 | 1.8 | 수면음악, 숙면음악 | 0 | 1.8 | 확인 전 |  |  |  |
| healing music kks | 1.8 | healing music, healingmusic | 0 | 1.8 | 확인 전 |  |  |  |
| piano music bros | 1.8 | piano music, pianomusic | 0 | 1.8 | 확인 전 |  |  |  |
| 수면음악 빗소리 | 1.6 | 수면음악, 숙면음악 | 0 | 1.6 | 확인 전 |  |  |  |
| healing music studio | 1.6 | healing music, healingmusic | 0 | 1.6 | 확인 전 |  |  |  |
| piano music for studying | 1.6 | piano music, pianomusic | 0 | 1.6 | 확인 전 |  |  |  |
| bgm 무료 | 1.6 | bgm, BGM | 0 | 1.6 | 확인 전 |  |  |  |
| 수면음악 지브리 | 1.4 | 수면음악, 숙면음악 | 0 | 1.4 | 확인 전 |  |  |  |
| meditation music 20 minutes | 1.4 | meditation music, MeditationM… | 0 | 1.4 | 확인 전 |  |  |  |
| sleep music 1 hour | 1.4 | sleep music, Sleep Music | 0 | 1.4 | 확인 전 |  |  |  |
| bgmer awaken | 1.4 | bgm, BGM | 0 | 1.4 | 확인 전 |  |  |  |
| 수면음악 10분 | 1.2 | 수면음악, 숙면음악 | 0 | 1.2 | 확인 전 |  |  |  |
| sleep music live | 1.2 | sleep music, Sleep Music | 0 | 1.2 | 확인 전 |  |  |  |
| bgmi air | 1.2 | bgm, BGM | 0 | 1.2 | 확인 전 |  |  |  |
| piano music bros chopin | 1.1 | piano music, pianomusic | 0 | 1.1 | 확인 전 |  |  |  |
| 수면음악 클래식 | 1.0 | 수면음악, 숙면음악 | 0 | 1.0 | 확인 전 |  |  |  |
| sleep music playlist | 1.0 | sleep music, Sleep Music | 0 | 1.0 | 확인 전 |  |  |  |
| bgm 추천 | 1.0 | bgm, BGM | 0 | 1.0 | 확인 전 |  |  |  |
| 잠잘때 듣는 노래 | 1.0 | 잠잘때 듣는 | 0 | 1.0 | 확인 전 |  |  |  |
| peaceful music for studying | 1.0 | peaceful music | 0 | 1.0 | 확인 전 |  |  |  |
| 명상음악 싱잉볼 | 0.9 | 명상음악 | 0 | 0.9 | 확인 전 |  |  |  |
| sleep music dark screen | 1.8 | sleep music, Sleep Music | 1 | 0.9 | 확인 전 |  |  |  |
| deep sleep music live | 0.9 | deep sleep music | 0 | 0.9 | 확인 전 |  |  |  |
| 자장가동화 | 0.9 | 자장가 | 0 | 0.9 | 확인 전 |  |  |  |
| 수면유도음악 4시간 | 0.9 | 수면유도음악 | 0 | 0.9 | 확인 전 |  |  |  |
| 치유음악 광고없음 | 0.9 | 치유음악 | 0 | 0.9 | 확인 전 |  |  |  |
| 집중음악 1시간 | 0.9 | 집중음악 | 0 | 0.9 | 확인 전 |  |  |  |
| 카페음악 가사없는 | 0.9 | 카페음악 | 0 | 0.9 | 확인 전 |  |  |  |
| 플리키뱅 | 0.9 | 플리 | 0 | 0.9 | 확인 전 |  |  |  |
| 음악줄넘기 | 0.9 | 음악 | 0 | 0.9 | 확인 전 |  |  |  |

### 3-4. 주제 묶음별 시청자 질문 (사례 댓글 — 좋아요 순)

- **9. 가요·발라드·트로트** (112개): 👍719 “젤루 잘생긴 성리 K트롯돌 실력자 올라운더 멀티 AI 성리 글로벌 세계로 가자 국민투표 연속 7주1위 성리 우승까지 밀어주시길 부탁드립니다 꾸~~벅 " 핑크 스타 다이아몬드" 성리 1대 전설이 되…” / 👍640 “조회수 궁금해서 계속와보는 사람 개츄 내가 살다살다 아이돌 트롯이 1500만 넘기는걸 보다니” / 👍4 “우연히 발라드곡 찾다가 들었는데 너무좋네요 첫곡 마지막곡 한곡씩 올려주시면 좋겠음^^ ai곡인줄 모르고 엄청찾았음... 너무좋아요 구독 좋아요😊”
- **15. CCM·찬양·국악·동요** (36개): 👍31 “모든 찬양에 은혜주신 주님께 감사드립니다 저녁에 찬양따라 부르며 울다가 웃다가 기도하며 찬양에 흠뻑 빠졌습니다 예전에 처음 교회다닐때 찬송가 하늘가는 밝은길이 그찬양만 들으면 얼마나 닭똥같던 눈물…” / 👍24 “이 찬양 큰위로가 됩니다 감사합니다, 혹시 찬양사역자분 누구신지. 알고싶네요,” / 👍16 “축하드립니다!! 계속 은혜로운 찬양 부탁합니다^*^”
- **6. 피아노·클래식·연주곡** (30개): 👍62 “최고에요! 제 브이로그 배경음악으로 클래식을 많이 쓰는데, 혹시 출처표시하고 bgm으로 쓸 수 있을까요? 안되더라두 괜찮으니 편하게 알려주세요! 좋은 음악 감사합니다! :)” / 👍10 “💖 따뜻한 분위기와 감성적인 피아노 연주가 어우러져서 듣는 내내 행복했습니다. 일상 속 작은 휴식이 필요할 때마다 다시 찾아 듣고 싶어요. 앞으로도 이런 힐링 음악 많이 올려주세요!” / 👍8 “이 곡을 이렇게 편곡할 수 있나요? 만드신 분의 내공이 느껴진다. 간주에 피아노와 기타의 콜라보, 대단하네요...좋은 곡 많이 부탁합니다. 😊”
- **12. 커버·노래 부르기** (29개): 👍10 “장윤정 꽃 불러줘(여러분 추천해주세요ㅠ)” / 👍7 “성리 우승 응원합니다. 궁금하다. 도대체 이것보다 어떻게 불러야 점수가 더 나올 라나 600점 만점에 550 도 넘지않는 점수를😊” / 👍6 “노래 너무 잘들었습니다! 혹시 물고기자리 누구 커버에요? 너무 선곡이 좋으셔서 궁금합니다”
- **3. 공부·집중·작업** (27개): 👍77 “할렐루야 주님께 영광돌립니다 . 호주에서 5년 살고 컴백한 시골사역 사모예요. 한국 정읍시 오주길 ~ 작은마을 개척교회사모입니다. 저희는 교회 사역에 필요한 야채 식료품 밭에서 직저자배해서 성도님…” / 👍9 “워낙 플리들이 다 좋아서 아무거나 틀어놔도 될 줄 알았는데, 확실히 독서할 땐 이거네요👍 덕분에 집에서도 책을 읽을 수 있게 됐어요🙂‍↕️독서용도 종종 만들어 주시면 정말 좋을 것 같아요..🙏” / 👍6 “코러스 집중 영상 올려주세요 ㅋㅋㅋ”
- **10. 팝송·K팝·J팝** (21개): 👍28 “번역기를 사용해서 문장이 조금 어색할 수 있는 점 양해 부탁드립니다. 우크라이나에서 인사드립니다! 🇺🇦 학창 시절 BIGBANG 노래를 정말 많이 들었던 팬으로서 이 버전은 정말 감동적이네요...…” / 👍8 “미나미 JPOP, 제나 트로트에 이어서 원이: 한글날 기념 판소리 메들리 (사랑가, 춘향가 포함 자작가로 거제가 부탁드립니다) 리브 메이: 크리스마스 기념 뮤지컬 메들리 (뮤지컬 제목: 리트와 메…” / 👍2 “제이팝 좋은거 찾고있는데 추천좀여”
- **1. 수면·명상·힐링** (20개): 👍20 “불면으로 힘들어하는 50대입니다. 수면제 10년째중이구요. 이 음악으로 마음의 평안을 얻습니다. 유투브에 저장해서 비행기에서도 무한반복이구요. 요즘 체력적으로 힘든치료 받고 온 날 해당음악 귀에 …” / 👍11 “평소에 드보르작의 곡을 좋아했지만 이곡은 정말 마음을 아름답고 즐겁게 하네 요. 아침에 우연히 들었는데 마음이 가볍고 편안하게 힐링 해주었습니다. 감사해요. 앞으로도 계속하여 또 좋은곡 부탁드립니…” / 👍9 “오늘도 청계천 걸어며 걸어온길 삶속에 명상하면서 음악 감상하고 갑니다 오늘도 좋은음악 올려주세요 셈님 감사합니다”
- **4. 카페·매장·라운지** (12개): 👍29 “다음카페 좀 힘들어도 자녀분들이나 폰가게 부탁해서 가입 부탁드려요 가입 시도해서 성리 비상하도록 힘합쳐봐요 어렵지 않아요 카페이전이 원래 회원들 이동도 힘들고 뭔가 어려운가 봅니다 2달 넘게 눈뜨…” / 👍14 “저런 광장에서 커피 한잔 마시면서 친한 친구와 놀면 얼마나 좋을까요? 좋아요와 구독하고 갑니다.” / 👍4 “카페 위치 어디인지 알수 있을까요?ㅎㅎ”
- **14. AI 음악** (12개): 👍5 “안녕하세요. 선생님이 만드시는 음악을 정말 좋아하고 존경합니다. 음악이 정말 너무 좋습니다. 저도 선생님처럼 좋은 음악을 만들어보고 싶어서 한 달 넘게 고민하고 여러 가지 방법으로 만들어봤지만, …” / 👍4 “ai노래 맞나요? 느낌이 살짝 그런거 같은데 노래 다 좋음 편안히 들을수있고 가수보다 훨씬 나은듯 함” / 👍4 “그 집 앞 노래를 못찾겠네요. 어디서 찾을 수 있을까요? AI 음악 같은데..”
- **5. 운동·드라이브·신나는** (10개): 👍20 “순천부영초등학교 이지인입니다 이챌린지을많이봤어요 이노래를듣으면 우울할때기분이 좋아져서이노래에 댓글을달았어요앞으로 신나는노래많이 올려주세요” / 👍8 “울적할때 이 노래 들으면서 드라이브하면 정말 좋을것 같아요 노래 스타일 너무 좋아요♡♡ 좋은 노래 많이 올려주세요!ㅎ” / 👍6 “트로트를 간혹 듣는 아재인데 용두산, 빵빵 등의 숨은 명곡을 알려주셔서 감사합니다. 90,00 신나는 명곡 메들리도 나중에 가능하실때 부탁드립니다. 일하면서 운전하면서 듣기에 너무 좋습니다”
- **7. 재즈·보사노바** (9개): 👍15 “도경수씨 커버앨범, 재즈앨범, 팝앨범 부탁해요” / 👍3 “넘넘넘 좋아요 요즘 맨날 이것만 들어요! 좀더 잔잔하고 웅장한(?) 느낌의 불교 재즈도 만들어주세요ㅜㅜ” / 👍3 “와 진짜 로제감성 낭낭한게 재즈로 느껴져서 너무 좋아요 ㅜㅜ 다른 노래들도 많이 재즈로 만들어주세요!!”
- **11. 힙합·R&B·EDM** (3개): 👍8 “다 좋아하는 노래예용 ㅠ 이런 감성힙합으로 사람들이 잘 모르는 숨겨진 띵곡 플리도 만들어주실 수 있나여??” / 👍1 “요즘 조선힙합이있어서 노래듣는맛이나네요..계속 이렇게 좋은노래 올려주세요~항상 감사해용~~😊😊”
- **8. 로파이·시티팝·칠** (2개): 👍4 “시티팝 모음집으로 한번 만들어주세요~!! 너무 좋네요” / 👍1 “어쩌다 알고리즘 떠서 들어왔는데 밤 공부용으로 딱이에요!!! 캐릭터도 너무 귀여워요..... ㅠㅠㅠㅠ 이런류 많이 올려주세요!! 시티팝 느낌도 좋을거 같아요!! 암튼 잘 듣겠습니당 ㅎㅎ”
- **2. 자연 소리·백색소음** (2개): 👍94 “항상 잘 듣고 있는 구독자입니다, 알아봐 주실지는 모르겠는데…. 매번 이렇게 댓글 다는 채널은 여기가 처음입니다. 매번 빠지지 않고 새 영상 올려주셔서 감사해요. 제가 고요한 걸 무서워해서 다양한…” / 👍6 “옛날 친구들과 모닥불옆에서 기타치며 노래하던 추억이 새록새록 살아나네요ㆍ그친구들 내여친은 어디서 무엇하는지 궁금하네요ㆍ캐나다 이민가고 연락이 ~뚝~~ㅠㅠ”
- **13. OST·사운드트랙** (2개): 👍7 “애니 ost 편도 해주세요 조회수 잘될듯?” / 👍0 “사운드트랙이 완벽해요. HAN은 이번에도 제대로 해냈네요. 언제나처럼 말이죠? 정말 마음에 들어요!”

## 4. 제목

### 4-1. 제목 특징별 성공 비율 (비교 집단: 있음 vs 없음)

'눈에 띔' = 차이 10%p 이상 · 양쪽 15개 이상 (원인이 아니라 표시). 마지막 열 = 성공 사례 중 그 특징이 있는 비율.

| 제목 특징 | 있음 (성공 비율) | 없음 (성공 비율) | 차이 | 표시 | 성공 사례 중 |
|---|---|---|---|---|---|
| vs 비교 | 74 (36%) | 5736 (20%) | +16%p | **눈에 띔** | 1.1% |
| 25자 미만 | 398 (33%) | 5412 (20%) | +13%p | **눈에 띔** | 8.1% |
| 빚투·신용·미수·레버리지·대출 | 2 (50%) | 5808 (21%) | +29%p | 표본 적음 | 0.1% |
| 손실 낱말(망하·날린·잃은·반토막) | 7 (0%) | 5803 (21%) | -21%p | 표본 적음 | 0% |
| 직접·해보니·N년 기록 | 3 (0%) | 5807 (21%) | -21%p | 표본 적음 | 0% |
| S&P500·ETF·지수·나스닥 | 1 (0%) | 5809 (21%) | -21%p | 표본 적음 | 0% |
| 노후·퇴직금·은퇴·50~70대 | 14 (36%) | 5796 (21%) | +15%p | 표본 적음 | 0.4% |
| N가지 | 3 (33%) | 5807 (21%) | +13%p | 표본 적음 | 0% |
| 사연·오디오북·실화·고백 | 10 (10%) | 5800 (21%) | -11%p | 표본 적음 | 0% |
| 40자 이상 | 4793 (19%) | 1017 (28%) | -10%p |  | 82% |
| 따옴표·괄호로 강조 | 1037 (26%) | 4773 (19%) | +7%p |  | 20% |
| 과정·벌어진 일·결말·결국 | 7 (14%) | 5803 (21%) | -6%p | 표본 적음 | 0% |
| 구분 기호(ㅣ·｜·/)로 나눔 | 3496 (19%) | 2314 (24%) | -5%p |  | 59% |
| 이유 | 12 (25%) | 5798 (21%) | +4%p | 표본 적음 | 0% |
| 물음표 ? | 102 (24%) | 5708 (20%) | +4%p |  | 1.2% |
| AI | 480 (22%) | 5330 (20%) | +2%p |  | 8.2% |
| 패턴형(공통점·특징·이유·N가지·착각·과정) | 18 (22%) | 5792 (21%) | +2%p |  | 0% |
| 느낌표 ! | 110 (19%) | 5700 (21%) | -2%p |  | 1.7% |
| 말줄임 …·... | 160 (22%) | 5650 (21%) | +1%p |  | 3.2% |
| 숫자가 들어감 | 1886 (21%) | 3924 (21%) | +0%p |  | 33% |

### 4-2. 제목 낱말 (비교 집단 제목에 자주 나온 낱말 — 조사를 거칠게 뗌)

| 낱말 | 있음 (성공 비율) | 없음 (성공 비율) | 차이 | 표시 |
|---|---|---|---|---|
| playlist | 218 (37%) | 5592 (20%) | +17%p | **눈에 띔** |
| Playlist | 447 (30%) | 5363 (20%) | +10%p | **눈에 띔** |
| 플레이리스트 | 178 (25%) | 5632 (20%) | +5%p |  |
| Jazz | 204 (24%) | 5606 (20%) | +4%p |  |
| Love | 214 (24%) | 5596 (20%) | +4%p |  |
| Chill | 191 (23%) | 5619 (20%) | +2%p |  |
| Lofi | 271 (22%) | 5539 (20%) | +2%p |  |
| Songs | 296 (22%) | 5514 (20%) | +2%p |  |
| Slowed | 215 (22%) | 5595 (21%) | +1%p |  |
| BGM | 236 (21%) | 5574 (21%) | +1%p |  |
| Song | 284 (21%) | 5526 (21%) | +0%p |  |
| Reverb | 214 (21%) | 5596 (21%) | +0%p |  |
| 음악 | 242 (8.3%) | 5568 (21%) | -13%p | **눈에 띔** |
| Healing | 212 (9.0%) | 5598 (21%) | -12%p | **눈에 띔** |
| Focus | 208 (9.1%) | 5602 (21%) | -12%p | **눈에 띔** |
| Meditation | 187 (10%) | 5623 (21%) | -11%p | **눈에 띔** |
| 마음 | 192 (10%) | 5618 (21%) | -11%p | **눈에 띔** |
| Deep | 422 (12%) | 5388 (21%) | -10%p |  |
| Study | 213 (12%) | 5597 (21%) | -9%p |  |
| Music | 1078 (13%) | 4732 (22%) | -9%p |  |
| Peaceful | 197 (12%) | 5613 (21%) | -9%p |  |
| Mind | 175 (14%) | 5635 (21%) | -6%p |  |

### 4-3. 제목 길이

| 길이 | 영상 (성공 비율) |
|---|---|
| 0~24자 | 398 (33%) |
| 25~34자 | 385 (29%) |
| 35~44자 | 491 (19%) |
| 45자 이상 | 4536 (19%) |

성공 사례 제목 전부는 1번 표 (#순).

## 5. 썸네일

글자·얼굴·색·구도는 자동으로 뽑지 않는다 — **이미지를 직접 보고** 판단한다 (번호 = 1번 표의 #).

성공 사례 #1–#20:

![성공 사례 썸네일 #1-#20](analysis_thumbs_01.jpg)

성공 사례 #21–#40:

![성공 사례 썸네일 #21-#40](analysis_thumbs_02.jpg)

성공 사례 #41–#60:

![성공 사례 썸네일 #41-#60](analysis_thumbs_03.jpg)

성공 사례 #61–#80:

![성공 사례 썸네일 #61-#80](analysis_thumbs_04.jpg)

성공 사례 #81–#100:

![성공 사례 썸네일 #81-#100](analysis_thumbs_05.jpg)

성공 사례 #101–#120:

![성공 사례 썸네일 #101-#120](analysis_thumbs_06.jpg)

성공 사례 #121–#140:

![성공 사례 썸네일 #121-#140](analysis_thumbs_07.jpg)

성공 사례 #141–#160:

![성공 사례 썸네일 #141-#160](analysis_thumbs_08.jpg)

성공 사례 #161–#180:

![성공 사례 썸네일 #161-#180](analysis_thumbs_09.jpg)

성공 사례 #181–#200:

![성공 사례 썸네일 #181-#200](analysis_thumbs_10.jpg)

성공 사례 #201–#220:

![성공 사례 썸네일 #201-#220](analysis_thumbs_11.jpg)

성공 사례 #221–#240:

![성공 사례 썸네일 #221-#240](analysis_thumbs_12.jpg)

성공 사례 #241–#260:

![성공 사례 썸네일 #241-#260](analysis_thumbs_13.jpg)

성공 사례 #261–#280:

![성공 사례 썸네일 #261-#280](analysis_thumbs_14.jpg)

성공 사례 #281–#300:

![성공 사례 썸네일 #281-#300](analysis_thumbs_15.jpg)

성공 사례 #301–#320:

![성공 사례 썸네일 #301-#320](analysis_thumbs_16.jpg)

성공 사례 #321–#340:

![성공 사례 썸네일 #321-#340](analysis_thumbs_17.jpg)

성공 사례 #341–#360:

![성공 사례 썸네일 #341-#360](analysis_thumbs_18.jpg)

성공 사례 #361–#380:

![성공 사례 썸네일 #361-#380](analysis_thumbs_19.jpg)

성공 사례 #381–#400:

![성공 사례 썸네일 #381-#400](analysis_thumbs_20.jpg)

성공 사례 #401–#420:

![성공 사례 썸네일 #401-#420](analysis_thumbs_21.jpg)

성공 사례 #421–#440:

![성공 사례 썸네일 #421-#440](analysis_thumbs_22.jpg)

성공 사례 #441–#460:

![성공 사례 썸네일 #441-#460](analysis_thumbs_23.jpg)

성공 사례 #461–#480:

![성공 사례 썸네일 #461-#480](analysis_thumbs_24.jpg)

성공 사례 #481–#500:

![성공 사례 썸네일 #481-#500](analysis_thumbs_25.jpg)

성공 사례 #501–#520:

![성공 사례 썸네일 #501-#520](analysis_thumbs_26.jpg)

성공 사례 #521–#540:

![성공 사례 썸네일 #521-#540](analysis_thumbs_27.jpg)

성공 사례 #541–#560:

![성공 사례 썸네일 #541-#560](analysis_thumbs_28.jpg)

성공 사례 #561–#580:

![성공 사례 썸네일 #561-#580](analysis_thumbs_29.jpg)

성공 사례 #581–#600:

![성공 사례 썸네일 #581-#600](analysis_thumbs_30.jpg)

성공 사례 #601–#620:

![성공 사례 썸네일 #601-#620](analysis_thumbs_31.jpg)

성공 사례 #621–#640:

![성공 사례 썸네일 #621-#640](analysis_thumbs_32.jpg)

성공 사례 #641–#660:

![성공 사례 썸네일 #641-#660](analysis_thumbs_33.jpg)

성공 사례 #661–#680:

![성공 사례 썸네일 #661-#680](analysis_thumbs_34.jpg)

성공 사례 #681–#700:

![성공 사례 썸네일 #681-#700](analysis_thumbs_35.jpg)

성공 사례 #701–#720:

![성공 사례 썸네일 #701-#720](analysis_thumbs_36.jpg)

성공 사례 #721–#740:

![성공 사례 썸네일 #721-#740](analysis_thumbs_37.jpg)

성공 사례 #741–#760:

![성공 사례 썸네일 #741-#760](analysis_thumbs_38.jpg)

성공 사례 #761–#780:

![성공 사례 썸네일 #761-#780](analysis_thumbs_39.jpg)

성공 사례 #781–#800:

![성공 사례 썸네일 #781-#800](analysis_thumbs_40.jpg)

성공 사례 #801–#820:

![성공 사례 썸네일 #801-#820](analysis_thumbs_41.jpg)

성공 사례 #821–#840:

![성공 사례 썸네일 #821-#840](analysis_thumbs_42.jpg)

성공 사례 #841–#860:

![성공 사례 썸네일 #841-#860](analysis_thumbs_43.jpg)

성공 사례 #861–#880:

![성공 사례 썸네일 #861-#880](analysis_thumbs_44.jpg)

성공 사례 #881–#900:

![성공 사례 썸네일 #881-#900](analysis_thumbs_45.jpg)

성공 사례 #901–#920:

![성공 사례 썸네일 #901-#920](analysis_thumbs_46.jpg)

성공 사례 #921–#940:

![성공 사례 썸네일 #921-#940](analysis_thumbs_47.jpg)

성공 사례 #941–#960:

![성공 사례 썸네일 #941-#960](analysis_thumbs_48.jpg)

성공 사례 #961–#980:

![성공 사례 썸네일 #961-#980](analysis_thumbs_49.jpg)

성공 사례 #981–#1000:

![성공 사례 썸네일 #981-#1000](analysis_thumbs_50.jpg)

성공 사례 #1001–#1020:

![성공 사례 썸네일 #1001-#1020](analysis_thumbs_51.jpg)

성공 사례 #1021–#1040:

![성공 사례 썸네일 #1021-#1040](analysis_thumbs_52.jpg)

성공 사례 #1041–#1060:

![성공 사례 썸네일 #1041-#1060](analysis_thumbs_53.jpg)

성공 사례 #1061–#1080:

![성공 사례 썸네일 #1061-#1080](analysis_thumbs_54.jpg)

성공 사례 #1081–#1100:

![성공 사례 썸네일 #1081-#1100](analysis_thumbs_55.jpg)

성공 사례 #1101–#1114:

![성공 사례 썸네일 #1101-#1114](analysis_thumbs_56.jpg)

같은 채널 짝 — 줄마다 [성공 사례 #n · 같은 채널 평소 영상 #n-a · #n-b] (1 … #14-b):

![같은 채널 썸네일 짝](analysis_thumbs_pairs_01.jpg)

같은 채널 짝 — 줄마다 [성공 사례 #n · 같은 채널 평소 영상 #n-a · #n-b] (16 … #33-b):

![같은 채널 썸네일 짝](analysis_thumbs_pairs_02.jpg)

비교 — 자료를 받았지만 성공 기준 밖 (조회수 큰 순, 번호는 `analysis.json` 의 others 순서):

![비교 썸네일](analysis_thumbs_others.jpg)

## 6. 길이·내용 구성

### 6-1. 길이별 성공 비율 (비교 집단)

| 길이 | 영상 (성공 비율) | 성공 사례 |
|---|---|---|
| 4~8분 | 1557 (19%) | 270 |
| 8~15분 | 615 (24%) | 122 |
| 15~25분 | 635 (34%) | 127 |
| 25~40분 | 425 (26%) | 70 |
| 40분 이상 | 2578 (17%) | 525 |

### 6-2. 채널 크기별 성공 비율 (참고 — 구독자가 적을수록 배수가 커지기 쉬움)

| 구독자 | 영상 (성공 비율) |
|---|---|
| 0~999명 | 809 (12%) |
| 1,000~4,999명 | 1640 (26%) |
| 5,000~19,999명 | 2072 (20%) |
| 20,000~50,000명 | 1289 (20%) |

### 6-3. 성공 사례의 구성

- 길이 중앙값: 성공 사례 29.9분 · 비교 집단의 나머지 31.2분
- 타임라인(챕터) 있는 성공 사례: 28% (챕터 수 중앙값 12)
- 대본이 있는 성공 사례: 0개 — 말 속도 중앙값 – 음절/초, 첫 1분 음절 중앙값 – (대본이 없어 도입부·흐름은 아직 셀 수 없음)
- 도입부(첫 20초 첫 문장) 유형: 대본 없음 — 아직 셀 수 없음
- 사례마다의 챕터·도입부(첫 20초)·첫 1분·90초마다 흐름은 9번.

### 6-4. 참여율 (비교 집단, 중앙값)

| | 영상 | 조회수 1,000회당 좋아요 | 조회수 1,000회당 댓글 |
|---|---|---|---|
| 성공 | 1197 | 7.8 | 0.2 |
| 나머지 | 4613 | 10.9 | 0.8 |

## 7. 구독자 — 빨리 크는 작은 채널

YouTube API 는 영상별 구독 증가를 주지 않는다 → 채널 단위로 본다. 개설 24개월 안·구독자 1,000 이상 채널을 **월 구독자 증가(구독자 ÷ 개설 뒤 달 수)** 순으로. 최근 하루 증가 = 받을 때마다 남긴 구독자 기록 (3일 넘게 벌어져야 나옴). 주로 다룬 주제 = 우리가 본 그 채널 영상의 주제 묶음. **기관·브랜드?** = 채널 이름에 운용사 ETF 상표·증권·은행·공식·방송 같은 말 (`analysis_rules.toml` [growth] BRAND_HINT) — 광고비로 큰 채널일 수 있어 개인 채널과 따로 보라.

| 채널 | 기관·브랜드? | 개설 | 구독자 | 월 구독자 증가 | 최근 하루 증가 | 영상 수 | 월 업로드 | 길이 중앙값 | 주로 다룬 주제 | 대표 영상 (하루 조회수 큰 것) |
|---|---|---|---|---|---|---|---|---|---|---|
| 정이랑의 진기명기 |  | 2025-11-07 | 198,000 | 17,419 | – | 310 | 27.3 | 23.1분 | 6. 피아노·클래식·연주곡 | [2007년 우己lㄱr バr己б했던 학원☆™🎹 #정이랑 #추억 #공감 #…](https://www.youtube.com/watch?v=argmeBt7OUU) 2,916,955회 |
| 명곡부활단 |  | 2026-03-21 | 105,000 | 15,006 | – | 316 | 45.2 | 4.8분 | 5. 운동·드라이브·신나는, 9. 가요·발… | [여인 – 우리 가슴속 깊이 박혀 있던 그 노래, 듣는 순간 그 시절로 …](https://www.youtube.com/watch?v=a0iBRRoDnDw) 6,699,495회 |
| comfort space ♡ |  | 2026-04-12 | 79,900 | 12,801 | – | 128 | 20.5 | 360.0분 | 1. 수면·명상·힐링 | [go to sleep, you need it.](https://www.youtube.com/watch?v=Q5bDzSwLE8w) 3,313,166회 |
| ClassicalMusic … |  | 2026-04-22 | 74,200 | 12,548 | – | 165 | 27.9 | 81.3분 | 6. 피아노·클래식·연주곡 | [Adagio (Cello, Piano, Violin) - Beautif…](https://www.youtube.com/watch?v=wNpsTbqdBiw) 4,946,444회 |
| Rb Lofi |  | 2026-08-23 | 23,700 | 12,438 | – | 29 | 15.2 | 18.5분 | 8. 로파이·시티팝·칠, 기타 | [ALL TRENDING HINDI SONGS 2026...PLAYLIS…](https://www.youtube.com/watch?v=xI0IEWIxUBQ) 9,921,293회 |
| Quiet Tunęs |  | 2025-10-13 | 151,000 | 12,356 | – | 129 | 10.6 | 322.5분 | 1. 수면·명상·힐링 | [432Hz + 528Hz + 741Hz ∣ The Deepest Hea…](https://www.youtube.com/watch?v=Y5wQB1TTh2s) 8,589,203회 |
| Tom’s Jazz Loun… |  | 2026-04-25 | 71,000 | 12,142 | – | 105 | 18.0 | 75.4분 | 7. 재즈·보사노바 | [Just One More Drink -- Jazz Noir](https://www.youtube.com/watch?v=7gtIh5dF9Xk) 6,414,861회 |
| Milesora Lounge |  | 2026-04-14 | 66,900 | 10,832 | – | 189 | 30.6 | 77.4분 | 12. 커버·노래 부르기, 4. 카페·매장… | [Smooth Jazz & Soul R&B ∣ Soft Female Vo…](https://www.youtube.com/watch?v=YQHnz8VuazY) 2,344,500회 |
| Serenata |  | 2025-09-30 | 119,000 | 9,433 | – | 46 | 3.6 | 62.2분 | 기타 | [Popular OPM Hits 2026 🌿 New Filipino Pl…](https://www.youtube.com/watch?v=Ur4FFQT--Qw) 5,554,518회 |
| 80s Guitar Loun… |  | 2026-08-04 | 23,800 | 9,409 | – | 40 | 15.8 | 68.3분 | 6. 피아노·클래식·연주곡, 12. 커버·… | [Classic Love Songs ❤️ Timeless Acoustic…](https://www.youtube.com/watch?v=jDUH254gfs8) 583,619회 |
| Nature for the … |  | 2026-08-24 | 17,200 | 9,349 | – | 80 | 43.5 | 3.0분 | 1. 수면·명상·힐링, 6. 피아노·클래식… | [Sultry Saxophone Beats • Smooth R&B Jaz…](https://www.youtube.com/watch?v=PxeZARMnC-0) 14,362회 |
| Retrovivals |  | 2025-12-02 | 97,500 | 9,217 | – | 156 | 14.7 | 4.8분 | 14. AI 음악 | [Retrovivals - Kung Ako Nalang Sana - Bi…](https://www.youtube.com/watch?v=wbI70GOWw0U) 3,670,954회 |
| Baby Bon Bon - … |  | 2026-07-28 | 24,600 | 9,022 | – | 21 | 7.7 | 11.4분 | 기타 | [Lola the Cow Song! (La Vaca Lola) 🐄 Ani…](https://www.youtube.com/watch?v=irzJfFIeggM) 42,977회 |
| 레코드 속 추억 | 예(레코드) | 2026-04-10 | 56,000 | 8,878 | – | 132 | 20.9 | 81.8분 | 기타, 9. 가요·발라드·트로트 | [“꽃길” “인연” “묻어버린 아픔” “마지막 연인” “사랑 참”🎸🔥조회…](https://www.youtube.com/watch?v=YBeWbO46Gtw) 1,217,971회 |
| cozi_music |  | 2026-07-10 | 29,400 | 8,774 | – | 10 | 3.0 | 4.5분 | 기타, 8. 로파이·시티팝·칠 | [𓆩♡𓆪 𝑻𝑹𝑬𝑵𝑫𝑰𝑵𝑮 𝑺𝑶𝑵𝑮𝑺 𝑶𝑭 𝟐𝟎𝟐𝟔 𓆩♡𓆪 ∣∣ All t…](https://www.youtube.com/watch?v=85vOsUlmkjM) 472,957회 |
| Jasu LOFI |  | 2026-07-15 | 26,700 | 8,379 | – | 154 | 48.3 | 5.4분 | 8. 로파이·시티팝·칠, 기타 | [Patar Bashori ∣ পাতার বাঁশরী ∣ Lofi Ban…](https://www.youtube.com/watch?v=rgKNbCrC-cc) 7,754,679회 |
| Violinhop |  | 2025-09-19 | 103,000 | 7,938 | – | 160 | 12.3 | 71.7분 | 11. 힙합·R&B·EDM | [【Violin x Hip Hop Playlist】– My Truth i…](https://www.youtube.com/watch?v=TGYiJ5uoEtM) 2,307,847회 |
| Ayan Studio |  | 2026-01-28 | 67,400 | 7,771 | – | 122 | 14.1 | 4.6분 | 기타 | [Na Bole Esechhi ∣ Male Version ∣ Heart …](https://www.youtube.com/watch?v=AQhp6kCxIRM) 2,135,149회 |
| Soulful Breaths… |  | 2026-04-06 | 49,600 | 7,703 | – | 188 | 29.2 | 39.2분 | 1. 수면·명상·힐링, 6. 피아노·클래식… | [Morning Cortisol Detox 🌿 Raag Bhairavi …](https://www.youtube.com/watch?v=cjNH2q4aBYc) 958,149회 |
| NOXTUNE |  | 2026-07-29 | 20,700 | 7,684 | – | 17 | 6.3 | 11.1분 | 기타, 8. 로파이·시티팝·칠 | [Playlist For You To Create Fake Scenari…](https://www.youtube.com/watch?v=0gUwbTCQ78k) 6,498,348회 |
| 노래방 옆 만화방 |  | 2025-11-20 | 81,000 | 7,382 | – | 235 | 21.4 | 4.5분 | 10. 팝송·K팝·J팝, 9. 가요·발라드… | [정승환 & 박지원- 그 여자 (시크릿가든 OST) l [정승환의 노래방…](https://www.youtube.com/watch?v=QlOJ3HsA6Jk) 2,718,336회 |
| Frequencies of … |  | 2026-04-10 | 46,400 | 7,356 | – | 19 | 3.0 | 75.7분 | 1. 수면·명상·힐링, 6. 피아노·클래식… | [Cleanse Everything Draining You ∣ Heal …](https://www.youtube.com/watch?v=QNxiKUklOKQ) 952,294회 |
| encore. |  | 2026-09-20 | 7,210 | 7,210 | – | 12 | 12.0 | 21.6분 | 기타 | [[Playlist] When music is all you need](https://www.youtube.com/watch?v=XXKXpf7xFC4) 2,673,428회 |
| ERRDAY GROOVE (… |  | 2025-11-05 | 81,700 | 7,126 | – | 226 | 19.7 | 4.1분 | 12. 커버·노래 부르기 | [엄정화 - 초대 [90's New Jack Swing Cover] (뉴…](https://www.youtube.com/watch?v=xNV5j1v53RY) 1,502,529회 |
| 국악딴따라 |  | 2026-05-19 | 35,000 | 6,963 | – | 49 | 9.7 | 3.7분 | 15. CCM·찬양·국악·동요, 1. 수면… | [국악딴따라 - 살아보니 그렇더라 (Official MV)](https://www.youtube.com/watch?v=FhNugHNh72s) 1,903,988회 |

## 8. 시청자 니즈 (성공 사례 1114개의 시청자 댓글 365,002개 — 채널 주인 댓글·도배 댓글 3,033개 뺌)

갈래는 낱말 규칙 (한 댓글이 여러 갈래). '더 알고 싶은 것'은 ① **요청**(다뤄 주세요·알려 주세요·궁금해요 — 다음 영상 주제 후보, 아래 8-1) 과 ② 물음표 질문(반문이 섞임, 8-2) 으로 나눠 인용한다.

| 갈래 | 댓글 | 비율 | 좋아요 합 |
|---|---|---|---|
| 좋은 점 — 영상 (도움·설명·정리·공감) | 598 | 0.2% | 3,675 |
| 감사·응원 (일반) | 7,694 | 2.1% | 57,970 |
| 더 알고 싶은 것 (질문·요청) | 1,010 | 0.3% | 12,550 |
| 아쉬운 점 — 영상 (제목·광고·길이·정보 오류·목소리) | 454 | 0.1% | 2,618 |
| 반박·불만 — 의견 다름 (내용) | 234 | 0.1% | 2,287 |
| 정치·사회 (영상과 무관한 의견) | 146 | 0% | 2,198 |
| 경험 공유 (내 이야기) | 2,773 | 0.8% | 43,733 |
| 구독·다음 기대 | 458 | 0.1% | 1,660 |

### 좋은 점 — 영상 (도움·설명·정리·공감) — 좋아요 많은 댓글

- 👍229 [#16] “처음에 크레이지 아케이드 소리 들리길래 영상 잘못 들어온 줄 알았네 ㅋㅋㅋㅋ 하 첫 곡부터 마지막 곡까지 너무 레전드라서 쉬는 날에 엄청난 힐링하고 갑니다 ㅠ”
- 👍189 [#819] “조선힙합 멜로디도 좋지만 모든 곡들의 가사가 너무 마음에 와닿습니다. 좋은 노래 만들어줘서 감사합니다. 위안이 되는 따뜻한 노래들.”
- 👍150 [#460] “저는 지금 이 순에도 위태로운 제 자신을 부여잡고 눈물을 흘리며 하루하루를 버티는 중년의 여성입니다 삶을 내려 놓고 싶은 순간이 너무 많지만 생명의 질긴 끊이 저를 버텨주네요 사실 용기도 없습니다 젊은 시절은 부모님 상처드리기 싫어 버티는 심정으로 살았고 지금은 제 반려견 걱정에 버티고 있습니다 얼마나 더 버틸수 있을까요..눈을 뜨고 하루를 대하는 저의 일”
- 👍124 [#556] “스타즈 오늘 둘다 레전드네 ㄷㄷㄷ❤❤❤❤”
- 👍108 [#261] “안녕하세요, 오늘의 플리님! 저는 도덕 수업에서 선플 달기 활동을 하고 있는 중1 학생입니다. 영상 정말 잘 보고 있어요. 항상 좋은 영상 올려주셔서 감사합니다. 좋은 하루 보내세요”
- 👍78 [#16] “디지몬 어드벤처, 이누야샤, 달빛천사, 아따맘마, 피치피치핏치, 카우보이 비밥, 나루토, 개구리 중사 케로로, 캐릭캐릭 체인지, 원피스 등등... 이런 레전드 꿀잼 애니메이션들을 감상할 수 있었던 90년대생들은 진짜 선택받은 어린이들 세대였던 것 같습니다.”
- 👍60 [#691] “힐링음악님 요즘 세로운 영상 찾아 올리시는 라 수고가 많으시죠? 덕분에 이렇게 좋은 영상을 보네요 고맙습니다🙏 (어디로 부터 그대는 왔는가) 전 이 가사가 유난히 좋더라구요^^”
- 👍59 [#11] “우리가 고3만 아니였다면 맞춰갈 수 있는 시간이 있었을텐데 정말 아쉽고 힘들다 벌써 1달이 넘었는데 단 하루도 널 잊은적이 없어 살면서 사랑을 알려줘서 고마워 지금은 너에게 아무것도 안하는게 돕는거라고 생각해서 수능 끝나고 연락할거야 우리 입시 성공해서 다시 만나자 영원한건 없어도 다시 만난다면 평생 사랑할게”

### 감사·응원 (일반) — 좋아요 많은 댓글

- 👍1,687 [#460] “26년 병원 검사를 마치고, 어제부터 1년을 선물 받았습니다. 안전한 1년이길 🙏하면서 , 오늘은 좋아하는 음악을 들으며 가만히 쉬어 봅니다. 이런날 음악이 친구가 되어주고, 위로가 되어줍니다. 클래식을 잘 모르지만, 저는 마음으로 느껴지는 걸 중요하게 생각하며 듣습니다. 귀로만 듣는게 아니라 몸과 마음을 어루만져 주는 그 찰나의 순간을 느끼는 것이지요. ”
- 👍744 [#1081] “김간지한테 고맙습니다 해야지”
- 👍576 [#679] “3기 진행성 위암 항암중입니다! 내 삶이 얼마나 될지 모르겠지만, 그저 부모님보다 먼저 죽으면 안되겠다는 생각에 살기 위해 애쓰고 있습니다 좋은 음악 감사합니다! 다들 건강하시고, 오늘도 살아 있음에 우리 주님께 감사 드립니다!”
- 👍531 [#926] “독다니엘 독일 살때 교회 다니며 파이프 오르간 연주자 였다더니 피아노도 수준급 인가보네요. 멋져요. 힝상 응원 합니다. 다니엘이 갖고 있는 순수함이 좋아요. 🎉🎉🎉🎉🎉❤❤❤❤❤”
- 👍529 [#198] “진짜 많이 보고싶다. 내 고등학생 생활이 전부 너라서 너 말고는 아무것도 안보였던 시기엿어. 고등학교 동안 나한테 과분한 사랑 주고 항상 내 편이 되어줘서 너무너무 고마워 우리 성인되는 날에 같이 첫 술 마시자고 했었는데 기억나? 그 약속 이제는 못 지키겠다. 헤어질 때 너무 아팟고 너와의 좋았던 기억들이 너무 많은데도 그 힘들었던 기억들이 계속 괴롭혔어.”
- 👍528 [#460] “번개탄 피워놓고 죽으면 다끝이지 않을까? 하는 마음을 떨쳐버리고 마음추스린지 일주일 입니다 삶에 무게너무 무겁지만 그래도 살아가는것이 맞겠지...하는생각에...모두들 힘내보아요”
- 👍486 [#679] “헨델의 많은곡을 들어봤으나 슬픔과 감정을 몰입하는 파사칼리아의 곡이 있는줄을 몰랐습니다. 계속 들어도 절제가 안되네요. 올려주신분께 감사하고 많은분들에 공유합니다.”
- 👍399 [#1060] “시험기간이라 그런지 요즘 영상이 많이 올라오네요 시험 화이팅 하세요”

### 더 알고 싶은 것 (질문·요청) — 좋아요 많은 댓글

- 👍6,477 [#446] “대체 뭔노래가 나올까 궁금해서 들어왔습니다”
- 👍1,047 [#407] “개발할 때마다 듣습니다; 많이 올려주세요”
- 👍945 [#679] “너무나 꿈같은 아들을 먼저 보냈습니다 33세의 꽃같은 나이에 바람이 되어 빛되어 제 주변에 맴 도는것 같습니다 세상의 어떤말도 표현 되어지지 않는 비 현실감.. 저의 모든것이었던 아들의 목소리를 더 이상 들을수 없는지 오늘이 51일째... 통곡의 울음조차 낼 수 없습니다 아들이 힘들어 할까봐.. 아빠를 너무 많이 닮은 아들. 모든면에서 너무나 비범했던 아들”
- 👍208 [#198] “여전히 잊지 못하였습니다. 당신이 나의 이상형이라서, 당신이 나의 첫사랑이라서, 끝난 관계임에도 나에게 잘 해줘서, 너무 착한 사람이라서, 귀여운 걸 본인만 몰라서, 허세 같은데 싫지 않은 적은 처음이라서, 영원을 약속하고 싶게 만든 사람이라서.. 이유는 수백 개 수천 개지만 그 정도로 당신이 좋은 이유가 수두룩 빽빽한데 이 이야기를 전할 수가 없습니다 이”
- 👍88 [#691] “김호중 테너의 활동 영상 발굴해서 많이 많이 올려주세요. 이미 완성된 테너 김호중 감동입니다.”
- 👍88 [#691] “기다렸습니다 김호중 테너님 공연 많이올려주시면 좋겠 습니다 영상감사합니다 🎉🎉🎉”
- 👍77 [#856] “할렐루야 주님께 영광돌립니다 . 호주에서 5년 살고 컴백한 시골사역 사모예요. 한국 정읍시 오주길 ~ 작은마을 개척교회사모입니다. 저희는 교회 사역에 필요한 야채 식료품 밭에서 직저자배해서 성도님들 섬기며 네팔에서 3월에 온 자매 형제님 선교도합니다. 한글공부 집중 중입니다 요즘 시골에 한국사람 없어 전도가 쉽지 않은데 네팔 🇳🇵 성도님들 제자삼아 성장시키”
- 👍76 [#1091] “파란색으로 블루베리도 만들어주세요!!!!”

### 아쉬운 점 — 영상 (제목·광고·길이·정보 오류·목소리) — 좋아요 많은 댓글

- 👍632 [#206] “현재 08년생 입니다.. 벌써 마지막 10대의 절반이 지났다는게 믿겨지지 않네요. 어릴때 저녁밥 먹기 전 동네 친구들과 술래잡기 하던게 엊그제 같은데 저에겐 항상 멀게만 느껴졌던 20대라는 현실을 곧 마주할 생각을 하니 솔직히 현실감이 없습니다.. 아직 추억도 많이 없고 즐기지못한게 많은거 같아 맨날 옛날로 돌아가고 싶다는 생각을 하곤 하는데 몇년 뒤엔 오”
- 👍70 [#809] “18년을 함께한 우리 고양이가 고양이별로 떠난지 4일째 되는 밤입니다. 집안 모든 곳이 냥이와 함께한 곳이라 가는 곳마다 눈물이 납니다. 마치 그곳에 앉아 있는 것 같아 나도 모르게 두 손을 뻗곤 합니다. 원없이 사랑한 것 같았는데 보내고나니 아쉬움과 후회만 밀려옵니다.”
- 👍64 [#703] “광고가 계속 나와요😢😢”
- 👍57 [#839] “가사는 모르지만, 애절하면서 흡인력 있는 목소리가 너무 좋습니다.”
- 👍51 [#691] “오늘 김호중 가수의 노래를 이것저것 찾아 듣고 있는데 이 노래를 듣게 되네요. 김호중 테너의 목소리가 너무 듣기 좋습니다. 이애숙님과 두 분 함께 부르는 노래가 완전 멋지네요. 올려주셔서 감사합니다 ~”
- 👍49 [#474] “남편의 계속 반복되는 외도로 어린아들 둘 데리고 이혼한지 9개월 눈물 흘릴 여유조차 없이 살다가 노래들으려고 켠 유튜브에서 우연히 발견한 노래들.. 마음을 보듬어 주는것같은 따뜻한 목소리에 눈물이 터져 울고 위로받고 갑니디 원래 안달지만 꼭 달고싶었어요. 오래 노래해주세요. 자주와서 들을게요. 너무 고맙습니다.”
- 👍45 [#682] “요즘 유튜브나 여러 플랫폼에서는 AI 기술을 활용해 특정 가수의 창법이나 음색을 학습시킨 커버 곡들이 정말 많이 쏟아지고 있네요. 특히 전통적인 록 발라드나 트로트 메들리 같은 영상 중에는 사람이 직접 부른 것처럼 정교하게 만들어졌지만, 실제로는 AI 목소리 모델을 입혀서 기계적으로 양산된 콘텐츠들이 꽤 많습니다. 음색이나 부르는 스타일이 지나치게 정형화되”
- 👍45 [#773] “AI로 작업했더라도 주인장 음악력 진짜 높은 듯. 듣기 편안한데 지루하지 않음.”

### 반박·불만 — 의견 다름 (내용) — 좋아요 많은 댓글

- 👍807 [#926] “다니엘 웃기는거 빼고 다 잘하네 🥰”
- 👍155 [#108] “선곡말도안됨”
- 👍142 [#1039] “아 메이플 관련 브금이랑 영상만 보면 저때로 돌아가고 싶다라는 생각이 계속 든다.. 무더운 여름방학 집에 에어컨도 없어서 방에서 선풍기 하나로 동생과 싸우고 한대 있는 컴퓨터로 너가 몇분을 더했니 어쨌니 그러다가 게임 금지 당하고.. 동생보다 30분이라도 먼저 일어나서 몰래 게임하고.. 지금은 동생도 나도 너무 많이 커버렸구나. 어렸을때 형이란 이유도 동생”
- 👍132 [#217] “-내가 약조하마.너를 지켜주겠다고. 그렇게 다정히 말씀하시던 든든한 나의 님은, 지금 풀숲에 쓰러져 간신히 숨만 내쉬고 계신다. -상공, 제발 숨만 쉬십시오. 제가 어떻게든... -연화야. 상공의 손이 나의 손은 따스히 잡아온다.그 온기가 서글프도록 따뜻해서, 심장 한편이 저릿하게 아려온다. -아닙니다, 그러지 마십시오. 지금이라도 의원을 부르면.. -너도”
- 👍113 [#295] “제목을 보자마자 한사람이 떠올라서 홀린듯이 클릭해버렸어요. 이런 플리 잘 안들을 것 같아서 그냥 터놓고 말할게. 중학교 때 처음 만난 언니. 정말 예쁘고, 멋지고 빛이 나서 이보다 주인공 같은 사람이 있을까 싶은 사람. 정병 와서 새벽에 연락해도 꼬박꼬박 답장해주고 내가 힘들때 옆에서 참 많을 위로를 해주었던 건 정말 아직도 고마워. 내가 죽지 않고 이렇게”
- 👍91 [#238] “탈북할 땐 어떤 노래를 듣는걸까 하고 왔는데 첫곡듣고 어이없어서 터졌네 ㅋㅋㅋㅋ 무슨 관련이야”
- 👍47 [#241] “왜 우리는 아는 사람들에게 위로받지 못하고 모르는 사람들에게 인터넷상에서 위로를 받는 걸까요 힘들다고 말하는 게 부끄러운 것도 아닌데 다른 사람들의 댓글을 보며 와.. 이런 사람들도 있구나 저런 사람들에 비하면 나는 행복한 거구나..라고 위안 삼으며 다시 또 지옥같이 지치는 일상으로 돌아가는 사람도 있고 다른 사람들의 댓글을 보며 위로를 받고 살아갈 용기를”
- 👍45 [#691] “너무잘한다 이런인재를 순간의 실수에 너무오래 가둬놓네 엄청난죄 지은 사람들도 다풀어주고 아예법의재제도 안하면서 국보급 가수한태는 왜그리 독한지 참어이없는 사법부다”

### 정치·사회 (영상과 무관한 의견) — 좋아요 많은 댓글

- 👍623 [#809] “사랑하는남편이 하늘나라가신지 두달하고십사일째입니다~ 제마음을 위로해주네요~”
- 👍522 [#191] “9:06 중국인들 탑 랩 파트, 학교를 안 갔어, 오빠오삐옵, 싸이노래 개좋아함”
- 👍85 [#691] “이런노래들으니 이나라가 얼마나 귀한지 모르겠습니다 망하는나라 한순간 우리가 모두 힘내어 지켜야 합니다”
- 👍79 [#926] “대한 외국인 중에서 한국인보다 역사를 많이 아는 다니엘~~ 굿입니다~~^^”
- 👍32 [#788] “멎있는예술의나라인데~전쟁하지않으면좋겠다두나라가파괴되는게너무아깝다~제발세계펑화를후손들위해~음악이웅장하고뭉클합니다”
- 👍26 [#87] “난 한국인인데 한국 사람들한탠 이런 이미지가 없단게 너무 슬프다 러시아나 다른 나라들의 사람들이라 하면 다들 각자의 신비롭고 그런 이미지들이 있는데 한국인이라고 하면 그냥 kpop이니 뭐니 하는 그런 재미없고 오글거리는것들밖에 없으니까 너무 아쉬움 정부가 한국콘텐츠진흥원같은거까지 만들어가면서 지원하지만 않았어도 이렇겐 안됬을거같다 그냥 차라리 스타크레프트 ”
- 👍24 [#20] “그냥 케이팝,드라마,예능 다 2010년대 이후로 이제 옛날같지않더라 케이팝으로 유명하던 우리나라가 더 이상 그냥 챌린지하는 노래밖에 안나오고..어제 청룡?보니까 확실히 전과 다름 연말에 가족끼리 시상식보는 감성도 사라진듯 다 모르는것들만 나오고 옛날엔 드라마도 지금보면 ㄹㅈㄷ인거 많이 나오고 예능도 신서유기,무도 등등 지금보면 ㄹㅈㄷ인거 많았는데 지금 보면”
- 👍23 [#667] “이재성..가장 뛰어난 싱어송라이터였는데.. 고독한DJ라는..노래불렀다가....전두환정권에서.방송금지당해..최전성기..87년에...갑자기TV에서.사라졌고.. 라디오에서도 이재성 노래를 10년동안 들을수 없었음.”

### 경험 공유 (내 이야기) — 좋아요 많은 댓글

- 👍2,673 [#198] “야 보고싶어 내 생일에 연락 왜 안했냐 너 밥 한끼 더 좋은거 먹으라고 네가 기념일마다 줬던 토스 기프티콘 일부러 안 썼어 너한테 입금 됐냐 돈 하나도 안 아까운데 그냥 그렇다고 내 계좌 비밀번호 우리 만난 날이야 내 노트북 비밀번호도 우리 만난 날이야 훔쳐가도 되는데 홍대에서 이제 공연해? 아직인가 너한테 기타 쳐달라고 했던 노래가 하필 이 영상 첫 노래”
- 👍2,513 [#206] “내가 왜 고3일까… 평생 안 올 줄 알았는데 ㅠㅠㅠㅠ 뽀로로 너랑 걱정없이 놀 때가 너무 그리워…”
- 👍1,898 [#206] “뉴스에서 고등학생 자살율 얘기할때 진짜 이해 안됐는데 막상 고등학생 되니까 내가 그 경계에 서있네”
- 👍1,308 [#446] “나도 모르게 "아 지랄 ㅋㅋ" 하면서 들어왔네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 아 미친”
- 👍1,252 [#967] “영상 내려가서 내가 멘헤라될뻔”
- 👍1,217 [#1060] “하트누르면 모두들 행복해지고 시험 잘 볼 거임!! 나도 포함”
- 👍1,132 [#198] “이 세상 단 둘만 가진 기억인데 아까워서 어떻게 잊나요 내가,”
- 👍1,069 [#241] “요즘 옥상문이 잠겨있네요 더워서 그런가 벌써 네 건물 가봤는데 잠겨서 죽고싶은데 마음데로 죽지도 못하네요 얼마전에 울다가 깨닳았어요 아 나 안죽고싶은데.. 내가 죽고싶은게 아니라 지금이 너무 힘들어서 차라리 죽고싶은거구나 아 행복해지고 싶은거구나 죽고싶은게 아니라 행복해지고 싶은데 행복이 저는 너무 어려워요 행복하고싶었던거라는 생각이 들지마자 너무 서러워서”

### 구독·다음 기대 — 좋아요 많은 댓글

- 👍110 [#819] “듣다보니. 가슴에 스며들어 구독하고. 계속 듣게 되네요 60후반이지만 요즘 젊은이들 조선힙합이 꽂치네요 좋은음악. ~^^❤❤❤”
- 👍105 [#691] “김호중님의 무대가 기다려집니다”
- 👍75 [#1004] “슬프고도 정화된 아름다운 선율 듣자마자 바로 구독하고 영혼의 단짝 친구와 공유했습니다 평생을 추구해온 제 삶의 궤적을 위로해주는 선율과 가사는 눈감고 들어도 한마디 한마디가 너무나 아름답습니다 저를 숨기고 제 슬픔을 숨기고 제 진실을 숨기고 모두에게서 옹달샘처럼 숨어있는 제 영혼이 공감받고 위로받는 듯 했습니다 이 채널을 준비해주신 그대에게 감사를 전하고자”
- 👍48 [#731] “구독박고 갑니다 태어나서 이렇게 섹시한 남자 첨이에요 허남준땜시 잠이 안와요 매일 유투브로 찾아봐도 질리지 않아요 ㅋ”
- 👍42 [#881] “썸녜일도 느낌.있고.음악도 좋네요 ! 음악은 ai로 만드신건가요?궁금. 그림도 왠지 직접그리신듯 구독하고가요😊”
- 👍32 [#276] “이별 벌써 20년째 저는 가족 반대 때문에 헤어진 한남자 잊지 못합니다 지금 도 그사람 잊지 못합니다 아니 영윈히 기다려요 이노래가 아퍼요 그사람 마음 같아😢”
- 👍18 [#529] “아침찬양에 너무 잘 맞는 목소리와 은혜입니다. 첫곡듣고 바로 구독했습니다”
- 👍17 [#672] “첨들어봤는데 넘좋아서 바로 구독했어요. 50대 주부~😊”

### 8-1. 더 알고 싶은 것 ① 요청 — 다뤄 주세요·알려 주세요·궁금해요 (748개 중 좋아요 순, 영상마다 2개까지)

- 👍6,477 [#446] “대체 뭔노래가 나올까 궁금해서 들어왔습니다”
- 👍1,047 [#407] “개발할 때마다 듣습니다; 많이 올려주세요”
- 👍88 [#691] “김호중 테너의 활동 영상 발굴해서 많이 많이 올려주세요. 이미 완성된 테너 김호중 감동입니다.”
- 👍88 [#691] “기다렸습니다 김호중 테너님 공연 많이올려주시면 좋겠 습니다 영상감사합니다 🎉🎉🎉”
- 👍77 [#856] “할렐루야 주님께 영광돌립니다 . 호주에서 5년 살고 컴백한 시골사역 사모예요. 한국 정읍시 오주길 ~ 작은마을 개척교회사모입니다. 저희는 교회 사역에 필요한 야채 식료품 밭에서 직저자배해서 성도님들 섬기며 네팔에서 3월에 온 자매 형제님 선교도합니다. 한글공부 집중 중입니다 요즘 시골에 한국사람 없어 전도가 쉽지 않은데 네팔 🇳🇵 성도님들 제자삼아 성장시키”
- 👍76 [#1091] “파란색으로 블루베리도 만들어주세요!!!!”
- 👍69 [#978] “나중에 브금 매쉬업버전 말고 각각 올려주시면 안될까요”
- 👍68 [#597] “8주된 뱃속의 아기를 와이프와 보내고 상심이 큰 어제와 오늘이었습니다. 와이프에게 어떻게 하면 힘이 될 수 있을까 하다 우연히 듣게 되었는데, 마치 고즈넉한 숲 속 궁전에서 여유로운 하루를 맞이하는 느낌을 주는 노래 같아 하루 종일 듣고 있습니다. 힘 내볼게요. 앞으로도 좋은 노래 많이 올려주세요”
- 👍62 [#597] “최고에요! 제 브이로그 배경음악으로 클래식을 많이 쓰는데, 혹시 출처표시하고 bgm으로 쓸 수 있을까요? 안되더라두 괜찮으니 편하게 알려주세요! 좋은 음악 감사합니다! :)”
- 👍54 [#415] “아 진짜 주인장 제발 이 플레이리스트 더 길게 만들어주세요 제발요”
- 👍47 [#881] “트랙리스트 위에있는 글은 주인장님이 써내려간 글귀일까요? 너무 멋져요.. ❤ 혹시 책의 한 소절이라면 제목을 알려주실 수 있으실까요😊”
- 👍45 [#123] “첫번째 나온 노래 너무 좋은데 가수랑 제목좀 알려주세요.. 아무리 찾아도 안나와요 😢”
- 👍41 [#704] “혹시 투어스 노래 모음 만들어 주실수 있나여..?”
- 👍35 [#33] “개조아요 타임라인 올려주세요”
- 👍33 [#874] “우선 이런 질문드려 죄송합니다. 제 생애 최고의 전율을 느꼈습니다. 그래서 무지한 질문을 드리더라도 용서부탁드립니다. 유튜브 보다가 떠서 감상하게 되었는데, 어느분이 부르신걸까요? 혹시 설명란에 있는것처럼 ai로 만드신 걸까요?”
- 👍32 [#333] “저런 얼굴하고 물어보면 어 아니 너가 훨씬 나아 가 나올듯 노래 리스트가 너무 좋아유 계속 올려주세요!”
- 👍32 [#993] “호르몬제는 무서워서 못 먹고 영양제 알아보던 중이에요. 한 번 깨면 다시 잠드는 게 너무 힘들어요. 흡수 잘 된다는 리포좀멜라토닌에 감태·레몬밤·가바 같이 들어간 각성완화제 먹고 있는데 엄청 센 건 아닌데 누우면 좀 차분해지긴 하더라고요. 같은 나이대 분들 어떻게 넘기시는지 궁금하네요.”
- 👍30 [#230] “진짜 ' '서운 이야기 띵!... 똥!... 유튜브 댓글에 알람이 떴어. "저 브라질 펑크에 관심이 많은데 이 분이 브라질 펑크 부른거만 모아서 영상 만들어 주실 수 있나요?" 그냥 자기가 듣고 찾아서 모음 딸깍하면 되는 황당한 요구를 하다니.. 저 사람은 너무 '오만'해 그 때.. '궈바오러우'가 나타났어”
- 👍30 [#674] “55분에 시작하는 노래 가수와 제목좀 알려주세요ㅜㅜ”
- 👍29 [#108] “진짜 댓글 앵간하면 안쓰는데 이거 조합 ㅈ됨 너무좋다 여자여자스러운데 당당하고 자존감높은 여자 플리임 이런거 너무 좋아서 맨날 들을거 같음 더 만들어주세요❤”
- 👍29 [#1004] “아다지오 평소에 사랑헸던 곡입니다...윌리엄님의 올리신곡은 또다른 멋으로 다가옵니다.사랑합니다.축복합니다.감사합니다.늘 좋은 음악.아름다운음악 부탁드립니다. 건강하세요”
- 👍27 [#978] “지킬만 분리해서 올려주세요 따로도 듣고 싶어요”
- 👍23 [#179] “노래다운받는방법 알려주세요”
- 👍23 [#644] “안녕하세요!오산중학교에다니는 3학년학생입니다.기술시간에 선플달기를 하고있는데 요즘 점점여름이 다가오는시기여서 그런지 이영상이 알고리즘에 떴더라고요!시원한 여름플리너무 잘만들어주셔서 잘들을것같아요!모두 시원한여름보내시고 앞으로더 좋은영상 많이 만들어주세요💕”
- 👍22 [#936] “청주에서 나주로 오는길에 우연히 들었는데 3시간 거리동안 거의 2시간을 무한반복 하면서 들었네요 덕분에 심심하지 않게 잘 내려왔습니다. 당신은 천재 이십니다. 감사합니다.계속 좋은음악 부탁합니다.😊”
- 👍21 [#402] “너무 시원하고 감동적인 노래 잘듣고 갑니다 앞으로도 더욱 많은 노래 올려주세요”
- 👍20 [#452] “순천부영초등학교 이지인입니다 이챌린지을많이봤어요 이노래를듣으면 우울할때기분이 좋아져서이노래에 댓글을달았어요앞으로 신나는노래많이 올려주세요”
- 👍20 [#491] “낮엔 피곤한데 밤엔 또렷해서 멜라토닌 알아봤네요. 요즘 부쩍 잠이 얕아지고 감정 기복에 잠까지 설쳐요. 일반 멜라토닌은 흡수가 별로라길래 리포좀멜라토닌에 가바·테아닌까지 든 각성완화제로 바꿔봤는데 엄청 센 건 아닌데 누우면 좀 차분해지긴 하더라고요. 같은 또래 워킹맘분들은 어떻게 관리하시나 궁금해요.”
- 👍20 [#609] “궁금해서 들어왓는데 이쫀득한 스캣출발 뭐여....”
- 👍20 [#679] “불면으로 힘들어하는 50대입니다. 수면제 10년째중이구요. 이 음악으로 마음의 평안을 얻습니다. 유투브에 저장해서 비행기에서도 무한반복이구요. 요즘 체력적으로 힘든치료 받고 온 날 해당음악 귀에 꽂고 누웠다 주말 낮에 잠깐씩 자는 기적이 생기네요. 첫번때 남자테너 목소리만 다시 돌려들고 다시 돌려듣고.. 첫번째 남자테너 목소리 한시간짜리 무한반복 업데이트 ”
- 👍20 [#983] “아들건강하게 해주시고 대운 부탁드립니다❤❤❤❤❤❤❤”
- 👍19 [#626] “넘 멋찌 십니다 제목 알고 싶어요”
- 👍19 [#674] “1시 9분 가수좀 알 수 있을까요?? 노래제목좀 부탁드려요 🙏”
- 👍19 [#969] “멜론에도 올려주세요 제발”
- 👍18 [#922] “혹시 실제 부르시는건지 AI 인지 궁금하네요 너무 은혜로와서~ 너무 잘하셔서~~”
- 👍17 [#660] “2번째 노래 제목 좀 부탁드립니다. 너무 좋아요”
- 👍16 [#926] “뭐야!!!!!!!터치❤❤이제까지 숨기고 있던거야??지성 넘치는건 익히 알았지만 감성까지 넘치네.뱃노래도 언젠가 부탁합니다”
- 👍16 [#1054] “축하드립니다!! 계속 은혜로운 찬양 부탁합니다^*^”
- 👍15 [#261] “노래 제목 부탁드립니다 아재라서 하나도 몰라요 ㅜㅡㅜ 40중반 아저씨의 간곡한 부탁입니다 ~!!!”
- 👍15 [#550] “첫번째 곡이랑 비슷한 노래 추천 좀 해주세요ㅠ 첫 곡이 너무 좋은데 찾아봐도 없어요ㅜㅜ”

### 8-2. 더 알고 싶은 것 ② 물음표 질문 (반문이 섞임 — 좋아요 순, 최상위 댓글)

- 👍945 [#679] “너무나 꿈같은 아들을 먼저 보냈습니다 33세의 꽃같은 나이에 바람이 되어 빛되어 제 주변에 맴 도는것 같습니다 세상의 어떤말도 표현 되어지지 않는 비 현실감.. 저의 모든것이었던 아들의 목소리를 더 이상 들을수 없는지 오늘이 51일째... 통곡의 울음조차 낼 수 없습니다 아들이 힘들어 할까봐.. 아빠를 너무 많이 닮은 아들. 모든면에서 너무나 비범했던 아들”
- 👍208 [#198] “여전히 잊지 못하였습니다. 당신이 나의 이상형이라서, 당신이 나의 첫사랑이라서, 끝난 관계임에도 나에게 잘 해줘서, 너무 착한 사람이라서, 귀여운 걸 본인만 몰라서, 허세 같은데 싫지 않은 적은 처음이라서, 영원을 약속하고 싶게 만든 사람이라서.. 이유는 수백 개 수천 개지만 그 정도로 당신이 좋은 이유가 수두룩 빽빽한데 이 이야기를 전할 수가 없습니다 이”
- 👍56 [#241] “어릴 땐 어른이 부러웠습니다. 아무거나 다 할 수 있는. 하지만 정작 어른이 된 저는 삶에 휩쓸려 무뎌지고 부서진, 그런 사람이라는 걸 깨닫게 되었습니다. 우리 다시 돌아갈 수 있을까요? 아무 걱정 없이, 아무 생각도 안 하는 그때로”
- 👍32 [#691] “오 😮이 반가운 영상 어떻케 오늘에야 만나죠? 언제인가요? 김호중 코리아나 이애숙님. 이죠?”
- 👍31 [#956] “언제 상송이 나오죠?”
- 👍16 [#11] “제 연인이 표현을 잘 안하는 편이에요 근데 저는 표현도 많이 하고 남자지만 불안형이거든요 연애초긴 하지만 그녀의 마음이 어떤지 연락도 잘 안될땐 뭘 하는지도 궁금하고 불안하고 그래요 어떻게 고칠까요?”
- 👍15 [#651] “뮤비좋은데 라이브 가능한가요?”
- 👍15 [#871] “혹시 첫 번째 노래 가수를 있을까요? 검색으로는 안 나와서요ㅜㅜ 가사를 보고 싶은데ㅜㅜ”
- 👍15 [#964] “안녕하세요~ 혹시 이 음악을 행사 진행 중에 사용하기 위해 다운로드할 수 있을까요? 감사합니다🙏🏼너무 좋아합니다❤️‍🔥”
- 👍13 [#319] “와~~ 정말 가슴이 뻥 뚫리고. 머리가 신선해집니다 어쩜 저런 보물이 있을까요? 수연양!!! 사랑합니다 할아버지 할머니랑 영원히 행복하세요~~~!!”
- 👍13 [#712] “가수가 어떻게 되나요?”
- 👍12 [#673] “혹시 배경 어딘지 정보알수있을까요?”
- 👍12 [#822] “혹시 흘러나오는 여자 목소리 가수이름 알수있을까요? 엄마가 궁금해하셔서요ㅠ”
- 👍11 [#431] “집사람이 좋아하네요 혹시 악보를 구입할수있을까요??”
- 👍11 [#967] “혹시 저 그림 웹툰이면 제목 알수있을까요?”
- 👍10 [#175] “이 노래를 들으면서 떠오르는 계절은 어느 계절인가요? 봄, 여름, 가을, 겨울 중 하나를 골라주세요. 🍂”
- 👍10 [#321] “영상의 사진이 어디서 나온 것인지 알 수 있을까요?”
- 👍10 [#774] “혹시 기뻐하며 경배하세 MR 어디서 구할 수 있을까요? 딸아이 결혼식에 혼주 입장곡으로 쓰고 싶어서요~”
- 👍8 [#198] “저두 가슴이 미어지는 사랑을 해보고싶어용 이성적인 감정은 언제 생기는건가요? 아무리 봐두 친구로밖에 안느껴지는데…”
- 👍8 [#415] “사진 출처 어딘지 알수있을까요?”

### 8-3. 아쉬운 점 — 영상에 대한 비판 (좋아요 순, 답글 포함)

- 👍632 [#206] “현재 08년생 입니다.. 벌써 마지막 10대의 절반이 지났다는게 믿겨지지 않네요. 어릴때 저녁밥 먹기 전 동네 친구들과 술래잡기 하던게 엊그제 같은데 저에겐 항상 멀게만 느껴졌던 20대라는 현실을 곧 마주할 생각을 하니 솔직히 현실감이 없습니다.. 아직 추억도 많이 없고 즐기지못한게 많은거 같아 맨날 옛날로 돌아가고 싶다는 생각을 하곤 하는데 몇년 뒤엔 오”
- 👍70 [#809] “18년을 함께한 우리 고양이가 고양이별로 떠난지 4일째 되는 밤입니다. 집안 모든 곳이 냥이와 함께한 곳이라 가는 곳마다 눈물이 납니다. 마치 그곳에 앉아 있는 것 같아 나도 모르게 두 손을 뻗곤 합니다. 원없이 사랑한 것 같았는데 보내고나니 아쉬움과 후회만 밀려옵니다.”
- 👍64 [#703] “광고가 계속 나와요😢😢”
- 👍58 [#20] (답글) “진짜요..ㅜㅜ다시는 이런 케이팝만의 분의기를 못 본다는게 너무 아쉬움…”
- 👍57 [#839] “가사는 모르지만, 애절하면서 흡인력 있는 목소리가 너무 좋습니다.”
- 👍51 [#691] “오늘 김호중 가수의 노래를 이것저것 찾아 듣고 있는데 이 노래를 듣게 되네요. 김호중 테너의 목소리가 너무 듣기 좋습니다. 이애숙님과 두 분 함께 부르는 노래가 완전 멋지네요. 올려주셔서 감사합니다 ~”
- 👍49 [#474] “남편의 계속 반복되는 외도로 어린아들 둘 데리고 이혼한지 9개월 눈물 흘릴 여유조차 없이 살다가 노래들으려고 켠 유튜브에서 우연히 발견한 노래들.. 마음을 보듬어 주는것같은 따뜻한 목소리에 눈물이 터져 울고 위로받고 갑니디 원래 안달지만 꼭 달고싶었어요. 오래 노래해주세요. 자주와서 들을게요. 너무 고맙습니다.”
- 👍45 [#682] “요즘 유튜브나 여러 플랫폼에서는 AI 기술을 활용해 특정 가수의 창법이나 음색을 학습시킨 커버 곡들이 정말 많이 쏟아지고 있네요. 특히 전통적인 록 발라드나 트로트 메들리 같은 영상 중에는 사람이 직접 부른 것처럼 정교하게 만들어졌지만, 실제로는 AI 목소리 모델을 입혀서 기계적으로 양산된 콘텐츠들이 꽤 많습니다. 음색이나 부르는 스타일이 지나치게 정형화되”
- 👍45 [#773] “AI로 작업했더라도 주인장 음악력 진짜 높은 듯. 듣기 편안한데 지루하지 않음.”
- 👍40 [#788] “너무 너무 멋진 분위기 취할수있는 선율. 감흡! 늦은밤까지 이어질듯요 무한반복~~😊😊😊”
- 👍38 [#1081] “그저 사막을 지나 가는 것 같던 20대 나의 맘 속에 요술 왕자 당신은 누구신가요 아무도 모르지만 탱탱볼을 던지고 사라지는 꿈을 쫓다 지치길 지나 나의 미래에게 Waiting for your calling back 반복되는 감정의 미끄럼틀 그리고 오늘 아침 미국에서 만나는 신나는 음악, 잘못된 인생 술탄 오브 더 디스코는 나의 청춘 고마워요, 술탄 혼자 외”
- 👍35 [#529] “두분다 목소리가 너무 좋으셔서 자꾸 듣게되요~찬송가도 너무좋지만 목소리가 엄청 편안하고 부드러워요”
- 👍34 [#859] “제 노래 스퇄일 최고입니다😊 가수 목소리 좋고 선곡도 최고 운동할때 이어폰 귀에 꼽고❤ 한시간 넘게 운동하는데 지루함 없이 운동합니다 대박 기원합니다🎉🎉🎉🎉🎉”
- 👍33 [#722] “역시나 보이스칼라가 독보적입니다.언제들어도 너무 감동입니다. 영상편집이 정성이 많이 들어간게 보이네요,보는 내내 웃게 되네요.👏👏👏👏👏👏👏👍👍👍김호중 테너 너무보고싶네요.무대에 서신 모습 빨리 보고싶어요”
- 👍27 [#19] (답글) “이 뮤직비디오를 보이콧해 주세요. 이 영상과 제니의 다른 몇몇 영상에는 자막이 없습니다. 청각 장애가 있는 사람으로서, 가사와 노래 속에서의 위치까지 완전히 외우기 전까지는 자막 없이 뮤직비디오를 보면서 노래 내용을 이해하기가 어렵습니다. 제니는 돈도 많고 팀도 큰데, 뮤직비디오에 자막을 넣을 사람을 구하는 건 식은 죽 먹기일 텐데요. 이건 무지한 행동입니”
- 👍26 [#11] “가장 헷갈린 시기 같아요 잘하고 있다고 누가 꼭 안아주면 좋겠어요 열심히 살았는데 아쉬움이 항상 남네요”
- 👍26 [#407] “이거 들으면서 학원 숙제 베꼈는데 밀려써서 걸렸습니다 조심하세요”
- 👍23 [#665] “청춘은 서툴기에 그 자체로 빛난다. 완벽하다면 너무 지루할테니까..”
- 👍23 [#671] “AI목소리든 아니든 지친 영혼을 달래주면 그뿐. 감상잘했습니다 ^^”
- 👍22 [#936] “청주에서 나주로 오는길에 우연히 들었는데 3시간 거리동안 거의 2시간을 무한반복 하면서 들었네요 덕분에 심심하지 않게 잘 내려왔습니다. 당신은 천재 이십니다. 감사합니다.계속 좋은음악 부탁합니다.😊”

## 9. 사례별 자세히 (따로 — 40개씩)

사례마다 챕터·설명 앞부분·대본(첫 20초·첫 1분·90초마다 흐름)·같은 채널 평소 영상·댓글 갈래와 인용 (같은 # 번호):

- `analysis_cases_01.md` — #1–#40
- `analysis_cases_02.md` — #41–#80
- `analysis_cases_03.md` — #81–#120
- `analysis_cases_04.md` — #121–#160
- `analysis_cases_05.md` — #161–#200
- `analysis_cases_06.md` — #201–#240
- `analysis_cases_07.md` — #241–#280
- `analysis_cases_08.md` — #281–#320
- `analysis_cases_09.md` — #321–#360
- `analysis_cases_10.md` — #361–#400
- `analysis_cases_11.md` — #401–#440
- `analysis_cases_12.md` — #441–#480
- `analysis_cases_13.md` — #481–#520
- `analysis_cases_14.md` — #521–#560
- `analysis_cases_15.md` — #561–#600
- `analysis_cases_16.md` — #601–#640
- `analysis_cases_17.md` — #641–#680
- `analysis_cases_18.md` — #681–#720
- `analysis_cases_19.md` — #721–#760
- `analysis_cases_20.md` — #761–#800
- `analysis_cases_21.md` — #801–#840
- `analysis_cases_22.md` — #841–#880
- `analysis_cases_23.md` — #881–#920
- `analysis_cases_24.md` — #921–#960
- `analysis_cases_25.md` — #961–#1000
- `analysis_cases_26.md` — #1001–#1040
- `analysis_cases_27.md` — #1041–#1080
- `analysis_cases_28.md` — #1081–#1114
