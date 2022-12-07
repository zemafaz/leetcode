import unittest

class Solution:
    def find_and_replace_pattern(self, words: list[str], pattern: str) -> list[str]:
        j = 0
        while j != len(words):
            word = words[j]
            d = {}
            for i in range(len(word)):
                c = word[i]
                if c in d.keys():
                    if pattern[i] != d[c]:
                        words.remove(word)
                        j -= 1
                        break
                elif pattern[i] in d.values():
                    words.remove(word)
                    j -= 1
                    break
                else:
                    d[c] = pattern[i] 
            j += 1
        return words

class TestSolution(unittest.TestCase):
    def test_1(self):
        words = ["abc","deq","mee","aqq","dkd","ccc"]
        pattern = "abb"
        output = ["mee","aqq"]
        self.assertEqual(Solution().find_and_replace_pattern(words, pattern), output)

    def test_2(self):
        words = ["a","b","c"]
        pattern = "a"
        output = ["a","b","c"]
        self.assertEqual(Solution().find_and_replace_pattern(words, pattern), output)

if __name__ == "__main__":
    unittest.main()
