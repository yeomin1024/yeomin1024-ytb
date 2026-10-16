# eonje-maesu-2026-10 업로드 시트

버전: v1.0 — 2026-10-16 — 최초 (`guides/upload_guide.md` 8번 형식 + `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음).
기준 파일: 대본 v1.0 (125문장) · SRT 문장 125 (추정 시각 — 오디오가 생기면 align-audio 로 다시) · 결과 `backtest/results.json` (`run.py` v1.2) · 올릴 영상 = 렌더 원본 `stock/out/eonje-maesu-2026-10/final_1080p.mp4`

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json` — 업로드 도구 v1.7 이 채널이 다르면 올리지 않음)로 `python tools/youtube_upload.py stock eonje-maesu-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (`titles.md` R1, 한국어 — 기본 언어)

```
매수 타이밍, 손절·익절·이평선 등 매수 규칙 10가지는 사서 들고만 있기보다 더 벌까? 32년 백테스트
```

## 2. 설명란 (한국어 — 그대로 복사)

```
"주식은 언제 매수해야 할까?" 떨어지면 사라, 10%에 손절해라, 이동평균선을 봐라… 방법이 정말 많습니다.
많이 쓰는 매수 규칙 10가지를, 그냥 사서 들고 있는 '관망'과 같은 1만 달러로 1991년 1월부터 2023년 6월까지 하나씩 붙여 봤습니다.
날짜가 흐르며 두 계좌가 어떻게 달라지는지, 시작 달을 바꿔 271번 다시 돌리면 어떻게 되는지까지 숫자로 확인합니다.

■ 챕터
0:00 언제 매수할까
0:27 1 분할 매수
1:25 2 저점 매수
2:06 3 물타기
2:40 4 익절
3:22 5 RSI
4:04 6 신고가 돌파
4:41 7 200일 이동평균선
5:33 8 골든 크로스
6:20 9 12개월 모멘텀
7:00 10 손절
7:52 종합 결과
9:37 이 실험의 한계
9:59 정리

■ 비교한 규칙 10가지
1 분할 매수 12개월 / 2 저점 매수(최고가보다 10% 낮으면) / 3 물타기(최고가보다 10·20·30% 낮을 때마다 4분의 1) / 4 익절 +10% / 5 RSI 30·70 / 6 신고가 돌파(55일·20일) / 7 200일 이동평균선 / 8 골든 크로스 50·200일 / 9 12개월 모멘텀 / 10 손절 −10%(반등 +10% 재매수)
규칙의 숫자는 교과서 기본값이며, 결과를 보고 바꾸지 않았습니다.

■ 실험 방법
자료: 배당을 다시 넣은 미국 S&P500 지수(일별), 1991-01-02 ~ 2023-06-30. 시작 돈 1만 달러 — 규칙과 관망 모두 같고, 더 넣거나 빼지 않습니다.
신호는 그날 종가까지만 보고, 사고파는 것은 다음 거래일 종가. 거래마다 비용 0.1%. 현금 이자는 0 (확인용으로 단기 국채 이자·10년 국채 금리도 계산).
여러 시작 시점: 1991년 1월부터 2013년 7월까지 매달 시작해 10년씩 271번. 나스닥 종합 지수와 2026년 2월까지(가격만)로도 확인했습니다.
계산 코드는 AI가 짰고, 미래 가격을 쓰지 않는지와 따로 쓴 계산과 같은 답이 나오는지 시험한 뒤 돌렸습니다.
세금·환율·상품 보수는 넣지 않았습니다. 이 영상의 내레이션은 AI 음성입니다.

■ 자료
S&P500 일별 종가: skfolio 1.9.0 자료(1990~2016) + FRED SP500(2016~) · 배당: Robert Shiller (github.com/datasets/s-and-p-500) · 나스닥 종합·1개월 T-bill: arch 8.0.0 자료(Kenneth R. French Data Library)

■ 알려 드립니다
과거 자료로 계산한 결과이며 앞으로도 같다는 보장은 없습니다. 특정 상품을 매수하라는 이야기가 아니며 투자 권유가 아닙니다.

