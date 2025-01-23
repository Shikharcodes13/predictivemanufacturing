import pandas as pd

REQUIRED_COLUMNS = ["Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"]

def validate_data(file_path):
    data = pd.read_csv(file_path)
    if not all(col in data.columns for col in REQUIRED_COLUMNS):
        raise ValueError("Invalid data format. Missing required columns.")
    return data
