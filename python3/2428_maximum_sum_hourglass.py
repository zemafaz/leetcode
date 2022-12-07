import unittest

class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        max_sum = 0
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                max_sum = max(max_sum,
                        grid[i][j] + grid[i][j+1] + grid[i][j+2] +
                        grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1]
                        + grid[i+2][j+2])
        return max_sum

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
        output = 30
        self.assertEqual(Solution().maxSum(grid), output)

    def test_2(self):
        grid = [[1,2,3],[4,5,6],[7,8,9]]
        output = 35
        self.assertEqual(Solution().maxSum(grid), output)

if __name__ == "__main__":
    unittest.main()
