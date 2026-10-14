#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-14 — 최초 작성 (사용자 지시 "이게 현재 날짜 기준으로 정말 맞는 정보야?" · "작년 기사 말고 현재 기준으로 확인"):
#          2026-10-14 대화에서 대본 사실을 확인할 때 쓴 국가법령정보센터(law.go.kr) 현행 법령 전문 받기를 도구로. 지시사항: guides/script_guide.md 3번
"""
현행 법령 전문 받기 — law.go.kr 의 '지금 시행 중인' 법령 본문을 텍스트로 저장하고, 조문·낱말을 찾아 보여 준다.

  python3 tools/law_text.py 소득세법 --out /tmp/law                    # /tmp/law/소득세법.txt (+ 시행일·법률 번호 출력)
  python3 tools/law_text.py 소득세법 --out /tmp/law --article 제14조    # 제14조 본문 앞부분
  python3 tools/law_text.py "국민건강보험법 시행규칙" --out /tmp/law --grep "1천만원|2천만원"

- 법령 이름은 law.go.kr 주소 그대로 (예: "소득세법 시행령", "국민건강보험법 시행규칙", "상속세 및 증여세법").
- 별표(예: 건보 피부양자 기준 별표 1의2)는 PDF 라서 이 도구로 받지 않는다 → 법령 화면의 별표 링크(flDownload.do)를 받아 PDF 로 읽는다.
- law.go.kr 는 가끔 연결을 끊는다 → 요청마다 6번까지 다시 시도한다(2·4·6…초 쉼).
- 받은 날짜·시행일을 대본 README 의 출처 표에 적는다 ("2026-10-14 받음, 시행 2026.7.1, 법률 제21221호" 처럼).
로그: [STAGE] 시각 key=value (stderr). 네트워크: law.go.kr 만.
"""
import argparse
import html
import logging
import re
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

VERSION = "v1.0"
BASE = "https://law.go.kr"
LOG = logging.getLogger("law_text")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def curl(args, out, ok_size, tries=6, what=""):
    """curl 로 받아 out 에 저장. 크기가 ok_size 를 넘으면 성공. 실패하면 다시 시도."""
    for i in range(tries):
        r = subprocess.run(["curl", "-sS", "-L", "--max-time", "90", "-o", str(out)] + args, capture_output=True, text=True)
        n = out.stat().st_size if out.exists() else 0
        if n > ok_size:
            log("FETCH", what=what, bytes=n, tries=i + 1)
            return n
        log("FETCH", logging.WARNING, what=what, bytes=n, tries=i + 1, error=(r.stderr or "").strip()[:120] or "작음")
        time.sleep(2 + 2 * i)
    raise SystemExit(f"[FETCH] ❌ {what} 받기 실패 ({tries}번) → 잠시 뒤 다시 실행하거나, 브라우저로 {BASE} 에서 직접 확인하세요")


def to_text(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</tr>", "\n", h)
    t = html.unescape(re.sub(r"<[^>]+>", " ", h))
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()


def fetch_law(name, outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    work = outdir / f".{name}"
    work.mkdir(exist_ok=True)
    main_html = work / "main.html"
    curl([f"{BASE}{urllib.parse.quote('/법령/' + name)}"], main_html, 200, what="법령 화면")
    m = re.search(r'src="(/LSW//lsInfoP\.do\?[^"]*)"', main_html.read_text("utf-8", "replace"))
    if not m:
        raise SystemExit(f"[PARSE] ❌ '{name}' 법령 화면에서 본문 주소를 못 찾음 → 법령 이름이 law.go.kr 주소와 같은지 확인 (예: '소득세법 시행령')")
    src = m.group(1).replace("&amp;", "&")
    info_html = work / "info.html"
    curl([BASE + src], info_html, 200, what="본문 정보")
    info = info_html.read_text("utf-8", "replace")

    def val(key):
        mm = re.search(rf'id="{key}"[^>]*value="([^"]*)"', info) or re.search(rf'id="{key}" value="([^"]*)"', info)
        if not mm:
            raise SystemExit(f"[PARSE] ❌ 본문 정보에 {key} 없음 → law.go.kr 화면 구조가 바뀌었을 수 있음 (브라우저로 확인)")
        return mm.group(1)
    q = urllib.parse.parse_qs(urllib.parse.urlparse(src).query)
    data = (f"lsiSeq={val('lsiSeq')}&efYd={q.get('efYd', [''])[0]}&chrClsCd=010202&ancYnChk=0&lsId={val('lsId')}"
            f"&ancYd={val('ancYd')}&ancNo={val('ancNo')}&nwJoYnInfo=Y&efGubun=Y&vSct=*")
    body = work / "body.html"
    curl(["-X", "POST", f"{BASE}/LSW/lsInfoR.do", "--data", data], body, 10000, what="법령 전문")
    text = to_text(body.read_text("utf-8", "replace"))
    out = outdir / f"{name}.txt"
    out.write_text(text, encoding="utf-8")
    head = re.search(r"\[시행[^\]]*\][^\n]{0,80}", text)
    log("SAVE", law=name, out=out, chars=len(text), header=(head.group(0) if head else "시행일 못 찾음"))
    return out, text, (head.group(0) if head else "")


def show_article(text, article, width=1500):
    """'제14조' 처럼 조문 머리('제14조(' )부터 width 글자."""
    m = re.search(rf"{re.escape(article)}\s*\(", text)
    if not m:
        return f"(본문에서 '{article}(' 를 못 찾음)"
    return text[m.start(): m.start() + width]


def main(argv=None):
    ap = argparse.ArgumentParser(description="law.go.kr 현행 법령 전문 받기·조문 찾기 (대본 사실 확인용)")
    ap.add_argument("name", help="법령 이름 (예: 소득세법, '소득세법 시행령')")
    ap.add_argument("--out", required=True, help="저장 폴더 (저장소 밖 임시 폴더 권장)")
    ap.add_argument("--article", action="append", default=[], help="보여 줄 조문 (예: 제14조) — 여러 번 가능")
    ap.add_argument("--grep", help="본문에서 찾을 정규식 (앞뒤 150자씩)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    log("START", version=VERSION, law=a.name)
    out, text, head = fetch_law(a.name, Path(a.out))
    print(f"{a.name}: {head}  → {out}")
    for art in a.article:
        print(f"\n--- {art} ---\n{show_article(text, art)}")
    if a.grep:
        for m in list(re.finditer(a.grep, text))[:30]:
            print(f"\n… {text[max(0, m.start() - 150): m.end() + 150]} …")
    return 0


if __name__ == "__main__":
    sys.exit(main())
