# gungmin-sigi-2026-10 쇼츠 썸네일 1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 회사 동기 모임 식당에서 두 손으로 머리를 감싸 쥔 57세 김씨 + '조기수령' 생각 꼬리표

버전: v1.0 — 2026-10-18 — 쇼츠 대본 `../gungmin-sigi-2026-10-shorts.txt` (`../shorts.md` v1.0) 기준. `guides/thumbnail_guide.md` v3.14 12번(재테크 쇼츠 = **세 칸 band** — 위 0~36% 검정 + 문구 2줄 줄마다 가운데·최대 크기 · 가운데 36~72% 사진 · 아래 72~100% 검정, 글자·얼굴은 높이 15~85% 안) · 피드백 21(조사)·22(좌절 얼굴)·24·25·26. 완성 예 `gicho-yeongeum-2026-10/shorts/thumbnails/thumbnail_1.md` v3.0.

| 항목 | 값 |
|---|---|
| 역할 | **본안 — 쇼츠 썸네일 + 첫 문장 화면.** ① 쇼츠 썸네일 (업로드 도구가 API 로 올림 — 이 채널에서 안 보이면 앱에서 0초 장면) ② 영상 0:00~약 0:07, 첫 문장을 읽는 동안 전체 화면 (확대 없이 — 피드백 26, 구운 자막은 아래 검정 칸에 얹힘). 쇼츠는 1장 |
| 시험하는 가설 | 없음 — 쇼츠는 시안 1장 |
| 배치 | `COVER_LAYOUT: band` — **세 칸**: 위 0~36% 검정 + 문구 2줄 · 가운데 36~72% 사진(가로 끝까지) · 아래 72~100% 검정(빈 칸 — 영상에서는 첫 문장 자막 자리). 글자·얼굴은 높이 15~85% 안 (일부 피드가 쇼츠 썸네일을 4:5 로 잘라 위아래 약 15%씩 안 보임). 검사 `python3 tools/cover_check.py` |
| 짝 제목 | `../shorts.md` R1 「국민연금 5년 당겨 받는 남편 평생 매달 39만 원 덜 받는다」 (사용자가 R2를 고르면 문구는 그대로 — 두 안 모두 '5년 당기면 평생 매달 39만 원 덜 받는다'를 담음) |
| 문구 | 제목을 줄인 말 — 2줄 「국민연금 5년 당기면 평생 / 매달 39만 원 덜 받는다」. '남편'은 그림이 보여 줌. 두 줄 너비를 맞추려고 '평생'을 1줄 끝에 (Noto Sans KR Black 100px 로 잼: 1줄 1,050px · 2줄 949px → 긴 줄을 너비 92% 에 맞추면 약 95px, 화면 높이의 4.9%) |
| 조사·뜻 점검 (피드백 21) | 2줄만 읽어도 '매달 39만 원 덜 받는다' = 받는 연금이 줄어듦 (무엇을 날리나 헷갈림 없음 — '날린다'가 아니라 '덜 받는다'). 1줄 '국민연금 5년 당기면 평생'은 2줄과 이어 읽는 말 |
| 근거 | 돈 이야기 성공 쇼츠 표지 66장 중 51장(77%)이 '위 검은 띠 + 큰 글씨 2줄 + 가운데 사진' 꼴 (`economic/source/eunte-kkeonaeseugi-2026-10/shorts/thumbnails/README.md` 3번 — 네 편 공통 근거) · 금액 21/66 · 실사 인물 45/66 · 노후 묶음 걱정 표정 23% vs 7% (롱폼 근거). 국민연금 받는 시기 쇼츠 표지 근거는 **없음** (닮은 성공 쇼츠 「국민연금 30% 덜 받아도… 전문가가 당겨 받겠다는 이유」는 진행자 실사 — shorts_insights 1번) · 그림 속 낱말 = 댓글 니즈 낱말 '조기수령' (롱폼 `../../thumbnails/README.md` 3-3) |
| 숫자 근거 | '39만 원' = 65세 월 130만 원 − 60세 월 91만 원 (쇼츠 문장 1·5, 롱폼 README 4번) · '5년'·'평생' = 법 제63조② (5년 당김 1천분의 700, 평생) · 2026년 숫자 |
| 인물 나이 | 쇼츠의 김씨 57세 — 젊어 보이는 50대 초반처럼. 옷·곳·몸짓은 롱폼 썸네일(밤 거실 식탁·진회색 카디건·이마를 짚음)과 다르게: **저녁 식당·남색 체크 셔츠·두 손으로 머리를 감싸 쥠** |
| 저장 경로 | `economic/source/gungmin-sigi-2026-10/shorts/thumbnails/thumbnail_1.png` |

