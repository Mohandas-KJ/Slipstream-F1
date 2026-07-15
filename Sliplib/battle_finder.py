"""
battle_finder.py

Automated driver-pair selection for race comparison plots.

Replaces manual "pick 4-6 drivers by feel" with a blended score computed
from on-track battle intensity, overtakes, position-gain divergence,
teammate status, and strategy divergence.

Intended to slot into Sliplib as e.g. Sliplib/battles.py, consumed by
GridSum / selection the same way pick_athletes() and calc_pos_gain() are.

Expects a FastF1-style Laps DataFrame (session.laps) with at least:
    Driver, Team, LapNumber, Position, Time, Compound, Stint

Usage:
    from battle_finder import find_top_battles

    top = find_top_battles(R_Laps, n=6)
    top[["Driver1", "Driver2", "blended_score", "reason"]]
"""

from itertools import combinations
import numpy as np
import pandas as pd


DEFAULT_WEIGHTS = {
    "battle_closeness": 0.35,
    "overtakes": 0.25,
    "position_gain_divergence": 0.20,
    "strategy_divergence": 0.10,
    "teammate_bonus": 0.10,
}

GAP_THRESHOLD_SECONDS = 1.5


def _driver_position_series(laps: pd.DataFrame, driver: str) -> pd.Series:
    """Return a driver's Position indexed by LapNumber, NaN positions dropped."""
    d = laps[laps["Driver"] == driver].sort_values("LapNumber")
    return d.set_index("LapNumber")["Position"].dropna()


def _driver_time_series(laps: pd.DataFrame, driver: str) -> pd.Series:
    """Return a driver's session Time (timedelta since session start) indexed by LapNumber, NaT dropped."""
    d = laps[laps["Driver"] == driver].sort_values("LapNumber")
    return d.set_index("LapNumber")["Time"].dropna()


def _battle_closeness(laps: pd.DataFrame, d1: str, d2: str) -> float:
    """Fraction of shared laps where the gap between d1 and d2 stayed under threshold."""
    t1 = _driver_time_series(laps, d1)
    t2 = _driver_time_series(laps, d2)
    shared = t1.index.intersection(t2.index)
    if len(shared) == 0:
        return 0.0
    gap = (t1.loc[shared] - t2.loc[shared]).abs().dt.total_seconds()
    return float((gap < GAP_THRESHOLD_SECONDS).mean())


def _overtake_count(laps: pd.DataFrame, d1: str, d2: str) -> int:
    """Count sign changes in (pos1 - pos2) across shared laps -> number of position swaps."""
    p1 = _driver_position_series(laps, d1)
    p2 = _driver_position_series(laps, d2)
    shared = p1.index.intersection(p2.index)
    if len(shared) < 2:
        return 0
    diff = (p1.loc[shared] - p2.loc[shared]).to_numpy()
    signs = np.sign(diff)
    signs = signs[signs != 0]
    if len(signs) < 2:
        return 0
    return int(np.sum(signs[1:] != signs[:-1]))


def _position_gain(laps: pd.DataFrame, driver: str) -> int:
    """Start position minus end position (positive = gained places).

    Uses the first and last laps with a *valid* (non-NaN) Position, since
    pit-in/out laps, red-flag laps, or post-retirement laps can carry NaN.
    Returns 0 if the driver has no valid position on record at all.
    """
    pos = _driver_position_series(laps, driver)
    if pos.empty:
        return 0
    return int(pos.iloc[0] - pos.iloc[-1])


def _strategy_divergence(laps: pd.DataFrame, d1: str, d2: str) -> int:
    """1 if the two drivers ran a different number of stints or different compound sets."""
    s1 = laps[laps["Driver"] == d1]
    s2 = laps[laps["Driver"] == d2]
    stints_differ = s1["Stint"].dropna().nunique() != s2["Stint"].dropna().nunique()
    compounds1 = set(s1["Compound"].dropna().unique())
    compounds2 = set(s2["Compound"].dropna().unique())
    compounds_differ = compounds1 != compounds2
    return int(stints_differ or compounds_differ)


def _is_teammate(laps: pd.DataFrame, d1: str, d2: str) -> int:
    t1 = laps.loc[laps["Driver"] == d1, "Team"].dropna()
    t2 = laps.loc[laps["Driver"] == d2, "Team"].dropna()
    if t1.empty or t2.empty:
        return 0
    return int(t1.iloc[0] == t2.iloc[0])


def _normalize(series: pd.Series) -> pd.Series:
    lo, hi = series.min(), series.max()
    if hi - lo == 0:
        return pd.Series(0.0, index=series.index)
    return (series - lo) / (hi - lo)


