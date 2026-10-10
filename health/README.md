# 건강 주제 폴더 (`health/`)

공통 지시사항은 저장소 최상위 `guides/`에 있고, 이 폴더에는 **건강에만 해당하는 것**만 둔다. 구조는 `stock/`과 같다.
※ 건강 정보 제공용 콘텐츠다. 의사의 진단·치료를 대신하지 않는다.

| 위치 | 내용 |
|---|---|
| `analyzer_config.toml` | 분석기 설정: 검색어 48개(혈당·당뇨 / 간·혈압·콜레스테롤 / 검진·나이대 / 영양제·약 / 노화·통증 / 습관·몸의 신호), 관련어·제외어 |
| `guides/script_rules.md` | 건강 대본 규칙: 시청자, 재구성 사연, 고지 카드 "의학적 진단이 아닙니다", 출처·숫자 규칙, 마무리 인사, 근거 자료 은행 |
| `guides/title_rules.md` | 건강 제목 규칙: 수치 반전(결과지 숫자), 결말 장치, 금지 표현 |
| `guides/thumbnail_rules.md` | 건강 썸네일 규칙: 색 의미(위험=빨강, 좋아짐=파랑), 결과지 그리기, 인물·의료 이미지 제한 |
| `guides/upload_rules.md` | 건강 업로드 규칙: 설명란 출처·고지, 태그, 의료 상담 댓글 응대 |
| `guides/data_insights.md` | (임시) 자동완성 검색 수요 근거. 분석기를 돌리면 갱신 |
| `source/used_content.md` | 이전 대본과의 중복 방지 목록 |
| `source/prediabetes-2026-10/` | 당뇨 전단계 영상: 대본 TXT·SRT(문장 86 / 자막 103), README(검산·출처), `titles.md`, `thumbnails/`, `upload.md` — 영상(Remotion)은 아직 |

## 분석 돌리기
```
python youtube_topic_analyzer.py --config health/analyzer_config.toml
```
