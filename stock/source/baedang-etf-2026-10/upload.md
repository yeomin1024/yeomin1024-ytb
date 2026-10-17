# baedang-etf-2026-10 업로드 시트

버전: v1.1 — 2026-10-17 — 대본 v1.1 (도입 + 규칙 약 24초 — 사용자 지시 2026-10-17 "야 너 내가 테스트 들어가지 전 도입 및 규칙 설명 30초 넘기지 말라고 했잖아 근데 왜 안지켜 다시 수정해"): 챕터 다시 계산 — 규칙 챕터는 첫 챕터에 합침(10초 미만이 될 수 있어서), 설명 챕터는 결과 뒤. (v1.0 — 2026-10-16 — 최초 (주식 3번 배당 ETF vs 지수 세후 — `backtest/run.py` v1.0). 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐". `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음.)
기준 파일: 대본 (111문장) · SRT 문장 111 (추정 시각 — 오디오가 생기면 다시) · 결과 `backtest/results.json` · 올릴 영상 = 렌더 원본 `stock/out/baedang-etf-2026-10/final_1080p.mp4` (오디오가 생긴 뒤 — 지금 있는 `preview_estimated_silent.mp4` 는 소리 없는 미리보기라 올리지 않음)

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json`)로 `python tools/youtube_upload.py stock baedang-etf-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (`titles.md` R1, 한국어 — 기본 언어)

```
배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까?
```

## 2. 설명란 (한국어 — 그대로 복사)

```
배당금이 통장에 들어오면 든든하죠. 그래서 배당 ETF를 매달 모으는 분이 많습니다. 그런데 배당에는 받을 때마다 세금이 붙어요. 세금을 떼고 나면, 배당 ETF가 정말 더 많이 남을까요?
2011년 11월부터 2026년 10월까지 매달 첫 거래일에 미국 배당 ETF SCHD와 S&P 500 ETF SPY를 1,000달러씩 매수했습니다. 배당은 받을 때마다 15%를 세금으로 떼고(많은 나라의 미국 배당 원천징수 세율), 남은 돈으로 그날 다시 매수했어요. 매수 수수료 0.25%.
날짜가 흐르며 두 계좌의 값, 넣은 돈, 받은 배당과 낸 세금이 실시간으로 바뀌고, 아래 띠가 어느 계좌가 앞서는지 보여 줍니다.

■ 챕터
0:00 배당 ETF, 세금 떼고도 더 남을까
0:27 2011년부터 날짜를 흘려 보면
2:58 2022년 하락장과 그 뒤
4:21 15년 결과
5:32 배당은 어디서 나오나
6:43 해마다 1년 수익률
7:33 세금·매도·한 번에 넣으면
8:37 시작한 달을 바꾸면
9:16 2006년부터 VYM으로
10:20 정리
11:03 이 실험의 한계

■ 실험 방법
자료: SCHD·SPY·VYM 일별 종가·배당 (분할 반영), 2011-11-01 ~ 2026-10-15 (VYM 은 2006-12-01 부터).
배당은 배당락일 종가에 받은 것으로 세고, 15%를 뗀 뒤 그날 종가에 다시 매수. 매수할 때마다 수수료 0.25%.
확인: 세금 0%·30%, 끝에 모두 매도하고 늘어난 돈에 15%, 처음에 10만 달러 한 번, 시작 달을 바꾼 5년 적립 120개·10년 적립 60개, VYM vs SPY(2008 금융위기 포함).
계산 코드는 AI가 짰고, 미래 가격을 쓰지 않는지 시험한 뒤 돌렸습니다. 환율·물가·건강보험료는 넣지 않았습니다. 이 영상의 내레이션은 AI 음성입니다.

■ 자료
일별 종가·배당: Yahoo Finance 차트 API

■ 알려 드립니다
과거 자료로 계산한 결과이며 앞으로도 같다는 보장은 없습니다. 세율은 나라·계좌마다 다릅니다. 특정 상품을 매수·매도하라는 이야기가 아니며 투자 권유가 아닙니다.

#배당ETF #백테스트 #SCHD
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/baedang-etf-2026-10/baedang-etf-2026-10.txt stock/source/baedang-etf-2026-10/baedang-etf-2026-10.srt --chapters "1=배당 ETF, 세금 떼고도 더 남을까;6=2011년부터 날짜를 흘려 보면;27=2022년 하락장과 그 뒤;38=15년 결과;49=배당은 어디서 나오나;63=해마다 1년 수익률;70=세금·매도·한 번에 넣으면;80=시작한 달을 바꾸면;87=2006년부터 VYM으로;97=정리;105=이 실험의 한계"
```
- 2026-10-17 추정 시각(오디오 전, 대본 v1.1)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 오디오에 맞춘 SRT로 다시 계산한다. 챕터 이름에 결과를 쓰지 않는다.

## 4. 태그

```
배당 ETF, 배당주, SCHD, SPY, VYM, S&P500, 배당세, 원천징수, 배당 재투자, 적립식, 월배당, 백테스트, dividend ETF, backtest, dividend tax
```

## 5. 언어별 제목·설명 (localizations)

JSON — 업로드 도구가 그대로 읽는다. 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜).

