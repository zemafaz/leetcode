import unittest

class Solution:
	def count_vowel_strings(self, n:int) -> int:
		return ((n+4) * (n+3) * (n+2) * (n+1)) / (4*3*2*1)

class TestSolution(unittest.TestCase):
	def test_1(self):
		n = 1
		res = 5
		self.assertEqual(Solution().count_vowel_strings(n), res)

	def test_2(self):
		n = 2
		res = 15
		self.assertEqual(Solution().count_vowel_strings(n), res)

	def test_3(self):
		n = 33
		res = 66045
		self.assertEqual(Solution().count_vowel_strings(n), res)

if __name__ == '__main__':
	unittest.main()