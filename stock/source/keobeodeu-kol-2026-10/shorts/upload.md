# keobeodeu-kol-2026-10-shorts 업로드 시트 (주식 쇼츠)

버전: v1.2 — 2026-10-18 — 설명란 = 첫 설명(간단히) + 롱폼 안내 + 자료 + 알려 드립니다, 각 아래 영어 · 롱폼 제목을 새 2줄 제목으로 · 태그에 영어 더함 · 그 밖은 원래대로 (사용자 지시 2026-10-18 "설명에 맨처음 설명(최대한 간단하게) 챕터, 자료, 알려 드립니다 만 남기고 나머지는 지워 그리고 각 밑 부분에 영어로 번역해서 쓰고 챕터는 각각 챕터 옆에 괄호 안에 영어로 번역해서 넣어 그렇게 수정하고 태그에 영어도 포함해 그리고 나머지는 원래대로 돌리자" · "한국어 제목 잘리잖아 안질리도록 영상 제목 다시 수정해봐").
(v1.1 — 2026-10-18 — 기본 언어 en 판은 되돌림)
(v1.0 — 2026-10-18 — 새로 만듦: `shorts.md` v2.1.1 의 제목 R1 · 설명란(4번) · 언어별 제목·설명(1-1)을 업로드 도구가 읽는 꼴로 옮김 · 자막 언어별 (사용자 지시 2026-10-18 "채권 표현 수정하고 영상 업로드 할 준비해").)

기준 파일: 쇼츠 대본 `keobeodeu-kol-2026-10-shorts.txt` (12문장) · SRT 문장 12 / 자막 15 (`align-audio` 로 오디오에 맞춤) · 오디오 `narration.mp3` 62.3초 · 올릴 영상 = `stock/out/keobeodeu-kol-2026-10-shorts/final_1080p.mp4` (이 클라우드 컨테이너에만 — git 에 넣지 않음, 장면 파일·오디오로 다시 만듦)

> 업로드: `python3 tools/youtube_upload.py stock keobeodeu-kol-2026-10-shorts --dry-run` → `--publish-at <시각>` (비공개로 올리고 그 시각에 공개). 롱폼 `keobeodeu-kol-2026-10` 과 **같은 시각에 공개** (`guides/upload_guide.md` 12번). 자막은 한국어 + 9개 언어 = 10개(4,000단위) — 할당량이 모자라면 남은 언어는 `--captions-only` 로 다음 날.
> ※ 연구·교육용 — 투자 권유가 아님.

## 1. 제목 (`shorts.md` R1, `title_fit.py --shorts` 2줄 안)

```
커버드콜 10만 달러, 분배금 매달 써도 원금 지켜질까?
```

## 2. 설명란 (첫 설명 · 롱폼 안내 · 자료 · 알려 드립니다 — 각 아래 영어)

```
QYLD(커버드콜)와 QQQ에 10만 달러씩 넣고, 매달 같은 날 같은 금액을 꺼내며 AI가 짠 파이썬 코드로 백테스트했습니다(2013년 12월부터). 2026년, QYLD 계좌는 약 7만 5천 달러로 원금보다 25.3% 적었고, QQQ 계좌에는 약 51만 달러, QYLD의 6.83배가 남았어요.
We put $100,000 each in QYLD (covered call) and QQQ, took out the same amount on the same days every month, and backtested it with AI-written Python code (from Dec 2013). By 2026, QYLD had about $75,000 left, 25.3% below the principal; QQQ had about $510,000, 6.83× QYLD.
▶ 그 이유와, 다른 달에 시작해도 결과가 같은지는 아래 '관련 동영상'에서 — 커버드콜 분배금, 매달 꺼내 써도 QQQ보다 더 남을까?
▶ Why, and other start months: see the related video below — Covered call payouts spent monthly: is more principal left after 13 years than selling QQQ?

■ 자료 (Data)
일별 종가·분배금: Yahoo Finance 차트 API
Daily close & payouts: Yahoo Finance chart API

■ 알려 드립니다 (Notice)
과거 자료로 계산한 결과이며 투자 권유가 아닙니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
Results from past data. Not investment advice. The code was written by AI and the narration is an AI voice.
#QYLD #QQQ
```

## 3. 언어별 제목·설명 (`shorts.md` 1-1 그대로 — 9개 언어, 업로드 도구 v1.6 localizations)

