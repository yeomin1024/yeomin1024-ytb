# miraclemorning-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py selfdev miraclemorning-2026-10` (2026-10-11 07:49). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **하루 2시간 벌겠다고 새벽 5시에 일어났다가 잠 200시간을 잃었습니다. 미라클모닝 따라 한 사람들의 불편한 진실**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 116 / 자막 148, 길이 11:01 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–18 · 진행자 19–116 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/miraclemorning-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 하루 2시간 벌겠다고 새벽 5시에 일어났다가 잠 200시간을 잃었습니다. 미라클모닝 따라 한 사람들의 불편한 진실 `속마음 · 이득→손실(2시간→200시간) · 불편한 진실` 63자 — 짝 썸네일: thumbnail_1 (숫자 반전)
- [ ] **T2.** 새벽 5시 인증 100일 만에 잠 200시간이 사라졌습니다. 잠 줄여 갓생 산 사람들이 마지막에 꼭 하는 후회 `장면 · 100일→200시간 · 마지막에 꼭 하는 후회` 61자 — 짝 썸네일: thumbnail_2 (인물·감정)
- [ ] **T3.** (짧은 변형) 잠 줄여 새벽 5시 100일, 잃은 잠 200시간. 미라클모닝의 공통점 `행동 · 100일→200시간 · 공통점` 39자 — 짝 썸네일: thumbnail_3 (대비)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (알람 시계 기록 카드)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 얻으려던 숫자(하루 +2시간)가 100배 큰 잃은 숫자(잠 -200시간)로 뒤집힌 **생활 숫자 반전**이 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 시계 | 05:00 | 잉크 #1E1E1E (노랑 시계 화면 위) | 노랑 #FFD400 (유일한 강조) |
| 기대 | 하루 +2시간 | 크림 #F2EBDD | — |
| 결과 | 잠 -200시간 | 흰색 (빨강 #E63B2E 상자 위) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic. Dark navy (#14213D) pre-dawn background, like a quiet bedroom before sunrise, with a very soft glow; nothing decorative.
On the left third, a simple generic tabletop digital alarm clock (no brand, no logo) whose display is a bright yellow (#FFD400) panel showing large ink-black digits "05:00".
On the right side, upper line: the text "하루 +2시간" in cream (#F2EBDD) bold letters, medium size.
Below it, a wide solid red (#E63B2E) rounded box containing the huge white bold text "잠 -200시간", the largest element in the image, about a quarter of the image height.
Keep all text and the clock inside the central 16:9 safe area. No people, no faces, no phone screens, no app interfaces, no brain imagery.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (오후 회의 전 꾸벅)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 잠을 줄인 결과를 마주한 **사람의 표정**(오후 사무실에서 꾸벅 조는 모습)이 숫자 카드보다 "내 얘기다"를 더 끈다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 장면 | 100일째, 무너졌다 | "100일째"는 잉크 #1E1E1E 글자 + 노랑 #FFD400 상자, ", 무너졌다"는 흰 글자 + 네이비 상자 | 노랑 상자 (글자 전체 높이, 유일한 강조) |
| 결과 | 잠 -200시간 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Softly blurred bright afternoon office background in warm cream and grey tones, afternoon sunlight through a window.
On the left 45% of the frame, a fictional Korean woman in her mid-thirties, office worker (neat blouse or knit top, plain lanyard with no text), sitting at her desk in front of a monitor, chin resting on her hand, eyes closed, head drooping as she dozes off; tired, drained, slightly regretful expression.
On the desk, a few empty plain paper coffee cups with no logos; the monitor screen is blurred with nothing readable.
Fictional person, not resembling any real or famous person, natural Korean features, realistic photo style. Not a doctor, no hospital, no pills, no crying, no collapse.
On the right side, upper headline "100일째, 무너졌다": the part "100일째" in ink-black letters on a solid bright yellow (#FFD400) box covering the full letter height, and the part ", 무너졌다" in white letters on a dark navy (#14213D) box.
Below it, a wide solid red (#E63B2E) rounded box with the huge white bold text "잠 -200시간", the largest element.
Keep the face and all text inside the central 16:9 safe area. No app screens, no phone interfaces, no brain imagery.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (새벽 5시의 나 vs 오후의 나)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 같은 사람의 **새벽(기대)과 오후(결과)를 나란히** 보여 주면, 문제 분석 첫 번째 메시지("아침 2시간은 잠에서 빌린 시간")가 한눈에 전해진다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 시계 | 05:00 | 잉크 #1E1E1E (노랑 시계 화면 위) | 노랑 #FFD400 (유일한 강조) |
| 왼쪽 | 인증 100일 | 잉크 #1E1E1E 글자 (크림 #F2EBDD 상자) | — |
| 오른쪽 | 잠 -200시간 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Split-screen comparison divided vertically in the middle by a thin cream line. Realistic photo style. The SAME fictional Korean woman in her mid-thirties, office worker, appears on both sides.
LEFT HALF (expectation): before sunrise, the window behind is deep navy (#14213D); a desk lit by a warm desk lamp, an open book and a plain notebook with no readable writing, and a simple generic digital alarm clock (no brand) whose display is a bright yellow (#FFD400) panel showing ink-black digits "05:00". The woman sits upright, motivated, reading. At the bottom of the left half, a solid cream (#F2EBDD) box with ink-black bold text "인증 100일".
RIGHT HALF (result): a bright afternoon office; the same woman dozing at her desk in front of a blurred monitor, chin on her hand, eyes closed, tired and drained expression. In the lower-middle of the right half (not in the bottom-right corner), a solid red (#E63B2E) box with huge white bold text "잠 -200시간", larger than the left label.
Fictional person, not resembling any real or famous person, natural Korean features. No doctor, no hospital, no pills, no crying. No phone screens, no app interfaces, no book covers with titles, no brain imagery. Keep faces and text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
잠드는 시간은 자정 그대로 두고 알람만 새벽 5시로 당겼더니, 100일 만에 줄어든 잠이 200시간이었습니다.
잠을 줄인 새벽 기상이 왜 문제인지 4가지로, 잠을 지키면서 아침 시간을 만드는 방법을 5가지로 정리했습니다.

■ 이 영상에서 다루는 것
- 아침 2시간은 번 시간이 아니라 잠에서 빌린 시간 (권장 수면 7시간 이상, 2025 지역사회건강조사)
- 줄인 잠의 대가는 졸음만이 아니다 (잠을 줄인 6주 실험)
- 새벽 기상 자체가 성공 비결은 아니다 (아침형·저녁형 유전 연구, 영국 2만 6천여 명 인지 검사)
- 주말에 몰아 자면 된다는 생각의 함정 (영국 6만여 명 수면 규칙성 연구)
- 잠을 지키는 5가지: 잠드는 시간부터, 2주마다 15분씩, 아침 루틴은 30분부터, 저녁형이면 퇴근 후 30분, 2주마다 몸의 신호 점검

■ 챕터
0:00 사연: 새벽 5시 100일, 잃은 잠 200시간
1:33 왜 잠부터 줄일까
2:38 문제 01 아침 2시간은 잠에서 빌린 시간
3:34 문제 02 줄인 잠의 대가는 졸음만이 아니다
4:33 문제 03 새벽 기상이 성공 비결은 아니다
5:37 문제 04 주말 몰아 자기의 함정
6:36 첫째: 일어나는 시간보다 잠드는 시간부터
7:56 둘째: 2주마다 15분씩, 주말도 같은 시간
8:38 셋째: 아침 루틴은 30분부터
9:12 넷째: 저녁형이면 퇴근 후 30분
9:49 다섯째: 2주마다 몸의 신호 점검
10:20 새벽 기상을 해도 되는 기준
10:43 정리

■ 사연에 대해
이 영상의 사연은 실제 연구와 통계를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 숫자는 이해를 돕기 위한 예시입니다.

■ 출처
- 통계청 2024년 생활시간조사 (2025.7.28 발표, 취침·기상 시각, 잠 못 이룸): https://www.newsis.com/view/NISX20250728_0003268438
- 미국수면의학회·수면연구학회 성인 권장 수면 시간 합의문 (Watson 외, SLEEP 2015): https://pmc.ncbi.nlm.nih.gov/articles/PMC4434546/
- 질병관리청 2025 지역사회건강조사 우울증상 관련요인 분석 (2026.4.15): https://kdca.go.kr/bbs/kdca/42/310745/artclView.do
- 잠을 줄인 6주 실험 (Zuraikat 외, Diabetes Care 2024): https://doi.org/10.2337/dc23-1156
- 같은 실험 미국 국립심장폐혈액연구소 소개: https://www.nhlbi.nih.gov/news/2023/chronic-sleep-deficiency-increases-insulin-resistance-women-especially-postmenopausal
- 아침형 유전 연구 (Jones 외, Nature Communications 2019): https://doi.org/10.1038/s41467-018-08259-7
- 잠의 길이·아침형과 인지 (West 외, BMJ Public Health 2024): https://doi.org/10.1136/bmjph-2024-001000
- 수면 규칙성과 사망 위험 (Windred 외, SLEEP 2024): https://doi.org/10.1093/sleep/zsad253
- 잠을 늘린 실험 (Tasali 외, JAMA Internal Medicine 2022): https://doi.org/10.1001/jamainternmed.2021.8098

■ 정보 제공용 영상입니다
이 영상은 자기계발 정보 제공을 위한 것이며, 의사나 상담 전문가의 진단을 대신하지 않습니다.
사연은 실제 연구와 통계를 바탕으로 재구성한 이야기이고, 사연 속 숫자는 이해를 돕기 위한 예시입니다.
같은 방법도 사람마다 효과가 다르니, 수면·건강·마음의 문제가 계속되면 전문가와 상담하세요.
영상 속 연구와 통계의 출처는 설명란에 있습니다.

#자기계발 #미라클모닝 #수면
```

**태그**: 새벽 기상, 아침 루틴, 아침 루틴 만들기, 수면 시간, 적정 수면 시간, 수면 부족, 아침형 인간, 미라클모닝, 미라클모닝 방법, 미라클모닝 부작용, 자기계발, 동기부여, 갓생, 30대 자기계발, 수면 연구

**고정 댓글**

```
새벽 기상을 시작하기 전에 이 두 가지부터 정해 보세요.
1. 잠드는 시간 (일어날 시각에서 7시간을 뺀 시각)
2. 2주마다 볼 몸의 신호 (오후 졸음, 커피 잔 수, 주말 늦잠)

새벽 기상을 오래 이어 간 적이 있나요? 그때는 무엇이 달랐는지 나눠 주세요.
※ 이 영상은 정보 제공용이며 진단이나 상담을 대신하지 않습니다. 잠·마음의 어려움이 계속되면 전문가와 상담해 주세요. 강의·제품 홍보 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 새해 첫 월요일인 2026년 1월 5일, 저는 알람을 새벽 5시로 바꿨어요.
2. 100일 동안 매일 인증하는 미라클모닝 챌린지였죠.
3. 저는 서른넷, 야근이 잦은 직장인이에요.
4. 퇴근하면 녹초가 돼서 제 시간은 하나도 없었죠.
5. 그래서 잠드는 시간은 자정 그대로 두고, 알람만 7시에서 5시로 당겼어요.
6. 그렇게 생긴 아침 2시간에 영어 30분, 운동 30분, 책 한 시간을 넣었죠.
7. 한 달 만에 책 두 권을 읽었고, 하루가 2시간 늘어난 기분이었어요.
8. 인증 글에 칭찬 댓글이 달리니까 주말에도 5시에 일어났죠.
9. 하지만 그 2시간은 공짜가 아니었습니다.
10. 100일째인 4월 14일, 처음으로 그동안의 잠을 계산해 봤어요.
11. 하루 2시간씩 100일, 줄어든 잠이 모두 200시간이었어요.
12. 꼬박 8일 하고도 8시간을 못 잔 셈이었죠.
13. 바로 그날 오후 회의에서 저는 꾸벅꾸벅 졸았어요.
14. 제가 만든 보고서에 숫자가 틀렸다는 지적까지 받았고요.
15. 돌아보니 저는 일어나는 시간만 당기고 잠드는 시간은 그대로 뒀더라고요.
16. 하루 한 잔이던 커피는 네 잔으로 늘었고, 오후 3시면 모니터 앞에서 고개가 떨어졌어요.
17. 그 2시간은 제가 번 시간이 아니라, 제 잠에서 몰래 빌려 쓴 시간이었어요.
18. 새벽 인증 사진 100장을 얻은 대신, 오후의 저를 100일 동안 잃어버렸네요.

**진행자 파트** — 🎙 진행자

19. 시간에 쫓기다 보면 많은 분들이 이런 생각을 하죠.
20. 남들보다 두 시간만 먼저 일어나면 인생이 달라질 거야.
21. 모자란 잠은 주말에 몰아서 자면 되잖아.
22. 성공한 사람들은 다 새벽에 일어난다던데.
23. 이런 식으로 아침 시간을 만들려고 잠부터 줄이는 경우가 많습니다.
24. 2024년 생활시간조사에서 우리나라 사람들의 평균 취침 시각은 밤 11시 28분이었습니다.
25. 평균 기상 시각은 아침 6시 59분이었고요.
26. 여기서 알람만 두 시간 당기면, 잠자리에 있는 시간은 5시간 반 남짓이 됩니다.
27. 잠을 이루지 못했다고 답한 사람도 11.9%로, 5년 전 7.3%보다 늘었습니다.
28. 사연자의 이야기가 남의 일이 아닌 이유입니다.
29. 그렇다면 잠을 줄인 새벽 기상은 무엇이 문제였을까요?

> 🟨 [장면] 정보 제공용 영상입니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 자기계발 정보 제공을 위한 것이며, 의사나 상담 전문가의 진단을 대신하지 않습니다.
> 사연은 실제 연구와 통계를 바탕으로 재구성한 이야기이고, 사연 속 숫자는 이해를 돕기 위한 예시입니다.
> 같은 방법도 사람마다 효과가 다르니, 수면·건강·마음의 문제가 계속되면 전문가와 상담하세요.
> 영상 속 연구와 통계의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

30. 첫 번째 문제는 아침 2시간이 번 시간이 아니라 잠에서 빌린 시간이라는 것입니다.
31. 미국 수면의학회와 수면연구학회는 성인에게 하룻밤 7시간 이상의 잠을 권고합니다.
32. 그것도 어쩌다 한 번이 아니라 규칙적으로 자야 한다고 했죠.
33. 자정에 자고 5시에 일어난 사연자의 잠은 5시간, 권고보다 매일 2시간이 모자랐습니다.
34. 국내 자료도 있습니다.
35. 2025년 지역사회건강조사에서 질병관리청이 성인 약 23만 명을 분석했습니다.
36. 기준은 하루 7시간에서 8시간 자는 사람들이었습니다.
37. 6시간 이하나 9시간 이상 자는 사람은 우울증상을 보일 가능성이 2.1배 높았습니다.
38. 잠이 원인이라고 단정할 수는 없지만, 적당한 잠과 마음 건강이 함께 간다는 뜻입니다.
39. 두 번째는 잠을 줄인 대가가 졸음으로만 끝나지 않는다는 것입니다.
40. 미국 컬럼비아대 연구팀은 평소 7시간에서 9시간을 자던 여성들로 실험을 했습니다.
41. 6주 동안은 잠자리에 드는 시간을 1시간 반씩 늦추게 했죠.
42. 같은 사람이 6주는 평소대로, 6주는 잠을 줄여 지내고 두 기간을 비교했습니다.
43. 실제로 줄어든 잠은 하룻밤 평균 1시간 20분 정도였습니다.
44. 그런데도 혈당을 낮추는 호르몬인 인슐린이 잘 듣지 않는 정도가 15% 가까이 높아졌습니다.
45. 다시 평소처럼 7시간에서 9시간을 자자, 이 수치는 원래대로 돌아왔다고 합니다.
46. 여성 수십 명의 작은 실험이지만, 사연자는 이보다 더 많이, 더 오래 잠을 줄였죠.
47. 그 몸이 어땠는지는 알 수 없지만, 줄인 잠은 몸에도 흔적을 남길 수 있다는 겁니다.
48. 세 번째는 새벽 기상 자체가 성공의 비결은 아니라는 것입니다.
49. 아침형인지 저녁형인지에는 타고난 부분이 있습니다.
50. 2019년에는 약 70만 명의 유전 정보를 분석한 연구가 나왔습니다.
51. 아침형 성향과 관련된 유전자 자리가 351곳이나 발견됐죠.
52. 2024년 영국 연구는 53세에서 86세 성인 2만 6천여 명을 분석했습니다.
53. 잠의 길이와 아침형인지 저녁형인지를 인지 검사 점수와 비교했죠.
54. 그 결과 아침형보다 저녁형과 중간형의 점수가 높았습니다.
55. 잠은 7시간에서 9시간을 잔 사람들의 점수가 가장 좋았고요.
56. 한 시점에 비교한 연구라 저녁형이 더 낫다는 뜻은 아닙니다.
57. 다만 아침형만 정답은 아니고, 몇 시에 일어나느냐보다 얼마나 자느냐가 중요하다는 거죠.
58. 자정이 돼야 졸린 사연자가 5시에 일어난 건, 타고난 몸 시계를 억지로 거스른 셈입니다.
59. 네 번째는 모자란 잠을 주말에 몰아서 자면 된다는 생각에도 함정이 있다는 것입니다.
60. 2024년 연구에서 영국 성인 6만여 명이 손목 활동 측정기로 잠자는 시간을 기록했습니다.
61. 잠자는 시간이 가장 들쭉날쭉한 그룹과 나머지 그룹을 비교했습니다.
62. 나머지 그룹은 사망 위험이 20에서 48% 낮았습니다.
63. 연구진은 잠의 규칙성이 잠의 길이보다 사망 위험을 더 잘 예측했다고 밝혔습니다.
64. 관찰 연구라 원인을 단정할 수는 없지만, 잠은 양만큼 일정함도 중요하다는 뜻이죠.
65. 평일에 줄이고 주말에 몰아 자면, 잠의 양도 일정함도 함께 흔들리게 됩니다.
66. 사연자는 주말에도 5시에 일어나 일정함은 지켰지만, 정작 잠의 양이 모자랐던 겁니다.
67. 그렇다면 잠을 지키면서 아침 시간을 만들려면 어떻게 해야 할까요?

**올바른 방법 파트** — 🎙 진행자

68. 첫째, 일어나는 시간이 아니라 잠드는 시간부터 정하는 것입니다.
69. 7시간을 자려면 5시에 일어나는 사람은 밤 10시에는 잠들어야 합니다.
70. 자정이 돼야 잠드는 사연자라면 7시 기상이 맞는 시간이었죠.
71. 그래서 기상 알람보다 먼저, 잠자리에 드는 알람을 맞춰 보세요.
72. 잠드는 시간을 당기는 건 생각보다 해 볼 만합니다.
73. 2022년 미국 시카고대 연구에는 평소 6시간 반도 못 자던 성인 80명이 참여했습니다.
74. 21세에서 40세의 과체중 성인들이었고, 무작위로 두 그룹으로 나눴죠.
75. 한 그룹만 잠 상담을 한 번 받고, 자기 집에서 평소처럼 생활하며 잠을 늘렸습니다.
76. 그러자 잠이 하룻밤 평균 1시간 12분 늘었습니다.
77. 식단 지시가 없었는데도 이 그룹은 다른 그룹보다 하루 평균 270킬로칼로리를 덜 먹었죠.
78. 연구진은 잠들기 전 전자기기 사용을 줄인 것이 핵심으로 보였다고 했습니다.
79. 2주 동안 지켜본 짧은 실험이지만, 잠은 생활 속에서도 늘릴 수 있다는 걸 보여 줍니다.
80. 기준은 하나입니다.
81. 잠드는 시간을 당기지 못했다면, 일어나는 시간도 당기지 않는 겁니다.
82. 둘째, 한 번에 2시간이 아니라 15분씩, 주말에도 같은 시간에 일어나는 것입니다.
83. 자정에 자고 7시에 일어나던 사연자라면, 2주마다 둘 다 15분씩 당겨 보세요.
84. 그러면 8주 뒤에는 밤 11시에 자고 아침 6시에 일어나게 됩니다.
85. 7시간을 지키면서도 아침 1시간이 생기는 거죠.
86. 15분은 연구로 정해진 숫자가 아니라, 몸이 따라오기 쉽게 잘게 나눈 예시입니다.
87. 그리고 앞에서 본 것처럼 잠은 일정함도 중요합니다.
88. 예를 들어 주말에도 평일과 일어나는 시간이 1시간 넘게 벌어지지 않게 해 보세요.
89. 셋째, 아침 루틴은 2시간이 아니라 30분부터 시작하는 것입니다.
90. 사연자는 영어, 운동, 독서를 한꺼번에 넣느라 2시간이 필요했죠.
91. 하나만 골라 30분이면, 6시 30분 기상으로 충분합니다.
92. 그러면 밤 11시 30분에만 잠들어도 7시간을 잘 수 있죠.
93. 30분이 익숙해지고 7시간도 지켜질 때, 그다음 15분을 더하면 됩니다.
94. 기준은 7시간을 지킬 수 있는 만큼만 일찍 일어나는 것입니다.
95. 넷째, 저녁형이라면 아침 대신 퇴근 후 30분을 쓰는 것입니다.
96. 앞에서 봤듯이 아침형과 저녁형에는 타고난 부분이 있습니다.
97. 밤 11시 전에는 도무지 졸리지 않는 사람도 있죠.
98. 그렇다면 억지로 새벽에 일어나기보다 할 일을 저녁으로 옮기는 편이 낫습니다.
99. 사연자라면 자정에 자고 7시에 일어나는 생활은 그대로 둡니다.
100. 대신 밤 10시부터 30분만 영어 공부를 하는 식이죠.
101. 중요한 건 알람 시각이 아니라, 매일 같은 시간에 꾸준히 하는 것입니다.
102. 다섯째, 2주마다 몸의 신호로 점검하는 것입니다.
103. 볼 것은 세 가지입니다.
104. 오후에 졸음이 쏟아지는지, 커피 잔 수가 늘었는지, 주말 늦잠이 길어졌는지요.
105. 하나라도 나빠졌다면 일어나는 시간을 15분 늦추면 됩니다.
106. 사연자였다면 커피가 네 잔으로 늘기 전, 첫 점검에서 멈출 수 있었을 겁니다.
107. 잠자리에 일찍 누워도 잠들지 못하는 날이 계속되면, 전문가와 상담하세요.
108. 물론 새벽 기상 자체가 나쁜 건 아닙니다.
109. 7시간 이상 자고, 주말에도 같은 시간에 일어나는지 보세요.
110. 그러고도 2주 동안 오후 졸음이 없다면 새벽 기상은 좋은 방법입니다.
111. 새벽 기상으로 하루가 달라진 사람들과 사연자의 차이는 하나였습니다.
112. 일찍 잠들었느냐, 잠을 줄였느냐였죠.

**마무리** — 🎙 진행자

113. 이렇게 해서 잠을 줄인 새벽 기상이 왜 문제인지와 다섯 가지 방법을 알아보았습니다.
114. 내일 알람을 바꾸기 전에, 오늘 밤 잠드는 시간부터 정해 보세요.
115. 원하는 변화를 꼭 이루셨으면 좋겠습니다.
116. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
