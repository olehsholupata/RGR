# music_analysis/music_operations.py

def get_artists_by_start_year(data, start_year):
    return data[data['released_year'] >= start_year]['artist(s)_name'].unique()
