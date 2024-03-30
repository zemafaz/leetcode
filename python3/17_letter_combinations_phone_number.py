import unittest

class Solution:
	mapping = {
		"2": "abc",
		"3": "def",
		"4": "ghi",
		"5": "jkl",
		"6": "mno",
		"7": "pqrs",
		"8": "tuv",
		"9": "wxyz"
	}

	def letter_combinations(self, digits:str) -> list[str]:
		res = []
		
		def aux(i, sta):
			if len(digits) == 0: return
			d = digits[i]
			letters = self.mapping[d]
			for e in letters:
				if i == len(digits) - 1:
					res.append(sta + e)
				else:
					aux(i+1, sta + e)

		aux(0, "")
		return res

class TestSolution(unittest.TestCase):
	def test_1(self):
		digits = "23"
		res = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
		self.assertCountEqual(Solution().letter_combinations(digits), res)
	
	def test_2(self):
		digits = ""
		res = []
		self.assertCountEqual(Solution().letter_combinations(digits), res)
	
	def test_3(self):
		digits = "2"
		res = ["a", "b", "c"]
		self.assertCountEqual(Solution().letter_combinations(digits), res)
	
if __name__ == "__main__":
	unittest.main()