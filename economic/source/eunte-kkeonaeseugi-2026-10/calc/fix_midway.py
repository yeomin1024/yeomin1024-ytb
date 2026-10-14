"""VERSION: v1.1 — 2026-10-14 — sim4.py v3.4 사용(배우자 공제·끝나는 조건 고침), 고친 계획도 선을 넘겨서라도 돈이 다 떨어질 때까지 꺼냄
A 부부가 중간에 고치면? — sim4.py 와 같은 가정으로, 'fix_age 세 첫해까지 A 방식 → 그해 말에 고침'.
고치는 것: ① 남편 이름 예금을 부부 반반으로 (배우자 증여는 10년 6억 원까지 증여세 없음 — 상증세법 제53조, 별도 확인)
          ② 그다음 해부터 예금 먼저, 연금저축은 마지막에 한 사람 1,500만 원 아래(남 1,000·여 800)로 나눠 꺼냄
못 고치는 것: 퇴직금을 한 번에 받아 이미 낸 퇴직소득세(받은 날부터 60일이 지나면 IRP 로 되돌릴 수 없음) — 숫자에는 처음부터 퇴직소득세를 넣지 않았음."""
import io, contextlib
ns = {"__name__": "x"}
exec(open("sim4.py", encoding="utf-8").read(), ns)
run, plan_a, plan_b, NEED, fill_rest = ns["run"], ns["plan_a"], ns["plan_b"], ns["NEED"], ns["fill_rest"]

def make_fixed(fix_age):
    def plan(age, dep, pen, irp, n):
        if age <= fix_age:
            out = plan_a(age, dep, pen, irp, n)
            if age == fix_age:                       # 그해 말에 예금 명의를 반반으로 (다음 해 이자부터 반영)
                tot = dep["h"] + dep["w"] - out.get("dep_h", 0) - out.get("dep_w", 0)
                # out 은 run() 이 나중에 빼므로, 뺀 뒤 반반이 되게 미리 맞춤
                half = tot / 2
                dep["h"] = half + out.get("dep_h", 0); dep["w"] = half + out.get("dep_w", 0)
            return out
        out, need = {}, NEED
        hh = min(dep["h"], need / 2); ww = min(dep["w"], need - hh)
        hh = min(dep["h"], need - ww)
        for k, x in (("dep_h", hh), ("dep_w", ww)):
            if x > 0: out[k] = x; need -= x
        for k, cap in (("pen_h", 1000), ("pen_w", 800)):
            x = min(pen[k[-1]], cap, need)
            if x > 0: out[k] = x; need -= x
        for k in ("pen_h", "pen_w"):
            x = min(pen[k[-1]] - out.get(k, 0), 1500 - out.get(k, 0), need)
            if x > 0: out[k] = out.get(k, 0) + x; need -= x
        return fill_rest(out, need, dep, pen, irp)     # v3.4: 선 때문에 돈이 남았는데 끝나지 않게
    return plan

f = io.StringIO()
with contextlib.redirect_stdout(f):
    A = run("A", plan_a, {"h": 30000, "w": 10000}, {"h": 6000, "w": 4000}, 0)
    B = run("B", plan_b, {"h": 10000, "w": 10000}, {"h": 6000, "w": 4000}, 20000)
    res = {fa: run(f"A→{fa}", make_fixed(fa), {"h": 30000, "w": 10000}, {"h": 6000, "w": 4000}, 0) for fa in (65, 67, 70)}
def ym(end):
    y = int(end); m = round((end - y) * 12); return f"{y}세 {m}개월"
print(f"{'경우':28s} {'평생 세금':>8s}  {'B와 차이':>8s}  피부양자 넘는 해          버팀")
print(f"{'A 그대로 (끝까지)':28s} {A[0]:8.0f}  {A[0]-B[0]:8.0f}  {str(A[2]):24s} {ym(A[1])}")
for fa, r in res.items():
    print(f"{'A, ' + str(fa) + '세 말에 고침':28s} {r[0]:8.0f}  {r[0]-B[0]:8.0f}  {str(r[2]):24s} {ym(r[1])}")
print(f"{'B (처음부터 순서대로)':28s} {B[0]:8.0f}  {0:8.0f}  {str(B[2]):24s} {ym(B[1])}")
print("\n※ 피부양자 '넘는 해' = 그해 소득이 기준을 넘은 해. 건보료 판정은 다음 해 11월에 전년도 소득으로 하므로, 고친 뒤에도 1년쯤 더 고지서가 나온다.")
