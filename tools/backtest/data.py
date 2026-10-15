# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-15 — 자료 저장소 커밋 고정(재현) · 받은 CSV 는 저장소에 올리지 않음(S&P 지수 값 재배포 피함, meta 만) ·
#          FRED 일별 종가(sp500_daily — 월평균이 짧은 폭락을 작게 보이는지 확인용)
# (v1.0 — 2026-10-15 — 최초 (사용자 지시 2026-10-15 "주식 채널 컨셉은 ai로 코드 만들어서 가설을 백테스트해서 검증해보는거니까").
#          자료 받기·캐시·검사. 첫 자료: S&P500 월별 (GitHub datasets/s-and-p-500 — Shiller 월평균 가격·배당·10년 금리 1871~,
#          2023-07 뒤 가격은 FRED 일별 종가의 월평균). 클라우드에서 Yahoo·FRED 는 막혀 있어 GitHub raw 만 씀 (stock/guides/concept.md 4번).)
"""자료 받기·캐시·검사 (연구·교육용).

    from backtest import data
    df, meta = data.sp500_monthly()          # 캐시(stock/data/sp500_monthly.csv)가 있으면 그대로, 없으면 받음
    df, meta = data.sp500_monthly(refresh=True)

반환 DataFrame (index = 달 첫날, 오름차순):
    price      월평균 지수 (Shiller: 그 달 일별 종가 평균)
    dividend   12개월 배당 (지수 단위, 연율). 자료에 0 으로 비어 있는 끝부분은 NaN
    long_rate  10년 국채 금리 (%, 연율). 끝부분 0 은 NaN
meta: 출처 URL·받은 시각(UTC)·sha256·행 수·처음/끝 달·배당·금리가 있는 마지막 달(complete_until)·검사 결과
"""
import hashlib
import io
import json
import logging
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "stock" / "data"
LOG = logging.getLogger("backtest.data")

# 자료 저장소 커밋을 고정해 받는다 (같은 커밋 = 같은 자료 → 재현). 받은 CSV 는 저장소에 올리지 않는다 (.gitignore —
# S&P 지수 값의 재배포를 피함), 출처·sha256 만 *.meta.json 으로 남긴다. 새 자료가 필요하면 커밋을 바꾸고 refresh.
DATASET_COMMIT = "07b81e6af68239acd65b901a11844d6d95db6ead"   # datasets/s-and-p-500 2026-10-01 자동 갱신
_RAW = f"https://raw.githubusercontent.com/datasets/s-and-p-500/{DATASET_COMMIT}"
SOURCES = {
    "sp500_monthly": {
        "url": f"{_RAW}/data/data.csv",
        "file": "sp500_monthly.csv",
        "license": "datasets/s-and-p-500 는 ODC-PDDL-1.0 표기. 원자료: Robert Shiller · FRED(S&P Dow Jones Indices) — 저장소에 다시 올리지 않음",
        "about": "Robert Shiller 자료 (월평균 가격·12개월 배당·10년 금리) + 2023-07 뒤 가격은 FRED SP500 일별 종가의 월평균 "
                 "(github.com/datasets/s-and-p-500 scripts/update_from_fred.py)",
    },
    "sp500_daily_fred": {
        "url": f"{_RAW}/archive/fred_sp500.csv",
        "file": "sp500_daily_fred.csv",
        "license": "FRED SP500 (S&P Dow Jones Indices LLC 저작권) — 저장소에 다시 올리지 않음, 확인용으로만",
        "about": "FRED SP500 일별 종가 (최근 약 10년, 가격만 — 배당 없음). 월평균이 짧은 폭락을 작게 보이는지 확인용",
    },
}


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def _fetch(url, timeout=60, tries=3):
    """URL → bytes. 실패하면 단계·입력·다음에 할 일을 담아 RuntimeError (조용히 넘어가지 않음)."""
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ytb-backtest/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = e
            log("DATA", logging.WARNING, fetch_failed=url, attempt=i + 1, error=repr(e))
            time.sleep(2 ** i)
    raise RuntimeError(f"[DATA] 자료 받기 실패: {url} ({last!r}) → 네트워크 허용 목록(클라우드 환경 설정 Network access) 확인, "
                       f"또는 PC 에서 받은 파일을 {DATA_DIR} 에 두고 refresh=False 로 다시")


def validate_monthly(df, cols):
    """월별 자료 검사 → 결과 dict (문제는 WARNING 로그). 고치지 않고 알린다 (고치는 것은 부르는 쪽이 명시적으로)."""
    rep = {"rows": int(len(df)), "first": str(df.index.min().date()), "last": str(df.index.max().date())}
    rep["duplicates"] = int(df.index.duplicated().sum())
    steps = pd.Series(df.index).diff().dropna()
    rep["gaps"] = int((steps > pd.Timedelta(days=31)).sum())
    rep["not_month_start"] = int((df.index.day != 1).sum())
    for c in cols:
        s = df[c]
        rep[f"{c}_missing"] = int(s.isna().sum())
        rep[f"{c}_nonpositive"] = int((s <= 0).sum())
    for k, v in rep.items():
        if k not in ("rows", "first", "last") and v:
            log("VALIDATE", logging.WARNING, check=k, count=v)
    log("VALIDATE", **rep)
    return rep


