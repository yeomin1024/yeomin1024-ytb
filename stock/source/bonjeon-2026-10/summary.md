# bonjeon-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py stock bonjeon-2026-10` (2026-10-12 12:57). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **본전만 오면 팔겠다고 버티다가 -200만원이 -1,600만원이 됐습니다. 손절 못 한 사람들의 최악의 결말**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 133 / 자막 149, 길이 11:25 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–6 · 진행자 7–133 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/bonjeon-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 본전만 오면 팔겠다고 버티다가 -200만원이 -1,600만원이 됐습니다. 손절 못 한 사람들의 최악의 결말 `속마음 · 손실→손실 · 최악의 결말` 59자 — 짝 썸네일: thumbnail_1 (계좌 숫자 반전)
- [ ] **T2.** -200만원일 때 못 팔고 버티다 반년 만에 1,600만원을 날렸습니다. 본전만 기다린 사람이 망하는 과정 `장면 · 손실→손실(기간) · ~하는 과정(시험)` 59자 — 짝 썸네일: thumbnail_2 (인물·감정 장면)
- [ ] **T3.** (짧은 변형) 반년 버티다 -200만원이 -1,600만원이 됐습니다. 물린 주식 못 판 사람들의 공통점 `행동 · 손실→손실 · 공통점` 49자 — 짝 썸네일: thumbnail_3 (검은 배경 제목형 — 채택 제목 문구)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (계좌 카드)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 작은 손실 **-200만 원이 반년 만에 -1,600만 원**(8배)으로 커진 **계좌 숫자 반전**이 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 시작 숫자 | -200만 원 | 파랑 #2D6CDF | 손실 = 파랑 (빨강 금지) |
| 펀치 (위쪽) | 반년 만에 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (노랑 상자는 이 1곳만) |
| 카드 결과 숫자 | -1,600만 원 | 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 본전 기다린 -200만원이 | 흰색 + 검정 외곽선 | — (14자) |
| 하단 2줄 | -1,600만원이 됐다 | 흰색 + 검정 외곽선 | "-1,600만원"만 노랑 #FFD400 (12자, 2줄 합 26자) |

