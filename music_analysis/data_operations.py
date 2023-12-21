# music_analysis/data_operations.py
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def filter_by_year(data, year):
    return data[data['released_year'] == year]