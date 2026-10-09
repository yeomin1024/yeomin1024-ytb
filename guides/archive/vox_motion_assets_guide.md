# Vox 스타일 모션그래픽 이미지 에셋 생성 지시사항 (ChatGPT용)

버전: v1.2 — 2026-10-05 — 한 번에 연속 생성 방식으로 변경
영상: 「한 종목에만 몰빵해서 얻은 천만원 수익이 -3천만원이 됐습니다. 한 종목 올인한 사람들의 최악의 결말」 (약 4분 8초, 자막 43개)

---

## 0. ChatGPT 작업 규칙 (반드시 지킬 것)

1. 이 파일을 끝까지 읽고 **3번 에셋 목록 40개를 BG01부터 E35까지 순서대로 한 번에 연속 생성**한다. 중간에 확인을 묻거나 멈추지 않는다.
2. **에셋 1개 = 이미지 1장**으로 만든다. 여러 에셋을 한 장에 합치지 않는다.
3. 이미지를 만들 때마다 **1번의 스타일 문구 + 해당 에셋의 프롬프트**를 그대로 합쳐서 사용한다. 스타일 문구를 줄이거나 바꾸지 않는다.
4. 각 이미지 아래에는 **에셋 ID와 파일명 한 줄만** 적는다. (예: `E01 — E01_스마트폰.png`) 로컬 저장이 가능하면 `~/Downloads/vox_assets/` 폴더에 표의 파일명 그대로 저장한다.
   - 생성 한도 때문에 중간에 멈추면, 사용자가 "계속"이라고 할 때 멈춘 다음 에셋부터 이어서 끝까지 만든다.
   - 40개를 모두 만들면 완료한 에셋 ID 목록을 한 번에 정리한다.
   - 사용자가 "수정: [에셋 ID] ~"라고 하면 그 에셋만 지적 사항을 반영해 다시 만든다.
