import unittest

class Solution:
	def is_palindrome(self, x: int) -> bool:
		if x < 0: return False
		rev = int(str(x)[::-1])
		return x == rev

	def is_palindrome_no_str(self, x: int) -> bool:
		if x < 0 or (x % 10 == 0 and x != 0): return False
		
		rev = 0

		while x > rev:
			rev = rev * 10 + x % 10
			x = x // 10
		
		return x == rev or x == rev // 10



class TestSolution(unittest.TestCase):
	def test1(self):
		self.assertEqual(Solution().is_palindrome(121), True)
	
	def test2(self):
		self.assertEqual(Solution().is_palindrome(-121), False)
	
	def test3(self):
		self.assertEqual(Solution().is_palindrome(10), False)

	def test1NoStr(self):
		self.assertEqual(Solution().is_palindrome_no_str(121), True)
	
	def test2NoStr(self):
		self.assertEqual(Solution().is_palindrome_no_str(-121), False)
	
	def test3NoStr(self):
		self.assertEqual(Solution().is_palindrome_no_str(10), False)

if __name__ == "__main__":
	unittest.main()
	
	