# gungmin-sigi-2026-10 장면 클립 — Kaggle 셀 (롱폼 29개 + 쇼츠 7개)

버전: v1.0 — 2026-10-20 — 그림 41장 검수 뒤 (커밋 `5a54ce4b`). 코드·설정·그림이 모두 이 커밋에 있다. 셀 설명: `videogen/README.md` 2-4.

## 준비 (처음 한 번)
1. Kaggle 노트북 오른쪽 Settings: **Accelerator = GPU T4 x2**, **Internet = On**
2. **Add-ons → Secrets → `GITHUB_TOKEN` 을 이 노트북에 켬** (내레이션 셀과 같은 토큰) — 클립을 GitHub Release 에 올려 Claude 가 받는다
3. 아래 셀 하나를 붙이고 **Save Version → Save & Run All (Commit)** (브라우저를 닫아도 끝까지 돈다)

## 셀 (고치지 않음)
```python
CODE_REF = "5a54ce4bd131d85f68d26056aa7d784b0ae572cc"   # 그림·설정·코드가 모두 든 커밋
SETTINGS_PATHS = [
    "economic/source/gungmin-sigi-2026-10/scenes/videogen.json",          # 롱폼 29개 (1280x704)
    "economic/source/gungmin-sigi-2026-10/shorts/scenes/videogen.json",   # 쇼츠 7개 (704x1280)
]

import os, sys, json, importlib, urllib.request
REPO = "yeomin1024/yeomin1024-ytb"
SRC = "/kaggle/tmp/videogen_src"
os.makedirs(SRC, exist_ok=True)
def get(path, dst):
    url = f"https://raw.githubusercontent.com/{REPO}/{CODE_REF}/{path}"
    headers, err = [{}], None
    try:
        from kaggle_secrets import UserSecretsClient
        headers.insert(0, {"Authorization": "token " + UserSecretsClient().get_secret("GITHUB_TOKEN")})
    except Exception:
        pass
    for h in headers:
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60) as r:
                open(dst, "wb").write(r.read())
            return dst
        except Exception as e:
            err = e
    raise RuntimeError(f"받기 실패: {url} ({err}) — Internet=On 인지 확인")
get("videogen/videogen.py", f"{SRC}/videogen.py")
sys.path.insert(0, SRC)
import videogen; importlib.reload(videogen)
print("videogen", videogen.__version__)
results = []
for k, path in enumerate(SETTINGS_PATHS, 1):
    S = json.load(open(get(path, f"{SRC}/settings_{k}.json"), encoding="utf-8"))
    S["image_base"] = f"https://raw.githubusercontent.com/{REPO}/{CODE_REF}/"
    S["preview"] = False
    print(f"===== [{k}/{len(SETTINGS_PATHS)}] {path} — 클립 {len(S['start_images'])}개 → Release {S['release_tag']}")
    r = videogen.run(S)
    results.append(r)
    print("RELEASE", r["release"])
print("끝 — Claude 에게 '클립 올렸어'")
```

## 끝난 뒤
- 로그 마지막에 `RELEASE {'ok': True, ...}` 가 두 번 (롱폼·쇼츠) 나오면 Claude 에게 "클립 올렸어" → Claude 가 `python3 tools/scene_clips.py fetch economic gungmin-sigi-2026-10 [--shorts]` 로 받아 합침.
- `ok: False` 이면 클립은 Output 탭 `outputs/<실행시각>/clips/` 에 있다 — 같은 세션에서 `videogen.publish_release(results[0]["clips_manifest"], "clips-gungmin-sigi-2026-10")` (쇼츠는 `results[1]`, `"clips-gungmin-sigi-2026-10-shorts"`).
- 시간: T4 실측 없음 — 처음 설치·5B 모델 받기 약 15~20분 + 클립 36개(약 150초 분량, 1280x704 3-step) 추정 1~2시간. `[SUMMARY] stage timings` 줄을 Claude 에게 알려 주면 다음 추정에 쓴다.
- L02·L19 는 그림을 다시 그리는 중 — 새 그림이 올라오면 그 두 장만 다시 만드는 작은 셀을 따로 준다 (같은 Release 에서 그 두 클립만 바뀜).
