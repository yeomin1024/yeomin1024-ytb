# jisu-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py stock jisu-2026-10` (2026-10-12 13:06). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **지수는 느리다며 갈아탔다가 +2,800만원 대신 900만원을 잃었습니다. 장기투자 못 버틴 사람들의 불편한 진실**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 124 / 자막 156, 길이 11:36 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–5 · 진행자 6–124 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/jisu-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 지수는 느리다며 갈아탔다가 +2,800만원 대신 900만원을 잃었습니다. 장기투자 못 버틴 사람들의 불편한 진실 `속마음 · +대비 · 불편한 진실` 62자 — 짝 썸네일: thumbnail_1 (갈림길 계좌 카드)
- [ ] **T2.** 남들 수익 인증에 3년 모은 지수를 깨고 900만원을 잃었습니다. 장기투자 하다 갈아탄 사람들이 망하는 과정 `계기 · 손실 · ~하는 과정(시험)` 60자 — 짝 썸네일: thumbnail_2 (인물·감정 장면)
- [ ] **T3.** (짧은 변형) 지수였으면 +2,800만원, 갈아타서 -900만원이 됐습니다. 적립 깬 사람들의 공통점 `장면(숫자 대비) · +대비 · 공통점` 48자 — 짝 썸네일: thumbnail_3 (검은 배경 제목형 — 채택 제목 문구)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (갈림길 계좌 카드)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 같은 4,500만 원이 **지수에 남았으면 +2,800만 원, 갈아탔더니 -900만 원**으로 갈린 **두 숫자의 대비**가 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 위 갈래 | 지수 (작은 라벨) / +2,800만 원 | 라벨 잉크 #1E1E1E / 숫자 빨강 #E63B2E | 수익(지수에 뒀다면) = 빨강 |
| 펀치 (위쪽) | 같은 돈인데 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (노랑 상자는 이 1곳만) |
| 카드 아래 갈래 | 내 종목 (작은 라벨) / -900만 원 | 라벨 잉크 / 숫자 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 지수 느리다며 갈아탔다가 | 흰색 + 검정 외곽선 | — (13자) |
| 하단 2줄 | 900만원 잃었습니다 | 흰색 + 검정 외곽선 | "900만원"만 노랑 #FFD400 (11자, 2줄 합 24자) |

