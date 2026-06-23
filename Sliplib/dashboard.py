import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Color scheme (F1-inspired dark theme) ──────────────────────────────────────
BG       = "#0f0f0f"
PANEL_BG = "#141414"
GRID     = "#2a2a2a"
TEXT     = "#e0e0e0"
ACCENT   = "#e10600"   # F1 red

C_SPEED    = "#00d2ff"   # cyan  – Speed
C_GEAR     = "#f5c518"   # gold  – Gear
C_THROTTLE = "#00e676"   # green – Throttle (on throttle)
C_BRAKE    = "#e10600"   # red   – Brake (on brake)
C_COAST    = "#ff9800"   # amber – coasting (throttle off, brake off)

def create_dashboard(data,name):

    # ── Load data ──────────────────────────────────────────────────────────────────
    df = data
    df["Brake"] = df["Brake"].astype(bool)

    dist     = df["Distance"]
    speed    = df["Speed"]
    gear     = df["nGear"]
    throttle = df["Throttle"]
    brake    = df["Brake"]

    # ── Figure setup ───────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(
    nrows=3, ncols=1,
    figsize=(16, 10),
    sharex=True,
    gridspec_kw={"hspace": 0.06, "height_ratios": [3, 2, 2]}
    )
    fig.patch.set_facecolor(BG)



    # ── Panel 1 — SPEED ────────────────────────────────────────────────────────────
    ax1 = axes[0]
    style_ax(ax1)

    # Shade braking zones as red background bands
    in_brake = False
    bstart   = None
    for i, (d, b) in enumerate(zip(dist, brake)):
        if b and not in_brake:
            bstart   = d
            in_brake = True
        elif not b and in_brake:
            ax1.axvspan(bstart, d, color=C_BRAKE, alpha=0.12, lw=0)
            in_brake = False
    if in_brake:
        ax1.axvspan(bstart, dist.iloc[-1], color=C_BRAKE, alpha=0.12, lw=0)

    ax1.plot(dist, speed, color=C_SPEED, linewidth=1.8, zorder=3)
    ax1.set_ylabel("Speed  (km/h)", fontsize=10, labelpad=8)
    ax1.set_ylim(60, speed.max() * 1.08)

    # Annotate peak speed
    peak_idx = speed.idxmax()
    ax1.annotate(
        f"  Peak {speed[peak_idx]:.0f} km/h",
        xy=(dist[peak_idx], speed[peak_idx]),
        color=C_SPEED, fontsize=8.5,
        xytext=(dist[peak_idx] + 80, speed[peak_idx] - 15),
        arrowprops=dict(arrowstyle="->", color=C_SPEED, lw=0.8)
    )

    # Annotate slowest point (corner apex)
    slow_idx = speed.idxmin()
    ax1.annotate(
        f"  Apex {speed[slow_idx]:.0f} km/h",
        xy=(dist[slow_idx], speed[slow_idx]),
        color=C_BRAKE, fontsize=8.5,
        xytext=(dist[slow_idx] + 100, speed[slow_idx] + 25),
        arrowprops=dict(arrowstyle="->", color=C_BRAKE, lw=0.8)
    )

    brake_patch = mpatches.Patch(color=C_BRAKE, alpha=0.35, label="Braking zone")
    speed_line  = mpatches.Patch(color=C_SPEED, label="Speed")
    ax1.legend(handles=[speed_line, brake_patch], loc="lower right",
            fontsize=8, facecolor="#1e1e1e", edgecolor=GRID, labelcolor=TEXT)

    # Title inside the top panel
    ax1.set_title(
        f"{name}  ·  LAP TELEMETRY  ·  F1",
        color=TEXT, fontsize=12, fontweight="bold", pad=10, loc="left"
    )

    # ── Panel 2 — GEAR ─────────────────────────────────────────────────────────────
    ax2 = axes[1]
    style_ax(ax2)

    # Step plot for gear (gears are discrete integers)
    ax2.step(dist, gear, where="post", color=C_GEAR, linewidth=1.8, zorder=3)
    ax2.fill_between(dist, gear, step="post", color=C_GEAR, alpha=0.15)

    # Mark every downshift
    gear_arr = gear.values
    dist_arr = dist.values
    for i in range(1, len(gear_arr)):
        if gear_arr[i] < gear_arr[i - 1]:
            ax2.annotate(
                f"↓{gear_arr[i]}",
                xy=(dist_arr[i], gear_arr[i]),
                fontsize=7, color=C_GEAR, alpha=0.85,
                xytext=(0, 6), textcoords="offset points", ha="center"
            )

    ax2.set_ylabel("Gear", fontsize=10, labelpad=8)
    ax2.set_yticks(range(int(gear.min()), int(gear.max()) + 1))
    ax2.set_ylim(gear.min() - 0.5, gear.max() + 0.8)

    gear_line = mpatches.Patch(color=C_GEAR, label="Gear selection")
    ax2.legend(handles=[gear_line], loc="lower right",
            fontsize=8, facecolor="#1e1e1e", edgecolor=GRID, labelcolor=TEXT)

    # ── Panel 3 — THROTTLE ─────────────────────────────────────────────────────────
    ax3 = axes[2]
    style_ax(ax3)

    # Color-fill throttle vs brake vs coast regions
    for i in range(len(dist) - 1):
        x0, x1 = dist.iloc[i], dist.iloc[i + 1]
        t, b    = throttle.iloc[i], brake.iloc[i]

        if b:
            color, alpha = C_BRAKE, 0.75        # braking
        elif t > 0:
            color, alpha = C_THROTTLE, 0.65     # on throttle
        else:
            color, alpha = C_COAST, 0.65        # coasting

        ax3.fill_between([x0, x1], [t, throttle.iloc[i + 1]], color=color, alpha=alpha)

    ax3.plot(dist, throttle, color="white", linewidth=0.8, alpha=0.5, zorder=3)

    # Brake overlay (scaled to throttle axis as 100%)
    brake_scaled = brake.astype(float) * 100
    ax3.fill_between(dist, brake_scaled, color=C_BRAKE, alpha=0.20)

    ax3.set_ylabel("Throttle  (%)", fontsize=10, labelpad=8)
    ax3.set_xlabel("Distance  (m)", fontsize=10, labelpad=8)
    ax3.tick_params(axis="x", colors=TEXT)
    ax3.set_ylim(-5, 115)

    thr_patch   = mpatches.Patch(color=C_THROTTLE, alpha=0.8, label="Throttle on")
    brake_patch2= mpatches.Patch(color=C_BRAKE,    alpha=0.8, label="Brake on")
    coast_patch = mpatches.Patch(color=C_COAST,    alpha=0.8, label="Coasting")
    ax3.legend(handles=[thr_patch, brake_patch2, coast_patch], loc="lower right",
               fontsize=8, facecolor="#1e1e1e", edgecolor=GRID, labelcolor=TEXT)

    # ── Shared x-axis label styling ────────────────────────────────────────────────
    ax3.tick_params(axis="x", colors=TEXT, labelsize=9)
    fig.text(0.5, 0.01, "← LAP PROGRESS →", ha="center", color="#555555", fontsize=8)

    plt.show()

def style_ax(ax):
    ax.set_facecolor(PANEL_BG)
    ax.tick_params(colors=TEXT, labelsize=9)
    ax.yaxis.label.set_color(TEXT)
    for spine in ax.spines.values():
        spine.set_edgecolor(GRID)
    ax.grid(axis="x", color=GRID, linewidth=0.5, linestyle="--")
    ax.grid(axis="y", color=GRID, linewidth=0.4, linestyle=":")