# gungmin-sigi-2026-10 썸네일 3 — 실험안 ②: 사람 없이, 오른쪽 3분의 1이 잘려 나간 빈 통장 + '30% 깎임' 낱말

버전: v2.0 — 2026-10-19 — 대본 v2.1(사연형 — 각색 인물 김 씨)·`titles.md` v2.0 R1 기준으로 다시. `guides/thumbnail_guide.md` v3.14. 근거: `README.md`. 옛 v1.0 은 git 이력.

| 항목 | 값 |
|---|---|
| 역할 | 실험안 ② — 공개 뒤 '테스트 및 비교' |
| 시험하는 가설 | 사람 얼굴 없이 '평생 깎인 통장' 한 장면만으로도 클릭을 부르는가 (본안과 사람 유무 한 가지만 다름 — 국민연금 성공 썸네일에 사람 없는 것은 없었음) |
| 짝 제목 | titles.md v2.0 R1 「은퇴 후 국민연금 신청 한 번에 평생 손해봤어요. 꼭 보세요」 |
| 문구 | 제목 R1에서 당부 '꼭 보세요'를 빼고 나머지는 제목 글자 그대로 — 시청자층 '은퇴 후'는 흰색 맨 앞 (`README.md` 2번) |
| 근거 (`README.md` 3번) | 노후·연금·절세 묶음: 걱정 표정 23% vs 7% · 실사 인물 성공 배수 상위 16개 중 56% · 빨강 글자 48% vs 32% · 손해 낱말 43% vs 18% (v1.0 과 같은 자료) |
| 그림 낱말 | '30% 깎임' (본안과 같음) |
| 숫자 근거 | '평생' = 5년 당긴 30% 감액이 평생(국민연금법 제61조②·제63조②, 대본 문장 15·19~22) · '30% 깎임' = 1년 6% × 5년 (문장 15) |
| 인물 나이 | 사람 없음 |
| 저장 경로 | `economic/source/gungmin-sigi-2026-10/thumbnails/thumbnail_3.png` |

## 화면 구성
- **위쪽 약 62%**:
  - 가운데~오른쪽 55%: 밤, 어두운 나무 탁자 위 글자 없는 통장이 펼쳐져 있고 오른쪽 3분의 1이 들쭉날쭉 잘려 나가 조금 떨어져 놓임, 옆에 가위, 탁상 스탠드의 강한 따뜻한 빛. 손·사람 없음.
  - 왼쪽 45%: 낱말 꼬리표 '30% 깎임' — 빨강 둥근 상자, 큰 흰 평면 글자. 굵은 빨강 화살표 2개가 잘려 나간 조각 쪽으로.
  - 배경: 흐린 어두운 거실, 차가운 푸른빛.
- **아래쪽 약 35%**: 본안과 같은 2줄.
- 오른쪽 아래 구석(약 220×70)은 비운다.

## 문구 (그대로 사용)
| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 30% 깎임 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 은퇴 후 국민연금 신청 한 번에 | '은퇴 후' 흰색 · **'국민연금 신청 한 번에' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 평생 손해봤어요 | **전부 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 크게 |

- 노랑은 중요한 것(국민연금 신청 한 번), 빨강은 나쁜 상황(평생 손해 · 30% 깎임)에 쓴다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Upper 62% of the frame:
- Center-right (about 55% of the width): close-up still life on a dark wooden coffee table at night — an open blank bank passbook with nothing printed on it, its right third cut away with a ragged edge, the cut piece lying a little apart, a pair of scissors beside it and a single desk lamp casting a hard warm light on it. No hands, no people.
- Left side (about 45% of the width): one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "30% 깎임" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag toward the cut-away piece of the passbook.
- Background: a dark living room at night, blurred and out of focus, cool blue tones.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge:
line 1 "은퇴 후 국민연금 신청 한 번에" — "은퇴 후" in white and "국민연금 신청 한 번에" in bright yellow #FFD400, all with a thick black outline (line 1 is the longer line: it may run to about 88% of the image width, but keep it at least 4% away from the right edge);
line 2 "평생 손해봤어요" — all in bright red #FF2A2A with a thick white outline, clearly larger than line 1.
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text at all, because YouTube's video length badge covers that corner. If the lines do not fit, make both lines a little smaller rather than letting them run into that corner. Keep the passbook and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
No money, no bills, no coins, no documents with writing, no phones, no calendars, no logos of any institution.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집 프로그램으로)
```
YouTube thumbnail background, 16:9 landscape (1280x720), photorealistic, high contrast.
Upper 62%: center-right, close-up still life on a dark wooden coffee table at night — an open blank passbook with its right third cut away (ragged edge), the cut piece lying apart, scissors beside it, hard warm desk-lamp light. No hands, no people. On the left, one empty solid bright red rounded box with two thick red arrows pointing toward the cut piece. Background: dark living room at night, blurred, cool blue tones.
Lower third: a dark band fading upward from the bottom edge, left empty for a two-line headline.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
- 글자 얹기 (캔바·미리캔버스 등):
  - 빨강 상자 안: 30% 깎임 (흰색, 굵은 고딕)
  - 하단 2줄: Noto Sans KR Black(또는 Pretendard Black), 1줄 약 88px (x 48~약 1,120) · 2줄 약 120px (x 48~약 848 — 가로 80% = 1,024 앞), 색은 위 '문구' 표대로

## 검수
- [ ] 글자가 한 글자도 틀리지 않았는가: 30% 깎임 · 은퇴 후 국민연금 신청 한 번에 · 평생 손해봤어요 ('퇴'의 ㅚ, '번에'의 ㄴ 받침, '봤어요'의 ㅘ·ㅆ 받침까지 확대해서)
- [ ] '국민연금 신청 한 번에'만 노랑, '평생 손해봤어요'만 빨강인가 · '은퇴 후'가 흰색으로 맨 앞에 있는가
- [ ] 사람·손이 없는가 · 잘린 통장이 240px 로 줄여도 '깎여 나간 것'으로 보이는가
- [ ] 가로 320px로 줄여도 2줄과 그림 낱말이 읽히는가
- [ ] 얼굴(또는 통장)과 글자가 가운데 16:9 안에 있는가 · 2줄째가 가로 80% 앞에서 끝나고 오른쪽 아래 구석이 비어 있는가
- [ ] 실존 인물을 닮지 않았는가 · 통장·벽에 글자·로고가 없는가 · 공단 로고·지폐가 없는가

## 이미지 검수 (Claude — 지시사항 10번)

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
