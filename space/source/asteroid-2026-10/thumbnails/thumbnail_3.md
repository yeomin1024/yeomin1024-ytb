# asteroid-2026-10 썸네일 3 — 대비 (쇼츠 속 숫자 / 실제 발표)

버전: v1.0 — 2026-10-11 — 최초 작성 (`space/guides/thumbnail_rules.md` v1.0 2번: 왼쪽 = 첫 뉴스가 준 인상(빨강), 오른쪽 = 실제 기록(파랑)), 대본 asteroid-2026-10.txt v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "역대 최고"라는 쇼츠 문구와 실제 결과를 **나란히 대비**하면 '나도 그 쇼츠 봤는데' 하는 공감이 생겨 클릭을 부른다 |
| 짝 제목 | `titles.md` T3 (짧은 변형) "짐을 다 싸고 나니 확률은 0.004%였습니다. 결국 3.1%가 뒤집힌 진짜 이유" |
| 숫자 근거 | 문장 1·2 "충돌 확률이 3.1%라는 쇼츠 … 확률이 역대 최고라는 내용이었죠" (0:03~0:13) · 문장 11 "엿새 뒤, 충돌 확률은 0.004%" (0:52) → 모두 1분 안 |

## 화면 구성
- 화면을 세로로 반씩 나눈다. 가운데 경계에 노랑 화살표 하나 (왼쪽 → 오른쪽)
- **왼쪽 (빨강 쪽):** 다크 네이비 #14213D 배경 위에 세로로 세운 단순한 휴대폰 실루엣. 화면 안은 빨강 바탕에 흰 글자 **"역대 최고 3.1%"** — 실제 앱·플랫폼 화면 서식 없음
- **오른쪽 (파랑 쪽):** 파랑 #2D6CDF 바탕 큰 카드. 위에 작은 흰 글자 **"엿새 뒤"**, 아래 아주 큰 흰 글자 **"0.004%"**
- 왼쪽 위 구석에 작은 회색 소행성 하나 (부딪히는 장면 없음)
- 오른쪽 아래 구석은 비움 · 인물 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 (쇼츠) | 역대 최고 3.1% | 흰 글자 (빨강 #E63B2E 휴대폰 화면) | — |
| 오른쪽 위 | 엿새 뒤 | 흰 글자 (파랑 카드) | — |
| 오른쪽 결과 | 0.004% | 흰 글자 (파랑 카드) | 가장 큰 글자 |
| 가운데 | (글자 없음) 화살표 | 노랑 #FFD400 | 유일한 강조 |

## [A] 완성형 프롬프트
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

## [B] 글자 없는 프롬프트
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, highlight yellow #FFD400, fact blue #2D6CDF, risk red #E63B2E.
Clean flat editorial illustration, clearly a graphic and not a photo. The frame is split vertically into two halves.
Left half: dark navy space background with a few sparse stars, one small plain grey asteroid in the top-left corner,
and a simple upright smartphone silhouette with an empty solid red screen (no interface, no icons). Right half: a large
empty solid blue (#2D6CDF) card. One thick bright yellow arrow on the dividing line pointing from left to right.
No people, no logos. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "역대 최고 3.1%" · "엿새 뒤" · "0.004%"가 한 글자도 틀리지 않음 (문장 1·2·11)
- [ ] 휴대폰 화면이 실제 쇼츠·앱 화면 서식처럼 보이지 않음 (로고·아이콘·버튼 없음)
- [ ] 위험·과장 = 빨강(왼쪽), 실제 결과 = 파랑(오른쪽) · 노랑 강조는 화살표 1곳
- [ ] 소행성 충돌·폭발 장면 없음 · 320px 축소본에서 "0.004%"가 읽힘 · 오른쪽 아래 비어 있음

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
