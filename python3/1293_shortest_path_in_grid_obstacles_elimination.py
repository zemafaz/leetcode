import unittest
from collections import deque

class Solution:

    def shortestPath(self, grid: list[list[int]], k: int) -> int:

        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        queue = deque([(0,0,k,int(0))])
        visited = set([(0,0,k)])

        if k > len(grid) - 1 + len(grid[0]) - 1:
            return len(grid) - 1 + len(grid[0]) - 1

        while queue:
            row, col, eliminate, steps = queue.popleft()
            for new_row, new_col in [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]:
                if (new_row >= 0 and
                        new_row < len(grid) and
                        new_col >= 0  and
                        new_col < len(grid[0])):
                    if (grid[new_row][new_col] == 1 and eliminate > 0 and
                            (new_row, new_col, eliminate - 1) not in visited):
                        visited.add((new_row, new_col, eliminate - 1))
                        queue.append((new_row, new_col, eliminate - 1, steps + 1))
                    if grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
                        if new_row == len(grid) - 1 and new_col == len(grid[0]) - 1:
                            return steps + 1
                        visited.add((new_row, new_col, eliminate))
                        queue.append((new_row, new_col, eliminate, steps + 1))
        return -1

class TestSolution(unittest.TestCase):

    def test_1(self):
        grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
        k = 1
        output = 6
        self.assertEqual(Solution().shortestPath(grid, k), output)

    def test_2(self):
        grid = [[0,1,1],[1,1,1],[1,0,0]]
        k = 1
        output = -1
        self.assertEqual(Solution().shortestPath(grid, k), output)

if __name__ == "__main__":
    unittest.main()
