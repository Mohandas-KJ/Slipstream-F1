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

def select_drivers(data,drivers):
    f_dr = {}

    for d in drivers:
        f_dr[d] = data.pick_drivers(d)

    print(f_dr.keys())
    return f_dr

def pick_fastest_group(drivers_data):

    return {
        code: df.pick_fastest()
        for code,df in drivers_data.items()
    }

# Function to pick Tyre Data
def pick_tyre_data(lap_data):

    tyre_columns = ["Driver","LapNumber","Compound","TyreLife","FreshTyre","Stint"]

    return {
        driver: df[tyre_columns]
        for driver,df in lap_data.items()
    }

# Function to give Crisp Result
def clean_result_Quali(data):
    return data[["Abbreviation","TeamName","Position"]]

def clean_result_race(data):
    return data[["Abbreviation","TeamName","ClassifiedPosition"]]

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

# Function to get Fresh Tyre Period
def get_fresh_tyre_period(data):

    drivers = data["Driver"].unique()

    df = {"Driver": [],
          "TyrePeriod": []}
    
    for d in drivers:
        period = int(data[data["Driver"] == d]["FreshTyre"].sum())
        df["Driver"].append(d)
        df["TyrePeriod"].append(period)
    
    return pd.DataFrame(df).sort_values(by="TyrePeriod",ascending=False)

# Analyse Track History
def analyse_track_History(data):

    df = {"Flags": [],
          "Occurence": []}

    flags = data["Flag"].unique()

    for f in flags:
        df["Flags"].append(f)
        df["Occurence"].append(len(data[data["Flag"] == f]))
    
    return pd.DataFrame(df)


# =====================================================================
#                      TELEMETRY ANALYSIS
# =====================================================================

def tel_fast_lap_summary(drivers_fast):

    df = {"Driver": [],
          "LapTime": [],
          "Compound": [],
          "TyreLife": []}
    
    for d in drivers_fast:
        df["Driver"].append(d["Driver"])
        df["LapTime"].append(time_cnc(d["LapTime"]))
        df["Compound"].append(d["Compound"])
        df["TyreLife"].append(d["TyreLife"])

    return pd.DataFrame(df)   

def tel_get_for_all(drivers_fast):

    return {
        code: df.get_car_data().add_distance()
        for code,df in drivers_fast.items()
    }
