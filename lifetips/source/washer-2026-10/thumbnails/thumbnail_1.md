# washer-2026-10 썸네일 1 — 숫자 반전 (영수증 카드)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `lifetips/guides/thumbnail_rules.md` v1.0), 대본 v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | 아끼려던 돈(12만 원)이 더 큰 수리비(21만 원)로 뒤집힌 **영수증 숫자 반전**이 가장 클릭을 부른다 |
| 짝 제목 | `titles.md` **T1 (채택)** "업체비 12만원 아끼려고 세탁기를 직접 분해했다가 …" — T3과도 어울림 |
| 숫자 근거 | 문장 2 "세탁기 분해 청소에 12만 원이 든다더라고요" (0:06) · 문장 7 "12만 원을 아꼈다는 생각에" (0:34) · 문장 10 "수리비가 21만 원이 나왔어요" (0:48~0:55) → 모두 1분 안 |

## 화면 구성
- 크림 배경 위, 화면 가운데를 크게 채우는 **길쭉한 흰 영수증 종이** 한 장 (아래쪽이 톱니 모양으로 찢긴 일반 영수증, 서비스센터 서식·로고·바코드·QR 없음)
- 영수증 위쪽: "12만 원" (파랑) + 그 옆 "아끼려다" (잉크 글자 + 노랑 형광펜 — 유일한 강조)
- 그 아래 굵은 빨강 아래 화살표 하나
- 영수증 아래쪽 절반: 넓은 빨강 상자 안에 흰 글자 **"수리비 21만 원"** (가장 큰 글자, 화면 높이의 25% 안팎)
- 인물 없음 · 세탁기 그림 없음(또는 영수증 뒤로 흐릿한 일반형 통돌이 윗부분만) · 오른쪽 아래 구석은 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 1 | 12만 원 아끼려다 | "12만 원" 파랑 #2D6CDF / "아끼려다" 잉크 #1E1E1E | "아끼려다"에 노랑 형광펜 #FFD400 (유일한 강조) |
| 2 | 수리비 21만 원 | 흰색 (빨강 #E63B2E 상자 위) | 가장 큰 글자 |

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, saved-money blue #2D6CDF, loss red #E63B2E.
Bottom-right corner kept empty (video length badge).
Clean flat editorial graphic on a cream paper background (#F2EBDD) with subtle paper grain. In the center, a tall plain
white paper receipt with a torn zigzag bottom edge, slightly tilted, filling most of the frame height (a generic receipt,
NOT any real company's service form: no logo, no company name, no barcode, no QR code, no table lines).
Top part of the receipt: the text "12만 원" in large blue (#2D6CDF) bold letters, followed on the same line by the word
"아끼려다" in black bold letters over a bright yellow (#FFD400) highlighter stripe.
Below it, one thick red (#E63B2E) arrow pointing down.
The lower half of the receipt is a wide solid red (#E63B2E) rounded box with the huge white bold text "수리비 21만 원",
the largest element in the image, about a quarter of the frame height.
Optionally, behind the receipt, a soft out-of-focus top of a plain generic white top-loading washing machine with no
brand, no logo and no buttons layout from a real product. No people, no hands, no tools. Keep all text inside the
central 16:9 safe area. Minimal, nothing decorative.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, ink black #1E1E1E, highlight yellow #FFD400, saved-money blue #2D6CDF, loss red #E63B2E.
Clean flat editorial graphic on a cream paper background with subtle paper grain. In the center, a tall plain white
paper receipt with a torn zigzag bottom edge, slightly tilted, filling most of the frame height, with no logo, no
barcode, no QR code and no form lines. Top part of the receipt: empty space for one line of text and a short bright
yellow highlighter stripe on the right of that line. Below it one thick red arrow pointing down. The lower half of the
receipt is a wide empty solid red (#E63B2E) rounded box. Optionally a soft out-of-focus top of a plain generic white
top-loading washing machine behind it, no brand. No people, no tools. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "12만 원" · "아끼려다" · "수리비 21만 원"이 한 글자도 틀리지 않음 (문장 2·7·10과 같은 숫자)
- [ ] 아낀 돈은 파랑, 수리비는 빨강 (`thumbnail_rules.md` 1번) · 노랑 강조 1곳
- [ ] 영수증이 실제 서비스센터·회사 서식처럼 보이지 않음 (로고·회사 이름·바코드·QR·표 없음)
- [ ] 세탁기가 있으면 어느 회사 제품인지 알 수 없는 일반형 · 분해 장면·공구 없음
- [ ] 320px 축소본에서 "21만 원"이 바로 읽힘 · 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
