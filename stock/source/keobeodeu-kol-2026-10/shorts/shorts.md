# 쇼츠 — `keobeodeu-kol-2026-10` 결과를 바로 보여 주는 쇼츠 (질문 → 방법 한 줄 → 결과 → 왜? → 롱폼 · 언어 없는 화면)

버전: v2.0 — 2026-10-17 — **꼴 바꿈: 결과를 바로 말한다** (사용자 지시 2026-10-17 "야 주식 쇼츠는 테스트로 호기심 유발, 어떻게 최대한 짧게 설명해서 결과를 바로 말하자 그리고 과정과 결과에 대한 분석으로 더 보고 싶으면 롱폼 영상으로 유도하는걸로하자 일단 하나만 수정해봐"). 프롤로그형(결말은 롱폼에)을 버리고 — 질문 하나(테스트) → 방법은 짧게(티커 한 문장 + 규칙 한 문장) → **결과를 바로**(꺼낸 돈 · QYLD 끝 값 · QQQ 끝 값) → '왜?' → 과정·원인·시작 달은 롱폼으로. 대본 9 → 8문장, 경주는 2026년 끝까지, QQQ 선도 그림. 제목은 2줄에 맞춤(`tools/title_fit.py --shorts`). **주식 쇼츠 네 편 중 이 편만 먼저** (나머지 셋은 사용자가 이 편을 본 뒤).
(v1.0.4 — 2026-10-17 — 쇼츠 썸네일 글자 = 큰 부등호 머리글 `QYLD > QQQ ?` · `−17.5%`. v1.0 — 2026-10-17 — 새로 만듦: 프롤로그형(첫 문장 경주 중간 숫자 → 상황 → 질문 → '아래 영상에서 확인하세요'), 결말 가림 — 커밋 9b8be2b5.)

- 보내는 곳(롱폼): **커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까?** (`../upload.md` 1번 제목) — 쇼츠의 '관련 동영상'으로 연결 (롱폼 공개 뒤)
- **쇼츠에서 말하는 것 (결과):** 2026년까지 꺼낸 돈 약 11만 달러(두 계좌 같음) · QYLD 계좌 약 7만 5천 달러, 원금보다 25.3% 적음 · QQQ 계좌 약 51만 달러, QYLD의 6.83배.
- **롱폼에만 남기는 것 (더 보고 싶은 사람에게):** 날짜별 과정(2014년 3월 +3.4% · 2016년 −17.5% · 코로나 −28.3% · 2022년 하락과 810일 회복) · 원인(오른 날 51.3%만, 떨어진 날 62.7% 따라감 — 커버드콜이 분배금을 만드는 방법) · 시작 달을 바꾼 계좌 94개·118개 · XYLD·JEPI · 세금 15%·다시 매수 · 한계. 쇼츠 끝 문장이 이 셋(과정·원인·시작 달)을 이름으로 부르고, 끝 화면에 그림 셋으로 보여 준다.
- 근거: [`stock/guides/shorts_insights.md`](../../../guides/shorts_insights.md) — 주식 성공 경주 쇼츠(디히치 ×32~×203)는 **끝 결과까지 보여 주는 꼴** → 이번 꼴이 그 근거와 같은 방향 (v1.0 의 '결말 가림'은 근거 없음이었음). 공통 규칙 `guides/shorts_guide.md` 4번(프롤로그형)과는 다르다 — 주식만 (`stock/guides/README.md` 7번).
- 길이: **8문장 · 234음절 · 예상 약 40.9초** (`render.mjs sync --estimate` — 진행자 H04 실측으로 맞춘 추정) · 결과 첫 숫자 약 17초(문장 4), 끝 값 약 21초(문장 5) · 50자 넘는 문장 없음. ⚠️ 비교 집단 성공 비율은 30~44초 14% vs 45~59초 19% (약한 기울기, shorts_insights 2번) — 사용자 지시('최대한 짧게')를 따라 40초대로, 올린 뒤 8번 숫자로 다시 본다.
- 목소리: 진행자 H04 하나 (CLAUDE.md) — 한국어 내레이션, **화면은 소리 없이도 이해되게** (해외 시청자는 자동 더빙·자동 번역)
- 숫자: 쇼츠 대본의 숫자는 모두 롱폼 대본에 있다 — `python3 tools/backtest/shorts_numcheck.py stock keobeodeu-kol-2026-10` → [`checklist.md`](checklist.md) (숫자 12개 · 없음 0). 화면 숫자는 `stock/source/keobeodeu-kol-2026-10/backtest/anim.js` (`a` QYLD · `b` QQQ · `out` 꺼낸 돈 · `ev` 분배금 날)에서만 — 장면 파일이 대본 숫자(25.3% · 6.83 · 11만 · 7만 5천 · 51만 · 2026)와 맞춰 보고 다르면 멈춘다.
- ※ 연구·교육용 — 투자 권유가 아님

