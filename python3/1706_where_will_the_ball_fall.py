import unittest

class Solution:

    def find_ball(self, grid: list[list[int]]) -> list[int]:
        res = [-1 for _ in range(len(grid[0]))]
        
        for i in range(len(res)):
            curr = i
            for j in range(len(grid)):
                dir = grid[j][curr]
                if curr + dir < 0 or curr + dir >= len(grid[0]):
                    break
                if grid[j][curr + dir] == -grid[j][curr]:
                    break
                curr = curr + dir
                if j == len(grid) - 1:
                    res[i] = curr
                
        return res

class TestSolution(unittest.TestCase):

    def test_1(self):
        grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
        output = [1,-1,-1,-1,-1]
        self.assertEqual(Solution().find_ball(grid), output)

    def test_2(self):
        grid = [[-1]]
        output = [-1]
        self.assertEqual(Solution().find_ball(grid), output)

    def test_3(self):
        grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
        output = [0,1,2,3,4,-1]
        self.assertEqual(Solution().find_ball(grid), output)

if __name__ == "__main__":
    unittest.main()
