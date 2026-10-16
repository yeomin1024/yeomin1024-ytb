# upload-test-2026-10-16 업로드 시트 (재테크 채널 업로드 시험용 데모 — 실제 영상 아님)

버전: v1.0 — 2026-10-16 — 최초. 사용자 지시 2026-10-16 "이 환경은 저장소에 있는 공통 지시사항 및 재테크 주제(economic)분석 결과와 지시사항 참고해 영상 소스를 만들고 최종적으로 영상을 만들어 부자백서 채널에 업로드 할 환경이야 한번 업로드 잘되는지 데모 영상 만들어서 업로드 테스트해봐".
기준 파일: `eunte-kkeonaeseugi-2026-10` 완성 장면(`video/episodes/eunte-kkeonaeseugi-2026-10/index.html`, 실제 오디오 시각)의 **도입 0~51초** (첫 장 '같은 5억, 다른 세금' 전부, 문장 1~14) · 실제 내레이션(H04) · 자막 구움 · 음량 -14 LUFS
(`render.mjs video economic eunte-kkeonaeseugi-2026-10 --from 0 --to 51` → `tools/loudnorm.py`) · 영상 파일은 git·Drive 에 넣지 않음 (컨테이너에만)

> 목적: 재테크 영상과 같은 설정(한국어 제목·설명 · **한국어 자막(SRT) 올리기** · 합성 콘텐츠 예 · 썸네일 webp → JPG 변환 · 예약 공개 값)이 이 클라우드 환경의 키로 **부자백서** 채널에 그대로 올라가는지 시험한다.
> 공개 상태: **비공개**. 예약 공개(`publishAt`)는 먼 날짜로 걸어 값이 저장되는지만 보고 **바로 지운다** (시험 영상이 공개되지 않게). 다 보면 스튜디오에서 지운다.
> 연구·교육용 콘텐츠 — 세무·보험·투자 상담이나 권유가 아님.

## 1. 제목

```
[업로드 테스트] 부자백서 데모 — 노후 연금 꺼내는 순서 도입 51초
```

## 2. 설명란

```
업로드 시험용 비공개 영상입니다. 실제 영상이 아니며 시험이 끝나면 지웁니다.
'노후 연금 꺼내는 순서' 영상의 도입 51초입니다.

이 영상의 내레이션은 AI 음성으로 만들었습니다.
이 영상은 정보 제공을 위한 것이며 세무·보험·투자 상담이나 권유가 아닙니다.
```

## 4. 태그

```
업로드 테스트, 노후 연금, 연금 꺼내는 순서
```

## 6. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | **비공개** · 예약 공개 시험: `--publish-at 2026-12-31T23:00:00+09:00` 로 올려 저장된 값을 읽고 곧바로 `videos.update` 로 예약을 지움 (결과 9번) |
| 썸네일 | 시험용: `eunte-kkeonaeseugi-2026-10/thumbnails/thumbnail_1.webp`(본안)을 `economic/out/upload-test-2026-10-16/thumbnails/thumbnail_1.webp` 로 복사 (git 에 없음) — webp → 1280×720 JPG 변환과 `thumbnails.set` 시험 |
| 자막 올리기 | 예 — `upload-test-2026-10-16.srt` (원래 SRT 의 0~51초 16개, 끝 시각 51.000 으로 자름. 화면에 구운 자막과 같은 글) |
| 기본 언어 | ko |
| 카테고리 | 교육 |
| 시청자층 | 아동용 아님 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — 사용자 지시 2026-10-11) |

- 챕터: 넣지 않음 (51초 안에 장이 하나뿐 — 유튜브 챕터는 3개 이상·10초 이상). 챕터 계산은 실제 시트 `--dry-run` 으로 따로 확인 (9번).

## 8. 점검
- 숫자는 원래 영상(대본 v1.2.1·`calc/calc.py`)의 도입 그대로 — 새로 쓴 숫자 없음.
- 제목·설명 100자·5,000자 이하, `< >` 없음 — `youtube_upload.py --dry-run` (결과 9번).

## 9. 결과 (업로드 후)
- `youtube.json` (업로드 도구가 씀) · 올라간 값 확인은 아래에 적는다.

