# tteoreojimyeon-sagi-2026-10 업로드 시트

버전: v2.0 — 2026-10-16 — 제목·설명·챕터·고정 댓글·언어별 제목·설명을 **결말 없이** 다시 (사용자 피드백 2026-10-16 "제목은 결말을 말하지말고 그리고 맨 앞에 시청자 니즈 만족하는 핵심 단어 사용하라고" · "샀다는 매수, 팔다는 매도 단어를 쓰고" · "제목은 명확하게 호기심을 유발하도록"). (v1.1 — 2026-10-15 — 대본 143문장 챕터. v1.0 — 최초 (`guides/upload_guide.md` 8번 형식 + `stock/guides/README.md` 2·4번: 언어별 제목·설명, 자막 올리지 않음).)
기준 파일: 대본 v1.2 (141문장) · SRT 문장 141 / 자막 154 (추정 시각 — 오디오가 생기면 align-audio 로 다시) · 결과 `backtest/results.json` (`run.py` v1.5) · 올릴 영상 = 렌더 원본 → Google Drive `내 드라이브/youtube/stock/tteoreojimyeon-sagi-2026-10.mp4`

> 업로드: PC 의 `run_uploader.ps1` (`guides/upload_guide.md` 11번) — 비공개 업로드 + **1시간 뒤 예약 공개**. 언어별 제목·설명은 `tools/youtube_upload.py` v1.6 이 `localizations` 로 함께 올린다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (`titles.md` R1, 한국어 — 기본 언어)

```
저점 매수, 최고점보다 10% 떨어질 때만 매수하면 매달 매수보다 더 벌까? 23년 백테스트
```

## 2. 설명란 (한국어 — 그대로 복사)

```
주가가 너무 올라서 "최고점보다 10% 떨어지면 그때 매수하겠다"며 현금을 들고 계신가요?
정말 떨어질 때까지 기다렸다 매수하면, 매달 정해진 날 매수한 사람보다 10년 뒤 수익이 더 많을까요?
2000년부터 23년 동안의 미국 S&P500 실제 자료로, 시작하는 달을 바꿔 가며 163번 백테스트했습니다.
20% 넘는 큰 폭락까지 기다리면 어떻게 되는지, 사상 최고치 근처에서 매수해도 되는지, 목돈은 한 번에 넣을지 나눠 넣을지도 숫자로 확인합니다.

■ 챕터
0:00 저점 매수, 기다리면 더 벌까
1:09 실험 방법, 163번
3:07 결과
5:10 원칙 1, 시장은 얼마나 자주 올랐나
5:50 원칙 2, 싸게 매수한 효과는
6:36 원칙 3, 큰 폭락을 기다리면
7:35 사상 최고치에 매수해도 될까
8:28 목돈은 한 번에, 아니면 나눠서
9:47 이 실험의 한계
10:50 정리

■ 실험 방법
매달 100만 원, 10년. 시작 달을 2000년 1월부터 2013년 7월까지 한 달씩 옮겨 163번 계산했습니다.
A: 매달 바로 매수 / B: 한 달 평균 가격이 그때까지의 최고점보다 10% 낮아지면 다음 달에 모은 돈을 한꺼번에 매수.
두 사람이 넣은 돈이 같으므로, 10년 뒤 남은 돈이 많은 쪽이 수익이 많은 쪽입니다.
배당은 다시 넣었고, 수수료·세금·환율은 넣지 않았습니다. 판단은 한 달 평균 가격 기준이라 하루 가격의 짧은 하락은 놓칩니다 — 2016년부터는 하루 종가로도 다시 계산했습니다.
계산 코드는 AI가 짰고, 한 달씩 매수하고 모으는 계산과 같은지·미래 가격을 쓰지 않는지 시험한 뒤 돌렸습니다.
영상 속 두 사람(55세 직장인)은 계산용 가상 인물이며, 숫자는 실제 자료입니다. 이 영상의 내레이션은 AI 음성입니다.

■ 자료
Robert Shiller S&P500 월별 자료(배당·금리) + FRED S&P500 — github.com/datasets/s-and-p-500 (2026-10-01 자료). 총수익은 배당 자료가 있는 2023년 6월까지.

■ 알려 드립니다
과거 자료로 계산한 결과이며 앞으로도 같다는 보장은 없습니다. 특정 상품을 매수하라는 이야기가 아니며 투자 권유가 아닙니다.

#저점매수 #S&P500 #백테스트
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/tteoreojimyeon-sagi-2026-10/tteoreojimyeon-sagi-2026-10.txt stock/source/tteoreojimyeon-sagi-2026-10/tteoreojimyeon-sagi-2026-10.srt --chapters "1=저점 매수, 기다리면 더 벌까;13=실험 방법, 163번;38=결과;62=원칙 1, 시장은 얼마나 자주 올랐나;71=원칙 2, 싸게 매수한 효과는;80=원칙 3, 큰 폭락을 기다리면;93=사상 최고치에 매수해도 될까;103=목돈은 한 번에, 아니면 나눠서;119=이 실험의 한계;133=정리"
```
- 2026-10-16 추정 시각(오디오 전)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 올릴 때 오디오에 맞춘 SRT로 다시 계산해 2번 설명란에 넣는다.
- **챕터 이름에도 결말을 쓰지 않는다** (진행 막대에 미리 보이므로 — 예전 '결과, 163번 중 117번'·'원칙 1 기다리는 돈은 쉬고 있다'를 바꿈).
- 언어별 설명(5번)에는 챕터를 넣지 않았다 (시각이 오디오 뒤에 바뀌므로).

