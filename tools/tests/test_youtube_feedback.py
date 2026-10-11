# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-11 — tools/youtube_feedback.py v1.0 시험 (가짜 API 응답만 씀 — 네트워크·실제 통계 없음)
r"""
  python3 -m unittest discover -s tools/tests -v

- 계산: ISO 길이, Analytics 표, 시청 지속 보간·챕터별 유지·가장 많이 빠진 구간
- 키·권한에 따른 받을 수 있는 자료(plan)
- 처음부터 끝까지: 빚투 영상의 실제 대본·SRT·youtube.json 사본 + 가짜 API → stats/<날짜>.json · feedback.md · 주제 모음
  (빠진 구간이 그 시간의 대본 문장과 챕터로 이어지는지, 같은 날 다시 실행하면 API를 부르지 않는지, 댓글 작성자 이름이 남지 않는지)
- 공개 전 영상 건너뜀, 권한 없을 때·일부 실패할 때도 문서가 만들어지는지, 예약 시각이 지났는데 비공개면 경고
- git_push: 임시 원격 저장소에 결과 파일만 커밋·푸시 (다른 변경은 커밋하지 않음)
FEEDBACK_SAMPLE_DIR 환경 변수가 있으면 가짜 숫자로 만든 feedback.md 예시를 그 폴더에 남긴다 (모양 확인용).
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import youtube_feedback as yf  # noqa: E402

VID, TOPIC = "bittu-2026-10", "stock"
NOW = datetime(2026, 10, 13, 0, 0, tzinfo=timezone.utc)          # 한국 2026-10-13 09:00 (공개 예약 2026-10-11 21:00 KST 뒤)
DURATION = 458                                                   # 'PT7M38S'
DROP_R = (0.20, 0.21)                                            # 가짜 곡선에서 가장 크게 빠지는 곳


def resp(names, rows):
    return {"columnHeaders": [{"name": n} for n in names], "rows": rows}


def fake_retention():
    rows = []
    for i in range(1, 101):
        r = i / 100
        w = 1.0 - 0.3 * r - (0.10 if r >= DROP_R[1] else 0.0) + (0.05 if i == 60 else 0.0)
        rows.append([r, round(w, 4), 0.55])
    return resp(["elapsedVideoTimeRatio", "audienceWatchRatio", "relativeRetentionPerformance"], rows)


class FakeSource:
    """Live 와 같은 모양 (plan · videos · report · comments). 부른 횟수를 센다."""

    def __init__(self, analytics=True, data="oauth", comments="api_key", privacy="public", visible=True, fail=()):
        self.plan = {"data": data, "analytics": analytics, "comments": comments}
        self.auth_note, self.calls, self.privacy, self.visible, self.fail = "fake", [], privacy, visible, set(fail)

    def videos(self, ids):
        self.calls.append("videos")
        if not self.visible:
            return []
        return [{"id": ids[0], "snippet": {"publishedAt": "2026-10-11T12:00:00Z"},
                 "statistics": {"viewCount": "1300", "likeCount": "47", "commentCount": "13"},
                 "status": {"privacyStatus": self.privacy}, "contentDetails": {"duration": "PT7M38S"}}]

    def report(self, params):
        dims = params.get("dimensions", "")
        self.calls.append(f"report:{dims or 'totals'}")
        if dims in self.fail:
            raise yf.ApiError(403, "forbidden", "가짜 실패")
        if not dims:
            return resp(yf.TOTAL_METRICS.split(","), [[1234, 3456.0, 168, 36.7, 45, 12, 3, 9, 1]])
        if dims == "day":
            return resp(["day", "views", "estimatedMinutesWatched", "averageViewDuration"],
                        [["2026-10-11", 400, 1100, 165], ["2026-10-12", 834, 2356, 170]])
        if dims == "elapsedVideoTimeRatio":
            return fake_retention()
        if dims == "insightTrafficSourceType":
            return resp(["insightTrafficSourceType", "views", "estimatedMinutesWatched"],
                        [["BROWSE", 700, 2000], ["SUGGESTED", 400, 1100], ["YT_SEARCH", 134, 356]])
        raise AssertionError(dims)

    def comments(self, video_id, n):
        self.calls.append("comments")
        return [{"snippet": {"totalReplyCount": 2, "topLevelComment": {"snippet": {
            "textDisplay": "반대매매 문자 받던 날이 생각나네요 | 저도 그랬어요", "likeCount": 7,
            "publishedAt": "2026-10-12T01:00:00Z", "authorDisplayName": "홍길동테스트"}}}}]


def make_root(tmp, publish_at="2026-10-11T12:00:00Z"):
    """빚투 영상의 대본·SRT·youtube.json 만 임시 저장소로 복사."""
    src, dst = REPO / TOPIC / "source" / VID, Path(tmp) / TOPIC / "source" / VID
    dst.mkdir(parents=True)
    for name in (f"{VID}.txt", f"{VID}.srt"):
        shutil.copy2(src / name, dst / name)
    rec = json.loads((src / "youtube.json").read_text("utf-8"))
    rec["publishAt"] = publish_at
    (dst / "youtube.json").write_text(json.dumps(rec, ensure_ascii=False), "utf-8")
    return Path(tmp)


class Calc(unittest.TestCase):
    def test_iso_duration(self):
        self.assertEqual(yf.parse_iso_duration("PT7M38S"), 458)
        self.assertEqual(yf.parse_iso_duration("PT1H2M3S"), 3723)
        self.assertEqual(yf.parse_iso_duration("P0D"), 0)
        self.assertIsNone(yf.parse_iso_duration("nonsense"))

    def test_table(self):
        self.assertEqual(yf.table(resp(["a", "b"], [[1, 2]])), [{"a": 1, "b": 2}])
        self.assertEqual(yf.table({"columnHeaders": [{"name": "a"}]}), [])

    def test_retention_math(self):
        rows = [{"elapsedVideoTimeRatio": i / 100, "audienceWatchRatio": 1 - 0.3 * i / 100,
                 "relativeRetentionPerformance": 0.5} for i in range(100, 0, -1)]      # 순서가 뒤섞여 와도
        pts = yf.retention_points(rows, 100)
        self.assertEqual([p["r"] for p in pts], sorted(p["r"] for p in pts))
        self.assertAlmostEqual(yf.interp(pts, 50), 0.85)
        self.assertAlmostEqual(yf.interp(pts, 55.5), 1 - 0.3 * 0.555)
        ch = yf.chapter_rows(pts, [(10, "가"), (60, "나")], 100)
        self.assertAlmostEqual(ch[0]["loss_pp"], 15.0)                # 0.3 × 0.5 × 100
        self.assertAlmostEqual(ch[0]["loss_pp_per_min"], 18.0)        # 15 ÷ (50초 = 0.833분)
        self.assertAlmostEqual(ch[1]["loss_pp"], 12.0)

    def test_moves(self):
        pts = yf.retention_points(yf.table(fake_retention()), DURATION)
        top = yf.moves(pts, 3, falling=True)
        self.assertAlmostEqual(top[0]["t0"], DROP_R[0] * DURATION)
        self.assertAlmostEqual(top[0]["t1"], DROP_R[1] * DURATION)
        self.assertLess(top[0]["d"], -0.1)
        up = yf.moves(pts, 3, falling=False)
        self.assertEqual(len(up), 1)                                  # 오른 곳은 r=0.60 한 곳뿐
        self.assertAlmostEqual(up[0]["t1"], 0.60 * DURATION)


class Plan(unittest.TestCase):
    def test_api_key_only(self):
        s = yf.Live("k", None)
        self.assertEqual(s.plan, {"data": "api_key", "analytics": False, "comments": "api_key"})

    def test_upload_scope_only(self):                                 # 지금 세션의 토큰 (youtube.upload 하나)
        s = yf.Live("", "tok", [yf.SCOPE + "youtube.upload"])
        self.assertEqual(s.plan, {"data": "none", "analytics": False, "comments": "none"})

    def test_full_scopes(self):
        s = yf.Live("k", "tok", [yf.SCOPE + "youtube.force-ssl", yf.SCOPE + "yt-analytics.readonly"])
        self.assertEqual(s.plan, {"data": "oauth", "analytics": True, "comments": "api_key"})

    def test_missing_env(self):
        s = yf.Live.from_env({"YOUTUBE_API_KEY": "k"})
        self.assertIsNone(s.token)
        self.assertIn("OAuth 환경변수 없음", s.auth_note)


class EndToEnd(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="yf_test_")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_full_run(self):
        root = make_root(self.tmp)
        fake = FakeSource()
        written = yf.run(root, TOPIC, source_factory=lambda: fake, now=NOW)
        d = root / TOPIC / "source" / VID
        snap_p, md_p, ov_p = d / "stats" / "2026-10-13.json", d / "feedback.md", root / TOPIC / "feedback.md"
        self.assertEqual(set(written), {snap_p, md_p, ov_p})
        snap, md, ov = json.loads(snap_p.read_text("utf-8")), md_p.read_text("utf-8"), ov_p.read_text("utf-8")

        self.assertEqual(snap["sources"], {"data": "oauth", "analytics": "ok", "comments": "api_key"})
        self.assertEqual(snap["analytics"]["period"]["start"], "2026-10-11")      # 공개일(태평양 시간)
        self.assertEqual(snap["analytics"]["period"]["end"], "2026-10-12")        # 한국 10-13 09:00 = 태평양 10-12 17:00
        self.assertEqual(len(snap["analytics"]["retention"]), 100)
        self.assertNotIn("홍길동테스트", json.dumps(snap, ensure_ascii=False))       # 작성자 이름은 저장하지 않음
        self.assertNotIn("홍길동테스트", md)

        # 가장 많이 빠진 구간 1번 = 가짜 곡선의 r 0.20→0.21, 그 시간의 대본 문장 번호가 같이 나온다
        t0, t1 = DROP_R[0] * DURATION, DROP_R[1] * DURATION
        tl = yf.load_timeline(root, TOPIC, VID)
        self.assertEqual(len(tl), 88)
        said = yf.sentences_between(tl, t0, t1)
        self.assertTrue(said, "그 구간에 대본 문장이 있어야 함")
        row = next(l for l in md.splitlines() if l.startswith(f"| 1 | {yf.mmss(t0)}–{yf.mmss(t1)} |"))
        for s in said:
            self.assertIn(f"{s['n']}. ", row)
        chapters = yf.parse_chapters(json.loads((d / "youtube.json").read_text("utf-8")))
        self.assertEqual(len(chapters), 12)
        self.assertIn(yf.chapter_at(chapters, t0), row)
        self.assertIn("-10.3%p", row)

        for heading in ("## 1. 핵심 지표", "## 2. 수집일별 추이", "## 3. 시청 지속", "### 3-3. 챕터별 유지", "## 4. 유입 경로",
                        "## 5. 일별 조회", "## 6. 댓글"):
            self.assertIn(heading, md)
        self.assertIn("| 평균 시청 비율 | 36.7% |", md)
        self.assertIn("탐색(홈·구독 피드) (`BROWSE`) | 700 | 56.7% |", md)
        self.assertIn("반대매매 문자 받던 날이 생각나네요 ｜ 저도 그랬어요", md)       # 표를 깨는 | 는 바꿈
        chapter_lines = [l for l in md.split("### 3-3. 챕터별 유지")[1].split("## 4.")[0].splitlines() if l.startswith("| ") and "%" in l]
        self.assertEqual(len(chapter_lines), 12)
        self.assertNotIn("⚠️", md)                                                   # 길이·대본이 맞으면 경고 없음
        self.assertIn(f"[{VID}](source/{VID}/feedback.md)", ov)
        self.assertIn("+8", ov)                                                       # 구독 9 − 1

        if os.environ.get("FEEDBACK_SAMPLE_DIR"):
            out = Path(os.environ["FEEDBACK_SAMPLE_DIR"])
            out.mkdir(parents=True, exist_ok=True)
            note = "> ⚠️ **예시 — 테스트용 가짜 숫자** (tools/tests/test_youtube_feedback.py). 실제 통계가 아니다.\n\n"
            (out / "feedback_sample.md").write_text(note + md, "utf-8")
            (out / "overview_sample.md").write_text(note + ov, "utf-8")

        # 같은 날 다시: API를 부르지 않는다 / --refresh: 다시 부른다
        n = len(fake.calls)
        yf.run(root, TOPIC, source_factory=lambda: fake, now=NOW)
        self.assertEqual(len(fake.calls), n)
        yf.run(root, TOPIC, source_factory=lambda: fake, now=NOW, refresh=True)
        self.assertGreater(len(fake.calls), n)

        # 다음 날: 원자료 2개 → 추이 표 2줄
        yf.run(root, TOPIC, source_factory=lambda: fake, now=datetime(2026, 10, 14, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(len(list((d / "stats").glob("*.json"))), 2)
        md2 = md_p.read_text("utf-8")
        trend = md2.split("## 2. 수집일별 추이")[1].split("## 3.")[0]
        self.assertEqual(len([l for l in trend.splitlines() if l.startswith("| 2026-")]), 2)

    def test_dry_run_writes_nothing(self):
        root = make_root(self.tmp)
        self.assertEqual(yf.run(root, TOPIC, source_factory=FakeSource, now=NOW, dry_run=True), [])
        self.assertFalse((root / TOPIC / "source" / VID / "stats").exists())
        self.assertFalse((root / TOPIC / "feedback.md").exists())

    def test_not_public_yet_skipped(self):
        root = make_root(self.tmp, publish_at="2026-10-20T12:00:00Z")
        fake = FakeSource()
        self.assertEqual(yf.run(root, TOPIC, source_factory=lambda: fake, now=NOW), [])
        self.assertEqual(fake.calls, [])

    def test_no_scopes_still_writes(self):                           # 지금 세션처럼 상세 분석 권한 없음 + API 키로 안 보임
        root = make_root(self.tmp)
        fake = FakeSource(analytics=False, data="api_key", visible=False)
        yf.run(root, TOPIC, source_factory=lambda: fake, now=NOW)
        md = (root / TOPIC / "source" / VID / "feedback.md").read_text("utf-8")
        self.assertIn("Data API에서 영상이 보이지 않음", md)
        self.assertIn("yt-analytics.readonly", md)
        self.assertIn("## 3. 시청 지속 (audience retention)\n\n자료 없음", md)
        self.assertFalse(any(c.startswith("report") for c in fake.calls))

    def test_partial_failure_and_private_warning(self):
        root = make_root(self.tmp)
        fake = FakeSource(privacy="private", fail={"insightTrafficSourceType"})
        yf.run(root, TOPIC, source_factory=lambda: fake, now=NOW)
        snap = json.loads((root / TOPIC / "source" / VID / "stats" / "2026-10-13.json").read_text("utf-8"))
        self.assertTrue(snap["sources"]["analytics"].startswith("일부 실패: traffic"))
        self.assertTrue(any("비공개 잠김" in w for w in snap["warnings"]))
        md = (root / TOPIC / "source" / VID / "feedback.md").read_text("utf-8")
        self.assertIn("## 4. 유입 경로\n\n자료 없음", md)
        self.assertIn("### 3-1. 가장 많이 빠진 구간", md)                          # 다른 부분은 그대로


class Push(unittest.TestCase):
    def git(self, cwd, *a):
        return subprocess.run(["git", "-C", str(cwd), *a], capture_output=True, text=True, check=True).stdout.strip()

    def test_push_only_result_files(self):
        tmp = Path(tempfile.mkdtemp(prefix="yf_git_"))
        try:
            remote, work = tmp / "remote.git", tmp / "work"
            subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(remote)], check=True)
            subprocess.run(["git", "clone", "-q", str(remote), str(work)], check=True, capture_output=True)
            for k, v in (("user.name", "t"), ("user.email", "t@example.com"), ("commit.gpgsign", "false")):
                self.git(work, "config", k, v)
            (work / "README.md").write_text("x\n")
            self.git(work, "add", "README.md")
            self.git(work, "commit", "-q", "-m", "init")
            self.git(work, "push", "-q", "origin", "HEAD:main")
            (work / "README.md").write_text("다른 변경 — 커밋하면 안 됨\n")
            a = work / "stock" / "source" / "v" / "feedback.md"
            b = work / "stock" / "feedback.md"
            a.parent.mkdir(parents=True)
            a.write_text("a\n")
            b.write_text("b\n")
            self.assertTrue(yf.git_push(work, [a, b], "피드백 자료: 시험", sleep=lambda s: None))
            files = self.git(remote, "show", "--name-only", "--format=", "main").splitlines()
            self.assertEqual(sorted(files), ["stock/feedback.md", "stock/source/v/feedback.md"])
            self.assertEqual(self.git(remote, "show", "main:README.md"), "x")
            self.assertTrue(yf.git_push(work, [a, b], "같은 내용", sleep=lambda s: None))   # 바뀐 것 없음 → 커밋 없이 성공
            self.assertEqual(len(self.git(remote, "log", "--oneline", "main").splitlines()), 2)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
