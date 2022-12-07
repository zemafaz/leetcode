import unittest

class Solution:

	@staticmethod
	def shiftGrid(grid: list[list[int]], k: int) -> list[list[int]]:
		
		m = len(grid)
		n = len(grid[0])
		new_grid = [[None for _ in range(n)] for _ in range(m)]
		
		for x, row in enumerate(grid):
			for y, element in enumerate(row):
				new_y = (y + k) % n
				new_x = (x + (y + k) // m) % m

				new_grid[new_x][new_y] = element

		return new_grid

class TestSolution(unittest.TestCase):

	def test1(self):
		self.assertEqual(Solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1), [[9,1,2],[3,4,5],[6,7,2]])
	
	def test2(self):
		self.assertEqual(Solution.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4), [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]])

	def test3(self):
		self.assertEqual(Solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9), [[1,2,3],[4,5,6],[7,8,9]])


if __name__ == '__main__':
	unittest.main()


# assert Solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1) == [[9,1,2],[3,4,5],[6,7,8]], "Test 1 Failed"