```
{
 "en": {
  "title": "$100K in a covered call: spend the payouts monthly, is the principal safe?",
  "description": "People say a covered call ETF keeps your principal even if you spend its monthly payouts. To check, we ran a backtest with AI-written Python code on real past prices. We tested QYLD, a Nasdaq-100 covered call ETF, against QQQ, which follows the Nasdaq-100 without covered calls. In December 2013 each account got $100,000 of principal. QYLD's payouts were spent every time they came; to keep it fair, the QQQ account sold the same amount on the same days. By 2026 each had paid out about $110,000. The QYLD account was down to about $75,000, 25.3% below the principal; the QQQ account had about $510,000 left, 6.83 times QYLD.\n▶ Why — and whether a different start month gives the same result — in the related video below: Covered call payouts spent monthly: is more principal left after 13 years than selling QQQ?\n\nData and full conditions (before tax, payout handling, 0.25% fee) are in the main video's description. The code was written by AI and the narration is an AI voice.\nPast data only — not investment advice.\n#QYLD #QQQ"
 },
 "hi": {
  "title": "कवर्ड कॉल में $100K: हर महीने भुगतान खर्च करें, क्या मूलधन बचेगा?",
  "description": "कहा जाता है कि कवर्ड कॉल ETF का मासिक भुगतान खर्च करने पर भी मूलधन ज़्यादा नहीं घटता। यह जाँचने के लिए हमने AI के लिखे Python कोड से पिछली असली कीमतों पर बैकटेस्ट किया। नैस्डैक-100 कवर्ड कॉल ETF QYLD की तुलना QQQ से की, जो बिना कवर्ड कॉल के नैस्डैक-100 को फॉलो करता है। दिसंबर 2013 में दोनों खातों में $100,000 मूलधन डाला। QYLD का हर भुगतान आते ही खर्च किया; बराबरी के लिए QQQ से उन्हीं दिनों उतनी ही रकम बेचकर निकाली। 2026 तक दोनों से लगभग $110,000 निकले। QYLD खाते में लगभग $75,000 बचे, मूलधन से 25.3% कम; QQQ खाते में लगभग $510,000 बचे — QYLD के 6.83 गुना।\n▶ ऐसा क्यों हुआ, और दूसरे महीने से शुरू करने पर भी नतीजा वही रहता है या नहीं — नीचे जुड़े वीडियो में: कवर्ड कॉल भुगतान हर महीने खर्च करें तो क्या 13 साल बाद QQQ बेचने से ज़्यादा मूलधन बचेगा?\n\nडेटा और पूरी शर्तें (टैक्स से पहले, भुगतान, 0.25% शुल्क) मुख्य वीडियो के विवरण में हैं। कोड AI ने लिखा और आवाज़ AI की है।\nसिर्फ़ पिछला डेटा — निवेश सलाह नहीं।\n#QYLD #QQQ"
 },
 "id": {
  "title": "$100 ribu di covered call: dividen dipakai tiap bulan, modal aman?",
  "description": "Katanya ETF covered call tidak banyak menggerus modal walau pembayaran bulanannya dipakai. Untuk mengeceknya, kami melakukan backtest dengan kode Python buatan AI pada harga riil masa lalu. QYLD, ETF covered call Nasdaq-100, kami bandingkan dengan QQQ, yang mengikuti Nasdaq-100 tanpa covered call. Pada Desember 2013 masing-masing akun diisi modal $100.000. Setiap pembayaran QYLD langsung dipakai; agar adil, akun QQQ menjual jumlah yang sama pada hari yang sama. Sampai 2026 masing-masing sudah menarik sekitar $110.000. Akun QYLD tinggal sekitar $75.000, 25,3% di bawah modal; akun QQQ masih sekitar $510.000, 6,83 kali QYLD.\n▶ Kenapa begitu, dan apakah hasilnya sama jika mulai di bulan lain — di video tertaut di bawah: Dividen covered call dipakai tiap bulan: apakah modal tersisa lebih banyak dari jual QQQ, 13 tahun?\n\nData dan syarat lengkap (sebelum pajak, pembayaran, biaya 0,25%) ada di deskripsi video utama. Kode ditulis AI dan narasinya suara AI.\nHanya data masa lalu — bukan saran investasi.\n#QYLD #QQQ"
 },
 "pt": {
  "title": "US$ 100 mil em covered call: gastando a renda todo mês, o capital se mantém?",
  "description": "Dizem que um ETF de covered call preserva o capital mesmo gastando a renda mensal. Para conferir, fizemos um backtest com código Python escrito por IA sobre preços reais do passado. Comparamos o QYLD, ETF de covered call do Nasdaq-100, com o QQQ, que segue o Nasdaq-100 sem covered call. Em dezembro de 2013 cada conta recebeu US$ 100.000 de capital. A renda do QYLD foi gasta toda vez que saiu; para ser justo, a conta de QQQ vendeu o mesmo valor nos mesmos dias. Até 2026 cada uma pagou cerca de US$ 110.000. A conta de QYLD caiu para cerca de US$ 75.000, 25,3% abaixo do capital; a de QQQ ficou com cerca de US$ 510.000, 6,83 vezes o QYLD.\n▶ Por que isso aconteceu, e se o resultado é o mesmo começando em outro mês — no vídeo vinculado abaixo: Renda de covered call gasta todo mês: sobra mais capital em 13 anos do que vendendo QQQ?\n\nDados e condições completas (antes de impostos, pagamentos, taxa de 0,25%) na descrição do vídeo principal. O código foi escrito por IA e a narração é voz de IA.\nApenas dados passados — não é recomendação de investimento.\n#QYLD #QQQ"
 },
 "es-419": {
  "title": "US$100,000 en covered call: gastando cada pago, ¿se conserva el capital?",
  "description": "Se dice que un ETF de covered call conserva el capital aunque gastes sus pagos mensuales. Para comprobarlo, hicimos un backtest con código Python escrito por IA sobre precios reales del pasado. Comparamos QYLD, un ETF de covered call del Nasdaq-100, con QQQ, que sigue el Nasdaq-100 sin covered call. En diciembre de 2013 cada cuenta recibió US$100,000 de capital. Cada pago de QYLD se gastó apenas llegó; para que fuera justo, la cuenta de QQQ vendió el mismo monto los mismos días. Hasta 2026 cada una pagó unos US$110,000. La cuenta de QYLD bajó a unos US$75,000, 25.3% por debajo del capital; a la de QQQ le quedaron unos US$510,000, 6.83 veces QYLD.\n▶ Por qué pasó, y si el resultado es el mismo empezando en otro mes — en el video vinculado abajo: Ingreso de covered call gastado cada mes: ¿queda más capital en 13 años que vendiendo QQQ?\n\nDatos y condiciones completas (antes de impuestos, pagos, comisión de 0.25%) en la descripción del video principal. El código lo escribió una IA y la narración es una voz de IA.\nSolo datos pasados — no es asesoría de inversión.\n#QYLD #QQQ"
 },
 "ja": {
  "title": "カバードコールに10万ドル、分配金を毎月使っても元本は守られる？",
  "description": "カバードコールETFは、毎月の分配金を使っても元本があまり減らないと言われます。本当かどうか、AIが書いたPythonコードで過去の実際の価格を使ってバックテストしました。ナスダック100のカバードコールETF・QYLDを、カバードコールなしでナスダック100にそのまま連動するQQQと比べました。2013年12月、2つの口座に元本10万ドルずつ。QYLDは分配金が出るたびに全部使い、公平になるようQQQからも同じ日に同じ額を売って引き出しました。2026年までに引き出した額はどちらも約11万ドル。QYLD口座は約7万5千ドルで元本より25.3%少なく、QQQ口座には約51万ドル、QYLDの6.83倍が残りました。\n▶ その理由と、別の月に始めても結果が同じかどうかは下のリンクの動画で — カバードコールの分配金を毎月使うと、同じ額を売るQQQより13年後に元本は多く残る？\n\nデータと計算条件（税引き前・分配金の扱い・手数料0.25%）は本編の説明欄にあります。計算コードはAIが書き、ナレーションはAI音声です。\n過去データによる計算で、投資の勧誘ではありません。\n#QYLD #QQQ"
 },
 "de": {
  "title": "100.000 $ im Covered Call: Ausschüttung monatlich ausgeben – bleibt das Kapital?",
  "description": "Es heißt, ein Covered-Call-ETF erhält das Kapital, auch wenn man die monatlichen Ausschüttungen ausgibt. Zur Prüfung haben wir mit von KI geschriebenem Python-Code einen Backtest auf echten historischen Kursen gemacht. Verglichen wurde QYLD, ein Nasdaq-100-Covered-Call-ETF, mit QQQ, der den Nasdaq-100 ohne Covered Calls abbildet. Im Dezember 2013 bekam jedes Konto 100.000 $ Kapital. Jede QYLD-Ausschüttung wurde sofort ausgegeben; damit es fair ist, verkaufte das QQQ-Konto an denselben Tagen denselben Betrag. Bis 2026 wurden aus jedem etwa 110.000 $ entnommen. Das QYLD-Konto lag bei etwa 75.000 $, 25,3 % unter dem Kapital; im QQQ-Konto blieben etwa 510.000 $, das 6,83-Fache von QYLD.\n▶ Warum – und ob ein anderer Startmonat zum gleichen Ergebnis führt – im verlinkten Video unten: Covered-Call-Ausschüttung monatlich ausgeben: Bleibt nach 13 Jahren mehr als beim QQQ-Verkauf?\n\nDaten und alle Bedingungen (vor Steuern, Ausschüttungen, 0,25 % Gebühr) in der Beschreibung des Hauptvideos. Der Code wurde von einer KI geschrieben, die Stimme ist eine KI-Stimme.\nNur historische Daten – keine Anlageberatung.\n#QYLD #QQQ"
 },
 "vi": {
  "title": "100.000 USD vào covered call: tiêu cổ tức mỗi tháng, vốn gốc có giữ được?",
  "description": "Người ta nói ETF covered call giữ được vốn gốc dù tiêu khoản chi trả hằng tháng. Để kiểm tra, chúng tôi chạy backtest bằng mã Python do AI viết trên giá thực tế trong quá khứ. Chúng tôi so sánh QYLD, ETF covered call Nasdaq-100, với QQQ, quỹ theo Nasdaq-100 mà không dùng covered call. Tháng 12/2013 mỗi tài khoản có 100.000 USD vốn gốc. Mỗi khoản chi trả của QYLD được tiêu ngay; để công bằng, tài khoản QQQ bán cùng số tiền vào cùng ngày. Đến năm 2026 mỗi bên đã rút khoảng 110.000 USD. Tài khoản QYLD còn khoảng 75.000 USD, thấp hơn vốn gốc 25,3%; tài khoản QQQ còn khoảng 510.000 USD, gấp 6,83 lần QYLD.\n▶ Vì sao, và nếu bắt đầu vào tháng khác thì kết quả có giống không — xem ở video liên kết bên dưới: Tiêu cổ tức covered call mỗi tháng: sau 13 năm vốn còn nhiều hơn bán QQQ cùng số tiền không?\n\nDữ liệu và điều kiện đầy đủ (trước thuế, chi trả, phí 0,25%) trong phần mô tả video chính. Mã do AI viết, lời thuyết minh là giọng AI.\nChỉ là dữ liệu quá khứ — không phải lời khuyên đầu tư.\n#QYLD #QQQ"
 },
 "tr": {
  "title": "Covered call'a 100.000 $: dağıtımı her ay harcarsanız anapara korunur mu?",
  "description": "Covered call ETF'lerinin aylık ödemeleri harcasanız bile anaparayı pek eritmediği söylenir. Bunu kontrol etmek için yapay zekânın yazdığı Python koduyla geçmişteki gerçek fiyatlar üzerinde backtest yaptık. Nasdaq-100 covered call ETF'si QYLD'yi, Nasdaq-100'ü covered call olmadan izleyen QQQ ile karşılaştırdık. Aralık 2013'te her hesaba 100.000 $ anapara koyduk. QYLD'nin her ödemesi gelir gelmez harcandı; adil olsun diye QQQ hesabı aynı günlerde aynı tutarı sattı. 2026'ya kadar her birinden yaklaşık 110.000 $ çekildi. QYLD hesabı yaklaşık 75.000 $'a, anaparanın %25,3 altına indi; QQQ hesabında ise yaklaşık 510.000 $, QYLD'nin 6,83 katı kaldı.\n▶ Nedeni ve başka bir ayda başlayınca sonucun aynı olup olmadığı aşağıdaki bağlantılı videoda: Covered call dağıtımını her ay harcarsanız 13 yıl sonra QQQ satmaktan fazla anapara kalır mı?\n\nVeriler ve tüm koşullar (vergi öncesi, ödemeler, %0,25 komisyon) ana videonun açıklamasında. Kodu yapay zekâ yazdı, seslendirme yapay zekâ sesi.\nYalnızca geçmiş veriler — yatırım tavsiyesi değildir.\n#QYLD #QQQ"
 }
}
```

