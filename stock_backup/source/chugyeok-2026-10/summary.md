# chugyeok-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py stock chugyeok-2026-10` (2026-10-12 09:39). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **나만 못 탈까 봐 따라 산 급등주에서 번 380만원이 -1천만원이 됐습니다. 추격매수한 사람들의 불편한 진실**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 103 / 자막 120, 길이 9:22 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–5 · 진행자 6–103 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/chugyeok-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 나만 못 탈까 봐 따라 산 급등주에서 번 380만원이 -1천만원이 됐습니다. 추격매수한 사람들의 불편한 진실 `속마음 · 이득→손실 · 불편한 진실` 60자 — 짝 썸네일: thumbnail_1 (계좌 숫자 반전)
- [ ] **T2.** 일곱 배 올랐다는 말만 듣고 올라탄 주식이 +380만원에서 -1천만원이 됐습니다. 급등주 쫓아간 사람들의 최악의 결말 `계기 · +대비 · 최악의 결말` 65자 — 짝 썸네일: thumbnail_2 (인물·감정 장면)
- [ ] **T3.** (짧은 변형) 급등주에 올라탄 지 일주일, 번 380만원이 -1천만원이 됐습니다. 고점에 따라 산 사람들의 공통점 `장면 · 이득→손실 · 공통점` 55자 — 짝 썸네일: thumbnail_3 (검은 배경 제목형 — 채택 제목 문구)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (계좌 카드)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 수익 **+380만 원이 일주일 만에 -1,000만 원**으로 뒤집힌 **계좌 숫자 반전**이 가장 클릭을 부른다 (성공 썸네일 중 인물 없는 3개가 모두 이 형태)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 시작 숫자 | +380만 원 | 빨강 #E63B2E | 수익 금액 = 빨강 |
| 펀치 (위쪽) | 일주일 만에 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (노랑 상자는 이 1곳만) |
| 카드 결과 숫자 | -1,000만 원 | 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 나만 못 탈까 봐 샀다가 | 흰색 + 검정 외곽선 | — (13자) |
| 하단 2줄 | +380만원이 -1천만원 | 흰색 + 검정 외곽선 | "-1천만원"만 노랑 #FFD400 (13자, 2줄 합 26자) |

