import unittest

class Solution:
	def permute_unique(self, nums: list[int]) -> list[list[int]]:
		res = []

		def aux(per: list[int], pool: list[int]):
			if len(pool) == 0:
				if per not in res:
					res.append(per)
				return

			for i in range(len(pool)):
				aux(per + [pool[i]], pool[:i] + pool[i+1:])
		
		aux([], nums)
		return res

class TestSolution(unittest.TestCase):
	def test_1(self):
		nums = [1,1,2]
		res = [[1,1,2], [1,2,1], [2,1,1]]
		self.assertCountEqual(Solution().permute_unique(nums), res)
	
	def test_2(self):
		nums = [1,2,3]
		res = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
		self.assertCountEqual(Solution().permute_unique(nums), res)

if __name__ == "__main__":
	unittest.main()