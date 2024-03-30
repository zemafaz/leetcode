from math import factorial
import unittest

class Solution:
	def unique_paths(self, m: int, n: int) -> int:
		n_steps = m + n - 2
		return factorial(n_steps) / (factorial(m-1) * factorial(n_steps - m + 1))

	def unique_paths_rec(self, m: int, n: int) -> int:
		def dfs(i,j):
			if i >= m or j >= n:
				return 0
			if i == m-1 and j == n-1:
				return 1
			return dfs(i+1, j) + dfs(i, j+1)
		return dfs(0,0)
	
	def unique_paths_dyn(self, m: int, n: int) -> int:
		dp = [[1]*n for _ in range(m)]
		for i in range(1,m):
			for j in range(1, n):
				dp[i][j] = dp[i][j-1]+ dp[i-1][j]
		return dp[-1][-1]

class TestSolution(unittest.TestCase):
	def test_1(self):
		self.assertEqual(Solution().unique_paths(3, 7), 28)
	
	def test_2(self):
		self.assertEqual(Solution().unique_paths(3,2), 3)
	
	def test_1_rec(self):
		self.assertEqual(Solution().unique_paths_rec(3, 7), 28)
	
	def test_2_rec(self):
		self.assertEqual(Solution().unique_paths_rec(3,2), 3)
	
	def test_1_dyn(self):
		self.assertEqual(Solution().unique_paths_dyn(3, 7), 28)
	
	def test_2_dyn(self):
		self.assertEqual(Solution().unique_paths_dyn(3,2), 3)
	

if __name__ == '__main__':
	unittest.main()