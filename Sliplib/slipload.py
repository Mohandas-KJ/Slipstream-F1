#Library File
import fastf1
import pandas as pd

def enable_cache():
    fastf1.Cache.enable_cache("../../cache")

# Function to load Session
def load_gp(year,name,category):
    enable_cache()
    session = fastf1.get_session(
        year,
        name,
        category
    )

    return session

#Fuction to show
def show_data(session):
    session.head()