# nuriho-2026-10 썸네일 3 — 대비 (2021 실패 1번 / 2026 성공 4번)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `space/guides/thumbnail_rules.md` v1.0), 대본 v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 첫 뉴스가 준 인상(실패 1번)과 실제 기록(성공 4번)을 **좌우로 나란히** 보여 주면, "내가 아는 건 왼쪽뿐"이라는 궁금증이 생긴다 |
| 짝 제목 | `titles.md` T3 (짧은 변형) "누리호 실패 뉴스에 아들 꿈을 말렸습니다. 결국 …" — T1과도 어울림 |
| 숫자 근거 | 문장 4 "위성 모사체가 궤도에 오르지 못했다는 뉴스" (0:18) · 문장 10 "2022년부터 4번 연속 성공" (0:52) · 문장 60 "5번 중 4번, 성공률 80%" (5:39) → 핵심 대비는 1분 안 |

## 화면 구성
- 화면을 세로로 반씩 나눈다 (가운데 가는 흰 선)
- **왼쪽 (빨강 쪽):** 어두운 네이비 하늘 높은 곳에서 3단 로켓의 마지막 단 엔진 불꽃이 꺼져 가는 모습 (작은 불꽃이 사그라짐, 폭발 아님). 왼쪽 위 빨강 상자에 **"실패 1번"**
- **오른쪽 (파랑 쪽):** 지구 위 궤도에서 작은 위성들이 차례로 펼쳐져 나오는 모습. 오른쪽 위 파랑 상자에 **"성공 4번"**
- 가운데 선 위에 노랑 화살표 하나 (왼쪽 → 오른쪽)
- 로켓·위성에 국기·글자·로고 없음 · 그림·일러스트 느낌 · 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 | 실패 1번 | 흰색 (빨강 #E63B2E 상자) | — |
| 오른쪽 | 성공 4번 | 흰색 (파랑 #2D6CDF 상자) | 노랑 #FFD400 화살표 하나 (유일한 강조) |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact/success blue #2D6CDF, failure red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean illustrated style (clearly an illustration, not a photo). The frame is split vertically into two equal halves by a
thin white line. LEFT half: dark navy (#14213D) sky high above the clouds, the small upper stage of a generic plain rocket
whose engine flame is fading out and shrinking (no explosion, no debris), slightly reddish tint. At the top-left, a solid
red (#E63B2E) box with the large white bold text "실패 1번". RIGHT half: Earth's curved horizon below and several small
generic satellites being released one after another into orbit, calm blue tint. At the top-right, a solid blue (#2D6CDF)
box with the large white bold text "성공 4번". One bright yellow (#FFD400) arrow on the center line pointing from left to
right. No flags, no letters or logos on the rocket or satellites, no people, no spacesuits. Keep all text inside the
central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Clean illustrated style. Frame split vertically into two halves by a thin white line. Left half: dark navy sky high above
the clouds, the small upper stage of a generic plain rocket whose engine flame is fading out (no explosion), reddish tint,
with an empty solid red box at the top-left. Right half: Earth's curved horizon and several small generic satellites being
released into orbit, blue tint, with an empty solid blue box at the top-right. One yellow arrow on the center line pointing
right. No flags, no logos, no people. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "실패 1번" · "성공 4번"이 한 글자도 틀리지 않음 (1차 실패, 2~5차 성공 = 문장 10·60)
- [ ] 왼쪽은 엔진 불꽃이 꺼지는 장면이지 폭발이 아님 (1차는 폭발하지 않았다)
- [ ] 로켓·위성에 국기·글자·기관 로고 없음 · 실제 우주 사진처럼 보이지 않음
- [ ] 320px 축소본에서 두 문구가 읽힘 · 노랑 강조 1곳 · 실패 빨강 / 성공 파랑
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
