# isa-mangi-2026-10 썸네일 3 — 실험안 ②: 사람 없이, 금이 간 유리 저금통에서 지폐가 새고 '세금'이 내리누름

버전: v1.0 — 2026-10-16 — 대본 isa-mangi-2026-10.txt v1.0 기준. 사용자 지시(`thumbnail_1.md` 버전 줄과 같음). 근거: `README.md`.

| 항목 | 값 |
|---|---|
| 역할 | **실험안 ②** — 본안과 하단 2줄·꼬리표는 같고, 그림에 **사람이 없다** |
| 시험하는 가설 | 사람 없이 새어 나가는 돈과 '세금' 낱말만으로도 클릭을 부른다 |
| 짝 제목 | titles.md R1 |
| 문구 | 본안과 같다: 50·60대 ISA 만기 돈 연금저축 / 안 옮기면 3년에 96만 원 손해 |
| 근거 (`README.md` 3번) | ISA 묶음 사람 없는 썸네일 성공 4/10 vs 기준 밖 0/5 (S2 ×30.1 · S3 ×14.3 · S9 · S11). 노후·연금·절세 묶음 18% vs 7%. 세 영상(기초연금·ISA·건보료) 모두 ②를 '사람 없음'으로 두어 결과를 함께 본다. 저금통이 새는 장면은 성공 자료에 없다 → 실험 |
| 숫자 근거 | 본안과 같다 (`thumbnail_1.md`) |

## 화면 구성
- **위쪽 약 62%**:
  - 가운데 오른쪽: 밤 책상 위 커다란 유리 저금통(뚜껑 있는 유리병). 일반 지폐(초상·숫자·무늬 없음)가 가득하다.
    - 병 아래쪽에 금이 가 있고, 그 틈으로 지폐가 새어 나와 책상 아래로 흘러내린다.
  - 왼쪽: 본안과 같은 빨강 꼬리표 '세금' (흰 평면 글자), 굵은 빨강 화살표 2개가 병 뚜껑을 내리누르듯 아래로 향한다.
  - 배경: 어두운 밤 사무실, 흐리게, 차가운 푸른빛. 병에 따뜻한 스포트라이트.
- **아래쪽 약 35%**: 본안과 같은 하단 2줄.
- 오른쪽 아래 구석은 비운다.

