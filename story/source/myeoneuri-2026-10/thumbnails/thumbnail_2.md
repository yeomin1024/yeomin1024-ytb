# myeoneuri-2026-10 썸네일 2 — 인물·감정 장면 (메모를 든 사연자)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) · `story/guides/thumbnail_rules.md` v1.2, 대본 `myeoneuri-2026-10.txt` v1.0 기준 (v1.0: 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 손글씨 메모를 든 채 빈 집에 선 **사연자의 허탈한 표정**이 숫자 카드보다 감정을 더 끈다 |
| 짝 제목 | `titles.md` T2 "이 집은 너희 내외 몫이라는 손글씨 한 장 믿고 8년을 모셨는데…" — 하단 2줄은 이 앞 문장을 줄인 것. T1(채택)·T3과도 어울림 |
| 숫자 근거 | 문장 7·8 달력 뒷장 메모, "그 종이 한 장으로 8년을" (0:28~0:33) · 문장 12 "제 몫은 0원" (0:55) · 문장 18 집을 팔고 나옴 → 숫자는 1분 안 |

## 화면 구성
- 오후 햇빛이 드는 **비어 가는 아파트 거실**: 바닥에 테이프로 봉한 이삿짐 상자 몇 개, 가구가 빠진 자리
- **위쪽 약 60% (y 약 48~430)** — 얼굴·손·메모와 글자 상자는 모두 이 안에
  - 왼쪽 45%: **가상 인물** — 50대 중반 한국 여성, 수수한 카디건, 양손에 낡은 달력 종이 한 장을 들고 내려다보며 허탈하고 서운한 표정 (울음 없음). 가슴 위 상반신 구도, 얼굴과 종이는 위 60% 안
  - 뒤쪽 벽에 작은 액자 하나: 나이 든 남성의 **흐릿한 실루엣**만 (얼굴 알아볼 수 없음 — 시아버지)
  - 오른쪽: 파랑 #2D6CDF 둥근 상자 하나 — 위에 작게 **"제 몫은"**, 아래에 크게 **"0원"** (흰 글자, "0원"이 가장 큼)
- **아래쪽 약 35% (y 약 450~690)** — 아래에서 위로 옅어지는 어두운 띠(검정, 불투명 70~90%)가 인물의 아랫몸을 덮고, 그 위에 하단 제목 2줄, 왼쪽 정렬 x 48부터. 2번째 줄은 x 1040 안에서 끝남
- 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 + 핵심 숫자 (위 오른쪽) | 제 몫은 0원 | 흰색 (파랑 #2D6CDF 상자) | "0원"이 가장 큰 글자 |
| 하단 1줄 | 손글씨 한 장 믿고 | 흰색 + 검정 외곽선 | "손글씨 한 장" 노랑 #FFD400 글자 |
| 하단 2줄 | 8년을 모셨는데 | 흰색 + 검정 외곽선 | — |

- 하단 2줄 = T2 앞 문장("이 집은 너희 내외 몫이라는 손글씨 한 장 믿고 8년을 모셨는데")을 줄인 것. 글자 수(띄어쓰기 포함) 10 · 8, 합 18. 결과는 위쪽 "제 몫은 0원"이 보여 준다
- 펀치 "제 몫은 0원"(7자)은 하단 2줄과 겹치는 말이 없다
- 강조 1곳(노랑 글자 "손글씨 한 장"). 빨강 없음 (잃은 몫 0원은 파랑 상자)

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A half-empty Korean apartment living room in soft afternoon light, a few taped cardboard moving
boxes on the floor, pale marks where furniture used to be. On the left 45% of the frame, a fictional Korean woman in her
mid 50s wearing a plain cardigan, chest-up framing, holding one old calendar sheet in both hands and looking down at it
with a hollow, quietly hurt expression (no tears); her face, hands and the sheet are all in the upper 60% of the frame.
Fictional person, not resembling any real or famous person, natural Korean features, realistic photo style.
On the wall behind her, a small framed photo showing only a blurred silhouette of an elderly man, face not recognizable.
The calendar sheet shows only faint illegible handwriting strokes. In the upper right area, one solid blue (#2D6CDF)
rounded box containing white bold text: a smaller line "제 몫은" above a huge "0원", the largest element.
No romance, no funeral, no court, no gavel, no legal form. Keep the face and all text inside the central 16:9 safe area.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "손글씨 한 장 믿고", line 2 "8년을 모셨는데". The word "손글씨 한 장" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, loss blue #2D6CDF.
Realistic photo style. A half-empty Korean apartment living room in soft afternoon light with a few taped moving boxes.
On the left 45% of the frame, a fictional Korean woman in her mid 50s in a plain cardigan, chest-up framing, holding one
old calendar sheet in both hands, looking down at it with a hollow, quietly hurt expression (no tears); her face and the
sheet are in the upper 60% of the frame. Fictional person, not resembling any real or famous person. A small framed photo
on the wall shows only a blurred silhouette of an elderly man. In the upper right area, one empty solid blue (#2D6CDF)
rounded box. The lower third is covered by a dark band that fades upward from the bottom edge, kept clean and empty for
two lines of headline. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "제 몫은 0원" · 하단 "손글씨 한 장 믿고" / "8년을 모셨는데"가 한 글자도 틀리지 않음 (대본 문장 8·12와 같은 숫자)
- [ ] 아래쪽에 하단 2줄이 크게 있음: 한 줄 14자 이내(10·8자), 합 26자 이내(18자), 어절 중간 줄바꿈 없음, 2번째 줄이 x 1040 안에서 끝남
- [ ] 얼굴·메모·파랑 상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 펀치 문구는 "제 몫은 0원" 1개(10자 이내), 하단과 같은 말 없음
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 50대 여성 · 표정은 허탈·서운함 수준 (울음·다툼 없음)
- [ ] 시아버지는 액자 속 흐린 실루엣뿐 · 시아버지·며느리 연애 암시·장례 장면 없음
- [ ] 메모 종이에 읽히는 글자·실제 유언장 서식 없음 · 법원·로고 없음
- [ ] 강조 1곳(노랑 글자), 3곳 이하 · 0원은 파랑 상자 흰 글자 (빨강 없음)
- [ ] 320px 축소본에서 얼굴 표정·"0원"·하단 2줄이 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
