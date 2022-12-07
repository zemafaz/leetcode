import unittest
from collections import Counter

class Solution:

    def top_k_frequent(self, words: list[str], k: int) -> list[str]:
        counter = Counter(words)
        return list(map(lambda x: x[0], counter.most_common(k)))

class TestSolution(unittest.TestCase):

    def test_1(self):
        words = ["i","love","leetcode","i","love","coding"]
        k = 2
        output = ["i","love"]
        self.assertEqual(Solution().top_k_frequent(words, k), output)

    def test_2(self):
        words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
        k = 4
        output = ["the","is","sunny","day"]
        self.assertEqual(Solution().top_k_frequent(words, k), output)

if __name__ == "__main__":
    unittest.main()
