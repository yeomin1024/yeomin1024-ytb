# 쇼츠 — `baedang-etf-2026-10` 롱폼으로 보내는 쇼츠 (프롤로그형 · 언어 없는 화면)

버전: v1.0.2 — 2026-10-17 — 쇼츠 썸네일 글자에 비교·수식 기호 `SCHD − TAX > SPY` · `+$33K` · `?` (사용자 지시 2026-10-17 "<, >, =, vs, +, - 등등 비교나 간단한 수식 관련된 기호 문구도 사용하는 게 좋을 것 같아 다시 수정해봐").
(v1.0.1 — 2026-10-17 — 쇼츠 썸네일 글자 `SCHD − TAX > SPY` · `+$33K` · `?` (간단한 영어·숫자·기호 — 사용자 지시 2026-10-17 "문구 없으니까 너무 허전하네 buy, sell 같은 정말 간단해서 모두 알만한 영어 문구는 써도 돼" · "숫자나 기호 같은 문구도 써도 돼").)
(v1.0 — 2026-10-17 — 새로 만듦 (사용자 지시 2026-10-17 "저번에 쇼츠 만들었었으니까 같은 방식으로 영상 당 쇼츠 1개씩 만들어봐" · "다른점은 전세계 시청자들 대상이니까 언어 문구, 자막 달지 말고 영상으로만 잘 이해가 가도록 해야해 계속 진행해"). 재테크 쇼츠(`economic/source/eunte-kkeonaeseugi-2026-10/shorts/`)와 같은 꼴 — 첫 문장 하나에 핵심 → 상황 → 질문 → '아래 영상에서 확인하세요' — 에 주식 규칙(자막 없음 · 화면 글자 언어 없음 · 결말 가림 · 10개 언어)을 더함.)

- 보내는 곳(롱폼): **배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까?** (`../upload.md` 1번 제목) — 쇼츠의 '관련 동영상'으로 연결 (롱폼 공개 뒤)
- **넣지 않는 것 (롱폼의 결말):** 2023년 4월 뒤 앞선 계좌, 2026년 두 계좌의 **끝 값**, 끝에 매도하고 세금을 낸 경우, VYM, 시작 시점을 바꾼 결과. 화면에도 2023.07 뒤는 '?' 띠로 가린다.
- **보여 주는 것:** SCHD·SPY 경주 2011~2023.01: 앞선 계좌가 43번 바뀜(2017년까지) · 2019 배당 +63.1% · 2022 −14.6% vs −22.2% · 2023.01.06 차이 약 $33K — 롱폼 경주의 중간 숫자.
- 근거: [`stock/guides/shorts_insights.md`](../../../guides/shorts_insights.md) v1.0 (주식 쇼츠 분석 — 경주 그래프 쇼츠 같은 채널 ×32~×203 · 45~59초 19% · 금액 +20%p ⚑ · 해시태그 3~5개 6.6%) · 공통 규칙 `guides/shorts_guide.md` 4번
- 길이: **9문장 · 275음절 · 예상 약 46.8초** (`render.mjs sync --estimate` — 진행자 H04 실측으로 맞춘 추정) · 45~59초 · 50자 넘는 문장 없음 · 첫 문장 약 6.1초
- 목소리: 진행자 H04 하나 (CLAUDE.md) — 한국어 내레이션, **화면은 소리 없이도 이해되게** (해외 시청자는 자동 더빙·자동 번역)
- 숫자: 쇼츠 대본의 숫자는 모두 롱폼 대본에 있다 — `python3 tools/backtest/shorts_numcheck.py stock baedang-etf-2026-10` → [`checklist.md`](checklist.md) (없음 0). 화면 숫자는 `stock/source/baedang-etf-2026-10/backtest/anim.js` (`a` SCHD · `b` SPY · `paid` · `facts` — 2023.06 뒤 값은 그리지 않음)에서만.
- ※ 연구·교육용 — 투자 권유가 아님

## 1. 제목

| | 제목 (한국어 — 기본 언어) | 글자 | 까닭 |
|---|---|---|---|
| **R1 (추천)** | **배당 ETF, 세금 떼고도 S&P 500보다 3만 3천 달러 앞섰다… 끝까지 앞설까?** | 47 | 금액 '3만 3천 달러' +20%p ⚑ · 맨 앞 니즈 낱말 '배당 ETF' · 말줄임 · '끝까지 앞설까?'로 결말을 숨김 |
| R2 | SCHD vs SPY, 매달 1,000달러씩 15년 모으면 어느 쪽이 더 남을까? | 45 | 두 티커 vs 비교(+5.8%p) · 매달 1,000달러 — 근거가 R1보다 약해 2안 |

