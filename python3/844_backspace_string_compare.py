import unittest

class Solution:
	def backspace_compare(self, s: str, t: str) -> bool:
		s_corr = []
		t_corr = []

		for i in range(max(len(s), len(t))):
			if i < len(s):
				if s[i] == '#':
					s_corr.pop()
				else:
					s_corr.append(s[i])
			if i < len(t):
				if t[i] == '#':
					t_corr.pop()
				else:
					t_corr.append(t[i])
		return s_corr == t_corr

class TestSolution(unittest.TestCase):
	def test_1(self):
		s = "ab#c"
		t = "ad#c"
		self.assertEqual(Solution().backspace_compare(s,t), True)
	
	def test_2(self):
		s = "ab##"
		t = "c#d#"
		self.assertEqual(Solution().backspace_compare(s,t), True)
	
	def test_3(self):
		s = "a#c"
		t = "b"
		self.assertEqual(Solution().backspace_compare(s,t), False)
	
if __name__ == '__main__':
	unittest.main()