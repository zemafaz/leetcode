import unittest

class Solution():
    def word_subsets(self, words1: list[str], words2: list[str]) -> list[str]:
        def aux(w1, i, w2):
            for c in w1[i]:
                for j in range(len(w2)):
                    if c in w2[j]:
                        k = w2[j].index(c)
                        w2[j] = w2[j][:k]+w2[j][k+1:]
            if w2.count("") != len(w2):
                w1 = w1[:i]+w1[i+1:]
                i -= 1
            return (w1, i)

        i = 0
        while i != len(words1):
            words1, i = aux(words1, i, words2.copy())
            i += 1
        return words1

class TestSolution(unittest.TestCase):
    def test_1(self):
        words1 = ["amazon","apple","facebook","google","leetcode"]
        words2 = ["e","o"]
        output = ["facebook","google","leetcode"]
        self.assertEqual(Solution().word_subsets(words1, words2), output)

    def test_2(self):
        words1 = ["amazon","apple","facebook","google","leetcode"]
        words2 = ["l","e"]
        output = ["apple","google","leetcode"]
        self.assertEqual(Solution().word_subsets(words1, words2), output)

if __name__ == '__main__':
    unittest.main()
