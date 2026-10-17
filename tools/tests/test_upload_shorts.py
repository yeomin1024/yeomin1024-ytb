# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-17 — tools/youtube_upload.py v1.8 시험: '<영상ID>-shorts' 는 source/<영상ID>/shorts/ 에서 시트를 읽고,
#          쇼츠는 썸네일을 찾지도 올리지도 않는다 (dry-run — 네트워크·키 없음, 임시 폴더만).
#          사용자 지시 2026-10-17 "아니 공개 자동예약으로 올려 쇼츠도 하나 올려보고".
"""cd tools/tests && python3 -m unittest test_upload_shorts -v"""
import contextlib
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import youtube_upload as yu  # noqa: E402

SHEET = """# 시트

## 1. 제목

```
쇼츠 제목
```

## 2. 설명란

```
쇼츠 설명
#태그
```

## 4. 태그

```
가, 나
```

## 6. 업로드 설정

| 항목 | 값 |
|---|---|
| 변경되거나 합성된 콘텐츠 | 예 |
"""


class Shorts(unittest.TestCase):
    def test_src_dir(self):
        self.assertEqual(yu.src_dir("economic", "a-2026-10"), yu.ROOT / "economic" / "source" / "a-2026-10")
        self.assertEqual(yu.src_dir("economic", "a-2026-10-shorts"), yu.ROOT / "economic" / "source" / "a-2026-10" / "shorts")

    def test_dry_run_reads_shorts_sheet_and_skips_thumbnail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            d = root / "economic" / "source" / "a-2026-10" / "shorts"
            (d / "thumbnails").mkdir(parents=True)
            (d / "upload.md").write_text(SHEET, "utf-8")
            (d / "thumbnails" / "thumbnail_1.png").write_bytes(b"not used")
            buf = io.StringIO()
            env = {k: v for k, v in os.environ.items() if not k.startswith("YOUTUBE_")}
            with mock.patch.object(yu, "ROOT", root), mock.patch.dict(os.environ, env, clear=True), \
                    mock.patch.object(yu, "prepare_thumbnail", side_effect=AssertionError("쇼츠 썸네일을 자르면 안 됨")), \
                    contextlib.redirect_stdout(buf):
                yu.run("economic", "a-2026-10-shorts", dry_run=True)
            out = buf.getvalue()
            self.assertIn("title_chars=5", out)
            self.assertIn("reason=쇼츠", out)
            self.assertIn("영상 파일 없음", out)


if __name__ == "__main__":
    unittest.main()
