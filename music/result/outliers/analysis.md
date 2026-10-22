# 음악 — 성공 사례 분석 (지시사항 재료)

자동 생성 — `tools/success_analysis.py` v1.5.1 (2026-10-22 07:59 UTC), 규칙 `music/analysis_rules.toml` v1.5. **이 문서는 숫자와 원문만 담는다 — 해석·지시사항은 이것을 읽는 AI 가 만든다.** 주별 추세는 `weekly.md`, 승인한 영상 전부는 `approved.md`. ※ 연구·교육용 — 투자 권유가 아님.

## 0. 자료와 한계

| 자료 | 수 |
|---|---|
| 사례 폴더 (설명·자막·댓글·썸네일을 받은 영상) | 1498 (웹 승인 1498) |
| **성공 사례** — 180일 안·구독자 50,000 이하·조회수 ≥ 구독자 × 3·10,000회 이상·4분 이상, 채널당 2개 | **1088** (기준 통과 1265 − 뺀 것 43 − 채널당 제한 134) |
| **하루 조회수 상위** (1-3번 — 성공 사례와 따로) — 검색에서 찾은 주제 관련 4분 이상 영상 2,839개 중 하루 조회수 상위 10% (하루 28,800회 이상), 구독자·올린 날짜 상관없이, 채널당 2개 | **211** (기준 통과 246 − 뺀 것 28 − 채널당 제한 7) · 자료를 받지 않은 후보 68 |
| 성공 사례의 글 출처 (자막·음성인식·설명·없음) | 설명 1013 · 없음 75 |
| 성공 사례 대본 — 전체 · 앞부분만(음성인식 1차) · 없음 | 0 · 0 · 1088 |
| 같은 채널 기준선 (채널 평소 영상) | 성공 사례 977/1088 · 채널 1026곳 (잘된 영상 3536 · 평소 영상 4143) |
| 성공 사례 댓글 (받은 / 달린) | 419,828 / 437,536 |
| 성공 사례 썸네일 | 1088 |
| 비교 집단 — 탐색에서 본 영상 중 구독자 50,000 이하·4분 이상·365일 안·주제 관련, 채널당 최근 5개 | 5840 (성공 1159 = 20%, 채널당 제한으로 뺀 22787) |
| 자료를 받지 않은 성공 후보 (웹 화면에서 승인하면 들어감 — 채널당 자리가 남은 것만) | 694 (자리가 찬 채널의 2,771개 뺌) |
| 수요·공급 시장 — 최근 90일 영상 (채널 크기 상관없음) | 881 · 검색어 61 · 자동완성 말 505 (공급 확인 0) |
| 채널 성장 자료 (개설일이 있는 채널) | 2147 (빨리 크는 작은 채널 25) |

성공 기준은 넘었지만 뺀 영상: Main Kabhi Bhoolunga Na Tujhe… (광고 의심(좋아요·댓글 거의 없음)) · SAD LO-FI 🥺 💔 2026 Ultimate M… (광고 의심(좋아요·댓글 거의 없음)) · Repvblik - Sandiwara Cinta (K… (광고 의심(좋아요·댓글 거의 없음)) · Baby Bear ∣ Colorful Caterpil… (광고 의심(좋아요·댓글 거의 없음)) · "Free" Cover ∣ Rumi Was Left … (광고 의심(좋아요·댓글 거의 없음)) · 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 틀기만 해도 기분이 좋아지는 가을 플… (광고 의심(좋아요·댓글 거의 없음)) · Nain Tere 🖤 Slowed + Reverb ∣… (광고 의심(좋아요·댓글 거의 없음)) · মন ছুঁয়ে যাওয়া বাংলা ∣∣ Bes… (광고 의심(좋아요·댓글 거의 없음)) · Dupatta Sarak Raha Hai 💕 ∣ Sl… (광고 의심(좋아요·댓글 거의 없음)) · I’d Rather – Acoustic + Saxop… (광고 의심(좋아요·댓글 거의 없음)) · SAD LO-FI 🥺 💔 2026 Ultimate M… (광고 의심(좋아요·댓글 거의 없음)) · Dekhne walon ne kya kya nahi … (광고 의심(좋아요·댓글 거의 없음))

**한계**

- 대본(자막·음성인식)이 없는 성공 사례 1088개 (#1, #2, #3, #4, #5, #6, #7, #8, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26, #27, #28, #29, #30 …) — 설명란·챕터만 있음. 도입부·구성·말 속도는 대본이 있는 0개로만 셌다 (음성인식이 끝나면 다시 셈)
- 비교 집단 5840개 = 검색(조회수 순 — 잘된 영상 쪽으로 치우침)·추가한 채널·성공 사례 채널의 평소 영상 4589개 (치우침 없음) 에서 올린 지 7~365일 영상, 성공 비율 20% — 실제 시장 비율이 아니다. 같은 집단 안의 '있음/없음' 차이로만 보고, '무엇이 먹혔나'는 1-2번(같은 채널 안)을 먼저 보라
- 외국 영상을 넣음 (주제 설정 INCLUDE_FOREIGN = true) — 성공 사례 중 외국 영상 719개 (#1, #4, #5, #6, #7, #8, #9, #10, #13, #14, #15, #17, #18, #19, #21, #22, #23, #24, #26, #30, #33, #35, #36, #38, #39, #40, #41, #42, #43, #44). 말 속도(한글 음절)는 한국어 영상만으로 셌고, 제목 특징·댓글 갈래(질문·요청 등)는 한국어 낱말 규칙이라 외국 영상에는 거의 걸리지 않는다 — 외국 사례는 원문을 직접 읽어라
- 하루 조회수 상위 묶음(1-3번) 211개는 구독자·올린 날짜 상관없이 골랐다 — 큰 채널(구독자 50,000 넘음) 90개라 채널 힘(구독자·추천)이 섞여 있다. 작은 채널이 따라 할 근거는 1번 성공 사례로 보라. 하루 조회수 = 조회수 ÷ 올린 지 날수라 갓 올린 영상(며칠)은 부풀고 오래된 영상은 낮아진다. 경계는 검색 결과(조회수 순 — 잘된 쪽으로 치우침) 2839개 안의 상위 10%. 자료를 받지 않은 후보 68개 (웹 화면에서 승인하면 들어감)
- 같은 채널 기준선이 있는 성공 사례 977/1088개 (채널 영상이 5개 미만이거나 아직 못 받음)
- 수요·공급의 '시장'은 탐색·검색에서 본 최근 90일 영상 881개 — 검색이 조회수 순이라 조회수 적은 영상이 덜 잡힌다. 주제 묶음 사이의 상대 비교(지수)로만 보라
- 자동완성 말의 '최근 영상 수'는 우리가 본 영상만 셌다 — 실제 공급은 웹 화면 [공급 확인](말 하나에 검색 1번 = 100단위)으로 확인
- 자동완성 말에는 책·방송·사람·채널 이름도 섞인다 (예: '…를 찾아서'·'…지침서') — 영상 주제가 아닌 말은 건너뛰고 읽어라
- 채널의 최근 구독자 증가는 구독자 수를 3일 넘게 사이를 두고 두 번 이상 받아야 나온다 (7일마다 다시 받음)
- '구독자가 많이 모이는가'는 YouTube API 로 영상별 구독 증가를 볼 수 없다 — 대신 채널 성장(7번: 개설 뒤 월 구독자·받을 때마다 남긴 기록), '구독·다음 기대' 댓글, 배수(조회수÷구독자)로 본다
- 댓글 갈래·제목 특징은 낱말 규칙이라 거칠다 (물음표 반문도 '질문', 한 댓글이 여러 갈래). 원문 인용을 함께 보라
- '눈에 띔'은 차이가 크고 표본이 충분하다는 표시일 뿐 원인이 아니다

## 1. 성공 사례 (1088개 — 배수 큰 순)

배수 = 조회수 ÷ 구독자. **채널 평소 대비** = 조회수 ÷ 그 채널 최근 롱폼 조회수 중앙값 (같은 채널 기준선 — 클수록 그 영상만의 힘). 썸네일은 5번(장마다 20개, 번호 = #), 사례별 자세히는 **`analysis_cases_01.md` …** (9번).

| # | 제목 | 채널 | 구독자 | 조회수 | 배수 | 채널 평소 대비 | 하루 조회수 | 길이 | 업로드 | 주제 묶음 | 형식 | 글 출처 | 댓글 받은/달린 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Jay Wheeler, Omar Courtz - De Lejitos (Remix) (Video Oficia…](https://www.youtube.com/watch?v=xCkf2L7gFnI) | JayWheelerVEVO | 6,750 | 120,974,274 | 17,922.1 | ×161.3 | 832,932.6 | 4.7분 | 2026-05-30 | 기타 | 음악 | 설명 | 4,024/4,031 |
| 2 | [너의 차선](https://www.youtube.com/watch?v=B9zWtLub7tk) | 조선힙합 - Topic | 25 | 1,504,015 | 15,040.1 | ×98.7 | 13,421.7 | 4.2분 | 2026-07-02 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 0/50 |
| 3 | [노엘 IT'S YOU (한요한 없는 버전 10m)](https://www.youtube.com/watch?v=82Li_A-cPWA) | 갱갱 | 77 | 456,066 | 4,560.7 | – | 2,751.7 | 10.3분 | 2026-05-09 | 기타 | 플레이리스트·모음 | 설명 | 123/123 |
| 4 | [Tìm Em](https://www.youtube.com/watch?v=PnGk00MuNM4) | Hngle - Topic | 1,350 | 4,582,506 | 3,394.4 | – | 36,429.6 | 4.6분 | 2026-06-18 | 기타 | 음악 | 설명 | 0/227 |
| 5 | [ขึ้นใจ (3am call)](https://www.youtube.com/watch?v=r1Eb1qnqLzA) | Mirrr - Topic | 4,290 | 12,861,686 | 2,998.1 | ×570.2 | 141,081.6 | 4.4분 | 2026-07-23 | 기타 | 음악 | 설명 | 0/281 |
| 6 | [Veer Hanumana Ati Balwana Ram Ram Ratiyo Re ∣ Arji Hamari M…](https://www.youtube.com/watch?v=DJjel4bCD8A) | Studio Hariom | 1,180 | 2,587,078 | 2,192.4 | ×2,303.7 | 17,222.1 | 6.8분 | 2026-05-25 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 137/142 |
| 7 | [झूमका झूलनिया Slowed + Reverb ∣ KhesariLal Yadav ∣ Bhojpuri…](https://www.youtube.com/watch?v=UgjIqEE-Eok) | officialprince | 1,910 | 3,905,222 | 2,044.6 | ×781.0 | 52,982.7 | 4.5분 | 2026-08-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 327/335 |
| 8 | [Ye Tune Kya Kiya (Slowed + Reverb) 🎧 ∣ Lofi Version ∣ Once …](https://www.youtube.com/watch?v=jqVvhD8Bps4) | Vɪʙᴇ Bʏ Lᴏғɪ | 2,500 | 5,050,913 | 2,020.4 | ×4,146.9 | 58,015.4 | 4.8분 | 2026-07-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 363/369 |
| 9 | [Khat navajot Ahuja / BGM THE BEST SONG 🥰#viral](https://www.youtube.com/watch?v=KdCRd8wTjaA) | ANSHU FF 1M | 389 | 706,644 | 1,816.6 | ×5,564.1 | 5,354.3 | 4.9분 | 2026-06-12 | 기타 | 음악 | 없음 | 26/26 |
| 10 | [Tera Hua Sahiba](https://www.youtube.com/watch?v=43sXuUq5N08) | Garvit Soni -… | 1,440 | 2,460,353 | 1,708.6 | – | 22,759.3 | 4.7분 | 2026-07-06 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/74 |
| 11 | [그대 사랑하는사람 나였으면](https://www.youtube.com/watch?v=E0EJikB3jg4) | ㅠㅁㅠ | 191 | 323,292 | 1,692.6 | – | 5,392.7 | 27.9분 | 2026-08-23 | 기타 | 정보·해설 | 없음 | 79/88 |
| 12 | [[playlist] 일하다 어깨 들썩이는 케이팝 노동요 ∣∣ 4K MV](https://www.youtube.com/watch?v=whggKiGBSx4) | 노래듣는 고영희 | 2,390 | 3,849,689 | 1,610.8 | ×1,612.4 | 49,244.3 | 148.4분 | 2026-08-05 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 193/196 |
| 13 | [DARKHAAST ❤️ ∣ Arijit Singh ∣ Slowed + Reverb ∣ LoFi Chill …](https://www.youtube.com/watch?v=DV1zd-C_Sms) | softtune 🎧 | 228 | 345,399 | 1,514.9 | ×523.3 | 5,214.2 | 6.9분 | 2026-08-17 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 18/19 |
| 14 | [When men loves you harder😭🌷](https://www.youtube.com/watch?v=2q4x4Ftz7mg) | wavy~ | 1,660 | 2,378,841 | 1,433.0 | ×177.7 | 62,918.7 | 9.3분 | 2026-09-14 | 기타 | 플레이리스트·모음 | 설명 | 487/507 |
| 15 | [Playlist for how a villain in love sounds like 🎧🔥✨.](https://www.youtube.com/watch?v=4NVS6d5eGyA) | Fictional Hea… | 2,920 | 4,092,694 | 1,401.6 | – | 71,902.6 | 9.7분 | 2026-08-26 | 기타 | 플레이리스트·모음 | 설명 | 324/325 |
| 16 | [ℙ𝕝𝕒𝕪𝕃𝕚𝕤𝕥 : 늙크크들 원기 회복시킬 애니 플리](https://www.youtube.com/watch?v=RbGKWnzZ0zI) | 연하네의 쓸만한 플레이리… | 826 | 1,142,441 | 1,383.1 | ×1,080.8 | 18,447.7 | 124.7분 | 2026-08-21 | 기타 | 플레이리스트·모음 | 설명 | 348/354 |
| 17 | [Cigarettes After Sex — late night playlist](https://www.youtube.com/watch?v=G5SAO7jS8xk) | ahmet | 1,130 | 1,547,866 | 1,369.8 | ×376.6 | 25,933.2 | 55.8분 | 2026-08-23 | 기타 | 플레이리스트·모음 | 설명 | 180/188 |
| 18 | [RAIM LAODE FULL ALBUM LAGU TERBAIK INDONESIA THE BEST MUSIC…](https://www.youtube.com/watch?v=plAW6z1Ex-w) | Playlist musi… | 2,260 | 3,034,153 | 1,342.5 | – | 25,362.1 | 18.2분 | 2026-06-24 | 기타 | 플레이리스트·모음 | 없음 | 306/312 |
| 19 | [JENNIE - FALLEN ANGEL (Official Video)](https://www.youtube.com/watch?v=s466YCiHfKw) | JennieRubyJan… | 24,500 | 32,524,835 | 1,327.5 | – | 589,583.4 | 5.7분 | 2026-08-28 | 10. 팝송·K팝·J팝 | 한 곡 | 설명 | 93,592/93,702 |
| 20 | [[Playlist] 코로나 전 오묘한 케이팝](https://www.youtube.com/watch?v=u7X8DqyBr64) | 원영 | 275 | 357,426 | 1,299.7 | – | 4,012.4 | 16.4분 | 2026-07-25 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 331/332 |
| 21 | [Achhi lagti ho (slowed + reverb ) lofi varsion 🎧](https://www.youtube.com/watch?v=AMg46cfQH8A) | lofi song 45 | 1,540 | 2,001,041 | 1,299.4 | ×347.9 | 29,073.6 | 5.1분 | 2026-08-14 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 182/183 |
| 22 | [Deltarune Ch. 5: Egg Room (FULL VERSION)](https://www.youtube.com/watch?v=I0S5CyJoZpw) | Clowd | 1,180 | 1,509,474 | 1,279.2 | – | 12,811.6 | 7.6분 | 2026-06-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,544/1,576 |
| 23 | [uMoya 2.0 (Tycoon Remix)](https://www.youtube.com/watch?v=HropgeYirpE) | Darque - Topic | 1,330 | 1,697,005 | 1,275.9 | ×16.7 | 40,487.9 | 8.7분 | 2026-09-10 | 기타 | 음악 | 설명 | 0/378 |
| 24 | [Kalyani [slowed & Reverb] ∣∣ With Shreya Ghoshal ∣∣Arjn / K…](https://www.youtube.com/watch?v=rbt6SjoZlWU) | TRL Lofi | 3,880 | 4,815,089 | 1,241.0 | ×1,984.0 | 48,224.2 | 4.4분 | 2026-07-14 | 기타 | 음악 | 설명 | 156/158 |
| 25 | [𝐑 𝐄 𝐙 𝐄](https://www.youtube.com/watch?v=mkRnOwNkpaQ) | iamkorean | 767 | 947,893 | 1,235.8 | – | 5,686.0 | 17분 | 2026-05-08 | 기타 | 음악 | 설명 | 211/212 |
| 26 | [Tum Ho Toh - Mashup 2026 ∣ Romantic Love Song ∣ Bollywood S…](https://www.youtube.com/watch?v=EmsrY9EQSSE) | VS Lofi Offic… | 2,230 | 2,754,032 | 1,235.0 | ×857.4 | 48,088.1 | 5.2분 | 2026-08-26 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 43/45 |
| 27 | [𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 가을 설레발 플리](https://www.youtube.com/watch?v=ams0ZufCafU) | 또잉 | 224 | 263,291 | 1,175.4 | ×727.3 | 4,807.3 | 19.6분 | 2026-08-28 | 기타 | 플레이리스트·모음 | 없음 | 17/18 |
| 28 | [별로 좋지 않은 하루를 보냈다고 생각할게](https://www.youtube.com/watch?v=wEwVgzsbqH4) | 니똥칼라똥 | 454 | 532,524 | 1,173.0 | – | 4,105.4 | 18.9분 | 2026-06-14 | 기타 | 플레이리스트·모음 | 없음 | 111/112 |
| 29 | [어른여자.mp3](https://www.youtube.com/watch?v=Ir8CBRecz7g) | 리 세이 | 510 | 595,690 | 1,168.0 | ×1,456.5 | 3,655.5 | 16분 | 2026-05-12 | 기타 | 플레이리스트·모음 | 설명 | 83/83 |
| 30 | [Hey Paaro - Full Song Bgm Raj The Show Man Puneeth Rajkumar…](https://www.youtube.com/watch?v=sj0JDjmC3es) | Mmusicworld46 | 322 | 370,282 | 1,149.9 | ×27.6 | 5,014.2 | 5.3분 | 2026-08-09 | 기타 | 음악 | 설명 | 7/7 |
| 31 | [[ 2024~2026 K-POP ] 최신곡 포함❗️ 랜덤 플레이 댄스 #랜덤플레이댄스 #kpop #2024…](https://www.youtube.com/watch?v=JnuZqf_O2N0) | 메이플 | 1,120 | 1,234,441 | 1,102.2 | – | 14,319.9 | 12.6분 | 2026-07-28 | 10. 팝송·K팝·J팝 | 한 곡 | 없음 | 86/93 |
| 32 | [3분 안에 잠드는 수면 음악 (30분) Fall Asleep in 3 Minutes (30 Min)](https://www.youtube.com/watch?v=E96njddrM5o) | 수면과학연구소 Sleep… | 89 | 108,479 | 1,084.8 | ×164.9 | 779.3 | 30분 | 2026-06-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/13 |
| 33 | [🌙 Late Night Hindi Playlist ∣ Relax • Study • Sleep ∣ Mysti…](https://www.youtube.com/watch?v=1eFr1phNoxQ) | Mystic Scenery | 1,860 | 1,980,856 | 1,065.0 | ×33.6 | 26,172.9 | 25.2분 | 2026-08-07 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 74/75 |
| 34 | [어 난데 여기 핫플이야](https://www.youtube.com/watch?v=JcIBpx-tGdA) | 햄 | 673 | 715,592 | 1,063.3 | ×1,233.8 | 4,315.7 | 24.1분 | 2026-05-09 | 기타 | 정보·해설 | 없음 | 84/84 |
| 35 | [Andekhi Anjaani si ∣ Slowed x Reverb ∣ lofi song ∣ lofi ver…](https://www.youtube.com/watch?v=FrqyfSyxOc4) | Midnight lofi… | 4,050 | 4,191,954 | 1,035.0 | ×786.3 | 84,054.9 | 6분 | 2026-09-02 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 132/133 |
| 36 | [THEN・❥・ Sweet Dreams ∣ Cinematic Techno](https://www.youtube.com/watch?v=0QAKKYJJ2l0) | THEN | 9,750 | 10,080,906 | 1,033.9 | ×2,290.6 | 74,312.7 | 4.4분 | 2026-06-08 | 기타 | 커버·직접 부른 노래 | 설명 | 491/497 |
| 37 | [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 사랑한다고 속삭여줘](https://www.youtube.com/watch?v=Tt_TimRh73Q) | 뜨신아아 | 1,060 | 1,041,376 | 982.4 | ×282.1 | 7,906.7 | 23.4분 | 2026-06-12 | 기타 | 플레이리스트·모음 | 설명 | 60/63 |
| 38 | [🎧 Le Main Saiyaan Aa Gayi (Lofi) ∣ Mohabbatein ∣ Shah Rukh …](https://www.youtube.com/watch?v=NVf0GhbUmAw) | BOYS KING 99.… | 2,470 | 2,397,354 | 970.6 | ×657.3 | 26,267.5 | 7.5분 | 2026-07-23 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 175/175 |
| 39 | [POV You're back in the 90s 💗📻 ∣ Old hindi songs ∣ Bollywood…](https://www.youtube.com/watch?v=4GMIMevMn6Y) | Manii | 2,510 | 2,335,680 | 930.5 | ×61.6 | 39,878.2 | 8.2분 | 2026-08-24 | 기타 | 음악 | 설명 | 803/835 |
| 40 | [Toota Rahunga](https://www.youtube.com/watch?v=qN9Vw9v2nLY) | Garvit Soni -… | 1,440 | 1,330,706 | 924.1 | – | 14,330.8 | 4.1분 | 2026-07-21 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/48 |
| 41 | [Baddies playlist🫦💋](https://www.youtube.com/watch?v=iwtL-agF0LQ) | Music-cholic | 1,230 | 1,063,699 | 864.8 | – | 7,165.1 | 18.9분 | 2026-05-26 | 기타 | 플레이리스트·모음 | 설명 | 56/56 |
| 42 | [Top Hits Indonesia 2026 ∣ Top Hits Spotify Indonesia 2026 ∣…](https://www.youtube.com/watch?v=ANPUoFuWpEo) | ShadowBrief | 9,720 | 8,267,756 | 850.6 | – | 50,901.3 | 65분 | 2026-05-12 | 기타 | 정보·해설 | 설명 | 998/1,000 |
| 43 | [MOOD : FIRST LOVE { Desi playlist }](https://www.youtube.com/watch?v=zVH3YHdvXHY) | xukiyo | 3,230 | 2,714,024 | 840.3 | ×86.1 | 16,553.4 | 11.8분 | 2026-05-11 | 기타 | 플레이리스트·모음 | 없음 | 71/71 |
| 44 | [DANGRANGTO Playlist Hay Nhất ∣ Xương Rồng, Vùng Vẫy, Wrong …](https://www.youtube.com/watch?v=okmN02_PnaM) | hiệu ứng đám … | 1,660 | 1,384,911 | 834.3 | ×6.2 | 14,269.0 | 24.9분 | 2026-07-17 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 58/58 |
| 45 | [🎧 Le Main Saiyaan Aa Gayi (Lofi) ∣ Mohabbatein ∣ Shah Rukh …](https://www.youtube.com/watch?v=iOdAwvF0kmk) | lofi.slowed_02 | 5,670 | 4,633,361 | 817.2 | ×904.1 | 48,722.2 | 7.5분 | 2026-07-19 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 291/296 |
| 46 | [Tera Sang Yaara - Slowed Reverb ∣∣ Atif Aslam ∣∣ Dopohor Lo…](https://www.youtube.com/watch?v=QcR63bT06iE) | Dopohor Lofi | 3,430 | 2,799,134 | 816.1 | ×236.0 | 67,080.0 | 5분 | 2026-09-10 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 219/227 |
| 47 | [Tu Chahiye [lyrics] Atif Aslam](https://www.youtube.com/watch?v=AJ0KTHkTGYA) | Chill Beats H… | 1,890 | 1,526,113 | 807.5 | ×396.0 | 23,916.7 | 4.5분 | 2026-08-19 | 기타 | 한 곡 | 설명 | 74/74 |
| 48 | [Hanuman Chalisa ∣ Peaceful & Divine ∣ Powerful Bhajan for P…](https://www.youtube.com/watch?v=pmQtkBTtzLw) | Shri Music St… | 1,410 | 1,128,647 | 800.5 | ×1,513.9 | 6,635.4 | 6.4분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 601/615 |
| 49 | [Những Bản Nhạc LoFi Chill Hay Nhất 2026 ∣ TikTok Viral Triệ…](https://www.youtube.com/watch?v=4vl5hS0oXH0) | Kvyzz Music | 1,260 | 1,000,057 | 793.7 | – | 11,312.1 | 26.1분 | 2026-07-25 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 185/189 |
| 50 | [Barsaat 🌧️ ∣ All Trending Songs 🎧∣ Taare x Samjho Na x Safa…](https://www.youtube.com/watch?v=xGPm2j1dDr4) | LOFI XP VIBES | 2,490 | 1,839,161 | 738.6 | ×240.5 | 45,152.6 | 23분 | 2026-09-11 | 기타 | 음악 | 설명 | 193/199 |
| 51 | [[Playlist Tâm Trạng]#1 - Xương Rồng, Vết Thương, Tìm Em, Ng…](https://www.youtube.com/watch?v=DcZ75tBPfa4) | Cà Chuaa | 2,410 | 1,758,535 | 729.7 | ×74.3 | 20,057.6 | 15.5분 | 2026-07-26 | 기타 | 플레이리스트·모음 | 설명 | 344/351 |
| 52 | [POV: You Own The Dance Floor💃🏻🪩✨ ∣∣Song Playlist+ Timestamp…](https://www.youtube.com/watch?v=HRGB0HnXdOs) | Author_Shreyuu | 6,200 | 4,446,380 | 717.2 | – | 29,614.0 | 8분 | 2026-05-25 | 기타 | 플레이리스트·모음 | 설명 | 617/619 |
| 53 | [MKAstro – Darkness Chill ∣ Club Banger Trap ∣ (Visualizer)](https://www.youtube.com/watch?v=emsqrCS0yiw) | MKAstro Studio | 3,570 | 2,548,242 | 713.8 | ×3,179.3 | 22,551.0 | 5.8분 | 2026-07-01 | 8. 로파이·시티팝·칠 | AI 음악 | 설명 | 154/165 |
| 54 | [Hanuman Chalisa Sleep Version 🕉️ ∣ Sleep In 5 Minutes 😴 ∣ S…](https://www.youtube.com/watch?v=RgmRMA0Bs34) | Ananta Rhythm | 4,510 | 3,168,070 | 702.5 | ×5,927.2 | 19,398.9 | 7.1분 | 2026-05-12 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,523/1,527 |
| 55 | [7 मिनट में बच्चा गहरी नींद सोए🌙 सो जा मेरे चाँद से लाल ∣ Hi…](https://www.youtube.com/watch?v=IxnmH8QjS_A) | deep sleep vi… | 898 | 624,462 | 695.4 | ×10,766.6 | 3,887.5 | 6.8분 | 2026-05-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 152/153 |
| 56 | [Yeh Raatein Yeh Mausam - Soft Acoustic Cover ∣ Beautiful Ni…](https://www.youtube.com/watch?v=IrLRtCGI2Oc) | Divine Soul R… | 8,280 | 5,712,633 | 689.9 | ×356.7 | 35,218.1 | 5.1분 | 2026-05-13 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 277/277 |
| 57 | [Steve Lacy - the feeling (Official Video)](https://www.youtube.com/watch?v=Qw20tg1v7Fc) | SteveLacyVEVO | 8,430 | 5,786,837 | 686.5 | – | 41,582.3 | 4.6분 | 2026-06-05 | 기타 | 플레이리스트·모음 | 설명 | 5,393/5,417 |
| 58 | [Pov: certified Baddie playlist 🔥# playlist # baddie](https://www.youtube.com/watch?v=vzNOiBV_W6g) | it's GAURAV P… | 7,850 | 5,381,277 | 685.5 | – | 42,313.0 | 8.3분 | 2026-06-17 | 기타 | 플레이리스트·모음 | 설명 | 696/701 |
| 59 | [Tere Liye [Slowed+Reverb+Lofi] Song ∣ Atif Aslam, Shreya Gh…](https://www.youtube.com/watch?v=zwDQAObOpx4) | DK LOFI | 3,590 | 2,445,278 | 681.1 | ×396.5 | 25,140.7 | 4.5분 | 2026-07-17 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 415/428 |
| 60 | [Mind Relax Lofi Mashup ∣ Mind Relaxing Songs ∣ Mind Relax L…](https://www.youtube.com/watch?v=JyM_L7ZZ9xw) | SONGS ZONE | 3,000 | 2,033,785 | 677.9 | – | 14,167.9 | 28.7분 | 2026-05-31 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 357/365 |
| 61 | ['pov: bạn mở lại một tab ký ức năm 2018 ♪♪](https://www.youtube.com/watch?v=8ljpWVIINTs) | chalye | 2,330 | 1,574,874 | 675.9 | ×133.9 | 11,795.6 | 27.4분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 설명 | 331/334 |
| 62 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=XLtdtHJExEY) | Clsxzff | 1,860 | 1,246,823 | 670.3 | – | 40,414.3 | 19.6분 | 2026-09-21 | 1. 수면·명상·힐링 | 음악 | 설명 | 173/187 |
| 63 | [POV: you discovered that ✨South Indian and Hindi ✨songs hit…](https://www.youtube.com/watch?v=lbT4VY3UKkY) | Arena | 3,490 | 2,300,755 | 659.2 | ×457.5 | 33,902.6 | 14.6분 | 2026-08-15 | 12. 커버·노래 부르기 | 음악 | 설명 | 406/426 |
| 64 | [Achchi Lagti Ho (Slowed + Reverb) ∣ Lofi Version 🎧](https://www.youtube.com/watch?v=fc8Mab9zGkg) | GTAvexo9 | 24,100 | 15,553,534 | 645.4 | – | 162,511.3 | 6.5분 | 2026-07-18 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 2,047/2,141 |
| 65 | [Darmiyaan](https://www.youtube.com/watch?v=v2TsWj3wxHM) | Rekha Bhardwa… | 8,590 | 5,537,265 | 644.6 | – | 58,889.7 | 4.5분 | 2026-07-20 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/238 |
| 66 | [이게 삶이더라고｜세월 끝에 깨닫는 인생 이야기｜감성 발라드](https://www.youtube.com/watch?v=QalAq2cvw8U) | 웃음콘서트TV | 2,660 | 1,703,113 | 640.3 | ×501.0 | 11,180.2 | 5.4분 | 2026-05-23 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 334/348 |
| 67 | [Hangova (From "DC")](https://www.youtube.com/watch?v=B6ppp6WBCKg) | Anirudh Ravic… | 31,700 | 20,083,381 | 633.5 | ×1,542.9 | 186,205.7 | 4.1분 | 2026-07-06 | 기타 | 정보·해설 | 설명 | 0/1,466 |
| 68 | [POV: You are ✨ Self Obsessed women💅 Playlist hindi bollywood](https://www.youtube.com/watch?v=wOy_aMJqDgo) | 𝐌𝐫. | 2,670 | 1,687,027 | 631.9 | ×1,391.9 | 15,342.2 | 14.4분 | 2026-07-04 | 기타 | 플레이리스트·모음 | 설명 | 841/843 |
| 69 | [Om Namah Shivaya 🕉 #hanumanansh #backgroundmusic #trendings…](https://www.youtube.com/watch?v=YnhFtBGO2zI) | Rudree Aarya … | 2,470 | 1,543,222 | 624.8 | – | 33,882.2 | 15.5분 | 2026-09-06 | 기타 | 음악 | 없음 | 385/385 |
| 70 | [Mann mera (Original Version) ∣ Slowed + Reverb ∣ Gajendra V…](https://www.youtube.com/watch?v=4ObYNh1TOHY) | LOFI ZONE 990K | 16,900 | 10,547,075 | 624.1 | ×1,464.1 | 120,983.8 | 5분 | 2026-07-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,591/1,648 |
| 71 | [Twinkle Twinkle - Best Lullabies for Babies To Sleep ∣ Litt…](https://www.youtube.com/watch?v=PE3jMxJjyB0) | KiddoBeatz | 850 | 529,803 | 623.3 | ×642.2 | 3,110.4 | 10.7분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 72 | [Heartbreak Chillout ∣ Vishal Mishra ∣ Arijit singh ∣ Soulfu…](https://www.youtube.com/watch?v=XlYh9K0UNXI) | Nilay Kumar M… | 2,400 | 1,492,190 | 621.8 | ×18,888.5 | 8,788.1 | 8분 | 2026-05-05 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 137/138 |
| 73 | [[𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 띵곡들만 모아놓은 애니 노동요 OST 플리💿](https://www.youtube.com/watch?v=16zIXIea0_U) | ASMRuru_루루 | 890 | 551,509 | 619.7 | ×878.2 | 4,082.2 | 54.4분 | 2026-06-09 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 91/93 |
| 74 | [Premada Oorali Kannada LO-FI Song By Nitro plus kannada](https://www.youtube.com/watch?v=LEqTIHGB7_g) | NITRO PLUS KA… | 4,530 | 2,783,486 | 614.5 | ×20,928.5 | 26,441.4 | 11.5분 | 2026-07-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 240/250 |
| 75 | [Playlist Song Inggris Gamon Santai...∣∣ The Winner Takes It…](https://www.youtube.com/watch?v=E9Nm4xOU-tk) | musik gen z | 1,990 | 1,210,851 | 608.5 | ×101.5 | 13,909.9 | 31.1분 | 2026-07-27 | 기타 | 플레이리스트·모음 | 설명 | 467/478 |
| 76 | [𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 느좋 인스타 감성](https://www.youtube.com/watch?v=RG-8iv6ORFY) | 알수없는 사용자 | 1,730 | 1,048,304 | 606.0 | ×29.0 | 14,739.3 | 27분 | 2026-08-12 | 기타 | 플레이리스트·모음 | 설명 | 94/100 |
| 77 | [Barsaat 🌧️∣ All Trending Songs ∣ Taare x Samjho Na x Safar …](https://www.youtube.com/watch?v=41HX_5G6eqQ) | Voxwaves | 13,600 | 8,113,845 | 596.6 | ×404.7 | 179,232.9 | 22.9분 | 2026-09-07 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,062/1,124 |
| 78 | [Peace of Mind : Sufi Bollywood Nonstop ∣ Rahat Fateh Ali Kh…](https://www.youtube.com/watch?v=RlyVCMHCuqc) | Aures Music S… | 3,720 | 2,208,105 | 593.6 | ×4,295.9 | 27,317.1 | 57.1분 | 2026-08-02 | 기타 | 음악 | 설명 | 124/124 |
| 79 | [○ Bollywood navratri song playlist ○ #navratri #garbasongs …](https://www.youtube.com/watch?v=g9nj1SDsXng) | july_luna | 4,540 | 2,666,733 | 587.4 | ×101.7 | 84,401.9 | 18.9분 | 2026-09-20 | 기타 | 플레이리스트·모음 | 없음 | 102/127 |
| 80 | [DUDE 30 Min Loop 🎧 ∣ Orchestral Suite • Metro Proposal • Pl…](https://www.youtube.com/watch?v=rNkUDAFaFbM) | Zontyx | 1,860 | 1,092,219 | 587.2 | ×6,188.2 | 7,340.1 | 29.7분 | 2026-05-26 | 기타 | 긴 한 곡·반복 | 설명 | 974/983 |
| 81 | [Old Punjabi Bangers ∣ Punjabi Hits Playlist ∣ Still Cookin](https://www.youtube.com/watch?v=rJgcNE-7emM) | STILL COOKIN | 3,420 | 1,963,916 | 574.2 | – | 18,630.7 | 14.1분 | 2026-07-08 | 기타 | 플레이리스트·모음 | 설명 | 107/109 |
| 82 | [You’ll Sleep Like a Child in Hanuman’s Protection ∣ Soft Ha…](https://www.youtube.com/watch?v=oSeh-sXFCTM) | Sanatan Jug | 5,540 | 3,158,097 | 570.0 | ×7,797.8 | 18,705.5 | 111.6분 | 2026-05-06 | 1. 수면·명상·힐링 | 한 곡 | 설명 | 399/413 |
| 83 | [Phonk/funk playlist bcz I’m bored (Timestaps)](https://www.youtube.com/watch?v=8AXBNw3EGu8) | 1vy_x | 5,110 | 2,893,014 | 566.1 | ×10.3 | 18,963.6 | 9.8분 | 2026-05-22 | 기타 | 플레이리스트·모음 | 설명 | 304/306 |
| 84 | [Autumn Fireplace Jazz ∣ Cozy Crackling Fire Ambience](https://www.youtube.com/watch?v=q87NJ-696WM) | Midnight Fika | 4,060 | 2,276,545 | 560.7 | ×3,454.5 | 58,748.2 | 129.6분 | 2026-09-13 | 2. 자연 소리·백색소음 | 음악 | 설명 | 207/212 |
| 85 | [DESI PUNJABI PLAYLIST THAT GETS YOUR VIBE 😌🎧](https://www.youtube.com/watch?v=JQ922u24pH8) | Your April | 3,210 | 1,798,932 | 560.4 | ×113.8 | 12,130.8 | 11.4분 | 2026-05-27 | 기타 | 플레이리스트·모음 | 설명 | 393/396 |
| 86 | [🍂 가을이 오면 생각나는 노래 ∣ 커피 한 잔과 함께 듣는 가을 감성 플레이리스트 ☕](https://www.youtube.com/watch?v=Fc7JJxJBgJA) | enuscento-에뉴센토 | 710 | 397,788 | 560.3 | ×1,258.8 | 8,129.6 | 114.3분 | 2026-09-03 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 62/69 |
| 87 | [Overthinking? Listen To This Krishna Flute Music & Stop Wor…](https://www.youtube.com/watch?v=Pckh0r0bGAM) | Dhwani | 1,420 | 783,741 | 551.9 | – | 5,857.0 | 8분 | 2026-06-10 | 기타 | 음악 | 설명 | 134/134 |
| 88 | [𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩 slavic](https://www.youtube.com/watch?v=49A1aj-uIcs) | aa | 1,540 | 842,879 | 547.3 | ×316.5 | 8,289.7 | 16.8분 | 2026-07-12 | 기타 | 플레이리스트·모음 | 설명 | 191/199 |
| 89 | [Sanson Ki Mala Pe (Slowed & Emotional Version) ∣ Hindi Love…](https://www.youtube.com/watch?v=7y_L2sW-3J4) | Karela Records | 4,360 | 2,384,482 | 546.9 | ×2,045.9 | 17,245.1 | 7.3분 | 2026-06-06 | 기타 | 음악 | 설명 | 92/92 |
| 90 | [Relaxing Jazz Café in Paris ∣ Rainy Evening Jazz Ambience w…](https://www.youtube.com/watch?v=eR37WB9IE9E) | European Jazz… | 1,240 | 675,437 | 544.7 | ×1,160.5 | 4,959.2 | 14.4분 | 2026-06-08 | 2. 자연 소리·백색소음 | 음악 | 설명 | 24/26 |
| 91 | [Baddie playlist 💋✨Aura+99999∣ SanviEditz #songplaylist](https://www.youtube.com/watch?v=p8u1URNm4ao) | ♡𝑺𝒂𝒏𝒗𝒊𝑬𝒅𝒊𝒕𝒛♡ | 4,820 | 2,583,301 | 536.0 | – | 56,192.5 | 8.1분 | 2026-09-06 | 기타 | 플레이리스트·모음 | 없음 | 2,195/2,277 |
| 92 | [✨️𝐬𝐨𝐧𝐠𝐬 𝐭𝐡𝐚𝐭 𝐦𝐚𝐤𝐞 𝐥𝐢𝐟𝐞 𝐟𝐞𝐞𝐥 𝐥𝐢𝐤𝐞 𝐚 𝐥𝐨𝐯𝐞 𝐬𝐭𝐨𝐫𝐲 ∣ aesthetic h…](https://www.youtube.com/watch?v=GMF0FN2nrBw) | Echoess of un… | 6,140 | 3,273,950 | 533.2 | ×19.0 | 23,095.2 | 18.6분 | 2026-06-02 | 기타 | 플레이리스트·모음 | 설명 | 409/409 |
| 93 | [धनियां बनबू कनियाँ - Lofi Song ∣∣ Khesari Lal Yadav ∣∣ Dilw…](https://www.youtube.com/watch?v=s-1MerBYomA) | ꧁༒乙x°᭄Ᏼᴀʙᴜ࿐ | 3,840 | 2,029,933 | 528.6 | ×353.8 | 35,419.5 | 5.1분 | 2026-08-26 | 8. 로파이·시티팝·칠 | 음악 | 없음 | 267/296 |
| 94 | [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 그리고 난 다시 사랑에 빠질수 밖에 없었어](https://www.youtube.com/watch?v=cIlJK2Pfhm8) | 느좋을 추구합니다 | 1,030 | 543,141 | 527.3 | – | 8,913.0 | 18.1분 | 2026-08-22 | 기타 | 플레이리스트·모음 | 없음 | 177/177 |
| 95 | [Me Sunti Rahu 💭🎶 ∣ Heart Touching Lofi Song (Slowed + Rever…](https://www.youtube.com/watch?v=TKMu6Wg396c) | 𝕃𝕠𝕤𝕥_𝕗𝕖𝕖𝕝𝕚𝕟𝕘𝕤… | 4,620 | 2,431,234 | 526.2 | ×654.5 | 17,144.2 | 5.7분 | 2026-06-02 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 389/392 |
| 96 | [Ankhiyon Ke Jharokhon Se ∣ Soft Classic Instrumental 🎶 ∣ Ol…](https://www.youtube.com/watch?v=KCgBk52MuY8) | Saaz-e-Dil | 1,930 | 1,010,216 | 523.4 | ×366.7 | 7,785.4 | 4.5분 | 2026-06-14 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 127/128 |
| 97 | [If you want to dance...🩰✨watch this playlist💃❣️ #bollywood …](https://www.youtube.com/watch?v=x0br2Hc-4G8) | LyricVibes~ | 6,060 | 3,155,353 | 520.7 | – | 21,188.2 | 24.4분 | 2026-05-26 | 기타 | 플레이리스트·모음 | 설명 | 380/380 |
| 98 | [💋 A Chatpati Playlist Only For Chatpata People 😋✨ ∣ Ultimat…](https://www.youtube.com/watch?v=3FhXwFGVaDE) | JellyBloxify | 33,100 | 17,206,844 | 519.8 | ×9,683.1 | 124,593.0 | 7.5분 | 2026-06-06 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 2,208/2,219 |
| 99 | [Ishq x Pal Pal Endless Mashup (Slowed + Reverb) - Afusic x …](https://www.youtube.com/watch?v=h231qlqI-dg) | Lost In Lyrics | 1,090 | 562,361 | 515.9 | ×146.3 | 5,416.0 | 27.6분 | 2026-07-10 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 109/109 |
| 100 | [Parindey (Slowed + Reverb) ∣ Haryanvi Lofi Song 🎧 Chill Vib…](https://www.youtube.com/watch?v=v8CKkI20B2s) | AS LO-FI Musi… | 3,740 | 1,909,594 | 510.6 | ×741.9 | 10,833.3 | 4.1분 | 2026-04-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 150/150 |
| 101 | [Arijit Singh - Tujhko (from Cocktail 2) Rashmika Mandanna, …](https://www.youtube.com/watch?v=WWIfHemqSEA) | iPop Superhits | 47,300 | 24,066,819 | 508.8 | – | 171,780.7 | 5.6분 | 2026-06-04 | 기타 | 한 곡 | 설명 | 1,133/1,136 |
| 102 | [Devik - Muje tumse x tu tu hai wahi DJ remix (BGM) music 🎶 …](https://www.youtube.com/watch?v=FPuJuLyZmJI) | Newworldbeats… | 729 | 364,754 | 500.4 | – | 7,129.0 | 9.7분 | 2026-09-01 | 기타 | 음악 | 설명 | 137/137 |
| 103 | [I'm Tired Of Loving You - Golden Lace Ballads ∣ Classic Cou…](https://www.youtube.com/watch?v=URrqbWhzzMU) | Golden Lace B… | 3,140 | 1,568,504 | 499.5 | ×1,503.1 | 10,395.5 | 5.8분 | 2026-05-24 | 기타 | 한 곡 | 설명 | 361/366 |
| 104 | [THE WEEKND ∣ Late Night Drive Playlist](https://www.youtube.com/watch?v=DgBM12cGM-Q) | Jostynsc | 10,300 | 5,136,117 | 498.6 | ×19.8 | 41,993.5 | 40.8분 | 2026-06-22 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 304/306 |
| 105 | [✨Best Bollywood LoFi Mashup 2026 🌙✨ lofi song](https://www.youtube.com/watch?v=ohHqAaHYlLI) | Soul Beats | 4,790 | 2,302,644 | 480.7 | ×1,053.8 | 22,864.5 | 25.8분 | 2026-07-13 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 122/122 |
| 106 | [[𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 저 정말 바라는 거 없어요](https://www.youtube.com/watch?v=ZUW47tZkwkg) | 음악저장소 | 1,820 | 867,425 | 476.6 | ×55.5 | 27,285.5 | 27.3분 | 2026-09-20 | 기타 | 플레이리스트·모음 | 없음 | 88/88 |
| 107 | [[ 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ] 적당히 신나는 그루브 힙합 플레이리스트 ∣ Chill R&B • Cafe Music](https://www.youtube.com/watch?v=p3tvSF3BgYM) | SSoundW | 4,020 | 1,914,311 | 476.2 | ×487.5 | 30,975.6 | 89.9분 | 2026-08-21 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 253/253 |
| 108 | [GTA 6 Raul Batista Mission Theme Music - Clean Audio - Exte…](https://www.youtube.com/watch?v=Lu2v0EWc0-0) | GAMING Benchm… | 1,350 | 642,107 | 475.6 | ×4,901.6 | 11,723.7 | 5.3분 | 2026-08-28 | 기타 | 음악 | 설명 | 864/871 |
| 109 | [Mind relaxing lofi song Arijit Singh ∣ Soft songs ∣ Arijit …](https://www.youtube.com/watch?v=43y5rT7YjQY) | Y Music 2 | 36,300 | 17,149,587 | 472.4 | ×125,179.5 | 119,857.6 | 27.9분 | 2026-06-01 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,372/1,384 |
| 110 | [Idea 22 - Depressed in 448Hz (Cello cry & Piano & slow) @Gi…](https://www.youtube.com/watch?v=zMMuayoF_o4) | WORRIES | 403 | 187,189 | 464.5 | ×125.8 | 2,192.8 | 12.9분 | 2026-07-28 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 116/116 |
| 111 | [🎶Spotify Hits Music 2026 ∣∣ Top Music Playlist -- Best 100 …](https://www.youtube.com/watch?v=0gvy7v6GTMo) | Soft Feelings | 5,900 | 2,739,041 | 464.2 | ×181.5 | 39,191.8 | 138.6분 | 2026-08-13 | 기타 | 플레이리스트·모음 | 설명 | 188/191 |
| 112 | [🎀Students fav playlist👀 ∣next comment∣](https://www.youtube.com/watch?v=yx9rhLzbY0A) | @vibe_withe_me | 5,400 | 2,506,093 | 464.1 | ×392.8 | 33,918.6 | 7분 | 2026-08-09 | 기타 | 플레이리스트·모음 | 없음 | 1,169/1,198 |
| 113 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 nên nghe gì khi gió Thu tràn về? 🍂📻 Playlist Nhạc …](https://www.youtube.com/watch?v=Pg39V_-aNPY) | chill out | 4,530 | 2,059,837 | 454.7 | ×45.7 | 64,513.7 | 83.5분 | 2026-09-20 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 236/243 |
| 114 | [One playlist. A thousand imaginary love stories. ❤️](https://www.youtube.com/watch?v=aIYTT2ihwvM) | soul wali vib… | 2,410 | 1,088,459 | 451.6 | ×99.0 | 18,568.2 | 22.1분 | 2026-08-24 | 기타 | 플레이리스트·모음 | 없음 | 354/355 |
| 115 | [𓍢ִ໋🌾 chatpate punjabi bangers](https://www.youtube.com/watch?v=neQ8CUHH7WQ) | b࣪ ִֶָ☾. | 6,870 | 3,069,703 | 446.8 | – | 22,240.2 | 12.2분 | 2026-06-06 | 기타 | 플레이리스트·모음 | 설명 | 277/281 |
| 116 | [Michael Jackson Greatest Hits Mix ∣ Celebrating MICHAEL (20…](https://www.youtube.com/watch?v=F2-83E_iNb4) | IONEMusic | 10,700 | 4,762,804 | 445.1 | ×4,143.4 | 45,973.4 | 94.5분 | 2026-07-10 | 기타 | 음악 | 설명 | 1,177/1,185 |
| 117 | [कर्पूरगौरं करुणावतारं ∣ Shiva Lingam Divine Prayer ∣ Karpur…](https://www.youtube.com/watch?v=5I7pQfjbUHo) | Darshan Dhara | 4,020 | 1,785,989 | 444.3 | ×1,374.9 | 10,854.6 | 8.4분 | 2026-05-10 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 139/139 |
| 118 | [모르는 노래 없는!! 2026 랜덤플레이댄스🍋 ∣ 랜플댄 ∣ 랜플💫 ∣ 모르는 노래 없는 랜플댄🩷 ∣ 케이…](https://www.youtube.com/watch?v=tAJM1fttdG0) | 바나나한 바냐 | 577 | 255,371 | 442.6 | – | 3,631.2 | 5.1분 | 2026-08-13 | 10. 팝송·K팝·J팝 | 음악 | 없음 | 36/36 |
| 119 | [Pov :- Bhojpuri playlist 🔥 ∣∣ chill guys and enjoy 😎∣∣ Ansh…](https://www.youtube.com/watch?v=4mnrtxd_GhE) | Anshika | 19,600 | 8,591,962 | 438.4 | ×61.3 | 109,154.1 | 11.6분 | 2026-08-04 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,684/1,706 |
| 120 | [Top Bhojpuri Hits Mix 2026 ∣ Nonstop Bhojpuri Mashup 🎧🔥](https://www.youtube.com/watch?v=7v8NIUwR1No) | Anivix | 6,070 | 2,654,598 | 437.3 | ×1,099.4 | 23,992.8 | 6분 | 2026-07-03 | 기타 | 음악 | 설명 | 483/486 |
| 121 | [🌊 여름에 듣기 좋은 노래☀️ 하루 종일 듣기 좋은 여름 플레이리스트 🌴 바다로 떠나고 싶어지는 여름 노래…](https://www.youtube.com/watch?v=L-pbTsp8AH8) | 마음선곡 | 844 | 368,453 | 436.6 | ×404.4 | 2,558.7 | 119분 | 2026-05-31 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 67/67 |
| 122 | ["𝐖𝐞 𝐚𝐫𝐞 𝐣𝐮𝐬𝐭 𝐟𝐫𝐢𝐞𝐧𝐝𝐬... 𝐑𝐢𝐠𝐡𝐭.?"/ 𝐀 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐟𝐨𝐫 𝐬𝐨𝐦𝐞𝐨𝐧𝐞 𝐲𝐨…](https://www.youtube.com/watch?v=A_yQZns_YGk) | 𝗩𝗮𝗺𝗽𝗶𝗿𝗲 𓂃⋆.˚ | 2,410 | 1,047,618 | 434.7 | ×41.8 | 9,990.5 | 20.4분 | 2026-07-09 | 기타 | 플레이리스트·모음 | 설명 | 610/611 |
| 123 | [katseye (clean) playlist ⊹ ࣪ ˖](https://www.youtube.com/watch?v=_VEtnBXtUNs) | 𝟑𝟎𝟑.𝐧𝐞𝐰.𝐞𝐫𝐚 | 7,780 | 3,366,462 | 432.7 | – | 40,953.0 | 25.3분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 설명 | 2,599/2,602 |
| 124 | [𝑮𝒐𝒍𝒅𝒆𝒏 𝑩𝒓𝒐𝒘𝒏 - 𝑻𝒉𝒆 𝑺𝒕𝒓𝒂𝒏𝒈𝒍𝒆𝒓𝒔 ∣ ⚔︎ 𝑩𝒆𝒔𝒕 𝒑𝒂𝒓𝒕 𝒍𝒐𝒐𝒑𝒆𝒅 ⚔︎](https://www.youtube.com/watch?v=9MLxTIPaoTQ) | Medieval Anem… | 2,410 | 1,042,206 | 432.4 | ×2,308.3 | 13,811.8 | 11.8분 | 2026-08-07 | 기타 | 정보·해설 | 설명 | 417/423 |
| 125 | [One Playlist. Endless Feelings. ∣ Soft Love Songs for Late …](https://www.youtube.com/watch?v=Auvd4NPXHnI) | Unrequited Lo… | 5,760 | 2,480,912 | 430.7 | – | 23,218.6 | 23.2분 | 2026-07-07 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 436/437 |
| 126 | [Stay With Me Now..](https://www.youtube.com/watch?v=mT2U96LfO3g) | AERIN - Proje… | 571 | 244,799 | 428.7 | ×1,419.1 | 1,523.5 | 4.6분 | 2026-05-14 | 기타 | 음악 | 설명 | 31/31 |
| 127 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Chi…](https://www.youtube.com/watch?v=ki362-gbdjs) | Qais Music St… | 2,170 | 912,273 | 420.4 | ×3,258.1 | 41,675.7 | 7.3분 | 2026-09-30 | 3. 공부·집중·작업 | 음악 | 설명 | 10/10 |
| 128 | [Dance playlist for chatpati girls 🥂💅🏻🍷#dance #viral#trendin…](https://www.youtube.com/watch?v=wh1wOQrBIrk) | soft girl 🦋💫 | 4,010 | 1,681,357 | 419.3 | ×83.2 | 12,581.1 | 8.5분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 없음 | 110/110 |
| 129 | [Playlist cuz you're in love 💌#playlist #love #2026](https://www.youtube.com/watch?v=gbf3ZYx6EbU) | it's GAURAV P… | 7,850 | 3,286,856 | 418.7 | – | 19,928.8 | 10.6분 | 2026-05-10 | 기타 | 플레이리스트·모음 | 설명 | 531/530 |
| 130 | [ALL TRENDING HINDI SONGS 2026...PLAYLIST #asthetic #trend #…](https://www.youtube.com/watch?v=xI0IEWIxUBQ) | Rb Lofi | 23,700 | 9,921,293 | 418.6 | ×1,098.2 | 165,397.1 | 7.9분 | 2026-08-23 | 기타 | 플레이리스트·모음 | 없음 | 1,565/1,634 |
| 131 | [[Playlist] Music is my drug](https://www.youtube.com/watch?v=msoR3EhPNAA) | Hugs | 6,470 | 2,667,761 | 412.3 | – | 54,828.8 | 20.9분 | 2026-09-03 | 기타 | 플레이리스트·모음 | 설명 | 538/540 |
| 132 | [Throwback R&B Classics 📺 Chris Brown, Rihanna, Akon, Usher,…](https://www.youtube.com/watch?v=gCUbxsTWZ18) | R&B Afterglow | 14,400 | 5,874,965 | 408.0 | ×4,498.4 | 60,619.4 | 193.5분 | 2026-07-17 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 698/732 |
| 133 | [𝙅 𝙋𝙤𝙥 𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩 저기, 나 지금 사랑에 빠지고 있어](https://www.youtube.com/watch?v=-_t34PClPSE) | 이로하 | 1,850 | 749,853 | 405.3 | – | 4,815.9 | 20.9분 | 2026-05-19 | 기타 | 플레이리스트·모음 | 설명 | 165/168 |
| 134 | ["some aesthetic desi song's you'll absolutely love"🌊✨😭//par…](https://www.youtube.com/watch?v=6D1sq3Y-hB0) | Anushri | 7,070 | 2,863,028 | 404.9 | ×15.5 | 26,156.6 | 12.5분 | 2026-07-04 | 기타 | 음악 | 설명 | 503/506 |
| 135 | [CHILL NIGHT MOOD🌙 R&B Mix Playlist ∣ Late Night Vibes, Rela…](https://www.youtube.com/watch?v=zA04SiNiLYk) | Late Night Rn… | 2,610 | 1,055,031 | 404.2 | – | 6,370.1 | 158.2분 | 2026-05-09 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 54/54 |
| 136 | [katseye playlist✨💋](https://www.youtube.com/watch?v=H40nuw4mebU) | maiia | 20,400 | 8,187,721 | 401.4 | – | 156,511.7 | 21.3분 | 2026-08-31 | 기타 | 플레이리스트·모음 | 없음 | 4,330/4,509 |
| 137 | [/KATSEYE PLAYLIST💫/ All Songs In One Video / ICONIC BY MIST…](https://www.youtube.com/watch?v=wQHy50dFnfY) | 𝓔𝓵𝓵𝓲𝔁𝔁𝓺 🤍🎀 | 2,610 | 1,046,744 | 401.1 | – | 9,048.4 | 43분 | 2026-06-28 | 기타 | 플레이리스트·모음 | 설명 | 950/946 |
| 138 | [Haryanvi playlist that walk up your inner dancer 🔥💋#lifewit…](https://www.youtube.com/watch?v=tYuLhTnHgOQ) | Venus Yadav | 11,800 | 4,725,514 | 400.5 | – | 57,899.8 | 11분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 없음 | 570/592 |
| 139 | [Heartbreaking 💔 Lofi Mashup 🎧Slowed + Reverb Songs ∣ Relax,…](https://www.youtube.com/watch?v=gCuJrBYRJpM) | Fiaz Baloch O… | 6,880 | 2,745,994 | 399.1 | ×4,674.0 | 59,396.6 | 8분 | 2026-09-06 | 3. 공부·집중·작업 | 음악 | 설명 | 154/154 |
| 140 | [[Playlist] When music is all you need](https://www.youtube.com/watch?v=XXKXpf7xFC4) | encore. | 7,210 | 2,875,464 | 398.8 | ×238.5 | 89,919.8 | 20.9분 | 2026-09-20 | 기타 | 플레이리스트·모음 | 설명 | 518/627 |
| 141 | [Attract Peace & Positive Energy ∣ Raag Malhar Morning Medit…](https://www.youtube.com/watch?v=c45OwnC599Y) | Tatva Meditat… | 208 | 82,829 | 398.2 | ×696.0 | 582.0 | 15분 | 2026-06-02 | 1. 수면·명상·힐링 | 음악 | 설명 | 9/9 |
| 142 | [Viral Songs Playlist 2026 ∣ Barsaat, Sheesha, Parvati, Roots](https://www.youtube.com/watch?v=nmc4ScFV3j4) | Vijay Garje | 3,540 | 1,403,754 | 396.5 | ×12,422.6 | 78,811.6 | 31.3분 | 2026-10-04 | 기타 | 플레이리스트·모음 | 설명 | 320/411 |
| 143 | [Emraan hashmi playlist #emraanhashmi](https://www.youtube.com/watch?v=zZzA1Hp30uE) | july_luna | 4,540 | 1,783,677 | 392.9 | ×68.0 | 28,928.1 | 7.2분 | 2026-08-21 | 기타 | 플레이리스트·모음 | 없음 | 22/25 |
| 144 | [Barsaat ∣ All Trending Hindi Songs 2026 ∣ Safar × Bairan × …](https://www.youtube.com/watch?v=-hXkiB-eLfs) | SukumusicHindi | 3,390 | 1,329,356 | 392.1 | ×716.6 | 31,832.0 | 22.9분 | 2026-09-10 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 161/165 |
| 145 | [[playlist] 잔잔한 안건호 보컬 모음 플레이리스트 ∣ 커버곡 ∣ 코르티스](https://www.youtube.com/watch?v=WHHQaKlBtZk) | W | 22 | 38,801 | 388.0 | – | 241.3 | 13.3분 | 2026-05-14 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 12/12 |
| 146 | [2026 최신곡 랜덤플레이댄스∣ K-pop Random Play Dance 2026 #랜덤플레이댄스 #랜플…](https://www.youtube.com/watch?v=bliX1fxHkKk) | 샤파 | 909 | 350,250 | 385.3 | ×3.2 | 18,445.8 | 6.1분 | 2026-10-03 | 10. 팝송·K팝·J팝 | 한 곡 | 설명 | 46/48 |
| 147 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Stu…](https://www.youtube.com/watch?v=MvV7_DKFZQA) | peacefulvibes… | 12,300 | 4,737,610 | 385.2 | ×13,307.9 | 81,598.2 | 16.3분 | 2026-08-25 | 3. 공부·집중·작업 | 음악 | 설명 | 284/284 |
| 148 | [🍂 알록달록 가을 음악이야기 ∣ Autumn Collection Vol.](https://www.youtube.com/watch?v=o3DojrmPMbs) | little step m… | 85 | 38,254 | 382.5 | ×49.7 | 1,814.1 | 206.4분 | 2026-10-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 3/3 |
| 149 | [Dopamine Reset ∣ Indian Classical Flute Music for Relaxatio…](https://www.youtube.com/watch?v=gSOocWITTT4) | Desert Harmon… | 2,190 | 834,905 | 381.2 | ×1,293.4 | 8,035.9 | 8.4분 | 2026-07-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 132/133 |
| 150 | [너 때문에 하루를 살아 #이별 #이별노래 #이별감성 #새벽감성 #OST #감성발라드 #kpop #kpopb…](https://www.youtube.com/watch?v=hhbJfI8dJ9o) | 글쓰는여자🎀 | 620 | 233,964 | 377.4 | ×573.4 | 1,934.3 | 5.3분 | 2026-06-23 | 10. 팝송·K팝·J팝 | 한 곡 | 없음 | 105/105 |
| 151 | [Lahore Diya ✨ Slowed Reverb ∣ Late Night Vibes ∣ Punjabi Lo…](https://www.youtube.com/watch?v=-rNlgODrgjo) | Arun music 100 | 9,450 | 3,540,863 | 374.7 | ×97.9 | 26,794.8 | 4.2분 | 2026-06-12 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 252/267 |
| 152 | [왜 이제 와｜음색 미쳤다는 반응 나온 새벽 감성 발라드 ｜ なぜ今になって｜音色がすごいという反応が出た、深夜の…](https://www.youtube.com/watch?v=TWunCWy98FU) | Faded Love No… | 1,130 | 421,530 | 373.0 | ×377.7 | 2,652.5 | 4.3분 | 2026-05-16 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 84/85 |
| 153 | [Teri Meri Prem Kahani 💖 Slowed + Reverb ∣ Romantic Lofi Son…](https://www.youtube.com/watch?v=Njmb7oBzkpM) | 🌙 MoonVerse | 7,090 | 2,632,070 | 371.2 | – | 24,314.4 | 6.3분 | 2026-07-06 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 755/768 |
| 154 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 (가사X) 후회 없는 미래를 위해 ✍️ 새벽공부 집중 로파이 BGM🎧 유리숲 플리 🌙](https://www.youtube.com/watch?v=hZLVePYp9Z0) | Yurisoop | 1,240 | 457,609 | 369.0 | ×267.6 | 6,265.1 | 132분 | 2026-08-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 42/45 |
| 155 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 : 딱딱 나 틀딱 ∣ 보카로 근본 플리 1탄](https://www.youtube.com/watch?v=W_G2W0nTGYY) | 윤슬자 | 1,060 | 390,869 | 368.7 | ×14.2 | 2,435.4 | 245.8분 | 2026-05-14 | 기타 | 플레이리스트·모음 | 설명 | 333/333 |
| 156 | [90’S Old Hindi Songs🥰 90s Love Song💘 Udit Narayan, Alka Yag…](https://www.youtube.com/watch?v=qDOFK8SfKmA) | 90s Lovers Po… | 17,600 | 6,427,613 | 365.2 | ×2,487.5 | 96,916.9 | 27.4분 | 2026-08-17 | 기타 | 음악 | 설명 | 217/225 |
| 157 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 🍁 설레는 바람이 부는 가을이 왔나봐 ∣ 틀어두기 좋은 감성 팝송 모음](https://www.youtube.com/watch?v=jmU_fq-iTSE) | Melly Moood | 6,230 | 2,270,310 | 364.4 | ×292.0 | 59,098.2 | 188.2분 | 2026-09-13 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 283/292 |
| 158 | [• playlist 순애](https://www.youtube.com/watch?v=Av29750WaJs) | ros!e | 446 | 161,970 | 363.2 | ×12.8 | 3,051.5 | 18.4분 | 2026-08-30 | 기타 | 플레이리스트·모음 | 없음 | 56/56 |
| 159 | [Desi baddie playlist 💅💌 @desi_diva12 #playlist #baddie #des…](https://www.youtube.com/watch?v=Y3q1y6M79EU) | Desi_.Diva12 | 6,090 | 2,207,171 | 362.4 | ×37.9 | 19,079.4 | 7.3분 | 2026-06-28 | 기타 | 플레이리스트·모음 | 설명 | 207/207 |
| 160 | [Banjaara 🥀 Slowed + Reverb ∣ Best Hindi Lofi Song 🎧 ∣ Anime…](https://www.youtube.com/watch?v=uxMeJy4JMS8) | Broken Sky01 | 6,750 | 2,436,242 | 360.9 | ×800.2 | 28,267.2 | 6.3분 | 2026-07-28 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 857/931 |
| 161 | [Rabba Tu Na Naraz Hovi ❤️ ∣ Soulful Heart Touching Punjabi …](https://www.youtube.com/watch?v=Zh-3CGV7BwQ) | Sufi Usman | 4,740 | 1,679,853 | 354.4 | ×1,039.5 | 20,222.7 | 5.9분 | 2026-07-31 | 기타 | 음악 | 설명 | 214/220 |
| 162 | [Perfect South Indian Playlist 🪷🦢 (+timestamps)](https://www.youtube.com/watch?v=ROBjw6FcYxs) | Being Diva 💅🏻 | 5,720 | 2,020,596 | 353.2 | ×16.7 | 56,707.2 | 7.7분 | 2026-09-16 | 기타 | 플레이리스트·모음 | 설명 | 266/280 |
| 163 | [[PLAYLIST] Biển Đảo Và Em, Fallin Flower, Người Yêu Bỏ Lỡ,……](https://www.youtube.com/watch?v=dMaqYNGvzmA) | wenjin. | 2,560 | 898,679 | 351.1 | ×19.1 | 8,699.9 | 26.2분 | 2026-07-11 | 기타 | 플레이리스트·모음 | 설명 | 442/448 |
| 164 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Study / Focus …](https://www.youtube.com/watch?v=KU7PfC9i9cE) | Focus Music 2… | 4,270 | 1,494,590 | 350.0 | ×3,579.9 | 65,261.8 | 13.8분 | 2026-09-29 | 3. 공부·집중·작업 | 음악 | 설명 | 92/92 |
| 165 | [Sonata in the Dark 🎹 Beethoven-Inspired Melancholic Classic…](https://www.youtube.com/watch?v=sakrZHnzs6k) | Elysian Class… | 189 | 66,082 | 349.6 | ×112.4 | 933.9 | 16분 | 2026-08-12 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 17/17 |
| 166 | [Golden Brown x Love Story - Relaxing Celtic Fantasy Medieva…](https://www.youtube.com/watch?v=hzPdVFw768A) | The Knight Sa… | 3,090 | 1,076,941 | 348.5 | – | 8,145.4 | 16.9분 | 2026-06-12 | 2. 자연 소리·백색소음 | 음악 | 설명 | 536/540 |
| 167 | [CORTIS PLAYLIST (코르티스 플레이리스트) 머니머니머니부터 나니까지](https://www.youtube.com/watch?v=2byCD3x_vPY) | 우울 대신 우웅! | 2,260 | 783,467 | 346.7 | – | 13,450.5 | 41.5분 | 2026-08-25 | 기타 | 플레이리스트·모음 | 없음 | 187/187 |
| 168 | [PLAYLIST I it's like supernatural I 느좋 팝송 기모띠 야르 찹찹 플리](https://www.youtube.com/watch?v=1huhmKD8P7U) | 자세히알아보기 | 551 | 190,399 | 345.6 | ×405.1 | 2,385.5 | 19.6분 | 2026-08-03 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 101/101 |
| 169 | [𝙋𝙤𝙫 :- 𝘽𝙝𝙤𝙟𝙥𝙪𝙧𝙞 𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩 ∣∣ 𝙘𝙝𝙞𝙡𝙡 𝙜𝙪𝙮𝙨 𝙖𝙣𝙙 𝙚𝙣𝙟𝙤𝙮 ∣∣ 𝙂𝘼𝙇𝘼𝙓𝘼𝙔…](https://www.youtube.com/watch?v=areWocW1pXI) | AYUSH | 4,310 | 1,485,637 | 344.7 | ×199.6 | 33,084.2 | 8분 | 2026-09-07 | 기타 | 플레이리스트·모음 | 설명 | 180/188 |
| 170 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 느좋](https://www.youtube.com/watch?v=3lY_H67eQl4) | 고김 | 539 | 185,658 | 344.4 | – | 1,588.4 | 15.3분 | 2026-06-27 | 기타 | 플레이리스트·모음 | 없음 | 52/52 |
| 171 | [Ama hem hem](https://www.youtube.com/watch?v=rPmZucO77sg) | Thatohatsi - … | 36,400 | 12,533,226 | 344.3 | ×69.4 | 119,462.7 | 7.5분 | 2026-07-09 | 기타 | 정보·해설 | 설명 | 0/2,577 |
| 172 | [Prasanna Vadanam – Enigma Style ∣ Lord Vishnu Peaceful Medi…](https://www.youtube.com/watch?v=QeF_NFcmxt4) | devinebeatsst… | 1,360 | 464,147 | 341.3 | ×2,994.5 | 4,823.4 | 5.1분 | 2026-07-18 | 1. 수면·명상·힐링 | 음악 | 설명 | 116/116 |
| 173 | [하우스룰즈가 최고야](https://www.youtube.com/watch?v=V0mzAQ7z3D0) | Yeon | 948 | 322,530 | 340.2 | ×218.2 | 6,465.1 | 18.1분 | 2026-09-02 | 기타 | 플레이리스트·모음 | 설명 | 232/249 |
| 174 | [LEO ROJAS - Top 16 Andean Pan Flute Melodies ★ Full Album -…](https://www.youtube.com/watch?v=wR5yxMCTZA0) | Andean Flute … | 4,840 | 1,639,020 | 338.6 | ×555.6 | 31,002.5 | 98.3분 | 2026-08-30 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 233/240 |
| 175 | [The Complete "Love Is in the Air" Theme by Rock Burwell ∣ O…](https://www.youtube.com/watch?v=ipCco3jw504) | NR ENTERTAINM… | 2,810 | 948,399 | 337.5 | ×3,161.3 | 6,305.8 | 4.5분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 614/623 |
| 176 | [한국 드라마 OST 황금기 모음💗마음을 울리는 인기 노래 모음 하루 종일 들어도 좋은 발라드🎧20-26년 …](https://www.youtube.com/watch?v=Vxw1QiXjDvs) | K-Drama Memor… | 2,670 | 900,235 | 337.2 | ×591.5 | 17,494.7 | 74.3분 | 2026-08-31 | 13. OST·사운드트랙 | 플레이리스트·모음 | 설명 | 140/140 |
| 177 | [【BGM】置いていかないで｜1分後に涙が溢れてくる曲](https://www.youtube.com/watch?v=e9ArzLcNNbw) | 1分後に〇〇する曲🎧 | 1,200 | 404,530 | 337.1 | ×88.7 | 3,065.1 | 4.3분 | 2026-06-12 | 기타 | 음악 | 설명 | 61/63 |
| 178 | [새벽 2시, 잠이 깼다면 다시 자세요 ∣ 6분 후 다시 잠드는 피아노 명상음악 for Deep Sleep …](https://www.youtube.com/watch?v=ViCEPJCOgy4) | 단잠TV | 2,510 | 845,278 | 336.8 | ×1,179.7 | 5,837.5 | 181.7분 | 2026-05-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 216/219 |
| 179 | [DARKHAAST ❤️‍🩹 slowed x reverb Arijit Singh (Lyrics) Ft. Su…](https://www.youtube.com/watch?v=7u9GjyI2yxg) | GK lofi song | 9,720 | 3,253,951 | 334.8 | ×554.9 | 28,050.4 | 6.9분 | 2026-06-28 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 264/271 |
| 180 | [Sands of Cairo at Night ∣ Egyptian Jazz & Relaxing Arabic L…](https://www.youtube.com/watch?v=k74U2uUB67s) | Moonlit Cairo | 4,110 | 1,373,833 | 334.3 | ×715.0 | 21,807.1 | 69.8분 | 2026-08-20 | 4. 카페·매장·라운지 | 음악 | 설명 | 127/140 |
| 181 | [𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 틱톡 그 느좋 노래 모음](https://www.youtube.com/watch?v=NG6SQIGv3-Y) | 뭐야 | 1,720 | 573,591 | 333.5 | ×51.0 | 5,690.6 | 8.9분 | 2026-07-13 | 기타 | 플레이리스트·모음 | 설명 | 112/112 |
| 182 | [💿 마음이 따뜻해지는 감성 발라드 🌸 광고없이 듣는 명곡 🌸 SG워너비, 김범수, 허각](https://www.youtube.com/watch?v=d68bRNKlMQA) | 서울 소울 발라드-Seo… | 899 | 298,608 | 332.2 | ×438.8 | 4,905.3 | 156.2분 | 2026-08-22 | 9. 가요·발라드·트로트 | 음악 | 설명 | 48/48 |
| 183 | [나그네](https://www.youtube.com/watch?v=FFwUpZZGqnc) | 여산일거 | 4,270 | 1,401,005 | 328.1 | ×211.8 | 8,319.5 | 8.9분 | 2026-05-06 | 기타 | 한 곡 | 설명 | 372/375 |
| 184 | [듣기만 해도 설레는 그시절 1990~2026년 사랑하고 슬퍼했던 노래- 휘성,프리스타일,조장혁,임재범,이승…](https://www.youtube.com/watch?v=dCB0KQI7qfU) | 감정 작사가 | 600 | 196,550 | 327.6 | ×1,803.2 | 1,245.4 | 118.5분 | 2026-05-17 | 기타 | 음악 | 설명 | 46/46 |
| 185 | [💖 मेरा चाँद मुझे आया नजर ∣ New Hindi Song 2026 ∣ Romantic S…](https://www.youtube.com/watch?v=FxNQw0BRhWg) | Feel The Music | 3,320 | 1,082,775 | 326.1 | ×641.5 | 30,240.5 | 16.1분 | 2026-09-16 | 기타 | 음악 | 설명 | 65/69 |
| 186 | [JANANAYAGAN - Forest BGM ∣ The Ultimate Cinematic Experienc…](https://www.youtube.com/watch?v=uVuVb5CdEC8) | Massplix | 1,330 | 432,969 | 325.5 | – | 2,552.5 | 4.5분 | 2026-05-05 | 기타 | 음악 | 설명 | 167/167 |
| 187 | [𝐵𝑒𝓈𝓉 𝒮𝑜𝓊𝓉𝒽 𝐼𝓃𝒹𝒾𝒶𝓃 𝒮𝑜𝓃𝑔𝓈 𝒫𝓁𝒶𝓎𝓁𝒾𝓈𝓉 🎶 𝒯𝒶𝓂𝒾𝓁 • 𝒯𝑒𝓁𝓊𝑔𝓊 • 𝑀𝒶𝓁𝒶𝓎𝒶𝓁…](https://www.youtube.com/watch?v=GAXYvJx8rD4) | Nyxelune | 5,650 | 1,835,907 | 324.9 | – | 19,572.2 | 10.3분 | 2026-07-20 | 기타 | 정보·해설 | 설명 | 1,056/1,069 |
| 188 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=29EWidvY0b8) | AR BROTHER | 7,190 | 2,331,578 | 324.3 | – | 50,641.9 | 18.6분 | 2026-09-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 87/89 |
| 189 | [90s Romantic Hits DJ Mix ∣ Hindi Love Song ∣ 90s Romantic B…](https://www.youtube.com/watch?v=Lk2qE-YdhS8) | AM MUSIC HUB | 4,000 | 1,279,110 | 319.8 | ×2,621.1 | 18,748.6 | 16분 | 2026-08-15 | 기타 | 음악 | 설명 | 50/58 |
| 190 | [Hallucination Journey ∣ Stoner Music & Trippy Visuals🌿](https://www.youtube.com/watch?v=QbWDBeBn_OY) | RYNO | 550 | 174,298 | 316.9 | ×213.6 | 1,318.8 | 10분 | 2026-06-12 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 13/13 |
| 191 | ["Comfort song's - All in one playlist"😭✨🌷//part-4//edit by …](https://www.youtube.com/watch?v=617yn663oeA) | Anushri | 7,070 | 2,237,283 | 316.4 | ×12.1 | 30,165.4 | 7.6분 | 2026-08-09 | 기타 | 플레이리스트·모음 | 설명 | 293/298 |
| 192 | [Sad lo_fi🥺💔2026 ultimate](https://www.youtube.com/watch?v=q-iefUnWPCY) | mr prakash 😊 | 5,320 | 1,678,843 | 315.6 | ×1,179.0 | 41,214.2 | 18.6분 | 2026-09-11 | 기타 | 음악 | 설명 | 143/147 |
| 193 | [Playlist For You To Create Fake Scenarios In Your Mind 🤍 ∣ …](https://www.youtube.com/watch?v=0gUwbTCQ78k) | NOXTUNE | 20,700 | 6,498,348 | 313.9 | ×1,069.2 | 87,008.2 | 12.6분 | 2026-08-08 | 기타 | 플레이리스트·모음 | 설명 | 1,399/1,423 |
| 194 | [Omnia vincit](https://www.youtube.com/watch?v=5yKI8IQNzAo) | Soul Beyond S… | 460 | 143,560 | 312.1 | – | 1,228.1 | 4.2분 | 2026-06-27 | 기타 | 정보·해설 | 설명 | 38/39 |
| 195 | [𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 1](https://www.youtube.com/watch?v=rRxojiPo0SU) | 헿 | 630 | 196,339 | 311.6 | – | 2,076.3 | 10.6분 | 2026-07-19 | 기타 | 플레이리스트·모음 | 없음 | 40/40 |
| 196 | [Karpur Gauram ∣ कर्पूर गौरम् ∣ Shiva Stotram Trance Remix ∣…](https://www.youtube.com/watch?v=d47X_wGxFnY) | DigitalDeepDe… | 4,130 | 1,285,689 | 311.3 | ×1,356.2 | 8,147.0 | 11.1분 | 2026-05-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 337/345 |
| 197 | [🎹 Your Name (君の名は。) Relaxing Piano BGM ∣ Anime Piano Lounge](https://www.youtube.com/watch?v=Gv3qOVcC5X8) | AnimeBeats | 1,270 | 394,665 | 310.8 | ×191.9 | 2,192.7 | 57.6분 | 2026-04-25 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 | 19/19 |
| 198 | [𝘊𝘦𝘳𝘵𝘪𝘧𝘪𝘦𝘥 𝘋𝘦𝘴𝘪 𝘉𝘢𝘯𝘨𝘦𝘳𝘴 𝘵𝘩𝘢𝘵 𝘴𝘭𝘢𝘱 (+𝘵𝘪𝘮𝘦𝘴𝘵𝘢𝘮𝘱𝘴) 💅🔥](https://www.youtube.com/watch?v=PZcsGXrrBGY) | A BEE Editz | 10,200 | 3,164,633 | 310.3 | ×52.1 | 52,057.2 | 12.9분 | 2026-08-22 | 기타 | 플레이리스트·모음 | 설명 | 363/374 |
| 199 | [Tum Jo Aaye ✨ ∣∣ Kitab Song ∣∣ Bairan ( Slowed X Reverb ) M…](https://www.youtube.com/watch?v=xyL4vZnw5xs) | Mix Facto 02 | 40,300 | 12,487,210 | 309.9 | ×7,058.9 | 76,248.8 | 20.3분 | 2026-05-11 | 기타 | 음악 | 설명 | 2,719/2,730 |
| 200 | [Jazz Cover Indonesia ∣ Lagu Santai Untuk Bekerja 🎷](https://www.youtube.com/watch?v=kwqjENclcyE) | Ide Rahayu | 4,500 | 1,387,273 | 308.3 | ×767.7 | 13,292.7 | 74.5분 | 2026-07-09 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 152/152 |
| 201 | [Golden Melodies for the Soul (Sax & Violin Lounge)](https://www.youtube.com/watch?v=0shfF2LDgmI) | Timeless Echo | 5,700 | 1,753,939 | 307.7 | ×188.6 | 12,573.7 | 6.7분 | 2026-06-04 | 4. 카페·매장·라운지 | 음악 | 설명 | 356/368 |
| 202 | [Nhạc Thiền Tĩnh Tâm 🌿 Giải Tỏa Căng Thẳng, Buông Bỏ Muộn Ph…](https://www.youtube.com/watch?v=qTOqj4r0FNg) | Thiền Sen Trúc | 2,050 | 628,255 | 306.5 | ×142.0 | 5,931.7 | 58.6분 | 2026-07-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 433/436 |
| 203 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=099F7hK6c8c) | Song verse Hi… | 9,700 | 2,965,412 | 305.7 | – | 77,488.6 | 13분 | 2026-09-14 | 3. 공부·집중·작업 | 음악 | 설명 | 186/189 |
| 204 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ Q. 여전히 잊지 못했나요?](https://www.youtube.com/watch?v=ObbsVpc8iRM) | 청춘 | 1,360 | 415,352 | 305.4 | ×5.1 | 3,101.2 | 24분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 설명 | 491/491 |
| 205 | [Patar Bashori ∣ পাতার বাঁশরী ∣ Lofi Bangla Song ∣ Emotional…](https://www.youtube.com/watch?v=rgKNbCrC-cc) | Jasu LOFI | 26,700 | 8,123,568 | 304.2 | ×4,098.7 | 97,010.5 | 4.1분 | 2026-07-30 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 1,081/1,119 |
| 206 | [Positive September 🍂 Relaxing Coffee Melody & Acoustic Chil…](https://www.youtube.com/watch?v=Bq4sPMz6fUk) | Chill Moments | 4,420 | 1,340,067 | 303.2 | ×249.9 | 24,420.4 | 142.9분 | 2026-08-28 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 98/98 |
| 207 | [LOVEIN & Ismail Uluçay - Drafting (Original Mix)](https://www.youtube.com/watch?v=clQARvetnyk) | LOVEIN | 40,500 | 12,216,195 | 301.6 | ×192.8 | 71,966.4 | 7.3분 | 2026-05-05 | 4. 카페·매장·라운지 | 음악 | 설명 | 422/430 |
| 208 | [pov: you're blushing while listening to this 🎧✨](https://www.youtube.com/watch?v=MOpFDe87RBM) | NIKKU | 9,120 | 2,724,306 | 298.7 | ×3,334.5 | 20,375.1 | 13.4분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 설명 | 1,534/1,537 |
| 209 | [Samadhi in the Stone ∣ Shiva Meditation Music ∣ Himalayan C…](https://www.youtube.com/watch?v=yp10IdD2SxY) | Divya vaani m… | 217 | 64,220 | 295.9 | ×137.2 | 3,826.4 | 6.1분 | 2026-10-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 11/12 |
| 210 | [난 아직 어린데](https://www.youtube.com/watch?v=Zo3DsQ9j2J0) | 맹묘 | 1,580 | 467,442 | 295.9 | – | 3,512.6 | 20.1분 | 2026-06-11 | 기타 | 플레이리스트·모음 | 없음 | 990/997 |
| 211 | [[グラブル] Granblue Fantasy OST - Last Salvation (vs. Raskeid &…](https://www.youtube.com/watch?v=TFsAT5TtzSg) | Decim | 1,650 | 485,696 | 294.4 | ×430.2 | 5,246.8 | 7분 | 2026-07-21 | 기타 | 음악 | 설명 | 416/417 |
| 212 | [🤍Golden brown x Love story (Piano Cover)🤍](https://www.youtube.com/watch?v=dK4RoOPXQ0Q) | Solaceful Keys | 212 | 61,962 | 292.3 | – | 641.7 | 4.1분 | 2026-07-17 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 82/82 |
| 213 | [Peni Me Chheni Satai Diyo -Instagram Trending Lofi Song ∣ A…](https://www.youtube.com/watch?v=gJyWm3GFFik) | Tushar Music … | 5,660 | 1,645,649 | 290.8 | ×1,371.4 | 20,023.3 | 6.1분 | 2026-08-01 | 8. 로파이·시티팝·칠 | 음악 | 없음 | 87/89 |
| 214 | [Cozy Rainy Autumn Café 🍁 Relaxing Day with Warm Jazz Music …](https://www.youtube.com/watch?v=1wyP0BN_jqI) | Tiny Café Jazz | 3,900 | 1,125,330 | 288.6 | ×673.6 | 11,492.8 | 231.1분 | 2026-07-16 | 4. 카페·매장·라운지 | 음악 | 설명 | 457/464 |
| 215 | [Vintage Vibes: Best of 80s with Cyndi Lauper, Modern Talkin…](https://www.youtube.com/watch?v=1n5pMgUPYnk) | Disco Paradis… | 24,500 | 6,982,256 | 285.0 | ×2,887.6 | 101,623.0 | 117.2분 | 2026-08-14 | 기타 | 플레이리스트·모음 | 설명 | 523/532 |
| 216 | ["수고했어..오늘은 푹 자! 😴 마음을 편하게 해주는 피아노 수면음악 (10 Hours)](https://www.youtube.com/watch?v=3br0mkww4do) | jazzyang 재즈냥 | 1,370 | 389,109 | 284.0 | ×1,425.3 | 4,024.1 | 616.6분 | 2026-07-17 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 91/124 |
| 217 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 l 연모(戀慕)](https://www.youtube.com/watch?v=uVbmoXg5YvI) | 미니악단 | 643 | 179,372 | 279.0 | ×726.2 | 1,480.0 | 69분 | 2026-06-23 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 88/90 |
| 218 | [[커버곡] 가는세월 🎧 락발라드로 다시 태어난 불후의 명곡 🎶두둥치 DUDUNGCHI](https://www.youtube.com/watch?v=0J4iOmTGAgo) | 두둥치 | 255 | 70,711 | 277.3 | ×397.3 | 435.6 | 4.2분 | 2026-05-12 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 26/26 |
| 219 | [Shri Krishna Govind Hare Murari - Non Stop Krishna Bhajans …](https://www.youtube.com/watch?v=Tqr5PqrzeQw) | Bhajan World … | 33,000 | 9,143,789 | 277.1 | ×123.8 | 79,641.8 | 29.8분 | 2026-06-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,540/1,543 |
| 220 | [😱NEW VIRAL😱SOBRANG SIKAT SA DISCO DJ MIX KABA-KABA NONSTOP …](https://www.youtube.com/watch?v=EF2Bbs1GWm0) | VIRAL MIX COL… | 16,700 | 4,611,425 | 276.1 | ×20,404.5 | 25,858.6 | 29.8분 | 2026-04-27 | 기타 | 음악 | 설명 | 606/607 |
| 221 | [𝐀𝐋𝐋 𝐓𝐑𝐄𝐍𝐃𝐈𝐍𝐆 𝐇𝐈𝐍𝐃𝐈 𝐒𝐎𝐍𝐆𝐒 𝟐𝟎𝟐𝟔 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 🎀 ∣COZI](https://www.youtube.com/watch?v=HNdauINck9s) | cozi_music | 29,400 | 8,086,546 | 275.1 | ×68.8 | 89,913.7 | 15.2분 | 2026-07-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 2,887/2,923 |
| 222 | [🏨 Luxury Hotel Lounge ∣ Smooth Jazz & Elegant Background Mu…](https://www.youtube.com/watch?v=GBLcMvTFGyg) | AMBER&OAK | 7,170 | 1,971,434 | 275.0 | ×896.1 | 14,093.3 | 100.4분 | 2026-06-04 | 4. 카페·매장·라운지 | 음악 | 설명 | 249/254 |
| 223 | [Rest Your Mind ∣ Your Brain Needs Silence ∣ Dopamine Reset …](https://www.youtube.com/watch?v=UWZ_QQNKmes) | Essential Ind… | 19,100 | 5,242,650 | 274.5 | ×3,583.5 | 44,792.4 | 20.7분 | 2026-06-27 | 1. 수면·명상·힐링 | 음악 | 설명 | 833/843 |
| 224 | [Hum Tere Hote Toh ( Official Music ) Musafir cafe ....](https://www.youtube.com/watch?v=V_UCyoYIWEo) | Music Covers … | 1,750 | 479,234 | 273.9 | ×418.2 | 5,563.4 | 4.4분 | 2026-07-28 | 4. 카페·매장·라운지 | 음악 | 설명 | 79/79 |
| 225 | [Vachindamma (Lyrics + English Translation) ∣ Geetha Govinda…](https://www.youtube.com/watch?v=DliA185LSPU) | LYRICS FOR YOU | 5,220 | 1,425,017 | 273.0 | ×238.0 | 8,202.3 | 4.1분 | 2026-05-01 | 기타 | 한 곡 | 설명 | 240/240 |
| 226 | [Heartbreaking 💔 songs + lofi Mashup songs Slowed Reverb son…](https://www.youtube.com/watch?v=swi-om1VW34) | JR buzdar off… | 16,400 | 4,476,229 | 272.9 | ×12,626.9 | 76,902.4 | 8분 | 2026-08-25 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 202/203 |
| 227 | [𝐬𝐭𝐮𝐝𝐲 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 이번엔 아무한테도 말 안 하고 준비한다 🤫 전문직·수험생 시험공부 집중 로파이 …](https://www.youtube.com/watch?v=eRQFKz_nigU) | loni pli 로니플리 | 1,450 | 394,982 | 272.4 | ×118.0 | 9,434.9 | 137.3분 | 2026-09-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 85/85 |
| 228 | [[ Playlist ] 어떻게 너가 다른 남자를 만나](https://www.youtube.com/watch?v=0USEQaYCf78) | 하온 | 1,700 | 462,610 | 272.1 | – | 5,333.5 | 20.9분 | 2026-07-27 | 기타 | 플레이리스트·모음 | 설명 | 48/48 |
| 229 | [.•♫•♬•𝙁𝙄𝙉𝙀𝙎𝙃𝙔𝙏 PLAYLIST•♬•♫](https://www.youtube.com/watch?v=wYiyAR_dBDU) | loverswift | 4,870 | 1,324,314 | 271.9 | ×31.8 | 14,566.5 | 16.8분 | 2026-07-23 | 기타 | 플레이리스트·모음 | 설명 | 112/113 |
| 230 | [🌊2000년 넘게 전해진 가장 슬픈 노래 ∣ 님아, 그 강을 건너지 마오 ∣ 역사노래 ∣ 사랑노래](https://www.youtube.com/watch?v=4q22526wbNM) | 노래말싸미 | 273 | 73,928 | 270.8 | ×325.7 | 568.9 | 4.6분 | 2026-06-14 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 38/38 |
| 231 | [우리들의 발라드2 1회 플레이리스트｜가을밤 마음을 울린 발라드 7곡 #우리들의발라드 #우발2](https://www.youtube.com/watch?v=wPEmG4xfTLE) | 우낄라꼬 | 1,190 | 321,856 | 270.5 | – | 21,959.5 | 30.4분 | 2026-10-07 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 63/64 |
| 232 | [조영버 노동요](https://www.youtube.com/watch?v=twTedu4I1mg) | 궈바오러우 | 498 | 134,570 | 270.2 | – | 792.5 | 19.7분 | 2026-05-05 | 3. 공부·집중·작업 | 플레이리스트·모음 | 없음 | 205/205 |
| 233 | [Om Namo Bhagavate Vasudevaya ∣ 1 Hour Divine Vishnu Meditat…](https://www.youtube.com/watch?v=OfDob7wO9OU) | Zynora | 4,450 | 1,194,471 | 268.4 | ×253.1 | 7,765.8 | 77.8분 | 2026-05-21 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 317/322 |
| 234 | [[Playlist] 드라마 OST 모음](https://www.youtube.com/watch?v=h_2uk2pTQQA) | playlistsilya… | 771 | 206,420 | 267.7 | ×13.4 | 3,773.1 | 17.5분 | 2026-08-28 | 13. OST·사운드트랙 | 플레이리스트·모음 | 없음 | 17/17 |
| 235 | [Sunday Morning Coffee Club ∣ R&B, Hip Hop, Afrobeats ∣ Feat…](https://www.youtube.com/watch?v=2zzgY6uxZ6o) | EChen | 7,820 | 2,065,573 | 264.1 | ×45.0 | 12,614.3 | 59.4분 | 2026-05-11 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 215/217 |
| 236 | [🌼 Sawan Shiv Bhajan 2026 ∣ Peaceful Mahadev Bhakti Song ∣ B…](https://www.youtube.com/watch?v=I_vnh6nZW6c) | Bhajan Soul C… | 8,590 | 2,268,153 | 264.1 | ×295.9 | 21,430.7 | 5.8분 | 2026-07-08 | 기타 | 음악 | 설명 | 612/616 |
| 237 | [MUSIK SANTAI VIRAL 2026 🎧 Lagu Pop Indonesia Akustik Terbai…](https://www.youtube.com/watch?v=bZEwYquV6Kg) | Akustik Cantik | 10,500 | 2,771,921 | 264.0 | ×495.0 | 28,799.5 | 78.5분 | 2026-07-18 | 기타 | 정보·해설 | 설명 | 182/197 |
| 238 | [별일 없던 하루였는데, 괜히 마음이 시끄러운 밤](https://www.youtube.com/watch?v=mc73qn75vMs) | 리듬다방(김리다) | 1,360 | 357,406 | 262.8 | ×775.3 | 2,653.7 | 7.5분 | 2026-06-09 | 기타 | 음악 | 설명 | 207/209 |
| 239 | [⛈️(No Ads) WARNING: YOU MAY SLEEP FAST 😴 NYC Rain on Window…](https://www.youtube.com/watch?v=HLp0t2jZlKQ) | Dreamy Raining | 3,810 | 992,292 | 260.4 | ×42.9 | 5,791.6 | 600분 | 2026-05-04 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 90/94 |
| 240 | [탈북할 때 듣는 플리](https://www.youtube.com/watch?v=rrgoyhVFJ68) | 비둘기 | 2,920 | 758,371 | 259.7 | ×251.3 | 9,285.9 | 57.6분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 없음 | 1,536/1,536 |
| 241 | [The Shiva Reset ∣ Shiva Trance for the Overstimulated Mind …](https://www.youtube.com/watch?v=N95edHAuFzA) | Nirvana Beats | 7,030 | 1,817,146 | 258.5 | ×352.5 | 24,439.3 | 6.8분 | 2026-08-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 295/304 |
| 242 | [A playlist cuz kanhi is your safe place 🦚🪷🪈🦢 ∣∣ Song playli…](https://www.youtube.com/watch?v=vH7kCnulptw) | Lily⋆.𐙚 ̊ | 9,350 | 2,412,710 | 258.0 | – | 18,311.7 | 17.5분 | 2026-06-12 | 기타 | 플레이리스트·모음 | 설명 | 843/856 |
| 243 | [Rain and Soft Piano Music for Deep Sleep - Calm Sleep and S…](https://www.youtube.com/watch?v=8DzndrjZi18) | RainwoodPiano… | 1,270 | 326,313 | 256.9 | ×213.6 | 6,277.9 | 31.9분 | 2026-08-31 | 1. 수면·명상·힐링 | 음악 | 설명 | 40/41 |
| 244 | [[𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 삶에 무뎌지는 법](https://www.youtube.com/watch?v=8KGuQMhnb14) | 꾹팅 | 1,220 | 311,726 | 255.5 | ×61.7 | 2,298.7 | 19.4분 | 2026-06-08 | 기타 | 플레이리스트·모음 | 설명 | 363/379 |
| 245 | [జీవితంలో ఒక్కసారైనా ఆ ఏడుకొండలు ఎక్కాలయ్యా ∣Soulful Sri Ven…](https://www.youtube.com/watch?v=sfnGhZdoNQk) | Surendra's Mu… | 5,100 | 1,289,044 | 252.8 | ×755.6 | 10,205.0 | 5.3분 | 2026-06-18 | 기타 | 음악 | 설명 | 554/554 |
| 246 | [Bedroom R&B After Hours ∣ Obsessive Love Playlist ∣ Dark ro…](https://www.youtube.com/watch?v=WRi5W4B2vgQ) | afterlove. | 7,490 | 1,892,253 | 252.6 | ×246.4 | 66,034.5 | 81.7분 | 2026-09-23 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 177/189 |
| 247 | [MIMIFY - I Waited too Long (Original Mix)](https://www.youtube.com/watch?v=F2Iga1V4cqo) | MIMIFY | 18,500 | 4,657,825 | 251.8 | ×421.6 | 45,725.6 | 7.8분 | 2026-07-12 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 675/677 |
| 248 | [Zindagi ∣ Chal Thora Aur ∣ Na Kwahish Na Koi Tamana Mujhe (…](https://www.youtube.com/watch?v=dyOp23A-i_o) | cefur studio | 11,400 | 2,867,950 | 251.6 | ×601.5 | 22,631.9 | 4.8분 | 2026-06-17 | 기타 | 음악 | 설명 | 1,835/1,846 |
| 249 | [All Stress Disappears When This Music Starts Playing 🎶 Emot…](https://www.youtube.com/watch?v=mtelE3vg758) | Nature Healin… | 7,390 | 1,826,772 | 247.2 | ×5,577.9 | 11,013.1 | 99.6분 | 2026-05-09 | 1. 수면·명상·힐링 | 음악 | 설명 | 482/480 |
| 250 | [𝐒𝐨𝐧𝐠𝐬 𝐭𝐡𝐚𝐭 𝐟𝐞𝐞𝐥 𝐥𝐢𝐤𝐞 𝐚 𝐛𝐨𝐥𝐥𝐲𝐰𝐨𝐨𝐝 𝐦𝐨𝐯𝐢𝐞 🦢🪷🪐∣∣ songs playlist…](https://www.youtube.com/watch?v=r88MexwnbMA) | ⋆.ʚଓ ּ𝐋𝗒𝗋𝗂𝖼αᥣ… | 6,790 | 1,668,453 | 245.7 | ×17.0 | 19,010.8 | 10.5분 | 2026-07-26 | 기타 | 플레이리스트·모음 | 설명 | 291/291 |
| 251 | [Relaxing Piano Music with Rain Sounds for Deep Sleep - Calm…](https://www.youtube.com/watch?v=dzRT9vqg9xs) | RainwoodPiano… | 1,270 | 311,378 | 245.2 | ×203.8 | 13,550.9 | 110분 | 2026-09-29 | 2. 자연 소리·백색소음 | 음악 | 설명 | 38/39 |
| 252 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐅𝐨𝐫 𝐘𝐨𝐮 𝐓𝐨 𝐂𝐫𝐞𝐚𝐭𝐞 𝐅𝐚𝐤𝐞 𝐒𝐜𝐞𝐧𝐚𝐫𝐢𝐨𝐬 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐌𝐢𝐧𝐝 🤍 ∣ …](https://www.youtube.com/watch?v=flQgOwg4jLI) | Ashik's Cloud… | 15,600 | 3,805,234 | 243.9 | ×6.3 | 36,630.5 | 15.2분 | 2026-07-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 965/970 |
| 253 | [Relax Cha Cha Music 🪘 Havana Cafe Music - Cha Cha Son Cubano](https://www.youtube.com/watch?v=poj2d6YKC6w) | Cha Cha Havan… | 1,610 | 390,924 | 242.8 | ×2,822.6 | 2,334.5 | 6.4분 | 2026-05-07 | 4. 카페·매장·라운지 | 음악 | 설명 | 96/97 |
| 254 | [Viral Pop Songs Cover 2026 🎙 Top Music Playlist Hits](https://www.youtube.com/watch?v=JKRRl5-5-hw) | Acoustic Ther… | 21,000 | 5,079,427 | 241.9 | ×8,990.1 | 34,236.3 | 57.4분 | 2026-05-26 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 설명 | 512/518 |
| 255 | [Put Your Baby to Sleep in 2 Minutes 😴 3 Hours Deep Lullaby …](https://www.youtube.com/watch?v=2W9Y6KcJK1E) | Calm Baby Lul… | 4,190 | 1,006,903 | 240.3 | ×1,910.6 | 5,799.9 | 183.3분 | 2026-05-01 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 0/0 |
| 256 | [Heartbreaking Lofi Mashup 💔 (Slowed + Reverb) ∣ Study, Focu…](https://www.youtube.com/watch?v=6mgb7GxwLvA) | stylish offic… | 12,100 | 2,889,364 | 238.8 | – | 41,138.1 | 7.8분 | 2026-08-13 | 3. 공부·집중·작업 | 음악 | 설명 | 132/135 |
| 257 | [🌼 Soulful Shiv Bhajan 2026 ∣ Peaceful Mahadev Bhakti Song ∣…](https://www.youtube.com/watch?v=soTUDFUagOU) | Divine Bhajan… | 5,950 | 1,394,998 | 234.4 | ×342.5 | 14,415.9 | 6.6분 | 2026-07-17 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 395/397 |
| 258 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=FB8QuMi3fTs) | Z B Official … | 21,200 | 4,908,118 | 231.5 | ×15,832.6 | 77,765.3 | 7.7분 | 2026-08-20 | 3. 공부·집중·작업 | 음악 | 설명 | 203/203 |
| 259 | [Slow and Reverb Pashto Tappy 🎧 ∣ New Pashto Song ∣ Relaxing…](https://www.youtube.com/watch?v=88J0afFBt3s) | MarjanMusic | 4,460 | 1,027,747 | 230.4 | ×548.7 | 8,050.5 | 13분 | 2026-06-16 | 기타 | 음악 | 설명 | 81/81 |
| 260 | [Heartbreaking💔 mashup lofi Songs ∣ Slowed + Reverb ∣ Late N…](https://www.youtube.com/watch?v=z3H-p4r9EC4) | Soulmate Song… | 7,510 | 1,722,783 | 229.4 | ×7,848.7 | 30,639.8 | 8분 | 2026-08-27 | 3. 공부·집중·작업 | 음악 | 설명 | 139/139 |
| 261 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Sad…](https://www.youtube.com/watch?v=KjFcRYZBKs0) | Music Nest HD | 11,800 | 2,693,124 | 228.2 | ×5,249.8 | 107,055.9 | 8.9분 | 2026-09-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 101/103 |
| 262 | [The Love Playlist You’ve Been Looking For😌🤍](https://www.youtube.com/watch?v=G4M-E29DlAE) | Melovo tunes | 3,320 | 755,471 | 227.6 | – | 5,322.2 | 10.4분 | 2026-06-02 | 기타 | 플레이리스트·모음 | 설명 | 800/807 |
| 263 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 틀기만 해도 기분이 좋아지는 플리☀️🌿 (광고없음) 국내 노래 모음](https://www.youtube.com/watch?v=mg5OWdP3DL8) | 오늘의 플리 | 6,700 | 1,522,659 | 227.3 | ×162.8 | 21,709.1 | 603.4분 | 2026-08-13 | 기타 | 플레이리스트·모음 | 없음 | 150/154 |
| 264 | [Music Therapy Helps Restore the Nervous System 🌿 Relaxing M…](https://www.youtube.com/watch?v=yP0NAC8Hzy8) | Clara Monica … | 3,500 | 789,908 | 225.7 | ×24.8 | 6,941.8 | 19.7분 | 2026-06-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 236/239 |
| 265 | [MEGA BASS 🔊🔥 EXTREME NONSTOP EDM REMIX 💯 MONSTER DROP ⚠️ CL…](https://www.youtube.com/watch?v=Kc071SEvHgc) | Street Bass C… | 27,100 | 6,111,463 | 225.5 | ×8,780.8 | 40,925.2 | 42.7분 | 2026-05-26 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 1,383/1,396 |
| 266 | [Hyperfocus ∣ LOCK IN for 3 Hours ∣ Deep Work Study With Me …](https://www.youtube.com/watch?v=UXwJ9RwdyHs) | Work With Paul | 18,000 | 4,058,360 | 225.5 | ×29.6 | 90,020.6 | 172분 | 2026-09-07 | 3. 공부·집중·작업 | 긴 한 곡·반복 | 설명 | 492/507 |
| 267 | [[PLAYLIST] 할머니가 돼서도 들을 노래](https://www.youtube.com/watch?v=Oomy8ijLJxQ) | 당무 | 2,590 | 583,331 | 225.2 | ×91.8 | 3,540.8 | 23.7분 | 2026-05-10 | 기타 | 플레이리스트·모음 | 없음 | 131/131 |
| 268 | [VIVANT ᐸMain themeᐳ](https://www.youtube.com/watch?v=MuGFcUggtDs) | Akira Senju -… | 7,280 | 1,629,345 | 223.8 | ×24.9 | 18,682.2 | 4.6분 | 2026-07-27 | 13. OST·사운드트랙 | 정보·해설 | 설명 | 0/0 |
| 269 | [🍂편안해지는 따뜻한 가을 노래 ∣ 추억의 올드팝송 ∣ 가을 카페 팝송 감미로운 여친 목소리∣ Oldies …](https://www.youtube.com/watch?v=yfKtKmmUsoQ) | 나무감성 NAMUVIBE | 2,410 | 534,398 | 221.7 | ×35.8 | 23,752.0 | 135분 | 2026-09-29 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 173/174 |
| 270 | [Relaxing Jazz Café in Paris ∣ Cozy Rainy Evening Jazz Ambie…](https://www.youtube.com/watch?v=3mNYh_27x5k) | European Jazz… | 1,240 | 272,280 | 219.6 | ×467.8 | 3,958.1 | 14.5분 | 2026-08-14 | 2. 자연 소리·백색소음 | 음악 | 설명 | 1/1 |
| 271 | [Playlist ∣ Start Your Work with This 😎 Light Focus, Solid R…](https://www.youtube.com/watch?v=PF7MEHrmFjQ) | Noirvoya | 371 | 81,174 | 218.8 | ×336.1 | 604.5 | 16.4분 | 2026-06-10 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 30/30 |
| 272 | [Peaceful Piano, Flute & Water Sounds 💧 ∣ Relaxing Music for…](https://www.youtube.com/watch?v=NO0Y0KepgZw) | Cozy Flow Rel… | 763 | 165,716 | 217.2 | ×199.8 | 3,437.4 | 14.6분 | 2026-09-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 78/96 |
| 273 | [[𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁] 행운이 따라올 것 같은 여름 플리 🌊🚃 ∣ 괜히 여행 가고 싶어지는 음악 ∣ 카페 BG…](https://www.youtube.com/watch?v=sdyu1kMXQPw) | HIWAVA | 2,080 | 450,955 | 216.8 | ×394.5 | 3,166.5 | 165.3분 | 2026-06-01 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 157/158 |
| 274 | [Top Spotify Hits 2026 🎵 Trending English Love Songs ∣ Acous…](https://www.youtube.com/watch?v=FPlJt2A0yYo) | Chill Chord | 11,900 | 2,577,455 | 216.6 | ×143.0 | 27,024.7 | 54.8분 | 2026-07-18 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 282/286 |
| 275 | [Asiwafuni](https://www.youtube.com/watch?v=9c1b0JLxKG4) | Benzoo - Topic | 11,900 | 2,542,749 | 213.7 | ×11.0 | 30,301.2 | 6.7분 | 2026-07-30 | 기타 | 음악 | 설명 | 0/1,364 |
| 276 | [राग भैरव ∣ भगवान शिव का पवित्र प्रभात राग ∣ Raga Bhairav ∣ …](https://www.youtube.com/watch?v=3kgbzavVRiY) | मनतरंग ∣ ManT… | 1,950 | 415,855 | 213.3 | – | 9,115.7 | 11.7분 | 2026-09-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 82/82 |
| 277 | [이선희 노래 〈잘가요, 내사랑〉 ∣ Goodbye, The One I Loved ∣ 再见了，我曾爱过的人 ∣…](https://www.youtube.com/watch?v=Ibdr_7ukGyI) | AI음악으로멜론1위찍습니다 | 3,080 | 651,857 | 211.6 | ×1,129.7 | 4,116.0 | 4.8분 | 2026-05-16 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 707/713 |
| 278 | [Sad Song Playlist (+ with timestamps) !!](https://www.youtube.com/watch?v=q48Y5Hf83Bk) | Mood Tapes 🎶 | 17,900 | 3,785,269 | 211.5 | ×85.9 | 28,104.7 | 14.7분 | 2026-06-09 | 기타 | 플레이리스트·모음 | 설명 | 1,520/1,544 |
| 279 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 안 붙잡을게, 진짜로](https://www.youtube.com/watch?v=mgSfxFVkmv4) | 탱이 | 1,680 | 354,226 | 210.8 | ×34.0 | 2,837.9 | 18.3분 | 2026-06-19 | 기타 | 플레이리스트·모음 | 설명 | 150/151 |
| 280 | [[Playlist] 스트레이 키즈 노래 모음 연속 듣기 🔥 Stray Kids Best Songs 2026…](https://www.youtube.com/watch?v=Lj8FLAC9h58) | 내귀에 PLY | 2,300 | 483,211 | 210.1 | ×1,421.2 | 6,862.3 | 120.4분 | 2026-08-12 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 164/174 |
| 281 | [Odysseus](https://www.youtube.com/watch?v=WCxx_OVOVUw) | Ludwig Görans… | 43,300 | 9,051,097 | 209.0 | ×18.6 | 92,437.4 | 8.7분 | 2026-07-16 | 13. OST·사운드트랙 | 음악 | 설명 | 0/5,631 |
| 282 | [Gladiator Ambience — Cinematic & Emotional Music for Honor …](https://www.youtube.com/watch?v=iBofqYaXA_U) | sleyvenn | 5,050 | 1,052,492 | 208.4 | ×238.7 | 7,207.2 | 120분 | 2026-05-29 | 2. 자연 소리·백색소음 | 음악 | 설명 | 284/292 |
| 283 | [(NO MID-ROLL ADS) Cozy Rainy & Spooky Halloween 🍂 Fall Jazz…](https://www.youtube.com/watch?v=p1b2tWu4XkE) | Relaxing Chri… | 4,360 | 905,017 | 207.6 | ×331.1 | 50,645.7 | 249.2분 | 2026-10-04 | 7. 재즈·보사노바 | 음악 | 설명 | 383/439 |
| 284 | [빗속 파리의 라흐마니노프 🌧️ In the Style of Rachmaninoff , 깊고 잔잔한 클래식 …](https://www.youtube.com/watch?v=msDBphyeZIc) | Moonlight rep… | 2,390 | 493,045 | 206.3 | ×778.9 | 4,950.5 | 65.6분 | 2026-07-14 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 116/117 |
| 285 | [일할 때 듣기 좋은 발라드 베스트 100곡 🌸 광고 없는 감성 플레이리스트 왁스, 소울스타, 원티드, 임창…](https://www.youtube.com/watch?v=aJ61beIT3qc) | Dragon Melody | 1,260 | 259,532 | 206.0 | ×551.0 | 2,042.9 | 138.7분 | 2026-06-17 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 30/31 |
| 286 | [#등불 - #영사운드(1972년) Covered by sMUSIC#영사운드 #Reinterpreting K…](https://www.youtube.com/watch?v=tW_gZzlbg-4) | sMusic 7080_명… | 6,860 | 1,407,280 | 205.1 | ×534.0 | 8,512.2 | 4.2분 | 2026-05-10 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 없음 | 296/303 |
| 287 | [सुकून देने वाली धुन 🏔️ ∣ Mind Relaxing Music ∣ Flute Music](https://www.youtube.com/watch?v=dLdXYN50hgQ) | Soulful Music… | 4,510 | 923,497 | 204.8 | ×14,317.8 | 6,654.8 | 5.9분 | 2026-06-05 | 기타 | 음악 | 설명 | 331/333 |
| 288 | [A playlist of nusrat fateh ali khan all popular qawaali's 💝💘](https://www.youtube.com/watch?v=idCpl6LfnKo) | preet_slaylist | 49,800 | 10,142,363 | 203.7 | ×60.0 | 63,992.7 | 9.2분 | 2026-05-16 | 기타 | 플레이리스트·모음 | 설명 | 4,952/5,021 |
| 289 | [lock the f*** in. (playlist)](https://www.youtube.com/watch?v=1mAMpmFvceY) | lucent | 7,670 | 1,552,483 | 202.4 | ×217.0 | 24,484.0 | 240분 | 2026-08-19 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 394/424 |
| 290 | [Lagu Pop Santai Indonesia 2026 ☕ Lagu Pop Indonesia Terbaik…](https://www.youtube.com/watch?v=MoghOkKhNFk) | MITRO MUSIC | 5,450 | 1,095,191 | 200.9 | ×240.1 | 6,897.1 | 83.7분 | 2026-05-16 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 178/178 |
| 291 | [🍉 아침에 커피 마시면서 혼자 듣는데 너무좋다. ∣ 하루 종일 틀어 놓으세요🎵7080추억의 올드팝 #감성팝…](https://www.youtube.com/watch?v=iRAcLZyPbsA) | woozune | 5,780 | 1,154,763 | 199.8 | ×102.7 | 13,364.9 | 74.3분 | 2026-07-27 | 9. 가요·발라드·트로트 | 음악 | 설명 | 187/197 |
| 292 | [☀️ Top Acoustic Love Hits 2026 💚 Relaxing Pop Covers for Pe…](https://www.youtube.com/watch?v=r0t7mEWAGyY) | Acoustic Pulse | 9,650 | 1,921,656 | 199.1 | ×44.0 | 18,418.6 | 51.8분 | 2026-07-10 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 166/168 |
| 293 | [Iske da faniyaar song Slowed + Reverb Lofi Music Mix ∣ Chil…](https://www.youtube.com/watch?v=yoLa1Xlkhvo) | @sanjumusic | 5,440 | 1,081,635 | 198.8 | ×596.9 | 9,937.0 | 5.1분 | 2026-07-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 217/217 |
| 294 | [들꽃처럼 살다가](https://www.youtube.com/watch?v=1vBXiLsHZrs) | 소은뮤직 | 583 | 115,471 | 198.1 | ×487.2 | 990.2 | 4.7분 | 2026-06-27 | 기타 | 음악 | 설명 | 108/114 |
| 295 | [Könül Xasıyeva - Yaralayırsan ∣ Piano Version by Xeqan](https://www.youtube.com/watch?v=Fqfo2bGkZik) | Xeqan | 5,780 | 1,125,296 | 194.7 | ×26.8 | 6,553.1 | 5.5분 | 2026-05-03 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 428/433 |
| 296 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 듣자마자 흥 폭발하는🔥 최신 K-POP 노래 모음 노동요](https://www.youtube.com/watch?v=yngpCQNKY_M) | 클로버 플레이리스트 | 3,580 | 696,552 | 194.6 | ×10.0 | 5,852.5 | 40.9분 | 2026-06-25 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 69/70 |
| 297 | [애매모호한 첫사랑](https://www.youtube.com/watch?v=A6rImTTl348) | na tsu | 933 | 181,463 | 194.5 | – | 1,912.6 | 19.3분 | 2026-07-19 | 기타 | 플레이리스트·모음 | 설명 | 419/419 |
| 298 | [🔥 𝗔𝗟𝗟 𝗧𝗥𝗘𝗡𝗗𝗜𝗡𝗚 𝗣𝗔𝗞𝗜𝗦𝗧𝗔𝗡𝗜 𝗦𝗢𝗡𝗚𝗦 🎶 ∣ 𝗩𝗜𝗥𝗔𝗟 𝗛𝗜𝗧𝗦 𝟮𝟬𝟮𝟲 🎧 ∣ 𝗧𝗢𝗣 …](https://www.youtube.com/watch?v=XL5PUUwrztg) | cozi_music | 29,400 | 5,695,105 | 193.7 | ×48.5 | 83,830.0 | 19.6분 | 2026-08-15 | 1. 수면·명상·힐링 | AI 음악 | 설명 | 2,153/2,236 |
| 299 | [2026 Ultimate Mind Relaxing Lofi Beats ∣ Study Sleep & Chil…](https://www.youtube.com/watch?v=FYePEj0IZC8) | Ace LoFi | 9,400 | 1,784,648 | 189.9 | ×4,684.1 | 17,221.2 | 28.2분 | 2026-07-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 140/140 |
| 300 | [일할때 듣기좋은 발라드 추천 광고없는 노래모음 유튜브 베스트곡 TOP BEST 100 임창정,성시경,더원,…](https://www.youtube.com/watch?v=YVeqKohQmuw) | LeafVibe 4K | 1,380 | 261,976 | 189.8 | ×327.9 | 1,988.4 | 71.8분 | 2026-06-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 13/13 |
| 301 | [Navkar mantra's Golden Shield ∣ Feel the Ancient Jain Power…](https://www.youtube.com/watch?v=FEQe99gciwU) | Navkarbhakti … | 4,350 | 821,108 | 188.8 | – | 4,740.3 | 8.1분 | 2026-05-02 | 1. 수면·명상·힐링 | 음악 | 설명 | 197/197 |
| 302 | [아득히 먼 곳 ∣ 이별 감성 발라드 ∣ 커버 노래 편곡 수노 AI](https://www.youtube.com/watch?v=8l6a5DRZqHU) | 엄마의 세월 - 한국 발… | 1,110 | 209,114 | 188.4 | ×409.2 | 1,392.5 | 4분 | 2026-05-25 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 20/20 |
| 303 | [ĐẾN KHI NÀO (Hot Trend)...Mặt Trời Ngừng Chiếu ∣ Những Bản …](https://www.youtube.com/watch?v=pB64u5qBd5g) | Chà Là Chill | 38,900 | 7,327,149 | 188.4 | ×61.9 | 143,795.8 | 91.8분 | 2026-09-01 | 8. 로파이·시티팝·칠 | 긴 한 곡·반복 | 설명 | 509/518 |
| 304 | [【洋楽Playlist】何も考えずに聴きたい心地いいChill R&B｜Relax｜Smooth Vibes](https://www.youtube.com/watch?v=6qkUHaRXvtE) | Ethereal TIME | 4,720 | 888,777 | 188.3 | ×419.8 | 7,609.3 | 65.2분 | 2026-06-27 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 63/63 |
| 305 | [Relax Cha Cha Music 🪘 Havana Cafe Music - Cha Cha Son Cuban…](https://www.youtube.com/watch?v=sUO0XTpAiCY) | Cha Cha Havan… | 1,610 | 300,707 | 186.8 | ×2,171.2 | 2,012.0 | 5.5분 | 2026-05-25 | 4. 카페·매장·라운지 | 음악 | 설명 | 20/20 |
| 306 | [♫ 𝗔𝗹𝗹 𝗛𝗶𝗻𝗱𝗶 𝗧𝗿𝗲𝗻𝗱𝗶𝗻𝗴 𝗦𝗼𝗻𝗴𝘀 𝗼𝗳 2026 ♫🎧🤍#HindiSongs#Playlist](https://www.youtube.com/watch?v=eC61t3Nw-vs) | 𝐌𝐚𝐧𝐬𝐢~ | 8,620 | 1,608,608 | 186.6 | ×6.8 | 14,626.4 | 11.9분 | 2026-07-04 | 기타 | 플레이리스트·모음 | 없음 | 506/506 |
| 307 | [[ 𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕 ] 전남친 잊는 플리](https://www.youtube.com/watch?v=bLYI4NHve9Y) | 아야 | 1,300 | 241,360 | 185.7 | – | 2,948.7 | 17.4분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 없음 | 55/57 |
| 308 | [Happy Morning Jazz 🎶 January Bossa Nova Instrumental and Re…](https://www.youtube.com/watch?v=qZjNyrGF4pk) | FunToon Rhymes | 9,570 | 1,775,622 | 185.5 | ×108.5 | 110,923.1 | 15.4분 | 2026-10-06 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 0/0 |
| 309 | [🎶 2026 Ultimate Mind Relaxing Lofi Beats ∣∣ Study, Sleep & …](https://www.youtube.com/watch?v=453LJJX0ncc) | Hindi Lofi So… | 12,700 | 2,344,100 | 184.6 | ×4,878.5 | 20,171.0 | 30.7분 | 2026-06-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 199/199 |
| 310 | [Peaceful Piano with Rain Sounds ∣ Relaxing Sleep Music for …](https://www.youtube.com/watch?v=Ral_oDb724k) | Soft Rain Pia… | 2,690 | 496,093 | 184.4 | ×85.6 | 3,795.4 | 47.1분 | 2026-06-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 104/104 |
| 311 | [🌧️ Relaxing Piano & Bird Sounds ∣ Rainy Nature Ambience for…](https://www.youtube.com/watch?v=O0goqFNLWDs) | Solace Birdso… | 1,790 | 329,905 | 184.3 | ×55.0 | 3,632.9 | 92.3분 | 2026-07-23 | 2. 자연 소리·백색소음 | 음악 | 설명 | 223/223 |
| 312 | [POV: The ultimate south indian dance🪩 playlist to blast at …](https://www.youtube.com/watch?v=Hh_Vewjk7wo) | Ethereal Echo… | 12,700 | 2,337,763 | 184.1 | ×7.4 | 17,044.2 | 18.6분 | 2026-06-07 | 기타 | 플레이리스트·모음 | 설명 | 299/300 |
| 313 | [Viral OPM Hits 2026 🇵🇭 Trending Tagalog Love Songs 🎧 Spotif…](https://www.youtube.com/watch?v=au1ycoHD9cY) | Calm Guitar | 11,600 | 2,119,667 | 182.7 | ×102.7 | 27,753.8 | 64.6분 | 2026-08-06 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 199/201 |
| 314 | [가을이 머무는 호숫가 ∣ 피아노·첼로·바이올린으로 듣는 고요한 클래식](https://www.youtube.com/watch?v=zNMH3ua74tE) | 순례자 우물 | 939 | 171,424 | 182.6 | ×484.2 | 3,812.1 | 122분 | 2026-09-07 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 36/39 |
| 315 | [Calm Work Music ∣ High Concentration Music for Studying, Fo…](https://www.youtube.com/watch?v=qXQ6wEipSug) | Calm Work Stu… | 5,770 | 1,031,195 | 178.7 | ×305.8 | 9,652.4 | 130.8분 | 2026-07-07 | 3. 공부·집중·작업 | 음악 | 설명 | 296/301 |
| 316 | [이수연, K-trot, [감성노래 탑7 메들리]](https://www.youtube.com/watch?v=wz-ZkvuAdTg) | 통기타 한석 TV | 2,620 | 467,922 | 178.6 | – | 2,812.4 | 26.3분 | 2026-05-08 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 없음 | 311/320 |
| 317 | [Heartbreaking 💔 Lofi Mashup 🎧Slowed +Reverb Songs ∣ Study,F…](https://www.youtube.com/watch?v=mw6hxi9NJwc) | Peaceful Vibe… | 5,320 | 947,226 | 178.1 | ×4,365.1 | 15,800.0 | 7.3분 | 2026-08-23 | 3. 공부·집중·작업 | 음악 | 설명 | 105/109 |
| 318 | [ANDEAN PAN FLUTE 🌿 Gentle Healing Music to Calm the Mind l …](https://www.youtube.com/watch?v=1NjCSdhJnjo) | Ginevra Melod… | 186 | 32,354 | 173.9 | ×110.8 | 1,565.4 | 94.5분 | 2026-10-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 6/6 |
| 319 | [सुनते ही नींद आएगी 😴 ∣ दिव्य निद्रा संगीत ∣ Himalayan Deep …](https://www.youtube.com/watch?v=R_LBzRfzBBo) | Sanatan Bodh | 3,060 | 532,165 | 173.9 | ×1,081.6 | 5,184.5 | 40분 | 2026-07-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 157/158 |
| 320 | [안들으면후회함 playlist](https://www.youtube.com/watch?v=_eAnA8TgKWM) | 서른마흔오백다섯살 | 3,410 | 591,466 | 173.4 | ×66.5 | 4,234.7 | 24분 | 2026-06-04 | 기타 | 플레이리스트·모음 | 없음 | 169/169 |
| 321 | [눈 뜨면 아침인 숲속 평온한 빗소리 ∣ 🌲 깊은 수면을 위한 평온한 백색소음 (Rain Sounds for…](https://www.youtube.com/watch?v=ri10d9TXXGE) | Cozy Rain on … | 3,290 | 566,383 | 172.2 | ×127.4 | 5,730.7 | 210분 | 2026-07-15 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 127/134 |
| 322 | [20 Of The Most Beautiful Classical Adagios for Relaxation a…](https://www.youtube.com/watch?v=t-scHKetq7I) | Classical Ins… | 13,700 | 2,354,595 | 171.9 | ×87.7 | 13,243.7 | 120분 | 2026-04-27 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 946/1,000 |
| 323 | [[스페인 감성] "Hermano Sócrates ∣ 테스형 - 나훈아 " Korean OldPop 한국명곡](https://www.youtube.com/watch?v=FMwiMkgcfW8) | 스페인 감성 한국 올드송 | 1,420 | 241,060 | 169.8 | ×6.5 | 10,618.4 | 5.1분 | 2026-09-29 | 12. 커버·노래 부르기 | 음악 | 설명 | 68/73 |
| 324 | [Spa & Healing Music · 3 Hours 🌺 Luxury Relaxation for Massa…](https://www.youtube.com/watch?v=uzHIWyuadHM) | Halcyon Hours | 364 | 61,248 | 168.3 | ×914.1 | 532.2 | 180분 | 2026-06-29 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 5/5 |
| 325 | [Zen Flute Therapy 🎶 ∣ Dopamine Reset Music for Stress & Anx…](https://www.youtube.com/watch?v=ldZHxztiahU) | Osen Moonlight | 10,100 | 1,697,504 | 168.1 | ×533.1 | 23,320.3 | 113.8분 | 2026-08-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 444/459 |
| 326 | [Hindi Lofi Nights ∣ Yeh Tune Kya Kiya x Ishq Risk x Ishq x …](https://www.youtube.com/watch?v=oHrvGKhcW4s) | Songhalo | 11,000 | 1,848,690 | 168.1 | ×22.1 | 11,083.9 | 23.8분 | 2026-05-08 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 907/907 |
| 327 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 첫 비트부터 심박수 폭발 ❤️ 미친 텐션 운동 플리 ∣ 헬스 · 러닝 · EDM · 힙…](https://www.youtube.com/watch?v=XrUNOYMFd58) | Grind Vibe | 5,550 | 928,287 | 167.3 | ×135.0 | 6,981.3 | 80.7분 | 2026-06-11 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 337/340 |
| 328 | [Om Shanti Om - Climax BGM ∣ Cineforge Records](https://www.youtube.com/watch?v=eGnTmVPO--k) | Cineforge Rec… | 3,120 | 519,737 | 166.6 | ×59.4 | 3,540.2 | 9.8분 | 2026-05-28 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 111/112 |
| 329 | [얼마나 들었는지 감도 안 옴](https://www.youtube.com/watch?v=1vELYr_nSxI) | shhh... | 6,860 | 1,140,977 | 166.3 | ×209.6 | 19,534.9 | 24.8분 | 2026-08-24 | 기타 | 음악 | 설명 | 169/174 |
| 330 | [DIFFERENT ROAD - Melodic Viking Music for Focus & Deep Study](https://www.youtube.com/watch?v=pP54saekswg) | Jonas & Ida | 2,610 | 432,331 | 165.6 | ×142.7 | 4,324.5 | 6.5분 | 2026-07-14 | 3. 공부·집중·작업 | 음악 | 설명 | 87/88 |
| 331 | [살면서 한 번쯤 들어봐야 할 클래식 15곡 ∣ 공부·휴식·카페에서 듣기 좋은 클래식 음악](https://www.youtube.com/watch?v=hDepOWqLbXI) | canvasclassics | 183 | 30,239 | 165.2 | – | 250.3 | 152.1분 | 2026-06-23 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 3/3 |
| 332 | [새벽 2시~4시 재입면 음악 ∣ 생각 멈추고 다시 잠드는 BGM [중간광고없음]](https://www.youtube.com/watch?v=KBdCHv2UpRU) | 단잠TV | 2,510 | 411,588 | 164.0 | ×574.4 | 2,559.8 | 191.6분 | 2026-05-14 | 2. 자연 소리·백색소음 | 음악 | 설명 | 62/63 |
| 333 | [Playlist ∣ 어때 그 남잔 나보다 더 나?](https://www.youtube.com/watch?v=Eh4ZRMyh8vo) | 안개 | 3,200 | 524,009 | 163.8 | ×16.4 | 3,969.8 | 25.6분 | 2026-06-12 | 기타 | 플레이리스트·모음 | 설명 | 69/69 |
| 334 | [ENIGMA Style Music🔥Mystic River🔥2026](https://www.youtube.com/watch?v=5m7k60JKkLc) | VoiceLine Mus… | 4,020 | 657,677 | 163.6 | ×3,715.7 | 3,661.4 | 5.2분 | 2026-04-25 | 기타 | 음악 | 설명 | 199/199 |
| 335 | [💃🔥𝐀 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐓𝐡𝐚𝐭 𝐖𝐢𝐥𝐥 𝐖𝐚𝐤𝐞 𝐔𝐩 𝐘𝐨𝐮𝐫 𝐈𝐧𝐧𝐞𝐫 𝐃𝐚𝐧𝐜𝐞𝐫 🎶⚡{+timest…](https://www.youtube.com/watch?v=ASY7vTTB-wo) | 𝙏𝙖𝙣𝙭 𝙀𝙙𝙞𝙩𝙯 🦋 | 13,200 | 2,157,957 | 163.5 | ×10.1 | 15,650.5 | 14.5분 | 2026-06-06 | 기타 | 플레이리스트·모음 | 설명 | 281/282 |
| 336 | [Relaxing Guzheng & Bamboo Flute 🌸Ancient Chinese Music 🌸 #a…](https://www.youtube.com/watch?v=N4y79JaFBeo) | Yuzira Music | 4,270 | 696,993 | 163.2 | ×2,833.3 | 4,416.2 | 64.1분 | 2026-05-17 | 기타 | 음악 | 설명 | 290/292 |
| 337 | [A Few Minutes of Mahadev ∣ Feel His Presence Instantly ∣ Ga…](https://www.youtube.com/watch?v=hsGWmUi1TQc) | Sacred Vedic … | 10,800 | 1,757,639 | 162.7 | ×472.2 | 9,833.2 | 37.9분 | 2026-04-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 462/465 |
| 338 | [99% DEEP SLEEP in 3 Minutes (NO ADS) • Brain Massage While …](https://www.youtube.com/watch?v=ZqzEQHOrvPw) | Awakened Soul | 5,060 | 816,096 | 161.3 | ×303.2 | 26,504.7 | 711분 | 2026-09-21 | 1. 수면·명상·힐링 | 음악 | 설명 | 439/462 |
| 339 | [Back To Chennai – Chennai Express Theme Music ∣ Shah Rukh K…](https://www.youtube.com/watch?v=g40bXb0KIFs) | Octave Valley | 1,360 | 217,185 | 159.7 | ×34.4 | 1,315.8 | 13.6분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 39/40 |
| 340 | [[90 Phút Lạc Trong Không Gian Huyền Ảo] Mixset Chillout Hoà…](https://www.youtube.com/watch?v=5BxoSQw9tOo) | Bee Chill | 8,860 | 1,403,296 | 158.4 | ×13.7 | 18,721.2 | 92.3분 | 2026-08-08 | 8. 로파이·시티팝·칠 | 긴 한 곡·반복 | 설명 | 115/119 |
| 341 | [노래방차트 발라드 2026년 7월 1차 🎤 최신 인기차트 노래모음 ∣ 발라드 플레이리스트](https://www.youtube.com/watch?v=uedFUZ1kMjk) | 오늘의 음악 | 1,130 | 178,540 | 158.0 | ×409.5 | 2,582.9 | 83.2분 | 2026-08-14 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 8/8 |
| 342 | [#장터에핀작은꽃#인생트로트#감성트로트#눈물나는노래#가족사랑#엄마생각#할머니사랑#추억의노래#7080감성#중년…](https://www.youtube.com/watch?v=U-J6pNop1bU) | 인생 감성 트롯트노래 | 1,780 | 281,016 | 157.9 | ×498.3 | 2,677.5 | 4.8분 | 2026-07-09 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 18/18 |
| 343 | [5 Minute Deep Meditation Music for Positive Energy • Relax …](https://www.youtube.com/watch?v=6-FPw2wSYsw) | Christmas Hav… | 289 | 45,158 | 156.3 | ×57.1 | 310.8 | 5.3분 | 2026-05-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 5/5 |
| 344 | [Könül Xasıyeva - Sən Məndən Xəbərsiz ∣ Piano Version by Xeq…](https://www.youtube.com/watch?v=ECMO19Ykny4) | Xeqan | 5,780 | 894,419 | 154.7 | ×21.3 | 5,335.9 | 6.1분 | 2026-05-07 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 379/382 |
| 345 | [[기절수면/중간광고없음] 10분후 검은화면/ 듣자마자 잠드는 대나무숲 빗소리 🌧️잎 끝에 떨어지는 편안한 …](https://www.youtube.com/watch?v=l89z7BzLSmI) | 신가네숲 빗소리 | 1,350 | 208,645 | 154.6 | ×30.5 | 1,818.9 | 420분 | 2026-06-29 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 41/41 |
| 346 | [Good Morning Vibes 💕 Best Acoustic Love Songs to Start Your…](https://www.youtube.com/watch?v=fxrrC6UCItY) | NiceOne | 10,900 | 1,684,475 | 154.5 | ×888.7 | 24,624.8 | 91.9분 | 2026-08-14 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 | 146/147 |
| 347 | [THE ULTIMATE HARYANVI PLAYLIST 🔥 !! #playlist #haryanvisong…](https://www.youtube.com/watch?v=SoVJljRBGMw) | 𐙚 𝒦𝒽𝓊𝓈𝒽𝒷𝓊𝓊 | 19,500 | 3,007,471 | 154.2 | ×5.9 | 26,585.9 | 6.9분 | 2026-07-01 | 기타 | 플레이리스트·모음 | 설명 | 305/306 |
| 348 | [[Playlist] ENHYPEN (엔하이픈)-'THE SIN : BLISS'丨2026 Full Album](https://www.youtube.com/watch?v=kG-CrsJXx5w) | κööκκ | 1,870 | 288,179 | 154.1 | ×72.0 | 4,660.6 | 15.9분 | 2026-08-21 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 240/241 |
| 349 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 야르한 제이팝](https://www.youtube.com/watch?v=3QaZldwEZ3g) | 탱이 | 1,680 | 258,668 | 154.0 | ×24.8 | 1,977.9 | 18.3분 | 2026-06-13 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 59/59 |
| 350 | [HEART BREAK 💔 SAD 😭 LOFI MASHUP ∣∣ HEART BROKEN 💔 HINDI SON…](https://www.youtube.com/watch?v=rXZRZ5z0Oqo) | Adnan Official | 10,000 | 1,535,644 | 153.6 | ×14,625.2 | 11,028.1 | 18.8분 | 2026-06-05 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 107/107 |
| 351 | [SONGS THAT’LL MAKE YOU DANCE AT 3AM ✨🔥 FT. DESI SONGS ❤️‍🔥💋…](https://www.youtube.com/watch?v=oIXkjb_FPC4) | Dramanique⋆.𐙚… | 31,800 | 4,802,213 | 151.0 | ×10.2 | 29,849.0 | 29.3분 | 2026-05-14 | 기타 | 음악 | 설명 | 746/747 |
| 352 | [Enigma - Eternity of Love (Enigmatic Ambient / New Age 4K)](https://www.youtube.com/watch?v=2ohn3S5VafQ) | 5TH FREQUENCY | 1,040 | 156,958 | 150.9 | ×184.0 | 2,309.4 | 5.4분 | 2026-08-15 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 60/60 |
| 353 | [Peaceful Autumn Escape 🍂 Colorful Forest Scenery with Natur…](https://www.youtube.com/watch?v=kpm3m2Afk18) | Gentle Nature… | 5,840 | 875,819 | 150.0 | ×37.5 | 10,823.8 | 142.2분 | 2026-08-02 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 143/145 |
| 354 | [김동률 명곡 모음 🎵 베스트 발라드 20곡 연속듣기 ∣ 다시 사랑한다 말할까 · 감사 · 기억의 습작 ∣ …](https://www.youtube.com/watch?v=9kIULv7grWs) | 노래모음 | 2,130 | 319,169 | 149.8 | – | 2,295.0 | 75.3분 | 2026-06-05 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 49/49 |
| 355 | [Disney Sleep Piano Collection 🧜‍♀️ ∣ Ariel’s Peaceful Night…](https://www.youtube.com/watch?v=kPPtBzS0hbE) | Fairy Door | 1,830 | 273,962 | 149.7 | ×39.6 | 3,227.1 | 196.9분 | 2026-07-29 | 2. 자연 소리·백색소음 | 커버·직접 부른 노래 | 설명 | 26/26 |
| 356 | [바흐의 파사칼리아](https://www.youtube.com/watch?v=MQf3ajxEFfQ) | 홍준 뮤직 TV | 4,490 | 671,032 | 149.4 | ×1,232.4 | 4,960.0 | 40분 | 2026-06-09 | 기타 | 정보·해설 | 설명 | 662/668 |
| 357 | [Happy Morning Jazz 🎶 January Bossa Nova Instrumental and Re…](https://www.youtube.com/watch?v=cwBj4t1V_FY) | Little Masti … | 10,300 | 1,537,451 | 149.3 | ×23.2 | 67,278.3 | 14.5분 | 2026-09-29 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 0/0 |
| 358 | [Coffee Shop Love Songs ∣ Relaxing Acoustic 70s 80s 90s Coll…](https://www.youtube.com/watch?v=p4zynVVTYpA) | Acoustic Memo… | 10,000 | 1,489,437 | 148.9 | ×38.6 | 54,472.5 | 80.3분 | 2026-09-24 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 130/134 |
| 359 | [playlist ∣ 우리 사랑은 필름 같았으면 해요](https://www.youtube.com/watch?v=k8giKQV4a40) | 웨일 | 3,400 | 505,137 | 148.6 | ×30.0 | 3,745.0 | 21.5분 | 2026-06-09 | 기타 | 플레이리스트·모음 | 없음 | 58/58 |
| 360 | [Mind Relaxing Flute Tabla and Sitar ∣ Hindustani Instrument…](https://www.youtube.com/watch?v=ZHwM82TaZFg) | Mystic Sitar | 2,540 | 374,415 | 147.4 | ×199.3 | 2,166.6 | 71.2분 | 2026-05-02 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 87/88 |
| 361 | [A CHATPATI PLAYLIST FOR CHATPATE PEOPLE 💅😜 #playlist #song …](https://www.youtube.com/watch?v=H0yLhDLJWuI) | 𐙚 𝒦𝒽𝓊𝓈𝒽𝒷𝓊𝓊 | 19,500 | 2,873,588 | 147.4 | ×5.6 | 26,897.0 | 11.2분 | 2026-07-07 | 기타 | 플레이리스트·모음 | 설명 | 300/302 |
| 362 | [Nhạc Thiền Tịnh Tâm An Lạc 🌿 Nhạc Thiền Chữa Lành Giúp Thư …](https://www.youtube.com/watch?v=I6stAluj1OI) | Hơi Thở Chánh… | 3,490 | 513,332 | 147.1 | ×539.8 | 2,854.3 | 64.3분 | 2026-04-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 119/119 |
| 363 | [If You Feel It in Your Blood… You’re a Viking ⚔️ ∣ Valhalla…](https://www.youtube.com/watch?v=uPK4MWJvxMk) | Viking Army | 9,580 | 1,406,242 | 146.8 | ×1,407.6 | 7,909.6 | 9.2분 | 2026-04-27 | 13. OST·사운드트랙 | 음악 | 설명 | 587/595 |
| 364 | [Hanuman Chalisa 🔥 Listen Can Change Your Energy ∣ Peace, Po…](https://www.youtube.com/watch?v=v7ezfXE074I) | bhakti offici… | 4,960 | 720,945 | 145.3 | ×1,938.0 | 4,245.9 | 6.7분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 582/584 |
| 365 | [@노노뮤직#피아노연주곡 #플루트연주곡#명상음악 #휴식음악 #뉴에이지 #감성음악 #숲길 #자연음악 #마음치유…](https://www.youtube.com/watch?v=8Fiore1srWM) | 노노스튜디오 | 462 | 67,117 | 145.3 | ×409.2 | 476.2 | 32.1분 | 2026-06-03 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 11/11 |
| 366 | [Sleep & Reset Your Vagus Nerve ∣ Singing Bowl Sound Bath Me…](https://www.youtube.com/watch?v=l91ztcnXYPM) | Echo Bowls | 504 | 73,044 | 144.9 | ×967.5 | 679.0 | 15.3분 | 2026-07-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 13/13 |
| 367 | [POV: You found the ultimate South Indian aesthetic🪷 playlis…](https://www.youtube.com/watch?v=oQz6Wt4qb3w) | Ethereal Echo… | 12,700 | 1,838,383 | 144.8 | ×5.8 | 12,245.9 | 13.3분 | 2026-05-25 | 기타 | 플레이리스트·모음 | 설명 | 356/357 |
| 368 | [𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 ∣ 일할때 틀어놓기 좋은 지브리 x 픽사 x 디즈니 재즈🔥🎺 ∣ #NoAImusic ∣ G…](https://www.youtube.com/watch?v=ayKr-gtJQIQ) | 오늘은 재즈데이 ∣ Ja… | 3,360 | 485,668 | 144.5 | ×472.9 | 3,560.2 | 379.1분 | 2026-06-07 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 40/41 |
| 369 | [Thankful Hearts ∣ Gratitude Sing Along Song with Lyrics 💗](https://www.youtube.com/watch?v=K-c4pzbzBzE) | Purely Positi… | 245 | 35,265 | 143.9 | ×218.4 | 608.9 | 4.5분 | 2026-08-25 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 21/25 |
| 370 | [【靜謐時光】 古箏竹笛療癒音樂｜超好聽的中國古典音樂 古箏、琵琶、竹笛、二胡｜療癒音樂 深度睡眠 - Chinese …](https://www.youtube.com/watch?v=7QV9JIx-euE) | Gentle Zen Me… | 9,590 | 1,379,032 | 143.8 | ×604.6 | 8,791.3 | 232분 | 2026-05-18 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,844/2,877 |
| 371 | [Calm Work Music ∣ Ambient Deep Work for Focus, Productivity…](https://www.youtube.com/watch?v=PBwiQgdwJdc) | Calm Work Stu… | 5,770 | 822,414 | 142.5 | ×243.9 | 7,626.8 | 130.2분 | 2026-07-06 | 3. 공부·집중·작업 | 음악 | 설명 | 202/203 |
| 372 | [지금 다시 들어도 좋은 2000년대 명곡 모음 (SG워너비·티아라·씨야) 🎧 그 시절 우리가 사랑했던 노래…](https://www.youtube.com/watch?v=vBIWuORF8vI) | 그때 그 가락 | 2,450 | 348,160 | 142.1 | ×5.4 | 22,523.6 | 101.5분 | 2026-10-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 40/62 |
| 373 | [Eldorado — Hypnotic Dream Trance & Tribal Ambient Music👑✨](https://www.youtube.com/watch?v=ggbo8YTXRrw) | ARTechnoMusic | 3,810 | 540,130 | 141.8 | ×34.8 | 5,311.9 | 5.8분 | 2026-07-12 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 69/69 |
| 374 | [𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 요즘 인스타 부계 감성](https://www.youtube.com/watch?v=WBabiGZluh8) | 알수없는 사용자 | 1,730 | 244,957 | 141.6 | ×6.8 | 3,192.1 | 17.5분 | 2026-08-06 | 기타 | 플레이리스트·모음 | 설명 | 52/53 |
| 375 | [মন ছুঁয়ে যাওয়া বাংলা Lo-Fi Romantic Songs ∣ Relaxing Bangla…](https://www.youtube.com/watch?v=rwiGXAhqrfU) | RESHMI LO-FI … | 24,000 | 3,389,111 | 141.2 | ×858.7 | 19,919.0 | 22.5분 | 2026-05-05 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 989/990 |
| 376 | [[오마주 OST] 모두가 자신의 무가치함과 싸우고 있다 Inspired Playlist ∣ 포켓라디오 #넷…](https://www.youtube.com/watch?v=CSIUAghSOPo) | pocketradio | 572 | 80,571 | 140.9 | ×257.4 | 449.1 | 16.3분 | 2026-04-25 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 93/93 |
| 377 | [Relaxing Jazz Saxophone instrument Relax & Slow Down 🌿 Soft…](https://www.youtube.com/watch?v=AaXKINtzSGI) | Peaceful Sax … | 13,800 | 1,942,813 | 140.8 | ×633.7 | 13,421.9 | 69.9분 | 2026-05-30 | 7. 재즈·보사노바 | 음악 | 설명 | 394/394 |
| 378 | [자비의 빛, 신묘장구대다라니](https://www.youtube.com/watch?v=oZyrd47zI6o) | 부다야나마하 | 2,860 | 402,359 | 140.7 | ×264.9 | 5,247.0 | 6.6분 | 2026-08-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 228/234 |
| 379 | [Le Café de Minuit 🇫🇷 Une Chanson Romantique Inspirée par le…](https://www.youtube.com/watch?v=D4-ltf3Tdh8) | Bistrot de Mi… | 3,400 | 474,999 | 139.7 | ×1,104.6 | 3,543.7 | 5.9분 | 2026-06-10 | 4. 카페·매장·라운지 | 음악 | 설명 | 101/102 |
| 380 | [Deep Sleep & Chill Lofi : Bhojpuri Slowed & Reverb Songs 🎧✨…](https://www.youtube.com/watch?v=zW8T1B9Fzd0) | VLOGDIPESH | 5,220 | 728,666 | 139.6 | ×4,923.4 | 51,439.2 | 17.1분 | 2026-10-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 33/33 |
| 381 | [[playlist] skrrrr….](https://www.youtube.com/watch?v=20mvF_OP0FY) | le | 12,300 | 1,711,567 | 139.2 | ×39.9 | 9,833.3 | 26.1분 | 2026-05-01 | 기타 | 플레이리스트·모음 | 없음 | 276/283 |
| 382 | [music that will get you to flowstate.](https://www.youtube.com/watch?v=72YoraTjNI0) | Pure Grit Stu… | 20,400 | 2,825,886 | 138.5 | ×135.9 | 27,841.5 | 145.4분 | 2026-07-12 | 기타 | 음악 | 설명 | 1,503/1,508 |
| 383 | [Jo Tere Sang KaTi RaTe 💔 Lofi Remix ∣ Emotional Slowed + Re…](https://www.youtube.com/watch?v=XKcT9t0tgbY) | Abidpro | 46,100 | 6,368,010 | 138.1 | ×1,134.4 | 40,864.5 | 6.3분 | 2026-05-19 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 809/811 |
| 384 | [Positive Jazz Music ☕ Bossa Nova instrumental for Stress Re…](https://www.youtube.com/watch?v=T2HdICk7_6M) | Golden Roast … | 10,900 | 1,499,879 | 137.6 | ×1,227.9 | 10,713.5 | 71.2분 | 2026-06-04 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 235/239 |
| 385 | [Shri Krishna Govind Hare Murari - Non Stop Krishna Bhajans …](https://www.youtube.com/watch?v=yl8by0hGZKE) | Hare Murare M… | 22,600 | 3,102,007 | 137.3 | ×1,016.1 | 21,333.5 | 59.2분 | 2026-05-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 419/423 |
| 386 | [Fall Into Sleep Instantly • Healing Stress, Anxiety, and De…](https://www.youtube.com/watch?v=ZIGKQlrOEV0) | Brainwave Res… | 13,800 | 1,890,676 | 137.0 | ×2,938.1 | 12,987.0 | 480분 | 2026-05-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,028/1,034 |
| 387 | [বিধি এমন ভাগ্য কেন দিলা ∣ Bidhi Amon Vaggo Keno Dila ∣ Bang…](https://www.youtube.com/watch?v=PGkwfiSxmJU) | আঁখি Lo-Fi | 11,400 | 1,559,254 | 136.8 | ×251.1 | 15,484.4 | 13.8분 | 2026-07-13 | 기타 | 음악 | 설명 | 194/194 |
| 388 | [Midnight in Beirut 🌙 ∣ Lebanese Jazz & Oud Melodies for Rel…](https://www.youtube.com/watch?v=pdSDzQVDYXk) | Arabic Jazz L… | 17,600 | 2,401,767 | 136.5 | ×1,123.9 | 13,963.9 | 25.3분 | 2026-05-03 | 3. 공부·집중·작업 | 음악 | 설명 | 767/768 |
| 389 | [Relax in Bikini Bottom 🛟 Calming Tropical Music 🌊 ∣ SpongeB…](https://www.youtube.com/watch?v=US8lFJPAWR0) | Vynture | 4,260 | 579,393 | 136.0 | ×432.9 | 6,394.1 | 249.3분 | 2026-07-23 | 1. 수면·명상·힐링 | 음악 | 설명 | 160/165 |
| 390 | [🎶Mind and body healing Music ∣ Bansuri flute + Esraj ∣ 1 ho…](https://www.youtube.com/watch?v=l1DL2JWYcyA) | Indian-Soulsc… | 279 | 37,589 | 134.7 | ×213.6 | 309.1 | 61.4분 | 2026-06-22 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 10/10 |
| 391 | [[playlist] 내 주위는 온통 lovely day](https://www.youtube.com/watch?v=m-xuokRyfvQ) | 지륭 | 1,210 | 162,765 | 134.5 | ×3.8 | 980.0 | 19.9분 | 2026-05-09 | 기타 | 플레이리스트·모음 | 없음 | 20/20 |
| 392 | [Autumn Morning Jazz In A Cozy Garden Lounge ∣ Gentle Piano …](https://www.youtube.com/watch?v=tiqZDLIBbHg) | Indoor Jazz M… | 5,400 | 722,651 | 133.8 | ×373.8 | 10,643.7 | 207.9분 | 2026-08-15 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 120/120 |
| 393 | [📝 1 HOUR OF FOCUS ∣ 🌧️ Relaxing Piano & Rain Sounds for Stu…](https://www.youtube.com/watch?v=yMcznSINsFs) | Melodies of C… | 4,500 | 600,667 | 133.5 | ×48.2 | 7,073.7 | 60.4분 | 2026-07-29 | 2. 자연 소리·백색소음 | 긴 한 곡·반복 | 설명 | 152/155 |
| 394 | [재생하자마자 텐션 터지는 2026 남녀돌 믹스업 (과제, 청소, 운동할 때 듣는 플리)](https://www.youtube.com/watch?v=x09m3Lgzc-A) | MxJin06 | 5,040 | 672,682 | 133.5 | ×10.2 | 8,105.7 | 99.2분 | 2026-07-31 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 없음 | 30/30 |
| 395 | [Deep Focus Music – Flow State for Study & Work](https://www.youtube.com/watch?v=9xYZzgG2EuI) | Deep365 | 4,180 | 557,546 | 133.4 | ×138.6 | 5,223.0 | 63.7분 | 2026-07-07 | 3. 공부·집중·작업 | 음악 | 설명 | 150/150 |
| 396 | [Bangla Old Is Gold Romantic Song ∣ Bangla Lo-Fi ∣ 1970-1990…](https://www.youtube.com/watch?v=OP2DddRRTKI) | Moner Tune | 24,300 | 3,239,860 | 133.3 | ×251.2 | 22,856.3 | 15.8분 | 2026-06-02 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 313/314 |
| 397 | [99% Fall Into Sleep Instantly (No Ads) • Eliminate Stress &…](https://www.youtube.com/watch?v=iVZPLhAlXUw) | Bedtime Calm … | 12,200 | 1,625,035 | 133.2 | ×251.0 | 31,478.1 | 237.9분 | 2026-08-31 | 1. 수면·명상·힐링 | 음악 | 설명 | 43/43 |
| 398 | [💖💖💖The Café by the Sea©](https://www.youtube.com/watch?v=7jPXHB9Ohus) | M's Music Lou… | 2,070 | 274,647 | 132.7 | ×771.5 | 2,200.3 | 4.2분 | 2026-06-19 | 4. 카페·매장·라운지 | 음악 | 설명 | 195/198 |
| 399 | [Sholey Title Music ∣ Music Maker Abani ∣ Instrumental Cover](https://www.youtube.com/watch?v=ajRxp64xcN8) | MUSIC MAKER A… | 5,850 | 775,285 | 132.5 | – | 6,588.1 | 4.7분 | 2026-06-26 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 1,423/1,433 |
| 400 | [김상민 – YOU (2001) ∣ 폭발적인 고음의 여자 보컬 리메이크/커버 2 Keys+](https://www.youtube.com/watch?v=-GVdD_Onszw) | AuraAPT | 13,100 | 1,731,999 | 132.2 | ×99.5 | 19,938.7 | 4.1분 | 2026-07-27 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 269/284 |
| 401 | [Hanuman Chalisa for Deep Sleep ∣ Divine Protection for Peac…](https://www.youtube.com/watch?v=XKK7ewgprws) | Inner Bhakti | 7,180 | 947,799 | 132.0 | – | 9,794.6 | 114.8분 | 2026-07-17 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 156/158 |
| 402 | [choose peace](https://www.youtube.com/watch?v=eIY-Pgg-b1E) | sleepwalker | 14,200 | 1,873,757 | 131.9 | ×165.7 | 10,907.2 | 60분 | 2026-05-03 | 기타 | 긴 한 곡·반복 | 설명 | 1,135/1,141 |
| 403 | [Cortisol Reset । 432Hz Krishna Bansuri Therapy for a Calm M…](https://www.youtube.com/watch?v=D5NHvEVAbWY) | Healing Raga … | 23,700 | 3,113,886 | 131.4 | ×220.9 | 32,824.8 | 65.7분 | 2026-07-19 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,970/1,999 |
| 404 | [Playlist ∣ 틀어놓으면 그냥 계속 리듬 타게 되는 그루브 😎 집중 끊기지 않는 리듬 🎧 ∣ JAZZ…](https://www.youtube.com/watch?v=wsB8ej3Jon4) | Hush Chords | 19,500 | 2,560,566 | 131.3 | ×498.6 | 15,573.8 | 318.1분 | 2026-05-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 722/725 |
| 405 | [𝙿𝚕𝚊𝚢𝚕𝚒𝚜𝚝 중국 가오 노래들](https://www.youtube.com/watch?v=-h0dUUluarY) | 진구달려 | 5,710 | 748,833 | 131.1 | ×14.9 | 15,822.9 | 14.1분 | 2026-09-05 | 기타 | 플레이리스트·모음 | 없음 | 225/257 |
| 406 | [[空靈鼓療癒音樂🎶]｜放鬆、舒壓、冥想、安眠｜Steel Tongue Drum Healing Music｜SUNO…](https://www.youtube.com/watch?v=a_8Hi2u43Q4) | AIMF Music Fa… | 1,250 | 163,880 | 131.1 | ×969.7 | 1,220.3 | 93.1분 | 2026-06-10 | 1. 수면·명상·힐링 | AI 음악 | 설명 | 12/12 |
| 407 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 듣자마자 텐션 업🔥K-POP 여돌 노래 모음 노동요](https://www.youtube.com/watch?v=xtfreKB54KQ) | 클로버 플레이리스트 | 3,580 | 467,749 | 130.7 | ×6.7 | 4,086.7 | 53분 | 2026-06-29 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 39/39 |
| 408 | [hard work pays off, let's be productive (focus playlist to …](https://www.youtube.com/watch?v=IS6yiMGlYkE) | taami study. | 9,660 | 1,254,169 | 129.8 | ×151.5 | 11,850.5 | 189.8분 | 2026-07-08 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 196/198 |
| 409 | [Best Morning Powerful Mantras ∣ Shiva, Ganesh, Hanuman, Vis…](https://www.youtube.com/watch?v=CFV27iuas7Q) | Sacred Naad | 22,300 | 2,856,394 | 128.1 | ×3,517.7 | 41,223.2 | 15.7분 | 2026-08-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 973/1,034 |
| 410 | [TANGGAL STRESS MO DITO 🔥🎶 ∣ DUB REGGAE MIX 🎶🔥🇵🇭](https://www.youtube.com/watch?v=0m7BLfBl2f8) | RELAX REGGAE … | 13,800 | 1,766,286 | 128.0 | ×1,956.0 | 23,855.6 | 74.8분 | 2026-08-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 256/261 |
| 411 | [Không Buông x Từng Là Của Nhau x Tìm Em - HNGLE x BẢO ANH ∣…](https://www.youtube.com/watch?v=wVLhvXB2flE) | Chà Là Chill | 38,900 | 4,959,526 | 127.5 | ×39.9 | 52,788.9 | 91.8분 | 2026-07-20 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 609/614 |
| 412 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 비에 젖은 와인향](https://www.youtube.com/watch?v=Pt3nGKCTF2U) | 유월 | 3,770 | 479,340 | 127.2 | ×13.8 | 3,355.0 | 21.1분 | 2026-06-01 | 기타 | 플레이리스트·모음 | 설명 | 124/124 |
| 413 | [🎵 전체듣기 ∣ 에헤야~ 막걸리 한 잔 하세 🍶 ∣힐링 국악](https://www.youtube.com/watch?v=KYXF2WEd2Ew) | 에헤라디여 5060 | 357 | 44,809 | 125.5 | ×119.8 | 322.7 | 4.2분 | 2026-06-05 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 30/30 |
| 414 | [당신의 피아노 레벨은? (Lv.1~Lv.8 + 라캄파넬라) ∣ What is your Piano Level…](https://www.youtube.com/watch?v=1E5Zi3Gs1ys) | Bony_Musician | 674 | 84,463 | 125.3 | – | 611.8 | 6.5분 | 2026-06-06 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 340/340 |
| 415 | [Happy Jazz Music ☕ Bossa Nova background for Relaxing, Grea…](https://www.youtube.com/watch?v=YTpDlQvvT3Q) | Golden Roast … | 10,900 | 1,354,226 | 124.2 | ×1,108.7 | 8,338.0 | 70.6분 | 2026-05-12 | 7. 재즈·보사노바 | 음악 | 설명 | 189/193 |
| 416 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 그냥 네 눈동자가 예뻤어](https://www.youtube.com/watch?v=FOjiqNxjDDw) | 유월 | 3,770 | 466,094 | 123.6 | ×13.4 | 2,971.9 | 21.9분 | 2026-05-18 | 기타 | 플레이리스트·모음 | 설명 | 67/67 |
| 417 | [Without You Lord, I Am Nothing ∣ Inspirational Christian Wo…](https://www.youtube.com/watch?v=4TI0GkgfvKk) | Music of Faith | 28,000 | 3,447,955 | 123.1 | ×718.9 | 22,151.1 | 6분 | 2026-05-19 | 15. CCM·찬양·국악… | 음악 | 설명 | 2,138/2,153 |
| 418 | [듣자 마자 바로 잠드는 숲속 시원한 빗소리 ASMR (Rain Sounds), 불면증 완화, 힐링 빗소리](https://www.youtube.com/watch?v=berSZ8YAKP8) | Cozy Rain on … | 3,290 | 404,572 | 123.0 | ×89.5 | 2,852.7 | 180분 | 2026-06-02 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 144/144 |
| 419 | [NAAD ∣ Powerful Instrumental Invocation #SpiritualMusic #Dr…](https://www.youtube.com/watch?v=bc4vTfxeLZk) | shivam sarasw… | 3,380 | 415,570 | 123.0 | ×1,505.7 | 2,860.7 | 7.9분 | 2026-05-30 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 60/60 |
| 420 | [Dragon Ball GT Celtic Fantasy Music ∣ Relax Music for Focus…](https://www.youtube.com/watch?v=fJ6rnqkvyCk) | Medieval Echo… | 1,190 | 145,767 | 122.5 | ×571.6 | 815.6 | 9분 | 2026-04-26 | 3. 공부·집중·작업 | 음악 | 설명 | 202/202 |
| 421 | [My Soundscape for Sleeping at the Edge of the Universe](https://www.youtube.com/watch?v=fsxvm6W4EoY) | Polarity Ambi… | 8,820 | 1,078,418 | 122.3 | ×151.4 | 9,933.2 | 35.9분 | 2026-07-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 884/895 |
| 422 | [Nhạc không lời Piano & Mưa Vol.1 ∣ Piano Thư Giãn, Học Bài,…](https://www.youtube.com/watch?v=tddKxQYCNlM) | Trí Nhật Piano | 8,640 | 1,037,374 | 120.1 | ×359.1 | 6,488.7 | 123분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 250/251 |
| 423 | [Sarap Sa Tenga To VOL. 3 🌿(IBA TO!) ∣ Spiritual Roots Regga…](https://www.youtube.com/watch?v=9w_QNH2ju3A) | Just Reggae S… | 45,800 | 5,423,189 | 118.4 | ×275.3 | 33,076.9 | 64.6분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,674/2,675 |
| 424 | [Relax Your Mind with Tabla & Bansuri Meditation Music ∣ Dee…](https://www.youtube.com/watch?v=OU-pcEjsoxs) | Raga Instrume… | 3,750 | 443,587 | 118.3 | ×2,721.4 | 2,707.7 | 93.3분 | 2026-05-11 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 138/138 |
| 425 | [쇼팽, 첼로로 물들다 ∣ 피아노와 첼로로 듣는 녹턴의 밤 (Chopin for Cello & Piano)](https://www.youtube.com/watch?v=HV7WBsQq-Ms) | EmberClassic | 4,830 | 569,336 | 117.9 | ×96.3 | 6,083.8 | 71.3분 | 2026-07-20 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 170/171 |
| 426 | [The Most Trending OPM Acoustic Songs on Spotify 2026 ✨ ∣ Vi…](https://www.youtube.com/watch?v=MbnaF3T2450) | Calm Guitar | 11,600 | 1,362,802 | 117.5 | ×66.0 | 18,830.0 | 63.8분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 121/123 |
| 427 | [Music to Rest Your Mind.](https://www.youtube.com/watch?v=-igpcHqULS0) | dark serenity… | 6,690 | 784,266 | 117.2 | ×95.3 | 4,846.2 | 57.3분 | 2026-05-13 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 241/245 |
| 428 | [⟨𝐜𝐚𝐟𝐞 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓⟩🩵맑은 초여름의 어느 날, 카페 피아노 10시간 [중간광고없음] ∣ 작업·공부·…](https://www.youtube.com/watch?v=nm_Mh-VIWvY) | Daily BGM plus | 1,350 | 157,888 | 117.0 | ×17.8 | 1,078.7 | 602.7분 | 2026-05-28 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 27/27 |
| 429 | [Dark Jazz Noir for Deep Focus, Work & Night Study ∣ Floatin…](https://www.youtube.com/watch?v=eFl7QIAYHHw) | What can I ge… | 12,600 | 1,468,269 | 116.5 | ×57.7 | 16,068.8 | 32분 | 2026-07-22 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 272/276 |
| 430 | [RUMI ∣ If You Want to Let Go of the Pain, Listen to This ∣ …](https://www.youtube.com/watch?v=p4VN5_1HW20) | Rumi Mystic S… | 1,440 | 167,728 | 116.5 | ×85.7 | 3,596.6 | 26.1분 | 2026-09-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 56/69 |
| 431 | [Greatest Classic Reggae Old Songs 70s-90s 🌴 RIVERS OF BABYL…](https://www.youtube.com/watch?v=1MPtYI4ExEo) | Zee | 11,600 | 1,341,568 | 115.7 | ×153.1 | 19,052.1 | 57.4분 | 2026-08-12 | 12. 커버·노래 부르기 | 플레이리스트·모음 | 설명 | 129/131 |
| 432 | [Dopamine Music 🎶 Peaceful Bansuri & Tabla Instrumental ∣ Me…](https://www.youtube.com/watch?v=6HPjmWDf0Q8) | KrishxBeats | 11,700 | 1,348,991 | 115.3 | ×672.5 | 18,059.5 | 27.9분 | 2026-08-08 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 646/654 |
| 433 | [{playlist} 할렐야루한 노래만 갖고옴...](https://www.youtube.com/watch?v=cnBMqI-z8q8) | 밤티플리 | 1,280 | 147,568 | 115.3 | ×27.3 | 1,019.1 | 18.8분 | 2026-05-30 | 기타 | 플레이리스트·모음 | 없음 | 30/30 |
| 434 | [【心整うBGM】聴くだけで疲れた一日がふっと和らぐ音楽✨｜心ほどけるピアノ２時間🌙｜作業,読書,睡眠用 / Sooth…](https://www.youtube.com/watch?v=-MEjaHzrcuU) | Kigokoro Café… | 6,480 | 737,430 | 113.8 | ×267.8 | 4,764.4 | 132.3분 | 2026-05-20 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 102/102 |
| 435 | [Painful - Emotional Cinematic Storytelling Music ∣ Orchestr…](https://www.youtube.com/watch?v=yk_jaCUz91M) | BynD Epic | 1,210 | 136,425 | 112.8 | ×75.6 | 976.4 | 4.9분 | 2026-06-04 | 13. OST·사운드트랙 | 음악 | 설명 | 64/64 |
| 436 | [🌸New Trending Acoustic Love Songs 2026 Cover🎧Best Trending …](https://www.youtube.com/watch?v=58xMPYKYcPg) | Calm Strings | 7,090 | 797,117 | 112.4 | ×78.3 | 8,629.2 | 49.7분 | 2026-07-21 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 103/103 |
| 437 | [Kabhi Shaam Dhale ∣ Romantic Recreated Version ∣ Soulful Hi…](https://www.youtube.com/watch?v=jHw-Ivg2bLc) | Deepak Pandey | 39,000 | 4,382,318 | 112.4 | ×781.0 | 25,214.5 | 4.7분 | 2026-05-01 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 449/455 |
| 438 | [If You Feel Stressed, Listen to This ∣ Deep Sufi Healing Mu…](https://www.youtube.com/watch?v=tGNczX2LApU) | Rumi Mystic S… | 1,440 | 161,254 | 112.0 | ×82.4 | 3,637.4 | 30.2분 | 2026-09-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 25/26 |
| 439 | [[𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩]🔥달려보자 2010년 아이돌 띵곡 노동요 모음.zip 플레이리스트💿](https://www.youtube.com/watch?v=_zFB1047_Ek) | 이꿈치 | 1,330 | 148,522 | 111.7 | ×4.4 | 1,725.3 | 73.5분 | 2026-07-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 20/20 |
| 440 | [Tomay Pelam Elo Mone ∣ তোমায় পেলাম এলো মনে হাজার আলোর বন্য…](https://www.youtube.com/watch?v=rPi4ScyrzIM) | Sudip Lo-Fi M… | 20,100 | 2,239,821 | 111.4 | ×2,429.3 | 12,961.6 | 4.3분 | 2026-05-02 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 165/169 |
| 441 | [🌧️ (No Ads) Real Heavy Rain & Powerful Thunderstorm ⛈️ ∣ De…](https://www.youtube.com/watch?v=tAd_vs_Ej_I) | Rain Drop's | 7,790 | 856,935 | 110.0 | ×23.0 | 10,153.9 | 95.1분 | 2026-07-29 | 2. 자연 소리·백색소음 | 음악 | 설명 | 287/290 |
| 442 | [ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ](https://www.youtube.com/watch?v=MsjHOAq7WH0) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 14,700 | 1,613,381 | 109.8 | ×329.6 | 31,713.2 | 67.7분 | 2026-09-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,119/1,122 |
| 443 | [나무에 내리는 부드러운 빗소리/ 듣자마자 기절수면 나무 빗소리/ 이명 치료 효과/ 빗소리 1시간/ 5분후 …](https://www.youtube.com/watch?v=otpGN7l-8mo) | 아늑한 빗소리 - Coz… | 4,200 | 460,754 | 109.7 | ×45.8 | 5,623.3 | 64분 | 2026-08-01 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 34/34 |
| 444 | [Pokémon Café Jazz Lofi ∣ ☕ Smooth Beats for Study & Focus S…](https://www.youtube.com/watch?v=t6yrxjE7HSM) | Rest Point Lo… | 4,080 | 446,111 | 109.3 | ×73.2 | 2,564.1 | 104.2분 | 2026-05-01 | 3. 공부·집중·작업 | 음악 | 설명 | 74/76 |
| 445 | [임영웅 콘서트 명곡 22곡 모음 💙 가장 사랑받는 감성 트로트·추억 발라드 연속듣기 #임영웅 #임영웅노래모…](https://www.youtube.com/watch?v=532qBV3Bs9o) | 별빛 영웅 뮤직 | 2,920 | 319,118 | 109.3 | ×1,619.9 | 2,812.7 | 75.3분 | 2026-06-30 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 113/114 |
| 446 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 라흐마니노프 - 지독한 슬픔 끝에 피어난 환희에 대하여ㅣRachmaninoff Style](https://www.youtube.com/watch?v=w5nhvxPli3E) | Moonlight Cla… | 8,360 | 910,282 | 108.9 | ×769.5 | 9,641.2 | 180분 | 2026-07-19 | 기타 | 플레이리스트·모음 | 설명 | 791/813 |
| 447 | [Darmiyaan - Unplugged](https://www.youtube.com/watch?v=f5vaem1fvGk) | Raghav Kaushi… | 9,810 | 1,063,738 | 108.4 | – | 11,993.0 | 5분 | 2026-07-25 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/29 |
| 448 | [🎻 바흐에게서 영감을 받은 바로크 듀엣 – 첼로와 오보에](https://www.youtube.com/watch?v=NxDxvXUWyFQ) | yoon acacia | 1,690 | 182,681 | 108.1 | ×308.1 | 2,263.5 | 69.7분 | 2026-08-02 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 35/35 |
| 449 | [💖신나게 미친(positive) 최신 걸그룹 노래 모음 ∣ 최신 여자아이돌 플레이리스트 [ Girl Gro…](https://www.youtube.com/watch?v=PiKPf0T7I84) | 띠잉뮤직 | 20,900 | 2,244,580 | 107.4 | ×189.5 | 13,250.6 | 120.5분 | 2026-05-05 | 기타 | 플레이리스트·모음 | 설명 | 270/270 |
| 450 | [Anirudh's new 2026 Mass songs ∣ Best Anirudh Songs #trending](https://www.youtube.com/watch?v=NV2bXZ4H4gA) | Musical Haven | 2,090 | 224,180 | 107.3 | – | 1,755.3 | 16.7분 | 2026-06-16 | 기타 | 음악 | 설명 | 15/16 |
| 451 | [Soft Acoustic Playlist 🎵 ∣ Best Relax & Chill Vibes Songs 2…](https://www.youtube.com/watch?v=MPT9v9MIod0) | Cozy Strings | 9,610 | 1,022,117 | 106.4 | ×338.8 | 6,601.4 | 69.8분 | 2026-05-20 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 84/84 |
| 452 | [Romantic Instrumental Playlist 💖 ∣ Saxophone & Flute Love M…](https://www.youtube.com/watch?v=dHqp0WOzSns) | Video Music S… | 6,080 | 645,090 | 106.1 | ×29.2 | 6,455.0 | 13.3분 | 2026-07-14 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 34/35 |
| 453 | [99% DEEP SLEEP in 3 Minutes (NO ADS) • Relieves Stress • In…](https://www.youtube.com/watch?v=E0hQGUOAhrQ) | Fall Asleep S… | 9,540 | 1,008,974 | 105.8 | ×103.1 | 13,566.8 | 116.9분 | 2026-08-08 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 281/284 |
| 454 | [Sera Se Cosera - One Name (Extended) ∣ Jailer 2 BGM ∣ Super…](https://www.youtube.com/watch?v=0EcRBvWCmhQ) | JB RagaMix | 16,400 | 1,727,124 | 105.3 | ×21.5 | 15,838.0 | 5분 | 2026-07-05 | 기타 | 음악 | 설명 | 324/335 |
| 455 | [(BGM) 432Hz Ultimate Healing Music ∣ Alpha Wave for Body an…](https://www.youtube.com/watch?v=3odCe4Ry-EY) | Serenę Sound | 6,880 | 720,417 | 104.7 | ×782.2 | 4,458.5 | 73.5분 | 2026-05-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 228/229 |
| 456 | [🌿 Возвращение к себе ∣ Музыка покоя 💦 Вода и тибетские чаши…](https://www.youtube.com/watch?v=eFje9j9VLZ0) | МУДРЫЕ МЕДИТА… | 6,810 | 703,854 | 103.4 | ×13.3 | 6,033.1 | 30.1분 | 2026-06-27 | 1. 수면·명상·힐링 | 음악 | 설명 | 162/163 |
| 457 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=ca4K-2vlfvA) | KKR rahul 09 | 16,000 | 1,645,781 | 102.9 | ×614.4 | 58,167.8 | 18.2분 | 2026-09-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 69/71 |
| 458 | [Quiet Night Playlist 🌙 ∣ Soft Love Songs for Deep Feelings …](https://www.youtube.com/watch?v=EvU4QgmjhMY) | Cozy Strings | 9,610 | 987,755 | 102.8 | ×327.4 | 7,114.7 | 134.1분 | 2026-06-05 | 기타 | 플레이리스트·모음 | 설명 | 162/165 |
| 459 | [옛날 시골집 슬레이트 빗소리ㅣ고향의 향수ㅣ추억ㅣ수면유도](https://www.youtube.com/watch?v=IHYnumQGS2o) | 빗소리 Healing S… | 1,350 | 138,708 | 102.8 | ×49.6 | 996.6 | 300분 | 2026-06-05 | 1. 수면·명상·힐링 | 자연 소리·백색소음 | 설명 | 47/47 |
| 460 | [Beautiful Sad Love Songs 2026 English Love Songs Playlist M…](https://www.youtube.com/watch?v=vKMy_Q_1wbc) | MusicLouds | 24,700 | 2,530,915 | 102.5 | ×1,763.1 | 14,833.6 | 71.4분 | 2026-05-04 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 870/876 |
| 461 | [Summer Deep House Mix 2026 ∣ Luxury Chillout Lounge Music f…](https://www.youtube.com/watch?v=ZZjKsakgbgw) | Surfboard Dee… | 5,770 | 588,791 | 102.0 | ×507.1 | 3,805.9 | 65.2분 | 2026-05-20 | 4. 카페·매장·라운지 | 음악 | 설명 | 248/251 |
| 462 | [Waheguru Jaap Before Sleep 🌙 Relaxing Meditation Kids, Babi…](https://www.youtube.com/watch?v=gT1SH3nqnuw) | Nanak Naam Ch… | 348 | 35,469 | 101.9 | – | 250.0 | 10.2분 | 2026-06-02 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 33/33 |
| 463 | [[Playlist] 조용히 혼자 듣고 싶다… 천상의 감성 보이스 7080 올드팝 🎧 ∣ 카페·휴식·감성 B…](https://www.youtube.com/watch?v=HBx4T1dadhI) | TrueOldies 70… | 5,550 | 564,867 | 101.8 | ×227.2 | 3,661.5 | 140.2분 | 2026-05-21 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 346/348 |
| 464 | [힐링음악 ∣ 쉬어 가도 괜찮아 (It’s Okay to Rest) ∣ 지친 마음을 쉬게 하는 국악 힙합 ∣…](https://www.youtube.com/watch?v=OTmG9c33c1M) | 풍그루 | 598 | 60,321 | 100.9 | ×19.8 | 700.7 | 5.1분 | 2026-07-28 | 1. 수면·명상·힐링 | 한 곡 | 설명 | 10/10 |
| 465 | [​🎧 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 아무 걱정 없이 쉬고 싶은 날, 편안하고 아늑한 어쿠스틱 빈티지 재즈](https://www.youtube.com/watch?v=Py3IKxJcbAA) | MONA mood | 9,840 | 978,833 | 99.5 | ×40.7 | 9,205.4 | 84.4분 | 2026-07-08 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 94/95 |
| 466 | [CHÌM VÀO GIẤC NGỦ SAY - Nhạc Lofi Chill Nhẹ Nhàng Thư Giãn …](https://www.youtube.com/watch?v=PJGgU7H4ruA) | Xóm Chill | 6,220 | 616,173 | 99.1 | ×143.4 | 8,129.9 | 156.2분 | 2026-08-07 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 82/82 |
| 467 | [If You Are Fall In Love Then Listen Romantic Indian Instrum…](https://www.youtube.com/watch?v=rCFoSTwT1GU) | Veena Meditat… | 2,390 | 236,458 | 98.9 | ×737.8 | 2,034.4 | 81.8분 | 2026-06-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 26/26 |
| 468 | [[Playlist] 만약에 그날, 널 붙잡았다면│감성 발라드 플리](https://www.youtube.com/watch?v=KtjdGajPw_8) | 심야플리 | 2,310 | 227,711 | 98.6 | ×51.8 | 1,287.7 | 67.3분 | 2026-04-28 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 179/179 |
| 469 | [Silver Moon — Hypnotic Vocal Ambient (Enigma & Schiller Sty…](https://www.youtube.com/watch?v=hJd8GIUEOog) | ARTechnoMusic | 3,810 | 374,162 | 98.2 | ×24.1 | 3,265.3 | 6분 | 2026-06-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 114/119 |
| 470 | [Mere Mehboob Qayamat Hogi ✨ ∣ Slowed Reverb + LoFi ∣ Sad Hi…](https://www.youtube.com/watch?v=AHo0xW8RYTQ) | Abidpro | 46,100 | 4,481,863 | 97.2 | ×798.4 | 28,970.9 | 9.4분 | 2026-05-20 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 350/350 |
| 471 | [Classic Rock Songs 70's 80's 90's Playlist 🔥 Guns N Roses, …](https://www.youtube.com/watch?v=erfv9QasZAw) | 80s90s Rock R… | 21,800 | 2,112,805 | 96.9 | ×4,829.3 | 25,818.7 | 106.5분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 설명 | 171/178 |
| 472 | [Dear God, Can You Hear Me ? - Ethereal Celtic ambient Track…](https://www.youtube.com/watch?v=7c2GwOr5NGc) | Dreamstatic E… | 4,120 | 398,004 | 96.6 | ×212.2 | 3,001.6 | 7분 | 2026-06-11 | 14. AI 음악 | AI 음악 | 설명 | 584/587 |
| 473 | [Ganga Dharaye Shiv 🙏 ∣ Om Namah Shivaya ∣ Powerful Shiva Bh…](https://www.youtube.com/watch?v=FTzC_e5FQZA) | Spiritual Tun… | 29,200 | 2,816,911 | 96.5 | ×7,007.2 | 15,886.8 | 66.4분 | 2026-04-28 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 492/494 |
| 474 | [신나는 뽕짝·트로트 14곡 연속듣기 🎵 관광버스 필수곡 ∣ 신나는 뽕짝 메들리 ∣ 고속도로 트롯 BEST](https://www.youtube.com/watch?v=LxWOrfUcQlY) | 뽕친놈 | 4,710 | 446,707 | 94.8 | ×162.4 | 4,347.6 | 50.7분 | 2026-07-11 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 77/79 |
| 475 | [Healing Music for Anxiety, Fears and Depression 🌿 Heals the…](https://www.youtube.com/watch?v=AcfJRtYtSZU) | Nature Aura | 3,940 | 373,288 | 94.7 | ×303.2 | 5,580.2 | 105.2분 | 2026-08-16 | 1. 수면·명상·힐링 | 음악 | 설명 | 32/34 |
| 476 | [Kur pata një lule t'bukur Alb Smooth Cover](https://www.youtube.com/watch?v=GES0QOroepY) | Alb Smooth Ca… | 4,990 | 470,510 | 94.3 | ×14.1 | 2,615.2 | 4.9분 | 2026-04-25 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 116/116 |
| 477 | [Playlist l 우리는 너무 어렸고 서툴렀다, 가사없는음악](https://www.youtube.com/watch?v=DN0T_nrFf6o) | Freemu 프리뮤 | 3,610 | 339,237 | 94.0 | ×939.7 | 5,080.7 | 60.2분 | 2026-08-16 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 56/59 |
| 478 | [회심곡(回心曲) - 쉬운 우리말로 풀어낸 한마음 회심곡, 불교음악, 부모은중경,부모은혜 ,인생무상 , 나무…](https://www.youtube.com/watch?v=0_QIhEcEiq0) | Dragonsong | 593 | 55,699 | 93.9 | ×55.3 | 895.8 | 7.5분 | 2026-08-21 | 기타 | 음악 | 설명 | 39/43 |
| 479 | [Vivaldi x Paganini x Bach Inspired 🎻 Fast & Relaxing Violin…](https://www.youtube.com/watch?v=0Jdy1C_QqvE) | Classical Vio… | 24,600 | 2,306,171 | 93.8 | ×2,888.1 | 15,551.7 | 74.7분 | 2026-05-27 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,656/1,673 |
| 480 | [All RED EVIL JACK MUSIC REJ儀式付【作業用/For work】](https://www.youtube.com/watch?v=_QAOzonmqh8) | イヴch🍳🥚 | 2,450 | 229,516 | 93.7 | – | 2,954.4 | 11.8분 | 2026-08-05 | 기타 | 음악 | 없음 | 132/137 |
| 481 | [Playlist ✍️집중력 1등 공부 플레이리스트 BGM ∣ 공부할때 듣기 좋은 음악🎧 focus&stud…](https://www.youtube.com/watch?v=wouMGz1k7K8) | obne music 오브… | 7,110 | 665,979 | 93.7 | ×91.3 | 11,130.7 | 122.1분 | 2026-08-23 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 49/54 |
| 482 | [#나는너를 - #장현 (1974년) Covered by sMUSIC #7080가요명곡 #리메이크명곡](https://www.youtube.com/watch?v=3F3vaZpv1ik) | sMusic 7080_명… | 6,860 | 640,244 | 93.3 | ×242.9 | 4,324.4 | 4.5분 | 2026-05-27 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 없음 | 80/80 |
| 483 | [Sunrise Serenity ∣ Raag Ahir Bhairav inspired Music with bi…](https://www.youtube.com/watch?v=LLFxvwEOEGs) | Music for Life | 6,120 | 564,215 | 92.2 | ×351.1 | 4,080.2 | 40.2분 | 2026-06-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 259/267 |
| 484 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 틀자마자 시원해지는 당도보장 여름플리🩵(중간광고❌) Feel Good Chill Pop🎧카…](https://www.youtube.com/watch?v=t1i4n4SvtkE) | OurmuseMusic | 848 | 78,071 | 92.1 | ×24.0 | 612.7 | 607.7분 | 2026-06-16 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 68/68 |
| 485 | [Cheema Y Best Songs Playlist ∣ Punjabi Hits 2026 ∣ Jukebox …](https://www.youtube.com/watch?v=LFpVqIlmn00) | Radio Level L… | 37,900 | 3,475,020 | 91.7 | – | 30,207.7 | 27.9분 | 2026-06-29 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,003/1,032 |
| 486 | [10 Minutes Deep Meditation Music for Positive Energy • Free…](https://www.youtube.com/watch?v=PtUp1X2POmU) | TRUEMÖ Musics | 296 | 27,139 | 91.7 | ×512.1 | 1,442.7 | 10.1분 | 2026-10-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 1/1 |
| 487 | [Viral Chill Songs Playlist 2026🔥I MidnightVibes ∣ Non-Stop …](https://www.youtube.com/watch?v=SNx32obvuEk) | Viralics | 8,770 | 804,048 | 91.7 | ×60.3 | 5,049.7 | 17.1분 | 2026-05-16 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 116/116 |
| 488 | [The Calm After the Storm - Classical Music for Emotional He…](https://www.youtube.com/watch?v=AkVSmWxf6WA) | Reverie Class… | 8,340 | 764,492 | 91.7 | ×418.2 | 9,342.1 | 57.2분 | 2026-08-01 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 401/417 |
| 489 | [🎧 2000s Nostalgia Mashup ∣ Tu Tu Hai Wahi (BGM) x Mujhse Mo…](https://www.youtube.com/watch?v=0K8bNaPHiWk) | VibesWithAni | 3,250 | 297,868 | 91.7 | ×4,137.1 | 4,901.0 | 6.5분 | 2026-08-22 | 기타 | 음악 | 설명 | 66/67 |
| 490 | [PIANO INSTRUMENTAL PARA ORAR - TU FIDELIDAD - FONDO MUSICAL](https://www.youtube.com/watch?v=SADBZgzxwo0) | Sonido Del Ci… | 1,240 | 113,610 | 91.6 | ×159.6 | 637.4 | 14.4분 | 2026-04-27 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 5/5 |
| 491 | [life](https://www.youtube.com/watch?v=8TjeO3AFTbM) | sleepwalker | 14,200 | 1,300,770 | 91.6 | ×115.0 | 8,095.6 | 60분 | 2026-05-14 | 기타 | 긴 한 곡·반복 | 설명 | 970/979 |
| 492 | [Patar Bashori 🥀 ∣ পাতার বাঁশরী ∣ Female Version ∣ Bangla No…](https://www.youtube.com/watch?v=kQ3IwNRzLMM) | Lofix Dj Fusi… | 31,100 | 2,843,418 | 91.4 | ×2,605.1 | 34,275.7 | 18.4분 | 2026-07-31 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 976/1,006 |
| 493 | [endless dream](https://www.youtube.com/watch?v=g33LSGLwLzo) | TaTa_Chan | 22,100 | 2,018,969 | 91.4 | ×268.7 | 14,344.4 | 165.3분 | 2026-06-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,317/2,373 |
| 494 | [Saxophone Instrumental Love Songs 🎷 Timeless Romantic Hits …](https://www.youtube.com/watch?v=y8IS36i_yOc) | MEMORIES PATH | 5,980 | 545,736 | 91.3 | ×432.8 | 5,638.0 | 56분 | 2026-07-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 109/112 |
| 495 | [Summer Café Bleu Lounge ∣ Luxury Originals](https://www.youtube.com/watch?v=_nmkwn2A8GI) | DeluxeChill | 7,030 | 640,815 | 91.2 | ×156.7 | 3,944.7 | 65.8분 | 2026-05-12 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 199/202 |
| 496 | [Relaxing Meditation Music & Waterfall Sounds 🌿Calm, Deep Sl…](https://www.youtube.com/watch?v=gfulfnnJ3lY) | Celestial Rel… | 11,400 | 1,034,935 | 90.8 | ×318.2 | 18,853.0 | 126.5분 | 2026-08-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 116/117 |
| 497 | [Indian Instrumental Fusion Music 🎶 Flute, Tabla, Veena & Si…](https://www.youtube.com/watch?v=646h8c7sUSw) | FLUTE TABLA A… | 6,030 | 546,049 | 90.6 | ×557.5 | 3,688.3 | 18.1분 | 2026-05-27 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 153/154 |
| 498 | ["सुकून भरी रातें 🌙 ∣ Romantic Hindi LoFi Songs ∣ Relaxing S…](https://www.youtube.com/watch?v=DU0Swx5GKB4) | Hindi Tuning | 25,200 | 2,279,766 | 90.5 | ×317.8 | 82,466.5 | 104분 | 2026-09-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 61/83 |
| 499 | [Lullaby for Babies 💤 Sleep instantly in 3 minutes ♥ Sleep m…](https://www.youtube.com/watch?v=BUvu6tA9VTM) | Starfish and … | 7,970 | 717,154 | 90.0 | ×160.4 | 4,310.5 | 123.9분 | 2026-05-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 500 | [🔥 JOSHHH BOOSTING BOLLYWOOD SONGS 🎧 ∣ Study Motivation Play…](https://www.youtube.com/watch?v=5BLt-lBa0gQ) | Echoess of un… | 6,140 | 551,272 | 89.8 | ×3.2 | 3,809.8 | 6.9분 | 2026-05-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 217/219 |
| 501 | [7 Pieces by Hans Zimmer \\ Iconic Soundtracks \\ Relaxing P…](https://www.youtube.com/watch?v=28vfE8VR2aE) | Yurii Salukha | 5,880 | 524,225 | 89.2 | ×399.3 | 7,653.0 | 33.3분 | 2026-08-14 | 13. OST·사운드트랙 | 음악 | 설명 | 57/59 |
| 502 | [싸이월드 감성 발라드 💿 그 시절 MP3에 꼭 있던 노래 ∣ 2000년대 발라드 명곡 모음 🎧 SG워너비,…](https://www.youtube.com/watch?v=5T42ApT_D-o) | 그때 그 가락 | 2,450 | 217,874 | 88.9 | ×3.4 | 7,153.4 | 105.1분 | 2026-09-21 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 16/17 |
| 503 | [the playlist to actually enter flowstate.](https://www.youtube.com/watch?v=wdDhTr_M7kA) | Pure Grit Stu… | 20,400 | 1,810,765 | 88.8 | ×96.1 | 33,846.7 | 123분 | 2026-08-29 | 기타 | 플레이리스트·모음 | 설명 | 545/553 |
| 504 | [🎧 Tanveer Evan: The Ultimate Love & Soulful Hits ∣ Emotiona…](https://www.youtube.com/watch?v=wHpNUy_W4GM) | Song Lyrics | 25,100 | 2,210,279 | 88.1 | ×177.3 | 15,778.9 | 23.6분 | 2026-06-04 | 기타 | 플레이리스트·모음 | 설명 | 890/896 |
| 505 | [腦子太吵時，先聽3分鐘｜2026最寧靜太極禪音精選｜讓呼吸慢下來，腦中的雜音也慢慢散去｜夜晚放空・晨間靜坐冥想・正念呼…](https://www.youtube.com/watch?v=KR1ZjmufbOE) | 清心樂坊Taiji Zen | 2,750 | 241,567 | 87.8 | ×35.2 | 3,335.8 | 59.3분 | 2026-08-10 | 기타 | 정보·해설 | 없음 | 24/24 |
| 506 | [The Wild Theme (EXTENDED REMIX) ∣ OM First Strike ∣ Sai Abh…](https://www.youtube.com/watch?v=IoJerPi947U) | JB RagaMix | 16,400 | 1,438,716 | 87.7 | ×17.9 | 13,862.2 | 4.3분 | 2026-07-10 | 기타 | 음악 | 설명 | 214/216 |
| 507 | [Enya - Miracles (Official Music Video)](https://www.youtube.com/watch?v=9hNpytudWRo) | Alternate Pop | 19,300 | 1,686,739 | 87.4 | ×146.7 | 13,022.0 | 8.1분 | 2026-06-14 | 1. 수면·명상·힐링 | 한 곡 | 설명 | 836/840 |
| 508 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 😎 회사 생각 안나는 방법 찾았음 ⚡ 이 음악 재생 필수! Groove JazzHop ㅣC…](https://www.youtube.com/watch?v=Lv02AFsUrN8) | grooveonpli | 986 | 86,163 | 87.4 | ×91.1 | 580.6 | 372.4분 | 2026-05-26 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 73/75 |
| 509 | [Smoke Mood - Just Relax ∣ Chill House & Deep House Mix 🎧 Ch…](https://www.youtube.com/watch?v=SMsadBMPWQU) | ChillNight Me… | 23,400 | 2,002,932 | 85.6 | ×579.7 | 14,302.5 | 67.5분 | 2026-06-04 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 317/320 |
| 510 | [Peaceful Chill Playlist 🌙 Trending English Songs 2026 🎧 Bes…](https://www.youtube.com/watch?v=td6iCrK4MHc) | Morning Seren… | 15,600 | 1,329,362 | 85.2 | ×29.7 | 45,256.5 | 70.7분 | 2026-09-22 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 137/147 |
| 511 | [🎧 Relax & Enjoy Playlist ∣ Best Trending Pop Music Collecti…](https://www.youtube.com/watch?v=vDs2KPkfw8Q) | Morning Seren… | 15,600 | 1,326,423 | 85.0 | ×29.7 | 17,143.0 | 67.4분 | 2026-08-05 | 3. 공부·집중·작업 | 커버·직접 부른 노래 | 설명 | 126/134 |
| 512 | [Soft Background Acoustic 🌿 Best Acoustic Covers Playlist 20…](https://www.youtube.com/watch?v=KoTsEko_7c8) | Afterhours Ac… | 15,400 | 1,305,209 | 84.8 | ×476.6 | 12,386.4 | 102분 | 2026-07-08 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 82/82 |
| 513 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 너도 지금 이 노래 듣고 있을까? 🤍 ∣ Chill R&B · 매장음악 · 카페 플레이리스트](https://www.youtube.com/watch?v=AM8WMi8_1cE) | mellomoodyy | 6,240 | 527,303 | 84.5 | ×147.7 | 5,665.9 | 90.1분 | 2026-07-21 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 185/185 |
| 514 | [[playlist] 다신 사랑하지 않을 다짐](https://www.youtube.com/watch?v=xNrmomdWeqk) | le | 12,300 | 1,022,658 | 83.1 | ×23.9 | 5,889.1 | 25.4분 | 2026-05-01 | 기타 | 플레이리스트·모음 | 없음 | 655/666 |
| 515 | [🎧요즘 들은 플리 중에 제일 느낌 좋다… 느좋 감성힙합 Chill 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 🌙](https://www.youtube.com/watch?v=9iqkcoMV39k) | 𝐅𝐞𝐞𝐥𝐿𝐲𝐧 | 5,020 | 415,614 | 82.8 | ×46.1 | 2,877.9 | 70.3분 | 2026-05-30 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 281/281 |
| 516 | [듣는 순간 마음이 편안해지는 첼로와 오보에 🎻 ∣ 공부, 휴식, 감성 힐링 음악](https://www.youtube.com/watch?v=aha1_5ENidU) | 따뜻한 휴식 Studio | 1,990 | 164,722 | 82.8 | ×377.8 | 1,144.6 | 33.4분 | 2026-05-31 | 1. 수면·명상·힐링 | 음악 | 설명 | 100/100 |
| 517 | [if this background music found you, life will get better](https://www.youtube.com/watch?v=l3UmhyVCF90) | Ksu4000 | 22,600 | 1,864,521 | 82.5 | ×163.9 | 26,016.8 | 60.5분 | 2026-08-11 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 2,014/2,020 |
| 518 | [마음이 편안해져요, 가을 아침 클래식 ㅣ듣기만 해도 행복해지는 클래식 명곡](https://www.youtube.com/watch?v=XOiUmptBDVk) | Aria classic … | 2,510 | 206,843 | 82.4 | ×37.2 | 4,096.0 | 68분 | 2026-09-01 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 18/18 |
| 519 | [33 Koti Devi Devta हरेक विहानको मन्त्र ∣ हर हर महादेव ∣ जय …](https://www.youtube.com/watch?v=7fiSZtq8nHs) | Bhajan Hub Ne… | 33,400 | 2,748,290 | 82.3 | ×386.1 | 18,989.3 | 11.5분 | 2026-05-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,375/1,385 |
| 520 | [108 Hare Krishna Mahamantra Chants ∣ Harinam Kirtan for Pea…](https://www.youtube.com/watch?v=_AXkyLABNdw) | Pinakin Music | 10,400 | 855,261 | 82.2 | ×524.7 | 7,787.0 | 18.2분 | 2026-07-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 422/425 |
| 521 | [Smoke Mood - Just Relax ∣ Chill House & Deep House Mix 🎧 Ch…](https://www.youtube.com/watch?v=yEASFhtzSMQ) | Chill Night H… | 28,600 | 2,341,551 | 81.9 | ×5,370.5 | 13,170.3 | 68.7분 | 2026-04-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 317/323 |
| 522 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Study / Focus …](https://www.youtube.com/watch?v=aJsXjVL43xI) | Chill Vibes H… | 7,920 | 643,228 | 81.2 | ×3,027.0 | 9,294.6 | 8분 | 2026-08-14 | 3. 공부·집중·작업 | 음악 | 설명 | 65/65 |
| 523 | [NIGHT PROTOCOL ∣ Dark Cyberpunk Music for Deep Work & Focus](https://www.youtube.com/watch?v=zXGb3k-A1Vo) | SoundFlow Lab | 8,950 | 725,168 | 81.0 | ×21.0 | 11,917.6 | 94.2분 | 2026-08-22 | 3. 공부·집중·작업 | 음악 | 설명 | 344/361 |
| 524 | [Relaxing Classic Rock 2026 🎸 Greatest Soft Rock Hits for Dr…](https://www.youtube.com/watch?v=m1zUF6E51kw) | Enchoes Of Cl… | 16,800 | 1,357,885 | 80.8 | ×1,846.2 | 8,629.8 | 81.6분 | 2026-05-17 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 1,040/1,055 |
| 525 | [하루를 밝게 만드는 찬송가 모음 10곡 ∣ 기분 좋아지는 찬송가 모음 10곡 ∣ 어쿠스틱 기타 찬양 ∣ 듣…](https://www.youtube.com/watch?v=AOyN15yGFrs) | 주님곁에 | 18,700 | 1,498,963 | 80.2 | ×33.7 | 10,116.8 | 70.5분 | 2026-05-27 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 1,229/1,239 |
| 526 | [Mozart Style ∣ 아침 공기처럼 가볍게 흐르는 모차르트풍 스트링 앙상블 ✿중간광고 없음 ∣ 잔잔한…](https://www.youtube.com/watch?v=8SUfn18vz_U) | Lucerna Harmo… | 18,200 | 1,457,258 | 80.1 | ×201.5 | 11,965.3 | 132분 | 2026-06-22 | 4. 카페·매장·라운지 | 음악 | 설명 | 1,123/1,142 |
| 527 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=8vwZSZcOPtM) | Click Bollywo… | 10,700 | 856,453 | 80.0 | ×6,851.6 | 7,768.6 | 7.9분 | 2026-07-04 | 3. 공부·집중·작업 | 음악 | 설명 | 91/92 |
| 528 | [𝘠𝘰𝘶 𝘢𝘤𝘤𝘪𝘥𝘦𝘯𝘵𝘢𝘭𝘭𝘺 𝘧𝘦𝘭𝘭 𝘪𝘯 𝘭𝘰𝘷𝘦 𝘸𝘪𝘵𝘩 𝘚𝘰𝘶𝘵𝘩 𝘐𝘯𝘥𝘪𝘢𝘯 𝘴𝘰𝘯𝘨𝘴 (+ 𝘵𝘪…](https://www.youtube.com/watch?v=JgO5ly6YvGI) | 𝙏𝙪𝙭𝙡𝙞𝙥𝙨 🌷 | 41,600 | 3,290,020 | 79.1 | ×5.8 | 21,512.6 | 19.5분 | 2026-05-22 | 기타 | 음악 | 설명 | 950/954 |
| 529 | [A K I R A - Floating High (original mix)](https://www.youtube.com/watch?v=cp_EDM8pS0Q) | AKIRA CLOUD | 7,870 | 621,027 | 78.9 | ×123.3 | 6,879.8 | 6.4분 | 2026-07-24 | 기타 | 음악 | 설명 | 122/122 |
| 530 | [মন ছুঁয়ে যাওয়া বাংলা Lo-Fi Romantic Songs _ Relaxing Bang…](https://www.youtube.com/watch?v=WX8EbRSHQYo) | Harano Kabita | 26,400 | 2,066,291 | 78.3 | ×454.8 | 28,032.2 | 17.6분 | 2026-08-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 255/256 |
| 531 | [영혼을 울리는 집시 바이올린 🎻 ∣ 감성 바이올린 · 집시 음악 · 휴식 플레이리스트 ∣ 보라빛 음악정원](https://www.youtube.com/watch?v=7xQeXJwhFh8) | 보랏빛 음악정원 | 174 | 13,589 | 78.1 | ×47.5 | 238.9 | 87.7분 | 2026-08-26 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 16/16 |
| 532 | [Heartbreaking 💔 songs + lofi Mashup songs Slowed Reverb son…](https://www.youtube.com/watch?v=u6gVi3TsKTM) | JR buzdar off… | 16,400 | 1,280,490 | 78.1 | ×3,612.1 | 15,372.5 | 7.8분 | 2026-07-31 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 53/53 |
| 533 | [15 Min Self Healing Music 🌿 Heal From Within & Find Inner P…](https://www.youtube.com/watch?v=wi3auWpIaZY) | Inner Healing… | 1,240 | 96,757 | 78.0 | ×65.2 | 2,163.2 | 16.5분 | 2026-09-07 | 1. 수면·명상·힐링 | 음악 | 설명 | 53/53 |
| 534 | [요즘 이 노래에 빠졌다 🎧 중독성 리듬 락트로트 17곡 2시간 10분 연속듣기 ∣ I’m Addicted …](https://www.youtube.com/watch?v=rDvH1El0H3k) | 인생은 트로트 | 9,120 | 709,965 | 77.8 | ×48.5 | 15,466.5 | 130.3분 | 2026-09-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 338/338 |
| 535 | [Batman’s Solitude ∣ Dark Jazz Noir for Late Night Reflection](https://www.youtube.com/watch?v=s87k34ud3Kc) | Saturday Nigh… | 17,300 | 1,345,069 | 77.8 | ×119.5 | 8,312.4 | 60분 | 2026-05-13 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 590/591 |
| 536 | [TAI CHI MUSIC - Ancient Tao Healing ∣ Chinese Zen Music for…](https://www.youtube.com/watch?v=FDUj2q61rQ8) | Nebula Dreams | 6,080 | 472,047 | 77.6 | ×31.9 | 4,021.3 | 85.3분 | 2026-06-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 192/193 |
| 537 | [【作業用BGM】名探偵コナン 夜ジャズメドレー☔️｜雨音とともに聴く Relaxing Jazz BGM](https://www.youtube.com/watch?v=ZoLpYGeZkn0) | Ken's Cafe&Ja… | 6,330 | 490,996 | 77.6 | ×22.2 | 3,050.3 | 167.6분 | 2026-05-14 | 7. 재즈·보사노바 | 음악 | 설명 | 175/175 |
| 538 | [Sitar for Dopamine Reset ∣ Indian Classical Music for Mindf…](https://www.youtube.com/watch?v=SEw8IsSXRSU) | Raga Focus | 37,500 | 2,898,355 | 77.3 | ×2,008.6 | 16,489.5 | 90분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,247/1,247 |
| 539 | [somehow this became your background music](https://www.youtube.com/watch?v=GTx1UYV9Y-o) | Ksu4000 | 22,600 | 1,745,927 | 77.2 | ×153.5 | 21,644.0 | 61.8분 | 2026-08-02 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 1,583/1,588 |
| 540 | [Do not listen to her music. She can hypnotise you in 4.49 m…](https://www.youtube.com/watch?v=0tBUIo44w-A) | Dream Weaver … | 18,900 | 1,457,093 | 77.1 | ×1,659.6 | 8,588.4 | 5.7분 | 2026-05-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 796/796 |
| 541 | [2 Hours Super Relaxing Baby Music ♥♥♥ Bedtime Lullaby For S…](https://www.youtube.com/watch?v=e_-uzFi6JlI) | Deep Calm Whi… | 31,500 | 2,419,750 | 76.8 | ×150.9 | 13,913.0 | 120.1분 | 2026-05-01 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 481/481 |
| 542 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=p8BH-D_YiQY) | Sani Music Of… | 8,880 | 681,248 | 76.7 | ×824.8 | 7,388.8 | 8분 | 2026-07-22 | 3. 공부·집중·작업 | 음악 | 설명 | 53/53 |
| 543 | [Positive Energy 2026 🌞 Feel Good Deep House Music for Morni…](https://www.youtube.com/watch?v=Dg9ePUDm4Vs) | ChillMorning … | 12,300 | 943,560 | 76.7 | ×275.8 | 6,513.0 | 65.7분 | 2026-05-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 331/331 |
| 544 | [jazz before i reach flow state](https://www.youtube.com/watch?v=fQIJb1h1RkA) | Defunct | 11,100 | 851,061 | 76.7 | ×190.6 | 5,253.5 | 127.8분 | 2026-05-13 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 944/946 |
| 545 | [MOOD OFF 💔Sad 😭 LOFI SONG MASHUP ∣∣ SAD HEART BROKEN 💔 MOOD…](https://www.youtube.com/watch?v=kjV1sVljycI) | Hindi sad son… | 41,700 | 3,196,392 | 76.7 | ×27,088.1 | 19,951.7 | 19.6분 | 2026-05-15 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 330/330 |
| 546 | [ENIGMA Style Music 🔥 Whisper of My Angel 🔥 2026](https://www.youtube.com/watch?v=ELv5bUhS-Qw) | VoiceLine Mus… | 4,020 | 307,769 | 76.6 | ×1,738.8 | 1,816.2 | 5.6분 | 2026-05-05 | 기타 | 음악 | 설명 | 95/97 |
| 547 | [Relajación Profunda, Claridad Mental 🌿 Reduce El Estrés Y L…](https://www.youtube.com/watch?v=j8hCioy51LU) | Healing Soul … | 10,700 | 818,863 | 76.5 | ×367.9 | 6,452.2 | 226.2분 | 2026-06-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 132/132 |
| 548 | [Melepasmu - Drive (Waktu Luang Version) ∣ Ambient Pop Melan…](https://www.youtube.com/watch?v=CfyEhCWn45o) | Waktu Luang | 18,700 | 1,430,416 | 76.5 | ×24.9 | 9,870.7 | 4.3분 | 2026-05-30 | 5. 운동·드라이브·신나는 | 커버·직접 부른 노래 | 설명 | 108/109 |
| 549 | [POV: YOU ARE A DESI BADDIE 💋😭 (PART-2) ✨ (+TIMESTAMPS) 😋 TH…](https://www.youtube.com/watch?v=9avHQt7MnK4) | Dramanique⋆.𐙚… | 31,800 | 2,429,366 | 76.4 | ×5.2 | 14,047.3 | 26.6분 | 2026-05-02 | 기타 | 정보·해설 | 설명 | 584/584 |
| 550 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=WH_pNjVfkCY) | Click Bollywo… | 10,700 | 817,449 | 76.4 | ×6,539.6 | 8,348.8 | 8분 | 2026-07-16 | 3. 공부·집중·작업 | 음악 | 설명 | 118/118 |
| 551 | [Enya Inspired - Tears Of The Rain (Ai Music)](https://www.youtube.com/watch?v=ZqRhMKrbk58) | Sonic Beatz | 5,870 | 445,689 | 75.9 | ×104.0 | 2,886.3 | 7.5분 | 2026-05-20 | 14. AI 음악 | AI 음악 | 설명 | 412/412 |
| 552 | [Afro House Mix 2026 🔥 Tribal Afro House Energy ∣ Emotional …](https://www.youtube.com/watch?v=UIzQAbsrlRk) | Jungle Pulse … | 27,000 | 2,048,863 | 75.9 | ×1,415.4 | 13,318.8 | 99.4분 | 2026-05-21 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 279/280 |
| 553 | [𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 들으면 행복해지는 노래 모음 🫧 하루종일 듣기 좋은 팝송 플레이리스트](https://www.youtube.com/watch?v=lQrhgr4_dKg) | seroma room | 16,600 | 1,258,439 | 75.8 | ×134.7 | 7,347.7 | 542.2분 | 2026-05-04 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 167/169 |
| 554 | [Life before Social Media - CHILL BRAZIL ∣ Samba, Luxury Bos…](https://www.youtube.com/watch?v=NHZXCzKGDQc) | Golden Smile | 6,570 | 497,029 | 75.7 | ×148.7 | 3,505.8 | 152.4분 | 2026-06-02 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 55/55 |
| 555 | [Playlist ∣ 가을밤에는 남자발라드를 들어요 🍂 ∣ 한국 감성 발라드 모음 🔥](https://www.youtube.com/watch?v=iaEax89R7fQ) | 이짐땡 | 2,860 | 215,298 | 75.3 | ×20.6 | 6,136.9 | 167.7분 | 2026-09-17 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 8/9 |
| 556 | [하츠투하츠 Hearts2Hearts 'RUDE!+Lemon Tang' 2026 한국대중음악상(KM Char…](https://www.youtube.com/watch?v=ddGnUiIjrgo) | poptforming | 5,870 | 441,699 | 75.2 | – | 4,974.2 | 6.6분 | 2026-07-25 | 기타 | 음악 | 없음 | 314/314 |
| 557 | [Ocean Chillout - Sunset Lounge Melodies and Luxury Lounge V…](https://www.youtube.com/watch?v=hFaOxrQmaQ4) | Afterglow Lou… | 10,700 | 792,848 | 74.1 | ×214.8 | 7,530.1 | 125.2분 | 2026-07-09 | 4. 카페·매장·라운지 | 음악 | 설명 | 231/232 |
| 558 | [दिमाग को शांत करने वाला संगीत ∣ बांसुरी + संतूर + जलतरंग + …](https://www.youtube.com/watch?v=z6QYtZlFvb4) | Shanti univer… | 713 | 52,660 | 73.9 | ×165.1 | 414.4 | 14.6분 | 2026-06-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 17/17 |
| 559 | [My Heart And Soul ∣ Romantic Emotional Love Song ∣ Soft Emo…](https://www.youtube.com/watch?v=f2LgAVp301Q) | Soft Emotion … | 13,700 | 1,006,956 | 73.5 | ×115.5 | 7,538.1 | 5.8분 | 2026-06-10 | 기타 | 한 곡 | 설명 | 179/183 |
| 560 | [모차르트에서 영감을 받은 아침 힐링 클래식 🌿 첼로 & 오보에 ∣ 평온한 산속 일출과 함께하는 휴식 음악](https://www.youtube.com/watch?v=tr3LEDt_p88) | Korean Rock B… | 4,750 | 348,991 | 73.5 | ×12.6 | 2,866.6 | 42.2분 | 2026-06-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 83/84 |
| 561 | [Lord Heal Me -Inspired By Enya (2026 Ai Music Video)](https://www.youtube.com/watch?v=Q-JjRkFbFhU) | SOUNDIASM | 10,700 | 784,099 | 73.3 | ×3,742.7 | 5,380.6 | 5.2분 | 2026-05-29 | 14. AI 음악 | AI 음악 | 설명 | 326/326 |
| 562 | [Flora's Garden 🌸🌷✨ soft waltz piano for studying, reading &…](https://www.youtube.com/watch?v=J8Qi6W8t0Ek) | rumi. | 12,700 | 930,148 | 73.2 | ×285.2 | 6,722.0 | 251.5분 | 2026-06-05 | 3. 공부·집중·작업 | 음악 | 설명 | 467/468 |
| 563 | [10 Most Powerful Morning Mantras ∣ Remove All Negativity ∣ …](https://www.youtube.com/watch?v=rH2JDVys2Os) | Adhyatmik Dhw… | 28,900 | 2,104,441 | 72.8 | ×1,581.1 | 13,999.5 | 20.7분 | 2026-05-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,753/1,773 |
| 564 | [【星河入夢】 Ancient Chinese Healing Music 🎵 ∣ Qixi Star River 🌌 …](https://www.youtube.com/watch?v=pFttQ6MZ9d8) | Tianhe Harmony | 879 | 63,710 | 72.5 | ×154.1 | 686.0 | 77.8분 | 2026-07-21 | 1. 수면·명상·힐링 | 음악 | 설명 | 48/48 |
| 565 | [스튜디오 지브리 풍 클래식🍃 신비로운 정원에서 듣는 음악 ∣ 따뜻한 피아노와 플루트](https://www.youtube.com/watch?v=KIunwCFWDUE) | Little DoReMi | 4,200 | 304,048 | 72.4 | ×401.6 | 2,279.0 | 136.3분 | 2026-06-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 39/39 |
| 566 | [빈예서 신곡 공개! 듣자마자 눈물 터졌다… “나훈아의 감성이 그대로” 😭🎵](https://www.youtube.com/watch?v=noMxR6lohxM) | 서울 뮤직 | 1,160 | 83,858 | 72.3 | ×98.9 | 5,909.2 | 6.9분 | 2026-10-08 | 기타 | 한 곡 | 설명 | 19/34 |
| 567 | [🎬 듣는 순간 지나온 세월이 생각나 울컥했습니다. 🎼 너무 많은 것들을 책임지며 살아온 당신을 위한 노래 …](https://www.youtube.com/watch?v=f9qBfvwQ9Ak) | 가슴을 울리는 락카페 | 10,900 | 785,129 | 72.0 | ×99.0 | 5,317.0 | 4분 | 2026-05-27 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 | 198/205 |
| 568 | [Morning Coffee Indie Folk – Warm Acoustic Music for Peacefu…](https://www.youtube.com/watch?v=wFy9kud8FHE) | Silver Coast | 28,700 | 2,063,605 | 71.9 | ×38.0 | 17,675.5 | 65.3분 | 2026-06-27 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 369/370 |
| 569 | [playlist l 틀자마자 집중 잘 되는 느좋 노동요 🎧 chill • r&b • vibes ☾](https://www.youtube.com/watch?v=ese2bIvjZGU) | luroom | 8,190 | 586,834 | 71.7 | ×73.9 | 9,968.4 | 248.2분 | 2026-08-24 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 175/179 |
| 570 | [Unlock Brain Power in 3 Minutes ∣ Classical Music for Focus…](https://www.youtube.com/watch?v=-zNMRToG5Vw) | Classical Mind | 22,600 | 1,613,419 | 71.4 | ×659.2 | 10,063.4 | 138.7분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 457/462 |
| 571 | [Paris Night Chanson 🌙 1960s Vintage French Café Music (Roma…](https://www.youtube.com/watch?v=8LyppqPNDns) | AtelierChanson | 15,600 | 1,104,855 | 70.8 | ×906.4 | 6,246.6 | 23.9분 | 2026-04-28 | 4. 카페·매장·라운지 | 음악 | 설명 | 941/942 |
| 572 | [ㅤㅤㅤㅤㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤ](https://www.youtube.com/watch?v=UHHSdhBSfgQ) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 22,900 | 1,621,765 | 70.8 | ×267.8 | 20,146.4 | 93.6분 | 2026-08-02 | 기타 | 음악 | 설명 | 956/966 |
| 573 | [옛추억에 눈물나는 노래 '세월' #감성발라드 #감성가요](https://www.youtube.com/watch?v=zNbEjZxdswM) | 고구려TV🍒음악방송 | 4,140 | 292,497 | 70.7 | ×925.6 | 2,720.4 | 67.3분 | 2026-07-06 | 9. 가요·발라드·트로트 | 음악 | 설명 | 196/198 |
| 574 | [Музыкальная терапия🌿успокаивает нервную систему и освежает …](https://www.youtube.com/watch?v=iBs7kGH9KhA) | МЕЛОДИЯ ДЛЯ Д… | 15,600 | 1,097,842 | 70.4 | ×425.3 | 7,005.4 | 60.2분 | 2026-05-18 | 6. 피아노·클래식·연주곡 | 음악 | 없음 | 912/914 |
| 575 | [Groove Playlist ∣ ∣ Let your worries melt into the rhythm ∣…](https://www.youtube.com/watch?v=PjyT13hITqM) | DRDR | 13,800 | 964,773 | 69.9 | ×262.2 | 6,146.7 | 206.3분 | 2026-05-18 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 218/218 |
| 576 | [The Most Beautiful And Emotional Cinematic Adagio ∣ Cello &…](https://www.youtube.com/watch?v=6AKklMjtK8M) | CLASSICAL SPA… | 11,200 | 782,668 | 69.9 | ×532.6 | 4,940.4 | 61.9분 | 2026-05-16 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 981/994 |
| 577 | [soft pastel flowers 🌸🌷 relaxing piano for dreamy & peaceful…](https://www.youtube.com/watch?v=9NxQWqVtHRA) | She of the Va… | 11,700 | 809,603 | 69.2 | ×123.9 | 4,578.6 | 37.8분 | 2026-04-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 358/360 |
| 578 | [공부할 때 듣는 판타지 음악 ∣ playlist](https://www.youtube.com/watch?v=d8sLNlVAuxE) | Flow Trigger. | 6,540 | 452,500 | 69.2 | ×27.9 | 7,047.5 | 130.3분 | 2026-08-19 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 58/60 |
| 579 | [Deep Chill Mix 2026 🌌 Emotional House & Soulful Vibes for S…](https://www.youtube.com/watch?v=5FQsa5nWaW0) | Rhythm Flow | 23,700 | 1,620,785 | 68.4 | ×280.5 | 15,019.0 | 60.8분 | 2026-07-06 | 3. 공부·집중·작업 | 정보·해설 | 설명 | 323/328 |
| 580 | [Clear Yourself of Everything That Drains You ∣ Calm Your Mi…](https://www.youtube.com/watch?v=Ww-tZVjkI9Y) | Frequencies o… | 46,400 | 3,156,662 | 68.0 | ×25.5 | 26,384.6 | 68.4분 | 2026-06-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,284/1,296 |
| 581 | [Put This On and Calm Your Brain... (No Ads)🌧️ Soft Piano Mu…](https://www.youtube.com/watch?v=vhJgRiH31bQ) | Cozy Attic Ni… | 5,880 | 399,150 | 67.9 | ×380.3 | 3,229.8 | 716.8분 | 2026-06-20 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 182/186 |
| 582 | [Playlist 🎤 노래방 발라드 인기차트 & 애창곡](https://www.youtube.com/watch?v=4ZLxFva_K5I) | 필청 | 2,150 | 144,709 | 67.3 | ×15.7 | 961.8 | 165분 | 2026-05-24 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 20/20 |
| 583 | [[KPOP playlist] 마법처럼 빠져드는 케이팝 노동요](https://www.youtube.com/watch?v=uuZiS5xRAVw) | 오이는빼주세요 | 13,100 | 875,543 | 66.8 | ×74.8 | 5,445.3 | 59.7분 | 2026-05-14 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 70/70 |
| 584 | [Too Much on Your Mind? Stay Here for a While ∣ Arabic Oud A…](https://www.youtube.com/watch?v=uDCjW-9mE2k) | Sahara Echo M… | 14,100 | 937,657 | 66.5 | ×296.6 | 5,359.4 | 64.4분 | 2026-04-30 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 442/442 |
| 585 | [Deepest Sleep Healing - Release Melatonin, Calm Anxiety & S…](https://www.youtube.com/watch?v=J64B8xhHEbs) | Deep Sleep Ha… | 12,800 | 848,645 | 66.3 | ×424.6 | 6,907.3 | 225.4분 | 2026-06-21 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 232/234 |
| 586 | [𝐂𝐡𝐚𝐭𝐩𝐚𝐭𝐢 𝐇𝐨𝐧𝐞𝐲 𝐬𝐢𝐧𝐠𝐡 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐜𝐮𝐳 𝐲𝐨𝐮 𝐫𝐞𝐚𝐥𝐥𝐲 𝐧𝐞𝐞𝐝 𝐭𝐡𝐢𝐬. 𝐛𝐲 …](https://www.youtube.com/watch?v=eXNfz_Rs-KQ) | 𝐫𝐢𝐞 | 28,900 | 1,910,526 | 66.1 | ×840.7 | 12,509.3 | 14.8분 | 2026-05-22 | 기타 | 플레이리스트·모음 | 없음 | 211/212 |
| 587 | [하늘을 닮은 여름 🌸 여름 감성 피아노 플레이리스트 ∣ BGM ∣ 힐링·작업·집중](https://www.youtube.com/watch?v=Os2XdhfzZdo) | Mellow Season | 2,870 | 189,636 | 66.1 | ×23.9 | 1,946.7 | 120.9분 | 2026-07-16 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 31/31 |
| 588 | [3小時宅家Lofi音樂合集｜累了，你只想宅在家裡｜超長版為一個人獨處而生的放鬆音樂，適合发呆或什么都不做](https://www.youtube.com/watch?v=kiClDrAsuqE) | SeaU Lofi | 14,200 | 936,332 | 65.9 | ×68.6 | 5,994.1 | 191.8분 | 2026-05-19 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 238/242 |
| 589 | [a quiet playlist for a quiet heart (calm/relax piano)](https://www.youtube.com/watch?v=BBz7-F9mdUE) | Little Thing | 30,600 | 2,016,687 | 65.9 | ×181.9 | 13,363.0 | 89.5분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 314/315 |
| 590 | [Chinese Night Music: Soft Guzheng & Erhu ∣ Sleep Like Ancie…](https://www.youtube.com/watch?v=rw5yQGIQuwE) | Lotus Echo 莲之… | 16,500 | 1,086,178 | 65.8 | ×270.4 | 6,080.8 | 240.2분 | 2026-04-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 378/380 |
| 591 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Stu…](https://www.youtube.com/watch?v=Koo5Xgqn_zE) | Stylish Offic… | 15,000 | 985,453 | 65.7 | ×2,227.0 | 17,215.3 | 8분 | 2026-08-26 | 3. 공부·집중·작업 | 음악 | 설명 | 99/101 |
| 592 | [मोहे मोर बनइय्यो राधा ∣ Mohe Mor Banaiyo Radha Apne Vrindav…](https://www.youtube.com/watch?v=CPGQtKem4Cc) | Rangilo Gurja… | 25,000 | 1,627,137 | 65.1 | ×1,809.9 | 12,768.2 | 19.4분 | 2026-06-16 | 1. 수면·명상·힐링 | 음악 | 설명 | 375/375 |
| 593 | [[Playlist] "아침에 듣기 좋은 산뜻한 클래식 왈츠" ∣ Summer Palace Waltz 🌿](https://www.youtube.com/watch?v=D2WezFoeswI) | okply | 15,500 | 1,008,196 | 65.0 | ×127.9 | 6,382.7 | 148.9분 | 2026-05-17 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 578/583 |
| 594 | [😊 아침부터 기분 좋게 행복해지는 노래 모음 🎧 가볍게 흥얼거리는 기분 좋게 행복한 노래 모음](https://www.youtube.com/watch?v=r0jtXc1Y-jE) | 행복 | 7,010 | 454,307 | 64.8 | ×119.7 | 7,397.2 | 116.4분 | 2026-08-21 | 14. AI 음악 | AI 음악 | 설명 | 152/158 |
| 595 | [मन को शांत करने वाली धुन ∣ राजयोग ध्यान की सहज विधि ∣ Brahm…](https://www.youtube.com/watch?v=ux3QNU3AaII) | Bhakti Naad | 771 | 49,879 | 64.7 | ×48.3 | 428.6 | 6.8분 | 2026-06-27 | 1. 수면·명상·힐링 | 음악 | 설명 | 27/27 |
| 596 | [Hyperfocus ∣ Lock In for 2 Hours ∣ Deep Work Study With Me …](https://www.youtube.com/watch?v=Rk0yG_dT0iI) | Work With Paul | 18,000 | 1,164,276 | 64.7 | ×8.5 | 16,613.0 | 111.4분 | 2026-08-13 | 3. 공부·집중·작업 | 긴 한 곡·반복 | 설명 | 138/141 |
| 597 | [Spiritual Temple Music ∣ 30 Minutes Stress Relief & Inner P…](https://www.youtube.com/watch?v=NF4gjQzGetw) | Shashwat Swar | 15,300 | 986,411 | 64.5 | ×82.8 | 6,766.3 | 34.2분 | 2026-05-29 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 146/149 |
| 598 | [샹송이 이렇게 까지 좋은줄 몰랐습니다. 아랑드롱이 사랑하던 멜로디가 아름다운 그 음악 ∣ Songs Tha…](https://www.youtube.com/watch?v=MHgCWNV-eKY) | Yesterday SOU… | 6,060 | 390,031 | 64.4 | ×773.9 | 2,454.0 | 43.9분 | 2026-05-16 | 기타 | 음악 | 설명 | 203/203 |
| 599 | [Richard Clayderman Tribute 🎹 ∣ Timeless Romantic Piano Music](https://www.youtube.com/watch?v=ZwlhZLzFxtk) | SONELIUM | 7,370 | 471,725 | 64.0 | ×1,206.5 | 6,412.2 | 29.4분 | 2026-08-09 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 178/179 |
| 600 | [Amélie ☕️ A Slow Weekend in Paris ∣ Piano Music for Relaxin…](https://www.youtube.com/watch?v=oToDtW7Gaas) | Peter Pan's L… | 5,950 | 380,237 | 63.9 | ×34.0 | 7,004.6 | 61.4분 | 2026-08-29 | 3. 공부·집중·작업 | 음악 | 설명 | 213/213 |
| 601 | [🌙 Relaxing Gospel R&B Worship Music 2026 – Peaceful Midnigh…](https://www.youtube.com/watch?v=SKYFRvhTL4A) | Sacred worshi… | 13,200 | 843,264 | 63.9 | ×1,821.3 | 5,352.7 | 61.2분 | 2026-05-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 355/356 |
| 602 | [생각보다 좋게 풀리는 날 🎵마음에 초록빛을 채우는 힐링 피아노 ∣ 스트레스 해소 · 편안한 휴식 · 카페음…](https://www.youtube.com/watch?v=QC3xgG-dZJg) | Romua 로무아 | 3,370 | 214,789 | 63.7 | ×30.8 | 1,769.9 | 180.7분 | 2026-06-22 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 33/33 |
| 603 | [Gentle Rain Outside, Warm Piano Inside (No Ads) 🌧️ Helps Yo…](https://www.youtube.com/watch?v=G9iosi2cIh4) | Cozy Attic Ni… | 5,880 | 373,588 | 63.5 | ×356.0 | 3,260.4 | 717.9분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 178/194 |
| 604 | [The Most Beautiful Rachmaninoff-Inspired Adagios ∣ Quiet Ce…](https://www.youtube.com/watch?v=ZdzITqD4vlM) | Adagio Melanc… | 9,930 | 628,237 | 63.3 | ×69.8 | 8,630.7 | 61.6분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,106/1,122 |
| 605 | [모든 일이 잘 풀리는 아침을 여는 음악 ∣ 막혔던 일이 시원하게 풀리는 기분](https://www.youtube.com/watch?v=6MQT5DkZTEU) | LazyFlow | 10,700 | 672,407 | 62.8 | ×122.3 | 3,945.7 | 90.4분 | 2026-05-04 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 167/168 |
| 606 | [Your Productive Office Playlist 🤍 Soft Acoustic Covers to S…](https://www.youtube.com/watch?v=h2cVkEu99eI) | Afterhours Ac… | 15,400 | 963,865 | 62.6 | ×352.0 | 9,324.0 | 116.7분 | 2026-07-10 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 54/54 |
| 607 | [Ludovico Einaudi – 6 Piano Pieces ∣ Relaxing Music for Stud…](https://www.youtube.com/watch?v=nFJCWUpe2w4) | Yurii Salukha | 5,880 | 367,859 | 62.6 | ×280.2 | 4,623.9 | 29.7분 | 2026-08-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 54/54 |
| 608 | [【異世界ケルト】路地裏で流れる安らぎのファンタジーBGM｜静かな街のかすかな余韻 [睡眠用BGM・リラックス用BGM・…](https://www.youtube.com/watch?v=w2XZiZpAYZg) | Roran Baron | 8,840 | 552,702 | 62.5 | ×53.6 | 3,281.3 | 182.9분 | 2026-05-06 | 기타 | 정보·해설 | 설명 | 261/261 |
| 609 | [the best classical music for deep concentration ∣ string qu…](https://www.youtube.com/watch?v=Px1HC9ExXOk) | FocusSpace | 8,990 | 559,782 | 62.3 | ×96.5 | 6,162.8 | 64.6분 | 2026-07-23 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 444/452 |
| 610 | [Dark Jazz & Late Night Trip-Hop // Atmospheric Music for La…](https://www.youtube.com/watch?v=pGuvWU_1j-o) | Jazz Haze | 32,900 | 2,043,693 | 62.1 | ×851.9 | 12,637.4 | 94.2분 | 2026-05-13 | 5. 운동·드라이브·신나는 | 음악 | 없음 | 480/481 |
| 611 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 너도 나 좋아했으면 좋겠다](https://www.youtube.com/watch?v=4mAxMsNJAMI) | .happy | 228 | 14,140 | 62.0 | ×3.1 | 110.6 | 18.4분 | 2026-06-16 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 2/2 |
| 612 | [【眠れない夜のBGM】頭の中がうるさい夜に。考えすぎて眠れない夜のギターLofi｜睡眠・リラックス・深夜BGM ∣ s…](https://www.youtube.com/watch?v=IZRmwcM2974) | gentle night … | 14,000 | 867,944 | 62.0 | ×248.5 | 4,853.4 | 125.2분 | 2026-04-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 173/183 |
| 613 | [바흐와 모차르트의 감성을 담은 아침 클래식 🌿 하루를 여는 평화로운 힐링 연주](https://www.youtube.com/watch?v=9_HXWyP1MsE) | Korean Rock B… | 4,750 | 293,992 | 61.9 | ×10.6 | 2,986.0 | 40.3분 | 2026-07-15 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 40/42 |
| 614 | [Dolce Vita 🇮🇹 Luxury Italian Lounge Music ∣ Elegant Café Ja…](https://www.youtube.com/watch?v=oiG7xIAgCFw) | ITALIAN MAFIA… | 14,300 | 876,710 | 61.3 | ×865.9 | 8,531.9 | 86.5분 | 2026-07-11 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 346/347 |
| 615 | [행운이 찾아오는 아침 🎵마음에 건강한 에너지를 채우는 힐링 피아노 ∣ 스트레스 해소 · 편안한 휴식 · 카…](https://www.youtube.com/watch?v=Xp2bSO5r5Os) | Romua 로무아 | 3,370 | 206,554 | 61.3 | ×29.6 | 1,526.0 | 180분 | 2026-06-08 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 37/37 |
| 616 | [7080 추억의 노래 광고없음🎶 7080노래모음 주옥같은노래 ✨7080 추억의 노래 한국인이 가장 좋아하는…](https://www.youtube.com/watch?v=3tshpfOljYs) | 7080 감성 선율 | 7,460 | 455,374 | 61.0 | ×17.4 | 10,984.2 | 118.6분 | 2026-09-10 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 63/66 |
| 617 | [15 Minute Meditation Music • Raise Your Vibration • Relax M…](https://www.youtube.com/watch?v=e8EVg-NJCng) | Soul Waves - … | 2,620 | 159,001 | 60.7 | ×180.4 | 914.7 | 15.4분 | 2026-05-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 16/16 |
| 618 | [a playlist to make your brain shut up](https://www.youtube.com/watch?v=xIX_A2PRoW0) | HIGHWIND | 40,200 | 2,436,856 | 60.6 | ×157.2 | 36,957.6 | 62.1분 | 2026-08-17 | 1. 수면·명상·힐링 | 연주 | 설명 | 811/848 |
| 619 | [2000년대 발라드 명곡 30곡 💿 그 시절 우리가 사랑했던 노래｜SG워너비·김동률·씨야·티아라·양파 ✔ …](https://www.youtube.com/watch?v=IZ6NgLQjStY) | 추억음악다방 | 3,430 | 207,609 | 60.5 | ×54.1 | 2,197.9 | 117.8분 | 2026-07-19 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 17/17 |
| 620 | [The Knight Who Chose Peace ⚔️ ∣ Relaxing Fantasy Music](https://www.youtube.com/watch?v=u8xCmb7KbA0) | Melody of the… | 14,000 | 846,232 | 60.5 | ×170.4 | 5,243.2 | 74.5분 | 2026-05-13 | 기타 | 음악 | 설명 | 516/518 |
| 621 | [【作業用BGM】ちいかわ Instrumental Jazz 2時間 ∣ 深夜のジャズラウンジ ∣ ひとりごつ, 島の…](https://www.youtube.com/watch?v=CJEgDVcFy80) | GINZA Midnight | 22,000 | 1,320,189 | 60.0 | ×50.9 | 23,162.8 | 126.6분 | 2026-08-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 324/330 |
| 622 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 세종대왕이 경복궁에서 야근하며 듣던 가야금 재즈](https://www.youtube.com/watch?v=q3oC3zdfyw4) | 조선재즈 | 9,970 | 597,548 | 59.9 | ×116.6 | 4,527.0 | 180.7분 | 2026-06-12 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 468/472 |
| 623 | [[스페인 감성] "Frente a Tu Casa ∣ 그집앞 - 이재성" Korean OldPop 한국명곡](https://www.youtube.com/watch?v=IXEpsuBWbg8) | 스페인 감성 한국 올드송 | 1,420 | 84,599 | 59.6 | ×2.3 | 1,200.5 | 4.5분 | 2026-08-12 | 12. 커버·노래 부르기 | 음악 | 설명 | 14/14 |
| 624 | [Bollywood+ Bhojpuri mix songs playlist (💗⚡💃🏻) ∣ @songplayli…](https://www.youtube.com/watch?v=sLPyIfOvPRQ) | xthetic._.vib… | 36,500 | 2,159,016 | 59.1 | – | 13,328.4 | 16.9분 | 2026-05-13 | 기타 | 플레이리스트·모음 | 설명 | 319/319 |
| 625 | [[COVER] 한오백년 _ 어버이날을 맞이하여...](https://www.youtube.com/watch?v=W40yM35SfWc) | 감성메아리 | 5,320 | 313,812 | 59.0 | ×592.1 | 1,845.4 | 4.8분 | 2026-05-05 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 58/58 |
| 626 | [Fresh Mind Relaxing 💗 ∣ Slowed + Reverb Lofi Mix for Calm, …](https://www.youtube.com/watch?v=ACcuQVFbfnI) | Vansh Lofi | 29,200 | 1,716,916 | 58.8 | – | 13,489.1 | 16분 | 2026-06-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 88/88 |
| 627 | [나는 어디로 가나 - (국악 발라드)](https://www.youtube.com/watch?v=hd_rjKroAqM) | Rok Bi | 8,520 | 497,404 | 58.4 | ×53.9 | 3,071.2 | 5분 | 2026-05-13 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 203/205 |
| 628 | [途中広告なし[BGM]癒しの森カフェで何も考えない朝☕Gentle Morning Piano Jazz｜心地よく一日…](https://www.youtube.com/watch?v=qDJ8LG4noFk) | Aurora Tune | 19,200 | 1,119,741 | 58.3 | ×18.4 | 6,458.5 | 92.5분 | 2026-05-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 116/116 |
| 629 | [SAXOPHONE LOVE SONGS ❤️ Best Romantic Saxophone Music ∣ Bea…](https://www.youtube.com/watch?v=QpBzIwJPEoo) | Sax Chill Vib… | 27,700 | 1,611,613 | 58.2 | ×19.9 | 23,269.2 | 57.6분 | 2026-08-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 225/227 |
| 630 | [Sade Morning Coffee ☕ Vol.3 ∣ Luxury ChillMix ∣ Soulful Jaz…](https://www.youtube.com/watch?v=mp4oA2JflBQ) | Setsukin | 43,100 | 2,489,355 | 57.8 | ×164.2 | 15,098.6 | 114.5분 | 2026-05-10 | 4. 카페·매장·라운지 | 음악 | 설명 | 780/783 |
| 631 | [Rainy Day in the Treehouse:Cooking Beef Stew Bread Bowl & B…](https://www.youtube.com/watch?v=_Mugeu0ne3M) | Ghibli - ASMR… | 4,820 | 278,285 | 57.7 | ×990.3 | 1,546.0 | 6.5분 | 2026-04-25 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 71/72 |
| 632 | [Paganini (Vivaldi x Beethoven) House Music Mix – Hypnotic V…](https://www.youtube.com/watch?v=Q9TSg4bKjcs) | Velvet Freque… | 5,600 | 323,282 | 57.7 | ×337.5 | 2,001.1 | 7분 | 2026-05-13 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 212/214 |
| 633 | [처음부터 신나서 환장하는! ❤️ 신나는 트로트리믹스 고속도로메들리 ∣ 최신트로트 ∣ 트로트메들리 ∣ 감성트…](https://www.youtube.com/watch?v=zt45-jow7lo) | 다솜이의 트로트책방 | 7,710 | 444,228 | 57.6 | ×46.1 | 2,653.5 | 71.2분 | 2026-05-07 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 139/142 |
| 634 | [[중간광고없음] 🌿 잠시, 아무 생각도 하지 말아요. ∣ 숲속에서 듣는 잔잔한 피아노 ∣ BGM ∣ 휴식,…](https://www.youtube.com/watch?v=ebDKy0szHC8) | Riae & Piano | 12,400 | 714,333 | 57.6 | ×45.7 | 7,261.4 | 181.3분 | 2026-07-15 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 191/195 |
| 635 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 초여름 별사탕 𖤐ˊ˗](https://www.youtube.com/watch?v=aW-TYu5rwAY) | Horu | 3,550 | 204,296 | 57.5 | ×6.1 | 1,174.5 | 19.8분 | 2026-05-01 | 기타 | 플레이리스트·모음 | 없음 | 42/42 |
| 636 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 교토의 작은 카페, 말차향 재즈 🍵🎧 抹茶オーツラテ](https://www.youtube.com/watch?v=vLX3-MrBXFk) | 아오링고 잡화점 AORI… | 10,500 | 598,466 | 57.0 | ×27.7 | 9,293.3 | 292.4분 | 2026-08-18 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 114/119 |
| 637 | [50대이상이 들으면 정말 좋아할 노래 추천곡✨중년들이 사랑하는 겨울 노래 모음💕박인희/배따라기/여진/휘버스…](https://www.youtube.com/watch?v=TTkoF883bC8) | KTrot Melody | 10,100 | 573,366 | 56.8 | – | 6,870.1 | 126분 | 2026-07-30 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 103/103 |
| 638 | [비와 당신 (라디오스타 OST) - 가연이와 함께 듣는 비 오는 감성](https://www.youtube.com/watch?v=WmHI_XkpO2E) | GAYEON YOON | 28,600 | 1,619,240 | 56.6 | ×65.5 | 14,851.3 | 4.3분 | 2026-07-05 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 237/242 |
| 639 | [✨💖요즘 폼 미친(positive) 최신 아이돌 노래 모음 ∣ 신나는 ∣ 최신곡 ∣ 여돌 ∣ 남돌 ∣ 아이…](https://www.youtube.com/watch?v=eLiTRGAnmyk) | 띠잉뮤직 | 20,900 | 1,178,361 | 56.4 | ×99.5 | 7,898.5 | 121.8분 | 2026-05-26 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 162/162 |
| 640 | [[MIXSET] 늙크크의 여름 HipHop & R&B](https://www.youtube.com/watch?v=_o3psN6OCTk) | 떵신 tteongshin | 8,140 | 458,561 | 56.3 | – | 4,687.2 | 22.1분 | 2026-07-16 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 204/204 |
| 641 | [KUMAMICHI（熊道） — Japanese Zen Music Along the Bear’s Path](https://www.youtube.com/watch?v=vFJuk4U-V7Q) | Aether Journey | 34,200 | 1,911,920 | 55.9 | ×507.4 | 34,736.4 | 347분 | 2026-08-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 235/241 |
| 642 | [숲속에 내리는 잔잔한 빗소리 🌧️ 명상, 깊은 수면, 편안한 소리](https://www.youtube.com/watch?v=4Xl4kMOmGY8) | 숲 속 빗소리 | 1,800 | 100,425 | 55.8 | ×53.4 | 1,243.0 | 187.7분 | 2026-08-02 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 41/41 |
| 643 | [A Regular Day on the Journey ∣ Medieval Fantasy Music for D…](https://www.youtube.com/watch?v=TACRmufLfko) | Tales of Velm… | 17,700 | 984,807 | 55.6 | ×172.7 | 5,733.5 | 129.7분 | 2026-05-03 | 3. 공부·집중·작업 | 음악 | 설명 | 374/374 |
| 644 | [Dopamine Boost Music ∣ Flute, Sitar & Tabla for Positive En…](https://www.youtube.com/watch?v=kY7GcKagdjI) | CLASSICAL FUS… | 19,000 | 1,052,840 | 55.4 | ×224.0 | 8,205.3 | 27.8분 | 2026-06-16 | 3. 공부·집중·작업 | 음악 | 설명 | 717/719 |
| 645 | [Elevate yourself - Bhagavad Gita ∣ Dark Trip-Hop X Downtemp…](https://www.youtube.com/watch?v=vrn7QzaHsbk) | SUR-SPIRITUAL | 7,910 | 437,724 | 55.3 | ×150.3 | 16,325.8 | 5.3분 | 2026-09-25 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 97/98 |
| 646 | [background music.](https://www.youtube.com/watch?v=gOwbMN0JswA) | quiet please. | 34,900 | 1,929,199 | 55.3 | ×11.6 | 11,310.3 | 60분 | 2026-05-04 | 8. 로파이·시티팝·칠 | 음악 | 없음 | 205/205 |
| 647 | [첫 곡부터 너무 좋다 🍂 하루종일 듣게 되는 가을 올드팝 ∣ Vol.228 ∣ 7080 추억의 팝송 ∣ A…](https://www.youtube.com/watch?v=naLL7CGOC-8) | moka melody | 14,600 | 804,147 | 55.1 | ×42.2 | 12,686.2 | 367.3분 | 2026-08-19 | 4. 카페·매장·라운지 | 음악 | 설명 | 301/301 |
| 648 | [If You Can’t Sleep, Play This 🌙 Instant Deep Sleep Music & …](https://www.youtube.com/watch?v=PFn7jFxLbhE) | Deep Sleep Ha… | 12,800 | 703,613 | 55.0 | ×352.1 | 9,541.2 | 181.2분 | 2026-08-09 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 237/237 |
| 649 | [PAMPATANGGAL STRESS 🌴NON-STOP PINOY DUB REGGAE 2026 ∣ Relax…](https://www.youtube.com/watch?v=m4vweFMrdzw) | Evo Reggae Mix | 19,000 | 1,043,200 | 54.9 | ×159.0 | 8,154.1 | 74.8분 | 2026-06-16 | 기타 | 정보·해설 | 설명 | 429/430 |
| 650 | [Heals You While You Sleep (No Ads) • Increases Deep Sleep •…](https://www.youtube.com/watch?v=f68XXr9BDYw) | Serene Dreams… | 16,600 | 909,507 | 54.8 | ×431.5 | 11,567.8 | 226.8분 | 2026-08-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 311/312 |
| 651 | [The Little Forest Concert Vol.2 ∣ Cozy String Quartet for R…](https://www.youtube.com/watch?v=0DvSj6DAKDM) | 그루잠 Gurujam | 27,400 | 1,498,430 | 54.7 | ×209.1 | 11,158.1 | 45.1분 | 2026-06-10 | 3. 공부·집중·작업 | 음악 | 설명 | 364/370 |
| 652 | [🎧 Samz Vai: The Ultimate Sad & Emotional Hits 💔 ∣ Bengali L…](https://www.youtube.com/watch?v=kizXE5FXIFc) | Bangla Lofi 3… | 39,000 | 2,128,712 | 54.6 | ×76.8 | 23,707.4 | 26.9분 | 2026-07-24 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 239/253 |
| 653 | [90년대 2000년대 락발라드 명곡 모음 🎧 남자라면 한 번쯤 울컥했던 추억의 감성 노래 ∣ 버즈, 김경호…](https://www.youtube.com/watch?v=oB4-QrY7Vcc) | 발라드 홈 / BALLA… | 10,200 | 556,150 | 54.5 | ×58.9 | 5,711.5 | 187.4분 | 2026-07-16 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 79/80 |
| 654 | [Krishna Mantra ∣ Pregnancy Music ∣ Music for pregnant women…](https://www.youtube.com/watch?v=TuMDXAiXlf0) | Be Listener M… | 18,500 | 1,008,373 | 54.5 | ×85.5 | 7,370.5 | 12.4분 | 2026-06-07 | 기타 | 음악 | 설명 | 384/385 |
| 655 | [I’M COVERED NOT BROKEN ∣ R&B Gospel Soul Song (Healing, Str…](https://www.youtube.com/watch?v=H2lPB-NdhcM) | JESUS HEALS P… | 18,000 | 979,531 | 54.4 | ×889.7 | 5,457.0 | 4.2분 | 2026-04-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 580/580 |
| 656 | [(중간 광고 없음) 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 그때의 우린 왜 그리 서툴렀을까 ｜ 밤에 듣는 시린 첫사랑 발라드 …](https://www.youtube.com/watch?v=O-wm0ZSF2KU) | SonaWave | 12,300 | 663,314 | 53.9 | ×138.6 | 4,335.4 | 125.1분 | 2026-05-22 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 674/678 |
| 657 | [Chinese Zen Music🎵: Bamboo flute, erhu & Guzheng ∣ Relaxing…](https://www.youtube.com/watch?v=yGbaHLXUZWY) | ZenFlute | 32,700 | 1,746,963 | 53.4 | ×252.3 | 9,712.1 | 91.4분 | 2026-04-25 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,271/1,272 |
| 658 | [그 집 앞 (스페인어 버전 뮤직비디오) ∣ 이재성 원곡 라틴팝 리메이크 ∣ 한국어/스페인어 가사 자막 ∣ …](https://www.youtube.com/watch?v=T1fdlthH7Fw) | J.K.M | 37,500 | 2,000,361 | 53.3 | – | 12,903.0 | 4.2분 | 2026-05-20 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 설명 | 1,077/1,078 |
| 659 | [Evergreen ghazal ∣ कभी फुर्सत मिले तो बैठ कर ये सोचता हूँ म…](https://www.youtube.com/watch?v=CiqRihLd68Q) | SOUL VIBES IN… | 30,000 | 1,595,763 | 53.2 | ×24.9 | 15,370.7 | 5.3분 | 2026-07-10 | 기타 | 음악 | 설명 | 298/299 |
| 660 | [카페음악 ∣ 최고 다방 음악❤️ 카페에서 듣기 좋은 노래 ❤️ 50대-60대가 좋아하는 중년가요 ∣ 아침 …](https://www.youtube.com/watch?v=_h8CNlmPkjo) | Korean Cafe M… | 3,280 | 174,006 | 53.0 | ×2,949.3 | 1,196.3 | 10.8분 | 2026-05-29 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 22/22 |
| 661 | [HEAVEN-GIVEN VOICE ∣ Sad Love Songs ∣ soft rock ballad ∣ 슬픈…](https://www.youtube.com/watch?v=ySdeFYT0ohc) | Woori Sound | 13,000 | 688,947 | 53.0 | ×96.9 | 4,292.2 | 127.9분 | 2026-05-14 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 567/567 |
| 662 | [첫 곡부터 감성 미쳐버린🎧8090 레전드 플레이리스트](https://www.youtube.com/watch?v=i4uJ7c6b9gw) | Ceci Pop | 29,500 | 1,561,554 | 52.9 | ×103.4 | 11,288.7 | 112.8분 | 2026-06-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 1,362/1,363 |
| 663 | [[Playlist] 초록빛 향기 머무는 여름날과 어울리는 음악 ∣ 잔잔한 감성팝 카페음악 ∣ Healing…](https://www.youtube.com/watch?v=l3rA0WjsaNM) | 낡은 레코드 | 8,870 | 467,167 | 52.7 | ×48.1 | 3,067.6 | 77.9분 | 2026-05-23 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 71/71 |
| 664 | [1990~2026 한국 감성 발라드 명곡 100 🎵 마음을 울리는 인기 노래 모음 하루 종일 들어도 좋은 …](https://www.youtube.com/watch?v=l3FyvUQUgSA) | 바람의 발라드 | 21,000 | 1,104,139 | 52.6 | ×657.2 | 8,463.6 | 130.5분 | 2026-06-13 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 121/123 |
| 665 | [22 Beautiful Serenity Adagios That Will Touch Your Soul ∣ R…](https://www.youtube.com/watch?v=-kXB3QJb1Vs) | Silent Adagio | 11,400 | 598,493 | 52.5 | – | 3,890.5 | 120분 | 2026-05-21 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 297/297 |
| 666 | [여자력 상승하는 플리](https://www.youtube.com/watch?v=KSeIkQ_dpsg) | 무한우주에순간의빛일지라도 | 3,250 | 170,132 | 52.4 | ×10.1 | 3,493.0 | 15.4분 | 2026-09-03 | 기타 | 플레이리스트·모음 | 설명 | 12/13 |
| 667 | [😴 Baby Sleep Music That Works in 3 Minutes! 💤 Newborn Sleep…](https://www.youtube.com/watch?v=22SPWR7nyfM) | Mother & Baby… | 17,700 | 925,423 | 52.3 | ×24.7 | 7,605.6 | 122.7분 | 2026-06-22 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 668 | [LiL Baby - Work For Money ( Official Music Video)](https://www.youtube.com/watch?v=3FclEMAiJ6Q) | Vibes World R… | 225 | 11,763 | 52.3 | ×7.3 | 237.6 | 7분 | 2026-09-02 | 기타 | 한 곡 | 설명 | 3/3 |
| 669 | [2026년 6월 여돌 노래모음 ∣ 🔥 KPOP PLAYLIST](https://www.youtube.com/watch?v=a_19lS2wwOw) | 달플리 𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕 | 12,000 | 619,166 | 51.6 | ×46.3 | 4,352.7 | 64.9분 | 2026-06-02 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 53/53 |
| 670 | [7080 감성 포크송 ∣ 듣기 좋은 통기타 포크 15곡](https://www.youtube.com/watch?v=Hpsm6Kn5TM4) | ***7080가요산책*** | 4,730 | 244,043 | 51.6 | ×24.8 | 2,729.3 | 64.5분 | 2026-07-24 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 105/105 |
| 671 | [(No Ads) Relaxing Music For Deep Sleep • Anxiety Relief, Me…](https://www.youtube.com/watch?v=UhQANX3rKzA) | Bedtime Calm … | 12,200 | 627,857 | 51.5 | ×96.4 | 3,933.0 | 94.3분 | 2026-05-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 68/69 |
| 672 | [💚 초여름맛 메론소다 ☆・. ‘ . ꒰ 가사없는 집중 음악 ꒱](https://www.youtube.com/watch?v=FkmrHoP4xSk) | 둥실 ︵☆ | 1,190 | 61,149 | 51.4 | ×174.7 | 370.6 | 171.3분 | 2026-05-10 | 3. 공부·집중·작업 | 한 곡 | 설명 | 60/60 |
| 673 | [Piano Sleep Music with Relaxing Rain 🎶 Calm Your Mind, Reli…](https://www.youtube.com/watch?v=pFL8mgVoxnc) | Piano Rain Re… | 29,900 | 1,527,790 | 51.1 | ×107.3 | 16,905.1 | 203.6분 | 2026-07-23 | 1. 수면·명상·힐링 | 음악 | 설명 | 327/327 |
| 674 | [2 Hour Sitar for Clean Your Brain Instantly ∣ Indian Classi…](https://www.youtube.com/watch?v=PVGFHGLRjK4) | Sacred Mind H… | 8,290 | 421,654 | 50.9 | ×305.4 | 2,399.0 | 120.4분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 206/206 |
| 675 | [𝙋𝙇𝘼𝙔𝙇𝙄𝙎𝙏 찻집 리틀 포레스트](https://www.youtube.com/watch?v=9NAEMS-BJT0) | off frame | 3,300 | 167,762 | 50.8 | ×81.3 | 1,312.2 | 78.8분 | 2026-06-16 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 129/133 |
| 676 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=3k0BBE7e6TA) | Z B Official … | 21,200 | 1,072,771 | 50.6 | ×3,460.6 | 14,281.7 | 8분 | 2026-08-08 | 3. 공부·집중·작업 | 음악 | 설명 | 75/78 |
| 677 | [🎵 내려놓아라 ∣ 신나는 불교 EDM 트로트 ∣ 근심 걱정 다 내려놔라](https://www.youtube.com/watch?v=-y3mLSiAcU0) | 극락가요 | 393 | 19,877 | 50.6 | ×13.5 | 155.4 | 4.5분 | 2026-06-16 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 7/7 |
| 678 | [50대이상이 들으면 기분좋아지는 7080노래모음, 베스트 7080노래모음, 광고 없는 7080 좋은노래 모음](https://www.youtube.com/watch?v=L0rtQ0ZFr7o) | VibeTune | 11,400 | 576,558 | 50.6 | ×466.5 | 3,549.9 | 72.7분 | 2026-05-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 85/85 |
| 679 | [Fall Asleep In 3 Minutes 😴 Mozart For Babies 💤 Extra Relaxi…](https://www.youtube.com/watch?v=P87LUaYiD34) | Mother & Baby… | 17,700 | 894,817 | 50.5 | ×23.8 | 15,489.3 | 150.1분 | 2026-08-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 680 | [[감동음악]🎵듣는 순간 가슴이 먹먹해진다… 김호중 × 이애숙 《나의 조국은》 감동 실황 ∣ 천상의 목소리 …](https://www.youtube.com/watch?v=FAMrq6SXxys) | 🎧 Sound Rest | 2,710 | 135,857 | 50.1 | ×463.7 | 828.4 | 4.5분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 612/613 |
| 681 | [Ithaca](https://www.youtube.com/watch?v=8DVfI_Muv_A) | Ludwig Görans… | 43,300 | 2,169,396 | 50.1 | ×4.5 | 22,155.7 | 5.7분 | 2026-07-16 | 13. OST·사운드트랙 | 음악 | 설명 | 0/796 |
| 682 | [Deep work focus music for productivity ~ Ambient study musi…](https://www.youtube.com/watch?v=Bk-0NZHRPFA) | Work Mode Aud… | 11,100 | 552,593 | 49.8 | ×107.4 | 4,053.4 | 91분 | 2026-06-08 | 3. 공부·집중·작업 | 음악 | 설명 | 254/256 |
| 683 | [Morning Coffee & Relaxing Italian Music ∣ Mediterranean Vib…](https://www.youtube.com/watch?v=Uu_fZV9xXRM) | Onda di Relax | 25,900 | 1,275,965 | 49.3 | ×502.9 | 7,126.7 | 141.2분 | 2026-04-26 | 4. 카페·매장·라운지 | 음악 | 설명 | 141/141 |
| 684 | [Beautiful September Autumn Forest 4K 🍁 Peaceful Nature Soun…](https://www.youtube.com/watch?v=RJma4cwfqIY) | Nature's Have… | 2,730 | 134,349 | 49.2 | ×33.5 | 3,280.2 | 154.8분 | 2026-09-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 49/50 |
| 685 | [Lightning — Romantic Ambient Pop & 80s Synth Ballad ∣ Thoma…](https://www.youtube.com/watch?v=2x_gLGrUdoY) | Thomas J. Cole | 4,040 | 196,106 | 48.5 | ×81.1 | 6,801.6 | 5분 | 2026-09-23 | 12. 커버·노래 부르기 | 음악 | 설명 | 94/97 |
| 686 | [Romantic Era Adagios (Cello, Violin & Piano) — Most Beautif…](https://www.youtube.com/watch?v=Dd3djaUS3Fw) | Classical Ada… | 13,100 | 635,479 | 48.5 | ×1,445.9 | 4,072.5 | 256.8분 | 2026-05-19 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 187/187 |
| 687 | [“사는 게 힘들수록, 그 시절 노래가 더 그립습니다…”｜가슴 저리는 7080 추억의 명곡모음｜슬로우 블루스…](https://www.youtube.com/watch?v=uS61Sf1rAsQ) | 추억의 멜로디 | 4,300 | 207,809 | 48.3 | ×20.8 | 2,908.2 | 85.9분 | 2026-08-11 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 84/86 |
| 688 | [𝑃𝑙𝑎𝑦𝑙𝑖𝑠𝑡 느좋 도우인 플리](https://www.youtube.com/watch?v=muaiYrT3glM) | 진구달려 | 5,710 | 275,729 | 48.3 | ×5.5 | 3,445.6 | 14.7분 | 2026-08-03 | 기타 | 플레이리스트·모음 | 없음 | 52/55 |
| 689 | [9 Adagios in Romantic Style ∣ AI Music ∣ Cello & Piano](https://www.youtube.com/watch?v=N4UaovHvFPE) | Vesper Classi… | 16,400 | 790,814 | 48.2 | ×1,245.4 | 4,655.3 | 28분 | 2026-05-05 | 14. AI 음악 | AI 음악 | 설명 | 421/421 |
| 690 | [【Playlist】Shamisen Rock You’ll Want to Replay ∣ Female Voca…](https://www.youtube.com/watch?v=skyHiOHKUJI) | Geisha Girl | 15,200 | 729,613 | 48.0 | ×61.8 | 4,369.0 | 111.1분 | 2026-05-08 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 193/193 |
| 691 | [💖 최고의 트로트 명곡 30곡 ∣ 중장년 애창곡 ∣ 운전·카페·휴식 음악 ∣ 안동역에서 미운사랑 홍시 진또…](https://www.youtube.com/watch?v=Tbtq8pWkeEk) | 달빛머문 새벽세시 | 1,040 | 49,879 | 48.0 | – | 1,856.7 | 98.2분 | 2026-09-25 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 6/6 |
| 692 | [ᴘʟᴀʏʟɪsᴛ ∣ 🌊푸른 바다처럼 시원한 7월 여돌 뮤직비디오 플리 ∣ 여름 청량 최신 걸그룹 인기곡 뮤…](https://www.youtube.com/watch?v=2EbdnZvOSwc) | 마쁠(MA-PLE·KPO… | 24,800 | 1,186,577 | 47.9 | ×7.3 | 12,764.7 | 127.2분 | 2026-07-21 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 84/84 |
| 693 | [[KPOP playlist] 난리도 아닌 감다살 케이팝 노동요](https://www.youtube.com/watch?v=AnsLD0Klc6s) | 오이는빼주세요 | 13,100 | 624,377 | 47.7 | ×53.4 | 4,702.0 | 59.1분 | 2026-06-11 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 47/47 |
| 694 | [업장을 소멸하고 복을 부르는 천수경 노래 ∣ 힐링 불교 음악](https://www.youtube.com/watch?v=AT2MDa7WctU) | 진서연의 세월한곡 | 9,450 | 448,162 | 47.4 | ×1,339.8 | 2,498.5 | 14.1분 | 2026-04-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 391/393 |
| 695 | [Bamboo Water + Tibetan Zen Sounds ∣ Cleanse Aura & Space ∣ …](https://www.youtube.com/watch?v=oA7EmuZ7JCU) | Serene Vibes | 15,700 | 743,366 | 47.4 | ×74.7 | 4,565.2 | 184.3분 | 2026-05-12 | 1. 수면·명상·힐링 | 음악 | 설명 | 204/204 |
| 696 | [Cinematic Piano Meets Melodic Techno 🌌 ∣ Neo Classic Pulse …](https://www.youtube.com/watch?v=gSn_K5j9uB8) | Neo Classic P… | 4,720 | 222,052 | 47.0 | ×72.0 | 2,649.6 | 45.2분 | 2026-07-30 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 166/166 |
| 697 | [조용히 틀어뒀는데 끝까지 듣게 되는 노래 ㅣ오늘 고생한 당신을 위한 편안한 올드팝 라디오 ㅣ 7080 감성…](https://www.youtube.com/watch?v=ej-ck75-Nps) | Plain Pop | 4,250 | 199,584 | 47.0 | ×44.2 | 1,327.3 | 85.2분 | 2026-05-24 | 9. 가요·발라드·트로트 | 음악 | 설명 | 156/156 |
| 698 | [途中広告なし【カフェBGM】ひとり静かな喫茶店｜のんびり過ごす午後の時間｜作業用・読書・リラックス｜Cafe Musi…](https://www.youtube.com/watch?v=QgtDgADXHS4) | Kokoro Music … | 21,100 | 986,861 | 46.8 | ×48.7 | 8,293.0 | 120.9분 | 2026-06-25 | 2. 자연 소리·백색소음 | 음악 | 설명 | 166/166 |
| 699 | [카페음악 ☕ 5월의 카페에서 잔잔하게 듣기 좋은 음악 🌿 7080 카페음악모음 🎶 중년을 위한 감성 카페 …](https://www.youtube.com/watch?v=5-b-PY1I2ss) | Cozy Cafe Mus… | 3,870 | 180,351 | 46.6 | ×36.0 | 1,058.3 | 12.8분 | 2026-05-04 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 19/19 |
| 700 | [𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩 ∣ 상큼하게 톡 터지는 딸기 에이드와 느린 독서 *'~*-⋆._.-*~⋆ ∣ 카페 플리 ∣…](https://www.youtube.com/watch?v=L1E4rkvGo-Y) | BlueDot Diary | 6,520 | 303,784 | 46.6 | ×109.4 | 2,644.3 | 123.4분 | 2026-06-29 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 75/75 |
| 701 | ["सुकून भरी रातें 🌙 ∣ Romantic Hindi LoFi Songs ∣ Relaxing S…](https://www.youtube.com/watch?v=YtyLIn9mrcw) | Hindi Tuning | 25,200 | 1,171,267 | 46.5 | ×162.8 | 7,329.1 | 110분 | 2026-05-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 160/160 |
| 702 | [듣다 보면 끝까지 듣게 되는 명품 보컬 ∣ 7080 슬로우 레게・레트로 락발라드・Love Song・Vint…](https://www.youtube.com/watch?v=V9FOduIEv6w) | afterparis | 7,200 | 334,354 | 46.4 | ×25.4 | 3,001.0 | 82.8분 | 2026-07-02 | 9. 가요·발라드·트로트 | 음악 | 설명 | 183/183 |
| 703 | [[playlist] 상큼 달콤 행복의 피아노 음악🍋 아이의 정서발달을 위한 멜로디🎹 행복해지는 마법같은 영…](https://www.youtube.com/watch?v=PxIbP-Lv3EQ) | 베베집 bebe zip | 8,240 | 380,914 | 46.2 | ×48.1 | 3,358.6 | 91분 | 2026-06-30 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 0/0 |
| 704 | [비 오는 밤의 라흐마니노프 ∣ 깊고 잔잔한 아다지오 1시간](https://www.youtube.com/watch?v=HNgBqMnvUcU) | Minimal Class… | 7,640 | 352,271 | 46.1 | ×43.3 | 2,414.7 | 60.2분 | 2026-05-29 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 341/341 |
| 705 | [마음이 편안해지는 명품 아침 클래식 ㅣ듣기만 해도 행복해지는 클래식 명곡](https://www.youtube.com/watch?v=jhz1rDyH7gc) | Aria classic … | 2,510 | 114,334 | 45.5 | ×20.6 | 1,236.6 | 59.4분 | 2026-07-21 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 18/18 |
| 706 | [ㅤㅤㅤ](https://www.youtube.com/watch?v=8k5vqajrHVw) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 38,800 | 1,756,066 | 45.3 | ×316.6 | 25,872.4 | 120.7분 | 2026-08-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 4,300/4,313 |
| 707 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=lXbnhKzEQl8) | Click Bollywo… | 25,800 | 1,164,979 | 45.1 | ×8,996.0 | 15,485.1 | 8.1분 | 2026-08-08 | 3. 공부·집중·작업 | 음악 | 설명 | 73/73 |
| 708 | [마음도 휴식이 필요해요 BGM (플루트 연주) 🎵 조용한 숲과 호수의 휴식](https://www.youtube.com/watch?v=pzBSdxT3Bp4) | 느린풍경이야기 | 1,060 | 47,769 | 45.1 | ×876.5 | 316.9 | 39.6분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 21/21 |
| 709 | [🎵듣는 순간 소름… 김호중·허종훈·임경택·임창한 남성4중창 레전드 공연 ∣ 김호중의 폭발적 테너… ‘오 나…](https://www.youtube.com/watch?v=ypW1MoCFDA8) | 🎧 Sound Rest | 2,710 | 121,289 | 44.8 | ×414.0 | 804.3 | 13.9분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 182/183 |
| 710 | [𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 듣자마자 행복해질거야🍦☀️ 요즘 감성 노래 모음 ∣ 하루 종일 듣기 좋은 팝송 플레이리스트](https://www.youtube.com/watch?v=4zc4GyIQPco) | seroma room | 16,600 | 742,836 | 44.8 | ×79.5 | 5,573.1 | 599.4분 | 2026-06-11 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 62/62 |
| 711 | [Harmony Of Seasons ∣ DVE ∣ Ultimate Classical Piano Collect…](https://www.youtube.com/watch?v=P4H9CSSCuQg) | DVE | 2,360 | 104,470 | 44.3 | ×2,429.5 | 2,047.1 | 15.8분 | 2026-09-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 180/183 |
| 712 | [Craig David – INSOMNIA 🌙 ∣ Deep Bass EDM Remix ∣ Feel The N…](https://www.youtube.com/watch?v=hymSZZ0mX5U) | musik story🎧 | 12,000 | 529,808 | 44.1 | ×52.2 | 7,437.5 | 4분 | 2026-08-12 | 11. 힙합·R&B·EDM | 음악 | 설명 | 76/77 |
| 713 | [여인 – 우리 가슴속 깊이 박혀 있던 그 노래, 듣는 순간 그 시절로 돌아갑니다, 이어폰 필수… 👉 첫 소…](https://www.youtube.com/watch?v=yQSP0R8pDqg) | 혼자 듣는 노래 | 8,130 | 358,319 | 44.1 | ×59.6 | 3,159.3 | 109.5분 | 2026-06-30 | 기타 | 음악 | 설명 | 104/104 |
| 714 | [Deep Work Music ~ Midnight City Ambience for Deep Focus ~ C…](https://www.youtube.com/watch?v=czMO-L42nnc) | Focus Room | 25,100 | 1,104,687 | 44.0 | ×126.5 | 6,870.4 | 132.4분 | 2026-05-14 | 2. 자연 소리·백색소음 | 음악 | 설명 | 112/113 |
| 715 | [TIME ALONE WITH GOD - Soaking worship instrumental ∣ Prayer…](https://www.youtube.com/watch?v=uqC91GqvvQg) | Calm Divine F… | 21,100 | 920,325 | 43.6 | ×54.0 | 10,249.7 | 67.1분 | 2026-07-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 515/520 |
| 716 | [[𝑬𝑽𝑬𝑹𝒀𝑫𝑨𝒀, 𝑷𝑰𝑨𝑵𝑶] 몽글몽글🩵 여름에 듣기 좋은 피아노 연주곡 10시간 모음 (중간광고없음, …](https://www.youtube.com/watch?v=5lWOn3zHsI0) | Everyday, Pia… | 5,430 | 236,722 | 43.6 | ×10.2 | 1,761.7 | 614.5분 | 2026-06-09 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 20/20 |
| 717 | [Playlist ∣ 매장을 세련되게 만드는 명품 그루브 🖤🎧 ∣ HIPHOP∙R&B MIX ∣ 매장음악∙카…](https://www.youtube.com/watch?v=h84x1mhg5C4) | hipnb groove | 4,550 | 198,383 | 43.6 | ×31.2 | 1,157.5 | 152.2분 | 2026-05-03 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 32/32 |
| 718 | [사랑했어요 - 김현식 ∣ 가슴 깊이 남은 진한 그리움과 아련한 추억 #윤가연 COVER](https://www.youtube.com/watch?v=2VFOp-WbafE) | GAYEON YOON | 28,600 | 1,244,083 | 43.5 | ×50.4 | 8,760.6 | 5.2분 | 2026-06-02 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 115/117 |
| 719 | [유어아너 허남준이 말아주는 나쁜남자 PLAYLIST 🖤 ㅣ A Dark Bad Boy Playlist In…](https://www.youtube.com/watch?v=0YV2RKwLls0) | 허남준 팬페이지 허남준독… | 5,000 | 217,387 | 43.5 | – | 1,544.9 | 18.4분 | 2026-06-03 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 493/493 |
| 720 | [The Last Dance Before Dawn ∣ Dark Neoclassical music](https://www.youtube.com/watch?v=wy2IX-zmEXo) | Kingdom of Da… | 13,900 | 602,887 | 43.4 | ×155.1 | 3,832.1 | 107.1분 | 2026-05-18 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 653/656 |
| 721 | [[Playlist] 기분 좋아지는 산뜻한 유럽 아침 앙상블 ∣ Morning Classical Ensemb…](https://www.youtube.com/watch?v=fdPFoR4XjNQ) | okply | 15,500 | 670,047 | 43.2 | ×85.0 | 4,113.9 | 80.8분 | 2026-05-12 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 325/327 |
| 722 | [👉듣는 순간 마음이 차분해지는 성경 찬양 ∣ Calm Scripture Worship (공부·집중·묵상)](https://www.youtube.com/watch?v=kdn9w1w3v_I) | 생명타임 | 4,690 | 202,347 | 43.1 | ×60.4 | 1,132.3 | 227.7분 | 2026-04-26 | 15. CCM·찬양·국악… | 음악 | 설명 | 178/179 |
| 723 | [[Playlist] 로제 재즈 플레이리스트 🌹🎷 ∣ ROSÉ Jazz Playlist ∣ 재즈 커버](https://www.youtube.com/watch?v=ZqL7hDxAlis) | PLYINK 플링크 | 8,050 | 346,392 | 43.0 | ×5.3 | 4,375.5 | 110.8분 | 2026-08-04 | 7. 재즈·보사노바 | 커버·직접 부른 노래 | 설명 | 116/117 |
| 724 | [Beautiful girl and inspiring piano music that help you love…](https://www.youtube.com/watch?v=6oZwrM-i8XU) | Benjamin Elie | 295 | 12,685 | 43.0 | ×1.8 | 366.3 | 4.8분 | 2026-09-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 4/4 |
| 725 | [Golden Horizon ∣ Cinematic Sci-Fi Ambient Music — Utopian F…](https://www.youtube.com/watch?v=QcVRYKcCIZ8) | Cosmic Infini… | 3,060 | 131,444 | 43.0 | ×156.7 | 797.4 | 13.2분 | 2026-05-10 | 3. 공부·집중·작업 | 음악 | 설명 | 109/109 |
| 726 | [Sneher Chayay Bhalobasay - স্নেহের ছায়ায় ভালোবাসায় ∣∣ Relax…](https://www.youtube.com/watch?v=uWinY9AA2Z8) | Aruhi Media | 26,500 | 1,138,184 | 43.0 | ×1,093.4 | 6,366.4 | 5.7분 | 2026-04-26 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 108/108 |
| 727 | [The Quiet Night Medieval Village ∣ Relaxing Fantasy Medieva…](https://www.youtube.com/watch?v=dJ5VtIE3kwU) | Fantasy Medie… | 20,700 | 887,751 | 42.9 | ×131.5 | 7,473.0 | 146.7분 | 2026-06-25 | 3. 공부·집중·작업 | 음악 | 설명 | 189/191 |
| 728 | [그냥 틀어두기 좋은 감성 팝송 ☕🌿 12hr Cozy Cafe BGM • ep.110](https://www.youtube.com/watch?v=sDuu-v_gUjw) | winterbudz | 5,370 | 230,141 | 42.9 | ×61.9 | 1,400.1 | 699.6분 | 2026-05-10 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 300/300 |
| 729 | [Relaxing Cha-Cha-Cha Swing on the Beautiful Beach – Latin R…](https://www.youtube.com/watch?v=f3zh_3lwiEI) | Grateful For … | 16,800 | 719,030 | 42.8 | ×633.5 | 4,497.5 | 63.8분 | 2026-05-15 | 기타 | 정보·해설 | 설명 | 194/195 |
| 730 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 틀기만 해도 기분이 좋아지는 플리☀️🌿 (광고없음) 국내 노래 모음](https://www.youtube.com/watch?v=9aeCgBBnmYI) | 오늘의 플리 | 6,700 | 286,503 | 42.8 | ×30.6 | 1,724.9 | 617.4분 | 2026-05-09 | 기타 | 플레이리스트·모음 | 없음 | 27/27 |
| 731 | [그레고리오성가*한국어* 주여 자비를 베푸소서 #가톨릭성가#그레고리오성가#성가미사#기도음악#묵상음악#천주교성…](https://www.youtube.com/watch?v=9qbqShZRPYw) | DIMOTEO RECOR… | 4,450 | 189,419 | 42.6 | ×101.4 | 1,101.5 | 82.1분 | 2026-05-03 | 15. CCM·찬양·국악… | 음악 | 설명 | 516/521 |
| 732 | [Clear Negative Thoughts: Krishna Flute & Sitar to Quiet Min…](https://www.youtube.com/watch?v=ugG3qiHWEak) | Healing Raga … | 23,700 | 1,003,045 | 42.3 | ×72.5 | 13,875.1 | 65.3분 | 2026-08-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 144/144 |
| 733 | [그냥 틀어만 놓아도 아침까지 푹 자요/ 이명치료효과/ 듣자마자 바로 잠오는 폭우 빗소리/ 깊은 잠을 위한 …](https://www.youtube.com/watch?v=ASEKIYKzzEc) | 비오는날 ASMR | 21,800 | 921,907 | 42.3 | ×52.4 | 5,151.5 | 180.8분 | 2026-04-26 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 162/167 |
| 734 | [전율 돋는 폭발적 감성 ⚡ 대한민국 락발라드 끝판왕! M.C The Max '잠시만 안녕' 커버 ∣ 김별이](https://www.youtube.com/watch?v=QK3Mxw--VFg) | 김별이 | 5,800 | 244,295 | 42.1 | ×48.2 | 4,408.4 | 5.4분 | 2026-08-27 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 32/34 |
| 735 | [일상에 틀어 놓는 잔잔한 찬송가 연속 듣기ㅣ어쿠스틱 편곡ㅣ3시간ㅣ중간 광고 없음ㅣ내 영혼이 은총 입어·내 …](https://www.youtube.com/watch?v=EwY1Z6_6H3I) | ALL THAT HYMN… | 7,240 | 304,747 | 42.1 | ×113.2 | 6,069.8 | 197.6분 | 2026-09-02 | 15. CCM·찬양·국악… | 커버·직접 부른 노래 | 설명 | 152/159 |
| 736 | [ENIGMA VOICES IN THE DARK 🌑 Mystical Ambient Music](https://www.youtube.com/watch?v=fOqrhVkQOh4) | The Sound Pal… | 9,630 | 401,108 | 41.6 | ×123.1 | 2,452.2 | 8분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 169/170 |
| 737 | [Relaxing Piano Music for Inner Peace, Meditation, Stress Re…](https://www.youtube.com/watch?v=dljV0oqDztU) | Celestial Rel… | 11,400 | 473,725 | 41.5 | ×145.7 | 8,789.8 | 127.7분 | 2026-08-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 236/244 |
| 738 | [The Sound Your Brain Needs Right Now 🌿 Deep Healing Music ∣…](https://www.youtube.com/watch?v=rQ5bIFKQoUc) | Osen Moonlight | 10,100 | 418,750 | 41.5 | ×131.5 | 7,245.9 | 107분 | 2026-08-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 128/165 |
| 739 | [Ancient Chinese Zen Music🍃Bamboo Flute, Erhu & Guzheng🍃Rela…](https://www.youtube.com/watch?v=CKQuvdIKXgU) | Sound to Peac… | 45,900 | 1,893,554 | 41.2 | ×799.1 | 11,750.9 | 184.4분 | 2026-05-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 592/594 |
| 740 | [@노노뮤직#피아노협주곡 #힐링음악 #감성피아노 #클래식음악 #휴식음악#명상음악 #잔잔한음악 #오케스트라 #…](https://www.youtube.com/watch?v=aLyOUOXr5F4) | 노노스튜디오 | 462 | 18,976 | 41.1 | ×115.7 | 130.9 | 30분 | 2026-05-30 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 9/9 |
| 741 | [디지몬 OST - 날 지켜줘 (벅차오르는 파워 락 발라드 어레인지 커버) ∣ GrangChe.Ver](https://www.youtube.com/watch?v=iWfeWC28USw) | GrangChe | 21,500 | 882,548 | 41.0 | ×82.5 | 5,542.7 | 4.8분 | 2026-05-16 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 233/235 |
| 742 | [ray 【カフェ風アレンジ】 / Remix / 超かぐや姫！](https://www.youtube.com/watch?v=js2syT4l9lc) | Remix中谷 | 5,530 | 225,905 | 40.9 | ×2.6 | 1,644.0 | 12분 | 2026-06-06 | 기타 | 정보·해설 | 설명 | 162/162 |
| 743 | [듣자마자 학창시절 떠오르는 노래 🎧 싸이월드 감성 PART 4](https://www.youtube.com/watch?v=F-0JE3Byo9U) | 소꿀 TV | 18,200 | 740,647 | 40.7 | – | 4,562.2 | 82.6분 | 2026-05-12 | 기타 | 플레이리스트·모음 | 설명 | 50/51 |
| 744 | [the best classical music for concentration ∣ deep meditatio…](https://www.youtube.com/watch?v=ViZf4iovMMk) | StillSpace | 32,800 | 1,327,024 | 40.5 | ×321.2 | 8,075.2 | 61.4분 | 2026-05-11 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 608/608 |
| 745 | [🎧"세상에서 가장 애절한 목소리" 한 편의 영화 같은 무대, 그리고 가슴을 울리는 목소리…🎙️ 김정호 - …](https://www.youtube.com/watch?v=tjA0yWEZnu8) | 가슴을 울리는 락카페 | 10,900 | 431,825 | 39.6 | ×54.5 | 2,670.7 | 4.4분 | 2026-05-13 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 | 90/90 |
| 746 | [Fresh Mind Relaxing 💗 ∣ Slowed + Reverb Lofi Mix for Calm, …](https://www.youtube.com/watch?v=70p4fSeLZ3I) | Vansh Lofi | 29,200 | 1,155,307 | 39.6 | – | 8,206.8 | 15분 | 2026-06-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 46/46 |
| 747 | [백 번을 들어도 후회없을 노래🎵트로트 거친 보이스 @1980통기타 음악 @1980guitar playlis…](https://www.youtube.com/watch?v=ZVTFRwA3r14) | 1980통기타 | 11,900 | 469,049 | 39.4 | ×53.2 | 4,531.9 | 29.9분 | 2026-07-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 107/108 |
| 748 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 우린 아직 흑백영화처럼 사랑하고](https://www.youtube.com/watch?v=71_AXp38B7M) | 세봄 | 14,300 | 562,118 | 39.3 | ×13.7 | 3,740.1 | 17.1분 | 2026-05-25 | 기타 | 플레이리스트·모음 | 설명 | 28/29 |
| 749 | [Rest Tonight In God's Love ∣ Christian Deep Sleep Worship M…](https://www.youtube.com/watch?v=nzc_yRoaBRI) | Midnight Sanc… | 22,200 | 855,269 | 38.5 | ×101.6 | 9,526.1 | 122.5분 | 2026-07-24 | 15. CCM·찬양·국악… | 음악 | 설명 | 332/334 |
| 750 | [途中広告なし【カフェBGM】涼やかな夏カフェ｜木漏れ日の、心ほどける森カフェ時間｜作業用・読書・リラックス｜Cafe …](https://www.youtube.com/watch?v=3QKdiHlK6c4) | Kokoro Music … | 21,100 | 804,510 | 38.1 | ×39.7 | 8,558.7 | 122.5분 | 2026-07-20 | 2. 자연 소리·백색소음 | 음악 | 설명 | 73/73 |
| 751 | [[No Ads] Uplifting Morning Piano Music 🌿 ∣ Fresh & Positive…](https://www.youtube.com/watch?v=D8dWbYNFXKc) | Elise Piano ∣… | 24,900 | 944,391 | 37.9 | ×46.7 | 8,713.3 | 183.7분 | 2026-07-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 123/127 |
| 752 | [Oscar & Deep - Feeling Flow](https://www.youtube.com/watch?v=b_DXB1Dj4l8) | Oscar & Deep | 24,400 | 921,571 | 37.8 | ×32.6 | 5,524.1 | 7.5분 | 2026-05-08 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 90/90 |
| 753 | [Dreams Never Sleep （映画『仮面ライダーゼッツ...](https://www.youtube.com/watch?v=9nOX0zxrLfw) | YUTA - Topic | 24,300 | 916,434 | 37.7 | – | 10,103.5 | 4.4분 | 2026-07-23 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 754 | [Soulful Sufi Ghazal - सफर की धूप में साया तलाशते रह गए ∣ He…](https://www.youtube.com/watch?v=JI1OFbt7jRM) | SOUL VIBES IN… | 30,000 | 1,123,391 | 37.5 | ×17.5 | 7,216.7 | 6.4분 | 2026-05-19 | 기타 | 정보·해설 | 설명 | 345/346 |
| 755 | [🪷 이 노래 들으면 막힌 재물운이 술술 풀립니다 ∣ 부처님 대운 명호·진언 13곡 ∣ 관세음·지장·아미타 …](https://www.youtube.com/watch?v=ztFLgJ5idWI) | 연꽃법음 | 3,540 | 131,665 | 37.2 | ×148.0 | 815.7 | 55.7분 | 2026-05-13 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 827/827 |
| 756 | [hyper-focus. ∣ deep house music for coding](https://www.youtube.com/watch?v=uNw_a7HFwvg) | deep archive | 25,200 | 932,572 | 37.0 | ×93.8 | 6,886.7 | 148.4분 | 2026-06-08 | 3. 공부·집중·작업 | 음악 | 설명 | 274/275 |
| 757 | [【ケルト音楽】家事スイッチが入る🌿 朝の光が気持ちいいBGM｜Relax · Cafe Time](https://www.youtube.com/watch?v=TqiJnA1qm4s) | よもぎの作業用BGM | 12,400 | 458,625 | 37.0 | ×42.0 | 3,542.7 | 63.3분 | 2026-06-14 | 4. 카페·매장·라운지 | 음악 | 설명 | 172/172 |
| 758 | [기분이 산뜻해지는 재즈 찬송가 ∣ Hymn Jazz Playlist ∣ 공부·휴식·카페 BGM [2H] (…](https://www.youtube.com/watch?v=AZCxtUAYrUw) | DearHymn | 11,800 | 436,188 | 37.0 | ×10.6 | 2,590.7 | 120.5분 | 2026-05-06 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 107/107 |
| 759 | [Best Acoustic Songs of the 80s 🎸 Romantic Classics & Nostal…](https://www.youtube.com/watch?v=9tAdobkt1N0) | 80s Guitar Lo… | 23,800 | 877,854 | 36.9 | ×11.8 | 13,021.5 | 58.5분 | 2026-08-15 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 115/124 |
| 760 | [Music for meditation, relaxation focus vibe ∣ deep sleep ∣ …](https://www.youtube.com/watch?v=Gsenq8igMJ0) | Healer of Bro… | 9,070 | 332,180 | 36.6 | ×704.5 | 1,899.5 | 61.5분 | 2026-04-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 192/192 |
| 761 | [Healing Music for Anxiety, Fears and Depression 🌿 Heals the…](https://www.youtube.com/watch?v=_SGd39jlrR8) | Peaceful Natu… | 2,920 | 106,764 | 36.6 | ×74.9 | 1,463.7 | 99.2분 | 2026-08-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 60/60 |
| 762 | [Saxophone Love Songs ❤️ Best Romantic Saxophone Covers ∣ Re…](https://www.youtube.com/watch?v=Uea_DclFKjw) | Sax Chill Vib… | 27,700 | 1,011,193 | 36.5 | ×12.5 | 13,820.6 | 61분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 97/98 |
| 763 | [Barbaad (Dream Rock Remix) ∣ Soulful Atmospheric Cover](https://www.youtube.com/watch?v=FGvMCTLKFjo) | Dhun Tadka | 2,890 | 104,936 | 36.3 | ×22.9 | 622.2 | 4.8분 | 2026-05-06 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 21/21 |
| 764 | [A Morning at a Paris Café, Feeling Just a Little Lighter ∣ …](https://www.youtube.com/watch?v=OlrHsQ9QexE) | lento | 20,300 | 736,818 | 36.3 | ×77.9 | 4,120.9 | 233.7분 | 2026-04-26 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 116/116 |
| 765 | [𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 ∣ Vinyl Jazz Hiphop ∣ TOKYO ∣ Nujabes / MF Doom / …](https://www.youtube.com/watch?v=2bEmWCwdCds) | ICYFOG | 45,500 | 1,646,807 | 36.2 | ×119.2 | 13,352.6 | 206.5분 | 2026-06-21 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 102/102 |
| 766 | ["매력있다 이 음색"#휴식음악#7080노래#어쿠스틱음악#힐링음악#수면음악#카페음악#7080발라드#명상음악#…](https://www.youtube.com/watch?v=CG3XI3D6gHg) | 7080 마로니에 통기타… | 390 | 14,114 | 36.2 | ×153.4 | 84.2 | 40.9분 | 2026-05-07 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 20/20 |
| 767 | [Sweetest Best Friends Lullaby 🐶🐱💤∣ Calm Sleep Music for Kid…](https://www.youtube.com/watch?v=P5zkPSvY368) | Kidz Wonder T… | 20,000 | 723,823 | 36.2 | ×1.9 | 4,268.3 | 9분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 768 | [JESUS CALM MY HEART - Instrumental Worship Music For Prayer](https://www.youtube.com/watch?v=GKDVqIGZ5GI) | One Thing | 17,700 | 637,668 | 36.0 | ×67.5 | 4,285.7 | 63.4분 | 2026-05-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 186/188 |
| 769 | [이 세상 미련 없이 가련다 [국악 트로트] 가슴 시린 중년 트토르](https://www.youtube.com/watch?v=XcyHeiPdmDc) | 인생트로트 라운지 | 4,140 | 148,908 | 36.0 | – | 934.7 | 5.8분 | 2026-05-16 | 9. 가요·발라드·트로트 | 음악 | 설명 | 19/19 |
| 770 | [music for overthinkers ∣ felt piano & cello for deep focus](https://www.youtube.com/watch?v=EZeW4Sfy8CE) | OTIUM | 27,500 | 986,372 | 35.9 | ×123.2 | 9,416.5 | 60.8분 | 2026-07-09 | 3. 공부·집중·작업 | 음악 | 설명 | 428/430 |
| 771 | [🎵 신나는 복고댄스 Playlist ∣ 추억 감성 뉴트로 댄스곡 모음🎧](https://www.youtube.com/watch?v=WjxmNnlQ8LU) | 7080 정미의 가요방 | 9,040 | 322,587 | 35.7 | ×21.5 | 1,967.3 | 15분 | 2026-05-11 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 217/217 |
| 772 | ["술 한잔 생각나는 깊은 목소리..." 첫 소절 부터 아련해지는 님은 먼 곳에(블루스 Ver.)](https://www.youtube.com/watch?v=M-8Z69t7Smo) | 세월블루스 | 20,900 | 742,836 | 35.5 | ×7.4 | 4,320.9 | 4.4분 | 2026-05-03 | 기타 | 한 곡 | 설명 | 193/194 |
| 773 | [Snowy Russian Night ❄️ Tchaikovsky-Inspired Winter Orchestr…](https://www.youtube.com/watch?v=R3xYX9LJ_hs) | 모노로그 레코드 | 25,600 | 907,398 | 35.5 | ×51.3 | 5,740.9 | 61분 | 2026-05-17 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 1,150/1,158 |
| 774 | [Bach Style ∣ 마음이 편안해지는 바흐풍 잔잔한 클래식 🌿 [중간광고없음] ∣ 힐링음악, 일상 BG…](https://www.youtube.com/watch?v=hbmQRFw1InE) | Elise Piano ∣… | 24,900 | 880,838 | 35.4 | ×43.6 | 5,358.7 | 130.9분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 341/353 |
| 775 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 텐션 MAX🔥핫한 걸그룹 인기곡 노동요 뮤비 플리☀️여자아이돌 노래모음 ∣ 4K UHD](https://www.youtube.com/watch?v=u7Mu1aDSaR4) | 마쁠(MA-PLE·KPO… | 24,800 | 871,555 | 35.1 | ×5.3 | 5,997.0 | 135.4분 | 2026-05-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 74/74 |
| 776 | [AMAPIANO MIX 2026 ∣ 🔥DEEP HOUSE MUSIC VIBES ∣ BEST AFRO PIA…](https://www.youtube.com/watch?v=pyDSBs4URas) | YANOS NATION | 22,600 | 790,949 | 35.0 | ×360.8 | 5,211.5 | 20.9분 | 2026-05-23 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 160/160 |
| 777 | [붓꽃잎 편지∣[감성 음악]∣댄스 트로트∣서정적인 트로트](https://www.youtube.com/watch?v=K82Wh68Jvjc) | MusubiRain | 1,310 | 45,795 | 35.0 | ×116.2 | 462.8 | 5분 | 2026-07-15 | 9. 가요·발라드·트로트 | 음악 | 설명 | 26/26 |
| 778 | [𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩 ∣ 아말피 테라스에서 봉골레와 와인 한 잔 ∣ 𝘚𝘰𝘧𝘵 𝘉𝘰𝘴𝘴𝘢 𝘑𝘢𝘻𝘻🍋🥂 ∣ 카페 플…](https://www.youtube.com/watch?v=ZgR4pGSybaw) | BlueDot Diary | 6,520 | 227,693 | 34.9 | ×82.0 | 2,170.2 | 142.8분 | 2026-07-09 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 45/45 |
| 779 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 여름 새벽향 낭만 플리](https://www.youtube.com/watch?v=9qwdolh_Jow) | 세봄 | 14,300 | 497,352 | 34.8 | ×12.1 | 3,496.5 | 18.9분 | 2026-06-02 | 기타 | 플레이리스트·모음 | 설명 | 17/17 |
| 780 | [쏟아지는 빗소리에 복잡한 생각은 내려 놓으세요 ∣ 수면유도 백색소음 힐링 ASMR](https://www.youtube.com/watch?v=9TqDVzWADgQ) | Cozy Rainy Da… | 9,320 | 323,254 | 34.7 | ×43.0 | 2,345.3 | 360.1분 | 2026-06-06 | 1. 수면·명상·힐링 | 자연 소리·백색소음 | 설명 | 97/102 |
| 781 | [【夜のリラックスBGM】星空にひたるだけの夜。/A night in starlight｜ピアノ 1時間](https://www.youtube.com/watch?v=wIaFkPnk9oA) | FeelTone | 26,200 | 908,315 | 34.7 | ×126.8 | 5,167.0 | 62분 | 2026-04-29 | 기타 | 정보·해설 | 설명 | 179/179 |
| 782 | [Rest Your Mind ∣ Soothing Indian Classical Music for Stress…](https://www.youtube.com/watch?v=56ymDCWXGZk) | Essential Ind… | 19,100 | 661,884 | 34.6 | ×452.4 | 4,766.7 | 17.7분 | 2026-06-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 93/93 |
| 783 | [Persian & Spanish Fusion Relaxing Music 4K ∣ Persian Gulf &…](https://www.youtube.com/watch?v=UH3bfZ6Rb9E) | WolfRelaxMusi… | 25,400 | 875,698 | 34.5 | ×275.2 | 5,040.0 | 63.7분 | 2026-05-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 857/864 |
| 784 | [Oscar & Deep - Closer To My Dreams](https://www.youtube.com/watch?v=YVYkI9z2Evk) | Oscar & Deep | 24,400 | 839,398 | 34.4 | ×29.9 | 9,245.7 | 9.8분 | 2026-07-23 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 45/45 |
| 785 | ["첫 소절 듣자마자 가슴 한쪽이 먹먹해지네요.." 세월 묻은 목소리로 다시부른 연인(블루스 Ver.)](https://www.youtube.com/watch?v=y7CUK-q-f1s) | 세월블루스 | 20,900 | 715,535 | 34.2 | ×7.1 | 4,091.0 | 4.6분 | 2026-04-30 | 기타 | 정보·해설 | 설명 | 274/274 |
| 786 | [임영웅, 신곡 〈그대 행복이면 됐소〉 발표! 그대만 행복하면 됐소…](https://www.youtube.com/watch?v=p8MCdXUSFmI) | 감성트롯다방 | 4,910 | 166,913 | 34.0 | ×143.1 | 1,515.7 | 6.4분 | 2026-07-04 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 262/265 |
| 787 | [2000~2010 K-POP 감성 모음 🎶 ∣ 듣자마자 떠오르는 그 시절 노래들 – Geuri-um Stu…](https://www.youtube.com/watch?v=9CHBQsxSNa4) | Geuri-um Stud… | 8,720 | 295,892 | 33.9 | ×77.4 | 1,686.8 | 87.5분 | 2026-04-29 | 10. 팝송·K팝·J팝 | 음악 | 설명 | 41/41 |
| 788 | [Zulu Spirit — African Spiritual Ambient Music for Healing &…](https://www.youtube.com/watch?v=cOLt_w3nBx4) | Echo Sanctum | 9,200 | 310,000 | 33.7 | ×22.8 | 1,920.3 | 180.8분 | 2026-05-13 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 228/229 |
| 789 | [[Playlist] 라흐마니노프의 깊은 그리움 ∣ 멀리서 들려오는 서정적인 선율 (Rachmaninoff …](https://www.youtube.com/watch?v=vcpBmyFBJos) | The Clavis | 19,800 | 662,578 | 33.5 | ×28.4 | 5,280.8 | 97.2분 | 2026-06-18 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 551/555 |
| 790 | [Chinese Zen Music🎵: Bamboo flute, erhu & Guzheng ∣ Relaxing…](https://www.youtube.com/watch?v=6UtPuJcUsyI) | ZenFlute | 32,700 | 1,086,384 | 33.2 | ×156.9 | 7,603.8 | 90.2분 | 2026-06-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 744/750 |
| 791 | [주부들이 엄선한 감성 팝송 Best 26 ∣ EverPop 레트로 팝 컬렉션 ∣ 7080 올드팝송 ∣ 추억…](https://www.youtube.com/watch?v=JZH9pZhtl9I) | 추억의 올드팝 EverP… | 15,800 | 522,696 | 33.1 | ×23.5 | 5,563.4 | 97.8분 | 2026-07-20 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 125/129 |
| 792 | [🌺 सर्व देवता हरेक बिहानको मन्त्र ∣ Morning Nepali Bhakti So…](https://www.youtube.com/watch?v=U984EoUC8Jo) | Bhajan Hub Ne… | 33,400 | 1,103,172 | 33.0 | ×155.0 | 7,316.9 | 13.6분 | 2026-05-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 760/761 |
| 793 | [A Quiet Rainy Afternoon in a 1958 Vermont Town ∣ Relaxing V…](https://www.youtube.com/watch?v=zjgFke-YGZk) | The Serene So… | 34,000 | 1,118,285 | 32.9 | ×60.0 | 6,467.3 | 64분 | 2026-05-02 | 기타 | 음악 | 설명 | 1,843/1,848 |
| 794 | [비 오는 날 듣기 좋은 화란 락발라드 모음 Vol.1 ☔7080 감성 Cover Collection](https://www.youtube.com/watch?v=c4hjZfzxkMM) | ​화란사운드® ∣ 보컬화란 | 16,800 | 551,975 | 32.9 | ×16.2 | 3,784.7 | 34분 | 2026-05-29 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 285/286 |
| 795 | [Best Romantic Flute Instrumental Collection ❤️ ∣ Tum Aa Gay…](https://www.youtube.com/watch?v=taYeLCeWCd8) | Mansa Music W… | 10,400 | 338,559 | 32.5 | ×153.1 | 2,838.6 | 19.6분 | 2026-06-25 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 84/84 |
| 796 | [𝐈𝐬 𝐭𝐢𝐦𝐞 𝐭𝐨 𝐫𝐞𝐥𝐚𝐱⎛˶’ᵕ’˶ ⎞♡.*･ﾟ](https://www.youtube.com/watch?v=a7psAnInAcI) | iamnotcute유유 | 13,800 | 448,159 | 32.5 | ×73.7 | 3,058.2 | 99.8분 | 2026-05-28 | 기타 | 정보·해설 | 설명 | 223/223 |
| 797 | [하루 끝에 듣는 힐링 발라드 🎶 광고 없는 감성 명곡 모음｜백지영, 성시경, 더원, 이승기, 김필, 양파,…](https://www.youtube.com/watch?v=85w3xNdP09U) | N Melody Ball… | 23,800 | 772,677 | 32.5 | ×128.1 | 5,662.4 | 49.8분 | 2026-06-07 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 없음 | 138/138 |
| 798 | [The Beatles on Abbey Road ∣ Greatest Hits in Quartet [No Mi…](https://www.youtube.com/watch?v=VGZ-Xzu73gg) | Golden Harmony | 19,500 | 633,143 | 32.5 | ×81.3 | 5,650.7 | 114.4분 | 2026-07-02 | 기타 | 음악 | 설명 | 299/302 |
| 799 | [QUIET WITH JESUS - Instrumental Worship Music For Prayer](https://www.youtube.com/watch?v=2JsArLBjn70) | One Thing | 17,700 | 563,694 | 31.9 | ×59.7 | 4,003.8 | 60.3분 | 2026-06-03 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 119/119 |
| 800 | [조선힙합 OFFICIAL 발표곡 중 인기곡만 모았습니다.](https://www.youtube.com/watch?v=fjjiznDoNEQ) | 조선힙합 Official | 28,600 | 910,125 | 31.8 | ×123.5 | 6,534.0 | 28.4분 | 2026-06-05 | 11. 힙합·R&B·EDM | 한 곡 | 설명 | 1,039/1,051 |
| 801 | [DUNE Music for Meditation, Rest & Focus ∣ 3 Hours ∣ No Ads](https://www.youtube.com/watch?v=qTdgu2POFlw) | Empyreal Ambi… | 14,700 | 465,160 | 31.6 | ×20.0 | 6,653.2 | 180분 | 2026-08-13 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 74/78 |
| 802 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 요즘 연남동 카페에서 듣기좋은 가을 감성 팝송 𝟏𝟎시간 (중간광고없음) 🍂☕ 작업 · 휴식…](https://www.youtube.com/watch?v=asmDdv4Dfig) | With Lofi Cafe | 4,980 | 157,018 | 31.5 | ×16.9 | 6,440.2 | 647.2분 | 2026-09-27 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 15/15 |
| 803 | [Sky - 영원 ∣ 여성보컬 COVER ∣ 다시 들어도 가슴이 무너지는 명곡](https://www.youtube.com/watch?v=ETq8E35CSwk) | 연애상황극 | 11,100 | 348,054 | 31.4 | ×148.9 | 2,121.1 | 4.6분 | 2026-05-11 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 180/180 |
| 804 | [Peaceful Adventist Hymns Instrumental ∣ SDA Prayer Music fo…](https://www.youtube.com/watch?v=tj1FpWQsyCg) | Adventist Hym… | 37,500 | 1,175,853 | 31.4 | ×5.8 | 7,129.1 | 61분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 570/571 |
| 805 | [🍀 7월, 바다를 보며 들으니 이 노래 너무 좋다 ☕ 커피 한 잔과 함께하는 7080 추억의 올드팝 🎧](https://www.youtube.com/watch?v=q3iHXzi_Qn0) | 행운을담은 올드팝 | 6,160 | 191,687 | 31.1 | ×14.9 | 1,720.4 | 85.7분 | 2026-07-02 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 160/160 |
| 806 | [Anvarbek Xamroyev - Hayronman 2 (piano version)](https://www.youtube.com/watch?v=q-oZ8xry4MM) | Anvarbek Xamr… | 32,000 | 995,636 | 31.1 | – | 9,878.2 | 4.2분 | 2026-07-13 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 205/206 |
| 807 | [celestial bloom 🌿∣ dreamy piano music reflected in dreamy w…](https://www.youtube.com/watch?v=coDaaicD9zM) | She of the Va… | 11,700 | 363,420 | 31.1 | ×55.6 | 4,235.3 | 36.4분 | 2026-07-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 124/126 |
| 808 | [😭 나훈아, 아들의 노래를 듣고 끝내 눈물을 흘리다… 가족 모두가 오열한 순간25](https://www.youtube.com/watch?v=keP33Q5JU_A) | 나훈아AI Korean … | 1,450 | 44,993 | 31.0 | ×79.8 | 452.5 | 6.5분 | 2026-07-14 | 기타 | 음악 | 설명 | 25/25 |
| 809 | [Deep Work Music – CEO Mode ∣ Strategic Clarity, Controlled …](https://www.youtube.com/watch?v=uX6jCay0c6I) | Deep Idle Room | 26,300 | 814,726 | 31.0 | ×206.9 | 5,199.1 | 92.4분 | 2026-05-18 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 475/478 |
| 810 | [1 Hour Uplifting Morning Music ∣ Veena & Mridangam Indian C…](https://www.youtube.com/watch?v=7z7ol63jaGw) | Nadam | 19,300 | 596,743 | 30.9 | ×316.2 | 3,867.8 | 60.3분 | 2026-05-21 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 303/307 |
| 811 | [Study Focus Enhancement ∣ Classical Music for Deep Concentr…](https://www.youtube.com/watch?v=hUUBG_Nlwh4) | Classical Mind | 22,600 | 694,740 | 30.7 | ×283.9 | 4,531.3 | 139.4분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 184/186 |
| 812 | [[Playlist] 초록빛 싱그러운 아침에 듣는 모차르트 ∣ 독서와 사색을 위한 평온한 클래식 (Mozar…](https://www.youtube.com/watch?v=wMHsFC7-kUE) | The Clavis | 19,800 | 607,498 | 30.7 | ×26.1 | 4,451.2 | 94.3분 | 2026-06-07 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 315/319 |
| 813 | [GOD IN ME - Soaking Worship Instrumental Presence of God ∣ …](https://www.youtube.com/watch?v=L-SoDe2nKoE) | Calm Divine F… | 21,100 | 643,151 | 30.5 | ×37.2 | 3,658.6 | 63.4분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 213/213 |
| 814 | [BEST AMAPIANO MIX 2026 ∣ 1hr Of Deep House Amapiano Mix 35 …](https://www.youtube.com/watch?v=3-c885KEOaM) | AMAPIANO SANC… | 19,200 | 584,721 | 30.4 | ×42.5 | 3,834.4 | 65.5분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 137/137 |
| 815 | [막힌 운을 여는 산신기도｜백호 산신 가피로 액운소멸·복덕성취·재물운 발원](https://www.youtube.com/watch?v=ez0HnQ7tuPM) | 풍요와복덕의노래 | 2,480 | 75,429 | 30.4 | ×14.6 | 570.2 | 4.9분 | 2026-06-12 | 1. 수면·명상·힐링 | 음악 | 설명 | 584/589 |
| 816 | [Peaceful Piano with Rain Sounds 🎶 Relaxing Sleep Music & In…](https://www.youtube.com/watch?v=eUslSNm96D4) | Piano Rain Re… | 29,900 | 904,064 | 30.2 | ×63.5 | 6,629.3 | 206.7분 | 2026-06-07 | 1. 수면·명상·힐링 | 음악 | 설명 | 168/168 |
| 817 | [Chinese Sleep Music: Soft Guzheng & Ambient Pads ∣ Deep Nig…](https://www.youtube.com/watch?v=0ykSzpX6rzg) | Lotus Echo 莲之… | 16,500 | 497,631 | 30.2 | ×123.9 | 3,303.8 | 240.1분 | 2026-05-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 111/111 |
| 818 | [Chandrashekara Pahimam ∣ Lord Shiva Meditation Music ∣ Powe…](https://www.youtube.com/watch?v=9sk0msSGgfA) | Satya Devotio… | 3,390 | 102,140 | 30.1 | ×2.7 | 1,848.1 | 6.8분 | 2026-08-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 23/23 |
| 819 | [【GamePiano90min】「時の回廊」クロノ・トリガーゆっくり聴く432Hz Breathing Piano V…](https://www.youtube.com/watch?v=0sJ4qqIp3kk) | 水面こは(Minamo K… | 21,000 | 630,137 | 30.0 | ×190.2 | 3,790.3 | 90.5분 | 2026-05-09 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 200/202 |
| 820 | [잘 지내💬 아직 네가 있어 / I Hope You’re Doing Well ∣ Sad Korean Ball…](https://www.youtube.com/watch?v=PSnEIoFQB-0) | MusicSong | 7,390 | 220,334 | 29.8 | ×548.1 | 1,289.8 | 4.1분 | 2026-05-04 | 기타 | 음악 | 설명 | 94/94 |
| 821 | [샹송이 이렇게 까지 좋은줄 몰랐습니다. 아침부터 저녁까지 듣게되는 7080올드팝 샹송 ∣ 감성이 폭발한다](https://www.youtube.com/watch?v=ubP0xqEZxYo) | Midnight Melo… | 28,000 | 835,027 | 29.8 | ×240.4 | 5,037.0 | 81.5분 | 2026-05-09 | 9. 가요·발라드·트로트 | 정보·해설 | 설명 | 283/284 |
| 822 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=634i1Q0C5UI) | Majnukhan | 36,300 | 1,075,952 | 29.6 | ×3,870.3 | 7,004.4 | 15.7분 | 2026-05-21 | 3. 공부·집중·작업 | 음악 | 설명 | 100/100 |
| 823 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=RXYyvE4qRqs) | Click Bollywo… | 25,800 | 760,139 | 29.5 | ×5,869.8 | 8,094.0 | 7.8분 | 2026-07-20 | 3. 공부·집중·작업 | 음악 | 설명 | 46/46 |
| 824 | [music for overthinkers — when the mind goes quiet ∣ deep fo…](https://www.youtube.com/watch?v=IsGUh_yMxDg) | StillSpace | 32,800 | 962,313 | 29.3 | ×232.9 | 5,488.5 | 85.2분 | 2026-04-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 310/310 |
| 825 | [[Playlist] 여름향기 가득한 카페에서 듣기 좋은 음악 ∣ 잔잔한 감성팝 카페음악 🎧 ∣ Healin…](https://www.youtube.com/watch?v=hlxPD1XBS-A) | 낡은 레코드 | 8,870 | 258,192 | 29.1 | ×26.6 | 1,741.2 | 77.9분 | 2026-05-27 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 33/33 |
| 826 | [𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩.°• 야호-!★⊹⋅ ˚💖 듣자마자 신나는 최신 여돌 플레이리스트](https://www.youtube.com/watch?v=v_AYwiX_XgI) | eon | 5,080 | 147,706 | 29.1 | ×8.3 | 1,103.3 | 81.8분 | 2026-06-10 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 16/16 |
| 827 | [마지막 약속(1995) - 김정민 ∣ 여자보컬 리메이크 [원곡감성] Cover](https://www.youtube.com/watch?v=L7EUtPDVddY) | AuraAPT | 13,100 | 379,829 | 29.0 | ×21.8 | 4,090.3 | 5분 | 2026-07-21 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 41/42 |
| 828 | [Paint It, Black – Dark Gothic Orchestral Cover ∣ Epic Cinem…](https://www.youtube.com/watch?v=zWArs5bT_Nc) | Mimousic | 27,300 | 788,423 | 28.9 | ×22.2 | 4,435.6 | 4.5분 | 2026-04-27 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 410/413 |
| 829 | [🔥5 Musik Instrumen Sunda Modern yang Bikin Nagih ∣ BASS_DRUM](https://www.youtube.com/watch?v=zIrcdA2el3w) | BASS_DRUM | 16,700 | 479,005 | 28.7 | ×181.7 | 2,901.8 | 13.3분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 295/295 |
| 830 | [(WCS2026) VGC Masters Finals Battle Music - Pokémon Champio…](https://www.youtube.com/watch?v=B9Vi8BjqFoc) | RezyMania | 13,000 | 371,314 | 28.6 | ×66.0 | 7,559.1 | 5분 | 2026-09-03 | 기타 | 음악 | 설명 | 355/357 |
| 831 | [그대 그리고 나(1988) - 소리새 ∣ Acoustic Cover ∣ 레트로카페](https://www.youtube.com/watch?v=CMDXDnLx3QA) | 레트로 카페 (Retro… | 11,600 | 330,384 | 28.5 | ×63.6 | 2,078.9 | 4분 | 2026-05-16 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 55/58 |
| 832 | [A Peaceful Moment with God 🌿 Relaxing Christian Music ∣ Kot…](https://www.youtube.com/watch?v=IIVkaj0R_Gk) | Haven of Faith | 9,260 | 262,216 | 28.3 | ×63.4 | 1,470.0 | 45.9분 | 2026-04-26 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 73/73 |
| 833 | [#singer #kishan #maldhari માં મેલડી તારી કૃપા અપરંપાર #medi…](https://www.youtube.com/watch?v=by0Ok3JgV3o) | Maa Sikotar O… | 1,670 | 47,292 | 28.3 | ×27.6 | 362.0 | 10.2분 | 2026-06-13 | 1. 수면·명상·힐링 | 음악 | 없음 | 16/16 |
| 834 | [15 Min 528Hz Self Healing Music 🌿 Calm Your Nervous System …](https://www.youtube.com/watch?v=HFW4awIfBmo) | Inner Healing… | 1,240 | 34,958 | 28.2 | ×23.6 | 1,175.9 | 15.5분 | 2026-09-22 | 1. 수면·명상·힐링 | 음악 | 설명 | 14/14 |
| 835 | [【4K/途中広告なし】がんばった自分を、休ませる夜｜自律神経を整える癒しのピアノBGM｜睡眠・リラックス用｜3時間](https://www.youtube.com/watch?v=TlPKpR7on9o) | Starry Note | 22,000 | 614,344 | 27.9 | ×57.9 | 5,348.0 | 192.8분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 199/203 |
| 836 | [마음이 맑아지는 클래식 찬송가 🌿 ∣ 아침에 듣기 좋은 Morning Hymns for Peace & Co…](https://www.youtube.com/watch?v=j6H9mPj769A) | DearHymn | 11,800 | 327,376 | 27.7 | ×7.9 | 2,028.2 | 130.2분 | 2026-05-13 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 455/459 |
| 837 | [잠 안 오 새벽, 깊은 허스키 보컬이 주는 위로 🌧️ 70s 빈티지 어쿠스틱 기타 BGM](https://www.youtube.com/watch?v=BQoJJ8V8TMg) | 조용한 그리움 | 21,400 | 592,665 | 27.7 | ×273.1 | 6,712.7 | 129.5분 | 2026-07-26 | 12. 커버·노래 부르기 | 음악 | 없음 | 106/113 |
| 838 | [[Playlist]고급스러운 카페의 여유로움 ☕️[중간광고없음]카페 매장 음악 🎧 그냥 틀어두세요, 차마실…](https://www.youtube.com/watch?v=lEcJTeg9gCQ) | BGMBUCKS | 19,800 | 545,757 | 27.6 | – | 3,061.2 | 64분 | 2026-04-27 | 4. 카페·매장·라운지 | 연주 | 설명 | 83/83 |
| 839 | [드루와자기 트로트 커버리믹스 총집합! 신나는 트로트 35곡 연속 듣기 🎶추억의 히트송 리믹스,레전드 트로트…](https://www.youtube.com/watch?v=al3dfBmH620) | 드루와자기 | 19,700 | 535,043 | 27.2 | ×1,594.8 | 3,527.8 | 136분 | 2026-05-23 | 5. 운동·드라이브·신나는 | 커버·직접 부른 노래 | 설명 | 236/236 |
| 840 | [🎤 고단한 하루 끝, 막걸리 한잔하며 듣는 눈물 나는 중년 위로가 — 인생막걸리 (가수 창)🎶 인생 트롯 …](https://www.youtube.com/watch?v=4EkREEo9LXQ) | 우리인생뮤직 | 19,700 | 530,831 | 26.9 | ×190.6 | 2,988.2 | 6분 | 2026-04-27 | 9. 가요·발라드·트로트 | 음악 | 설명 | 309/309 |
| 841 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 서울숲 카페에서 하루종일 듣기좋은 팝송 𝟏𝟎시간 (중간광고없음) ☀️🌿 기분 좋아지는 카페…](https://www.youtube.com/watch?v=2eFGY53k350) | With Lofi Cafe | 4,980 | 134,154 | 26.9 | ×14.4 | 998.3 | 616.3분 | 2026-06-09 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 9/9 |
| 842 | [Soothe Station - Andamanaya - Tagalog Version (Pakaranon Ba…](https://www.youtube.com/watch?v=4SWpVSbm4Qo) | Soothe Sta. | 28,900 | 774,222 | 26.8 | ×5.6 | 5,573.3 | 4.4분 | 2026-06-05 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 168/169 |
| 843 | [비 오는 날 카페에서 듣기 좋은 추억의 노래 ∣ 계속 듣게 되는 7080 라디오 감성 올드팝](https://www.youtube.com/watch?v=riMgzQ7B4JA) | morgellia(모르겔… | 18,100 | 484,789 | 26.8 | ×59.5 | 3,120.1 | 165.9분 | 2026-05-19 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 313/313 |
| 844 | [Your Soul Will Thank You For This ∣∣ DIVINE Krishna Dhun & …](https://www.youtube.com/watch?v=-gGLDLqN03M) | Krishna Lovers | 49,800 | 1,328,327 | 26.7 | ×358.6 | 8,517.2 | 30.6분 | 2026-05-19 | 기타 | 정보·해설 | 설명 | 1,350/1,359 |
| 845 | [Mortal Shell 2 [OST] - Ambient Music [HQ]](https://www.youtube.com/watch?v=0xjJ71Vcqc0) | Taneomi | 5,760 | 153,370 | 26.6 | ×36.3 | 1,132.9 | 5.8분 | 2026-06-08 | 13. OST·사운드트랙 | 음악 | 설명 | 258/259 |
| 846 | [Stress Relief Jazz 🌙 Smooth Sax for Calm, Relaxation & Anxi…](https://www.youtube.com/watch?v=YPsVWworsbc) | JazzAyo Lounge | 37,700 | 1,002,644 | 26.6 | ×737.2 | 5,802.7 | 133.2분 | 2026-05-02 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 387/399 |
| 847 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 이게 극락 사운드인가?🪷 ∣ 속세 탈출용 불교 재즈🎧](https://www.youtube.com/watch?v=EQzDJeyYNX0) | chill potato … | 15,500 | 411,007 | 26.5 | ×54.8 | 2,515.1 | 123.1분 | 2026-05-11 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 282/282 |
| 848 | [𝐘𝐨𝐠𝐚 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 바람이 살랑 우붓의 요가 샬라ㅣ허밍 요가 음악](https://www.youtube.com/watch?v=34ESzO9DdwQ) | 김샨티(Shanti Ki… | 5,070 | 134,076 | 26.4 | ×12.2 | 1,080.2 | 61.5분 | 2026-06-20 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 45/46 |
| 849 | [Arabic Deep House Mix & arabic Oud - The Last Pharaoh (Offi…](https://www.youtube.com/watch?v=zEA4nqtiy94) | Deep Tune Fan… | 20,200 | 534,052 | 26.4 | ×58.2 | 3,341.3 | 8분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 113/113 |
| 850 | [1 Hour Relaxing Piano ∣ Piano Therapy (پیانو درمانی) ∣ ۱ سا…](https://www.youtube.com/watch?v=rhfCDOTWNs0) | amir moradi | 7,130 | 187,781 | 26.3 | ×33.2 | 1,048.8 | 61.3분 | 2026-04-26 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 386/386 |
| 851 | [All RED EVIL JACK MUSIC【作業用/For work】](https://www.youtube.com/watch?v=hruX5UfVTYw) | イヴch🍳🥚 | 2,450 | 64,313 | 26.2 | – | 757.1 | 8.6분 | 2026-07-29 | 기타 | 음악 | 설명 | 49/49 |
| 852 | [[playlist] 신기하네, 이런 빈티지재즈 좋아하는 걸 어떻게 알고 틀어줬지? ∣ 중간 광고 없음 Ja…](https://www.youtube.com/watch?v=aZRegDWuCEo) | 포 시즌 플리 Four … | 39,200 | 1,018,491 | 26.0 | ×44.1 | 14,971.1 | 75.1분 | 2026-08-15 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 416/434 |
| 853 | [Spirit Of Wolf ∣ Native Inspired Healing Music for Deep Cal…](https://www.youtube.com/watch?v=SUgiw7VzoUY) | Ancestral Ech… | 5,010 | 129,993 | 25.9 | ×153.8 | 1,093.4 | 8.1분 | 2026-06-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 318/320 |
| 854 | [지렸다... 심장마비 🔥 선넘은 여성보컬 락발라드 COVER 33곡 모음 ∣ 전율돋는 초고음 소름주의보 3…](https://www.youtube.com/watch?v=tol8QOlOsPo) | 아무노래개조소 | 9,460 | 243,608 | 25.8 | ×27.8 | 1,888.4 | 133.5분 | 2026-06-15 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 143/148 |
| 855 | [Drifting Low (Ethereal Deep House) — Club Nights](https://www.youtube.com/watch?v=YtprplnFUpc) | Club Nights | 28,400 | 728,336 | 25.6 | ×25.7 | 5,984.7 | 6.4분 | 2026-06-22 | 기타 | 정보·해설 | 설명 | 47/47 |
| 856 | [Naagin All Seasons - ‘The Origin of Revenge‘ MV ∣ Naagin Em…](https://www.youtube.com/watch?v=-yEf-59hqRs) | 𝐍𝐚𝐚𝐠𝐢𝐧 𝐇𝐏 𝐎𝐟𝐟… | 24,100 | 616,756 | 25.6 | – | 4,400.7 | 11.4분 | 2026-06-04 | 기타 | 한 곡 | 설명 | 163/163 |
| 857 | [Chike & Tiwa Savage - We Go Make Am Work (2026 Afro Music) …](https://www.youtube.com/watch?v=0PVF8lImHNs) | Afro Music So… | 2,600 | 65,856 | 25.3 | ×84.3 | 528.4 | 6분 | 2026-06-19 | 14. AI 음악 | AI 음악 | 설명 | 10/10 |
| 858 | [Arabic Oud & Flamenco Guitar – Gentle Instrumental Music fo…](https://www.youtube.com/watch?v=4HR2eB5p8WI) | Andalusian Ou… | 26,700 | 674,996 | 25.3 | ×178.8 | 4,452.4 | 90.8분 | 2026-05-23 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 264/267 |
| 859 | [💿 노릇노릇 빵아저씨가 만든 브금🍞](https://www.youtube.com/watch?v=2bUpv56PbMw) | 프륀 Pruiin | 11,400 | 287,314 | 25.2 | ×19.4 | 2,161.1 | 123.7분 | 2026-06-11 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 90/91 |
| 860 | [playlist ∣ 여름, 레몬과 재즈에 대하여](https://www.youtube.com/watch?v=Gr7ZxTdL8XA) | centralgrocer… | 27,200 | 684,159 | 25.1 | ×50.5 | 6,260.3 | 236.8분 | 2026-07-05 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 207/209 |
| 861 | [Relaxing Country Gospel ∣ Call Upon the Name of Jesus ∣ Hea…](https://www.youtube.com/watch?v=R38UIWZtjkQ) | Breathing Pla… | 35,000 | 871,138 | 24.9 | ×245.6 | 6,730.2 | 6.4분 | 2026-06-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 863/859 |
| 862 | [Into the Misty Scottish Highlands｜Celtic Music for Deep Foc…](https://www.youtube.com/watch?v=7JojfPKvTM4) | Echoes of Alba | 44,800 | 1,114,471 | 24.9 | ×44.0 | 6,267.0 | 143.4분 | 2026-04-27 | 3. 공부·집중·작업 | 음악 | 설명 | 480/481 |
| 863 | [눈물 없이는 못 듣는 감성 락발라드 트로트 12곡｜중년 가슴을 울리는 인생 노래 모음｜55분 연속듣기](https://www.youtube.com/watch?v=0rFs08Wz1Xw) | 인생은 트로트 | 9,120 | 226,496 | 24.8 | ×15.5 | 2,795.9 | 55.5분 | 2026-08-02 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 96/96 |
| 864 | [듣는 순간 마음이 편안해지는 첼로 음악 🎻 ∣ 공부, 휴식, 감성 힐링 음악](https://www.youtube.com/watch?v=QmJoFjq-aWE) | 따뜻한 휴식 Studio | 1,990 | 49,094 | 24.7 | ×112.6 | 325.4 | 51.4분 | 2026-05-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 37/37 |
| 865 | [Música espiritual hebrea - Melodías antiguas de Israel para…](https://www.youtube.com/watch?v=A7ZlOXV_CrU) | Sacred Hebrew… | 20,200 | 494,694 | 24.5 | ×274.4 | 3,235.1 | 63.5분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 749/752 |
| 866 | [Spirit Of Eagle Native American Healing Music for Vision, F…](https://www.youtube.com/watch?v=j3OaU9N8uIU) | Ancestral Ech… | 5,010 | 119,799 | 23.9 | ×141.8 | 1,043.7 | 9.1분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 215/215 |
| 867 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭☕ Let the Day Start Softly with Coffee and Korean C…](https://www.youtube.com/watch?v=FUrT7LN9VRU) | Seoul Flow AI | 23,700 | 564,115 | 23.8 | ×48.6 | 3,653.2 | 166.6분 | 2026-05-20 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 133/133 |
| 868 | [Morning Serenity 🌿 Raag Alhaiya Bilawal inspired Healing In…](https://www.youtube.com/watch?v=7RR_x4Tu7EE) | Soulful Breat… | 49,600 | 1,168,921 | 23.6 | ×107.5 | 7,430.1 | 66.2분 | 2026-05-18 | 1. 수면·명상·힐링 | 음악 | 설명 | 278/279 |
| 869 | [내 삶에 임하소서 ∣ 주기도문 기반 잔잔한 찬양, 조용한 기도 ∣ Let Your Presence Fill…](https://www.youtube.com/watch?v=HzyxKZ_w2_8) | 쉼이 되는 찬양 | 3,030 | 71,265 | 23.5 | ×13.8 | 403.9 | 5.3분 | 2026-04-28 | 15. CCM·찬양·국악… | 음악 | 설명 | 27/27 |
| 870 | [पहाड़ों में गूंजती जादुई बाँसुरी 🎋 Magical Mountain Flute M…](https://www.youtube.com/watch?v=orUOWfIkmM4) | Vibe Without … | 26,600 | 625,618 | 23.5 | ×216.7 | 3,880.8 | 46.8분 | 2026-05-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 416/416 |
| 871 | [Playlist ∣ Smooth Hip Hop Groove 😎 ∣ GROOVE · JAZZHOP ∣ Caf…](https://www.youtube.com/watch?v=ru-PF195pR0) | PoponWave | 23,000 | 535,070 | 23.3 | ×36.3 | 3,050.7 | 215.2분 | 2026-04-29 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 177/178 |
| 872 | [Calm Morning Music ∣ Relaxing Flute for Anxiety Relief](https://www.youtube.com/watch?v=P1aHG6IqCtM) | Moksha Sounds… | 37,000 | 859,614 | 23.2 | ×138.5 | 4,927.1 | 40.2분 | 2026-04-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 293/294 |
| 873 | [【あつ森】Lofi Night｜雨降る夜に部屋でゆっくりと過ごす☔雨音｜作業・勉強【1時間】](https://www.youtube.com/watch?v=2SV-ueN0hxA) | Tsumugi's Coz… | 24,800 | 574,011 | 23.1 | ×55.2 | 4,253.3 | 60.2분 | 2026-06-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 104/108 |
| 874 | [LOVE 💚 ∣ 639Hz Heart Chakra Healing Music ∣ Self-Love, Comp…](https://www.youtube.com/watch?v=DZYgNIUjkH4) | Sound of the … | 1,570 | 36,232 | 23.1 | ×19.0 | 634.4 | 5.4분 | 2026-08-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 130/134 |
| 875 | [KWUBAKA (AMAPIANO remix) by ABASHAZANGENDO (BGM remix)](https://www.youtube.com/watch?v=3TgKlzPGh6Y) | Burundi Golde… | 16,700 | 383,707 | 23.0 | ×13.2 | 2,585.4 | 4.4분 | 2026-05-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 90/90 |
| 876 | [10-Minute Divine Flute Meditation ∣ Inner Peace & Healing ∣…](https://www.youtube.com/watch?v=_3PmWQ0lENE) | Sri Ganapathy… | 45,500 | 1,039,812 | 22.9 | ×1,725.8 | 9,656.9 | 10.6분 | 2026-07-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,480/1,482 |
| 877 | [Playlist✍️ 수험생 초집중모드 공부 플레이리스트 ∣ 틀어놓는 순간 공부에 빠져드는 공부플리 BGM🎧…](https://www.youtube.com/watch?v=vuYrODP_RTE) | obne music 오브… | 7,110 | 161,939 | 22.8 | ×22.2 | 2,951.1 | 120.2분 | 2026-08-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 4/6 |
| 878 | [music to stay locked in](https://www.youtube.com/watch?v=eL5rWVPguoc) | Productivity … | 39,000 | 873,967 | 22.4 | ×37.5 | 12,006.6 | 115.6분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 208/210 |
| 879 | [Nine Inch Nails x Hans Zimmer - Right Where Time Belongs (D…](https://www.youtube.com/watch?v=QqyWPg0fM_E) | Dreams Of Col… | 14,300 | 318,670 | 22.3 | ×8.4 | 2,556.2 | 7분 | 2026-06-19 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,321/1,327 |
| 880 | [[Playlist] 오늘은 일본 카페에 앉아 있는 기분으로](https://www.youtube.com/watch?v=fDk1BeVbz_4) | JazzBrown | 15,900 | 352,807 | 22.2 | ×61.8 | 2,462.3 | 70.5분 | 2026-06-01 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 30/31 |
| 881 | [【在喧囂中尋回本心，伴隨天籟美聲聆聽千年的清静】 靈魂淨化｜清静經 ｜Taoist Healing Music・ヒーリ…](https://www.youtube.com/watch?v=AqSDuxZWMHk) | YUCHIN'S TAOI… | 3,500 | 77,638 | 22.2 | ×15.8 | 606.2 | 4.6분 | 2026-06-16 | 1. 수면·명상·힐링 | 음악 | 설명 | 73/73 |
| 882 | [👑💎 Beautiful Princesses, Magical Animals & Relaxing Piano M…](https://www.youtube.com/watch?v=LGexlV5skko) | Princesses Pa… | 7,620 | 168,253 | 22.1 | ×33.3 | 1,433.1 | 5.7분 | 2026-06-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 181/182 |
| 883 | [途中広告なし[BGM]心が晴れる朝🌿Gentle Morning Piano & Guitar Music](https://www.youtube.com/watch?v=OSXpI32ZlQI) | Aurora Tune | 19,200 | 421,845 | 22.0 | ×6.9 | 3,070.8 | 123.5분 | 2026-06-06 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 50/50 |
| 884 | [[중간광고없음] 🌲✨ 복잡한 마음은 잠시 내려놓자 ∣ 위로와 휴식의 피아노 ∣ BGM ∣ 휴식, 힐링, 위로](https://www.youtube.com/watch?v=ADirqRo8IyI) | Riae & Piano | 12,400 | 270,178 | 21.8 | ×17.6 | 3,682.2 | 180.9분 | 2026-08-09 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 33/35 |
| 885 | [불(佛)빛사운드 - 물처럼, 바람처럼 M/V 4K #불교음악](https://www.youtube.com/watch?v=G7P3BWOH67s) | 불佛빛사운드 | 3,990 | 86,361 | 21.6 | ×10.3 | 587.5 | 5.8분 | 2026-05-28 | 1. 수면·명상·힐링 | AI 음악 | 설명 | 118/119 |
| 886 | [TAI CHI MUSIC – MELODIES OF THE TAO ∣ Chinese Relaxing Musi…](https://www.youtube.com/watch?v=PcSZ9tCBFQ0) | VibrArte Music | 17,100 | 369,475 | 21.6 | ×65.3 | 2,177.7 | 58.9분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 162/162 |
| 887 | [[playlist] 희한하네, 살면서 이렇게 좋은 재즈는 처음 들어. 이렇게 오래 살았는데도 말이야. ∣ …](https://www.youtube.com/watch?v=cHC2M0hdKCU) | 포 시즌 플리 Four … | 39,200 | 842,742 | 21.5 | ×36.5 | 10,811.7 | 65분 | 2026-08-05 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 299/300 |
| 888 | [[60만뷰 감사합니다]가왕의 명곡을 락발라드로! 조용필 - 그 겨울의 찻집 (AI Cover / 알고보니 …](https://www.youtube.com/watch?v=_GrNoR-QyMQ) | 알고보니 혼비백산 | 42,900 | 920,105 | 21.4 | ×102.7 | 6,015.8 | 5.4분 | 2026-05-22 | 14. AI 음악 | AI 음악 | 설명 | 249/256 |
| 889 | [고양이 카페에 놀러 올래?](https://www.youtube.com/watch?v=ifT02Y1gbuI) | 꾸양이 | 14,800 | 313,219 | 21.2 | ×15.4 | 2,114.6 | 63.6분 | 2026-05-27 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 152/154 |
| 890 | [머리가 맑아지고🌳마음이 평온해져요. 피아노와 플루트 선율 ∣ 3시간, 힐링음악, 명상음악 ∣ Relaxin…](https://www.youtube.com/watch?v=QPa9L5TDD-4) | 살구사운드 SalguSo… | 10,700 | 226,297 | 21.1 | ×17.0 | 1,864.6 | 188분 | 2026-06-22 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 129/129 |
| 891 | [【洋楽Playlist】疲れた夜に聴きたい、やさしく包まれるチルR&B 🌆✨｜途中広告なし【作業用BGM】](https://www.youtube.com/watch?v=kf0crw-vh4g) | Moo'in Nights | 25,000 | 528,762 | 21.1 | ×17.3 | 3,600.1 | 66.2분 | 2026-05-28 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 35/35 |
| 892 | [Bombay BGM ∣ 80-Piece Orchestra](https://www.youtube.com/watch?v=ssC6VM6GQ-4) | Australian In… | 32,100 | 676,973 | 21.1 | – | 4,286.5 | 13.3분 | 2026-05-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 234/236 |
| 893 | [🍂하루종일 듣기 좋은 기분 좋은 클래식 명곡 ∣ 중간광고❌∣ 쇼팽, 리스트, 슈만, 바흐 ∣ 명상, 휴식,…](https://www.youtube.com/watch?v=zG6O9a_rRpY) | 퓨얼리 피아노 클래식 𝚋… | 22,200 | 463,183 | 20.9 | ×16.0 | 10,673.6 | 180.7분 | 2026-09-08 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 112/117 |
| 894 | [Enya - I know Your Pain (2026 Official Music Video)](https://www.youtube.com/watch?v=1AZagg8LCDw) | Celestine Echo | 14,700 | 305,632 | 20.8 | ×58.6 | 2,839.2 | 6.3분 | 2026-07-06 | 기타 | 한 곡 | 설명 | 97/97 |
| 895 | [10 Most Beautiful Melodies Ever Written for Piano](https://www.youtube.com/watch?v=vmbG0x1jq_s) | Lisztopher | 9,580 | 198,661 | 20.7 | ×36.0 | 1,316.4 | 15.9분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 269/269 |
| 896 | [Lingashtakam Shiva Meditation Music ∣ Powerful Healing Mant…](https://www.youtube.com/watch?v=TehHNpaUk0s) | Satya Devotio… | 3,390 | 70,269 | 20.7 | ×1.9 | 515.3 | 5.7분 | 2026-06-07 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 30/30 |
| 897 | [🍉 냉장고를 열었더니 수박만 있는 브금](https://www.youtube.com/watch?v=h6oskIb0ASU) | 프륀 Pruiin | 11,400 | 235,916 | 20.7 | ×16.2 | 2,360.4 | 146.4분 | 2026-07-14 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 100/101 |
| 898 | [싱그러운 아침, 고요한 클래식 선율 속에서 마음의 평화를 느껴보세요. Healing Classics와 함께…](https://www.youtube.com/watch?v=gtHsO8taxgo) | 클래식힐링 | 14,600 | 301,806 | 20.7 | ×48.9 | 1,829.9 | 125.2분 | 2026-05-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 127/127 |
| 899 | [Whispers of the Ancient Forest｜Mystical Celtic Music for De…](https://www.youtube.com/watch?v=DQ_KPUXyY7o) | Echoes of Alba | 44,800 | 925,183 | 20.6 | ×36.5 | 6,053.6 | 140.2분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 129/135 |
| 900 | [🍃Xanh Playlist 2🍃TAN LÀM, BẬT NHẠC∣ Nhạc R&B Lofi Chill Yêu…](https://www.youtube.com/watch?v=lkotmZNWq5I) | Xanh | 46,200 | 953,048 | 20.6 | ×18.5 | 17,341.6 | 50.4분 | 2026-08-28 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 217/227 |
| 901 | [#Zumba Work out 💪🏽..Full energy...Best music for Work out..](https://www.youtube.com/watch?v=cuzHvFb2It0) | Zumbique | 1,210 | 24,938 | 20.6 | ×9.0 | 221.3 | 7.8분 | 2026-07-01 | 기타 | 음악 | 설명 | 4/4 |
| 902 | [[찬송가 모음]주님 앞에 펑펑 울고 싶을 때 듣는 찬양ㅣ눈물의 찬송가 10곡ㅣ깊은 울림 바리톤 찬양ㅣHYM…](https://www.youtube.com/watch?v=giFgcjlR4Co) | 골방 찬양 | 26,000 | 534,541 | 20.6 | ×5.5 | 3,352.2 | 81.4분 | 2026-05-15 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 1,318/1,318 |
| 903 | [가슴을 울리는 감성 트로트 5곡 모음 ∣ 깊은 밤 듣기 좋은 노래](https://www.youtube.com/watch?v=o_RE1dPuUoo) | 트로트 작은 음악실 | 23,500 | 482,871 | 20.6 | ×79.6 | 3,075.2 | 24.4분 | 2026-05-18 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 209/214 |
| 904 | [Morning Cortisol Detox 🌿 Raag Bhairavi Bansuri 432 Hz for S…](https://www.youtube.com/watch?v=cjNH2q4aBYc) | Soulful Breat… | 49,600 | 1,016,110 | 20.5 | ×93.4 | 14,049.8 | 83.2분 | 2026-08-11 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 255/258 |
| 905 | [Habias X Filho Do Zua - Se a Vida Decide Me Levar](https://www.youtube.com/watch?v=SnGHZcvK2TA) | Habias | 31,400 | 639,756 | 20.4 | ×35.0 | 7,748.1 | 4.2분 | 2026-07-31 | 기타 | 음악 | 설명 | 245/247 |
| 906 | [🎹 Corazón Silente ∣ Piano para Calmar la Mente](https://www.youtube.com/watch?v=3jUY4NFO9sg) | El Piano de E… | 14,200 | 288,924 | 20.4 | ×356.5 | 3,325.8 | 4.1분 | 2026-07-27 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 25/25 |
| 907 | [고고프렌즈 “국어별동대” 피아노커버](https://www.youtube.com/watch?v=IkZ1vxE2GeQ) | MUJINS 뮤진스 | 19,200 | 378,881 | 19.7 | ×54.7 | 3,866.6 | 7.5분 | 2026-07-16 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 521/525 |
| 908 | [It's TV Time! – Deltarune Piano Collections, Vol. 2 (Offici…](https://www.youtube.com/watch?v=44Dh4Vb8Wtk) | Trevor Alan G… | 18,200 | 353,364 | 19.4 | – | 17,352.8 | 5.6분 | 2026-10-01 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 993/997 |
| 909 | [【作業用BGM】流すだけで前向きになれる洋楽 House Pop Mix｜リラックス・集中・気分転換](https://www.youtube.com/watch?v=Kk1n4AZQyws) | Lucky Clover … | 39,600 | 768,874 | 19.4 | ×95.3 | 5,496.9 | 105.5분 | 2026-06-04 | 기타 | 음악 | 설명 | 66/66 |
| 910 | [Walking Past an Old Library in Autumn Boston 🍂 Warm Jazz, F…](https://www.youtube.com/watch?v=0KCrdROdw4g) | Dreams Jazz M… | 48,200 | 934,740 | 19.4 | ×28.8 | 25,320.9 | 209분 | 2026-09-15 | 7. 재즈·보사노바 | 음악 | 설명 | 72/75 |
| 911 | [(Free For Profit) Melodic Type Beat - "ANGEL"](https://www.youtube.com/watch?v=LgS91RB_BDk) | Nocturnn | 36,000 | 697,219 | 19.4 | ×20.2 | 5,584.3 | 4분 | 2026-06-19 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 229/232 |
| 912 | [Sleep Instantly with Soft Piano and Rain 🌧️ Relaxing Music …](https://www.youtube.com/watch?v=PclKQrQuR7U) | Relaxing Piano | 37,000 | 707,007 | 19.1 | ×122.0 | 8,806.6 | 181.6분 | 2026-08-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 79/79 |
| 913 | [네가 내게 알려줬어💕｜『 四季の笑顔 (사계절 미소)』｜가사해석/Lyrics](https://www.youtube.com/watch?v=T7gBckYYJug) | Nonohara | 1,240 | 23,517 | 19.0 | ×10.7 | 462.6 | 4.9분 | 2026-09-01 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 22/23 |
| 914 | [💔K- 락 발라드 초강력 허스키 여신 떳다 l 2곡 연속 목소리 소름 미쳤다😱"사랑이 나를 죽인다" ㅣ원곡…](https://www.youtube.com/watch?v=EpXINywBT1M) | 음악의 정원 [Garde… | 16,800 | 317,621 | 18.9 | ×95.7 | 1,775.0 | 7.7분 | 2026-04-26 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 106/106 |
| 915 | [Healing Music for Anxiety, Fears and Depression 🌿 Heals the…](https://www.youtube.com/watch?v=RUowd-_b72Y) | Nature Aura | 3,940 | 74,473 | 18.9 | ×60.5 | 689.9 | 104.8분 | 2026-07-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 51/51 |
| 916 | [𝓅𝓁𝒶𝓎𝓁𝒾𝓈𝓉 𖤐₊˚ 앙큼 미소녀 브금 │ 공부·작업·집중 BGM ✦](https://www.youtube.com/watch?v=8rE90EGyCbY) | 오늘은 무슨 컨셉? | 3,010 | 56,044 | 18.6 | ×15.8 | 397.6 | 29.2분 | 2026-06-03 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 39/39 |
| 917 | [(No Ads)Rain Ambience and Calm Piano Music – Peaceful Sleep…](https://www.youtube.com/watch?v=oa4PEL3kHLo) | Relaxing Piano | 37,000 | 686,094 | 18.5 | ×118.4 | 7,434.4 | 183.7분 | 2026-07-22 | 2. 자연 소리·백색소음 | 음악 | 설명 | 228/229 |
| 918 | [7080 카페음악 베스트🌺50대이상이 들으면 기분좋아지는 7080노래모음 ∣ 베스트 7080노래모음 ∣ 광…](https://www.youtube.com/watch?v=IZmsMTzrWDY) | Korean Cafe M… | 3,280 | 60,041 | 18.3 | ×1,017.6 | 649.4 | 10.3분 | 2026-07-21 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 3/3 |
| 919 | [90년대 00년대 락발라드 명곡 모음 ∣ 샤우팅 넘치며 감동적인 락발라드 40곡 연속듣기 ∣ 엠씨더맥스, …](https://www.youtube.com/watch?v=5c_EJyjOdWQ) | 발라드 홈 / BALLA… | 10,200 | 185,172 | 18.1 | ×19.4 | 1,664.5 | 154.9분 | 2026-07-03 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 23/23 |
| 920 | [Deep Sleep Music ∣ 528hz Whole Body Healing Frequency, Mela…](https://www.youtube.com/watch?v=9tczYViDUak) | Healing Sleep… | 28,100 | 509,659 | 18.1 | ×146.4 | 4,461.0 | 698.1분 | 2026-06-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 283/283 |
| 921 | [트로트 모음 50곡 #트로트 메들리 #인기트로트 🎶 하루 종일 듣기 좋은 노래 모음 🎶 추억의 트로트 명곡…](https://www.youtube.com/watch?v=5GO9R1-U5OM) | SonicVista | 26,900 | 483,693 | 18.0 | ×2,853.6 | 3,708.9 | 78.9분 | 2026-06-13 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 77/79 |
| 922 | [Morning Energy Music ∣ Dilruba Raga Yaman ∣ 1.5 Hours](https://www.youtube.com/watch?v=DMcoOLvmAyQ) | Raga Focus | 37,500 | 671,341 | 17.9 | ×465.2 | 4,038.2 | 90분 | 2026-05-09 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 166/167 |
| 923 | [밤바다 보이는 카페 창가, 조용히 듣기 좋은 7080 라디오 감성 올드팝](https://www.youtube.com/watch?v=9x53vG82_Ao) | morgellia(모르겔… | 18,100 | 322,801 | 17.8 | ×39.6 | 2,175.6 | 159.8분 | 2026-05-26 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 151/151 |
| 924 | [가슴 뭉클한 옛날 노래 🍂 백마강·해운대 엘레지·동숙의 노래｜중년·어르신을 위한 추억의 트로트 50곡 🍁 …](https://www.youtube.com/watch?v=F9mzexxZOVo) | 추억의 K트롯 | 14,700 | 261,084 | 17.8 | ×70.4 | 3,055.1 | 137.7분 | 2026-07-28 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 104/105 |
| 925 | [Soft Telugu Songs for your SOUL ♡](https://www.youtube.com/watch?v=17nDtmG2PRU) | With Love Ash… | 36,500 | 646,553 | 17.7 | – | 4,652.9 | 9.8분 | 2026-06-05 | 기타 | 플레이리스트·모음 | 설명 | 23/23 |
| 926 | [Chopin for Autumn Nights — Peaceful Piano for Relaxation (4…](https://www.youtube.com/watch?v=AkZrzHCfivc) | Rain Whisper … | 40,800 | 718,071 | 17.6 | ×26.2 | 15,335.8 | 78.5분 | 2026-09-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 143/145 |
| 927 | [Lofi Summer Vibes 🌊 Seaside Coffee & Relaxing Lofi for a Se…](https://www.youtube.com/watch?v=ovS27OGTajs) | Little Lofi C… | 26,000 | 456,713 | 17.6 | ×55.8 | 2,611.1 | 205.8분 | 2026-04-30 | 11. 힙합·R&B·EDM | 음악 | 설명 | 112/112 |
| 928 | [NGWIZA (BGM Remix) Ballet Royal du Burundi](https://www.youtube.com/watch?v=ho_IGrAkUSs) | Burundi Golde… | 16,700 | 292,587 | 17.5 | ×10.1 | 1,785.3 | 4.2분 | 2026-05-11 | 기타 | 음악 | 설명 | 206/206 |
| 929 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 올해 내내 듣게 될 시원한 청량팝 모음🐶🩵 첫 곡부터 기분 좋아지는 여름 플리👙 카페음…](https://www.youtube.com/watch?v=DwlYkGuixsw) | OOOffi | 25,600 | 443,427 | 17.3 | ×15.8 | 3,028.6 | 657.9분 | 2026-05-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 59/59 |
| 930 | [🌿🍁 미사리에서 듣는 최고의 가을 카페음악｜2026 가을 감성 플레이리스트 ☕ 마음이 편안해지는 음악](https://www.youtube.com/watch?v=sDs-SBQlNCw) | Cozy Cafe Mus… | 3,870 | 66,514 | 17.2 | ×13.3 | 1,606.0 | 62.6분 | 2026-09-10 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 0/13 |
| 931 | [Mind Relaxing Music – Peaceful Flute Meditation Music, Esca…](https://www.youtube.com/watch?v=bx_QXhMb5xM) | CLASSICAL FUS… | 19,000 | 325,781 | 17.1 | ×69.3 | 2,288.5 | 40.1분 | 2026-06-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 76/77 |
| 932 | [샹송이 이렇게 까지 좋은줄 몰랐습니다 ∣ 너무 좋아서 아침부터 듣게 되는 7080 올드팝 ∣ 감성이 터진](https://www.youtube.com/watch?v=KFu4Y2j652w) | Midnight Melo… | 28,000 | 478,857 | 17.1 | ×137.8 | 2,785.7 | 119.9분 | 2026-05-03 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 157/157 |
| 933 | [The Little Forest Concert Vol.3 🌿 ∣ Warm BGM for Reading, S…](https://www.youtube.com/watch?v=_zmbIUADeMw) | 그루잠 Gurujam | 27,400 | 467,507 | 17.1 | ×78.3 | 6,837.5 | 32.6분 | 2026-08-14 | 3. 공부·집중·작업 | 음악 | 설명 | 71/71 |
| 934 | [TAO — 道 ∣ Japanese Zen Music for Deep Meditation & Inner Ca…](https://www.youtube.com/watch?v=SepvquaFWAY) | Hikari Zen | 27,300 | 465,585 | 17.1 | ×101.0 | 2,773.4 | 237.6분 | 2026-05-07 | 1. 수면·명상·힐링 | 음악 | 설명 | 107/107 |
| 935 | [Morning Anxiety Calms ∣ Prana Vihara — Bansuri 432Hz for Cl…](https://www.youtube.com/watch?v=Ae8IzAhMcYY) | Shunya SoundS… | 20,400 | 345,722 | 16.9 | ×331.8 | 1,971.6 | 34.2분 | 2026-04-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 189/189 |
| 936 | [[눈물주의]세상에서 가장 슬픈 노래 😢 어미의 한 [판소리]💔The Saddest Song Ever Wri…](https://www.youtube.com/watch?v=DhredFI94dc) | Nana Music | 10,000 | 165,979 | 16.6 | ×195.7 | 1,844.7 | 6분 | 2026-07-24 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 99/103 |
| 937 | [[연속듣기] 눈물 나게 가슴 뭉클한 옛날 노래 45곡 🎵 세월이 흘러도 잊을 수 없는 추억의 트로트 🎵 흘…](https://www.youtube.com/watch?v=xj8SEIUhbjY) | 추억의 K트롯 | 14,700 | 243,138 | 16.5 | ×65.5 | 1,671.5 | 132.4분 | 2026-05-29 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 78/78 |
| 938 | [Instrumental Christian Piano for Focus ∣ 2 Hours Worship Pi…](https://www.youtube.com/watch?v=q7ooKtFTYMk) | In His Presen… | 17,200 | 284,066 | 16.5 | ×26.2 | 1,947.3 | 121.4분 | 2026-05-29 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 16/16 |
| 939 | [딸에게 한 번도 하지 못했던 말... 오늘 이 노래로 전합니다 / 내딸아 / 도연스님 / 만복감성트롯 / …](https://www.youtube.com/watch?v=k5oAx-igPIU) | 만복 낭만트롯 | 2,500 | 41,094 | 16.4 | ×15.8 | 500.9 | 5분 | 2026-08-01 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 30/30 |
| 940 | [【あつ森BGM】夜のリラックスタイム🌙 心落ち着くLo-fi Chill Hop & ASMR｜作業・勉強・睡眠用](https://www.youtube.com/watch?v=YgEA5Ow6mk4) | Chill Mori BGM | 29,300 | 480,386 | 16.4 | ×5.5 | 2,762.2 | 180.1분 | 2026-05-01 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 51/51 |
| 941 | [Deep meditation ∣ use headphones for better results ∣ mindf…](https://www.youtube.com/watch?v=HR4UkS5H-kk) | Modern Yogii | 711 | 11,644 | 16.4 | – | 70.3 | 15.2분 | 2026-05-09 | 1. 수면·명상·힐링 | 음악 | 설명 | 7/7 |
| 942 | [[𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 정병 제대로 터져버린 멘헤라남 플리](https://www.youtube.com/watch?v=N2zEbM5dIH4) | 안평화 | 17,100 | 276,938 | 16.2 | ×9.8 | 5,925.2 | 15.6분 | 2026-09-05 | 기타 | 플레이리스트·모음 | 없음 | 168/174 |
| 943 | [🍉여름에 듣기 좋은 카페 음악 ☕ 상쾌한 여름 바닷가 처럼 기분좋은 Playlist ∣ 중간 광고 없음 ∣…](https://www.youtube.com/watch?v=ZSVnVZ0-ROg) | 오늘의 멜로디 Today… | 19,700 | 318,365 | 16.2 | ×65.0 | 1,972.8 | 120.4분 | 2026-05-13 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 57/57 |
| 944 | [너에플리 리메이크 모음｜CHAPTER 1](https://www.youtube.com/watch?v=iSJD2jZwB8E) | 너에플리 | 28,600 | 459,175 | 16.1 | – | 3,172.1 | 34분 | 2026-05-30 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 184/184 |
| 945 | [[평안 찬송] 마음에 평안과 기쁨을 채워주는 은혜의 찬송가 모음 ∣ 들을수록 마음이 편안해지는 찬송가 연속…](https://www.youtube.com/watch?v=GaBxDi7Eg3M) | 주님곁에 | 18,700 | 297,563 | 15.9 | ×6.7 | 3,889.7 | 71.2분 | 2026-08-06 | 15. CCM·찬양·국악… | 커버·직접 부른 노래 | 설명 | 277/281 |
| 946 | [[찬송가 연속듣기] 마음이 복잡할 때 듣는 잔잔한 찬송가 20곡 ∣ 잠들기 전 평안을 주는 찬양 메들리 (…](https://www.youtube.com/watch?v=Tt9qwuoMPtI) | 골방 찬양 | 26,000 | 413,281 | 15.9 | ×4.3 | 2,658.7 | 246.6분 | 2026-05-19 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 622/631 |
| 947 | [[외모지상주의 BGM] Jekyll & Unconscious 3 ∣ Lookism BGM](https://www.youtube.com/watch?v=7FcjatxdDXo) | 루트레이블 (ROUTEL… | 13,200 | 206,593 | 15.7 | ×7.2 | 1,343.7 | 5.7분 | 2026-05-21 | 기타 | 음악 | 설명 | 126/126 |
| 948 | [🎵그냥 틀어놨는데 눈물이 났네요...주님은 다 아시죠ㅣ은혜로운 찬양모음 ㅣCCM플레이리스트 ㅣ위로CCM ㅣ…](https://www.youtube.com/watch?v=aY-zdL2QUBk) | 평화로운음악 찬양카페 | 12,900 | 201,743 | 15.6 | ×23.8 | 1,170.0 | 36.8분 | 2026-05-02 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 257/257 |
| 949 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 가을은 이런 노래 들으려고 있는 거잖아🍃 🚲아침부터 설레는 느좋 팝송.zip🎧 카페음악…](https://www.youtube.com/watch?v=h03aGRBo6m8) | OOOffi | 25,600 | 399,692 | 15.6 | ×14.6 | 5,757.9 | 631.4분 | 2026-08-13 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 42/47 |
| 950 | [[PLAYLIST] 비 오는 날 계속 듣게 되는 발라드 7곡 ☔ ∣ 감성발라드 · 사랑노래 · 여름 플레이…](https://www.youtube.com/watch?v=fG0GudU56S0) | 뮤직앤라이트 Music&… | 8,640 | 134,693 | 15.6 | ×17.9 | 1,242.1 | 27.9분 | 2026-07-05 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 112/112 |
| 951 | [Rumi Sufi Healing Music for Anxiety Relief & Inner Peace ∣ …](https://www.youtube.com/watch?v=Whuol6tvJ5w) | Whispering Sp… | 4,360 | 67,798 | 15.6 | ×20.4 | 1,445.1 | 88.1분 | 2026-09-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 5/6 |
| 952 | [ボサノバ カフェ 朝カフェ｜気分が晴れる心地よい女性ボーカル リラックス音楽 海の見えるカフェ（作業用BGM・波音）（…](https://www.youtube.com/watch?v=UJ00ifFN3jQ) | Relax Lofi Li… | 33,400 | 519,186 | 15.5 | ×59.4 | 3,277.4 | 180.3분 | 2026-05-16 | 3. 공부·집중·작업 | 음악 | 설명 | 53/53 |
| 953 | [국악딴따라 노래모음｜30곡 연속듣기](https://www.youtube.com/watch?v=VctWdCriD_k) | 국악딴따라 | 35,000 | 543,969 | 15.5 | ×11.0 | 10,494.7 | 91.7분 | 2026-08-31 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 344/361 |
| 954 | [[Playlist] 마음이 편안해지는 힐링 피아노 ∣ Healing Piano Music for Stres…](https://www.youtube.com/watch?v=o0F2bvcNLMc) | Piano Haven | 5,100 | 79,163 | 15.5 | ×17.7 | 446.3 | 194.8분 | 2026-04-27 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 16/16 |
| 955 | [Playlist ∣ 틀자마자 기분 좋아지는 힙합 그루브 😎 ∣ GROOVE · JAZZHOP ∣ 카페 · …](https://www.youtube.com/watch?v=5ThjSEl5Dvs) | PoponWave | 23,000 | 354,075 | 15.4 | ×24.0 | 1,973.7 | 223.3분 | 2026-04-25 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 121/121 |
| 956 | [[외모지상주의 BGM] Unconscious 3 ∣ Lookism BGM](https://www.youtube.com/watch?v=BIE83KOrsgk) | 루트레이블 (ROUTEL… | 13,200 | 201,550 | 15.3 | ×7.0 | 1,373.4 | 5분 | 2026-05-28 | 기타 | 음악 | 설명 | 211/213 |
| 957 | [African Healing Music ∣ Zulu Voices for Anxiety Relief & Em…](https://www.youtube.com/watch?v=Nt0so0uLUoI) | africavoices | 4,770 | 72,603 | 15.2 | ×41.8 | 1,253.6 | 92.4분 | 2026-08-25 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 22/22 |
| 958 | [매일 듣기 좋은 편안한 클래식🌿∣행복한 힐링 클래식 음악☕∣클래식 명곡 18곡 모음🎵](https://www.youtube.com/watch?v=DTVWGGI7nKE) | 클래식라이프Classic | 23,600 | 358,433 | 15.2 | ×54.1 | 2,670.7 | 68분 | 2026-06-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 99/99 |
| 959 | [가장 편안하고 깊은 잠에 빠지게 만드는 부드러운 빗소리 ASMR ∣ 수면유도 백색소음](https://www.youtube.com/watch?v=qOwxf0IAk_E) | Cozy Rainy Da… | 9,320 | 141,559 | 15.2 | ×18.8 | 1,492.7 | 360분 | 2026-07-19 | 1. 수면·명상·힐링 | 자연 소리·백색소음 | 설명 | 27/30 |
| 960 | [지금 꼭 들으세요 🙏 아들 일이 잘 풀립니다 ∣ 경주 불국사의 기도 음악 #불교음악 #자녀기도노래](https://www.youtube.com/watch?v=QmfOTgF-Akw) | 연등 아래서 | 11,300 | 170,960 | 15.1 | ×34.2 | 1,014.9 | 35.6분 | 2026-05-06 | 기타 | 음악 | 설명 | 4,056/4,083 |
| 961 | [Easy Listening Music for Relaxation, Study, Work & Stress R…](https://www.youtube.com/watch?v=W-QDYTQch9c) | Luxenza Music | 4,610 | 69,306 | 15.0 | – | 578.6 | 18.6분 | 2026-06-24 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 2/2 |
| 962 | [[커버송 모음 50곡] (중간 광고 없어요^^:) /그 시절 추억의 노래 50곡/ 구독자 선정곡 1위~50…](https://www.youtube.com/watch?v=av1_naa9D2o) | 음악과 여행 | 26,100 | 388,855 | 14.9 | ×363.8 | 4,730.8 | 214.9분 | 2026-08-01 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 238/240 |
| 963 | [Cafe Reggae 🌴 Chill Island Vibes ∣ Relaxing Reggae Music fo…](https://www.youtube.com/watch?v=407QqF8EBko) | AI IRIE FM | 39,500 | 585,361 | 14.8 | ×29.1 | 3,447.0 | 61분 | 2026-05-05 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 129/129 |
| 964 | [💎 "신이내린 목소리네요..." 100년에 한번 있을까 말까 한 희귀한 음색 ㄷㄷ;; 귀한 노래만 엄선 ∣…](https://www.youtube.com/watch?v=5vdkZXq8IVY) | 7080사랑해요 | 33,500 | 489,379 | 14.6 | ×75.7 | 3,296.2 | 68.1분 | 2026-05-26 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 358/358 |
| 965 | [BGMで巡る東京ディズニーランド&ディズニーシー 【総集編 2 】](https://www.youtube.com/watch?v=PQH90HnjyO4) | ネンサウンド | 37,600 | 548,647 | 14.6 | ×3.9 | 3,125.6 | 240.1분 | 2026-04-29 | 기타 | 정보·해설 | 설명 | 52/52 |
| 966 | [여름 바닷가 테라스카페 커피한잔 너무좋다 ∣Vol.177∣ 7080 라디오 l 올드팝송 명곡 ∣ Coffe…](https://www.youtube.com/watch?v=NczlNLq6beY) | moka melody | 14,600 | 212,684 | 14.6 | ×10.7 | 1,570.9 | 661.1분 | 2026-06-08 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 77/77 |
| 967 | [기분전환 200%🔥 도파민 터지는, 신나는 노래들🎧 ∣ EDM ∣ Playlist ∣ 클럽음악 ∣ 노동요 …](https://www.youtube.com/watch?v=Tr5-cBvP22g) | DJ Corgi | 13,300 | 190,651 | 14.3 | ×21.3 | 1,293.3 | 150.8분 | 2026-05-27 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 31/31 |
| 968 | [눕자마자 바로 기절 숙면 빗소리, [중간광고없음]10분후 검은화면, "머리 대자마자 5분 만에 기절했어요"…](https://www.youtube.com/watch?v=MGtgljKRiaI) | 빗소리 자장가 Rain … | 22,300 | 314,232 | 14.1 | ×23.0 | 2,298.6 | 420분 | 2026-06-07 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 54/54 |
| 969 | [Relaxing Healing Music for Stress, Anxiety, and Depression …](https://www.youtube.com/watch?v=Pxc3SMtKGPo) | Clara Monica … | 3,500 | 49,164 | 14.1 | ×1.5 | 987.4 | 25.3분 | 2026-09-02 | 1. 수면·명상·힐링 | 음악 | 설명 | 18/18 |
| 970 | [Garbh Sanskar Deep Sleep Music 🌙 शांत संगीत ∣ Pregnancy Rel…](https://www.youtube.com/watch?v=r-WZM4San-c) | Swarmaa | 16,200 | 226,362 | 14.0 | ×524.0 | 1,602.3 | 5.5분 | 2026-06-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 39/39 |
| 971 | [[Playlist]공간의 분위기 채우는☕️[중간광고없음]카페 매장 음악 🎧그냥 틀어두세요, 차 마실 때, …](https://www.youtube.com/watch?v=kqvHu52KHmQ) | BGMBUCKS | 19,800 | 275,629 | 13.9 | – | 1,678.1 | 69.3분 | 2026-05-11 | 4. 카페·매장·라운지 | 연주 | 설명 | 82/82 |
| 972 | [☀️108𝐓𝐈𝐌𝐄𝐒 Activate High Intelligence: Gayatri Mantra Medit…](https://www.youtube.com/watch?v=_7EQF3GWDIM) | Inner Harmony… | 24,500 | 337,308 | 13.8 | ×101.5 | 1,889.1 | 60분 | 2026-04-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 117/117 |
| 973 | [주부들의 휴식 시간을 채워줄 팝송 Best 100 ∣ EverPop 명곡팝 컬렉션 ∣ 올드팝송 ∣ 7080…](https://www.youtube.com/watch?v=D4H7ItMDIGU) | 추억의 올드팝 EverP… | 15,800 | 216,181 | 13.7 | ×9.7 | 1,634.1 | 117.5분 | 2026-06-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 57/57 |
| 974 | [💃🏼노동요 들으면서 파라파라나 춰야겠다ㅣK-POP PLAYLISTㅣRESCENE, AESPA, CORTIS…](https://www.youtube.com/watch?v=uAE7TcPSJn0) | Tezz Boyz 서테즈… | 38,900 | 532,154 | 13.7 | ×61.4 | 4,538.7 | 76.1분 | 2026-06-27 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 23/23 |
| 975 | [매일듣는 편안한 클래식 음악🎵∣🌿힐링 클래식 명곡 모음 #클래식 #클래식 음악 #편안한 클래식](https://www.youtube.com/watch?v=ek_Tc24cziw) | 클래식라이프Classic | 23,600 | 321,580 | 13.6 | ×48.6 | 1,867.7 | 55.6분 | 2026-05-03 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 64/65 |
| 976 | [⠀](https://www.youtube.com/watch?v=mDkyPzypfuo) | islistening | 32,400 | 437,704 | 13.5 | ×7.5 | 3,528.0 | 21.9분 | 2026-06-20 | 기타 | 플레이리스트·모음 | 설명 | 125/127 |
| 977 | [【Nhất Định Phải Nghe Dành Cho Người Mất Ngủ!】Nhạc Piano Nhẹ…](https://www.youtube.com/watch?v=1-OgDgY_peU) | Nhạc Ngủ Thư … | 48,900 | 650,742 | 13.3 | ×19.6 | 5,013.8 | 182.7분 | 2026-06-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 184/186 |
| 978 | [새벽에 듣기좋은 메이플 로파이 재즈 ∣ 1시간 작업·공부 음악](https://www.youtube.com/watch?v=N5AE0jDAY2o) | DOKANG | 20,400 | 271,448 | 13.3 | ×24.5 | 1,686.9 | 63.9분 | 2026-05-14 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 155/156 |
| 979 | [[Masterpiece Series] Albinoni Adagio – 4 Variations Songs o…](https://www.youtube.com/watch?v=OFfc765eTgY) | WilliamPoetic… | 40,600 | 539,505 | 13.3 | ×44.7 | 3,050.9 | 17.4분 | 2026-04-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 781/781 |
| 980 | [“프린세스 티니핑송“ 피아노 커버(Princess Teenieping Song Piano Cover)](https://www.youtube.com/watch?v=BS-GSU9dLqk) | MUJINS 뮤진스 | 19,200 | 253,449 | 13.2 | ×32.9 | 1,823.5 | 6.9분 | 2026-06-05 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 49/50 |
| 981 | [아침까지 기절 숙면 잠 잘 오는 빗소리, [중간광고없음]10분후 검은화면, "눈 뜨니 개운한 아침이에요" …](https://www.youtube.com/watch?v=pkUgoZ7h_2M) | 빗소리 자장가 Rain … | 22,300 | 290,463 | 13.0 | ×21.3 | 1,807.4 | 420분 | 2026-05-14 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 40/40 |
| 982 | [Faith: You Were Never Walking Alone ∣ Heavenly Meditation M…](https://www.youtube.com/watch?v=_psuP3ukwOY) | Healing Ether | 45,400 | 571,534 | 12.6 | ×61.0 | 3,481.4 | 71.2분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 376/381 |
| 983 | [[커버(cover)송] 카페 - "여인" 원곡 : 솔개트리오 / 밤에 들으면 더 좋은 노래 ∣ 가요 ∣ k…](https://www.youtube.com/watch?v=zmb2j7REliY) | 음악과 여행 | 26,100 | 328,429 | 12.6 | ×307.2 | 2,484.4 | 5분 | 2026-06-12 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 25/25 |
| 984 | [🌈Album Preview ∣ Find the Full Album in the Playlist ∣ Cele…](https://www.youtube.com/watch?v=2qh-NuD0YMs) | Calm Music & … | 3,470 | 42,304 | 12.2 | ×386.3 | 1,266.8 | 4.8분 | 2026-09-18 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 1/1 |
| 985 | [Kiven Mukhre Ton Nazraan ∣ Ustad Nusrat Fateh Ali Khan ∣ Da…](https://www.youtube.com/watch?v=PMqkvHE1cm0) | XAN | 24,700 | 297,641 | 12.1 | ×30.2 | 1,987.7 | 4.9분 | 2026-05-25 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 158/158 |
| 986 | [숲에서 쉬는 효과🌳머리가 맑아지는 치유명상음악 ∣ 3시간, 힐링음악, 명상음악 ∣ Relaxing Musi…](https://www.youtube.com/watch?v=yq-lSVEu7U0) | 살구사운드 SalguSo… | 10,700 | 127,389 | 11.9 | ×9.6 | 4,195.4 | 191.9분 | 2026-09-21 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 43/47 |
| 987 | [Mama Said ∣ Ogryn Chain Gang Blues Work Song ∣ Warhammer 40…](https://www.youtube.com/watch?v=H6yrpYWMyRs) | Solar Void | 20,800 | 246,905 | 11.9 | ×26.8 | 1,444.5 | 6분 | 2026-05-04 | 2. 자연 소리·백색소음 | 음악 | 설명 | 395/395 |
| 988 | [우연히 들었는데 첫 곡부터... 너무 좋다 ∣ 7080 추억의 올드 팝송 모음 Old Pop Song Pl…](https://www.youtube.com/watch?v=ktav8W-fW8I) | theoldpopsong | 40,800 | 483,534 | 11.8 | ×29.2 | 2,710.2 | 58.3분 | 2026-04-26 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 287/287 |
| 989 | [가을이 오면... 커피향이 가득한 카페에서 듣고 싶은 음악](https://www.youtube.com/watch?v=4lPZuU2kCbA) | EverOldies | 44,800 | 529,822 | 11.8 | ×64.7 | 10,940.1 | 96.9분 | 2026-09-03 | 4. 카페·매장·라운지 | 음악 | 설명 | 292/316 |
| 990 | [Awit ng Paghahangad by Bukas Palad Music Ministry ∣ Senti P…](https://www.youtube.com/watch?v=5yDRTUMvk3I) | Clyde Pianist… | 12,000 | 141,394 | 11.8 | ×26.6 | 1,224.8 | 7.2분 | 2026-06-28 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 102/102 |
| 991 | [정서안정과 고운 마음을 위한 잔잔하고 아름다운 음악 l 어린이집 유치원 교실 편안한 배경 음악](https://www.youtube.com/watch?v=ONTpCdvC9mo) | 조이멜로디 JOY MEL… | 21,600 | 249,862 | 11.6 | ×24.6 | 1,474.8 | 82.3분 | 2026-05-05 | 기타 | 음악 | 설명 | 0/0 |
| 992 | [싱그러운 여름 아침, 꽃향기가 스며드는 기분좋은 카페음악 ∣ 계속 듣게 되는 감성팝송 ∣ Old Pop P…](https://www.youtube.com/watch?v=EnD2m1z3fkM) | 선율향기 | 11,500 | 132,588 | 11.5 | ×33.9 | 1,008.9 | 91.5분 | 2026-06-12 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 72/72 |
| 993 | [The Odyssey - Odysseus (EPIC Piano Cover)](https://www.youtube.com/watch?v=jtUq7gMr-7k) | Laurie Théber… | 46,000 | 529,808 | 11.5 | ×39.8 | 5,589.2 | 6.3분 | 2026-07-19 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 192/192 |
| 994 | [한 줌 흙으로 돌아가는 길 ∣ 황혼길의 깨달음 국악 판소리트로트](https://www.youtube.com/watch?v=Vb3VooJUgyk) | Nana Music | 10,000 | 114,613 | 11.5 | ×135.2 | 941.1 | 7.6분 | 2026-06-22 | 9. 가요·발라드·트로트 | 음악 | 설명 | 106/110 |
| 995 | [[𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁] 인스타에서 한번쯤 들어본 느@좋 플리](https://www.youtube.com/watch?v=4qcGtkqrfMk) | 프리다앤 / FRIDA-… | 41,500 | 473,086 | 11.4 | ×49.6 | 2,767.3 | 60.8분 | 2026-05-04 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 19/19 |
| 996 | [🔥한 번 들으면 멈출 수 없는 역설적 감성🔥 락트롯 ∣ 가슴속 응어리를 뻥~ 뚫어버리는 사이다 보컬 ∣ 도…](https://www.youtube.com/watch?v=LmEOZx2IH9M) | 노래마실 [ Music … | 2,790 | 31,666 | 11.3 | ×59.0 | 253.4 | 4.3분 | 2026-06-19 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 19/19 |
| 997 | [「영화 〈애수〉, 다시 노래가 되다｜세월이 지나도 남는 영화](https://www.youtube.com/watch?v=cIBIrAEYVZM) | 절로 가는 이야기 | 2,560 | 29,000 | 11.3 | ×10.3 | 1,786.4 | 4.6분 | 2026-10-06 | 기타 | 음악 | 설명 | 43/43 |
| 998 | [Rod Wave - It Will All Work Out - (Official Music Video)](https://www.youtube.com/watch?v=OHYv2zYBdfU) | Street Empire… | 1,570 | 17,757 | 11.3 | ×27.6 | 134.7 | 13분 | 2026-06-12 | 기타 | 한 곡 | 없음 | 5/5 |
| 999 | [Enthiran BGM ∣ A.R. Rahman ∣ 80-Piece Symphony Orchestra](https://www.youtube.com/watch?v=swMgOH67TdI) | Australian In… | 32,100 | 347,042 | 10.8 | – | 2,425.1 | 8.5분 | 2026-06-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 486/486 |
| 1000 | [【ドッカンバトル】超サイヤ人孫悟空 変身 bgm](https://www.youtube.com/watch?v=nwzLO39prTs) | メガゲン | 21,200 | 225,198 | 10.6 | ×8.0 | 1,445.4 | 10.1분 | 2026-05-19 | 기타 | 음악 | 없음 | 374/375 |
| 1001 | [【ドッカンバトル】超サイヤ人孫悟空 本気 bgm](https://www.youtube.com/watch?v=rr_DEN34wp0) | メガゲン | 21,200 | 221,987 | 10.5 | ×7.9 | 4,117.3 | 10.1분 | 2026-08-29 | 기타 | 음악 | 없음 | 175/180 |
| 1002 | [🌸나훈아 - 무시로 (Blues Remix) – 이 감성 뭐냐… l 🎙️별이트로트](https://www.youtube.com/watch?v=bBz2DSGQSIw) | 별이트로트 | 8,030 | 83,828 | 10.4 | ×26.6 | 478.6 | 4.3분 | 2026-04-30 | 9. 가요·발라드·트로트 | 음악 | 설명 | 29/29 |
| 1003 | [듣자마자 어깨춤 터지는 신명나는 트로트 찬불가 14곡 #불교음악 #트로트찬불가](https://www.youtube.com/watch?v=EYh7Yz748vs) | 연꽃선율 | 21,500 | 221,417 | 10.3 | ×375.9 | 1,358.8 | 61.5분 | 2026-05-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 289/289 |
| 1004 | [권태 [감성트롯 끝판왕]연속4번재생](https://www.youtube.com/watch?v=07n66F10ofY) | 리듬다방(김리다) | 1,360 | 14,001 | 10.3 | ×30.4 | 104.0 | 12분 | 2026-06-09 | 9. 가요·발라드·트로트 | 음악 | 설명 | 17/17 |
| 1005 | [슈베르트가 생의 끝에서 남긴 가장 아름다운 노래 ∣ 슈베르트 '세레나데' D.957 (Franz Schub…](https://www.youtube.com/watch?v=15GfRzMd3qw) | 클래식 여행자 (Clas… | 13,400 | 137,880 | 10.3 | ×1.9 | 826.2 | 4.2분 | 2026-05-08 | 기타 | 음악 | 설명 | 38/38 |
| 1006 | [The Throne Room ∣ House of The Dragon Season 3 Episode 2 En…](https://www.youtube.com/watch?v=s2GxTf1Ft4s) | Jeremy Brauns… | 29,300 | 300,246 | 10.2 | ×6.9 | 2,617.7 | 4.1분 | 2026-06-29 | 13. OST·사운드트랙 | 커버·직접 부른 노래 | 설명 | 163/163 |
| 1007 | [2000년대 히트곡 모음 추억의 노동요 playlist](https://www.youtube.com/watch?v=C4rRsOUQMRg) | 플리 말아주는 주모 | 25,800 | 262,530 | 10.2 | ×1.6 | 1,783.3 | 189.9분 | 2026-05-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 322/322 |
| 1008 | [Pan Flute Healing Music ∣ Sacred Andean Melodies for 2 Hours](https://www.youtube.com/watch?v=zq_vdOfFzlc) | Andean Flute … | 4,970 | 49,840 | 10.0 | ×53.5 | 391.0 | 144.8분 | 2026-06-16 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 13/13 |
| 1009 | [가질수 없는 너(1995) - 뱅크 ∣ Acoustic Cover ∣ 레트로카페](https://www.youtube.com/watch?v=FLzOl-Y5jiw) | 레트로 카페 (Retro… | 11,600 | 115,640 | 10.0 | ×22.3 | 665.8 | 4.6분 | 2026-05-01 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 9/11 |
| 1010 | [Wake Up with Krishna 🌿 Peaceful Dawn Meditation Music](https://www.youtube.com/watch?v=1A7xEA1j_Qg) | Moksha Sounds… | 37,000 | 364,150 | 9.8 | ×58.7 | 2,710.6 | 69분 | 2026-06-09 | 1. 수면·명상·힐링 | 음악 | 설명 | 176/177 |
| 1011 | [Jaxson Blue - Honest Work (Official Music Video)](https://www.youtube.com/watch?v=Sbs0YyDhlDI) | Jaxson Blue | 29,300 | 286,555 | 9.8 | – | 2,116.8 | 4.2분 | 2026-06-08 | 기타 | 한 곡 | 설명 | 73/74 |
| 1012 | [【美しいクラシック60分】思わず聴き入る名曲集｜読書・作業・リラックスBGM｜ショパン・ベートーヴェン・バッハ](https://www.youtube.com/watch?v=Us79QrAAa70) | クラシックの森 – Cal… | 49,300 | 480,034 | 9.7 | ×16.4 | 4,231.0 | 62.6분 | 2026-06-30 | 기타 | 정보·해설 | 설명 | 35/36 |
| 1013 | [농도 99%, 취향 좋은 사장님이 아껴둔 흔하지 않은 카페 플리 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 · Minimal Ca…](https://www.youtube.com/watch?v=PyA6gUmJW34) | Radear | 31,200 | 287,809 | 9.2 | ×14.7 | 1,645.4 | 236.8분 | 2026-04-30 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 96/96 |
| 1014 | [선선한 가을 밤 잠잘때 듣는 메이플 브금 (풀벌래 ASMR ) ∣ 수면유도음악 8시간](https://www.youtube.com/watch?v=mkpa_vCH-Aw) | DOKANG | 20,400 | 187,563 | 9.2 | ×17.0 | 1,294.3 | 480분 | 2026-05-30 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 61/62 |
| 1015 | [Hebt Euch #himmelfahrt #healingmusic #vikingmusic #selbsthe…](https://www.youtube.com/watch?v=QIXGLP6vZgQ) | VikingHealing | 2,610 | 23,876 | 9.2 | ×40.4 | 147.9 | 4분 | 2026-05-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 15/15 |
| 1016 | [아름다운 것도 아파 (Beautiful Things Hurt Too) ∣ 여자 듀엣 감성 발라드 Sad E…](https://www.youtube.com/watch?v=jwUGSmtsSIs) | MusicSong | 7,390 | 66,977 | 9.1 | ×166.6 | 396.7 | 4.4분 | 2026-05-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 43/43 |
| 1017 | [🏡 평생 잊지 못할 내 마음의 고향 ∣ 힐링 트로트 ∣ 혜영스님](https://www.youtube.com/watch?v=Dx4ewFSkxSg) | 혜영스님 ∣ 힐링트로트 | 7,600 | 68,022 | 8.9 | ×11.7 | 636.4 | 5.7분 | 2026-07-07 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 26/26 |
| 1018 | ["카페 음악 때문에 또 왔어요" 단골들이 숨겨두고 듣는 미니멀 팝 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 · Minimal C…](https://www.youtube.com/watch?v=fYmDt5bWDxg) | Radear | 31,200 | 278,433 | 8.9 | ×14.2 | 1,796.8 | 243.6분 | 2026-05-20 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 63/63 |
| 1019 | [중년 남자의 눈물 쏙 빼는 미친 호소력. '님은 먼곳에' (AI커버블루스 락 Ver.)#김추자 #님은먼곳에…](https://www.youtube.com/watch?v=A0SSBzDh-Ew) | 알고보니 혼비백산 | 42,900 | 374,582 | 8.7 | ×41.8 | 2,153.4 | 5.7분 | 2026-05-01 | 14. AI 음악 | AI 음악 | 설명 | 244/245 |
| 1020 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 그대여, -BM](https://www.youtube.com/watch?v=YDESKcB9ppA) | Artist BM | 8,660 | 75,624 | 8.7 | ×2.3 | 1,494.7 | 4분 | 2026-09-01 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 22/23 |
| 1021 | [텐션폭발! 운동성공! 오늘부터 내 노동요는 이거다!! [90~2000년대] 클럽 리믹스 35곡 [텐션업 플…](https://www.youtube.com/watch?v=t5GX_3shfEw) | 드루와자기 | 19,700 | 171,632 | 8.7 | ×511.6 | 1,497.1 | 125.2분 | 2026-06-29 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 63/63 |
| 1022 | [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 나른 야르한 제이팝 플리](https://www.youtube.com/watch?v=6Kd2P_Pu5Ug) | Nonohara | 1,240 | 10,778 | 8.7 | ×4.9 | 154.3 | 14.7분 | 2026-08-13 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 28/28 |
| 1023 | [One Lifetime Wasn't Enough ∣ Emotional Piano Love Ballad ∣ …](https://www.youtube.com/watch?v=b5N4DQLrfAg) | Soft Emotion … | 13,700 | 118,471 | 8.7 | ×13.6 | 1,099.8 | 6분 | 2026-07-06 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 15/15 |
| 1024 | [너와 걸으며/달달한노래/아련한노래/달콤한노래/잔잔한노래/편안한노래/가을노래/자기전에 듣기좋은 노래/여행갈때…](https://www.youtube.com/watch?v=bzVlQQuegBc) | 황금밴드 / Golden… | 1,880 | 16,032 | 8.5 | ×2.6 | 268.4 | 4.2분 | 2026-08-23 | 9. 가요·발라드·트로트 | 음악 | 설명 | 16/16 |
| 1025 | [㉖대한민국 정통 트로트 60선 (Korean Trot 60) ∣ 전설의 거장들이 빚어낸 정통 명곡 메들리 …](https://www.youtube.com/watch?v=75u_o8j9V0s) | 트로트의 맛! | 39,600 | 331,609 | 8.4 | – | 1,982.2 | 188.5분 | 2026-05-08 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 174/176 |
| 1026 | [10. 그리스 이타카, 무화과맛 재즈 ∣ playlist](https://www.youtube.com/watch?v=Nxeex1L0sYU) | dansoonhee | 16,300 | 135,944 | 8.3 | ×14.4 | 1,733.6 | 280.3분 | 2026-08-04 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 74/74 |
| 1027 | [Om Namah Shivaya Chanting ∣ Divine Shiva Meditation Music f…](https://www.youtube.com/watch?v=UsiJNIk0F88) | Echoes of Shi… | 1,620 | 13,416 | 8.3 | ×3.6 | 74.7 | 7.3분 | 2026-04-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 16/16 |
| 1028 | [432 Hz Reiki Music for Healing and Cleansing Negativity - 2…](https://www.youtube.com/watch?v=auzLrS12AUo) | Reiki Healing… | 20,000 | 165,303 | 8.3 | ×19.9 | 1,440.3 | 20분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 22/22 |
| 1029 | [🎵Do You Hear Me… — A Story of Love & Loss ∣ Full Emotional …](https://www.youtube.com/watch?v=BwNZ573NSVs) | HeartEcho AI … | 29,500 | 239,742 | 8.1 | ×34.3 | 1,363.7 | 57.9분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 364/367 |
| 1030 | [In der Walpurgisnacht brennt mein altes Ich #walpurgisnacht…](https://www.youtube.com/watch?v=jugVBYVn8ag) | VikingHealing | 2,610 | 21,218 | 8.1 | ×35.9 | 121.0 | 4.6분 | 2026-04-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 12/12 |
| 1031 | [This Will Reset Your Nervous System in Minutes ∣ Deep India…](https://www.youtube.com/watch?v=5YnCFwtGK28) | Sacred Mind H… | 8,290 | 67,120 | 8.1 | ×48.6 | 373.3 | 36.6분 | 2026-04-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 40/40 |
| 1032 | [Work Music, Deep Focus Music for ADHD Relief and Concentrat…](https://www.youtube.com/watch?v=CQ7p1pOOwrA) | Greenred Prod… | 8,540 | 68,232 | 8.0 | ×24.0 | 470.8 | 9.8분 | 2026-05-30 | 3. 공부·집중·작업 | 음악 | 설명 | 0/0 |
| 1033 | [VITAL ENERGY ∣ 432Hz • Clear Overthinking & Awaken Inner Cl…](https://www.youtube.com/watch?v=8EBBcZFo4PU) | Zen Celesta | 49,000 | 381,963 | 7.8 | ×32.6 | 5,469.7 | 60분 | 2026-08-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 102/105 |
| 1034 | [우리 행복하자 (Let's Just Be Happy) ∣ 미안하단 말보다 우리 행복하자 ∣ KR/ROM/E…](https://www.youtube.com/watch?v=d0jaFafrkkM) | 한그루브 | 50,000 | 389,519 | 7.8 | ×29.5 | 3,418.1 | 5.5분 | 2026-06-30 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 319/319 |
| 1035 | [OUR LADY OF FATIMA HEALING HYMNS ∣ Catholic Prayer Music fo…](https://www.youtube.com/watch?v=kL-iJ_qbbms) | Marian Morning | 35,100 | 273,186 | 7.8 | ×209.0 | 1,685.6 | 183.4분 | 2026-05-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 395/402 |
| 1036 | [Odysseus ∣ Epic Orchestral Cover ∣ The Odyssey Ludwig Goran…](https://www.youtube.com/watch?v=Qx1hmx1Fsmc) | Jeremy Brauns… | 29,300 | 227,698 | 7.8 | ×5.3 | 2,409.8 | 8.4분 | 2026-07-19 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 79/79 |
| 1037 | [한여름 밤의 꿈](https://www.youtube.com/watch?v=t87CPyEGmHQ) | 오레 ooree | 18,700 | 144,302 | 7.7 | ×19.2 | 1,109.4 | 119.7분 | 2026-06-14 | 기타 | 플레이리스트·모음 | 설명 | 88/88 |
| 1038 | [Fall 🍂 5 Minute Autumn Timer with Relaxing Piano Music 🍁 (N…](https://www.youtube.com/watch?v=2PQoOVZmxnY) | Timers Box | 2,920 | 22,300 | 7.6 | ×87.6 | 1,035.2 | 5분 | 2026-09-30 | 3. 공부·집중·작업 | 음악 | 설명 | 1/1 |
| 1039 | [[Fanmade OST] 하루의 끝에서/이안대군 테마 **21세기 대군부인** 감성 발라드](https://www.youtube.com/watch?v=sf5dMF71cg4) | ycmusic25 | 13,700 | 102,680 | 7.5 | ×163.5 | 611.3 | 4.1분 | 2026-05-07 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 79/79 |
| 1040 | [🎵 견디고 또 견딘 당신에게 전하는 메시지 ∣ 너의 봄이 온다 - AIIN](https://www.youtube.com/watch?v=9r7SCZtxgLQ) | 박PD 음악다방 | 9,820 | 73,007 | 7.4 | ×24.7 | 521.6 | 5.8분 | 2026-06-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 48/48 |
| 1041 | [playlist ∣ 여름과 가을사이, 내 독서용 브금](https://www.youtube.com/watch?v=zSUHxG9TGeQ) | centralgrocer… | 27,200 | 202,189 | 7.4 | ×14.9 | 1,993.7 | 225.8분 | 2026-07-12 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 50/50 |
| 1042 | [가시리 ∣ 조선힙합(Official Music Video)](https://www.youtube.com/watch?v=_uYBH28d_ys) | 조선힙합 Official | 28,600 | 212,227 | 7.4 | ×28.8 | 1,284.1 | 4.6분 | 2026-05-10 | 11. 힙합·R&B·EDM | 한 곡 | 설명 | 47/46 |
| 1043 | [Samtang Ako May Kinabuhi Pa - Piano Jazz Version ∣ jazz it …](https://www.youtube.com/watch?v=JqWXP8WjhX4) | jazz it back | 7,540 | 55,728 | 7.4 | ×7.7 | 347.9 | 4.2분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 7/7 |
| 1044 | [Playlist 2016 그곳으로](https://www.youtube.com/watch?v=JXJWz7Ky8KA) | 느좋모음집 | 29,100 | 211,851 | 7.3 | ×8.6 | 1,810.4 | 18.2분 | 2026-06-27 | 기타 | 플레이리스트·모음 | 없음 | 75/75 |
| 1045 | [🍂 Cozy September Jazz (NO MID-ROLL ADS) – Warm Piano Music …](https://www.youtube.com/watch?v=zw5ml1zLxPs) | Chill Jazz St… | 24,900 | 181,391 | 7.3 | ×17.1 | 3,785.6 | 376.4분 | 2026-09-04 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 39/39 |
| 1046 | [시작하면 시작된다 ٩(๑❛ᴗ❛๑)۶](https://www.youtube.com/watch?v=gjtaovTAbMU) | 톤톤 tonton | 20,200 | 145,520 | 7.2 | ×22.9 | 1,120.0 | 266.2분 | 2026-06-14 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 72/73 |
| 1047 | [창문으로 여름이 실려오는 브금 𓇼 ⋆.˚](https://www.youtube.com/watch?v=wStibHhXn1A) | 톤톤 tonton | 20,200 | 143,842 | 7.1 | ×22.6 | 836.7 | 250.8분 | 2026-05-03 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 58/58 |
| 1048 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 주황색, -BM](https://www.youtube.com/watch?v=63-irShSXR0) | Artist BM | 8,660 | 61,532 | 7.1 | ×1.9 | 784.2 | 4.2분 | 2026-08-04 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 23/23 |
| 1049 | [🎤 이놈아 나좀 살여줘~ / 트롯가수 창 🎶 사랑도 체력이다 인생 풍자 트롯 ✔️](https://www.youtube.com/watch?v=WFt570kk21o) | 우리인생뮤직 | 19,700 | 139,274 | 7.1 | ×50.0 | 797.8 | 4.1분 | 2026-04-30 | 9. 가요·발라드·트로트 | 음악 | 설명 | 137/139 |
| 1050 | [✨ Музыка восстановления 🕯️ Тибетские поющие чаши для глубок…](https://www.youtube.com/watch?v=hivuH3iFJRw) | МУДРЫЕ МЕДИТА… | 6,810 | 48,126 | 7.1 | ×0.8 | 455.5 | 30.3분 | 2026-07-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 29/29 |
| 1051 | [푸른 여름 사이로 🌸 여름 감성 피아노 플레이리스트 ∣ BGM ∣ 휴식·힐링·집중](https://www.youtube.com/watch?v=rHuz5RflH24) | Mellow Season | 2,870 | 20,261 | 7.1 | ×2.5 | 224.1 | 135.7분 | 2026-07-23 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 2/2 |
| 1052 | [임재현 - 웃어주지마요 Official MV](https://www.youtube.com/watch?v=L4aOBuPkpLg) | 임재현 Official | 39,100 | 273,847 | 7.0 | – | 2,609.1 | 4.4분 | 2026-07-09 | 기타 | 한 곡 | 없음 | 156/160 |
| 1053 | [김상민 - You ∣ 여성보컬 개사 커버 ∣ 폭발적인 감성 발라드](https://www.youtube.com/watch?v=uCvyMW60AD4) | 연애상황극 | 11,100 | 76,871 | 6.9 | ×32.9 | 454.5 | 4.2분 | 2026-05-06 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 17/17 |
| 1054 | [운동러들이 환장하는 '비트 깡패' 플리 ∣ 파상풍맛 외힙 노동요 playlist](https://www.youtube.com/watch?v=pNmK5x-0bkA) | 플리메이커 | 48,700 | 336,391 | 6.9 | ×5.9 | 2,137.2 | 57.1분 | 2026-05-17 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 142/144 |
| 1055 | [깊은밤 색소폰 Vol.35 ∣ 시원한 파도 휴식 🌊 ∣ 2시간 힐링 색소폰 연주 ∣ Ocean Waves …](https://www.youtube.com/watch?v=1jrUOOVjFpE) | 고향 가는 나그네 | 2,670 | 18,420 | 6.9 | ×5.6 | 204.8 | 128.2분 | 2026-07-24 | 1. 수면·명상·힐링 | 연주 | 설명 | 22/22 |
| 1056 | [술탄 오브 더 디스코 - 신나는 음악, 잘못된 인생 Good Beats,…](https://www.youtube.com/watch?v=UMinXZIMfQc) | Sultan Of The… | 39,500 | 264,861 | 6.7 | – | 3,680.8 | 4분 | 2026-08-11 | 기타 | 한 곡 | 설명 | 632/632 |
| 1057 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 요즘 제일 핫한 노동요 다 모아놨어요..🤍 (중간광고없음) 10시간 ∣ 감성힙합 R&B 플…](https://www.youtube.com/watch?v=LFFmtspEl8Q) | 중간광고없음 | 18,700 | 125,240 | 6.7 | ×4.1 | 1,191.2 | 601.7분 | 2026-07-09 | 3. 공부·집중·작업 | 플레이리스트·모음 | 없음 | 10/10 |
| 1058 | [☕️ 다시 듣고 싶은 추억의 애창곡 ∣ 유튜브 발라드 애창곡 20곡 연속듣기 ∣ 김광석 임재범 신승훈 이문…](https://www.youtube.com/watch?v=ZJHh-chAUSQ) | Korean Ballad… | 43,700 | 292,814 | 6.7 | ×242.6 | 2,603.8 | 117.5분 | 2026-07-01 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 40/41 |
| 1059 | [🍉여름에 듣기 좋은 카페 음악 🌊 여름 바닷가 카페처럼 기분 좋은 Playlist ∣ 중간 광고 없음 ∣ …](https://www.youtube.com/watch?v=SDGqz6SUFKY) | 오늘의 멜로디 Today… | 19,700 | 125,968 | 6.4 | ×25.7 | 766.4 | 121.5분 | 2026-05-10 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 31/31 |
| 1060 | [㉝대한민국 정통 트로트 100선(Vol.1)(Korean Authentic Trot 100) 한 번 틀면 …](https://www.youtube.com/watch?v=PrpsrGzD3Ag) | 트로트의 맛! | 39,600 | 252,719 | 6.4 | – | 1,896.0 | 311.1분 | 2026-06-11 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 201/210 |
| 1061 | [Healing Music ∣ Indian Classical Devotional Meditation ∣ Si…](https://www.youtube.com/watch?v=08mQREpo8HM) | RAGA FUSION | 2,100 | 13,317 | 6.3 | – | 103.0 | 18.5분 | 2026-06-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 10/10 |
| 1062 | [서러워 마라 ∣ 구름 같은 인연이더라](https://www.youtube.com/watch?v=X43yOI7dXDI) | 인생트로트 라운지 | 4,140 | 25,669 | 6.2 | – | 168.7 | 5분 | 2026-05-23 | 기타 | 음악 | 설명 | 13/13 |
| 1063 | [조선힙합🔥연실🔥듣자마자 오늘은 이 리듬🔥오늘의힐링🔥국악힙합🔥노동요🔥퓨전국악🔥Korea Joseon Hip-…](https://www.youtube.com/watch?v=iQkMFMSQVOc) | sisovibe | 2,810 | 17,348 | 6.2 | ×5.6 | 724.6 | 5.2분 | 2026-09-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 24/24 |
| 1064 | [[뮤직비디오] 🎵 사의 찬미 ∣ 원곡 윤심덕 ∣ 감성 리메이크](https://www.youtube.com/watch?v=Au2qy-W1WNA) | 초이스 라이브카페 | 2,160 | 12,645 | 5.8 | ×22.6 | 139.3 | 4.5분 | 2026-07-23 | 4. 카페·매장·라운지 | 한 곡 | 설명 | 6/6 |
| 1065 | [Playlist ∣ 여름, 토마토, 재즈](https://www.youtube.com/watch?v=fl5G97CMAvU) | 야채상회 Vege Mar… | 44,400 | 258,559 | 5.8 | ×17.7 | 2,303.0 | 133.1분 | 2026-07-02 | 7. 재즈·보사노바 | AI 음악 | 설명 | 55/55 |
| 1066 | [Multo by Cup of Joe ∣ Senti Piano Cover ∣ Clyde Pianist ∣ 4K](https://www.youtube.com/watch?v=Sz9HlKCn8Gs) | Clyde Pianist… | 12,000 | 68,346 | 5.7 | ×11.7 | 459.0 | 5.6분 | 2026-05-26 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 44/46 |
| 1067 | [𝙋𝙇𝘼𝙔𝙇𝙄𝙎𝙏 이상한 가을밤 (Halloween)](https://www.youtube.com/watch?v=rSj2Sx4vx5w) | off frame | 3,300 | 18,519 | 5.6 | ×9.0 | 1,875.5 | 15.3분 | 2026-10-12 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 41/42 |
| 1068 | [노동요로 들으려고 만든 House 하우스 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭](https://www.youtube.com/watch?v=-ExhSbJTkj8) | 노마카세 | 46,200 | 257,544 | 5.6 | ×6.0 | 6,968.7 | 52.1분 | 2026-09-15 | 3. 공부·집중·작업 | 플레이리스트·모음 | 없음 | 143/150 |
| 1069 | [Sanctum of Roots: The Sanctuary That Calls You Back to Your…](https://www.youtube.com/watch?v=Lh-IDUyiSCc) | Healing Ether | 45,400 | 253,074 | 5.6 | ×27.0 | 1,610.2 | 71.2분 | 2026-05-18 | 1. 수면·명상·힐링 | 음악 | 설명 | 55/55 |
| 1070 | [✨ Divine Royal Guanyin: Sacred Protection & Healing Music ∣…](https://www.youtube.com/watch?v=5UT5XqVBEfs) | Eternal Frequ… | 7,510 | 41,590 | 5.5 | ×3.7 | 775.6 | 29.6분 | 2026-08-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 62/62 |
| 1071 | [인생 뭐 있어 (In-saeng Mwo It-eo) ∣ 왔다 가는 바람 같은 것이지 ∣ KR/ROM/EN …](https://www.youtube.com/watch?v=h0r9xLYF474) | 한그루브 | 50,000 | 275,219 | 5.5 | ×20.8 | 1,799.3 | 4.1분 | 2026-05-22 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 125/125 |
| 1072 | [Arknights OST - Battleplan Obliteration ∣ アークナイツ/明日方舟 危機契約 …](https://www.youtube.com/watch?v=cY-y4dU2xTk) | RiverV | 49,500 | 262,962 | 5.3 | – | 2,228.9 | 4.1분 | 2026-06-26 | 기타 | 음악 | 설명 | 95/95 |
| 1073 | [🌿 𝑯𝒆𝒂𝒍𝒊𝒎𝒂𝒍𝒔 ∣ 🧘 숲속 호텔의 저녁 명상 클래스 ∣ 싱잉볼 & 잔잔한 피아노 ∣ Meditati…](https://www.youtube.com/watch?v=GjtPZpv7iKo) | 힐리멀스 | 23,000 | 121,261 | 5.3 | ×2.0 | 1,730.5 | 148분 | 2026-08-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 122/124 |
| 1074 | [🙏 기도가 잘되는 팬플룻 찬송가 3시간 ∣ 마음이 평안해지는 독서 · 묵상 · 휴식 음악 ∣ Pan Flu…](https://www.youtube.com/watch?v=QOTgCp4r7fo) | 히솝워십 ∣ Hyssop… | 36,300 | 185,459 | 5.1 | ×12.4 | 1,054.8 | 191.8분 | 2026-04-29 | 15. CCM·찬양·국악… | 긴 한 곡·반복 | 설명 | 290/290 |
| 1075 | [[Playlist] 예의 없는 조선 디바들의 노동요 🌶️💃 #어우동 #신사임당 #장화홍련 #성춘향 #바리공…](https://www.youtube.com/watch?v=2bp_rmtK96o) | 조선노래꾼 | 6,470 | 32,440 | 5.0 | – | 183.3 | 13.7분 | 2026-04-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 60/60 |
| 1076 | [Divine Royal Guanyin: Golden Phoenix Blessing & Healing Mus…](https://www.youtube.com/watch?v=W__4-TezX9M) | Eternal Frequ… | 7,510 | 37,355 | 5.0 | ×3.3 | 801.2 | 32분 | 2026-09-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 68/73 |
| 1077 | [Dopamine Music 🧘‍♂️ मन को शांत करने वाला संगीत ∣ Bansuri & …](https://www.youtube.com/watch?v=h6ERD2c1c0E) | KrishxBeats | 11,700 | 57,277 | 4.9 | ×30.4 | 838.3 | 8.2분 | 2026-08-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 12/12 |
| 1078 | [🌙 잠들기 전 듣는 하프 찬송가 3시간 VOL.2 ∣ 마음이 평안해지는 수면 찬송가 · 기도 · 묵상 ∣ …](https://www.youtube.com/watch?v=XqAFJ0UXfNM) | 히솝워십 ∣ Hyssop… | 36,300 | 176,966 | 4.9 | ×11.8 | 1,352.2 | 186.7분 | 2026-06-13 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 376/378 |
| 1079 | [Relaxing Piano Collection ∣ Best of Tyron James ∣ Passacagl…](https://www.youtube.com/watch?v=KbMFv0FHgrY) | tyron james | 24,900 | 113,237 | 4.5 | – | 1,601.9 | 19.8분 | 2026-08-12 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,221/1,254 |
| 1080 | [Dark Violin Focus Techno 🎻 Deep Work Music for Intense Conc…](https://www.youtube.com/watch?v=lC8EFwtdyyw) | INSTRUMENTAL … | 6,000 | 25,524 | 4.2 | ×17.4 | 218.0 | 17.4분 | 2026-06-27 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 37/37 |
| 1081 | [주옥같은 7080 명곡모음 🎶 7080 내 생애 가장 아름다운 추억 🎶 광고 없는 7080 좋은노래 37곡…](https://www.youtube.com/watch?v=VAQ3RjZh_9w) | Enjoy life | 10,400 | 38,624 | 3.7 | ×299.4 | 480.1 | 16.8분 | 2026-08-02 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 9/10 |
| 1082 | [SABILULUNGAN Version 2🌿 Sunda Instrumental Reggae Chill ∣ R…](https://www.youtube.com/watch?v=xtm29OfGf7w) | BASS_DRUM | 16,700 | 61,097 | 3.7 | ×23.2 | 426.5 | 4.6분 | 2026-06-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 14/14 |
| 1083 | [Mashup Không buông x Tìm em (Hngle) ∣ Alice Piano cover …](https://www.youtube.com/watch?v=Myx39SJ5uQs) | Alice Piano | 20,400 | 74,090 | 3.6 | ×19.2 | 762.0 | 8분 | 2026-07-17 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 24/24 |
| 1084 | [송골매 - 세상만사 (스토리 뮤직) / 8090명곡/ 감성음악](https://www.youtube.com/watch?v=2AfpfnGCaw4) | 스토리 뮤직 ( Stor… | 6,910 | 24,512 | 3.5 | ×24.9 | 145.5 | 4.7분 | 2026-05-06 | 9. 가요·발라드·트로트 | 음악 | 설명 | 6/6 |
| 1085 | [Reason (OST Trái tim mùa thu ) ∣ Alice Piano cover x Synt…](https://www.youtube.com/watch?v=htWfvXUplM4) | Alice Piano | 20,400 | 72,261 | 3.5 | ×18.7 | 857.9 | 10.8분 | 2026-07-30 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 10/10 |
| 1086 | [minimalist deep house for elevated concentration](https://www.youtube.com/watch?v=SSCthKXaAZQ) | deep archive | 25,200 | 87,524 | 3.5 | ×8.8 | 629.9 | 148.2분 | 2026-06-05 | 2. 자연 소리·백색소음 | 음악 | 설명 | 16/16 |
| 1087 | [우연히 들었는데 이 노래 ... 정말 너무 좋다 ∣ 7080 추억의 올드 팝송 모음 Old Pop Song…](https://www.youtube.com/watch?v=0H6Hqq-H7Y4) | theoldpopsong | 40,800 | 133,732 | 3.3 | ×8.1 | 1,101.4 | 84분 | 2026-06-22 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 109/109 |
| 1088 | [출근길 텐션 끌어올릴 때 듣는 노래 ∣ 국악퓨전 노동요 ∣ 달려](https://www.youtube.com/watch?v=L_l_mIXqCOc) | 저승팝 - 묘령강림 | 9,460 | 30,811 | 3.3 | ×13.2 | 201.5 | 4.9분 | 2026-05-22 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 52/52 |

### 자료를 받지 않은 성공 후보 (694개 중 배수 큰 40개 — 웹 화면 탐색 목록에서 승인하면 분석에 들어감, 성공 사례가 이미 채널당 2개인 채널은 뺌)

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
| [Aesthetic Road Trip Playlist 🌄 Arijit Singh Songs ∣ Calm Vi…](https://www.youtube.com/watch?v=DZIRWgMYL9g) | VibeHaven | 2,590 | 1,110,846 | 428.9 | 27.9분 | 2026-06-18 | 기타 |
| [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 전주만 들어도 심장이 뛰는 애니 OST 플리💿](https://www.youtube.com/watch?v=M16IXOXLGAI) | ASMRuru_루루 | 890 | 339,756 | 381.8 | 58.7분 | 2026-06-12 | 13. OST·사운드트랙 |
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
| [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 로제 노래 모음 ∣ ROSE Playlist](https://www.youtube.com/watch?v=2RfuCXhJNmY) | 오느레 | 112 | 31,695 | 283.0 | 27.4분 | 2026-09-18 | 기타 |
| [Just Listen to the Song](https://www.youtube.com/watch?v=GdP7Z11cm3E) | iamkorean | 767 | 208,114 | 271.3 | 45.8분 | 2026-06-21 | 기타 |
| [Ek Mulaqat (Slowed + Reverb) Mashup - Arijit Singh x Jubin …](https://www.youtube.com/watch?v=ZQ4JgVWHPwM) | Lost In Lyrics | 1,090 | 293,659 | 269.4 | 14.7분 | 2026-06-29 | 8. 로파이·시티팝·칠 |
| [ℙ𝕝𝕒𝕪𝕃𝕚𝕤𝕥 : 늙크크들 회춘시킬 애니 플리](https://www.youtube.com/watch?v=H6TQETWqS6I) | 연하네의 쓸만한 플레이리… | 826 | 220,917 | 267.4 | 131.8분 | 2026-08-17 | 기타 |
| [Ishq Risk 🔥 ∣ Ishq ∣ Ishqa Ve ∣ Ishq E Jaan ∣ Sajde ❤️ ∣ Sl…](https://www.youtube.com/watch?v=iOQi_K5ERfg) | SukumusicHindi | 3,390 | 882,165 | 260.2 | 25.4분 | 2026-09-09 | 8. 로파이·시티팝·칠 |
| [김추자 석양 1986년 공연, 원본 영상 오디오 그대로 ∣ 가사 자막 ∣ 이별 감성 발라드](https://www.youtube.com/watch?v=EquV6m5VTdY) | 엄마의 세월 - 한국 발… | 1,110 | 286,983 | 258.5 | 5분 | 2026-07-16 | 9. 가요·발라드·트로트 |
| [Luke’s Diner ∣ Gilmore Girls Ambience ∣ Cozy Acoustic Music…](https://www.youtube.com/watch?v=cT0I4tqsqB8) | Portal to Els… | 3,030 | 777,498 | 256.6 | 124.7분 | 2026-08-25 | 2. 자연 소리·백색소음 |
| [BHOJPURI PLAYLIST 🌼✨ ~{Timestamp}~ @Desi_.Diva12 #music #ae…](https://www.youtube.com/watch?v=GL7Y0gmUzG0) | Desi_.Diva12 | 6,090 | 1,553,546 | 255.1 | 12.8분 | 2026-07-05 | 기타 |
| [POV: You're in Your Devotee Era 🦚🪷✨∣ Krishna Playlist 🩵](https://www.youtube.com/watch?v=_u-AYjZwL2U) | 𝐌𝐫. | 2,670 | 652,931 | 244.5 | 11.2분 | 2026-07-31 | 기타 |

## 1-2. 같은 채널 안에서 — 잘된 영상 vs 평소 영상 (채널 크기·구독층을 뺀 비교)

채널 918곳의 최근 롱폼(7~365일)에서, 그 채널 조회수 중앙값의 ×3 넘은 **잘된 영상 3536개**와 ×0.5~1.5 인 **평소 영상 4143개** (채널당 5개씩). 같은 채널이니 차이는 채널 크기가 아니라 영상(주제·제목·썸네일·길이) 쪽이다.

### 1-2-1. 제목 특징 (잘된 영상 중 비율 vs 평소 영상 중 비율)

| 제목 특징 | 잘된 영상 | 평소 영상 | 차이 | 표시 |
|---|---|---|---|---|
| 숫자가 들어감 | 36% | 34% | +3%p |  |
| 40자 이상 | 86% | 84% | +1%p |  |
| 따옴표·괄호로 강조 | 17% | 17% | +1%p |  |
| vs 비교 | 1.5% | 1.1% | +0%p |  |
| 물음표 ? | 1.4% | 1.7% | -0%p |  |
| 말줄임 …·... | 3.4% | 3.1% | +0%p |  |
| AI | 8.7% | 8.9% | -0%p |  |
| 구분 기호(ㅣ·｜·/)로 나눔 | 62% | 62% | -0%p |  |
| 느낌표 ! | 1.6% | 1.7% | -0%p |  |
| 패턴형(공통점·특징·이유·N가지·착각·과정) | 0.1% | 0.2% | -0%p |  |
| 과정·벌어진 일·결말·결국 | 0.1% | 0.2% | -0%p |  |
| 손실 낱말(망하·날린·잃은·반토막) | 0.1% | 0.2% | -0%p |  |
| 직접·해보니·N년 기록 | 0% | 0.1% | -0%p |  |
| 빚투·신용·미수·레버리지·대출 | 0.1% | 0% | +0%p |  |
| 25자 미만 | 5.8% | 5.9% | -0%p |  |
| 이유 | 0.1% | 0.1% | +0%p |  |
| 노후·퇴직금·은퇴·50~70대 | 0.3% | 0.3% | +0%p |  |
| 사연·오디오북·실화·고백 | 0.1% | 0.1% | +0%p |  |

### 1-2-2. 주제 묶음 (잘된 영상 중 비율 vs 평소 영상 중 비율)

| 주제 묶음 | 잘된 영상 | 평소 영상 | 차이 |
|---|---|---|---|
| 6. 피아노·클래식·연주곡 | 16% | 15% | +1%p |
| 10. 팝송·K팝·J팝 | 2.2% | 1.8% | +0%p |
| 기타 | 22% | 22% | +0%p |
| 4. 카페·매장·라운지 | 3.8% | 3.5% | +0%p |
| 1. 수면·명상·힐링 | 17% | 17% | +0%p |
| 12. 커버·노래 부르기 | 3.0% | 2.8% | +0%p |
| 2. 자연 소리·백색소음 | 2.8% | 2.7% | +0%p |
| 8. 로파이·시티팝·칠 | 9.3% | 9.2% | +0%p |
| 13. OST·사운드트랙 | 1.1% | 1.1% | +0%p |
| 9. 가요·발라드·트로트 | 7.0% | 7.2% | -0%p |
| 7. 재즈·보사노바 | 2.2% | 2.5% | -0%p |
| 11. 힙합·R&B·EDM | 2.2% | 2.5% | -0%p |
| 14. AI 음악 | 0.8% | 1.1% | -0%p |
| 15. CCM·찬양·국악·동요 | 2.2% | 2.5% | -0%p |
| 5. 운동·드라이브·신나는 | 1.7% | 2.1% | -0%p |
| 3. 공부·집중·작업 | 6.8% | 7.5% | -1%p |

### 1-2-3. 제목 낱말 (같은 채널 안 — 잘된 영상에 더 자주 / 덜 나온 말, 합쳐 5번 이상)

| 낱말 | 잘된 영상 | 평소 영상 | 차이 |
|---|---|---|---|
| Best | 3.0% | 1.9% | +1%p |
| Mix | 3.6% | 2.9% | +1%p |
| Songs | 6.6% | 5.8% | +1%p |
| of | 4.0% | 3.3% | +1%p |
| song | 1.6% | 1.0% | +1%p |
| Relaxing | 8.3% | 7.6% | +1%p |
| playlist | 3.2% | 2.6% | +1%p |
| Collection | 1.0% | 0.5% | +0%p |
| Instrumental | 2.8% | 2.3% | +0%p |
| Journey | 0.8% | 0.3% | +0%p |
| 모음 | 3.8% | 3.3% | +0%p |
| BGM | 4.9% | 4.3% | +0%p |
| 가을 | 3.0% | 4.4% | -1%p |
| Music | 19% | 20% | -1%p |
| Rain | 1.3% | 2.1% | -1%p |
| Piano | 5.5% | 6.2% | -1%p |
| Study | 3.9% | 4.6% | -1%p |
| Video | 1.1% | 1.7% | -1%p |
| Focus | 4.1% | 4.6% | -1%p |
| Autumn | 1.5% | 2.0% | -0%p |

- 길이 중앙값: 잘된 영상 57.5분 · 평소 영상 55.9분
- 제목 글자 수 중앙값: 잘된 영상 72.0 · 평소 영상 72
- 타임라인(챕터) 있는 영상: 잘된 영상 28% · 평소 영상 26%

### 1-2-4. 성공 사례와 같은 채널의 평소 영상 (제목 짝 — 썸네일 짝은 5번)

| # | 성공 사례 (채널 평소 대비) | 같은 채널 평소 영상 1 | 같은 채널 평소 영상 2 |
|---|---|---|---|
| 1 | Jay Wheeler, Omar Courtz - De Lejitos (Remix) (Vi… (×161.3) | Jay Wheeler, Kennyy - Corazón De Lego (Offic… (986,185회) | Jay Wheeler, Luar La L, Torrres, Remers - Sh… (513,814회) |
| 2 | 너의 차선 (×98.7) | 한 시간만 (Instrumental) (6,550회) | 형이 말해줄게 (Instrumental) (4,776회) |
| 5 | ขึ้นใจ (3am call) (×570.2) | ขึ้นใจ (3am call) (22,558회) | กี่เหตุผล ( 1000REASONS ) (12,160회) |
| 6 | Veer Hanumana Ati Balwana Ram Ram Ratiyo Re ∣ Arj… (×2,303.7) | Peaceful Siya Ram Dhun ∣ सियाराम धुन ∣ Sitar… (1,123회) | Jai Ganesh Jai Ganesh Deva Aarti ∣ Ganpati A… (1,151회) |
| 7 | झूमका झूलनिया Slowed + Reverb ∣ KhesariLal Yadav … (×781.0) | Le Me Saiya Aa Gai Sari DuniyaChhod KelNew T… (5,000회) | Dheere Dheere Se Meri Zindagi (4K Video) Meh… (6,014회) |
| 8 | Ye Tune Kya Kiya (Slowed + Reverb) 🎧 ∣ Lofi Versi… (×4,146.9) | Late Night Sad Songs Mashup 💔 ∣ Arijit Singh… (1,218회) | Saude Bazi - Lofi ∣ Feel the pain of this so… (1,261회) |
| 9 | Khat navajot Ahuja / BGM THE BEST SONG 🥰#viral (×5,564.1) | AFGHAN JALEBI MASUK FAREBI SLOW MOTION THE B… (133회) | Tu HI MERA THE BEST SONG FEEL THE MUSIC 💝#vi… (121회) |
| 12 | [playlist] 일하다 어깨 들썩이는 케이팝 노동요 ∣∣ 4K MV (×1,612.4) | [PlayList] 무슨 감성이지 (2,427회) | [playlist] 오늘은 그냥 누워 있을래 (2,348회) |
| 13 | DARKHAAST ❤️ ∣ Arijit Singh ∣ Slowed + Reverb ∣ L… (×523.3) | Gehra Hua ❤️ ∣ Official Music Video ∣ Heart … (660회) | Mero Man Lagyo Vrindavan Dham 🙏❤️ ∣ Full Son… (710회) |
| 14 | When men loves you harder😭🌷 (×177.7) | 𝑷𝒐𝒗 : 𝒋𝒖𝒔𝒕 𝒔𝒍𝒂𝒚𝒚 𝒊𝒕.. (𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 𝒄𝒂𝒖𝒔𝒆 𝒊𝒕𝒔 𝒚𝒐… (24,985회) | They love you beyond your imagination 🌷😭🫣 (66,112회) |
| 16 | ℙ𝕝𝕒𝕪𝕃𝕚𝕤𝕥 : 늙크크들 원기 회복시킬 애니 플리 (×1,080.8) | 질주 / 이도형 - 오란고교 사교클럽 [한국판 ED] (1,057회) | [노래방] 질주 / 이도형 - 오란고교 사교클럽 [한국판 ED] (610회) |
| 17 | Cigarettes After Sex — late night playlist (×376.6) | fall in love again ∣ playlist ∣ (4,110회) | songs that feel like a memory ∣ nostalgic pl… (4,145회) |
| 21 | Achhi lagti ho (slowed + reverb ) lofi varsion 🎧 (×347.9) | Tere maste maste do nen ! ( Slowed - tere) (6,001회) | Main Rang Sharbaton Ka [Slowed+Reverb] Lyric… (5,501회) |
| 23 | uMoya 2.0 (Tycoon Remix) (×16.7) | Open Your Eyes (101,893회) | Unembeza (Extended Mix) (108,242회) |
| 24 | Kalyani [slowed & Reverb] ∣∣ With Shreya Ghoshal … (×1,984.0) | Sitaare [Slowed & Reverb] ∣∣ Arijit Singh ∣∣… (2,651회) | Lutt Le Gaya [Slowed & Reverb] ∣∣ Dhurandhar… (2,203회) |
| 26 | Tum Ho Toh - Mashup 2026 ∣ Romantic Love Song ∣ B… (×857.4) | Ek Mulaqat x Mohabbat - Mashup 2026 ∣ Romant… (3,212회) | Haara x Itna Tera Intezaar Kiya - Mashup 202… (3,319회) |
| 27 | 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 가을 설레발 플리 (×727.3) | 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 우리가 영원을 말하면 여름이 될거야 (362회) | 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 우주를 줄게 (315회) |
| 29 | 어른여자.mp3 (×1,456.5) | 살며시 눈 뜨면 집 근처 코너를 돌던 아빠 차 안 (409회) | 애니 속 히로인, 출동 준비 완★료 (423회) |
| 30 | Hey Paaro - Full Song Bgm Raj The Show Man Puneet… (×27.6) | Navagraha ∣ Kan Kanna Salige ∣ HD Song BGM ∣… (13,397회) | Usire Usire Song Video ∣ Kiccha Sudeep ∣ Rek… (14,801회) |
| 32 | 3분 안에 잠드는 수면 음악 (30분) Fall Asleep in 3 Minutes (3… (×164.9) | 수면과학 연구소의 숙면 유도 음악 (15분) Sleep Science Lab ∣… (658회) | 5분 안에 잠드는 수면 음악 (30분) Fall Asleep in 5 Minut… (585회) |

## 1-3. 하루 조회수 상위 — 구독자·올린 날짜 상관없이 (211개, 하루 조회수 큰 순)

하루 조회수 = 조회수 ÷ 올린 지 날수. 경계 = 검색에서 찾은 주제 관련 4분 이상 영상 2,839개 중 상위 10% (**하루 28,800회 이상**). 자료를 받은 영상 중 넘은 것, 채널당 2개 (V# 번호). **성공 사례(1번)와 따로** — 큰 채널 90개, 성공 사례에도 든 것 119개(‘성공 #’ 칸). 글 출처: 설명 202 · 없음 9 · 댓글 받은/달린 1,108,604/1,125,790.

| V# | 제목 | 채널 | 구독자 | 조회수 | 하루 조회수 | 배수 | 올린 지 | 길이 | 주제 묶음 | 형식 | 글 출처 | 댓글 받은/달린 | 성공 # |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V1 | [Shakira, Burna Boy - Dai Dai (Official Video)](https://www.youtube.com/watch?v=fcnDmrtj6Sk) | shakiraVEVO | 19,700,000 | 1,274,965,701 | 8,406,944.3 | 64.7 | 151.7일 | 4분 | 기타 | 한 곡 | 설명 | 362,730/363,040 |  |
| V2 | [KALYANI (with Shreya Ghoshal) OFFICIAL MUSIC VIDEO ∣ ARJN ∣…](https://www.youtube.com/watch?v=xvT1jH8B9AM) | MONEY VERSE R… | 299,000 | 270,591,425 | 2,401,274.6 | 905.0 | 112.7일 | 4.8분 | 기타 | 한 곡 | 설명 | 45,981/46,105 |  |
| V3 | [BASINGA BALAALU FULL SONG ∣ KALYAN KEYS ∣ SHEKAR VIRUS ∣ ES…](https://www.youtube.com/watch?v=A_RV2H2F9jw) | VEDHAS MUSIC | 214,000 | 215,612,604 | 1,643,207.9 | 1,007.5 | 131.2일 | 4.4분 | 기타 | 음악 | 설명 | 12,032/12,127 |  |
| V4 | [Parvati - Full Song ∣ Hanuman Ansh ∣ Sadhu Tiwari ∣ Shobhin…](https://www.youtube.com/watch?v=s2HYl12gmOY) | Times Music S… | 3,590,000 | 133,780,661 | 1,436,905.4 | 37.3 | 93.1일 | 4.8분 | 기타 | 음악 | 설명 | 17,664/17,804 |  |
| V5 | [Tera Mera Rishta - New Version ∣ Awarapan 2 ∣ Emraan, Disha…](https://www.youtube.com/watch?v=6rvUyBiBtik) | Sony Music In… | 73,300,000 | 110,185,685 | 1,432,586.6 | 1.5 | 76.9일 | 6.2분 | 기타 | 한 곡 | 설명 | 28,405/28,444 |  |
| V6 | [BLOK3 x POİZİ - ÇOK GÜZEL GÜLÜYORSUN (Official Music Vi…](https://www.youtube.com/watch?v=q2IMrkhSjSA) | Blok3 | 2,080,000 | 158,225,098 | 1,134,577.7 | 76.1 | 139.5일 | 4분 | 기타 | 한 곡 | 설명 | 22,349/22,419 |  |
| V7 | [Parvati (Full Song) ∣ Jab Zid Pe Aa Gayi Parvati ∣ Hanuman …](https://www.youtube.com/watch?v=rjfxLq3OQ0w) | Times Music | 18,000,000 | 58,483,323 | 1,126,952.7 | 3.2 | 51.9일 | 5분 | 기타 | 음악 | 설명 | 6,751/6,819 |  |
| V8 | [Vaaroon Forever (Official Video) ∣ Mirzapur The Movie ∣ Shr…](https://www.youtube.com/watch?v=SQ4jZ-EAL88) | Excel Movies | 4,740,000 | 66,226,030 | 1,019,164.4 | 14.0 | 65.0일 | 4.2분 | 기타 | 한 곡 | 설명 | 5,159/5,170 |  |
| V9 | [KALYANI (with Shreya Ghoshal) ARJN ∣ KDS ∣ FIFTY4 ∣ RONN ∣ …](https://www.youtube.com/watch?v=z5y8Clp_TdE) | Universal Mus… | 16,900,000 | 84,218,542 | 1,013,418.9 | 5.0 | 83.1일 | 4.2분 | 기타 | 한 곡 | 설명 | 10,834/10,940 |  |
| V10 | [Ala Bolelo - Lyric Video ∣ Jailer 2 ∣ Superstar Rajinikanth…](https://www.youtube.com/watch?v=hIHUeuw2yj8) | Sun TV | 33,000,000 | 57,705,263 | 933,623.1 | 1.8 | 61.8일 | 4분 | 기타 | 한 곡 | 설명 | 16,107/16,227 |  |
| V11 | [Jay Wheeler, Omar Courtz - De Lejitos (Remix) (Video Oficia…](https://www.youtube.com/watch?v=xCkf2L7gFnI) | JayWheelerVEVO | 6,750 | 120,974,274 | 832,932.6 | 17,922.1 | 145.2일 | 4.7분 | 기타 | 음악 | 설명 | 4,024/4,031 | #1 |
| V12 | [Falling In Reverse - "Joseph" (feat. Corey Taylor and Serj …](https://www.youtube.com/watch?v=Tk9TM7-eTmw) | Epitaph Recor… | 4,010,000 | 27,091,830 | 720,062.2 | 6.8 | 37.6일 | 4.3분 | 기타 | 한 곡 | 설명 | 38,146/38,025 |  |
| V13 | [JENNIE - FALLEN ANGEL (Official Video)](https://www.youtube.com/watch?v=s466YCiHfKw) | JennieRubyJan… | 24,500 | 32,524,835 | 589,583.4 | 1,327.5 | 55.2일 | 5.7분 | 10. 팝송·K팝·J팝 | 한 곡 | 설명 | 93,592/93,702 | #19 |
| V14 | [Neno Butterfly Lyric Video∣ Vishwanath and Sons ∣ Suriya, M…](https://www.youtube.com/watch?v=9dV6Hl2u3vM) | Aditya Music | 36,900,000 | 71,703,987 | 574,321.4 | 1.9 | 124.8일 | 4.1분 | 기타 | 한 곡 | 설명 | 4,162/4,190 |  |
| V15 | [[추석 특집] 제나의 트로트 메들리](https://www.youtube.com/watch?v=JYUilbw34Z0) | 안녕하세요원이입니다잘부탁… | 2,340,000 | 18,984,421 | 559,750.5 | 8.1 | 33.9일 | 11.3분 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 74,907/75,550 |  |
| V16 | [Karuppa Kooda Va - Video Song ∣ Suriya's Karuppu ∣ RJ Balaj…](https://www.youtube.com/watch?v=49x5rfxmv4E) | Think Music I… | 23,000,000 | 65,336,406 | 540,811.4 | 2.8 | 120.8일 | 4.4분 | 기타 | 음악 | 설명 | 6,306/6,346 |  |
| V17 | [Parvati (Lyrical) ∣ Jab Zid Pe Aa Gayi Parvati ∣ Hanuman An…](https://www.youtube.com/watch?v=PwTcikeQ8Wg) | Times Music | 18,000,000 | 24,070,895 | 535,415.2 | 1.3 | 45.0일 | 5.1분 | 기타 | 한 곡 | 설명 | 3,394/3,347 |  |
| V18 | [Kath Lagda - Navaan Sandhu ft Dhanda Nyoliwala ( Official M…](https://www.youtube.com/watch?v=nMozMETeCyw) | Navaan Sandhu | 1,400,000 | 66,286,259 | 501,775.1 | 47.4 | 132.1일 | 5.2분 | 기타 | 한 곡 | 설명 | 21,291/21,300 |  |
| V19 | [Pattampoochi Lyric Video ∣ Vishwanath and Sons ∣ Suriya, Ma…](https://www.youtube.com/watch?v=Bm9lLpmPM0A) | Aditya Music … | 3,390,000 | 59,460,790 | 476,257.9 | 17.5 | 124.8일 | 4.1분 | 기타 | 한 곡 | 설명 | 6,189/6,205 |  |
| V20 | [Thalapathy Kacheri Full Video (Tamil) ∣ Hon’ble CM Thalapat…](https://www.youtube.com/watch?v=6JaeasJw-QI) | T-Series | 316,000,000 | 34,088,866 | 449,407.4 | 0.1 | 75.9일 | 4.9분 | 기타 | 음악 | 설명 | 4,983/5,040 |  |
| V21 | [Narak ∣ Jai Randhhawa ∣ Shehnaaz Gill ∣ Ishqnama ∣ Arvvindr…](https://www.youtube.com/watch?v=mlb5yBGTTRI) | Tips Punjabi | 5,180,000 | 45,707,876 | 435,402.6 | 8.8 | 105.0일 | 4.4분 | 기타 | 음악 | 설명 | 6,537/6,549 |  |
| V22 | [Headliner ∣ Navaan Sandhu ∣ Haakam ( Official Video ) Shimm…](https://www.youtube.com/watch?v=GE6w7DRyqcM) | Navaan Sandhu | 1,400,000 | 43,298,719 | 419,784.3 | 30.9 | 103.1일 | 5.2분 | 기타 | 한 곡 | 설명 | 10,247/10,250 |  |
| V23 | [God Mode - Video Song ∣ Suriya's Karuppu ∣ RJ Balaji ∣@SaiA…](https://www.youtube.com/watch?v=_Vp-jCG7gno) | Think Music I… | 23,000,000 | 53,089,240 | 379,832.5 | 2.3 | 139.8일 | 4.2분 | 기타 | 한 곡 | 설명 | 5,048/5,060 |  |
| V24 | [Sambavakaari Video Song ∣ Gatta Kusthi 2 ∣ Vishnu Vishal, A…](https://www.youtube.com/watch?v=undhkaMMenU) | Sony Music So… | 21,800,000 | 34,026,356 | 333,936.2 | 1.6 | 101.9일 | 4.1분 | 기타 | 음악 | 설명 | 1,580/1,587 |  |
| V25 | [Dangrangto - 'xương rồng (intro)' (Prod. DONAL)](https://www.youtube.com/watch?v=4jjOH2FR6-E) | Dangrangto | 254,000 | 41,802,603 | 329,752.3 | 164.6 | 126.8일 | 4.2분 | 기타 | 정보·해설 | 설명 | 2,134/2,134 |  |
| V26 | [Feel The Pain - Chillout Mashup ∣ Lo-fi 2307 ∣ Arijit SIngh…](https://www.youtube.com/watch?v=D_J4cGrygxg) | Lo-fi 2307 | 1,070,000 | 4,313,177 | 314,331.8 | 4.0 | 13.7일 | 6.2분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 88/88 |  |
| V27 | [Chirya Boli Chu Chu ∣ Allah Hoo Allah Hoo ∣ Soothing Islami…](https://www.youtube.com/watch?v=qaM8EL9KDDA) | Little Heart … | 52,200 | 42,597,541 | 251,583.8 | 816.0 | 169.3일 | 4.6분 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |  |
| V28 | [Chalre Chalre Waal Song - Tu Sanwal Phul Kasturi (lyrical V…](https://www.youtube.com/watch?v=PgKjt5Aygps) | ISAR"MUSIC | 62,000 | 2,473,046 | 249,867.0 | 39.9 | 9.9일 | 4.5분 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 196/196 |  |
| V29 | [G-Wagona Wale (Official Music Video) R Nait ∣ Isha Sharma ∣…](https://www.youtube.com/watch?v=DgsZHiA03KI) | JCD MUSIC | 876,000 | 8,270,766 | 242,230.3 | 9.4 | 34.1일 | 4.3분 | 기타 | 한 곡 | 설명 | 520/520 |  |
| V30 | [Hangova - Music Video ∣ DC ∣ Lokesh Kanagaraj∣ Sun Pictures…](https://www.youtube.com/watch?v=wc8XNJ2x1Xs) | Sun TV | 33,000,000 | 20,311,874 | 188,413.7 | 0.6 | 107.8일 | 4분 | 기타 | 한 곡 | 설명 | 2,972/2,966 |  |
| V31 | [Hangova (From "DC")](https://www.youtube.com/watch?v=B6ppp6WBCKg) | Anirudh Ravic… | 31,700 | 20,083,381 | 186,205.7 | 633.5 | 107.9일 | 4.1분 | 기타 | 정보·해설 | 설명 | 0/1,466 | #67 |
| V32 | [Barsaat 🌧️∣ All Trending Songs ∣ Taare x Samjho Na x Safar …](https://www.youtube.com/watch?v=41HX_5G6eqQ) | Voxwaves | 13,600 | 8,113,845 | 179,232.9 | 596.6 | 45.3일 | 22.9분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,062/1,124 | #77 |
| V33 | [Vaaste 8K Video Song: Dhvani B, Siddharth G ∣ Tanishk B,Nik…](https://www.youtube.com/watch?v=eTl-FnVvGu0) | T-Series | 316,000,000 | 16,812,403 | 178,737.8 | 0.1 | 94.1일 | 4.3분 | 기타 | 음악 | 설명 | 1,418/1,417 |  |
| V34 | [Arijit Singh - Tujhko (from Cocktail 2) Rashmika Mandanna, …](https://www.youtube.com/watch?v=WWIfHemqSEA) | iPop Superhits | 47,300 | 24,066,819 | 171,780.7 | 508.8 | 140.1일 | 5.6분 | 기타 | 한 곡 | 설명 | 1,133/1,136 | #101 |
| V35 | [ALL TRENDING HINDI SONGS 2026...PLAYLIST #asthetic #trend #…](https://www.youtube.com/watch?v=xI0IEWIxUBQ) | Rb Lofi | 23,700 | 9,921,293 | 165,397.1 | 418.6 | 60.0일 | 7.9분 | 기타 | 플레이리스트·모음 | 없음 | 1,565/1,634 | #130 |
| V36 | [sombr - My Body Isn't Ready (official video)](https://www.youtube.com/watch?v=ofywN3NgGqY) | sombr | 1,160,000 | 19,303,379 | 163,013.3 | 16.6 | 118.4일 | 4.6분 | 기타 | 한 곡 | 설명 | 8,769/8,741 |  |
| V37 | [Achchi Lagti Ho (Slowed + Reverb) ∣ Lofi Version 🎧](https://www.youtube.com/watch?v=fc8Mab9zGkg) | GTAvexo9 | 24,100 | 15,553,534 | 162,511.3 | 645.4 | 95.7일 | 6.5분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 2,047/2,141 | #64 |
| V38 | [katseye playlist✨💋](https://www.youtube.com/watch?v=H40nuw4mebU) | maiia | 20,400 | 8,187,721 | 156,511.7 | 401.4 | 52.3일 | 21.3분 | 기타 | 플레이리스트·모음 | 없음 | 4,330/4,509 | #136 |
| V39 | [Tere Paas Main∣Main Vaapas Aaunga∣@diljitdosanjh,@ARRahman,…](https://www.youtube.com/watch?v=k3AqQzW3cGI) | Tips Official | 82,600,000 | 13,982,790 | 155,240.3 | 0.2 | 90.1일 | 4.1분 | 기타 | 한 곡 | 설명 | 1,557/1,557 |  |
| V40 | [Nếu Như Ta Chẳng Còn - MCK (ft. A$AP Ướt Mi)](https://www.youtube.com/watch?v=rYWLIJB214Q) | MCK // Nger | 1,070,000 | 19,394,869 | 153,004.1 | 18.1 | 126.8일 | 5.2분 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 5,075/5,075 |  |
| V41 | [Most Viral Phonk/Funk 2026 🎵](https://www.youtube.com/watch?v=CuR4HJsq5RA) | NTL Funk | 161,000 | 19,016,997 | 145,504.3 | 118.1 | 130.7일 | 18.4분 | 기타 | 플레이리스트·모음 | 설명 | 6,535/6,424 |  |
| V42 | [ĐẾN KHI NÀO (Hot Trend)...Mặt Trời Ngừng Chiếu ∣ Những Bản …](https://www.youtube.com/watch?v=pB64u5qBd5g) | Chà Là Chill | 38,900 | 7,327,149 | 143,795.8 | 188.4 | 51.0일 | 91.8분 | 8. 로파이·시티팝·칠 | 긴 한 곡·반복 | 설명 | 509/518 | #303 |
| V43 | [WOODZ X 이승철 - 우리만의 이야기 [Official MV]](https://www.youtube.com/watch?v=swbPnEZrQjE) | LEE SEUNGCHUL | 94,700 | 3,120,207 | 142,103.6 | 33.0 | 22.0일 | 4.2분 | 10. 팝송·K팝·J팝 | 한 곡 | 설명 | 545/545 |  |
| V44 | [ขึ้นใจ (3am call)](https://www.youtube.com/watch?v=r1Eb1qnqLzA) | Mirrr - Topic | 4,290 | 12,861,686 | 141,081.6 | 2,998.1 | 91.2일 | 4.4분 | 기타 | 음악 | 설명 | 0/281 | #5 |
| V45 | [Jaadu (Official Video) - Filmy & Rawme Hooda ∣ New Haryanvi…](https://www.youtube.com/watch?v=qU5ezUVgovg) | Real Music | 5,080,000 | 6,213,618 | 140,758.9 | 1.2 | 44.1일 | 4분 | 기타 | 한 곡 | 설명 | 2,917/2,917 |  |
| V46 | [💋 A Chatpati Playlist Only For Chatpata People 😋✨ ∣ Ultimat…](https://www.youtube.com/watch?v=3FhXwFGVaDE) | JellyBloxify | 33,100 | 17,206,844 | 124,593.0 | 519.8 | 138.1일 | 7.5분 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 2,208/2,219 | #98 |
| V47 | [Bass Thioung - BAOL (Clip Officiel) Ft. Nafi & Alassane](https://www.youtube.com/watch?v=ttkXaHl0o5g) | Bass Thioung | 645,000 | 18,355,504 | 124,164.6 | 28.5 | 147.8일 | 5.4분 | 기타 | 음악 | 설명 | 1,639/1,632 |  |
| V48 | [Mann mera (Original Version) ∣ Slowed + Reverb ∣ Gajendra V…](https://www.youtube.com/watch?v=4ObYNh1TOHY) | LOFI ZONE 990K | 16,900 | 10,547,075 | 120,983.8 | 624.1 | 87.2일 | 5분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,591/1,648 | #70 |
| V49 | [Mind relaxing lofi song Arijit Singh ∣ Soft songs ∣ Arijit …](https://www.youtube.com/watch?v=43y5rT7YjQY) | Y Music 2 | 36,300 | 17,149,587 | 119,857.6 | 472.4 | 143.1일 | 27.9분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,372/1,384 | #109 |
| V50 | [Ama hem hem](https://www.youtube.com/watch?v=rPmZucO77sg) | Thatohatsi - … | 36,400 | 12,533,226 | 119,462.7 | 344.3 | 104.9일 | 7.5분 | 기타 | 정보·해설 | 설명 | 0/2,577 | #171 |
| V51 | [Syumekal Gebre - Gojamoch Zenetu ∣ ስዩመቃል ገብሬ ∣ ጎጃሞች ዘነጡ ∣ N…](https://www.youtube.com/watch?v=adtJUEOe9sA) | Nahom Records… | 3,090,000 | 18,689,161 | 112,109.7 | 6.0 | 166.7일 | 6.9분 | 기타 | 한 곡 | 설명 | 3,764/3,761 |  |
| V52 | [Happy Morning Jazz 🎶 January Bossa Nova Instrumental and Re…](https://www.youtube.com/watch?v=qZjNyrGF4pk) | FunToon Rhymes | 9,570 | 1,775,622 | 110,923.1 | 185.5 | 16.0일 | 15.4분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 0/0 | #308 |
| V53 | [FUNK ABNORMAL (ULTRA SLOWED)](https://www.youtube.com/watch?v=8dOMXfWmghg) | SUKA. | 1,630,000 | 17,606,224 | 110,257.0 | 10.8 | 159.7일 | 5.6분 | 기타 | 플레이리스트·모음 | 설명 | 3,683/3,675 |  |
| V54 | [Pov :- Bhojpuri playlist 🔥 ∣∣ chill guys and enjoy 😎∣∣ Ansh…](https://www.youtube.com/watch?v=4mnrtxd_GhE) | Anshika | 19,600 | 8,591,962 | 109,154.1 | 438.4 | 78.7일 | 11.6분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,684/1,706 | #119 |
| V55 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Sad…](https://www.youtube.com/watch?v=KjFcRYZBKs0) | Music Nest HD | 11,800 | 2,693,124 | 107,055.9 | 228.2 | 25.2일 | 8.9분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 101/103 | #261 |
| V56 | [𝐀𝐋𝐋 𝐓𝐑𝐄𝐍𝐃𝐈𝐍𝐆 𝐇𝐈𝐍𝐃𝐈 𝐒𝐎𝐍𝐆𝐒 𝟐𝟎𝟐𝟔 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 🎀](https://www.youtube.com/watch?v=qZ78-_PdbwQ) | Aesthetic boo… | 87,100 | 12,167,144 | 102,578.8 | 139.7 | 118.6일 | 11.9분 | 기타 | 플레이리스트·모음 | 설명 | 7,609/7,607 |  |
| V57 | [Vintage Vibes: Best of 80s with Cyndi Lauper, Modern Talkin…](https://www.youtube.com/watch?v=1n5pMgUPYnk) | Disco Paradis… | 24,500 | 6,982,256 | 101,623.0 | 285.0 | 68.7일 | 117.2분 | 기타 | 플레이리스트·모음 | 설명 | 523/532 | #215 |
| V58 | [Patar Bashori ∣ পাতার বাঁশরী ∣ Lofi Bangla Song ∣ Emotional…](https://www.youtube.com/watch?v=rgKNbCrC-cc) | Jasu LOFI | 26,700 | 8,123,568 | 97,010.5 | 304.2 | 83.7일 | 4.1분 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 1,081/1,119 | #205 |
| V59 | [90’S Old Hindi Songs🥰 90s Love Song💘 Udit Narayan, Alka Yag…](https://www.youtube.com/watch?v=qDOFK8SfKmA) | 90s Lovers Po… | 17,600 | 6,427,613 | 96,916.9 | 365.2 | 66.3일 | 27.4분 | 기타 | 음악 | 설명 | 217/225 | #156 |
| V60 | [Odysseus](https://www.youtube.com/watch?v=WCxx_OVOVUw) | Ludwig Görans… | 43,300 | 9,051,097 | 92,437.4 | 209.0 | 97.9일 | 8.7분 | 13. OST·사운드트랙 | 음악 | 설명 | 0/5,631 | #281 |
| V61 | [Karuppa Kooda Va (From "Karuppu")](https://www.youtube.com/watch?v=WIbmUGWykTw) | Sai Abhyankka… | 66,600 | 15,957,067 | 90,313.3 | 239.6 | 176.7일 | 4.2분 | 기타 | 음악 | 설명 | 0/1,554 |  |
| V62 | [Hyperfocus ∣ LOCK IN for 3 Hours ∣ Deep Work Study With Me …](https://www.youtube.com/watch?v=UXwJ9RwdyHs) | Work With Paul | 18,000 | 4,058,360 | 90,020.6 | 225.5 | 45.1일 | 172분 | 3. 공부·집중·작업 | 긴 한 곡·반복 | 설명 | 492/507 | #266 |
| V63 | [[Playlist] When music is all you need](https://www.youtube.com/watch?v=XXKXpf7xFC4) | encore. | 7,210 | 2,875,464 | 89,919.8 | 398.8 | 32.0일 | 20.9분 | 기타 | 플레이리스트·모음 | 설명 | 518/627 | #140 |
| V64 | [𝐀𝐋𝐋 𝐓𝐑𝐄𝐍𝐃𝐈𝐍𝐆 𝐇𝐈𝐍𝐃𝐈 𝐒𝐎𝐍𝐆𝐒 𝟐𝟎𝟐𝟔 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 🎀 ∣COZI](https://www.youtube.com/watch?v=HNdauINck9s) | cozi_music | 29,400 | 8,086,546 | 89,913.7 | 275.1 | 89.9일 | 15.2분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 2,887/2,923 | #221 |
| V65 | [DJ Phaphane - Amapiano To The World ∣ Paris Nights](https://www.youtube.com/watch?v=O1sU1F6dZNk) | DJ Phaphane | 127,000 | 13,787,178 | 87,423.2 | 108.6 | 157.7일 | 63.9분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 5,141/5,100 |  |
| V66 | [Playlist For You To Create Fake Scenarios In Your Mind 🤍 ∣ …](https://www.youtube.com/watch?v=0gUwbTCQ78k) | NOXTUNE | 20,700 | 6,498,348 | 87,008.2 | 313.9 | 74.7일 | 12.6분 | 기타 | 플레이리스트·모음 | 설명 | 1,399/1,423 | #193 |
| V67 | [Noah Kahan - Orbiter (Official Lyric Video)](https://www.youtube.com/watch?v=OFcKm-5jSQE) | NoahKahanVEVO | 29,700 | 15,563,086 | 86,302.2 | 524.0 | 180.3일 | 4.8분 | 기타 | 한 곡 | 설명 | 1,405/1,426 |  |
| V68 | [○ Bollywood navratri song playlist ○ #navratri #garbasongs …](https://www.youtube.com/watch?v=g9nj1SDsXng) | july_luna | 4,540 | 2,666,733 | 84,401.9 | 587.4 | 31.6일 | 18.9분 | 기타 | 플레이리스트·모음 | 없음 | 102/127 | #79 |
| V69 | [Andekhi Anjaani si ∣ Slowed x Reverb ∣ lofi song ∣ lofi ver…](https://www.youtube.com/watch?v=FrqyfSyxOc4) | Midnight lofi… | 4,050 | 4,191,954 | 84,054.9 | 1,035.0 | 49.9일 | 6분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 132/133 | #35 |
| V70 | [🔥 𝗔𝗟𝗟 𝗧𝗥𝗘𝗡𝗗𝗜𝗡𝗚 𝗣𝗔𝗞𝗜𝗦𝗧𝗔𝗡𝗜 𝗦𝗢𝗡𝗚𝗦 🎶 ∣ 𝗩𝗜𝗥𝗔𝗟 𝗛𝗜𝗧𝗦 𝟮𝟬𝟮𝟲 🎧 ∣ 𝗧𝗢𝗣 …](https://www.youtube.com/watch?v=XL5PUUwrztg) | cozi_music | 29,400 | 5,695,105 | 83,830.0 | 193.7 | 67.9일 | 19.6분 | 1. 수면·명상·힐링 | AI 음악 | 설명 | 2,153/2,236 | #298 |
| V71 | ["सुकून भरी रातें 🌙 ∣ Romantic Hindi LoFi Songs ∣ Relaxing S…](https://www.youtube.com/watch?v=DU0Swx5GKB4) | Hindi Tuning | 25,200 | 2,279,766 | 82,466.5 | 90.5 | 27.6일 | 104분 | 1. 수면·명상·힐링 | 음악 | 설명 | 61/83 | #498 |
| V72 | ["Golden Autumn Pond" Beautiful Relaxing Music, Peaceful Soo…](https://www.youtube.com/watch?v=wWvxaQRIt0k) | Tim Janis | 2,170,000 | 1,097,611 | 82,326.4 | 0.5 | 13.3일 | 8.6분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 116/114 |  |
| V73 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Stu…](https://www.youtube.com/watch?v=MvV7_DKFZQA) | peacefulvibes… | 12,300 | 4,737,610 | 81,598.2 | 385.2 | 58.1일 | 16.3분 | 3. 공부·집중·작업 | 음악 | 설명 | 284/284 | #147 |
| V74 | [“모든 장르를 소화하네” 🥹 성시경이 반한 ‘고막 올라운더’ 도경수 #성시경의고막남친 ㅣ KBS 26091…](https://www.youtube.com/watch?v=ltqA0UR0I2E) | KBS 한국방송 | 2,770,000 | 3,285,160 | 81,578.1 | 1.2 | 40.3일 | 15.8분 | 기타 | 정보·해설 | 설명 | 1,502/1,502 |  |
| V75 | [Chris Brown - Fallin' (Official Video) ft. Leon Thomas](https://www.youtube.com/watch?v=-CepAYN0WyM) | ChrisBrownVEVO | 11,700,000 | 13,970,596 | 80,445.2 | 1.2 | 173.7일 | 8.5분 | 11. 힙합·R&B·EDM | 한 곡 | 설명 | 24,441/24,441 |  |
| V76 | [Very Powerful Morning Mantras ∣ Ganesh, Shiva, Hanuman,Gaya…](https://www.youtube.com/watch?v=uxQaS8og_Tc) | Vedic chants … | 126,000 | 12,005,933 | 80,117.3 | 95.3 | 149.9일 | 50.6분 | 1. 수면·명상·힐링 | 음악 | 설명 | 5,279/5,279 |  |
| V77 | [Asalayavale (From "Khalifa")](https://www.youtube.com/watch?v=3igIAOJlJ2s) | Jakes Bejoy -… | 186,000 | 7,498,472 | 80,020.2 | 40.3 | 93.7일 | 5분 | 기타 | 음악 | 설명 | 0/0 |  |
| V78 | [Shri Krishna Govind Hare Murari - Non Stop Krishna Bhajans …](https://www.youtube.com/watch?v=Tqr5PqrzeQw) | Bhajan World … | 33,000 | 9,143,789 | 79,641.8 | 277.1 | 114.8일 | 29.8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,540/1,543 | #219 |
| V79 | [Ishq X Barbaad - Mashup (Full Version) Lo-fi 2307 ∣ Jubin N…](https://www.youtube.com/watch?v=lFlK7t1INjA) | Lo-fi 2307 | 1,070,000 | 9,704,819 | 78,861.4 | 9.1 | 123.1일 | 5.8분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 300/300 |  |
| V80 | [Viral Songs Playlist 2026 ∣ Barsaat, Sheesha, Parvati, Roots](https://www.youtube.com/watch?v=nmc4ScFV3j4) | Vijay Garje | 3,540 | 1,403,754 | 78,811.6 | 396.5 | 17.8일 | 31.3분 | 기타 | 플레이리스트·모음 | 설명 | 320/411 | #142 |
| V81 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=FB8QuMi3fTs) | Z B Official … | 21,200 | 4,908,118 | 77,765.3 | 231.5 | 63.1일 | 7.7분 | 3. 공부·집중·작업 | 음악 | 설명 | 203/203 | #258 |
| V82 | [Best Morning Powerful Mantras ∣ Ganesh, Durga, Shiva, Gayat…](https://www.youtube.com/watch?v=1aDk9BdZ8uc) | Sanatan Mantr… | 100,000 | 12,883,505 | 77,758.3 | 128.8 | 165.7일 | 14.9분 | 1. 수면·명상·힐링 | 음악 | 설명 | 3,194/3,194 |  |
| V83 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=099F7hK6c8c) | Song verse Hi… | 9,700 | 2,965,412 | 77,488.6 | 305.7 | 38.3일 | 13분 | 3. 공부·집중·작업 | 음악 | 설명 | 186/189 | #203 |
| V84 | [음악중심 육아일기 ∣ T:TIME ∣ TXT (투모로우바이투게더)](https://www.youtube.com/watch?v=g9YbAlUZqa4) | TOMORROW X TO… | 13,900,000 | 10,338,347 | 77,224.3 | 0.7 | 133.9일 | 7.2분 | 기타 | 음악 | 설명 | 1,034/1,036 |  |
| V85 | [Heartbreaking 💔 songs + lofi Mashup songs Slowed Reverb son…](https://www.youtube.com/watch?v=swi-om1VW34) | JR buzdar off… | 16,400 | 4,476,229 | 76,902.4 | 272.9 | 58.2일 | 8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 202/203 | #226 |
| V86 | [Tum Jo Aaye ✨ ∣∣ Kitab Song ∣∣ Bairan ( Slowed X Reverb ) M…](https://www.youtube.com/watch?v=xyL4vZnw5xs) | Mix Facto 02 | 40,300 | 12,487,210 | 76,248.8 | 309.9 | 163.8일 | 20.3분 | 기타 | 음악 | 설명 | 2,719/2,730 | #199 |
| V87 | [CORTIS (코르티스) 'REDRED' Dance Practice (Fix ver.)](https://www.youtube.com/watch?v=kuVNutQeBBA) | CORTIS | 7,380,000 | 13,547,349 | 76,180.3 | 1.8 | 177.8일 | 4.4분 | 기타 | 음악 | 설명 | 5,480/5,493 |  |
| V88 | [Felix "다시 사랑한다 말할까" Cover (원곡 : 김동률) ∣ [Stray Kids : SKZ-RE…](https://www.youtube.com/watch?v=uvcpylgYDSU) | Stray Kids | 25,400,000 | 2,404,339 | 75,629.5 | 0.1 | 31.8일 | 4.2분 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 15,572/15,552 |  |
| V89 | [THEN・❥・ Sweet Dreams ∣ Cinematic Techno](https://www.youtube.com/watch?v=0QAKKYJJ2l0) | THEN | 9,750 | 10,080,906 | 74,312.7 | 1,033.9 | 135.7일 | 4.4분 | 기타 | 커버·직접 부른 노래 | 설명 | 491/497 | #36 |
| V90 | [NEW VIRAL BUDOTS REMIX 2026 - NONSTOP TIKTOK DANCE TREND PA…](https://www.youtube.com/watch?v=y2njcNWs9nk) | DJ EJ REMIX | 114,000 | 6,852,937 | 74,220.4 | 60.1 | 92.3일 | 26.6분 | 기타 | 음악 | 설명 | 669/669 |  |
| V91 | [90s Bollywood All Time Hit Songs ∣ 90s Evergreen Songs ∣ 90…](https://www.youtube.com/watch?v=1YddSDFIsk4) | Tips Official | 82,600,000 | 11,206,947 | 73,298.2 | 0.1 | 152.9일 | 69.4분 | 기타 | 음악 | 설명 | 441/437 |  |
| V92 | [BIGBANG (빅뱅) - 뱅뱅뱅 (BANG BANG BANG) (트로트 버전) [MV]](https://www.youtube.com/watch?v=wD9nunl0nKY) | ERRDAY DRIP (… | 232,000 | 6,845,616 | 72,656.3 | 29.5 | 94.2일 | 4.1분 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 6,325/6,338 |  |
| V93 | [LOVEIN & Ismail Uluçay - Drafting (Original Mix)](https://www.youtube.com/watch?v=clQARvetnyk) | LOVEIN | 40,500 | 12,216,195 | 71,966.4 | 301.6 | 169.7일 | 7.3분 | 4. 카페·매장·라운지 | 음악 | 설명 | 422/430 | #207 |
| V94 | [Playlist for how a villain in love sounds like 🎧🔥✨.](https://www.youtube.com/watch?v=4NVS6d5eGyA) | Fictional Hea… | 2,920 | 4,092,694 | 71,902.6 | 1,401.6 | 56.9일 | 9.7분 | 기타 | 플레이리스트·모음 | 설명 | 324/325 | #15 |
| V95 | [Sitaare [Slowed+Reverb] - Arijit Singh ∣ Amitabh Bhattachar…](https://www.youtube.com/watch?v=3_Y885eZ4Es) | Manan mp3 | 779,000 | 12,547,302 | 69,225.4 | 16.1 | 181.3일 | 4.4분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 861/856 |  |
| V96 | [Happy Morning Jazz 🎶 January Bossa Nova Instrumental and Re…](https://www.youtube.com/watch?v=cwBj4t1V_FY) | Little Masti … | 10,300 | 1,537,451 | 67,278.3 | 149.3 | 22.9일 | 14.5분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 0/0 | #357 |
| V97 | [Tera Sang Yaara - Slowed Reverb ∣∣ Atif Aslam ∣∣ Dopohor Lo…](https://www.youtube.com/watch?v=QcR63bT06iE) | Dopohor Lofi | 3,430 | 2,799,134 | 67,080.0 | 816.1 | 41.7일 | 5분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 219/227 | #46 |
| V98 | [Bedroom R&B After Hours ∣ Obsessive Love Playlist ∣ Dark ro…](https://www.youtube.com/watch?v=WRi5W4B2vgQ) | afterlove. | 7,490 | 1,892,253 | 66,034.5 | 252.6 | 28.7일 | 81.7분 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 177/189 | #246 |
| V99 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Study / Focus …](https://www.youtube.com/watch?v=KU7PfC9i9cE) | Focus Music 2… | 4,270 | 1,494,590 | 65,261.8 | 350.0 | 22.9일 | 13.8분 | 3. 공부·집중·작업 | 음악 | 설명 | 92/92 | #164 |
| V100 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 nên nghe gì khi gió Thu tràn về? 🍂📻 Playlist Nhạc …](https://www.youtube.com/watch?v=Pg39V_-aNPY) | chill out | 4,530 | 2,059,837 | 64,513.7 | 454.7 | 31.9일 | 83.5분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 236/243 | #113 |
| V101 | [A playlist of nusrat fateh ali khan all popular qawaali's 💝💘](https://www.youtube.com/watch?v=idCpl6LfnKo) | preet_slaylist | 49,800 | 10,142,363 | 63,992.7 | 203.7 | 158.5일 | 9.2분 | 기타 | 플레이리스트·모음 | 설명 | 4,952/5,021 | #288 |
| V102 | [HAN "back to life" ∣ [Stray Kids : SKZ-PLAYER]](https://www.youtube.com/watch?v=F0UIsSnotlA) | Stray Kids | 25,400,000 | 10,660,628 | 63,948.0 | 0.4 | 166.7일 | 4.3분 | 기타 | 한 곡 | 설명 | 45,159/45,174 |  |
| V103 | [When men loves you harder😭🌷](https://www.youtube.com/watch?v=2q4x4Ftz7mg) | wavy~ | 1,660 | 2,378,841 | 62,918.7 | 1,433.0 | 37.8일 | 9.3분 | 기타 | 플레이리스트·모음 | 설명 | 487/507 | #14 |
| V104 | [YOSHIKI – ENDLESS RAIN (From UNDER THE SKY)](https://www.youtube.com/watch?v=LJ5tn3-2YHI) | Yoshiki | 1,330,000 | 1,878,214 | 62,008.2 | 1.4 | 30.3일 | 7.5분 | 기타 | 한 곡 | 설명 | 628/628 |  |
| V105 | [Relax & Unwind Playlist 🎧 Trending Pop Hits 2026 🌙 Best Aco…](https://www.youtube.com/watch?v=juN2PpuhZk4) | Calm Hits | 55,300 | 5,812,487 | 61,589.7 | 105.1 | 94.4일 | 58.1분 | 기타 | 플레이리스트·모음 | 설명 | 1,089/1,089 |  |
| V106 | [Tulus - Teh Hijau ∣∣ [Mix Lirik] - eńau & Ari Lesmana, Bah…](https://www.youtube.com/watch?v=TN-3LJS2itE) | Bintik Musik | 111,000 | 6,396,917 | 61,245.6 | 57.6 | 104.4일 | 19.6분 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 507/503 |  |
| V107 | [이승철X성시경 - 말리꽃 [더 시즌즈-성시경의 고막남친] ∣ KBS 260710 방송](https://www.youtube.com/watch?v=17zQPXQS6fk) | KBS Kpop | 10,400,000 | 6,346,078 | 61,203.3 | 0.6 | 103.7일 | 4.8분 | 기타 | 음악 | 설명 | 2,777/2,801 |  |
| V108 | [Шадэ, Jony, Мальборо, Zivert, MiyaGi, MOT ∣ ХИТЫ 2026 #всех…](https://www.youtube.com/watch?v=mUll6jirang) | The Nicklaus | 51,000 | 5,929,120 | 61,027.2 | 116.3 | 97.2일 | 65.3분 | 기타 | 음악 | 설명 | 730/723 |  |
| V109 | [Throwback R&B Classics 📺 Chris Brown, Rihanna, Akon, Usher,…](https://www.youtube.com/watch?v=gCUbxsTWZ18) | R&B Afterglow | 14,400 | 5,874,965 | 60,619.4 | 408.0 | 96.9일 | 193.5분 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 698/732 | #132 |
| V110 | [A Chatpati Playlist Only For Chatpata People 😋✨ ∣ Ultimate …](https://www.youtube.com/watch?v=wNnngvJeuio) | Clumsyy Cizzy | 54,200 | 2,137,853 | 59,714.9 | 39.4 | 35.8일 | 7.5분 | 기타 | 플레이리스트·모음 | 설명 | 206/198 |  |
| V111 | [Heartbreaking 💔 Lofi Mashup 🎧Slowed + Reverb Songs ∣ Relax,…](https://www.youtube.com/watch?v=gCuJrBYRJpM) | Fiaz Baloch O… | 6,880 | 2,745,994 | 59,396.6 | 399.1 | 46.2일 | 8분 | 3. 공부·집중·작업 | 음악 | 설명 | 154/154 | #139 |
| V112 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 🍁 설레는 바람이 부는 가을이 왔나봐 ∣ 틀어두기 좋은 감성 팝송 모음](https://www.youtube.com/watch?v=jmU_fq-iTSE) | Melly Moood | 6,230 | 2,270,310 | 59,098.2 | 364.4 | 38.4일 | 188.2분 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 283/292 | #157 |
| V113 | [Darmiyaan](https://www.youtube.com/watch?v=v2TsWj3wxHM) | Rekha Bhardwa… | 8,590 | 5,537,265 | 58,889.7 | 644.6 | 94.0일 | 4.5분 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/238 | #65 |
| V114 | [Autumn Fireplace Jazz ∣ Cozy Crackling Fire Ambience](https://www.youtube.com/watch?v=q87NJ-696WM) | Midnight Fika | 4,060 | 2,276,545 | 58,748.2 | 560.7 | 38.8일 | 129.6분 | 2. 자연 소리·백색소음 | 음악 | 설명 | 207/212 | #84 |
| V115 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=ca4K-2vlfvA) | KKR rahul 09 | 16,000 | 1,645,781 | 58,167.8 | 102.9 | 28.3일 | 18.2분 | 1. 수면·명상·힐링 | 음악 | 설명 | 69/71 | #457 |
| V116 | [CORTIS (코르티스) ‘ACAI’ Dance Practice (Fix ver.)](https://www.youtube.com/watch?v=ysg6GVlzz9Y) | CORTIS | 7,380,000 | 9,000,845 | 58,132.7 | 1.2 | 154.8일 | 4.8분 | 기타 | 음악 | 설명 | 4,932/4,930 |  |
| V117 | [Ye Tune Kya Kiya (Slowed + Reverb) 🎧 ∣ Lofi Version ∣ Once …](https://www.youtube.com/watch?v=jqVvhD8Bps4) | Vɪʙᴇ Bʏ Lᴏғɪ | 2,500 | 5,050,913 | 58,015.4 | 2,020.4 | 87.1일 | 4.8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 363/369 | #8 |
| V118 | [Haryanvi playlist that walk up your inner dancer 🔥💋#lifewit…](https://www.youtube.com/watch?v=tYuLhTnHgOQ) | Venus Yadav | 11,800 | 4,725,514 | 57,899.8 | 400.5 | 81.6일 | 11분 | 기타 | 플레이리스트·모음 | 없음 | 570/592 | #138 |
| V119 | [Jay Park & LNGSHOT - 'MOYA' Official Music Video](https://www.youtube.com/watch?v=2-B4MdfuWkE) | MORE VISION | 321,000 | 8,818,498 | 57,371.9 | 27.5 | 153.7일 | 6.5분 | 기타 | 한 곡 | 설명 | 7,479/7,469 |  |
| V120 | [Perfect South Indian Playlist 🪷🦢 (+timestamps)](https://www.youtube.com/watch?v=ROBjw6FcYxs) | Being Diva 💅🏻 | 5,720 | 2,020,596 | 56,707.2 | 353.2 | 35.6일 | 7.7분 | 기타 | 플레이리스트·모음 | 설명 | 266/280 | #162 |
| V121 | [Baddie playlist 💋✨Aura+99999∣ SanviEditz #songplaylist](https://www.youtube.com/watch?v=p8u1URNm4ao) | ♡𝑺𝒂𝒏𝒗𝒊𝑬𝒅𝒊𝒕𝒛♡ | 4,820 | 2,583,301 | 56,192.5 | 536.0 | 46.0일 | 8.1분 | 기타 | 플레이리스트·모음 | 없음 | 2,195/2,277 | #91 |
| V122 | [[Playlist] Music is my drug](https://www.youtube.com/watch?v=msoR3EhPNAA) | Hugs | 6,470 | 2,667,761 | 54,828.8 | 412.3 | 48.7일 | 20.9분 | 기타 | 플레이리스트·모음 | 설명 | 538/540 | #131 |
| V123 | [Popular OPM Hits 2026 🌿 New Filipino Playlist ∣ Beautiful T…](https://www.youtube.com/watch?v=Ur4FFQT--Qw) | Serenata | 119,000 | 5,554,518 | 54,747.4 | 46.7 | 101.5일 | 70.4분 | 기타 | 플레이리스트·모음 | 설명 | 290/290 |  |
| V124 | [Coffee Shop Love Songs ∣ Relaxing Acoustic 70s 80s 90s Coll…](https://www.youtube.com/watch?v=p4zynVVTYpA) | Acoustic Memo… | 10,000 | 1,489,437 | 54,472.5 | 148.9 | 27.3일 | 80.3분 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 130/134 | #358 |
| V125 | [𝟭𝗛 𝗼𝗳 𝟮𝟬𝟮𝟲 𝗣𝗛𝗢𝗡𝗞 / 𝗙𝗨𝗡𝗞 𝗠𝗜𝗫 🔥‼️∣ 𝘓𝘰𝘯𝘶𝘵'𝘴 𝘗𝘭𝘢𝘺𝘭𝘪𝘴𝘵 😼‼️](https://www.youtube.com/watch?v=xAgGIDEsnU0) | 𝐋𝐨𝐧𝐮𝐭 | 560,000 | 3,384,770 | 53,238.7 | 6.0 | 63.6일 | 60분 | 기타 | 플레이리스트·모음 | 설명 | 2,134/2,076 |  |
| V126 | [झूमका झूलनिया Slowed + Reverb ∣ KhesariLal Yadav ∣ Bhojpuri…](https://www.youtube.com/watch?v=UgjIqEE-Eok) | officialprince | 1,910 | 3,905,222 | 52,982.7 | 2,044.6 | 73.7일 | 4.5분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 327/335 | #7 |
| V127 | [Không Buông x Từng Là Của Nhau x Tìm Em - HNGLE x BẢO ANH ∣…](https://www.youtube.com/watch?v=wVLhvXB2flE) | Chà Là Chill | 38,900 | 4,959,526 | 52,788.9 | 127.5 | 94.0일 | 91.8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 609/614 | #411 |
| V128 | [Shri Krishna Govind Hare Murari - Non Stop Krishna Bhajans …](https://www.youtube.com/watch?v=3GOzu5Hjbhw) | Radha Krishna… | 50,300 | 8,306,884 | 52,121.9 | 165.2 | 159.4일 | 29.8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 2,114/2,098 |  |
| V129 | [𝘊𝘦𝘳𝘵𝘪𝘧𝘪𝘦𝘥 𝘋𝘦𝘴𝘪 𝘉𝘢𝘯𝘨𝘦𝘳𝘴 𝘵𝘩𝘢𝘵 𝘴𝘭𝘢𝘱 (+𝘵𝘪𝘮𝘦𝘴𝘵𝘢𝘮𝘱𝘴) 💅🔥](https://www.youtube.com/watch?v=PZcsGXrrBGY) | A BEE Editz | 10,200 | 3,164,633 | 52,057.2 | 310.3 | 60.8일 | 12.9분 | 기타 | 플레이리스트·모음 | 설명 | 363/374 | #198 |
| V130 | [Deep Sleep & Chill Lofi : Bhojpuri Slowed & Reverb Songs 🎧✨…](https://www.youtube.com/watch?v=zW8T1B9Fzd0) | VLOGDIPESH | 5,220 | 728,666 | 51,439.2 | 139.6 | 14.2일 | 17.1분 | 1. 수면·명상·힐링 | 음악 | 설명 | 33/33 | #380 |
| V131 | [Top Hits Indonesia 2026 ∣ Top Hits Spotify Indonesia 2026 ∣…](https://www.youtube.com/watch?v=ANPUoFuWpEo) | ShadowBrief | 9,720 | 8,267,756 | 50,901.3 | 850.6 | 162.4일 | 65분 | 기타 | 정보·해설 | 설명 | 998/1,000 | #42 |
| V132 | [(NO MID-ROLL ADS) Cozy Rainy & Spooky Halloween 🍂 Fall Jazz…](https://www.youtube.com/watch?v=p1b2tWu4XkE) | Relaxing Chri… | 4,360 | 905,017 | 50,645.7 | 207.6 | 17.9일 | 249.2분 | 7. 재즈·보사노바 | 음악 | 설명 | 383/439 | #283 |
| V133 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=29EWidvY0b8) | AR BROTHER | 7,190 | 2,331,578 | 50,641.9 | 324.3 | 46.0일 | 18.6분 | 1. 수면·명상·힐링 | 음악 | 설명 | 87/89 | #188 |
| V134 | [मोहे नंदी बनइय्यो भोले ∣ Mohe Nandi Banaiyo Bhole Apne Kail…](https://www.youtube.com/watch?v=2Dm4aMBCG1s) | Bajao Bhakti | 649,000 | 8,855,331 | 49,379.4 | 13.6 | 179.3일 | 5.7분 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,788/1,788 |  |
| V135 | [[playlist] 일하다 어깨 들썩이는 케이팝 노동요 ∣∣ 4K MV](https://www.youtube.com/watch?v=whggKiGBSx4) | 노래듣는 고영희 | 2,390 | 3,849,689 | 49,244.3 | 1,610.8 | 78.2일 | 148.4분 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 193/196 | #12 |
| V136 | [🎧 Le Main Saiyaan Aa Gayi (Lofi) ∣ Mohabbatein ∣ Shah Rukh …](https://www.youtube.com/watch?v=iOdAwvF0kmk) | lofi.slowed_02 | 5,670 | 4,633,361 | 48,722.2 | 817.2 | 95.1일 | 7.5분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 291/296 | #45 |
| V137 | [90’S Old Hindi Songs🥰 90s Love Song💘 Udit Narayan, Alka Yag…](https://www.youtube.com/watch?v=ImUEhW6KTnM) | Flashback Bea… | 119,000 | 6,990,596 | 48,497.0 | 58.7 | 144.1일 | 26.3분 | 기타 | 음악 | 설명 | 404/402 |  |
| V138 | [Kalyani [slowed & Reverb] ∣∣ With Shreya Ghoshal ∣∣Arjn / K…](https://www.youtube.com/watch?v=rbt6SjoZlWU) | TRL Lofi | 3,880 | 4,815,089 | 48,224.2 | 1,241.0 | 99.8일 | 4.4분 | 기타 | 음악 | 설명 | 156/158 | #24 |
| V139 | [Tum Ho Toh - Mashup 2026 ∣ Romantic Love Song ∣ Bollywood S…](https://www.youtube.com/watch?v=EmsrY9EQSSE) | VS Lofi Offic… | 2,230 | 2,754,032 | 48,088.1 | 1,235.0 | 57.3일 | 5.2분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 43/45 | #26 |
| V140 | [ASTAGA BERCANDA- Akbar Chalay, Mingse ∣ MMG My Mine Gueh ∣ …](https://www.youtube.com/watch?v=2VS7QHm4MgA) | INDO POPULER … | 244,000 | 4,759,958 | 48,008.7 | 19.5 | 99.1일 | 40.5분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 741/738 |  |
| V141 | ["Quiet October Morning" Beautiful Relaxing Music, Peaceful …](https://www.youtube.com/watch?v=7CtUqbXKYEc) | Tim Janis | 2,170,000 | 587,170 | 47,612.3 | 0.3 | 12.3일 | 9.1분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 109/109 |  |
| V142 | [Narak - Lyrical ∣ Ishqnama ∣ Jai Randhhawa ∣ Shehnaaz Gill …](https://www.youtube.com/watch?v=VR881KWobuk) | Tips Punjabi | 5,180,000 | 2,223,282 | 46,485.7 | 0.4 | 47.8일 | 4.5분 | 기타 | 한 곡 | 설명 | 111/111 |  |
| V143 | [Romantic Saxophone Jazz 2026 ✨ Smooth Chill Lounge Music fo…](https://www.youtube.com/watch?v=tntu_zHVCdI) | Paris Melody … | 72,700 | 7,184,609 | 46,018.6 | 98.8 | 156.1일 | 190.9분 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 1,137/1,133 |  |
| V144 | [Michael Jackson Greatest Hits Mix ∣ Celebrating MICHAEL (20…](https://www.youtube.com/watch?v=F2-83E_iNb4) | IONEMusic | 10,700 | 4,762,804 | 45,973.4 | 445.1 | 103.6일 | 94.5분 | 기타 | 음악 | 설명 | 1,177/1,185 | #116 |
| V145 | [MIMIFY - I Waited too Long (Original Mix)](https://www.youtube.com/watch?v=F2Iga1V4cqo) | MIMIFY | 18,500 | 4,657,825 | 45,725.6 | 251.8 | 101.9일 | 7.8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 675/677 | #247 |
| V146 | [Peaceful Chill Playlist 🌙 Trending English Songs 2026 🎧 Bes…](https://www.youtube.com/watch?v=td6iCrK4MHc) | Morning Seren… | 15,600 | 1,329,362 | 45,256.5 | 85.2 | 29.4일 | 70.7분 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 137/147 | #510 |
| V147 | [Barsaat 🌧️ ∣ All Trending Songs 🎧∣ Taare x Samjho Na x Safa…](https://www.youtube.com/watch?v=xGPm2j1dDr4) | LOFI XP VIBES | 2,490 | 1,839,161 | 45,152.6 | 738.6 | 40.7일 | 23분 | 기타 | 음악 | 설명 | 193/199 | #50 |
| V148 | [Best Morning Powerful Mantras ∣ Hanuman, Ganesh, Shiva, Gay…](https://www.youtube.com/watch?v=HwIWdqpsKF8) | Bhakti Beena | 105,000 | 8,037,438 | 44,831.6 | 76.5 | 179.3일 | 12분 | 1. 수면·명상·힐링 | 음악 | 설명 | 3,004/3,004 |  |
| V149 | [Rest Your Mind ∣ Your Brain Needs Silence ∣ Dopamine Reset …](https://www.youtube.com/watch?v=UWZ_QQNKmes) | Essential Ind… | 19,100 | 5,242,650 | 44,792.4 | 274.5 | 117.0일 | 20.7분 | 1. 수면·명상·힐링 | 음악 | 설명 | 833/843 | #223 |
| V150 | [MGA MATATANG MAPANGHUSGA NONSTOP HITS VOL.1 ∣ Best OPM Regg…](https://www.youtube.com/watch?v=IbxIsoqu6s8) | VincH Music | 53,600 | 5,261,704 | 44,498.6 | 98.2 | 118.2일 | 83.2분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,713/1,704 |  |
| V151 | [Tere Bin [Slowed+Reverb] - Rahat Fateh Ali Khan, Asees Kaur…](https://www.youtube.com/watch?v=voemJVo9Lrc) | Manan mp3 | 779,000 | 6,673,044 | 44,413.4 | 8.6 | 150.2일 | 4.2분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 747/747 |  |
| V152 | [CrushX성시경 - 행복한 나를 [더 시즌즈-성시경의 고막남친] ∣ KBS 260717 방송](https://www.youtube.com/watch?v=KZwBjyQOuGQ) | KBS Kpop | 10,400,000 | 4,285,542 | 44,321.1 | 0.4 | 96.7일 | 4.7분 | 기타 | 음악 | 설명 | 1,024/1,030 |  |
| V153 | [ORANGE x HOÀNG DŨNG - “CỨ THẾ” ∣ OFFICIAL MV (From album 'D…](https://www.youtube.com/watch?v=BVwmm3dno2A) | Orange Singer… | 502,000 | 1,820,662 | 43,566.1 | 3.6 | 41.8일 | 4분 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 947/947 |  |
| V154 | [Just One More Drink -- Jazz Noir](https://www.youtube.com/watch?v=7gtIh5dF9Xk) | Tom’s Jazz Lo… | 71,000 | 6,414,861 | 43,172.0 | 90.3 | 148.6일 | 81.8분 | 7. 재즈·보사노바 | 음악 | 설명 | 1,538/1,528 |  |
| V155 | [Pov: certified Baddie playlist 🔥# playlist # baddie](https://www.youtube.com/watch?v=vzNOiBV_W6g) | it's GAURAV P… | 7,850 | 5,381,277 | 42,313.0 | 685.5 | 127.2일 | 8.3분 | 기타 | 플레이리스트·모음 | 설명 | 696/701 | #58 |
| V156 | [THE WEEKND ∣ Late Night Drive Playlist](https://www.youtube.com/watch?v=DgBM12cGM-Q) | Jostynsc | 10,300 | 5,136,117 | 41,993.5 | 498.6 | 122.3일 | 40.8분 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 304/306 | #104 |
| V157 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Chi…](https://www.youtube.com/watch?v=ki362-gbdjs) | Qais Music St… | 2,170 | 912,273 | 41,675.7 | 420.4 | 21.9일 | 7.3분 | 3. 공부·집중·작업 | 음악 | 설명 | 10/10 | #127 |
| V158 | [Steve Lacy - the feeling (Official Video)](https://www.youtube.com/watch?v=Qw20tg1v7Fc) | SteveLacyVEVO | 8,430 | 5,786,837 | 41,582.3 | 686.5 | 139.2일 | 4.6분 | 기타 | 플레이리스트·모음 | 설명 | 5,393/5,417 | #57 |
| V159 | [YARA YARA YA PHONK [All Versions] ∣∣ {NORMAL, SLOWED, SUPER…](https://www.youtube.com/watch?v=yMo3VnIH-TU) | Funk7Xqueen | 64,600 | 5,502,526 | 41,457.3 | 85.2 | 132.7일 | 8.3분 | 기타 | 긴 한 곡·반복 | 설명 | 2,234/2,234 |  |
| V160 | [Best Morning Powerful Mantras ∣ Shiva, Ganesh, Hanuman, Vis…](https://www.youtube.com/watch?v=CFV27iuas7Q) | Sacred Naad | 22,300 | 2,856,394 | 41,223.2 | 128.1 | 69.3일 | 15.7분 | 1. 수면·명상·힐링 | 음악 | 설명 | 973/1,034 | #409 |
| V161 | [Sad lo_fi🥺💔2026 ultimate](https://www.youtube.com/watch?v=q-iefUnWPCY) | mr prakash 😊 | 5,320 | 1,678,843 | 41,214.2 | 315.6 | 40.7일 | 18.6분 | 기타 | 음악 | 설명 | 143/147 | #192 |
| V162 | [Heartbreaking Lofi Mashup 💔 (Slowed + Reverb) ∣ Study, Focu…](https://www.youtube.com/watch?v=6mgb7GxwLvA) | stylish offic… | 12,100 | 2,889,364 | 41,138.1 | 238.8 | 70.2일 | 7.8분 | 3. 공부·집중·작업 | 음악 | 설명 | 132/135 | #256 |
| V163 | [katseye (clean) playlist ⊹ ࣪ ˖](https://www.youtube.com/watch?v=_VEtnBXtUNs) | 𝟑𝟎𝟑.𝐧𝐞𝐰.𝐞𝐫𝐚 | 7,780 | 3,366,462 | 40,953.0 | 432.7 | 82.2일 | 25.3분 | 기타 | 플레이리스트·모음 | 설명 | 2,599/2,602 | #123 |
| V164 | [MEGA BASS 🔊🔥 EXTREME NONSTOP EDM REMIX 💯 MONSTER DROP ⚠️ CL…](https://www.youtube.com/watch?v=Kc071SEvHgc) | Street Bass C… | 27,100 | 6,111,463 | 40,925.2 | 225.5 | 149.3일 | 42.7분 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 1,383/1,396 | #265 |
| V165 | [Jo Tere Sang KaTi RaTe 💔 Lofi Remix ∣ Emotional Slowed + Re…](https://www.youtube.com/watch?v=XKcT9t0tgbY) | Abidpro | 46,100 | 6,368,010 | 40,864.5 | 138.1 | 155.8일 | 6.3분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 809/811 | #383 |
| V166 | [uMoya 2.0 (Tycoon Remix)](https://www.youtube.com/watch?v=HropgeYirpE) | Darque - Topic | 1,330 | 1,697,005 | 40,487.9 | 1,275.9 | 41.9일 | 8.7분 | 기타 | 음악 | 설명 | 0/378 | #23 |
| V167 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=XLtdtHJExEY) | Clsxzff | 1,860 | 1,246,823 | 40,414.3 | 670.3 | 30.9일 | 19.6분 | 1. 수면·명상·힐링 | 음악 | 설명 | 173/187 | #62 |
| V168 | [POV You're back in the 90s 💗📻 ∣ Old hindi songs ∣ Bollywood…](https://www.youtube.com/watch?v=4GMIMevMn6Y) | Manii | 2,510 | 2,335,680 | 39,878.2 | 930.5 | 58.6일 | 8.2분 | 기타 | 음악 | 설명 | 803/835 | #39 |
| V169 | [🎶Spotify Hits Music 2026 ∣∣ Top Music Playlist -- Best 100 …](https://www.youtube.com/watch?v=0gvy7v6GTMo) | Soft Feelings | 5,900 | 2,739,041 | 39,191.8 | 464.2 | 69.9일 | 138.6분 | 기타 | 플레이리스트·모음 | 설명 | 188/191 | #111 |
| V170 | [여인 – 우리 가슴속 깊이 박혀 있던 그 노래, 듣는 순간 그 시절로 돌아갑니다, 이어폰 필수… 👉 첫 소…](https://www.youtube.com/watch?v=a0iBRRoDnDw) | 명곡부활단 | 105,000 | 6,699,495 | 38,964.9 | 63.8 | 171.9일 | 5.1분 | 5. 운동·드라이브·신나는 | AI 음악 | 설명 | 1,812/1,832 |  |
| V171 | [Mood Lifter Playlist (Visualizer) ∣ Feel Good Songs ∣ Natur…](https://www.youtube.com/watch?v=Rg3YlUwSkUc) | Sony Music In… | 73,300,000 | 3,252,225 | 38,327.7 | 0.0 | 84.9일 | 65.6분 | 기타 | 플레이리스트·모음 | 설명 | 159/157 |  |
| V172 | [f(x) 에프엑스 - Hot Summer (트로트 버전) [MV]](https://www.youtube.com/watch?v=ldfmc4lnwoY) | ERRDAY DRIP (… | 232,000 | 3,365,141 | 37,702.7 | 14.5 | 89.3일 | 4.2분 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 2,948/2,963 |  |
| V173 | [The Best Field Day Songs: 3 Dances + Bonus Soccer Song Incl…](https://www.youtube.com/watch?v=SSWSQKYCE0A) | Oliver’s Melo… | 276,000 | 5,237,098 | 37,060.6 | 19.0 | 141.3일 | 9.3분 | 기타 | 음악 | 설명 | 0/0 |  |
| V174 | [a playlist to make your brain shut up](https://www.youtube.com/watch?v=xIX_A2PRoW0) | HIGHWIND | 40,200 | 2,436,856 | 36,957.6 | 60.6 | 65.9일 | 62.1분 | 1. 수면·명상·힐링 | 연주 | 설명 | 811/848 | #618 |
| V175 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐅𝐨𝐫 𝐘𝐨𝐮 𝐓𝐨 𝐂𝐫𝐞𝐚𝐭𝐞 𝐅𝐚𝐤𝐞 𝐒𝐜𝐞𝐧𝐚𝐫𝐢𝐨𝐬 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐌𝐢𝐧𝐝 🤍 ∣ …](https://www.youtube.com/watch?v=flQgOwg4jLI) | Ashik's Cloud… | 15,600 | 3,805,234 | 36,630.5 | 243.9 | 103.9일 | 15.2분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 965/970 | #252 |
| V176 | [Tìm Em](https://www.youtube.com/watch?v=PnGk00MuNM4) | Hngle - Topic | 1,350 | 4,582,506 | 36,429.6 | 3,394.4 | 125.8일 | 4.6분 | 기타 | 음악 | 설명 | 0/227 | #4 |
| V177 | [New OPM Trending 2026 🎧 Tagalog Love Songs With Lyrics ∣ So…](https://www.youtube.com/watch?v=7NQYmIycWj4) | Serenata | 119,000 | 6,414,469 | 36,351.5 | 53.9 | 176.5일 | 54분 | 기타 | 플레이리스트·모음 | 설명 | 376/376 |  |
| V178 | [धनियां बनबू कनियाँ - Lofi Song ∣∣ Khesari Lal Yadav ∣∣ Dilw…](https://www.youtube.com/watch?v=s-1MerBYomA) | ꧁༒乙x°᭄Ᏼᴀʙᴜ࿐ | 3,840 | 2,029,933 | 35,419.5 | 528.6 | 57.3일 | 5.1분 | 8. 로파이·시티팝·칠 | 음악 | 없음 | 267/296 | #93 |
| V179 | [Yeh Raatein Yeh Mausam - Soft Acoustic Cover ∣ Beautiful Ni…](https://www.youtube.com/watch?v=IrLRtCGI2Oc) | Divine Soul R… | 8,280 | 5,712,633 | 35,218.1 | 689.9 | 162.2일 | 5.1분 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 277/277 | #56 |
| V180 | [12 HOURS⚡TOP MOST VIRAL PHONK/FUNK 2026 SONGS 🎵 PLAYLIST 🎵](https://www.youtube.com/watch?v=5GG_MkQYQq0) | Vaddy Daddy | 81,700 | 3,145,164 | 35,011.4 | 38.5 | 89.8일 | 719.5분 | 기타 | 플레이리스트·모음 | 설명 | 788/781 |  |
| V181 | [KUMAMICHI（熊道） — Japanese Zen Music Along the Bear’s Path](https://www.youtube.com/watch?v=vFJuk4U-V7Q) | Aether Journey | 34,200 | 1,911,920 | 34,736.4 | 55.9 | 55.0일 | 347분 | 1. 수면·명상·힐링 | 음악 | 설명 | 235/241 | #641 |
| V182 | [Kalyani Remix (Lyrics) - ARJN, KDS, FIFTY4, RONN & Shreya G…](https://www.youtube.com/watch?v=zoVYtZpo6oA) | D-Muze India | 188,000 | 3,381,451 | 34,563.6 | 18.0 | 97.8일 | 4.5분 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 652/652 |  |
| V183 | [Patar Bashori 🥀 ∣ পাতার বাঁশরী ∣ Female Version ∣ Bangla No…](https://www.youtube.com/watch?v=kQ3IwNRzLMM) | Lofix Dj Fusi… | 31,100 | 2,843,418 | 34,275.7 | 91.4 | 83.0일 | 18.4분 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 976/1,006 | #492 |
| V184 | [Viral Pop Songs Cover 2026 🎙 Top Music Playlist Hits](https://www.youtube.com/watch?v=JKRRl5-5-hw) | Acoustic Ther… | 21,000 | 5,079,427 | 34,236.3 | 241.9 | 148.4일 | 57.4분 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 설명 | 512/518 | #254 |
| V185 | [🎀Students fav playlist👀 ∣next comment∣](https://www.youtube.com/watch?v=yx9rhLzbY0A) | @vibe_withe_me | 5,400 | 2,506,093 | 33,918.6 | 464.1 | 73.9일 | 7분 | 기타 | 플레이리스트·모음 | 없음 | 1,169/1,198 | #112 |
| V186 | [POV: you discovered that ✨South Indian and Hindi ✨songs hit…](https://www.youtube.com/watch?v=lbT4VY3UKkY) | Arena | 3,490 | 2,300,755 | 33,902.6 | 659.2 | 67.9일 | 14.6분 | 12. 커버·노래 부르기 | 음악 | 설명 | 406/426 | #63 |
| V187 | [Om Namah Shivaya 🕉 #hanumanansh #backgroundmusic #trendings…](https://www.youtube.com/watch?v=YnhFtBGO2zI) | Rudree Aarya … | 2,470 | 1,543,222 | 33,882.2 | 624.8 | 45.5일 | 15.5분 | 기타 | 음악 | 없음 | 385/385 | #69 |
| V188 | [Morning Cortisol Detox 🌱 ∣ Raag Bhairavi Bansuri 432Hz for …](https://www.youtube.com/watch?v=iYO8SH-maAc) | Dhun Detox | 56,100 | 3,972,323 | 33,855.2 | 70.8 | 117.3일 | 19.1분 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,600/2,556 |  |
| V189 | [the playlist to actually enter flowstate.](https://www.youtube.com/watch?v=wdDhTr_M7kA) | Pure Grit Stu… | 20,400 | 1,810,765 | 33,846.7 | 88.8 | 53.5일 | 123분 | 기타 | 플레이리스트·모음 | 설명 | 545/553 | #503 |
| V190 | [Peek A Boo - Toxic ∣ Rocking Star Yash, Kiara Advani, Nayan…](https://www.youtube.com/watch?v=XGnxAIcb2pY) | Zee Music Com… | 123,000,000 | 1,899,706 | 33,447.3 | 0.0 | 56.8일 | 4.4분 | 기타 | 음악 | 설명 | 874/873 |  |
| V191 | [𝙋𝙤𝙫 :- 𝘽𝙝𝙤𝙟𝙥𝙪𝙧𝙞 𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩 ∣∣ 𝙘𝙝𝙞𝙡𝙡 𝙜𝙪𝙮𝙨 𝙖𝙣𝙙 𝙚𝙣𝙟𝙤𝙮 ∣∣ 𝙂𝘼𝙇𝘼𝙓𝘼𝙔…](https://www.youtube.com/watch?v=areWocW1pXI) | AYUSH | 4,310 | 1,485,637 | 33,084.2 | 344.7 | 44.9일 | 8분 | 기타 | 플레이리스트·모음 | 설명 | 180/188 | #169 |
| V192 | [Sarap Sa Tenga To VOL. 3 🌿(IBA TO!) ∣ Spiritual Roots Regga…](https://www.youtube.com/watch?v=9w_QNH2ju3A) | Just Reggae S… | 45,800 | 5,423,189 | 33,076.9 | 118.4 | 164.0일 | 64.6분 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,674/2,675 | #423 |
| V193 | [Cortisol Reset । 432Hz Krishna Bansuri Therapy for a Calm M…](https://www.youtube.com/watch?v=D5NHvEVAbWY) | Healing Raga … | 23,700 | 3,113,886 | 32,824.8 | 131.4 | 94.9일 | 65.7분 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,970/1,999 | #403 |
| V194 | [Barsaat ∣ All Trending Hindi Songs 2026 ∣ Safar × Bairan × …](https://www.youtube.com/watch?v=-hXkiB-eLfs) | SukumusicHindi | 3,390 | 1,329,356 | 31,832.0 | 392.1 | 41.8일 | 22.9분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 161/165 | #144 |
| V195 | [Best pakistani OST for you ✨🤍 ∣ Pakistani songs∣ #playlist …](https://www.youtube.com/watch?v=-VoKBfZJR5U) | shaaedits31 | 10,200 | 5,811,434 | 31,811.8 | 569.8 | 182.7일 | 17.7분 | 기타 | 플레이리스트·모음 | 설명 | 926/932 |  |
| V196 | [ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ](https://www.youtube.com/watch?v=MsjHOAq7WH0) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 14,700 | 1,613,381 | 31,713.2 | 109.8 | 50.9일 | 67.7분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,119/1,122 | #442 |
| V197 | [99% Fall Into Sleep Instantly (No Ads) • Eliminate Stress &…](https://www.youtube.com/watch?v=iVZPLhAlXUw) | Bedtime Calm … | 12,200 | 1,625,035 | 31,478.1 | 133.2 | 51.6일 | 237.9분 | 1. 수면·명상·힐링 | 음악 | 설명 | 43/43 | #397 |
| V198 | [LEO ROJAS - Top 16 Andean Pan Flute Melodies ★ Full Album -…](https://www.youtube.com/watch?v=wR5yxMCTZA0) | Andean Flute … | 4,840 | 1,639,020 | 31,002.5 | 338.6 | 52.9일 | 98.3분 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 233/240 | #174 |
| V199 | [[ 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ] 적당히 신나는 그루브 힙합 플레이리스트 ∣ Chill R&B • Cafe Music](https://www.youtube.com/watch?v=p3tvSF3BgYM) | SSoundW | 4,020 | 1,914,311 | 30,975.6 | 476.2 | 61.8일 | 89.9분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 253/253 | #107 |
| V200 | [Heartbreaking💔 mashup lofi Songs ∣ Slowed + Reverb ∣ Late N…](https://www.youtube.com/watch?v=z3H-p4r9EC4) | Soulmate Song… | 7,510 | 1,722,783 | 30,639.8 | 229.4 | 56.2일 | 8분 | 3. 공부·집중·작업 | 음악 | 설명 | 139/139 | #260 |
| V201 | [Asiwafuni](https://www.youtube.com/watch?v=9c1b0JLxKG4) | Benzoo - Topic | 11,900 | 2,542,749 | 30,301.2 | 213.7 | 83.9일 | 6.7분 | 기타 | 음악 | 설명 | 0/1,364 | #275 |
| V202 | [💖 मेरा चाँद मुझे आया नजर ∣ New Hindi Song 2026 ∣ Romantic S…](https://www.youtube.com/watch?v=FxNQw0BRhWg) | Feel The Music | 3,320 | 1,082,775 | 30,240.5 | 326.1 | 35.8일 | 16.1분 | 기타 | 음악 | 설명 | 65/69 | #185 |
| V203 | [Cheema Y Best Songs Playlist ∣ Punjabi Hits 2026 ∣ Jukebox …](https://www.youtube.com/watch?v=LFpVqIlmn00) | Radio Level L… | 37,900 | 3,475,020 | 30,207.7 | 91.7 | 115.0일 | 27.9분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,003/1,032 | #485 |
| V204 | ["Comfort song's - All in one playlist"😭✨🌷//part-4//edit by …](https://www.youtube.com/watch?v=617yn663oeA) | Anushri | 7,070 | 2,237,283 | 30,165.4 | 316.4 | 74.2일 | 7.6분 | 기타 | 플레이리스트·모음 | 설명 | 293/298 | #191 |
| V205 | [SONGS THAT’LL MAKE YOU DANCE AT 3AM ✨🔥 FT. DESI SONGS ❤️‍🔥💋…](https://www.youtube.com/watch?v=oIXkjb_FPC4) | Dramanique⋆.𐙚… | 31,800 | 4,802,213 | 29,849.0 | 151.0 | 160.9일 | 29.3분 | 기타 | 음악 | 설명 | 746/747 | #351 |
| V206 | [POV: You Own The Dance Floor💃🏻🪩✨ ∣∣Song Playlist+ Timestamp…](https://www.youtube.com/watch?v=HRGB0HnXdOs) | Author_Shreyuu | 6,200 | 4,446,380 | 29,614.0 | 717.2 | 150.1일 | 8분 | 기타 | 플레이리스트·모음 | 설명 | 617/619 | #52 |
| V207 | [조선힙합 '그냥 해' Official MV](https://www.youtube.com/watch?v=5hL7uPsISY0) | 조선힙합 | 257,000 | 3,759,742 | 29,385.1 | 14.6 | 127.9일 | 4분 | 11. 힙합·R&B·EDM | 한 곡 | 설명 | 1,950/1,961 |  |
| V208 | [Achhi lagti ho (slowed + reverb ) lofi varsion 🎧](https://www.youtube.com/watch?v=AMg46cfQH8A) | lofi song 45 | 1,540 | 2,001,041 | 29,073.6 | 1,299.4 | 68.8일 | 5.1분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 182/183 | #21 |
| V209 | [Mere Mehboob Qayamat Hogi ✨ ∣ Slowed Reverb + LoFi ∣ Sad Hi…](https://www.youtube.com/watch?v=AHo0xW8RYTQ) | Abidpro | 46,100 | 4,481,863 | 28,970.9 | 97.2 | 154.7일 | 9.4분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 350/350 | #470 |
| V210 | [Emraan hashmi playlist #emraanhashmi](https://www.youtube.com/watch?v=zZzA1Hp30uE) | july_luna | 4,540 | 1,783,677 | 28,928.1 | 392.9 | 61.7일 | 7.2분 | 기타 | 플레이리스트·모음 | 없음 | 22/25 | #143 |
| V211 | [MUSIK SANTAI VIRAL 2026 🎧 Lagu Pop Indonesia Akustik Terbai…](https://www.youtube.com/watch?v=bZEwYquV6Kg) | Akustik Cantik | 10,500 | 2,771,921 | 28,799.5 | 264.0 | 96.2일 | 78.5분 | 기타 | 정보·해설 | 설명 | 182/197 | #237 |

### 1-3-1. 자료를 받지 않은 하루 조회수 상위 후보 (68개 중 하루 조회수 큰 30개 — 승인하면 이 묶음에 들어감)

| 제목 | 채널 | 구독자 | 조회수 | 하루 조회수 | 길이 | 업로드 | 주제 묶음 |
|---|---|---|---|---|---|---|---|
| [Every Diwali Ever Ft. @NOTYOURTYPE #BGMI](https://www.youtube.com/watch?v=CiMwEmCqpfc) | BATTLEGROUNDS… | 5,530,000 | 6,062,676 | 612,589.5 | 5.1분 | 2026-10-12 | 기타 |
| [Hey Dukh Bhanjan ∣ Powerful Hanuman Bhajan ∣ मन को शांति दे…](https://www.youtube.com/watch?v=V9jCPRF7_IE) | NMF BHAKTI | 109,000 | 140,595,046 | 433,264.3 | 5.7분 | 2025-12-01 | 기타 |
| [I Went On 100 Dates In 24 Hours! (KPop Demon Hunters)](https://www.youtube.com/watch?v=fYVC8_0v7x0) | Topper Guild | 95,300,000 | 26,795,825 | 279,611.0 | 34.1분 | 2026-07-18 | 10. 팝송·K팝·J팝 |
| [[우리들의 발라드] 김소연🎵사랑 그 쓸쓸함에 대하여_양희은｜261005 1회](https://www.youtube.com/watch?v=C2AhBIE9_f8) | 스브스 예능맛집 | 2,770,000 | 3,741,485 | 224,138.6 | 5.9분 | 2026-10-05 | 9. 가요·발라드·트로트 |
| [우발라 최초 만점 득표?! 모두의 마음을 움직인 15세 소녀의 파워보컬🎤🫢 #우리들의발라드](https://www.youtube.com/watch?v=PWK1Y2hExVI) | 스브스 예능맛집 | 2,770,000 | 1,793,849 | 200,260.8 | 41.3분 | 2026-10-13 | 9. 가요·발라드·트로트 |
| [[우리들의 발라드] 박예승🎵나를 외치다_마야｜261012 2회](https://www.youtube.com/watch?v=YBzP2x3wM78) | 스브스 예능맛집 | 2,770,000 | 1,886,668 | 194,510.8 | 4.3분 | 2026-10-12 | 9. 가요·발라드·트로트 |
| [The most INSANE Street Performance you will ever see!! (wit…](https://www.youtube.com/watch?v=OhbbPxCtyxc) | Julien Cohen | 8,110,000 | 8,758,474 | 182,615.7 | 19분 | 2026-09-04 | 기타 |
| [KAYBEDEN TAKIMI DELİRTEN EKİP! ∣ GTA5: PLAYLIST ∣](https://www.youtube.com/watch?v=D_DQEUGdtNY) | Elraenn | 3,900,000 | 2,114,407 | 144,224.8 | 163.9분 | 2026-10-07 | 기타 |
| [ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ…](https://www.youtube.com/watch?v=l-vSSYEuO88) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 127,000 | 9,736,735 | 136,578.1 | 145.1분 | 2026-08-12 | 6. 피아노·클래식·연주곡 |
| [KPop Demon Hunters Go On 100 Dates!](https://www.youtube.com/watch?v=aJEVpCn_imY) | Topper Guild | 95,300,000 | 21,773,667 | 131,385.5 | 24.4분 | 2026-05-09 | 10. 팝송·K팝·J팝 |
| [I Faked My Death To Hide From KPop Demon Hunters!](https://www.youtube.com/watch?v=dubaKZmtnlE) | Topper Guild | 95,300,000 | 13,952,005 | 127,029.7 | 32분 | 2026-07-04 | 10. 팝송·K팝·J팝 |
| [I Married EVIL Rumi! (KPop Demon Hunters)](https://www.youtube.com/watch?v=KIb2oE4Xtig) | Topper Guild | 95,300,000 | 10,632,609 | 119,693.0 | 27.4분 | 2026-07-25 | 10. 팝송·K팝·J팝 |
| [Anirudh plays his favorite superstar Rajinikanth songs ∣ Ja…](https://www.youtube.com/watch?v=8w72RL2Rnps) | Sun TV | 33,000,000 | 1,002,417 | 102,060.2 | 7.3분 | 2026-10-12 | 기타 |
| ["노래 모르는 아가씨" 심수봉 저격에 펑펑 운 김다현, 하루 만에 "실언" 사과 [더펀치]](https://www.youtube.com/watch?v=DBlQIA3nJos) | MBN News | 2,590,000 | 3,023,403 | 97,983.4 | 13분 | 2026-09-21 | 기타 |
| [I Became a DEMON In Squid Game! (KPop Demon Hunters)](https://www.youtube.com/watch?v=TK-CHHQVH3o) | Topper Guild | 95,300,000 | 12,508,673 | 95,608.3 | 33.5분 | 2026-06-13 | 10. 팝송·K팝·J팝 |
| [This 2 year old SINGER shocked EVERYONE 🥹❤️](https://www.youtube.com/watch?v=W6exbBZNmPE) | Emilio Piano | 9,150,000 | 14,087,039 | 94,853.5 | 4.7분 | 2026-05-26 | 6. 피아노·클래식·연주곡 |
| [Last To Leave Elevator Wins $1,000! (KPop Demon Hunters)](https://www.youtube.com/watch?v=QsUJjZ09vE0) | Topper Guild | 95,300,000 | 15,033,119 | 93,470.9 | 22.4분 | 2026-05-14 | 10. 팝송·K팝·J팝 |
| [“선배님과 이 노래를 하다니🥹” 성발라가 극찬한 '최고의 보컬' 박재정 #헤어지자말해요 #아니면서 #성시경…](https://www.youtube.com/watch?v=GhV-gzhR9Hg) | KBS 한국방송 | 2,770,000 | 1,678,100 | 87,272.9 | 18.6분 | 2026-10-03 | 12. 커버·노래 부르기 |
| [[우리들의 발라드] 임바다🎵김성호의 회상_김성호｜261005 1회](https://www.youtube.com/watch?v=TCEYiDptimE) | 스브스 예능맛집 | 2,770,000 | 1,378,974 | 82,466.4 | 4.7분 | 2026-10-05 | 9. 가요·발라드·트로트 |
| [I Exposed the KPop Demon Hunters EVIL Babysitter!](https://www.youtube.com/watch?v=wdluy5UnnDU) | Topper Guild | 95,300,000 | 13,759,849 | 79,614.2 | 29분 | 2026-05-02 | 10. 팝송·K팝·J팝 |
| [Battle of the Idols! HUNTR/X VS Saja Boys 💥 KPop Demon Hunt…](https://www.youtube.com/watch?v=jGbHLocBmmY) | Netflix Family | 10,700,000 | 9,719,284 | 78,513.6 | 10.5분 | 2026-06-20 | 10. 팝송·K팝·J팝 |
| [HANUMAN CHALISA - Healing Version 🕉️ ∣ हनुमान चालीसा ∣ Calm…](https://www.youtube.com/watch?v=Ui0y6Wx9vBo) | Mantra Marg | 29,800 | 25,276,650 | 76,365.3 | 8분 | 2025-11-25 | 1. 수면·명상·힐링 |
| [🔥 Gareeb Piano Genius Ko Rich School Mein Scholarship Mili……](https://www.youtube.com/watch?v=TNsvoP-Dl9g) | Alex Explaine… | 57,800 | 1,030,457 | 75,318.5 | 64.2분 | 2026-10-08 | 6. 피아노·클래식·연주곡 |
| [피아노가 들리는 원희 노래실력 근황](https://www.youtube.com/watch?v=CmXSVMCrNUQ) | Sofa4844 | 263,000 | 1,017,571 | 73,068.3 | 8.3분 | 2026-10-08 | 6. 피아노·클래식·연주곡 |
| [기대 0% '한국 피아노맨'이 뉴욕의 낯선 공원에서 피아노를 쳤더니 생긴 일 (ft. 절대음감 피아노맨)](https://www.youtube.com/watch?v=EbQjKTOWVHg) | 콜드쉽 Coldsheep | 324,000 | 929,417 | 71,971.5 | 32.6분 | 2026-10-09 | 6. 피아노·클래식·연주곡 |
| [무슨 16살이 노래를 이렇게 잘해… 모두를 울린 레전드 참가자의 등장😭 #우리들의발라드](https://www.youtube.com/watch?v=McHPp3o-uFM) | 스브스 예능맛집 | 2,770,000 | 1,062,820 | 71,057.2 | 44.5분 | 2026-10-07 | 9. 가요·발라드·트로트 |
| [The Sound of Silence ∣ Like You've Never Felt Before ∣ Blue…](https://www.youtube.com/watch?v=cmRcndB-xE8) | PulsedBlues | 18,700 | 6,535,810 | 69,294.6 | 5.2분 | 2026-07-20 | 6. 피아노·클래식·연주곡 |
| [人魚VS Kpopスター! 🧜‍♀️✨ Kpopから人魚メイクオーバーへ 💄🌊](https://www.youtube.com/watch?v=0ikOKIelu1g) | VelvetPop Jap… | 258,000 | 5,738,108 | 69,238.8 | 16.1분 | 2026-07-31 | 10. 팝송·K팝·J팝 |
| [썸데이 - 고백 I [해피투게더🍀혼자가 아니어서 좋아] ∣ KBS 260904 방송](https://www.youtube.com/watch?v=g2nVvWGDNrY) | KBS 해피투게더 | 195,000 | 3,243,662 | 67,872.3 | 4.8분 | 2026-09-04 | 11. 힙합·R&B·EDM |
| [Bukzin Keyz, Benzoo, Tango Supreme - Mopepe (Visualizer)](https://www.youtube.com/watch?v=zZBtkOCPQ0o) | BukzinKeysVEVO | 24,600 | 15,904,654 | 65,072.3 | 4.5분 | 2026-02-19 | 6. 피아노·클래식·연주곡 |

### 1-3-2. 이 묶음의 시청자 니즈 (시청자 댓글 1,088,649개 — 채널 주인 댓글·도배 3,989개 뺌, 8번과 같은 규칙)

| 갈래 | 댓글 | 비율 | 좋아요 합 |
|---|---|---|---|
| 좋은 점 — 영상 (도움·설명·정리·공감) | 800 | 0.1% | 24,151 |
| 감사·응원 (일반) | 2,675 | 0.2% | 85,693 |
| 더 알고 싶은 것 (질문·요청) | 824 | 0.1% | 23,563 |
| 아쉬운 점 — 영상 (제목·광고·길이·정보 오류·목소리) | 630 | 0.1% | 20,633 |
| 반박·불만 — 의견 다름 (내용) | 457 | 0% | 12,708 |
| 정치·사회 (영상과 무관한 의견) | 185 | 0% | 1,525 |
| 경험 공유 (내 이야기) | 3,047 | 0.3% | 75,431 |
| 구독·다음 기대 | 311 | 0% | 4,852 |
| **어느 갈래에도 안 듦** | 1,080,276 | 99% | 8,534,415 |

요청 — 다뤄 주세요·알려 주세요·궁금해요 (652개 중 좋아요 순 15개, 영상마다 2개까지):

- 👍9,594 [V15] “조회수 궁금해서 온 사람 손”
- 👍6,477 [V196] “대체 뭔노래가 나올까 궁금해서 들어왔습니다”
- 👍1,112 [V15] “아니 궁금해서 멜론 드가보니 진짜 빵빵 감상비율 20대가 젤 높은거 개웃기네 ㅋㅋㅋㅋ 5060보다 2030이 비율 더 높은거 실화냐 ㅋㅋㅋ”
- 👍61 [V152] “이건 무조건 음원 만들어 주세요!”
- 👍61 [V207] “정말 와… 소리만 나와서 댓글 남깁니다… 영상을 보면서 아직 저는 한참 부족하다는 걸 다시 느꼈네요… 정말! 많이 배우고 갑니다! 앞으로도 좋은 작품 많이 만들어 주세요!”
- 👍39 [V170] “처음 듣는 곡인데... 마음이 너무 아려서 끝까지 듣기가.. 눈물이 아리네요❤❤ 명곡 많이 많이 올려 주세요^^”
- 👍35 [V88] “스테이는 아니지만.. 좋은의미로 발라드부르시는 목소리가 의외네요~ 이런 음색을 내실수 있구나 싶어서.. 담담히 고백하는듯 부르시는게 좋았고 다른 발라드는 어떨지 궁금하네요~”
- 👍28 [V92] “번역기를 사용해서 문장이 조금 어색할 수 있는 점 양해 부탁드립니다. 우크라이나에서 인사드립니다! 🇺🇦 학창 시절 BIGBANG 노래를 정말 많이 들었던 팬으로서 이 버전은 정말 감동적이네요... 특유의 레트로 감성이 노래와 너무 잘 어울리고, 진짜 완벽한 곡이에요! 요즘 K-POP도 좋지만 역시 빅뱅 노래만의 감성은 대체 불가인 것 같아요. 방금 이 영상”
- 👍20 [V74] “도경수 재발 음방좀해줘 부탁해요👏👏👏👍👍👍👍🎉🎉❤️❤️💓”
- 👍18 [V107] “고막할배될때까지 계속해주세요 가요무대처럼 성시경오빠 오래오래방송해주세요~❤😊”
- 👍16 [V43] “가사에 귀 기울이다가 너무 좋아서 지하철 개찰구를 나오지 못하고 계속 서성이면서 들었어요. 감동을 너머 가슴을 후벼파네요. 우즈님 잘한다 잘한다 하니 너무 잘하시네요. 그리고 이승철선배님과 목소리 합이 예술입니다. 두 분 자주 같이 이런 프로젝트 부탁드려요🙏 마음이 너무 좋다🫶”
- 👍15 [V74] “도경수씨 커버앨범, 재즈앨범, 팝앨범 부탁해요”
- 👍10 [V107] “시경이횽 버전 세로캠 풀버젼 부탁드려요 섹황님의 세로캠🎉🎉🎉🎉🎉🎉”
- 👍9 [V84] “아기 유준이랑 더 많은 콘텐츠 만들어주세요”
- 👍9 [V102] “JYPE PLEASE put it on Spotify! PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE JYPE 스포티파이에 올려주세요! If you don't, Stays will put it up again and then everyone will be in trouble, lets avo”

물음표 질문 (반문이 섞임 — 좋아요 순 10개):

- 👍55 [V15] “나 50대 아줌마에요 리센느 그냥 좋은데 이걸 어쩌요 더더더 좋아지네요 너무 잘하구 이뿌구 귀엽구 트로트매들리 2. 언제 나오나요?!!!”
- 👍22 [V15] “리센느 제나 추석선물 대박이네요. 어렸을때 받았던 종합선물세트 같네요. 정겹고 구수하고 맛있고 정이 있고 감동이 있네요. 가족이 생각나고 계속 계속 들어요.빵빵. 트롯은 언제 이렇게 배웠나요? 트롯천재! 재능이 이렇게 많은가요~~🎉🎉”
- 👍7 [V13] “댓글로 마녀사냥 하지 마세요 이해못한다해서 틀린게 아니에요 맘대로 추측해서 결국 불에 태워죽인 여성 예술가가 얼마나 많았나요? 중세시대도 아니고 댓글이 너무 기괴하고 음침합니다”
- 👍7 [V107] “성시경이계속하면안되나요? 연장 재연장 재재연장”
- 👍6 [V102] “누군가를 너무나 사랑하지만 직접 말할 수 없을 때 어떻게 해야 할까요?이 노래는 완벽하게 나왔어요. ❤”
- 👍3 [V102] “🇰🇷음, 어떻게 말해야 할까요? 여러분은 한 시대를 대표하는 최고의 그룹이 될 거예요. 정말 믿기지 않을 정도예요. 여러분 모두 정말 땀과 노력을 쏟아부었으니까요. 😍 솔직히 여러분이 군 복무를 하러 가게 되면 제가 어떻게 견딜 수 있을지 모르겠어요. 🥺 정말 많이 사랑해요. 제 가장 큰 꿈은 여러분의 콘서트에 가는 건데, 티켓을 사거나 한국으로 갈 형편이”
- 👍3 [V207] “이노래 컬러링은 안되나요?”
- 👍2 [V88] “🇰🇷음, 어떻게 말해야 할까요? 여러분은 한 시대를 대표하는 최고의 그룹이 될 거예요. 정말 믿기지 않을 정도예요. 여러분 모두 정말 땀과 노력을 쏟아부었으니까요. 😍 솔직히 여러분이 군 복무를 하러 가게 되면 제가 어떻게 견딜 수 있을지 모르겠어요. 🥺 정말 많이 사랑해요. 제 가장 큰 꿈은 여러분의 콘서트에 가는 건데, 티켓을 사거나 한국으로 갈 형편이”
- 👍2 [V107] “근데 성시경 키가 몇 인가요? 이재훈도 호빗으로 만들더니 이승철도 호빗으로 만들어 버리네”
- 👍2 [V112] “두번째 곡인 Drifiting through autumn은 언제 발매되나요? 너무 제 취향이에요! 애플뮤직에 없어서요.”

## 2. 주제 — 주제 묶음별 성공 비율 (비교 집단)

주제 묶음 = `tag_rules.toml` TAG_THEMES (제목에서 맞는 글자가 가장 긴 묶음, 없으면 태그). 비교 집단 성공 비율 20% 과 견주어 본다. 영상 15개 미만은 '표본 적음'.

| 주제 묶음 | 영상 | 성공 | 성공 비율 | 배수 중앙값 | 조회수 중앙값 | 성공 사례 # |
|---|---|---|---|---|---|---|
| 기타 | 1327 | 467 | 35% | 1.4 | 6,767 | 1, 3, 4, 5, 9, 11, 14, 15, 16, 17, 18, 23, 24, 25, 27, 28, 29, 30, 34, 36, 37, 39, 41, 42, 43, 47, 50, 51, 52, 57, 58, 61, 67, 68, 69, 75, 76, 78, 79, 80, 81, 83, 85, 87, 88, 89, 91, 92, 94, 97, 101, 102, 103, 106, 108, 111, 112, 114, 115, 116, 120, 122, 123, 124, 126, 128, 129, 130, 131, 133, 134, 136, 137, 138, 140, 142, 143, 155, 156, 158, 159, 161, 162, 163, 167, 169, 170, 171, 173, 177, 181, 183, 184, 185, 186, 187, 189, 191, 192, 193, 194, 195, 198, 199, 204, 208, 210, 211, 215, 220, 225, 228, 229, 236, 237, 238, 240, 242, 244, 245, 248, 250, 259, 262, 263, 267, 275, 278, 279, 287, 288, 294, 297, 306, 307, 312, 320, 329, 333, 334, 335, 336, 347, 351, 356, 359, 361, 367, 374, 381, 382, 387, 391, 402, 405, 412, 416, 433, 446, 449, 450, 454, 458, 471, 478, 480, 489, 491, 503, 504, 505, 506, 514, 528, 529, 546, 549, 556, 559, 566, 572, 586, 598, 608, 620, 624, 635, 649, 654, 659, 666, 668, 688, 713, 729, 730, 742, 743, 748, 754, 772, 779, 781, 785, 793, 796, 798, 808, 820, 830, 844, 851, 855, 856, 894, 901, 905, 909, 925, 928, 942, 947, 956, 960, 965, 976, 991, 997, 998, 1000, 1001, 1005, 1011, 1012, 1037, 1044, 1052, 1056, 1062, 1072 |
| 13. OST·사운드트랙 | 56 | 19 | 34% | 1.2 | 5,890.5 | 176, 234, 268, 281, 363, 435, 501, 681, 845, 1006 |
| 10. 팝송·K팝·J팝 | 122 | 33 | 27% | 1.2 | 6,997.5 | 19, 20, 31, 118, 146, 150, 157, 168, 254, 280, 286, 296, 348, 349, 407, 460, 553, 583, 639, 658, 669, 690, 692, 693, 710, 719, 787, 913, 974, 988, 1022, 1025, 1060, 1087 |
| 5. 운동·드라이브·신나는 | 104 | 27 | 26% | 1.2 | 6,772.0 | 104, 121, 125, 265, 394, 474, 548, 605, 610, 633, 677, 752, 771, 784, 826, 839, 1034, 1071 |
| 11. 힙합·R&B·EDM | 167 | 38 | 23% | 0.7 | 7,280 | 2, 132, 235, 246, 327, 640, 712, 717, 765, 800, 859, 871, 891, 897, 927, 995, 1042 |
| 8. 로파이·시티팝·칠 | 485 | 107 | 22% | 0.7 | 4,588 | 6, 7, 8, 13, 21, 26, 35, 38, 44, 45, 46, 49, 53, 59, 60, 64, 70, 72, 74, 77, 93, 95, 99, 100, 105, 107, 109, 113, 117, 119, 144, 151, 153, 154, 160, 179, 190, 205, 213, 219, 226, 227, 247, 252, 257, 261, 274, 303, 304, 313, 326, 340, 350, 373, 375, 383, 385, 396, 404, 410, 411, 451, 466, 469, 470, 484, 485, 487, 492, 509, 510, 513, 515, 521, 524, 530, 532, 545, 569, 588, 646, 652, 873, 900, 940, 978, 1046, 1047 |
| 12. 커버·노래 부르기 | 169 | 37 | 22% | 0.5 | 5,235 | 56, 63, 145, 200, 292, 323, 400, 431, 436, 437, 440, 476, 482, 623, 625, 638, 685, 718, 726, 763, 794, 803, 827, 828, 831, 837, 842, 854, 944, 983, 985, 1009, 1036 |
| 7. 재즈·보사노바 | 115 | 22 | 19% | 0.4 | 7,087 | 283, 368, 377, 415, 465, 535, 537, 544, 622, 723, 846, 847, 852, 860, 887, 910, 955, 1026, 1065 |
| 6. 피아노·클래식·연주곡 | 853 | 138 | 16% | 0.5 | 3,031 | 22, 96, 110, 165, 174, 175, 212, 221, 284, 295, 308, 314, 322, 328, 331, 339, 344, 352, 353, 357, 360, 365, 369, 384, 390, 399, 414, 419, 422, 424, 425, 426, 427, 428, 432, 434, 442, 448, 452, 467, 477, 479, 488, 490, 494, 497, 512, 517, 518, 531, 538, 539, 540, 547, 560, 565, 570, 574, 576, 577, 581, 584, 587, 589, 593, 597, 599, 602, 604, 609, 612, 613, 615, 621, 628, 629, 631, 632, 634, 645, 657, 665, 674, 675, 686, 696, 703, 705, 708, 709, 711, 715, 716, 720, 721, 724, 739, 740, 747, 751, 758, 759, 762, 766, 768, 773, 774, 776, 782, 783, 789, 790, 795, 799, 804, 806, 807, 809, 810, 811, 812, 813, 814, 819, 829, 832, 849, 850, 858, 865, 870, 875, 878, 882, 883, 884, 892, 893, 895, 899, 906, 907, 908, 911, 926, 938, 958, 975, 977, 979, 980, 984, 990, 993, 999, 1023, 1029, 1043, 1045, 1051, 1066, 1067, 1079, 1080, 1082, 1083, 1085 |
| 2. 자연 소리·백색소음 | 139 | 22 | 16% | 0.7 | 4,240 | 84, 90, 166, 251, 270, 282, 311, 321, 332, 345, 355, 393, 418, 441, 443, 642, 698, 714, 733, 750, 917, 968, 981, 987, 1086 |
| 4. 카페·매장·라운지 | 213 | 27 | 13% | 0.5 | 2,830 | 10, 40, 65, 86, 180, 197, 201, 206, 207, 214, 222, 224, 253, 269, 305, 346, 358, 379, 392, 398, 447, 461, 495, 508, 526, 552, 557, 567, 568, 571, 614, 630, 636, 647, 660, 683, 728, 745, 757, 764, 778, 838, 841, 867, 880, 889, 930, 943, 963, 966, 971, 989, 992, 1013, 1018, 1059, 1064 |
| 14. AI 음악 | 73 | 9 | 12% | 0.2 | 1,994 | 472, 551, 561, 594, 689, 857, 888, 1019 |
| 9. 가요·발라드·트로트 | 364 | 42 | 12% | 0.4 | 1,659.0 | 66, 152, 182, 218, 230, 231, 277, 285, 291, 300, 302, 316, 341, 342, 354, 372, 445, 463, 468, 502, 534, 555, 573, 582, 616, 619, 627, 637, 653, 656, 661, 662, 664, 670, 678, 687, 691, 697, 699, 702, 734, 741, 769, 777, 786, 791, 797, 805, 821, 840, 843, 863, 903, 914, 918, 919, 921, 923, 924, 932, 937, 939, 950, 962, 964, 973, 994, 996, 1002, 1003, 1004, 1016, 1017, 1020, 1024, 1039, 1048, 1049, 1053, 1058, 1081, 1084 |
| 3. 공부·집중·작업 | 419 | 44 | 10% | 0.4 | 2,430 | 12, 73, 127, 135, 139, 147, 164, 203, 217, 232, 256, 258, 260, 266, 271, 273, 289, 290, 315, 317, 330, 371, 388, 395, 408, 420, 429, 439, 444, 481, 500, 511, 522, 523, 527, 542, 543, 550, 554, 562, 575, 578, 579, 591, 596, 600, 606, 611, 643, 644, 651, 672, 676, 682, 700, 707, 725, 727, 756, 770, 775, 802, 822, 823, 824, 862, 877, 916, 929, 933, 949, 952, 961, 967, 1007, 1021, 1032, 1038, 1041, 1054, 1057, 1063, 1068, 1075, 1088 |
| 1. 수면·명상·힐링 | 1115 | 116 | 10% | 0.5 | 1,521 | 32, 33, 48, 54, 55, 62, 71, 82, 98, 141, 148, 149, 172, 178, 188, 196, 202, 209, 216, 223, 233, 239, 241, 243, 249, 255, 264, 272, 276, 293, 298, 299, 301, 309, 310, 318, 319, 324, 325, 337, 338, 343, 362, 364, 366, 370, 376, 378, 380, 386, 389, 397, 401, 403, 406, 409, 413, 421, 423, 430, 438, 453, 455, 456, 457, 459, 462, 464, 473, 475, 483, 486, 493, 496, 498, 499, 507, 516, 519, 520, 533, 536, 541, 558, 563, 564, 580, 585, 590, 592, 595, 601, 603, 607, 617, 618, 626, 641, 648, 650, 655, 663, 667, 671, 673, 679, 680, 684, 694, 695, 701, 704, 706, 732, 736, 737, 738, 744, 746, 753, 760, 761, 767, 780, 788, 792, 801, 815, 816, 817, 818, 825, 833, 834, 835, 848, 853, 861, 864, 866, 868, 872, 874, 876, 879, 881, 885, 886, 890, 896, 898, 904, 912, 915, 920, 922, 931, 934, 935, 941, 951, 954, 957, 959, 969, 970, 972, 982, 986, 1008, 1010, 1014, 1015, 1027, 1028, 1030, 1031, 1033, 1035, 1040, 1050, 1055, 1061, 1069, 1070, 1073, 1076, 1077, 1078 |
| 15. CCM·찬양·국악·동요 | 119 | 11 | 9.2% | 0.5 | 3,172 | 417, 525, 722, 731, 735, 749, 755, 836, 869, 902, 936, 945, 946, 948, 953, 1074 |

## 2-2. 형식(포맷) — 어떤 모양의 영상인가 (제목·채널 이름·태그 낱말로 나눔)

형식 규칙 = `analysis_rules.toml` [format] (위에서부터 먼저 맞는 것 하나, 낱말 규칙이라 거칠다). **성공 사례 몫**은 성공 사례 중 그 형식 비율, **시장 지수**는 3번과 같은 수요 몫 ÷ 공급 몫 (1보다 크면 영상 하나가 평균보다 많이 봄), **같은 채널**은 1-2번의 잘된 영상 중 비율 vs 평소 영상 중 비율. 원인이 아니라 묶음이다.

| 형식 | 비교 집단 영상 (성공 비율) | 배수 중앙값 | 성공 사례 몫 (#) | 시장 영상 · 지수 | 같은 채널 잘된 vs 평소 |
|---|---|---|---|---|---|
| AI 음악 | 171 (8.8%) | 0.3 | 2.9% (53, 110, 152, 277, 298, 302, 406, 472, 551, 561, 594, 625 …) | 47 · 0.1 | 2.6% vs 2.6% |
| 커버·직접 부른 노래 | 301 (21%) | 0.5 | 5.8% (36, 56, 145, 197, 200, 212, 218, 254, 274, 286, 292, 295 …) | 44 · 0.8 | 5.4% vs 5.2% |
| 연주 (직접 연주하는 영상) | 70 (24%) | 0.9 | 1.2% (365, 414, 512, 518, 618, 705, 708, 716, 740, 766, 838, 971 …) | 13 · 0.3 (표본 적음) | 1.0% vs 1.0% |
| 플레이리스트·모음 (여러 곡) | 1823 (27%) | 1.1 | 34% (3, 12, 14, 15, 16, 17, 18, 20, 27, 28, 29, 33 …) | 251 · 0.7 | 32% vs 30% |
| 자연 소리·백색소음 (음악 낱말 없는 제목) | 58 (16%) | 1.1 | 1.0% (321, 345, 418, 443, 459, 642, 733, 780, 959, 968, 981) | 2 · 0.1 (표본 적음) | 1.2% vs 1.2% |
| 긴 한 곡·반복 (N시간) | 155 (16%) | 0.4 | 3.2% (80, 233, 239, 255, 266, 303, 324, 340, 360, 390, 393, 402 …) | 15 · 0.9 | 3.5% vs 2.9% |
| 한 곡 (뮤직비디오·음원·가사) | 243 (19%) | 0.6 | 3.5% (19, 31, 47, 66, 82, 99, 101, 103, 146, 150, 151, 179 …) | 45 · 6.4 | 3.7% vs 4.4% |
| 음악 (그 밖 모양 — 한 편짜리 BGM 등) | 2759 (15%) | 0.4 | 44% (1, 4, 5, 6, 7, 8, 9, 13, 21, 22, 23, 24 …) | 434 · 0.7 | 46% vs 47% |
| 정보·해설 (그 밖) | 260 (26%) | 1.0 | 4.0% (2, 10, 11, 34, 40, 42, 65, 67, 96, 124, 132, 171 …) | 30 · 1.3 | 4.8% vs 6.0% |

## 3. 수요와 공급 — 찾는 사람에 비해 영상이 적은 곳

### 3-1. 주제 묶음별 (최근 90일 영상 881개 — 채널 크기 상관없음)

수요 몫 = 그 묶음 영상들의 하루 조회수 합 ÷ 전체, 공급 몫 = 영상 수 ÷ 전체. **지수 = 수요 몫 ÷ 공급 몫** — 1 보다 크면 영상 하나가 평균보다 많이 보임(공급이 모자라 보임), 작으면 영상이 넘침. 작은 채널 성공 비율 = 2번 표. 시청자 질문 = 사례 댓글 중 그 묶음 낱말이 든 질문·요청.

| 주제 묶음 | 영상(공급) | 채널 | 수요 몫 | 공급 몫 | 지수 | 영상당 하루 조회수 중앙값 | 작은 채널 성공 비율 | 시청자 질문 |
|---|---|---|---|---|---|---|---|---|
| 기타 | 174 | 129 | 52% | 20% | **2.6** | 9,099.5 | 35% | 0 |
| 8. 로파이·시티팝·칠 | 48 | 44 | 10% | 5.4% | **1.9** | 25,078.5 | 22% | 2 |
| 9. 가요·발라드·트로트 | 61 | 44 | 7.6% | 6.9% | **1.1** | 4,118.4 | 12% | 113 |
| 10. 팝송·K팝·J팝 | 40 | 27 | 5.0% | 4.5% | **1.1** | 3,501.1 | 27% | 21 |
| 12. 커버·노래 부르기 | 24 | 17 | 1.7% | 2.7% | **0.6** | 5,409.9 | 22% | 29 |
| 4. 카페·매장·라운지 | 51 | 35 | 2.8% | 5.8% | **0.5** | 3,746.4 | 13% | 12 |
| 6. 피아노·클래식·연주곡 | 172 | 119 | 9.1% | 20% | **0.5** | 5,032.1 | 16% | 30 |
| 3. 공부·집중·작업 | 77 | 66 | 4.1% | 8.7% | **0.5** | 1,035.2 | 10% | 27 |
| 1. 수면·명상·힐링 | 177 | 131 | 4.5% | 20% | **0.2** | 261.7 | 10% | 21 |
| 11. 힙합·R&B·EDM (표본 적음) | 9 | 9 | 0.7% | 1.0% | **0.7** | 1,759.8 | 23% | 3 |
| 7. 재즈·보사노바 (표본 적음) | 10 | 8 | 0.6% | 1.1% | **0.5** | 7,595.7 | 19% | 9 |
| 2. 자연 소리·백색소음 (표본 적음) | 10 | 10 | 0.5% | 1.1% | **0.4** | 4,790.7 | 16% | 2 |
| 13. OST·사운드트랙 (표본 적음) | 8 | 8 | 0.3% | 0.9% | **0.4** | 5,935.5 | 34% | 2 |
| 5. 운동·드라이브·신나는 (표본 적음) | 11 | 10 | 0.3% | 1.2% | **0.2** | 1,472.5 | 26% | 10 |
| 15. CCM·찬양·국악·동요 (표본 적음) | 7 | 7 | 0.2% | 0.8% | **0.2** | 3,889.7 | 9.2% | 36 |
| 14. AI 음악 (표본 적음) | 2 | 2 | 0% | 0.2% | **0.1** | 3,762.9 | 12% | 12 |

### 3-2. 검색어별 (탐색·검색 캐시 — 검색어마다 조회수 순 상위 결과)

결과 수 = YouTube 가 알려 준 그 기간 영상 수 추정(공급). 영상당 하루 조회수 = 상위 결과 하루 조회수 합 ÷ 결과 수 (클수록 영상에 비해 찾는 사람이 많음). 큰 채널 비율 = 상위 결과 중 구독자 5만 넘는 채널 (클수록 들어가기 어려움). **작은 채널이 뚫은 비율** = 상위 결과 중 작은 채널(5만 이하)의 성공 영상(×3·1만) 비율 — 클수록 새 채널도 상위에 들 수 있음. 지금 검색어(keywords.txt)가 먼저, 예전 검색어는 '(예전)'.

| 검색어 | 기간(일) | 본 영상 | 결과 수(공급) | 최근 30일 | 조회수 중앙값 | 하루 조회수 중앙값 | 영상당 하루 조회수 | 큰 채널 비율 | 작은 채널이 뚫은 비율 |
|---|---|---|---|---|---|---|---|---|---|
| playlist | 182 | 100 | 2,000,000 | 3 | 2,493,502.5 | 26,741.5 | 1.8 | 11% | 89% (78개) |
| 플리 | 182 | 100 | 1,253,238 | 0 | 550,153 | 4,137.8 | 0.5 | 12% | 88% (80개) |
| study music | 182 | 100 | 2,000,000 | 2 | 2,109,372.0 | 15,859.6 | 1.3 | 15% | 85% (66개) |
| stress relief music | 182 | 100 | 1,247,946 | 3 | 1,263,656.5 | 10,495.4 | 1.3 | 17% | 83% (68개) |
| deep sleep music | 182 | 100 | 1,373,573 | 3 | 1,066,449.0 | 9,965.5 | 1.0 | 19% | 81% (60개) |
| ambient music | 182 | 100 | 1,973,196 | 4 | 905,017 | 6,267.0 | 0.4 | 20% | 80% (62개) |
| lofi | 182 | 100 | 2,000,000 | 1 | 2,128,712 | 24,314.4 | 1.6 | 21% | 79% (67개) |
| peaceful music | 182 | 100 | 1,988,001 | 2 | 1,595,763 | 10,907.2 | 0.8 | 24% | 76% (62개) |
| calm music | 182 | 100 | 2,000,000 | 2 | 1,763,734.5 | 13,629.0 | 0.8 | 24% | 76% (56개) |
| focus music | 182 | 100 | 2,000,000 | 2 | 1,158,090.0 | 9,548.0 | 0.7 | 24% | 76% (56개) |
| BGM | 182 | 100 | 2,000,000 | 1 | 549,637.0 | 4,449.8 | 0.8 | 26% | 74% (67개) |
| MeditationMusic | 182 | 100 | 877,295 | 3 | 349,334 | 2,195.9 | 0.4 | 22% | 74% (57개) |
| soothing music | 182 | 100 | 1,548,676 | 2 | 1,202,718.0 | 10,666.0 | 1.1 | 26% | 74% (59개) |
| yoga music | 182 | 100 | 2,000,000 | 0 | 1,746,963 | 12,303.2 | 0.5 | 28% | 72% (34개) |
| calming music | 182 | 100 | 2,000,000 | 2 | 1,343,429.0 | 11,898.0 | 0.7 | 29% | 71% (54개) |
| 플레이리스트 | 182 | 100 | 1,520,777 | 2 | 573,591 | 4,781.1 | 0.5 | 30% | 70% (57개) |
| Sleep Music | 182 | 100 | 2,000,000 | 2 | 1,536,124 | 15,372.5 | 0.8 | 30% | 70% (44개) |
| 힐링음악 | 182 | 100 | 387,758 | 1 | 301,806 | 1,918.1 | 1.0 | 24% | 70% (66개) |
| 감성발라드 | 182 | 100 | 254,101 | 1 | 421,530 | 4,116.0 | 2.2 | 34% | 66% (63개) |
| cafe music | 182 | 100 | 2,000,000 | 4 | 1,125,330 | 11,492.8 | 0.7 | 35% | 65% (50개) |
| chill music | 182 | 100 | 2,000,000 | 2 | 2,466,691 | 24,624.8 | 3.0 | 35% | 65% (46개) |
| 감성음악 | 182 | 100 | 1,090,278 | 4 | 348,129.5 | 2,940.2 | 0.4 | 26% | 63% (59개) |
| relaxing music | 365 | 100 | 1,722,502 | 0 | 3,794,957.0 | 18,580.5 | 1.2 | 38% | 62% (45개) |
| work music | 182 | 100 | 2,000,000 | 4 | 286,555 | 3,050.7 | 0.3 | 15% | 61% (48개) |
| relaxation music | 182 | 100 | 1,658,036 | 1 | 1,106,041.0 | 9,772.6 | 0.8 | 40% | 60% (48개) |
| healingmusic | 182 | 100 | 516,429 | 6 | 49,092.0 | 583.3 | 0.2 | 8.8% | 59% (40개) |
| instrumental music | 182 | 100 | 2,000,000 | 2 | 896,802.5 | 8,271.6 | 0.5 | 43% | 57% (43개) |
| 카페음악 | 182 | 100 | 534,014 | 0 | 275,629 | 1,966.1 | 0.6 | 33% | 56% (53개) |
| relaxing piano | 182 | 100 | 1,363,317 | 8 | 466,125.5 | 4,732.7 | 0.5 | 45% | 54% (46개) |
| piano | 182 | 100 | 2,000,000 | 3 | 1,002,417 | 9,336.5 | 0.8 | 49% | 51% (35개) |
| RelaxingMusic | 182 | 100 | 1,218,528 | 5 | 818,863 | 8,601.4 | 0.8 | 49% | 51% (44개) |
| background music | 182 | 100 | 2,000,000 | 5 | 897,359.0 | 9,346.5 | 0.6 | 51% | 49% (39개) |
| piano music | 365 | 100 | 2,000,000 | 0 | 2,078,967 | 9,287.9 | 0.7 | 52% | 48% (30개) |
| pianomusic | 182 | 100 | 563,594 | 11 | 141,394 | 1,048.8 | 0.3 | 20% | 47% (39개) |
| 명상음악 | 182 | 100 | 542,059 | 2 | 127,668.5 | 971.2 | 0.3 | 17% | 45% (38개) |
| 발라드 | 182 | 100 | 572,147 | 9 | 799,399 | 6,215.7 | 2.8 | 56% | 44% (41개) |
| relaxing piano music | 182 | 100 | 2,000,000 | 12 | 491,497.0 | 6,723.1 | 0.4 | 56% | 44% (36개) |
| 음악 | 182 | 100 | 2,000,000 | 5 | 845,705.5 | 7,128.4 | 0.7 | 57% | 43% (36개) |
| 편안한음악 | 182 | 100 | 420,824 | 12 | 126,566 | 774.6 | 0.4 | 13% | 42% (41개) |
| 마음이편안해지는음악 | 182 | 100 | 152,118 | 4 | 107,737 | 947.2 | 1.2 | 20% | 40% (37개) |
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
| healing music playlist | 1.0 | healing music, healingmusic | 0 | 1.0 | 확인 전 |  |  |  |
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

### 3-4. 주제 묶음별 시청자 질문 (사례 댓글 — 좋아요 순)

- **9. 가요·발라드·트로트** (113개): 👍719 “젤루 잘생긴 성리 K트롯돌 실력자 올라운더 멀티 AI 성리 글로벌 세계로 가자 국민투표 연속 7주1위 성리 우승까지 밀어주시길 부탁드립니다 꾸~~벅 " 핑크 스타 다이아몬드" 성리 1대 전설이 되…” / 👍640 “조회수 궁금해서 계속와보는 사람 개츄 내가 살다살다 아이돌 트롯이 1500만 넘기는걸 보다니” / 👍35 “스테이는 아니지만.. 좋은의미로 발라드부르시는 목소리가 의외네요~ 이런 음색을 내실수 있구나 싶어서.. 담담히 고백하는듯 부르시는게 좋았고 다른 발라드는 어떨지 궁금하네요~”
- **15. CCM·찬양·국악·동요** (36개): 👍31 “모든 찬양에 은혜주신 주님께 감사드립니다 저녁에 찬양따라 부르며 울다가 웃다가 기도하며 찬양에 흠뻑 빠졌습니다 예전에 처음 교회다닐때 찬송가 하늘가는 밝은길이 그찬양만 들으면 얼마나 닭똥같던 눈물…” / 👍24 “이 찬양 큰위로가 됩니다 감사합니다, 혹시 찬양사역자분 누구신지. 알고싶네요,” / 👍16 “축하드립니다!! 계속 은혜로운 찬양 부탁합니다^*^”
- **6. 피아노·클래식·연주곡** (30개): 👍62 “최고에요! 제 브이로그 배경음악으로 클래식을 많이 쓰는데, 혹시 출처표시하고 bgm으로 쓸 수 있을까요? 안되더라두 괜찮으니 편하게 알려주세요! 좋은 음악 감사합니다! :)” / 👍10 “💖 따뜻한 분위기와 감성적인 피아노 연주가 어우러져서 듣는 내내 행복했습니다. 일상 속 작은 휴식이 필요할 때마다 다시 찾아 듣고 싶어요. 앞으로도 이런 힐링 음악 많이 올려주세요!” / 👍8 “이 곡을 이렇게 편곡할 수 있나요? 만드신 분의 내공이 느껴진다. 간주에 피아노와 기타의 콜라보, 대단하네요...좋은 곡 많이 부탁합니다. 😊”
- **12. 커버·노래 부르기** (29개): 👍10 “장윤정 꽃 불러줘(여러분 추천해주세요ㅠ)” / 👍7 “성리 우승 응원합니다. 궁금하다. 도대체 이것보다 어떻게 불러야 점수가 더 나올 라나 600점 만점에 550 도 넘지않는 점수를😊” / 👍6 “노래 너무 잘들었습니다! 혹시 물고기자리 누구 커버에요? 너무 선곡이 좋으셔서 궁금합니다”
- **3. 공부·집중·작업** (27개): 👍77 “할렐루야 주님께 영광돌립니다 . 호주에서 5년 살고 컴백한 시골사역 사모예요. 한국 정읍시 오주길 ~ 작은마을 개척교회사모입니다. 저희는 교회 사역에 필요한 야채 식료품 밭에서 직저자배해서 성도님…” / 👍9 “워낙 플리들이 다 좋아서 아무거나 틀어놔도 될 줄 알았는데, 확실히 독서할 땐 이거네요👍 덕분에 집에서도 책을 읽을 수 있게 됐어요🙂‍↕️독서용도 종종 만들어 주시면 정말 좋을 것 같아요..🙏” / 👍6 “코러스 집중 영상 올려주세요 ㅋㅋㅋ”
- **10. 팝송·K팝·J팝** (21개): 👍28 “번역기를 사용해서 문장이 조금 어색할 수 있는 점 양해 부탁드립니다. 우크라이나에서 인사드립니다! 🇺🇦 학창 시절 BIGBANG 노래를 정말 많이 들었던 팬으로서 이 버전은 정말 감동적이네요...…” / 👍8 “미나미 JPOP, 제나 트로트에 이어서 원이: 한글날 기념 판소리 메들리 (사랑가, 춘향가 포함 자작가로 거제가 부탁드립니다) 리브 메이: 크리스마스 기념 뮤지컬 메들리 (뮤지컬 제목: 리트와 메…” / 👍2 “제이팝 좋은거 찾고있는데 추천좀여”
- **1. 수면·명상·힐링** (21개): 👍20 “불면으로 힘들어하는 50대입니다. 수면제 10년째중이구요. 이 음악으로 마음의 평안을 얻습니다. 유투브에 저장해서 비행기에서도 무한반복이구요. 요즘 체력적으로 힘든치료 받고 온 날 해당음악 귀에 …” / 👍11 “평소에 드보르작의 곡을 좋아했지만 이곡은 정말 마음을 아름답고 즐겁게 하네 요. 아침에 우연히 들었는데 마음이 가볍고 편안하게 힐링 해주었습니다. 감사해요. 앞으로도 계속하여 또 좋은곡 부탁드립니…” / 👍9 “오늘도 청계천 걸어며 걸어온길 삶속에 명상하면서 음악 감상하고 갑니다 오늘도 좋은음악 올려주세요 셈님 감사합니다”
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
| vs 비교 | 75 (35%) | 5765 (20%) | +15%p | **눈에 띔** | 1.1% |
| 25자 미만 | 396 (32%) | 5444 (19%) | +13%p | **눈에 띔** | 8.2% |
| 빚투·신용·미수·레버리지·대출 | 2 (50%) | 5838 (20%) | +30%p | 표본 적음 | 0.1% |
| 손실 낱말(망하·날린·잃은·반토막) | 7 (0%) | 5833 (20%) | -20%p | 표본 적음 | 0% |
| 직접·해보니·N년 기록 | 3 (0%) | 5837 (20%) | -20%p | 표본 적음 | 0% |
| 금액(억·만원) | 1 (0%) | 5839 (20%) | -20%p | 표본 적음 | 0% |
| S&P500·ETF·지수·나스닥 | 1 (0%) | 5839 (20%) | -20%p | 표본 적음 | 0% |
| N가지 | 3 (33%) | 5837 (20%) | +14%p | 표본 적음 | 0% |
| 사연·오디오북·실화·고백 | 11 (9.1%) | 5829 (20%) | -11%p | 표본 적음 | 0% |
| 과정·벌어진 일·결말·결국 | 10 (10%) | 5830 (20%) | -10%p | 표본 적음 | 0% |
| 40자 이상 | 4826 (18%) | 1014 (28%) | -10%p |  | 82% |
| 노후·퇴직금·은퇴·50~70대 | 18 (28%) | 5822 (20%) | +8%p |  | 0.5% |
| 물음표 ? | 94 (27%) | 5746 (20%) | +7%p |  | 1.1% |
| 따옴표·괄호로 강조 | 1053 (25%) | 4787 (19%) | +6%p |  | 19% |
| 이유 | 12 (25%) | 5828 (20%) | +5%p | 표본 적음 | 0% |
| 구분 기호(ㅣ·｜·/)로 나눔 | 3523 (18%) | 2317 (23%) | -5%p |  | 59% |
| AI | 472 (22%) | 5368 (20%) | +2%p |  | 8.2% |
| 패턴형(공통점·특징·이유·N가지·착각·과정) | 19 (21%) | 5821 (20%) | +1%p |  | 0% |
| 느낌표 ! | 112 (19%) | 5728 (20%) | -1%p |  | 1.7% |
| 말줄임 …·... | 164 (21%) | 5676 (20%) | +1%p |  | 3.3% |
| 숫자가 들어감 | 1897 (20%) | 3943 (20%) | -0%p |  | 33% |

### 4-2. 제목 낱말 (비교 집단 제목에 자주 나온 낱말 — 조사를 거칠게 뗌)

| 낱말 | 있음 (성공 비율) | 없음 (성공 비율) | 차이 | 표시 |
|---|---|---|---|---|
| playlist | 220 (37%) | 5620 (19%) | +18%p | **눈에 띔** |
| Playlist | 453 (28%) | 5387 (19%) | +9%p |  |
| Love | 217 (24%) | 5623 (20%) | +4%p |  |
| Jazz | 204 (23%) | 5636 (20%) | +3%p |  |
| Song | 281 (21%) | 5559 (20%) | +2%p |  |
| Lofi | 279 (21%) | 5561 (20%) | +1%p |  |
| BGM | 235 (21%) | 5605 (20%) | +1%p |  |
| Songs | 308 (21%) | 5532 (20%) | +1%p |  |
| Slowed | 216 (21%) | 5624 (20%) | +1%p |  |
| Chill | 206 (20%) | 5634 (20%) | +0%p |  |
| 음악 | 245 (8.2%) | 5595 (20%) | -12%p | **눈에 띔** |
| Focus | 211 (8.1%) | 5629 (20%) | -12%p | **눈에 띔** |
| Healing | 210 (10%) | 5630 (20%) | -10%p | **눈에 띔** |
| Meditation | 184 (10%) | 5656 (20%) | -10%p |  |
| Deep | 413 (11%) | 5427 (20%) | -10%p |  |
| 마음 | 193 (10%) | 5647 (20%) | -10%p |  |
| Study | 220 (11%) | 5620 (20%) | -9%p |  |
| Music | 1081 (12%) | 4759 (22%) | -9%p |  |
| Mind | 177 (13%) | 5663 (20%) | -7%p |  |
| Peaceful | 195 (14%) | 5645 (20%) | -6%p |  |

### 4-3. 제목 길이

| 길이 | 영상 (성공 비율) |
|---|---|
| 0~24자 | 396 (32%) |
| 25~34자 | 385 (28%) |
| 35~44자 | 485 (19%) |
| 45자 이상 | 4574 (18%) |

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

성공 사례 #1081–#1088:

![성공 사례 썸네일 #1081-#1088](analysis_thumbs_55.jpg)

같은 채널 짝 — 줄마다 [성공 사례 #n · 같은 채널 평소 영상 #n-a · #n-b] (1 … #14-b):

![같은 채널 썸네일 짝](analysis_thumbs_pairs_01.jpg)

같은 채널 짝 — 줄마다 [성공 사례 #n · 같은 채널 평소 영상 #n-a · #n-b] (16 … #32-b):

![같은 채널 썸네일 짝](analysis_thumbs_pairs_02.jpg)

비교 — 자료를 받았지만 성공 기준 밖 (조회수 큰 순, 번호는 `analysis.json` 의 others 순서):

![비교 썸네일](analysis_thumbs_others.jpg)

## 6. 길이·내용 구성

### 6-1. 길이별 성공 비율 (비교 집단)

| 길이 | 영상 (성공 비율) | 성공 사례 |
|---|---|---|
| 4~8분 | 1562 (19%) | 264 |
| 8~15분 | 612 (24%) | 120 |
| 15~25분 | 628 (33%) | 125 |
| 25~40분 | 452 (24%) | 67 |
| 40분 이상 | 2586 (16%) | 512 |

### 6-2. 채널 크기별 성공 비율 (참고 — 구독자가 적을수록 배수가 커지기 쉬움)

| 구독자 | 영상 (성공 비율) |
|---|---|
| 0~999명 | 812 (12%) |
| 1,000~4,999명 | 1645 (26%) |
| 5,000~19,999명 | 2079 (19%) |
| 20,000~50,000명 | 1304 (19%) |

### 6-3. 성공 사례의 구성

- 길이 중앙값: 성공 사례 29.8분 · 비교 집단의 나머지 31.3분
- 타임라인(챕터) 있는 성공 사례: 28% (챕터 수 중앙값 12.0)
- 대본이 있는 성공 사례: 0개 — 말 속도 중앙값 – 음절/초, 첫 1분 음절 중앙값 – (대본이 없어 도입부·흐름은 아직 셀 수 없음)
- 도입부(첫 20초 첫 문장) 유형: 대본 없음 — 아직 셀 수 없음
- 사례마다의 챕터·도입부(첫 20초)·첫 1분·90초마다 흐름은 9번.

### 6-4. 참여율 (비교 집단, 중앙값)

| | 영상 | 조회수 1,000회당 좋아요 | 조회수 1,000회당 댓글 |
|---|---|---|---|
| 성공 | 1159 | 7.8 | 0.2 |
| 나머지 | 4681 | 10.9 | 0.8 |

## 7. 구독자 — 빨리 크는 작은 채널

YouTube API 는 영상별 구독 증가를 주지 않는다 → 채널 단위로 본다. 개설 24개월 안·구독자 1,000 이상 채널을 **월 구독자 증가(구독자 ÷ 개설 뒤 달 수)** 순으로. 최근 하루 증가 = 받을 때마다 남긴 구독자 기록 (3일 넘게 벌어져야 나옴). 주로 다룬 주제 = 우리가 본 그 채널 영상의 주제 묶음. **기관·브랜드?** = 채널 이름에 운용사 ETF 상표·증권·은행·공식·방송 같은 말 (`analysis_rules.toml` [growth] BRAND_HINT) — 광고비로 큰 채널일 수 있어 개인 채널과 따로 보라.

| 채널 | 기관·브랜드? | 개설 | 구독자 | 월 구독자 증가 | 최근 하루 증가 | 영상 수 | 월 업로드 | 길이 중앙값 | 주로 다룬 주제 | 대표 영상 (하루 조회수 큰 것) |
|---|---|---|---|---|---|---|---|---|---|---|
| 정이랑의 진기명기 |  | 2025-11-07 | 198,000 | 17,319 | – | 310 | 27.1 | 23.1분 | 6. 피아노·클래식·연주곡 | [2007년 우己lㄱr バr己б했던 학원☆™🎹 #정이랑 #추억 #공감 #…](https://www.youtube.com/watch?v=argmeBt7OUU) 2,916,955회 |
| 명곡부활단 |  | 2026-03-21 | 105,000 | 14,866 | – | 316 | 44.7 | 4.8분 | 5. 운동·드라이브·신나는, 9. 가요·발… | [여인 – 우리 가슴속 깊이 박혀 있던 그 노래, 듣는 순간 그 시절로 …](https://www.youtube.com/watch?v=a0iBRRoDnDw) 6,699,495회 |
| comfort space ♡ |  | 2026-04-12 | 79,900 | 12,667 | – | 128 | 20.3 | 360.0분 | 1. 수면·명상·힐링 | [go to sleep, you need it.](https://www.youtube.com/watch?v=Q5bDzSwLE8w) 3,313,166회 |
| ClassicalMusic … |  | 2026-04-22 | 74,200 | 12,410 | – | 165 | 27.6 | 81.3분 | 6. 피아노·클래식·연주곡 | [Adagio (Cello, Piano, Violin) - Beautif…](https://www.youtube.com/watch?v=wNpsTbqdBiw) 4,946,444회 |
| Quiet Tunęs |  | 2025-10-13 | 151,000 | 12,290 | – | 129 | 10.5 | 322.5분 | 1. 수면·명상·힐링 | [432Hz + 528Hz + 741Hz ∣ The Deepest Hea…](https://www.youtube.com/watch?v=Y5wQB1TTh2s) 8,589,203회 |
| Rb Lofi |  | 2026-08-23 | 23,700 | 12,024 | – | 29 | 14.7 | 18.5분 | 8. 로파이·시티팝·칠, 기타 | [ALL TRENDING HINDI SONGS 2026...PLAYLIS…](https://www.youtube.com/watch?v=xI0IEWIxUBQ) 9,921,293회 |
| Tom’s Jazz Loun… |  | 2026-04-25 | 71,000 | 12,007 | – | 105 | 17.8 | 75.4분 | 7. 재즈·보사노바 | [Just One More Drink -- Jazz Noir](https://www.youtube.com/watch?v=7gtIh5dF9Xk) 6,414,861회 |
| Milesora Lounge |  | 2026-04-14 | 66,900 | 10,718 | – | 189 | 30.3 | 77.4분 | 12. 커버·노래 부르기, 4. 카페·매장… | [Smooth Jazz & Soul R&B ∣ Soft Female Vo…](https://www.youtube.com/watch?v=YQHnz8VuazY) 2,344,500회 |
| Serenata |  | 2025-09-30 | 119,000 | 9,384 | – | 46 | 3.6 | 62.2분 | 기타 | [Popular OPM Hits 2026 🌿 New Filipino Pl…](https://www.youtube.com/watch?v=Ur4FFQT--Qw) 5,554,518회 |
| 80s Guitar Loun… |  | 2026-08-04 | 23,800 | 9,171 | – | 40 | 15.4 | 68.3분 | 6. 피아노·클래식·연주곡, 12. 커버·… | [Classic Love Songs ❤️ Timeless Acoustic…](https://www.youtube.com/watch?v=jDUH254gfs8) 583,619회 |
| Retrovivals |  | 2025-12-02 | 97,500 | 9,160 | – | 156 | 14.7 | 4.8분 | 14. AI 음악 | [Retrovivals - Kung Ako Nalang Sana - Bi…](https://www.youtube.com/watch?v=wbI70GOWw0U) 3,670,954회 |
| Nature for the … |  | 2026-08-24 | 17,200 | 9,027 | – | 80 | 42.0 | 3.0분 | 1. 수면·명상·힐링, 6. 피아노·클래식… | [Sultry Saxophone Beats • Smooth R&B Jaz…](https://www.youtube.com/watch?v=PxeZARMnC-0) 14,362회 |
| Baby Bon Bon - … |  | 2026-07-28 | 24,600 | 8,810 | – | 21 | 7.5 | 11.4분 | 기타 | [Lola the Cow Song! (La Vaca Lola) 🐄 Ani…](https://www.youtube.com/watch?v=irzJfFIeggM) 42,977회 |
| 레코드 속 추억 | 예(레코드) | 2026-04-10 | 56,000 | 8,787 | – | 132 | 20.7 | 81.8분 | 기타, 9. 가요·발라드·트로트 | [“꽃길” “인연” “묻어버린 아픔” “마지막 연인” “사랑 참”🎸🔥조회…](https://www.youtube.com/watch?v=YBeWbO46Gtw) 1,217,971회 |
| cozi_music |  | 2026-07-10 | 29,400 | 8,605 | – | 10 | 2.9 | 4.5분 | 기타, 8. 로파이·시티팝·칠 | [𓆩♡𓆪 𝑻𝑹𝑬𝑵𝑫𝑰𝑵𝑮 𝑺𝑶𝑵𝑮𝑺 𝑶𝑭 𝟐𝟎𝟐𝟔 𓆩♡𓆪 ∣∣ All t…](https://www.youtube.com/watch?v=85vOsUlmkjM) 472,957회 |
| Jasu LOFI |  | 2026-07-15 | 26,700 | 8,210 | – | 154 | 47.4 | 5.4분 | 8. 로파이·시티팝·칠, 기타 | [Patar Bashori ∣ পাতার বাঁশরী ∣ Lofi Ban…](https://www.youtube.com/watch?v=rgKNbCrC-cc) 8,123,568회 |
| Violinhop |  | 2025-09-19 | 103,000 | 7,898 | – | 160 | 12.3 | 71.7분 | 11. 힙합·R&B·EDM | [【Violin x Hip Hop Playlist】– My Truth i…](https://www.youtube.com/watch?v=TGYiJ5uoEtM) 2,307,847회 |
| Ayan Studio |  | 2026-01-28 | 67,400 | 7,713 | – | 122 | 14.0 | 4.6분 | 기타 | [Na Bole Esechhi ∣ Male Version ∣ Heart …](https://www.youtube.com/watch?v=AQhp6kCxIRM) 2,177,071회 |
| Soulful Breaths… |  | 2026-04-06 | 49,600 | 7,625 | – | 188 | 28.9 | 39.2분 | 1. 수면·명상·힐링, 6. 피아노·클래식… | [Morning Cortisol Detox 🌿 Raag Bhairavi …](https://www.youtube.com/watch?v=cjNH2q4aBYc) 1,016,110회 |
| NOXTUNE |  | 2026-07-29 | 20,700 | 7,501 | – | 17 | 6.2 | 11.1분 | 기타, 8. 로파이·시티팝·칠 | [Playlist For You To Create Fake Scenari…](https://www.youtube.com/watch?v=0gUwbTCQ78k) 6,498,348회 |
| 노래방 옆 만화방 |  | 2025-11-20 | 81,000 | 7,338 | – | 235 | 21.3 | 4.5분 | 10. 팝송·K팝·J팝, 9. 가요·발라드… | [정승환 & 박지원- 그 여자 (시크릿가든 OST) l [정승환의 노래방…](https://www.youtube.com/watch?v=QlOJ3HsA6Jk) 2,718,336회 |
| Frequencies of … |  | 2026-04-10 | 46,400 | 7,280 | – | 19 | 3.0 | 75.7분 | 1. 수면·명상·힐링, 6. 피아노·클래식… | [Cleanse Everything Draining You ∣ Heal …](https://www.youtube.com/watch?v=QNxiKUklOKQ) 952,294회 |
| ERRDAY GROOVE (… |  | 2025-11-05 | 81,700 | 7,085 | – | 226 | 19.6 | 4.1분 | 12. 커버·노래 부르기 | [엄정화 - 초대 [90's New Jack Swing Cover] (뉴…](https://www.youtube.com/watch?v=xNV5j1v53RY) 1,502,529회 |
| 국악딴따라 |  | 2026-05-19 | 35,000 | 6,874 | – | 49 | 9.6 | 3.7분 | 15. CCM·찬양·국악·동요, 1. 수면… | [국악딴따라 - 살아보니 그렇더라 (Official MV)](https://www.youtube.com/watch?v=FhNugHNh72s) 1,903,988회 |
| encore. |  | 2026-09-20 | 7,210 | 6,859 | – | 12 | 11.4 | 21.6분 | 기타 | [[Playlist] When music is all you need](https://www.youtube.com/watch?v=XXKXpf7xFC4) 2,875,464회 |

## 8. 시청자 니즈 (성공 사례 1088개의 시청자 댓글 353,829개 — 채널 주인 댓글·도배 댓글 2,999개 뺌)

갈래는 낱말 규칙 (한 댓글이 여러 갈래). '더 알고 싶은 것'은 ① **요청**(다뤄 주세요·알려 주세요·궁금해요 — 다음 영상 주제 후보, 아래 8-1) 과 ② 물음표 질문(반문이 섞임, 8-2) 으로 나눠 인용한다. **어느 갈래에도 안 듦** 줄을 같이 볼 것 — 갈래 비율은 낱말 규칙에 걸린 몫이다. 모든 댓글(승인 영상 전부)에 유형 하나를 붙인 분포는 `comment_types.md` (사람이 분류한 표본 1,100개 + 규칙 — 2번이 가장 믿을 숫자).

| 갈래 | 댓글 | 비율 | 좋아요 합 |
|---|---|---|---|
| 좋은 점 — 영상 (도움·설명·정리·공감) | 580 | 0.2% | 3,590 |
| 감사·응원 (일반) | 6,960 | 2.0% | 47,661 |
| 더 알고 싶은 것 (질문·요청) | 938 | 0.3% | 11,195 |
| 아쉬운 점 — 영상 (제목·광고·길이·정보 오류·목소리) | 424 | 0.1% | 2,541 |
| 반박·불만 — 의견 다름 (내용) | 220 | 0.1% | 1,366 |
| 정치·사회 (영상과 무관한 의견) | 132 | 0% | 2,092 |
| 경험 공유 (내 이야기) | 2,569 | 0.7% | 40,298 |
| 구독·다음 기대 | 441 | 0.1% | 1,648 |
| **어느 갈래에도 안 듦** | 342,695 | 97% | 2,255,836 |

### 좋은 점 — 영상 (도움·설명·정리·공감) — 좋아요 많은 댓글

- 👍229 [#16] “처음에 크레이지 아케이드 소리 들리길래 영상 잘못 들어온 줄 알았네 ㅋㅋㅋㅋ 하 첫 곡부터 마지막 곡까지 너무 레전드라서 쉬는 날에 엄청난 힐링하고 갑니다 ㅠ”
- 👍189 [#800] “조선힙합 멜로디도 좋지만 모든 곡들의 가사가 너무 마음에 와닿습니다. 좋은 노래 만들어줘서 감사합니다. 위안이 되는 따뜻한 노래들.”
- 👍150 [#446] “저는 지금 이 순에도 위태로운 제 자신을 부여잡고 눈물을 흘리며 하루하루를 버티는 중년의 여성입니다 삶을 내려 놓고 싶은 순간이 너무 많지만 생명의 질긴 끊이 저를 버텨주네요 사실 용기도 없습니다 젊은 시절은 부모님 상처드리기 싫어 버티는 심정으로 살았고 지금은 제 반려견 걱정에 버티고 있습니다 얼마나 더 버틸수 있을까요..눈을 뜨고 하루를 대하는 저의 일”
- 👍124 [#556] “스타즈 오늘 둘다 레전드네 ㄷㄷㄷ❤❤❤❤”
- 👍108 [#263] “안녕하세요, 오늘의 플리님! 저는 도덕 수업에서 선플 달기 활동을 하고 있는 중1 학생입니다. 영상 정말 잘 보고 있어요. 항상 좋은 영상 올려주셔서 감사합니다. 좋은 하루 보내세요”
- 👍78 [#16] “디지몬 어드벤처, 이누야샤, 달빛천사, 아따맘마, 피치피치핏치, 카우보이 비밥, 나루토, 개구리 중사 케로로, 캐릭캐릭 체인지, 원피스 등등... 이런 레전드 꿀잼 애니메이션들을 감상할 수 있었던 90년대생들은 진짜 선택받은 어린이들 세대였던 것 같습니다.”
- 👍60 [#680] “힐링음악님 요즘 세로운 영상 찾아 올리시는 라 수고가 많으시죠? 덕분에 이렇게 좋은 영상을 보네요 고맙습니다🙏 (어디로 부터 그대는 왔는가) 전 이 가사가 유난히 좋더라구요^^”
- 👍59 [#11] “우리가 고3만 아니였다면 맞춰갈 수 있는 시간이 있었을텐데 정말 아쉽고 힘들다 벌써 1달이 넘었는데 단 하루도 널 잊은적이 없어 살면서 사랑을 알려줘서 고마워 지금은 너에게 아무것도 안하는게 돕는거라고 생각해서 수능 끝나고 연락할거야 우리 입시 성공해서 다시 만나자 영원한건 없어도 다시 만난다면 평생 사랑할게”

### 감사·응원 (일반) — 좋아요 많은 댓글

- 👍1,687 [#446] “26년 병원 검사를 마치고, 어제부터 1년을 선물 받았습니다. 안전한 1년이길 🙏하면서 , 오늘은 좋아하는 음악을 들으며 가만히 쉬어 봅니다. 이런날 음악이 친구가 되어주고, 위로가 되어줍니다. 클래식을 잘 모르지만, 저는 마음으로 느껴지는 걸 중요하게 생각하며 듣습니다. 귀로만 듣는게 아니라 몸과 마음을 어루만져 주는 그 찰나의 순간을 느끼는 것이지요. ”
- 👍744 [#1056] “김간지한테 고맙습니다 해야지”
- 👍529 [#204] “진짜 많이 보고싶다. 내 고등학생 생활이 전부 너라서 너 말고는 아무것도 안보였던 시기엿어. 고등학교 동안 나한테 과분한 사랑 주고 항상 내 편이 되어줘서 너무너무 고마워 우리 성인되는 날에 같이 첫 술 마시자고 했었는데 기억나? 그 약속 이제는 못 지키겠다. 헤어질 때 너무 아팟고 너와의 좋았던 기억들이 너무 많은데도 그 힘들었던 기억들이 계속 괴롭혔어.”
- 👍528 [#446] “번개탄 피워놓고 죽으면 다끝이지 않을까? 하는 마음을 떨쳐버리고 마음추스린지 일주일 입니다 삶에 무게너무 무겁지만 그래도 살아가는것이 맞겠지...하는생각에...모두들 힘내보아요”
- 👍399 [#1037] “시험기간이라 그런지 요즘 영상이 많이 올라오네요 시험 화이팅 하세요”
- 👍252 [#240] “이 플리 듣고 자전거 타면서 수많은 지뢰를 피해서 겨우 탈북했네요~감사합니다 근데.. 앞에 누가 총을 들고있네요?”
- 👍250 [#773] “배경화면에 끌려서 클릭 했다가 환상적인 연주에 빠져들어서 맘을 쓸어내리며 감상해요.. 아름답고 애절한 연주 감상할 수 있게 해주셔서 감사합니다♡”
- 👍244 [#526] “마음을 행복하게 해주셔서 감사드립니다. 기쁨이 몽글몽글😊 건강해지는 기분입니다. 모두모두 행복하시기를... 좋은 선물 주시는 운영자님도 행복하시고, 좋은 일이 가득가득하시기를😊”

### 더 알고 싶은 것 (질문·요청) — 좋아요 많은 댓글

- 👍6,477 [#442] “대체 뭔노래가 나올까 궁금해서 들어왔습니다”
- 👍1,047 [#405] “개발할 때마다 듣습니다; 많이 올려주세요”
- 👍208 [#204] “여전히 잊지 못하였습니다. 당신이 나의 이상형이라서, 당신이 나의 첫사랑이라서, 끝난 관계임에도 나에게 잘 해줘서, 너무 착한 사람이라서, 귀여운 걸 본인만 몰라서, 허세 같은데 싫지 않은 적은 처음이라서, 영원을 약속하고 싶게 만든 사람이라서.. 이유는 수백 개 수천 개지만 그 정도로 당신이 좋은 이유가 수두룩 빽빽한데 이 이야기를 전할 수가 없습니다 이”
- 👍88 [#680] “김호중 테너의 활동 영상 발굴해서 많이 많이 올려주세요. 이미 완성된 테너 김호중 감동입니다.”
- 👍88 [#680] “기다렸습니다 김호중 테너님 공연 많이올려주시면 좋겠 습니다 영상감사합니다 🎉🎉🎉”
- 👍77 [#836] “할렐루야 주님께 영광돌립니다 . 호주에서 5년 살고 컴백한 시골사역 사모예요. 한국 정읍시 오주길 ~ 작은마을 개척교회사모입니다. 저희는 교회 사역에 필요한 야채 식료품 밭에서 직저자배해서 성도님들 섬기며 네팔에서 3월에 온 자매 형제님 선교도합니다. 한글공부 집중 중입니다 요즘 시골에 한국사람 없어 전도가 쉽지 않은데 네팔 🇳🇵 성도님들 제자삼아 성장시키”
- 👍76 [#1065] “파란색으로 블루베리도 만들어주세요!!!!”
- 👍69 [#947] “나중에 브금 매쉬업버전 말고 각각 올려주시면 안될까요”

### 아쉬운 점 — 영상 (제목·광고·길이·정보 오류·목소리) — 좋아요 많은 댓글

- 👍632 [#210] “현재 08년생 입니다.. 벌써 마지막 10대의 절반이 지났다는게 믿겨지지 않네요. 어릴때 저녁밥 먹기 전 동네 친구들과 술래잡기 하던게 엊그제 같은데 저에겐 항상 멀게만 느껴졌던 20대라는 현실을 곧 마주할 생각을 하니 솔직히 현실감이 없습니다.. 아직 추억도 많이 없고 즐기지못한게 많은거 같아 맨날 옛날로 돌아가고 싶다는 생각을 하곤 하는데 몇년 뒤엔 오”
- 👍70 [#789] “18년을 함께한 우리 고양이가 고양이별로 떠난지 4일째 되는 밤입니다. 집안 모든 곳이 냥이와 함께한 곳이라 가는 곳마다 눈물이 납니다. 마치 그곳에 앉아 있는 것 같아 나도 모르게 두 손을 뻗곤 합니다. 원없이 사랑한 것 같았는데 보내고나니 아쉬움과 후회만 밀려옵니다.”
- 👍64 [#692] “광고가 계속 나와요😢😢”
- 👍57 [#821] “가사는 모르지만, 애절하면서 흡인력 있는 목소리가 너무 좋습니다.”
- 👍51 [#680] “오늘 김호중 가수의 노래를 이것저것 찾아 듣고 있는데 이 노래를 듣게 되네요. 김호중 테너의 목소리가 너무 듣기 좋습니다. 이애숙님과 두 분 함께 부르는 노래가 완전 멋지네요. 올려주셔서 감사합니다 ~”
- 👍49 [#468] “남편의 계속 반복되는 외도로 어린아들 둘 데리고 이혼한지 9개월 눈물 흘릴 여유조차 없이 살다가 노래들으려고 켠 유튜브에서 우연히 발견한 노래들.. 마음을 보듬어 주는것같은 따뜻한 목소리에 눈물이 터져 울고 위로받고 갑니디 원래 안달지만 꼭 달고싶었어요. 오래 노래해주세요. 자주와서 들을게요. 너무 고맙습니다.”
- 👍45 [#670] “요즘 유튜브나 여러 플랫폼에서는 AI 기술을 활용해 특정 가수의 창법이나 음색을 학습시킨 커버 곡들이 정말 많이 쏟아지고 있네요. 특히 전통적인 록 발라드나 트로트 메들리 같은 영상 중에는 사람이 직접 부른 것처럼 정교하게 만들어졌지만, 실제로는 AI 목소리 모델을 입혀서 기계적으로 양산된 콘텐츠들이 꽤 많습니다. 음색이나 부르는 스타일이 지나치게 정형화되”
- 👍45 [#756] “AI로 작업했더라도 주인장 음악력 진짜 높은 듯. 듣기 편안한데 지루하지 않음.”

### 반박·불만 — 의견 다름 (내용) — 좋아요 많은 댓글

- 👍155 [#106] “선곡말도안됨”
- 👍142 [#1014] “아 메이플 관련 브금이랑 영상만 보면 저때로 돌아가고 싶다라는 생각이 계속 든다.. 무더운 여름방학 집에 에어컨도 없어서 방에서 선풍기 하나로 동생과 싸우고 한대 있는 컴퓨터로 너가 몇분을 더했니 어쨌니 그러다가 게임 금지 당하고.. 동생보다 30분이라도 먼저 일어나서 몰래 게임하고.. 지금은 동생도 나도 너무 많이 커버렸구나. 어렸을때 형이란 이유도 동생”
- 👍132 [#217] “-내가 약조하마.너를 지켜주겠다고. 그렇게 다정히 말씀하시던 든든한 나의 님은, 지금 풀숲에 쓰러져 간신히 숨만 내쉬고 계신다. -상공, 제발 숨만 쉬십시오. 제가 어떻게든... -연화야. 상공의 손이 나의 손은 따스히 잡아온다.그 온기가 서글프도록 따뜻해서, 심장 한편이 저릿하게 아려온다. -아닙니다, 그러지 마십시오. 지금이라도 의원을 부르면.. -너도”
- 👍113 [#297] “제목을 보자마자 한사람이 떠올라서 홀린듯이 클릭해버렸어요. 이런 플리 잘 안들을 것 같아서 그냥 터놓고 말할게. 중학교 때 처음 만난 언니. 정말 예쁘고, 멋지고 빛이 나서 이보다 주인공 같은 사람이 있을까 싶은 사람. 정병 와서 새벽에 연락해도 꼬박꼬박 답장해주고 내가 힘들때 옆에서 참 많을 위로를 해주었던 건 정말 아직도 고마워. 내가 죽지 않고 이렇게”
- 👍91 [#240] “탈북할 땐 어떤 노래를 듣는걸까 하고 왔는데 첫곡듣고 어이없어서 터졌네 ㅋㅋㅋㅋ 무슨 관련이야”
- 👍47 [#244] “왜 우리는 아는 사람들에게 위로받지 못하고 모르는 사람들에게 인터넷상에서 위로를 받는 걸까요 힘들다고 말하는 게 부끄러운 것도 아닌데 다른 사람들의 댓글을 보며 와.. 이런 사람들도 있구나 저런 사람들에 비하면 나는 행복한 거구나..라고 위안 삼으며 다시 또 지옥같이 지치는 일상으로 돌아가는 사람도 있고 다른 사람들의 댓글을 보며 위로를 받고 살아갈 용기를”
- 👍45 [#680] “너무잘한다 이런인재를 순간의 실수에 너무오래 가둬놓네 엄청난죄 지은 사람들도 다풀어주고 아예법의재제도 안하면서 국보급 가수한태는 왜그리 독한지 참어이없는 사법부다”
- 👍38 [#821] “80을 넘는 음악을 아는 사람도 아닌데 아득한 옛날 그리움을 노래하는 것 같네요...”

### 정치·사회 (영상과 무관한 의견) — 좋아요 많은 댓글

- 👍623 [#789] “사랑하는남편이 하늘나라가신지 두달하고십사일째입니다~ 제마음을 위로해주네요~”
- 👍522 [#195] “9:06 중국인들 탑 랩 파트, 학교를 안 갔어, 오빠오삐옵, 싸이노래 개좋아함”
- 👍85 [#680] “이런노래들으니 이나라가 얼마나 귀한지 모르겠습니다 망하는나라 한순간 우리가 모두 힘내어 지켜야 합니다”
- 👍32 [#773] “멎있는예술의나라인데~전쟁하지않으면좋겠다두나라가파괴되는게너무아깝다~제발세계펑화를후손들위해~음악이웅장하고뭉클합니다”
- 👍26 [#88] “난 한국인인데 한국 사람들한탠 이런 이미지가 없단게 너무 슬프다 러시아나 다른 나라들의 사람들이라 하면 다들 각자의 신비롭고 그런 이미지들이 있는데 한국인이라고 하면 그냥 kpop이니 뭐니 하는 그런 재미없고 오글거리는것들밖에 없으니까 너무 아쉬움 정부가 한국콘텐츠진흥원같은거까지 만들어가면서 지원하지만 않았어도 이렇겐 안됬을거같다 그냥 차라리 스타크레프트 ”
- 👍24 [#20] “그냥 케이팝,드라마,예능 다 2010년대 이후로 이제 옛날같지않더라 케이팝으로 유명하던 우리나라가 더 이상 그냥 챌린지하는 노래밖에 안나오고..어제 청룡?보니까 확실히 전과 다름 연말에 가족끼리 시상식보는 감성도 사라진듯 다 모르는것들만 나오고 옛날엔 드라마도 지금보면 ㄹㅈㄷ인거 많이 나오고 예능도 신서유기,무도 등등 지금보면 ㄹㅈㄷ인거 많았는데 지금 보면”
- 👍23 [#658] “이재성..가장 뛰어난 싱어송라이터였는데.. 고독한DJ라는..노래불렀다가....전두환정권에서.방송금지당해..최전성기..87년에...갑자기TV에서.사라졌고.. 라디오에서도 이재성 노래를 10년동안 들을수 없었음.”
- 👍20 [#19] “영상이 기괴하다더니 진짜 그렀네~ ㅠㅠ 외국인들은 예술로 보는게 놀랍다 한국이 인신제사에 쓰이려나”

### 경험 공유 (내 이야기) — 좋아요 많은 댓글

- 👍2,673 [#204] “야 보고싶어 내 생일에 연락 왜 안했냐 너 밥 한끼 더 좋은거 먹으라고 네가 기념일마다 줬던 토스 기프티콘 일부러 안 썼어 너한테 입금 됐냐 돈 하나도 안 아까운데 그냥 그렇다고 내 계좌 비밀번호 우리 만난 날이야 내 노트북 비밀번호도 우리 만난 날이야 훔쳐가도 되는데 홍대에서 이제 공연해? 아직인가 너한테 기타 쳐달라고 했던 노래가 하필 이 영상 첫 노래”
- 👍2,513 [#210] “내가 왜 고3일까… 평생 안 올 줄 알았는데 ㅠㅠㅠㅠ 뽀로로 너랑 걱정없이 놀 때가 너무 그리워…”
- 👍1,898 [#210] “뉴스에서 고등학생 자살율 얘기할때 진짜 이해 안됐는데 막상 고등학생 되니까 내가 그 경계에 서있네”
- 👍1,308 [#442] “나도 모르게 "아 지랄 ㅋㅋ" 하면서 들어왔네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 아 미친”
- 👍1,252 [#942] “영상 내려가서 내가 멘헤라될뻔”
- 👍1,217 [#1037] “하트누르면 모두들 행복해지고 시험 잘 볼 거임!! 나도 포함”
- 👍1,132 [#204] “이 세상 단 둘만 가진 기억인데 아까워서 어떻게 잊나요 내가,”
- 👍1,069 [#244] “요즘 옥상문이 잠겨있네요 더워서 그런가 벌써 네 건물 가봤는데 잠겨서 죽고싶은데 마음데로 죽지도 못하네요 얼마전에 울다가 깨닳았어요 아 나 안죽고싶은데.. 내가 죽고싶은게 아니라 지금이 너무 힘들어서 차라리 죽고싶은거구나 아 행복해지고 싶은거구나 죽고싶은게 아니라 행복해지고 싶은데 행복이 저는 너무 어려워요 행복하고싶었던거라는 생각이 들지마자 너무 서러워서”

### 구독·다음 기대 — 좋아요 많은 댓글

- 👍110 [#800] “듣다보니. 가슴에 스며들어 구독하고. 계속 듣게 되네요 60후반이지만 요즘 젊은이들 조선힙합이 꽂치네요 좋은음악. ~^^❤❤❤”
- 👍105 [#680] “김호중님의 무대가 기다려집니다”
- 👍75 [#979] “슬프고도 정화된 아름다운 선율 듣자마자 바로 구독하고 영혼의 단짝 친구와 공유했습니다 평생을 추구해온 제 삶의 궤적을 위로해주는 선율과 가사는 눈감고 들어도 한마디 한마디가 너무나 아름답습니다 저를 숨기고 제 슬픔을 숨기고 제 진실을 숨기고 모두에게서 옹달샘처럼 숨어있는 제 영혼이 공감받고 위로받는 듯 했습니다 이 채널을 준비해주신 그대에게 감사를 전하고자”
- 👍48 [#719] “구독박고 갑니다 태어나서 이렇게 섹시한 남자 첨이에요 허남준땜시 잠이 안와요 매일 유투브로 찾아봐도 질리지 않아요 ㅋ”
- 👍42 [#860] “썸녜일도 느낌.있고.음악도 좋네요 ! 음악은 ai로 만드신건가요?궁금. 그림도 왠지 직접그리신듯 구독하고가요😊”
- 👍32 [#277] “이별 벌써 20년째 저는 가족 반대 때문에 헤어진 한남자 잊지 못합니다 지금 도 그사람 잊지 못합니다 아니 영윈히 기다려요 이노래가 아퍼요 그사람 마음 같아😢”
- 👍18 [#525] “아침찬양에 너무 잘 맞는 목소리와 은혜입니다. 첫곡듣고 바로 구독했습니다”
- 👍17 [#662] “첨들어봤는데 넘좋아서 바로 구독했어요. 50대 주부~😊”

### 8-1. 더 알고 싶은 것 ① 요청 — 다뤄 주세요·알려 주세요·궁금해요 (705개 중 좋아요 순, 영상마다 2개까지)

- 👍6,477 [#442] “대체 뭔노래가 나올까 궁금해서 들어왔습니다”
- 👍1,047 [#405] “개발할 때마다 듣습니다; 많이 올려주세요”
- 👍88 [#680] “김호중 테너의 활동 영상 발굴해서 많이 많이 올려주세요. 이미 완성된 테너 김호중 감동입니다.”
- 👍88 [#680] “기다렸습니다 김호중 테너님 공연 많이올려주시면 좋겠 습니다 영상감사합니다 🎉🎉🎉”
- 👍77 [#836] “할렐루야 주님께 영광돌립니다 . 호주에서 5년 살고 컴백한 시골사역 사모예요. 한국 정읍시 오주길 ~ 작은마을 개척교회사모입니다. 저희는 교회 사역에 필요한 야채 식료품 밭에서 직저자배해서 성도님들 섬기며 네팔에서 3월에 온 자매 형제님 선교도합니다. 한글공부 집중 중입니다 요즘 시골에 한국사람 없어 전도가 쉽지 않은데 네팔 🇳🇵 성도님들 제자삼아 성장시키”
- 👍76 [#1065] “파란색으로 블루베리도 만들어주세요!!!!”
- 👍69 [#947] “나중에 브금 매쉬업버전 말고 각각 올려주시면 안될까요”
- 👍68 [#593] “8주된 뱃속의 아기를 와이프와 보내고 상심이 큰 어제와 오늘이었습니다. 와이프에게 어떻게 하면 힘이 될 수 있을까 하다 우연히 듣게 되었는데, 마치 고즈넉한 숲 속 궁전에서 여유로운 하루를 맞이하는 느낌을 주는 노래 같아 하루 종일 듣고 있습니다. 힘 내볼게요. 앞으로도 좋은 노래 많이 올려주세요”
- 👍62 [#593] “최고에요! 제 브이로그 배경음악으로 클래식을 많이 쓰는데, 혹시 출처표시하고 bgm으로 쓸 수 있을까요? 안되더라두 괜찮으니 편하게 알려주세요! 좋은 음악 감사합니다! :)”
- 👍54 [#412] “아 진짜 주인장 제발 이 플레이리스트 더 길게 만들어주세요 제발요”
- 👍47 [#860] “트랙리스트 위에있는 글은 주인장님이 써내려간 글귀일까요? 너무 멋져요.. ❤ 혹시 책의 한 소절이라면 제목을 알려주실 수 있으실까요😊”
- 👍45 [#121] “첫번째 나온 노래 너무 좋은데 가수랑 제목좀 알려주세요.. 아무리 찾아도 안나와요 😢”
- 👍41 [#693] “혹시 투어스 노래 모음 만들어 주실수 있나여..?”
- 👍35 [#34] “개조아요 타임라인 올려주세요”
- 👍33 [#854] “우선 이런 질문드려 죄송합니다. 제 생애 최고의 전율을 느꼈습니다. 그래서 무지한 질문을 드리더라도 용서부탁드립니다. 유튜브 보다가 떠서 감상하게 되었는데, 어느분이 부르신걸까요? 혹시 설명란에 있는것처럼 ai로 만드신 걸까요?”
- 👍32 [#333] “저런 얼굴하고 물어보면 어 아니 너가 훨씬 나아 가 나올듯 노래 리스트가 너무 좋아유 계속 올려주세요!”
- 👍32 [#968] “호르몬제는 무서워서 못 먹고 영양제 알아보던 중이에요. 한 번 깨면 다시 잠드는 게 너무 힘들어요. 흡수 잘 된다는 리포좀멜라토닌에 감태·레몬밤·가바 같이 들어간 각성완화제 먹고 있는데 엄청 센 건 아닌데 누우면 좀 차분해지긴 하더라고요. 같은 나이대 분들 어떻게 넘기시는지 궁금하네요.”
- 👍30 [#232] “진짜 ' '서운 이야기 띵!... 똥!... 유튜브 댓글에 알람이 떴어. "저 브라질 펑크에 관심이 많은데 이 분이 브라질 펑크 부른거만 모아서 영상 만들어 주실 수 있나요?" 그냥 자기가 듣고 찾아서 모음 딸깍하면 되는 황당한 요구를 하다니.. 저 사람은 너무 '오만'해 그 때.. '궈바오러우'가 나타났어”
- 👍30 [#664] “55분에 시작하는 노래 가수와 제목좀 알려주세요ㅜㅜ”
- 👍29 [#106] “진짜 댓글 앵간하면 안쓰는데 이거 조합 ㅈ됨 너무좋다 여자여자스러운데 당당하고 자존감높은 여자 플리임 이런거 너무 좋아서 맨날 들을거 같음 더 만들어주세요❤”
- 👍29 [#979] “아다지오 평소에 사랑헸던 곡입니다...윌리엄님의 올리신곡은 또다른 멋으로 다가옵니다.사랑합니다.축복합니다.감사합니다.늘 좋은 음악.아름다운음악 부탁드립니다. 건강하세요”
- 👍27 [#947] “지킬만 분리해서 올려주세요 따로도 듣고 싶어요”
- 👍23 [#183] “노래다운받는방법 알려주세요”
- 👍23 [#635] “안녕하세요!오산중학교에다니는 3학년학생입니다.기술시간에 선플달기를 하고있는데 요즘 점점여름이 다가오는시기여서 그런지 이영상이 알고리즘에 떴더라고요!시원한 여름플리너무 잘만들어주셔서 잘들을것같아요!모두 시원한여름보내시고 앞으로더 좋은영상 많이 만들어주세요💕”
- 👍22 [#914] “청주에서 나주로 오는길에 우연히 들었는데 3시간 거리동안 거의 2시간을 무한반복 하면서 들었네요 덕분에 심심하지 않게 잘 내려왔습니다. 당신은 천재 이십니다. 감사합니다.계속 좋은음악 부탁합니다.😊”
- 👍21 [#400] “너무 시원하고 감동적인 노래 잘듣고 갑니다 앞으로도 더욱 많은 노래 올려주세요”
- 👍20 [#449] “순천부영초등학교 이지인입니다 이챌린지을많이봤어요 이노래를듣으면 우울할때기분이 좋아져서이노래에 댓글을달았어요앞으로 신나는노래많이 올려주세요”
- 👍20 [#484] “낮엔 피곤한데 밤엔 또렷해서 멜라토닌 알아봤네요. 요즘 부쩍 잠이 얕아지고 감정 기복에 잠까지 설쳐요. 일반 멜라토닌은 흡수가 별로라길래 리포좀멜라토닌에 가바·테아닌까지 든 각성완화제로 바꿔봤는데 엄청 센 건 아닌데 누우면 좀 차분해지긴 하더라고요. 같은 또래 워킹맘분들은 어떻게 관리하시나 궁금해요.”
- 👍20 [#960] “아들건강하게 해주시고 대운 부탁드립니다❤❤❤❤❤❤❤”
- 👍19 [#664] “1시 9분 가수좀 알 수 있을까요?? 노래제목좀 부탁드려요 🙏”
- 👍19 [#944] “멜론에도 올려주세요 제발”
- 👍18 [#902] “혹시 실제 부르시는건지 AI 인지 궁금하네요 너무 은혜로와서~ 너무 잘하셔서~~”
- 👍17 [#653] “2번째 노래 제목 좀 부탁드립니다. 너무 좋아요”
- 👍15 [#263] “노래 제목 부탁드립니다 아재라서 하나도 몰라요 ㅜㅡㅜ 40중반 아저씨의 간곡한 부탁입니다 ~!!!”
- 👍15 [#553] “첫번째 곡이랑 비슷한 노래 추천 좀 해주세요ㅠ 첫 곡이 너무 좋은데 찾아봐도 없어요ㅜㅜ”
- 👍14 [#730] “와 첫번째 노래 궁금하다 좋으네”
- 👍14 [#825] “우연히 듣게 됐는데 너무 상큼하고 너무 행복해져요. 제목도 알고 싶은데.. 방법 없을까요?”
- 👍14 [#860] “가사하나 없는 플리인데.. 들으면 마음이 진짜 편안해져요ㅎㅎ 적당히 잔잔하면서 넘 좋아요ㅎㅎ 몇주간 이 채널의 플리만 계속 무의식적으로 들었네요❤️ 좋은 플리 많이 올려주세요❤️”
- 👍13 [#1007] “와 썸네일 지나가듯이 봤는데 무언가 잘못된 썸네일을 봤는데...라는 느낌을 받음과 동시에 새로고침을했는데 너무 궁금해서 헤매고 다녔다”
- 👍12 [#391] “이런 느낌으로 좀 더 만들어주세요ㅠㅠ 너무 제스탈 인생리스트!!”

### 8-2. 더 알고 싶은 것 ② 물음표 질문 (반문이 섞임 — 좋아요 순, 최상위 댓글)

- 👍208 [#204] “여전히 잊지 못하였습니다. 당신이 나의 이상형이라서, 당신이 나의 첫사랑이라서, 끝난 관계임에도 나에게 잘 해줘서, 너무 착한 사람이라서, 귀여운 걸 본인만 몰라서, 허세 같은데 싫지 않은 적은 처음이라서, 영원을 약속하고 싶게 만든 사람이라서.. 이유는 수백 개 수천 개지만 그 정도로 당신이 좋은 이유가 수두룩 빽빽한데 이 이야기를 전할 수가 없습니다 이”
- 👍56 [#244] “어릴 땐 어른이 부러웠습니다. 아무거나 다 할 수 있는. 하지만 정작 어른이 된 저는 삶에 휩쓸려 무뎌지고 부서진, 그런 사람이라는 걸 깨닫게 되었습니다. 우리 다시 돌아갈 수 있을까요? 아무 걱정 없이, 아무 생각도 안 하는 그때로”
- 👍32 [#680] “오 😮이 반가운 영상 어떻케 오늘에야 만나죠? 언제인가요? 김호중 코리아나 이애숙님. 이죠?”
- 👍31 [#932] “언제 상송이 나오죠?”
- 👍16 [#11] “제 연인이 표현을 잘 안하는 편이에요 근데 저는 표현도 많이 하고 남자지만 불안형이거든요 연애초긴 하지만 그녀의 마음이 어떤지 연락도 잘 안될땐 뭘 하는지도 궁금하고 불안하고 그래요 어떻게 고칠까요?”
- 👍15 [#639] “뮤비좋은데 라이브 가능한가요?”
- 👍15 [#852] “혹시 첫 번째 노래 가수를 있을까요? 검색으로는 안 나와서요ㅜㅜ 가사를 보고 싶은데ㅜㅜ”
- 👍15 [#933] “안녕하세요~ 혹시 이 음악을 행사 진행 중에 사용하기 위해 다운로드할 수 있을까요? 감사합니다🙏🏼너무 좋아합니다❤️‍🔥”
- 👍13 [#316] “와~~ 정말 가슴이 뻥 뚫리고. 머리가 신선해집니다 어쩜 저런 보물이 있을까요? 수연양!!! 사랑합니다 할아버지 할머니랑 영원히 행복하세요~~~!!”
- 👍13 [#702] “가수가 어떻게 되나요?”
- 👍12 [#663] “혹시 배경 어딘지 정보알수있을까요?”
- 👍12 [#805] “혹시 흘러나오는 여자 목소리 가수이름 알수있을까요? 엄마가 궁금해하셔서요ㅠ”
- 👍11 [#425] “집사람이 좋아하네요 혹시 악보를 구입할수있을까요??”
- 👍11 [#942] “혹시 저 그림 웹툰이면 제목 알수있을까요?”
- 👍10 [#182] “이 노래를 들으면서 떠오르는 계절은 어느 계절인가요? 봄, 여름, 가을, 겨울 중 하나를 골라주세요. 🍂”
- 👍10 [#320] “영상의 사진이 어디서 나온 것인지 알 수 있을까요?”
- 👍10 [#758] “혹시 기뻐하며 경배하세 MR 어디서 구할 수 있을까요? 딸아이 결혼식에 혼주 입장곡으로 쓰고 싶어서요~”
- 👍8 [#204] “저두 가슴이 미어지는 사랑을 해보고싶어용 이성적인 감정은 언제 생기는건가요? 아무리 봐두 친구로밖에 안느껴지는데…”
- 👍8 [#412] “사진 출처 어딘지 알수있을까요?”
- 👍8 [#468] “첫번째 노래 가수 이름 알수있을까요?”

### 8-3. 아쉬운 점 — 영상에 대한 비판 (좋아요 순, 답글 포함)

- 👍632 [#210] “현재 08년생 입니다.. 벌써 마지막 10대의 절반이 지났다는게 믿겨지지 않네요. 어릴때 저녁밥 먹기 전 동네 친구들과 술래잡기 하던게 엊그제 같은데 저에겐 항상 멀게만 느껴졌던 20대라는 현실을 곧 마주할 생각을 하니 솔직히 현실감이 없습니다.. 아직 추억도 많이 없고 즐기지못한게 많은거 같아 맨날 옛날로 돌아가고 싶다는 생각을 하곤 하는데 몇년 뒤엔 오”
- 👍70 [#789] “18년을 함께한 우리 고양이가 고양이별로 떠난지 4일째 되는 밤입니다. 집안 모든 곳이 냥이와 함께한 곳이라 가는 곳마다 눈물이 납니다. 마치 그곳에 앉아 있는 것 같아 나도 모르게 두 손을 뻗곤 합니다. 원없이 사랑한 것 같았는데 보내고나니 아쉬움과 후회만 밀려옵니다.”
- 👍64 [#692] “광고가 계속 나와요😢😢”
- 👍58 [#20] (답글) “진짜요..ㅜㅜ다시는 이런 케이팝만의 분의기를 못 본다는게 너무 아쉬움…”
- 👍57 [#821] “가사는 모르지만, 애절하면서 흡인력 있는 목소리가 너무 좋습니다.”
- 👍51 [#680] “오늘 김호중 가수의 노래를 이것저것 찾아 듣고 있는데 이 노래를 듣게 되네요. 김호중 테너의 목소리가 너무 듣기 좋습니다. 이애숙님과 두 분 함께 부르는 노래가 완전 멋지네요. 올려주셔서 감사합니다 ~”
- 👍49 [#468] “남편의 계속 반복되는 외도로 어린아들 둘 데리고 이혼한지 9개월 눈물 흘릴 여유조차 없이 살다가 노래들으려고 켠 유튜브에서 우연히 발견한 노래들.. 마음을 보듬어 주는것같은 따뜻한 목소리에 눈물이 터져 울고 위로받고 갑니디 원래 안달지만 꼭 달고싶었어요. 오래 노래해주세요. 자주와서 들을게요. 너무 고맙습니다.”
- 👍45 [#670] “요즘 유튜브나 여러 플랫폼에서는 AI 기술을 활용해 특정 가수의 창법이나 음색을 학습시킨 커버 곡들이 정말 많이 쏟아지고 있네요. 특히 전통적인 록 발라드나 트로트 메들리 같은 영상 중에는 사람이 직접 부른 것처럼 정교하게 만들어졌지만, 실제로는 AI 목소리 모델을 입혀서 기계적으로 양산된 콘텐츠들이 꽤 많습니다. 음색이나 부르는 스타일이 지나치게 정형화되”
- 👍45 [#756] “AI로 작업했더라도 주인장 음악력 진짜 높은 듯. 듣기 편안한데 지루하지 않음.”
- 👍40 [#773] “너무 너무 멋진 분위기 취할수있는 선율. 감흡! 늦은밤까지 이어질듯요 무한반복~~😊😊😊”
- 👍38 [#1056] “그저 사막을 지나 가는 것 같던 20대 나의 맘 속에 요술 왕자 당신은 누구신가요 아무도 모르지만 탱탱볼을 던지고 사라지는 꿈을 쫓다 지치길 지나 나의 미래에게 Waiting for your calling back 반복되는 감정의 미끄럼틀 그리고 오늘 아침 미국에서 만나는 신나는 음악, 잘못된 인생 술탄 오브 더 디스코는 나의 청춘 고마워요, 술탄 혼자 외”
- 👍35 [#525] “두분다 목소리가 너무 좋으셔서 자꾸 듣게되요~찬송가도 너무좋지만 목소리가 엄청 편안하고 부드러워요”
- 👍34 [#839] “제 노래 스퇄일 최고입니다😊 가수 목소리 좋고 선곡도 최고 운동할때 이어폰 귀에 꼽고❤ 한시간 넘게 운동하는데 지루함 없이 운동합니다 대박 기원합니다🎉🎉🎉🎉🎉”
- 👍33 [#709] “역시나 보이스칼라가 독보적입니다.언제들어도 너무 감동입니다. 영상편집이 정성이 많이 들어간게 보이네요,보는 내내 웃게 되네요.👏👏👏👏👏👏👏👍👍👍김호중 테너 너무보고싶네요.무대에 서신 모습 빨리 보고싶어요”
- 👍27 [#19] (답글) “이 뮤직비디오를 보이콧해 주세요. 이 영상과 제니의 다른 몇몇 영상에는 자막이 없습니다. 청각 장애가 있는 사람으로서, 가사와 노래 속에서의 위치까지 완전히 외우기 전까지는 자막 없이 뮤직비디오를 보면서 노래 내용을 이해하기가 어렵습니다. 제니는 돈도 많고 팀도 큰데, 뮤직비디오에 자막을 넣을 사람을 구하는 건 식은 죽 먹기일 텐데요. 이건 무지한 행동입니”
- 👍26 [#11] “가장 헷갈린 시기 같아요 잘하고 있다고 누가 꼭 안아주면 좋겠어요 열심히 살았는데 아쉬움이 항상 남네요”
- 👍26 [#405] “이거 들으면서 학원 숙제 베꼈는데 밀려써서 걸렸습니다 조심하세요”
- 👍23 [#656] “청춘은 서툴기에 그 자체로 빛난다. 완벽하다면 너무 지루할테니까..”
- 👍23 [#661] “AI목소리든 아니든 지친 영혼을 달래주면 그뿐. 감상잘했습니다 ^^”
- 👍22 [#914] “청주에서 나주로 오는길에 우연히 들었는데 3시간 거리동안 거의 2시간을 무한반복 하면서 들었네요 덕분에 심심하지 않게 잘 내려왔습니다. 당신은 천재 이십니다. 감사합니다.계속 좋은음악 부탁합니다.😊”

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
- `analysis_cases_28.md` — #1081–#1088
