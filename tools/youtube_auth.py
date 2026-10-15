#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-15 — 권한에 Google Drive(drive) 추가 (사용자 지시 "구글 드라이브 내 드라이브에 youtube 폴더에 … 원본 영상 올리고 pc에서
#          영상 및 환경설정을 받아서 업로드" — tools/drive_videos.py·tools/pc_upload.py), --save-env .env 로 PC 의 .env 에 바로 저장
# (v1.1 — 2026-10-11 — 권한에 yt-analytics.readonly 추가 (tools/youtube_feedback.py 의 시청 지속·유입 경로 등 상세 분석), 발급 뒤 허용되지 않은 권한 경고)
#          (v1.0: 유튜브 업로드용 OAuth 리프레시 토큰을 한 번 발급 (사용자 PC에서 실행, 표준 라이브러리만))
r"""
유튜브 자동 업로드(tools/youtube_upload.py)에 필요한 "리프레시 토큰"을 한 번만 발급합니다.
**클라우드가 아니라 내 PC에서** 실행합니다 (브라우저로 내 유튜브 계정에 로그인해야 하므로).

  python youtube_auth.py --client-id <클라이언트 ID> --client-secret <클라이언트 보안 비밀번호>
  (또는 환경변수 YOUTUBE_CLIENT_ID / YOUTUBE_CLIENT_SECRET)

준비 (guides/pipeline.md "처음 한 번 할 일" 2번):
  1) Google Cloud 콘솔에서 프로젝트 만들기 → "YouTube Data API v3" 사용 설정
     (통계 피드백 tools/youtube_feedback.py 를 쓰려면 같은 프로젝트에서 "YouTube Analytics API"도 사용 설정)
     (영상 원본을 Google Drive 로 주고받으려면 같은 프로젝트에서 "Google Drive API"도 사용 설정 — v1.2)
  2) OAuth 동의 화면: 외부(External) → 내 구글 계정을 테스트 사용자로 추가 → **게시 상태를 "프로덕션"으로**
     (테스트 상태로 두면 리프레시 토큰이 7일 뒤 만료됩니다. 프로덕션이어도 나 혼자 쓰면 Google 검토 없이 쓸 수 있고,
      로그인 때 "확인되지 않은 앱" 경고가 나오면 고급 → 이동을 누릅니다)
  3) 사용자 인증 정보 → OAuth 클라이언트 ID → 애플리케이션 유형 "데스크톱 앱" → 클라이언트 ID·보안 비밀번호 복사

실행하면 브라우저가 열립니다 → 영상을 올릴 유튜브 채널의 구글 계정으로 로그인·허용 (권한 체크 칸이 나오면 모두 체크)
→ 터미널에 YOUTUBE_REFRESH_TOKEN 값이 나옵니다. 이 값과 클라이언트 ID·비밀번호를
  Claude Code 클라우드 환경 설정(Network secrets 또는 환경 변수)에 넣습니다. **채팅창에는 붙여 넣지 마세요.**
"""
import argparse
import base64
import hashlib
import http.server
import json
import os
import secrets
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
# 업로드(videos.insert), 썸네일(thumbnails.set), 자막(captions.insert)에 필요한 권한 + 통계 읽기(youtube_feedback.py: YouTube Analytics API)
# 동의 화면에 권한 체크 칸이 나오면 모두 체크한다 (하나라도 빼면 그 기능만 403 — 예: 자막 업로드, 상세 분석)
# + 영상 원본 주고받기(tools/drive_videos.py — 내 드라이브/youtube/<주제>/, 사용자가 만든 폴더도 써야 해서 drive) — v1.2
SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube.force-ssl",
          "https://www.googleapis.com/auth/yt-analytics.readonly", "https://www.googleapis.com/auth/drive"]