## 1. 제목

| | 제목 (한국어 — 기본 언어) | 글자 | 2줄 (`title_fit.py --shorts`) | 까닭 |
|---|---|---|---|---|
| **R1 (추천)** | **커버드콜 10만 달러, 매달 꺼내 쓰면 QQQ보다 남을까?** | 32 | ✅ 홈 Shorts 칸·재생 화면·PC 다음 동영상 모두 2줄 | 금액 '10만 달러' +20%p ⚑ (shorts_insights 3번) · 맨 앞 니즈 낱말 '커버드콜' · 테스트 = 질문 (답은 영상 안에서 바로) |
| R2 | 커버드콜 분배금 매달 꺼내 쓰면, QQQ보다 더 남을까? | 31 | ✅ 모두 2줄 | 쇼츠 첫 문장(질문)과 같은 말 — 금액 없음 |

- 예전 R1 「커버드콜 분배금 매달 꺼내 쓴 10만 달러, QQQ였다면 더 남았을까?」(39자)는 좁은 폰 홈·PC 다음 동영상에서 3줄 → 잘림 (`guides/title_guide.md` v3.1 0번 8 — 사용자 지시 2026-10-17 "모바일, PC 둘다 안 잘리도록").
- 제목은 결과를 말하지 않는다 (테스트로 호기심 — 사용자 지시). 결과는 영상 17~31초에서.
- 쓰지 않은 것: '이유' · '재테크'(0%)·'투자'(3.8%)·'주식투자'(4.7%)·'AI'(6.2%) 낱말 (shorts_insights 3번).

### 1-1. 언어별 제목·설명 (localizations — 롱폼 `upload.md` 5번과 같은 9개 언어)

JSON — 롱폼 업로드 시트와 같은 꼴 (업로드 도구가 읽는 형식). 설명은 한국어 설명란(4번)과 같은 뜻 — 결과까지 말하고, '▶' 줄은 롱폼에만 있는 것(과정·원인·시작 달) + 그 언어의 롱폼 제목. 해시태그는 언어와 상관없는 티커. 숫자 표기는 그 언어 관습(소수점 쉼표 등).

