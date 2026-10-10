# 주식 주제 폴더 (`stock/`)

공통 지시사항은 저장소 최상위 `guides/`에 있고, 이 폴더에는 **주식에만 해당하는 것**만 둔다.

| 위치 | 내용 |
|---|---|
| `analyzer_config.toml` | 분석기 설정: 검색 키워드(9개 카테고리·90개), 관련어, 광고 의심 기준 |
| `result/` | 분석 결과 (분석기가 GitHub에 올림 — 직접 고치지 않음) |
| `guides/data_insights.md` | 분석 결과를 지시사항용으로 요약 (분량·제목·소재·썸네일 근거) |
| `guides/script_rules.md` | 주식 대본 규칙: 금액 1억 이하, 투자 유의 4요소, 근거 자료 은행 |
| `guides/title_rules.md` | 주식 제목 규칙: 상시 고민 목록, 기준 제목, 좋음 9개, 숫자 기준값 |
| `guides/thumbnail_rules.md` | 주식 썸네일 규칙: 손실 파랑 고정, 계좌 카드, 가상 인물 사용 |
| `guides/upload_rules.md` | 주식 업로드 규칙: 설명란 필수 고지·출처, 태그 묶음, 스팸 차단 단어 |
| `titles/` | 제목 피드백 시트 (1차 50개 — 표시 완료, 2차 36개 — 표시 전) |
| `source/used_content.md` | 이전 대본과의 중복 방지 목록 |
| `source/molppang-2026-10/` | 몰빵 영상 v2.0: 엔론 5문장 삭제한 대본 TXT·SRT(문장 91 / 자막 117, 문장 18 뒤 고지 공백), README(옛→새 번호 대응표) |
| `source/multagi-2026-10/` | 물타기 영상: 대본 v1.3 TXT·SRT, README(검산·출처), `titles.md`(제목 3개, T1 채택), `thumbnails/`(썸네일 프롬프트 3개), `upload.md`(업로드 시트). SRT: 문장 91 / 자막 110 |
| `source/bittu-2026-10/` | 빚투 영상: 대본 v1.0 TXT·SRT(문장 87 / 자막 104), README(검산·출처), `titles.md`(T1 채택), `thumbnails/`(3개), `upload.md`. 사연: SK하이닉스 2026년 5~7월, 신용 → 반대매매. 영상 제작 전 |
| `source/panicsell-2026-10/` | 패닉셀 영상: 대본 v1.0 TXT·SRT(문장 92 / 자막 109), README(검산·출처), `titles.md`(T1 채택), `thumbnails/`(3개), `upload.md`. 사연: 삼성전자 2026년 3월 폭락 날 전량 매도 → 7주 뒤 +30%. 영상 제작 전 |
| `source/<영상ID>/summary.md` | 영상별 한눈에 보기 (자동 생성: `python tools/make_summary.py`) — 상태·제목·썸네일 프롬프트·설명란·스토리보드·대본 |
| `thumbnail_todo.md` | 이미지가 아직 없는 썸네일의 프롬프트 모음 (자동 생성: `python tools/make_summary.py --thumb-todo stock`) |
| `out/multagi-2026-10/` | 물타기 영상 `scene_plan.md`(장면 구성표), `storyboard/`(장면 still 44장 + `index.html`). 완성 영상 `final_1080p.mp4`는 용량 때문에 git에 올리지 않음 |

## 분석 다시 돌리기
```
python youtube_topic_analyzer.py --config stock/analyzer_config.toml
```
→ `result/`가 새 결과로 바뀌면 `guides/data_insights.md` 9번 절차로 근거 숫자를 갱신한다.

> 2026-10-09 실행은 키워드 90개 중 40개만 수집됐다 (검색 일일 한도). 남은 50개는 다음 실행 때 이어서 수집된다.
