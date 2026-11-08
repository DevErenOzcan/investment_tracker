"""Swing-horizon technical factors and a cross-sectional score. Fully deterministic."""
from __future__ import annotations

import numpy as np
import pandas as pd

# Score weights (swing: a few days to a few weeks)
WEIGHTS = {
    "z_mom": 0.30,        # blend of 1- and 3-month returns
    "z_rs": 0.20,         # 3-month relative strength vs the benchmark
    "z_trend": 0.15,      # moving-average alignment
    "z_high": 0.15,       # proximity to the 52-week high (breakout candidates)
    "z_volume": 0.10,     # volume surge
    "z_ext": -0.10,       # over-extension penalty
}


def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    d = close.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    rs = up / dn.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    pc = df["close"].shift()
    tr = pd.concat([df["high"] - df["low"], (df["high"] - pc).abs(), (df["low"] - pc).abs()],
                   axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def per_symbol(g: pd.DataFrame, bench_ret63: float | None, atr_n: int = 14) -> dict | None:
    g = g.sort_values("date")
    if len(g) < 130:
        return None
    c, v = g["close"], g["volume"]
    last = float(c.iloc[-1])
    sma20, sma50 = c.rolling(20).mean().iloc[-1], c.rolling(50).mean().iloc[-1]
    sma200 = c.rolling(200).mean().iloc[-1] if len(g) >= 200 else np.nan
    a = float(atr(g, atr_n).iloc[-1])
    ret = lambda n: float(last / c.iloc[-n - 1] - 1) if len(c) > n else np.nan  # noqa: E731
    r63 = ret(63)
    high252 = float(g["high"].tail(252).max())
    dv20 = float((c * v).tail(20).mean())
    trend = int(last > sma20) + int(last > sma50) + int(sma20 > sma50) + \
        int(not np.isnan(sma200) and sma50 > sma200)
    return {
        "symbol": g["symbol"].iloc[0],
        "date": g["date"].iloc[-1].date().isoformat(),
        "close": round(last, 4),
        "ret_5": ret(5), "ret_21": ret(21), "ret_63": r63, "ret_126": ret(126),
        "rs_63": (r63 - bench_ret63) if bench_ret63 is not None and not np.isnan(r63) else np.nan,
        "sma20": float(sma20), "sma50": float(sma50), "sma200": float(sma200),
        "trend": trend,
        "atr": a, "atr_pct": a / last,
        "rsi14": float(rsi(c).iloc[-1]),
        "dist_high": last / high252 - 1,
        "vol_ratio": float(v.tail(5).mean() / max(v.tail(50).mean(), 1)),
        "ext_20": last / float(sma20) - 1,
        "vol_20": float(c.pct_change().tail(20).std() * np.sqrt(252)),
        "dollar_volume_20": dv20,
        "low_20": float(g["low"].tail(20).min()),
        "high_20": float(g["high"].tail(20).max()),
    }


def compute(ohlcv: pd.DataFrame, benchmark: str = "QQQ") -> pd.DataFrame:
    bench = ohlcv[ohlcv["symbol"] == benchmark].sort_values("date")
    b63 = float(bench["close"].iloc[-1] / bench["close"].iloc[-64] - 1) if len(bench) > 64 else None
    rows = [r for _, g in ohlcv.groupby("symbol") if (r := per_symbol(g, b63)) is not None]
    return pd.DataFrame(rows)


def _z(s: pd.Series) -> pd.Series:
    s = s.astype(float)
    lo, hi = s.quantile(0.02), s.quantile(0.98)
    s = s.clip(lo, hi)
    sd = s.std()
    return (s - s.mean()) / sd if sd and not np.isnan(sd) else s * 0


def score(f: pd.DataFrame) -> pd.DataFrame:
    f = f.copy()
    f["z_mom"] = _z(0.5 * f["ret_21"].fillna(0) + 0.5 * f["ret_63"].fillna(0))
    f["z_rs"] = _z(f["rs_63"].fillna(0))
    f["z_trend"] = _z(f["trend"])
    f["z_high"] = _z(f["dist_high"])
    f["z_volume"] = _z(np.log(f["vol_ratio"].clip(lower=0.1)))
    # over-extension: 15%+ above the 20-day average or RSI > 80
    ext = (f["ext_20"] - 0.15).clip(lower=0) * 10 + ((f["rsi14"] - 80).clip(lower=0) / 10)
    f["z_ext"] = _z(ext)
    f["score"] = sum(w * f[k] for k, w in WEIGHTS.items())
    # push down very volatile names (daily ATR > 8%)
    f.loc[f["atr_pct"] > 0.08, "score"] -= 1.0
    return f.sort_values("score", ascending=False).reset_index(drop=True)


def correlation(ohlcv: pd.DataFrame, symbols: list[str], lookback: int = 60) -> pd.DataFrame:
    px = ohlcv[ohlcv["symbol"].isin(symbols)].pivot(index="date", columns="symbol", values="close")
    return px.pct_change().tail(lookback).corr()


def covariance(ohlcv: pd.DataFrame, symbols: list[str], lookback: int = 60) -> pd.DataFrame:
    px = ohlcv[ohlcv["symbol"].isin(symbols)].pivot(index="date", columns="symbol", values="close")
    return px.pct_change().tail(lookback).cov() * 252
