# toejik-geonbo-2026-10 쇼츠 썸네일 1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 현관에서 첫 건보료 고지서를 열어 보고 좌절한 60세 최씨 부부

버전: v3.0 — 2026-10-17 — **세 칸 배치** (위 0~36% 검정 + 문구 2줄 「건보료 고지서대로 내면 / 3년에 860만 원 날린다」 줄마다 가운데·최대 크기 약 102px · 가운데 36~72% 사진 · 아래 72~100% 검정) · 글자·얼굴은 높이 15~85% 안 (4:5 로 잘려도 남게) — 사용자 지시 2026-10-17 "이미지 외 영역은 검은 배경으로 하고 문구는 두 줄로해서 최대 크기로 맞춰 너가 보내준 ISA 만기 쇼츠 문구 위치 좀 어긋나 있는데 저렇게 하면 안돼 그리고 PC나 모바일에서 볼 때 위 아래 영역이 좀 짤릴 수 있는데 그러면 안돼 프롬프트 수정해봐" (`guides/thumbnail_guide.md` 12번·피드백 24, `tools/cover_check.py` v1.1 band). 장면·표정·꼬리표는 v2.1 그대로. (v2.2 — 2026-10-17 — **문구를 크게 — 3줄** 「건보료 고지서대로 / 내면 3년에 / 860만 원 날린다」: 글자 높이 약 화면의 7% (약 125px — 예전 2줄은 너비 7~84% 안이라 약 86px), 가장 긴 줄이 너비 94% 까지, 글자 자리 10~36%·얼굴·꼬리표 38~66% (사용자 지시 2026-10-17 "문구를 더 크게해서 잘보이게 해봐" — `guides/thumbnail_guide.md` 12번·피드백 23). 낱말·색 뜻·장면은 그대로. (v2.1 — 2026-10-17 — **표정 = 손해를 알고 좌절** (v2.0 '편지를 보며 굳음' = 놀람이라 손해로 안 보임 — 미간을 찌푸리고 이를 악문 채 어깨가 처짐, 아내는 울상. 장면·문구·봉투·자리는 그대로 — `guides/thumbnail_guide.md` 피드백 22, 사용자 지시 2026-10-17 "야 기초연금 썸네일 그림은 왜이래? 왜 손해봐서 좌절하는게 아닌것 같지?"). (v2.0 — 2026-10-17 — **제목이 바뀌어 문구를 새로** (짝 제목 R3 「건보료 고지서대로 낸 부부 3년에 860만 원 날린다」 → 문구 「건보료 고지서대로 내면 / 3년에 860만 원 날린다」 — 동사로 끝·조사), **사진이 화면 끝까지** (빈 남색 띠 없음 — `guides/thumbnail_guide.md` v3.8 12번·피드백 18·19). 장면(인물·물건)은 1차와 같음. 1차 그림 → `rejected/thumbnail_1_try1_2026-10-17.png`. 사용자 지시 2026-10-17 "나머지도 변경 사항 있으면 썸네일 다시 그리도록 해 그리고 chatgpt 한테 줄 지시사항 변경한거 맞지 다시 확인해". (v1.0 — 2026-10-16 — 쇼츠 대본 toejik-geonbo-2026-10-shorts.txt (`../shorts.md` v2.0) 기준. 사용자 지시 2026-10-16 "이거 쇼츠 영상 썸네일 이미지 프롬프트 만들어서 영상 처음에만 그걸 포함 시키고 첫 대사를 그 이미지 띄워놓고 하는게 나을 것 같아 롱폼 영상 만들 때처럼 해서 쇼츠 영상, 이미지 프롬프트 4개 다 만들도록 하고". `guides/thumbnail_guide.md` v3.3 (쇼츠라서 다른 것은 1편 `eunte-kkeonaeseugi-2026-10/shorts/thumbnails/README.md` 2번). 근거: `README.md`.)

| 항목 | 값 |
|---|---|
| 역할 | **본안 — 쇼츠 썸네일 + 첫 문장 화면.** ① 쇼츠 썸네일 (업로드 도구가 API 로 올림 — 이 채널에서 안 보이면 앱에서 0초 장면) ② 영상 0:00~약 0:05, 첫 문장을 읽는 동안 전체 화면 (구운 자막이 y 1300~1520 에 얹힘). 쇼츠는 1장 |
| 배치 | `COVER_LAYOUT: band` — **세 칸** (v3.0): 위 0~36% 검정 + 문구 2줄 · 가운데 36~72% 사진(가로 끝까지) · 아래 72~100% 검정(빈 칸 — 영상에서는 첫 문장 자막 자리). 글자·얼굴은 높이 15~85% 안 (일부 피드가 쇼츠 썸네일을 4:5 로 잘라 위아래 약 15%씩 안 보임). 검사 `python3 tools/cover_check.py` (이 줄을 보고 세 칸으로 잼) |
| 시험하는 가설 | 없음 — 쇼츠는 시안 1장. 올린 뒤 스튜디오 '본 비율 vs 넘긴 비율'·관련 동영상 클릭을 네 편끼리 비교 (`economic/guides/shorts_insights.md` 8번) |
| 짝 제목 | `../shorts.md` R3 「건보료 고지서대로 낸 부부 3년에 860만 원 날린다」 (2026-10-17 — 사람 이름을 뺀 제목, `guides/shorts_guide.md` v1.11 4번 5항) |
| 문구 | 제목 「건보료 고지서대로 낸 부부 3년에 860만 원 날린다」을 줄인 말 — 2줄 「건보료 고지서대로 내면 / 3년에 860만 원 날린다」 (v3.0 — 검은 위 칸에 줄마다 가운데 정렬·최대 크기) (동사로 끝, 조사 '에'). '부부'는 그림이 보여 줌 |
| 근거 (`README.md` 3번) | 돈 이야기 성공 쇼츠 표지 66개 (1편 README 3번): 위쪽 머리 글자 2줄 55 · 띠 꼴 51 · 금액 21 · 실사 인물 45 vs 그림 4. 건보료 성공 쇼츠 #28 ×51.25 = 띠 꼴 + 위쪽 2줄(2줄째 노랑에 '건보료') + 진행자 실사 (1개). 니즈 낱말 = 건보료 댓글 362개 👍3,416, 퇴직·은퇴와 함께 물은 것 49 · 👍756 |
| 숫자 근거 | '860만 원' = 고지서대로 내면 퇴직 후 3년 동안 약 860만 원 (쇼츠 대본 문장 10 — 같은 3년 동기 부부는 0원, 롱폼 README 4번) · ⚠️ 롱폼 `checklist.md` C표 1·2 (공단 확인 전 — 보수적 가정) · 2026년 숫자 |
| 인물 나이 | 쇼츠의 최씨 부부 60세 (쇼츠 문장 2·6). 젊어 보이는 50대 중반처럼 그린다. 롱폼 썸네일 부부(밤 거실·회색 니트·분홍 카디건)와 옷·장면을 다르게. 자녀는 그리지 않음 |
| 저장 경로 | `economic/source/toejik-geonbo-2026-10/shorts/thumbnails/thumbnail_1.png` |

## 화면 구성
- 세로 9:16 (1080×1920), **세 칸** (v3.0 — 사용자 지시 2026-10-17 "이미지 외 영역은 검은 배경으로 하고 문구는 두 줄로해서 최대 크기로 맞춰 너가 보내준 ISA 만기 쇼츠 문구 위치 좀 어긋나 있는데 저렇게 하면 안돼 그리고 PC나 모바일에서 볼 때 위 아래 영역이 좀 짤릴 수 있는데 그러면 안돼 프롬프트 수정해봐"):
  - **0~36% — 검은 바탕(#000000) + 문구 2줄**: 줄마다 **가운데 정렬**(두 줄의 가운데 축이 같음 — 어긋나지 않게), 두 줄 같은 크기, **최대 크기 = 긴 줄이 너비 4~96%** (약 102px — 화면 높이의 5.3%). 두 줄 덩어리는 높이 약 19~32% (가운데 약 25% — 15% 선과 사진 사이 가운데), 사진과 3% 넘게 떨어짐 (겹치거나 붙지 않음).
  - **36~72% — 사진 칸** (가로 끝까지, 위아래 경계는 곧은 가로선, 테두리·그라데이션 없음): 인물·물건 — 밝은 낮, 아파트 현관(현관문·신발장이 흐리게).
    - 최씨(너비 약 40~80%, 가슴 위까지): 짧게 정돈한 검은 머리 + 조금 희끗, 베이지 니트 집업 카디건 + 흰 티셔츠. 한 손에 펼친 편지(빈 뒷면이 시청자 쪽)를 힘없이 들고 봄 — 미간을 찌푸리고 이를 악문, 어깨가 처진 **좌절** 얼굴 (v2.1 — 놀라 굳은 얼굴이 아님). 다른 손은 열린 봉투를 아래쪽 앞으로 들고 있음.
    - 아내(최씨 왼쪽 뒤, 너비 약 30~55%): 어깨 길이 짙은 머리, 연보라 블라우스. 남편 팔에 손을 얹고 다른 손은 가슴에, 어깨 너머로 편지를 들여다보며 울상.
    - 봉투(너비 약 8~38%, 높이 약 48~62%, 앞면이 시청자 쪽): 흰 일반 봉투, 앞면에 빨강 띠 + 흰 평면 글자 '건보료 고지서'. 손가락이 글자를 가리지 않게 가장자리를 잡음.
  - **72~100% — 검은 바탕, 빈 칸** (영상에서는 첫 문장 자막이 여기 얹힘 · 유튜브 화면에서는 제목·채널 글씨 자리).
- **안전 구역 = 높이 15~85%** — PC·모바일 일부 피드는 쇼츠 썸네일을 4:5 로 잘라 위아래 약 15%씩 안 보인다. 글자·얼굴·꼬리표는 모두 이 안 (위 0~15%·아래 85~100% 는 잘려도 되는 검정).
- 오른쪽 16% (좋아요·댓글 버튼 자리 — 높이 약 45% 아래): 사진은 이어지고 얼굴·꼬리표 없음.

## 문구 (그대로 사용)
| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 (봉투 앞면) | 건보료 고지서 | 흰 평면 글자 on 빨강 띠 #FF2A2A |
| 위 1줄 | 건보료 고지서대로 내면 | **'건보료' 노랑 #FFD400** · '고지서대로 내면' 흰색 — 검은 바탕, 가운데 정렬 |
| 위 2줄 | 3년에 860만 원 날린다 | **전부 빨강 #FF2A2A + 얇은 흰 외곽선**. 1줄과 같은 크기, 가운데 정렬 |

- 노랑은 중요한 것(주제 낱말 '건보료' — 1줄), 빨강은 나쁜 상황(날리는 돈 — 2줄, 봉투 띠 '건보료 고지서')에만 쓴다.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), high contrast, bold and readable at small size. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
LAYOUT — three stacked zones, each spanning the full width of the canvas:
1. Top zone, from 0% to 36% of the height: flat solid pure black (#000000), with only the headline text on it.
2. Photo panel, from 36% to 72% of the height: one photorealistic photograph filling the full width edge to edge (a wide horizontal picture, about 3:2), with straight horizontal top and bottom edges.
3. Bottom zone, from 72% to 100% of the height: flat solid pure black (#000000), completely empty (a subtitle is added there later in the video).
No gradient or fade between the zones, no border or frame around the photo, no other bands or panels.
SAFE AREA: YouTube crops Shorts thumbnails to about 4:5 in some feeds on phones and PCs, cutting about 15% from the top and 15% from the bottom. Every important thing — all text, every face and word tag — must stay between 15% and 85% of the height.
Headline in the top black zone: exactly TWO lines of very large, heavy, bold Korean text, both lines the same letter size, EACH LINE CENTERED horizontally on the same center axis (the two lines must not be shifted left or right against each other). Make the letters as large as possible: the longer line spans from about 4% to 96% of the width (each letter about 5.3% of the image height tall, roughly 102 px on a 1080x1920 canvas). Vertically, the two-line block is centered between the 15% line and the top of the photo — it sits between about 19% and 32% of the height — with a black gap of at least 3% of the height between the text and the photo. The text never touches or overlaps the photo. Flat letters on the black, no glow, no 3D, no shadow boxes:
line 1 "건보료 고지서대로 내면" — "건보료" in bright yellow #FFD400 and "고지서대로 내면" in white;
line 2 "3년에 860만 원 날린다" — all in bright red #FF2A2A with a thin white outline.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536) with the same three zones (it will be center-cropped to 9:16, cutting about 8% from the left and right), and keep the headline between 12% and 88% of the width.
Scene inside the photo panel (from 36% to 72% of the height, full width), the entrance hall of a Korean apartment in bright daytime, soft daylight, front door and shoe cabinet softly blurred:
- Center-right (between about 40% and 80% of the width): a Korean man aged 60, just retired, who looks youthful for his age, like his mid 50s (short neat black hair with a little gray, beige knit zip-up cardigan over a white T-shirt), shown from the chest up. He holds an unfolded letter up in one hand with its blank back side toward the viewer and stares at it, crushed: he has just realized how much money they are losing, brows knitted in pain, jaw clenched, shoulders slumped, eyes heavy with frustration and regret (face visible, no hand on the forehead). Just behind his left shoulder (about 30% to 55% of the width), his wife aged 60 who looks like her mid 50s (shoulder-length dark hair, light lavender blouse) rests one hand on his arm and the other on her chest, peering at the letter, devastated, brows drawn up. The despair must read clearly even at small thumbnail size, but stay realistic, not cartoonish. Natural, realistic expressions, not exaggerated. Fictional people, not resembling any real or famous person.
- Lower left of the scene (between about 8% and 38% of the width, at about 48% to 62% of the height): in his other hand, held by its edge so no finger covers the words, an opened plain white envelope with its front facing the viewer. On the front there is one flat bright red (#FF2A2A) band with the Korean words "건보료 고지서" printed in huge flat heavy bold white letters. The letters are flat print, not carved, embossed or 3D letter shapes. Nothing else on the envelope: no logos, no institution names, no addresses, no stamps, no barcodes, no numbers.
No children, no ID cards, no forms, no calendars, no money, no charts, no arrows.
Render ONLY the Korean text given in quotes, exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집 프로그램으로)
```
Vertical YouTube Shorts thumbnail background, 9:16 portrait (1080x1920), high contrast. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas. It is also the full-screen opening frame of the Short.
LAYOUT — three stacked zones, each spanning the full width: top zone from 0% to 36% of the height flat solid pure black (#000000), completely empty (a two-line headline will be added later); photo panel from 36% to 72% of the height, one photorealistic photograph filling the full width edge to edge with straight top and bottom edges; bottom zone from 72% to 100% flat solid pure black, empty. No gradient, no fade, no border.
Keep all faces and important objects between 38% and 70% of the height (inside the photo panel).
Photo panel: the entrance hall of a Korean apartment in bright daytime, soft daylight, softly blurred. Center-right (about 40% to 80% of the width): a Korean man aged 60 who looks like his mid 50s (short black hair with a little gray, beige knit zip-up cardigan, white T-shirt), chest up, holding up an unfolded letter with its blank back toward the viewer, crushed, brows knitted in frustration and regret, shoulders slumped (face visible); just behind his left shoulder his wife aged 60 who looks like her mid 50s (shoulder-length dark hair, lavender blouse), hand on his arm, devastated. Fictional people, not resembling any real or famous person. Lower left (about 8% to 38% of the width, 48% to 62% of the height): in his other hand, held by its edge, an opened plain white envelope facing the viewer with one empty flat bright red band across its front. Keep the right 16% of the width free of faces.
If 9:16 is not available, use 2:3 portrait (1024x1536) with the same zones and keep faces inside the middle of the width.
Absolutely no text, letters, numbers, logos or watermarks.
```
- 글자 얹기 (캔바·미리캔버스 등, 1080×1920 기준):
  - 봉투 빨강 띠 안: 건보료 고지서 (흰색, 굵은 고딕)
  - 위 2줄 (검은 위 칸): Noto Sans KR Black(또는 Pretendard Black), 두 줄 같은 크기 약 102px, **줄마다 가운데 정렬**(가운데 x 540 — 긴 줄이 x 43~1037), 두 줄 덩어리의 가운데 y 약 488 (글자 y 약 370~615), 줄 간격 = 글자 크기 × 1.2, 색은 위 '문구' 표대로 (외곽선은 빨강 줄만 얇은 흰색)

## 검수
- [ ] 한글이 한 글자도 틀리지 않았는가: 건보료 고지서 · 건보료 고지서대로 내면 · 3년에 860만 원 날린다 ('료'의 ㄹ, '보'의 ㅗ, '고지서대로'의 ㄹ, '년에'의 '에', '날린다'의 ㄹ 받침까지 확대해서)
- [ ] 1줄 '건보료'만 노랑, '3년에 860만 원 날린다'와 봉투 띠만 빨강인가
- [ ] 세로 9:16 (세로 ÷ 가로 1.78 안팎) — 2:3 이면 가운데 9:16 으로 잘라도 글자·얼굴이 다 남는가
- [ ] **문구 2줄이 검은 위 칸에 최대 크기·가운데인가** (v3.0) — 줄마다 가운데 정렬(두 줄 가운데 축이 같음 — 어긋나지 않음), 긴 줄이 너비 약 4~96%, 글자 높이 약 5.3% (1080 가로에서 약 102px), 사진과 겹치거나 붙지 않음
- [ ] **세 칸 배치인가** — `python3 tools/cover_check.py economic/source/toejik-geonbo-2026-10/shorts/thumbnails/thumbnail_1.png` ✅ (위 0~36%·아래 72~100% 검정, 사진 칸은 가로 끝까지, 글자는 높이 15% 아래·사진과 1.5% 넘게 떨어짐, 줄마다 가운데, 긴 줄 너비 80% 이상)
- [ ] **4:5 로 잘라도(위아래 15%씩) 글자·얼굴·꼬리표가 다 남는가** — PC·모바일 피드
- [ ] 가로 240px 로 줄여도 2줄과 '건보료 고지서'가 읽히는가
- [ ] **손해를 알고 좌절한 얼굴로 보이는가** (v2.1 — 미간을 찌푸리고 어깨가 처진 얼굴, 가로 240px 로 줄여도) — 놀라 굳은 얼굴(눈썹이 올라가고 입이 벌어짐)이면 반려
- [ ] 실존 인물을 닮지 않았는가 · 봉투·편지에 기관 이름·로고·주소·바코드·금액·글자가 없는가 · 자녀·신청서·달력이 없는가
- [ ] 넣지 않는 것이 없는가: '피부양자'·'지역가입자'·'임의계속'·'0원 되는'·'순서' (`README.md` 7번)
- [ ] 롱폼 썸네일(밤 거실·푸른빛·이마를 짚은 남편·'지역가입자' 빨강 상자와 화살표·아래 2줄)과 한눈에 달라 보이는가

## 이미지 검수 (Claude — 지시사항 10번)

### 4차 그림 통과 (2026-10-18 01:50 KST — 사용자 지시 2026-10-18 "썸네일 다시 생성했으니 다시 확인해봐") — `thumbnail_1.png` (ChatGPT 원본 `original/thumbnail_1_chatgpt_2026-10-18.png`)
| 항목 | 결과 |
|---|---|
| 판 | 세 칸 v3.0 프롬프트로 그림 ✅ (ChatGPT 커밋 2026-10-17 16:48Z) |
| 문구·그림 낱말 | 확대해 봄 — 모두 맞음 ✅ |
| 표정 | 손해를 알고 좌절 (입을 가림·미간·처진 어깨) ✅ |
| 배치 | 원본은 문구가 높이 14.3% 부터 — 4:5 로 잘리는 선(15%) 위 ❌ → **`tools/cover_shift.py` 로 문구 칸·사진 칸을 그대로 잘라 아래로 옮김** (문구 위 16.5%, 사진 32.4~72.2% → 34.7~74.4%, 새로 그린 픽셀 없음) → `cover_check.py` ✅ |
| 4:5 로 잘라 봄 | 문구 2줄·얼굴·꼬리표 다 남음 ✅ |

### 3차 그림 반려 (2026-10-18 01:30 KST) — `rejected/thumbnail_1_try2_2026-10-18.png`
- ChatGPT 가 저장소에 올림 (커밋 2026-10-17 16:27Z — 세 칸 프롬프트 v3.0 을 올린 지 9분 뒤). **옛 프롬프트(v2.0)로 그린 그림**: 사진이 화면 끝까지 + 왼쪽 정렬 2줄 (세 칸이 아님 — `tools/cover_check.py` ❌ 사진 칸 0~100%) · 편지를 들고 놀라 굳은 얼굴 (v2.1 '좌절'이 아님) · 문구는 맞음.
- 까닭 (추정): ChatGPT 가 앞서 읽은 파일을 다시 씀 (같은 대화) 또는 main 주소가 몇 분 캐시됨 → 다음부터 **커밋을 고정한 주소 + 새 대화** (`guides/thumbnail_guide.md` 피드백 25).

### 1차 그림 반려 (2026-10-17) — `rejected/thumbnail_1_try1_2026-10-17.png`
- 까닭: ① 위·아래·오른쪽이 빈 남색 (`tools/cover_check.py` ❌ — 영상에서 비율이 틀린 것처럼 보임, 사용자 지시 2026-10-17 "검은색 여백있는건 뭔데") ② 쇼츠 제목이 이름 없는 R3 로 바뀌어 문구도 제목에 맞춤 (사용자 지시 2026-10-17 "나머지도 변경 사항 있으면 썸네일 다시 그리도록 해 그리고 chatgpt 한테 줄 지시사항 변경한거 맞지 다시 확인해"). 아래는 그때 검수 기록.

### 1차 이미지 검수 (2026-10-17, ChatGPT가 저장소에 올림 — Claude 확인)
| 항목 | 결과 |
|---|---|
| 크기 | 941×1672 (9:16) ✅ |
| 한글 | 퇴직 후 안 내도 될 건보료 · 매달 약 30만 원씩 낸다 · 건보료 고지서 — 확대해 봄, 모두 맞음 ✅ |
| 색 | '안 내도 될 건보료' 노랑 · '매달 약 30만 원씩' 빨강 + 흰 외곽선 · '낸다' 흰색 · 봉투 빨강 띠 ✅ |
| 자리 | 글자 2줄 높이 약 12~24% — 윗줄 위 끝이 13% 선보다 약 1% 위 (경미, 쇼츠 위쪽 아이콘과 겹치지 않음) · 오른쪽 끝 가로 약 74% ✅ · 장면 약 25~60% ✅ · 아래 약 40% 빈 남색 ✅ |
| 인물·물건 | 가상 부부, 고지서를 보고 놀란 표정 (문구와 맞음), 기관 이름·로고 없음 ✅ |
| 작게 보기 | 가로 270px 축소본에서 2줄·봉투 글자 읽힘 ✅ |
| **판정** | ✅ 통과 — 쇼츠 첫 문장 화면·썸네일로 씀 |

## 결과 (업로드 후)
| 날짜 | 스튜디오 숫자 (본 비율 vs 넘긴 비율 · 관련 동영상 클릭) | 메모 |
|---|---|---|