```
{
 "en": {
  "title": "$100K in a covered call, payouts spent monthly: more left than QQQ?",
  "description": "We put $100,000 each into QYLD, a Nasdaq-100 covered call ETF, and QQQ, which follows the Nasdaq-100, in December 2013, and took the same cash out of both accounts every month. By 2026 each had paid out about $110,000. The QYLD account was down to about $75,000, 25.3% below the principal; the QQQ account had about $510,000 left, 6.83 times QYLD.\n▶ How the gap opened, why, and what changes with a different start month — in the related video below: Covered call payouts spent monthly: is more principal left after 13 years than selling QQQ?\n\nData and full conditions (before tax, payout handling, 0.25% fee) are in the main video's description. The code was written by AI and the narration is an AI voice.\nPast data only — not investment advice.\n#QYLD #QQQ"
 },
 "hi": {
  "title": "कवर्ड कॉल में $100K, हर महीने भुगतान खर्च: क्या QQQ से ज़्यादा बचेगा?",
  "description": "दिसंबर 2013 में नैस्डैक-100 कवर्ड कॉल ETF QYLD और नैस्डैक-100 को फॉलो करने वाले QQQ में $100,000-$100,000 लगाए और हर महीने दोनों खातों से बराबर रकम निकाली। 2026 तक दोनों से लगभग $110,000 निकले। QYLD खाते में लगभग $75,000 बचे, मूलधन से 25.3% कम; QQQ खाते में लगभग $510,000 बचे — QYLD के 6.83 गुना।\n▶ फ़र्क कैसे बढ़ा, क्यों, और शुरुआती महीना बदलने पर क्या होता है — नीचे जुड़े वीडियो में: कवर्ड कॉल भुगतान हर महीने खर्च करें तो क्या 13 साल बाद QQQ बेचने से ज़्यादा मूलधन बचेगा?\n\nडेटा और पूरी शर्तें (टैक्स से पहले, भुगतान, 0.25% शुल्क) मुख्य वीडियो के विवरण में हैं। कोड AI ने लिखा और आवाज़ AI की है।\nसिर्फ़ पिछला डेटा — निवेश सलाह नहीं।\n#QYLD #QQQ"
 },
 "id": {
  "title": "$100 ribu di covered call, dividen dipakai tiap bulan: sisa lebih banyak dari QQQ?",
  "description": "Pada Desember 2013 kami menaruh masing-masing $100.000 di QYLD, ETF covered call Nasdaq-100, dan QQQ, yang mengikuti Nasdaq-100, lalu menarik uang yang sama dari kedua akun setiap bulan. Sampai 2026 masing-masing sudah menarik sekitar $110.000. Akun QYLD tinggal sekitar $75.000, 25,3% di bawah modal; akun QQQ masih sekitar $510.000, 6,83 kali QYLD.\n▶ Bagaimana selisihnya melebar, kenapa, dan apa yang berubah jika bulan mulainya diganti — di video tertaut di bawah: Dividen covered call dipakai tiap bulan: apakah modal tersisa lebih banyak dari jual QQQ, 13 tahun?\n\nData dan syarat lengkap (sebelum pajak, pembayaran, biaya 0,25%) ada di deskripsi video utama. Kode ditulis AI dan narasinya suara AI.\nHanya data masa lalu — bukan saran investasi.\n#QYLD #QQQ"
 },
 "pt": {
  "title": "US$ 100 mil em covered call, renda gasta todo mês: sobra mais que no QQQ?",
  "description": "Em dezembro de 2013 colocamos US$ 100.000 no QYLD, um ETF de covered call do Nasdaq-100, e outros US$ 100.000 no QQQ, que segue o Nasdaq-100, e retiramos o mesmo valor das duas contas todo mês. Até 2026 cada uma pagou cerca de US$ 110.000. A conta de QYLD caiu para cerca de US$ 75.000, 25,3% abaixo do capital; a de QQQ ficou com cerca de US$ 510.000, 6,83 vezes o QYLD.\n▶ Como a diferença cresceu, por quê, e o que muda com outro mês de início — no vídeo vinculado abaixo: Renda de covered call gasta todo mês: sobra mais capital em 13 anos do que vendendo QQQ?\n\nDados e condições completas (antes de impostos, pagamentos, taxa de 0,25%) na descrição do vídeo principal. O código foi escrito por IA e a narração é voz de IA.\nApenas dados passados — não é recomendação de investimento.\n#QYLD #QQQ"
 },
 "es-419": {
  "title": "US$100,000 en covered call, gastando cada pago: ¿queda más que en QQQ?",
  "description": "En diciembre de 2013 pusimos US$100,000 en QYLD, un ETF de covered call del Nasdaq-100, y otros US$100,000 en QQQ, que sigue el Nasdaq-100, y retiramos el mismo dinero de ambas cuentas cada mes. Hasta 2026 cada una pagó unos US$110,000. La cuenta de QYLD bajó a unos US$75,000, 25.3% por debajo del capital; a la de QQQ le quedaron unos US$510,000, 6.83 veces QYLD.\n▶ Cómo se abrió la brecha, por qué, y qué cambia con otro mes de inicio — en el video vinculado abajo: Ingreso de covered call gastado cada mes: ¿queda más capital en 13 años que vendiendo QQQ?\n\nDatos y condiciones completas (antes de impuestos, pagos, comisión de 0.25%) en la descripción del video principal. El código lo escribió una IA y la narración es una voz de IA.\nSolo datos pasados — no es asesoría de inversión.\n#QYLD #QQQ"
 },
 "ja": {
  "title": "カバードコールに10万ドル、分配金を毎月使ったら QQQより残る？",
  "description": "2013年12月、ナスダック100のカバードコールETF・QYLDと、ナスダック100に連動するQQQに10万ドルずつ入れ、毎月2つの口座から同じ額を引き出しました。2026年までに引き出した額はどちらも約11万ドル。QYLD口座は約7万5千ドルで元本より25.3%少なく、QQQ口座には約51万ドル、QYLDの6.83倍が残りました。\n▶ 差が開いた過程と原因、始める月を変えた結果は下のリンクの動画で — カバードコールの分配金を毎月使うと、同じ額を売るQQQより13年後に元本は多く残る？\n\nデータと計算条件（税引き前・分配金の扱い・手数料0.25%）は本編の説明欄にあります。計算コードはAIが書き、ナレーションはAI音声です。\n過去データによる計算で、投資の勧誘ではありません。\n#QYLD #QQQ"
 },
 "de": {
  "title": "100.000 $ im Covered Call, Ausschüttung monatlich ausgegeben: mehr übrig als mit QQQ?",
  "description": "Im Dezember 2013 haben wir je 100.000 $ in QYLD, einen Nasdaq-100-Covered-Call-ETF, und in QQQ, der den Nasdaq-100 abbildet, angelegt und jeden Monat aus beiden Konten denselben Betrag entnommen. Bis 2026 wurden aus jedem etwa 110.000 $ entnommen. Das QYLD-Konto lag bei etwa 75.000 $, 25,3 % unter dem Kapital; im QQQ-Konto blieben etwa 510.000 $, das 6,83-Fache von QYLD.\n▶ Wie die Lücke entstand, warum, und was ein anderer Startmonat ändert — im verlinkten Video unten: Covered-Call-Ausschüttung monatlich ausgeben: Bleibt nach 13 Jahren mehr als beim QQQ-Verkauf?\n\nDaten und alle Bedingungen (vor Steuern, Ausschüttungen, 0,25 % Gebühr) in der Beschreibung des Hauptvideos. Der Code wurde von einer KI geschrieben, die Stimme ist eine KI-Stimme.\nNur historische Daten – keine Anlageberatung.\n#QYLD #QQQ"
 },
 "vi": {
  "title": "100.000 USD vào covered call, tiêu cổ tức mỗi tháng: còn nhiều hơn QQQ?",
  "description": "Tháng 12/2013 chúng tôi đặt mỗi bên 100.000 USD vào QYLD, ETF covered call Nasdaq-100, và QQQ, quỹ theo Nasdaq-100, rồi rút cùng một số tiền từ cả hai tài khoản mỗi tháng. Đến năm 2026 mỗi bên đã rút khoảng 110.000 USD. Tài khoản QYLD còn khoảng 75.000 USD, thấp hơn vốn gốc 25,3%; tài khoản QQQ còn khoảng 510.000 USD, gấp 6,83 lần QYLD.\n▶ Khoảng cách lớn dần thế nào, vì sao, và đổi tháng bắt đầu thì ra sao — xem ở video liên kết bên dưới: Tiêu cổ tức covered call mỗi tháng: sau 13 năm vốn còn nhiều hơn bán QQQ cùng số tiền không?\n\nDữ liệu và điều kiện đầy đủ (trước thuế, chi trả, phí 0,25%) trong phần mô tả video chính. Mã do AI viết, lời thuyết minh là giọng AI.\nChỉ là dữ liệu quá khứ — không phải lời khuyên đầu tư.\n#QYLD #QQQ"
 },
 "tr": {
  "title": "Covered call'a 100.000 $, dağıtım her ay harcandı: QQQ'dan fazla kalır mı?",
  "description": "Aralık 2013'te Nasdaq-100 covered call ETF'si QYLD'ye ve Nasdaq-100'ü izleyen QQQ'ya 100.000'er $ yatırdık ve her ay iki hesaptan da aynı parayı çektik. 2026'ya kadar her birinden yaklaşık 110.000 $ çekildi. QYLD hesabı yaklaşık 75.000 $'a, anaparanın %25,3 altına indi; QQQ hesabında ise yaklaşık 510.000 $, QYLD'nin 6,83 katı kaldı.\n▶ Farkın nasıl açıldığı, nedeni ve başlangıç ayı değişince ne olduğu aşağıdaki bağlantılı videoda: Covered call dağıtımını her ay harcarsanız 13 yıl sonra QQQ satmaktan fazla anapara kalır mı?\n\nVeriler ve tüm koşullar (vergi öncesi, ödemeler, %0,25 komisyon) ana videonun açıklamasında. Kodu yapay zekâ yazdı, seslendirme yapay zekâ sesi.\nYalnızca geçmiş veriler — yatırım tavsiyesi değildir.\n#QYLD #QQQ"
 }
}
```

