# molppang-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py stock molppang-2026-10` (2026-10-11 08:41). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다. 한 종목 올인한 사람들의 최악의 결말**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 91 / 자막 116, 길이 7:56 (오디오에 맞춤) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–11 · 진행자 12–91 (`voices/*.json`) |
| 오디오 | ✅ narration.mp3 · 지금 대본과 같음 |
| 영상 코드 | ✅ `video/src/episodes/molppang-2026-10/` |
| 렌더 | ✅ final_1080p.mp4 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다. 한 종목 올인한 사람들의 최악의 결말 `행동 · 수익→손실 · 최악의 결말` 56자 — 짝 썸네일: thumbnail_1 (계좌 숫자 반전)
- [ ] **T2.** 좋은 종목이라 확신하고 전 재산 몰빵했다가 천만원 수익이 -2천만원이 됐습니다. 한 종목에 올인한 사람들의 공통점 `속마음 · 수익→손실 · 공통점` 63자 — 짝 썸네일: thumbnail_2 (인물·감정 장면)
- [ ] **T3.** (짧은 변형) CEO 이적 소식에 천만원 수익이던 몰빵 계좌가 -2천만원이 됐습니다. 올인한 사람들의 불편한 진실 `장면 · 수익→손실 · 불편한 진실` 55자 — 짝 썸네일: thumbnail_3 (검은 배경 제목형 — 채택 제목 문구)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (계좌 카드)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 천만 원 수익(빨강)이 -2천만 원 손실(파랑)로 뒤집힌 **계좌 숫자 반전**이 가장 클릭을 부른다 (성공 썸네일 중 인물 없는 3개가 모두 이 형태)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 라벨 (작게) | 내 계좌 | 잉크 #1E1E1E | — |
| 카드 시작 숫자 | +1,000만 원 | 빨강 #E63B2E (수익) | 강조 1 — 빨강 = 수익 |
| 펀치 (가장 큰 숫자) | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 (파랑 = 손실) |
| 하단 1줄 | 한 종목에만 몰빵했다가 | 흰색 + 두꺼운 검정 외곽선 | "몰빵했다가" 노랑 #FFD400 — 강조 2 |
| 하단 2줄 | 천만원 수익이 -2천만원 | 흰색 + 두꺼운 검정 외곽선 | — (손실 숫자는 빨강 금지 → 흰색) |

