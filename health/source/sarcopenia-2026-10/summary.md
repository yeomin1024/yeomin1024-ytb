# sarcopenia-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py health sarcopenia-2026-10` (2026-10-11 07:55). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **만 보만 걸으면 된다고 믿다가 2년 만에 악력 17kg, 근감소증이 됐습니다. 걷기만 하는 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 107 / 자막 132, 길이 10:17 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–15 · 진행자 16–107 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/sarcopenia-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 만 보만 걸으면 된다고 믿다가 2년 만에 악력 17kg, 근감소증이 됐습니다. 걷기만 하는 사람들의 공통점 `속마음 · 만 보→악력 17kg·근감소증 · 공통점` 59자 — 짝 썸네일: thumbnail_1
- [ ] **T2.** 매일 만 보 걷던 60대가 2년 만에 근감소증이 됐습니다. 근력운동 없이 걷기만 한 사람들이 꼭 하는 후회 `행동 · 만 보→근감소증 · 후회("마지막에 꼭 하는 후회"를 줄여 씀)` 59자 — 짝 썸네일: thumbnail_2
- [ ] **T3.** (짧은 변형) 몸무게 6kg 빠졌다고 자랑했는데 근감소증이 됐습니다. 걷기만 한 사람들의 불편한 진실 `장면(작은 만족) · -6kg→근감소증 · 불편한 진실` 48자 — 짝 썸네일: thumbnail_3

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (걸음 수 10,000 → 악력 17kg)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 매일 채운 **걸음 수 10,000**과 병원에서 잰 **악력 17kg**을 화살표 하나로 잇는 숫자 반전이 가장 빨리 읽힌다 (롱폼 숫자 제목 54.5% — `data_insights.md` 3번)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 처음 | 10,000 | 잉크 #1E1E1E | 휴대폰 화면 안, 중간 크기 |
| 처음 단위 | 걸음 | 잉크 #1E1E1E | 작게, 숫자 아래 |
| 기간 | 2년 | 잉크 #1E1E1E | 작게, 화살표 위 |
| 검사 이름 | 악력 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 노랑) |
| 결과 | 17kg | 빨강 #E63B2E | 가장 큰 글자 |

