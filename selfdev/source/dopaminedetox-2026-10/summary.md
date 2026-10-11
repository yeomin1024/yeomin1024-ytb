# dopaminedetox-2026-10 한눈에 보기

자동 생성 — `python tools/make_summary.py selfdev dopaminedetox-2026-10` (2026-10-11 07:48). 이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.

> **도파민 디톡스 한다고 주말 48시간 폰을 끊었는데 월요일에만 9시간을 봤습니다. 숏폼 끊으려던 사람들의 최악의 결말**

## 0. 상태

| 단계 | 상태 |
|---|---|
| 대본·SRT | ✅ 문장 122 / 자막 162, 길이 11:57 (SRT 추정) |
| 제목 3개 | ✅ 채택 T1 |
| 썸네일 | 프롬프트 3개 ✅ · 이미지 0/3 (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장) |
| 업로드 시트 | ✅ 설명란·태그·고정 댓글·챕터 |
| 내레이션 역할 | 사연자 1–22 · 진행자 23–122 (`voices/*.json`) |
| 오디오 | ⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/dopaminedetox-2026-10/narration.mp3`로 올리면 영상 제작 시작 |
| 영상 코드 | ⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더) |
| 렌더 | ⏳ 오디오 뒤 |
| 유튜브 | ⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개 |

## 1. 제목 3개 (`titles.md`)

- [x] **T1. (채택)** 도파민 디톡스 한다고 주말 48시간 폰을 끊었는데 월요일에만 9시간을 봤습니다. 숏폼 끊으려던 사람들의 최악의 결말 `행동 · 48시간→9시간 · 최악의 결말` 64자 — 짝 썸네일: thumbnail_1 (숫자 반전)
- [ ] **T2.** 48시간만 참으면 리셋된다길래 버텼는데 월요일에 9시간을 봤습니다. 도파민 디톡스한 사람들이 마지막에 꼭 하는 후회 `속마음 · 48시간→9시간 · 마지막에 꼭 하는 후회` 64자 — 짝 썸네일: thumbnail_2 (인물·감정)
- [ ] **T3.** (짧은 변형) 폰 끊은 주말 48시간, 월요일엔 9시간. 도파민 디톡스의 불편한 진실 `장면 · 48시간→9시간 · 불편한 진실` 39자 — 짝 썸네일: thumbnail_3 (대비)

## 2. 썸네일 3개 (`thumbnails/`)

썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.

### 썸네일 1 ✅ 기본(채택 제목의 짝) — 숫자 반전 (서랍 속 휴대폰 → 월요일 9시간)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_1.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_1.png`로 저장