- 강조색 2곳: 노랑 형광펜 "반년 만에", 노랑 글자 "-1,600만원". 손실 숫자는 빨강으로 쓰지 않는다 (카드는 파랑, 하단은 노랑 — `stock/guides/thumbnail_rules.md` 1번).
- 하단 2줄은 T1 앞 문장("본전만 오면 팔겠다고 버티다가 -200만원이 -1,600만원이 됐습니다")을 줄인 것. 2줄 합 26자 안에 넣으려고 "본전만 오면 팔겠다고 버티다가"를 "본전 기다린"으로 줄였다.
- 하단 2줄은 제목 표기("-200만원", "-1,600만원"), 카드는 영상 계좌 카드 표기("-200만 원", "-1,600만 원")다. 값은 같다.
- 펀치 "반년 만에"는 문장 6 "반년을 버텼을까요"와 실제 기간(2025-07-01 매수 → 12-30 매도)이다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos, no stock names). Inside the card, on the left: the text
"-200만 원" in medium-size blue (#2D6CDF) bold letters. In the middle: a thick blue (#2D6CDF) arrow that steps down
like a staircase several times toward the lower right, with the label "반년 만에" in black bold letters over a bright
yellow (#FFD400) highlighter stripe just above the arrow. On the right: a solid blue (#2D6CDF) rounded box with the huge
white bold text "-1,600만 원", the largest element in the image. No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "본전 기다린 -200만원이", line 2 "-1,600만원이 됐다". The word "-1,600만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 반년 동안 계좌를 외면하다 결국 손실을 마주한 순간의 **사람 표정**이 숫자 카드보다 "내 얘기"라는 감정을 더 끈다 (작은 채널 성공 썸네일 15개 중 14개에 사람·캐릭터 — `stock/guides/thumbnail_rules.md` 2번)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 반년을 버텼다 | 흰색 #F7F3EA ("반년"만 검정) | "반년"에 노랑 상자 (글자 전체 높이, 노랑 상자는 이 1곳만) |
| 결과 숫자 (위쪽) | -1,600만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |
| 하단 1줄 | -200만원일 때 못 팔고 | 흰색 + 검정 외곽선 | — (14자) |
| 하단 2줄 | 1,600만원 날렸다 | 흰색 + 검정 외곽선 | "1,600만원"만 노랑 #FFD400 (11자, 2줄 합 25자) |

- 강조색 2곳: 노랑 상자 "반년", 노랑 "1,600만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (위쪽은 파랑 상자, 하단은 노랑).
- 하단 2줄은 T2 앞 문장("-200만원일 때 못 팔고 버티다 반년 만에 1,600만원을 날렸습니다")을 줄인 것. "반년"은 펀치에 있어 하단에 다시 쓰지 않았다.
- 펀치 "반년을 버텼다"는 문장 6 "반년을 버텼을까요"의 말이다.
- 하단 2줄은 제목 표기("-200만원", "1,600만원"), 위쪽 상자는 영상 계좌 카드 표기("-1,600만 원")다. 값은 같다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned living room late at night, lit only by a small floor lamp next to a sofa. On the
left 40% of the frame, a fictional Korean man in his early 40s, an office worker just home from work (white shirt, loosened
tie), sitting on the sofa edge and finally looking at his smartphone after avoiding it for months, one hand pressed to his
forehead, frozen stunned and regretful expression, face lit by the phone's cold light. The face and the phone are in the
upper 60% of the frame; the lower body fades into darkness at the bottom. The phone screen shows only a simple blue line
that steps down like a staircase and keeps falling, no app interface, no text. Fictional person, not resembling any real
or famous person, natural Korean features, realistic photo style. No gray hair, no retirement props. In the upper right
area, large bold text "반년을 버텼다" in off-white, where only the word "반년" sits on a solid bright yellow (#FFD400) box
with black text. Below it, still in the upper 60%, a wide solid blue (#2D6CDF) rounded box with a thin white border
containing the huge white bold text "-1,600만 원", the largest element. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "-200만원일 때 못 팔고", line 2 "1,600만원 날렸다". In line 2, "1,600만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 검은 배경 제목형 (채택 제목 문구)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 그림 없이 **검은 배경에 채택 제목 앞 문장만** 크게 넣은 글자 썸네일이 사진 썸네일 사이에서 눈에 띄어 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 본전만 오면 팔겠다고 | 흰색 #FFFFFF | — (11자) |
| 2줄 | 버티다가 -200만원이 | "버티다가" 빨강 #E63B2E, 나머지 흰색 | 손실을 부른 행동 단어 = 빨강 (12자) |
| 3줄 | -1,600만원이 됐습니다 | "-1,600만원" 노랑 #FFD400, 나머지 흰색 | 손실 금액 = 노랑, 빨강 금지 (14자) |

- 채택 제목 앞 문장 "본전만 오면 팔겠다고 버티다가 -200만원이 -1,600만원이 됐습니다."를 **글자 그대로** 3줄로 나눴다 (끝 마침표만 뺌). 뒤 문장(결말 장치 "손절 못 한 사람들의 최악의 결말")은 넣지 않는다.
- 줄 길이(띄어쓰기 포함): 11자 · 12자 · 14자 — 모두 14자 이내, 어절 단위로 끊음
- 숫자 반전("-200만원이 -1,600만원이")은 2줄 끝 → 3줄 첫머리로 바로 이어지게 나눴다.
- 강조 2곳: 빨강 "버티다가"(행동 단어 — 숫자가 아닌 단어에만, `stock/guides/thumbnail_rules.md` 2번), 노랑 "-1,600만원"(손실). 이 제목에는 수익 금액이 없어서 빨강이 '수익'으로 읽힐 숫자가 없다. "-200만원"은 흰색으로 두어 작은 손실 → 큰 손실의 차이를 노랑 하나로 보이게 했다 (강조를 더 원하면 "-200만원"도 노랑 — 그래도 3곳 이하).

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 3 lines with tight line spacing:
line 1 "본전만 오면 팔겠다고", line 2 "버티다가 -200만원이", line 3 "-1,600만원이 됐습니다".
All text pure white (#FFFFFF) except "-1,600만원" at the start of line 3 in bright yellow (#FFD400) and "버티다가" at the start of line 2 in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
2주 만에 -200만 원이던 손실을 본전만 기다리며 들고 있다가, 반년 뒤 -1,600만 원에 정리한 사연입니다.
손절을 못 하게 만드는 본전 심리가 작은 손실을 키우는 5단계와, 날짜와 사건으로 미리 정해 두는 살아남는 장치 5가지를 정리했습니다.

■ 이 영상에서 다루는 것
- 1단계 작은 손실을 잠깐이라 부른다 (2024년 국내 종목 보고서 2만 426건 중 매도 의견 4건)
- 2단계 본전이 매도 기준이 된다 (손실이 300만 원대로 줄어든 날에도 팔지 못한 이유, 역대 최대 실적에도 돌아오지 않은 주가)
- 3단계 계좌를 열지 않는다 (2022년 하락장 때 증권 앱 1인당 사용 시간 40% 넘게 감소)
- 4단계 팔면 오를 것 같아 못 판다 (본전을 기다린 반년 동안 코스피는 30% 넘게 상승)
- 5단계 지쳐서 가장 아플 때 판다 (코스피 4,000 돌파 주에도 NH투자증권 고객 54.6%가 손실)
- 살아남는 장치 5가지: 잠깐에 날짜 붙이기, 본전 대신 절반부터, 실적 발표 다음 날엔 계좌 열기, 판 뒤를 기록하기, 사기 전에 팔 조건 카드 쓰기

■ 챕터
0:00 사연: 본전 기다리다 -200만 원이 -1,600만 원
0:26 왜 본전만 기다릴까
1:45 1단계 작은 손실을 잠깐이라 부른다
2:53 2단계 본전이 매도 기준이 된다
3:48 3단계 계좌를 열지 않는다
4:49 4단계 팔면 오를 것 같아 못 판다
5:35 5단계 지쳐서 가장 아플 때 판다
6:56 장치 1 잠깐에 날짜를 붙인다
8:00 장치 2 본전 대신 절반부터
8:49 장치 3 실적 발표 다음 날엔 계좌를 연다
9:36 장치 4 판 뒤를 기록한다
10:17 장치 5 사기 전에 팔 조건 카드
11:04 정리

■ 사연에 대해
이 영상의 사연은 실제 주가 흐름(크래프톤, 2025년 7월~12월)을 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시입니다.
이 영상의 내레이션은 AI 음성으로 만들었습니다.

■ 출처
- 크래프톤 주가 2025-07-01 (유진투자증권 리포트): https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%9C%A0%EC%A7%8420250702%ED%81%AC%EB%9E%98%ED%94%84%ED%86%A4.pdf
- 크래프톤 주가 2025-07-15 (유안타증권 리포트 브리핑): https://news.nate.com/view/20250716n09548
- 크래프톤 주가 2025-07-29 (유진투자증권 리포트): https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%9C%A0%EC%A7%8420250730%ED%81%AC%EB%9E%98%ED%94%84%ED%86%A4.pdf
- 크래프톤 주가 2025-07-30: https://www.tgdaily.co.kr/news/articleView.html?idxno=341323
- 크래프톤 주가 2025-08-01: https://www.tgdaily.co.kr/news/articleView.html?idxno=341376
- 크래프톤 주가 2025년 8~11월, 3분기까지 영업이익 (머니S 2025-11-07): https://www.moneys.co.kr/article/2025110713544432799
- 크래프톤 52주 신저가 (아시아경제 2025-11-05): https://core.asiae.co.kr/article/2025110509233907695
- 목표주가 줄하향 (머니투데이 2025-12-17): https://www.mt.co.kr/tech/2025/12/17/2025121616050233412
- 크래프톤 주가 2025-12-30 (헤럴드경제 2026-01-03): https://www.heraldk.com/article/2026010318000000819
- 크래프톤 주가 2026-01-08 (아시아경제 2026-01-13): https://core.asiae.co.kr/article/2026011316354025831
- 크래프톤 주가 2026-05-04 (키움증권): https://bbn.kiwoom.com/rfCR12069
- 크래프톤 주가 2026년 10월: https://stockanalysis.com/quote/krx/259960/statistics/
- 크래프톤 2분기 실적: https://www.bloter.net/news/articleView.html?idxno=641078
- 경쟁 신작과 이용자 감소 (딜사이트): https://dealsite.co.kr/articles/152486
- 2024년 종목 보고서 중 매도 의견 (머니투데이 2025-03-12): https://v.daum.net/v/20250312160826018
- 2022년 증권 앱 사용 시간 (이투데이 2022-07-05, 모바일인덱스): https://www.etoday.co.kr/news/view/2150400
- NH투자증권 고객 손실 현황 (파이낸셜뉴스 2025-11-10): https://www.fnnews.com/news/202511100800479153
- 포스코홀딩스 2023년 상반기 개인 매수 1위 (머니투데이 2023-07-29): https://www.mt.co.kr/stock/2023/07/29/2023072714434596759
- 코스피 첫 4,000 돌파 (뉴시스 2025-10-27): https://mobile.newsis.com/view/NISX20251027_0003378556
- 코스피 첫 5,000 돌파 (이투데이 2026-01-27): https://www.etoday.co.kr/news/view/2549989
- 코스피 2025-12-30 종가 (머니투데이): https://www.mt.co.kr/stock/2025/12/30/2025123015340935056

■ 투자 유의 사항
이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
투자 판단과 책임은 투자자 본인에게 있습니다.

#주식 #손절 #본전
```

**태그**: 손절, 손절 못하는 이유, 본전 심리, 물린 주식, 주식 손실, 주식 물림, 손절 기준, 주식, 주식 투자, 주식 초보, 주식 공부, 크래프톤, 게임주, 배틀그라운드

**고정 댓글**

```
물린 주식이 있다면, 다음 두 가지만 오늘 적어 보세요.
1. 언제까지 본전이 안 오면 정리를 시작할지 (날짜 하나)
2. 손실이 줄어드는 날이 오면 얼마를 먼저 팔지 (예: 절반)

여러분은 본전만 기다리다 손절 시기를 놓쳐 본 적이 있나요? 그때 결국 어떻게 정리하셨는지 댓글로 나눠 주세요.
※ 이 영상은 투자 권유가 아닙니다. 특정 종목 추천·리딩방 홍보 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 본전만 오면 판다던 -200만 원이, -1,600만 원이 됐어요.
2. 작년 7월, 크래프톤을 5천만 원어치 샀죠.
3. 2주 만에 -200만 원, 잠깐이라 생각했어요.
4. 8월 말엔 손실이 300만 원대로 줄었는데도, 본전이 아니라 안 팔았죠.
5. 결국 연말에 지쳐서 다 팔았어요.
6. 본전이 뭐라고, 반년을 버텼을까요.

**진행자 파트** — 🎙 진행자

7. 물린 주식 앞에서 우리가 하는 생각은 대개 비슷합니다.
8. 조금 빠진 건데, 금방 돌아오겠지.
9. 본전만 오면 그때 깔끔하게 팔아야지.
10. 내가 팔기만 하면 꼭 오르더라.
11. 이런 식으로 산 값이 매도 기준이 되면, 작은 손실은 몇 달짜리 큰 손실로 자랍니다.
12. 사연 속 크래프톤은 배틀그라운드를 만든 국내 게임 대장주입니다.
13. 2025년 하반기, 경쟁 신작이 쏟아졌고 크래프톤 기대작 출시는 2026년으로 밀렸습니다.
14. 그 뒤 실적이 예상에 못 미칠 때마다, 주가는 한 계단씩 내려갔습니다.
15. 본전을 기다리는 사람들은 거의 같은 순서를 밟습니다.
16. 작은 손실을 잠깐이라 부르고, 본전을 기준으로 삼고, 계좌를 닫습니다.
17. 그러다 팔면 오를까 봐 못 팔고, 결국 가장 아플 때 지쳐서 팝니다.
18. 코스피가 처음 5,000을 넘은 올해 같은 장에서는, 이 순서가 더 아프게 느껴집니다.
19. 내 종목만 제자리인 게 더 크게 보이니까요.
20. 그럼 이 다섯 단계를 하나씩 짚어 보겠습니다.

> 🟨 [장면] 투자 권유가 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
> 사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
> 과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
> 투자 판단과 책임은 투자자 본인에게 있습니다.

**망하는 과정 파트** — 🎙 진행자

21. 혹시 지금 계좌에, 몇 달째 파란 종목이 하나쯤 있으신가요?
22. 첫 번째 단계는 작은 손실을 잠깐이라고 부르는 것입니다.
23. 이 정도 손실은 손실도 아니지.
24. 사연자가 크래프톤을 산 값은 주당 36만 2천 원이었습니다.
25. 2주 만에 -200만 원이 됐지만, 잠깐이라고 넘겼죠.
26. 이렇게 넘기기 쉬운 건, 들려오는 말도 대부분 버티라는 쪽이기 때문입니다.
27. 2024년 한 해 국내 증권사가 낸 종목 보고서는 2만 426건이었습니다.
28. 그중 팔라는 매도 의견은 단 네 건이었죠.
29. 7월 29일에는 2분기 영업이익이 1년 전보다 25.9% 줄었다는 발표가 나왔습니다.
30. 다음 날 손실은 -490만 원으로 커졌지만, 여전히 잠깐이었습니다.
31. 문제는 잠깐에 끝나는 날짜가 없다는 겁니다.
32. 날짜가 없으니, 손실이 두 배가 넘게 커져도 계속 잠깐인 거죠.
33. 그리고 잠깐이 길어지면, 다음 단계가 찾아옵니다.
34. 두 번째 단계는 본전이 매도 기준이 되는 것입니다.
35. 여기까지 버텼는데, 본전은 받고 나와야지.
36. 8월 27일 크래프톤은 33만 9천 원까지 올랐고, 손실은 300만 원대로 줄었습니다.
37. 본전인 36만 2천 원이 아니라서, 그날도 팔지 않았습니다.
38. 그런데 산 값은 회사와 아무 상관이 없는 숫자입니다.
39. 회사는 사연자가 얼마에 샀는지 모르니까요.
40. 회사가 잘되면 언젠가 본전은 오겠지, 하는 믿음도 마찬가지입니다.
41. 크래프톤은 2025년 3분기까지 역대 최대인 1조 원 넘는 영업이익을 냈습니다.
42. 그래도 주가는 끝내 사연자가 산 값으로 돌아오지 않았습니다.
43. 본전이 기준이 되면, 손실이 줄어든 날조차 파는 날이 되지 못합니다.
44. 그런데 여기서 멈추지 않습니다.
45. 세 번째 단계는 계좌를 아예 열지 않는 것입니다.
46. 어차피 안 팔 건데, 봐서 뭐 해.
47. 9월 25일 크래프톤은 30만 원선이 깨졌고, 손실은 -860만 원이 됐습니다.
48. 11월에는 3분기 실적이 예상에 못 미쳐, 다음 날 주가가 52주 신저가를 찍었습니다.
49. 그 뒤 한 달 동안, 증권사 열 곳 넘게 목표 주가를 낮췄습니다.
50. 하지만 앱을 열지 않는 사연자에게는 어떤 소식도 닿지 않았습니다.
51. 이건 사연자만의 일이 아닙니다.
52. 2022년 하락장 때 한 대형 증권사 앱을 보면 알 수 있습니다.
53. 1인당 한 달 사용 시간이 1년 사이 393분에서 234분으로, 40% 넘게 줄었죠.
54. 계좌를 닫으면 손실은 안 보이지만, 회사가 보내는 신호도 함께 안 보입니다.
55. 그렇게 몇 달이 지나면, 이번엔 다른 두려움이 생깁니다.
56. 네 번째 단계는 팔면 오를 것 같아서 못 파는 것입니다.
57. 이제 와서 팔면, 꼭 그다음 날 오를 것 같다.
58. 11월 7일, 사연자의 손실은 이미 1,400만 원을 넘었습니다.
59. 그런데도 손이 안 나가는 건, 기억이 한쪽으로 기울어 있기 때문입니다.
60. 판 다음 날 오른 기억은 또렷하게 남고, 안 판 다음 더 떨어진 기억은 금방 흐려집니다.
61. 그사이 흘러간 시간도 공짜가 아니었습니다.
62. 사연자가 본전을 기다린 그 반년 동안, 코스피는 30% 넘게 올랐습니다.
63. 묶인 5천만 원은 그동안 다른 어디에서도 일하지 못한 셈이죠.
64. 그리고 마지막 단계는, 대개 가장 아픈 순간에 옵니다.
65. 다섯 번째 단계는 결국 지쳐서, 손실이 가장 클 때 파는 것입니다.
66. 더는 못 보겠다, 해 넘기기 전에 다 정리하자.
67. 사연자는 12월 30일, 주당 24만 6천 원에 전부 팔았습니다.
68. 손실은 -1,600만 원이었죠.
69. 그럼 끝까지 버텼다면 달랐을까요?
70. 판 지 열흘도 안 돼, 주가는 23만 5천 원까지 더 내려갔습니다.
71. 올해 5월엔 한때 28만 원을 넘었지만, 본전 36만 2천 원에는 닿지 못했습니다.
72. 그리고 10월 초 주가는 18만 원대로, 산 값의 절반 남짓입니다.
73. 버텼어도 본전은 오지 않았던 겁니다.
74. 이렇게 본전에 묶인 돈은 생각보다 흔합니다.
75. 코스피가 처음 4,000을 넘은 2025년 10월 마지막 주의 자료입니다.
76. NH투자증권 고객 240만여 명 가운데 54.6%가 손실이었습니다.
77. 손실 금액이 가장 큰 종목은 포스코홀딩스였는데요.
78. 2023년 2차전지 열풍 때, 개인이 상반기에 가장 많이 산 종목입니다.
79. 2년이 넘게 지나도, 그때 들어간 돈이 아직 손실로 묶여 있다는 뜻입니다.
80. 그렇다면 본전에 묶이지 않으려면 어떻게 해야 할까요?

**살아남는 방법 파트** — 🎙 진행자

81. 핵심은 팔지 말지를 그날 기분이 아니라, 미리 정해 둔 날짜에 맡기는 것입니다.
82. 가격을 정해 두는 방법도 있지만, 그 가격 앞에선 본전 생각이 다시 끼어들기 쉽습니다.
83. 날짜와 사건으로 정하는 장치를, 다섯 단계마다 하나씩 보겠습니다.
84. 첫째, 잠깐에 날짜를 붙입니다.
85. 손실이 작을 때는 팔 이유가 없어 보여서, 오히려 팔기가 어렵습니다.
86. 그래서 살 때 잠깐의 길이를 날짜로 적어 둡니다.
87. 예를 들어 한 달입니다.
88. 한 달 뒤에도 본전 아래라면, 잠깐은 끝난 것으로 보고 정리를 시작합니다.
89. 사연자가 7월 1일에 샀다면, 점검일은 8월 1일입니다.
90. 그날 손실은 -635만 원이었습니다.
91. -200만 원보다는 컸지만, 끝까지 버틴 -1,600만 원의 절반도 안 됩니다.
92. 기한은 사람마다 달라도 되지만, 손실이 나기 전에 적어 두는 게 핵심입니다.
93. 둘째, 본전 대신 절반을 목표로 합니다.
94. 사실 본전 근처까지 왔을 때가 가장 팔기 어렵습니다.
95. 조금만 더 기다리면 본전일 것 같으니까요.
96. 그래서 손실이 줄어든 날에는 본전을 기다리지 않고, 절반부터 팝니다.
97. 사연자가 손실이 300만 원대로 줄었던 8월 27일에 절반을 팔았다고 해 보겠습니다.
98. 그 절반의 손실은 160만 원 정도입니다.
99. 남은 절반을 연말에 팔았더라도, 전체 손실은 960만 원 정도입니다.
100. 실제 -1,600만 원보다 640만 원 적죠.
101. 절반을 판 뒤에 오르면 남은 절반이 웃고, 내리면 판 절반이 웃습니다.
102. 어느 쪽이든, 후회가 절반으로 줄어듭니다.
103. 셋째, 실적 발표 다음 날만큼은 계좌를 엽니다.
104. 손실 난 계좌를 매일 보는 건 고통이고, 매일 볼 필요도 없습니다.
105. 대신 1년에 네 번, 회사가 분기 실적을 낸 다음 날에는 꼭 계좌를 엽니다.
106. 증권 앱에서 그 종목의 공시 알림을 켜 두면, 그날을 놓치지 않습니다.
107. 그날 실적이 예상보다 낮았다는 기사가 나오면, 가진 주식을 줄입니다.
108. 크래프톤은 반년 동안 이런 신호를 두 번 보냈습니다.
109. 2분기 실적 다음 날인 7월 30일에 정리했다면, 손실은 -490만 원이었습니다.
110. 3분기 실적 다음 날인 11월 5일에도 -1,370만 원으로, 연말보다는 적었죠.
111. 넷째, 판 뒤를 기록합니다.
112. 팔면 오를 것 같은 두려움은, 실제로 그런 일을 한두 번 겪어서 생깁니다.
113. 판 종목은 관심 목록에 남기고, 판 값 옆에 몇 달 뒤 가격을 이어 적습니다.
114. 사연자가 판 뒤를 적었다면 이렇습니다.
115. 열흘 뒤엔 판 값보다 낮았습니다.
116. 넉 달 뒤엔 한때 판 값보다 17% 높았습니다.
117. 그리고 아홉 달 뒤엔, 다시 판 값보다 20% 넘게 낮습니다.
118. 오른 날만 기억하면 팔면 꼭 오른다고 느끼지만, 기록을 보면 그 말은 반만 맞습니다.
119. 무엇보다 그 어느 날에도, 본전은 오지 않았습니다.
120. 다섯째, 다시 살 때는 팔 조건 카드부터 씁니다.
121. 크게 잃고 정리한 뒤에는, 다음 매수가 더 조급해지기 쉽습니다.
122. 그래서 매수 버튼을 누르기 전에, 팔 조건 세 줄을 먼저 적습니다.
123. 잠깐의 기한, 절반을 팔 기준, 그리고 확인할 실적 발표일입니다.
124. 사연자의 카드였다면, 7월 30일과 8월 1일이 미리 적혀 있었을 겁니다.
125. 그리고 이 카드를 가족이나 친구 한 사람에게 보여 줍니다.
126. 누군가 알고 있으면, 그날 미루기가 훨씬 어려워집니다.
127. 물론 버티는 것 자체가 나쁜 건 아닙니다.
128. 기한 안이고 실적이 예상대로 나오는 동안에는, 버티는 게 아니라 기다리는 거니까요.

**마무리 파트** — 🎙 진행자

129. 이렇게 해서 본전 심리가 작은 손실을 키우는 다섯 단계와 그 장치를 알아보았습니다.
130. 본전은 산 날 내가 정한 숫자일 뿐, 회사가 지켜 주는 약속이 아닙니다.
131. 다음에 살 때는, 사기 전에 팔 날짜부터 적어 보세요.
132. 성공 투자 하셨으면 좋겠습니다.
133. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
