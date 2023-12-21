# tests/test_visualization.py
import pandas as pd
import unittest
from music_analysis.visualization import plot_stream_vs_rating

class TestVisualization(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.DataFrame({'Rating': [3, 4, 5],
                                       'streams': [100, 200, 300],
                                       'in_spotify_playlists': [True, False, True]})

    def test_plot_stream_vs_rating(self):
        # Add your testing logic for the plot function
        pass
