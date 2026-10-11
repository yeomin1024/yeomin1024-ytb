# voyager-2026-10 썸네일 2 — 인물·감정 장면 (학생이 내민 기사)

버전: v1.1 — 2026-10-11 — 사용자 지시: 하단 제목 2줄, 펀치 문구 1개 (thumbnail_guide v1.3) — `space/guides/thumbnail_rules.md` v1.1, 대본 v1.0 기준 (v1.0 — 2026-10-11 — 최초 작성). 빨강 상자 "끝났다더니"는 빼고 하단 1줄의 빨강 단어 "끝났다던"으로 옮김

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 틀린 걸 가르친 가상 강사가 **다섯 달 만에 복구**됐다는 기사를 마주한 당황한 얼굴이 가장 클릭을 부른다 |
| 짝 제목 | `titles.md` **T2** "쇼츠만 믿고 보이저 1호는 끝났다고 했는데 다섯 달 만에 살아났습니다 …" — T1·T3과도 어울림 |
| 숫자 근거 | 문장 1 "보이저 1호가 끝났다는 1분짜리 쇼츠를 봤어요" (0:00) · 문장 3 "서른넷 학원 과학 강사였던 저는" (0:13) · 문장 7 "한 학생이 보이저 1호가 다섯 달 만에 살아났다는 기사를 내밀었어요" (0:39~0:47) → 1분 안 |

## 화면 구성
- 배경: 학원 교실, 뒤에 짙은 초록 칠판 (칠판에는 분필로 그린 단순한 탐사선 그림만, 글자 없음). 약간 어두운 조명
- **위쪽 약 60% (y 0~430)** 안에 인물과 숫자를 넣는다
  - 왼쪽 55%: 30대 중반 가상의 한국 여성 강사 (캐주얼 셔츠, 가슴 위까지), 앞쪽에서 내민 휴대폰을 보며 당황한 표정 (눈을 크게 뜨고 입을 살짝 벌림, 우는 얼굴 아님)
  - 인물 앞 가운데: 학생의 손이 휴대폰을 내밀고 있음 (손만 보임). 휴대폰 화면은 단순한 파란 화면에 작은 탐사선 아이콘만 — 언론사 틀·로고·글자 없음
  - 오른쪽 위: 파랑 상자 **"다섯 달 만에 복구"** (흰 글자, 화면에서 가장 큰 글자 = 핵심 숫자이자 펀치 문구), 상자 왼쪽 끝에 노랑 세로 띠 하나
- **아래쪽 약 35% (y 450~690)**: 아래에서 위로 옅어지는 어두운 띠 위에 하단 제목 2줄 (왼쪽 정렬, x 48부터)
  - 1줄 "쇼츠만 믿고 끝났다던" ("끝났다던"만 빨강) / 2줄 "보이저 1호가 살아났다"
- 오른쪽 아래 구석(약 220×70px)은 비움
- 강조색 2곳: 빨강 "끝났다던" (틀린 말) · 노랑 세로 띠. 파랑 상자는 사실 색

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 위쪽 핵심 숫자·펀치 | 다섯 달 만에 복구 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자, 상자 왼쪽 노랑 #FFD400 세로 띠 하나 |
| 하단 1줄 | 쇼츠만 믿고 끝났다던 | 흰색 + 검정 외곽선 | "끝났다던" 빨강 #E63B2E (틀린 말) |
| 하단 2줄 | 보이저 1호가 살아났다 | 흰색 + 검정 외곽선 | — |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, fact blue #2D6CDF, wrong-information red #E63B2E, cream #F2EBDD.
Bottom-right corner kept empty (video length badge).
A small private-academy classroom in Korea with slightly dim lighting and a dark green chalkboard behind; on the chalkboard
only a simple chalk drawing of a space probe with a dish antenna, no writing. Everything in this paragraph stays in the
upper 60% of the frame: on the left 55%, a fictional Korean woman in her mid-thirties, a science tutor in a casual shirt,
shown from the chest up, looking at a smartphone held out toward her with a surprised, embarrassed expression (wide eyes,
slightly open mouth, not crying). In front of her only a student's hand is visible holding the smartphone; the phone
screen is a plain blue screen with a tiny simple probe icon, no news layout, no logos, no text. Upper right: a large solid
blue (#2D6CDF) box with the big white bold text "다섯 달 만에 복구", the largest text in the image, with one thin bright
yellow (#FFD400) vertical stripe on its left edge.
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "쇼츠만 믿고 끝났다던", line 2 "보이저 1호가 살아났다". The word "끝났다던" is red #E63B2E. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 safe area.
fictional person, not resembling any real or famous person, natural Korean features, realistic photo style.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, highlight yellow #FFD400, fact blue #2D6CDF, wrong-information red #E63B2E.
A small private-academy classroom with slightly dim lighting and a dark green chalkboard showing only a simple chalk
drawing of a space probe, no writing. All picture elements stay in the upper 60% of the frame: on the left 55%, a
fictional Korean woman in her mid-thirties, a science tutor in a casual shirt, chest up, looking at a smartphone held out
by a student's hand in front of her, surprised and embarrassed (wide eyes, slightly open mouth, not crying). The phone
screen is plain blue with a tiny probe icon, no text, no logos. Upper right: an empty large solid blue box with a thin
yellow vertical stripe on its left edge.
The lower third of the frame is a dark band (black to dark navy) fading upward from the bottom edge, completely clean and
empty, for two lines of headline text added later. Bottom-right corner empty.
fictional person, not resembling any real or famous person, natural Korean features, realistic photo style.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "다섯 달 만에 복구" · "쇼츠만 믿고 끝났다던" · "보이저 1호가 살아났다"가 한 글자도 틀리지 않음 (문장 1·7과 같은 말·숫자)
- [ ] 아래쪽에 제목 문구 2줄이 크게 있음 (1줄 11자, 2줄 12자 — 한 줄 14자 이내, 합 23자) · 위쪽 펀치 문구는 "다섯 달 만에 복구" 1개(10자)
- [ ] 인물·휴대폰·파랑 상자가 위쪽 60% 안에 있고 하단 2줄을 가리지 않음 · 2줄째 오른쪽 끝이 x 1040 안
- [ ] 인물이 실존 인물·유명인을 닮지 않음 · 우는 얼굴·과장된 공포 없음 · 30대 중반 여성 (사연자 2023년 서른넷)
- [ ] 휴대폰 화면에 실제 언론사 틀·로고·기사 글자 없음 · 학원 간판·이름 없음
- [ ] 320px 축소본에서 "다섯 달 만에 복구"와 하단 2줄이 읽힘 · 강조색 2곳(빨강 "끝났다던", 노랑 띠) · 틀린 말 빨강, 실제 결과 파랑
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
