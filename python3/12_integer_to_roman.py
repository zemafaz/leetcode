import unittest

class Solution:
	def int_to_roman(self, num: int) -> str:
		if num >= 4000: return

		SYMBOLS = ['I','V','X','L','C','D','M']

		roman = ''
		i = 0
		
		while(num != 0):
			x = num % 10
			num = num // 10

			if x != 0:
				j = i
				if x >= 5:
					j = i + 1
				x = x % 5
				
				if x == 4:
					roman = SYMBOLS[i] + SYMBOLS[j+1] + roman
				else:
					roman = SYMBOLS[i] * x + roman
					if (j>i):
						roman = SYMBOLS[j] + roman
			i += 2
		return roman

class TestSolution(unittest.TestCase):
	def test_1(self):
		self.assertEqual(Solution().int_to_roman(3), "III")
	
	def test_2(self):
		self.assertEqual(Solution().int_to_roman(58), "LVIII")
	
	def test_3(self):
		self.assertEqual(Solution().int_to_roman(1994), "MCMXCIV")
	
if __name__ == '__main__':
	unittest.main()