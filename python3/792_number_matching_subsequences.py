import unittest

class Solution:
    def num_matching_subseq(self, s: str, words: list[str]) -> str:
        res = 0
        for w in words:
            j = -1
            for i in range(len(w)):
                while j < len(s) - 1:
                    j += 1
                    if w[i] == s[j]:
                        if i == len(w) - 1:
                            res += 1
                        break
                if j == len(s) - 1:
                    break
        return res

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "abcde"
        words = ["a","bb","acd","ace"]
        self.assertEqual(Solution().num_matching_subseq(s, words), 3)

    def test_2(self):
        s = "dsahjpjauf"
        words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
        self.assertEqual(Solution().num_matching_subseq(s, words), 2)

if __name__ == "__main__":
    unittest.main()