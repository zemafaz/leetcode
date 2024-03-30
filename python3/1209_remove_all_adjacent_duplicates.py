import unittest

class Solution:
	def remove_duplicates(self, s: str, k:int) -> str:
		removed = True

		while removed:
			removed = False
			last_char = ""
			n = 1
			i = 0
			while i < len(s):
				if s[i] == last_char:
					n += 1
				else:
					if n >= k:
						j = i - k
						s = s[:j] + s[i:]
						i = i - k
						removed = True
					last_char = s[i]
					n = 1
				i += 1
		
		return s
	
	def remove_duplicates_stack(self, s:str, k: int) -> str:
		stack = [["#", 0]]

		for c in s:
			if stack[-1][0] == c:
				stack[-1][1] += 1
				if stack[-1][1] == k:
					stack.pop()
			else:
				stack.append([c,1])
		
		return "".join(c*k for c, k in stack)

class TestSolution(unittest.TestCase):
	def test_1(self):
		s, k = "abcd", 2
		self.assertEqual(Solution().remove_duplicates(s, k), "abcd")

	def test_2(self):
		s, k = "deeedbbcccbdaa", 3
		self.assertEqual(Solution().remove_duplicates(s, k), "aa")

	def test_3(self):
		s, k = "pbbcggttciiippooaais", 2
		self.assertEqual(Solution().remove_duplicates(s, k), "ps")

	def test_1_stack(self):
		s, k = "abcd", 2
		self.assertEqual(Solution().remove_duplicates_stack(s, k), "abcd")

	def test_2_stack(self):
		s, k = "deeedbbcccbdaa", 3
		self.assertEqual(Solution().remove_duplicates_stack(s, k), "aa")

	def test_3_stack(self):
		s, k = "pbbcggttciiippooaais", 2
		self.assertEqual(Solution().remove_duplicates_stack(s, k), "ps")

if __name__ == "__main__":
	unittest.main()