쓰지 않은 것: **'이유'**(쇼츠가 이유를 말하지 않음 — `guides/shorts_guide.md` 4번 5항) · '재테크'(0%)·'투자'(3.8%)·'주식투자'(4.7%)·'AI'(6.2%) 낱말 (shorts_insights 3번) · 결말(롱폼의 끝 결과). 길이는 40자 안팎 — 쇼츠 비교 집단에서 20자 미만 16%·30~39자 14%·40자 이상 15%로 차이가 작다 (shorts_insights 3번).

### 1-1. 언어별 제목·설명 (localizations — 롱폼 `upload.md` 5번과 같은 9개 언어)

JSON — 롱폼 업로드 시트와 같은 꼴 (업로드 도구 v1.6 이 읽는 형식). '▶' 줄의 롱폼 제목은 그 언어의 롱폼 제목. 해시태그는 언어와 상관없는 티커.

```
{
 "en": {
  "title": "A dividend ETF was $33,000 ahead of the S&P 500 even after tax… will it stay ahead?",
  "description": "From 2011 we put $1,000 a month into SCHD, a US dividend stock ETF, and into SPY, an S&P 500 ETF. Each dividend lost 15% to tax and the rest was reinvested. Up to 2017 the lead changed 43 times; in the 2022 bear market SCHD fell 14.6% and SPY 22.2%. In January 2023, SCHD was about $33,000 ahead.\n▶ The result after 15 years of saving is in the related video below — Dividend ETF saved monthly: after 15% dividend tax, is more left than the same money in the S&P 500?\n\nData and full conditions (dividends, buy day, fees) are in the main video's description. The code was written by AI and the narration is an AI voice.\nPast data only — not investment advice.\n#SCHD #SPY"
 },
 "hi": {
  "title": "डिविडेंड ETF टैक्स के बाद भी S&P 500 से $33,000 आगे… क्या आगे ही रहेगा?",
  "description": "2011 से हर महीने $1,000 अमेरिकी डिविडेंड ETF SCHD और S&P 500 ETF SPY में डाले। हर डिविडेंड से 15% टैक्स कटा और बाकी फिर से निवेश हुआ। 2017 तक आगे रहने वाला खाता 43 बार बदला; 2022 की गिरावट में SCHD 14.6% और SPY 22.2% गिरा। जनवरी 2023 में SCHD लगभग $33,000 आगे था।\n▶ 15 साल जमा करने का नतीजा नीचे जुड़े वीडियो में — डिविडेंड ETF हर महीने जमा करें: 15% टैक्स के बाद क्या S&P 500 में उतने ही पैसे से ज़्यादा बचेगा?\n\nडेटा और पूरी शर्तें (डिविडेंड, खरीद का दिन, शुल्क) मुख्य वीडियो के विवरण में हैं। कोड AI ने लिखा और आवाज़ AI की है।\nसिर्फ़ पिछला डेटा — निवेश सलाह नहीं।\n#SCHD #SPY"
 },
 "id": {
  "title": "ETF dividen unggul $33.000 dari S&P 500 meski sudah dipotong pajak… tetap unggul sampai akhir?",
  "description": "Sejak 2011 kami menaruh $1.000 per bulan di SCHD, ETF saham dividen AS, dan di SPY, ETF S&P 500. Setiap dividen dipotong pajak 15% dan sisanya diinvestasikan lagi. Sampai 2017 posisi unggul berganti 43 kali; di pasar turun 2022 SCHD turun 14,6% dan SPY 22,2%. Pada Januari 2023, SCHD unggul sekitar $33.000.\n▶ Hasil setelah 15 tahun menabung ada di video tertaut di bawah — ETF dividen tiap bulan: setelah pajak dividen 15%, sisa lebih banyak dari S&P 500 dengan uang sama?\n\nData dan syarat lengkap (dividen, hari beli, biaya) ada di deskripsi video utama. Kode ditulis AI dan narasinya suara AI.\nHanya data masa lalu — bukan saran investasi.\n#SCHD #SPY"
 },
 "pt": {
  "title": "ETF de dividendos ficou US$ 33 mil à frente do S&P 500 mesmo após imposto… segue na frente?",
  "description": "Desde 2011 colocamos US$ 1.000 por mês no SCHD, um ETF de ações de dividendos dos EUA, e no SPY, um ETF do S&P 500. Cada dividendo perdeu 15% de imposto e o resto foi reinvestido. Até 2017 a liderança mudou 43 vezes; no mercado em queda de 2022 o SCHD caiu 14,6% e o SPY 22,2%. Em janeiro de 2023, o SCHD estava cerca de US$ 33.000 à frente.\n▶ O resultado depois de 15 anos de aportes está no vídeo vinculado abaixo — ETF de dividendos todo mês: com 15% de imposto, sobra mais que o mesmo dinheiro no S&P 500?\n\nDados e condições completas (dividendos, dia de compra, taxas) na descrição do vídeo principal. O código foi escrito por IA e a narração é voz de IA.\nApenas dados passados — não é recomendação de investimento.\n#SCHD #SPY"
 },
 "es-419": {
  "title": "Un ETF de dividendos iba US$33,000 por delante del S&P 500 aun tras impuestos… ¿seguirá adelante?",
  "description": "Desde 2011 pusimos US$1,000 al mes en SCHD, un ETF de acciones de dividendos de EE. UU., y en SPY, un ETF del S&P 500. A cada dividendo se le restó 15% de impuesto y el resto se reinvirtió. Hasta 2017 el liderazgo cambió 43 veces; en la caída de 2022 SCHD bajó 14.6% y SPY 22.2%. En enero de 2023, SCHD iba unos US$33,000 por delante.\n▶ El resultado tras 15 años de aportes está en el video vinculado abajo — ETF de dividendos cada mes: con 15% de impuesto, ¿queda más que el mismo dinero en el S&P 500?\n\nDatos y condiciones completas (dividendos, día de compra, comisiones) en la descripción del video principal. El código lo escribió una IA y la narración es una voz de IA.\nSolo datos pasados — no es asesoría de inversión.\n#SCHD #SPY"
 },
 "ja": {
  "title": "配当ETF、税引き後でもS&P 500より3万3千ドル先行… 最後まで先行する？",
  "description": "2011年から毎月1,000ドルずつ、米国配当株ETFのSCHDとS&P 500 ETFのSPYに入れました。配当は受け取るたびに15%を差し引いて再投資。2017年までに先行する口座が43回入れ替わり、2022年の下落相場ではSCHDが14.6%、SPYが22.2%減りました。2023年1月にはSCHDが約3万3千ドル先行。\n▶ 15年積み立てた2つの口座の結果は、下のリンクの動画で — 高配当ETFを毎月積み立てると、配当税15%を引いても同じ額のS&P 500より多く残る？\n\nデータと計算条件（配当の扱い・買付日・手数料）は本編の説明欄にあります。計算コードはAIが書き、ナレーションはAI音声です。\n過去データによる計算で、投資の勧誘ではありません。\n#SCHD #SPY"
 },
 "de": {
  "title": "Dividenden-ETF lag selbst nach Steuern 33.000 $ vor dem S&P 500 … bleibt er vorn?",
  "description": "Ab 2011 flossen jeden Monat 1.000 $ in SCHD, einen ETF auf US-Dividendenaktien, und in SPY, einen S&P-500-ETF. Von jeder Dividende gingen 15 % Steuer ab, der Rest wurde wieder angelegt. Bis 2017 wechselte die Führung 43-mal; im Bärenmarkt 2022 fiel SCHD um 14,6 % und SPY um 22,2 %. Im Januar 2023 lag SCHD rund 33.000 $ vorn.\n▶ Das Ergebnis nach 15 Jahren Sparen im verlinkten Video unten — Dividenden-ETF monatlich sparen: Bleibt nach 15 % Steuer mehr als mit gleichem Geld im S&P 500?\n\nDaten und alle Bedingungen (Dividenden, Kauftag, Gebühren) in der Beschreibung des Hauptvideos. Der Code wurde von einer KI geschrieben, die Stimme ist eine KI-Stimme.\nNur historische Daten – keine Anlageberatung.\n#SCHD #SPY"
 },
 "vi": {
  "title": "ETF cổ tức dẫn trước S&P 500 33.000 USD dù đã trừ thuế… có dẫn trước đến cuối?",
  "description": "Từ năm 2011, mỗi tháng chúng tôi bỏ 1.000 USD vào SCHD, ETF cổ phiếu cổ tức Mỹ, và vào SPY, ETF S&P 500. Mỗi lần nhận cổ tức trừ 15% thuế rồi tái đầu tư phần còn lại. Đến năm 2017 tài khoản dẫn trước đổi chỗ 43 lần; trong thị trường giảm 2022 SCHD giảm 14,6%, SPY giảm 22,2%. Tháng 1/2023, SCHD dẫn trước khoảng 33.000 USD.\n▶ Kết quả sau 15 năm tích lũy ở video liên kết bên dưới — Tích lũy ETF cổ tức mỗi tháng: sau thuế cổ tức 15%, có còn nhiều hơn S&P 500 với cùng số tiền?\n\nDữ liệu và điều kiện đầy đủ (cổ tức, ngày mua, phí) trong phần mô tả video chính. Mã do AI viết, lời thuyết minh là giọng AI.\nChỉ là dữ liệu quá khứ — không phải lời khuyên đầu tư.\n#SCHD #SPY"
 },
 "tr": {
  "title": "Temettü ETF'si vergiden sonra bile S&P 500'ün 33.000 $ önündeydi… önde kalacak mı?",
  "description": "2011'den itibaren her ay 1.000 $'ı ABD temettü hisse ETF'si SCHD'ye ve S&P 500 ETF'si SPY'a yatırdık. Her temettüden %15 vergi kesildi, kalanı yeniden yatırıldı. 2017'ye kadar öndeki hesap 43 kez değişti; 2022 düşüşünde SCHD %14,6, SPY %22,2 geriledi. Ocak 2023'te SCHD yaklaşık 33.000 $ öndeydi.\n▶ 15 yıllık birikimin sonucu aşağıdaki bağlantılı videoda — Temettü ETF'si her ay biriktirilirse %15 vergiden sonra aynı parayla S&P 500'den fazla kalır mı?\n\nVeriler ve tüm koşullar (temettü, alım günü, komisyon) ana videonun açıklamasında. Kodu yapay zekâ yazdı, seslendirme yapay zekâ sesi.\nYalnızca geçmiş veriler — yatırım tavsiyesi değildir.\n#SCHD #SPY"
 }
}
```

