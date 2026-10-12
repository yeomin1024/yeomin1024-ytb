# pandon-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py stock pandon-2026-10` (2026-10-12 12:44). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **소질 있는 줄 알고 판돈 키웠다가 번 285만원이 -1,288만원이 됐습니다. 금액부터 늘린 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 125 / 자막 144, 길이 11:31 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–5 · 진행자 6–125 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/pandon-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 소질 있는 줄 알고 판돈 키웠다가 번 285만원이 -1,288만원이 됐습니다. 금액부터 늘린 사람들의 공통점 `속마음 · 이득→손실 · 공통점` 60자 — 짝 썸네일: thumbnail_1 (계좌 숫자 반전)
- [ ] **T2.** 500만원으로 번 285만원 믿고 판돈 12배 키웠다가 1,288만원 잃었습니다. 금액 늘린 개미가 결국 망하는 과정 `행동 · 이득→손실 · ~하는 과정(시험)` 65자 — 짝 썸네일: thumbnail_2 (인물·감정 장면)
- [ ] **T3.** (짧은 변형) +285만원 계좌가 판돈 키우자 1,288만원 손실이 됐습니다. 증액한 개미의 최악의 결말 `장면 · +대비 · 최악의 결말` 50자 — 짝 썸네일: thumbnail_3 (검은 배경 제목형 — 채택 제목 문구)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (계좌 카드)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 작은 수익 **+285만 원이 판돈을 12배로 키운 뒤 -1,288만 원**으로 뒤집힌 **계좌 숫자 반전**이 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 카드 라벨 | 내 계좌 | 잉크 #1E1E1E (작게) | — |
| 카드 시작 숫자 | +285만 원 | 빨강 #E63B2E | 수익 금액 = 빨강 |
| 펀치 (위쪽) | 판돈 12배 | 검정 #1E1E1E | 노랑 형광펜 #FFD400 (노랑 상자는 이 1곳만) |
| 카드 결과 숫자 | -1,288만 원 | 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 소질 믿고 판돈 키웠다가 | 흰색 + 검정 외곽선 | — (13자) |
| 하단 2줄 | -1,288만원 됐습니다 | 흰색 + 검정 외곽선 | "-1,288만원"만 노랑 #FFD400 (13자, 2줄 합 26자) |

