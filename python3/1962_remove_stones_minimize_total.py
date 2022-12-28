import unittest
from math import floor

class Solution:

    def min_stone_sum(self, piles: list[int], k: int) -> int:
        for _ in range(k):
            max_index: int = piles.index(max(piles))
            piles[max_index] -= floor(piles[max_index] / 2)
        return sum(piles)

class TestSolution(unittest.TestCase):

    def test_1(self):
        piles: list[int] = [5,4,9]
        k: int = 2
        output: int = 12
        self.assertEqual(Solution().min_stone_sum(piles, k), output)

    def test_2(self):
        piles: list[int] = [4,3,6,7]
        k: int = 3
        output: int = 12
        self.assertEqual(Solution().min_stone_sum(piles, k), output)

if __name__ == "__main__":
    unittest.main()
