from collections import defaultdict
import unittest

class Solution:
	def smallest_string_with_swaps(self, s: str, pairs: list[list[int]]) -> str:
		class UF:
			def __init__(self, n): self.p = list(range(n))
			def union(self, x, y): self.p[self.find(x)] = self.find(y)
			def find(self, x):
				if x != self.p[x]: self.p[x] = self.find(self.p[x])
				return self.p[x]
		uf, res, m = UF(len(s)), [], defaultdict(list)
		for x,y in pairs: 
			uf.union(x,y)
		for i in range(len(s)): 
			m[uf.find(i)].append(s[i])
		for comp_id in m.keys(): 
			m[comp_id].sort(reverse=True)
		for i in range(len(s)): 
			res.append(m[uf.find(i)].pop())
		return ''.join(res)

class TestSolution(unittest.TestCase):
	def test_1(self):
		s, pairs = "dcab", [[0,3],[1,2]]
		self.assertEqual(Solution().smallest_string_with_swaps(s, pairs), "bacd")
	
	def test_2(self):
		s, pairs = "dcab", [[0,3],[1,2],[0,2]]
		self.assertEqual(Solution().smallest_string_with_swaps(s, pairs), "abcd")
	
	def test_3(self):
		s, pairs = "cba", [[0,1],[1,2]]
		self.assertEqual(Solution().smallest_string_with_swaps(s, pairs), "abc")

if __name__ == '__main__':
	unittest.main()