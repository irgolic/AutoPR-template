import unittest
from typing import List
from solution import find_two_sum

class TestMediumChallenge(unittest.TestCase):

    def test_example_1(self):
        nums: List[int] = [2, 7, 11, 15]
        target: int = 9
        result = find_two_sum(nums, target)
        self.assertTrue((result == [0, 1]) or (result == [1, 0]))

    def test_example_2(self):
        nums: List[int] = [3, 2, 4]
        target: int = 6
        result = find_two_sum(nums, target)
        self.assertTrue((result == [1, 2]) or (result == [2, 1]))

    def test_example_3(self):
        nums: List[int] = [3, 3]
        target: int = 6
        result = find_two_sum(nums, target)
        self.assertTrue((result == [0, 1]) or (result == [1, 0]))

if __name__ == '__main__':
    unittest.main()