- 강조색 3곳: 빨강 "+2,800만 원"(수익 쪽), 노랑 형광펜 "같은 돈인데", 노랑 글자 "900만원". 손실 숫자는 빨강으로 쓰지 않는다 (카드는 파랑 상자, 하단은 노랑 — `stock/guides/thumbnail_rules.md` 1번).
- 하단 2줄은 T1 앞 문장("지수는 느리다며 갈아탔다가 +2,800만원 대신 900만원을 잃었습니다")을 줄인 것. "+2,800만원 대신"은 카드 숫자로 넘기고 하단에서는 뺐다.
- 작은 라벨 "지수"·"내 종목"은 카드의 일부(작은 잉크 글자)다. 펀치 문구는 "같은 돈인데" 1개.
- 하단 2줄은 제목 표기("900만원"), 카드는 영상 계좌 카드 표기("+2,800만 원", "-900만 원")다. 값은 같다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos, no stock or fund names). Inside the card, on the left, one small
black dot where a single line splits into two branches like a fork in the road: one thick red (#E63B2E) branch rises up to the
upper right and ends at the small ink label "지수" and the red bold text "+2,800만 원"; the other thick blue (#2D6CDF) branch
drops steeply down to the lower right and ends at the small ink label "내 종목" next to a solid blue (#2D6CDF) rounded box
with the huge white bold text "-900만 원", the largest element in the image. Just above the split point, the words
"같은 돈인데" in black bold letters over a bright yellow (#FFD400) highlighter stripe. No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "지수 느리다며 갈아탔다가", line 2 "900만원 잃었습니다". The word "900만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 지수는 두 배가 됐는데 내 계좌만 마이너스인 걸 확인한 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (옛 자료: 작은 채널 성공 썸네일 15개 중 사람·캐릭터 14개 — `stock/guides/thumbnail_rules.md` 2번)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 코스피는 두 배 | 흰색 #F7F3EA ("두 배"만 빨강) | "두 배" 빨강 #E63B2E (지수 상승 = 빨강) |
| 결과 숫자 (위쪽) | -900만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |
| 하단 1줄 | 남들 인증에 지수 깨고 | 흰색 + 검정 외곽선 | — (12자) |
| 하단 2줄 | 900만원을 잃었습니다 | 흰색 + 검정 외곽선 | "900만원"만 노랑 #FFD400 (12자, 2줄 합 24자) |

- 강조색 2곳: 빨강 "두 배"(지수 상승), 노랑 "900만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (위쪽은 파랑 상자, 하단은 노랑).
- 하단 2줄은 T2 앞 문장("남들 수익 인증에 3년 모은 지수를 깨고 900만원을 잃었습니다")을 줄인 것.
- 펀치 "코스피는 두 배"는 사연 문장 4("코스피가 두 배를 넘은 6월 19일")의 말이다. 손실은 금액("-900만 원")을 가장 크게 썼다 (`stock/guides/thumbnail_rules.md` 1번).

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned room late at night, lit only by a small desk lamp. On the left 40% of the frame,
a fictional Korean man office worker in his early 40s (plain dress shirt), sitting and holding a smartphone, the other hand
pressed to his forehead, frozen stunned and regretful expression, face lit by the phone's cold light. The face and the phone
are in the upper 60% of the frame; the lower body fades into darkness at the bottom. The phone screen shows only a simple
blue line sliding down, no app interface, no text. Fictional person, not resembling any real or famous person, natural
Korean features, realistic photo style. In the upper right area, large bold text "코스피는 두 배" in off-white, where only
"두 배" is red (#E63B2E). Below it, still in the upper 60%, a wide solid blue (#2D6CDF) rounded box with a thin white border
containing the huge white bold text "-900만 원", the largest element. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "남들 인증에 지수 깨고", line 2 "900만원을 잃었습니다". The word "900만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 검은 배경 제목형 (채택 제목 문구)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 그림 없이 **검은 배경에 채택 제목 앞 문장만** 크게 넣은 글자 썸네일이 사진 썸네일 사이에서 눈에 띄어 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 지수는 느리다며 | 흰색 #FFFFFF | — (8자) |
| 2줄 | 갈아탔다가 | 흰색 #FFFFFF | — (5자) |
| 3줄 | +2,800만원 대신 | "+2,800만원" 빨강 #E63B2E, "대신" 흰색 | 수익 금액 = 빨강 (11자) |
| 4줄 | 900만원을 잃었습니다 | "900만원" 노랑 #FFD400, 나머지 흰색 | 손실 금액 = 노랑, 빨강 금지 (12자) |

- 채택 제목 앞 문장 "지수는 느리다며 갈아탔다가 +2,800만원 대신 900만원을 잃었습니다."를 **글자 그대로** 4줄로 나눴다 (끝 마침표만 뺌). 뒤 문장(결말 장치 "장기투자 못 버틴 사람들의 불편한 진실")은 넣지 않는다.
- 줄 길이(띄어쓰기 포함): 8자 · 5자 · 11자 · 12자 — 모두 14자 이내, 어절 단위로 끊음.
- 3줄로 나누면 1줄 "지수는 느리다며 갈아탔다가"(한글 12자)가 100px에서 약 1,250px로 화면 폭 85%를 넘는다 → 4줄로 나눴다. 숫자 반전("+2,800만원 대신" → "900만원을 잃었습니다")은 3·4줄에 위아래로 붙여 한눈에 대비되게 했다.
- 강조 2곳: 빨강 "+2,800만원"(이 채널에서 빨강 = 수익 — 지수에 뒀다면 벌었을 돈), 노랑 "900만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (`stock/guides/thumbnail_rules.md` 1번·2번).
- 행동 단어 "갈아탔다가"는 흰색으로 둔다. 바로 아래 줄의 빨강(수익)과 붙어 빨강의 뜻이 섞이지 않게 하기 위해서다 (옛 몰빵·빚투·추격 매수 thumbnail_3과 같은 선택).

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "지수는 느리다며", line 2 "갈아탔다가", line 3 "+2,800만원 대신", line 4 "900만원을 잃었습니다".
All text pure white (#FFFFFF) except "+2,800만원" at the start of line 3 in red (#E63B2E) and "900만원" at the start of line 4 in bright yellow (#FFD400). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
3년 모은 지수 ETF 4,500만 원을 팔아 덜 오른 인터넷 대장주로 갈아탔더니, 9개월 뒤 계좌는 -900만 원이 됐습니다. 지수에 그대로 뒀다면 +2,800만 원이었을 돈입니다.
지수 적립을 떠나는 다섯 단계와, 단계마다 붙잡아 줄 장치 다섯 가지를 정리했습니다.

■ 이 영상에서 다루는 것
- 1단계 지루함: 코스피는 2021년 7월의 최고치를 4년 2개월 동안 넘지 못했지만, 2025년 9월 그 기록을 넘은 뒤 넉 달도 안 돼 27% 더 올랐습니다
- 2단계 비교: 불장에는 수익 인증이 넘칩니다 (2026년 1분기 신한투자증권 고객 중 주식을 판 사람의 80%가 이익). 하지만 벌었다는 것과 지수보다 더 벌었다는 건 다릅니다
- 3단계 조금만 하는 타협: 2026년 5월 말 나온 단일종목 레버리지 ETF를 개인이 3주 남짓 만에 8조 2천억 원어치 순매수 (자본시장연구원)
- 4단계 전부 옮기기: 1분기 매출이 16% 넘게 늘어도 주가는 따로 간 네이버 (7월 14일 장중 산 값보다 25% 아래)
- 5단계 돌아갈 때를 놓침: 코스피가 최고치를 넘은 2025년 9월 10일, 개인은 2조 2,545억 원을 순매도했습니다
- 살아남는 장치 다섯 가지: 적립은 자동으로·멈추기는 번거롭게, 인증 대신 볼 숫자, 재미 계좌는 금액으로, 적립 계좌는 다른 증권사에, 돌아가는 날은 달력으로

■ 챕터
0:00 사연: 지수에 뒀으면 +2,800만 원, 갈아타서 -900만 원
0:26 왜 지수를 떠날까
1:51 1단계 지루함: 적립은 너무 느리다
2:38 2단계 비교: 남들은 몇 배씩 번다는데
3:41 3단계 조금만 하는 타협
4:47 4단계 전부 옮기기: 실적 좋은 대장주의 함정
6:00 5단계 돌아갈 때를 놓친다
7:24 장치 첫째: 적립은 자동으로, 멈추기는 번거롭게
8:11 장치 둘째: 인증 대신 볼 숫자
9:03 장치 셋째: 재미 계좌는 금액으로
9:42 장치 넷째: 적립 계좌는 다른 증권사에
10:34 장치 다섯째: 돌아가는 날은 달력으로
11:18 정리

■ 사연에 대해
이 영상의 사연은 실제 주가 흐름(코스피 지수와 네이버, 2025년 12월 30일~2026년 9월 30일)을 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시입니다.
이 영상의 내레이션은 AI 음성으로 만들었습니다.
계산 기준: 지수 쪽은 코스피 지수 등락률, 네이버는 원화 종가이며 양쪽 모두 배당과 수수료는 넣지 않았습니다.

■ 출처
- 코스피 2025년 마지막 거래일 4,214.17 (머니투데이 2025-12-30): https://www.mt.co.kr/stock/2025/12/30/2025123015340935056
- 코스피 2022년 마지막 거래일 2,236.40 (뉴시스 2022-12-29): https://www.newsis.com/view/NISX20221229_0002141388
- 코스피 2025-09-10 사상 최고치 경신·개인 순매도 (머니투데이): https://www.mt.co.kr/article/2025091014212674442
- 코스피 2026-06-22 9,114.55 (트윅24): https://www.twig24.com/news/2026/06/22/20260622500191
- 코스피 2026-06-30 8,476.48 (한국경제): https://www.hankyung.com/article/2026063070016
- 코스피 2026-07-31 6,595.45, 전날보다 1,001.89 상승 (SBS Biz): https://biz.sbs.co.kr/amp/article/20000325956
- 코스피 2026-09-30 6,838.04 (위키트리): https://www.wikitree.co.kr/articles/1163083
- 네이버 2025년 연말 종가 242,500원 (NAVER 통합보고서): https://www.navercorp.com/api/article/read/6dc53f1f-cbee-4198-acfc-023f44b51bac/NAVER_2025_%ED%86%B5%ED%95%A9%EB%B3%B4%EA%B3%A0%EC%84%9C.pdf
- 네이버 2025-12-30 시가총액 약 38조 원 (글로벌이코노믹): https://www.g-enews.com/article/Securities/2026/01/202601011344168313edf69f862c_1
- 네이버 2026-09-30 종가 193,500원 (NAVER IR 주가정보): https://www.navercorp.com/investment/stock
- 네이버 2026년 1분기 실적 (뉴시스 2026-04-30): https://www.newsis.com/view/NISX20260430_0003612889
- 네이버 실적과 주가의 괴리, AI 투자 부담·두나무 합병 지연 (MTN 2026-05-18): https://news.mtn.co.kr/news-detail/2026051815023875648
- 네이버, 6월 초 엔비디아 협력 기대에 급등 후 제자리 (다음 2026-06-04·06-11): https://v.daum.net/v/20260604060253448 · https://v.daum.net/v/20260611112105427
- 네이버 2026-06-19 종가 229,500원 (중앙이코노미뉴스 6/22): https://www.joongangenews.com/news/articleView.html?idxno=527278
- 네이버 52주 최저 181,100원(2026-07-14) (다음 금융): https://m.finance.daum.net/quotes/A035420/home
- 신한투자증권 2026년 1분기 개인 투자자 성과 (헤럴드경제 2026-05-10): https://www.heraldk.com/article/2026051019500060472
- 2026년 넉 달 동안 코스피 75.2% 상승, KRX 헬스케어 지수 4.3% 하락 (데일리팜 2026-05-07): https://www.dailypharm.com/user/news/338191
- 자본시장연구원, 단일종목 레버리지·인버스 ETF 출시 전후 주식시장 동향 및 시사점 (2026): https://www.kcmi.re.kr/publications/pub_detail_view?syear=2026&zcd=002001016&zno=1922&cno=6801

■ 투자 유의 사항
이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
투자 판단과 책임은 투자자 본인에게 있습니다.

#주식 #장기투자 #적립식투자
```

**태그**: 장기투자, 지수 투자, 적립식 투자, 지수 ETF, ETF 적립, 코스피, 개별주, 주식 손실, 주식, 주식 투자, 주식 초보, 주식 공부, 네이버, 인터넷주, 자동 매수

**고정 댓글**

```
적립 계좌를 깨고 싶어질 때, 이 두 가지부터 확인해 보세요.
1. 그 수익 인증과 같은 기간에 지수는 얼마나 올랐는지
2. 내 지수 계좌의 3년 성적

여러분은 지수 적립을 하다가 개별 종목으로 갈아타고 싶었던 적이 있나요? 그때 무엇이 마음을 움직였는지, 버틴 분이라면 어떤 장치가 도움이 됐는지 나눠 주세요.
※ 이 영상은 투자 권유가 아닙니다. 특정 종목 추천·리딩방 홍보 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 지수에 뒀으면 +2,800만 원이었을 돈이, -900만 원이 됐어요.
2. 3년 모은 지수 ETF 4,500만 원을 2025년 연말에 팔았죠.
3. 그 돈으로 덜 오른 인터넷 대장주를 샀고요.
4. 코스피가 두 배를 넘은 6월 19일, 제 계좌는 마이너스였어요.
5. 느리다고 버린 지수가, 제 종목보다 훨씬 빨랐어요.

**진행자 파트** — 🎙 진행자

6. 적립식으로 지수에 돈을 넣다 보면, 어느 순간 이런 생각이 고개를 듭니다.
7. 이렇게 느려서야 돈이 언제 모이지?
8. 남들은 한 종목으로 두세 배씩 벌었다는데.
9. 덜 오른 좋은 종목만 잘 고르면 지수보다 빠르겠지.
10. 이런 식으로 지루함에 비교가 더해지면, 몇 년 모은 적립 계좌도 하루 만에 깨집니다.
11. 사연 속 종목은 국내 최대 인터넷 검색 회사, 네이버입니다.
12. 사연자는 12월 30일, 주당 24만 2,500원에 185주를 샀습니다.
13. 9개월 뒤인 올해 9월 말, 사연자의 계좌는 20% 빠졌고 코스피는 62% 올랐습니다.
14. 지수를 떠나는 분들은 거의 같은 순서를 밟습니다.
15. 지루함, 비교, 조금만 하는 타협, 전부 옮기기, 그리고 돌아갈 때를 놓치는 순서죠.
16. 올해는 이 순서가 유난히 비쌌습니다.
17. 넉 달 만에 코스피가 75% 오르는 사이, 제약·바이오 지수는 오히려 4% 넘게 떨어졌죠.
18. 지수가 오르는 해에도, 지수를 떠나 고른 종목은 거꾸로 갈 수 있다는 뜻입니다.
19. 그럼 첫 단계부터 차례로 보겠습니다.

> 🟨 [장면] 투자 권유가 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
> 사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
> 과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
> 투자 판단과 책임은 투자자 본인에게 있습니다.

**망하는 과정 파트** — 🎙 진행자

20. 첫 번째 단계는 지루함입니다.
21. 매달 꼬박꼬박 넣는데, 계좌는 늘 그대로인 것 같다.
22. 사연자가 적립을 시작한 2023년부터 2년 동안, 코스피는 7% 남짓 올랐습니다.
23. 매달 넣은 돈이 2년 내내 제자리걸음을 한 거죠.
24. 길게 보면, 코스피는 2021년 7월의 최고치를 4년 2개월 동안 못 넘었습니다.
25. 그런데 2025년 9월 그 기록을 넘고 나서는, 넉 달도 안 돼 27%가 더 올랐죠.
26. 지수의 수익은 고르게 나눠서 오지 않는다는 뜻입니다.
27. 문제는 지루함이 쌓일수록, 다음 유혹에 쉽게 흔들린다는 겁니다.
28. 그리고 그 유혹은 대개 남의 계좌에서 옵니다.
29. 두 번째 단계는 비교입니다.
30. 다들 몇 배씩 버는데, 나만 가만히 있다가 바보가 되는 것 같다.
31. 사연자가 계좌를 깬 2025년 연말, 주변에선 한 해 수익률 인증이 이어졌습니다.
32. 그해 사연자의 지수 계좌도 크게 올랐지만, 인증 속 숫자에 비하면 초라해 보였죠.
33. 불장에서는 인증할 거리가 넘칩니다.
34. 올해 1분기 신한투자증권 고객 중 주식을 판 사람의 80%가 이익을 냈습니다.
35. 이익을 낸 사람의 평균 수익은 848만 원이었죠.
36. 하지만 벌었다는 것과, 지수보다 더 벌었다는 건 다른 이야기입니다.
37. 인증 글은 번 금액만 말할 뿐, 같은 기간 지수가 얼마나 올랐는지는 말하지 않습니다.
38. 지수보다 덜 번 사람, 잃은 사람은 아예 글을 올리지 않죠.
39. 비교 상대를 잘못 고르면, 잘 가고 있는 계좌도 실패처럼 보입니다.
40. 비교가 시작되면, 다음에는 작은 예외를 만듭니다.
41. 세 번째 단계는 조금만 하는 타협입니다.
42. 적립 계좌는 그대로 두고, 이번 달 적립금만 다른 데 넣어 보자.
43. 사연자도 처음엔 한 달 적립을 건너뛰고, 그 돈으로 개별 종목을 샀습니다.
44. 작은 돈이니 괜찮다고 생각했죠.
45. 올해는 숫자로도 이 흐름이 보였습니다.
46. 5월 말, 한 종목의 하루 등락을 두 배로 따라가는 ETF가 국내에 나왔습니다.
47. 삼성전자와 SK하이닉스를 따라가는 상품들이었죠.
48. 자본시장연구원 집계로, 개인은 3주 남짓 만에 8조 2천억 원어치를 순매수했습니다.
49. 출시 직후엔 개인의 코스피 지수형 ETF 순매도도 늘었습니다.
50. 지수에서 뺀 돈이 더 빠르고 더 센 곳으로 옮겨 간 흐름이죠.
51. 조금만이라는 말이 위험한 건 금액 때문이 아닙니다.
52. 한 번 지수 밖으로 나간 돈은, 벌든 잃든 다음엔 더 큰 금액을 부르기 쉽기 때문입니다.
53. 사연자의 작은 예외도 오래가지 않았습니다.
54. 네 번째 단계는 전부 옮기기입니다.
55. 이번엔 확실하다, 실적 좋은 대장주가 덜 올랐으니 이제 오를 차례다.
56. 사연자는 지수 ETF를 판 4,500만 원을 모두 네이버 한 종목에 넣었습니다.
57. 실적은 실제로 좋았습니다.
58. 올해 1분기 네이버 매출은 3조 2,411억 원으로, 1년 전보다 16% 넘게 늘었죠.
59. 그런데 주가는 실적과 따로 움직였습니다.
60. AI 투자 부담과 업비트 운영사 두나무와의 합병 지연이 걸림돌로 꼽혔거든요.
61. 6월 초엔 엔비디아와의 협력 기대로 급등했지만, 며칠 못 가 제자리로 돌아왔습니다.
62. 7월 14일엔 장중 18만 1,100원, 1년 중 최저가까지 밀렸죠.
63. 산 값보다 25% 낮은 값이었습니다.
64. 실적이 좋아도, 한 종목의 주가는 지수와 전혀 다른 길로 갈 수 있다는 뜻입니다.
65. 계좌 전체를 한 회사의 사정에 걸어 둔 겁니다.
66. 지수는 한 회사가 이렇게 흔들려도, 그 회사 비중만큼만 흔들립니다.
67. 진짜 손해는 오히려 계좌 밖에서 커졌습니다.
68. 다섯 번째 단계는 돌아갈 때를 놓치는 것입니다.
69. 지수가 너무 올라 버렸다, 조금 빠지면 그때 돌아가자.
70. 사연자가 떠날 때 4,214였던 코스피는, 6월 22일 9,114까지 올랐습니다.
71. 두 배가 된 값에 다시 사기는 아까웠죠.
72. 7월 말 코스피가 고점보다 40% 가까이 빠졌을 때는, 더 빠질까 봐 또 기다렸습니다.
73. 그렇게 9월 말이 됐고, 사연자의 평가액은 3,600만 원에 못 미쳤습니다.
74. 그날 코스피는 6,838, 떠날 때보다 62% 높았죠.
75. 이런 망설임은 사연자만의 일이 아닙니다.
76. 2025년 9월 10일, 코스피가 마침내 그 최고치를 넘은 날이 있었습니다.
77. 그날 개인은 2조 2,545억 원어치를 순매도했습니다.
78. 그때 3,314였던 코스피는, 1년 남짓 뒤인 올해 9월 말 그 두 배를 넘었습니다.
79. 물론 6월 고점에 한꺼번에 다시 들어갔다면, 9월 말엔 25% 가까이 잃었을 겁니다.
80. 돌아갈 날을 가격으로 고르면, 비쌀 땐 비싸서, 빠질 땐 무서워서 미루게 됩니다.
81. 그동안 돈은 지수 밖에 머물게 되죠.
82. 그렇다면 이 다섯 단계는 어디서 끊어야 할까요?

**살아남는 방법 파트** — 🎙 진행자

83. 지수에 넣고 오래 두는 게 답이라는 건, 사실 다들 압니다.
84. 문제는 알면서도 손이 먼저 간다는 것, 그래서 마음보다 손을 막는 장치가 필요합니다.
85. 첫째, 적립은 저절로 되게 하고, 멈추는 길은 번거롭게 만듭니다.
86. 매달 내가 직접 사야 하는 적립은, 지루한 달마다 멈출 이유가 생깁니다.
87. 그러니 월급날 다음 날 자동으로 사도록, 증권사의 정기 매수 기능을 켜 둡니다.
88. 돈은 월급 통장이 있는 은행에서 자동이체로 보내 둡니다.
89. 그러면 적립을 멈추려면, 은행과 증권사 두 곳에서 따로 해지해야 하죠.
90. 연말 하루의 기분으로 3년 모은 4,500만 원을 깨기가 그만큼 어려워집니다.
91. 둘째, 남의 수익 인증 대신 볼 숫자를 정해 둡니다.
92. 인증을 아예 안 보기는 어려우니, 볼 때마다 옆에 둘 숫자를 정하는 겁니다.
93. 하나는 인증과 같은 기간에 지수가 얼마나 올랐는지입니다.
94. 다른 하나는 지수의 3년 성적입니다.
95. 코스피는 2022년 말부터 3년 동안, 2,236에서 4,214로 88% 올랐습니다.
96. 그리고 매년 마지막 거래일에, 내가 고른 종목과 지수의 1년 성적을 한 줄로 적어 둡니다.
97. 사연자라면 9월 말 기준으로, 내 종목 -20%, 지수 +62%가 그 한 줄이겠죠.
98. 개별 종목으로 지수를 이기는 해도 있겠지만, 그게 매년 되는지는 이 한 줄이 알려 줍니다.
99. 셋째, 개별 종목을 하고 싶다면 재미 계좌를 따로 두고, 넣을 돈을 금액으로 정합니다.
100. 하고 싶은 마음을 무조건 막으면, 결국 적립 계좌에 손을 대게 됩니다.
101. 예를 들어 1년에 300만 원까지, 그것도 월급에서만 넣습니다.
102. 적립 계좌에서는 절대 꺼내 오지 않고, 다 잃어도 그해에는 다시 채우지 않습니다.
103. 사연자가 네이버에 300만 원만 넣었다면, 9월 말 손실은 60만 원 정도였을 겁니다.
104. 지수 ETF 4,500만 원은 그대로 남아, 7,300만 원 정도가 돼 있었겠죠.
105. 넷째, 적립 계좌와 매매 계좌를 아예 다른 증권사에 둡니다.
106. 한 앱 안에 두 계좌가 있으면, 지수를 팔고 종목을 사는 데 몇 분이면 충분합니다.
107. 사연자의 4,500만 원도 그렇게 하루 만에 옮겨 갔습니다.
108. 증권사가 다르면, 판 돈을 결제일인 이틀 뒤에야 빼서 다른 증권사로 보내야 합니다.
109. 적립 계좌 앱은 휴대폰에서 지우고, 확인은 컴퓨터로만 합니다.
110. 적립 계좌에서는 시장 전체를 담는 지수 상품만 산다는 규칙도 정합니다.
111. 물론 지수도 올해 7월처럼 크게 빠질 때가 있습니다.
112. 하지만 한 회사의 소식 하나로 무너지지 않고, 새로 커지는 회사를 저절로 더 담습니다.
113. 그래서 적립 계좌에는 그런 하락을 견딜 수 있는 돈만 넣는 게 먼저입니다.
114. 다섯째, 이미 지수를 떠났다면, 돌아가는 날을 가격이 아니라 달력으로 정합니다.
115. 떠날 때의 지수, 사연자라면 4,214라는 숫자는 잊습니다.
116. 다음 월급날부터, 예전과 같은 금액으로 자동 적립을 다시 켜는 겁니다.
117. 같은 돈을 매달 넣으면, 비쌀 땐 적게 사고 쌀 땐 많이 사게 됩니다.
118. 올해 6월 말 코스피는 8,476, 7월 말은 6,595였습니다.
119. 같은 금액으로 7월 말에는 6월 말보다 지수를 28% 넘게 더 산 거죠.
120. 갈아탄 종목을 어떻게 할지는 따로 정하고, 적립 재개를 그 결과에 묶지 않습니다.

**마무리 파트** — 🎙 진행자

121. 이렇게 해서 지수를 떠나는 다섯 단계와, 단계마다 붙잡아 줄 장치를 알아보았습니다.
122. 적립 계좌를 깨고 싶어지는 날, 남의 인증 대신 지수의 3년 성적부터 확인해 보세요.
123. 성공 투자 하셨으면 좋겠습니다.
124. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
