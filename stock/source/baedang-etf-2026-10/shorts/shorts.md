# 쇼츠 — `baedang-etf-2026-10` 결과를 바로 보여 주는 쇼츠 (왜 → 어떻게 → 비교 상대 → 조건 → 결과 → 왜? → 롱폼 · 언어 없는 화면)

버전: v2.1 — 2026-10-17 — **결과형 + 왜·어떻게** (2번 커버드콜 쇼츠 v2.1 과 같은 꼴 — 사용자 지시 2026-10-17 "R1으로 하고 나머지 3개도 수정하고 외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐" · 그 앞 "그래 왜 그런 테스트 했는지 언급을 해줘야 할 거 아니야 … 파이썬 코드로 테스트를 해봤습니다 이렇게 무슨 방법으로 테스트했는지도 말해야지 … 니가 아무것도 모르는 시청자 입장이 되보라고"): 대본 12문장 — 왜(시험할 말) → 어떻게(AI가 짠 파이썬 코드 · 과거 실제 가격 · 백테스트 — 화면에 코드 카드) → 비교 상대와 까닭 → 조건 → 결과 → 왜? → 롱폼에만 있는 것. 제목 R1·R2 = 시험할 말(2줄). 9개 언어 제목·설명 다시 · 언어별 자막 대본 `subs/` (화면에 굽지 않고 CC 로 올림).
(v1.0.4 까지 — 프롤로그형(첫 문장 2023년 1월 약 3만 3천 달러 → 앞선 계좌 43번 → 2019 배당 → 2022 하락 → '결과는 아래 영상') — 결말 가림, 커밋 9b8be2b5.)

- 보내는 곳(롱폼): **배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까?** (`../upload.md` 1번 제목) — 쇼츠의 '관련 동영상'으로 연결 (롱폼 공개 뒤)
- **쇼츠에서 말하는 것:** (왜) 배당 ETF를 오래 모으면 지수 ETF보다 더 남는다는 말을 확인하려고 · (어떻게) AI가 짠 파이썬 코드에 과거 실제 가격을 넣은 백테스트, 미국 배당주 ETF SCHD vs 배당은 적지만 S&P 500을 그대로 따라가는 SPY, 2011년부터 매달 1,000달러, **두 계좌 모두** 배당에 세금 15%를 떼고 다시 매수(15% = 많은 나라에서 미국 배당에 떼는 세율) · (결과) 넣은 돈 18만 달러 · SCHD 약 48만 달러 · SPY 약 59만 달러 · 배당은 SCHD 가 SPY 의 2.1배 · 남은 돈은 SPY 가 1.22배.
- **롱폼에만 남기는 것 (더 보고 싶은 사람에게):** 날짜별 과정(앞선 계좌 43번 바뀜 · 코로나 · 2022년 하락에서 SCHD 가 덜 떨어짐 · 2023년 1월 약 3만 3천 달러 앞섬) · 이유(배당 날 주가가 배당만큼 내려감 · 세금을 일찍 냄) · 해마다 수익률 · 세금 0%·30% · 끝에 모두 매도 · 한 번에 넣기 · 시작 달을 바꾼 계좌 120개 · VYM · 한계. 쇼츠 끝 문장이 '그 이유와, 다른 달에 시작해도 결과가 같은지는'을 부르고 끝 화면이 그림 둘(배당 날 주가가 내려감 ? · 달력 ↻)로 보여 준다.
- 근거: [`stock/guides/shorts_insights.md`](../../../guides/shorts_insights.md) v1.1 (주식 성공 경주 쇼츠는 끝 결과까지 보여 줌 — 결과형과 같은 방향) · 꼴 `stock/guides/README.md` v1.24 7번
- 길이: **12문장 · 예상 약 59.9초** (`render.mjs sync --estimate` — 진행자 H04 실측으로 맞춘 추정) · 결과 첫 숫자 약 34초 · 50자 넘는 문장 없음 · 45~59초 = 비교 집단에서 가장 높은 구간 (shorts_insights 2번)
- 목소리: 진행자 H04 하나 (CLAUDE.md) — 한국어 내레이션, **화면은 소리 없이도 이해되게** · 외국어는 언어별 자막(CC — `subs/<영상ID>-shorts.<언어>.txt` → 오디오 뒤 `tools/subs_tool.py build` 로 SRT) + 자동 더빙
- 숫자: 쇼츠 대본의 숫자는 모두 롱폼 대본에 있다 — `python3 tools/backtest/shorts_numcheck.py stock baedang-etf-2026-10` → [`checklist.md`](checklist.md) (숫자 11개 · 없음 0). 화면 숫자는 그 롱폼의 `backtest/` anim 자료에서만 — 장면 파일이 대본 숫자와 맞춰 보고 다르면 멈춘다.
- ※ 연구·교육용 — 투자 권유가 아님

