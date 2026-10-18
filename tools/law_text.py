#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-18 — law.go.kr 이 막히면(이 클라우드 2026-10-18: 프록시 403) GitHub 법령 저장소 legalize-kr 의 개정 이력에서
#          '그 날짜에 시행 중인 판'을 받는다 (--source auto|lawgo|mirror, --date). 저장소 main 은 공포된 최신판이라 시행일이 미래일 수 있어
#          (예: 국민연금법 시행 2027-03-16) 커밋을 거슬러 시행일자 ≤ 날짜인 첫 판을 고름. 사용자 지시 2026-10-18 "1,3번으로 각각 만들어봐".
# v1.0 — 2026-10-14 — 최초 작성 (사용자 지시 "이게 현재 날짜 기준으로 정말 맞는 정보야?" · "작년 기사 말고 현재 기준으로 확인"):
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
- v1.1: law.go.kr 이 막히면 GitHub 의 legalize-kr(법령마다 Markdown, 개정마다 커밋)에서 받는다 — `--source mirror --date 2026-10-18`.
  처음 한 번 저장소를 내용 없이 받아(--filter=blob:none, 약 1분) `--mirror-dir`(기본 ~/.cache/legalize-kr)에 둔다. 판 고르기 = 그 법령 파일의
  커밋을 최신부터 거슬러 머리글 '시행일자' ≤ 날짜인 첫 판. 부칙에서 조문별로 시행일을 늦춘 것은 따로 확인한다 (출력에 경고).
로그: [STAGE] 시각 key=value (stderr). 네트워크: law.go.kr · github.com(legalize-kr).
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

VERSION = "v1.1"
BASE = "https://law.go.kr"
MIRROR_URL = "https://github.com/legalize-kr/legalize-kr.git"
LOG = logging.getLogger("law_text")


CURL_TRIES = None  # --source auto 일 때 law.go.kr 을 짧게만 시도


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def curl(args, out, ok_size, tries=6, what=""):
    tries = CURL_TRIES or tries
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


def mirror_path(name):
    """'소득세법 시행령' → kr/소득세법/시행령.md · '상속세 및 증여세법' → kr/상속세및증여세법/법률.md"""
    kind = "법률"
    for k in ("시행령", "시행규칙"):
        if name.endswith(" " + k):
            name, kind = name[: -len(k) - 1], k
    return f"kr/{name.replace(' ', '')}/{kind}.md"


def git(args, cwd, check=True):
    r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode:
        raise SystemExit(f"[MIRROR] ❌ git {' '.join(args[:3])} 실패: {r.stderr.strip()[:200]} → 네트워크(github.com)를 확인")
    return r.stdout


def fetch_mirror(name, outdir, date, mirror_dir):
    md = Path(mirror_dir).expanduser()
    if not (md / ".git").exists():
        md.parent.mkdir(parents=True, exist_ok=True)
        log("MIRROR", action="clone", url=MIRROR_URL, dir=md)
        git(["clone", "-q", "--filter=blob:none", "--no-checkout", MIRROR_URL, str(md)], cwd=md.parent)
    else:
        git(["fetch", "-q", "origin", "main"], cwd=md, check=False)
    path = mirror_path(name)
    commits = git(["log", "--format=%H %cs", "origin/main", "--", path], cwd=md).split()
    if not commits:
        raise SystemExit(f"[MIRROR] ❌ '{path}' 없음 → 법령 이름 확인 (띄어쓰기는 law.go.kr 이름 그대로, 예: '국민건강보험법 시행규칙')")
    pairs = list(zip(commits[0::2], commits[1::2]))
    newest = None
    for h, cdate in pairs:
        text = git(["show", f"{h}:{path}"], cwd=md)
        fm = dict(re.findall(r"^(시행일자|공포일자|공포번호): '?([^'\n]*)'?$", text[:2000], re.M))
        ef = fm.get("시행일자", "")
        newest = newest or (ef, fm.get("공포일자", ""))
        log("MIRROR", level=logging.DEBUG, commit=h[:10], promulgated=fm.get("공포일자"), effective=ef)
        if ef and ef <= date:
            head = f"[시행 {ef}] [공포 {fm.get('공포일자', '')} 제{fm.get('공포번호', '')}호] (legalize-kr {h[:10]})"
            outdir.mkdir(parents=True, exist_ok=True)
            out = outdir / f"{name}.txt"
            out.write_text(head + "\n" + text, encoding="utf-8")
            if newest[0] > date:
                log("MIRROR", logging.WARNING, note=f"더 새 판(공포 {newest[1]}·시행 {newest[0]})은 아직 시행 전 — {date} 시행 중인 판을 씀")
            log("MIRROR", logging.WARNING, note="부칙에서 조문별 시행일을 늦춘 것이 있는지 따로 확인")
            log("SAVE", law=name, out=out, chars=len(text), header=head)
            return out, text, head
    raise SystemExit(f"[MIRROR] ❌ '{path}' 에 {date} 이전 시행 판이 없음 (판 {len(pairs)}개)")


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
    ap.add_argument("--source", default="auto", choices=["auto", "lawgo", "mirror"],
                    help="auto = law.go.kr 을 2번 시도하고 막히면 legalize-kr (v1.1)")
    ap.add_argument("--date", default=time.strftime("%Y-%m-%d"), help="이 날짜에 시행 중인 판 (mirror, 기본 오늘)")
    ap.add_argument("--mirror-dir", default="~/.cache/legalize-kr")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    log("START", version=VERSION, law=a.name, source=a.source, date=a.date)
    global CURL_TRIES
    if a.source == "mirror":
        out, text, head = fetch_mirror(a.name, Path(a.out), a.date, a.mirror_dir)
    elif a.source == "lawgo":
        out, text, head = fetch_law(a.name, Path(a.out))
    else:
        CURL_TRIES = 2
        try:
            out, text, head = fetch_law(a.name, Path(a.out))
        except SystemExit as e:
            log("FALLBACK", logging.WARNING, reason=str(e)[:80], to="legalize-kr")
            out, text, head = fetch_mirror(a.name, Path(a.out), a.date, a.mirror_dir)
    print(f"{a.name}: {head}  → {out}")
    for art in a.article:
        print(f"\n--- {art} ---\n{show_article(text, art)}")
    if a.grep:
        for m in list(re.finditer(a.grep, text))[:30]:
            print(f"\n… {text[max(0, m.start() - 150): m.end() + 150]} …")
    return 0


if __name__ == "__main__":
    sys.exit(main())
