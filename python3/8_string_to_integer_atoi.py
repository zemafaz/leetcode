from curses.ascii import is_digit
import unittest

class Solution:
	INT_MAX = 2 ** 31 - 1
	INT_MIN = 2 ** 31

	def my_atoi(self, s:str) -> int:
		leading_space = True
		signal = 0
		num = 0

		for i, e in enumerate(s):
			if not self.is_digit(e):
				if leading_space == False:
					break
				elif signal == 0:
					if e == "+":
						signal = 1
						leading_space = False
					elif e == "-":
						signal = -1
						leading_space = False
				else:
					break
			else:
				if signal == 0:
					signal = 1
				dig = ord(e) - 48
				if self.check_overflow(num, dig, signal) == True:
					return self.INT_MAX if signal == 1 else self.INT_MIN
				num = num * 10 + dig
		return signal * num
				

	def is_digit(self, n: str) -> bool:
		if 48 <= ord(n) <= 57:
			return True
		return False
	
	def check_overflow(self, n: int, d: int, sig: int) -> bool:
		if n >= self.INT_MAX // 10 and sig == 1 and d >= self.INT_MAX % 10:
			return True
		elif n >= self.INT_MIN // 10 and sig == -1 and d >= self.INT_MIN % 10:
			return True
		return 0

class TestSolution(unittest.TestCase):
	def test1(self):
		self.assertEqual(Solution().my_atoi("2147483649"), 2147483647)

	def test2(self):
		self.assertEqual(Solution().my_atoi("      -42"), -42)
	
	def test3(self):
		self.assertEqual(Solution().my_atoi("4193 with words"), 4193)

if __name__ == '__main__':
	unittest.main()

	