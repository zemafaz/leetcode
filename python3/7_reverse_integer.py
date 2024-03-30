import unittest

class Solution:
	@staticmethod
	def reverse(x: int) -> int:
		
		sig = 1 if x >= 0 else -1
		rem = abs(x)
		rev = 0

		while rem != 0:
			rev = rev * 10 + rem % 10
			rem = rem // 10
		
		return 0 if rev > 2 ** 31 else sig * rev

class TestSolution(unittest.TestCase):
	def test1(self):
		self.assertEqual(Solution.reverse(123), 321)
	
	def test2(self):
		self.assertEqual(Solution.reverse(-123), -321)

	def test3(self):
		self.assertEqual(Solution.reverse(120), 21)


if __name__ == '__main__':
	unittest.main()