def sp500_monthly(refresh=False, data_dir=None, fetch=_fetch):
    """S&P500 월별 자료 (캐시 우선). 끝부분의 0 배당·0 금리는 '없음'(NaN)으로 바꾸고 complete_until 에 적는다."""
    src = SOURCES["sp500_monthly"]
    d = Path(data_dir) if data_dir else DATA_DIR
    path, meta_path = d / src["file"], d / (src["file"] + ".meta.json")
    t0 = time.time()
    if path.is_file() and not refresh:
        raw = path.read_bytes()
        meta = json.loads(meta_path.read_text("utf-8")) if meta_path.is_file() else {}
        log("DATA", source="cache", path=path, bytes=len(raw), fetched_at=meta.get("fetched_at", "?"))
    else:
        raw = fetch(src["url"])
        d.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        meta = {"url": src["url"], "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "license": src["license"], "about": src["about"]}
        log("DATA", source="download", url=src["url"], bytes=len(raw))
    try:
        df = pd.read_csv(io.BytesIO(raw), parse_dates=["Date"])
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(f"[DATA] {path} 읽기 실패: {e!r} → refresh=True 로 다시 받기") from e
    need = {"Date", "SP500", "Dividend", "Long Interest Rate"}
    if not need <= set(df.columns):
        raise RuntimeError(f"[DATA] 열이 바뀜: {sorted(need - set(df.columns))} 없음 → 자료 저장소의 형식 확인")
    df = (df.rename(columns={"Date": "date", "SP500": "price", "Dividend": "dividend", "Long Interest Rate": "long_rate"})
            .set_index("date").sort_index()[["price", "dividend", "long_rate"]].astype(float))
    # 끝부분 0 = 아직 채워지지 않은 값 (2026-10-15 기준 배당 2023-06·금리 2023-09 까지) → NaN. 중간의 0 은 그대로 두고 검사에서 알림
    for c in ("dividend", "long_rate"):
        pos = df.index[df[c] > 0]
        if len(pos):
            tail = df.index > pos.max()
            df.loc[tail, c] = np.nan
    rep = validate_monthly(df, ["price", "dividend", "long_rate"])
    complete = df.dropna().index.max()
    meta.update({"sha256": hashlib.sha256(raw).hexdigest(), "rows": rep["rows"], "first": rep["first"], "last": rep["last"],
                 "dividend_until": str(df["dividend"].dropna().index.max().date()),
                 "long_rate_until": str(df["long_rate"].dropna().index.max().date()),
                 "complete_until": str(complete.date()), "validate": rep})
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), "utf-8")
    log("DATA", rows=rep["rows"], first=rep["first"], last=rep["last"], dividend_until=meta["dividend_until"],
        long_rate_until=meta["long_rate_until"], complete_until=meta["complete_until"], seconds=f"{time.time() - t0:.2f}")
    return df, meta


def sp500_daily(refresh=False, data_dir=None, fetch=_fetch):
    """FRED S&P500 일별 종가 (가격만). 빈 값('' · '.')은 휴장일 → 뺀다. → (Series close, meta)."""
    src = SOURCES["sp500_daily_fred"]
    d = Path(data_dir) if data_dir else DATA_DIR
    path, meta_path = d / src["file"], d / (src["file"] + ".meta.json")
    if path.is_file() and not refresh:
        raw = path.read_bytes()
        meta = json.loads(meta_path.read_text("utf-8")) if meta_path.is_file() else {}
        log("DATA", source="cache", path=path, bytes=len(raw), fetched_at=meta.get("fetched_at", "?"))
    else:
        raw = fetch(src["url"])
        d.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        meta = {"url": src["url"], "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "license": src["license"], "about": src["about"]}
        log("DATA", source="download", url=src["url"], bytes=len(raw))
    try:
        df = pd.read_csv(io.BytesIO(raw), na_values=[".", ""])
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(f"[DATA] {path} 읽기 실패: {e!r} → refresh=True 로 다시 받기") from e
    date_col = "observation_date" if "observation_date" in df.columns else "DATE"
    if date_col not in df.columns or "SP500" not in df.columns:
        raise RuntimeError("[DATA] FRED 열(observation_date/DATE, SP500)이 없음 → 자료 형식 확인")
    blanks = int(df["SP500"].isna().sum())
    s = (df.assign(date=pd.to_datetime(df[date_col])).dropna(subset=["SP500"]).set_index("date")["SP500"].astype(float).sort_index())
    dup = int(s.index.duplicated().sum())
    gaps = int((pd.Series(s.index).diff().dt.days > 5).sum())
    bad = int((s <= 0).sum())
    for k, v in (("duplicates", dup), ("gaps_over_5_days", gaps), ("nonpositive", bad)):
        if v:
            log("VALIDATE", logging.WARNING, data="sp500_daily", check=k, count=v)
    meta.update({"sha256": hashlib.sha256(raw).hexdigest(), "rows": int(len(s)), "blank_days_dropped": blanks,
                 "first": str(s.index.min().date()), "last": str(s.index.max().date()),
                 "validate": {"duplicates": dup, "gaps_over_5_days": gaps, "nonpositive": bad}})
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), "utf-8")
    log("VALIDATE", data="sp500_daily", rows=len(s), first=meta["first"], last=meta["last"], blank_days_dropped=blanks,
        duplicates=dup, gaps_over_5_days=gaps)
    return s, meta
