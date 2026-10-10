# 사연을 통한 교훈 주제 폴더 (`story/`)

공통 지시사항은 저장소 최상위 `guides/`에 있고, 이 폴더에는 **사연·교훈 주제에만 해당하는 것**만 둔다. 구조는 `stock/`과 같다.

> ⏸ **보류 (사용자 지시 2026-10-10):** 분석 결과가 나오기 전에는 이 주제의 대본을 만들지 않는다. 지금은 분석 설정과 제목·썸네일·업로드 규칙 초안만 있다. 대본 규칙(`guides/script_rules.md`), 중복 방지 목록, 첫 영상은 아직 없다.

| 위치 | 내용 |
|---|---|
| `analyzer_config.toml` | 분석기 설정: 검색어 48개(가족 갈등 / 돈·배신·결혼 후회 / 인생 후회 / 인간관계 / 사연 포맷 / 사이다·감동), 관련어·제외어 |
| `guides/title_rules.md` | 제목 규칙: 관계 + 금액 반전, 결말 장치, 금지 표현 |
| `guides/thumbnail_rules.md` | 썸네일 규칙: 색 의미, 인물(가상)·관계 장면, 실존 문서 서식 금지 |
| `guides/upload_rules.md` | 업로드 규칙: 설명란 고지·출처, 댓글 응대 |
| `guides/data_insights.md` | (임시) 자동완성 검색 수요 근거. 분석기를 돌리면 갱신 |

## 분석 돌리기
```
python youtube_topic_analyzer.py --config story/analyzer_config.toml
```
