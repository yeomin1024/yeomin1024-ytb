# ppalli-test-2026-11-shorts 업로드 시트 (주식 쇼츠)

버전: v1.5 — 2026-11-05 — 외국어 설정 (사용자 지시 "외국어 자막, 제목, 썸네일 등 외국어 설정에 필요한 것들 생성하고 지시사항에 반영해 이건 영상이 렌더까지 완료되면 하는거야"): 6번 언어별 제목·설명 9개 언어(en·hi·id·pt·es-419·ja·de·vi·tr — 2번 그대로 옮김, ▶ 줄의 롱폼 제목도 그 언어 제목) · 자막 = 한국어 + 언어별 SRT 9개 (`subs/`, `tools/subs_tool.py` build) · 업로드 설정에 기본 언어 ko · 자막 올리기 언어별 · 썸네일은 한국어 하나 그대로(세 칸 band — 영상 0초 장면) · 섹션 번호 6→7·7→8.
이전 v1.4 — 2026-11-05 — 쇼츠 설명란은 원래 꼴로 되돌림 (사용자 지시 "쇼츠는 다시 원래했던 설명으로 지시사항 수정하고 다시 설명 보여줘" — 규칙 45 는 롱폼만) · 태그는 늘린 것 그대로.
이전 v1.3 — 2026-11-05 — 설명란 줄임·태그 늘림 (사용자 지시 "김씨는 실제 숫자로 만든 가상의 인물입니다. 내레이션은 AI 음성이고, 그림은 AI로 만든 연출입니다. 다섯 가지 선택, 계산기준빼고 태그도 더 추가 하는걸로 설명 만들자 지시사항에도 반영해" — `stock/guides/quick_board.md` 규칙 45): '다섯 가지 선택'·'계산 기준'·'○씨는 가상의 인물'·'AI 음성/그림' 줄 뺌 · 태그 20개(편 낱말 + 실제 영상 태그 `stock/tag_candidates.md`).
이전 v1.2 — 2026-11-05 — 설명란을 면세 쇼츠 꼴로 자세히 ('이 생각' 풀이 · 롱폼 안내 · '99%' 강조 표현 안내 · AI 음성·그림 · 해시태그 2개 — 사용자 "영상 설명 좀 면세 영상 올릴 때 처럼 자세하게") · 고정 댓글 칸 더함.
이전 v1.1 — 2026-11-05 — 완성 영상을 저장소에 둠 `stock/videos/ppalli-test-2026-11-shorts.mp4` (사용자 지시 "그냥 깃허브에 올려 1편 영상들") → 새 세션은 다시 렌더 없이 `python3 tools/youtube_upload.py stock ppalli-test-2026-11-shorts --video stock/videos/ppalli-test-2026-11-shorts.mp4 --publish-at 2026-11-12T08:00:00Z`.
이전 v1.0 — 2026-11-04 — 새로 만듦 (사용자 지시 "1편은 각각 일주일 후로 자동 예약 걸어서 업로드 해") · 제목 = 사용자 쇼츠 제목 그대로 (`stock/topics/쇼츠안_2026-10-30.md` 1편 — 사용자 결정 2026-11-02 「1편 쇼츠는 이미 있는 내용으로」) · 설명란 = 짧은 설명 + 롱폼 안내 + 알려 드립니다 + 해시태그 2개 · 한국어만 (롱폼 시트와 같음).

기준 파일: 쇼츠 대본 `ppalli-test-2026-11-shorts.txt` (11문장) · SRT `ppalli-test-2026-11-shorts.srt` (오디오에 맞춤) · 올릴 영상 = `stock/out/ppalli-test-2026-11-shorts/final_1080p.mp4` (이 클라우드 컨테이너에만 — git 에 넣지 않음, 장면 파일·오디오로 다시 만듦)

> 업로드: `python3 tools/youtube_upload.py stock ppalli-test-2026-11-shorts --dry-run` → `--publish-at 2026-11-12T08:00:00Z` (비공개로 올리고 그 시각에 공개 — 한국 시각 11월 12일 오후 5시). 롱폼 `ppalli-test-2026-11` 과 **같은 시각에 공개** (`guides/upload_guide.md` 12번). 관련 동영상 = 그 롱폼 (사용자가 스튜디오에서).
> ※ 연구·교육용 — 투자 권유가 아님.

## 1. 제목 (사용자 쇼츠 제목 그대로)