#매수타이밍 #백테스트 #S&P500
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/eonje-maesu-2026-10/eonje-maesu-2026-10.txt stock/source/eonje-maesu-2026-10/eonje-maesu-2026-10.srt --chapters "1=언제 매수할까;6=1 분할 매수;17=2 저점 매수;25=3 물타기;32=4 익절;40=5 RSI;47=6 신고가 돌파;55=7 200일 이동평균선;64=8 골든 크로스;73=9 12개월 모멘텀;80=10 손절;89=종합 결과;109=이 실험의 한계;114=정리"
```
- 2026-10-16 추정 시각(오디오 전)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 올릴 때 오디오에 맞춘 SRT로 다시 계산해 2번 설명란에 넣는다.
- 챕터 이름에 결과를 쓰지 않는다 (진행 막대에 미리 보이므로).

## 4. 태그

```
매수 타이밍, 손절, 익절, 분할매수, 물타기, 저점매수, 이동평균선, 200일 이동평균선, 골든크로스, RSI, 모멘텀, 백테스트, S&P500, buy and hold, backtest
```

## 5. 언어별 제목·설명 (localizations)

`stock/guides/README.md` 2번의 9개 언어 (기본 언어 ko 는 1·2번). JSON — 업로드 도구가 그대로 읽는다 (고칠 때 따옴표·쉼표 주의). 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜).

```
{
 "en": {
  "title": "When to buy: do 10 popular buy rules beat simple buy and hold? 32-year S&P 500 backtest",
  "description": "\"When should I buy?\" Buy the dip, use a 10% stop-loss, watch the 200-day moving average... there are many rules.\nWe took 10 popular buy rules and put each one against simple buy and hold, with the same $10,000, from January 1991 to June 2023 (S&P 500 with dividends reinvested). We also restart every month to run 271 ten-year periods.\n\nRules: 12-month split buying, buy the dip (10% below the high), averaging down at -10/-20/-30%, +10% take-profit, RSI 30/70, 55/20-day breakout, 200-day moving average, 50/200 golden cross, 12-month momentum, -10% trailing stop. Textbook settings, not tuned to the results.\nSignals use closing prices up to that day; trades happen at the next day's close; 0.1% cost per trade; no interest on cash (checked with T-bill and 10-year yields too). The backtest code was written by AI and tested for look-ahead bias and against an independent calculation. Taxes, currency effects and fund fees are not included. The narration is an AI voice.\nData: skfolio 1.9.0 and FRED (S&P 500 closes), Robert Shiller (dividends), arch 8.0.0 (NASDAQ Composite, Fama-French T-bill).\nPast results do not guarantee future returns. This video is for education only and is not investment advice."
 },
 "hi": {
  "title": "कब खरीदें: क्या 10 लोकप्रिय खरीद नियम सिर्फ खरीदकर रखने से ज़्यादा कमाते हैं? S&P 500 के 32 साल",
  "description": "\"शेयर कब खरीदें?\" गिरावट में खरीदो, 10% पर स्टॉप-लॉस लगाओ, 200 दिन की औसत देखो... नियम बहुत हैं।\nहमने 10 लोकप्रिय खरीद नियमों को एक-एक करके सिर्फ खरीदकर रखने से मिलाया — दोनों में वही $10,000, जनवरी 1991 से जून 2023 तक (डिविडेंड दोबारा निवेश के साथ S&P 500)। हर महीने नई शुरुआत करके 10-10 साल की 271 अवधियाँ भी चलाईं।\nसिग्नल उसी दिन के बंद भाव तक, सौदा अगले दिन के बंद भाव पर, हर सौदे पर 0.1% खर्च, नकद पर ब्याज नहीं (जाँच के लिए ब्याज के साथ भी)। कोड AI ने लिखा और भविष्य के डेटा व अलग गणना से जाँचा। टैक्स, मुद्रा और फंड फीस शामिल नहीं। वॉइस-ओवर AI आवाज़ है।\nपिछले नतीजे भविष्य की गारंटी नहीं हैं। यह वीडियो केवल शिक्षा के लिए है, निवेश सलाह नहीं।"
 },
 "id": {
  "title": "Kapan beli: apakah 10 aturan beli populer lebih untung daripada beli lalu tahan? 32 tahun S&P 500",
  "description": "\"Kapan sebaiknya beli saham?\" Beli saat turun, cut loss 10%, lihat rata-rata 200 hari... aturannya banyak.\nKami membandingkan 10 aturan beli populer satu per satu dengan sekadar beli lalu tahan, dengan $10.000 yang sama, dari Januari 1991 sampai Juni 2023 (S&P 500 dengan dividen diinvestasikan kembali). Kami juga memulai ulang setiap bulan untuk 271 periode 10 tahun.\nSinyal memakai harga penutupan sampai hari itu, transaksi di penutupan hari berikutnya, biaya 0,1% per transaksi, tanpa bunga kas (juga dicek dengan bunga). Kode ditulis oleh AI dan diuji terhadap look-ahead bias serta perhitungan terpisah. Pajak, kurs, dan biaya reksa dana tidak dihitung. Narasi memakai suara AI.\nHasil masa lalu tidak menjamin hasil masa depan. Video ini hanya untuk edukasi, bukan saran investasi."
 },
 "pt": {
  "title": "Quando comprar: 10 regras populares de compra rendem mais que comprar e segurar? 32 anos de S&P 500",
  "description": "\"Quando devo comprar?\" Compre na queda, use stop-loss de 10%, olhe a média de 200 dias... as regras são muitas.\nComparamos 10 regras populares de compra, uma a uma, com simplesmente comprar e segurar, com os mesmos US$ 10.000, de janeiro de 1991 a junho de 2023 (S&P 500 com dividendos reinvestidos). Também recomeçamos a cada mês para 271 períodos de 10 anos.\nOs sinais usam fechamentos até aquele dia; as operações ocorrem no fechamento do dia seguinte; custo de 0,1% por operação; sem juros no caixa (também conferido com juros). O código foi escrito por IA e testado contra viés de antecipação e um cálculo independente. Impostos, câmbio e taxas de fundos não foram incluídos. A narração é uma voz de IA.\nResultados passados não garantem resultados futuros. Este vídeo é educativo e não é recomendação de investimento."
 },
 "es-419": {
  "title": "¿Cuándo comprar? ¿10 reglas populares de compra ganan más que comprar y mantener? 32 años S&P 500",
  "description": "\"¿Cuándo debo comprar?\" Compra en la caída, usa un stop-loss del 10%, mira la media de 200 días... hay muchas reglas.\nComparamos 10 reglas populares de compra, una por una, con simplemente comprar y mantener, con los mismos US$10,000, de enero de 1991 a junio de 2023 (S&P 500 con dividendos reinvertidos). También reiniciamos cada mes para 271 periodos de 10 años.\nLas señales usan cierres hasta ese día; las operaciones se hacen al cierre del día siguiente; costo de 0.1% por operación; sin intereses en efectivo (también revisado con intereses). El código lo escribió una IA y se probó contra el sesgo de anticipación y un cálculo independiente. No incluye impuestos, tipo de cambio ni comisiones de fondos. La narración es una voz de IA.\nLos resultados pasados no garantizan resultados futuros. Este video es educativo y no es asesoría de inversión."
 },
 "ja": {
  "title": "買うタイミング：よく使われる売買ルール10個は、買って持つだけより儲かる？S&P500の32年バックテスト",
  "description": "「株はいつ買えばいい？」下がったら買え、10%で損切り、200日移動平均を見ろ…ルールはたくさんあります。\nよく使われる売買ルール10個を、ただ買って持ち続ける「ほったらかし」と、同じ1万ドルで1991年1月から2023年6月まで一つずつ比べました（配当再投資のS&P500）。開始月を毎月ずらした10年×271通りも確かめます。\nシグナルはその日の終値までで判断し、売買は翌営業日の終値、1回0.1%のコスト、現金の利息は0（確認用に利息ありも計算）。コードはAIが書き、未来の情報を使っていないか・別の計算と一致するかを確認しました。税金・為替・ファンド手数料は含みません。ナレーションはAI音声です。\n過去の結果は将来を保証しません。この動画は教育目的であり、投資助言ではありません。"
 },
 "de": {
  "title": "Wann kaufen: Bringen 10 beliebte Kaufregeln mehr als einfach Kaufen und Halten? 32 Jahre S&P 500",
  "description": "„Wann soll ich kaufen?“ Buy the Dip, 10 % Stop-Loss, auf den 200-Tage-Durchschnitt achten … es gibt viele Regeln.\nWir haben 10 beliebte Kaufregeln einzeln gegen einfaches Kaufen und Halten antreten lassen – mit denselben 10.000 US-Dollar, von Januar 1991 bis Juni 2023 (S&P 500 mit reinvestierten Dividenden). Außerdem starten wir jeden Monat neu für 271 Zehnjahreszeiträume.\nSignale nutzen Schlusskurse bis zu diesem Tag, gehandelt wird zum Schlusskurs des nächsten Tages, 0,1 % Kosten pro Trade, keine Zinsen auf Bargeld (auch mit Zinsen geprüft). Den Code hat eine KI geschrieben; er wurde auf Look-ahead-Bias und gegen eine unabhängige Rechnung geprüft. Steuern, Wechselkurse und Fondsgebühren sind nicht enthalten. Die Sprecherstimme ist eine KI-Stimme.\nVergangene Ergebnisse garantieren keine zukünftigen Renditen. Dieses Video dient nur der Bildung und ist keine Anlageberatung."
 },
 "vi": {
  "title": "Khi nào nên mua: 10 quy tắc mua phổ biến có lãi hơn mua rồi giữ không? Backtest 32 năm S&P 500",
  "description": "\"Khi nào nên mua cổ phiếu?\" Mua khi giảm, cắt lỗ 10%, nhìn đường trung bình 200 ngày... quy tắc thì rất nhiều.\nChúng tôi đặt 10 quy tắc mua phổ biến lần lượt cạnh việc chỉ mua rồi giữ, cùng 10.000 USD, từ tháng 1/1991 đến tháng 6/2023 (S&P 500 có tái đầu tư cổ tức). Chúng tôi cũng bắt đầu lại mỗi tháng để chạy 271 giai đoạn 10 năm.\nTín hiệu dùng giá đóng cửa đến ngày đó, giao dịch ở giá đóng cửa ngày hôm sau, phí 0,1% mỗi giao dịch, tiền mặt không có lãi (cũng kiểm tra khi có lãi). Mã do AI viết và đã được kiểm tra lỗi dùng dữ liệu tương lai cũng như so với một phép tính độc lập. Chưa tính thuế, tỷ giá và phí quỹ. Giọng đọc là giọng AI.\nKết quả quá khứ không đảm bảo tương lai. Video chỉ nhằm mục đích giáo dục, không phải lời khuyên đầu tư."
 },
 "tr": {
  "title": "Ne zaman almalı: 10 popüler alım kuralı, al ve tut'tan daha mı kârlı? 32 yıllık S&P 500 testi",
  "description": "\"Ne zaman almalıyım?\" Düşüşte al, %10'da zarar kes, 200 günlük ortalamaya bak... kurallar çok.\n10 popüler alım kuralını tek tek basitçe al ve tut ile karşılaştırdık; ikisinde de aynı 10.000 dolar, Ocak 1991'den Haziran 2023'e kadar (temettüleri yeniden yatırılan S&P 500). Ayrıca her ay yeniden başlayarak 271 adet 10 yıllık dönem çalıştırdık.\nSinyaller o günün kapanışına kadar olan fiyatları kullanır, işlemler ertesi günün kapanışında yapılır, işlem başına %0,1 maliyet, nakitte faiz yok (faizle de kontrol edildi). Kodu yapay zekâ yazdı; geleceğe bakma hatasına ve bağımsız bir hesaba karşı test edildi. Vergi, kur ve fon ücretleri dahil değildir. Seslendirme yapay zekâ sesidir.\nGeçmiş sonuçlar gelecekteki getirileri garanti etmez. Bu video yalnızca eğitim amaçlıdır, yatırım tavsiyesi değildir."
 }
}
```

## 6. 고정 댓글

```
10가지 규칙 가운데, 지금 쓰고 계신 규칙이 있나요? 영상을 보기 전에는 몇 개가 '사서 들고 있기'보다 더 벌 거라고 생각하셨나요?
다음에 백테스트로 검증해 볼 규칙도 댓글로 알려 주세요.
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

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과(몇 개가 이겼는지·끝 값·193/271 등)를 쓰지 않았다. 결과는 영상 각 장의 끝과 '종합 결과'(s89~)에서만.
- 설명란·언어별 설명의 숫자(1만 달러·1991-01·2023-06·271번·10년·0.1%·10%·200일·55·20일·30·70·12개월)는 대본·`backtest/results.json`·`run.py` 설정에 있는 것만 썼다 (`checklist.md` 117/117 ✅).
- 제목 58자 · 언어별 제목 53~99자 (모두 100자 이하) · `< >` 없음 — `python tools/youtube_upload.py stock eonje-maesu-2026-10 --dry-run` 으로 확인.
- 사다 → 매수, 팔다 → 매도.

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, 시청 지속 그래프에서 크게 떨어지는 장(1~10), **나라·언어별 조회수**
