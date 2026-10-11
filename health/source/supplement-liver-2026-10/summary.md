# supplement-liver-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py health supplement-liver-2026-10` (2026-10-11 07:55). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **몸에 좋다길래 영양제를 9가지로 늘렸다가 간수치 24가 89가 됐습니다. 영양제 겹쳐 먹는 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 119 / 자막 161, 길이 11:47 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–17 · 진행자 18–119 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/supplement-liver-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 몸에 좋다길래 영양제를 9가지로 늘렸다가 간수치 24가 89가 됐습니다. 영양제 겹쳐 먹는 사람들의 공통점 `속마음 · 24→89 · 공통점` 59자 — 짝 썸네일: thumbnail_1
- [ ] **T2.** 검진 결과지의 간수치 24가 2년 만에 89가 됐습니다. 영양제 9가지 챙겨 먹은 50대의 불편한 진실 `장면 · 24→89 · 불편한 진실` 57자 — 짝 썸네일: thumbnail_2
- [ ] **T3.** (짧은 변형) 영양제를 하루 14알씩 먹다 간수치 24가 89가 됐습니다. 한 줌씩 먹은 사람들의 후회 `행동 · 24→89 · 후회("마지막에 꼭 하는 후회"를 줄여 씀)` 49자 — 짝 썸네일: thumbnail_3

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 결과지 숫자 반전

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 결과지 간수치가 24에서 89로 뛴 **숫자 반전** 하나가 가장 빨리 읽힌다 (롱폼 숫자 제목 54.5% — `data_insights.md` 3번)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 검사 이름 | 간수치(ALT) | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 노랑) |
| 처음 | 24 | 잉크 #1E1E1E | 중간 크기 |
| 기간 | 2년 | 잉크 #1E1E1E | 작게, 화살표 위 |
| 결과 | 89 | 빨강 #E63B2E | 가장 큰 글자 |