## 2. 대본 (시각은 예상 — 내레이션 뒤 실제 시각으로 맞춤)

| # | 시각 | 대본 | 역할 | 화면 (언어 없음 — 숫자·$·%·×·연도·티커·기호·아이콘) |
|---|---|---|---|---|
| 1 | 0:00 | 커버드콜 QYLD로 분배금을 매달 꺼내 쓰면, QQQ보다 더 남을까요? | **테스트 질문** | **쇼츠 썸네일 그림** (글자 `QYLD > QQQ ?` — 금고에서 금화를 꺼내는 손, 노란 점선 위에 걸친 금고, 천에 덮인 두 번째 계좌) |
| 2 | 0:05 | 나스닥100 커버드콜 ETF인 QYLD와, 나스닥100을 따라가는 ETF인 QQQ예요. | 티커 (짧게) | `NASDAQ 100` · 카드 둘: `QYLD` + 위가 노란 천장에 잘린 선(커버드콜) / `QQQ` + 그대로 오르는 선 |
| 3 | 0:12 | 2013년 12월 10만 달러씩 넣고, 두 계좌에서 매달 같은 돈을 꺼냈어요. | 방법 (한 문장) | 경주 시작 2013.12 · 원금 `$100,000` 노란 점선 · 꺼낸 날마다 **두 선 끝에서 동전이 떨어짐** · 아래 칸: QYLD 값·원금 대비 % / QQQ 값 / 🪙=🪙 → 꺼낸 돈 |
| 4 | 0:17 | 2026년까지 꺼낸 돈은, 둘 다 약 11만 달러였어요. | **결과 ①** | 경주가 2026.10.15 에 닿음 · 꺼낸 돈 칸 `$112,980` 깜빡 |
| 5 | 0:21 | QYLD 계좌에 남은 돈은 약 7만 5천 달러로, 원금보다 25.3% 적어요. | **결과 ②** | QYLD `$74,653` 칸 깜빡 · 원금 아래로 내려간 날 = 빨간 띠 · 끝에 빨간 틈 + 칩 `−25.3%` |
| 6 | 0:27 | QQQ 계좌에는 약 51만 달러, QYLD의 6.83배가 남았습니다. | **결과 ③** | QQQ `$510,215` 칸 깜빡 · QYLD 끝 → QQQ 끝 노란 점선 + 큰 `×6.83` |
| 7 | 0:32 | 같은 돈을 꺼냈는데, 왜 이렇게 차이가 났을까요? | 호기심 (왜?) | 두 선 사이를 노랗게 · 가운데 큰 `?` |
| 8 | 0:36 | 벌어진 과정과 원인, 시작 달을 바꾼 결과는 아래 영상에서 확인하세요. | 롱폼 안내 | 끝 화면: `QYLD` `QQQ` · 그림 셋(날짜별 경주 · ↑↓? · 달력 여럿 ↻ — 말하는 낱말에 하나씩) · `2013 → 2026` · 노란 ⬇ |

