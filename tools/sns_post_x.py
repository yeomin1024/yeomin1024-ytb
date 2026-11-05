#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-05 — 주식 SNS 평가판에서 통과한 X(트위터) 글을 API 로 올리는 도구 (사용자 지시 2026-11-05
#   "일단 트위터로 글 업로드하는 코드 만들고 내가 환경변수로 뭘 넣어야 하는지 받는 방법도 알려줘").
#   · 글 내용 = stock/topics/sns/sns_<날짜>.json → tools/sns_posts.py 의 make() 가 짠 X 본문 글 + 댓글 (손으로 안 씀)
#   · 올리는 순서: 본문 글은 앞 글에 답글로 이어 쓰기(스레드) · 댓글은 첫 글(루트) 아래 답글 — sns_posts.md 의 '올리는 순서' 와 같음
#   · 인증: OAuth 1.0a 사용자 컨텍스트 — 환경 변수 X_API_KEY · X_API_SECRET · X_ACCESS_TOKEN · X_ACCESS_TOKEN_SECRET (표준 라이브러리만)
#   · **안전장치(되돌리기 어려운 바깥 행동)**: 기본은 --dry-run(아무것도 안 올림) · 실제 게시는 --publish 일 때만 ·
#       통과(stock/topics/sns/approved.json 의 "x" 에 그 글 key 와 같은 원본 ver)한 글만 · 원본 ver 이 통과 때와 다르면 거절 ·
#       영상 링크 자리 '(영상 링크' 가 남은 댓글이 있으면 거절(--without-link 로 그 댓글만 뺌) ·
#       올린 기록 stock/topics/sns/posted.json — 이미 올린 글은 다시 안 올림(중간에 끊기면 이어서) · 글자 수(가중 280) 재검사
#   · 비용 참고(2026-11 조사, stock/guides/sns_autopost.md): 글 약 $0.015 · 링크 든 글 $0.20 — 실제 값은 X 개발자 화면에서 확인
#   · 비밀값은 출력·저장 ✗ (헤더도 로그에 안 찍음). 연구·교육용 — 투자 권유가 아님.
# 사용:
#   python3 tools/sns_post_x.py 1                  # 1편 점검만 (dry-run, 올릴 글과 게이트 결과를 보여 줌)
#   python3 tools/sns_post_x.py 1 --check-auth     # 키가 맞는지 GET /2/users/me 한 번 (읽기 1건)
#   python3 tools/sns_post_x.py 1 --publish --without-link   # 실제 게시 (영상 링크 댓글은 뺌)
import argparse
import base64
import hashlib
import hmac
import json
import os
import secrets
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import sns_posts as SP  # noqa: E402  make() · xlen · K8 검사 — 글은 이 도구와 같은 코드로 짬

SRC_DIR = ROOT / "stock/topics/sns"
APPROVED = SRC_DIR / "approved.json"   # {"x": {"e1-x": "v4"}} — 사용자가 판에서 '통과 (올림)' 한 글 key → 통과 때의 원본 ver
POSTED = SRC_DIR / "posted.json"       # {"x": {"e1-x": {"tweets": [{"i": 1, "kind": "post", "id": "...", "at": "..."}]}}}
API = os.environ.get("X_API_BASE", "https://api.x.com")   # 시험용으로만 바꿈 (가짜 서버)
ENV = ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]
GAP_SEC = 1.5


def log(stage, **kv):
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    print(f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def enc(s):
    return urllib.parse.quote(str(s), safe="~")


def oauth_header(method, url, creds):
    """OAuth 1.0a 서명 — JSON 본문은 서명에 넣지 않음(X 규격), 쿼리 없는 URL 만 씀."""
    p = {"oauth_consumer_key": creds["X_API_KEY"], "oauth_nonce": secrets.token_hex(16),
         "oauth_signature_method": "HMAC-SHA1", "oauth_timestamp": str(int(time.time())),
         "oauth_token": creds["X_ACCESS_TOKEN"], "oauth_version": "1.0"}
    base = "&".join([method.upper(), enc(url), enc("&".join(f"{enc(k)}={enc(v)}" for k, v in sorted(p.items())))])
    key = f"{enc(creds['X_API_SECRET'])}&{enc(creds['X_ACCESS_TOKEN_SECRET'])}"
    p["oauth_signature"] = base64.b64encode(hmac.new(key.encode(), base.encode(), hashlib.sha1).digest()).decode()
    return "OAuth " + ", ".join(f'{enc(k)}="{enc(v)}"' for k, v in sorted(p.items()))


def call(method, path, creds, body=None):
    url = API + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": oauth_header(method, url, creds), "Content-Type": "application/json", "User-Agent": "sns-post-x/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode() or "{}")
        except Exception:
            return e.code, {}
    except Exception as e:  # 네트워크 — 어느 단계에서 무엇 때문에 멈췄는지 남김
        return 0, {"error": f"{type(e).__name__}: {e}"}


HINT = {401: "키·토큰이 틀리거나 앱 권한이 'Read and write' 가 아님 — 권한을 바꾼 뒤 Access Token 을 다시 만들어야 함",
        402: "크레딧 없음 — X 개발자 화면에서 크레딧 충전", 403: "권한 부족·중복 글·정책 거절 — 본문 detail 확인",
        429: "한도 초과 — 잠시 뒤 다시", 0: "네트워크 — 이 환경에서 api.x.com 이 허용되는지(read_documentation environment.network) 확인"}