전체 13자 (2줄 구성: "10,000 걸음" / "악력 17kg"). 제목을 그대로 반복하지 않는다 — 제목에 없는 **휴대폰 걸음 수 화면**(문장 5)과 "2년" 화살표를 보탠다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat illustration on a cream (#F2EBDD) background. On the left, a simple generic smartphone seen from the front, its
plain white screen showing only the big black number "10,000" and below it the small black word "걸음". No app name, no
icons, no logos, no status bar, no other interface elements, so it does not look like any real app. In the middle, a thick
black arrow pointing from the phone to the right, with the small black text "2년" above the arrow. On the right, a simple
unbranded hand grip dynamometer (a handle with a round analog dial and a needle, the dial has no printed numbers or text).
Above the dynamometer, the black bold text "악력" on a solid bright yellow (#FFD400) box. Next to the dynamometer, the huge
red (#E63B2E) text "17kg", the largest element in the image (about 28% of the image height). No people, no hands, no gym
equipment brands, no hospital scenes, no falling. Keep all text inside the central area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (계단 난간을 붙잡은 순간)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 계단에서 다리에 힘이 풀려 난간을 붙잡은 **60대 여성의 당황한 표정**이 숫자 카드보다 감정을 더 끈다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 속마음 | 매일 걸었는데 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 노랑) |
| 결과 | 악력 17kg | 흰 글자 (빨강 #E63B2E 상자) | "17kg"을 가장 크게 |

전체 14자. 짝 제목 T2에 없는 **악력 17kg**(문장 10)과 계단 장면(문장 9)을 보탠다. "매일 걸었는데"는 진행자 연결 문장 25 "매일 걸었는데도 왜 근육이 줄었는지"와 같은 말이다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Bright daytime, outdoor concrete stairs in an apartment complex, background softly blurred in warm
cream tones. On the left 45% of the frame, a fictional Korean woman in her early 60s with neat short hair, wearing a plain
light-colored windbreaker with no patterns, no text and no logos. She is walking down the stairs and has suddenly stopped,
gripping the metal handrail firmly with one hand, knees slightly bent, both feet still on the steps, looking down at her
own legs with a surprised and flustered expression. She is standing, not falling, not sitting down, not injured.
Fictional person, not resembling any real or famous person, natural Korean features. No doctor, no white coat, no hospital,
no walking stick, no gym equipment. On the right side, large bold headline text "매일 걸었는데" in ink black on a solid
bright yellow (#FFD400) box. Below it, a wide solid red (#E63B2E) rounded box containing the white bold text "악력 17kg",
with "17kg" much larger than the word. No crying, no pain, no extreme fear.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (몸무게 -6kg vs 악력 17kg)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 왼쪽에 **체중계 -6kg**(좋아했던 숫자, 파랑)과 오른쪽 **악력 17kg**(결과, 빨강)을 나란히 놓으면 "몸무게는 줄었는데 힘이 빠졌구나"가 한눈에 읽힌다 — 썸네일 1(걸음 수)과 '믿었던 숫자'만 바꿔 어느 쪽이 더 끄는지 본다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 위 | 좋아했는데 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (유일한 노랑) |
| 왼쪽 | -6kg | 파랑 #2D6CDF | 크게 (좋아했던 숫자) |
| 오른쪽 위 | 악력 | 흰색 #F7F3EA | 작게 |
| 오른쪽 | 17kg | 빨강 #E63B2E (흰 테두리) | 가장 큰 글자 |

전체 13자 (2줄 구성: "좋아했는데 -6kg" / "악력 17kg"). 짝 제목 T3("6kg … 근감소증")에 없는 **악력 17kg**을 보태고, "근감소증"은 반복하지 않는다.

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Flat editorial paper-collage graphic. The frame is split by a vertical torn-paper edge in the middle.
Left half (cream #F2EBDD): a simple unbranded white bathroom scale seen from slightly above, drawn with thin ink outlines,
its display window blank. Above the scale, the black bold text "좋아했는데" on a solid bright yellow (#FFD400) box, and
below that the large blue (#2D6CDF) text "-6kg". Right half (dark navy #14213D): the small off-white bold word "악력" near
the top, and below it the huge red (#E63B2E) text "17kg" with a thin white outline, the largest element in the image
(about 30% of the image height). No people, no faces, no gym equipment, no hospital scenes, no logos.
Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
2년 동안 하루도 빠짐없이 만 보를 걷고 몸무게도 6kg 줄었는데, 올봄 병원에서 잰 악력은 17kg, 근감소증 진단이 나왔습니다.
매일 걸어도 근육이 줄어드는 이유 5가지와, 걷기는 그대로 두고 근육을 지키는 방법 5가지를 정리했습니다.

■ 이 영상에서 다루는 것
- 걷기만으로는 근력이 잘 늘지 않는다 (근감소증 노인 운동 연구 23개 분석, 2022)
- 근력운동을 하는 사람이 드물다 (국민건강영양조사 연구: 2024년 40세 이상, 2014~2019년 65세 이상 8,671명)
- 체중계는 근육을 보여 주지 않는다 (질병관리청 근감소증 설명)
- 근육이 줄어드는 걸 나이 탓으로만 넘기면 안 된다 (2021년 질병 코드, 2025년 아시아 근감소증 기준의 50~64세 기준)
- 약해진 손힘을 가볍게 넘기기 쉽다 (질병관리청 2026년 8월 발표)
- 근육을 지키는 5가지 방법: 집에서 근육 상태 확인하기, 근력운동 주 2일 이상, 균형 운동 섞어 주 3일, 단백질을 끼니마다, 걷기는 계속하되 기록할 숫자 바꾸기

■ 챕터
0:00 사연: 매일 만 보, 악력 17kg 근감소증으로
1:19 왜 걷기만으로 충분하다고 믿을까
2:18 문제 01 걷기만으로는 근력이 잘 늘지 않는다
2:56 문제 02 근력운동을 하는 사람이 드물다
3:50 문제 03 체중계는 근육을 보여 주지 않는다
4:24 문제 04 나이 탓으로만 넘기면 안 된다
5:15 문제 05 약해진 손힘을 가볍게 넘긴다
5:57 약으로 되돌리기는 아직 어렵다
6:27 첫째: 집에서 근육 상태부터 확인
7:09 둘째: 근력운동 주 2일 이상
7:55 셋째: 균형 운동 섞어 주 3일
8:25 넷째: 단백질을 끼니마다
9:15 다섯째: 걷기는 계속, 기록할 숫자를 바꾸기
9:56 정리

■ 사연에 대해
이 영상의 사연은 실제 진단 기준과 통계를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 수치는 이해를 돕기 위한 예시입니다.

■ 출처
- 질병관리청 보도자료 (2026.8.11, 악력과 근감소증·국민건강영양조사 2022~2024): https://www.kdca.go.kr/bbs/kdca/42/312118/artclView.do
- 질병관리청 국가건강정보포털 「근 손실」: https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6722
- 아시아 근감소증 기준 2025 (Chen 외, Nature Aging 2025): https://doi.org/10.1038/s43587-025-01004-y
- 아시아 근감소증 기준 2019 (Chen 외, JAMDA 2020): https://pubmed.ncbi.nlm.nih.gov/32033882/
- 근감소증 노인 운동 연구 메타분석 (Wang 외, IJERPH 2022): https://doi.org/10.3390/ijerph19138212
- 2024 국민건강영양조사 운동 종류와 근감소증 (Ryu, Muscles 2026): https://doi.org/10.3390/muscles5020033
- 국내 65세 이상 근력운동 참여 (J Clin Med 2024): https://doi.org/10.3390/jcm13195900
- 근감소증 질병 코드, 한국표준질병사인분류 8차 (뉴시스, 2022.9.6): https://mobile.newsis.com/view/NISX20220906_0002004367
- 대한근감소증학회 리뷰 (Ann Geriatr Med Res 2026): https://www.e-agmr.org/journal/view.php?doi=10.4235%2Fagmr.25.0182
- 근감소증 진단과 치료 리뷰 (Korean J Intern Med 2025): https://www.kjim.org/upload/kjim-2025-057.pdf
- 국내 근감소증 운동 지침 (Ann Geriatr Med Res 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12489597/
- 세계보건기구 신체활동·좌식행동 지침 2020: https://www.who.int/publications/i/item/9789240015128
- 2025 한국인 영양소 섭취기준 (보건복지부, 2025.12.31): https://www.korea.kr/briefing/pressReleaseView.do?newsId=156737581

■ 의학적 진단이 아닙니다
이 영상은 건강 정보 제공을 위한 것이며, 의사의 진단과 치료를 대신하지 않습니다.
사연 속 수치는 실제 진단 기준을 바탕으로 재구성한 예시입니다.
검사 결과와 몸 상태는 사람마다 다르니, 치료와 식단·운동 변화는 의사와 상담하세요.
영상 속 통계와 연구의 출처는 설명란에 있습니다.

#근감소증 #근력운동 #건강정보
```

**태그**: 근감소증, 근감소증 증상, 근감소증 예방 운동, 악력, 근력운동, 만보 걷기, 걷기 운동, 단백질 섭취, 60대 건강관리, 노인 건강관리, 시니어 건강, 건강정보, 질병관리청

**고정 댓글**

```
오늘 이 두 가지만 해 보세요.
1. 팔짱을 끼고 의자에서 다섯 번 일어섰다 앉는 시간을 재서 적어 두기 (한 달에 한 번)
2. 일주일에 이틀은 걷는 시간 일부를 의자에서 일어섰다 앉기 같은 근력운동으로 바꾸기

여러분은 걷기 말고 함께 하는 운동이 있나요? 근력운동을 시작해 본 경험을 나눠 주세요.
※ 개인 증상·약에 대한 질문은 진료하는 의사와 상담해 주세요. 영상은 진단을 대신하지 않습니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 2년 전 퇴직하던 날부터 저는 하루 만 보 걷기를 시작했어요.
2. 그때 저는 예순, 30년 넘게 책상 앞에만 앉아 있던 직장인이었어요.
3. 건강은 걷기만 하면 충분하다고 믿었고, 근력운동은 해 본 적이 없었죠.
4. 입맛도 줄어서 아침은 커피 한 잔, 반찬은 채소 위주로 가볍게 먹었어요.
5. 휴대폰 걸음 수는 하루도 빠짐없이 만 보를 넘겼어요.
6. 2년 사이 몸무게도 58kg에서 52kg으로 6kg이나 빠졌죠.
7. 친구들에게 걷기로 살을 뺐다고 자랑까지 했어요.
8. 하지만 빠진 건 살만이 아니었습니다.
9. 올봄 계단을 내려가다 다리에 힘이 풀려 난간을 붙잡았어요.
10. 병원에서 잰 악력은 17kg, 제 나이 여자 기준인 20kg에 못 미쳤어요.
11. 의자에서 다섯 번 일어서는 데도 13초나 걸렸고요.
12. 근육량까지 기준보다 적어서 근감소증이라는 진단을 받았습니다.
13. 의사는 걷기만 하고 근력운동은 안 한 데다, 단백질도 모자랐을 거라고 했어요.
14. 걸음 수를 채우는 동안 다리 근육은 한 번도 챙기지 않았던 거예요.
15. 6kg 빠졌다고 자랑하던 제가 이제는 부끄러워요.

**진행자 파트** — 🎙 진행자

16. 매일 부지런히 걷는 분들은 이런 생각을 하기 쉽죠.
17. 매일 만 보를 걸으니까 운동은 이걸로 충분해.
18. 살이 빠졌으니 건강해진 거야.
19. 나이 들면 근육 빠지는 건 어쩔 수 없지.
20. 이런 식으로 걸음 수와 몸무게만 보다 보면 근육이 줄어드는 건 놓치게 됩니다.
21. 질병관리청이 올해 8월, 국민건강영양조사로 노인의 근감소증을 분석해 발표했습니다.
22. 80세 이상은 네 명 중 한 명꼴로 근감소증이었습니다.
23. 65세에서 69세 사이에서는 여성이 5.8%로, 남성 2.6%의 두 배가 넘었고요.
24. 예순을 넘긴 여성에게도 근감소증은 먼 이야기가 아닌 셈이죠.
25. 그럼 매일 걸었는데도 왜 근육이 줄었는지 하나씩 살펴보겠습니다.

> 🟨 [장면] 의학적 진단이 아닙니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 건강 정보 제공을 위한 것이며, 의사의 진단과 치료를 대신하지 않습니다.
> 사연 속 수치는 실제 진단 기준을 바탕으로 재구성한 예시입니다.
> 검사 결과와 몸 상태는 사람마다 다르니, 치료와 식단·운동 변화는 의사와 상담하세요.
> 영상 속 통계와 연구의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

26. 첫 번째 문제는 걷기만으로는 근력이 잘 늘지 않는다는 것입니다.
27. 걷기는 심장과 폐를 쓰는 대표적인 유산소운동입니다.
28. 2022년에 나온 한 분석은 근감소증 노인의 운동 연구 23개를 모았습니다.
29. 참가자를 무작위로 나눠 운동 효과를 비교한 연구들이죠.
30. 근력운동이나 여러 운동을 섞은 쪽은 근력이 늘었습니다.
31. 하지만 유산소운동만 한 쪽은 근력이 뚜렷하게 늘지 않았습니다.
32. 사연자의 2년 만 보가 다리 힘을 지켜 주지 못한 것도 이 때문으로 볼 수 있죠.
33. 두 번째는 근력운동이 이렇게 중요한데도 하는 사람이 드물다는 것입니다.
34. 2024년 국민건강영양조사로 40세 이상을 살펴본 연구에서도 차이는 근력운동에서 났습니다.
35. 근력운동을 하는 사람은, 운동을 안 하는 사람보다 근감소증 가능성이 60% 넘게 낮았죠.
36. 유산소운동만 하는 사람은 뚜렷한 차이가 없었고요.
37. 한 시점에 조사한 자료라 원인과 결과까지 단정할 수는 없습니다.
38. 그런데 2014년부터 2019년까지 65세 이상 8,671명을 분석한 연구가 있습니다.
39. 근력운동을 일주일에 이틀도 안 하는 사람이 여성 91%, 남성 71%였습니다.
40. 여성은 열 명 중 아홉 명꼴로 근력운동을 거의 하지 않는 겁니다.
41. 세 번째는 체중계가 근육을 보여 주지 않는다는 것입니다.
42. 질병관리청 설명으로는 근육량이 줄고, 근력이나 신체 기능도 떨어져야 근감소증입니다.
43. 진단 기준에 몸무게는 없습니다.
44. 근육량도 몸무게가 아니라 팔다리 근육의 양을 기계로 따로 잽니다.
45. 사연자는 6kg이 빠져 좋아했지만, 병원에서 잰 악력은 17kg이었죠.
46. 단백질이 모자란 채로 몸무게가 줄면, 무엇이 빠졌는지 체중계로는 알 수 없습니다.
47. 네 번째는 근육이 줄어드는 걸 나이 탓으로만 넘기면 안 된다는 것입니다.
48. 우리나라는 2021년부터 근감소증에 질병 코드를 붙여 질병으로 분류하고 있습니다.
49. 2025년에 아시아 전문가들이 새로 낸 근감소증 기준도 있습니다.
50. 이 기준은 50세에서 64세 기준을 처음으로 따로 만들었습니다.
51. 이 나이에는 악력이 남자 34kg, 여자 20kg보다 낮으면 근력이 약하다고 봅니다.
52. 65세 이상 기준인 남자 28kg, 여자 18kg보다 높게 잡은 거죠.
53. 근육은 노인이 된 뒤가 아니라 중년부터 챙겨야 한다는 뜻입니다.
54. 사연자가 병원에서 들은 여자 기준 20kg이 바로 이 새 기준입니다.
55. 다섯 번째는 약해진 손힘을 가볍게 넘기기 쉽다는 것입니다.
56. 질병관리청 분석에서 악력이 약한 노인의 85%는 근육량까지 적은 근감소증이었습니다.
57. 손힘만 살펴봐도 근육 상태를 꽤 짐작할 수 있다는 뜻이죠.
58. 65세에서 74세 사이에서는, 악력이 약한 사람의 14.3%가 우울장애를 겪고 있었습니다.
59. 악력이 정상인 사람 2.0%보다 일곱 배 넘게 높습니다.
60. 이것도 한 시점의 조사라 어느 쪽이 먼저인지는 알 수 없습니다.
61. 그래도 손힘이 몸과 마음의 상태를 함께 비춘다는 건 알 수 있습니다.
62. 그렇다면 근육이 이미 줄었을 때 약으로 되돌릴 수는 없을까요?
63. 아쉽게도 근감소증에는 아직 효과가 입증된 약이 많지 않습니다.
64. 미국 식품의약국이 근감소증 치료제로 승인한 약도 아직 없습니다.
65. 대한근감소증학회는 2026년 논문에서 근력운동과 단백질을 치료의 중심으로 꼽았습니다.
66. 그럼 걷기에 무엇을 더해야 근육을 지킬 수 있는지 알아보겠습니다.

**올바른 방법 설명 파트** — 🎙 진행자

67. 첫째, 걸음 수 말고 근육 상태부터 집에서 확인해 보는 것입니다.
68. 가장 쉬운 방법은 팔짱을 끼고 의자에서 다섯 번 일어섰다 앉는 시간을 재는 것입니다.
69. 아시아 근감소증 기준에서는 이 시간이 12초 이상이면 기능이 떨어졌다고 봅니다.
70. 2025년 새 기준은 50세에서 64세도 따로 나눠 더 일찍 살피게 했습니다.
71. 사연자는 13초였으니 이미 기준을 넘겼던 거죠.
72. 질병관리청은 페트병 뚜껑 열기나 물수건 짜기가 힘들어졌는지도 살펴보라고 안내합니다.
73. 이런 신호가 보이면 병원에서 악력과 근육량을 재 보세요.
74. 둘째, 근력운동을 일주일에 이틀 이상 하는 것입니다.
75. 세계보건기구는 큰 근육을 두루 쓰는 근력운동을 주 2일 이상 권합니다.
76. 국내 근감소증 전문가들은 2025년 운동 지침에서 주 2회 이상을 권했습니다.
77. 그리고 적어도 12주는 꾸준히 이어 가야 한다고 봤죠.
78. 질병관리청도 탄력 밴드나 맨몸 운동을 주 2~3회 꾸준히 하라고 안내합니다.
79. 예를 들어 일주일에 이틀은 만 보 걷는 시간 일부를 근력운동에 내어 주세요.
80. 의자에서 일어섰다 앉기나 벽 짚고 팔 굽혀 밀기처럼, 집에서 할 수 있는 동작이면 됩니다.
81. 강도는 조금 힘들다 싶은 정도면 충분합니다.
82. 셋째, 균형 운동을 섞어 일주일에 사흘 이상 움직이는 것입니다.
83. 세계보건기구는 노인에게 균형과 근력을 함께 쓰는 운동을 주 3일 이상 권합니다.
84. 몸의 기능을 지키고 넘어지는 것을 막기 위해서입니다.
85. 계단에서 휘청했던 사연자라면 걷고 돌아와서 벽을 짚고 한 발로 서기부터 시작하면 됩니다.
86. 발뒤꿈치를 들었다 내리는 동작도 의자 등받이를 잡고 하면 안전하죠.
87. 넷째, 단백질을 끼니마다 챙겨 먹는 것입니다.
88. 질병관리청은 근육 손실을 관리하려면 단백질을 몸무게 1kg당 1.2g 먹도록 권합니다.
89. 52kg인 사연자라면 하루 60g 남짓입니다.
90. 세 끼로 나누면 한 끼에 20g 정도죠.
91. 아침을 커피 한 잔으로 때우면 하루 목표를 채우기 어렵습니다.
92. 달걀, 두부, 생선, 살코기 같은 음식을 끼니마다 한 가지씩 올려 보세요.
93. 2025년 한국인 영양소 섭취기준도 단백질 기준을 높였습니다.
94. 하루 열량 중 단백질로 채울 비율의 아래 기준을 7%에서 10%로 올렸죠.
95. 다만 콩팥 질환이 있으면 단백질을 조절해야 할 수 있으니, 먼저 의사와 상담하세요.
96. 다섯째, 걷기는 계속하되 기록할 숫자를 바꾸는 것입니다.
97. 질병관리청도 걷기 같은 유산소운동을 함께 하면 심폐 기능과 혈류 개선에 좋다고 설명합니다.
98. 그러니 만 보를 그만둘 필요는 없습니다.
99. 대신 한 달에 한 번, 의자에서 다섯 번 일어서는 시간을 적어 보세요.
100. 사연자라면 13초가 12초 아래로 내려오는지가 첫 목표가 됩니다.
101. 걸음 수는 그대로 두고, 근육이 붙는지를 숫자로 확인하는 겁니다.
102. 무릎이나 허리가 아프거나, 심장병이나 고혈압이 있다면 운동 강도는 먼저 의사와 상담하세요.

**마무리** — 🎙 진행자

103. 이렇게 해서 매일 걸어도 근육이 줄어드는 이유와, 지키는 방법 다섯 가지를 알아보았습니다.
104. 오늘 의자에서 다섯 번 일어서는 시간부터 재 보세요.
105. 만 보는 그대로 두고, 일주일에 이틀은 근육에도 시간을 나눠 주세요.
106. 건강하셨으면 좋겠습니다.
107. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
