# bleach-2026-10 썸네일 2 — 인물·감정 장면 (욕실 문 앞)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) · `lifetips/guides/thumbnail_rules.md` v1.1 5·6번(가상 인물, 입을 가리고 기침하는 정도까지, 세정제를 붓거나 섞는 장면 금지), 대본 `bleach-2026-10.txt` v1.0 기준 (v1.0: 최초 작성)

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 욕실 문 앞에서 입을 가리고 기침하는 **사람의 표정**이 숫자 카드보다 "내 얘기다"를 더 끈다 |
| 짝 제목 | `titles.md` T2 "욕실 문 닫고 락스를 뿌렸다가 1분 꿀팁이 응급실 4시간이 됐습니다 …" |
| 숫자 근거 | 문장 1 "1분이면 곰팡이가 녹는다는 영상" (0:00) · 문장 6 "욕실 문도 꼭 닫았고요" (0:30) · 문장 9 "기침이 멈추지 않더니" (0:44) · 문장 10 "응급실에서 4시간" (0:53) → 모두 1분 안 |

## 화면 구성
- **위쪽 약 60% (y 0~430)** — 실사 느낌. 밝은 흰 타일 욕실 바로 바깥 복도
  - 왼쪽 45%: **가상 인물** — 40대 후반 한국인 여성(집에서 입는 편한 옷, 고무장갑은 벗어 손에 없음), 한 손으로 입을 가리고 기침하며 눈가가 촉촉한 당황·후회 표정. 상반신까지, 서 있음, 얼굴은 위쪽 60% 안
  - 인물 뒤로 반쯤 열린 욕실 문, 그 너머로 하얗게 된 타일 줄눈이 흐릿하게 보임 (세정제 병·분무기는 보이지 않음)
  - 오른쪽: 빨강 상자 안 흰 글자 **"응급실 4시간"** (가장 큰 글자 — 하단 2줄보다 크게)
  - 펀치 문구는 없음 (전 펀치 "문까지 닫았더니"는 하단 1줄 "문 닫고"와 겹쳐서 뺐다 — 닫힌 문 이야기는 하단 2줄이 맡음)
- **아래쪽 약 35% (y 약 450~690)** — 아래에서 위로 옅어지는 어두운 띠(검정 70~90%) 위에 하단 제목 2줄, 왼쪽 정렬(x 48부터): "문 닫고 락스 뿌렸다가" / "1분 꿀팁이 응급실 4시간" ("1분"만 노랑)
- 오른쪽 아래 구석(약 220×70px)은 비움 — 2번째 줄은 x 1040 안에서 끝남

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 핵심 숫자 | 응급실 4시간 | 흰 글자 (빨강 #E63B2E 상자) | 가장 큰 글자 |
| 하단 1줄 | 문 닫고 락스 뿌렸다가 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | — |
| 하단 2줄 | 1분 꿀팁이 응급실 4시간 | 흰색 #FFFFFF + 두꺼운 검정 외곽선 | "1분"만 노랑 #FFD400 글자 (꿀팁이 약속한 시간) |

- 길이: 하단 1줄 12자 · 하단 2줄 14자 (2줄 합 26자) · 펀치 없음
- 하단 2줄은 짝 제목 T2 앞 문장을 줄인 것 ("욕실 문 닫고 락스를 뿌렸다가" → "문 닫고 락스 뿌렸다가", "응급실 4시간이 됐습니다" → "응급실 4시간")
- 강조 합 2곳: 빨강 상자 "응급실 4시간" · 하단 노랑 "1분"

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, safe blue #2D6CDF, cost red #E63B2E.
Bottom-right corner kept empty (video length badge).
Upper 60% of the frame: realistic photo style, soft natural light. A home hallway right outside a small bright
white-tiled bathroom; the bathroom door is half open behind her and the clean white tile grout inside is softly blurred.
On the left 45% of the frame, a fictional Korean woman in her late 40s in comfortable home clothes, shown from the chest
up, covering her mouth with one hand while coughing, eyes slightly watery, embarrassed and regretful expression.
Fictional person, not resembling any real or famous person, natural Korean features. She is standing upright and steady.
No cleaning bottles, no spray bottles, no pouring, no mixing, no smoke, no fumes, no hospital, no ambulance, no oxygen
mask, nobody lying down. On the right side, inside the upper 60%, a wide solid red (#E63B2E) rounded box containing the
huge white bold text "응급실 4시간", the largest text in the image.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "문 닫고 락스 뿌렸다가", line 2 "1분 꿀팁이 응급실 4시간". The word "1분" in line 2 is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep face and text inside the central 16:9 safe area.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, cost red #E63B2E.
Upper 60% of the frame: realistic photo style, soft natural light. A home hallway right outside a small bright
white-tiled bathroom, the door half open behind her with clean white tile grout softly blurred. On the left 45% of the
frame, a fictional Korean woman in her late 40s in comfortable home clothes, shown from the chest up, covering her mouth
with one hand while coughing, eyes slightly watery, embarrassed and regretful expression, standing upright.
Fictional person, not resembling any real or famous person. No bottles, no smoke, no hospital, no oxygen mask.
On the right, inside the upper 60%, an empty wide solid red (#E63B2E) rounded box.
Lower third: a dark band that fades upward from the bottom edge across the full width, with clean empty space for two
lines of large left-aligned headline text. Nothing else in the lower third. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "응급실 4시간" · "문 닫고 락스 뿌렸다가" · "1분 꿀팁이 응급실 4시간"이 한 글자도 틀리지 않음 (문장 1·6·10, 제목 T2와 같은 숫자)
- [ ] 아래쪽 약 35% 안에 하단 2줄이 크게 있음 (12자·14자, 한 줄 14자·합 26자 이내) · 줄바꿈 위치가 "문구" 표와 같음 · 2번째 줄이 오른쪽 아래 구석 전에 끝남
- [ ] 위쪽 그림 영역에는 "응급실 4시간" 하나만 있음 (펀치 문구 없음) · 인물과 빨강 상자가 위쪽 60% 안에 있어 하단 2줄을 가리지 않음
- [ ] 인물이 실존 인물·유명인·살림 유튜버를 닮지 않음 · 표정은 당황·후회 수준 · 서 있음 (쓰러짐·병원 침대·산소마스크·구급차·연기 없음)
- [ ] 세정제 병·분무기·붓는 장면이 보이지 않음 (`thumbnail_rules.md` 6번)
- [ ] 320px 축소본에서 표정, "응급실 4시간", 하단 2줄이 읽힘 · 노랑·빨강 강조 합 2곳 ("1분" 노랑 = 꿀팁 약속, "응급실 4시간" 빨강 = 위험 결과) · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