```
{
 "en": {
  "title": "Dividend ETF saved monthly: after 15% dividend tax, is more left than the same money in the S&P 500?",
  "description": "Dividends landing in your account feel reassuring, so many people buy a dividend ETF every month. But dividends are taxed every time you receive them. After tax, does the dividend ETF really leave you with more?\nWe bought $1,000 of SCHD (a US dividend ETF) and $1,000 of SPY (S&P 500) on the first trading day of every month from November 2011 to October 2026. Every dividend was taxed 15% (a common treaty withholding rate on US dividends) and the rest was reinvested the same day. 0.25% fee per purchase. As the dates roll forward, both account values, the money put in, the dividends received and the tax paid change in real time, and a strip shows which account is ahead.\nChecks: 0% and 30% tax, selling everything at the end with 15% tax on gains, one lump sum of $100,000, 120 five-year and 60 ten-year accounts started in different months, and VYM vs SPY from 2006 (including 2008). The code was written by AI and tested for look-ahead bias. Currency, inflation and health-insurance costs are not included. The narration is an AI voice.\nData: Yahoo Finance (daily closes and dividends).\nPast results do not guarantee future returns. This video is for education only and is not investment advice."
 },
 "hi": {
  "title": "डिविडेंड ETF हर महीने जमा करें: 15% टैक्स के बाद क्या S&P 500 में उतने ही पैसे से ज़्यादा बचेगा?",
  "description": "खाते में डिविडेंड आना अच्छा लगता है, इसलिए बहुत लोग हर महीने डिविडेंड ETF खरीदते हैं। लेकिन हर बार डिविडेंड पर टैक्स लगता है। टैक्स के बाद क्या डिविडेंड ETF सच में ज़्यादा बचाता है?\nनवंबर 2011 से अक्टूबर 2026 तक हर महीने के पहले कारोबारी दिन $1,000 का SCHD और $1,000 का SPY खरीदा। हर डिविडेंड पर 15% टैक्स काटा और बाकी उसी दिन दोबारा निवेश किया। हर खरीद पर 0.25% शुल्क।\nजाँच: 0% और 30% टैक्स, अंत में सब बेचकर लाभ पर 15% टैक्स, एक साथ $100,000, अलग महीनों से शुरू हुए खाते, और 2006 से VYM बनाम SPY। कोड AI ने लिखा। वॉइस-ओवर AI आवाज़ है।\nडेटा: Yahoo Finance।\nपिछले नतीजे भविष्य की गारंटी नहीं हैं। यह वीडियो केवल शिक्षा के लिए है, निवेश सलाह नहीं।"
 },
 "id": {
  "title": "ETF dividen tiap bulan: setelah pajak dividen 15%, sisa lebih banyak dari S&P 500 dengan uang sama?",
  "description": "Dividen yang masuk ke rekening terasa menenangkan, jadi banyak orang membeli ETF dividen setiap bulan. Tapi dividen dipajaki setiap kali diterima. Setelah pajak, apakah ETF dividen benar-benar menyisakan lebih banyak?\nKami membeli SCHD senilai $1.000 dan SPY senilai $1.000 pada hari bursa pertama setiap bulan dari November 2011 sampai Oktober 2026. Setiap dividen dipotong pajak 15% dan sisanya diinvestasikan kembali di hari yang sama. Biaya 0,25% per pembelian.\nPengecekan: pajak 0% dan 30%, menjual semuanya di akhir dengan pajak 15% atas keuntungan, sekali $100.000, akun yang dimulai di bulan berbeda, dan VYM vs SPY sejak 2006. Kode ditulis oleh AI. Narasi memakai suara AI.\nData: Yahoo Finance.\nHasil masa lalu tidak menjamin hasil masa depan. Video ini hanya untuk edukasi, bukan saran investasi."
 },
 "pt": {
  "title": "ETF de dividendos todo mês: com 15% de imposto, sobra mais que o mesmo dinheiro no S&P 500?",
  "description": "Ver dividendos caindo na conta traz segurança, então muita gente compra um ETF de dividendos todo mês. Mas os dividendos são tributados a cada recebimento. Depois do imposto, o ETF de dividendos realmente deixa mais?\nCompramos US$ 1.000 de SCHD e US$ 1.000 de SPY no primeiro dia útil de cada mês, de novembro de 2011 a outubro de 2026. Cada dividendo teve 15% de imposto e o resto foi reinvestido no mesmo dia. Taxa de 0,25% por compra.\nVerificações: imposto de 0% e 30%, vender tudo no fim com 15% sobre o ganho, um aporte único de US$ 100.000, contas iniciadas em meses diferentes e VYM vs SPY desde 2006. O código foi escrito por IA. A narração é uma voz de IA.\nDados: Yahoo Finance.\nResultados passados não garantem resultados futuros. Este vídeo é educativo e não é recomendação de investimento."
 },
 "es-419": {
  "title": "ETF de dividendos cada mes: con 15% de impuesto, ¿queda más que el mismo dinero en el S&P 500?",
  "description": "Ver dividendos en la cuenta da tranquilidad, por eso mucha gente compra un ETF de dividendos cada mes. Pero los dividendos pagan impuesto cada vez que se reciben. Después de impuestos, ¿el ETF de dividendos de verdad deja más?\nCompramos US$1,000 de SCHD y US$1,000 de SPY el primer día hábil de cada mes, de noviembre de 2011 a octubre de 2026. A cada dividendo se le quitó 15% de impuesto y el resto se reinvirtió el mismo día. Comisión de 0.25% por compra.\nComprobaciones: impuesto de 0% y 30%, vender todo al final con 15% sobre la ganancia, una sola inversión de US$100,000, cuentas iniciadas en meses distintos y VYM vs SPY desde 2006. El código lo escribió una IA. La narración es una voz de IA.\nDatos: Yahoo Finance.\nLos resultados pasados no garantizan resultados futuros. Este video es educativo y no es asesoría de inversión."
 },
 "ja": {
  "title": "高配当ETFを毎月積み立てると、配当税15%を引いても同じ額のS&P 500より多く残る？",
  "description": "配当が口座に入ると安心するので、高配当ETFを毎月買う人は多いです。でも配当は受け取るたびに課税されます。税引き後でも、高配当ETFは本当に多く残るのでしょうか？\n2011年11月〜2026年10月、毎月最初の取引日にSCHD（米国高配当ETF）とSPY（S&P 500）を1,000ドルずつ買いました。配当は受け取るたびに15%を源泉徴収し、残りをその日に再投資。購入ごとに手数料0.25%。\n確認：税率0%・30%、最後に全部売って利益に15%課税、10万ドルの一括投資、開始月を変えた口座、2006年からのVYM対SPY。コードはAIが書きました。ナレーションはAI音声です。\nデータ：Yahoo Finance。\n過去の結果は将来を保証しません。この動画は教育目的であり、投資助言ではありません。"
 },
 "de": {
  "title": "Dividenden-ETF monatlich sparen: Bleibt nach 15 % Steuer mehr als mit gleichem Geld im S&P 500?",
  "description": "Dividenden auf dem Konto beruhigen, deshalb kaufen viele jeden Monat einen Dividenden-ETF. Doch Dividenden werden bei jeder Auszahlung besteuert. Bleibt nach Steuern mit dem Dividenden-ETF wirklich mehr übrig?\nWir haben von November 2011 bis Oktober 2026 am ersten Handelstag jedes Monats je 1.000 $ SCHD und SPY gekauft. Jede Dividende wurde mit 15 % besteuert, der Rest am selben Tag wieder angelegt. 0,25 % Gebühr pro Kauf.\nPrüfungen: 0 % und 30 % Steuer, alles am Ende verkaufen mit 15 % auf den Gewinn, einmalig 100.000 $, Konten mit verschiedenen Startmonaten und VYM vs. SPY ab 2006. Den Code hat eine KI geschrieben. Die Sprecherstimme ist eine KI-Stimme.\nDaten: Yahoo Finance.\nVergangene Ergebnisse garantieren keine zukünftigen Renditen. Dieses Video dient nur der Bildung und ist keine Anlageberatung."
 },
 "vi": {
  "title": "Tích lũy ETF cổ tức mỗi tháng: sau thuế cổ tức 15%, có còn nhiều hơn S&P 500 với cùng số tiền?",
  "description": "Cổ tức về tài khoản khiến ta yên tâm, nên nhiều người mua ETF cổ tức mỗi tháng. Nhưng cổ tức bị đánh thuế mỗi lần nhận. Sau thuế, ETF cổ tức có thật sự để lại nhiều hơn?\nChúng tôi mua 1.000 USD SCHD và 1.000 USD SPY vào ngày giao dịch đầu tiên mỗi tháng từ tháng 11/2011 đến tháng 10/2026. Mỗi lần nhận cổ tức trừ thuế 15%, phần còn lại tái đầu tư ngay trong ngày. Phí 0,25% mỗi lần mua.\nKiểm tra: thuế 0% và 30%, bán hết cuối kỳ và đóng 15% trên phần lãi, đầu tư một lần 100.000 USD, tài khoản bắt đầu ở các tháng khác nhau, và VYM so với SPY từ 2006. Mã do AI viết. Giọng đọc là giọng AI.\nDữ liệu: Yahoo Finance.\nKết quả quá khứ không đảm bảo tương lai. Video chỉ nhằm mục đích giáo dục, không phải lời khuyên đầu tư."
 },
 "tr": {
  "title": "Temettü ETF'si her ay biriktirilirse %15 vergiden sonra aynı parayla S&P 500'den fazla kalır mı?",
  "description": "Hesaba gelen temettü insanı rahatlatır; bu yüzden birçok kişi her ay temettü ETF'si alır. Ama temettü her alındığında vergilendirilir. Vergiden sonra temettü ETF'si gerçekten daha fazla bırakır mı?\nKasım 2011'den Ekim 2026'ya kadar her ayın ilk işlem gününde 1.000 dolarlık SCHD ve 1.000 dolarlık SPY aldık. Her temettüden %15 vergi kesildi, kalanı aynı gün yeniden yatırıldı. Alım başına %0,25 komisyon.\nKontroller: %0 ve %30 vergi, sonda hepsini satıp kazançtan %15 vergi, tek seferde 100.000 dolar, farklı aylarda başlayan hesaplar ve 2006'dan itibaren VYM - SPY. Kodu yapay zekâ yazdı. Seslendirme yapay zekâ sesidir.\nVeri: Yahoo Finance.\nGeçmiş sonuçlar gelecekteki getirileri garanti etmez. Bu video yalnızca eğitim amaçlıdır, yatırım tavsiyesi değildir."
 }
}
```

