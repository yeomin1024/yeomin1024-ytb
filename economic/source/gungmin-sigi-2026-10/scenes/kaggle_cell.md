# gungmin-sigi-2026-10 장면 클립 — Kaggle 고정 셀 (롱폼 29개 + 쇼츠 7개)

버전: v2.0 — 2026-10-20 — **고정 셀** (사용자 지시 "kaggle 영상 클립 코드 내가 실행 셀 변경 안해도 파일 읽어서 처리하게 해줘 셀 코드 알려주고", videogen v1.5.0). 무엇을 만들지는 저장소 `videogen/queue.json` 이 정한다 — 지금은 이 영상 롱폼·쇼츠 두 작업. 셀 설명 `videogen/README.md` 2-5.
이전 v1.0 — 2026-10-20 — 커밋 `5a54ce4b` 를 적은 셀 (그림이 바뀌면 셀을 고쳐야 했음).

## 준비 (노트북 하나에 처음 한 번)
1. Kaggle 노트북 오른쪽 Settings: **Accelerator = GPU T4 x2**, **Internet = On**
2. **Add-ons → Secrets → `GITHUB_TOKEN` 을 이 노트북에 켬** (내레이션 셀과 같은 토큰) — 클립을 GitHub Release 에 올려 Claude 가 받는다
3. 아래 셀 하나를 붙이고 **Save Version → Save & Run All (Commit)** (브라우저를 닫아도 끝까지 돈다)

## 셀 (고치지 않음 — 다음 영상에도 그대로)
```python
# 고치지 않는 셀 — 무엇을 만들지는 저장소 videogen/queue.json 이 정함 (Claude 가 고침)
import os, sys, json, importlib, urllib.request
REPO = "yeomin1024/yeomin1024-ytb"
SRC = "/kaggle/tmp/videogen_src"
os.makedirs(SRC, exist_ok=True)
def _token():
    try:
        from kaggle_secrets import UserSecretsClient
        return UserSecretsClient().get_secret("GITHUB_TOKEN")
    except Exception:
        return os.environ.get("GITHUB_TOKEN")
def _get(url):
    t, err = _token(), None
    for h in ([{"Authorization": "token " + t}] if t else []) + [{}]:
        try:
            req = urllib.request.Request(url, headers=dict(h, **{"User-Agent": "videogen-cell"}))
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            err = e
    raise RuntimeError(f"받기 실패: {url} ({err}) — Settings 에서 Internet = On 인지 확인")
try:
    SHA = json.loads(_get(f"https://api.github.com/repos/{REPO}/commits/main"))["sha"]
except Exception as e:
    print("main 커밋을 못 읽음 — main 그대로 씀:", e)
    SHA = "main"
open(f"{SRC}/videogen.py", "wb").write(_get(f"https://raw.githubusercontent.com/{REPO}/{SHA}/videogen/videogen.py"))
sys.path.insert(0, SRC)
import videogen; importlib.reload(videogen)
print("videogen", videogen.__version__, "commit", SHA[:12])
result = videogen.run_queue(ref=SHA)
```

## 실행하면
- 로그 처음: `[QUEUE] job 1/2 name="gungmin-sigi-2026-10 롱폼" clips=29 todo=29 ...` · `job 2/2 ... 쇼츠 clips=7 todo=7`.
- 끝: `[QUEUE] result ... release_ok=True` 두 줄 + `done — tell Claude '클립 올렸어'` → Claude 에게 "클립 올렸어" → Claude 가 `python3 tools/scene_clips.py fetch economic gungmin-sigi-2026-10 [--shorts]` 로 받아 합침.
- **L02·L19 그림을 다시 그려 올린 뒤엔 같은 셀을 다시 실행만** — `todo=2 ... L02(image_sha256 changed),L19(image_sha256 changed)` 로 그 두 클립만 만들고 Release 에서 그 둘만 바뀐다 (쇼츠는 `todo=0`, 다른 27개는 그대로·같은 seed).
- 이미 다 올라간 뒤 다시 실행하면 `nothing to make` — 설치 없이 1분 안에 끝남.
- `release_ok=False` 이면 클립은 Output 탭 `outputs/<실행시각>/clips/` 에 있다 — 같은 세션에서 `videogen.publish_release(result["jobs"][0]["manifest"], "clips-gungmin-sigi-2026-10")` (쇼츠는 `jobs[1]`, `"clips-gungmin-sigi-2026-10-shorts"`).
- 시간: T4 실측 없음 — 처음 설치·5B 모델 받기 약 15~20분 + 클립 36개(약 150초 분량, 1280x704 3-step) 추정 1~2시간. `[SUMMARY] stage timings` 줄을 Claude 에게 알려 주면 다음 추정에 쓴다.
