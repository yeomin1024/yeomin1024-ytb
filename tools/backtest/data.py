# -*- coding: utf-8 -*-
# VERSION: v1.5 — 2026-10-16 — 주식 2·3·4번 자료 (사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐"):
#          yahoo_daily 가 주식 분할이 있는 심볼(QQQ·QLD·TQQQ·SCHD)도 받음 — Yahoo chart v8 의 close·배당은 이미 분할 반영(분할 날 앞뒤 종가가 이어짐을 2026-10-16 확인).
#          받을 때 분할 날 하루 변화가 분할 비율만큼 튀지 않는지 검사해 튀면 멈춤(분할 미반영 자료로 계산하지 않음), meta 에 splits 기록.
#          from_date 인자(기본 1993-01-01 — ^NDX 처럼 더 오래된 지수는 1985-10-01) · 오늘 장중 값은 until 로 뺌.
# (v1.4 — 2026-10-16 — Yahoo 일별 (사용자가 클라우드 Network access 에 Yahoo 를 허용 — 사용자 지시 2026-10-16 "허용했으니 기간 늘려"):
#          yahoo_daily(symbol) → 종가·배당(그날 배당락) → 총수익 지수(배당 재투자)를 우리가 직접 셈 (Yahoo adjclose 는 대조만).
#          SPY·^GSPC·^VIX·^IRX. 캐시 stock/data/yahoo_<심볼>_daily.csv(git 밖) + meta(sha256·받은 시각·검사). Yahoo 는 커밋 고정이 안 되므로
#          받은 날·sha256 을 남기고 FRED·datasets/finance-vix 와 겹치는 날을 대조한다.
# (v1.3 — 2026-10-16 — VIX 일별 종가 (공포지수 매수 규칙 — 사용자 지시 2026-10-16 "지금은 매수만 보는 거니까 매수에 관련된 것만 테스트해야지"):
#          GitHub datasets/finance-vix 커밋 3dbea23(2026-09-23) 고정 + 파일 sha256 고정 → vix_daily(). 다르면 멈춤 (조용히 다른 자료로 계산하지 않음).)
# (v1.2 — 2026-10-16 — 긴 일별 자료 (사용자 지시 2026-10-16 "흔히 사용하는 매수 전략을 10가지 정도 골라서 그냥 매수하고 관망하는거랑
#          비교 … 이걸 위한 티커, 테스트 기간을 적당하게 잡아보고"): 클라우드는 GitHub·pypi 만 열려 있어 pypi 휠에 든 자료를 버전·sha256 고정으로 받음 —
#          skfolio 1.9.0 S&P500 일별 종가 1990-01-02~2022-12-28, arch 8.0.0 S&P500·나스닥 종합 일별 1999~2018·Fama-French 월별 T-bill(RF) 1926~2018-11.
#          sp500_daily_long(): skfolio(FRED 첫날 전까지) + FRED(2016-02-12~, 공식 종가) 이어 붙임, 겹치는 기간 값이 같은지 검사(skfolio vs FRED 2016~2022 —
#          2일만 다름 → FRED 값, skfolio vs arch 1999~2018 — 같음).)
# (v1.1 — 2026-10-15 — 자료 저장소 커밋 고정(재현) · 받은 CSV 는 저장소에 올리지 않음(S&P 지수 값 재배포 피함, meta 만) ·
#          FRED 일별 종가(sp500_daily — 월평균이 짧은 폭락을 작게 보이는지 확인용))
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

v1.2 긴 일별 자료 (pypi 휠 안의 자료 — 휠 sha256·파일 sha256 고정):
    close, meta = data.sp500_daily_long()   # S&P500 일별 종가 1990-01-02~2026-02-11 (가격만)
    close, meta = data.nasdaq_daily()       # 나스닥 종합 일별 종가 1999-01-04~2018-12-31 (가격만)
    rf, meta = data.ff_rf_monthly()         # 1개월 T-bill 월 수익률 % (Fama-French RF) 1926-07~2018-11

v1.5 (분할 있는 ETF·오래된 지수):
    df, meta = data.yahoo_daily("TQQQ", until="2026-10-16")              # 분할 반영 종가 (검사함) · 2026-10-15 까지
    df, meta = data.yahoo_daily("^NDX", from_date="1985-10-01", until="2026-10-16")

