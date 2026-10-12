# molppang-2026-10 썸네일 3 — 검은 배경 제목형 (채택 제목 문구)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.3 4-1, `stock/guides/thumbnail_rules.md` v1.2, 사용자 지시 2026-10-11), 대본 molppang-2026-10.txt v2.1 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 그림 없이 **검은 배경에 채택 제목 앞 문장만** 크게 넣은 글자 썸네일이 사진 썸네일 사이에서 눈에 띄어 클릭을 부른다 |
| 짝 제목 | `titles.md` **T1 (채택)** — 글자가 곧 채택 제목의 앞 문장이다 (titles.md에서는 T3 줄에 "검은 배경 제목형 — 채택 제목 문구"로 적음). 채택 제목이 바뀌면 이 문구도 바꾼다 |
| 숫자 근거 | 문장 4 "천만 원 정도 수익" (0:21) · 문장 7 "갑자기 -2천만 원이 찍힌 겁니다" (0:34) → 1분 안 |

## 화면 구성
- 배경: 순수 검정 #000000 한 가지 (인물·소품·도형·무늬·그라데이션 없음)
- 가운데 정렬 3줄, 글자 높이 약 100px, 줄 간격 1.15, 글자 폭은 화면 폭의 85% 안 (3줄 묶음이 화면 세로 가운데, 약 y 190~530)
- 기본 흰색, 강조는 2곳: 수익 금액 "천만원"(빨강), 손실 금액 "-2천만원"(노랑) — 수익 빨강 → 손실 노랑의 반전만 눈에 띄게
- 외곽선·그림자·빛 효과 없음 · 다른 글자·로고 없음 · 오른쪽 아래 구석(약 220×70) 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 한 종목에만 몰빵해서 | 흰색 #FFFFFF | — (11자) |
| 2줄 | 얻은 천만원 수익이 | "천만원" 빨강 #E63B2E, 나머지 흰색 | 수익 금액 = 빨강 (10자) |
| 3줄 | -2천만원이 됐습니다 | "-2천만원" 노랑 #FFD400, 나머지 흰색 | 손실 금액 = 노랑, 빨강 금지 (11자) |

- 채택 제목 앞 문장 "한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다."를 **글자 그대로** 3줄로 나눴다 (끝 마침표만 뺌). 뒤 문장(결말 장치 "한 종목 올인한 사람들의 최악의 결말")은 넣지 않는다.
- 줄 길이(띄어쓰기 포함): 11자 · 10자 · 11자 — 모두 14자 이내, 어절 단위로 끊음
- 숫자 반전("천만원 수익이 -2천만원이")은 15자라 한 줄에 들어가지 않아 2줄 끝 "천만원 수익이" → 3줄 첫머리 "-2천만원이"로 바로 이어지게 나눴다
- 강조 2곳: 빨강 "천만원"(수익), 노랑 "-2천만원"(손실). 손실 숫자는 빨강으로 쓰지 않는다 (`stock/guides/thumbnail_rules.md` 1번·2번).
- "몰빵해서"는 흰색으로 둔다. 바로 아래 줄의 빨강(수익)과 붙어 빨강의 뜻(이 채널에서는 수익)이 섞이지 않게 하기 위해서다 — 같은 상황(수익 금액이 있는 제목)인 빚투 thumbnail_3과 같은 선택.

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 3 lines with tight line spacing:
line 1 "한 종목에만 몰빵해서", line 2 "얻은 천만원 수익이", line 3 "-2천만원이 됐습니다".
All text pure white (#FFFFFF) except "-2천만원" at the start of line 3 in bright yellow (#FFD400) and "천만원" in line 2 in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 편집 프로그램으로 직접 (이미지 AI 없이 — 캔바·미리캔버스·포토샵 등)
```
캔버스: 1280×720, 배경 #000000 한 가지 (그림·도형·그라데이션 없음)
글꼴: Noto Sans KR Black (또는 Pretendard Black), 글자 높이 약 100px, 줄 간격 1.15, 가운데 정렬, 글자 폭은 화면 폭의 85%(약 1088px) 안
1줄: 한 종목에만 몰빵해서   → 모두 #FFFFFF
2줄: 얻은 천만원 수익이     → "천만원" #E63B2E, 나머지 #FFFFFF
3줄: -2천만원이 됐습니다    → "-2천만원" #FFD400, "이 됐습니다" #FFFFFF
효과: 외곽선·그림자·빛 없음 · 다른 글자·로고 없음 · 오른쪽 아래 220×70 비움
저장: thumbnails/thumbnail_3.png (1280×720, 2MB 이하)
```

## 검수
- [ ] 세 줄을 이으면 채택 제목 앞 문장 "한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다"와 한 글자도 다르지 않음 (끝 마침표만 없음)
- [ ] 배경이 검정 한 가지 · 그림·도형·효과 없음
- [ ] 손실 금액 "-2천만원"은 노랑(빨강 아님), 수익 금액 "천만원"만 빨강 · 강조 2곳 (3곳 이하)
- [ ] 2줄의 "천만원"만 빨강이고 3줄 "-2천만원" 안의 "천만원"은 노랑으로 한 덩어리 (이미지 AI가 자주 섞음)
- [ ] 320px 축소본에서 3줄이 모두 읽힘
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