- 하단 2줄 = T1 앞 문장 "한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다"를 줄인 것: 12자 + 13자 = 25자 (띄어쓰기 포함, 한 줄 14자 이내 · 합 26자 이내)
- 강조색(노랑·빨강) 2곳 · 노랑 상자 없음 · 펀치(위쪽 큰 문구)는 "-2,000만 원" 1개(9자)
- 하단 2줄의 "-2천만원"은 제목 표기, 카드의 "-2,000만 원"은 영상 카드 표기 — 값은 같다 (`stock/guides/thumbnail_rules.md` 1번)

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a solid dark navy (#14213D) background. In the upper 60% of the frame, slightly left of
center, a light-cream (#F2EBDD) rounded rectangle card with a thin ink-black outline, about 70% of the frame width, like a
simple personal account summary card (NOT a real banking or brokerage app: no app name, no logos, no menus, no stock name
or ticker). Inside the card: a small ink-black label "내 계좌" at the top-left; below it the text "+1,000만 원" in
medium-size bold red (#E63B2E); below that a thick blue (#2D6CDF) arrow pointing down; and across the bottom of the card a
wide solid blue (#2D6CDF) rounded box with the huge white bold text "-2,000만 원", the largest text in the image (about one
fifth of the image height). No people, no faces, no chart axes or extra numbers, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "한 종목에만 몰빵했다가", line 2 "천만원 수익이 -2천만원". The word "몰빵했다가" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep all text at least 48px inside the edges, within the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (계좌를 확인한 밤)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 전 재산을 넣은 계좌를 확인한 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (성공 썸네일 24개 중 약 20개가 감정이 드러난 얼굴)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽, 가장 큰 숫자) | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 (파랑 = 손실) |
| 하단 1줄 | 좋은 종목이라 몰빵했다가 | 흰색 + 두꺼운 검정 외곽선 | "몰빵했다가" 노랑 #FFD400 — 유일한 강조색 |
| 하단 2줄 | 천만원 수익이 -2천만원 | 흰색 + 두꺼운 검정 외곽선 | — (손실 숫자는 빨강 금지 → 흰색) |

- 하단 2줄 = T2 앞 문장 "좋은 종목이라 확신하고 전 재산 몰빵했다가 천만원 수익이 -2천만원이 됐습니다"를 줄인 것: 13자 + 13자 = 26자 (띄어쓰기 포함, 한 줄 14자 이내 · 합 26자 이내)
- 강조색 1곳 · 노랑 상자 없음 · 펀치는 "-2,000만 원" 1개(9자)

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A dim, dark navy-toned kitchen at night, lights mostly off. On the right half of the frame, a
fictional Korean woman in her late 30s with an office-worker look (plain cardigan over a blouse), sitting at a kitchen
table and staring at a smartphone held in both hands, frozen, stunned and regretful expression, lips pressed together,
face lit by the phone's cold light. Her face, hands and the phone are in the upper 60% of the frame; her lower body fades
into the dark bottom band. The phone screen shows only one simple blue line dropping sharply, no app interface, no text.
Fictional person, not resembling any real or famous person, natural Korean features. No crying, no extreme fear.
In the upper-left area, a wide solid blue (#2D6CDF) rounded box with a thin white border containing the huge white bold
text "-2,000만 원", the largest text in the image (about one fifth of the image height).
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "좋은 종목이라 몰빵했다가", line 2 "천만원 수익이 -2천만원". The word "몰빵했다가" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 area, at least 48px from the edges.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 검은 배경 제목형 (채택 제목 문구)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 그림 없이 **검은 배경에 채택 제목 앞 문장만** 크게 넣은 글자 썸네일이 사진 썸네일 사이에서 눈에 띄어 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 한 종목에만 몰빵해서 | 흰색 #FFFFFF | — (11자) |
| 2줄 | 얻은 천만원 수익이 | "천만원" 빨강 #E63B2E, 나머지 흰색 | 수익 금액 = 빨강 (10자) |
| 3줄 | -2천만원이 됐습니다 | "-2천만원" 노랑 #FFD400, 나머지 흰색 | 손실 금액 = 노랑, 빨강 금지 (11자) |

- 채택 제목 앞 문장 "한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다."를 **글자 그대로** 3줄로 나눴다 (끝 마침표만 뺌). 뒤 문장(결말 장치 "한 종목 올인한 사람들의 최악의 결말")은 넣지 않는다.
- 줄 길이(띄어쓰기 포함): 11자 · 10자 · 11자 — 모두 14자 이내, 어절 단위로 끊음
- 숫자 반전("천만원 수익이 -2천만원이")은 15자라 한 줄에 들어가지 않아 2줄 끝 "천만원 수익이" → 3줄 첫머리 "-2천만원이"로 바로 이어지게 나눴다
- 강조 2곳: 빨강 "천만원"(수익), 노랑 "-2천만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (`stock/guides/thumbnail_rules.md` 1번·2번).
- "몰빵해서"는 흰색으로 둔다. 바로 아래 줄의 빨강(수익)과 붙어 빨강의 뜻(이 채널에서는 수익)이 섞이지 않게 하기 위해서다 — 같은 상황(수익 금액이 있는 제목)인 빚투 thumbnail_3과 같은 선택.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 3 lines with tight line spacing:
line 1 "한 종목에만 몰빵해서", line 2 "얻은 천만원 수익이", line 3 "-2천만원이 됐습니다".
All text pure white (#FFFFFF) except "-2천만원" at the start of line 3 in bright yellow (#FFD400) and "천만원" in line 2 in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
전 재산 7천만 원을 AI 관련주 한 종목에 몰빵해 천만 원 수익을 봤는데, 어느 날 CEO 이적 소식에 계좌가 -2천만 원이 됐습니다.
한 종목 몰빵이 왜 위험한지 4가지로, 위험을 나눠 담는 분산 투자 방법을 5가지로 정리했습니다.

■ 이 영상에서 다루는 것
- 몰빵 종목이 하락하면 대처할 방법이 없는 이유 (메타 2022년·구글 2023년·엔비디아 2025년 하루 급락)
- 그렇다고 버티는 것도 답이 아닌 이유 (7천만 원이 5천만 원이 되면 40%가 올라야 본전)
- 한 종목으로 큰 수익을 낼 확률 자체가 낮은 이유 (자본시장연구원: 2023년 말까지 10년간 국내 상장사 52%가 1년짜리 안전한 채권보다 못 벎, 2026년 코스피가 두 배 넘게 오를 때 지수를 이긴 종목 4% 미만)
- 몰빵이 판단력까지 무너뜨리는 이유 (잃을 때의 고통은 얻을 때의 기쁨보다 두 배 정도 큼)
- 나눠 담는 방법 5가지: 한 종목 비중의 상한, 업종 나누기, 지수 ETF 기본, 현금 남기기, 수익 난 종목의 비중 확인

■ 챕터
0:00 사연: 전 재산 몰빵, 천만 원 수익이 -2천만 원
1:05 왜 한 종목에 몰빵할까
1:41 문제 01 몰빵 종목이 하락하면 대처할 방법이 없다
3:04 문제 02 버티는 것도 답이 아니다
3:27 문제 03 큰 수익을 낼 확률 자체가 낮다
4:24 문제 04 몰빵은 판단력까지 무너뜨린다
5:02 방법 첫째: 한 종목 비중의 상한 정하기
5:35 방법 둘째: 종목만 말고 업종도 나누기
6:10 방법 셋째: 어렵다면 지수 ETF를 기본으로
6:39 방법 넷째: 한 번에 다 사지 말고 현금 남기기
7:02 방법 다섯째: 수익 나면 비중부터 확인
7:32 정리

■ 사연에 대해
이 영상의 사연은 실제 주가 흐름(몽고디비, 2026년 9월 28일 CEO 이적 발표 전후)을 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시입니다.

■ 출처
- 몽고디비 일별 주가: https://stockanalysis.com/stocks/mdb/history/
- 2026년 9월 28일 몽고디비 CEO 메타 이적 발표·주가 급락: https://www.tikr.com/blog/meta-poaches-mongodb-ceo-effective-immediately-stock-sinks-24
- 같은 날 종가 하락과 시장 반응: https://www.tikr.com/blog/mongodb-stock-fell-18-when-its-ceo-left-for-meta-heres-what-the-street-is-saying-now
- 메타 2022년 2월 3일 하루 -26%: https://www.itv.com/news/2022-02-04/facebook-owner-meta-suffers-26-plunge-in-share-price
- 메타 폭락 직전 매도 의견 애널리스트 2명 (블룸버그 2022-02-11): https://www.bloomberg.com/news/articles/2022-02-11/wall-street-s-lack-of-big-tech-skepticism-is-why-it-got-meta-earnings-so-wrong
- 구글 2023년 2월 8일 AI 챗봇 광고 오답: https://www.npr.org/2023/02/09/1155650909/google-chatbot--error-bard-shares
- 2025년 1월 27일 딥시크 충격 (엔비디아·브로드컴·비스트라, 로이터): https://theprint.in/tech/deepseek-sparks-global-ai-selloff-nvidia-losses-about-593-billion-of-value/2466124/
- 자본시장연구원 이슈보고서 24-31 (2024), 국내 상장기업 저평가에 관한 고찰: https://www.kcmi.re.kr/kcmifile/report_data/1811/reportpdf_1811_1.pdf
- 2026년 코스피 상승기 지수를 이긴 종목 (한국경제 2026-07-28): https://www.hankyung.com/article/2026072780786
- 엔씨소프트 2021년 최고가: https://www.ajunews.com/view/20210828222017690
- LG생활건강 2021년 최고가: https://v.daum.net/v/20250520060100341
- 코스피 2021년 7월 6일 최고치: https://www.sedaily.com/article/14115908
- 코스피 2026년 10월 8일 종가: https://etoday.co.kr/news/view/2633993
- Brown, Imai, Vieider & Camerer (2024), 손실 회피 메타분석: https://www.aeaweb.org/doi/10.1257/jel.20221698
- 버크셔 해서웨이 2013년 주주 서한 (워런 버핏, S&P 500 지수 펀드 90%): https://www.berkshirehathaway.com/letters/2013ltr.pdf

■ 투자 유의 사항
이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
투자 판단과 책임은 투자자 본인에게 있습니다.

#주식 #몰빵 #분산투자
```

**태그**: 몰빵, 한 종목 몰빵, 올인, 분산 투자, 분산투자, 주식 손실, 주식, 주식 투자, 주식 초보, 주식 공부, 미국 주식, 서학개미, 지수 ETF, S&P 500, 몽고디비

**고정 댓글**

```
한 종목에 더 넣기 전에 이 두 가지부터 확인해 보세요.
1. 내 계좌에서 가장 비중이 큰 종목이 몇 %인지
2. 그 종목에 악재가 터졌을 때 꺼내 쓸 현금이 남아 있는지

여러분은 한 종목에 크게 넣어 본 적이 있나요? 그때 정해 둔 비중 기준이 있었는지 댓글로 나눠 주세요.
※ 이 영상은 투자 권유가 아닙니다. 특정 종목 추천·리딩방 홍보 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 최근에 AI와 관련된 주식 종목을 찾아보다가 몽고디비라는 종목을 알게 되었어요.
2. 투자 전망도 좋고 실적도 잘 나오고 주가 상승세도 좋았어요.
3. 그래서 좋은 종목이라고 확신하고 전 재산 7천만 원을 이 종목에 몰빵했었죠.
4. 매수하고 나서 천만 원 정도 수익이 나서 정말 기분이 좋았어요.
5. 전고점을 생각하면 더 상승할 것 같았죠.
6. 하지만 그건 달콤한 꿈일 뿐이었습니다.
7. 어느 날 계좌를 확인해 보니 갑자기 -2천만 원이 찍힌 겁니다.
8. 도대체 무슨 일인가 찾아보니 CEO가 다른 회사로 이적했다는 소식이었어요.
9. 안 그래도 고점에서 내려오던 주가가 그 소식에 최대 -26%까지 폭락했다는 거예요.
10. 물타기 할 돈도 없는데 하필이면 제가 매수한 다음에 이런 일이 일어나다니요.
11. 이 세상은 저한테 너무 가혹한 것 같아요.

**진행자 파트** — 🎙 진행자

12. 앞의 사연과 같이
13. 이 종목은 전망이 좋으니까 몰빵하면 많이 오르겠지?
14. 여러 종목에 나눠 사면 수익이 줄어드니까 한 종목에 다 넣어야지.
15. 혹시 떨어져도 좋은 종목이니까 금방 다시 오르겠지.
16. 이런 식으로 자신이 좋다고 생각하는 종목에 전 재산을 몰빵하는 분들 꽤 있으실 겁니다.
17. 과연 이렇게 몰빵 투자를 하는 사람들이 생각대로 큰 수익을 얻을 수 있을까요?
18. 한번 문제가 뭔지 알아보겠습니다.

> 🟨 [장면] 투자 권유가 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
> 사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
> 과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
> 투자 판단과 책임은 투자자 본인에게 있습니다.

**문제 분석 파트** — 🎙 진행자

19. 첫 번째이자 가장 큰 문제는 몰빵한 종목이 하락하면 대처할 방법이 없다는 것입니다.
20. 사람 일이 어떻게 될지 모르듯이 앞으로 어떻게 움직일지 모르는 게 주식입니다.
21. 장기적으로는 상승할 수 있어도 사연과 같이 단기적으로 갑자기 큰 악재가 발생할 수 있습니다.
22. 최근 상승세를 보고 매수하거나 기존에 수익을 보고 있던 투자자들도 큰 손해를 볼 수 있는 것이죠.
23. 이런 사례는 메타, 구글, 엔비디아 같은 빅테크에서도 일어났어요.
24. 2022년 메타는 실적 실망으로 하루에 26% 빠졌습니다.
25. 2023년 구글은 AI 챗봇 광고 속 오답 하나로 장중 9% 빠졌고요.
26. 2025년 엔비디아는 중국 AI 기업 딥시크의 등장으로 하루에 17% 빠졌습니다.
27. 당시 미국 증시 역사상 하루 기준 가장 큰 시가총액 손실이었죠.
28. 이런 폭락은 전문가들조차 미리 알기 어렵습니다.
29. 실제로 메타가 폭락하기 직전, 팔라는 의견을 낸 애널리스트는 단 2명뿐이었습니다.
30. 문제는 몰빵한 상태에서 이런 일이 터지면 선택지가 없다는 겁니다.
31. 현금이 없으니 물타기도 못 하고, 손절하면 손실이 그대로 확정되죠.
32. 게다가 미리 정해 둔 손절 라인도 소용없을 수 있습니다.
33. 장 시작 전에 악재가 터지면 주가가 그보다 훨씬 아래에서 시작하니까요.
34. 두 번째는 그렇다고 버티는 것도 답이 아니라는 것입니다.
35. 한 번 크게 잃으면 되찾기가 훨씬 어렵기 때문이죠.
36. 사연처럼 7천만 원이 5천만 원이 되면 원금을 되찾는 데 40%가 올라야 합니다.
37. 반토막이 나면 두 배가 올라야 본전이고, 70% 빠지면 세 배 넘게 올라야 합니다.
38. 몰빵은 이 위험을 계좌 전체로 떠안는 일입니다.
39. 세 번째는 한 종목으로 큰 수익을 낼 확률 자체가 낮다는 것입니다.
40. 자본시장연구원이 2023년 말까지 10년간 국내 상장사의 주식 수익률을 분석했는데요.
41. 절반이 넘는 52%가 1년짜리 안전한 채권에 넣어 둔 것보다 못 벌었습니다.
42. 시가총액 상위 30% 대형주만 보면 이 비율이 58%로 오히려 더 높았죠.
43. 2026년 코스피가 두 배 넘게 오른 6월까지, 지수를 이긴 종목은 4%도 안 됐죠.
44. 한 종목에 몰빵한다는 건 이 4%를 정확히 골라야 한다는 뜻입니다.
45. 2021년 고점을 찍은 엔씨소프트와 LG생활건강은 지금 70% 넘게 빠져 있습니다.
46. 5년이 넘도록 그 고점을 한 번도 되찾지 못했죠.
47. 그사이 코스피는 2021년 고점의 두 배 수준까지 올랐는데 말이죠.
48. 그런데도 몰빵 성공담만 들리는 건, 크게 잃은 사람들은 조용히 떠나기 때문이죠.
49. 네 번째는 몰빵이 판단력까지 무너뜨린다는 것입니다.
50. 사람은 원래 잃는 것에 훨씬 예민합니다.
51. 연구에 따르면 잃을 때의 고통은 같은 금액을 얻을 때의 기쁨보다 두 배 정도 큽니다.
52. 전 재산이 걸려 있으면 그 고통이 매일 찾아오죠.
53. 하루에도 수십 번 앱을 열고, 밤에는 미국 장을 지켜보느라 잠을 설치게 됩니다.
54. 그러다 보면 팔아야 할 때 못 팔고, 기다려야 할 때 못 기다리게 됩니다.
55. 그렇다면 어떻게 투자해야 할까요?

**올바른 방법 설명 파트** — 🎙 진행자

56. 핵심은 큰 수익을 한 번에 얻겠다는 욕심을 버리고 나눠 담는 것입니다.
57. 구체적으로 다섯 가지만 기억하세요.
58. 첫째, 한 종목이 내 계좌에서 차지하는 비중의 상한을 정하세요.
59. 예를 들어 상한이 15%면 7천만 원 계좌에서 한 종목에 1,050만 원까지만 넣는 거죠.
60. 사연의 7천만 원을 10개 종목에 700만 원씩 나눴다면 어땠을까요?
61. 같은 폭락에도 손실은 약 200만 원, 계좌 전체의 3% 정도였을 겁니다.
62. 물론 시장 전체가 빠지는 날엔 다른 종목들도 함께 빠집니다.
63. 하지만 한 회사의 악재 하나로 계좌 전체가 무너지는 일은 막을 수 있습니다.
64. 둘째, 종목만 나누지 말고 업종도 나누세요.
65. AI 반도체, AI 소프트웨어, AI 전력주를 나눠 샀다면 사실상 한 종목입니다.
66. 딥시크가 등장한 날 AI 반도체인 엔비디아와 브로드컴은 17% 빠졌습니다.
67. AI 데이터센터 전력 수요 기대로 오르던 전력주 비스트라는 28%나 빠졌죠.
68. 진짜 분산은 반도체, 헬스케어, 소비재, 금융처럼 서로 다른 업종에 나누는 겁니다.
69. 업종이 다르면 같은 악재에 함께 무너질 가능성이 줄어드니까요.
70. 셋째, 종목 고르기가 어렵다면 지수 ETF를 기본으로 깔아 두세요.
71. S&P 500 ETF 하나만 사면 미국 대표 기업 500곳에 한 번에 나눠 투자하는 셈이죠.
72. 시장을 이끄는 대형 승자 기업들을 직접 고르지 않아도 함께 담게 됩니다.
73. 워런 버핏도 아내에게 남길 돈의 90%를 S&P 500 지수 펀드에 넣으라고 했습니다.
74. 예를 들어 절반은 지수 ETF로 깔고, 나머지만 개별 종목에 나누는 식입니다.
75. 넷째, 한 번에 다 사지 말고 현금을 남겨 두세요.
76. 한 종목에 넣을 700만 원을 한 번에 사지 않고 세 번에 나눠 산다고 해볼까요?
77. 첫 매수 직후 악재가 터져도, 남은 돈으로 더 싸게 살지 기다릴지 고를 수 있습니다.
78. 사연자가 가장 괴로웠던 것도 물타기 할 돈조차 없었다는 거였죠.
79. 현금은 노는 돈이 아니라 위기 때 꺼내 쓸 수 있는 선택지입니다.
80. 다섯째, 수익이 났을 때 더 얹지 말고 비중부터 확인하세요.
81. 수익이 나면 사연자처럼 더 오를 것 같아서 그대로 두거나 더 사고 싶어지죠.
82. 700만 원 넣은 종목이 두 배가 되면 그 비중은 10%에서 18% 정도로 커집니다.
83. 그대로 두면 나도 모르게 몰빵에 가까워지는 거죠.
84. 정해 둔 상한 15%를 넘은 만큼만 팔아서 다른 종목에 나눠 두면 됩니다.
85. 이렇게 나눠 두면 한 종목에 악재가 터져도 대처할 여유가 생깁니다.
86. 이렇게 해서 한 종목 몰빵 투자의 위험과 분산 투자의 중요성을 알아보았습니다.
87. 이미 손실을 보셨더라도 늦지 않았습니다.
88. 지금 내 계좌에서 가장 비중이 큰 종목이 몇 %인지부터 확인해 보세요.
89. 큰 수익보다는 대처가 가능하도록 투자하는 게 중요하다는 것을 잊지 마세요.
90. 여러분 모두 성공 투자 하셨으면 좋겠습니다.
91. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
