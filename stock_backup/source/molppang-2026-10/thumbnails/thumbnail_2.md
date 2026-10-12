# molppang-2026-10 썸네일 2 — 인물·감정 장면 (계좌를 확인한 밤)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.3, `stock/guides/thumbnail_rules.md` v1.2), 대본 molppang-2026-10.txt v2.1 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 전 재산을 넣은 계좌를 확인한 순간의 **사람 표정**이 숫자 카드보다 감정을 더 끈다 (성공 썸네일 24개 중 약 20개가 감정이 드러난 얼굴) |
| 짝 제목 | `titles.md` T2 "좋은 종목이라 확신하고 전 재산 몰빵했다가 …" — T1(채택)·T3과도 어울림 |
| 숫자 근거 | 문장 3 "좋은 종목이라고 확신하고 전 재산 7천만 원을 이 종목에 몰빵" (0:15) · 문장 4 "천만 원 정도 수익" (0:21) · 문장 7 "어느 날 계좌를 확인해 보니 갑자기 -2천만 원이 찍힌 겁니다" (0:34) → 장면과 숫자 모두 1분 안 |

## 화면 구성
- 밤, 불이 거의 꺼진 부엌 식탁. 전체 톤은 다크 네이비
- 오른쪽 절반: **가상 인물** — 30대 후반 한국인 여성 직장인 (사연을 읽는 목소리가 여성이라 맞춤), 식탁에 앉아 두 손으로 든 휴대폰을 들여다보며 굳은 표정(허탈·후회), 휴대폰 불빛이 얼굴을 비춘다
  - 얼굴·손·휴대폰은 위쪽 약 60% 안. 몸 아래쪽은 하단 어두운 띠 속으로 사라진다
  - 휴대폰 화면에는 단순한 파란 하락 선 하나만 (앱 화면·글자·로고 없음)
- 왼쪽 위: 파랑 상자(흰 얇은 테두리) 안에 **"-2,000만 원"** (흰 글자, 가장 큰 글자 — 화면 높이 약 20%)
- 아래쪽 약 35% (y 450~690): 아래에서 위로 옅어지는 검정 띠 + **하단 제목 2줄** (왼쪽 정렬 x 48부터, 2번째 줄은 x 1040 안에서 끝남)
- 오른쪽 아래 구석(약 220×70)은 어둡게 비움 · 우는 얼굴·극단적 공포 없음

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 펀치 (위쪽, 가장 큰 숫자) | -2,000만 원 | 흰색 (파랑 #2D6CDF 상자, 흰 테두리) | 가장 큰 글자 (파랑 = 손실) |
| 하단 1줄 | 좋은 종목이라 몰빵했다가 | 흰색 + 두꺼운 검정 외곽선 | "몰빵했다가" 노랑 #FFD400 — 유일한 강조색 |
| 하단 2줄 | 천만원 수익이 -2천만원 | 흰색 + 두꺼운 검정 외곽선 | — (손실 숫자는 빨강 금지 → 흰색) |

- 하단 2줄 = T2 앞 문장 "좋은 종목이라 확신하고 전 재산 몰빵했다가 천만원 수익이 -2천만원이 됐습니다"를 줄인 것: 13자 + 13자 = 26자 (띄어쓰기 포함, 한 줄 14자 이내 · 합 26자 이내)
- 강조색 1곳 · 노랑 상자 없음 · 펀치는 "-2,000만 원" 1개(9자)

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style. A dim, dark navy-toned kitchen at night, lights mostly off. On the right half of the frame, a
fictional Korean woman in her late 30s with an office-worker look (plain cardigan over a blouse), sitting at a kitchen
table and staring at a smartphone held in both hands, frozen, stunned and regretful expression, lips pressed together,
face lit by the phone's cold light. Her face, hands and the phone are in the upper 60% of the frame; her lower body fades
into the dark bottom band. The phone screen shows only one simple blue line dropping sharply, no app interface, no text.
Fictional person, not resembling any real or famous person, natural Korean features. No crying, no extreme fear.
In the upper-left area, a wide solid blue (#2D6CDF) rounded box with a thin white border containing the huge white bold
text "-2,000만 원", the largest text in the image (about one fifth of the image height).
Bottom title: in the lower third, over a dark band that fades upward from the bottom edge, two lines of huge heavy bold Korean text, left-aligned near the left edge, white with a thick black outline:
line 1 "좋은 종목이라 몰빵했다가", line 2 "천만원 수익이 -2천만원". The word "몰빵했다가" is bright yellow #FFD400. The second line ends well before the bottom-right corner.
Keep all other picture elements in the upper 60% so they never cover the bottom title.
Keep the face and all text inside the central 16:9 area, at least 48px from the edges.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: dark navy #14213D, ink black #1E1E1E, loss blue #2D6CDF.
Realistic photo style. A dim, dark navy-toned kitchen at night. On the right half of the frame, a fictional Korean woman
in her late 30s with an office-worker look, sitting at a kitchen table staring at a smartphone in both hands, stunned and
regretful expression, face lit by the phone's cold light; the phone screen shows only a simple blue line dropping sharply.
Her face, hands and the phone are in the upper 60% of the frame. Fictional person, not resembling any real or famous
person, natural Korean features. In the upper-left area, an empty solid blue (#2D6CDF) rounded box with a thin white
border. The lower 35% of the frame is an empty dark band that fades upward from the bottom edge (black, about 85%
opacity), kept completely clear for a two-line title. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```
- [B]로 만들면 편집 프로그램에서 "문구" 표대로 얹는다: 파랑 상자 안 "-2,000만 원" 흰색 약 140px, 하단 2줄은 Noto Sans KR Black(또는 Pretendard Black) 약 90px, 흰색 + 검정 외곽선 8px 안팎, x 48부터 왼쪽 정렬, y 약 470~680.

## 검수
- [ ] "-2,000만 원" · "좋은 종목이라 몰빵했다가" · "천만원 수익이 -2천만원"이 한 글자도 틀리지 않음 (문장 3·4·7과 같은 숫자)
- [ ] 아래쪽 제목 2줄이 크게 있고, 얼굴·휴대폰·파랑 상자가 2줄을 가리지 않음
- [ ] 가상 인물: 실존 인물·유명인을 닮지 않음, 표정은 허탈·후회까지 (우는 얼굴·공포 없음), 사연에 없는 설정(노후 등) 없음
- [ ] 휴대폰 화면에 앱 이름·로고·실제 앱 화면 없음 · 종목명·티커 없음
- [ ] 손실 숫자에 빨강 없음 · 강조색 1곳 · 320px 축소본에서 얼굴 표정·"-2,000만 원"·하단 2줄이 읽힘
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하 (아니면 업로드 도구가 자동 변환)

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
