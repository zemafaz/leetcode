import unittest

class Solution:
	def is_match(self, s: str, p: str) -> bool:
		p_i = 0

		for s_i in range(len(s)):
			if p_i >= len(p):
				return False
			elif p[p_i] == s[s_i] or p[p_i] == ".":
				p_i += 1
			elif p[p_i] == "*":
				if not (p[p_i - 1] == s[s_i] or p[p_i - 1] == "."):
					p_i += 1
			else:
				if p_i + 1 < len(p):
					if p[p_i] == "*":
						p_i += 1
				else:
					return False

		return True

	def is_match_dp(self, s: str, p: str) -> bool:
		memo = {}

		def dp(i, j):
			if (i, j) not in memo:
				if j == len(p):
					ans = i == len(s)
				else:
					first_match = i < len(s) and p[j] in {s[i], '.'}
					if j + 1 < len(p) and p[j+1] == '*':
						ans = dp(i, j+2) or first_match and dp(i+1, j)
					else:
						ans = first_match and dp(i+1, j+1)
				memo[i, j] = ans
			return memo[i, j]
		
		return dp(0,0)


class TestSolution(unittest.TestCase):
	def test_1(self):
		self.assertEqual(Solution().is_match('aa', 'a'), False)
	
	def test_2(self):
		self.assertEqual(Solution().is_match('aa', 'a*'), True)
	
	def test_3(self):
		self.assertEqual(Solution().is_match('aa', '.*'), True)

	def test_1_dp(self):
		self.assertEqual(Solution().is_match_dp('aa', 'a'), False)
	
	def test_2_dp(self):
		self.assertEqual(Solution().is_match_dp('aa', 'a*'), True)
	
	def test_3_dp(self):
		self.assertEqual(Solution().is_match_dp('aa', '.*'), True)

	
	
if __name__ == '__main__':
	unittest.main()
