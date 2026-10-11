# asteroid-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py space asteroid-2026-10` (2026-10-11 04:01). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **충돌 확률 3.1%에 생존 배낭부터 샀는데 엿새 뒤 0.004%였습니다. 소행성 뉴스에 놀란 사람들의 공통점**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 131 / 자막 158, 길이 12:28 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–19 · 진행자 20–131 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/asteroid-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 충돌 확률 3.1%에 생존 배낭부터 샀는데 엿새 뒤 0.004%였습니다. 소행성 뉴스에 놀란 사람들의 공통점 `계기 · 확률 반전 · 공통점` 60자 — 짝 썸네일: thumbnail_1 (확률 게이지 반전)
- [ ] **T2.** 딸 걱정에 짐부터 쌌는데 충돌 확률은 엿새 뒤 0.004%가 됐습니다. 소행성에 겁먹은 사람들의 불편한 진실 `속마음 · 확률 반전 · 불편한 진실` 60자 — 짝 썸네일: thumbnail_2 (인물·감정)
- [ ] **T3.** (짧은 변형) 짐을 다 싸고 나니 확률은 0.004%였습니다. 결국 3.1%가 뒤집힌 진짜 이유 `장면 · 확률 반전 · 진짜 이유(호기심)` 45자 — 짝 썸네일: thumbnail_3 (쇼츠 대 실제 대비)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (확률 게이지)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 확률 바늘이 빨간 **3.1%**에서 파란 **0.004%**로 떨어지는 **숫자 반전**이 가장 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 시작 | 3.1% | 빨강 #E63B2E | — |
| 라벨 | 엿새 뒤 | 잉크 #1E1E1E | 노랑 형광 띠 #FFD400 (글자 전체 높이, 유일한 강조) |
| 결과 | 0.004% | 흰색 (파랑 #2D6CDF 상자 위) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact blue #2D6CDF, risk red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat illustration style, clearly a graphic and not a photo. Dark navy (#14213D) space background with a few sparse
small stars. Far away in the upper right, one small plain grey asteroid drifting alone (no Earth, no Moon, no impact,
no fire, no explosion). In the center-left, a large simple semicircle probability gauge drawn as a flat graphic: the left
end of the arc is red (#E63B2E), the right end is blue (#2D6CDF), and a white needle has swung all the way to the blue
end with a faint motion trail. Next to the red end of the gauge, the text "3.1%" in red bold letters, medium size.
Below the gauge, the short label "엿새 뒤" in ink-black bold letters on a solid bright yellow (#FFD400) highlighter band
the full height of the letters. Across the lower part of the frame, a wide solid blue (#2D6CDF) rounded box with the
huge white bold text "0.004%", the largest element in the image. No people, no logos, no agency names, no mission
patches. Keep all text and the gauge inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: 생존 배낭 앞에서 휴대폰을 보는 **사람의 허탈한 표정**과 쓴 돈이 숫자 카드보다 감정을 더 끈다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 행동 | 150만 원 썼는데 | 빨강 #E63B2E (외곽선 흰색) | "150만 원" 아래 노랑 #FFD400 밑줄 (유일한 강조) |
| 결과 | 0.004% | 흰 글자 (파랑 #2D6CDF 상자) | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact blue #2D6CDF, risk red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Softly blurred bright Korean apartment living room in warm cream tones. On the left 40% of the
frame, a fictional Korean woman around 40, office-worker casual look (plain knit sweater), sitting on the floor and
looking down at her smartphone with a deflated, sheepish, regretful expression, a small tired half-smile, not crying,
not scared. Beside her: a few opened cardboard delivery boxes and two fully packed plain backpacks, with no brand names,
no labels and no printed text on anything. The phone screen faces away or is blurred, no app interface visible.
Fictional person, not resembling any real or famous person, natural Korean features.
On the right side, the bold headline text "150만 원 썼는데" in red (#E63B2E) letters with a thin white outline, with one
thin bright yellow (#FFD400) underline under "150만 원" only. Below it, a wide solid blue (#2D6CDF) rounded box containing
the huge white bold text "0.004%", the largest element. Keep face and text inside the central 16:9 safe area.
No space suit, no astronaut, no asteroid impact, no fire.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (쇼츠 속 숫자 / 실제 발표)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: "역대 최고"라는 쇼츠 문구와 실제 결과를 **나란히 대비**하면 '나도 그 쇼츠 봤는데' 하는 공감이 생겨 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 (쇼츠) | 역대 최고 3.1% | 흰 글자 (빨강 #E63B2E 휴대폰 화면) | — |
| 오른쪽 위 | 엿새 뒤 | 흰 글자 (파랑 카드) | — |
| 오른쪽 결과 | 0.004% | 흰 글자 (파랑 카드) | 가장 큰 글자 |
| 가운데 | (글자 없음) 화살표 | 노랑 #FFD400 | 유일한 강조 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact blue #2D6CDF, risk red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial illustration, clearly a graphic and not a photo. The frame is split vertically into two halves.
Left half: dark navy (#14213D) space background with a few sparse stars and one small plain grey asteroid in the top-left
corner (no Earth, no impact, no explosion). In the middle of the left half, a simple upright smartphone silhouette whose
screen is solid red (#E63B2E) showing only the white bold text "역대 최고 3.1%" (no app interface, no platform logo, no
icons, no buttons). Right half: a large solid blue (#2D6CDF) card filling the half, with the small white bold text
"엿새 뒤" at the top and below it the huge white bold text "0.004%", the largest element in the image.
On the dividing line between the halves, one thick bright yellow (#FFD400) arrow pointing from left to right.
No people, no logos, no agency names. Keep all text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
소행성 충돌 확률 3.1%라는 소식에 생존 배낭부터 샀는데, 엿새 뒤 그 확률은 0.004%가 됐습니다.
소행성 2024 YR4의 충돌 확률이 왜 올랐다가 떨어졌는지, 다음에 확률 뉴스를 보면 무엇부터 확인할지 정리했습니다.

■ 이 영상에서 다루는 것
- 처음 나온 확률은 '아직 모른다'는 뜻 (발견 53일 만의 3.1%, 엿새 뒤 0.004%)
- 확률이 오른 건 위험이 커져서가 아니라 범위가 좁아져서 (유럽우주국 설명)
- 퍼센트 대신 등급으로 읽기 (토리노 척도 3등급 → 1등급 → 0등급)
- 달 충돌 확률 4.3%도 2026년 3월 '가능성 없음'으로 (제임스 웹 우주망원경 관측)
- 크기로 피해 범위 가늠하기 (지름 약 60미터)
- 확률 뉴스를 읽는 5가지: 발견 날짜, 등급, 다음 발표까지 기다리기, 지름, 아이에게 '지켜보는 사람들' 이야기 (루빈 천문대, 다트 실험, 니오 서베이어)

■ 챕터
0:00 사연: 충돌 확률 3.1%에 생존 배낭부터
1:46 역대 최고 확률에 왜 겁이 날까
2:49 문제 01 처음 확률은 '아직 모른다'는 뜻
3:43 문제 02 확률이 오른 건 범위가 좁아져서
4:40 문제 03 퍼센트만 보고 등급은 안 봤다
5:42 문제 04 걱정은 달 충돌로 옮겨 갔다
6:48 문제 05 크기를 훨씬 크게 상상했다
7:40 첫째: 발견된 지 며칠째인지 붙여 읽기
8:15 둘째: 퍼센트를 등급으로 바꿔 읽기
8:52 셋째: 큰돈은 다음 발표 뒤에
9:40 넷째: 지름을 확인하기
10:21 다섯째: 아이에게는 지켜보는 사람들 이야기
11:56 정리

■ 사연에 대해
이 영상의 사연은 실제 발표와 보도(미국 항공우주국·유럽우주국의 소행성 2024 YR4 발표, 2024년 12월~2026년 3월)를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 금액은 이해를 돕기 위한 예시이며, 실존 인물과 관계없습니다.

■ 출처 (확률·거리는 발표 날짜 기준)
- 나사 소행성 2024 YR4 (발견 2024년 12월 27일, 크기): https://science.nasa.gov/solar-system/asteroids/2024-yr4/
- 나사 근지구천체연구센터 — 2024 YR4 토리노 척도 3등급: https://cneos.jpl.nasa.gov/news/news210.html
- 지구 충돌 확률 3.1% (2025년 2월 18일 발표 기준): https://news.wttw.com/2025/02/19/will-asteroid-hit-earth-2032-space-rock-has-highest-impact-probability-ever-recorded-s
- 1.5% (2025년 2월 19일 발표 기준): https://www.ytn.co.kr/_ln/0134_202502201704227690
- 0.28%와 토리노 척도 1등급 (2025년 2월 20일 발표 기준): https://www.theweathernetwork.com/en/news/science/space/impact-odds-of-city-killer-asteroid-2024-yr4-suddenly-drop
- 0.004%, 달 충돌 1.7% (2025년 2월 24일 발표 기준): https://science.nasa.gov/blogs/planetary-defense/2025/02/24/latest-calculations-conclude-asteroid-2024-yr4-now-poses-no-significant-threat-to-earth-in-2032-and-beyond
- 유럽우주국 — 확률이 올랐다가 0이 되는 이유: https://blogs.esa.int/rocketscience/?p=5746
- 토리노 척도 등급 설명: https://cneos.jpl.nasa.gov/sentry/torino_scale.html
- 달 충돌 3.8%, 4.3% (2025년 4월·6월 발표 기준): https://www.theweathernetwork.com/en/news/science/space/puck-shaped-asteroid-2024-yr4-chances-of-hitting-the-moon-increase
- 달 충돌 가능성 없음, 달 표면에서 약 2만 1,200km (2026년 3월 5일 발표 기준): https://science.nasa.gov/blogs/planetary-defense/2026/03/05/new-nasa-asteroid-observations-eliminate-chance-of-2032-lunar-impact/
- 근지구 소행성 발견 현황 (2025년 12월 3일 기준): https://science.nasa.gov/science-research/planetary-science/planetary-defense/near-Earth-asteroids/
- 루빈 천문대 첫 관측 (2025년 6월 23일): https://cnn.com/2025/06/23/science/vera-rubin-observatory-first-images
- 다트 실험 결과 (2022년 10월 발표): https://www.jhuapl.edu/news/news-releases/221011-dart-mission-impact-changed-asteroids-motion-in-space
- 니오 서베이어: https://www.jpl.nasa.gov/missions/near-earth-object-surveyor

■ 과학 정보 제공용 재구성 사연입니다
이 영상은 과학 정보 제공을 위한 것이며, 사연은 실제 발표와 보도를 바탕으로 재구성한 이야기입니다.
사연 속 인물과 금액은 이해를 돕기 위한 예시이며, 실존 인물과 관계없습니다.
확률과 거리 같은 수치는 발표 시점 기준이며, 새로운 관측으로 바뀔 수 있습니다.
영상 속 자료의 출처는 설명란에 있습니다.

#우주 #소행성 #우주뉴스
```

**태그**: 소행성 충돌 확률, 소행성 2024 YR4, 소행성 충돌 2032, 2024 YR4, 소행성 달 충돌, 행성 방위, 토리노 척도, 제임스 웹 우주망원경, 나사, 우주 뉴스, 과학다큐, 우주이야기, 우주미스터리, 천문학, 과학

**고정 댓글**

```
다음에 '충돌 확률' 뉴스를 보면 이 세 가지만 먼저 확인해 보세요.
1. 그 소행성이 발견된 지 며칠째인지
2. 토리노 척도 등급이 몇인지 (0~1등급은 대중이 걱정할 이유가 없는 단계)
3. 지름이 몇 미터인지

우주 뉴스를 보고 놀랐다가 나중에 숫자가 바뀐 걸 안 적이 있나요? 그때 어떻게 하셨는지 나눠 주세요.
※ 영상 속 확률·거리는 발표 시점 기준입니다. 새 발표가 나오면 고정 댓글에 덧붙이겠습니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 2025년 2월 19일 아침 출근길, 소행성 충돌 확률이 3.1%라는 쇼츠를 봤어요.
2. 2032년에 지구에 부딪힐 확률이 역대 최고라는 내용이었죠.
3. 저는 마흔하나, 아홉 살 딸을 키우는 직장인이에요.
4. 2032년이면 딸이 열여섯 살이 되는 해라는 생각부터 들었어요.
5. 그날 밤 생존 배낭 두 개와 한 달 치 비상식량을 결제했어요.
6. 캠핑용 대용량 배터리까지 더하니 150만 원어치였죠.
7. 택배 상자가 현관에 쌓이자 오히려 마음이 놓였어요.
8. 남편은 너무 과하다고 했지만, 3%면 백 명 중 세 명이라며 밀어붙였죠.
9. 딸에게도 엄마가 다 준비해 뒀으니 걱정하지 말라고 했어요.
10. 하지만 그 숫자는 일주일도 버티지 못했어요.
11. 엿새 뒤, 충돌 확률은 0.004%, 2만 5천분의 1로 떨어져 있었어요.
12. 상자는 이미 다 뜯어서 딸과 함께 배낭까지 싸 둔 뒤였죠.
13. 그런데 배낭을 같이 싼 뒤로 딸이 달라졌어요.
14. 잠들기 전마다 2032년에 우리 어떻게 되냐고 묻더라고요.
15. 도대체 왜 이렇게 바뀌었나 찾아보니, 발견된 지 두 달도 안 된 소행성이었어요.
16. 관측이 쌓이는 동안 확률이 올랐다가 한꺼번에 떨어지는 건 예상된 흐름이었대요.
17. 그 뒤에 나온 달 충돌 확률 4.3%도 2026년 3월, 가능성 없음으로 끝났고요.
18. 3.1%라는 숫자 하나에 150만 원과 딸의 밤잠을 맞바꾼 셈이에요.
19. 숫자가 왜 바뀌는지 한 번만 찾아봤어도 아이 앞에서 그렇게 겁먹지 않았을 거예요.

**진행자 파트** — 🎙 진행자

20. 역대 최고 충돌 확률이라는 뉴스를 보면 많은 분들이 이런 생각을 하죠.
21. 3%면 백 번 중 세 번이나 되잖아.
22. 나사가 발표했으면 진짜 위험한 거겠지.
23. 확률이 계속 오르면 결국 부딪히는 거 아냐?
24. 이런 식으로 숫자 하나가 마음속에서 곧 일어날 일로 바뀝니다.
25. 실제로 3.1%는 당시 기록이었습니다.
26. 지름 수십 미터가 넘는 소행성에 매겨진 충돌 확률 가운데 가장 높았거든요.
27. 국내 뉴스에도 이 숫자가 크게 실렸죠.
28. 물론 3%면 낮은 확률 아니냐고 생각하는 분도 계실 겁니다.
29. 맞는 말이지만, 역대 최고라는 말이 붙으면 숫자보다 그 말이 먼저 들어옵니다.
30. 사연자처럼 겁이 난 것도 무리는 아니었던 거죠.
31. 그렇다면 이 숫자가 엿새 만에 뒤집힌 진짜 이유는 뭘까요?

> 🟨 [장면] 과학 정보 제공용 재구성 사연입니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 과학 정보 제공을 위한 것이며, 사연은 실제 발표와 보도를 바탕으로 재구성한 이야기입니다.
> 사연 속 인물과 금액은 이해를 돕기 위한 예시이며, 실존 인물과 관계없습니다.
> 확률과 거리 같은 수치는 발표 시점 기준이며, 새로운 관측으로 바뀔 수 있습니다.
> 영상 속 자료의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

32. 첫 번째 문제는 처음 나온 확률이 '아직 모른다'의 다른 말이었다는 것입니다.
33. 이 소행성의 이름은 2024 YR4입니다.
34. 2024년 12월 27일, 칠레에 있는 소행성 감시 망원경이 처음 찾아냈습니다.
35. 미국 항공우주국 나사는 미국 시간 2025년 2월 18일에 3.1%를 발표했습니다.
36. 발견된 지 53일 만이었죠.
37. 하루 뒤에는 1.5%, 이틀 뒤에는 0.28%로 내려갔습니다.
38. 그리고 엿새 뒤인 2월 24일, 0.004%가 됐습니다.
39. 나사는 이때, 앞으로 100년 동안 지구에 의미 있는 충돌 위험은 없다고 밝혔습니다.
40. 두 달도 안 되는 관측으로 낸 3.1%는 결론이 아니라 중간 계산이었던 겁니다.
41. 두 번째는 확률이 오른 이유를 잘못 읽었다는 것입니다.
42. 확률이 오른 건 위험이 커져서가 아니라, 범위가 좁아져서였습니다.
43. 처음에는 2032년 12월 22일에 소행성이 있을 자리가 아주 넓게 퍼져 있습니다.
44. 관측이 쌓일수록 그 범위가 점점 좁아지죠.
45. 지구가 그 범위 안에 남아 있으면, 범위가 좁아질수록 지구가 차지하는 몫이 커집니다.
46. 그래서 계산된 확률이 올라가는 겁니다.
47. 유럽우주국은 이렇게 확률이 오르는 건 예상된 결과라고 설명했습니다.
48. 그리고 범위가 지구를 벗어나면 확률은 빠르게 0으로 떨어진다고 했죠.
49. 태풍 예상 진로가 날마다 좁아지면서 우리 동네가 들어갔다가 빠지는 것과 비슷합니다.
50. 사연자가 본 3.1%는 범위가 좁아지는 도중의 숫자였습니다.
51. 세 번째는 퍼센트만 보고 등급은 보지 않았다는 것입니다.
52. 소행성 충돌 위험에는 토리노 척도라는 0부터 10까지의 등급이 있습니다.
53. 3.1%일 때 이 소행성은 3등급이었습니다.
54. 3등급의 공식 설명은 천문학자들의 주의가 필요한 가까운 접근입니다.
55. 충돌 확률이 1% 이상이고, 부딪히면 한 지역에 피해를 줄 수 있는 크기라는 뜻이죠.
56. 같은 설명에는 새 관측이 이어지면 대부분 0등급으로 다시 매겨진다는 문장도 있습니다.
57. 접근이 10년 안이면 대중과 공무원도 관심을 가질 만하다고 적혀 있죠.
58. 관심을 가질 단계였지, 짐을 쌀 단계라는 뜻은 아니었습니다.
59. 실제로 확률이 1% 아래로 내려가자 1등급이 됐습니다.
60. 1등급은 일상적인 발견으로, 대중이 걱정할 이유가 없다는 단계입니다.
61. 그리고 곧 위험이 없다는 0등급으로 내려갔습니다.
62. 네 번째는 걱정이 다음 숫자로 옮겨 간다는 것입니다.
63. 지구 충돌 가능성이 사라진 2월 24일, 달에 부딪힐 확률은 1.7%였습니다.
64. 그러자 이번에는 달 충돌 소식이 이어졌죠.
65. 달 충돌 확률은 2025년 4월에 3.8%, 6월에는 4.3%까지 올랐습니다.
66. 2026년 2월, 제임스 웹 우주망원경이 이 소행성을 관측했습니다.
67. 지상 망원경으로는 너무 어두워 보이지 않게 된 뒤였죠.
68. 나사는 2026년 3월 5일, 이 소행성이 달과 부딪힐 가능성은 없다고 발표했습니다.
69. 소행성은 달 표면에서 약 2만 1,200킬로미터 떨어진 곳을 지나갈 것으로 계산됐습니다.
70. 그럼 나사가 틀린 거냐고 물을 수 있습니다.
71. 나사는 소행성의 길이 바뀐 게 아니라고 설명했습니다.
72. 2032년의 위치를 더 정밀하게 알게 된 것이라고요.
73. 지구에서 있었던 일이 달에서 한 번 더 반복된 겁니다.
74. 다섯 번째는 이 소행성의 크기를 실제보다 훨씬 크게 상상했다는 것입니다.
75. 발견 당시에는 밝기만으로 지름 40에서 90미터 정도라고 짐작했습니다.
76. 제임스 웹 우주망원경은 2025년 3월에도 이 소행성을 관측했습니다.
77. 적외선 관측으로 지름을 53에서 67미터로 좁혔죠.
78. 약 60미터, 나사의 설명으로는 10층 건물 정도 크기입니다.
79. 해외 언론이 붙인 별명은 도시 파괴급 소행성이었습니다.
80. 토리노 척도의 설명대로, 부딪혀도 피해는 한 지역 규모라는 뜻이었죠.
81. 하지만 무서운 별명과 역대 최고라는 말이 겹치면서, 사연자는 훨씬 큰 일을 떠올린 겁니다.
82. 그렇다면 다음에 이런 확률 뉴스를 보면 어떻게 읽어야 할까요?

**올바른 방법 파트** — 🎙 진행자

83. 첫째, 확률 옆에 발견된 지 며칠째인지를 붙여 읽는 것입니다.
84. 사연자가 본 3.1%는 발견 53일 만에 나온 숫자였습니다.
85. 관측이 두 달도 쌓이지 않은 확률은 앞으로 바뀔 숫자라고 보면 됩니다.
86. 실제로 나사는 2월 한 달 동안 날짜를 붙여 새 숫자를 여러 번 발표했죠.
87. 처음 듣는 소행성 이름이 나오면 언제 발견됐는지부터 찾아보세요.
88. 관측이 몇 달씩 쌓였는데도 확률이 내려가지 않을 때, 그때 무게를 두면 됩니다.
89. 둘째, 퍼센트를 등급으로 바꿔 읽는 것입니다.
90. 3.1%라는 숫자만 보면 크게 느껴지지만, 토리노 척도로는 3등급이었습니다.
91. 0이나 1등급이면 대중이 걱정할 이유가 없는 단계입니다.
92. 2부터 4등급까지는 천문학자들이 주의해서 지켜보는 단계죠.
93. 기사에 등급이 나와 있으면 퍼센트보다 등급을 먼저 보세요.
94. 생활을 바꾸는 행동은 정부나 공식 기관이 구체적인 안내를 냈을 때 따르면 됩니다.
95. 그전까지는 소식을 지켜보는 것으로 충분합니다.
96. 셋째, 큰돈을 쓰는 결정은 다음 발표를 한 번 본 뒤에 하는 것입니다.
97. 사연자는 3.1%를 본 그날 밤 150만 원을 결제했습니다.
98. 바로 다음 발표에서 확률은 1.5%로 절반이 됐습니다.
99. 엿새를 기다렸다면 0.004%, 결제할 이유 자체가 사라졌죠.
100. 2032년의 일을 걱정하는 거라면 일주일을 기다려도 늦지 않습니다.
101. 위험 소식에 큰돈을 쓰고 싶어지면, 결제 대신 달력에 일주일 뒤 날짜를 적어 두세요.
102. 물론 평소 재난에 대비해 비상용품을 갖춰 두는 것까지 나쁘다는 뜻은 아닙니다.
103. 다만 그건 뉴스 하나에 쫓겨서가 아니라, 평소 계획으로 차분히 준비할 일이죠.
104. 넷째, 확률 다음으로 소행성의 지름을 확인하는 것입니다.
105. 사연자가 걱정한 소행성은 약 60미터였습니다.
106. 앞에서 본 것처럼, 이 정도 크기는 부딪혀도 피해가 한 지역에 그치는 규모입니다.
107. 반대로 지름 1킬로미터가 넘는 큰 소행성은 나사가 따로 세고 있습니다.
108. 2025년 12월 기준으로 873개를 찾았고, 남은 건 50개 정도로 추정합니다.
109. 큰 소행성은 대부분 이미 찾아서 궤도를 알고 있다는 뜻이죠.
110. 그래서 확률과 등급, 지름을 함께 본 뒤에 얼마나 걱정할지 정하면 됩니다.
111. 다섯째, 아이에게는 무서운 숫자보다, 하늘을 지켜보는 사람들을 이야기해 주는 것입니다.
112. 사연자의 딸은 3.1%라는 숫자보다, 배낭을 싸는 엄마의 모습에 더 놀랐을지도 모릅니다.
113. 예를 들어 밤마다 하늘을 살피는 망원경들이 있다고 말해 줄 수 있습니다.
114. 2025년 6월, 칠레의 베라 루빈 천문대가 첫 관측 영상을 공개했습니다.
115. 새로 지은 이 천문대는 약 10시간 관측만으로 새 소행성 2,104개를 찾아냈습니다.
116. 그중 지구 가까이 오는 7개도 위험하지 않은 것으로 확인됐죠.
117. 2022년에는 나사가 소행성의 길을 바꿀 수 있는지 시험했습니다.
118. 다트라는 탐사선을 작은 소행성에 일부러 부딪힌 실험이었죠.
119. 그 소행성이 큰 소행성을 한 바퀴 도는 시간은 30분 넘게 짧아졌습니다.
120. 나사가 정한 최소 목표인 73초의 25배가 넘는 변화였습니다.
121. 하지만 아직 찾지 못한 소행성도 많습니다.
122. 나사 집계로 계산하면, 지름 140미터가 넘는 소행성은 45% 정도만 찾았거든요.
123. 그래서 소행성을 찾는 우주망원경 니오 서베이어가 2027년 9월 이후 발사될 예정입니다.
124. 목표는 5년 동안, 지름 140미터가 넘는 소행성의 3분의 2 이상을 찾는 거죠.
125. 아이가 물으면 지금 등급이 몇인지, 누가 지켜보고 있는지로 답해 주세요.

**마무리** — 🎙 진행자

126. 이렇게 해서 충돌 확률 3.1%가, 엿새 만에 0.004%가 된 이유를 알아보았습니다.
127. 확률 뉴스를 읽는 다섯 가지 방법도 함께 살펴봤죠.
128. 처음 나온 확률은 아직 모른다는 뜻이라는 것만 기억하셔도 충분합니다.
129. 다음에 비슷한 소식을 보면 발견된 날짜와 등급, 크기부터 확인해 보세요.
130. 우주 소식일수록 숫자와 날짜부터 차분히 확인하셨으면 좋겠습니다.
131. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
