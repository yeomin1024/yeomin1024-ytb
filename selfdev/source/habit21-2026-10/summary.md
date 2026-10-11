# habit21-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py selfdev habit21-2026-10` (2026-10-11 08:41). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **21일만 버티면 습관이 된다길래 꼬박 채웠는데 사흘 만에 0일이 됐습니다. 작심삼일 반복하는 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 105 / 자막 138, 길이 10:37 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–16 · 진행자 17–105 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/habit21-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 21일만 버티면 습관이 된다길래 꼬박 채웠는데 사흘 만에 0일이 됐습니다. 작심삼일 반복하는 사람들의 공통점 `속마음 · 21일→0일 · 공통점` 60자 — 짝 썸네일: thumbnail_1 (달력 숫자 반전)
- [ ] **T2.** 22일째 하루쯤 괜찮다며 알람을 껐더니 21일 기록이 0일이 됐습니다. 21일만 믿은 사람들의 최악의 결말 `장면 · 21일→0일 · 최악의 결말` 59자 — 짝 썸네일: thumbnail_2 (인물·감정)
- [ ] **T3.** (짧은 변형) 21일 챌린지 꼬박 채우고 사흘 만에 0일. 작심삼일의 불편한 진실 `행동 · 21일→0일 · 불편한 진실` 37자 — 짝 썸네일: thumbnail_3 (검은 배경 제목형 — 채택 제목 문구)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (달력 기록 카드)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 동그라미 21개가 꽉 찬 달력이 **"0일"**로 뒤집히는 숫자 반전이 가장 클릭을 부른다 (시청자가 아는 "21일"을 노랑으로 강조)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 문구 (시작) | 21일 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (노랑 상자 1곳) |
| 핵심 숫자 (결과) | 0일 | 빨강 #E63B2E (잃은 것) | 가장 큰 글자 |
| 하단 1줄 (11자) | 21일 꼬박 채웠는데 | 흰색 + 두꺼운 검정 외곽선 | — |
| 하단 2줄 (12자) | 사흘 만에 0일이 됐다 | 흰색 + 두꺼운 검정 외곽선 | "0일"만 빨강 #E63B2E (무너진 결과) |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain.
Upper 60% of the frame: on the left half, a single sheet of a simple paper wall calendar with a plain grid of boxes (date numbers very faint and blurred, no month name, no brand, no printed words). The first 21 boxes, the top three rows, each have a hand-drawn ink-black circle; all the remaining boxes are empty. Above the calendar, a solid bright yellow (#FFD400) box with the large ink-black bold text "21일". On the right 40%, a thick ink-black arrow points from the calendar to a huge red (#E63B2E) bold text "0일", the largest element in the image, about 30% of the image height.
Bottom title: in the lower third, over a dark navy (#14213D) band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "21일 꼬박 채웠는데", line 2 "사흘 만에 0일이 됐다". The word "0일" in line 2 is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
No people, no faces, no apps, no phones. Minimal, nothing decorative. Keep all text and the calendar inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (22일째 아침)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 말아 둔 운동 매트 앞에서 허탈해하는 **30대 여성 직장인의 표정**이 숫자 카드보다 "내 얘기다"를 더 끈다 (성공 썸네일 대부분이 감정이 드러난 얼굴 — 주식 결과 임시 근거)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 핵심 숫자 | 22일째 | 잉크 #1E1E1E | 노랑 상자 #FFD400 (글자 전체 높이, 노랑 상자 1곳) — 위쪽에서 가장 큰 글자 |
| 하단 1줄 (11자) | 하루쯤 알람을 껐더니 | 흰색 + 두꺼운 검정 외곽선 | — |
| 하단 2줄 (14자) | 21일 기록이 0일이 됐다 | 흰색 + 두꺼운 검정 외곽선 | "0일"만 빨강 #E63B2E (무너진 결과) |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, regained blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A dim, dark navy-toned living room in the early morning, faint pale light through a window.
Upper 60% of the frame: on the left 45%, a fictional Korean woman in her mid 30s, office-worker look, wearing a plain sweatshirt before work, sitting on the living-room floor and staring with a tired, deflated, regretful expression at a rolled-up exercise mat standing against the wall next to her. She loosely holds a smartphone with its screen turned off. Her face and the mat stay in the upper 60% of the frame.
Fictional person, not resembling any real or famous person, natural Korean features. No crying, no extreme emotion.
On the upper right, a solid bright yellow (#FFD400) box covering the full letter height with the huge black bold text "22일째", the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "하루쯤 알람을 껐더니", line 2 "21일 기록이 0일이 됐다". The word "0일" in line 2 is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 safe area. No brand logos on the mat, no app screens.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 검은 배경 제목형 (채택 제목 문구)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 그림 없이 **검은 배경의 채택 제목 문구(글자)만으로** 클릭을 부르는지 — 사진 썸네일 사이에서 오히려 눈에 띄는지

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 (8자) | 21일만 버티면 | 흰색 #FFFFFF | "21일"만 노랑 #FFD400 (처음 목표 숫자) |
| 2줄 (8자) | 습관이 된다길래 | 흰색 #FFFFFF | — |
| 3줄 (7자) | 꼬박 채웠는데 | 흰색 #FFFFFF | — |
| 4줄 (14자) | 사흘 만에 0일이 됐습니다 | 흰색 #FFFFFF | "0일"만 빨강 #E63B2E (무너진 결과) |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "21일만 버티면", line 2 "습관이 된다길래", line 3 "꼬박 채웠는데", line 4 "사흘 만에 0일이 됐습니다".
All text pure white (#FFFFFF) except "21일" in bright yellow (#FFD400) and "0일" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
21일 홈트 챌린지를 하루도 빠짐없이 채웠는데, 22일째 하루 쉰 뒤 사흘 만에 연속 기록이 0일이 됐습니다.
작심삼일이 반복되는 이유 4가지와, 21일을 진짜 습관으로 이어 가는 방법 6가지를 연구로 정리했습니다.

■ 이 영상에서 다루는 것
- 21일은 연구로 확인된 숫자가 아니다 (연구 20개 분석: 중간값 59~66일, 사람에 따라 4~335일)
- 운동 습관은 특히 오래 걸린다 (헬스장 출입 기록 분석: 68~78일, 두세 달)
- 빠진 날보다 빠진 다음 날이 문제다 (한 번 빠진 건 큰 영향 없음, 끊긴 연속 기록의 영향)
- 바쁜 날의 계획이 없었다 (실행 의도 실험 642개 분석)
- 방법 6가지: 석 달 목표, 날짜 대신 '저절로 되는지' 확인, 최소 버전, 언제·어디서 한 문장과 만약 계획, 두 번 연속 빠지지 않기와 작은 보상, 연속 일수 대신 한 날 수

■ 챕터
0:00 사연: 21일 채웠는데 사흘 만에 0일
1:29 왜 21일만 채우고 멈출까
2:43 문제 01 21일은 연구로 확인된 숫자가 아니다
3:55 문제 02 운동 습관은 두세 달이 걸린다
4:37 문제 03 빠진 날보다 빠진 다음 날
5:38 문제 04 바쁜 날의 계획이 없었다
6:33 첫째: 목표 기간은 석 달
7:03 둘째: 날짜 대신 저절로 되는지 확인
7:35 셋째: 바쁜 날의 최소 버전
8:06 넷째: 언제·어디서 한 문장과 만약 계획
8:44 다섯째: 두 번 연속 빠지지 않기
9:25 여섯째: 연속 일수 대신 한 날 수
9:54 21일 챌린지를 해도 되는 때
10:13 정리

■ 사연에 대해
이 영상의 사연은 실제 연구와 통계를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 숫자는 이해를 돕기 위한 예시입니다.

■ 출처
- 습관이 되는 기간 체계적 문헌고찰 (Singh 외, Healthcare 2024): https://doi.org/10.3390/healthcare12232488
- 헬스장·손 씻기 습관 연구 (Buyalskaya 외, PNAS 2023): https://doi.org/10.1073/pnas.2216115120
- 위 연구의 정정 (PNAS 2023, 헬스장 습관 68~78일): https://doi.org/10.1073/pnas.2312763120
- 위 연구 보도자료 "No magic number for time it takes to form habits" (2023): https://www.eurekalert.org/news-releases/986381
- 헬스장 회원 6만 1천여 명 대상 4주 프로그램 54가지 실험 (Milkman 외, Nature 2021): https://doi.org/10.1038/s41586-021-04128-4
- 한 번 빠져도 습관 형성에 큰 영향 없음 (Lally 외, European Journal of Social Psychology 2010): https://doi.org/10.1002/ejsp.674
- 끊긴 연속 기록의 영향 (Silverman·Barasch, Journal of Consumer Research 2023): https://doi.org/10.1093/jcr/ucac029
- 실행 의도 실험 642개 메타분석 (Sheeran·Listrom·Gollwitzer, European Review of Social Psychology 2025, 온라인 2024): https://doi.org/10.1080/10463283.2024.2334563

■ 정보 제공용 영상입니다
이 영상은 자기계발 정보 제공을 위한 것이며, 의사나 상담 전문가의 진단을 대신하지 않습니다.
사연은 실제 연구와 통계를 바탕으로 재구성한 이야기이고, 사연 속 숫자는 이해를 돕기 위한 예시입니다.
같은 방법도 사람마다 효과가 다르니, 수면·건강·마음의 문제가 계속되면 전문가와 상담하세요.
영상 속 연구와 통계의 출처는 설명란에 있습니다.

#자기계발 #작심삼일 #습관만들기
```

**태그**: 작심삼일, 작심삼일 극복, 습관 만들기, 좋은 습관 만들기, 21일 습관, 66일 습관, 21일 챌린지, 운동 습관, 홈트 습관, 습관 형성, 자기계발, 동기부여, 30대 자기계발, 직장인 자기계발, 습관 연구

**고정 댓글**

```
새 습관을 시작할 때 이 두 가지만 먼저 적어 보세요.
1. 목표 기간은 21일이 아니라 석 달 (1월 1일 시작이면 3월 31일까지)
2. 바쁜 날의 최소 버전 한 줄 (예: 야근한 날은 매트 위 5분 스트레칭)

여러분은 21일 넘게 이어진 습관이 있나요? 그때는 무엇이 달랐는지 댓글로 나눠 주세요.
※ 이 영상은 정보 제공용이며 진단이나 상담을 대신하지 않습니다. 잠·마음의 어려움이 계속되면 전문가와 상담해 주세요. 강의·제품 홍보 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 2026년 1월 1일, 저는 거실 달력에 21칸을 그렸어요.
2. 21일만 버티면 습관이 된다는 영상을 보고 홈트 챌린지를 시작한 거죠.
3. 저는 서른여섯, 하루 종일 사무실 의자에 앉아 있는 직장인이에요.
4. 운동은 늘 작심삼일이었지만, 21일이면 끝난다니 이번엔 될 것 같았어요.
5. 매일 아침 7시, 거실 매트 위에서 30분씩 운동했어요.
6. 21일 동안 하루도 빠지지 않았고, 달력에는 동그라미 21개가 생겼죠.
7. 회사 계단을 올라도 숨이 덜 찼고, 이제 습관이 됐다고 믿었어요.
8. 그런데 진짜 시험은 22일째부터였습니다.
9. 1월 22일 아침, 습관이 됐으니 하루쯤은 괜찮겠다며 알람을 껐어요.
10. 다음 날은 야근, 그다음 날은 늦잠이었죠.
11. 그렇게 딱 사흘 만에 21일이던 연속 기록이 0일이 됐어요.
12. 다시 1일부터 세야 한다는 생각에 매트는 그대로 말려 있었어요.
13. 4월 1일과 7월 1일에도 똑같이 21일을 채우고, 똑같이 무너졌어요.
14. 21일을 채우면 끝인 줄 알았지, 그다음 계획은 하나도 없었던 거예요.
15. 동그라미를 63개나 그렸는데, 제 몸에 남은 습관은 하나도 없어요.
16. 21일을 결승선으로 착각한 바람에 세 번이나 출발선으로 돌아온 셈이에요.

**진행자 파트** — 🎙 진행자

17. 새해나 월초가 되면 많은 분들이 이런 생각을 하죠.
18. 21일만 버티면 그다음엔 저절로 되겠지.
19. 하루 빠졌으니 이번에도 망했어.
20. 이번 달은 바쁘니까 다음 달 1일부터 다시 하자.
21. 이런 식으로 기간을 정해 놓고, 그 기간이 끝나면 손을 놓는 경우가 많습니다.
22. 2021년에 발표된 미국의 대규모 실험이 이 모습을 잘 보여 줍니다.
23. 헬스장 체인 회원 6만 1천여 명을, 4주짜리 운동 프로그램 54가지에 무작위로 나눴죠.
24. 그중 절반 가까이는 프로그램 기간 동안 헬스장 방문을 9~27% 늘렸습니다.
25. 그런데 4주가 끝난 뒤에도 효과가 남은 프로그램은 8%뿐이었습니다.
26. 정해진 기간 안에서는 잘 되다가, 기간이 끝나면 대부분 원래대로 돌아간 거죠.
27. 사연 속 21일 챌린지가 남의 이야기가 아닌 이유입니다.
28. 그럼 21일 챌린지가 왜 습관으로 이어지지 않았는지 하나씩 짚어 보겠습니다.

> 🟨 [장면] 정보 제공용 영상입니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 자기계발 정보 제공을 위한 것이며, 의사나 상담 전문가의 진단을 대신하지 않습니다.
> 사연은 실제 연구와 통계를 바탕으로 재구성한 이야기이고, 사연 속 숫자는 이해를 돕기 위한 예시입니다.
> 같은 방법도 사람마다 효과가 다르니, 수면·건강·마음의 문제가 계속되면 전문가와 상담하세요.
> 영상 속 연구와 통계의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

29. 첫 번째 문제는 21일이 연구로 확인된 숫자가 아니라는 것입니다.
30. 2024년 호주 연구진이 습관 연구 20개, 2,601명의 자료를 모아 분석했습니다.
31. 습관이 되기까지 걸린 기간은 중간값으로 59일에서 66일이었습니다.
32. 중간값은 걸린 기간 순서로 사람들을 줄 세웠을 때 한가운데 사람의 값입니다.
33. 평균으로 보면 106일에서 154일로, 오래 걸린 사람들 때문에 더 길어졌고요.
34. 사람에 따라서는 4일 만에 된 경우도, 335일이 걸린 경우도 있었습니다.
35. 그러니 21일 만에 습관이 된 사람이 있다고 해서, 그게 내 기준이 될 수는 없습니다.
36. 흔히 말하는 66일도 여러 사람의 중간값일 뿐, 누구에게나 맞는 숫자는 아닙니다.
37. 다만 기간까지 보고한 연구는 4개뿐이라 정확한 숫자로 외울 필요는 없습니다.
38. 두 달은 넘게 걸리고, 사람마다 크게 다르다는 것만 기억하면 됩니다.
39. 사연자의 21일은 그 중간값의 3분의 1 남짓에서 멈춘 셈이죠.
40. 두 번째는 운동이 그중에서도 시간이 더 걸리는 습관이라는 것입니다.
41. 2023년 한 연구는 4년 치 헬스장 출입 기록으로, 이용자 3만 110명을 살펴봤습니다.
42. 병원 직원들이 손을 씻는 기록도 함께 인공지능 기법으로 분석했죠.
43. 손 씻기는 몇 주 만에 습관이 됐습니다.
44. 하지만 헬스장에 가는 습관은 68일에서 78일, 두세 달 정도가 걸렸습니다.
45. 연구진은 습관이 되는 마법의 숫자 같은 건 없다고 정리했습니다.
46. 사연자가 습관이 됐다고 믿은 21일은 이 기준의 3분의 1도 안 되는 시점이었던 거죠.
47. 세 번째는 하루 빠진 게 아니라, 빠진 다음에 돌아가지 않은 게 문제라는 것입니다.
48. 2010년 영국 연구진이 96명에게 12주 동안 새 습관을 매일 하게 한 실험이 있습니다.
49. 여기서 한 번 빠진 것은, 습관이 만들어지는 과정에 큰 영향을 주지 않았습니다.
50. 문제는 빠진 하루보다, 그 하루 때문에 0이 된 기록일 수 있습니다.
51. 2023년 한 소비자 심리 연구는 실험 일곱 개로 연속 기록의 힘을 살펴봤습니다.
52. 기록이 이어지고 있다는 표시를 본 사람들은 그 행동을 더 이어 갔습니다.
53. 반대로 기록이 끊겼다는 표시를 본 사람들은 덜 이어 갔죠.
54. 끊긴 이유를 남이 아니라 자기 탓으로 돌릴 때 그 차이가 더 커졌습니다.
55. 사연자도 스스로 알람을 끈 날 기록이 끊겼고, 0일이 된 달력 앞에서 멈췄습니다.
56. 하루 빠진 날보다 빠진 다음 날이 진짜 승부처였던 겁니다.
57. 네 번째는 계획이 잘 풀리는 날에만 맞춰져 있었다는 것입니다.
58. 사연자의 계획은 매일 아침 7시, 거실 매트에서 30분, 이것 하나였어요.
59. 야근한 다음 날이나 늦잠 잔 날에는 무엇을 할지 정해 둔 게 없었죠.
60. 2024년 미국과 독일 연구진이 실행 의도 실험 642개를 모아 분석했습니다.
61. 실행 의도는 언제, 어디서, 어떻게 하겠다고 미리 정해 두는 계획입니다.
62. 이 계획은 행동뿐 아니라 생각과 감정을 다스리는 데도 효과가 있었습니다.
63. 특히 만약 이런 일이 생기면 이렇게 한다는 식으로, 조건을 붙인 계획에서 효과가 더 컸죠.
64. 바쁜 날의 계획이 없으면, 다음 달 1일만 기다리게 되는 겁니다.
65. 그렇다면 21일 챌린지를 진짜 습관으로 이어 가려면 어떻게 해야 할까요?

**올바른 방법 파트** — 🎙 진행자

66. 첫째, 목표 기간을 21일이 아니라 석 달로 잡는 것입니다.
67. 1월 1일에 시작했다면 3월 31일까지, 달력 석 장에 90일을 그리는 거죠.
68. 앞에서 본 헬스장 연구의 68일에서 78일보다 열흘 넘게 여유가 있는 기간입니다.
69. 물론 사람에 따라 석 달보다 더 걸릴 수도 있습니다.
70. 그래서 석 달째 되는 날은, 졸업 날이 아니라 점검하는 날로 정해 둡니다.
71. 둘째, 습관이 됐는지는 날짜가 아니라 저절로 되는지로 확인하는 것입니다.
72. 습관 연구들은 며칠을 했는지보다, 생각하지 않아도 하게 되는지를 물어서 습관을 잽니다.
73. 예를 들어 아침에 매트를 펼지 말지, 이제는 고민하지 않는지 물어보는 겁니다.
74. 알람이 울리기 전에 몸이 먼저 매트로 가는지도 함께 보면 좋습니다.
75. 아직 아니라면 날짜가 지났더라도 계획과 기록을 그대로 이어 가면 됩니다.
76. 셋째, 바쁜 날에 할 최소 버전을 미리 정해 두는 것입니다.
77. 30분 홈트가 기본이라면, 야근한 날은 매트 위 5분 스트레칭만 하는 겁니다.
78. 사연자가 22일째 아침에 알람을 끄는 대신 5분만 했다면, 기록은 이어졌을 거예요.
79. 영국의 12주 실험에서도 꾸준히 한 사람일수록 습관이 자리 잡는 모습이 뚜렷했습니다.
80. 최소 버전은 너무 쉬워서 웃음이 날 만큼 작게 정하는 게 좋습니다.
81. 넷째, 언제·어디서·무엇을 할지 한 문장으로 적고, 만약 계획도 하나 붙이는 것입니다.
82. 예를 들어 아침 7시 양치를 마치면 거실 매트에서 스쿼트 20개부터 한다고 적는 거죠.
83. 그리고 야근을 하면 자기 전에 매트 위에서 5분 스트레칭을 한다는 만약 계획을 붙입니다.
84. 642개 실험을 모은 분석에서도, 이렇게 조건을 붙인 계획이 효과가 더 컸습니다.
85. 계획을 여러 번 되뇌었을 때도 마찬가지였고요.
86. 적어 둔 두 문장을 냉장고나 매트 옆에 붙여 두고 소리 내어 읽어 보세요.
87. 다섯째, 두 번 연속으로는 빠지지 않고, 돌아온 날에는 작은 보상을 주는 것입니다.
88. 사연자가 22일째 쉬었다면, 23일째에는 야근을 했더라도 5분은 하는 거죠.
89. 처음에 본 헬스장 회원 실험에서도, 1위는 빠진 뒤 돌아오게 하는 방법이었습니다.
90. 운동을 빠진 뒤 다음번에 다시 오면 9센트, 우리 돈 백 원 남짓의 포인트를 더 줬죠.
91. 이 작은 보상을 넣은 프로그램은 4주 동안 헬스장 방문을 27% 늘렸습니다.
92. 보상은 좋아하는 차 한 잔처럼, 다른 습관을 망치지 않는 것으로 고르면 됩니다.
93. 여섯째, 연속 일수 대신 이번 달에 한 날 수를 적는 것입니다.
94. 하루 빠지면 연속 기록은 0일이 되지만, 한 날 수는 그대로 남습니다.
95. 사연자의 1월도 연속 기록 0일이 아니라, 31일 중 21일 운동한 달로 남는 거죠.
96. 목표는 한 달에 20일 이상처럼 날 수로 정하면 됩니다.
97. 연속 기록 연구에서도, 끊긴 기록을 메울 수 있게 하자 그 영향이 줄었습니다.
98. 물론 21일 챌린지 자체가 나쁜 건 아닙니다.
99. 21일을 끝이 아니라 첫 단계로 보고, 그다음 69일의 계획을 미리 정해 두면 됩니다.
100. 최소 버전과 만약 계획까지 함께 정해 둔다면, 21일은 좋은 출발이 될 수 있습니다.

**마무리** — 🎙 진행자

101. 이렇게 해서 21일 챌린지가 습관이 되지 못한 이유와, 이어 가는 방법을 알아보았습니다.
102. 21일은 결승선이 아니라 출발선이고, 빠진 날보다 빠진 다음 날이 더 중요합니다.
103. 오늘 달력에 바쁜 날의 5분 계획부터 적어 보세요.
104. 원하는 변화를 꼭 이루셨으면 좋겠습니다.
105. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