## 4. 태그

```
저점매수, 매수 타이밍, S&P500, S&P 500, 백테스트, 적립식, 매달 매수, 분할매수, 떨어지면 매수, 장기투자, 사상 최고치, 목돈 투자, buy the dip, dollar cost averaging, backtest
```

## 5. 언어별 제목·설명 (localizations)

`stock/guides/README.md` 2번의 9개 언어 (기본 언어 ko 는 1·2번). JSON — 업로드 도구가 그대로 읽는다 (고칠 때 따옴표·쉼표 주의).

```
{
 "en": {
  "title": "Buy the dip: buy only after a 10% drop from the high. Does it beat buying monthly? 23 yrs of S&P 500",
  "description": "Prices feel too high, so you hold cash and wait: \"I'll buy when it falls 10% from the high.\" Does waiting for the dip really earn more than simply buying on the same day every month?\nWe backtested it with real S&P 500 data from January 2000 to June 2023 (dividends reinvested): 1,000,000 KRW a month for 10 years, starting in every month from January 2000 to July 2013 — 163 periods. We also test waiting for a 20% crash, buying near all-time highs, and investing a lump sum at once versus over 12 months.\n\nThe backtest code was written by AI and checked against a month-by-month simulation and for look-ahead bias.\nData: Robert Shiller / FRED via github.com/datasets/s-and-p-500. Fees, taxes and currency effects are not included.\nPast results do not guarantee future returns. This video is for education only and is not investment advice."
 },
 "hi": {
  "title": "गिरावट में खरीदारी: हाई से 10% गिरने पर ही खरीदें तो क्या हर महीने से ज़्यादा कमाई? 23 साल S&P 500",
  "description": "शेयर बहुत ऊपर लगते हैं, इसलिए आप नकद लेकर इंतज़ार कर रहे हैं: \"हाई से 10% गिरेगा तब खरीदूँगा।\" क्या गिरावट का इंतज़ार करके खरीदना, हर महीने एक तय दिन खरीदने से सच में ज़्यादा कमाई देता है?\nहमने जनवरी 2000 से जून 2023 तक के असली S&P 500 डेटा (डिविडेंड दोबारा निवेश) से बैकटेस्ट किया: 10 साल तक हर महीने 1,000,000 KRW, शुरुआत जनवरी 2000 से जुलाई 2013 तक हर महीने — कुल 163 अवधियाँ। 20% की बड़ी गिरावट का इंतज़ार, ऑल-टाइम हाई के पास खरीद, और एकमुश्त बनाम 12 महीनों में निवेश भी जाँचा गया।\n\nबैकटेस्ट का कोड AI ने लिखा और उसे महीने-दर-महीने गणना और भविष्य के डेटा (look-ahead) की जाँच से परखा गया।\nडेटा: Robert Shiller / FRED (github.com/datasets/s-and-p-500)। फीस, टैक्स और मुद्रा का असर शामिल नहीं है।\nपिछले नतीजे भविष्य की गारंटी नहीं हैं। यह वीडियो केवल शिक्षा के लिए है, निवेश सलाह नहीं।"
 },
 "id": {
  "title": "Beli saat turun: hanya beli saat turun 10% dari puncak, lebih untung dari beli rutin? 23 thn S&P 500",
  "description": "Harga terasa terlalu tinggi, jadi Anda memegang uang tunai dan menunggu: \"Saya beli kalau sudah turun 10% dari puncak.\" Apakah menunggu penurunan benar-benar lebih untung daripada membeli di tanggal yang sama setiap bulan?\nKami melakukan backtest dengan data asli S&P 500 dari Januari 2000 sampai Juni 2023 (dividen diinvestasikan kembali): 1.000.000 KRW per bulan selama 10 tahun, dimulai di setiap bulan dari Januari 2000 sampai Juli 2013 — 163 periode. Kami juga menguji menunggu penurunan besar 20%, membeli di dekat rekor tertinggi, serta uang sekaligus vs dicicil 12 bulan.\n\nKode backtest ditulis oleh AI dan diuji dengan simulasi bulan demi bulan serta pemeriksaan look-ahead bias.\nData: Robert Shiller / FRED melalui github.com/datasets/s-and-p-500. Biaya, pajak, dan kurs tidak dihitung.\nHasil masa lalu tidak menjamin hasil masa depan. Video ini hanya untuk edukasi, bukan saran investasi."
 },
 "pt": {
  "title": "Comprar na queda: comprar só após cair 10% do topo rende mais que comprar todo mês? 23 anos S&P 500",
  "description": "Os preços parecem altos demais, então você guarda dinheiro e espera: \"Vou comprar quando cair 10% do topo.\" Esperar a queda rende mesmo mais do que comprar no mesmo dia todo mês?\nFizemos um backtest com dados reais do S&P 500 de janeiro de 2000 a junho de 2023 (dividendos reinvestidos): 1.000.000 KRW por mês durante 10 anos, começando em cada mês de janeiro de 2000 a julho de 2013 — 163 períodos. Também testamos esperar uma queda de 20%, comprar perto da máxima histórica e investir uma quantia de uma vez ou em 12 meses.\n\nO código do backtest foi escrito por IA e testado contra uma simulação mês a mês e contra viés de antecipação (look-ahead).\nDados: Robert Shiller / FRED via github.com/datasets/s-and-p-500. Taxas, impostos e câmbio não foram incluídos.\nResultados passados não garantem resultados futuros. Este vídeo é educativo e não é recomendação de investimento."
 },
 "es-419": {
  "title": "Comprar en la caída: ¿comprar solo tras bajar 10% del máximo gana más que cada mes? 23 años S&P 500",
  "description": "Los precios parecen demasiado altos, así que guardas efectivo y esperas: \"Compraré cuando baje un 10% desde el máximo.\" ¿Esperar la caída realmente gana más que comprar el mismo día cada mes?\nHicimos un backtest con datos reales del S&P 500 de enero de 2000 a junio de 2023 (dividendos reinvertidos): 1.000.000 KRW al mes durante 10 años, empezando en cada mes de enero de 2000 a julio de 2013 — 163 periodos. También probamos esperar una caída del 20%, comprar cerca del máximo histórico e invertir una suma de una vez o en 12 meses.\n\nEl código del backtest lo escribió una IA y se comprobó con una simulación mes a mes y contra el sesgo de anticipación (look-ahead).\nDatos: Robert Shiller / FRED vía github.com/datasets/s-and-p-500. No incluye comisiones, impuestos ni tipo de cambio.\nLos resultados pasados no garantizan resultados futuros. Este video es educativo y no es asesoría de inversión."
 },
 "ja": {
  "title": "押し目買い：最高値から10%下がった時だけ買うと、毎月買うより儲かる？S&P500の23年バックテスト",
  "description": "株価が上がりすぎた気がして、「最高値から10%下がったら買おう」と現金で待っていませんか？ 下落を待って買う方が、毎月決まった日に買うより本当に儲かるのでしょうか。\n2000年1月〜2023年6月のS&P500の実データ（配当再投資）でバックテストしました。毎月100万ウォンを10年間、開始月を2000年1月から2013年7月まで1か月ずつずらした163通りです。20%の大暴落を待つ場合、最高値付近で買う場合、まとまったお金を一括で入れるか12か月に分けるかも確かめます。\n\nバックテストのコードはAIが書き、1か月ずつのシミュレーションとの一致と、未来の情報を使っていないかを確認しました。\nデータ：Robert Shiller / FRED（github.com/datasets/s-and-p-500）。手数料・税金・為替は含みません。\n過去の結果は将来を保証しません。この動画は教育目的であり、投資助言ではありません。"
 },
 "de": {
  "title": "Buy the Dip: Nur nach 10 % Rückgang vom Hoch kaufen – mehr Gewinn als monatlich? 23 Jahre S&P 500",
  "description": "Die Kurse wirken zu hoch, also halten Sie Bargeld und warten: „Ich kaufe, wenn es 10 % unter dem Hoch steht.“ Bringt das Warten auf den Rücksetzer wirklich mehr als einfach jeden Monat am selben Tag zu kaufen?\nWir haben es mit echten S&P-500-Daten von Januar 2000 bis Juni 2023 (Dividenden reinvestiert) getestet: 1.000.000 KRW pro Monat über 10 Jahre, Start in jedem Monat von Januar 2000 bis Juli 2013 – 163 Zeiträume. Außerdem prüfen wir das Warten auf einen 20-%-Crash, Käufe nahe dem Allzeithoch und eine Einmalanlage gegenüber 12 Monatsraten.\n\nDen Backtest-Code hat eine KI geschrieben; er wurde gegen eine Monat-für-Monat-Simulation und auf Look-ahead-Bias geprüft.\nDaten: Robert Shiller / FRED über github.com/datasets/s-and-p-500. Gebühren, Steuern und Wechselkurse sind nicht enthalten.\nVergangene Ergebnisse garantieren keine zukünftigen Renditen. Dieses Video dient nur der Bildung und ist keine Anlageberatung."
 },
 "vi": {
  "title": "Bắt đáy: chỉ mua khi giảm 10% từ đỉnh có lãi hơn mua đều mỗi tháng? Backtest 23 năm S&P 500",
  "description": "Giá có vẻ quá cao nên bạn giữ tiền mặt và chờ: \"Giảm 10% từ đỉnh thì mình mới mua.\" Chờ giá giảm rồi mua có thật sự lãi hơn mua vào cùng một ngày mỗi tháng không?\nChúng tôi đã backtest bằng dữ liệu thật của S&P 500 từ tháng 1/2000 đến tháng 6/2023 (tái đầu tư cổ tức): 1.000.000 KRW mỗi tháng trong 10 năm, bắt đầu ở từng tháng từ 1/2000 đến 7/2013 — 163 giai đoạn. Chúng tôi cũng thử chờ một đợt sập 20%, mua gần đỉnh lịch sử, và bỏ tiền một lần so với chia 12 tháng.\n\nMã backtest do AI viết và đã được kiểm tra với mô phỏng từng tháng cũng như lỗi dùng dữ liệu tương lai (look-ahead).\nDữ liệu: Robert Shiller / FRED qua github.com/datasets/s-and-p-500. Chưa tính phí, thuế và tỷ giá.\nKết quả quá khứ không đảm bảo tương lai. Video chỉ nhằm mục đích giáo dục, không phải lời khuyên đầu tư."
 },
 "tr": {
  "title": "Düşüşte alım: Zirveden %10 düşünce almak, her ay almaktan daha mı kârlı? 23 yıllık S&P 500 testi",
  "description": "Fiyatlar çok yüksek görünüyor, bu yüzden nakitte bekliyorsunuz: \"Zirveden yüzde 10 düşünce alırım.\" Düşüşü bekleyip almak, her ay aynı gün almaktan gerçekten daha mı kârlı?\nOcak 2000 – Haziran 2023 arasındaki gerçek S&P 500 verileriyle (temettüler yeniden yatırıldı) test ettik: 10 yıl boyunca her ay 1.000.000 KRW, Ocak 2000'den Temmuz 2013'e kadar her ay başlayan 163 dönem. Ayrıca yüzde 20'lik bir çöküşü beklemeyi, tüm zamanların zirvesine yakın almayı ve toplu parayı tek seferde ya da 12 ayda yatırmayı da deniyoruz.\n\nBacktest kodunu yapay zekâ yazdı; ay ay simülasyonla ve geleceğe bakma (look-ahead) hatasına karşı test edildi.\nVeri: Robert Shiller / FRED, github.com/datasets/s-and-p-500 üzerinden. Komisyon, vergi ve kur etkisi dahil değildir.\nGeçmiş sonuçlar gelecekteki getirileri garanti etmez. Bu video yalnızca eğitim amaçlıdır, yatırım tavsiyesi değildir."
 }
}
```

## 6. 고정 댓글

```
A: 매달 정해진 날 매수 / B: 최고점보다 10% 떨어지면 매수 — 영상을 보기 전, 10년 뒤 수익은 어느 쪽이 더 많을 거라고 생각하셨나요?
다음에 백테스트로 검증해 볼 가설도 댓글로 알려 주세요.
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

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과 숫자(117·46·1.2%·25%·898만 등)를 쓰지 않았다. 결과는 영상 결과 파트(문장 38~)에서만.
- 설명란·언어별 설명의 숫자(10%·23년·163번·100만 원·10년·20%)는 대본과 `backtest/results.json`에 있는 것만 썼다 (`checklist.md` 50/50 ✅).
- 한국어 제목 51자 · 언어별 제목 51~100자 (모두 100자 이하) · `< >` 없음 — `tools/youtube_upload.py` `read_sheet`·`validate`로 확인.
- 사다 → 매수, 팔다 → 매도 (사용자 피드백 2026-10-16).

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, **나라·언어별 조회수**(스튜디오 '지역'·'자막·더빙 언어')
