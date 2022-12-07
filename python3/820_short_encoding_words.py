import unittest

class Solution:
	def minimum_length_encoding(self, words: list[str]) -> int:
		words.sort(reverse=True)
		words_on_string = []

		for word in words:
			word_len = len(word)
			add_word = True
			for loaded_word in words_on_string:
				if loaded_word[-word_len:] == word:
					add_word = False
					break
			if add_word:
				words_on_string.append(word)

		return len(words_on_string) + len("".join(words_on_string))

class TestSolution(unittest.TestCase):
	def test_1(self):
		words = ["time", "me", "bell"]
		self.assertEqual(Solution().minimum_length_encoding(words), 10)
	
	def test_2(self):
		words = ["t"]
		self.assertEqual(Solution().minimum_length_encoding(words), 2)

if __name__ == '__main__':
	unittest.main()
	