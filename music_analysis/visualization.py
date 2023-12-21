# music_analysis/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_stream_vs_rating(data):
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='Rating', y='streams', data=data, hue='in_spotify_playlists', palette='viridis', size='streams', sizes=(20, 200))
    plt.title('Scatter plot of streams vs rating')
    plt.xlabel('Rating')
    plt.ylabel('Streams')
    plt.legend(title='In Spotify Playlists')
    plt.show()
