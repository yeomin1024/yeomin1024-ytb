# upload-test-2026-10-16 업로드 시트 (업로드 시험용 데모 — 실제 영상 아님)

버전: v1.0 — 2026-10-16 — 최초. 사용자 지시 2026-10-16 "한번 업로드 잘되는지 데모 영상 만들어서 업로드 테스트해봐" (STOCK LAB 채널 — 채널 이름은 아직 '편안한 음악 Relaxing Music', 사용자: "내가 아직 채널명 변경안해서 그래 한번 올려봐").
기준 파일: 장면 `video/episodes/tteoreojimyeon-sagi-2026-10/index.html` v1.1 의 도입 0~40초 · **추정 시각, 소리 없음** (`render.mjs video … --estimated-preview --from 0 --to 40`) · 영상 파일은 git·Drive 에 넣지 않음 (컨테이너에만)

> 목적: 주식 영상과 같은 설정(언어별 제목·설명 9개 + 기본 언어 ko · 자막 올리지 않음 · 합성 콘텐츠 예 · 썸네일 1개)이 API 로 그대로 올라가는지 시험한다.
> 공개 상태: **비공개, 예약 공개 없음** — 시험 영상이 채널에 공개되지 않게 한다. 다 보면 스튜디오에서 지운다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (한국어 — 기본 언어)

```
[업로드 테스트] STOCK LAB 데모 — 저점 매수 백테스트 도입 40초
```

## 2. 설명란 (한국어)

```
업로드 시험용 비공개 영상입니다. 실제 영상이 아니며 시험이 끝나면 지웁니다.
'저점 매수' 백테스트 영상의 도입 40초를 소리 없이 미리 렌더한 것입니다 (내레이션 전 추정 시각).

과거 자료로 계산한 결과는 앞으로도 같다는 보장이 없습니다. 투자 권유가 아닙니다.
```

## 4. 태그

```
업로드 테스트, 백테스트, S&P500
```

## 5. 언어별 제목·설명 (localizations)

```
{
 "en": {"title": "[Upload test] STOCK LAB demo — buy-the-dip backtest intro, 40 s", "description": "Private upload test. Not a real video; it will be deleted after the test.\nA silent 40-second preview of the intro of the buy-the-dip backtest video.\nFor education only. Not investment advice."},
 "hi": {"title": "[अपलोड टेस्ट] STOCK LAB डेमो — गिरावट में खरीद बैकटेस्ट, शुरुआत 40 सेकंड", "description": "निजी अपलोड टेस्ट। यह असली वीडियो नहीं है; टेस्ट के बाद हटा दिया जाएगा।\nकेवल शिक्षा के लिए, निवेश सलाह नहीं।"},
 "id": {"title": "[Uji unggah] Demo STOCK LAB — pembuka backtest beli saat turun, 40 detik", "description": "Uji unggah pribadi. Bukan video sebenarnya; akan dihapus setelah uji.\nHanya untuk edukasi, bukan saran investasi."},
 "pt": {"title": "[Teste de envio] Demo STOCK LAB — abertura do backtest comprar na queda, 40 s", "description": "Teste de envio privado. Não é um vídeo real; será apagado após o teste.\nApenas educativo, não é recomendação de investimento."},
 "es-419": {"title": "[Prueba de subida] Demo STOCK LAB — inicio del backtest comprar en la caída, 40 s", "description": "Prueba de subida privada. No es un video real; se borrará después de la prueba.\nSolo educativo, no es asesoría de inversión."},
 "ja": {"title": "[アップロードテスト] STOCK LAB デモ — 押し目買いバックテスト冒頭40秒", "description": "非公開のアップロードテストです。本番の動画ではなく、テスト後に削除します。\n教育目的であり、投資助言ではありません。"},
 "de": {"title": "[Upload-Test] STOCK LAB Demo — Buy-the-Dip-Backtest, Intro 40 s", "description": "Privater Upload-Test. Kein echtes Video; wird nach dem Test gelöscht.\nNur zur Bildung, keine Anlageberatung."},
 "vi": {"title": "[Thử tải lên] Demo STOCK LAB — mở đầu backtest bắt đáy, 40 giây", "description": "Thử tải lên ở chế độ riêng tư. Không phải video thật; sẽ xóa sau khi thử.\nChỉ nhằm mục đích giáo dục, không phải lời khuyên đầu tư."},
 "tr": {"title": "[Yükleme testi] STOCK LAB demo — düşüşte alım backtest girişi, 40 sn", "description": "Gizli yükleme testi. Gerçek video değildir; testten sonra silinecek.\nYalnızca eğitim amaçlıdır, yatırım tavsiyesi değildir."}
}
```

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | **비공개, 예약 공개 없음** (`youtube_upload.py` 기본 — `--publish-at` 안 씀) |
| 썸네일 | 시험용: 데모 영상 한 장면(0:04)을 뽑은 것 — `stock/out/upload-test-2026-10-16/thumbnails/thumbnail_1.jpg` (git 에 없음, 실제 썸네일 규칙과 무관 — `thumbnails.set` 이 되는지만 시험) |
| 기본 언어 | ko |
| 자막 올리기 | **아니요** (주식 영상과 같게) |
| 카테고리 | 교육 |
| 시청자층 | 아동용 아님 |
| 변경되거나 합성된 콘텐츠 | **예** (데모엔 목소리가 없지만 실제 주식 영상과 같은 값이 등록되는지 시험) |

