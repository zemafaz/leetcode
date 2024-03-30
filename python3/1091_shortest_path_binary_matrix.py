import unittest

class Solution:
	SURROUNDINGS = [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,0), (-1,-1), (-1,1)]
	def shortest_path_binary_matrix(self, grid: list[list[int]]) -> int:
		if grid[0][0] == 1: return -1

		n, q, ans, visited = len(grid) - 1, [(0,0)], 0, []
		while len(q):
			lvl_len, ans = len(q), ans+1
			for _ in range(lvl_len):
				curr = q.pop(0)
				visited.append(curr)
				if curr == (n,n):
					return ans
				for i in self.SURROUNDINGS:
					x = curr[0] + i[0]
					y = curr[1] + i[1]
					if 0 <= x <= n and 0 <= y <= n:
						if grid[y][x] == 0 and (x,y) not in visited:
							q.append((x,y))
			
		return -1

class TestSolution(unittest.TestCase):
	def test_1(self):
		grid = [[0,1],[1,0]]
		self.assertEqual(Solution().shortest_path_binary_matrix(grid), 2)
	
	def test_2(self):
		grid = [[0,0,0],[1,1,0],[1,1,0]]
		self.assertEqual(Solution().shortest_path_binary_matrix(grid), 4)

	def test_3(self):
		grid = [[1,0,0],[1,1,0],[1,1,0]]
		self.assertEqual(Solution().shortest_path_binary_matrix(grid), -1)

if __name__ == '__main__':
	unittest.main()
