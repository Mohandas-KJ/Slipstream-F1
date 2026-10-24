import os
from pathlib import Path
import fastf1
import pandas as pd

# Default cache directory resolved relative to project root (Slipstream-F1/cache)
DEFAULT_CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"

def enable_cache(cache_dir=None):
    """Enable FastF1 disk cache at the specified or default cache directory."""
    target_cache = Path(cache_dir) if cache_dir else DEFAULT_CACHE_DIR
    target_cache.mkdir(parents=True, exist_ok=True)
    fastf1.Cache.enable_cache(str(target_cache))

# Function to load Session
def load_gp(year, name, category, cache_dir=None):
    """Enable cache and retrieve a FastF1 session object."""
    enable_cache(cache_dir)
    session = fastf1.get_session(
        year,
        name,
        category
    )
    return session

# Function to show
def show_data(session):
    if hasattr(session, "results") and session.results is not None:
        return session.results.head()
    return session