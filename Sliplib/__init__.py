"""
Sliplib: Formula 1 Data Analytics and Race Intelligence Library
"""

__version__ = "0.1.0"
__author__ = "Mohan Das"

from .slipload import load_gp, enable_cache, show_data
from .selection import (
    select_drivers,
    pick_athletes,
    pick_fastest_group,
    pick_tyre_data,
    clean_result_Quali,
    clean_result_race,
    analyse_fastest,
    get_lap_stint,
    get_fresh_tyre_period,
    analyse_track_History,
    tel_fast_lap_summary,
    tel_get_for_all,
    time_cnc,
)
from .battle_finder import find_top_battles
from .dashboard import create_dashboard
from .Gotyres import stint_breakdown
from .GridSum import get_stint, calc_pos_gain, calc_position_gain
from .plotting import (
    plot_race_progression,
    plot_dist_speed,
    plot_dist_brake,
    plot_dist_throttle,
    plot_dist_ngear,
    plot_dist_rpms,
    plot_tyre_degradation,
)

__all__ = [
    # Loader
    "load_gp",
    "enable_cache",
    "show_data",
    # Selection
    "select_drivers",
    "pick_athletes",
    "pick_fastest_group",
    "pick_tyre_data",
    "clean_result_Quali",
    "clean_result_race",
    "analyse_fastest",
    "get_lap_stint",
    "get_fresh_tyre_period",
    "analyse_track_History",
    "tel_fast_lap_summary",
    "tel_get_for_all",
    "time_cnc",
    # Battles
    "find_top_battles",
    # Dashboard & Plotting
    "create_dashboard",
    "plot_race_progression",
    "plot_dist_speed",
    "plot_dist_brake",
    "plot_dist_throttle",
    "plot_dist_ngear",
    "plot_dist_rpms",
    "plot_tyre_degradation",
    # Strategy & Grid
    "stint_breakdown",
    "get_stint",
    "calc_pos_gain",
    "calc_position_gain",
]