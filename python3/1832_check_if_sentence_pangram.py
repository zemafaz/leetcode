import unittest
import string

class Solution:

    def check_if_pangram(self, sentence: str) -> bool:
        alphabet = set(string.ascii_lowercase)
        for char in sentence:
            alphabet.discard(char)
            if len(alphabet) == 0:
                return True
        return False

class TestSolution(unittest.TestCase):

    def test_1(self):
        sentence = "thequickbrownfoxjumpsoverthelazydog"
        output = True
        self.assertEqual(Solution().check_if_pangram(sentence), output)

    def test_2(self):
        sentence = "leetcode"
        output = False
        self.assertEqual(Solution().check_if_pangram(sentence), output)

if __name__ == "__main__":
    unittest.main()
