import unittest
from typing import List
from solution import max_sum_non_adjacent

class TestMaxSumNonAdjacent(unittest.TestCase):

    def test_example_cases(self):
        self.assertEqual(max_sum_non_adjacent([1, 2, 3, 4, 5, 6, 7]), 16)
        self.assertEqual(max_sum_non_adjacent([3, 2, 7, 10]), 13)
        self.assertEqual(max_sum_non_adjacent([3, 2, 5, 10, 7]), 15)

    def test_edge_cases(self):
        self.assertEqual(max_sum_non_adjacent([1]), 1)
        self.assertEqual(max_sum_non_adjacent([1, 1, 1, 1, 1]), 3)

if __name__ == '__main__':
    unittest.main()