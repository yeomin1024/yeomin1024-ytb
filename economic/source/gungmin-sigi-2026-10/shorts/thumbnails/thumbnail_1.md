# gungmin-sigi-2026-10 쇼츠 썸네일 1 — 본안(쇼츠 썸네일 + 첫 문장 화면): 동창 모임 식당에서 친구의 말을 듣고 두 손으로 머리를 감싸 쥔 60세 김 씨 + '평생 30%' 꼬리표

버전: v2.0 — 2026-10-19 — 쇼츠 대본 v2.0(`../gungmin-sigi-2026-10-shorts.txt` — 롱폼 v2.1 의 각색 인물 김 씨) 기준으로 다시. `guides/thumbnail_guide.md` v3.14 12번(재테크 쇼츠 = **세 칸 band**). 옛 v1.0(57세 김씨 · 39만 원)은 git 이력.

| 항목 | 값 |
|---|---|
| 역할 | **본안 — 쇼츠 썸네일 + 첫 문장 화면.** ① 쇼츠 썸네일 (업로드 도구가 API 로 올림 — 안 보이면 앱에서 0초 장면) ② 영상 0:00~첫 문장 끝까지 전체 화면 (확대 없이 — 구운 자막은 아래 검정 칸에 얹힘). 쇼츠는 1장 |
| 시험하는 가설 | 없음 — 쇼츠는 1장 |
| 배치 | `COVER_LAYOUT: band` — **세 칸**: 위 0~36% 검정 + 문구 2줄 · 가운데 36~72% 사진(가로 끝까지) · 아래 72~100% 검정(빈 칸 — 영상에서는 첫 문장 자막 자리). 글자·얼굴·꼬리표는 높이 15~85% 안 (일부 피드가 4:5 로 잘라 위아래 약 15%씩 안 보임). 검사 `python3 tools/cover_check.py` |
| 짝 제목 | `../shorts.md` v2.0 R1 「국민연금 신청서 한 장에 평생 매달 27만 원 덜 받는다」 (R2 를 고르면 1줄만 '국민연금 5년 당긴 60세'로 바꿈) |
| 문구 | 제목을 그대로 두 줄로 — 「국민연금 신청서 한 장에 / 평생 매달 27만 원 덜 받는다」 (Noto Sans KR Black 900 으로 잼: 100px 에서 1줄 989px · 2줄 1,156px → 긴 줄을 너비 96%(1,037px)에 맞추면 **약 89px**, 화면 높이의 4.7%) |
| 조사·뜻 점검 (피드백 21) | 2줄만 읽어도 '평생 매달 27만 원 덜 받는다' = 받는 연금이 줄어듦 ('날린다'가 아니라 '덜 받는다' — 먼저 받는 돈이 있으므로) |
| 근거 | 돈 이야기 성공 쇼츠 표지 66장 중 51장(77%)이 '위 검은 띠 + 큰 글씨 2줄 + 가운데 사진' 꼴 (`economic/source/eunte-kkeonaeseugi-2026-10/shorts/thumbnails/README.md` 3번) · 금액 21/66 · 실사 인물 45/66 · 노후 묶음 걱정 표정 23% vs 7%. 국민연금 받는 시기 쇼츠 표지 근거는 **없음** |
| 숫자 근거 | '27만 원' = 64세 예상 월 90만 원 − 5년 당김 63만 원 (롱폼 문장 14·24, `calc/calc.py` v1.1.1 8번 절) · '평생' = 국민연금법 제61조②·제63조② (5년 당김 1천분의 700, 평생) |
| 인물 나이 | 김 씨 60세 — 젊어 보이는 50대 중반처럼. 옷·곳·몸짓은 롱폼 썸네일(밤 거실 소파·남색 셔츠·이마를 짚음)과 다르게: **저녁 한식당 동창 모임·베이지 니트·두 손으로 머리를 감싸 쥠** |
| 저장 경로 | `economic/source/gungmin-sigi-2026-10/shorts/thumbnails/thumbnail_1.png` |

