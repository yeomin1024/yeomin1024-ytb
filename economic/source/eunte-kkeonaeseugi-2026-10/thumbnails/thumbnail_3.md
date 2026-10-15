# eunte-kkeonaeseugi-2026-10 썸네일 3 — 실험안 ②: 사람 없이 '세금'·'건보료' 글자가 노후 자금을 내리찍는 장면

버전: v4.0 — 2026-10-15 — 대본 eunte-kkeonaeseugi-2026-10.txt v1.2 기준. 사용자 지시(`thumbnail_1.md` 버전 줄과 같음) "나머지 2개는 좀 실험적인걸로". 근거: `README.md`.

| 항목 | 값 |
|---|---|
| 역할 | **실험안 ②** — 본안과 하단 2줄은 같고, 그림에 **사람이 없다** |
| 시험하는 가설 | 사람 얼굴 없이 '세금'·'건보료' 글자가 돈을 부수는 장면만으로도 클릭을 부른다 |
| 짝 제목 | titles.md R1 |
| 문구 | 본안과 같다: 연금 꺼내는 순서 모르면 / 평생 2천만 원 손해 |
| 근거 (`README.md` 3번) | 사람 없는 썸네일: 성공 18% vs 기준 밖 7% (#8 ×221, #38 ×37 — 단 이 둘은 글자가 화면 가득한 꼴). 성공 #133 ×5.9은 돈다발에 빨강 화살표와 '세금 폭탄' 꼬리표를 붙였다. **글자가 돈을 부수는 장면 자체는 성공 자료에 없다** → 실험 |
| 숫자 근거 | 본안과 같다 (`thumbnail_1.md`) |

## 화면 구성
- **위쪽 약 62%**: 어두운 극적 배경, 가운데에 스포트라이트.
  - 가운데 아래쪽: 가지런히 쌓인 돈다발 더미. 무늬를 알아볼 수 없는 일반 지폐로, 실제 화폐 도안은 쓰지 않는다.
  - 위에서 거대한 입체 글자 '세금'(왼쪽)과 '건보료'(오른쪽)가 쾅 내려와 돈다발을 내리찍는다.
    - 입체 글자는 반짝이는 빨강 #FF2A2A이고 흰 모서리가 있다.
    - 돈다발은 찌그러지고, 지폐가 사방으로 흩날린다. 움직임 흔적과 먼지를 넣는다.
- **아래쪽 약 35%**: 본안과 같은 하단 2줄.
- 오른쪽 아래 구석은 비운다.

## 문구 (그대로 사용)
| 자리 | 문구 | 색 |
|---|---|---|
| 입체 글자 1 (왼쪽) | 세금 | 빨강 #FF2A2A, 흰 모서리 |
| 입체 글자 2 (오른쪽) | 건보료 | 같음 |
| 하단 1줄 | 연금 꺼내는 순서 모르면 | **'연금 꺼내는 순서' 노랑 #FFD400** · '모르면' 흰색 — 모두 두꺼운 검정 외곽선 |
| 하단 2줄 | 평생 2천만 원 손해 | '평생' 흰색 + 검정 외곽선 · **'2천만 원 손해' 빨강 #FF2A2A + 두꺼운 흰 외곽선**. 1줄보다 조금 크게 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic dramatic product-style shot, high contrast, bold and readable at small size. No people.
Upper 62% of the frame: a dark dramatic background with a spotlight in the center. In the lower center of this area, a neat tall stack of generic paper banknotes (no readable currency design, no real money artwork). Two gigantic glossy 3D Korean words, "세금" on the left and "건보료" on the right, in bright red (#FF2A2A) with white edges, slam down from above onto the money stack, crushing it; banknotes burst and fly out in all directions, with motion streaks and dust.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge:
line 1 "연금 꺼내는 순서 모르면" — "연금 꺼내는 순서" in bright yellow #FFD400 and "모르면" in white, both with a thick black outline;
line 2 "평생 2천만 원 손해", slightly larger than line 1 — "평생" in white with a thick black outline, and "2천만 원 손해" in bright red #FF2A2A with a thick white outline.
The second line ends well before the bottom-right corner; keep the bottom-right corner empty for the video length badge. Keep the 3D words and the money in the upper part so they never cover the bottom title.
If the canvas is not exactly 16:9, keep all text inside the central 16:9 area, at least 8% away from the top and bottom edges.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때)
```
YouTube thumbnail background, 16:9 landscape (1280x720), photorealistic dramatic product-style shot, high contrast. No people.
Upper 62%: dark dramatic background with a central spotlight; a neat tall stack of generic paper banknotes (no readable currency design) being crushed from above by two gigantic glossy bright red blocks with white edges and smooth flat front faces (words will be added later), banknotes bursting and flying out, motion streaks and dust.
Lower third: a dark band fading upward from the bottom edge, left empty for a two-line headline.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
- 글자 얹기: 빨강 덩어리 앞면에 흰색 굵은 고딕 '세금'(왼쪽)·'건보료'(오른쪽). 하단 2줄은 `thumbnail_1.md`와 같다.

## 검수
- [ ] 한글이 한 글자도 틀리지 않았는가: 세금 · 건보료 · 연금 꺼내는 순서 모르면 · 평생 2천만 원 손해
- [ ] 지폐에 실제 화폐 도안(인물·숫자·은행 이름)이 보이지 않는가
- [ ] 하단 2줄이 본안과 글자·색이 같은가
- [ ] 320px로 줄여도 '세금'·'건보료'와 2줄이 읽히는가 · 글자가 가운데 16:9 안에 있는가
- [ ] 오른쪽 아래 구석이 비어 있는가

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
