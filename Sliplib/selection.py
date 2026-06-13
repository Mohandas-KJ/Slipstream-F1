import fastf1

def pick_athletes(data,drivers):
    dr = []
    for i in drivers:
        td = data.pick_drivers(i)
        dr.append(td)
    return tuple(dr)