# baedang-etf-2026-10-shorts 업로드 시트 (주식 쇼츠)

버전: v1.0 — 2026-10-18 — 새로 만듦: `shorts.md` v2.1 의 제목 R1 · 설명란(4번) · 언어별 제목·설명(1-1)을 업로드 도구가 읽는 꼴로 옮김 · 자막 언어별 (사용자 지시 2026-10-18 "채권 표현 수정하고 영상 업로드 할 준비해").

기준 파일: 쇼츠 대본 `baedang-etf-2026-10-shorts.txt` (12문장) · SRT 문장 12 / 자막 14 (`align-audio` 로 오디오에 맞춤) · 오디오 `narration.mp3` 59.9초 · 올릴 영상 = `stock/out/baedang-etf-2026-10-shorts/final_1080p.mp4` (이 클라우드 컨테이너에만 — git 에 넣지 않음, 장면 파일·오디오로 다시 만듦)

> 업로드: `python3 tools/youtube_upload.py stock baedang-etf-2026-10-shorts --dry-run` → `--publish-at <시각>` (비공개로 올리고 그 시각에 공개). 롱폼 `baedang-etf-2026-10` 과 **같은 시각에 공개** (`guides/upload_guide.md` 12번). 자막은 한국어 + 9개 언어 = 10개(4,000단위) — 할당량이 모자라면 남은 언어는 `--captions-only` 로 다음 날.
> ※ 연구·교육용 — 투자 권유가 아님.

## 1. 제목 (`shorts.md` R1, `title_fit.py --shorts` 2줄 안)

```
배당 ETF 매달 1,000달러, S&P 500보다 더 남을까?
```

## 2. 설명란 (`shorts.md` 4번 그대로)

```
배당 ETF를 오래 모으면 지수 ETF보다 더 남는다고들 하죠. 정말 그런지 AI가 짠 파이썬 코드로 과거 실제 가격을 넣어 백테스트했습니다. 미국 배당주 ETF인 SCHD와, 배당은 적지만 S&P 500을 그대로 따라가는 SPY에 2011년부터 매달 1,000달러씩 넣었어요. 두 계좌 모두 배당은 받을 때마다 세금 15%(많은 나라에서 미국 배당에 떼는 세율)를 떼고 다시 매수했습니다. 2026년까지 넣은 돈은 둘 다 18만 달러. SCHD 계좌는 약 48만 달러, SPY 계좌는 약 59만 달러였어요. 배당은 SCHD가 SPY의 2.1배를 받았지만, 남은 돈은 SPY가 1.22배 많았습니다.
▶ 그 이유와, 다른 달에 시작해도 결과가 같은지는 아래 '관련 동영상'에서 — 배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까?

자료·계산 조건(배당 처리, 소수점 주식, 수수료 0.25%)은 본편 설명란에 있습니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
과거 자료로 계산한 결과이며 투자 권유가 아닙니다.
#SCHD #SPY
```

## 3. 언어별 제목·설명 (`shorts.md` 1-1 그대로 — 9개 언어, 업로드 도구 v1.6 localizations)

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

## 4. 태그

```
SCHD, SPY, 배당 ETF, 배당주, 배당 재투자, 배당세, S&P 500, 백테스트, dividend ETF, backtest
```

## 6. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 범위 | 비공개로 올리고 예약 시각에 공개 (`--publish-at`) — 롱폼과 같은 시각 |
| 기본 언어 | ko |
| 자막 올리기 | **언어별** (한국어 `baedang-etf-2026-10-shorts.srt` + `subs/baedang-etf-2026-10-shorts.<언어>.srt` 9개 — 화면에는 굽지 않음, `stock/guides/README.md` v1.24 4번) |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 썸네일 | `thumbnails/thumbnail_1.png` (세로 9:16 — 그림이 화면 끝까지) → 도구가 세로 720×1280 JPG 로 올림 · 0초 장면도 같은 그림 · 공개 뒤 `i.ytimg.com/vi/<ID>/oardefault.jpg` 로 확인 |
| 관련 동영상 | 롱폼 `baedang-etf-2026-10` 「배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까?」 (`../youtube.json`) — 스튜디오 → 콘텐츠 → Shorts → 연필 → '관련 동영상' (API 로 못 검 — 사용자가 직접) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |

## 7. 결과 (업로드 후)
- (올린 뒤 `youtube.json` 의 영상 ID·예약 시각·자막 언어를 적는다)