```
'이 생각'으로 주식 투자를 하면 당신은 99% 손해 봅니다.
```

- `title_fit.py --shorts`: 쇼츠 재생 화면·PC 다음 동영상 2줄 ✅ · 홈 Shorts 칸(좁은 폰) 3줄 ❌ — 사용자 제목이라 그대로 (2026-11-02 점검에서 알고 둠). '99%'는 계산한 숫자가 아님 (쇼츠안 1편 점검 — 알고 그대로).

## 2. 설명란 (그대로 복사)

```
'이 생각'은 바로, 주식으로 돈을 빨리 벌고 싶다는 생각입니다.
수익이 나면 매수 금액을 점점 늘리고, 손실이 나면 빨리 되찾으려고 더 자주, 더 크게 사고팔게 됩니다. 그러다 큰 하락이 오면 더 살 돈도, 팔 여유도 남지 않습니다.
▶ 김씨가 마주한 다섯 번의 갈림길에서 당신은 어떤 선택을 할지, 테스트 전체는 아래 '관련 동영상'에서 — 주식 투자 실패하는 사람들은 절대 통과 못하는 테스트

※ 제목의 '99%'는 계산한 숫자가 아니라, 그만큼 손해 보기 쉽다는 강조 표현입니다.
과거 자료로 만든 연구·교육용 영상이며, 투자 권유가 아닙니다. 내레이션은 AI 음성이고, 그림은 AI로 만든 연출입니다.
#주식 #주식테스트
```

## 3. 챕터

```
```

- 쇼츠는 챕터 없음.

## 4. 태그

```
주식 테스트, 주식 투자 습관, 투자 실패, 리스크 관리, 분산투자, 하락장, 주식, 주식투자, 미국주식, 주식초보, 주린이, 주식공부, 주식기초, 투자공부, 투자마인드, 개미투자자, 초보투자자, 장기투자, S&P500, 주식하는법
```

## 5. 고정 댓글 (공개 뒤 사용자가 달고 '고정' — 쇼츠 댓글 링크는 눌리지 않음)

```
당신의 '이 생각'은 몇 퍼센트인가요? 다섯 가지 선택 테스트는 본편에서 확인하세요 👉 「주식 투자 실패하는 사람들은 절대 통과 못하는 테스트」
```

## 6. 언어별 제목·설명 (9개 언어 en·hi·id·pt·es-419·ja·de·vi·tr — 업로드 도구 localizations · 기본 언어 ko 는 1·2번)

