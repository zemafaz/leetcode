import unittest

class Solution:
	def longest_common_prefix(self, strs: list[str]) -> str:
		res = ''
		i=0
		
		if len(strs) != 0:
			while True:
				different = False
				for word in strs[1:]:
					if strs[0][i] != word[i] or word[i] == None or strs[0][i] == None:
						different = True
						break
				if different == False:
					res += strs[0][i]
				else:
					break
				i += 1

		return res

	def longest_common_prefix_bin(self, strs: list[str]) -> str:
		smallest = min(strs, key=len)
		left = 0
		middle = round(len(smallest) / 2)
		right = len(smallest)

		res = ""

		while left < middle:
			if Solution().compare_strings(strs, left, middle) == True:
				res += smallest[left:middle]
				left = middle
				middle = (right - middle) / 2
			else:
				right = middle
				middle = (middle - right) / 2		

		return res
		
	
	def compare_strings(self, strs: list[str], left: int, right: int) -> bool:
		if len(strs) != 0:
			ref = strs[0][left:right]
			for word in strs:
				try:
					if word[left:right] != ref:
						return False
				except:
					return False
			return True
		return False
		

class TestSolution(unittest.TestCase):
	def test_1(self):
		self.assertEqual(Solution().longest_common_prefix(["flower","flow","flight"]), "fl")
	
	def test_2(self):
		self.assertEqual(Solution().longest_common_prefix(["dog","racecar","car"]), '')

	def test_1_bin(self):
		self.assertEqual(Solution().longest_common_prefix_bin(["flower","flow","flight"]), "fl")
	
	def test_2_bin(self):
		self.assertEqual(Solution().longest_common_prefix_bin(["dog","racecar","car"]), '')


if __name__ == '__main__':
	unittest.main()