- 흐름: ① 테스트 질문 → ② 티커 → ③ 방법 한 문장 → ④⑤⑥ 결과 → ⑦ 왜? → ⑧ 롱폼 (과정·원인·시작 달).
- 롱폼과 같은 색 = 같은 계좌 (주황 QYLD · 파랑 QQQ · 노란 점선 원금 — 주식 쇼츠 0-1 5번).
- 끝인사("시청해주셔서 감사합니다.")는 넣지 않는다 (`guides/shorts_guide.md` 4번).
- 대본 TXT (내레이션용): [`keobeodeu-kol-2026-10-shorts.txt`](keobeodeu-kol-2026-10-shorts.txt)

## 3. 영상 만드는 법 (오디오가 생긴 뒤 — CLAUDE.md '오디오 먼저')

**첫 문장 = 쇼츠 썸네일 그림:** 0초부터 첫 문장(질문)이 끝날 때까지 `thumbnails/thumbnail_1.png`(ChatGPT 가 [`thumbnails/thumbnail_1.md`](thumbnails/thumbnail_1.md) v2.0 으로 만들고 Claude 가 검수해 올림 — 그림 + `QYLD > QQQ ?`)를 화면 가득 (kit.js `K.cover`). 그림에 빈 띠가 있으면 `python3 tools/cover_check.py` 로 재고 `K.cover(…, { box })` (`guides/video_guide.md` v4.13 6번). 그림이 없으면 미리보기는 그림 아이콘 자리, 최종 렌더는 멈춘다.

