# SNS 자동 게시 조사 — X · 스레드 · 틱톡 · 인스타 (2026-11-05)

VERSION: v1.1 — 2026-11-05 — v1.0 조사(사용자 지시 "트위터, 스레드, 틱톡, 인스타 자동으로 올릴 수 있는지도 알아봐") + **X 올리기 도구 `tools/sns_post_x.py` · 이용 준비(아래 '## X 이용 준비')**. 키·실제 게시는 아직 안 함(가짜 서버로만 시험).
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

## X 이용 준비 (사용자가 할 일 — 키는 채팅에 붙이지 않음)
1. **X 개발자 계정·앱 만들기**: developer.x.com 에 올릴 X 계정으로 로그인 → 개발자 포털에서 프로젝트·앱 생성. 요금은 종량제 — **크레딧 충전**(카드 등록)이 있어야 올라감(402 면 크레딧 없음). 가격은 개발자 화면에서 확인.
2. **앱 권한을 'Read and write' 로 먼저 바꾸기**: 앱 설정 → User authentication settings → App permissions = *Read and write*, (App type = Web App/Automated App, 콜백 URL 칸은 아무 https 주소). ⚠️ **권한을 바꾼 뒤에** 3번의 Access Token 을 만들어야 쓰기가 됨(읽기 전용으로 만든 토큰은 401·403).
3. **키 4개 받기**: 앱의 *Keys and tokens* 탭 → ① *API Key* ② *API Key Secret* (Consumer Keys) · ③ *Access Token* ④ *Access Token Secret* (Authentication Tokens → Generate — 'Created with Read and Write permissions' 라고 떠야 함). 비밀값은 만든 때 한 번만 보이니 바로 복사.
4. **클라우드 환경에 넣기**: Claude Code 클라우드 환경 메뉴(세션 제목 줄) → Edit → **환경 변수**(또는 Network secrets/API credentials 칸이 있으면 그쪽) 에 아래 4개 이름 그대로 — **새 세션부터 적용**(지금 세션엔 안 보임). 채팅·저장소에는 붙이지 않음.

| 환경 변수 | 3번의 어느 값 |
|---|---|
| `X_API_KEY` | API Key (Consumer Key) |
| `X_API_SECRET` | API Key Secret |
| `X_ACCESS_TOKEN` | Access Token |
| `X_ACCESS_TOKEN_SECRET` | Access Token Secret |

5. **새 세션에서 확인**: `python3 tools/sns_post_x.py 1 --check-auth` → `status=200 user="내계정"` 이면 연결 성공(읽기 1건 비용). 401 = 키·토큰 오타 또는 권한 문제, 402 = 크레딧, `where="auth" missing=…` = 환경 변수가 안 들어감.

## X 올리기 — `tools/sns_post_x.py` (v1.0)
```bash
python3 tools/sns_post_x.py 1                       # dry-run — 올릴 글·게이트 결과만 (기본)
python3 tools/sns_post_x.py 1 --publish --without-link   # 실제 게시 (영상 링크 댓글은 뺌)
```
- 글 = `tools/sns_posts.py` 가 짠 X 본문(앞 글에 답글로 이어 쓰기) + 댓글(첫 글 아래 답글). 손으로 쓰지 않음.
- **게이트(하나라도 걸리면 올리지 않음)**: ① `stock/topics/sns/approved.json` 의 `x.<e1-x>` 에 **통과 때의 원본 ver** 가 있어야 함 (지금 `e1-x = v4` — 사용자가 판에서 통과시킨 글만, 사용자가 통과라고 말할 때만 Claude 가 적음) ② 원본 ver 이 통과 때와 다르면 거절(피드백으로 글이 바뀜 → 다시 통과) ③ `(영상 링크` 자리가 남은 글이 있으면 거절(영상이 올라가면 `video_link` 를 채움, 아니면 `--without-link`) ④ 글자 수(가중 280)·권유 낱말·케이스 수치 검사.
- **중복 방지**: 한 글씩 올릴 때마다 `stock/topics/sns/posted.json` 에 ID 를 적고, 다시 돌리면 올린 글은 건너뜀(중간에 429 등으로 끊겨도 같은 명령으로 이어서). X 도 같은 글을 거절함.
- **시험**: `X_API_BASE=http://127.0.0.1:<포트>` 로 가짜 서버를 두면 실제 X 에 안 올라감(2026-11-05 시험 — 서명 헤더·답글 잇기·429 뒤 이어 올리기·재실행 중복 없음 확인). 시험 뒤 `posted.json` 은 지움(가짜 ID).
- 실제 게시는 **되돌리기 어려운 바깥 행동** — Claude 는 사용자가 "올려" 라고 한 뒤에만 `--publish`, 올리기 전에 dry-run 결과를 보여 줌.

## 출처 (확인일 2026-11-05)
X 가격: [outstand.so](https://www.outstand.so/blog/x-api-pricing) · [postproxy.dev](https://postproxy.dev/blog/x-api-pricing-2026/) · 스레드: [Meta 문서](https://developers.facebook.com/docs/threads/overview) · [답글 관리](https://developers.facebook.com/docs/threads/retrieve-and-manage-replies) · 인스타: [Meta 문서](https://developers.facebook.com/docs/instagram-platform/content-publishing) · 틱톡: [콘텐츠 공유 지침](https://developers.tiktok.com/doc/content-sharing-guidelines)
