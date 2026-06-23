import fastf1

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