## 화면 구성
- 세로 9:16 (1080×1920), **세 칸**:
  - **0~36% — 검은 바탕(#000000) + 문구 2줄**: 줄마다 **가운데 정렬**(두 줄의 가운데 축이 같음), 두 줄 같은 크기, **최대 크기 = 긴 줄이 너비 4~96%** (약 89px). 두 줄 덩어리는 높이 약 19~32%, 사진과 3% 넘게 떨어짐.
  - **36~72% — 사진 칸** (가로 끝까지, 위아래 곧은 가로선, 테두리·그라데이션 없음): 저녁, 따뜻한 조명의 한식당 동창 모임(배경에 흐릿한 친구들). 식탁 앞에 앉은 김 씨(너비 약 30~82%, 가슴 위까지): 짧은 검은 머리에 관자놀이가 희끗, 베이지 니트. **두 손으로 머리를 감싸 쥐고 고개를 떨굼**, 눈을 질끈 감고 미간을 찌푸림 (친구의 말로 평생 깎인다는 걸 알게 된 좌절). 얼굴은 손에 다 가리지 않게. 식탁 위 소주잔·반찬 접시(글자 없음).
    - 왼쪽(너비 약 7~28%, 높이 약 40~56%): 말풍선 꼬리표 1개 '평생 30%' — 빨강 둥근 사각형 + 흰 평면 글자, 친구 쪽에서 김 씨 쪽으로 꼬리 (친구가 한 말).
  - **72~100% — 검은 바탕, 빈 칸**.
- **안전 구역 = 높이 15~85%** — 글자·얼굴·꼬리표는 모두 이 안. 오른쪽 16%(높이 45% 아래 버튼 자리)에 얼굴·꼬리표 없음.

## 문구 (그대로 사용)
| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 평생 30% | 흰 평면 글자 on 빨강 말풍선 #FF2A2A |
| 위 1줄 | 국민연금 신청서 한 장에 | **'국민연금' 노랑 #FFD400** · '신청서 한 장에' 흰색 — 두꺼운 검정 외곽선 없이 검정 바탕 위 평면 글자 |
| 위 2줄 | 평생 매달 27만 원 덜 받는다 | **전부 빨강 #FF2A2A** (나쁜 상황) — 1줄과 같은 크기 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), high contrast. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
LAYOUT — three full-width zones: 0–36% of the height flat solid pure black (#000000) with only the headline; 36–72% one photorealistic photograph edge to edge with straight top and bottom edges; 72–100% flat solid pure black, empty. No gradient, fade or border.
SAFE AREA: some feeds crop to about 4:5 — all text, faces and word tags stay between 15% and 85% of the height.
Headline: exactly TWO lines of very large heavy bold Korean text, same size, EACH LINE CENTERED on the same axis, the longer line from about 4% to 96% of the width, the block between about 19% and 32% of the height and at least 3% above the photo; flat letters, no glow, no 3D.
line 1 "국민연금 신청서 한 장에" — "국민연금" in bright yellow #FFD400 and "신청서 한 장에" in white;
line 2 "평생 매달 27만 원 덜 받는다" — all in bright red #FF2A2A.
Photo zone: a warm, softly lit Korean restaurant in the evening, a reunion dinner of old classmates with blurred friends in the background. At the table sits a Korean man aged 60 who looks youthful for his age, like his mid-50s (short black hair with gray at the temples, beige knit sweater), shown from the chest up, centered slightly right (about 30–82% of the width). A friend has just told him his early pension cut lasts for life, and he is crushed: both hands clutching his head, head bowed, eyes squeezed shut, brows knitted — clear frustration, regret and despair that read even at small size. Keep most of his face visible (hands must not cover his eyes and mouth completely). Realistic, not cartoonish. On the table only small soju glasses and side dishes with no labels. Fictional person, not resembling any real or famous person.
On the left of the photo (about 7–28% of the width, 40–56% of the height): one speech-bubble tag, a solid bright red (#FF2A2A) rounded box with the Korean text "평생 30%" printed in large flat heavy bold white letters on its flat front face (flat print, not carved or 3D), its tail pointing from a blurred friend toward the man. Keep the right 16% of the width below 45% of the height free of faces and tags (Shorts buttons).
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536) with the same zones and keep the headline between 12% and 88% of the width.
No money, no bills, no documents with writing, no phones, no logos of any institution or restaurant.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집 프로그램으로)
```
Vertical YouTube Shorts background, 9:16 portrait (1080x1920), high contrast. Three full-width zones: 0–36% flat solid pure black (empty — the headline will be added later); 36–72% one photorealistic photograph edge to edge with straight edges; 72–100% flat solid pure black, empty. No gradient, fade or border.
Photo: a warm Korean restaurant reunion dinner in the evening, blurred friends behind. A Korean man aged 60 who looks like his mid-50s (short black hair with gray temples, beige knit sweater), chest up, about 30–82% of the width, both hands clutching his head, head bowed, eyes squeezed shut, brows knitted in frustration and regret (most of the face visible). Small soju glasses and side dishes on the table. Fictional person, not resembling any real or famous person. On the left (7–28% of the width, 40–56% of the height) one empty solid bright red speech-bubble box with its tail toward the man. All faces and the bubble between 15% and 85% of the height.
Absolutely no text, letters, numbers, logos or watermarks.
```
- 글자 얹기 (캔바·미리캔버스 등): 위 2줄 Noto Sans KR Black 약 89px, 줄마다 가운데, 덩어리 높이 약 19~32% · 말풍선 안 '평생 30%' 흰색 굵은 고딕.

## 검수
- [ ] 글자가 한 글자도 틀리지 않았는가: 국민연금 신청서 한 장에 · 평생 매달 27만 원 덜 받는다 · 평생 30% ('청'의 ㅓ·ㅇ, '받는다'의 ㄴ 받침까지 확대해서)
- [ ] 세 칸이 곧은 가로선으로 나뉘는가 (그라데이션 없음) · `python3 tools/cover_check.py economic/source/gungmin-sigi-2026-10/shorts/thumbnails/thumbnail_1.png` ✅
- [ ] 두 줄이 같은 크기·같은 가운데 축인가 · 긴 줄이 너비 4~96% 안인가 · 2줄째만 빨강인가
- [ ] **좌절로 보이는가** — 두 손으로 머리를 감싸고 고개를 떨군 얼굴 (놀람·고민 아님)
- [ ] 글자·얼굴·말풍선이 높이 15~85% 안인가 · 오른쪽 아래 버튼 자리가 비었는가
- [ ] 실존 인물을 닮지 않았는가 · 식당 간판·로고·지폐가 없는가

## 이미지 검수 (Claude — 지시사항 10번)

## 결과 (업로드 후)
| 날짜 | 실제로 보인 썸네일 (`oardefault.jpg`) | 메모 |
|---|---|---|
