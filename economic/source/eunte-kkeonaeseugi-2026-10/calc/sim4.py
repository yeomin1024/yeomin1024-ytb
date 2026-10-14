"""draft3 검산 v3.4 — 2026-10-14
 v3.4 ① 배우자 기본공제: 아내가 연금저축을 종합과세로 신고하면 아내 종합소득금액이 100만 원을 넘어 남편이 배우자 공제(150)를 못 받는다
        (소득세법 제50조 ①2호). 부부 세금을 함께 보고 아내 분리/종합 중 '부부 합계'가 싼 쪽을 고른다. 70세부터 배우자 경로우대 100도 넣음(제51조).
      ② 끝나는 때: 한 사람 1,500 선 때문에 꺼내지 못해 '돈이 남았는데 끝'으로 잡히던 것을 고침 — 선을 넘겨서라도 꺼내고, 돈이 다 떨어진 해에 끝.
 v3.3 (사적연금 1,500 초과분은 피부양자 소득에 포함)
 v3.2 (국민연금 과세 몫 65% — v3.1 은 100%로 봐서 A 부부 연금저축 세금을 크게 잡았음)
 v3.1 (퇴직소득세 감면 구간: 실제 수령 1~10년 30%·11~20년 40%·21년~ 50% — 2026.1.1 이후 수령분) (연금저축 세금 = 16.5%·저율 분리·종합과세 중 싼 쪽, tax.py) — 5억 은퇴 부부, 꺼내 쓰는 순서별 세금·피부양자·버티는 나이 (만 원).
가정: 실질 기준(예금·계좌 수익 연 3.5% = 물가, 그래서 원금 실질가치 유지) — 대신 해마다 낸 세금만큼 자산이 줄어든다.
계좌(IRP·연금저축) 안에서 불어난 몫은 나중에 꺼낼 때 연금소득세를 내므로 그해 연금세율로 미리 잡는다(근사).
퇴직소득세(근속연수마다 다름)·건보료(재산마다 다름)는 숫자에 넣지 않는다. 연구·교육용 예시 — 세무·투자 권유 아님."""
from tax import pension_deduction, income_tax, sep_rate
RATE, NEED = 0.035, 1800
PUB_TAX_SHARE = 0.65   # 국민연금 중 세금이 붙는 몫 (소득세법 제20조의3 ②: 2002년 이후 낸 몫만 과세) — 1961년생 예시 가정. 피부양자 소득에는 전부 들어감(시행령 제41조)
PUB = {"h": 110 * 12, "w": 40 * 12}

def _gtax(total, ded):
    """연금소득만 있는 사람의 종합소득세(지방세 포함). total = 종합과세 대상 연금 합계, ded = 인적공제 합계."""
    inc = total - pension_deduction(total)
    t = income_tax(max(inc - ded, 0))
    return (max(t - 7, 0) if t > 0 else 0) * 1.1, inc      # 표준세액공제 7, 지방세 10%

def household_tax(xh, xw, age):
    """그해 부부 연금 세금 증가분(국민연금만 있을 때 대비) — 아내 신고 방식을 고르면 남편 배우자 공제가 달라지므로 함께 본다.
    반환: (세금, 남편 방식, 아내 방식)"""
    ph, pw = PUB["h"] * PUB_TAX_SHARE, PUB["w"] * PUB_TAX_SHARE
    old = 100 if age >= 70 else 0
    base_w, inc_w0 = _gtax(pw, 150 + old)
    opts_w = [("-", 0.0, inc_w0)] if xw <= 0 else []
    if xw > 0:
        opts_w.append(("분리", xw * (sep_rate(age) if xw <= 1500 else 0.165), inc_w0))   # 분리과세는 종합소득금액에 안 들어감
        tw, inc_w = _gtax(pw + xw, 150 + old)
        opts_w.append(("종합", tw - base_w, inc_w))
    base_h_ok, _ = _gtax(ph, 150 + 150 + old + old)          # 기준: 국민연금만 있을 때(아내 공제 받음)
    best = None
    for hw_w, tw, inc_w in opts_w:
        ok = inc_w <= 100                                    # 배우자 소득금액 100만 원 이하
        ded_h = 150 + (150 if ok else 0) + old + (old if ok else 0)
        th0, _ = _gtax(ph, ded_h)
        opts_h = [("-", th0 - base_h_ok)] if xh <= 0 else [
            ("분리", xh * (sep_rate(age) if xh <= 1500 else 0.165) + th0 - base_h_ok),
            ("종합", _gtax(ph + xh, ded_h)[0] - base_h_ok)]
        hw_h, th = min(opts_h, key=lambda o: o[1])
        cand = (th + tw, hw_h, hw_w)
        if best is None or cand[0] < best[0]: best = cand
    return best

def pen_rate(age):
    return 0.055 if age < 70 else 0.044 if age < 80 else 0.033

