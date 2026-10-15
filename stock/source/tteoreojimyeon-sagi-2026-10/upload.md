# tteoreojimyeon-sagi-2026-10 업로드 시트

버전: v1.1 — 2026-10-15 — 대본 v1.1(143문장: 한계에 '한 달 평균 가격' 3문장)에 맞춰 챕터 '정리' 132→135·시각 다시 계산, 설명란 실험 방법에 월평균 판단 한 줄. v1.0 — 최초 (`guides/upload_guide.md` 8번 형식 + `stock/guides/README.md` 2·4번: 언어별 제목·설명, 자막 올리지 않음). 사용자 지시 2026-10-15 "제목, 대본, 썸네일 프롬프트, 영상까지 다 만들어봐" · "주식 주제는 전세계 사람들 대상으로 할거니까 영상에 자막 달지말고 … 그 언어로 제목 각각 만들어".
기준 파일: 대본 v1.1 (143문장) · SRT 문장 143 / 자막 156 (추정 시각 — 오디오가 생기면 align-audio 로 다시) · 결과 `backtest/results.json` (`run.py` v1.5) · 올릴 영상 = 렌더 원본 → Google Drive `내 드라이브/youtube/stock/tteoreojimyeon-sagi-2026-10.mp4`

> 업로드: PC 의 `run_uploader.ps1` (`guides/upload_guide.md` 11번) — 비공개 업로드 + **1시간 뒤 예약 공개**. 언어별 제목·설명은 `tools/youtube_upload.py` v1.6 이 `localizations` 로 함께 올린다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (`titles.md` R1, 한국어 — 기본 언어)

```
떨어지면 사겠다는 돈, 23년 치 돌려 보니 163번 중 117번 졌다
```

## 2. 설명란 (한국어 — 그대로 복사)

```
"10% 떨어지면 사겠다"며 기다린 돈은, 2000년부터 23년 동안의 미국 S&P500 실제 자료로 163번 돌려 본 결과 117번 매달 산 돈보다 적게 남았습니다.
기다린 쪽이 이긴 때도 많아야 1.2%, 매달 산 쪽이 이긴 때는 25% 넘게 차이가 났습니다.
큰 폭락(20%)까지 기다리면 결과는 반반 — 폭락이 언제 오느냐에 달렸고, 목돈은 한 번에 넣는 쪽이 셋 중 둘 더 많았지만 가장 나쁠 때는 1년 뒤 −43%(나눠 넣으면 −26%)였습니다.

■ 챕터
0:00 떨어지면 사겠다는 현금
1:09 실험 방법, 163번
3:05 결과, 163번 중 117번
5:07 원칙 1 기다리는 돈은 쉬고 있다
5:47 원칙 2 조금 싸게 사도 덜 남는다
6:31 원칙 3 폭락이 언제 올지는 모른다
7:30 사상 최고치에 사도 될까
8:18 목돈은 한 번에, 아니면 나눠서
9:40 이 실험의 한계
10:41 정리

■ 실험 방법
매달 100만 원, 10년. 시작 달을 2000년 1월부터 2013년 7월까지 한 달씩 옮겨 163번 계산했습니다.
A: 매달 바로 산다 / B: 한 달 평균 가격이 그때까지 최고치보다 10% 낮아지면 다음 달에 모은 돈을 한꺼번에 산다.
배당은 다시 넣었고, 수수료·세금·환율은 넣지 않았습니다. 판단은 한 달 평균 가격 기준이라 하루 가격의 짧은 하락은 놓칩니다 — 2016년부터는 하루 종가로 다시 계산해도 같은 결과였습니다.
계산 코드는 AI가 짰고, 한 달씩 사고 모으는 계산과 같은지·미래 가격을 쓰지 않는지 시험한 뒤 돌렸습니다.
영상 속 두 사람(55세 직장인)은 계산용 가상 인물이며, 숫자는 실제 자료입니다. 이 영상의 내레이션은 AI 음성입니다.

■ 자료
Robert Shiller S&P500 월별 자료(배당·금리) + FRED S&P500 — github.com/datasets/s-and-p-500 (2026-10-01 자료). 총수익은 배당 자료가 있는 2023년 6월까지.

■ 알려 드립니다
과거 자료로 계산한 결과이며 앞으로도 같다는 보장은 없습니다. 특정 상품을 사라는 이야기가 아니며 투자 권유가 아닙니다.

#S&P500 #백테스트 #적립식
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/tteoreojimyeon-sagi-2026-10/tteoreojimyeon-sagi-2026-10.txt stock/source/tteoreojimyeon-sagi-2026-10/tteoreojimyeon-sagi-2026-10.srt --chapters "1=떨어지면 사겠다는 현금;14=실험 방법, 163번;40=결과, 163번 중 117번;64=원칙 1 기다리는 돈은 쉬고 있다;73=원칙 2 조금 싸게 사도 덜 남는다;82=원칙 3 폭락이 언제 올지는 모른다;95=사상 최고치에 사도 될까;104=목돈은 한 번에, 아니면 나눠서;121=이 실험의 한계;135=정리"
```
- 2026-10-15 추정 시각(오디오 전)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 올릴 때 오디오에 맞춘 SRT로 다시 계산해 2번 설명란에 넣는다.
- 언어별 설명(5번)에는 챕터를 넣지 않았다 (시각이 오디오 뒤에 바뀌므로).

