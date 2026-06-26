#Imports
import pandas as pd

# Get Stint for Strategy Analysis
def get_stint(data):
    stint = {}

    drivers = data["Driver"].unique()
    
    for i in drivers:
        tot_stint = data[data["Driver"] == i]["Stint"].max()
        stint[i] = int(tot_stint)
    
    #Returns a clean DataFrame with 'Driver' and 'Stint' columns
    #return data.groupby("Driver")["Stint"].max().reset_index()

    df = pd.DataFrame(stint.items(),columns=["Driver","Total Stint"])
    df["Pit Stops"] = df["Total Stint"] - 1

    return df.sort_values(by="Pit Stops",ascending=True).reset_index(drop=True)

# Calculate Position Gain
def calc_position_gain(data):

    pos = {}

    drivers = data["Driver"].unique()

    for i in drivers:
        gain_meter = 0
        pos_list = data[data["Driver"] == i]["Position"].dropna().tolist()

        c = pos_list[0]

        for p in pos_list[1:]:
            addi = c - p
            c = p
            gain_meter += addi
        
        pos[i] = int(gain_meter)

    df = pd.DataFrame(pos.items(),columns=["Driver","Position Gain"])

    return df.sort_values(by="Position Gain",ascending=False).reset_index(drop=True) 

import pandas as pd
import numpy as np

def calc_pos_gain(data):

    result = {
        "Driver": [],
        "PositionGain": [],
        "Status": []
    }

    drivers = data["Abbreviation"].unique()

    for d in drivers:

        row = data[data["Abbreviation"] == d].iloc[0]

        grid_pos = row["GridPosition"]
        classi_pos = row["ClassifiedPosition"]

        try:
            gain = int(grid_pos) - int(classi_pos)

            result["Driver"].append(d)
            result["PositionGain"].append(gain)
            result["Status"].append("Finished")

        except (ValueError, TypeError):

            result["Driver"].append(d)
            result["PositionGain"].append(np.nan)
            result["Status"].append(str(classi_pos))

    return (
        pd.DataFrame(result)
        .sort_values(
            by="PositionGain",
            ascending=False,
            na_position="last"
        )
        .reset_index(drop=True)
    )