## 2. 대본 (시각은 예상 — 내레이션 뒤 실제 시각으로 맞춤)

| # | 시각 | 대본 | 역할 | 화면 (언어 없음 — 숫자·$·%·연도·티커·BUY·기호·아이콘) |
|---|---|---|---|---|
| 1 | 0:00 | 배당 ETF가 세금 떼고도, 2023년 1월 지수 ETF보다 약 3만 3천 달러 많았어요. | 핵심 한 문장 | **쇼츠 썸네일 그림** (글자 `SCHD − TAX > SPY` · `+$33K` · `?` — 보라 동전 나무 vs 파란 나무 줄다리기, 매듭은 살짝 보라 쪽, 줄 끝은 안개) |
| 2 | 0:06 | 미국 배당주 ETF인 SCHD와, S&P 500 ETF인 SPY를 비교한 거예요. | 두 계좌 | 왼쪽 카드 `SCHD` + 동전 열린 나무 · 오른쪽 카드 `SPY` + `↗ S&P 500` |
| 3 | 0:13 | 2011년부터 두 계좌에 매달 1,000달러씩 넣었어요. | 규칙 | 경주 시작 2011.11 · 위 `📅 BUY $1,000` · 넣은 돈 노란 점선이 계단처럼 오름 |
| 4 | 0:17 | 배당은 받을 때마다 15%를 떼고 다시 매수했고요. | 규칙 | 오른쪽 위 판: `🪙 → 🧾 −15%` · `🪙 ↺ BUY` (배당에서 15%를 떼고 나머지로 다시 매수) |
| 5 | 0:21 | 2017년까지는 앞선 계좌가 43번이나 바뀌었어요. | 엎치락뒤치락 | 2017.12.29 에서 잠깐 멈춤 · 아래 칸 왕관이 SCHD·SPY 사이를 오가고 `👑 ⇄ 43` 이 노랗게 |
| 6 | 0:25 | 2019년 배당은 SCHD가 SPY보다 63.1% 많았고요. | 배당 | 오른쪽 아래 판: `🪙 2019` · SCHD 막대 vs SPY 막대 · `+63.1%`(보라) |
| 7 | 0:30 | 2022년 하락장에서는 SCHD가 14.6%만 줄어, SPY 22.2%보다 덜 떨어졌어요. | 하락장 | 2022.09.30 칩 `−14.6%`(보라) · `−22.2%`(파랑) → 2023.01.06 두 선 사이 괄호 `$33K` |
| 8 | 0:39 | 그럼 15년을 모았다면, 어느 계좌가 더 많이 남았을까요? | 질문 | 경주 위에 `2026` · `SCHD ＞ SPY ?` |
| 9 | 0:43 | 두 계좌의 결과는 아래 영상에서 확인하세요. | 롱폼 안내 | 끝 화면: `SCHD ?` `SPY ?` · `📅 BUY $1,000` · `2011 → 2026` · 노란 ⬇ |

