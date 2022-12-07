import unittest

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        word += "b"
        VOWELS = "aeiou"
        index = 0
        curr = 0
        res = 0

        for letter in word:
            if letter == VOWELS[index]:
                curr += 1
            elif index < 4 and letter == VOWELS[index + 1]:
                curr += 1
                index += 1
            else:
                if index == 4:
                    res = max(res, curr)
                curr = 0
                index = 0
        
        return res

class TestSolution(unittest.TestCase):

    def test_1(self):
        word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
        output = 13
        self.assertEqual(Solution().longestBeautifulSubstring(word), output)

    def test_2(self):
        word = "aeeeiiiioooauuuaeiou"
        output = 5
        self.assertEqual(Solution().longestBeautifulSubstring(word), output)

    def test_3(self):
        word = "a"
        output = 0
        self.assertEqual(Solution().longestBeautifulSubstring(word), output)

if __name__ == "__main__":
    unittest.main()