## 4. 태그

```
S&P500, S&P 500, 백테스트, 적립식, 매달 적립, 분할매수, 떨어지면 사기, 장기투자, 사상 최고치, 목돈 투자, 미국 지수, backtest, dollar cost averaging, buy the dip, lump sum vs DCA
```

## 5. 언어별 제목·설명 (localizations)

`stock/guides/README.md` 2번의 9개 언어 (기본 언어 ko 는 1·2번). JSON — 업로드 도구가 그대로 읽는다 (고칠 때 따옴표·쉼표 주의).

```
{
 "en": {
  "title": "Waiting for a 10% dip to buy? 23 years of S&P 500 data: it lost 117 of 163 times",
  "description": "We tested \"I'll buy when it drops 10%\" against simply buying every month, using real S&P 500 data from January 2000 to June 2023 (dividends reinvested) over 163 ten-year periods.\n\nWaiting for the dip ended with less money in 117 of 163 periods. When waiting won, it was ahead by at most 1.2%; when buying every month won, the gap was more than 25%.\nOver 20 years, buying every month won all 43 periods. Waiting for a 20% crash was a coin flip that depended on when the crash came.\nWith a lump sum, investing all at once beat spreading it over 12 months in 195 of 271 cases, but the worst one-year loss was 43% versus 26%.\n\nThe backtest code was written by AI and checked against a month-by-month simulation and for look-ahead bias.\nData: Robert Shiller / FRED via github.com/datasets/s-and-p-500. Fees, taxes and currency effects are not included.\nPast results do not guarantee future returns. This video is for education only and is not investment advice."
 },
 "hi": {
  "title": "10% गिरावट का इंतज़ार करके खरीदें? S&P 500 के 23 साल के डेटा में 163 में से 117 बार हार",
  "description": "हमने \"10% गिरने पर खरीदूँगा\" की तुलना हर महीने नियमित खरीद से की — जनवरी 2000 से जून 2023 तक के असली S&P 500 डेटा (डिविडेंड दोबारा निवेश) से, 163 अलग-अलग 10-साल की अवधियों में।\n\n163 में से 117 अवधियों में गिरावट का इंतज़ार करने वाले के पास कम पैसा बचा। इंतज़ार जीता भी तो ज़्यादा से ज़्यादा 1.2% से; हर महीने खरीदने वाला जीता तो अंतर 25% से भी ज़्यादा था।\n20 साल में हर महीने खरीदने वाला सभी 43 बार जीता।\n\nबैकटेस्ट का कोड AI ने लिखा और उसे महीने-दर-महीने गणना और भविष्य के डेटा (look-ahead) की जाँच से परखा गया।\nडेटा: Robert Shiller / FRED (github.com/datasets/s-and-p-500)। फीस, टैक्स और मुद्रा का असर शामिल नहीं है।\nपिछले नतीजे भविष्य की गारंटी नहीं हैं। यह वीडियो केवल शिक्षा के लिए है, निवेश सलाह नहीं।"
 },
 "id": {
  "title": "Menunggu turun 10% baru beli? Data S&P 500 selama 23 tahun: kalah 117 dari 163 kali",
  "description": "Kami membandingkan \"beli kalau sudah turun 10%\" dengan membeli rutin setiap bulan, memakai data asli S&P 500 dari Januari 2000 sampai Juni 2023 (dividen diinvestasikan kembali) dalam 163 periode 10 tahun.\n\nMenunggu penurunan berakhir dengan uang lebih sedikit di 117 dari 163 periode. Saat menunggu menang, selisihnya paling banyak 1,2%; saat beli rutin menang, selisihnya lebih dari 25%.\nDalam 20 tahun, beli rutin setiap bulan menang di semua 43 periode.\n\nKode backtest ditulis oleh AI dan diuji dengan simulasi bulan demi bulan serta pemeriksaan look-ahead bias.\nData: Robert Shiller / FRED melalui github.com/datasets/s-and-p-500. Biaya, pajak, dan kurs tidak dihitung.\nHasil masa lalu tidak menjamin hasil masa depan. Video ini hanya untuk edukasi, bukan saran investasi."
 },
 "pt": {
  "title": "Esperar cair 10% para comprar? 23 anos de dados do S&P 500: perdeu 117 de 163 vezes",
  "description": "Comparamos \"vou comprar quando cair 10%\" com simplesmente comprar todo mês, usando dados reais do S&P 500 de janeiro de 2000 a junho de 2023 (dividendos reinvestidos) em 163 períodos de 10 anos.\n\nEsperar a queda terminou com menos dinheiro em 117 de 163 períodos. Quando esperar venceu, a vantagem foi de no máximo 1,2%; quando comprar todo mês venceu, a diferença passou de 25%.\nEm 20 anos, comprar todo mês venceu nos 43 períodos.\n\nO código do backtest foi escrito por IA e testado contra uma simulação mês a mês e contra viés de antecipação (look-ahead).\nDados: Robert Shiller / FRED via github.com/datasets/s-and-p-500. Taxas, impostos e câmbio não foram incluídos.\nResultados passados não garantem resultados futuros. Este vídeo é educativo e não é recomendação de investimento."
 },
 "es-419": {
  "title": "¿Esperar a que caiga un 10% para comprar? 23 años del S&P 500: perdió 117 de 163 veces",
  "description": "Comparamos \"voy a comprar cuando caiga un 10%\" con simplemente comprar cada mes, usando datos reales del S&P 500 de enero de 2000 a junio de 2023 (dividendos reinvertidos) en 163 periodos de 10 años.\n\nEsperar la caída terminó con menos dinero en 117 de 163 periodos. Cuando esperar ganó, fue por 1.2% como máximo; cuando comprar cada mes ganó, la diferencia superó el 25%.\nEn 20 años, comprar cada mes ganó en los 43 periodos.\n\nEl código del backtest lo escribió una IA y se comprobó con una simulación mes a mes y contra el sesgo de anticipación (look-ahead).\nDatos: Robert Shiller / FRED vía github.com/datasets/s-and-p-500. No incluye comisiones, impuestos ni tipo de cambio.\nLos resultados pasados no garantizan resultados futuros. Este video es educativo y no es asesoría de inversión."
 },
 "ja": {
  "title": "10%下がったら買う？S&P500の23年分のデータで検証、163回中117回負けた",
  "description": "「10%下がったら買う」と「毎月決まった日に買う」を、2000年1月〜2023年6月のS&P500の実データ（配当再投資）で、10年間の期間163通りについて比べました。\n\n下落を待つ方法は163回中117回、毎月買う方法より少ないお金しか残りませんでした。待つ方が勝ったときの差は最大1.2%、毎月買う方が勝ったときの差は25%を超えました。\n20年で見ると、毎月買う方法が43回すべてで勝ちました。\n\nバックテストのコードはAIが書き、1か月ずつのシミュレーションとの一致と、未来の情報を使っていないかを確認しました。\nデータ：Robert Shiller / FRED（github.com/datasets/s-and-p-500）。手数料・税金・為替は含みません。\n過去の結果は将来を保証しません。この動画は教育目的であり、投資助言ではありません。"
 },
 "de": {
  "title": "Erst bei 10 % Rückgang kaufen? 23 Jahre S&P-500-Daten: 117 von 163 Mal verloren",
  "description": "Wir haben „Ich kaufe erst, wenn es 10 % fällt“ mit einfachem monatlichem Kaufen verglichen – mit echten S&P-500-Daten von Januar 2000 bis Juni 2023 (Dividenden reinvestiert) über 163 Zehnjahreszeiträume.\n\nDas Warten auf den Rückgang endete in 117 von 163 Zeiträumen mit weniger Geld. Wenn Warten gewann, lag es höchstens 1,2 % vorn; wenn monatliches Kaufen gewann, betrug der Abstand mehr als 25 %.\nÜber 20 Jahre gewann monatliches Kaufen alle 43 Zeiträume.\n\nDen Backtest-Code hat eine KI geschrieben; er wurde gegen eine Monat-für-Monat-Simulation und auf Look-ahead-Bias geprüft.\nDaten: Robert Shiller / FRED über github.com/datasets/s-and-p-500. Gebühren, Steuern und Wechselkurse sind nicht enthalten.\nVergangene Ergebnisse garantieren keine zukünftigen Renditen. Dieses Video dient nur der Bildung und ist keine Anlageberatung."
 },
 "vi": {
  "title": "Chờ giảm 10% mới mua? 23 năm dữ liệu S&P 500: thua 117 trên 163 lần",
  "description": "Chúng tôi so sánh \"giảm 10% rồi mới mua\" với việc mua đều đặn mỗi tháng, dùng dữ liệu thật của S&P 500 từ tháng 1/2000 đến tháng 6/2023 (tái đầu tư cổ tức) trên 163 giai đoạn 10 năm.\n\nChờ giá giảm kết thúc với ít tiền hơn ở 117 trên 163 giai đoạn. Khi chờ thắng, chênh lệch nhiều nhất chỉ 1,2%; khi mua mỗi tháng thắng, chênh lệch vượt quá 25%.\nTrong 20 năm, mua mỗi tháng thắng cả 43 giai đoạn.\n\nMã backtest do AI viết và đã được kiểm tra với mô phỏng từng tháng cũng như lỗi dùng dữ liệu tương lai (look-ahead).\nDữ liệu: Robert Shiller / FRED qua github.com/datasets/s-and-p-500. Chưa tính phí, thuế và tỷ giá.\nKết quả quá khứ không đảm bảo tương lai. Video chỉ nhằm mục đích giáo dục, không phải lời khuyên đầu tư."
 },
 "tr": {
  "title": "Yüzde 10 düşüşü bekleyip almak mı? 23 yıllık S&P 500 verisi: 163 denemenin 117'sinde kaybetti",
  "description": "\"Yüzde 10 düşünce alırım\" yaklaşımını her ay düzenli almakla karşılaştırdık: Ocak 2000 – Haziran 2023 arasındaki gerçek S&P 500 verileriyle (temettüler yeniden yatırıldı), 163 farklı 10 yıllık dönemde.\n\nDüşüşü beklemek 163 dönemin 117'sinde daha az parayla bitti. Beklemek kazandığında fark en fazla yüzde 1,2 oldu; her ay almak kazandığında fark yüzde 25'i aştı.\n20 yıllık dönemlerde her ay almak 43 dönemin hepsinde kazandı.\n\nBacktest kodunu yapay zekâ yazdı; ay ay simülasyonla ve geleceğe bakma (look-ahead) hatasına karşı test edildi.\nVeri: Robert Shiller / FRED, github.com/datasets/s-and-p-500 üzerinden. Komisyon, vergi ve kur etkisi dahil değildir.\nGeçmiş sonuçlar gelecekteki getirileri garanti etmez. Bu video yalnızca eğitim amaçlıdır, yatırım tavsiyesi değildir."
 }
}
```

## 6. 고정 댓글

```
A: 매달 산다 / B: 10% 떨어지면 산다 — 163번 중 117번 A가 더 많이 남았습니다.
여러분은 어느 쪽이었나요? 다음에 검증해 볼 가설도 댓글로 알려 주세요.
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

- 설명란·태그·고정 댓글·언어별 설명의 숫자는 `checklist.md`(50/50 ✅)와 `backtest/results.json`에 있는 것만 썼다.
- 한국어 제목 39자 · 언어별 제목 42~93자 (모두 100자 이하) · 설명란 1030자 · `< >` 없음.
- 언어별 설명의 '26%'(나눠 넣은 경우)는 같은 달(2008-04) 비교다 (`E3.main_12m_all_cash0.split_at_lump_worst`).

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, **나라·언어별 조회수**(스튜디오 '지역'·'자막·더빙 언어')
