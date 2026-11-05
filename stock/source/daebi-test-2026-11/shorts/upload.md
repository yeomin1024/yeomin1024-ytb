# daebi-test-2026-11-shorts 업로드 시트 (주식 쇼츠)

버전: v1.3 — 2026-11-05 — 외국어 설정 (사용자 지시 "외국어 자막, 제목, 썸네일 등 외국어 설정에 필요한 것들 생성하고 지시사항에 반영해 이건 영상이 렌더까지 완료되면 하는거야" — `stock/guides/quick_board.md` 규칙 46): 5번 언어별 제목·설명 9개(지금 제목·설명란 번역 · ▶ 줄의 롱폼 제목은 롱폼 시트 6번의 그 언어 제목) · 자막 대본·SRT `subs/daebi-test-2026-11-shorts.<언어>.txt·srt` 9개 · 설정표 '기본 언어 ko'·'자막 올리기 언어별' · 썸네일은 0초 장면이라 언어별 없음 — 섹션 번호 5~6 → 6~7.
이전 v1.2 — 2026-11-05 — 쇼츠 설명란은 원래 꼴로 되돌림 (사용자 지시 "쇼츠는 다시 원래했던 설명으로 지시사항 수정하고 다시 설명 보여줘" — 규칙 45 는 롱폼만) · 태그는 늘린 것 그대로.
이전 v1.1 — 2026-11-05 — 설명란 줄임·태그 늘림 (사용자 지시 "김씨는 실제 숫자로 만든 가상의 인물입니다. 내레이션은 AI 음성이고, 그림은 AI로 만든 연출입니다. 다섯 가지 선택, 계산기준빼고 태그도 더 추가 하는걸로 설명 만들자 지시사항에도 반영해" — `stock/guides/quick_board.md` 규칙 45): '다섯 가지 선택'·'계산 기준'·'○씨는 가상의 인물'·'AI 음성/그림' 줄 뺌 · 태그 21개(편 낱말 + 실제 영상 태그 `stock/tag_candidates.md`).
이전 v1.0 — 2026-11-05 — 새로 만듦 (사용자 "2편은 쇼츠 대본 만든거 아니야?" → 대본·음성이 있어 영상 만듦) · 제목 = 사용자 쇼츠 제목 그대로 (`stock/topics/쇼츠안_2026-10-30.md` 2편) · 설명란 = 짧은 설명 + 롱폼 안내 + 알려 드립니다 + 해시태그 2개 · 한국어만 (1편 쇼츠 시트와 같은 꼴).

기준 파일: 쇼츠 대본 `daebi-test-2026-11-shorts.txt` (12문장) · SRT `daebi-test-2026-11-shorts.srt` (오디오에 맞춤, 끝 0:53.4) · 올릴 영상 = `stock/out/daebi-test-2026-11-shorts/final_1080p.mp4` (이 클라우드 컨테이너에만 — git 에 넣지 않음, 장면 파일·오디오로 다시 만듦)

> 업로드: `python3 tools/youtube_upload.py stock daebi-test-2026-11-shorts --dry-run` → `--publish-at <롱폼과 같은 시각>`. 롱폼 `daebi-test-2026-11` 과 **같은 시각에 공개** (`guides/upload_guide.md` 12번). 관련 동영상 = 그 롱폼 (사용자가 스튜디오에서). 2편 공개 날짜는 사용자가 정하기 전 — 1편(2026-11-12 17시) 다음 날 이후.
> ※ 연구·교육용 — 투자 권유가 아님.

## 1. 제목 (사용자 쇼츠 제목 그대로)

```
'이 생각'을 가지고 주식 투자하면 당신은 절대 폭락을 피하지 못할 겁니다.
```

- `title_fit.py --shorts`: 쇼츠 재생 화면 2줄 ✅ · 홈 Shorts 칸·PC 다음 동영상 3줄 ❌ (42자) — 사용자 제목이라 그대로 (2026-11-02 점검에서 알고 둠). '절대'는 반론 페르소나 K8 낱말 — 사용자 제목.

## 2. 설명란 (그대로 복사)

```
상승장에서 번 돈을 내 실력이라고 믿는 생각이, 폭락에서 어떻게 계좌를 무너뜨리는지 짧게 담았습니다.
▶ 다섯 가지 생각 가운데 당신은 몇 개인지, 테스트 전체는 아래 '관련 동영상'에서 확인하세요 — 수익 나도 결국 손실 보는 생각 5개, 당신은 몇 개인가요?

■ 알려 드립니다
과거 자료로 만든 연구·교육용 영상이며, 투자 권유가 아닙니다. 2020년에 2배 넘게 오른 회사 수는 지금 S&P 500에 속한 회사만 센 것입니다. 내레이션은 AI 음성이고, 그림은 AI로 만든 연출입니다.
#주식 #주식테스트
```