**2026-10-16 클라우드에서 올림 — 성공** (`python tools/youtube_upload.py economic upload-test-2026-10-16 --publish-at 2026-12-31T23:00:00+09:00`, 이 환경의 클라우드 환경 변수 키, 업로드 도구 v1.7)
- 영상: https://youtu.be/CGuiF0dP6Bw · 스튜디오 https://studio.youtube.com/video/CGuiF0dP6Bw/edit
- 채널: **부자백서** (UCJ1gjiL7VuAhMQSfAhxAefg) — 올리기 전 채널 확인 `[CHANNEL] status=ok` (v1.7, `economic/youtube_channel.json`).
- 렌더 88초(1,530프레임, 작업자 3) → 음량 -20.34 → **-14.22 LUFS**, 트루 피크 -3.63 → **-1.69 dBTP** (2번째 시도에서 통과) → 51.03초 1920×1080 H.264 + AAC 48kHz 모노, 4.0MB.
- 올리기 1초 → 처리 `succeeded` · 자막 `captions.insert` 성공 · 썸네일 webp(1672×941) → JPG 1280×720 0.14MB 변환·`thumbnails.set` 성공 (= 이 채널은 맞춤 썸네일 가능).

유튜브가 저장한 값 (`videos.list`·`captions.list` 로 다시 읽음, 07:33Z):

| 항목 | 보낸 값 | 유튜브 값 | |
|---|---|---|---|
| 채널 | 부자백서 | channelTitle 부자백서 | ✅ |
| 공개 상태 | private + publishAt 2026-12-31T14:00:00Z | private, **publishAt 2026-12-31T14:00:00Z 저장됨** | ✅ 예약 공개 값이 API 로 걸림 |
| 예약 지우기 | `videos.update`(status, publishAt 뺌) | publishAt 없음, private 그대로 | ✅ (이때 `publicStatsViewable` 이 false 로 바뀌어 true 로 다시 보냄 → true) |
| 제목·설명 | 1·2번 | 같음 (설명 146자) | ✅ |
| 기본 언어 · 오디오 언어 | ko · ko | ko · ko | ✅ |
| 카테고리 | 27 (교육) | 27 | ✅ |
| 태그 | 3개 | 3개 | ✅ |
| 아동용 | 아니요 | madeForKids false | ✅ |
| 합성 콘텐츠 | 예 | `videos.list` 는 이 칸을 돌려주지 않음 → `videos.update` 응답 `containsSyntheticMedia: true` | ✅ (스튜디오에서 눈으로 한 번 더) |
| 자막 | `upload-test-2026-10-16.srt` (16개) | 한국어 standard `serving` (+ 유튜브 자동 자막 asr) | ✅ |
| 썸네일 | thumbnail_1_upload.jpg 1280×720 | maxres 까지 생김 | ✅ |
| 길이·화질 | 51.03초 1080p | PT52S · hd | ✅ (초 올림) |

- 실제 1편 시트 `eunte-kkeonaeseugi-2026-10 --dry-run`: 챕터 9개 규칙 통과·채널 확인 ok, 문제는 '영상 파일 없음'(이 컨테이너에서 전편을 렌더하지 않음) 하나.
- 채널 확인이 막는지 실제 키로: `stock tteoreojimyeon-sagi-2026-10 --dry-run` → `키의 채널 = 부자백서 …, stock 채널 = STOCK LAB … 멈춤` ✅.
- 이 키에 **Google Drive 권한은 없음** (`drive_videos.py check` ❌) — 클라우드에서 바로 올리면 Drive 는 필요 없다. PC 업로더 길(Drive 원본)을 쓸 때만 `youtube_auth.py` v1.2 로 키를 다시 받는다.
- **확인 못 한 것**: Google 감사 전 API 프로젝트의 '비공개 잠금' — API 값으로는 안 보임. 스튜디오 → 이 영상 → 공개 상태에 잠금 표시(제한)가 있는지 사용자가 본다. 잠겨 있으면 예약 공개 값은 걸려도 그 시각에 공개되지 않는다.
- 다 보면 스튜디오에서 이 영상을 지운다 (이 `youtube.json` 은 기록으로 둔다 — 지우면 PC 업로더가 이 폴더를 '올릴 영상'으로 본다).