**모양:** 세로 1080×1920 · 롱폼과 같은 짙은 남색 바탕·색 · **자막 없음**(굽지도 올리지도 않음) · 화면 글자는 언어 없이 (`K.init` `noWords` — `render.mjs check` 가 낱말을 잡음) · 음악 없음 · 음량 -14 LUFS.

**화면 자리 — 가운데·크게 (`guides/video_guide.md` v4.13 6번, `<meta name="video-safe" content="150 60 1320 60">`):** 장면 파일 v2.0 은 화면 좌표를 바로 쓴다 (가운데 x 540 — 예전 v1.0 의 가운데 x 495·위 250 은 '비율 안 맞는 영상'으로 보였음). 글자·그림 x 66~1014 · y 160~1306, 세로 가운데 약 735. 아래 1320~1920 은 비움 (제목·채널·관련 동영상 링크 — 끝 화면 ⬇ 이 이 링크를 가리킨다).

**장면 8개:** ① 썸네일 그림 ② NASDAQ 100 · QYLD(커버드콜) · QQQ ③ 경주 2013.12 → (동전) ④ 2026.10.15 · $112,980 ⑤ $74,653 · 빨간 띠 · −25.3% ⑥ $510,215 · ×6.83 ⑦ 두 선 사이 · ? ⑧ 끝 화면 그림 셋 + ⬇ — 장면 파일 [`video/episodes/keobeodeu-kol-2026-10-shorts/index.html`](../../../../video/episodes/keobeodeu-kol-2026-10-shorts/index.html) v2.0. 장면 시각 = 문장·낱말 시각(손으로 적은 초 없음). 경주 속도 = 문장 3 시작 → 문장 4 '11만'(약 7.4초에 12.8년, `[PACE]` 로그).

**도구:**
1. 내레이션 — `tools/tts_narration.py` 가 롱폼 대본과 함께 `shorts/keobeodeu-kol-2026-10-shorts.txt` 도 읽어 `shorts/narration.mp3`·`shorts/tts_narration.json` 을 만든다 (영상ID `keobeodeu-kol-2026-10-shorts`, Kaggle 셀 범위 `stock` 또는 전체 · 진행자 H04 · `voices/ref/host.wav`).
2. 오디오가 오면:
   ```
   cd video && npm run align-audio -- stock keobeodeu-kol-2026-10-shorts --no-export && cd ..
   node video/render/render.mjs sync  stock keobeodeu-kol-2026-10-shorts
   node video/render/render.mjs check stock keobeodeu-kol-2026-10-shorts
   node video/render/render.mjs video stock keobeodeu-kol-2026-10-shorts
   ```
   → `stock/out/keobeodeu-kol-2026-10-shorts/final_1080p.mp4` (git 에 넣지 않음) → **완성 mp4 장면을 Claude 가 직접 본다** (video_guide v4.13). 지금은 추정 시각의 소리 없는 미리보기 `stock/out/keobeodeu-kol-2026-10-shorts/preview_estimated_silent.mp4` 만 (이 컨테이너에만 — 최종본 아님).
3. 올리기 — 업로드 도구 `tools/youtube_upload.py` v1.10 은 쇼츠 시트 `shorts/upload.md` 를 읽는다 (아직 없음 — 네 편 꼴이 정해지면 만든다). 롱폼과 짝 쇼츠는 같은 시각에 공개 (`guides/upload_guide.md` 12번).

## 4. 설명란 (한국어 — 그대로 복사)