## 문구 (그대로 사용)
| 자리 | 문구 | 색 |
|---|---|---|
| 그림 낱말 | 세금 | 흰 글자 on 빨강 상자 #FF2A2A |
| 하단 1줄 | 50·60대 ISA 만기 돈 연금저축 | '50·60대' 흰색 · **'ISA 만기 돈 연금저축' 노랑 #FFD400** — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 안 옮기면 3년에 96만 원 손해 | '안 옮기면' 흰색 + 검정 외곽선 · **'3년에 96만 원 손해' 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄과 같은 크기 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, dramatic, high contrast, bold and readable at small size. No people in the image.
Upper 62% of the frame:
- Center-right: a large glass savings jar with a lid, standing on a desk at night, filled with plain generic banknotes with no portraits, no numbers and no patterns. The bottom of the jar is cracked, and banknotes are leaking out through the crack and spilling off the edge of the desk.
- Left side: one bold word tag, a solid bright red (#FF2A2A) rounded box with the Korean word "세금" printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes). Two thick bright red arrows point from the tag down onto the jar's lid, as if pressing on it.
- Background: a dark office at night, softly blurred, cool blue tones; a warm spotlight on the jar.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold text, left-aligned near the left edge, both lines the same size:
line 1 "50·60대 ISA 만기 돈 연금저축" — "50·60대" in white and "ISA 만기 돈 연금저축" in bright yellow #FFD400, all with a thick black outline (keep the middle dot "·" between 50 and 60, and write ISA in capital Latin letters);
line 2 "안 옮기면 3년에 96만 원 손해" — "안 옮기면" in white with a thick black outline, and "3년에 96만 원 손해" in bright red #FF2A2A with a thick white outline.
The second line ends well before the bottom-right corner; keep the bottom-right corner empty for the video length badge. Keep the jar, the banknotes and the word tag in the upper part so they never cover the bottom title.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text inside the central 16:9 area, at least 8% away from the top and bottom edges.
Render ONLY the text given in quotes (Korean, plus the Latin letters ISA), exactly as written with the same letters and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때)
```
YouTube thumbnail background, 16:9 landscape (1280x720), photorealistic, dramatic, high contrast. No people.
Upper 62%: center-right, a large lidded glass savings jar on a desk at night, full of plain generic banknotes (no portraits, no numbers, no patterns), cracked at the bottom with banknotes leaking out and spilling off the desk. On the left, one empty solid bright red rounded box with two thick red arrows pointing down onto the jar's lid. Background: dark office at night, softly blurred, cool blue tones, warm spotlight on the jar.
Lower third: a dark band fading upward from the bottom edge, left empty for a two-line headline.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
- 글자 얹기: 빨강 상자 안 '세금', 하단 2줄은 `thumbnail_1.md`와 같다.

## 검수
- [ ] 글자가 한 글자도 틀리지 않았는가: 세금 · 50·60대 ISA 만기 돈 연금저축 · 안 옮기면 3년에 96만 원 손해
- [ ] 사람이 없는가 · 지폐에 초상·숫자·무늬가 없는가 · 병에 글자·상표가 없는가
- [ ] 가로 320px로 줄여도 2줄과 '세금'이 읽히는가 · 글자가 가운데 16:9 안 · 오른쪽 아래 구석 비움

## 이미지 검수 (Claude — 지시사항 10번)

### 1차 이미지 검수 (2026-10-16, ChatGPT가 저장소에 올림 — Claude 확인)
| 항목 | 결과 |
|---|---|
| 크기 | 1672×941 (1.777, 16:9) ✅ — JPG 변환 시험 218KB |
| 한글 | 꼬리표 「세금」, 하단 「50·60대 ISA 만기 돈 연금저축」 / 「안 옮기면 3년에 96만 원 손해」 — 문구표와 같음 ✅ |
| 색 | 'ISA 만기 돈 연금저축'만 노랑, '3년에 96만 원 손해'만 빨강+흰 외곽선, 「세금」 빨강 상자+흰 글자, 화살표 빨강 ✅ |
| 자리 | 1줄 윗선 = 아래 34%, 2줄 아랫선 = 6.8% (16:9라 잘림 없음) ✅ · 2줄째 끝 1280 기준 x 1033 → 구석 칸 앞에서 끝남, 구석에는 흩어진 지폐뿐(글자 없음) ✅ |
| 인물·물건 | 사람 없음 ✅ · 밤 책상 위 뚜껑 있는 큰 유리병, 아래쪽 금 간 곳으로 지폐가 새어 나와 책상 밖으로 흘러내림 ✅ · 화살표 2개가 뚜껑을 내리누름 ✅ · 병에 글자·상표 없음, 지폐는 옅은 테두리 무늬만(초상·숫자 없음) ✅ · 스탠드·연필꽂이·모니터에도 글자 없음 ✅ |
| 320px | 2줄과 「세금」 모두 읽힘 ✅ |
| **판정** | ✅ 통과 (실험안 ②) |
- 재는 법: 원본에서 하단 2줄과 그림 속 낱말을 잘라 3~4배로 키워 한 글자씩 봄. '구석 칸' = 1280×720 기준 오른쪽 아래 220×70 (x 1060~, y 650~). '길이 표시 시험' = 가로 320·360·400px로 줄인 뒤 영상 길이 표시(320px 기준 약 38×18px, 가장자리 4px)를 얹어 2줄째 마지막 글자가 가려지는 비율을 셈.

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