- 강조색 3곳: 빨강 "+285만 원"(카드, 수익), 노랑 형광펜 "판돈 12배", 노랑 글자 "-1,288만원". 손실 숫자는 빨강으로 쓰지 않는다 (카드는 파랑 상자, 하단은 노랑).
- 하단 2줄은 T1 앞 문장("소질 있는 줄 알고 판돈 키웠다가 번 285만원이 -1,288만원이 됐습니다")을 줄인 것. 2줄 합 26자 안에 넣으려고 "소질 있는 줄 알고"를 "소질 믿고"로, "번 285만원이"는 카드의 "+285만 원"이 대신 보여 주게 뺐다.
- "판돈 12배" = 500만 원 → 6,000만 원 (문장 3·74). 하단 2줄은 제목 표기("-1,288만원"), 카드는 영상 계좌 카드 표기("+285만 원", "-1,288만 원")다. 값은 같다 (`stock/guides/thumbnail_rules.md` 1번).

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the upper 60% of the frame,
a wide light-cream rounded rectangle card with a thin black outline, like a simple personal account summary card
(NOT a real banking or brokerage app, no app name, no logos, no stock names), with the small label "내 계좌" in its top-left corner.
Inside the card, on the left: the text "+285만 원" in large red (#E63B2E) bold letters. In the middle: a thick blue (#2D6CDF)
arrow that rises a little and then plunges steeply down to the right, with the label "판돈 12배" in black bold letters over a
bright yellow (#FFD400) highlighter stripe just above the arrow. On the right: a solid blue (#2D6CDF) rounded box with the huge
white bold text "-1,288만 원", the largest element in the image. No people, no faces. Minimal, nothing decorative.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "소질 믿고 판돈 키웠다가", line 2 "-1,288만원 됐습니다". The word "-1,288만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep all text and the card inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 판돈을 키운 뒤 하루 -22%를 확인한 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (작은 채널 성공 썸네일 15개 중 14개에 사람·캐릭터 — `stock/guides/thumbnail_rules.md` 2번)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽) | 하루 -22% | 흰색 #F7F3EA ("-22%"만 검정) | "-22%"에 노랑 상자 (글자 전체 높이, 노랑 상자는 이 1곳만) |
| 하단 1줄 | 번 돈 믿고 키운 판돈 | 흰색 + 검정 외곽선 | — (12자) |
| 하단 2줄 | 1,288만원 잃었습니다 | 흰색 + 검정 외곽선 | "1,288만원"만 노랑 #FFD400 (13자, 2줄 합 25자) |

- 강조색 2곳: 노랑 상자 "-22%", 노랑 "1,288만원"(손실). 빨강은 쓰지 않는다 (이 채널에서 빨강 = 수익).
- 하단 2줄은 T2 앞 문장("500만원으로 번 285만원 믿고 판돈 12배 키웠다가 1,288만원 잃었습니다")을 줄인 것. "번 285만원 믿고 판돈 키웠다가"를 "번 돈 믿고 키운 판돈"으로 줄였다.
- 펀치 "하루 -22%"는 문장 4(0:18.0)와 문장 79 "1월 21일, 주가는 22.35% 떨어진 37만 3,500원"의 말이다. 대본·제목의 손실 금액 표기 "1,288만원"과 값이 같다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A navy-toned office desk scene in the daytime, soft window light. On the left 40% of the frame,
a fictional Korean woman office worker in her late 30s (plain blouse), sitting and holding a smartphone, the other hand
pressed against her forehead, frozen stunned and regretful expression, face lit by the phone. The face and the phone are
in the upper 60% of the frame; the lower body fades into darkness at the bottom. The phone screen shows only a simple line
that rises and then turns blue and drops sharply, no app interface, no text. Fictional person, not resembling any real or
famous person, natural Korean features, realistic photo style. In the upper right area, the huge bold text "하루 -22%" in
off-white, where only "-22%" sits on a solid bright yellow (#FFD400) box with black text; it is the largest text in the
upper area. No crying, no extreme fear.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "번 돈 믿고 키운 판돈", line 2 "1,288만원 잃었습니다". The word "1,288만원" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 검은 배경 제목형 (채택 제목 문구)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 그림 없이 **검은 배경에 채택 제목 앞 문장만** 크게 넣은 글자 썸네일이 사진 썸네일 사이에서 눈에 띄어 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 소질 있는 줄 알고 | 흰색 #FFFFFF | — (10자) |
| 2줄 | 판돈 키웠다가 | 흰색 #FFFFFF | — (7자) |
| 3줄 | 번 285만원이 | "285만원" 빨강 #E63B2E, 나머지 흰색 | 수익 금액 = 빨강 (8자) |
| 4줄 | -1,288만원이 됐습니다 | "-1,288만원" 노랑 #FFD400, 나머지 흰색 | 손실 금액 = 노랑, 빨강 금지 (14자) |

- 채택 제목 앞 문장 "소질 있는 줄 알고 판돈 키웠다가 번 285만원이 -1,288만원이 됐습니다."를 **글자 그대로** 4줄로 나눴다 (끝 마침표만 뺌). 뒤 문장(결말 장치 "금액부터 늘린 사람들의 공통점")은 넣지 않는다.
- 줄 길이(띄어쓰기 포함): 10자 · 7자 · 8자 · 14자 — 모두 14자 이내, 어절 단위로 끊음. 속마음(1줄) → 행동(2줄) → 번 돈(3줄) → 결과(4줄)로 한 줄에 한 덩어리씩.
- 강조 2곳: 빨강 "285만원"(수익), 노랑 "-1,288만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (`stock/guides/thumbnail_rules.md` 1번·2번).
- 행동 단어 "판돈 키웠다가"는 흰색으로 둔다. 바로 옆 줄의 빨강(수익)과 붙어 빨강의 뜻(이 채널에서는 수익)이 섞이지 않게 하기 위해서다 — 추격 매수·몰빵 thumbnail_3과 같은 선택.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "소질 있는 줄 알고", line 2 "판돈 키웠다가", line 3 "번 285만원이", line 4 "-1,288만원이 됐습니다".
All text pure white (#FFFFFF) except "285만원" in line 3 in red (#E63B2E) and "-1,288만원" at the start of line 4 in bright yellow (#FFD400). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
500만 원으로 반년 만에 285만 원을 번 뒤 판돈을 6,000만 원까지 키웠다가, 기대보다 작은 계약 하나에 하루 22%가 빠져 -1,288만 원이 됐습니다.
처음 번 돈이 판돈을 키우고 한 번에 돌려주게 만드는 5단계와, 단계마다 짝이 되는 장치 5가지를 정리했습니다.

■ 이 영상에서 다루는 것
- 1단계 처음 번 돈: 코스피가 한 해 75.6% 오른 2025년, 500만 원이 반년 만에 285만 원을 벌어 준 이유
- 2단계 운을 실력으로 착각: 2025년 코스피 종목 948개 중 지수보다 더 오른 종목은 122개 (열 개 중 하나 남짓)
- 3단계 판돈 키우기: 하루 만에 일곱 배로 커진 금액, 그대로인 기준 (인도 공모주 추첨 연구: 운으로 번 사람이 거래를 늘렸다)
- 4단계 큰 금액에 온 작은 하락: 주가 7.5% 하락에 반년 수익 285만 원이 모두 사라진 계산
- 5단계 되찾으려 한 번 더 키우기: 판돈 6,000만 원에서 하루에만 1,356만 원이 줄어든 날
- 살아남는 장치 5가지: 번 돈은 원금과 따로 담기, 운인지 실력인지 기록으로 가리기, 금액을 늘리는 규칙은 미리, 넣기 전에 하한가를 원으로 계산하기, 번 돈을 다 돌려준 날은 금액을 줄이는 날

■ 챕터
0:00 사연: 500만 원으로 번 285만 원이 -1,288만 원
0:26 왜 처음 번 돈이 판돈을 키울까
1:36 1단계 처음 번 돈
2:12 2단계 운을 실력으로 착각
3:08 3단계 판돈 키우기
4:19 4단계 큰 금액에 온 작은 하락
5:37 5단계 되찾으려 한 번 더 키우기
7:41 장치 1 번 돈은 원금과 따로 담기
8:29 장치 2 운인지 실력인지 기록으로 가리기
9:13 장치 3 금액을 늘리는 규칙은 미리
10:01 장치 4 넣기 전에 하한가를 원으로
10:42 장치 5 다 돌려준 날은 줄이는 날
11:13 정리

■ 사연에 대해
이 영상의 사연은 실제 주가 흐름(알테오젠, 2024년 12월~2026년 1월)을 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시입니다.
이 영상의 내레이션은 AI 음성으로 만들었습니다.

■ 출처
- 알테오젠 2024년 말 종가와 2025년 7월 상승률 (뉴시스 2025-07-17): https://www.newsis.com/view/NISX20250717_0003255373
- 알테오젠 2025년 12월 30일 종가 (시대일보 2026-02-03): https://www.sidae.com/article/2026020310462275357
- 독일 키트루다 피하 주사 판매 금지 가처분과 주가 (헤럴드경제): https://www.heraldk.com/article/2025120417400851416
- 하나증권 "독일은 키트루다 매출의 2%대" (스마트투데이 2025-12-08): https://www.smarttoday.co.kr/ko-kr/articles/98370
- 2025년 12월 외국인 순매도·개인 순매수 (헤럴드경제): https://www.heraldk.com/article/2025121418214755657
- JP모건 헬스케어 콘퍼런스와 1월 16일 주가 (한국경제 2026-01-16): https://www.hankyung.com/article/2026011658261
- GSK 자회사와 최대 4,200억 원 계약 (한국경제 2026-01-20): https://www.hankyung.com/article/202601201627i
- 아스트라제네카 계약 (한국경제 2025-03-18): https://www.hankyung.com/article/2025031809096
- 키트루다 피하 주사 로열티 2% (스마트투데이): https://www.smarttoday.co.kr/ko-kr/articles/101808
- 1월 21일 22.35% 하락, 2020년 6월 이후 최대 (더팩트): https://news.tf.co.kr/read/economy/2284843.htm
- 2025년 코스피 75.6%, 948개 중 122개 (헤럴드경제 2025-12-30): https://www.heraldk.com/article/2025123017551462713
- 2025년 코스닥 36.5% (헤럴드경제 2025-12-30): https://www.heraldk.com/article/2025123001114462421
- 2026년 6월 22일 코스피 9,114.55 (트윅24): https://www.twig24.com/news/2026/06/22/20260622500191
- 가격제한폭 30% (이투데이): https://www.etoday.co.kr/news/view/1127429
- Anagol, Balasubramaniam & Ramadorai (2021), 인도 공모주 추첨 연구: https://ideas.repec.org/a/eee/jfinec/v140y2021i3p965-986.html

■ 투자 유의 사항
이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
투자 판단과 책임은 투자자 본인에게 있습니다.

#주식 #판돈키우기 #투자원칙
```

**태그**: 판돈, 판돈 키우기, 초심자의 행운, 주식 수익 반납, 주식 손실, 투자 원칙, 투자 금액, 주식, 주식 투자, 주식 초보, 주식 공부, 코스닥, 바이오주, 알테오젠, 개인 투자자

**고정 댓글**

```
처음 수익이 난 날, 이 두 가지부터 해 보세요.
1. 번 돈만큼은 팔아서 주식 계좌 밖으로 옮기기
2. 금액을 늘리는 규칙(한 번에 얼마까지, 언제, 어디까지)을 숫자로 적어 두기

조금 벌고 나서 넣는 돈을 늘려 본 적 있나요? 그때 금액을 늘린 나만의 기준이 있었다면 하나만 알려 주세요.
※ 이 영상은 투자 권유가 아닙니다. 특정 종목 추천·리딩방 홍보 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 500만 원으로 번 285만 원이, 판돈 키운 뒤 -1,288만 원이 됐어요.
2. 알테오젠이 반년 만에 57% 오르자, 제가 소질이 있는 줄 알았죠.
3. 넣는 돈을 두 번에 걸쳐 6,000만 원까지 키웠어요.
4. 그런데 기대보다 작은 계약 하나에, 하루 22%가 빠졌어요.
5. 운을 실력이라 믿은 대가였어요.

**진행자 파트** — 🎙 진행자

6. 처음 넣은 돈이 몇 달 만에 불어나면, 머릿속에서 이런 계산이 시작됩니다.
7. 조금 넣고도 이만큼 벌었는데, 크게 넣었으면 훨씬 벌었겠다.
8. 아무래도 나는 주식에 소질이 있는 것 같아.
9. 잃은 만큼만 되찾으면, 그때 금액을 줄이면 되지.
10. 이런 식으로 처음 번 돈이 다음 판돈의 크기를 정하게 됩니다.
11. 그리고 이런 분들은 거의 같은 순서를 밟습니다.
12. 조금 넣어서 벌고, 그걸 실력이라 믿고, 판돈을 키웁니다.
13. 그다음 작은 하락에 흔들리고, 잃은 걸 되찾으려 더 넣다가 한 번에 돌려주죠.
14. 사연 속 알테오젠은 정맥 주사약을 피하 주사로 바꾸는 기술을 가진 바이오 회사입니다.
15. 2025년 코스닥 시가총액 1위였죠.
16. 올해처럼 코스피가 반년도 안 돼 두 배가 되는 불장에선, 이 순서가 더 빨리 돌아갑니다.
17. 사연자가 밟은 다섯 단계를 하나씩 따라가 보겠습니다.

> 🟨 [장면] 투자 권유가 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 투자 교육과 정보 제공을 위한 것이며, 특정 종목의 매수나 매도를 권유하지 않습니다.
> 사연 속 금액과 계산은 이해를 돕기 위한 예시입니다.
> 과거 주가와 통계는 미래 수익을 보장하지 않으며, 원금 손실이 생길 수 있습니다.
> 투자 판단과 책임은 투자자 본인에게 있습니다.

**망하는 과정 파트** — 🎙 진행자

18. 첫 번째 단계는 처음 번 돈입니다.
19. 생각보다 쉬운데?
20. 사연자는 2024년 마지막 거래일에 알테오젠을 500만 원어치 샀습니다.
21. 2025년 7월 16일, 주가는 48만 6천 원으로 산 값보다 57% 높았죠.
22. 반년 만에 285만 원을 번 겁니다.
23. 그해는 코스피가 한 해 동안 75.6% 오른 해였습니다.
24. 문제는 이렇게 쉽게 번 첫 수익이, 그다음 판단의 기준이 된다는 겁니다.
25. 첫 수익은 대개 착각을 데리고 옵니다.
26. 두 번째 단계는 운을 실력으로 착각하는 겁니다.
27. 남들은 헤매는데 나는 벌잖아, 보는 눈이 있나 봐.
28. 그 무렵 알테오젠은 사상 최고가를 잇달아 새로 쓰고 있었습니다.
29. 내가 고른 종목이 최고가를 찍으니, 실력이라고 믿기 딱 좋은 순간이었죠.
30. 하지만 2025년 코스피에 상장된 종목은 948개였습니다.
31. 그중 지수보다 더 오른 종목은 122개, 열 개 중 하나 남짓이었죠.
32. 사연자의 알테오젠도 2025년 한 해 45% 올랐습니다.
33. 코스닥 지수 36.5%보다는 높았지만, 코스피 75.6%보다는 낮았죠.
34. 한 해, 한 종목의 결과로는 그게 운인지 실력인지 가를 수 없다는 뜻입니다.
35. 착각은 생각에서 끝나지 않고, 곧 금액으로 옮겨 갑니다.
36. 세 번째 단계는 판돈 키우기입니다.
37. 500만 원으로 285만 원이면, 3,000만 원이면 1,700만 원이잖아.
38. 사연자는 바로 그날, 3,000만 원을 더 넣었습니다.
39. 넣은 돈이 하루 만에 500만 원에서 3,500만 원, 일곱 배가 됐죠.
40. 바뀌지 않은 것도 있었습니다.
41. 언제 팔지, 얼마까지 잃어도 되는지는 500만 원일 때처럼 정해 둔 게 없었습니다.
42. 운으로 번 돈이 판을 키운다는 건 연구로도 확인됩니다.
43. 인도에서는 공모주 청약이 몰리면, 추첨으로 주식을 나눠 줍니다.
44. 2021년 발표된 한 연구가, 이 추첨에 참여한 투자자 150만 명을 살폈습니다.
45. 순전히 운으로 당첨된 공모주가 오르자, 당첨자들은 다른 주식 거래까지 늘렸습니다.
46. 운으로 얻은 수익을, 자기 실력의 증거로 받아들인 겁니다.
47. 물론 금액을 키워서 더 번 사람도 있습니다.
48. 차이는 키우기 전에 규칙이 있었느냐입니다.
49. 규칙 없이 커진 금액은, 같은 하락도 전혀 다른 크기로 만듭니다.
50. 네 번째 단계는 큰 금액에 찾아온 작은 하락입니다.
51. 이 정도 조정은 금방 회복하겠지.
52. 2025년 12월 초, 독일 법원이 한 항암제의 독일 판매를 임시로 막았습니다.
53. 알테오젠 기술로 만든, 미국 제약사 머크의 키트루다 피하 주사였죠.
54. 특허를 문제 삼은 미국 바이오 회사 할로자임의 가처분이었습니다.
55. 하나증권은 독일 판매가 이 약 전체 매출의 2%대라고 봤습니다.
56. 그런데도 알테오젠 주가는 하루에 12% 넘게 빠졌습니다.
57. 12월 30일, 2025년 마지막 종가는 44만 9,500원이었습니다.
58. 사연자가 3,000만 원을 더 넣은 날보다 7.5% 낮은 값이었죠.
59. 주가는 7.5% 내렸을 뿐인데, 반년 동안 번 285만 원이 모두 사라졌습니다.
60. 넣은 돈도 3,500만 원, 계좌 평가액도 3,500만 원, 딱 본전이었죠.
61. 500만 원만 들고 있었다면, 같은 기간 줄어든 돈은 60만 원이 안 됐습니다.
62. 같은 퍼센트라도 금액이 커지면, 작은 하락 하나가 몇 달 치 수익을 지웁니다.
63. 그리고 마지막 단계가 옵니다.
64. 다섯 번째 단계는 잃은 수익을 되찾으려고, 판돈을 한 번 더 키우는 겁니다.
65. 날아간 285만 원, 이번에 크게 넣어서 한 번에 되찾자.
66. 주가가 빠질 때 더 사들인 쪽도 개인이었습니다.
67. 12월 1일부터 12일까지, 외국인은 알테오젠을 2,780억 원어치 팔았습니다.
68. 같은 기간 개인은 4,400억 원어치를 샀죠.
69. 사연자의 차례는 한 달 뒤에 왔습니다.
70. 2026년 1월, 세계 최대 제약·바이오 투자 행사가 미국에서 열렸습니다.
71. 알테오젠 대표는 이 자리에서, 큰 제약사 열 곳과 기술 수출을 논의 중이라고 밝혔죠.
72. 1월 16일 주가는 하루에 10% 뛰어 51만 8천 원이 됐습니다.
73. 사연자는 그날 2,500만 원을 더 넣었습니다.
74. 넣은 돈은 모두 6,000만 원, 처음 500만 원의 열두 배였습니다.
75. 나흘 뒤인 1월 20일, 기다리던 기술 수출 계약이 나왔습니다.
76. 영국 제약사 GSK의 자회사와 맺은 계약으로, 최대 4,200억 원 규모였습니다.
77. 2025년 아스트라제네카와 맺은 1조 9천억 원 규모 계약에 한참 못 미쳤죠.
78. 머크에게서 받는 로열티가 시장 기대보다 낮은 2%라는 점도 다시 불거졌습니다.
79. 다음 날인 1월 21일, 주가는 22.35% 떨어진 37만 3,500원으로 마감했습니다.
80. 2020년 6월 이후 가장 큰 하루 하락이었습니다.
81. 사연자 계좌는 그날 하루에만 1,356만 원이 줄었습니다.
82. 전체로는 -1,288만 원, 처음 번 285만 원의 네 배가 넘는 손실입니다.
83. 되찾으려고 넣은 돈은 늘 가장 큰 돈이 되고, 가장 비싼 값에 들어갑니다.
84. 그래서 한 번의 하락이, 그동안 번 돈을 한꺼번에 가져갑니다.

**살아남는 방법 파트** — 🎙 진행자

85. 그렇다면 처음 번 돈 앞에서 어떻게 해야 할까요?
86. 단계마다 짝이 되는 장치를 하나씩 정리해 보겠습니다.
87. 첫째, 번 돈은 원금과 따로 담는 겁니다.
88. 수익으로 생긴 돈은 내 돈 같지 않아서, 더 쉽게 걸게 됩니다.
89. 그래서 수익이 나면 수익만큼 팔아서, 주식 계좌 밖의 다른 통장으로 옮겨 둡니다.
90. 계좌에는 처음 넣은 원금만 남기는 거죠.
91. 사연자의 7월 16일 계좌는 785만 원이었습니다.
92. 여기서 285만 원어치를 팔아 옮겼다면, 1월 21일에 남은 주식은 384만 원입니다.
93. 옮겨 둔 285만 원을 더하면 669만 원, 처음 500만 원보다 169만 원 많습니다.
94. 둘째, 운인지 실력인지는 기록으로 가립니다.
95. 벌면 내 판단 덕, 잃으면 시장 탓으로 느끼기 쉽기 때문입니다.
96. 살 때마다 날짜와 금액, 그리고 그날의 코스피와 코스닥 지수를 적어 두세요.
97. 석 달에 한 번, 같은 돈을 지수에 넣었다면 얼마였을지 옆에 적어 봅니다.
98. 적어도 1년 동안 이 비교를 해 보기 전에는, 그 수익을 실력이라고 부르지 않습니다.
99. 사연자의 2025년 기록은 알테오젠 45%, 코스피 75.6%, 코스닥 36.5%입니다.
100. 반년 결과로 금액을 일곱 배 키울 근거는 어디에도 없었던 셈입니다.
101. 셋째, 금액을 늘리는 규칙은 오르기 전에 정합니다.
102. 오르는 걸 보면서 정하면, 지금 당장 크게 넣는 게 늘 정답처럼 보이기 때문입니다.
103. 규칙은 세 줄이면 됩니다.
104. 한 번에 늘리는 건 지금 넣은 돈의 두 배까지.
105. 늘린 금액으로 큰 하락을 한 번 겪어 본 뒤에야 다음 계단.
106. 그리고 넘지 않을 상한을 숫자로 적어 두기.
107. 이 규칙이면 7월 16일 사연자가 갈 수 있는 금액은 1,000만 원까지였습니다.
108. 그러면 12월 30일까지 줄어든 돈은 285만 원이 아니라 97만 원 정도였습니다.
109. 1월 16일에 2,000만 원까지 올렸더라도, 1월 21일 손실은 291만 원이었습니다.
110. 넷째, 넣기 전에 하한가를 원으로 계산합니다.
111. 우리는 퍼센트로 생각하지만, 생활은 원 단위로 흔들립니다.
112. 우리 증시에서 한 종목이 하루에 빠질 수 있는 최대폭, 하한가는 30%입니다.
113. 넣으려는 돈에 30%를 곱해 보고, 그 금액을 잃어도 되는 돈과 비교합니다.
114. 잃어도 되는 돈이 300만 원이라면, 넣을 돈은 1,000만 원까지입니다.
115. 사연자의 6,000만 원이면, 하한가 하루에 1,800만 원이 사라질 수 있었습니다.
116. 실제로 1월 21일 하루에 줄어든 돈만 1,356만 원이었죠.
117. 다섯째, 번 돈을 다 돌려준 날은 금액을 줄이는 날로 정해 둡니다.
118. 되찾고 싶은 마음은 누구에게나 생기니, 그때 할 일을 미리 정해 두는 겁니다.
119. 수익을 다 반납하고 본전이 된 날엔, 처음 넣었던 원금 크기로 돌아갑니다.
120. 사연자 계좌가 딱 본전이던 12월 30일, 500만 원어치만 남겼다면 어땠을까요?
121. 1월에 더 넣지 않았다면, 1월 21일까지 손실은 84만 원 정도였을 겁니다.

**마무리 파트** — 🎙 진행자

122. 이렇게 해서 조금 벌고 판돈을 키웠다가 다 돌려주는 과정을 알아보았습니다.
123. 수익이 난 날은 금액을 늘리는 날이 아니라, 금액을 늘리는 규칙을 적는 날이었으면 합니다.
124. 성공 투자 하셨으면 좋겠습니다.
125. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
