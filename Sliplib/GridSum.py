#Imports
import pandas as pd

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
