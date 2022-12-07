import unittest

class Solution:
	def hamming_weight(self, n: int) -> int:
		res = 0

		while n != 0:
			if n % 2 == 1:
				res += 1
			n = n >> 1
		
		return res
	
	def hamming_weight_built_in(self, n: int):
		return n.bit_count()
		#return bin(n).count('1')

class TestSolution(unittest.TestCase):
	def test_1(self):
		n = 0b00000000000000000000000000001011
		self.assertEqual(Solution().hamming_weight(n),3)
	
	def test_2(self):
		n = 0b0000000000000000000000010000000
		self.assertEqual(Solution().hamming_weight(n),1)
	
	def test_3(self):
		n = 0b11111111111111111111111111111101
		self.assertEqual(Solution().hamming_weight(n),31)
	
	def test_1_built_in(self):
		n = 0b00000000000000000000000000001011
		self.assertEqual(Solution().hamming_weight_built_in(n),3)
	

if __name__ == '__main__':
	unittest.main()
	