v1.4 (Yahoo — 사용자가 허용):
    df, meta = data.yahoo_daily("SPY")      # 열: close(종가) · div(그날 배당락 배당) · tr(총수익 지수, 배당 재투자) · adjclose(Yahoo, 대조용)

v1.3:
    vix, meta = data.vix_daily()            # CBOE VIX 일별 종가 1990-01-02~2026-09-22 (datasets/finance-vix 커밋·sha256 고정)
"""
import gzip
import hashlib
import io
import json
import logging
import time
import zipfile
import urllib.error
import urllib.parse
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

# v1.3 VIX — datasets/finance-vix (ODC-PDDL-1.0, 원자료 CBOE). 커밋과 파일 sha256 을 고정한다.
VIX_COMMIT = "3dbea23c70cc2afbeeec8ac232c9ec72ac26ac21"       # datasets/finance-vix 2026-09-23 "Update data"
VIX_SOURCE = {
    "url": f"https://raw.githubusercontent.com/datasets/finance-vix/{VIX_COMMIT}/data/vix-daily.csv",
    "file": "vix_daily.csv",
    "sha256": "570e05630c9a5e7350d0c3dbe3acc58e793cb5248181ab0e949c121cc082fb83",
    "license": "datasets/finance-vix 는 ODC-PDDL-1.0 표기. 원자료: Cboe Global Markets (VIX®) — 저장소에 다시 올리지 않음",
    "about": "CBOE VIX 일별 시가·고가·저가·종가 1990-01-02~2026-09-22 (공포지수 — S&P 500 옵션의 30일 기대 변동성)",
}


# v1.2 pypi 휠 안의 자료 — 휠(버전·sha256)과 그 안 파일(sha256)을 고정. 캐시는 꺼낸 파일 그대로 (stock/data/*.csv.gz, .gitignore)
_SKF = "https://files.pythonhosted.org/packages/01/4b/77f24add7e04949b0e77cb235f4f9e3d2e196e1cf91864b3e35a0da6284e/skfolio-1.9.0-py3-none-any.whl"
_ARCH = ("https://files.pythonhosted.org/packages/d6/40/7b7ac152c35c32da2a00ba3523ea84c358478b12ee7b3b2b6892e5b9d81b/"
         "arch-8.0.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl")
_SKF_SHA = "b2b0d59800644d4949e8fb8222b95a4ab10305fbe82095bcfab6c0b8bfc68177"
_ARCH_SHA = "8c1f1d8abefab2f69f7fdbef08cc18c8377667d3b8d197a1f301d97f0e686cd2"
PYPI_SOURCES = {
    "sp500_daily_skfolio": {
        "wheel": _SKF, "wheel_sha256": _SKF_SHA, "member": "skfolio/datasets/data/sp500_index.csv.gz",
        "member_sha256": "894c34431c284f86aa64a467e176e2a3c9b697c857eb9ab35006c2dd55d3fdf2", "file": "sp500_daily_skfolio.csv.gz",
        "license": "skfolio 1.9.0 (BSD-3) 에 든 자료. S&P 500 지수 값은 S&P Dow Jones Indices 저작권 — 저장소에 다시 올리지 않음",
        "about": "S&P 500 지수 일별 종가 1990-01-02~2022-12-28 (가격만 — skfolio.datasets.load_sp500_index)",
    },
    "sp500_daily_arch": {
        "wheel": _ARCH, "wheel_sha256": _ARCH_SHA, "member": "arch/data/sp500/sp500.csv.gz",
        "member_sha256": "1e028cbb9c400cc018c816ccc439b33c919387e726c3ed5ca2c05c82746059de", "file": "sp500_daily_arch.csv.gz",
        "license": "arch 8.0.0 (NCSA) 에 든 자료. S&P 500 지수 값은 S&P Dow Jones Indices 저작권 — 저장소에 다시 올리지 않음",
        "about": "S&P 500 지수 일별 시가·고가·저가·종가 1999-01-04~2018-12-31 (arch.data.sp500) — skfolio 값 맞춰 보기용",
    },
    "nasdaq_daily_arch": {
        "wheel": _ARCH, "wheel_sha256": _ARCH_SHA, "member": "arch/data/nasdaq/nasdaq.csv.gz",
        "member_sha256": "b2009535343ebb14e0aa11ed086788d2997a416ffe4f9450eed9a561ae30ac59", "file": "nasdaq_daily_arch.csv.gz",
        "license": "arch 8.0.0 (NCSA) 에 든 자료. NASDAQ Composite 값은 Nasdaq 저작권 — 저장소에 다시 올리지 않음",
        "about": "나스닥 종합 지수 일별 종가 1999-01-04~2018-12-31 (arch.data.nasdaq, 가격만)",
    },
    "ff_factors_monthly_arch": {
        "wheel": _ARCH, "wheel_sha256": _ARCH_SHA, "member": "arch/data/frenchdata/frenchdata.csv.gz",
        "member_sha256": "f23436727b01d879e1372e3ee277514b0962a23d2b158f1aee6a402a90994f52", "file": "ff_factors_monthly_arch.csv.gz",
        "license": "arch 8.0.0 (NCSA) 에 든 Kenneth R. French Data Library 자료",
        "about": "Fama-French 3요인 월별 1926-07~2018-11 (Mkt-RF·SMB·HML·RF, % 월) — RF = 1개월 T-bill (현금 이자 확인용)",
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


# ----------------------------------------------------------------------------- v1.2 pypi 휠 안의 자료
def pypi_member(key, refresh=False, data_dir=None, fetch=_fetch):
    """PYPI_SOURCES[key] 의 파일 → (csv 바이트(압축 풂), meta). 캐시가 있으면 그대로 (파일 sha256 이 맞을 때만).
    휠 sha256 · 파일 sha256 이 고정값과 다르면 멈춘다 (다른 자료로 조용히 계산하지 않음)."""
    src = PYPI_SOURCES[key]
    d = Path(data_dir) if data_dir else DATA_DIR
    path, meta_path = d / src["file"], d / (src["file"] + ".meta.json")
    raw = path.read_bytes() if path.is_file() and not refresh else None
    if raw is not None and hashlib.sha256(raw).hexdigest() != src["member_sha256"]:
        log("DATA", logging.WARNING, key=key, cache="sha256 다름 → 다시 받음", path=path)
        raw = None
    if raw is None:
        wheel = fetch(src["wheel"], timeout=120)
        got = hashlib.sha256(wheel).hexdigest()
        if got != src["wheel_sha256"]:
            raise RuntimeError(f"[DATA] {key}: 휠 sha256 다름 ({got[:12]}… ≠ {src['wheel_sha256'][:12]}…) → PYPI_SOURCES 확인")
        with zipfile.ZipFile(io.BytesIO(wheel)) as z:
            raw = z.read(src["member"])
        if hashlib.sha256(raw).hexdigest() != src["member_sha256"]:
            raise RuntimeError(f"[DATA] {key}: 휠 안 파일 sha256 다름 → PYPI_SOURCES 확인")
        d.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        log("DATA", source="download", key=key, wheel=src["wheel"].rsplit("/", 1)[-1], member=src["member"], bytes=len(raw))
        meta = {"fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    else:
        meta = json.loads(meta_path.read_text("utf-8")) if meta_path.is_file() else {}
        log("DATA", source="cache", key=key, path=path, bytes=len(raw), fetched_at=meta.get("fetched_at", "?"))
    meta.update({"wheel": src["wheel"], "wheel_sha256": src["wheel_sha256"], "member": src["member"],
                 "sha256": src["member_sha256"], "license": src["license"], "about": src["about"]})
    return gzip.decompress(raw), meta, meta_path


def _validate_daily(s, name, big_move=0.12):
    """일별 종가 검사 → dict. 중복·0 이하·5일 넘는 빈 날(9·11 휴장 등 알려진 것도 그대로 알림)·하루 ±big_move 넘는 변화
    (기본 12% — 지수. VIX 는 하루 ±12% 가 흔해 100% 로 부른다, v1.3)."""
    dup = int(s.index.duplicated().sum())
    gaps = pd.Series(s.index).diff().dt.days
    gap_list = [str(s.index[i].date()) for i in np.where(gaps.to_numpy() > 5)[0]]
    r = s.pct_change()
    big = [f"{i.date()}:{v:+.1%}" for i, v in r[r.abs() > big_move].items()]
    rep = {"rows": int(len(s)), "first": str(s.index.min().date()), "last": str(s.index.max().date()), "duplicates": dup,
           "nonpositive": int((s <= 0).sum()), "missing": int(s.isna().sum()), "gaps_over_5_days": gap_list, "moves_over_12pct": big}
    for k in ("duplicates", "nonpositive", "missing"):
        if rep[k]:
            log("VALIDATE", logging.WARNING, data=name, check=k, count=rep[k])
    if gap_list or big:
        log("VALIDATE", logging.WARNING, data=name, gaps_over_5_days=",".join(gap_list) or "-", moves_over_12pct=",".join(big) or "-")
    log("VALIDATE", data=name, rows=rep["rows"], first=rep["first"], last=rep["last"], duplicates=dup)
    return rep


def _daily_close(raw, date_col, value_col, date_format=None):
    df = pd.read_csv(io.BytesIO(raw))
    if date_col not in df.columns or value_col not in df.columns:
        raise RuntimeError(f"[DATA] 열 {date_col}/{value_col} 이 없음 → 자료 형식 확인 (있는 열: {list(df.columns)[:8]})")
    idx = pd.to_datetime(df[date_col], format=date_format)
    return pd.Series(df[value_col].astype(float).to_numpy(), index=idx, name="close").sort_index()


def _overlap(a, b, name):
    """두 일별 종가의 겹치는 날 비교 → dict (같은 날 수, 한쪽에만 있는 날, 최대 상대 차이)."""
    common = a.index.intersection(b.index)
    rel = (a.loc[common] / b.loc[common] - 1).abs()
    rep = {"common_days": int(len(common)), "only_a": int(len(a.loc[common.min():common.max()].index.difference(common))),
           "only_b": int(len(b.loc[common.min():common.max()].index.difference(common))),
           "max_rel_diff": float(rel.max()), "days_over_0_01pct": int((rel > 1e-4).sum()),
           "from": str(common.min().date()), "to": str(common.max().date())}
    lvl = logging.WARNING if rep["max_rel_diff"] > 1e-3 else logging.INFO
    log("VALIDATE", lvl, overlap=name, **rep)
    return rep


def sp500_daily_long(refresh=False, data_dir=None, fetch=_fetch):
    """S&P500 일별 종가 1990-01-02~ (가격만): skfolio(FRED 첫날 전까지) + FRED(2016-02-12~, S&P 공식 종가).
    겹치는 기간 검사를 meta 에. 차이가 0.5% 를 넘는 날이 있거나 0.01% 넘게 다른 날이 5일을 넘으면 멈춘다 (다른 지수일 수 있음).
    2026-10-16 확인: skfolio~FRED 1,732일 중 2일만 다름 (2019-08-12 −0.04%, 2021-08-11 −0.12% — 앞뒤 날은 같음) → 겹치는 기간은 FRED."""
    raw, meta, meta_path = pypi_member("sp500_daily_skfolio", refresh, data_dir, fetch)
    skf = _daily_close(raw, "Date", "SP500")
    raw_a, meta_a, meta_path_a = pypi_member("sp500_daily_arch", refresh, data_dir, fetch)
    arc = _daily_close(raw_a, "Date", "Close", "%m/%d/%Y")
    fred, meta_f = sp500_daily(refresh, data_dir, fetch)
    ov_fred = _overlap(skf, fred, "skfolio~FRED")
    ov_arch = _overlap(skf, arc, "skfolio~arch")
    for ov in (ov_fred, ov_arch):
        if ov["max_rel_diff"] > 5e-3 or ov["days_over_0_01pct"] > 5:
            raise RuntimeError(f"[DATA] 겹치는 기간 값이 다름 {ov} → 자료 확인 (이어 붙이지 않음)")
    c = skf.index.intersection(fred.index)
    rel = skf.loc[c] / fred.loc[c] - 1
    fixed = {str(t.date()): {"skfolio": round(float(skf.loc[t]), 2), "fred": round(float(fred.loc[t]), 2)} for t in rel[rel.abs() > 1e-4].index}
    if fixed:
        log("VALIDATE", logging.WARNING, splice="겹치는 기간은 FRED(공식 종가) 값을 씀", days=",".join(fixed))
    tail = fred.loc[fred.index >= fred.index.min()]
    close = pd.concat([skf.loc[skf.index < tail.index.min()], tail])
    rep = _validate_daily(close, "sp500_daily_long")
    meta.update({"rows": rep["rows"], "first": rep["first"], "last": rep["last"], "validate": rep,
                 "splice": {"skfolio_until": str(skf.index[skf.index < tail.index.min()].max().date()), "fred_from": str(tail.index.min().date()),
                            "fred_rows": int(len(tail)), "fred_url": meta_f.get("url"), "fred_sha256": meta_f.get("sha256"),
                            "overlap_days_where_values_differ_fred_used": fixed},
                 "overlap_skfolio_fred": ov_fred, "overlap_skfolio_arch": ov_arch})
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), "utf-8")
    meta_a.update({"rows": int(len(arc)), "first": str(arc.index.min().date()), "last": str(arc.index.max().date())})
    meta_path_a.write_text(json.dumps(meta_a, ensure_ascii=False, indent=2), "utf-8")
    log("DATA", data="sp500_daily_long", rows=rep["rows"], first=rep["first"], last=rep["last"],
        splice=f"skfolio~{meta['splice']['skfolio_until']}+FRED{meta['splice']['fred_rows']}")
    return close, meta


def nasdaq_daily(refresh=False, data_dir=None, fetch=_fetch):
    """나스닥 종합 일별 종가 1999-01-04~2018-12-31 (가격만, arch.data.nasdaq)."""
    raw, meta, meta_path = pypi_member("nasdaq_daily_arch", refresh, data_dir, fetch)
    close = _daily_close(raw, "Date", "Close", "%m/%d/%Y")
    rep = _validate_daily(close, "nasdaq_daily")
    meta.update({"rows": rep["rows"], "first": rep["first"], "last": rep["last"], "validate": rep})
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), "utf-8")
    return close, meta


def ff_rf_monthly(refresh=False, data_dir=None, fetch=_fetch):
    """1개월 T-bill 월 수익률 (% / 월, Fama-French RF) → Series(index = 달 첫날)."""
    raw, meta, meta_path = pypi_member("ff_factors_monthly_arch", refresh, data_dir, fetch)
    df = pd.read_csv(io.BytesIO(raw))
    if not {"Date", "RF"} <= set(df.columns):
        raise RuntimeError("[DATA] Fama-French 열(Date, RF)이 없음 → 자료 형식 확인")
    idx = pd.to_datetime(df["Date"].astype(str), format="%Y%m")
    rf = pd.Series(df["RF"].astype(float).to_numpy(), index=idx, name="rf_pct_month").sort_index()
    rep = validate_monthly(rf.to_frame(), ["rf_pct_month"])
    meta.update({"rows": rep["rows"], "first": rep["first"], "last": rep["last"], "validate": rep})
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), "utf-8")
    return rf, meta


# ----------------------------------------------------------------------------- v1.3 VIX
def vix_daily(refresh=False, data_dir=None, fetch=_fetch):
    """CBOE VIX 일별 종가 → (Series, meta). 캐시가 있으면 그대로 (sha256 이 맞을 때만). sha256 이 고정값과 다르면 멈춘다."""
    src = VIX_SOURCE
    d = Path(data_dir) if data_dir else DATA_DIR
    path, meta_path = d / src["file"], d / (src["file"] + ".meta.json")
    raw = path.read_bytes() if path.is_file() and not refresh else None
    if raw is not None and hashlib.sha256(raw).hexdigest() != src["sha256"]:
        log("DATA", logging.WARNING, key="vix_daily", cache="sha256 다름 → 다시 받음", path=path)
        raw = None
    if raw is None:
        raw = fetch(src["url"])
        got = hashlib.sha256(raw).hexdigest()
        if got != src["sha256"]:
            raise RuntimeError(f"[DATA] vix_daily: sha256 다름 ({got[:12]}… ≠ {src['sha256'][:12]}…) → VIX_COMMIT·VIX_SOURCE 확인")
        d.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        meta = {"fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
        log("DATA", source="download", key="vix_daily", url=src["url"], bytes=len(raw))
    else:
        meta = json.loads(meta_path.read_text("utf-8")) if meta_path.is_file() else {}
        log("DATA", source="cache", key="vix_daily", path=path, bytes=len(raw), fetched_at=meta.get("fetched_at", "?"))
    s = _daily_close(raw, "DATE", "CLOSE")
    rep = _validate_daily(s, "vix_daily", big_move=1.0)
    meta.update({"url": src["url"], "commit": VIX_COMMIT, "sha256": src["sha256"], "license": src["license"], "about": src["about"],
                 "rows": rep["rows"], "first": rep["first"], "last": rep["last"], "validate": rep})
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), "utf-8")
    return s, meta


# ----------------------------------------------------------------------------- v1.4 Yahoo 일별
YAHOO_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{sym}?period1={p1}&period2={p2}&interval=1d&events=div%2Csplit"
YAHOO_FROM = "1993-01-01"                                         # SPY 상장 1993-01-29 — 지표(200일·52주·12개월) 준비 기간을 넉넉히


def _yahoo_fetch(url, timeout=60, tries=3):
    last = None
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research backtest; stock channel)"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except (urllib.error.URLError, TimeoutError, OSError) as e:  # noqa: PERF203
            last = e
            log("DATA", logging.WARNING, source="yahoo", url=url, try_=k + 1, error=repr(e)[:160])
            time.sleep(2 ** (k + 1))
    raise RuntimeError(f"[DATA] Yahoo 받기 실패: {url} ({last!r}) → 클라우드 Network access 에 query1.finance.yahoo.com·query2.finance.yahoo.com·"
                       f"fc.yahoo.com 이 있는지 확인, 없으면 refresh=False 로 캐시를 씀")


def yahoo_daily(symbol, refresh=False, data_dir=None, fetch=_yahoo_fetch, until=None, from_date=None):
    """Yahoo 일별 → (DataFrame[close, div, tr, adjclose], meta). 날짜 = 거래소(뉴욕) 날짜.
    tr: tr[t] = tr[t-1] × (close[t] + div[t]) / close[t-1] — 그날이 배당락일이면 그 배당을 다시 투자 (배당 재투자 총수익).
    캐시가 있으면 그대로 (refresh=True 로 다시 받음).
    v1.5 분할: Yahoo close·배당은 분할 반영 값 → 그대로 씀. 단, 분할 날 하루 변화가 '분할 비율로 나눈 값' 쪽에 더 가까우면(미반영) 멈춤.
    until: 이 날짜(UTC 0시) 앞까지만 (오늘 장중 값을 빼려면 오늘 날짜). from_date: 받기 시작 날짜 (기본 YAHOO_FROM)."""
    d = Path(data_dir) if data_dir else DATA_DIR
    key = symbol.replace("^", "").lower()
    path, meta_path = d / f"yahoo_{key}_daily.csv", d / f"yahoo_{key}_daily.csv.meta.json"
    if path.is_file() and not refresh:
        raw_csv = path.read_bytes()
        meta = json.loads(meta_path.read_text("utf-8")) if meta_path.is_file() else {}
        log("DATA", source="cache", key=f"yahoo_{key}", path=path, bytes=len(raw_csv), fetched_at=meta.get("fetched_at", "?"))
        df = pd.read_csv(io.BytesIO(raw_csv), parse_dates=["date"]).set_index("date")
    else:
        p1 = int(pd.Timestamp(from_date or YAHOO_FROM, tz="UTC").timestamp())
        p2 = int((pd.Timestamp(until, tz="UTC") if until else pd.Timestamp.now(tz="UTC")).timestamp())
        url = YAHOO_URL.format(sym=urllib.parse.quote(symbol), p1=p1, p2=p2)
        raw = fetch(url)
        try:
            res = json.loads(raw)["chart"]["result"][0]
        except Exception as e:  # noqa: BLE001
            raise RuntimeError(f"[DATA] Yahoo 응답 형식이 다름 ({symbol}): {raw[:200]!r} → 심볼·주소 확인") from e
        tz = res["meta"].get("exchangeTimezoneName", "America/New_York")
        idx = pd.to_datetime(res["timestamp"], unit="s", utc=True).tz_convert(tz).normalize().tz_localize(None)
        q = res["indicators"]["quote"][0]
        adj = (res["indicators"].get("adjclose") or [{}])[0].get("adjclose") or [None] * len(idx)
        df = pd.DataFrame({"close": q["close"], "adjclose": adj}, index=pd.DatetimeIndex(idx, name="date"), dtype=float)
        splits = []
        for v in ((res.get("events") or {}).get("splits") or {}).values():   # v1.5: close 가 분할 반영인지 분할 날마다 검사
            sd = pd.Timestamp(v["date"], unit="s", tz="UTC").tz_convert(tz).normalize().tz_localize(None)
            ratio = float(v["numerator"]) / float(v["denominator"])
            if sd in df.index and df.index.get_loc(sd) > 0:
                k = df.index.get_loc(sd)
                move = df["close"].iloc[k] / df["close"].iloc[k - 1]
                if abs(np.log(move * ratio)) < abs(np.log(move)):            # 1/ratio 쪽에 더 가까움 = 분할 미반영
                    raise RuntimeError(f"[DATA] {symbol} 분할 {sd.date()} {v['splitRatio']} 이 종가에 반영되지 않은 것 같음 (하루 변화 ×{move:.3f}) → 분할 처리 뒤 쓰기")
                splits.append({"date": str(sd.date()), "ratio": v["splitRatio"], "day_move": round(float(move), 4)})
            else:
                splits.append({"date": str(sd.date()), "ratio": v["splitRatio"], "day_move": None})
        if splits:
            log("DATA", symbol=symbol, splits=len(splits), adjusted="yes", days=",".join(f"{x['date']}:{x['ratio']}:x{x['day_move']}" for x in splits))
        divs = (res.get("events") or {}).get("dividends") or {}
        div = pd.Series(0.0, index=df.index)
        for v in divs.values():
            dd = pd.Timestamp(v["date"], unit="s", tz="UTC").tz_convert(tz).normalize().tz_localize(None)
            if dd not in div.index:
                raise RuntimeError(f"[DATA] {symbol} 배당락일 {dd.date()} 이 거래일에 없음 → 자료 확인")
            div.loc[dd] += float(v["amount"])
        df["div"] = div
        nulls = int(df["close"].isna().sum())
        df = df.dropna(subset=["close"])
        df = df[~df.index.duplicated(keep="last")].sort_index()
        d.mkdir(parents=True, exist_ok=True)
        raw_csv = df[["close", "div", "adjclose"]].to_csv(float_format="%.6f").encode()
        path.write_bytes(raw_csv)
        meta = {"url": url, "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "symbol": symbol, "exchange_tz": tz,
                "null_closes_dropped": nulls, "dividends": int(len(divs)), "splits": splits, "from": from_date or YAHOO_FROM, "until": str(until) if until else None,
                "license": "Yahoo Finance 자료 — 저장소에 다시 올리지 않음 (연구용 계산만, meta 만 올림)",
                "about": f"{symbol} 일별 종가·배당 (Yahoo chart API v8). tr = 배당 재투자 총수익 지수 (우리 계산)"}
        log("DATA", source="download", key=f"yahoo_{key}", url=url, rows=len(df), dividends=len(divs), null_closes_dropped=nulls)
    close = df["close"].astype(float)
    tr = (close + df["div"]).div(close.shift(1)).fillna(1.0).cumprod()
    df["tr"] = tr
    rep = _validate_daily(close, f"yahoo_{key}", big_move=1.0 if key in ("vix", "irx") else (0.40 if key in ("qld", "tqqq") else 0.12))
    adj_note = "-"
    if df["adjclose"].notna().all() and df["div"].sum() > 0:                 # Yahoo adjclose 와 하루 수익률 대조 (배당 방식이 조금 다름)
        a = df["adjclose"].pct_change().dropna()
        b = tr.pct_change().dropna()
        diff = (a - b).abs()
        adj_note = {"max_daily_diff": float(diff.max()), "days_over_0_01pct": int((diff > 1e-4).sum()),
                    "tr_vs_adj_growth_ratio": float((tr.iloc[-1] / tr.iloc[0]) / (df["adjclose"].iloc[-1] / df["adjclose"].iloc[0]))}
        lvl = logging.WARNING if adj_note["max_daily_diff"] > 2e-3 else logging.INFO
        log("VALIDATE", lvl, data=f"yahoo_{key}", vs="yahoo_adjclose", **adj_note)
    meta.update({"sha256": hashlib.sha256(raw_csv).hexdigest(), "rows": rep["rows"], "first": rep["first"], "last": rep["last"],
                 "validate": rep, "tr_vs_yahoo_adjclose": adj_note, "div_sum": float(df["div"].sum())})
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), "utf-8")
    return df, meta