- 흐름: ① 핵심 한 문장(경주 중간의 숫자) → ② 대상·티커 설명 → ③ 규칙 → ④ 경주 중간의 사실 → ⑤ 질문(결말) → ⑥ '아래 영상에서 확인하세요'.
- 롱폼과 같은 색 = 같은 계좌 (주식 쇼츠 0-1 5번) — 쇼츠에서 롱폼으로 넘어와도 같은 그림.
- 끝인사("시청해주셔서 감사합니다.")는 넣지 않는다 (`guides/shorts_guide.md` 4번).
- 대본 TXT (내레이션용): [`baedang-etf-2026-10-shorts.txt`](baedang-etf-2026-10-shorts.txt)

## 3. 영상 만드는 법 (오디오가 생긴 뒤 — CLAUDE.md '오디오 먼저')

**첫 문장 = 쇼츠 썸네일 그림:** 0초부터 첫 문장이 끝날 때까지 `thumbnails/thumbnail_1.png`(ChatGPT 가 [`thumbnails/thumbnail_1.md`](thumbnails/thumbnail_1.md) 로 만들고 Claude 가 검수해 올림 — 그림 + 첫 문장의 숫자·티커 `SCHD − TAX > SPY` · `+$33K` · `?`)를 화면 가득 (kit.js `K.cover`). 0초 장면 = 앱에서 썸네일로 고를 장면. 그림이 없으면 미리보기는 그림 아이콘 자리(kit.js v1.5 — 언어 없음), 최종 렌더는 멈춘다.

