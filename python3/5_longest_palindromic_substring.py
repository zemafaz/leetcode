import unittest

class Solution:
	@staticmethod
	def longestPalindrome(s: str) -> str:
		palindrome = s[0]

		for i in range(len(s)):
			if i+1 < len(s):
				for j in range(len(s)-1, i, -1):
					subs = s[i:j]
					if Solution.verifyPalindrome(subs) == True:
						if len(subs) > len(palindrome):
							palindrome = subs
						break
			else:
				break
		return palindrome

	@staticmethod
	def verifyPalindrome(s1: str) -> bool:
		return s1 == s1[::-1]

class TestSolution(unittest.TestCase):

	def test1(self):
		self.assertIn(Solution.longestPalindrome("babad"), ["bab","aba"])
	
	def test2(self):
		self.assertEqual(Solution.longestPalindrome("cbbd"), "bb")

if __name__ == '__main__':
	unittest.main()
	