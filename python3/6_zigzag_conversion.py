import unittest

class Solution:
	@staticmethod
	def convert_sort(s: str, numRows: int) -> str:

		if numRows == 1 or numRows >= len(s):
			return s
		
		result = [''] * numRows
		index, step = 0, 1

		for c in s:
			result[index] += c
			if index == 0:
				step = 1
			elif index == numRows - 1:
				step = -1
			index += step

		return ''.join(result)

class TestSolution(unittest.TestCase):

	def test1_sort(self):
		self.assertEqual(Solution.convert_sort("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
	
	def test2_sort(self):
		self.assertEqual(Solution.convert_sort("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
	
	def test3_sort(self):
		self.assertEqual(Solution.convert_sort("A", 1), "A")

if __name__ == '__main__':
	unittest.main()