**모양:** 세로 1080×1920 · 롱폼과 같은 짙은 남색 바탕·색 · **자막 없음**(굽지도 올리지도 않음) · 화면 글자는 언어 없이 (`K.init` `noWords` — `render.mjs check` 가 낱말을 잡음) · 음악 없음 · 음량 -14 LUFS.

**화면 자리 (유튜브가 쇼츠 위에 얹는 것을 피함 — `<meta name="video-safe" content="250 150 1500 60">`):**

| 자리 | 세로 위치 | 무엇 |
|---|---|---|
| 위 | 0~250px | 비움 (유튜브 위쪽 아이콘) |
| 가운데 | 250~1500px | 장면 — x 60~930 (오른쪽 150px 은 좋아요·댓글 버튼), 장면 가운데 x 495. 자막 띠가 없어 재테크 쇼츠(1270)보다 아래까지 씀 |
| 아래 | 1500~1920px | 비움 (제목·채널·관련 동영상 링크) — 끝 화면 ⬇ 이 이 링크를 가리킨다 |

**장면 9개:** ① 썸네일 그림 ② SCHD·SPY ③ 경주 시작 BUY $1,000 ④ 배당 −15% · ↺ BUY ⑤ ⇄ 43 ⑥ 2019 배당 +63.1% ⑦ 2022 −14.6%·−22.2% → $33K ⑧ SCHD ＞ SPY ? ⑨ 끝 화면 ⬇ — 장면 파일 [`video/episodes/baedang-etf-2026-10-shorts/index.html`](../../../../video/episodes/baedang-etf-2026-10-shorts/index.html) v1.0. 장면 시각 = 문장·낱말 시각(손으로 적은 초 없음). 경주는 결말 전에서 멈추고, 오른쪽 '?' 띠가 그 뒤(→ 2026)를 가린다.

