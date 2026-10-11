# miraclemorning-2026-10 썸네일 3 — 검은 배경 제목형 (채택 제목 문구)

버전: v2.0 — 2026-10-11 — 사용자 지시: 검은 배경에 채택 제목 문구 그대로 (대비 축 대신) — `guides/thumbnail_guide.md` v1.3 4-1, `selfdev/guides/thumbnail_rules.md` v1.1 2번, 대본 `miraclemorning-2026-10.txt` v1.0 기준 (v1.0: 대비 — 새벽 5시의 나 vs 오후의 나)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 그림 없이 **검은 배경의 채택 제목 문구(글자)만으로** 클릭을 부르는지 — 사진 썸네일 사이에서 오히려 눈에 띄는지 |
| 짝 제목 | `titles.md` **T1 (채택)** "하루 2시간 벌겠다고 새벽 5시에 일어났다가 잠 200시간을 잃었습니다. 미라클모닝 따라 한 사람들의 불편한 진실" — 글자가 곧 이 제목의 앞 문장 |
| 숫자 근거 | 문장 1 "알람을 새벽 5시로 바꿨어요" (0:00) · 문장 6·7 "아침 2시간", "하루가 2시간 늘어난 기분" (0:24~0:36) · 문장 11 "줄어든 잠이 모두 200시간이었어요" (0:50) → 모두 1분 안 |

## 화면 구성
- 1280×720 전체가 순수 검정 #000000 한 가지. 인물·소품·도형·무늬·그라데이션 없음
- 채택 제목 앞 문장을 **글자 그대로** 3줄로 (마침표만 뺌, 뒤 문장 "미라클모닝 따라 한 사람들의 불편한 진실"은 넣지 않음)
  - 원문: 하루 2시간 벌겠다고 새벽 5시에 일어났다가 잠 200시간을 잃었습니다
- 가운데 정렬, 글자 덩어리는 화면 위아래 가운데, 화면 폭의 85% 안, 글자 높이 약 100px, 줄 간격 1.15
- 기본 흰색 #FFFFFF. 강조 2곳: **노랑 "2시간"**(처음 목표 숫자) · **빨강 "200시간"**(잃은 것) — 숫자 반전이 색으로 보인다
- 외곽선·그림자·효과 없음 · 오른쪽 아래 구석(약 220×70px)은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 (11자) | 하루 2시간 벌겠다고 | 흰색 #FFFFFF | "2시간"만 노랑 #FFD400 (처음 목표 숫자) |
| 2줄 (12자) | 새벽 5시에 일어났다가 | 흰색 #FFFFFF | — |
| 3줄 (14자) | 잠 200시간을 잃었습니다 | 흰색 #FFFFFF | "200시간"만 빨강 #E63B2E (잃은 것) |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 3 lines with tight line spacing:
line 1 "하루 2시간 벌겠다고", line 2 "새벽 5시에 일어났다가", line 3 "잠 200시간을 잃었습니다".
All text pure white (#FFFFFF) except "2시간" in bright yellow (#FFD400) and "200시간" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 편집 프로그램으로 직접 (이미지 AI 없이)
- 캔버스 1280×720, 배경 #000000 한 가지 (그 밖에 아무것도 넣지 않음)
- 글꼴 Noto Sans KR Black (또는 Pretendard Black), 글자 높이 약 100px, 줄 간격 1.15, 가운데 정렬
  - 가장 긴 3줄(14자)이 화면 폭 85%(약 1090px)를 넘으면 세 줄 모두 같은 크기로 조금 줄인다 (90px까지)
- 위 "문구" 표의 줄 나눔·색 그대로: 흰색 #FFFFFF, "2시간" 노랑 #FFD400, "200시간" 빨강 #E63B2E. 외곽선·그림자·효과 없음
- 글자 덩어리를 화면 위아래 가운데에 둔다. 오른쪽 아래 220×70px는 비움
- PNG 또는 JPG, 2MB 이하로 `thumbnails/thumbnail_3.png`에 저장

## 검수
- [ ] 글자가 채택 제목 앞 문장과 **글자 그대로** 같음: "하루 2시간 벌겠다고 새벽 5시에 일어났다가 잠 200시간을 잃었습니다" (마침표만 뺌, 숫자 표기 "2시간"·"5시"·"200시간" 같음) — 한 글자도 틀리지 않음, 다른 글자 없음
- [ ] 줄 나눔이 "문구" 표와 같음 (3줄, 한 줄 14자 이내, 어절 중간에서 끊지 않음)
- [ ] 강조 2곳(노랑 "2시간", 빨강 "200시간")뿐 — 3곳 이하, 나머지 흰색 · 색의 뜻: 빨강 = 잃은 것, 노랑 = 처음 목표 숫자 · 파랑 글자 없음
- [ ] 배경은 순수 검정 하나 — 인물·소품·도형·무늬·그라데이션 없음 · 외곽선·그림자·네온 없음 · 로고 없음
- [ ] 320px 축소본에서 세 줄이 모두 읽힘
- [ ] 오른쪽 아래 220×70 비어 있음 · 1280×720, 2MB 이하
- [ ] 채택 제목이 바뀌면 이 문구도 같이 바꿈

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
