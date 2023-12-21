# tests/test_data_operations.py
import pandas as pd
import unittest
from music_analysis.data_operations import load_data, filter_by_year

class TestDataOperations(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.DataFrame({'released_year': [2010, 2011, 2012],
                                       'other_column': ['a', 'b', 'c']})

    def test_load_data(self):
        data = load_data('path/to/test_data.csv')
        self.assertIsInstance(data, pd.DataFrame)

    def test_filter_by_year(self):
        filtered_data = filter_by_year(self.test_data, 2011)
        self.assertEqual(len(filtered_data), 1)