```
나스닥100 커버드콜 ETF QYLD와, 나스닥100을 따라가는 QQQ에 2013년 12월 10만 달러씩 넣고 두 계좌에서 매달 같은 돈을 꺼냈습니다. 2026년까지 꺼낸 돈은 둘 다 약 11만 달러. QYLD 계좌는 약 7만 5천 달러로 원금보다 25.3% 적었고, QQQ 계좌에는 약 51만 달러, QYLD의 6.83배가 남았습니다.
▶ 차이가 벌어진 과정과 원인, 시작 달을 바꾼 결과는 아래 '관련 동영상'에서 — 커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까?

자료·계산 조건(세전, 분배금 처리, 수수료 0.25%)은 본편 설명란에 있습니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
과거 자료로 계산한 결과이며 투자 권유가 아닙니다.
#QYLD #QQQ
```
- 해시태그 2개 `#QYLD #QQQ` — 두 계좌의 티커. 3~5개 쇼츠의 성공 비율이 6.6%로 가장 낮다 (shorts_insights 4번) · 태그 자체의 효과는 근거 없음.
- 결과는 쓰고(영상과 같음), **과정·원인·시작 달은 쓰지 않는다** — 롱폼으로 가는 까닭. 계산 조건 전체는 롱폼 설명란 '실험 방법·재현 조건'에.

## 5. 올리기 설정

| 항목 | 값 |
|---|---|
| 관련 동영상 | **이 롱폼** (`../youtube.json` 의 영상). API 로는 못 건다 → 사용자가 직접: 컴퓨터 스튜디오 → 콘텐츠 → Shorts → 이 쇼츠의 연필(세부정보) → 오른쪽 '관련 동영상' → 이 롱폼 → 저장 (같은 채널·공개된 영상만). 끝 화면 ⬇ 이 그 링크 자리를 가리킴 |
| 썸네일 | `youtube_upload.py` v1.10 이 세로 720×1280 으로 올림 (빈 띠 그림이면 완성 영상 0초 장면). 안 보이면 유튜브 앱 → 쇼츠 수정 → 썸네일 → 0초 장면 |
| 올리는 때 | 롱폼과 **같은 시각에 공개** (`guides/upload_guide.md` 12번 — 할당량이 모자라면 롱폼부터) |
| 기본 언어 | ko |
| 자막 올리기 | **아니요** (전 세계 대상 — 사용자 지시 2026-10-15) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 공개 범위 | 롱폼과 같은 방식 (비공개 업로드 → 예약 공개) |
| 고정 댓글 | 쓰려면 질문 하나: "같은 돈을 꺼냈는데 6.83배 차이, 예상하셨나요? 왜 벌어졌는지는 본편에서 확인하세요." — 근거 없음, 시험 |

## 6. 숫자 근거 (쇼츠 대본의 숫자 → 롱폼 대본 문장)

롱폼 숫자는 `backtest/check_numbers.py` 가 결과 파일로 맞춰 봤다 (전부는 `checklist.md`).

| 쇼츠 문장 | 숫자 | 롱폼 문장 | 롱폼 대본 |
|---:|---|---|---|
| 2 | `100` | s1 | 원금은 잘 안 깎인다는 나스닥100 커버드콜 ETF, QYLD. |
| 3 | `2013년` · `12월` · `10만` | s4 | 2013년 12월, 10만 달러씩 매수해요. |
| 4 | `2026년` | s33 | 2026년 10월 15일, 결과입니다. |
| 4 | `11만` | s34 | 두 계좌가 꺼낸 돈은 똑같이 148번, 약 11만 달러였어요. |
| 5 | `7만` · `5천` · `25.3%` | s35 | QYLD 계좌에 남은 돈은 약 7만 5천 달러로, 원금보다 25.3% 적어요. |
| 6 | `51만` · `6.83배` | s37 | QQQ 계좌에 남은 돈은 약 51만 달러로, 같은 돈을 꺼냈는데 6.83배 많았어요. |

화면 숫자(`$112,980` · `$74,653` · `$510,215` · `×6.83` · `−25.3%`)는 `backtest/results.md` 본 실험 줄과 같다 (QYLD vs QQQ — 꺼낸 돈 합 $112,980 · 분배 ETF 끝 $74,653 · 지수 ETF 끝 $510,215 · ×6.83).

