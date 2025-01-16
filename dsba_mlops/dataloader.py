import pandas as pd

def load_data(file_path):
    # returning dataframe from csv
    return pd.read_csv(file_path)