class _Handler(http.server.BaseHTTPRequestHandler):
    result = {}

    def do_GET(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        _Handler.result = {k: v[0] for k, v in q.items()}
        ok = "code" in q
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        msg = "인증 완료 — 이 창을 닫고 터미널을 보세요." if ok else f"인증 실패: {_Handler.result.get('error', '알 수 없음')}"
        self.wfile.write(f"<html><body style='font-family:sans-serif;padding:40px'><h2>{msg}</h2></body></html>".encode("utf-8"))

    def log_message(self, *_):  # 서버 로그 숨김
        pass


def save_env(path, values):
    """.env 의 KEY= 줄을 새 값으로 (없으면 끝에 더함). 다른 줄·주석은 그대로."""
    p = Path(path)
    lines = p.read_text("utf-8-sig").splitlines() if p.is_file() else []
    done = set()
    for i, ln in enumerate(lines):
        k = ln.split("=", 1)[0].strip()
        if k in values and not ln.lstrip().startswith("#"):
            lines[i] = f"{k}={values[k]}"
            done.add(k)
    lines += [f"{k}={v}" for k, v in values.items() if k not in done]
    p.write_text("\n".join(lines) + "\n", "utf-8")


def main():
    ap = argparse.ArgumentParser(description="유튜브 업로드용 리프레시 토큰 발급 (내 PC에서 한 번)")
    ap.add_argument("--client-id", default=os.environ.get("YOUTUBE_CLIENT_ID", ""))
    ap.add_argument("--client-secret", default=os.environ.get("YOUTUBE_CLIENT_SECRET", ""))
    ap.add_argument("--save-env", default=None, help="이 .env 파일에 YOUTUBE_CLIENT_ID·SECRET·REFRESH_TOKEN 을 저장 (있던 줄은 바꿈, 다른 줄은 그대로)")
    a = ap.parse_args()
    if not a.client_id or not a.client_secret:
        sys.exit("[AUTH] ❌ --client-id 와 --client-secret 이 필요합니다 (Google Cloud 콘솔 → 사용자 인증 정보 → 데스크톱 앱 OAuth 클라이언트)")

    server = http.server.HTTPServer(("127.0.0.1", 0), _Handler)       # 빈 포트 자동 선택 (루프백)
    redirect = f"http://127.0.0.1:{server.server_port}"
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    state = secrets.token_urlsafe(16)
    url = AUTH_URL + "?" + urllib.parse.urlencode({
        "client_id": a.client_id, "redirect_uri": redirect, "response_type": "code", "scope": " ".join(SCOPES),
        "access_type": "offline", "prompt": "consent", "code_challenge": challenge, "code_challenge_method": "S256",
        "state": state})
    print("[AUTH] 브라우저에서 유튜브 채널의 구글 계정으로 로그인하고 허용하세요.")
    print(f"[AUTH] 브라우저가 열리지 않으면 이 주소를 직접 여세요:\n{url}\n")
    threading.Thread(target=server.handle_request, daemon=True).start()
    webbrowser.open(url)
    try:
        while not _Handler.result:
            threading.Event().wait(0.3)
    except KeyboardInterrupt:
        sys.exit("[AUTH] 취소했습니다.")
    r = _Handler.result
    if r.get("state") != state or "code" not in r:
        sys.exit(f"[AUTH] ❌ 인증 실패: {r.get('error', 'state 불일치')} → 다시 실행하세요")

    body = urllib.parse.urlencode({"code": r["code"], "client_id": a.client_id, "client_secret": a.client_secret,
                                   "redirect_uri": redirect, "grant_type": "authorization_code",
                                   "code_verifier": verifier}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(TOKEN_URL, data=body), timeout=30) as resp:
            tok = json.load(resp)
    except urllib.error.HTTPError as e:
        sys.exit(f"[AUTH] ❌ 토큰 교환 실패 ({e.code}): {e.read().decode(errors='replace')[:300]}")
    if "refresh_token" not in tok:
        sys.exit("[AUTH] ❌ 리프레시 토큰이 오지 않았습니다 → https://myaccount.google.com/permissions 에서 이 앱 권한을 지우고 다시 실행")

    granted = set((tok.get("scope") or "").split())
    missing = [s.rsplit("/", 1)[-1] for s in SCOPES if s not in granted]
    if missing:   # 동의 화면에서 체크를 뺀 권한 — 그 기능만 403 이 난다
        print(f"[AUTH] ⚠️ 허용되지 않은 권한: {', '.join(missing)} → 그 기능은 안 됩니다 (자막 업로드: youtube.force-ssl, "
              "통계 상세 분석: yt-analytics.readonly, 영상 원본 Drive: drive). 모두 쓰려면 다시 실행해서 체크 칸을 모두 체크하세요.\n")
    if a.save_env:
        save_env(a.save_env, {"YOUTUBE_CLIENT_ID": a.client_id, "YOUTUBE_CLIENT_SECRET": a.client_secret,
                              "YOUTUBE_REFRESH_TOKEN": tok["refresh_token"]})
        print(f"[AUTH] 💾 {a.save_env} 에 저장했습니다 (PC 업로더가 씀). 클라우드 환경에도 같은 값을 넣어야 Claude 가 Drive 에 영상을 올립니다.\n")
    print("[AUTH] ✅ 발급 완료. 아래 3개를 Claude Code 클라우드 환경 설정(Network secrets 또는 환경 변수)에 넣으세요.")
    print("[AUTH]    채팅창에 붙여 넣지 말고, 이 터미널 창을 닫으면 다시 볼 수 없으니 바로 옮기세요.\n")
    print(f"YOUTUBE_CLIENT_ID={a.client_id}")
    print(f"YOUTUBE_CLIENT_SECRET={a.client_secret}")
    print(f"YOUTUBE_REFRESH_TOKEN={tok['refresh_token']}")


if __name__ == "__main__":
    main()