## 1. 제목

| | 제목 (한국어 — 기본 언어) | 2줄 (`title_fit.py --shorts`) | 까닭 |
|---|---|---|---|
| **R1 (추천)** | **배당 ETF 매달 1,000달러, S&P 500보다 더 남을까?** | ✅ 홈 Shorts 칸·재생 화면·PC 다음 동영상 | 쇼츠가 시험하는 말 그대로 · 맨 앞 핵심 낱말 · 질문 (결과는 영상 안에서) |
| R2 | SCHD vs SPY, 배당 많이 받으면 더 남을까? | ✅ | 같은 질문을 다르게 |

- 제목은 결과를 말하지 않는다 (테스트로 호기심 — 사용자 지시). 결과는 영상 34초부터.

### 1-1. 언어별 제목·설명 (localizations — 롱폼 `upload.md` 5번과 같은 9개 언어)

JSON — 업로드 도구가 읽는 꼴. 설명 = 한국어 설명란(4번)과 같은 뜻 (왜 → 어떻게 → 결과, '▶' 줄 = 롱폼에만 있는 것 + 그 언어의 롱폼 제목). 해시태그는 티커. 숫자 표기는 그 언어 관습.

```
{
 "en": {
  "title": "$1,000 a month in a dividend ETF: more left than the S&P 500?",
  "description": "People say saving in a dividend ETF for years leaves more than an index ETF. To check, we ran a backtest with AI-written Python code on real past prices. From 2011, $1,000 a month went into each of two accounts: SCHD, a US dividend stock ETF, and SPY, which pays smaller dividends but tracks the S&P 500. In both accounts, every dividend had 15% tax withheld (the rate withheld on US dividends in many countries) before being reinvested. By 2026 each had put in $180,000. The SCHD account had about $480,000; the SPY account, about $590,000. SCHD received 2.1 times SPY's dividends, but SPY had 1.22 times as much money left.\n▶ Why — and whether a different start month gives the same result — in the related video below: Dividend ETF saved monthly: after 15% dividend tax, is more left than the same money in the S&P 500?\n\nData and full conditions (dividend handling, fractional shares, 0.25% fee) are in the main video's description. The code was written by AI and the narration is an AI voice.\nPast data only — not investment advice.\n#SCHD #SPY"
 },
 "hi": {
  "title": "डिविडेंड ETF में हर महीने $1,000: क्या S&P 500 से ज़्यादा बचेगा?",
  "description": "कहा जाता है कि डिविडेंड ETF लंबे समय तक जमा करें, तो इंडेक्स ETF से ज़्यादा बचता है। यह जाँचने के लिए हमने AI के लिखे Python कोड से पिछली असली कीमतों पर बैकटेस्ट किया। 2011 से दो खातों में हर महीने $1,000 डाले — एक अमेरिकी डिविडेंड शेयरों के ETF, SCHD में, दूसरा कम डिविडेंड वाले पर S&P 500 को फॉलो करने वाले SPY में। दोनों खातों में हर डिविडेंड से 15% टैक्स कटा (कई देशों में अमेरिकी डिविडेंड पर यही दर कटती है), फिर बाकी से दोबारा खरीदा। 2026 तक दोनों में $180,000 डाले गए। SCHD खाते में लगभग $480,000 और SPY खाते में लगभग $590,000 थे। डिविडेंड SCHD को SPY का 2.1 गुना मिला, पर बचा पैसा SPY में 1.22 गुना था।\n▶ ऐसा क्यों हुआ, और दूसरे महीने से शुरू करने पर भी नतीजा वही रहता है या नहीं — नीचे जुड़े वीडियो में: डिविडेंड ETF हर महीने जमा करें: 15% टैक्स के बाद क्या S&P 500 में उतने ही पैसे से ज़्यादा बचेगा?\n\nडेटा और पूरी शर्तें (डिविडेंड का हिसाब, आंशिक शेयर, 0.25% शुल्क) मुख्य वीडियो के विवरण में हैं। कोड AI ने लिखा और आवाज़ AI की है।\nसिर्फ़ पिछला डेटा — निवेश सलाह नहीं।\n#SCHD #SPY"
 },
 "id": {
  "title": "ETF dividen $1.000 tiap bulan: sisa lebih banyak dari S&P 500?",
  "description": "Katanya menabung ETF dividen dalam waktu lama menyisakan lebih banyak dari ETF indeks. Untuk mengeceknya, kami melakukan backtest dengan kode Python buatan AI pada harga riil masa lalu. Sejak 2011, kami memasukkan masing-masing $1.000 tiap bulan ke SCHD, ETF saham dividen AS, dan ke SPY, yang dividennya kecil tapi mengikuti S&P 500. Di kedua akun, tiap dividen dipotong pajak 15% (tarif yang dipotong dari dividen AS di banyak negara), lalu dibelikan lagi. Sampai 2026 uang yang masuk sama-sama $180.000. Akun SCHD sekitar $480.000, akun SPY sekitar $590.000. Dividen SCHD 2,1 kali SPY, tapi sisa uang SPY 1,22 kali SCHD.\n▶ Kenapa begitu, dan apakah hasilnya sama jika mulai di bulan lain — di video tertaut di bawah: ETF dividen tiap bulan: setelah pajak dividen 15%, sisa lebih banyak dari S&P 500 dengan uang sama?\n\nData dan syarat lengkap (perlakuan dividen, saham pecahan, biaya 0,25%) ada di deskripsi video utama. Kode ditulis AI dan narasinya suara AI.\nHanya data masa lalu — bukan saran investasi.\n#SCHD #SPY"
 },
 "pt": {
  "title": "US$ 1.000 por mês em ETF de dividendos: sobra mais que no S&P 500?",
  "description": "Dizem que acumular um ETF de dividendos por anos deixa mais que um ETF de índice. Para conferir, fizemos um backtest com código Python escrito por IA sobre preços reais do passado. Desde 2011, aplicamos US$ 1.000 por mês em cada conta: SCHD, ETF de ações de dividendos dos EUA, e SPY, que paga menos dividendos mas segue o S&P 500. Nas duas contas, cada dividendo teve 15% de imposto retido (a alíquota retida sobre dividendos dos EUA em muitos países) e foi reinvestido. Até 2026, cada uma aplicou US$ 180.000. A conta de SCHD tinha cerca de US$ 480.000; a de SPY, cerca de US$ 590.000. O SCHD recebeu 2,1 vezes os dividendos do SPY, mas o saldo do SPY foi 1,22 vez o do SCHD.\n▶ Por que isso aconteceu, e se o resultado é o mesmo começando em outro mês — no vídeo vinculado abaixo: ETF de dividendos todo mês: com 15% de imposto, sobra mais que o mesmo dinheiro no S&P 500?\n\nDados e condições completas (tratamento dos dividendos, frações de ações, taxa de 0,25%) na descrição do vídeo principal. O código foi escrito por IA e a narração é voz de IA.\nApenas dados passados — não é recomendação de investimento.\n#SCHD #SPY"
 },
 "es-419": {
  "title": "US$1,000 al mes en un ETF de dividendos: ¿queda más que en el S&P 500?",
  "description": "Dicen que acumular un ETF de dividendos por años deja más que un ETF de índice. Para comprobarlo, hicimos un backtest con código Python escrito por IA sobre precios reales del pasado. Desde 2011 invertimos US$1,000 al mes en cada cuenta: SCHD, un ETF de acciones de dividendos de EE. UU., y SPY, que paga menos dividendos pero sigue el S&P 500. En las dos cuentas, a cada dividendo se le retuvo 15% de impuesto (la tasa retenida a dividendos de EE. UU. en muchos países) y se reinvirtió. Hasta 2026, cada una invirtió US$180,000. La cuenta de SCHD tenía unos US$480,000; la de SPY, unos US$590,000. SCHD recibió 2.1 veces los dividendos de SPY, pero el saldo de SPY fue 1.22 veces el de SCHD.\n▶ Por qué pasó, y si el resultado es el mismo empezando en otro mes — en el video vinculado abajo: ETF de dividendos cada mes: con 15% de impuesto, ¿queda más que el mismo dinero en el S&P 500?\n\nDatos y condiciones completas (manejo de dividendos, fracciones de acciones, comisión de 0.25%) en la descripción del video principal. El código lo escribió una IA y la narración es una voz de IA.\nSolo datos pasados — no es asesoría de inversión.\n#SCHD #SPY"
 },
 "ja": {
  "title": "配当ETFに毎月1,000ドル、S&P 500より多く残る？",
  "description": "配当ETFを長く積み立てると、指数ETFより多く残ると言われます。本当かどうか、AIが書いたPythonコードで過去の実際の価格を使ってバックテストしました。米国の配当株ETF・SCHDと、配当は少ないもののS&P 500にそのまま連動するSPYに、2011年から毎月1,000ドルずつ入れました。どちらの口座も、配当は受け取るたびに税金15%（多くの国で米国の配当に課される税率）を引いて再投資しました。2026年までに入れた額はどちらも18万ドル。SCHDの口座は約48万ドル、SPYの口座は約59万ドルでした。配当はSCHDがSPYの2.1倍受け取りましたが、残ったお金はSPYがSCHDの1.22倍でした。\n▶ その理由と、別の月に始めても結果が同じかどうかは下のリンクの動画で — 高配当ETFを毎月積み立てると、配当税15%を引いても同じ額のS&P 500より多く残る？\n\nデータと計算条件（配当の扱い・端数株・手数料0.25%）は本編の説明欄にあります。計算コードはAIが書き、ナレーションはAI音声です。\n過去データによる計算で、投資の勧誘ではありません。\n#SCHD #SPY"
 },
 "de": {
  "title": "Monatlich 1.000 $ in einen Dividenden-ETF: Bleibt mehr als im S&P 500?",
  "description": "Es heißt, ein lange besparter Dividenden-ETF bringt mehr als ein Index-ETF. Zur Prüfung haben wir mit von KI geschriebenem Python-Code einen Backtest auf echten historischen Kursen gemacht. Ab 2011 flossen monatlich je 1.000 $ in SCHD, einen ETF auf US-Dividendenaktien, und in SPY, der weniger Dividende zahlt, aber den S&P 500 abbildet. In beiden Konten wurden von jeder Dividende 15 % Steuer einbehalten (der Satz, der in vielen Ländern auf US-Dividenden anfällt), der Rest wurde reinvestiert. Bis 2026 zahlte jedes Konto 180.000 $ ein. Das SCHD-Konto hatte rund 480.000 $, das SPY-Konto rund 590.000 $. SCHD bekam das 2,1-Fache an Dividenden von SPY, doch SPY hatte am Ende das 1,22-Fache an Geld.\n▶ Warum – und ob ein anderer Startmonat zum gleichen Ergebnis führt – im verlinkten Video unten: Dividenden-ETF monatlich sparen: Bleibt nach 15 % Steuer mehr als mit gleichem Geld im S&P 500?\n\nDaten und alle Bedingungen (Dividendenbehandlung, Bruchteilsaktien, 0,25 % Gebühr) in der Beschreibung des Hauptvideos. Der Code wurde von einer KI geschrieben, die Stimme ist eine KI-Stimme.\nNur historische Daten – keine Anlageberatung.\n#SCHD #SPY"
 },
 "vi": {
  "title": "Mỗi tháng 1.000 USD vào ETF cổ tức: còn nhiều hơn S&P 500 không?",
  "description": "Người ta nói tích lũy ETF cổ tức lâu dài sẽ còn nhiều hơn ETF chỉ số. Để kiểm tra, chúng tôi chạy backtest bằng mã Python do AI viết trên giá thực tế trong quá khứ. Từ năm 2011, mỗi tháng bỏ 1.000 USD vào mỗi tài khoản: SCHD, ETF cổ phiếu cổ tức Mỹ, và SPY, cổ tức ít hơn nhưng bám theo S&P 500. Ở cả hai tài khoản, mỗi lần nhận cổ tức đều bị trừ thuế 15% (thuế suất khấu trừ cổ tức Mỹ ở nhiều nước) rồi mua lại. Đến năm 2026, mỗi bên đã bỏ vào 180.000 USD. Tài khoản SCHD khoảng 480.000 USD, tài khoản SPY khoảng 590.000 USD. SCHD nhận cổ tức gấp 2,1 lần SPY, nhưng tiền còn lại của SPY gấp 1,22 lần SCHD.\n▶ Vì sao, và nếu bắt đầu vào tháng khác thì kết quả có giống không — xem ở video liên kết bên dưới: Tích lũy ETF cổ tức mỗi tháng: sau thuế cổ tức 15%, có còn nhiều hơn S&P 500 với cùng số tiền?\n\nDữ liệu và điều kiện đầy đủ (cách xử lý cổ tức, cổ phiếu lẻ, phí 0,25%) trong phần mô tả video chính. Mã do AI viết, lời thuyết minh là giọng AI.\nChỉ là dữ liệu quá khứ — không phải lời khuyên đầu tư.\n#SCHD #SPY"
 },
 "tr": {
  "title": "Temettü ETF'sine her ay 1.000 $: S&P 500'den fazla kalır mı?",
  "description": "Temettü ETF'si uzun süre biriktirilirse endeks ETF'sinden fazla kaldığı söylenir. Bunu kontrol etmek için yapay zekânın yazdığı Python koduyla geçmişteki gerçek fiyatlar üzerinde backtest yaptık. 2011'den itibaren her ay ABD temettü hisseleri ETF'si SCHD'ye ve temettüsü düşük ama S&P 500'ü izleyen SPY'ye ayrı ayrı 1.000 $ koyduk. İki hesapta da her temettüden %15 vergi (birçok ülkede ABD temettüsünden kesilen oran) kesildi, sonra yeniden alım yapıldı. 2026'ya kadar her hesaba 180.000 $ kondu. SCHD hesabı yaklaşık 480.000 $, SPY hesabı yaklaşık 590.000 $ oldu. SCHD, SPY'nin 2,1 katı temettü aldı; ama SPY'de kalan para SCHD'nin 1,22 katıydı.\n▶ Nedeni ve başka bir ayda başlayınca sonucun aynı olup olmadığı aşağıdaki bağlantılı videoda: Temettü ETF'si her ay biriktirilirse %15 vergiden sonra aynı parayla S&P 500'den fazla kalır mı?\n\nVeriler ve tüm koşullar (temettü işlemi, kesirli hisse, %0,25 komisyon) ana videonun açıklamasında. Kodu yapay zekâ yazdı, seslendirme yapay zekâ sesi.\nYalnızca geçmiş veriler — yatırım tavsiyesi değildir.\n#SCHD #SPY"
 }
}
```

