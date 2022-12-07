import unittest

class Solution:
    def min_cost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        dp, dp2 = {(0,0): 0}, {}
        for i, a in enumerate(houses):
            for cj in (range(1, n+1) if a == 0 else [a]):
                for ci, b in dp:
                    b2 = b + (ci != cj)
                    if b2 > target: continue
                    dp2[cj, b2] = min(dp2.get((cj, b2), float('inf')), dp[ci, b] + (cost[i][cj - 1] if cj != a else 0))
            dp, dp2 = dp2, {}
        return min([dp[c, b] for c, b in dp if b == target] or [-1])

class TestSolution(unittest.TestCase):
    def test_1(self):
        houses = [0,0,0,0,0]
        cost = [[1,10], [10,1], [10,1], [1,10], [5,1]]
        m = 5
        n = 2
        target = 3
        self.assertEqual(Solution().min_cost(houses, cost, m, n, target), 9)

    def test_2(self):
        houses = [0,2,1,2,0]
        cost = [[1,10], [10,1], [10,1], [1,10], [5,1]]
        m = 5
        n = 2
        target = 3
        self.assertEqual(Solution().min_cost(houses, cost, m, n, target), 11)
    
    def test_3(self):
        houses = [3,1,2,3]
        cost = [[1,1,1], [1,1,1], [1,1,1], [1,1,1]]
        m = 4
        n = 2
        target = 3
        self.assertEqual(Solution().min_cost(houses, cost, m, n, target), -1)

if __name__ == '__main__':
    unittest.main()