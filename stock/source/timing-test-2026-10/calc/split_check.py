# 반론 검토 5회차 재현: 점수 항목을 시작 시기(2000~2008 · 2009~)로 나눠 정답 쪽이 이긴 몫. 실행: python3 -B stock/source/timing-test-2026-10/calc/split_check.py (calc.py 함수 그대로 · 네트워크 없음). ※ 연구·교육용
import sys; sys.path.insert(0,'stock/source/timing-test-2026-10/calc'); sys.path.insert(0,'tools')
import calc as C, numpy as np, logging
from datetime import timedelta
logging.getLogger("timing-test-calc").setLevel(logging.WARNING)
d,p=C.load('sp500tr'); idd,iv=C.load('irx'); c=C.cash_index(d,C.align_irx(d,idd,iv)); ms,mk=C.month_starts(d)
def sh(a,b): a,b=np.array(a),np.array(b); return f"{np.mean(a>b)*100:.1f}%({len(a)})" if len(a) else "-"
for lab,months,days in (("2y",24,730),("5y",60,1826)):
    W=C.windows(ms,mk,d,months); res={}
    for half,cond in (("2000-08",lambda s:d[s].year<=2008),("2009-",lambda s:d[s].year>=2009)):
        Wh=[w for w in W if cond(w[0])]
        # item1 q2b (start month s)
        now,wait=[],[]
        for s in ms:
            if d[s]<C.START_EVAL or not cond(s): continue
            seg=p[s+1:]; up=np.flatnonzero(seg>=1.1*p[s]); dn=np.flatnonzero(seg<=0.9*p[s])
            if not len(up) or (len(dn) and dn[0]<up[0]): continue
            t=s+1+up[0]; e=int(np.searchsorted(d,d[t]+timedelta(days=days)))
            if e>=len(d): continue
            hit=np.flatnonzero(p[t+1:e+1]<=0.9*p[s]); now.append(p[e]/p[t])
            wait.append(c[t+1+hit[0]]/c[t]*p[e]/p[t+1+hit[0]] if len(hit) else c[e]/c[t])
        i1=sh(now,wait)
        q3b=C.q3b_speed(p,c,Wh); q3s=C.q3s_stop_rebuy(d,p,c,Wh); q10=C.q10_wait_months(p,c,Wh,12); q6b=C.q6b_sell_in_may(d,p,c,Wh)
        print(lab,half,'item1',i1,'item2 lump>12',f"{q3b['lump_beats_dca12']*100:.1f}",'12>36',f"{q3b['dca12_beats_dca36']*100:.1f}",'item3',f"{q3s['hold_wins']*100:.1f}({q3s['triggered']})",'item4',f"{q10['now_wins']*100:.1f}",'item5',f"{q6b['monthly_wins']*100:.1f}")