## 화면 구성
- 세로 9:16 (1080×1920), **세 칸**:
  - **0~36% — 검은 바탕(#000000) + 문구 2줄**: 줄마다 **가운데 정렬**(두 줄의 가운데 축이 같음), 두 줄 같은 크기, **최대 크기 = 긴 줄이 너비 4~96%** (약 95px). 두 줄 덩어리는 높이 약 19~32% (15% 선과 사진 사이 가운데), 사진과 3% 넘게 떨어짐.
  - **36~72% — 사진 칸** (가로 끝까지, 위아래 곧은 가로선, 테두리·그라데이션 없음): 저녁, 따뜻한 조명의 한식당(배경 흐림). 식탁 앞에 앉은 김씨(너비 약 30~82%, 가슴 위까지): 짧은 검은 머리에 관자놀이만 희끗, 남색 체크 셔츠. **두 손으로 머리를 감싸 쥐고 고개를 떨굼**, 눈을 질끈 감고 미간을 찌푸린 좌절·후회 얼굴 (평생 덜 받는다는 걸 막 알게 됨). 얼굴은 손에 가리지 않게. 왼쪽 앞(화면 밖에서 들어온) 친구의 손이 글자 없는 흰 종이 한 장을 식탁 위에 내밀고 있음 — 친구 얼굴은 보이지 않음.
    - 왼쪽(너비 약 7~28%, 높이 약 40~56%): 생각 꼬리표 1개 '조기수령' — 연회색 둥근 사각형 + 짙은 회색 테두리 + 검정 평면 글자, 김씨 머리 쪽으로 작은 회색 점 (김씨가 하려던 것 — 손해 자체가 아니라 빨강이 아님).
  - **72~100% — 검은 바탕, 빈 칸** (영상에서는 첫 문장 자막 자리 · 유튜브 화면에서는 제목·채널 글씨 자리).
- **안전 구역 = 높이 15~85%** — 글자·얼굴·꼬리표는 모두 이 안.
- 오른쪽 16% (좋아요·댓글 버튼 자리 — 높이 약 45% 아래): 사진은 이어지고 얼굴·꼬리표 없음.

## 문구 (그대로 사용)
| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 조기수령 | 검정 평면 글자 on 연회색 꼬리표 #D9DEE6 (짙은 회색 테두리) |
| 위 1줄 | 국민연금 5년 당기면 평생 | **'국민연금' 노랑 #FFD400** · '5년 당기면 평생' 흰색 — 검은 바탕, 가운데 정렬 |
| 위 2줄 | 매달 39만 원 덜 받는다 | **전부 빨강 #FF2A2A + 얇은 흰 외곽선**. 1줄과 같은 크기, 가운데 정렬 |

- 노랑은 중요한 것(주제 낱말 '국민연금'), 빨강은 나쁜 상황(덜 받는 돈)에만. 회색 꼬리표 = 김씨의 생각.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
LAYOUT — three stacked zones, each spanning the full width of the canvas:
1. Top zone, from 0% to 36% of the height: flat solid pure black (#000000), with only the headline text on it.
2. Photo panel, from 36% to 72% of the height: one photorealistic photograph filling the full width edge to edge (a wide horizontal picture, about 3:2), with straight horizontal top and bottom edges.
3. Bottom zone, from 72% to 100% of the height: flat solid pure black (#000000), completely empty (a subtitle is added there later in the video).
No gradient or fade between the zones, no border or frame around the photo, no other bands or panels.
SAFE AREA: YouTube crops Shorts thumbnails to about 4:5 in some feeds on phones and PCs, cutting about 15% from the top and 15% from the bottom. Every important thing — all text, every face and word tag — must stay between 15% and 85% of the height.
Headline in the top black zone: exactly TWO lines of very large, heavy, bold Korean text, both lines the same letter size, EACH LINE CENTERED horizontally on the same center axis (the two lines must not be shifted left or right against each other). Make the letters as large as possible: the longer line spans from about 4% to 96% of the width (each letter about 4.9% of the image height tall, roughly 95 px on a 1080x1920 canvas). Vertically, the two-line block is centered between the 15% line and the top of the photo — it sits between about 19% and 32% of the height — with a black gap of at least 3% of the height between the text and the photo. The text never touches or overlaps the photo. Flat letters on the black, no glow, no 3D, no shadow boxes:
line 1 "국민연금 5년 당기면 평생" — "국민연금" in bright yellow #FFD400 and "5년 당기면 평생" in white;
line 2 "매달 39만 원 덜 받는다" — all in bright red #FF2A2A with a thin white outline.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536) with the same three zones (it will be center-cropped to 9:16, cutting about 8% from the left and right), and keep the headline between 12% and 88% of the width.
Scene inside the photo panel (from 36% to 72% of the height, full width), a warmly lit Korean restaurant in the evening, background softly blurred:
- Center-right (between about 30% and 82% of the width, chest up, face between 40% and 64% of the height): a Korean man aged 57 who looks youthful for his age, like his early 50s (short neat black hair with a little gray at the temples, navy checked button-up shirt), sitting at a restaurant table. He has just realized that he would get less pension every month for the rest of his life, and he is crushed: both hands gripping the sides of his head, head bowed, eyes squeezed shut and brows knitted in pain — clear frustration, regret and despair that read even at small thumbnail size. His face stays visible (the hands are on the sides of his head, not covering his eyes or mouth). Realistic, not cartoonish. From the lower left edge, only the hand of a friend (no face) slides one blank white sheet of paper with nothing printed on it across the table toward him. Fictional person, not resembling any real or famous person. No other people.
- Left side (between about 7% and 28% of the width, at about 40% to 56% of the height): one word tag like a thought label, linked to the man's head by a short trail of small light-gray dots (it shows what he had planned). The tag is a solid light gray (#D9DEE6) rounded rectangle with a thick dark gray border and the Korean word printed in huge flat heavy bold black letters on its flat front face: "조기수령". The letters are flat print, not carved, embossed or 3D letter shapes. No arrows. Nothing overlaps or covers the tag or the letters.
No money, no bills, no coins, no documents with writing, no phones, no calculators, no calendars, no menus or signs with writing, no logos, no charts.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집 프로그램으로)
```
Vertical YouTube Shorts thumbnail background, 9:16 portrait (1080x1920), high contrast. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas. It is also the full-screen opening frame of the Short.
LAYOUT — three stacked zones, each spanning the full width: top zone from 0% to 36% of the height flat solid pure black (#000000), completely empty (a two-line headline will be added later); photo panel from 36% to 72% of the height, one photorealistic photograph filling the full width edge to edge with straight top and bottom edges; bottom zone from 72% to 100% flat solid pure black, empty. No gradient, no fade, no border.
Keep all faces and important objects between 38% and 70% of the height (inside the photo panel).
Photo panel: a warmly lit Korean restaurant in the evening, background blurred; a Korean man aged 57 who looks like his early 50s (short black hair with a little gray at the temples, navy checked shirt), chest up, center-right (about 30% to 82% of the width), both hands gripping the sides of his head, head bowed, eyes squeezed shut, brows knitted in frustration and regret (face visible); from the lower left edge only a friend's hand slides one blank white sheet of paper across the table toward him. Fictional person, not resembling any real or famous person. On the left (about 7% to 28% of the width, 40% to 56% of the height): one empty solid light gray rounded rectangle with a thick dark gray border, linked to the man's head by a short trail of small light-gray dots. Keep the right 16% of the width free of faces.
If 9:16 is not available, use 2:3 portrait (1024x1536) with the same zones and keep the face inside the middle of the width.
Absolutely no text, letters, numbers, logos or watermarks.
```
- 글자 얹기 (캔바·미리캔버스 등, 1080×1920 기준):
  - 회색 꼬리표 안: 조기수령 (검정, 굵은 고딕)
  - 위 2줄 (검은 위 칸): Noto Sans KR Black(또는 Pretendard Black), 두 줄 같은 크기 약 95px, **줄마다 가운데 정렬**(가운데 x 540 — 긴 줄이 x 43~1,037), 두 줄 덩어리의 가운데 y 약 488 (글자 y 약 375~600), 줄 간격 = 글자 크기 × 1.2, 색은 위 '문구' 표대로 (외곽선은 빨강 줄만 얇은 흰색)

## 검수
- [ ] 한글이 한 글자도 틀리지 않았는가: 조기수령 · 국민연금 5년 당기면 평생 · 매달 39만 원 덜 받는다 ('령'의 ㅕ, '당기면'의 ㅇ 받침, '평생'의 ㅇ 받침, '받는다'의 ㄷ 받침까지 확대해서)
- [ ] '국민연금'만 노랑, '매달 39만 원 덜 받는다'만 빨강인가 · 꼬리표가 회색(빨강 아님)인가
- [ ] **문구 2줄이 검은 위 칸에 최대 크기·가운데인가** — 줄마다 가운데 정렬(두 줄 가운데 축이 같음), 긴 줄이 너비 약 4~96%, 글자 높이 약 4.9%, 사진과 겹치거나 붙지 않음
- [ ] **세 칸 배치인가** — `python3 tools/cover_check.py economic/source/gungmin-sigi-2026-10/shorts/thumbnails/thumbnail_1.png` ✅ (위 0~36%·아래 72~100% 검정, 사진 칸은 가로 끝까지, 글자는 높이 15% 아래·사진과 1.5% 넘게 떨어짐, 줄마다 가운데, 긴 줄 너비 80% 이상). 문구가 15% 선 위면 `tools/cover_shift.py` (피드백 26)
- [ ] **좌절로 보이는가** — 두 손으로 머리를 감싸 쥐고 고개를 떨군 얼굴 (놀람·고민 아님), 얼굴이 손에 가리지 않음, 가로 240px 로 줄여도
- [ ] 친구 얼굴이 없고, 종이에 글자가 없는가 · 메뉴·간판·로고·돈이 없는가 · 실존 인물을 닮지 않았는가
- [ ] 롱폼 썸네일(밤 거실·진회색 카디건·이마를 짚음)과 다르게 보이는가

## 이미지 검수 (Claude — 지시사항 10번)

## 결과 (업로드 후)
| 날짜 | 공개 뒤 썸네일 보임 (`oardefault.jpg`) · 본 비율 · 관련 동영상 클릭 | 메모 |
|---|---|---|