def load(p):
    try:
        return json.loads(p.read_text("utf-8"))
    except FileNotFoundError:
        return {}


def build(ep_no, without_link):
    srcs = sorted(SRC_DIR.glob("sns_*.json"))
    D = json.loads(srcs[-1].read_text("utf-8"))
    ep = next((e for e in D["episodes"] if e["ep"] == ep_no), None)
    if ep is None:
        raise SystemExit(f"[ERROR] {ep_no}편이 {srcs[-1].name} 에 없음")
    out = SP.make(ep, D.get("video_link", "(영상 링크)"))
    posts, comments = out["x"]
    problems = SP.check(ep, out)
    if without_link:
        comments = [c for c in comments if "(영상 링크" not in c]
    return D, posts, comments, problems


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("ep", type=int, help="편 번호 (1~4)")
    ap.add_argument("--publish", action="store_true", help="실제로 올림 (없으면 dry-run)")
    ap.add_argument("--without-link", action="store_true", help="영상 링크 자리가 남은 댓글을 빼고 올림")
    ap.add_argument("--check-auth", action="store_true", help="키 확인만 (GET /2/users/me)")
    a = ap.parse_args(argv)
    key = f"e{a.ep}-x"
    creds = {k: os.environ.get(k, "") for k in ENV}
    missing = [k for k in ENV if not creds[k]]

    if a.check_auth:
        if missing:
            log("ERROR", where="auth", missing=",".join(missing), next="환경 변수 4개를 넣은 새 세션에서 다시 (stock/guides/sns_autopost.md '이용 준비')")
            return 1
        st, js = call("GET", "/2/users/me", creds)
        log("AUTH", status=st, user=(js.get("data") or {}).get("username", ""), hint=HINT.get(st, "") if st != 200 else "ok")
        return 0 if st == 200 else 1

    D, posts, comments, problems = build(a.ep, a.without_link)
    ver = D.get("ver", "v1")
    approved = (load(APPROVED).get("x") or {}).get(key)
    posted = (load(POSTED).get("x") or {}).get(key, {}).get("tweets", [])
    gates = []
    if approved is None:
        gates.append(f"통과 기록 없음 — 판에서 '통과 (올림)' 한 글만 올림 (approved.json 의 x.{key})")
    elif approved != ver:
        gates.append(f"통과는 {approved} 때인데 원본이 {ver} 로 바뀜 — 판에서 다시 통과를 받아야 함")
    for k, c in enumerate(posts + comments, 1):
        if "(영상 링크" in c:
            gates.append(f"글 {k} 에 영상 링크 자리가 남음 — 영상을 올린 뒤 video_link 를 채우거나 --without-link")
    gates += problems
    log("PLAN", key=key, ver=ver, approved=str(approved), posts=len(posts), comments=len(comments), already_posted=len(posted),
        weighted_max=max(SP.xlen(t) for t in posts + comments), mode="PUBLISH" if a.publish else "dry-run", gates=len(gates))
    for g in gates:
        log("GATE", blocked=g)
    seq = [("post", t) for t in posts] + [("comment", t) for t in comments]
    for n, (kind, t) in enumerate(seq, 1):
        log("TWEET", n=n, kind=kind, weighted=SP.xlen(t), done=n <= len(posted), head=t.split("\n")[0][:40])
    if not a.publish:
        log("DONE", wrote=False, note="dry-run — 아무것도 올리지 않음. 실제 게시는 --publish")
        return 1 if gates else 0
    if gates:
        log("STOP", reason="게이트 통과 못 함 — 올리지 않음")
        return 1
    if missing:
        log("ERROR", where="env", missing=",".join(missing), next="환경 변수 4개 필요 — stock/guides/sns_autopost.md")
        return 1

    # 실제 게시 — 한 글마다 기록(끊겨도 이어서)
    rec = load(POSTED)
    ent = rec.setdefault("x", {}).setdefault(key, {"ver": ver, "tweets": []})
    done = ent["tweets"]
    root = next((t["id"] for t in done if t["kind"] == "post" and t["i"] == 1), None)
    prev = next((t["id"] for t in reversed(done) if t["kind"] == "post"), None)
    prev_c = next((t["id"] for t in reversed(done) if t["kind"] == "comment"), None)
    new = 0
    for n, (kind, text) in enumerate(seq, 1):
        if n <= len(done):
            continue
        body = {"text": text}
        parent = prev if kind == "post" else (prev_c or root)
        if n > 1 and parent:
            body["reply"] = {"in_reply_to_tweet_id": parent}
        st, js = call("POST", "/2/tweets", creds, body)
        tid = (js.get("data") or {}).get("id")
        if st not in (200, 201) or not tid:
            log("FAIL", n=n, status=st, detail=json.dumps(js, ensure_ascii=False)[:300], hint=HINT.get(st, ""), next="고친 뒤 같은 명령을 다시 — 올린 글은 건너뜀")
            POSTED.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", "utf-8")
            return 1
        done.append({"i": n if kind == "post" else n - len(posts), "kind": kind, "id": tid, "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
        if kind == "post":
            root, prev = root or tid, tid
        else:
            prev_c = tid
        POSTED.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", "utf-8")
        new += 1
        log("POSTED", n=n, kind=kind, id=tid)
        time.sleep(GAP_SEC)
    log("DONE", wrote=new > 0, new=new, tweets=len(done), root=root)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