## 8. 점검
- 제목·언어별 제목 100자 이하, `< >` 없음 — `youtube_upload.py --dry-run` 으로 확인 (결과는 9번).
- 결과 숫자 없음 (도입 0~40초는 결과 전 — 화면도 `?`·`₩?`).

## 9. 결과 (업로드 후)
- `youtube.json` (업로드 도구가 씀) · 올라간 값 확인은 아래 줄에 적는다.

**2026-10-16 클라우드에서 올림 — 성공** (`python tools/youtube_upload.py stock upload-test-2026-10-16`, 클라우드 환경 변수 키)
- 영상: https://youtu.be/3FJPCemQ0fw · 스튜디오 https://studio.youtube.com/video/3FJPCemQ0fw/edit
- 채널: `편안한 음악 Relaxing Music` (UC7Rw5HWgKz5njCCciX8IVJQ) — 사용자: STOCK LAB 채널이 맞고 이름은 아직 안 바꿈.
- 올리기 1초(0.9MB) → 처리 `succeeded`, 썸네일 `thumbnails.set` 성공(= 채널 전화 인증 됨), 자막 건너뜀(시트 '아니요').

유튜브가 저장한 값 (`videos.list` 로 다시 읽음, 06:38Z):

| 항목 | 보낸 값 | 유튜브 값 | |
|---|---|---|---|
| 공개 상태 | private (예약 없음) | private, uploadStatus processed | ✅ |
| 제목·설명 (ko) | 1·2번 | 같음 | ✅ |
| 언어별 제목·설명 | 9개 | ko 포함 10개 (de·en·es-419·hi·id·ja·ko·pt·tr·vi), en 제목 같음 | ✅ |
| 기본 언어 · 오디오 언어 | ko · ko | ko · ko | ✅ |
| 카테고리 | 27 (교육) | 27 | ✅ |
| 태그 | 3개 | 3개 | ✅ |
| 아동용 | 아니요 | madeForKids false | ✅ |
| 합성 콘텐츠 | 예 | `videos.list` 는 이 칸을 돌려주지 않음 → 같은 값으로 `videos.update`(status) 하니 응답에 `containsSyntheticMedia: true` | ✅ (스튜디오에서 눈으로 한 번 더) |
| 썸네일 | thumbnail_1.jpg 1280×720 | maxres 까지 생김 | ✅ |
| 길이·화질 | 40초 1080p | PT40S · hd | ✅ |
| 자막 | 올리지 않음 | caption false | ✅ |

- **확인 못 한 것**: ① 예약 공개(`publishAt`) — 시험 영상이 공개되면 안 돼서 걸지 않음. ② Google 감사 전 API 프로젝트의 '비공개 잠금' — API 값으로는 안 보임. 스튜디오 → 이 영상 → 공개 상태에 잠금 표시(제한)가 있는지 사용자가 본다.
- 다 보면 스튜디오에서 이 영상을 지운다 (이 `youtube.json` 은 기록으로 둔다 — 지우면 PC 업로더가 이 폴더를 '올릴 영상'으로 본다).
