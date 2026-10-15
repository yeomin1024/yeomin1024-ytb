#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.1 — 2026-10-15 — 가짜 자막 함수가 outlier_research v2.4 의 any_lang(외국 영상 원래 언어 자막)을 받음 (시험 내용은 그대로)
# (v1.0 — 2026-10-15 — 쇼츠 분석 시험 (사용자 지시: "… 쇼츠 분석 기능도 추가해 목적은 사람들의 니즈를 충족해주는 쇼츠를 만들어서
#          최대한 조회수를 높이기 위한 쇼츠를 만들기 위해 분석하는거야 전력을 다해서 해봐"):
#          outlier_research v2.3 (쇼츠 판별·화면비·채널 쇼츠 목록·쇼츠 검색 캐시) · shorts_analysis v1.0 (가짜 자료로 결과 숫자 확인) ·
#          web_ui v1.6 (쇼츠 탐색 → 승인 → 분석, 음성인식 남은 수). 진짜 YouTube·GitHub 에 요청하지 않는다: urlopen·자막을 가짜로,
#          저장소 대신 임시 폴더를 ROOT 로, GITHUB_TOKEN 류는 지움 (CLAUDE.md '시험이 진짜 GitHub 에 올리지 않게').)
"""python3 -m unittest tools.tests.test_shorts -v   (또는 python3 tools/tests/test_shorts.py)"""
import csv
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
import urllib.error
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parent.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import outlier_research as orr      # noqa: E402
import pc_analysis as pc            # noqa: E402
import shorts_analysis as sh        # noqa: E402
import web_ui as web                # noqa: E402

KEY = "AIza-test-key-not-real-000"
NOW = datetime.now(timezone.utc)


def _iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _jpeg(w=90, h=160):
    try:
        from PIL import Image
        b = io.BytesIO()
        Image.new("RGB", (w, h), (200, 30, 30)).save(b, "JPEG")
        return b.getvalue() + b"\0" * 1200            # 1KB 넘게 (빈 그림 거르기 통과)
    except ImportError:
        return b"\xff\xd8" + b"\0" * 2000


