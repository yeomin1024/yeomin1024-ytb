# eonje-maesu-2026-10 업로드 시트

버전: v3.0 — 2026-10-16 — 다시 만듦: 잣대 = 성공률(매수한 값보다 +5% 종가가 −2% 종가보다 먼저) · 비교 상대 = 신호 없이 무작위 날짜에 매수한 계좌 2천 개 · 자주 나오는 매수 신호 10가지 (`backtest/barrier/run.py` v2.0). 사용자 지시 2026-10-16 "그럼 신호 없이 무작위로 매수 했을 때랑 비교하는 거지? 그게 맞는거 같은데 그리고 m을 1~2%로 해야 엄격하게 봐서 성공 확률이 줄지 m은 내가 말한 범위에서 적절하게 정해서 영상 만들어봐". `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음.
(v2.1 — 끝 값 비교·매도 = 산 뒤 최고 −10% — 커밋 28e1b7b. v1.0 — `stock/source/_old/eonje-maesu-2026-10-v1/upload.md`)
기준 파일: 대본 v3.0 (167문장) · SRT 문장 167 (추정 시각 — 오디오가 생기면 다시) · 결과 `backtest/barrier/results.json` · 올릴 영상 = 렌더 원본 `stock/out/eonje-maesu-2026-10/final_1080p.mp4` (오디오가 생긴 뒤 — 지금 있는 `preview_estimated_silent.mp4` 는 소리 없는 미리보기라 올리지 않음)

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json` — 업로드 도구 v1.7 이 채널이 다르면 올리지 않음)로 `python tools/youtube_upload.py stock eonje-maesu-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (`titles.md` R1, 한국어 — 기본 언어)

```
매수 타이밍, 저점·RSI·신고가 신호는 2% 떨어지기 전 5% 오를 확률이 무작위 매수보다 높을까?
```

## 2. 설명란 (한국어 — 그대로 복사)

```
매수하자마자 떨어지면, 타이밍을 잘못 잡았나 싶죠. 많이 쓰는 매수 신호는 정말 성공 확률을 높일까요?
매수 신호 10가지를 같은 규칙으로 시험했습니다. 매수한 값보다 종가가 5% 오르면 성공, 그 전에 2% 떨어지면 실패. 판정이 나면 다음 날 매도하고, 신호가 다시 나오면 또 매수합니다.
비교 상대는 신호 없이 무작위 날짜에 매수한 계좌 2천 개(같은 횟수·같은 매도 규칙)입니다. SPY, 2016년 1월 ~ 2026년 10월, 수수료 0.25%.
날짜가 흐르며 각 신호의 성공(초록)·실패(빨강)와 성공률이 무작위 계좌와 함께 3D 차트에서 실시간으로 바뀝니다.

■ 챕터
0:00 언제 매수할까
0:35 1 매달 첫 거래일
1:53 2 20일 신고가 돌파
2:59 3 1개월 모멘텀
4:05 4 20일 이동평균선 돌파
5:17 5 골든 크로스 5·20일
6:30 6 하루 −1% 하락 다음 날
7:45 7 RSI 40 아래
8:50 8 공포지수 VIX 20 이상
9:58 9 20일 고점 −5%
11:03 10 최고 종가 −5%
12:18 10가지 결과
12:54 실패 기준·기간을 바꾸면
13:29 정리
13:59 이 실험의 한계

■ 시험한 매수 신호 10가지
1 매달 첫 거래일 / 2 20일 신고가 돌파 / 3 1개월 모멘텀(21 거래일 전 종가보다 높으면) / 4 20일 이동평균선 위로 돌파 / 5 골든 크로스 5·20일 / 6 하루 −1% 하락 다음 날 / 7 RSI(14) 40 아래 / 8 공포지수 VIX 20 이상 / 9 최근 20 거래일 고점보다 5% 아래 / 10 그때까지 최고 종가보다 5% 아래
신호가 너무 드물지 않도록 문턱을 넓혔고(예: RSI 30 → 40), 문턱은 성공률을 보기 전에 신호가 나온 날 수만 보고 정했습니다.

■ 실험 방법
자료: SPY(S&P 500 ETF) 일별 종가, 2016-01-04 ~ 2026-10-15. 신호는 그날 종가까지만 보고, 매수는 다음 거래일 종가.
성공·실패는 종가로 판정하고, 판정 다음 거래일 종가에 매도. 들고 있는 동안은 새로 매수하지 않습니다. 사고팔 때마다 수수료 0.25%.
실패 기준 2%는 1~2% 안에서, 결과를 보기 전에 자료 성질(하루 보통 움직임 약 1.1%)만 보고 정했습니다. 확인용으로 1%·1.5%와 1994~2015년도 계산했습니다.
무작위 계좌 2천 개는 각 신호와 같은 매도 규칙·같은 쉬는 기간으로, 매수 날짜만 무작위입니다(시드 고정).
계산 코드는 AI가 짰고, 미래 가격을 쓰지 않는지 시험한 뒤 돌렸습니다. 세금·환전 비용은 넣지 않았습니다. 이 영상의 내레이션은 AI 음성입니다.

