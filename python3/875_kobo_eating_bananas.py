import unittest
import math

class Solution:

    def min_eating_speed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            middle = (left + right) // 2
            if sum(math.ceil(pile / middle) for pile in piles) > h:
                left = middle + 1
            else:
                right = middle
        return left

class TestSolution(unittest.TestCase):

    def test_1(self):
        piles = [3,6,7,11]
        h = 8
        output = 4
        self.assertEqual(Solution().min_eating_speed(piles, h), output)

    def test_2(self):
        piles = [30,11,23,4,20]
        h = 5
        output = 30
        self.assertEqual(Solution().min_eating_speed(piles, h), output)

    def test_3(self):
        piles = [30,11,23,4,20]
        h = 6
        output = 23 
        self.assertEqual(Solution().min_eating_speed(piles, h), output)

if __name__ == "__main__":
    unittest.main()
