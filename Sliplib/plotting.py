import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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