## 3. 챕터

```
```

- 쇼츠는 챕터 없음.

## 4. 태그

```
주식 테스트, 상승장, 폭락, 투자 실패, 리스크 관리, 하락장, 성장주, 주식, 주식투자, 미국주식, 주식초보, 주린이, 주식공부, 주식기초, 투자공부, 투자마인드, 개미투자자, 초보투자자, 장기투자, S&P500, 주식하는법
```

## 5. 언어별 제목·설명 (2026-11-05 — 1·2번을 그대로 번역 · 9개 언어 · 업로드 도구 localizations)

```
{
 "en": {
  "title": "Invest with 'this thought' and you'll never escape a crash.",
  "description": "A short look at how believing that money made in a bull market is your own skill can wreck your account in a crash.\n▶ Which of the five thoughts do you have? Take the full test in the related video below: 5 thoughts that turn stock gains into losses: how many do you have?\n\n■ Please note\nA research and educational video made from past data, not investment advice. The number of companies that rose more than 2x in 2020 counts only companies in today's S&P 500. The narration is an AI voice, and the images are AI-made illustrations.\n#Stocks #StockTest"
 },
 "hi": {
  "title": "'इस सोच' के साथ शेयरों में निवेश करेंगे, तो क्रैश से कभी नहीं बचेंगे।",
  "description": "तेज़ी के बाज़ार में कमाए पैसे को अपना हुनर मानने की सोच, क्रैश में आपका खाता कैसे डुबो देती है, यह छोटे में दिखाया है।\n▶ पाँच विचारों में से आपमें कितने हैं, पूरा टेस्ट नीचे जुड़े वीडियो में देखिए: मुनाफ़े के बाद भी घाटा कराने वाले 5 विचार, आपमें कितने हैं?\n\n■ ध्यान दें\nयह पुराने डेटा से बना शोध और शिक्षा का वीडियो है, निवेश सलाह नहीं। 2020 में 2 गुना से ज़्यादा बढ़ी कंपनियों की गिनती सिर्फ़ आज की S&P 500 कंपनियों में से है। आवाज़ AI की है, और चित्र AI से बनाए गए हैं।\n#शेयरबाज़ार #शेयरटेस्ट"
 },
 "id": {
  "title": "Investasi saham dengan 'pikiran ini', kamu tak akan lolos dari pasar anjlok.",
  "description": "Singkatnya, bagaimana pikiran bahwa uang dari pasar naik adalah hasil keahlianmu bisa menghancurkan akunmu saat pasar anjlok.\n▶ Dari lima pikiran itu, kamu punya berapa? Tes lengkapnya ada di video tertaut di bawah: 5 pikiran yang bikin untung saham berujung rugi, kamu punya berapa?\n\n■ Perlu diketahui\nVideo riset dan edukasi dari data masa lalu, bukan ajakan investasi. Jumlah perusahaan yang naik lebih dari 2 kali lipat pada 2020 hanya menghitung perusahaan yang kini ada di S&P 500. Narasinya suara AI, dan gambarnya ilustrasi buatan AI.\n#Saham #TesSaham"
 },
 "pt": {
  "title": "Investindo com 'este pensamento', você nunca vai escapar de um crash.",
  "description": "Mostramos rapidinho como achar que o dinheiro ganho na alta vem do seu talento pode destruir sua conta num crash.\n▶ Quantos dos cinco pensamentos você tem? Faça o teste completo no vídeo vinculado abaixo: 5 pensamentos que transformam lucro em prejuízo: quantos você tem?\n\n■ Aviso\nVídeo de pesquisa e educação feito com dados do passado; não é recomendação de investimento. O número de empresas que subiram mais de 2 vezes em 2020 conta só as empresas que estão hoje no S&P 500. A narração é voz de IA, e as imagens são ilustrações feitas com IA.\n#Ações #TesteDeAções"
 },
 "es-419": {
  "title": "Si inviertes con 'este pensamiento', nunca escaparás de un desplome.",
  "description": "Te mostramos en corto cómo creer que el dinero ganado en un mercado alcista viene de tu habilidad puede hundir tu cuenta en un desplome.\n▶ ¿Cuántos de los cinco pensamientos tienes? Haz la prueba completa en el video vinculado abajo: 5 pensamientos que convierten ganancias en pérdidas: ¿cuántos tienes?\n\n■ Aviso\nVideo de investigación y educación hecho con datos del pasado; no es recomendación de inversión. El número de empresas que subieron más de 2 veces en 2020 solo cuenta las empresas que hoy están en el S&P 500. La narración es una voz de IA y las imágenes son ilustraciones hechas con IA.\n#Acciones #TestDeAcciones"
 },
 "ja": {
  "title": "「この考え」で株式投資をすると、あなたは絶対に暴落を避けられません。",
  "description": "上昇相場で稼いだお金を自分の実力だと信じる考えが、暴落でどう口座を崩すのかを短くまとめました。\n▶ 五つの考えのうちあなたはいくつ当てはまるか、テストの全編は下のリンクの動画で確認してください — 利益が出ても結局損する5つの考え、あなたはいくつ当てはまる？\n\n■ お知らせ\n過去のデータで作った研究・教育用の動画で、投資の勧誘ではありません。2020年に2倍を超えて上がった企業の数は、今のS&P 500に属する企業だけを数えたものです。ナレーションはAI音声で、絵はAIで作った演出です。\n#株 #株テスト"
 },
 "de": {
  "title": "Mit „diesem Gedanken“ an der Börse entkommst du keinem Crash.",
  "description": "Kurz gezeigt: Wie der Glaube, im Bullenmarkt verdientes Geld sei dein eigenes Können, dein Depot im Crash ruinieren kann.\n▶ Wie viele der fünf Gedanken hast du? Den ganzen Test findest du im verlinkten Video unten: 5 Gedanken, die aus Gewinnen Verluste machen – wie viele hast du?\n\n■ Hinweis\nForschungs- und Bildungsvideo auf Basis vergangener Daten, keine Anlageberatung. Die Zahl der Firmen, die 2020 auf mehr als das 2-Fache stiegen, zählt nur Firmen, die heute im S&P 500 sind. Die Stimme ist eine KI-Stimme, die Bilder sind mit KI erstellte Illustrationen.\n#Aktien #AktienTest"
 },
 "vi": {
  "title": "Đầu tư với 'suy nghĩ này', bạn chắc chắn không tránh được cú sập.",
  "description": "Tóm tắt ngắn cách suy nghĩ rằng tiền kiếm được trong thị trường tăng là nhờ thực lực của mình có thể làm tài khoản sụp đổ khi thị trường sập.\n▶ Trong năm suy nghĩ, bạn mắc mấy cái? Xem toàn bộ bài test ở video liên kết bên dưới: 5 suy nghĩ khiến có lời rồi vẫn lỗ, bạn mắc mấy cái?\n\n■ Lưu ý\nVideo nghiên cứu và giáo dục làm từ dữ liệu quá khứ, không phải lời khuyên đầu tư. Số công ty tăng hơn 2 lần trong năm 2020 chỉ tính các công ty hiện thuộc S&P 500. Lời thuyết minh là giọng AI, hình ảnh là minh họa tạo bằng AI.\n#ChứngKhoán #TestChứngKhoán"
 },
 "tr": {
  "title": "'Bu düşünceyle' borsaya yatırım yaparsanız çöküşten asla kaçamazsınız.",
  "description": "Yükselen piyasada kazanılan parayı kendi yeteneğiniz sanmanın, çöküşte hesabınızı nasıl batırdığını kısaca anlattık.\n▶ Beş düşünceden sizde kaç tane var? Testin tamamı aşağıdaki bağlantılı videoda: Kâr etseniz de sonunda zarar ettiren 5 düşünce: sizde kaç tane var?\n\n■ Bilgilendirme\nGeçmiş verilerle hazırlanmış araştırma ve eğitim videosudur, yatırım tavsiyesi değildir. 2020'de 2 kattan fazla yükselen şirket sayısı yalnızca bugün S&P 500'de yer alan şirketleri sayar. Seslendirme yapay zekâ sesi, görseller ise yapay zekâyla hazırlanmış çizimlerdir.\n#Borsa #BorsaTesti"
 }
}
```

## 6. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올린 뒤 예약 공개 (롱폼과 같은 시각) |
| 썸네일 | `thumbnails/thumbnail_1.jpg` (세 칸 band — 영상 0초 장면과 같음) · 안 보이면 공개 뒤 앱에서 0초 장면 |
| 자막 | `daebi-test-2026-11-shorts.srt` |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 |
| 기본 언어 | ko |
| 자막 올리기 | 언어별 (한국어 `daebi-test-2026-11-shorts.srt` + `subs/daebi-test-2026-11-shorts.<언어>.srt` 9개 — `tools/subs_tool.py build`, 장면 파일 문장 시각) |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성) |

## 7. 결과 (업로드 후)

- (아직 없음)
