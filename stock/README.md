# 주식 주제 폴더 (`stock/`) — 새로 시작 (2026-10-12)

공통 지시사항은 저장소 최상위 `guides/`에 있고, 이 폴더에는 **주식에만 해당하는 것**만 둔다.
※ 투자 교육용 콘텐츠다. 투자 권유가 아니다.

2026-10-12 사용자 지시로 옛 주식 폴더를 `stock_backup/`(⏸ 백업)으로 옮기고 이 폴더를 새로 만들었다:
"기존 주제폴더 _backup 붙여서 백업해놓고 stock만 새로 만들어서 유튜브 성공사례 분석 코드 돌려서 분석 결과 파일 만들고
성공사례 분석(대본 내용, 댓글 반응 등 영상의 여러 정보 참고)해서 각 지시사항 파일 새로 만들고 오디오 생성 전 단계까지 결과물 만들어봐"

- 옛 영상 4개(빚투·몰빵·물타기·패닉셀)는 채널에 올라가 있다 → 기록·통계는 `stock_backup/source/<영상ID>/`, 피드백 자료는 `python3 tools/youtube_feedback.py stock_backup`.
- 새 영상은 옛 영상과 내용이 겹치지 않게 만든다 (`source/used_content.md` — 옛 영상 사용 내용을 이어받음).

| 위치 | 내용 |
|---|---|
| `analyzer_config.toml` | 분석기 설정 v2.0 (새로 만듦): 키워드 9개 그룹 × 5개 = 45개 — 사연·특징/패턴·심리·노후·ETF 장기투자·빚투·사기·실험·시장 급락 |
| `result/` | 분석기 결과 (실행 `20261012_204952`, 영상 1,589개) — 직접 고치지 않음 |
| `result/outliers/` | 작은 채널 성공 사례 (`tools/outlier_research.py`, 2026-10-12 — 복구본: `summary.md` 맨 위 설명) |
| `guides/data_insights.md` | **v3.0** 분석 정리: 성공 사례 33개 형식, 제목 요소(작은 채널 437개), 길이(4~8분 7%), 챕터 구성, 댓글 1,103개의 시청자 니즈, 사용자 결정 필요 4개 |
| `guides/script_rules.md` | **v2.0** 대본: "망하는 과정형"(사연 20~30초 → 진행자 → 고지 → 단계 4~5개 → 장치 4~5개 → 마무리), 10~12분, 1억 이하, 근거 자료 은행 |
| `guides/title_rules.md` | **v2.1** 제목: 우선 소재 3개, 기준 제목·좋음 9개(사용자), "과정·벌어진 일"은 T2에서만 시험 |
| `guides/thumbnail_rules.md` | v2.0 썸네일 (규칙은 옛 v1.3 그대로 — 이번 수집은 썸네일을 못 받음) |
| `guides/upload_rules.md` | v2.0 업로드: AI 음성 안내 한 줄, 챕터 = 단계 이름 |
| `source/used_content.md` | 중복 방지 목록 (옛 영상 5개 + 새 영상) |
| `source/pandon-2026-10/` | **판돈 키우기** v1.0: 사연 알테오젠 2024-12 ~ 2026-01, 500만 원 → +285만 원 → 판돈 6,000만 원(12배) → 계약 실망 하루 -22.35% → -1,288만 원. 문장 125 / 자막 144, 고지 공백 문장 17 뒤, 사연 5문장·124음절 ≈ 28초, 추정 11:32. 제목 3개(T1 채택), 썸네일 프롬프트 3개, 업로드 시트, 요약 — **오디오 대기** |
| `source/bonjeon-2026-10/` | **손절·본전 심리** — 작성 중 |
| `source/jisu-2026-10/` | **장기투자 이탈** — 작성 중 |
| `source/<영상ID>/summary.md` | 영상별 한눈에 보기 (자동: `python tools/make_summary.py stock <영상ID>`) |

## 다음 할 일
1. 내레이션(사용자, Kaggle 셀 하나): `guides/tts_guide.md` 3번 — 새 영상 3개의 `narration.mp3`가 대본 폴더에 올라온다.
2. "오디오 올렸어" → 영상 코드·렌더·비공개 업로드 (`guides/pipeline.md` 4단계).
3. 다음 할당량에 `python3 tools/outlier_research.py stock --per-group 2 --top 20` → `python3 tools/outlier_stats.py stock` (지워진 `candidates.csv` 복구, `data_insights.md` 6번).

## 분석 다시 돌리기
```
bash tools/run_analysis.sh stock                                  # 분석기 (클라우드, v1.1부터 result/outliers 보존)
python3 tools/outlier_research.py stock --per-group 2 --top 20    # 작은 채널 성공 사례 (약 3,700단위)
python3 tools/outlier_stats.py stock --skip-ranks 1,7,11,13,15    # data_insights 숫자 다시 계산
```
같은 키의 하루 10,000단위를 나눠 쓴다 (2026-10-12: 성공 사례 3,653 + 분석기 5,833).