def run(name, plan, dep, pen, irp, verbose=False):
    dep, pen = dict(dep), dict(pen)
    tot = dict(pen_tax=0.0, int_tax=0.0, defer=0.0); lost = []; irp_n = 0; band = {"30%": 0, "40%": 0, "50%": 0}; rows = []
    age = 65
    while True:
        assets = sum(dep.values()) + sum(pen.values()) + irp
        intr = {p: dep[p] * RATE for p in dep}
        draw = plan(age, dep, pen, irp, irp_n)
        got = sum(draw.values())
        for p in ("h", "w"):
            dep[p] -= draw.get("dep_" + p, 0); pen[p] -= draw.get("pen_" + p, 0)
        if draw.get("irp", 0) > 0:
            irp_n += 1; irp -= draw["irp"]; band["30%" if irp_n <= 10 else "40%" if irp_n <= 20 else "50%"] += draw["irp"]
        t_pen, hh, ww = household_tax(draw.get("pen_h", 0), draw.get("pen_w", 0), age)
        how = {"h": hh, "w": ww}
        t_int = sum(intr.values()) * 0.154
        t_def = (sum(pen.values()) + irp) * RATE * pen_rate(age)
        tot["pen_tax"] += t_pen; tot["int_tax"] += t_int; tot["defer"] += t_def
        # 세금만큼 자산 감소: 예금 → 연금저축 → IRP 순
        due = t_pen + t_int + t_def
        for k in ("h", "w"):
            x = min(dep[k], due); dep[k] -= x; due -= x
        for k in ("h", "w"):
            x = min(pen[k], due); pen[k] -= x; due -= x
        irp -= min(irp, due)
        fin = {p: intr[p] if intr[p] > 1000 else 0 for p in intr}
        # v3.3: 사적연금(연금저축 세액공제분·수익)이 한 사람 1년 1,500만 원을 넘으면 종합소득이 되어 피부양자 소득에 들어감
        #       (건보공단 챗봇 답변 2026-10-14, 사용자 확인). 1,500 이하(분리과세)·퇴직금 연금(이연퇴직소득)은 안 들어감
        priv = {p: (draw.get('pen_' + p, 0) if draw.get('pen_' + p, 0) > 1500 else 0) for p in PUB}
        ded = {p: PUB[p] + fin[p] + priv[p] for p in PUB}
        if max(ded.values()) > 2000: lost.append(age)
        rows.append((age, draw, t_pen, t_int, t_def, dict(dep), dict(pen), irp, ded, how))
        if got < NEED - 0.01 or sum(dep.values()) + sum(pen.values()) + irp <= 0.01:
            end = age + got / NEED
            break
        age += 1
    y = int(end); m = round((end - y) * 12)
    life = tot["pen_tax"] + tot["int_tax"] + tot["defer"]
    print(f"{name}: 첫해 세금 {rows[0][2] + rows[0][3]:.1f} (연금 {rows[0][2]:.1f} + 이자 {rows[0][3]:.1f}) · 평생 세금 {life:.0f} (연금 {tot['pen_tax']:.0f} 이자 {tot['int_tax']:.0f} 계좌 안 몫 {tot['defer']:.0f}) · 피부양자 기준 넘는 해 {lost[0] if lost else '-'}~{lost[-1] if lost else ''} ({len(lost)}년) · 버팀 {y}세 {m}개월 · IRP {band}")
    if verbose:
        for r in rows:
            a, d, tp, ti, td, dp, pn, ir, dd, hw = r
            print(f"  {a}세 {d} 세금 연금 {tp:.1f}({hw['h']}/{hw['w']}) 이자 {ti:.1f} 계좌안 {td:.1f} 남음 예금 {dp['h']:.0f}/{dp['w']:.0f} 연금저축 {pn['h']:.0f}/{pn['w']:.0f} IRP {ir:.0f} 피부양자소득 {dd['h']:.0f}")
    return life, end, lost, rows

def plan_a(age, dep, pen, irp, n):          # 한 통장씩: 남편 연금저축 → 아내 연금저축 → 남편 예금 → 아내 예금
    out, need = {}, NEED
    for k in ("pen_h", "pen_w", "dep_h", "dep_w"):
        bal = (pen if k.startswith("pen") else dep)[k[-1]]
        x = min(bal, need)
        if x > 0: out[k] = x; need -= x
        if need <= 0: break
    return out

def plan_b(age, dep, pen, irp, n, small=100):
    out, need = {}, NEED
    x = min(irp, small if n < 10 else NEED)          # 실제 수령 10년 채우기 전엔 조금, 11년째부터 크게
    if x > 0: out["irp"] = x; need -= x
    for k in ("dep_h", "dep_w"):                      # 예금(해마다 이자세) 먼저
        x = min(dep[k[-1]], need)
        if x > 0: out[k] = x; need -= x
    for k, cap in (("pen_h", 1000), ("pen_w", 800)):  # 연금저축은 마지막, 한 사람 1,500 아래
        x = min(pen[k[-1]], cap, need)
        if x > 0: out[k] = x; need -= x
    for k in ("pen_h", "pen_w"):
        x = min(pen[k[-1]] - out.get(k, 0), 1500 - out.get(k, 0), need)
        if x > 0: out[k] = out.get(k, 0) + x; need -= x
    return fill_rest(out, need, dep, pen, irp)

def fill_rest(out, need, dep, pen, irp):
    """v3.4: 선을 지켜서는 생활비가 모자라는 마지막 해 — 남은 돈이 있으면 선을 넘겨서라도 꺼낸다."""
    for k in ("dep_h", "dep_w", "pen_h", "pen_w"):
        if need <= 0: break
        bal = (pen if k.startswith("pen") else dep)[k[-1]] - out.get(k, 0)
        x = min(bal, need)
        if x > 0: out[k] = out.get(k, 0) + x; need -= x
    if need > 0 and irp - out.get("irp", 0) > 0:
        x = min(irp - out.get("irp", 0), need); out["irp"] = out.get("irp", 0) + x
    return out

if __name__ == "__main__":
    import sys
    v = "-v" in sys.argv
    A = run("A 부부", plan_a, {"h": 30000, "w": 10000}, {"h": 6000, "w": 4000}, 0, v)
    B = run("B 부부", plan_b, {"h": 10000, "w": 10000}, {"h": 6000, "w": 4000}, 20000, v)
    print(f"차이: 평생 세금 {A[0] - B[0]:.0f} ({A[0] / B[0]:.2f}배) · 버팀 {(B[1] - A[1]) * 12:.0f}개월 더")