## 2. 대본 (시각은 예상 — 내레이션 뒤 실제 시각으로 맞춤)

| # | 시각 | 대본 | 역할 | 화면 (언어 없음 — 숫자·$·%·×·연도·티커·기호·아이콘) |
|---|---|---|---|---|
| 1 | 0:00 | 배당 ETF를 오래 모으면, 지수 ETF보다 더 남는다고들 하죠. | **왜** — 시험할 말 | **쇼츠 썸네일 그림** (`SCHD > SPY ?` — 같은 크기 두 나무, 둘 다 동전 + 빨간 조각, 줄다리기 매듭은 정확히 가운데) |
| 2 | 0:05 | 정말 그런지, AI가 짠 파이썬 코드로 과거 실제 가격을 넣어 백테스트해 봤습니다. | **어떻게** | 흰 가격 선 + **코드 카드** `income.py` (`tools/backtest/income.py` `reinvest()` 의 실제 줄 — `net = g * (1 - tax)` · `sh += net * (1 - fee) / c[i]` · `sh += monthly * (1 - fee) / c[i]`) |
| 3 | 0:11 | 시험한 건 미국 배당주 ETF인 SCHD예요. | 시험한 것 | 카드 `SCHD` (보라) + 동전 많은 나무 |
| 4 | 0:14 | 비교 상대는 배당은 적지만 S&P 500을 그대로 따라가는 ETF, SPY입니다. | 비교 상대와 고른 까닭 | 카드 `SPY` (파랑) · `S&P 500` + 동전 하나 나무 |
| 5 | 0:21 | 2011년부터 두 계좌에 매달 1,000달러씩 넣었어요. | 조건 ① | 경주 화면 2011.11.01 · 넣은 돈 노란 점선 · 칩 `$1,000` |
| 6 | 0:24 | 두 계좌 모두, 배당은 받을 때마다 세금 15%를 떼고 다시 매수했고요. | 조건 ② (두 계좌 모두) | 날짜가 흐름 · 배당 날마다 두 선 끝에서 동전 + 빨간 조각 · 위 오른쪽 `🪙 −15% → BUY` · 아래 칸 SCHD·SPY 값·받은 배당 / 넣은 돈 |
| 7 | 0:30 | 15%는 많은 나라에서 미국 배당에 떼는 세율이에요. | 15% 의 까닭 | 🌐 `15%` (위 왼쪽) |
| 8 | 0:34 | 2026년까지 두 계좌 모두 18만 달러를 넣었어요. | **결과 ①** | 경주가 2026.10.15 에 닿음 · 칩 `$180,000` · 넣은 돈 칸 깜빡 |
| 9 | 0:37 | SCHD 계좌는 약 48만 달러, SPY 계좌는 약 59만 달러였어요. | **결과 ②** | SCHD `$483,585` · SPY `$589,704` 칸 깜빡 |
| 10 | 0:43 | 배당은 SCHD가 SPY의 2.1배를 받았지만, 남은 돈은 SPY가 1.22배 많았어요. | **결과 ③** | 위 왼쪽 큰 글자: `SCHD 🪙 ×2.1` → `SPY ×1.22` · SCHD 끝 → SPY 끝 노란 점선 |
| 11 | 0:51 | 배당을 더 많이 받았는데, 왜 덜 남았을까요? | 호기심 (왜?) | 두 선 사이를 노랗게 · 큰 `?` |
| 12 | 0:54 | 그 이유와, 다른 달에 시작해도 결과가 같은지는 아래 영상에서 확인하세요. | 롱폼 안내 | 끝 화면: `SCHD` `SPY` · 그림 둘(배당 날 주가가 내려감 `?` · 달력 ↻) · 노란 ⬇ |

