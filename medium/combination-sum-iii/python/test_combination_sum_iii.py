import unittest
from combination_sum_iii import Solution

class TestCombinationSumIII(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_3_7(self):
        result = self.s.combinationSum3(3, 7)
        self.assertEqual(result, [[1,2,4]])

    def test_3_9(self):
        result = self.s.combinationSum3(3, 9)
        self.assertEqual(result, [[1,2,6], [1,3,5], [2,3,4]])

    def tearDown(self):
        self.s = None