- 가설: 서랍에 넣은 휴대폰 "48시간 끊고"가 **"월요일 9시간"**으로 뒤집히는 숫자 반전이 가장 빨리 읽히고 클릭을 부른다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 시작 | 48시간 끊고 | 흰색 | 파랑 #2D6CDF 상자 |
| 결과 1 | 월요일 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (유일한 강조) |
| 결과 2 | 9시간 | 빨강 #E63B2E (잃은 것), 흰 테두리 | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, blue #2D6CDF (what was hoped for), red #E63B2E (what was lost).
Bottom-right corner kept empty (video length badge).
Clean semi-flat illustration on a plain dark navy (#14213D) background. On the left 40% of the frame, a half-open wooden
desk drawer seen from the front, with one smartphone lying face-down inside, screen off. Above the drawer, a solid blue
(#2D6CDF) rounded box with white bold text "48시간 끊고". In the center, a thick white arrow pointing right. On the right
50% of the frame, one upright smartphone with its screen on; the screen shows only five or six plain flat vertical bars
with no labels, no numbers, no icons and no app interface, and the last bar is red (#E63B2E) and much taller than the
others. Next to the phone, a solid bright yellow (#FFD400) box with black bold text "월요일", and directly below it the
huge red (#E63B2E) bold text "9시간" with a thin white outline, the largest element in the image. No people, no brain
images, no app logos, no real phone operating system screens. Keep all text and both phones inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 2 — 인물·감정 장면 (월요일 밤 침대에서 휴대폰을 보는 얼굴)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_2.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_2.png`로 저장

- 가설: "리셋 완료"라고 적은 다음 날 밤, 침대에서 또 휴대폰 빛을 받고 있는 **지친 얼굴**이 숫자 카드보다 시청자 자신의 밤을 더 떠올리게 한다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 감정 | 리셋은 없었다 | 잉크 #1E1E1E | 노랑 #FFD400 상자 (글자 전체 높이, 유일한 강조) |
| 결과 | 월요일 9시간 | 흰색 | 빨강 #E63B2E 상자 (잃은 것), "9시간"을 가장 크게 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, blue #2D6CDF (what was hoped for), red #E63B2E (what was lost).
Bottom-right corner kept empty (video length badge).
Realistic photo style. A dark bedroom at night, overall dark navy tone. On the left 45% of the frame, a fictional Korean
woman in her early 30s, an office worker still wearing a plain office blouse after work, lying on her side in bed and
holding a smartphone close to her face. The phone's cold blue-white light illuminates her face. Her expression is tired,
drained and regretful, not crying, not panicked. The phone shows only its back or a soft blank glow, no app interface, no
text. Fictional person, not resembling any real or famous person, natural Korean features. On the right side, a solid
bright yellow (#FFD400) box with black bold text "리셋은 없었다". Below it, a solid red (#E63B2E) box with white bold text
"월요일 9시간", where "9시간" is the largest text in the image. No brain images, no hospital, no pills, no logos.
Keep the face and all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

### 썸네일 3 — 대비 (일요일 밤 '리셋 완료' vs 월요일 출근길 9시간)

🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_3.md`의 [A] 프롬프트를 넣어 만든 뒤 `thumbnails/thumbnail_3.png`로 저장

- 가설: 왼쪽 기대(다이어리의 "리셋 완료")와 오른쪽 결과(월요일 출근길의 "9시간")를 한 화면에 나란히 두면, 문제 분석 첫 메시지("리셋은 일어나지 않는다")가 한눈에 읽힌다

| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 기대 (왼쪽) | 리셋 완료 | 잉크 #1E1E1E 손글씨 느낌의 굵은 글자 | 아래에 노랑 #FFD400 형광펜 줄 (유일한 강조) |
| 결과 (오른쪽) | 9시간 | 빨강 #E63B2E (잃은 것), 흰 테두리 | 가장 큰 글자 |

<details><summary>[A] 완성형 프롬프트</summary>

```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, blue #2D6CDF (what was hoped for), red #E63B2E (what was lost).
Bottom-right corner kept empty (video length badge).
Split-screen image divided vertically in the middle by a thin white line.
LEFT HALF, warm cream (#F2EBDD) lamplight, Sunday night: a desk with an open paper diary; on the page, the large bold
hand-lettered black Korean text "리셋 완료" with one check mark, and a bright yellow (#FFD400) highlighter stroke under the
text. Beside the diary, a half-read book with a blank cover and a pair of clean sneakers. No phone visible.
RIGHT HALF, cool dark navy (#14213D) tone, Monday morning: inside a commuter subway car, the back view of a fictional
Korean woman in her early 30s in office clothes, standing and holding a hand strap, looking down at a smartphone held
close, the phone giving off a soft glow with no visible interface. Her face is not visible. No route maps, no ads, no
signs, no text anywhere in the subway. In the upper part of the right half, the huge red (#E63B2E) bold text "9시간" with
a thin white outline, the largest element in the image. Fictional person, not resembling any real or famous person.
No brain images, no logos. Keep all text inside the central 16:9 area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```
</details>

## 3. 업로드 정보 (`upload.md`)

**설명란**

```
주말 48시간 동안 휴대폰을 서랍에 넣고 도파민 디톡스를 했는데, 월요일 하루에만 화면 시간이 9시간이 나왔습니다.
'도파민 리셋'이 일어나지 않은 이유 5가지와, 숏폼 시간을 줄이는 방법 5가지를 연구와 통계로 정리했습니다.

■ 이 영상에서 다루는 것
- 2025년 스마트폰 과의존 실태조사: 이용자의 22.7%가 과의존 위험군
- '도파민 디톡스'는 과학 용어가 아니다 (하버드 의대 건강 블로그, 2020)
- 한 번에 다 끊는 디지털 디톡스의 효과는 연구마다 엇갈린다 (연구 21개 분석, 2022)
- 문제는 몇 시간 보느냐보다 멈추기 어려운가 (숏폼 연구 71개 분석, 2025)
- 마음먹는 것만으로는 줄이기 어렵다 (스마트폰 사용자 2천여 명 실험, 2022)
- '끊기' 목표보다 '하기' 목표가 더 잘 지켜졌다 (새해 결심 1,066명, 2020)
- 방법 5가지: 2주 동안 설정으로 막기, 하루 한도 미리 정하기, 흑백 화면은 보조로, 안 보기 대신 할 일 정하기, 쉬는 날엔 돌아온 다음 날의 규칙부터

■ 챕터
0:00 사연: 주말 48시간 끊고 월요일 9시간
1:53 왜 한 번에 다 끊으려 할까
3:14 문제 01 '도파민 디톡스'는 과학 용어가 아니다
4:07 문제 02 다 끊는 방법의 효과는 엇갈린다
5:07 문제 03 시간보다 멈추기 어려움이 문제
5:49 문제 04 마음먹기만으로는 줄이기 어렵다
6:25 문제 05 '끊기'만 있고 할 일이 없었다
7:08 첫째: 2주 동안 설정으로 막기
8:27 둘째: 하루 한도를 미리 정하기
9:08 셋째: 흑백 화면은 보조로
9:59 넷째: 안 보기 대신 할 일 정하기
10:37 다섯째: 돌아온 다음 날의 규칙 먼저
11:32 정리

■ 사연에 대해
이 영상의 사연은 실제 연구와 통계를 바탕으로 재구성한 이야기입니다. 사연 속 인물과 숫자는 이해를 돕기 위한 예시입니다.

■ 출처
- 과학기술정보통신부·한국지능정보사회진흥원, 2025년 스마트폰 과의존 실태조사 (2026년 3월 발표): https://eiec.kdi.re.kr/policy/materialView.do?num=278528
- 같은 조사 보도 (머니투데이, 2026년 3월 27일): https://www.mt.co.kr/tech/2026/03/27/2026032710122977237
- 스마트폰 과의존의 뜻 (e-나라지표): https://www.index.go.kr/unify/idx-info.do?idxCd=3061
- Grinspoon, Dopamine fasting: Misunderstanding science spawns a maladaptive fad, Harvard Health Blog 2020: https://www.health.harvard.edu/blog/dopamine-fasting-misunderstanding-science-spawns-a-maladaptive-fad-2020022618917
- Radtke 외, Digital detox: An effective solution in the smartphone era? A systematic literature review, Mobile Media & Communication 2022: https://doi.org/10.1177/20501579211028647
- Nguyen 외, Feeds, Feelings, and Focus (숏폼 메타분석), Psychological Bulletin 2025: https://pubmed.ncbi.nlm.nih.gov/41231585/
- Allcott·Gentzkow·Song, Digital Addiction, American Economic Review 2022: https://www.aeaweb.org/articles?id=10.1257/aer.20210867
- Oscarsson 외, 새해 결심 1년 실험(접근 목표와 회피 목표), PLOS ONE 2020: https://doi.org/10.1371/journal.pone.0234097
- Castelo 외, Blocking mobile internet on smartphones improves sustained attention, mental health, and subjective well-being, PNAS Nexus 2025: https://doi.org/10.1093/pnasnexus/pgaf017
- Dekker·Baumgartner, Is life brighter when your phone is not? (흑백 화면 실험), Mobile Media & Communication 2024: https://journals.sagepub.com/doi/10.1177/20501579231212062

■ 정보 제공용 영상입니다
이 영상은 자기계발 정보 제공을 위한 것이며, 의사나 상담 전문가의 진단을 대신하지 않습니다.
사연은 실제 연구와 통계를 바탕으로 재구성한 이야기이고, 사연 속 숫자는 이해를 돕기 위한 예시입니다.
같은 방법도 사람마다 효과가 다르니, 수면·건강·마음의 문제가 계속되면 전문가와 상담하세요.
영상 속 연구와 통계의 출처는 설명란에 있습니다.

#자기계발 #도파민디톡스 #스크린타임
```

**태그**: 도파민 디톡스, 도파민 디톡스 방법, 도파민 디톡스 효과, 디지털 디톡스, 숏폼 중독, 스마트폰 중독, 스마트폰 과의존, 스크린타임, 스크린타임 줄이기, 집중력, 흑백 화면, 자기계발, 동기부여, 30대 자기계발, 직장인 자기계발

**고정 댓글**

```
휴대폰을 서랍에 넣기 전에 이 두 가지부터 정해 보세요.
1. 숏폼 앱을 잠가 둘 시간 (예: 밤 9시~아침 7시)
2. 다시 켰을 때의 규칙 (예: 출근길 알림 확인 10분, 숏폼은 퇴근 후 30분)

여러분은 휴대폰을 끊어 보거나 줄여 본 적이 있나요? 그때 오래간 방법과 금방 무너진 방법을 댓글로 나눠 주세요.
※ 이 영상은 정보 제공용이며 진단이나 상담을 대신하지 않습니다. 잠·마음의 어려움이 계속되면 전문가와 상담해 주세요. 강의·제품 홍보 댓글은 삭제합니다.
```

## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)

**사연 파트** — 🎙 사연자

1. 2026년 5월, 제 휴대폰이 알려 준 하루 평균 화면 시간은 6시간이었어요.
2. 그중 3시간 넘게는 숏폼이었고요.
3. 저는 서른둘, 출퇴근에만 왕복 두 시간을 쓰는 직장인이에요.
4. 퇴근하면 침대에서 숏폼만 넘기다 새벽 1시를 넘기기 일쑤였죠.
5. 그러다 48시간만 모든 자극을 끊으면 뇌가 리셋된다는 도파민 디톡스 영상을 봤어요.
6. 주말 이틀이면 된다니, 이번엔 할 수 있을 것 같았죠.
7. 5월 8일 금요일 밤 10시, 휴대폰을 서랍에 넣고 음악과 단 음식까지 끊었어요.
8. 주말 동안 산책을 두 번 하고, 책도 반 권이나 읽었죠.
9. 일요일 밤 10시, 48시간을 채우자 머리가 맑아진 것 같았어요.
10. 다이어리에는 '리셋 완료'라고 적었죠.
11. 하지만 그 리셋은 하루도 가지 않았습니다.
12. 월요일 하루에만 화면 시간이 9시간, 평소보다 3시간이나 많았거든요.
13. 서랍에서 꺼낸 휴대폰에는 밀린 알림이 가득했어요.
14. 출근길 지하철에서 알림을 확인하다가 저도 모르게 숏폼으로 넘어갔죠.
15. 점심시간에도, 일하는 틈틈이도, 퇴근하고 침대에 누워서도 멈추지 못했어요.
16. 이틀이나 참았으니 오늘 하루쯤은 괜찮다고 생각했던 거예요.
17. 돌아보니 바뀐 건 하나도 없었어요.
18. 숏폼 앱도, 알림도, 침대 옆 충전기도 그대로였으니까요.
19. 그렇게 4주 동안 주말마다 서랍에 넣었다가 월요일마다 다시 꺼냈어요.
20. 주말은 0시간이었지만, 평일은 오히려 하루 7시간 가까이로 늘어 있었죠.
21. 주말 이틀을 참은 대가로 평일을 통째로 내준 셈이에요.
22. 제가 리셋한 건 뇌가 아니라 한 주의 시작이었나 봐요.

**진행자 파트** — 🎙 진행자

23. 휴대폰 화면 시간을 보고 놀란 날이면 많은 분들이 이런 생각을 하죠.
24. 주말에 한 번 확 끊으면 리셋되겠지.
25. 나는 중독까진 아니야, 심심해서 보는 거지.
26. 마음만 먹으면 언제든 끊을 수 있어.
27. 이런 식으로 마음먹기만 믿다 보면, 한 번에 다 끊는 방법부터 찾게 됩니다.
28. 하지만 마음먹은 대로 휴대폰을 내려놓지 못하는 사람은 생각보다 많습니다.
29. 2026년 3월 정부가 발표한 2025년 스마트폰 과의존 실태조사가 있습니다.
30. 과학기술정보통신부와 한국지능정보사회진흥원이 해마다 하는 조사죠.
31. 이 조사에서 과의존은 사용을 조절하기 어려워 생활에 문제가 생기는 상태를 말합니다.
32. 스마트폰 이용자의 22.7%가 이 과의존 위험군이었습니다.
33. 다섯 명 중 한 명이 넘는 셈이죠.
34. 스마트폰 없이는 일상이 어렵다고 느끼는 고위험군도 4.1%였습니다.
35. 사연자의 주말이 남의 일만은 아닌 이유입니다.
36. 그렇다면 주말 48시간 디톡스는 무엇이 문제였을까요?

> 🟨 [장면] 정보 제공용 영상입니다 (화면 고지 카드 — 자막·내레이션 아님)
> 이 영상은 자기계발 정보 제공을 위한 것이며, 의사나 상담 전문가의 진단을 대신하지 않습니다.
> 사연은 실제 연구와 통계를 바탕으로 재구성한 이야기이고, 사연 속 숫자는 이해를 돕기 위한 예시입니다.
> 같은 방법도 사람마다 효과가 다르니, 수면·건강·마음의 문제가 계속되면 전문가와 상담하세요.
> 영상 속 연구와 통계의 출처는 설명란에 있습니다.

**문제 분석 파트** — 🎙 진행자

37. 첫 번째 문제는 '도파민 디톡스'라는 말부터 과학과 거리가 멀다는 것입니다.
38. 흔히 이틀만 자극을 끊으면 뇌가 리셋된다고 하지만, 연구로 확인된 이야기가 아닙니다.
39. 2020년 하버드 의대 건강 블로그에서 한 의사는 이 유행을 이렇게 짚었습니다.
40. '도파민 단식'은 단식과도, 도파민과도 거의 관계가 없다고요.
41. 도파민은 몸이 늘 만들어 쓰는 물질이라, 굶어서 비울 수 있는 게 아니라는 거죠.
42. 이 방법을 널리 알린 미국의 심리 전문가도, 이름을 글자 그대로 믿지 말라고 했습니다.
43. 원래 뜻은 알림 같은 자극에 바로 반응하는 습관을 줄이자는 상담 치료 방법에 가까웠죠.
44. 사연자의 주말에도 뇌가 리셋된 게 아니라, 휴대폰이 이틀 동안 서랍에 있었을 뿐입니다.
45. 두 번째는 한 번에 다 끊는 방법의 효과가 생각만큼 분명하지 않다는 것입니다.
46. 휴대폰 같은 기기를 한동안 끊는 것을 디지털 디톡스라고 하죠.
47. 2022년에 이런 디지털 디톡스 연구 21개를 모은 논문이 있습니다.
48. 모두 3,625명이었고, 그중 12개는 사람들을 무작위로 나눠 비교한 실험이었죠.
49. 결과는 효과가 있었다는 연구, 없었다는 연구, 오히려 나빠졌다는 연구가 섞여 있었습니다.
50. 끊기만 하면 저절로 좋아진다고 말하기는 어렵다는 뜻입니다.
51. 사연자의 48시간도 월요일의 출근길과 점심시간, 침대 옆 충전기는 하나도 바꾸지 못했죠.
52. 물론 월요일의 9시간은 사연자 한 사람의 경험이고, 누구나 이렇게 된다는 뜻은 아닙니다.
53. 다만 끊었던 이틀이 지나자, 그대로인 평일이 기다리고 있었던 겁니다.
54. 세 번째는 문제가 몇 시간 보느냐보다 멈추기 어려운가에 있다는 것입니다.
55. 2025년 미국심리학회 학술지에 숏폼 연구 71개를 모은 분석이 실렸습니다.
56. 모두 합쳐 9만 8천여 명의 자료였죠.
57. 숏폼을 많이 볼수록 주의력과 충동을 참는 힘이 낮은 경향이 뚜렷했습니다.
58. 특히 보는 시간보다 그만두기 어려운 정도로 잰 연구에서 관련이 더 컸죠.
59. 다만 함께 나타나는 관계를 본 분석이라, 숏폼이 원인이라고 단정할 수는 없습니다.
60. 그래서 중독인지 아닌지보다, 멈추고 싶을 때 멈출 수 있는지가 더 중요합니다.
61. 네 번째는 마음먹는 것만으로는 생각보다 줄이기 어렵다는 것입니다.
62. 2022년 미국경제학회 학술지에는, 스마트폰 사용자 2천여 명의 실험이 실렸습니다.
63. 연구진은 소셜미디어 사용의 31% 정도가, 줄이고 싶어도 못 줄인 몫이라고 추정했습니다.
64. 게다가 참가자들은, 자신의 이런 어려움을 충분히 알아차리지 못했고요.
65. 의지가 약해서만이 아니라, 누구에게나 마음먹은 대로 줄이기 어려운 몫이 있다는 뜻입니다.
66. 다섯 번째는 '끊기'만 있고, 그 시간에 할 일은 없었다는 것입니다.
67. 스웨덴 스톡홀름대 연구진은, 새해 결심을 세운 1,066명을 1년 동안 지켜봤습니다.
68. 무언가를 하겠다는 목표를 세운 사람은 58.9%가 1년 뒤 결심을 지켰다고 답했습니다.
69. 반면 무언가를 끊겠다는 목표는 47.1%에 그쳤죠.
70. 사연자의 계획에는 휴대폰을 안 보는 것만 있었고, 그 시간에 무엇을 할지는 없었습니다.
71. 주말에 했던 산책과 책 읽기도 평일 계획으로는 이어지지 않았죠.
72. 그렇다면 숏폼을 다시 내 뜻대로 쓰려면 어떻게 해야 할까요?

**올바른 방법 파트** — 🎙 진행자

73. 첫째, 이틀 동안 다 끊는 대신 2주 동안 설정으로 막는 것입니다.
74. 캐나다 앨버타대 연구진이 2025년에 발표한 실험이 있습니다.
75. 18세부터 74세까지 467명이 2주 동안 휴대폰의 모바일 인터넷을 막았습니다.
76. 전화와 문자는 그대로 쓸 수 있게 했죠.
77. 그러자 주의력이 나이 들며 떨어지는 10년 치를 되돌린 만큼 좋아졌습니다.
78. 참가자의 91%는 행복감, 정신건강, 주의력 가운데 적어도 하나가 나아졌고요.
79. 인터넷이 막힌 동안 사람을 만나고, 운동하고, 바깥에서 보내는 시간도 늘었습니다.
80. 다만 2주 중 10일 이상 차단을 지킨 사람은 네 명 중 한 명 정도였습니다.
81. 그래서 처음부터 전부 막기보다, 지킬 수 있는 크기로 시작하는 게 현실적입니다.
82. 사연자처럼 퇴근 후에 숏폼을 3시간씩 봤다면, 밤 시간만 막아 보는 거죠.
83. 휴대폰의 앱 시간 제한 기능으로, 밤 9시부터 아침 7시까지 숏폼 앱만 잠그는 식입니다.
84. 충전기는 침대 옆이 아니라 거실로 옮겨 두고요.
85. 실험보다 약한 방법이지만, 2주를 버텨 낸 다음에 막는 시간을 늘려 가면 됩니다.
86. 둘째, 하루에 쓸 한도를 미리 정해 두는 것입니다.
87. 앞에서 본 경제학 실험에서는, 사용 한도를 미리 정하게 하자 사용이 크게 줄었습니다.
88. 잠깐 보상을 걸어 사용을 줄이게 했을 때도, 보상이 끝난 뒤까지 줄어든 효과가 이어졌죠.
89. 사연자라면 숏폼을 하루 30분으로 정해 볼 수 있습니다.
90. 3시간 보던 숏폼을 30분으로 줄이면, 하루에 2시간 30분이 생깁니다.
91. 처음부터 30분이 어렵다면 1시간에서 시작해 2주마다 줄여도 됩니다.
92. 한도는 그날 기분으로 정하지 말고, 전날 미리 정해 두세요.
93. 셋째, 화면을 흑백으로 바꿔 손이 덜 가게 하는 것입니다.
94. 2023년 네덜란드의 작은 실험에서는, 84명이 일주일 동안 화면을 흑백으로 바꿨습니다.
95. 하루 화면 시간이 20분 정도 줄었습니다.
96. 사용을 조절하고 있다는 느낌은 커지고, 스트레스는 덜하다고 답했죠.
97. 다만 휴대폰을 여는 횟수는 그대로였고, 업무 능률이나 잠의 질까지 좋아지지는 않았습니다.
98. 연구 평균만큼이면 사연자의 6시간이 5시간 40분 정도가 되니, 큰 효과는 아닙니다.
99. 그래서 흑백 화면은 앞의 두 방법에 더하는 보조 수단으로 쓰는 게 좋습니다.
100. 하루 종일 흑백이 불편하면, 기종에 따라 밤에만 흑백이 되게 설정할 수도 있습니다.
101. 넷째, 안 보기 대신 할 일을 목표로 세우는 것입니다.
102. 숏폼 안 보기가 아니라, 퇴근 지하철에서 책 10쪽 읽기처럼 할 일을 정하는 거죠.
103. 자기 전 침대에서는 20분 스트레칭을 하는 식으로요.
104. 주말에 사연자가 했던 산책과 책 읽기가 바로 이런 할 일이었습니다.
105. 그 할 일을 주말에만 두지 않고 평일 저녁으로 옮겨 오는 겁니다.
106. 앞에서 본 새해 결심 연구에서도, 하겠다는 목표가 끊겠다는 목표보다 더 많이 지켜졌죠.
107. 할 일은 거창하지 않아도 되고, 하나면 충분합니다.
108. 다섯째, 쉬고 싶은 날은 쉬되, 돌아온 다음 날의 규칙을 먼저 정하는 것입니다.
109. 휴대폰 없이 주말을 보내는 것 자체가 나쁜 건 아닙니다.
110. 다만 리셋을 기대하지 말고, 휴대폰을 다시 켰을 때 무엇을 할지 먼저 정해 두세요.
111. 예를 들어 출근길 알림 확인은 10분, 숏폼은 퇴근 후 30분만 보는 식이죠.
112. 이 규칙을 일요일 밤 다이어리에 '리셋 완료' 대신 적어 두세요.
113. 그러면 월요일 아침 휴대폰을 꺼낼 때 기준이 생깁니다.
114. 그리고 2주 뒤 화면 시간을 다시 확인해 보세요.
115. 6시간이던 하루 평균이 5시간, 4시간대로 조금씩 내려오고 있다면 방향은 맞는 겁니다.
116. 줄이려고 애써도 잠이나 일, 사람 관계가 계속 흔들릴 수 있습니다.
117. 그럴 때는 혼자 버티지 말고 전문가와 상담해 보세요.

**마무리** — 🎙 진행자

118. 이렇게 해서 도파민 디톡스로 리셋이 되지 않은 이유와, 다섯 가지 방법을 알아보았습니다.
119. 이틀 동안 다 끊는 것보다, 매일 쓰는 휴대폰의 설정 하나를 바꾸는 게 먼저입니다.
120. 오늘 밤 숏폼 앱에 시간 제한 하나를 걸어 두는 것부터 시작해 보세요.
121. 원하는 변화를 꼭 이루셨으면 좋겠습니다.
122. 감사합니다.


## 5. 검산·출처

사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)