- **아무것도 모르는 시청자가 '뭐야? 왜 이렇게 했고 어떻게 했다는 거야?'라고 묻지 않게** — 왜·어떻게·비교 상대와 까닭·공정한 조건은 빼지 않는다 (`stock/guides/README.md` 7번 · `guides/script_guide.md` 피드백 21).
- 롱폼과 같은 색 = 같은 계좌. 끝인사("시청해주셔서 감사합니다.")는 넣지 않는다 (`guides/shorts_guide.md` 4번).
- 대본 TXT (내레이션용): [`baedang-etf-2026-10-shorts.txt`](baedang-etf-2026-10-shorts.txt) · 언어별 자막 대본: [`subs/`](subs/) (`python3 tools/subs_tool.py check stock baedang-etf-2026-10-shorts`)

## 3. 영상 만드는 법 (오디오가 생긴 뒤 — CLAUDE.md '오디오 먼저')

**첫 문장 = 쇼츠 썸네일 그림:** 0초부터 첫 문장(시험할 말)이 끝날 때까지 `thumbnails/thumbnail_1.png` (ChatGPT 가 [`thumbnails/thumbnail_1.md`](thumbnails/thumbnail_1.md) 로 만들고 Claude 가 검수 — 글자 `SCHD > SPY ?`)를 화면 가득 (kit.js `K.cover`). 빈 띠가 있으면 `tools/cover_check.py` 로 재고 `K.cover(…, { box })`.