**도구:**
1. 내레이션 — `tools/tts_narration.py` 가 롱폼 대본과 함께 `shorts/baedang-etf-2026-10-shorts.txt` 도 읽어 `shorts/narration.mp3`·`shorts/tts_narration.json` 을 만든다 (영상ID `baedang-etf-2026-10-shorts`, Kaggle 셀 범위 `stock` 또는 전체 · 진행자 H04 · `voices/ref/host.wav`).
2. 오디오가 오면:
   ```
   cd video && npm run align-audio -- stock baedang-etf-2026-10-shorts --no-export && cd ..
   node video/render/render.mjs sync  stock baedang-etf-2026-10-shorts
   node video/render/render.mjs check stock baedang-etf-2026-10-shorts
   node video/render/render.mjs video stock baedang-etf-2026-10-shorts
   ```
   → `stock/out/baedang-etf-2026-10-shorts/final_1080p.mp4` (git 에 넣지 않음). 지금은 추정 시각의 소리 없는 미리보기 `stock/out/baedang-etf-2026-10-shorts/preview_estimated_silent.mp4` 만 (이 컨테이너에만 — 최종본 아님).
3. 올리기 — 롱폼 공개 뒤. 업로드 도구(`tools/youtube_upload.py`)는 아직 쇼츠 시트를 읽지 않는다 (재테크 쇼츠와 같은 상태 — shorts_insights 7번). 3분 이하 세로 영상은 유튜브가 쇼츠로 본다.

## 4. 설명란 (한국어 — 그대로 복사)

```
미국 배당주 ETF SCHD와 S&P 500 ETF SPY에 2011년부터 매달 1,000달러씩 넣었습니다. 배당은 받을 때마다 15%를 떼고 다시 매수했고요. 2017년까지 앞선 계좌가 43번 바뀌었고, 2022년 하락장에선 SCHD가 14.6%, SPY가 22.2% 줄었습니다. 2023년 1월엔 SCHD가 약 3만 3천 달러 앞섰습니다.
▶ 15년을 모은 두 계좌의 결과는 아래 '관련 동영상'에서 — 배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까?

자료·계산 조건(배당 처리·매수일·수수료)은 본편 설명란에 있습니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
과거 자료로 계산한 결과이며 투자 권유가 아닙니다.
#SCHD #SPY
```
- 해시태그 2개 `#SCHD #SPY` — 두 계좌의 티커. 3~5개 쇼츠의 성공 비율이 6.6%로 가장 낮다 (shorts_insights 4번) · 태그 자체의 효과는 근거 없음.
- 결말(끝 값·10년 결과)은 쓰지 않는다 (`stock/guides/README.md` 2번). 계산 조건 전체는 롱폼 설명란 '실험 방법·재현 조건'에 있다.

## 5. 올리기 설정

| 항목 | 값 |
|---|---|
| 관련 동영상 | **이 롱폼** (`../youtube.json` 의 영상). API 로는 못 건다 → 사용자가 직접: 컴퓨터 스튜디오 → 콘텐츠 → Shorts → 이 쇼츠의 연필(세부정보) → 오른쪽 '관련 동영상' → 이 롱폼 → 저장 (같은 채널·공개된 영상만). 끝 화면 ⬇ 이 그 링크 자리를 가리킴 |
| 썸네일 | 올린 뒤 **유튜브 앱**에서 쇼츠 수정 → 썸네일 → **0초 장면**(첫 문장 그림) · 파트너 프로그램 가입 뒤: 스튜디오에서 `thumbnails/thumbnail_1.png` |
| 올리는 때 | 롱폼 공개 뒤, **월·목 15~17시** 하나씩 (네 편을 한꺼번에 올리지 않음 — 약한 기울기, shorts_insights 6번) |
| 기본 언어 | ko |
| 자막 올리기 | **아니요** (전 세계 대상 — 사용자 지시 2026-10-15) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 공개 범위 | 롱폼과 같은 방식 (비공개 업로드 → 예약 공개) |
| 고정 댓글 | 쓰려면 질문 하나: "배당 ETF와 S&P 500, 15년 모으면 어느 쪽이 더 남을 거라고 보시나요? 결과는 본편에서 확인하세요." — 근거 없음, 시험 |

## 6. 숫자 근거 (쇼츠 대본의 숫자 → 롱폼 대본 문장)

롱폼 숫자는 `backtest/check_numbers.py` 가 결과 파일로 맞춰 봤다. 같은 숫자가 여러 문장에 있으면 첫 문장만 적음 (전부는 `checklist.md`).