5. **이미지 안에 글자, 숫자, 한글, 로고, 워터마크를 절대 넣지 않는다.** 모든 텍스트와 숫자는 편집 단계에서 넣는다.
6. **사람, 캐릭터, 인물 실루엣을 그리지 않는다.** 실제 기업 로고와 실제 화폐 도안도 그리지 않는다. 기업은 로고 없는 일반 건물, 돈은 도안 없는 일반 지폐로 표현한다.
7. 오브젝트는 **투명 배경 PNG**로 만든다. 투명 배경이 안 되면 순백색(#FFFFFF) 단색 배경으로 만든다.
8. 크기: 배경(BG) 1536×1024 가로, 오브젝트(E) 1024×1024 정사각형. (세트 에셋은 표에 적힌 크기)

---

## 1. 공통 스타일 문구 (매번 프롬프트 앞에 붙인다)

**색상 팔레트 (고정)**
| 용도 | 색 | HEX |
|---|---|---|
| 기본 배경 | 크림 종이 | #F2EBDD |
| 선·글자 | 잉크 블랙 | #1E1E1E |
| 강조 하이라이트 | 노랑 | #FFD400 |
| 상승·수익 (국내 증권 앱 관례) | 빨강 | #E63B2E |
| 하락·손실 (국내 증권 앱 관례) | 파랑 | #2D6CDF |
| 보조 | 웜 그레이 | #9A968E |
| 위기 장면 배경 | 다크 네이비 | #14213D |

### [STYLE-OBJ] 오브젝트용
```
Editorial explainer-video collage asset. Single subject, centered with generous margin, isolated on a fully transparent background (PNG with alpha). Looks like a printed paper cut-out: thick white sticker border around the silhouette, subtle paper grain, halftone dot print texture, slightly rough hand-cut edges, flat soft lighting. Limited palette only: ink black #1E1E1E, cream #F2EBDD, highlight yellow #FFD400, red #E63B2E, blue #2D6CDF, warm gray #9A968E. No people, no characters. Absolutely no text, letters, numbers, logos, or watermarks.
```

### [STYLE-BG] 배경용
```
Editorial explainer-video collage background, landscape, flat and uncluttered with empty space in the center for text and cut-out layers. Printed paper look with visible paper grain and fine halftone texture, slightly uneven print. Limited palette only: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, warm gray #9A968E, dark navy #14213D. No people, no text, no letters, no numbers, no logos.
```

---

## 2. 장면 구성표 (참고용 — ChatGPT는 3번 에셋만 생성)

| 장면 | 시간 | 자막 | 화면 연출 | 사용 에셋 | 편집에서 넣을 텍스트 |
|---|---|---|---|---|---|
| S01 | 0:00–0:12 | 1–2 | 폰 화면 위로 AI 칩이 떠오르고 작은 상승 화살표 | BG01, E01, E02, E05 | 몽고디비 |
| S02 | 0:12–0:18 | 3 | 지폐 더미가 큰 바구니 하나로 전부 빨려 들어감, 바구니에 종목 카드 부착 | E03, E31, E04 | 전 재산 1억 원 |
| S03 | 0:18–0:26 | 4–5 | 컨페티가 터지고 빨간 화살표 상승, 위에 전고점 점선 | E07, E05 | +1천만 원, 전고점 점선 |
| S04 | 0:26–0:30 | 6 | 꿈 구름이 떠오른 뒤 종이가 찢어지며 어두운 화면으로 전환 | E08, E09, BG02 | — |
| S05 | 0:30–0:35 | 7 | 어두운 배경, 폰 화면에 파란 손실, 파란 화살표 추락 | BG02, E01, E06 | -3천만 원 |
| S06 | 0:35–0:42 | 8 | 신문 기사 슬라이드 인, 건물 A에서 건물 B로 마커 화살표가 그려짐 | E10, E11, E19 | CEO, 다른 회사로 이적 |
| S07 | 0:42–0:48 | 9 | 급락 차트 조각 확대, 급락 지점에 빨간 마커 동그라미 | E12, E19 | 최대 -26% |
| S08 | 0:48–0:58 | 10–11 | 빈 지갑에서 나방이 날아가고, 위로 먹구름과 비 | E13, E14 | — |
| S09 | 0:58–1:00 | 12 | 노랑 띠 배경 인트로 카드, 테이프로 붙인 느낌 | BG03, E18 | 채널명 |
| S10 | 1:00–1:15 | 13–15 | 생각 말풍선 3개가 차례로 등장 | E15 | 따옴표 속 생각 3개 |
| S11 | 1:15–1:21 | 16 | 장밋빛 안경이 화면 중앙으로 내려옴 | E16 | 확신 |
| S12 | 1:21–1:38 | 17–19 | 폰 여러 대가 화면을 채우고, 위에 큰 물음표 | E01, E17 | — |
| S13 | 1:38 직전 2~3초 | [장면] | 투자 권유 고지 카드 | BG03, E18 | 투자 권유가 아닙니다 |
| S14 | 1:38–1:51 | 20–21 | 안개 낀 길, 물음표 | BG04, E17 | 대처할 방법이 없다 |
| S15 | 1:51–2:07 | 22–23 | 롤러코스터 레일이 올라가다 정상에서 번개, 급하강 | E21, E20 | — |
| S16 | 2:07–2:27 | 24–26 | 건물 3개에 각각 파란 하락 화살표, 이어서 업종 아이콘 줄 전체가 함께 하락 | E11, E06, E19, E22 | CDNS, 메타, 구글 / -10%, -26%, -9% |
| S17 | 2:27–2:46 | 27–29 | 논문 더미와 돋보기 → 말 100개 격자(와플 차트) 중 58개 회색 강조, 옆에 국채 증서 | E23, E24, E25 | 2만 6천 개, 58%, 미국 단기 국채 |
| S18 | 2:46–2:53 | 30 | 격자 중 금색 말 4개만 빛남, 트로피와 금괴 | E24, E26 | 상위 4% |
| S19 | 2:53–3:06 | 31–32 | 절벽 위를 달리던 차트 선이 절벽 아래로 떨어짐 | E27 | 40% 이상, -70% |
| S20 | 3:06–3:12 | 33 | 건초더미 속 금바늘에 빨간 마커 동그라미 | E28, E19 | 4% |
| S21 | 3:12–3:24 | 34–35 | 지폐가 작은 바구니 10개로 나눠 담김, 천칭 저울로 비중 조절 | E03, E29, E33 | 분산, 비중 조절 |
| S22 | 3:24–3:43 | 36–38 | 화면 분할: 왼쪽 부서진 큰 바구니 vs 오른쪽 바구니 10개 중 1개만 부서짐 → 저울 | E32, E29, E30, E33 | -3천만 원 vs -300만 원(3%), 15% |
| S23 | 3:43–3:49 | 39 | 방패가 바구니들을 먹구름·번개로부터 막음 | E34, E29, E14, E20 | 대처할 여유 |
| S24 | 3:49–4:07 | 40–43 | 아침 햇살 배경, 새싹 화분 → 노랑 띠 엔딩 카드 | BG05, E35, BG03 | 핵심 당부 문장, 감사합니다 |

---

## 3. 에셋 목록 (이 순서대로 한 번에 연속 생성)

### 3-1. 배경 (BG) — [STYLE-BG] + 프롬프트, 1536×1024

| ID | 파일명 | 프롬프트 |
|---|---|---|
| BG01 | BG01_크림종이.png | Plain cream paper background with very faint warm gray grid lines, empty composition. |
| BG02 | BG02_다크네이비.png | Dark navy #14213D paper background with subtle grain and soft dark vignette, ominous mood, empty composition. |
| BG03 | BG03_노랑띠.png | Cream paper background with one wide horizontal strip of torn yellow #FFD400 paper across the middle, ragged torn edges, empty composition. |
| BG04 | BG04_안개길.png | Collage of a straight empty road disappearing into thick fog, desaturated halftone photo cut-out laid on cream paper, mysterious and uncertain mood. |
| BG05 | BG05_아침햇살.png | Warm sunrise over layered paper-cut hills, soft yellow and cream tones, calm hopeful mood, empty sky area for text. |

### 3-2. 오브젝트 (E) — [STYLE-OBJ] + 프롬프트, 1024×1024 (세트는 1536×1024)

| ID | 파일명 | 크기 | 프롬프트 |
|---|---|---|---|
| E01 | E01_스마트폰.png | 1024×1024 | Modern smartphone, front view, screen completely blank pure white. |
| E02 | E02_AI칩.png | 1024×1024 | Microchip with glowing yellow circuit lines radiating outward. |
| E03 | E03_지폐더미.png | 1024×1024 | Several stacks of generic banknotes with paper bands, no real currency design, no numbers. |
| E04 | E04_종목카드.png | 1024×1024 | A single paper index card slightly tilted, blank title area at top and a blank small chart window below, a piece of tape on one corner. |
| E05 | E05_상승화살표.png | 1024×1024 | Thick paper-cut arrow pointing up and to the right, red #E63B2E, torn edges. |
| E06 | E06_하락화살표.png | 1024×1024 | Thick paper-cut arrow plunging down and to the right, blue #2D6CDF, torn edges. |
| E07 | E07_컨페티.png | 1024×1024 | Scattered paper confetti pieces in red, yellow and cream. |
| E08 | E08_꿈구름.png | 1024×1024 | Fluffy paper-cut cloud thought bubble, cream with ink outline, blank inside, dreamy. |
| E09 | E09_찢어지는종이.png | 1536×1024 | A horizontal sheet of cream paper torn in half with ragged edges, the two halves slightly pulled apart. |
| E10 | E10_신문기사.png | 1024×1024 | Newspaper clipping with a blank headline bar, an empty photo box, and body text shown only as unreadable gray placeholder lines. |
| E11 | E11_기업빌딩세트.png | 1536×1024 | Four different generic corporate office buildings in a row, evenly spaced: glass tower, low modern campus, brick office, angular modern HQ. No logos, no signage. |
| E12 | E12_급락차트.png | 1024×1024 | Torn paper piece showing a simple line chart that rises steadily then crashes sharply at the end; rising part red, crash part blue; no axes labels, no numbers. |
| E13 | E13_빈지갑.png | 1024×1024 | Open empty brown leather wallet with a small moth flying out. |
| E14 | E14_먹구름.png | 1024×1024 | Dark gray paper-cut storm cloud with falling rain drops. |
| E15 | E15_생각말풍선.png | 1024×1024 | Thought bubble with three small trailing circles, white with ink outline, blank inside. |
| E16 | E16_장밋빛안경.png | 1024×1024 | Pair of glasses with rose-pink tinted lenses, front view. |
| E17 | E17_물음표.png | 1024×1024 | Big chunky paper-cut question mark, yellow #FFD400 with ink outline. |
| E18 | E18_마스킹테이프.png | 1536×1024 | Six separate torn masking tape pieces in cream and yellow, different angles, evenly spaced. |
| E19 | E19_마커낙서.png | 1536×1024 | Hand-drawn marker doodles, evenly spaced: a loose circle, an underline, a curved arrow, an X mark, an exclamation mark; in red #E63B2E and ink black. |
| E20 | E20_번개.png | 1024×1024 | Paper-cut lightning bolt, yellow #FFD400 with ink outline. |
| E21 | E21_롤러코스터.png | 1536×1024 | Side view of an empty roller coaster track that climbs high then drops steeply, paper cut-out style. |
| E22 | E22_업종아이콘.png | 1536×1024 | Six flat icons in a row, evenly spaced: semiconductor chip, shopping bag, medicine capsule, factory, car, bank building. |
| E23 | E23_논문돋보기.png | 1024×1024 | Stack of academic papers with unreadable gray placeholder lines and a magnifying glass on top. |
| E24 | E24_종목말.png | 1024×1024 | Two simple flat game pawn tokens side by side: one warm gray, one shiny gold. |
| E25 | E25_국채증서.png | 1024×1024 | Generic government bond certificate paper with an ornate border, blank center, no seals, no text. |
| E26 | E26_트로피금괴.png | 1024×1024 | Golden trophy with a few gold bars in front. |
| E27 | E27_절벽차트.png | 1536×1024 | Paper-cut cliff landscape; a chart line runs along the flat top and falls off the cliff edge. |
| E28 | E28_건초더미바늘.png | 1024×1024 | Haystack with one tiny shining golden needle visible near the surface. |
| E29 | E29_작은바구니.png | 1024×1024 | Small woven basket, empty, front view. |
| E30 | E30_작은바구니_부서짐.png | 1024×1024 | Same small woven basket as E29, broken and torn open with a crack. |
| E31 | E31_큰바구니.png | 1024×1024 | One big woven basket overflowing with generic banknotes. |
| E32 | E32_큰바구니_부서짐.png | 1024×1024 | Same big woven basket as E31, broken apart at the bottom with banknotes spilling and blowing away. |
| E33 | E33_천칭저울.png | 1024×1024 | Brass balance scale, the two pans level. |
| E34 | E34_방패.png | 1024×1024 | Paper-cut shield, yellow #FFD400 with ink outline. |
| E35 | E35_새싹화분.png | 1024×1024 | Small terracotta pot with a fresh green sprout. |

총 40개 (배경 5, 오브젝트 35)

---

## 4. 생성하지 않는 것 (편집에서 직접 만든다)

- 캐릭터, 인물, 사람 실루엣
- 모든 자막, 한글 텍스트, 숫자 (-3천만 원, -26%, 58%, 4% 등)
- 실제 데이터 차트와 와플 차트 배치 (E24를 복제해 만든다)
- 기업명, 채널명, 투자 권유 고지 문구
- 폰 화면 속 계좌 화면, 전고점 점선

---

## 5. 편집 참고 (Vox 스타일 모션)

- 레이어를 배경·중간·전경으로 나누고 천천히 줌인하며 패럴랙스를 준다.
- 컷아웃은 살짝 회전하며 미끄러져 들어오게 하고, 12fps 정도의 스톱모션 흔들림을 준다.
- 핵심 숫자와 단어는 노랑(#FFD400) 형광펜이 지나가듯 강조한다.
- 마커 낙서(E19)는 그려지는 애니메이션으로 쓴다.
- 전체 화면에 종이 질감과 필름 그레인을 얹는다.
- 수익은 빨강, 손실은 파랑으로 통일한다.

---

## 변경 이력

| 버전 | 날짜 | 변경 내용 | 변경 위치 |
|---|---|---|---|
| v1.2 | 2026-10-05 | 한 개씩 생성 후 대기하던 방식을 40개 한 번에 연속 생성으로 변경. 에셋 1개 = 이미지 1장 규칙, 로컬 저장 폴더(~/Downloads/vox_assets/), 중단 시 "계속"으로 이어서 생성, 완료 후 목록 정리 규칙 추가 | 0, 3 |
| v1.1 | 2026-10-05 | 캐릭터 에셋 C01~C08과 [STYLE-CHAR] 삭제. 사람·캐릭터·실루엣 금지 규칙 추가. 캐릭터가 나오던 장면(S01, S03, S05, S06, S08, S10, S11, S12, S14, S24)을 오브젝트만으로 연출하도록 수정. 총 에셋 48개 → 40개 | 0, 1, 2, 3, 4 |
| v1.0 | 2026-10-05 | 최초 작성 | 전체 |
