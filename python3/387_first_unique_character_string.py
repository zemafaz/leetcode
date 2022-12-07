from collections import Counter
import unittest

class Solution:
    def first_unique_char(self,s:str) -> int:
        count = Counter(s)

        for i, e in enumerate(count):
            if count[e] == 1:
                return i
        return -1

class TestSolution(unittest.TestCase):
    def test_1(self):
        s="leetcode"
        output=0
        self.assertEqual(Solution().first_unique_char(s),output)

    def test_2(self):
        s="loveleetcode"
        output=2
        self.assertEqual(Solution().first_unique_char(s),output)

    def test_3(self):
        s="aabb"
        output=-1
        self.assertEqual(Solution().first_unique_char(s),output)

if __name__=="__main__":
    unittest.main()
