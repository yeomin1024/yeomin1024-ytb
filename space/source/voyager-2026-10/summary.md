# voyager-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py space voyager-2026-10` (2026-10-11 04:04). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **보이저 1호는 끝났다고 가르쳤는데 아직 살아서 빛으로 하루 거리에 닿습니다. 낚시 영상 믿은 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 122 / 자막 166, 길이 12:13 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–14 · 진행자 15–122 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/voyager-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 보이저 1호는 끝났다고 가르쳤는데 아직 살아서 빛으로 하루 거리에 닿습니다. 낚시 영상 믿은 사람들의 공통점 `행동 · 판정 반전(끝났다 → 빛으로 하루 거리) · 공통점` 60자 — 짝 썸네일: thumbnail_1 (끝났다 → 빛으로 하루)
- [ ] **T2.** 쇼츠만 믿고 보이저 1호는 끝났다고 했는데 다섯 달 만에 살아났습니다. 제목에 속은 사람들의 불편한 진실 `계기 · 시간 반전(고장 → 다섯 달 만에 복구) · 불편한 진실` 58자 — 짝 썸네일: thumbnail_2 (인물·감정 장면)
- [ ] **T3.** (짧은 변형) 다섯 달 만에 살아난 보이저 1호. 끝났다던 영상이 틀린 진짜 이유 `장면 · 시간 반전 · 진짜 이유(호기심형)` 37자 — 짝 썸네일: thumbnail_3 (끝났다 / 지금도 신호 대비)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (끝났다 → 빛으로 하루 거리)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: '끝났다'는 판정이 **빛으로 하루 거리**까지 간 실제 기록으로 뒤집힌 거리 반전이 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 지운 말 | 끝났다 | 빨강 #E63B2E (네이비 위, 흰 외곽선), 빨강 가로줄로 지움 | — |
| 결과 | 빛으로 하루 거리 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |
| (그림) | 신호선 가운데 노랑 띠 | 노랑 #FFD400 | 유일한 노랑 강조 (글자 없음) |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact blue #2D6CDF, wrong-information red #E63B2E, cream #F2EBDD.
Bottom-right corner kept empty (video length badge).
Clean flat illustrated style (clearly an illustration, not a photo). Dark navy (#14213D) deep-space background with only a
few small faint stars. Lower left: a small simple blue Earth. Upper right: a small generic space probe illustration with
a large dish antenna and thin booms, intact, no logos, no letters, no flags. A thin glowing dotted wave line connects the
Earth and the probe across the frame, with one short bright yellow (#FFD400) band in the middle of the line. Upper center:
the Korean word "끝났다" in bold red (#E63B2E) letters with a thin white outline, crossed out by one thick red horizontal
strike line. Lower center: a wide solid blue (#2D6CDF) rounded box with the huge white bold text "빛으로 하루 거리", the
largest element in the image. Keep all text inside the central 16:9 safe area. Minimal, nothing decorative, no people.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (학생이 내민 기사)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 틀린 걸 가르친 가상 강사가 **다섯 달 만에 복구**됐다는 기사를 마주한 당황한 얼굴이 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 기대 | 끝났다더니 | 흰색 (빨강 #E63B2E 상자) | — |
| 결과 | 다섯 달 만에 복구 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자, 노랑 #FFD400 세로 띠 하나 (유일한 강조) |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact blue #2D6CDF, wrong-information red #E63B2E, cream #F2EBDD.
Bottom-right corner kept empty (video length badge).
A small private-academy classroom in Korea with slightly dim lighting and a dark green chalkboard behind; on the chalkboard
only a simple chalk drawing of a space probe with a dish antenna, no writing. On the left 60% of the frame: a fictional
Korean woman in her mid-thirties, a science tutor in a casual shirt, shown from the chest up, looking at a smartphone held
out toward her with a surprised, embarrassed expression (wide eyes, slightly open mouth, not crying). At the bottom center
only a student's hand is visible holding the smartphone; the phone screen is a plain blue screen with a tiny simple probe
icon, no news layout, no logos, no text. Upper right: a small solid red (#E63B2E) box with white bold text "끝났다더니".
Middle right: a large solid blue (#2D6CDF) box with the big white bold text "다섯 달 만에 복구", the largest text block,
with one thin bright yellow (#FFD400) vertical stripe on its left edge. Keep the face and all text inside the central 16:9
safe area.
fictional person, not resembling any real or famous person, natural Korean features, realistic photo style.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (끝났다는 쇼츠 / 지금도 신호)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 쇼츠가 준 인상('끝났다')과 실제 기록('지금도 신호', 11월 18일)을 좌우로 맞세운 대비가 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 (쇼츠 인상) | 끝났다 | 흰색 (빨강 #E63B2E 상자) | — |
| 오른쪽 (실제 기록) | 지금도 신호 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |
| 오른쪽 아래 | 11월 18일 | 흰색 (네이비 위) | — |
| (그림) | 가운데 화살표 | 노랑 #FFD400 | 유일한 노랑 강조 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact blue #2D6CDF, wrong-information red #E63B2E, cream #F2EBDD.
Bottom-right corner kept empty (video length badge).
Clean flat illustrated style (clearly an illustration, not a photo). The frame is split vertically into two halves.
Left half: a red-tinted panel with a thick red (#E63B2E) border containing one simple tall smartphone screen that looks
like a dark generic short-video screen, with no app name, no buttons, no logos, no channel name; in its center the big
white bold text "끝났다" on a solid red box. Right half: dark navy (#14213D) deep space with a few faint stars and a small
generic space probe illustration with a dish antenna (intact, no logos, no letters, no flags) sending a thin glowing
dotted signal line toward the left; below it a wide solid blue (#2D6CDF) rounded box with the large white bold text
"지금도 신호", the largest text block, and under that box the smaller white bold text "11월 18일". On the dividing line
in the center, one bright yellow (#FFD400) arrow pointing from left to right. Keep all text inside the central 16:9 safe
area. Minimal, nothing decorative, no people.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
보이저 1호가 끝났다는 쇼츠를 믿고 학생들에게 그대로 가르쳤는데, 보이저 1호는 고장 다섯 달 만에 복구됐고 2026년 11월 18일 빛으로 하루 거리에 닿습니다.
보이저 1호 근황을 날짜와 나사 원문으로 정리하고, 탐사선 근황 영상이 사실인지 확인하는 법 5가지를 알려 드립니다.

■ 이 영상에서 다루는 것
- 고장은 끝이 아니었다 (2023년 11월 알아볼 수 없는 신호 → 2024년 4월 다섯 달 만에 복구 → 6월 과학 장비 네 개 자료 복구)
- 이상한 신호의 정체는 칩 하나였다 (비행 데이터 컴퓨터 메모리 약 3%, 코드를 나눠 옮겨 고침)
- 곧 꺼진다는 말은 반만 맞다 (전력이 해마다 약 4와트 감소, 2025년·2026년 장비 끄기, 남은 과학 장비 2개)
- 연락이 끊겼다와 끝났다는 다르다 (약 23와트 송신기, 지름 70m 안테나, 2024년 예비 송신기, 2025년 추진기 복구)
- 벽을 발견했다의 실제 (2012년 태양풍이 끝나는 경계 통과)
- 근황 영상 확인법 5가지: 단정하는 말 의심하기, 영상 날짜와 사건 날짜 맞추기, 원문 찾기, 숫자로 대조하기, 틀렸으면 같은 자리에서 고치기

■ 챕터
0:00 사연: 끝났다고 가르친 보이저 1호가 다섯 달 만에 살아났다
1:30 왜 이런 제목에 끌릴까
2:35 오해 01 고장은 끝이 아니었다
3:26 오해 02 이상한 신호의 정체는 칩 하나
4:26 오해 03 곧 꺼진다는 말은 반만 맞다
6:13 오해 04 연락이 끊겼다와 끝났다는 다르다
7:17 오해 05 벽을 발견했다의 실제
8:15 확인법 첫째: 단정하는 말부터 의심하기
8:51 확인법 둘째: 영상 날짜와 사건 날짜 맞추기
9:35 확인법 셋째: 원문 한 번 찾기
10:15 확인법 넷째: 숫자로 대조하기
11:10 확인법 다섯째: 틀렸으면 같은 자리에서 고치기
11:54 정리

■ 사연에 대해
이 영상의 사연은 실제 발표와 보도(보이저 1호 고장·복구와 1광일 발표, 2023년 11월~2026년 8월)를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시이며, 실존 인물과 관계없습니다. 사연 속 쇼츠는 가상의 영상입니다.

■ 출처 (발표·보도 날짜 기준)
- 나사 보이저 블로그 (2023년 12월~2024년 3월, 비행 데이터 컴퓨터 문제·명령은 받고 실행 중): https://science.nasa.gov/blogs/voyager/2024/03/15/nasa-engineers-make-progress-toward-understanding-voyager-1-issue
- 나사 보이저 블로그 2024-04-04 (메모리 약 3% 손상, 칩 하나): https://science.nasa.gov/blogs/voyager/2024/04/04/engineers-pinpoint-cause-of-voyager-1-issue-are-working-on-solution/
- 나사 2024-04-22 (4월 20일 상태 정보 복구, 다섯 달 만에): https://blogs.nasa.gov/voyager/2024/04
- 2024-04 코드를 나눠 옮긴 방법·신호 편도 약 22.5시간: https://www.theregister.com/2024/04/23/voyager_1_engineering_updates/
- 2024-06 과학 장비 네 개 자료 복구: https://www.space.com/voyager-1-fully-operational
- 2024-10~11 예비 송신기 전환과 복구: https://edition.cnn.com/2024/11/01/science/voyager-1-transmitter-issue/index.html
- 제트추진연구소 2025-03-05 (전력 해마다 약 4와트 감소, 2월 25일 우주 방사선 측정 장비 끔): https://www.jpl.nasa.gov/news/nasa-turns-off-two-voyager-science-instruments-to-extend-mission/
- 2025-05 주 추진기 21년 만에 복구 (3월 20일 확인): https://edition.cnn.com/2025/05/14/science/voyager-1-thruster-fix
- 제트추진연구소 2026-04 (2월 27일 전력 하락, 4월 17일 저에너지 입자 장비 끔, 남은 과학 장비 2개): https://www.jpl.nasa.gov/news/nasa-shuts-off-instrument-on-voyager-1-to-keep-spacecraft-operating/
- 나사 보이저 블로그 2026-08-04 (보이저 2호 전력 절약, 장비 세 개 1년 더): https://science.nasa.gov/blogs/voyager/2026/08/04/nasa-engineers-help-prolong-voyager-2s-science-mission/
- 나사 보이저 위치 (2026-11-18 빛으로 하루 거리, 미국 태평양 표준시 새벽 2시 16분): https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/
- 1광일 날짜 발표 보도 (2026-06): https://earthsky.org/space/voyager-1-1-light-day-from-earth-november-17-18-2026/
- 송신기 약 23와트: https://voyager.jpl.nasa.gov/news/details.php?article_id=50
- 나사 2013-09 (2012년 8월 25일 성간 공간 진입, 전자 밀도): https://www.jpl.nasa.gov/news/nasa-spacecraft-embarks-on-historic-journey-into-interstellar-space/

■ 알려 드립니다
이 영상은 과학 정보 제공을 위한 것이며, 사연은 실제 발표와 보도를 바탕으로 재구성한 이야기입니다.
사연 속 인물과 금액은 이해를 돕기 위한 예시이며, 실존 인물과 관계없습니다.
확률과 거리 같은 수치는 발표 시점 기준이며, 새로운 관측으로 바뀔 수 있습니다.
영상 속 자료의 출처는 설명란에 있습니다.

#우주 #보이저1호 #우주뉴스
```

**태그**: 보이저 1호, 보이저호 근황, 보이저1호 위치, 보이저 1호 1광일, 보이저1호, 보이저 2호, 나사, 우주탐사, 성간우주, 과학다큐, 우주다큐, 우주이야기, 천문학, 과학, 우주 뉴스

**고정 댓글**

```
'끝났다'는 우주 영상을 보면 공유하기 전에 이 세 가지부터 확인해 보세요.
1. 영상 날짜 뒤에 새 발표가 있었나 (보이저 1호: 2023년 11월 고장 → 2024년 4월 복구)
2. 나사 원문에 같은 말이 있나 (나사 보이저 블로그)
3. 숫자가 맞나 (거리 ÷ 빛의 속도 = 신호가 가는 시간, 11월 18일부터 왕복 이틀)

우주 영상 제목을 믿었다가 나중에 사실이 아니란 걸 안 적이 있나요? 댓글로 나눠 주세요.
※ 영상 속 확률·거리는 발표 시점 기준입니다. 새 발표가 나오면 고정 댓글에 덧붙이겠습니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 2023년 12월, 50년 가까이 날아간 보이저 1호가 끝났다는 1분짜리 쇼츠를 봤어요.
2. 마지막 신호는 아무도 못 읽는다고, 외계 신호일지도 모른다고 했죠.
3. 서른넷 학원 과학 강사였던 저는, 지루해하던 중학교 2학년 스물네 명에게 그대로 전했어요.
4. 보이저 1호는 사실상 끝났고, 이상한 신호는 외계에서 온 걸 수도 있다고요.
5. 확인도 안 했는데 반응은 최고였고, 재미있는 선생님이라는 소문에 수강 문의도 늘었죠.
6. 하지만 제가 가르친 건 과학이 아니라 낚시 제목이었어요.
7. 2024년 4월, 한 학생이 보이저 1호가 다섯 달 만에 살아났다는 기사를 내밀었어요.
8. 그 탐사선은 지금도 신호를 보내며 2026년 11월 18일 빛으로 하루 거리에 닿는대요.
9. 기사가 나온 그 주에, 학부모 단톡방에는 학원에서 틀린 걸 가르친다는 말이 돌았어요.
10. 결국 그 반 스물네 명 가운데 여섯 명이 학원을 옮겼어요.
11. 그제야 찾아보니, 이상한 신호는 탐사선 컴퓨터의 칩 하나가 고장 나서 생긴 거였어요.
12. 미국 항공우주국 나사의 기술자들이 지구에서 코드를 옮겨 고친 거였죠.
13. 확인 한 번 안 한 1분짜리 영상이, 아이들 스물네 명의 과학 시간을 틀리게 만들었어요.
14. 제가 선생님이라고 불릴 자격이 있었나 싶어요.

**진행자 파트** — 🎙 진행자

15. 보이저 1호처럼 오래된 탐사선 소식을 들으면 많은 분들이 이런 생각을 하죠.
16. 그렇게 오래됐으면 고장 나는 게 당연하지.
17. 그렇게 먼 데서 고장 난 걸 어떻게 고쳐.
18. 이상한 신호가 왔다면 뭔가 있는 거 아냐?
19. 이런 식으로 우리가 이미 품고 있는 생각을 건드리는 제목일수록 확인 없이 퍼지기 쉽습니다.
20. 실제로 최근 1년 사이 보이저 영상 제목에는 단정하는 말이 자주 붙었습니다.
21. 우주 미아, 소름, 벽을 발견했다, 종료하기로 했다 같은 말들이죠.
22. 그런 영상의 댓글에는 썸네일 낚시 영상은 보지 말라는 말까지 달리기도 합니다.
23. 사연자처럼 그 말을 교실이나 단톡방에서 그대로 전하면, 틀린 이야기는 더 멀리 퍼집니다.
24. 그렇다면 보이저 1호의 실제 기록은 어땠는지 날짜와 숫자로 하나씩 짚어 보겠습니다.

> 🟨 [장면] 과학 정보 제공용 재구성 사연입니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 과학 정보 제공을 위한 것이며, 사연은 실제 발표와 보도를 바탕으로 재구성한 이야기입니다.
> 사연 속 인물과 금액은 이해를 돕기 위한 예시이며, 실존 인물과 관계없습니다.
> 확률과 거리 같은 수치는 발표 시점 기준이며, 새로운 관측으로 바뀔 수 있습니다.
> 영상 속 자료의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

25. 첫 번째 오해는 고장이 곧 끝이라는 생각입니다.
26. 보이저 1호가 알아볼 수 없는 신호를 보내기 시작한 건 2023년 11월 14일입니다.
27. 같은 패턴만 되풀이될 뿐, 과학 자료도 탐사선의 상태도 읽을 수 없었죠.
28. 그런데 나사는 그해 12월, 탐사선이 지구의 명령을 받아 실행하고는 있다고 밝혔습니다.
29. 탐사선이 멈춘 게 아니라, 보내는 말을 알아들을 수 없게 된 상태였던 겁니다.
30. 2024년 4월 20일, 나사는 다섯 달 만에 탐사선의 상태 정보를 다시 받았습니다.
31. 6월에는 그때 켜져 있던 과학 장비 네 개의 자료도 모두 돌아왔죠.
32. 사연자가 쇼츠를 본 2023년 12월은 이야기의 끝이 아니라 시작이었던 셈입니다.
33. 두 번째 오해는 이상한 신호에 무언가 숨은 뜻이 있다는 생각입니다.
34. 원인은 보이저 1호에 실린 컴퓨터 세 대 가운데 하나에 있었습니다.
35. 과학 자료와 상태 정보를 묶어서 지구로 보내는 비행 데이터 컴퓨터죠.
36. 2024년 3월 1일, 기술자들은 이 컴퓨터에 메모리 내용을 통째로 보내라고 명령했습니다.
37. 이틀 뒤 돌아온 신호를 분석한 끝에, 나사는 4월 초 원인을 밝혔습니다.
38. 메모리의 약 3퍼센트를 맡은 칩 하나가 제대로 작동하지 않았던 거죠.
39. 강한 우주 입자에 맞았는지, 그냥 낡아서인지는 나사도 확실히 알 수 없다고 했습니다.
40. 칩을 갈아 끼울 수는 없었습니다.
41. 그래서 칩에 있던 코드를 여러 조각으로 나눠 메모리의 다른 자리에 옮겨 담았습니다.
42. 외계 신호가 아니라, 오래된 컴퓨터의 칩 하나가 일으킨 고장이었던 겁니다.
43. 세 번째로, 보이저가 곧 꺼진다는 말은 반만 맞습니다.
44. 보이저는 플루토늄이 내는 열로 전기를 만드는 원자력 전지로 움직입니다.
45. 이 전력이 해마다 약 4와트씩 줄어들죠.
46. 그래서 나사는 남은 전력에 맞춰 장비를 하나씩 끄고 있습니다.
47. 2025년 2월 25일에는 보이저 1호의 우주 방사선 측정 장비를 껐습니다.
48. 당시 나사의 보이저 프로젝트 책임자는 이렇게 설명했습니다.
49. 지금 장비를 끄지 않으면, 몇 달 뒤 임무 종료를 선언해야 할 수도 있다고요.
50. 2026년 2월 27일에는 탐사선의 방향을 돌리는 작업 중에 전력이 예상보다 떨어졌습니다.
51. 전압이 더 떨어지면 탐사선이 스스로 장치들을 꺼 버리는 보호 기능이 작동할 수 있었죠.
52. 결국 4월 17일에는 저에너지 입자 측정 장비까지 꺼서, 약 1년의 여유를 벌었습니다.
53. 이제 보이저 1호에 남은 과학 장비는 플라스마 파동과 자기장을 재는 두 개뿐입니다.
54. 그럼 결국 곧 끝나는 것 아니냐고 물으실 수 있습니다.
55. 맞습니다.
56. 2025년에 보이저의 프로젝트 과학자도 매일이 마지막일 수 있다고 말했으니까요.
57. 그래도 끝났다와 아껴 쓰는 중은 다릅니다.
58. 2026년 8월 나사 발표에 따르면, 보이저 2호의 히터 같은 장치들을 한꺼번에 껐습니다.
59. 전기를 덜 쓰는 다른 장치들을 대신 켜서, 탐사선이 얼지 않게 한 거죠.
60. 덕분에 남은 과학 장비 세 개를 적어도 1년 더 쓸 수 있게 됐습니다.
61. 나사는 같은 방법을 보이저 1호에도 쓸 계획입니다.
62. 네 번째 오해는 연락이 끊겼다는 소식을 끝났다는 뜻으로 받아들이는 것입니다.
63. 보이저 1호의 송신기 출력은 약 23와트, 냉장고 전구 정도입니다.
64. 이 약한 신호는 미국과 스페인과 호주에 있는, 지름 70미터짜리 안테나들이 받아 냅니다.
65. 지구가 돌아도 한 곳은 늘 보이저 쪽을 볼 수 있게 세 나라에 나눠 둔 거죠.
66. 2024년 10월에는 히터를 켜는 명령 뒤에 보호 기능이 작동해 주 송신기가 꺼졌습니다.
67. 탐사선은 40년 넘게 쓰지 않던 예비 송신기로 바꿔 신호를 보냈죠.
68. 신호는 훨씬 약했지만, 나사는 며칠 만에 그 신호를 찾아 다시 연락했습니다.
69. 11월에는 주 송신기를 다시 켜고 과학 자료도 다시 받기 시작했습니다.
70. 21년 동안 못 쓰던 방향 조절용 주 추진기를, 2025년 3월에 되살리기도 했죠.
71. 연락이 끊겼다는 소식과 끝났다는 소식 사이에는 이만큼 큰 차이가 있습니다.
72. 다섯 번째는 보이저가 태양계 끝에서 벽을 발견했다는 말입니다.
73. 보이저 1호는 2012년 8월 25일, 태양풍이 끝나는 경계를 지났습니다.
74. 태양풍은 태양에서 쉬지 않고 불어 나오는 아주 작은 입자들의 바람입니다.
75. 나사는 이듬해 9월, 보이저 1호가 별과 별 사이 공간에 들어갔다고 발표했죠.
76. 이 경계 근처의 입자는 아주 뜨겁지만, 너무 드물어서 탐사선을 데우지 못합니다.
77. 경계 너머에서 2013년에 잰 전자 수는 1세제곱센티미터에 0.08개 정도였습니다.
78. 가로세로높이 1센티미터짜리 상자 열두 개를 다 뒤져야 전자 하나가 나오는 셈이죠.
79. 벽이 아니라, 태양의 영향이 끝나고 별 사이 공간이 시작되는 경계였던 겁니다.
80. 그렇다면 다음에 보이저 소식을 볼 때는 무엇을 확인하면 될까요?

**올바른 방법 파트** — 🎙 진행자

81. 첫째, 제목의 단정하는 말부터 의심하는 것입니다.
82. 사연자가 본 쇼츠는 끝났다, 외계 같은 결론부터 말했습니다.
83. 같은 시기 나사는 명령은 받지만 자료가 제대로 오지 않는다는 상태만 설명했죠.
84. 나사가 정말 임무를 끝낼 때는 임무 종료를 공식적으로 선언합니다.
85. 그 선언이 없는데 끝났다고 말하는 영상이라면, 사실이 아니라 의견으로 들으면 됩니다.
86. 남에게 전하는 소식은 날짜와 기관과 숫자가 함께 있는 것으로만 고르는 게 좋습니다.
87. 둘째, 영상이 올라온 날짜와 사건 날짜를 맞춰 보는 것입니다.
88. 사연자가 본 쇼츠는 고장 한 달쯤 뒤인 2023년 12월에 나왔습니다.
89. 원인을 찾아낸 2024년 4월보다 넉 달이나 앞선 영상이었죠.
90. 그 뒤 새 발표를 한 번만 찾아봤어도, 학생이 내민 기사에 놀랄 일은 없었을 겁니다.
91. 빛으로 하루 거리에 닿는 날도 처음에는 기사마다 11월 13일, 15일로 달랐습니다.
92. 나사가 2026년 6월에 직접 계산해 발표한 날짜는 11월 18일이었죠.
93. 날짜가 서로 다른 소식이 보이면, 더 나중에 나온 기관의 발표를 기준으로 삼으면 됩니다.
94. 셋째, 원문을 한 번 찾아보는 것입니다.
95. 나사는 보이저 소식을 홈페이지의 보이저 블로그에 날짜와 함께 올립니다.
96. 2026년 4월 17일 글 제목은 탐사선을 계속 운영하려고 장비 하나를 껐다는 뜻이었죠.
97. 그 뒤 영상 제목에는, 나사가 보이저 1호를 종료하기로 했다는 말까지 나왔습니다.
98. 제목만 보면, 탐사선을 살리려고 내린 결정이 정반대로 읽히는 거죠.
99. 영어가 어렵다면 번역기로 제목과 첫 문단만 읽어 봐도 충분합니다.
100. 원문의 문장과 영상의 말이 같을 때만 믿고 전하면 됩니다.
101. 넷째, 숫자끼리 맞는지 대조해 보는 것입니다.
102. 거리를 빛의 속도로 나누면 신호가 한 번 가는 데 걸리는 시간이 나옵니다.
103. 빛은 1초에 약 30만 킬로미터를 갑니다.
104. 11월 18일의 거리는 약 259억 킬로미터입니다.
105. 이걸 30만 킬로미터로 나누면 약 8만 6천 초, 꼬박 하루죠.
106. 2024년 4월에도 신호가 한 번 가는 데 22시간 반쯤 걸렸습니다.
107. 그래서 4월 18일에 보낸 명령의 결과를 4월 20일에야 확인할 수 있었죠.
108. 11월 18일부터는 명령을 보내고 답을 받는 데 꼬박 이틀이 걸립니다.
109. 그러니 하루 만에 고쳤다거나 실시간으로 대화했다는 말은 숫자부터 맞지 않습니다.
110. 이렇게 숫자가 서로 맞아떨어지는지 확인한 뒤에 믿으면 됩니다.
111. 다섯째, 틀린 걸 전했다면 전한 그 자리에서 바로 고치는 것입니다.
112. 사연자는 스물네 명 앞에서 틀린 이야기를 했습니다.
113. 그렇다면 고치는 것도 같은 스물네 명 앞에서 해야 합니다.
114. 예를 들어 칠판에 날짜와 기관과 숫자를 한 줄로 적는 겁니다.
115. 2024년 4월 20일, 나사, 다섯 달 만에 상태 정보 복구.
116. 학부모 단톡방처럼 틀린 말이 퍼진 곳에도 원문 링크를 함께 보내면 됩니다.
117. 한국 시간 11월 18일 저녁 7시 16분쯤을, 아이들과 함께 기다려 볼 수도 있죠.
118. 고친 내용도 날짜와 원문과 숫자로 확인했다면, 그때는 자신 있게 전해도 됩니다.

**마무리** — 🎙 진행자

119. 이렇게 해서 보이저 1호 근황 영상을 제대로 확인하는 법을 알아보았습니다.
120. 끝났다는 제목을 보면, 공유하기 전에 나사의 원문부터 찾아보세요.
121. 우주 소식일수록 숫자와 날짜부터 차분히 확인하셨으면 좋겠습니다.
122. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
