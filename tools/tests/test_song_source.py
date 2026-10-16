# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — tools/song_source.py v1.0 classify() 시험 (실제 성공 사례 설명란에서 따온 꼴, 네트워크 없이).
"""python3 -m unittest test_song_source  (tools/tests 에서)"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import song_source as ss  # noqa: E402


class Classify(unittest.TestCase):
    def test_ai_made(self):
        d = "모든 음악은 쎄씨팝만의 감성으로 AI 제작 도구를 활용해 직접 기획·제작한 오리지널 콘텐츠입니다."
        self.assertEqual(ss.classify("첫 곡부터 감성 미쳐버린 8090 플레이리스트", d)[0], "AI 음악")

    def test_no_ai_is_not_ai(self):
        d = "영상 내 음원 및 이미지의 무단 AI 학습을 엄격히 금지합니다. #NoAImusic"
        self.assertNotEqual(ss.classify("일할때 틀어놓기 좋은 지브리 재즈", d)[0], "AI 음악")

    def test_existing_tracklist(self):
        d = "00:00 아이유 - 밤편지\n03:40 성시경 - 거리에서\n07:50 김동률 - 감사\n12:10 이문세 - 옛사랑"
        src, n_tl, n_art = ss.classify("발라드 모음", d)
        self.assertEqual((src, n_tl, n_art), ("기존 곡 모음", 4, 4))

    def test_original_copyright(self):
        d = "📌 본 영상의 모든 음원은 저작권 문제가 없는 음원으로 제작되었습니다. 무단 도용 및 재업로드를 금지합니다."
        self.assertEqual(ss.classify("샹송이 이렇게 좋은줄 몰랐습니다", d)[0], "직접 만든 곡")

    def test_cover_title(self):
        self.assertEqual(ss.classify("사랑했어요 - 김현식 #윤가연 COVER", "")[0], "커버·리메이크")

    def test_hashtag_only_kpop(self):
        self.assertEqual(ss.classify("playlist | 우리 사랑은 필름 같았으면 해요", "#playlist #음악 #kpop")[0], "기존 곡으로 보임")

    def test_unknown(self):
        self.assertEqual(ss.classify("고양이 카페에 놀러 올래?", "집중할 때 듣기 좋은 힐링 재즈 음악이야")[0], "알 수 없음")


if __name__ == "__main__":
    unittest.main()
