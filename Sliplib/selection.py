import fastf1
import pandas as pd

def time_cnc(time):
    t = pd.to_timedelta(time)

    mins = int(t.total_seconds() // 60)
    secs = t.total_seconds() % 60

    return f"{mins}:{secs:06.3f}"

def pick_athletes(data,drivers):
    dr = []
    for i in drivers:
        td = data.pick_drivers(i)
        dr.append(td)
    return tuple(dr)

# Function to pick Tyre Data
def pick_tyre_data(lap_data):

    tyre_columns = ["Driver","LapNumber","Compound","TyreLife","FreshTyre","Stint"]

    return lap_data[tyre_columns]

# Function to give Crisp Result
def clean_result(data):
    return data[["Abbreviation","TeamName","Position"]]

# Function to give Crisp Fastest
def analyse_fastest(fast_lap_data):

    df = pd.DataFrame({
        "Name": [
            "Driver",
            "LapNumber",
            "LapTime",
            "Stint",
            "Compound"
            
        ],
        "Value": [
            fast_lap_data["Driver"],
            fast_lap_data["LapNumber"],
            time_cnc(fast_lap_data["LapTime"]),
            fast_lap_data["Stint"],
            fast_lap_data["Compound"]
        ]
    })

    return df

# Function to Get Lap and Stint Data
def get_lap_stint(data):

    drivers = data["Driver"].unique()

    df = {"Driver": drivers,
          "TotalLaps": [],
          "TotalStint": []}

    for i in drivers:
        lap = int(data[data["Driver"] == i]["LapNumber"].max())
        stint = int(data[data["Driver"] == i]["Stint"].max())

        df["TotalLaps"].append(lap)
        df["TotalStint"].append(stint)
    
    return pd.DataFrame(df)