**모양:** 세로 1080×1920 · 롱폼과 같은 짙은 남색 바탕·색 · **화면에 자막을 굽지 않음** (언어별 자막은 CC 로 올림) · 화면 글자는 언어 없이 (`K.init` `noWords`) · 음악 없음 · 음량 -14 LUFS.

**화면 자리 — 가운데·크게** (`guides/video_guide.md` v4.13 6번, `<meta name="video-safe" content="150 60 1320 60">`): 장면 파일 v2.1 은 화면 좌표를 바로 씀 (가운데 x 540), 글자·그림 y 160~1316, 아래 1320~1920 은 비움 (제목·관련 동영상 링크 — 끝 화면 ⬇ 이 가리킴).

**장면:** 2번 표 — 장면 파일 [`video/episodes/baedang-etf-2026-10-shorts/index.html`](../../../../video/episodes/baedang-etf-2026-10-shorts/index.html) v2.1 (check 문제 0 · 완성 mp4 장면을 직접 봄). 장면 시각 = 문장·낱말 시각(손으로 적은 초 없음).

**도구:**
1. 내레이션 — Kaggle 셀 범위 `stock` (영상ID `baedang-etf-2026-10-shorts` — `shorts/narration.mp3`·`shorts/tts_narration.json`).
2. 오디오가 오면:
   ```
   cd video && npm run align-audio -- stock baedang-etf-2026-10-shorts --no-export && cd ..
   node video/render/render.mjs sync  stock baedang-etf-2026-10-shorts
   node video/render/render.mjs check stock baedang-etf-2026-10-shorts
   node video/render/render.mjs video stock baedang-etf-2026-10-shorts
   python3 tools/subs_tool.py build stock baedang-etf-2026-10-shorts        # 언어별 SRT (오디오 시각) → shorts/subs/
   ```
   → `stock/out/baedang-etf-2026-10-shorts/final_1080p.mp4` (git 밖) → **완성 mp4 장면을 Claude 가 직접 본다**. 지금은 추정 시각의 소리 없는 미리보기 `stock/out/baedang-etf-2026-10-shorts/preview_estimated_silent.mp4` 만.
