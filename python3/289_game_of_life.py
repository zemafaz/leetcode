import math
import unittest


class Solution:

	@staticmethod
	def gameOfLife(board: list[list[int]]) -> None:
		m = len(board)
		n = len(board[0])

		for i in range(m):
			for j in range(n):
				neighbors = Solution.getNeighbors(i, j, board, m, n)
				alive = neighbors.count(1) + neighbors.count(2)
				
				if (alive < 2 or alive > 3) and board[i][j] == 1:
					board[i][j] = 2
				if alive == 3 and board[i][j] == 0:
					board[i][j] = 3
		
		for i in range(m):
			for j in range(n):
				if board[i][j] > 1:
					board[i][j] = board[i][j] - 2

	@staticmethod
	def getNeighbors(i, j, board, m, n):
		neighbors = []
		
		for k in range(8):
			new_i = int(i + round(math.cos(k*math.pi/4)))
			new_j = int(j + round(math.sin(k*math.pi/4)))

			if -1 < new_i < m and -1 < new_j < n:
				neighbors.append(board[new_i][new_j])
		
		return neighbors

	
class TestSolution(unittest.TestCase):

	def test1(self):
		board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
		Solution.gameOfLife(board)
		self.assertEqual(board, [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])
	
	def test2(self):
		board = [[1,1],[1,0]]
		Solution.gameOfLife(board)
		self.assertEqual(board, [[1,1],[1,1]])


if __name__ == '__main__':
	unittest.main()