- 강조색 3곳: 빨강 "+380만 원"(카드, 수익), 노랑 형광펜 "일주일 만에", 노랑 글자 "-1천만원". 손실 숫자는 빨강으로 쓰지 않는다 (카드는 파랑 상자, 하단은 노랑).
- 하단 2줄은 T1 앞 문장("나만 못 탈까 봐 따라 산 급등주에서 번 380만원이 -1천만원이 됐습니다")을 줄인 것. 2줄 합 26자 안에 넣으려고 "따라 산 급등주에서 번"을 "샀다가"로 줄였다. "+"는 380만원이 손실이 아니라 수익이라는 걸 한눈에 보이게 붙였다 (값은 제목과 같음).
- 하단 2줄은 제목 표기("380만원", "-1천만원"), 카드는 영상 계좌 카드 표기("+380만 원", "-1,000만 원")다. 값은 같다 (`stock/guides/thumbnail_rules.md` 1번).

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos, no stock names). Inside the card, on the left: the text
"+380만 원" in large red (#E63B2E) bold letters. In the middle: a thick blue (#2D6CDF) arrow that goes up a little and then
plunges steeply down to the right, with the label "일주일 만에" in black bold letters over a bright yellow (#FFD400)
highlighter stripe just above the arrow. On the right: a solid blue (#2D6CDF) rounded box with the huge white bold text
"-1,000만 원", the largest element in the image. No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "나만 못 탈까 봐 샀다가", line 2 "+380만원이 -1천만원". The word "-1천만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 꼭대기 근처에서 따라 산 뒤 손실을 확인한 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (성공 썸네일 24개 중 약 20개가 얼굴)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 일곱 배에 샀다 | 흰색 #F7F3EA ("일곱 배"만 검정) | "일곱 배"에 노랑 상자 (글자 전체 높이, 노랑 상자는 이 1곳만) |
| 결과 숫자 (위쪽) | -1,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |
| 하단 1줄 | 말만 듣고 올라탄 주식 | 흰색 + 검정 외곽선 | — (12자) |
| 하단 2줄 | +380만원에서 -1천만원 | 흰색 + 검정 외곽선 | "+380만원" 빨강 #E63B2E(수익), "-1천만원" 노랑 #FFD400(손실) (14자, 2줄 합 26자) |

- 강조색 3곳: 노랑 상자 "일곱 배", 빨강 "+380만원"(수익), 노랑 "-1천만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (위쪽은 파랑 상자, 하단은 노랑).
- 하단 2줄은 T2 앞 문장("일곱 배 올랐다는 말만 듣고 올라탄 주식이 +380만원에서 -1천만원이 됐습니다")을 줄인 것. "일곱 배"는 펀치에 있어 하단에 다시 쓰지 않았다.
- 펀치 "일곱 배에 샀다"는 문장 2(공모가의 일곱 배가 넘은 값에 산 것, 0:06)와 문장 22("공모가 31달러의 일곱 배가 넘는 값")의 말이다.
- 하단 2줄은 제목 표기("+380만원", "-1천만원"), 위쪽 상자는 영상 계좌 카드 표기("-1,000만 원")다. 값은 같다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned room late at night, lit only by a small desk lamp. On the left 40% of the frame,
a fictional Korean office worker around 40 years old (plain shirt), sitting and holding a smartphone, the other hand
covering the mouth, frozen stunned and regretful expression, face lit by the phone's cold light. The face and the phone
are in the upper 60% of the frame; the lower body fades into darkness at the bottom. The phone screen shows only a simple
line that rises briefly in red and then turns blue and drops sharply, no app interface, no text. Fictional person, not
resembling any real or famous person, natural Korean features, realistic photo style. In the upper right area, large bold
text "일곱 배에 샀다" in off-white, where only the words "일곱 배" sit on a solid bright yellow (#FFD400) box with black
text. Below it, still in the upper 60%, a wide solid blue (#2D6CDF) rounded box with a thin white border containing the
huge white bold text "-1,000만 원", the largest element. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "말만 듣고 올라탄 주식", line 2 "+380만원에서 -1천만원". In line 2, "+380만원" is red #E63B2E and "-1천만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 검은 배경 제목형 (채택 제목 문구)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 그림 없이 **검은 배경에 채택 제목 앞 문장만** 크게 넣은 글자 썸네일이 사진 썸네일 사이에서 눈에 띄어 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 나만 못 탈까 봐 따라 산 | 흰색 #FFFFFF | — (14자) |
| 2줄 | 급등주에서 번 380만원이 | "380만원" 빨강 #E63B2E, 나머지 흰색 | 수익 금액 = 빨강 (14자) |
| 3줄 | -1천만원이 됐습니다 | "-1천만원" 노랑 #FFD400, 나머지 흰색 | 손실 금액 = 노랑, 빨강 금지 (11자) |

- 채택 제목 앞 문장 "나만 못 탈까 봐 따라 산 급등주에서 번 380만원이 -1천만원이 됐습니다."를 **글자 그대로** 3줄로 나눴다 (끝 마침표만 뺌). 뒤 문장(결말 장치 "추격매수한 사람들의 불편한 진실")은 넣지 않는다.
- 줄 길이(띄어쓰기 포함): 14자 · 14자 · 11자 — 모두 14자 이내, 어절 단위로 끊음
- 숫자 반전("380만원이 -1천만원이")은 2줄 끝 "380만원이" → 3줄 첫머리 "-1천만원이"로 바로 이어지게 나눴다 (몰빵 thumbnail_3과 같은 방식). 한 줄에 모으면 4줄이 되고 글자가 작아진다.
- 강조 2곳: 빨강 "380만원"(수익), 노랑 "-1천만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (`stock/guides/thumbnail_rules.md` 1번·2번).
- 행동 단어 "따라 산"은 흰색으로 둔다. 바로 아래 줄의 빨강(수익)과 붙어 빨강의 뜻(이 채널에서는 수익)이 섞이지 않게 하기 위해서다 — 같은 상황(수익 금액이 있는 제목)인 몰빵·빚투 thumbnail_3과 같은 선택.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 3 lines with tight line spacing:
line 1 "나만 못 탈까 봐 따라 산", line 2 "급등주에서 번 380만원이", line 3 "-1천만원이 됐습니다".
All text pure white (#FFFFFF) except "-1천만원" at the start of line 3 in bright yellow (#FFD400) and "380만원" in line 2 in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
상장 보름 만에 일곱 배가 넘은 주식을 4천만 원어치 따라 샀다가, 380만 원 수익이 일주일 만에 -1천만 원이 됐습니다.
급등주 추격 매수가 왜 꼭대기에서 물리기 쉬운지 4가지로, 사기 전에 확인할 순서를 5가지로 정리했습니다.

■ 이 영상에서 다루는 것
- 많이 오른 뒤에 사면 더 오를 몫보다 떨어질 몫이 큰 이유 (써클 2025년 6월: 공모가의 일곱 배에 산 주식, 시가총액은 순이익의 440배)
- 급등의 끝에서 사 주는 쪽이 늦게 들어온 개인이 되기 쉬운 이유 (꼭대기에서 판 아크 인베스트, 그 주에 2,600억 원 넘게 산 국내 투자자)
- 사람이 한꺼번에 몰린 종목일수록 그 뒤 성과가 나빴던 이유 (로빈후드 사용자 연구: 20일 동안 시장보다 평균 4.7% 뒤처짐, 금융감독원·한국거래소 2025년 테마주 60개 중 72%가 고점보다 30% 넘게 하락)
- 놓칠까 봐 조급한 마음이 꼭 확인할 것을 건너뛰게 만드는 이유 (아문디 2026년 조사: ETF 투자 이유로 뒤처질까 봐 두려운 마음을 꼽은 한국인 19%, 세계 평균 12%)
- 사기 전에 확인할 순서 5가지: 얼마나 올랐는지, 왜 올랐는지, 누가 팔고 있는지, 놓치기 싫은 몫만 따로, 급등 소식을 들은 날은 사지 않기

■ 챕터
0:00 사연: 따라 산 급등주, 380만 원이 -1천만 원
0:25 왜 급등주를 따라 살까
1:46 문제 01 많이 오른 뒤에 사면 떨어질 몫이 더 크다
2:49 문제 02 꼭대기에서 사 주는 쪽은 늦게 온 개인
3:40 문제 03 사람이 몰린 종목일수록 성과가 나빴다
4:56 문제 04 조급함이 확인을 건너뛰게 만든다
6:07 방법 첫째: 얼마나 올랐는지 숫자로 확인
6:45 방법 둘째: 왜 올랐는지 확인
7:21 방법 셋째: 누가 팔고 있는지 확인
7:52 방법 넷째: 놓치기 싫은 몫만 따로 정하기
8:18 방법 다섯째: 급등 소식 들은 날은 사지 않기
9:00 정리

■ 사연에 대해
이 영상의 사연은 실제 주가 흐름(써클, 2025년 6월 상장 직후 급등과 급락)을 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시입니다.

■ 출처
- 써클 일별 주가 (2025년 6~8월): https://finance.yahoo.com/quote/CRCL/history/?period1=1748736000&period2=1756684800
- 써클 일별 주가 (2026년): https://stockanalysis.com/stocks/crcl/history/
- 써클 상장 서류 S-1 (2024년 순이익, 매출 구성, 금리 영향): https://www.sec.gov/Archives/edgar/data/1876042/000119312525070481/d737521ds1.htm
- 2024년 순이익 42% 감소: https://www.financemagnates.com/cryptocurrency/stablecoin-issuer-circle-files-for-us-ipo-despite-42-profit-decline/
- 2024년 유통 비용 (Coin Metrics): https://coinmetrics.substack.com/p/state-of-the-network-issue-307
- 미국 상원 스테이블코인 법안 통과와 써클 주가: https://cointelegraph.com/news/coinbase-circle-stocks-surge-us-senate-genius-stablecoin-bill
- 고점 298.99달러와 국내 투자자 한 주 순매수 (머니투데이 2025-06-26): https://www.mt.co.kr/stock/2025/06/26/2025062513372185795
- 2025년 6월 국내 투자자 써클 순매수 1위 (한국경제 2025-07-03): https://www.hankyung.com/article/202507035024i
- 아크 인베스트 6월 23일 매도와 시가총액: https://www.theblock.co/post/359350/ark-invest-offloads-110-million-worth-circle-shares
- 아크 인베스트 6월 16·17일 매도: https://www.theblock.co/post/358679/ark-invest-offloads-44-million-worth-circle-shares
- JP모건 목표 주가 80달러 (2025-06-30): https://www.aol.com/news/wall-street-analysts-bullish-circle-120031653.html
- 2025년 8월 1천만 주 공모 (주당 130달러): https://investor.circle.com/news/news-details/2025/Circle-Announces-Pricing-of-Public-Offering/default.aspx
- Barber, Huang, Odean & Schwarz (2022), 로빈후드 사용자 연구: https://ideas.repec.org/a/bla/jfinan/v77y2022i6p3141-3190.html
- 금융감독원·한국거래소 테마주 60개 분석 (2025-05-14): https://www.hankyung.com/article/2025051423366
- 아문디 Decoding Investors 2026 (2026-10-01): https://biz.heraldcorp.com/article/10890282

■ 투자 유의 사항
이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
투자 판단과 책임은 투자자 본인에게 있습니다.

#주식 #추격매수 #급등주
```

**태그**: 추격 매수, 추격매수, 급등주, 고점 매수, 주식 손실, 주식 물림, 주식, 주식 투자, 주식 초보, 주식 공부, 미국 주식, 서학개미, 써클, 스테이블코인, 공모주

**고정 댓글**

```
급등 뉴스에 사고 싶어질 때, 이 세 가지부터 확인해 보세요.
1. 최근 한 달 동안 몇 % 올랐는지
2. 이익이 늘어서 오른 건지, 뉴스와 기대만으로 오른 건지
3. 대주주나 큰 기관이 팔고 있지는 않은지

여러분은 급등주를 따라 샀다가 꼭대기에서 물려 본 적이 있나요? 그때 사기 전에 확인한 것이 있었는지 댓글로 나눠 주세요.
※ 이 영상은 투자 권유가 아닙니다. 특정 종목 추천·리딩방 홍보 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 따라 사서 번 380만 원이, 일주일 만에 -1천만 원이 됐어요.
2. 2025년 6월, 상장 보름 만에 일곱 배가 넘은 써클을 4천만 원어치 샀죠.
3. 그런데 다음 주, 하루 15%씩 두 번 무너졌어요.
4. 지금도 주가는 제가 산 값의 절반이 안 돼요.
5. 나만 못 탈까 봐 서두른 그 하루가, 1천만 원을 가져갔어요.

**진행자 파트** — 🎙 진행자

6. 며칠 새 몇 배씩 올랐다는 주식 뉴스가 쏟아지면 이런 생각이 들기 쉽습니다.
7. 지금이라도 안 타면 나만 뒤처지는 거 아니야?
8. 이렇게 오르는 데는 다 이유가 있겠지.
9. 조금만 먹고 바로 빠지면 되지.
10. 이런 식으로 놓칠까 봐 조급한 마음이 꼭대기 근처의 추격 매수로 이어집니다.
11. 사연 속 써클은 스테이블코인을 만드는 미국 회사입니다.
12. 스테이블코인은 달러와 1대1로 값을 맞춘 디지털 화폐죠.
13. 써클은 2025년 6월 5일, 공모가 31달러에 미국 증시에 상장했습니다.
14. 6월 17일, 미국 상원이 스테이블코인 법안을 통과시켰습니다.
15. 그러자 다음 날 써클 주가는 34% 가까이 뛰었죠.
16. 국내 투자자도 몰렸습니다.
17. 2025년 6월 한 달 동안 써클을 8천억 원 넘게 순매수했죠.
18. 그달 해외 주식 가운데 순매수 1위였습니다.
19. 사연자처럼 꼭대기 근처에서 올라탄 사람이 그만큼 많았다는 뜻입니다.
20. 그럼 급등주를 따라 사면 왜 꼭대기에서 물리기 쉬운지 하나씩 짚어 보겠습니다.

> 🟨 [장면] 투자 권유가 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
> 사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
> 과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
> 투자 판단과 책임은 투자자 본인에게 있습니다.

**문제 분석 파트** — 🎙 진행자

21. 첫 번째 문제는 많이 오른 뒤에 사면, 더 오를 몫보다 떨어질 몫이 훨씬 크다는 것입니다.
22. 사연자가 산 240달러는 공모가 31달러의 일곱 배가 넘는 값이었습니다.
23. 그 뒤 가장 높았던 값은 다음 거래일 장중 300달러 가까이였습니다.
24. 산 값보다 25% 가까이 위였죠.
25. 반면 2026년 10월 주가는 80달러대로, 사연자가 산 값의 3분의 1 남짓입니다.
26. 꼭대기였던 6월 23일, 회사 전체의 몸값인 시가총액은 689억 달러였습니다.
27. 2024년 한 해 순이익 1억 5,600만 달러의 440배가 넘는 값이었죠.
28. 그 순이익마저 1년 전보다 40% 넘게 줄어든 숫자였습니다.
29. 일주일 뒤, 써클 상장을 주관한 미국 은행 JP모건은 목표 주가를 80달러로 잡았습니다.
30. 급등한 값에는 몇 년 뒤의 기대까지 이미 들어가 있다는 뜻입니다.
31. 두 번째는 급등의 끝에서 사 주는 쪽이 늦게 들어온 개인이 되기 쉽다는 것입니다.
32. 미국 자산운용사 아크 인베스트는 상장 첫날 써클 주식을 450만 주 가까이 샀습니다.
33. 그리고 주가가 치솟던 6월 16일부터 팔기 시작했죠.
34. 꼭대기를 찍은 6월 23일 하루에만 1억 달러 넘게 팔았습니다.
35. 반대로 국내 투자자는 6월 18일부터 24일까지 2,600억 원 넘게 순매수했습니다.
36. 8월에는 회사와 기존 주주들이 주식 1천만 주를 주당 130달러에 더 팔았습니다.
37. 누군가 꼭대기에서 사려면, 누군가는 꼭대기에서 팔아야 합니다.
38. 먼저 들어온 사람이 차익을 챙기는 그 가격에, 늦게 들어온 사람이 사 주는 셈이죠.
39. 세 번째는 사람이 한꺼번에 몰린 종목일수록 그 뒤 성과가 나빴다는 것입니다.
40. 로빈후드는 미국 개인 투자자들이 많이 쓰는 주식 앱입니다.
41. 미국 캘리포니아대 등 연구진이 이 앱 사용자들의 거래를 분석했습니다.
42. 2018년부터 2020년까지의 자료입니다.
43. 날마다 매수가 가장 많이 몰린 종목들을 따로 살펴봤습니다.
44. 이 종목들은 그 뒤 20일 동안 시장보다 평균 4.7% 뒤처졌습니다.
45. 급등 뉴스를 보고 사는 순간, 이 무리 속에 들어가는 겁니다.
46. 국내도 다르지 않습니다.
47. 2025년 5월, 금융감독원과 한국거래소가 테마주 60개를 살펴봤습니다.
48. 대통령 선거를 앞두고 급등한 종목들이었죠.
49. 그중 72%가 고점보다 30% 넘게 떨어져 있었습니다.
50. 이 종목들을 사고판 사람의 87%가 개인이었습니다.
51. 시장 전체의 개인 비중 67%보다 훨씬 높았죠.
52. 물론 오르는 주식이 더 오르기도 합니다.
53. 하지만 며칠 새 사람이 한꺼번에 몰린 종목은 그 반대인 경우가 많았다는 겁니다.
54. 네 번째는 놓칠까 봐 조급한 마음이 꼭 확인할 것을 건너뛰게 만든다는 것입니다.
55. 서두르면 이 회사가 무엇으로 돈을 버는지 볼 틈이 없습니다.
56. 써클 매출의 99%는 맡아 둔 달러를 미국 국채 등에 넣어 받는 이자였습니다.
57. 그래서 금리가 내리면 수익도 줄어드는 구조죠.
58. 게다가 2024년에는 번 돈의 60% 정도를 협력사에 나눠 줬습니다.
59. 미국 가상자산 거래소 코인베이스 같은 곳이죠.
60. 이 내용은 모두 상장 서류에 나와 있었습니다.
61. 하지만 일곱 배 오른 주가 앞에서는 이런 숫자가 눈에 들어오지 않습니다.
62. 놓칠까 봐 서두르는 마음은 한국 투자자에게 더 흔하기도 합니다.
63. 2026년 자산운용사 아문디가 26개국 투자자 1만 8천 명을 조사했습니다.
64. ETF를 가졌거나 사려는 한국인 중 19%가 뒤처질까 봐 두려운 마음을 이유로 꼽았습니다.
65. 세계 평균 12%보다 높았죠.
66. 그렇다면 급등하는 주식 앞에서는 어떻게 해야 할까요?

**올바른 방법 설명 파트** — 🎙 진행자

67. 핵심은 사기 전에 확인하는 순서를 정해 두고, 그 순서를 건너뛰지 않는 것입니다.
68. 첫째, 얼마나 올랐는지부터 숫자로 확인합니다.
69. 최근 한 달 동안 몇 % 올랐는지, 며칠 사이에 오른 건지 봅니다.
70. 사연자가 산 6월 20일, 써클은 거래일 이틀 만에 60% 넘게 올라 있었습니다.
71. 예를 들어 한 달 사이 두 배 넘게 오른 종목은 그날 사지 않는다고 정해 둡니다.
72. 그날은 관심 목록에만 넣어 두는 거죠.
73. 이 기준이면 사연자는 그날 써클을 사지 않았을 겁니다.
74. 둘째, 왜 올랐는지 확인합니다.
75. 이익이 늘어서 오른 건지, 뉴스와 기대만으로 오른 건지 나눠 봅니다.
76. 써클이 크게 뛴 이유는 상원의 법안 통과, 즉 앞으로에 대한 기대였습니다.
77. 반면 회사의 이익은 주가만큼 늘고 있지 않았습니다.
78. 앞에서 본 것처럼 2024년 순이익은 오히려 40% 넘게 줄었죠.
79. 기대만으로 오른 주식은 기대가 식으면 오른 만큼 빠지기 쉽습니다.
80. 반대로 이익이 함께 늘고 값도 지나치지 않다면, 오른 뒤에 사도 됩니다.
81. 셋째, 누가 팔고 있는지 확인합니다.
82. 대주주나 큰 기관이 팔고 있는지, 회사가 새 주식을 낼 계획이 있는지 공시에서 봅니다.
83. 아크 인베스트의 매도는 매일 공개되는 매매 내역에 그대로 나와 있었습니다.
84. 국내 주식은 전자공시시스템 다트에서 대주주 지분 변동과 유상증자를 확인할 수 있습니다.
85. 먼저 들어온 사람이 팔고 있다면, 그 물량을 받아 주는 쪽이 되지 않는 게 먼저입니다.
86. 넷째, 그래도 사고 싶다면 놓치기 싫은 마음을 위한 몫만 따로 정합니다.
87. 예를 들어 계좌의 5%까지만 급등주에 쓰는 겁니다.
88. 사연자라면 4천만 원의 5%, 200만 원입니다.
89. 같은 일주일을 겪었어도 손실은 50만 원 정도에서 그쳤을 겁니다.
90. 이 몫을 다 쓰면, 주가가 더 올라도 더 넣지 않습니다.
91. 다섯째, 급등 소식을 들은 날은 사지 않고 일주일 뒤에 다시 보는 것입니다.
92. 놓친 수익은 손실이 아닙니다.
93. 써클을 사지 않았다면 사연자의 4천만 원은 그대로였습니다.
94. 법안 통과 소식에 써클이 34% 뛴 날은 6월 18일이었습니다.
95. 일주일 뒤인 6월 25일 주가는 198달러로, 꼭대기보다 3분의 1 낮았죠.
96. 사연자가 산 값보다도 17% 낮은 가격이었습니다.
97. 일주일만 지나도 열기가 식는지, 이익이 따라오는지가 보입니다.
98. 그때 첫째부터 넷째까지 다시 확인하고, 모두 맞을 때만 삽니다.

**마무리** — 🎙 진행자

99. 이렇게 해서 급등주를 따라 사면 위험한 이유와, 사기 전에 확인할 순서를 알아보았습니다.
100. 급등 뉴스에 손이 갈 때일수록, 사기 전에 세 가지부터 확인하세요.
101. 얼마나 올랐는지, 왜 올랐는지, 누가 팔고 있는지입니다.
102. 성공 투자 하셨으면 좋겠습니다.
103. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
