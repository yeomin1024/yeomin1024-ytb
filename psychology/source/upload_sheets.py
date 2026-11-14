#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-14 — 심리 네 편 업로드 시트 upload.md (사용자 지시 "업로드 시트 만들고 uploads 브랜치에 올려")
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-14 | 최초 — 제목(package.json) · 설명란(소개 2줄 · 챕터 · 출처 · 알려 드립니다 · 해시태그 2) · 챕터 명령 · 태그 · 고정 댓글 · 설정 · 점검 | build · main |
"""psychology/source/<영상ID>/upload.md 를 쓴다 — tools/youtube_upload.py(read_sheet) · tools/upload_pack.py(check) · PC 업로드 화면이 읽는 꼴.

- 1번 제목 = package.json title (페르소나 관문 title 단계 통과 — 글자 그대로) · 썸네일 본안 thumbnail_1 · 1-1 실험안 = thumbnail_2·3 (같은 제목).
- 2번 설명란: 소개 2줄(대본에 있는 말로) · ■ 챕터(0:00 은 올릴 때 SRT 로 다시 계산) · ■ 출처(대본_근거.md 1번 표 — 지금 대본에 남은 것만) ·
  ■ 알려 드립니다(연구·교육용 · 진단 아님 · 위기 번호) · 해시태그 2개.
- 3번 챕터 명령 = 대본 장(-줄) 시작 문장 번호. 4번 태그 = 편 낱말 + psychology/tag_candidates.md 상위(채널 5곳 이상이 쓴 태그).
실행: python3 psychology/source/upload_sheets.py   (그 뒤 python3 tools/upload_pack.py check psychology <영상ID…>)
※ 연구·교육용 영상 — 심리 진단·치료가 아님.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VERSION = "v1.0"
DATE = "2026-11-14"
CRISIS = "24시간 정신건강 상담 전화 1577-0199 · 자살예방 상담 전화 109 · 당장 위험하면 119"
NOTICE = ("이 영상은 연구와 상담 글을 바탕으로 한 교육용 콘텐츠이며, 심리 진단이나 치료가 아닙니다.\n"
          "영상 속 인물과 장면은 이해를 돕기 위해 만든 것이고, 특정 사람의 이야기가 아닙니다. 연구는 대부분 한 번 조사한 결과라 원인을 밝힌 것이 아니며, 나에게 꼭 맞지 않을 수 있습니다.\n"
          "힘든 날이 오래 이어지면 가까운 정신건강의학과나 정신건강복지센터에 먼저 전화로 물어보세요.")
COMMON_TAGS = ["심리학", "심리", "인간관계", "자존감", "마음", "마음공부", "감정조절", "정신건강", "심리상담"]

# 순서 = 추천 공개 순서 (첫 영상 추천 그릇 → 같은 '엄마' 주제 두 편은 떨어뜨림 — 반복 콘텐츠 정책)
EP = {
    "geureut-moa-2026-11": {
        "order": 1,
        "intro": "식당에서 빈 그릇을 한쪽에 모아 두는 사람에게서 볼 수 있는 특징 세 가지를, 성격 이론과 닮은 연구, 비슷한 영상의 실제 댓글로 짚었습니다.\n"
                 "이 습관이 지나칠 때 알아 둘 점과, 집에서 정리 습관이 다를 때 할 일도 정리했습니다.",
        "chapters": "1=식당에서 그릇을 모으는 사람;16=끝까지 마무리하려는 성향;28=치울 사람을 먼저 떠올림;45=착해서만이 아니라 불편해서;67=지나칠 때 알아 둘 점;80=집에서 습관이 다를 때;95=정리",
        "sources": [
            "성격 5요인(Big Five)의 성실성 — 성격심리학 교과서적 정의",
            "Horncastle, Ludlow, Gutierrez (2022). Journal of Obsessive-Compulsive and Related Disorders, 35, 100762 ('딱 맞지 않는 느낌'과 강박 증상 점수 — 메타분석).",
            "Coles, Frost, Heimberg, Rhéaume (2003). Behaviour Research and Therapy, 41, 681–700 ('딱 맞지 않는 느낌' 연구).",
            "강박장애 설명: 미국정신의학회 DSM-5 진단 기준 (진단은 전문가가 합니다)",
            "댓글: 의자를 다시 넣는 사람을 다룬 유튜브 영상의 댓글 (좋아요 순 · 2026년 11월 기준 · 작성자 정보는 싣지 않음)",
        ],
        "notice_extra": "그릇을 모으는 행동만 따로 조사한 연구는 아직 없어, 닮은 성향을 다룬 연구와 댓글로 짚었습니다.",
        "crisis": "24시간 정신건강 상담 전화 1577-0199",
        "hashtags": "#심리학 #인간관계",
        "tags": ["그릇 모으는 사람", "식당 그릇", "식당 예절", "성실성", "성격 5요인", "배려", "공감", "강박", "정리 습관", "부부 정리 습관", "설거지", "심리학적 특징"],
        "pin": "식당에서 그릇을 모아 두시나요? 세 가지 가운데 어느 마음에 가장 가까운지, 아니면 그냥 배운 습관인지 댓글로 알려 주세요.\n집에서 정리 습관이 달라 생긴 일이 있다면 함께 나눠 주세요.\n연구와 댓글을 바탕으로 한 교육용 영상이며, 심리 진단이 아닙니다.",
    },
    "eomma-gibun-2026-11": {
        "order": 2,
        "intro": "어릴 때 엄마 기분부터 살피던 사람에게서 자주 이야기되는 특징 다섯 가지를 정리했습니다.\n"
                 "엄마를 탓하자는 것이 아니라 내가 힘들었던 마음을 알아보자는 이야기이며, 이미 이렇게 살고 있다면 지금 해 볼 수 있는 것도 담았습니다.",
        "chapters": "1=엄마 기분부터 살피던 아이;19=먼저 알아 둘 말, 부모화;29=표정을 빨리 알아챔;39=거절이 어려움;48=내 기분은 뒤로;64=쉬면 불편함;73=돌보는 일을 잘함;82=지금 해 볼 수 있는 것;103=정리",
        "sources": [
            "다섯 가지 특징(상담 전문가들의 글 — 연구로 하나하나 확인된 목록은 아님): Psychology Today (2019) 'Did you have to grow up too soon?' · Psychotherapy Networker 'The Parentification Trap' · Simply Psychology 'Parentification'",
            "Dariotis 외 (2023). Parentification Vulnerability, Reactivity, Resilience, and Thriving. International Journal of Environmental Research and Public Health, 20(13), 6197.",
            "신말숙·심혜원 (2017). 부모화에 관한 이론적 고찰: 상담에서의 시사점을 중심으로. 한국심리학회지: 일반, 36(1), 61–80.",
            "서강대학교 일반대학원 심리학과 석사 논문 (2020). 부모화가 우울에 미치는 영향: 자기침묵과 외로움을 중심으로 (20대 387명 온라인 설문).",
        ],
        "notice_extra": "엄마를 예로 들었지만, 아빠나 다른 어른이었어도 비슷할 수 있습니다.",
        "crisis": "24시간 정신건강 상담 전화 1577-0199 · 자살예방 상담 전화 109",
        "hashtags": "#부모화 #심리학",
        "tags": ["부모화", "정서적 부모화", "엄마 눈치", "눈치 보는 성격", "착한 아이 콤플렉스", "거절 못하는 성격", "감정 표현", "가족 상처", "엄마와 딸", "어린 시절 상처"],
        "pin": "다섯 가지 가운데 나와 가장 닮은 것은 몇 번째였나요? 오늘 내 기분을 한 낱말로 남겨 주셔도 좋습니다.\n연구와 상담 글을 바탕으로 한 교육용 영상이며, 심리 진단이 아닙니다.\n많이 힘드시면 24시간 정신건강 상담 전화 1577-0199 에 먼저 걸어 보세요.",
    },
    "sangcheo-gonggyeok-2026-11": {
        "order": 3,
        "intro": "가볍게 한 말에 날카롭게 받아치는 사람, 혹시 나일 때는 없었나요? 거절로 상처받은 뒤 날카로워지는 까닭 세 가지를 연구로 짚었습니다.\n"
                 "이유를 아는 것은 감싸려는 것이 아니라 멈추기 위해서이며, 내가 이런 쪽일 때와 가까운 사람이 이럴 때 해 볼 수 있는 것도 정리했습니다.",
        "chapters": "1=날카롭게 받아치는 사람;17=바탕이 된 연구;25=거절의 낌새에 미리 날을 세움;35=남의 행동을 공격으로 읽음;57=내가 누구인지 흔들림;71=내가 이런 쪽이라면;86=가까운 사람이 이렇다면;97=정리",
        "sources": [
            "Quarmley 외 (2022). Testing effects of social rejection on aggressive and prosocial behavior. Aggressive Behavior, 48(6), 529–545 (실험 연구 메타분석).",
            "Gao, Assink, Liu, Chan, Ip (2021). Trauma, Violence, & Abuse, 22(1), 125–135 (거부 민감성과 공격 — 연구 52편 메타분석).",
            "이건희·이민규 (2023). 한국심리학회지: 문화 및 사회문제, 29(4), 477–496 (대학생 250명 온라인 설문).",
            "댓글: 한 강연 영상의 댓글 (공감 9천여 개 · 2026년 11월 기준 · 작성자 정보는 싣지 않음)",
        ],
        "notice_extra": "연구는 함께 나타나는 약한 연결을 본 것이라 순서는 아직 모릅니다. '해 볼 것' 세 가지는 연구로 효과를 확인한 방법이 아닙니다. 말이 위협이나 폭력으로 번지면 이해보다 내 안전이 먼저입니다.",
        "crisis": "24시간 정신건강 상담 전화 1577-0199",
        "hashtags": "#인간관계 #심리학",
        "tags": ["거부 민감성", "적대적 귀인 편향", "자기 개념", "공격성", "상처받은 사람", "예민한 사람", "날카로운 말", "말투", "직장 인간관계", "대인관계", "관계심리"],
        "pin": "애매한 말에 날카롭게 받아친 적이 있나요? 그때 '다른 뜻일 수도 있다'고 떠올릴 수 있었다면 무엇이 달라졌을지 나눠 주세요.\n연구를 바탕으로 한 교육용 영상이며, 심리 진단이 아닙니다.",
    },
    "eomma-hasoyeon-2026-11": {
        "order": 4,
        "intro": "엄마의 하소연을 딸 혼자 다 받아 주면 안 되는 이유 세 가지와, 전화를 끊지 않고도 나를 지키는 말 네 가지를 정리했습니다.\n"
                 "엄마 속상함이 틀렸다는 뜻이 아니라, 오래 혼자 들어 온 무게를 나누자는 이야기입니다.",
        "chapters": "1=엄마 전화가 오면;12=왜 딸에게 몰릴까;22=엄마의 걱정이 내 걱정으로;32=저절로 가까워지지 않음;43=다른 가족과도 멀어짐;64=이미 지쳤다는 신호;74=끊지 않고 나를 지키는 말 네 가지;101=정리",
        "sources": [
            "Dariotis 외 (2023). Parentification Vulnerability, Reactivity, Resilience, and Thriving. International Journal of Environmental Research and Public Health, 20(13), 6197.",
            "Koerner, Wallace, Lehman, Raymond (2002). Mother-to-Daughter Disclosure After Divorce: Are There Costs and Benefits? Journal of Child and Family Studies, 11(4), 469–483.",
            "Schrodt & Afifi (2007). Communication Monographs, 74(2), 200–228 (부모의 상대 부모 흉과 자녀의 '사이에 끼인 느낌').",
        ],
        "notice_extra": "아들이나 외동이어도, 엄마의 하소연을 혼자 받는 자녀라면 같이 들어 보세요. 폭력·외도·빚처럼 엄마가 실제로 피해를 입는 일은 흉이 아니며, 도움받을 곳을 함께 찾아 주세요.",
        "crisis": "여성긴급전화 1366 (24시간) · 자살예방 상담 전화 109 · 24시간 정신건강 상담 전화 1577-0199 · 당장 위험하면 119",
        "hashtags": "#엄마와딸 #심리학",
        "tags": ["엄마 하소연", "감정 쓰레기통", "엄마와 딸", "정서적 부모화", "부모화", "가족 갈등", "부모 이혼", "사이에 끼인 느낌", "경계 세우기", "가족 상처", "부모와 관계"],
        "pin": "엄마 전화가 오면 숨부터 고르게 되시나요? 네 가지 말 가운데 오늘 먼저 꺼내 볼 말은 무엇인지 남겨 주세요.\n연구를 바탕으로 한 교육용 영상이며, 심리 진단이 아닙니다.\n폭력·폭언이라면 여성긴급전화 1366, '죽고 싶다'는 말을 들었다면 그날 자살예방 상담 전화 109 에 함께 걸어 보세요.",
    },
}


def log(stage: str, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def sentence_count(ep: str) -> int:
    n = 0
    for ln in (ROOT / "psychology/source" / ep / f"{ep}.txt").read_text("utf-8").splitlines():
        if ln.strip() and not ln.startswith("-") and not ln.startswith("#"):
            n += 1
    return n


def build(ep: str, sp: dict) -> str:
    src = ROOT / "psychology/source" / ep
    pkg = json.loads((src / "package.json").read_text("utf-8"))
    title = pkg["title"]
    n = sentence_count(ep)
    for part in sp["chapters"].split(";"):
        k = int(part.split("=")[0])
        if not 1 <= k <= n:
            raise SystemExit(f"[SHEET] {ep} 챕터 문장 번호 {k} 가 대본(1~{n}) 밖")
    names = [p.split("=", 1)[1] for p in sp["chapters"].split(";")]
    desc = (sp["intro"] + "\n\n■ 챕터\n" + "\n".join(f"0:00 {x}" for x in names) + "\n\n■ 출처\n" + "\n".join(f"- {s}" for s in sp["sources"])
            + "\n\n■ 알려 드립니다\n" + NOTICE + "\n" + sp["notice_extra"] + "\n\n■ 도움받을 곳\n" + sp["crisis"] + "\n\n" + sp["hashtags"])
    tags = []
    for t in sp["tags"] + COMMON_TAGS:
        if t not in tags:
            tags.append(t)
    th = pkg["thumb_main"]
    gate = json.loads((src / "persona_loop.json").read_text("utf-8"))["items"][ep]
    gl = []
    for st in ("title", "script_exit", "script_rebuttal"):
        rs = gate.get(st, {}).get("rounds", [])
        gl.append(f"{st} {'✅' if rs and rs[-1]['pass'] else '❌'} {len(rs)}회차")
    L = [f"# {ep} 업로드 시트 (롱폼 · 심리)", "",
         f"버전: {VERSION} — {DATE} — 최초 (사용자 지시 \"업로드 시트 만들고 uploads 브랜치에 올려\") · 생성 `psychology/source/upload_sheets.py` {VERSION}.",
         f"기준 파일: 대본 `{ep}.txt` ({n}문장) · 오디오 `narration.mp3` · 자막 `{ep}.srt`(align-audio — 실제 오디오) · 영상 `psychology/out/{ep}/final_1080p.mp4`(만스피 꼴 · `video/episodes/{ep}/`) · 썸네일 `thumbnails/thumbnail_1~3.jpg`.",
         "", "> 업로드 채널 = 심리 채널. 연구·교육용 콘텐츠 — 심리 진단·치료가 아님.",
         "> ⚠ `psychology/youtube_channel.json` 이 아직 없음 → 올리는 도구가 키의 채널을 확인하지 못함. PC 업로드 화면 psychology 탭에는 **심리 채널 키**만 넣는다 (처음 올린 뒤 화면의 '기억'으로 채널 ID 를 남김).",
         "", "## 1. 제목 (본안)", "", "```", title, "```",
         f"- 짝 썸네일 `thumbnail_1.jpg` (「{th[0]} / {th[1]}」 + 말풍선 「{pkg['thumb_sub'].strip(chr(34))}」 — 그림 `images/TH-CHAR.jpg` ChatGPT + 문구 코드 `thumb.mjs`).",
         "- 제목·썸네일 문구는 package.json 그대로 — 페르소나 관문 title 단계 통과 (`persona_loop.json`). `title_fit`: 모바일·PC 모든 화면 2줄 안 ✅.",
         "", "## 1-1. 실험안 — 스튜디오 '테스트 및 비교'용 (API 로 올리지 않음 · 공개 뒤 사용자가 넣음)", "",
         "| 안 | 제목 | 썸네일 |", "|---|---|---|",
         f"| 실험 1 | (본안과 같음) | `thumbnail_2.jpg` — 보조 문구(말풍선) 없음 |",
         f"| 실험 2 | (본안과 같음) | `thumbnail_3.jpg` — 같은 낱말 · 강조 색 바꿈 + 노란 말풍선 |",
         "- 글이 다른 실험 제목은 만들지 않음 (새 문구는 persona_loop title 단계부터).",
         "", "## 2. 설명란 (그대로 복사)", "", "```", desc, "```",
         "", "## 3. 챕터 다시 계산하기 (문장 번호 기준 — 실제 내레이션 SRT)", "", "```",
         f"python tools/srt_tool.py upload psychology/source/{ep}/{ep}.txt psychology/source/{ep}/{ep}.srt --chapters \"{sp['chapters']}\"", "```",
         "", "## 4. 태그", "", "```", ", ".join(tags), "```",
         "", "## 5. 고정 댓글", "", "```", sp["pin"], "```",
         "", "## 7. 업로드 설정", "", "| 항목 | 값 |", "|---|---|",
         "| 공개 상태 | 비공개로 올린 뒤 예약 공개 |",
         f"| 추천 공개 순서 | {sp['order']}번째 — 그릇 → 엄마 기분 → 상처 → 하소연, 하루에 한 편 (첫 영상 추천 = 그릇 · '엄마' 두 편은 떨어뜨림 — 반복 콘텐츠 정책) |",
         "| 썸네일 | `thumbnails/thumbnail_1.jpg` (본안 · 1280×720) |",
         f"| 자막 | `{ep}.srt` (실제 오디오에 맞춤) |",
         "| 자막 올리기 | 예 |",
         "| 카테고리 | 교육 |", "| 동영상 언어 · 기본 언어 | 한국어 · ko |", "| 오디오 언어 | ko |",
         "| 시청자층 | 아동용 아님 |", "| 유료 프로모션 | 없음 |",
         "| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 · 그림이 AI 생성) |",
         "", "## 8. 점검 (설명란에 넣지 않음)", "",
         f"- 페르소나 관문 (`persona_loop.json`): {' · '.join(gl)} — 이탈·반론 단계는 상한(5회차, 일부 7회차)까지 돌린 뒤 사용자가 영상·썸네일·업로드로 진행 (2026-11-13). 통과로 적지 않음.",
         "- 숫자·연구는 `대본_근거.md` 1번 표 · 지금 대본에서 뺀 연구는 출처에 넣지 않음.",
         "- 잡음 검사 `audio_check.md`: 보고 수준 후보만 (고칠 것 없음).",
         "- 영상: render check 0 · layout-check 0 · 완성 mp4 장면을 Claude 가 봄 · 음량 -14 LUFS 안팎 · 트루 피크 -1.5 dBTP 이하.",
         "- 다른 사람의 영상 파일은 받지도 넣지도 않음 · 댓글은 뜻만 (작성자 정보 없음).",
         "", "## 9. 결과 (업로드 후)", "", "- (아직 없음)", ""]
    return "\n".join(L)


def main() -> int:
    for ep, sp in sorted(EP.items(), key=lambda kv: kv[1]["order"]):
        md = build(ep, sp)
        p = ROOT / "psychology/source" / ep / "upload.md"
        p.write_text(md, encoding="utf-8")
        log("SHEET", ep=ep, order=sp["order"], file=str(p.relative_to(ROOT)), bytes=len(md.encode()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
