# keobeodeu-kol-2026-10 업로드 시트

버전: v1.6 — 2026-10-18 — 제목을 2줄 안으로 줄임 · 설명란 = 첫 설명(간단히) + 챕터(괄호 영어) + 자료 + 알려 드립니다, 각 아래 영어 (실험 방법·재현 조건 단락은 지움) · 태그에 영어 더함 · 그 밖(기본 언어 ko·언어별·고정 댓글)은 원래대로 (사용자 지시 2026-10-18 "설명에 맨처음 설명(최대한 간단하게) 챕터, 자료, 알려 드립니다 만 남기고 나머지는 지워 그리고 각 밑 부분에 영어로 번역해서 쓰고 챕터는 각각 챕터 옆에 괄호 안에 영어로 번역해서 넣어 그렇게 수정하고 태그에 영어도 포함해 그리고 나머지는 원래대로 돌리자" · "한국어 제목 잘리잖아 안질리도록 영상 제목 다시 수정해봐").
(v1.5 — 2026-10-18 — 기본 언어 en 판은 되돌림)
(v1.4.1 — 2026-10-17 — 업로드 설정 '자막 올리기' = **언어별** (한국어 + 9개 언어 CC — 화면에는 굽지 않음, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") · 자막 대본 `subs/<영상ID>.<언어>.txt` 9개.)
(v1.4 — 2026-10-17 — 대본 v1.4 (티커 설명 (사용자 지시 2026-10-17 "일단 티커에 대한 설명도 추가해 예를 들어 'S&P500을 추종하는 ETF인 SPY' 이런식으로 다 수정해보고")) — 챕터·문장 수 다시.)
(v1.3 — 2026-10-17 — 대본 v1.3 (사용자가 붙인 ChatGPT 페르소나 검토 2차 '네 영상에 공통으로 반복되는 문제 5개'): 2번 설명란과 5번 언어별 설명 9개에 **재현 조건** 한 단락 (가격 자료·배당 처리·매수 날·ETF 보수) · 챕터 다시 계산.)
(v1.2 — 2026-10-17 — 대본 v1.2 (사용자가 붙인 ChatGPT 페르소나 검토 2026-10-17 '네 영상에 반복되는 문제 5개' — 경주 해설은 대표 장면만, 조건을 앞에서 분명히, 숫자와 뜻을 한 문장에, 말하는 금액은 어림(만 단위 하나), 한계에 결정 조건): 챕터 다시 계산 (문장 번호 바뀜).)
(v1.1 — 2026-10-17 — 대본 v1.1 (도입 + 규칙 약 23초 — 사용자 지시 2026-10-17 "야 너 내가 테스트 들어가지 전 도입 및 규칙 설명 30초 넘기지 말라고 했잖아 근데 왜 안지켜 다시 수정해"): 챕터 다시 계산 — 규칙 챕터는 첫 챕터에 합침(10초 미만이 될 수 있어서), 설명 챕터는 결과 뒤. (v1.0 — 2026-10-16 — 최초 (주식 2번 커버드콜 원금 — `backtest/run.py` v1.0). 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐". `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음.))
기준 파일: 대본 v1.4 (98문장) · SRT 문장 98 (추정 시각 — 오디오가 생기면 다시) · 결과 `backtest/results.json` · 올릴 영상 = 렌더 원본 `stock/out/keobeodeu-kol-2026-10/final_1080p.mp4` (오디오가 생긴 뒤 — 지금 있는 `preview_estimated_silent.mp4` 는 소리 없는 미리보기라 올리지 않음)

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json` — 업로드 도구 v1.7 이 채널이 다르면 올리지 않음)로 `python tools/youtube_upload.py stock keobeodeu-kol-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (한국어 — 기본 언어 · 모바일·PC 목록 2줄 안 `title_fit.py` ✅ · 예전 「커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까?」은 잘려서 줄임)

```
커버드콜 분배금, 매달 꺼내 써도 QQQ보다 더 남을까?
```

## 2. 설명란 (첫 설명 · 챕터 · 자료 · 알려 드립니다 — 각 아래 영어, 챕터는 괄호 영어 · 시각은 업로드 도구가 SRT 로 다시 계산)

```
분배금을 매달 꺼내 써도 원금은 지켜질까요? 커버드콜 ETF QYLD와 QQQ에 10만 달러씩 넣고, 같은 날 같은 금액을 꺼내며 13년을 AI가 짠 파이썬 코드로 백테스트했습니다.
Spend the payouts every month — is the principal safe? We put $100,000 each in QYLD (a covered call ETF) and QQQ, took out the same amount on the same days, and backtested 13 years with AI-written Python code.

■ 챕터 (Chapters)
0:00 커버드콜 분배금, 원금은? (Covered call: is the money safe?)
0:25 2013년부터 날짜를 흘려 보면 (From 2013, day by day)
1:35 2022년 긴 하락 (2022: a long fall)
2:20 2025년부터 끝까지 (2025 to the end)
2:36 13년 결과 (13-year result)
3:12 커버드콜은 어떻게 분배금을 만드나 (How covered calls pay)
4:06 시작한 달을 바꾸면 (Other start months)
5:03 XYLD·JEPI도 같을까 (XYLD & JEPI too?)
6:04 세금·다시 매수하면 (Tax & reinvest)
6:43 정리 (Summary)
7:12 이 실험의 한계 (Limits)

■ 자료 (Data)
일별 종가·분배금: Yahoo Finance 차트 API
Daily close & payouts: Yahoo Finance chart API

■ 알려 드립니다 (Notice)
과거 자료로 계산한 결과이며 앞으로도 같다는 보장은 없습니다. 특정 상품을 매수·매도하라는 이야기가 아니며 투자 권유가 아닙니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
These results come from past data — the future may be different. This is not a tip to buy or sell any product and not investment advice. The code was written by AI and the narration is an AI voice.

#커버드콜 #백테스트 #QYLD
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/keobeodeu-kol-2026-10/keobeodeu-kol-2026-10.txt stock/source/keobeodeu-kol-2026-10/keobeodeu-kol-2026-10.srt --chapters "1=커버드콜 분배금, 원금은?;7=2013년부터 날짜를 흘려 보면;21=2022년 긴 하락;30=2025년부터 끝까지;33=13년 결과;40=커버드콜은 어떻게 분배금을 만드나;51=시작한 달을 바꾸면;64=XYLD·JEPI도 같을까;76=세금·다시 매수하면;84=정리;90=이 실험의 한계"
```
- 2026-10-17 추정 시각(오디오 전, 대본 v1.4)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 올릴 때 오디오에 맞춘 SRT로 다시 계산해 2번 설명란에 넣는다.
- 챕터 이름에 결과를 쓰지 않는다.

## 4. 태그 (한국어 + 영어)

```
커버드콜, 커버드콜 ETF, 분배금, 원금, QYLD, QQQ, XYLD, JEPI, 나스닥100, 월배당, 은퇴 생활비, 백테스트, covered call, backtest, dividend income, covered call ETF, monthly dividend, Nasdaq 100, retirement income, Python backtest, investing
```

## 5. 언어별 제목·설명 (localizations)

JSON — 업로드 도구가 그대로 읽는다. 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜).

```
{
 "en": {
  "title": "Covered call payouts spent monthly: is more principal left after 13 years than selling QQQ?",
  "description": "Covered call ETFs pay every month and are said to keep your principal. If you spend the payouts every month, is the principal really kept?\nWe put the same $100,000 into a Nasdaq-100 covered call ETF (QYLD) and into QQQ, which follows the same Nasdaq-100. Every time QYLD paid out, we spent all of it; from QQQ we sold the same amount on the same day. Both accounts took out exactly the same cash. December 2013 to October 2026, 0.25% fee per trade, before tax. As the dates roll forward, the two account values, the cash taken out and the principal (one box = $100,000) change in real time.\nChecks: 94 five-year and 118 three-year accounts started in different months, XYLD vs SPY, JEPI vs SPY, 15% withholding tax, and reinvesting the payouts. The code was written by AI and tested for look-ahead bias. Inflation, currency and country taxes are not included. The narration is an AI voice.\nReproduction details: Yahoo split-adjusted closes and distributions (counted on the ex-date). Both accounts buy at the start-date close with $100,000 minus the 0.25% fee (fractional shares) — QYLD 2013-12-12, XYLD 2013-06-24, JEPI 2020-05-21. Each distribution is taken out in full on the ex-date; the index ETF sells, at that day's close, enough to hand over the same cash after the fee. QQQ/SPY dividends are reinvested the same day. ETF expense ratios are already in the prices.\nData: Yahoo Finance (daily closes and distributions).\nPast results do not guarantee future returns. This video is for education only and is not investment advice."
 },
 "hi": {
  "title": "कवर्ड कॉल भुगतान हर महीने खर्च करें तो क्या 13 साल बाद QQQ बेचने से ज़्यादा मूलधन बचेगा?",
  "description": "कवर्ड कॉल ETF हर महीने भुगतान देते हैं और कहा जाता है कि मूलधन बचा रहता है। अगर हर महीने भुगतान खर्च करें तो क्या मूलधन सच में बचता है?\nहमने वही $100,000 नैस्डैक-100 कवर्ड कॉल ETF (QYLD) और उसी नैस्डैक-100 को फॉलो करने वाले QQQ में लगाए। QYLD के हर भुगतान को पूरा खर्च किया और QQQ से उसी दिन उतनी ही रकम बेची — दोनों खातों से बिल्कुल बराबर पैसा निकला। दिसंबर 2013 से अक्टूबर 2026, हर सौदे पर 0.25% शुल्क, टैक्स से पहले।\nजाँच: अलग-अलग महीनों में शुरू हुए 5 साल के 94 और 3 साल के 118 खाते, XYLD बनाम SPY, JEPI बनाम SPY, 15% टैक्स, और भुगतान दोबारा निवेश। कोड AI ने लिखा। वॉइस-ओवर AI आवाज़ है।\nदोबारा जाँचने के लिए: Yahoo के स्प्लिट-समायोजित बंद भाव और वितरण (एक्स-डेट के हिसाब से)। दोनों खाते शुरुआती दिन के बंद भाव पर $100,000 में से 0.25% शुल्क घटाकर खरीदते हैं (आंशिक शेयर) — QYLD 2013-12-12, XYLD 2013-06-24, JEPI 2020-05-21। हर वितरण एक्स-डेट पर पूरा निकाला जाता है; इंडेक्स ETF उसी दिन के बंद भाव पर इतना बेचता है कि शुल्क के बाद उतनी ही नकदी मिले। QQQ/SPY का डिविडेंड उसी दिन दोबारा लगाया जाता है। ETF का खर्च अनुपात कीमतों में पहले से शामिल है।\nडेटा: Yahoo Finance।\nपिछले नतीजे भविष्य की गारंटी नहीं हैं। यह वीडियो केवल शिक्षा के लिए है, निवेश सलाह नहीं।"
 },
 "id": {
  "title": "Dividen covered call dipakai tiap bulan: apakah modal tersisa lebih banyak dari jual QQQ, 13 tahun?",
  "description": "ETF covered call membayar tiap bulan dan katanya modal tetap terjaga. Jika pembayarannya dipakai setiap bulan, apakah modal benar-benar terjaga?\nKami menaruh $100.000 yang sama di ETF covered call Nasdaq-100 (QYLD) dan di QQQ yang mengikuti Nasdaq-100 yang sama. Setiap QYLD membayar, semuanya kami pakai; dari QQQ kami jual jumlah yang sama di hari yang sama. Kedua akun menarik uang yang persis sama. Desember 2013 sampai Oktober 2026, biaya 0,25% per transaksi, sebelum pajak.\nPengecekan: 94 akun 5 tahun dan 118 akun 3 tahun dengan bulan mulai berbeda, XYLD vs SPY, JEPI vs SPY, pajak 15%, dan menginvestasikan kembali pembayaran. Kode ditulis oleh AI. Narasi memakai suara AI.\nDetail untuk mengulang: harga penutupan Yahoo yang disesuaikan split dan distribusi (dihitung pada tanggal ex). Kedua akun membeli di harga penutupan hari pertama dengan $100.000 dikurangi biaya 0,25% (saham pecahan) — QYLD 2013-12-12, XYLD 2013-06-24, JEPI 2020-05-21. Setiap distribusi diambil penuh pada tanggal ex; ETF indeks menjual di harga penutupan hari itu sebanyak yang perlu agar setelah biaya uang tunainya sama. Dividen QQQ/SPY diinvestasikan kembali pada hari yang sama. Biaya pengelolaan ETF sudah termasuk dalam harga.\nData: Yahoo Finance.\nHasil masa lalu tidak menjamin hasil masa depan. Video ini hanya untuk edukasi, bukan saran investasi."
 },
 "pt": {
  "title": "Renda de covered call gasta todo mês: sobra mais capital em 13 anos do que vendendo QQQ?",
  "description": "ETFs de covered call pagam todo mês e dizem que preservam o capital. Se você gastar os pagamentos todo mês, o capital é mesmo preservado?\nColocamos os mesmos US$ 100.000 num ETF de covered call do Nasdaq-100 (QYLD) e no QQQ, que segue o mesmo Nasdaq-100. A cada pagamento do QYLD gastamos tudo; do QQQ vendemos o mesmo valor no mesmo dia. As duas contas retiraram exatamente o mesmo dinheiro. Dezembro de 2013 a outubro de 2026, taxa de 0,25% por operação, antes de impostos.\nVerificações: 94 contas de 5 anos e 118 de 3 anos iniciadas em meses diferentes, XYLD vs SPY, JEPI vs SPY, imposto de 15% e reinvestimento dos pagamentos. O código foi escrito por IA. A narração é uma voz de IA.\nDetalhes para reproduzir: fechamentos da Yahoo ajustados por desdobramentos e distribuições (contadas na data ex). As duas contas compram no fechamento da data inicial com US$ 100.000 menos a taxa de 0,25% (frações de cotas) — QYLD 2013-12-12, XYLD 2013-06-24, JEPI 2020-05-21. Cada distribuição é retirada inteira na data ex; o ETF de índice vende, no fechamento do dia, o suficiente para entregar o mesmo valor depois da taxa. Os dividendos de QQQ/SPY são reinvestidos no mesmo dia. A taxa de administração dos ETFs já está nos preços.\nDados: Yahoo Finance.\nResultados passados não garantem resultados futuros. Este vídeo é educativo e não é recomendação de investimento."
 },
 "es-419": {
  "title": "Ingreso de covered call gastado cada mes: ¿queda más capital en 13 años que vendiendo QQQ?",
  "description": "Los ETF de covered call pagan cada mes y dicen que conservan el capital. Si gastas los pagos cada mes, ¿de verdad se conserva el capital?\nPusimos los mismos US$100,000 en un ETF de covered call del Nasdaq-100 (QYLD) y en QQQ, que sigue el mismo Nasdaq-100. Cada vez que QYLD pagó, gastamos todo; de QQQ vendimos el mismo monto el mismo día. Las dos cuentas retiraron exactamente el mismo dinero. Diciembre de 2013 a octubre de 2026, comisión de 0.25% por operación, antes de impuestos.\nComprobaciones: 94 cuentas de 5 años y 118 de 3 años iniciadas en meses distintos, XYLD vs SPY, JEPI vs SPY, impuesto de 15% y reinvertir los pagos. El código lo escribió una IA. La narración es una voz de IA.\nDetalles para reproducir: cierres de Yahoo ajustados por splits y distribuciones (contadas en la fecha ex). Ambas cuentas compran al cierre de la fecha inicial con US$100,000 menos la comisión de 0.25% (acciones fraccionadas) — QYLD 2013-12-12, XYLD 2013-06-24, JEPI 2020-05-21. Cada distribución se retira completa en la fecha ex; el ETF de índice vende, al cierre de ese día, lo necesario para entregar el mismo dinero después de la comisión. Los dividendos de QQQ/SPY se reinvierten el mismo día. La comisión de administración de los ETF ya está en los precios.\nDatos: Yahoo Finance.\nLos resultados pasados no garantizan resultados futuros. Este video es educativo y no es asesoría de inversión."
 },
 "ja": {
  "title": "カバードコールの分配金を毎月使うと、同じ額を売るQQQより13年後に元本は多く残る？",
  "description": "毎月分配金が出て、元本はあまり減らないと言われるカバードコールETF。分配金を毎月使っても、元本は本当に守られるのでしょうか？\n同じ10万ドルを、ナスダック100のカバードコールETF（QYLD）と、同じナスダック100に連動するQQQに入れました。QYLDの分配金は出るたびに全部使い、QQQは同じ日に同じ金額だけ売って使います。2つの口座が引き出したお金は日付も金額も同じです。2013年12月〜2026年10月、売買ごとに手数料0.25%、税引き前。\n確認：開始月を変えた5年口座94個・3年口座118個、XYLD対SPY、JEPI対SPY、源泉徴収15%、分配金を再投資した場合。コードはAIが書きました。ナレーションはAI音声です。\n再現条件：Yahooの分割調整済み終値と分配金（権利落ち日で計算）。2つの口座とも開始日の終値で、10万ドルから手数料0.25%を引いた分を購入（端数株）— QYLD 2013-12-12、XYLD 2013-06-24、JEPI 2020-05-21。分配金は権利落ち日に全額引き出し、指数ETFはその日の終値で、手数料を払っても同じ金額が残るだけ売却。QQQ・SPYの配当は同じ日に再投資。ETFの経費率は価格に含まれています。\nデータ：Yahoo Finance。\n過去の結果は将来を保証しません。この動画は教育目的であり、投資助言ではありません。"
 },
 "de": {
  "title": "Covered-Call-Ausschüttung monatlich ausgeben: Bleibt nach 13 Jahren mehr als beim QQQ-Verkauf?",
  "description": "Covered-Call-ETFs zahlen jeden Monat aus und sollen das Kapital erhalten. Bleibt das Kapital wirklich erhalten, wenn man die Ausschüttungen jeden Monat ausgibt?\nWir haben dieselben 100.000 $ in einen Nasdaq-100-Covered-Call-ETF (QYLD) und in QQQ angelegt, der denselben Nasdaq-100 abbildet. Jede QYLD-Ausschüttung wurde komplett ausgegeben; bei QQQ wurde am selben Tag derselbe Betrag verkauft. Beide Konten entnahmen genau dasselbe Geld. Dezember 2013 bis Oktober 2026, 0,25 % Gebühr pro Trade, vor Steuern.\nPrüfungen: 94 Fünfjahres- und 118 Dreijahreskonten mit verschiedenen Startmonaten, XYLD vs. SPY, JEPI vs. SPY, 15 % Quellensteuer und Wiederanlage der Ausschüttungen. Den Code hat eine KI geschrieben. Die Sprecherstimme ist eine KI-Stimme.\nDetails zum Nachrechnen: split-bereinigte Yahoo-Schlusskurse und Ausschüttungen (am Ex-Tag gezählt). Beide Konten kaufen zum Schlusskurs des Starttags für 100.000 $ abzüglich 0,25 % Gebühr (Bruchteile) — QYLD 2013-12-12, XYLD 2013-06-24, JEPI 2020-05-21. Jede Ausschüttung wird am Ex-Tag vollständig entnommen; der Index-ETF verkauft zum Schlusskurs des Tages so viel, dass nach Gebühr derselbe Betrag bleibt. Dividenden von QQQ/SPY werden am selben Tag wieder angelegt. Die Kostenquoten der ETFs stecken bereits in den Kursen.\nDaten: Yahoo Finance.\nVergangene Ergebnisse garantieren keine zukünftigen Renditen. Dieses Video dient nur der Bildung und ist keine Anlageberatung."
 },
 "vi": {
  "title": "Tiêu cổ tức covered call mỗi tháng: sau 13 năm vốn còn nhiều hơn bán QQQ cùng số tiền không?",
  "description": "ETF covered call trả tiền mỗi tháng và được cho là giữ được vốn gốc. Nếu tiêu khoản chi trả mỗi tháng, vốn gốc có thật sự được giữ?\nChúng tôi đặt cùng 100.000 USD vào ETF covered call Nasdaq-100 (QYLD) và vào QQQ, quỹ theo cùng chỉ số Nasdaq-100. Mỗi lần QYLD chi trả, chúng tôi tiêu hết; với QQQ, bán cùng số tiền vào cùng ngày. Hai tài khoản rút ra số tiền giống hệt nhau. Từ tháng 12/2013 đến tháng 10/2026, phí 0,25% mỗi giao dịch, trước thuế.\nKiểm tra: 94 tài khoản 5 năm và 118 tài khoản 3 năm bắt đầu ở các tháng khác nhau, XYLD so với SPY, JEPI so với SPY, thuế 15% và tái đầu tư khoản chi trả. Mã do AI viết. Giọng đọc là giọng AI.\nChi tiết để tính lại: giá đóng cửa Yahoo đã điều chỉnh tách cổ phiếu và các khoản phân phối (tính theo ngày giao dịch không hưởng quyền). Cả hai tài khoản mua ở giá đóng cửa ngày bắt đầu với 100.000 USD trừ phí 0,25% (cổ phiếu lẻ) — QYLD 2013-12-12, XYLD 2013-06-24, JEPI 2020-05-21. Mỗi khoản phân phối được rút hết vào ngày không hưởng quyền; ETF chỉ số bán ở giá đóng cửa ngày đó đủ để sau phí còn đúng số tiền như vậy. Cổ tức QQQ/SPY được tái đầu tư cùng ngày. Phí quản lý ETF đã nằm trong giá.\nDữ liệu: Yahoo Finance.\nKết quả quá khứ không đảm bảo tương lai. Video chỉ nhằm mục đích giáo dục, không phải lời khuyên đầu tư."
 },
 "tr": {
  "title": "Covered call dağıtımını her ay harcarsanız 13 yıl sonra QQQ satmaktan fazla anapara kalır mı?",
  "description": "Covered call ETF'leri her ay ödeme yapar ve anaparayı koruduğu söylenir. Ödemeleri her ay harcarsanız anapara gerçekten korunur mu?\nAynı 100.000 doları Nasdaq-100 covered call ETF'si QYLD'ye ve aynı Nasdaq-100'ü izleyen QQQ'ya yatırdık. QYLD her ödeme yaptığında hepsini harcadık; QQQ'dan aynı gün aynı tutarı sattık. İki hesap da tam olarak aynı parayı çekti. Aralık 2013 - Ekim 2026, işlem başına %0,25 komisyon, vergi öncesi.\nKontroller: farklı aylarda başlayan 94 beş yıllık ve 118 üç yıllık hesap, XYLD - SPY, JEPI - SPY, %15 stopaj ve ödemelerin yeniden yatırılması. Kodu yapay zekâ yazdı. Seslendirme yapay zekâ sesidir.\nYeniden hesaplama ayrıntıları: bölünmeye göre düzeltilmiş Yahoo kapanışları ve dağıtımlar (hak kullanım tarihinde sayıldı). İki hesap da başlangıç günü kapanışından 100.000 dolardan %0,25 komisyon düşülerek alır (kesirli pay) — QYLD 2013-12-12, XYLD 2013-06-24, JEPI 2020-05-21. Her dağıtım hak kullanım tarihinde tamamen çekilir; endeks ETF'si o günün kapanışından, komisyondan sonra aynı nakit kalacak kadar satar. QQQ/SPY temettüleri aynı gün yeniden yatırılır. ETF gider oranları fiyatlara zaten dahildir.\nVeri: Yahoo Finance.\nGeçmiş sonuçlar gelecekteki getirileri garanti etmez. Bu video yalnızca eğitim amaçlıdır, yatırım tavsiyesi değildir."
 }
}
```

## 6. 고정 댓글

```
분배금을 매달 꺼내 쓰는 커버드콜 계좌와, 같은 돈을 꺼낸 지수 계좌 — 13년 뒤 어느 쪽 원금이 더 남을 거라고 생각하셨나요? 지금 쓰고 계신 커버드콜 ETF가 있다면 알려 주세요.
다음에 백테스트로 검증해 볼 가설도 댓글로 남겨 주세요.
(정보 제공용이며 투자 권유가 아닙니다)
```

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올리고 **1시간 뒤 예약 공개** (`--publish-at +1h`) |
| 썸네일 | `thumbnails/thumbnail_1.*` (본안 — 글자 없음). 공개 뒤 '테스트 및 비교'에 thumbnail_1~3 |
| 기본 언어 | ko |
| 자막 올리기 | **언어별** (한국어 + en·hi·id·pt·es-419·ja·de·vi·tr — 화면에는 굽지 않고 CC 로, `subs/` 대본 → 오디오 뒤 `python3 tools/subs_tool.py build stock keobeodeu-kol-2026-10` · 업로드 도구 v1.12 가 자막 하나 400단위 — 할당량이 모자라면 `--captions-only` 로 다음 날, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 (내레이션) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — 사용자 지시 2026-10-11) |

## 8. 점검

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과(남은 원금·어느 쪽이 많았는지·배수)를 쓰지 않았다. 결과는 영상 '13년 결과'(s58~)와 각 확인 장 끝에서만.
- 설명란·언어별 설명의 숫자(10만 달러·2013-12·2026-10·0.25%·94·118·5년·3년·15%)는 대본·`backtest/results.json`·`run.py` 설정에 있는 것만 썼다.
- 언어별 제목 100자 이하 · `< >` 없음 — `python tools/youtube_upload.py stock keobeodeu-kol-2026-10 --dry-run` 으로 확인.
- 사다 → 매수, 팔다 → 매도 (설명란의 '매도해서').

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, 시청 지속 그래프에서 크게 떨어지는 장, **나라·언어별 조회수**
