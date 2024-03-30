import unittest

class Solution:
	def combination_sum_3(self, k: int, n: int) -> list[list[int]]:
		res = []

		def aux(rem: list[int], k: int, n: int, stack: list[int]):
			if k < 0 or n < 0:
				return
			if k == 0 and n == 0:
				res.append(stack)
			for i in range(len(rem)):
				aux(rem[i+1:], k-1, n - rem[i], stack + [rem[i]])
		
		aux(list(range(1,9)), k, n, [])

		return res

class TestSolution(unittest.TestCase):
	def test_1(self):
		k = 3
		n = 7
		res = [[1,2,4]]
		self.assertCountEqual(Solution().combination_sum_3(k, n), res)
	
	def test_2(self):
		k = 3
		n = 9
		res = [[1,2,6],[1,3,5],[2,3,4]]
		self.assertCountEqual(Solution().combination_sum_3(k, n), res)
	
	def test_3(self):
		k = 4
		n = 1
		res = []
		self.assertCountEqual(Solution().combination_sum_3(k, n), res)
	
if __name__ == '__main__':
	unittest.main()