3. 올리기 — `tools/youtube_upload.py` v1.12 가 쇼츠 시트 `shorts/upload.md`(아직 없음 — 다음 할 일)를 읽고 한국어 + 언어별 자막(CC)을 올림. 자막 하나 400단위 — 할당량이 모자라면 `--captions-only` 로 다음 날. 롱폼과 같은 시각에 공개 (`guides/upload_guide.md` 12번).

## 4. 설명란 (한국어 — 그대로 복사)

```
배당 ETF를 오래 모으면 지수 ETF보다 더 남는다고들 하죠. 정말 그런지 AI가 짠 파이썬 코드로 과거 실제 가격을 넣어 백테스트했습니다. 미국 배당주 ETF인 SCHD와, 배당은 적지만 S&P 500을 그대로 따라가는 SPY에 2011년부터 매달 1,000달러씩 넣었어요. 두 계좌 모두 배당은 받을 때마다 세금 15%(많은 나라에서 미국 배당에 떼는 세율)를 떼고 다시 매수했습니다. 2026년까지 넣은 돈은 둘 다 18만 달러. SCHD 계좌는 약 48만 달러, SPY 계좌는 약 59만 달러였어요. 배당은 SCHD가 SPY의 2.1배를 받았지만, 남은 돈은 SPY가 1.22배 많았습니다.
▶ 그 이유와, 다른 달에 시작해도 결과가 같은지는 아래 '관련 동영상'에서 — 배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까?

자료·계산 조건(배당 처리, 소수점 주식, 수수료 0.25%)은 본편 설명란에 있습니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
과거 자료로 계산한 결과이며 투자 권유가 아닙니다.
#SCHD #SPY
```
- 해시태그 2개 `#SCHD #SPY` (shorts_insights 4번 — 3~5개가 가장 낮음).
- 왜·어떻게·결과는 쓰고(영상과 같음), **롱폼에만 있는 것은 쓰지 않는다** — 롱폼으로 가는 까닭.

