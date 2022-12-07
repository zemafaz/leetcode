import unittest
from collections import Counter

class Solution:
    def min_deletions(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        used = set()
        for ch, freq in counter.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "aab"
        self.assertEqual(Solution().min_deletions(s), 0)
    
    def test_2(self):
        s = "aaabbbcc"
        self.assertEqual(Solution().min_deletions(s), 2)
    
    def test_3(self):
        s = "ceabaacb"
        self.assertEqual(Solution().min_deletions(s), 2)

if __name__ == '__main__':
    unittest.main()   