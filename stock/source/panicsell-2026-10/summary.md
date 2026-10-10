# panicsell-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py stock panicsell-2026-10` (2026-10-10 08:37). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **하락장이 무서워 -800만원에 다 팔았는데 그 뒤 +30% 반등했습니다. 패닉셀한 사람들이 마지막에 꼭 하는 후회**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 92 / 자막 109, 길이 8:19 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 스토리보드 | ✅ still 53장 |
| 오디오 | ⏳ 없음 → `source/panicsell-2026-10/narration.mp3`(또는 .wav·.m4a)를 올리면 4단계 시작 |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 하락장이 무서워 -800만원에 다 팔았는데 그 뒤 +30% 반등했습니다. 패닉셀한 사람들이 마지막에 꼭 하는 후회 `속마음 · 판 뒤 반등 · 마지막에 꼭 하는 후회` 63자 — 짝 썸네일: thumbnail_1 (계좌 숫자 반전)
- [ ] **T2.** 서킷브레이커 걸린 날 -800만원에 전부 팔았는데 다음 날 +11% 올랐습니다. 공포에 다 판 사람들의 공통점 `장면 · 판 뒤 반등 · 공통점` 61자 — 짝 썸네일: thumbnail_2 (인물 장면)
- [ ] **T3.** (짧은 변형) 폭락한 날 -800만원에 다 팔았더니 7주 뒤 +30%였습니다. 겁먹고 판 사람들의 불편한 진실 `행동 · 판 뒤 반등 · 불편한 진실` 53자 — 짝 썸네일: thumbnail_3 (판 날 vs 7주 뒤 대비)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (판 금액 → 판 뒤 반등)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: "-800만 원에 팔았는데 그 뒤 +30%"라는 **판 뒤 반등의 숫자 대비**가 가장 클릭을 부른다 (판 사람의 후회를 숫자 두 개로)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 판 금액 | -800만 원 | 흰색 (파랑 #2D6CDF 상자 위) | — |
| 라벨 | 전부 매도 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (유일한 강조) |
| 판 뒤 | +30% | 빨강 #E63B2E | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. A large light-cream rounded
rectangle card with a thin black outline fills most of the frame, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos). On the left half of the card: a solid blue (#2D6CDF) rounded
box with the large white bold text "-800만 원", and below it the label "전부 매도" in black bold letters over a bright
yellow (#FFD400) highlighter stripe. On the right half of the card: a thick red (#E63B2E) arrow rising steeply from the
lower left to the upper right, ending at the huge red bold text "+30%", the largest element in the image.
No people, no faces. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (다 판 다음 날)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 다 판 다음 날 오른 주가를 본 **사람의 허탈한 표정**이 숫자 카드보다 감정을 더 끈다 (성공 썸네일 24개 중 약 20개가 얼굴)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 장면 | 다 판 다음 날 | 흰색 #F7F3EA ("다 판"만 검정) | "다 판"에 노랑 상자 (글자 전체 높이) |
| 결과 | +11% | 빨강 #E63B2E | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned kitchen in the early morning before work. On the left 40% of the frame, a fictional
Korean woman in her late 30s, office-worker look (plain blouse), sitting at a kitchen table and staring at a smartphone,
mouth slightly open, blank regretful expression, face lit by the phone's light. The phone screen shows only a simple red
line rising sharply, no app interface, no text. Fictional person, not resembling any real or famous person, natural Korean
features. On the right side, large bold headline text "다 판 다음 날" in off-white, where only the words "다 판" sit on a
solid bright yellow (#FFD400) box with black text. Below it, the huge red (#E63B2E) bold text "+11%" with a thin white
outline, the largest element. No crying, no extreme fear.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (판 날 vs 7주 뒤)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: "판 날"과 "7주 뒤"를 나란히 놓은 **시간 대비**가, 폭락장에 다 팔고 싶었던 사람에게 가장 와닿는다 (문제 분석 세 번째 "바닥은 지나고 나서야 보인다")

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 판 날 | 흰색 #F7F3EA | — |
| 왼쪽 숫자 | -800만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | — |
| 오른쪽 | 7주 뒤 | 검정 (노랑 상자 위) | 노랑 상자 #FFD400 (유일한 강조) |
| 오른쪽 숫자 | +30% | 빨강 #E63B2E | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat editorial paper-collage graphic. The frame is split by a vertical torn-paper edge slightly left of center.
Left side (45%, dark navy #14213D): the off-white bold text "판 날" at the top, below it a thick blue (#2D6CDF) line
plunging sharply downward, and under it a solid blue rounded box with a thin white border containing the white bold text
"-800만 원". Right side (55%, cream #F2EBDD): the black bold text "7주 뒤" on a solid bright yellow (#FFD400) box at the
top, below it a thick red (#E63B2E) line rising steeply, ending at the huge red bold text "+30%", the largest element,
placed in the upper-middle of the right side. No people, no faces, no logos. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
서킷브레이커가 걸린 날 겁이 나서 -800만원에 전부 팔았는데, 다음 날 11% 넘게 오르더니 7주 뒤에는 판 가격보다 30% 넘게 올라 있었습니다.
폭락장에서 전부 팔아 버리는 패닉셀이 왜 위험한지 4가지로, 하락장에서 지킬 기준을 5가지로 정리했습니다.

■ 이 영상에서 다루는 것
- 가장 크게 오르는 날은 가장 크게 떨어진 날 바로 뒤에 온다 (2026년 3월 코스피, 2020년 코로나, JP모건 20년 분석)
- 한번 팔면 다시 사기가 훨씬 어렵다 (MIT 계좌 65만여 개 연구)
- 바닥은 지나고 나서야 보인다
- 사고판 시점 때문에 투자자 수익이 줄어든다 (모닝스타 분석)
- 하락장의 기준 5가지: 곧 쓸 돈은 넣지 않기, 폭락한 날엔 하루 기다리기, 팔아도 정해 둔 만큼만, 다시 살 날짜 정하기, 계좌는 정해 둔 날에만 보기

■ 챕터
0:00 사연: -800만 원에 다 팔았는데 +30%
1:18 폭락장에서 왜 다 팔고 싶어질까
2:14 문제 01 최고의 날은 최악의 날 바로 뒤에
3:09 문제 02 한번 팔면 다시 사기 어렵다
3:49 문제 03 바닥은 지나고 나서야 보인다
4:18 문제 04 사고판 시점이 수익을 깎는다
5:12 기준 첫째: 곧 쓸 돈은 넣지 않기
5:38 기준 둘째: 폭락한 날엔 하루 기다리기
6:03 기준 셋째: 팔아도 정해 둔 만큼만
6:32 기준 넷째: 다시 살 날짜와 금액 정하기
7:05 기준 다섯째: 계좌는 정해 둔 날에만
8:01 정리

■ 사연에 대해
이 영상의 사연은 실제 주가 흐름(삼성전자, 2026년 2~4월)을 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시입니다.

■ 출처
- 삼성전자 일별 주가: https://finance.naver.com/item/sise_day.naver?code=005930
- 2026년 3월 4일 코스피 사상 최대 하락률·VKOSPI·거래대금: https://m.news.nate.com/view/20260304n28429
- 2026년 3월 4일 서킷브레이커: https://www.mt.co.kr/stock/2026/03/04/2026030411404835941
- 2026년 3월 5일 반등: https://m.news.nate.com/view/20260305n28396
- 2026년 3월 31일 코스피: https://view.asiae.co.kr/article/2026033115572629582
- 2020년 3월 19일 코스피: https://www.asiae.co.kr/en/article/2020031916201794710
- J.P. Morgan Guide to Retirement 2026: https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/insights/retirement-insights/guide-to-retirement-us.pdf
- MIT 패닉셀 연구 (Elkind 외, 2022): https://dspace.mit.edu/handle/1721.1/141712
- Morningstar Mind the Gap 2025: https://www.morningstar.com/content/cs-assets/v3/assets/blt9415ea4cc4157833/blt2c5c4d9171638c42/689b424311f3880edc4b4813/US_Mind_the_Gap_2025.pdf
- Thaler 외 (1997), The Effect of Myopia and Loss Aversion on Risk Taking: https://faculty.chicagobooth.edu/-/media/faculty/richard-thaler/assets/files/the-effect-of-myopia-and-loss-aversion-on-risk-taking-an-experimental-test.pdf

■ 투자 유의 사항
이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
투자 판단과 책임은 투자자 본인에게 있습니다.

#주식 #패닉셀 #하락장
```

**태그**: 패닉셀, 하락장, 주식 폭락, 코스피 폭락, 서킷브레이커, 주식 손실, 주식, 주식 투자, 주식 초보, 주식 공부, 국내 주식, 삼성전자, 장기 투자, 투자 심리, 리처드 탈러

**고정 댓글**

```
폭락한 날 매도 버튼 앞에서 이 두 가지부터 확인해 보세요.
1. 오늘이 서킷브레이커가 걸릴 만큼 크게 떨어진 날인가 (그렇다면 결정은 내일로)
2. 이 돈을 1~2년 안에 써야 하는가

여러분은 폭락장에서 다 팔아 본 적이 있나요? 그 뒤 어떻게 다시 시작했는지 댓글로 나눠 주세요.
※ 이 영상은 투자 권유가 아닙니다. 특정 종목 추천·리딩방 홍보 댓글은 삭제합니다.
```

## 4. 스토리보드

장면 31개 (장면마다 마지막 문장 끝 직전 still)

| | | |
|---|---|---|
| <img src="../../out/panicsell-2026-10/storyboard/S01.jpg" width="100%"><br><b>S01</b> 문장 1 · 0:00.0–0:06.3<br><sub>1: 뉴스 카드(2026년 3월 4일 · 코스피) → -12% 카운트다운(파랑) → '넘게 · 하루 만에'</sub> | <img src="../../out/panicsell-2026-10/storyboard/S02.jpg" width="100%"><br><b>S02</b> 문장 2–6 · 0:06.3–0:29.4<br><sub>2: 계좌 카드 등장, 막대가 삼성전자(잉크)로 0 → 4,000만 원, 평가손익 0원 + 오른쪽 '닷새 전' / 3: 뉴스 카드 '반도체가 잘 팔린다' + '오…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S03.jpg" width="100%"><br><b>S03</b> 문장 7–8 · 0:29.4–0:39.2<br><sub>7: 찢어진 종이 전환(네이비), '다음 날' + 큰 날짜 '3월 4일' / 8: 서킷브레이커 카드(오전 11시쯤) → 일시정지 표시 + '시장 전체 거래 20분…</sub> |
| <img src="../../out/panicsell-2026-10/storyboard/S04.jpg" width="100%"><br><b>S04</b> 문장 9–11 · 0:39.2–0:53.7<br><sub>9: S02의 계좌 카드(머리 '3월 4일') 평가손익 -400만 → -800만 원 + '넘게', 카드가 흔들림 / 10: 뉴스 카드 3장이 쌓임 '전쟁 확대' …</sub> | <img src="../../out/panicsell-2026-10/storyboard/S05.jpg" width="100%"><br><b>S05</b> 문장 12–14 · 0:53.7–1:06.8<br><sub>12: 삼성전자 실제 종가 선 — 산 날 → 3월 4일 다 판 날(회색) → 다음 날 빨강 상승 '+11% 넘게' / 13: '판 가격' 점선, 7주 뒤 점(점선…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S06.jpg" width="100%"><br><b>S06</b> 문장 15–16 · 1:06.8–1:18.5<br><sub>15: 왼쪽 '시장이 빼앗아 감'(회색)에 취소선 → 오른쪽 '겁에 질려 내던진'(형광펜) + 파랑 상자 800만 원 / 16: 모두 퇴장, 휴대폰 화면 '삼성전…</sub> |
| <img src="../../out/panicsell-2026-10/storyboard/S07.jpg" width="100%"><br><b>S07</b> 문장 17–21 · 1:18.5–1:38.9<br><sub>17: 파랑 선 3개가 함께 내려감 + '시장 전체 ↓' (개념도) / 18·19·20: 생각 말풍선이 자막마다 하나씩 / 21: 모두 퇴장, '겁 > 판단' 칩…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S08.jpg" width="100%"><br><b>S08</b> 문장 22–23 · 1:38.9–1:50.4<br><sub>22: '3월 4일' 칩 + '변동성 지수 VKOSPI', 80 카운트업 + '넘어', '사상 최고'(형광펜) / 23: 숫자를 둘러싼 반원 게이지가 그려지고 바…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S09.jpg" width="100%"><br><b>S09</b> 문장 24–26 · 1:50.4–2:06.6<br><sub>24: '코스피 하루 거래대금' 58조 원 카운트업 + '넘게', '사상 최대'(형광펜) / 25: 작은 계좌 아이콘 12개 — 첫째는 '사연자'(진하게), 나머…</sub> |
| <img src="../../out/panicsell-2026-10/storyboard/S10.jpg" width="100%"><br><b>S10</b> 문장 27–31 · 2:14.6–2:40.4<br><sub>27: 번호 타이틀 01 '크게 오르는 날은' / (뒷줄) '크게 떨어진 날 바로 뒤에'('바로 뒤에' 형광펜) / 28: 사례 카드① '2026년 · 코스피',…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S11.jpg" width="100%"><br><b>S11</b> 문장 32–34 · 2:40.4–2:58.2<br><sub>32: 카드 '미국 자산운용사 · JP모건' / (뒷줄) 'S&P 500 지수' + 타임라인 2006년 → 2025년 '20년' / 33: 퇴장, 막대 비교 — …</sub> | <img src="../../out/panicsell-2026-10/storyboard/S12.jpg" width="100%"><br><b>S12</b> 문장 35–36 · 2:58.2–3:09.7<br><sub>35: '가장 많이 오른 10일' 빨강 점 10개 → 6개만 남고 4개는 회색, 괄호 + '6일' + '가장 크게 떨어진 10일과 2주 안'(2주 안 형광펜) /…</sub> |
| <img src="../../out/panicsell-2026-10/storyboard/S13.jpg" width="100%"><br><b>S13</b> 문장 37–39 · 3:09.7–3:26.1<br><sub>37: 번호 타이틀 02 ('훨씬 어렵다' 형광펜) / 38: 왼쪽 카드 '3월 4일 · 판 가격' / (뒷줄) 빨강 화살표 → 오른쪽 위 카드 '다음 날 · 다…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S14.jpg" width="100%"><br><b>S14</b> 문장 40–41 · 3:26.1–3:38.9<br><sub>40: 연구 카드 '미국 MIT 연구진' + '2003년부터 13년' / (뒷줄) '증권 계좌 65만여 개' / 41: '패닉셀'(형광펜) + '한 달 사이 주식…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S15.jpg" width="100%"><br><b>S15</b> 문장 42–43 · 3:38.9–3:49.6<br><sub>42: 10×10 와플 31칸이 채워짐 + '패닉셀 중' 31%(형광펜) + '다시 주식으로 돌아오지 않음' / 43: S07의 말풍선 '일단 팔고, 잠잠해지면 …</sub> |
| <img src="../../out/panicsell-2026-10/storyboard/S16.jpg" width="100%"><br><b>S16</b> 문장 44–47 · 3:49.6–4:08.4<br><sub>44: 번호 타이틀 03 ('지나고 나서야' 형광펜) / 45: 3월 4일 '판 날' 점 + 그 높이의 회색 점선 / 46: '코스피' 칩, 실제 지수 선 3월 …</sub> | <img src="../../out/panicsell-2026-10/storyboard/S17.jpg" width="100%"><br><b>S17</b> 문장 48–49 · 4:08.4–4:18.3<br><sub>48: '더 싸게 다시 사려면 → 둘 다 맞혀야'(둘 다 형광펜) + 과녁 카드 '파는 날' ✓ + '사는 날' ✓ / 49: 머리글이 파랑 '겁에 질린 날'로 …</sub> | <img src="../../out/panicsell-2026-10/storyboard/S18.jpg" width="100%"><br><b>S18</b> 문장 50–53 · 4:18.3–4:48.2<br><sub>50: 번호 타이틀 04 '사고판 시점 때문에' / (뒷줄) '수익이 줄어든다' / 51: 카드 '모닝스타 · 미국 펀드 평가사 · 2024년까지' / (뒷줄) …</sub> |
| <img src="../../out/panicsell-2026-10/storyboard/S19.jpg" width="100%"><br><b>S19</b> 문장 54–56 · 4:48.2–5:01.3<br><sub>54: 헤드라인 '긴 하락장도 있다' / 55: '2008년 금융위기 · 코스피' 칩, 실제 지수 선이 1년 동안 파랑으로 내려가 '1년 만에 절반 넘게 ↓' /…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S20.jpg" width="100%"><br><b>S20</b> 문장 57–58 · 5:01.3–5:12.4<br><sub>57: 왼쪽 카드 '무조건 버티기'(회색)에 취소선 / (뒷줄) 오른쪽 카드 '겁이 결정하지 않도록' + '미리 세운 기준'(형광펜) / 58: 카드 퇴장, '하…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S21.jpg" width="100%"><br><b>S21</b> 문장 59–61 · 5:12.4–5:29.8<br><sub>59: 밝은 크림 전환, 번호 타이틀 '첫째 1~2년 안에 쓸 돈은 넣지 않기'(1~2년 형광펜) / 60: 패널 '2008년' + S19와 같은 모양의 작은 선…</sub> |
| <img src="../../out/panicsell-2026-10/storyboard/S22.jpg" width="100%"><br><b>S22</b> 문장 62–63 · 5:29.8–5:38.8<br><sub>62: S02의 계좌 카드(간단형, '예시 · 4,000만 원'), 막대 끝 1/4이 빗금(현금)으로 바뀌며 '1년 안에 쓸 돈 1,000만 원' / 63: 아래…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S23.jpg" width="100%"><br><b>S23</b> 문장 64–67 · 5:38.8–6:03.7<br><sub>64: 번호 타이틀 '둘째 크게 떨어진 날엔 하루 기다리기'('하루 기다리기' 형광펜) / 65: 파랑 날짜 칸 '서킷브레이커 걸린 날'(S03과 같은 일시정지 …</sub> | <img src="../../out/panicsell-2026-10/storyboard/S24.jpg" width="100%"><br><b>S24</b> 문장 68–69 · 6:03.7–6:14.8<br><sub>68: 번호 타이틀 '셋째 꼭 팔아야 한다면, 정해 둔 만큼만', 잉크 막대 + '전부'에 취소선 / 69: 막대가 3칸으로 나뉘고 오른쪽 1칸이 빗금(현금), …</sub> |
| <img src="../../out/panicsell-2026-10/storyboard/S25.jpg" width="100%"><br><b>S25</b> 문장 70–72 · 6:14.8–6:32.4<br><sub>70: 오른쪽에 S02의 계좌 카드(머리 '3월 4일', -800만 원 넘게), 막대 3칸 중 1칸이 현금으로 '삼성전자 2/3 · 판 1/3 → 현금' / (뒷…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S26.jpg" width="100%"><br><b>S26</b> 문장 73–75 · 6:32.4–6:49.4<br><sub>73: 번호 타이틀 '넷째 다시 살 날짜와 금액도 정해 두기' / 74: 날짜 칸 4개 '금요일 3월 6일 · 13일 · 20일 · 27일' + 각 '판 돈 1/…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S27.jpg" width="100%"><br><b>S27</b> 문장 76–78 · 6:49.4–7:05.2<br><sub>76: 오른쪽 S02의 계좌 카드(머리 '4월 23일', 막대 4칸 다시 삼성전자) 평가손익 -800만 → -190만 원 '정도' / 77: 왼쪽 '다시 사지 않…</sub> |
| <img src="../../out/panicsell-2026-10/storyboard/S28.jpg" width="100%"><br><b>S28</b> 문장 79–82 · 7:05.2–7:25.9<br><sub>79: 번호 타이틀 '다섯째 계좌는 정해 둔 날에만 확인' / 80: 카드 '노벨 경제학상 · 리처드 탈러 교수 등' / (뒷줄) '1997년 실험' / 81: …</sub> | <img src="../../out/panicsell-2026-10/storyboard/S29.jpg" width="100%"><br><b>S29</b> 문장 83–85 · 7:25.9–7:41.4<br><sub>83: 왼쪽 '매달 본 학생' 주식 41% 카운트 + 나눔 막대 41% / 84: 오른쪽 '1년에 한 번 본 학생' 주식 70% 가까이 + 막대 70% / 85:…</sub> | <img src="../../out/panicsell-2026-10/storyboard/S30.jpg" width="100%"><br><b>S30</b> 문장 86–88 · 7:41.4–8:01.8<br><sub>86: 3월·4월 달력, 마지막 금요일(27일·24일)에 동그라미 + '○ = 마지막 금요일' / 87: 오른쪽 '3월 27일 -670만 원'(파랑) / (뒷줄)…</sub> |
| <img src="../../out/panicsell-2026-10/storyboard/S31.jpg" width="100%"><br><b>S31</b> 문장 89–92 · 8:01.8–8:21.0<br><sub>89: 두 열 요약 — 왼쪽 '위험한 이유' 01~04 / (뒷줄) 오른쪽 '지킬 기준' 첫째~다섯째 / 90: 요약 퇴장, 휴대폰 '다 팔고 싶은 날' ✓ '오…</sub> |  |  |

전체 장면 구성표: `out/panicsell-2026-10/scene_plan.md` · 모든 still: `out/panicsell-2026-10/storyboard/index.html`


## 5. 대본 (번호 = 대본 문장 번호)

**사연 파트**

1. 2026년 3월 4일, 코스피가 하루 만에 12% 넘게 떨어졌어요.
2. 저는 그 닷새 전 4천만 원으로 삼성전자를 샀어요.
3. 반도체가 잘 팔린다는 뉴스를 보고 오래 들고 갈 생각이었죠.
4. 그런데 산 다음 날, 미국과 이스라엘이 이란을 공격했어요.
5. 연휴 뒤 첫 거래일인 3월 3일, 계좌는 -400만 원이 됐어요.
6. 그래도 금방 회복하겠지 하고 버텼죠.
7. 하지만 다음 날은 차원이 달랐습니다.
8. 오전 11시쯤에는 서킷브레이커로 시장 전체의 거래가 20분 동안 멈췄어요.
9. 계좌는 어느새 -800만 원이 넘어 있었고요.
10. 전쟁이 커지면서 유가와 환율이 치솟는다는 뉴스가 쏟아졌어요.
11. 이러다 전부 잃겠다는 생각에 장 마감 직전 모두 팔았어요.
12. 그런데 바로 다음 날 삼성전자는 11% 넘게 올랐습니다.
13. 7주 뒤에는 제가 판 가격보다 30% 넘게 올라 있었어요.
14. 처음 산 가격도 이미 넘어 있었죠.
15. 시장이 빼앗아 간 게 아니라, 제가 겁에 질려 내던진 800만 원이었어요.
16. 다음 날 빨갛게 오른 주가를 보면서 한참 동안 아무것도 할 수 없었어요.

**진행자 파트**

17. 시장 전체가 무너지는 날이면 많은 분들이 이런 생각을 하죠.
18. 이러다 정말 0원이 되는 거 아니야?
19. 일단 팔고 잠잠해지면 다시 사면 되지.
20. 뉴스마다 더 떨어진다고 하잖아.
21. 이런 식으로 겁이 판단을 앞서면, 가격이 가장 낮을 때 가장 많이 팔게 됩니다.
22. 실제로 3월 4일, 변동성 지수 VKOSPI는 80을 넘어 사상 최고였습니다.
23. 시장이 느끼는 공포를 숫자로 보여 주는 지수죠.
24. 코스피 하루 거래대금도 58조 원을 넘어 사상 최대였습니다.
25. 그날 두려움에 떤 사람이 사연자 혼자가 아니었던 겁니다.
26. 그럼 하락장에서 전부 팔아 버리는 게 왜 위험한지 하나씩 짚어 보겠습니다.

> 🟨 [장면] 투자 권유가 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
> 사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
> 과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
> 투자 판단과 책임은 투자자 본인에게 있습니다.

**문제 분석 파트**

27. 첫 번째 문제는 크게 오르는 날이 크게 떨어진 날 바로 뒤에 몰려 있다는 것입니다.
28. 3월 4일은 코스피 역사상 하루 하락률이 가장 큰 날이었습니다.
29. 하루 뒤 코스피는 거꾸로 10% 가까이 올랐죠.
30. 2020년 코로나 때도 그랬습니다.
31. 3월 19일 8% 넘게 떨어진 코스피는 다음 날 7% 넘게 올랐습니다.
32. 미국 자산운용사 JP모건이 2006년부터 20년 동안 S&P 500 지수를 분석했습니다.
33. 1천만 원을 계속 넣어 뒀다면 8천만 원이 넘었습니다.
34. 그런데 가장 많이 오른 10일만 놓쳐도 3,600만 원에 그쳤죠.
35. 그 10일 중 6일은 가장 크게 떨어진 10일과 2주 안에 붙어 있었습니다.
36. 폭락한 날 팔고 나가면 바로 뒤에 오는 반등을 놓치기 쉽다는 뜻입니다.
37. 두 번째는 한번 팔고 나면 다시 사기가 훨씬 어렵다는 것입니다.
38. 사연자가 판 다음 날 다시 사려면 판 가격보다 11% 넘게 비싸게 사야 했습니다.
39. 내가 틀렸다는 걸 인정해야 하니 쉽게 손이 가지 않죠.
40. 미국 MIT 연구진은 2003년부터 13년 동안 증권 계좌 65만여 개를 살펴봤습니다.
41. 한 달 사이 주식을 90% 넘게 정리한 패닉셀을 찾아봤죠.
42. 그중 31%는 다시는 주식으로 돌아오지 않았습니다.
43. 잠잠해지면 다시 사겠다는 계획이 생각처럼 되지 않는 이유입니다.
44. 세 번째는 바닥이 지나고 나서야 보인다는 것입니다.
45. 사연자가 판 3월 4일도 바닥은 아니었습니다.
46. 코스피는 3월 31일 그보다 더 낮은 5,052까지 내려갔죠.
47. 그런데 그 뒤 한 달도 안 돼 30% 넘게 올랐습니다.
48. 팔았다가 더 싸게 다시 사려면 파는 날과 사는 날을 둘 다 맞혀야 합니다.
49. 겁에 질린 날 그 두 가지를 맞히기는 훨씬 더 어렵죠.
50. 네 번째는 사고판 시점 때문에 투자자가 가져가는 수익이 줄어든다는 것입니다.
51. 미국 펀드 평가사 모닝스타가 2024년까지 10년 동안 미국 펀드를 분석했습니다.
52. 펀드 자체는 1년에 8.2%씩 벌었는데, 투자자들이 실제로 번 돈은 7.0%였습니다.
53. 1년에 1.2%포인트, 전체 수익의 15% 정도가 사고판 시점 때문에 사라진 겁니다.
54. 물론 하락장이 길게 이어질 때도 있습니다.
55. 2008년 금융위기 때 코스피는 1년 만에 절반 넘게 떨어졌습니다.
56. 이전 고점을 되찾기까지는 3년이 넘게 걸렸죠.
57. 그래서 무조건 버티라는 게 아니라, 겁이 결정하지 않도록 미리 기준을 세워 둬야 합니다.
58. 그렇다면 하락장에서는 어떻게 해야 할까요?

**올바른 방법 설명 파트**

59. 첫째, 1~2년 안에 쓸 돈은 처음부터 주식에 넣지 않는 것입니다.
60. 2008년처럼 회복에 몇 년이 걸리는 하락장도 있기 때문입니다.
61. 그 사이에 꺼내 써야 할 돈이 주식에 묶여 있으면 바닥에서라도 팔 수밖에 없습니다.
62. 예를 들어 4천만 원 중 1년 안에 쓸 돈이 1천만 원이라고 해 보죠.
63. 그러면 주식에는 3천만 원만 넣는 겁니다.
64. 둘째, 크게 떨어진 날에는 사고팔지 않고 하루를 기다리는 것입니다.
65. 특히 서킷브레이커가 걸릴 만큼 시장이 흔들린 날에는 결정을 다음 날로 미룹니다.
66. 사연자가 같은 결정을 하루만 늦춰 3월 5일에 팔았다면 손실은 460만 원이었습니다.
67. 800만 원 넘게 잃은 것과 비교하면 절반 가까이 줄어든 거죠.
68. 셋째, 꼭 팔아야겠다면 전부가 아니라 정해 둔 만큼만 나눠 파는 것입니다.
69. 예를 들어 한 번에 3분의 1까지만 판다고 정해 두는 겁니다.
70. 사연자가 3월 4일 3분의 1만 팔았다면, 4월 23일 계좌는 -170만 원 정도였습니다.
71. 전부 판 사연자보다 손실이 650만 원 가까이 적었죠.
72. 판 쪽이 틀려도 크게 틀리지 않게 만드는 방법입니다.
73. 넷째, 팔았다면 다시 살 날짜와 금액도 함께 정해 두는 것입니다.
74. 예를 들어 판 돈을 4주 동안 매주 금요일에 4분의 1씩 다시 사는 겁니다.
75. 사연자가 이렇게 했다면 평균 18만 8천 원 정도에 다시 샀을 겁니다.
76. 4월 23일 계좌는 -190만 원 정도였을 겁니다.
77. 다시 사지 않았을 때보다 600만 원 넘게 나은 결과죠.
78. 판 가격보다 비싸게 사야 해도, 정해 둔 날이 되면 그대로 사는 게 핵심입니다.
79. 다섯째, 계좌는 정해 둔 날에만 확인하는 것입니다.
80. 노벨 경제학상을 받은 리처드 탈러 교수 등이 1997년에 발표한 실험이 있습니다.
81. 대학생들에게 가상의 주식과 채권에 돈을 나눠 넣게 했죠.
82. 그리고 결과를 보여 주는 횟수만 다르게 했습니다.
83. 결과를 매달 본 학생들은 주식에 41%만 넣었습니다.
84. 1년에 한 번 본 학생들은 70% 가까이 넣었죠.
85. 자주 볼수록 손실이 자주 보이니 겁을 먹고, 결국 가장 적게 벌었습니다.
86. 예를 들어 계좌는 매달 마지막 금요일에만 열어 보는 겁니다.
87. 사연자라면 3월 27일에는 -670만 원, 4월 24일에는 +55만 원을 봤을 겁니다.
88. 매일 보지 않았다면 3월 4일의 공포를 계좌 화면으로 마주할 일도 없었겠죠.

**마무리**

89. 이렇게 해서 하락장에서 다 팔아 버리면 위험한 이유와 지킬 기준을 알아보았습니다.
90. 다 팔고 싶은 날일수록 오늘이 폭락한 날인지, 이 돈을 곧 써야 하는지부터 확인하세요.
91. 성공 투자 하셨으면 좋겠습니다.
92. 감사합니다.


## 6. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