## 5. 올리기 설정

| 항목 | 값 |
|---|---|
| 관련 동영상 | **이 롱폼** (`../youtube.json`). API 로는 못 건다 → 사용자가 스튜디오 → 콘텐츠 → Shorts → 이 쇼츠 세부정보 → '관련 동영상' |
| 썸네일 | `youtube_upload.py` 가 세로 720×1280 으로 올림 (빈 띠 그림이면 완성 영상 0초 장면) |
| 올리는 때 | 롱폼과 **같은 시각에 공개** (`guides/upload_guide.md` 12번) |
| 기본 언어 | ko |
| 자막 올리기 | **언어별** (한국어 + en·hi·id·pt·es-419·ja·de·vi·tr — 화면에 굽지 않고 CC, 사용자 지시 2026-10-17) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 공개 범위 | 롱폼과 같은 방식 (비공개 업로드 → 예약 공개) |

## 6. 숫자 근거 (쇼츠 대본의 숫자 → 롱폼 대본 문장)

롱폼 숫자는 `backtest/check_numbers.py` 가 결과 파일로 맞춰 봤다 (전부는 `checklist.md`).

| 쇼츠 문장 | 숫자 | 롱폼 문장 | 롱폼 대본 |
|---:|---|---|---|
| 4 | `500` | s3 | 미국 배당주 ETF인 SCHD와, S&P 500 ETF인 SPY로 백테스트해 보겠습니다. |
| 5 | `2011년` · `1,000달러` | s4 | 2011년부터 매달 첫 거래일에 1,000달러씩 매수해요. |
| 6 | `15%` | s5 | 배당은 15%를 떼고 다시 매수하고, 수수료는 0.25%예요. |
| 7 | `15%` | s5 | 배당은 15%를 떼고 다시 매수하고, 수수료는 0.25%예요. |
| 8 | `2026년` | s22 | 2026년 10월 15일, 결과입니다. |
| 8 | `18만` | s23 | 두 계좌 모두 180번, 18만 달러를 넣었어요. |
| 9 | `48만` · `59만` | s24 | SCHD 계좌는 약 48만 달러, SPY 계좌는 약 59만 달러였어요. |
| 10 | `1.22배` | s25 | SPY 계좌가 1.22배, 약 11만 달러 더 많았습니다. |
| 10 | `2.1배` | s28 | 받은 배당은 SCHD가 약 8만 7천 달러로, SPY의 2.1배였어요. |

