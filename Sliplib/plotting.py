from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def _finalize_plot(save_path=None, show=True, dpi=150):
    """Internal helper to optionally save figure to file and display it."""
    if save_path:
        p = Path(save_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(str(p), bbox_inches="tight", dpi=dpi)
        print(f"Plot saved to: {save_path}")
    if show:
        plt.show()
    else:
        plt.close()

# Plot Driver Position given the laps
def plot_race_progression(drivers, save_path=None, show=True):
    plt.figure(figsize=(10, 6))
    for dr in drivers:
        x = dr["LapNumber"]
        y = dr["Position"]
        plt.plot(x, y, label=dr["Driver"].iloc[0])
    plt.gca().invert_yaxis()
    plt.xlabel("Laps")
    plt.ylabel("Position")
    plt.title(f"Race Progression of {len(drivers)} drivers")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    _finalize_plot(save_path, show)

# Plot Speed of drivers given the distance for a single lap (fastest lap)
def plot_dist_speed(drivers, names, save_path=None, show=True):
    plt.figure(figsize=(10, 5))
    for i, dr in enumerate(drivers):
        x = dr["Distance"]
        y = dr["Speed"]
        plt.plot(x, y, label=names[i])
    plt.xlabel("Distance (m)")
    plt.ylabel("Speed (km/h)")
    plt.title(f"Distance vs Speed of {len(drivers)} Drivers")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    _finalize_plot(save_path, show)

# Plot Brake Application of drivers given the distance for a single lap (fastest lap)
def plot_dist_brake(drivers, names, save_path=None, show=True):
    plt.figure(figsize=(10, 4))
    for i, dr in enumerate(drivers):
        x = dr["Distance"]
        y = dr["Brake"] * 100
        plt.plot(x, y, label=names[i])
    plt.xlabel("Distance (m)")
    plt.ylabel("Brake (%)")
    plt.title(f"Distance vs Brake of {len(drivers)} Drivers")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    _finalize_plot(save_path, show)

# Plot Throttle of drivers given the distance for a single lap (fastest lap)
def plot_dist_throttle(drivers, names, save_path=None, show=True):
    plt.figure(figsize=(10, 4))
    for i, dr in enumerate(drivers):
        x = dr["Distance"]
        y = dr["Throttle"]
        plt.plot(x, y, label=names[i])
    plt.xlabel("Distance (m)")
    plt.ylabel("Throttle (%)")
    plt.title(f"Distance vs Throttle of {len(drivers)} Drivers")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    _finalize_plot(save_path, show)

# Plot nGears of drivers given the distance for a single lap (fastest lap)
def plot_dist_ngear(drivers, names, save_path=None, show=True):
    plt.figure(figsize=(10, 4))
    for i, dr in enumerate(drivers):
        x = dr["Distance"]
        y = dr["nGear"]
        plt.plot(x, y, label=names[i])
    plt.xlabel("Distance (m)")
    plt.ylabel("nGear")
    plt.title(f"Distance vs nGear of {len(drivers)} Drivers")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    _finalize_plot(save_path, show)

# Plot RPM of drivers given the distance for a single lap (fastest lap)
def plot_dist_rpms(drivers, names, save_path=None, show=True):
    plt.figure(figsize=(10, 4))
    for i, dr in enumerate(drivers):
        x = dr["Distance"]
        y = dr["RPM"]
        plt.plot(x, y, label=names[i])
    plt.xlabel("Distance (m)")
    plt.ylabel("RPM")
    plt.title(f"Distance vs RPM of {len(drivers)} Drivers")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    _finalize_plot(save_path, show)

# Plot Tyre Degradation
def plot_tyre_degradation(drivers_data, pair, save_path=None, show=True):
    """
    Plot tyre degradation for two drivers.

    Parameters
    ----------
    drivers_data : dict
        Dictionary returned by select_drivers()
    pair : tuple
        Example: ("HUL", "OCO")
    save_path : str, optional
        File path to save the generated plot.
    show : bool, optional
        Whether to call plt.show() (default True).
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    for driver in pair:
        clean = drivers_data[driver].pick_quicklaps()
        ax.scatter(
            clean["TyreLife"],
            clean["LapTime"].dt.total_seconds(),
            label=driver
        )

    ax.set_xlabel("Tyre Life (Laps)")
    ax.set_ylabel("Lap Time (s)")
    ax.set_title(f"Tyre Degradation: {pair[0]} vs {pair[1]}")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend()
    plt.tight_layout()
    _finalize_plot(save_path, show)