## 7. 주의 — 근거와 다른 점·한계

- **결과를 쇼츠에서 말한다** (사용자 지시 2026-10-17) — 주식 성공 경주 쇼츠(디히치)와 같은 꼴. 쇼츠에서 답을 들은 사람이 롱폼으로 넘어올지는 **근거 없음** → 올린 뒤 '관련 동영상' 클릭 수·롱폼 트래픽 소스 'Shorts 피드'로 본다 (shorts_insights 8번). 롱폼으로 보내는 미끼 = '왜?' + 과정·원인·시작 달 (쇼츠에서 말하지 않음).
- 쇼츠의 결과는 **한 가지 시작 날(2013년 12월)·세전** 결과다. 시작 달을 바꾼 결과·세금은 롱폼에 — 쇼츠 끝 문장과 설명란이 그 둘을 가리킨다.
- 40초대 — 비교 집단에서 45~59초보다 성공 비율이 조금 낮은 구간 (약한 기울기).
- 대본(자막·음성인식)이 있는 성공 쇼츠가 0개라 첫 3초·말 속도·끝 문장은 근거 없음 — 롱폼 말투를 그대로 썼다.
- 언어 없는 화면이 해외에서 통하는지는 올린 뒤 시청자 지리로 본다.

## 8. 다음에 할 일

1. 사용자가 소리 없는 미리보기를 보고 이 꼴을 확인 → 나머지 세 편(①③④)을 같은 꼴로.
2. 썸네일 그림(ChatGPT — `stock/thumbnails_chatgpt.md`) → Claude 검수·업로드.
3. 쇼츠 업로드 시트 `shorts/upload.md` (업로드 도구 v1.10 꼴) — 네 편 꼴이 정해지면.
4. Kaggle 셀(범위 `stock`)로 내레이션 → 3번 '도구' 2 (맞춤·sync·check·video·완성 영상 보기) → 롱폼과 같은 시각에 올리기 → 5번 관련 동영상을 사용자가 건다.

## 변경 이력

| 버전 | 날짜 | 내용 |
|---|---|---|
| v2.0 | 2026-10-17 | 꼴 바꿈 — 결과를 바로 말함 (질문 → 티커 → 방법 한 문장 → 결과 셋 → 왜? → 롱폼): 대본 8문장 234음절 예상 약 40.9초 · 제목 R1 「커버드콜 10만 달러, 매달 꺼내 쓰면 QQQ보다 남을까?」(2줄) · 9개 언어 제목·설명 다시 · 장면 v2.0 (가운데·크게, 경주 2026년 끝까지, QQQ 선) · 썸네일 v2.0 (`QYLD > QQQ ?`만) · 숫자 12개 없음 0 (사용자 지시 "야 주식 쇼츠는 테스트로 호기심 유발, 어떻게 최대한 짧게 설명해서 결과를 바로 말하자 그리고 과정과 결과에 대한 분석으로 더 보고 싶으면 롱폼 영상으로 유도하는걸로하자 일단 하나만 수정해봐") |
| v1.0.4 | 2026-10-17 | 쇼츠 썸네일 글자 `QYLD > QQQ ?` · `−17.5%` — 큰 부등호 머리글 (사용자 지시) |
| v1.0.3 | 2026-10-17 | 쇼츠 썸네일 글자 `−17.5%` · `QYLD` · `?` — 딱 봤을 때 이해되는 것만 (사용자 지시) |
| v1.0.2 | 2026-10-17 | 쇼츠 썸네일 글자 `QYLD < $100,000` · `−17.5%` · `QQQ = ?` — 비교·수식 기호 (사용자 지시) |
| v1.0.1 | 2026-10-17 | 쇼츠 썸네일 글자 `−17.5%` · `QYLD` · `$100,000` · `?` (사용자 지시 — 영어·숫자·기호 써도 됨) |
| v1.0 | 2026-10-17 | 새로 만듦 — 대본 9문장 257음절 예상 약 44.5초 · 제목 R1 「커버드콜 분배금 매달 꺼내 쓴 10만 달러, QQQ였다면 더 남았을까?」 · 9개 언어 제목·설명 · 언어 없는 세로 장면 v1.0 · 숫자 근거 17개 (없음 0) |
