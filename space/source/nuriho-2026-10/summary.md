# nuriho-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py space nuriho-2026-10` (2026-10-11 08:41). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **46초 모자란 실패에 아들 꿈을 말렸는데 누리호는 4번 연속 성공했습니다. 첫 실패만 본 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 127 / 자막 147, 길이 11:52 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–17 · 진행자 18–127 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/nuriho-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 46초 모자란 실패에 아들 꿈을 말렸는데 누리호는 4번 연속 성공했습니다. 첫 실패만 본 사람들의 공통점 `장면 · 횟수 반전(실패 1번 → 4번 연속 성공) · 공통점` 58자 — 짝 썸네일: thumbnail_1 (숫자 반전)
- [ ] **T2.** 우리나라는 안 된다며 아들 꿈을 말렸는데 누리호가 4번 연속 성공했습니다. 실패만 본 부모의 불편한 진실 `속마음 · 횟수 반전 · 불편한 진실` 58자 — 짝 썸네일: thumbnail_2 (인물·감정 장면)
- [ ] **T3.** (짧은 변형) 누리호 실패 뉴스에 아들 꿈을 말렸습니다. 결국 4번 연속 성공한 진짜 이유 `계기 · 횟수 반전 · 결국/진짜 이유(호기심형)` 43자 — 짝 썸네일: thumbnail_3 (검은 배경 제목형 — 채택 제목 문구)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (실패 1번 → 4번 연속 성공)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: "46초"라는 아주 작은 모자람이 **4번 연속 성공**으로 뒤집힌 숫자 반전이 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 핵심 숫자 | 46초 | 빨강 #E63B2E (네이비 위, 흰 외곽선) | 가장 큰 글자 |
| 위쪽 펀치 | 모자란 실패 | 흰색 #FFFFFF (네이비 위, 검정 외곽선) | — |
| 하단 1줄 | 아들 꿈을 말렸는데 | 흰색 + 검정 외곽선 | — |
| 하단 2줄 | 누리호는 4번 연속 성공 | 흰색 + 검정 외곽선 | "4번 연속" 노랑 #FFD400 (실제 결과) |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact/success blue #2D6CDF, failure red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat illustrated style (clearly an illustration, not a photo). Dark navy (#14213D) space background with a few small
faint stars. Everything in this paragraph stays in the upper 60% of the frame: on the left quarter, a small generic plain
three-stage rocket silhouette rising upward with an ordinary orange flame, no flags, no letters, no logos, no explosion.
On the upper right, the huge text "46초" in bold red (#E63B2E) letters with a thin white outline, the biggest text in the
image, and directly below it the smaller white bold text "모자란 실패" with a black outline. Next to them, one short white
arrow pointing right toward a horizontal row of five equal square tiles - the first tile solid red with a white X shape,
the other four tiles solid blue (#2D6CDF) with white check-mark shapes (drawn as simple shapes). No people.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "아들 꿈을 말렸는데", line 2 "누리호는 4번 연속 성공". The word "4번 연속" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep all text inside the central 16:9 safe area. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (생중계 앞의 엄마)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 발사 성공 생중계 앞에서 **후회하는 엄마의 표정**과 등을 돌린 아들이, 숫자 카드보다 '내 얘기'라는 감정을 더 끈다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 핵심 숫자·펀치 | 4번 연속 성공 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |
| 하단 1줄 | 우리나라는 안 된다며 | 흰색 + 검정 외곽선 | "안 된다며" 빨강 #E63B2E (틀린 말, 유일한 강조) |
| 하단 2줄 | 아들 꿈을 말렸는데 | 흰색 + 검정 외곽선 | — |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact/success blue #2D6CDF, failure red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style, soft daylight living room with muted navy and cream tones. Everything in this paragraph stays in
the upper 60% of the frame: on the left 45%, a fictional Korean woman around 50 years old, office-worker look (simple
knit top), shown from the chest up, sitting on a sofa and looking down at a smartphone in her hands with a regretful,
deflated, quietly guilty expression (not crying, not scared). The phone screen shows only a simple drawing of a rocket
rising and one small blue check-mark shape, no app interface, no logos, no text. In the soft background behind her, a
blurred silhouette of a college-age young man standing by the window with his back turned. Fictional people, not
resembling any real or famous person, natural Korean features. On the upper right, a solid blue (#2D6CDF) rounded box with
the huge white bold text "4번 연속 성공", the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "우리나라는 안 된다며", line 2 "아들 꿈을 말렸는데". The words "안 된다며" are red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 safe area. No spacesuits, no flags, no logos, no explosion.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 검은 배경 제목형 (채택 제목 문구)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 그림 없이 검은 배경에 채택 제목 앞 문장만 크게 넣은 **글자만으로** 클릭을 부르는지 (사진·일러스트 썸네일 사이에서 눈에 띄는지)

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 46초 모자란 실패에 | 흰색 #FFFFFF | "실패" 빨강 #E63B2E |
| 2줄 | 아들 꿈을 말렸는데 | 흰색 #FFFFFF | — |
| 3줄 | 누리호는 | 흰색 #FFFFFF | — |
| 4줄 | 4번 연속 성공했습니다 | 흰색 #FFFFFF | "4번 연속 성공" 노랑 #FFD400 |

- 이어 붙이면 "46초 모자란 실패에 아들 꿈을 말렸는데 누리호는 4번 연속 성공했습니다" = 채택 제목 앞 문장 (마침표만 뺌)

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "46초 모자란 실패에", line 2 "아들 꿈을 말렸는데", line 3 "누리호는", line 4 "4번 연속 성공했습니다".
All text pure white (#FFFFFF) except "4번 연속 성공" in bright yellow (#FFD400) and "실패" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
누리호 첫 발사 실패 뉴스 하나로 아들의 우주 꿈을 말렸는데, 그 실패는 3단 엔진 46초가 모자란 것이었고 누리호는 그 뒤 4번 연속 성공했습니다.
누리호 1차 실패의 진짜 내용과 2~5차 발사 기록, 발사 성공·실패 뉴스를 나눠 읽는 법을 정리했습니다.

■ 이 영상에서 다루는 것
- 1차 실패는 마지막 46초였다 (3단 엔진 521초 중 475초, 목표 고도 700km 도달)
- 실패 원인을 찾아 고쳤다 (헬륨 탱크 고정 장치, 2021년 12월 원인 발표 → 8개월 뒤 2차 성공)
- 한 번의 결과로 성공률을 말할 수 없다 (5번 중 4번, 80%)
- 새 로켓의 첫 발사 실패는 다른 나라에도 있다 (일본 H3, 2023년)
- 성공 뉴스도 나눠 읽어야 한다 (5차 15기 중 14기, 3차 도요샛 3호)
- 발사 뉴스 읽는 법 5가지: 어디까지 갔나, 원인과 다음 날짜, 몇 번 중 몇 번, 로켓과 위성 나눠 보기, 아이의 꿈은 함께 확인하기

■ 챕터
0:00 사연: 46초 모자란 실패에 꺾은 아들의 꿈
1:37 첫 실패만 기억하는 이유
2:41 오해 01 실패는 마지막 46초였다
3:44 오해 02 원인을 찾아 고쳤다
4:55 오해 03 한 번으로 성공률을 말할 수 없다
6:08 오해 04 새 로켓의 첫 발사는 어디서나 어렵다
6:58 오해 05 성공 뉴스도 나눠 읽어야 한다
7:49 첫째: 어디까지 갔는지부터
8:30 둘째: 원인 발표와 다음 날짜
9:08 셋째: 몇 번 중 몇 번
9:49 넷째: 로켓과 위성을 나눠 보기
10:33 다섯째: 아이의 꿈은 함께 확인하기
11:32 정리

■ 사연에 대해
이 영상의 사연은 실제 발표와 보도(누리호 1~5차 발사, 2021년 10월~2026년 10월)를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시이며, 실존 인물과 관계없습니다.

■ 출처 (발표·보도 날짜 기준)
- 1차 발사(2021-10-21) 3단 엔진 521초 → 475초: https://www.mt.co.kr/tech/2022/02/25/2022022513354446679
- 1차 발사 "아깝다 46초": https://biz.sbs.co.kr/amp/article/20000035405
- 1차 실패 원인 발표(2021-12-29): https://www.fnnews.com/news/202112291416336373
- 1차 실패 개선(걸쇠식 고정, 4.3G의 1.5배): https://www.nocutnews.co.kr/news/5757648
- 2차 발사 성공(2022-06-21): https://www.mt.co.kr/tech/2022/06/21/2022062117202564968
- 2차 발사 세계 7번째·궤도 속도 초속 7.5km: https://www.newsis.com/view/NISX20220621_0001914924
- 3차 발사 성공(2023-05-25): https://www.mt.co.kr/tech/2023/05/25/2023052515135396944
- 3차 도요샛 3호 미사출 분석(2023-06): https://www.ytn.co.kr/_ln/0105_202306040538374850
- 4차 발사 성공(2025-11-27): https://mobile.newsis.com/view/NISX20251127_0003418610
- 5차 발사 성공·15기 중 14기(2026-10-07): https://news.mtn.co.kr/news-detail/2026100716330458112
- 5차 발사 정부 발표(2026-10-07): https://www.ytn.co.kr/_ln/0105_202610071557514831
- 성공률 80%·6차 2027년 하반기(2026-10-07): https://inews24.com/view/2012682
- 성공률 90%와 상업화(2026-10-04): https://khan.co.kr/article/202610040800001
- 5차 민간 주운영자(2026-10-08): https://news.mtn.co.kr/news-detail/2026100812444652520
- 일본 H3 1호기 실패(2023-03): https://www.upi.com/Science_News/2023/03/06/Japan-H3-rocket-launch-fails/7611678152873/
- 일본 H3 2호기 성공(2024-02-17): https://www.newsis.com/view/NISX20240217_0002630060

■ 알려 드립니다
이 영상은 과학 정보 제공을 위한 것이며, 사연은 실제 발표와 보도를 바탕으로 재구성한 이야기입니다.
사연 속 인물과 금액은 이해를 돕기 위한 예시이며, 실존 인물과 관계없습니다.
확률과 거리 같은 수치는 발표 시점 기준이며, 새로운 관측으로 바뀔 수 있습니다.
영상 속 자료의 출처는 설명란에 있습니다.

#우주 #누리호 #우주뉴스
```

**태그**: 누리호, 누리호 발사, 누리호 5차, 누리호 1차 실패, 누리호 성공률, 누리호 해외반응, 한국형 발사체, 우주항공청, 한국항공우주연구원, 일본 H3, 우주탐사, 우주 뉴스, 우주이야기, 과학다큐, 과학

**고정 댓글**

```
발사 뉴스에서 '실패'라는 말을 보면 이 세 가지부터 확인해 보세요.
1. 어디까지 갔나 (1차는 3단 엔진 521초 중 475초, 목표 고도 도달)
2. 원인 발표와 다음 발사 날짜 (원인 2021년 12월, 2차 성공 2022년 6월)
3. 몇 번 중 몇 번인가 (지금 5번 중 4번, 80%)

첫 뉴스만 보고 판단했다가 나중에 다른 사실을 알게 된 적이 있나요? 댓글로 나눠 주세요.
※ 영상 속 확률·거리는 발표 시점 기준입니다. 새 발표가 나오면 고정 댓글에 덧붙이겠습니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 2021년 10월 21일, 중학교 3학년 아들과 누리호 첫 발사 생중계를 봤어요.
2. 그때 저는 마흔여섯, 아이 진로 걱정이 많던 직장인 엄마였죠.
3. 아들은 어릴 때부터 로켓을 좋아해서 항공우주를 공부하겠다고 했어요.
4. 그날 저녁, 위성 모사체가 궤도에 오르지 못했다는 뉴스가 나왔어요.
5. 저는 아들에게 봤지, 우리나라는 아직 안 된다며 현실적인 과를 가라고 했죠.
6. 그 뒤로 아들은 로켓 이야기를 꺼내지 않았어요.
7. 4년 뒤 다른 과에 합격했을 때는 아이를 현실적인 길로 잘 이끌었다고 믿었죠.
8. 하지만 그날 제가 본 건 46초가 모자랐던 장면 하나였습니다.
9. 2026년 10월 7일 낮 12시 25분, 누리호 다섯 번째 발사가 성공했어요.
10. 2022년부터 4번 연속 성공이었죠.
11. 그 생중계를 휴대폰으로 끝까지 본 대학 2학년 아들이 조용히 말했어요.
12. 엄마, 나 원래 저거 하고 싶었잖아.
13. 그제야 찾아보니 2021년에는 3단 엔진이 521초 중 475초만 타고 꺼졌더라고요.
14. 목표 고도 700킬로미터까지 올라가고도, 46초가 모자라 궤도에 남지 못한 거죠.
15. 원인을 찾아 고친 누리호는 8개월 뒤 두 번째 발사에서 바로 성공했고요.
16. 46초 모자랐던 하루가 아들의 5년을 정해 버렸어요.
17. 실패라는 두 글자 뒤에 무엇이 있었는지, 저는 한 번도 찾아보지 않았어요.

**진행자 파트** — 🎙 진행자

18. 나라의 첫 로켓이 실패했다는 뉴스를 보면 많은 분들이 이런 생각을 하죠.
19. 첫 발사부터 실패했으면 기술이 없는 거지.
20. 우리나라가 무슨 우주야, 이미 늦었어.
21. 실패한 데 계속 돈을 쓰는 건 낭비 아냐?
22. 이런 식으로 '실패'라는 한 단어가 그 뒤의 이야기를 가려 버립니다.
23. 처음 본 장면은 오래 남고, 그 뒤의 소식은 일부러 찾지 않으면 잘 보이지 않죠.
24. 2021년 10월 그날 저녁의 실패 소식을 기억하는 분은 많을 겁니다.
25. 하지만 그 뒤 누리호가 몇 번 중 몇 번 성공했는지 바로 답할 분은 많지 않을 겁니다.
26. 사연자처럼 첫 뉴스 하나로 판단을 끝내는 일이 남의 일만은 아닌 이유입니다.
27. 그렇다면 그날의 실패는 진짜로 무엇이었을까요?
28. 실패 뉴스와 성공 뉴스를 하나씩 나눠서 살펴보겠습니다.

> 🟨 [장면] 과학 정보 제공용 재구성 사연입니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 과학 정보 제공을 위한 것이며, 사연은 실제 발표와 보도를 바탕으로 재구성한 이야기입니다.
> 사연 속 인물과 금액은 이해를 돕기 위한 예시이며, 실존 인물과 관계없습니다.
> 확률과 거리 같은 수치는 발표 시점 기준이며, 새로운 관측으로 바뀔 수 있습니다.
> 영상 속 자료의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

29. 첫 번째 오해는 2021년 1차 발사를 처음부터 다 틀린 발사로 보는 것입니다.
30. 실제로 1차 발사에서 1단과 2단은 계획대로 타고 분리됐습니다.
31. 위성을 감싸는 덮개인 페어링도 떨어져 나갔고, 목표 고도 700킬로미터에도 올라갔죠.
32. 진짜 위성 대신 실은 1.5톤짜리 모형, 위성 모사체도 로켓에서 분리됐습니다.
33. 문제는 마지막 3단에 달린 7톤급 엔진이었습니다.
34. 521초를 타야 할 엔진이 475초 만에 꺼지면서 46초가 모자랐죠.
35. 궤도에 머물려면 초속 7.5킬로미터의 속도가 필요합니다.
36. 그런데 마지막 46초를 못 타서 그 속도를 다 내지 못한 겁니다.
37. 계획한 연소 시간으로 치면 91%까지는 탄 셈이죠.
38. 당시에도 절반의 성공이라는 평가가 함께 나왔습니다.
39. 하지만 사연자의 기억에는 실패라는 두 글자만 남았습니다.
40. 두 번째는 그 실패가 원인을 모르는 실패가 아니었다는 것입니다.
41. 정부와 한국항공우주연구원은 발사조사위원회를 꾸렸습니다.
42. 위원회는 비행 중 로켓이 보내온 데이터 2,600여 개를 분석했죠.
43. 그리고 두 달 뒤인 2021년 12월 29일, 원인을 발표했습니다.
44. 3단 산화제 탱크 안에 있는 헬륨 탱크의 고정 장치가 풀린 것이었습니다.
45. 비행 중에는 최대 중력의 4.3배에 이르는 가속이 걸립니다.
46. 액체산소에 잠긴 헬륨 탱크를 밀어 올리는 부력도 그만큼 커집니다.
47. 그런데 설계할 때 이 힘을 반영하지 못했던 거죠.
48. 풀린 헬륨 탱크가 움직이며 헬륨이 새고, 산화제 탱크에도 금이 갔습니다.
49. 엔진에 들어갈 산화제가 모자라면서 3단 엔진이 일찍 꺼진 겁니다.
50. 연구진은 마찰로 붙잡던 고정 장치를 걸쇠처럼 거는 기계식으로 바꿨습니다.
51. 그리고 4.3배보다 1.5배 큰 힘까지 견디도록 보강했죠.
52. 실패한 비행에서 나온 데이터가 고칠 곳을 정확히 짚어 준 셈입니다.
53. 세 번째는 한 번의 결과로 성공률을 정할 수 없다는 것입니다.
54. 1차 발사 직후 누리호의 기록은 1번 중 0번이었습니다.
55. 8개월 뒤인 2022년 6월 21일, 2차 발사는 성능검증위성을 궤도에 올렸습니다.
56. 1톤 넘는 위성을 자체 기술로 쏘아 올린 세계 7번째 나라라는 평가가 나왔죠.
57. 2023년 5월 25일 3차 발사는 처음으로 실용위성 8기를 싣고 갔습니다.
58. 2025년 11월 27일 새벽 4차 발사는 처음으로 밤에 쏘아 올려 성공했습니다.
59. 그리고 2026년 10월 7일, 5차 발사까지 성공했죠.
60. 그래서 지금 기록은 5번 중 4번, 성공률 80%입니다.
61. 물론 80%가 아직 높은 숫자는 아닙니다.
62. 세계 발사 시장에서 신뢰를 얻으려면 성공률 90% 이상이 필요하다는 보도도 있습니다.
63. 90%가 되려면 10번 중 9번, 앞으로 다섯 번을 연달아 성공해야 하죠.
64. 지금의 누리호는 된다, 안 된다가 아니라 기록을 쌓는 중이라고 봐야 합니다.
65. 네 번째는 새 로켓의 첫 발사 실패가 우리나라만의 일이 아니라는 것입니다.
66. 일본은 30년 만에 새 주력 로켓 H3를 만들었습니다.
67. 2023년 3월 첫 발사에서는 2단 엔진이 켜지지 않았습니다.
68. 결국 파괴 명령을 보내 비행을 끝냈죠.
69. 이때 실려 있던 지구 관측 위성도 함께 잃었습니다.
70. 그리고 1년 뒤인 2024년 2월, 두 번째 발사에서 성공했습니다.
71. 오래 우주 개발을 해 온 나라에도 새 로켓의 첫 비행은 그만큼 어렵다는 뜻입니다.
72. 누리호도 1차에는 모형을, 2차에는 성능검증위성을 실었습니다.
73. 실용위성은 3차에야 실었죠.
74. 한 단계씩 확인한 뒤에 실제 위성을 맡기는 순서였던 겁니다.
75. 다섯 번째는 성공이라는 말도 한 단어로만 읽으면 놓치는 게 있다는 것입니다.
76. 2026년 10월 5차 발사에는 위성 15기가 실렸습니다.
77. 가장 중요한 임무였던 초소형 군집위성 5기는 모두 목표 궤도에 들어갔습니다.
78. 하지만 함께 실은 작은 큐브위성 10기 중 1기는 사출관 덮개가 열리지 않았죠.
79. 그래서 15기 중 14기만 궤도에 들어갔습니다.
80. 2023년 3차 때도 큐브위성 도요샛 3호가 사출관 문이 열리지 않아 분리되지 못했습니다.
81. 그때도 발사 자체는 성공으로 평가됐죠.
82. 성공 뉴스에도 안 된 일이 들어 있고, 실패 뉴스에도 된 일이 들어 있는 겁니다.
83. 그렇다면 다음에 발사 뉴스를 볼 때는 무엇부터 확인해야 할까요?

**올바른 방법 파트** — 🎙 진행자

84. 첫째, 실패 뉴스는 어디까지 갔는지부터 확인하는 것입니다.
85. 발사는 1단 분리, 덮개 분리, 2단 분리, 3단 연소, 위성 분리로 나뉩니다.
86. 2021년 1차는 이 중 3단 연소 단계에서 시간이 모자랐습니다.
87. 521초 중 475초, 계획의 91%까지 탄 거죠.
88. 그렇다면 물어야 할 건 우리나라는 안 된다가 아니라, 모자란 9%가 무엇이었나입니다.
89. 정말 실패로 봐도 되는 때는 같은 원인으로 다시 실패할 때입니다.
90. 원인 발표도 다음 일정도 나오지 않을 때도 그렇고요.
91. 둘째, 원인 발표와 다음 발사 날짜를 찾아보는 것입니다.
92. 누리호는 1차 발사 두 달 뒤에 원인을 발표했습니다.
93. 넉 달 뒤에는 고친 방법과 다음 발사 날짜까지 내놓았죠.
94. 그리고 2022년 6월, 2차 발사에서 성공했습니다.
95. 사연자가 그해 12월 원인 기사를 한 번만 찾아봤다면 어땠을까요?
96. 아들에게 고칠 수 있는 문제래, 다음 발사를 같이 보자고 말해 줄 수 있었을 겁니다.
97. 원인과 고친 방법이 함께 나왔다면, 그 실패는 끝난 일이 아니라 진행 중인 일입니다.
98. 셋째, 성공률은 몇 번 중 몇 번으로 말하는 것입니다.
99. 80%는 5번 중 4번이라는 뜻입니다.
100. 누리호의 6차 발사는 2027년 하반기로 잡혀 있습니다.
101. 6차가 성공하면 6번 중 5번, 83%가 됩니다.
102. 반대로 실패하면 6번 중 4번, 67%로 떨어지죠.
103. 1차 직후 0%였던 성공률이 2차 한 번으로 50%가 된 것도 같은 이유입니다.
104. 횟수가 적을수록 한 번의 결과에 숫자가 크게 흔들리는 겁니다.
105. 퍼센트만 적힌 기사를 보면 몇 번 중 몇 번인지도 함께 찾아보세요.
106. 넷째, 로켓의 결과와 위성의 결과를 나눠 보는 것입니다.
107. 5차의 15기 중 14기라는 숫자만 보면 어디서 생긴 일인지 알 수 없습니다.
108. 분리되지 않은 1기는 위성 쪽 장비인 사출관이 열리지 않은 경우였습니다.
109. 로켓은 정해진 높이까지 위성들을 실어 날랐고, 사출 신호도 정상적으로 보냈습니다.
110. 그래서 정부는 로켓의 임무와 큐브위성 사출을 나눠서 판정했습니다.
111. 5차의 성공 기준은 군집위성 5기를 고도 570킬로미터 근처에 넣는 것이었죠.
112. 제목에 실패나 절반의 성공이 보이면, 로켓과 위성 중 어디의 일인지부터 나눠 보세요.
113. 다섯째, 아이의 하고 싶다는 마음은 뉴스 한 줄이 아니라 함께 확인하는 것입니다.
114. 사연자는 2021년 뉴스 한 줄로 아들의 관심을 접게 했습니다.
115. 2027년 하반기 6차 발사 공식 생중계를 아이와 함께 보세요.
116. 그리고 로켓과 위성, 교신 중 무엇이 가장 궁금한지 물어보세요.
117. 5차 발사에서는 민간 기업이 주운영자를 맡아 발사와 교신을 이끌었습니다.
118. 우주항공청은 2032년까지 해마다 적어도 한 번씩 누리호를 쏘겠다는 계획도 밝혔죠.
119. 한 번의 결과보다 이렇게 이어지는 일정을 함께 보여 주는 게 좋습니다.
120. 말려도 되는 때는 아이가 직접 해 보고 흥미가 식었을 때입니다.
121. 뉴스 한 줄을 봤을 때가 아니고요.
122. 대학생이 된 아이라도 마찬가지입니다.
123. 전공을 바꾸라는 말보다, 그때의 마음을 먼저 물어봐 주세요.

**마무리** — 🎙 진행자

124. 이렇게 해서 발사 실패와 성공 뉴스를 나눠 읽는 법을 알아보았습니다.
125. 실패라는 제목을 보면 어디까지 갔는지와 원인, 몇 번 중 몇 번인지부터 확인해 보세요.
126. 우주 소식일수록 숫자와 날짜부터 차분히 확인하셨으면 좋겠습니다.
127. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
