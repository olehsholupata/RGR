# tests/test_music_operations.py
import pandas as pd
import unittest
from music_analysis.music_operations import get_artists_by_start_year

class TestMusicOperations(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.DataFrame({'released_year': [2010, 2011, 2012],
                                       'artist(s)_name': ['Artist1', 'Artist2', 'Artist3']})

    def test_get_artists_by_start_year(self):
        artists = get_artists_by_start_year(self.test_data, 2011)
        self.assertEqual(len(artists), 2)