## 7. 주의 — 근거와 다른 점·한계

- **결과를 쇼츠에서 말한다** (사용자 지시) — 롱폼으로 넘어오는지는 근거 없음 → 올린 뒤 '관련 동영상' 클릭 수·롱폼 트래픽 소스 'Shorts 피드' (shorts_insights 8번).
- 쇼츠의 결과는 한 가지 시작 날·한 가지 조건의 결과다 — 다른 조건·시작 시점은 롱폼에 (설명란 '▶' 줄).
- 대본이 있는 성공 쇼츠가 0개라 첫 3초·말 속도는 근거 없음. 언어 없는 화면 + 언어별 자막이 해외에서 통하는지는 올린 뒤 시청자 지리·자막 언어로 본다.

## 8. 다음에 할 일

1. 사용자가 소리 없는 미리보기를 확인 → 썸네일 그림(ChatGPT — `stock/thumbnails_chatgpt.md`) → Claude 검수·업로드.
2. 쇼츠 업로드 시트 `shorts/upload.md` (업로드 도구 v1.12 꼴 — 자막 올리기 '언어별').
3. Kaggle 내레이션(범위 `stock`) → 3번 '도구' 2 → 롱폼과 같은 시각에 올리기 → 관련 동영상을 사용자가 건다.

## 변경 이력

| 버전 | 날짜 | 내용 |
|---|---|---|
| v2.1 | 2026-10-17 | 결과형 + 왜·어떻게 — 대본 12문장 예상 약 59.9초 · 제목 R1 「배당 ETF 매달 1,000달러, S&P 500보다 더 남을까?」 · 9개 언어 제목·설명 · 언어별 자막 대본 · 장면 v2.1 (가운데·크게, 코드 카드, 경주 끝까지) · 썸네일 글자 `SCHD > SPY ?`만 · 숫자 11개 없음 0 (사용자 지시) |
|---|---|---|
| v1.0.4 | 2026-10-17 | 쇼츠 썸네일 글자 `SCHD > SPY ?` · `+$33K` — 큰 부등호 머리글 (사용자 지시) |
| v1.0.3 | 2026-10-17 | 쇼츠 썸네일 글자 `+$33K` · `SCHD` · `SPY` — 딱 봤을 때 이해되는 것만 (사용자 지시) |
| v1.0.2 | 2026-10-17 | 쇼츠 썸네일 글자 `SCHD − TAX > SPY` · `+$33K` · `?` — 비교·수식 기호 (사용자 지시) |
| v1.0.1 | 2026-10-17 | 쇼츠 썸네일 글자 `+$33K` · `SCHD` · `SPY` · `?` (사용자 지시 — 영어·숫자·기호 써도 됨) |
| v1.0 | 2026-10-17 | 새로 만듦 — 대본 9문장 275음절 예상 약 46.8초 · 제목 R1 「배당 ETF, 세금 떼고도 S&P 500보다 3만 3천 달러 앞섰다… 끝까지 앞설까?」 · 9개 언어 제목·설명 · 언어 없는 세로 장면 v1.0 · 숫자 근거 16개 (없음 0) |
