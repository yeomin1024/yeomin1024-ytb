# eonje-maesu-2026-10 썸네일 2 — 실험안 ①(사람 없음): 같은 크기의 두 받침대 — 매수 신호 버튼 10개 vs 주사위 — 와 두 점선 사이의 가격 선, 위에 닫힌 상자

버전: v3.1 — 2026-10-17 — **글자: 간단한 영어 낱말·숫자·기호만** (사용자 지시 2026-10-17 "문구 없으니까 너무 허전하네 buy, sell 같은 정말 간단해서 모두 알만한 영어 문구는 써도 돼" · "숫자나 기호 같은 문구도 써도 돼"): `BUY → +5% or −2% ?` — 한국어·문장 없음, 결말 없음 (`stock/guides/README.md` v1.15 3번).
(v3.0 — 2026-10-16 — 다시 만듦: 영상 v4 (잣대 = 성공률 — +5% 가 −2% 보다 먼저 · 비교 상대 = 무작위로 매수한 계좌 2천 개). 두 선택(신호 10개 / 주사위)을 같은 크기로, 결과는 닫힌 상자로 가림 (`stock/guides/README.md` 3번 · 사용자 지시 2026-10-16 "그래 결말 궁금해하도록 변경해"). (v2.0 — 버튼 10개 + 닫힌 상자 — 커밋 28e1b7b))

| 항목 | 값 |
|---|---|
| 역할 | 실험안 ① — 본안에서 **사람만 뺌** (다른 것은 같음) |
| 글자 | **영어 낱말·숫자·기호만** — `BUY → +5% or −2% ?` (누구나 아는 말·숫자·기호·영상 화면의 티커 — `stock/guides/README.md` 3번, 사용자 지시 2026-10-17) |
| 결말 | **보여 주지 않음** — 무작위보다 성공 확률이 높은 신호가 있었는지는 영상에서 (사용자 지시 2026-10-16) |
| 시험하는 가설 | 사람 없이 두 받침대·두 점선·닫힌 상자만으로도 '어느 쪽?'이 읽히면, 더 단순한 쪽이 작은 화면에서 잘 눌린다 |
| 짝 제목 | titles.md R1 「매수 타이밍, 저점·RSI·신고가 신호는 2% 떨어지기 전 5% 오를 확률이 무작위 매수보다 높을까?」 |
| 근거 | 그림·캐릭터 23% vs 10% · 빨강·어두운 쪽 P 0.58·0.61 · 같은 채널 잘된 쪽 = 대비. '결과를 가린 그림'·'주사위'의 근거는 없다 (사용자 지시·영상 화면에 맞춤) |
| 숫자 근거 | '+5%'·'−2%' = 대본 문장 4 (성공은 매수한 값보다 5% 오르는 것, 그 전에 2% 떨어지면 실패) · BUY = 매수 (영상 화면의 BUY 표와 같음) |

## 화면 구성
- 본안에서 **사람만 뺌**: 같은 크기의 받침대 두 개(왼쪽 = 신호 버튼 10개, 오른쪽 = 큰 주사위)가 가운데 아래에 나란히
- 뒤: 3D 파랑 가격 벽 + 초록 점선(+5%)·빨강 점선(−2%) 사이의 가격 선 (닿지 않음)
- 위 가운데: 빛이 새는 닫힌 상자
- 오른쪽 아래 약 220×70: 비움

