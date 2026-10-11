# nuriho-2026-10 썸네일 3 — 검은 배경 제목형 (채택 제목 문구)

버전: v2.0 — 2026-10-11 — 사용자 지시: 검은 배경에 채택 제목 문구 그대로 (대비 축 대신) — `guides/thumbnail_guide.md` v1.3 4-1, `space/guides/thumbnail_rules.md` v1.1, 대본 v1.0 기준 (v1.0 — 2026-10-11 — 대비: 2021 실패 1번 / 2026 성공 4번)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 그림 없이 검은 배경에 채택 제목 앞 문장만 크게 넣은 **글자만으로** 클릭을 부르는지 (사진·일러스트 썸네일 사이에서 눈에 띄는지) |
| 짝 제목 | `titles.md` **T1 (채택)** "46초 모자란 실패에 아들 꿈을 말렸는데 누리호는 4번 연속 성공했습니다. 첫 실패만 본 사람들의 공통점" — 글자가 곧 채택 제목 |
| 숫자 근거 | 문장 8 "46초가 모자랐던 장면 하나였습니다" (0:40) · 문장 10 "2022년부터 4번 연속 성공이었죠" (0:52) · 문장 13~14 521초 중 475초, 46초 모자람 (1:09~1:20) → 핵심 숫자 둘 다 1분 안 |

## 화면 구성
- 배경: 순수 검정 #000000 한 가지. 인물·로켓·도형·무늬·그라데이션 없음
- 글자: 채택 제목의 앞 문장을 **글자 그대로** 4줄로, 가운데 정렬, 화면 폭의 85% 안
- 강조 2곳: 빨강 "실패" (처음 겁준 말) · 노랑 "4번 연속 성공" (실제 결과). 검정 위 파랑 글자는 쓰지 않는다
- 오른쪽 아래 구석(약 220×70px)은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1줄 | 46초 모자란 실패에 | 흰색 #FFFFFF | "실패" 빨강 #E63B2E |
| 2줄 | 아들 꿈을 말렸는데 | 흰색 #FFFFFF | — |
| 3줄 | 누리호는 | 흰색 #FFFFFF | — |
| 4줄 | 4번 연속 성공했습니다 | 흰색 #FFFFFF | "4번 연속 성공" 노랑 #FFD400 |

- 이어 붙이면 "46초 모자란 실패에 아들 꿈을 말렸는데 누리호는 4번 연속 성공했습니다" = 채택 제목 앞 문장 (마침표만 뺌)

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720). Plain solid pure black background (#000000) and nothing else: no people, no objects, no shapes, no gradients, no texture, no effects.
Only huge heavy bold Korean typography, centered, about 85% of the frame width, 4 lines with tight line spacing:
line 1 "46초 모자란 실패에", line 2 "아들 꿈을 말렸는데", line 3 "누리호는", line 4 "4번 연속 성공했습니다".
All text pure white (#FFFFFF) except "4번 연속 성공" in bright yellow (#FFD400) and "실패" in red (#E63B2E). No outlines, shadows or glow.
Bottom-right corner kept empty (video length badge).
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 편집 프로그램으로 직접 (이미지 AI 없이)
- 캔바·미리캔버스·포토샵 등에서 새 캔버스 **1280×720**, 배경 **#000000** 한 가지
- 글꼴 **Noto Sans KR Black** (또는 Pretendard Black), 글자 높이 약 **100px**, 줄 간격 **1.15**, **가운데 정렬**, 4줄 묶음을 화면 가운데에
- 색은 "문구" 표대로: 기본 흰색 #FFFFFF, "실패"만 빨강 #E63B2E, "4번 연속 성공"만 노랑 #FFD400
- 외곽선·그림자·빛 효과 없음 · 오른쪽 아래 **220×70** 구석은 비움
- PNG 또는 JPG로 내보내기 (2MB 이하)

## 검수
- [ ] 4줄을 이어 붙이면 채택 제목 앞 문장과 **한 글자도 다르지 않음** ("46초 모자란 실패에 아들 꿈을 말렸는데 누리호는 4번 연속 성공했습니다")
- [ ] 줄마다 14자 이내 (11 · 10 · 4 · 12자), 어절 중간에서 끊지 않음, "4번 연속 성공했습니다"가 한 줄
- [ ] 강조 2곳(빨강 "실패", 노랑 "4번 연속 성공") — 3곳 이하 · 빨강 = 처음 겁준 말, 노랑 = 실제 결과 · 파랑 글자 없음
- [ ] 배경은 검정 하나뿐 (인물·로켓·도형·그라데이션·효과 없음)
- [ ] 320px 축소본에서 4줄이 모두 읽힘
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
