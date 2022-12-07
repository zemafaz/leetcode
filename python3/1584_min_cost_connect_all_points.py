import unittest
from tree_node import TreeNode

class Solution:
	def min_cost_connect_points(self, points: list[list[int]]) -> int:
		res = 0
		lines = [None] * (len(points) - 1)

		for i in range(len(points) - 1):
			min_dis = None
			for j, _ in enumerate(points):
				if i != j and (j, i) not in lines:
					man_dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
					if min_dis == None or man_dis < min_dis:
						min_dis = man_dis
						lines[i] = (i, j)
			res += min_dis
		return res
	
		

class TestSolution(unittest.TestCase):
	def test_1(self):
		points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
		self.assertEqual(Solution().min_cost_connect_points(points), 20)
	
	def test_2(self):
		points = [[3,12],[-2,5],[-4,1]]
		self.assertEqual(Solution().min_cost_connect_points(points), 18)
	
if __name__ == '__main__':
	unittest.main()