## 4. 태그 (한국어 + 영어)

```
QYLD, QQQ, 커버드콜, 커버드콜 ETF, 분배금, 원금, 나스닥100, 백테스트, covered call, backtest, covered call ETF, monthly dividend, Nasdaq 100, investing, Shorts
```

## 6. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 범위 | 비공개로 올리고 예약 시각에 공개 (`--publish-at`) — 롱폼과 같은 시각 |
| 기본 언어 | ko |
| 자막 올리기 | **언어별** (한국어 `keobeodeu-kol-2026-10-shorts.srt` + `subs/keobeodeu-kol-2026-10-shorts.<언어>.srt` 9개 — 화면에는 굽지 않음, `stock/guides/README.md` v1.24 4번) |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 썸네일 | `thumbnails/thumbnail_1.png` (세로 9:16 — 그림이 화면 끝까지) → 도구가 세로 720×1280 JPG 로 올림 · 0초 장면도 같은 그림 · 공개 뒤 `i.ytimg.com/vi/<ID>/oardefault.jpg` 로 확인 |
| 관련 동영상 | 롱폼 `keobeodeu-kol-2026-10` 「커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까?」 (`../youtube.json`) — 스튜디오 → 콘텐츠 → Shorts → 연필 → '관련 동영상' (API 로 못 검 — 사용자가 직접) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |

## 7. 결과 (업로드 후)
- (올린 뒤 `youtube.json` 의 영상 ID·예약 시각·자막 언어를 적는다)