```json
{
 "en": {
  "title": "Invest in stocks with 'this thought' and you're 99% sure to lose.",
  "description": "'This thought' is the wish to make money fast with stocks.\nWhen you profit, you keep raising how much you buy; when you lose, you trade more often and bigger to win it back fast. Then when a big drop comes, there's no money left to buy more and no room to sell.\n▶ What would you choose at the five crossroads Mr. Kim faced? The full test is in the related video below: The Test People Who Fail at Stock Investing Can Never Pass\n\n※ The '99%' in the title is not a calculated figure; it's an emphasis on how easy it is to lose.\nA research and educational video made from past data, not investment advice. The narration is an AI voice, and the images are AI-generated illustrations.\n#Stocks #StockTest"
 },
 "hi": {
  "title": "'इस सोच' के साथ शेयरों में निवेश किया, तो 99% नुकसान तय है।",
  "description": "'इस सोच' का मतलब है, शेयरों से जल्दी पैसा कमाने की चाह।\nमुनाफ़ा हो तो ख़रीद की रक़म बढ़ाते जाते हैं, और घाटा हो तो जल्दी भरपाई के लिए और बार-बार, और बड़े सौदे करते हैं। फिर बड़ी गिरावट आती है, तो न और ख़रीदने का पैसा बचता है, न बेचने की गुंजाइश।\n▶ मिस्टर किम के सामने आए पाँच मोड़ों पर आप क्या चुनते? पूरा टेस्ट नीचे जुड़े वीडियो में: शेयर निवेश में नाकाम लोग यह टेस्ट कभी पास नहीं कर पाते\n\n※ टाइटल का '99%' कोई गिना हुआ आँकड़ा नहीं, बल्कि इस पर ज़ोर है कि नुकसान कितनी आसानी से होता है।\nयह पुराने आँकड़ों पर बना रिसर्च और शिक्षा का वीडियो है, निवेश की सलाह नहीं। आवाज़ AI की है, और तस्वीरें AI से बनाई गई हैं।\n#शेयर #शेयरटेस्ट"
 },
 "id": {
  "title": "Investasi saham dengan 'pikiran ini', 99% Anda pasti rugi.",
  "description": "'Pikiran ini' adalah keinginan cepat dapat uang dari saham.\nSaat untung, jumlah beli terus dinaikkan; saat rugi, jual-beli makin sering dan makin besar demi cepat balik modal. Lalu saat penurunan besar datang, tak ada lagi uang untuk membeli dan tak ada ruang untuk menjual.\n▶ Apa pilihan Anda di lima persimpangan yang dihadapi Pak Kim? Tes lengkapnya ada di video terkait di bawah: Tes yang Tidak Akan Pernah Bisa Dilewati Orang yang Gagal Investasi Saham\n\n※ Angka '99%' di judul bukan hasil hitungan, melainkan penekanan betapa mudahnya rugi.\nVideo riset dan edukasi dari data masa lalu, bukan ajakan investasi. Narasinya suara AI, dan gambarnya ilustrasi buatan AI.\n#Saham #TesSaham"
 },
 "pt": {
  "title": "Se você investir em ações com 'esse pensamento', tem 99% de chance de perder.",
  "description": "'Esse pensamento' é a vontade de ganhar dinheiro rápido com ações.\nQuando lucra, você aumenta o valor das compras; quando perde, compra e vende cada vez mais e em valores maiores para recuperar rápido. Aí, quando vem uma grande queda, não sobra dinheiro para comprar nem margem para vender.\n▶ O que você escolheria nas cinco encruzilhadas que o Sr. Kim enfrentou? O teste completo está no vídeo relacionado abaixo: O teste em que quem fracassa com ações nunca passa\n\n※ O '99%' do título não é um número calculado, e sim uma ênfase em como é fácil perder.\nVídeo de pesquisa e educação feito com dados passados, não é recomendação de investimento. A narração é voz de IA, e as imagens são ilustrações criadas por IA.\n#Ações #TesteDeAções"
 },
 "es-419": {
  "title": "Si inviertes en acciones con 'este pensamiento', tienes un 99% de probabilidad de perder.",
  "description": "'Este pensamiento' es el deseo de ganar dinero rápido con acciones.\nSi ganas, aumentas el monto de tus compras; si pierdes, compras y vendes cada vez más seguido y en montos más grandes para recuperarlo rápido. Y cuando llega una gran caída, no te queda dinero para comprar ni margen para vender.\n▶ ¿Qué elegirías en las cinco encrucijadas que enfrentó el señor Kim? La prueba completa está en el video relacionado abajo: La prueba que quienes fracasan en la bolsa nunca logran pasar\n\n※ El '99%' del título no es una cifra calculada, sino un énfasis en lo fácil que es perder.\nVideo de investigación y educación hecho con datos pasados; no es asesoría de inversión. La narración es una voz de IA y las imágenes son ilustraciones creadas con IA.\n#Acciones #PruebaDeAcciones"
 },
 "ja": {
  "title": "「この考え」で株式投資をすると、あなたは99%損をします。",
  "description": "「この考え」とは、株で早くお金を稼ぎたいという考えです。\n利益が出ると買う金額をどんどん増やし、損失が出ると早く取り戻そうと、もっと頻繁に、もっと大きく売り買いするようになります。そして大きな下落が来ると、買い増すお金も、売る余裕も残っていません。\n▶ キムさんが直面した五つの分かれ道で、あなたはどう選ぶか。テストの全体は下の関連動画で：株式投資で失敗する人は絶対に合格できないテスト\n\n※ タイトルの「99%」は計算した数字ではなく、それほど損をしやすいという強調の表現です。\n過去のデータで作った研究・教育用の動画で、投資の勧誘ではありません。ナレーションはAI音声、画像はAIで作った演出です。\n#株式 #株式テスト"
 },
 "de": {
  "title": "Wer mit „diesem Gedanken“ in Aktien investiert, macht zu 99% Verlust.",
  "description": "„Dieser Gedanke“ ist der Wunsch, mit Aktien schnell Geld zu verdienen.\nMachst du Gewinn, kaufst du für immer größere Beträge; machst du Verlust, handelst du öfter und größer, um ihn schnell zurückzuholen. Kommt dann ein großer Absturz, bleibt weder Geld zum Nachkaufen noch Spielraum zum Verkaufen.\n▶ Wie würdest du dich an den fünf Weggabelungen von Herrn Kim entscheiden? Den ganzen Test gibt es im verlinkten Video unten: Der Test, den Leute, die an der Börse scheitern, nie bestehen\n\n※ Die „99%“ im Titel sind keine berechnete Zahl, sondern eine Zuspitzung dafür, wie leicht man Verluste macht.\nEin Forschungs- und Bildungsvideo auf Basis historischer Daten, keine Anlageberatung. Die Stimme ist eine KI-Stimme, die Bilder sind mit KI erstellte Illustrationen.\n#Aktien #AktienTest"
 },
 "vi": {
  "title": "Đầu tư cổ phiếu với 'suy nghĩ này', 99% bạn sẽ thua lỗ.",
  "description": "'Suy nghĩ này' chính là mong muốn kiếm tiền thật nhanh từ cổ phiếu.\nCó lãi thì cứ tăng số tiền mua vào; lỗ thì muốn gỡ nhanh nên mua bán ngày càng nhiều lần, ngày càng lớn. Rồi khi đợt giảm mạnh ập đến, chẳng còn tiền để mua thêm, cũng chẳng còn đường để bán.\n▶ Ở năm ngã rẽ mà anh Kim từng gặp, bạn sẽ chọn gì? Toàn bộ bài kiểm tra có trong video liên quan bên dưới: Bài kiểm tra mà người đầu tư cổ phiếu thất bại không bao giờ vượt qua được\n\n※ Con số '99%' trong tiêu đề không phải số liệu tính toán, mà là cách nhấn mạnh rằng rất dễ thua lỗ.\nVideo nghiên cứu, giáo dục dựa trên dữ liệu quá khứ, không phải lời khuyên đầu tư. Lời thuyết minh là giọng AI, hình ảnh là minh họa do AI tạo.\n#CổPhiếu #TestCổPhiếu"
 },
 "tr": {
  "title": "'Bu düşünceyle' borsaya yatırım yaparsanız %99 zarar edersiniz.",
  "description": "'Bu düşünce', borsadan hızlıca para kazanma isteğidir.\nKâr edince alım tutarını giderek artırırsınız; zarar edince de hemen telafi etmek için daha sık ve daha büyük alım satım yaparsınız. Sonra büyük bir düşüş geldiğinde ne alacak paranız ne de satacak hâliniz kalır.\n▶ Kim Bey'in karşılaştığı beş yol ayrımında siz ne seçerdiniz? Testin tamamı aşağıdaki ilgili videoda: Borsada başarısız olanların asla geçemediği test\n\n※ Başlıktaki '%99' hesaplanmış bir sayı değil, zarar etmenin ne kadar kolay olduğunu vurgulayan bir ifadedir.\nGeçmiş verilerle hazırlanmış bir araştırma ve eğitim videosudur, yatırım tavsiyesi değildir. Seslendirme yapay zekâ sesidir, görseller yapay zekâyla hazırlanmış canlandırmalardır.\n#Borsa #BorsaTesti"
 }
}
```

