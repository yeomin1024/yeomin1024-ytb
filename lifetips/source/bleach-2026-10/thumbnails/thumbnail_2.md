# bleach-2026-10 썸네일 2 — 인물·감정 장면 (욕실 문 앞)

버전: v1.0 — 2026-10-11 — 최초 작성 (`lifetips/guides/thumbnail_rules.md` v1.0 5·6번: 가상 인물, 입을 가리고 기침하는 정도까지, 세정제를 붓거나 섞는 장면 금지)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 욕실 문 앞에서 입을 가리고 기침하는 **사람의 표정**이 숫자 카드보다 "내 얘기다"를 더 끈다 |
| 짝 제목 | `titles.md` T2 "욕실 문 닫고 락스를 뿌렸다가 1분 꿀팁이 응급실 4시간이 됐습니다 …" |
| 숫자 근거 | 문장 6 "욕실 문도 꼭 닫았고요" (0:31) · 문장 9 "기침이 멈추지 않더니" (0:44) · 문장 10 "응급실에서 4시간" (0:53) |

## 화면 구성
- 실사 느낌. 밝은 흰 타일 욕실 바로 바깥 복도. 왼쪽 45%: **가상 인물** — 40대 후반 한국인 여성(집에서 입는 편한 옷, 고무장갑은 벗어 손에 없음), 한 손으로 입을 가리고 기침하며 눈가가 촉촉한 당황·후회 표정
- 인물 뒤로 반쯤 열린 욕실 문, 그 너머로 하얗게 된 타일 줄눈이 흐릿하게 보임 (세정제 병·분무기는 보이지 않음)
- 오른쪽 50%: 위에 **"문까지 닫았더니"** (잉크 글자, "문까지"만 노랑 상자), 아래에 빨강 상자 안 흰 글자 **"응급실 4시간"** (가장 큼)
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 행동 | 문까지 닫았더니 | 잉크 #1E1E1E ("문까지"만 노랑 상자) | 노랑 상자 (글자 전체 높이, 유일한 강조) |
| 결과 | 응급실 4시간 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |

## [A] 완성형 프롬프트
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, safe blue #2D6CDF, cost red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style, soft natural light. A home hallway right outside a small bright white-tiled bathroom; the bathroom
door is half open behind her and the clean white tile grout inside is softly blurred. On the left 45% of the frame, a
fictional Korean woman in her late 40s in comfortable home clothes, covering her mouth with one hand while coughing,
eyes slightly watery, embarrassed and regretful expression. Fictional person, not resembling any real or famous person,
natural Korean features. She is standing upright and steady. No cleaning bottles, no spray bottles, no pouring, no
mixing, no smoke, no fumes, no hospital, no ambulance, no oxygen mask, nobody lying down. On the right side, bold
headline text "문까지 닫았더니" in ink black, where only the word "문까지" sits on a solid bright yellow (#FFD400) box of
full letter height. Below it, a wide solid red (#E63B2E) rounded box containing the huge white bold text "응급실 4시간",
the largest element. Keep face and text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, cost red #E63B2E.
Realistic photo style, soft natural light. A home hallway right outside a small bright white-tiled bathroom, the door
half open behind her with clean white tile grout softly blurred. On the left 45% of the frame, a fictional Korean woman
in her late 40s in comfortable home clothes, covering her mouth with one hand while coughing, eyes slightly watery,
embarrassed and regretful expression, standing upright. Fictional person, not resembling any real or famous person.
No bottles, no smoke, no hospital, no oxygen mask. The right 50% of the frame is calm empty space for headline text,
with an empty solid red (#E63B2E) rounded box in the lower right-middle. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "문까지 닫았더니" · "응급실 4시간"이 한 글자도 틀리지 않음
- [ ] 인물이 실존 인물·유명인·살림 유튜버를 닮지 않음 · 표정은 당황·후회 수준 · 서 있음 (쓰러짐·병원 침대·산소마스크·구급차·연기 없음)
- [ ] 세정제 병·분무기·붓는 장면이 보이지 않음 (`thumbnail_rules.md` 6번)
- [ ] 320px 축소본에서 표정과 "응급실 4시간"이 읽힘 · 노랑 강조 1곳 · 오른쪽 아래 비어 있음

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
