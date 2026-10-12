# 주식 주제 폴더 — 백업 (`stock_backup/`, 옛 `stock/`)

> ⏸ 백업 — 보류 (사용자 지시 2026-10-12: "기존 주제폴더 _backup 붙여서 백업해놓고 stock만 새로 만들어서"). 2026-10-12까지의 주식 폴더를 그대로 옮겨 둔 것이다. 새 작업은 `stock/`에서 한다.
> - 이 폴더는 내레이션(`tts_narration.py all`)·요약(`make_summary.py --all`)에서 건너뛴다 (위 ⏸ 보류 표시).
> - 이미 올린 영상 4개(bittu·molppang·multagi·panicsell)의 `youtube.json`·통계는 여기 남는다 — `python tools/youtube_feedback.py stock_backup` 로 계속 모은다.
> - 아래 표의 경로 `stock/…`는 옮기기 전 이름이다 (지금은 `stock_backup/…`).


공통 지시사항은 저장소 최상위 `guides/`에 있고, 이 폴더에는 **주식에만 해당하는 것**만 둔다.

| 위치 | 내용 |
|---|---|
| `analyzer_config.toml` | 분석기 설정: 검색 키워드(9개 카테고리·90개), 관련어, 광고 의심 기준 |
| `result/` | 분석 결과 (분석기가 GitHub에 올림 — 직접 고치지 않음) |
| `guides/data_insights.md` | 분석 결과를 지시사항용으로 요약 — v2.0: 작은 채널(구독자 5만 이하) 최근 성공 사례 30개의 제목·길이·형식·썸네일, 성공 사례 댓글 748개로 본 시청자 니즈, 사용자 결정 필요 항목 (지난 분석기 통계는 7번 참고) |
| `guides/script_rules.md` | 주식 대본 규칙: 금액 1억 이하, 투자 유의 4요소, 근거 자료 은행 |
| `guides/title_rules.md` | 주식 제목 규칙: 상시 고민 목록, 기준 제목, 좋음 9개, 숫자 기준값 |
| `guides/thumbnail_rules.md` | 주식 썸네일 규칙: 손실 파랑 고정, 계좌 카드, 가상 인물 사용 |
| `guides/upload_rules.md` | 주식 업로드 규칙: 설명란 필수 고지·출처, 태그 묶음, 스팸 차단 단어 |
| `titles/` | 제목 피드백 시트 (1차 50개 — 표시 완료, 2차 36개 — 표시 전) |
| `source/used_content.md` | 이전 대본과의 중복 방지 목록 |
| `source/molppang-2026-10/` | 몰빵 영상 v2.1: 대본 TXT·SRT(문장 91 / 자막 116, 문장 18 뒤 고지 공백, 내레이션에 맞춤), 문장 40~47을 최신 사례로 교체(v2.1), README(최신 사례 출처·옛→새 번호 대응표), `titles.md`(제목 3개, T1 채택 = 기준 제목), `thumbnails/`(썸네일 프롬프트 3개 — 하단 제목 2줄, thumbnail_3 검은 배경 제목형), `upload.md`(업로드 시트, 챕터는 오디오 시간). 사연: 몽고디비 2026년 9월 CEO 이적 소식. 영상 코드 `video/src/episodes/molppang-2026-10/` — 렌더 완료(7:57) |
| `source/multagi-2026-10/` | 물타기 영상: 대본 v1.4 TXT·SRT(문장 91 / 자막 107, 문제 03·04를 최신 사례로), README(검산·출처), `titles.md`(제목 3개, T1 채택), `thumbnails/`(썸네일 프롬프트 3개), `upload.md`(업로드 시트) |
| `source/bittu-2026-10/` | 빚투 영상: 대본 v1.1 TXT·SRT(문장 88 / 자막 105), README(검산·출처), `titles.md`(T1 채택), `thumbnails/`(3개), `upload.md`. 사연: SK하이닉스 2026년 5~7월, 신용 → 반대매매. 영상 코드 `video/src/episodes/bittu-2026-10/` — 내레이션 대기 |
| `source/panicsell-2026-10/` | 패닉셀 영상: 대본 v1.1 TXT·SRT(문장 92 / 자막 111, 문장 80~85를 최신 사례로), README(검산·출처), `titles.md`(T1 채택), `thumbnails/`(3개), `upload.md`. 사연: 삼성전자 2026년 3월 폭락 날 전량 매도 → 7주 뒤 +30%. 영상 코드 `video/src/episodes/panicsell-2026-10/` — 내레이션 대기 |
| `source/chugyeok-2026-10/` | 추격 매수 영상: 대본 v1.0 TXT·SRT(문장 103 / 자막 120, 문장 20 뒤 고지 공백, **사연 5문장·121음절 ≈ 27초** — 사연 20~30초 규칙으로 쓴 첫 대본), README(검산·출처), `titles.md`(T1 채택), `thumbnails/`(3개 — 하단 제목 2줄, thumbnail_3 검은 배경 제목형), `upload.md`. 사연: 써클 2025년 6월 상장 직후 공모가 7배에 따라 산 뒤 일주일 만에 +380만 원 → -1천만 원. 영상 코드 없음 — 내레이션 대기 |
| `source/<영상ID>/summary.md` | 영상별 한눈에 보기 (자동 생성: `python tools/make_summary.py`) — 상태·제목·썸네일 프롬프트·설명란·대본(🎙 사연자·진행자). 스토리보드는 넣지 않음 |
| `thumbnail_todo.md` | 이미지가 아직 없는 썸네일의 프롬프트 모음 (자동 생성: `python tools/make_summary.py --thumb-todo stock`) |
| `out/<영상ID>/` | 완성 영상 `final_1080p.mp4` 자리 (용량 때문에 git에 올리지 않음). 스토리보드는 만들지 않음 (사용자 지시 2026-10-10) |

## 분석 다시 돌리기
```
python youtube_topic_analyzer.py --config stock/analyzer_config.toml
```
→ `result/`가 새 결과로 바뀌면 `guides/data_insights.md` 9번 절차로 근거 숫자를 갱신한다.

> 2026-10-09 실행은 키워드 90개 중 40개만 수집됐다 (검색 일일 한도). 남은 50개는 다음 실행 때 이어서 수집된다.