- 한국어 1·2번을 그대로 옮김 · 제목의 '이 생각' 따옴표 꼴 유지 · ▶ 줄의 롱폼 제목 = 롱폼 시트 6번의 그 언어 제목 · 해시태그는 언어마다 2개.
- 언어별 자막 `subs/ppalli-test-2026-11-shorts.<언어>.srt` (대본 `subs/ppalli-test-2026-11-shorts.<언어>.txt`) · 썸네일은 언어별로 만들지 않음 (첫 장면에 한국어 문구가 구워져 있음).

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올린 뒤 예약 공개 (롱폼과 같은 시각) |
| 썸네일 | `thumbnails/thumbnail_1.jpg` (세 칸 band — 영상 0초 장면과 같음) · 안 보이면 공개 뒤 앱에서 0초 장면 |
| 자막 | `ppalli-test-2026-11-shorts.srt` |
| 자막 올리기 | 언어별 (한국어 `ppalli-test-2026-11-shorts.srt` + `subs/ppalli-test-2026-11-shorts.<언어>.srt` 9개 — 외국어는 CC · 한국어 자막이 화면에 구워져 있어 겹칠 수 있음, 올리기 전 사용자 확인 — 규칙 46) |
| 기본 언어 | ko |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성, 그림이 AI 연출) |

## 8. 결과 (업로드 후)

- (아직 없음)
