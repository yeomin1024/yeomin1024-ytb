# bleach-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py lifetips bleach-2026-10` (2026-10-11 08:41). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **1분이면 녹는다는 말에 락스에 세정제까지 뿌렸다가 응급실에서 4시간을 보냈습니다. 화장실 곰팡이 잡던 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 89 / 자막 110, 길이 8:28 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–15 · 진행자 16–89 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/bleach-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 1분이면 녹는다는 말에 락스에 세정제까지 뿌렸다가 응급실에서 4시간을 보냈습니다. 화장실 곰팡이 잡던 사람들의 공통점 `속마음 · 1분→응급실 4시간 · 공통점` 65자 — 짝 썸네일: thumbnail_1
- [ ] **T2.** 욕실 문 닫고 락스를 뿌렸다가 1분 꿀팁이 응급실 4시간이 됐습니다. 환기 없이 청소한 사람들이 마지막에 꼭 하는 후회 `행동 · 1분→응급실 4시간 · 마지막에 꼭 하는 후회` 66자 — 짝 썸네일: thumbnail_2
- [ ] **T3.** (짧은 변형) 화장실 곰팡이 1분 꿀팁이 응급실 4시간 됐습니다. 세정제의 불편한 진실 `계기 · 1분→응급실 4시간 · 불편한 진실` 40자 — 짝 썸네일: thumbnail_3 (검은 배경 제목형 — 채택 제목 문구)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (1분 → 응급실 4시간)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 꿀팁이 약속한 **"1분"**이 **"응급실 4시간"**으로 뒤집힌 시간 반전이 가장 클릭을 부른다 (몸을 다친 사연은 시간으로 반전, `title_rules.md` 6-1)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 펀치 (작은 카드) | 1분 꿀팁 | "1분" 파랑 #2D6CDF / "꿀팁" 잉크 #1E1E1E | "꿀팁"에 노랑 형광펜 #FFD400 (글자 전체 높이) |
| 위쪽 핵심 숫자 | 응급실 4시간 | 흰색 (빨강 #E63B2E 상자 위) | 가장 큰 글자 |
| 하단 1줄 | 락스에 세정제까지 뿌렸다가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | — |
| 하단 2줄 | 응급실에서 4시간 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | 줄 전체 "응급실에서 4시간" 빨강 #E63B2E (위험 결과) |

- 길이: 펀치 5자 · 하단 1줄 14자 · 하단 2줄 9자 (2줄 합 23자)
- 강조 합 3곳: 노랑 형광펜 "꿀팁" · 빨강 상자 "응급실 4시간" · 하단 빨강 "응급실에서 4시간"

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, safe blue #2D6CDF, cost red #E63B2E.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain.
Upper-left area: a small light-cream rounded card with a thin black outline, containing a simple line-drawing stopwatch
icon (no numerals, no marks with digits) and next to it the text "1분 꿀팁" in bold blue (#2D6CDF); only the word "꿀팁"
is in ink black on a bright yellow (#FFD400) highlighter box of full letter height. A single thick ink-black arrow goes
from the small card down to the right. Upper-right area, still inside the upper 60%: a wide solid red (#E63B2E) rounded
box with the huge white bold text "응급실 4시간", the largest text in the image, with "4시간" slightly larger.
No people, no faces, no hospital, no ambulance, no medical cross, no bottles, no spray, no pouring, no smoke.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "락스에 세정제까지 뿌렸다가", line 2 "응급실에서 4시간". The words "응급실에서 4시간" in line 2 are red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Minimal, nothing decorative. Keep all text and key elements inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (욕실 문 앞)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 욕실 문 앞에서 입을 가리고 기침하는 **사람의 표정**이 숫자 카드보다 "내 얘기다"를 더 끈다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 핵심 숫자 | 응급실 4시간 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |
| 하단 1줄 | 문 닫고 락스 뿌렸다가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | — |
| 하단 2줄 | 1분 꿀팁이 응급실 4시간 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "1분"만 노랑 #FFD400 글자 (꿀팁이 약속한 시간) |

- 길이: 하단 1줄 12자 · 하단 2줄 14자 (2줄 합 26자) · 펀치 없음
- 하단 2줄은 짝 제목 T2 앞 문장을 줄인 것 ("욕실 문 닫고 락스를 뿌렸다가" → "문 닫고 락스 뿌렸다가", "응급실 4시간이 됐습니다" → "응급실 4시간")
- 강조 합 2곳: 빨강 상자 "응급실 4시간" · 하단 노랑 "1분"

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, safe blue #2D6CDF, cost red #E63B2E.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: realistic photo style, soft natural light. A home hallway right outside a small bright
white-tiled bathroom; the bathroom door is half open behind her and the clean white tile grout inside is softly blurred.
On the left 45% of the frame, a fictional Korean woman in her late 40s in comfortable home clothes, shown from the chest
up, covering her mouth with one hand while coughing, eyes slightly watery, embarrassed and regretful expression.
Fictional person, not resembling any real or famous person, natural Korean features. She is standing upright and steady.
No cleaning bottles, no spray bottles, no pouring, no mixing, no smoke, no fumes, no hospital, no ambulance, no oxygen
mask, nobody lying down. On the right side, inside the upper 60%, a wide solid red (#E63B2E) rounded box containing the
huge white bold text "응급실 4시간", the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "문 닫고 락스 뿌렸다가", line 2 "1분 꿀팁이 응급실 4시간". The word "1분" in line 2 is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep face and text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 검은 배경 제목형 (채택 제목 문구)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 그림 없이 검은 배경에 채택 제목 문구만 크게 넣은 썸네일이 **글자만으로** 클릭을 부르는지 (사진 썸네일 사이에서 오히려 눈에 띄는지)

| 줄 | 문구 | 글자 수 | 색 |
|---|---|---|---|
| 1 | 1분이면 녹는다는 말에 | 12 | 흰색 #FFFFFF, **"1분"만 노랑 #FFD400** (꿀팁이 약속한 시간) |
| 2 | 락스에 세정제까지 뿌렸다가 | 14 | 흰색 #FFFFFF |
| 3 | 응급실에서 4시간을 | 10 | 흰색 #FFFFFF, **"응급실에서 4시간"만 빨강 #E63B2E** (위험 결과, 조사 "을"은 흰색) |
| 4 | 보냈습니다 | 5 | 흰색 #FFFFFF |

- 4줄을 띄어쓰기 하나로 이으면 "1분이면 녹는다는 말에 락스에 세정제까지 뿌렸다가 응급실에서 4시간을 보냈습니다" = 채택 제목 앞 문장 (끝 "." 제외)
- 강조 2곳 (노랑 "1분" · 빨강 "응급실에서 4시간") — 3곳 이하. 2줄(행동)은 강조하지 않는다 (섞는 행동을 눈에 띄게 하지 않음). 파랑 글자는 쓰지 않는다 (검정 위에서 안 읽힘)

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "1분이면 녹는다는 말에", line 2 "락스에 세정제까지 뿌렸다가", line 3 "응급실에서 4시간을", line 4 "보냈습니다".
All text pure white (#FFFFFF) except "1분" in bright yellow (#FFD400) and "응급실에서 4시간" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
곰팡이가 1분이면 녹는다는 영상만 믿고, 창문 없는 욕실 문까지 닫은 채 세정제를 겹쳐 뿌린 주부는 응급실에서 4시간을 보냈습니다.
화장실 곰팡이 청소에서 몸이 먼저 상하는 이유 3가지와, 락스를 안전하게 쓰는 방법 5가지를 정리했습니다.

■ 이 영상에서 다루는 것
- 세정제끼리 만나면 자극적인 기체가 생긴다 (2026년 10월 제주 호텔 수영장 염소가스 사고)
- 닫힌 욕실에서 뿌리면 더 많이 들이마신다 (뿌리지 말고 적셔 닦기)
- 더 독하게 해도 곰팡이는 끝나지 않는다 (한국소비자원 곰팡이 세정제 시험, 습기 관리)
- 안전하게 지우는 5가지: 한 번에 세정제 하나만, 시작 전부터 끝난 뒤까지 환기, 뿌리지 말고 적셔서 닦기, 습기부터 잡기, 이상하면 멈추고 밖으로

■ 챕터
0:00 사연: 1분 꿀팁이 응급실 4시간으로
1:23 왜 더 세게 하고 싶을까
2:35 문제 01 세정제끼리 만나면 기체가 생긴다
3:55 문제 02 닫힌 욕실에서 뿌리면 더 들이마신다
4:52 문제 03 더 독하게 해도 곰팡이는 안 끝난다
5:43 첫째: 한 번에 세정제 하나만
6:11 둘째: 시작 전부터 끝난 뒤까지 환기
6:41 셋째: 뿌리지 말고 적셔서 닦기
7:09 넷째: 습기부터 잡기
7:41 다섯째: 이상하면 멈추고 밖으로
8:12 정리

■ 몸이 이상하면
청소 중 눈이나 목이 따갑거나 기침이 나면 바로 멈추고 신선한 공기가 있는 곳으로 나가세요. 숨쉬기 힘들면 119에 연락하세요.

■ 사연에 대해
이 영상의 사연은 실제 기준과 공식 자료를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시입니다.

■ 출처 (2026년 10월 11일 확인)
- 미국 질병통제예방센터(CDC) MMWR 2020, 세정제·소독제 독극물 상담 분석: https://www.cdc.gov/mmwr/volumes/69/wr/mm6916e1.htm
- 제주 호텔 수영장 염소가스 사고 원인, 제주도 발표 (파이낸셜뉴스, 2026.10.6): https://www.fnnews.com/news/202610061702144700
- 같은 사고 당일 보도 (YTN, 2026.10.1): https://www.ytn.co.kr/_ln/0115_202610012103482882
- 같은 사고 이송 인원 (데일리안, 2026.10.1): https://www.dailian.co.kr/news/view/1697094
- 서울시 소독 안내 「뿌리지 말고 닦으세요」 (서울시 미디어허브, 2021): https://mediahub.seoul.go.kr/archives/2002183
- 강남구 일상 소독 안내 (2020): https://www.gangnam.go.kr/board/article/4487/view.do?mid=fm0503
- 한국소비자원 곰팡이 제거용 욕실세정제 시험 (데일리안, 2022.11): https://www.dailian.co.kr/news/view/1169472/
- 미국 환경보호청(EPA) 곰팡이 청소에 표백제를 써야 하나: https://www.epa.gov/mold/should-i-use-bleach-clean-mold
- 미국 환경보호청(EPA) 곰팡이에 대해 꼭 알아두어야 할 10가지: https://www.epa.gov/lep/gompangie-daehae-ggog-aladueoya-hal-10gaji
- 미국 질병통제예방센터(CDC) 염소 안내: https://www.cdc.gov/chemical-emergencies/chemical-fact-sheets/chlorine.html

■ 따라 하기 전에 확인하세요
이 영상은 생활 정보 제공을 위한 것이며, 특정 제품이나 업체를 추천하지 않습니다.
사연은 실제 기준과 공식 자료를 바탕으로 재구성한 이야기이고, 금액과 수치는 예시입니다.
제품과 집 구조마다 방법이 다르니, 제조사 사용설명서와 제품 표시사항을 먼저 따르세요.
세정제와 표백제는 서로 섞지 말고, 환기하면서 표시된 방법대로만 쓰세요.
영상 속 자료의 출처는 설명란에 있습니다.

#생활꿀팁 #화장실청소 #곰팡이제거
```

**태그**: 화장실 청소 꿀팁, 화장실 곰팡이 제거, 욕실 곰팡이, 줄눈 곰팡이, 곰팡이 제거방법, 락스 사용법, 락스 희석, 세정제 섞지 않기, 염소가스, 욕실 청소, 청소 꿀팁, 생활꿀팁, 살림꿀팁, 한국소비자원

**고정 댓글**

```
화장실 곰팡이를 지우기 전에 세 가지를 확인해 보세요.
1. 세정제는 한 번에 하나만 (다른 세정제와 겹쳐 쓰지 않기)
2. 욕실 문과 환풍기, 창문부터 열고 시작하기
3. 눈이나 목이 따갑거나 기침이 나면 바로 멈추고 밖으로, 숨쉬기 힘들면 119

꿀팁을 따라 했다가 오히려 고생한 적 있나요? 그때 무엇을 먼저 확인했으면 좋았을까요?
※ 제품마다 방법이 다르니 사용설명서를 먼저 확인해 주세요. 특정 제품 홍보·구매 링크 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 지난 7월, 1분이면 곰팡이가 녹는다는 영상을 보고 욕실 청소를 시작했어요.
2. 흔히 락스라고 부르는 염소계 표백제만 뿌리면 된다는 영상이었죠.
3. 장마가 끝나면 해마다 욕실 줄눈이 까만 곰팡이로 덮였거든요.
4. 저는 마흔일곱, 창문 없는 욕실이 딸린 오래된 아파트에 사는 주부예요.
5. 이번에는 확실하게 끝내려고 집에 있던 다른 욕실 세정제까지 같은 줄눈에 뿌렸어요.
6. 냄새가 거실로 퍼질까 봐 욕실 문도 꼭 닫았고요.
7. 몇 분 만에 까맣던 줄눈이 하얗게 변하는 걸 보니 속이 다 시원했어요.
8. 하지만 그 1분 꿀팁에는 따로 치러야 할 값이 있었습니다.
9. 갑자기 눈물이 쏟아지고 기침이 멈추지 않더니 가슴이 꽉 조여 왔어요.
10. 겨우 욕실을 빠져나와 119를 불렀고, 응급실에서 4시간을 보낸 뒤에야 집에 돌아왔어요.
11. 그 뒤로도 며칠 동안 마른기침이 이어졌죠.
12. 나중에 알고 보니, 두 세정제가 섞이면서 자극적인 기체가 생긴 거였어요.
13. 창문도 없는 욕실에 문까지 닫았으니, 그 기체를 제가 고스란히 마신 거죠.
14. 곰팡이를 1분 만에 지우려다 응급실에서 4시간을 보낸 셈이에요.
15. 세정제 통 뒷면의 주의사항은 한 번도 읽어 보지 않았네요.

**진행자 파트** — 🎙 진행자

16. 화장실 곰팡이를 보면 많은 분들이 이런 생각을 하죠.
17. 곰팡이에는 독한 게 최고지.
18. 세정제 두 개를 같이 쓰면 더 잘 지워지겠지.
19. 냄새 좀 나는 건 잠깐이니까 괜찮아.
20. 이런 식으로 더 세게, 더 빨리 끝내려다 보면 몸이 먼저 탈이 날 수 있습니다.
21. 실제로 미국에서는 2020년 1월부터 3월까지 세정제와 소독제 상담이 크게 늘었습니다.
22. 독극물 상담센터에 걸려 온 전화가 1년 전 같은 기간보다 20.4% 많았죠.
23. 그중 세정제 쪽에서 늘어난 전화의 62%가 표백제 때문이었습니다.
24. 코로나19로 청소와 소독이 크게 늘던 때, 미국 질병통제예방센터가 분석한 결과입니다.
25. 살림 영상 댓글에도 락스로 청소하다 눈물 콧물이 났다는 경험담이 적지 않죠.
26. 사연 속 일이 어느 집 욕실에서든 일어날 수 있는 이유입니다.
27. 그럼 이런 청소가 왜 문제인지 하나씩 살펴보겠습니다.

> 🟨 [장면] 따라 하기 전에 확인하세요 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 생활 정보 제공을 위한 것이며, 특정 제품이나 업체를 추천하지 않습니다.
> 사연은 실제 기준과 공식 자료를 바탕으로 재구성한 이야기이고, 금액과 수치는 예시입니다.
> 제품과 집 구조마다 방법이 다르니, 제조사 사용설명서와 제품 표시사항을 먼저 따르세요.
> 세정제와 표백제는 서로 섞지 말고, 환기하면서 표시된 방법대로만 쓰세요.
> 영상 속 자료의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

28. 첫 번째 문제는 세정제끼리 만나면 자극적인 기체가 생길 수 있다는 것입니다.
29. 락스, 즉 염소계 표백제의 주성분은 차아염소산나트륨입니다.
30. 이 성분이 산성 물질 같은 다른 약품과 섞이면 염소가스가 생길 수 있습니다.
31. 올해 10월 1일, 제주의 한 호텔 수영장에서 바로 이런 사고가 났습니다.
32. 제주도가 밝힌 원인은 소독약을 다른 약품이 든 통에 잘못 넣은 것이었습니다.
33. 두 약품이 섞이면서 염소가스가 생긴 거죠.
34. 380여 명이 대피했고, 59명이 병원으로 옮겨졌습니다.
35. 메스꺼움과 구토, 두통 같은 증상이었습니다.
36. 다행히 생명에 지장은 없었지만, 약품 하나를 잘못 넣은 실수로 벌어진 일이었죠.
37. 사연자의 욕실에서 일어난 일도 크기만 작을 뿐 같은 종류의 사고였던 겁니다.
38. 미국 환경보호청도 곰팡이 청소 안내에서 같은 점을 경고합니다.
39. 염소계 표백제를 특정 성분이 든 다른 세정제와 섞으면 유독한 기체가 생길 수 있다는 거죠.
40. 수십 년 이렇게 청소했는데 괜찮았다는 분도 계실 겁니다.
41. 그건 그때 섞인 제품이 없었거나, 공기가 잘 통했기 때문일 수 있습니다.
42. 두 번째는 문을 닫은 좁은 욕실에서 뿌리는 방식이 들이마시는 양을 키운다는 것입니다.
43. 서울시는 코로나19 시기 소독 안내에서 소독제를 뿌리지 말고 천에 적셔 닦으라고 했습니다.
44. 뿌리면 아주 작은 물방울이 공기 중에 떠서 숨으로 들이마시기 쉽기 때문입니다.
45. 그리고 작업을 시작하기 전에 먼저 문을 열어 환기하라고 안내했죠.
46. 사연자는 창문 없는 욕실에서 문까지 닫고, 줄눈 전체에 세정제를 뿌렸습니다.
47. 기체가 빠져나갈 길을 모두 막은 채, 그 안에서 숨을 쉬고 있었던 겁니다.
48. 미국 질병통제예방센터는 염소가스를 마시면 눈물이 나고 목이 따가울 수 있다고 합니다.
49. 기침이 나고 가슴이 조이는 느낌이 들기도 하죠.
50. 냄새 좀 나는 건 잠깐이라고 넘긴 그 순간에도, 몸은 이미 신호를 보내고 있었죠.
51. 세 번째는 더 독하게, 더 빨리 한다고 곰팡이가 끝나지 않는다는 것입니다.
52. 한국소비자원이 2022년 곰팡이 제거용 욕실 세정제 8개를 시험했습니다.
53. 곰팡이에 15분 동안 닿게 한 뒤에도 곰팡이를 완전히 죽인 제품은 6개였습니다.
54. 1분이면 녹는다는 말과는 거리가 있죠.
55. 미국 환경보호청은 집 안의 곰팡이와 포자를 모두 없애는 현실적인 방법은 없다고 설명합니다.
56. 곰팡이를 막는 길은 습기를 잡는 것이라고 하죠.
57. 그래서 곰팡이 청소에 표백제 같은 살균제를 늘 쓰는 것도 권하지 않습니다.
58. 사연자의 줄눈이 장마 뒤마다 다시 까매진 것도 습기 때문일 수 있습니다.
59. 그렇다면 화장실 곰팡이, 어떻게 지워야 할까요?

**올바른 방법 파트** — 🎙 진행자

60. 첫째, 곰팡이 청소에는 한 번에 세정제 하나만 씁니다.
61. 사연자처럼 같은 줄눈에 두 제품을 겹쳐 뿌리는 일부터 하지 않는 거죠.
62. 제주 사고처럼 약품이 엉뚱한 통에 들어가도 섞이는 건 똑같습니다.
63. 그래서 세정제는 다른 통이나 분무기에 옮겨 담지 말고 처음 통 그대로 씁니다.
64. 통 뒷면 주의사항에 함께 쓰면 안 되는 제품이 적혀 있는지도 먼저 보세요.
65. 둘째, 청소를 시작하기 전부터 끝난 뒤까지 환기합니다.
66. 미국 환경보호청도 표백제를 쓸 때는 늘 환기해서 공기를 바깥으로 빼라고 안내합니다.
67. 창문 없는 욕실이라면 욕실 문을 활짝 열고 환풍기를 켜고, 거실 창문도 열어 둡니다.
68. 청소가 끝난 뒤에도 냄새가 빠질 때까지 환풍기를 켜 둡니다.
69. 사연자처럼 냄새가 퍼질까 봐 문을 닫으면, 그 냄새를 내 쪽으로 모으는 셈입니다.
70. 셋째, 뿌리지 말고 적셔서 닦고, 표시된 방법대로만 씁니다.
71. 줄눈은 분무기로 뿌리는 대신 솔이나 천에 묻혀서 문지릅니다.
72. 물에 희석해 쓰는 제품이라면 표시사항에 적힌 비율을 그대로 따릅니다.
73. 1분이면 된다는 영상보다 내 손에 든 제품의 사용법이 먼저입니다.
74. 장갑을 끼고, 청소하는 동안 눈과 코, 입을 만지지 않는 것도 잊지 마세요.
75. 넷째, 곰팡이가 다시 안 생기게 습기부터 잡습니다.
76. 미국 환경보호청은 실내 습도를 30에서 60% 사이로 낮추라고 권합니다.
77. 젖은 곳은 24시간에서 48시간 안에 말려야 곰팡이가 자라는 걸 막을 수 있다고 하죠.
78. 샤워가 끝나면 벽과 줄눈의 물기를 닦아 내고 환풍기를 켜 둡니다.
79. 사연자처럼 창문 없는 욕실이라면 샤워 뒤 욕실 문을 열어 습기가 빠질 길을 만들어 주세요.
80. 다섯째, 몸이 이상하면 바로 멈추고 밖으로 나갑니다.
81. 눈이 따갑거나 기침이 나면 하던 청소를 그 자리에서 멈춥니다.
82. 그리고 바로 욕실 밖, 신선한 공기가 있는 곳으로 나가세요.
83. 숨쉬기 힘들거나 가슴이 답답하면 망설이지 말고 119에 연락하세요.
84. 그렇다고 락스를 쓰지 말라는 얘기는 아닙니다.
85. 다른 세정제 없이 하나만, 표시된 방법대로, 환기되는 곳에서 짧게 쓰면 됩니다.

**마무리** — 🎙 진행자

86. 이렇게 해서 화장실 곰팡이 청소의 문제와 방법을 알아보았습니다.
87. 곰팡이를 지우기 전에 세정제 통 뒷면의 주의사항부터 읽어 보세요.
88. 안전하고 알뜰한 살림 하셨으면 좋겠습니다.
89. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
