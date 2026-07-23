# This is used to process tyre Releated Data
# Imports
from IPython.display import display

# Display the Tyre Strategy!
def stint_breakdown(tyre_data):
    for name, tyre_df in tyre_data.items():
        print(f"--- {name} ---")
        display(tyre_df.groupby("Stint").agg({
            "LapNumber": ["min","max"],
            "Compound": "first",
            "FreshTyre": "first"
        }))