## 6. 고정 댓글

```
배당 ETF와 지수 ETF에 15년 동안 같은 돈을 모았다면, 세금을 떼고 어느 쪽이 더 남을 거라고 생각하셨나요? 지금 모으고 계신 배당 ETF가 있다면 알려 주세요.
다음에 백테스트로 검증해 볼 가설도 댓글로 남겨 주세요.
(정보 제공용이며 투자 권유가 아닙니다)
```

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올리고 **1시간 뒤 예약 공개** (`--publish-at +1h`) |
| 썸네일 | `thumbnails/thumbnail_1.*` (본안 — 글자 없음). 공개 뒤 '테스트 및 비교'에 thumbnail_1~3 |
| 기본 언어 | ko |
| 자막 올리기 | **아니요** (전 세계 대상) |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 (내레이션) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성) |

## 8. 점검

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과(어느 계좌가 많았는지·배수·금액)를 쓰지 않았다.
- 설명란 숫자(2011-11·2026-10·1,000달러·15%·0.25%·0%·30%·10만 달러·120·60·5년·10년·2006·2008)는 대본·`backtest/results.json`·`run.py` 설정에 있는 것만.
- 언어별 제목 100자 이하 · `< >` 없음 — `python tools/youtube_upload.py stock baedang-etf-2026-10 --dry-run` 으로 확인.
- 사다 → 매수, 팔다 → 매도.

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, 시청 지속 그래프에서 크게 떨어지는 장, **나라·언어별 조회수**
