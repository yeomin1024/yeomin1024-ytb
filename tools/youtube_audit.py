#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.1 — 2026-10-18 — 태그는 순서 없이 비교(유튜브가 가나다순으로 돌려줌) · 설명란이 다르면 시트에만 있는 줄을 보여 줌.
# v1.0 — 2026-10-18 — 최초 작성. 사용자 지시 2026-10-18 "각 영상들 최적화돼서 올라갔는지 확인해봐":
#          올라간 영상(youtube.json)의 지금 유튜브 정보를 읽어 업로드 시트(upload.md)·지시사항 규칙과 하나씩 맞춰 본다. 고치지는 않음(읽기만).
r"""
올라간 영상 점검 — 업로드 시트·규칙과 지금 유튜브 정보를 대조 (읽기만)

  python3 tools/youtube_audit.py economic                 # youtube.json 이 있는 영상 전부
  python3 tools/youtube_audit.py economic --captions      # + 자막 목록 (영상마다 50단위)

할당량: videos.list 1단위(50개씩) · commentThreads.list 영상마다 1단위 · --captions 면 captions.list 영상마다 50단위.
보는 것 (롱폼 / 쇼츠):
  제목 = 시트 1번 · 화면 폭(title_fit) · 설명란 = 시트 2번(챕터 줄은 올릴 때 SRT 로 다시 계산되므로 빼고 비교) · 첫 줄 길이 ·
  챕터(롱폼: 0:00 시작·3개 이상) · 해시태그 수(롱폼 3 · 쇼츠 2) · 'AI 음성' 고지 · 태그 = 시트 4번·500자 안 ·
  카테고리 27(교육) · 기본·오디오 언어 ko · 아동용 아님 · 공개 상태·예약 시각 · 길이(쇼츠 3분 안) · 처리 끝 ·
  채널 주인 댓글(고정 댓글 후보 — 고정 여부는 API 로 못 봄) · (--captions) 한국어 자막.
API 로 못 보는 것: 합성 콘텐츠 표시(보낼 때만 됨)·쇼츠 관련 동영상·고정 여부·썸네일 그림(i.ytimg.com 막힘) → 사용자가 스튜디오에서.
로그: [STAGE] 시각 key=value (stderr).
"""
import argparse
import json
import logging
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import youtube_upload as yu  # noqa: E402

VERSION = "v1.0.1"
API = "https://www.googleapis.com/youtube/v3"
LOG = logging.getLogger("youtube_audit")
CHAPTER_LINE = re.compile(r"^\d+:\d\d(?::\d\d)? ")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def records(topic):
    """youtube.json → [(영상ID(시트), youtube_id)] — 롱폼 source/<ID>/, 쇼츠 source/<ID>/shorts/."""
    out = []
    for p in sorted((yu.ROOT / topic / "source").glob("*/youtube.json")) + sorted((yu.ROOT / topic / "source").glob("*/shorts/youtube.json")):
        d = json.loads(p.read_text("utf-8"))
        yid = d.get("youtube_id") or d.get("id") or d.get("videoId")
        if not yid or "upload-test" in str(p):
            continue
        vid = p.parent.parent.name + "-shorts" if p.parent.name == "shorts" else p.parent.name
        out.append((vid, yid))
    return out


def no_chapters(text):
    return "\n".join(l for l in text.strip().splitlines() if not CHAPTER_LINE.match(l)).strip()


def title_fit(title, shorts):
    r = subprocess.run([sys.executable, str(yu.ROOT / "tools" / "title_fit.py"), title] + (["--shorts"] if shorts else []),
                       capture_output=True, text=True)
    bad = [l.strip() for l in r.stdout.splitlines() if "❌" in l]
    return bad


def iso_seconds(d):
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", d or "")
    return sum(int(x or 0) * k for x, k in zip(m.groups(), (3600, 60, 1))) if m else None