| 쇼츠 문장 | 숫자 | 롱폼 문장 | 롱폼 대본 |
|---:|---|---|---|
| 1 | `2023년` | s19 | 2023년 1월 6일에는 SCHD가 약 3만 3천 달러까지 앞섰어요. |
| 1 | `1월` | s12 | 2018년 1월 2일부터는 SPY가 앞섰습니다. |
| 1 | `3만` | s19 | 2023년 1월 6일에는 SCHD가 약 3만 3천 달러까지 앞섰어요. |
| 1 | `3천` | s19 | 2023년 1월 6일에는 SCHD가 약 3만 3천 달러까지 앞섰어요. |
| 2 | `500` | s3 | 미국 배당주 ETF인 SCHD와, S&P 500 ETF인 SPY로 백테스트해 보겠습니다. |
| 3 | `2011년` | s4 | 2011년부터 매달 첫 거래일에 1,000달러씩 매수해요. |
| 3 | `1,000달러` | s4 | 2011년부터 매달 첫 거래일에 1,000달러씩 매수해요. |
| 4 | `15%` | s5 | 배당은 15%를 떼고 다시 매수하고, 수수료는 0.25%예요. |
| 5 | `2017년` | s11 | 2017년까지는 앞선 계좌가 43번 바뀌며, 두 계좌가 엎치락뒤치락했어요. |
| 5 | `43번` | s11 | 2017년까지는 앞선 계좌가 43번 바뀌며, 두 계좌가 엎치락뒤치락했어요. |
| 6 | `2019년` | s13 | 2019년 배당은 SCHD가 SPY보다 63.1% 많았지만, 계좌는 SPY가 앞섰어요. |
| 6 | `63.1%` | s13 | 2019년 배당은 SCHD가 SPY보다 63.1% 많았지만, 계좌는 SPY가 앞섰어요. |
| 7 | `2022년` | s16 | 2022년, 긴 하락장이 왔어요. |
| 7 | `14.6%` | s18 | 그해 SCHD는 14.6%, SPY는 22.2% 줄어, SCHD가 덜 떨어졌어요. |
| 7 | `22.2%` | s18 | 그해 SCHD는 14.6%, SPY는 22.2% 줄어, SCHD가 덜 떨어졌어요. |
| 8 | `15년` | s81 | 세금 15%를 떼고 15년 동안 매달 모았어요. |

## 7. 주의 — 근거와 다른 점 (사용자 지시로 고름)

- 주식 쇼츠 근거의 경주 쇼츠(디히치 ×32~×203)는 **끝 결과까지 보여 준다.** 이 쇼츠는 채널 규칙(결말을 말하지 않음 — `stock/guides/README.md` 2·3번)과 프롤로그형(`guides/shorts_guide.md` 4번)에 따라 **결과를 롱폼에 둔다.** 결말을 가린 효과는 근거 없음 — 올린 뒤 '본편 공개' 불만 댓글 수·관련 동영상 클릭 수로 본다 (shorts_insights 8번).
- 대본(자막·음성인식)이 있는 성공 쇼츠가 0개라 첫 3초·말 속도·끝 문장은 근거 없음 — 롱폼 말투를 그대로 썼다.
- 언어 없는 화면이 해외에서 통하는지는 올린 뒤 시청자 지리로 본다.

## 8. 다음에 할 일

1. 사용자가 소리 없는 미리보기를 보고 장면을 확인 → 썸네일 그림(ChatGPT — `stock/thumbnails_chatgpt.md`) → Claude 검수·업로드.
2. Kaggle 셀(범위 `stock`)로 내레이션 → 3번 '도구' 2 (맞춤·sync·check·video) → 롱폼 공개 뒤 올리기 → 5번 관련 동영상을 사용자가 건다.

## 변경 이력

| 버전 | 날짜 | 내용 |
|---|---|---|
| v1.0.2 | 2026-10-17 | 쇼츠 썸네일 글자 `SCHD − TAX > SPY` · `+$33K` · `?` — 비교·수식 기호 (사용자 지시) |
| v1.0.1 | 2026-10-17 | 쇼츠 썸네일 글자 `SCHD − TAX > SPY` · `+$33K` · `?` (사용자 지시 — 영어·숫자·기호 써도 됨) |
| v1.0 | 2026-10-17 | 새로 만듦 — 대본 9문장 275음절 예상 약 46.8초 · 제목 R1 「배당 ETF, 세금 떼고도 S&P 500보다 3만 3천 달러 앞섰다… 끝까지 앞설까?」 · 9개 언어 제목·설명 · 언어 없는 세로 장면 v1.0 · 숫자 근거 16개 (없음 0) |
