# multagi-2026-10 썸네일 2 — 인물·감정 장면

버전: v1.1 — 2026-10-09 — 사용자 지시로 인물 사용, 노후 자금 통장 삭제 → 가상 인물 장면으로 교체 (`guides/thumbnail_guide.md` v1.1, `stock/guides/thumbnail_rules.md` v1.1), 대본 v1.3 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 손실을 확인한 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (성공 썸네일 24개 중 약 20개가 얼굴) |
| 짝 제목 | `titles.md` T2 "본전 금방 온다며 기준 없이 물타서 …" — T1(채택)·T3과도 어울림 |
| 숫자 근거 | 자막 8 "조금만 반등해도 본전이라고 생각했어요" (0:38) · 자막 10 "아침, 눈을 뜨자마자 계좌를 열었더니 -2천만 원이 찍혀 있었어요" (0:47) → 1분 안 |

## 화면 구성
- 다크 네이비 배경. 이른 아침의 어두운 방
- 왼쪽 40~45%: **가상 인물** — 40대 초반 한국인 남성 직장인, 휴대폰을 든 채 다른 손으로 이마를 짚고 굳은 표정
  - 휴대폰 불빛이 얼굴을 비춘다.
  - 휴대폰 화면에는 파란 하락 선만 있다 (앱 화면·글자 없음).
- 오른쪽: 위에 **"본전 오겠지"** (흰 글자, "본전"만 노랑 상자 + 검정 글자), 아래에 파랑 상자 안 **"-2,000만 원"** (흰 글자, 가장 큼)
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 속마음 | 본전 오겠지 | 흰색 #F7F3EA ("본전"만 검정) | "본전"에 노랑 상자 (글자 전체 높이) |
| 결과 | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. Dark navy-toned room in early morning. On the left 40% of the frame, a fictional Korean man in his
early 40s, office-worker look (plain shirt), sitting and holding a smartphone, his other hand on his forehead, frozen
stunned and regretful expression, face lit by the phone's cold light. The phone screen shows only a simple blue line
dropping sharply, no app interface, no text. Fictional person, not resembling any real or famous person, natural Korean
features. On the right side, large bold headline text "본전 오겠지" in off-white, where only the word "본전" sits on a
solid bright yellow (#FFD400) box with black text. Below it, a wide solid blue (#2D6CDF) rounded box with a thin white
border containing the huge white bold text "-2,000만 원", the largest element. No crying, no extreme fear.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF.
Realistic photo style. Dark navy-toned room in early morning. On the left 40% of the frame, a fictional Korean man in his
early 40s, office-worker look, holding a smartphone, other hand on his forehead, stunned and regretful expression, face lit
by the phone's cold light; the phone screen shows only a simple blue line dropping sharply. Fictional person, not
resembling any real or famous person. The right 55% of the frame is calm dark empty space for headline text, with an
empty solid blue (#2D6CDF) rounded box with thin white border in the lower right-middle. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "본전 오겠지" · "-2,000만 원"이 한 글자도 틀리지 않음
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 표정은 당황·후회 수준 (울음·극단적 공포 없음)
- [ ] 휴대폰 화면에 앱 이름·로고·글자 없음 · 종목명 없음
- [ ] 320px 축소본에서 얼굴 표정과 "-2,000만 원"이 읽힘 · 노랑 강조 1곳
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
