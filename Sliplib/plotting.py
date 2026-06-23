import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Plot Driver Position given the laps
def plot_race_progression(drivers):
    plt.figure(figsize=(8,6))
    for dr in drivers:
        x = dr["LapNumber"]
        y = dr["Position"]

        plt.plot(x,y,label=dr["Driver"].iloc[0])
    plt.gca().invert_yaxis()
    plt.xlabel("Laps")
    plt.ylabel("Position")
    plt.title(f"Race Progression of {len(drivers)} drivers")
    plt.legend()
    plt.show()

# Plot Speed of drivers given the distance for a single lap (fastest lap)
def plot_dist_speed(drivers,names):
    plt.figure(figsize=(8,6))
    for i,dr in enumerate(drivers):
        x = dr["Distance"]
        y = dr["Speed"]

        plt.plot(x,y,label=names[i])
    plt.xlabel("Distance")
    plt.ylabel("Speed")
    plt.title(f"Distance vs Speed of {len(drivers)} Drivers")
    plt.legend()
    plt.show()

# Plot Brake Application of drivers given the distance for a single lap (fastest lap)
def plot_dist_brake(drivers,names):
    plt.figure(figsize=(8,6))
    for i,dr in enumerate(drivers):
        x = dr["Distance"]
        y = dr["Brake"] * 100

        plt.plot(x,y,label=names[i])
    plt.xlabel("Distance")
    plt.ylabel("Brake")
    plt.title(f"Distance vs Brake of {len(drivers)} Drivers")
    plt.legend()
    plt.show()

# Plot Throttle of drivers given the distance for a single lap (fastest lap)
def plot_dist_throttle(drivers,names):
    plt.figure(figsize=(8,6))
    for i,dr in enumerate(drivers):
        x = dr["Distance"]
        y = dr["Throttle"]

        plt.plot(x,y,label=names[i])
    plt.xlabel("Distance")
    plt.ylabel("Throttle")
    plt.title(f"Distance vs Throttle of {len(drivers)} Drivers")
    plt.legend()
    plt.show()

# Plot nGears of drivers given the distance for a single lap (fastest lap)
def plot_dist_ngear(drivers,names):
    plt.figure(figsize=(8,6))
    for i,dr in enumerate(drivers):
        x = dr["Distance"]
        y = dr["nGear"]

        plt.plot(x,y,label=names[i])
    plt.xlabel("Distance")
    plt.ylabel("nGear")
    plt.title(f"Distance vs nGear of {len(drivers)} Drivers")
    plt.legend()
    plt.show()

# Plot RPM of drivers given the distance for a single lap (fastest lap)
# Can Measure Engine Powers
def plot_dist_rpms(drivers,names):
    plt.figure(figsize=(8,6))
    for i,dr in enumerate(drivers):
        x = dr["Distance"]
        y = dr["RPM"]

        plt.plot(x,y,label=names[i])
    plt.xlabel("Distance")
    plt.ylabel("RPM")
    plt.title(f"Distance vs RPM of {len(drivers)} Drivers")
    plt.legend()
    plt.show()