## 문구 (그대로 사용)
| 자리 | 문구 | 색 |
|---|---|---|
| 왼쪽 위 — 큰 머리글 | `BUY → +5% or −2% ?` | BUY 초록 표(글자 흰색) · → 흰색 · +5% 초록 · or 흰색 · −2% 빨강 · ? 노랑 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 landscape (1280x720), semi-realistic digital illustration with cinematic lighting, deep dark navy background (#0C1424) with a soft glow behind the center.
Background: a huge three-dimensional stock-price wall seen in perspective, rising gently from the left to the right with several small dips. The wall's front face is glowing deep blue (#3E8FE0) fading to dark at the bottom and its top edge is a bright white glowing line. Just above the end of the wall floats a glowing green dashed horizontal line (#2BE0A0), and just below it a glowing red dashed horizontal line (#FF4D5E) — the price line runs between the two dashed lines and has not touched either one yet. There are no axes and no grid lines.
Between the green dashed line and the top of the image floats a heavy closed wooden treasure chest, its lid shut tight, with warm golden light leaking out through the gaps; what is inside cannot be seen.
Foreground, bottom: two identical glowing pedestals of exactly the same size and height, side by side. On the left pedestal: ten small identical round glowing buttons in two rows of five, and above each button floats one small glowing icon: a blank calendar square, a small flag on a pole, an arrow bending upward, a line rising over a smooth yellow line, two smooth lines crossing each other, a red arrow bending downward, a semicircle gauge dial with a needle and no markings, a sharp red mountain-shaped zigzag line, a yellow star above a dashed yellow line, and a yellow star just above a dashed yellow line. On the right pedestal: one big glowing white die with only round pips, taking up exactly the same space as the group of ten buttons.
There is no person in the image.
Neither side is highlighted, pressed or brighter; nobody is winning. The mood is suspense: which one reaches the green line first?
Color accents: green only on the upper dashed line, red only on the lower dashed line, the down arrow and the zigzag icon, yellow only on the stars and dashed icon lines, blue on the price wall, warm gold only from the chest. Large simple shapes, high contrast, readable when shrunk to 320 pixels wide. Leave the bottom-right corner (about 220x70 pixels) dark and empty.
If 16:9 is not available, use the widest landscape canvas; in any case keep the pedestals and the chest inside the central 16:9 area, at least 8% away from the top and bottom edges.
Text: add only the following text in a very bold, clean, flat sans-serif typeface (like Arial Black), flat 2D lettering with a thin dark outline so it stands out on the dark background — never 3D, never embossed, never curved, never in perspective: (1) the headline "BUY → +5% or −2% ?" in the upper-left area, above the main objects (keep it off the chest and the face), very large (about 13% of the image height), written as "BUY" in white letters on a bright green (#2BE0A0) rounded tag, "→" in white, "+5%" in bright green (#2BE0A0), "or" in white, "−2%" in red (#FF4D5E), "?" in yellow (#FFD400). Spell every item exactly as written, character by character: the minus sign is a real minus "−", and "%", "$", ",", ".", "×", "→" and "?" stay exactly as written. These are the ONLY letters, numbers and symbols in the whole image — no other text, no extra numbers, no logos and no watermarks anywhere; coins are plain gold discs, and the buttons, the die, the calendar, the gauge, the pedestals and the price wall have nothing else written on them. Keep all text off any face and out of the bottom-right corner.
```

## [B] 단순한 구도 (가짜 글자·숫자가 계속 생길 때)
```
YouTube thumbnail, 16:9 landscape (1280x720), clean illustration, deep dark navy background (#0C1424).
Background: a glowing blue 3D price wall rising left to right, a green dashed line above its end and a red dashed line below it (the price touches neither); a closed wooden chest with golden light leaking from its lid near the top center.
Foreground: two identical pedestals of the same size — left: ten plain glowing round buttons with simple glowing shapes above them; right: one big glowing die with round pips only. No person.
Keep the pedestals and chest inside the central 16:9 area, 8% away from the top and bottom edges; leave the bottom-right corner empty.
Only this text, flat bold sans-serif, spelled exactly: "BUY → +5% or −2% ?". No other text, letters, numbers, logos or watermarks anywhere.
```

## 검수
- [ ] 그림 속 글자는 문구 표의 1개(`BUY → +5% or −2% ?`)뿐이고 철자·기호가 정확하다 (`−`·`%`·`$`·`,`·`.`·`×`·`→` 를 확대) — 다른 가짜 글자·숫자 없음 (동전 면·상자·받침 확대)
- [ ] **결말이 보이지 않는다**: 신호 버튼 묶음과 주사위가 같은 크기·같은 높이·같은 밝기, 어느 쪽도 눌리거나 빛나지 않음, 가격 선이 초록·빨강 점선 어느 쪽에도 닿지 않음, 상자는 닫혀 있음
- [ ] 초록 = 위 점선(+5%), 빨강 = 아래 점선(−2%), 파랑 = 판정 전 가격 벽 (영상 색과 같음)
- [ ] 16:9, 중요한 그림이 가운데 16:9 안, 오른쪽 아래 비움
- [ ] (사람이 있으면) 가상 인물, 표정 = 망설임 (웃음·좌절 아님)
- [ ] 가로 320px로 줄여도 '신호 버튼 10개 vs 주사위, 두 점선 사이의 가격 선, 닫힌 상자'가 읽힘

## 이미지 검수 (Claude — 10번)
- (이미지가 올라오면 결과를 적는다)

## 결과 (스튜디오 '테스트 및 비교')
| 날짜 | 노출 | 클릭률 | 시청 시간 점유 | 메모 |
|---|---|---|---|---|
