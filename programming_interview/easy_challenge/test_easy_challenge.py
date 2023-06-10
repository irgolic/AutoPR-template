import unittest
from typing import List
from solution import longest_increasing_subsequence


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_example(self):
        self.assertEqual(longest_increasing_subsequence([1, 3, 5, 4, 7]), 3)

    def test_empty_array(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)

    def test_increasing_array(self):
        self.assertEqual(longest_increasing_subsequence(list(range(1, 101))), 100)

    def test_decreasing_array(self):
        self.assertEqual(longest_increasing_subsequence(list(range(100, 0, -1))), 1)

    def test_alternating_array(self):
        self.assertEqual(longest_increasing_subsequence([1, 3, 5, 4, 7, 6, 9, 8]), 5)


if __name__ == "__main__":
    unittest.main()