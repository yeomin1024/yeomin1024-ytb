# SNS 자동 게시 조사 — X · 스레드 · 틱톡 · 인스타 (2026-11-05)

VERSION: v1.0 — 2026-11-05 — 사용자 지시 "트위터, 스레드, 틱톡, 인스타 자동으로 올릴 수 있는지도 알아봐". **조사만 — 키·앱 만들기·게시는 아직 아무것도 안 함.**
※ 출처 대부분이 제3자 블로그라 숫자는 참고용 — 실제 값은 각 공식 문서(아래 링크)에서 만들기 직전에 다시 확인. 연구·교육용 — 투자 권유 아님.

## 한눈에
| 플랫폼 | 자동 게시 | 글(텍스트) | 이어 쓰기 | 막히는 곳 |
|---|---|---|---|---|
| X | 가능 (API) | ✅ | ✅ 답글로 잇기 | **유료 종량제** — 글 약 $0.015, **링크가 든 글 $0.20** (무료 단계 사실상 없음) |
| 스레드 | 가능 (Threads API) | ✅ | ✅ `reply_to_id` | 앱 심사(권한 `threads_content_publish`) · 하루 250글 |
| 인스타 | 가능 (Graph API) | ❌ 글만은 안 됨 — **그림·영상 필요** | 캐러셀 | **비즈니스 계정**(크리에이터 ✗) · 앱 심사(`instagram_business_content_publish`) · 하루 100건 |
| 틱톡 | 가능 (Content Posting API) | ❌ **영상(·사진)만** | — | **감사(audit) 전엔 비공개로만** 올라감 · 감사 전 하루 5명 |

## 플랫폼별
- **X**: 종량제. 글 하나 약 $0.015, URL 이 든 글 $0.20, 읽기 $0.005/건(여러 블로그 일치, X 문서로 재확인 필요). `POST /2/tweets` 하루 10,000·15분 100. 우리 글은 **영상 링크가 첫 댓글 2**에 있어 편마다 링크 글 1개 = $0.20 — 4편 × (본문 4 + 댓글 2) 를 다 올려도 몇 달러 수준. 인증 = OAuth 2.0 (사용자 대신 올림).
- **스레드**: Meta 공식 — 24시간에 API 글 250개(답글은 따로 1,000개). 이어 쓰기 = 앞 글 ID 를 `reply_to_id` 로. 사용 한도 확인 `GET /{id}/threads_publishing_limit`. 개인 계정도 됨, 앱 심사 필요.
- **인스타**: Meta 공식 — 24시간에 100건(캐러셀은 1건). 텍스트 전용 게시 없음 → 문항 글을 **그림 카드**로 만들거나 **릴스(영상)** 로. 릴스는 쇼츠 mp4 를 그대로 쓸 수 있음(H.264 MP4·길이 제한 있음). 비즈니스 계정 필요, 권한 심사 2~4주 추정.
- **틱톡**: Content Posting API 는 영상/사진만. **감사 전에는 올린 것이 전부 '나만 보기'**, 감사 전 하루 5명까지 · 계정당 하루 약 15개. 공개 게시하려면 틱톡 감사 통과가 먼저.

## 우리 파이프라인에 맞추면
- **글 중심(지금 평가판)** = X · 스레드가 맞음. 인스타·틱톡은 글이 아니라 **영상/그림** 플랫폼이라 지금 SNS 글(텍스트)은 못 올림.
- **쇼츠 mp4 가 이미 있다** → 인스타 릴스 · 틱톡 · (유튜브 쇼츠는 이미 `tools/youtube_upload.py`) 에 같은 영상 재사용이 가장 쉬운 길. 단 틱톡은 감사 전 비공개.
- 제안 순서: ① **스레드**(무료·글·이어 쓰기 — 가장 쉬움) → ② **X**(과금 설정 필요) → ③ 인스타 릴스(비즈니스 계정·심사) → ④ 틱톡(감사). 시작 전에 사용자가 할 일: 개발자 앱 만들기(X Developer·Meta for Developers·TikTok for Developers), 계정 연결, 키를 **환경 변수**로(저장소에 올리지 않음).

## 지켜야 할 것
- **올리는 건 되돌리기 어려운 바깥 행동** — 게시 도구는 `--dry-run` 이 기본, 실제 게시는 **판정 '통과 (올림)' 인 글만**, 사용자가 시킬 때만 (`youtube_upload.py` 와 같은 길). 통과 안 된 글·`(영상 링크 — 올린 뒤 채움)` 자리 그대로인 글은 막음.
- 같은 글을 두 번 올리지 않도록 올린 기록(`stock/topics/sns/posted.json`: 플랫폼·글 번호·ID·시각)을 남기고 먼저 읽음.
- 비밀값은 커밋·출력 ✗. 외국어 버전은 통과 글에서만 (`board_4_sns.md` 2-1번).
- 이 환경에서 API 호출이 되는지(아웃바운드 허용 목록)는 만들 때 `read_documentation environment.network` 로 확인.

## 출처 (확인일 2026-11-05)
X 가격: [outstand.so](https://www.outstand.so/blog/x-api-pricing) · [postproxy.dev](https://postproxy.dev/blog/x-api-pricing-2026/) · 스레드: [Meta 문서](https://developers.facebook.com/docs/threads/overview) · [답글 관리](https://developers.facebook.com/docs/threads/retrieve-and-manage-replies) · 인스타: [Meta 문서](https://developers.facebook.com/docs/instagram-platform/content-publishing) · 틱톡: [콘텐츠 공유 지침](https://developers.tiktok.com/doc/content-sharing-guidelines)
