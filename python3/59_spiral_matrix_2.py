import unittest

class Solution:
	def generateMatrix(n:int) -> list[list[int]]:
		
		mat = Solution.createMatrix(n)
		
		start_x, start_y, end_x, end_y = 0, 0, n-1, n-1
		step_x, step_y = 1, 0
		x, y = 0, 0

		for i in range(n*n):
			mat[y][x] = i + 1

			if step_y == 0:
				if x == end_x and y == start_y:
					step_x = 0
					step_y = 1
					start_y += 1
				elif x == start_x and y == end_y:
					step_x = 0
					step_y = -1
					end_y -= 1
			elif step_x == 0:
				if x == start_x and y == start_y:
					step_y = 0
					step_x = 1
					start_x += 1
				elif x == end_x and y == end_y:
					step_y = 0
					step_x = -1
					end_x -= 1

			x += step_x
			y += step_y

		return mat

	def createMatrix(n: int) -> list[list[int]]:
		return [[0] * n for _ in range(n)]


class TestSolution(unittest.TestCase):

	def test1(self):
		self.assertEqual(Solution.generateMatrix(3), [[1,2,3],[8,9,4],[7,6,5]])

	def test2(self):
		self.assertEqual(Solution.generateMatrix(1), [[1]])

if __name__ == '__main__':
	unittest.main()