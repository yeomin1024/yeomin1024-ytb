# 음악 — 성공 사례 분석 (지시사항 재료)

자동 생성 — `tools/success_analysis.py` v1.5.1 (2026-10-24 07:42 UTC), 규칙 `music/analysis_rules.toml` v1.5. **이 문서는 숫자와 원문만 담는다 — 해석·지시사항은 이것을 읽는 AI 가 만든다.** 주별 추세는 `weekly.md`, 승인한 영상 전부는 `approved.md`. ※ 연구·교육용 — 투자 권유가 아님.

## 0. 자료와 한계

| 자료 | 수 |
|---|---|
| 사례 폴더 (설명·자막·댓글·썸네일을 받은 영상) | 1505 (웹 승인 1505) |
| **성공 사례** — 180일 안·구독자 50,000 이하·조회수 ≥ 구독자 × 3·10,000회 이상·4분 이상, 채널당 2개 | **1055** (기준 통과 1225 − 뺀 것 42 − 채널당 제한 128) |
| **하루 조회수 상위** (1-3번 — 성공 사례와 따로) — 검색에서 찾은 주제 관련 4분 이상 영상 2,840개 중 하루 조회수 상위 10% (하루 28,349회 이상), 구독자·올린 날짜 상관없이, 채널당 2개 | **214** (기준 통과 253 − 뺀 것 31 − 채널당 제한 8) · 자료를 받지 않은 후보 64 |
| 성공 사례의 글 출처 (자막·음성인식·설명·없음) | 설명 980 · 없음 75 |
| 성공 사례 대본 — 전체 · 앞부분만(음성인식 1차) · 없음 | 0 · 0 · 1055 |
| 같은 채널 기준선 (채널 평소 영상) | 성공 사례 946/1055 · 채널 1031곳 (잘된 영상 3608 · 평소 영상 4173) |
| 성공 사례 댓글 (받은 / 달린) | 406,242 / 427,274 |
| 성공 사례 썸네일 | 1055 |
| 비교 집단 — 탐색에서 본 영상 중 구독자 50,000 이하·4분 이상·365일 안·주제 관련, 채널당 최근 5개 | 5831 (성공 1107 = 19%, 채널당 제한으로 뺀 23559) |
| 자료를 받지 않은 성공 후보 (웹 화면에서 승인하면 들어감 — 채널당 자리가 남은 것만) | 699 (자리가 찬 채널의 2,701개 뺌) |
| 수요·공급 시장 — 최근 90일 영상 (채널 크기 상관없음) | 850 · 검색어 61 · 자동완성 말 514 (공급 확인 0) |
| 채널 성장 자료 (개설일이 있는 채널) | 2147 (빨리 크는 작은 채널 25) |

성공 기준은 넘었지만 뺀 영상: Main Kabhi Bhoolunga Na Tujhe… (광고 의심(좋아요·댓글 거의 없음)) · SAD LO-FI 🥺 💔 2026 Ultimate M… (광고 의심(좋아요·댓글 거의 없음)) · Repvblik - Sandiwara Cinta (K… (광고 의심(좋아요·댓글 거의 없음)) · Baby Bear ∣ Colorful Caterpil… (광고 의심(좋아요·댓글 거의 없음)) · "Free" Cover ∣ Rumi Was Left … (광고 의심(좋아요·댓글 거의 없음)) · Nain Tere 🖤 Slowed + Reverb ∣… (광고 의심(좋아요·댓글 거의 없음)) · মন ছুঁয়ে যাওয়া বাংলা ∣∣ Bes… (광고 의심(좋아요·댓글 거의 없음)) · Dupatta Sarak Raha Hai 💕 ∣ Sl… (광고 의심(좋아요·댓글 거의 없음)) · I’d Rather – Acoustic + Saxop… (광고 의심(좋아요·댓글 거의 없음)) · SAD LO-FI 🥺 💔 2026 Ultimate M… (광고 의심(좋아요·댓글 거의 없음)) · Dekhne walon ne kya kya nahi … (광고 의심(좋아요·댓글 거의 없음)) · Indigenous Drumming Punctuate… (광고 의심(좋아요·댓글 거의 없음))

**한계**

- 대본(자막·음성인식)이 없는 성공 사례 1055개 (#1, #2, #3, #4, #5, #6, #7, #8, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26, #27, #28, #29, #30 …) — 설명란·챕터만 있음. 도입부·구성·말 속도는 대본이 있는 0개로만 셌다 (음성인식이 끝나면 다시 셈)
- 비교 집단 5831개 = 검색(조회수 순 — 잘된 영상 쪽으로 치우침)·추가한 채널·성공 사례 채널의 평소 영상 4584개 (치우침 없음) 에서 올린 지 7~365일 영상, 성공 비율 19% — 실제 시장 비율이 아니다. 같은 집단 안의 '있음/없음' 차이로만 보고, '무엇이 먹혔나'는 1-2번(같은 채널 안)을 먼저 보라
- 외국 영상을 넣음 (주제 설정 INCLUDE_FOREIGN = true) — 성공 사례 중 외국 영상 691개 (#1, #4, #5, #6, #7, #8, #9, #10, #11, #15, #16, #17, #18, #19, #21, #22, #23, #24, #26, #29, #33, #34, #35, #36, #38, #39, #40, #41, #42, #43). 말 속도(한글 음절)는 한국어 영상만으로 셌고, 제목 특징·댓글 갈래(질문·요청 등)는 한국어 낱말 규칙이라 외국 영상에는 거의 걸리지 않는다 — 외국 사례는 원문을 직접 읽어라
- 하루 조회수 상위 묶음(1-3번) 214개는 구독자·올린 날짜 상관없이 골랐다 — 큰 채널(구독자 50,000 넘음) 95개라 채널 힘(구독자·추천)이 섞여 있다. 작은 채널이 따라 할 근거는 1번 성공 사례로 보라. 하루 조회수 = 조회수 ÷ 올린 지 날수라 갓 올린 영상(며칠)은 부풀고 오래된 영상은 낮아진다. 경계는 검색 결과(조회수 순 — 잘된 쪽으로 치우침) 2840개 안의 상위 10%. 자료를 받지 않은 후보 64개 (웹 화면에서 승인하면 들어감)
- 같은 채널 기준선이 있는 성공 사례 946/1055개 (채널 영상이 5개 미만이거나 아직 못 받음)
- 수요·공급의 '시장'은 탐색·검색에서 본 최근 90일 영상 850개 — 검색이 조회수 순이라 조회수 적은 영상이 덜 잡힌다. 주제 묶음 사이의 상대 비교(지수)로만 보라
- 자동완성 말의 '최근 영상 수'는 우리가 본 영상만 셌다 — 실제 공급은 웹 화면 [공급 확인](말 하나에 검색 1번 = 100단위)으로 확인
- 자동완성 말에는 책·방송·사람·채널 이름도 섞인다 (예: '…를 찾아서'·'…지침서') — 영상 주제가 아닌 말은 건너뛰고 읽어라
- '구독자가 많이 모이는가'는 YouTube API 로 영상별 구독 증가를 볼 수 없다 — 대신 채널 성장(7번: 개설 뒤 월 구독자·받을 때마다 남긴 기록), '구독·다음 기대' 댓글, 배수(조회수÷구독자)로 본다
- 댓글 갈래·제목 특징은 낱말 규칙이라 거칠다 (물음표 반문도 '질문', 한 댓글이 여러 갈래). 원문 인용을 함께 보라
- '눈에 띔'은 차이가 크고 표본이 충분하다는 표시일 뿐 원인이 아니다

## 1. 성공 사례 (1055개 — 배수 큰 순)

배수 = 조회수 ÷ 구독자. **채널 평소 대비** = 조회수 ÷ 그 채널 최근 롱폼 조회수 중앙값 (같은 채널 기준선 — 클수록 그 영상만의 힘). 썸네일은 5번(장마다 20개, 번호 = #), 사례별 자세히는 **`analysis_cases_01.md` …** (9번).

| # | 제목 | 채널 | 구독자 | 조회수 | 배수 | 채널 평소 대비 | 하루 조회수 | 길이 | 업로드 | 주제 묶음 | 형식 | 글 출처 | 댓글 받은/달린 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Jay Wheeler, Omar Courtz - De Lejitos (Remix) (Video Oficia…](https://www.youtube.com/watch?v=xCkf2L7gFnI) | JayWheelerVEVO | 6,830 | 122,505,421 | 17,936.4 | ×163.3 | 832,084.4 | 4.7분 | 2026-05-30 | 기타 | 음악 | 설명 | 4,024/4,041 |
| 2 | [너의 차선](https://www.youtube.com/watch?v=B9zWtLub7tk) | 조선힙합 - Topic | 25 | 1,504,015 | 15,040.1 | ×98.7 | 13,187.8 | 4.2분 | 2026-07-02 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 0/50 |
| 3 | [노엘 IT'S YOU (한요한 없는 버전 10m)](https://www.youtube.com/watch?v=82Li_A-cPWA) | 갱갱 | 77 | 465,768 | 4,657.7 | – | 2,776.9 | 10.3분 | 2026-05-09 | 기타 | 플레이리스트·모음 | 설명 | 123/123 |
| 4 | [Tìm Em](https://www.youtube.com/watch?v=PnGk00MuNM4) | Hngle - Topic | 1,350 | 4,582,506 | 3,394.4 | – | 35,862.8 | 4.6분 | 2026-06-18 | 기타 | 음악 | 설명 | 0/227 |
| 5 | [ขึ้นใจ (3am call)](https://www.youtube.com/watch?v=r1Eb1qnqLzA) | Mirrr - Topic | 4,290 | 12,861,686 | 2,998.1 | ×570.2 | 138,070.5 | 4.4분 | 2026-07-23 | 기타 | 음악 | 설명 | 0/281 |
| 6 | [Veer Hanumana Ati Balwana Ram Ram Ratiyo Re ∣ Arji Hamari M…](https://www.youtube.com/watch?v=DJjel4bCD8A) | Studio Hariom | 1,180 | 2,587,078 | 2,192.4 | ×2,609.3 | 16,997.2 | 6.8분 | 2026-05-25 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 137/142 |
| 7 | [झूमका झूलनिया Slowed + Reverb ∣ KhesariLal Yadav ∣ Bhojpuri…](https://www.youtube.com/watch?v=UgjIqEE-Eok) | officialprince | 1,910 | 3,905,222 | 2,044.6 | ×781.0 | 51,591.1 | 4.5분 | 2026-08-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 327/335 |
| 8 | [Ye Tune Kya Kiya (Slowed + Reverb) 🎧 ∣ Lofi Version ∣ Once …](https://www.youtube.com/watch?v=jqVvhD8Bps4) | Vɪʙᴇ Bʏ Lᴏғɪ | 2,500 | 5,050,913 | 2,020.4 | ×4,146.9 | 56,720.1 | 4.8분 | 2026-07-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 363/369 |
| 9 | [Khat navajot Ahuja / BGM THE BEST SONG 🥰#viral](https://www.youtube.com/watch?v=KdCRd8wTjaA) | ANSHU FF 1M | 389 | 707,337 | 1,818.3 | ×5,569.6 | 5,280.0 | 4.9분 | 2026-06-12 | 기타 | 음악 | 없음 | 26/26 |
| 10 | [Tera Hua Sahiba](https://www.youtube.com/watch?v=43sXuUq5N08) | Garvit Soni -… | 1,440 | 2,522,011 | 1,751.4 | – | 22,908.4 | 4.7분 | 2026-07-06 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/75 |
| 11 | [DARKHAAST ❤️ ∣ Arijit Singh ∣ Slowed + Reverb ∣ LoFi Chill …](https://www.youtube.com/watch?v=DV1zd-C_Sms) | softtune 🎧 | 228 | 364,045 | 1,596.7 | ×551.6 | 5,335.6 | 6.9분 | 2026-08-17 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 18/19 |
| 12 | [그대 사랑하는사람 나였으면](https://www.youtube.com/watch?v=E0EJikB3jg4) | ㅠㅁㅠ | 217 | 342,169 | 1,576.8 | – | 5,524.4 | 27.9분 | 2026-08-23 | 기타 | 정보·해설 | 없음 | 79/92 |
| 13 | [[playlist] 일하다 어깨 들썩이는 케이팝 노동요 ∣∣ 4K MV](https://www.youtube.com/watch?v=whggKiGBSx4) | 노래듣는 고영희 | 2,530 | 3,967,128 | 1,568.0 | ×1,689.6 | 49,487.9 | 148.4분 | 2026-08-05 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 193/199 |
| 14 | [ℙ𝕝𝕒𝕪𝕃𝕚𝕤𝕥 : 늙크크들 원기 회복시킬 애니 플리](https://www.youtube.com/watch?v=RbGKWnzZ0zI) | 연하네의 쓸만한 플레이리… | 863 | 1,177,093 | 1,364.0 | ×1,113.6 | 18,416.0 | 124.7분 | 2026-08-21 | 기타 | 플레이리스트·모음 | 설명 | 348/361 |
| 15 | [JENNIE - FALLEN ANGEL (Official Video)](https://www.youtube.com/watch?v=s466YCiHfKw) | JennieRubyJan… | 25,000 | 32,734,639 | 1,309.4 | – | 572,744.8 | 5.7분 | 2026-08-28 | 10. 팝송·K팝·J팝 | 한 곡 | 설명 | 93,592/93,814 |
| 16 | [RAIM LAODE FULL ALBUM LAGU TERBAIK INDONESIA THE BEST MUSIC…](https://www.youtube.com/watch?v=plAW6z1Ex-w) | Playlist musi… | 2,380 | 3,111,492 | 1,307.3 | – | 25,583.4 | 18.2분 | 2026-06-24 | 기타 | 플레이리스트·모음 | 없음 | 306/318 |
| 17 | [Playlist for how a villain in love sounds like 🎧🔥✨.](https://www.youtube.com/watch?v=4NVS6d5eGyA) | Fictional Hea… | 3,290 | 4,300,581 | 1,307.2 | – | 73,004.9 | 9.7분 | 2026-08-26 | 기타 | 플레이리스트·모음 | 설명 | 324/336 |
| 18 | [When men loves you harder😭🌷](https://www.youtube.com/watch?v=2q4x4Ftz7mg) | wavy~ | 2,030 | 2,646,979 | 1,303.9 | ×197.7 | 66,513.1 | 9.3분 | 2026-09-14 | 기타 | 플레이리스트·모음 | 설명 | 487/538 |
| 19 | [Achhi lagti ho (slowed + reverb ) lofi varsion 🎧](https://www.youtube.com/watch?v=AMg46cfQH8A) | lofi song 45 | 1,540 | 2,001,041 | 1,299.4 | ×347.9 | 28,257.3 | 5.1분 | 2026-08-14 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 182/183 |
| 20 | [[Playlist] 코로나 전 오묘한 케이팝](https://www.youtube.com/watch?v=u7X8DqyBr64) | 원영 | 279 | 361,430 | 1,295.5 | – | 3,968.8 | 16.4분 | 2026-07-25 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 331/336 |
| 21 | [Deltarune Ch. 5: Egg Room (FULL VERSION)](https://www.youtube.com/watch?v=I0S5CyJoZpw) | Clowd | 1,180 | 1,509,474 | 1,279.2 | – | 12,599.0 | 7.6분 | 2026-06-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,544/1,576 |
| 22 | [uMoya 2.0 (Tycoon Remix)](https://www.youtube.com/watch?v=HropgeYirpE) | Darque - Topic | 1,330 | 1,697,005 | 1,275.9 | ×286.0 | 38,654.3 | 8.7분 | 2026-09-10 | 기타 | 음악 | 설명 | 0/378 |
| 23 | [Kalyani [slowed & Reverb] ∣∣ With Shreya Ghoshal ∣∣Arjn / K…](https://www.youtube.com/watch?v=rbt6SjoZlWU) | TRL Lofi | 3,880 | 4,815,089 | 1,241.0 | ×1,984.0 | 47,282.7 | 4.4분 | 2026-07-14 | 기타 | 음악 | 설명 | 156/158 |
| 24 | [Tum Ho Toh - Mashup 2026 ∣ Romantic Love Song ∣ Bollywood S…](https://www.youtube.com/watch?v=EmsrY9EQSSE) | VS Lofi Offic… | 2,230 | 2,754,032 | 1,235.0 | ×857.4 | 46,474.7 | 5.2분 | 2026-08-26 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 43/45 |
| 25 | [𝐑 𝐄 𝐙 𝐄](https://www.youtube.com/watch?v=mkRnOwNkpaQ) | iamkorean | 794 | 968,958 | 1,220.3 | – | 5,743.9 | 17분 | 2026-05-08 | 기타 | 음악 | 설명 | 211/214 |
| 26 | [Cigarettes After Sex — late night playlist](https://www.youtube.com/watch?v=G5SAO7jS8xk) | ahmet | 1,380 | 1,678,193 | 1,216.1 | ×408.3 | 27,210.3 | 55.8분 | 2026-08-23 | 기타 | 플레이리스트·모음 | 설명 | 180/202 |
| 27 | [어른여자.mp3](https://www.youtube.com/watch?v=Ir8CBRecz7g) | 리 세이 | 512 | 601,044 | 1,173.9 | ×1,602.8 | 3,643.9 | 16분 | 2026-05-12 | 기타 | 플레이리스트·모음 | 설명 | 83/84 |
| 28 | [별로 좋지 않은 하루를 보냈다고 생각할게](https://www.youtube.com/watch?v=wEwVgzsbqH4) | 니똥칼라똥 | 463 | 541,135 | 1,168.8 | – | 4,108.8 | 18.9분 | 2026-06-14 | 기타 | 플레이리스트·모음 | 없음 | 111/112 |
| 29 | [Hey Paaro - Full Song Bgm Raj The Show Man Puneeth Rajkumar…](https://www.youtube.com/watch?v=sj0JDjmC3es) | Mmusicworld46 | 332 | 372,471 | 1,121.9 | ×27.8 | 4,911.6 | 5.3분 | 2026-08-09 | 기타 | 음악 | 설명 | 7/7 |
| 30 | [[ 2024~2026 K-POP ] 최신곡 포함❗️ 랜덤 플레이 댄스 #랜덤플레이댄스 #kpop #2024…](https://www.youtube.com/watch?v=JnuZqf_O2N0) | 메이플 | 1,150 | 1,254,516 | 1,090.9 | – | 14,224.7 | 12.6분 | 2026-07-28 | 10. 팝송·K팝·J팝 | 한 곡 | 없음 | 86/93 |
| 31 | [3분 안에 잠드는 수면 음악 (30분) Fall Asleep in 3 Minutes (30 Min)](https://www.youtube.com/watch?v=E96njddrM5o) | 수면과학연구소 Sleep… | 89 | 108,479 | 1,084.8 | ×150.9 | 768.3 | 30분 | 2026-06-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/13 |
| 32 | [어 난데 여기 핫플이야](https://www.youtube.com/watch?v=JcIBpx-tGdA) | 햄 | 676 | 716,980 | 1,060.6 | ×1,236.2 | 4,272.8 | 24.1분 | 2026-05-09 | 기타 | 정보·해설 | 없음 | 84/84 |
| 33 | [Andekhi Anjaani si ∣ Slowed x Reverb ∣ lofi song ∣ lofi ver…](https://www.youtube.com/watch?v=FrqyfSyxOc4) | Midnight lofi… | 4,050 | 4,191,954 | 1,035.0 | ×786.3 | 80,832.5 | 6분 | 2026-09-02 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 132/133 |
| 34 | [THEN・❥・ Sweet Dreams ∣ Cinematic Techno](https://www.youtube.com/watch?v=0QAKKYJJ2l0) | THEN | 9,750 | 10,080,906 | 1,033.9 | ×2,352.3 | 73,239.3 | 4.4분 | 2026-06-08 | 기타 | 커버·직접 부른 노래 | 설명 | 491/497 |
| 35 | [🌙 Late Night Hindi Playlist ∣ Relax • Study • Sleep ∣ Mysti…](https://www.youtube.com/watch?v=1eFr1phNoxQ) | Mystic Scenery | 2,080 | 2,037,379 | 979.5 | ×34.5 | 26,230.6 | 25.2분 | 2026-08-07 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 74/74 |
| 36 | [🎧 Le Main Saiyaan Aa Gayi (Lofi) ∣ Mohabbatein ∣ Shah Rukh …](https://www.youtube.com/watch?v=NVf0GhbUmAw) | BOYS KING 99.… | 2,470 | 2,397,354 | 970.6 | ×657.3 | 25,707.5 | 7.5분 | 2026-07-23 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 175/175 |
| 37 | [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 사랑한다고 속삭여줘](https://www.youtube.com/watch?v=Tt_TimRh73Q) | 뜨신아아 | 1,100 | 1,056,441 | 960.4 | ×286.1 | 7,901.8 | 23.4분 | 2026-06-12 | 기타 | 플레이리스트·모음 | 설명 | 60/63 |
| 38 | [Toota Rahunga](https://www.youtube.com/watch?v=qN9Vw9v2nLY) | Garvit Soni -… | 1,440 | 1,355,168 | 941.1 | – | 14,288.3 | 4.1분 | 2026-07-21 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/48 |
| 39 | [POV You're back in the 90s 💗📻 ∣ Old hindi songs ∣ Bollywood…](https://www.youtube.com/watch?v=4GMIMevMn6Y) | Manii | 2,800 | 2,465,223 | 880.4 | ×65.0 | 40,708.2 | 8.2분 | 2026-08-24 | 기타 | 음악 | 설명 | 803/877 |
| 40 | [DANGRANGTO Playlist Hay Nhất ∣ Xương Rồng, Vùng Vẫy, Wrong …](https://www.youtube.com/watch?v=okmN02_PnaM) | hiệu ứng đám … | 1,660 | 1,411,331 | 850.2 | ×6.4 | 14,249.3 | 24.9분 | 2026-07-17 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 58/58 |
| 41 | [Top Hits Indonesia 2026 ∣ Top Hits Spotify Indonesia 2026 ∣…](https://www.youtube.com/watch?v=ANPUoFuWpEo) | ShadowBrief | 9,790 | 8,319,423 | 849.8 | – | 50,600.1 | 65분 | 2026-05-12 | 기타 | 정보·해설 | 설명 | 998/1,004 |
| 42 | [MOOD : FIRST LOVE { Desi playlist }](https://www.youtube.com/watch?v=zVH3YHdvXHY) | xukiyo | 3,310 | 2,748,889 | 830.5 | ×87.2 | 16,565.2 | 11.8분 | 2026-05-11 | 기타 | 플레이리스트·모음 | 없음 | 71/73 |
| 43 | [🎧 Le Main Saiyaan Aa Gayi (Lofi) ∣ Mohabbatein ∣ Shah Rukh …](https://www.youtube.com/watch?v=iOdAwvF0kmk) | lofi.slowed_02 | 5,670 | 4,633,361 | 817.2 | ×904.1 | 47,724.5 | 7.5분 | 2026-07-19 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 291/296 |
| 44 | [Tera Sang Yaara - Slowed Reverb ∣∣ Atif Aslam ∣∣ Dopohor Lo…](https://www.youtube.com/watch?v=QcR63bT06iE) | Dopohor Lofi | 3,430 | 2,799,134 | 816.1 | ×236.0 | 64,029.3 | 5분 | 2026-09-10 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 219/227 |
| 45 | [Baddies playlist🫦💋](https://www.youtube.com/watch?v=iwtL-agF0LQ) | Music-cholic | 1,350 | 1,092,178 | 809.0 | – | 7,259.7 | 18.9분 | 2026-05-26 | 기타 | 플레이리스트·모음 | 설명 | 56/57 |
| 46 | [Hanuman Chalisa ∣ Peaceful & Divine ∣ Powerful Bhajan for P…](https://www.youtube.com/watch?v=pmQtkBTtzLw) | Shri Music St… | 1,410 | 1,128,647 | 800.5 | ×1,628.6 | 6,558.7 | 6.4분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 601/615 |
| 47 | [Những Bản Nhạc LoFi Chill Hay Nhất 2026 ∣ TikTok Viral Triệ…](https://www.youtube.com/watch?v=4vl5hS0oXH0) | Kvyzz Music | 1,260 | 1,000,057 | 793.7 | – | 11,063.3 | 26.1분 | 2026-07-25 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 185/189 |
| 48 | [Tu Chahiye [lyrics] Atif Aslam](https://www.youtube.com/watch?v=AJ0KTHkTGYA) | Chill Beats H… | 1,950 | 1,526,113 | 782.6 | ×396.0 | 23,194.0 | 4.5분 | 2026-08-19 | 기타 | 한 곡 | 설명 | 74/74 |
| 49 | [[Playlist Tâm Trạng]#1 - Xương Rồng, Vết Thương, Tìm Em, Ng…](https://www.youtube.com/watch?v=DcZ75tBPfa4) | Cà Chuaa | 2,410 | 1,758,535 | 729.7 | ×74.3 | 19,612.9 | 15.5분 | 2026-07-26 | 기타 | 플레이리스트·모음 | 설명 | 344/351 |
| 50 | [MKAstro – Darkness Chill ∣ Club Banger Trap ∣ (Visualizer)](https://www.youtube.com/watch?v=emsqrCS0yiw) | MKAstro Studio | 3,570 | 2,548,242 | 713.8 | ×3,179.3 | 22,161.1 | 5.8분 | 2026-07-01 | 8. 로파이·시티팝·칠 | AI 음악 | 설명 | 154/165 |
| 51 | [7 मिनट में बच्चा गहरी नींद सोए🌙 सो जा मेरे चाँद से लाल ∣ Hi…](https://www.youtube.com/watch?v=IxnmH8QjS_A) | deep sleep vi… | 898 | 639,030 | 711.6 | ×11,017.8 | 3,929.5 | 6.8분 | 2026-05-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 152/156 |
| 52 | [POV: You Own The Dance Floor💃🏻🪩✨ ∣∣Song Playlist+ Timestamp…](https://www.youtube.com/watch?v=HRGB0HnXdOs) | Author_Shreyuu | 6,480 | 4,600,213 | 709.9 | – | 30,238.1 | 8분 | 2026-05-25 | 기타 | 플레이리스트·모음 | 설명 | 617/625 |
| 53 | [𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 가을 설레발 플리](https://www.youtube.com/watch?v=ams0ZufCafU) | 또잉 | 392 | 278,139 | 709.5 | ×821.7 | 4,900.5 | 19.6분 | 2026-08-28 | 기타 | 플레이리스트·모음 | 없음 | 17/20 |
| 54 | [Hanuman Chalisa Sleep Version 🕉️ ∣ Sleep In 5 Minutes 😴 ∣ S…](https://www.youtube.com/watch?v=RgmRMA0Bs34) | Ananta Rhythm | 4,670 | 3,240,435 | 693.9 | ×6,062.6 | 19,603.4 | 7.1분 | 2026-05-12 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,523/1,545 |
| 55 | [Steve Lacy - the feeling (Official Video)](https://www.youtube.com/watch?v=Qw20tg1v7Fc) | SteveLacyVEVO | 8,430 | 5,786,837 | 686.5 | – | 40,996.6 | 4.6분 | 2026-06-05 | 기타 | 플레이리스트·모음 | 설명 | 5,393/5,417 |
| 56 | [Barsaat 🌧️ ∣ All Trending Songs 🎧∣ Taare x Samjho Na x Safa…](https://www.youtube.com/watch?v=xGPm2j1dDr4) | LOFI XP VIBES | 2,900 | 1,990,035 | 686.2 | ×260.2 | 46,582.9 | 23분 | 2026-09-11 | 기타 | 음악 | 설명 | 193/207 |
| 57 | ['pov: bạn mở lại một tab ký ức năm 2018 ♪♪](https://www.youtube.com/watch?v=8ljpWVIINTs) | chalye | 2,330 | 1,594,199 | 684.2 | ×135.6 | 11,765.1 | 27.4분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 설명 | 331/336 |
| 58 | [Pov: certified Baddie playlist 🔥# playlist # baddie](https://www.youtube.com/watch?v=vzNOiBV_W6g) | it's GAURAV P… | 7,970 | 5,448,963 | 683.7 | – | 42,185.7 | 8.3분 | 2026-06-17 | 기타 | 플레이리스트·모음 | 설명 | 696/706 |
| 59 | [Mind Relax Lofi Mashup ∣ Mind Relaxing Songs ∣ Mind Relax L…](https://www.youtube.com/watch?v=JyM_L7ZZ9xw) | SONGS ZONE | 3,000 | 2,033,785 | 677.9 | – | 13,974.3 | 28.7분 | 2026-05-31 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 357/365 |
| 60 | [Tere Liye [Slowed+Reverb+Lofi] Song ∣ Atif Aslam, Shreya Gh…](https://www.youtube.com/watch?v=zwDQAObOpx4) | DK LOFI | 3,990 | 2,695,645 | 675.6 | ×459.1 | 27,159.6 | 4.5분 | 2026-07-17 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 415/459 |
| 61 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=XLtdtHJExEY) | Clsxzff | 1,860 | 1,246,823 | 670.3 | – | 37,967.5 | 19.6분 | 2026-09-21 | 1. 수면·명상·힐링 | 음악 | 설명 | 173/187 |
| 62 | [Darmiyaan](https://www.youtube.com/watch?v=v2TsWj3wxHM) | Rekha Bhardwa… | 8,590 | 5,651,106 | 657.9 | – | 58,856.0 | 4.5분 | 2026-07-20 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/239 |
| 63 | [Twinkle Twinkle - Best Lullabies for Babies To Sleep ∣ Litt…](https://www.youtube.com/watch?v=PE3jMxJjyB0) | KiddoBeatz | 850 | 557,796 | 656.2 | ×676.1 | 3,237.0 | 10.7분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 64 | [Hangova (From "DC")](https://www.youtube.com/watch?v=B6ppp6WBCKg) | Anirudh Ravic… | 31,700 | 20,510,948 | 647.0 | ×1,575.7 | 186,727.9 | 4.1분 | 2026-07-06 | 기타 | 정보·해설 | 설명 | 0/1,473 |
| 65 | [Achchi Lagti Ho (Slowed + Reverb) ∣ Lofi Version 🎧](https://www.youtube.com/watch?v=fc8Mab9zGkg) | GTAvexo9 | 24,100 | 15,553,534 | 645.4 | – | 159,204.1 | 6.5분 | 2026-07-18 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 2,047/2,141 |
| 66 | [Mann mera (Original Version) ∣ Slowed + Reverb ∣ Gajendra V…](https://www.youtube.com/watch?v=4ObYNh1TOHY) | LOFI ZONE 990K | 16,900 | 10,547,075 | 624.1 | ×1,464.1 | 118,286.2 | 5분 | 2026-07-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,591/1,648 |
| 67 | [Playlist Song Inggris Gamon Santai...∣∣ The Winner Takes It…](https://www.youtube.com/watch?v=E9Nm4xOU-tk) | musik gen z | 1,990 | 1,241,132 | 623.7 | ×104.0 | 13,939.4 | 31.1분 | 2026-07-27 | 기타 | 플레이리스트·모음 | 설명 | 467/487 |
| 68 | [Om Namah Shivaya 🕉 #hanumanansh #backgroundmusic #trendings…](https://www.youtube.com/watch?v=YnhFtBGO2zI) | Rudree Aarya … | 2,500 | 1,554,595 | 621.8 | – | 32,704.3 | 15.5분 | 2026-09-06 | 기타 | 음악 | 없음 | 385/387 |
| 69 | [Heartbreak Chillout ∣ Vishal Mishra ∣ Arijit singh ∣ Soulfu…](https://www.youtube.com/watch?v=XlYh9K0UNXI) | Nilay Kumar M… | 2,400 | 1,492,190 | 621.8 | ×18,888.5 | 8,686.4 | 8분 | 2026-05-05 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 137/138 |
| 70 | [POV: You are ✨ Self Obsessed women💅 Playlist hindi bollywood](https://www.youtube.com/watch?v=wOy_aMJqDgo) | 𝐌𝐫. | 2,780 | 1,715,715 | 617.2 | ×1,415.6 | 15,326.0 | 14.4분 | 2026-07-04 | 기타 | 플레이리스트·모음 | 설명 | 841/839 |
| 71 | [[𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 띵곡들만 모아놓은 애니 노동요 OST 플리💿](https://www.youtube.com/watch?v=16zIXIea0_U) | ASMRuru_루루 | 909 | 560,698 | 616.8 | ×892.8 | 4,090.0 | 54.4분 | 2026-06-09 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 91/93 |
| 72 | [Premada Oorali Kannada LO-FI Song By Nitro plus kannada](https://www.youtube.com/watch?v=LEqTIHGB7_g) | NITRO PLUS KA… | 4,530 | 2,783,486 | 614.5 | ×20,928.5 | 25,951.3 | 11.5분 | 2026-07-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 240/250 |
| 73 | [POV: you discovered that ✨South Indian and Hindi ✨songs hit…](https://www.youtube.com/watch?v=lbT4VY3UKkY) | Arena | 3,950 | 2,372,915 | 600.7 | ×348.2 | 33,970.7 | 14.6분 | 2026-08-15 | 12. 커버·노래 부르기 | 음악 | 설명 | 406/438 |
| 74 | [𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 느좋 인스타 감성](https://www.youtube.com/watch?v=RG-8iv6ORFY) | 알수없는 사용자 | 1,810 | 1,077,782 | 595.5 | ×29.8 | 14,741.7 | 27분 | 2026-08-12 | 기타 | 플레이리스트·모음 | 설명 | 94/100 |
| 75 | [Peace of Mind : Sufi Bollywood Nonstop ∣ Rahat Fateh Ali Kh…](https://www.youtube.com/watch?v=RlyVCMHCuqc) | Aures Music S… | 3,800 | 2,246,184 | 591.1 | ×4,370.0 | 27,121.1 | 57.1분 | 2026-08-02 | 기타 | 음악 | 설명 | 124/124 |
| 76 | [Old Punjabi Bangers ∣ Punjabi Hits Playlist ∣ Still Cookin](https://www.youtube.com/watch?v=rJgcNE-7emM) | STILL COOKIN | 3,530 | 2,086,389 | 591.0 | – | 19,426.2 | 14.1분 | 2026-07-08 | 기타 | 플레이리스트·모음 | 설명 | 107/118 |
| 77 | [You’ll Sleep Like a Child in Hanuman’s Protection ∣ Soft Ha…](https://www.youtube.com/watch?v=oSeh-sXFCTM) | Sanatan Jug | 5,540 | 3,259,673 | 588.4 | ×9,105.2 | 19,082.4 | 111.6분 | 2026-05-06 | 1. 수면·명상·힐링 | 한 곡 | 설명 | 399/420 |
| 78 | [DUDE 30 Min Loop 🎧 ∣ Orchestral Suite • Metro Proposal • Pl…](https://www.youtube.com/watch?v=rNkUDAFaFbM) | Zontyx | 1,900 | 1,111,550 | 585.0 | ×6,297.7 | 7,371.5 | 29.7분 | 2026-05-26 | 기타 | 긴 한 곡·반복 | 설명 | 974/1,003 |
| 79 | [이게 삶이더라고｜세월 끝에 깨닫는 인생 이야기｜감성 발라드](https://www.youtube.com/watch?v=QalAq2cvw8U) | 웃음콘서트TV | 3,040 | 1,770,665 | 582.5 | ×520.9 | 11,473.9 | 5.4분 | 2026-05-23 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 334/357 |
| 80 | [DESI PUNJABI PLAYLIST THAT GETS YOUR VIBE 😌🎧](https://www.youtube.com/watch?v=JQ922u24pH8) | Your April | 3,290 | 1,833,093 | 557.2 | ×116.0 | 12,197.6 | 11.4분 | 2026-05-27 | 기타 | 플레이리스트·모음 | 설명 | 393/400 |
| 81 | [Overthinking? Listen To This Krishna Flute Music & Stop Wor…](https://www.youtube.com/watch?v=Pckh0r0bGAM) | Dhwani | 1,440 | 802,001 | 557.0 | – | 5,905.8 | 8분 | 2026-06-10 | 기타 | 음악 | 설명 | 134/138 |
| 82 | [Phonk/funk playlist bcz I’m bored (Timestaps)](https://www.youtube.com/watch?v=8AXBNw3EGu8) | 1vy_x | 5,350 | 2,951,188 | 551.6 | ×21.7 | 19,096.1 | 9.8분 | 2026-05-22 | 기타 | 플레이리스트·모음 | 설명 | 304/309 |
| 83 | [Sanson Ki Mala Pe (Slowed & Emotional Version) ∣ Hindi Love…](https://www.youtube.com/watch?v=7y_L2sW-3J4) | Karela Records | 4,360 | 2,384,482 | 546.9 | ×2,045.9 | 17,000.7 | 7.3분 | 2026-06-06 | 기타 | 음악 | 설명 | 92/92 |
| 84 | [✨️𝐬𝐨𝐧𝐠𝐬 𝐭𝐡𝐚𝐭 𝐦𝐚𝐤𝐞 𝐥𝐢𝐟𝐞 𝐟𝐞𝐞𝐥 𝐥𝐢𝐤𝐞 𝐚 𝐥𝐨𝐯𝐞 𝐬𝐭𝐨𝐫𝐲 ∣ aesthetic h…](https://www.youtube.com/watch?v=GMF0FN2nrBw) | Echoess of un… | 6,270 | 3,317,281 | 529.1 | ×19.3 | 23,077.2 | 18.6분 | 2026-06-02 | 기타 | 플레이리스트·모음 | 설명 | 409/408 |
| 85 | [धनियां बनबू कनियाँ - Lofi Song ∣∣ Khesari Lal Yadav ∣∣ Dilw…](https://www.youtube.com/watch?v=s-1MerBYomA) | ꧁༒乙x°᭄Ᏼᴀʙᴜ࿐ | 3,840 | 2,029,933 | 528.6 | ×353.8 | 34,232.0 | 5.1분 | 2026-08-26 | 8. 로파이·시티팝·칠 | 음악 | 없음 | 267/296 |
| 86 | [Me Sunti Rahu 💭🎶 ∣ Heart Touching Lofi Song (Slowed + Rever…](https://www.youtube.com/watch?v=TKMu6Wg396c) | 𝕃𝕠𝕤𝕥_𝕗𝕖𝕖𝕝𝕚𝕟𝕘𝕤… | 4,620 | 2,431,234 | 526.2 | ×654.5 | 16,907.1 | 5.7분 | 2026-06-02 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 389/392 |
| 87 | [🍂 가을이 오면 생각나는 노래 ∣ 커피 한 잔과 함께 듣는 가을 감성 플레이리스트 ☕](https://www.youtube.com/watch?v=Fc7JJxJBgJA) | enuscento-에뉴센토 | 810 | 424,923 | 524.6 | ×1,212.3 | 8,345.1 | 114.3분 | 2026-09-03 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 62/71 |
| 88 | [Ankhiyon Ke Jharokhon Se ∣ Soft Classic Instrumental 🎶 ∣ Ol…](https://www.youtube.com/watch?v=KCgBk52MuY8) | Saaz-e-Dil | 1,930 | 1,010,216 | 523.4 | ×366.7 | 7,667.9 | 4.5분 | 2026-06-14 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 127/128 |
| 89 | [If you want to dance...🩰✨watch this playlist💃❣️ #bollywood …](https://www.youtube.com/watch?v=x0br2Hc-4G8) | LyricVibes~ | 6,130 | 3,190,923 | 520.5 | – | 21,144.7 | 24.4분 | 2026-05-26 | 기타 | 플레이리스트·모음 | 설명 | 380/390 |
| 90 | [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 그리고 난 다시 사랑에 빠질수 밖에 없었어](https://www.youtube.com/watch?v=cIlJK2Pfhm8) | 느좋을 추구합니다 | 1,070 | 555,098 | 518.8 | – | 8,821.4 | 18.1분 | 2026-08-22 | 기타 | 플레이리스트·모음 | 없음 | 177/183 |
| 91 | [Ishq x Pal Pal Endless Mashup (Slowed + Reverb) - Afusic x …](https://www.youtube.com/watch?v=h231qlqI-dg) | Lost In Lyrics | 1,090 | 562,361 | 515.9 | ×148.5 | 5,314.3 | 27.6분 | 2026-07-10 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 109/109 |
| 92 | [💋 A Chatpati Playlist Only For Chatpata People 😋✨ ∣ Ultimat…](https://www.youtube.com/watch?v=3FhXwFGVaDE) | JellyBloxify | 34,000 | 17,475,309 | 514.0 | ×9,834.2 | 124,741.1 | 7.5분 | 2026-06-06 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 2,208/2,242 |
| 93 | [Autumn Fireplace Jazz ∣ Cozy Crackling Fire Ambience](https://www.youtube.com/watch?v=q87NJ-696WM) | Midnight Fika | 4,790 | 2,456,191 | 512.8 | ×3,727.1 | 60,290.8 | 129.6분 | 2026-09-13 | 2. 자연 소리·백색소음 | 음악 | 설명 | 207/224 |
| 94 | [𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩 slavic](https://www.youtube.com/watch?v=49A1aj-uIcs) | aa | 1,730 | 884,002 | 511.0 | ×332.0 | 8,527.4 | 16.8분 | 2026-07-12 | 기타 | 플레이리스트·모음 | 설명 | 191/207 |
| 95 | [Parindey (Slowed + Reverb) ∣ Haryanvi Lofi Song 🎧 Chill Vib…](https://www.youtube.com/watch?v=v8CKkI20B2s) | AS LO-FI Musi… | 3,740 | 1,909,594 | 510.6 | ×741.9 | 10,712.5 | 4.1분 | 2026-04-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 150/150 |
| 96 | [○ Bollywood navratri song playlist ○ #navratri #garbasongs …](https://www.youtube.com/watch?v=g9nj1SDsXng) | july_luna | 5,480 | 2,738,151 | 499.7 | ×104.4 | 81,531.8 | 18.9분 | 2026-09-20 | 기타 | 플레이리스트·모음 | 없음 | 102/129 |
| 97 | [Barsaat 🌧️∣ All Trending Songs ∣ Taare x Samjho Na x Safar …](https://www.youtube.com/watch?v=41HX_5G6eqQ) | Voxwaves | 17,500 | 8,655,656 | 494.6 | ×461.7 | 183,157.4 | 22.9분 | 2026-09-07 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,062/1,197 |
| 98 | [I'm Tired Of Loving You - Golden Lace Ballads ∣ Classic Cou…](https://www.youtube.com/watch?v=URrqbWhzzMU) | Golden Lace B… | 3,200 | 1,580,999 | 494.1 | ×1,515.1 | 10,342.0 | 5.8분 | 2026-05-24 | 기타 | 한 곡 | 설명 | 361/368 |
| 99 | [Baddie playlist 💋✨Aura+99999∣ SanviEditz #songplaylist](https://www.youtube.com/watch?v=p8u1URNm4ao) | ♡𝑺𝒂𝒏𝒗𝒊𝑬𝒅𝒊𝒕𝒛♡ | 5,550 | 2,720,745 | 490.2 | – | 56,728.9 | 8.1분 | 2026-09-06 | 기타 | 플레이리스트·모음 | 없음 | 2,195/2,367 |
| 100 | [THE WEEKND ∣ Late Night Drive Playlist](https://www.youtube.com/watch?v=DgBM12cGM-Q) | Jostynsc | 11,100 | 5,348,191 | 481.8 | ×20.6 | 43,028.0 | 40.8분 | 2026-06-22 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 304/338 |
| 101 | [✨Best Bollywood LoFi Mashup 2026 🌙✨ lofi song](https://www.youtube.com/watch?v=ohHqAaHYlLI) | Soul Beats | 4,820 | 2,308,956 | 479.0 | ×1,056.7 | 22,483.3 | 25.8분 | 2026-07-13 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 122/122 |
| 102 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 nên nghe gì khi gió Thu tràn về? 🍂📻 Playlist Nhạc …](https://www.youtube.com/watch?v=Pg39V_-aNPY) | chill out | 4,530 | 2,159,722 | 476.8 | ×60.2 | 63,677.0 | 83.5분 | 2026-09-20 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 236/269 |
| 103 | [[ 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ] 적당히 신나는 그루브 힙합 플레이리스트 ∣ Chill R&B • Cafe Music](https://www.youtube.com/watch?v=p3tvSF3BgYM) | SSoundW | 4,020 | 1,914,311 | 476.2 | ×512.9 | 30,010.2 | 89.9분 | 2026-08-21 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 253/253 |
| 104 | [Devik - Muje tumse x tu tu hai wahi DJ remix (BGM) music 🎶 …](https://www.youtube.com/watch?v=FPuJuLyZmJI) | Newworldbeats… | 796 | 377,184 | 473.9 | – | 7,096.2 | 9.7분 | 2026-09-01 | 기타 | 음악 | 설명 | 137/138 |
| 105 | [Mind relaxing lofi song Arijit Singh ∣ Soft songs ∣ Arijit …](https://www.youtube.com/watch?v=43y5rT7YjQY) | Y Music 2 | 36,800 | 17,406,323 | 473.0 | – | 119,984.7 | 27.9분 | 2026-06-01 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,372/1,403 |
| 106 | [GTA 6 Raul Batista Mission Theme Music - Clean Audio - Exte…](https://www.youtube.com/watch?v=Lu2v0EWc0-0) | GAMING Benchm… | 1,390 | 654,084 | 470.6 | ×4,993.0 | 11,524.1 | 5.3분 | 2026-08-28 | 기타 | 음악 | 설명 | 864/881 |
| 107 | [Relaxing Jazz Café in Paris ∣ Rainy Evening Jazz Ambience w…](https://www.youtube.com/watch?v=eR37WB9IE9E) | European Jazz… | 1,630 | 745,623 | 457.4 | ×1,281.1 | 5,395.8 | 14.4분 | 2026-06-08 | 2. 자연 소리·백색소음 | 음악 | 설명 | 24/27 |
| 108 | [[𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 저 정말 바라는 거 없어요](https://www.youtube.com/watch?v=ZUW47tZkwkg) | 음악저장소 | 2,050 | 936,588 | 456.9 | ×59.9 | 27,727.0 | 27.3분 | 2026-09-20 | 기타 | 플레이리스트·모음 | 없음 | 88/93 |
| 109 | [𓍢ִ໋🌾 chatpate punjabi bangers](https://www.youtube.com/watch?v=neQ8CUHH7WQ) | b࣪ ִֶָ☾. | 6,950 | 3,151,031 | 453.4 | – | 22,505.3 | 12.2분 | 2026-06-06 | 기타 | 플레이리스트·모음 | 설명 | 277/282 |
| 110 | [🎶Spotify Hits Music 2026 ∣∣ Top Music Playlist -- Best 100 …](https://www.youtube.com/watch?v=0gvy7v6GTMo) | Soft Feelings | 6,250 | 2,831,710 | 453.1 | ×187.7 | 39,397.0 | 138.6분 | 2026-08-13 | 기타 | 플레이리스트·모음 | 설명 | 188/197 |
| 111 | [🎀Students fav playlist👀 ∣next comment∣](https://www.youtube.com/watch?v=yx9rhLzbY0A) | @vibe_withe_me | 5,660 | 2,556,375 | 451.7 | ×400.7 | 33,692.5 | 7분 | 2026-08-09 | 기타 | 플레이리스트·모음 | 없음 | 1,169/1,207 |
| 112 | [Idea 22 - Depressed in 448Hz (Cello cry & Piano & slow) @Gi…](https://www.youtube.com/watch?v=zMMuayoF_o4) | WORRIES | 430 | 192,696 | 448.1 | ×129.5 | 2,206.0 | 12.9분 | 2026-07-28 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 116/116 |
| 113 | [One playlist. A thousand imaginary love stories. ❤️](https://www.youtube.com/watch?v=aIYTT2ihwvM) | soul wali vib… | 2,490 | 1,114,330 | 447.5 | ×101.4 | 18,385.9 | 22.1분 | 2026-08-24 | 기타 | 플레이리스트·모음 | 없음 | 354/359 |
| 114 | [모르는 노래 없는!! 2026 랜덤플레이댄스🍋 ∣ 랜플댄 ∣ 랜플💫 ∣ 모르는 노래 없는 랜플댄🩷 ∣ 케이…](https://www.youtube.com/watch?v=tAJM1fttdG0) | 바나나한 바냐 | 579 | 257,302 | 444.4 | – | 3,558.1 | 5.1분 | 2026-08-13 | 10. 팝송·K팝·J팝 | 음악 | 없음 | 36/37 |
| 115 | [कर्पूरगौरं करुणावतारं ∣ Shiva Lingam Divine Prayer ∣ Karpur…](https://www.youtube.com/watch?v=5I7pQfjbUHo) | Darshan Dhara | 4,020 | 1,785,989 | 444.3 | ×1,374.9 | 10,725.0 | 8.4분 | 2026-05-10 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 139/139 |
| 116 | ["𝐖𝐞 𝐚𝐫𝐞 𝐣𝐮𝐬𝐭 𝐟𝐫𝐢𝐞𝐧𝐝𝐬... 𝐑𝐢𝐠𝐡𝐭.?"/ 𝐀 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐟𝐨𝐫 𝐬𝐨𝐦𝐞𝐨𝐧𝐞 𝐲𝐨…](https://www.youtube.com/watch?v=A_yQZns_YGk) | 𝗩𝗮𝗺𝗽𝗶𝗿𝗲 𓂃⋆.˚ | 2,410 | 1,060,291 | 439.9 | ×42.3 | 9,923.2 | 20.4분 | 2026-07-09 | 기타 | 플레이리스트·모음 | 설명 | 610/613 |
| 117 | [[Playlist] When music is all you need](https://www.youtube.com/watch?v=XXKXpf7xFC4) | encore. | 7,210 | 3,168,321 | 439.4 | ×262.8 | 93,278.5 | 20.9분 | 2026-09-20 | 기타 | 플레이리스트·모음 | 설명 | 518/715 |
| 118 | [Michael Jackson Greatest Hits Mix ∣ Celebrating MICHAEL (20…](https://www.youtube.com/watch?v=F2-83E_iNb4) | IONEMusic | 11,100 | 4,869,963 | 438.7 | ×4,236.6 | 46,122.7 | 94.5분 | 2026-07-10 | 기타 | 음악 | 설명 | 1,177/1,203 |
| 119 | [🌊 여름에 듣기 좋은 노래☀️ 하루 종일 듣기 좋은 여름 플레이리스트 🌴 바다로 떠나고 싶어지는 여름 노래…](https://www.youtube.com/watch?v=L-pbTsp8AH8) | 마음선곡 | 844 | 368,453 | 436.6 | ×404.4 | 2,523.8 | 119분 | 2026-05-31 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 67/67 |
| 120 | [Pov :- Bhojpuri playlist 🔥 ∣∣ chill guys and enjoy 😎∣∣ Ansh…](https://www.youtube.com/watch?v=4mnrtxd_GhE) | Anshika | 20,300 | 8,819,776 | 434.5 | ×62.9 | 109,287.9 | 11.6분 | 2026-08-04 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,684/1,725 |
| 121 | [katseye (clean) playlist ⊹ ࣪ ˖](https://www.youtube.com/watch?v=_VEtnBXtUNs) | 𝟑𝟎𝟑.𝐧𝐞𝐰.𝐞𝐫𝐚 | 7,800 | 3,382,569 | 433.7 | – | 40,177.2 | 25.3분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 설명 | 2,599/2,611 |
| 122 | [One Playlist. Endless Feelings. ∣ Soft Love Songs for Late …](https://www.youtube.com/watch?v=Auvd4NPXHnI) | Unrequited Lo… | 5,750 | 2,488,796 | 432.8 | – | 22,866.9 | 23.2분 | 2026-07-07 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 436/437 |
| 123 | [𝑮𝒐𝒍𝒅𝒆𝒏 𝑩𝒓𝒐𝒘𝒏 - 𝑻𝒉𝒆 𝑺𝒕𝒓𝒂𝒏𝒈𝒍𝒆𝒓𝒔 ∣ ⚔︎ 𝑩𝒆𝒔𝒕 𝒑𝒂𝒓𝒕 𝒍𝒐𝒐𝒑𝒆𝒅 ⚔︎](https://www.youtube.com/watch?v=9MLxTIPaoTQ) | Medieval Anem… | 2,410 | 1,042,206 | 432.4 | ×2,316.0 | 13,457.2 | 11.8분 | 2026-08-07 | 기타 | 정보·해설 | 설명 | 417/423 |
| 124 | [Top Bhojpuri Hits Mix 2026 ∣ Nonstop Bhojpuri Mashup 🎧🔥](https://www.youtube.com/watch?v=7v8NIUwR1No) | Anivix | 6,320 | 2,717,465 | 430.0 | ×1,125.5 | 24,127.4 | 6분 | 2026-07-03 | 기타 | 음악 | 설명 | 483/497 |
| 125 | [Stay With Me Now..](https://www.youtube.com/watch?v=mT2U96LfO3g) | AERIN - Proje… | 571 | 244,799 | 428.7 | ×1,419.1 | 1,504.9 | 4.6분 | 2026-05-14 | 기타 | 음악 | 설명 | 31/31 |
| 126 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Chi…](https://www.youtube.com/watch?v=ki362-gbdjs) | Qais Music St… | 2,170 | 922,906 | 425.3 | ×3,605.1 | 38,650.9 | 7.3분 | 2026-09-30 | 3. 공부·집중·작업 | 음악 | 설명 | 10/10 |
| 127 | [Playlist cuz you're in love 💌#playlist #love #2026](https://www.youtube.com/watch?v=gbf3ZYx6EbU) | it's GAURAV P… | 7,970 | 3,309,446 | 415.2 | – | 19,826.8 | 10.6분 | 2026-05-10 | 기타 | 플레이리스트·모음 | 설명 | 531/529 |
| 128 | [Dance playlist for chatpati girls 🥂💅🏻🍷#dance #viral#trendin…](https://www.youtube.com/watch?v=wh1wOQrBIrk) | soft girl 🦋💫 | 4,100 | 1,694,028 | 413.2 | ×83.8 | 12,490.1 | 8.5분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 없음 | 110/110 |
| 129 | [CHILL NIGHT MOOD🌙 R&B Mix Playlist ∣ Late Night Vibes, Rela…](https://www.youtube.com/watch?v=zA04SiNiLYk) | Late Night Rn… | 2,610 | 1,075,786 | 412.2 | – | 6,418.4 | 158.2분 | 2026-05-09 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 54/54 |
| 130 | [🍂 알록달록 가을 음악이야기 ∣ Autumn Collection Vol.](https://www.youtube.com/watch?v=o3DojrmPMbs) | little step m… | 85 | 40,965 | 409.6 | ×53.3 | 1,775.3 | 206.4분 | 2026-10-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 3/3 |
| 131 | [Viral Songs Playlist 2026 ∣ Barsaat, Sheesha, Parvati, Roots](https://www.youtube.com/watch?v=nmc4ScFV3j4) | Vijay Garje | 3,540 | 1,441,984 | 407.3 | ×12,760.9 | 72,828.6 | 31.3분 | 2026-10-04 | 기타 | 플레이리스트·모음 | 설명 | 320/439 |
| 132 | [[Playlist] Music is my drug](https://www.youtube.com/watch?v=msoR3EhPNAA) | Hugs | 6,660 | 2,700,334 | 405.5 | – | 53,319.6 | 20.9분 | 2026-09-03 | 기타 | 플레이리스트·모음 | 설명 | 538/541 |
| 133 | [𝙅 𝙋𝙤𝙥 𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩 저기, 나 지금 사랑에 빠지고 있어](https://www.youtube.com/watch?v=-_t34PClPSE) | 이로하 | 1,890 | 765,128 | 404.8 | – | 4,852.0 | 20.9분 | 2026-05-19 | 기타 | 플레이리스트·모음 | 설명 | 165/168 |
| 134 | [Attract Peace & Positive Energy ∣ Raag Malhar Morning Medit…](https://www.youtube.com/watch?v=c45OwnC599Y) | Tatva Meditat… | 215 | 86,802 | 403.7 | ×729.4 | 601.5 | 15분 | 2026-06-02 | 1. 수면·명상·힐링 | 음악 | 설명 | 9/9 |
| 135 | [Throwback R&B Classics 📺 Chris Brown, Rihanna, Akon, Usher,…](https://www.youtube.com/watch?v=gCUbxsTWZ18) | R&B Afterglow | 15,500 | 6,177,435 | 398.5 | ×4,730.0 | 62,459.0 | 193.5분 | 2026-07-17 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 698/762 |
| 136 | [2026 최신곡 랜덤플레이댄스∣ K-pop Random Play Dance 2026 #랜덤플레이댄스 #랜플…](https://www.youtube.com/watch?v=bliX1fxHkKk) | 샤파 | 909 | 362,228 | 398.5 | ×3.4 | 17,268.5 | 6.1분 | 2026-10-03 | 10. 팝송·K팝·J팝 | 한 곡 | 설명 | 46/48 |
| 137 | [/KATSEYE PLAYLIST💫/ All Songs In One Video / ICONIC BY MIST…](https://www.youtube.com/watch?v=wQHy50dFnfY) | 𝓔𝓵𝓵𝓲𝔁𝔁𝓺 🤍🎀 | 2,640 | 1,051,488 | 398.3 | – | 8,935.8 | 43분 | 2026-06-28 | 기타 | 플레이리스트·모음 | 설명 | 950/950 |
| 138 | [[playlist] 잔잔한 안건호 보컬 모음 플레이리스트 ∣ 커버곡 ∣ 코르티스](https://www.youtube.com/watch?v=WHHQaKlBtZk) | W | 24 | 39,548 | 395.5 | – | 242.9 | 13.3분 | 2026-05-14 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 12/12 |
| 139 | [Heartbreaking 💔 Lofi Mashup 🎧Slowed + Reverb Songs ∣ Relax,…](https://www.youtube.com/watch?v=gCuJrBYRJpM) | Fiaz Baloch O… | 7,170 | 2,818,580 | 393.1 | ×5,598.0 | 58,452.9 | 8분 | 2026-09-06 | 3. 공부·집중·작업 | 음악 | 설명 | 154/156 |
| 140 | [Barsaat ∣ All Trending Hindi Songs 2026 ∣ Safar × Bairan × …](https://www.youtube.com/watch?v=-hXkiB-eLfs) | SukumusicHindi | 3,390 | 1,329,356 | 392.1 | ×969.6 | 30,385.4 | 22.9분 | 2026-09-10 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 161/165 |
| 141 | [ALL TRENDING HINDI SONGS 2026...PLAYLIST #asthetic #trend #…](https://www.youtube.com/watch?v=xI0IEWIxUBQ) | Rb Lofi | 27,000 | 10,422,745 | 386.0 | ×1,153.7 | 168,182.4 | 7.9분 | 2026-08-23 | 기타 | 플레이리스트·모음 | 없음 | 1,565/1,716 |
| 142 | ["some aesthetic desi song's you'll absolutely love"🌊✨😭//par…](https://www.youtube.com/watch?v=6D1sq3Y-hB0) | Anushri | 7,570 | 2,905,241 | 383.8 | ×15.7 | 26,068.8 | 12.5분 | 2026-07-04 | 기타 | 음악 | 설명 | 503/508 |
| 143 | [Haryanvi playlist that walk up your inner dancer 🔥💋#lifewit…](https://www.youtube.com/watch?v=tYuLhTnHgOQ) | Venus Yadav | 12,500 | 4,725,514 | 378.0 | – | 56,522.9 | 11분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 없음 | 570/592 |
| 144 | [Dopamine Reset ∣ Indian Classical Flute Music for Relaxatio…](https://www.youtube.com/watch?v=gSOocWITTT4) | Desert Harmon… | 2,320 | 872,821 | 376.2 | ×1,465.7 | 8,243.1 | 8.4분 | 2026-07-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 132/138 |
| 145 | [너 때문에 하루를 살아 #이별 #이별노래 #이별감성 #새벽감성 #OST #감성발라드 #kpop #kpopb…](https://www.youtube.com/watch?v=hhbJfI8dJ9o) | 글쓰는여자🎀 | 640 | 240,358 | 375.6 | ×597.9 | 1,955.0 | 5.3분 | 2026-06-23 | 10. 팝송·K팝·J팝 | 한 곡 | 없음 | 105/105 |
| 146 | [90’S Old Hindi Songs🥰 90s Love Song💘 Udit Narayan, Alka Yag…](https://www.youtube.com/watch?v=qDOFK8SfKmA) | 90s Lovers Po… | 17,600 | 6,603,923 | 375.2 | ×3,968.7 | 96,677.1 | 27.4분 | 2026-08-17 | 기타 | 음악 | 설명 | 217/234 |
| 147 | [Lahore Diya ✨ Slowed Reverb ∣ Late Night Vibes ∣ Punjabi Lo…](https://www.youtube.com/watch?v=-rNlgODrgjo) | Arun music 100 | 9,450 | 3,540,863 | 374.7 | ×97.9 | 26,397.7 | 4.2분 | 2026-06-12 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 252/267 |
| 148 | [왜 이제 와｜음색 미쳤다는 반응 나온 새벽 감성 발라드 ｜ なぜ今になって｜音色がすごいという反応が出た、深夜の…](https://www.youtube.com/watch?v=TWunCWy98FU) | Faded Love No… | 1,150 | 428,773 | 372.9 | ×384.2 | 2,664.8 | 4.3분 | 2026-05-16 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 84/85 |
| 149 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Stu…](https://www.youtube.com/watch?v=MvV7_DKFZQA) | peacefulvibes… | 12,900 | 4,803,102 | 372.3 | ×14,402.1 | 79,987.2 | 16.3분 | 2026-08-25 | 3. 공부·집중·작업 | 음악 | 설명 | 284/292 |
| 150 | [Teri Meri Prem Kahani 💖 Slowed + Reverb ∣ Romantic Lofi Son…](https://www.youtube.com/watch?v=Njmb7oBzkpM) | 🌙 MoonVerse | 7,090 | 2,632,070 | 371.2 | – | 23,875.9 | 6.3분 | 2026-07-06 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 755/768 |
| 151 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 : 딱딱 나 틀딱 ∣ 보카로 근본 플리 1탄](https://www.youtube.com/watch?v=W_G2W0nTGYY) | 윤슬자 | 1,060 | 390,869 | 368.7 | ×14.2 | 2,405.6 | 245.8분 | 2026-05-14 | 기타 | 플레이리스트·모음 | 설명 | 333/333 |
| 152 | [katseye playlist✨💋](https://www.youtube.com/watch?v=H40nuw4mebU) | maiia | 23,200 | 8,535,456 | 367.9 | – | 157,185.1 | 21.3분 | 2026-08-31 | 기타 | 플레이리스트·모음 | 없음 | 4,330/4,722 |
| 153 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 (가사X) 후회 없는 미래를 위해 ✍️ 새벽공부 집중 로파이 BGM🎧 유리숲 플리 🌙](https://www.youtube.com/watch?v=hZLVePYp9Z0) | Yurisoop | 1,290 | 469,599 | 364.0 | ×274.6 | 6,258.9 | 132분 | 2026-08-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 42/45 |
| 154 | [Samadhi in the Stone ∣ Shiva Meditation Music ∣ Himalayan C…](https://www.youtube.com/watch?v=yp10IdD2SxY) | Divya vaani m… | 217 | 78,461 | 361.6 | ×167.7 | 4,179.8 | 6.1분 | 2026-10-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 11/12 |
| 155 | [Banjaara 🥀 Slowed + Reverb ∣ Best Hindi Lofi Song 🎧 ∣ Anime…](https://www.youtube.com/watch?v=uxMeJy4JMS8) | Broken Sky01 | 6,750 | 2,436,242 | 360.9 | ×800.2 | 27,629.8 | 6.3분 | 2026-07-28 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 857/931 |
| 156 | [• playlist 순애](https://www.youtube.com/watch?v=Av29750WaJs) | ros!e | 459 | 164,801 | 359.0 | ×13.0 | 2,992.7 | 18.4분 | 2026-08-30 | 기타 | 플레이리스트·모음 | 없음 | 56/57 |
| 157 | [Desi baddie playlist 💅💌 @desi_diva12 #playlist #baddie #des…](https://www.youtube.com/watch?v=Y3q1y6M79EU) | Desi_.Diva12 | 6,330 | 2,255,373 | 356.3 | ×38.8 | 19,166.7 | 7.3분 | 2026-06-28 | 기타 | 플레이리스트·모음 | 설명 | 207/209 |
| 158 | [Rabba Tu Na Naraz Hovi ❤️ ∣ Soulful Heart Touching Punjabi …](https://www.youtube.com/watch?v=Zh-3CGV7BwQ) | Sufi Usman | 4,740 | 1,679,853 | 354.4 | ×1,039.5 | 19,750.0 | 5.9분 | 2026-07-31 | 기타 | 음악 | 설명 | 214/220 |
| 159 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Study / Focus …](https://www.youtube.com/watch?v=KU7PfC9i9cE) | Focus Music 2… | 4,270 | 1,506,191 | 352.7 | ×3,607.6 | 60,514.8 | 13.8분 | 2026-09-29 | 3. 공부·집중·작업 | 음악 | 설명 | 92/92 |
| 160 | [Ama hem hem](https://www.youtube.com/watch?v=rPmZucO77sg) | Thatohatsi - … | 36,400 | 12,824,484 | 352.3 | ×71.1 | 119,965.5 | 7.5분 | 2026-07-09 | 기타 | 정보·해설 | 설명 | 0/2,609 |
| 161 | [[PLAYLIST] Biển Đảo Và Em, Fallin Flower, Người Yêu Bỏ Lỡ,……](https://www.youtube.com/watch?v=dMaqYNGvzmA) | wenjin. | 2,560 | 898,679 | 351.1 | ×19.1 | 8,535.6 | 26.2분 | 2026-07-11 | 기타 | 플레이리스트·모음 | 설명 | 442/448 |
| 162 | [Prasanna Vadanam – Enigma Style ∣ Lord Vishnu Peaceful Medi…](https://www.youtube.com/watch?v=QeF_NFcmxt4) | devinebeatsst… | 1,360 | 473,546 | 348.2 | ×3,055.1 | 4,821.5 | 5.1분 | 2026-07-18 | 1. 수면·명상·힐링 | 음악 | 설명 | 116/117 |
| 163 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 느좋](https://www.youtube.com/watch?v=3lY_H67eQl4) | 고김 | 544 | 189,063 | 347.5 | – | 1,590.4 | 15.3분 | 2026-06-27 | 기타 | 플레이리스트·모음 | 없음 | 52/52 |
| 164 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 🍁 설레는 바람이 부는 가을이 왔나봐 ∣ 틀어두기 좋은 감성 팝송 모음](https://www.youtube.com/watch?v=jmU_fq-iTSE) | Melly Moood | 6,780 | 2,354,739 | 347.3 | ×342.9 | 58,279.7 | 188.2분 | 2026-09-13 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 283/294 |
| 165 | [CORTIS PLAYLIST (코르티스 플레이리스트) 머니머니머니부터 나니까지](https://www.youtube.com/watch?v=2byCD3x_vPY) | 우울 대신 우웅! | 2,260 | 783,467 | 346.7 | – | 13,006.6 | 41.5분 | 2026-08-25 | 기타 | 플레이리스트·모음 | 없음 | 187/187 |
| 166 | [𝙋𝙤𝙫 :- 𝘽𝙝𝙤𝙟𝙥𝙪𝙧𝙞 𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩 ∣∣ 𝙘𝙝𝙞𝙡𝙡 𝙜𝙪𝙮𝙨 𝙖𝙣𝙙 𝙚𝙣𝙟𝙤𝙮 ∣∣ 𝙂𝘼𝙇𝘼𝙓𝘼𝙔…](https://www.youtube.com/watch?v=areWocW1pXI) | AYUSH | 4,310 | 1,485,637 | 344.7 | ×190.4 | 31,681.5 | 8분 | 2026-09-07 | 기타 | 플레이리스트·모음 | 설명 | 180/188 |
| 167 | [Golden Brown x Love Story - Relaxing Celtic Fantasy Medieva…](https://www.youtube.com/watch?v=hzPdVFw768A) | The Knight Sa… | 3,260 | 1,114,431 | 341.9 | – | 8,304.1 | 16.9분 | 2026-06-12 | 2. 자연 소리·백색소음 | 음악 | 설명 | 536/552 |
| 168 | [Sonata in the Dark 🎹 Beethoven-Inspired Melancholic Classic…](https://www.youtube.com/watch?v=sakrZHnzs6k) | Elysian Class… | 216 | 73,679 | 341.1 | ×125.3 | 1,012.8 | 16분 | 2026-08-12 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 17/17 |
| 169 | [하우스룰즈가 최고야](https://www.youtube.com/watch?v=V0mzAQ7z3D0) | Yeon | 1,010 | 344,486 | 341.1 | ×233.1 | 6,640.6 | 18.1분 | 2026-09-02 | 기타 | 플레이리스트·모음 | 설명 | 232/257 |
| 170 | [PLAYLIST I it's like supernatural I 느좋 팝송 기모띠 야르 찹찹 플리](https://www.youtube.com/watch?v=1huhmKD8P7U) | 자세히알아보기 | 565 | 192,664 | 341.0 | ×409.9 | 2,355.2 | 19.6분 | 2026-08-03 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 101/101 |
| 171 | [LEO ROJAS - Top 16 Andean Pan Flute Melodies ★ Full Album -…](https://www.youtube.com/watch?v=wR5yxMCTZA0) | Andean Flute … | 4,840 | 1,639,020 | 338.6 | ×678.0 | 29,878.9 | 98.3분 | 2026-08-30 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 233/240 |
| 172 | [The Complete "Love Is in the Air" Theme by Rock Burwell ∣ O…](https://www.youtube.com/watch?v=ipCco3jw504) | NR ENTERTAINM… | 2,810 | 948,399 | 337.5 | ×3,161.3 | 6,223.5 | 4.5분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 614/623 |
| 173 | [Emraan hashmi playlist #emraanhashmi](https://www.youtube.com/watch?v=zZzA1Hp30uE) | july_luna | 5,480 | 1,847,082 | 337.1 | ×70.4 | 29,020.7 | 7.2분 | 2026-08-21 | 기타 | 플레이리스트·모음 | 없음 | 22/31 |
| 174 | [DARKHAAST ❤️‍🩹 slowed x reverb Arijit Singh (Lyrics) Ft. Su…](https://www.youtube.com/watch?v=7u9GjyI2yxg) | GK lofi song | 9,720 | 3,253,951 | 334.8 | ×593.6 | 27,577.7 | 6.9분 | 2026-06-28 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 264/271 |
| 175 | [💿 마음이 따뜻해지는 감성 발라드 🌸 광고없이 듣는 명곡 🌸 SG워너비, 김범수, 허각](https://www.youtube.com/watch?v=d68bRNKlMQA) | 서울 소울 발라드-Seo… | 893 | 298,817 | 334.6 | ×439.1 | 4,753.5 | 156.2분 | 2026-08-22 | 9. 가요·발라드·트로트 | 음악 | 설명 | 48/48 |
| 176 | [Sands of Cairo at Night ∣ Egyptian Jazz & Relaxing Arabic L…](https://www.youtube.com/watch?v=k74U2uUB67s) | Moonlit Cairo | 4,110 | 1,373,833 | 334.3 | ×754.2 | 21,140.0 | 69.8분 | 2026-08-20 | 4. 카페·매장·라운지 | 음악 | 설명 | 127/140 |
| 177 | [【BGM】置いていかないで｜1分後に涙が溢れてくる曲](https://www.youtube.com/watch?v=e9ArzLcNNbw) | 1分後に〇〇する曲🎧 | 1,240 | 411,125 | 331.6 | ×90.1 | 3,068.8 | 4.3분 | 2026-06-12 | 기타 | 음악 | 설명 | 61/65 |
| 178 | [새벽 2시, 잠이 깼다면 다시 자세요 ∣ 6분 후 다시 잠드는 피아노 명상음악 for Deep Sleep …](https://www.youtube.com/watch?v=ViCEPJCOgy4) | 단잠TV | 2,740 | 904,738 | 330.2 | ×1,287.0 | 6,163.5 | 181.7분 | 2026-05-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 216/221 |
| 179 | [듣기만 해도 설레는 그시절 1990~2026년 사랑하고 슬퍼했던 노래- 휘성,프리스타일,조장혁,임재범,이승…](https://www.youtube.com/watch?v=dCB0KQI7qfU) | 감정 작사가 | 598 | 196,591 | 328.8 | ×1,803.6 | 1,230.1 | 118.5분 | 2026-05-17 | 기타 | 음악 | 설명 | 46/46 |
| 180 | [Perfect South Indian Playlist 🪷🦢 (+timestamps)](https://www.youtube.com/watch?v=ROBjw6FcYxs) | Being Diva 💅🏻 | 6,540 | 2,146,755 | 328.2 | ×17.8 | 57,063.8 | 7.7분 | 2026-09-16 | 기타 | 플레이리스트·모음 | 설명 | 266/291 |
| 181 | [한국 드라마 OST 황금기 모음💗마음을 울리는 인기 노래 모음 하루 종일 들어도 좋은 발라드🎧20-26년 …](https://www.youtube.com/watch?v=Vxw1QiXjDvs) | K-Drama Memor… | 2,760 | 900,235 | 326.2 | ×374.6 | 16,843.9 | 74.3분 | 2026-08-31 | 13. OST·사운드트랙 | 플레이리스트·모음 | 설명 | 140/140 |
| 182 | [💖 मेरा चाँद मुझे आया नजर ∣ New Hindi Song 2026 ∣ Romantic S…](https://www.youtube.com/watch?v=FxNQw0BRhWg) | Feel The Music | 3,320 | 1,082,775 | 326.1 | ×641.5 | 28,649.6 | 16.1분 | 2026-09-16 | 기타 | 음악 | 설명 | 65/69 |
| 183 | [나그네](https://www.youtube.com/watch?v=FFwUpZZGqnc) | 여산일거 | 4,340 | 1,414,102 | 325.8 | ×213.7 | 8,299.3 | 8.9분 | 2026-05-06 | 기타 | 한 곡 | 설명 | 372/376 |
| 184 | [JANANAYAGAN - Forest BGM ∣ The Ultimate Cinematic Experienc…](https://www.youtube.com/watch?v=uVuVb5CdEC8) | Massplix | 1,340 | 436,185 | 325.5 | – | 2,541.6 | 4.5분 | 2026-05-05 | 기타 | 음악 | 설명 | 167/168 |
| 185 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=29EWidvY0b8) | AR BROTHER | 7,450 | 2,412,805 | 323.9 | – | 50,236.7 | 18.6분 | 2026-09-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 87/95 |
| 186 | [𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 틱톡 그 느좋 노래 모음](https://www.youtube.com/watch?v=NG6SQIGv3-Y) | 뭐야 | 1,840 | 590,112 | 320.7 | ×52.5 | 5,741.3 | 8.9분 | 2026-07-13 | 기타 | 플레이리스트·모음 | 설명 | 112/113 |
| 187 | [90s Romantic Hits DJ Mix ∣ Hindi Love Song ∣ 90s Romantic B…](https://www.youtube.com/watch?v=Lk2qE-YdhS8) | AM MUSIC HUB | 4,000 | 1,279,110 | 319.8 | ×2,621.1 | 18,217.7 | 16분 | 2026-08-15 | 기타 | 음악 | 설명 | 50/58 |
| 188 | [Hallucination Journey ∣ Stoner Music & Trippy Visuals🌿](https://www.youtube.com/watch?v=QbWDBeBn_OY) | RYNO | 550 | 174,298 | 316.9 | ×213.6 | 1,299.2 | 10분 | 2026-06-12 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 13/13 |
| 189 | [Playlist For You To Create Fake Scenarios In Your Mind 🤍 ∣ …](https://www.youtube.com/watch?v=0gUwbTCQ78k) | NOXTUNE | 21,000 | 6,635,761 | 316.0 | ×1,091.9 | 86,544.2 | 12.6분 | 2026-08-08 | 기타 | 플레이리스트·모음 | 설명 | 1,399/1,438 |
| 190 | [Sad lo_fi🥺💔2026 ultimate](https://www.youtube.com/watch?v=q-iefUnWPCY) | mr prakash 😊 | 5,510 | 1,735,087 | 314.9 | ×1,218.5 | 40,612.8 | 18.6분 | 2026-09-11 | 기타 | 음악 | 설명 | 143/151 |
| 191 | [𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 1](https://www.youtube.com/watch?v=rRxojiPo0SU) | 헿 | 635 | 198,716 | 312.9 | – | 2,058.1 | 10.6분 | 2026-07-19 | 기타 | 플레이리스트·모음 | 없음 | 40/40 |
| 192 | [Omnia vincit](https://www.youtube.com/watch?v=5yKI8IQNzAo) | Soul Beyond S… | 460 | 143,560 | 312.1 | – | 1,207.6 | 4.2분 | 2026-06-27 | 기타 | 정보·해설 | 설명 | 38/39 |
| 193 | [Karpur Gauram ∣ कर्पूर गौरम् ∣ Shiva Stotram Trance Remix ∣…](https://www.youtube.com/watch?v=d47X_wGxFnY) | DigitalDeepDe… | 4,130 | 1,285,689 | 311.3 | ×1,356.2 | 8,045.6 | 11.1분 | 2026-05-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 337/345 |
| 194 | [𝐵𝑒𝓈𝓉 𝒮𝑜𝓊𝓉𝒽 𝐼𝓃𝒹𝒾𝒶𝓃 𝒮𝑜𝓃𝑔𝓈 𝒫𝓁𝒶𝓎𝓁𝒾𝓈𝓉 🎶 𝒯𝒶𝓂𝒾𝓁 • 𝒯𝑒𝓁𝓊𝑔𝓊 • 𝑀𝒶𝓁𝒶𝓎𝒶𝓁…](https://www.youtube.com/watch?v=GAXYvJx8rD4) | Nyxelune | 6,120 | 1,891,397 | 309.1 | – | 19,745.3 | 10.3분 | 2026-07-20 | 기타 | 정보·해설 | 설명 | 1,056/1,084 |
| 195 | [Golden Melodies for the Soul (Sax & Violin Lounge)](https://www.youtube.com/watch?v=0shfF2LDgmI) | Timeless Echo | 5,700 | 1,753,939 | 307.7 | ×188.6 | 12,397.0 | 6.7분 | 2026-06-04 | 4. 카페·매장·라운지 | 음악 | 설명 | 356/368 |
| 196 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ Q. 여전히 잊지 못했나요?](https://www.youtube.com/watch?v=ObbsVpc8iRM) | 청춘 | 1,360 | 417,999 | 307.4 | ×5.1 | 3,075.3 | 24분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 설명 | 491/491 |
| 197 | [Jazz Cover Indonesia ∣ Lagu Santai Untuk Bekerja 🎷](https://www.youtube.com/watch?v=kwqjENclcyE) | Ide Rahayu | 4,630 | 1,420,137 | 306.7 | ×856.3 | 13,353.3 | 74.5분 | 2026-07-09 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 152/159 |
| 198 | [Tum Jo Aaye ✨ ∣∣ Kitab Song ∣∣ Bairan ( Slowed X Reverb ) M…](https://www.youtube.com/watch?v=xyL4vZnw5xs) | Mix Facto 02 | 41,200 | 12,628,093 | 306.5 | ×8,915.0 | 76,184.1 | 20.3분 | 2026-05-11 | 기타 | 음악 | 설명 | 2,719/2,751 |
| 199 | [Nhạc Thiền Tĩnh Tâm 🌿 Giải Tỏa Căng Thẳng, Buông Bỏ Muộn Ph…](https://www.youtube.com/watch?v=qTOqj4r0FNg) | Thiền Sen Trúc | 2,050 | 628,255 | 306.5 | ×142.0 | 5,822.4 | 58.6분 | 2026-07-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 433/436 |
| 200 | ["Comfort song's - All in one playlist"😭✨🌷//part-4//edit by …](https://www.youtube.com/watch?v=617yn663oeA) | Anushri | 7,570 | 2,319,077 | 306.4 | ×12.5 | 30,452.0 | 7.6분 | 2026-08-09 | 기타 | 플레이리스트·모음 | 설명 | 293/308 |
| 201 | [Patar Bashori ∣ পাতার বাঁশরী ∣ Lofi Bangla Song ∣ Emotional…](https://www.youtube.com/watch?v=rgKNbCrC-cc) | Jasu LOFI | 26,700 | 8,123,568 | 304.2 | ×4,151.0 | 94,760.6 | 4.1분 | 2026-07-30 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 1,081/1,119 |
| 202 | [LOVEIN & Ismail Uluçay - Drafting (Original Mix)](https://www.youtube.com/watch?v=clQARvetnyk) | LOVEIN | 40,500 | 12,216,195 | 301.6 | ×192.8 | 71,133.2 | 7.3분 | 2026-05-05 | 4. 카페·매장·라운지 | 음악 | 설명 | 422/430 |
| 203 | [𝘊𝘦𝘳𝘵𝘪𝘧𝘪𝘦𝘥 𝘋𝘦𝘴𝘪 𝘉𝘢𝘯𝘨𝘦𝘳𝘴 𝘵𝘩𝘢𝘵 𝘴𝘭𝘢𝘱 (+𝘵𝘪𝘮𝘦𝘴𝘵𝘢𝘮𝘱𝘴) 💅🔥](https://www.youtube.com/watch?v=PZcsGXrrBGY) | A BEE Editz | 11,100 | 3,337,481 | 300.7 | ×55.0 | 53,161.8 | 12.9분 | 2026-08-22 | 기타 | 플레이리스트·모음 | 설명 | 363/391 |
| 204 | [pov: you're blushing while listening to this 🎧✨](https://www.youtube.com/watch?v=MOpFDe87RBM) | NIKKU | 9,260 | 2,756,227 | 297.6 | ×3,373.6 | 20,311.8 | 13.4분 | 2026-06-10 | 기타 | 플레이리스트·모음 | 설명 | 1,534/1,561 |
| 205 | [[グラブル] Granblue Fantasy OST - Last Salvation (vs. Raskeid &…](https://www.youtube.com/watch?v=TFsAT5TtzSg) | Decim | 1,690 | 500,962 | 296.4 | ×443.7 | 5,297.9 | 7분 | 2026-07-21 | 기타 | 음악 | 설명 | 416/420 |
| 206 | [Positive September 🍂 Relaxing Coffee Melody & Acoustic Chil…](https://www.youtube.com/watch?v=Bq4sPMz6fUk) | Chill Moments | 4,550 | 1,344,222 | 295.4 | ×262.5 | 23,639.6 | 142.9분 | 2026-08-28 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 98/98 |
| 207 | [난 아직 어린데](https://www.youtube.com/watch?v=Zo3DsQ9j2J0) | 맹묘 | 1,600 | 472,016 | 295.0 | – | 3,494.7 | 20.1분 | 2026-06-11 | 기타 | 플레이리스트·모음 | 없음 | 990/1,011 |
| 208 | [🤍Golden brown x Love story (Piano Cover)🤍](https://www.youtube.com/watch?v=dK4RoOPXQ0Q) | Solaceful Keys | 212 | 61,962 | 292.3 | – | 628.7 | 4.1분 | 2026-07-17 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 82/82 |
| 209 | [Peni Me Chheni Satai Diyo -Instagram Trending Lofi Song ∣ A…](https://www.youtube.com/watch?v=gJyWm3GFFik) | Tushar Music … | 5,660 | 1,645,649 | 290.8 | ×1,371.4 | 19,550.4 | 6.1분 | 2026-08-01 | 8. 로파이·시티팝·칠 | 음악 | 없음 | 87/89 |
| 210 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=099F7hK6c8c) | Song verse Hi… | 10,300 | 2,987,057 | 290.0 | ×9,247.9 | 74,199.4 | 13분 | 2026-09-14 | 3. 공부·집중·작업 | 음악 | 설명 | 186/189 |
| 211 | [MUSIK SANTAI VIRAL 2026 🎧 Lagu Pop Indonesia Akustik Terbai…](https://www.youtube.com/watch?v=bZEwYquV6Kg) | Akustik Cantik | 10,500 | 3,012,978 | 286.9 | ×539.1 | 30,670.4 | 78.5분 | 2026-07-18 | 기타 | 정보·해설 | 설명 | 182/209 |
| 212 | [Cozy Rainy Autumn Café 🍁 Relaxing Day with Warm Jazz Music …](https://www.youtube.com/watch?v=1wyP0BN_jqI) | Tiny Café Jazz | 4,090 | 1,156,735 | 282.8 | ×850.2 | 11,578.5 | 231.1분 | 2026-07-16 | 4. 카페·매장·라운지 | 음악 | 설명 | 457/464 |
| 213 | [𝐬𝐭𝐮𝐝𝐲 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 이번엔 아무한테도 말 안 하고 준비한다 🤫 전문직·수험생 시험공부 집중 로파이 …](https://www.youtube.com/watch?v=eRQFKz_nigU) | loni pli 로니플리 | 1,450 | 409,206 | 282.2 | ×95.5 | 9,331.5 | 137.3분 | 2026-09-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 85/87 |
| 214 | [[커버곡] 가는세월 🎧 락발라드로 다시 태어난 불후의 명곡 🎶두둥치 DUDUNGCHI](https://www.youtube.com/watch?v=0J4iOmTGAgo) | 두둥치 | 255 | 70,711 | 277.3 | ×397.3 | 430.3 | 4.2분 | 2026-05-12 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 26/26 |
| 215 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 l 연모(戀慕)](https://www.youtube.com/watch?v=uVbmoXg5YvI) | 미니악단 | 659 | 182,627 | 277.1 | ×739.4 | 1,482.5 | 69분 | 2026-06-23 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 88/91 |
| 216 | [Shri Krishna Govind Hare Murari - Non Stop Krishna Bhajans …](https://www.youtube.com/watch?v=Tqr5PqrzeQw) | Bhajan World … | 33,000 | 9,143,789 | 277.1 | ×123.8 | 78,286.1 | 29.8분 | 2026-06-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,540/1,543 |
| 217 | [Rest Your Mind ∣ Your Brain Needs Silence ∣ Dopamine Reset …](https://www.youtube.com/watch?v=UWZ_QQNKmes) | Essential Ind… | 19,400 | 5,349,642 | 275.8 | ×3,656.6 | 44,943.1 | 20.7분 | 2026-06-27 | 1. 수면·명상·힐링 | 음악 | 설명 | 833/854 |
| 218 | [Hum Tere Hote Toh ( Official Music ) Musafir cafe ....](https://www.youtube.com/watch?v=V_UCyoYIWEo) | Music Covers … | 1,770 | 485,547 | 274.3 | ×409.2 | 5,509.5 | 4.4분 | 2026-07-28 | 4. 카페·매장·라운지 | 음악 | 설명 | 79/79 |
| 219 | [Vachindamma (Lyrics + English Translation) ∣ Geetha Govinda…](https://www.youtube.com/watch?v=DliA185LSPU) | LYRICS FOR YOU | 5,220 | 1,425,017 | 273.0 | ×238.0 | 8,109.5 | 4.1분 | 2026-05-01 | 기타 | 한 곡 | 설명 | 240/240 |
| 220 | [Om Namo Bhagavate Vasudevaya ∣ 1 Hour Divine Vishnu Meditat…](https://www.youtube.com/watch?v=OfDob7wO9OU) | Zynora | 4,450 | 1,212,784 | 272.5 | ×256.9 | 7,784.2 | 77.8분 | 2026-05-21 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 317/328 |
| 221 | [[ Playlist ] 어떻게 너가 다른 남자를 만나](https://www.youtube.com/watch?v=0USEQaYCf78) | 하온 | 1,700 | 462,610 | 272.1 | – | 5,213.9 | 20.9분 | 2026-07-27 | 기타 | 플레이리스트·모음 | 설명 | 48/48 |
| 222 | [.•♫•♬•𝙁𝙄𝙉𝙀𝙎𝙃𝙔𝙏 PLAYLIST•♬•♫](https://www.youtube.com/watch?v=wYiyAR_dBDU) | loverswift | 5,040 | 1,368,815 | 271.6 | ×32.8 | 14,733.8 | 16.8분 | 2026-07-23 | 기타 | 플레이리스트·모음 | 설명 | 112/116 |
| 223 | [조영버 노동요](https://www.youtube.com/watch?v=twTedu4I1mg) | 궈바오러우 | 498 | 135,209 | 271.5 | – | 787.0 | 19.7분 | 2026-05-05 | 3. 공부·집중·작업 | 플레이리스트·모음 | 없음 | 205/205 |
| 224 | [🌊2000년 넘게 전해진 가장 슬픈 노래 ∣ 님아, 그 강을 건너지 마오 ∣ 역사노래 ∣ 사랑노래](https://www.youtube.com/watch?v=4q22526wbNM) | 노래말싸미 | 273 | 73,928 | 270.8 | ×325.7 | 560.3 | 4.6분 | 2026-06-14 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 38/38 |
| 225 | ["수고했어..오늘은 푹 자! 😴 마음을 편하게 해주는 피아노 수면음악 (10 Hours)](https://www.youtube.com/watch?v=3br0mkww4do) | jazzyang 재즈냥 | 1,470 | 396,089 | 269.4 | ×1,450.9 | 4,013.7 | 616.6분 | 2026-07-17 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 91/128 |
| 226 | [Vintage Vibes: Best of 80s with Cyndi Lauper, Modern Talkin…](https://www.youtube.com/watch?v=1n5pMgUPYnk) | Disco Paradis… | 26,800 | 7,187,964 | 268.2 | ×2,961.7 | 101,674.8 | 117.2분 | 2026-08-14 | 기타 | 플레이리스트·모음 | 설명 | 523/548 |
| 227 | [Heartbreaking 💔 songs + lofi Mashup songs Slowed Reverb son…](https://www.youtube.com/watch?v=swi-om1VW34) | JR buzdar off… | 16,900 | 4,526,034 | 267.8 | ×13,081.0 | 75,189.8 | 8분 | 2026-08-25 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 202/205 |
| 228 | [Sunday Morning Coffee Club ∣ R&B, Hip Hop, Afrobeats ∣ Feat…](https://www.youtube.com/watch?v=2zzgY6uxZ6o) | EChen | 7,820 | 2,082,947 | 266.4 | ×45.4 | 12,567.8 | 59.4분 | 2026-05-11 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 215/217 |
| 229 | [🏨 Luxury Hotel Lounge ∣ Smooth Jazz & Elegant Background Mu…](https://www.youtube.com/watch?v=GBLcMvTFGyg) | AMBER&OAK | 7,700 | 2,049,686 | 266.2 | ×932.1 | 14,447.3 | 100.4분 | 2026-06-04 | 4. 카페·매장·라운지 | 음악 | 설명 | 249/263 |
| 230 | [🌼 Sawan Shiv Bhajan 2026 ∣ Peaceful Mahadev Bhakti Song ∣ B…](https://www.youtube.com/watch?v=I_vnh6nZW6c) | Bhajan Soul C… | 8,590 | 2,268,153 | 264.1 | ×295.9 | 21,035.6 | 5.8분 | 2026-07-08 | 기타 | 음악 | 설명 | 612/616 |
| 231 | [별일 없던 하루였는데, 괜히 마음이 시끄러운 밤](https://www.youtube.com/watch?v=mc73qn75vMs) | 리듬다방(김리다) | 1,440 | 379,012 | 263.2 | ×822.2 | 2,773.2 | 7.5분 | 2026-06-09 | 기타 | 음악 | 설명 | 207/218 |
| 232 | [탈북할 때 듣는 플리](https://www.youtube.com/watch?v=rrgoyhVFJ68) | 비둘기 | 2,910 | 759,028 | 260.8 | ×251.5 | 9,073.1 | 57.6분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 없음 | 1,536/1,536 |
| 233 | [A playlist cuz kanhi is your safe place 🦚🪷🪈🦢 ∣∣ Song playli…](https://www.youtube.com/watch?v=vH7kCnulptw) | Lily⋆.𐙚 ̊ | 9,470 | 2,462,026 | 260.0 | – | 18,408.2 | 17.5분 | 2026-06-12 | 기타 | 플레이리스트·모음 | 설명 | 843/865 |
| 234 | [The Shiva Reset ∣ Shiva Trance for the Overstimulated Mind …](https://www.youtube.com/watch?v=N95edHAuFzA) | Nirvana Beats | 7,030 | 1,817,146 | 258.5 | ×352.5 | 23,802.9 | 6.8분 | 2026-08-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 295/304 |
| 235 | [[Playlist] 드라마 OST 모음](https://www.youtube.com/watch?v=h_2uk2pTQQA) | playlistsilya… | 828 | 213,926 | 258.4 | ×13.9 | 3,773.2 | 17.5분 | 2026-08-28 | 13. OST·사운드트랙 | 플레이리스트·모음 | 없음 | 17/17 |
| 236 | [Rain and Soft Piano Music for Deep Sleep - Calm Sleep and S…](https://www.youtube.com/watch?v=8DzndrjZi18) | RainwoodPiano… | 1,270 | 326,313 | 256.9 | ×213.6 | 6,046.6 | 31.9분 | 2026-08-31 | 1. 수면·명상·힐링 | 음악 | 설명 | 40/41 |
| 237 | [⛈️(No Ads) WARNING: YOU MAY SLEEP FAST 😴 NYC Rain on Window…](https://www.youtube.com/watch?v=HLp0t2jZlKQ) | Dreamy Raining | 3,950 | 1,012,926 | 256.4 | ×43.8 | 5,844.2 | 600분 | 2026-05-04 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 90/94 |
| 238 | [𝐀𝐋𝐋 𝐓𝐑𝐄𝐍𝐃𝐈𝐍𝐆 𝐇𝐈𝐍𝐃𝐈 𝐒𝐎𝐍𝐆𝐒 𝟐𝟎𝟐𝟔 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 🎀 ∣COZI](https://www.youtube.com/watch?v=HNdauINck9s) | cozi_music | 32,800 | 8,388,031 | 255.7 | ×71.4 | 91,248.7 | 15.2분 | 2026-07-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 2,887/2,956 |
| 239 | [[𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 삶에 무뎌지는 법](https://www.youtube.com/watch?v=8KGuQMhnb14) | 꾹팅 | 1,280 | 323,769 | 252.9 | ×63.4 | 2,353.0 | 19.4분 | 2026-06-08 | 기타 | 플레이리스트·모음 | 설명 | 363/408 |
| 240 | [జీవితంలో ఒక్కసారైనా ఆ ఏడుకొండలు ఎక్కాలయ్యా ∣Soulful Sri Ven…](https://www.youtube.com/watch?v=sfnGhZdoNQk) | Surendra's Mu… | 5,100 | 1,289,044 | 252.8 | ×755.6 | 10,046.8 | 5.3분 | 2026-06-18 | 기타 | 음악 | 설명 | 554/554 |
| 241 | [MIMIFY - I Waited too Long (Original Mix)](https://www.youtube.com/watch?v=F2Iga1V4cqo) | MIMIFY | 18,500 | 4,657,825 | 251.8 | ×421.6 | 44,850.2 | 7.8분 | 2026-07-12 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 675/677 |
| 242 | [Zindagi ∣ Chal Thora Aur ∣ Na Kwahish Na Koi Tamana Mujhe (…](https://www.youtube.com/watch?v=dyOp23A-i_o) | cefur studio | 11,600 | 2,910,784 | 250.9 | ×631.6 | 22,615.1 | 4.8분 | 2026-06-17 | 기타 | 음악 | 설명 | 1,835/1,848 |
| 243 | [All Stress Disappears When This Music Starts Playing 🎶 Emot…](https://www.youtube.com/watch?v=mtelE3vg758) | Nature Healin… | 7,390 | 1,836,062 | 248.4 | ×5,755.7 | 10,938.0 | 99.6분 | 2026-05-09 | 1. 수면·명상·힐링 | 음악 | 설명 | 482/481 |
| 244 | [우리들의 발라드2 1회 플레이리스트｜가을밤 마음을 울린 발라드 7곡 #우리들의발라드 #우발2](https://www.youtube.com/watch?v=wPEmG4xfTLE) | 우낄라꼬 | 1,310 | 323,468 | 246.9 | – | 19,433.4 | 30.4분 | 2026-10-07 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 63/64 |
| 245 | [Relaxing Piano Music with Rain Sounds for Deep Sleep - Calm…](https://www.youtube.com/watch?v=dzRT9vqg9xs) | RainwoodPiano… | 1,270 | 312,677 | 246.2 | ×204.6 | 12,523.8 | 110분 | 2026-09-29 | 2. 자연 소리·백색소음 | 음악 | 설명 | 38/40 |
| 246 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐅𝐨𝐫 𝐘𝐨𝐮 𝐓𝐨 𝐂𝐫𝐞𝐚𝐭𝐞 𝐅𝐚𝐤𝐞 𝐒𝐜𝐞𝐧𝐚𝐫𝐢𝐨𝐬 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐌𝐢𝐧𝐝 🤍 ∣ …](https://www.youtube.com/watch?v=flQgOwg4jLI) | Ashik's Cloud… | 15,800 | 3,869,010 | 244.9 | ×6.4 | 36,545.0 | 15.2분 | 2026-07-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 965/983 |
| 247 | [Viral Pop Songs Cover 2026 🎙 Top Music Playlist Hits](https://www.youtube.com/watch?v=JKRRl5-5-hw) | Acoustic Ther… | 21,300 | 5,148,621 | 241.7 | ×9,112.6 | 34,243.8 | 57.4분 | 2026-05-26 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 설명 | 512/521 |
| 248 | [Relax Cha Cha Music 🪘 Havana Cafe Music - Cha Cha Son Cubano](https://www.youtube.com/watch?v=poj2d6YKC6w) | Cha Cha Havan… | 1,640 | 396,182 | 241.6 | ×2,870.9 | 2,338.1 | 6.4분 | 2026-05-07 | 4. 카페·매장·라운지 | 음악 | 설명 | 96/99 |
| 249 | [राग भैरव ∣ भगवान शिव का पवित्र प्रभात राग ∣ Raga Bhairav ∣ …](https://www.youtube.com/watch?v=3kgbzavVRiY) | मनतरंग ∣ ManT… | 1,950 | 467,465 | 239.7 | – | 9,819.1 | 11.7분 | 2026-09-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 82/82 |
| 250 | [Heartbreaking Lofi Mashup 💔 (Slowed + Reverb) ∣ Study, Focu…](https://www.youtube.com/watch?v=6mgb7GxwLvA) | stylish offic… | 12,200 | 2,919,539 | 239.3 | ×10,483.1 | 40,423.4 | 7.8분 | 2026-08-13 | 3. 공부·집중·작업 | 음악 | 설명 | 132/135 |
| 251 | [𝐒𝐨𝐧𝐠𝐬 𝐭𝐡𝐚𝐭 𝐟𝐞𝐞𝐥 𝐥𝐢𝐤𝐞 𝐚 𝐛𝐨𝐥𝐥𝐲𝐰𝐨𝐨𝐝 𝐦𝐨𝐯𝐢𝐞 🦢🪷🪐∣∣ songs playlist…](https://www.youtube.com/watch?v=r88MexwnbMA) | ⋆.ʚଓ ּ𝐋𝗒𝗋𝗂𝖼αᥣ… | 7,150 | 1,706,831 | 238.7 | ×17.4 | 19,017.3 | 10.5분 | 2026-07-26 | 기타 | 플레이리스트·모음 | 설명 | 291/296 |
| 252 | [Put Your Baby to Sleep in 2 Minutes 😴 3 Hours Deep Lullaby …](https://www.youtube.com/watch?v=2W9Y6KcJK1E) | Calm Baby Lul… | 4,340 | 1,024,530 | 236.1 | ×1,944.1 | 5,834.6 | 183.3분 | 2026-05-01 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 0/0 |
| 253 | [🌼 Soulful Shiv Bhajan 2026 ∣ Peaceful Mahadev Bhakti Song ∣…](https://www.youtube.com/watch?v=soTUDFUagOU) | Divine Bhajan… | 5,950 | 1,394,998 | 234.4 | ×362.3 | 14,125.7 | 6.6분 | 2026-07-17 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 395/397 |
| 254 | [Slow and Reverb Pashto Tappy 🎧 ∣ New Pashto Song ∣ Relaxing…](https://www.youtube.com/watch?v=88J0afFBt3s) | MarjanMusic | 4,460 | 1,027,747 | 230.4 | ×548.7 | 7,927.0 | 13분 | 2026-06-16 | 기타 | 음악 | 설명 | 81/81 |
| 255 | [VIVANT ᐸMain themeᐳ](https://www.youtube.com/watch?v=MuGFcUggtDs) | Akira Senju -… | 7,670 | 1,762,094 | 229.7 | ×26.9 | 19,754.0 | 4.6분 | 2026-07-27 | 13. OST·사운드트랙 | 정보·해설 | 설명 | 0/0 |
| 256 | [The Love Playlist You’ve Been Looking For😌🤍](https://www.youtube.com/watch?v=G4M-E29DlAE) | Melovo tunes | 3,320 | 755,471 | 227.6 | – | 5,248.7 | 10.4분 | 2026-06-02 | 기타 | 플레이리스트·모음 | 설명 | 800/807 |
| 257 | [[PLAYLIST] 할머니가 돼서도 들을 노래](https://www.youtube.com/watch?v=Oomy8ijLJxQ) | 당무 | 2,620 | 590,617 | 225.4 | ×92.9 | 3,542.3 | 23.7분 | 2026-05-10 | 기타 | 플레이리스트·모음 | 없음 | 131/131 |
| 258 | [MEGA BASS 🔊🔥 EXTREME NONSTOP EDM REMIX 💯 MONSTER DROP ⚠️ CL…](https://www.youtube.com/watch?v=Kc071SEvHgc) | Street Bass C… | 27,400 | 6,169,917 | 225.2 | ×8,871.2 | 40,773.8 | 42.7분 | 2026-05-26 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 1,383/1,400 |
| 259 | [Music Therapy Helps Restore the Nervous System 🌿 Relaxing M…](https://www.youtube.com/watch?v=yP0NAC8Hzy8) | Clara Monica … | 3,590 | 804,905 | 224.2 | ×26.2 | 6,952.1 | 19.7분 | 2026-06-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 236/244 |
| 260 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 틀기만 해도 기분이 좋아지는 플리☀️🌿 (광고없음) 국내 노래 모음](https://www.youtube.com/watch?v=mg5OWdP3DL8) | 오늘의 플리 | 6,960 | 1,556,804 | 223.7 | ×173.0 | 21,584.1 | 603.4분 | 2026-08-13 | 기타 | 플레이리스트·모음 | 없음 | 150/156 |
| 261 | [Bedroom R&B After Hours ∣ Obsessive Love Playlist ∣ Dark ro…](https://www.youtube.com/watch?v=WRi5W4B2vgQ) | afterlove. | 8,570 | 1,915,987 | 223.6 | ×253.1 | 62,524.7 | 81.7분 | 2026-09-23 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 177/192 |
| 262 | [Heartbreaking💔 mashup lofi Songs ∣ Slowed + Reverb ∣ Late N…](https://www.youtube.com/watch?v=z3H-p4r9EC4) | Soulmate Song… | 7,940 | 1,766,877 | 222.5 | ×8,314.7 | 30,350.8 | 8분 | 2026-08-27 | 3. 공부·집중·작업 | 음악 | 설명 | 139/145 |
| 263 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Sad…](https://www.youtube.com/watch?v=KjFcRYZBKs0) | Music Nest HD | 12,200 | 2,712,244 | 222.3 | ×8,000.7 | 99,919.0 | 8.9분 | 2026-09-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 101/103 |
| 264 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=FB8QuMi3fTs) | Z B Official … | 22,700 | 4,989,375 | 219.8 | ×14,588.8 | 76,638.5 | 7.7분 | 2026-08-20 | 3. 공부·집중·작업 | 음악 | 설명 | 203/205 |
| 265 | [Playlist ∣ Start Your Work with This 😎 Light Focus, Solid R…](https://www.youtube.com/watch?v=PF7MEHrmFjQ) | Noirvoya | 371 | 81,174 | 218.8 | ×336.1 | 595.6 | 16.4분 | 2026-06-10 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 30/30 |
| 266 | [Top Spotify Hits 2026 🎵 Trending English Love Songs ∣ Acous…](https://www.youtube.com/watch?v=FPlJt2A0yYo) | Chill Chord | 12,000 | 2,624,578 | 218.7 | ×150.2 | 26,956.9 | 54.8분 | 2026-07-18 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 282/294 |
| 267 | [Hyperfocus ∣ LOCK IN for 3 Hours ∣ Deep Work Study With Me …](https://www.youtube.com/watch?v=UXwJ9RwdyHs) | Work With Paul | 19,500 | 4,258,886 | 218.4 | ×31.0 | 90,478.4 | 172분 | 2026-09-07 | 3. 공부·집중·작업 | 긴 한 곡·반복 | 설명 | 492/536 |
| 268 | [Peaceful Piano, Flute & Water Sounds 💧 ∣ Relaxing Music for…](https://www.youtube.com/watch?v=NO0Y0KepgZw) | Cozy Flow Rel… | 763 | 165,716 | 217.2 | ×199.8 | 3,301.2 | 14.6분 | 2026-09-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 78/96 |
| 269 | [🍂편안해지는 따뜻한 가을 노래 ∣ 추억의 올드팝송 ∣ 가을 카페 팝송 감미로운 여친 목소리∣ Oldies …](https://www.youtube.com/watch?v=yfKtKmmUsoQ) | 나무감성 NAMUVIBE | 2,470 | 535,692 | 216.9 | ×35.9 | 21,876.3 | 135분 | 2026-09-29 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 173/175 |
| 270 | [Asiwafuni](https://www.youtube.com/watch?v=9c1b0JLxKG4) | Benzoo - Topic | 11,900 | 2,580,206 | 216.8 | ×11.2 | 30,035.9 | 6.7분 | 2026-07-30 | 기타 | 음악 | 설명 | 0/1,373 |
| 271 | [[𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁] 행운이 따라올 것 같은 여름 플리 🌊🚃 ∣ 괜히 여행 가고 싶어지는 음악 ∣ 카페 BG…](https://www.youtube.com/watch?v=sdyu1kMXQPw) | HIWAVA | 2,090 | 451,716 | 216.1 | ×398.3 | 3,128.1 | 165.3분 | 2026-06-01 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 157/158 |
| 272 | [Relaxing Jazz Café in Paris ∣ Cozy Rainy Evening Jazz Ambie…](https://www.youtube.com/watch?v=3mNYh_27x5k) | European Jazz… | 1,630 | 352,041 | 216.0 | ×604.9 | 4,973.8 | 14.5분 | 2026-08-14 | 2. 자연 소리·백색소음 | 음악 | 설명 | 1/1 |
| 273 | [(NO MID-ROLL ADS) Cozy Rainy & Spooky Halloween 🍂 Fall Jazz…](https://www.youtube.com/watch?v=p1b2tWu4XkE) | Relaxing Chri… | 4,360 | 939,874 | 215.6 | ×308.6 | 47,330.3 | 249.2분 | 2026-10-04 | 7. 재즈·보사노바 | 음악 | 설명 | 383/449 |
| 274 | [Odysseus](https://www.youtube.com/watch?v=WCxx_OVOVUw) | Ludwig Görans… | 43,300 | 9,212,521 | 212.8 | ×18.9 | 92,213.6 | 8.7분 | 2026-07-16 | 13. OST·사운드트랙 | 음악 | 설명 | 0/5,658 |
| 275 | [이선희 노래 〈잘가요, 내사랑〉 ∣ Goodbye, The One I Loved ∣ 再见了，我曾爱过的人 ∣…](https://www.youtube.com/watch?v=Ibdr_7ukGyI) | AI음악으로멜론1위찍습니다 | 3,100 | 656,160 | 211.7 | ×1,137.2 | 4,091.8 | 4.8분 | 2026-05-16 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 707/713 |
| 276 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 안 붙잡을게, 진짜로](https://www.youtube.com/watch?v=mgSfxFVkmv4) | 탱이 | 1,700 | 358,737 | 211.0 | ×34.5 | 2,828.9 | 18.3분 | 2026-06-19 | 기타 | 플레이리스트·모음 | 설명 | 150/151 |
| 277 | [Sad Song Playlist (+ with timestamps) !!](https://www.youtube.com/watch?v=q48Y5Hf83Bk) | Mood Tapes 🎶 | 18,500 | 3,874,572 | 209.4 | ×87.9 | 28,349.3 | 14.7분 | 2026-06-09 | 기타 | 플레이리스트·모음 | 설명 | 1,520/1,577 |
| 278 | [일할 때 듣기 좋은 발라드 베스트 100곡 🌸 광고 없는 감성 플레이리스트 왁스, 소울스타, 원티드, 임창…](https://www.youtube.com/watch?v=aJ61beIT3qc) | Dragon Melody | 1,310 | 274,290 | 209.4 | ×614.3 | 2,125.8 | 138.7분 | 2026-06-17 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 30/31 |
| 279 | [Lagu Pop Santai Indonesia 2026 ☕ Lagu Pop Indonesia Terbaik…](https://www.youtube.com/watch?v=MoghOkKhNFk) | MITRO MUSIC | 5,450 | 1,137,215 | 208.7 | ×249.3 | 7,073.2 | 83.7분 | 2026-05-16 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 178/185 |
| 280 | [Gladiator Ambience — Cinematic & Emotional Music for Honor …](https://www.youtube.com/watch?v=iBofqYaXA_U) | sleyvenn | 5,050 | 1,052,492 | 208.4 | ×238.7 | 7,110.4 | 120분 | 2026-05-29 | 2. 자연 소리·백색소음 | 음악 | 설명 | 284/292 |
| 281 | [빗속 파리의 라흐마니노프 🌧️ In the Style of Rachmaninoff , 깊고 잔잔한 클래식 …](https://www.youtube.com/watch?v=msDBphyeZIc) | Moonlight rep… | 2,390 | 493,045 | 206.3 | ×778.9 | 4,853.6 | 65.6분 | 2026-07-14 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 116/117 |
| 282 | [[Playlist] 스트레이 키즈 노래 모음 연속 듣기 🔥 Stray Kids Best Songs 2026…](https://www.youtube.com/watch?v=Lj8FLAC9h58) | 내귀에 PLY | 2,420 | 497,735 | 205.7 | ×1,463.9 | 6,874.4 | 120.4분 | 2026-08-12 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 164/183 |
| 283 | [सुकून देने वाली धुन 🏔️ ∣ Mind Relaxing Music ∣ Flute Music](https://www.youtube.com/watch?v=dLdXYN50hgQ) | Soulful Music… | 4,510 | 923,497 | 204.8 | ×14,317.8 | 6,560.8 | 5.9분 | 2026-06-05 | 기타 | 음악 | 설명 | 331/333 |
| 284 | [#등불 - #영사운드(1972년) Covered by sMUSIC#영사운드 #Reinterpreting K…](https://www.youtube.com/watch?v=tW_gZzlbg-4) | sMusic 7080_명… | 7,130 | 1,449,813 | 203.3 | ×550.1 | 8,665.2 | 4.2분 | 2026-05-10 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 없음 | 296/306 |
| 285 | [lock the f*** in. (playlist)](https://www.youtube.com/watch?v=1mAMpmFvceY) | lucent | 7,670 | 1,552,483 | 202.4 | ×218.9 | 23,739.6 | 240분 | 2026-08-19 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 394/424 |
| 286 | [Iske da faniyaar song Slowed + Reverb Lofi Music Mix ∣ Chil…](https://www.youtube.com/watch?v=yoLa1Xlkhvo) | @sanjumusic | 5,440 | 1,081,635 | 198.8 | ×596.9 | 9,758.7 | 5.1분 | 2026-07-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 217/217 |
| 287 | [들꽃처럼 살다가](https://www.youtube.com/watch?v=1vBXiLsHZrs) | 소은뮤직 | 644 | 127,685 | 198.3 | ×587.1 | 1,076.5 | 4.7분 | 2026-06-27 | 기타 | 음악 | 설명 | 108/121 |
| 288 | [☀️ Top Acoustic Love Hits 2026 💚 Relaxing Pop Covers for Pe…](https://www.youtube.com/watch?v=r0t7mEWAGyY) | Acoustic Pulse | 10,100 | 1,998,975 | 197.9 | ×77.9 | 18,801.4 | 51.8분 | 2026-07-10 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 166/181 |
| 289 | [🍉 아침에 커피 마시면서 혼자 듣는데 너무좋다. ∣ 하루 종일 틀어 놓으세요🎵7080추억의 올드팝 #감성팝…](https://www.youtube.com/watch?v=iRAcLZyPbsA) | woozune | 6,000 | 1,185,378 | 197.6 | ×106.5 | 13,410.7 | 74.3분 | 2026-07-27 | 9. 가요·발라드·트로트 | 음악 | 설명 | 187/202 |
| 290 | [Könül Xasıyeva - Yaralayırsan ∣ Piano Version by Xeqan](https://www.youtube.com/watch?v=Fqfo2bGkZik) | Xeqan | 5,780 | 1,125,296 | 194.7 | ×26.8 | 6,478.1 | 5.5분 | 2026-05-03 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 428/433 |
| 291 | [애매모호한 첫사랑](https://www.youtube.com/watch?v=A6rImTTl348) | na tsu | 933 | 181,463 | 194.5 | – | 1,873.3 | 19.3분 | 2026-07-19 | 기타 | 플레이리스트·모음 | 설명 | 419/419 |
| 292 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 듣자마자 흥 폭발하는🔥 최신 K-POP 노래 모음 노동요](https://www.youtube.com/watch?v=yngpCQNKY_M) | 클로버 플레이리스트 | 3,630 | 699,894 | 192.8 | ×10.1 | 5,784.0 | 40.9분 | 2026-06-25 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 69/70 |
| 293 | [일할때 듣기좋은 발라드 추천 광고없는 노래모음 유튜브 베스트곡 TOP BEST 100 임창정,성시경,더원,…](https://www.youtube.com/watch?v=YVeqKohQmuw) | LeafVibe 4K | 1,390 | 266,207 | 191.5 | ×333.2 | 1,990.5 | 71.8분 | 2026-06-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 13/13 |
| 294 | [2026 Ultimate Mind Relaxing Lofi Beats ∣ Study Sleep & Chil…](https://www.youtube.com/watch?v=FYePEj0IZC8) | Ace LoFi | 9,400 | 1,784,648 | 189.9 | ×4,708.8 | 16,897.1 | 28.2분 | 2026-07-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 140/140 |
| 295 | [Navkar mantra's Golden Shield ∣ Feel the Ancient Jain Power…](https://www.youtube.com/watch?v=FEQe99gciwU) | Navkarbhakti … | 4,410 | 837,166 | 189.8 | – | 4,778.2 | 8.1분 | 2026-05-02 | 1. 수면·명상·힐링 | 음악 | 설명 | 197/198 |
| 296 | [ĐẾN KHI NÀO (Hot Trend)...Mặt Trời Ngừng Chiếu ∣ Những Bản …](https://www.youtube.com/watch?v=pB64u5qBd5g) | Chà Là Chill | 38,900 | 7,327,149 | 188.4 | ×59.0 | 138,395.9 | 91.8분 | 2026-09-01 | 8. 로파이·시티팝·칠 | 긴 한 곡·반복 | 설명 | 509/518 |
| 297 | [【洋楽Playlist】何も考えずに聴きたい心地いいChill R&B｜Relax｜Smooth Vibes](https://www.youtube.com/watch?v=6qkUHaRXvtE) | Ethereal TIME | 4,850 | 910,784 | 187.8 | ×430.2 | 7,667.2 | 65.2분 | 2026-06-27 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 63/63 |
| 298 | [🔥 𝗔𝗟𝗟 𝗧𝗥𝗘𝗡𝗗𝗜𝗡𝗚 𝗣𝗔𝗞𝗜𝗦𝗧𝗔𝗡𝗜 𝗦𝗢𝗡𝗚𝗦 🎶 ∣ 𝗩𝗜𝗥𝗔𝗟 𝗛𝗜𝗧𝗦 𝟮𝟬𝟮𝟲 🎧 ∣ 𝗧𝗢𝗣 …](https://www.youtube.com/watch?v=XL5PUUwrztg) | cozi_music | 32,800 | 6,123,748 | 186.7 | ×52.1 | 87,576.5 | 19.6분 | 2026-08-15 | 1. 수면·명상·힐링 | AI 음악 | 설명 | 2,153/2,307 |
| 299 | [아득히 먼 곳 ∣ 이별 감성 발라드 ∣ 커버 노래 편곡 수노 AI](https://www.youtube.com/watch?v=8l6a5DRZqHU) | 엄마의 세월 - 한국 발… | 1,130 | 210,957 | 186.7 | ×412.8 | 1,386.4 | 4분 | 2026-05-25 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 20/20 |
| 300 | [Relax Cha Cha Music 🪘 Havana Cafe Music - Cha Cha Son Cuban…](https://www.youtube.com/watch?v=sUO0XTpAiCY) | Cha Cha Havan… | 1,640 | 305,357 | 186.2 | ×2,212.7 | 2,016.3 | 5.5분 | 2026-05-25 | 4. 카페·매장·라운지 | 음악 | 설명 | 20/20 |
| 301 | [[ 𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕 ] 전남친 잊는 플리](https://www.youtube.com/watch?v=bLYI4NHve9Y) | 아야 | 1,330 | 246,086 | 185.0 | – | 2,935.2 | 17.4분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 없음 | 55/59 |
| 302 | [🎶 2026 Ultimate Mind Relaxing Lofi Beats ∣∣ Study, Sleep & …](https://www.youtube.com/watch?v=453LJJX0ncc) | Hindi Lofi So… | 12,700 | 2,344,100 | 184.6 | ×5,407.4 | 19,831.8 | 30.7분 | 2026-06-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 199/199 |
| 303 | [🌧️ Relaxing Piano & Bird Sounds ∣ Rainy Nature Ambience for…](https://www.youtube.com/watch?v=O0goqFNLWDs) | Solace Birdso… | 1,790 | 329,905 | 184.3 | ×55.0 | 3,555.0 | 92.3분 | 2026-07-23 | 2. 자연 소리·백색소음 | 음악 | 설명 | 223/223 |
| 304 | [Peaceful Piano with Rain Sounds ∣ Relaxing Sleep Music for …](https://www.youtube.com/watch?v=Ral_oDb724k) | Soft Rain Pia… | 2,760 | 504,668 | 182.8 | ×87.1 | 3,803.2 | 47.1분 | 2026-06-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 104/104 |
| 305 | [POV: The ultimate south indian dance🪩 playlist to blast at …](https://www.youtube.com/watch?v=Hh_Vewjk7wo) | Ethereal Echo… | 13,000 | 2,370,406 | 182.3 | ×7.5 | 17,035.2 | 18.6분 | 2026-06-07 | 기타 | 플레이리스트·모음 | 설명 | 299/307 |
| 306 | [♫ 𝗔𝗹𝗹 𝗛𝗶𝗻𝗱𝗶 𝗧𝗿𝗲𝗻𝗱𝗶𝗻𝗴 𝗦𝗼𝗻𝗴𝘀 𝗼𝗳 2026 ♫🎧🤍#HindiSongs#Playlist](https://www.youtube.com/watch?v=eC61t3Nw-vs) | 𝐌𝐚𝐧𝐬𝐢~ | 8,920 | 1,610,914 | 180.6 | ×8.8 | 14,387.3 | 11.9분 | 2026-07-04 | 기타 | 플레이리스트·모음 | 없음 | 506/506 |
| 307 | [Heartbreaking 💔 Lofi Mashup 🎧Slowed +Reverb Songs ∣ Study,F…](https://www.youtube.com/watch?v=mw6hxi9NJwc) | Peaceful Vibe… | 5,320 | 947,226 | 178.1 | ×4,191.3 | 15,292.8 | 7.3분 | 2026-08-23 | 3. 공부·집중·작업 | 음악 | 설명 | 105/109 |
| 308 | [이수연, K-trot, [감성노래 탑7 메들리]](https://www.youtube.com/watch?v=wz-ZkvuAdTg) | 통기타 한석 TV | 2,710 | 480,643 | 177.4 | – | 2,854.7 | 26.3분 | 2026-05-08 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 없음 | 311/323 |
| 309 | [Calm Work Music ∣ High Concentration Music for Studying, Fo…](https://www.youtube.com/watch?v=qXQ6wEipSug) | Calm Work Stu… | 6,110 | 1,080,083 | 176.8 | ×330.0 | 9,925.3 | 130.8분 | 2026-07-07 | 3. 공부·집중·작업 | 음악 | 설명 | 296/318 |
| 310 | [가을이 머무는 호숫가 ∣ 피아노·첼로·바이올린으로 듣는 고요한 클래식](https://www.youtube.com/watch?v=zNMH3ua74tE) | 순례자 우물 | 1,030 | 181,074 | 175.8 | ×511.5 | 3,856.2 | 122분 | 2026-09-07 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 36/41 |
| 311 | [सुनते ही नींद आएगी 😴 ∣ दिव्य निद्रा संगीत ∣ Himalayan Deep …](https://www.youtube.com/watch?v=R_LBzRfzBBo) | Sanatan Bodh | 3,140 | 551,085 | 175.5 | ×1,172.5 | 5,266.8 | 40분 | 2026-07-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 157/158 |
| 312 | [ANDEAN PAN FLUTE 🌿 Gentle Healing Music to Calm the Mind l …](https://www.youtube.com/watch?v=1NjCSdhJnjo) | Ginevra Melod… | 186 | 32,460 | 174.5 | ×108.9 | 1,432.7 | 94.5분 | 2026-10-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 6/6 |
| 313 | [안들으면후회함 playlist](https://www.youtube.com/watch?v=_eAnA8TgKWM) | 서른마흔오백다섯살 | 3,420 | 593,486 | 173.5 | ×66.7 | 4,189.5 | 24분 | 2026-06-04 | 기타 | 플레이리스트·모음 | 없음 | 169/169 |
| 314 | [눈 뜨면 아침인 숲속 평온한 빗소리 ∣ 🌲 깊은 수면을 위한 평온한 백색소음 (Rain Sounds for…](https://www.youtube.com/watch?v=ri10d9TXXGE) | Cozy Rain on … | 3,520 | 605,913 | 172.1 | ×123.8 | 6,009.8 | 210분 | 2026-07-15 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 127/140 |
| 315 | [20 Of The Most Beautiful Classical Adagios for Relaxation a…](https://www.youtube.com/watch?v=t-scHKetq7I) | Classical Ins… | 13,700 | 2,354,595 | 171.9 | ×87.7 | 13,097.2 | 120분 | 2026-04-27 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 946/1,000 |
| 316 | [Spa & Healing Music · 3 Hours 🌺 Luxury Relaxation for Massa…](https://www.youtube.com/watch?v=uzHIWyuadHM) | Halcyon Hours | 364 | 62,073 | 170.5 | ×969.9 | 530.2 | 180분 | 2026-06-29 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 5/5 |
| 317 | [Hindi Lofi Nights ∣ Yeh Tune Kya Kiya x Ishq Risk x Ishq x …](https://www.youtube.com/watch?v=oHrvGKhcW4s) | Songhalo | 11,000 | 1,848,690 | 168.1 | ×22.1 | 10,953.4 | 23.8분 | 2026-05-08 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 907/907 |
| 318 | [Viral OPM Hits 2026 🇵🇭 Trending Tagalog Love Songs 🎧 Spotif…](https://www.youtube.com/watch?v=au1ycoHD9cY) | Calm Guitar | 13,100 | 2,198,329 | 167.8 | ×185.0 | 28,053.4 | 64.6분 | 2026-08-06 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 199/208 |
| 319 | [Relaxing Guzheng & Bamboo Flute 🌸Ancient Chinese Music 🌸 #a…](https://www.youtube.com/watch?v=N4y79JaFBeo) | Yuzira Music | 4,270 | 710,751 | 166.4 | ×2,889.2 | 4,447.3 | 64.1분 | 2026-05-17 | 기타 | 음악 | 설명 | 290/294 |
| 320 | [DIFFERENT ROAD - Melodic Viking Music for Focus & Deep Study](https://www.youtube.com/watch?v=pP54saekswg) | Jonas & Ida | 2,610 | 432,331 | 165.6 | ×142.7 | 4,240.2 | 6.5분 | 2026-07-14 | 3. 공부·집중·작업 | 음악 | 설명 | 87/88 |
| 321 | [Om Shanti Om - Climax BGM ∣ Cineforge Records](https://www.youtube.com/watch?v=eGnTmVPO--k) | Cineforge Rec… | 3,200 | 529,497 | 165.5 | ×60.5 | 3,558.5 | 9.8분 | 2026-05-28 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 111/113 |
| 322 | [살면서 한 번쯤 들어봐야 할 클래식 15곡 ∣ 공부·휴식·카페에서 듣기 좋은 클래식 음악](https://www.youtube.com/watch?v=hDepOWqLbXI) | canvasclassics | 184 | 30,332 | 164.8 | – | 247.0 | 152.1분 | 2026-06-23 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 3/3 |
| 323 | [Playlist ∣ 어때 그 남잔 나보다 더 나?](https://www.youtube.com/watch?v=Eh4ZRMyh8vo) | 안개 | 3,290 | 536,044 | 162.9 | ×16.8 | 4,000.7 | 25.6분 | 2026-06-12 | 기타 | 플레이리스트·모음 | 설명 | 69/70 |
| 324 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 첫 비트부터 심박수 폭발 ❤️ 미친 텐션 운동 플리 ∣ 헬스 · 러닝 · EDM · 힙…](https://www.youtube.com/watch?v=XrUNOYMFd58) | Grind Vibe | 5,840 | 951,191 | 162.9 | ×138.4 | 7,048.2 | 80.7분 | 2026-06-11 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 337/344 |
| 325 | [새벽 2시~4시 재입면 음악 ∣ 생각 멈추고 다시 잠드는 BGM [중간광고없음]](https://www.youtube.com/watch?v=KBdCHv2UpRU) | 단잠TV | 2,740 | 444,432 | 162.2 | ×632.2 | 2,730.3 | 191.6분 | 2026-05-14 | 2. 자연 소리·백색소음 | 음악 | 설명 | 62/62 |
| 326 | [99% DEEP SLEEP in 3 Minutes (NO ADS) • Brain Massage While …](https://www.youtube.com/watch?v=ZqzEQHOrvPw) | Awakened Soul | 5,080 | 816,096 | 160.7 | ×393.9 | 24,897.1 | 711분 | 2026-09-21 | 1. 수면·명상·힐링 | 음악 | 설명 | 439/462 |
| 327 | [#장터에핀작은꽃#인생트로트#감성트로트#눈물나는노래#가족사랑#엄마생각#할머니사랑#추억의노래#7080감성#중년…](https://www.youtube.com/watch?v=U-J6pNop1bU) | 인생 감성 트롯트노래 | 1,800 | 286,757 | 159.3 | ×508.4 | 2,681.4 | 4.8분 | 2026-07-09 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 18/18 |
| 328 | [[90 Phút Lạc Trong Không Gian Huyền Ảo] Mixset Chillout Hoà…](https://www.youtube.com/watch?v=5BxoSQw9tOo) | Bee Chill | 8,860 | 1,403,296 | 158.4 | ×13.7 | 18,237.5 | 92.3분 | 2026-08-08 | 8. 로파이·시티팝·칠 | 긴 한 곡·반복 | 설명 | 115/119 |
| 329 | [노래방차트 발라드 2026년 7월 1차 🎤 최신 인기차트 노래모음 ∣ 발라드 플레이리스트](https://www.youtube.com/watch?v=uedFUZ1kMjk) | 오늘의 음악 | 1,150 | 181,042 | 157.4 | ×415.2 | 2,545.9 | 83.2분 | 2026-08-14 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 8/9 |
| 330 | [Back To Chennai – Chennai Express Theme Music ∣ Shah Rukh K…](https://www.youtube.com/watch?v=g40bXb0KIFs) | Octave Valley | 1,410 | 221,256 | 156.9 | ×35.0 | 1,324.5 | 13.6분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 39/41 |
| 331 | [5 Minute Deep Meditation Music for Positive Energy • Relax …](https://www.youtube.com/watch?v=6-FPw2wSYsw) | Christmas Hav… | 289 | 45,310 | 156.8 | ×57.3 | 307.7 | 5.3분 | 2026-05-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 5/5 |
| 332 | [Könül Xasıyeva - Sən Məndən Xəbərsiz ∣ Piano Version by Xeq…](https://www.youtube.com/watch?v=ECMO19Ykny4) | Xeqan | 5,780 | 894,419 | 154.7 | ×21.3 | 5,273.3 | 6.1분 | 2026-05-07 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 379/382 |
| 333 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 야르한 제이팝](https://www.youtube.com/watch?v=3QaZldwEZ3g) | 탱이 | 1,700 | 262,193 | 154.2 | ×25.2 | 1,974.8 | 18.3분 | 2026-06-13 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 59/59 |
| 334 | [얼마나 들었는지 감도 안 옴](https://www.youtube.com/watch?v=1vELYr_nSxI) | shhh... | 7,660 | 1,179,321 | 154.0 | ×267.2 | 19,526.7 | 24.8분 | 2026-08-24 | 기타 | 음악 | 설명 | 169/174 |
| 335 | [Good Morning Vibes 💕 Best Acoustic Love Songs to Start Your…](https://www.youtube.com/watch?v=fxrrC6UCItY) | NiceOne | 11,500 | 1,769,486 | 153.9 | ×933.5 | 25,137.0 | 91.9분 | 2026-08-14 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 | 146/149 |
| 336 | [HEART BREAK 💔 SAD 😭 LOFI MASHUP ∣∣ HEART BROKEN 💔 HINDI SON…](https://www.youtube.com/watch?v=rXZRZ5z0Oqo) | Adnan Official | 10,000 | 1,535,644 | 153.6 | ×14,218.9 | 10,872.8 | 18.8분 | 2026-06-05 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 107/107 |
| 337 | [💃🔥𝐀 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐓𝐡𝐚𝐭 𝐖𝐢𝐥𝐥 𝐖𝐚𝐤𝐞 𝐔𝐩 𝐘𝐨𝐮𝐫 𝐈𝐧𝐧𝐞𝐫 𝐃𝐚𝐧𝐜𝐞𝐫 🎶⚡{+timest…](https://www.youtube.com/watch?v=ASY7vTTB-wo) | 𝙏𝙖𝙣𝙭 𝙀𝙙𝙞𝙩𝙯 🦋 | 14,300 | 2,184,504 | 152.8 | ×10.2 | 15,617.9 | 14.5분 | 2026-06-06 | 기타 | 플레이리스트·모음 | 설명 | 281/286 |
| 338 | [Mind Relaxing Flute Tabla and Sitar ∣ Hindustani Instrument…](https://www.youtube.com/watch?v=ZHwM82TaZFg) | Mystic Sitar | 2,540 | 385,120 | 151.6 | ×224.3 | 2,203.2 | 71.2분 | 2026-05-02 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 87/88 |
| 339 | [THE ULTIMATE HARYANVI PLAYLIST 🔥 !! #playlist #haryanvisong…](https://www.youtube.com/watch?v=SoVJljRBGMw) | 𐙚 𝒦𝒽𝓊𝓈𝒽𝒷𝓊𝓊 | 20,400 | 3,082,159 | 151.1 | ×6.0 | 26,775.6 | 6.9분 | 2026-07-01 | 기타 | 플레이리스트·모음 | 설명 | 305/309 |
| 340 | [Enigma - Eternity of Love (Enigmatic Ambient / New Age 4K)](https://www.youtube.com/watch?v=2ohn3S5VafQ) | 5TH FREQUENCY | 1,040 | 156,958 | 150.9 | ×184.0 | 2,243.8 | 5.4분 | 2026-08-15 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 60/60 |
| 341 | [바흐의 파사칼리아](https://www.youtube.com/watch?v=MQf3ajxEFfQ) | 홍준 뮤직 TV | 4,600 | 692,406 | 150.5 | ×1,271.6 | 5,043.9 | 40분 | 2026-06-09 | 기타 | 정보·해설 | 설명 | 662/675 |
| 342 | [Coffee Shop Love Songs ∣ Relaxing Acoustic 70s 80s 90s Coll…](https://www.youtube.com/watch?v=p4zynVVTYpA) | Acoustic Memo… | 10,000 | 1,503,013 | 150.3 | ×40.6 | 51,243.0 | 80.3분 | 2026-09-24 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 130/141 |
| 343 | [SONGS THAT’LL MAKE YOU DANCE AT 3AM ✨🔥 FT. DESI SONGS ❤️‍🔥💋…](https://www.youtube.com/watch?v=oIXkjb_FPC4) | Dramanique⋆.𐙚… | 32,400 | 4,861,681 | 150.1 | ×10.3 | 29,849.7 | 29.3분 | 2026-05-14 | 기타 | 음악 | 설명 | 746/752 |
| 344 | [Peaceful Autumn Escape 🍂 Colorful Forest Scenery with Natur…](https://www.youtube.com/watch?v=kpm3m2Afk18) | Gentle Nature… | 5,840 | 875,819 | 150.0 | ×40.7 | 10,564.3 | 142.2분 | 2026-08-02 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 143/145 |
| 345 | [[Playlist] ENHYPEN (엔하이픈)-'THE SIN : BLISS'丨2026 Full Album](https://www.youtube.com/watch?v=kG-CrsJXx5w) | κööκκ | 1,960 | 293,104 | 149.5 | ×74.4 | 4,592.6 | 15.9분 | 2026-08-21 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 240/243 |
| 346 | [[기절수면/중간광고없음] 10분후 검은화면/ 듣자마자 잠드는 대나무숲 빗소리 🌧️잎 끝에 떨어지는 편안한 …](https://www.youtube.com/watch?v=l89z7BzLSmI) | 신가네숲 빗소리 | 1,450 | 216,396 | 149.2 | ×32.7 | 1,854.4 | 420분 | 2026-06-29 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 41/41 |
| 347 | [김동률 명곡 모음 🎵 베스트 발라드 20곡 연속듣기 ∣ 다시 사랑한다 말할까 · 감사 · 기억의 습작 ∣ …](https://www.youtube.com/watch?v=9kIULv7grWs) | 노래모음 | 2,190 | 326,395 | 149.0 | – | 2,313.9 | 75.3분 | 2026-06-05 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 49/49 |
| 348 | [playlist ∣ 우리 사랑은 필름 같았으면 해요](https://www.youtube.com/watch?v=k8giKQV4a40) | 웨일 | 3,410 | 506,943 | 148.7 | ×30.1 | 3,703.8 | 21.5분 | 2026-06-09 | 기타 | 플레이리스트·모음 | 없음 | 58/60 |
| 349 | [Hanuman Chalisa 🔥 Listen Can Change Your Energy ∣ Peace, Po…](https://www.youtube.com/watch?v=v7ezfXE074I) | bhakti offici… | 5,000 | 743,174 | 148.6 | ×1,997.8 | 4,326.2 | 6.7분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 582/588 |
| 350 | [Zen Flute Therapy 🎶 ∣ Dopamine Reset Music for Stress & Anx…](https://www.youtube.com/watch?v=ldZHxztiahU) | Osen Moonlight | 11,800 | 1,745,825 | 147.9 | ×536.1 | 23,346.5 | 113.8분 | 2026-08-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 444/488 |
| 351 | [If You Feel It in Your Blood… You’re a Viking ⚔️ ∣ Valhalla…](https://www.youtube.com/watch?v=uPK4MWJvxMk) | Viking Army | 9,580 | 1,406,242 | 146.8 | ×1,407.6 | 7,822.1 | 9.2분 | 2026-04-27 | 13. OST·사운드트랙 | 음악 | 설명 | 587/595 |
| 352 | [[스페인 감성] "Hermano Sócrates ∣ 테스형 - 나훈아 " Korean OldPop 한국명곡](https://www.youtube.com/watch?v=FMwiMkgcfW8) | 스페인 감성 한국 올드송 | 1,680 | 246,535 | 146.8 | ×6.5 | 9,985.1 | 5.1분 | 2026-09-29 | 12. 커버·노래 부르기 | 음악 | 설명 | 68/73 |
| 353 | [Happy Morning Jazz 🎶 January Bossa Nova Instrumental and Re…](https://www.youtube.com/watch?v=qZjNyrGF4pk) | FunToon Rhymes | 12,300 | 1,795,867 | 146.0 | ×213.0 | 99,793.3 | 15.4분 | 2026-10-06 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 0/0 |
| 354 | [𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 ∣ 일할때 틀어놓기 좋은 지브리 x 픽사 x 디즈니 재즈🔥🎺 ∣ #NoAImusic ∣ G…](https://www.youtube.com/watch?v=ayKr-gtJQIQ) | 오늘은 재즈데이 ∣ Ja… | 3,430 | 500,472 | 145.9 | ×487.3 | 3,616.0 | 379.1분 | 2026-06-07 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 40/41 |
| 355 | [@노노뮤직#피아노연주곡 #플루트연주곡#명상음악 #휴식음악 #뉴에이지 #감성음악 #숲길 #자연음악 #마음치유…](https://www.youtube.com/watch?v=8Fiore1srWM) | 노노스튜디오 | 462 | 67,283 | 145.6 | ×423.2 | 470.7 | 32.1분 | 2026-06-03 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 11/11 |
| 356 | [Disney Sleep Piano Collection 🧜‍♀️ ∣ Ariel’s Peaceful Night…](https://www.youtube.com/watch?v=kPPtBzS0hbE) | Fairy Door | 1,920 | 279,322 | 145.5 | ×40.6 | 3,214.9 | 196.9분 | 2026-07-29 | 2. 자연 소리·백색소음 | 커버·직접 부른 노래 | 설명 | 26/26 |
| 357 | [【靜謐時光】 古箏竹笛療癒音樂｜超好聽的中國古典音樂 古箏、琵琶、竹笛、二胡｜療癒音樂 深度睡眠 - Chinese …](https://www.youtube.com/watch?v=7QV9JIx-euE) | Gentle Zen Me… | 9,740 | 1,401,913 | 143.9 | ×670.0 | 8,825.3 | 232분 | 2026-05-18 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,844/2,906 |
| 358 | [POV: You found the ultimate South Indian aesthetic🪷 playlis…](https://www.youtube.com/watch?v=oQz6Wt4qb3w) | Ethereal Echo… | 13,000 | 1,859,223 | 143.0 | ×5.9 | 12,222.8 | 13.3분 | 2026-05-25 | 기타 | 플레이리스트·모음 | 설명 | 356/358 |
| 359 | [A CHATPATI PLAYLIST FOR CHATPATE PEOPLE 💅😜 #playlist #song …](https://www.youtube.com/watch?v=H0yLhDLJWuI) | 𐙚 𝒦𝒽𝓊𝓈𝒽𝒷𝓊𝓊 | 20,400 | 2,899,206 | 142.1 | ×5.7 | 26,641.0 | 11.2분 | 2026-07-07 | 기타 | 플레이리스트·모음 | 설명 | 300/306 |
| 360 | [Eldorado — Hypnotic Dream Trance & Tribal Ambient Music👑✨](https://www.youtube.com/watch?v=ggbo8YTXRrw) | ARTechnoMusic | 3,810 | 540,130 | 141.8 | ×34.8 | 5,210.0 | 5.8분 | 2026-07-12 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 69/69 |
| 361 | [মন ছুঁয়ে যাওয়া বাংলা Lo-Fi Romantic Songs ∣ Relaxing Bangla…](https://www.youtube.com/watch?v=rwiGXAhqrfU) | RESHMI LO-FI … | 24,000 | 3,389,111 | 141.2 | ×756.7 | 19,688.9 | 22.5분 | 2026-05-05 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 989/990 |
| 362 | [Le Café de Minuit 🇫🇷 Une Chanson Romantique Inspirée par le…](https://www.youtube.com/watch?v=D4-ltf3Tdh8) | Bistrot de Mi… | 3,490 | 491,342 | 140.8 | ×1,142.7 | 3,612.0 | 5.9분 | 2026-06-10 | 4. 카페·매장·라운지 | 음악 | 설명 | 101/102 |
| 363 | [Relaxing Jazz Saxophone instrument Relax & Slow Down 🌿 Soft…](https://www.youtube.com/watch?v=AaXKINtzSGI) | Peaceful Sax … | 13,900 | 1,955,651 | 140.7 | ×638.5 | 13,327.5 | 69.9분 | 2026-05-30 | 7. 재즈·보사노바 | 음악 | 설명 | 394/395 |
| 364 | [Deep Sleep & Chill Lofi : Bhojpuri Slowed & Reverb Songs 🎧✨…](https://www.youtube.com/watch?v=zW8T1B9Fzd0) | VLOGDIPESH | 5,220 | 732,679 | 140.4 | ×4,950.5 | 45,356.6 | 17.1분 | 2026-10-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 33/33 |
| 365 | [Shri Krishna Govind Hare Murari - Non Stop Krishna Bhajans …](https://www.youtube.com/watch?v=yl8by0hGZKE) | Hare Murare M… | 22,600 | 3,140,089 | 138.9 | ×1,102.0 | 21,304.1 | 59.2분 | 2026-05-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 419/426 |
| 366 | [Sleep & Reset Your Vagus Nerve ∣ Singing Bowl Sound Bath Me…](https://www.youtube.com/watch?v=l91ztcnXYPM) | Echo Bowls | 543 | 75,141 | 138.4 | ×995.2 | 685.8 | 15.3분 | 2026-07-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 13/17 |
| 367 | [Jo Tere Sang KaTi RaTe 💔 Lofi Remix ∣ Emotional Slowed + Re…](https://www.youtube.com/watch?v=XKcT9t0tgbY) | Abidpro | 46,100 | 6,368,010 | 138.1 | ×1,134.4 | 40,349.7 | 6.3분 | 2026-05-19 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 809/811 |
| 368 | [Positive Jazz Music ☕ Bossa Nova instrumental for Stress Re…](https://www.youtube.com/watch?v=T2HdICk7_6M) | Golden Roast … | 11,300 | 1,558,995 | 138.0 | ×1,309.0 | 10,979.8 | 71.2분 | 2026-06-04 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 235/245 |
| 369 | [[playlist] skrrrr….](https://www.youtube.com/watch?v=20mvF_OP0FY) | le | 12,600 | 1,736,236 | 137.8 | ×40.5 | 9,862.3 | 26.1분 | 2026-05-01 | 기타 | 플레이리스트·모음 | 없음 | 276/285 |
| 370 | [music that will get you to flowstate.](https://www.youtube.com/watch?v=72YoraTjNI0) | Pure Grit Stu… | 20,700 | 2,850,510 | 137.7 | ×137.1 | 27,544.6 | 145.4분 | 2026-07-12 | 기타 | 음악 | 설명 | 1,503/1,520 |
| 371 | [Calm Work Music ∣ Ambient Deep Work for Focus, Productivity…](https://www.youtube.com/watch?v=PBwiQgdwJdc) | Calm Work Stu… | 6,110 | 839,191 | 137.3 | ×256.4 | 7,641.5 | 130.2분 | 2026-07-06 | 3. 공부·집중·작업 | 음악 | 설명 | 202/204 |
| 372 | [𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 요즘 인스타 부계 감성](https://www.youtube.com/watch?v=WBabiGZluh8) | 알수없는 사용자 | 1,810 | 247,092 | 136.5 | ×6.8 | 3,138.6 | 17.5분 | 2026-08-06 | 기타 | 플레이리스트·모음 | 설명 | 52/53 |
| 373 | [Midnight in Beirut 🌙 ∣ Lebanese Jazz & Oud Melodies for Rel…](https://www.youtube.com/watch?v=pdSDzQVDYXk) | Arabic Jazz L… | 17,900 | 2,435,920 | 136.1 | ×1,139.9 | 14,000.6 | 25.3분 | 2026-05-03 | 3. 공부·집중·작업 | 음악 | 설명 | 767/771 |
| 374 | [Fall Into Sleep Instantly • Healing Stress, Anxiety, and De…](https://www.youtube.com/watch?v=ZIGKQlrOEV0) | Brainwave Res… | 14,200 | 1,931,860 | 136.1 | ×3,002.1 | 13,091.1 | 480분 | 2026-05-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,028/1,035 |
| 375 | [Relax in Bikini Bottom 🛟 Calming Tropical Music 🌊 ∣ SpongeB…](https://www.youtube.com/watch?v=US8lFJPAWR0) | Vynture | 4,260 | 579,393 | 136.0 | ×458.0 | 6,256.8 | 249.3분 | 2026-07-23 | 1. 수면·명상·힐링 | 음악 | 설명 | 160/165 |
| 376 | [재생하자마자 텐션 터지는 2026 남녀돌 믹스업 (과제, 청소, 운동할 때 듣는 플리)](https://www.youtube.com/watch?v=x09m3Lgzc-A) | MxJin06 | 5,060 | 685,395 | 135.4 | ×10.4 | 8,065.7 | 99.2분 | 2026-07-31 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 없음 | 30/30 |
| 377 | [🎶Mind and body healing Music ∣ Bansuri flute + Esraj ∣ 1 ho…](https://www.youtube.com/watch?v=l1DL2JWYcyA) | Indian-Soulsc… | 279 | 37,658 | 135.0 | ×214.0 | 304.7 | 61.4분 | 2026-06-22 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 10/10 |
| 378 | [💖💖💖The Café by the Sea©](https://www.youtube.com/watch?v=7jPXHB9Ohus) | M's Music Lou… | 2,070 | 278,621 | 134.6 | ×1,243.8 | 2,197.1 | 4.2분 | 2026-06-19 | 4. 카페·매장·라운지 | 음악 | 설명 | 195/198 |
| 379 | [বিধি এমন ভাগ্য কেন দিলা ∣ Bidhi Amon Vaggo Keno Dila ∣ Bang…](https://www.youtube.com/watch?v=PGkwfiSxmJU) | আঁখি Lo-Fi | 11,900 | 1,593,972 | 133.9 | ×256.7 | 15,522.7 | 13.8분 | 2026-07-13 | 기타 | 음악 | 설명 | 194/195 |
| 380 | [[playlist] 내 주위는 온통 lovely day](https://www.youtube.com/watch?v=m-xuokRyfvQ) | 지륭 | 1,220 | 163,269 | 133.8 | ×5.6 | 971.4 | 19.9분 | 2026-05-09 | 기타 | 플레이리스트·모음 | 없음 | 20/20 |
| 381 | [Autumn Morning Jazz In A Cozy Garden Lounge ∣ Gentle Piano …](https://www.youtube.com/watch?v=tiqZDLIBbHg) | Indoor Jazz M… | 5,400 | 722,651 | 133.8 | ×388.9 | 10,340.9 | 207.9분 | 2026-08-15 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 120/120 |
| 382 | [Hanuman Chalisa for Deep Sleep ∣ Divine Protection for Peac…](https://www.youtube.com/watch?v=XKK7ewgprws) | Inner Bhakti | 7,410 | 989,563 | 133.5 | – | 10,020.3 | 114.8분 | 2026-07-17 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 156/165 |
| 383 | [Deep Focus Music – Flow State for Study & Work](https://www.youtube.com/watch?v=9xYZzgG2EuI) | Deep365 | 4,180 | 557,546 | 133.4 | ×138.6 | 5,127.5 | 63.7분 | 2026-07-07 | 3. 공부·집중·작업 | 음악 | 설명 | 150/150 |
| 384 | [Bangla Old Is Gold Romantic Song ∣ Bangla Lo-Fi ∣ 1970-1990…](https://www.youtube.com/watch?v=OP2DddRRTKI) | Moner Tune | 24,300 | 3,239,860 | 133.3 | ×251.2 | 22,540.1 | 15.8분 | 2026-06-02 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 313/314 |
| 385 | [Thankful Hearts ∣ Gratitude Sing Along Song with Lyrics 💗](https://www.youtube.com/watch?v=K-c4pzbzBzE) | Purely Positi… | 285 | 37,840 | 132.8 | ×234.3 | 631.7 | 4.5분 | 2026-08-25 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 21/26 |
| 386 | [[空靈鼓療癒音樂🎶]｜放鬆、舒壓、冥想、安眠｜Steel Tongue Drum Healing Music｜SUNO…](https://www.youtube.com/watch?v=a_8Hi2u43Q4) | AIMF Music Fa… | 1,250 | 165,677 | 132.5 | ×980.3 | 1,215.7 | 93.1분 | 2026-06-10 | 1. 수면·명상·힐링 | AI 음악 | 설명 | 12/12 |
| 387 | [Sholey Title Music ∣ Music Maker Abani ∣ Instrumental Cover](https://www.youtube.com/watch?v=ajRxp64xcN8) | MUSIC MAKER A… | 5,850 | 775,285 | 132.5 | – | 6,478.7 | 4.7분 | 2026-06-26 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 1,423/1,433 |
| 388 | [Playlist ∣ 틀어놓으면 그냥 계속 리듬 타게 되는 그루브 😎 집중 끊기지 않는 리듬 🎧 ∣ JAZZ…](https://www.youtube.com/watch?v=wsB8ej3Jon4) | Hush Chords | 19,900 | 2,624,028 | 131.9 | ×511.7 | 15,769.1 | 318.1분 | 2026-05-10 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 722/730 |
| 389 | [99% Fall Into Sleep Instantly (No Ads) • Eliminate Stress &…](https://www.youtube.com/watch?v=iVZPLhAlXUw) | Bedtime Calm … | 12,600 | 1,659,599 | 131.7 | ×256.3 | 30,955.5 | 237.9분 | 2026-08-31 | 1. 수면·명상·힐링 | 음악 | 설명 | 43/43 |
| 390 | [자비의 빛, 신묘장구대다라니](https://www.youtube.com/watch?v=oZyrd47zI6o) | 부다야나마하 | 3,160 | 415,249 | 131.4 | ×276.6 | 5,278.2 | 6.6분 | 2026-08-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 228/238 |
| 391 | [choose peace](https://www.youtube.com/watch?v=eIY-Pgg-b1E) | sleepwalker | 14,600 | 1,914,197 | 131.1 | ×169.2 | 11,015.2 | 60분 | 2026-05-03 | 기타 | 긴 한 곡·반복 | 설명 | 1,135/1,154 |
| 392 | [Cortisol Reset । 432Hz Krishna Bansuri Therapy for a Calm M…](https://www.youtube.com/watch?v=D5NHvEVAbWY) | Healing Raga … | 24,500 | 3,206,842 | 130.9 | ×231.9 | 33,110.8 | 65.7분 | 2026-07-19 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,970/2,039 |
| 393 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 듣자마자 텐션 업🔥K-POP 여돌 노래 모음 노동요](https://www.youtube.com/watch?v=xtfreKB54KQ) | 클로버 플레이리스트 | 3,630 | 472,537 | 130.2 | ×6.8 | 4,058.0 | 53분 | 2026-06-29 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 39/39 |
| 394 | [hard work pays off, let's be productive (focus playlist to …](https://www.youtube.com/watch?v=IS6yiMGlYkE) | taami study. | 9,960 | 1,290,439 | 129.6 | ×165.3 | 11,968.4 | 189.8분 | 2026-07-08 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 196/198 |
| 395 | [Best Morning Powerful Mantras ∣ Shiva, Ganesh, Hanuman, Vis…](https://www.youtube.com/watch?v=CFV27iuas7Q) | Sacred Naad | 22,300 | 2,856,394 | 128.1 | ×3,517.7 | 40,073.4 | 15.7분 | 2026-08-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 973/1,034 |
| 396 | [TANGGAL STRESS MO DITO 🔥🎶 ∣ DUB REGGAE MIX 🎶🔥🇵🇭](https://www.youtube.com/watch?v=0m7BLfBl2f8) | RELAX REGGAE … | 13,800 | 1,766,286 | 128.0 | ×1,903.3 | 23,231.8 | 74.8분 | 2026-08-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 256/261 |
| 397 | [📝 1 HOUR OF FOCUS ∣ 🌧️ Relaxing Piano & Rain Sounds for Stu…](https://www.youtube.com/watch?v=yMcznSINsFs) | Melodies of C… | 4,970 | 636,072 | 128.0 | ×51.6 | 7,319.3 | 60.4분 | 2026-07-29 | 2. 자연 소리·백색소음 | 긴 한 곡·반복 | 설명 | 152/170 |
| 398 | [Không Buông x Từng Là Của Nhau x Tìm Em - HNGLE x BẢO ANH ∣…](https://www.youtube.com/watch?v=wVLhvXB2flE) | Chà Là Chill | 38,900 | 4,959,526 | 127.5 | ×37.0 | 51,695.0 | 91.8분 | 2026-07-20 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 609/614 |
| 399 | [𝙿𝚕𝚊𝚢𝚕𝚒𝚜𝚝 중국 가오 노래들](https://www.youtube.com/watch?v=-h0dUUluarY) | 진구달려 | 6,350 | 807,698 | 127.2 | ×16.1 | 16,378.6 | 14.1분 | 2026-09-05 | 기타 | 플레이리스트·모음 | 없음 | 225/263 |
| 400 | [RUMI ∣ If You Want to Let Go of the Pain, Listen to This ∣ …](https://www.youtube.com/watch?v=p4VN5_1HW20) | Rumi Mystic S… | 1,440 | 181,630 | 126.1 | ×118.5 | 3,735.5 | 26.1분 | 2026-09-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 56/75 |
| 401 | [김상민 – YOU (2001) ∣ 폭발적인 고음의 여자 보컬 리메이크/커버 2 Keys+](https://www.youtube.com/watch?v=-GVdD_Onszw) | AuraAPT | 14,300 | 1,801,600 | 126.0 | ×107.2 | 20,275.9 | 4.1분 | 2026-07-27 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 269/290 |
| 402 | [🎵 전체듣기 ∣ 에헤야~ 막걸리 한 잔 하세 🍶 ∣힐링 국악](https://www.youtube.com/watch?v=KYXF2WEd2Ew) | 에헤라디여 5060 | 358 | 45,092 | 126.0 | ×120.6 | 320.1 | 4.2분 | 2026-06-05 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 30/30 |
| 403 | [당신의 피아노 레벨은? (Lv.1~Lv.8 + 라캄파넬라) ∣ What is your Piano Level…](https://www.youtube.com/watch?v=1E5Zi3Gs1ys) | Bony_Musician | 674 | 84,463 | 125.3 | – | 603.1 | 6.5분 | 2026-06-06 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 340/340 |
| 404 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 비에 젖은 와인향](https://www.youtube.com/watch?v=Pt3nGKCTF2U) | 유월 | 3,850 | 482,305 | 125.3 | ×13.9 | 3,329.4 | 21.1분 | 2026-06-01 | 기타 | 플레이리스트·모음 | 설명 | 124/124 |
| 405 | [Happy Morning Jazz 🎶 January Bossa Nova Instrumental and Re…](https://www.youtube.com/watch?v=cwBj4t1V_FY) | Little Masti … | 12,500 | 1,561,690 | 124.9 | ×38.7 | 62,869.3 | 14.5분 | 2026-09-29 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 0/0 |
| 406 | [NAAD ∣ Powerful Instrumental Invocation #SpiritualMusic #Dr…](https://www.youtube.com/watch?v=bc4vTfxeLZk) | shivam sarasw… | 3,380 | 417,262 | 123.5 | ×1,506.4 | 2,833.6 | 7.9분 | 2026-05-30 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 60/60 |
| 407 | [Without You Lord, I Am Nothing ∣ Inspirational Christian Wo…](https://www.youtube.com/watch?v=4TI0GkgfvKk) | Music of Faith | 28,000 | 3,447,955 | 123.1 | ×739.3 | 21,871.7 | 6분 | 2026-05-19 | 15. CCM·찬양·국악… | 음악 | 설명 | 2,138/2,153 |
| 408 | [Happy Jazz Music ☕ Bossa Nova background for Relaxing, Grea…](https://www.youtube.com/watch?v=YTpDlQvvT3Q) | Golden Roast … | 11,300 | 1,390,352 | 123.0 | ×1,167.4 | 8,456.9 | 70.6분 | 2026-05-12 | 7. 재즈·보사노바 | 음악 | 설명 | 189/199 |
| 409 | [My Soundscape for Sleeping at the Edge of the Universe](https://www.youtube.com/watch?v=fsxvm6W4EoY) | Polarity Ambi… | 8,820 | 1,078,418 | 122.3 | ×151.4 | 9,754.6 | 35.9분 | 2026-07-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 884/895 |
| 410 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 그냥 네 눈동자가 예뻤어](https://www.youtube.com/watch?v=FOjiqNxjDDw) | 유월 | 3,850 | 469,822 | 122.0 | ×13.5 | 2,958.2 | 21.9분 | 2026-05-18 | 기타 | 플레이리스트·모음 | 설명 | 67/67 |
| 411 | [Nhạc không lời Piano & Mưa Vol.1 ∣ Piano Thư Giãn, Học Bài,…](https://www.youtube.com/watch?v=tddKxQYCNlM) | Trí Nhật Piano | 8,790 | 1,064,931 | 121.2 | ×380.3 | 6,579.3 | 123분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 250/257 |
| 412 | [지금 다시 들어도 좋은 2000년대 명곡 모음 (SG워너비·티아라·씨야) 🎧 그 시절 우리가 사랑했던 노래…](https://www.youtube.com/watch?v=vBIWuORF8vI) | 그때 그 가락 | 3,100 | 373,194 | 120.4 | ×6.4 | 21,391.7 | 101.5분 | 2026-10-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 40/68 |
| 413 | [Relax Your Mind with Tabla & Bansuri Meditation Music ∣ Dee…](https://www.youtube.com/watch?v=OU-pcEjsoxs) | Raga Instrume… | 3,750 | 449,097 | 119.8 | ×2,789.4 | 2,708.5 | 93.3분 | 2026-05-11 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 138/138 |
| 414 | [Sarap Sa Tenga To VOL. 3 🌿(IBA TO!) ∣ Spiritual Roots Regga…](https://www.youtube.com/watch?v=9w_QNH2ju3A) | Just Reggae S… | 46,000 | 5,451,886 | 118.5 | ×276.8 | 32,853.5 | 64.6분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,674/2,673 |
| 415 | [If You Feel Stressed, Listen to This ∣ Deep Sufi Healing Mu…](https://www.youtube.com/watch?v=tGNczX2LApU) | Rumi Mystic S… | 1,440 | 169,439 | 117.7 | ×110.5 | 3,658.0 | 30.2분 | 2026-09-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 25/26 |
| 416 | [쇼팽, 첼로로 물들다 ∣ 피아노와 첼로로 듣는 녹턴의 밤 (Chopin for Cello & Piano)](https://www.youtube.com/watch?v=HV7WBsQq-Ms) | EmberClassic | 4,960 | 582,204 | 117.4 | ×108.3 | 6,091.9 | 71.3분 | 2026-07-20 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 170/173 |
| 417 | [Greatest Classic Reggae Old Songs 70s-90s 🌴 RIVERS OF BABYL…](https://www.youtube.com/watch?v=1MPtYI4ExEo) | Zee | 11,600 | 1,360,553 | 117.3 | ×155.2 | 18,791.2 | 57.4분 | 2026-08-12 | 12. 커버·노래 부르기 | 플레이리스트·모음 | 설명 | 129/133 |
| 418 | [Music to Rest Your Mind.](https://www.youtube.com/watch?v=-igpcHqULS0) | dark serenity… | 6,690 | 784,266 | 117.2 | ×95.6 | 4,787.3 | 57.3분 | 2026-05-13 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 241/245 |
| 419 | [듣자 마자 바로 잠드는 숲속 시원한 빗소리 ASMR (Rain Sounds), 불면증 완화, 힐링 빗소리](https://www.youtube.com/watch?v=berSZ8YAKP8) | Cozy Rain on … | 3,520 | 412,131 | 117.1 | ×84.2 | 2,865.8 | 180분 | 2026-06-02 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 144/144 |
| 420 | [{playlist} 할렐야루한 노래만 갖고옴...](https://www.youtube.com/watch?v=cnBMqI-z8q8) | 밤티플리 | 1,270 | 147,912 | 116.5 | ×27.4 | 1,007.7 | 18.8분 | 2026-05-30 | 기타 | 플레이리스트·모음 | 없음 | 30/30 |
| 421 | [【心整うBGM】聴くだけで疲れた一日がふっと和らぐ音楽✨｜心ほどけるピアノ２時間🌙｜作業,読書,睡眠用 / Sooth…](https://www.youtube.com/watch?v=-MEjaHzrcuU) | Kigokoro Café… | 6,520 | 749,418 | 114.9 | ×280.4 | 4,780.5 | 132.3분 | 2026-05-20 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 102/105 |
| 422 | [Dopamine Music 🎶 Peaceful Bansuri & Tabla Instrumental ∣ Me…](https://www.youtube.com/watch?v=6HPjmWDf0Q8) | KrishxBeats | 12,100 | 1,388,760 | 114.8 | ×737.5 | 18,109.9 | 27.9분 | 2026-08-08 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 646/664 |
| 423 | [🌸New Trending Acoustic Love Songs 2026 Cover🎧Best Trending …](https://www.youtube.com/watch?v=58xMPYKYcPg) | Calm Strings | 7,090 | 811,744 | 114.5 | ×111.5 | 8,602.4 | 49.7분 | 2026-07-21 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 103/107 |
| 424 | [나무에 내리는 부드러운 빗소리/ 듣자마자 기절수면 나무 빗소리/ 이명 치료 효과/ 빗소리 1시간/ 5분후 …](https://www.youtube.com/watch?v=otpGN7l-8mo) | 아늑한 빗소리 - Coz… | 4,320 | 492,612 | 114.0 | ×50.9 | 5,869.7 | 64분 | 2026-08-01 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 34/34 |
| 425 | [Anirudh's new 2026 Mass songs ∣ Best Anirudh Songs #trending](https://www.youtube.com/watch?v=NV2bXZ4H4gA) | Musical Haven | 2,090 | 237,317 | 113.5 | – | 1,829.7 | 16.7분 | 2026-06-16 | 기타 | 음악 | 설명 | 15/16 |
| 426 | [[𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩]🔥달려보자 2010년 아이돌 띵곡 노동요 모음.zip 플레이리스트💿](https://www.youtube.com/watch?v=_zFB1047_Ek) | 이꿈치 | 1,330 | 150,896 | 113.5 | ×4.5 | 1,713.3 | 73.5분 | 2026-07-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 20/20 |
| 427 | [⟨𝐜𝐚𝐟𝐞 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓⟩🩵맑은 초여름의 어느 날, 카페 피아노 10시간 [중간광고없음] ∣ 작업·공부·…](https://www.youtube.com/watch?v=nm_Mh-VIWvY) | Daily BGM plus | 1,400 | 158,601 | 113.3 | ×17.9 | 1,069.1 | 602.7분 | 2026-05-28 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 27/27 |
| 428 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 라흐마니노프 - 지독한 슬픔 끝에 피어난 환희에 대하여ㅣRachmaninoff Style](https://www.youtube.com/watch?v=w5nhvxPli3E) | Moonlight Cla… | 8,360 | 944,056 | 112.9 | ×798.0 | 9,792.7 | 180분 | 2026-07-19 | 기타 | 플레이리스트·모음 | 설명 | 791/823 |
| 429 | [Painful - Emotional Cinematic Storytelling Music ∣ Orchestr…](https://www.youtube.com/watch?v=yk_jaCUz91M) | BynD Epic | 1,210 | 136,425 | 112.8 | ×78.3 | 962.7 | 4.9분 | 2026-06-04 | 13. OST·사운드트랙 | 음악 | 설명 | 64/64 |
| 430 | [🌧️ (No Ads) Real Heavy Rain & Powerful Thunderstorm ⛈️ ∣ De…](https://www.youtube.com/watch?v=tAd_vs_Ej_I) | Rain Drop's | 7,790 | 875,790 | 112.4 | ×23.7 | 10,138.5 | 95.1분 | 2026-07-29 | 2. 자연 소리·백색소음 | 음악 | 설명 | 287/293 |
| 431 | [Kabhi Shaam Dhale ∣ Romantic Recreated Version ∣ Soulful Hi…](https://www.youtube.com/watch?v=jHw-Ivg2bLc) | Deepak Pandey | 39,000 | 4,382,318 | 112.4 | ×882.5 | 24,929.4 | 4.7분 | 2026-05-01 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 449/455 |
| 432 | [The Most Trending OPM Acoustic Songs on Spotify 2026 ✨ ∣ Vi…](https://www.youtube.com/watch?v=MbnaF3T2450) | Calm Guitar | 13,100 | 1,468,125 | 112.1 | ×123.5 | 19,742.9 | 63.8분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 121/129 |
| 433 | [Darmiyaan - Unplugged](https://www.youtube.com/watch?v=f5vaem1fvGk) | Raghav Kaushi… | 9,800 | 1,097,055 | 111.9 | – | 12,097.5 | 5분 | 2026-07-25 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/30 |
| 434 | [Tomay Pelam Elo Mone ∣ তোমায় পেলাম এলো মনে হাজার আলোর বন্য…](https://www.youtube.com/watch?v=rPi4ScyrzIM) | Sudip Lo-Fi M… | 20,100 | 2,239,821 | 111.4 | ×2,429.3 | 12,814.2 | 4.3분 | 2026-05-02 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 165/169 |
| 435 | [Pokémon Café Jazz Lofi ∣ ☕ Smooth Beats for Study & Focus S…](https://www.youtube.com/watch?v=t6yrxjE7HSM) | Rest Point Lo… | 4,080 | 452,862 | 111.0 | ×74.3 | 2,573.5 | 104.2분 | 2026-05-01 | 3. 공부·집중·작업 | 음악 | 설명 | 74/76 |
| 436 | [Romantic Instrumental Playlist 💖 ∣ Saxophone & Flute Love M…](https://www.youtube.com/watch?v=dHqp0WOzSns) | Video Music S… | 6,080 | 672,582 | 110.6 | ×30.5 | 6,598.8 | 13.3분 | 2026-07-14 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 34/35 |
| 437 | [임영웅 콘서트 명곡 22곡 모음 💙 가장 사랑받는 감성 트로트·추억 발라드 연속듣기 #임영웅 #임영웅노래모…](https://www.youtube.com/watch?v=532qBV3Bs9o) | 별빛 영웅 뮤직 | 2,990 | 328,563 | 109.9 | ×1,667.8 | 2,846.0 | 75.3분 | 2026-06-30 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 113/114 |
| 438 | [ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ](https://www.youtube.com/watch?v=MsjHOAq7WH0) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 14,700 | 1,613,381 | 109.8 | ×309.9 | 30,520.4 | 67.7분 | 2026-09-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,119/1,122 |
| 439 | [Sera Se Cosera - One Name (Extended) ∣ Jailer 2 BGM ∣ Super…](https://www.youtube.com/watch?v=0EcRBvWCmhQ) | JB RagaMix | 17,000 | 1,860,429 | 109.4 | ×23.2 | 16,754.9 | 5분 | 2026-07-05 | 기타 | 음악 | 설명 | 324/352 |
| 440 | [💖신나게 미친(positive) 최신 걸그룹 노래 모음 ∣ 최신 여자아이돌 플레이리스트 [ Girl Gro…](https://www.youtube.com/watch?v=PiKPf0T7I84) | 띠잉뮤직 | 20,900 | 2,268,991 | 108.6 | ×191.5 | 13,239.3 | 120.5분 | 2026-05-05 | 기타 | 플레이리스트·모음 | 설명 | 270/271 |
| 441 | [🎻 바흐에게서 영감을 받은 바로크 듀엣 – 첼로와 오보에](https://www.youtube.com/watch?v=NxDxvXUWyFQ) | yoon acacia | 1,690 | 182,681 | 108.1 | ×329.2 | 2,209.1 | 69.7분 | 2026-08-02 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 35/35 |
| 442 | [Dark Jazz Noir for Deep Focus, Work & Night Study ∣ Floatin…](https://www.youtube.com/watch?v=eFl7QIAYHHw) | What can I ge… | 14,200 | 1,530,260 | 107.8 | ×61.0 | 16,390.6 | 32분 | 2026-07-22 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 272/281 |
| 443 | [Soft Acoustic Playlist 🎵 ∣ Best Relax & Chill Vibes Songs 2…](https://www.youtube.com/watch?v=MPT9v9MIod0) | Cozy Strings | 9,790 | 1,050,442 | 107.3 | ×348.2 | 6,698.4 | 69.8분 | 2026-05-20 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 84/92 |
| 444 | [(BGM) 432Hz Ultimate Healing Music ∣ Alpha Wave for Body an…](https://www.youtube.com/watch?v=3odCe4Ry-EY) | Serenę Sound | 6,880 | 724,367 | 105.3 | ×1,175.9 | 4,428.5 | 73.5분 | 2026-05-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 228/231 |
| 445 | [99% DEEP SLEEP in 3 Minutes (NO ADS) • Relieves Stress • In…](https://www.youtube.com/watch?v=E0hQGUOAhrQ) | Fall Asleep S… | 9,920 | 1,039,021 | 104.7 | ×106.5 | 13,607.0 | 116.9분 | 2026-08-08 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 281/275 |
| 446 | [Beautiful Sad Love Songs 2026 English Love Songs Playlist M…](https://www.youtube.com/watch?v=vKMy_Q_1wbc) | MusicLouds | 24,700 | 2,583,521 | 104.6 | ×1,799.7 | 14,967.5 | 71.4분 | 2026-05-04 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 870/879 |
| 447 | [Quiet Night Playlist 🌙 ∣ Soft Love Songs for Deep Feelings …](https://www.youtube.com/watch?v=EvU4QgmjhMY) | Cozy Strings | 9,790 | 1,019,077 | 104.1 | ×337.8 | 7,236.7 | 134.1분 | 2026-06-05 | 기타 | 플레이리스트·모음 | 설명 | 162/181 |
| 448 | [🌿 Возвращение к себе ∣ Музыка покоя 💦 Вода и тибетские чаши…](https://www.youtube.com/watch?v=eFje9j9VLZ0) | МУДРЫЕ МЕДИТА… | 6,810 | 703,854 | 103.4 | ×13.8 | 5,932.0 | 30.1분 | 2026-06-27 | 1. 수면·명상·힐링 | 음악 | 설명 | 162/163 |
| 449 | [Summer Deep House Mix 2026 ∣ Luxury Chillout Lounge Music f…](https://www.youtube.com/watch?v=ZZjKsakgbgw) | Surfboard Dee… | 5,770 | 588,791 | 102.0 | ×507.1 | 3,757.7 | 65.2분 | 2026-05-20 | 4. 카페·매장·라운지 | 음악 | 설명 | 248/251 |
| 450 | [[Playlist] 조용히 혼자 듣고 싶다… 천상의 감성 보이스 7080 올드팝 🎧 ∣ 카페·휴식·감성 B…](https://www.youtube.com/watch?v=HBx4T1dadhI) | TrueOldies 70… | 5,630 | 574,082 | 102.0 | ×240.7 | 3,673.9 | 140.2분 | 2026-05-21 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 346/352 |
| 451 | [Waheguru Jaap Before Sleep 🌙 Relaxing Meditation Kids, Babi…](https://www.youtube.com/watch?v=gT1SH3nqnuw) | Nanak Naam Ch… | 349 | 35,505 | 101.7 | – | 246.8 | 10.2분 | 2026-06-02 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 33/33 |
| 452 | [​🎧 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 아무 걱정 없이 쉬고 싶은 날, 편안하고 아늑한 어쿠스틱 빈티지 재즈](https://www.youtube.com/watch?v=Py3IKxJcbAA) | MONA mood | 10,000 | 1,013,573 | 101.4 | ×42.1 | 9,357.2 | 84.4분 | 2026-07-08 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 94/98 |
| 453 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=ca4K-2vlfvA) | KKR rahul 09 | 16,500 | 1,669,356 | 101.2 | ×623.2 | 55,127.3 | 18.2분 | 2026-09-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 69/72 |
| 454 | [힐링음악 ∣ 쉬어 가도 괜찮아 (It’s Okay to Rest) ∣ 지친 마음을 쉬게 하는 국악 힙합 ∣…](https://www.youtube.com/watch?v=OTmG9c33c1M) | 풍그루 | 637 | 63,327 | 99.4 | ×21.8 | 719.0 | 5.1분 | 2026-07-28 | 1. 수면·명상·힐링 | 한 곡 | 설명 | 10/10 |
| 455 | [[Playlist] 만약에 그날, 널 붙잡았다면│감성 발라드 플리](https://www.youtube.com/watch?v=KtjdGajPw_8) | 심야플리 | 2,320 | 230,242 | 99.2 | ×52.4 | 1,287.6 | 67.3분 | 2026-04-28 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 179/179 |
| 456 | [CHÌM VÀO GIẤC NGỦ SAY - Nhạc Lofi Chill Nhẹ Nhàng Thư Giãn …](https://www.youtube.com/watch?v=PJGgU7H4ruA) | Xóm Chill | 6,220 | 616,173 | 99.1 | ×143.4 | 7,922.1 | 156.2분 | 2026-08-07 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 82/82 |
| 457 | [Silver Moon — Hypnotic Vocal Ambient (Enigma & Schiller Sty…](https://www.youtube.com/watch?v=hJd8GIUEOog) | ARTechnoMusic | 3,810 | 374,162 | 98.2 | ×24.1 | 3,209.6 | 6분 | 2026-06-29 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 114/119 |
| 458 | [Healing Music for Anxiety, Fears and Depression 🌿 Heals the…](https://www.youtube.com/watch?v=AcfJRtYtSZU) | Nature Aura | 3,940 | 386,722 | 98.2 | ×315.4 | 5,614.2 | 105.2분 | 2026-08-16 | 1. 수면·명상·힐링 | 음악 | 설명 | 32/35 |
| 459 | [Mere Mehboob Qayamat Hogi ✨ ∣ Slowed Reverb + LoFi ∣ Sad Hi…](https://www.youtube.com/watch?v=AHo0xW8RYTQ) | Abidpro | 46,100 | 4,481,863 | 97.2 | ×798.4 | 28,603.3 | 9.4분 | 2026-05-20 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 350/350 |
| 460 | [Dear God, Can You Hear Me ? - Ethereal Celtic ambient Track…](https://www.youtube.com/watch?v=7c2GwOr5NGc) | Dreamstatic E… | 4,120 | 398,004 | 96.6 | ×212.2 | 2,957.3 | 7분 | 2026-06-11 | 14. AI 음악 | AI 음악 | 설명 | 584/587 |
| 461 | [Ganga Dharaye Shiv 🙏 ∣ Om Namah Shivaya ∣ Powerful Shiva Bh…](https://www.youtube.com/watch?v=FTzC_e5FQZA) | Spiritual Tun… | 29,200 | 2,816,911 | 96.5 | ×7,007.2 | 15,710.6 | 66.4분 | 2026-04-28 | 1. 수면·명상·힐링 | 정보·해설 | 설명 | 492/494 |
| 462 | ["सुकून भरी रातें 🌙 ∣ Romantic Hindi LoFi Songs ∣ Relaxing S…](https://www.youtube.com/watch?v=DU0Swx5GKB4) | Hindi Tuning | 25,200 | 2,422,424 | 96.1 | ×335.8 | 81,747.7 | 104분 | 2026-09-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 61/93 |
| 463 | [10 Minutes Deep Meditation Music for Positive Energy • Free…](https://www.youtube.com/watch?v=PtUp1X2POmU) | TRUEMÖ Musics | 296 | 28,119 | 95.0 | ×530.5 | 1,351.9 | 10.1분 | 2026-10-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 1/1 |
| 464 | [If You Are Fall In Love Then Listen Romantic Indian Instrum…](https://www.youtube.com/watch?v=rCFoSTwT1GU) | Veena Meditat… | 2,630 | 248,587 | 94.5 | ×775.6 | 2,102.8 | 81.8분 | 2026-06-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 26/27 |
| 465 | [Playlist l 우리는 너무 어렸고 서툴렀다, 가사없는음악](https://www.youtube.com/watch?v=DN0T_nrFf6o) | Freemu 프리뮤 | 3,840 | 362,510 | 94.4 | ×1,082.1 | 5,272.3 | 60.2분 | 2026-08-16 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 56/61 |
| 466 | [All RED EVIL JACK MUSIC REJ儀式付【作業用/For work】](https://www.youtube.com/watch?v=_QAOzonmqh8) | イヴch🍳🥚 | 2,450 | 229,516 | 93.7 | – | 2,880.7 | 11.8분 | 2026-08-05 | 기타 | 음악 | 없음 | 132/137 |
| 467 | [Vivaldi x Paganini x Bach Inspired 🎻 Fast & Relaxing Violin…](https://www.youtube.com/watch?v=0Jdy1C_QqvE) | Classical Vio… | 25,600 | 2,371,738 | 92.7 | ×3,060.3 | 15,782.2 | 74.7분 | 2026-05-27 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,656/1,720 |
| 468 | [endless dream](https://www.youtube.com/watch?v=g33LSGLwLzo) | TaTa_Chan | 23,300 | 2,154,232 | 92.5 | ×286.8 | 15,092.3 | 165.3분 | 2026-06-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,317/2,426 |
| 469 | [Cheema Y Best Songs Playlist ∣ Punjabi Hits 2026 ∣ Jukebox …](https://www.youtube.com/watch?v=LFpVqIlmn00) | Radio Level L… | 38,600 | 3,562,281 | 92.3 | – | 30,440.2 | 27.9분 | 2026-06-29 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,003/1,063 |
| 470 | [Sunrise Serenity ∣ Raag Ahir Bhairav inspired Music with bi…](https://www.youtube.com/watch?v=LLFxvwEOEGs) | Music for Life | 6,120 | 564,215 | 92.2 | ×404.3 | 4,022.3 | 40.2분 | 2026-06-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 259/267 |
| 471 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 틀자마자 시원해지는 당도보장 여름플리🩵(중간광고❌) Feel Good Chill Pop🎧카…](https://www.youtube.com/watch?v=t1i4n4SvtkE) | OurmuseMusic | 848 | 78,071 | 92.1 | ×24.0 | 603.3 | 607.7분 | 2026-06-16 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 68/68 |
| 472 | [#나는너를 - #장현 (1974년) Covered by sMUSIC #7080가요명곡 #리메이크명곡](https://www.youtube.com/watch?v=3F3vaZpv1ik) | sMusic 7080_명… | 7,130 | 654,486 | 91.8 | ×248.3 | 4,362.0 | 4.5분 | 2026-05-27 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 없음 | 80/82 |
| 473 | [Classic Rock Songs 70's 80's 90's Playlist 🔥 Guns N Roses, …](https://www.youtube.com/watch?v=erfv9QasZAw) | 80s90s Rock R… | 24,200 | 2,219,579 | 91.7 | ×5,114.2 | 26,480.1 | 106.5분 | 2026-08-01 | 기타 | 플레이리스트·모음 | 설명 | 171/188 |
| 474 | [회심곡(回心曲) - 쉬운 우리말로 풀어낸 한마음 회심곡, 불교음악, 부모은중경,부모은혜 ,인생무상 , 나무…](https://www.youtube.com/watch?v=0_QIhEcEiq0) | Dragonsong | 668 | 61,261 | 91.7 | ×61.9 | 954.7 | 7.5분 | 2026-08-21 | 기타 | 음악 | 설명 | 39/43 |
| 475 | [Viral Chill Songs Playlist 2026🔥I MidnightVibes ∣ Non-Stop …](https://www.youtube.com/watch?v=SNx32obvuEk) | Viralics | 8,770 | 804,048 | 91.7 | ×60.3 | 4,987.4 | 17.1분 | 2026-05-16 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 116/116 |
| 476 | [The Calm After the Storm - Classical Music for Emotional He…](https://www.youtube.com/watch?v=AkVSmWxf6WA) | Reverie Class… | 8,340 | 764,492 | 91.7 | ×423.5 | 9,120.6 | 57.2분 | 2026-08-01 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 401/417 |
| 477 | [Patar Bashori 🥀 ∣ পাতার বাঁশরী ∣ Female Version ∣ Bangla No…](https://www.youtube.com/watch?v=kQ3IwNRzLMM) | Lofix Dj Fusi… | 31,100 | 2,843,418 | 91.4 | ×2,605.1 | 33,473.5 | 18.4분 | 2026-07-31 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 976/1,006 |
| 478 | [Playlist ✍️집중력 1등 공부 플레이리스트 BGM ∣ 공부할때 듣기 좋은 음악🎧 focus&stud…](https://www.youtube.com/watch?v=wouMGz1k7K8) | obne music 오브… | 7,740 | 706,986 | 91.3 | ×98.0 | 11,436.1 | 122.1분 | 2026-08-23 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 49/56 |
| 479 | [Saxophone Instrumental Love Songs 🎷 Timeless Romantic Hits …](https://www.youtube.com/watch?v=y8IS36i_yOc) | MEMORIES PATH | 5,980 | 545,736 | 91.3 | ×432.8 | 5,524.6 | 56분 | 2026-07-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 109/112 |
| 480 | [옛날 시골집 슬레이트 빗소리ㅣ고향의 향수ㅣ추억ㅣ수면유도](https://www.youtube.com/watch?v=IHYnumQGS2o) | 빗소리 Healing S… | 1,570 | 142,463 | 90.7 | ×51.0 | 1,009.1 | 300분 | 2026-06-05 | 1. 수면·명상·힐링 | 자연 소리·백색소음 | 설명 | 47/47 |
| 481 | [Lullaby for Babies 💤 Sleep instantly in 3 minutes ♥ Sleep m…](https://www.youtube.com/watch?v=BUvu6tA9VTM) | Starfish and … | 8,130 | 735,958 | 90.5 | ×166.4 | 4,371.3 | 123.9분 | 2026-05-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 482 | [7 Pieces by Hans Zimmer \\ Iconic Soundtracks \\ Relaxing P…](https://www.youtube.com/watch?v=28vfE8VR2aE) | Yurii Salukha | 6,080 | 548,348 | 90.2 | ×417.6 | 7,779.4 | 33.3분 | 2026-08-14 | 13. OST·사운드트랙 | 음악 | 설명 | 57/59 |
| 483 | [Summer Café Bleu Lounge ∣ Luxury Originals](https://www.youtube.com/watch?v=_nmkwn2A8GI) | DeluxeChill | 7,140 | 643,898 | 90.2 | ×160.9 | 3,915.8 | 65.8분 | 2026-05-12 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 199/202 |
| 484 | [신나는 뽕짝·트로트 14곡 연속듣기 🎵 관광버스 필수곡 ∣ 신나는 뽕짝 메들리 ∣ 고속도로 트롯 BEST](https://www.youtube.com/watch?v=LxWOrfUcQlY) | 뽕친놈 | 5,140 | 461,512 | 89.8 | ×167.7 | 4,406.4 | 50.7분 | 2026-07-11 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 77/81 |
| 485 | [Indian Instrumental Fusion Music 🎶 Flute, Tabla, Veena & Si…](https://www.youtube.com/watch?v=646h8c7sUSw) | FLUTE TABLA A… | 6,160 | 551,659 | 89.6 | ×600.0 | 3,676.8 | 18.1분 | 2026-05-27 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 153/154 |
| 486 | [life](https://www.youtube.com/watch?v=8TjeO3AFTbM) | sleepwalker | 14,600 | 1,300,770 | 89.1 | ×115.0 | 7,996.6 | 60분 | 2026-05-14 | 기타 | 긴 한 곡·반복 | 설명 | 970/979 |
| 487 | [🎧 Tanveer Evan: The Ultimate Love & Soulful Hits ∣ Emotiona…](https://www.youtube.com/watch?v=wHpNUy_W4GM) | Song Lyrics | 25,100 | 2,230,266 | 88.9 | ×198.3 | 15,698.8 | 23.6분 | 2026-06-04 | 기타 | 플레이리스트·모음 | 설명 | 890/900 |
| 488 | [Enya - Miracles (Official Music Video)](https://www.youtube.com/watch?v=9hNpytudWRo) | Alternate Pop | 19,700 | 1,735,869 | 88.1 | ×151.0 | 13,198.7 | 8.1분 | 2026-06-14 | 1. 수면·명상·힐링 | 한 곡 | 설명 | 836/851 |
| 489 | [🔥 JOSHHH BOOSTING BOLLYWOOD SONGS 🎧 ∣ Study Motivation Play…](https://www.youtube.com/watch?v=5BLt-lBa0gQ) | Echoess of un… | 6,270 | 551,272 | 87.9 | ×3.2 | 3,758.1 | 6.9분 | 2026-05-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 217/219 |
| 490 | [the playlist to actually enter flowstate.](https://www.youtube.com/watch?v=wdDhTr_M7kA) | Pure Grit Stu… | 20,700 | 1,810,765 | 87.5 | ×96.1 | 32,633.9 | 123분 | 2026-08-29 | 기타 | 플레이리스트·모음 | 설명 | 545/553 |
| 491 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 😎 회사 생각 안나는 방법 찾았음 ⚡ 이 음악 재생 필수! Groove JazzHop ㅣC…](https://www.youtube.com/watch?v=Lv02AFsUrN8) | grooveonpli | 986 | 86,240 | 87.5 | ×88.0 | 573.4 | 372.4분 | 2026-05-26 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 73/75 |
| 492 | [🎧 Relax & Enjoy Playlist ∣ Best Trending Pop Music Collecti…](https://www.youtube.com/watch?v=vDs2KPkfw8Q) | Morning Seren… | 17,400 | 1,514,915 | 87.1 | ×35.4 | 19,088.6 | 67.4분 | 2026-08-05 | 3. 공부·집중·작업 | 커버·직접 부른 노래 | 설명 | 126/138 |
| 493 | [🎧 2000s Nostalgia Mashup ∣ Tu Tu Hai Wahi (BGM) x Mujhse Mo…](https://www.youtube.com/watch?v=0K8bNaPHiWk) | VibesWithAni | 3,540 | 307,259 | 86.8 | ×4,267.5 | 4,895.4 | 6.5분 | 2026-08-22 | 기타 | 음악 | 설명 | 66/67 |
| 494 | [Relaxing Meditation Music & Waterfall Sounds 🌿Calm, Deep Sl…](https://www.youtube.com/watch?v=gfulfnnJ3lY) | Celestial Rel… | 12,300 | 1,066,804 | 86.7 | ×328.0 | 18,754.3 | 126.5분 | 2026-08-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 116/126 |
| 495 | [The Wild Theme (EXTENDED REMIX) ∣ OM First Strike ∣ Sai Abh…](https://www.youtube.com/watch?v=IoJerPi947U) | JB RagaMix | 17,000 | 1,469,439 | 86.4 | ×18.3 | 13,892.1 | 4.3분 | 2026-07-10 | 기타 | 음악 | 설명 | 214/219 |
| 496 | [Soft Background Acoustic 🌿 Best Acoustic Covers Playlist 20…](https://www.youtube.com/watch?v=KoTsEko_7c8) | Afterhours Ac… | 15,800 | 1,355,071 | 85.8 | ×525.9 | 12,621.5 | 102분 | 2026-07-08 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 82/83 |
| 497 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 너도 지금 이 노래 듣고 있을까? 🤍 ∣ Chill R&B · 매장음악 · 카페 플레이리스트](https://www.youtube.com/watch?v=AM8WMi8_1cE) | mellomoodyy | 6,370 | 535,796 | 84.1 | ×155.4 | 5,636.7 | 90.1분 | 2026-07-21 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 185/185 |
| 498 | [Smoke Mood - Just Relax ∣ Chill House & Deep House Mix 🎧 Ch…](https://www.youtube.com/watch?v=SMsadBMPWQU) | ChillNight Me… | 24,000 | 2,002,932 | 83.5 | ×579.7 | 14,102.3 | 67.5분 | 2026-06-04 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 317/320 |
| 499 | [듣는 순간 마음이 편안해지는 첼로와 오보에 🎻 ∣ 공부, 휴식, 감성 힐링 음악](https://www.youtube.com/watch?v=aha1_5ENidU) | 따뜻한 휴식 Studio | 2,010 | 167,117 | 83.1 | ×390.0 | 1,145.4 | 33.4분 | 2026-05-31 | 1. 수면·명상·힐링 | 음악 | 설명 | 100/100 |
| 500 | [🎧요즘 들은 플리 중에 제일 느낌 좋다… 느좋 감성힙합 Chill 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 🌙](https://www.youtube.com/watch?v=9iqkcoMV39k) | 𝐅𝐞𝐞𝐥𝐿𝐲𝐧 | 5,020 | 415,614 | 82.8 | ×46.7 | 2,838.8 | 70.3분 | 2026-05-30 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 281/281 |
| 501 | [Smoke Mood - Just Relax ∣ Chill House & Deep House Mix 🎧 Ch…](https://www.youtube.com/watch?v=yEASFhtzSMQ) | Chill Night H… | 28,800 | 2,376,311 | 82.5 | ×5,462.8 | 13,218.0 | 68.7분 | 2026-04-27 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 317/323 |
| 502 | [33 Koti Devi Devta हरेक विहानको मन्त्र ∣ हर हर महादेव ∣ जय …](https://www.youtube.com/watch?v=7fiSZtq8nHs) | Bhajan Hub Ne… | 33,400 | 2,748,290 | 82.3 | ×516.3 | 18,732.0 | 11.5분 | 2026-05-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,375/1,385 |
| 503 | [108 Hare Krishna Mahamantra Chants ∣ Harinam Kirtan for Pea…](https://www.youtube.com/watch?v=_AXkyLABNdw) | Pinakin Music | 10,400 | 855,261 | 82.2 | ×524.7 | 7,648.5 | 18.2분 | 2026-07-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 422/425 |
| 504 | [[playlist] 다신 사랑하지 않을 다짐](https://www.youtube.com/watch?v=xNrmomdWeqk) | le | 12,600 | 1,034,856 | 82.1 | ×24.1 | 5,891.9 | 25.4분 | 2026-05-01 | 기타 | 플레이리스트·모음 | 없음 | 655/669 |
| 505 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Study / Focus …](https://www.youtube.com/watch?v=aJsXjVL43xI) | Chill Vibes H… | 7,920 | 643,228 | 81.2 | ×2,382.3 | 9,035.1 | 8분 | 2026-08-14 | 3. 공부·집중·작업 | 음악 | 설명 | 65/65 |
| 506 | [if this background music found you, life will get better](https://www.youtube.com/watch?v=l3UmhyVCF90) | Ksu4000 | 23,300 | 1,888,535 | 81.0 | ×164.4 | 25,640.6 | 60.5분 | 2026-08-11 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 2,014/2,035 |
| 507 | [NIGHT PROTOCOL ∣ Dark Cyberpunk Music for Deep Work & Focus](https://www.youtube.com/watch?v=zXGb3k-A1Vo) | SoundFlow Lab | 8,950 | 725,168 | 81.0 | ×21.0 | 11,540.5 | 94.2분 | 2026-08-22 | 3. 공부·집중·작업 | 음악 | 설명 | 344/361 |
| 508 | [마음이 편안해져요, 가을 아침 클래식 ㅣ듣기만 해도 행복해지는 클래식 명곡](https://www.youtube.com/watch?v=XOiUmptBDVk) | Aria classic … | 2,600 | 209,333 | 80.5 | ×37.7 | 3,988.2 | 68분 | 2026-09-01 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 18/18 |
| 509 | [Relaxing Classic Rock 2026 🎸 Greatest Soft Rock Hits for Dr…](https://www.youtube.com/watch?v=m1zUF6E51kw) | Enchoes Of Cl… | 17,200 | 1,382,858 | 80.4 | ×1,880.2 | 8,678.8 | 81.6분 | 2026-05-17 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 1,040/1,061 |
| 510 | [15 Min Self Healing Music 🌿 Heal From Within & Find Inner P…](https://www.youtube.com/watch?v=wi3auWpIaZY) | Inner Healing… | 1,240 | 99,491 | 80.2 | ×64.8 | 2,129.7 | 16.5분 | 2026-09-07 | 1. 수면·명상·힐링 | 음악 | 설명 | 53/53 |
| 511 | [하루를 밝게 만드는 찬송가 모음 10곡 ∣ 기분 좋아지는 찬송가 모음 10곡 ∣ 어쿠스틱 기타 찬양 ∣ 듣…](https://www.youtube.com/watch?v=AOyN15yGFrs) | 주님곁에 | 19,100 | 1,531,673 | 80.2 | ×34.5 | 10,200.7 | 70.5분 | 2026-05-27 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 1,229/1,240 |
| 512 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=8vwZSZcOPtM) | Click Bollywo… | 10,700 | 856,453 | 80.0 | ×6,488.3 | 7,631.0 | 7.9분 | 2026-07-04 | 3. 공부·집중·작업 | 음악 | 설명 | 91/92 |
| 513 | [Mozart Style ∣ 아침 공기처럼 가볍게 흐르는 모차르트풍 스트링 앙상블 ✿중간광고 없음 ∣ 잔잔한…](https://www.youtube.com/watch?v=8SUfn18vz_U) | Lucerna Harmo… | 18,600 | 1,484,080 | 79.8 | ×212.0 | 11,989.8 | 132분 | 2026-06-22 | 4. 카페·매장·라운지 | 음악 | 설명 | 1,123/1,148 |
| 514 | [𝘠𝘰𝘶 𝘢𝘤𝘤𝘪𝘥𝘦𝘯𝘵𝘢𝘭𝘭𝘺 𝘧𝘦𝘭𝘭 𝘪𝘯 𝘭𝘰𝘷𝘦 𝘸𝘪𝘵𝘩 𝘚𝘰𝘶𝘵𝘩 𝘐𝘯𝘥𝘪𝘢𝘯 𝘴𝘰𝘯𝘨𝘴 (+ 𝘵𝘪…](https://www.youtube.com/watch?v=JgO5ly6YvGI) | 𝙏𝙪𝙭𝙡𝙞𝙥𝙨 🌷 | 42,000 | 3,331,945 | 79.3 | ×6.0 | 21,507.1 | 19.5분 | 2026-05-22 | 기타 | 음악 | 설명 | 950/957 |
| 515 | [TAI CHI MUSIC - Ancient Tao Healing ∣ Chinese Zen Music for…](https://www.youtube.com/watch?v=FDUj2q61rQ8) | Nebula Dreams | 6,080 | 480,230 | 79.0 | ×32.5 | 4,022.9 | 85.3분 | 2026-06-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 192/196 |
| 516 | [A K I R A - Floating High (original mix)](https://www.youtube.com/watch?v=cp_EDM8pS0Q) | AKIRA CLOUD | 7,870 | 621,027 | 78.9 | ×124.9 | 6,731.6 | 6.4분 | 2026-07-24 | 기타 | 음악 | 설명 | 122/122 |
| 517 | [Playlist ∣ 가을밤에는 남자발라드를 들어요 🍂 ∣ 한국 감성 발라드 모음 🔥](https://www.youtube.com/watch?v=iaEax89R7fQ) | 이짐땡 | 2,860 | 225,636 | 78.9 | ×21.6 | 6,086.7 | 167.7분 | 2026-09-17 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 8/10 |
| 518 | [মন ছুঁয়ে যাওয়া বাংলা Lo-Fi Romantic Songs _ Relaxing Bang…](https://www.youtube.com/watch?v=WX8EbRSHQYo) | Harano Kabita | 26,400 | 2,072,342 | 78.5 | ×456.2 | 27,375.9 | 17.6분 | 2026-08-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 255/258 |
| 519 | [【作業用BGM】名探偵コナン 夜ジャズメドレー☔️｜雨音とともに聴く Relaxing Jazz BGM](https://www.youtube.com/watch?v=ZoLpYGeZkn0) | Ken's Cafe&Ja… | 6,330 | 495,052 | 78.2 | ×22.4 | 3,038.0 | 167.6분 | 2026-05-14 | 7. 재즈·보사노바 | 음악 | 설명 | 175/175 |
| 520 | [Batman’s Solitude ∣ Dark Jazz Noir for Late Night Reflection](https://www.youtube.com/watch?v=s87k34ud3Kc) | Saturday Nigh… | 17,400 | 1,359,413 | 78.1 | ×123.2 | 8,299.1 | 60분 | 2026-05-13 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 590/591 |
| 521 | [영혼을 울리는 집시 바이올린 🎻 ∣ 감성 바이올린 · 집시 음악 · 휴식 플레이리스트 ∣ 보라빛 음악정원](https://www.youtube.com/watch?v=7xQeXJwhFh8) | 보랏빛 음악정원 | 174 | 13,589 | 78.1 | ×47.5 | 230.9 | 87.7분 | 2026-08-26 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 16/16 |
| 522 | [Peaceful Chill Playlist 🌙 Trending English Songs 2026 🎧 Bes…](https://www.youtube.com/watch?v=td6iCrK4MHc) | Morning Seren… | 17,400 | 1,358,464 | 78.1 | ×31.7 | 43,315.5 | 70.7분 | 2026-09-22 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 137/150 |
| 523 | [Heartbreaking 💔 songs + lofi Mashup songs Slowed Reverb son…](https://www.youtube.com/watch?v=u6gVi3TsKTM) | JR buzdar off… | 16,900 | 1,318,334 | 78.0 | ×3,810.2 | 15,457.9 | 7.8분 | 2026-07-31 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 53/53 |
| 524 | [Relajación Profunda, Claridad Mental 🌿 Reduce El Estrés Y L…](https://www.youtube.com/watch?v=j8hCioy51LU) | Healing Soul … | 10,700 | 832,928 | 77.8 | ×310.9 | 6,461.8 | 226.2분 | 2026-06-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 132/132 |
| 525 | [Positive Energy 2026 🌞 Feel Good Deep House Music for Morni…](https://www.youtube.com/watch?v=Dg9ePUDm4Vs) | ChillMorning … | 12,400 | 964,837 | 77.8 | ×280.6 | 6,569.7 | 65.7분 | 2026-05-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 331/331 |
| 526 | [Sitar for Dopamine Reset ∣ Indian Classical Music for Mindf…](https://www.youtube.com/watch?v=SEw8IsSXRSU) | Raga Focus | 37,700 | 2,922,004 | 77.5 | ×2,140.7 | 16,438.1 | 90분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,247/1,257 |
| 527 | [腦子太吵時，先聽3分鐘｜2026最寧靜太極禪音精選｜讓呼吸慢下來，腦中的雜音也慢慢散去｜夜晚放空・晨間靜坐冥想・正念呼…](https://www.youtube.com/watch?v=KR1ZjmufbOE) | 清心樂坊Taiji Zen | 3,250 | 251,018 | 77.2 | ×37.3 | 3,373.7 | 59.3분 | 2026-08-10 | 기타 | 정보·해설 | 없음 | 24/27 |
| 528 | [Do not listen to her music. She can hypnotise you in 4.49 m…](https://www.youtube.com/watch?v=0tBUIo44w-A) | Dream Weaver … | 19,100 | 1,469,221 | 76.9 | ×1,673.4 | 8,559.6 | 5.7분 | 2026-05-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 796/799 |
| 529 | [2 Hours Super Relaxing Baby Music ♥♥♥ Bedtime Lullaby For S…](https://www.youtube.com/watch?v=e_-uzFi6JlI) | Deep Calm Whi… | 31,500 | 2,420,339 | 76.8 | ×150.9 | 13,759.1 | 120.1분 | 2026-05-01 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 481/481 |
| 530 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=p8BH-D_YiQY) | Sani Music Of… | 8,880 | 681,248 | 76.7 | ×824.8 | 7,232.9 | 8분 | 2026-07-22 | 3. 공부·집중·작업 | 음악 | 설명 | 53/53 |
| 531 | [Afro House Mix 2026 🔥 Tribal Afro House Energy ∣ Emotional …](https://www.youtube.com/watch?v=UIzQAbsrlRk) | Jungle Pulse … | 27,000 | 2,070,354 | 76.7 | ×1,465.7 | 13,286.8 | 99.4분 | 2026-05-21 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 279/280 |
| 532 | [MOOD OFF 💔Sad 😭 LOFI SONG MASHUP ∣∣ SAD HEART BROKEN 💔 MOOD…](https://www.youtube.com/watch?v=kjV1sVljycI) | Hindi sad son… | 41,700 | 3,197,035 | 76.7 | ×32,790.1 | 19,711.1 | 19.6분 | 2026-05-15 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 330/330 |
| 533 | [jazz before i reach flow state](https://www.youtube.com/watch?v=fQIJb1h1RkA) | Defunct | 11,200 | 857,931 | 76.6 | ×192.1 | 5,231.7 | 127.8분 | 2026-05-13 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 944/947 |
| 534 | [ENIGMA Style Music 🔥 Whisper of My Angel 🔥 2026](https://www.youtube.com/watch?v=ELv5bUhS-Qw) | VoiceLine Mus… | 4,020 | 307,769 | 76.6 | ×1,805.1 | 1,795.1 | 5.6분 | 2026-05-05 | 기타 | 음악 | 설명 | 95/97 |
| 535 | [Melepasmu - Drive (Waktu Luang Version) ∣ Ambient Pop Melan…](https://www.youtube.com/watch?v=CfyEhCWn45o) | Waktu Luang | 18,700 | 1,430,416 | 76.5 | ×24.9 | 9,737.1 | 4.3분 | 2026-05-30 | 5. 운동·드라이브·신나는 | 커버·직접 부른 노래 | 설명 | 108/109 |
| 536 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=WH_pNjVfkCY) | Click Bollywo… | 10,700 | 817,449 | 76.4 | ×6,192.8 | 8,182.6 | 8분 | 2026-07-16 | 3. 공부·집중·작업 | 음악 | 설명 | 118/118 |
| 537 | [somehow this became your background music](https://www.youtube.com/watch?v=GTx1UYV9Y-o) | Ksu4000 | 23,300 | 1,777,432 | 76.3 | ×154.7 | 21,504.5 | 61.8분 | 2026-08-02 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 1,583/1,609 |
| 538 | [Enya Inspired - Tears Of The Rain (Ai Music)](https://www.youtube.com/watch?v=ZqRhMKrbk58) | Sonic Beatz | 5,870 | 445,689 | 75.9 | ×104.0 | 2,849.6 | 7.5분 | 2026-05-20 | 14. AI 음악 | AI 음악 | 설명 | 412/412 |
| 539 | [𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 들으면 행복해지는 노래 모음 🫧 하루종일 듣기 좋은 팝송 플레이리스트](https://www.youtube.com/watch?v=lQrhgr4_dKg) | seroma room | 16,700 | 1,267,119 | 75.9 | ×135.7 | 7,313.5 | 542.2분 | 2026-05-04 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 167/170 |
| 540 | [Life before Social Media - CHILL BRAZIL ∣ Samba, Luxury Bos…](https://www.youtube.com/watch?v=NHZXCzKGDQc) | Golden Smile | 6,570 | 497,029 | 75.7 | ×150.8 | 3,457.3 | 152.4분 | 2026-06-02 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 55/55 |
| 541 | [POV: YOU ARE A DESI BADDIE 💋😭 (PART-2) ✨ (+TIMESTAMPS) 😋 TH…](https://www.youtube.com/watch?v=9avHQt7MnK4) | Dramanique⋆.𐙚… | 32,400 | 2,447,925 | 75.5 | ×5.2 | 13,993.7 | 26.6분 | 2026-05-02 | 기타 | 정보·해설 | 설명 | 584/586 |
| 542 | [하츠투하츠 Hearts2Hearts 'RUDE!+Lemon Tang' 2026 한국대중음악상(KM Char…](https://www.youtube.com/watch?v=ddGnUiIjrgo) | poptforming | 5,950 | 444,645 | 74.7 | – | 4,897.7 | 6.6분 | 2026-07-25 | 기타 | 음악 | 없음 | 314/314 |
| 543 | [요즘 이 노래에 빠졌다 🎧 중독성 리듬 락트로트 17곡 2시간 10분 연속듣기 ∣ I’m Addicted …](https://www.youtube.com/watch?v=rDvH1El0H3k) | 인생은 트로트 | 9,890 | 733,161 | 74.1 | ×52.3 | 15,308.7 | 130.3분 | 2026-09-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 338/344 |
| 544 | [Ocean Chillout - Sunset Lounge Melodies and Luxury Lounge V…](https://www.youtube.com/watch?v=hFaOxrQmaQ4) | Afterglow Lou… | 10,700 | 792,848 | 74.1 | ×230.9 | 7,390.6 | 125.2분 | 2026-07-09 | 4. 카페·매장·라운지 | 음악 | 설명 | 231/232 |
| 545 | [दिमाग को शांत करने वाला संगीत ∣ बांसुरी + संतूर + जलतरंग + …](https://www.youtube.com/watch?v=z6QYtZlFvb4) | Shanti univer… | 713 | 52,789 | 74.0 | ×166.0 | 409.0 | 14.6분 | 2026-06-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 17/17 |
| 546 | [Flora's Garden 🌸🌷✨ soft waltz piano for studying, reading &…](https://www.youtube.com/watch?v=J8Qi6W8t0Ek) | rumi. | 12,800 | 946,079 | 73.9 | ×290.1 | 6,740.3 | 251.5분 | 2026-06-05 | 3. 공부·집중·작업 | 음악 | 설명 | 467/471 |
| 547 | [My Heart And Soul ∣ Romantic Emotional Love Song ∣ Soft Emo…](https://www.youtube.com/watch?v=f2LgAVp301Q) | Soft Emotion … | 13,700 | 1,006,956 | 73.5 | ×121.7 | 7,427.5 | 5.8분 | 2026-06-10 | 기타 | 한 곡 | 설명 | 179/183 |
| 548 | [Lord Heal Me -Inspired By Enya (2026 Ai Music Video)](https://www.youtube.com/watch?v=Q-JjRkFbFhU) | SOUNDIASM | 10,700 | 784,099 | 73.3 | ×3,853.1 | 5,308.1 | 5.2분 | 2026-05-29 | 14. AI 음악 | AI 음악 | 설명 | 326/326 |
| 549 | [공부할 때 듣는 판타지 음악 ∣ playlist](https://www.youtube.com/watch?v=d8sLNlVAuxE) | Flow Trigger. | 6,540 | 478,252 | 73.1 | ×29.5 | 7,224.8 | 130.3분 | 2026-08-19 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 58/63 |
| 550 | [모차르트에서 영감을 받은 아침 힐링 클래식 🌿 첼로 & 오보에 ∣ 평온한 산속 일출과 함께하는 휴식 음악](https://www.youtube.com/watch?v=tr3LEDt_p88) | Korean Rock B… | 4,910 | 358,491 | 73.0 | ×13.0 | 2,897.3 | 42.2분 | 2026-06-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 83/86 |
| 551 | [【星河入夢】 Ancient Chinese Healing Music 🎵 ∣ Qixi Star River 🌌 …](https://www.youtube.com/watch?v=pFttQ6MZ9d8) | Tianhe Harmony | 879 | 64,075 | 72.9 | ×156.3 | 675.5 | 77.8분 | 2026-07-21 | 1. 수면·명상·힐링 | 음악 | 설명 | 48/48 |
| 552 | [10 Most Powerful Morning Mantras ∣ Remove All Negativity ∣ …](https://www.youtube.com/watch?v=rH2JDVys2Os) | Adhyatmik Dhw… | 28,900 | 2,104,441 | 72.8 | ×1,914.9 | 13,816.8 | 20.7분 | 2026-05-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,753/1,773 |
| 553 | [스튜디오 지브리 풍 클래식🍃 신비로운 정원에서 듣는 음악 ∣ 따뜻한 피아노와 플루트](https://www.youtube.com/watch?v=KIunwCFWDUE) | Little DoReMi | 4,320 | 311,293 | 72.1 | ×411.2 | 2,299.0 | 136.3분 | 2026-06-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 39/40 |
| 554 | [Unlock Brain Power in 3 Minutes ∣ Classical Music for Focus…](https://www.youtube.com/watch?v=-zNMRToG5Vw) | Classical Mind | 23,300 | 1,656,813 | 71.1 | ×726.4 | 10,207.5 | 138.7분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 457/466 |
| 555 | [Paris Night Chanson 🌙 1960s Vintage French Café Music (Roma…](https://www.youtube.com/watch?v=8LyppqPNDns) | AtelierChanson | 15,700 | 1,116,300 | 71.1 | ×930.6 | 6,241.1 | 23.9분 | 2026-04-28 | 4. 카페·매장·라운지 | 음악 | 설명 | 941/943 |
| 556 | [🎬 듣는 순간 지나온 세월이 생각나 울컥했습니다. 🎼 너무 많은 것들을 책임지며 살아온 당신을 위한 노래 …](https://www.youtube.com/watch?v=f9qBfvwQ9Ak) | 가슴을 울리는 락카페 | 11,300 | 802,162 | 71.0 | ×103.6 | 5,360.2 | 4분 | 2026-05-27 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 | 198/208 |
| 557 | [ㅤㅤㅤㅤㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤ](https://www.youtube.com/watch?v=UHHSdhBSfgQ) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 22,900 | 1,621,765 | 70.8 | ×287.2 | 19,660.8 | 93.6분 | 2026-08-02 | 기타 | 음악 | 설명 | 956/966 |
| 558 | [Музыкальная терапия🌿успокаивает нервную систему и освежает …](https://www.youtube.com/watch?v=iBs7kGH9KhA) | МЕЛОДИЯ ДЛЯ Д… | 15,800 | 1,118,549 | 70.8 | ×460.1 | 7,048.1 | 60.2분 | 2026-05-18 | 6. 피아노·클래식·연주곡 | 음악 | 없음 | 912/920 |
| 559 | [playlist l 틀자마자 집중 잘 되는 느좋 노동요 🎧 chill • r&b • vibes ☾](https://www.youtube.com/watch?v=ese2bIvjZGU) | luroom | 8,490 | 600,380 | 70.7 | ×75.7 | 9,865.4 | 248.2분 | 2026-08-24 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 175/181 |
| 560 | [옛추억에 눈물나는 노래 '세월' #감성발라드 #감성가요](https://www.youtube.com/watch?v=zNbEjZxdswM) | 고구려TV🍒음악방송 | 4,180 | 295,283 | 70.6 | ×934.4 | 2,696.5 | 67.3분 | 2026-07-06 | 9. 가요·발라드·트로트 | 음악 | 설명 | 196/199 |
| 561 | [Morning Coffee Indie Folk – Warm Acoustic Music for Peacefu…](https://www.youtube.com/watch?v=wFy9kud8FHE) | Silver Coast | 29,600 | 2,088,799 | 70.6 | ×39.2 | 17,591.8 | 65.3분 | 2026-06-27 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 369/371 |
| 562 | [싸이월드 감성 발라드 💿 그 시절 MP3에 꼭 있던 노래 ∣ 2000년대 발라드 명곡 모음 🎧 SG워너비,…](https://www.youtube.com/watch?v=5T42ApT_D-o) | 그때 그 가락 | 3,100 | 217,874 | 70.3 | ×3.8 | 6,715.0 | 105.1분 | 2026-09-21 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 16/17 |
| 563 | [Groove Playlist ∣ ∣ Let your worries melt into the rhythm ∣…](https://www.youtube.com/watch?v=PjyT13hITqM) | DRDR | 13,800 | 964,773 | 69.9 | ×262.2 | 6,069.8 | 206.3분 | 2026-05-18 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 218/218 |
| 564 | [The Most Beautiful And Emotional Cinematic Adagio ∣ Cello &…](https://www.youtube.com/watch?v=6AKklMjtK8M) | CLASSICAL SPA… | 11,200 | 782,668 | 69.9 | ×537.9 | 4,879.1 | 61.9분 | 2026-05-16 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 981/994 |
| 565 | [soft pastel flowers 🌸🌷 relaxing piano for dreamy & peaceful…](https://www.youtube.com/watch?v=9NxQWqVtHRA) | She of the Va… | 11,900 | 814,012 | 68.4 | ×124.5 | 4,552.4 | 37.8분 | 2026-04-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 358/360 |
| 566 | [Deep Chill Mix 2026 🌌 Emotional House & Soulful Vibes for S…](https://www.youtube.com/watch?v=5FQsa5nWaW0) | Rhythm Flow | 23,700 | 1,620,785 | 68.4 | ×290.7 | 14,747.3 | 60.8분 | 2026-07-06 | 3. 공부·집중·작업 | 정보·해설 | 설명 | 323/328 |
| 567 | [Clear Yourself of Everything That Drains You ∣ Calm Your Mi…](https://www.youtube.com/watch?v=Ww-tZVjkI9Y) | Frequencies o… | 46,400 | 3,156,662 | 68.0 | ×25.5 | 25,953.3 | 68.4분 | 2026-06-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,284/1,296 |
| 568 | [a quiet playlist for a quiet heart (calm/relax piano)](https://www.youtube.com/watch?v=BBz7-F9mdUE) | Little Thing | 30,700 | 2,083,818 | 67.9 | ×188.0 | 13,628.3 | 89.5분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 314/318 |
| 569 | [Put This On and Calm Your Brain... (No Ads)🌧️ Soft Piano Mu…](https://www.youtube.com/watch?v=vhJgRiH31bQ) | Cozy Attic Ni… | 5,880 | 399,150 | 67.9 | ×397.6 | 3,178.7 | 716.8분 | 2026-06-20 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 182/186 |
| 570 | [Playlist 🎤 노래방 발라드 인기차트 & 애창곡](https://www.youtube.com/watch?v=4ZLxFva_K5I) | 필청 | 2,140 | 144,814 | 67.7 | ×15.8 | 949.9 | 165분 | 2026-05-24 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 20/20 |
| 571 | [𝐂𝐡𝐚𝐭𝐩𝐚𝐭𝐢 𝐇𝐨𝐧𝐞𝐲 𝐬𝐢𝐧𝐠𝐡 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐜𝐮𝐳 𝐲𝐨𝐮 𝐫𝐞𝐚𝐥𝐥𝐲 𝐧𝐞𝐞𝐝 𝐭𝐡𝐢𝐬. 𝐛𝐲 …](https://www.youtube.com/watch?v=eXNfz_Rs-KQ) | 𝐫𝐢𝐞 | 29,100 | 1,947,039 | 66.9 | ×1,465.0 | 12,584.6 | 14.8분 | 2026-05-22 | 기타 | 플레이리스트·모음 | 없음 | 211/218 |
| 572 | [The Most Beautiful Rachmaninoff-Inspired Adagios ∣ Quiet Ce…](https://www.youtube.com/watch?v=ZdzITqD4vlM) | Adagio Melanc… | 9,930 | 661,981 | 66.7 | ×74.8 | 8,852.5 | 61.6분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,106/1,158 |
| 573 | [Spiritual Temple Music ∣ 30 Minutes Stress Relief & Inner P…](https://www.youtube.com/watch?v=NF4gjQzGetw) | Shashwat Swar | 15,500 | 1,031,450 | 66.5 | ×86.6 | 6,980.0 | 34.2분 | 2026-05-29 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 146/150 |
| 574 | [Too Much on Your Mind? Stay Here for a While ∣ Arabic Oud A…](https://www.youtube.com/watch?v=uDCjW-9mE2k) | Sahara Echo M… | 14,400 | 957,987 | 66.5 | ×336.3 | 5,414.0 | 64.4분 | 2026-04-30 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 442/446 |
| 575 | [😊 아침부터 기분 좋게 행복해지는 노래 모음 🎧 가볍게 흥얼거리는 기분 좋게 행복한 노래 모음](https://www.youtube.com/watch?v=r0jtXc1Y-jE) | 행복 | 7,160 | 475,790 | 66.5 | ×128.9 | 7,504.1 | 116.4분 | 2026-08-21 | 14. AI 음악 | AI 음악 | 설명 | 152/158 |
| 576 | [하늘을 닮은 여름 🌸 여름 감성 피아노 플레이리스트 ∣ BGM ∣ 힐링·작업·집중](https://www.youtube.com/watch?v=Os2XdhfzZdo) | Mellow Season | 2,860 | 189,931 | 66.4 | ×23.9 | 1,910.7 | 120.9분 | 2026-07-16 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 31/31 |
| 577 | [3小時宅家Lofi音樂合集｜累了，你只想宅在家裡｜超長版為一個人獨處而生的放鬆音樂，適合发呆或什么都不做](https://www.youtube.com/watch?v=kiClDrAsuqE) | SeaU Lofi | 14,200 | 936,332 | 65.9 | ×68.7 | 5,918.8 | 191.8분 | 2026-05-19 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 238/242 |
| 578 | [मन को शांत करने वाली धुन ∣ राजयोग ध्यान की सहज विधि ∣ Brahm…](https://www.youtube.com/watch?v=ux3QNU3AaII) | Bhakti Naad | 771 | 50,360 | 65.3 | ×48.8 | 425.4 | 6.8분 | 2026-06-27 | 1. 수면·명상·힐링 | 음악 | 설명 | 27/27 |
| 579 | [[Playlist] "아침에 듣기 좋은 산뜻한 클래식 왈츠" ∣ Summer Palace Waltz 🌿](https://www.youtube.com/watch?v=D2WezFoeswI) | okply | 15,700 | 1,023,553 | 65.2 | ×129.8 | 6,399.4 | 148.9분 | 2026-05-17 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 578/586 |
| 580 | [Deepest Sleep Healing - Release Melatonin, Calm Anxiety & S…](https://www.youtube.com/watch?v=J64B8xhHEbs) | Deep Sleep Ha… | 13,500 | 879,717 | 65.2 | ×460.8 | 7,046.2 | 225.4분 | 2026-06-21 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 232/235 |
| 581 | [मोहे मोर बनइय्यो राधा ∣ Mohe Mor Banaiyo Radha Apne Vrindav…](https://www.youtube.com/watch?v=CPGQtKem4Cc) | Rangilo Gurja… | 25,000 | 1,627,137 | 65.1 | ×1,299.6 | 12,572.0 | 19.4분 | 2026-06-16 | 1. 수면·명상·힐링 | 음악 | 설명 | 375/375 |
| 582 | [샹송이 이렇게 까지 좋은줄 몰랐습니다. 아랑드롱이 사랑하던 멜로디가 아름다운 그 음악 ∣ Songs Tha…](https://www.youtube.com/watch?v=MHgCWNV-eKY) | Yesterday SOU… | 6,090 | 394,894 | 64.8 | ×783.5 | 2,453.9 | 43.9분 | 2026-05-16 | 기타 | 음악 | 설명 | 203/207 |
| 583 | [생각보다 좋게 풀리는 날 🎵마음에 초록빛을 채우는 힐링 피아노 ∣ 스트레스 해소 · 편안한 휴식 · 카페음…](https://www.youtube.com/watch?v=QC3xgG-dZJg) | Romua 로무아 | 3,410 | 218,650 | 64.1 | ×32.1 | 1,772.7 | 180.7분 | 2026-06-22 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 33/33 |
| 584 | [2000년대 발라드 명곡 30곡 💿 그 시절 우리가 사랑했던 노래｜SG워너비·김동률·씨야·티아라·양파 ✔ …](https://www.youtube.com/watch?v=IZ6NgLQjStY) | 추억음악다방 | 3,460 | 221,294 | 64.0 | ×57.6 | 2,294.5 | 117.8분 | 2026-07-19 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 17/18 |
| 585 | [모든 일이 잘 풀리는 아침을 여는 음악 ∣ 막혔던 일이 시원하게 풀리는 기분](https://www.youtube.com/watch?v=6MQT5DkZTEU) | LazyFlow | 10,900 | 696,296 | 63.9 | ×133.3 | 4,038.7 | 90.4분 | 2026-05-04 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 167/175 |
| 586 | [🌙 Relaxing Gospel R&B Worship Music 2026 – Peaceful Midnigh…](https://www.youtube.com/watch?v=SKYFRvhTL4A) | Sacred worshi… | 13,200 | 843,264 | 63.9 | ×1,847.2 | 5,286.0 | 61.2분 | 2026-05-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 355/356 |
| 587 | [[KPOP playlist] 마법처럼 빠져드는 케이팝 노동요](https://www.youtube.com/watch?v=uuZiS5xRAVw) | 오이는빼주세요 | 13,800 | 880,412 | 63.8 | ×75.2 | 5,408.7 | 59.7분 | 2026-05-14 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 70/70 |
| 588 | [Your Productive Office Playlist 🤍 Soft Acoustic Covers to S…](https://www.youtube.com/watch?v=h2cVkEu99eI) | Afterhours Ac… | 15,800 | 1,007,628 | 63.8 | ×391.1 | 9,563.5 | 116.7분 | 2026-07-10 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 54/54 |
| 589 | [【異世界ケルト】路地裏で流れる安らぎのファンタジーBGM｜静かな街のかすかな余韻 [睡眠用BGM・リラックス用BGM・…](https://www.youtube.com/watch?v=w2XZiZpAYZg) | Roran Baron | 8,840 | 562,665 | 63.6 | ×54.6 | 3,301.4 | 182.9분 | 2026-05-06 | 기타 | 정보·해설 | 설명 | 261/261 |
| 590 | [Gentle Rain Outside, Warm Piano Inside (No Ads) 🌧️ Helps Yo…](https://www.youtube.com/watch?v=G9iosi2cIh4) | Cozy Attic Ni… | 5,880 | 373,588 | 63.5 | ×372.1 | 3,204.8 | 717.9분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 178/194 |
| 591 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Stu…](https://www.youtube.com/watch?v=Koo5Xgqn_zE) | Stylish Offic… | 16,200 | 1,017,056 | 62.8 | ×2,655.5 | 17,171.0 | 8분 | 2026-08-26 | 3. 공부·집중·작업 | 음악 | 설명 | 99/107 |
| 592 | [Amélie ☕️ A Slow Weekend in Paris ∣ Piano Music for Relaxin…](https://www.youtube.com/watch?v=oToDtW7Gaas) | Peter Pan's L… | 6,130 | 384,788 | 62.8 | ×40.8 | 6,838.0 | 61.4분 | 2026-08-29 | 3. 공부·집중·작업 | 음악 | 설명 | 213/216 |
| 593 | [행운이 찾아오는 아침 🎵마음에 건강한 에너지를 채우는 힐링 피아노 ∣ 스트레스 해소 · 편안한 휴식 · 카…](https://www.youtube.com/watch?v=Xp2bSO5r5Os) | Romua 로무아 | 3,410 | 213,841 | 62.7 | ×31.4 | 1,557.0 | 180분 | 2026-06-08 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 37/37 |
| 594 | [바흐와 모차르트의 감성을 담은 아침 클래식 🌿 하루를 여는 평화로운 힐링 연주](https://www.youtube.com/watch?v=9_HXWyP1MsE) | Korean Rock B… | 4,910 | 306,524 | 62.4 | ×11.1 | 3,051.6 | 40.3분 | 2026-07-15 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 40/42 |
| 595 | [Ludovico Einaudi – 6 Piano Pieces ∣ Relaxing Music for Stud…](https://www.youtube.com/watch?v=nFJCWUpe2w4) | Yurii Salukha | 6,080 | 379,148 | 62.4 | ×288.8 | 4,649.6 | 29.7분 | 2026-08-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 54/54 |
| 596 | [Dark Jazz & Late Night Trip-Hop // Atmospheric Music for La…](https://www.youtube.com/watch?v=pGuvWU_1j-o) | Jazz Haze | 33,500 | 2,087,151 | 62.3 | ×898.9 | 12,749.4 | 94.2분 | 2026-05-13 | 5. 운동·드라이브·신나는 | 음악 | 없음 | 480/488 |
| 597 | [the best classical music for deep concentration ∣ string qu…](https://www.youtube.com/watch?v=Px1HC9ExXOk) | FocusSpace | 8,990 | 559,782 | 62.3 | ×96.9 | 6,030.8 | 64.6분 | 2026-07-23 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 444/452 |
| 598 | [Dolce Vita 🇮🇹 Luxury Italian Lounge Music ∣ Elegant Café Ja…](https://www.youtube.com/watch?v=oiG7xIAgCFw) | ITALIAN MAFIA… | 14,600 | 902,113 | 61.8 | ×948.6 | 8,612.5 | 86.5분 | 2026-07-11 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 346/356 |
| 599 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 세종대왕이 경복궁에서 야근하며 듣던 가야금 재즈](https://www.youtube.com/watch?v=q3oC3zdfyw4) | 조선재즈 | 10,200 | 620,039 | 60.8 | ×126.9 | 4,627.7 | 180.7분 | 2026-06-12 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 468/475 |
| 600 | [15 Minute Meditation Music • Raise Your Vibration • Relax M…](https://www.youtube.com/watch?v=e8EVg-NJCng) | Soul Waves - … | 2,620 | 159,097 | 60.7 | ×180.5 | 904.9 | 15.4분 | 2026-05-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 16/16 |
| 601 | [a playlist to make your brain shut up](https://www.youtube.com/watch?v=xIX_A2PRoW0) | HIGHWIND | 40,200 | 2,436,856 | 60.6 | ×166.1 | 35,875.8 | 62.1분 | 2026-08-17 | 1. 수면·명상·힐링 | 연주 | 설명 | 811/848 |
| 602 | [Richard Clayderman Tribute 🎹 ∣ Timeless Romantic Piano Music](https://www.youtube.com/watch?v=ZwlhZLzFxtk) | SONELIUM | 8,050 | 484,369 | 60.2 | ×1,245.2 | 6,410.8 | 29.4분 | 2026-08-09 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 178/179 |
| 603 | [7080 추억의 노래 광고없음🎶 7080노래모음 주옥같은노래 ✨7080 추억의 노래 한국인이 가장 좋아하는…](https://www.youtube.com/watch?v=3tshpfOljYs) | 7080 감성 선율 | 8,270 | 495,153 | 59.9 | ×21.4 | 11,397.1 | 118.6분 | 2026-09-10 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 63/67 |
| 604 | [Hyperfocus ∣ Lock In for 2 Hours ∣ Deep Work Study With Me …](https://www.youtube.com/watch?v=Rk0yG_dT0iI) | Work With Paul | 19,500 | 1,164,276 | 59.7 | ×8.5 | 16,154.7 | 111.4분 | 2026-08-13 | 3. 공부·집중·작업 | 긴 한 곡·반복 | 설명 | 138/141 |
| 605 | [The Knight Who Chose Peace ⚔️ ∣ Relaxing Fantasy Music](https://www.youtube.com/watch?v=u8xCmb7KbA0) | Melody of the… | 14,500 | 861,860 | 59.4 | ×177.2 | 5,275.1 | 74.5분 | 2026-05-13 | 기타 | 음악 | 설명 | 516/525 |
| 606 | [SAXOPHONE LOVE SONGS ❤️ Best Romantic Saxophone Music ∣ Bea…](https://www.youtube.com/watch?v=QpBzIwJPEoo) | Sax Chill Vib… | 28,700 | 1,699,913 | 59.2 | ×21.0 | 23,859.2 | 57.6분 | 2026-08-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 225/235 |
| 607 | [Bollywood+ Bhojpuri mix songs playlist (💗⚡💃🏻) ∣ @songplayli…](https://www.youtube.com/watch?v=sLPyIfOvPRQ) | xthetic._.vib… | 37,000 | 2,185,790 | 59.1 | – | 13,330.1 | 16.9분 | 2026-05-13 | 기타 | 플레이리스트·모음 | 설명 | 319/320 |
| 608 | [나는 어디로 가나 - (국악 발라드)](https://www.youtube.com/watch?v=hd_rjKroAqM) | Rok Bi | 8,600 | 505,032 | 58.7 | ×69.8 | 3,080.5 | 5분 | 2026-05-13 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 203/205 |
| 609 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 너도 나 좋아했으면 좋겠다](https://www.youtube.com/watch?v=4mAxMsNJAMI) | .happy | 241 | 14,145 | 58.7 | ×2.7 | 109.0 | 18.4분 | 2026-06-16 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 2/2 |
| 610 | [KUMAMICHI（熊道） — Japanese Zen Music Along the Bear’s Path](https://www.youtube.com/watch?v=vFJuk4U-V7Q) | Aether Journey | 34,200 | 2,007,149 | 58.7 | ×532.0 | 35,195.2 | 347분 | 2026-08-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 235/253 |
| 611 | [Fresh Mind Relaxing 💗 ∣ Slowed + Reverb Lofi Mix for Calm, …](https://www.youtube.com/watch?v=ACcuQVFbfnI) | Vansh Lofi | 29,500 | 1,729,908 | 58.6 | – | 13,382.1 | 16분 | 2026-06-17 | 1. 수면·명상·힐링 | 음악 | 설명 | 88/88 |
| 612 | [【作業用BGM】ちいかわ Instrumental Jazz 2時間 ∣ 深夜のジャズラウンジ ∣ ひとりごつ, 島の…](https://www.youtube.com/watch?v=CJEgDVcFy80) | GINZA Midnight | 23,100 | 1,353,905 | 58.6 | ×49.3 | 22,953.7 | 126.6분 | 2026-08-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 324/331 |
| 613 | [途中広告なし[BGM]癒しの森カフェで何も考えない朝☕Gentle Morning Piano Jazz｜心地よく一日…](https://www.youtube.com/watch?v=qDJ8LG4noFk) | Aurora Tune | 19,400 | 1,135,208 | 58.5 | ×18.6 | 6,473.5 | 92.5분 | 2026-05-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 116/116 |
| 614 | [빈예서 신곡 공개! 듣자마자 눈물 터졌다… “나훈아의 감성이 그대로” 😭🎵](https://www.youtube.com/watch?v=noMxR6lohxM) | 서울 뮤직 | 1,510 | 88,316 | 58.5 | ×104.1 | 5,458.6 | 6.9분 | 2026-10-08 | 기타 | 한 곡 | 설명 | 19/35 |
| 615 | [[COVER] 한오백년 _ 어버이날을 맞이하여...](https://www.youtube.com/watch?v=W40yM35SfWc) | 감성메아리 | 5,410 | 313,812 | 58.0 | ×592.1 | 1,824.1 | 4.8분 | 2026-05-05 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 58/58 |
| 616 | [Sade Morning Coffee ☕ Vol.3 ∣ Luxury ChillMix ∣ Soulful Jaz…](https://www.youtube.com/watch?v=mp4oA2JflBQ) | Setsukin | 43,900 | 2,545,292 | 58.0 | ×185.0 | 15,253.9 | 114.5분 | 2026-05-10 | 4. 카페·매장·라운지 | 음악 | 설명 | 780/789 |
| 617 | [[중간광고없음] 🌿 잠시, 아무 생각도 하지 말아요. ∣ 숲속에서 듣는 잔잔한 피아노 ∣ BGM ∣ 휴식,…](https://www.youtube.com/watch?v=ebDKy0szHC8) | Riae & Piano | 12,600 | 730,290 | 58.0 | ×47.6 | 7,276.6 | 181.3분 | 2026-07-15 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 191/203 |
| 618 | [처음부터 신나서 환장하는! ❤️ 신나는 트로트리믹스 고속도로메들리 ∣ 최신트로트 ∣ 트로트메들리 ∣ 감성트…](https://www.youtube.com/watch?v=zt45-jow7lo) | 다솜이의 트로트책방 | 7,810 | 452,370 | 57.9 | ×47.3 | 2,670.4 | 71.2분 | 2026-05-07 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 139/143 |
| 619 | [Paganini (Vivaldi x Beethoven) House Music Mix – Hypnotic V…](https://www.youtube.com/watch?v=Q9TSg4bKjcs) | Velvet Freque… | 5,600 | 323,282 | 57.7 | ×339.4 | 1,976.7 | 7분 | 2026-05-13 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 212/214 |
| 620 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 초여름 별사탕 𖤐ˊ˗](https://www.youtube.com/watch?v=aW-TYu5rwAY) | Horu | 3,550 | 204,346 | 57.6 | ×6.1 | 1,161.5 | 19.8분 | 2026-05-01 | 기타 | 플레이리스트·모음 | 없음 | 42/42 |
| 621 | [Elevate yourself - Bhagavad Gita ∣ Dark Trip-Hop X Downtemp…](https://www.youtube.com/watch?v=vrn7QzaHsbk) | SUR-SPIRITUAL | 7,910 | 450,764 | 57.0 | ×154.8 | 15,651.6 | 5.3분 | 2026-09-25 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 97/98 |
| 622 | [[MIXSET] 늙크크의 여름 HipHop & R&B](https://www.youtube.com/watch?v=_o3psN6OCTk) | 떵신 tteongshin | 8,150 | 461,902 | 56.7 | – | 4,627.3 | 22.1분 | 2026-07-16 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 204/204 |
| 623 | [✨💖요즘 폼 미친(positive) 최신 아이돌 노래 모음 ∣ 신나는 ∣ 최신곡 ∣ 여돌 ∣ 남돌 ∣ 아이…](https://www.youtube.com/watch?v=eLiTRGAnmyk) | 띠잉뮤직 | 20,900 | 1,178,569 | 56.4 | ×99.5 | 7,796.0 | 121.8분 | 2026-05-26 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 162/162 |
| 624 | [A Regular Day on the Journey ∣ Medieval Fantasy Music for D…](https://www.youtube.com/watch?v=TACRmufLfko) | Tales of Velm… | 18,000 | 1,007,617 | 56.0 | ×179.9 | 5,799.2 | 129.7분 | 2026-05-03 | 3. 공부·집중·작업 | 음악 | 설명 | 374/374 |
| 625 | [숲속에 내리는 잔잔한 빗소리 🌧️ 명상, 깊은 수면, 편안한 소리](https://www.youtube.com/watch?v=4Xl4kMOmGY8) | 숲 속 빗소리 | 1,800 | 100,554 | 55.9 | ×59.1 | 1,214.7 | 187.7분 | 2026-08-02 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 41/41 |
| 626 | [background music.](https://www.youtube.com/watch?v=gOwbMN0JswA) | quiet please. | 35,400 | 1,971,506 | 55.7 | ×11.9 | 11,425.2 | 60분 | 2026-05-04 | 8. 로파이·시티팝·칠 | 음악 | 없음 | 205/206 |
| 627 | [Dopamine Boost Music ∣ Flute, Sitar & Tabla for Positive En…](https://www.youtube.com/watch?v=kY7GcKagdjI) | CLASSICAL FUS… | 19,200 | 1,068,394 | 55.6 | ×270.8 | 8,199.5 | 27.8분 | 2026-06-16 | 3. 공부·집중·작업 | 음악 | 설명 | 717/722 |
| 628 | [90년대 2000년대 락발라드 명곡 모음 🎧 남자라면 한 번쯤 울컥했던 추억의 감성 노래 ∣ 버즈, 김경호…](https://www.youtube.com/watch?v=oB4-QrY7Vcc) | 발라드 홈 / BALLA… | 10,300 | 572,986 | 55.6 | ×60.7 | 5,766.6 | 187.4분 | 2026-07-16 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 79/81 |
| 629 | [비와 당신 (라디오스타 OST) - 가연이와 함께 듣는 비 오는 감성](https://www.youtube.com/watch?v=WmHI_XkpO2E) | GAYEON YOON | 30,300 | 1,666,704 | 55.0 | ×68.1 | 15,012.8 | 4.3분 | 2026-07-05 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 237/248 |
| 630 | [PAMPATANGGAL STRESS 🌴NON-STOP PINOY DUB REGGAE 2026 ∣ Relax…](https://www.youtube.com/watch?v=m4vweFMrdzw) | Evo Reggae Mix | 19,000 | 1,043,200 | 54.9 | ×161.3 | 8,029.3 | 74.8분 | 2026-06-16 | 기타 | 정보·해설 | 설명 | 429/430 |
| 631 | [🎧 Samz Vai: The Ultimate Sad & Emotional Hits 💔 ∣ Bengali L…](https://www.youtube.com/watch?v=kizXE5FXIFc) | Bangla Lofi 3… | 39,000 | 2,128,712 | 54.6 | ×65.8 | 23,193.9 | 26.9분 | 2026-07-24 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 239/253 |
| 632 | [(중간 광고 없음) 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 그때의 우린 왜 그리 서툴렀을까 ｜ 밤에 듣는 시린 첫사랑 발라드 …](https://www.youtube.com/watch?v=O-wm0ZSF2KU) | SonaWave | 12,400 | 675,056 | 54.4 | ×143.5 | 4,355.6 | 125.1분 | 2026-05-22 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 674/682 |
| 633 | [Krishna Mantra ∣ Pregnancy Music ∣ Music for pregnant women…](https://www.youtube.com/watch?v=TuMDXAiXlf0) | Be Listener M… | 18,900 | 1,028,299 | 54.4 | ×101.1 | 7,408.5 | 12.4분 | 2026-06-07 | 기타 | 음악 | 설명 | 384/391 |
| 634 | [Heals You While You Sleep (No Ads) • Increases Deep Sleep •…](https://www.youtube.com/watch?v=f68XXr9BDYw) | Serene Dreams… | 16,800 | 910,235 | 54.2 | ×436.4 | 11,291.5 | 226.8분 | 2026-08-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 311/312 |
| 635 | [The Little Forest Concert Vol.2 ∣ Cozy String Quartet for R…](https://www.youtube.com/watch?v=0DvSj6DAKDM) | 그루잠 Gurujam | 28,600 | 1,547,310 | 54.1 | ×259.2 | 11,354.0 | 45.1분 | 2026-06-10 | 3. 공부·집중·작업 | 음악 | 설명 | 364/378 |
| 636 | [첫 곡부터 너무 좋다 🍂 하루종일 듣게 되는 가을 올드팝 ∣ Vol.228 ∣ 7080 추억의 팝송 ∣ A…](https://www.youtube.com/watch?v=naLL7CGOC-8) | moka melody | 14,900 | 804,147 | 54.0 | ×44.4 | 12,300.4 | 367.3분 | 2026-08-19 | 4. 카페·매장·라운지 | 음악 | 설명 | 301/301 |
| 637 | [1990~2026 한국 감성 발라드 명곡 100 🎵 마음을 울리는 인기 노래 모음 하루 종일 들어도 좋은 …](https://www.youtube.com/watch?v=l3FyvUQUgSA) | 바람의 발라드 | 21,200 | 1,137,189 | 53.6 | ×701.5 | 8,586.1 | 130.5분 | 2026-06-13 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 121/123 |
| 638 | [Evergreen ghazal ∣ कभी फुर्सत मिले तो बैठ कर ये सोचता हूँ म…](https://www.youtube.com/watch?v=CiqRihLd68Q) | SOUL VIBES IN… | 30,000 | 1,595,763 | 53.2 | ×29.0 | 15,081.8 | 5.3분 | 2026-07-10 | 기타 | 음악 | 설명 | 298/299 |
| 639 | [여자력 상승하는 플리](https://www.youtube.com/watch?v=KSeIkQ_dpsg) | 무한우주에순간의빛일지라도 | 3,370 | 179,229 | 53.2 | ×10.6 | 3,535.5 | 15.4분 | 2026-09-03 | 기타 | 플레이리스트·모음 | 설명 | 12/13 |
| 640 | [If You Can’t Sleep, Play This 🌙 Instant Deep Sleep Music & …](https://www.youtube.com/watch?v=PFn7jFxLbhE) | Deep Sleep Ha… | 13,500 | 717,764 | 53.2 | ×376.0 | 9,477.6 | 181.2분 | 2026-08-09 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 237/239 |
| 641 | [카페음악 ∣ 최고 다방 음악❤️ 카페에서 듣기 좋은 노래 ❤️ 50대-60대가 좋아하는 중년가요 ∣ 아침 …](https://www.youtube.com/watch?v=_h8CNlmPkjo) | Korean Cafe M… | 3,280 | 174,316 | 53.1 | ×3,169.4 | 1,182.2 | 10.8분 | 2026-05-29 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 22/22 |
| 642 | [첫 곡부터 감성 미쳐버린🎧8090 레전드 플레이리스트](https://www.youtube.com/watch?v=i4uJ7c6b9gw) | Ceci Pop | 30,000 | 1,587,504 | 52.9 | ×107.3 | 11,313.7 | 112.8분 | 2026-06-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 1,362/1,367 |
| 643 | [50대이상이 들으면 정말 좋아할 노래 추천곡✨중년들이 사랑하는 겨울 노래 모음💕박인희/배따라기/여진/휘버스…](https://www.youtube.com/watch?v=TTkoF883bC8) | KTrot Melody | 11,400 | 601,547 | 52.8 | – | 7,040.1 | 126분 | 2026-07-30 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 103/109 |
| 644 | [HEAVEN-GIVEN VOICE ∣ Sad Love Songs ∣ soft rock ballad ∣ 슬픈…](https://www.youtube.com/watch?v=ySdeFYT0ohc) | Woori Sound | 13,200 | 696,526 | 52.8 | ×96.6 | 4,286.4 | 127.9분 | 2026-05-14 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 567/575 |
| 645 | [그 집 앞 (스페인어 버전 뮤직비디오) ∣ 이재성 원곡 라틴팝 리메이크 ∣ 한국어/스페인어 가사 자막 ∣ …](https://www.youtube.com/watch?v=T1fdlthH7Fw) | J.K.M | 38,200 | 2,012,590 | 52.7 | – | 12,817.5 | 4.2분 | 2026-05-20 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 설명 | 1,077/1,078 |
| 646 | [[Playlist] 초록빛 향기 머무는 여름날과 어울리는 음악 ∣ 잔잔한 감성팝 카페음악 ∣ Healing…](https://www.youtube.com/watch?v=l3rA0WjsaNM) | 낡은 레코드 | 8,930 | 468,280 | 52.4 | ×49.5 | 3,035.3 | 77.9분 | 2026-05-23 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 71/71 |
| 647 | [LiL Baby - Work For Money ( Official Music Video)](https://www.youtube.com/watch?v=3FclEMAiJ6Q) | Vibes World R… | 225 | 11,763 | 52.3 | ×7.3 | 228.5 | 7분 | 2026-09-02 | 기타 | 한 곡 | 설명 | 3/3 |
| 648 | [[스페인 감성] "Frente a Tu Casa ∣ 그집앞 - 이재성" Korean OldPop 한국명곡](https://www.youtube.com/watch?v=IXEpsuBWbg8) | 스페인 감성 한국 올드송 | 1,680 | 86,758 | 51.6 | ×2.3 | 1,197.3 | 4.5분 | 2026-08-12 | 12. 커버·노래 부르기 | 음악 | 설명 | 14/15 |
| 649 | [💚 초여름맛 메론소다 ☆・. ‘ . ꒰ 가사없는 집중 음악 ꒱](https://www.youtube.com/watch?v=FkmrHoP4xSk) | 둥실 ︵☆ | 1,190 | 61,291 | 51.5 | ×176.6 | 367.1 | 171.3분 | 2026-05-10 | 3. 공부·집중·작업 | 한 곡 | 설명 | 60/60 |
| 650 | [7080 감성 포크송 ∣ 듣기 좋은 통기타 포크 15곡](https://www.youtube.com/watch?v=Hpsm6Kn5TM4) | ***7080가요산책*** | 4,800 | 247,101 | 51.5 | ×25.2 | 2,703.4 | 64.5분 | 2026-07-24 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 105/106 |
| 651 | [2 Hour Sitar for Clean Your Brain Instantly ∣ Indian Classi…](https://www.youtube.com/watch?v=PVGFHGLRjK4) | Sacred Mind H… | 8,290 | 425,014 | 51.3 | ×311.1 | 2,391.1 | 120.4분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 206/208 |
| 652 | [Piano Sleep Music with Relaxing Rain 🎶 Calm Your Mind, Reli…](https://www.youtube.com/watch?v=pFL8mgVoxnc) | Piano Rain Re… | 30,300 | 1,546,228 | 51.0 | ×111.2 | 16,740.9 | 203.6분 | 2026-07-23 | 1. 수면·명상·힐링 | 음악 | 설명 | 327/329 |
| 653 | [Fall Asleep In 3 Minutes 😴 Mozart For Babies 💤 Extra Relaxi…](https://www.youtube.com/watch?v=P87LUaYiD34) | Mother & Baby… | 18,700 | 953,690 | 51.0 | ×25.4 | 15,959.1 | 150.1분 | 2026-08-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 654 | [2026년 6월 여돌 노래모음 ∣ 🔥 KPOP PLAYLIST](https://www.youtube.com/watch?v=a_19lS2wwOw) | 달플리 𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕 | 12,200 | 621,154 | 50.9 | ×46.4 | 4,306.5 | 64.9분 | 2026-06-02 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 53/53 |
| 655 | [(No Ads) Relaxing Music For Deep Sleep • Anxiety Relief, Me…](https://www.youtube.com/watch?v=UhQANX3rKzA) | Bedtime Calm … | 12,600 | 639,890 | 50.8 | ×98.3 | 3,959.0 | 94.3분 | 2026-05-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 68/70 |
| 656 | [22 Beautiful Serenity Adagios That Will Touch Your Soul ∣ R…](https://www.youtube.com/watch?v=-kXB3QJb1Vs) | Silent Adagio | 11,900 | 604,206 | 50.8 | – | 3,877.6 | 120분 | 2026-05-21 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 297/297 |
| 657 | [50대이상이 들으면 기분좋아지는 7080노래모음, 베스트 7080노래모음, 광고 없는 7080 좋은노래 모음](https://www.youtube.com/watch?v=L0rtQ0ZFr7o) | VibeTune | 11,500 | 583,400 | 50.7 | ×483.1 | 3,548.6 | 72.7분 | 2026-05-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 85/85 |
| 658 | [Ithaca](https://www.youtube.com/watch?v=8DVfI_Muv_A) | Ludwig Görans… | 43,300 | 2,193,981 | 50.7 | ×4.5 | 21,960.9 | 5.7분 | 2026-07-16 | 13. OST·사운드트랙 | 음악 | 설명 | 0/798 |
| 659 | [😴 Baby Sleep Music That Works in 3 Minutes! 💤 Newborn Sleep…](https://www.youtube.com/watch?v=22SPWR7nyfM) | Mother & Baby… | 18,700 | 947,034 | 50.6 | ×25.2 | 7,658.0 | 122.7분 | 2026-06-22 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 660 | [[감동음악]🎵듣는 순간 가슴이 먹먹해진다… 김호중 × 이애숙 《나의 조국은》 감동 실황 ∣ 천상의 목소리 …](https://www.youtube.com/watch?v=FAMrq6SXxys) | 🎧 Sound Rest | 2,710 | 137,245 | 50.6 | ×468.4 | 826.9 | 4.5분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 612/614 |
| 661 | [🎵 내려놓아라 ∣ 신나는 불교 EDM 트로트 ∣ 근심 걱정 다 내려놔라](https://www.youtube.com/watch?v=-y3mLSiAcU0) | 극락가요 | 393 | 19,877 | 50.6 | ×13.5 | 153.0 | 4.5분 | 2026-06-16 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 7/7 |
| 662 | [Deep work focus music for productivity ~ Ambient study musi…](https://www.youtube.com/watch?v=Bk-0NZHRPFA) | Work Mode Aud… | 11,500 | 576,731 | 50.1 | ×112.9 | 4,169.7 | 91분 | 2026-06-08 | 3. 공부·집중·작업 | 음악 | 설명 | 254/258 |
| 663 | [Beautiful September Autumn Forest 4K 🍁 Peaceful Nature Soun…](https://www.youtube.com/watch?v=RJma4cwfqIY) | Nature's Have… | 2,730 | 136,093 | 49.9 | ×36.7 | 3,169.0 | 154.8분 | 2026-09-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 49/50 |
| 664 | [𝙋𝙇𝘼𝙔𝙇𝙄𝙎𝙏 찻집 리틀 포레스트](https://www.youtube.com/watch?v=9NAEMS-BJT0) | off frame | 3,450 | 170,876 | 49.5 | ×82.8 | 1,316.1 | 78.8분 | 2026-06-16 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 129/133 |
| 665 | [Lightning — Romantic Ambient Pop & 80s Synth Ballad ∣ Thoma…](https://www.youtube.com/watch?v=2x_gLGrUdoY) | Thomas J. Cole | 4,040 | 198,954 | 49.2 | ×84.0 | 6,455.2 | 5분 | 2026-09-23 | 12. 커버·노래 부르기 | 음악 | 설명 | 94/97 |
| 666 | [💖 최고의 트로트 명곡 30곡 ∣ 중장년 애창곡 ∣ 운전·카페·휴식 음악 ∣ 안동역에서 미운사랑 홍시 진또…](https://www.youtube.com/watch?v=Tbtq8pWkeEk) | 달빛머문 새벽세시 | 1,050 | 50,949 | 48.5 | – | 1,765.9 | 98.2분 | 2026-09-25 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 6/6 |
| 667 | [Romantic Era Adagios (Cello, Violin & Piano) — Most Beautif…](https://www.youtube.com/watch?v=Dd3djaUS3Fw) | Classical Ada… | 13,100 | 635,479 | 48.5 | ×1,445.9 | 4,021.3 | 256.8분 | 2026-05-19 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 187/187 |
| 668 | [9 Adagios in Romantic Style ∣ AI Music ∣ Cello & Piano](https://www.youtube.com/watch?v=N4UaovHvFPE) | Vesper Classi… | 16,400 | 790,814 | 48.2 | ×1,245.4 | 4,601.4 | 28분 | 2026-05-05 | 14. AI 음악 | AI 음악 | 설명 | 421/421 |
| 669 | [ᴘʟᴀʏʟɪsᴛ ∣ 🌊푸른 바다처럼 시원한 7월 여돌 뮤직비디오 플리 ∣ 여름 청량 최신 걸그룹 인기곡 뮤…](https://www.youtube.com/watch?v=2EbdnZvOSwc) | 마쁠(MA-PLE·KPO… | 25,000 | 1,201,306 | 48.0 | ×7.4 | 12,652.6 | 127.2분 | 2026-07-21 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 84/85 |
| 670 | [【Playlist】Shamisen Rock You’ll Want to Replay ∣ Female Voca…](https://www.youtube.com/watch?v=skyHiOHKUJI) | Geisha Girl | 15,500 | 738,448 | 47.6 | ×63.1 | 4,369.8 | 111.1분 | 2026-05-08 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 193/194 |
| 671 | [Bamboo Water + Tibetan Zen Sounds ∣ Cleanse Aura & Space ∣ …](https://www.youtube.com/watch?v=oA7EmuZ7JCU) | Serene Vibes | 15,700 | 743,366 | 47.4 | ×70.4 | 4,510.2 | 184.3분 | 2026-05-12 | 1. 수면·명상·힐링 | 음악 | 설명 | 204/204 |
| 672 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=3k0BBE7e6TA) | Z B Official … | 22,700 | 1,072,771 | 47.3 | ×3,136.8 | 13,913.4 | 8분 | 2026-08-08 | 3. 공부·집중·작업 | 음악 | 설명 | 75/78 |
| 673 | [조용히 틀어뒀는데 끝까지 듣게 되는 노래 ㅣ오늘 고생한 당신을 위한 편안한 올드팝 라디오 ㅣ 7080 감성…](https://www.youtube.com/watch?v=ej-ck75-Nps) | Plain Pop | 4,250 | 200,683 | 47.2 | ×45.0 | 1,317.1 | 85.2분 | 2026-05-24 | 9. 가요·발라드·트로트 | 음악 | 설명 | 156/156 |
| 674 | ["सुकून भरी रातें 🌙 ∣ Romantic Hindi LoFi Songs ∣ Relaxing S…](https://www.youtube.com/watch?v=YtyLIn9mrcw) | Hindi Tuning | 25,200 | 1,177,897 | 46.7 | ×158.5 | 7,280.0 | 110분 | 2026-05-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 160/160 |
| 675 | [Cinematic Piano Meets Melodic Techno 🌌 ∣ Neo Classic Pulse …](https://www.youtube.com/watch?v=gSn_K5j9uB8) | Neo Classic P… | 4,820 | 224,808 | 46.6 | ×75.5 | 2,620.3 | 45.2분 | 2026-07-30 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 166/167 |
| 676 | [카페음악 ☕ 5월의 카페에서 잔잔하게 듣기 좋은 음악 🌿 7080 카페음악모음 🎶 중년을 위한 감성 카페 …](https://www.youtube.com/watch?v=5-b-PY1I2ss) | Cozy Cafe Mus… | 3,870 | 180,351 | 46.6 | ×87.6 | 1,046.1 | 12.8분 | 2026-05-04 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 19/19 |
| 677 | [𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩 ∣ 상큼하게 톡 터지는 딸기 에이드와 느린 독서 *'~*-⋆._.-*~⋆ ∣ 카페 플리 ∣…](https://www.youtube.com/watch?v=L1E4rkvGo-Y) | BlueDot Diary | 6,610 | 307,665 | 46.5 | ×111.5 | 2,632.5 | 123.4분 | 2026-06-29 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 75/75 |
| 678 | [[playlist] 상큼 달콤 행복의 피아노 음악🍋 아이의 정서발달을 위한 멜로디🎹 행복해지는 마법같은 영…](https://www.youtube.com/watch?v=PxIbP-Lv3EQ) | 베베집 bebe zip | 8,430 | 392,069 | 46.5 | ×49.5 | 3,397.4 | 91분 | 2026-06-30 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 0/0 |
| 679 | [“사는 게 힘들수록, 그 시절 노래가 더 그립습니다…”｜가슴 저리는 7080 추억의 명곡모음｜슬로우 블루스…](https://www.youtube.com/watch?v=uS61Sf1rAsQ) | 추억의 멜로디 | 4,580 | 212,653 | 46.4 | ×24.1 | 2,895.4 | 85.9분 | 2026-08-11 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 84/88 |
| 680 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=lXbnhKzEQl8) | Click Bollywo… | 27,800 | 1,281,980 | 46.1 | ×10,683.2 | 16,601.5 | 8.1분 | 2026-08-08 | 3. 공부·집중·작업 | 음악 | 설명 | 73/80 |
| 681 | [途中広告なし【カフェBGM】ひとり静かな喫茶店｜のんびり過ごす午後の時間｜作業用・読書・リラックス｜Cafe Musi…](https://www.youtube.com/watch?v=QgtDgADXHS4) | Kokoro Music … | 21,800 | 1,000,775 | 45.9 | ×50.8 | 8,271.7 | 120.9분 | 2026-06-25 | 2. 자연 소리·백색소음 | 음악 | 설명 | 166/166 |
| 682 | [[KPOP playlist] 난리도 아닌 감다살 케이팝 노동요](https://www.youtube.com/watch?v=AnsLD0Klc6s) | 오이는빼주세요 | 13,800 | 626,064 | 45.4 | ×53.5 | 4,645.1 | 59.1분 | 2026-06-11 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 없음 | 47/47 |
| 683 | [Deep Work Music ~ Midnight City Ambience for Deep Focus ~ C…](https://www.youtube.com/watch?v=czMO-L42nnc) | Focus Room | 25,800 | 1,170,024 | 45.4 | ×135.4 | 7,187.8 | 132.4분 | 2026-05-14 | 2. 자연 소리·백색소음 | 음악 | 설명 | 112/117 |
| 684 | [Craig David – INSOMNIA 🌙 ∣ Deep Bass EDM Remix ∣ Feel The N…](https://www.youtube.com/watch?v=hymSZZ0mX5U) | musik story🎧 | 12,000 | 543,842 | 45.3 | ×53.6 | 7,427.2 | 4분 | 2026-08-12 | 11. 힙합·R&B·EDM | 음악 | 설명 | 76/78 |
| 685 | [ㅤㅤㅤ](https://www.youtube.com/watch?v=8k5vqajrHVw) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 38,800 | 1,756,066 | 45.3 | ×324.5 | 25,136.1 | 120.7분 | 2026-08-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 4,300/4,313 |
| 686 | [Beautiful girl and inspiring piano music that help you love…](https://www.youtube.com/watch?v=6oZwrM-i8XU) | Benjamin Elie | 295 | 13,349 | 45.2 | ×2.2 | 364.5 | 4.8분 | 2026-09-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 4/4 |
| 687 | [마음도 휴식이 필요해요 BGM (플루트 연주) 🎵 조용한 숲과 호수의 휴식](https://www.youtube.com/watch?v=pzBSdxT3Bp4) | 느린풍경이야기 | 1,060 | 47,926 | 45.2 | ×879.4 | 313.8 | 39.6분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 21/21 |
| 688 | [비 오는 밤의 라흐마니노프 ∣ 깊고 잔잔한 아다지오 1시간](https://www.youtube.com/watch?v=HNgBqMnvUcU) | Minimal Class… | 7,940 | 358,301 | 45.1 | ×44.1 | 2,423.1 | 60.2분 | 2026-05-29 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 341/342 |
| 689 | [듣다 보면 끝까지 듣게 되는 명품 보컬 ∣ 7080 슬로우 레게・레트로 락발라드・Love Song・Vint…](https://www.youtube.com/watch?v=V9FOduIEv6w) | afterparis | 7,510 | 338,351 | 45.0 | ×25.8 | 2,983.6 | 82.8분 | 2026-07-02 | 9. 가요·발라드·트로트 | 음악 | 설명 | 183/186 |
| 690 | [𝑃𝑙𝑎𝑦𝑙𝑖𝑠𝑡 느좋 도우인 플리](https://www.youtube.com/watch?v=muaiYrT3glM) | 진구달려 | 6,350 | 285,632 | 45.0 | ×5.7 | 3,482.8 | 14.7분 | 2026-08-03 | 기타 | 플레이리스트·모음 | 없음 | 52/55 |
| 691 | [🎵듣는 순간 소름… 김호중·허종훈·임경택·임창한 남성4중창 레전드 공연 ∣ 김호중의 폭발적 테너… ‘오 나…](https://www.youtube.com/watch?v=ypW1MoCFDA8) | 🎧 Sound Rest | 2,710 | 121,818 | 45.0 | ×415.8 | 797.3 | 13.9분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 182/184 |
| 692 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 교토의 작은 카페, 말차향 재즈 🍵🎧 抹茶オーツラテ](https://www.youtube.com/watch?v=vLX3-MrBXFk) | 아오링고 잡화점 AORI… | 13,900 | 623,190 | 44.8 | ×29.5 | 9,387.4 | 292.4분 | 2026-08-18 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 114/123 |
| 693 | [마음이 편안해지는 명품 아침 클래식 ㅣ듣기만 해도 행복해지는 클래식 명곡](https://www.youtube.com/watch?v=jhz1rDyH7gc) | Aria classic … | 2,600 | 116,468 | 44.8 | ×21.0 | 1,233.2 | 59.4분 | 2026-07-21 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 18/18 |
| 694 | [𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 듣자마자 행복해질거야🍦☀️ 요즘 감성 노래 모음 ∣ 하루 종일 듣기 좋은 팝송 플레이리스트](https://www.youtube.com/watch?v=4zc4GyIQPco) | seroma room | 16,700 | 747,282 | 44.8 | ×80.0 | 5,524.0 | 599.4분 | 2026-06-11 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 62/63 |
| 695 | [여인 – 우리 가슴속 깊이 박혀 있던 그 노래, 듣는 순간 그 시절로 돌아갑니다, 이어폰 필수… 👉 첫 소…](https://www.youtube.com/watch?v=yQSP0R8pDqg) | 혼자 듣는 노래 | 8,220 | 366,559 | 44.6 | ×61.5 | 3,176.3 | 109.5분 | 2026-06-30 | 기타 | 음악 | 설명 | 104/104 |
| 696 | [Harmony Of Seasons ∣ DVE ∣ Ultimate Classical Piano Collect…](https://www.youtube.com/watch?v=P4H9CSSCuQg) | DVE | 2,360 | 104,470 | 44.3 | ×2,429.5 | 1,970.4 | 15.8분 | 2026-09-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 180/183 |
| 697 | [TIME ALONE WITH GOD - Soaking worship instrumental ∣ Prayer…](https://www.youtube.com/watch?v=uqC91GqvvQg) | Calm Divine F… | 21,700 | 947,551 | 43.7 | ×56.4 | 10,324.3 | 67.1분 | 2026-07-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 515/537 |
| 698 | [[Playlist] 기분 좋아지는 산뜻한 유럽 아침 앙상블 ∣ Morning Classical Ensemb…](https://www.youtube.com/watch?v=fdPFoR4XjNQ) | okply | 15,700 | 683,010 | 43.5 | ×86.6 | 4,142.9 | 80.8분 | 2026-05-12 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 325/332 |
| 699 | [유어아너 허남준이 말아주는 나쁜남자 PLAYLIST 🖤 ㅣ A Dark Bad Boy Playlist In…](https://www.youtube.com/watch?v=0YV2RKwLls0) | 허남준 팬페이지 허남준독… | 5,050 | 219,012 | 43.4 | – | 1,534.8 | 18.4분 | 2026-06-03 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 493/494 |
| 700 | [The Last Dance Before Dawn ∣ Dark Neoclassical music](https://www.youtube.com/watch?v=wy2IX-zmEXo) | Kingdom of Da… | 13,900 | 602,887 | 43.4 | ×155.1 | 3,784.2 | 107.1분 | 2026-05-18 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 653/656 |
| 701 | [[𝑬𝑽𝑬𝑹𝒀𝑫𝑨𝒀, 𝑷𝑰𝑨𝑵𝑶] 몽글몽글🩵 여름에 듣기 좋은 피아노 연주곡 10시간 모음 (중간광고없음, …](https://www.youtube.com/watch?v=5lWOn3zHsI0) | Everyday, Pia… | 5,490 | 237,545 | 43.3 | ×10.3 | 1,742.0 | 614.5분 | 2026-06-09 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 20/20 |
| 702 | [Playlist ∣ 매장을 세련되게 만드는 명품 그루브 🖤🎧 ∣ HIPHOP∙R&B MIX ∣ 매장음악∙카…](https://www.youtube.com/watch?v=h84x1mhg5C4) | hipnb groove | 4,640 | 200,262 | 43.2 | ×31.6 | 1,155.0 | 152.2분 | 2026-05-03 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 32/32 |
| 703 | [Relaxing Cha-Cha-Cha Swing on the Beautiful Beach – Latin R…](https://www.youtube.com/watch?v=f3zh_3lwiEI) | Grateful For … | 16,800 | 724,443 | 43.1 | ×638.3 | 4,475.7 | 63.8분 | 2026-05-15 | 기타 | 정보·해설 | 설명 | 194/195 |
| 704 | [그레고리오성가*한국어* 주여 자비를 베푸소서 #가톨릭성가#그레고리오성가#성가미사#기도음악#묵상음악#천주교성…](https://www.youtube.com/watch?v=9qbqShZRPYw) | DIMOTEO RECOR… | 4,510 | 193,980 | 43.0 | ×102.1 | 1,115.2 | 82.1분 | 2026-05-03 | 15. CCM·찬양·국악… | 음악 | 설명 | 516/521 |
| 705 | [Golden Horizon ∣ Cinematic Sci-Fi Ambient Music — Utopian F…](https://www.youtube.com/watch?v=QcVRYKcCIZ8) | Cosmic Infini… | 3,060 | 131,444 | 43.0 | ×156.7 | 787.9 | 13.2분 | 2026-05-10 | 3. 공부·집중·작업 | 음악 | 설명 | 109/109 |
| 706 | [그냥 틀어두기 좋은 감성 팝송 ☕🌿 12hr Cozy Cafe BGM • ep.110](https://www.youtube.com/watch?v=sDuu-v_gUjw) | winterbudz | 5,380 | 230,837 | 42.9 | ×63.0 | 1,387.6 | 699.6분 | 2026-05-10 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 300/300 |
| 707 | [The Quiet Night Medieval Village ∣ Relaxing Fantasy Medieva…](https://www.youtube.com/watch?v=dJ5VtIE3kwU) | Fantasy Medie… | 21,400 | 911,802 | 42.6 | ×130.1 | 7,549.1 | 146.7분 | 2026-06-25 | 3. 공부·집중·작업 | 음악 | 설명 | 189/193 |
| 708 | [사랑했어요 - 김현식 ∣ 가슴 깊이 남은 진한 그리움과 아련한 추억 #윤가연 COVER](https://www.youtube.com/watch?v=2VFOp-WbafE) | GAYEON YOON | 30,300 | 1,284,495 | 42.4 | ×52.5 | 8,920.3 | 5.2분 | 2026-06-02 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 115/124 |
| 709 | [Clear Negative Thoughts: Krishna Flute & Sitar to Quiet Min…](https://www.youtube.com/watch?v=ugG3qiHWEak) | Healing Raga … | 24,500 | 1,033,917 | 42.2 | ×76.2 | 13,919.3 | 65.3분 | 2026-08-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 144/145 |
| 710 | [전율 돋는 폭발적 감성 ⚡ 대한민국 락발라드 끝판왕! M.C The Max '잠시만 안녕' 커버 ∣ 김별이](https://www.youtube.com/watch?v=QK3Mxw--VFg) | 김별이 | 6,130 | 258,514 | 42.2 | ×57.9 | 4,503.4 | 5.4분 | 2026-08-27 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 32/34 |
| 711 | [일상에 틀어 놓는 잔잔한 찬송가 연속 듣기ㅣ어쿠스틱 편곡ㅣ3시간ㅣ중간 광고 없음ㅣ내 영혼이 은총 입어·내 …](https://www.youtube.com/watch?v=EwY1Z6_6H3I) | ALL THAT HYMN… | 7,240 | 304,747 | 42.1 | ×113.2 | 5,838.6 | 197.6분 | 2026-09-02 | 15. CCM·찬양·국악… | 커버·직접 부른 노래 | 설명 | 152/159 |
| 712 | [[Playlist] 로제 재즈 플레이리스트 🌹🎷 ∣ ROSÉ Jazz Playlist ∣ 재즈 커버](https://www.youtube.com/watch?v=ZqL7hDxAlis) | PLYINK 플링크 | 8,540 | 357,080 | 41.8 | ×5.5 | 4,400.0 | 110.8분 | 2026-08-04 | 7. 재즈·보사노바 | 커버·직접 부른 노래 | 설명 | 116/118 |
| 713 | [Ancient Chinese Zen Music🍃Bamboo Flute, Erhu & Guzheng🍃Rela…](https://www.youtube.com/watch?v=CKQuvdIKXgU) | Sound to Peac… | 46,300 | 1,934,584 | 41.8 | ×849.8 | 11,859.2 | 184.4분 | 2026-05-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 592/603 |
| 714 | [ENIGMA VOICES IN THE DARK 🌑 Mystical Ambient Music](https://www.youtube.com/watch?v=fOqrhVkQOh4) | The Sound Pal… | 9,630 | 401,108 | 41.6 | ×124.3 | 2,422.8 | 8분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 169/170 |
| 715 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 틀기만 해도 기분이 좋아지는 플리☀️🌿 (광고없음) 국내 노래 모음](https://www.youtube.com/watch?v=9aeCgBBnmYI) | 오늘의 플리 | 6,960 | 289,723 | 41.6 | ×32.2 | 1,723.7 | 617.4분 | 2026-05-09 | 기타 | 플레이리스트·모음 | 없음 | 27/27 |
| 716 | [ray 【カフェ風アレンジ】 / Remix / 超かぐや姫！](https://www.youtube.com/watch?v=js2syT4l9lc) | Remix中谷 | 5,530 | 229,342 | 41.5 | ×2.7 | 1,645.2 | 12분 | 2026-06-06 | 기타 | 정보·해설 | 설명 | 162/162 |
| 717 | [디지몬 OST - 날 지켜줘 (벅차오르는 파워 락 발라드 어레인지 커버) ∣ GrangChe.Ver](https://www.youtube.com/watch?v=iWfeWC28USw) | GrangChe | 21,700 | 895,962 | 41.3 | ×83.8 | 5,557.5 | 4.8분 | 2026-05-16 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 233/236 |
| 718 | [@노노뮤직#피아노협주곡 #힐링음악 #감성피아노 #클래식음악 #휴식음악#명상음악 #잔잔한음악 #오케스트라 #…](https://www.youtube.com/watch?v=aLyOUOXr5F4) | 노노스튜디오 | 462 | 19,019 | 41.2 | ×119.6 | 129.4 | 30분 | 2026-05-30 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 9/9 |
| 719 | [듣자마자 학창시절 떠오르는 노래 🎧 싸이월드 감성 PART 4](https://www.youtube.com/watch?v=F-0JE3Byo9U) | 소꿀 TV | 18,400 | 749,871 | 40.8 | – | 4,563.2 | 82.6분 | 2026-05-12 | 기타 | 플레이리스트·모음 | 설명 | 50/53 |
| 720 | [Relaxing Piano Music for Inner Peace, Meditation, Stress Re…](https://www.youtube.com/watch?v=dljV0oqDztU) | Celestial Rel… | 12,300 | 499,274 | 40.6 | ×153.5 | 8,934.3 | 127.7분 | 2026-08-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 236/254 |
| 721 | [the best classical music for concentration ∣ deep meditatio…](https://www.youtube.com/watch?v=ViZf4iovMMk) | StillSpace | 33,300 | 1,351,435 | 40.6 | ×332.3 | 8,125.5 | 61.4분 | 2026-05-11 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 608/616 |
| 722 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 우린 아직 흑백영화처럼 사랑하고](https://www.youtube.com/watch?v=71_AXp38B7M) | 세봄 | 14,300 | 572,591 | 40.0 | ×13.9 | 3,760.1 | 17.1분 | 2026-05-25 | 기타 | 플레이리스트·모음 | 설명 | 28/29 |
| 723 | [The Sound Your Brain Needs Right Now 🌿 Deep Healing Music ∣…](https://www.youtube.com/watch?v=rQ5bIFKQoUc) | Osen Moonlight | 11,800 | 467,376 | 39.6 | ×143.5 | 7,818.4 | 107분 | 2026-08-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 128/173 |
| 724 | [Fresh Mind Relaxing 💗 ∣ Slowed + Reverb Lofi Mix for Calm, …](https://www.youtube.com/watch?v=70p4fSeLZ3I) | Vansh Lofi | 29,500 | 1,157,911 | 39.2 | – | 8,110.7 | 15분 | 2026-06-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 46/46 |
| 725 | [백 번을 들어도 후회없을 노래🎵트로트 거친 보이스 @1980통기타 음악 @1980guitar playlis…](https://www.youtube.com/watch?v=ZVTFRwA3r14) | 1980통기타 | 12,300 | 482,097 | 39.2 | ×54.7 | 4,570.2 | 29.9분 | 2026-07-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 107/109 |
| 726 | [Best Acoustic Songs of the 80s 🎸 Romantic Classics & Nostal…](https://www.youtube.com/watch?v=9tAdobkt1N0) | 80s Guitar Lo… | 23,800 | 916,901 | 38.5 | ×13.2 | 13,211.1 | 58.5분 | 2026-08-15 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 115/128 |
| 727 | [Rest Tonight In God's Love ∣ Christian Deep Sleep Worship M…](https://www.youtube.com/watch?v=nzc_yRoaBRI) | Midnight Sanc… | 22,800 | 877,149 | 38.5 | ×98.8 | 9,558.1 | 122.5분 | 2026-07-24 | 15. CCM·찬양·국악… | 음악 | 설명 | 332/337 |
| 728 | [🎧"세상에서 가장 애절한 목소리" 한 편의 영화 같은 무대, 그리고 가슴을 울리는 목소리…🎙️ 김정호 - …](https://www.youtube.com/watch?v=tjA0yWEZnu8) | 가슴을 울리는 락카페 | 11,300 | 434,541 | 38.5 | ×56.1 | 2,654.8 | 4.4분 | 2026-05-13 | 4. 카페·매장·라운지 | 커버·직접 부른 노래 | 설명 | 90/90 |
| 729 | [Dreams Never Sleep （映画『仮面ライダーゼッツ...](https://www.youtube.com/watch?v=9nOX0zxrLfw) | YUTA - Topic | 24,300 | 928,184 | 38.2 | – | 10,013.6 | 4.4분 | 2026-07-23 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 730 | [[No Ads] Uplifting Morning Piano Music 🌿 ∣ Fresh & Positive…](https://www.youtube.com/watch?v=D8dWbYNFXKc) | Elise Piano ∣… | 25,700 | 979,554 | 38.1 | ×48.5 | 8,875.0 | 183.7분 | 2026-07-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 123/135 |
| 731 | [Oscar & Deep - Feeling Flow](https://www.youtube.com/watch?v=b_DXB1Dj4l8) | Oscar & Deep | 24,400 | 921,571 | 37.8 | ×32.8 | 5,459.0 | 7.5분 | 2026-05-08 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 90/90 |
| 732 | [Soulful Sufi Ghazal - सफर की धूप में साया तलाशते रह गए ∣ He…](https://www.youtube.com/watch?v=JI1OFbt7jRM) | SOUL VIBES IN… | 30,000 | 1,123,391 | 37.5 | ×20.4 | 7,125.7 | 6.4분 | 2026-05-19 | 기타 | 정보·해설 | 설명 | 345/346 |
| 733 | [【ケルト音楽】家事スイッチが入る🌿 朝の光が気持ちいいBGM｜Relax · Cafe Time](https://www.youtube.com/watch?v=TqiJnA1qm4s) | よもぎの作業用BGM | 12,400 | 463,813 | 37.4 | ×42.5 | 3,528.6 | 63.3분 | 2026-06-14 | 4. 카페·매장·라운지 | 음악 | 설명 | 172/173 |
| 734 | [기분이 산뜻해지는 재즈 찬송가 ∣ Hymn Jazz Playlist ∣ 공부·휴식·카페 BGM [2H] (…](https://www.youtube.com/watch?v=AZCxtUAYrUw) | DearHymn | 11,900 | 442,603 | 37.2 | ×10.7 | 2,598.1 | 120.5분 | 2026-05-06 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 107/110 |
| 735 | [🪷 이 노래 들으면 막힌 재물운이 술술 풀립니다 ∣ 부처님 대운 명호·진언 13곡 ∣ 관세음·지장·아미타 …](https://www.youtube.com/watch?v=ztFLgJ5idWI) | 연꽃법음 | 3,540 | 131,665 | 37.2 | ×142.3 | 805.8 | 55.7분 | 2026-05-13 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 827/827 |
| 736 | [Saxophone Love Songs ❤️ Best Romantic Saxophone Covers ∣ Re…](https://www.youtube.com/watch?v=Uea_DclFKjw) | Sax Chill Vib… | 28,700 | 1,065,994 | 37.1 | ×13.2 | 14,184.2 | 61분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 97/104 |
| 737 | [途中広告なし【カフェBGM】涼やかな夏カフェ｜木漏れ日の、心ほどける森カフェ時間｜作業用・読書・リラックス｜Cafe …](https://www.youtube.com/watch?v=3QKdiHlK6c4) | Kokoro Music … | 21,800 | 807,740 | 37.0 | ×41.0 | 8,415.1 | 122.5분 | 2026-07-20 | 2. 자연 소리·백색소음 | 음악 | 설명 | 73/73 |
| 738 | [Music for meditation, relaxation focus vibe ∣ deep sleep ∣ …](https://www.youtube.com/watch?v=Gsenq8igMJ0) | Healer of Bro… | 9,070 | 334,260 | 36.9 | ×718.8 | 1,889.9 | 61.5분 | 2026-04-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 192/192 |
| 739 | [hyper-focus. ∣ deep house music for coding](https://www.youtube.com/watch?v=uNw_a7HFwvg) | deep archive | 25,900 | 951,424 | 36.7 | ×96.6 | 6,924.3 | 148.4분 | 2026-06-08 | 3. 공부·집중·작업 | 음악 | 설명 | 274/277 |
| 740 | [𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 ∣ Vinyl Jazz Hiphop ∣ TOKYO ∣ Nujabes / MF Doom / …](https://www.youtube.com/watch?v=2bEmWCwdCds) | ICYFOG | 46,300 | 1,698,876 | 36.7 | ×128.3 | 13,556.2 | 206.5분 | 2026-06-21 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 102/108 |
| 741 | [Healing Music for Anxiety, Fears and Depression 🌿 Heals the…](https://www.youtube.com/watch?v=_SGd39jlrR8) | Peaceful Natu… | 2,920 | 107,124 | 36.7 | ×75.1 | 1,429.6 | 99.2분 | 2026-08-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 60/61 |
| 742 | ["매력있다 이 음색"#휴식음악#7080노래#어쿠스틱음악#힐링음악#수면음악#카페음악#7080발라드#명상음악#…](https://www.youtube.com/watch?v=CG3XI3D6gHg) | 7080 마로니에 통기타… | 389 | 14,128 | 36.3 | ×153.6 | 83.3 | 40.9분 | 2026-05-07 | 6. 피아노·클래식·연주곡 | 연주 | 설명 | 20/20 |
| 743 | [Barbaad (Dream Rock Remix) ∣ Soulful Atmospheric Cover](https://www.youtube.com/watch?v=FGvMCTLKFjo) | Dhun Tadka | 2,890 | 104,936 | 36.3 | ×22.9 | 615.0 | 4.8분 | 2026-05-06 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 21/21 |
| 744 | [JESUS CALM MY HEART - Instrumental Worship Music For Prayer](https://www.youtube.com/watch?v=GKDVqIGZ5GI) | One Thing | 17,700 | 637,668 | 36.0 | ×67.5 | 4,229.2 | 63.4분 | 2026-05-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 186/188 |
| 745 | [Sweetest Best Friends Lullaby 🐶🐱💤∣ Calm Sleep Music for Kid…](https://www.youtube.com/watch?v=P5zkPSvY368) | Kidz Wonder T… | 20,800 | 746,970 | 35.9 | ×1.9 | 4,353.7 | 9분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |
| 746 | [music for overthinkers ∣ felt piano & cello for deep focus](https://www.youtube.com/watch?v=EZeW4Sfy8CE) | OTIUM | 28,600 | 1,018,888 | 35.6 | ×130.0 | 9,545.7 | 60.8분 | 2026-07-09 | 3. 공부·집중·작업 | 음악 | 설명 | 428/443 |
| 747 | [이 세상 미련 없이 가련다 [국악 트로트] 가슴 시린 중년 트토르](https://www.youtube.com/watch?v=XcyHeiPdmDc) | 인생트로트 라운지 | 4,230 | 150,481 | 35.6 | – | 933.0 | 5.8분 | 2026-05-16 | 9. 가요·발라드·트로트 | 음악 | 설명 | 19/19 |
| 748 | ["술 한잔 생각나는 깊은 목소리..." 첫 소절 부터 아련해지는 님은 먼 곳에(블루스 Ver.)](https://www.youtube.com/watch?v=M-8Z69t7Smo) | 세월블루스 | 21,100 | 747,792 | 35.4 | ×7.4 | 4,300.0 | 4.4분 | 2026-05-03 | 기타 | 한 곡 | 설명 | 193/194 |
| 749 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 텐션 MAX🔥핫한 걸그룹 인기곡 노동요 뮤비 플리☀️여자아이돌 노래모음 ∣ 4K UHD](https://www.youtube.com/watch?v=u7Mu1aDSaR4) | 마쁠(MA-PLE·KPO… | 25,000 | 878,648 | 35.1 | ×5.4 | 5,964.2 | 135.4분 | 2026-05-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 74/74 |
| 750 | [【夜のリラックスBGM】星空にひたるだけの夜。/A night in starlight｜ピアノ 1時間](https://www.youtube.com/watch?v=wIaFkPnk9oA) | FeelTone | 26,400 | 925,965 | 35.1 | ×129.3 | 5,208.5 | 62분 | 2026-04-29 | 기타 | 정보·해설 | 설명 | 179/181 |
| 751 | [AMAPIANO MIX 2026 ∣ 🔥DEEP HOUSE MUSIC VIBES ∣ BEST AFRO PIA…](https://www.youtube.com/watch?v=pyDSBs4URas) | YANOS NATION | 22,600 | 790,949 | 35.0 | ×360.8 | 5,144.1 | 20.9분 | 2026-05-23 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 160/160 |
| 752 | [𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩 ∣ 아말피 테라스에서 봉골레와 와인 한 잔 ∣ 𝘚𝘰𝘧𝘵 𝘉𝘰𝘴𝘴𝘢 𝘑𝘢𝘻𝘻🍋🥂 ∣ 카페 플…](https://www.youtube.com/watch?v=ZgR4pGSybaw) | BlueDot Diary | 6,610 | 230,967 | 34.9 | ×83.7 | 2,160.5 | 142.8분 | 2026-07-09 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 45/45 |
| 753 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 여름 새벽향 낭만 플리](https://www.youtube.com/watch?v=9qwdolh_Jow) | 세봄 | 14,300 | 498,135 | 34.8 | ×12.1 | 3,453.7 | 18.9분 | 2026-06-02 | 기타 | 플레이리스트·모음 | 설명 | 17/17 |
| 754 | [Bach Style ∣ 마음이 편안해지는 바흐풍 잔잔한 클래식 🌿 [중간광고없음] ∣ 힐링음악, 일상 BG…](https://www.youtube.com/watch?v=hbmQRFw1InE) | Elise Piano ∣… | 25,700 | 895,165 | 34.8 | ×44.3 | 5,380.8 | 130.9분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 341/363 |
| 755 | [🎵 신나는 복고댄스 Playlist ∣ 추억 감성 뉴트로 댄스곡 모음🎧](https://www.youtube.com/watch?v=WjxmNnlQ8LU) | 7080 정미의 가요방 | 9,470 | 326,984 | 34.5 | ×21.8 | 1,970.3 | 15분 | 2026-05-11 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 217/217 |
| 756 | [Persian & Spanish Fusion Relaxing Music 4K ∣ Persian Gulf &…](https://www.youtube.com/watch?v=UH3bfZ6Rb9E) | WolfRelaxMusi… | 25,400 | 875,698 | 34.5 | ×282.3 | 4,983.0 | 63.7분 | 2026-05-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 857/864 |
| 757 | [Oscar & Deep - Closer To My Dreams](https://www.youtube.com/watch?v=YVYkI9z2Evk) | Oscar & Deep | 24,400 | 839,398 | 34.4 | ×30.0 | 9,047.5 | 9.8분 | 2026-07-23 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 45/45 |
| 758 | [Zulu Spirit — African Spiritual Ambient Music for Healing &…](https://www.youtube.com/watch?v=cOLt_w3nBx4) | Echo Sanctum | 9,200 | 315,177 | 34.3 | ×23.2 | 1,928.6 | 180.8분 | 2026-05-13 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 228/229 |
| 759 | [임영웅, 신곡 〈그대 행복이면 됐소〉 발표! 그대만 행복하면 됐소…](https://www.youtube.com/watch?v=p8MCdXUSFmI) | 감성트롯다방 | 4,940 | 169,012 | 34.2 | ×144.9 | 1,507.5 | 6.4분 | 2026-07-04 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 262/265 |
| 760 | ["첫 소절 듣자마자 가슴 한쪽이 먹먹해지네요.." 세월 묻은 목소리로 다시부른 연인(블루스 Ver.)](https://www.youtube.com/watch?v=y7CUK-q-f1s) | 세월블루스 | 21,100 | 721,436 | 34.2 | ×7.1 | 4,078.4 | 4.6분 | 2026-04-30 | 기타 | 정보·해설 | 설명 | 274/277 |
| 761 | [Rest Your Mind ∣ Soothing Indian Classical Music for Stress…](https://www.youtube.com/watch?v=56ymDCWXGZk) | Essential Ind… | 19,400 | 662,667 | 34.2 | ×453.0 | 4,705.0 | 17.7분 | 2026-06-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 93/93 |
| 762 | [쏟아지는 빗소리에 복잡한 생각은 내려 놓으세요 ∣ 수면유도 백색소음 힐링 ASMR](https://www.youtube.com/watch?v=9TqDVzWADgQ) | Cozy Rainy Da… | 9,730 | 330,637 | 34.0 | ×41.0 | 2,364.7 | 360.1분 | 2026-06-06 | 1. 수면·명상·힐링 | 자연 소리·백색소음 | 설명 | 97/102 |
| 763 | [2000~2010 K-POP 감성 모음 🎶 ∣ 듣자마자 떠오르는 그 시절 노래들 – Geuri-um Stu…](https://www.youtube.com/watch?v=9CHBQsxSNa4) | Geuri-um Stud… | 8,760 | 297,548 | 34.0 | ×79.3 | 1,677.2 | 87.5분 | 2026-04-29 | 10. 팝송·K팝·J팝 | 음악 | 설명 | 41/41 |
| 764 | [주부들이 엄선한 감성 팝송 Best 26 ∣ EverPop 레트로 팝 컬렉션 ∣ 7080 올드팝송 ∣ 추억…](https://www.youtube.com/watch?v=JZH9pZhtl9I) | 추억의 올드팝 EverP… | 16,200 | 550,019 | 34.0 | ×26.0 | 5,732.9 | 97.8분 | 2026-07-20 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 125/131 |
| 765 | [Snowy Russian Night ❄️ Tchaikovsky-Inspired Winter Orchestr…](https://www.youtube.com/watch?v=R3xYX9LJ_hs) | 모노로그 레코드 | 27,700 | 928,935 | 33.5 | ×57.9 | 5,804.2 | 61분 | 2026-05-17 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 1,150/1,157 |
| 766 | [[Playlist] 라흐마니노프의 깊은 그리움 ∣ 멀리서 들려오는 서정적인 선율 (Rachmaninoff …](https://www.youtube.com/watch?v=vcpBmyFBJos) | The Clavis | 20,200 | 674,455 | 33.4 | ×29.2 | 5,291.7 | 97.2분 | 2026-06-18 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 551/555 |
| 767 | [Chinese Zen Music🎵: Bamboo flute, erhu & Guzheng ∣ Relaxing…](https://www.youtube.com/watch?v=6UtPuJcUsyI) | ZenFlute | 33,600 | 1,121,069 | 33.4 | ×162.0 | 7,738.8 | 90.2분 | 2026-06-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 744/758 |
| 768 | [A Quiet Rainy Afternoon in a 1958 Vermont Town ∣ Relaxing V…](https://www.youtube.com/watch?v=zjgFke-YGZk) | The Serene So… | 34,000 | 1,131,892 | 33.3 | ×60.7 | 6,471.5 | 64분 | 2026-05-02 | 기타 | 음악 | 설명 | 1,843/1,858 |
| 769 | [DUNE Music for Meditation, Rest & Focus ∣ 3 Hours ∣ No Ads](https://www.youtube.com/watch?v=qTdgu2POFlw) | Empyreal Ambi… | 14,700 | 487,670 | 33.2 | ×21.0 | 6,782.3 | 180분 | 2026-08-13 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 74/79 |
| 770 | [🌺 सर्व देवता हरेक बिहानको मन्त्र ∣ Morning Nepali Bhakti So…](https://www.youtube.com/watch?v=U984EoUC8Jo) | Bhajan Hub Ne… | 33,400 | 1,103,172 | 33.0 | ×207.2 | 7,221.7 | 13.6분 | 2026-05-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 760/761 |
| 771 | [𝐈𝐬 𝐭𝐢𝐦𝐞 𝐭𝐨 𝐫𝐞𝐥𝐚𝐱⎛˶’ᵕ’˶ ⎞♡.*･ﾟ](https://www.youtube.com/watch?v=a7psAnInAcI) | iamnotcute유유 | 13,800 | 450,856 | 32.7 | ×74.2 | 3,035.4 | 99.8분 | 2026-05-28 | 기타 | 정보·해설 | 설명 | 223/223 |
| 772 | [하루 끝에 듣는 힐링 발라드 🎶 광고 없는 감성 명곡 모음｜백지영, 성시경, 더원, 이승기, 김필, 양파,…](https://www.youtube.com/watch?v=85w3xNdP09U) | N Melody Ball… | 24,100 | 786,359 | 32.6 | ×130.4 | 5,679.9 | 49.8분 | 2026-06-07 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 없음 | 138/141 |
| 773 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 요즘 연남동 카페에서 듣기좋은 가을 감성 팝송 𝟏𝟎시간 (중간광고없음) 🍂☕ 작업 · 휴식…](https://www.youtube.com/watch?v=asmDdv4Dfig) | With Lofi Cafe | 5,100 | 166,413 | 32.6 | ×18.0 | 6,310.9 | 647.2분 | 2026-09-27 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 15/15 |
| 774 | [The Beatles on Abbey Road ∣ Greatest Hits in Quartet [No Mi…](https://www.youtube.com/watch?v=VGZ-Xzu73gg) | Golden Harmony | 19,500 | 633,143 | 32.5 | ×81.3 | 5,552.2 | 114.4분 | 2026-07-02 | 기타 | 음악 | 설명 | 299/302 |
| 775 | [Best Romantic Flute Instrumental Collection ❤️ ∣ Tum Aa Gay…](https://www.youtube.com/watch?v=taYeLCeWCd8) | Mansa Music W… | 10,700 | 344,976 | 32.2 | ×171.6 | 2,845.0 | 19.6분 | 2026-06-25 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 84/84 |
| 776 | [QUIET WITH JESUS - Instrumental Worship Music For Prayer](https://www.youtube.com/watch?v=2JsArLBjn70) | One Thing | 17,700 | 563,694 | 31.9 | ×59.7 | 3,948.0 | 60.3분 | 2026-06-03 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 119/119 |
| 777 | [celestial bloom 🌿∣ dreamy piano music reflected in dreamy w…](https://www.youtube.com/watch?v=coDaaicD9zM) | She of the Va… | 11,900 | 377,397 | 31.7 | ×57.7 | 4,298.6 | 36.4분 | 2026-07-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 124/127 |
| 778 | [Sky - 영원 ∣ 여성보컬 COVER ∣ 다시 들어도 가슴이 무너지는 명곡](https://www.youtube.com/watch?v=ETq8E35CSwk) | 연애상황극 | 11,100 | 351,855 | 31.7 | ×204.7 | 2,118.6 | 4.6분 | 2026-05-11 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 180/180 |
| 779 | [비 오는 날 듣기 좋은 화란 락발라드 모음 Vol.1 ☔7080 감성 Cover Collection](https://www.youtube.com/watch?v=c4hjZfzxkMM) | ​화란사운드® ∣ 보컬화란 | 17,600 | 556,336 | 31.6 | ×16.4 | 3,763.3 | 34분 | 2026-05-29 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 285/288 |
| 780 | [Anvarbek Xamroyev - Hayronman 2 (piano version)](https://www.youtube.com/watch?v=q-oZ8xry4MM) | Anvarbek Xamr… | 32,000 | 1,007,010 | 31.5 | – | 9,797.8 | 4.2분 | 2026-07-13 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 205/206 |
| 781 | [Deep Work Music – CEO Mode ∣ Strategic Clarity, Controlled …](https://www.youtube.com/watch?v=uX6jCay0c6I) | Deep Idle Room | 27,100 | 851,981 | 31.4 | ×216.4 | 5,368.7 | 92.4분 | 2026-05-18 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 475/484 |
| 782 | [😭 나훈아, 아들의 노래를 듣고 끝내 눈물을 흘리다… 가족 모두가 오열한 순간25](https://www.youtube.com/watch?v=keP33Q5JU_A) | 나훈아AI Korean … | 1,450 | 45,230 | 31.2 | ×80.3 | 445.9 | 6.5분 | 2026-07-14 | 기타 | 음악 | 설명 | 25/25 |
| 783 | [🍀 7월, 바다를 보며 들으니 이 노래 너무 좋다 ☕ 커피 한 잔과 함께하는 7080 추억의 올드팝 🎧](https://www.youtube.com/watch?v=q3iHXzi_Qn0) | 행운을담은 올드팝 | 6,190 | 191,920 | 31.0 | ×15.1 | 1,692.3 | 85.7분 | 2026-07-02 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 160/160 |
| 784 | [Peaceful Adventist Hymns Instrumental ∣ SDA Prayer Music fo…](https://www.youtube.com/watch?v=tj1FpWQsyCg) | Adventist Hym… | 38,700 | 1,199,115 | 31.0 | ×5.9 | 7,183.6 | 61분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 570/574 |
| 785 | [1 Hour Uplifting Morning Music ∣ Veena & Mridangam Indian C…](https://www.youtube.com/watch?v=7z7ol63jaGw) | Nadam | 19,300 | 596,743 | 30.9 | ×316.2 | 3,818.5 | 60.3분 | 2026-05-21 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 303/307 |
| 786 | [조선힙합 OFFICIAL 발표곡 중 인기곡만 모았습니다.](https://www.youtube.com/watch?v=fjjiznDoNEQ) | 조선힙합 Official | 30,000 | 927,149 | 30.9 | ×125.8 | 6,562.5 | 28.4분 | 2026-06-05 | 11. 힙합·R&B·EDM | 한 곡 | 설명 | 1,039/1,067 |
| 787 | [【GamePiano90min】「時の回廊」クロノ・トリガーゆっくり聴く432Hz Breathing Piano V…](https://www.youtube.com/watch?v=0sJ4qqIp3kk) | 水面こは(Minamo K… | 21,000 | 647,112 | 30.8 | ×195.4 | 3,846.4 | 90.5분 | 2026-05-09 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 200/206 |
| 788 | [[Playlist] 초록빛 싱그러운 아침에 듣는 모차르트 ∣ 독서와 사색을 위한 평온한 클래식 (Mozar…](https://www.youtube.com/watch?v=wMHsFC7-kUE) | The Clavis | 20,200 | 619,466 | 30.7 | ×26.8 | 4,473.8 | 94.3분 | 2026-06-07 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 315/319 |
| 789 | [Peaceful Piano with Rain Sounds 🎶 Relaxing Sleep Music & In…](https://www.youtube.com/watch?v=eUslSNm96D4) | Piano Rain Re… | 30,300 | 925,321 | 30.5 | ×66.5 | 6,687.7 | 206.7분 | 2026-06-07 | 1. 수면·명상·힐링 | 음악 | 설명 | 168/168 |
| 790 | [Chandrashekara Pahimam ∣ Lord Shiva Meditation Music ∣ Powe…](https://www.youtube.com/watch?v=9sk0msSGgfA) | Satya Devotio… | 3,390 | 103,275 | 30.5 | ×2.8 | 1,803.7 | 6.8분 | 2026-08-28 | 1. 수면·명상·힐링 | 음악 | 설명 | 23/23 |
| 791 | [BEST AMAPIANO MIX 2026 ∣ 1hr Of Deep House Amapiano Mix 35 …](https://www.youtube.com/watch?v=3-c885KEOaM) | AMAPIANO SANC… | 19,200 | 584,721 | 30.4 | ×42.5 | 3,785.0 | 65.5분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 긴 한 곡·반복 | 설명 | 137/137 |
| 792 | [붓꽃잎 편지∣[감성 음악]∣댄스 트로트∣서정적인 트로트](https://www.youtube.com/watch?v=K82Wh68Jvjc) | MusubiRain | 1,560 | 47,459 | 30.4 | ×133.3 | 470.1 | 5분 | 2026-07-15 | 9. 가요·발라드·트로트 | 음악 | 설명 | 26/26 |
| 793 | [막힌 운을 여는 산신기도｜백호 산신 가피로 액운소멸·복덕성취·재물운 발원](https://www.youtube.com/watch?v=ez0HnQ7tuPM) | 풍요와복덕의노래 | 2,560 | 77,419 | 30.2 | ×15.0 | 576.6 | 4.9분 | 2026-06-12 | 1. 수면·명상·힐링 | 음악 | 설명 | 584/590 |
| 794 | [샹송이 이렇게 까지 좋은줄 몰랐습니다. 아침부터 저녁까지 듣게되는 7080올드팝 샹송 ∣ 감성이 폭발한다](https://www.youtube.com/watch?v=ubP0xqEZxYo) | Midnight Melo… | 28,300 | 846,447 | 29.9 | ×246.0 | 5,045.4 | 81.5분 | 2026-05-09 | 9. 가요·발라드·트로트 | 정보·해설 | 설명 | 283/285 |
| 795 | [Study Focus Enhancement ∣ Classical Music for Deep Concentr…](https://www.youtube.com/watch?v=hUUBG_Nlwh4) | Classical Mind | 23,300 | 694,740 | 29.8 | ×304.6 | 4,473.3 | 139.4분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 184/186 |
| 796 | [잠 안 오 새벽, 깊은 허스키 보컬이 주는 위로 🌧️ 70s 빈티지 어쿠스틱 기타 BGM](https://www.youtube.com/watch?v=BQoJJ8V8TMg) | 조용한 그리움 | 21,800 | 649,649 | 29.8 | ×428.7 | 7,196.0 | 129.5분 | 2026-07-26 | 12. 커버·노래 부르기 | 음악 | 없음 | 106/117 |
| 797 | [잘 지내💬 아직 네가 있어 / I Hope You’re Doing Well ∣ Sad Korean Ball…](https://www.youtube.com/watch?v=PSnEIoFQB-0) | MusicSong | 7,420 | 220,334 | 29.7 | ×548.1 | 1,275.0 | 4.1분 | 2026-05-04 | 기타 | 음악 | 설명 | 94/94 |
| 798 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=634i1Q0C5UI) | Majnukhan | 36,300 | 1,075,952 | 29.6 | ×3,659.7 | 6,914.9 | 15.7분 | 2026-05-21 | 3. 공부·집중·작업 | 음악 | 설명 | 100/100 |
| 799 | [GOD IN ME - Soaking Worship Instrumental Presence of God ∣ …](https://www.youtube.com/watch?v=L-SoDe2nKoE) | Calm Divine F… | 21,700 | 643,151 | 29.6 | ×37.7 | 3,617.7 | 63.4분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 213/213 |
| 800 | [Chinese Sleep Music: Soft Guzheng & Ambient Pads ∣ Deep Nig…](https://www.youtube.com/watch?v=0ykSzpX6rzg) | Lotus Echo 莲之… | 17,200 | 507,797 | 29.5 | ×129.1 | 3,327.4 | 240.1분 | 2026-05-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 111/112 |
| 801 | [Paint It, Black – Dark Gothic Orchestral Cover ∣ Epic Cinem…](https://www.youtube.com/watch?v=zWArs5bT_Nc) | Mimousic | 27,300 | 803,232 | 29.4 | ×22.6 | 4,468.9 | 4.5분 | 2026-04-27 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 410/415 |
| 802 | [music for overthinkers — when the mind goes quiet ∣ deep fo…](https://www.youtube.com/watch?v=IsGUh_yMxDg) | StillSpace | 33,300 | 976,025 | 29.3 | ×240.0 | 5,504.3 | 85.2분 | 2026-04-30 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 310/311 |
| 803 | [𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩.°• 야호-!★⊹⋅ ˚💖 듣자마자 신나는 최신 여돌 플레이리스트](https://www.youtube.com/watch?v=v_AYwiX_XgI) | eon | 5,080 | 148,231 | 29.2 | ×8.8 | 1,091.0 | 81.8분 | 2026-06-10 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 16/16 |
| 804 | [15 Min 528Hz Self Healing Music 🌿 Calm Your Nervous System …](https://www.youtube.com/watch?v=HFW4awIfBmo) | Inner Healing… | 1,240 | 36,059 | 29.1 | ×23.5 | 1,136.9 | 15.5분 | 2026-09-22 | 1. 수면·명상·힐링 | 음악 | 설명 | 14/14 |
| 805 | [(WCS2026) VGC Masters Finals Battle Music - Pokémon Champio…](https://www.youtube.com/watch?v=B9Vi8BjqFoc) | RezyMania | 13,000 | 377,111 | 29.0 | ×67.0 | 7,378.5 | 5분 | 2026-09-03 | 기타 | 음악 | 설명 | 355/358 |
| 806 | [[Playlist] 여름향기 가득한 카페에서 듣기 좋은 음악 ∣ 잔잔한 감성팝 카페음악 🎧 ∣ Healin…](https://www.youtube.com/watch?v=hlxPD1XBS-A) | 낡은 레코드 | 8,930 | 258,781 | 29.0 | ×27.4 | 1,722.1 | 77.9분 | 2026-05-27 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 33/33 |
| 807 | [【4K/途中広告なし】がんばった自分を、休ませる夜｜自律神経を整える癒しのピアノBGM｜睡眠・リラックス用｜3時間](https://www.youtube.com/watch?v=TlPKpR7on9o) | Starry Note | 22,000 | 636,940 | 28.9 | ×60.1 | 5,450.4 | 192.8분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 199/203 |
| 808 | [🔥5 Musik Instrumen Sunda Modern yang Bikin Nagih ∣ BASS_DRUM](https://www.youtube.com/watch?v=zIrcdA2el3w) | BASS_DRUM | 16,700 | 479,005 | 28.7 | ×181.7 | 2,867.3 | 13.3분 | 2026-05-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 295/295 |
| 809 | [마지막 약속(1995) - 김정민 ∣ 여자보컬 리메이크 [원곡감성] Cover](https://www.youtube.com/watch?v=L7EUtPDVddY) | AuraAPT | 14,300 | 406,766 | 28.4 | ×24.2 | 4,288.5 | 5분 | 2026-07-21 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 41/44 |
| 810 | [그대 그리고 나(1988) - 소리새 ∣ Acoustic Cover ∣ 레트로카페](https://www.youtube.com/watch?v=CMDXDnLx3QA) | 레트로 카페 (Retro… | 12,100 | 336,565 | 27.8 | ×70.0 | 2,091.6 | 4분 | 2026-05-16 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 55/58 |
| 811 | [마음이 맑아지는 클래식 찬송가 🌿 ∣ 아침에 듣기 좋은 Morning Hymns for Peace & Co…](https://www.youtube.com/watch?v=j6H9mPj769A) | DearHymn | 11,900 | 330,928 | 27.8 | ×8.0 | 2,025.2 | 130.2분 | 2026-05-13 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 455/459 |
| 812 | [드루와자기 트로트 커버리믹스 총집합! 신나는 트로트 35곡 연속 듣기 🎶추억의 히트송 리믹스,레전드 트로트…](https://www.youtube.com/watch?v=al3dfBmH620) | 드루와자기 | 19,800 | 546,158 | 27.6 | ×1,627.9 | 3,554.5 | 136분 | 2026-05-23 | 5. 운동·드라이브·신나는 | 커버·직접 부른 노래 | 설명 | 236/236 |
| 813 | [#singer #kishan #maldhari માં મેલડી તારી કૃપા અપરંપાર #medi…](https://www.youtube.com/watch?v=by0Ok3JgV3o) | Maa Sikotar O… | 1,750 | 47,913 | 27.4 | ×28.0 | 361.3 | 10.2분 | 2026-06-13 | 1. 수면·명상·힐링 | 음악 | 없음 | 16/16 |
| 814 | [Heartbreaking 💔 lofi mashup 🎶 slowed + reverb songs ∣ study…](https://www.youtube.com/watch?v=RXYyvE4qRqs) | Click Bollywo… | 27,800 | 760,139 | 27.3 | ×6,334.5 | 7,926.2 | 7.8분 | 2026-07-20 | 3. 공부·집중·작업 | 음악 | 설명 | 46/46 |
| 815 | [비 오는 날 카페에서 듣기 좋은 추억의 노래 ∣ 계속 듣게 되는 7080 라디오 감성 올드팝](https://www.youtube.com/watch?v=riMgzQ7B4JA) | morgellia(모르겔… | 18,200 | 490,053 | 26.9 | ×59.5 | 3,114.2 | 165.9분 | 2026-05-19 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 313/315 |
| 816 | [Soothe Station - Andamanaya - Tagalog Version (Pakaranon Ba…](https://www.youtube.com/watch?v=4SWpVSbm4Qo) | Soothe Sta. | 28,900 | 774,222 | 26.8 | ×5.6 | 5,494.7 | 4.4분 | 2026-06-05 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 168/169 |
| 817 | [Your Soul Will Thank You For This ∣∣ DIVINE Krishna Dhun & …](https://www.youtube.com/watch?v=-gGLDLqN03M) | Krishna Lovers | 49,800 | 1,328,327 | 26.7 | ×358.6 | 8,410.0 | 30.6분 | 2026-05-19 | 기타 | 정보·해설 | 설명 | 1,350/1,359 |
| 818 | [Mortal Shell 2 [OST] - Ambient Music [HQ]](https://www.youtube.com/watch?v=0xjJ71Vcqc0) | Taneomi | 5,760 | 153,370 | 26.6 | ×36.5 | 1,116.5 | 5.8분 | 2026-06-08 | 13. OST·사운드트랙 | 음악 | 설명 | 258/259 |
| 819 | [Stress Relief Jazz 🌙 Smooth Sax for Calm, Relaxation & Anxi…](https://www.youtube.com/watch?v=YPsVWworsbc) | JazzAyo Lounge | 37,700 | 1,002,644 | 26.6 | ×741.1 | 5,736.7 | 133.2분 | 2026-05-02 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 387/399 |
| 820 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 이게 극락 사운드인가?🪷 ∣ 속세 탈출용 불교 재즈🎧](https://www.youtube.com/watch?v=EQzDJeyYNX0) | chill potato … | 15,500 | 411,007 | 26.5 | ×59.5 | 2,484.9 | 123.1분 | 2026-05-11 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 282/282 |
| 821 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 서울숲 카페에서 하루종일 듣기좋은 팝송 𝟏𝟎시간 (중간광고없음) ☀️🌿 기분 좋아지는 카페…](https://www.youtube.com/watch?v=2eFGY53k350) | With Lofi Cafe | 5,100 | 134,834 | 26.4 | ×14.5 | 988.7 | 616.3분 | 2026-06-09 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 9/11 |
| 822 | [Arabic Deep House Mix & arabic Oud - The Last Pharaoh (Offi…](https://www.youtube.com/watch?v=zEA4nqtiy94) | Deep Tune Fan… | 20,200 | 534,052 | 26.4 | ×58.2 | 3,300.3 | 8분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 113/113 |
| 823 | [All RED EVIL JACK MUSIC【作業用/For work】](https://www.youtube.com/watch?v=hruX5UfVTYw) | イヴch🍳🥚 | 2,450 | 64,313 | 26.2 | – | 739.8 | 8.6분 | 2026-07-29 | 기타 | 음악 | 설명 | 49/49 |
| 824 | [𝐘𝐨𝐠𝐚 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 바람이 살랑 우붓의 요가 샬라ㅣ허밍 요가 음악](https://www.youtube.com/watch?v=34ESzO9DdwQ) | 김샨티(Shanti Ki… | 5,350 | 140,266 | 26.2 | ×12.6 | 1,112.2 | 61.5분 | 2026-06-20 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 45/46 |
| 825 | [Spirit Of Wolf ∣ Native Inspired Healing Music for Deep Cal…](https://www.youtube.com/watch?v=SUgiw7VzoUY) | Ancestral Ech… | 5,010 | 131,241 | 26.2 | ×155.3 | 1,085.8 | 8.1분 | 2026-06-25 | 1. 수면·명상·힐링 | 음악 | 설명 | 318/322 |
| 826 | [지렸다... 심장마비 🔥 선넘은 여성보컬 락발라드 COVER 33곡 모음 ∣ 전율돋는 초고음 소름주의보 3…](https://www.youtube.com/watch?v=tol8QOlOsPo) | 아무노래개조소 | 9,570 | 249,053 | 26.0 | ×28.4 | 1,901.4 | 133.5분 | 2026-06-15 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 143/152 |
| 827 | [[playlist] 신기하네, 이런 빈티지재즈 좋아하는 걸 어떻게 알고 틀어줬지? ∣ 중간 광고 없음 Ja…](https://www.youtube.com/watch?v=aZRegDWuCEo) | 포 시즌 플리 Four … | 41,000 | 1,063,259 | 25.9 | ×48.0 | 15,185.4 | 75.1분 | 2026-08-15 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 416/442 |
| 828 | [Naagin All Seasons - ‘The Origin of Revenge‘ MV ∣ Naagin Em…](https://www.youtube.com/watch?v=-yEf-59hqRs) | 𝐍𝐚𝐚𝐠𝐢𝐧 𝐇𝐏 𝐎𝐟𝐟… | 24,300 | 624,957 | 25.7 | – | 4,396.8 | 11.4분 | 2026-06-04 | 기타 | 한 곡 | 설명 | 163/164 |
| 829 | [Drifting Low (Ethereal Deep House) — Club Nights](https://www.youtube.com/watch?v=YtprplnFUpc) | Club Nights | 28,400 | 728,336 | 25.6 | ×25.7 | 5,888.5 | 6.4분 | 2026-06-22 | 기타 | 정보·해설 | 설명 | 47/47 |
| 830 | [Chike & Tiwa Savage - We Go Make Am Work (2026 Afro Music) …](https://www.youtube.com/watch?v=0PVF8lImHNs) | Afro Music So… | 2,600 | 65,856 | 25.3 | ×84.3 | 520.1 | 6분 | 2026-06-19 | 14. AI 음악 | AI 음악 | 설명 | 10/10 |
| 831 | [Arabic Oud & Flamenco Guitar – Gentle Instrumental Music fo…](https://www.youtube.com/watch?v=4HR2eB5p8WI) | Andalusian Ou… | 26,700 | 674,996 | 25.3 | ×182.5 | 4,394.7 | 90.8분 | 2026-05-23 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 264/267 |
| 832 | [Relaxing Country Gospel ∣ Call Upon the Name of Jesus ∣ Hea…](https://www.youtube.com/watch?v=R38UIWZtjkQ) | Breathing Pla… | 35,100 | 886,860 | 25.3 | ×250.6 | 6,748.0 | 6.4분 | 2026-06-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 863/857 |
| 833 | [Música espiritual hebrea - Melodías antiguas de Israel para…](https://www.youtube.com/watch?v=A7ZlOXV_CrU) | Sacred Hebrew… | 20,600 | 519,111 | 25.2 | ×289.7 | 3,351.2 | 63.5분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 749/789 |
| 834 | [Into the Misty Scottish Highlands｜Celtic Music for Deep Foc…](https://www.youtube.com/watch?v=7JojfPKvTM4) | Echoes of Alba | 45,400 | 1,136,705 | 25.0 | ×44.9 | 6,321.3 | 143.4분 | 2026-04-27 | 3. 공부·집중·작업 | 음악 | 설명 | 480/485 |
| 835 | [Spirit Of Eagle Native American Healing Music for Vision, F…](https://www.youtube.com/watch?v=j3OaU9N8uIU) | Ancestral Ech… | 5,010 | 124,917 | 24.9 | ×147.8 | 1,069.8 | 9.1분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 215/218 |
| 836 | [playlist ∣ 여름, 레몬과 재즈에 대하여](https://www.youtube.com/watch?v=Gr7ZxTdL8XA) | centralgrocer… | 27,800 | 688,448 | 24.8 | ×50.9 | 6,187.0 | 236.8분 | 2026-07-05 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 207/209 |
| 837 | [듣는 순간 마음이 편안해지는 첼로 음악 🎻 ∣ 공부, 휴식, 감성 힐링 음악](https://www.youtube.com/watch?v=QmJoFjq-aWE) | 따뜻한 휴식 Studio | 2,010 | 49,375 | 24.6 | ×115.2 | 323.0 | 51.4분 | 2026-05-24 | 1. 수면·명상·힐링 | 음악 | 설명 | 37/37 |
| 838 | [LOVE 💚 ∣ 639Hz Heart Chakra Healing Music ∣ Self-Love, Comp…](https://www.youtube.com/watch?v=DZYgNIUjkH4) | Sound of the … | 1,570 | 38,452 | 24.5 | ×20.1 | 650.6 | 5.4분 | 2026-08-26 | 1. 수면·명상·힐링 | 음악 | 설명 | 130/134 |
| 839 | [💿 노릇노릇 빵아저씨가 만든 브금🍞](https://www.youtube.com/watch?v=2bUpv56PbMw) | 프륀 Pruiin | 12,100 | 292,615 | 24.2 | ×20.1 | 2,168.6 | 123.7분 | 2026-06-11 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 90/92 |
| 840 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭☕ Let the Day Start Softly with Coffee and Korean C…](https://www.youtube.com/watch?v=FUrT7LN9VRU) | Seoul Flow AI | 23,800 | 571,669 | 24.0 | ×49.3 | 3,655.1 | 166.6분 | 2026-05-20 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 133/135 |
| 841 | [내 삶에 임하소서 ∣ 주기도문 기반 잔잔한 찬양, 조용한 기도 ∣ Let Your Presence Fill…](https://www.youtube.com/watch?v=HzyxKZ_w2_8) | 쉼이 되는 찬양 | 3,080 | 73,032 | 23.7 | ×14.2 | 409.4 | 5.3분 | 2026-04-28 | 15. CCM·찬양·국악… | 음악 | 설명 | 27/27 |
| 842 | [【あつ森】Lofi Night｜雨降る夜に部屋でゆっくりと過ごす☔雨音｜作業・勉強【1時間】](https://www.youtube.com/watch?v=2SV-ueN0hxA) | Tsumugi's Coz… | 24,800 | 585,283 | 23.6 | ×56.3 | 4,273.8 | 60.2분 | 2026-06-09 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 104/108 |
| 843 | [🎤 고단한 하루 끝, 막걸리 한잔하며 듣는 눈물 나는 중년 위로가 — 인생막걸리 (가수 창)🎶 인생 트롯 …](https://www.youtube.com/watch?v=4EkREEo9LXQ) | 우리인생뮤직 | 22,700 | 534,919 | 23.6 | ×193.9 | 2,977.8 | 6분 | 2026-04-27 | 9. 가요·발라드·트로트 | 음악 | 설명 | 309/311 |
| 844 | [Calm Morning Music ∣ Relaxing Flute for Anxiety Relief](https://www.youtube.com/watch?v=P1aHG6IqCtM) | Moksha Sounds… | 37,000 | 871,686 | 23.6 | ×142.0 | 4,940.0 | 40.2분 | 2026-04-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 293/296 |
| 845 | [पहाड़ों में गूंजती जादुई बाँसुरी 🎋 Magical Mountain Flute M…](https://www.youtube.com/watch?v=orUOWfIkmM4) | Vibe Without … | 26,800 | 625,618 | 23.3 | ×225.7 | 3,833.6 | 46.8분 | 2026-05-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 416/416 |
| 846 | [눈물 없이는 못 듣는 감성 락발라드 트로트 12곡｜중년 가슴을 울리는 인생 노래 모음｜55분 연속듣기](https://www.youtube.com/watch?v=0rFs08Wz1Xw) | 인생은 트로트 | 9,890 | 229,271 | 23.2 | ×16.4 | 2,762.3 | 55.5분 | 2026-08-02 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 96/96 |
| 847 | [Playlist ∣ Smooth Hip Hop Groove 😎 ∣ GROOVE · JAZZHOP ∣ Caf…](https://www.youtube.com/watch?v=ru-PF195pR0) | PoponWave | 23,500 | 535,070 | 22.8 | ×36.3 | 3,016.5 | 215.2분 | 2026-04-29 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 177/178 |
| 848 | [KWUBAKA (AMAPIANO remix) by ABASHAZANGENDO (BGM remix)](https://www.youtube.com/watch?v=3TgKlzPGh6Y) | Burundi Golde… | 17,200 | 391,436 | 22.8 | ×13.5 | 2,602.6 | 4.4분 | 2026-05-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 90/92 |
| 849 | [10-Minute Divine Flute Meditation ∣ Inner Peace & Healing ∣…](https://www.youtube.com/watch?v=_3PmWQ0lENE) | Sri Ganapathy… | 46,500 | 1,047,201 | 22.5 | ×4,265.6 | 9,549.2 | 10.6분 | 2026-07-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,480/1,493 |
| 850 | [[Playlist] 오늘은 일본 카페에 앉아 있는 기분으로](https://www.youtube.com/watch?v=fDk1BeVbz_4) | JazzBrown | 16,000 | 359,884 | 22.5 | ×63.9 | 2,477.4 | 70.5분 | 2026-06-01 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 30/31 |
| 851 | [【在喧囂中尋回本心，伴隨天籟美聲聆聽千年的清静】 靈魂淨化｜清静經 ｜Taoist Healing Music・ヒーリ…](https://www.youtube.com/watch?v=AqSDuxZWMHk) | YUCHIN'S TAOI… | 3,520 | 78,882 | 22.4 | ×16.8 | 606.5 | 4.6분 | 2026-06-16 | 1. 수면·명상·힐링 | 음악 | 설명 | 73/74 |
| 852 | [music to stay locked in](https://www.youtube.com/watch?v=eL5rWVPguoc) | Productivity … | 39,000 | 873,967 | 22.4 | ×38.3 | 11,687.4 | 115.6분 | 2026-08-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 208/210 |
| 853 | [Nine Inch Nails x Hans Zimmer - Right Where Time Belongs (D…](https://www.youtube.com/watch?v=QqyWPg0fM_E) | Dreams Of Col… | 14,300 | 318,670 | 22.3 | ×8.4 | 2,516.1 | 7분 | 2026-06-19 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,321/1,327 |
| 854 | [[중간광고없음] 🌲✨ 복잡한 마음은 잠시 내려놓자 ∣ 위로와 휴식의 피아노 ∣ BGM ∣ 휴식, 힐링, 위로](https://www.youtube.com/watch?v=ADirqRo8IyI) | Riae & Piano | 12,600 | 278,131 | 22.1 | ×18.5 | 3,690.6 | 180.9분 | 2026-08-09 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 33/38 |
| 855 | [途中広告なし[BGM]心が晴れる朝🌿Gentle Morning Piano & Guitar Music](https://www.youtube.com/watch?v=OSXpI32ZlQI) | Aurora Tune | 19,400 | 427,180 | 22.0 | ×7.0 | 3,065.2 | 123.5분 | 2026-06-06 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 50/50 |
| 856 | [👑💎 Beautiful Princesses, Magical Animals & Relaxing Piano M…](https://www.youtube.com/watch?v=LGexlV5skko) | Princesses Pa… | 7,810 | 171,664 | 22.0 | ×34.0 | 1,437.8 | 5.7분 | 2026-06-26 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 181/182 |
| 857 | [TAI CHI MUSIC – MELODIES OF THE TAO ∣ Chinese Relaxing Musi…](https://www.youtube.com/watch?v=PcSZ9tCBFQ0) | VibrArte Music | 17,100 | 375,656 | 22.0 | ×67.4 | 2,188.5 | 58.9분 | 2026-05-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 162/164 |
| 858 | [Playlist✍️ 수험생 초집중모드 공부 플레이리스트 ∣ 틀어놓는 순간 공부에 빠져드는 공부플리 BGM🎧…](https://www.youtube.com/watch?v=vuYrODP_RTE) | obne music 오브… | 7,740 | 169,784 | 21.9 | ×23.5 | 2,985.9 | 120.2분 | 2026-08-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 4/6 |
| 859 | [불(佛)빛사운드 - 물처럼, 바람처럼 M/V 4K #불교음악](https://www.youtube.com/watch?v=G7P3BWOH67s) | 불佛빛사운드 | 4,050 | 88,194 | 21.8 | ×10.6 | 592.0 | 5.8분 | 2026-05-28 | 1. 수면·명상·힐링 | AI 음악 | 설명 | 118/119 |
| 860 | [🍂하루종일 듣기 좋은 기분 좋은 클래식 명곡 ∣ 중간광고❌∣ 쇼팽, 리스트, 슈만, 바흐 ∣ 명상, 휴식,…](https://www.youtube.com/watch?v=zG6O9a_rRpY) | 퓨얼리 피아노 클래식 𝚋… | 22,800 | 490,651 | 21.5 | ×16.9 | 10,811.3 | 180.7분 | 2026-09-08 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 112/122 |
| 861 | [[60만뷰 감사합니다]가왕의 명곡을 락발라드로! 조용필 - 그 겨울의 찻집 (AI Cover / 알고보니 …](https://www.youtube.com/watch?v=_GrNoR-QyMQ) | 알고보니 혼비백산 | 43,400 | 930,641 | 21.4 | ×107.5 | 6,006.6 | 5.4분 | 2026-05-22 | 14. AI 음악 | AI 음악 | 설명 | 249/257 |
| 862 | [【洋楽Playlist】疲れた夜に聴きたい、やさしく包まれるチルR&B 🌆✨｜途中広告なし【作業用BGM】](https://www.youtube.com/watch?v=kf0crw-vh4g) | Moo'in Nights | 25,000 | 534,211 | 21.4 | ×17.5 | 3,588.6 | 66.2분 | 2026-05-28 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 35/35 |
| 863 | [고양이 카페에 놀러 올래?](https://www.youtube.com/watch?v=ifT02Y1gbuI) | 꾸양이 | 14,900 | 316,688 | 21.2 | ×15.5 | 2,109.7 | 63.6분 | 2026-05-27 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 152/154 |
| 864 | [머리가 맑아지고🌳마음이 평온해져요. 피아노와 플루트 선율 ∣ 3시간, 힐링음악, 명상음악 ∣ Relaxin…](https://www.youtube.com/watch?v=QPa9L5TDD-4) | 살구사운드 SalguSo… | 10,800 | 229,294 | 21.2 | ×16.9 | 1,858.9 | 188분 | 2026-06-22 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 129/129 |
| 865 | [[playlist] 희한하네, 살면서 이렇게 좋은 재즈는 처음 들어. 이렇게 오래 살았는데도 말이야. ∣ …](https://www.youtube.com/watch?v=cHC2M0hdKCU) | 포 시즌 플리 Four … | 41,000 | 870,460 | 21.2 | ×39.3 | 10,889.5 | 65분 | 2026-08-05 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 299/308 |
| 866 | [Bombay BGM ∣ 80-Piece Orchestra](https://www.youtube.com/watch?v=ssC6VM6GQ-4) | Australian In… | 32,600 | 688,961 | 21.1 | – | 4,308.1 | 13.3분 | 2026-05-17 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 234/240 |
| 867 | [Lingashtakam Shiva Meditation Music ∣ Powerful Healing Mant…](https://www.youtube.com/watch?v=TehHNpaUk0s) | Satya Devotio… | 3,390 | 71,009 | 20.9 | ×1.9 | 513.3 | 5.7분 | 2026-06-07 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 30/30 |
| 868 | [Enya - I know Your Pain (2026 Official Music Video)](https://www.youtube.com/watch?v=1AZagg8LCDw) | Celestine Echo | 14,700 | 305,632 | 20.8 | ×58.6 | 2,787.7 | 6.3분 | 2026-07-06 | 기타 | 한 곡 | 설명 | 97/97 |
| 869 | [[찬송가 모음]주님 앞에 펑펑 울고 싶을 때 듣는 찬양ㅣ눈물의 찬송가 10곡ㅣ깊은 울림 바리톤 찬양ㅣHYM…](https://www.youtube.com/watch?v=giFgcjlR4Co) | 골방 찬양 | 26,500 | 550,549 | 20.8 | ×5.3 | 3,410.1 | 81.4분 | 2026-05-15 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 1,318/1,329 |
| 870 | [싱그러운 아침, 고요한 클래식 선율 속에서 마음의 평화를 느껴보세요. Healing Classics와 함께…](https://www.youtube.com/watch?v=gtHsO8taxgo) | 클래식힐링 | 14,600 | 302,240 | 20.7 | ×48.9 | 1,810.7 | 125.2분 | 2026-05-10 | 1. 수면·명상·힐링 | 음악 | 설명 | 127/127 |
| 871 | [🍃Xanh Playlist 2🍃TAN LÀM, BẬT NHẠC∣ Nhạc R&B Lofi Chill Yêu…](https://www.youtube.com/watch?v=lkotmZNWq5I) | Xanh | 46,200 | 953,048 | 20.6 | ×18.5 | 16,736.1 | 50.4분 | 2026-08-28 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 217/227 |
| 872 | [#Zumba Work out 💪🏽..Full energy...Best music for Work out..](https://www.youtube.com/watch?v=cuzHvFb2It0) | Zumbique | 1,210 | 24,938 | 20.6 | ×9.0 | 217.5 | 7.8분 | 2026-07-01 | 기타 | 음악 | 설명 | 4/4 |
| 873 | [가슴을 울리는 감성 트로트 5곡 모음 ∣ 깊은 밤 듣기 좋은 노래](https://www.youtube.com/watch?v=o_RE1dPuUoo) | 트로트 작은 음악실 | 23,600 | 486,457 | 20.6 | ×81.1 | 3,059.3 | 24.4분 | 2026-05-18 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 209/214 |
| 874 | [Whispers of the Ancient Forest｜Mystical Celtic Music for De…](https://www.youtube.com/watch?v=DQ_KPUXyY7o) | Echoes of Alba | 45,400 | 925,183 | 20.4 | ×36.5 | 5,975.8 | 140.2분 | 2026-05-22 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 129/135 |
| 875 | [Habias X Filho Do Zua - Se a Vida Decide Me Levar](https://www.youtube.com/watch?v=SnGHZcvK2TA) | Habias | 31,400 | 639,756 | 20.4 | ×35.0 | 7,565.9 | 4.2분 | 2026-07-31 | 기타 | 음악 | 설명 | 245/247 |
| 876 | [🎹 Corazón Silente ∣ Piano para Calmar la Mente](https://www.youtube.com/watch?v=3jUY4NFO9sg) | El Piano de E… | 14,200 | 288,924 | 20.4 | ×356.5 | 3,251.4 | 4.1분 | 2026-07-27 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 25/25 |
| 877 | [Chinese Sleep Music: Soft Biwa & Ambient Layers ∣ Restful N…](https://www.youtube.com/watch?v=wInynTSVhOk) | Lotus Echo 莲之… | 17,200 | 345,638 | 20.1 | ×87.8 | 2,235.5 | 241.1분 | 2026-05-22 | 1. 수면·명상·힐링 | 음악 | 설명 | 75/77 |
| 878 | [10 Most Beautiful Melodies Ever Written for Piano](https://www.youtube.com/watch?v=vmbG0x1jq_s) | Lisztopher | 10,200 | 202,858 | 19.9 | ×33.1 | 1,326.7 | 15.9분 | 2026-05-24 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 269/269 |
| 879 | [고고프렌즈 “국어별동대” 피아노커버](https://www.youtube.com/watch?v=IkZ1vxE2GeQ) | MUJINS 뮤진스 | 19,300 | 381,752 | 19.8 | ×66.8 | 3,818.4 | 7.5분 | 2026-07-16 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 521/527 |
| 880 | [【作業用BGM】流すだけで前向きになれる洋楽 House Pop Mix｜リラックス・集中・気分転換](https://www.youtube.com/watch?v=Kk1n4AZQyws) | Lucky Clover … | 39,800 | 781,860 | 19.6 | ×99.2 | 5,511.4 | 105.5분 | 2026-06-04 | 기타 | 음악 | 설명 | 66/66 |
| 881 | [🍉 냉장고를 열었더니 수박만 있는 브금](https://www.youtube.com/watch?v=h6oskIb0ASU) | 프륀 Pruiin | 12,100 | 237,550 | 19.6 | ×16.6 | 2,330.4 | 146.4분 | 2026-07-14 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 100/100 |
| 882 | [Walking Past an Old Library in Autumn Boston 🍂 Warm Jazz, F…](https://www.youtube.com/watch?v=0KCrdROdw4g) | Dreams Jazz M… | 48,200 | 934,740 | 19.4 | ×28.8 | 24,026.8 | 209분 | 2026-09-15 | 7. 재즈·보사노바 | 음악 | 설명 | 72/75 |
| 883 | [(Free For Profit) Melodic Type Beat - "ANGEL"](https://www.youtube.com/watch?v=LgS91RB_BDk) | Nocturnn | 36,000 | 697,219 | 19.4 | ×20.4 | 5,496.8 | 4분 | 2026-06-19 | 6. 피아노·클래식·연주곡 | 정보·해설 | 설명 | 229/232 |
| 884 | [Healing Music for Anxiety, Fears and Depression 🌿 Heals the…](https://www.youtube.com/watch?v=RUowd-_b72Y) | Nature Aura | 3,940 | 74,515 | 18.9 | ×60.8 | 677.8 | 104.8분 | 2026-07-06 | 1. 수면·명상·힐링 | 음악 | 설명 | 51/51 |
| 885 | [Sleep Instantly with Soft Piano and Rain 🌧️ Relaxing Music …](https://www.youtube.com/watch?v=PclKQrQuR7U) | Relaxing Piano | 37,500 | 707,007 | 18.9 | ×126.3 | 8,593.8 | 181.6분 | 2026-08-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 79/79 |
| 886 | [𝓅𝓁𝒶𝓎𝓁𝒾𝓈𝓉 𖤐₊˚ 앙큼 미소녀 브금 │ 공부·작업·집중 BGM ✦](https://www.youtube.com/watch?v=8rE90EGyCbY) | 오늘은 무슨 컨셉? | 3,010 | 56,044 | 18.6 | ×15.8 | 392.0 | 29.2분 | 2026-06-03 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 39/39 |
| 887 | [It's TV Time! – Deltarune Piano Collections, Vol. 2 (Offici…](https://www.youtube.com/watch?v=44Dh4Vb8Wtk) | Trevor Alan G… | 19,300 | 357,100 | 18.5 | – | 15,976.4 | 5.6분 | 2026-10-01 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 993/998 |
| 888 | [7080 카페음악 베스트🌺50대이상이 들으면 기분좋아지는 7080노래모음 ∣ 베스트 7080노래모음 ∣ 광…](https://www.youtube.com/watch?v=IZmsMTzrWDY) | Korean Cafe M… | 3,280 | 60,489 | 18.4 | ×1,099.8 | 640.5 | 10.3분 | 2026-07-21 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 3/3 |
| 889 | [트로트 모음 50곡 #트로트 메들리 #인기트로트 🎶 하루 종일 듣기 좋은 노래 모음 🎶 추억의 트로트 명곡…](https://www.youtube.com/watch?v=5GO9R1-U5OM) | SonicVista | 26,900 | 494,255 | 18.4 | ×2,959.6 | 3,732.9 | 78.9분 | 2026-06-13 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 77/79 |
| 890 | [90년대 00년대 락발라드 명곡 모음 ∣ 샤우팅 넘치며 감동적인 락발라드 40곡 연속듣기 ∣ 엠씨더맥스, …](https://www.youtube.com/watch?v=5c_EJyjOdWQ) | 발라드 홈 / BALLA… | 10,300 | 189,213 | 18.4 | ×19.9 | 1,670.9 | 154.9분 | 2026-07-03 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 23/23 |
| 891 | [네가 내게 알려줬어💕｜『 四季の笑顔 (사계절 미소)』｜가사해석/Lyrics](https://www.youtube.com/watch?v=T7gBckYYJug) | Nonohara | 1,290 | 23,673 | 18.4 | ×10.9 | 448.2 | 4.9분 | 2026-09-01 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 22/23 |
| 892 | [(No Ads)Rain Ambience and Calm Piano Music – Peaceful Sleep…](https://www.youtube.com/watch?v=oa4PEL3kHLo) | Relaxing Piano | 37,500 | 686,882 | 18.3 | ×122.7 | 7,286.0 | 183.7분 | 2026-07-22 | 2. 자연 소리·백색소음 | 음악 | 설명 | 228/228 |
| 893 | [Morning Energy Music ∣ Dilruba Raga Yaman ∣ 1.5 Hours](https://www.youtube.com/watch?v=DMcoOLvmAyQ) | Raga Focus | 37,700 | 684,182 | 18.1 | ×501.2 | 4,066.8 | 90분 | 2026-05-09 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 166/167 |
| 894 | [밤바다 보이는 카페 창가, 조용히 듣기 좋은 7080 라디오 감성 올드팝](https://www.youtube.com/watch?v=9x53vG82_Ao) | morgellia(모르겔… | 18,200 | 324,667 | 17.8 | ×39.4 | 2,159.2 | 159.8분 | 2026-05-26 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 151/151 |
| 895 | [가슴 뭉클한 옛날 노래 🍂 백마강·해운대 엘레지·동숙의 노래｜중년·어르신을 위한 추억의 트로트 50곡 🍁 …](https://www.youtube.com/watch?v=F9mzexxZOVo) | 추억의 K트롯 | 15,000 | 266,166 | 17.7 | ×73.1 | 3,043.8 | 137.7분 | 2026-07-28 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 104/107 |
| 896 | [Soft Telugu Songs for your SOUL ♡](https://www.youtube.com/watch?v=17nDtmG2PRU) | With Love Ash… | 36,500 | 646,553 | 17.7 | – | 4,587.2 | 9.8분 | 2026-06-05 | 기타 | 플레이리스트·모음 | 설명 | 23/23 |
| 897 | [Chopin for Autumn Nights — Peaceful Piano for Relaxation (4…](https://www.youtube.com/watch?v=AkZrzHCfivc) | Rain Whisper … | 42,800 | 754,198 | 17.6 | ×27.6 | 15,451.3 | 78.5분 | 2026-09-05 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 143/147 |
| 898 | [Lofi Summer Vibes 🌊 Seaside Coffee & Relaxing Lofi for a Se…](https://www.youtube.com/watch?v=ovS27OGTajs) | Little Lofi C… | 26,000 | 456,713 | 17.6 | ×56.8 | 2,581.7 | 205.8분 | 2026-04-30 | 11. 힙합·R&B·EDM | 음악 | 설명 | 112/112 |
| 899 | [Deep Sleep Music ∣ 528hz Whole Body Healing Frequency, Mela…](https://www.youtube.com/watch?v=9tczYViDUak) | Healing Sleep… | 29,400 | 512,116 | 17.4 | ×110.8 | 4,405.8 | 698.1분 | 2026-06-30 | 1. 수면·명상·힐링 | 음악 | 설명 | 283/283 |
| 900 | [TAO — 道 ∣ Japanese Zen Music for Deep Meditation & Inner Ca…](https://www.youtube.com/watch?v=SepvquaFWAY) | Hikari Zen | 27,300 | 474,372 | 17.4 | ×102.9 | 2,792.7 | 237.6분 | 2026-05-07 | 1. 수면·명상·힐링 | 음악 | 설명 | 107/108 |
| 901 | [Mind Relaxing Music – Peaceful Flute Meditation Music, Esca…](https://www.youtube.com/watch?v=bx_QXhMb5xM) | CLASSICAL FUS… | 19,200 | 331,581 | 17.3 | ×84.0 | 2,297.2 | 40.1분 | 2026-06-01 | 1. 수면·명상·힐링 | 음악 | 설명 | 76/77 |
| 902 | [NGWIZA (BGM Remix) Ballet Royal du Burundi](https://www.youtube.com/watch?v=ho_IGrAkUSs) | Burundi Golde… | 17,200 | 295,817 | 17.2 | ×10.2 | 1,783.4 | 4.2분 | 2026-05-11 | 기타 | 음악 | 설명 | 206/206 |
| 903 | [🌿🍁 미사리에서 듣는 최고의 가을 카페음악｜2026 가을 감성 플레이리스트 ☕ 마음이 편안해지는 음악](https://www.youtube.com/watch?v=sDs-SBQlNCw) | Cozy Cafe Mus… | 3,870 | 66,514 | 17.2 | ×32.3 | 1,532.4 | 62.6분 | 2026-09-10 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 0/13 |
| 904 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 올해 내내 듣게 될 시원한 청량팝 모음🐶🩵 첫 곡부터 기분 좋아지는 여름 플리👙 카페음…](https://www.youtube.com/watch?v=DwlYkGuixsw) | OOOffi | 25,900 | 444,062 | 17.1 | ×16.2 | 2,992.3 | 657.9분 | 2026-05-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 59/59 |
| 905 | [샹송이 이렇게 까지 좋은줄 몰랐습니다 ∣ 너무 좋아서 아침부터 듣게 되는 7080 올드팝 ∣ 감성이 터진](https://www.youtube.com/watch?v=KFu4Y2j652w) | Midnight Melo… | 28,300 | 484,589 | 17.1 | ×140.8 | 2,786.8 | 119.9분 | 2026-05-03 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 157/157 |
| 906 | [Morning Anxiety Calms ∣ Prana Vihara — Bansuri 432Hz for Cl…](https://www.youtube.com/watch?v=Ae8IzAhMcYY) | Shunya SoundS… | 20,400 | 349,111 | 17.1 | ×359.7 | 1,968.6 | 34.2분 | 2026-04-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 189/190 |
| 907 | [The Little Forest Concert Vol.3 🌿 ∣ Warm BGM for Reading, S…](https://www.youtube.com/watch?v=_zmbIUADeMw) | 그루잠 Gurujam | 28,600 | 483,887 | 16.9 | ×95.8 | 6,877.1 | 32.6분 | 2026-08-14 | 3. 공부·집중·작업 | 음악 | 설명 | 71/72 |
| 908 | [【あつ森BGM】夜のリラックスタイム🌙 心落ち着くLo-fi Chill Hop & ASMR｜作業・勉強・睡眠用](https://www.youtube.com/watch?v=YgEA5Ow6mk4) | Chill Mori BGM | 29,300 | 494,087 | 16.9 | ×5.7 | 2,808.9 | 180.1분 | 2026-05-01 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 51/51 |
| 909 | [Instrumental Christian Piano for Focus ∣ 2 Hours Worship Pi…](https://www.youtube.com/watch?v=q7ooKtFTYMk) | In His Presen… | 17,400 | 292,068 | 16.8 | ×26.9 | 1,975.3 | 121.4분 | 2026-05-29 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 16/17 |
| 910 | [[눈물주의]세상에서 가장 슬픈 노래 😢 어미의 한 [판소리]💔The Saddest Song Ever Wri…](https://www.youtube.com/watch?v=DhredFI94dc) | Nana Music | 10,200 | 170,798 | 16.7 | ×217.0 | 1,857.2 | 6분 | 2026-07-24 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 99/105 |
| 911 | [[𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 정병 제대로 터져버린 멘헤라남 플리](https://www.youtube.com/watch?v=N2zEbM5dIH4) | 안평화 | 17,300 | 285,671 | 16.5 | ×10.1 | 5,862.7 | 15.6분 | 2026-09-05 | 기타 | 플레이리스트·모음 | 없음 | 168/176 |
| 912 | [딸에게 한 번도 하지 못했던 말... 오늘 이 노래로 전합니다 / 내딸아 / 도연스님 / 만복감성트롯 / …](https://www.youtube.com/watch?v=k5oAx-igPIU) | 만복 낭만트롯 | 2,510 | 41,313 | 16.5 | ×15.9 | 491.7 | 5분 | 2026-08-01 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 30/30 |
| 913 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ∣ 가을은 이런 노래 들으려고 있는 거잖아🍃 🚲아침부터 설레는 느좋 팝송.zip🎧 카페음악…](https://www.youtube.com/watch?v=h03aGRBo6m8) | OOOffi | 25,900 | 425,486 | 16.4 | ×16.0 | 5,958.9 | 631.4분 | 2026-08-13 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 42/49 |
| 914 | [Deep meditation ∣ use headphones for better results ∣ mindf…](https://www.youtube.com/watch?v=HR4UkS5H-kk) | Modern Yogii | 711 | 11,651 | 16.4 | – | 69.5 | 15.2분 | 2026-05-09 | 1. 수면·명상·힐링 | 음악 | 설명 | 7/7 |
| 915 | [[연속듣기] 눈물 나게 가슴 뭉클한 옛날 노래 45곡 🎵 세월이 흘러도 잊을 수 없는 추억의 트로트 🎵 흘…](https://www.youtube.com/watch?v=xj8SEIUhbjY) | 추억의 K트롯 | 15,000 | 244,670 | 16.3 | ×67.2 | 1,659.4 | 132.4분 | 2026-05-29 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 78/79 |
| 916 | [Rumi Sufi Healing Music for Anxiety Relief & Inner Peace ∣ …](https://www.youtube.com/watch?v=Whuol6tvJ5w) | Whispering Sp… | 4,360 | 70,338 | 16.1 | ×19.9 | 1,438.3 | 88.1분 | 2026-09-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 5/6 |
| 917 | [🍉여름에 듣기 좋은 카페 음악 ☕ 상쾌한 여름 바닷가 처럼 기분좋은 Playlist ∣ 중간 광고 없음 ∣…](https://www.youtube.com/watch?v=ZSVnVZ0-ROg) | 오늘의 멜로디 Today… | 19,800 | 318,748 | 16.1 | ×70.3 | 1,951.2 | 120.4분 | 2026-05-13 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 57/57 |
| 918 | [너에플리 리메이크 모음｜CHAPTER 1](https://www.youtube.com/watch?v=iSJD2jZwB8E) | 너에플리 | 28,800 | 461,542 | 16.0 | – | 3,145.3 | 34분 | 2026-05-30 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 184/185 |
| 919 | [[평안 찬송] 마음에 평안과 기쁨을 채워주는 은혜의 찬송가 모음 ∣ 들을수록 마음이 편안해지는 찬송가 연속…](https://www.youtube.com/watch?v=GaBxDi7Eg3M) | 주님곁에 | 19,100 | 305,866 | 16.0 | ×6.9 | 3,897.0 | 71.2분 | 2026-08-06 | 15. CCM·찬양·국악… | 커버·직접 부른 노래 | 설명 | 277/287 |
| 920 | [[찬송가 연속듣기] 마음이 복잡할 때 듣는 잔잔한 찬송가 20곡 ∣ 잠들기 전 평안을 주는 찬양 메들리 (…](https://www.youtube.com/watch?v=Tt9qwuoMPtI) | 골방 찬양 | 26,500 | 423,007 | 16.0 | ×4.1 | 2,686.9 | 246.6분 | 2026-05-19 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 622/639 |
| 921 | [국악딴따라 노래모음｜30곡 연속듣기](https://www.youtube.com/watch?v=VctWdCriD_k) | 국악딴따라 | 36,000 | 573,886 | 15.9 | ×11.7 | 10,662.9 | 91.7분 | 2026-08-31 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 344/382 |
| 922 | [가장 편안하고 깊은 잠에 빠지게 만드는 부드러운 빗소리 ASMR ∣ 수면유도 백색소음](https://www.youtube.com/watch?v=qOwxf0IAk_E) | Cozy Rainy Da… | 9,730 | 154,447 | 15.9 | ×19.1 | 1,595.2 | 360분 | 2026-07-19 | 1. 수면·명상·힐링 | 자연 소리·백색소음 | 설명 | 27/31 |
| 923 | [ボサノバ カフェ 朝カフェ｜気分が晴れる心地よい女性ボーカル リラックス音楽 海の見えるカフェ（作業用BGM・波音）（…](https://www.youtube.com/watch?v=UJ00ifFN3jQ) | Relax Lofi Li… | 33,400 | 527,041 | 15.8 | ×60.5 | 3,285.7 | 180.3분 | 2026-05-16 | 3. 공부·집중·작업 | 음악 | 설명 | 53/53 |
| 924 | [[외모지상주의 BGM] Jekyll & Unconscious 3 ∣ Lookism BGM](https://www.youtube.com/watch?v=7FcjatxdDXo) | 루트레이블 (ROUTEL… | 13,300 | 208,776 | 15.7 | ×7.3 | 1,340.6 | 5.7분 | 2026-05-21 | 기타 | 음악 | 설명 | 126/126 |
| 925 | [🎵그냥 틀어놨는데 눈물이 났네요...주님은 다 아시죠ㅣ은혜로운 찬양모음 ㅣCCM플레이리스트 ㅣ위로CCM ㅣ…](https://www.youtube.com/watch?v=aY-zdL2QUBk) | 평화로운음악 찬양카페 | 13,100 | 205,239 | 15.7 | ×18.9 | 1,176.7 | 36.8분 | 2026-05-02 | 15. CCM·찬양·국악… | 플레이리스트·모음 | 설명 | 257/258 |
| 926 | [African Healing Music ∣ Zulu Voices for Anxiety Relief & Em…](https://www.youtube.com/watch?v=Nt0so0uLUoI) | africavoices | 4,770 | 74,349 | 15.6 | ×42.8 | 1,241.1 | 92.4분 | 2026-08-25 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 22/23 |
| 927 | [[PLAYLIST] 비 오는 날 계속 듣게 되는 발라드 7곡 ☔ ∣ 감성발라드 · 사랑노래 · 여름 플레이…](https://www.youtube.com/watch?v=fG0GudU56S0) | 뮤직앤라이트 Music&… | 8,800 | 135,663 | 15.4 | ×18.0 | 1,228.6 | 27.9분 | 2026-07-05 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 112/112 |
| 928 | [[외모지상주의 BGM] Unconscious 3 ∣ Lookism BGM](https://www.youtube.com/watch?v=BIE83KOrsgk) | 루트레이블 (ROUTEL… | 13,300 | 203,755 | 15.3 | ×7.1 | 1,369.9 | 5분 | 2026-05-28 | 기타 | 음악 | 설명 | 211/214 |
| 929 | [[Playlist] 마음이 편안해지는 힐링 피아노 ∣ Healing Piano Music for Stres…](https://www.youtube.com/watch?v=o0F2bvcNLMc) | Piano Haven | 5,200 | 79,669 | 15.3 | ×18.2 | 444.2 | 194.8분 | 2026-04-27 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 16/16 |
| 930 | [지금 꼭 들으세요 🙏 아들 일이 잘 풀립니다 ∣ 경주 불국사의 기도 음악 #불교음악 #자녀기도노래](https://www.youtube.com/watch?v=QmfOTgF-Akw) | 연등 아래서 | 11,400 | 173,869 | 15.2 | ×34.8 | 1,020.1 | 35.6분 | 2026-05-06 | 기타 | 음악 | 설명 | 4,056/4,095 |
| 931 | [[커버송 모음 50곡] (중간 광고 없어요^^:) /그 시절 추억의 노래 50곡/ 구독자 선정곡 1위~50…](https://www.youtube.com/watch?v=av1_naa9D2o) | 음악과 여행 | 26,500 | 403,869 | 15.2 | ×426.9 | 4,797.4 | 214.9분 | 2026-08-01 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 238/264 |
| 932 | [매일 듣기 좋은 편안한 클래식🌿∣행복한 힐링 클래식 음악☕∣클래식 명곡 18곡 모음🎵](https://www.youtube.com/watch?v=DTVWGGI7nKE) | 클래식라이프Classic | 23,700 | 360,993 | 15.2 | ×51.1 | 2,650.5 | 68분 | 2026-06-10 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 99/101 |
| 933 | [Chinese Zen Music🎵: Bamboo flute, erhu & Guzheng ∣ Relaxing…](https://www.youtube.com/watch?v=NthOaamO8AI) | ZenFlute | 33,600 | 510,395 | 15.2 | ×73.8 | 3,991.8 | 89.8분 | 2026-06-18 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 244/251 |
| 934 | [Easy Listening Music for Relaxation, Study, Work & Stress R…](https://www.youtube.com/watch?v=W-QDYTQch9c) | Luxenza Music | 4,610 | 69,306 | 15.0 | – | 569.1 | 18.6분 | 2026-06-24 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 2/2 |
| 935 | [BGMで巡る東京ディズニーランド&ディズニーシー 【総集編 2 】](https://www.youtube.com/watch?v=PQH90HnjyO4) | ネンサウンド | 37,600 | 558,867 | 14.9 | ×4.0 | 3,148.2 | 240.1분 | 2026-04-29 | 기타 | 정보·해설 | 설명 | 52/52 |
| 936 | [💎 "신이내린 목소리네요..." 100년에 한번 있을까 말까 한 희귀한 음색 ㄷㄷ;; 귀한 노래만 엄선 ∣…](https://www.youtube.com/watch?v=5vdkZXq8IVY) | 7080사랑해요 | 33,500 | 489,379 | 14.6 | ×78.5 | 3,252.6 | 68.1분 | 2026-05-26 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 358/358 |
| 937 | [기분전환 200%🔥 도파민 터지는, 신나는 노래들🎧 ∣ EDM ∣ Playlist ∣ 클럽음악 ∣ 노동요 …](https://www.youtube.com/watch?v=Tr5-cBvP22g) | DJ Corgi | 13,300 | 194,075 | 14.6 | ×21.8 | 1,299.0 | 150.8분 | 2026-05-27 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 31/31 |
| 938 | [Cafe Reggae 🌴 Chill Island Vibes ∣ Relaxing Reggae Music fo…](https://www.youtube.com/watch?v=407QqF8EBko) | AI IRIE FM | 41,400 | 593,480 | 14.3 | ×29.5 | 3,454.4 | 61분 | 2026-05-05 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 129/130 |
| 939 | [여름 바닷가 테라스카페 커피한잔 너무좋다 ∣Vol.177∣ 7080 라디오 l 올드팝송 명곡 ∣ Coffe…](https://www.youtube.com/watch?v=NczlNLq6beY) | moka melody | 14,900 | 213,130 | 14.3 | ×11.2 | 1,551.4 | 661.1분 | 2026-06-08 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 77/77 |
| 940 | [눕자마자 바로 기절 숙면 빗소리, [중간광고없음]10분후 검은화면, "머리 대자마자 5분 만에 기절했어요"…](https://www.youtube.com/watch?v=MGtgljKRiaI) | 빗소리 자장가 Rain … | 22,600 | 319,769 | 14.2 | ×23.9 | 2,305.5 | 420분 | 2026-06-07 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 54/54 |
| 941 | [Garbh Sanskar Deep Sleep Music 🌙 शांत संगीत ∣ Pregnancy Rel…](https://www.youtube.com/watch?v=r-WZM4San-c) | Swarmaa | 16,200 | 228,529 | 14.1 | ×529.0 | 1,595.2 | 5.5분 | 2026-06-03 | 1. 수면·명상·힐링 | 음악 | 설명 | 39/39 |
| 942 | [[Playlist]공간의 분위기 채우는☕️[중간광고없음]카페 매장 음악 🎧그냥 틀어두세요, 차 마실 때, …](https://www.youtube.com/watch?v=kqvHu52KHmQ) | BGMBUCKS | 20,300 | 281,019 | 13.8 | – | 1,690.5 | 69.3분 | 2026-05-11 | 4. 카페·매장·라운지 | 연주 | 설명 | 82/82 |
| 943 | [💃🏼노동요 들으면서 파라파라나 춰야겠다ㅣK-POP PLAYLISTㅣRESCENE, AESPA, CORTIS…](https://www.youtube.com/watch?v=uAE7TcPSJn0) | Tezz Boyz 서테즈… | 38,900 | 538,127 | 13.8 | ×62.1 | 4,513.1 | 76.1분 | 2026-06-27 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 23/23 |
| 944 | [Relaxing Healing Music for Stress, Anxiety, and Depression …](https://www.youtube.com/watch?v=Pxc3SMtKGPo) | Clara Monica … | 3,590 | 49,425 | 13.8 | ×1.6 | 954.5 | 25.3분 | 2026-09-02 | 1. 수면·명상·힐링 | 음악 | 설명 | 18/18 |
| 945 | [매일듣는 편안한 클래식 음악🎵∣🌿힐링 클래식 명곡 모음 #클래식 #클래식 음악 #편안한 클래식](https://www.youtube.com/watch?v=ek_Tc24cziw) | 클래식라이프Classic | 23,700 | 326,335 | 13.8 | ×46.2 | 1,873.6 | 55.6분 | 2026-05-03 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 64/65 |
| 946 | [⠀](https://www.youtube.com/watch?v=mDkyPzypfuo) | islistening | 32,500 | 443,715 | 13.7 | ×7.6 | 3,520.0 | 21.9분 | 2026-06-20 | 기타 | 플레이리스트·모음 | 설명 | 125/127 |
| 947 | [주부들의 휴식 시간을 채워줄 팝송 Best 100 ∣ EverPop 명곡팝 컬렉션 ∣ 올드팝송 ∣ 7080…](https://www.youtube.com/watch?v=D4H7ItMDIGU) | 추억의 올드팝 EverP… | 16,200 | 220,480 | 13.6 | ×10.4 | 1,642.0 | 117.5분 | 2026-06-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 57/57 |
| 948 | [[Masterpiece Series] Albinoni Adagio – 4 Variations Songs o…](https://www.youtube.com/watch?v=OFfc765eTgY) | WilliamPoetic… | 41,100 | 547,479 | 13.3 | ×45.4 | 3,061.6 | 17.4분 | 2026-04-28 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 781/783 |
| 949 | [【Nhất Định Phải Nghe Dành Cho Người Mất Ngủ!】Nhạc Piano Nhẹ…](https://www.youtube.com/watch?v=1-OgDgY_peU) | Nhạc Ngủ Thư … | 48,900 | 650,742 | 13.3 | ×20.1 | 4,938.1 | 182.7분 | 2026-06-14 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 184/186 |
| 950 | [새벽에 듣기좋은 메이플 로파이 재즈 ∣ 1시간 작업·공부 음악](https://www.youtube.com/watch?v=N5AE0jDAY2o) | DOKANG | 20,700 | 275,028 | 13.3 | ×24.3 | 1,688.3 | 63.9분 | 2026-05-14 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 155/157 |
| 951 | [“프린세스 티니핑송“ 피아노 커버(Princess Teenieping Song Piano Cover)](https://www.youtube.com/watch?v=BS-GSU9dLqk) | MUJINS 뮤진스 | 19,300 | 255,466 | 13.2 | ×36.9 | 1,812.1 | 6.9분 | 2026-06-05 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 49/50 |
| 952 | [아침까지 기절 숙면 잠 잘 오는 빗소리, [중간광고없음]10분후 검은화면, "눈 뜨니 개운한 아침이에요" …](https://www.youtube.com/watch?v=pkUgoZ7h_2M) | 빗소리 자장가 Rain … | 22,600 | 294,241 | 13.0 | ×22.0 | 1,808.5 | 420분 | 2026-05-14 | 2. 자연 소리·백색소음 | 자연 소리·백색소음 | 설명 | 40/41 |
| 953 | [🌈Album Preview ∣ Find the Full Album in the Playlist ∣ Cele…](https://www.youtube.com/watch?v=2qh-NuD0YMs) | Calm Music & … | 3,470 | 45,134 | 13.0 | ×412.2 | 1,275.6 | 4.8분 | 2026-09-18 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 1/1 |
| 954 | [[커버(cover)송] 카페 - "여인" 원곡 : 솔개트리오 / 밤에 들으면 더 좋은 노래 ∣ 가요 ∣ k…](https://www.youtube.com/watch?v=zmb2j7REliY) | 음악과 여행 | 26,500 | 334,211 | 12.6 | ×353.3 | 2,490.7 | 5분 | 2026-06-12 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 25/25 |
| 955 | [Faith: You Were Never Walking Alone ∣ Heavenly Meditation M…](https://www.youtube.com/watch?v=_psuP3ukwOY) | Healing Ether | 47,200 | 583,251 | 12.4 | ×67.4 | 3,510.3 | 71.2분 | 2026-05-11 | 1. 수면·명상·힐링 | 음악 | 설명 | 376/391 |
| 956 | [Mama Said ∣ Ogryn Chain Gang Blues Work Song ∣ Warhammer 40…](https://www.youtube.com/watch?v=H6yrpYWMyRs) | Solar Void | 20,800 | 246,905 | 11.9 | ×26.8 | 1,427.9 | 6분 | 2026-05-04 | 2. 자연 소리·백색소음 | 음악 | 설명 | 395/395 |
| 957 | [Awit ng Paghahangad by Bukas Palad Music Ministry ∣ Senti P…](https://www.youtube.com/watch?v=5yDRTUMvk3I) | Clyde Pianist… | 12,200 | 144,719 | 11.9 | ×27.2 | 1,232.4 | 7.2분 | 2026-06-28 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 102/108 |
| 958 | [Kiven Mukhre Ton Nazraan ∣ Ustad Nusrat Fateh Ali Khan ∣ Da…](https://www.youtube.com/watch?v=PMqkvHE1cm0) | XAN | 25,100 | 297,641 | 11.9 | ×30.2 | 1,961.7 | 4.9분 | 2026-05-25 | 12. 커버·노래 부르기 | AI 음악 | 설명 | 158/158 |
| 959 | [숲에서 쉬는 효과🌳머리가 맑아지는 치유명상음악 ∣ 3시간, 힐링음악, 명상음악 ∣ Relaxing Musi…](https://www.youtube.com/watch?v=yq-lSVEu7U0) | 살구사운드 SalguSo… | 10,800 | 127,389 | 11.8 | ×9.4 | 3,937.6 | 191.9분 | 2026-09-21 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 43/47 |
| 960 | [정서안정과 고운 마음을 위한 잔잔하고 아름다운 음악 l 어린이집 유치원 교실 편안한 배경 음악](https://www.youtube.com/watch?v=ONTpCdvC9mo) | 조이멜로디 JOY MEL… | 22,000 | 255,192 | 11.6 | ×25.1 | 1,488.8 | 82.3분 | 2026-05-05 | 기타 | 음악 | 설명 | 0/0 |
| 961 | [가을이 오면... 커피향이 가득한 카페에서 듣고 싶은 음악](https://www.youtube.com/watch?v=4lPZuU2kCbA) | EverOldies | 48,600 | 563,287 | 11.6 | ×61.7 | 11,172.5 | 96.9분 | 2026-09-03 | 4. 카페·매장·라운지 | 음악 | 설명 | 292/330 |
| 962 | [「영화 〈애수〉, 다시 노래가 되다｜세월이 지나도 남는 영화](https://www.youtube.com/watch?v=cIBIrAEYVZM) | 절로 가는 이야기 | 2,560 | 29,604 | 11.6 | ×10.6 | 1,624.6 | 4.6분 | 2026-10-06 | 기타 | 음악 | 설명 | 43/43 |
| 963 | [싱그러운 여름 아침, 꽃향기가 스며드는 기분좋은 카페음악 ∣ 계속 듣게 되는 감성팝송 ∣ Old Pop P…](https://www.youtube.com/watch?v=EnD2m1z3fkM) | 선율향기 | 11,500 | 132,588 | 11.5 | ×33.9 | 993.9 | 91.5분 | 2026-06-12 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 72/72 |
| 964 | [[𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁] 인스타에서 한번쯤 들어본 느@좋 플리](https://www.youtube.com/watch?v=4qcGtkqrfMk) | 프리다앤 / FRIDA-… | 41,500 | 476,888 | 11.5 | ×50.0 | 2,757.4 | 60.8분 | 2026-05-04 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 19/19 |
| 965 | [The Odyssey - Odysseus (EPIC Piano Cover)](https://www.youtube.com/watch?v=jtUq7gMr-7k) | Laurie Théber… | 46,100 | 529,808 | 11.5 | ×39.8 | 5,474.4 | 6.3분 | 2026-07-19 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 192/192 |
| 966 | [한 줌 흙으로 돌아가는 길 ∣ 황혼길의 깨달음 국악 판소리트로트](https://www.youtube.com/watch?v=Vb3VooJUgyk) | Nana Music | 10,200 | 116,513 | 11.4 | ×148.0 | 941.3 | 7.6분 | 2026-06-22 | 9. 가요·발라드·트로트 | 음악 | 설명 | 106/110 |
| 967 | [🔥한 번 들으면 멈출 수 없는 역설적 감성🔥 락트롯 ∣ 가슴속 응어리를 뻥~ 뚫어버리는 사이다 보컬 ∣ 도…](https://www.youtube.com/watch?v=LmEOZx2IH9M) | 노래마실 [ Music … | 2,790 | 31,666 | 11.3 | ×60.4 | 249.5 | 4.3분 | 2026-06-19 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 19/19 |
| 968 | [Rod Wave - It Will All Work Out - (Official Music Video)](https://www.youtube.com/watch?v=OHYv2zYBdfU) | Street Empire… | 1,570 | 17,757 | 11.3 | ×28.7 | 132.7 | 13분 | 2026-06-12 | 기타 | 한 곡 | 없음 | 5/5 |
| 969 | [Enthiran BGM ∣ A.R. Rahman ∣ 80-Piece Symphony Orchestra](https://www.youtube.com/watch?v=swMgOH67TdI) | Australian In… | 32,600 | 354,648 | 10.9 | – | 2,444.3 | 8.5분 | 2026-06-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 486/486 |
| 970 | [【ドッカンバトル】超サイヤ人孫悟空 本気 bgm](https://www.youtube.com/watch?v=rr_DEN34wp0) | メガゲン | 21,200 | 228,500 | 10.8 | ×8.2 | 4,087.3 | 10.1분 | 2026-08-29 | 기타 | 음악 | 없음 | 175/186 |
| 971 | [【ドッカンバトル】超サイヤ人孫悟空 変身 bgm](https://www.youtube.com/watch?v=nwzLO39prTs) | メガゲン | 21,200 | 227,151 | 10.7 | ×8.1 | 1,439.5 | 10.1분 | 2026-05-19 | 기타 | 음악 | 없음 | 374/377 |
| 972 | [🌸나훈아 - 무시로 (Blues Remix) – 이 감성 뭐냐… l 🎙️별이트로트](https://www.youtube.com/watch?v=bBz2DSGQSIw) | 별이트로트 | 8,030 | 83,828 | 10.4 | ×26.6 | 473.2 | 4.3분 | 2026-04-30 | 9. 가요·발라드·트로트 | 음악 | 설명 | 29/29 |
| 973 | [듣자마자 어깨춤 터지는 신명나는 트로트 찬불가 14곡 #불교음악 #트로트찬불가](https://www.youtube.com/watch?v=EYh7Yz748vs) | 연꽃선율 | 21,500 | 223,761 | 10.4 | ×379.9 | 1,356.6 | 61.5분 | 2026-05-12 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 289/289 |
| 974 | [The Throne Room ∣ House of The Dragon Season 3 Episode 2 En…](https://www.youtube.com/watch?v=s2GxTf1Ft4s) | Jeremy Brauns… | 29,400 | 302,683 | 10.3 | ×7.0 | 2,594.0 | 4.1분 | 2026-06-29 | 13. OST·사운드트랙 | 커버·직접 부른 노래 | 설명 | 163/163 |
| 975 | [슈베르트가 생의 끝에서 남긴 가장 아름다운 노래 ∣ 슈베르트 '세레나데' D.957 (Franz Schub…](https://www.youtube.com/watch?v=15GfRzMd3qw) | 클래식 여행자 (Clas… | 13,800 | 141,180 | 10.2 | ×1.9 | 836.0 | 4.2분 | 2026-05-08 | 기타 | 음악 | 설명 | 38/38 |
| 976 | [【美しいクラシック60分】思わず聴き入る名曲集｜読書・作業・リラックスBGM｜ショパン・ベートーヴェン・バッハ](https://www.youtube.com/watch?v=Us79QrAAa70) | クラシックの森 – Cal… | 49,300 | 495,483 | 10.1 | ×17.2 | 4,291.9 | 62.6분 | 2026-06-30 | 기타 | 정보·해설 | 설명 | 35/37 |
| 977 | [Pan Flute Healing Music ∣ Sacred Andean Melodies for 2 Hours](https://www.youtube.com/watch?v=zq_vdOfFzlc) | Andean Flute … | 4,970 | 49,915 | 10.0 | ×53.6 | 385.6 | 144.8분 | 2026-06-16 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 13/13 |
| 978 | [Wake Up with Krishna 🌿 Peaceful Dawn Meditation Music](https://www.youtube.com/watch?v=1A7xEA1j_Qg) | Moksha Sounds… | 37,000 | 370,692 | 10.0 | ×60.4 | 2,719.1 | 69분 | 2026-06-09 | 1. 수면·명상·힐링 | 음악 | 설명 | 176/178 |
| 979 | [2000년대 히트곡 모음 추억의 노동요 playlist](https://www.youtube.com/watch?v=C4rRsOUQMRg) | 플리 말아주는 주모 | 27,100 | 266,791 | 9.8 | ×1.6 | 1,788.1 | 189.9분 | 2026-05-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 322/322 |
| 980 | [가질수 없는 너(1995) - 뱅크 ∣ Acoustic Cover ∣ 레트로카페](https://www.youtube.com/watch?v=FLzOl-Y5jiw) | 레트로 카페 (Retro… | 12,100 | 119,097 | 9.8 | ×24.8 | 677.9 | 4.6분 | 2026-05-01 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 9/11 |
| 981 | [Jaxson Blue - Honest Work (Official Music Video)](https://www.youtube.com/watch?v=Sbs0YyDhlDI) | Jaxson Blue | 29,300 | 286,555 | 9.8 | – | 2,086.1 | 4.2분 | 2026-06-08 | 기타 | 한 곡 | 설명 | 73/74 |
| 982 | [권태 [감성트롯 끝판왕]연속4번재생](https://www.youtube.com/watch?v=07n66F10ofY) | 리듬다방(김리다) | 1,440 | 14,001 | 9.7 | ×30.4 | 102.5 | 12분 | 2026-06-09 | 9. 가요·발라드·트로트 | 음악 | 설명 | 17/17 |
| 983 | [농도 99%, 취향 좋은 사장님이 아껴둔 흔하지 않은 카페 플리 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 · Minimal Ca…](https://www.youtube.com/watch?v=PyA6gUmJW34) | Radear | 31,400 | 288,861 | 9.2 | ×15.4 | 1,632.9 | 236.8분 | 2026-04-30 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 96/96 |
| 984 | [선선한 가을 밤 잠잘때 듣는 메이플 브금 (풀벌래 ASMR ) ∣ 수면유도음악 8시간](https://www.youtube.com/watch?v=mkpa_vCH-Aw) | DOKANG | 20,700 | 189,105 | 9.1 | ×16.7 | 1,287.3 | 480분 | 2026-05-30 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 61/62 |
| 985 | [Hebt Euch #himmelfahrt #healingmusic #vikingmusic #selbsthe…](https://www.youtube.com/watch?v=QIXGLP6vZgQ) | VikingHealing | 2,640 | 23,963 | 9.1 | ×40.6 | 146.6 | 4분 | 2026-05-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 15/15 |
| 986 | [아름다운 것도 아파 (Beautiful Things Hurt Too) ∣ 여자 듀엣 감성 발라드 Sad E…](https://www.youtube.com/watch?v=jwUGSmtsSIs) | MusicSong | 7,420 | 67,309 | 9.1 | ×167.4 | 394.0 | 4.4분 | 2026-05-06 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 43/43 |
| 987 | ["카페 음악 때문에 또 왔어요" 단골들이 숨겨두고 듣는 미니멀 팝 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 · Minimal C…](https://www.youtube.com/watch?v=fYmDt5bWDxg) | Radear | 31,400 | 280,151 | 8.9 | ×14.9 | 1,785.0 | 243.6분 | 2026-05-20 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 63/63 |
| 988 | [텐션폭발! 운동성공! 오늘부터 내 노동요는 이거다!! [90~2000년대] 클럽 리믹스 35곡 [텐션업 플…](https://www.youtube.com/watch?v=t5GX_3shfEw) | 드루와자기 | 19,800 | 176,379 | 8.9 | ×525.7 | 1,512.3 | 125.2분 | 2026-06-29 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 63/64 |
| 989 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 그대여, -BM](https://www.youtube.com/watch?v=YDESKcB9ppA) | Artist BM | 8,790 | 78,100 | 8.9 | ×2.4 | 1,485.3 | 4분 | 2026-09-01 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 22/23 |
| 990 | [중년 남자의 눈물 쏙 빼는 미친 호소력. '님은 먼곳에' (AI커버블루스 락 Ver.)#김추자 #님은먼곳에…](https://www.youtube.com/watch?v=A0SSBzDh-Ew) | 알고보니 혼비백산 | 43,400 | 380,099 | 8.8 | ×43.9 | 2,160.4 | 5.7분 | 2026-05-01 | 14. AI 음악 | AI 음악 | 설명 | 244/245 |
| 991 | [🏡 평생 잊지 못할 내 마음의 고향 ∣ 힐링 트로트 ∣ 혜영스님](https://www.youtube.com/watch?v=Dx4ewFSkxSg) | 혜영스님 ∣ 힐링트로트 | 7,900 | 68,667 | 8.7 | ×12.0 | 630.7 | 5.7분 | 2026-07-07 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 26/26 |
| 992 | [One Lifetime Wasn't Enough ∣ Emotional Piano Love Ballad ∣ …](https://www.youtube.com/watch?v=b5N4DQLrfAg) | Soft Emotion … | 13,700 | 118,471 | 8.7 | ×14.3 | 1,079.9 | 6분 | 2026-07-06 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 15/15 |
| 993 | [432 Hz Reiki Music for Healing and Cleansing Negativity - 2…](https://www.youtube.com/watch?v=auzLrS12AUo) | Reiki Healing… | 20,100 | 170,875 | 8.5 | ×20.5 | 1,463.5 | 20분 | 2026-06-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 22/24 |
| 994 | [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 나른 야르한 제이팝 플리](https://www.youtube.com/watch?v=6Kd2P_Pu5Ug) | Nonohara | 1,290 | 10,856 | 8.4 | ×5.0 | 151.2 | 14.7분 | 2026-08-13 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 28/28 |
| 995 | [㉖대한민국 정통 트로트 60선 (Korean Trot 60) ∣ 전설의 거장들이 빚어낸 정통 명곡 메들리 …](https://www.youtube.com/watch?v=75u_o8j9V0s) | 트로트의 맛! | 40,700 | 336,224 | 8.3 | – | 1,986.2 | 188.5분 | 2026-05-08 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 174/176 |
| 996 | [🎵Do You Hear Me… — A Story of Love & Loss ∣ Full Emotional …](https://www.youtube.com/watch?v=BwNZ573NSVs) | HeartEcho AI … | 29,500 | 242,555 | 8.2 | ×34.7 | 1,364.3 | 57.9분 | 2026-04-29 | 6. 피아노·클래식·연주곡 | AI 음악 | 설명 | 364/367 |
| 997 | [10. 그리스 이타카, 무화과맛 재즈 ∣ playlist](https://www.youtube.com/watch?v=Nxeex1L0sYU) | dansoonhee | 17,000 | 138,997 | 8.2 | ×14.7 | 1,728.7 | 280.3분 | 2026-08-04 | 7. 재즈·보사노바 | 플레이리스트·모음 | 설명 | 74/75 |
| 998 | [VITAL ENERGY ∣ 432Hz • Clear Overthinking & Awaken Inner Cl…](https://www.youtube.com/watch?v=8EBBcZFo4PU) | Zen Celesta | 49,000 | 397,561 | 8.1 | ×34.0 | 5,535.5 | 60분 | 2026-08-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 102/107 |
| 999 | [Fall 🍂 5 Minute Autumn Timer with Relaxing Piano Music 🍁 (N…](https://www.youtube.com/watch?v=2PQoOVZmxnY) | Timers Box | 2,920 | 23,662 | 8.1 | ×93.0 | 1,005.6 | 5분 | 2026-09-30 | 3. 공부·집중·작업 | 음악 | 설명 | 1/1 |
| 1000 | [너와 걸으며/달달한노래/아련한노래/달콤한노래/잔잔한노래/편안한노래/가을노래/자기전에 듣기좋은 노래/여행갈때…](https://www.youtube.com/watch?v=bzVlQQuegBc) | 황금밴드 / Golden… | 2,000 | 16,143 | 8.1 | ×2.6 | 261.5 | 4.2분 | 2026-08-23 | 9. 가요·발라드·트로트 | 음악 | 설명 | 16/17 |
| 1001 | [In der Walpurgisnacht brennt mein altes Ich #walpurgisnacht…](https://www.youtube.com/watch?v=jugVBYVn8ag) | VikingHealing | 2,640 | 21,266 | 8.1 | ×36.0 | 119.9 | 4.6분 | 2026-04-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 12/12 |
| 1002 | [OUR LADY OF FATIMA HEALING HYMNS ∣ Catholic Prayer Music fo…](https://www.youtube.com/watch?v=kL-iJ_qbbms) | Marian Morning | 35,100 | 281,787 | 8.0 | ×232.0 | 1,717.6 | 183.4분 | 2026-05-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 395/408 |
| 1003 | [Work Music, Deep Focus Music for ADHD Relief and Concentrat…](https://www.youtube.com/watch?v=CQ7p1pOOwrA) | Greenred Prod… | 8,540 | 68,232 | 8.0 | ×24.0 | 464.5 | 9.8분 | 2026-05-30 | 3. 공부·집중·작업 | 음악 | 설명 | 0/0 |
| 1004 | [Odysseus ∣ Epic Orchestral Cover ∣ The Odyssey Ludwig Goran…](https://www.youtube.com/watch?v=Qx1hmx1Fsmc) | Jeremy Brauns… | 29,400 | 229,794 | 7.8 | ×5.3 | 2,381.8 | 8.4분 | 2026-07-19 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 79/79 |
| 1005 | [한여름 밤의 꿈](https://www.youtube.com/watch?v=t87CPyEGmHQ) | 오레 ooree | 18,800 | 144,618 | 7.7 | ×19.2 | 1,095.1 | 119.7분 | 2026-06-14 | 기타 | 플레이리스트·모음 | 설명 | 88/88 |
| 1006 | [[Fanmade OST] 하루의 끝에서/이안대군 테마 **21세기 대군부인** 감성 발라드](https://www.youtube.com/watch?v=sf5dMF71cg4) | ycmusic25 | 13,700 | 103,237 | 7.5 | ×164.4 | 607.5 | 4.1분 | 2026-05-07 | 9. 가요·발라드·트로트 | AI 음악 | 설명 | 79/79 |
| 1007 | [🎵 견디고 또 견딘 당신에게 전하는 메시지 ∣ 너의 봄이 온다 - AIIN](https://www.youtube.com/watch?v=9r7SCZtxgLQ) | 박PD 음악다방 | 9,820 | 73,007 | 7.4 | ×24.7 | 514.3 | 5.8분 | 2026-06-04 | 1. 수면·명상·힐링 | 음악 | 설명 | 48/48 |
| 1008 | [playlist ∣ 여름과 가을사이, 내 독서용 브금](https://www.youtube.com/watch?v=zSUHxG9TGeQ) | centralgrocer… | 27,800 | 205,660 | 7.4 | ×15.2 | 1,988.9 | 225.8분 | 2026-07-12 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 50/50 |
| 1009 | [Samtang Ako May Kinabuhi Pa - Piano Jazz Version ∣ jazz it …](https://www.youtube.com/watch?v=JqWXP8WjhX4) | jazz it back | 7,540 | 55,728 | 7.4 | ×8.1 | 343.7 | 4.2분 | 2026-05-15 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 7/7 |
| 1010 | [Playlist 2016 그곳으로](https://www.youtube.com/watch?v=JXJWz7Ky8KA) | 느좋모음집 | 29,200 | 214,674 | 7.3 | ×8.7 | 1,803.8 | 18.2분 | 2026-06-27 | 기타 | 플레이리스트·모음 | 없음 | 75/76 |
| 1011 | [시작하면 시작된다 ٩(๑❛ᴗ❛๑)۶](https://www.youtube.com/watch?v=gjtaovTAbMU) | 톤톤 tonton | 20,500 | 149,762 | 7.3 | ×23.7 | 1,135.3 | 266.2분 | 2026-06-14 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 72/76 |
| 1012 | [🍂 Cozy September Jazz (NO MID-ROLL ADS) – Warm Piano Music …](https://www.youtube.com/watch?v=zw5ml1zLxPs) | Chill Jazz St… | 25,200 | 182,818 | 7.2 | ×19.0 | 3,663.4 | 376.4분 | 2026-09-04 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 39/39 |
| 1013 | [✨ Музыка восстановления 🕯️ Тибетские поющие чаши для глубок…](https://www.youtube.com/watch?v=hivuH3iFJRw) | МУДРЫЕ МЕДИТА… | 6,810 | 48,979 | 7.2 | ×0.9 | 455.0 | 30.3분 | 2026-07-08 | 1. 수면·명상·힐링 | 음악 | 설명 | 29/29 |
| 1014 | [임재현 - 웃어주지마요 Official MV](https://www.youtube.com/watch?v=L4aOBuPkpLg) | 임재현 Official | 39,200 | 280,748 | 7.2 | – | 2,625.1 | 4.4분 | 2026-07-09 | 기타 | 한 곡 | 없음 | 156/160 |
| 1015 | [푸른 여름 사이로 🌸 여름 감성 피아노 플레이리스트 ∣ BGM ∣ 휴식·힐링·집중](https://www.youtube.com/watch?v=rHuz5RflH24) | Mellow Season | 2,860 | 20,292 | 7.1 | ×2.6 | 219.6 | 135.7분 | 2026-07-23 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 2/2 |
| 1016 | [가시리 ∣ 조선힙합(Official Music Video)](https://www.youtube.com/watch?v=_uYBH28d_ys) | 조선힙합 Official | 30,000 | 212,227 | 7.1 | ×28.8 | 1,268.9 | 4.6분 | 2026-05-10 | 11. 힙합·R&B·EDM | 한 곡 | 설명 | 47/46 |
| 1017 | [[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 주황색, -BM](https://www.youtube.com/watch?v=63-irShSXR0) | Artist BM | 8,790 | 62,060 | 7.1 | ×1.9 | 771.4 | 4.2분 | 2026-08-04 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 23/23 |
| 1018 | [창문으로 여름이 실려오는 브금 𓇼 ⋆.˚](https://www.youtube.com/watch?v=wStibHhXn1A) | 톤톤 tonton | 20,500 | 144,236 | 7.0 | ×22.8 | 829.4 | 250.8분 | 2026-05-03 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 58/58 |
| 1019 | [운동러들이 환장하는 '비트 깡패' 플리 ∣ 파상풍맛 외힙 노동요 playlist](https://www.youtube.com/watch?v=pNmK5x-0bkA) | 플리메이커 | 49,100 | 344,272 | 7.0 | ×6.1 | 2,160.0 | 57.1분 | 2026-05-17 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 142/146 |
| 1020 | [김상민 - You ∣ 여성보컬 개사 커버 ∣ 폭발적인 감성 발라드](https://www.youtube.com/watch?v=uCvyMW60AD4) | 연애상황극 | 11,100 | 76,871 | 6.9 | ×44.7 | 449.2 | 4.2분 | 2026-05-06 | 9. 가요·발라드·트로트 | 커버·직접 부른 노래 | 설명 | 17/17 |
| 1021 | [깊은밤 색소폰 Vol.35 ∣ 시원한 파도 휴식 🌊 ∣ 2시간 힐링 색소폰 연주 ∣ Ocean Waves …](https://www.youtube.com/watch?v=1jrUOOVjFpE) | 고향 가는 나그네 | 2,680 | 18,538 | 6.9 | ×5.6 | 201.6 | 128.2분 | 2026-07-24 | 1. 수면·명상·힐링 | 연주 | 설명 | 22/22 |
| 1022 | [☕️ 다시 듣고 싶은 추억의 애창곡 ∣ 유튜브 발라드 애창곡 20곡 연속듣기 ∣ 김광석 임재범 신승훈 이문…](https://www.youtube.com/watch?v=ZJHh-chAUSQ) | Korean Ballad… | 44,100 | 303,797 | 6.9 | ×267.7 | 2,654.5 | 117.5분 | 2026-07-01 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 40/41 |
| 1023 | [술탄 오브 더 디스코 - 신나는 음악, 잘못된 인생 Good Beats,…](https://www.youtube.com/watch?v=UMinXZIMfQc) | Sultan Of The… | 39,500 | 264,861 | 6.7 | – | 3,581.8 | 4분 | 2026-08-11 | 기타 | 한 곡 | 설명 | 632/632 |
| 1024 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 요즘 제일 핫한 노동요 다 모아놨어요..🤍 (중간광고없음) 10시간 ∣ 감성힙합 R&B 플…](https://www.youtube.com/watch?v=LFFmtspEl8Q) | 중간광고없음 | 18,700 | 125,357 | 6.7 | ×4.3 | 1,170.2 | 601.7분 | 2026-07-09 | 3. 공부·집중·작업 | 플레이리스트·모음 | 없음 | 10/10 |
| 1025 | [🍉여름에 듣기 좋은 카페 음악 🌊 여름 바닷가 카페처럼 기분 좋은 Playlist ∣ 중간 광고 없음 ∣ …](https://www.youtube.com/watch?v=SDGqz6SUFKY) | 오늘의 멜로디 Today… | 19,800 | 126,085 | 6.4 | ×27.8 | 757.9 | 121.5분 | 2026-05-10 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 31/31 |
| 1026 | [Healing Music ∣ Indian Classical Devotional Meditation ∣ Si…](https://www.youtube.com/watch?v=08mQREpo8HM) | RAGA FUSION | 2,100 | 13,327 | 6.3 | – | 101.5 | 18.5분 | 2026-06-14 | 1. 수면·명상·힐링 | 음악 | 설명 | 10/10 |
| 1027 | [㉝대한민국 정통 트로트 100선(Vol.1)(Korean Authentic Trot 100) 한 번 틀면 …](https://www.youtube.com/watch?v=PrpsrGzD3Ag) | 트로트의 맛! | 40,700 | 256,435 | 6.3 | – | 1,895.6 | 311.1분 | 2026-06-11 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 201/212 |
| 1028 | [🎤 이놈아 나좀 살여줘~ / 트롯가수 창 🎶 사랑도 체력이다 인생 풍자 트롯 ✔️](https://www.youtube.com/watch?v=WFt570kk21o) | 우리인생뮤직 | 22,700 | 140,383 | 6.2 | ×50.9 | 795.1 | 4.1분 | 2026-04-30 | 9. 가요·발라드·트로트 | 음악 | 설명 | 137/139 |
| 1029 | [조선힙합🔥연실🔥듣자마자 오늘은 이 리듬🔥오늘의힐링🔥국악힙합🔥노동요🔥퓨전국악🔥Korea Joseon Hip-…](https://www.youtube.com/watch?v=iQkMFMSQVOc) | sisovibe | 2,850 | 17,451 | 6.1 | ×5.7 | 673.0 | 5.2분 | 2026-09-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 24/24 |
| 1030 | [서러워 마라 ∣ 구름 같은 인연이더라](https://www.youtube.com/watch?v=X43yOI7dXDI) | 인생트로트 라운지 | 4,230 | 25,849 | 6.1 | – | 167.7 | 5분 | 2026-05-23 | 기타 | 음악 | 설명 | 13/13 |
| 1031 | [[뮤직비디오] 🎵 사의 찬미 ∣ 원곡 윤심덕 ∣ 감성 리메이크](https://www.youtube.com/watch?v=Au2qy-W1WNA) | 초이스 라이브카페 | 2,220 | 13,050 | 5.9 | ×23.3 | 140.7 | 4.5분 | 2026-07-23 | 4. 카페·매장·라운지 | 한 곡 | 설명 | 6/6 |
| 1032 | [[Playlist]분위기 좋은 카페 하루☕️[중간광고없음]카페 매장 음악 🎧 그냥 틀어두세요, 차 마실 때…](https://www.youtube.com/watch?v=lLEjhHc1Nxw) | BGMBUCKS | 20,300 | 118,908 | 5.9 | – | 746.7 | 80.8분 | 2026-05-18 | 4. 카페·매장·라운지 | 연주 | 설명 | 53/53 |
| 1033 | [노동요로 들으려고 만든 House 하우스 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭](https://www.youtube.com/watch?v=-ExhSbJTkj8) | 노마카세 | 46,200 | 268,875 | 5.8 | ×6.2 | 6,903.9 | 52.1분 | 2026-09-15 | 3. 공부·집중·작업 | 플레이리스트·모음 | 없음 | 143/155 |
| 1034 | [Playlist ∣ 여름, 토마토, 재즈](https://www.youtube.com/watch?v=fl5G97CMAvU) | 야채상회 Vege Mar… | 44,800 | 260,348 | 5.8 | ×17.3 | 2,278.6 | 133.1분 | 2026-07-02 | 7. 재즈·보사노바 | AI 음악 | 설명 | 55/55 |
| 1035 | [Multo by Cup of Joe ∣ Senti Piano Cover ∣ Clyde Pianist ∣ 4K](https://www.youtube.com/watch?v=Sz9HlKCn8Gs) | Clyde Pianist… | 12,200 | 70,183 | 5.8 | ×12.0 | 465.2 | 5.6분 | 2026-05-26 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 44/46 |
| 1036 | [✨ Divine Royal Guanyin: Sacred Protection & Healing Music ∣…](https://www.youtube.com/watch?v=5UT5XqVBEfs) | Eternal Frequ… | 7,510 | 42,469 | 5.7 | ×3.8 | 763.7 | 29.6분 | 2026-08-29 | 1. 수면·명상·힐링 | 음악 | 설명 | 62/62 |
| 1037 | [Sanctum of Roots: The Sanctuary That Calls You Back to Your…](https://www.youtube.com/watch?v=Lh-IDUyiSCc) | Healing Ether | 47,200 | 265,483 | 5.6 | ×30.7 | 1,668.1 | 71.2분 | 2026-05-18 | 1. 수면·명상·힐링 | 음악 | 설명 | 55/54 |
| 1038 | [𝙋𝙇𝘼𝙔𝙇𝙄𝙎𝙏 이상한 가을밤 (Halloween)](https://www.youtube.com/watch?v=rSj2Sx4vx5w) | off frame | 3,450 | 18,848 | 5.5 | ×9.1 | 1,588.9 | 15.3분 | 2026-10-12 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 41/46 |
| 1039 | [Arknights OST - Battleplan Obliteration ∣ アークナイツ/明日方舟 危機契約 …](https://www.youtube.com/watch?v=cY-y4dU2xTk) | RiverV | 49,500 | 267,472 | 5.4 | – | 2,229.6 | 4.1분 | 2026-06-26 | 기타 | 음악 | 설명 | 95/95 |
| 1040 | [Divine Royal Guanyin: Golden Phoenix Blessing & Healing Mus…](https://www.youtube.com/watch?v=W__4-TezX9M) | Eternal Frequ… | 7,510 | 38,718 | 5.2 | ×3.5 | 796.5 | 32분 | 2026-09-05 | 1. 수면·명상·힐링 | 음악 | 설명 | 68/73 |
| 1041 | [🌿 𝑯𝒆𝒂𝒍𝒊𝒎𝒂𝒍𝒔 ∣ 🧘 숲속 호텔의 저녁 명상 클래스 ∣ 싱잉볼 & 잔잔한 피아노 ∣ Meditati…](https://www.youtube.com/watch?v=GjtPZpv7iKo) | 힐리멀스 | 24,100 | 123,889 | 5.1 | ×2.3 | 1,719.2 | 148분 | 2026-08-13 | 1. 수면·명상·힐링 | 음악 | 설명 | 122/124 |
| 1042 | [🙏 기도가 잘되는 팬플룻 찬송가 3시간 ∣ 마음이 평안해지는 독서 · 묵상 · 휴식 음악 ∣ Pan Flu…](https://www.youtube.com/watch?v=QOTgCp4r7fo) | 히솝워십 ∣ Hyssop… | 36,600 | 185,459 | 5.1 | ×13.4 | 1,043.0 | 191.8분 | 2026-04-29 | 15. CCM·찬양·국악… | 긴 한 곡·반복 | 설명 | 290/290 |
| 1043 | [Dopamine Music 🧘‍♂️ मन को शांत करने वाला संगीत ∣ Bansuri & …](https://www.youtube.com/watch?v=h6ERD2c1c0E) | KrishxBeats | 12,100 | 60,533 | 5.0 | ×32.5 | 860.9 | 8.2분 | 2026-08-15 | 1. 수면·명상·힐링 | 음악 | 설명 | 12/13 |
| 1044 | [[Playlist] 예의 없는 조선 디바들의 노동요 🌶️💃 #어우동 #신사임당 #장화홍련 #성춘향 #바리공…](https://www.youtube.com/watch?v=2bp_rmtK96o) | 조선노래꾼 | 6,610 | 32,558 | 4.9 | – | 181.9 | 13.7분 | 2026-04-28 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 60/60 |
| 1045 | [🌙 잠들기 전 듣는 하프 찬송가 3시간 VOL.2 ∣ 마음이 평안해지는 수면 찬송가 · 기도 · 묵상 ∣ …](https://www.youtube.com/watch?v=XqAFJ0UXfNM) | 히솝워십 ∣ Hyssop… | 36,600 | 180,616 | 4.9 | ×13.0 | 1,359.4 | 186.7분 | 2026-06-13 | 1. 수면·명상·힐링 | 긴 한 곡·반복 | 설명 | 376/380 |
| 1046 | [Relaxing Piano Collection ∣ Best of Tyron James ∣ Passacagl…](https://www.youtube.com/watch?v=KbMFv0FHgrY) | tyron james | 26,500 | 118,579 | 4.5 | – | 1,631.6 | 19.8분 | 2026-08-12 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,221/1,316 |
| 1047 | [Dark Violin Focus Techno 🎻 Deep Work Music for Intense Conc…](https://www.youtube.com/watch?v=lC8EFwtdyyw) | INSTRUMENTAL … | 6,000 | 25,524 | 4.2 | ×18.9 | 214.4 | 17.4분 | 2026-06-27 | 6. 피아노·클래식·연주곡 | 한 곡 | 설명 | 37/37 |
| 1048 | [주옥같은 7080 명곡모음 🎶 7080 내 생애 가장 아름다운 추억 🎶 광고 없는 7080 좋은노래 37곡…](https://www.youtube.com/watch?v=VAQ3RjZh_9w) | Enjoy life | 10,400 | 38,738 | 3.7 | ×300.3 | 469.9 | 16.8분 | 2026-08-02 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 9/10 |
| 1049 | [SABILULUNGAN Version 2🌿 Sunda Instrumental Reggae Chill ∣ R…](https://www.youtube.com/watch?v=xtm29OfGf7w) | BASS_DRUM | 16,700 | 61,097 | 3.7 | ×23.2 | 420.7 | 4.6분 | 2026-06-01 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 14/14 |
| 1050 | [Mashup Không buông x Tìm em (Hngle) ∣ Alice Piano cover …](https://www.youtube.com/watch?v=Myx39SJ5uQs) | Alice Piano | 20,400 | 74,090 | 3.6 | ×19.2 | 746.8 | 8분 | 2026-07-17 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 24/24 |
| 1051 | [송골매 - 세상만사 (스토리 뮤직) / 8090명곡/ 감성음악](https://www.youtube.com/watch?v=2AfpfnGCaw4) | 스토리 뮤직 ( Stor… | 7,110 | 25,170 | 3.5 | ×25.5 | 147.7 | 4.7분 | 2026-05-06 | 9. 가요·발라드·트로트 | 음악 | 설명 | 6/6 |
| 1052 | [Reason (OST Trái tim mùa thu ) ∣ Alice Piano cover x Synt…](https://www.youtube.com/watch?v=htWfvXUplM4) | Alice Piano | 20,400 | 72,261 | 3.5 | ×18.7 | 838.1 | 10.8분 | 2026-07-30 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 10/10 |
| 1053 | [minimalist deep house for elevated concentration](https://www.youtube.com/watch?v=SSCthKXaAZQ) | deep archive | 25,900 | 88,549 | 3.4 | ×9.0 | 628.2 | 148.2분 | 2026-06-05 | 2. 자연 소리·백색소음 | 음악 | 설명 | 16/16 |
| 1054 | [우연히 들었는데 이 노래 ... 정말 너무 좋다 ∣ 7080 추억의 올드 팝송 모음 Old Pop Song…](https://www.youtube.com/watch?v=0H6Hqq-H7Y4) | theoldpopsong | 40,900 | 136,787 | 3.3 | ×8.3 | 1,108.4 | 84분 | 2026-06-22 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 109/109 |
| 1055 | [출근길 텐션 끌어올릴 때 듣는 노래 ∣ 국악퓨전 노동요 ∣ 달려](https://www.youtube.com/watch?v=L_l_mIXqCOc) | 저승팝 - 묘령강림 | 9,520 | 30,938 | 3.2 | ×13.3 | 199.7 | 4.9분 | 2026-05-22 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 52/52 |

### 자료를 받지 않은 성공 후보 (699개 중 배수 큰 40개 — 웹 화면 탐색 목록에서 승인하면 분석에 들어감, 성공 사례가 이미 채널당 2개인 채널은 뺌)

| 제목 | 채널 | 구독자 | 조회수 | 배수 | 길이 | 업로드 | 주제 묶음 |
|---|---|---|---|---|---|---|---|
| [Raga of Revenge (Extended Version) ∣ DC ∣ Lokesh Kanagraj ∣…](https://www.youtube.com/watch?v=jEOcIJ4B950) | No Username | 663 | 1,653,715 | 2,494.3 | 4.5분 | 2026-06-01 | 기타 |
| [한 시간만](https://www.youtube.com/watch?v=W0sYhOnCJko) | 조선힙합 - Topic | 25 | 248,191 | 2,481.9 | 4.4분 | 2026-09-14 | 11. 힙합·R&B·EDM |
| [ANDAMANAYA with lyrics (Tagalog Female Version)#ChazzyMusic…](https://www.youtube.com/watch?v=MlM2clMwF0s) | Chazzy Music … | 12,800 | 16,422,297 | 1,283.0 | 5.3분 | 2026-05-02 | 기타 |
| [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 제니 노래 모음 ∣ Jennie playlist](https://www.youtube.com/watch?v=Bv5Ed9dWBaw) | 오느레 | 123 | 104,622 | 850.6 | 27.3분 | 2026-08-30 | 기타 |
| [𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐓𝐫𝐞𝐧𝐝𝐢𝐧𝐠 [𝐍𝐨𝐧𝐬𝐭𝐨𝐩 𝐌𝐚𝐬𝐡𝐮𝐩] 𝐁𝐚𝐢𝐫𝐚𝐧 ∣ 𝐒𝐚𝐡𝐢𝐛𝐚 ∣ 𝐁𝐚𝐫𝐬𝐚…](https://www.youtube.com/watch?v=ASasDfNFPAo) | 𝐀𝐄𝐑Ø™ | 1,420 | 1,176,274 | 828.4 | 22.9분 | 2026-09-15 | 기타 |
| [Alok & Alan Walker - Headlights (feat. KIDDO) ∣ Flipside De…](https://www.youtube.com/watch?v=jW-ysI71WY0) | The Flipside | 18,100 | 14,302,930 | 790.2 | 8.4분 | 2026-05-09 | 5. 운동·드라이브·신나는 |
| [HNGLE Playlist Hay Nhất ∣ Tìm Em, Buông, Không Buông, Cô Đơ…](https://www.youtube.com/watch?v=rHNlIOPIdSM) | hiệu ứng đám … | 1,660 | 1,285,472 | 774.4 | 17분 | 2026-07-09 | 기타 |
| [Thodi Der — Farhan Saeed & Shreya Ghoshal (Half Girlfriend)…](https://www.youtube.com/watch?v=x9wfmi3SyRc) | @Lofi_7ff | 2,020 | 1,473,473 | 729.4 | 5.4분 | 2026-07-20 | 8. 로파이·시티팝·칠 |
| [​🌧️ Dard Dilo Ke -[ Mohammed Irfan] Lofi Flip / Slowed + Re…](https://www.youtube.com/watch?v=iCJoTAtGH0Q) | Lofi__dust | 1,890 | 1,338,764 | 708.3 | 6.6분 | 2026-08-06 | 8. 로파이·시티팝·칠 |
| [Sautin Ke Leke[Slowed+Reverb] Awadesh Premi∣ New Song∣∣ Bho…](https://www.youtube.com/watch?v=6yo2grovVA8) | LofiKosh | 779 | 547,375 | 702.7 | 5.8분 | 2026-10-01 | 8. 로파이·시티팝·칠 |
| [Jay Wheeler - Rubio (Official Video)](https://www.youtube.com/watch?v=_6B2s5psSmQ) | JayWheelerVEVO | 6,830 | 4,196,028 | 614.4 | 4.8분 | 2026-05-29 | 기타 |
| [when you are living your DELULU MOMENTS 💗∣ perfect playlist…](https://www.youtube.com/watch?v=qRGQ3ruB7g8) | Shikhaa Thakur | 1,970 | 1,147,726 | 582.6 | 20.8분 | 2026-08-24 | 기타 |
| [Brown Eyes (Acoustic Jazz Soul Version) ∣ Destiny's Child ∣…](https://www.youtube.com/watch?v=SiSiPtkAY3Y) | SoulPH | 1,930 | 936,470 | 485.2 | 4.6분 | 2026-06-25 | 7. 재즈·보사노바 |
| [2026 랜덤플레이댄스🎀 ∣ 다드루와!!💗 ∣ 2026 랜플댄🍌 ∣ 모르는 노래 없을걸? ∣ 최신곡 다 모…](https://www.youtube.com/watch?v=SaUdZK10Hws) | 바나나한 바냐 | 579 | 264,603 | 457.0 | 5.9분 | 2026-04-27 | 10. 팝송·K팝·J팝 |
| [Songs that make you want to dance ~ 2AM party playlist](https://www.youtube.com/watch?v=ClaVtLtnDsY) | hot nights | 3,240 | 1,455,364 | 449.2 | 26.7분 | 2026-06-24 | 기타 |
| [Beautiful October Autumn Forest 4K 🍁 Peaceful Nature Sounds…](https://www.youtube.com/watch?v=7qgQpr-fyTo) | Nature Harmon… | 2,420 | 1,080,956 | 446.7 | 83.2분 | 2026-09-03 | 1. 수면·명상·힐링 |
| [he is obsessed with you — after all this? — dark romance pl…](https://www.youtube.com/watch?v=TUFYkfqHsEI) | obsessed with… | 2,170 | 959,736 | 442.3 | 32.3분 | 2026-07-14 | 기타 |
| [Aesthetic Road Trip Playlist 🌄 Arijit Singh Songs ∣ Calm Vi…](https://www.youtube.com/watch?v=DZIRWgMYL9g) | VibeHaven | 2,590 | 1,110,846 | 428.9 | 27.9분 | 2026-06-18 | 기타 |
| [[𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭] 전주만 들어도 심장이 뛰는 애니 OST 플리💿](https://www.youtube.com/watch?v=M16IXOXLGAI) | ASMRuru_루루 | 909 | 339,756 | 373.8 | 58.7분 | 2026-06-12 | 13. OST·사운드트랙 |
| [Chahun main ya naa 🥺💔 Ultimate#lofimusic #trendingsong #vir…](https://www.youtube.com/watch?v=7UzXVqnuKqY) | Midnight Mons… | 2,200 | 809,221 | 367.8 | 5.7분 | 2026-08-03 | 8. 로파이·시티팝·칠 |
| [The Sound of Silence ∣ Like You've Never Felt Before ∣ Blue…](https://www.youtube.com/watch?v=cmRcndB-xE8) | PulsedBlues | 18,700 | 6,535,810 | 349.5 | 5.2분 | 2026-07-20 | 6. 피아노·클래식·연주곡 |
| [Heartbreaking 💔 LoFi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=LOXCRBImgw4) | Sammo lagh of… | 2,670 | 903,087 | 338.2 | 8분 | 2026-08-18 | 3. 공부·집중·작업 |
| [✦ 𝐀 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐜𝐮𝐳 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐨𝐛𝐬𝐞𝐬𝐬𝐞𝐝 𝐰𝐢𝐭𝐡 𝐒𝐨𝐮𝐭𝐡 𝐢𝐧𝐝𝐢𝐚𝐧 𝐝𝐢𝐯𝐚𝐬 ✦](https://www.youtube.com/watch?v=WGnsvuBwsE4) | 𝐏ᝰ.ᐟ | 3,160 | 984,517 | 311.6 | 11.3분 | 2026-05-14 | 기타 |
| [Playlist Hot Lana Del Rey 🎧 ∣ Top Songs Collection](https://www.youtube.com/watch?v=H86JZTaEnHM) | PA Nè | 4,710 | 1,429,899 | 303.6 | 23.3분 | 2026-06-02 | 기타 |
| [Kotigobba 2 ∣ Salutilave song video ∣ Kannada Movie 2016 ∣ …](https://www.youtube.com/watch?v=tvAFGclCE24) | Mmusicworld46 | 332 | 97,842 | 294.7 | 4.7분 | 2026-07-20 | 기타 |
| [Đến Khi Nào (Hot Trend) Mặt Trời Ngừng Chiếu ∣ NHỮNG BẢN…](https://www.youtube.com/watch?v=FxUWM0QblFY) | chill out | 4,530 | 1,302,798 | 287.6 | 80분 | 2026-09-16 | 8. 로파이·시티팝·칠 |
| [🌌 If memories had a soundtrack, this would be it.🤧](https://www.youtube.com/watch?v=pRi7ZNEqlOk) | soul wali vib… | 2,490 | 715,820 | 287.5 | 25.3분 | 2026-07-28 | 13. OST·사운드트랙 |
| [Tei Ankho Me Bo Jadu Hai (Slowed & Reverb)New Lofi Song](https://www.youtube.com/watch?v=2VQYOk8CJZk) | Ss raj 67 | 5,050 | 1,439,428 | 285.0 | 6분 | 2026-05-13 | 8. 로파이·시티팝·칠 |
| [Thodi der [lyrics] Farhan saeed & Sherya ghosal](https://www.youtube.com/watch?v=dg7FXktqe1c) | Chill Beats H… | 1,950 | 554,527 | 284.4 | 5분 | 2026-09-01 | 기타 |
| [Chirodini Adhare Kete Gelo E Jibon(Female Version) ∣Relaxin…](https://www.youtube.com/watch?v=CkslS6ahuyA) | Hasanur Ai so… | 12,500 | 3,520,712 | 281.7 | 5.6분 | 2026-05-02 | 8. 로파이·시티팝·칠 |
| [Ek Mulaqat (Slowed + Reverb) Mashup - Arijit Singh x Jubin …](https://www.youtube.com/watch?v=ZQ4JgVWHPwM) | Lost In Lyrics | 1,090 | 293,659 | 269.4 | 14.7분 | 2026-06-29 | 8. 로파이·시티팝·칠 |
| [𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩 b**ch](https://www.youtube.com/watch?v=Ev0TvXow-24) | aa | 1,730 | 454,015 | 262.4 | 16.1분 | 2026-08-03 | 기타 |
| [Just Listen to the Song](https://www.youtube.com/watch?v=GdP7Z11cm3E) | iamkorean | 794 | 208,114 | 262.1 | 45.8분 | 2026-06-21 | 기타 |
| [Ishq Risk 🔥 ∣ Ishq ∣ Ishqa Ve ∣ Ishq E Jaan ∣ Sajde ❤️ ∣ Sl…](https://www.youtube.com/watch?v=iOQi_K5ERfg) | SukumusicHindi | 3,390 | 882,165 | 260.2 | 25.4분 | 2026-09-09 | 8. 로파이·시티팝·칠 |
| [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 로제 노래 모음 ∣ ROSE Playlist](https://www.youtube.com/watch?v=2RfuCXhJNmY) | 오느레 | 123 | 31,695 | 257.7 | 27.4분 | 2026-09-18 | 기타 |
| [Luke’s Diner ∣ Gilmore Girls Ambience ∣ Cozy Acoustic Music…](https://www.youtube.com/watch?v=cT0I4tqsqB8) | Portal to Els… | 3,030 | 777,498 | 256.6 | 124.7분 | 2026-08-25 | 2. 자연 소리·백색소음 |
| [ℙ𝕝𝕒𝕪𝕃𝕚𝕤𝕥 : 늙크크들 회춘시킬 애니 플리](https://www.youtube.com/watch?v=H6TQETWqS6I) | 연하네의 쓸만한 플레이리… | 863 | 220,917 | 256.0 | 131.8분 | 2026-08-17 | 기타 |
| [김추자 석양 1986년 공연, 원본 영상 오디오 그대로 ∣ 가사 자막 ∣ 이별 감성 발라드](https://www.youtube.com/watch?v=EquV6m5VTdY) | 엄마의 세월 - 한국 발… | 1,130 | 286,983 | 254.0 | 5분 | 2026-07-16 | 9. 가요·발라드·트로트 |
| [BHOJPURI PLAYLIST 🌼✨ ~{Timestamp}~ @Desi_.Diva12 #music #ae…](https://www.youtube.com/watch?v=GL7Y0gmUzG0) | Desi_.Diva12 | 6,330 | 1,553,546 | 245.4 | 12.8분 | 2026-07-05 | 기타 |
| [Tự Do Như Cơn Gió∣ Xanh🌿(Lyrics video)🌸 ĐƯỜNG DÀI KIA TỰ DO…](https://www.youtube.com/watch?v=jM6UrE3Bxw4) | Xanh | 46,200 | 10,998,187 | 238.1 | 4.1분 | 2026-06-15 | 기타 |

## 1-2. 같은 채널 안에서 — 잘된 영상 vs 평소 영상 (채널 크기·구독층을 뺀 비교)

채널 922곳의 최근 롱폼(7~365일)에서, 그 채널 조회수 중앙값의 ×3 넘은 **잘된 영상 3608개**와 ×0.5~1.5 인 **평소 영상 4173개** (채널당 5개씩). 같은 채널이니 차이는 채널 크기가 아니라 영상(주제·제목·썸네일·길이) 쪽이다.

### 1-2-1. 제목 특징 (잘된 영상 중 비율 vs 평소 영상 중 비율)

| 제목 특징 | 잘된 영상 | 평소 영상 | 차이 | 표시 |
|---|---|---|---|---|
| 숫자가 들어감 | 36% | 33% | +3%p |  |
| 40자 이상 | 86% | 84% | +1%p |  |
| 따옴표·괄호로 강조 | 17% | 17% | +0%p |  |
| vs 비교 | 1.5% | 1.1% | +0%p |  |
| 말줄임 …·... | 3.4% | 3.0% | +0%p |  |
| 구분 기호(ㅣ·｜·/)로 나눔 | 62% | 62% | +0%p |  |
| 물음표 ? | 1.4% | 1.6% | -0%p |  |
| 느낌표 ! | 1.7% | 1.8% | -0%p |  |
| 패턴형(공통점·특징·이유·N가지·착각·과정) | 0.1% | 0.2% | -0%p |  |
| 과정·벌어진 일·결말·결국 | 0.1% | 0.2% | -0%p |  |
| 손실 낱말(망하·날린·잃은·반토막) | 0.1% | 0.2% | -0%p |  |
| 직접·해보니·N년 기록 | 0% | 0.1% | -0%p |  |
| 빚투·신용·미수·레버리지·대출 | 0.1% | 0% | +0%p |  |
| AI | 8.8% | 8.7% | +0%p |  |
| 이유 | 0.1% | 0.1% | +0%p |  |
| 노후·퇴직금·은퇴·50~70대 | 0.3% | 0.3% | +0%p |  |
| 사연·오디오북·실화·고백 | 0.1% | 0.1% | +0%p |  |
| 25자 미만 | 5.8% | 5.8% | +0%p |  |

### 1-2-2. 주제 묶음 (잘된 영상 중 비율 vs 평소 영상 중 비율)

| 주제 묶음 | 잘된 영상 | 평소 영상 | 차이 |
|---|---|---|---|
| 6. 피아노·클래식·연주곡 | 16% | 15% | +1%p |
| 1. 수면·명상·힐링 | 17% | 17% | +0%p |
| 4. 카페·매장·라운지 | 3.9% | 3.5% | +0%p |
| 10. 팝송·K팝·J팝 | 2.2% | 1.8% | +0%p |
| 2. 자연 소리·백색소음 | 2.8% | 2.6% | +0%p |
| 기타 | 22% | 22% | +0%p |
| 8. 로파이·시티팝·칠 | 9.1% | 9.0% | +0%p |
| 12. 커버·노래 부르기 | 3.0% | 3.0% | +0%p |
| 13. OST·사운드트랙 | 1.0% | 1.1% | -0%p |
| 3. 공부·집중·작업 | 7.5% | 7.7% | -0%p |
| 9. 가요·발라드·트로트 | 6.9% | 7.1% | -0%p |
| 7. 재즈·보사노바 | 2.1% | 2.4% | -0%p |
| 11. 힙합·R&B·EDM | 2.2% | 2.5% | -0%p |
| 14. AI 음악 | 0.8% | 1.1% | -0%p |
| 15. CCM·찬양·국악·동요 | 2.2% | 2.5% | -0%p |
| 5. 운동·드라이브·신나는 | 1.7% | 2.1% | -0%p |

### 1-2-3. 제목 낱말 (같은 채널 안 — 잘된 영상에 더 자주 / 덜 나온 말, 합쳐 5번 이상)

| 낱말 | 잘된 영상 | 평소 영상 | 차이 |
|---|---|---|---|
| Best | 2.9% | 1.9% | +1%p |
| Songs | 6.9% | 6.0% | +1%p |
| Relaxing | 8.3% | 7.5% | +1%p |
| of | 3.9% | 3.1% | +1%p |
| Mix | 3.6% | 2.8% | +1%p |
| playlist | 3.2% | 2.7% | +1%p |
| Playlist | 7.8% | 7.3% | +0%p |
| Journey | 0.8% | 0.3% | +0%p |
| 여름 | 1.1% | 0.6% | +0%p |
| 플리 | 2.1% | 1.7% | +0%p |
| Hits | 1.8% | 1.3% | +0%p |
| 모음 | 3.7% | 3.2% | +0%p |
| 가을 | 2.9% | 4.2% | -1%p |
| Music | 19% | 20% | -1%p |
| Rain | 1.4% | 2.1% | -1%p |
| Deep | 8.3% | 9.0% | -1%p |
| Piano | 5.4% | 6.1% | -1%p |
| in | 2.8% | 3.5% | -1%p |
| 사람 | 0.1% | 0.7% | -1%p |
| Video | 1.1% | 1.7% | -1%p |

- 길이 중앙값: 잘된 영상 55.6분 · 평소 영상 54.7분
- 제목 글자 수 중앙값: 잘된 영상 73.0 · 평소 영상 72
- 타임라인(챕터) 있는 영상: 잘된 영상 28% · 평소 영상 26%

### 1-2-4. 성공 사례와 같은 채널의 평소 영상 (제목 짝 — 썸네일 짝은 5번)

| # | 성공 사례 (채널 평소 대비) | 같은 채널 평소 영상 1 | 같은 채널 평소 영상 2 |
|---|---|---|---|
| 1 | Jay Wheeler, Omar Courtz - De Lejitos (Remix) (Vi… (×163.3) | Jay Wheeler, Kennyy - Corazón De Lego (Offic… (986,185회) | Jay Wheeler, Luar La L, Torrres, Remers - Sh… (513,814회) |
| 2 | 너의 차선 (×98.7) | 한 시간만 (Instrumental) (6,550회) | 형이 말해줄게 (Instrumental) (4,776회) |
| 5 | ขึ้นใจ (3am call) (×570.2) | ขึ้นใจ (3am call) (22,558회) | กี่เหตุผล ( 1000REASONS ) (12,160회) |
| 6 | Veer Hanumana Ati Balwana Ram Ram Ratiyo Re ∣ Arj… (×2,609.3) | Peaceful Siya Ram Dhun ∣ सियाराम धुन ∣ Sitar… (1,123회) | Madhurashtakam ∣ Devotional Krishna Bhajan ∣… (860회) |
| 7 | झूमका झूलनिया Slowed + Reverb ∣ KhesariLal Yadav … (×781.0) | Le Me Saiya Aa Gai Sari DuniyaChhod KelNew T… (5,000회) | Dheere Dheere Se Meri Zindagi (4K Video) Meh… (6,014회) |
| 8 | Ye Tune Kya Kiya (Slowed + Reverb) 🎧 ∣ Lofi Versi… (×4,146.9) | Late Night Sad Songs Mashup 💔 ∣ Arijit Singh… (1,218회) | Saude Bazi - Lofi ∣ Feel the pain of this so… (1,261회) |
| 9 | Khat navajot Ahuja / BGM THE BEST SONG 🥰#viral (×5,569.6) | AFGHAN JALEBI MASUK FAREBI SLOW MOTION THE B… (133회) | Tu HI MERA THE BEST SONG FEEL THE MUSIC 💝#vi… (121회) |
| 11 | DARKHAAST ❤️ ∣ Arijit Singh ∣ Slowed + Reverb ∣ L… (×551.6) | Gehra Hua ❤️ ∣ Official Music Video ∣ Heart … (660회) | Mero Man Lagyo Vrindavan Dham 🙏❤️ ∣ Full Son… (710회) |
| 13 | [playlist] 일하다 어깨 들썩이는 케이팝 노동요 ∣∣ 4K MV (×1,689.6) | [playlist] 오늘은 그냥 누워 있을래 (2,348회) | [PlayList] 무슨 감성이지 (2,427회) |
| 14 | ℙ𝕝𝕒𝕪𝕃𝕚𝕤𝕥 : 늙크크들 원기 회복시킬 애니 플리 (×1,113.6) | 질주 / 이도형 - 오란고교 사교클럽 [한국판 ED] (1,057회) | [노래방] 질주 / 이도형 - 오란고교 사교클럽 [한국판 ED] (610회) |
| 18 | When men loves you harder😭🌷 (×197.7) | 𝑷𝒐𝒗 : 𝒋𝒖𝒔𝒕 𝒔𝒍𝒂𝒚𝒚 𝒊𝒕.. (𝒑𝒍𝒂𝒚𝒍𝒊𝒔𝒕 𝒄𝒂𝒖𝒔𝒆 𝒊𝒕𝒔 𝒚𝒐… (24,985회) | They love you beyond your imagination 🌷😭🫣 (66,112회) |
| 19 | Achhi lagti ho (slowed + reverb ) lofi varsion 🎧 (×347.9) | Tere maste maste do nen ! ( Slowed - tere) (6,001회) | Main Rang Sharbaton Ka [Slowed+Reverb] Lyric… (5,501회) |
| 22 | uMoya 2.0 (Tycoon Remix) (×286.0) | Amaphupho (5,933회) | Ke Mang (3,835회) |
| 23 | Kalyani [slowed & Reverb] ∣∣ With Shreya Ghoshal … (×1,984.0) | Sitaare [Slowed & Reverb] ∣∣ Arijit Singh ∣∣… (2,651회) | Lutt Le Gaya [Slowed & Reverb] ∣∣ Dhurandhar… (2,203회) |
| 24 | Tum Ho Toh - Mashup 2026 ∣ Romantic Love Song ∣ B… (×857.4) | Ek Mulaqat x Mohabbat - Mashup 2026 ∣ Romant… (3,212회) | Haara x Itna Tera Intezaar Kiya - Mashup 202… (3,319회) |
| 26 | Cigarettes After Sex — late night playlist (×408.3) | fall in love again ∣ playlist ∣ (4,110회) | songs that feel like a memory ∣ nostalgic pl… (4,145회) |
| 27 | 어른여자.mp3 (×1,602.8) | 살며시 눈 뜨면 집 근처 코너를 돌던 아빠 차 안 (409회) | 안정형 하이퍼팝과 불안형 일렉트로팝 (341회) |
| 29 | Hey Paaro - Full Song Bgm Raj The Show Man Puneet… (×27.8) | Navagraha ∣ Kan Kanna Salige ∣ HD Song BGM ∣… (13,397회) | Usire Usire Song Video ∣ Kiccha Sudeep ∣ Rek… (14,801회) |
| 31 | 3분 안에 잠드는 수면 음악 (30분) Fall Asleep in 3 Minutes (3… (×150.9) | 수면과학 연구소의 숙면 유도 음악 (15분) Sleep Science Lab ∣… (719회) | 5분 안에 잠드는 수면 음악 (30분) Fall Asleep in 5 Minut… (585회) |
| 32 | 어 난데 여기 핫플이야 (×1,236.2) | 파워워킹 처하자 (750회) | 흔하지 않은 하우스 케이팝 (410회) |

## 1-3. 하루 조회수 상위 — 구독자·올린 날짜 상관없이 (214개, 하루 조회수 큰 순)

하루 조회수 = 조회수 ÷ 올린 지 날수. 경계 = 검색에서 찾은 주제 관련 4분 이상 영상 2,840개 중 상위 10% (**하루 28,349회 이상**). 자료를 받은 영상 중 넘은 것, 채널당 2개 (V# 번호). **성공 사례(1번)와 따로** — 큰 채널 95개, 성공 사례에도 든 것 116개(‘성공 #’ 칸). 글 출처: 설명 205 · 없음 9 · 댓글 받은/달린 1,145,758/1,168,631.

| V# | 제목 | 채널 | 구독자 | 조회수 | 하루 조회수 | 배수 | 올린 지 | 길이 | 주제 묶음 | 형식 | 글 출처 | 댓글 받은/달린 | 성공 # |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V1 | [Shakira, Burna Boy - Dai Dai (Official Video)](https://www.youtube.com/watch?v=fcnDmrtj6Sk) | shakiraVEVO | 19,800,000 | 1,287,676,380 | 8,380,885.6 | 65.0 | 153.6일 | 4분 | 기타 | 한 곡 | 설명 | 362,730/363,834 |  |
| V2 | [KALYANI (with Shreya Ghoshal) OFFICIAL MUSIC VIDEO ∣ ARJN ∣…](https://www.youtube.com/watch?v=xvT1jH8B9AM) | MONEY VERSE R… | 308,000 | 278,049,477 | 2,424,679.1 | 902.8 | 114.7일 | 4.8분 | 기타 | 한 곡 | 설명 | 45,981/46,442 |  |
| V3 | [BASINGA BALAALU FULL SONG ∣ KALYAN KEYS ∣ SHEKAR VIRUS ∣ ES…](https://www.youtube.com/watch?v=A_RV2H2F9jw) | VEDHAS MUSIC | 225,000 | 221,979,190 | 1,666,477.8 | 986.6 | 133.2일 | 4.4분 | 기타 | 음악 | 설명 | 12,032/12,257 |  |
| V4 | [Parvati - Full Song ∣ Hanuman Ansh ∣ Sadhu Tiwari ∣ Shobhin…](https://www.youtube.com/watch?v=s2HYl12gmOY) | Times Music S… | 3,600,000 | 138,151,415 | 1,452,826.3 | 38.4 | 95.1일 | 4.8분 | 기타 | 음악 | 설명 | 17,664/18,016 |  |
| V5 | [Tera Mera Rishta - New Version ∣ Awarapan 2 ∣ Emraan, Disha…](https://www.youtube.com/watch?v=6rvUyBiBtik) | Sony Music In… | 73,400,000 | 112,604,129 | 1,427,139.5 | 1.5 | 78.9일 | 6.2분 | 기타 | 한 곡 | 설명 | 28,405/28,510 |  |
| V6 | [BLOK3 x POİZİ - ÇOK GÜZEL GÜLÜYORSUN (Official Music Vi…](https://www.youtube.com/watch?v=q2IMrkhSjSA) | Blok3 | 2,080,000 | 161,441,003 | 1,141,365.9 | 77.6 | 141.4일 | 4분 | 기타 | 한 곡 | 설명 | 22,349/22,541 |  |
| V7 | [Parvati (Full Song) ∣ Jab Zid Pe Aa Gayi Parvati ∣ Hanuman …](https://www.youtube.com/watch?v=rjfxLq3OQ0w) | Times Music | 18,000,000 | 60,558,111 | 1,123,875.9 | 3.4 | 53.9일 | 5분 | 기타 | 음악 | 설명 | 6,751/6,937 |  |
| V8 | [KALYANI (with Shreya Ghoshal) ARJN ∣ KDS ∣ FIFTY4 ∣ RONN ∣ …](https://www.youtube.com/watch?v=z5y8Clp_TdE) | Universal Mus… | 16,900,000 | 88,668,471 | 1,042,036.0 | 5.2 | 85.1일 | 4.2분 | 기타 | 한 곡 | 설명 | 10,834/11,271 |  |
| V9 | [Ala Bolelo - Lyric Video ∣ Jailer 2 ∣ Superstar Rajinikanth…](https://www.youtube.com/watch?v=hIHUeuw2yj8) | Sun TV | 33,000,000 | 64,949,621 | 1,018,082.2 | 2.0 | 63.8일 | 4분 | 기타 | 한 곡 | 설명 | 16,107/16,451 |  |
| V10 | [Vaaroon Forever (Official Video) ∣ Mirzapur The Movie ∣ Shr…](https://www.youtube.com/watch?v=SQ4jZ-EAL88) | Excel Movies | 4,750,000 | 67,785,432 | 1,012,192.9 | 14.3 | 67.0일 | 4.2분 | 기타 | 한 곡 | 설명 | 5,159/5,188 |  |
| V11 | [Jay Wheeler, Omar Courtz - De Lejitos (Remix) (Video Oficia…](https://www.youtube.com/watch?v=xCkf2L7gFnI) | JayWheelerVEVO | 6,830 | 122,505,421 | 832,084.4 | 17,936.4 | 147.2일 | 4.7분 | 기타 | 음악 | 설명 | 4,024/4,041 | #1 |
| V12 | [Falling In Reverse - "Joseph" (feat. Corey Taylor and Serj …](https://www.youtube.com/watch?v=Tk9TM7-eTmw) | Epitaph Recor… | 4,020,000 | 27,932,630 | 705,147.5 | 7.0 | 39.6일 | 4.3분 | 기타 | 한 곡 | 설명 | 38,146/38,202 |  |
| V13 | [Neno Butterfly Lyric Video∣ Vishwanath and Sons ∣ Suriya, M…](https://www.youtube.com/watch?v=9dV6Hl2u3vM) | Aditya Music | 36,900,000 | 73,052,269 | 575,948.9 | 2.0 | 126.8일 | 4.1분 | 기타 | 한 곡 | 설명 | 4,162/4,241 |  |
| V14 | [JENNIE - FALLEN ANGEL (Official Video)](https://www.youtube.com/watch?v=s466YCiHfKw) | JennieRubyJan… | 25,000 | 32,734,639 | 572,744.8 | 1,309.4 | 57.2일 | 5.7분 | 10. 팝송·K팝·J팝 | 한 곡 | 설명 | 93,592/93,814 | #15 |
| V15 | [Karuppa Kooda Va - Video Song ∣ Suriya's Karuppu ∣ RJ Balaj…](https://www.youtube.com/watch?v=49x5rfxmv4E) | Think Music I… | 23,000,000 | 67,241,556 | 547,569.7 | 2.9 | 122.8일 | 4.4분 | 기타 | 음악 | 설명 | 6,306/6,426 |  |
| V16 | [Parvati (Lyrical) ∣ Jab Zid Pe Aa Gayi Parvati ∣ Hanuman An…](https://www.youtube.com/watch?v=PwTcikeQ8Wg) | Times Music | 18,000,000 | 24,844,155 | 529,211.5 | 1.4 | 46.9일 | 5.1분 | 기타 | 한 곡 | 설명 | 3,394/3,401 |  |
| V17 | [[추석 특집] 제나의 트로트 메들리](https://www.youtube.com/watch?v=JYUilbw34Z0) | 안녕하세요원이입니다잘부탁… | 2,370,000 | 18,984,421 | 528,754.5 | 8.0 | 35.9일 | 11.3분 | 9. 가요·발라드·트로트 | 플레이리스트·모음 | 설명 | 74,907/75,550 |  |
| V18 | [Kath Lagda - Navaan Sandhu ft Dhanda Nyoliwala ( Official M…](https://www.youtube.com/watch?v=nMozMETeCyw) | Navaan Sandhu | 1,410,000 | 66,886,349 | 498,810.6 | 47.4 | 134.1일 | 5.2분 | 기타 | 한 곡 | 설명 | 21,291/21,347 |  |
| V19 | [Pattampoochi Lyric Video ∣ Vishwanath and Sons ∣ Suriya, Ma…](https://www.youtube.com/watch?v=Bm9lLpmPM0A) | Aditya Music … | 3,390,000 | 60,179,468 | 474,458.7 | 17.8 | 126.8일 | 4.1분 | 기타 | 한 곡 | 설명 | 6,189/6,242 |  |
| V20 | [Thalapathy Kacheri Full Video (Tamil) ∣ Hon’ble CM Thalapat…](https://www.youtube.com/watch?v=6JaeasJw-QI) | T-Series | 316,000,000 | 35,037,888 | 450,120.7 | 0.1 | 77.8일 | 4.9분 | 기타 | 음악 | 설명 | 4,983/5,077 |  |
| V21 | [Narak ∣ Jai Randhhawa ∣ Shehnaaz Gill ∣ Ishqnama ∣ Arvvindr…](https://www.youtube.com/watch?v=mlb5yBGTTRI) | Tips Punjabi | 5,180,000 | 46,331,711 | 433,141.9 | 8.9 | 107.0일 | 4.4분 | 기타 | 음악 | 설명 | 6,537/6,571 |  |
| V22 | [Headliner ∣ Navaan Sandhu ∣ Haakam ( Official Video ) Shimm…](https://www.youtube.com/watch?v=GE6w7DRyqcM) | Navaan Sandhu | 1,410,000 | 43,728,827 | 415,936.9 | 31.0 | 105.1일 | 5.2분 | 기타 | 한 곡 | 설명 | 10,247/10,260 |  |
| V23 | [God Mode - Video Song ∣ Suriya's Karuppu ∣ RJ Balaji ∣@SaiA…](https://www.youtube.com/watch?v=_Vp-jCG7gno) | Think Music I… | 23,000,000 | 53,716,679 | 378,931.5 | 2.3 | 141.8일 | 4.2분 | 기타 | 한 곡 | 설명 | 5,048/5,086 |  |
| V24 | [Sambavakaari Video Song ∣ Gatta Kusthi 2 ∣ Vishnu Vishal, A…](https://www.youtube.com/watch?v=undhkaMMenU) | Sony Music So… | 21,800,000 | 34,638,358 | 333,436.4 | 1.6 | 103.9일 | 4.1분 | 기타 | 음악 | 설명 | 1,580/1,602 |  |
| V25 | [Dangrangto - 'xương rồng (intro)' (Prod. DONAL)](https://www.youtube.com/watch?v=4jjOH2FR6-E) | Dangrangto | 254,000 | 41,802,603 | 324,660.5 | 164.6 | 128.8일 | 4.2분 | 기타 | 정보·해설 | 설명 | 2,134/2,134 |  |
| V26 | [Feel The Pain - Chillout Mashup ∣ Lo-fi 2307 ∣ Arijit SIngh…](https://www.youtube.com/watch?v=D_J4cGrygxg) | Lo-fi 2307 | 1,070,000 | 4,547,832 | 289,488.2 | 4.2 | 15.7일 | 6.2분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 88/94 |  |
| V27 | [Chirya Boli Chu Chu ∣ Allah Hoo Allah Hoo ∣ Soothing Islami…](https://www.youtube.com/watch?v=qaM8EL9KDDA) | Little Heart … | 52,200 | 42,597,541 | 248,663.9 | 816.0 | 171.3일 | 4.6분 | 1. 수면·명상·힐링 | 음악 | 설명 | 0/0 |  |
| V28 | [Chalre Chalre Waal Song - Tu Sanwal Phul Kasturi (lyrical V…](https://www.youtube.com/watch?v=PgKjt5Aygps) | ISAR"MUSIC | 62,000 | 2,898,140 | 243,835.8 | 46.7 | 11.9일 | 4.5분 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 196/215 |  |
| V29 | [G-Wagona Wale (Official Music Video) R Nait ∣ Isha Sharma ∣…](https://www.youtube.com/watch?v=DgsZHiA03KI) | JCD MUSIC | 876,000 | 8,270,766 | 228,901.6 | 9.4 | 36.1일 | 4.3분 | 기타 | 한 곡 | 설명 | 520/520 |  |
| V30 | [Hangova - Music Video ∣ DC ∣ Lokesh Kanagaraj∣ Sun Pictures…](https://www.youtube.com/watch?v=wc8XNJ2x1Xs) | Sun TV | 33,000,000 | 20,617,104 | 187,781.9 | 0.6 | 109.8일 | 4분 | 기타 | 한 곡 | 설명 | 2,972/2,973 |  |
| V31 | [Hangova (From "DC")](https://www.youtube.com/watch?v=B6ppp6WBCKg) | Anirudh Ravic… | 31,700 | 20,510,948 | 186,727.9 | 647.0 | 109.8일 | 4.1분 | 기타 | 정보·해설 | 설명 | 0/1,473 | #64 |
| V32 | [Barsaat 🌧️∣ All Trending Songs ∣ Taare x Samjho Na x Safar …](https://www.youtube.com/watch?v=41HX_5G6eqQ) | Voxwaves | 17,500 | 8,655,656 | 183,157.4 | 494.6 | 47.3일 | 22.9분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,062/1,197 | #97 |
| V33 | [Vaaste 8K Video Song: Dhvani B, Siddharth G ∣ Tanishk B,Nik…](https://www.youtube.com/watch?v=eTl-FnVvGu0) | T-Series | 316,000,000 | 16,812,403 | 175,038.1 | 0.1 | 96.0일 | 4.3분 | 기타 | 음악 | 설명 | 1,418/1,417 |  |
| V34 | [Arijit Singh - Tujhko (from Cocktail 2) Rashmika Mandanna, …](https://www.youtube.com/watch?v=WWIfHemqSEA) | iPop Superhits | 50,100 | 24,368,262 | 171,498.6 | 486.4 | 142.1일 | 5.6분 | 기타 | 한 곡 | 설명 | 1,133/1,144 |  |
| V35 | [ALL TRENDING HINDI SONGS 2026...PLAYLIST #asthetic #trend #…](https://www.youtube.com/watch?v=xI0IEWIxUBQ) | Rb Lofi | 27,000 | 10,422,745 | 168,182.4 | 386.0 | 62.0일 | 7.9분 | 기타 | 플레이리스트·모음 | 없음 | 1,565/1,716 | #141 |
| V36 | [sombr - My Body Isn't Ready (official video)](https://www.youtube.com/watch?v=ofywN3NgGqY) | sombr | 1,170,000 | 19,497,149 | 161,930.9 | 16.7 | 120.4일 | 4.6분 | 기타 | 한 곡 | 설명 | 8,769/8,789 |  |
| V37 | [Achchi Lagti Ho (Slowed + Reverb) ∣ Lofi Version 🎧](https://www.youtube.com/watch?v=fc8Mab9zGkg) | GTAvexo9 | 24,100 | 15,553,534 | 159,204.1 | 645.4 | 97.7일 | 6.5분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 2,047/2,141 | #65 |
| V38 | [katseye playlist✨💋](https://www.youtube.com/watch?v=H40nuw4mebU) | maiia | 23,200 | 8,535,456 | 157,185.1 | 367.9 | 54.3일 | 21.3분 | 기타 | 플레이리스트·모음 | 없음 | 4,330/4,722 | #152 |
| V39 | [Tere Paas Main∣Main Vaapas Aaunga∣@diljitdosanjh,@ARRahman,…](https://www.youtube.com/watch?v=k3AqQzW3cGI) | Tips Official | 82,600,000 | 13,982,790 | 151,887.7 | 0.2 | 92.1일 | 4.1분 | 기타 | 한 곡 | 설명 | 1,557/1,557 |  |
| V40 | [Nếu Như Ta Chẳng Còn - MCK (ft. A$AP Ướt Mi)](https://www.youtube.com/watch?v=rYWLIJB214Q) | MCK // Nger | 1,070,000 | 19,394,869 | 150,641.3 | 18.1 | 128.7일 | 5.2분 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 5,075/5,075 |  |
| V41 | [Most Viral Phonk/Funk 2026 🎵](https://www.youtube.com/watch?v=CuR4HJsq5RA) | NTL Funk | 168,000 | 19,466,072 | 146,708.6 | 115.9 | 132.7일 | 18.4분 | 기타 | 플레이리스트·모음 | 설명 | 6,535/6,598 |  |
| V42 | [ĐẾN KHI NÀO (Hot Trend)...Mặt Trời Ngừng Chiếu ∣ Những Bản …](https://www.youtube.com/watch?v=pB64u5qBd5g) | Chà Là Chill | 38,900 | 7,327,149 | 138,395.9 | 188.4 | 52.9일 | 91.8분 | 8. 로파이·시티팝·칠 | 긴 한 곡·반복 | 설명 | 509/518 | #296 |
| V43 | [ขึ้นใจ (3am call)](https://www.youtube.com/watch?v=r1Eb1qnqLzA) | Mirrr - Topic | 4,290 | 12,861,686 | 138,070.5 | 2,998.1 | 93.2일 | 4.4분 | 기타 | 음악 | 설명 | 0/281 | #5 |
| V44 | [Jaadu (Official Video) - Filmy & Rawme Hooda ∣ New Haryanvi…](https://www.youtube.com/watch?v=qU5ezUVgovg) | Real Music | 5,080,000 | 6,213,618 | 134,692.5 | 1.2 | 46.1일 | 4분 | 기타 | 한 곡 | 설명 | 2,917/2,917 |  |
| V45 | [WOODZ X 이승철 - 우리만의 이야기 [Official MV]](https://www.youtube.com/watch?v=swbPnEZrQjE) | LEE SEUNGCHUL | 94,700 | 3,124,539 | 130,485.7 | 33.0 | 23.9일 | 4.2분 | 10. 팝송·K팝·J팝 | 한 곡 | 설명 | 545/546 |  |
| V46 | [💋 A Chatpati Playlist Only For Chatpata People 😋✨ ∣ Ultimat…](https://www.youtube.com/watch?v=3FhXwFGVaDE) | JellyBloxify | 34,000 | 17,475,309 | 124,741.1 | 514.0 | 140.1일 | 7.5분 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 2,208/2,242 | #92 |
| V47 | [Bass Thioung - BAOL (Clip Officiel) Ft. Nafi & Alassane](https://www.youtube.com/watch?v=ttkXaHl0o5g) | Bass Thioung | 646,000 | 18,600,930 | 124,155.0 | 28.8 | 149.8일 | 5.4분 | 기타 | 음악 | 설명 | 1,639/1,642 |  |
| V48 | [Mind relaxing lofi song Arijit Singh ∣ Soft songs ∣ Arijit …](https://www.youtube.com/watch?v=43y5rT7YjQY) | Y Music 2 | 36,800 | 17,406,323 | 119,984.7 | 473.0 | 145.1일 | 27.9분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,372/1,403 | #105 |
| V49 | [Ama hem hem](https://www.youtube.com/watch?v=rPmZucO77sg) | Thatohatsi - … | 36,400 | 12,824,484 | 119,965.5 | 352.3 | 106.9일 | 7.5분 | 기타 | 정보·해설 | 설명 | 0/2,609 | #160 |
| V50 | [Mann mera (Original Version) ∣ Slowed + Reverb ∣ Gajendra V…](https://www.youtube.com/watch?v=4ObYNh1TOHY) | LOFI ZONE 990K | 16,900 | 10,547,075 | 118,286.2 | 624.1 | 89.2일 | 5분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,591/1,648 | #66 |
| V51 | [Syumekal Gebre - Gojamoch Zenetu ∣ ስዩመቃል ገብሬ ∣ ጎጃሞች ዘነጡ ∣ N…](https://www.youtube.com/watch?v=adtJUEOe9sA) | Nahom Records… | 3,100,000 | 18,877,859 | 111,907.0 | 6.1 | 168.7일 | 6.9분 | 기타 | 한 곡 | 설명 | 3,764/3,766 |  |
| V52 | [FUNK ABNORMAL (ULTRA SLOWED)](https://www.youtube.com/watch?v=8dOMXfWmghg) | SUKA. | 1,630,000 | 17,715,641 | 109,577.9 | 10.9 | 161.7일 | 5.6분 | 기타 | 플레이리스트·모음 | 설명 | 3,683/3,688 |  |
| V53 | [Pov :- Bhojpuri playlist 🔥 ∣∣ chill guys and enjoy 😎∣∣ Ansh…](https://www.youtube.com/watch?v=4mnrtxd_GhE) | Anshika | 20,300 | 8,819,776 | 109,287.9 | 434.5 | 80.7일 | 11.6분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,684/1,725 | #120 |
| V54 | [Vintage Vibes: Best of 80s with Cyndi Lauper, Modern Talkin…](https://www.youtube.com/watch?v=1n5pMgUPYnk) | Disco Paradis… | 26,800 | 7,187,964 | 101,674.8 | 268.2 | 70.7일 | 117.2분 | 기타 | 플레이리스트·모음 | 설명 | 523/548 | #226 |
| V55 | [𝐀𝐋𝐋 𝐓𝐑𝐄𝐍𝐃𝐈𝐍𝐆 𝐇𝐈𝐍𝐃𝐈 𝐒𝐎𝐍𝐆𝐒 𝟐𝟎𝟐𝟔 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 🎀](https://www.youtube.com/watch?v=qZ78-_PdbwQ) | Aesthetic boo… | 88,000 | 12,240,954 | 101,499.8 | 139.1 | 120.6일 | 11.9분 | 기타 | 플레이리스트·모음 | 설명 | 7,609/7,612 |  |
| V56 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Sad…](https://www.youtube.com/watch?v=KjFcRYZBKs0) | Music Nest HD | 12,200 | 2,712,244 | 99,919.0 | 222.3 | 27.1일 | 8.9분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 101/103 | #263 |
| V57 | [Happy Morning Jazz 🎶 January Bossa Nova Instrumental and Re…](https://www.youtube.com/watch?v=qZjNyrGF4pk) | FunToon Rhymes | 12,300 | 1,795,867 | 99,793.3 | 146.0 | 18.0일 | 15.4분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 0/0 | #353 |
| V58 | [90’S Old Hindi Songs🥰 90s Love Song💘 Udit Narayan, Alka Yag…](https://www.youtube.com/watch?v=qDOFK8SfKmA) | 90s Lovers Po… | 17,600 | 6,603,923 | 96,677.1 | 375.2 | 68.3일 | 27.4분 | 기타 | 음악 | 설명 | 217/234 | #146 |
| V59 | [Patar Bashori ∣ পাতার বাঁশরী ∣ Lofi Bangla Song ∣ Emotional…](https://www.youtube.com/watch?v=rgKNbCrC-cc) | Jasu LOFI | 26,700 | 8,123,568 | 94,760.6 | 304.2 | 85.7일 | 4.1분 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 1,081/1,119 | #201 |
| V60 | [[Playlist] When music is all you need](https://www.youtube.com/watch?v=XXKXpf7xFC4) | encore. | 7,210 | 3,168,321 | 93,278.5 | 439.4 | 34.0일 | 20.9분 | 기타 | 플레이리스트·모음 | 설명 | 518/715 | #117 |
| V61 | [Odysseus](https://www.youtube.com/watch?v=WCxx_OVOVUw) | Ludwig Görans… | 43,300 | 9,212,521 | 92,213.6 | 212.8 | 99.9일 | 8.7분 | 13. OST·사운드트랙 | 음악 | 설명 | 0/5,658 | #274 |
| V62 | [𝐀𝐋𝐋 𝐓𝐑𝐄𝐍𝐃𝐈𝐍𝐆 𝐇𝐈𝐍𝐃𝐈 𝐒𝐎𝐍𝐆𝐒 𝟐𝟎𝟐𝟔 ∣ 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 🎀 ∣COZI](https://www.youtube.com/watch?v=HNdauINck9s) | cozi_music | 32,800 | 8,388,031 | 91,248.7 | 255.7 | 91.9일 | 15.2분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 2,887/2,956 | #238 |
| V63 | [Hyperfocus ∣ LOCK IN for 3 Hours ∣ Deep Work Study With Me …](https://www.youtube.com/watch?v=UXwJ9RwdyHs) | Work With Paul | 19,500 | 4,258,886 | 90,478.4 | 218.4 | 47.1일 | 172분 | 3. 공부·집중·작업 | 긴 한 곡·반복 | 설명 | 492/536 | #267 |
| V64 | [Karuppa Kooda Va (From "Karuppu")](https://www.youtube.com/watch?v=WIbmUGWykTw) | Sai Abhyankka… | 66,600 | 16,146,453 | 90,368.3 | 242.4 | 178.7일 | 4.2분 | 기타 | 음악 | 설명 | 0/1,559 |  |
| V65 | [DJ Phaphane - Amapiano To The World ∣ Paris Nights](https://www.youtube.com/watch?v=O1sU1F6dZNk) | DJ Phaphane | 135,000 | 14,049,343 | 87,976.4 | 104.1 | 159.7일 | 63.9분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 5,141/5,165 |  |
| V66 | [🔥 𝗔𝗟𝗟 𝗧𝗥𝗘𝗡𝗗𝗜𝗡𝗚 𝗣𝗔𝗞𝗜𝗦𝗧𝗔𝗡𝗜 𝗦𝗢𝗡𝗚𝗦 🎶 ∣ 𝗩𝗜𝗥𝗔𝗟 𝗛𝗜𝗧𝗦 𝟮𝟬𝟮𝟲 🎧 ∣ 𝗧𝗢𝗣 …](https://www.youtube.com/watch?v=XL5PUUwrztg) | cozi_music | 32,800 | 6,123,748 | 87,576.5 | 186.7 | 69.9일 | 19.6분 | 1. 수면·명상·힐링 | AI 음악 | 설명 | 2,153/2,307 | #298 |
| V67 | [Playlist For You To Create Fake Scenarios In Your Mind 🤍 ∣ …](https://www.youtube.com/watch?v=0gUwbTCQ78k) | NOXTUNE | 21,000 | 6,635,761 | 86,544.2 | 316.0 | 76.7일 | 12.6분 | 기타 | 플레이리스트·모음 | 설명 | 1,399/1,438 | #189 |
| V68 | [Noah Kahan - Orbiter (Official Lyric Video)](https://www.youtube.com/watch?v=OFcKm-5jSQE) | NoahKahanVEVO | 29,700 | 15,563,086 | 85,361.1 | 524.0 | 182.3일 | 4.8분 | 기타 | 한 곡 | 설명 | 1,405/1,426 |  |
| V69 | ["सुकून भरी रातें 🌙 ∣ Romantic Hindi LoFi Songs ∣ Relaxing S…](https://www.youtube.com/watch?v=DU0Swx5GKB4) | Hindi Tuning | 25,200 | 2,422,424 | 81,747.7 | 96.1 | 29.6일 | 104분 | 1. 수면·명상·힐링 | 음악 | 설명 | 61/93 | #462 |
| V70 | [○ Bollywood navratri song playlist ○ #navratri #garbasongs …](https://www.youtube.com/watch?v=g9nj1SDsXng) | july_luna | 5,480 | 2,738,151 | 81,531.8 | 499.7 | 33.6일 | 18.9분 | 기타 | 플레이리스트·모음 | 없음 | 102/129 | #96 |
| V71 | [Andekhi Anjaani si ∣ Slowed x Reverb ∣ lofi song ∣ lofi ver…](https://www.youtube.com/watch?v=FrqyfSyxOc4) | Midnight lofi… | 4,050 | 4,191,954 | 80,832.5 | 1,035.0 | 51.9일 | 6분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 132/133 | #33 |
| V72 | [Asalayavale (From "Khalifa")](https://www.youtube.com/watch?v=3igIAOJlJ2s) | Jakes Bejoy -… | 186,000 | 7,694,510 | 80,406.2 | 41.4 | 95.7일 | 5분 | 기타 | 음악 | 설명 | 0/0 |  |
| V73 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Stu…](https://www.youtube.com/watch?v=MvV7_DKFZQA) | peacefulvibes… | 12,900 | 4,803,102 | 79,987.2 | 372.3 | 60.0일 | 16.3분 | 3. 공부·집중·작업 | 음악 | 설명 | 284/292 | #149 |
| V74 | [Chris Brown - Fallin' (Official Video) ft. Leon Thomas](https://www.youtube.com/watch?v=-CepAYN0WyM) | ChrisBrownVEVO | 11,700,000 | 13,970,596 | 79,534.7 | 1.2 | 175.7일 | 8.5분 | 11. 힙합·R&B·EDM | 한 곡 | 설명 | 24,441/24,441 |  |
| V75 | ["Golden Autumn Pond" Beautiful Relaxing Music, Peaceful Soo…](https://www.youtube.com/watch?v=wWvxaQRIt0k) | Tim Janis | 2,170,000 | 1,217,360 | 79,459.0 | 0.6 | 15.3일 | 8.6분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 116/122 |  |
| V76 | [Very Powerful Morning Mantras ∣ Ganesh, Shiva, Hanuman,Gaya…](https://www.youtube.com/watch?v=uxQaS8og_Tc) | Vedic chants … | 126,000 | 12,005,933 | 79,068.2 | 95.3 | 151.8일 | 50.6분 | 1. 수면·명상·힐링 | 음악 | 설명 | 5,279/5,279 |  |
| V77 | [Shri Krishna Govind Hare Murari - Non Stop Krishna Bhajans …](https://www.youtube.com/watch?v=Tqr5PqrzeQw) | Bhajan World … | 33,000 | 9,143,789 | 78,286.1 | 277.1 | 116.8일 | 29.8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,540/1,543 | #216 |
| V78 | [“모든 장르를 소화하네” 🥹 성시경이 반한 ‘고막 올라운더’ 도경수 #성시경의고막남친 ㅣ KBS 26091…](https://www.youtube.com/watch?v=ltqA0UR0I2E) | KBS 한국방송 | 2,780,000 | 3,285,160 | 77,740.0 | 1.2 | 42.3일 | 15.8분 | 기타 | 정보·해설 | 설명 | 1,502/1,502 |  |
| V79 | [Ishq X Barbaad - Mashup (Full Version) Lo-fi 2307 ∣ Jubin N…](https://www.youtube.com/watch?v=lFlK7t1INjA) | Lo-fi 2307 | 1,070,000 | 9,704,819 | 77,607.5 | 9.1 | 125.0일 | 5.8분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 300/300 |  |
| V80 | [음악중심 육아일기 ∣ T:TIME ∣ TXT (투모로우바이투게더)](https://www.youtube.com/watch?v=g9YbAlUZqa4) | TOMORROW X TO… | 13,900,000 | 10,455,077 | 76,953.4 | 0.8 | 135.9일 | 7.2분 | 기타 | 음악 | 설명 | 1,034/1,036 |  |
| V81 | [Best Morning Powerful Mantras ∣ Ganesh, Durga, Shiva, Gayat…](https://www.youtube.com/watch?v=1aDk9BdZ8uc) | Sanatan Mantr… | 100,000 | 12,883,505 | 76,836.3 | 128.8 | 167.7일 | 14.9분 | 1. 수면·명상·힐링 | 음악 | 설명 | 3,194/3,194 |  |
| V82 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=FB8QuMi3fTs) | Z B Official … | 22,700 | 4,989,375 | 76,638.5 | 219.8 | 65.1일 | 7.7분 | 3. 공부·집중·작업 | 음악 | 설명 | 203/205 | #264 |
| V83 | [Tum Jo Aaye ✨ ∣∣ Kitab Song ∣∣ Bairan ( Slowed X Reverb ) M…](https://www.youtube.com/watch?v=xyL4vZnw5xs) | Mix Facto 02 | 41,200 | 12,628,093 | 76,184.1 | 306.5 | 165.8일 | 20.3분 | 기타 | 음악 | 설명 | 2,719/2,751 | #198 |
| V84 | [CORTIS (코르티스) 'REDRED' Dance Practice (Fix ver.)](https://www.youtube.com/watch?v=kuVNutQeBBA) | CORTIS | 7,480,000 | 13,696,198 | 76,165.8 | 1.8 | 179.8일 | 4.4분 | 기타 | 음악 | 설명 | 5,480/5,487 |  |
| V85 | [Heartbreaking 💔 songs + lofi Mashup songs Slowed Reverb son…](https://www.youtube.com/watch?v=swi-om1VW34) | JR buzdar off… | 16,900 | 4,526,034 | 75,189.8 | 267.8 | 60.2일 | 8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 202/205 | #227 |
| V86 | [90s Bollywood All Time Hit Songs ∣ 90s Evergreen Songs ∣ 90…](https://www.youtube.com/watch?v=1YddSDFIsk4) | Tips Official | 82,600,000 | 11,519,946 | 74,378.2 | 0.1 | 154.9일 | 69.4분 | 기타 | 음악 | 설명 | 441/442 |  |
| V87 | [Heartbreaking 💔 Lofi Mashup 🎧 Slowed + Reverb Songs ∣ Study…](https://www.youtube.com/watch?v=099F7hK6c8c) | Song verse Hi… | 10,300 | 2,987,057 | 74,199.4 | 290.0 | 40.3일 | 13분 | 3. 공부·집중·작업 | 음악 | 설명 | 186/189 | #210 |
| V88 | [NEW VIRAL BUDOTS REMIX 2026 - NONSTOP TIKTOK DANCE TREND PA…](https://www.youtube.com/watch?v=y2njcNWs9nk) | DJ EJ REMIX | 116,000 | 6,939,575 | 73,574.4 | 59.8 | 94.3일 | 26.6분 | 기타 | 음악 | 설명 | 669/671 |  |
| V89 | [THEN・❥・ Sweet Dreams ∣ Cinematic Techno](https://www.youtube.com/watch?v=0QAKKYJJ2l0) | THEN | 9,750 | 10,080,906 | 73,239.3 | 1,033.9 | 137.6일 | 4.4분 | 기타 | 커버·직접 부른 노래 | 설명 | 491/497 | #34 |
| V90 | [Playlist for how a villain in love sounds like 🎧🔥✨.](https://www.youtube.com/watch?v=4NVS6d5eGyA) | Fictional Hea… | 3,290 | 4,300,581 | 73,004.9 | 1,307.2 | 58.9일 | 9.7분 | 기타 | 플레이리스트·모음 | 설명 | 324/336 | #17 |
| V91 | [Viral Songs Playlist 2026 ∣ Barsaat, Sheesha, Parvati, Roots](https://www.youtube.com/watch?v=nmc4ScFV3j4) | Vijay Garje | 3,540 | 1,441,984 | 72,828.6 | 407.3 | 19.8일 | 31.3분 | 기타 | 플레이리스트·모음 | 설명 | 320/439 | #131 |
| V92 | [Felix "다시 사랑한다 말할까" Cover (원곡 : 김동률) ∣ [Stray Kids : SKZ-RE…](https://www.youtube.com/watch?v=uvcpylgYDSU) | Stray Kids | 25,500,000 | 2,444,082 | 72,354.6 | 0.1 | 33.8일 | 4.2분 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 15,572/15,583 |  |
| V93 | [BIGBANG (빅뱅) - 뱅뱅뱅 (BANG BANG BANG) (트로트 버전) [MV]](https://www.youtube.com/watch?v=wD9nunl0nKY) | ERRDAY DRIP (… | 236,000 | 6,912,784 | 71,852.9 | 29.3 | 96.2일 | 4.1분 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 6,325/6,351 |  |
| V94 | [LOVEIN & Ismail Uluçay - Drafting (Original Mix)](https://www.youtube.com/watch?v=clQARvetnyk) | LOVEIN | 40,500 | 12,216,195 | 71,133.2 | 301.6 | 171.7일 | 7.3분 | 4. 카페·매장·라운지 | 음악 | 설명 | 422/430 | #202 |
| V95 | [Sitaare [Slowed+Reverb] - Arijit Singh ∣ Amitabh Bhattachar…](https://www.youtube.com/watch?v=3_Y885eZ4Es) | Manan mp3 | 779,000 | 12,547,302 | 68,474.3 | 16.1 | 183.2일 | 4.4분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 861/856 |  |
| V96 | [When men loves you harder😭🌷](https://www.youtube.com/watch?v=2q4x4Ftz7mg) | wavy~ | 2,030 | 2,646,979 | 66,513.1 | 1,303.9 | 39.8일 | 9.3분 | 기타 | 플레이리스트·모음 | 설명 | 487/538 | #18 |
| V97 | [A playlist of nusrat fateh ali khan all popular qawaali's 💝💘](https://www.youtube.com/watch?v=idCpl6LfnKo) | preet_slaylist | 51,000 | 10,337,678 | 64,417.0 | 202.7 | 160.5일 | 9.2분 | 기타 | 플레이리스트·모음 | 설명 | 4,952/5,103 |  |
| V98 | [Tera Sang Yaara - Slowed Reverb ∣∣ Atif Aslam ∣∣ Dopohor Lo…](https://www.youtube.com/watch?v=QcR63bT06iE) | Dopohor Lofi | 3,430 | 2,799,134 | 64,029.3 | 816.1 | 43.7일 | 5분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 219/227 | #44 |
| V99 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 nên nghe gì khi gió Thu tràn về? 🍂📻 Playlist Nhạc …](https://www.youtube.com/watch?v=Pg39V_-aNPY) | chill out | 4,530 | 2,159,722 | 63,677.0 | 476.8 | 33.9일 | 83.5분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 236/269 | #102 |
| V100 | [HAN "back to life" ∣ [Stray Kids : SKZ-PLAYER]](https://www.youtube.com/watch?v=F0UIsSnotlA) | Stray Kids | 25,500,000 | 10,731,451 | 63,614.2 | 0.4 | 168.7일 | 4.3분 | 기타 | 한 곡 | 설명 | 45,159/45,194 |  |
| V101 | [Happy Morning Jazz 🎶 January Bossa Nova Instrumental and Re…](https://www.youtube.com/watch?v=cwBj4t1V_FY) | Little Masti … | 12,500 | 1,561,690 | 62,869.3 | 124.9 | 24.8일 | 14.5분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 0/0 | #405 |
| V102 | [Bedroom R&B After Hours ∣ Obsessive Love Playlist ∣ Dark ro…](https://www.youtube.com/watch?v=WRi5W4B2vgQ) | afterlove. | 8,570 | 1,915,987 | 62,524.7 | 223.6 | 30.6일 | 81.7분 | 11. 힙합·R&B·EDM | 플레이리스트·모음 | 설명 | 177/192 | #261 |
| V103 | [Throwback R&B Classics 📺 Chris Brown, Rihanna, Akon, Usher,…](https://www.youtube.com/watch?v=gCUbxsTWZ18) | R&B Afterglow | 15,500 | 6,177,435 | 62,459.0 | 398.5 | 98.9일 | 193.5분 | 11. 힙합·R&B·EDM | 정보·해설 | 설명 | 698/762 | #135 |
| V104 | [Шадэ, Jony, Мальборо, Zivert, MiyaGi, MOT ∣ ХИТЫ 2026 #всех…](https://www.youtube.com/watch?v=mUll6jirang) | The Nicklaus | 51,000 | 6,080,329 | 61,328.5 | 119.2 | 99.1일 | 65.3분 | 기타 | 음악 | 설명 | 730/731 |  |
| V105 | [Tulus - Teh Hijau ∣∣ [Mix Lirik] - eńau & Ari Lesmana, Bah…](https://www.youtube.com/watch?v=TN-3LJS2itE) | Bintik Musik | 111,000 | 6,493,971 | 61,013.4 | 58.5 | 106.4일 | 19.6분 | 6. 피아노·클래식·연주곡 | 커버·직접 부른 노래 | 설명 | 507/509 |  |
| V106 | [이승철X성시경 - 말리꽃 [더 시즌즈-성시경의 고막남친] ∣ KBS 260710 방송](https://www.youtube.com/watch?v=17zQPXQS6fk) | KBS Kpop | 10,400,000 | 6,434,590 | 60,889.4 | 0.6 | 105.7일 | 4.8분 | 기타 | 음악 | 설명 | 2,777/2,810 |  |
| V107 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Study / Focus …](https://www.youtube.com/watch?v=KU7PfC9i9cE) | Focus Music 2… | 4,270 | 1,506,191 | 60,514.8 | 352.7 | 24.9일 | 13.8분 | 3. 공부·집중·작업 | 음악 | 설명 | 92/92 | #159 |
| V108 | [Relax & Unwind Playlist 🎧 Trending Pop Hits 2026 🌙 Best Aco…](https://www.youtube.com/watch?v=juN2PpuhZk4) | Calm Hits | 55,500 | 5,816,388 | 60,359.5 | 104.8 | 96.4일 | 58.1분 | 기타 | 플레이리스트·모음 | 설명 | 1,089/1,090 |  |
| V109 | [Autumn Fireplace Jazz ∣ Cozy Crackling Fire Ambience](https://www.youtube.com/watch?v=q87NJ-696WM) | Midnight Fika | 4,790 | 2,456,191 | 60,290.8 | 512.8 | 40.7일 | 129.6분 | 2. 자연 소리·백색소음 | 음악 | 설명 | 207/224 | #93 |
| V110 | [A Chatpati Playlist Only For Chatpata People 😋✨ ∣ Ultimate …](https://www.youtube.com/watch?v=wNnngvJeuio) | Clumsyy Cizzy | 55,000 | 2,263,303 | 59,892.9 | 41.1 | 37.8일 | 7.5분 | 기타 | 플레이리스트·모음 | 설명 | 206/208 |  |
| V111 | [Darmiyaan](https://www.youtube.com/watch?v=v2TsWj3wxHM) | Rekha Bhardwa… | 8,590 | 5,651,106 | 58,856.0 | 657.9 | 96.0일 | 4.5분 | 4. 카페·매장·라운지 | 정보·해설 | 설명 | 0/239 | #62 |
| V112 | [Heartbreaking 💔 Lofi Mashup 🎧Slowed + Reverb Songs ∣ Relax,…](https://www.youtube.com/watch?v=gCuJrBYRJpM) | Fiaz Baloch O… | 7,170 | 2,818,580 | 58,452.9 | 393.1 | 48.2일 | 8분 | 3. 공부·집중·작업 | 음악 | 설명 | 154/156 | #139 |
| V113 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 🍁 설레는 바람이 부는 가을이 왔나봐 ∣ 틀어두기 좋은 감성 팝송 모음](https://www.youtube.com/watch?v=jmU_fq-iTSE) | Melly Moood | 6,780 | 2,354,739 | 58,279.7 | 347.3 | 40.4일 | 188.2분 | 10. 팝송·K팝·J팝 | 플레이리스트·모음 | 설명 | 283/294 | #164 |
| V114 | [YOSHIKI – ENDLESS RAIN (From UNDER THE SKY)](https://www.youtube.com/watch?v=LJ5tn3-2YHI) | Yoshiki | 1,330,000 | 1,878,214 | 58,188.8 | 1.4 | 32.3일 | 7.5분 | 기타 | 한 곡 | 설명 | 628/628 |  |
| V115 | [CORTIS (코르티스) ‘ACAI’ Dance Practice (Fix ver.)](https://www.youtube.com/watch?v=ysg6GVlzz9Y) | CORTIS | 7,480,000 | 9,081,324 | 57,908.9 | 1.2 | 156.8일 | 4.8분 | 기타 | 음악 | 설명 | 4,932/4,937 |  |
| V116 | [Perfect South Indian Playlist 🪷🦢 (+timestamps)](https://www.youtube.com/watch?v=ROBjw6FcYxs) | Being Diva 💅🏻 | 6,540 | 2,146,755 | 57,063.8 | 328.2 | 37.6일 | 7.7분 | 기타 | 플레이리스트·모음 | 설명 | 266/291 | #180 |
| V117 | [Jay Park & LNGSHOT - 'MOYA' Official Music Video](https://www.youtube.com/watch?v=2-B4MdfuWkE) | MORE VISION | 344,000 | 8,870,440 | 56,972.9 | 25.8 | 155.7일 | 6.5분 | 기타 | 한 곡 | 설명 | 7,479/7,489 |  |
| V118 | [Baddie playlist 💋✨Aura+99999∣ SanviEditz #songplaylist](https://www.youtube.com/watch?v=p8u1URNm4ao) | ♡𝑺𝒂𝒏𝒗𝒊𝑬𝒅𝒊𝒕𝒛♡ | 5,550 | 2,720,745 | 56,728.9 | 490.2 | 48.0일 | 8.1분 | 기타 | 플레이리스트·모음 | 없음 | 2,195/2,367 | #99 |
| V119 | [Ye Tune Kya Kiya (Slowed + Reverb) 🎧 ∣ Lofi Version ∣ Once …](https://www.youtube.com/watch?v=jqVvhD8Bps4) | Vɪʙᴇ Bʏ Lᴏғɪ | 2,500 | 5,050,913 | 56,720.1 | 2,020.4 | 89.0일 | 4.8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 363/369 | #8 |
| V120 | [Haryanvi playlist that walk up your inner dancer 🔥💋#lifewit…](https://www.youtube.com/watch?v=tYuLhTnHgOQ) | Venus Yadav | 12,500 | 4,725,514 | 56,522.9 | 378.0 | 83.6일 | 11분 | 기타 | 플레이리스트·모음 | 없음 | 570/592 | #143 |
| V121 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=ca4K-2vlfvA) | KKR rahul 09 | 16,500 | 1,669,356 | 55,127.3 | 101.2 | 30.3일 | 18.2분 | 1. 수면·명상·힐링 | 음악 | 설명 | 69/72 | #453 |
| V122 | [Popular OPM Hits 2026 🌿 New Filipino Playlist ∣ Beautiful T…](https://www.youtube.com/watch?v=Ur4FFQT--Qw) | Serenata | 122,000 | 5,607,137 | 54,203.9 | 46.0 | 103.4일 | 70.4분 | 기타 | 플레이리스트·모음 | 설명 | 290/290 |  |
| V123 | [[Playlist] Music is my drug](https://www.youtube.com/watch?v=msoR3EhPNAA) | Hugs | 6,660 | 2,700,334 | 53,319.6 | 405.5 | 50.6일 | 20.9분 | 기타 | 플레이리스트·모음 | 설명 | 538/541 | #132 |
| V124 | [𝟭𝗛 𝗼𝗳 𝟮𝟬𝟮𝟲 𝗣𝗛𝗢𝗡𝗞 / 𝗙𝗨𝗡𝗞 𝗠𝗜𝗫 🔥‼️∣ 𝘓𝘰𝘯𝘶𝘵'𝘴 𝘗𝘭𝘢𝘺𝘭𝘪𝘴𝘵 😼‼️](https://www.youtube.com/watch?v=xAgGIDEsnU0) | 𝐋𝐨𝐧𝐮𝐭 | 562,000 | 3,492,366 | 53,265.4 | 6.2 | 65.6일 | 60분 | 기타 | 플레이리스트·모음 | 설명 | 2,134/2,153 |  |
| V125 | [𝘊𝘦𝘳𝘵𝘪𝘧𝘪𝘦𝘥 𝘋𝘦𝘴𝘪 𝘉𝘢𝘯𝘨𝘦𝘳𝘴 𝘵𝘩𝘢𝘵 𝘴𝘭𝘢𝘱 (+𝘵𝘪𝘮𝘦𝘴𝘵𝘢𝘮𝘱𝘴) 💅🔥](https://www.youtube.com/watch?v=PZcsGXrrBGY) | A BEE Editz | 11,100 | 3,337,481 | 53,161.8 | 300.7 | 62.8일 | 12.9분 | 기타 | 플레이리스트·모음 | 설명 | 363/391 | #203 |
| V126 | [Shri Krishna Govind Hare Murari - Non Stop Krishna Bhajans …](https://www.youtube.com/watch?v=3GOzu5Hjbhw) | Radha Krishna… | 50,800 | 8,421,323 | 52,188.9 | 165.8 | 161.4일 | 29.8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 2,114/2,122 |  |
| V127 | [Không Buông x Từng Là Của Nhau x Tìm Em - HNGLE x BẢO ANH ∣…](https://www.youtube.com/watch?v=wVLhvXB2flE) | Chà Là Chill | 38,900 | 4,959,526 | 51,695.0 | 127.5 | 95.9일 | 91.8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 609/614 | #398 |
| V128 | [झूमका झूलनिया Slowed + Reverb ∣ KhesariLal Yadav ∣ Bhojpuri…](https://www.youtube.com/watch?v=UgjIqEE-Eok) | officialprince | 1,910 | 3,905,222 | 51,591.1 | 2,044.6 | 75.7일 | 4.5분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 327/335 | #7 |
| V129 | [Coffee Shop Love Songs ∣ Relaxing Acoustic 70s 80s 90s Coll…](https://www.youtube.com/watch?v=p4zynVVTYpA) | Acoustic Memo… | 10,000 | 1,503,013 | 51,243.0 | 150.3 | 29.3일 | 80.3분 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 130/141 | #342 |
| V130 | [Top Hits Indonesia 2026 ∣ Top Hits Spotify Indonesia 2026 ∣…](https://www.youtube.com/watch?v=ANPUoFuWpEo) | ShadowBrief | 9,790 | 8,319,423 | 50,600.1 | 849.8 | 164.4일 | 65분 | 기타 | 정보·해설 | 설명 | 998/1,004 | #41 |
| V131 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=29EWidvY0b8) | AR BROTHER | 7,450 | 2,412,805 | 50,236.7 | 323.9 | 48.0일 | 18.6분 | 1. 수면·명상·힐링 | 음악 | 설명 | 87/95 | #185 |
| V132 | [90’S Old Hindi Songs🥰 90s Love Song💘 Udit Narayan, Alka Yag…](https://www.youtube.com/watch?v=ImUEhW6KTnM) | Flashback Bea… | 119,000 | 7,254,870 | 49,645.6 | 61.0 | 146.1일 | 26.3분 | 기타 | 음악 | 설명 | 404/412 |  |
| V133 | [[playlist] 일하다 어깨 들썩이는 케이팝 노동요 ∣∣ 4K MV](https://www.youtube.com/watch?v=whggKiGBSx4) | 노래듣는 고영희 | 2,530 | 3,967,128 | 49,487.9 | 1,568.0 | 80.2일 | 148.4분 | 3. 공부·집중·작업 | 플레이리스트·모음 | 설명 | 193/199 | #13 |
| V134 | [मोहे नंदी बनइय्यो भोले ∣ Mohe Nandi Banaiyo Bhole Apne Kail…](https://www.youtube.com/watch?v=2Dm4aMBCG1s) | Bajao Bhakti | 649,000 | 8,855,331 | 48,837.9 | 13.6 | 181.3일 | 5.7분 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,788/1,788 |  |
| V135 | [🎧 Le Main Saiyaan Aa Gayi (Lofi) ∣ Mohabbatein ∣ Shah Rukh …](https://www.youtube.com/watch?v=iOdAwvF0kmk) | lofi.slowed_02 | 5,670 | 4,633,361 | 47,724.5 | 817.2 | 97.1일 | 7.5분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 291/296 | #43 |
| V136 | [ASTAGA BERCANDA- Akbar Chalay, Mingse ∣ MMG My Mine Gueh ∣ …](https://www.youtube.com/watch?v=2VS7QHm4MgA) | INDO POPULER … | 244,000 | 4,809,784 | 47,557.6 | 19.7 | 101.1일 | 40.5분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 741/741 |  |
| V137 | [(NO MID-ROLL ADS) Cozy Rainy & Spooky Halloween 🍂 Fall Jazz…](https://www.youtube.com/watch?v=p1b2tWu4XkE) | Relaxing Chri… | 4,360 | 939,874 | 47,330.3 | 215.6 | 19.9일 | 249.2분 | 7. 재즈·보사노바 | 음악 | 설명 | 383/449 | #273 |
| V138 | [Kalyani [slowed & Reverb] ∣∣ With Shreya Ghoshal ∣∣Arjn / K…](https://www.youtube.com/watch?v=rbt6SjoZlWU) | TRL Lofi | 3,880 | 4,815,089 | 47,282.7 | 1,241.0 | 101.8일 | 4.4분 | 기타 | 음악 | 설명 | 156/158 | #23 |
| V139 | [Barsaat 🌧️ ∣ All Trending Songs 🎧∣ Taare x Samjho Na x Safa…](https://www.youtube.com/watch?v=xGPm2j1dDr4) | LOFI XP VIBES | 2,900 | 1,990,035 | 46,582.9 | 686.2 | 42.7일 | 23분 | 기타 | 음악 | 설명 | 193/207 | #56 |
| V140 | [Tum Ho Toh - Mashup 2026 ∣ Romantic Love Song ∣ Bollywood S…](https://www.youtube.com/watch?v=EmsrY9EQSSE) | VS Lofi Offic… | 2,230 | 2,754,032 | 46,474.7 | 1,235.0 | 59.3일 | 5.2분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 43/45 | #24 |
| V141 | [Michael Jackson Greatest Hits Mix ∣ Celebrating MICHAEL (20…](https://www.youtube.com/watch?v=F2-83E_iNb4) | IONEMusic | 11,100 | 4,869,963 | 46,122.7 | 438.7 | 105.6일 | 94.5분 | 기타 | 음악 | 설명 | 1,177/1,203 | #118 |
| V142 | [Romantic Saxophone Jazz 2026 ✨ Smooth Chill Lounge Music fo…](https://www.youtube.com/watch?v=tntu_zHVCdI) | Paris Melody … | 73,400 | 7,275,637 | 46,015.7 | 99.1 | 158.1일 | 190.9분 | 4. 카페·매장·라운지 | 플레이리스트·모음 | 설명 | 1,137/1,139 |  |
| V143 | [Deep Sleep & Chill Lofi : Bhojpuri Slowed & Reverb Songs 🎧✨…](https://www.youtube.com/watch?v=zW8T1B9Fzd0) | VLOGDIPESH | 5,220 | 732,679 | 45,356.6 | 140.4 | 16.2일 | 17.1분 | 1. 수면·명상·힐링 | 음악 | 설명 | 33/33 | #364 |
| V144 | [Rest Your Mind ∣ Your Brain Needs Silence ∣ Dopamine Reset …](https://www.youtube.com/watch?v=UWZ_QQNKmes) | Essential Ind… | 19,400 | 5,349,642 | 44,943.1 | 275.8 | 119.0일 | 20.7분 | 1. 수면·명상·힐링 | 음악 | 설명 | 833/854 | #217 |
| V145 | [MIMIFY - I Waited too Long (Original Mix)](https://www.youtube.com/watch?v=F2Iga1V4cqo) | MIMIFY | 18,500 | 4,657,825 | 44,850.2 | 251.8 | 103.9일 | 7.8분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 675/677 | #241 |
| V146 | [MGA MATATANG MAPANGHUSGA NONSTOP HITS VOL.1 ∣ Best OPM Regg…](https://www.youtube.com/watch?v=IbxIsoqu6s8) | VincH Music | 55,600 | 5,374,008 | 44,696.8 | 96.7 | 120.2일 | 83.2분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 1,713/1,718 |  |
| V147 | [Narak - Lyrical ∣ Ishqnama ∣ Jai Randhhawa ∣ Shehnaaz Gill …](https://www.youtube.com/watch?v=VR881KWobuk) | Tips Punjabi | 5,180,000 | 2,223,282 | 44,630.4 | 0.4 | 49.8일 | 4.5분 | 기타 | 한 곡 | 설명 | 111/111 |  |
| V148 | [CrushX성시경 - 행복한 나를 [더 시즌즈-성시경의 고막남친] ∣ KBS 260717 방송](https://www.youtube.com/watch?v=KZwBjyQOuGQ) | KBS Kpop | 10,400,000 | 4,394,125 | 44,528.5 | 0.4 | 98.7일 | 4.7분 | 기타 | 음악 | 설명 | 1,024/1,035 |  |
| V149 | [Best Morning Powerful Mantras ∣ Hanuman, Ganesh, Shiva, Gay…](https://www.youtube.com/watch?v=HwIWdqpsKF8) | Bhakti Beena | 105,000 | 8,037,438 | 44,339.9 | 76.5 | 181.3일 | 12분 | 1. 수면·명상·힐링 | 음악 | 설명 | 3,004/3,004 |  |
| V150 | [Tere Bin [Slowed+Reverb] - Rahat Fateh Ali Khan, Asees Kaur…](https://www.youtube.com/watch?v=voemJVo9Lrc) | Manan mp3 | 779,000 | 6,673,044 | 43,833.4 | 8.6 | 152.2일 | 4.2분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 747/747 |  |
| V151 | [Just One More Drink -- Jazz Noir](https://www.youtube.com/watch?v=7gtIh5dF9Xk) | Tom’s Jazz Lo… | 72,600 | 6,555,029 | 43,532.8 | 90.3 | 150.6일 | 81.8분 | 7. 재즈·보사노바 | 음악 | 설명 | 1,538/1,543 |  |
| V152 | [Peaceful Chill Playlist 🌙 Trending English Songs 2026 🎧 Bes…](https://www.youtube.com/watch?v=td6iCrK4MHc) | Morning Seren… | 17,400 | 1,358,464 | 43,315.5 | 78.1 | 31.4일 | 70.7분 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 137/150 | #522 |
| V153 | [THE WEEKND ∣ Late Night Drive Playlist](https://www.youtube.com/watch?v=DgBM12cGM-Q) | Jostynsc | 11,100 | 5,348,191 | 43,028.0 | 481.8 | 124.3일 | 40.8분 | 5. 운동·드라이브·신나는 | 플레이리스트·모음 | 설명 | 304/338 | #100 |
| V154 | ["Quiet October Morning" Beautiful Relaxing Music, Peaceful …](https://www.youtube.com/watch?v=7CtUqbXKYEc) | Tim Janis | 2,170,000 | 616,012 | 43,016.1 | 0.3 | 14.3일 | 9.1분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 109/109 |  |
| V155 | [Pov: certified Baddie playlist 🔥# playlist # baddie](https://www.youtube.com/watch?v=vzNOiBV_W6g) | it's GAURAV P… | 7,970 | 5,448,963 | 42,185.7 | 683.7 | 129.2일 | 8.3분 | 기타 | 플레이리스트·모음 | 설명 | 696/706 | #58 |
| V156 | [ORANGE x HOÀNG DŨNG - “CỨ THẾ” ∣ OFFICIAL MV (From album 'D…](https://www.youtube.com/watch?v=BVwmm3dno2A) | Orange Singer… | 502,000 | 1,820,662 | 41,587.6 | 3.6 | 43.8일 | 4분 | 12. 커버·노래 부르기 | 커버·직접 부른 노래 | 설명 | 947/947 |  |
| V157 | [YARA YARA YA PHONK [All Versions] ∣∣ {NORMAL, SLOWED, SUPER…](https://www.youtube.com/watch?v=yMo3VnIH-TU) | Funk7Xqueen | 64,600 | 5,528,533 | 41,038.5 | 85.6 | 134.7일 | 8.3분 | 기타 | 긴 한 곡·반복 | 설명 | 2,234/2,243 |  |
| V158 | [Steve Lacy - the feeling (Official Video)](https://www.youtube.com/watch?v=Qw20tg1v7Fc) | SteveLacyVEVO | 8,430 | 5,786,837 | 40,996.6 | 686.5 | 141.2일 | 4.6분 | 기타 | 플레이리스트·모음 | 설명 | 5,393/5,417 | #55 |
| V159 | [MEGA BASS 🔊🔥 EXTREME NONSTOP EDM REMIX 💯 MONSTER DROP ⚠️ CL…](https://www.youtube.com/watch?v=Kc071SEvHgc) | Street Bass C… | 27,400 | 6,169,917 | 40,773.8 | 225.2 | 151.3일 | 42.7분 | 5. 운동·드라이브·신나는 | 음악 | 설명 | 1,383/1,400 | #258 |
| V160 | [POV You're back in the 90s 💗📻 ∣ Old hindi songs ∣ Bollywood…](https://www.youtube.com/watch?v=4GMIMevMn6Y) | Manii | 2,800 | 2,465,223 | 40,708.2 | 880.4 | 60.6일 | 8.2분 | 기타 | 음악 | 설명 | 803/877 | #39 |
| V161 | [Sad lo_fi🥺💔2026 ultimate](https://www.youtube.com/watch?v=q-iefUnWPCY) | mr prakash 😊 | 5,510 | 1,735,087 | 40,612.8 | 314.9 | 42.7일 | 18.6분 | 기타 | 음악 | 설명 | 143/151 | #190 |
| V162 | [Heartbreaking Lofi Mashup 💔 (Slowed + Reverb) ∣ Study, Focu…](https://www.youtube.com/watch?v=6mgb7GxwLvA) | stylish offic… | 12,200 | 2,919,539 | 40,423.4 | 239.3 | 72.2일 | 7.8분 | 3. 공부·집중·작업 | 음악 | 설명 | 132/135 | #250 |
| V163 | [Jo Tere Sang KaTi RaTe 💔 Lofi Remix ∣ Emotional Slowed + Re…](https://www.youtube.com/watch?v=XKcT9t0tgbY) | Abidpro | 46,100 | 6,368,010 | 40,349.7 | 138.1 | 157.8일 | 6.3분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 809/811 | #367 |
| V164 | [katseye (clean) playlist ⊹ ࣪ ˖](https://www.youtube.com/watch?v=_VEtnBXtUNs) | 𝟑𝟎𝟑.𝐧𝐞𝐰.𝐞𝐫𝐚 | 7,800 | 3,382,569 | 40,177.2 | 433.7 | 84.2일 | 25.3분 | 기타 | 플레이리스트·모음 | 설명 | 2,599/2,611 | #121 |
| V165 | [Best Morning Powerful Mantras ∣ Shiva, Ganesh, Hanuman, Vis…](https://www.youtube.com/watch?v=CFV27iuas7Q) | Sacred Naad | 22,300 | 2,856,394 | 40,073.4 | 128.1 | 71.3일 | 15.7분 | 1. 수면·명상·힐링 | 음악 | 설명 | 973/1,034 | #395 |
| V166 | [🎶Spotify Hits Music 2026 ∣∣ Top Music Playlist -- Best 100 …](https://www.youtube.com/watch?v=0gvy7v6GTMo) | Soft Feelings | 6,250 | 2,831,710 | 39,397.0 | 453.1 | 71.9일 | 138.6분 | 기타 | 플레이리스트·모음 | 설명 | 188/197 | #110 |
| V167 | [Mood Lifter Playlist (Visualizer) ∣ Feel Good Songs ∣ Natur…](https://www.youtube.com/watch?v=Rg3YlUwSkUc) | Sony Music In… | 73,400,000 | 3,391,836 | 39,057.9 | 0.1 | 86.8일 | 65.6분 | 기타 | 플레이리스트·모음 | 설명 | 159/160 |  |
| V168 | [여인 – 우리 가슴속 깊이 박혀 있던 그 노래, 듣는 순간 그 시절로 돌아갑니다, 이어폰 필수… 👉 첫 소…](https://www.youtube.com/watch?v=a0iBRRoDnDw) | 명곡부활단 | 107,000 | 6,778,194 | 38,972.0 | 63.4 | 173.9일 | 5.1분 | 5. 운동·드라이브·신나는 | AI 음악 | 설명 | 1,812/1,847 |  |
| V169 | [uMoya 2.0 (Tycoon Remix)](https://www.youtube.com/watch?v=HropgeYirpE) | Darque - Topic | 1,330 | 1,697,005 | 38,654.3 | 1,275.9 | 43.9일 | 8.7분 | 기타 | 음악 | 설명 | 0/378 | #22 |
| V170 | [Heartbroken Lofi Songs 💔 ∣ Slowed + Reverb ∣ Late Night Chi…](https://www.youtube.com/watch?v=ki362-gbdjs) | Qais Music St… | 2,170 | 922,906 | 38,650.9 | 425.3 | 23.9일 | 7.3분 | 3. 공부·집중·작업 | 음악 | 설명 | 10/10 | #126 |
| V171 | [SAD LO-FI 🥺 💔 2026 Ultimate Mind Relaxing Lofi Beats ∣ Stud…](https://www.youtube.com/watch?v=XLtdtHJExEY) | Clsxzff | 1,860 | 1,246,823 | 37,967.5 | 670.3 | 32.8일 | 19.6분 | 1. 수면·명상·힐링 | 음악 | 설명 | 173/187 | #61 |
| V172 | [f(x) 에프엑스 - Hot Summer (트로트 버전) [MV]](https://www.youtube.com/watch?v=ldfmc4lnwoY) | ERRDAY DRIP (… | 236,000 | 3,407,690 | 37,347.5 | 14.4 | 91.2일 | 4.2분 | 9. 가요·발라드·트로트 | 한 곡 | 설명 | 2,948/2,969 |  |
| V173 | [12 HOURS⚡TOP MOST VIRAL PHONK/FUNK 2026 SONGS 🎵 PLAYLIST 🎵](https://www.youtube.com/watch?v=5GG_MkQYQq0) | Vaddy Daddy | 83,700 | 3,364,288 | 36,639.7 | 40.2 | 91.8일 | 719.5분 | 기타 | 플레이리스트·모음 | 설명 | 788/803 |  |
| V174 | [The Best Field Day Songs: 3 Dances + Bonus Soccer Song Incl…](https://www.youtube.com/watch?v=SSWSQKYCE0A) | Oliver’s Melo… | 276,000 | 5,237,098 | 36,546.5 | 19.0 | 143.3일 | 9.3분 | 기타 | 음악 | 설명 | 0/0 |  |
| V175 | [𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐅𝐨𝐫 𝐘𝐨𝐮 𝐓𝐨 𝐂𝐫𝐞𝐚𝐭𝐞 𝐅𝐚𝐤𝐞 𝐒𝐜𝐞𝐧𝐚𝐫𝐢𝐨𝐬 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐌𝐢𝐧𝐝 🤍 ∣ …](https://www.youtube.com/watch?v=flQgOwg4jLI) | Ashik's Cloud… | 15,800 | 3,869,010 | 36,545.0 | 244.9 | 105.9일 | 15.2분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 965/983 | #246 |
| V176 | [New OPM Trending 2026 🎧 Tagalog Love Songs With Lyrics ∣ So…](https://www.youtube.com/watch?v=7NQYmIycWj4) | Serenata | 122,000 | 6,423,824 | 35,998.9 | 52.6 | 178.4일 | 54분 | 기타 | 플레이리스트·모음 | 설명 | 376/376 |  |
| V177 | [a playlist to make your brain shut up](https://www.youtube.com/watch?v=xIX_A2PRoW0) | HIGHWIND | 40,200 | 2,436,856 | 35,875.8 | 60.6 | 67.9일 | 62.1분 | 1. 수면·명상·힐링 | 연주 | 설명 | 811/848 | #601 |
| V178 | [Tìm Em](https://www.youtube.com/watch?v=PnGk00MuNM4) | Hngle - Topic | 1,350 | 4,582,506 | 35,862.8 | 3,394.4 | 127.8일 | 4.6분 | 기타 | 음악 | 설명 | 0/227 | #4 |
| V179 | [KUMAMICHI（熊道） — Japanese Zen Music Along the Bear’s Path](https://www.youtube.com/watch?v=vFJuk4U-V7Q) | Aether Journey | 34,200 | 2,007,149 | 35,195.2 | 58.7 | 57.0일 | 347분 | 1. 수면·명상·힐링 | 음악 | 설명 | 235/253 | #610 |
| V180 | [Morning Cortisol Detox 🌱 ∣ Raag Bhairavi Bansuri 432Hz for …](https://www.youtube.com/watch?v=iYO8SH-maAc) | Dhun Detox | 57,600 | 4,127,074 | 34,588.1 | 71.7 | 119.3일 | 19.1분 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,600/2,616 |  |
| V181 | [Viral Pop Songs Cover 2026 🎙 Top Music Playlist Hits](https://www.youtube.com/watch?v=JKRRl5-5-hw) | Acoustic Ther… | 21,300 | 5,148,621 | 34,243.8 | 241.7 | 150.4일 | 57.4분 | 10. 팝송·K팝·J팝 | 커버·직접 부른 노래 | 설명 | 512/521 | #247 |
| V182 | [धनियां बनबू कनियाँ - Lofi Song ∣∣ Khesari Lal Yadav ∣∣ Dilw…](https://www.youtube.com/watch?v=s-1MerBYomA) | ꧁༒乙x°᭄Ᏼᴀʙᴜ࿐ | 3,840 | 2,029,933 | 34,232.0 | 528.6 | 59.3일 | 5.1분 | 8. 로파이·시티팝·칠 | 음악 | 없음 | 267/296 | #85 |
| V183 | [POV: you discovered that ✨South Indian and Hindi ✨songs hit…](https://www.youtube.com/watch?v=lbT4VY3UKkY) | Arena | 3,950 | 2,372,915 | 33,970.7 | 600.7 | 69.9일 | 14.6분 | 12. 커버·노래 부르기 | 음악 | 설명 | 406/438 | #73 |
| V184 | [Kalyani Remix (Lyrics) - ARJN, KDS, FIFTY4, RONN & Shreya G…](https://www.youtube.com/watch?v=zoVYtZpo6oA) | D-Muze India | 188,000 | 3,381,451 | 33,875.2 | 18.0 | 99.8일 | 4.5분 | 8. 로파이·시티팝·칠 | 한 곡 | 설명 | 652/652 |  |
| V185 | [🎀Students fav playlist👀 ∣next comment∣](https://www.youtube.com/watch?v=yx9rhLzbY0A) | @vibe_withe_me | 5,660 | 2,556,375 | 33,692.5 | 451.7 | 75.9일 | 7분 | 기타 | 플레이리스트·모음 | 없음 | 1,169/1,207 | #111 |
| V186 | [Patar Bashori 🥀 ∣ পাতার বাঁশরী ∣ Female Version ∣ Bangla No…](https://www.youtube.com/watch?v=kQ3IwNRzLMM) | Lofix Dj Fusi… | 31,100 | 2,843,418 | 33,473.5 | 91.4 | 84.9일 | 18.4분 | 8. 로파이·시티팝·칠 | 커버·직접 부른 노래 | 설명 | 976/1,006 | #477 |
| V187 | [Cortisol Reset । 432Hz Krishna Bansuri Therapy for a Calm M…](https://www.youtube.com/watch?v=D5NHvEVAbWY) | Healing Raga … | 24,500 | 3,206,842 | 33,110.8 | 130.9 | 96.9일 | 65.7분 | 1. 수면·명상·힐링 | 음악 | 설명 | 1,970/2,039 | #392 |
| V188 | [Sarap Sa Tenga To VOL. 3 🌿(IBA TO!) ∣ Spiritual Roots Regga…](https://www.youtube.com/watch?v=9w_QNH2ju3A) | Just Reggae S… | 46,000 | 5,451,886 | 32,853.5 | 118.5 | 165.9일 | 64.6분 | 1. 수면·명상·힐링 | 음악 | 설명 | 2,674/2,673 | #414 |
| V189 | [Peek A Boo - Toxic ∣ Rocking Star Yash, Kiara Advani, Nayan…](https://www.youtube.com/watch?v=XGnxAIcb2pY) | Zee Music Com… | 123,000,000 | 1,925,543 | 32,755.6 | 0.0 | 58.8일 | 4.4분 | 기타 | 음악 | 설명 | 874/874 |  |
| V190 | [Om Namah Shivaya 🕉 #hanumanansh #backgroundmusic #trendings…](https://www.youtube.com/watch?v=YnhFtBGO2zI) | Rudree Aarya … | 2,500 | 1,554,595 | 32,704.3 | 621.8 | 47.5일 | 15.5분 | 기타 | 음악 | 없음 | 385/387 | #68 |
| V191 | [the playlist to actually enter flowstate.](https://www.youtube.com/watch?v=wdDhTr_M7kA) | Pure Grit Stu… | 20,700 | 1,810,765 | 32,633.9 | 87.5 | 55.5일 | 123분 | 기타 | 플레이리스트·모음 | 설명 | 545/553 | #490 |
| V192 | [𝙋𝙤𝙫 :- 𝘽𝙝𝙤𝙟𝙥𝙪𝙧𝙞 𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩 ∣∣ 𝙘𝙝𝙞𝙡𝙡 𝙜𝙪𝙮𝙨 𝙖𝙣𝙙 𝙚𝙣𝙟𝙤𝙮 ∣∣ 𝙂𝘼𝙇𝘼𝙓𝘼𝙔…](https://www.youtube.com/watch?v=areWocW1pXI) | AYUSH | 4,310 | 1,485,637 | 31,681.5 | 344.7 | 46.9일 | 8분 | 기타 | 플레이리스트·모음 | 설명 | 180/188 | #166 |
| V193 | [Best pakistani OST for you ✨🤍 ∣ Pakistani songs∣ #playlist …](https://www.youtube.com/watch?v=-VoKBfZJR5U) | shaaedits31 | 10,900 | 5,811,434 | 31,469.3 | 533.2 | 184.7일 | 17.7분 | 기타 | 플레이리스트·모음 | 설명 | 926/932 |  |
| V194 | [99% Fall Into Sleep Instantly (No Ads) • Eliminate Stress &…](https://www.youtube.com/watch?v=iVZPLhAlXUw) | Bedtime Calm … | 12,600 | 1,659,599 | 30,955.5 | 131.7 | 53.6일 | 237.9분 | 1. 수면·명상·힐링 | 음악 | 설명 | 43/43 | #389 |
| V195 | [MUSIK SANTAI VIRAL 2026 🎧 Lagu Pop Indonesia Akustik Terbai…](https://www.youtube.com/watch?v=bZEwYquV6Kg) | Akustik Cantik | 10,500 | 3,012,978 | 30,670.4 | 286.9 | 98.2일 | 78.5분 | 기타 | 정보·해설 | 설명 | 182/209 | #211 |
| V196 | [ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ](https://www.youtube.com/watch?v=MsjHOAq7WH0) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 14,700 | 1,613,381 | 30,520.4 | 109.8 | 52.9일 | 67.7분 | 6. 피아노·클래식·연주곡 | 음악 | 설명 | 1,119/1,122 | #438 |
| V197 | ["Comfort song's - All in one playlist"😭✨🌷//part-4//edit by …](https://www.youtube.com/watch?v=617yn663oeA) | Anushri | 7,570 | 2,319,077 | 30,452.0 | 306.4 | 76.2일 | 7.6분 | 기타 | 플레이리스트·모음 | 설명 | 293/308 | #200 |
| V198 | [Cheema Y Best Songs Playlist ∣ Punjabi Hits 2026 ∣ Jukebox …](https://www.youtube.com/watch?v=LFpVqIlmn00) | Radio Level L… | 38,600 | 3,562,281 | 30,440.2 | 92.3 | 117.0일 | 27.9분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 1,003/1,063 | #469 |
| V199 | [Barsaat ∣ All Trending Hindi Songs 2026 ∣ Safar × Bairan × …](https://www.youtube.com/watch?v=-hXkiB-eLfs) | SukumusicHindi | 3,390 | 1,329,356 | 30,385.4 | 392.1 | 43.7일 | 22.9분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 161/165 | #140 |
| V200 | [Heartbreaking💔 mashup lofi Songs ∣ Slowed + Reverb ∣ Late N…](https://www.youtube.com/watch?v=z3H-p4r9EC4) | Soulmate Song… | 7,940 | 1,766,877 | 30,350.8 | 222.5 | 58.2일 | 8분 | 3. 공부·집중·작업 | 음악 | 설명 | 139/145 | #262 |
| V201 | [POV: You Own The Dance Floor💃🏻🪩✨ ∣∣Song Playlist+ Timestamp…](https://www.youtube.com/watch?v=HRGB0HnXdOs) | Author_Shreyuu | 6,480 | 4,600,213 | 30,238.1 | 709.9 | 152.1일 | 8분 | 기타 | 플레이리스트·모음 | 설명 | 617/625 | #52 |
| V202 | [Asiwafuni](https://www.youtube.com/watch?v=9c1b0JLxKG4) | Benzoo - Topic | 11,900 | 2,580,206 | 30,035.9 | 216.8 | 85.9일 | 6.7분 | 기타 | 음악 | 설명 | 0/1,373 | #270 |
| V203 | [[ 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ] 적당히 신나는 그루브 힙합 플레이리스트 ∣ Chill R&B • Cafe Music](https://www.youtube.com/watch?v=p3tvSF3BgYM) | SSoundW | 4,020 | 1,914,311 | 30,010.2 | 476.2 | 63.8일 | 89.9분 | 8. 로파이·시티팝·칠 | 플레이리스트·모음 | 설명 | 253/253 | #103 |
| V204 | [TOP 100 MOST VIRAL PHONK/FUNK 2026 SONGS 🎵 PLAYLIST 🎵](https://www.youtube.com/watch?v=XSEyhGFc8rA) | TOKYO GOD | 136,000 | 4,009,708 | 29,972.7 | 29.5 | 133.8일 | 168.1분 | 기타 | 플레이리스트·모음 | 설명 | 1,359/1,359 |  |
| V205 | [LEO ROJAS - Top 16 Andean Pan Flute Melodies ★ Full Album -…](https://www.youtube.com/watch?v=wR5yxMCTZA0) | Andean Flute … | 4,840 | 1,639,020 | 29,878.9 | 338.6 | 54.9일 | 98.3분 | 6. 피아노·클래식·연주곡 | 플레이리스트·모음 | 설명 | 233/240 | #171 |
| V206 | [SONGS THAT’LL MAKE YOU DANCE AT 3AM ✨🔥 FT. DESI SONGS ❤️‍🔥💋…](https://www.youtube.com/watch?v=oIXkjb_FPC4) | Dramanique⋆.𐙚… | 32,400 | 4,861,681 | 29,849.7 | 150.1 | 162.9일 | 29.3분 | 기타 | 음악 | 설명 | 746/752 | #343 |
| V207 | [늙크크의 가을 플레이리스트🍂](https://www.youtube.com/watch?v=-y-j-uwrLDg) | 빵또A | 232,000 | 1,273,232 | 29,829.0 | 5.5 | 42.7일 | 74.1분 | 기타 | 플레이리스트·모음 | 설명 | 394/394 |  |
| V208 | [Night Mood 🌙 Chill R&B Mix ∣ Late Night Vibes, Relaxing Sou…](https://www.youtube.com/watch?v=i8W-LdXKT6s) | Relaxing Chil… | 25,700 | 5,523,393 | 29,506.0 | 214.9 | 187.2일 | 125.8분 | 1. 수면·명상·힐링 | 플레이리스트·모음 | 설명 | 577/595 |  |
| V209 | [조선힙합 '그냥 해' Official MV](https://www.youtube.com/watch?v=5hL7uPsISY0) | 조선힙합 | 278,000 | 3,830,609 | 29,480.9 | 13.8 | 129.9일 | 4분 | 11. 힙합·R&B·EDM | 한 곡 | 설명 | 1,950/1,967 |  |
| V210 | [Emraan hashmi playlist #emraanhashmi](https://www.youtube.com/watch?v=zZzA1Hp30uE) | july_luna | 5,480 | 1,847,082 | 29,020.7 | 337.1 | 63.6일 | 7.2분 | 기타 | 플레이리스트·모음 | 없음 | 22/31 | #173 |
| V211 | [💖 मेरा चाँद मुझे आया नजर ∣ New Hindi Song 2026 ∣ Romantic S…](https://www.youtube.com/watch?v=FxNQw0BRhWg) | Feel The Music | 3,320 | 1,082,775 | 28,649.6 | 326.1 | 37.8일 | 16.1분 | 기타 | 음악 | 설명 | 65/69 | #182 |
| V212 | [Mere Mehboob Qayamat Hogi ✨ ∣ Slowed Reverb + LoFi ∣ Sad Hi…](https://www.youtube.com/watch?v=AHo0xW8RYTQ) | Abidpro | 46,100 | 4,481,863 | 28,603.3 | 97.2 | 156.7일 | 9.4분 | 8. 로파이·시티팝·칠 | 음악 | 설명 | 350/350 | #459 |
| V213 | [[히트곡 미션] 성리 - 오늘 이 밤｜무명전설 11회](https://www.youtube.com/watch?v=e229ghL4akE) | MBN MUSIC | 2,360,000 | 4,843,432 | 28,375.8 | 2.0 | 170.7일 | 4.2분 | 기타 | 음악 | 설명 | 33,763/34,075 |  |
| V214 | [Sad Song Playlist (+ with timestamps) !!](https://www.youtube.com/watch?v=q48Y5Hf83Bk) | Mood Tapes 🎶 | 18,500 | 3,874,572 | 28,349.3 | 209.4 | 136.7일 | 14.7분 | 기타 | 플레이리스트·모음 | 설명 | 1,520/1,577 | #277 |

### 1-3-1. 자료를 받지 않은 하루 조회수 상위 후보 (64개 중 하루 조회수 큰 30개 — 승인하면 이 묶음에 들어감)

| 제목 | 채널 | 구독자 | 조회수 | 하루 조회수 | 길이 | 업로드 | 주제 묶음 |
|---|---|---|---|---|---|---|---|
| [Every Diwali Ever Ft. @NOTYOURTYPE #BGMI](https://www.youtube.com/watch?v=CiMwEmCqpfc) | BATTLEGROUNDS… | 5,530,000 | 6,328,582 | 532,486.0 | 5.1분 | 2026-10-12 | 기타 |
| [Hey Dukh Bhanjan ∣ Powerful Hanuman Bhajan ∣ मन को शांति दे…](https://www.youtube.com/watch?v=V9jCPRF7_IE) | NMF BHAKTI | 109,000 | 140,595,046 | 430,625.9 | 5.7분 | 2025-12-01 | 기타 |
| [I Went On 100 Dates In 24 Hours! (KPop Demon Hunters)](https://www.youtube.com/watch?v=fYVC8_0v7x0) | Topper Guild | 95,600,000 | 26,877,689 | 274,764.9 | 34.1분 | 2026-07-18 | 10. 팝송·K팝·J팝 |
| [[우리들의 발라드] 김소연🎵사랑 그 쓸쓸함에 대하여_양희은｜261005 1회](https://www.youtube.com/watch?v=C2AhBIE9_f8) | 스브스 예능맛집 | 2,780,000 | 3,806,187 | 203,747.5 | 5.9분 | 2026-10-05 | 9. 가요·발라드·트로트 |
| [The most INSANE Street Performance you will ever see!! (wit…](https://www.youtube.com/watch?v=OhbbPxCtyxc) | Julien Cohen | 8,180,000 | 9,082,187 | 181,827.7 | 19분 | 2026-09-04 | 기타 |
| [우발라 최초 만점 득표?! 모두의 마음을 움직인 15세 소녀의 파워보컬🎤🫢 #우리들의발라드](https://www.youtube.com/watch?v=PWK1Y2hExVI) | 스브스 예능맛집 | 2,780,000 | 1,862,311 | 170,140.3 | 41.3분 | 2026-10-13 | 9. 가요·발라드·트로트 |
| [[우리들의 발라드] 박예승🎵나를 외치다_마야｜261012 2회](https://www.youtube.com/watch?v=YBzP2x3wM78) | 스브스 예능맛집 | 2,780,000 | 1,966,723 | 168,272.5 | 4.3분 | 2026-10-12 | 9. 가요·발라드·트로트 |
| [ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ…](https://www.youtube.com/watch?v=l-vSSYEuO88) | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ… | 127,000 | 9,736,735 | 132,872.5 | 145.1분 | 2026-08-12 | 6. 피아노·클래식·연주곡 |
| [KPop Demon Hunters Go On 100 Dates!](https://www.youtube.com/watch?v=aJEVpCn_imY) | Topper Guild | 95,600,000 | 21,809,962 | 130,044.4 | 24.4분 | 2026-05-09 | 10. 팝송·K팝·J팝 |
| [KAYBEDEN TAKIMI DELİRTEN EKİP! ∣ GTA5: PLAYLIST ∣](https://www.youtube.com/watch?v=D_DQEUGdtNY) | Elraenn | 3,900,000 | 2,130,912 | 127,993.0 | 163.9분 | 2026-10-07 | 기타 |
| [I Faked My Death To Hide From KPop Demon Hunters!](https://www.youtube.com/watch?v=dubaKZmtnlE) | Topper Guild | 95,600,000 | 14,205,344 | 127,036.7 | 32분 | 2026-07-04 | 10. 팝송·K팝·J팝 |
| [I Married EVIL Rumi! (KPop Demon Hunters)](https://www.youtube.com/watch?v=KIb2oE4Xtig) | Topper Guild | 95,600,000 | 10,734,614 | 118,195.9 | 27.4분 | 2026-07-25 | 10. 팝송·K팝·J팝 |
| [I Became a DEMON In Squid Game! (KPop Demon Hunters)](https://www.youtube.com/watch?v=TK-CHHQVH3o) | Topper Guild | 95,600,000 | 12,566,147 | 94,609.9 | 33.5분 | 2026-06-13 | 10. 팝송·K팝·J팝 |
| [This 2 year old SINGER shocked EVERYONE 🥹❤️](https://www.youtube.com/watch?v=W6exbBZNmPE) | Emilio Piano | 9,170,000 | 14,176,324 | 94,193.7 | 4.7분 | 2026-05-26 | 6. 피아노·클래식·연주곡 |
| [Last To Leave Elevator Wins $1,000! (KPop Demon Hunters)](https://www.youtube.com/watch?v=QsUJjZ09vE0) | Topper Guild | 95,600,000 | 15,060,708 | 92,498.9 | 22.4분 | 2026-05-14 | 10. 팝송·K팝·J팝 |
| ["노래 모르는 아가씨" 심수봉 저격에 펑펑 운 김다현, 하루 만에 "실언" 사과 [더펀치]](https://www.youtube.com/watch?v=DBlQIA3nJos) | MBN News | 2,600,000 | 3,023,403 | 92,052.2 | 13분 | 2026-09-21 | 기타 |
| [Anirudh plays his favorite superstar Rajinikanth songs ∣ Ja…](https://www.youtube.com/watch?v=8w72RL2Rnps) | Sun TV | 33,000,000 | 1,036,605 | 87,773.5 | 7.3분 | 2026-10-12 | 기타 |
| [“선배님과 이 노래를 하다니🥹” 성발라가 극찬한 '최고의 보컬' 박재정 #헤어지자말해요 #아니면서 #성시경…](https://www.youtube.com/watch?v=GhV-gzhR9Hg) | KBS 한국방송 | 2,780,000 | 1,687,913 | 79,557.1 | 18.6분 | 2026-10-03 | 12. 커버·노래 부르기 |
| [I Exposed the KPop Demon Hunters EVIL Babysitter!](https://www.youtube.com/watch?v=wdluy5UnnDU) | Topper Guild | 95,600,000 | 13,791,370 | 78,889.1 | 29분 | 2026-05-02 | 10. 팝송·K팝·J팝 |
| [Battle of the Idols! HUNTR/X VS Saja Boys 💥 KPop Demon Hunt…](https://www.youtube.com/watch?v=jGbHLocBmmY) | Netflix Family | 10,700,000 | 9,908,441 | 78,776.5 | 10.5분 | 2026-06-20 | 10. 팝송·K팝·J팝 |
| [HANUMAN CHALISA - Healing Version 🕉️ ∣ हनुमान चालीसा ∣ Calm…](https://www.youtube.com/watch?v=Ui0y6Wx9vBo) | Mantra Marg | 29,800 | 25,276,650 | 75,909.4 | 8분 | 2025-11-25 | 1. 수면·명상·힐링 |
| [[우리들의 발라드] 임바다🎵김성호의 회상_김성호｜261005 1회](https://www.youtube.com/watch?v=TCEYiDptimE) | 스브스 예능맛집 | 2,780,000 | 1,412,206 | 75,479.4 | 4.7분 | 2026-10-05 | 9. 가요·발라드·트로트 |
| [人魚VS Kpopスター! 🧜‍♀️✨ Kpopから人魚メイクオーバーへ 💄🌊](https://www.youtube.com/watch?v=0ikOKIelu1g) | VelvetPop Jap… | 259,000 | 5,764,950 | 67,933.0 | 16.1분 | 2026-07-31 | 10. 팝송·K팝·J팝 |
| [The Sound of Silence ∣ Like You've Never Felt Before ∣ Blue…](https://www.youtube.com/watch?v=cmRcndB-xE8) | PulsedBlues | 18,700 | 6,535,810 | 67,864.1 | 5.2분 | 2026-07-20 | 6. 피아노·클래식·연주곡 |
| [🔥 Gareeb Piano Genius Ko Rich School Mein Scholarship Mili……](https://www.youtube.com/watch?v=TNsvoP-Dl9g) | Alex Explaine… | 57,800 | 1,050,285 | 67,027.4 | 64.2분 | 2026-10-08 | 6. 피아노·클래식·연주곡 |
| [썸데이 - 고백 I [해피투게더🍀혼자가 아니어서 좋아] ∣ KBS 260904 방송](https://www.youtube.com/watch?v=g2nVvWGDNrY) | KBS 해피투게더 | 196,000 | 3,285,532 | 66,002.6 | 4.8분 | 2026-09-04 | 11. 힙합·R&B·EDM |
| [피아노가 들리는 원희 노래실력 근황](https://www.youtube.com/watch?v=CmXSVMCrNUQ) | Sofa4844 | 264,000 | 1,044,755 | 65,648.1 | 8.3분 | 2026-10-08 | 6. 피아노·클래식·연주곡 |
| [Bukzin Keyz, Benzoo, Tango Supreme - Mopepe (Visualizer)](https://www.youtube.com/watch?v=zZBtkOCPQ0o) | BukzinKeysVEVO | 24,600 | 15,904,654 | 64,547.2 | 4.5분 | 2026-02-19 | 6. 피아노·클래식·연주곡 |
| [기대 0% '한국 피아노맨'이 뉴욕의 낯선 공원에서 피아노를 쳤더니 생긴 일 (ft. 절대음감 피아노맨)](https://www.youtube.com/watch?v=EbQjKTOWVHg) | 콜드쉽 Coldsheep | 325,000 | 947,630 | 63,591.4 | 32.6분 | 2026-10-09 | 6. 피아노·클래식·연주곡 |
| [무슨 16살이 노래를 이렇게 잘해… 모두를 울린 레전드 참가자의 등장😭 #우리들의발라드](https://www.youtube.com/watch?v=McHPp3o-uFM) | 스브스 예능맛집 | 2,780,000 | 1,075,804 | 63,486.4 | 44.5분 | 2026-10-07 | 9. 가요·발라드·트로트 |

### 1-3-2. 이 묶음의 시청자 니즈 (시청자 댓글 1,125,218개 — 채널 주인 댓글·도배 4,011개 뺌, 8번과 같은 규칙)

| 갈래 | 댓글 | 비율 | 좋아요 합 |
|---|---|---|---|
| 좋은 점 — 영상 (도움·설명·정리·공감) | 1,146 | 0.1% | 31,096 |
| 감사·응원 (일반) | 10,695 | 1.0% | 274,951 |
| 더 알고 싶은 것 (질문·요청) | 1,066 | 0.1% | 27,935 |
| 아쉬운 점 — 영상 (제목·광고·길이·정보 오류·목소리) | 756 | 0.1% | 24,570 |
| 반박·불만 — 의견 다름 (내용) | 498 | 0% | 13,088 |
| 정치·사회 (영상과 무관한 의견) | 192 | 0% | 1,668 |
| 경험 공유 (내 이야기) | 3,672 | 0.3% | 85,155 |
| 구독·다음 기대 | 543 | 0% | 11,100 |
| **어느 갈래에도 안 듦** | 1,107,617 | 98% | 9,030,226 |

요청 — 다뤄 주세요·알려 주세요·궁금해요 (855개 중 좋아요 순 15개, 영상마다 2개까지):

- 👍9,594 [V17] “조회수 궁금해서 온 사람 손”
- 👍6,477 [V196] “대체 뭔노래가 나올까 궁금해서 들어왔습니다”
- 👍1,112 [V17] “아니 궁금해서 멜론 드가보니 진짜 빵빵 감상비율 20대가 젤 높은거 개웃기네 ㅋㅋㅋㅋ 5060보다 2030이 비율 더 높은거 실화냐 ㅋㅋㅋ”
- 👍719 [V213] “젤루 잘생긴 성리 K트롯돌 실력자 올라운더 멀티 AI 성리 글로벌 세계로 가자 국민투표 연속 7주1위 성리 우승까지 밀어주시길 부탁드립니다 꾸~~벅 " 핑크 스타 다이아몬드" 성리 1대 전설이 되자 ❤❤❤❤❤”
- 👍696 [V213] “성리 님 무명전설 오늘이밤 잔망스러움과 멋짐을 한껏 보여주신 무대 훌륭합니다 가수님께 국민투표 부탁드립니다”
- 👍61 [V148] “이건 무조건 음원 만들어 주세요!”
- 👍61 [V209] “정말 와… 소리만 나와서 댓글 남깁니다… 영상을 보면서 아직 저는 한참 부족하다는 걸 다시 느꼈네요… 정말! 많이 배우고 갑니다! 앞으로도 좋은 작품 많이 만들어 주세요!”
- 👍39 [V168] “처음 듣는 곡인데... 마음이 너무 아려서 끝까지 듣기가.. 눈물이 아리네요❤❤ 명곡 많이 많이 올려 주세요^^”
- 👍35 [V92] “스테이는 아니지만.. 좋은의미로 발라드부르시는 목소리가 의외네요~ 이런 음색을 내실수 있구나 싶어서.. 담담히 고백하는듯 부르시는게 좋았고 다른 발라드는 어떨지 궁금하네요~”
- 👍28 [V93] “번역기를 사용해서 문장이 조금 어색할 수 있는 점 양해 부탁드립니다. 우크라이나에서 인사드립니다! 🇺🇦 학창 시절 BIGBANG 노래를 정말 많이 들었던 팬으로서 이 버전은 정말 감동적이네요... 특유의 레트로 감성이 노래와 너무 잘 어울리고, 진짜 완벽한 곡이에요! 요즘 K-POP도 좋지만 역시 빅뱅 노래만의 감성은 대체 불가인 것 같아요. 방금 이 영상”
- 👍20 [V78] “도경수 재발 음방좀해줘 부탁해요👏👏👏👍👍👍👍🎉🎉❤️❤️💓”
- 👍18 [V106] “고막할배될때까지 계속해주세요 가요무대처럼 성시경오빠 오래오래방송해주세요~❤😊”
- 👍16 [V45] “가사에 귀 기울이다가 너무 좋아서 지하철 개찰구를 나오지 못하고 계속 서성이면서 들었어요. 감동을 너머 가슴을 후벼파네요. 우즈님 잘한다 잘한다 하니 너무 잘하시네요. 그리고 이승철선배님과 목소리 합이 예술입니다. 두 분 자주 같이 이런 프로젝트 부탁드려요🙏 마음이 너무 좋다🫶”
- 👍15 [V78] “도경수씨 커버앨범, 재즈앨범, 팝앨범 부탁해요”
- 👍10 [V106] “시경이횽 버전 세로캠 풀버젼 부탁드려요 섹황님의 세로캠🎉🎉🎉🎉🎉🎉”

물음표 질문 (반문이 섞임 — 좋아요 순 10개):

- 👍484 [V213] “❤성리 님❤ 촘을 추며 노래하는 게 얼마나 힘들까요? 성리님은 그 어려운 것을 이주 완변하게 해냅니다. 정말 멋진 분 입니다.”
- 👍55 [V17] “나 50대 아줌마에요 리센느 그냥 좋은데 이걸 어쩌요 더더더 좋아지네요 너무 잘하구 이뿌구 귀엽구 트로트매들리 2. 언제 나오나요?!!!”
- 👍47 [V213] “성리 오늘이밤 은 성리 님 만 부를수 있는 노래같아요 서서 부를순 있겠지만 춤을 추면서 저렇게 음이 안정적인 가수가 있을까요?”
- 👍22 [V17] “리센느 제나 추석선물 대박이네요. 어렸을때 받았던 종합선물세트 같네요. 정겹고 구수하고 맛있고 정이 있고 감동이 있네요. 가족이 생각나고 계속 계속 들어요.빵빵. 트롯은 언제 이렇게 배웠나요? 트롯천재! 재능이 이렇게 많은가요~~🎉🎉”
- 👍7 [V14] “댓글로 마녀사냥 하지 마세요 이해못한다해서 틀린게 아니에요 맘대로 추측해서 결국 불에 태워죽인 여성 예술가가 얼마나 많았나요? 중세시대도 아니고 댓글이 너무 기괴하고 음침합니다”
- 👍7 [V106] “성시경이계속하면안되나요? 연장 재연장 재재연장”
- 👍6 [V100] “누군가를 너무나 사랑하지만 직접 말할 수 없을 때 어떻게 해야 할까요?이 노래는 완벽하게 나왔어요. ❤”
- 👍6 [V207] “늙크크는 몇년생부터인가요?”
- 👍3 [V100] “🇰🇷음, 어떻게 말해야 할까요? 여러분은 한 시대를 대표하는 최고의 그룹이 될 거예요. 정말 믿기지 않을 정도예요. 여러분 모두 정말 땀과 노력을 쏟아부었으니까요. 😍 솔직히 여러분이 군 복무를 하러 가게 되면 제가 어떻게 견딜 수 있을지 모르겠어요. 🥺 정말 많이 사랑해요. 제 가장 큰 꿈은 여러분의 콘서트에 가는 건데, 티켓을 사거나 한국으로 갈 형편이”
- 👍3 [V209] “이노래 컬러링은 안되나요?”

## 2. 주제 — 주제 묶음별 성공 비율 (비교 집단)

주제 묶음 = `tag_rules.toml` TAG_THEMES (제목에서 맞는 글자가 가장 긴 묶음, 없으면 태그). 비교 집단 성공 비율 19% 과 견주어 본다. 영상 15개 미만은 '표본 적음'.

| 주제 묶음 | 영상 | 성공 | 성공 비율 | 배수 중앙값 | 조회수 중앙값 | 성공 사례 # |
|---|---|---|---|---|---|---|
| 13. OST·사운드트랙 | 55 | 19 | 34% | 1.3 | 5,324 | 181, 235, 255, 274, 351, 429, 482, 658, 818, 974 |
| 기타 | 1332 | 447 | 34% | 1.1 | 6,107.0 | 1, 3, 4, 5, 9, 12, 14, 16, 17, 18, 22, 23, 25, 26, 27, 28, 29, 32, 34, 37, 39, 41, 42, 45, 48, 49, 52, 53, 55, 56, 57, 58, 64, 67, 68, 70, 74, 75, 76, 78, 80, 81, 82, 83, 84, 89, 90, 94, 96, 98, 99, 104, 106, 108, 109, 110, 111, 113, 116, 117, 118, 121, 123, 124, 125, 127, 128, 131, 132, 133, 137, 141, 142, 143, 146, 151, 152, 156, 157, 158, 160, 161, 163, 165, 166, 169, 173, 177, 179, 180, 182, 183, 184, 186, 187, 189, 190, 191, 192, 194, 196, 198, 200, 203, 204, 205, 207, 211, 219, 221, 222, 226, 230, 231, 232, 233, 239, 240, 242, 251, 254, 256, 257, 260, 270, 276, 277, 283, 287, 291, 301, 305, 306, 313, 319, 323, 334, 337, 339, 341, 343, 348, 358, 359, 369, 370, 372, 379, 380, 391, 399, 404, 410, 420, 425, 428, 439, 440, 447, 466, 473, 474, 486, 487, 490, 493, 495, 504, 514, 516, 527, 534, 541, 542, 547, 557, 571, 582, 589, 605, 607, 614, 620, 630, 633, 638, 639, 647, 690, 695, 703, 715, 716, 719, 722, 732, 748, 750, 753, 760, 768, 771, 774, 782, 797, 805, 817, 823, 828, 829, 868, 872, 875, 880, 896, 902, 911, 924, 928, 930, 935, 946, 960, 962, 968, 970, 971, 975, 976, 981, 1005, 1010, 1014, 1023, 1030, 1039 |
| 10. 팝송·K팝·J팝 | 118 | 32 | 27% | 1.1 | 6,885.0 | 15, 20, 30, 114, 136, 145, 164, 170, 247, 282, 284, 292, 333, 345, 393, 446, 539, 587, 623, 645, 654, 669, 670, 682, 694, 699, 763, 891, 943, 994, 995, 1027, 1054 |
| 5. 운동·드라이브·신나는 | 98 | 25 | 26% | 1.2 | 5,996.5 | 100, 119, 122, 258, 376, 484, 535, 585, 596, 618, 661, 731, 755, 757, 803, 812 |
| 11. 힙합·R&B·EDM | 165 | 37 | 22% | 0.7 | 6,584 | 2, 135, 228, 261, 324, 622, 684, 702, 740, 786, 839, 847, 862, 881, 898, 964, 1016 |
| 8. 로파이·시티팝·칠 | 476 | 104 | 22% | 0.7 | 4,592.5 | 6, 7, 8, 11, 19, 24, 33, 36, 40, 43, 44, 47, 50, 59, 60, 65, 66, 69, 72, 85, 86, 91, 95, 97, 101, 102, 103, 105, 115, 120, 140, 147, 150, 153, 155, 174, 188, 201, 209, 213, 216, 227, 241, 246, 253, 263, 266, 296, 297, 317, 318, 328, 336, 360, 361, 365, 367, 384, 388, 396, 398, 443, 456, 457, 459, 469, 471, 475, 477, 497, 498, 500, 501, 509, 518, 522, 523, 532, 559, 577, 626, 631, 842, 871, 908, 950, 1011, 1018 |
| 12. 커버·노래 부르기 | 173 | 37 | 21% | 0.4 | 4,574 | 73, 138, 197, 288, 352, 401, 417, 423, 431, 434, 472, 615, 629, 648, 665, 708, 743, 778, 779, 796, 801, 809, 810, 816, 826, 918, 954, 958, 980, 1004 |
| 7. 재즈·보사노바 | 109 | 20 | 18% | 0.3 | 6,399 | 273, 354, 363, 408, 452, 519, 520, 533, 599, 712, 819, 820, 827, 836, 865, 882, 997, 1034 |
| 2. 자연 소리·백색소음 | 143 | 24 | 17% | 0.6 | 4,070 | 93, 107, 167, 245, 272, 280, 303, 314, 325, 346, 356, 397, 419, 424, 430, 625, 681, 683, 737, 892, 940, 952, 956, 1053 |
| 6. 피아노·클래식·연주곡 | 869 | 131 | 15% | 0.4 | 2,734 | 21, 88, 112, 168, 171, 172, 208, 238, 281, 290, 310, 315, 321, 322, 330, 332, 338, 340, 344, 353, 355, 368, 377, 385, 387, 403, 405, 406, 411, 413, 416, 418, 421, 422, 427, 432, 436, 438, 441, 464, 465, 467, 476, 479, 485, 496, 506, 508, 521, 524, 526, 528, 537, 550, 553, 554, 558, 564, 565, 568, 569, 572, 573, 574, 576, 579, 583, 593, 594, 597, 602, 606, 612, 613, 617, 619, 621, 651, 656, 664, 667, 675, 678, 686, 687, 691, 693, 696, 697, 698, 700, 701, 713, 718, 725, 726, 730, 734, 736, 742, 744, 751, 754, 756, 761, 765, 766, 767, 775, 776, 777, 780, 781, 784, 785, 787, 788, 791, 795, 799, 808, 822, 831, 833, 845, 848, 852, 854, 855, 856, 860, 866, 874, 876, 878, 879, 883, 887, 897, 909, 932, 933, 945, 948, 949, 951, 953, 957, 965, 969, 992, 996, 1009, 1012, 1015, 1035, 1038, 1046, 1047, 1049, 1050, 1052 |
| 4. 카페·매장·라운지 | 210 | 27 | 13% | 0.4 | 2,359.0 | 10, 38, 62, 87, 176, 195, 202, 206, 212, 218, 229, 248, 269, 300, 335, 342, 362, 378, 381, 433, 449, 483, 491, 513, 531, 544, 555, 556, 561, 598, 616, 636, 641, 692, 706, 728, 733, 752, 821, 840, 850, 863, 903, 917, 938, 939, 942, 961, 963, 983, 987, 1025, 1031, 1032 |
| 14. AI 음악 | 71 | 9 | 13% | 0.2 | 1,994 | 460, 538, 548, 575, 668, 830, 861, 990 |
| 9. 가요·발라드·트로트 | 367 | 37 | 10% | 0.3 | 1,640 | 79, 148, 175, 214, 224, 244, 275, 278, 289, 293, 299, 308, 327, 329, 347, 412, 437, 450, 455, 517, 543, 560, 562, 570, 584, 603, 608, 628, 632, 637, 642, 643, 644, 650, 657, 666, 673, 676, 679, 689, 710, 717, 747, 759, 764, 772, 783, 792, 794, 815, 843, 846, 873, 888, 889, 890, 894, 895, 905, 912, 915, 927, 931, 936, 947, 966, 967, 972, 973, 982, 986, 989, 991, 1000, 1006, 1017, 1020, 1022, 1028, 1048, 1051 |
| 1. 수면·명상·힐링 | 1106 | 107 | 9.7% | 0.5 | 1,350.5 | 31, 35, 46, 51, 54, 61, 63, 77, 92, 130, 134, 144, 154, 162, 178, 185, 193, 199, 217, 220, 225, 234, 236, 237, 243, 249, 252, 259, 268, 286, 294, 295, 298, 302, 304, 311, 312, 316, 326, 331, 349, 350, 357, 364, 366, 374, 375, 382, 386, 389, 390, 392, 395, 400, 402, 409, 414, 415, 444, 445, 448, 451, 453, 454, 458, 461, 462, 463, 468, 470, 480, 481, 488, 494, 499, 502, 503, 510, 515, 529, 545, 551, 552, 567, 578, 580, 581, 586, 590, 595, 600, 601, 610, 611, 634, 640, 646, 652, 653, 655, 659, 660, 663, 671, 674, 685, 688, 709, 714, 720, 721, 723, 724, 729, 738, 741, 745, 758, 762, 769, 770, 789, 790, 793, 800, 804, 806, 807, 813, 824, 825, 832, 835, 837, 838, 844, 849, 851, 853, 857, 859, 864, 867, 870, 877, 884, 885, 893, 899, 900, 901, 906, 914, 916, 922, 926, 929, 941, 944, 955, 959, 977, 978, 984, 985, 993, 998, 1001, 1002, 1007, 1013, 1021, 1026, 1036, 1037, 1040, 1041, 1043, 1045 |
| 3. 공부·집중·작업 | 420 | 40 | 9.5% | 0.3 | 2,110.5 | 13, 71, 126, 129, 139, 149, 159, 210, 215, 223, 250, 262, 264, 265, 267, 271, 279, 285, 307, 309, 320, 371, 373, 383, 394, 426, 435, 442, 478, 489, 492, 505, 507, 512, 525, 530, 536, 540, 546, 549, 563, 566, 588, 591, 592, 604, 609, 624, 627, 635, 649, 662, 672, 677, 680, 705, 707, 739, 746, 749, 773, 798, 802, 814, 834, 858, 886, 904, 907, 913, 923, 934, 937, 979, 988, 999, 1003, 1008, 1019, 1024, 1029, 1033, 1044, 1055 |
| 15. CCM·찬양·국악·동요 | 119 | 11 | 9.2% | 0.5 | 3,110 | 407, 511, 704, 711, 727, 735, 811, 841, 869, 910, 919, 920, 921, 925, 1042 |

## 2-2. 형식(포맷) — 어떤 모양의 영상인가 (제목·채널 이름·태그 낱말로 나눔)

형식 규칙 = `analysis_rules.toml` [format] (위에서부터 먼저 맞는 것 하나, 낱말 규칙이라 거칠다). **성공 사례 몫**은 성공 사례 중 그 형식 비율, **시장 지수**는 3번과 같은 수요 몫 ÷ 공급 몫 (1보다 크면 영상 하나가 평균보다 많이 봄), **같은 채널**은 1-2번의 잘된 영상 중 비율 vs 평소 영상 중 비율. 원인이 아니라 묶음이다.

| 형식 | 비교 집단 영상 (성공 비율) | 배수 중앙값 | 성공 사례 몫 (#) | 시장 영상 · 지수 | 같은 채널 잘된 vs 평소 |
|---|---|---|---|---|---|
| AI 음악 | 170 (8.8%) | 0.3 | 2.9% (50, 112, 148, 275, 298, 299, 386, 460, 538, 548, 575, 608 …) | 45 · 0.1 | 2.6% vs 2.6% |
| 커버·직접 부른 노래 | 308 (20%) | 0.4 | 5.5% (34, 138, 197, 208, 214, 247, 266, 284, 288, 290, 321, 332 …) | 43 · 0.8 | 5.4% vs 5.3% |
| 연주 (직접 연주하는 영상) | 72 (24%) | 0.9 | 1.2% (355, 403, 496, 508, 601, 687, 693, 701, 718, 742, 942, 1021 …) | 12 · 0.3 (표본 적음) | 0.9% vs 1.0% |
| 플레이리스트·모음 (여러 곡) | 1821 (26%) | 1.0 | 34% (3, 13, 14, 16, 17, 18, 20, 26, 27, 28, 35, 37 …) | 245 · 0.7 | 31% vs 30% |
| 자연 소리·백색소음 (음악 낱말 없는 제목) | 59 (12%) | 1.0 | 0.9% (314, 346, 419, 424, 480, 625, 762, 922, 940, 952) | 2 · 0.1 (표본 적음) | 1.1% vs 1.2% |
| 긴 한 곡·반복 (N시간) | 158 (15%) | 0.4 | 3.1% (78, 220, 237, 252, 267, 296, 316, 328, 338, 377, 391, 397 …) | 15 · 0.9 | 3.5% vs 2.9% |
| 한 곡 (뮤직비디오·음원·가사) | 241 (19%) | 0.6 | 3.5% (15, 30, 48, 77, 79, 91, 98, 136, 145, 147, 174, 183 …) | 44 · 6.5 | 3.7% vs 4.5% |
| 음악 (그 밖 모양 — 한 편짜리 BGM 등) | 2740 (14%) | 0.4 | 44% (1, 4, 5, 6, 7, 8, 9, 11, 19, 21, 22, 23 …) | 416 · 0.7 | 47% vs 46% |
| 정보·해설 (그 밖) | 262 (26%) | 1.0 | 4.2% (2, 10, 12, 32, 38, 41, 62, 64, 88, 123, 135, 160 …) | 28 · 1.2 | 4.8% vs 6.1% |

## 3. 수요와 공급 — 찾는 사람에 비해 영상이 적은 곳

### 3-1. 주제 묶음별 (최근 90일 영상 850개 — 채널 크기 상관없음)

수요 몫 = 그 묶음 영상들의 하루 조회수 합 ÷ 전체, 공급 몫 = 영상 수 ÷ 전체. **지수 = 수요 몫 ÷ 공급 몫** — 1 보다 크면 영상 하나가 평균보다 많이 보임(공급이 모자라 보임), 작으면 영상이 넘침. 작은 채널 성공 비율 = 2번 표. 시청자 질문 = 사례 댓글 중 그 묶음 낱말이 든 질문·요청.

| 주제 묶음 | 영상(공급) | 채널 | 수요 몫 | 공급 몫 | 지수 | 영상당 하루 조회수 중앙값 | 작은 채널 성공 비율 | 시청자 질문 |
|---|---|---|---|---|---|---|---|---|
| 기타 | 171 | 125 | 54% | 20% | **2.7** | 9,073.1 | 34% | 0 |
| 8. 로파이·시티팝·칠 | 45 | 41 | 10% | 5.3% | **1.9** | 27,375.9 | 22% | 2 |
| 9. 가요·발라드·트로트 | 58 | 41 | 7.1% | 6.8% | **1.0** | 3,583.0 | 10% | 113 |
| 10. 팝송·K팝·J팝 | 38 | 25 | 4.5% | 4.5% | **1.0** | 2,878.2 | 27% | 21 |
| 12. 커버·노래 부르기 | 22 | 16 | 1.6% | 2.6% | **0.6** | 5,364.2 | 21% | 29 |
| 3. 공부·집중·작업 | 76 | 65 | 4.2% | 8.9% | **0.5** | 1,202.8 | 9.5% | 27 |
| 4. 카페·매장·라운지 | 47 | 33 | 2.4% | 5.5% | **0.4** | 3,402.1 | 13% | 12 |
| 6. 피아노·클래식·연주곡 | 166 | 113 | 8.5% | 20% | **0.4** | 4,905.5 | 15% | 30 |
| 1. 수면·명상·힐링 | 172 | 128 | 4.6% | 20% | **0.2** | 309.6 | 9.7% | 21 |
| 11. 힙합·R&B·EDM (표본 적음) | 9 | 9 | 0.7% | 1.1% | **0.7** | 1,767.6 | 22% | 3 |
| 7. 재즈·보사노바 (표본 적음) | 10 | 8 | 0.6% | 1.2% | **0.5** | 7,689.2 | 18% | 9 |
| 2. 자연 소리·백색소음 (표본 적음) | 10 | 10 | 0.5% | 1.2% | **0.4** | 5,421.8 | 17% | 2 |
| 13. OST·사운드트랙 (표본 적음) | 8 | 8 | 0.4% | 0.9% | **0.4** | 6,048.1 | 34% | 2 |
| 5. 운동·드라이브·신나는 (표본 적음) | 11 | 10 | 0.3% | 1.3% | **0.2** | 1,461.0 | 26% | 10 |
| 15. CCM·찬양·국악·동요 (표본 적음) | 5 | 5 | 0.1% | 0.6% | **0.2** | 3,897.0 | 9.2% | 36 |
| 14. AI 음악 (표본 적음) | 2 | 2 | 0% | 0.2% | **0.1** | 3,812.8 | 13% | 12 |

### 3-2. 검색어별 (탐색·검색 캐시 — 검색어마다 조회수 순 상위 결과)

결과 수 = YouTube 가 알려 준 그 기간 영상 수 추정(공급). 영상당 하루 조회수 = 상위 결과 하루 조회수 합 ÷ 결과 수 (클수록 영상에 비해 찾는 사람이 많음). 큰 채널 비율 = 상위 결과 중 구독자 5만 넘는 채널 (클수록 들어가기 어려움). **작은 채널이 뚫은 비율** = 상위 결과 중 작은 채널(5만 이하)의 성공 영상(×3·1만) 비율 — 클수록 새 채널도 상위에 들 수 있음. 지금 검색어(keywords.txt)가 먼저, 예전 검색어는 '(예전)'.

| 검색어 | 기간(일) | 본 영상 | 결과 수(공급) | 최근 30일 | 조회수 중앙값 | 하루 조회수 중앙값 | 영상당 하루 조회수 | 큰 채널 비율 | 작은 채널이 뚫은 비율 |
|---|---|---|---|---|---|---|---|---|---|
| 플리 | 182 | 100 | 1,253,238 | 0 | 560,698 | 4,158.9 | 0.5 | 12% | 88% (80개) |
| playlist | 182 | 100 | 2,000,000 | 2 | 2,569,948.0 | 26,993.0 | 1.8 | 12% | 88% (77개) |
| study music | 182 | 100 | 2,000,000 | 2 | 2,169,517.0 | 16,414.3 | 1.3 | 15% | 85% (66개) |
| deep sleep music | 182 | 100 | 1,373,573 | 2 | 1,105,112.0 | 9,910.9 | 1.0 | 19% | 81% (60개) |
| stress relief music | 182 | 100 | 1,247,946 | 2 | 1,282,578.5 | 10,512.8 | 1.3 | 20% | 80% (66개) |
| ambient music | 182 | 100 | 1,973,196 | 3 | 925,183 | 6,321.3 | 0.4 | 20% | 80% (62개) |
| lofi | 182 | 100 | 2,000,000 | 1 | 2,128,712 | 23,875.9 | 1.6 | 21% | 79% (67개) |
| focus music | 182 | 100 | 2,000,000 | 2 | 1,203,449.5 | 9,719.2 | 0.7 | 24% | 76% (56개) |
| calm music | 182 | 100 | 2,000,000 | 1 | 1,785,989 | 13,949.9 | 0.8 | 25% | 75% (55개) |
| BGM | 182 | 100 | 2,000,000 | 1 | 560,766.0 | 4,450.4 | 0.8 | 26% | 74% (67개) |
| peaceful music | 182 | 100 | 1,988,001 | 1 | 1,627,137 | 10,938.0 | 0.8 | 26% | 74% (60개) |
| MeditationMusic | 182 | 100 | 877,295 | 3 | 349,334 | 2,235.5 | 0.4 | 22% | 74% (57개) |
| soothing music | 182 | 100 | 1,548,676 | 2 | 1,216,617 | 10,141.4 | 1.0 | 28% | 72% (57개) |
| calming music | 182 | 100 | 2,000,000 | 1 | 1,377,200.5 | 12,015.1 | 0.7 | 29% | 71% (54개) |
| 플레이리스트 | 182 | 100 | 1,520,777 | 2 | 590,112 | 4,768.2 | 0.5 | 30% | 70% (57개) |
| Sleep Music | 182 | 100 | 2,000,000 | 1 | 1,593,972 | 15,457.9 | 0.8 | 30% | 70% (44개) |
| 힐링음악 | 182 | 100 | 387,758 | 1 | 302,240 | 1,903.4 | 1.0 | 24% | 70% (66개) |
| 감성발라드 | 182 | 100 | 254,101 | 1 | 428,773 | 4,286.4 | 2.2 | 34% | 66% (63개) |
| chill music | 182 | 100 | 2,000,000 | 2 | 2,545,292 | 25,137.0 | 3.0 | 35% | 65% (46개) |
| yoga music | 182 | 100 | 2,000,000 | 0 | 1,754,936 | 12,451.7 | 0.5 | 36% | 64% (30개) |
| cafe music | 182 | 100 | 2,000,000 | 3 | 1,156,735 | 11,578.5 | 0.7 | 36% | 64% (49개) |
| 감성음악 | 182 | 100 | 1,090,278 | 4 | 354,709.0 | 2,940.7 | 0.4 | 26% | 63% (59개) |
| relaxing music | 365 | 100 | 1,722,502 | 0 | 3,794,957.0 | 18,544.4 | 1.2 | 38% | 62% (45개) |
| work music | 182 | 100 | 2,000,000 | 3 | 286,555 | 3,016.5 | 0.3 | 15% | 61% (48개) |
| relaxation music | 182 | 100 | 1,658,036 | 1 | 1,146,720.0 | 9,763.3 | 0.8 | 40% | 60% (48개) |
| healingmusic | 182 | 100 | 516,429 | 3 | 49,239 | 530.2 | 0.2 | 10% | 58% (40개) |
| instrumental music | 182 | 100 | 2,000,000 | 2 | 930,100.5 | 8,380.5 | 0.5 | 43% | 57% (43개) |
| 카페음악 | 182 | 100 | 534,014 | 0 | 281,019 | 1,944.4 | 0.6 | 33% | 55% (52개) |
| relaxing piano | 182 | 100 | 1,363,317 | 8 | 475,903.0 | 4,810.5 | 0.5 | 45% | 54% (46개) |
| piano | 182 | 100 | 2,000,000 | 3 | 1,018,888 | 9,103.9 | 0.8 | 49% | 51% (35개) |
| background music | 182 | 100 | 2,000,000 | 4 | 936,621.0 | 9,196.1 | 0.6 | 51% | 49% (39개) |
| RelaxingMusic | 182 | 100 | 1,218,528 | 3 | 839,191 | 8,312.5 | 0.8 | 52% | 48% (42개) |
| piano music | 365 | 100 | 2,000,000 | 0 | 2,083,818 | 9,232.8 | 0.7 | 52% | 48% (30개) |
| pianomusic | 182 | 100 | 563,594 | 9 | 144,719 | 1,049.8 | 0.3 | 20% | 47% (39개) |
| 명상음악 | 182 | 100 | 542,059 | 1 | 132,077.5 | 980.0 | 0.3 | 17% | 45% (38개) |
| 발라드 | 182 | 100 | 572,147 | 9 | 820,907 | 6,305.5 | 2.6 | 56% | 44% (41개) |
| relaxing piano music | 182 | 100 | 2,000,000 | 11 | 501,971.0 | 6,791.1 | 0.4 | 56% | 44% (36개) |
| 음악 | 182 | 100 | 2,000,000 | 5 | 864,521.5 | 7,219.1 | 0.6 | 57% | 43% (36개) |
| 편안한음악 | 182 | 100 | 420,824 | 12 | 126,566 | 768.8 | 0.4 | 13% | 42% (41개) |
| 공부음악 | 182 | 100 | 474,576 | 2 | 209,116 | 1,688.3 | 0.6 | 28% | 40% (30개) |
| … 나머지 21개는 analysis.json |  |  |  |  |  |  |  |  |  |

### 3-3. 사람들이 찾는 말 (YouTube 자동완성) 중 최근 영상이 적은 말

수요 점수 = 검색어를 넣었을 때 자동완성에 앞쪽에 나올수록·여러 검색어에서 나올수록 큼. 최근 영상 = 우리가 본 최근 영상 중 제목에 그 말의 낱말이 다 든 수. 틈 = 수요 점수 ÷ (1 + 최근 영상). **공급 확인** = 웹 화면 [공급 확인]으로 그 말을 직접 검색한 결과 (최근 90일 결과 수·상위 영상).

| 말 | 수요 점수 | 나온 검색어 | 최근 영상(우리가 본) | 틈 | 공급 확인: 결과 수 | 영상당 하루 조회수 | 작은 채널 비율 | 최근 30일 |
|---|---|---|---|---|---|---|---|---|
| healing music kks | 1.8 | healing music, healingmusic | 0 | 1.8 | 확인 전 |  |  |  |
| piano music bros | 1.8 | piano music, pianomusic | 0 | 1.8 | 확인 전 |  |  |  |
| 수면음악 빗소리 | 1.7 | 수면음악, 숙면음악 | 0 | 1.7 | 확인 전 |  |  |  |
| 수면음악 3시간 | 1.7 | 수면음악, 숙면음악 | 0 | 1.7 | 확인 전 |  |  |  |
| healing music studio | 1.6 | healing music, healingmusic | 0 | 1.6 | 확인 전 |  |  |  |
| piano music for studying | 1.6 | piano music, pianomusic | 0 | 1.6 | 확인 전 |  |  |  |
| bgm 무료 | 1.6 | bgm, BGM | 0 | 1.6 | 확인 전 |  |  |  |
| 수면음악 지브리 | 1.4 | 수면음악, 숙면음악 | 0 | 1.4 | 확인 전 |  |  |  |
| meditation music 20 minutes | 1.4 | meditation music, MeditationM… | 0 | 1.4 | 확인 전 |  |  |  |
| sleep music 1 hour | 1.4 | sleep music, Sleep Music | 0 | 1.4 | 확인 전 |  |  |  |
| bgmer awaken | 1.4 | bgm, BGM | 0 | 1.4 | 확인 전 |  |  |  |
| 수면음악 10분 | 1.2 | 수면음악, 숙면음악 | 0 | 1.2 | 확인 전 |  |  |  |
| sleep music live | 1.2 | sleep music, Sleep Music | 0 | 1.2 | 확인 전 |  |  |  |
| piano music bros chopin | 1.1 | piano music, pianomusic | 0 | 1.1 | 확인 전 |  |  |  |
| bgm 추천 | 1.1 | bgm, BGM | 0 | 1.1 | 확인 전 |  |  |  |
| 수면음악 클래식 | 1.0 | 수면음악, 숙면음악 | 0 | 1.0 | 확인 전 |  |  |  |
| healing music playlist | 1.0 | healing music, healingmusic | 0 | 1.0 | 확인 전 |  |  |  |
| sleep music playlist | 1.0 | sleep music, Sleep Music | 0 | 1.0 | 확인 전 |  |  |  |
| peaceful music for studying | 1.0 | peaceful music | 0 | 1.0 | 확인 전 |  |  |  |
| 명상음악 5분 | 0.9 | 명상음악 | 0 | 0.9 | 확인 전 |  |  |  |
| meditation music for positive… | 1.8 | meditation music, MeditationM… | 1 | 0.9 | 확인 전 |  |  |  |
| deep sleep music live | 0.9 | deep sleep music | 0 | 0.9 | 확인 전 |  |  |  |
| 자장가동화 | 0.9 | 자장가 | 0 | 0.9 | 확인 전 |  |  |  |
| 수면유도음악 4시간 | 0.9 | 수면유도음악 | 0 | 0.9 | 확인 전 |  |  |  |
| 치유음악 광고없음 | 0.9 | 치유음악 | 0 | 0.9 | 확인 전 |  |  |  |
| 집중음악 1시간 | 0.9 | 집중음악 | 0 | 0.9 | 확인 전 |  |  |  |
| 카페음악 광고없는 | 0.9 | 카페음악 | 0 | 0.9 | 확인 전 |  |  |  |
| 노래모음 아이돌 | 0.9 | 노래모음 | 0 | 0.9 | 확인 전 |  |  |  |
| kpop in public | 0.9 | kpop | 0 | 0.9 | 확인 전 |  |  |  |
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
| vs 비교 | 69 (35%) | 5762 (19%) | +16%p | **눈에 띔** | 1.1% |
| 25자 미만 | 397 (30%) | 5434 (18%) | +12%p | **눈에 띔** | 8.4% |
| 빚투·신용·미수·레버리지·대출 | 2 (50%) | 5829 (19%) | +31%p | 표본 적음 | 0.1% |
| 금액(억·만원) | 1 (0%) | 5830 (19%) | -19%p | 표본 적음 | 0% |
| 손실 낱말(망하·날린·잃은·반토막) | 7 (0%) | 5824 (19%) | -19%p | 표본 적음 | 0% |
| 직접·해보니·N년 기록 | 4 (0%) | 5827 (19%) | -19%p | 표본 적음 | 0% |
| S&P500·ETF·지수·나스닥 | 1 (0%) | 5830 (19%) | -19%p | 표본 적음 | 0% |
| N가지 | 3 (33%) | 5828 (19%) | +14%p | 표본 적음 | 0% |
| 과정·벌어진 일·결말·결국 | 12 (8.3%) | 5819 (19%) | -11%p | 표본 적음 | 0% |
| 사연·오디오북·실화·고백 | 12 (8.3%) | 5819 (19%) | -11%p | 표본 적음 | 0% |
| 40자 이상 | 4824 (17%) | 1007 (27%) | -10%p |  | 82% |
| 물음표 ? | 92 (26%) | 5739 (19%) | +7%p |  | 1.1% |
| 따옴표·괄호로 강조 | 1055 (24%) | 4776 (18%) | +6%p |  | 19% |
| 구분 기호(ㅣ·｜·/)로 나눔 | 3502 (17%) | 2329 (22%) | -5%p |  | 59% |
| 이유 | 13 (23%) | 5818 (19%) | +4%p | 표본 적음 | 0% |
| AI | 469 (22%) | 5362 (19%) | +3%p |  | 8.1% |
| 노후·퇴직금·은퇴·50~70대 | 18 (22%) | 5813 (19%) | +3%p |  | 0.5% |
| 느낌표 ! | 114 (18%) | 5717 (19%) | -2%p |  | 1.8% |
| 숫자가 들어감 | 1898 (18%) | 3933 (19%) | -1%p |  | 33% |
| 말줄임 …·... | 168 (18%) | 5663 (19%) | -0%p |  | 3.3% |
| 패턴형(공통점·특징·이유·N가지·착각·과정) | 21 (19%) | 5810 (19%) | +0%p |  | 0% |

### 4-2. 제목 낱말 (비교 집단 제목에 자주 나온 낱말 — 조사를 거칠게 뗌)

| 낱말 | 있음 (성공 비율) | 없음 (성공 비율) | 차이 | 표시 |
|---|---|---|---|---|
| playlist | 220 (36%) | 5611 (18%) | +18%p | **눈에 띔** |
| Playlist | 445 (28%) | 5386 (18%) | +10%p |  |
| 플레이리스트 | 181 (23%) | 5650 (19%) | +4%p |  |
| Jazz | 207 (21%) | 5624 (19%) | +2%p |  |
| Love | 215 (20%) | 5616 (19%) | +2%p |  |
| Chill | 206 (19%) | 5625 (19%) | +0%p |  |
| Lofi | 285 (19%) | 5546 (19%) | +0%p |  |
| Song | 280 (19%) | 5551 (19%) | +0%p |  |
| BGM | 234 (19%) | 5597 (19%) | +0%p |  |
| Focus | 215 (7.0%) | 5616 (19%) | -12%p | **눈에 띔** |
| 음악 | 246 (8.1%) | 5585 (20%) | -11%p | **눈에 띔** |
| Deep | 424 (9.4%) | 5407 (20%) | -10%p | **눈에 띔** |
| Study | 230 (9.1%) | 5601 (19%) | -10%p | **눈에 띔** |
| Healing | 206 (9.7%) | 5625 (19%) | -10%p |  |
| 마음 | 193 (9.8%) | 5638 (19%) | -10%p |  |
| Music | 1076 (12%) | 4755 (21%) | -9%p |  |
| Mind | 181 (11%) | 5650 (19%) | -8%p |  |
| Sleep | 333 (13%) | 5498 (19%) | -7%p |  |
| Peaceful | 198 (13%) | 5633 (19%) | -7%p |  |

### 4-3. 제목 길이

| 길이 | 영상 (성공 비율) |
|---|---|
| 0~24자 | 397 (30%) |
| 25~34자 | 380 (28%) |
| 35~44자 | 484 (18%) |
| 45자 이상 | 4570 (17%) |

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

성공 사례 #1041–#1055:

![성공 사례 썸네일 #1041-#1055](analysis_thumbs_53.jpg)

같은 채널 짝 — 줄마다 [성공 사례 #n · 같은 채널 평소 영상 #n-a · #n-b] (1 … #14-b):

![같은 채널 썸네일 짝](analysis_thumbs_pairs_01.jpg)

같은 채널 짝 — 줄마다 [성공 사례 #n · 같은 채널 평소 영상 #n-a · #n-b] (18 … #32-b):

![같은 채널 썸네일 짝](analysis_thumbs_pairs_02.jpg)

비교 — 자료를 받았지만 성공 기준 밖 (조회수 큰 순, 번호는 `analysis.json` 의 others 순서):

![비교 썸네일](analysis_thumbs_others.jpg)

## 6. 길이·내용 구성

### 6-1. 길이별 성공 비율 (비교 집단)

| 길이 | 영상 (성공 비율) | 성공 사례 |
|---|---|---|
| 4~8분 | 1555 (18%) | 253 |
| 8~15분 | 614 (23%) | 116 |
| 15~25분 | 629 (32%) | 124 |
| 25~40분 | 445 (23%) | 64 |
| 40분 이상 | 2588 (15%) | 498 |

### 6-2. 채널 크기별 성공 비율 (참고 — 구독자가 적을수록 배수가 커지기 쉬움)

| 구독자 | 영상 (성공 비율) |
|---|---|
| 0~999명 | 801 (12%) |
| 1,000~4,999명 | 1628 (25%) |
| 5,000~19,999명 | 2095 (18%) |
| 20,000~50,000명 | 1307 (18%) |

### 6-3. 성공 사례의 구성

- 길이 중앙값: 성공 사례 29.7분 · 비교 집단의 나머지 31.5분
- 타임라인(챕터) 있는 성공 사례: 28% (챕터 수 중앙값 12)
- 대본이 있는 성공 사례: 0개 — 말 속도 중앙값 – 음절/초, 첫 1분 음절 중앙값 – (대본이 없어 도입부·흐름은 아직 셀 수 없음)
- 도입부(첫 20초 첫 문장) 유형: 대본 없음 — 아직 셀 수 없음
- 사례마다의 챕터·도입부(첫 20초)·첫 1분·90초마다 흐름은 9번.

### 6-4. 참여율 (비교 집단, 중앙값)

| | 영상 | 조회수 1,000회당 좋아요 | 조회수 1,000회당 댓글 |
|---|---|---|---|
| 성공 | 1107 | 7.9 | 0.2 |
| 나머지 | 4724 | 11.0 | 0.8 |

## 7. 구독자 — 빨리 크는 작은 채널

YouTube API 는 영상별 구독 증가를 주지 않는다 → 채널 단위로 본다. 개설 24개월 안·구독자 1,000 이상 채널을 **월 구독자 증가(구독자 ÷ 개설 뒤 달 수)** 순으로. 최근 하루 증가 = 받을 때마다 남긴 구독자 기록 (3일 넘게 벌어져야 나옴). 주로 다룬 주제 = 우리가 본 그 채널 영상의 주제 묶음. **기관·브랜드?** = 채널 이름에 운용사 ETF 상표·증권·은행·공식·방송 같은 말 (`analysis_rules.toml` [growth] BRAND_HINT) — 광고비로 큰 채널일 수 있어 개인 채널과 따로 보라.

| 채널 | 기관·브랜드? | 개설 | 구독자 | 월 구독자 증가 | 최근 하루 증가 | 영상 수 | 월 업로드 | 길이 중앙값 | 주로 다룬 주제 | 대표 영상 (하루 조회수 큰 것) |
|---|---|---|---|---|---|---|---|---|---|---|
| 정이랑의 진기명기 |  | 2025-11-07 | 198,000 | 17,220 | 0.0 | 310 | 27.0 | 23.1분 | 6. 피아노·클래식·연주곡 | [2007년 우己lㄱr バr己б했던 학원☆™🎹 #정이랑 #추억 #공감 #…](https://www.youtube.com/watch?v=argmeBt7OUU) 2,916,955회 |
| 명곡부활단 |  | 2026-03-21 | 107,000 | 15,010 | 250.0 | 329 | 46.2 | 4.8분 | 5. 운동·드라이브·신나는, 9. 가요·발… | [여인 – 우리 가슴속 깊이 박혀 있던 그 노래, 듣는 순간 그 시절로 …](https://www.youtube.com/watch?v=a0iBRRoDnDw) 6,778,194회 |
| Rb Lofi |  | 2026-08-23 | 27,000 | 13,256 | 412.5 | 27 | 13.3 | 18.5분 | 8. 로파이·시티팝·칠, 기타 | [ALL TRENDING HINDI SONGS 2026...PLAYLIS…](https://www.youtube.com/watch?v=xI0IEWIxUBQ) 10,422,745회 |
| comfort space ♡ |  | 2026-04-12 | 82,200 | 12,898 | 287.5 | 130 | 20.4 | 360.0분 | 1. 수면·명상·힐링 | [go to sleep, you need it.](https://www.youtube.com/watch?v=Q5bDzSwLE8w) 3,379,954회 |
| ClassicalMusic … |  | 2026-04-22 | 75,800 | 12,540 | 200.0 | 165 | 27.3 | 81.3분 | 6. 피아노·클래식·연주곡 | [Adagio (Cello, Piano, Violin) - Beautif…](https://www.youtube.com/watch?v=wNpsTbqdBiw) 4,946,444회 |
| Quiet Tunęs |  | 2025-10-13 | 153,000 | 12,420 | 250.0 | 133 | 10.8 | 322.5분 | 1. 수면·명상·힐링 | [432Hz + 528Hz + 741Hz ∣ The Deepest Hea…](https://www.youtube.com/watch?v=Y5wQB1TTh2s) 8,589,203회 |
| Tom’s Jazz Loun… |  | 2026-04-25 | 72,600 | 12,143 | 200.0 | 107 | 17.9 | 75.4분 | 7. 재즈·보사노바 | [Just One More Drink -- Jazz Noir](https://www.youtube.com/watch?v=7gtIh5dF9Xk) 6,555,029회 |
| Milesora Lounge |  | 2026-04-14 | 68,200 | 10,813 | 162.5 | 197 | 31.2 | 77.4분 | 12. 커버·노래 부르기, 4. 카페·매장… | [Smooth Jazz & Soul R&B ∣ Soft Female Vo…](https://www.youtube.com/watch?v=YQHnz8VuazY) 2,380,272회 |
| Serenata |  | 2025-09-30 | 122,000 | 9,571 | 375.0 | 45 | 3.5 | 62.2분 | 기타 | [Popular OPM Hits 2026 🌿 New Filipino Pl…](https://www.youtube.com/watch?v=Ur4FFQT--Qw) 5,607,137회 |
| cozi_music |  | 2026-07-10 | 32,800 | 9,419 | 425.0 | 11 | 3.2 | 4.5분 | 기타, 8. 로파이·시티팝·칠 | [𓆩♡𓆪 𝑻𝑹𝑬𝑵𝑫𝑰𝑵𝑮 𝑺𝑶𝑵𝑮𝑺 𝑶𝑭 𝟐𝟎𝟐𝟔 𓆩♡𓆪 ∣∣ All t…](https://www.youtube.com/watch?v=85vOsUlmkjM) 472,957회 |
| Retrovivals |  | 2025-12-02 | 97,500 | 9,104 | – | 156 | 14.6 | 4.8분 | 14. AI 음악 | [Retrovivals - Kung Ako Nalang Sana - Bi…](https://www.youtube.com/watch?v=wbI70GOWw0U) 3,670,954회 |
| 80s Guitar Loun… |  | 2026-08-04 | 23,800 | 8,944 | – | 40 | 15.0 | 68.3분 | 6. 피아노·클래식·연주곡, 12. 커버·… | [Classic Love Songs ❤️ Timeless Acoustic…](https://www.youtube.com/watch?v=jDUH254gfs8) 583,619회 |
| 레코드 속 추억 | 예(레코드) | 2026-04-10 | 56,600 | 8,790 | 75.0 | 139 | 21.6 | 81.8분 | 기타, 9. 가요·발라드·트로트 | [“꽃길” “인연” “묻어버린 아픔” “마지막 연인” “사랑 참”🎸🔥조회…](https://www.youtube.com/watch?v=YBeWbO46Gtw) 1,225,792회 |
| Nature for the … |  | 2026-08-24 | 17,200 | 8,726 | – | 80 | 40.6 | 3.0분 | 1. 수면·명상·힐링, 6. 피아노·클래식… | [Sultry Saxophone Beats • Smooth R&B Jaz…](https://www.youtube.com/watch?v=PxeZARMnC-0) 14,362회 |
| Baby Bon Bon - … |  | 2026-07-28 | 24,700 | 8,642 | 12.5 | 21 | 7.3 | 11.4분 | 기타 | [Lola the Cow Song! (La Vaca Lola) 🐄 Ani…](https://www.youtube.com/watch?v=irzJfFIeggM) 42,977회 |
| Jasu LOFI |  | 2026-07-15 | 26,700 | 8,047 | – | 154 | 46.4 | 5.4분 | 8. 로파이·시티팝·칠, 기타 | [Patar Bashori ∣ পাতার বাঁশরী ∣ Lofi Ban…](https://www.youtube.com/watch?v=rgKNbCrC-cc) 8,123,568회 |
| Violinhop |  | 2025-09-19 | 103,000 | 7,858 | – | 160 | 12.2 | 71.7분 | 11. 힙합·R&B·EDM | [【Violin x Hip Hop Playlist】– My Truth i…](https://www.youtube.com/watch?v=TGYiJ5uoEtM) 2,307,847회 |
| Soulful Breaths… |  | 2026-04-06 | 51,500 | 7,838 | 237.5 | 196 | 29.8 | 39.2분 | 1. 수면·명상·힐링, 6. 피아노·클래식… | [Morning Cortisol Detox 🌿 Raag Bhairavi …](https://www.youtube.com/watch?v=cjNH2q4aBYc) 1,016,110회 |
| Ayan Studio |  | 2026-01-28 | 68,100 | 7,735 | 87.5 | 123 | 14.0 | 4.6분 | 기타 | [Na Bole Esechhi ∣ Male Version ∣ Heart …](https://www.youtube.com/watch?v=AQhp6kCxIRM) 2,177,071회 |
| NOXTUNE |  | 2026-07-29 | 21,000 | 7,433 | 37.5 | 17 | 6.0 | 11.1분 | 기타, 8. 로파이·시티팝·칠 | [Playlist For You To Create Fake Scenari…](https://www.youtube.com/watch?v=0gUwbTCQ78k) 6,635,761회 |
| 노래방 옆 만화방 |  | 2025-11-20 | 81,000 | 7,295 | – | 235 | 21.2 | 4.5분 | 10. 팝송·K팝·J팝, 9. 가요·발라드… | [정승환 & 박지원- 그 여자 (시크릿가든 OST) l [정승환의 노래방…](https://www.youtube.com/watch?v=QlOJ3HsA6Jk) 2,718,336회 |
| Frequencies of … |  | 2026-04-10 | 46,400 | 7,206 | – | 19 | 3.0 | 75.7분 | 1. 수면·명상·힐링, 6. 피아노·클래식… | [Cleanse Everything Draining You ∣ Heal …](https://www.youtube.com/watch?v=QNxiKUklOKQ) 952,294회 |
| Click Bollywood… |  | 2026-06-25 | 27,800 | 7,052 | 250.0 | 1,267 | 321.4 | 24.8분 | 3. 공부·집중·작업 | [Heartbreaking 💔 lofi mashup 🎶 slowed + …](https://www.youtube.com/watch?v=lXbnhKzEQl8) 1,281,980회 |
| ERRDAY GROOVE (… |  | 2025-11-05 | 81,700 | 7,045 | – | 226 | 19.5 | 4.1분 | 12. 커버·노래 부르기 | [엄정화 - 초대 [90's New Jack Swing Cover] (뉴…](https://www.youtube.com/watch?v=xNV5j1v53RY) 1,502,529회 |
| 국악딴따라 |  | 2026-05-19 | 36,000 | 6,980 | 125.0 | 51 | 9.9 | 3.7분 | 15. CCM·찬양·국악·동요, 1. 수면… | [국악딴따라 - 살아보니 그렇더라 (Official MV)](https://www.youtube.com/watch?v=FhNugHNh72s) 1,903,988회 |

## 8. 시청자 니즈 (성공 사례 1055개의 시청자 댓글 342,651개 — 채널 주인 댓글·도배 댓글 2,903개 뺌)

갈래는 낱말 규칙 (한 댓글이 여러 갈래). '더 알고 싶은 것'은 ① **요청**(다뤄 주세요·알려 주세요·궁금해요 — 다음 영상 주제 후보, 아래 8-1) 과 ② 물음표 질문(반문이 섞임, 8-2) 으로 나눠 인용한다. **어느 갈래에도 안 듦** 줄을 같이 볼 것 — 갈래 비율은 낱말 규칙에 걸린 몫이다. 모든 댓글(승인 영상 전부)에 유형 하나를 붙인 분포는 `comment_types.md` (사람이 분류한 표본 1,100개 + 규칙 — 2번이 가장 믿을 숫자).

| 갈래 | 댓글 | 비율 | 좋아요 합 |
|---|---|---|---|
| 좋은 점 — 영상 (도움·설명·정리·공감) | 567 | 0.2% | 3,541 |
| 감사·응원 (일반) | 6,707 | 2.0% | 46,195 |
| 더 알고 싶은 것 (질문·요청) | 914 | 0.3% | 11,119 |
| 아쉬운 점 — 영상 (제목·광고·길이·정보 오류·목소리) | 417 | 0.1% | 2,488 |
| 반박·불만 — 의견 다름 (내용) | 218 | 0.1% | 1,354 |
| 정치·사회 (영상과 무관한 의견) | 131 | 0% | 2,090 |
| 경험 공유 (내 이야기) | 2,527 | 0.7% | 40,108 |
| 구독·다음 기대 | 427 | 0.1% | 1,602 |
| **어느 갈래에도 안 듦** | 331,834 | 97% | 2,206,526 |

### 좋은 점 — 영상 (도움·설명·정리·공감) — 좋아요 많은 댓글

- 👍229 [#14] “처음에 크레이지 아케이드 소리 들리길래 영상 잘못 들어온 줄 알았네 ㅋㅋㅋㅋ 하 첫 곡부터 마지막 곡까지 너무 레전드라서 쉬는 날에 엄청난 힐링하고 갑니다 ㅠ”
- 👍189 [#786] “조선힙합 멜로디도 좋지만 모든 곡들의 가사가 너무 마음에 와닿습니다. 좋은 노래 만들어줘서 감사합니다. 위안이 되는 따뜻한 노래들.”
- 👍150 [#428] “저는 지금 이 순에도 위태로운 제 자신을 부여잡고 눈물을 흘리며 하루하루를 버티는 중년의 여성입니다 삶을 내려 놓고 싶은 순간이 너무 많지만 생명의 질긴 끊이 저를 버텨주네요 사실 용기도 없습니다 젊은 시절은 부모님 상처드리기 싫어 버티는 심정으로 살았고 지금은 제 반려견 걱정에 버티고 있습니다 얼마나 더 버틸수 있을까요..눈을 뜨고 하루를 대하는 저의 일”
- 👍124 [#542] “스타즈 오늘 둘다 레전드네 ㄷㄷㄷ❤❤❤❤”
- 👍108 [#260] “안녕하세요, 오늘의 플리님! 저는 도덕 수업에서 선플 달기 활동을 하고 있는 중1 학생입니다. 영상 정말 잘 보고 있어요. 항상 좋은 영상 올려주셔서 감사합니다. 좋은 하루 보내세요”
- 👍78 [#14] “디지몬 어드벤처, 이누야샤, 달빛천사, 아따맘마, 피치피치핏치, 카우보이 비밥, 나루토, 개구리 중사 케로로, 캐릭캐릭 체인지, 원피스 등등... 이런 레전드 꿀잼 애니메이션들을 감상할 수 있었던 90년대생들은 진짜 선택받은 어린이들 세대였던 것 같습니다.”
- 👍60 [#660] “힐링음악님 요즘 세로운 영상 찾아 올리시는 라 수고가 많으시죠? 덕분에 이렇게 좋은 영상을 보네요 고맙습니다🙏 (어디로 부터 그대는 왔는가) 전 이 가사가 유난히 좋더라구요^^”
- 👍59 [#12] “우리가 고3만 아니였다면 맞춰갈 수 있는 시간이 있었을텐데 정말 아쉽고 힘들다 벌써 1달이 넘었는데 단 하루도 널 잊은적이 없어 살면서 사랑을 알려줘서 고마워 지금은 너에게 아무것도 안하는게 돕는거라고 생각해서 수능 끝나고 연락할거야 우리 입시 성공해서 다시 만나자 영원한건 없어도 다시 만난다면 평생 사랑할게”

### 감사·응원 (일반) — 좋아요 많은 댓글

- 👍1,687 [#428] “26년 병원 검사를 마치고, 어제부터 1년을 선물 받았습니다. 안전한 1년이길 🙏하면서 , 오늘은 좋아하는 음악을 들으며 가만히 쉬어 봅니다. 이런날 음악이 친구가 되어주고, 위로가 되어줍니다. 클래식을 잘 모르지만, 저는 마음으로 느껴지는 걸 중요하게 생각하며 듣습니다. 귀로만 듣는게 아니라 몸과 마음을 어루만져 주는 그 찰나의 순간을 느끼는 것이지요. ”
- 👍744 [#1023] “김간지한테 고맙습니다 해야지”
- 👍529 [#196] “진짜 많이 보고싶다. 내 고등학생 생활이 전부 너라서 너 말고는 아무것도 안보였던 시기엿어. 고등학교 동안 나한테 과분한 사랑 주고 항상 내 편이 되어줘서 너무너무 고마워 우리 성인되는 날에 같이 첫 술 마시자고 했었는데 기억나? 그 약속 이제는 못 지키겠다. 헤어질 때 너무 아팟고 너와의 좋았던 기억들이 너무 많은데도 그 힘들었던 기억들이 계속 괴롭혔어.”
- 👍528 [#428] “번개탄 피워놓고 죽으면 다끝이지 않을까? 하는 마음을 떨쳐버리고 마음추스린지 일주일 입니다 삶에 무게너무 무겁지만 그래도 살아가는것이 맞겠지...하는생각에...모두들 힘내보아요”
- 👍399 [#1005] “시험기간이라 그런지 요즘 영상이 많이 올라오네요 시험 화이팅 하세요”
- 👍252 [#232] “이 플리 듣고 자전거 타면서 수많은 지뢰를 피해서 겨우 탈북했네요~감사합니다 근데.. 앞에 누가 총을 들고있네요?”
- 👍250 [#765] “배경화면에 끌려서 클릭 했다가 환상적인 연주에 빠져들어서 맘을 쓸어내리며 감상해요.. 아름답고 애절한 연주 감상할 수 있게 해주셔서 감사합니다♡”
- 👍244 [#513] “마음을 행복하게 해주셔서 감사드립니다. 기쁨이 몽글몽글😊 건강해지는 기분입니다. 모두모두 행복하시기를... 좋은 선물 주시는 운영자님도 행복하시고, 좋은 일이 가득가득하시기를😊”

### 더 알고 싶은 것 (질문·요청) — 좋아요 많은 댓글

- 👍6,477 [#438] “대체 뭔노래가 나올까 궁금해서 들어왔습니다”
- 👍1,047 [#399] “개발할 때마다 듣습니다; 많이 올려주세요”
- 👍208 [#196] “여전히 잊지 못하였습니다. 당신이 나의 이상형이라서, 당신이 나의 첫사랑이라서, 끝난 관계임에도 나에게 잘 해줘서, 너무 착한 사람이라서, 귀여운 걸 본인만 몰라서, 허세 같은데 싫지 않은 적은 처음이라서, 영원을 약속하고 싶게 만든 사람이라서.. 이유는 수백 개 수천 개지만 그 정도로 당신이 좋은 이유가 수두룩 빽빽한데 이 이야기를 전할 수가 없습니다 이”
- 👍88 [#660] “김호중 테너의 활동 영상 발굴해서 많이 많이 올려주세요. 이미 완성된 테너 김호중 감동입니다.”
- 👍88 [#660] “기다렸습니다 김호중 테너님 공연 많이올려주시면 좋겠 습니다 영상감사합니다 🎉🎉🎉”
- 👍77 [#811] “할렐루야 주님께 영광돌립니다 . 호주에서 5년 살고 컴백한 시골사역 사모예요. 한국 정읍시 오주길 ~ 작은마을 개척교회사모입니다. 저희는 교회 사역에 필요한 야채 식료품 밭에서 직저자배해서 성도님들 섬기며 네팔에서 3월에 온 자매 형제님 선교도합니다. 한글공부 집중 중입니다 요즘 시골에 한국사람 없어 전도가 쉽지 않은데 네팔 🇳🇵 성도님들 제자삼아 성장시키”
- 👍76 [#1034] “파란색으로 블루베리도 만들어주세요!!!!”
- 👍69 [#924] “나중에 브금 매쉬업버전 말고 각각 올려주시면 안될까요”

### 아쉬운 점 — 영상 (제목·광고·길이·정보 오류·목소리) — 좋아요 많은 댓글

- 👍632 [#207] “현재 08년생 입니다.. 벌써 마지막 10대의 절반이 지났다는게 믿겨지지 않네요. 어릴때 저녁밥 먹기 전 동네 친구들과 술래잡기 하던게 엊그제 같은데 저에겐 항상 멀게만 느껴졌던 20대라는 현실을 곧 마주할 생각을 하니 솔직히 현실감이 없습니다.. 아직 추억도 많이 없고 즐기지못한게 많은거 같아 맨날 옛날로 돌아가고 싶다는 생각을 하곤 하는데 몇년 뒤엔 오”
- 👍70 [#766] “18년을 함께한 우리 고양이가 고양이별로 떠난지 4일째 되는 밤입니다. 집안 모든 곳이 냥이와 함께한 곳이라 가는 곳마다 눈물이 납니다. 마치 그곳에 앉아 있는 것 같아 나도 모르게 두 손을 뻗곤 합니다. 원없이 사랑한 것 같았는데 보내고나니 아쉬움과 후회만 밀려옵니다.”
- 👍64 [#669] “광고가 계속 나와요😢😢”
- 👍57 [#794] “가사는 모르지만, 애절하면서 흡인력 있는 목소리가 너무 좋습니다.”
- 👍51 [#660] “오늘 김호중 가수의 노래를 이것저것 찾아 듣고 있는데 이 노래를 듣게 되네요. 김호중 테너의 목소리가 너무 듣기 좋습니다. 이애숙님과 두 분 함께 부르는 노래가 완전 멋지네요. 올려주셔서 감사합니다 ~”
- 👍49 [#455] “남편의 계속 반복되는 외도로 어린아들 둘 데리고 이혼한지 9개월 눈물 흘릴 여유조차 없이 살다가 노래들으려고 켠 유튜브에서 우연히 발견한 노래들.. 마음을 보듬어 주는것같은 따뜻한 목소리에 눈물이 터져 울고 위로받고 갑니디 원래 안달지만 꼭 달고싶었어요. 오래 노래해주세요. 자주와서 들을게요. 너무 고맙습니다.”
- 👍45 [#650] “요즘 유튜브나 여러 플랫폼에서는 AI 기술을 활용해 특정 가수의 창법이나 음색을 학습시킨 커버 곡들이 정말 많이 쏟아지고 있네요. 특히 전통적인 록 발라드나 트로트 메들리 같은 영상 중에는 사람이 직접 부른 것처럼 정교하게 만들어졌지만, 실제로는 AI 목소리 모델을 입혀서 기계적으로 양산된 콘텐츠들이 꽤 많습니다. 음색이나 부르는 스타일이 지나치게 정형화되”
- 👍45 [#739] “AI로 작업했더라도 주인장 음악력 진짜 높은 듯. 듣기 편안한데 지루하지 않음.”

### 반박·불만 — 의견 다름 (내용) — 좋아요 많은 댓글

- 👍155 [#108] “선곡말도안됨”
- 👍142 [#984] “아 메이플 관련 브금이랑 영상만 보면 저때로 돌아가고 싶다라는 생각이 계속 든다.. 무더운 여름방학 집에 에어컨도 없어서 방에서 선풍기 하나로 동생과 싸우고 한대 있는 컴퓨터로 너가 몇분을 더했니 어쨌니 그러다가 게임 금지 당하고.. 동생보다 30분이라도 먼저 일어나서 몰래 게임하고.. 지금은 동생도 나도 너무 많이 커버렸구나. 어렸을때 형이란 이유도 동생”
- 👍132 [#215] “-내가 약조하마.너를 지켜주겠다고. 그렇게 다정히 말씀하시던 든든한 나의 님은, 지금 풀숲에 쓰러져 간신히 숨만 내쉬고 계신다. -상공, 제발 숨만 쉬십시오. 제가 어떻게든... -연화야. 상공의 손이 나의 손은 따스히 잡아온다.그 온기가 서글프도록 따뜻해서, 심장 한편이 저릿하게 아려온다. -아닙니다, 그러지 마십시오. 지금이라도 의원을 부르면.. -너도”
- 👍113 [#291] “제목을 보자마자 한사람이 떠올라서 홀린듯이 클릭해버렸어요. 이런 플리 잘 안들을 것 같아서 그냥 터놓고 말할게. 중학교 때 처음 만난 언니. 정말 예쁘고, 멋지고 빛이 나서 이보다 주인공 같은 사람이 있을까 싶은 사람. 정병 와서 새벽에 연락해도 꼬박꼬박 답장해주고 내가 힘들때 옆에서 참 많을 위로를 해주었던 건 정말 아직도 고마워. 내가 죽지 않고 이렇게”
- 👍91 [#232] “탈북할 땐 어떤 노래를 듣는걸까 하고 왔는데 첫곡듣고 어이없어서 터졌네 ㅋㅋㅋㅋ 무슨 관련이야”
- 👍47 [#239] “왜 우리는 아는 사람들에게 위로받지 못하고 모르는 사람들에게 인터넷상에서 위로를 받는 걸까요 힘들다고 말하는 게 부끄러운 것도 아닌데 다른 사람들의 댓글을 보며 와.. 이런 사람들도 있구나 저런 사람들에 비하면 나는 행복한 거구나..라고 위안 삼으며 다시 또 지옥같이 지치는 일상으로 돌아가는 사람도 있고 다른 사람들의 댓글을 보며 위로를 받고 살아갈 용기를”
- 👍45 [#660] “너무잘한다 이런인재를 순간의 실수에 너무오래 가둬놓네 엄청난죄 지은 사람들도 다풀어주고 아예법의재제도 안하면서 국보급 가수한태는 왜그리 독한지 참어이없는 사법부다”
- 👍38 [#794] “80을 넘는 음악을 아는 사람도 아닌데 아득한 옛날 그리움을 노래하는 것 같네요...”

### 정치·사회 (영상과 무관한 의견) — 좋아요 많은 댓글

- 👍623 [#766] “사랑하는남편이 하늘나라가신지 두달하고십사일째입니다~ 제마음을 위로해주네요~”
- 👍522 [#191] “9:06 중국인들 탑 랩 파트, 학교를 안 갔어, 오빠오삐옵, 싸이노래 개좋아함”
- 👍85 [#660] “이런노래들으니 이나라가 얼마나 귀한지 모르겠습니다 망하는나라 한순간 우리가 모두 힘내어 지켜야 합니다”
- 👍32 [#765] “멎있는예술의나라인데~전쟁하지않으면좋겠다두나라가파괴되는게너무아깝다~제발세계펑화를후손들위해~음악이웅장하고뭉클합니다”
- 👍26 [#94] “난 한국인인데 한국 사람들한탠 이런 이미지가 없단게 너무 슬프다 러시아나 다른 나라들의 사람들이라 하면 다들 각자의 신비롭고 그런 이미지들이 있는데 한국인이라고 하면 그냥 kpop이니 뭐니 하는 그런 재미없고 오글거리는것들밖에 없으니까 너무 아쉬움 정부가 한국콘텐츠진흥원같은거까지 만들어가면서 지원하지만 않았어도 이렇겐 안됬을거같다 그냥 차라리 스타크레프트 ”
- 👍24 [#20] “그냥 케이팝,드라마,예능 다 2010년대 이후로 이제 옛날같지않더라 케이팝으로 유명하던 우리나라가 더 이상 그냥 챌린지하는 노래밖에 안나오고..어제 청룡?보니까 확실히 전과 다름 연말에 가족끼리 시상식보는 감성도 사라진듯 다 모르는것들만 나오고 옛날엔 드라마도 지금보면 ㄹㅈㄷ인거 많이 나오고 예능도 신서유기,무도 등등 지금보면 ㄹㅈㄷ인거 많았는데 지금 보면”
- 👍23 [#645] “이재성..가장 뛰어난 싱어송라이터였는데.. 고독한DJ라는..노래불렀다가....전두환정권에서.방송금지당해..최전성기..87년에...갑자기TV에서.사라졌고.. 라디오에서도 이재성 노래를 10년동안 들을수 없었음.”
- 👍20 [#15] “영상이 기괴하다더니 진짜 그렀네~ ㅠㅠ 외국인들은 예술로 보는게 놀랍다 한국이 인신제사에 쓰이려나”

### 경험 공유 (내 이야기) — 좋아요 많은 댓글

- 👍2,673 [#196] “야 보고싶어 내 생일에 연락 왜 안했냐 너 밥 한끼 더 좋은거 먹으라고 네가 기념일마다 줬던 토스 기프티콘 일부러 안 썼어 너한테 입금 됐냐 돈 하나도 안 아까운데 그냥 그렇다고 내 계좌 비밀번호 우리 만난 날이야 내 노트북 비밀번호도 우리 만난 날이야 훔쳐가도 되는데 홍대에서 이제 공연해? 아직인가 너한테 기타 쳐달라고 했던 노래가 하필 이 영상 첫 노래”
- 👍2,513 [#207] “내가 왜 고3일까… 평생 안 올 줄 알았는데 ㅠㅠㅠㅠ 뽀로로 너랑 걱정없이 놀 때가 너무 그리워…”
- 👍1,898 [#207] “뉴스에서 고등학생 자살율 얘기할때 진짜 이해 안됐는데 막상 고등학생 되니까 내가 그 경계에 서있네”
- 👍1,308 [#438] “나도 모르게 "아 지랄 ㅋㅋ" 하면서 들어왔네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 아 미친”
- 👍1,252 [#911] “영상 내려가서 내가 멘헤라될뻔”
- 👍1,217 [#1005] “하트누르면 모두들 행복해지고 시험 잘 볼 거임!! 나도 포함”
- 👍1,132 [#196] “이 세상 단 둘만 가진 기억인데 아까워서 어떻게 잊나요 내가,”
- 👍1,069 [#239] “요즘 옥상문이 잠겨있네요 더워서 그런가 벌써 네 건물 가봤는데 잠겨서 죽고싶은데 마음데로 죽지도 못하네요 얼마전에 울다가 깨닳았어요 아 나 안죽고싶은데.. 내가 죽고싶은게 아니라 지금이 너무 힘들어서 차라리 죽고싶은거구나 아 행복해지고 싶은거구나 죽고싶은게 아니라 행복해지고 싶은데 행복이 저는 너무 어려워요 행복하고싶었던거라는 생각이 들지마자 너무 서러워서”

### 구독·다음 기대 — 좋아요 많은 댓글

- 👍110 [#786] “듣다보니. 가슴에 스며들어 구독하고. 계속 듣게 되네요 60후반이지만 요즘 젊은이들 조선힙합이 꽂치네요 좋은음악. ~^^❤❤❤”
- 👍105 [#660] “김호중님의 무대가 기다려집니다”
- 👍75 [#948] “슬프고도 정화된 아름다운 선율 듣자마자 바로 구독하고 영혼의 단짝 친구와 공유했습니다 평생을 추구해온 제 삶의 궤적을 위로해주는 선율과 가사는 눈감고 들어도 한마디 한마디가 너무나 아름답습니다 저를 숨기고 제 슬픔을 숨기고 제 진실을 숨기고 모두에게서 옹달샘처럼 숨어있는 제 영혼이 공감받고 위로받는 듯 했습니다 이 채널을 준비해주신 그대에게 감사를 전하고자”
- 👍48 [#699] “구독박고 갑니다 태어나서 이렇게 섹시한 남자 첨이에요 허남준땜시 잠이 안와요 매일 유투브로 찾아봐도 질리지 않아요 ㅋ”
- 👍42 [#836] “썸녜일도 느낌.있고.음악도 좋네요 ! 음악은 ai로 만드신건가요?궁금. 그림도 왠지 직접그리신듯 구독하고가요😊”
- 👍32 [#275] “이별 벌써 20년째 저는 가족 반대 때문에 헤어진 한남자 잊지 못합니다 지금 도 그사람 잊지 못합니다 아니 영윈히 기다려요 이노래가 아퍼요 그사람 마음 같아😢”
- 👍18 [#511] “아침찬양에 너무 잘 맞는 목소리와 은혜입니다. 첫곡듣고 바로 구독했습니다”
- 👍17 [#642] “첨들어봤는데 넘좋아서 바로 구독했어요. 50대 주부~😊”

### 8-1. 더 알고 싶은 것 ① 요청 — 다뤄 주세요·알려 주세요·궁금해요 (686개 중 좋아요 순, 영상마다 2개까지)

- 👍6,477 [#438] “대체 뭔노래가 나올까 궁금해서 들어왔습니다”
- 👍1,047 [#399] “개발할 때마다 듣습니다; 많이 올려주세요”
- 👍88 [#660] “김호중 테너의 활동 영상 발굴해서 많이 많이 올려주세요. 이미 완성된 테너 김호중 감동입니다.”
- 👍88 [#660] “기다렸습니다 김호중 테너님 공연 많이올려주시면 좋겠 습니다 영상감사합니다 🎉🎉🎉”
- 👍77 [#811] “할렐루야 주님께 영광돌립니다 . 호주에서 5년 살고 컴백한 시골사역 사모예요. 한국 정읍시 오주길 ~ 작은마을 개척교회사모입니다. 저희는 교회 사역에 필요한 야채 식료품 밭에서 직저자배해서 성도님들 섬기며 네팔에서 3월에 온 자매 형제님 선교도합니다. 한글공부 집중 중입니다 요즘 시골에 한국사람 없어 전도가 쉽지 않은데 네팔 🇳🇵 성도님들 제자삼아 성장시키”
- 👍76 [#1034] “파란색으로 블루베리도 만들어주세요!!!!”
- 👍69 [#924] “나중에 브금 매쉬업버전 말고 각각 올려주시면 안될까요”
- 👍68 [#579] “8주된 뱃속의 아기를 와이프와 보내고 상심이 큰 어제와 오늘이었습니다. 와이프에게 어떻게 하면 힘이 될 수 있을까 하다 우연히 듣게 되었는데, 마치 고즈넉한 숲 속 궁전에서 여유로운 하루를 맞이하는 느낌을 주는 노래 같아 하루 종일 듣고 있습니다. 힘 내볼게요. 앞으로도 좋은 노래 많이 올려주세요”
- 👍62 [#579] “최고에요! 제 브이로그 배경음악으로 클래식을 많이 쓰는데, 혹시 출처표시하고 bgm으로 쓸 수 있을까요? 안되더라두 괜찮으니 편하게 알려주세요! 좋은 음악 감사합니다! :)”
- 👍54 [#404] “아 진짜 주인장 제발 이 플레이리스트 더 길게 만들어주세요 제발요”
- 👍47 [#836] “트랙리스트 위에있는 글은 주인장님이 써내려간 글귀일까요? 너무 멋져요.. ❤ 혹시 책의 한 소절이라면 제목을 알려주실 수 있으실까요😊”
- 👍45 [#119] “첫번째 나온 노래 너무 좋은데 가수랑 제목좀 알려주세요.. 아무리 찾아도 안나와요 😢”
- 👍41 [#682] “혹시 투어스 노래 모음 만들어 주실수 있나여..?”
- 👍35 [#32] “개조아요 타임라인 올려주세요”
- 👍33 [#826] “우선 이런 질문드려 죄송합니다. 제 생애 최고의 전율을 느꼈습니다. 그래서 무지한 질문을 드리더라도 용서부탁드립니다. 유튜브 보다가 떠서 감상하게 되었는데, 어느분이 부르신걸까요? 혹시 설명란에 있는것처럼 ai로 만드신 걸까요?”
- 👍32 [#323] “저런 얼굴하고 물어보면 어 아니 너가 훨씬 나아 가 나올듯 노래 리스트가 너무 좋아유 계속 올려주세요!”
- 👍32 [#940] “호르몬제는 무서워서 못 먹고 영양제 알아보던 중이에요. 한 번 깨면 다시 잠드는 게 너무 힘들어요. 흡수 잘 된다는 리포좀멜라토닌에 감태·레몬밤·가바 같이 들어간 각성완화제 먹고 있는데 엄청 센 건 아닌데 누우면 좀 차분해지긴 하더라고요. 같은 나이대 분들 어떻게 넘기시는지 궁금하네요.”
- 👍30 [#223] “진짜 ' '서운 이야기 띵!... 똥!... 유튜브 댓글에 알람이 떴어. "저 브라질 펑크에 관심이 많은데 이 분이 브라질 펑크 부른거만 모아서 영상 만들어 주실 수 있나요?" 그냥 자기가 듣고 찾아서 모음 딸깍하면 되는 황당한 요구를 하다니.. 저 사람은 너무 '오만'해 그 때.. '궈바오러우'가 나타났어”
- 👍30 [#637] “55분에 시작하는 노래 가수와 제목좀 알려주세요ㅜㅜ”
- 👍29 [#108] “진짜 댓글 앵간하면 안쓰는데 이거 조합 ㅈ됨 너무좋다 여자여자스러운데 당당하고 자존감높은 여자 플리임 이런거 너무 좋아서 맨날 들을거 같음 더 만들어주세요❤”
- 👍29 [#948] “아다지오 평소에 사랑헸던 곡입니다...윌리엄님의 올리신곡은 또다른 멋으로 다가옵니다.사랑합니다.축복합니다.감사합니다.늘 좋은 음악.아름다운음악 부탁드립니다. 건강하세요”
- 👍27 [#924] “지킬만 분리해서 올려주세요 따로도 듣고 싶어요”
- 👍23 [#183] “노래다운받는방법 알려주세요”
- 👍23 [#620] “안녕하세요!오산중학교에다니는 3학년학생입니다.기술시간에 선플달기를 하고있는데 요즘 점점여름이 다가오는시기여서 그런지 이영상이 알고리즘에 떴더라고요!시원한 여름플리너무 잘만들어주셔서 잘들을것같아요!모두 시원한여름보내시고 앞으로더 좋은영상 많이 만들어주세요💕”
- 👍21 [#401] “너무 시원하고 감동적인 노래 잘듣고 갑니다 앞으로도 더욱 많은 노래 올려주세요”
- 👍20 [#440] “순천부영초등학교 이지인입니다 이챌린지을많이봤어요 이노래를듣으면 우울할때기분이 좋아져서이노래에 댓글을달았어요앞으로 신나는노래많이 올려주세요”
- 👍20 [#471] “낮엔 피곤한데 밤엔 또렷해서 멜라토닌 알아봤네요. 요즘 부쩍 잠이 얕아지고 감정 기복에 잠까지 설쳐요. 일반 멜라토닌은 흡수가 별로라길래 리포좀멜라토닌에 가바·테아닌까지 든 각성완화제로 바꿔봤는데 엄청 센 건 아닌데 누우면 좀 차분해지긴 하더라고요. 같은 또래 워킹맘분들은 어떻게 관리하시나 궁금해요.”
- 👍20 [#930] “아들건강하게 해주시고 대운 부탁드립니다❤❤❤❤❤❤❤”
- 👍19 [#637] “1시 9분 가수좀 알 수 있을까요?? 노래제목좀 부탁드려요 🙏”
- 👍19 [#918] “멜론에도 올려주세요 제발”
- 👍18 [#869] “혹시 실제 부르시는건지 AI 인지 궁금하네요 너무 은혜로와서~ 너무 잘하셔서~~”
- 👍17 [#628] “2번째 노래 제목 좀 부탁드립니다. 너무 좋아요”
- 👍15 [#260] “노래 제목 부탁드립니다 아재라서 하나도 몰라요 ㅜㅡㅜ 40중반 아저씨의 간곡한 부탁입니다 ~!!!”
- 👍15 [#539] “첫번째 곡이랑 비슷한 노래 추천 좀 해주세요ㅠ 첫 곡이 너무 좋은데 찾아봐도 없어요ㅜㅜ”
- 👍14 [#715] “와 첫번째 노래 궁금하다 좋으네”
- 👍14 [#806] “우연히 듣게 됐는데 너무 상큼하고 너무 행복해져요. 제목도 알고 싶은데.. 방법 없을까요?”
- 👍14 [#836] “가사하나 없는 플리인데.. 들으면 마음이 진짜 편안해져요ㅎㅎ 적당히 잔잔하면서 넘 좋아요ㅎㅎ 몇주간 이 채널의 플리만 계속 무의식적으로 들었네요❤️ 좋은 플리 많이 올려주세요❤️”
- 👍13 [#979] “와 썸네일 지나가듯이 봤는데 무언가 잘못된 썸네일을 봤는데...라는 느낌을 받음과 동시에 새로고침을했는데 너무 궁금해서 헤매고 다녔다”
- 👍12 [#380] “이런 느낌으로 좀 더 만들어주세요ㅠㅠ 너무 제스탈 인생리스트!!”
- 👍12 [#644] “노래 듣다가 나도모르게 구독 좋아요 누르게됨 좋은음 많이 올려 주시길~~58년생 할배입니다 ^^”

### 8-2. 더 알고 싶은 것 ② 물음표 질문 (반문이 섞임 — 좋아요 순, 최상위 댓글)

- 👍208 [#196] “여전히 잊지 못하였습니다. 당신이 나의 이상형이라서, 당신이 나의 첫사랑이라서, 끝난 관계임에도 나에게 잘 해줘서, 너무 착한 사람이라서, 귀여운 걸 본인만 몰라서, 허세 같은데 싫지 않은 적은 처음이라서, 영원을 약속하고 싶게 만든 사람이라서.. 이유는 수백 개 수천 개지만 그 정도로 당신이 좋은 이유가 수두룩 빽빽한데 이 이야기를 전할 수가 없습니다 이”
- 👍56 [#239] “어릴 땐 어른이 부러웠습니다. 아무거나 다 할 수 있는. 하지만 정작 어른이 된 저는 삶에 휩쓸려 무뎌지고 부서진, 그런 사람이라는 걸 깨닫게 되었습니다. 우리 다시 돌아갈 수 있을까요? 아무 걱정 없이, 아무 생각도 안 하는 그때로”
- 👍32 [#660] “오 😮이 반가운 영상 어떻케 오늘에야 만나죠? 언제인가요? 김호중 코리아나 이애숙님. 이죠?”
- 👍31 [#905] “언제 상송이 나오죠?”
- 👍16 [#12] “제 연인이 표현을 잘 안하는 편이에요 근데 저는 표현도 많이 하고 남자지만 불안형이거든요 연애초긴 하지만 그녀의 마음이 어떤지 연락도 잘 안될땐 뭘 하는지도 궁금하고 불안하고 그래요 어떻게 고칠까요?”
- 👍15 [#623] “뮤비좋은데 라이브 가능한가요?”
- 👍15 [#827] “혹시 첫 번째 노래 가수를 있을까요? 검색으로는 안 나와서요ㅜㅜ 가사를 보고 싶은데ㅜㅜ”
- 👍15 [#907] “안녕하세요~ 혹시 이 음악을 행사 진행 중에 사용하기 위해 다운로드할 수 있을까요? 감사합니다🙏🏼너무 좋아합니다❤️‍🔥”
- 👍13 [#308] “와~~ 정말 가슴이 뻥 뚫리고. 머리가 신선해집니다 어쩜 저런 보물이 있을까요? 수연양!!! 사랑합니다 할아버지 할머니랑 영원히 행복하세요~~~!!”
- 👍13 [#689] “가수가 어떻게 되나요?”
- 👍12 [#646] “혹시 배경 어딘지 정보알수있을까요?”
- 👍12 [#783] “혹시 흘러나오는 여자 목소리 가수이름 알수있을까요? 엄마가 궁금해하셔서요ㅠ”
- 👍11 [#416] “집사람이 좋아하네요 혹시 악보를 구입할수있을까요??”
- 👍11 [#911] “혹시 저 그림 웹툰이면 제목 알수있을까요?”
- 👍10 [#175] “이 노래를 들으면서 떠오르는 계절은 어느 계절인가요? 봄, 여름, 가을, 겨울 중 하나를 골라주세요. 🍂”
- 👍10 [#313] “영상의 사진이 어디서 나온 것인지 알 수 있을까요?”
- 👍10 [#734] “혹시 기뻐하며 경배하세 MR 어디서 구할 수 있을까요? 딸아이 결혼식에 혼주 입장곡으로 쓰고 싶어서요~”
- 👍8 [#196] “저두 가슴이 미어지는 사랑을 해보고싶어용 이성적인 감정은 언제 생기는건가요? 아무리 봐두 친구로밖에 안느껴지는데…”
- 👍8 [#404] “사진 출처 어딘지 알수있을까요?”
- 👍8 [#455] “첫번째 노래 가수 이름 알수있을까요?”

### 8-3. 아쉬운 점 — 영상에 대한 비판 (좋아요 순, 답글 포함)

- 👍632 [#207] “현재 08년생 입니다.. 벌써 마지막 10대의 절반이 지났다는게 믿겨지지 않네요. 어릴때 저녁밥 먹기 전 동네 친구들과 술래잡기 하던게 엊그제 같은데 저에겐 항상 멀게만 느껴졌던 20대라는 현실을 곧 마주할 생각을 하니 솔직히 현실감이 없습니다.. 아직 추억도 많이 없고 즐기지못한게 많은거 같아 맨날 옛날로 돌아가고 싶다는 생각을 하곤 하는데 몇년 뒤엔 오”
- 👍70 [#766] “18년을 함께한 우리 고양이가 고양이별로 떠난지 4일째 되는 밤입니다. 집안 모든 곳이 냥이와 함께한 곳이라 가는 곳마다 눈물이 납니다. 마치 그곳에 앉아 있는 것 같아 나도 모르게 두 손을 뻗곤 합니다. 원없이 사랑한 것 같았는데 보내고나니 아쉬움과 후회만 밀려옵니다.”
- 👍64 [#669] “광고가 계속 나와요😢😢”
- 👍58 [#20] (답글) “진짜요..ㅜㅜ다시는 이런 케이팝만의 분의기를 못 본다는게 너무 아쉬움…”
- 👍57 [#794] “가사는 모르지만, 애절하면서 흡인력 있는 목소리가 너무 좋습니다.”
- 👍51 [#660] “오늘 김호중 가수의 노래를 이것저것 찾아 듣고 있는데 이 노래를 듣게 되네요. 김호중 테너의 목소리가 너무 듣기 좋습니다. 이애숙님과 두 분 함께 부르는 노래가 완전 멋지네요. 올려주셔서 감사합니다 ~”
- 👍49 [#455] “남편의 계속 반복되는 외도로 어린아들 둘 데리고 이혼한지 9개월 눈물 흘릴 여유조차 없이 살다가 노래들으려고 켠 유튜브에서 우연히 발견한 노래들.. 마음을 보듬어 주는것같은 따뜻한 목소리에 눈물이 터져 울고 위로받고 갑니디 원래 안달지만 꼭 달고싶었어요. 오래 노래해주세요. 자주와서 들을게요. 너무 고맙습니다.”
- 👍45 [#650] “요즘 유튜브나 여러 플랫폼에서는 AI 기술을 활용해 특정 가수의 창법이나 음색을 학습시킨 커버 곡들이 정말 많이 쏟아지고 있네요. 특히 전통적인 록 발라드나 트로트 메들리 같은 영상 중에는 사람이 직접 부른 것처럼 정교하게 만들어졌지만, 실제로는 AI 목소리 모델을 입혀서 기계적으로 양산된 콘텐츠들이 꽤 많습니다. 음색이나 부르는 스타일이 지나치게 정형화되”
- 👍45 [#739] “AI로 작업했더라도 주인장 음악력 진짜 높은 듯. 듣기 편안한데 지루하지 않음.”
- 👍40 [#765] “너무 너무 멋진 분위기 취할수있는 선율. 감흡! 늦은밤까지 이어질듯요 무한반복~~😊😊😊”
- 👍38 [#1023] “그저 사막을 지나 가는 것 같던 20대 나의 맘 속에 요술 왕자 당신은 누구신가요 아무도 모르지만 탱탱볼을 던지고 사라지는 꿈을 쫓다 지치길 지나 나의 미래에게 Waiting for your calling back 반복되는 감정의 미끄럼틀 그리고 오늘 아침 미국에서 만나는 신나는 음악, 잘못된 인생 술탄 오브 더 디스코는 나의 청춘 고마워요, 술탄 혼자 외”
- 👍35 [#511] “두분다 목소리가 너무 좋으셔서 자꾸 듣게되요~찬송가도 너무좋지만 목소리가 엄청 편안하고 부드러워요”
- 👍34 [#812] “제 노래 스퇄일 최고입니다😊 가수 목소리 좋고 선곡도 최고 운동할때 이어폰 귀에 꼽고❤ 한시간 넘게 운동하는데 지루함 없이 운동합니다 대박 기원합니다🎉🎉🎉🎉🎉”
- 👍33 [#691] “역시나 보이스칼라가 독보적입니다.언제들어도 너무 감동입니다. 영상편집이 정성이 많이 들어간게 보이네요,보는 내내 웃게 되네요.👏👏👏👏👏👏👏👍👍👍김호중 테너 너무보고싶네요.무대에 서신 모습 빨리 보고싶어요”
- 👍27 [#15] (답글) “이 뮤직비디오를 보이콧해 주세요. 이 영상과 제니의 다른 몇몇 영상에는 자막이 없습니다. 청각 장애가 있는 사람으로서, 가사와 노래 속에서의 위치까지 완전히 외우기 전까지는 자막 없이 뮤직비디오를 보면서 노래 내용을 이해하기가 어렵습니다. 제니는 돈도 많고 팀도 큰데, 뮤직비디오에 자막을 넣을 사람을 구하는 건 식은 죽 먹기일 텐데요. 이건 무지한 행동입니”
- 👍26 [#12] “가장 헷갈린 시기 같아요 잘하고 있다고 누가 꼭 안아주면 좋겠어요 열심히 살았는데 아쉬움이 항상 남네요”
- 👍26 [#399] “이거 들으면서 학원 숙제 베꼈는데 밀려써서 걸렸습니다 조심하세요”
- 👍23 [#632] “청춘은 서툴기에 그 자체로 빛난다. 완벽하다면 너무 지루할테니까..”
- 👍23 [#644] “AI목소리든 아니든 지친 영혼을 달래주면 그뿐. 감상잘했습니다 ^^”
- 👍18 [#14] “엄선한 노래+고음질 음원+고화질 일러스트+노래 도입부마다 짧은 영상+기막힌 재생 순서... 이게 정성이고 사랑이네요 저 지금 케이블 티비 달린 친구네 집 놀러 온 기분이에요 바닥에 엎어져서 빌린 닌텐도DS로 만져라+커비 왕창 하고 과자 먹고 또 티비 보다가 집에 저녁 먹으러 돌아가야 할 것 같아요 진짜 양질의 재생목록... 감사합니다”

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
- `analysis_cases_27.md` — #1041–#1055
