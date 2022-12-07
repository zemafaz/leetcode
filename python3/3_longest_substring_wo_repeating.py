import unittest

class Solution:

	@staticmethod
	def lengthOfLongestSubstring(s: str) -> int:
		max_l = 0
	
		for i in range(len(s) - 1):
			dict = {s[i]}

			for j in range(i + 1, len(s)):
				if s[j] in dict or j+1 == len(s):
					if max_l < j - i:
						max_l = j - i
					break
				else:
					dict.add(s[j])
		
		return max_l

	@staticmethod
	def optimal(s: str) -> int:
		max_l = 0
		dict = {}

		i = 0

		for j in range(len(s)):
			if s[j] in dict:
				i = dict[s[j]]
			
			max_l = max(max_l, j - i + 1)
			dict[s[j]] = j + 1
		
		return max_l


class TestSolution(unittest.TestCase):

	def test1(self):
		# self.assertEqual(Solution.lengthOfLongestSubstring('abcabcbb'), 3)
		self.assertEqual(Solution.optimal('abcabcbb'), 3)

	
	def test2(self):
		# self.assertEqual(Solution.lengthOfLongestSubstring('bbbbb'), 1)
		self.assertEqual(Solution.optimal('bbbbb'), 1)
	
	def test3(self):
		# self.assertEqual(Solution.lengthOfLongestSubstring('pwwkew'), 3)
		self.assertEqual(Solution.optimal('pwwkew'), 3)


if __name__ == '__main__':
	unittest.main()