def find_top_battles(
    laps: pd.DataFrame,
    n: int = 6,
    weights: dict = None,
    max_appearances_per_driver: int = 2,
    gap_threshold_seconds: float = GAP_THRESHOLD_SECONDS,
) -> pd.DataFrame:
    """
    Score every driver pair that shared track time and return the top n.

    Parameters
    ----------
    laps : pd.DataFrame
        session.laps (FastF1 Laps object works fine, it's a DataFrame subclass).
    n : int
        How many pairs to return.
    weights : dict
        Override any of DEFAULT_WEIGHTS. Missing keys fall back to defaults.
    max_appearances_per_driver : int
        Diversity cap - no single driver appears in more than this many
        of the returned top pairs. Set to None to disable.
    gap_threshold_seconds : float
        Gap under which two drivers are considered "in a battle" for a lap.

    Returns
    -------
    pd.DataFrame with columns:
        Driver1, Driver2, battle_closeness, overtakes,
        position_gain_divergence, strategy_divergence, is_teammate,
        blended_score, reason
    """
    global GAP_THRESHOLD_SECONDS
    GAP_THRESHOLD_SECONDS = gap_threshold_seconds

    w = {**DEFAULT_WEIGHTS, **(weights or {})}

    drivers = laps["Driver"].unique()
    rows = []

    for d1, d2 in combinations(drivers, 2):
        closeness = _battle_closeness(laps, d1, d2)
        overtakes = _overtake_count(laps, d1, d2)
        gain_div = abs(_position_gain(laps, d1) - _position_gain(laps, d2))
        strat_div = _strategy_divergence(laps, d1, d2)
        teammate = _is_teammate(laps, d1, d2)

        # skip pairs that never actually shared a lap (e.g. one retired lap 1
        # before the other even started, DNS, etc.)
        if closeness == 0 and overtakes == 0 and gain_div == 0:
            continue

        rows.append({
            "Driver1": d1,
            "Driver2": d2,
            "battle_closeness": closeness,
            "overtakes": overtakes,
            "position_gain_divergence": gain_div,
            "strategy_divergence": strat_div,
            "is_teammate": teammate,
        })

    if not rows:
        return pd.DataFrame(columns=[
            "Driver1", "Driver2", "battle_closeness", "overtakes",
            "position_gain_divergence", "strategy_divergence", "is_teammate",
            "blended_score", "reason"
        ])

    df = pd.DataFrame(rows)

    # normalize each raw signal to 0-1 across this race's pairs
    norm_closeness = _normalize(df["battle_closeness"])
    norm_overtakes = _normalize(df["overtakes"])
    norm_gain_div = _normalize(df["position_gain_divergence"])
    norm_strat = df["strategy_divergence"].astype(float)  # already 0/1
    norm_teammate = df["is_teammate"].astype(float)        # already 0/1

    df["blended_score"] = (
        w["battle_closeness"] * norm_closeness
        + w["overtakes"] * norm_overtakes
        + w["position_gain_divergence"] * norm_gain_div
        + w["strategy_divergence"] * norm_strat
        + w["teammate_bonus"] * norm_teammate
    )

    def _reason(row):
        parts = []
        if row["battle_closeness"] > 0.3:
            parts.append("sustained close gap")
        if row["overtakes"] >= 2:
            parts.append(f"{int(row['overtakes'])} position swaps")
        if row["is_teammate"]:
            parts.append("teammates")
        if row["strategy_divergence"]:
            parts.append("diverging strategy")
        if row["position_gain_divergence"] >= 5:
            parts.append("very different race trajectories")
        return ", ".join(parts) if parts else "moderate overall signal"

    df["reason"] = df.apply(_reason, axis=1)
    df = df.sort_values("blended_score", ascending=False).reset_index(drop=True)

    if max_appearances_per_driver is None:
        return df.head(n)

    # diversity filter: greedily take pairs, skipping ones that would push
    # a driver over the appearance cap
    appearances = {}
    selected = []
    for _, row in df.iterrows():
        d1, d2 = row["Driver1"], row["Driver2"]
        if (appearances.get(d1, 0) >= max_appearances_per_driver or
                appearances.get(d2, 0) >= max_appearances_per_driver):
            continue
        selected.append(row)
        appearances[d1] = appearances.get(d1, 0) + 1
        appearances[d2] = appearances.get(d2, 0) + 1
        if len(selected) == n:
            break

    return pd.DataFrame(selected).reset_index(drop=True)