def audit(topic, vid, v, sheet, comments, caps):
    sh = yu.is_shorts(vid)
    sn, st, cd = v["snippet"], v["status"], v["contentDetails"]
    res = []                                            # (항목, ok, 메모)

    def add(name, ok, note=""):
        res.append((name, ok, note))
    add("제목 = 시트", sn["title"] == sheet["title"], "" if sn["title"] == sheet["title"] else f"올라감「{sn['title']}」 / 시트「{sheet['title']}」")
    bad = title_fit(sn["title"], sh)
    add("제목 화면 폭(2줄)", not bad, "; ".join(bad)[:120])
    same = no_chapters(sn["description"]) == no_chapters(sheet["description"])
    if same:
        add("설명란 = 시트(챕터 줄 빼고)", True)
    else:
        lv, sv = no_chapters(sn["description"]), no_chapters(sheet["description"])
        gone = [l for l in sv.splitlines() if l and l not in lv.splitlines()]
        add("설명란 = 시트(챕터 줄 빼고)", False, f"유튜브 {len(sn['description'])}자 / 시트 {len(sheet['description'])}자 — 시트에만 있는 줄: " + " | ".join(gone)[:160])
    first = sn["description"].strip().splitlines()[0] if sn["description"].strip() else ""
    add("설명란 첫 줄", 15 <= len(first) <= 110, f"{len(first)}자")
    chap = [l for l in sn["description"].splitlines() if CHAPTER_LINE.match(l)]
    if not sh:
        add("챕터 (0:00·3개 이상)", len(chap) >= 3 and chap[0].startswith("0:00"), f"{len(chap)}개")
    tags_h = re.findall(r"(?<!\S)#\S+", sn["description"])
    want = 2 if sh else 3
    add(f"해시태그 {want}개", len(tags_h) == want, " ".join(tags_h))
    add("AI 음성 고지", "AI 음성" in sn["description"])
    tags = sn.get("tags") or []
    same_tags = sorted(tags) == sorted(sheet["tags"])        # 유튜브는 태그를 가나다순으로 돌려줌 — 순서는 보지 않음
    add("태그 = 시트", same_tags, f"{len(tags)}개 · {yu.tags_length(tags)}자" + ("" if same_tags else f" (시트 {len(sheet['tags'])}개: 빠짐 {sorted(set(sheet['tags']) - set(tags))})"))
    add("카테고리 교육(27)", sn.get("categoryId") == "27", sn.get("categoryId", ""))
    add("언어 ko (기본·오디오)", sn.get("defaultLanguage") == "ko" and sn.get("defaultAudioLanguage") == "ko",
        f"{sn.get('defaultLanguage')}/{sn.get('defaultAudioLanguage')}")
    add("아동용 아님", st.get("selfDeclaredMadeForKids") is False and st.get("madeForKids") is False)
    pub = st.get("privacyStatus")
    add("공개 상태", pub == "public" or (pub == "private" and st.get("publishAt")), f"{pub} {st.get('publishAt', '')}")
    sec = iso_seconds(cd.get("duration"))
    add("길이", (sec or 0) <= 180 if sh else (sec or 0) >= 240, f"{sec}초")
    add("처리 끝", st.get("uploadStatus") == "processed", st.get("uploadStatus", ""))
    if comments is not None:
        add("채널 주인 댓글(고정용)", comments > 0, f"{comments}개" + ("" if comments else " — 공개 뒤 고정 댓글 달기"))
    if caps is not None:
        add("한국어 자막" if not sh else "자막(쇼츠는 화면에 구움)", ("ko" in caps) if not sh else True, ",".join(caps) or "없음")
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description="올라간 영상 점검 (읽기만)")
    ap.add_argument("topic")
    ap.add_argument("--captions", action="store_true", help="자막 목록도 (영상마다 50단위)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    recs = records(a.topic)
    log("START", version=VERSION, topic=a.topic, videos=len(recs), captions=a.captions)
    tok = yu.access_token()
    yu.check_channel(a.topic, tok)
    ids = ",".join(y for _, y in recs)
    _, _, data = yu.request("GET", f"{API}/videos?part=snippet,status,contentDetails&id={ids}", tok)
    live = {v["id"]: v for v in data.get("items", [])}
    units = 1 + 1
    total_bad = 0
    for vid, yid in recs:
        v = live.get(yid)
        print(f"\n## {vid} — https://youtu.be/{yid}")
        if not v:
            print("- ❌ 유튜브에 없음 (지워졌거나 다른 채널)")
            total_bad += 1
            continue
        sheet = yu.read_sheet(a.topic, vid)
        comments = None
        try:
            _, _, ct = yu.request("GET", f"{API}/commentThreads?part=snippet&videoId={yid}&maxResults=50", tok, retries=0)
            ch = v["snippet"]["channelId"]
            comments = sum(1 for t in ct.get("items", []) if t["snippet"]["topLevelComment"]["snippet"].get("authorChannelId", {}).get("value") == ch)
            units += 1
        except SystemExit as e:                                       # 비공개 영상은 댓글을 못 읽음
            log("COMMENTS", logging.DEBUG, video=yid, note=str(e)[:80])
        except Exception as e:                                        # noqa: BLE001
            log("COMMENTS", logging.DEBUG, video=yid, note=str(e)[:80])
        caps = None
        if a.captions:
            _, _, cl = yu.request("GET", f"{API}/captions?part=snippet&videoId={yid}", tok)
            caps = sorted({c["snippet"]["language"] for c in cl.get("items", [])})
            units += 50
        for name, ok, note in audit(a.topic, vid, v, sheet, comments, caps):
            total_bad += 0 if ok else 1
            print(f"- {'✅' if ok else '❌'} {name}" + (f" — {note}" if note else ""))
    print("\n※ API 로 못 보는 것: 합성 콘텐츠 표시 · 쇼츠 '관련 동영상' · 댓글 고정 여부 · 썸네일 그림 → 스튜디오에서 확인")
    log("DONE", videos=len(recs), problems=total_bad, units=units)
    return 0 if total_bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