■ 자료
SPY·VIX 일별: Yahoo Finance 차트 API

■ 알려 드립니다
과거 자료로 계산한 결과이며 앞으로도 같다는 보장은 없습니다. 특정 상품을 매수하라는 이야기가 아니며 투자 권유가 아닙니다.

#매수타이밍 #백테스트 #SPY
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/eonje-maesu-2026-10/eonje-maesu-2026-10.txt stock/source/eonje-maesu-2026-10/eonje-maesu-2026-10.srt --chapters "1=언제 매수할까;8=1 매달 첫 거래일;23=2 20일 신고가 돌파;35=3 1개월 모멘텀;48=4 20일 이동평균선 돌파;61=5 골든 크로스 5·20일;75=6 하루 −1% 하락 다음 날;89=7 RSI 40 아래;101=8 공포지수 VIX 20 이상;114=9 20일 고점 −5%;127=10 최고 종가 −5%;141=10가지 결과;148=실패 기준·기간을 바꾸면;155=정리;161=이 실험의 한계"
```
- 2026-10-16 추정 시각(오디오 전, `srt_tool.py` 추정)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 올릴 때 오디오에 맞춘 SRT로 다시 계산해 2번 설명란에 넣는다.
- 챕터 이름에 결과를 쓰지 않는다 (진행 막대에 미리 보이므로). 번호는 영상에 나오는 순서 (장 카드의 노란 번호와 같음).

## 4. 태그

```
매수 타이밍, 매수 신호, 저점 매수, RSI, 신고가 돌파, 모멘텀, 이동평균선, 골든크로스, 공포지수, VIX, 매달 매수, 무작위 매수, 성공 확률, 백테스트, SPY, S&P500, buy signal, backtest, random entry
```

## 5. 언어별 제목·설명 (localizations)

`stock/guides/README.md` 2번의 9개 언어 (기본 언어 ko 는 1·2번). JSON — 업로드 도구가 그대로 읽는다 (고칠 때 따옴표·쉼표 주의). 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜). 만든 스크립트가 제목 100자 이하·`< >` 없음을 확인했다.

```
{
 "en": {
  "title": "When to buy: do dip, RSI and breakout signals hit +5% before −2% more often than random buys?",
  "description": "Buy, and the price drops right away... was it bad timing? Do popular buy signals really raise your odds?\nWe tested 10 common buy signals with the same rule: a trade succeeds if the close reaches +5% above the buy price before it falls 2% below it. Once a trade is decided we sell the next day, and buy again on the next signal. The comparison is 2,000 accounts that buy on random dates without any signal (same number of trades, same sell rule). SPY, January 2016 to October 2026, 0.25% fee per trade.\nAs the dates roll forward, a 3D chart shows each signal's successes (green), failures (red) and success rate next to the random accounts in real time.\n\nSignals: first trading day of the month, 20-day high breakout, 1-month momentum, close crossing above the 20-day average, 5/20-day golden cross, the day after a 1% drop, RSI(14) below 40, VIX at 20 or above, 5% below the 20-day high, 5% below the all-time high. Thresholds were widened so signals are not rare, and set only from how often signals occur, before looking at success rates. The 2% failure line was chosen within 1–2% from data properties (a typical daily move is about 1.1%), also before looking at results; we also checked 1% and 1.5% and the years 1994–2015.\nSignals use closes up to that day; buys happen at the next day's close; success and failure are judged on closes. The code was written by AI and tested for look-ahead bias. Taxes and currency costs are not included. The narration is an AI voice.\nData: Yahoo Finance (SPY, ^VIX daily).\nPast results do not guarantee future returns. This video is for education only and is not investment advice."
 },
 "hi": {
  "title": "कब खरीदें: क्या डिप, RSI और ब्रेकआउट संकेत रैंडम खरीद से ज़्यादा बार −2% से पहले +5% छूते हैं?",
  "description": "खरीदते ही दाम गिर जाए तो लगता है टाइमिंग गलत थी। क्या लोकप्रिय खरीद संकेत सच में सफलता की संभावना बढ़ाते हैं?\nहमने 10 आम खरीद संकेतों को एक ही नियम से परखा: खरीद भाव से 2% नीचे गिरने से पहले बंद भाव 5% ऊपर पहुँचे तो सफल, नहीं तो असफल। फैसला होते ही अगले दिन बेचते हैं और अगले संकेत पर फिर खरीदते हैं। तुलना: बिना संकेत के रैंडम तारीखों पर खरीदने वाले 2,000 खाते (उतने ही सौदे, वही बिक्री नियम)। SPY, जनवरी 2016 से अक्टूबर 2026, हर सौदे पर 0.25% शुल्क। 3D चार्ट पर तारीख आगे बढ़ते हुए हर संकेत की सफलता (हरा), असफलता (लाल) और सफलता दर रैंडम खातों के साथ दिखती है।\nसंकेत दुर्लभ न हों इसलिए सीमाएँ ढीली की गईं, और नतीजे देखने से पहले केवल संकेतों की संख्या देखकर तय की गईं। कोड AI ने लिखा और भविष्य के डेटा के इस्तेमाल से बचाव की जाँच की। टैक्स और मुद्रा खर्च शामिल नहीं। वॉइस-ओवर AI आवाज़ है।\nडेटा: Yahoo Finance (SPY, ^VIX)।\nपिछले नतीजे भविष्य की गारंटी नहीं हैं। यह वीडियो केवल शिक्षा के लिए है, निवेश सलाह नहीं।"
 },
 "id": {
  "title": "Kapan beli: sinyal dip, RSI, breakout lebih sering naik 5% sebelum turun 2% dibanding beli acak?",
  "description": "Baru beli, harga langsung turun... salah timing? Apakah sinyal beli populer benar-benar menaikkan peluang berhasil?\nKami menguji 10 sinyal beli umum dengan aturan yang sama: berhasil jika harga penutupan naik 5% di atas harga beli sebelum turun 2% di bawahnya. Setelah ada hasil, kami jual esok hari dan beli lagi pada sinyal berikutnya. Pembandingnya 2.000 akun yang membeli pada tanggal acak tanpa sinyal (jumlah transaksi dan aturan jual sama). SPY, Januari 2016 sampai Oktober 2026, biaya 0,25% per transaksi. Grafik 3D menunjukkan keberhasilan (hijau), kegagalan (merah) dan tingkat keberhasilan tiap sinyal di samping akun acak secara langsung.\nAmbang sinyal dilonggarkan agar sinyal tidak jarang, dan ditetapkan hanya dari seberapa sering sinyal muncul, sebelum melihat hasil. Kode ditulis oleh AI dan diuji terhadap look-ahead bias. Pajak dan biaya kurs tidak dihitung. Narasi memakai suara AI.\nData: Yahoo Finance (SPY, ^VIX).\nHasil masa lalu tidak menjamin hasil masa depan. Video ini hanya untuk edukasi, bukan saran investasi."
 },
 "pt": {
  "title": "Quando comprar: queda, RSI e rompimento sobem 5% antes de cair 2% mais que compras aleatórias?",
  "description": "Você compra e o preço cai logo em seguida... foi o momento errado? Os sinais de compra populares realmente aumentam a chance de acerto?\nTestamos 10 sinais de compra comuns com a mesma regra: a operação dá certo se o fechamento sobe 5% acima do preço de compra antes de cair 2% abaixo dele. Decidida a operação, vendemos no dia seguinte e compramos de novo no próximo sinal. A comparação são 2.000 contas que compram em datas aleatórias, sem sinal (mesmo número de operações e mesma regra de venda). SPY, de janeiro de 2016 a outubro de 2026, taxa de 0,25% por operação. Um gráfico 3D mostra, em tempo real, acertos (verde), erros (vermelho) e a taxa de acerto de cada sinal ao lado das contas aleatórias.\nOs limites dos sinais foram ampliados para que não fossem raros, definidos só pela frequência dos sinais, antes de ver os resultados. O código foi escrito por IA e testado contra viés de antecipação. Impostos e câmbio não foram incluídos. A narração é uma voz de IA.\nDados: Yahoo Finance (SPY, ^VIX).\nResultados passados não garantem resultados futuros. Este vídeo é educativo e não é recomendação de investimento."
 },
 "es-419": {
  "title": "¿Cuándo comprar? ¿Caída, RSI y ruptura suben 5% antes de caer 2% más seguido que comprar al azar?",
  "description": "Compras y el precio baja enseguida... ¿fue mal momento? ¿Las señales de compra populares de verdad aumentan la probabilidad de acertar?\nProbamos 10 señales de compra comunes con la misma regla: la operación sale bien si el cierre sube 5% sobre el precio de compra antes de caer 2% por debajo. Decidida la operación, vendemos al día siguiente y volvemos a comprar en la siguiente señal. La comparación son 2,000 cuentas que compran en fechas al azar, sin señal (mismo número de operaciones y misma regla de venta). SPY, de enero de 2016 a octubre de 2026, comisión de 0.25% por operación. Un gráfico 3D muestra en tiempo real los aciertos (verde), fallos (rojo) y la tasa de acierto de cada señal junto a las cuentas al azar.\nLos umbrales se ampliaron para que las señales no fueran raras, y se fijaron solo por su frecuencia, antes de ver los resultados. El código lo escribió una IA y se probó contra el sesgo de anticipación. No incluye impuestos ni costos de cambio. La narración es una voz de IA.\nDatos: Yahoo Finance (SPY, ^VIX).\nLos resultados pasados no garantizan resultados futuros. Este video es educativo y no es asesoría de inversión."
 },
 "ja": {
  "title": "買うタイミング：押し目・RSI・高値更新のシグナルは、ランダムに買うより−2%の前に+5%に届く確率が高い？",
  "description": "買った途端に下がると、タイミングが悪かったのかと思いますよね。よく使われる買いシグナルは、本当に成功の確率を上げるのでしょうか？\n買いシグナル10個を同じルールで試しました。買値から2%下がる前に終値が5%上がれば成功、先に2%下がれば失敗。判定が出たら翌日に売り、次のシグナルでまた買います。比べる相手は、シグナルなしでランダムな日に買う口座2,000個（同じ回数・同じ売りルール）。SPY、2016年1月〜2026年10月、売買ごとに手数料0.25%。日付が進むにつれ、各シグナルの成功（緑）・失敗（赤）と成功率が、ランダム口座と並んで3Dチャートでリアルタイムに変わります。\nシグナルがまれにならないよう基準を広げ、結果を見る前にシグナルの出る回数だけで決めました。コードはAIが書き、未来の情報を使っていないか確認しました。税金・為替コストは含みません。ナレーションはAI音声です。\nデータ：Yahoo Finance（SPY、^VIX）。\n過去の結果は将来を保証しません。この動画は教育目的であり、投資助言ではありません。"
 },
 "de": {
  "title": "Wann kaufen: Erreichen Dip-, RSI- und Ausbruchssignale öfter +5 % vor −2 % als zufällige Käufe?",
  "description": "Gekauft – und sofort fällt der Kurs … falscher Zeitpunkt? Erhöhen beliebte Kaufsignale wirklich die Erfolgschance?\nWir haben 10 gängige Kaufsignale mit derselben Regel getestet: Ein Trade ist erfolgreich, wenn der Schlusskurs 5 % über dem Kaufkurs liegt, bevor er 2 % darunter fällt. Steht das Ergebnis fest, verkaufen wir am nächsten Tag und kaufen beim nächsten Signal erneut. Verglichen wird mit 2.000 Konten, die ohne Signal an zufälligen Tagen kaufen (gleich viele Trades, gleiche Verkaufsregel). SPY, Januar 2016 bis Oktober 2026, 0,25 % Gebühr pro Trade. Ein 3D-Chart zeigt in Echtzeit Erfolge (grün), Misserfolge (rot) und die Erfolgsquote jedes Signals neben den Zufallskonten.\nDie Schwellen wurden gelockert, damit die Signale nicht zu selten sind, und nur nach ihrer Häufigkeit festgelegt – bevor die Ergebnisse angesehen wurden. Den Code hat eine KI geschrieben; er wurde auf Look-ahead-Bias geprüft. Steuern und Wechselkosten sind nicht enthalten. Die Sprecherstimme ist eine KI-Stimme.\nDaten: Yahoo Finance (SPY, ^VIX).\nVergangene Ergebnisse garantieren keine zukünftigen Renditen. Dieses Video dient nur der Bildung und ist keine Anlageberatung."
 },
 "vi": {
  "title": "Khi nào mua: tín hiệu giảm sâu, RSI, phá đỉnh có lên 5% trước khi xuống 2% nhiều hơn mua ngẫu nhiên?",
  "description": "Vừa mua thì giá giảm ngay... có phải sai thời điểm? Các tín hiệu mua phổ biến có thật sự làm tăng xác suất thành công?\nChúng tôi thử 10 tín hiệu mua thông dụng với cùng một quy tắc: thành công nếu giá đóng cửa tăng 5% so với giá mua trước khi giảm 2%. Khi đã có kết quả, bán vào ngày hôm sau và mua lại khi có tín hiệu tiếp theo. Đối chứng là 2.000 tài khoản mua vào ngày ngẫu nhiên, không cần tín hiệu (cùng số giao dịch, cùng quy tắc bán). SPY, từ tháng 1/2016 đến tháng 10/2026, phí 0,25% mỗi giao dịch. Biểu đồ 3D cho thấy theo thời gian thực số lần thành công (xanh), thất bại (đỏ) và tỷ lệ thành công của từng tín hiệu bên cạnh các tài khoản ngẫu nhiên.\nNgưỡng tín hiệu được nới rộng để tín hiệu không quá hiếm, và chỉ dựa trên tần suất xuất hiện, trước khi xem kết quả. Mã do AI viết và đã được kiểm tra lỗi dùng dữ liệu tương lai. Chưa tính thuế và chi phí đổi tiền. Giọng đọc là giọng AI.\nDữ liệu: Yahoo Finance (SPY, ^VIX).\nKết quả quá khứ không đảm bảo tương lai. Video chỉ nhằm mục đích giáo dục, không phải lời khuyên đầu tư."
 },
 "tr": {
  "title": "Ne zaman almalı: düşüş, RSI ve kırılım sinyali, rastgele alımdan sık mı %2 düşmeden %5 çıkar?",
  "description": "Alır almaz fiyat düşerse zamanlama mı yanlıştı diye düşünürsünüz. Popüler alım sinyalleri başarı olasılığını gerçekten artırıyor mu?\n10 yaygın alım sinyalini aynı kuralla test ettik: kapanış, alış fiyatının %2 altına düşmeden %5 üstüne çıkarsa başarılı. Sonuç belli olunca ertesi gün satıyor, bir sonraki sinyalde yeniden alıyoruz. Karşılaştırma: sinyal olmadan rastgele günlerde alım yapan 2.000 hesap (aynı işlem sayısı, aynı satış kuralı). SPY, Ocak 2016'dan Ekim 2026'ya, işlem başına %0,25 komisyon. 3D grafik, her sinyalin başarılarını (yeşil), başarısızlıklarını (kırmızı) ve başarı oranını rastgele hesaplarla yan yana gerçek zamanlı gösteriyor.\nSinyaller nadir olmasın diye eşikler genişletildi ve sonuçlara bakmadan yalnızca sinyallerin sıklığına göre belirlendi. Kodu yapay zekâ yazdı; geleceğe bakma hatasına karşı test edildi. Vergi ve kur maliyetleri dahil değildir. Seslendirme yapay zekâ sesidir.\nVeri: Yahoo Finance (SPY, ^VIX).\nGeçmiş sonuçlar gelecekteki getirileri garanti etmez. Bu video yalnızca eğitim amaçlıdır, yatırım tavsiyesi değildir."
 }
}
```

## 6. 고정 댓글

```
10가지 매수 신호 가운데, 무작위로 매수한 것보다 성공 확률이 높을 거라고 생각한 신호가 있었나요? 지금 쓰고 계신 신호가 있다면 몇 번인지도 알려 주세요.
다음에 백테스트로 검증해 볼 가설도 댓글로 남겨 주세요.
(정보 제공용이며 투자 권유가 아닙니다)
```

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올리고 **1시간 뒤 예약 공개** (`--publish-at +1h`) |
| 썸네일 | `thumbnails/thumbnail_1.*` (본안 — 글자 없음). 공개 뒤 '테스트 및 비교'에 thumbnail_1~3 |
| 기본 언어 | ko |
| 자막 올리기 | **아니요** (전 세계 대상 — 자막을 굽지도 올리지도 않음, 사용자 지시 2026-10-15) |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 (내레이션) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 (전 세계 대상) |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — 사용자 지시 2026-10-11) |

## 8. 점검

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과(무작위보다 높은 신호가 있었는지·성공률·순위)를 쓰지 않았다. 결과는 영상 각 장의 끝과 '10가지 결과'(s141~)에서만.
- 설명란·언어별 설명의 숫자(2016-01-04·2026-10-15·5%·2%·0.25%·2천 개·1.1%·1%·1.5%·1994~2015·20·21·5·14·40·30·1%)는 대본·`backtest/barrier/results.json`·`run.py` 설정에 있는 것만 썼다 (하루 보통 움직임 1.1% = results.json choose_m.daily_std 1.12%).
- 제목 56자 · 언어별 제목 54~100자 (모두 100자 이하) · `< >` 없음 — `python tools/youtube_upload.py stock eonje-maesu-2026-10 --dry-run` 으로 확인.
- 사다 → 매수, 팔다 → 매도.

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, 시청 지속 그래프에서 크게 떨어지는 장(1~10), **나라·언어별 조회수**
