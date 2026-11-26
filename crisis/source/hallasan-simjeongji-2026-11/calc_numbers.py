# VERSION: v1.0 — 2026-11-26 — 한라산 심정지 편 대본 v3.0 의 숫자를 모두 여기서 계산 (CLAUDE.md '숫자는 계산 코드 출력만').
#   입력 값은 보도·공식 발표 숫자 그대로 (출처는 근거.md) · 출력 = 대본에 쓰는 말.
#   사용: python3 crisis/source/hallasan-simjeongji-2026-11/calc_numbers.py
# CHANGELOG
#   v1.0 2026-11-26 — 처음 (사용자 지시 "대본을 공통 규칙 만족하도록 한번 수정해서 알려줘봐").
import datetime as dt
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] [%(asctime)s] %(message)s", datefmt="%Y-%m-%dT%H:%M:%S")
log = logging.getLogger("calc")

def minutes(hhmm: str) -> int:
    h, m = map(int, hhmm.split(":"))
    return h * 60 + m

def main() -> dict:
    out = {}
    # 2023-03-26 한라산 둘레길 (서울신문 2023-03-27): 13:48 실종 신고 → 1시간 만에 심정지 발견 → 15:28 사망
    d = minutes("15:28") - minutes("13:48")
    out["신고→사망"] = f"{d // 60}시간 {d % 60}분"
    out["요일"] = "일월화수목금토일"[dt.date(2023, 3, 26).weekday() + 1] + "요일"
    # 국립공원공단 2024-08 보도자료: 2014~2023 사망 167명 · 심장돌연사 84명 · 추락사 54명 · 익사 15명
    total, cardiac, fall = 167, 84, 54
    out["심정지 비율"] = f"{cardiac / total * 100:.1f}% → '절반'"
    out["심정지-추락 차이"] = f"{cardiac - fall}명"
    # 질병관리청 2024 급성심장정지조사: 일반인 심폐소생술 했을 때 14.4% · 안 했을 때 6.1%
    ratio = 14.4 / 6.1
    out["생존율 배수"] = f"{ratio:.2f}배 → '두 배 넘게'"
    # 2016 미국 오리건 연구 (Marijon 등): 신호가 있던 사람 중 119 먼저 연락 19%
    out["119 먼저 연락"] = f"19% {'<' if 19 < 20 else '>='} 20% → '다섯 명 중 한 명도 안 됨'"
    # 2026-10-11 운악산 → 2026-10-26 성판악
    gap = (dt.date(2026, 10, 26) - dt.date(2026, 10, 11)).days
    out["운악산→성판악"] = f"{gap}일 → '보름'"
    for k, v in out.items():
        log.info("CALC item=%s value=%s", k, v)
    return out

if __name__ == "__main__":
    main()