전체 문구 12자 (2줄 구성: "간수치(ALT)" / "24 → 89"), 제목을 그대로 반복하지 않는다 (제목에 없는 "2년" 화살표·카드 장면을 보탬).

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat illustration on a cream (#F2EBDD) background. At the top center, a solid bright yellow (#FFD400) box with the
black bold text "간수치(ALT)". Below it, two simple white medical checkup result cards overlap in the center, with no logos,
no institution names, no barcodes, no personal data and no small print. On the smaller card at the back left, the black
number "24" in medium size. A thick black arrow points from the left card to the right card, with the small black text
"2년" above the arrow. On the larger card in front on the right, the huge red (#E63B2E) number "89", the largest element
in the image (about 28% of the image height). No pills, no bottles, no liver or organ drawings, no people, no needles,
no hospital scenes. Keep all text inside the central area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 식탁 위 영양제 통 앞에서 결과지를 든 **50대 여성의 걱정스러운 표정**이 숫자 카드보다 감정을 더 끈다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 속마음 | 좋다길래 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 노랑) |
| 결과 | 간수치 89 | 흰 글자 (빨강 #E63B2E 상자) | "89"를 가장 크게 |

전체 8자. 짝 제목 T2에 없는 속마음 "좋다길래"를 보탠다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A bright home kitchen table in the morning, background softly blurred in warm cream tones.
On the left 45% of the frame, a fictional Korean woman in her early 50s, office-worker look (neat blouse), holding a
single health checkup result sheet in her hands, the sheet facing away or blurred so no text is readable, surprised and
worried expression looking at the paper. Fictional person, not resembling any real or famous person, natural Korean
features. Not a doctor, no white coat, no hospital, no needles. On the table in front of her: several plain white plastic
supplement bottles with absolutely no labels, no text, no logos and no brand-like colors, and a small saucer with a modest
handful of pills (no pills pouring or spilling). On the right side, large bold headline text "좋다길래" in ink black on a
solid bright yellow (#FFD400) box. Below it, a wide solid red (#E63B2E) rounded box containing the white bold text
"간수치 89", with the number "89" much larger than the word. No crying, no extreme fear.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (영양제 9가지 vs 간수치 89)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 왼쪽에 줄지어 선 **영양제 통 9개**(믿었던 것)와 오른쪽 **빨간 89**(결과)를 나란히 놓으면 "많이 먹은 게 문제였구나"가 한눈에 읽힌다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 9가지 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (유일한 노랑) |
| 오른쪽 위 | 간수치 | 흰색 #F7F3EA | 작게 |
| 오른쪽 | 89 | 빨강 #E63B2E (흰 테두리) | 가장 큰 글자 |

전체 8자. 짝 제목 T3("하루 14알")에 없는 "9가지"를 보탠다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat editorial paper-collage graphic. The frame is split by a vertical torn-paper edge in the middle.
Left half (cream #F2EBDD): exactly nine identical plain white supplement bottles drawn with thin ink outlines, arranged
neatly in three rows of three, with absolutely no labels, no text, no logos and no brand-like colors. Above the bottles,
the black bold text "9가지" on a solid bright yellow (#FFD400) box. Right half (dark navy #14213D): the small off-white
bold word "간수치" near the top, and below it the huge red (#E63B2E) number "89" with a thin white outline, the largest
element in the image (about 30% of the image height). No people, no faces, no organs, no pills spilling.
Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
2년 전 건강검진에서 24였던 간수치가, 영양제를 하루 14알까지 늘린 올해는 89가 나왔습니다.
영양제를 겹쳐 먹으면 왜 문제가 되는지 5가지로, 영양제를 먹는 방법 6가지와 먹어도 되는 기준을 정리했습니다.

■ 이 영상에서 다루는 것
- 식품이니까 괜찮다는 생각 (2025년 식약처 회수 사례와 새 섭취 시 주의사항)
- 여러 개를 겹쳐 먹을수록 성분끼리 부딪친다 (질병관리청·식약처 안내)
- 고르는 기준이 광고였다 (건강기능식품 부당광고 적발 자료)
- 먹는 것을 말하지 않으면 원인을 찾기 어렵다 (미국 성인 9,685명 연구, 2024)
- 간은 결과지 숫자로 먼저 말할 수 있다 (간기능 검사 AST·ALT 기준)
- 영양제를 먹는 6가지 방법: 한 장에 적기, 의사·약사에게 보여 주기, 하나씩 시작하기, 섭취 시 주의사항 지키기, 광고 말고 표시 보기, 간수치가 넘으면 멈추고 진료

■ 챕터
0:00 사연: 영양제 9가지, 간수치 24가 89로
1:30 왜 영양제를 하나씩 늘릴까
2:44 문제 01 식품이니까 괜찮다는 생각
3:46 문제 02 겹쳐 먹을수록 부딪친다
4:37 문제 03 고르는 기준이 광고
5:21 문제 04 말하지 않으면 원인을 못 찾는다
6:31 문제 05 간은 결과지 숫자로 먼저 말한다
7:20 첫째: 먹는 것을 한 장에 적기
8:04 둘째: 목록을 의사·약사에게
8:44 셋째: 한 번에 하나씩, 시작한 날 적기
9:15 넷째: 섭취 시 주의사항 지키기
9:49 다섯째: 광고 말고 표시 보기
10:19 여섯째: 간수치가 넘으면 멈추고 진료
11:04 먹어도 되는 기준과 정리

■ 사연에 대해
이 영상의 사연은 실제 진단 기준과 통계를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 수치는 이해를 돕기 위한 예시입니다.
이 영상은 특정 제품을 추천하거나 비방하지 않습니다.

■ 출처
- 질병관리청 국가건강정보포털 「알아두면 도움이 되는 건강검진」(간기능 판정): https://health.kdca.go.kr/healthinfo/biz/health/ntcnInfo/healthSourc/thtimtCntnts/thtimtCntntsView.do?thtimt_cntnts_sn=7
- 질병관리청 「간기능검사」: https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=5444
- 질병관리청 「독성 간 손상」: https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6585
- 질병관리청 「건강기능식품」: https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6548
- 식약처 체지방 감소 건강기능식품 이상사례 신고 자료 (아시아경제, 2026.6.27): https://view.asiae.co.kr/article/2026062710593567678
- 식약처 회수 조치 (데일리메디, 2025.9.23): https://www.dailymedi.com/news/news_view.php?ca_id=22&wr_id=929278
- 식약처 기능성 원료 재평가·함께 섭취 주의 (데일리팜, 2025.1): https://www.dailypharm.com/Users/News/NewsView.html?ID=319344
- 식약처 섭취 시 주의사항 개정 (약사공론, 2026.6): https://www.kpanews.co.kr/news/articleView.html?idxno=536539
- 식약처 건강기능식품 부당광고 국정감사 자료 (푸드투데이, 2026.9): https://www.foodtoday.or.kr/news/article.html?no=208303
- Likhitsup 외, JAMA Network Open 2024 (미국 성인 9,685명): https://doi.org/10.1001/jamanetworkopen.2024.25822
- 미국 국립보건원 LiverTox 「Vitamins」: https://www.ncbi.nlm.nih.gov/books/NBK548888/
- 미국 국립보건원 LiverTox 「Vitamin A」: https://www.ncbi.nlm.nih.gov/books/NBK548165/
- 식약처 건강기능식품 종합정보 서비스 「의약품 병용섭취정보」: https://data.mfds.go.kr/hid/opeaa01/drugUsjntIntkAttnMttrLst.do
- 식약처 건강기능식품 섭취 주의보 (파이낸셜뉴스, 2026.9.20): https://www.fnnews.com/news/202609201847458035
- 식품안전나라 건강기능식품 이상사례 신고: https://www.foodsafetykorea.go.kr/portal/sideeffect/online.do

■ 의학적 진단이 아닙니다
이 영상은 건강 정보 제공을 위한 것이며, 의사의 진단과 치료를 대신하지 않습니다.
사연 속 수치는 실제 진단 기준을 바탕으로 재구성한 예시입니다.
검사 결과와 몸 상태는 사람마다 다르니, 치료와 영양제·식단·운동 변화는 의사와 상담하세요.
영상 속 통계와 연구의 출처는 설명란에 있습니다.

#간수치 #영양제부작용 #건강정보
```

**태그**: 영양제 부작용, 간수치 높은 이유, 간수치, 간기능 검사, 영양제 과다 복용, 영양제 조합, 건강기능식품, 건강검진 결과 보는법, 50대 건강관리, 건강검진, 건강정보, 식약처, 질병관리청

**고정 댓글**

```
오늘 드시는 영양제를 전부 꺼내 이 두 가지만 확인해 보세요.
1. 성분과 하루 섭취량을 한 장에 적었을 때 같은 성분이 두 번 나오는지
2. 그 목록을 의사나 약사에게 보여 준 적이 있는지

여러분은 영양제를 몇 가지 드시나요? 목록을 정리해 보고 바꾼 점이 있다면 나눠 주세요.
※ 개인 증상·약에 대한 질문은 진료하는 의사와 상담해 주세요. 영상은 진단을 대신하지 않습니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 2년 전 건강검진 결과지에 찍힌 제 간수치는 24였어요.
2. 걱정할 게 하나도 없는 숫자였죠.
3. 그때 저는 쉰하나, 회사 일에 집안일까지 하느라 늘 피곤한 직장인이었어요.
4. 회식 자리에서는 술도 조금씩 마셨고요.
5. 늘 몸이 무거우니 홈쇼핑이나 광고에서 몸에 좋다는 영양제를 보면 하나씩 샀어요.
6. 종합비타민에 비타민 D를 따로 더하고, 눈과 관절, 장에 좋다는 것도 샀죠.
7. 마지막에는 살 빠지게 돕는다는 제품까지 더했어요.
8. 그렇게 2년 만에 9가지, 하루 14알이 됐습니다.
9. 아침저녁으로 한 줌씩 삼키고 나면 몸을 챙기고 있다는 생각에 든든했어요.
10. 그런데 그 한 줌이 쌓이는 동안 제 간은 다른 이야기를 하고 있었습니다.
11. 올해 결과지의 간수치는 89, 기준인 35를 두 배 넘게 넘어 있었어요.
12. 병원에서 검사해 보니 간염도 아니고 지방간도 아니라고 했어요.
13. 의사 선생님은 제가 적어 간 영양제 9가지 목록을 한참 들여다봤죠.
14. 여러 개를 한꺼번에 먹어서 무엇 때문인지 하나로 짚기 어렵다고요.
15. 일단 전부 끊고 다시 재 보자는 말에 아무 대답도 못 했어요.
16. 몸에 좋다는 말만 믿고 한 알씩 더한 게 제 간에는 짐이었던 거예요.
17. 목록을 의사에게 한 번만 보여 줬어도 9가지까지는 가지 않았을 텐데요.

**진행자 파트** — 🎙 진행자

18. 영양제를 하나씩 늘려 갈 때 많은 분들이 이런 생각을 하죠.
19. 몸에 좋은 거니까 많이 먹을수록 좋겠지.
20. 약도 아니고 식품인데 뭐.
21. 하나 더 먹는다고 무슨 일 있겠어.
22. 이런 식으로 한 알씩 더하다 보면 무엇을 얼마나 먹는지 나도 모르게 됩니다.
23. 식약처가 국회에 낸 자료를 보면 이런 일이 드물지 않습니다.
24. 체지방 감소 기능성을 내세운 건강기능식품의 이상사례 신고는 2023년 217건이었습니다.
25. 그런데 2024년에는 717건, 2025년에는 920건으로 늘었죠.
26. 2020년부터 올해 5월까지 모두 2,375건입니다.
27. 물론 신고는 먹은 뒤 증상이 있었다는 뜻이지, 제품 때문이라고 확인됐다는 뜻은 아닙니다.
28. 그래도 사연자처럼 살 빠지게 돕는다는 제품까지 더해 먹는 분들에게는 남의 일이 아니죠.
29. 그럼 영양제를 이렇게 늘려 가면 무엇이 문제인지 차례로 살펴보겠습니다.

> 🟨 [장면] 의학적 진단이 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 건강 정보 제공을 위한 것이며, 의사의 진단과 치료를 대신하지 않습니다.
> 사연 속 수치는 실제 진단 기준을 바탕으로 재구성한 예시입니다.
> 검사 결과와 몸 상태는 사람마다 다르니, 치료와 영양제·식단·운동 변화는 의사와 상담하세요.
> 영상 속 통계와 연구의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

30. 첫 번째 문제는 식품이니까 괜찮다는 생각입니다.
31. 나라가 기능성을 인정한 원료라도 드물게 간에 탈이 날 수 있습니다.
32. 2025년 9월 식약처는 체지방 감소 제품 하나를 회수 조치했습니다.
33. 기능성 원료인 가르시니아캄보지아 추출물이 든 제품이었죠.
34. 이 제품을 먹은 두 사람에게서 급성 간염 증상이 보고됐기 때문입니다.
35. 제품을 검사해 보니 기준에 어긋난 것은 없었습니다.
36. 그런데도 식약처 건강기능식품 심의위원회는 인과관계 가능성이 매우 높다고 봤습니다.
37. 두 사람 모두 제품을 먹는 동안 술도 함께 마신 것으로 확인됐고요.
38. 그 뒤 이 원료의 섭취 시 주의사항에는 간에 관한 문구가 더해졌습니다.
39. 드물게 간에 해를 끼칠 수 있으니, 먹는 동안에는 술을 피하라는 내용입니다.
40. 회식 때 술을 마시던 사연자도 영양제 통의 주의사항은 한 번도 읽지 않았죠.
41. 두 번째는 여러 개를 겹쳐 먹을수록 성분끼리 부딪칠 일이 늘어난다는 것입니다.
42. 질병관리청은 건강기능식품 여러 개를 함께 먹으면 문제가 생길 수 있다고 설명합니다.
43. 성분끼리 흡수를 방해하거나 서로 작용해서 부작용이 생길 수 있다는 거죠.
44. 식약처도 앞의 원료가 든 제품은, 다른 체지방 감소 제품과 함께 먹지 말라고 안내합니다.
45. 같은 효과를 노린 제품끼리 함께 먹으면 이상사례가 생길 우려가 있다고 본 겁니다.
46. 사연자의 9가지에도 겹치는 게 있었습니다.
47. 종합비타민 안에 든 비타민 D에, 따로 먹는 비타민 D가 한 번 더 들어가고 있었죠.
48. 통은 9개로 다 달라도 속을 열어 보면 같은 성분이 두 번씩 들어갈 수 있습니다.
49. 세 번째는 무엇을 먹을지 고른 기준이 광고였다는 것입니다.
50. 식약처가 2022년부터 올해 7월까지 적발한 건강기능식품 부당광고를 보겠습니다.
51. 모두 1만 5,812건이었습니다.
52. 그중 가장 많은 33%가 병을 예방하거나 치료한다고 내세운 광고였습니다.
53. 건강기능식품은 병을 고치는 약이 아닌데, 광고는 그렇게 말하고 있었던 겁니다.
54. 건강기능식품인 척한 일반식품 광고도 지난해 7,244건으로 최근 5년 중 가장 많았습니다.
55. 홈쇼핑과 광고를 보고 하나씩 사 모은 사연자의 목록도 결국 광고가 골라 준 셈이죠.
56. 네 번째는 먹는 것을 아무에게도 말하지 않으면, 탈이 나도 원인을 찾기 어렵다는 것입니다.
57. 미국 미시간대 연구진이 2024년에 미국 국민건강영양조사 자료를 분석한 연구가 있습니다.
58. 2017년부터 2020년 초까지의 자료입니다.
59. 성인 9,685명 중 57.6%가 최근 한 달 안에 건강보조제를 먹었습니다.
60. 간 손상 보고가 있는 식물 성분 6가지 중 하나라도 먹는 사람은 4.7%였습니다.
61. 그중 가장 많이 먹은 건 강황이었고요.
62. 한 시점에 조사한 자료라서 이 성분들이 실제로 간을 상하게 했는지는 알 수 없습니다.
63. 다만 연구진은 의사들이 영양제를 먹는지 꼭 묻지는 않는다고 지적했습니다.
64. 질병관리청은 독성 간 손상을 진단할 때, 먹은 이력과 간기능 검사를 본다고 설명합니다.
65. 다른 원인을 하나씩 빼 가며 무엇을 먹었는지 따지는 거죠.
66. 9가지를 한꺼번에 먹은 사연자의 경우, 의사도 원인을 하나로 짚지 못했죠.
67. 다섯 번째는 간이 아프다는 신호보다, 결과지 숫자로 먼저 말할 수 있다는 것입니다.
68. 질병관리청은 우리나라 독성 간 손상의 원인으로 약물과 한약, 건강보조제 등을 꼽습니다.
69. 그리고 독성 간 손상은 증상이 없을 수도 있다고 합니다.
70. 결과지에는 간수치가 보통 AST와 ALT 두 칸으로 나옵니다.
71. 질병관리청 안내로는 AST가 40, ALT가 35를 넘으면 간기능 이상 의심입니다.
72. 검사한 곳에 따라 기준 숫자는 조금 다를 수 있으니 결과지의 기준도 같이 보세요.
73. 사연자도 아픈 데 하나 없이, 결과지의 ALT 89를 보고서야 알게 됐죠.
74. 그렇다면 영양제는 어떻게 먹어야 할까요?

**올바른 방법 설명 파트** — 🎙 진행자

75. 첫째, 지금 먹는 영양제를 전부 꺼내 한 장에 적는 것입니다.
76. 제품 이름 대신 통 뒷면에 적힌 성분과 함량, 하루 섭취량을 옮겨 적으세요.
77. 사연자의 9가지, 하루 14알을 한 장에 적으면 비타민 D가 두 줄에 나옵니다.
78. 같은 성분이 두 번 보이면 함량을 더해 보고 의사나 약사에게 물어보면 됩니다.
79. 미국 국립보건원 자료로는, 권장량을 지킨 비타민이 간 손상과 이어진 적은 없습니다.
80. 하지만 비타민 A는 하루 4만 국제단위 넘게 먹으면, 간을 해칠 수 있다고 합니다.
81. 한 장에 적어 둬야 내가 먹는 양이 권장량을 넘는지 물어볼 수 있습니다.
82. 둘째, 그 목록을 검진이나 진료 때 의사나 약사에게 보여 주는 것입니다.
83. 앞의 연구처럼 의사가 먼저 묻지 않을 수 있으니, 내가 먼저 꺼내야 합니다.
84. 특히 약을 먹고 있다면 새 영양제는 먹기 전에 상담하세요.
85. 식약처 건강기능식품 종합정보 서비스에서는 약과 함께 먹을 때 주의할 점을 알려 줍니다.
86. 지금은 원료 33가지에 대한 정보가 올라와 있습니다.
87. 제품 포장에 QR 코드가 있으면 찍어서 이런 정보를 확인할 수도 있습니다.
88. 사연자는 9가지가 될 때까지 목록을 누구에게도 보여 주지 않았죠.
89. 셋째, 새 영양제는 한 번에 하나씩 시작하고, 시작한 날을 적어 두는 것입니다.
90. 사연자는 2년 동안 9가지를 아무 기록 없이 늘렸습니다.
91. 그래서 간수치가 오른 뒤에도 언제 무엇을 더한 뒤였는지 알 수 없었죠.
92. 예를 들어 하나를 시작하면 몇 주 지켜보고, 이상이 없을 때 다음 것을 고민하는 식입니다.
93. 시작한 날이 적혀 있으면 문제가 생겼을 때 의사가 원인을 좁히기 쉬워집니다.
94. 넷째, 통에 적힌 섭취 시 주의사항을 읽고 그대로 지키는 것입니다.
95. 질병관리청도 건강기능식품의 포장과 라벨에서 섭취 시 주의사항을 확인하라고 안내합니다.
96. 앞의 체지방 감소 원료처럼, 술이나 같은 기능 제품을 피하라는 문구가 붙은 것도 있습니다.
97. 주의사항에 내가 앓는 병이나 먹는 약이 나온다면 먹기 전에 상담부터 하세요.
98. 회식 날 술을 마시고도 영양제를 그대로 챙겨 먹던 사연자에게 꼭 필요했던 일이죠.
99. 다섯째, 광고 문구 대신 제품에 적힌 표시를 보고 고르는 것입니다.
100. 건강기능식품에는 그 문구나 도안이 있고, 식약처가 인정한 기능성만 적을 수 있습니다.
101. 병을 예방하거나 치료한다는 말은 부당광고로 가장 많이 적발되는 유형입니다.
102. 그런 말이 들리면 사기 전에 한 번 멈추세요.
103. 좋다는 말을 들을 때마다 한 통씩 늘린 사연자라면, 그 말부터 의심해 봐야 했던 거죠.
104. 여섯째, 간수치가 기준을 넘었거나 몸이 이상하면 영양제를 멈추고 진료를 받는 것입니다.
105. 이때 첫째에서 적은 목록을 꼭 들고 가세요.
106. 질병관리청에 따르면, 독성 간 손상의 가장 중요한 치료는 원인을 바로 끊는 것입니다.
107. 그리고 대부분은 간 기능이 정상으로 돌아온다고 합니다.
108. 사연자처럼 89가 나왔다면 의사와 끊을 것을 정하고, 끊은 뒤 다시 재 보면 됩니다.
109. 다만 병원에서 처방받은 약은 혼자 끊지 말고 의사와 먼저 상의하세요.
110. 먹고 탈이 났다면 식품안전나라나 전화 1577-2488로 이상사례를 신고할 수 있습니다.
111. 그렇다고 영양제가 모두 나쁜 것은 아닙니다.
112. 검사나 진료로 부족하다는 게 확인됐거나, 의사가 권한 것이라면 도움이 될 수 있습니다.
113. 표시된 하루 섭취량을 지키고, 목록을 의사에게 보여 줬다면 걱정을 크게 덜 수 있죠.
114. 많이 먹는 것보다 내게 무엇이 필요한지 알고 먹는 것이 기준입니다.

**마무리** — 🎙 진행자

115. 이렇게 해서 영양제를 늘리다 간수치가 오르는 이유와, 여섯 가지 방법을 알아보았습니다.
116. 오늘 먹는 영양제를 전부 꺼내 한 장에 적어 보세요.
117. 그리고 다음 검진 때 그 종이를 의사에게 보여 주세요.
118. 건강하셨으면 좋겠습니다.
119. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