class _Resp(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()


class FakeYouTube:
    """urlopen 대신. videos: 영상마다 (길이 초, 세로?, 채널, 조회수, 올린 지 며칠). playlistItems: UUSH 목록 (없으면 404). i.ytimg.com: 그림."""

    def __init__(self):
        self.calls, self.search_ids, self.lists, self.vids, self.covers = [], {}, {}, {}, set()

    def add(self, vid, sec, vertical, ch, views, age, title="연금 꿀팁 #shorts", subs_ch=None):
        self.vids[vid] = {"sec": sec, "vertical": vertical, "ch": ch, "views": views, "age": age, "title": title}

    def __call__(self, req, timeout=30):
        url = req.full_url if hasattr(req, "full_url") else str(req)
        u = urllib.parse.urlparse(url)
        if u.netloc == "suggestqueries.google.com":                       # 자동완성 (할당량 0)
            q = urllib.parse.parse_qs(u.query)["q"][0]
            self.calls.append(("autocomplete", {"q": q}))
            return _Resp(json.dumps([q, [q, q + " 나이", q + " 세금"]]).encode("utf-8"))
        if u.netloc == "i.ytimg.com":
            name = u.path.rsplit("/", 1)[-1]
            self.calls.append(("thumb", {"name": name}))
            if name == "oar2.jpg" and u.path.split("/")[2] in self.covers:
                return _Resp(_jpeg())
            if name == "hqdefault.jpg":
                return _Resp(_jpeg(480, 360))
            raise urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO(b""))
        kind = u.path.rsplit("/", 1)[-1]
        q = {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}
        assert q.get("key") == KEY
        self.calls.append((kind, q))
        if kind == "search":
            ids = self.search_ids.get((q["q"], q.get("videoDuration")), [])
            data = {"items": [{"id": {"videoId": v}} for v in ids], "pageInfo": {"totalResults": len(ids) * 7}}
        elif kind == "videos":
            data = {"items": [self._video(v, "player" in q["part"]) for v in q["id"].split(",") if v in self.vids]}
        elif kind == "channels":
            data = {"items": [{"id": c, "snippet": {"title": "채널 " + c[-3:], "publishedAt": "2025-06-01T00:00:00Z"},
                               "statistics": {"subscriberCount": "8000", "videoCount": "60", "viewCount": "900000"}} for c in q["id"].split(",")]}
        elif kind == "playlistItems":
            pid = q["playlistId"]
            if pid not in self.lists:
                raise urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO(b'{"error":{"errors":[{"reason":"playlistNotFound"}]}}'))
            ids = self.lists[pid]
            start = int(q.get("pageToken") or 0)
            data = {"items": [{"contentDetails": {"videoId": v}} for v in ids[start:start + 50]], "pageInfo": {"totalResults": len(ids)}}
            if start + 50 < len(ids):
                data["nextPageToken"] = str(start + 50)
        elif kind == "commentThreads":
            texts = ["다음 편도 알려 주세요", "풀영상 어디서 보나요?", "정말 도움이 됐어요", "연금저축 세액공제 얼마나 되나요?"]
            data = {"items": [{"snippet": {"totalReplyCount": 0, "topLevelComment": {
                "id": f"c{q['videoId']}_{i}", "snippet": {"textDisplay": t, "likeCount": 5 - i, "publishedAt": "2026-10-01T00:00:00Z",
                                                          "authorChannelId": {"value": "UCviewer"}}}}} for i, t in enumerate(texts)]}
        elif kind == "comments":
            data = {"items": []}
        else:
            raise AssertionError(kind)
        return _Resp(json.dumps(data).encode("utf-8"))

    def _video(self, v, player):
        x = self.vids[v]
        it = {"id": v, "snippet": {"title": x["title"], "channelTitle": "채널 " + x["ch"][-3:], "channelId": x["ch"],
                                   "publishedAt": _iso(NOW - timedelta(days=x["age"])), "description": "연금 이야기 #연금 #노후",
                                   "tags": ["연금"], "liveBroadcastContent": "none", "defaultAudioLanguage": "ko"},
              "contentDetails": {"duration": f"PT{x['sec']}S"},
              "statistics": {"viewCount": str(x["views"]), "likeCount": str(x["views"] // (5000 if x["sec"] < 10 else 50)),
                             "commentCount": str(x["views"] // 2000)}}
        if player:
            it["player"] = {"embedHtml": "<iframe>", "embedWidth": "4608" if x["vertical"] else "14564", "embedHeight": "8192"}
        return it

    def count(self, kind):
        return sum(1 for k, _ in self.calls if k == kind)


def ch(n):
    return ("UC" + f"shortschannel{n:02d}").ljust(24, "x")[:24]


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.env = mock.patch.dict(os.environ, {"YOUTUBE_API_KEY": KEY}, clear=False)
        self.env.start()
        for name in list(os.environ):                     # 시험이 진짜 GitHub 에 올리지 않게 (CLAUDE.md)
            if name.startswith(("GITHUB_TOKEN", "GH_TOKEN")):
                os.environ.pop(name)
        self.patches = [mock.patch.object(pc, "ROOT", self.root), mock.patch.object(orr, "ROOT", self.root),
                        mock.patch.object(web, "ROOT", self.root), mock.patch.object(sh, "ROOT", self.root),
                        mock.patch.object(web, "sh", sh), mock.patch.object(web, "orr", orr),
                        mock.patch.object(orr, "transcript", self.fake_transcript)]
        for p in self.patches:
            p.start()
        self.yt = FakeYouTube()
        self.urlopen = mock.patch.object(orr.urllib.request, "urlopen", self.yt)
        self.urlopen.start()
        (self.root / ".yt_work").mkdir()
        td = self.root / "economic"
        td.mkdir()
        for f in ("analyzer_config.toml", "keywords.toml", "tag_rules.toml", "analysis_rules.toml"):
            shutil.copy(REPO / "economic" / f, td / f)
        (td / "keywords.txt").write_text("연금\n노후준비\n", "utf-8")

    def fake_transcript(self, vid, any_lang=False):                             # v1.0.1: outlier_research v2.4 any_lang
        if vid.endswith("1"):
            return ([{"text": "연금 이렇게 받으면 손해일까요?", "start": 0.4, "duration": 2.2},
                     {"text": "정답은 순서에 있습니다", "start": 2.6, "duration": 2.0},
                     {"text": "풀영상은 고정 댓글에서 확인하세요", "start": 40.0, "duration": 3.0}], "ko", "ok")
        return [], "-", "IpBlocked: 429 (시험)"

    def tearDown(self):
        self.urlopen.stop()
        for p in self.patches:
            p.stop()
        self.env.stop()
        self.tmp.cleanup()


class TestHelpers(Base):
    def test_is_short_and_hashtags(self):
        self.assertEqual(orr.is_short({"duration": 49, "embed_w": 4608, "embed_h": 8192}), (True, "세로·정사각"))
        self.assertEqual(orr.is_short({"duration": 157, "embed_w": 14564, "embed_h": 8192})[0], False)
        self.assertEqual(orr.is_short({"duration": 181, "embed_w": 4608, "embed_h": 8192})[0], False)
        self.assertTrue(orr.is_short({"duration": 120, "title": "연금 #Shorts"})[0])
        self.assertTrue(orr.is_short({"id": "a", "duration": 150, "embed_w": 9, "embed_h": 1}, {"a"})[0])   # 채널 쇼츠 목록이 먼저
        self.assertFalse(orr.is_short({"duration": 90, "title": "x"})[0])
        self.assertEqual(orr.hashtags("제목 #연금 #Shorts", "#연금 #노후_팁"), ["연금", "shorts", "노후_팁"])

    def test_player_dims_and_refetch_old_cache(self):
        self.yt.add("v0000000001", 45, True, ch(1), 1000, 5)
        cache = self.root / "c"
        cache.mkdir()
        old = {"id": "v0000000001", "title": "t", "channel_id": ch(1), "published": _iso(NOW), "duration": 45, "was_live": False,
               "fetched": NOW.isoformat()}
        (cache / "v0000000001.json").write_text(json.dumps(old), "utf-8")
        api = orr.Api(KEY, 1000)
        st = orr.new_state()
        orr.fetch_video_infos(api, cache, ["v0000000001"], st)                     # 롱폼 방식 — 캐시 그대로
        self.assertEqual(self.yt.count("videos"), 0)
        infos = orr.fetch_video_infos(api, cache, ["v0000000001"], st, player=True)   # 쇼츠 — 화면비 없는 캐시는 다시 (1단위)
        self.assertEqual(self.yt.count("videos"), 1)
        q = self.yt.calls[-1][1]
        self.assertIn("player", q["part"])
        self.assertEqual(q["maxHeight"], "8192")
        self.assertEqual((infos[0]["embed_w"], infos[0]["embed_h"]), (4608, 8192))
        orr.fetch_video_infos(api, cache, ["v0000000001"], st, player=True)
        self.assertEqual(self.yt.count("videos"), 1)                               # 이제 캐시
        self.assertEqual(api.used, 1)

    def test_channel_shorts_list_and_404(self):
        self.yt.lists["UUSH" + ch(1)[2:]] = [f"s{i:010d}" for i in range(60)]
        cache = self.root / "c2"
        cache.mkdir()
        api = orr.Api(KEY, 1000)
        ids = orr.channel_shorts(api, cache, ch(1), ttl_h=24)
        self.assertEqual(len(ids), 60)
        self.assertEqual(json.loads((cache / f"uploads_{ch(1)}.json").read_text("utf-8"))["total"], 60)
        self.assertEqual(orr.channel_shorts(api, cache, ch(2), ttl_h=24), [])         # 쇼츠 없는 채널(404) → 빈 목록, 오류 아님
        d = json.loads((cache / f"uploads_{ch(2)}.json").read_text("utf-8"))
        self.assertTrue(d["none"])
        n = self.yt.count("playlistItems")
        orr.channel_shorts(api, cache, ch(2), ttl_h=24)                              # 캐시 — 다시 묻지 않음
        self.assertEqual(self.yt.count("playlistItems"), n)
        self.assertEqual(orr.channel_shorts(api, cache, "bad"), [])

    def test_adaptive_cache_counts_shorts_for_short_searches(self):
        cache = self.root / "c3"
        cache.mkdir()
        (cache / "v0000000009.json").write_text(json.dumps({"id": "v0000000009", "title": "연금", "duration": 40, "published": _iso(NOW),
                                                            "audio_lang": "ko"}), "utf-8")
        self.assertEqual(orr._useful_novel(cache, {"dur": "short", "novel": ["v0000000009"]}, 56), 1)
        self.assertEqual(orr._useful_novel(cache, {"dur": "medium", "novel": ["v0000000009"]}, 56), 0)

    def test_speech_features(self):
        f = sh.speech_features([{"text": "여러분 연금 얼마 받으세요?", "start": 1.0, "duration": 3.0},
                                {"text": "이것만 알면 됩니다", "start": 4.0, "duration": 2.0},
                                {"text": "구독하고 다음 편에서 봬요 그리고", "start": 25.0, "duration": 3.0}], 30)
        self.assertEqual(f["first_speech_sec"], 1.0)
        self.assertIn("질문으로 시작", f["hook_types"])
        self.assertIn("시청자 부르기", f["hook_types"])
        self.assertIn("구독·좋아요 부탁", f["ending_types"])
        self.assertIn("풀영상·다음 편 안내", f["ending_types"])
        self.assertTrue(f["ends_open"])                                  # '그리고'로 끝남
        self.assertAlmostEqual(f["coverage"], 8 / 30, places=2)
        self.assertGreater(f["syl_first3"], 0)


class TestAnalysis(Base):
    def _case(self, vid, cid, subs, views, sec=45, age=20, vertical=True, transcript=None, title="연금 이렇게 받으세요"):
        d = self.root / "economic" / "result" / "outliers" / "shorts" / f"S_{vid}"
        d.mkdir(parents=True)
        meta = {"id": vid, "title": title, "channel": "채널 " + cid[-3:], "channel_id": cid, "subs": subs, "views": views, "likes": views // 40,
                "comments_reported": views // 1000, "published_at": _iso(NOW - timedelta(days=age)), "seconds": sec, "minutes": round(sec / 60, 1),
                "comments_complete": True, "transcript_status": "ok" if transcript else "IpBlocked", "cover": "oar2.jpg"}
        (d / "metadata.json").write_text(json.dumps(meta), "utf-8")
        (d / "description.txt").write_text("연금 이야기 #연금 #노후\n전체 영상: https://youtu.be/abcdefghijk", "utf-8")
        if transcript is not None:
            (d / "transcript.json").write_text(json.dumps(transcript), "utf-8")
        with open(d / "comments.csv", "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=["text", "likes", "is_reply", "creator"])
            w.writeheader()
            for t, lk in (("다음 편도 알려 주세요", 9), ("풀영상 어디서 보나요?", 4), ("정말 도움이 됐어요", 3)):
                w.writerow({"text": t, "likes": lk, "is_reply": 0, "creator": 0})
        cache = self.root / "economic" / "result" / "outliers" / ".cache" / "shorts"
        cache.mkdir(parents=True, exist_ok=True)
        (cache / f"{vid}.json").write_text(json.dumps({"id": vid, "title": title, "channel": "채널 " + cid[-3:], "channel_id": cid,
                                                       "published": _iso(NOW - timedelta(days=age)), "duration": sec, "view_count": views,
                                                       "like_count": views // 40, "comment_count": views // 1000, "description": "연금 #연금",
                                                       "tags": ["연금"], "live": False, "was_live": False, "audio_lang": "ko",
                                                       "embed_w": 4608 if vertical else 14564, "embed_h": 8192, "fetched": NOW.isoformat()}), "utf-8")

    def test_run_on_synthetic_data(self):
        out = self.root / "economic" / "result" / "outliers"
        cache = out / ".cache" / "shorts"
        a, b = ch(1), ch(2)
        tr = {"lang": "ko", "snippets": [{"text": "연금 이렇게 받으면 손해일까요?", "start": 0.3, "duration": 2.5},
                                         {"text": "풀영상은 고정 댓글에서", "start": 40, "duration": 3}]}
        self._case("aaaaaaaaaa1", a, 9000, 300000, transcript=tr)                 # 성공 (×33)
        self._case("aaaaaaaaaa2", a, 9000, 200000)                                # 성공 (×22)
        self._case("aaaaaaaaaa3", a, 9000, 100000)                                # 성공 기준이지만 채널당 2개 → 잘림
        self._case("bbbbbbbbbb1", b, 20000, 70000, transcript={"lang": "ko(음성인식)", "snippets": [], "no_speech": True})   # 성공 (×3.5) · 말 없음
        self._case("bbbbbbbbbb2", b, 20000, 30000)                                # 성공 아님 (조회수 < 5만)
        self._case("hhhhhhhhhh1", b, 20000, 900000, sec=150, vertical=False)       # 가로 → 쇼츠 아님
        self._case("adadadadad1", ch(3), 1110, 2788240, sec=6)                     # 조회수 부풀림 의심 (6초 · 좋아요 0.04% — 2026-10-15 실측 모양)
        ad = json.loads((cache / "adadadadad1.json").read_text("utf-8"))
        ad["like_count"] = 1012
        (cache / "adadadadad1.json").write_text(json.dumps(ad), "utf-8")
        am = out / "shorts" / "S_adadadadad1" / "metadata.json"
        (lambda m: am.write_text(json.dumps({**m, "likes": 1012}), "utf-8"))(json.loads(am.read_text("utf-8")))
        # 채널 평소 쇼츠 (UUSH) — 채널 a: 평소 2,000회 쇼츠 8개
        normal = [f"n{i:010d}" for i in range(8)]
        for i, v in enumerate(normal):
            (cache / f"{v}.json").write_text(json.dumps({"id": v, "title": f"연금 평소 이야기 {i}", "channel": "채널 a", "channel_id": a,
                                                         "published": _iso(NOW - timedelta(days=10 + i)), "duration": 30, "view_count": 2000 + i * 10,
                                                         "like_count": 30, "comment_count": 1, "description": "", "tags": [], "live": False,
                                                         "was_live": False, "audio_lang": "ko", "embed_w": 4608, "embed_h": 8192}), "utf-8")
        (cache / f"uploads_{a}.json").write_text(json.dumps({"channel": a, "ids": normal + ["aaaaaaaaaa1", "aaaaaaaaaa2", "aaaaaaaaaa3"],
                                                             "total": 40, "fetched": NOW.isoformat(), "complete": True}), "utf-8")
        (cache / "search_x.json").write_text(json.dumps({"q": "연금", "dur": "short", "ids": ["aaaaaaaaaa1", "bbbbbbbbbb2", "n0000000001"],
                                                         "total": 300, "fetched": NOW.isoformat()}), "utf-8")
        (out / ".cache" / "channels.json").write_text(json.dumps({
            a: {"subs": 9000, "created": "2025-08-01T00:00:00Z", "videos": 50, "fetched": NOW.isoformat()},
            b: {"subs": 20000, "created": "2020-01-01T00:00:00Z", "videos": 400, "fetched": NOW.isoformat()}}), "utf-8")
        (out / ".cache" / "autocomplete.json").write_text(json.dumps({"연금": {"s": ["연금", "연금 수령 나이", "연금저축 세액공제"],
                                                                              "fetched": NOW.isoformat()}}), "utf-8")
        d = sh.run("economic", now=NOW, root=self.root, fetch_thumbs=False)
        sd = out / "shorts"
        self.assertEqual([c["id"] for c in d["success_cases"]], ["aaaaaaaaaa1", "aaaaaaaaaa2", "bbbbbbbbbb1"])
        self.assertEqual([x["id"] for x in d["sources"]["success_channel_cut"]], ["aaaaaaaaaa3"])
        self.assertIn("가로 영상", "".join(d["sources"]["not_short"]))
        self.assertTrue(next(r for r in d["approved"] if r["id"] == "adadadadad1")["exclude"].startswith("조회수 부풀림 의심(좋아요 0.2%"))
        self.assertEqual(d["sources"]["excluded_shorts"].get("조회수 부풀림 의심"), 1)
        self.assertTrue(any("부풀림·광고 의심 1개의 길이 중앙값 6" in x for x in d["limits"]))
        self.assertEqual((d["tiny"]["tiny"]["n"], d["tiny"]["tiny"]["inflated"]), (1, 1))      # 5-2번: 15초 미만 = 부풀림 의심 1개
        self.assertEqual(d["tiny"]["examples"][0]["id"], "adadadadad1")
        appr = {r["id"]: r for r in d["approved"]}
        self.assertTrue(appr["hhhhhhhhhh1"]["exclude"].startswith("쇼츠 아님"))
        c1 = d["success_cases"][0]
        self.assertEqual(c1["channel_ratio"], round(300000 / 2045, 1))            # 채널 a 평소 쇼츠 중앙값 대비 (자기 자신과 다른 성공 쇼츠 포함, 자신 제외)
        self.assertEqual(c1["first_speech_sec"], 0.3)
        self.assertIn("질문으로 시작", c1["hook_types"])
        self.assertIn("풀영상·다음 편 안내", c1["ending_types"])
        self.assertTrue(c1["long_link"])
        self.assertEqual(d["speech"]["success"]["no_speech"], 1)
        self.assertEqual(d["sources"]["text_sources"].get("말 없음(음성인식)"), 1)
        self.assertGreaterEqual(d["needs"]["requests_total"], 3)                   # 성공 쇼츠 3개 × '다음 편도 알려 주세요'
        more = next(r for r in d["needs"]["categories"] if r["name"] == sh.CAT_MORE)
        self.assertGreaterEqual(more["count"], 6)                                  # '다음 편' + '풀영상' × 3
        self.assertGreaterEqual(d["baseline"]["hits"], 1)
        self.assertEqual(d["market"]["videos"], 3)
        self.assertTrue(any(r["phrase"] == "연금 수령 나이" for r in d["market"]["autocomplete"]))
        self.assertEqual(d["growth"]["fast"][0]["channel_id"], a)                   # 개설 14개월 안·쇼츠 몫 80%
        for f in ("analysis.md", "analysis.json", "compare.csv", "approved.md", "cases_01.md"):
            self.assertTrue((sd / f).is_file(), f)
        md = (sd / "analysis.md").read_text("utf-8")
        for head in ("## 0. 자료와 한계", "## 1. 성공 쇼츠 3개", "### 1-2. 같은 채널 기준선", "## 5. 길이 (초)", "## 6. 첫 3초",
                     "## 11. 시청자 니즈", "2025-03-31"):
            self.assertIn(head, md)
        self.assertNotRegex(md, r"\| None \|")                                   # 빈 칸이 'None' 으로 새지 않게

    def test_no_data_writes_nothing(self):
        self.assertIsNone(sh.run("economic", now=NOW, root=self.root, fetch_thumbs=False))
        self.assertFalse((self.root / "economic" / "result" / "outliers" / "shorts" / "analysis.md").exists())


class TestWeb(Base):
    def setUp(self):
        super().setUp()
        a, b = ch(1), ch(2)
        self.yt.add("sssssssss01", 40, True, a, 400000, 12, "연금 받는 순서 이렇게 #shorts")    # 성공 쇼츠 (구독자 8,000 → ×50)
        self.yt.add("sssssssss02", 55, True, b, 20000, 9, "노후준비 체크")                        # 쇼츠, 성공 아님
        self.yt.add("hhhhhhhhh01", 150, False, b, 900000, 8, "연금 가로 영상")                   # 가로 → 쇼츠 아님
        self.yt.add("lllllllll01", 200, True, a, 900000, 8, "연금 3분 넘음")                     # 3분 넘음 → 쇼츠 아님
        self.yt.add("aaaaaaaaa01", 6, True, b, 2788240, 20, "국민연금 얼마 받을까?")              # 조회수 부풀림 의심 (좋아요 0.02%)
        self.yt.search_ids[("연금", "short")] = ["sssssssss01", "hhhhhhhhh01", "lllllllll01", "aaaaaaaaa01"]
        self.yt.search_ids[("노후준비", "short")] = ["sssssssss02"]
        self.yt.lists["UUSH" + a[2:]] = ["sssssssss01"] + [f"m{i:010d}" for i in range(6)]
        for i in range(6):
            self.yt.add(f"m{i:010d}", 30, True, a, 3000 + i, 15 + i, f"연금 평소 {i}")
        self.yt.covers.add("sssssssss01")

    def test_explore_approve_analyze(self):
        r = web.job_shorts_explore("economic", 8, True)
        self.assertEqual(self.yt.count("search"), 2)
        self.assertTrue(all(q.get("videoDuration") == "short" for k, q in self.yt.calls if k == "search"))
        ex = json.loads((self.root / "economic" / "result" / "web" / "shorts_explore.json").read_text("utf-8"))
        rows = {x["id"]: x for x in ex["rows"]}
        self.assertEqual(set(rows), {"sssssssss01", "sssssssss02", "aaaaaaaaa01"})
        self.assertEqual(ex["excluded"], {"쇼츠 아님 (가로 영상)": 1, "쇼츠 아님 (3분 넘음)": 1,
                                          "조회수 부풀림 의심 — 광고·반복 재생 (표시만, 추천 안 함)": 1})
        self.assertEqual((rows["aaaaaaaaa01"]["flag"], rows["aaaaaaaaa01"]["success"], rows["aaaaaaaaa01"]["reason"]), ("부풀림 의심", False, ""))
        self.assertNotIn("aaaaaaaaa01", ex["checked"])                              # 부풀림 의심은 추천(체크) 안 함
        self.assertTrue(rows["sssssssss01"]["success"])
        self.assertIn("sssssssss01", ex["checked"])
        self.assertEqual(rows["sssssssss01"]["url"], "https://www.youtube.com/shorts/sssssssss01")
        self.assertEqual(r["quota_used"], 200 + 1 + 1)                             # 검색 2 + 영상 정보 1 + 채널 1
        # 롱폼 목록은 그대로 (따로)
        self.assertFalse((self.root / "economic" / "result" / "web" / "explore.json").exists())
        est = web.estimate_shorts("economic", 8, True)
        self.assertEqual((est["searches"], est["cached"]), (2, 2))                 # 다시 하면 캐시
        res = web.job_shorts_approve("economic", ["sssssssss01", "sssssssss02"], auto_whisper=False)
        sd = self.root / "economic" / "result" / "outliers" / "shorts"
        m1 = json.loads((sd / "S_sssssssss01" / "metadata.json").read_text("utf-8"))
        self.assertEqual((m1["kind"], m1["seconds"], m1["cover"], m1["transcript_status"]), ("shorts", 40, "oar2.jpg", "ok"))
        m2 = json.loads((sd / "S_sssssssss02" / "metadata.json").read_text("utf-8"))
        self.assertEqual(m2["cover"], "hqdefault.jpg")                               # 세로 표지가 없으면 4:3 표지
        self.assertTrue(m1["comments_complete"])
        self.assertEqual(res["whisper_needed"], 1)
        self.assertFalse(res["pushed"])                                              # 토큰 없음 — GitHub 에 안 올림
        self.assertEqual(res["shorts_success"], 1)
        self.assertGreaterEqual(res["shorts_baseline_fetched"], 1)                   # 채널 a 평소 쇼츠 (UUSH) — 채널 b 는 목록 없음(404)
        a = json.loads((sd / "analysis.json").read_text("utf-8"))
        self.assertEqual(a["success_cases"][0]["id"], "sssssssss01")
        self.assertEqual(a["success_cases"][0]["channel_ratio"], round(400000 / 3002.5, 1))
        self.assertTrue((sd / "analysis.md").is_file())
        self.assertEqual(web.used_shorts_ids("economic"), {"sssssssss01", "sssssssss02"})
        self.assertEqual(web.whisper_pending("economic", fresh=True), 1)            # 자막 못 받은 쇼츠 1개
        v = web.shorts_view("economic")
        self.assertEqual(v["success"], 1)
        plan = web.resume_plan("economic")
        self.assertEqual((plan["shorts_explore"], plan["shorts_baseline"]), (0, 0))
        # 롱폼 쪽이 쇼츠 폴더를 사례로 세지 않음 · 쇼츠만 있으면 다시 분석이 롱폼 분석 파일을 만들지 않음
        self.assertEqual(web.used_ids("economic"), set())
        with mock.patch.object(web, "wa", None):
            r2 = web.job_analyze("economic")
        self.assertEqual((r2["cases"], r2["shorts_cases"]), (0, 2))
        self.assertFalse((self.root / "economic" / "result" / "outliers" / "weekly.md").exists())

    def test_endpoint_mode_switch(self):
        web.job_shorts_explore("economic", 8, True)
        h = web.Handler.__new__(web.Handler)
        sent = {}
        h._send = lambda code, body, ctype=None: sent.update(code=code, body=body)
        h._host_ok = lambda: True
        h._authorized = lambda: True
        web.STATE["topic"] = "economic"
        for path, n in (("/api/explore?mode=shorts", 3), ("/api/explore", 0)):
            h.path = path
            h.do_GET()
            self.assertEqual(sent["code"], 200)
            self.assertEqual(len(sent["body"].get("rows") or []), n, path)
        h.path = "/api/estimate?weeks=8&kw=1&mode=shorts"
        h.do_GET()
        self.assertEqual(sent["body"]["searches"], 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
